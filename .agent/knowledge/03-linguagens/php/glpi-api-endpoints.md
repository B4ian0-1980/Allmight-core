---json
{
  "id": "glpi-api-endpoints",
  "title": "Mapeamento de Operações → Endpoints GLPI REST API",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Base URL:** `https://{servidor}/apirest.php` **Headers obrigatórios em todas as requisições:**",
  "gatilhos": [
    "api",
    "endpoints",
    "glpi",
    "linguagens",
    "mapeamento",
    "php",
    "rest"
  ],
  "perguntas_tipo": [
    "Como utilizar Mapeamento de Operações → Endpoints GLPI REST API?",
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

# Mapeamento de Operações → Endpoints GLPI REST API

> **Base URL:** `https://{servidor}/apirest.php`  
> **Headers obrigatórios em todas as requisições:**
> ```
> App-Token: {app_token}
> Session-Token: {session_token}
> Content-Type: application/json
> ```

---

## 1. Autenticação

### 1.1 Iniciar Sessão
Executado no início de **toda** interação antes de qualquer consulta.

```
GET /apirest.php/initSession
```

**Headers:**
```
Authorization: Basic {base64(usuario:senha)}
App-Token: {app_token}
```

**Resposta:**
```json
{ "session_token": "abc123xyz" }
```

**Quando usar:** Ao receber qualquer mensagem do WhatsApp, antes de consultar usuário ou criar ticket.

---

### 1.2 Encerrar Sessão
Executado ao final do fluxo ou quando o usuário clica em **❌ Encerrar**.

```
GET /apirest.php/killSession
```

**Quando usar:** Logout explícito, timeout de sessão ou encerramento do bot.

---

## 2. Gestão de Usuários

### 2.1 Buscar Usuário por Número de Celular
Primeira consulta ao identificar número WhatsApp recebido.

```
GET /apirest.php/User?searchText[mobile]={numero}
```

**Parâmetros:**
| Parâmetro | Valor | Descrição |
|---|---|---|
| `searchText[mobile]` | `5511999999999` | Número normalizado (somente dígitos) |

**Resposta (encontrado):**
```json
[{ "id": 42, "name": "joao.silva", "firstname": "João", "realname": "Silva" }]
```

**Resposta (não encontrado):**
```json
[]
```

---

### 2.2 Buscar Usuário por Matrícula
Executado quando número não é encontrado e usuário informa a matrícula.

```
GET /apirest.php/User?searchText[registration_number]={matricula}
```

**Parâmetros:**
| Parâmetro | Valor | Descrição |
|---|---|---|
| `searchText[registration_number]` | `12345` | Matrícula funcional |

---

### 2.3 Carregar Dados Completos do Usuário
Executado após localizar o `id` do usuário, para carregar dados de confirmação de identidade.

```
GET /apirest.php/User/{id}?expand_dropdowns=true
```

**Campos retornados relevantes:**
| Campo GLPI | Uso no bot |
|---|---|
| `firstname` | Primeiro nome — validação identidade |
| `realname` | Sobrenome — validação identidade |
| `mobile` | Número celular cadastrado |
| `phone` | Telefone fixo |
| `phone2` | Telefone alternativo |
| `registration_number` | Matrícula — validação identidade |
| `entities_id` | Entidade/setor do servidor |

---

### 2.4 Buscar E-mails do Usuário

```
GET /apirest.php/User/{id}/UserEmail
```

**Resposta:**
```json
[
  { "id": 1, "users_id": 42, "email": "joao@org.gov.br", "is_default": 1 }
]
```

---

### 2.5 Criar Novo Usuário
Executado ao final do fluxo de **cadastro novo** (servidor encontrado no CSV mas inexistente no GLPI).

```
POST /apirest.php/User/
```

**Body:**
```json
{
  "input": {
    "name": "joao.silva",
    "firstname": "João",
    "realname": "Silva",
    "mobile": "5511999999999",
    "phone": "551133334444",
    "phone2": "",
    "registration_number": "12345",
    "entities_id": 5,
    "_useremails": ["joao.silva@org.gov.br"]
  }
}
```

**Resposta:**
```json
{ "id": 43, "message": "Item successfully added" }
```

---

### 2.6 Atualizar Número de Celular do Usuário
Executado ao final do fluxo de **recuperação de conta** (servidor acerta as perguntas de segurança e está acessando de número diferente).

```
PUT /apirest.php/User/{id}
```

**Body:**
```json
{
  "input": {
    "mobile": "5521988887777"
  }
}
```

---

## 3. Entidades e Setores

### 3.1 Listar Entidades do Usuário Autenticado
Usado para montar os botões de seleção de setor na confirmação de identidade.

```
GET /apirest.php/getMyEntities?is_recursive=true
```

**Resposta:**
```json
{
  "myentities": [
    { "id": 1, "name": "Prefeitura Municipal" },
    { "id": 5, "name": "Secretaria de Saúde" }
  ]
}
```

---

### 3.2 Listar Todas as Entidades
Usado para montar os botões de seleção de entidade no cadastro de novo usuário.

```
GET /apirest.php/Entity?range=0-99
```

**Parâmetros opcionais:**
| Parâmetro | Valor | Descrição |
|---|---|---|
| `range` | `0-99` | Paginação |
| `expand_dropdowns` | `true` | Expande campos relacionais |

---

## 4. Abertura de Chamados

### 4.1 Buscar Categorias de Chamado
Executado antes de abrir chamado, lista as categorias disponíveis para envio à IA de classificação.

```
GET /apirest.php/ITILCategory?expand_dropdowns=true&range=0-999
```

**Resposta:**
```json
[
  { "id": 3, "name": "Hardware", "completename": "TI > Hardware" },
  { "id": 5, "name": "Computador", "completename": "TI > Hardware > Computador" }
]
```

**Quando usar:** Uma vez por sessão ou quando o usuário acessa o fluxo de abertura de chamado.

---

### 4.2 Criar Chamado
Executado após o usuário confirmar o resumo do chamado.

```
POST /apirest.php/Ticket/
```

**Body:**
```json
{
  "input": {
    "name": "Título resumido gerado pela IA",
    "content": "Descrição completa digitada pelo servidor",
    "itilcategories_id": 5,
    "entities_id": 5,
    "urgency": 3,
    "impact": 3,
    "priority": 3,
    "type": 1,
    "_users_id_requester": 42
  }
}
```

**Mapa de valores:**

| Campo | Valores |
|---|---|
| `type` | `1` = Incidente · `2` = Requisição |
| `urgency` / `impact` / `priority` | `1` = Muito Alta · `2` = Alta · `3` = Média · `4` = Baixa · `5` = Muito Baixa |
| `status` | `1` = Novo · `2` = Em Processamento · `3` = Atribuído · `4` = Pendente · `5` = Resolvido · `6` = Fechado |

**Resposta:**
```json
{ "id": 1234, "message": "Item successfully added" }
```

---

## 5. Consulta e Acompanhamento de Chamados

### 5.1 Listar Chamados Abertos do Servidor
Executado ao selecionar **📋 Consultar meus Chamados** no menu principal.

```
GET /apirest.php/search/Ticket
```

**Parâmetros:**
```
?criteria[0][field]=4
&criteria[0][searchtype]=equals
&criteria[0][value]={glpi_user_id}
&criteria[1][link]=AND
&criteria[1][field]=12
&criteria[1][searchtype]=notequals
&criteria[1][value]=6
&forcedisplay[0]=2
&forcedisplay[1]=12
&forcedisplay[2]=15
&forcedisplay[3]=4
```

**Mapa de campos (`field`):**
| field | Coluna |
|---|---|
| `2` | ID do chamado |
| `4` | Solicitante |
| `12` | Status |
| `15` | Data de abertura |
| `21` | Descrição |
| `80` | Entidade |

**Resposta:**
```json
{
  "data": [
    { "2": 1234, "12": 2, "15": "2025-06-01 09:00:00" }
  ]
}
```

---

### 5.2 Detalhar Chamado Específico
Executado quando o servidor clica em um chamado da lista.

```
GET /apirest.php/Ticket/{id}?expand_dropdowns=true
```

**Campos retornados relevantes:**
| Campo | Descrição |
|---|---|
| `id` | Número do chamado |
| `name` | Título |
| `content` | Descrição |
| `status` | Status atual (numérico) |
| `date` | Data de abertura |
| `date_mod` | Última atualização |
| `itilcategories_id` | Categoria |
| `urgency` / `priority` | Urgência / Prioridade |

---

### 5.3 Listar Acompanhamentos (Follow-ups) do Chamado

```
GET /apirest.php/Ticket/{id}/ITILFollowup
```

**Resposta:**
```json
[
  {
    "id": 10,
    "items_id": 1234,
    "content": "Técnico verificando o equipamento",
    "date": "2025-06-02 14:30:00",
    "users_id": 8
  }
]
```

---

### 5.4 Adicionar Follow-up (Comentário) ao Chamado
Executado quando o servidor digita um comentário em um chamado existente.

```
POST /apirest.php/ITILFollowup/
```

**Body:**
```json
{
  "input": {
    "items_id": 1234,
    "itemtype": "Ticket",
    "content": "Texto do comentário digitado pelo servidor"
  }
}
```

---

### 5.5 Atualizar Status do Chamado

```
PUT /apirest.php/Ticket/{id}
```

**Body:**
```json
{
  "input": {
    "status": 5
  }
}
```

---

## 6. Documentos e Anexos

### 6.1 Enviar Documento (Anexo)

```
POST /apirest.php/Document/
Content-Type: multipart/form-data
```

**Form data:**
```
uploadManifest: {
  "input": {
    "name": "Nome do arquivo",
    "entities_id": 5
  }
}
file: [binário do arquivo]
```

**Resposta:**
```json
{ "id": 99, "message": "Item successfully added", "upload_result": { "filename": "arquivo.pdf" } }
```

---

### 6.2 Vincular Documento a um Chamado

```
POST /apirest.php/Document_Item/
```

**Body:**
```json
{
  "input": {
    "documents_id": 99,
    "items_id": 1234,
    "itemtype": "Ticket"
  }
}
```

---

## 7. Mapeamento Resumido por Etapa do Bot

| Etapa | Método | Endpoint |
|---|---|---|
| Início de qualquer interação | `GET` | `/initSession` |
| Buscar usuário pelo número | `GET` | `/User?searchText[mobile]={numero}` |
| Buscar usuário pela matrícula | `GET` | `/User?searchText[registration_number]={mat}` |
| Carregar dados do usuário | `GET` | `/User/{id}?expand_dropdowns=true` |
| Carregar e-mails do usuário | `GET` | `/User/{id}/UserEmail` |
| Criar novo usuário | `POST` | `/User/` |
| Atualizar número do usuário | `PUT` | `/User/{id}` |
| Listar entidades disponíveis | `GET` | `/getMyEntities?is_recursive=true` |
| Listar todas as entidades | `GET` | `/Entity?range=0-99` |
| Listar categorias para IA | `GET` | `/ITILCategory?expand_dropdowns=true` |
| Criar chamado | `POST` | `/Ticket/` |
| Listar chamados do servidor | `GET` | `/search/Ticket?criteria...` |
| Detalhar chamado | `GET` | `/Ticket/{id}?expand_dropdowns=true` |
| Listar follow-ups | `GET` | `/Ticket/{id}/ITILFollowup` |
| Adicionar comentário | `POST` | `/ITILFollowup/` |
| Atualizar status do chamado | `PUT` | `/Ticket/{id}` |
| Enviar anexo | `POST` | `/Document/` |
| Vincular anexo ao chamado | `POST` | `/Document_Item/` |
| Encerrar sessão | `GET` | `/killSession` |

---

## 8. Tratamento de Erros Comuns

| HTTP Status | Significado | Ação no bot |
|---|---|---|
| `200` | Sucesso | Prosseguir fluxo |
| `201` | Criado com sucesso | Confirmar criação ao usuário |
| `400` | Dados inválidos | Solicitar nova entrada |
| `401` | Não autenticado | Re-executar `/initSession` |
| `403` | Sem permissão | Mensagem de erro + suporte |
| `404` | Não encontrado | Tratar como "não existe" |
| `500` | Erro interno GLPI | Mensagem de indisponibilidade + retry |

---

## 9. Notas de Implementação

- **Session-Token** expira. Sempre verificar retorno `401` e renovar via `/initSession`.
- O campo `mobile` no GLPI deve ser normalizado em formato E.164 sem `+` — ex: `5511999999999`.
- O endpoint `/search/Ticket` usa índices numéricos de campo (`field`), não nomes de coluna.
- `expand_dropdowns=true` retorna nomes legíveis em vez de IDs nos campos relacionais.
- Para paginação usar `range=0-49` (máximo recomendado: 50 registros por página).
- O `entities_id` do usuário deve corresponder ao `entities_id` do chamado criado.
