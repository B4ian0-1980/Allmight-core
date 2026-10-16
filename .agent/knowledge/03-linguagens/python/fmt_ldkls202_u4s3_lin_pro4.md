---json
{
  "id": "fmt_ldkls202_u4s3_lin_pro4",
  "title": "Fmt Ldkls202 U4S3 Lin Pro4",
  "categoria": "03-linguagens",
  "subcategoria": "python",
  "resumo": "Guia tecnico e referencias sobre Fmt Ldkls202 U4S3 Lin Pro4.",
  "gatilhos": [
    "fmt",
    "ldkls202",
    "lin",
    "linguagens",
    "pro4",
    "python",
    "u4s3"
  ],
  "perguntas_tipo": [
    "Como utilizar Fmt Ldkls202 U4S3 Lin Pro4?",
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

FOCO NO MERCADO DE TRABALHO

## VISUALIZAÇÃO DE DADOS EM PYTHON

Vanessa Cadan Scheer

DESAFIO

ANÁLISE E APRESENTAÇÃO DE DADOS

As bibliotecas pandas, matplotlib e seaborn podem ser utilizadas para o carregamento dos
dados e a geração dos grácos.

Fonte: Shutterstock.

Deseja ouvir este material?

Áudio disponível no material digital.

Como desenvolvedor em uma empresa de consultoria de software, você foi

alocado em um projeto para uma empresa de telecomunicações. Essa empresa

tem interesse em habilitar um novo serviço, mas antes precisa entender qual a

disponibilidade dos satélites autorizados a operar no Brasil. Para a primeira sprint

(período de 15 dias de trabalho), você foi encarregado de apresentar, uma análise

preliminar da situação dos satélites.

Nessa primeira entrega, você deve apresentar a comparação da quantidade de

satélites que são brasileiros, dos que são estrangeiros. Dentre os satélites

Imprimir

0
Ver anotações

fmt_ldkls202_u4s3_lin_pro
https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...

1 of 7
14/12/2021 07:51


--------------------------------------------------

RESOLUÇÃO

brasileiros, você deve discriminar a quantidade de cada operadora comercial, bem

como a quantidade de satélites operando em cada banda. As mesmas análises

devem ser feitas para os satélites que pertencem a outros países.

Onde esses dados podem ser encontrados? Qual a melhor forma de apresentar os

resultados, basta levar os números? Qual biblioteca pode ser usada para resolver o

desao?

Um dos grandes desaos nessa primeira entrega é encontrar uma fonte conável

de dados.

No endereço https://www.dados.gov.br/dataset, existe uma categoria especíca

para esse tipo de informação: Agência Nacional de Telecomunicações - Anatel.

Dentro dessa categoria encontramos um arquivo delimitado (csv) com a relação de

satélites autorizados a operar no Brasil: https://www.dados.gov.br/dataset/relacao-

de-satelites-geoestacionarios-autorizados-a-operar-no-brasil, basta clicar no

recurso e fazer download para a pasta do projeto.

Agora que identicamos uma fonte conável podemos usar as bibliotecas pandas,

matplotlib e seaborn para carregar os dados e gerar grácos que contemplem as

informações solicitadas.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Vamos carregar os dados em um DataFrame pandas, chamado df_satelites. Os

dados possuem como delimitador ";", logo é preciso informar ao método read_csv

esse parâmetro. Também é preciso garantir que linhas duplicadas sejam

removidas (linha 2) e para ter os índices variando de 0 até N, vamos resetar (linha

3).

Como resultado temos um DF com 68 linhas e 7 colunas.

In [19]:

In [20]:

0
Ver anotações

fmt_ldkls202_u4s3_lin_pro
https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...

2 of 7
14/12/2021 07:51


--------------------------------------------------

df_satelites** =**
pd**.**read_csv('satelites_operando_comercialmente.csv', sep**=**';') 
df_satelites**.**drop_duplicates(inplace**=True**)
df_satelites**.**reset_index(drop**=True**, inplace**=True**)

print(df_satelites**.**info())
df_satelites**.**head()

Agora vamos criar um gráco que faz a contagem e visualmente, faz a comparação

entre a quantidade de satélites brasileiros e estrangeiros. Podemos usar o

countplot(), passando como parâmetros o DF e a coluna 'Direito', como variável

categórica a ser contada. Também podemos usar os recursos da biblioteca

matplotlib para congurar o tamanho da gura e dos textos nos eixos.

*# Quantos satélites são brasileiros e quantos são estrangeiro?*

plt**.**figure(figsize**=**(5,3))
plt**.**tick_params(labelsize**=**12)
sns**.**countplot(data**=**df_satelites, x**=**'Direito')

Agora vamos extrair as informações sobre os satélites brasileiros. Para facilitar,

vamos criar um novo DataFrame aplicando um ltro. Veja na linha 13, que o DF

In [21]:

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 68 entries, 0 to 67
Data columns (total 7 columns):
Satelite operando      68 non-null object
Órbita                 68 non-null object
Bandas                 68 non-null object
Status do Satélite     68 non-null object
Pos. Orbital           68 non-null object
Direito                68 non-null object
Operadora Comercial    68 non-null object
dtypes: object(7)
memory usage: 3.8+ KB
None

Satelite
operando
Órbita
Bandas
Status do
Satélite
Pos.
Orbital
Direito
Operadora Comercial

0
EUTELSAT 65
West A

Satélite
Geoestacionário
(GEO)

C (AP30B), Ku (AP30B),
Ka
operação
comercial
65ºO
Brasileiro
EUTELSAT DO BRASIL LTDA

1
HISPASAT
74W-1

Satélite
Geoestacionário
(GEO)
Ku (AP30/30A)
operação
comercial
74ºO
Brasileiro
HISPAMAR SATELITES S.A.

2
AL YAH 3
Satélite
Geoestacionário
(GEO)
Ka
operação
comercial
20ºO
Brasileiro
YAH TELECOMUNICAÇÕES
LTDA

3
SGDC
Satélite
Geoestacionário
(GEO)
Ka
operação
comercial
75ºO
Brasileiro
TELECOMUNICACOES
BRASILEIRAS SA TELEBRAS

4
SES-14
Satélite
Geoestacionário
(GEO)

C (não planejada), Ku
(não planejada), Ka
operação
comercial
47,5ºO
Brasileiro
SES DTH DO BRASIL LTDA

Out[20]:

<matplotlib.axes._subplots.AxesSubplot at 0x1cf35cfdbe0>

Out[21]:

0
Ver anotações

fmt_ldkls202_u4s3_lin_pro
https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...

3 of 7
14/12/2021 07:51


--------------------------------------------------

df_satelites_brasileiros, será um ltro do DF df_satelites onde somente os

brasileiros estarão presentes. Agora, podemos usar o countplot no

df_satelites_brasileiros para contar quantos satélites cada operadora comercial no

Brasil possui (linha 8). Como o nome das operadoras é longo, vamos pedir para

exibir na vertical, por isso conguramos a rotação do "xticks" na linha 6. Na linha 7

conguramos o tamanho dos textos nos eixos.

*# quantos satétiles cada operadora brasileira possui operando?*

df_satelites_brasileiros** =**
df_satelites**.**loc[df_satelites['Direito']** ==** 'Brasileiro']

plt**.**figure(figsize**=**(15,5))
plt**.**xticks(rotation**=**90)
plt**.**tick_params(labelsize**=**12)
sns**.**countplot(data**=**df_satelites_brasileiros, x**=**'Operadora 
Comercial')

Para saber quantos satélites brasileiros estão operando em cada banda, vamos

usar o countplot, passando como parâmetro o df_satelites_brasileiros e a coluna

'Bandas'. Novamente foi necessário congurar o texto nos eixos.

*# Quantos satélites brasileiros estão operando em cada banda?*

plt**.**figure(figsize**=**(15,5))
plt**.**xticks(rotation**=**90)
plt**.**tick_params(labelsize**=**12)
sns**.**countplot(data**=**df_satelites_brasileiros, x**=**'Bandas')

In [22]:

In [23]:

<matplotlib.axes._subplots.AxesSubplot at 0x1cf36eb4e10>

Out[22]:

0
Ver anotações

fmt_ldkls202_u4s3_lin_pro
https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...

4 of 7
14/12/2021 07:51


--------------------------------------------------

Agora vamos repetir os mesmos processos para os satélites estrangeiros,

começando pela criação de um DataFrame que contenha somente as informações

sobre eles (linha 3). Esse primeiro gráco mostra quantos satélites cada operadora

estrangeira possui em operação.

*# Quantos satétiles cada operadora estrangeira possui *
*operando?*

df_satelites_estrangeiros** =**
df_satelites**.**loc[df_satelites['Direito']** ==** 'Estrangeiro']

plt**.**figure(figsize**=**(15,5))
plt**.**xticks(rotation**=**90)
plt**.**tick_params(labelsize**=**12)
sns**.**countplot(data**=**df_satelites_estrangeiros, x**=**'Operadora 
Comercial')

In [24]:

<matplotlib.axes._subplots.AxesSubplot at 0x1cf33aeb588>

Out[23]:

0
Ver anotações

fmt_ldkls202_u4s3_lin_pro
https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...

5 of 7
14/12/2021 07:51


--------------------------------------------------

Agora vamos plotar quantos satélites estrangeiros estão operando em cada banda.

*# Quantos satélites brasileiros estão operando em cada banda?*

plt**.**figure(figsize**=**(15,5))
plt**.**xticks(rotation**=**90)
plt**.**tick_params(labelsize**=**12)
sns**.**countplot(data**=**df_satelites_estrangeiros, x**=**'Bandas')

In [25]:

Com essas informações o cliente começará a ter argumentos para a escolha de

uma operadora e banda que deseja contratar. Que tal personalizar um pouco mais

o tamanho das legendas, criar títulos para os grácos?

<matplotlib.axes._subplots.AxesSubplot at 0x1cf36f5ab70>

Out[24]:

<matplotlib.axes._subplots.AxesSubplot at 0x1cf36f4da20>

Out[25]:

0
Ver anotações

fmt_ldkls202_u4s3_lin_pro
https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...

6 of 7
14/12/2021 07:51


--------------------------------------------------

DESAFIO DA INTERNET

Ganhar habilidade em programação exige estudo e treino (muito treino). Acesse o

endereço https://www.kaggle.com/datasets, faço seu cadastro e escolha uma base

de dados para treinar e desenvolver seu conhecimento sobre visualização de

dados.

0
Ver anotações

fmt_ldkls202_u4s3_lin_pro
https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...

7 of 7
14/12/2021 07:51

