---json
{
  "id": "documentacao_go",
  "title": "Documentação Go (Golang) — Guia Completo",
  "categoria": "03-linguagens",
  "subcategoria": "go",
  "resumo": "**Fonte:** [W3Schools Go](https://www.w3schools.com/go/index.php) · [Go Docs](https://go.dev/doc/) **Versão:** Go 1.22+",
  "gatilhos": [
    "completo",
    "documentacao",
    "golang",
    "guia",
    "linguagens"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação Go (Golang) — Guia Completo?",
    "Quais as boas praticas de go?"
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
  "dono": "stack-go",
  "prioridade": 2
}
---

# Documentação Go (Golang) — Guia Completo

> **Fonte:** [W3Schools Go](https://www.w3schools.com/go/index.php) · [Go Docs](https://go.dev/doc/)
> **Versão:** Go 1.22+
> **Atualizado:** 2026-02-14

---

## Sumário

1. [Fundamentos](#fundamentos)
2. [Tipos de Dados](#tipos-de-dados)
3. [Controle de Fluxo](#controle-de-fluxo)
4. [Funções](#funções)
5. [Structs e Interfaces](#structs-e-interfaces)
6. [Slices e Maps](#slices-e-maps)
7. [Concorrência (Goroutines e Channels)](#concorrência)
8. [Tratamento de Erros](#tratamento-de-erros)
9. [Pacotes e Módulos](#pacotes-e-módulos)

---

## Fundamentos

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

```bash
go run main.go
go build -o app main.go
go mod init meu-projeto
go get github.com/pacote/lib
go test ./...
```

### Variáveis

```go
// Declaração explícita
var nome string = "Maria"
var idade int = 30

// Inferência
var ativo = true

// Short declaration (dentro de funções)
salario := 4500.50

// Constantes
const PI = 3.14159
const (
    StatusAtivo   = "ativo"
    StatusInativo = "inativo"
)

// iota (auto-increment)
type Cor int
const (
    Vermelho Cor = iota  // 0
    Verde                // 1
    Azul                 // 2
)

// Zero values: int=0, string="", bool=false, pointer=nil
```

---

## Tipos de Dados

| Tipo | Tamanho |
|---|---|
| `int8/16/32/64` | 1/2/4/8 bytes |
| `uint8/16/32/64` | Sem sinal |
| `int`, `uint` | Dependente de plataforma |
| `float32`, `float64` | Ponto flutuante |
| `complex64`, `complex128` | Complexo |
| `bool` | true/false |
| `string` | UTF-8 |
| `byte` | Alias para uint8 |
| `rune` | Alias para int32 (Unicode) |

### Strings

```go
s := "Hello World"
len(s)                           // Bytes (not runes)
strings.ToUpper(s)
strings.ToLower(s)
strings.Contains(s, "World")
strings.HasPrefix(s, "Hello")
strings.Split(s, " ")
strings.Join([]string{"a", "b"}, ", ")
strings.TrimSpace("  hello  ")
strings.Replace(s, "World", "Go", 1)
fmt.Sprintf("Nome: %s, Idade: %d", nome, idade)

// Strings builder (eficiente)
var b strings.Builder
b.WriteString("Hello")
b.WriteString(" World")
resultado := b.String()
```

---

## Controle de Fluxo

```go
// if (sem parênteses; com init statement)
if idade := calcularIdade(); idade >= 18 {
    fmt.Println("Adulto")
} else {
    fmt.Println("Menor")
}

// switch (sem break necessário)
switch dia {
case "segunda", "terça": fmt.Println("Início")
case "sexta": fmt.Println("Sextou!")
default: fmt.Println("Meio da semana")
}

// Type switch
switch v := valor.(type) {
case int: fmt.Printf("Int: %d\n", v)
case string: fmt.Printf("String: %s\n", v)
default: fmt.Println("Outro tipo")
}

// for (o único loop em Go)
for i := 0; i < 10; i++ { }
for i < 100 { i++ }                   // while
for { break }                          // loop infinito
for i, v := range slice { }           // range
for k, v := range mapa { }
for _, c := range "texto" { }         // Runes
```

---

## Funções

```go
// Múltiplos retornos
func dividir(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("divisão por zero")
    }
    return a / b, nil
}
resultado, err := dividir(10, 3)

// Named return values
func rect(l, a float64) (area, perimetro float64) {
    area = l * a
    perimetro = 2 * (l + a)
    return // naked return
}

// Variadic
func soma(nums ...int) int {
    total := 0
    for _, n := range nums {
        total += n
    }
    return total
}
soma(1, 2, 3, 4, 5)

// First-class functions
func aplicar(nums []int, fn func(int) int) []int {
    result := make([]int, len(nums))
    for i, n := range nums {
        result[i] = fn(n)
    }
    return result
}
dobros := aplicar([]int{1, 2, 3}, func(n int) int { return n * 2 })

// Defer (executa ao sair da função — LIFO)
func processarArquivo(path string) error {
    f, err := os.Open(path)
    if err != nil { return err }
    defer f.Close()  // Garante fechamento
    // ... processar ...
    return nil
}
```

---

## Structs e Interfaces

```go
// Struct
type Pessoa struct {
    Nome  string
    Idade int
    Email string
}

// Métodos (receiver)
func (p Pessoa) Apresentar() string {
    return fmt.Sprintf("%s, %d anos", p.Nome, p.Idade)
}

func (p *Pessoa) Aniversario() {
    p.Idade++  // Ponteiro para modificar
}

// Constructor (convenção)
func NovaPessoa(nome string, idade int) *Pessoa {
    return &Pessoa{Nome: nome, Idade: idade}
}

// Composição (em vez de herança)
type Funcionario struct {
    Pessoa     // Embedded struct
    Cargo  string
    Salario float64
}

f := Funcionario{
    Pessoa: Pessoa{Nome: "Ana", Idade: 30},
    Cargo:  "Dev",
}
fmt.Println(f.Nome)  // Acesso direto via embedding

// Interface (implícita — não precisa declarar!)
type Falante interface {
    Falar() string
}

// Qualquer tipo com método Falar() implementa Falante
type Cachorro struct{ Nome string }
func (c Cachorro) Falar() string { return c.Nome + ": Au au!" }

type Gato struct{ Nome string }
func (g Gato) Falar() string { return g.Nome + ": Miau!" }

func cumprimentar(f Falante) {
    fmt.Println(f.Falar())
}
cumprimentar(Cachorro{Nome: "Rex"})
cumprimentar(Gato{Nome: "Mimi"})

// interface{} / any (qualquer tipo)
func imprimir(v any) { fmt.Println(v) }
```

---

## Slices e Maps

### Slices

```go
// Slice (array dinâmico)
s := []int{1, 2, 3, 4, 5}
s = append(s, 6, 7)
len(s)  // Comprimento
cap(s)  // Capacidade

// make
s2 := make([]int, 5, 10)  // len=5, cap=10

// Slice de slice
sub := s[1:4]  // [2, 3, 4]

// Copiar
dst := make([]int, len(s))
copy(dst, s)

// Deletar elemento no índice i
s = append(s[:i], s[i+1:]...)
```

### Maps

```go
m := map[string]int{
    "Ana":   25,
    "Bruno": 30,
}
m["Carlos"] = 35
delete(m, "Bruno")

// Verificar existência
v, ok := m["Ana"]
if ok { fmt.Println(v) }

// Iterar
for k, v := range m {
    fmt.Printf("%s: %d\n", k, v)
}
```

---

## Concorrência

```go
// Goroutine
go func() {
    fmt.Println("Executando em paralelo")
}()

// Channel (comunicação entre goroutines)
ch := make(chan string)
go func() { ch <- "mensagem" }()
msg := <-ch

// Buffered channel
ch := make(chan int, 10)

// Select (multiplexar channels)
select {
case msg := <-ch1:
    fmt.Println("ch1:", msg)
case msg := <-ch2:
    fmt.Println("ch2:", msg)
case <-time.After(5 * time.Second):
    fmt.Println("Timeout!")
}

// WaitGroup
var wg sync.WaitGroup
for i := 0; i < 5; i++ {
    wg.Add(1)
    go func(id int) {
        defer wg.Done()
        fmt.Printf("Worker %d\n", id)
    }(i)
}
wg.Wait()

// Mutex
var mu sync.Mutex
var contador int
mu.Lock()
contador++
mu.Unlock()

// Context (cancelamento e timeout)
ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
defer cancel()
```

---

## Tratamento de Erros

```go
// Padrão Go: retornar error
func lerArquivo(path string) ([]byte, error) {
    data, err := os.ReadFile(path)
    if err != nil {
        return nil, fmt.Errorf("leitura falhou: %w", err)  // Wrap error
    }
    return data, nil
}

// Uso
data, err := lerArquivo("config.json")
if err != nil {
    log.Fatal(err)
}

// Erro customizado
type AppError struct {
    Code    int
    Message string
}
func (e *AppError) Error() string {
    return fmt.Sprintf("[%d] %s", e.Code, e.Message)
}

// errors.Is / errors.As
if errors.Is(err, os.ErrNotExist) { }
var appErr *AppError
if errors.As(err, &appErr) { fmt.Println(appErr.Code) }

// Panic/Recover (exceções — use com moderação)
func seguro() {
    defer func() {
        if r := recover(); r != nil {
            fmt.Println("Recuperado:", r)
        }
    }()
    panic("algo deu errado")
}
```

---

## Pacotes e Módulos

```bash
# Iniciar módulo
go mod init github.com/usuario/projeto

# Adicionar dependência
go get github.com/gin-gonic/gin

# Atualizar dependências
go mod tidy
```

```go
// Pacotes úteis da stdlib
import (
    "encoding/json"      // JSON
    "net/http"           // HTTP server/client
    "os"                 // Sistema operacional
    "io"                 // I/O
    "bufio"              // Buffered I/O
    "path/filepath"      // Caminhos de arquivo
    "strconv"            // Conversão string↔números
    "sort"               // Ordenação
    "sync"               // Concorrência
    "context"            // Contexto
    "testing"            // Testes
    "log"                // Logging
    "time"               // Tempo
)

// HTTP Server simples
http.HandleFunc("/api/hello", func(w http.ResponseWriter, r *http.Request) {
    json.NewEncoder(w).Encode(map[string]string{"msg": "Hello!"})
})
http.ListenAndServe(":8080", nil)

// JSON
type User struct {
    Nome  string `json:"nome"`
    Idade int    `json:"idade"`
}
data, _ := json.Marshal(User{Nome: "Ana", Idade: 25})
var u User
json.Unmarshal(data, &u)
```

---

*Fonte: [W3Schools Go](https://www.w3schools.com/go/) · [Go Docs](https://go.dev/doc/)*
