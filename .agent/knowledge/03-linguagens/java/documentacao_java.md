---json
{
  "id": "documentacao_java",
  "title": "Documentação Java — Guia Completo",
  "categoria": "03-linguagens",
  "subcategoria": "java",
  "resumo": "**Fonte:** [W3Schools Java](https://www.w3schools.com/java/default.asp) · [Oracle Java Docs](https://docs.oracle.com/javase/) **Versão:** Java 21+ (LTS)",
  "gatilhos": [
    "completo",
    "documentacao",
    "guia",
    "java",
    "linguagens"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação Java — Guia Completo?",
    "Quais as boas praticas de java?"
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
  "dono": "stack-java",
  "prioridade": 2
}
---

# Documentação Java — Guia Completo

> **Fonte:** [W3Schools Java](https://www.w3schools.com/java/default.asp) · [Oracle Java Docs](https://docs.oracle.com/javase/)
> **Versão:** Java 21+ (LTS)
> **Atualizado:** 2026-02-14

---

## Sumário

1. [Fundamentos](#fundamentos)
2. [Tipos de Dados](#tipos-de-dados)
3. [Controle de Fluxo](#controle-de-fluxo)
4. [Arrays e Strings](#arrays-e-strings)
5. [Métodos](#métodos)
6. [OOP — Classes e Objetos](#oop--classes-e-objetos)
7. [Herança e Polimorfismo](#herança-e-polimorfismo)
8. [Interfaces e Abstração](#interfaces-e-abstração)
9. [Tratamento de Erros](#tratamento-de-erros)
10. [Coleções (Collections)](#coleções-collections)
11. [I/O e Arquivos](#io-e-arquivos)
12. [Streams e Lambdas](#streams-e-lambdas)

---

## Fundamentos

### Hello World

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

### Compilar e executar

```bash
javac Main.java    # Compila → Main.class
java Main          # Executa
```

### Variáveis

```java
// Tipos primitivos
int idade = 25;
double salario = 4500.50;
float pi = 3.14f;
long populacao = 7_900_000_000L;
char letra = 'A';
boolean ativo = true;
byte b = 127;
short s = 32000;

// Tipo referência
String nome = "João";

// Constantes
final double PI = 3.14159265;

// var (Java 10+) — inferência de tipo
var lista = new ArrayList<String>();
```

---

## Tipos de Dados

| Tipo | Tamanho | Range |
|---|---|---|
| `byte` | 1 byte | -128 a 127 |
| `short` | 2 bytes | -32.768 a 32.767 |
| `int` | 4 bytes | -2³¹ a 2³¹-1 |
| `long` | 8 bytes | -2⁶³ a 2⁶³-1 |
| `float` | 4 bytes | ~7 dígitos decimais |
| `double` | 8 bytes | ~15 dígitos decimais |
| `char` | 2 bytes | Unicode (0 a 65.535) |
| `boolean` | 1 bit | true / false |

### Casting

```java
// Widening (automático): menor → maior
int i = 100;
double d = i;  // 100.0

// Narrowing (manual): maior → menor
double x = 9.78;
int y = (int) x;  // 9
```

---

## Controle de Fluxo

```java
// if-else
if (idade >= 18) {
    System.out.println("Maior de idade");
} else if (idade >= 12) {
    System.out.println("Adolescente");
} else {
    System.out.println("Criança");
}

// Ternário
String status = (idade >= 18) ? "adulto" : "menor";

// switch (tradicional)
switch (dia) {
    case 1: System.out.println("Segunda"); break;
    case 2: System.out.println("Terça"); break;
    default: System.out.println("Outro");
}

// switch expression (Java 14+)
String resultado = switch (dia) {
    case 1 -> "Segunda";
    case 2 -> "Terça";
    default -> "Outro";
};

// for
for (int i = 0; i < 10; i++) { }

// for-each
for (String item : lista) { }

// while
while (condicao) { }

// do-while
do { } while (condicao);
```

---

## Arrays e Strings

### Arrays

```java
// Declaração
int[] numeros = {1, 2, 3, 4, 5};
String[] nomes = new String[3];
nomes[0] = "Ana";

// Multidimensional
int[][] matrix = {{1, 2}, {3, 4}, {5, 6}};

// Percorrer
for (int n : numeros) { System.out.println(n); }
Arrays.sort(numeros);
System.out.println(Arrays.toString(numeros));
```

### Strings

```java
String s = "Hello World";
s.length();                    // 11
s.toUpperCase();               // "HELLO WORLD"
s.toLowerCase();               // "hello world"
s.trim();                      // Remove espaços
s.indexOf("World");            // 6
s.substring(0, 5);             // "Hello"
s.replace("World", "Java");    // "Hello Java"
s.split(" ");                  // ["Hello", "World"]
s.contains("World");           // true
s.equals("Hello World");       // true (comparação correta)
s.charAt(0);                   // 'H'
String.format("Olá %s, %d anos", nome, idade);

// StringBuilder (mutável, melhor performance)
StringBuilder sb = new StringBuilder();
sb.append("Hello").append(" ").append("World");
String result = sb.toString();

// Text blocks (Java 15+)
String json = """
    {
        "nome": "João",
        "idade": 25
    }
    """;
```

---

## Métodos

```java
// Método com retorno
public static int somar(int a, int b) {
    return a + b;
}

// Método void
public static void exibir(String msg) {
    System.out.println(msg);
}

// Varargs
public static int soma(int... numeros) {
    int total = 0;
    for (int n : numeros) total += n;
    return total;
}
soma(1, 2, 3, 4); // 10

// Overloading (mesmo nome, params diferentes)
public static double area(double r)           { return Math.PI * r * r; }
public static double area(double l, double a) { return l * a; }

// Recursão
public static int fatorial(int n) {
    return (n <= 1) ? 1 : n * fatorial(n - 1);
}
```

---

## OOP — Classes e Objetos

```java
public class Pessoa {
    // Atributos (encapsulados)
    private String nome;
    private int idade;
    private static int contador = 0; // Compartilhado

    // Construtor
    public Pessoa(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
        contador++;
    }

    // Construtor vazio
    public Pessoa() {
        this("Anônimo", 0);
    }

    // Getters e Setters
    public String getNome() { return nome; }
    public void setNome(String nome) { this.nome = nome; }
    public int getIdade() { return idade; }

    // Método
    public String apresentar() {
        return String.format("Sou %s, %d anos", nome, idade);
    }

    // toString
    @Override
    public String toString() {
        return "Pessoa{nome='" + nome + "', idade=" + idade + "}";
    }

    // Static method
    public static int getContador() { return contador; }
}

// Uso
Pessoa p = new Pessoa("Maria", 30);
System.out.println(p.apresentar());
```

### Modificadores de Acesso

| Modificador | Classe | Pacote | Subclasse | Global |
|---|---|---|---|---|
| `public` | ✅ | ✅ | ✅ | ✅ |
| `protected` | ✅ | ✅ | ✅ | ❌ |
| (default) | ✅ | ✅ | ❌ | ❌ |
| `private` | ✅ | ❌ | ❌ | ❌ |

---

## Herança e Polimorfismo

```java
// Classe base
public class Animal {
    protected String nome;

    public Animal(String nome) { this.nome = nome; }

    public void emitirSom() {
        System.out.println("...");
    }
}

// Herança
public class Cachorro extends Animal {
    public Cachorro(String nome) { super(nome); }

    @Override
    public void emitirSom() {
        System.out.println(nome + " diz: Au au!");
    }
}

public class Gato extends Animal {
    public Gato(String nome) { super(nome); }

    @Override
    public void emitirSom() {
        System.out.println(nome + " diz: Miau!");
    }
}

// Polimorfismo
Animal a1 = new Cachorro("Rex");
Animal a2 = new Gato("Mimi");
a1.emitirSom(); // "Rex diz: Au au!"
a2.emitirSom(); // "Mimi diz: Miau!"
```

---

## Interfaces e Abstração

```java
// Interface
public interface Pagavel {
    double calcularPagamento();           // Abstrato
    default String moeda() { return "BRL"; } // Default method
    static double converter(double v) { return v * 5.0; } // Static
}

// Classe abstrata
public abstract class Forma {
    protected String cor;
    public abstract double area();         // Deve ser implementado
    public void exibirCor() { System.out.println(cor); } // Concreto
}

// Implementação
public class Circulo extends Forma implements Pagavel {
    private double raio;

    public Circulo(double raio, String cor) {
        this.raio = raio;
        this.cor = cor;
    }

    @Override
    public double area() { return Math.PI * raio * raio; }

    @Override
    public double calcularPagamento() { return area() * 10; }
}

// Enum
public enum Status {
    ATIVO("Em uso"),
    INATIVO("Parado"),
    MANUTENCAO("Em reparo");

    private final String descricao;
    Status(String desc) { this.descricao = desc; }
    public String getDescricao() { return descricao; }
}
```

---

## Tratamento de Erros

```java
// try-catch-finally
try {
    int resultado = 10 / 0;
} catch (ArithmeticException e) {
    System.out.println("Erro: " + e.getMessage());
} catch (Exception e) {
    System.out.println("Erro genérico: " + e);
} finally {
    System.out.println("Sempre executa");
}

// try-with-resources (Java 7+)
try (var reader = new BufferedReader(new FileReader("arquivo.txt"))) {
    String linha;
    while ((linha = reader.readLine()) != null) {
        System.out.println(linha);
    }
} catch (IOException e) {
    e.printStackTrace();
}

// Exceção customizada
public class SaldoInsuficienteException extends Exception {
    public SaldoInsuficienteException(String msg) { super(msg); }
}

// Lançar exceção
public void sacar(double valor) throws SaldoInsuficienteException {
    if (valor > saldo) throw new SaldoInsuficienteException("Saldo insuficiente");
    saldo -= valor;
}
```

---

## Coleções (Collections)

```java
// ArrayList (lista dinâmica)
List<String> nomes = new ArrayList<>();
nomes.add("Ana");
nomes.add("Bruno");
nomes.get(0);        // "Ana"
nomes.remove(0);
nomes.size();
nomes.contains("Bruno");

// LinkedList
List<Integer> nums = new LinkedList<>();

// HashMap
Map<String, Integer> idades = new HashMap<>();
idades.put("Ana", 25);
idades.get("Ana");     // 25
idades.containsKey("Ana");
idades.getOrDefault("X", 0);
for (var entry : idades.entrySet()) {
    System.out.println(entry.getKey() + ": " + entry.getValue());
}

// HashSet (sem duplicatas)
Set<String> tags = new HashSet<>();
tags.add("java");
tags.add("java"); // Ignorado

// Queue / Deque
Queue<String> fila = new LinkedList<>();
fila.offer("primeiro");
fila.poll();  // Remove e retorna

// Collections utility
Collections.sort(nomes);
Collections.reverse(nomes);
Collections.unmodifiableList(nomes);
```

---

## I/O e Arquivos

```java
import java.nio.file.*;

// Ler arquivo inteiro (Java 11+)
String conteudo = Files.readString(Path.of("arquivo.txt"));

// Ler linhas
List<String> linhas = Files.readAllLines(Path.of("dados.csv"));

// Escrever
Files.writeString(Path.of("saida.txt"), "Conteúdo aqui");

// Append
Files.writeString(Path.of("log.txt"), "Nova linha\n",
    StandardOpenOption.CREATE, StandardOpenOption.APPEND);

// Listar diretório
try (var stream = Files.list(Path.of("."))) {
    stream.filter(Files::isRegularFile)
          .forEach(System.out::println);
}

// Verificar existência
Files.exists(Path.of("arquivo.txt"));
Files.isDirectory(Path.of("pasta"));
```

---

## Streams e Lambdas

```java
// Lambda
Comparator<String> comp = (a, b) -> a.length() - b.length();
Runnable task = () -> System.out.println("Executando");

// Stream API
List<String> nomes = List.of("Ana", "Bruno", "Carlos", "Diana", "Eva");

// Filtrar, transformar, coletar
List<String> resultado = nomes.stream()
    .filter(n -> n.length() > 3)           // Bruno, Carlos, Diana
    .map(String::toUpperCase)              // BRUNO, CARLOS, DIANA
    .sorted()                              // BRUNO, CARLOS, DIANA
    .collect(Collectors.toList());

// Estatísticas numéricas
IntStream.rangeClosed(1, 100)
    .filter(n -> n % 2 == 0)
    .average()
    .ifPresent(System.out::println);  // 51.0

// Map com streams
Map<Character, List<String>> agrupado = nomes.stream()
    .collect(Collectors.groupingBy(n -> n.charAt(0)));

// Optional (evitar null)
Optional<String> opt = nomes.stream().filter(n -> n.startsWith("X")).findFirst();
String valor = opt.orElse("Não encontrado");

// Parallel stream
long count = nomes.parallelStream()
    .filter(n -> n.contains("a"))
    .count();
```

---

## Records e Sealed Classes (Java 16+)

```java
// Record — classe imutável automática
public record Ponto(double x, double y) {
    // Getters, equals, hashCode, toString automáticos
    public double distancia(Ponto outro) {
        return Math.sqrt(Math.pow(x - outro.x, 2) + Math.pow(y - outro.y, 2));
    }
}
var p = new Ponto(3, 4);
System.out.println(p.x()); // 3

// Sealed class (Java 17+)
public sealed class Forma permits Circulo, Retangulo, Triangulo { }
public final class Circulo extends Forma { }
public final class Retangulo extends Forma { }
public non-sealed class Triangulo extends Forma { }

// Pattern matching (Java 21+)
if (obj instanceof String s && s.length() > 5) {
    System.out.println(s.toUpperCase());
}
```

---

*Fonte: [W3Schools Java](https://www.w3schools.com/java/) · [Oracle Java SE Docs](https://docs.oracle.com/javase/)*
