---json
{
  "id": "padroes-codigo-laravel",
  "title": "📐 Padrões de Código Laravel - Guia Completo",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "Guia tecnico e referencias sobre 📐 Padrões de Código Laravel - Guia Completo.",
  "gatilhos": [
    "codigo",
    "completo",
    "guia",
    "laravel",
    "linguagens",
    "padroes",
    "php"
  ],
  "perguntas_tipo": [
    "Como utilizar 📐 Padrões de Código Laravel - Guia Completo?",
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

# 📐 Padrões de Código Laravel - Guia Completo

**Data:** 2025-01-27  
**Versão:** 1.0  
**Status:** Referência para Desenvolvimento por IA  
**Contexto:** Sistema SESAU Eventos - Laravel 12.x

---

## 📝 Classificação de Tarefa

**Tipo:** 🏗️ **Arquitetura** - Padrões e convenções de código  
**Modo:** 🏗️ **Modo Arquiteto** - Decisões sobre padrões de código

---

## 🎯 Objetivo

Este documento consolida **todos os padrões de código Laravel** que a IA deve seguir ao desenvolver o sistema. Baseado em:
- ✅ Laravel Best Practices (comunidade)
- ✅ PSR Standards (PHP-FIG)
- ✅ Convenções oficiais do Laravel
- ✅ Boas práticas específicas do projeto

---

## 📚 Documentos de Referência

### 1. Laravel Best Practices
**Arquivo:** `LARAVEL_BEST_PRACTICES.md` e `Laravel 12/Laravel melhores práticas README.md`

Contém práticas específicas do Laravel que geralmente são ignoradas:
- Models gordos, controllers finos
- Validação em Request classes
- Lógica de negócio em Services
- Uso de Eloquent vs Query Builder
- Eager loading (evitar N+1)
- Atribuição em massa
- Chunk para dados pesados
- E muito mais...

### 2. Documentação Oficial Laravel 12.x
**Arquivo:** `Laravel 12/laravel-12.x.md` (convertido do PDF)

Documentação completa do Laravel 12.x com todos os recursos e funcionalidades.

### 3. Arquitetura e Estrutura
**Arquivo:** `ARQUITETURA_ESTRUTURA_LARAVEL12.md`

Estrutura completa de pastas do Laravel 12, organização por responsabilidade, e convenções de nomenclatura.

---

## 🎨 Convenções de Nomenclatura

### Controllers
- ✅ **Singular:** `ArticleController`
- ❌ ~~Plural: `ArticlesController`~~

### Models
- ✅ **Singular:** `User`, `Article`, `Paciente`
- ❌ ~~Plural: `Users`, `Articles`, `Pacientes`~~

### Routes
- ✅ **Plural:** `articles/1`, `pacientes/1`
- ❌ ~~Singular: `article/1`~~

### Named Routes
- ✅ **snake_case com dot notation:** `users.show_active`
- ❌ ~~kebab-case: `users.show-active`~~
- ❌ ~~camelCase: `users.showActive`~~

### Relacionamentos
- ✅ **hasOne/belongsTo:** singular (`articleComment`)
- ✅ **hasMany/belongsToMany:** plural (`articleComments`)
- ❌ ~~snake_case: `article_comment`~~

### Tabelas
- ✅ **Plural snake_case:** `article_comments`, `pacientes`
- ❌ ~~Singular: `article_comment`~~
- ❌ ~~CamelCase: `articleComments`~~

### Colunas
- ✅ **snake_case sem nome do model:** `meta_title`, `nome_completo`
- ❌ ~~CamelCase: `MetaTitle`~~
- ❌ ~~Com prefixo: `article_meta_title`~~

### Foreign Keys
- ✅ **singular_model_id:** `article_id`, `paciente_id`
- ❌ ~~CamelCase: `ArticleId`~~
- ❌ ~~Invertido: `id_article`~~

### Migrations
- ✅ **timestamp_action_table:** `2017_01_01_000000_create_articles_table`
- ❌ ~~Sem create: `2017_01_01_000000_articles`~~

### Métodos
- ✅ **camelCase:** `getAll()`, `criarPaciente()`
- ❌ ~~snake_case: `get_all()`~~

### Métodos em Controllers (Resource)
- ✅ **Padrão REST:** `index`, `store`, `show`, `update`, `destroy`
- ❌ ~~Customizados: `saveArticle`, `deleteArticle`~~

### Variáveis
- ✅ **camelCase:** `$articlesWithAuthor`, `$nomeCompleto`
- ❌ ~~snake_case: `$articles_with_author`~~

### Collections
- ✅ **Descritivo, plural:** `$activeUsers = User::active()->get()`
- ❌ ~~Genérico: `$active`, `$data`~~

### Objects
- ✅ **Descritivo, singular:** `$activeUser = User::active()->first()`
- ❌ ~~Genérico: `$users`, `$obj`~~

### Views (Blade)
- ✅ **kebab-case:** `show-filtered.blade.php`
- ❌ ~~camelCase: `showFiltered.blade.php`~~
- ❌ ~~snake_case: `show_filtered.blade.php`~~

### Config Files
- ✅ **snake_case:** `google_calendar.php`
- ❌ ~~camelCase: `googleCalendar.php`~~

### Contracts (Interfaces)
- ✅ **Adjetivo ou substantivo:** `Authenticatable`
- ❌ ~~Com sufixo: `AuthenticationInterface`, `IAuthentication`~~

### Traits
- ✅ **Adjetivo:** `Notifiable`
- ❌ ~~Com sufixo: `NotificationTrait`~~

---

## 🏗️ Estrutura de Arquivos

### Organização de Controllers

```
app/Http/Controllers/
├── Api/              # API REST controllers
│   ├── PacienteController.php
│   └── AtendimentoController.php
└── Web/              # Web controllers
    ├── PacienteController.php
    └── DashboardController.php
```

### Organização de Models

```
app/Models/
├── Paciente.php
├── Atendimento.php
├── Medico.php
└── Triagem.php
```

### Organização de Services

```
app/Services/
├── PacienteService.php
├── AtendimentoService.php
└── TriagemService.php
```

### Organização de Requests

```
app/Http/Requests/
├── StorePacienteRequest.php
├── UpdatePacienteRequest.php
└── CriarAtendimentoRequest.php
```

---

## 💻 Padrões de Código

### 1. Princípio da Responsabilidade Única

**❌ Ruim:**
```php
public function getFullNameAttribute()
{
    if (auth()->user() && auth()->user()->hasRole('client') && auth()->user()->isVerified()) {
        return 'Sr. ' . $this->first_name . ' ' . $this->middle_name . ' ' . $this->last_name;
    } else {
        return $this->first_name[0] . '. ' . $this->last_name;
    }
}
```

**✅ Bom:**
```php
public function getFullNameAttribute()
{
    return $this->isVerifiedClient() ? $this->getFullNameLong() : $this->getFullNameShort();
}

public function isVerifiedClient()
{
    return auth()->user() && auth()->user()->hasRole('client') && auth()->user()->isVerified();
}

public function getFullNameLong()
{
    return 'Sr. ' . $this->first_name . ' ' . $this->middle_name . ' ' . $this->last_name;
}

public function getFullNameShort()
{
    return $this->first_name[0] . '. ' . $this->last_name;
}
```

### 2. Models Gordos, Controllers Finos

**❌ Ruim:**
```php
public function index()
{
    $pacientes = Paciente::verified()
        ->with(['atendimentos' => function ($q) {
            $q->where('created_at', '>', Carbon::today()->subWeek());
        }])
        ->get();

    return view('index', ['pacientes' => $pacientes]);
}
```

**✅ Bom:**
```php
public function index()
{
    return view('index', ['pacientes' => $this->paciente->getWithNewAtendimentos()]);
}

// No Model
class Paciente extends Model
{
    public function getWithNewAtendimentos()
    {
        return $this->verified()
            ->with(['atendimentos' => function ($q) {
                $q->where('created_at', '>', Carbon::today()->subWeek());
            }])
            ->get();
    }
}
```

### 3. Validação em Request Classes

**❌ Ruim:**
```php
public function store(Request $request)
{
    $request->validate([
        'nome_completo' => 'required|max:255',
        'cpf' => 'required|unique:pacientes|max:11',
        'data_nascimento' => 'nullable|date',
    ]);

    // ...
}
```

**✅ Bom:**
```php
public function store(StorePacienteRequest $request)
{
    // Validação automática
    // ...
}

// app/Http/Requests/StorePacienteRequest.php
class StorePacienteRequest extends Request
{
    public function rules()
    {
        return [
            'nome_completo' => 'required|max:255',
            'cpf' => 'required|unique:pacientes|max:11',
            'data_nascimento' => 'nullable|date',
        ];
    }
}
```

### 4. Lógica de Negócio em Services

**❌ Ruim:**
```php
public function store(Request $request)
{
    if ($request->hasFile('foto')) {
        $request->file('foto')->move(public_path('images') . 'temp');
    }

    // ...
}
```

**✅ Bom:**
```php
public function store(StorePacienteRequest $request)
{
    $this->pacienteService->handleUploadedFoto($request->file('foto'));

    // ...
}

// app/Services/PacienteService.php
class PacienteService
{
    public function handleUploadedFoto($foto)
    {
        if (!is_null($foto)) {
            $foto->move(public_path('images') . 'temp');
        }
    }
}
```

### 5. DRY (Don't Repeat Yourself)

**❌ Ruim:**
```php
public function getActive()
{
    return $this->where('verified', 1)->whereNotNull('deleted_at')->get();
}

public function getAtendimentos()
{
    return $this->whereHas('paciente', function ($q) {
        $q->where('verified', 1)->whereNotNull('deleted_at');
    })->get();
}
```

**✅ Bom:**
```php
public function scopeActive($q)
{
    return $q->where('verified', 1)->whereNotNull('deleted_at');
}

public function getActive()
{
    return $this->active()->get();
}

public function getAtendimentos()
{
    return $this->whereHas('paciente', function ($q) {
        $q->active();
    })->get();
}
```

### 6. Eloquent vs Query Builder

**❌ Ruim (Raw SQL):**
```sql
SELECT *
FROM `atendimentos`
WHERE EXISTS (SELECT *
              FROM `pacientes`
              WHERE `atendimentos`.`paciente_id` = `pacientes`.`id`
              AND EXISTS (SELECT *
                          FROM `triagens`
                          WHERE `triagens`.`paciente_id` = `pacientes`.`id`)
              AND `pacientes`.`deleted_at` IS NULL)
AND `verified` = '1'
AND `active` = '1'
ORDER BY `created_at` DESC
```

**✅ Bom (Eloquent):**
```php
Atendimento::has('paciente.triagem')->verified()->latest()->get();
```

### 7. Atribuição em Massa

**❌ Ruim:**
```php
$paciente = new Paciente;
$paciente->nome_completo = $request->nome_completo;
$paciente->cpf = $request->cpf;
$paciente->data_nascimento = $request->data_nascimento;
$paciente->evento_id = $evento->id;
$paciente->save();
```

**✅ Bom:**
```php
$evento->pacientes()->create($request->validated());
```

### 8. Eager Loading (Evitar N+1)

**❌ Ruim (101 queries para 100 pacientes):**
```php
@foreach (Paciente::all() as $paciente)
    {{ $paciente->atendimento->medico->nome }}
@endforeach
```

**✅ Bom (2 queries para 100 pacientes):**
```php
$pacientes = Paciente::with('atendimento.medico')->get();

@foreach ($pacientes as $paciente)
    {{ $paciente->atendimento->medico->nome }}
@endforeach
```

### 9. Chunk para Dados Pesados

**❌ Ruim:**
```php
$pacientes = Paciente::all();

foreach ($pacientes as $paciente) {
    // Processar...
}
```

**✅ Bom:**
```php
Paciente::chunk(500, function ($pacientes) {
    foreach ($pacientes as $paciente) {
        // Processar...
    }
});
```

### 10. Sintaxes Pequenas e Legíveis

**❌ Ruim:**
```php
$request->session()->get('cart');
$request->input('nome');
return Redirect::back();
Carbon::now();
```

**✅ Bom:**
```php
session('cart');
$request->nome;
return back();
now();
```

**Mais exemplos:**

| Sintaxe Comum | Sintaxe Pequena |
|---------------|-----------------|
| `Session::get('cart')` | `session('cart')` |
| `Session::put('cart', $data)` | `session(['cart' => $data])` |
| `$request->input('name')` | `$request->name` |
| `return Redirect::back()` | `return back()` |
| `Carbon::now()` | `now()` |
| `->orderBy('created_at', 'desc')` | `->latest()` |
| `->orderBy('created_at', 'asc')` | `->oldest()` |
| `->first()->name` | `->value('name')` |

### 11. IoC Container (Dependency Injection)

**❌ Ruim:**
```php
$paciente = new Paciente;
$paciente->create($request->all());
```

**✅ Bom:**
```php
public function __construct(Paciente $paciente)
{
    $this->paciente = $paciente;
}

// ...

$this->paciente->create($request->all());
```

### 12. Config vs .env

**❌ Ruim:**
```php
$apiKey = env('API_KEY');
```

**✅ Bom:**
```php
// config/api.php
'key' => env('API_KEY'),

// Uso
$apiKey = config('api.key');
```

### 13. Constantes vs Strings

**❌ Ruim:**
```php
public function isNormal()
{
    return $atendimento->tipo === 'normal';
}

return back()->with('message', 'Atendimento criado com sucesso!');
```

**✅ Bom:**
```php
// No Model
const TIPO_NORMAL = 'normal';
const TIPO_URGENTE = 'urgente';

public function isNormal()
{
    return $this->tipo === self::TIPO_NORMAL;
}

// No Controller
return back()->with('message', __('app.atendimento_criado'));
```

---

## 📋 Checklist de Qualidade

Antes de finalizar qualquer código Laravel, verifique:

### Nomenclatura
- [ ] Controllers no singular
- [ ] Models no singular
- [ ] Routes no plural
- [ ] Variáveis em camelCase
- [ ] Métodos em camelCase
- [ ] Constantes em UPPER_SNAKE_CASE

### Estrutura
- [ ] Controllers finos (lógica em Services/Models)
- [ ] Validação em Request classes
- [ ] Lógica de negócio em Services
- [ ] Queries complexas em Models (scopes)

### Performance
- [ ] Eager loading usado (evitar N+1)
- [ ] Chunk para dados pesados
- [ ] Índices em foreign keys

### Código
- [ ] Eloquent usado (não raw SQL)
- [ ] Collections usadas (não arrays)
- [ ] Sintaxes pequenas e legíveis
- [ ] IoC Container usado
- [ ] Config usado (não .env direto)

---

## 📚 Referências

- **Laravel Best Practices:** `LARAVEL_BEST_PRACTICES.md`
- **Documentação Laravel 12.x:** `Laravel 12/laravel-12.x.md`
- **PSR Standards:** https://www.php-fig.org/psr/
- **Laravel Docs:** https://laravel.com/docs

---

**Última Atualização:** 2025-01-27  
**Status:** Referência Ativa para Desenvolvimento

