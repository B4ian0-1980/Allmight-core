---json
{
  "id": "npf_ldkls202_u1s2_lin_pro3p",
  "title": "Exemplo de uso do continue",
  "categoria": "03-linguagens",
  "subcategoria": "python",
  "resumo": "Guia tecnico e referencias sobre Exemplo de uso do continue.",
  "gatilhos": [
    "continue",
    "exemplo",
    "ldkls202",
    "lin",
    "linguagens",
    "npf",
    "pro3p",
    "python"
  ],
  "perguntas_tipo": [
    "Como utilizar Exemplo de uso do continue?",
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

NÃO PODE FALTAR

## ESTRUTURAS LÓGICAS, CONDICIONAIS E DE REPETIÇÃO EM
## PYTHON

Vanessa Cadan Scheer

Criamos algoritmos para resolver problemas, o que implica tomar decisões. No

universo da programação, a técnica que nos permite tomar decisões é chamada de

estrutura condicional (MANZANO; OLIVEIRA, 2019). A Figura 1.5 ilustra uma cidade e

suas vias. Ao dirigir em uma cidade, você precisa decidir quais caminhos (ruas)

seguir com o objetivo de chegar a um destino; por exemplo, em um cruzamento,

pode-se virar à direita ou à esquerda e/ou seguir em frente. Um programa funciona

de forma similar: deve-se decidir qual caminho será executado em um código. Em

geral, em um programa você tem opções de caminhos ou lista de comandos que

nada mais são que trechos de códigos que podem ser executados, devendo-se

tomar decisões sobre qual trecho de código será executado em um determinado

momento.

AS ESTRUTURAS DE COMANDO EM PYTHON

Vamos conhecer alguns trechos de código e sua lógica de execução.

Fonte: Shutterstock.

Deseja ouvir este material?

Áudio disponível no material digital.

In [1]:
In [2]:
In [3]:
In [4]:
In [5]:
In [6]:
In [7]:
In [8]:
In [9]:
In [10]:
In [11]:
In [12]:

Imprimir

0
Ver anotações

npf_ldkls202_u1s2_lin_pro
https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...

1 of 15
14/12/2021 07:52


--------------------------------------------------

Figura 1.5 | Fluxo de tomada de decisões de um algoritmo para a escolha de um caminho em uma

cidade

Fonte: adaptada de Griths e Barry (2009, p. 13).

Para tomarmos decisões, precisamos dos operadores relacionais (Quadro 1.2), que

já fazem parte do nosso vocabulário, desde as aulas de matemática do colégio.

Vamos usá-los para fazer comparações entre objetos (lembrando que em Python

tudo é objeto, então uma variável também é um objeto).

0
Ver anotações

npf_ldkls202_u1s2_lin_pro
https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...

2 of 15
14/12/2021 07:52


--------------------------------------------------

Quadro 1.2 - Operadores relacionais

Operação
Signicado

a < b
O valor de a é menor que b?

a <= b
O valor de a é menor OU igual que b?

a > b
O valor de a é maior que b?

a >= b
O valor de a é maior OU igual que b?

a == b
O valor de a é igual ao de b?

a != b
O valor de a é diferente do valor de b?

a is b
O valor de a é idêntico ao valor de b?

a is not b
O valor de a não é idêntico ao valor de b?

Fonte: adaptado de https://docs.python.org/3/library/stdtypes.html.

### ESTRUTURAS CONDICIONAIS EM PYTHON: IF, ELIF, ELSE

O comando if.. else.. signicam se.. senão.. e são usados para constuir as estruturas

condicionais. Se uma condição for satisfeita, então o uxo de execução segue por

um caminho, se não for satisfeito então segue por outro caminho. A Figura 1.6

ilustra um exemplo de tomada de decisão. No exemplo, dois caminhos podem ser

seguidos pelo condutor: um verdadeiro (TRUE), e um falso (FALSE). Assim funciona

uma condição: ela pode ser satisfeita (Verdade) ou não (Falsa). No exemplo, se a

idade for menor ou igual a 3, o condutor seguirá o caminho verdadeiro. Por sua vez,

se ela for maior que 3, seguirá o caminho falso.

Figura 1.6 | Tomada de decisão utilizando Se/senão (If/else)

0
Ver anotações

npf_ldkls202_u1s2_lin_pro
https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...

3 of 15
14/12/2021 07:52


--------------------------------------------------

a** =** 5
b** =** 10

if a** <** b:
print("a é menor do que b")
r** =** a** +** b
print(r)

Como você pode observar, a construção do if (se) deve ser feita com dois pontos ao

nal da condição, e o bloco de ações que devem ser feitas. Caso o trecho seja

verdadeiro, deve possuir uma indentação especíca de uma tabulação ou 4 espaços

em branco. Repare que não precisamos escrever if a < b == True.

O código apresentado na entrada 1(In [1]) refere-se a uma estrutura condicional

simples, pois só existem ações caso a condição seja verdadeira. Veja como construir

uma estrutura composta:

a** =** 10
b** =** 5

if a** <** b:
print("a é menor do que b")
r** =** a** +** b
print(r)
else:
print("a é maior do que b")
r** =** a** -** b
print(r)

O código apresentado na entrada 2(In [2]) refere-se a uma estrutura condicional

composta, pois existem ações tanto para a condição verdadeira quanto para a falsa.

Veja que o else (senão) está no mesmo nível de identação do if, e os blocos de

ações com uma tabulação de indentação.

Além das estruturas simples e compostas, existem as estruturas encadeadas. Em

diversas linguagens como C, Java, C#, C++, etc, essa estrutura é construída como o

comando switch..case. Em Python, não existe o comando switch

(https://docs.python.org/3/tutorial/controlow.html). Para construir uma estrutura

encadeada, devemos usar o comando "elif", que é uma abreviação de else if. Veja

um exemplo desse tipo de estrutura:

a é menor do que b
15

a é maior do que b
5

0
Ver anotações

npf_ldkls202_u1s2_lin_pro
https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...

4 of 15
14/12/2021 07:52


--------------------------------------------------

codigo_compra** =** 5111

if codigo_compra** ==** 5222:
print("Compra à vista.")
elif codigo_compra** ==** 5333:
print("Compra à prazo no boleto.")
elif codigo_compra** ==** 5444:
print("Compra à prazo no cartão.")
else:
print("Código não cadastrado")

O código apresentado na entrada 3 (In [3]) mostra a construção de uma estrutura

condicional encadeada. Veja que começamos pelo teste com if, depois testamos

várias alternativas com o elif e, por m, colocamos uma mensagem, caso nenhuma

opção seja verdadeira, no else.

### ESTRUTURAS LÓGICAS EM PYTHON: AND, OR, NOT

Além dos operadores relacionais, podemos usar os operadores booleanos para

construir estruturas de decisões mais complexas.

• Operador booleano and: Esse operador faz a operação lógica E, ou seja, dada a

expressão (a and b), o resultado será True, somente quando os dois

argumentos forem verdadeiros.

• Operador booleano or: Esse operador faz a operação lógica OU, ou seja, dada a

expressão (a or b), o resultado será True, quando pelo menos um dos

argumentos for verdadeiro.

• Operador booleano not: Esse operador faz a operação lógica NOT, ou seja,

dada a expressão (not a), ele irá inverter o valor do argumento. Portanto, se o

argumento for verdadeiro, a operação o transformará em falso e vice-versa.

Observe o exemplo a seguir, que cria uma estrutura condicional usando os

operadores booleanos. Um aluno só pode ser aprovado caso ele tenha menos de 5

faltas e média nal superior a 7.

qtde_faltas** =** int(input("Digite a quantidade de faltas: "))
media_final** =** float(input("Digite a média final: "))

if qtde_faltas** <=** 5 and media_final** >=** 7:
print("Aluno aprovado!")
else:
print("Aluno reprovado!")

No exemplo da entrada 4 (In [4]), zemos a conversão do tipo string para numérico,

encadeando funções. Como já sabemos, primeiro são resolvidos os parênteses

mais internos, ou seja, na linha 1, será feita primeiro a função input(), em seguida, a

Código não cadastrado

Digite a quantidade de faltas: 2
Digite a média final: 7
Aluno aprovado!

0
Ver anotações

npf_ldkls202_u1s2_lin_pro
https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...

5 of 15
14/12/2021 07:52


--------------------------------------------------

entrada digitada será convertida para inteira com a função int(). A mesma lógica se

aplica na linha 2, na qual a entrada é convertida para ponto utuante. Na linha 4

zemos o teste condicional, primeiro são resolvidos os operadores relacionais, em

seguida, os lógicos.

Obs: not tem uma prioridade mais baixa que os operadores relacionais.

Portanto, not a == b é interpretado como: not (a == b) e a == not b gera um erro

de sintaxe.

Obs2: Assim como as operações matemáticas possuem ordem de precedência,

as operações booleanas também têm. Essa prioridade obedece à seguinte

ordem: not primeiro, and em seguida e or por último (BANIN, 2018).

Veja o exemplo a seguir:

A** =** 15
B** =** 9
C** =** 9

print(B** ==** C or A** <** B and A** <** C)
print((B** ==** C or A** <** B) and A** <** C )

Na entrada 5 (In [5]), temos os seguintes casos:

Linha 5: True or False and False. Nesse caso será feito primeiro o and, que resulta

em False, mas em seguida é feito o or, que então resulta em verdadeiro.

Linha 6: (True or False) and False. Nesse caso será feito primeiro o or, que resulta

em True, mas em seguida é feito o and, que então resulta em falso, pois ambos

teriam que ser verdadeiro para o and ser True.

Utilize o emulador a seguir para testar os códigos. Crie novas variáveis e condições

para treinar.

True
False

0
Ver anotações

npf_ldkls202_u1s2_lin_pro
https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...

6 of 15
14/12/2021 07:52


--------------------------------------------------



 Code

Remix


3

Python3

Run
Share

Procurar…
Nenhum arquivo selecionado.


main.py
inammation-01.csv


### ESTRUTURAS DE REPETIÇÃO EM PYTHON: WHILE E FOR

É comum, durante a implementação de uma solução, criarmos estruturas que

precisam executar várias vezes o mesmo trecho de código. Tal estrutura é chamada

de estrutura de repetição e, em Python, pode ser feita pelo comando while

(enquanto) ou pelo comando for (para). Antes de apresentarmos a implementação,

observe a Figura 1.7. Temos a ilustração de uma estrutura de repetição por meio de

uma montanha russa. Enquanto uma condição for verdadeira, ou seja, enquanto x

for menor ou igual a 3, o condutor continuará no loop; quando for falsa, ou seja,

quando x for maior que 3, então ele sairá.

Em uma estrutura de repetição sempre haverá uma estrutura decisão, pois a

repetição de um trecho de código sempre está associada a uma condição. Ou seja,

um bloco de comandos será executado repetidas vezes, até que uma condição não

seja mais satisfeita.

0
Ver anotações

npf_ldkls202_u1s2_lin_pro
https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...

7 of 15
14/12/2021 07:52


--------------------------------------------------

Figura 1.7 | Fluxograma estrutura de repetição

numero** =** 1
while numero** !=** 0:
numero** =** int(input("Digite um número: "))
if numero** %** 2** ==** 0:
print("Número par!")
else:
print("Número ímpar!")

A seguir, você pode testar o código, vericando o passo a passo de sua execução.

Ao clicar em "Next", você irá para a próxima linha a ser executada do "while" para

cada um dos casos. Ao clicar em "Prev", você retorna a linha executada

anteriormente. Observe que a seta verde na linha de código representa a linha em

execução, e a seta vermelha representa a próxima linha a ser executada. Digite um

número, submeta, clique em "Next" e observe o uxo de execução e as saídas do

código.

Veja a construção do comando while na entrada 6 (In [6]). Na linha 1, criamos uma

variável chamada número com valor 1. Na linha 2 criamos a estrutura de repetição,

veja que o comando while possui uma condição: o número tem que ser diferente de

zero para o bloco executar. Todo o bloco com a identação de uma tabulação (4

espaços) faz parte da estrutura de repetição. Lembre: todos os blocos de comandos

em Python são controlados pela indentação.

Digite um número: 4
Número par!
Digite um número: 7
Número ímpar!
Digite um número: 0
Número par!

0
Ver anotações

npf_ldkls202_u1s2_lin_pro
https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...

8 of 15
14/12/2021 07:52


--------------------------------------------------

Na prática é comum utilizarmos esse tipo de estrutura de repetição, com while,

para deixarmos serviços executando em servidores. Por exemplo, o serviço deve

car executando enquanto a hora do sistema for diferente de 20 horas.

Outro comando muito utilizado para construir as estruturas de repetição é o for. A

instrução for em Python difere um pouco do que ocorre em outras linguagens,

como C ou Java, com as quais você pode estar acostumado (https://docs.python.org

/3/tutorial/controlow.html). Em vez de sempre dar ao usuário a capacidade de

denir a etapa de iteração e a condição de parada (como C), a instrução Python for

itera sobre os itens de qualquer sequência, por exemplo, iterar sobre os caracteres

de uma palavra, pois uma palavra é um tipo de sequência. Observe um exemplo a

seguir
nome** =** "Guido"
for c in nome:
print(c)

Na entrada 7 (In [7]) construímos nossa primeira estrutura de repetição com for.

Vamos analisar a sintaxe da estrutura. Usamos o comando "for" seguido da variável

de controle "c", na sequência o comando "in", que traduzindo signica "em", por

m, a sequência sobre a qual a estrutura deve iterar. Os dois pontos marcam o

início do bloco que deve ser repetido.

Junto com o comando for, podemos usar a função enumerate() para retornar à

posição de cada item, dentro da sequência. Considerando o exemplo dado, no qual

atribuímos a variável "nome" o valor de "Guido", "G" ocupa a posição 0 na

sequência, "u" ocupa a posição 1, "i" a posição 2, e assim por diante. A função

enumerate() recebe como parâmetro a sequência e retorna a posição. Para que

possamos capturar tanto a posição quanto o valor, vamos precisar usar duas

variáveis de controle. Observe o código a seguir, veja que a variável "i" é usada para

capturar a posição e a variável "c" cada caracter da palavra.

nome** =** "Guido"
for i, c in enumerate(nome):
print(f"Posição = {i}, valor = {c}")

G
u
i
d
o

0
Ver anotações

npf_ldkls202_u1s2_lin_pro
https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...

9 of 15
14/12/2021 07:52


--------------------------------------------------

### CONTROLE DE REPETIÇÃO COM RANGE, BREAK E CONTINUE

Como já dissemos, o comando for em Python requer uma sequência para que

ocorra a iteração. Mas e se precisarmos que a iteração ocorra em uma sequência

numérica, por exemplo, de 0 a 5? Para criar uma sequência numérica de iteração

em Python, podemos usar a função range(). Observe o código a seguir.

for x in range(5):
print(x)

No comando, "x" é a variável de controle, ou seja, a cada iteração do laço, seu valor

é alterado, já a função range() foi utilizada para criar um "iterable" numérico (objeto

iterável) para que as repetições acontecesse. A função range() pode ser usada de

três formas distintas:

1. Método 1: passando um único argumento que representa a quantidade de

vezes que o laço deve repetir;

2. Método 2: passando dois argumentos, um que representa o início das

repetições e outro o limite superior (NÃO INCLUÍDO) do valor da variável de

controle;

3. Método 3: Passando três argumentos, um que representa o início das

repetições; outro, o limite superior (NÃO INCLUÍDO) do valor da variável de

controle e um que representa o incremento. Observe as três maneiras a seguir.

A execução dos três métodos pode ser visualizada a seguir. Ao clicar em "Next",

você irá para a próxima linha a ser executada do "for" para cada um dos casos.

Observe que a seta verde na linha de código representa a linha em execução, e a

seta vermelha representa a próxima linha a ser executada.

Além de controlar as iterações com o tamanho da sequência, outra forma de

inuenciar no uxo é por meio dos comandos "break" e "continue". O comando

break para a execução de uma estrutura de repetição, já com o comando continue,

conseguimos "pular" algumas execuções, dependendo de uma condição. Veja o

exemplo:

Posição = 0, valor = G
Posição = 1, valor = u

0
1
2
3
4

0
Ver anotações

npf_ldkls202_u1s2_lin_pro
https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...

10 of 15
14/12/2021 07:52


--------------------------------------------------

*# Exemplo de uso do break*
disciplina** =** "Linguagem de programação"
for c in disciplina:
if c** ==** 'a':
break
else:
print(c)

No exemplo com uso do break, perceba que foram impressas as letras L i n g u,

quando chegou a primeira letra a, a estrutura de repetição foi interrompida. Agora

observe o exemplo com continue.

# Exemplo de uso do continue
disciplina** =** "Linguagem de programação"
for c in disciplina:
if c** ==** 'a':
continue
else:
print(c)

No exemplo com uso do continue, perceba que foram impressas todas as letras,

exceto as vogais "a", pois toda vez que elas eram encontradas, o continue

determina que se pule, mas que a repetição prossiga para o próximo valor. Utilize o

emulador para executar os códigos e crie novas combinações para explorar.

L
i
n
g
u

L
i
n
g
u
g
e
m
d
e
p
r
o
g
r
m
ç
ã
o

0
Ver anotações

npf_ldkls202_u1s2_lin_pro
https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...

11 of 15
14/12/2021 07:52


--------------------------------------------------



 Code

Remix


3

Python3

Run
Share

Procurar…
Nenhum arquivo selecionado.


main.py
inammation-01.csv


0
Ver anotações

npf_ldkls202_u1s2_lin_pro
https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...

12 of 15
14/12/2021 07:52


--------------------------------------------------

EXEMPLIFICANDO

Vamos brincar um pouco com o que aprendemos. Vamos criar uma solução que

procura pelas vogais "a", "e" em um texto (somente minúsculas). Toda vez que

essas vogais são encontradas, devemos informar que encontramos e qual posição

do texto ela está. Nosso texto será:

texto = A inserção de comentários no código do programa é uma prática normal.

Em função disso, toda linguagem de programação tem alguma maneira de permitir

que comentários sejam inseridos nos programas. O objetivo é adicionar descrições

em partes do código, seja para documentá-lo ou para adicionar uma descrição do

algoritmo implementado (BANIN, 2018, p. 45).

texto** =** """
A inserção de comentários no código do programa é uma prática normal.
Em função disso, toda linguagem de programação tem alguma maneira de 
permitir que comentários sejam inseridos nos programas.
O objetivo é adicionar descrições em partes do código, seja para 
documentá-lo ou para adicionar uma descrição do algoritmo implementado 
(BANIN, p. 45, 2018)."
"""
for i, c in enumerate(texto):
if c** ==** 'a' or c** ==** 'e':
print(f"Vogal '{c}' encontrada, na posição {i}")
else:
continue

0
Ver anotações

npf_ldkls202_u1s2_lin_pro
https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...

13 of 15
14/12/2021 07:52


--------------------------------------------------

Uma novidade nesse exemplo foi o uso das aspas triplas para que pudéssemos

quebrar a linha do texto. As aspas triplas também podem ser usadas para criar

comentários de várias linhas em Python. Que tal alterar a solução de busca por

vogais e contar quantas vezes cada vogal foi encontrada. Lembre-se de que, quanto

mais praticar, mais desenvolverá sua lógica de programação e uência em uma

determinada linguagem!



 Code

Remix


3

Python3

Run
Share

Procurar…
Nenhum arquivo selecionado.


main.py
inammation-01.csv


### REFERÊNCIAS E LINKS ÚTEIS

BANIN, S. L. Python 3 - conceitos e aplicações: uma abordagem didática. São

Paulo: Érica, 2018.

Vogal 'e' encontrada, na posição 6
Vogal 'e' encontrada, na posição 13
Vogal 'e' encontrada, na posição 18
Vogal 'a' encontrada, na posição 45
Vogal 'a' encontrada, na posição 47
Vogal 'a' encontrada, na posição 53
Vogal 'a' encontrada, na posição 61
Vogal 'a' encontrada, na posição 67
Vogal 'a' encontrada, na posição 91
Vogal 'a' encontrada, na posição 98
Vogal 'e' encontrada, na posição 100
Vogal 'e' encontrada, na posição 104
Vogal 'a' encontrada, na posição 111
Vogal 'a' encontrada, na posição 113
Vogal 'e' encontrada, na posição 119
Vogal 'a' encontrada, na posição 122
Vogal 'a' encontrada, na posição 127
Vogal 'a' encontrada, na posição 130
Vogal 'e' encontrada, na posição 132
Vogal 'a' encontrada, na posição 135
Vogal 'e' encontrada, na posição 138
Vogal 'e' encontrada, na posição 141
Vogal 'e' encontrada, na posição 151
Vogal 'e' encontrada, na posição 156
Vogal 'e' encontrada, na posição 166
Vogal 'a' encontrada, na posição 168
V
l ' '
t
d
i ã
174

0
Ver anotações

npf_ldkls202_u1s2_lin_pro
https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...

14 of 15
14/12/2021 07:52


--------------------------------------------------

GRIFFITHS, D.; BARRY, P. Head First Programming: A learner's guide to

programming using the Python language. [S.l.]: O'Reilly Media, 2009.

MANZANO, J. A. N. G.; OLIVEIRA, J. F. de. Algoritmos: lógica para desenvolvimento de

programação de computadores. 29. ed. São Paulo: Érica, 2019.

PYTHON SOFTWARE FOUNDATION. More Control Flow Tools. Disponível em:

https://docs.python.org/3/tutorial/controlow.html. Acesso em: 15 abr. 2020.

PYTHON SOFTWARE FOUNDATION. Numeric Types: int, oat, complex. Disponível

em: https://docs.python.org/3/library/stdtypes.html. Acesso em: 15 abr. 2020.

SUBSECRETARIA DE TRIBUTAÇÃO E CONTENCIOSO. Imposto sobre a renda das

pessoas físicas. Disponível em: http://receita.economia.gov.br/acesso-rapido

b
f
d
d

b

0
Ver anotações

npf_ldkls202_u1s2_lin_pro
https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...

15 of 15
14/12/2021 07:52

