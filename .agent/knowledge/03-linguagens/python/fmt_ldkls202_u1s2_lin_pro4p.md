---json
{
  "id": "fmt_ldkls202_u1s2_lin_pro4p",
  "title": "Fmt Ldkls202 U1S2 Lin Pro4P",
  "categoria": "03-linguagens",
  "subcategoria": "python",
  "resumo": "Guia tecnico e referencias sobre Fmt Ldkls202 U1S2 Lin Pro4P.",
  "gatilhos": [
    "fmt",
    "ldkls202",
    "lin",
    "linguagens",
    "pro4p",
    "python",
    "u1s2"
  ],
  "perguntas_tipo": [
    "Como utilizar Fmt Ldkls202 U1S2 Lin Pro4P?",
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

## ESTRUTURAS LÓGICAS, CONDICIONAIS E DE REPETIÇÃO EM
## PYTHON

Vanessa Cadan Scheer

### DESAFIO

Trabalhar em uma empresa de consultoria focada no desenvolvimento de software

é desaador, pois você pode atender difentes clientes e atuar em diferentes

projetos. Embora desaador, sem dúvida é uma experiência enriquecedora.

Dando continuidade ao seu trabalho na empresa de consultoria de software, o

cliente que fabrica peças automotivas requisitou uma nova funcionalidade para o

sistema: calcular o imposto de renda a ser deduzido do salário dos colaboradores.

O imposto de renda "Incide sobre a renda e os proventos de contribuintes

residentes no País ou residentes no exterior que recebam rendimentos de fontes

no Brasil. Apresenta alíquotas variáveis conforme a renda dos contribuintes, de

forma que os de menor renda não sejam alcançados pela tributação." (IRPF, 2020)

IMPLEMENTANDO UMA SOLUÇÃO

Desenvolvendo novas funcionalidades de sistema.

Fonte: Shutterstock.

Deseja ouvir este material?

Áudio disponível no material digital.

In [1]:
In [2]:

Imprimir

0
Ver anotações

fmt_ldkls202_u1s2_lin_pro
https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...

1 of 4
14/12/2021 07:53


--------------------------------------------------

Você foi designado para pesquisar a tabela de valores para o imposto de renda do

ano de 2020, pensar no algoritmo e implementar a primeira versão da solução.

Quando o cliente aprovar, a versão passará para o time de produção. Nessa

primeira versão, o programa deve solicitar o salário do colaborador e então,

informar qual o valor do imposto que será deduzido do salário.

Já sabe qual ferramenta vai utilizar para implementar a solução? Onde buscar as

informações conáveis sobre o imposto de renda? Como implementar a solução?

Faça um bom trabalho e mostre para seu gestor sua evolução!

### RESOLUÇÃO

Em seu novo projeto, você foi designado a implementar uma solução que envolve o

cálculo do imposto de renda, baseado nos dados do ano de 2020. O primeiro passo

é encontrar uma fonte conável de informação, que nesse caso é o portal da

Receita Federal. No endereço (http://receita.economia.gov.br/acesso-rapido

/tributos/irpf-imposto-de-renda-pessoa-sica) você encontra vários links a respeito

desse imposto, e no link (http://receita.economia.gov.br/acesso-rapido/tributos/irpf-

imposto-de-renda-pessoa-sica#calculo_mensal_IRPF) você tem acesso às tabelas

de incidência mensal desse imposto para cada ano. Como o ano solicitado foi 2020,

a útlima tabela disponível é a de 2015 (Tabela 1.2).

0
Ver anotações

fmt_ldkls202_u1s2_lin_pro
https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...

2 of 4
14/12/2021 07:53


--------------------------------------------------

Tabela 1.2 | Tabela de incidência mensal, ano 2015

Base de cálculo em reais
Alíquota (%)
Parcela a deduzir do IRPF em reais

Até 1.903,98
-
-

De 1.903,99 até 2.826,65
7,5
142,80

De 2.826,66 até 3.751,05
15
354,80

De 3.751,06 até 4.664,68
22,5
636,13

Acima de 4.664,68
27,5
869,36
salario** =** 0
salario** =** float(input("Digite o salário do colaborador: "))

if salario** <=** 1903.98:
print(f"O colaborador isento de imposto.")
elif salario** <=** 2826.65:
print(f"O colaborador deve pagar R$ 142,80 de imposto.")
elif salario** <=** 3751.05:
print(f"O colaborador deve pagar R$ 354,80 de imposto.")
elif salario** <=** 4664.68:
print(f"O colaborador deve pagar R$ 636,13 de imposto.")
else:
print(f"O colaborador deve pagar R$ 869,36 de imposto.")

Na solução apresentada, veja que na linha 1, criamos e inicializamos a variável

"salario", embora não seja obrigatório em Python é uma boa prática de

programação.

Veja como zemos o teste do valor, por que usamos somente um valor para testar?

Fizemos dessa forma, porque em uma estrutura condicional encadeada, quando a

primeira condição for satisfeita, as demais não são testadas. Por exemplo,

considerando um colaborada que ganha R$ 2 mil por mês, embora esse valor seja

menor que 3751,05 e 4664,68, a primeira condição que é satisfeita para o caso é a

da linha 6 "elif salario <= 2826.65", logo essa será executada e não as demais.

Que tal mostrar para seu gerente e cliente sua pró-atividade e, além de criar uma

solução que exibe o valor do desconto, também já seja impresso o valor do salário

com o desconto aplicado? Observe o código com essa nova feature!

Digite o salário do colaborador: 2000
O colaborador deve pagar R$ 142,80 de imposto.

0
Ver anotações

fmt_ldkls202_u1s2_lin_pro
https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...

3 of 4
14/12/2021 07:53


--------------------------------------------------

salario** =** 0
salario** =** float(input("Digite o salário do colaborador: "))

if salario** <=** 1903.98:
print(f"O colaborador isento de imposto.")
print(f"Salário a receber = {salario}")
elif salario** <=** 2826.65:
print(f"O colaborador deve pagar R$ 142,80 de imposto.")
print(f"Salário a receber = {salario** -** 142.80}")
elif salario** <=** 3751.05:
print(f"O colaborador deve pagar R$ 354,80 de imposto.")
print(f"Salário a receber = {salario** -** 354.80}")
elif salario** <=** 4664.68:
print(f"O colaborador deve pagar R$ 636,13 de imposto.")
print(f"Salário a receber = {salario** -** 636.13}")
else:
print(f"O colaborador deve pagar R$ 869,36 de imposto.")
print(f"Salário a receber = {salario** -** 869.36}")

### DESAFIO DA INTERNET

Que tal treinar um pouco mais de programação e conhecer novas fontes de

informações? Você, aluno, tem acesso à Biblioteca Virtual, um repositório de

livros e artigos que pode ser acessado no endereço: (http://biblioteca-

virtual.com/).

Na página 75 (capítulo 3) da obra: BANIN, S. L. Python 3 - conceitos e aplicações:

uma abordagem didática. São Paulo: Érica, 2018, você encontra o exercício 3 (uso

de condições mistas). Utilize o emulador a seguir, para resolver o desao.

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

Digite o salário do colaborador: 2000
O colaborador deve pagar R$ 142,80 de imposto.
Salário a receber = 1857.2

0
Ver anotações

fmt_ldkls202_u1s2_lin_pro
https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...

4 of 4
14/12/2021 07:53

