---json
{
  "id": "documentacao_rust",
  "title": "Documentação Rust — Guia Completo",
  "categoria": "03-linguagens",
  "subcategoria": "rust",
  "resumo": "**Fonte:** [W3Schools Rust](https://www.w3schools.com/rust/index.php) · [The Rust Book](https://doc.rust-lang.org/book/) **Versão:** Rust 1.75+",
  "gatilhos": [
    "completo",
    "documentacao",
    "guia",
    "linguagens",
    "rust"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação Rust — Guia Completo?",
    "Quais as boas praticas de rust?"
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
  "dono": "stack-rust",
  "prioridade": 2
}
---

# Documentação Rust — Guia Completo

> **Fonte:** [W3Schools Rust](https://www.w3schools.com/rust/index.php) · [The Rust Book](https://doc.rust-lang.org/book/)
> **Versão:** Rust 1.75+
> **Atualizado:** 2026-02-14

---

## Sumário

1. [Fundamentos](#fundamentos)
2. [Ownership e Borrowing](#ownership-e-borrowing)
3. [Tipos de Dados](#tipos-de-dados)
4. [Controle de Fluxo](#controle-de-fluxo)
5. [Structs e Enums](#structs-e-enums)
6. [Traits e Generics](#traits-e-generics)
7. [Tratamento de Erros](#tratamento-de-erros)
8. [Coleções](#coleções)
9. [Closures e Iterators](#closures-e-iterators)
10. [Concorrência](#concorrência)

---

## Fundamentos

```rust
fn main() {
    println!("Hello, World!");
}
```

### Compilar e executar

```bash
# Com rustc
rustc main.rs && ./main

# Com Cargo (recomendado)
cargo new meu_projeto
cargo build
cargo run
cargo test
```

### Variáveis

```rust
// Imutável por padrão
let x = 5;
// x = 6;  // ERRO!

// Mutável
let mut y = 10;
y = 20;  // OK

// Constante (deve ter tipo explícito)
const MAX_POINTS: u32 = 100_000;

// Shadowing (mesmo nome, novo binding)
let x = 5;
let x = x + 1;     // x = 6
let x = "texto";   // Agora é &str
```

---

## Ownership e Borrowing

> O conceito mais importante de Rust. Garante segurança de memória sem garbage collector.

### Regras

1. Cada valor tem exatamente **um owner**
2. Quando o owner sai de escopo, o valor é **dropped** (liberado)
3. Pode haver **uma referência mutável** OU **múltiplas referências imutáveis**, nunca ambas

```rust
// Move (transferência de ownership)
let s1 = String::from("hello");
let s2 = s1;        // s1 foi MOVIDO para s2
// println!("{}", s1); // ERRO: s1 não é mais válido

// Clone (cópia explícita)
let s3 = s2.clone();

// Referência imutável (borrowing)
fn tamanho(s: &String) -> usize {
    s.len()
}
let s = String::from("hello");
let len = tamanho(&s);  // s continua válido

// Referência mutável
fn adicionar(s: &mut String) {
    s.push_str(", world!");
}
let mut s = String::from("hello");
adicionar(&mut s);

// Lifetime
fn maior<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

---

## Tipos de Dados

| Tipo | Exemplos |
|---|---|
| `i8`, `i16`, `i32`, `i64`, `i128` | Inteiros com sinal |
| `u8`, `u16`, `u32`, `u64`, `u128` | Inteiros sem sinal |
| `isize`, `usize` | Tamanho do ponteiro |
| `f32`, `f64` | Ponto flutuante |
| `bool` | `true`, `false` |
| `char` | `'A'`, `'😀'` (4 bytes, Unicode) |
| `&str` | String slice (referência) |
| `String` | String heap (owned) |
| `(i32, f64)` | Tupla |
| `[i32; 5]` | Array fixo |

### Strings

```rust
// &str (string slice — referência, stack)
let s1: &str = "hello";

// String (heap, mutável, owned)
let mut s2 = String::from("hello");
s2.push_str(" world");
s2.push('!');

// Conversões
let s3: String = s1.to_string();
let s4: &str = &s2;

// Formatação
let msg = format!("{} tem {} anos", "Ana", 25);
```

---

## Controle de Fluxo

```rust
// if-else (é uma expressão!)
let status = if idade >= 18 { "adulto" } else { "menor" };

// match (switch turbinado)
let nota = 8;
let conceito = match nota {
    9..=10 => "A",
    7..=8 => "B",
    5..=6 => "C",
    _ => "D",
};

// if let (destructuring)
let valor: Option<i32> = Some(42);
if let Some(v) = valor {
    println!("Valor: {}", v);
}

// loop (infinito)
let mut count = 0;
let result = loop {
    count += 1;
    if count == 10 { break count * 2; }
};

// while
while count > 0 { count -= 1; }

// for
for i in 0..10 { }               // 0 a 9
for i in 0..=10 { }              // 0 a 10
for item in lista.iter() { }
for (i, item) in lista.iter().enumerate() { }
```

---

## Structs e Enums

```rust
// Struct
#[derive(Debug, Clone)]
struct Pessoa {
    nome: String,
    idade: u32,
}

impl Pessoa {
    // Construtor (convenção)
    fn new(nome: &str, idade: u32) -> Self {
        Pessoa {
            nome: nome.to_string(),
            idade,
        }
    }

    // Método (&self)
    fn apresentar(&self) -> String {
        format!("{} tem {} anos", self.nome, self.idade)
    }

    // Método mutável (&mut self)
    fn aniversario(&mut self) {
        self.idade += 1;
    }
}

// Enum (com dados associados!)
enum Forma {
    Circulo(f64),                         // Raio
    Retangulo { largura: f64, altura: f64 },
    Triangulo(f64, f64, f64),             // Lados
}

impl Forma {
    fn area(&self) -> f64 {
        match self {
            Forma::Circulo(r) => std::f64::consts::PI * r * r,
            Forma::Retangulo { largura, altura } => largura * altura,
            Forma::Triangulo(a, b, c) => {
                let s = (a + b + c) / 2.0;
                (s * (s - a) * (s - b) * (s - c)).sqrt()
            }
        }
    }
}

// Option e Result (enums fundamentais)
let encontrado: Option<i32> = Some(42);
let nada: Option<i32> = None;

let ok: Result<i32, String> = Ok(42);
let erro: Result<i32, String> = Err("falhou".to_string());
```

---

## Traits e Generics

```rust
// Trait (equivalente a interface)
trait Resumo {
    fn resumir(&self) -> String;
    fn preview(&self) -> String {  // Default
        format!("{}...", &self.resumir()[..50])
    }
}

impl Resumo for Pessoa {
    fn resumir(&self) -> String {
        format!("{}, {} anos", self.nome, self.idade)
    }
}

// Generic
fn maior<T: PartialOrd>(a: T, b: T) -> T {
    if a > b { a } else { b }
}

// Trait bounds (where clause)
fn processar<T>(item: &T) -> String
where
    T: Resumo + std::fmt::Debug,
{
    format!("{:?}: {}", item, item.resumir())
}

// impl Trait (retorno)
fn criar_resumivel() -> impl Resumo {
    Pessoa::new("Ana", 25)
}

// Derive macros comuns
#[derive(Debug, Clone, PartialEq, Eq, Hash, Default)]
struct Config { /* ... */ }
```

---

## Tratamento de Erros

```rust
use std::fs;
use std::io;

// Result<T, E>
fn ler_arquivo(path: &str) -> Result<String, io::Error> {
    fs::read_to_string(path)
}

// ? operator (propaga erro)
fn processar(path: &str) -> Result<usize, io::Error> {
    let conteudo = fs::read_to_string(path)?;
    Ok(conteudo.lines().count())
}

// unwrap (pânico se Err — só para protótipos!)
let conteudo = fs::read_to_string("dados.txt").unwrap();

// expect (pânico com mensagem)
let conteudo = fs::read_to_string("dados.txt")
    .expect("Não foi possível ler o arquivo");

// unwrap_or, unwrap_or_else
let valor = resultado.unwrap_or(0);
let valor = resultado.unwrap_or_else(|_| calcular_padrao());

// Erro customizado (com thiserror crate)
// #[derive(Debug, thiserror::Error)]
// enum AppError {
//     #[error("IO error: {0}")]
//     Io(#[from] std::io::Error),
//     #[error("Parse error: {msg}")]
//     Parse { msg: String },
// }
```

---

## Coleções

```rust
// Vec<T> (vetor dinâmico)
let mut v = vec![1, 2, 3];
v.push(4);
v.pop();
v.len();
v.contains(&2);
v[0]; // Pânico se fora do range
v.get(0); // Option<&i32>

// HashMap
use std::collections::HashMap;
let mut map = HashMap::new();
map.insert("Ana", 25);
map.entry("Bruno").or_insert(30);
if let Some(idade) = map.get("Ana") {
    println!("Idade: {}", idade);
}

// HashSet
use std::collections::HashSet;
let mut set: HashSet<i32> = HashSet::from([1, 2, 3]);
set.insert(4);
set.contains(&2);

// VecDeque, BTreeMap, BTreeSet, LinkedList
```

---

## Closures e Iterators

```rust
// Closures
let soma = |a: i32, b: i32| a + b;
let mut count = 0;
let incrementar = || { count += 1; count };

// Iterators
let nums = vec![1, 2, 3, 4, 5];

let resultado: Vec<i32> = nums.iter()
    .filter(|&&n| n > 2)
    .map(|&n| n * 2)
    .collect();
// [6, 8, 10]

// Métodos de iterador
nums.iter().sum::<i32>();
nums.iter().any(|&n| n > 3);
nums.iter().all(|&n| n > 0);
nums.iter().find(|&&n| n == 3);
nums.iter().enumerate();
nums.iter().zip(outro.iter());
nums.iter().flat_map(|x| vec![x, &(x * 10)]);
nums.chunks(2);
```

---

## Concorrência

```rust
use std::thread;
use std::sync::{Arc, Mutex};

// Threads
let handle = thread::spawn(|| {
    println!("Thread executando");
    42
});
let resultado = handle.join().unwrap();

// Dados compartilhados (Arc + Mutex)
let contador = Arc::new(Mutex::new(0));
let mut handles = vec![];

for _ in 0..10 {
    let c = Arc::clone(&contador);
    handles.push(thread::spawn(move || {
        let mut num = c.lock().unwrap();
        *num += 1;
    }));
}
for h in handles { h.join().unwrap(); }
println!("Total: {}", *contador.lock().unwrap());

// Channels (message passing)
use std::sync::mpsc;
let (tx, rx) = mpsc::channel();
thread::spawn(move || { tx.send("mensagem").unwrap(); });
let msg = rx.recv().unwrap();

// async/await (com tokio)
// #[tokio::main]
// async fn main() {
//     let result = fetch_data().await;
// }
```

---

*Fonte: [W3Schools Rust](https://www.w3schools.com/rust/) · [The Rust Book](https://doc.rust-lang.org/book/)*
