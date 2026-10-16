---json
{
  "id": "documentacao_c",
  "title": "Documentação C — Guia Completo",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Fonte:** [W3Schools C](https://www.w3schools.com/c/index.php) · [cppreference.com](https://en.cppreference.com/w/c) **Versão:** C17/C23",
  "gatilhos": [
    "completo",
    "documentacao",
    "guia",
    "linguagens",
    "php"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação C — Guia Completo?",
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

# Documentação C — Guia Completo

> **Fonte:** [W3Schools C](https://www.w3schools.com/c/index.php) · [cppreference.com](https://en.cppreference.com/w/c)
> **Versão:** C17/C23
> **Atualizado:** 2026-02-14

---

## Sumário

1. [Fundamentos](#fundamentos)
2. [Tipos de Dados](#tipos-de-dados)
3. [Controle de Fluxo](#controle-de-fluxo)
4. [Arrays e Strings](#arrays-e-strings)
5. [Ponteiros](#ponteiros)
6. [Funções](#funções)
7. [Structs, Unions e Enums](#structs-unions-e-enums)
8. [Gerenciamento de Memória](#gerenciamento-de-memória)
9. [Arquivos](#arquivos)
10. [Preprocessador e Macros](#preprocessador-e-macros)

---

## Fundamentos

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    printf("Hello, World!\n");
    return 0;
}
```

### Compilar e executar

```bash
gcc -Wall -Wextra -o programa main.c
./programa
```

### Variáveis

```c
int idade = 25;
float preco = 19.99f;
double pi = 3.14159265358979;
char letra = 'A';
char nome[] = "João";

// Constantes
const int MAX = 100;
#define PI 3.14159
```

---

## Tipos de Dados

| Tipo | Tamanho | Formato printf |
|---|---|---|
| `char` | 1 byte | `%c` (char), `%d` (int) |
| `short` | 2 bytes | `%hd` |
| `int` | 4 bytes | `%d` |
| `long` | 4/8 bytes | `%ld` |
| `long long` | 8 bytes | `%lld` |
| `float` | 4 bytes | `%f`, `%.2f` |
| `double` | 8 bytes | `%lf` |
| `unsigned int` | 4 bytes | `%u` |
| `size_t` | 4/8 bytes | `%zu` |

### Conversão de tipos (casting)

```c
int a = 5, b = 2;
double resultado = (double) a / b;  // 2.5
int truncado = (int) 3.99;          // 3
```

---

## Controle de Fluxo

```c
// if-else
if (idade >= 18) {
    printf("Maior de idade\n");
} else if (idade >= 12) {
    printf("Adolescente\n");
} else {
    printf("Criança\n");
}

// Ternário
char* status = (idade >= 18) ? "adulto" : "menor";

// switch
switch (opcao) {
    case 1: printf("Opção 1\n"); break;
    case 2: printf("Opção 2\n"); break;
    default: printf("Inválido\n");
}

// for
for (int i = 0; i < 10; i++) { }

// while
while (condicao) { }

// do-while
do { } while (condicao);
```

---

## Arrays e Strings

### Arrays

```c
// Declaração
int nums[5] = {10, 20, 30, 40, 50};
int zeros[100] = {0};  // Todos zero
int auto_size[] = {1, 2, 3};  // Tamanho 3

// Multidimensional
int matrix[3][3] = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

// Tamanho
int tamanho = sizeof(nums) / sizeof(nums[0]);  // 5
```

### Strings

```c
#include <string.h>

char nome[50] = "João";
char sobrenome[] = "Silva";

strlen(nome);                     // 4
strcpy(destino, origem);          // Copiar
strncpy(dest, orig, n);          // Copiar n chars
strcat(nome, " Silva");          // Concatenar
strncat(s1, s2, n);
strcmp(s1, s2);                   // 0 = igual
strncmp(s1, s2, n);
strchr(nome, 'o');               // Encontrar char
strstr(texto, "busca");          // Encontrar substring
sprintf(buffer, "Idade: %d", 25); // Printf em string
snprintf(buf, sizeof(buf), "%s", str); // Seguro

// Entrada
char input[100];
fgets(input, sizeof(input), stdin);  // Seguro (usa isso!)
// NUNCA use gets() - buffer overflow
```

---

## Ponteiros

```c
int x = 42;
int *ptr = &x;       // Ponteiro para x

printf("%p\n", ptr);  // Endereço de memória
printf("%d\n", *ptr); // 42 (valor apontado)

*ptr = 100;           // x agora é 100

// Ponteiro nulo
int *p = NULL;
if (p != NULL) { /* seguro */ }

// Ponteiro para array
int arr[] = {10, 20, 30};
int *p = arr;         // Aponta para arr[0]
printf("%d\n", *(p + 1));  // 20 (aritmética de ponteiros)
printf("%d\n", p[1]);      // 20 (equivalente)

// Array de ponteiros
char *cores[] = {"vermelho", "azul", "verde"};

// Ponteiro para ponteiro
int **pp = &ptr;
printf("%d\n", **pp);  // 42

// const com ponteiros
const int *p1 = &x;   // Não pode mudar o valor via p1
int *const p2 = &x;   // Não pode mudar para onde p2 aponta
const int *const p3 = &x;  // Ambos const
```

---

## Funções

```c
// Declaração e definição
int somar(int a, int b) {
    return a + b;
}

// Protótipo (declaração antecipada)
void exibir(const char *msg);

// Passagem por referência (via ponteiro)
void dobrar(int *valor) {
    *valor *= 2;
}
int x = 5;
dobrar(&x);  // x agora é 10

// Array como parâmetro
void imprimir(int arr[], int tamanho) {
    for (int i = 0; i < tamanho; i++)
        printf("%d ", arr[i]);
}

// Ponteiro de função
int (*operacao)(int, int) = somar;
int resultado = operacao(3, 4);  // 7

// Callback
void aplicar(int *arr, int n, int (*func)(int)) {
    for (int i = 0; i < n; i++)
        arr[i] = func(arr[i]);
}
int quadrado(int x) { return x * x; }
aplicar(nums, 5, quadrado);

// Variadic
#include <stdarg.h>
double media(int count, ...) {
    va_list args;
    va_start(args, count);
    double soma = 0;
    for (int i = 0; i < count; i++)
        soma += va_arg(args, double);
    va_end(args);
    return soma / count;
}
```

---

## Structs, Unions e Enums

### Struct

```c
// Definição
typedef struct {
    char nome[50];
    int idade;
    double salario;
} Pessoa;

// Uso
Pessoa p1 = {"Maria", 30, 5000.0};
printf("%s tem %d anos\n", p1.nome, p1.idade);

// Ponteiro para struct
Pessoa *ptr = &p1;
printf("%s\n", ptr->nome);  // Operador seta

// Struct aninhada
typedef struct {
    char rua[100];
    int numero;
    char cidade[50];
} Endereco;

typedef struct {
    char nome[50];
    Endereco endereco;
} Cliente;

// Struct com padding
// Use __attribute__((packed)) para remover padding (GCC)
```

### Union

```c
typedef union {
    int inteiro;
    float decimal;
    char texto[20];
} Valor;

Valor v;
v.inteiro = 42;       // Usa o mesmo espaço de memória
v.decimal = 3.14f;    // Sobrescreve inteiro
```

### Enum

```c
typedef enum {
    DOMINGO,     // 0
    SEGUNDA,     // 1
    TERCA,       // 2
    QUARTA,      // 3
    QUINTA,      // 4
    SEXTA,       // 5
    SABADO       // 6
} DiaSemana;

typedef enum {
    HTTP_OK = 200,
    HTTP_NOT_FOUND = 404,
    HTTP_SERVER_ERROR = 500
} HttpStatus;
```

---

## Gerenciamento de Memória

```c
#include <stdlib.h>

// malloc — alocar memória
int *arr = (int *) malloc(10 * sizeof(int));
if (arr == NULL) {
    fprintf(stderr, "Erro de alocação!\n");
    exit(1);
}

// calloc — alocar e zerar
int *zeros = (int *) calloc(10, sizeof(int));

// realloc — redimensionar
arr = (int *) realloc(arr, 20 * sizeof(int));

// free — liberar memória
free(arr);
arr = NULL;  // Evitar dangling pointer

// Exemplo: array dinâmico
typedef struct {
    int *dados;
    int tamanho;
    int capacidade;
} VetorDinamico;

VetorDinamico* criar_vetor(int capacidade) {
    VetorDinamico *v = malloc(sizeof(VetorDinamico));
    v->dados = malloc(capacidade * sizeof(int));
    v->tamanho = 0;
    v->capacidade = capacidade;
    return v;
}

void destruir_vetor(VetorDinamico *v) {
    free(v->dados);
    free(v);
}
```

---

## Arquivos

```c
#include <stdio.h>

// Escrever
FILE *fp = fopen("dados.txt", "w");
if (fp == NULL) { perror("Erro"); exit(1); }
fprintf(fp, "Nome: %s\nIdade: %d\n", "Ana", 25);
fclose(fp);

// Ler
FILE *fp = fopen("dados.txt", "r");
char linha[256];
while (fgets(linha, sizeof(linha), fp) != NULL) {
    printf("%s", linha);
}
fclose(fp);

// Binário
FILE *fp = fopen("dados.bin", "wb");
int nums[] = {1, 2, 3, 4, 5};
fwrite(nums, sizeof(int), 5, fp);
fclose(fp);

// Modos: "r" ler, "w" escrever, "a" append
//        "rb"/"wb"/"ab" para binário
//        "r+"/"w+" leitura+escrita
```

---

## Preprocessador e Macros

```c
// Include guards
#ifndef MEU_HEADER_H
#define MEU_HEADER_H

// Macros
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define ARRAY_SIZE(arr) (sizeof(arr) / sizeof((arr)[0]))
#define LOG(msg) fprintf(stderr, "[LOG] %s:%d: %s\n", __FILE__, __LINE__, msg)

// Compilação condicional
#ifdef DEBUG
    #define DBG(x) printf("DEBUG: %s = %d\n", #x, x)
#else
    #define DBG(x)
#endif

// Pragmas
#pragma once  // Alternativa a include guards

#endif
```

---

*Fonte: [W3Schools C](https://www.w3schools.com/c/) · [cppreference.com](https://en.cppreference.com/w/c)*
