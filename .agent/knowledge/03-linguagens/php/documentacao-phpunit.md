---json
{
  "id": "documentacao-phpunit",
  "title": "Testes PHP — PHPUnit Guia Completo",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "Guia tecnico e referencias sobre Testes PHP — PHPUnit Guia Completo.",
  "gatilhos": [
    "completo",
    "documentacao",
    "guia",
    "linguagens",
    "php",
    "phpunit",
    "testes"
  ],
  "perguntas_tipo": [
    "Como utilizar Testes PHP — PHPUnit Guia Completo?",
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

# Testes PHP — PHPUnit Guia Completo

**Fonte:** [phpunit.de](https://phpunit.de/documentation.html) · [freecodecamp.org](https://www.freecodecamp.org/news/test-php-code-with-phpunit/)  
**Versão:** PHPUnit 11.x / 10.x  
**Categoria:** Testes · Backend · PHP  
**Última Atualização do Conteúdo:** 2026-02-14  
**Último Acesso às Fontes:** 2026-02-14

---

## 1. O que é PHPUnit?

PHPUnit é o **framework de testes padrão** para PHP. Usado nativamente pelo Laravel, Symfony e praticamente todo projeto PHP moderno. Permite testes unitários, de integração e funcionais.

---

## 2. Instalação

```bash
# Via Composer (RECOMENDADO)
composer require --dev phpunit/phpunit

# Laravel já inclui PHPUnit!
# Basta rodar:
php artisan test
# ou
./vendor/bin/phpunit
```

### Configuração (`phpunit.xml`)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<phpunit bootstrap="vendor/autoload.php"
         colors="true"
         stopOnFailure="false"
         cacheDirectory=".phpunit.cache">
    <testsuites>
        <testsuite name="Unit">
            <directory>tests/Unit</directory>
        </testsuite>
        <testsuite name="Feature">
            <directory>tests/Feature</directory>
        </testsuite>
    </testsuites>
    <source>
        <include>
            <directory>app</directory>
        </include>
    </source>
    <php>
        <env name="APP_ENV" value="testing"/>
        <env name="DB_DATABASE" value="test_db"/>
    </php>
</phpunit>
```

---

## 3. Estrutura de Testes

```
tests/
├── Unit/                     # Testes unitários (sem DB, sem HTTP)
│   ├── Services/
│   │   └── UserServiceTest.php
│   └── Helpers/
│       └── StringHelperTest.php
├── Feature/                  # Testes de integração (com DB, HTTP)
│   ├── Api/
│   │   └── UserApiTest.php
│   └── Auth/
│       └── LoginTest.php
└── TestCase.php              # Classe base (Laravel)
```

---

## 4. Anatomia de um Teste

```php
<?php

namespace Tests\Unit;

use PHPUnit\Framework\TestCase;
use App\Services\Calculator;

class CalculatorTest extends TestCase
{
    private Calculator $calculator;

    // Executa ANTES de cada teste
    protected function setUp(): void
    {
        parent::setUp();
        $this->calculator = new Calculator();
    }

    // Executa DEPOIS de cada teste
    protected function tearDown(): void
    {
        parent::tearDown();
    }

    // ✅ Teste básico
    public function test_soma_dois_numeros(): void
    {
        $resultado = $this->calculator->soma(2, 3);
        $this->assertEquals(5, $resultado);
    }

    // ✅ Teste com atributo (PHPUnit 10+)
    #[Test]
    public function deve_subtrair_corretamente(): void
    {
        $this->assertEquals(7, $this->calculator->subtrair(10, 3));
    }

    // ✅ Teste com data provider
    #[DataProvider('somaCasosProvider')]
    public function test_soma_multiplos_casos(int $a, int $b, int $esperado): void
    {
        $this->assertEquals($esperado, $this->calculator->soma($a, $b));
    }

    public static function somaCasosProvider(): array
    {
        return [
            'positivos'     => [2, 3, 5],
            'negativos'     => [-1, -2, -3],
            'zero'          => [0, 0, 0],
            'misto'         => [-1, 5, 4],
        ];
    }
}
```

---

## 5. Assertions (Verificações)

### Igualdade e Tipo
```php
$this->assertEquals(5, $resultado);              // Valor igual (type coercion)
$this->assertSame(5, $resultado);                // Valor E tipo iguais (strict)
$this->assertNotEquals('admin', $role);
$this->assertTrue($user->isActive());
$this->assertFalse($user->isBlocked());
$this->assertNull($user->deletedAt);
$this->assertNotNull($user->email);
```

### Strings
```php
$this->assertStringContainsString('Hello', $response);
$this->assertStringStartsWith('Error:', $message);
$this->assertStringEndsWith('.pdf', $filename);
$this->assertMatchesRegularExpression('/^\d{3}\.\d{3}\.\d{3}-\d{2}$/', $cpf);
$this->assertEmpty($errors);
$this->assertNotEmpty($results);
```

### Arrays e Coleções
```php
$this->assertCount(3, $users);
$this->assertContains('admin', $roles);
$this->assertArrayHasKey('email', $userData);
$this->assertIsArray($result);
```

### Tipos
```php
$this->assertIsString($name);
$this->assertIsInt($age);
$this->assertIsBool($active);
$this->assertIsFloat($price);
$this->assertInstanceOf(User::class, $user);
```

### Exceções
```php
public function test_divide_por_zero_lanca_excecao(): void
{
    $this->expectException(\DivisionByZeroError::class);
    $this->expectExceptionMessage('Division by zero');

    $this->calculator->dividir(10, 0);
}
```

---

## 6. Testes Laravel (Feature Tests)

### Teste de API
```php
<?php

namespace Tests\Feature\Api;

use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class UserApiTest extends TestCase
{
    use RefreshDatabase;  // Reseta DB a cada teste

    public function test_listar_usuarios(): void
    {
        User::factory()->count(5)->create();

        $response = $this->getJson('/api/users');

        $response->assertStatus(200)
                 ->assertJsonCount(5, 'data')
                 ->assertJsonStructure([
                     'data' => [
                         '*' => ['id', 'name', 'email', 'created_at']
                     ]
                 ]);
    }

    public function test_criar_usuario(): void
    {
        $response = $this->postJson('/api/users', [
            'name' => 'João Silva',
            'email' => 'joao@email.com',
            'password' => 'senha123',
        ]);

        $response->assertStatus(201)
                 ->assertJsonFragment(['name' => 'João Silva']);

        $this->assertDatabaseHas('users', [
            'email' => 'joao@email.com',
        ]);
    }

    public function test_validacao_email_obrigatorio(): void
    {
        $response = $this->postJson('/api/users', [
            'name' => 'João',
            // email faltando
        ]);

        $response->assertStatus(422)
                 ->assertJsonValidationErrors(['email']);
    }

    public function test_deletar_usuario(): void
    {
        $user = User::factory()->create();

        $response = $this->deleteJson("/api/users/{$user->id}");

        $response->assertStatus(204);
        $this->assertDatabaseMissing('users', ['id' => $user->id]);
    }
}
```

### Teste de Autenticação
```php
public function test_rota_protegida_sem_auth(): void
{
    $response = $this->getJson('/api/dashboard');
    $response->assertStatus(401);
}

public function test_rota_protegida_com_auth(): void
{
    $user = User::factory()->create();

    $response = $this->actingAs($user)
                     ->getJson('/api/dashboard');

    $response->assertStatus(200);
}
```

---

## 7. Mocks e Stubs

```php
use PHPUnit\Framework\TestCase;

class PaymentServiceTest extends TestCase
{
    public function test_processa_pagamento(): void
    {
        // Criar mock do gateway de pagamento
        $gateway = $this->createMock(PaymentGateway::class);

        // Configurar expectativa
        $gateway->expects($this->once())
                ->method('charge')
                ->with(100.00, 'card_token_123')
                ->willReturn(true);

        // Injetar mock
        $service = new PaymentService($gateway);
        $result = $service->processPayment(100.00, 'card_token_123');

        $this->assertTrue($result);
    }

    public function test_falha_no_pagamento(): void
    {
        $gateway = $this->createMock(PaymentGateway::class);
        $gateway->method('charge')
                ->willThrowException(new \RuntimeException('Gateway offline'));

        $service = new PaymentService($gateway);

        $this->expectException(\RuntimeException::class);
        $service->processPayment(100.00, 'card_token_123');
    }
}
```

---

## 8. Comandos

```bash
# Rodar todos os testes
./vendor/bin/phpunit
php artisan test                    # Laravel

# Rodar um arquivo
./vendor/bin/phpunit tests/Unit/CalculatorTest.php

# Rodar um método
./vendor/bin/phpunit --filter test_soma_dois_numeros

# Rodar uma suite
./vendor/bin/phpunit --testsuite Unit
./vendor/bin/phpunit --testsuite Feature

# Com coverage
./vendor/bin/phpunit --coverage-html reports/coverage

# Parar no primeiro erro
./vendor/bin/phpunit --stop-on-failure

# Modo verboso
./vendor/bin/phpunit -v

# Laravel: com paralelismo
php artisan test --parallel
```

---

## 9. Boas Práticas

1. **Nomeie testes descritivamente:** `test_usuario_nao_pode_acessar_sem_login`
2. **Um assert por teste** (quando possível)
3. **Use `RefreshDatabase`** em testes de Feature
4. **Use Factories** para criar dados de teste
5. **Teste o comportamento**, não a implementação
6. **Organize:** `tests/Unit/` para lógica pura, `tests/Feature/` para HTTP

---

*Fontes: [phpunit.de](https://phpunit.de/documentation.html) · [freecodecamp.org/phpunit](https://www.freecodecamp.org/news/test-php-code-with-phpunit/) — Acessado em 2026-02-14*
