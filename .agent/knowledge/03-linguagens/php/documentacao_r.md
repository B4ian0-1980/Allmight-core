---json
{
  "id": "documentacao_r",
  "title": "Documentação R — Guia Completo",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Fonte:** [W3Schools R](https://www.w3schools.com/r/default.asp) · [R Project](https://www.r-project.org/other-docs.html) **Versão:** R 4.3+",
  "gatilhos": [
    "completo",
    "documentacao",
    "guia",
    "linguagens",
    "php"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação R — Guia Completo?",
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

# Documentação R — Guia Completo

> **Fonte:** [W3Schools R](https://www.w3schools.com/r/default.asp) · [R Project](https://www.r-project.org/other-docs.html)
> **Versão:** R 4.3+
> **Atualizado:** 2026-02-14

---

## Sumário

1. [Fundamentos](#fundamentos)
2. [Tipos de Dados](#tipos-de-dados)
3. [Vetores e Matrizes](#vetores-e-matrizes)
4. [Data Frames](#data-frames)
5. [Controle de Fluxo](#controle-de-fluxo)
6. [Funções](#funções)
7. [Manipulação de Dados (tidyverse)](#manipulação-de-dados)
8. [Visualização (ggplot2)](#visualização-ggplot2)
9. [Estatística](#estatística)
10. [I/O e Arquivos](#io-e-arquivos)

---

## Fundamentos

```r
# Hello World
print("Hello, World!")
cat("Hello, World!\n")

# Variáveis (atribuição com <- ou =)
nome <- "Maria"
idade <- 30
salario <- 4500.50
ativo <- TRUE

# Classe/tipo
class(nome)   # "character"
typeof(idade)  # "double"
is.numeric(idade)  # TRUE

# Help
?mean
help(mean)
```

---

## Tipos de Dados

| Tipo | Exemplo |
|---|---|
| `numeric` | `42`, `3.14` |
| `integer` | `42L` |
| `character` | `"hello"` |
| `logical` | `TRUE`, `FALSE` |
| `complex` | `3+4i` |
| `vector` | `c(1, 2, 3)` |
| `list` | `list(a=1, b="texto")` |
| `matrix` | `matrix(1:9, nrow=3)` |
| `data.frame` | Tabela |
| `factor` | Categóricos |
| `NULL`, `NA`, `NaN`, `Inf` | Especiais |

### Strings

```r
s <- "Hello World"
nchar(s)                # 11
toupper(s)              # "HELLO WORLD"
tolower(s)              # "hello world"
substr(s, 1, 5)         # "Hello"
gsub("World", "R", s)   # "Hello R"
strsplit(s, " ")        # list("Hello", "World")
paste("Hello", "R")     # "Hello R"
paste0("a", "b")        # "ab" (sem espaço)
sprintf("Nome: %s, Idade: %d", nome, idade)
grepl("World", s)       # TRUE
trimws("  hello  ")     # "hello"
```

---

## Vetores e Matrizes

### Vetores

```r
# Criação
nums <- c(10, 20, 30, 40, 50)
seq_nums <- 1:10
seq_custom <- seq(0, 100, by=5)
repetidos <- rep(0, times=5)
nomes <- c("Ana", "Bruno", "Carlos")

# Indexação (1-based!)
nums[1]           # 10
nums[2:4]         # 20 30 40
nums[c(1, 3, 5)]  # 10 30 50
nums[-1]          # Remove primeiro: 20 30 40 50
nums[nums > 25]   # Filtro: 30 40 50

# Operações vetorizadas
nums * 2          # 20 40 60 80 100
nums + c(1, 2, 3, 4, 5)  # Elemento a elemento
sum(nums)         # 150
mean(nums)        # 30
median(nums)      # 30
sd(nums)          # 15.81
min(nums); max(nums)
length(nums)      # 5
sort(nums, decreasing=TRUE)
which(nums > 25)  # Índices: 3 4 5
```

### Matrizes

```r
m <- matrix(1:9, nrow=3, ncol=3, byrow=TRUE)
#      [,1] [,2] [,3]
# [1,]    1    2    3
# [2,]    4    5    6
# [3,]    7    8    9

m[1,]       # Linha 1
m[,2]       # Coluna 2
m[2, 3]     # Elemento (2,3)
dim(m)      # 3 3
t(m)        # Transposta
m %*% m     # Multiplicação matricial
det(m)      # Determinante
```

---

## Data Frames

```r
# Criação
df <- data.frame(
  nome = c("Ana", "Bruno", "Carlos"),
  idade = c(25, 30, 22),
  salario = c(3000, 5000, 3500),
  stringsAsFactors = FALSE
)

# Acesso
df$nome           # Coluna nome
df[1, ]           # Primeira linha
df[, "idade"]     # Coluna idade
df[df$idade > 25, ]  # Filtro

# Info
str(df)           # Estrutura
summary(df)       # Estatísticas
head(df, 2)       # Primeiras 2 linhas
nrow(df); ncol(df)
names(df)         # Nomes das colunas

# Manipulação
df$ativo <- TRUE                        # Nova coluna
df$salario_anual <- df$salario * 12     # Calculada
df <- df[order(df$idade), ]             # Ordenar
df <- subset(df, idade > 22)            # Filtrar
df <- merge(df1, df2, by="id")         # Join
```

---

## Controle de Fluxo

```r
# if-else
if (idade >= 18) {
  cat("Adulto\n")
} else if (idade >= 12) {
  cat("Adolescente\n")
} else {
  cat("Criança\n")
}

# ifelse (vetorizado)
status <- ifelse(df$idade >= 18, "adulto", "menor")

# for
for (i in 1:10) { cat(i, " ") }
for (nome in nomes) { cat(nome, "\n") }

# while
while (x > 0) { x <- x - 1 }

# apply (preferir sobre loops)
sapply(nums, function(x) x^2)       # Retorna vetor
lapply(lista, function(x) x*2)      # Retorna lista
apply(matrix, 1, sum)                # Aplica por linha
tapply(df$salario, df$dept, mean)    # Agrupa e aplica
mapply(function(a, b) a+b, x, y)    # Múltiplos vetores
```

---

## Funções

```r
# Função básica
somar <- function(a, b) {
  return(a + b)
}

# Default args (último valor é retorno implícito)
saudar <- function(nome, saudacao = "Olá") {
  paste(saudacao, nome)
}

# Varargs
soma <- function(...) {
  sum(c(...))
}

# Pipe operator (R 4.1+)
resultado <- nums |>
  sort() |>
  rev() |>
  head(3)

# Closure
criar_contador <- function() {
  count <- 0
  function() {
    count <<- count + 1  # <<- modifica variável do pai
    count
  }
}
cont <- criar_contador()
cont()  # 1
cont()  # 2
```

---

## Manipulação de Dados

```r
library(dplyr)
library(tidyr)

# dplyr (tidyverse)
resultado <- df %>%
  filter(idade > 22) %>%
  mutate(salario_anual = salario * 12) %>%
  select(nome, idade, salario_anual) %>%
  arrange(desc(salario_anual)) %>%
  rename(Funcionario = nome)

# Agrupamento
resumo <- df %>%
  group_by(departamento) %>%
  summarise(
    media_sal = mean(salario),
    total = n(),
    .groups = "drop"
  )

# Join
inner_join(df1, df2, by = "id")
left_join(df1, df2, by = "id")

# Reshape com tidyr
pivot_longer(df, cols = c(jan, fev, mar), names_to = "mes", values_to = "venda")
pivot_wider(df, names_from = "mes", values_from = "venda")
```

---

## Visualização (ggplot2)

```r
library(ggplot2)

# Gráfico básico
ggplot(df, aes(x = idade, y = salario)) +
  geom_point(color = "steelblue", size = 3) +
  geom_smooth(method = "lm", se = FALSE) +
  labs(title = "Salário vs Idade",
       x = "Idade", y = "Salário (R$)") +
  theme_minimal()

# Barras
ggplot(df, aes(x = departamento, fill = departamento)) +
  geom_bar() +
  scale_fill_brewer(palette = "Set2") +
  theme_minimal()

# Histograma
ggplot(df, aes(x = salario)) +
  geom_histogram(bins = 30, fill = "coral", color = "white")

# Boxplot
ggplot(df, aes(x = dept, y = salario)) +
  geom_boxplot(fill = "lightblue")

# Salvar
ggsave("grafico.png", width = 10, height = 6, dpi = 300)
```

---

## Estatística

```r
# Descritiva
mean(x); median(x); sd(x); var(x)
quantile(x, probs = c(0.25, 0.5, 0.75))
cor(x, y)           # Correlação
table(categorias)    # Frequência

# Testes
t.test(grupo1, grupo2)                   # Teste t
chisq.test(tabela)                        # Qui-quadrado
cor.test(x, y, method = "pearson")        # Correlação
wilcox.test(grupo1, grupo2)               # Não-paramétrico

# Regressão linear
modelo <- lm(salario ~ idade + experiencia, data = df)
summary(modelo)
predict(modelo, newdata = data.frame(idade = 30, experiencia = 5))

# Distribuições
rnorm(100, mean = 0, sd = 1)   # Gerar normal
dnorm(0)                        # Densidade
pnorm(1.96)                     # Probabilidade acumulada
qnorm(0.975)                    # Quantil
```

---

## I/O e Arquivos

```r
# CSV
df <- read.csv("dados.csv", stringsAsFactors = FALSE)
write.csv(df, "saida.csv", row.names = FALSE)

# readr (tidyverse — mais rápido)
library(readr)
df <- read_csv("dados.csv")
write_csv(df, "saida.csv")

# Excel
library(readxl)
df <- read_excel("dados.xlsx", sheet = 1)

# JSON
library(jsonlite)
dados <- fromJSON("dados.json")
json_str <- toJSON(df, pretty = TRUE)

# RDS (formato nativo, compacto)
saveRDS(df, "dados.rds")
df <- readRDS("dados.rds")

# Diretórios
getwd()
setwd("/caminho")
list.files(".", pattern = "\\.csv$")
file.exists("arquivo.txt")
```

---

*Fonte: [W3Schools R](https://www.w3schools.com/r/) · [R Project](https://www.r-project.org/)*
