---json
{
  "id": "documentacao-php",
  "title": "PHP 8.3 — Guia Completo",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "Guia tecnico e referencias sobre PHP 8.3 — Guia Completo.",
  "gatilhos": [
    "completo",
    "documentacao",
    "guia",
    "linguagens",
    "php"
  ],
  "perguntas_tipo": [
    "Como utilizar PHP 8.3 — Guia Completo?",
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

# PHP 8.3 — Guia Completo

**Fonte:** [php.net/docs](https://www.php.net/docs.php) · [php.net/manual/pt_BR](https://www.php.net/manual/pt_BR/)  
**Versão:** PHP 8.3  
**Categoria:** Backend · Linguagem  
**Última Atualização do Conteúdo:** 2026-02-14  
**Último Acesso às Fontes:** 2026-02-14

---

## 1. Tipos e Variáveis

```php
<?php

// Tipos escalares
$nome = 'João';              // string
$idade = 30;                 // int
$preco = 19.99;              // float
$ativo = true;               // bool
$nulo = null;                // null

// Tipo declarado (PHP 7+)
function soma(int $a, int $b): int {
    return $a + $b;
}

// Nullable
function findUser(?int $id): ?User {
    return $id ? User::find($id) : null;
}

// Union types (PHP 8.0+)
function parse(string|int $value): string {
    return (string) $value;
}

// Intersection types (PHP 8.1+)
function process(Countable&Iterator $collection): void { /* ... */ }

// Readonly (PHP 8.1+)
readonly class Point {
    public function __construct(
        public float $x,
        public float $y,
    ) {}
}

// Enums (PHP 8.1+)
enum Status: string {
    case Active = 'active';
    case Inactive = 'inactive';
    case Pending = 'pending';
}

$status = Status::Active;
$status->value;  // 'active'
```

---

## 2. Strings

```php
$nome = 'João';
$msg = "Olá, {$nome}!";   // Interpolação (aspas duplas)

// Métodos (funções)
strlen($nome);              // 4
strtoupper($nome);          // 'JOÃO'
strtolower($nome);          // 'joão'
str_contains($msg, 'Olá'); // true (PHP 8.0+)
str_starts_with($msg, 'O');// true (PHP 8.0+)
str_ends_with($msg, '!');  // true (PHP 8.0+)
substr($nome, 0, 2);       // 'Jo'
str_replace('João', 'Maria', $msg);
trim($texto);
explode(',', 'a,b,c');     // ['a','b','c']
implode(', ', $array);     // 'a, b, c'
sprintf('Nome: %s, Idade: %d', $nome, $idade);
```

---

## 3. Arrays

```php
// Array indexado
$frutas = ['maçã', 'banana', 'uva'];

// Array associativo
$user = [
    'name' => 'João',
    'email' => 'joao@email.com',
    'age' => 30,
];

// Adicionar
$frutas[] = 'manga';
array_push($frutas, 'pêra');

// Funções úteis
count($frutas);
in_array('banana', $frutas);       // true
array_key_exists('name', $user);   // true
array_keys($user);                 // ['name','email','age']
array_values($user);
array_unique([1,2,2,3]);           // [1,2,3]
array_merge($arr1, $arr2);
array_slice($frutas, 1, 2);       // ['banana','uva']
array_splice($frutas, 1, 1);      // Remove 'banana'

// Transformar
$upper = array_map(fn($f) => strtoupper($f), $frutas);
$comA = array_filter($frutas, fn($f) => str_contains($f, 'a'));
$soma = array_reduce($nums, fn($acc, $n) => $acc + $n, 0);

// Ordenar
sort($frutas);       // Crescente
rsort($frutas);      // Decrescente
usort($users, fn($a, $b) => $a['age'] <=> $b['age']);

// Destructuring
['name' => $name, 'email' => $email] = $user;
[$primeiro, $segundo] = $frutas;

// Spread (PHP 7.4+)
$merged = [...$arr1, ...$arr2];
```

---

## 4. POO (Classes)

```php
class User {
    // Constructor promotion (PHP 8.0+)
    public function __construct(
        private readonly string $name,
        private readonly string $email,
        private string $role = 'user',
    ) {}

    public function getName(): string {
        return $this->name;
    }

    public function isAdmin(): bool {
        return $this->role === 'admin';
    }

    // Método estático
    public static function create(array $data): self {
        return new self(
            name: $data['name'],
            email: $data['email'],
            role: $data['role'] ?? 'user',
        );
    }
}

// Herança
class Admin extends User {
    public function __construct(
        string $name,
        string $email,
        private array $permissions = [],
    ) {
        parent::__construct($name, $email, 'admin');
    }

    public function hasPermission(string $perm): bool {
        return in_array($perm, $this->permissions);
    }
}

// Interface
interface Authenticatable {
    public function getAuthIdentifier(): string;
    public function getPassword(): string;
}

// Trait
trait HasTimestamps {
    public \DateTimeInterface $createdAt;
    public \DateTimeInterface $updatedAt;

    public function touch(): void {
        $this->updatedAt = new \DateTimeImmutable();
    }
}
```

---

## 5. Match Expression (PHP 8.0+)

```php
$result = match($status) {
    'active' => 'Ativo',
    'inactive', 'suspended' => 'Inativo',
    'pending' => 'Pendente',
    default => 'Desconhecido',
};

// Named arguments (PHP 8.0+)
$user = User::create(
    name: 'João',
    email: 'joao@email.com',
);
```

---

## 6. Error Handling

```php
try {
    $result = riskyOperation();
} catch (InvalidArgumentException $e) {
    log('Argumento inválido: ' . $e->getMessage());
} catch (\Throwable $e) {
    log('Erro geral: ' . $e->getMessage());
} finally {
    cleanup();
}

// Exceção customizada
class ValidationException extends \RuntimeException {
    public function __construct(
        private array $errors,
        string $message = 'Validation failed',
    ) {
        parent::__construct($message);
    }

    public function getErrors(): array {
        return $this->errors;
    }
}
```

---

## 7. Fibers (PHP 8.1+)

```php
$fiber = new Fiber(function (): void {
    $data = Fiber::suspend('waiting for data');
    echo "Received: $data";
});

$result = $fiber->start();   // 'waiting for data'
$fiber->resume('hello');     // 'Received: hello'
```

---

## 8. PDO (Banco de Dados)

```php
$pdo = new PDO(
    'mysql:host=localhost;dbname=mydb;charset=utf8mb4',
    'root', 'password',
    [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]
);

// Prepared statement (SEMPRE use para evitar SQL Injection)
$stmt = $pdo->prepare('SELECT * FROM users WHERE email = :email');
$stmt->execute(['email' => $email]);
$user = $stmt->fetch(PDO::FETCH_ASSOC);

// Insert
$stmt = $pdo->prepare('INSERT INTO users (name, email) VALUES (:name, :email)');
$stmt->execute(['name' => 'João', 'email' => 'joao@email.com']);
$id = $pdo->lastInsertId();

// Transaction
$pdo->beginTransaction();
try {
    $pdo->exec("UPDATE accounts SET balance = balance - 100 WHERE id = 1");
    $pdo->exec("UPDATE accounts SET balance = balance + 100 WHERE id = 2");
    $pdo->commit();
} catch (\Exception $e) {
    $pdo->rollBack();
    throw $e;
}
```

---

## 9. Features PHP 8.3

```php
// Typed class constants
class Config {
    const string VERSION = '1.0.0';
    const int MAX_RETRIES = 3;
}

// #[\Override] attribute
class Child extends Parent {
    #[\Override]
    public function method(): void { /* ... */ }
}

// json_validate()
if (json_validate($jsonString)) {
    $data = json_decode($jsonString);
}
```

---

## 10. Boas Práticas

1. **Sempre use `declare(strict_types=1);`** no topo dos arquivos
2. **Use Composer** para dependências e autoload PSR-4
3. **Prepared Statements** para queries SQL (nunca concatene!)
4. **Type declarations** em parâmetros e retornos
5. **Constructor Promotion** para código mais limpo
6. **Enums** no lugar de constantes para valores finitos

---

*Fontes: [php.net/docs](https://www.php.net/docs.php) · [php.net/manual/pt_BR](https://www.php.net/manual/pt_BR/) — Acessado em 2026-02-14*
