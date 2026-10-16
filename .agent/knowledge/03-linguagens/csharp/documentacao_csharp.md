---json
{
  "id": "documentacao_csharp",
  "title": "Documentação C— Guia Completo",
  "categoria": "03-linguagens",
  "subcategoria": "csharp",
  "resumo": "**Fonte:** [W3Schools C#](https://www.w3schools.com/cs/index.php) · [Microsoft Learn](https://learn.microsoft.com/dotnet/csharp/) **Versão:** C# 12 / .NET 8+",
  "gatilhos": [
    "completo",
    "csharp",
    "documentacao",
    "guia",
    "linguagens"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação C— Guia Completo?",
    "Quais as boas praticas de csharp?"
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
  "dono": "stack-csharp",
  "prioridade": 2
}
---

# Documentação C# — Guia Completo

> **Fonte:** [W3Schools C#](https://www.w3schools.com/cs/index.php) · [Microsoft Learn](https://learn.microsoft.com/dotnet/csharp/)
> **Versão:** C# 12 / .NET 8+
> **Atualizado:** 2026-02-14

---

## Sumário

1. [Fundamentos](#fundamentos)
2. [Tipos de Dados](#tipos-de-dados)
3. [Controle de Fluxo](#controle-de-fluxo)
4. [Arrays e Coleções](#arrays-e-coleções)
5. [Métodos](#métodos)
6. [OOP — Classes](#oop--classes)
7. [Herança e Polimorfismo](#herança-e-polimorfismo)
8. [Interfaces e Abstração](#interfaces-e-abstração)
9. [Tratamento de Erros](#tratamento-de-erros)
10. [LINQ](#linq)
11. [Async/Await](#asyncawait)
12. [Recursos Modernos](#recursos-modernos)

---

## Fundamentos

```csharp
// Top-level statements (C# 9+)
Console.WriteLine("Hello, World!");

// ou forma clássica
namespace MeuApp;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Hello, World!");
    }
}
```

### Variáveis

```csharp
int idade = 25;
double salario = 4500.50;
decimal preco = 19.99m;
string nome = "Maria";
char letra = 'A';
bool ativo = true;

// var (inferência de tipo)
var lista = new List<string>();

// Constantes
const double PI = 3.14159;
readonly int maxRetries = 3;  // Apenas em classes

// Nullable
int? valor = null;
string? texto = null;
int resultado = valor ?? 0;   // Null coalescing
valor?.ToString();             // Null conditional
```

---

## Tipos de Dados

| Tipo | Tamanho | Range |
|---|---|---|
| `byte` | 1 byte | 0 a 255 |
| `short` | 2 bytes | -32.768 a 32.767 |
| `int` | 4 bytes | -2³¹ a 2³¹-1 |
| `long` | 8 bytes | -2⁶³ a 2⁶³-1 |
| `float` | 4 bytes | ~7 dígitos |
| `double` | 8 bytes | ~15 dígitos |
| `decimal` | 16 bytes | ~28 dígitos (financeiro) |
| `char` | 2 bytes | Unicode |
| `bool` | 1 byte | true/false |
| `string` | variável | Referência |

### String Interpolation

```csharp
var nome = "João";
var idade = 30;
Console.WriteLine($"Nome: {nome}, Idade: {idade}");
Console.WriteLine($"Salário: {salario:C2}");  // R$ 4.500,50
Console.WriteLine($"Data: {DateTime.Now:yyyy-MM-dd}");

// Raw string literals (C# 11)
var json = """
    {
        "nome": "João",
        "idade": 30
    }
    """;

// Verbatim strings
var path = @"C:\Users\Documents\file.txt";
```

---

## Controle de Fluxo

```csharp
// if-else
if (idade >= 18)
    Console.WriteLine("Adulto");
else if (idade >= 12)
    Console.WriteLine("Adolescente");
else
    Console.WriteLine("Criança");

// Ternário
var status = idade >= 18 ? "adulto" : "menor";

// switch expression (C# 8+)
var descricao = diaSemana switch
{
    DayOfWeek.Monday => "Segunda",
    DayOfWeek.Friday => "Sexta!",
    DayOfWeek.Saturday or DayOfWeek.Sunday => "Fim de semana",
    _ => "Dia útil"
};

// Pattern matching (C# 9+)
var classificacao = nota switch
{
    >= 9 => "A",
    >= 7 => "B",
    >= 5 => "C",
    _ => "D"
};

// for
for (int i = 0; i < 10; i++) { }

// foreach
foreach (var item in lista) { }

// while / do-while
while (condicao) { }
do { } while (condicao);
```

---

## Arrays e Coleções

```csharp
// Arrays
int[] nums = { 1, 2, 3, 4, 5 };
int[] zeros = new int[10];
string[,] matrix = { {"a", "b"}, {"c", "d"} };  // Multidimensional
int[][] jagged = new int[3][];  // Array of arrays

Array.Sort(nums);
Array.Reverse(nums);
Array.IndexOf(nums, 3);

// List<T>
var nomes = new List<string> { "Ana", "Bruno", "Carlos" };
nomes.Add("Diana");
nomes.Remove("Bruno");
nomes.Contains("Ana");
nomes.Sort();
nomes.Count;

// Dictionary<K,V>
var idades = new Dictionary<string, int>
{
    ["Ana"] = 25,
    ["Bruno"] = 30
};
idades["Carlos"] = 35;
idades.TryGetValue("Ana", out var idade);
foreach (var (key, value) in idades) { }

// HashSet<T>
var tags = new HashSet<string> { "c#", "dotnet" };

// Queue<T> e Stack<T>
var fila = new Queue<string>();
fila.Enqueue("primeiro");
var item = fila.Dequeue();

var pilha = new Stack<int>();
pilha.Push(1);
var topo = pilha.Pop();
```

---

## Métodos

```csharp
// Básico
static int Somar(int a, int b) => a + b;

// Parâmetros opcionais e nomeados
static void Log(string msg, int nivel = 1, bool timestamp = true)
{
    if (timestamp) Console.Write($"[{DateTime.Now:HH:mm}] ");
    Console.WriteLine(msg);
}
Log("Erro", nivel: 3);

// out e ref
static bool TryParse(string input, out int result)
{
    return int.TryParse(input, out result);
}

// params (varargs)
static int Soma(params int[] nums) => nums.Sum();
Soma(1, 2, 3, 4, 5);

// Tuplas
static (string Nome, int Idade) GetPessoa()
{
    return ("Ana", 25);
}
var (nome, idade) = GetPessoa();

// Extension methods
public static class StringExt
{
    public static bool IsNullOrEmpty(this string? s) =>
        string.IsNullOrEmpty(s);
}
"hello".IsNullOrEmpty(); // false
```

---

## OOP — Classes

```csharp
public class Pessoa
{
    // Properties (auto-implemented)
    public string Nome { get; set; }
    public int Idade { get; private set; }
    public string Email { get; init; }  // Init-only (C# 9)

    // Property com validação
    private double _salario;
    public double Salario
    {
        get => _salario;
        set => _salario = value >= 0 ? value : throw new ArgumentException("Negativo");
    }

    // Construtor primário (C# 12)
    // public class Pessoa(string nome, int idade);

    // Construtor
    public Pessoa(string nome, int idade)
    {
        Nome = nome;
        Idade = idade;
    }

    // Destrutor/Finalizer (raro)
    ~Pessoa() { }

    // Override ToString
    public override string ToString() => $"{Nome}, {Idade} anos";
}

// Record (C# 9+) — imutável, value equality
public record Ponto(double X, double Y);
var p1 = new Ponto(3, 4);
var p2 = p1 with { X = 5 };  // Cópia com mudança

// Record struct (C# 10)
public record struct Cor(byte R, byte G, byte B);
```

---

## Herança e Polimorfismo

```csharp
public abstract class Forma
{
    public string Cor { get; set; }
    public abstract double Area();
    public virtual void Desenhar()
    {
        Console.WriteLine($"Forma {Cor}");
    }
}

public class Circulo : Forma
{
    public double Raio { get; set; }

    public Circulo(double raio, string cor)
    {
        Raio = raio;
        Cor = cor;
    }

    public override double Area() => Math.PI * Raio * Raio;
    public override void Desenhar()
    {
        Console.WriteLine($"Circulo {Cor} r={Raio}");
    }
}

public sealed class Quadrado : Forma  // sealed: não herda
{
    public double Lado { get; set; }
    public override double Area() => Lado * Lado;
}

// Polimorfismo
List<Forma> formas = [new Circulo(5, "azul"), new Quadrado { Lado = 3, Cor = "red" }];
foreach (var f in formas)
    Console.WriteLine($"Área: {f.Area():F2}");

// Pattern matching com tipos (C# 7+)
if (forma is Circulo c)
    Console.WriteLine($"Raio: {c.Raio}");
```

---

## Interfaces e Abstração

```csharp
public interface IPagavel
{
    decimal CalcularPagamento();
    decimal Taxa => 0.05m;   // Default implementation (C# 8)
}

public interface ISerializavel
{
    string ToJson();
}

// Implementação múltipla
public class Fatura : IPagavel, ISerializavel
{
    public decimal Valor { get; set; }
    public decimal CalcularPagamento() => Valor * (1 + ((IPagavel)this).Taxa);
    public string ToJson() => $"{{\"valor\": {Valor}}}";
}

// Generic constraints
public interface IRepository<T> where T : class, new()
{
    T? GetById(int id);
    IEnumerable<T> GetAll();
    void Add(T entity);
    void Delete(int id);
}
```

---

## Tratamento de Erros

```csharp
try
{
    var resultado = Dividir(10, 0);
}
catch (DivideByZeroException ex)
{
    Console.WriteLine($"Erro: {ex.Message}");
}
catch (Exception ex) when (ex is not OutOfMemoryException)
{
    Console.WriteLine($"Erro filtrado: {ex.Message}");
}
finally
{
    Console.WriteLine("Cleanup");
}

// Exceção customizada
public class SaldoInsuficienteException : Exception
{
    public decimal Saldo { get; }
    public SaldoInsuficienteException(decimal saldo)
        : base($"Saldo insuficiente: {saldo:C2}")
    {
        Saldo = saldo;
    }
}

// using (IDisposable)
using var conn = new SqlConnection(connectionString);
using var reader = new StreamReader("arquivo.txt");
```

---

## LINQ

```csharp
using System.Linq;

var pessoas = new List<Pessoa>
{
    new("Ana", 25), new("Bruno", 30), new("Carlos", 22), new("Diana", 28)
};

// Query syntax
var jovens = from p in pessoas
             where p.Idade < 28
             orderby p.Nome
             select p.Nome;

// Method syntax (mais comum)
var resultado = pessoas
    .Where(p => p.Idade >= 25)
    .OrderBy(p => p.Nome)
    .Select(p => new { p.Nome, p.Idade })
    .ToList();

// Operações comuns
pessoas.First(p => p.Nome == "Ana");
pessoas.FirstOrDefault(p => p.Nome == "X");
pessoas.Any(p => p.Idade > 30);
pessoas.All(p => p.Idade > 18);
pessoas.Count(p => p.Idade >= 25);
pessoas.Average(p => p.Idade);
pessoas.Sum(p => p.Idade);
pessoas.Min(p => p.Idade);
pessoas.Max(p => p.Idade);
pessoas.GroupBy(p => p.Idade >= 25 ? "Senior" : "Junior");
pessoas.Distinct();
pessoas.Skip(1).Take(2);
```

---

## Async/Await

```csharp
// Método assíncrono
public async Task<string> FetchDataAsync(string url)
{
    using var client = new HttpClient();
    var response = await client.GetAsync(url);
    response.EnsureSuccessStatusCode();
    return await response.Content.ReadAsStringAsync();
}

// Paralelo
var tasks = urls.Select(url => FetchDataAsync(url));
var resultados = await Task.WhenAll(tasks);

// Cancelamento
var cts = new CancellationTokenSource(TimeSpan.FromSeconds(10));
try
{
    await Task.Delay(5000, cts.Token);
}
catch (OperationCanceledException) { }

// ValueTask (performance)
public ValueTask<int> GetCachedValueAsync(string key)
{
    if (_cache.TryGetValue(key, out var v)) return ValueTask.FromResult(v);
    return new ValueTask<int>(FetchAsync(key));
}

// IAsyncEnumerable (C# 8)
public async IAsyncEnumerable<int> GerarAsync()
{
    for (int i = 0; i < 10; i++)
    {
        await Task.Delay(100);
        yield return i;
    }
}
await foreach (var n in GerarAsync()) { Console.WriteLine(n); }
```

---

## Recursos Modernos

```csharp
// Collection expressions (C# 12)
int[] nums = [1, 2, 3, 4, 5];
List<string> nomes = ["Ana", "Bruno"];
Span<int> span = [1, 2, 3];

// Primary constructors (C# 12)
public class Service(ILogger logger, IRepository repo)
{
    public void Execute() => logger.Log("Executando");
}

// Global using (C# 10)
// Em GlobalUsings.cs:
global using System.Collections.Generic;
global using System.Linq;

// File-scoped namespace (C# 10)
namespace MeuApp;  // Sem chaves

// Required members (C# 11)
public class Config
{
    public required string ConnectionString { get; init; }
    public required int Port { get; init; }
}

// List patterns (C# 11)
var resultado = lista switch
{
    [var first, .., var last] => $"Primeiro: {first}, Último: {last}",
    [var single] => $"Único: {single}",
    [] => "Vazio",
};

// Span<T> (performance)
ReadOnlySpan<char> span = "Hello World".AsSpan();
var hello = span[..5]; // Sem alocação
```

---

*Fonte: [W3Schools C#](https://www.w3schools.com/cs/) · [Microsoft Learn](https://learn.microsoft.com/dotnet/csharp/)*
