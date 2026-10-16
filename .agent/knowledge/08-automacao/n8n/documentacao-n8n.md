---json
{
  "id": "documentacao-n8n",
  "title": "🤖 n8n - Workflow Automation & API",
  "categoria": "08-automacao",
  "subcategoria": "n8n",
  "resumo": "**Classificação:** Integrações / Automação / iPaaS **Status:** Documentação de Referência",
  "gatilhos": [
    "api",
    "automacao",
    "automation",
    "documentacao",
    "n8n",
    "workflow"
  ],
  "perguntas_tipo": [
    "Como utilizar 🤖 n8n - Workflow Automation & API?",
    "Quais as boas praticas de n8n?"
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
  "dono": "stack-n8n",
  "prioridade": 2
}
---

# 🤖 n8n - Workflow Automation & API

> **Classificação:** Integrações / Automação / iPaaS
> **Status:** Documentação de Referência
> **Data de Adição:** 16/02/2026

## 📄 Visão Geral

n8n (Nodemation) é uma ferramenta de automação de fluxo de trabalho "expansível" e baseada em nós. Ela permite conectar qualquer coisa a tudo via API, webhook ou os milhares de nós nativos.

Embora o uso principal do n8n seja visual (arrastar e soltar nós), ele possui uma **Public REST API** poderosa para gestão programática da instância (criar workflows, gerenciar usuários, verificar execuções).

---

## 📚 Documentação Técnica (Public API)

**Fonte Oficial:** [n8n API Reference](https://docs.n8n.io/api/)

### 🔑 Autenticação

* [API Key Authentication](https://docs.n8n.io/api/authentication/): Como gerar e usar chaves de API (`X-N8N-API-KEY`).

### 🛠️ Recursos Principais da API

A API pública permite controlar a própria infraestrutura do n8n externamente:

* **Workflows:**
  * `GET /workflows`: Listar todos os fluxos.
  * `POST /workflows`: Criar um novo fluxo via JSON.
  * `POST /workflows/{id}/activate`: Ativar/Desativar fluxos.
* **Execuções (Logs):**
  * `GET /executions`: Consultar histórico de execuções (sucesso/erro).
  * `GET /executions/{id}`: Ver detalhes de uma execução específica (dados de entrada/saída).
* **Credenciais:**
  * `GET /credentials`: Listar credenciais cadastradas.
  * `POST /credentials`: Criar novas credenciais via API.
* **Gestão de Usuários (Enterprise/Cloud):**
  * Endpoints para convidar e gerenciar permissões de usuários.

---

## 🔗 Integração Inversa (Webhook Node)

Além de controlar o n8n via API, a forma mais comum de integração é o n8n **receber** dados.

* **Webhook Node:** Cria um endpoint HTTP (GET/POST) dentro do fluxo.
  * *Uso:* Seu sistema (Laravel) envia um POST para `https://n8n.seuservidor.com/webhook/entidade-atualizada`.
  * O n8n recebe o JSON, processa (ex: formata, envia para WAHA, salva no GLPI) e retorna uma resposta.

## 💡 Cenários de Uso (GPMC/Smart/Ceresta)

1. **Monitoramento de Falhas:**
    * Monitorar o endpoint `/executions` do n8n via script PHP. Se houver falhas consecutivas em fluxos críticos, alertar a TI.
2. **Versionamento de Fluxos:**
    * Criar um script que faz backup diário de todos os workflows (`GET /workflows`) e salva em JSON no Git.
3. **Criação Dinâmica:**
    * Um painel administrativo onde o usuário configura uma integração e o sistema cria o workflow correspondente no n8n via API (`POST /workflows`).

---

## ⚠️ Dica de Segurança

---

## 📂 Exemplos de Workflow (JSON)

Foram arquivados exemplos práticos de fluxos na pasta `exemplos/`. Para usar, basta importar o JSON no n8n:

1. **WHATSAPP ABERTURA + CONSULTA + IA FUNCIONAL (1).json**: Exemplo complexo integrando WhatsApp e IA.
2. **My workflow 3 (10) (1).json**: Fluxo genérico (validar conteúdo ao importar).

### 9. `WORKFLOW_SUPORTE_V8_MENU_DINAMICO.json` (Zero Digitação)

* **Descrição:** Menu Dinâmico via API + Abertura Rápida.
* **Destaque (Zero Typing):**
    1. **Lista:** Seleciona Categoria ITIL (do GLPI).
    2. **Botões:** Seleciona Urgência (🟢 Baixa, 🟡 Média, 🔴 Alta).
    3. **Botões:** "🚀 Enviar Agora" (Usa título padrão) ou "📝 Detalhar".
    4. **Resultado:** Permite abrir um chamado em 3 toques, sem digitar nenhuma palavra.

### 10. `WORKFLOW_SUPORTE_V9_IA_CLASSIFICACAO.json` (IA Generativa)

* **Descrição:** Classificação e Filtragem Inteligente via IA.
* **Funcionamento (Smart):**
    1. O usuário descreve o problema primeiro (ex: "Minha impressora não está puxando papel").
    2. O **Bot (IA)** analisa o texto e cruza com as 50+ categorias do GLPI.
    3. Apresenta para o usuário apenas as **3 Categorias Mais Prováveis** (ex: *Impressoras HP*, *Suprimentos*, *Atolamento*).
    4. **Urgência Automática:** A IA define o nível de prioridade (1 a 5) baseado na gravidade do relato, sem perguntar ao usuário.
    5. O chamado é aberto com 1 clique de confirmação.

### 11. `WORKFLOW_SUPORTE_IDENTIFICADO_V7_SECURE_UPDATE.json` (Premium)

* **Descrição:** Fluxo com **Upgrade de Segurança** (Pós-Validação).
* **Recurso Extra:**
  * Após o usuário validar sua identidade pela primeira vez (via Matrícula + Nome/Sobrenome + Admissão), o bot oferece:
  * *"Deseja cadastrar **Nome da Mãe** e **Aniversário** para facilitar sua recuperação no futuro?"*
  * Se o usuário aceitar, esses dados são salvos no perfil dele no GLPI.
  * Nas próximas vezes, ele pode usar essas informações secretas para uma recuperação ágil.

### 12. `WORKFLOW_MASTER_ROTEADOR.json` (O Cérebro Central)

* **Descrição:** Orquestrador que conecta tudo.
* **Funcionamento:**
    1. Recebe a mensagem do WhatsApp (Porta de Entrada Única).
    2. Verifica: "Esse telefone existe no GLPI?"
    3. **Sim:** Encaminha para o **V9** (Atendimento direto).
    4. **Não:** Encaminha para o **V7** (Recuperação de Acesso).
* **Dica:** Ao subir para produção, você só precisa configurar o Webhook do WhatsApp para apontar para ESTE fluxo.

### 13. `WORKFLOW_EVOLUTION_V9_IA_CLASSIFICACAO.json` (Exclusivo Evolution API)

* **Descrição:** Versão do fluxo de IA adaptada para **Evolution API**.
* **Localização:** `biblioteca/integracoes/evolution-api/exemplos/`
* **Diferenças Chave:**
    1. **Webhook:** Processa o JSON específico da Evolution (`data.message...`).
    2. **Envio:** Não usa nós do WAHA. Usa `HTTP Request` batendo direto nos endpoints `/message/sendText` e `/message/sendList` da Evolution.
    3. **Config:** Exige variáveis `$env.EVOLUTION_API_URL` e `$env.EVOLUTION_API_KEY`.

### 14. `WORKFLOW_EVOLUTION_MASTER_ROTEADOR.json`

* **Descrição:** Orquestrador Master adaptado para Evolution.
* **Localização:** `biblioteca/integracoes/evolution-api/exemplos/`

### 15. `WORKFLOW_EVOLUTION_V7_RECUPERACAO.json`

* **Descrição:** Fluxo de Recuperação/Segurança adaptado para Evolution.
* **Localização:** `biblioteca/integracoes/evolution-api/exemplos/`

### 16. `WORKFLOW_EVOLUTION_YUI_ASSISTENTE.json` (Bonus)

* **Descrição:** Versão do **Agente YUI** (Seu arquivo original) convertido para Evolution.
* **Localização:** `biblioteca/integracoes/evolution-api/exemplos/`
* **Upgrade:** Substituiu os nós WAHA (antigos) por requisições HTTP da Evolution.

### 17. `WORKFLOW_WEB_FORM_GLPI.json` (Portal Web)

* **Descrição:** Interface Web (Formulário) para abertura de chamados sem login no GLPI.
* **Recurso:** Usa o nó **n8n Form Trigger**.
* **Campos:** Nome, Email, Tipo (Incidente/Requisição), Título, Descrição, Urgência.
* **Resultado:** Cria o chamado via API e retorna o ID na tela para o usuário.
* **URL de Acesso:** `https://seu-n8n.com/form/abrir-chamado`
