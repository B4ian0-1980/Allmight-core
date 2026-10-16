---json
{
  "id": "guia_pratico",
  "title": "💻 Exemplos Práticos Laravel - Guia Completo",
  "categoria": "04-frameworks",
  "subcategoria": "laravel",
  "resumo": "Guia tecnico e referencias sobre 💻 Exemplos Práticos Laravel - Guia Completo.",
  "gatilhos": [
    "completo",
    "exemplos",
    "frameworks",
    "guia",
    "laravel",
    "pratico"
  ],
  "perguntas_tipo": [
    "Como utilizar 💻 Exemplos Práticos Laravel - Guia Completo?",
    "Quais as boas praticas de laravel?"
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
  "dono": "stack-laravel",
  "prioridade": 2
}
---

# 💻 Exemplos Práticos Laravel - Guia Completo

**Data:** 2025-01-27  
**Versão:** 1.0  
**Status:** Referência Prática para Desenvolvimento por IA  
**Contexto:** Sistema SESAU Eventos - Laravel 12.x

---

## 📝 Classificação de Tarefa

**Tipo:** 📚 **Documentação** - Exemplos práticos de código  
**Modo:** 🏗️ **Modo Arquiteto** - Consolidação de exemplos

---

## 🎯 Decisão Técnica

**O que será feito:**
Consolidar exemplos práticos de código Laravel extraídos de fontes confiáveis, organizados por categoria, para servir como referência imediata durante desenvolvimento.

**Abordagem:**
- **Exemplos Reais:** Código funcional e testado
- **Organização por Categoria:** Fácil de encontrar
- **Explicações Concisas:** Contexto claro
- **Padrões do Laravel 12:** Atualizados

---

## 💡 Justificativa

**Por que essa abordagem:**
1. **Referência Rápida:** IA encontra exemplos rapidamente
2. **Código Testado:** Exemplos de fontes confiáveis
3. **Padrões Corretos:** Seguem convenções do Laravel
4. **Produtividade:** Acelera desenvolvimento

**Alternativas Consideradas:**
1. **Sem exemplos** - ❌ Rejeitada: IA precisa de referências práticas
2. **Exemplos dispersos** - ❌ Rejeitada: difícil de encontrar

**Trade-offs:**
- ✅ **Ganhos:** Desenvolvimento mais rápido, código melhor
- ⚠️ **Custos:** Manutenção de exemplos
- ✅ **ROI:** Muito alto - acelera desenvolvimento significativamente

---

## 📊 Análise de Impacto

### O que muda no sistema?
- **Documentação:** Mais exemplos práticos disponíveis
- **Desenvolvimento:** Mais rápido com referências claras
- **Qualidade:** Código segue padrões corretos

### Riscos Identificados
1. **Risco de Exemplos Desatualizados:** Exemplos podem ficar obsoletos
   - **Mitigação:** Revisar periodicamente, marcar versão do Laravel

### Custos
- **Manutenção:** Atualizar exemplos quando necessário

### Breaking Changes
- ❌ **Nenhum:** Apenas exemplos, não código de produção

---

## ✅ Critérios de Aceite

### Validação
- ✅ Exemplos organizados por categoria
- ✅ Código funcional e testado
- ✅ Explicações claras
- ✅ Padrões do Laravel 12

### Casos Cobertos
- ✅ Controllers
- ✅ Models e Eloquent
- ✅ Form Requests
- ✅ Migrations e Seeds
- ✅ Middleware
- ✅ Artisan Commands

---

## 📚 Exemplos por Categoria

### 1. Controllers

#### Controller Básico

```php
<?php

namespace App\Http\Controllers;

use App\Models\Paciente;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\View\View;

class PacienteController extends Controller
{
    /**
     * Lista todos os pacientes
     */
    public function index(): View
    {
        $pacientes = Paciente::with('atendimentos')->latest()->get();
        
        return view('pacientes.index', compact('pacientes'));
    }

    /**
     * Exibe formulário de criação
     */
    public function create(): View
    {
        return view('pacientes.create');
    }

    /**
     * Armazena novo paciente
     */
    public function store(Request $request): RedirectResponse
    {
        $paciente = Paciente::create($request->validated());
        
        return to_route('pacientes.show', $paciente)
            ->with('success', 'Paciente criado com sucesso!');
    }

    /**
     * Exibe paciente específico
     */
    public function show(Paciente $paciente): View
    {
        $paciente->load('atendimentos.medico');
        
        return view('pacientes.show', compact('paciente'));
    }

    /**
     * Exibe formulário de edição
     */
    public function edit(Paciente $paciente): View
    {
        return view('pacientes.edit', compact('paciente'));
    }

    /**
     * Atualiza paciente
     */
    public function update(Request $request, Paciente $paciente): RedirectResponse
    {
        $paciente->update($request->validated());
        
        return to_route('pacientes.show', $paciente)
            ->with('success', 'Paciente atualizado com sucesso!');
    }

    /**
     * Remove paciente
     */
    public function destroy(Paciente $paciente): RedirectResponse
    {
        $paciente->delete();
        
        return to_route('pacientes.index')
            ->with('success', 'Paciente removido com sucesso!');
    }
}
```

#### Controller com Service

```php
<?php

namespace App\Http\Controllers;

use App\Http\Requests\StorePacienteRequest;
use App\Services\PacienteService;
use Illuminate\Http\RedirectResponse;

class PacienteController extends Controller
{
    public function __construct(
        private PacienteService $pacienteService
    ) {}

    public function store(StorePacienteRequest $request): RedirectResponse
    {
        $paciente = $this->pacienteService->criarPaciente($request->validated());
        
        return to_route('pacientes.show', $paciente)
            ->with('success', 'Paciente criado com sucesso!');
    }
}
```

---

### 2. Models e Eloquent

#### Model Básico com Relacionamentos

```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Paciente extends Model
{
    protected $fillable = [
        'nome_completo',
        'cpf',
        'data_nascimento',
        'sexo',
        'triagem',
        'status',
    ];

    protected $casts = [
        'data_nascimento' => 'date',
    ];

    /**
     * Relacionamento: Paciente tem muitos atendimentos
     */
    public function atendimentos(): HasMany
    {
        return $this->hasMany(Atendimento::class);
    }

    /**
     * Scope: Pacientes verificados
     */
    public function scopeVerificados($query)
    {
        return $query->whereNotNull('cpf');
    }

    /**
     * Scope: Por triagem
     */
    public function scopePorTriagem($query, string $triagem)
    {
        return $query->where('triagem', $triagem);
    }

    /**
     * Accessor: Idade calculada
     */
    public function getIdadeAttribute(): int
    {
        return $this->data_nascimento
            ? $this->data_nascimento->age
            : 0;
    }

    /**
     * Mutator: Nome sempre em maiúsculas
     */
    public function setNomeCompletoAttribute($value)
    {
        $this->attributes['nome_completo'] = strtoupper($value);
    }

    /**
     * Buscar pacientes com novos atendimentos
     */
    public static function getWithNewAtendimentos()
    {
        return static::verificados()
            ->with(['atendimentos' => function ($query) {
                $query->where('created_at', '>', now()->subWeek());
            }])
            ->get();
    }
}
```

#### Model com Soft Deletes

```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\SoftDeletes;

class Atendimento extends Model
{
    use SoftDeletes;

    protected $fillable = [
        'paciente_id',
        'medico_id',
        'observacoes',
        'status',
    ];

    // Nota: O trait SoftDeletes automaticamente faz o cast de deleted_at
    // Não é mais necessário usar $dates (depreciado no Laravel 8+)
    // Se precisar de outros casts, use $casts:
    // protected $casts = [
    //     'deleted_at' => 'datetime',
    // ];

    public function paciente(): BelongsTo
    {
        return $this->belongsTo(Paciente::class);
    }

    public function medico(): BelongsTo
    {
        return $this->belongsTo(Medico::class);
    }
}
```

---

### 3. Form Requests (Validação)

#### Form Request Básico

```php
<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;

class StorePacienteRequest extends FormRequest
{
    /**
     * Determina se o usuário está autorizado a fazer esta requisição
     */
    public function authorize(): bool
    {
        return true; // Ou lógica de autorização
    }

    /**
     * Regras de validação
     */
    public function rules(): array
    {
        return [
            'nome_completo' => 'required|string|max:255',
            'cpf' => 'required|string|size:11|unique:pacientes,cpf',
            'data_nascimento' => 'required|date|before:today',
            'sexo' => 'required|in:masculino,feminino',
            'triagem' => 'required|in:vermelho,amarelo,verde,azul',
            'celular' => 'nullable|string|max:15',
            'cep' => 'nullable|string|size:8',
        ];
    }

    /**
     * Mensagens customizadas
     */
    public function messages(): array
    {
        return [
            'nome_completo.required' => 'O nome completo é obrigatório.',
            'cpf.unique' => 'Este CPF já está cadastrado.',
            'data_nascimento.before' => 'A data de nascimento deve ser anterior a hoje.',
        ];
    }

    /**
     * Atributos customizados para mensagens
     */
    public function attributes(): array
    {
        return [
            'nome_completo' => 'nome completo',
            'data_nascimento' => 'data de nascimento',
        ];
    }
}
```

#### Form Request com Validação Condicional

```php
<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;
use Illuminate\Validation\Rule;

class UpdatePacienteRequest extends FormRequest
{
    public function authorize(): bool
    {
        return true;
    }

    public function rules(): array
    {
        $pacienteId = $this->route('paciente')->id;

        return [
            'nome_completo' => 'sometimes|required|string|max:255',
            'cpf' => [
                'sometimes',
                'required',
                'string',
                'size:11',
                Rule::unique('pacientes', 'cpf')->ignore($pacienteId),
            ],
            'triagem' => 'sometimes|required|in:vermelho,amarelo,verde,azul',
        ];
    }
}
```

---

### 4. Migrations

#### Migration de Criação de Tabela

```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Executa as migrations
     */
    public function up(): void
    {
        Schema::create('pacientes', function (Blueprint $table) {
            $table->id();
            $table->string('nome_completo');
            $table->string('cpf', 11)->unique();
            $table->date('data_nascimento')->nullable();
            $table->enum('sexo', ['masculino', 'feminino'])->nullable();
            $table->enum('triagem', ['vermelho', 'amarelo', 'verde', 'azul'])->default('verde');
            $table->enum('status', ['aguardando', 'em_atendimento', 'atendido', 'cancelado'])->default('aguardando');
            $table->string('celular', 15)->nullable();
            $table->string('cep', 8)->nullable();
            $table->string('logradouro')->nullable();
            $table->string('numero')->nullable();
            $table->string('complemento')->nullable();
            $table->string('bairro')->nullable();
            $table->string('cidade')->nullable();
            $table->string('estado', 2)->nullable();
            $table->string('cns', 15)->nullable();
            $table->string('raca_cor')->nullable();
            $table->timestamps();
            $table->softDeletes();

            // Índices
            $table->index('cpf');
            $table->index('triagem');
            $table->index('status');
            $table->index('created_at');
        });
    }

    /**
     * Reverte as migrations
     */
    public function down(): void
    {
        Schema::dropIfExists('pacientes');
    }
};
```

#### Migration de Alteração de Tabela

```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::table('pacientes', function (Blueprint $table) {
            $table->string('observacoes')->nullable()->after('status');
            $table->index('observacoes');
        });
    }

    public function down(): void
    {
        Schema::table('pacientes', function (Blueprint $table) {
            $table->dropColumn('observacoes');
        });
    }
};
```

---

### 5. Seeders

#### Seeder Básico

```php
<?php

namespace Database\Seeders;

use App\Models\Paciente;
use Illuminate\Database\Seeder;

class PacienteSeeder extends Seeder
{
    /**
     * Executa o seeder
     */
    public function run(): void
    {
        Paciente::factory()->count(50)->create();
    }
}
```

#### Seeder com Dados Específicos

```php
<?php

namespace Database\Seeders;

use App\Models\Paciente;
use Illuminate\Database\Seeder;

class PacienteSeeder extends Seeder
{
    public function run(): void
    {
        $pacientes = [
            [
                'nome_completo' => 'JOÃO SILVA',
                'cpf' => '12345678901',
                'data_nascimento' => '1990-01-15',
                'sexo' => 'masculino',
                'triagem' => 'verde',
                'status' => 'aguardando',
            ],
            [
                'nome_completo' => 'MARIA SANTOS',
                'cpf' => '98765432100',
                'data_nascimento' => '1985-05-20',
                'sexo' => 'feminino',
                'triagem' => 'amarelo',
                'status' => 'aguardando',
            ],
        ];

        foreach ($pacientes as $paciente) {
            Paciente::create($paciente);
        }
    }
}
```

#### DatabaseSeeder Principal

```php
<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    /**
     * Executa os seeders do banco de dados
     */
    public function run(): void
    {
        $this->call([
            PacienteSeeder::class,
            AtendimentoSeeder::class,
            MedicoSeeder::class,
        ]);
    }
}
```

---

### 6. Factories

#### Factory Básica

```php
<?php

namespace Database\Factories;

use App\Models\Paciente;
use Illuminate\Database\Eloquent\Factories\Factory;

class PacienteFactory extends Factory
{
    protected $model = Paciente::class;

    /**
     * Define o estado padrão do model
     */
    public function definition(): array
    {
        return [
            'nome_completo' => strtoupper($this->faker->name),
            'cpf' => $this->faker->unique()->numerify('###########'),
            'data_nascimento' => $this->faker->dateTimeBetween('-80 years', '-18 years'),
            'sexo' => $this->faker->randomElement(['masculino', 'feminino']),
            'triagem' => $this->faker->randomElement(['vermelho', 'amarelo', 'verde', 'azul']),
            'status' => $this->faker->randomElement(['aguardando', 'em_atendimento', 'atendido']),
            'celular' => $this->faker->phoneNumber,
            'cep' => $this->faker->postcode,
            'logradouro' => $this->faker->streetName,
            'numero' => $this->faker->buildingNumber,
            'bairro' => $this->faker->citySuffix,
            'cidade' => $this->faker->city,
            'estado' => $this->faker->stateAbbr,
        ];
    }

    /**
     * Estado: Paciente com triagem vermelha
     */
    public function triagemVermelha(): static
    {
        return $this->state(fn (array $attributes) => [
            'triagem' => 'vermelho',
            'status' => 'aguardando',
        ]);
    }

    /**
     * Estado: Paciente aguardando
     */
    public function aguardando(): static
    {
        return $this->state(fn (array $attributes) => [
            'status' => 'aguardando',
        ]);
    }
}
```

#### Uso da Factory

```php
// Criar um paciente
$paciente = Paciente::factory()->create();

// Criar múltiplos
$pacientes = Paciente::factory()->count(10)->create();

// Criar com estado específico
$pacienteVermelho = Paciente::factory()->triagemVermelha()->create();

// Criar com atributos específicos
$paciente = Paciente::factory()->create([
    'nome_completo' => 'JOÃO SILVA',
    'triagem' => 'verde',
]);
```

---

### 7. Middleware

#### Middleware Customizado

```php
<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\Response;

class CheckPermission
{
    /**
     * Handle an incoming request
     */
    public function handle(Request $request, Closure $next, string $permission): Response
    {
        if (!auth()->check()) {
            return redirect()->route('login');
        }

        if (!auth()->user()->hasPermission($permission)) {
            abort(403, 'Acesso negado');
        }

        return $next($request);
    }
}
```

#### Registro do Middleware

```php
// bootstrap/app.php (Laravel 11+)

use App\Http\Middleware\CheckPermission;
use Illuminate\Foundation\Configuration\Middleware;

return Application::configure(basePath: dirname(__DIR__))
    ->withRouting(
        // ...
    )
    ->withMiddleware(function (Middleware $middleware): void {
        // Middleware global (executa em todas as requisições)
        $middleware->append(CheckPermission::class);
        
        // Ou adicionar a um grupo específico
        $middleware->web(append: [
            CheckPermission::class,
        ]);
        
        // Ou criar um alias para usar em rotas
        $middleware->alias([
            'permission' => CheckPermission::class,
        ]);
    })
    ->withExceptions(function (Exceptions $exceptions): void {
        // ...
    })
    ->create();
```

**Nota:** No Laravel 11+, o registro de middleware mudou de `app/Http/Kernel.php` para `bootstrap/app.php`. O exemplo acima mostra a forma moderna de registrar middleware.

#### Uso em Rotas

```php
// routes/web.php

// Middleware em rota específica
Route::get('/admin/pacientes', [PacienteController::class, 'index'])
    ->middleware('permission:gerenciar_pacientes');

// Middleware em grupo de rotas
Route::middleware(['auth', 'permission:admin'])->group(function () {
    Route::resource('pacientes', PacienteController::class);
});
```

---

### 8. Artisan Commands

#### Comando Customizado

```php
<?php

namespace App\Console\Commands;

use App\Models\Paciente;
use Illuminate\Console\Command;

class LimparPacientesAntigos extends Command
{
    /**
     * Nome e assinatura do comando
     */
    protected $signature = 'pacientes:limpar {--dias=365 : Número de dias}';

    /**
     * Descrição do comando
     */
    protected $description = 'Remove pacientes antigos do banco de dados';

    /**
     * Executa o comando
     */
    public function handle(): int
    {
        $dias = $this->option('dias');
        $dataLimite = now()->subDays($dias);

        $this->info("Removendo pacientes anteriores a {$dataLimite->format('d/m/Y')}...");

        $removidos = Paciente::where('created_at', '<', $dataLimite)
            ->where('status', 'atendido')
            ->delete();

        $this->info("{$removidos} pacientes removidos com sucesso!");

        return Command::SUCCESS;
    }
}
```

#### Uso do Comando

```bash
# Executar comando
php artisan pacientes:limpar

# Com opção
php artisan pacientes:limpar --dias=180
```

---

### 9. Services

#### Service Básico

```php
<?php

namespace App\Services;

use App\Models\Paciente;
use App\Events\PacienteRegistrado;
use Illuminate\Support\Facades\DB;

class PacienteService
{
    /**
     * Cria um novo paciente
     */
    public function criarPaciente(array $dados): Paciente
    {
        return DB::transaction(function () use ($dados) {
            $paciente = Paciente::create($dados);
            
            event(new PacienteRegistrado($paciente));
            
            return $paciente;
        });
    }

    /**
     * Atualiza triagem do paciente
     */
    public function atualizarTriagem(Paciente $paciente, string $triagem, ?string $justificativa = null): void
    {
        $paciente->update([
            'triagem' => $triagem,
            'justificativa_triagem' => $justificativa,
        ]);
    }

    /**
     * Busca pacientes por filtros
     */
    public function buscarPorFiltros(array $filtros)
    {
        $query = Paciente::query();

        if (isset($filtros['triagem'])) {
            $query->where('triagem', $filtros['triagem']);
        }

        if (isset($filtros['status'])) {
            $query->where('status', $filtros['status']);
        }

        if (isset($filtros['nome'])) {
            $query->where('nome_completo', 'like', "%{$filtros['nome']}%");
        }

        return $query->latest()->paginate(15);
    }
}
```

---

### 10. Queries Eloquent Avançadas

#### Eager Loading (Evitar N+1)

```php
// ❌ Ruim: N+1 queries
$pacientes = Paciente::all();
foreach ($pacientes as $paciente) {
    echo $paciente->atendimentos->count(); // Query para cada paciente
}

// ✅ Bom: 2 queries apenas
$pacientes = Paciente::with('atendimentos.medico')->get();
foreach ($pacientes as $paciente) {
    echo $paciente->atendimentos->count(); // Sem queries adicionais
}
```

#### Chunk para Dados Pesados

```php
// ❌ Ruim: Carrega tudo na memória
$pacientes = Paciente::all();
foreach ($pacientes as $paciente) {
    // Processar...
}

// ✅ Bom: Processa em lotes
Paciente::chunk(500, function ($pacientes) {
    foreach ($pacientes as $paciente) {
        // Processar...
    }
});
```

#### Queries com Scopes

```php
// No Model
public function scopePorTriagem($query, string $triagem)
{
    return $query->where('triagem', $triagem);
}

public function scopeAguardando($query)
{
    return $query->where('status', 'aguardando');
}

// Uso
$pacientes = Paciente::porTriagem('vermelho')
    ->aguardando()
    ->latest()
    ->get();
```

---

## 📋 Checklist de Uso

### Ao Criar Controller
- [ ] Herda de `Controller`
- [ ] Usa Form Requests para validação
- [ ] Usa Services para lógica complexa
- [ ] Retorna views ou JSON apropriados
- [ ] Usa route model binding quando possível

### Ao Criar Model
- [ ] Define `$fillable` ou `$guarded`
- [ ] Define `$casts` para tipos
- [ ] Define relacionamentos
- [ ] Cria scopes reutilizáveis
- [ ] Usa accessors/mutators quando necessário

### Ao Criar Migration
- [ ] Sempre cria método `down()`
- [ ] Adiciona índices em foreign keys
- [ ] Adiciona índices em colunas de busca frequente
- [ ] Usa tipos apropriados (enum, date, etc.)

### Ao Criar Form Request
- [ ] Define método `authorize()`
- [ ] Define método `rules()`
- [ ] Customiza mensagens se necessário
- [ ] Usa validação condicional quando necessário

---

## 🔍 Reflexão sobre Escalabilidade e Manutenibilidade

### Escalabilidade
Exemplos práticos bem organizados permitem que a IA crie código escalável desde o início. Padrões como Services, Repositories e Eager Loading garantem que o código suporte crescimento.

**Considerações futuras:**
- Adicionar exemplos de padrões mais avançados conforme necessário
- Manter exemplos atualizados com novas versões do Laravel

### Manutenibilidade
Código seguindo padrões claros é mais fácil de manter. Exemplos servem como referência rápida para decisões de implementação. Padrões consistentes facilitam entendimento.

**Melhorias sugeridas:**
- Adicionar mais exemplos de casos complexos
- Criar exemplos de integração entre componentes
- Adicionar exemplos de testes para cada padrão

---

---

## ⚠️ Notas Importantes sobre Laravel 12

### Mudanças Principais

1. **SoftDeletes:**
   - ❌ **Depreciado:** `protected $dates = ['deleted_at'];`
   - ✅ **Correto:** O trait `SoftDeletes` automaticamente faz o cast de `deleted_at`
   - Use `$casts` apenas se precisar de outros tipos de cast

2. **Middleware:**
   - ❌ **Antigo (Laravel 10 e anteriores):** Registro em `app/Http/Kernel.php`
   - ✅ **Novo (Laravel 11+):** Registro em `bootstrap/app.php` usando `withMiddleware()`

3. **Form Requests:**
   - ✅ Sempre importe `Illuminate\Validation\Rule` quando usar `Rule::unique()` ou outras regras do Rule

4. **Migrations:**
   - ✅ Use classes anônimas: `return new class extends Migration`
   - ✅ Métodos `up()` e `down()` devem retornar `void`

5. **Type Hints:**
   - ✅ Use type hints de retorno (`: RedirectResponse`, `: View`, etc.) quando possível
   - ✅ Importe os tipos necessários: `use Illuminate\Http\RedirectResponse;`, `use Illuminate\View\View;`

6. **Helpers de Redirecionamento:**
   - ✅ **Recomendado:** Use `to_route()` em vez de `redirect()->route()`
   - ✅ Mais conciso e legível: `to_route('pacientes.show', $paciente)`

---

**Última Atualização:** 2025-01-27  
**Versão Laravel:** 12.x  
**Baseado em:** `qi/PHP e Laravel Crie aplicações web como um verdadeiro artesão.md` + Documentação oficial Laravel 12.x

