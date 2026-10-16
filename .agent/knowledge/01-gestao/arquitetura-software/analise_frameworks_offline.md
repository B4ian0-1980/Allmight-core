---json
{
  "id": "analise_frameworks_offline",
  "title": "🔌 Análise de Frameworks para Sistema Offline - SESAU Eventos",
  "categoria": "01-gestao",
  "subcategoria": "arquitetura-software",
  "resumo": "Guia tecnico e referencias sobre 🔌 Análise de Frameworks para Sistema Offline - SESAU Eventos.",
  "gatilhos": [
    "analise",
    "arquitetura",
    "eventos",
    "frameworks",
    "gestao",
    "offline",
    "para",
    "sesau"
  ],
  "perguntas_tipo": [
    "Como utilizar 🔌 Análise de Frameworks para Sistema Offline - SESAU Eventos?",
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

# 🔌 Análise de Frameworks para Sistema Offline - SESAU Eventos

**Versão:** 1.0  
**Data:** 2025-01-27  
**Contexto:** Sistema gratuito para Secretaria de Saúde de Camaçari  
**Requisito Crítico:** Funcionamento offline completo

---

## 📋 ÍNDICE

1. [Requisitos e Contexto](#requisitos-e-contexto)
2. [Estratégias para Funcionamento Offline](#estratégias-para-funcionamento-offline)
3. [Análise de Frameworks PHP](#análise-de-frameworks-php)
4. [Tecnologias Frontend para Offline](#tecnologias-frontend-para-offline)
5. [Arquitetura Proposta: PWA (Progressive Web App)](#arquitetura-proposta-pwa)
6. [Comparativo de Soluções](#comparativo-de-soluções)
7. [Recomendação Final](#recomendação-final)
8. [Plano de Implementação](#plano-de-implementação)

---

## 🎯 REQUISITOS E CONTEXTO

### Requisitos do Projeto

- ✅ **Gratuito/Open Source**: Sem custos de licenciamento
- ✅ **Funcionamento Offline**: Sistema deve funcionar sem internet
- ✅ **Sincronização**: Dados devem sincronizar quando internet voltar
- ✅ **PHP Backend**: Manter compatibilidade com código existente
- ✅ **Baixo Custo de Infraestrutura**: Solução leve e eficiente
- ✅ **Fácil Manutenção**: Para equipe da Secretaria de Saúde

### Cenários de Uso Offline

1. **Eventos em Locais Remotos**
   - Sem conexão de internet estável
   - Necessidade de registrar atendimentos localmente
   - Sincronização ao final do evento

2. **Falhas de Conexão Temporárias**
   - Sistema continua funcionando
   - Dados salvos localmente
   - Sincronização automática quando conexão retorna

3. **Uso em Tablets/Smartphones**
   - Profissionais em campo
   - Registro de atendimentos móveis
   - Sincronização quando retornam à base

---

## 🔄 ESTRATÉGIAS PARA FUNCIONAMENTO OFFLINE

### Estratégia 1: PWA (Progressive Web App) ⭐ RECOMENDADO

**Conceito:**
- Aplicação web que funciona como app nativo
- Service Workers para cache e funcionamento offline
- IndexedDB para armazenamento local
- Sincronização em background quando online

**Vantagens:**
- ✅ Funciona em qualquer dispositivo (desktop, tablet, mobile)
- ✅ Não requer instalação de app store
- ✅ Atualizações automáticas
- ✅ Gratuito e open source
- ✅ Funciona offline completo

**Tecnologias:**
- Service Workers (JavaScript)
- IndexedDB (banco local no navegador)
- Cache API
- Background Sync API

### Estratégia 2: Aplicativo Híbrido (Cordova/Capacitor)

**Conceito:**
- App nativo que encapsula web app
- Acesso a recursos do dispositivo
- Armazenamento local nativo

**Vantagens:**
- ✅ Acesso a recursos do dispositivo (câmera, GPS, etc.)
- ✅ Pode ser distribuído via app stores
- ✅ Funciona offline

**Desvantagens:**
- ⚠️ Requer desenvolvimento adicional
- ⚠️ Mais complexo de manter
- ⚠️ Requer publicação em app stores

### Estratégia 3: Sincronização Manual

**Conceito:**
- Exportar dados quando offline
- Importar quando online
- Processo manual

**Desvantagens:**
- ❌ Não é automático
- ❌ Propenso a erros
- ❌ Não recomendado

---

## 🏗️ ANÁLISE DE FRAMEWORKS PHP

### Framework 1: Laravel ⭐ RECOMENDADO

**Licença:** MIT (Gratuito e Open Source)

**Características:**
- Framework PHP moderno e robusto
- Grande comunidade e documentação
- Muitos pacotes disponíveis
- Suporta API REST nativamente

**Para Sistema Offline:**
- ✅ API REST para comunicação com frontend
- ✅ Queue system para sincronização
- ✅ Event system para triggers
- ✅ Eloquent ORM para acesso a dados

**Pacotes Úteis:**
- `laravel/passport` - OAuth 2.0 (gratuito)
- `spatie/laravel-backup` - Backups (gratuito)
- `laravel/horizon` - Monitoramento de filas (gratuito)

**Exemplo de Estrutura:**
```php
// routes/api.php
Route::apiResource('pacientes', PacienteController::class);
Route::apiResource('atendimentos', AtendimentoController::class);

// app/Http/Controllers/AtendimentoController.php
class AtendimentoController extends Controller {
    public function store(Request $request) {
        // Salvar no banco
        // Retornar JSON para sincronização
    }
    
    public function sync(Request $request) {
        // Receber dados offline
        // Processar sincronização
        // Resolver conflitos
    }
}
```

**Custo:** Gratuito  
**Complexidade:** Média  
**Manutenibilidade:** Alta  
**Recomendação:** ⭐⭐⭐⭐⭐

---

### Framework 2: Symfony

**Licença:** MIT (Gratuito e Open Source)

**Características:**
- Framework PHP muito flexível
- Componentes modulares
- Mais complexo que Laravel
- Excelente para projetos enterprise

**Para Sistema Offline:**
- ✅ API Platform (componente para APIs REST)
- ✅ Messenger component (filas e sincronização)
- ✅ Doctrine ORM (mais poderoso que Eloquent)

**Custo:** Gratuito  
**Complexidade:** Alta  
**Manutenibilidade:** Alta  
**Recomendação:** ⭐⭐⭐⭐ (se equipe tem experiência)

---

### Framework 3: Slim Framework

**Licença:** MIT (Gratuito e Open Source)

**Características:**
- Micro-framework minimalista
- Leve e rápido
- Ideal para APIs
- Poucas dependências

**Para Sistema Offline:**
- ✅ Focado em APIs REST
- ✅ Leve e rápido
- ⚠️ Requer mais código manual

**Custo:** Gratuito  
**Complexidade:** Baixa  
**Manutenibilidade:** Média  
**Recomendação:** ⭐⭐⭐ (para APIs simples)

---

### Framework 4: CodeIgniter 4

**Licença:** MIT (Gratuito e Open Source)

**Características:**
- Framework PHP tradicional
- Curva de aprendizado baixa
- Documentação em português disponível
- Mais simples que Laravel

**Para Sistema Offline:**
- ✅ Suporta APIs REST
- ✅ Fácil de aprender
- ⚠️ Menos recursos que Laravel

**Custo:** Gratuito  
**Complexidade:** Baixa  
**Manutenibilidade:** Média  
**Recomendação:** ⭐⭐⭐⭐ (para equipes iniciantes)

---

### Framework 5: Manter PHP Puro (Sem Framework)

**Licença:** N/A (PHP é open source)

**Características:**
- Código atual já é PHP puro
- Sem dependências de framework
- Controle total sobre código

**Para Sistema Offline:**
- ✅ Sem mudanças arquiteturais grandes
- ✅ Adicionar apenas API REST
- ⚠️ Mais código manual
- ⚠️ Menos estrutura

**Custo:** Gratuito  
**Complexidade:** Baixa (manter) / Alta (adicionar features)  
**Manutenibilidade:** Baixa (sem estrutura)  
**Recomendação:** ⭐⭐ (apenas se migração for inviável)

---

## 💻 TECNOLOGIAS FRONTEND PARA OFFLINE

### Opção 1: React + PWA ⭐ RECOMENDADO

**Stack:**
- **React** - Biblioteca JavaScript (gratuita)
- **Workbox** - Service Workers (gratuito, Google)
- **IndexedDB** - Banco local (nativo do navegador)
- **React Query / SWR** - Sincronização de dados (gratuito)

**Vantagens:**
- ✅ Ecossistema rico e moderno
- ✅ Grande comunidade
- ✅ Muitas bibliotecas gratuitas
- ✅ PWA nativo

**Exemplo:**
```javascript
// service-worker.js (Workbox)
import { precacheAndRoute } from 'workbox-precaching';
import { registerRoute } from 'workbox-routing';
import { CacheFirst, NetworkFirst } from 'workbox-strategies';

// Cache de assets
precacheAndRoute(self.__WB_MANIFEST);

// API: Network First (tenta rede, fallback para cache)
registerRoute(
  /^https:\/\/api\.sesau\.gov\.br\/api\//,
  new NetworkFirst({
    cacheName: 'api-cache',
    plugins: [{
      cacheKeyWillBeUsed: async ({ request }) => {
        return request.url;
      }
    }]
  })
);

// IndexedDB para dados offline
import { openDB } from 'idb';

const db = await openDB('sesau-db', 1, {
  upgrade(db) {
    db.createObjectStore('pacientes', { keyPath: 'id' });
    db.createObjectStore('atendimentos', { keyPath: 'id' });
    db.createObjectStore('sync-queue', { keyPath: 'id', autoIncrement: true });
  }
});

// Salvar offline
async function salvarOffline(dados) {
  await db.put('atendimentos', dados);
  await db.put('sync-queue', { 
    action: 'create', 
    resource: 'atendimento', 
    data: dados 
  });
}

// Sincronizar quando online
navigator.serviceWorker.ready.then(registration => {
  registration.sync.register('sync-data');
});
```

**Custo:** Gratuito  
**Complexidade:** Média  
**Recomendação:** ⭐⭐⭐⭐⭐

---

### Opção 2: Vue.js + PWA

**Stack:**
- **Vue.js** - Framework JavaScript (gratuito)
- **Workbox** - Service Workers
- **PouchDB** - Banco local (gratuito, compatível com CouchDB)
- **Vuex** - Gerenciamento de estado

**Vantagens:**
- ✅ Curva de aprendizado mais baixa que React
- ✅ Documentação excelente
- ✅ Mais simples para iniciantes

**Custo:** Gratuito  
**Complexidade:** Média  
**Recomendação:** ⭐⭐⭐⭐

---

### Opção 3: Vanilla JavaScript + PWA

**Stack:**
- **JavaScript Puro** - Sem frameworks
- **Workbox** - Service Workers
- **IndexedDB** - Banco local

**Vantagens:**
- ✅ Sem dependências
- ✅ Leve e rápido
- ✅ Controle total

**Desvantagens:**
- ⚠️ Mais código manual
- ⚠️ Menos estrutura

**Custo:** Gratuito  
**Complexidade:** Alta (muito código manual)  
**Recomendação:** ⭐⭐⭐ (apenas se necessário)

---

## 🏛️ ARQUITETURA PROPOSTA: PWA (PROGRESSIVE WEB APP)

### Arquitetura Híbrida: Laravel API + React PWA

```
┌─────────────────────────────────────────────────────────┐
│                    FRONTEND (PWA)                       │
│  ┌───────────────────────────────────────────────────┐  │
│  │  React App (Service Worker + IndexedDB)          │  │
│  │  - Funciona offline                              │  │
│  │  - Cache de assets                               │  │
│  │  - Armazenamento local                           │  │
│  │  - Sincronização automática                      │  │
│  └───────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
                        ↕ (HTTPS quando online)
┌─────────────────────────────────────────────────────────┐
│                    BACKEND (Laravel)                     │
│  ┌───────────────────────────────────────────────────┐  │
│  │  API REST (Laravel)                              │  │
│  │  - Endpoints JSON                                │  │
│  │  - Autenticação JWT                              │  │
│  │  - Queue para sincronização                     │  │
│  └───────────────────────────────────────────────────┘  │
│                        ↕                                │
│  ┌───────────────────────────────────────────────────┐  │
│  │  MySQL/MariaDB                                    │  │
│  │  - Banco principal                               │  │
│  │  - Dados sincronizados                           │  │
│  └───────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

### Fluxo de Funcionamento Offline

```
1. Usuário acessa sistema (online ou offline)
   ↓
2. Service Worker intercepta requisições
   ↓
3. SE online:
   - Busca dados do servidor
   - Atualiza cache
   - Sincroniza dados offline pendentes
   ↓
4. SE offline:
   - Serve dados do cache
   - Salva novas ações no IndexedDB
   - Adiciona à fila de sincronização
   ↓
5. Quando volta online:
   - Service Worker detecta conexão
   - Processa fila de sincronização
   - Resolve conflitos (se houver)
   - Atualiza cache
```

### Estrutura de Dados Offline

```javascript
// Estrutura IndexedDB
{
  stores: {
    'pacientes': {
      keyPath: 'id',
      indexes: ['nome', 'cpf']
    },
    'atendimentos': {
      keyPath: 'id',
      indexes: ['paciente_id', 'status', 'data_entrada']
    },
    'evolucoes': {
      keyPath: 'id',
      indexes: ['atendimento_id']
    },
    'estoque': {
      keyPath: 'id',
      indexes: ['nome']
    },
    'sync-queue': {
      keyPath: 'id',
      autoIncrement: true,
      indexes: ['status', 'timestamp']
    },
    'config': {
      keyPath: 'key'
    }
  }
}
```

---

## 📊 COMPARATIVO DE SOLUÇÕES

### Comparativo: Frameworks Backend

| Framework | Gratuito | Offline Support | API REST | Curva Aprendizado | Comunidade | Recomendação |
|-----------|----------|-----------------|----------|-------------------|------------|--------------|
| **Laravel** | ✅ MIT | ✅ Sim (via API) | ✅ Nativo | Média | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Symfony** | ✅ MIT | ✅ Sim (via API) | ✅ API Platform | Alta | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Slim** | ✅ MIT | ✅ Sim (via API) | ✅ Nativo | Baixa | ⭐⭐⭐ | ⭐⭐⭐ |
| **CodeIgniter 4** | ✅ MIT | ✅ Sim (via API) | ✅ Sim | Baixa | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **PHP Puro** | ✅ N/A | ⚠️ Manual | ⚠️ Manual | Baixa | - | ⭐⭐ |

### Comparativo: Frameworks Frontend

| Framework | Gratuito | PWA Support | Offline | Curva Aprendizado | Tamanho | Recomendação |
|-----------|----------|-------------|---------|-------------------|---------|--------------|
| **React** | ✅ MIT | ✅ Excelente | ✅ Nativo | Média | Médio | ⭐⭐⭐⭐⭐ |
| **Vue.js** | ✅ MIT | ✅ Excelente | ✅ Nativo | Baixa | Pequeno | ⭐⭐⭐⭐ |
| **Angular** | ✅ MIT | ✅ Excelente | ✅ Nativo | Alta | Grande | ⭐⭐⭐ |
| **Vanilla JS** | ✅ N/A | ⚠️ Manual | ⚠️ Manual | Alta | Mínimo | ⭐⭐⭐ |

---

## 🎯 RECOMENDAÇÃO FINAL

### Stack Recomendada: Laravel + React PWA

**Justificativa:**

1. **Gratuito e Open Source**
   - Laravel: MIT License
   - React: MIT License
   - Todas as dependências são gratuitas

2. **Funcionamento Offline Completo**
   - Service Workers para cache
   - IndexedDB para armazenamento local
   - Sincronização automática quando online

3. **Compatibilidade com Código Existente**
   - Migração gradual possível
   - Laravel pode coexistir com PHP puro
   - API REST pode ser adicionada incrementalmente

4. **Baixo Custo de Infraestrutura**
   - Funciona em servidor simples
   - Não requer serviços pagos
   - Pode rodar em servidor próprio da Secretaria

5. **Fácil Manutenção**
   - Documentação extensa
   - Grande comunidade
   - Muitos recursos em português

### Arquitetura Proposta

```
┌─────────────────────────────────────────────────────────┐
│  FRONTEND: React PWA                                     │
│  ├── Service Worker (Workbox)                            │
│  ├── IndexedDB (dados offline)                          │
│  ├── Cache API (assets)                                 │
│  └── Background Sync (sincronização)                    │
└─────────────────────────────────────────────────────────┘
                    ↕ HTTPS
┌─────────────────────────────────────────────────────────┐
│  BACKEND: Laravel API                                    │
│  ├── API REST (JSON)                                    │
│  ├── JWT Authentication                                 │
│  ├── Queue System (sincronização)                       │
│  └── MySQL/MariaDB                                      │
└─────────────────────────────────────────────────────────┘
```

### Migração Gradual

**Fase 1: Adicionar API REST (Sem quebrar código existente)**
```
Sistema Atual (PHP Puro)
    ↓
Adicionar Laravel como API
    ↓
Manter PHP puro funcionando
    ↓
Migrar gradualmente para Laravel
```

**Fase 2: Adicionar Frontend PWA**
```
Frontend Atual (PHP + HTML)
    ↓
Adicionar React PWA
    ↓
Manter ambos funcionando
    ↓
Migrar páginas gradualmente
```

---

## 📋 PLANO DE IMPLEMENTAÇÃO

### Fase 1: Preparação (1-2 semanas)

**Objetivo:** Preparar ambiente e estrutura base

**Tarefas:**
1. Instalar Laravel (via Composer)
2. Configurar API REST básica
3. Criar endpoints para:
   - Autenticação (JWT)
   - Pacientes (CRUD)
   - Atendimentos (CRUD)
   - Sincronização

**Código Exemplo:**
```bash
# Instalar Laravel
composer create-project laravel/laravel sesau-api

# Instalar JWT
composer require tymon/jwt-auth

# Instalar CORS
composer require fruitcake/laravel-cors
```

### Fase 2: Frontend PWA (2-3 semanas)

**Objetivo:** Criar interface PWA que funciona offline

**Tarefas:**
1. Criar React app com PWA
2. Configurar Service Worker (Workbox)
3. Implementar IndexedDB
4. Criar sistema de sincronização
5. Implementar UI offline-first

**Código Exemplo:**
```bash
# Criar React app com PWA
npx create-react-app sesau-pwa --template cra-template-pwa

# Instalar dependências
npm install workbox-window idb react-query
```

### Fase 3: Sincronização (1-2 semanas)

**Objetivo:** Implementar sincronização automática

**Tarefas:**
1. Fila de sincronização no frontend
2. Endpoint de sincronização no backend
3. Resolução de conflitos
4. Testes de sincronização

### Fase 4: Migração Gradual (4-6 semanas)

**Objetivo:** Migrar funcionalidades existentes

**Tarefas:**
1. Migrar módulo de recepção
2. Migrar módulo clínico
3. Migrar módulo de farmácia
4. Migrar notificações
5. Testes completos

---

## 💰 ANÁLISE DE CUSTOS

### Custo Total: R$ 0,00 (Gratuito)

**Componentes:**
- ✅ Laravel: Gratuito (MIT)
- ✅ React: Gratuito (MIT)
- ✅ Workbox: Gratuito (Apache 2.0)
- ✅ MySQL/MariaDB: Gratuito (GPL)
- ✅ Servidor: Pode usar servidor próprio da Secretaria

**Infraestrutura Mínima:**
- Servidor web (Apache/Nginx): Gratuito
- PHP 8.5+: Gratuito
- MySQL/MariaDB: Gratuito
- Node.js (para build): Gratuito

**Custos Opcionais (se necessário):**
- Hospedagem cloud: R$ 50-200/mês (se não tiver servidor próprio)
- Domínio: R$ 30-50/ano (se necessário)

---

## 🔧 IMPLEMENTAÇÃO TÉCNICA DETALHADA

### 1. Service Worker (Workbox)

```javascript
// public/sw.js
import { precacheAndRoute } from 'workbox-precaching';
import { registerRoute } from 'workbox-routing';
import { NetworkFirst, CacheFirst } from 'workbox-strategies';
import { BackgroundSyncPlugin } from 'workbox-background-sync';

// Precache assets
precacheAndRoute(self.__WB_MANIFEST);

// API: Network First com fallback para cache
registerRoute(
  ({url}) => url.pathname.startsWith('/api/'),
  new NetworkFirst({
    cacheName: 'api-cache',
    plugins: [
      {
        cacheKeyWillBeUsed: async ({request}) => request.url,
      },
      new BackgroundSyncPlugin('sync-queue', {
        maxRetentionTime: 24 * 60, // 24 horas
      }),
    ],
  })
);

// Assets estáticos: Cache First
registerRoute(
  ({request}) => request.destination === 'style' || 
                 request.destination === 'script' ||
                 request.destination === 'image',
  new CacheFirst({
    cacheName: 'static-cache',
  })
);
```

### 2. IndexedDB Helper

```javascript
// utils/db.js
import { openDB } from 'idb';

const DB_NAME = 'sesau-db';
const DB_VERSION = 1;

export async function initDB() {
  return await openDB(DB_NAME, DB_VERSION, {
    upgrade(db) {
      // Store de pacientes
      if (!db.objectStoreNames.contains('pacientes')) {
        const pacienteStore = db.createObjectStore('pacientes', { keyPath: 'id' });
        pacienteStore.createIndex('nome', 'nome');
        pacienteStore.createIndex('cpf', 'cpf');
      }
      
      // Store de atendimentos
      if (!db.objectStoreNames.contains('atendimentos')) {
        const atendimentoStore = db.createObjectStore('atendimentos', { keyPath: 'id' });
        atendimentoStore.createIndex('paciente_id', 'paciente_id');
        atendimentoStore.createIndex('status', 'status');
        atendimentoStore.createIndex('data_entrada', 'data_entrada');
      }
      
      // Fila de sincronização
      if (!db.objectStoreNames.contains('sync-queue')) {
        const syncStore = db.createObjectStore('sync-queue', { 
          keyPath: 'id', 
          autoIncrement: true 
        });
        syncStore.createIndex('status', 'status');
        syncStore.createIndex('timestamp', 'timestamp');
      }
      
      // Configurações
      if (!db.objectStoreNames.contains('config')) {
        db.createObjectStore('config', { keyPath: 'key' });
      }
    },
  });
}

// Salvar paciente offline
export async function salvarPacienteOffline(paciente) {
  const db = await initDB();
  const tx = db.transaction('pacientes', 'readwrite');
  await tx.store.put(paciente);
  await tx.done;
  
  // Adicionar à fila de sincronização
  await adicionarSyncQueue('create', 'paciente', paciente);
}

// Adicionar à fila de sincronização
async function adicionarSyncQueue(action, resource, data) {
  const db = await initDB();
  const tx = db.transaction('sync-queue', 'readwrite');
  await tx.store.add({
    action,
    resource,
    data,
    status: 'pending',
    timestamp: Date.now(),
  });
  await tx.done;
}
```

### 3. Sincronização Automática

```javascript
// utils/sync.js
import { initDB } from './db';

export async function sincronizarDados() {
  if (!navigator.onLine) {
    console.log('Offline - sincronização agendada');
    return;
  }
  
  const db = await initDB();
  const tx = db.transaction('sync-queue', 'readwrite');
  const queue = await tx.store.getAll();
  
  const pendentes = queue.filter(item => item.status === 'pending');
  
  for (const item of pendentes) {
    try {
      await processarItemSync(item);
      
      // Marcar como processado
      item.status = 'completed';
      await tx.store.put(item);
    } catch (error) {
      console.error('Erro ao sincronizar:', error);
      item.status = 'error';
      item.error = error.message;
      await tx.store.put(item);
    }
  }
  
  await tx.done;
}

async function processarItemSync(item) {
  const { action, resource, data } = item;
  
  let url = `/api/${resource}`;
  let method = 'POST';
  
  if (action === 'update') {
    url += `/${data.id}`;
    method = 'PUT';
  } else if (action === 'delete') {
    url += `/${data.id}`;
    method = 'DELETE';
  }
  
  const response = await fetch(url, {
    method,
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${getToken()}`,
    },
    body: JSON.stringify(data),
  });
  
  if (!response.ok) {
    throw new Error(`HTTP ${response.status}: ${response.statusText}`);
  }
  
  return await response.json();
}

// Detectar quando volta online
window.addEventListener('online', () => {
  console.log('Online - iniciando sincronização');
  sincronizarDados();
});

// Sincronizar periodicamente quando online
if (navigator.onLine) {
  setInterval(sincronizarDados, 30000); // A cada 30 segundos
}
```

### 4. Laravel API - Endpoint de Sincronização

```php
// routes/api.php
Route::middleware('auth:api')->group(function () {
    Route::post('/sync', [SyncController::class, 'sync']);
    Route::get('/sync/status', [SyncController::class, 'status']);
});

// app/Http/Controllers/SyncController.php
class SyncController extends Controller
{
    public function sync(Request $request)
    {
        $dados = $request->all();
        $resultados = [];
        
        foreach ($dados as $item) {
            try {
                $resultado = $this->processarItem($item);
                $resultados[] = [
                    'id' => $item['id'],
                    'status' => 'success',
                    'data' => $resultado
                ];
            } catch (\Exception $e) {
                $resultados[] = [
                    'id' => $item['id'],
                    'status' => 'error',
                    'error' => $e->getMessage()
                ];
            }
        }
        
        return response()->json([
            'success' => true,
            'results' => $resultados
        ]);
    }
    
    private function processarItem($item)
    {
        $action = $item['action'];
        $resource = $item['resource'];
        $data = $item['data'];
        
        switch ($resource) {
            case 'paciente':
                return $this->processarPaciente($action, $data);
            case 'atendimento':
                return $this->processarAtendimento($action, $data);
            // ... outros recursos
        }
    }
    
    private function processarPaciente($action, $data)
    {
        if ($action === 'create' || $action === 'update') {
            $paciente = Paciente::updateOrCreate(
                ['id' => $data['id']],
                $data
            );
            return $paciente;
        } elseif ($action === 'delete') {
            Paciente::destroy($data['id']);
            return ['deleted' => true];
        }
    }
}
```

---

## 🎨 EXEMPLO DE IMPLEMENTAÇÃO: Registro Offline

```javascript
// components/RegistroEntrada.jsx
import { useState } from 'react';
import { salvarPacienteOffline, salvarAtendimentoOffline } from '../utils/db';
import { sincronizarDados } from '../utils/sync';

function RegistroEntrada() {
  const [nome, setNome] = useState('');
  const [isOnline, setIsOnline] = useState(navigator.onLine);
  
  // Detectar status online/offline
  useEffect(() => {
    const handleOnline = () => setIsOnline(true);
    const handleOffline = () => setIsOnline(false);
    
    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);
    
    return () => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    };
  }, []);
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    
    const atendimento = {
      id: Date.now(), // ID temporário
      nome: nome.toUpperCase(),
      data_entrada: new Date().toISOString(),
      status: 'aguardando',
      triagem: 'verde',
      sync_status: 'pending'
    };
    
    if (isOnline) {
      // Tentar salvar online primeiro
      try {
        const response = await fetch('/api/atendimentos', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${getToken()}`,
          },
          body: JSON.stringify(atendimento),
        });
        
        if (response.ok) {
          const data = await response.json();
          showMessage('Registrado com sucesso!', 'success');
          setNome('');
          return;
        }
      } catch (error) {
        console.error('Erro ao salvar online, salvando offline:', error);
      }
    }
    
    // Salvar offline
    await salvarAtendimentoOffline(atendimento);
    showMessage(
      isOnline 
        ? 'Salvo localmente (erro na conexão). Sincronizará automaticamente.'
        : 'Salvo localmente. Sincronizará quando voltar online.',
      'info'
    );
    setNome('');
    
    // Tentar sincronizar se online
    if (isOnline) {
      sincronizarDados();
    }
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <div className="status-indicator">
        {isOnline ? (
          <span className="badge bg-success">🟢 Online</span>
        ) : (
          <span className="badge bg-warning">🟡 Offline</span>
        )}
      </div>
      
      <input
        type="text"
        value={nome}
        onChange={(e) => setNome(e.target.value)}
        placeholder="Nome completo"
        required
      />
      
      <button type="submit">
        {isOnline ? 'Registrar' : 'Salvar (Offline)'}
      </button>
    </form>
  );
}
```

---

## 📱 FUNCIONALIDADES OFFLINE

### O que Funciona Offline

✅ **Registro de Entrada**
- Cadastro de pacientes
- Classificação de triagem
- Adição de observações
- Edição de dados básicos

✅ **Atendimento Clínico**
- Visualização de fila (cache)
- Registro de evoluções
- Registro de sinais vitais
- Prescrição de medicamentos

✅ **Farmácia**
- Consulta de estoque (cache)
- Registro de movimentações
- Alertas de estoque baixo

✅ **Notificações**
- Criação de notificações
- Visualização de pendentes
- Marcação como resolvida (sincroniza depois)

### O que NÃO Funciona Offline

❌ **Sincronização Imediata**
- Dados ficam na fila até voltar online

❌ **Relatórios em Tempo Real**
- Apenas dados locais disponíveis

❌ **Configurações do Sistema**
- Requer conexão para alterar

---

## 🔒 SEGURANÇA EM MODO OFFLINE

### Considerações

1. **Autenticação**
   - Token JWT armazenado localmente (localStorage)
   - Validação de expiração
   - Renovação automática quando online

2. **Dados Sensíveis**
   - Criptografia de dados no IndexedDB (opcional)
   - Limpeza automática após período
   - Não armazenar senhas

3. **Integridade**
   - Validação de dados antes de salvar
   - Checksum para detectar corrupção
   - Backup automático local

---

## 📊 COMPARATIVO FINAL

### Solução Recomendada: Laravel + React PWA

| Critério | Avaliação | Nota |
|----------|-----------|------|
| **Gratuito** | ✅ 100% Open Source | ⭐⭐⭐⭐⭐ |
| **Offline** | ✅ Funcionamento completo | ⭐⭐⭐⭐⭐ |
| **Facilidade** | ✅ Boa documentação | ⭐⭐⭐⭐ |
| **Performance** | ✅ Rápido e eficiente | ⭐⭐⭐⭐⭐ |
| **Manutenção** | ✅ Grande comunidade | ⭐⭐⭐⭐⭐ |
| **Custo Infra** | ✅ Baixo (servidor próprio) | ⭐⭐⭐⭐⭐ |

**Nota Final:** ⭐⭐⭐⭐⭐ (5/5)

---

## 🚀 PRÓXIMOS PASSOS

1. **Aprovar Stack:** Laravel + React PWA
2. **Configurar Ambiente:** Instalar dependências
3. **Criar API Base:** Endpoints REST básicos
4. **Implementar PWA:** Service Worker + IndexedDB
5. **Testar Offline:** Validar funcionamento
6. **Migração Gradual:** Mover funcionalidades

---

**Última Atualização:** 2025-01-27  
**Status:** Recomendação Final Aprovada

