---json
{
  "id": "documentacao-python",
  "title": "Documentação Python — Guia Completo",
  "categoria": "03-linguagens",
  "subcategoria": "python",
  "resumo": "**Fonte:** [W3Schools Python](https://www.w3schools.com/python/default.asp) · [Python Docs](https://docs.python.org/3/) **Versão:** Python 3.12+",
  "gatilhos": [
    "completo",
    "documentacao",
    "guia",
    "linguagens",
    "python"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação Python — Guia Completo?",
    "Quais as boas praticas de python?"
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
  "dono": "stack-python",
  "prioridade": 2
}
---

# Documentação Python — Guia Completo

> **Fonte:** [W3Schools Python](https://www.w3schools.com/python/default.asp) · [Python Docs](https://docs.python.org/3/)
> **Versão:** Python 3.12+
> **Atualizado:** 2026-02-14

---

## Sumário

1. [Fundamentos](#fundamentos)
2. [Tipos de Dados](#tipos-de-dados)
3. [Estruturas de Dados](#estruturas-de-dados)
4. [Controle de Fluxo](#controle-de-fluxo)
5. [Funções](#funções)
6. [OOP — Classes](#oop--classes)
7. [Módulos e Pacotes](#módulos-e-pacotes)
8. [Tratamento de Erros](#tratamento-de-erros)
9. [Arquivos e I/O](#arquivos-e-io)
10. [Comprehensions e Generators](#comprehensions-e-generators)
11. [Decorators e Context Managers](#decorators-e-context-managers)
12. [Type Hints e Async](#type-hints-e-async)

---

## Fundamentos

```python
# Variáveis (tipagem dinâmica)
nome = "Maria"
idade = 30
salario = 4500.50
ativo = True

# Múltipla atribuição
x, y, z = 1, 2, 3
a = b = c = 0

# Constantes (convenção)
PI = 3.14159
MAX_RETRY = 3

# f-strings (formatação)
print(f"Nome: {nome}, Idade: {idade}")
print(f"Salário: R${salario:,.2f}")
print(f"{'Centralizado':^30}")

# Input
nome = input("Digite seu nome: ")
idade = int(input("Idade: "))

# Tipo
type(nome)   # <class 'str'>
isinstance(nome, str)  # True
```

---

## Tipos de Dados

| Tipo | Exemplo | Mutável |
|---|---|---|
| `int` | `42`, `0xFF`, `0b1010` | ❌ |
| `float` | `3.14`, `1e-5` | ❌ |
| `complex` | `3+4j` | ❌ |
| `str` | `"hello"`, `'world'` | ❌ |
| `bool` | `True`, `False` | ❌ |
| `list` | `[1, 2, 3]` | ✅ |
| `tuple` | `(1, 2, 3)` | ❌ |
| `set` | `{1, 2, 3}` | ✅ |
| `frozenset` | `frozenset({1, 2})` | ❌ |
| `dict` | `{"a": 1}` | ✅ |
| `None` | `None` | ❌ |
| `bytes` | `b"hello"` | ❌ |

### Strings

```python
s = "Hello World"
s.upper()           # "HELLO WORLD"
s.lower()           # "hello world"
s.strip()           # Remove espaços
s.split(" ")        # ["Hello", "World"]
s.replace("World", "Python")
s.startswith("Hello")
s.find("World")     # 6 (-1 se não encontrar)
s[0:5]              # "Hello" (slice)
s[::-1]             # "dlroW olleH" (reverso)
"_".join(["a", "b", "c"])  # "a_b_c"
f"{42:08d}"         # "00000042"
```

---

## Estruturas de Dados

### List

```python
frutas = ["maçã", "banana", "laranja"]
frutas.append("uva")
frutas.insert(1, "manga")
frutas.remove("banana")
frutas.pop()        # Remove último
frutas.sort()
frutas.reverse()
len(frutas)
"maçã" in frutas    # True

# Slice
nums = [0, 1, 2, 3, 4, 5]
nums[1:4]    # [1, 2, 3]
nums[::2]    # [0, 2, 4]
nums[-3:]    # [3, 4, 5]

# Unpacking
primeiro, *resto, ultimo = [1, 2, 3, 4, 5]
# primeiro=1, resto=[2,3,4], ultimo=5
```

### Tuple

```python
coords = (10.5, 20.3)
x, y = coords  # Unpacking
# Imutável — não pode alterar após criação
```

### Dictionary

```python
pessoa = {"nome": "Ana", "idade": 25, "cidade": "SP"}
pessoa["email"] = "ana@email.com"
pessoa.get("telefone", "N/A")
pessoa.keys()      # dict_keys
pessoa.values()    # dict_values
pessoa.items()     # dict_items
pessoa.pop("cidade")
{**pessoa, "ativo": True}  # Merge

# Iterar
for k, v in pessoa.items():
    print(f"{k}: {v}")
```

### Set

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a | b      # União: {1,2,3,4,5,6}
a & b      # Interseção: {3,4}
a - b      # Diferença: {1,2}
a ^ b      # Simétrica: {1,2,5,6}
a.add(5)
a.discard(1)
```

---

## Controle de Fluxo

```python
# if-elif-else
if nota >= 9:
    conceito = "A"
elif nota >= 7:
    conceito = "B"
else:
    conceito = "C"

# Ternário
status = "aprovado" if nota >= 7 else "reprovado"

# match-case (Python 3.10+)
match comando:
    case "sair" | "exit":
        sys.exit()
    case "ajuda":
        mostrar_ajuda()
    case str(s) if s.startswith("/"):
        executar(s)
    case _:
        print("Comando desconhecido")

# for
for i in range(10):           # 0 a 9
for i in range(2, 10, 2):     # 2, 4, 6, 8
for i, item in enumerate(lista): # Com índice
for a, b in zip(lista1, lista2): # Paralelo

# while
while condicao:
    pass

# for-else
for item in itens:
    if item == alvo:
        break
else:
    print("Não encontrado")  # Executa se não deu break
```

---

## Funções

```python
# Básica
def somar(a: int, b: int) -> int:
    return a + b

# Parâmetros default
def saudar(nome: str, saudacao: str = "Olá") -> str:
    return f"{saudacao}, {nome}!"

# *args e **kwargs
def func(*args, **kwargs):
    print(args)    # Tupla de posicionais
    print(kwargs)  # Dict de nomeados

func(1, 2, 3, nome="Ana", idade=25)

# Lambda
quadrado = lambda x: x ** 2
sorted(lista, key=lambda x: x["nome"])

# Funções built-in úteis
map(str.upper, ["a", "b"])     # Aplica função
filter(lambda x: x > 0, nums) # Filtra
sum(nums)
min(nums), max(nums)
any([False, True, False])  # True
all([True, True, False])   # False
sorted(lista, key=len, reverse=True)
```

---

## OOP — Classes

```python
from dataclasses import dataclass

class Animal:
    """Classe base para animais."""

    total = 0  # Atributo de classe

    def __init__(self, nome: str, especie: str):
        self.nome = nome          # Atributo de instância
        self._especie = especie   # Protegido (convenção)
        Animal.total += 1

    def falar(self) -> str:
        return "..."

    @property
    def especie(self) -> str:
        return self._especie

    @staticmethod
    def info():
        return "Classe Animal"

    @classmethod
    def criar(cls, nome: str):
        return cls(nome, "Desconhecida")

    def __str__(self):
        return f"{self.nome} ({self._especie})"

    def __repr__(self):
        return f"Animal('{self.nome}', '{self._especie}')"


class Cachorro(Animal):
    def __init__(self, nome: str, raca: str):
        super().__init__(nome, "Canino")
        self.raca = raca

    def falar(self) -> str:
        return f"{self.nome} diz: Au au!"


# Dataclass (Python 3.7+)
@dataclass
class Ponto:
    x: float
    y: float
    z: float = 0.0

    def distancia(self, outro: "Ponto") -> float:
        return ((self.x - outro.x)**2 + (self.y - outro.y)**2) ** 0.5

p = Ponto(3, 4)  # __init__, __repr__, __eq__ automáticos
```

---

## Módulos e Pacotes

```python
# Importar módulo
import os
import json
from pathlib import Path
from datetime import datetime, timedelta
from collections import Counter, defaultdict
from typing import Optional, List

# Módulos úteis
import math       # sin, cos, sqrt, pi
import random     # randint, choice, shuffle
import re         # regex
import hashlib    # hash (md5, sha256)
import uuid       # UUID únicos
import csv        # Leitura/escrita CSV
import sqlite3    # Banco de dados embutido

# pip (gerenciador de pacotes)
# pip install requests flask pandas
import requests
response = requests.get("https://api.example.com/data")
data = response.json()

# Criar pacote
# meu_pacote/
#   __init__.py
#   modulo1.py
#   modulo2.py
```

---

## Tratamento de Erros

```python
# try-except-else-finally
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Divisão por zero!")
except (ValueError, TypeError) as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")
else:
    print("Sem erros!")    # Só executa se NÃO houve exceção
finally:
    print("Sempre executa")

# Lançar exceção
def dividir(a, b):
    if b == 0:
        raise ValueError("Divisor não pode ser zero")
    return a / b

# Exceção customizada
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, valor):
        super().__init__(f"Saldo {saldo} insuficiente para {valor}")
        self.saldo = saldo
        self.valor = valor

# assert (desenvolvimento/testes)
assert idade >= 0, "Idade não pode ser negativa"
```

---

## Arquivos e I/O

```python
from pathlib import Path

# Ler arquivo
with open("dados.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()        # Tudo de uma vez
    # ou
    linhas = f.readlines()     # Lista de linhas

# Escrever arquivo
with open("saida.txt", "w", encoding="utf-8") as f:
    f.write("Linha 1\n")
    f.writelines(["Linha 2\n", "Linha 3\n"])

# Append
with open("log.txt", "a") as f:
    f.write("Nova entrada\n")

# JSON
import json
with open("config.json") as f:
    config = json.load(f)

with open("output.json", "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# CSV
import csv
with open("dados.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["nome"])

# Pathlib (moderno)
p = Path("pasta/subpasta")
p.mkdir(parents=True, exist_ok=True)
p.exists()
p.is_file()
p.glob("*.py")         # Listar .py
p.read_text()           # Ler conteúdo
p.write_text("conteúdo") # Escrever
```

---

## Comprehensions e Generators

```python
# List comprehension
quadrados = [x**2 for x in range(10)]
pares = [x for x in range(20) if x % 2 == 0]
matrix_flat = [n for row in matrix for n in row]

# Dict comprehension
contagem = {c: texto.count(c) for c in set(texto)}
inverso = {v: k for k, v in original.items()}

# Set comprehension
unicos = {palavra.lower() for palavra in texto.split()}

# Generator expression (lazy — não carrega tudo na memória)
soma = sum(x**2 for x in range(1_000_000))

# Generator function
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
[next(fib) for _ in range(10)]  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

---

## Decorators e Context Managers

```python
# Decorator
import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} levou {elapsed:.4f}s")
        return result
    return wrapper

@timer
def processar_dados():
    time.sleep(1)

# Decorator com parâmetros
def retry(tentativas=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(tentativas):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if i == tentativas - 1:
                        raise
        return wrapper
    return decorator

@retry(tentativas=5)
def api_call():
    pass

# Context Manager
from contextlib import contextmanager

@contextmanager
def timer_context(label):
    start = time.perf_counter()
    yield
    print(f"{label}: {time.perf_counter() - start:.4f}s")

with timer_context("Processamento"):
    processar_dados()
```

---

## Type Hints e Async

### Type Hints (Python 3.9+)

```python
from typing import Optional, Union

def buscar(id: int) -> Optional[dict]:
    ...

def processar(dados: list[dict[str, int]]) -> list[str]:
    ...

# Union types (Python 3.10+)
def converter(valor: int | float | str) -> str:
    return str(valor)
```

### Async/Await

```python
import asyncio

async def fetch_data(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()

async def main():
    # Execução paralela
    resultados = await asyncio.gather(
        fetch_data("https://api1.com"),
        fetch_data("https://api2.com"),
        fetch_data("https://api3.com"),
    )
    return resultados

asyncio.run(main())
```

---

*Fonte: [W3Schools Python](https://www.w3schools.com/python/) · [Python 3 Docs](https://docs.python.org/3/)*
