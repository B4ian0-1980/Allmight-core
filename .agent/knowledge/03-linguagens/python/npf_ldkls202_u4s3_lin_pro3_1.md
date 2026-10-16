---json
{
  "id": "npf_ldkls202_u4s3_lin_pro3_1",
  "title": "npf_ldkls202_u4s3_lin_pro3",
  "categoria": "03-linguagens",
  "subcategoria": "python",
  "resumo": "**Arquivo Original:** `npf_ldkls202_u4s3_lin_pro3.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "ldkls202",
    "lin",
    "linguagens",
    "npf",
    "npf_ldkls202_u4s3_lin_pro3",
    "pro3",
    "python",
    "u4s3"
  ],
  "perguntas_tipo": [
    "Como utilizar npf_ldkls202_u4s3_lin_pro3?",
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

# npf_ldkls202_u4s3_lin_pro3

> **Arquivo Original:** `npf_ldkls202_u4s3_lin_pro3.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 1

NÃO PODE FALTAR
VISUALIZAÇÃO DE DADOS EM PYTHON
Vanessa Cadan Sche�er
INTRODUÇÃO A VISUALIZAÇÃO DE DADOS EM PYTHON
BIBLIOTECAS E FUNÇÕES PARA CRIAÇÃO DE GRÁFICOS
Para a criação de grá�cos em Python são utilizadas as bibliotecas matplotib e outras baseadas
na matplotlib, e também funções que permitem criar e personalizar os grá�cos.
Fonte: Shutterstock.
Deseja ouvir este material?
Áudio disponível no material digital.
Visualização de dados ou DataViz é um dos pilares dos pro�ssionais que trabalham
com dados. Existem pro�ssionais que se especializam e inclusive tiram
certi�cações para atuar nessa área especí�ca. Após uma análise de dados e
extração de informações é interessante que a entrega de resultados para a área de
negócios seja feita de maneira visual, ou seja, por meio de grá�cos. Um grá�co
bem elaborado "fala" por si só e ajuda aos que assistem a entenderem os
resultados.
A linguagem Python, conta com uma série de bibliotecas que permitem a criação
Imprimir
0Ver anotações
npf_ldkls202_u4s3_lin_pro https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...
1 of 17 14/12/2021 07:51

## Página 2

de grá�cos, os quais podem ser estáticos (sem iteração) ou dinâmicos, que
apresentam iteração, como por exemplo, responder a eventos de clique do mouse.
Nessa aula, nossa objetivo é apresentar um pouco desse universo de
possibilidades.
0Ver anotações
npf_ldkls202_u4s3_lin_pro https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...
2 of 17 14/12/2021 07:51

## Página 3

MATPLOTLIB
frommatplotlib import pyplot as plt
%matplotlib inline
Ao se falar em criação de grá�cos em Python, o pro�ssional precisa conhecer a
biblioteca matplotlib, pois diversas outras são construídas a partir desta. A criação
e grande parte da evolução dessa biblioteca se deve a John Hunter, que a
desenvolveu como uma opção ao uso dos softwares gnuplot e MATLAB
(MCGREGGOR, 2015). Com a utilização da linguagem Python na área cientí�ca para
trabalhar com dados, após a extração dos resultados, o cientista precisava criar
seus grá�cos nos outros softwares mencionados, o que se tornava incoveniente,
motivando a criação da biblioteca em Python.
A instalação da biblioteca pode ser feita via pip install: pip install matplotlib,
lembrando que em ambientes como o projeto Anaconta e o Colab esse recurso já
está disponível. O módulo pyplot possui uma coleção de funções que permitem
criar e personalizar os grá�cos (https://matplotlib.org/api/_as_gen/matplotlib.pyplo
t.html). Existem duas sintaxes que são amplamente adotadas para importar essa
biblioteca para o projeto:
• import matplotlib.pyplot as plt
• from matplotlib import pyplot as plt
Em ambas formas de importação utilizamos o apelido "plt" que é uma convenção
adotada para facilitar o uso das funções. Ao trabalharmos no jupyter notebook
com o kernel do IPython (o kernel do IPython é o backend de execução do Python
para o Jupyter), podemos habilitar uma opção de fazer a impressão do grá�co
"inline", ou seja, no próprio notebook. Essa opção faz parte do "Built-in magic
commands", cuja documentação pode ser acessada no endereço https://ipython.re
adthedocs.io/en/stable/interactive/magics.html. Para habilitar utiliza-se a sintaxe:
%matplotlib inline. Portanto, projetos no jupyter notebook, que utilizem o
matplotlib sempre terão no começo, os comandos a seguir.
In [1]:
Os grá�cos são uma forma visual de "contar" a história dos dados. Em breve
contaremos várias histórias, mas como nosso primeiro grá�co, que tal um pouco
de arte abstrata? Vamos criar duas listas aleatórias de valores inteiros com o
0Ver anotações
npf_ldkls202_u4s3_lin_pro https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...
3 of 17 14/12/2021 07:51

## Página 4

importrandom
dados1=random.sample(range(100), k=20)
dados2=random.sample(range(100), k=20)
plt.plot(dados1, dados2) # pyplot gerencia a figura e o eixo
FIGURA COM EIXO COMO VARIÁVEL
Vamos explorar o estilo orientado a objetos, começando pela criação de eixos de
forma explícita, ou seja com atribuição a uma variável. Vamos criar uma �gura com
1 linha 2 duas colunas, ou seja, teremos dois eixos. Pense nos eixos como uma
matriz, na qual cada eixo é uma posição que pode ter uma �gura alocada. Vale
módulo random e então plotar um grá�co de linhas, com a função plt.plot() do
módulo pyplot. Veja a seguir, após criar duas listas com valores aleatórios, a função
plot() as recebe como parâmetros, utilizando-as para os valores dos eixos
horizontal (x) e vertical (y) e já cria o grá�co. Mágico não? Mas como "ele" sabia que
era para criar um grá�co de linhas? Por que colocou a cor azul? Por que fez desse
tamanho? Todos esses parâmetros e muitos outros, podem ser con�gurados!
In [2]:
Existem essencialmente duas maneiras de usar o Matplotlib:
1. Deixar para o pyplot criar e gerenciar automaticamente �guras e eixos, e usar
as funções do pyplot para plotagem.
2. Criar explicitamente �guras e eixos e chamar métodos sobre eles (o "estilo
orientado a objetos (OO)").
No grá�co que criamos, nós utilizamos a opção 1, ou seja, foi o próprio módulo
que criou o ambiente da �gura e do eixo. Ao utilizar a segunda opção, podemos
criar uma �gura com ou sem eixos, com a função plt.subplots(), que quando
invocada sem parâmetros, cria um layout de �gura com 1 linha e 1 coluna.
[<matplotlib.lines.Line2D at 0x1cf32995940>]
Out[2]:
0Ver anotações
npf_ldkls202_u4s3_lin_pro https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...
4 of 17 14/12/2021 07:51

## Página 5

ressaltar que sobre um eixo (sobre uma �gura), podem ser plotados diversos
grá�cos. Para criar essa estrutura usamos a sintaxe: fig, ax = plt.subplots(1,
2), onde �g e ax são os nomes das variáveis escolhidas. A variável ax, é do tipo
array numpy, ou seja, os eixos nada mais são, que uma matriz de contêiners para
se criar os plots. Como a �gura possui dois eixos, temos que especi�car em qual
vamos plotar, para isso informamos qual contêiner vamos usar: ax[0] ou ax[1].
Veja o código a seguir. Na linha 6 criamos a �gura, com 1 linha 2 colunas e o eixo
que vamos utilizar e ainda de�nimos o tamanho das �guras por meio do
parâmetro �gsize. Nas linhas 8, 9 e 10, imprimimos algumas informações para
entendermos esse mecanismo do pyplot. ax é do tipo 'numpy.ndarray', como já
havíamos mencionado. Ao imprimir o conteúdo de ax[0] e ax[1], podemos ver as
coordenadas alocadas para realizar a impressão da �guras. Das linhas 12 a 18,
imprimimos 3 grá�cos sobre o primeiro eixo (que será posicionado uma �gura do
lado esquerdo), de�nimos os rótulos dos eixos, o título do grá�co e pedimos para
exibir a legenda, que é construída a partir do parâmetro "label" na função plot().
Das linhas 20 a 26, criamos novos 3 grá�cos, mas agora sobre o segundo eixo (que
será posicionado uma �gura do lado direito). Nesse novo conjunto de grá�cos,
con�guramos a aparência das linhas, com os parâmetros 'r--' (red tracejado), 'b--'
(blue tracejado) e 'g--' (green tracejado). Observe o resultado dos grá�cos. Ao criar
uma estrutura com 1 linha e 2 colunas, os grá�cos �cam posicionados lado a lado,
e se tivéssemos criado com 2 linhas e 1 coluna?
In [3]:
0Ver anotações
npf_ldkls202_u4s3_lin_pro https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...
5 of 17 14/12/2021 07:51

## Página 6

importnumpy as np
x=range(5)
x=np.array(x) # temos que converter para um array numpy, 
senão o plot não consegue fazer operações.
fig, ax=plt.subplots(1, 2, figsize=(12, 5)) # Cria figura 
com subplots: 1 linha, 2 colunas e eixos
print("Tipo de ax = ", type(ax))
print("Conteúdo de ax[0] = ", ax[0])
print("Conteúdo de ax[1] = ", ax[1])
ax[0].plot(x, x, label='eq_1') # cria gráfico sobre eixo 0
ax[0].plot(x, x**2, label='eq_2') # cria gráfico sobre eixo 0
ax[0].plot(x, x**3, label='eq_3') # cria gráfico sobre eixo 0
ax[0].set_xlabel('Eixo x')
ax[0].set_ylabel('Eixo y')
ax[0].set_title("Gráfico 1")
ax[0].legend()
ax[1].plot(x, x, 'r--', label='eq_1') # cria gráfico sobre 
eixo 1
ax[1].plot(x**2, x, 'b--', label='eq_2') # cria gráfico sobre 
eixo 1
ax[1].plot(x**3, x, 'g--', label='eq_3') # cria gráfico sobre 
eixo 1
ax[1].set_xlabel('Novo Eixo x')
ax[1].set_ylabel('Novo Eixo y')
ax[1].set_title("Gráfico 2")
ax[1].legend()
FIGURA SEM EIXO COMO VARIÁVEL
Também podemos criar uma �gura, sem atribuir o eixo a uma variável. Nesse caso,
temos que usar a função plt.subplot(n_rows, n_cols2, plot_number), para
de�nir onde será plotado o grá�co. Veja no código a seguir. Na linha 4 criamos
uma �gura, mas agora sem eixo e sem especi�car o grid. Na linha 5, estamos
adicionando um subplot com 1 linha, 2 colunas e o primeiro grá�co (121). O
primeiro parâmetro do método subplot() é a quantidade de linhas; o segundo
parâmetro é a quantidade de colunas; o terceiro é número do plot dentro da
�gura, deve começar em 1 e ir até a quantidade de plots que se tem. Como o eixo
não está atribuído a nenhuma variável, agora usamos o próprio para acessar a
função plot(). Veja que na linha 14 estamos adicionando um subplot de 1 linha, 2
colunas a mesma �gura, mas agora especi�cando que plotaremos a segunda �gura
(122).
In [4]:
Tipo de ax =  <class 'numpy.ndarray'>
Conteúdo de ax[0] =  AxesSubplot(0.125,0.125;0.352273x0.755)
Conteúdo de ax[1] =  
AxesSubplot(0.547727,0.125;0.352273x0.755)
<matplotlib.legend.Legend at 0x1cf32a6cb00>
Out[3]:
0Ver anotações
npf_ldkls202_u4s3_lin_pro https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...
6 of 17 14/12/2021 07:51

## Página 7

BIBLIOTECA PANDAS
x=range(5)
x=np.array(x) # temos que converter para um array numpy, 
senão o plot não consegue fazer operações.
fig=plt.subplots(figsize=(12, 5)) # Cria figura sem eixo
plt.subplot(121) # Adiciona um grid de subplots a figura: 1 
linha, 2 colunas - Figura 1           
plt.plot(x, x, label='eq_1')
plt.plot(x, x**2, label='eq_2')
plt.plot(x, x**3, label='eq_3')
plt.title("Gráfico 1")
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.legend()
plt.subplot(122) # Adiciona um grid de subplots a figura: 1 
linha, 2 colunas - Figura 2            
plt.plot(x, x, 'r--', label='eq_1')
plt.plot(x**2, x, 'b--', label='eq_2')
plt.plot(x**3, x, 'g--', label='eq_3')
plt.title("Gráfico 2")
plt.xlabel('Novo eixo x')
plt.ylabel('Novo eixo y')
plt.legend()
Naturalmente obtivemos o mesmo resultado anterior, pois criamos a mesma
estrutura com uma sintaxe diferente. Ao optar em utilizar eixos como variáveis ou
não, o desenvolvedor deve �car atento somente as regras de sintaxe e as funções
disponíveis para cada opção. Podemos então resumir que:
• plt.subplots() é usado para criar um layout de �gura e subplots. (https://matp
lotlib.org/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplo
ts).
• plt.subplot() é usado para adiconar um subplot em um �gura existente. (http
s://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplo
t.subplot).
Que tal treinar e explorar utilizando o simulador a seguir. Veja os exemplos que a
própria ferramenta utiliza em sua página principal.
As principais estruturas de dados da biblioteca pandas (Series e DataFrame)
<matplotlib.legend.Legend at 0x1cf32b44c50>
Out[4]:
0Ver anotações
npf_ldkls202_u4s3_lin_pro https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...
7 of 17 14/12/2021 07:51

## Página 8

importpandas as pd
dados={
'turma':['A', 'B', 'C'],
'qtde_alunos':[33, 50, 45]
}
df=pd.DataFrame(dados)
df
df.plot(x='turma', y='qtde_alunos', kind='bar')
df.plot(x='turma', y='qtde_alunos', kind='barh')
possuem o método plot(), construído com base no matplotlib e que permite criar
grá�cos a partir dos dados nas estruturas. Vamos começar criando um DataFrame
a partir de um dicionário, com a quantidade de alunos em três turmas distintas.
In [5]:
A partir de um DataFrame, podemos invocar o método: df.plot(*args,
**kwargs) para criar os grá�cos. Os argumentos dessa função, podem variar, mas
existem três que são triviais: os nomes das colunas com os dados para os eixos x e
y, bem como o tipo de grá�co (kind). Veja o código a seguir, os valores da coluna
'turma' serão usados no eixo x, da coluna 'qtde_alunos' no eixo y e o tipo de grá�co
será o de barras (bar). Nas entradas 7 e 8, repetimos a mesma construção,
entretanto mudando o tipo de grá�co para barra na horizontal (barh) e linha (line).
In [6]:
In [7]:
turma qtde_alunos
0A 33
1B 50
2C 45
Out[5]:
<matplotlib.axes._subplots.AxesSubplot at 0x1cf339fe7b8>
Out[6]:
0Ver anotações
npf_ldkls202_u4s3_lin_pro https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...
8 of 17 14/12/2021 07:51

## Página 9

df.plot(x='turma', y='qtde_alunos', kind='line')
df.set_index('turma').plot(y='qtde_alunos', kind='pie')
In [8]:
No endereço https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.
DataFrame.plot.html você pode encontrar a lista com todos os tipos de grá�cos
possíveis de serem construídos com o método plot() da biblioteca. Para construir
um grá�co do tipo pizza (pie), precisamos de�nir como indíce os dados que serão
usados como legenda. Veja a seguir, fazemos a transformação no DF seguido do
plot com o tipo pie. Esse tipo de sintaxe é chamado de encadeamento, pois ao
invés de fazermos a transformação, salvar em um novo objeto e depois plotar,
fazemos tudo em uma única linha, sem precisar criar o novo objeto.
In [9]:
Vale ressaltar que para todos os grá�cos criados, a biblioteca oferece uma segunda
opção de sintaxe, que é invocar o tipo de grá�co como método, por exemplo:
<matplotlib.axes._subplots.AxesSubplot at 0x1cf32bd2470>
Out[7]:
<matplotlib.axes._subplots.AxesSubplot at 0x1cf33aeb668>
Out[8]:
<matplotlib.axes._subplots.AxesSubplot at 0x1cf33b7fda0>
Out[9]:
0Ver anotações
npf_ldkls202_u4s3_lin_pro https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...
9 of 17 14/12/2021 07:51

## Página 10

EXEMPLIFICANDO
Vamos utilizar os dados sobre a exportação de etanol hidratado (barris
equivalentes de petróleo) 2012-2020, disponível no endereço: https://www.
anp.gov.br/arquivos/dadosabertos/iee/exportacao-etanol-hidratado-2012-2
020-bep.csv, para analisarmos e extrairmos informações de forma visual.
Para conseguir utilizar o método plot nessa base, teremos que transformar
a vírgula em ponto (padrão numérico) e converter os dados para os tipos
�oat e int. Veja o código a seguir em que preparamos os dados
df_etanol=pd.read_csv('exportacao-etanol-hidratado-
2012-2020-bep.csv', sep=';', encoding="ISO-8859-1")
# Apaga colunas que não usaremos
df_etanol.drop(columns=['PRODUTO', 'MOVIMENTO 
COMERCIAL', 'UNIDADE'], inplace=True)
# Substitui a vírgula por ponto em cada coluna
for mes in 'JAN FEV MAR ABR MAI JUN JUL AGO SET OUT NOV 
DEZ TOTAL'.split():
df_etanol[mes]=df_etanol[mes].str.replace(',',
'.')
# Converte os valores para float
df_etanol=df_etanol.astype(float)
# Converte o ano para inteiro
df_etanol['ANO']=df_etanol['ANO'].astype(int)
df_etanol.head(2)
Agora com os dados corretos podemos usar o método de plotagem para
que, de forma visual, possamos identi�car o ano que teve a menor e maior
arrecadação para o mês de janeiro. Veja o código a seguir. No eixo x, vamos
usar a informação de ano, e no y todos os valores da coluna 'JAN'; (kind) o
tipo do grá�co será de barras; (�gsize) a �gura terá um tamanho de 10
polegadas na horizontal por 5 na vertical; (rot) a legenda no eixo x não deve
ser rotacionada; (fontsize) o tamanho das fontes na �gura deve ser 12 pt;
• df.plot.bar(x='turma', y='qtde_alunos')
• df.plot.line(x='turma', y='qtde_alunos')
• df.set_index('turma').plot.pie(y='qtde_alunos')
In [10]:
ANO JAN FEV MAR ABR MAI JUN JUL AGO
02012 87231.41132 141513.5186 122157.33850 98004.42926 153286.6078 144373.6894 384743.6142 244861.0289
12013 673419.97670 387331.6487 96929.59201 54390.05046 115092.4820 387498.3792 339162.2100 354343.2858
Out[10]:
0Ver anotações
npf_ldkls202_u4s3_lin_pro https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...
10 of 17 14/12/2021 07:51

## Página 11

(legend) não queremos legenda nesse grá�co. Pelo grá�co, podemos
identi�car com facilidade que o ano que teve menor arrecadação nesse
mês, foi 2017 e o maior 2013. Também plotamos o mesmo grá�co, mas em
linhas, veja como é possível explicar os dados agora sobre outra
perspectiva: o comportamento da variação da arrecadação ao longo do
tempo.
df_etanol.plot(x='ANO',
y='JAN',
kind='bar',
figsize=(10, 5),
rot=0,
fontsize=12,
legend=False)
df_etanol.plot(x='ANO',
y='JAN',
kind='line',
figsize=(10, 5),
rot=0,
fontsize=12,
legend=False)
Queremos criar um grá�co, que nos possibilite comparar a arrecadação
entre os meses de janeiro e fevereiro. Veja no código a seguir. Estamos
selecionando três colunas do nosso DF e encadeando o método plot(),
agora passando como parâmetro somente o valor x, o tipo, o tamanho, a
In [11]:
<matplotlib.axes._subplots.AxesSubplot at 0x1cf34c166a0>
Out[11]:
0Ver anotações
npf_ldkls202_u4s3_lin_pro https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...
11 of 17 14/12/2021 07:51

## Página 12

rotação da legenda e o tamanho da fonte. Os valores para o eixo y, serão
usados das colunas. Com essa construção se torna possível avaliar,
visualmente, o desempenho nos meses. Veja que em determinados anos, a
discrepância entre eles é consideravel.
df_etanol[['ANO', 'JAN', 'FEV']].plot(x='ANO',
kind='bar', figsize=(10, 5), rot=0, fontsize=12)
BIBLIOTECA SEABORN
In [12]:
Seaborn é outra biblioteca Python, também baseada na matplotlib, que foi
desenvolvida especi�camente para criação de grá�cos. Seaborn pode ser instalado
via pip install: pip install seaborn, e para utilizar no projeto existe uma
convenção para sintaxe: import seaborn as sns. A biblioteca conta com um
repositório de datasets que podem ser usados para explorar as funcionalidades e
estão disponíveis no endereço: https://github.com/mwaskom/seaborn-data. Vamos
carregar os dados sobre gorjetas (tips) para nosso estudo. Veja no código a seguir,
utilizamos a função load_dataset(), cujo retorno é um DataFrame pandas, para
carregar a base de dados. A seguir imprimimos as informações básicas que foram
carregadas. Temos 244 linhas e 7 colunas, cujos dados são do tipo ponto �utuante,
categóricos e um inteiro.
In [13]:
<matplotlib.axes._subplots.AxesSubplot at 0x1cf34c708d0>
Out[12]:
0Ver anotações
npf_ldkls202_u4s3_lin_pro https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...
12 of 17 14/12/2021 07:51

## Página 13

importseaborn as sns
# Configurando o visual do gráfico. Leia mais em 
https://seaborn.pydata.org/generated
/seaborn.set.html#seaborn.set
sns.set(style="whitegrid") # opções: darkgrid, whitegrid, 
dark, white, ticks
df_tips=sns.load_dataset('tips')
print(df_tips.info())
df_tips.head()
FUNÇÃO BARPLOT()
Dentro do grupo de funções para grá�cos de variáveis categóricas, temos o
barplot(), que permite criar grá�cos de barras, mas por que usaríamos essa função
e não a da biblioteca pandas? A resposta está nas opções de parâmetros que cada
biblioteca suporta. Veja o construtor da função barplot: seaborn.barplot(x=None,
y=None, hue=None, data=None, order=None, hue_order=None,
estimator=function mean, ci=95, n_boot=1000, units=None, seed=None,
orient=None, color=None, palette=None, saturation=0.75, errcolor='.26',
errwidth=None, capsize=None, dodge=True, ax=None, **kwargs). Esse construtor
possui uma série de parâmetros estatísticos, que dão muita �exibilidade e poder
aos cientista de dados, vamos falar sobre o parâmetro "estimator", que por default
é a função média. Isso signi�ca que cada barra do grá�co, exibirá a média dos
valores de uma determinada coluna, o que pode não fazer sentido, uma vez que
queremos exibir a quantidade dos valores (len) ou a soma (sum).
Para entender como esse parâmetro pode "afetar" a construção do grá�co, veja o
código a seguir. Usamos o matplotlib para construir uma �gura e um eixo com três
O tipo de dados que uma coluna possui é muito importante para a biblioteca
seborn, uma vez que as funções usadas para construir os grá�cos são dividas em
grupos: relacional, categóricos, distribuição, regressão, matriz e grids (https://seab
orn.pydata.org/api.html).
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 244 entries, 0 to 243
Data columns (total 7 columns):
total_bill    244 non-null float64
tip           244 non-null float64
sex           244 non-null category
smoker        244 non-null category
day           244 non-null category
time          244 non-null category
size          244 non-null int64
dtypes: category(4), float64(2), int64(1)
memory usage: 7.2 KB
None
total_bill tip sex smoker day time size
016.99 1.01 Female No Sun Dinner 2
110.34 1.66 Male No Sun Dinner 3
221.01 3.50 Male No Sun Dinner 3
323.68 3.31 Male No Sun Dinner 2
424.59 3.61 Female No Sun Dinner 4
Out[13]:
0Ver anotações
npf_ldkls202_u4s3_lin_pro https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...
13 of 17 14/12/2021 07:51

## Página 14

posições. Nosso primeiro grá�co de barras (linha 3), utiliza o estimator padrão, que
sabemos que é a média. O segundo (linha 4), utiliza a função de soma como
estimator e o terceiro (linha 5), a função len, para contar. Veja no resultado como
os grá�cos são diferentes. No primeiro, nos conta que a o valor médio da conta
entre homens e mulheres é próximo, embora os homens gastem um pouco mais.
Já o segundo grá�co, nos mostra que os homens gastam "muito mais", será que é
verdade? A soma da conta dos homens, de fato é superior a das mulheres, mas
será que não existem muito mais homens do que mulheres na base? O terceiro
grá�co nos conta isso, quantos homens e mulheres possuem na base.
fig, ax=plt.subplots(1, 3, figsize=(15, 5))
sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[0])
sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[1],
estimator=sum)
sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[2],
estimator=len)
Construir grá�cos não é somente plotar imagens bonitas, existem muitos conceitos
estatísticos envolvidos e a biblioteca seaborn fornece mecanismos para que essas
informações estejam presentes nos resultados visuais.
A biblioteca seaborn integra totalmente com a matplotlib. Vamos criar um grá�co
que nos mostre o valor médio diário de venda. Veja o código a seguir, a criação do
grá�co está na linha 3, mas con�guramos seu tamanho na linha 1, e das linhas 5 a
8, con�guramos os rótulos e os tamanhos.
plt.figure(figsize=(10, 5))
ax=sns.barplot(x="day", y="total_bill", data=df_tips)
ax.axes.set_title("Venda média diária", fontsize=14)
ax.set_xlabel("Dia", fontsize=14)
ax.set_ylabel("Venda média ", fontsize=14)
ax.tick_params(labelsize=14)
In [14]:
In [15]:
<matplotlib.axes._subplots.AxesSubplot at 0x1cf35b313c8>
Out[14]:
0Ver anotações
npf_ldkls202_u4s3_lin_pro https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...
14 of 17 14/12/2021 07:51

## Página 15

FUNÇÃO COUNTPLOT()
Conseguimos plotar a contagem de uma variável categórica, com a função barplot
e o estimator len, entretanto, a biblioteca seaborn possui uma função especí�ca
para esse tipo de grá�co: seaborn.countplot(x=None, y=None, hue=None,
data=None, order=None, hue_order=None, orient=None, color=None,
palette=None, saturation=0.75, dodge=True, ax=None, **kwargs).
Esse método não aceita que sejam passados valores de x e y ao mesmo tempo,
pois a contagem será feita sobre uma variável categórica, portanto devemos
especi�car x ou y, a diferença será na orientação do grá�co. Se informamos x,
teremos uma grá�co na vertical, se y, na horizontal.
plt.figure(figsize=(10, 5))
sns.countplot(data=df_tips, x="day")
Vamos plotar mais um grá�co de contagem para mostrar o poder de um único
parâmetro. O parâmetro hue é usado como entrada de dados, pois irá discriminar
no grá�co a variável atribuída ao parâmetro. Para entendermos, vamos plotar a
quantidade de pessoas por dia, mas discriminado por genêro, quantos homens e
mulheres estiveram presentes em cada dia? Veja no código a seguir, a única
In [16]:
<matplotlib.axes._subplots.AxesSubplot at 0x1cf35ad2e80>
Out[16]:
0Ver anotações
npf_ldkls202_u4s3_lin_pro https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...
15 of 17 14/12/2021 07:51

## Página 16

diferença é o parâmetro.
plt.figure(figsize=(10, 5))
sns.countplot(data=df_tips, x="day", hue="sex")
FUNÇÃO SCARTTERPLOT()
Os grá�cos do grupo relacional, permitem avaliar, de forma visual a relação entre
duas variáveis: x, y. A função possui a seguinte sintaxe:
seaborn.scatterplot(x=None, y=None, hue=None, style=None, size=None,
data=None, palette=None, hue_order=None, hue_norm=None, sizes=None,
size_order=None, size_norm=None, markers=True, style_order=None,
x_bins=None, y_bins=None, units=None, estimator=None, ci=95, n_boot=1000,
alpha='auto', x_jitter=None, y_jitter=None, legend='brief', ax=None,
**kwargs).
Vamos construir um grá�co que permita avaliar se existe uma relação entre o valor
da conta e da gorjeta. Será que quem gastou mais também deu mais gorjeta? Veja
o código a seguir, invocamos a função passando o valor da conta como parâmetro
para x e a gorjeta para y. Agora vamos avaliar o resultado. Cada "bolinha"
representa uma conta paga e uma gorjeta, por exemplo, a bolinha mais a direita,
podemos interpretar que para uma conta de aproximadamente 50 e poucos
doláres foi dada uma gorjeta de 10. Olhando para o grá�co, parece quanto maior o
valor da conta, maior foi o valor da gorjeta. Esse comportamento é chamado de
relação linear, pois conseguimos traçar uma reta entre os pontos, descrevendo seu
comportamento através de uma função linear.
plt.figure(figsize=(10, 5))
sns.scatterplot(data=df_tips, x="total_bill", y="tip")
In [17]:
In [18]:
<matplotlib.axes._subplots.AxesSubplot at 0x1cf35ba9240>
Out[17]:
0Ver anotações
npf_ldkls202_u4s3_lin_pro https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...
16 of 17 14/12/2021 07:51

## Página 17

O grá�co scatterplot é muito utilizado por cientistas de dados que estão buscando
por padrões nos dados. O padrão observado no grá�co, que mostra a relação
entre o valor da conta e da gorjeta, pode ser um forte indício que, caso o cientista
precise escolher um algoritmo de aprendizado de máquina para prever a
quantidade de gorjeta que um cliente dará, ele poderá uma regressão linear.
O universo dos dados é cada vez mais requisitado nas empresas, se você gostou
do que aprendemos, não deixe de investir mais tempo em estudo e treinamento,
pois há muito o que se aprender!
REFERÊNCIAS E LINKS ÚTEIS
IPython Development Team. Built-in magic commands. Disponível em: https://ipyth
on.readthedocs.io/en/stable/interactive/magics.html. Acesso em: 17 jun. 2020.
Matplotlib development team. matplotlib.pyplot. Disponível em: (https://matplotlib.
org/api/_as_gen/matplotlib.pyplot.html) Acesso em: 27 jun. 2020.
Michael Waskom. seaborn. Disponível em: (https://seaborn.pydata.org/api.html)
Acesso em: 27 jun. 2020.
Pandas Team. pandas.DataFrame.plot. Disponível em: https://pandas.pydata.org/p
andas-docs/stable/reference/api/pandas.DataFrame.plot.html. Acesso em: 27 jun.
2020.
Secretaria de Tecnologia da Informação, Ministério do Planejamento,
Desenvolvimento e Gestão. Conjuntos de dados. Disponível em: https://www.dado
s.gov.br/dataset. Acesso em: 27 jun. 2020.
<matplotlib.axes._subplots.AxesSubplot at 0x1cf35c7e908>
Out[18]:
0Ver anotações
npf_ldkls202_u4s3_lin_pro https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...
17 of 17 14/12/2021 07:51