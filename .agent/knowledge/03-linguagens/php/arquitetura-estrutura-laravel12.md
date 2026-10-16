---json
{
  "id": "arquitetura-estrutura-laravel12",
  "title": "🏗️ Arquitetura e Estrutura Laravel 12 - Guia Completo para SDLC",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "Guia tecnico e referencias sobre 🏗️ Arquitetura e Estrutura Laravel 12 - Guia Completo para SDLC.",
  "gatilhos": [
    "arquitetura",
    "completo",
    "estrutura",
    "guia",
    "laravel",
    "laravel12",
    "linguagens",
    "para"
  ],
  "perguntas_tipo": [
    "Como utilizar 🏗️ Arquitetura e Estrutura Laravel 12 - Guia Completo para SDLC?",
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

# 🏗️ Arquitetura e Estrutura Laravel 12 - Guia Completo para SDLC

**Data:** 2025-01-27  
**Versão:** 1.0  
**Status:** Referência Completa para Desenvolvimento por IA  
**Contexto:** Sistema SESAU Eventos - Laravel 12.x + React 19 + Inertia 2

---

## 📝 Classificação de Tarefa

**Tipo:** 🏗️ **Arquitetura** - Estrutura e organização do projeto  
**Modo:** 🏗️ **Modo Arquiteto** - Decisões estruturais baseadas em Laravel 12

---

## 🎯 Decisão Técnica

**O que será feito:**
Documentar a estrutura completa de pastas do Laravel 12, padrões de organização, e como organizar código seguindo as melhores práticas oficiais do framework.

**Abordagem:**
- **Estrutura Oficial Laravel 12:** Seguir estrutura padrão do framework
- **Organização por Responsabilidade:** Separar código por tipo (Controllers, Services, Models, etc.)
- **Convenções do Laravel:** Seguir convenções oficiais de nomenclatura e organização
- **PSR-4 Autoloading:** Usar namespaces e autoloading padrão

---

## 💡 Justificativa

**Por que essa abordagem:**
1. **Estrutura Oficial:** Laravel 12 fornece estrutura testada e aprovada pela comunidade
2. **Manutenibilidade:** Estrutura clara facilita navegação e manutenção
3. **Escalabilidade:** Estrutura suporta crescimento do projeto
4. **Convenções:** Seguir convenções facilita onboarding e colaboração
5. **Autoloading:** PSR-4 garante carregamento automático de classes

**Alternativas Consideradas:**
1. **Estrutura customizada** - ❌ Rejeitada: quebra convenções, dificulta manutenção
2. **Organização por feature** - ⚠️ Considerada: pode ser usada em partes específicas, mas estrutura padrão é melhor para começar

**Trade-offs:**
- ✅ **Ganhos:** Estrutura clara, fácil navegação, convenções seguidas, escalável
- ⚠️ **Custos:** Pode precisar reorganizar se projeto crescer muito (mas estrutura padrão suporta bem)
- ✅ **ROI:** Muito alto - estrutura bem organizada economiza muito tempo

---

## 📊 Análise de Impacto

### O que muda no sistema?
- **Estrutura:** Estrutura de pastas definida e documentada
- **Organização:** Regras claras de onde colocar cada tipo de arquivo
- **Convenções:** Padrões de nomenclatura e organização estabelecidos

### Riscos Identificados
1. **Risco de Desorganização:** Código pode ser colocado em lugares errados
   - **Mitigação:** Documentação clara, estrutura bem definida
2. **Risco de Confusão:** Desenvolvedores podem não saber onde colocar código
   - **Mitigação:** Guia completo, exemplos claros

### Custos
- **Tempo:** Tempo para entender e seguir estrutura
- **Manutenção:** Manter estrutura organizada

### Breaking Changes
- ❌ **Nenhum:** Estrutura é padrão do Laravel, não quebra nada

---

## ✅ Critérios de Aceite

### Validação
- ✅ Estrutura de pastas documentada completamente
- ✅ Regras de organização definidas
- ✅ Convenções de nomenclatura especificadas
- ✅ Exemplos de uso fornecidos

### Casos Cobertos
- ✅ Onde colocar cada tipo de classe
- ✅ Como organizar por responsabilidade
- ✅ Convenções de nomenclatura
- ✅ Estrutura de pastas completa

### Riscos Remanescentes
- ⚠️ **Adesão:** Risco de não seguir estrutura (mitigado por documentação clara)

### Impacto
- 📊 **Afetados:** Todos os desenvolvedores (IA e humanos)
- 🔄 **Breaking Changes:** Nenhum
- 📚 **Documentação:** Estrutura serve como referência permanente

---

## 📁 Estrutura Completa de Pastas Laravel 12

### Diretório Raiz

```
projeto/
├── app/                    # Código principal da aplicação
├── bootstrap/              # Arquivos de inicialização
├── config/                 # Arquivos de configuração
├── database/               # Migrations, factories, seeders
├── public/                 # Ponto de entrada público
├── resources/             # Views, assets não compilados
├── routes/                 # Definições de rotas
├── storage/                # Arquivos gerados (logs, cache, uploads)
├── tests/                  # Testes automatizados
└── vendor/                 # Dependências Composer
```

---

## 📂 Detalhamento de Cada Diretório

### 1. Diretório `app/` (Código Principal)

**Propósito:** Contém todo o código principal da aplicação. Namespace padrão: `App\`

**Estrutura Completa:**

```
app/
├── Broadcasting/          # Classes de canais de broadcast
├── Console/               # Comandos Artisan customizados
├── Events/                # Classes de eventos
├── Exceptions/            # Exceções customizadas
├── Http/                  # Controllers, Middleware, Requests
│   ├── Controllers/       # Controllers da aplicação
│   │   ├── Api/           # Controllers de API (opcional)
│   │   └── Web/           # Controllers Web (opcional)
│   ├── Middleware/        # Middleware customizado
│   ├── Requests/          # Form Requests (validação)
│   └── Resources/         # API Resources (transformação)
├── Jobs/                  # Jobs de fila
├── Listeners/             # Event listeners
├── Mail/                  # Classes de email
├── Models/                # Modelos Eloquent
├── Notifications/         # Classes de notificação
├── Policies/              # Policies de autorização
├── Providers/             # Service Providers
└── Rules/                  # Regras de validação customizadas
```

#### 📋 Regras de Organização

**Controllers:**
- ✅ **Localização:** `app/Http/Controllers/`
- ✅ **Namespace:** `App\Http\Controllers`
- ✅ **Nomenclatura:** Singular + `Controller` (ex: `PacienteController`)
- ✅ **Organização:** Pode criar subpastas por módulo (ex: `Api/PacienteController`)

**Models:**
- ✅ **Localização:** `app/Models/`
- ✅ **Namespace:** `App\Models`
- ✅ **Nomenclatura:** Singular (ex: `Paciente`, `Atendimento`)
- ✅ **Organização:** Um arquivo por model

**Services:**
- ✅ **Localização:** `app/Services/` (criar se necessário)
- ✅ **Namespace:** `App\Services`
- ✅ **Nomenclatura:** Singular + `Service` (ex: `PacienteService`)
- ✅ **Uso:** Lógica de negócio complexa

**Repositories:**
- ✅ **Localização:** `app/Repositories/` (criar se necessário)
- ✅ **Namespace:** `App\Repositories`
- ✅ **Nomenclatura:** Singular + `Repository` (ex: `PacienteRepository`)
- ✅ **Uso:** Abstração de acesso a dados

**Requests (Form Requests):**
- ✅ **Localização:** `app/Http/Requests/`
- ✅ **Namespace:** `App\Http\Requests`
- ✅ **Nomenclatura:** Nome do recurso + `Request` (ex: `StorePacienteRequest`)
- ✅ **Uso:** Validação de formulários

**Resources (API Resources):**
- ✅ **Localização:** `app/Http/Resources/`
- ✅ **Namespace:** `App\Http\Resources`
- ✅ **Nomenclatura:** Nome do recurso + `Resource` (ex: `PacienteResource`)
- ✅ **Uso:** Transformação de dados para API

**Middleware:**
- ✅ **Localização:** `app/Http/Middleware/`
- ✅ **Namespace:** `App\Http\Middleware`
- ✅ **Nomenclatura:** Descrição + `Middleware` (ex: `CheckPermissionMiddleware`)
- ✅ **Uso:** Interceptar requisições

**Events:**
- ✅ **Localização:** `app/Events/`
- ✅ **Namespace:** `App\Events`
- ✅ **Nomenclatura:** Ação no passado (ex: `PacienteRegistrado`)
- ✅ **Uso:** Notificar outras partes do sistema

**Listeners:**
- ✅ **Localização:** `app/Listeners/`
- ✅ **Namespace:** `App\Listeners`
- ✅ **Nomenclatura:** Ação + `Listener` (ex: `EnviarEmailBemVindoListener`)
- ✅ **Uso:** Responder a eventos

**Jobs:**
- ✅ **Localização:** `app/Jobs/`
- ✅ **Namespace:** `App\Jobs`
- ✅ **Nomenclatura:** Ação + `Job` (ex: `ProcessarAtendimentoJob`)
- ✅ **Uso:** Tarefas assíncronas

**Policies:**
- ✅ **Localização:** `app/Policies/`
- ✅ **Namespace:** `App\Policies`
- ✅ **Nomenclatura:** Nome do model + `Policy` (ex: `PacientePolicy`)
- ✅ **Uso:** Autorização de ações

**Rules:**
- ✅ **Localização:** `app/Rules/`
- ✅ **Namespace:** `App\Rules`
- ✅ **Nomenclatura:** Descrição + `Rule` (ex: `CpfValidoRule`)
- ✅ **Uso:** Regras de validação customizadas

---

### 2. Diretório `bootstrap/`

**Propósito:** Arquivos de inicialização do framework

**Estrutura:**
```
bootstrap/
├── app.php                # Bootstrap principal
└── cache/                 # Cache gerado pelo framework
    ├── config.php         # Cache de configuração
    ├── routes.php         # Cache de rotas
    └── services.php       # Cache de serviços
```

**Regras:**
- ❌ **Não editar manualmente** arquivos de cache
- ✅ **Usar comandos Artisan** para limpar cache

---

### 3. Diretório `config/`

**Propósito:** Arquivos de configuração da aplicação

**Estrutura:**
```
config/
├── app.php                # Configuração principal
├── auth.php               # Configuração de autenticação
├── cache.php              # Configuração de cache
├── database.php           # Configuração de banco de dados
├── filesystems.php        # Configuração de filesystems
├── logging.php            # Configuração de logs
├── mail.php               # Configuração de email
├── queue.php              # Configuração de filas
├── session.php            # Configuração de sessão
└── ...                    # Outros arquivos de config
```

**Regras:**
- ✅ **Usar `config()` helper** para acessar valores
- ❌ **Nunca acessar `.env` diretamente** (usar `env()` apenas em config files)
- ✅ **Documentar opções** importantes nos arquivos de config

---

### 4. Diretório `database/`

**Propósito:** Migrations, factories, seeders e banco SQLite (opcional)

**Estrutura:**
```
database/
├── factories/             # Model Factories
│   └── PacienteFactory.php
├── migrations/            # Migrations
│   ├── 2024_01_01_000000_create_pacientes_table.php
│   └── ...
├── seeders/              # Database Seeders
│   ├── DatabaseSeeder.php
│   └── PacienteSeeder.php
└── .gitignore            # Ignorar SQLite se usado
```

**Regras:**
- ✅ **Nomenclatura de migrations:** `YYYY_MM_DD_HHMMSS_action_table_name.php`
- ✅ **Uma migration por mudança** no schema
- ✅ **Sempre criar `down()` method** para rollback
- ✅ **Factories para dados de teste**
- ✅ **Seeders para dados iniciais**

---

### 5. Diretório `public/`

**Propósito:** Ponto de entrada público, assets compilados

**Estrutura:**
```
public/
├── index.php             # Ponto de entrada
├── .htaccess            # Configuração Apache (se usado)
├── favicon.ico          # Favicon
├── robots.txt           # Robots.txt
├── storage/             # Link simbólico para storage/app/public
└── build/               # Assets compilados (Vite)
```

**Regras:**
- ✅ **Apenas `index.php`** como ponto de entrada
- ✅ **Assets compilados** vão para `build/`
- ✅ **Link simbólico** `storage` aponta para `storage/app/public`

---

### 6. Diretório `resources/`

**Propósito:** Views, assets não compilados (CSS, JS)

**Estrutura:**
```
resources/
├── css/                  # CSS não compilado
│   └── app.css
├── js/                   # JavaScript não compilado
│   ├── app.js
│   ├── bootstrap.js
│   └── components/      # Componentes React/Vue
│       └── ui/
├── views/                # Views Blade (se usar Blade)
│   ├── layouts/
│   └── ...
└── lang/                 # Arquivos de tradução
    └── pt_BR/
```

**Regras:**
- ✅ **Assets não compilados** ficam aqui
- ✅ **Views Blade** (se usar Blade além de Inertia)
- ✅ **Traduções** em `lang/`

---

### 7. Diretório `routes/`

**Propósito:** Definições de rotas

**Estrutura:**
```
routes/
├── web.php              # Rotas web (sessão, CSRF)
├── api.php              # Rotas API (opcional, instalar com `install:api`)
├── console.php          # Comandos console
└── channels.php         # Canais de broadcast (opcional)
```

**Regras:**
- ✅ **Rotas web** em `web.php` (sessão, CSRF)
- ✅ **Rotas API** em `api.php` (stateless, tokens)
- ✅ **Comandos console** em `console.php`
- ❌ **Nunca colocar lógica** nas rotas (usar controllers)

---

### 8. Diretório `storage/`

**Propósito:** Arquivos gerados (logs, cache, uploads)

**Estrutura:**
```
storage/
├── app/                  # Arquivos da aplicação
│   ├── public/           # Arquivos públicos (link simbólico)
│   └── private/          # Arquivos privados
├── framework/            # Arquivos do framework
│   ├── cache/            # Cache do framework
│   ├── sessions/         # Sessões baseadas em arquivo
│   ├── testing/          # Arquivos de teste
│   └── views/            # Views compiladas
└── logs/                 # Arquivos de log
    └── laravel.log
```

**Regras:**
- ✅ **Uploads públicos** em `app/public/`
- ✅ **Uploads privados** em `app/private/`
- ✅ **Logs** em `logs/`
- ✅ **Criar link simbólico** para `app/public` → `public/storage`

---

### 9. Diretório `tests/`

**Propósito:** Testes automatizados

**Estrutura:**
```
tests/
├── Feature/              # Testes de feature (integração)
│   └── PacienteTest.php
├── Unit/                 # Testes unitários
│   └── PacienteServiceTest.php
└── TestCase.php          # Classe base de testes
```

**Regras:**
- ✅ **Nomenclatura:** Nome da classe + `Test` (ex: `PacienteTest`)
- ✅ **Feature tests** para fluxos completos
- ✅ **Unit tests** para classes isoladas
- ✅ **Usar Pest ou PHPUnit**

---

## 🎨 Padrões de Organização por Responsabilidade

### Quando Criar Services?

**Criar Service quando:**
- ✅ Lógica de negócio complexa (não apenas CRUD)
- ✅ Múltiplos models envolvidos
- ✅ Lógica reutilizável em vários controllers
- ✅ Processamento complexo de dados

**Exemplo:**
```php
// app/Services/PacienteService.php
namespace App\Services;

use App\Models\Paciente;
use App\Events\PacienteRegistrado;

class PacienteService
{
    public function criarPaciente(array $dados): Paciente
    {
        // Lógica complexa de criação
        $paciente = Paciente::create($dados);
        
        // Disparar eventos
        event(new PacienteRegistrado($paciente));
        
        return $paciente;
    }
}
```

### Quando Criar Repositories?

**Criar Repository quando:**
- ✅ Queries complexas reutilizáveis
- ✅ Abstração de acesso a dados
- ✅ Facilita testes (mock de repository)
- ✅ Múltiplas fontes de dados

**Exemplo:**
```php
// app/Repositories/PacienteRepository.php
namespace App\Repositories;

use App\Models\Paciente;

class PacienteRepository
{
    public function buscarPorTriagem(string $triagem)
    {
        return Paciente::where('triagem', $triagem)
            ->orderBy('created_at')
            ->get();
    }
}
```

### Quando Usar Form Requests?

**Sempre usar Form Requests para:**
- ✅ Validação de formulários
- ✅ Autorização de ações
- ✅ Transformação de dados

**Exemplo:**
```php
// app/Http/Requests/StorePacienteRequest.php
namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;

class StorePacienteRequest extends FormRequest
{
    public function rules(): array
    {
        return [
            'nome_completo' => 'required|string|max:255',
            'cpf' => 'required|string|size:11|unique:pacientes',
            'triagem' => 'required|in:vermelho,amarelo,verde,azul',
        ];
    }
}
```

---

## 📋 Convenções de Nomenclatura (Resumo)

| Tipo | Convenção | Exemplo |
|------|-----------|---------|
| Controller | Singular + Controller | `PacienteController` |
| Model | Singular | `Paciente` |
| Service | Singular + Service | `PacienteService` |
| Repository | Singular + Repository | `PacienteRepository` |
| Request | Ação + Request | `StorePacienteRequest` |
| Resource | Singular + Resource | `PacienteResource` |
| Middleware | Descrição + Middleware | `CheckPermissionMiddleware` |
| Event | Passado | `PacienteRegistrado` |
| Listener | Ação + Listener | `EnviarEmailBemVindoListener` |
| Job | Ação + Job | `ProcessarAtendimentoJob` |
| Policy | Model + Policy | `PacientePolicy` |
| Rule | Descrição + Rule | `CpfValidoRule` |
| Table | Plural snake_case | `pacientes` |
| Column | snake_case | `nome_completo` |
| Foreign Key | singular_id | `paciente_id` |
| Migration | timestamp_action_table | `2024_01_01_000000_create_pacientes_table` |

---

## 🔍 Reflexão sobre Escalabilidade e Manutenibilidade

### Escalabilidade
A estrutura padrão do Laravel 12 escala bem para projetos grandes. A organização por responsabilidade permite adicionar novos módulos sem confusão. Services e Repositories podem ser adicionados conforme necessário sem quebrar a estrutura.

**Considerações futuras:**
- Se projeto crescer muito, pode considerar organização por módulo/feature
- Services podem ser organizados em subpastas por domínio
- Repositories podem ser organizados por contexto

### Manutenibilidade
Estrutura clara e bem documentada facilita manutenção. Convenções seguidas permitem que qualquer desenvolvedor (ou IA) encontre código rapidamente. Separação de responsabilidades facilita mudanças isoladas.

**Melhorias sugeridas:**
- Manter estrutura organizada conforme projeto cresce
- Documentar decisões de organização não-padrão
- Revisar estrutura periodicamente

---

**Última Atualização:** 2025-01-27  
**Próxima Revisão:** Quando necessário ou a cada 3 meses

