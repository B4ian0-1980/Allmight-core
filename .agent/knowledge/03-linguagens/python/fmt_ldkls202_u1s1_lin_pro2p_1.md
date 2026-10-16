---json
{
  "id": "fmt_ldkls202_u1s1_lin_pro2p_1",
  "title": "fmt_ldkls202_u1s1_lin_pro2p",
  "categoria": "03-linguagens",
  "subcategoria": "python",
  "resumo": "**Arquivo Original:** `fmt_ldkls202_u1s1_lin_pro2p.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "fmt",
    "fmt_ldkls202_u1s1_lin_pro2p",
    "ldkls202",
    "lin",
    "linguagens",
    "pro2p",
    "python",
    "u1s1"
  ],
  "perguntas_tipo": [
    "Como utilizar fmt_ldkls202_u1s1_lin_pro2p?",
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

# fmt_ldkls202_u1s1_lin_pro2p

> **Arquivo Original:** `fmt_ldkls202_u1s1_lin_pro2p.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 1

FOCO NO MERCADO DE TRABALHO
A LINGUAGEM PYTHON
Vanessa Cadan Sche�er
DESAFIO
No mercado de trabalho, existem diversas empresas que construíram seu modelo
de negócio baseado na prestação de serviço especializado para outras empresas e
são chamadas de "consultorias". Dentre essas empresas de consultoria, há uma
grande procura pelas que desenvolvem software, assim a empresa contratante não
precisa ter uma área de desenvolvimento interna, ela contrata a consultoria e faz a
encomenda da solução que necessita.
Como seu primeiro trabalho de desenvolvedor em uma empresa de consultoria de
software, você foi designado para antender um cliente que fabrica peças
automotivas e criar um protótipo da solução que ele necessita. O cliente relata que
tem aumentado o número de peças e que gostaria de uma solução que fosse capaz
DESENVOLVENDO UM PROTÓTIPO
Implementando algoritmos em Python.
Fonte: Shutterstock.
Deseja ouvir este material?
Áudio disponível no material digital.
Imprimir
In [1]:
0Ver anotações
fmt_ldkls202_u1s1_lin_pro https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...
1 of 4 14/12/2021 07:52

## Página 2

de prever quantas peças serão vendidas em um determinado mês. Esse resultado é
importante para ele, uma vez que dependendo da quantidade, ele precisa contratar
mais funcionários, reforçar seu estoque e prever horas extras.
O cliente enviou para você o relatório de vendas dos últimos 6 meses (Figura 1.4).
Agora você precisa analisar o grá�co, pensar no algoritmo que, a partir das
informações no grá�co, seja capaz de prever quantas peças serão vendidas em um
determinado mês. Por exemplo, considerando o mês de janeiro como o primeiro
mês, ele vendeu x peças, em fevereiro (segundo mês) ele vendeu n peças, quantas
peças ele vai vender no mês 10, e no mês 11 e no mês 32? Por se tratar de um
protótipo, você deve utilizar somente as informações que lhe foram cedidas, não
precisa, nesse momento, analisar o comportamento de fatores externos, por
exemplo, comportamento da bolsa de valores, tendência de mercado, etc.
Figura 1.4 | Relatório de vendas
Fonte: elaborada pela autora.
Você precisa escolher qual ferramenta de trabalho irá adotar para criar o protótipo,
em seguida implementar o algoritmo que faça a previsão usando a linguagem de
programação Python.
RESOLUÇÃO
Foi lhe dada a missão de escolher uma ferramenta para desenvolver um protótipo
para o cliente que fabrica peças automotivas. Uma opção é usar o Colab, pois nessa
0Ver anotações
fmt_ldkls202_u1s1_lin_pro https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...
2 of 4 14/12/2021 07:52

## Página 3

ferramenta você consegue implementar seu algoritmo usando a linguagem Python.
Outra grande vantagem em utilizá-lo é o fato de ser on-line e não precisar de
instalação. Uma vez pronto o protótipo, você pode enviar o link, tanto para seu
gerente ver o resultado do seu trabalho, quanto para o cliente testar a solução.
Uma vez decidida a ferramenta, é hora de começar a pensar na solução. Tudo que
você tem de informação está em um grá�co, portanto é preciso interpretá-lo.
Vamos extrair as informações de venda do grá�co e escrever em forma de tabela
(Tabela 1.1).
Tabela 1.1 | Venda de peças
Mês Resultado Aumento
1 200 -
2 400 200
3 600 200
4 800 200
5 1000 200
6 1200 200
Fonte: elaborada pela autora.
Ao tabular os dados do grá�co, aparece um valor interessante na coluna que
mostra o aumento mês após mês. De acordo com as informações o aumento tem
sido constante.
Se o aumento é constante, podemos usar uma função do primeiro grau para prever
qual será o resultado em qualquer mês. A função será r = c * mes, onde, r é o
resultado que queremos, c é a constante de crescimento e mes é a variável de
entrada. Dessa forma, ao obter um mês qualquer (2, 4, 30, etc) podemos dizer qual
o resultado.
Vamos testar nossa fórmula:
• mes = 2; c = 200 -> r = 200 * 2 = 400 (Valor correto para o mês 2.
• mes = 3; c = 200 -> r = 200 * 3 = 600 (Valor correto para o mês 3.
• mes = 4; c = 200 -> r = 200 * 4 = 800 (Valor correto para o mês 4.
• mes = 5; c = 200 -> r = 200 * 5 = 1000 (Valor correto para o mês 5.
0Ver anotações
fmt_ldkls202_u1s1_lin_pro https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...
3 of 4 14/12/2021 07:52

## Página 4

Agora que já sabemos como resolver, vamos implementar usando a linguagem
c=200 # valor da constante
mes=input("Digite o mês que deseja saber o resultado: ") # Função para 
captura o mês que o cliente digitar
mes=int(mes) # Não esqueça de converter para numérico o valor captura 
pela função input()
r=c*mes # Equação do primeiro grau, também chamada função do primeiro 
grau ou de função linear.
print(f"A quantidade de peças para o mês {mes} será {r}") # Impressão do 
resultado usando string interpolada "f-strings" (PEP 498)
DESAFIO DA INTERNET
Que tal treinar um pouco mais de programação e conhecer novas fontes de
informações? Você, aluno, tem acesso à Biblioteca Virtual, um repositório de livros e
artigos que pode ser acessado no endereço: (http://biblioteca-virtual.com/).
Na página 47 (capítulo 2: Objetos e Comandos de Entrada e Saída em Python) da
obra: BANIN, S. L. Python 3 - conceitos e aplicações: uma abordagem didática. São
Paulo: Érica, 2018, você encontra o exercício proposto 1. Utilize o emulador a seguir,
para resolver o desa�o!
Utilize o emulador a seguir, para resolver o desa�o!

  Code 
Remix 

3
Python3
 Run  Share
Procurar…Nenhum arquivo selecionado.
  main.pyin�ammation-01.csv  
Digite o mês que deseja saber o resultado: 30
A quantidade de peças para o mês 30 será 6000
0Ver anotações
fmt_ldkls202_u1s1_lin_pro https://conteudo.colaboraread.com.br/202002/TRILHA_DE_CARREIRA/ANALI...
4 of 4 14/12/2021 07:52