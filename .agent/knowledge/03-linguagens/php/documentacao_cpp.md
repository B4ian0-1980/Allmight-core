---json
{
  "id": "documentacao_cpp",
  "title": "Documentação C++ — Guia Completo",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Fonte:** [W3Schools C++](https://www.w3schools.com/cpp/default.asp) · [cppreference.com](https://en.cppreference.com/w/cpp) **Versão:** C++17/C++20/C++23",
  "gatilhos": [
    "completo",
    "cpp",
    "documentacao",
    "guia",
    "linguagens",
    "php"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação C++ — Guia Completo?",
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

# Documentação C++ — Guia Completo

> **Fonte:** [W3Schools C++](https://www.w3schools.com/cpp/default.asp) · [cppreference.com](https://en.cppreference.com/w/cpp)
> **Versão:** C++17/C++20/C++23
> **Atualizado:** 2026-02-14

---

## Sumário

1. [Fundamentos](#fundamentos)
2. [Tipos e Variáveis](#tipos-e-variáveis)
3. [Controle de Fluxo](#controle-de-fluxo)
4. [Arrays, Strings e Vectors](#arrays-strings-e-vectors)
5. [Ponteiros e Referências](#ponteiros-e-referências)
6. [Funções](#funções)
7. [OOP — Classes](#oop--classes)
8. [Herança e Polimorfismo](#herança-e-polimorfismo)
9. [Templates](#templates)
10. [STL — Containers e Algoritmos](#stl--containers-e-algoritmos)
11. [Smart Pointers e RAII](#smart-pointers-e-raii)
12. [Recursos Modernos (C++17/20/23)](#recursos-modernos-c1720)

---

## Fundamentos

```cpp
#include <iostream>
#include <string>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

### Compilar

```bash
g++ -std=c++20 -Wall -Wextra -o programa main.cpp
./programa
```

### I/O

```cpp
#include <iostream>
using namespace std;

int idade;
string nome;
cout << "Nome: ";
getline(cin, nome);
cout << "Idade: ";
cin >> idade;
cout << nome << " tem " << idade << " anos" << endl;
```

---

## Tipos e Variáveis

```cpp
// Tipos primitivos (mesmos do C + extras)
int x = 42;
double pi = 3.14159;
bool ativo = true;
char c = 'A';
auto valor = 42;        // Inferência de tipo
const int MAX = 100;
constexpr int N = 10;   // Compilação

// Inicialização uniforme (C++11)
int a{42};
std::string s{"hello"};
std::vector<int> v{1, 2, 3};

// nullptr (em vez de NULL)
int* ptr = nullptr;
```

---

## Controle de Fluxo

```cpp
// if com inicializador (C++17)
if (auto it = mapa.find("chave"); it != mapa.end()) {
    std::cout << it->second << std::endl;
}

// switch
switch (opcao) {
    case 1: cout << "Um"; break;
    case 2: cout << "Dois"; break;
    default: cout << "Outro";
}

// Range-based for (C++11)
std::vector<int> nums = {1, 2, 3, 4, 5};
for (const auto& n : nums) {
    std::cout << n << " ";
}

// Structured bindings (C++17)
std::map<string, int> m = {{"a", 1}, {"b", 2}};
for (const auto& [chave, valor] : m) {
    cout << chave << ": " << valor << endl;
}
```

---

## Arrays, Strings e Vectors

```cpp
#include <string>
#include <vector>
#include <array>

// std::array (tamanho fixo, C++11)
std::array<int, 5> arr = {1, 2, 3, 4, 5};
arr.size();  // 5
arr.at(0);   // Acesso seguro (bounds check)

// std::vector (tamanho dinâmico)
std::vector<int> v = {10, 20, 30};
v.push_back(40);
v.emplace_back(50);   // Mais eficiente
v.pop_back();
v.size();
v.empty();
v.clear();
v.insert(v.begin() + 1, 15);
v.erase(v.begin());

// std::string
std::string s = "Hello";
s += " World";          // Concatenar
s.length();             // 11
s.substr(0, 5);         // "Hello"
s.find("World");        // 6
s.replace(6, 5, "C++"); // "Hello C++"
s.empty();
s.starts_with("He");    // C++20
s.ends_with("++");      // C++20
s.contains("lo");       // C++23

// String views (C++17, sem cópia)
std::string_view sv = "Hello World";
```

---

## Ponteiros e Referências

```cpp
// Referências (alias — mais seguras que ponteiros)
int x = 42;
int& ref = x;          // ref é alias de x
ref = 100;             // x agora é 100

// const reference (parâmetros eficientes)
void processar(const std::string& texto) { /* ... */ }

// Ponteiros
int* ptr = &x;
*ptr = 200;

// Diferenças chave:
// - Referência DEVE ser inicializada, não pode ser null
// - Ponteiro pode ser null e reatribuído
// - Use referência por padrão, ponteiro quando precisa de null/reatribuição
```

---

## Funções

```cpp
// Básica
int somar(int a, int b) { return a + b; }

// Parâmetros default
void log(const string& msg, int nivel = 1) { /* ... */ }

// Overloading
double area(double r)           { return 3.14159 * r * r; }
double area(double l, double a) { return l * a; }

// Passagem por referência
void swap(int& a, int& b) { int t = a; a = b; b = t; }

// Auto return type (C++14)
auto multiplicar(int a, int b) { return a * b; }

// constexpr (avaliação em tempo de compilação)
constexpr int fatorial(int n) {
    return (n <= 1) ? 1 : n * fatorial(n - 1);
}
static_assert(fatorial(5) == 120);

// Lambda (C++11)
auto soma = [](int a, int b) { return a + b; };
auto captura = [&x, y](int z) { return x + y + z; };
auto generico = [](auto a, auto b) { return a + b; }; // C++14

// Lambda com template (C++20)
auto add = []<typename T>(T a, T b) { return a + b; };
```

---

## OOP — Classes

```cpp
class Conta {
private:
    std::string titular;
    double saldo;
    static int total_contas;

public:
    // Construtor
    Conta(const std::string& titular, double saldo = 0.0)
        : titular(titular), saldo(saldo) { total_contas++; }

    // Construtor de cópia
    Conta(const Conta& outra) = default;

    // Move constructor (C++11)
    Conta(Conta&& outra) noexcept = default;

    // Destrutor
    ~Conta() { total_contas--; }

    // Getters
    const std::string& getTitular() const { return titular; }
    double getSaldo() const { return saldo; }

    // Métodos
    void depositar(double valor) {
        if (valor > 0) saldo += valor;
    }

    bool sacar(double valor) {
        if (valor > 0 && valor <= saldo) {
            saldo -= valor;
            return true;
        }
        return false;
    }

    // Operador overload
    Conta operator+(const Conta& outra) const {
        return Conta(titular, saldo + outra.saldo);
    }

    bool operator==(const Conta& outra) const = default; // C++20

    // Friend
    friend std::ostream& operator<<(std::ostream& os, const Conta& c) {
        return os << c.titular << ": R$" << c.saldo;
    }

    // Static
    static int getTotalContas() { return total_contas; }
};

int Conta::total_contas = 0;
```

---

## Herança e Polimorfismo

```cpp
class Forma {
protected:
    std::string cor;
public:
    Forma(const std::string& cor) : cor(cor) {}
    virtual ~Forma() = default;              // Destrutor virtual!
    virtual double area() const = 0;          // Puro virtual (abstrato)
    virtual void desenhar() const {
        std::cout << "Forma " << cor << std::endl;
    }
};

class Circulo : public Forma {
    double raio;
public:
    Circulo(double r, const std::string& cor) : Forma(cor), raio(r) {}

    double area() const override { return 3.14159 * raio * raio; }
    void desenhar() const override {
        std::cout << "Circulo " << cor << " r=" << raio << std::endl;
    }
};

class Retangulo final : public Forma {  // final: não pode herdar
    double largura, altura;
public:
    Retangulo(double l, double a, const std::string& cor)
        : Forma(cor), largura(l), altura(a) {}
    double area() const override { return largura * altura; }
};

// Polimorfismo
std::vector<std::unique_ptr<Forma>> formas;
formas.push_back(std::make_unique<Circulo>(5, "azul"));
formas.push_back(std::make_unique<Retangulo>(3, 4, "vermelho"));

for (const auto& f : formas) {
    f->desenhar();
    std::cout << "Área: " << f->area() << std::endl;
}
```

---

## Templates

```cpp
// Template de função
template <typename T>
T maximo(T a, T b) { return (a > b) ? a : b; }

maximo(3, 7);       // int
maximo(3.14, 2.71); // double

// Template de classe
template <typename T, int N>
class FixedArray {
    T data[N];
public:
    T& operator[](int i) { return data[i]; }
    constexpr int size() const { return N; }
};

FixedArray<int, 10> arr;

// Concepts (C++20)
template <typename T>
concept Numerico = std::integral<T> || std::floating_point<T>;

template <Numerico T>
T somar(T a, T b) { return a + b; }

// Variadic templates
template <typename... Args>
void print(Args... args) {
    ((std::cout << args << " "), ...);  // Fold expression (C++17)
    std::cout << std::endl;
}
print(1, "hello", 3.14);
```

---

## STL — Containers e Algoritmos

```cpp
#include <algorithm>
#include <numeric>
#include <ranges>       // C++20

std::vector<int> v = {5, 2, 8, 1, 9, 3};

// Algoritmos
std::sort(v.begin(), v.end());
std::reverse(v.begin(), v.end());
auto it = std::find(v.begin(), v.end(), 8);
bool tem = std::binary_search(v.begin(), v.end(), 5);
int soma = std::accumulate(v.begin(), v.end(), 0);
std::for_each(v.begin(), v.end(), [](int n) { std::cout << n; });

// Ranges (C++20)
namespace rv = std::views;
auto resultado = v
    | rv::filter([](int n) { return n > 3; })
    | rv::transform([](int n) { return n * 2; });

// Containers
std::map<std::string, int> m = {{"a", 1}, {"b", 2}};
std::unordered_map<std::string, int> um;  // Hash map (mais rápido)
std::set<int> s = {3, 1, 4, 1, 5};       // {1, 3, 4, 5}
std::deque<int> dq;
std::stack<int> st;
std::queue<int> q;
std::priority_queue<int> pq;

// Inserção com try_emplace (C++17)
m.try_emplace("c", 3);
```

---

## Smart Pointers e RAII

```cpp
#include <memory>

// unique_ptr — posse exclusiva
auto p1 = std::make_unique<int>(42);
auto p2 = std::make_unique<Conta>("Ana", 1000);
p2->depositar(500);

// shared_ptr — posse compartilhada
auto s1 = std::make_shared<Conta>("Bruno", 2000);
auto s2 = s1;  // Referências: 2
std::cout << s1.use_count();  // 2

// weak_ptr — referência fraca (não impede destruição)
std::weak_ptr<Conta> w = s1;
if (auto locked = w.lock()) {
    // Objeto ainda existe
}

// REGRA: Nunca use new/delete manualmente
// Use make_unique/make_shared
```

---

## Recursos Modernos (C++17/20)

```cpp
// std::optional (C++17)
std::optional<int> buscar(int id) {
    if (id > 0) return 42;
    return std::nullopt;
}
auto r = buscar(1);
if (r.has_value()) std::cout << *r;
std::cout << r.value_or(-1);

// std::variant (C++17) — union segura
std::variant<int, double, std::string> v = "hello";
std::cout << std::get<std::string>(v);

// std::any (C++17)
std::any a = 42;
a = std::string("texto");
auto s = std::any_cast<std::string>(a);

// std::filesystem (C++17)
#include <filesystem>
namespace fs = std::filesystem;
for (auto& entry : fs::directory_iterator(".")) {
    std::cout << entry.path() << std::endl;
}
fs::exists("arquivo.txt");
fs::file_size("arquivo.txt");
fs::create_directories("a/b/c");

// std::format (C++20)
#include <format>
auto msg = std::format("Nome: {}, Idade: {}", "Ana", 25);

// Coroutines (C++20)
// Modules (C++20)
// std::expected (C++23)
```

---

*Fonte: [W3Schools C++](https://www.w3schools.com/cpp/) · [cppreference.com](https://en.cppreference.com/w/cpp)*
