---json
{
  "id": "documentacao_swift",
  "title": "Documentação Swift — Guia Completo",
  "categoria": "04-frameworks",
  "subcategoria": "mobile",
  "resumo": "**Fonte:** [W3Schools Swift](https://www.w3schools.com/swift/default.asp) · [Swift Docs](https://docs.swift.org/swift-book/) **Versão:** Swift 5.9+",
  "gatilhos": [
    "completo",
    "documentacao",
    "frameworks",
    "guia",
    "mobile",
    "swift"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação Swift — Guia Completo?",
    "Quais as boas praticas de mobile?"
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
  "dono": "stack-mobile",
  "prioridade": 2
}
---

# Documentação Swift — Guia Completo

> **Fonte:** [W3Schools Swift](https://www.w3schools.com/swift/default.asp) · [Swift Docs](https://docs.swift.org/swift-book/)
> **Versão:** Swift 5.9+
> **Atualizado:** 2026-02-14

---

## Sumário

1. [Fundamentos](#fundamentos)
2. [Tipos e Optionals](#tipos-e-optionals)
3. [Controle de Fluxo](#controle-de-fluxo)
4. [Funções e Closures](#funções-e-closures)
5. [OOP — Classes e Structs](#oop--classes-e-structs)
6. [Protocolos e Extensions](#protocolos-e-extensions)
7. [Enums e Pattern Matching](#enums-e-pattern-matching)
8. [Coleções](#coleções)
9. [Tratamento de Erros](#tratamento-de-erros)
10. [Concurrency (async/await)](#concurrency)
11. [SwiftUI Básico](#swiftui-básico)

---

## Fundamentos

```swift
import Foundation

print("Hello, World!")

// Variáveis e constantes
let nome = "Maria"       // Constante (let) — preferir
var idade = 30           // Variável (var)
let pi: Double = 3.14159 // Tipo explícito

// String interpolation
print("Nome: \(nome), Idade: \(idade)")
print("PI: \(String(format: "%.2f", pi))")

// Multiline
let texto = """
    Primeira linha
    Segunda linha
    """
```

---

## Tipos e Optionals

| Tipo | Exemplo |
|---|---|
| `Int`, `Int8/16/32/64` | Inteiro |
| `UInt` | Sem sinal |
| `Double`, `Float` | Ponto flutuante |
| `Bool` | `true`, `false` |
| `String` | `"hello"` |
| `Character` | `"A"` |
| `[Int]` | Array |
| `[String: Int]` | Dictionary |
| `(Int, String)` | Tuple |

### Optionals (null safety)

```swift
var email: String? = nil  // Pode ser nil

// Optional binding (if let)
if let e = email {
    print("Email: \(e)")
}

// Guard let (early return)
func processar(email: String?) {
    guard let e = email else {
        print("Email ausente")
        return
    }
    print("Processando: \(e)")
}

// Nil coalescing
let valor = email ?? "sem@email.com"

// Optional chaining
let tamanho = email?.count

// Force unwrap (cuidado!)
let forçado = email!  // Crash se nil

// Implicit unwrap
var config: String! = "valor"
```

---

## Controle de Fluxo

```swift
// if-else
if idade >= 18 {
    print("Adulto")
} else if idade >= 12 {
    print("Adolescente")
} else {
    print("Criança")
}

// Ternário
let status = idade >= 18 ? "adulto" : "menor"

// switch (exaustivo, sem fallthrough implícito)
switch nota {
case 9...10: print("A")
case 7..<9: print("B")
case 5..<7: print("C")
case let n where n < 0: print("Inválido: \(n)")
default: print("D")
}

// for-in
for i in 1...10 { }
for i in stride(from: 0, to: 20, by: 2) { }  // 0, 2, 4, ..., 18
for (index, valor) in lista.enumerated() { }
for _ in 0..<5 { }  // Sem variável

// while
while condicao { }
repeat { } while condicao  // do-while
```

---

## Funções e Closures

```swift
// Função básica
func somar(_ a: Int, _ b: Int) -> Int {
    return a + b
}
somar(3, 4)

// Argument labels
func saudar(para nome: String, com saudacao: String = "Olá") -> String {
    return "\(saudacao), \(nome)!"
}
saudar(para: "Ana", com: "Oi")

// Retorno de tupla
func minMax(array: [Int]) -> (min: Int, max: Int)? {
    guard !array.isEmpty else { return nil }
    return (array.min()!, array.max()!)
}
if let resultado = minMax(array: [3, 1, 4, 1, 5]) {
    print("Min: \(resultado.min), Max: \(resultado.max)")
}

// Variadic
func media(_ nums: Double...) -> Double {
    nums.reduce(0, +) / Double(nums.count)
}

// inout (passagem por referência)
func trocar(_ a: inout Int, _ b: inout Int) {
    (a, b) = (b, a)
}

// Closures
let quadrado = { (n: Int) -> Int in n * n }
let dobro: (Int) -> Int = { $0 * 2 }

// Trailing closure
let filtrados = nums.filter { $0 > 5 }
let mapeados = nums.map { "\($0)" }
let soma = nums.reduce(0) { $0 + $1 }

// @escaping closure
func executarDepois(delay: Double, acao: @escaping () -> Void) {
    DispatchQueue.main.asyncAfter(deadline: .now() + delay, execute: acao)
}
```

---

## OOP — Classes e Structs

```swift
// Struct (value type — preferir)
struct Ponto {
    var x: Double
    var y: Double

    func distancia(para outro: Ponto) -> Double {
        sqrt(pow(x - outro.x, 2) + pow(y - outro.y, 2))
    }

    mutating func mover(dx: Double, dy: Double) {
        x += dx
        y += dy
    }
}

// Class (reference type — herança, identidade)
class Pessoa {
    let nome: String
    var idade: Int

    init(nome: String, idade: Int) {
        self.nome = nome
        self.idade = idade
    }

    deinit { print("\(nome) destruído") }

    func apresentar() -> String {
        "\(nome), \(idade) anos"
    }
}

// Herança
class Funcionario: Pessoa {
    var cargo: String

    init(nome: String, idade: Int, cargo: String) {
        self.cargo = cargo
        super.init(nome: nome, idade: idade)
    }

    override func apresentar() -> String {
        "\(super.apresentar()) - \(cargo)"
    }
}

// Properties
class Circulo {
    var raio: Double

    // Computed property
    var area: Double {
        get { Double.pi * raio * raio }
    }

    var diametro: Double {
        get { raio * 2 }
        set { raio = newValue / 2 }
    }

    // Property observer
    var cor: String = "azul" {
        willSet { print("Mudando de \(cor) para \(newValue)") }
        didSet { print("Mudou de \(oldValue) para \(cor)") }
    }

    init(raio: Double) { self.raio = raio }
}
```

---

## Protocolos e Extensions

```swift
// Protocolo (equivalente a interface)
protocol Descritivel {
    var descricao: String { get }
    func resumir() -> String
}

// Default implementation
extension Descritivel {
    func resumir() -> String { descricao }
}

// Extension (adicionar funcionalidade a tipos existentes)
extension Int {
    var quadrado: Int { self * self }
    func repetir(acao: () -> Void) {
        for _ in 0..<self { acao() }
    }
}
print(5.quadrado)  // 25
3.repetir { print("Olá!") }

// Protocol-oriented programming
protocol Renderizavel {
    func render() -> String
}

struct HTML: Renderizavel {
    let tag: String
    let conteudo: String
    func render() -> String { "<\(tag)>\(conteudo)</\(tag)>" }
}
```

---

## Enums e Pattern Matching

```swift
// Enum com associated values
enum Resultado {
    case sucesso(dados: String)
    case erro(codigo: Int, mensagem: String)
    case carregando(progresso: Double)
}

let r: Resultado = .sucesso(dados: "OK")

switch r {
case .sucesso(let dados):
    print("Dados: \(dados)")
case .erro(let codigo, let msg) where codigo >= 500:
    print("Erro servidor: \(msg)")
case .erro(_, let msg):
    print("Erro: \(msg)")
case .carregando(let p) where p >= 1.0:
    print("Completo!")
case .carregando(let p):
    print("Carregando: \(Int(p * 100))%")
}

// Enum com raw values
enum Planeta: Int {
    case mercurio = 1, venus, terra, marte
}

enum Moeda: String {
    case real = "BRL"
    case dolar = "USD"
    case euro = "EUR"
}

// Enum com métodos
enum Direcao {
    case norte, sul, leste, oeste

    var oposta: Direcao {
        switch self {
        case .norte: return .sul
        case .sul: return .norte
        case .leste: return .oeste
        case .oeste: return .leste
        }
    }
}
```

---

## Coleções

```swift
// Array
var nums = [1, 2, 3, 4, 5]
nums.append(6)
nums.insert(0, at: 0)
nums.remove(at: 0)
nums.contains(3)
nums.filter { $0 > 3 }
nums.map { $0 * 2 }
nums.compactMap { Int($0) }  // Remove nils
nums.flatMap { [$0, $0 * 10] }
nums.reduce(0, +)
nums.sorted()
nums.first(where: { $0 > 3 })

// Dictionary
var capitais: [String: String] = [
    "Brasil": "Brasília",
    "Portugal": "Lisboa"
]
capitais["EUA"] = "Washington"
capitais.removeValue(forKey: "Portugal")
for (pais, capital) in capitais { }

// Set
var tags: Set<String> = ["swift", "ios", "xcode"]
tags.insert("apple")
tags.contains("swift")
let uniao = tags.union(outraSet)
let inter = tags.intersection(outraSet)
```

---

## Tratamento de Erros

```swift
// Definir erros
enum AppError: Error {
    case redeIndisponivel
    case dadosInvalidos(String)
    case naoEncontrado
}

// Função que lança
func buscar(id: Int) throws -> String {
    guard id > 0 else { throw AppError.dadosInvalidos("ID inválido") }
    guard id < 1000 else { throw AppError.naoEncontrado }
    return "Resultado \(id)"
}

// do-try-catch
do {
    let resultado = try buscar(id: 5)
    print(resultado)
} catch AppError.naoEncontrado {
    print("Não encontrado")
} catch AppError.dadosInvalidos(let msg) {
    print("Inválido: \(msg)")
} catch {
    print("Erro: \(error)")
}

// try? (retorna optional)
let resultado = try? buscar(id: 5)  // String?

// try! (crash se erro)
let resultado = try! buscar(id: 5)  // Não recomendado
```

---

## Concurrency

```swift
// async/await (Swift 5.5+)
func fetchDados(url: String) async throws -> Data {
    let (data, _) = try await URLSession.shared.data(from: URL(string: url)!)
    return data
}

// Chamada
Task {
    do {
        let dados = try await fetchDados(url: "https://api.example.com")
        print("Recebidos: \(dados.count) bytes")
    } catch {
        print("Erro: \(error)")
    }
}

// Paralelo
async let d1 = fetchDados(url: "url1")
async let d2 = fetchDados(url: "url2")
let (r1, r2) = try await (d1, d2)

// Actor (thread-safe)
actor Contador {
    private var valor = 0
    func incrementar() { valor += 1 }
    func atual() -> Int { valor }
}

let c = Contador()
await c.incrementar()
print(await c.atual())
```

---

## SwiftUI Básico

```swift
import SwiftUI

struct ContentView: View {
    @State private var contador = 0

    var body: some View {
        VStack(spacing: 20) {
            Text("Contador: \(contador)")
                .font(.largeTitle)
                .foregroundColor(.blue)

            HStack {
                Button("- 1") { contador -= 1 }
                    .buttonStyle(.bordered)

                Button("+ 1") { contador += 1 }
                    .buttonStyle(.borderedProminent)
            }
        }
        .padding()
    }
}

// MVVM com ObservableObject
@Observable
class ViewModel {
    var items: [String] = []
    var isLoading = false

    func carregar() async {
        isLoading = true
        // await fetch...
        isLoading = false
    }
}
```

---

*Fonte: [W3Schools Swift](https://www.w3schools.com/swift/) · [Swift Docs](https://docs.swift.org/swift-book/)*
