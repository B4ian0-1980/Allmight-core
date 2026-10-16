---json
{
  "id": "djangoframeworknapratica_1",
  "title": "djangoframeworknapratica",
  "categoria": "03-linguagens",
  "subcategoria": "python",
  "resumo": "**Arquivo Original:** `djangoframeworknapratica.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "djangoframeworknapratica",
    "linguagens",
    "python"
  ],
  "perguntas_tipo": [
    "Como utilizar djangoframeworknapratica?",
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

# djangoframeworknapratica

> **Arquivo Original:** `djangoframeworknapratica.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 1

Django Framework na prática

## Página 2

Home
Todo material aqui apresentado serve de guia para o desenvolvimento do curso Django 
framework na prática e pode ser utilizado como material complementar às aulas 
disponíveis na plataforma Udemy. Apesar disto, todo o material referente ao livro "Django 
framework na prática" é de uso aberto e pode ser utilizado no aprendizado livre sem a 
necessidade de qualquer pagamento, contribuição ou até mesmo compra do curso na 
plataforma mencionada.
O objetivo do curso é explorar as principais funcionalidades do framework Django por meio
da construção de uma dashboard para registro e administração de visitantes de um 
determinado condomínio. Vamos desenvolver um projeto real e aprender ao longo de seu 
desenvolvimento o que são as ferramentas que o framework nos dá e como utilizá-las. 
Seguindo o roteiro aqui apresentado, você vai poder iniciar a sua carreira como 
desenvolvedor web utilizando a linguagem Python e desenvolver aplicações seguras e 
escaláveis em tempo recorde.
Inicie no mundo do desenvolvimento fullstack utilizando a linguagem Python!
Conhecendo o processo
 
O projeto controle-visitantes tem o objetivo informatizar o processo de registro e 
administração de visitantes do condomínio Montanhas Azuis. 
Hoje o condomínio conta com um processo manual e por meio de cadernos que são 
utilizados para registrar as informações referentes aos visitantes e informatizar esse 
processo é importante para ganhar tempo no processo, melhorar a experiência de trabalho 
dos porteiros e ainda armazenar as informações de forma segura e conﬁável.
O projeto consiste em uma ou mais páginas web em que seja possível registrar visitantes e 
visualizar suas informações. Além disso, precisamos disponibilizar algumas 
funcionalidades que seguem os ﬂuxos executados pelo porteiro assim que um visitante 
chega à portaria e quando o mesmo deixa as dependências do condomínio.

## Página 3

Imagem com etapas do processo de registro de visitantes, onde temos quatro etapas: 
chegada na portaria, aguardando autorização, realizando visita e visita ﬁnalizada
Na imagem abaixo é possível visualizar o ﬂuxo executado pelos porteiros e suas etapas:
Principais funcionalidades
 
Registro de visitantes
O formulário de registro de visitantes deve abstrair a etapa 01 do processo, onde o visitante 
informa nome completo, CPF, data de nascimento, o número da casa que deseja visitar e 
ainda a placa do veículo, se estiver utilizando durante a visita. Além desta informações, o 
formulário salva o horário de chegada do visitante automaticamente.

## Página 4

Tela de registro de visitante com formulário para inserção das informações
Tela com lista de visitantes recentes
Listagem de visitantes
A listagem de visitantes exibe, por meio de uma tabela, os visitantes recentes classiﬁcados 
por horário de chegada, do mais recente para o mais antigo.


## Página 5

Captura de tela de widgets para resumo de informações de visitantes
Tela de informações de visitante
Widgets para resumo de informações
O widgets da página inicial da dashboard têm a função de exibir um resumo dos números 
referentes aos visitantes em cada status e ainda o número total de visitantes registrados 
no mês.
Visualização de informações de visitante
A partir da tabela que lista os visitantes recentes, é possível acessar a página que exibe as 
informações detalhadas de cada visitante. No exemplo abaixo um visitante com a visita já 
ﬁnalizada:


## Página 6

Tela de informações de visitante com botão para autorizar a entrada
Autorização de entrada
A tela de informações de vistante é importante pois a partir dela é possível utilizar as 
funcionalidades de autorização de entrada e ﬁnalização de visita.
Quando um visitante está aguardando autorização, o botão para autorizar a entrada ﬁca 
disponível na tela de informações deste visitante e, para autorizar a entrada, basta clicar no
botão para abrir o formulário que deve ser preenchido com o nome do morador que 
autorizou a entrada do visitante e conﬁrmar a ação.
No exemplo a seguir o visitante está aguardando autorização:
Assim como quando o porteiro anotava o nome do morador responsável por autorizar a 
entrada e o horário de contato com esse morador, a funcionalidade recebe o nome do 
morador através de um formulário e salva o horário de contato e autorização de forma 
automática ao concluir a ação.

## Página 7

Tela de informações de visitante ao fundo com alerta exibindo formulário de cadastro de 
morador responsável
Finalização de visita
Assim como conseguimos utilizar a funcionalidade para autorizar a entrada do visitante, 
podemos ﬁnalizar sua visita. A funcionalidade funciona de forma parecida, com a 
diferença que é necessário apenas conﬁrmar a ação, sem necessidade de informações 
adicionais.
Ao clicar no botão para ﬁnalizar uma visita, um alerta é exibido solicitando que o porteiro 
conﬁrme a ação.

## Página 8

Tela de informações de visitante com botão para ﬁnalizar visita
Ao conﬁrmar a ação clicando no botão "ﬁnalizar visita", o porteiro encerra o processo 
referente a este visitante e o horário em que a ação ocorreu é registrada.

## Página 9

Tela de informações de visitante ao fundo com alerta exibindo a conﬁrmação de que o 
usuário realmente deseja encerrar a visita
Os botões "autorizar entrada" e "ﬁnalizar visita" são exibidos somente quando é possível 
executar a ação para o visitante em questão. Caso contrário, como quando o visitante já 
deixou as dependências do condomínio, nenhum botão é exibido.
Tecnologias utilizadas
 
O projeto controle-visitantes utiliza as seguintes tecnologias e recursos de código aberto:
Django framework
Django widget tweaks
Start Bootstrap - SB Admin 2
 

## Página 10

Requisitos desejáveis
Para um bom aproveitamento de todo material e atividades aqui propostas, é desejável que
você tenha os seguintes conhecimentos:
Conhecimentos básicos da linguagem Python
Funções
Noções de Programação Orientada a Objetos
Classes
Instância de classe
Atributos
Métodos
Conhecimentos básicos em HTML, CSS e JS
Noções de Bootstrap
Sistema operacional baseado em Unix
Conhecimentos básicos em terminal

## Página 11

Tópicos do livro
Capítulo 01
Conhecendo o instrutor e sabendo mais sobre o curso
Sobre o instrutor
Sobre o curso
O que iremos construir?
A linguagem de programação Python
O que é Django Framework?
Instalando e conﬁgurando o ambiente para iniciar o projeto
Python 3.8
Virtualenv
Pip
Django framework
Capítulo 02
 
Iniciando seu primeiro projeto Django
Um pouco mais sobre o django-admin
Entendendo a estrutura do projeto
Criando nosso primeiro aplicativo Django
Escrevendo nosso "Hello World"
Capítulo 03
 
Escrevendo as models
Escrevendo a classe modelo
Escrevendo um manager personalizado
Alterando o modelo padrão nas conﬁgurações
Criando as tabelas do nosso banco de dados
Criando um super usuário

## Página 12

Conhecendo o Django Admin
Alterações necessárias nas conﬁgurações
Capítulo 04
 
Criando aplicativo para gerenciar porteiros
Escrevendo as models do nosso aplicativo de porteiros
Conhecendo o campo DateField
Conhecendo o campo OneToOneField
Registrando nossa aplicação no Admin do Django
Aplicando as alterações em nosso banco de dados
Criando porteiro através do Admin do Django
Capítulo 05
 
Conﬁgurando a aplicação para trabalhar com arquivos estáticos e templates HTML
Criando a pasta templates em nosso projeto
Criando a pasta static em nosso projeto
Criando views que renderizam templates
Conhecendo a função render
Entendendo as adaptações necessárias no template
Conhecendo a tag static
Alterando o caminho dos arquivos estáticos
Exibindo variáveis no template
Deﬁnindo nosso dicionário de contexto
Exibindo as informações nos templates
Capítulo 06
 
Criando o aplicativo para gerenciar visitantes
Escrevendo as models do nosso aplicativo de visitantes

## Página 13

Conhecendo o campo DateTimeField
Conhecendo o campo ForeignKey
Registrando nossa aplicação no Admin do Django
Aplicando as alterações em nosso banco de dados
Adicionando visitante utilizando o Django Admin
Listando visitantes na página inicial da dashboard
Buscando registros de visitantes no banco de dados
Listando registros de visitantes no template HTML
Capítulo 07
 
Criando tela para registro de novo visitante
Criando view para registrar visitante
Criando URL para mapear view
Adaptando nossos templates para trabalhar com a template engine do Django
Criando o template base
Adaptando template index
Adaptando template base
Adaptando template registrar_visitante
Capítulo 08
 
Trabalhando com formulários no Django
Criando formulário para registro de visitante
Renderizando nosso formulário automaticamente
Melhorando a exibição do nosso formulário
Estilizando nosso formulário com django-widget-tweaks
Como instalar
Importando no template
Utilizando o render_ﬁeld
 

## Página 14

Capítulo 09
Preparando view para receber requisição do tipo POST
Conhecendo o objeto request
Conhecendo um pouco mais dos formulários
Tratando problema com atributo nulo
Exibindo uma mensagem para o usuário ao cadastrar novo visitante
Conhecendo o Django messages
Alterando o template para exigir as mensagens
Tratando possíveis erros em nosso formulário
Deixando nossas mensagens de erro mais claras
Capítulo 10
 
Criando tela para exibir informações de visitante
Criando a view
Conhecendo o atalho get_model_or_404
Criando URL para acessar informações de visitante
Criando template para exibir informações de visitante
Criando métodos personalizados para exibir informações do Visitante
Criando método para exibir horário de saída
Criando métodos para exibir horário de autorização de entrada e morador 
responsável por autorizar a entrada
Criando método para exibir placa do veículo utilizado na visita
Utilizando métodos personalizados no template
Utilizando o Django para renderizar nossas URLs
Renderizando a URL para retornar à página inicial
Capítulo 11
 
Criando funcionalidade para autorização de entrada de visitante
Criando um status diferente para cada estágio da visita

## Página 15

Criando o arquivo de migrações
Efetuando as alterações no banco de dados
Criando formulário para atualizar atributos especíﬁcos do visitante
Alterando view para autorizar entrada de visitante
Alterando template para exibir modal com formulário
Atualizando os campos horario_autorizacao e status diretamente
Atualizando o status
Conhecendo o timezone do Django
Capítulo 12
 
Criando função para ﬁnalizar visita
Criando URL
Alterando template para exibir botão e modal para ﬁnalizar visita
Prevenindo erros e operações desnecessárias
Exibição condicional de botões para autorizar entrada e ﬁnalizar visita
Bloqueando o acesso à URL por métodos diferentes do POST
Capítulo 13
 
Implementando melhorias em nossos templates
Exibindo botão com função de "voltar" e "cancelar" em páginas de informações e 
registro de visitante
Melhorando a exibição do CPF do visitante
Conhecendo o f-strings do Python
Utilizando método para exibir status do visitante
Implementando melhorias na estrutura do nosso projeto
Capítulo 14
 
Criando aplicativos para administrar informações da dashboard

## Página 16

Migrando view "index" para aplicativo dashboard
Conhecendo o método ﬁlter das querysets
Filtrando nossos visitantes por status
Contando os resultados de uma queryset
Capítulo 15
 
Aprendendo a ﬁltrar nossos visitantes por data
Conhecendo o ﬁeld lookups da Queryset API
Filtrando apenas os registros do mês atual
Utilizando o timezone para descobrir o mês atual
Ordenando nossa lista de visitantes por horário de chegada
Capítulo 16
 
Bloqueando o acesso para usuários não autenticados nas nossas views
Conhecendo o decorator login_required
Alterando a URL padrão para login e redirecionamento após login
Utilizando o sistema de autenticação do Django para nos fornecer a view de login
Criando o template de login
Renderizando formulário de login
Adicionando mensagem de erro em formulário de login
Criando URL para logout
Criando template de logout
Inserindo link para logout em dashboard
Capítulo ﬁnal
 
Encerramento e agradecimentos

## Página 17

Proposta de desenvolvimento
O condomínio Montanhas Azuis é um conceituado empreendimento que oferece conforto, 
qualidade e segurança para seus moradores. O condomínio nos procurou com o intuito de 
melhorar a experiência de trabalho de seus porteiros e tornar informatizado o processo de 
registro e administração de visitantes, de modo que os porteiros tenham acesso a uma 
página web e essas informações possam ser acessadas de qualquer lugar. Além do mais, 
desta forma, é possível garantir a segurança e a conﬁabilidade dos registros.
Entendendo o processo
 
Quando um visitante chega à portaria do condomínio, o mesmo deve informar alguns 
dados pessoais para que o porteiro anote estas informações no caderno de visitantes. 
Feito isso, o porteiro deve comunicar um morador que esteja na casa no momento e que 
possa autorizar a entrada deste visitante. Com a autorização concedida, o porteiro deve 
anotar o nome do morador e o horário em que a autorização ocorreu. Somente após esta 
etapa que o visitante pode adentrar ao condomínio e iniciar sua visita. Ao ﬁnal da visita, o 
porteiro deve registrar o horário em que o visitante saiu das dependências do condomínio e 
ainda escrever seu nome para registrar que ele é o responsável pelo registro.
Todo esse processo, atualmente, ocorre de forma manual e através de um caderno que é 
destinado ao registro de visitantes. Devido a isso, o processo acaba levando mais tempo 
que deveria e as informações podem ter sua conﬁabilidade questionada e segurança 
ameaçada, pois problemas podem acontecer com o caderno ou as folhas deste caderno e 
até mesmo rasuras podem acontecer e prejudicar as informações ali contidas. Além dos 
pontos levantados, com um sistema web podemos automatizar algumas funções para 
poupar tempo e reduzir as informações que devem ser preenchidas pelo porteiro.
Ter um sistema web para registro e administração de visitantes é um projeto importante 
para o condomínio pois será um diferencial frente aos seus concorrentes e ainda vai 
melhorar bastante a experiência de trabalho dos porteiros que, com o sistema em 
funcionamento, terão menos informações para preencher e, consequentemente, menos 
tempo será perdido com as atividades relacionadas ao registro de visitantes.
 

## Página 18

Imagem com etapas do processo de registro de visitantes, onde temos quatro etapas: 
Levantamento de requisitos
Com todo esse cenário em mente, precisamos desenvolver uma página web que seja 
acessível por meio das credenciais e-mail e senha e que possibilite o registro dos 
visitantes, conforme é feito atualmente no caderno. Para cadastrar um visitante é 
necessário informar seu nome completo, CPF, data de nascimento, o número da casa a 
ser visitada, a placa do veículo do visitante, se houver, e ainda o horário em que o 
visitante se apresentou à portaria.
Após o registro, o porteiro deve entrar em contato com um morador que esteja na casa no 
momento e informar à respeito da visita para que o morador autorize a entrada do 
visitante. Com a autorização concedida, o porteiro deve colocar no caderno o nome do 
morador que autorizou a entrada do visitante e o horário em que essa autorização 
ocorreu. Ao ﬁnal da visita, o horário em que o visitante deixou as dependências do 
condomínio deve ser registrado junto do nome do porteiro responsável pelo registro. O 
ﬂuxo e as etapas de todo o processo são as seguintes:


## Página 19

chegada na portaria, aguardando autorização, realizando visita e visita ﬁnalizada
A divisão do processo por etapas faz com que ﬁquem mais claras as atividades e a ordem 
em que elas devem ocorrer. Enxergando desta forma, podemos pensar em formas de dividir
o preenchimento das informações e a automatização de determinadas informações.
Para poupar tempo do porteiro, ao receber as primeiras informações para o registro, seria 
interessante que o horário de chegada fosse preenchido automaticamente pois, desta 
forma, o porteiro ﬁca preocupado somente em receber as informações pessoais do 
visitante, a casa a ser visitada e informar o placa do veículo, se houver.
Outro ponto interessante seria o registro automático do horário de autorização, assim que 
o porteiro informar o nome do morador responsável por autorizar a entrada do visitante. 
Essa informação pode ser preenchida num segundo momento, pois o visitante ﬁcará na 
recepção aguardando o contato do porteiro com um morador que autorize a sua entrada. 
Preenchendo o nome do morador, vamos atualizar essa informação junto do horário de 
autorização e a visita se inicia. Ao ﬁnal, claro, quando o visitante retorna à portaria para 
ﬁnalizar sua visita, devemos atualizar o horário de saída e inserir o nome do porteiro 
responsável pelo registro, tudo de forma automática.
Tudo isso deverá ocorrer em uma interface web onde seja possível visualizar os últimos 
visitantes registrados, ver informações detalhadas de cada visitante e ainda autorizar e 
ﬁnalizar suas visitas. Além destas informações, é desejável que o sistema web exiba um 
resumo das informações como número de visitantes aguardando autorização, número de 
visitantes no condomínio, número de visitas ﬁnalizadas e ainda o número de registros no 
mês.
Quais informações salvar
Nosso sistema deve estar preparado para armazenar uma série de informações, tanto dos 
porteiros, quanto dos visitantes. Essas informações são úteis para ﬁns de controle e 
segurança de todos os envolvidos e também para o setor responsável pelos recursos 
humanos do condomínio.
Com relação aos porteiros, é necessário armazenar as seguintes informações para 
registro:

## Página 20

E-mail (Utilizado na criação do usuário para acesso ao sistema)
Nome completo
CPF
Telefone
Data de nascimento
Com relação aos visitantes:
Nome completo
CPF
Data de nascimento
Casa a ser visitada
Placa do veículo utilizado, se houver
Além das informações acima, ainda precisamos registrar as seguintes informações
Horário de chegada na portaria
Nome do morador responsável por autorizar a entrada do visitante
Horário em que a autorização ocorreu
Horário em que o visitante deixou as dependências do condomínio
Porteiro responsável pelo registro

## Página 21

Capítulos

## Página 22

Capítulo 01
Conhecendo o instrutor e sabendo mais sobre o curso
Sobre o instrutor
Olá, meu nome é Thiago Brasil e na internet eu sou o @tchaguitos. Cursei Ciência da 
Computação e sou desenvolvedor web há aproximadamente 4 anos. Nesse tempo 
trabalhei principalmente com as linguagens Python e Javascript e me aventurei em vários 
projetos utilizando Django, NodeJS, ReactJS e mais algumas outras tecnologias da web. 
Além disso, trabalhei também com análise e visualização de dados geográﬁcos.
Se você quiser ver alguns dos meus códigos, dá uma passadinha aqui no meu Github
Sobre o curso
Com o curso "Django Framework na prática" você vai poder iniciar sua carreira como 
desenvolvedor web utilizando a linguagem Python e aprender a desenvolver aplicações 
web seguras e escaláveis numa velocidade incrível. O objetivo do curso é explorar as 
principais funcionalidades do framework por meio da construção de um projeto real e 
aprender ao longo de seu desenvolvimento o que são as ferramentas que o framework nos 
dá e como utilizá-las. 
Nesse curso a gente vai construir junto uma aplicação web do zero com Python que 
consiste num sistema de controle de visitantes para condomínio. A aplicação deverá ser 
capaz de possibilitar o registro e administração de visitantes e ainda contar com 
funcionalidades como visualização de informações de visitantes, autorização de entrada e 
ﬁnalização de visitas.
Depois desse curso você estará apto para desenvolver aplicações web robustas utilizando 
Django framework tendo visão ampla das boas práticas e principais funcionalidades que o 
framework nos permite utilizar.
O que iremos construir?

## Página 23

A partir da necessidade de informatizar o processo de registro de visitantes, um famoso 
condomínio entrou em contato conosco para desenvolver um sistema web que pudesse 
suprir essa demanda. Ao encontrar problemas na conﬁabilidade das informações e até 
mesmo para melhorar o ﬂuxo de trabalho dos porteiros, o condomínio resolveu buscar 
ajuda.
Nosso sistema web deverá ser capaz de possibilitar o registro de visitantes, exibir os 
últimos visitantes registrados, exibir informações detalhadas de cada visitante e ainda 
autorizar e ﬁnalizar suas visitas, registrando informações especíﬁcas para cada etapa do 
processo. É interessante lembrar que existem algumas regras que os porteiros seguem à 
risca para manter a segurança dos moradores e nosso sistema deverá obedecer a essas 
regras.
Além destas informações, nosso sistema web deverá exibir um resumo das informações 
como o número de visitantes aguardando autorização, o número de visitantes realizando 
visitas no condomínio, o número de visitas ﬁnalizadas e ainda o número de registros 
realizados no mês.
A linguagem de programação Python
 
Python é uma linguagem de programação de código aberto poderosa, amigável e bastante 
popular. Com ela é possível desenvolver sistemas web, trabalhar com análise de dados, 
inteligência artiﬁcial e machine learning, nomes muito falados ultimamente, além de 
desenvolver aplicativos móveis e aplicações para desktop.
A linguagem foi criada por Guido van Rossum em 1991 com o objetivo de ser uma 
linguagem produtiva e legível, de modo que fosse fácil para humanos trabalharem em seus
códigos, tornando menos custoso o processo de desenvolvimento e manutenção de 
sistemas.
Além da grande variedade de ferramentas que a própria linguagem disponibiliza, Python 
tem se tornado cada vez mais comum devido a sua utilização em áreas como Data 
Science, Machine Learning e Inteligência Artiﬁcial e, com isso, ganhado diversas 
bibliotecas e módulos que facilitam o dia a dia do desenvolvedor.

## Página 24

Por último e não menos importante: Python tem caminhado rumo ao status de linguagem 
de programação mais popular do mundo!
O que é Django Framework?
 
Django é um framework para construção de aplicações web escrito em Python gratuito e 
de código aberto. Um framework tem o objetivo de agrupar funcionalidades que são 
utilizadas com certa frequência na construção de aplicações exatamente com o intuito de 
economizar tempo dos desenvolvedores.
O Django, por sua vez, foi construído por desenvolvedores experientes e projetado pra 
resolver grande parte dos problemas existentes no desenvolvimento web. Sendo assim, a 
gente pode se concentrar em escrever a nossa aplicação sem a necessidade de ﬁcar 
reinventando a roda.
Dentre as empresas que utilizam o Django no mundo, temos exemplos grandes como 
Instagram, Pinterest e a Mozilla. Aqui no Brasil existem diversas empresas que utilizam 
como a Olist, a Magalu e o pessoal da Globo.com.
Instalando e conﬁgurando o ambiente para iniciar o projeto
 
Antes de começar a colocar a mão na massa, a gente precisa preparar o nosso ambiente 
de desenvolvimento. Esse nosso ambiente é bem simples e tem como dependência apenas 
quatro itens. São eles:
Python 3.8
Pip
Virtualenv
Django framework
Todos os comandos aqui utilizados são compatíveis com distribuições Linux 
baseadas em Ubuntu (Debian) e as aulas foram gravadas utilizando o Ubuntu 

## Página 25

20.04
Python 3.8
As versões mais recentes das distribuições linux baseadas no Ubuntu (Debian) já vêm com 
a versão 3.8.2 do Python instalada, mas se este não é o seu caso, basta seguir os 
comandos abaixo.
Antes de instalar o Python de fato, precisamos instalar alguns pacotes que vão nos ajudar 
com esta tarefa. Primeiro, vamos atualizar nossos pacotes e instalar algumas 
dependências:
$ sudo apt update1
$ sudo apt install software-properties-common2
Com isso feito, podemos agora adicionar o repositório PPA que será utilizado como fonte 
para instalarmos o Python3.8:
$ sudo add-apt-repository ppa:deadsnakes/ppa
O terminal vai pedir para que o você aperte enter  para conﬁrmar a ação. Faça isso para 
adicionar o repositório à sua lista e utilize os comandos abaixo para novamente atualizar 
os pacotes existentes e, ﬁnalmente, instalar a versão 3.8 do Python:
$ sudo apt update1
$ sudo apt install python3.82
Vamos utilizar esta versão pois é a versão mais recente e estável que temos da linguagem. 
O Django encoraja a utilização de versões mais recentes da linguagem e ainda oferece 

## Página 26

suporte oﬁcial sempre para as últimas versões disponíveis. Como utilizaremos a versão 3.0 
do Django, vamos já utilizar a versão 3.8.2 do Python lançada em 24 de fevereiro de 2020.
Virtualenv
Agora que temos a versão 3.8 do Python instalada, vamos instalar o Virtualenv para nos 
ajudar a organizar e isolar os ambientes de desenvolvimento dentro da nossa máquina. 
Com isso, a gente ganha a possibilidade de trabalhar em diversos projetos utilizando 
diferentes versões do Python e do Django na mesma máquina, sem correr o risco de que 
ocorram conﬂitos ou outros problemas relacionados a versão dos pacotes. Para instalar o 
Virtualenv vamos utilizar o seguinte comando:
$ sudo apt install virtualenv
Com o Virtualenv instalado, podemos criar um ambiente totalmente isolado para instalar 
as dependências relacionadas a cada projeto. Com o terminal aberto na pasta home , 
vamos criar um diretório chamado dev  para mantermos nossos projetos. Para criar e 
acessar o diretório, vamos utilizar os seguintes comandos:
$ cd1
$ mkdir dev2
$ cd dev3
Vamos utilizar o comando cd  para garantir que estamos na pasta home  do usuário 
logado em sua máquina e depois utilizamos o comando mkdir dev  para criar a pasta 
dev . Com o diretório dev  criado, vamos entrar nele utilizando o comando cd dev  e 
criar o diretório que dará nome ao nosso projeto. Para isso, vamos utilizar os seguintes 
comandos:
$ mkdir controle-visitantes1
$ cd controle-visitantes2

## Página 27

Feito isso, vamos criar o nosso ambiente virtual utilizando o Virtualenv. Ele cria para nós 
um diretório onde ﬁcam os pacotes instalados e utilizados dentro do nosso projeto. Vamos 
utilizar o comando:
$ virtualenv -p python3.8 env
O comando virtualenv  nos deixa passar alguns argumentos para deixar o 
ambiente mais próximo das nossas necessidades. Neste caso, estamos dizendo 
para ele qual a versão do Python queremos utilizar (Python 3.8 ) e o nome do 
nosso ambiente, que será env 
Após criarmos o ambiente, temos que ativá-lo. Esse passo deve ser executado sempre que 
você for começar a trabalhar no projeto, pois nossa máquina contém pacotes e versões 
diferentes das que estão em nosso ambiente virtual e, por isso, precisamos avisar para 
nosso terminal de onde ele deverá executar os pacotes e até mesmo o Python. Para ativar 
nosso ambiente, utilizaremos o comando:
$ source env/bin/activate
Após execução do comando e ativação do ambiente, você deverá visualizar em seu 
terminal algo como:
(env)$
Pip
O pip é um gerenciador de pacotes bastante utilizado no mundo Python e ele vem 
instalado sempre que criamos um novo ambiente virtual utilizando o virtualenv. Sendo 

## Página 28

assim, não vamos precisar instalá-lo, mas precisamos lembrar que só teremos a 
possibilidade de utilizar o comando pip  com o ambiente virtual ativado.
Django framework
Com o ambiente virtual ativado, vamos começar a instalar as dependências do projeto. Por 
enquanto temos apenas o Django Framework, que é quem vai nos ajudar e muito nessa 
jornada. Para instalá-lo, vamos utilizar o Pip, nosso gerenciador de pacotes do universo 
Python utilizando o comando pip . Bem tranquilo, não?
Para que a gente não tenha problemas referentes à versão utilizada, vamos especiﬁcar ao 
Pip qual versão do Django queremos instalar:
(env)$ pip install Django==3.0.0
Ao ﬁm de tudo e tendo sucesso em todas as instalações, temos o ambiente pronto para 
começar a desenvolver o projeto. 
Sendo assim, bora pro próximo capítulo!

## Página 29

Capítulo 02
Iniciando seu primeiro projeto Django
Antes de partimos para todas as atividades que envolvem o desenvolvimento da nossa 
dashboard, temos que iniciar nosso projeto, claro. Iniciar um projeto signiﬁca criar toda a 
estrutura básica necessária para garantir que o código que a gente vai escrever vai 
funcionar conforme esperado utilizando as tecnologias escolhidas. 
Felizmente, o Django já nos dá alguns scripts que servem para executar tarefas especíﬁcas 
do nosso projeto e, dentre elas, criar o esqueleto de um novo projeto com esse estrutura 
básica necessária. Ao ﬁm da execução do script, teremos algumas pastas e arquivos que 
poderão ser alterados conforme nossa necessidade.
Antes de executar os comandos necessários para iniciar projeto, vamos lembrar de ativar o 
ambiente virtual. Basta acessar a pasta do projeto (cd controle-visitantes ) e utilizar o 
comando source  passando caminho env/bin/activate :
$ cd controle-visitantes1
$ source env/bin/activate2
Após a ativação do ambiente, vamos criar um novo projeto utilizando o comando 
startproject  do django-admin :
(env)$ django-admin startproject controle_visitantes .
O comando startproject  pode receber, além do nome do projeto, o diretório em que o 
mesmo deverá ser iniciado (caso o diretório não seja informado, o Django criará um 
diretório de mesmo nome do projeto). Além disso, o Django permite apenas letras, números 
e o underline em nomes de projetos, por isso a pasta se chama controle-visitantes  e o 
projeto controle_visitantes . Com o comando acima estamos iniciando nosso projeto 

## Página 30

com nome controle_visitantes  na pasta em que estamos trabalhando, isto é, na pasta 
controle-visitantes  (note o ponto especiﬁcando o diretório atual).
Um pouco mais sobre o django-admin
O django-admin  é um pacote de comandos úteis para realização de tarefas 
administrativas dentro da aplicação e dispõe de comandos para criar um novo projeto, 
iniciar o servidor de desenvolvimento, veriﬁcar erros e muito mais. Em complemento ao 
django-admin , o arquivo manage.py  é criado.
O manage.py  funciona exatamente como o django-admin . Na verdade, eles são a 
mesma coisa, com a diferença que que o manage.py , por baixo dos panos, deﬁne um 
arquivo de conﬁgurações para ser utilizado pelo servidor de desenvolvimento. Em geral, o 
arquivo de conﬁgurações do nosso projeto.
Como o Django já possui um servidor de desenvolvimento integrado que nos possibilita 
rodar a aplicação localmente, vamos iniciá-lo e veriﬁcar se está tudo funcionando 
conforme esperado. Para isso, vamos utilizar o seguinte comando:
(env)$ python manage.py runserver
Por enquanto, vamos ignorar os avisos referentes às migrações de banco de 
dados. Em breve vamos entender melhor do que se trata.
Com o servidor de desenvolvimento rodando, vamos acessar o endereço 
http://127.0.0.1:8000/. Caso a tela abaixo apareça, signiﬁca que está tudo funcionando 
corretamente.

## Página 31

Tela de boas vindas do Django framework onde é exibido um foguete em direção ao céu e 
uma mensagem informando que a aplicação está funcionando
Entendendo a estrutura do projeto
 
Como vimos anteriormente, o django-admin  cria o esqueleto de um novo projeto e é isso 
que nós vamos entender agora: a estrutura que foi criada. Antes de tudo, vamos abrir a 
pasta do projeto em um editor de código. Eu vou utilizar o VS Code, mas ﬁque livre para 
escolher o seu favorito.
Com a pasta do projeto aberta no editor de código, vamos passar por cada um dos 
arquivos criados e entender o motivo pelo qual estão aí. A lista é a seguinte:
controle-visitantes/    1
    manage.py    2
    controle_visitantes/3
        asgi.py4
        __init__.py5
        settings.py6
        urls.py7
        wsgi.py8

## Página 32

O primeiro diretório nomeado controle-visitantes/  é apenas um container para 
armazenar os arquivos do nosso projeto. O nome desse diretório não é importante para
o Django e pode ser alterado a qualquer momento. 
 
O arquivo manage.py  é um utilitário de linha de comando que permite que a gente 
interaja com o projeto Django de diversas maneiras, conforme vimos anteriormente. 
 
O segundo diretório nomeado controle_visitantes/  é o diretório que agrupa o 
pacote Python referente ao nosso projeto. O nome do diretório é o nome do nosso 
pacote e ele é importante pois nos auxilia no processo de importação de arquivos e 
funções. Sendo assim, alterar o nome deste diretório nos trará sérios problemas. 
 
O arquivo controle_visitantes/__init__.py  é um arquivo vazio que diz ao Python 
que aquele diretório deve ser reconhecido e tratado como um pacote. 
 
O arquivo controle_visitantes/settings.py  é o arquivo de conﬁgurações do nosso 
projeto Django. Nele nós podemos detalhar como o projeto funciona e quais deﬁnições 
estão disponíveis. 
 
O arquivo controle_visitantes/urls.py  é o arquivo que declara as URLs do nosso 
projeto. Para que uma URL do nosso projeto seja acessível através do navegador, 
temos que declará-la neste arquivo. 
 
O arquivo controle_visitantes/wsgi.py  é um ponto de integração para servidores 
web que implementam o WSGI, um padrão Python que descreve como os servidores 
devem se comunicar com as aplicações web. 
 
Já o arquivo controle_visitantes/asgi.py  é o ponto de integração para servidores 
web utilizarem comunicação assíncrona
A partir da versão 3.0 o Django passou a dar suporte a alguns padrões de 
comunicação assíncrona
 

## Página 33

Criando nosso primeiro aplicativo Django
Agora que o ambiente de desenvolvimento está conﬁgurado, é hora da gente começar a 
colocar a mão na massa!
Conforme vimos, um projeto Django nada mais é que um pacote Python que deve seguir 
algumas convenções, como nomenclatura de arquivos e diretórios. O mesmo, obviamente, 
se estende para os aplicativos deste projeto. Sendo assim, devemos seguir uma estrutura 
básica dentro dos nossos aplicativos, que nada mais são que outros pacotes Python. A 
diferença básica entre eles é que um aplicativo deve executar uma tarefa em especíﬁco, 
como o gerenciamento de usuários do sistema, e um projeto é, na verdade, um conjunto de 
conﬁgurações e aplicativos que executam tarefas distintas. Um projeto pode ter vários 
aplicativos e um aplicativo pode estar presente em vários projetos.
Felizmente, podemos usar o nosso bom e velho amigo manage.py  para nos auxiliar nessa 
tarefa de criar toda a estrutura necessária para um novo aplicativo. Para criar nossos 
aplicativos podemos utilizar o comando startapp  passando o nome do aplicativo que 
deverá ser criado:
(env)$ python manage.py startapp usuarios
Após o comando ser executado, uma nova pasta, com o nome escolhido (usuarios), será 
criada dentro do projeto. Essa pasta terá a seguinte estrutura, que vamos entender melhor 
no decorrer das aulas:
usuarios/1
    __init__.py2
    admin.py3
    apps.py4
    migrations/5
        __init__.py6
    models.py7
    tests.py8
    views.py9

## Página 34

Todos os aplicativos do seu projeto Django terão essa mesma estrutura devido às 
convenções e padrões que falamos anteriormente. Esses padrões são legais pois nos 
ajudam a manter uma certa organização, o que nos facilita bastante em casos de 
manutenções e deixa nosso código mais previsível.
Antes de começarmos a trabalhar no código de um novo aplicativo, temos que registrá-lo 
nas conﬁgurações do nosso projeto para que o mesmo seja reconhecido. Caso esse passo 
não seja executado, o projeto não saberá que a pasta usuarios  é um aplicativo do 
projeto.
Vamos abrir o arquivo settings.py  no diretório principal do projeto e procurar pela 
variável INSTALLED_APPS . Essa variável guarda o nome dos aplicativos que são utilizados 
no projeto. Por padrão, o Django já começa utilizando alguns aplicativos do próprio 
framework, como admin , auth , sessions  e messages , cada um com uma ﬁnalidade 
especíﬁca.
INSTALLED_APPS = [1
    "django.contrib.admin",2
    "django.contrib.auth",3
    "django.contrib.contenttypes",4
    "django.contrib.sessions",5
    "django.contrib.messages",6
    "django.contrib.staticfiles",7
]8
Para registrar nosso aplicativo, basta colocarmos ele no ﬁnal dessa lista e o Django fará 
todo o resto. Para manter uma melhor organização, vamos separar os aplicativos do 
Django dos nossos aplicativos nessa conﬁguração. Para isso, basta inserir o código 
abaixo logo após a variável INSTALLED_APPS . 
INSTALLED_APPS += [1
    "usuarios",2
]3

## Página 35

Note que estamos utilizando um operador de atribuição diferente, sendo +=  ao invés de 
= . Esse operador faz com que o valor existente na variável seja mantido e a gente 
acrescente o valor à direita do operador. Isto é, estamos mantendo os aplicativos do 
Django e adicionando os nossos. O código que teremos será o seguinte:
INSTALLED_APPS = [1
    "django.contrib.admin",2
    "django.contrib.auth",3
    "django.contrib.contenttypes",4
    "django.contrib.sessions",5
    "django.contrib.messages",6
    "django.contrib.staticfiles",7
]8
9
INSTALLED_APPS += [10
    "usuarios",11
]12
Escrevendo nosso "Hello World"
 
O "Hello world" (ou "Olá mundo") é aquele famoso programa de computador que imprime 
na tela o texto "Hello world" e é sempre utilizado como exemplo minimalista de 
determinada linguagem ou framework. Não vamos deixar a tradição de lado e vamos 
implementar a nossa versão do programa em Django. A diferença é que, como estamos 
trabalhando na web, vamos exibir o texto no navegador, acessando a URL que vamos 
conﬁgurar. Mão na massa!
Vamos começar trabalhando no arquivo views.py  do nosso aplicativo usuarios . A 
camada view é responsável por encapsular a lógica que recebe e responde as requisições 
dos nossos usuários, podendo ou não deﬁnir comportamentos especíﬁcos e buscar 
informações no banco de dados, por exemplo. Toda view no Django é uma função de 
retorno vinculada a uma URL especíﬁca. Sendo assim, não existe uma URL sem uma 
função de view.
from django.shortcuts import render1

## Página 36

from django.http import HttpResponse2
3
def index(request):4
    return HttpResponse("Hello world")5
Essa é o exemplo mais básico de view que podemos escrever no Django. Ela apenas 
retorna um objeto do tipo HttpResponse  que nada mais é, neste caso, que um texto 
simples.
Com a nossa função de view pronta, temos agora que mapear ela para ser chamada junto 
à uma URL. Para isso, vamos alterar o arquivo urls.py  no diretório principal do nosso 
projeto. O arquivo terá um conteúdo parecido com o abaixo:
from django.urls import path1
from django.contrib import admin2
3
urlpatterns = [4
    path("admin/", admin.site.urls),5
]6
O primeiro passo será importar o arquivo de views do nosso aplicativo usuarios  e depois 
adicionar uma nova linha na lista urlpatterns . Vamos substituir o conteúdo do arquivo 
pelo seguinte código:
from django.urls import path1
from django.contrib import admin2
3
from usuarios.views import index4
5
urlpatterns = [6
    path("admin/", admin.site.urls),7
    8
    path(9
        "",10
        index,11
        name="index"12
    ),13
]14

## Página 37

A função path  recebe uma string que será a URL a ser acessada no navegador, uma 
função a ser executada e um nome para a URL ser identiﬁcada mais facilmente dentro do 
projeto. O nome da URL é bem útil para casos onde temos que renderizar o endereço 
completo da URL no template ou direcionar o usuário para uma página especíﬁca, por 
exemplo. Em breve vamos aprender mais sobre.
Feito isso, vamos utilizar o comando para iniciar nosso servidor de desenvolvimento e ver o
que aparece ao acessarmos o endereço através do navegador.
(env)$ python manage.py runserver
Feito isso e não havendo erros no terminal, você deverá acessar o endereço 
http://127.0.0.1:8000/  em seu navegador e visualizar nosso tão esperado "Hello 
world".

## Página 38

Capítulo 03
Escrevendo as models
Escrevendo a classe modelo
A camada model do nosso projeto, representada pelos arquivos models.py , nada mais é 
que uma representação exata do nosso banco de dados, sendo a classe uma tabela e seus 
atributos os campos dessa tabela. É nessa camada que guardamos as informações que 
serão disponibilizadas para outras camadas. Como o Django segue o princípio DRY - don't 
repeat yourself (algo tipo "não se repita"), o objetivo é deﬁnir o modelo de dados em um 
único lugar e automaticamente derivar informações e regras de negócio a partir dele.
O aplicativo usuarios  será responsável por gerenciar os usuários do sistema. Ou seja, 
como vamos salvar as credenciais, quais credenciais vamos utilizar e tudo mais. Nesse 
ponto, é importante dizer que o Django já fornece um modelo padrão para usuários do 
sistema muito bom e útil para diversos cenários, mas que não dispõe de um suporte 
amigável para customizações. Se a gente precisar utilizar um e-mail ao invés de um nome 
de usuário para acessar o sistema, encontraríamos problemas com o modelo fornecido por 
padrão. Sendo assim, vamos criar nosso modelo personalizado para que seja possível 
disponibilizar o acesso à dashboard via e-mail.
O próprio Django, em sua documentação, cita exemplos em que o modelo padrão não é o 
mais apropriado e recomenda alternativas para contornar o problema. Uma das 
alternativas é sobrescrever o modelo padrão por outro que será deﬁnido por nós. Para isso, 
começaremos alterando o arquivo models.py  dentro do diretório do nosso aplicativo de 
nome usuarios .
Ao abrir o arquivo, vamos apagar o conteúdo que foi colocado pelo Django e começar 
importando as classes BaseUserManager , AbstractUser  e PermissionsMixin . Estas 
classes vão nos auxiliar na tarefa de criar um novo modelo para usuários em nosso 
projeto.
from django.db import models1
from django.contrib.auth.models import (2

## Página 39

    BaseUserManager,3
    AbstractBaseUser,4
    PermissionsMixin,5
)6
Vamos começar criando nossa classe Usuario  como subclasse de AbstractBaseUser  e 
PermissionsMixin  e deﬁnir o atributo e-mail .
class Usuario(AbstractBaseUser, PermissionsMixin):1
2
    email = models.EmailField(3
        verbose_name="E-mail do usuário",4
        max_length=194,5
        unique=True,6
    )7
    8
Existem inúmeros tipos de campos que o Django traz por padrão, sendo eles 
classes contidas no pacote models do Django. O EmailField é apenas um deles 
e no decorrer do curso vamos conhecer mais deles.
Após deﬁnirmos o atributo email , vamos deﬁnir alguns outros que são obrigatórios para 
um modelo de usuário do Django, os campos is_active , is_staff  e is_superuser . 
Vamos aproveitar também para criar a variável USERNAME_FIELD  que é quem especiﬁca 
para o Django qual campo deve ser utilizado como nome de usuário que, no nosso caso, é 
o campo email .
class Usuario(AbstractBaseUser, PermissionsMixin):1
2
    email = models.EmailField(3
        verbose_name="E-mail do usuário",4
        max_length=254,5
        unique=True,6
    )7
    8

## Página 40

    is_active = models.BooleanField(9
        verbose_name="Usuario ativo?",10
        default=True11
    )12
        13
    is_staff = models.BooleanField(14
        verbose_name="Usuário é da equipe de desenvolvimento?",15
        default=False16
    )17
18
    is_superuser = models.BooleanField(19
        verbose_name="Usuário é um superusuário?"20
        default=False21
    )22
    23
    USERNAME_FIELD = "email"24
    25
    class Meta:26
        verbose_name = "Usuário"27
        verbose_name_plural = "Usuários"28
        db_table = "usuario"29
    30
    def __str__(self):31
        return self.email32
Após a deﬁnição destes campos e variáveis, vamos escrever uma classe interna à classe 
Usuario  chamada Meta . Essa classe é comum a todos os modelos e serve para que a 
gente informe ao Django metadados. Existem diversas opções de metadados que 
podemos explicitar mas, por hora, vamos nos concentrar no verbose_name , 
verbose_name_plural  e db_table.  Estas opções deixam claro para o Django como ele 
deve apelidar o model, qual o apelido no plural e o nome da tabela no banco de dados 
referente ao model criado.
Vamos escrever também o método __str__ . Esse método é obrigatório e chamado 
sempre que transformamos o objeto numa string para ﬁns de exibição. Um dos casos em 
que isso ocorre é quando o Django precisa exibir a instância no Django Admin (não se 
preocupe com esse nome agora, vamos conhecê-lo melhor em breve). Sendo assim, seu 
método __str__  deve sempre retornar um texto fácil e de rápida identiﬁcação para seres 
humanos. Feito isso, podemos partir para o segundo passo!
Escrevendo um manager personalizado

## Página 41

O segundo passo para substituirmos o modelo de usuários padrão do Django é criarmos 
uma subclasse de BaseUserManager  e sobrescrevermos os métodos create_user  e 
create_superuser . Estes métodos são responsáveis por criar usuários e super usuários 
em nosso sistema e devem ser sobrescritos para se adequarem às nossas necessidades. 
Devido ao fato de estarmos estabelecendo uma relação de herança entre UsuarioManager 
e BaseUserManager , não precisamos implementar todos os atributos e métodos, pois 
estas informações são repassadas à classe ﬁlho. 
Uma classe manager é uma interface que fornece informações sobre e como as queries 
devem ser executadas pela classe modelo quando houver interação com o banco de 
dados. Para cada classe modelo, existe pelo menos um manager.
Vamos escrever nossa classe manager em cima da classe Usuario :
class UsuarioManager(BaseUserManager):1
2
    def create_user(self, email, password=None):3
        usuario = self.model(4
            email=self.normalize_email(email),5
        )6
7
        usuario.is_active = True8
        usuario.is_staff = False9
        usuario.is_superuser = False10
11
        if password:12
            usuario.set_password(password)13
14
        usuario.save()15
16
        return usuario17
    18
    def create_superuser(self, email, password):19
        usuario = self.create_user(20
            email=self.normalize_email(email),21
            password=password,22
        )23
        24
        usuario.is_active = True25
        usuario.is_staff = True26
        usuario.is_superuser = True27
        28
        usuario.set_password(password)29
        usuario.save()30

## Página 42

        31
        return usuario32
33
class Usuario(models.Model):34
    # código abaixo omitido...35
Com a classe e métodos escritos, agora temos um manager com a função de criar 
usuários conforme a nossa necessidade. Com isso, nosso sistema está quase pronto para 
criar usuários, faltando apenas explicitar que a classe modelo deve utilizar este manager 
como padrão. Para isso, vamos adicionar um atributo na classe modelo com o nome do 
manager que queremos utilizar.
O Django utiliza o nome objects  para o manager padrão da classe, sendo assim, vamos 
apenas sobrescrever o manager padrão pelo que nós criamos. Vamos criar o atributo 
objects  na classe Usuario  atribuindo a ele a classe UsuarioManager .
class Usuario(AbstractBaseUser, PermissionsMixin):1
    email = models.EmailField(2
        verbose_name="E-mail do usuário",3
        max_length=254,4
        unique=True,5
    )6
    7
    is_active = models.BooleanField(8
        "usuario ativo?",9
        default=True10
    )11
        12
    is_staff = models.BooleanField(13
        "usuario é da equipe de desenvolvimento?",14
        default=False15
    )16
17
    is_superuser = models.BooleanField(18
        "usuario é um superusuário?",19
        default=False20
    )21
    22
    USERNAME_FIELD = "email"23
    24
    objects = UsuarioManager()25
    26
    class Meta:27

## Página 43

        verbose_name="Usuário"28
        verbose_name_plural = "Usuários"29
        db_table = "usuario"30
    31
    def __str__(self):32
        return self.email33
Alterando o modelo padrão nas conﬁgurações
Para dizermos ao Django que ele deve utilizar a nossa classe modelo ao invés do modelo 
padrão para usuários do sistema, temos que adicionar a variável AUTH_USER_MODEL  ao 
arquivo settings.py  e apontar para a classe a ser utilizada. 
AUTH_USER_MODEL = "usuarios.Usuario"
Ao escrevermos isso, estamos dizendo "hey, Django, use a classe Usuario do 
aplicativo usuarios como modelo de usuários do sistema".
Criando as tabelas do nosso banco de dados
Com o trecho de código que escrevemos o Django já é capaz de executar instruções para 
criação da tabela usuario  no nosso banco de dados e disponibilizar uma API de acesso 
aos objetos do tipo Usuario,  mas antes precisamos avisar ao Django a respeito destas 
alterações. Sempre que ocorrer alguma alteração nos modelos ou você criar um novo 
modelo, é necessário avisar ao Django para que ele cuide de toda a parte anterior à 
efetivação das mudanças no banco de dados.
Para isso, quando escrevemos uma classe modelo, temos que executar o comando 
makemigrations . Esse comando vai criar um arquivo de migração contendo todas as 
alterações que devem ser feitas no banco de dados, tais como criação de tabelas com 
determinados atributos, alteração nos atributos, dentre outros. Vamos executar o seguinte 
comando:

## Página 44

(env)$ python manage.py makemigrations usuarios
Ao executar o comando makemigrations , você está dizendo ao Django para armazenar 
as alterações realizadas em forma de migração. Uma migração nada mais é que um 
arquivo de texto contendo todos os passos que devem ser executados para efetivação das 
alterações no banco de dados. Aparecerá algo como isso na tela do terminal:
Migrations for 'usuarios':1
  usuarios/migrations/0001_initial.py2
    - Create model Usuario3
Existe também um comando para rodar as migrações e gerenciar o schema do banco de 
dados de forma automática. O comando migrate  é quem vai reunir todas as migrações 
que ainda não foram executadas e aplicar elas em seu banco de dados - isto é, vai 
sincronizar seu banco de dados com as informações que estão na classe modelo. Para 
efetuar as alterações em nosso banco de dados vamos executar o comando:
(env)$ python manage.py migrate
Migrações são um recurso poderoso pois nos permitem alterar as classes modelos ao 
longo do tempo sem a necessidade de manipular nosso banco de dados. O comando 
migrate  é especialista em atualizar nosso banco de dados em tempo real sem perder 
dados.
Operations to perform:1
  Apply all migrations: admin, auth, contenttypes, sessions, usuarios2
3
Running migrations:4
  Applying contenttypes.0001_initial... OK5
  Applying contenttypes.0002_remove_content_type_name... OK6
  Applying auth.0001_initial... OK7
  Applying auth.0002_alter_permission_name_max_length... OK8
  Applying auth.0003_alter_user_email_max_length... OK9

## Página 45

  Applying auth.0004_alter_user_username_opts... OK10
  Applying auth.0005_alter_user_last_login_null... OK11
  Applying auth.0006_require_contenttypes_0002... OK12
  Applying auth.0007_alter_validators_add_error_messages... OK13
  Applying auth.0008_alter_user_username_max_length... OK14
  Applying auth.0009_alter_user_last_name_max_length... OK15
  Applying auth.0010_alter_group_name_max_length... OK16
  Applying auth.0011_update_proxy_permissions... OK17
  Applying usuarios.0001_initial... OK18
  Applying admin.0001_initial... OK19
  Applying admin.0002_logentry_remove_auto_add... OK20
  Applying admin.0003_logentry_add_action_flag_choices... OK21
  Applying sessions.0001_initial... OK22
Não se assuste com as tantas letras que vão aparecer no terminal. Elas nos informam 
quais aplicativos tiveram operações executadas e quais arquivos de migração foram 
utilizados para a migração em questão.
Agora temos nosso modelo personalizado de usuários criado e ativado em nosso banco de 
dados e estamos prontos para criar usuários.
Criando um super usuário
 
A gente viu que o Django segue uma ﬁlosoﬁa que tenta aproveitar o máximo de coisas 
para evitar que a gente ﬁque repetindo código. Pensando nisso, os desenvolvedores do 
framework disponibilizam um painel administrativo com funções para adicionar, alterar e 
deletar conteúdo com base nas classes modelo do nosso projeto.
O Django foi desenvolvido em um ambiente de redação, onde havia uma clara separação 
entre “produtores de conteúdo” e o site “público”. Gerentes utilizavam o sistema para 
adicionar notícias, eventos, resultados de esportes, por exemplo, e o conteúdo era exibido 
no site público.
Como a administração do Django não foi desenvolvida para ser utilizada pelos visitantes 
do site, mas sim pelos gerentes, temos que criar um tipo diferente de usuário, que seria 
nosso "super usuário". Para isso basta utilizarmos o comando createsuperuser  do nosso 
bom e velho amigo manage.py :

## Página 46

Tela de um terminal Linux após a execução do comando createsuperuser do Django. O 
terminal espera que o usuário insira E-mail e Senha para criar um super usuário
(env)$ python manage.py createsuperuser
Ao executar o comando, o terminal ﬁcará travado esperando que a gente informe o e-mail a 
ser utilizado pelo super usuário. Após o e-mail, temos que deﬁnir a senha e repetir essa 
senha. Não ocorrendo erros, temos o nosso super usuário criado e pronto para acessar o 
painel administrativo do Django.
Vamos iniciar novamente nosso servidor de desenvolvimento e acessar o endereço 
http://127.0.0.1:8000/admin/  em nosso navegador e vamos nos deparar com a tela de 
login do Djando Admin.

## Página 47

Formulário de autenticação para acesso ao Django Admin. O formulário exibe os campos 
"E-mail do usuário" e "Senha", além de um botão para Log in
Tela inicial do Django Admin, onde é exibida as ações recentes do usuário, além de uma 
mensagem de boas vindas e links para alterar senha e sair do Admin
Utilize e-mail e senha informados na hora da criação do super usuário para acessar e, 
dando tudo certo, você será direcionado para a página inicial da administração do Django:
Conhecendo o Django Admin
 

## Página 48

Ao acessarmos o painel administrativo, é possível notar que o aplicativo usuários não está 
sendo exibido. Isso porque para que nossas classes modelo sejam identiﬁcadas pelo 
painel administrativo é necessário alterar o arquivo admin.py . Esse arquivo sempre 
existirá dentro de um aplicativo criado utilizando o manage.py  e é quem irá dizer ao 
Django que nossa classe deve ter uma interface de administração. 
Vamos abrir o arquivo usuarios/admin.py  e importar nossa classe Usuario :
from django.contrib import admin1
from usuarios.models import Usuario2
Após a importação, temos apenas que registrar a classe no admin. Para isso, basta utilizar 
o método admin.site.register  passando a classe Usuario  como argumento:
from django.contrib import admin1
from usuarios.models import Usuario2
3
admin.site.register(Usuario)4
Feito isso, vamos voltar ao painel administrativo do Django e podemos notar que agora 
existe uma seção referente ao aplicativo usuarios. O mais legal é que os nomes que 
deﬁnimos em verbose_name  e verbose_name_plural  são utilizados aqui, além do valor 
que deﬁnimos como retorno do método __str__ .
Alterações necessárias nas conﬁgurações
 
Nosso projeto já está rodando sem problemas e possui um modelo personalizado de 
usuários. Isso já é bem legal, mas ainda vamos realizar algumas alterações nas 
conﬁgurações para que ele se adeque ainda mais às nossas necessidades. Neste 
momento, vamos alterar conﬁgurações de fuso horário e idioma utilizado.

## Página 49

Tela inicial do Admin agora com o aplicativo Usuários sendo exibido
O Django possui integrado um módulo para internacionalização e localização. Esses 
módulos são interessantes pois permitem que a aplicação funcione em idiomas e 
formatos diferentes com base nas preferências do usuário. Um exemplo de funcionamento 
do módulo de internacionalização é o próprio painel administrativo do Django que 
funciona dessa maneira.  
Para alterar o idioma padrão utilizado no projeto, vamos no arquivo settings.py  e 
procurar pela variável LANGUAGE_CODE . Essa variável recebe uma string referente ao 
identiﬁcador do idioma e país de origem com base na especiﬁcação que deﬁne os 
formatos de idiomas para serem utilizados. Para nosso caso, utilizaremos a string pt-BR  
que faz com que o Django utilize português do Brasil como idioma principal do projeto. 
Vamos substituir o valor da variável pelo seguinte valor:
LANGUAGE_CODE = "pt-br"
Com isso, todas as mensagens e textos exibidos no painel administrativo já serão 
traduzidos automaticamente pelo módulo de internacionalização.


## Página 50

Nosso próximo passo é alterar o fuso horário padrão do projeto. Essa conﬁguração é 
importante pois não queremos que datas erradas sejam exibidas para nossos usuários. 
Por padrão, o Django trabalha e exibe as datas no fuso horário America/Chicago  (ou 
UTC ) mas como esse não é o fuso horário para a nossa região, vamos inserir a 
conﬁguração correta para nós. Existe também uma lista de fuso horários disponíveis e 
como podemos especiﬁcar eles através de uma string simples, como acontece no caso dos 
identiﬁcadores de idioma. Vamos utilizar o fuso horário America/Sao_Paulo . Ainda no 
arquivo settings.py,  vamos encontrar a variável TIME_ZONE  e alterar seu valor para o 
da nossa região:
TIME_ZONE = "America/Sao_Paulo"
Antes de realizar a modiﬁcação, observe os horários no painel administrativo do 
Django. O atributo "último login" e o histórico de modiﬁcações do usuário 
aparecem em um horário que não é o nosso.
Com isso, além do nosso projeto possuir um modelo personalizado de usuários, agora ele 
exibe mensagens e horários no idioma e fuso horário que é o mais apropriado para nossa 
região. A partir de agora é que as coisas vão ﬁcar mais interessantes e o projeto começará 
a tomar forma! Aperte os cintos!

## Página 51

Capítulo 04
Criando aplicativo para gerenciar porteiros
Aprendemos como instalar nossas dependências, como iniciar um novo projeto e já até 
escrevemos um modelo personalizado de usuários. Com isso, podemos dizer que já temos 
uma base sólida para iniciar, de fato, a construção dos módulos que estão diretamente 
ligados aos requisitos que o sistema deverá atender.
A partir dos requisitos que temos, é possível identiﬁcar que existe a necessidade de que os 
porteiros do condomínio tenham acesso a uma página para registrar os visitantes. Com 
isso em mente, podemos concluir:
Os porteiros terão um usuário para acessar o sistema
Deverá existir um modelo para representar os porteiros do condomínio
Os porteiros deverão ter acesso a uma dashboard com funcionalidades especíﬁcas
Deverá existir uma página para um porteiro registrar um visitante no condomínio
Vamos nos concentrar em cada item separadamente e, por agora, vamos focar no 
desenvolvimento da classe modelo que vai representar nossos porteiros. 
Já falamos que os aplicativos de um projeto Django devem executar tarefas especíﬁcas, 
como gerenciar os usuários do sistema - que é exatamente o que o nosso aplicativo 
usuarios  faz. Sendo assim, vamos iniciar um novo aplicativo com nome de "porteiros" 
que será responsável por gerenciar tudo referente aos porteiros. Vamos utilizar nosso bom 
e velho amigo manage.py :
(env)$ python manage.py startapp porteiros
Conforme vimos, será criado um diretório com o nome informado para representar o 
módulo do nosso aplicativo e, além disso, temos que instalar nosso novo aplicativo nas 
conﬁgurações do projeto. Vamos abrir nosso arquivo de conﬁgurações e inserir o aplicativo 
"porteiros" na variável INSTALLED_APPS :

## Página 52

INSTALLED_APPS += [1
    "usuarios",2
    "porteiros",3
]4
Caso não se lembre, tudo bem... nosso arquivo de conﬁgurações é o 
settings.py .
Agora que criamos e registramos nosso aplicativo, vamos partir para a construção do 
modelo que vai representar os porteiros.
Escrevendo as models do nosso aplicativo de porteiros
 
Assim como escrevemos a classe Usuario  para representar e descrever nossos usuários, 
vamos escrever a classe Porteiro  que será a representação de nossos porteiros. Em 
nosso documento de requisitos é possível veriﬁcar que os porteiros devem possuir os 
seguintes atributos:
Usuário para acesso ao sistema (e-mail)
Nome completo
CPF
Telefone
Data de nascimento
O primeiro passo será criar a classe Porteiro  no arquivo porteiros/models.py . Como 
já sabemos os atributos que um porteiro deve ter e já usamos o campo do tipo CharField  
anteriormente, começaremos trabalhando nos atributos que são deste tipo (nome 
completo, CPF e telefone):
from django.db import models1
2

## Página 53

class Porteiro(models.Model):3
4
    nome_completo = models.CharField(5
        verbose_name="Nome completo",6
        max_length=1947
    )8
9
    cpf = models.CharField(10
        verbose_name="CPF",11
        max_length=11,12
    )13
14
    telefone = models.CharField(15
        verbose_name="Telefone de contato",16
        max_length=11,17
    )18
Nossos três primeiros campos receberão apenas os argumentos verbose_name  e 
max_length . O primeiro para dizer por qual nome devemos chamar o campo e o segundo 
para dizer o tamanho máximo permitido.
Apesar de CPF e telefone serem representados por números, possuem 
características e particularidades que fazem com que a gente trabalhe com eles 
como se fossem texto. Além disso, o telefone está com tamanho 11 pois vamos 
trabalhar com o DDD + 9 dígitos.
Conhecendo o campo DateField
Sabemos também que, por exigência do setor de RH, é necessário informar a data de 
nascimento do porteiro para realização do cadastro. Vamos adicionar mais um campo ao 
nosso modelo, agora com nome de data_nascimento  e o tipo data (DateField ).
Os campos do tipo data representam datas - obviamente, mas é interessante a gente 
prestar atenção ao fato de que esses campos são representados por instâncias do tipo 
datetime.date  que é como as datas são tratadas no Python e podem receber dois 
argumentos que ainda não conhecemos: auto_now  e auto_now_add .

## Página 54

O argumento auto_now  diz para o Django que é necessário atualizar o valor sempre que 
nosso objeto for salvo. Se nós deﬁnirmos ele como True  (verdadeiro), o valor de 
data_nascimento  será atualizado para um valor atual sempre que atualizarmos as 
informações de um porteiro. No caso do argumento auto_now_add , ele diz para o Django 
que é necessário inserir a data atual como valor do atributo no momento da criação do 
registro no banco de dados e, feito isso, o valor não é atualizado novamente.
Como nosso objetivo é informar uma data que represente a data de nascimento do 
porteiro, vamos dizer ao Django que não é necessário preencher o campo 
automaticamente apenas setando os valores dos argumentos como False . 
from django.db import models1
2
class Porteiro(models.Model):3
4
    nome_completo = models.CharField(5
        verbose_name="Nome completo",6
        max_length=1947
    )8
9
    cpf = models.CharField(10
        verbose_name="CPF",11
        max_length=11,12
    )13
14
    telefone = models.CharField(15
        verbose_name="Telefone de contato",16
        max_length=11,17
    )18
    19
    data_nascimento = models.DateField(20
        verbose_name="Data de nascimento",21
        auto_now_add=False,22
        auto_now=False23
    )24
Conhecendo o campo OneToOneField
Até o momento utilizamos apenas campos do tipo texto e data, que são campos bastante 
úteis, mas que não são os ideais para todos os tipos de dados necessários para nosso 

## Página 55

modelo. Sendo assim, temos que conhecer um pouco mais dos tipos de campos 
disponíveis nos modelos do Django.
Sabemos que um dos requisitos é que haja um usuário do sistema para cada porteiro. 
Sendo assim, podemos dizer que é necessário vincular um usuário ao modelo que irá 
representar os porteiros em nosso sistema.
Uma vez que já temos o nosso modelo de usuários deﬁnido, temos que apenas vinculá-lo 
ao modelo de porteiros. Para tal, vamos conhecer o campo OneToOne  que é quem vai 
tornar explícito esse vínculo entre os modelos. Essencialmente, o campo OneToOne  
representa uma relação "um para um". Isto é, para cada porteiro existirá um único usuário. 
Para utilizar esse tipo de campo é bem fácil e funciona de modo bem parecido com os 
outros que já conhecemos, mudando apenas o argumento obrigatório que deve ser 
passado para o campo funcionar corretamente. Acima do atributo nome_completo , vamos 
começar deﬁnindo o atributo usuario  que será igual a models.OneToOneField() . 
from django.db import models1
2
class Porteiro(models.Model):3
4
    usuario = models.OneToOneField()5
6
    nome_completo = models.CharField(7
        verbose_name="Nome completo",8
        max_length=1949
    )10
11
    cpf = models.CharField(12
        verbose_name="CPF",13
        max_length=11,14
    )15
16
    telefone = models.CharField(17
        verbose_name="Telefone de contato",18
        max_length=11,19
    )20
    21
    data_nascimento = models.DateField(22
        verbose_name="Data de nascimento",23
        auto_now_add=False,24
        auto_now=False25
    )26

## Página 56

Conforme falamos, os argumentos que devem ser passados variam de campo para 
campo. Para o campo OneToOne , é necessário dizer qual modelo queremos que seja 
vinculado. Isto é, temos que dizer que o atributo usuario  do modelo Porteiro  deverá 
receber como valor uma instância da classe Usuario . Sempre que formos criar um 
Porteiro  temos que criar também um Usuario  e vinculá-lo ao Porteiro  criado.
Vamos primeiro dizer qual é o modelo que queremos vincular ao atributo. Para o caso é o 
modelo Usuario  do aplicativo usuarios . Podemos fazer isso passando apenas um 
texto contendo o caminho do modelo (usuarios.Usuario ). Os outros dois argumentos 
são o verbose_name , que nós já conhecemos e o on_delete , que é um nome novo para 
nós. O on_delete  diz para o Django o que deve ser feito com o registro do porteiro caso o 
usuário seja deletado. Nesse caso, se o usuario for removido da base de dados, o mesmo 
acontecerá com o porteiro.
from django.db import models1
2
class Porteiro(models.Model):3
4
    usuario = models.OneToOneField(5
        "usuarios.Usuario",6
        verbose_name="Usuário",7
        on_delete=models.CASCADE8
    )9
    10
    # código abaixo omitido...11
Para ﬁnalizar, vamos escrever as classes e métodos que devem acompanhar todos os 
modelos do Django. Vamos começar com a classe Meta  e depois escrever o método 
__str__ . Como vimos, devemos escrever essa classe e método para deﬁnir informações 
de como o modelo pode ser chamado, o nome da tabela que irá armazenar as informações 
no banco de dados e como a instância é exibida ao ser transformada em string. Nossa 
classe Porteiro  ﬁcará assim:
from django.db import models1

## Página 57

2
class Porteiro(models.Model):3
4
    usuario = models.OneToOneField(5
        "usuarios.Usuario",6
        verbose_name="Usuário",7
        on_delete=models.CASCADE8
    )9
10
    nome_completo = models.CharField(11
        verbose_name="Nome completo", max_length=19412
    )13
14
    cpf = models.CharField(15
        verbose_name="CPF",16
        max_length=11,17
    )18
19
    telefone = models.CharField(20
        verbose_name="Telefone de contato",21
        max_length=11,22
        blank=True23
    )24
25
    data_nascimento = models.DateField(26
        verbose_name="Data de nascimento",27
        auto_now=False28
    )29
30
    class Meta:31
        verbose_name = "Porteiro"32
        verbose_name_plural = "Porteiros"33
        db_table = "porteiro"34
35
    def __str__(self):36
        return self.nome_completo37
Registrando nossa aplicação no Admin do Django
 
O próximo passo que vamos executar é tornar o nosso modelo de porteiros visível para o 
Admin do Django. Como já sabemos fazer isso, vai ser bem rápido!
Vamos abrir o arquivo admin.py  do nosso aplicativo porteiros, importar a classe 
Porteiro  e passá-la como argumento do método admin.site.register() .

## Página 58

from django.contrib import admin1
from porteiros.models import Porteiro2
3
admin.site.register(Porteiro)4
Aplicando as alterações em nosso banco de dados
 
Feito isso, vamos agora validar o código escrito e criar as migrações do modelo criado 
utilizando o comando makemigrations .
(env)$ python manage.py makemigrations porteiros
Se ocorrer bem, vamos receber as seguintes informações em nosso terminal:
Migrations for 'porteiros':1
  porteiros/migrations/0001_initial.py2
    - Create model Porteiro3
Com todas as informações necessárias para executar as alterações no banco de dados 
armazenadas em forma de migração, vamos pedir ao Django que efetue essas alterações 
em nosso banco. Para isso vamos executar o comando migrate .
(env)$ python manage.py migrate
E, se tudo ocorrer bem, vamos receber em nosso terminal:
Operations to perform:1
  Apply all migrations: admin, auth, contenttypes, porteiros, sessions, us2

## Página 59

Captura tirada do Admin do Django focando nos links para a exibição de Grupos, Usuário e 
agora Porteiros também
3
Running migrations:4
  Applying porteiros.0001_initial.py... OK5
Criando porteiro através do Admin do Django
 
Como sabemos, o Django disponibiliza uma interface de administração para as classes de 
modelo criadas e registradas nos arquivos admin.py . Até agora, tudo que ﬁzemos foi 
apenas visualizar e alterar informações de usuários, mas é possível fazer bem mais com o 
Admin do Django. Vamos acessar o admin através do navegador e clicar no item porteiros.
A próxima tela deverá exibir a lista de porteiros registrados em nosso sistema. Como ainda 
não temos porteiros registrados, temos apenas a informação de que existem "0 Porteiros" e 
opção de adicionar um porteiro. 

## Página 60

Tela listando os porteiros registrados em nosso banco de dados (no caso, ainda não temos 
porteiros registrados e, por isso, o texto "0 porteiros" é exibido
Vamos clicar no botão "adicionar porteiro" para ter acesso ao formulário de cadastro de 
porteiros. Para adicionar um porteiro, basta preencher as informações obrigatórias que são 
usuário, nome completo, CPF e data de nascimento. Note que os campos obrigatórios 
ﬁcam destacados em negrito.
O Admin do Django é tão interessante que já disponibiliza um elemento do tipo 
select para selecionarmos o usuário que será vinculado ao novo porteiro. 
Bacana, não?
Vamos selecionar o usuário criado através do terminal com o comando createsuperuser  
e preencher as informações necessárias. Esteja livre para preencher da sua maneira!
Você deve utilizar o formato DD/MM/AAAA para a data de nascimento do 
porteiro

## Página 61

Tela listando os porteiros registrados em nosso banco de dados, agora com nosso primeiro 
porteiro registrado
Se tudo estiver certo com os dados informados, o Django Admin vai nos redirecionar para 
a tela que lista os porteiros e mostrar uma mensagem de sucesso. Note que o Django já 
exibe a mensagem personalizada com o nome do porteiro criado e link para visualização 
das informações.
Agora que temos um porteiro criado, podemos partir para a construção da dashboard que 
contará com as funções descritas em nosso documento de requisitos.

## Página 62

Capítulo 05
Conﬁgurando a aplicação para trabalhar com arquivos 
estáticos e templates HTML
Nos capítulos anteriores, iniciamos o projeto e criamos toda a estrutura necessária para 
administração de usuários do sistema e porteiros que serão os responsáveis por operar a 
dashboard proposta. Além disso, também preparamos o ambiente de desenvolvimento e 
aprendemos bastante sobre detalhes técnicos do funcionamento do Django.
Focamos nosso trabalho nos arquivos models.py  e admin.py  e também conhecemos o 
poder existente do Admin que o Django nos disponibiliza. Como nosso objetivo é 
desenvolver uma dashboard personalizada para exibir as informações dos visitantes do 
condomínio e implementar funcionalidades especíﬁcas, a partir de agora, trabalharemos 
para desenvolver os templates que irão apresentar as informações necessárias e executar 
as funcionalidades que vamos desenvolver. Sendo assim, posso dizer que a partir de agora 
as coisas começam a ﬁcar mais interessantes!
Neste próximo módulo, aprenderemos a conﬁgurar o Django para trabalhar com arquivos 
estáticos (CSS e JS) e templates HTML.
O Django, por padrão, vem conﬁgurado para que já seja possível trabalhar com 
templates HTML, mas vamos alterar as conﬁgurações para que a haja uma 
maior organização dos arquivos e de modo que a gente agrupe todos os 
template numa só pasta
Criando a pasta templates em nosso projeto
Sendo um framework web, o Django precisa fornecer uma maneira de gerar os templates 
de forma dinâmica, de modo que seja possível exibir valores especíﬁcos e atender os 
diversos cenários. Essencialmente, um template é constituído por uma parte estática, que 
são os arquivos CSS e JS e partes que se repetem, e uma parte onde serão exibidas as 
informações desejadas, que variam de acordo com cada cenário.

## Página 63

Imagine em nosso caso em que os porteiros deverão registrar visitantes. Para 
cada visitante, teremos informações diferentes e, desta forma, o template 
deverá ser capaz de exibir essas informações de acordo com o contexto de 
cada visitante
Para resolver esse problema, o Django nos fornece uma engine rica e poderosa capaz de 
executar funções condicionais, loops, exibir valores e ainda possui diversas 
funcionalidades que podem ser utilizadas diretamente nos templates HTML através de 
tags.
Uma engine de template nada mais é que uma aplicação que visa facilitar o 
processo de criação de templates HTML dinâmicos e tornar o processo de envio 
e exibição de informações nos templates menos burocrático
Por padrão, o Django vem conﬁgurado para procurar os templates dentro de cada 
aplicativo. Isto é, em cada aplicativo deverá existir uma pasta templates para armazenar 
os templates referentes ao aplicativo em questão. Todavia, para uma melhor organização, 
utilizaremos uma pasta externa para armazenar todos os arquivos de templates do projeto.
Para isso, começaremos alterando o arquivo settings.py  do nosso projeto. Nesse 
arquivo é possível encontrar a variável TEMPLATES , que é responsável por deﬁnir as 
conﬁgurações de template do projeto, como engine a ser utilizada, diretórios que 
armazenam os templates, dentre outras.
A variável TEMPLATES  é uma lista que recebe um dicionário contendo valores especíﬁcos, 
tais como BACKEND , DIRS , APP_DIRS  e OPTIONS , cada um com uma função especíﬁca. 
No nosso caso, vamos alterar o valor DIRS  de uma lista vazia para uma lista contendo a 
string "templates", que é o nome da pasta que utilizaremos para armazenar os templates 
na raiz do projeto. A variável TEMPLATES  ﬁcará da seguinte forma:
TEMPLATES = [1
    {2

## Página 64

        "BACKEND": "django.template.backends.django.DjangoTemplates",3
        "DIRS": ["templates"],4
        "APP_DIRS": True,5
        "OPTIONS": {6
            "context_processors": [7
                "django.template.context_processors.debug",8
                "django.template.context_processors.request",9
                "django.contrib.auth.context_processors.auth",10
                "django.contrib.messages.context_processors.messages",11
            ],12
        },13
    },14
]15
Para facilitar as coisas e economizar um pouquinho de tempo, você pode fazer download 
da pasta templates zipada, extrair os arquivos e colocá-la na raíz do seu projeto:
Iniciar o download templates.zip - 2KB
Criando a pasta static em nosso projeto
Feito isso, vamos agora deﬁnir as conﬁgurações para os arquivos estáticos do nosso 
projeto. Assim como para os templates, o Django também nos dá toda a estrutura 
necessária para trabalharmos com arquivos estáticos.
Por "arquivos estáticos", entenda arquivos do tipo CSS, JS (javascript) e imagens que serão 
utilizadas em nossos templates, tais como logotipo, imagem padrão para avatar de 
usuários, dentre outras.
Para realizarmos a conﬁguração, vamos novamente alterar o arquivo settings.py.  Ao 
ﬁnal do arquivo, você vai encontrar a variável STATIC_URL  que é onde nossos arquivos 
estáticos devem ﬁcar, ou seja, na pasta static  na raiz do projeto:
STATIC_URL = "/static/"

## Página 65

Abaixo da variável STATIC_URL , coloque também o seguinte trecho de código:
STATICFILES_DIRS = [1
    os.path.join(BASE_DIR, "static")2
]3
Desta forma estamos dizendo para o Django que os arquivos estáticos devem ser 
procurados na pasta static na raiz do projeto. Para facilitar e economizar tempo 
novamente, faça download da pasta zipada clicando no link abaixo (agora da pasta static, 
claro) e a coloque na raiz do projeto:
Iniciar o download static.zip - 2MB
Faça o download e coloque a pasta static na raiz do projeto, juntamente com a pasta 
templates. Feito isso, já podemos utilizar templates HTML e arquivos estáticos em nosso 
projeto.
Criando views que renderizam templates
 
O HTML (Linguagem de Marcação de HiperTexto) é o bloco de construção mais básico da 
pilha de tecnologias que compõem a web, mas é ela que dá signiﬁcado e deﬁne a estrutura 
do conteúdo das páginas. Existem também tecnologias que descrevem 
aparência/apresentação (CSS) e funcionalidade/comportamento (Javascript) de uma 
página web (inclusive já falamos um pouquinho delas por aqui quando falamos sobre 
arquivos estáticos).
Basicamente, um arquivo de template é um arquivo de texto com extensão .html . Os 
navegadores interpretam esses arquivos de texto e cuidam de exibir exatamente da 
maneira que você enxerga pelo seu monitor. 
Bacana não? Além disso, o HTML ajuda a dizer para os motores de busca o que é 
relevante, o que é texto, o que é imagem e tudo mais. Sendo assim, o HTML tem um papel 

## Página 66

fundamental dentro da web! 
E ah, não se assuste com a palavra HiperTexto no nome, hipertexto são apenas 
os links entre as páginas que se conectam na web. 
Como o Django já nos dá tudo que é necessário para criarmos aplicações web, ele também 
nos dá a possibilidade de criarmos views que renderizam templates. Isso signiﬁca que a 
partir de agora, ao invés de ser exibido um texto ao acessarmos uma URL através do 
navegador, como ﬁzemos anteriormente, vamos dizer para o Django que é necessário exibir
um template HTML, aﬁm de exibir as informações de forma estruturada e de modo que 
ﬁquei fácil a compreensão para nossos usuários.
Conhecendo a função render
Para que o Django exiba um template ao invés de um texto em tela, precisaremos alterar o 
retorno da nossa view chamada index . Antes de seguir, vamos trabalhar um pouco a 
memória e lembrar como a nossa view está:
from django.http import HttpResponse1
2
def index(request):3
    return HttpResponse("Olá, mundo!")4
Até então, utilizamos o HttpResponse  para retornar uma mensagem, mas a partir de 
agora utilizaremos a função render  para exibir um template HTML no lugar dessa 
mensagem. 
A função render  é uma função de atalho do Django que nos possibilita combinar um 
template HTML e um dicionário de contexto. A função deve receber sempre a variável 
request  e uma string  representando o caminho do template a ser utilizado. Esses 
argumentos são obrigatórios e devem ser passados para a função render  sempre que a 
mesma for utilizada.

## Página 67

Vamos alterar a nova view para que retorne a função render  ao invés da classe 
HttpResponse  passando a variável request  e o caminho para o template index.html :
def index(request):1
    return render(request, "index.html")2
Como já ﬁzemos o download das pastas static e templates e toda a conﬁguração 
necessária para funcionamento de ambas, o Django já reconhece a pasta e busca pelo 
template index.html  dentro dela.
Entendendo as adaptações necessárias no template
 
Como você deve ter percebido, o template não está sendo exibido como deveria. Isso 
porque os arquivos estáticos não foram carregados. Lembra que ﬁzemos a conﬁguração 
da variável STATIC_URL ? Pois bem, precisamos falar dela aqui pois para que os arquivos 
sejam carregados corretamente, o caminho relativo até eles deve estar correto e é aqui que 
a STATIC_URL  entra em cena.
Conhecendo a tag static
Quando falamos anteriormente sobre a engine de templates do Django, falamos que ela é 
capaz de executar funções condicionais, loops, exibir valores e possui diversas outras 
funcionalidades que podem ser executadas diretamente nos templates através de tags. 
Vamos agora conhecer a primeira tag que vamos utilizar em nosso projeto, a tag static.
A tag static é a representação da variável STATIC_URL  nos templates. O Django fornece 
essa tag no intuito de facilitar o trabalho com arquivos estáticos. Vamos aprender como 
utilizar a tag e resolver o problema de exibição do template.
O primeiro passo para utilizarmos a tag static é carregá-la no template. Para isso vamos 
inserir o seguinte trecho de código no topo do nosso HTML:

## Página 68

<!DOCTYPE html>1
2
{% load static %}3
4
<html lang="pt-br">5
Tags no Django são escritas dessa maneira: {% %} . Guarde isso, pois 
utilizaremos bastante no decorrer do curso. 
Com isso já podemos utilizar a tag no template index.html .
Alterando o caminho dos arquivos estáticos
Como falamos, a tag {% static %}  é a representação da pasta static. A tag nos dá um 
link para essa pasta para utilização no carregamento dos arquivos estáticos nos 
templates. Como é o Django que cuida de toda essa parte por nós, também vamos delegar 
a ele o carregamento dos nossos arquivos JS, CSS e imagens.
Alterando as importações dos arquivos CSS
Vamos alterar primeiro as importações dos arquivos CSS. As linhas que fazem o 
carregamento dos arquivos CSS no template são:
<link href="css/sb-admin-2.min.css" rel="stylesheet">1
<link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type2
Vamos alterar os textos referentes a href  para utilizarmos a tag {% static %} . As 
importações ﬁcarão assim:
<link href="{% static 'css/sb-admin-2.min.css' %}" rel="stylesheet">    1
<link href="{% static 'vendor/fontawesome-free/css/all.min.css' %}" rel="s2

## Página 69

Tela inicial da dashboard contento uma tabela que lista os visitantes recentes, nela é 
possível observar o visitante "Don Corleone"
Alterando as importações dos arquivos JS
Para alterarmos as importações dos arquivos JS, vamos encontrar as linhas:
<script src="vendor/jquery/jquery.min.js"></script>1
<script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>2
<script src="js/sb-admin-2.min.js"></script>3
E alterá-las para que ﬁquem da seguinte forma:
<script src="{% static 'vendor/jquery/jquery.min.js' %}"></script>1
<script src="{% static 'vendor/bootstrap/js/bootstrap.bundle.min.js' %}"><2
<script src="{% static 'js/sb-admin-2.min.js' %}"></script>3
Com isso, ao acessarmos http://127.0.0.1:8000/  novamente no navegador, teremos o 
template exibido de forma estruturada com os arquivos CSS (exibição) e JS 
(comportamento) devidamente carregados. Nosso template será exibido desta forma no 
navegador:
 

## Página 70

Exibindo variáveis no template
Quando conhecemos a função render  falamos que ela é responsável por combinar um 
template HTML e um dicionário de contexto, mas não fomos a fundo a respeito do que é 
um dicionário de contexto.
Um dicionário de contexto é a variável do tipo dicionário que pode ser passada como 
argumento para a função render . Quando passada, é possível acessarmos os valores 
contidos na variável diretamente no template através de tags especíﬁcas, diferentes das 
tags utilizadas anteriormente.
Dicionário é uma estrutura de dados em Python de elementos (ou propriedades) 
não ordenados e que podemos acessar utilizando chaves. Os dicionários são 
estruturas poderosas e muito utilizadas. Existem linguagens que este tipo é 
conhecido como "matrizes associativas" ou apenas "objetos"
Deﬁnindo nosso dicionário de contexto
Para fazer isso, vamos no arquivo views.py  e vamos criar a variável context  acima do 
retorno da função. A função index  ﬁcará da seguinte forma:
def index(request):1
    2
    context = {3
        "nome_pagina": "Início da dashboard",4
    }5
    6
    return render(request, "index.html", context)7
No código acima criamos a variável context  já com o valor de nome_pagina  deﬁnido 
como "Início da dashboard". Se a gente quisesse utilizar uma variável ao invés de um texto 
diretamente, poderíamos fazer desta forma: 

## Página 71

def index(request):1
    nome_pagina = "Início da dashboard"2
3
    context = {4
        "nome_pagina": nome_pagina,5
    }6
    7
    return render(request, "index.html", context)8
Exibindo as informações nos templates
A partir de agora, vamos aprender um pouco mais sobre a linguagem de templates do 
Django. Ela foi projetada para ser poderosa e fácil de forma que seja confortável trabalhar 
com a linguagem HTML.
Essencialmente, templates são arquivos de texto, geralmente no formato HTML. Para o 
Django, um template pode conter variáveis que devem ser substituídas por valores quando 
o template for interpretado.
Agora que já deﬁnimos o nosso dicionário de contexto e passamos ele como argumento 
para a função render , vamos exibir essas informações no template index.html .
Para exibirmos os valores contidos no dicionário context  basta utilizarmos a sintaxe 
para variáveis da linguagem de templates do Django: {{ propriedade_do_dicionario }} 
. Para nosso caso, vamos exibir o valor da propriedade nome_pagina  que, dentro do 
dicionário context , corresponde ao texto Início da dashboard. 
Vamos abrir o arquivo index.html  e procurar pela seguinte linha:
<h1 class="h3 mb-0 text-gray-800">Página inicial</h1>
Vamos alterar o texto da tag h1  (o texto Página inicial) para exibir também o valor da 
nossa variável nome_pagina  passada na variável context  da view. A linha deverá ﬁcar 
assim:

## Página 72

<h1 class="h3 mb-0 text-gray-800">{{ nome_pagina }}</h1>
Volte para o navegador, atualize a página e veja a mágica acontecer: o valor 
{{ nome_pagina }}  será substituído pelo texto "Início da dashboard" que deﬁnimos no 
dicionário context . Se alterarmos o valor no arquivo views.py  o mesmo acontece no 
index.html .

## Página 73

Capítulo 06
Criando o aplicativo para gerenciar visitantes
No último capítulo conﬁguramos o Django para trabalhar com templates HTML e arquivos 
estáticos e criamos as pastas templates e static na raiz do projeto. Além disso, ainda 
aprendemos como passar informações de uma função view para o template através da 
variável context.
Como já deﬁnimos os usuários do sistema, os porteiros e ﬁzemos as conﬁgurações dos 
templates que serão a base para construção da dashboard para controle de visitantes, 
podemos partir agora para a deﬁnição da classe modelo que irá representar os visitantes 
em nosso sistema.
Antes de mais nada, como já sabemos, devemos isolar as responsabilidades e, por isso, 
vamos criar um aplicativo para administrar toda a parte referente aos nossos visitantes. 
Vamos criar um novo aplicativo com nome de visitantes utilizando o manage.py :
(env)$ python manage.py startapp visitantes
Após criarmos o aplicativo utilizando o manage.py , vamos registrá-lo no arquivo de 
conﬁgurações, o settings.py , logo abaixo do aplicativo porteiros:
INSTALLED_APPS += [1
    "usuarios",2
    "porteiros",3
    "visitantes",4
]5
Feito isso, vamos começar os trabalhos no arquivos models.py  para deﬁnirmos as 
informações necessárias para o modelo de visitantes.
 

## Página 74

Escrevendo as models do nosso aplicativo de visitantes
Conforme falamos, a camada model (ou camada de modelo) é nossa fonte segura de 
dados e onde deﬁnimos o formato das informações que serão disponibilizadas para outras
camadas da aplicação.
Precisamos guardar uma série de informações a respeito de quem deseja adentrar ao 
condomínio para realizar visitas a moradores, além da autorização de um morador que 
esteja na casa no momento da visita. O procedimento faz parte de normas do condomínio 
para ﬁns de ﬁscalização, controle e segurança dos moradores. Segundo normas do 
condomínio, devemos guardar as seguintes informações referentes à visita:
1. Nome completo do visitante
2. CPF do visitante
3. Data de nascimento do visitante
4. Número da casa a ser visitada
5. Placa do veículo utilizado na visita, se houver
 . Horário de chegada na portaria
7. Horário de saída do condomínio
 . Horário de autorização de entrada
9. Nome do morador responsável por autorizar a entrada do visitante
10. Porteiro responsável por registrar visitante
Inicialmente, vamos nos concentrar nas informações de 1 a 5 para que possamos avaliar e 
escrever por partes o modelo de visitantes. Vamos escrever primeiro os atributos nome 
completo, CPF, data de nascimento, número da casa e placa do veículo, pois a gente já 
conhece a maioria desses tipos de dados. Nossa classe Visitante  ﬁcará assim:
from django.db import models1
2
class Visitante(models.Model):3
    nome_completo = models.CharField(4
        verbose_name="Nome completo", max_length=1945
    )6
7
    cpf = models.CharField(8
        verbose_name="CPF",9
        max_length=11,10
    )11

## Página 75

12
    data_nascimento = models.DateField(13
        verbose_name="Data de nascimento",14
        auto_now=False,15
        auto_now_add=False,16
    )17
18
    numero_casa = models.PositiveSmallIntegerField(19
        verbose_name="Número da casa a ser visitada"20
    )21
22
    placa_veiculo = models.CharField(23
        verbose_name="Placa do veículo",24
        max_length=7,25
        blank=True,26
        null=True,27
    )28
Conhecendo o campo DateTimeField
Antes de prosseguirmos, vamos conhecer o campo DateTimeField , um cara bem 
parecido com o DateField  que já conhecemos com a diferença que, além da data, salva 
também o horário exato do registro. Assim como o DateField , o DateTimeField  aceita 
auto_now  e auto_now_add  como argumentos, além das opções blank  e null . Vamos 
utilizar o DateTimeField  para deﬁnirmos os atributos que vão representar o horário de 
chegada e o horário de saída do visitante.
Primeiro vamos deﬁnir o atributo horario_chegada , que é quem representa o horário de 
chegada do visitante à portaria do condomínio. Como o atributo representa o horário de 
chegada do visitante à portaria, faz sentido que o mesmo seja preenchido no exato 
momento que registrarmos o visitante em nosso sistema. Para isso, utilizaremos a opção 
auto_now_add  com o valor True , assim garantimos que o atributo receberá o valor da 
hora atual assim que o registro for adicionado ao banco de dados.
from django.db import models1
2
class Visitante(models.Model):3
    # código acima omitido...4
5
    placa_veiculo = models.CharField(6
        verbose_name="Placa do veículo",7

## Página 76

        max_length=7,8
        blank=True,9
        null=True,10
    )11
    12
    horario_chegada = models.DateTimeField(13
        verbose_name="Horário de chegada na portaria",14
        auto_now_add=True15
    )16
Para o caso do horário de saída, utilizaremos uma conﬁguração diferente para o atributo. 
Como precisamos setar o valor somente após a saída do visitante do condomínio, esse 
valor precisa ser registrado inicialmente como um valor em branco. Para isso, o Django nos
dá a possibilidade de utilização do atributo auto_now  como False  e dizer que podemos 
aceitar valores em branco e nulos. Utilizando o auto_now  como False , o campo 
receberá um valor em branco no momento da criação do registro no banco de dados.
from django.db import models1
2
class Visitante(models.Model):3
    # código acima omitido...4
5
    placa_veiculo = models.CharField(6
        verbose_name="Placa do veículo",7
        max_length=7,8
        blank=True,9
        null=True,10
    )11
    12
    horario_chegada = models.DateTimeField(13
        verbose_name="Horário de chegada na portaria",14
        auto_now_add=True15
    )16
    17
    horario_saida = models.DateTimeField(18
        verbose_name="Horário de saída do condomínio",19
        auto_now=False,20
        blank=True,21
        null=True,22
    )23

## Página 77

Conforme visto, além destas informações, precisamos guardar também o nome do 
morador que autorizou a entrada do visitante e o horário da autorização. Sendo assim, 
teremos mais dois atributos:
Horário de autorização de entrada
Nome do morador responsável por autorizar a entrada do visitante
Utilizaremos os campos já conhecidos DateTimeField  e CharField  para deﬁnir os 
atributos:
from django.db import models1
2
class Visitante(models.Model):3
    # código acima omitido...4
    5
    horario_saida = models.DateTimeField(6
        verbose_name="Horário de saída do condomínio",7
        auto_now=False,8
        blank=True,9
        null=True,10
    )11
    12
    horario_autorizacao = models.DateTimeField(13
        verbose_name="Horário de autorização de entrada",14
        auto_now=False,15
        blank=True,16
        null=True,17
    )18
    19
    morador_responsavel = models.CharField(20
        verbose_name="Nome do morador responsável por autorizar a entrada 21
        max_length=194,22
        blank=True,23
    )24
Nada de novo por enquanto: utilizamos um campo do tipo CharField  para armazenar o 
nome do morador responsável por autorizar a entrada e utilizamos um DateTimeField  
para armazenar o horário em que a autorização ocorreu. Conforme vimos, se não 
queremos que o campo DateTimeField  seja preenchido na hora da criação ou 
atualização do registro, setamos o argumento auto_now  como False . Isso garante 
também que o campo possa ser preenchido com um texto vazio.

## Página 78

Conhecendo o campo ForeignKey
Seguindo a lista de requisitos, o próximo atributo que devemos adicionar ao nosso modelo 
é a informação referente ao porteiro responsável por registrar a entrada do visitante.
Como criamos um modelo que representa nossos porteiros dentro do sistema, podemos 
associar esse modelo ao modelo de visitante por meio do campo ForeignKey . Esse 
campo cria um atributo que vincula um registro de modelo a outro registro de modelo. 
Neste caso, queremos vincular o modelo Porteiro  ao modelo Visitante  para 
representar o porteiro responsável pelo registro.
O campo ForeignKey  é importante pois assim não precisamos replicar as informações 
do porteiro no registro de visitante, apenas referenciamos essas informações inserindo o 
id  referente ao registro do porteiro. Como os modelos são representações das tabelas do 
nosso banco de dados, estamos dizendo algo como: "hey, Django, procure essas 
informações na tabela de porteiros usando esse id!" e o Django faz todo o trabalho de 
trazer essas informações por nós.
É importante lembrar que tudo isso é possível devido à ORM do Django, que é 
quem abstrai todas as funcionalidades do banco de dados e manipula todas as 
interações necessárias
Abaixo do atributo morador_responsavel , vamos escrever o atributo  registrado_por  
sendo do tipo ForeignKey , que representará a informação do porteiro responsável por 
registrar a entrada do visitante:
from django.db import models1
2
class Visitante(models.Model):3
    # código acima omitido...4
    5
    morador_responsavel = models.CharField(6
        verbose_name="Nome do morador responsável por autorizar a entrada 7
        max_length=194,8
        blank=True,9
    )10

## Página 79

    11
    registrado_por = models.ForeignKey(12
        "porteiros.Porteiro",13
        verbose_name="Porteiro responsável pelo registro",14
        on_delete=models.PROTECT15
    )16
Os argumentos que o campo ForeignKey  recebe são bem parecidos com os do 
OneToOneField  que já conhecemos. Primeiro informamos a classe modelo que deverá ser 
relacionada: a classe Porteiro  do aplicativo porteiros. Depois utilizamos o 
verbose_name  para dar um nome descritivo para o campo e informamos o que deve ser 
feito com o registro do visitante caso o registro do porteiro da relação seja excluído. Nesse 
caso, utilizaremos para o on_delete  a ação models.PROTECT , pois assim protegemos 
também o modelo de visitantes. Sempre que houver tentativa de exclusão de um registro 
de porteiro que esteja vinculado a um visitante, o Django mostrará um erro. O atributo está 
protegido contra exclusão.
Nosso próximo passo agora é apenas escrever a classe Meta  e o método __str__  da 
classe Visitante. Nosso modelo ﬁcará assim:
from django.db import models1
2
class Visitante(models.Model):3
    nome_completo = models.CharField(4
        verbose_name="Nome completo", max_length=1945
    )6
7
    cpf = models.CharField(8
        verbose_name="CPF",9
        max_length=11,10
    )11
12
    data_nascimento = models.DateField(13
        verbose_name="Data de nascimento",14
        auto_now=False15
    )16
17
    numero_casa = models.PositiveSmallIntegerField(18
        verbose_name="Número da casa a ser visitada",19
    )20
21
    placa_veiculo = models.CharField(22

## Página 80

        verbose_name="Placa do veículo",23
        max_length=7,24
        blank=True,25
        null=True,26
    )27
    28
    horario_chegada = models.DateTimeField(29
        verbose_name="Horário de chegada na portaria",30
        auto_now_add=True31
    )32
    33
    horario_saida = models.DateTimeField(34
        verbose_name="Horário de saída do condomínio",35
        auto_now=False,36
        blank=True,37
        null=True,38
    )39
    40
    horario_autorizacao = models.DateTimeField(41
        verbose_name="Horário de autorização de entrada",42
        auto_now=False,43
        blank=True,44
        null=True,45
    )46
    47
    morador_responsavel = models.CharField(48
        verbose_name="Nome do morador responsável por autorizar a entrada 49
        max_length=194,50
        blank=True,51
    )52
53
    registrado_por = models.ForeignKey(54
        "porteiros.Porteiro",55
        verbose_name="Porteiro responsável pelo registro",56
        on_delete=models.PROTECT57
    )58
    59
    class Meta:60
        verbose_name = "Visitante"61
        verbose_name_plural = "Visitantes"62
        db_table = "visitante"63
64
    def __str__(self):65
        return self.nome_completo66
Registrando nossa aplicação no Admin do Django
 

## Página 81

O próximo passo a ser executado, como já vimos, é tornar o nosso modelo visível para o 
Admin do Django. Então vamos lá!
Vamos abrir o arquivo admin.py  do nosso aplicativo visitantes, importar a classe 
Visitante  e passá-la como argumento da função admin.site.register() .
from django.contrib import admin1
from visitantes.models import Visitante2
3
admin.site.register(Visitante)4
Aplicando as alterações em nosso banco de dados
 
Feito isso, mais uma vez vamos criar as migrações do modelo criado utilizando o 
comando makemigrations .
(env)$ python manage.py makemigrations visitantes
Se tudo ocorrer bem, vamos receber as seguintes informações em nosso terminal:
Migrations for 'visitantes':1
  porteiros/migrations/0001_initial.py2
    - Create model Visitante3
Com todas as informações necessárias para executar as alterações no banco de dados 
armazenadas em forma de migração, vamos aplicar as alterações em nosso banco de 
dados com o comando migrate .
(env)$ python manage.py migrate

## Página 82

Captura tirada do Admin do Django focando nos links para a exibição de Grupos, Usuários, 
Porteiros e agora Visitantes também
Devemos receber as seguintes informações em nosso terminal:
Operations to perform:1
  Apply all migrations: admin, auth, contenttypes, porteiros, sessions,2
  usuarios, visitantes3
4
Running migrations:5
  Applying visitantes.0001_initial.py... OK6
Adicionando visitante utilizando o Django Admin
 
Da mesma forma que cadastramos um porteiro utilizando o Admin do Django, vamos 
adicionar também um visitante. Vamos novamente acessar http://127.0.0.1:8000/admin e 
agora veremos o aplicativo visitantes disponível para nós.


## Página 83

Formulário para registro de visitante. O formulário apresenta os campos da classe modelo
Dessa vez, vamos clicar diretamente no botão "adicionar" para que a gente vá direto para o 
formulário de cadastro de visitantes. O formulário a ser exibido deverá se parecer com isto:
Por enquanto vamos preencher os campos obrigatórios nome completo, CPF, data de 
nascimento e número da casa a ser visitada e deﬁnir o porteiro responsável por registrar o 
visitante. Fique livre para preencher as informações à sua maneira. Após preencher os 
campos citados, clique em salvar e visualize a lista de visitantes agora com o novo 
visitante registrado.
Essa foi a primeira e última vez utilizamos o Django Admin para registar um visitante, pois 
a partir de agora trabalharemos diretamente nos templates HTML da dashboard que 
vamos disponibilizar para os porteiros do condomínio.
Listando visitantes na página inicial da dashboard
 
Como já deﬁnimos nosso modelo e até registramos visitantes através do Admin, agora 
vamos aprender como buscar esses registros em nosso banco de dados.
Quando precisamos buscar registros em nosso banco de dados, devemos construir uma 
Queryset utilizando o Manager da classe modelo em questão. A classe Manager, conforme
visto, deﬁne como as interações com o banco de dados devem acontecer e, por padrão, é 

## Página 84

um atributo da classe chamado objects . Já uma queryset nada mais é que uma lista de 
objetos de um determinado tipo existentes em nosso banco de dados. 
Sempre que deﬁnimos uma subclasse de django.db.models.Model , que é o que todos os 
nossos modelos são, o Django nos fornece de forma automática uma interface para 
realizar operações em nosso banco de dados, tais como buscar, atualizar, criar e deletar 
registros, mas por hora, vamos nos concentrar apenas em buscar os registros de visitantes.
Buscando registros de visitantes no banco de dados
Quando falamos da camada view, vimos que é ela quem deve encapsular toda a lógica 
necessária para apresentar os dados. Geralmente, as views devem buscar as informações 
no banco de dados, carregar o template e renderizar esse template com as informações 
buscadas. Uma view no Django tem a função de exatamente conectar a camada de 
modelo à camada de template.
O primeiro passo para buscarmos os registros é criar uma variável para armazenar os 
registros que serão retornados, para isto utilizaremos a variável todos_visitantes . A 
variável receberá uma queryset que será retornada pelo método all()  do Manager 
objects  do modelo Visitante.
Antes de tudo, vamos importar o modelo no arquivo views.py  do aplicativo usuarios.
from django.shortcuts import render1
2
from visitantes.models import Visitante3
4
def index(request):5
    context = {6
        "nome_pagina": "Início da dashboard",7
    }8
    9
    return render(request, "index.html", context)10
Feito isso, vamos criar a variável todos_visitantes  acima da variável context  e deﬁnir 
seu valor como Visitante.objects.all() . Desta forma, estamos buscando todos os 
registros de visitantes existentes em nosso banco de dados.

## Página 85

Não podemos nos esquecer de colocar a variável todos_visitantes  dentro do nosso 
dicionário context  para que possamos acessá-la através do template. A função index  
ﬁcará assim:
from visitantes.models import Visitante1
2
def index(request):3
4
    todos_visitantes = Visitante.objects.all()5
    6
    context = {7
        "nome_pagina": "Início da dashboard",8
        "todos_visitantes": todos_visitantes,9
    }10
    11
    return render(request, "index.html", context)12
Listando registros de visitantes no template HTML
Conhecendo a tag for e acessando atributos do visitante
Para exibir variáveis nos templates vimos que podemos utilizar a sintaxe de chaves (
{{  }} ), mas se tentarmos exibir uma queryset desta maneira, não será possível, pois 
uma queryset é uma lista que contém vários itens. É necessário percorrer os itens dessa 
lista e acessar item por item. Pra nossa sorte, o Django nos fornecer uma tag para que 
possamos executar loops em listas.
A tag {% for %}  é quem vai nos ajudar agora. O que ela faz é justamente andar por todos
os itens da lista e disponibilizar uma variável para que possamos acessar as informações 
da mesma. Parece um pouco confuso? Não se assuste, vamos entender melhor 
visualizando o código.
No nosso caso, buscamos todos os registros de visitantes que temos em nosso banco de 
dados e passamos essa lista como variável dentro do contexto da view. O que precisamos 
fazer agora é passar em cada item existente na lista de visitantes e exibir as informações 
como nome completo, CPF e data de nascimento.

## Página 86

Para acessarmos as informações dos visitantes nos templates, utilizaremos o 
nome dos atributos deﬁnidos da classe modelo.
Vamos abrir o arquivo de template index.html  e buscar pelo elemento HTML <tbody> . 
É dentro dele, acima dos elementos <tr>  que vamos deﬁnir o início da tag {% for %} . 
Para utilizar essa tag, precisamos também evidenciar onde o loop deve ser parado e 
fazemos isso utilizando a tag {% endfor %} .
Logo abaixo do elemento <tbody>  insira o trecho 
{% for visitante in todos_visitantes %} . Lembra que falamos da variável que a tag 
{% for %}  disponibiliza para que possamos acessar as informações? Pois bem, 
podemos dar nome a ela e, neste caso, utilizaremos o nome visitante . O trecho de 
código ﬁcará assim:
<tbody>1
    {% for visitante in todos_visitantes %}2
        <tr>3
            <td>Don Corleone</td>4
            <td>123.123.123.06</td>5
            <td>22 de agosto 15:30</td>6
            <td>22 de agosto 15:38</td>7
            <td>Darth Vader</td>8
            <td>9
                <a href="#">10
                    Ver detalhes11
                </a>12
            </td>13
        </tr>14
    {% endfor %}15
</tbody>16
Olha só que bacana: estamos dizendo para o Django "hey, cara, para cada visitante  que 
existir na lista todos_visitantes , repita essa estrutura de elementos <td> . Com isso já 
estamos executando o loop na lista todos_visitantes , mas ainda não estamos exibindo 
os valores referentes a cada visitante existente no banco de dados. Para fazer isso, vamos 

## Página 87

utilizar a sintaxe de chaves ({{  }} ) em conjunto com variável visitante  que criamos 
dentro da tag {% for %} .
Os atributos do visitante podem ser acessados utilizando a sintaxe 
visitante.nome_do_atributo . Se queremos exibir o nome completo do visitante, vamos 
utilizar visitante.nome_completo . Faremos o mesmo com os atributos CPF, horário de 
chegada, horário de autorização de entrada e morador responsável. Realizando as 
alterações para exibirmos os atributos, o código ﬁcará assim:
<tbody>1
    {% for visitante in todos_visitantes %}2
        <tr>3
            <td>{{ visitante.nome_completo }}</td>4
            <td>{{ visitante.cpf }}</td>5
            <td>{{ visitante.horario_chegada }}</td>6
            <td>{{ visitante.horario_autorizacao }}</td>7
            <td>{{ visitante.morador_responsavel }}</td>8
            <td>9
                <a href="#">10
                    Ver detalhes11
                </a>12
            </td>13
        </tr>14
    {% endfor %}15
</tbody>16
Agora quando atualizarmos a página, vamos visualizar as informações dos visitantes 
registrados através do Admin. Caso queira testar, ﬁque à vontade para registrar outros 
visitantes. Quando você acessar novamente http://127.0.0.1:8000/ e atualizar a página, os 
novos visitantes serão adicionados à tabela de forma automática! Bem bacana, não?

## Página 88

Capítulo 07
Criando tela para registro de novo visitante
Assim como quando registramos um novo visitante através do Admin, precisaremos de um 
formulário para inserir as informações. Por isso, vamos trabalhar agora na tela que será 
responsável por exibir um formulário e registrar o visitante em nosso banco de dados.
Vimos que uma view é um tipo de função dentro da aplicação que conecta a camada de 
modelo à camada de template e, geralmente, renderiza um template especíﬁco com 
informações buscadas no banco de dados. Até agora escrevemos apenas views que 
buscam informações e renderizam o template utilizando essas informações, mas agora 
vamos trabalhar em views que também salvam informações no banco de dados.
A próxima view que vamos escrever, chamada de registrar_visitante , terá a 
responsabilidade de exibir um formulário, identiﬁcar e tratar uma requisição do tipo POST, 
validar o formulário com base das informações enviadas na requisição e salvar o novo 
visitante no banco de dados. Não se assuste, você vai ver como o Django nos ajuda 
abstraindo a maior parte desses requisitos.
Criando view para registrar visitante
 
Como você já deve ter percebido, existe um roteiro a ser seguido quando vamos criar novas 
funcionalidades num sistema web com Django, sendo o primeiro passo a criação da 
função de view no arquivo views.py . Como nossa função diz respeito ao registro de um 
novo vistante, vamos trabalhar dentro do aplicativo visitantes.
Vamos abrir o arquivo views.py  do aplicativo visitantes e escrever a função de view 
registrar_visitante , que deverá renderizar o template registrar_visitante.html . 
Por hora, nossa view ﬁcará assim:
from django.shortcuts import render1
2

## Página 89

def registrar_visitante(request):3
4
    context = {}5
    6
    return render(request, "registrar_visitante.html", context)7
Assim como ﬁzemos anteriormente, vamos baixar o arquivo HTML e agora colocá-lo na 
pasta templates localizada na raiz do nosso projeto:
Iniciar o download registrar_visitante.zip - 2KB
Criando URL para mapear view
Quando criamos nossa primeira view, criamos também uma URL que é responsável por 
mapear a view para acessarmos ela através do navegador. Caso não se lembre do 
processo, não se preocupe, pois vamos repeti-lo agora.
Vamos abrir o arquivo urls.py  do nosso projeto e, abaixo da URL de nome index, 
utilizando a função path , vamos criar a URL de nome registrar_visitante que deverá 
mapear a função de view registrar_visitante . Não podemos nos esquecer de importar 
as views do aplicativo visitantes!
O arquivo urls.py  ﬁcará assim:
from django.urls import path1
from django.contrib import admin2
3
import usuarios.views4
import visitantes.views5
6
urlpatterns = [7
    # codigo acima omitido...8
    9
    path(10
        "",11
        usuarios.views.index,12
        name="index",13
    ),14

## Página 90

    15
    path(16
        "registrar-visitante/",17
        visitantes.views.registrar_visitante,18
        name="registrar_visitante",19
    )20
]21
Abra seu navegador e acesse http://127.0.0.1:8000/registrar-visitante/ para veriﬁcar se 
está tudo funcionando corretamente. Se sim, o template baixado será exibido no 
navegador.
Adaptando nossos templates para trabalhar com a 
template engine do Django
 
Temos agora duas views que renderizam dois templates diferentes e expõem 
funcionalidades diferentes: uma delas, que é a página inicial da dashboard, exibe os 
visitantes registrados, e a segunda deverá possibilitar o registro de novos visitantes. Antes 
de seguir adiante, vamos realizar algumas alterações em nossos templates para que 
possamos aproveitar melhor as funcionalidades do framework que estamos utilizando.
Além das funcionalidades que falamos e exploramos, a engine de templates do Django 
também nos dá a possibilidade de reaproveitarmos trechos de código contidos em outros 
templates. No nosso caso, se você observar os templates index.html  e 
registrar_visitante.html , vai notar que existem partes iguais nos dois templates e, 
para evitar isso, a engine de templates do Django nos fornece as tags {% extends %}  e 
{% block %} .
Criando o template base
Antes de tudo, vamos criar um arquivo com nome de base.html  na pasta templates e 
copiar o conteúdo do arquivo index.html  para ele. O objetivo do nosso template 
base.html  é armazenar a parte comum a todos os templates da dashboard. O que 
podemos chamar de parte central do nosso template, que é a parte que em um template 

## Página 91

exibe uma tabela e no outro um formulário, será trocada de acordo com a view acessada e 
as barras lateral e superior e o rodapé serão mantidos no template base.html . Por hora, 
vamos apenas copiar o conteúdo do arquivo index.html  para o arquivo base.html  e 
deixá-lo de lado.
Adaptando template index
Com o template base.html  criado, vamos fazer algumas adaptações em nosso template 
index.html  para garantir que ele seja exibido corretamente fazendo uso da engine de 
templates do Django. Apague todo o conteúdo existente no arquivo index.html  deixando 
apenas o conteúdo dentro do elemento HTML <div class="container-fluid"> . O 
arquivo index.html  ﬁcará assim:
<div class="container-fluid">1
    <div class="d-sm-flex align-items-center justify-content-between mb-4"2
        <h1 class="h3 mb-0 text-gray-800">{{ nome_pagina }}</h1>3
    </div>4
5
    <div class="row">6
        <div class="col-xl-3 col-md-6 mb-4">7
            <div class="card border-left-warning shadow h-100 py-2">8
                <div class="card-body">9
                    <div class="row no-gutters align-items-center">10
                        <div class="col mr-2">11
                            <div class="text-xs font-weight-bold text-warn12
                            <div class="h5 mb-0 font-weight-bold text-gray13
                        </div>14
                        15
                        <div class="col-auto">16
                            <i class="fas fa-user-lock fa-2x text-gray-30017
                        </div>18
                    </div>19
                </div>20
            </div>21
        </div>22
23
        <div class="col-xl-3 col-md-6 mb-4">24
            <div class="card border-left-primary shadow h-100 py-2">25
                <div class="card-body">26
                    <div class="row no-gutters align-items-center">27
                        <div class="col mr-2">28
                            <div class="text-xs font-weight-bold text-prim29
                            <div class="h5 mb-0 font-weight-bold text-gray30

## Página 92

                        </div>31
                        32
                        <div class="col-auto">33
                            <i class="fas fa-user-clock fa-2x text-gray-3034
                        </div>35
                    </div>36
                </div>37
            </div>38
        </div>39
40
        <div class="col-xl-3 col-md-6 mb-4">41
            <div class="card border-left-success shadow h-100 py-2">42
                <div class="card-body">43
                    <div class="row no-gutters align-items-center">44
                        <div class="col mr-2">45
                            <div class="text-xs font-weight-bold text-succ46
                            <div class="h5 mb-0 font-weight-bold text-gray47
                        </div>48
                        <div class="col-auto">49
                            <i class="fas fa-user-check fa-2x text-gray-3050
                        </div>51
                    </div>52
                </div>53
            </div>54
        </div>55
        56
        <div class="col-xl-3 col-md-6 mb-4">57
            <div class="card border-left-info shadow h-100 py-2">58
                <div class="card-body">59
                    <div class="row no-gutters align-items-center">60
                        <div class="col mr-2">61
                            <div class="text-xs font-weight-bold text-info 62
                            <div class="h5 mb-0 font-weight-bold text-gray63
                        </div>64
                        <div class="col-auto">65
                            <i class="fas fa-users fa-2x text-gray-300"></66
                        </div>67
                    </div>68
                </div>69
            </div>70
        </div>71
    </div>72
    73
    <div class="card shadow mb-4">74
        <div class="card-header py-3 d-sm-flex align-items-center justify-75
            <h6 class="m-0 font-weight-bold text-primary">Visitantes recen76
        </div>77
78
        <div class="card-body">79
            <div class="table-responsive">80
                <table class="table table-bordered">81

## Página 93

                    <thead>82
                        <th>Nome</th>83
                        <th>CPF</th>84
                        <th>Horário de chegada</th>85
                        <th>Horário da autorização</th>86
                        <th>Autorizado por</th>87
                        <th>Mais informações</th>88
                    </thead>89
90
                    <tbody>91
                        {% for visitante in todos_visitantes %}92
                            <tr>93
                                <td>{{ visitante.nome_completo }}</td>94
                                <td>{{ visitante.cpf }}</td>95
                                <td>{{ visitante.horario_chegada }}</td>96
                                <td>{{ visitante.horario_autorizacao }}</t97
                                <td>{{ visitante.morador_responsavel }}</t98
                                <td>99
                                    <a href="#">100
                                        Ver informações101
                                    </a>102
                                </td>103
                            </tr>104
                        {% endfor %}105
                    </tbody>106
                </table>107
            </div>108
        </div>109
    </div>110
</div>111
Com os templates devidamente separados, vamos trabalhar agora nas adaptações 
necessárias ao template index.html . O primeiro passo é inserirmos a tag 
{% extends %}  no início do nosso arquivo, que é quem dirá ao Django que o template em 
questão é uma extensão de outro. A tag {% extends %}  funciona de modo que 
precisamos identiﬁcar o template "pai" ou "mãe" que será utilizado na extensão. Isto é, 
neste caso, o template index.html  será extensão do template base.html , sendo este o 
"seu template pai ou mãe". Na primeira linha do arquivo index.html  insira o trecho 
{% extends "base.html" %} .
Além disto, precisamos também dizer ao Django qual trecho deverá ser utilizado para 
substituição. Faremos isso utilizando as tags {% block %}  e {% endblock %}  passando 
um nome a elas. Logo abaixo da tag {% extends "base.html" %}  vamos inserir a tag 

## Página 94

{% block conteudo %}  e ao ﬁnal do arquivo a tag {% endblock conteudo %} . Fazendo 
isso estamos deixando claro para o Django qual trecho deverá ser colocado no template 
base.html  quando acessarmos a view que renderiza o template index.html .  Nosso 
arquivo ﬁcará assim após as adaptações:
{% extends "base.html" %}1
2
{% block conteudo %}3
<div class="container-fluid">4
    <div class="d-sm-flex align-items-center justify-content-between mb-4"5
        <h1 class="h3 mb-0 text-gray-800">{{ nome_pagina }}</h1>6
    </div>7
8
    <div class="row">9
        <div class="col-xl-3 col-md-6 mb-4">10
            <div class="card border-left-warning shadow h-100 py-2">11
                <div class="card-body">12
                    <div class="row no-gutters align-items-center">13
                        <div class="col mr-2">14
                            <div class="text-xs font-weight-bold text-warn15
                            <div class="h5 mb-0 font-weight-bold text-gray16
                        </div>17
                        18
                        <div class="col-auto">19
                            <i class="fas fa-user-lock fa-2x text-gray-30020
                        </div>21
                    </div>22
                </div>23
            </div>24
        </div>25
26
        <div class="col-xl-3 col-md-6 mb-4">27
            <div class="card border-left-primary shadow h-100 py-2">28
                <div class="card-body">29
                    <div class="row no-gutters align-items-center">30
                        <div class="col mr-2">31
                            <div class="text-xs font-weight-bold text-prim32
                            <div class="h5 mb-0 font-weight-bold text-gray33
                        </div>34
                        35
                        <div class="col-auto">36
                            <i class="fas fa-user-clock fa-2x text-gray-3037
                        </div>38
                    </div>39
                </div>40
            </div>41
        </div>42

## Página 95

43
        <div class="col-xl-3 col-md-6 mb-4">44
            <div class="card border-left-success shadow h-100 py-2">45
                <div class="card-body">46
                    <div class="row no-gutters align-items-center">47
                        <div class="col mr-2">48
                            <div class="text-xs font-weight-bold text-succ49
                            <div class="h5 mb-0 font-weight-bold text-gray50
                        </div>51
                        <div class="col-auto">52
                            <i class="fas fa-user-check fa-2x text-gray-3053
                        </div>54
                    </div>55
                </div>56
            </div>57
        </div>58
        59
        <div class="col-xl-3 col-md-6 mb-4">60
            <div class="card border-left-info shadow h-100 py-2">61
                <div class="card-body">62
                    <div class="row no-gutters align-items-center">63
                        <div class="col mr-2">64
                            <div class="text-xs font-weight-bold text-info 65
                            <div class="h5 mb-0 font-weight-bold text-gray66
                        </div>67
                        <div class="col-auto">68
                            <i class="fas fa-users fa-2x text-gray-300"></69
                        </div>70
                    </div>71
                </div>72
            </div>73
        </div>74
    </div>75
    76
    <div class="card shadow mb-4">77
        <div class="card-header py-3 d-sm-flex align-items-center justify-78
            <h6 class="m-0 font-weight-bold text-primary">Visitantes recen79
        </div>80
81
        <div class="card-body">82
            <div class="table-responsive">83
                <table class="table table-bordered">84
                    <thead>85
                        <th>Nome</th>86
                        <th>CPF</th>87
                        <th>Horário de chegada</th>88
                        <th>Horário da autorização</th>89
                        <th>Autorizado por</th>90
                        <th>Mais informações</th>91
                    </thead>92
93

## Página 96

                    <tbody>94
                        {% for visitante in todos_visitantes %}95
                            <tr>96
                                <td>{{ visitante.nome_completo }}</td>97
                                <td>{{ visitante.cpf }}</td>98
                                <td>{{ visitante.horario_chegada }}</td>99
                                <td>{{ visitante.horario_autorizacao }}</t100
                                <td>{{ visitante.morador_responsavel }}</t101
                                <td>102
                                    <a href="#">103
                                        Ver informações104
                                    </a>105
                                </td>106
                            </tr>107
                        {% endfor %}108
                    </tbody>109
                </table>110
            </div>111
        </div>112
    </div>113
</div>114
{% endblock conteudo %}115
Adaptando template base
Quando criamos o template base.html , copiamos o conteúdo de index.html  para ele e 
o deixamos de lado, mas agora é hora de trabalharmos nele. O que temos que fazer é 
substituir o elemento HTML <div class="container-fluid">  pelas tags 
{% block conteudo %}  e {% endblock conteudo %}.  O template base.html  ﬁcará 
assim:
<!DOCTYPE html>1
2
{% load static %}3
4
<html lang="pt-br">5
    <head>6
        <meta charset="utf-8">7
        <meta http-equiv="X-UA-Compatible" content="IE=edge">8
        <meta name="viewport" content="width=device-width, initial-scale=19
10
        <title>Controle de Visitantes | Django Framework na prática</title11
        12
        <link href="https://fonts.googleapis.com/css?family=Nunito:200,20013

## Página 97

        14
        <link href="{% static 'css/sb-admin-2.min.css' %}" rel="stylesheet15
        <link href="{% static 'vendor/fontawesome-free/css/all.min.css' %}16
    </head>17
18
    <body id="page-top">19
        <div id="wrapper">20
            <ul class="navbar-nav bg-gradient-primary sidebar sidebar-dark 21
                <a class="sidebar-brand d-flex align-items-center justify-22
                    <div class="sidebar-brand-icon rotate-n-15">23
                        <i class="fas fa-user-shield"></i>24
                    </div>25
                    26
                    <div class="sidebar-brand-text">Controle de Visitantes27
                </a>28
                29
                <hr class="sidebar-divider my-0">30
                31
                <li class="nav-item">32
                    <a class="nav-link" href="#">33
                        <i class="fas fa-home"></i>34
                        <span>Início</span>35
                    </a>36
                </li>37
                38
                <hr class="sidebar-divider">39
            </ul>40
41
            <div id="content-wrapper" class="d-flex flex-column">42
                <div id="content">43
                    <nav class="navbar navbar-expand navbar-light bg-white 44
                        <button id="sidebarToggleTop" class="btn btn-link 45
                            <i class="fa fa-bars"></i>46
                        </button>47
                        48
                        <ul class="navbar-nav ml-auto">49
                            <li class="nav-item dropdown no-arrow">50
                                <a class="nav-link dropdown-toggle" href="51
                                    <span class="mr-2 d-none d-lg-inline t52
                                        <i class="fas fa-cog"></i>53
                                    </span>54
                                </a>55
                                56
                                <div class="dropdown-menu dropdown-menu-ri57
                                    <a class="dropdown-item" href="#" data58
                                        <i class="fas fa-sign-out-alt fa-s59
                                        Sair60
                                    </a>61
                                </div>62
                            </li>63
                        </ul>64

## Página 98

                    </nav>65
66
                    {% block conteudo %} {% endblock conteudo %}67
68
                    <footer class="sticky-footer bg-white">69
                        <div class="container my-auto">70
                            <div class="copyright text-center my-auto">71
                                <span>Copyright © Django framework na prát72
                            </div>73
                        </div>74
                    </footer>75
                </div>76
            </div>77
78
            <div class="modal fade" id="logoutModal" tabindex="-1" role="d79
                <div class="modal-dialog" role="document">80
                    <div class="modal-content">81
                        <div class="modal-header">82
                            <h5 class="modal-title" id="ModalLabel">Você r83
                            84
                            <button class="close" type="button" data-dismi85
                                <span aria-hidden="true">×</span>86
                            </button>87
                        </div>88
                        89
                        <div class="modal-body">Selecione "sair" se realme90
                        91
                        <div class="modal-footer">92
                            <button class="btn btn-secondary" type="button93
                            <a class="btn btn-primary" href="#">Sair</a>94
                        </div>95
                    </div>96
                </div>97
            </div>98
        </div>99
100
        <script src="{% static 'vendor/jquery/jquery.min.js' %}"></script>101
        <script src="{% static 'vendor/bootstrap/js/bootstrap.bundle.min.j102
        <script src="{% static 'js/sb-admin-2.min.js' %}"></script>103
    </body>104
</html>105
Adaptando template registrar_visitante
Faremos o mesmo que ﬁzemos com o template index.html , mas agora deixando apenas 
o conteúdo existente dentro do elemento HTML <div class="container">  e inserindo as 

## Página 99

tags {% extends "base.html" %} , {% block conteudo %}  e {% endblock conteudo %} 
. O template registrar_visitante.html  ﬁcará assim:
{% extends "base.html" %}1
2
{% block conteudo %}3
<div class="container">4
    <div class="d-sm-flex align-items-center justify-content-between mb-4"5
        <h1 class="h3 mb-0 text-gray-800">{{ nome_pagina }}</h1>6
    </div>7
8
    <div class="card shadow mb-4">9
        <div class="card-body">10
            <h4 class="mb-3 text-primary">11
                Formulário para registro de novo visitante12
            </h4>13
14
            <form method="post">15
                <div class="form-row">16
                    <p class="ml-2">Aqui deveria ter um formulário</p>17
                </div>18
19
                <div class="text-right">20
                    <button class="btn btn-primary" type="submit">21
                        <span class="text">Registrar visitante</span>22
                    </button>23
                </div>24
            </form>25
        </div>26
    </div>27
</div>28
{% endblock %}29
Caso preﬁra, você pode fazer download da pasta templates com as alterações realizadas 
até aqui clicando no link abaixo:
Iniciar o download templates.zip - 3KB
Agora que adaptamos todos os nossos templates, vamos voltar ao desenvolvimento da 
view responsável por registrar nossos visitantes.

## Página 100

Capítulo 08
Trabalhando com formulários no Django
Manipular formulários não é uma tarefa tão fácil. Se observarmos o Admin do Django, 
podemos notar que existem diversos tipos de dados e maneiras diferentes de tratar e 
renderizar esses dados. Além disso, existe a estrutura HTML do formulário a ser 
renderizada no template, esse formulário deve validar as informações que são enviadas 
pelo usuário, salvar as informações ou exibir uma mensagem para o usuário caso os 
dados estejam inválidos, etc. Para simpliﬁcar nosso trabalho, o Django fornece 
ferramentas para automatizar e simpliﬁcar esse processo, garantindo também segurança 
para implementar as funcionalidades necessárias.
Um formulário pode ser deﬁnido como um conjunto de elementos dentro do elemento 
HTML <form>  que permitem que o usuário insira textos, números, escolha opções e, ao 
ﬁm, envie essas informações de volta para o servidor. No contexto da nossa aplicação web,
um formulário pode signiﬁcar também o formulário que a classe Form  do Django nos 
disponibiliza, que é quem faz toda mágica por nós. Da mesma maneira que uma classe 
Model  descreve toda estrutura lógica de um objeto, seu comportamento e a maneira 
como suas partes são representadas para nós, uma classe Form  descreve um formulário 
e determina como ele funciona e se parece.
Criando formulário para registro de visitante
 
Assim como outras camadas importantes da arquitetura do nosso projeto, os formulários 
também devem ter um arquivo próprio para eles, mas que, neste caso, precisamos criar: o 
arquivo forms.py . Vamos abrir a pasta do nosso aplicativo visitantes e criar o arquivo 
forms.py . Após criarmos o arquivo, vamos abri-lo e importar o pacote forms do django. 
Ficará assim:
from django import forms

## Página 101

De forma semelhante aos campos de uma classe Model  que são mapeados para os 
campos do banco de dados, os campos de uma classe Form  são mapeados para 
elementos HTML. É exatamente assim que toda a mágica do Admin do Django funciona: 
mapeando os campos da sua classe Model , criando classes Form  e renderizando esses 
campos como elementos HTML. Muito bacana, não?
Para quando queremos mapear automaticamente os campos de uma classe Model , o 
Django nos permite utilizar a classe ModelForm.  Tudo que precisamos fazer é deﬁnir uma 
subclasse de ModelForm  e depois identiﬁcarmos a classe Model  a ser utilizada. Sendo 
assim, vamos também importar a classe Visitante e depois deﬁnir uma subclasse de 
forms.ModelForm  de nome VisitanteForm . O arquivo forms.py  ﬁcará assim:
from django import forms1
from visitantes.models import Visitante2
3
class VisitanteForm(forms.ModelForm):4
    class Meta:5
        model = Visitante6
        fields = "__all__"7
Criamos a subclasse de forms.ModelForm  chamada VisitanteForm , que é quem 
representa nosso formulário e deﬁnimos a classe interna Meta  para explicitarmos qual 
classe Model  deve ser utilizada (model = Visitante ) e quais campos devem ser 
renderizados (fields = "__all__" ). Por hora, vamos utilizar a string  "__all__"  para 
renderizarmos todos os campos.
Renderizando nosso formulário automaticamente
 
Agora que deﬁnimos a classe que vai representar nosso formulário, podemos partir para a 
segunda etapa, que é renderizar esse formulário diretamente no HTML. Para isso, vamos 
trabalhar no arquivo views.py  do aplicativo visitantes, começando pela importação do 
formulário. Após isso, vamos criar uma variável de nome form  que será igual à uma 

## Página 102

instância da classe VisitanteForm  e passá-la dentro da variável context  da view 
registrar_visitante . O arquivo ﬁcará assim: 
from django.shortcuts import render1
from visitantes.forms import VisitanteForm2
3
def registrar_visitante(request):4
5
    form = VisitanteForm()6
    7
    context = {8
        "nome_pagina": "Registrar visitante",9
        "form": form,10
    }11
12
    return render(request, "registrar_visitante.html", context)13
Apenas com as alterações realizadas, já podemos trabalhar no template 
registrar_visitante.html  para que o formulário seja renderizado de forma automática. 
Vamos abrir o arquivo registrar_visitante.html  dentro da pasta templates e procurar 
pelo elemento HTML <form> . Substitua todo o conteúdo existente dentro do elemento 
pela variável {{ form }}  e acesse http://127.0.0.1:8000/registrar-visitante/ em seu 
navegador. O arquivo registrar_visitante.html  ﬁcará assim:
<!-- codigo acima omitido -->1
<div class="card-body">2
    <h4 class="mb-3 text-primary">3
        Formulário para registro de novo visitante4
    </h4>5
6
    <div class="container">7
        {{ form }}8
    </div>9
</div>10
<!-- codigo abaixo omitido -->11

## Página 103

Deﬁnimos no contexto também a variável nome_pagina , mas desta vez, como 
"Registrar visitante". Note como o Django reconhece o valor da variável de 
acordo com cada view e altera o valor no template base.html 
Melhorando a exibição do nosso formulário
 
Quando o assunto é criar formulários, o Django faz esse papel muito bem, além de prover 
uma funcionalidade segura e estável. Veja bem, com menos de 10 linhas conseguimos 
criar e renderizar um formulário que se adapta totalmente às necessidades do nosso 
modelo. Desta forma, é altamente recomendado utilizar os formulários do Django para 
automatizar nosso trabalho.
O Django faz muito bem o trabalho que se propõe a fazer: preparar e reestruturar os dados 
para renderização, criar o formulário para receber os dados e ainda processar e validar 
esses dados, mas quando precisamos renderizar essas informações no formato HTML de 
modo que ﬁque mais atrativo para o usuário, faltam algumas opções. É aí que entra o 
django-widget-tweaks, um pacote Python muito interessante e útil disponibilizado pela 
comunidade para nos ajudar na renderização dos nossos formulários.
Estilizando nosso formulário com django-widget-tweaks
 
O django-widget-tweaks nos ajuda tornando mais fácil o processo de adicionar atributos e 
classes aos campos de um formulário Django, aﬁm de aplicar classes personalizadas para 
alterar aparência ou comportamento dos elementos, quando necessário. Como estamos 
utilizando um tema que utiliza o Bootstrap como base, podemos também utilizar suas 
classes CSS para alterar a aparência dos elementos.
Isso resolve o problema do nosso formulário não estar sendo exibido de maneira atrativa 
para o usuário. Isso porque o Django renderiza um formulário HTML simples, sem 
adicionar classes para alterar o estilo dos elementos que compõem esse formulário. Sendo 
assim, utilizaremos o django-widget-tweaks para adicionar a classe form-control  aos 

## Página 104

campos do nosso formulário, e assim aplicar as características descritas no arquivo de 
estilização (CSS) do tema utilizado.
Como instalar
Para instalar o django-widget-tweaks utilizaremos nosso já conhecido gerenciador de 
pacotes: o pip . Para instalar vamos utilizar o seguinte comando:
(env)$ pip install django-widget-tweaks
Caso ocorra bem tudo, você terá instalado o django-widget-tweaks em seu ambiente 
virtual. Feito isso, também vamos adicionar o pacote à variável INSTALLED_APPS  do nosso
arquivo de conﬁgurações. Para uma melhor organização, vamos criar uma lista separada 
da lista dos nossos aplicativos.
# código acima omitido1
2
INSTALLED_APPS += [3
    "widget_tweaks",4
]5
6
INSTALLED_APPS += [7
    "usuarios",8
    "porteiros",9
    "visitantes",10
]11
12
# código abaixo omitido13
Utilizamos três variáveis de mesmo nome e as incrementamos pois assim 
separamos os aplicativos do Django (primeira), os pacotes Python instalados 
(segunda) e os aplicativos criados por nós (terceira). Lembre-se que é 
necessário utilizar o operador +=  quando queremos incrementar os valores 
existentes na variável

## Página 105

Importando no template
Agora que instalamos e registramos o pacote em nosso arquivo de conﬁgurações, temos 
que utilizar a tag {% load widget_tweaks %}  sempre que precisarmos utilizar as 
funcionalidades do pacote num determinado template. Vamos adicionar a tag logo abaixo 
da primeira linha do template registrar_visitante.html . O arquivo ﬁcará assim:
{% extends "base.html" %}1
2
{% load widget_tweaks %}3
4
<!-- código abaixo omitido -->5
Utilizando o render_ﬁeld
Existem duas maneiras que o django-widget-tweaks nos permite utilizar suas 
funcionalidades, mas utilizaremos a tag personalizada {% render_field %} , com ela 
conseguimos descrever nossos campos de forma bem parecida com o HTML5.
Vamos abrir o arquivo registrar_visitante.html  e substituir a variável {{ form }}  
pelo elemento <form method="post">  abaixo e seu conteúdo. O código ﬁcará assim:
<!-- codigo acima omitido -->1
<div class="card-body">2
    <h4 class="mb-3 text-primary">3
        Formulário para registro de novo visitante4
    </h4>5
6
    <p class="mb-5 ml-1">7
        <small>8
            O asterisco (*) indica que o campo é obrigatório9
        </small>10
    </p>11
    12
    <form method="post">13
        <div class="form-row">14
            {% csrf_token %}15
16
            {% for field in form %}17

## Página 106

                <div class="form-group col-md-12">18
                    <label>{{ field.label }} {% if field.field.required %} 19
                    {% render_field field placeholder=field.label class="f20
                </div>21
            {% endfor %}22
        </div>23
        24
        <div class="text-right">25
            <button class="btn btn-primary" type="submit">26
                <span class="text">Registrar visitante</span>27
            </button>28
        </div>29
    </form>30
</div>31
<!-- codigo abaixo omitido -->32
Vamos adicionar também um trecho de código HTML com um aviso sinalizando que o 
asterisco (*) acima dos campos do formulário indica que o campo é obrigatório.
A tag {% csrf_token %}  fornece proteção para nossa aplicação, de modo a 
impedir que sites mal intencionados enviem requisições para ela. Caso a gente 
não coloque essa tag dentro dos nossos formulários, o Django não aceitará a 
requisição enviada e mostrará um erro pois não vai identiﬁcar a requisição 
como segura
Logo abaixo da tag {% csrf_token %} , estamos utilizando novamente a tag {% for %}  
para realizar um loop, mas desta vez na variável form . Quando realizamos um loop em 
nosso formulário, conseguimos acessar seus campos, e é exatamente o que precisamos 
fazer: executar um loop e acessar as informações de cada campo para que possamos 
passá-las para a tag {% render_field %}  fazer o trabalho de renderização destes 
campos.
Aqui temos uma novidade, a utilização da tag {% if %} . Uma estrutura 
condicional que pode ser utilizada em templates. O que estiver dentro dela só 
será exibido caso o resultado da expressão seja verdadeiro. Ou seja, quando 

## Página 107

existem mensagens e a variável messages  está deﬁnida, exibimos o trecho 
HTML
Para cada campo (variável ﬁeld) em nosso formulário, criamos a estrutura padrão para 
campos de um formulário do nosso tema. Acessamos também a propriedade label   para
exibir o nome e o placeholder do input  e passamos a variável que representa o campo 
para a tag {% render_field %} . Veja como ﬁcará estrutura de cada campo:
<div class="form-group col-md-12">1
    <label>{{ field.label }} {% if field.field.required %} * {% endif %}</2
    {% render_field field placeholder=field.label class="form-control" %}3
</div>4
Note que deﬁnimos também os atributos placeholder=field.label  e 
class="form-control" , além de veriﬁcarmos se o campo é obrigatório e, caso seja, 
colocamos um asterisco (*) ao lado do nome do campo. Acesse a página e veja na prática 
como o layout do nosso formulário melhorou e muito!

## Página 108

Capítulo 09
Preparando view para receber requisição do tipo POST
Agora que cuidamos da usabilidade do nosso formulário, podemos seguir com as outras 
partes da nossa view. Até o momento, apenas criamos a variável que representa o 
formulário e a passamos no contexto, o que faremos agora é preparar nossa view para 
receber os dados que serão enviados na requisição.
Conhecendo o objeto request
Você já deve ter notado que sempre que criamos uma view, precisamos que ela receba a 
variável request  como argumento. Isso porque, quando falamos do protocolo que 
sustenta a web, o HTTP, requisições são o que movimentam toda a estrutura. Quando 
acessamos uma página web estamos enviando uma requisição do tipo GET . Isso tudo 
acontece em questão de segundos e por baixo dos panos, nos ﬁos que conectam a web.
A variável request  é uma representação da requisição que é enviada à view acessada e 
contém diversas informações como usuário logado, método HTTP utilizado, navegador e 
sistema operacional, dentre outras. No momento, nos interessa o método da requisição e o 
corpo que é enviado. 
Para prepararmos a view para receber as informações da requisição, vamos adicionar um 
if  abaixo da linha form = VisitanteForm()  para veriﬁcar se o método da requisição é 
do tipo POST . Podemos fazer isso dessa forma:
from django.shortcuts import render1
from visitantes.forms import VisitanteForm2
3
def registrar_visitante(request):4
5
    form = VisitanteForm()6
    7
    if request.method == "POST":8
        print("o método é post")9
    10
    context = {11

## Página 109

        "nome_pagina": "Registrar visitante",12
        "form": form,13
    }14
15
    return render(request, "registrar_visitante.html", context)16
O método POST  é utilizado sempre que precisamos enviar informações para o 
servidor. No nosso caso, por exemplo, queremos enviar as informações de um 
novo visitante a ser registrado e fazemos isso através do formulário HTML
Agora que veriﬁcamos se o método da requisição enviada é do tipo POST , vamos reutilizar 
a variável form , agora atribuindo a ela outra instância do formulário VisitanteForm() , 
mas agora passando o corpo da requisição à classe, e utilizar o método is_valid()  do 
formulário para validar as informações. O código ﬁcará o seguinte:
from django.shortcuts import render1
from visitantes.forms import VisitanteForm2
3
def registrar_visitante(request):4
5
    form = VisitanteForm()6
    7
    if request.method == "POST":8
        form = VisitanteForm(request.POST)9
        10
        if form.is_valid():11
            form.save()12
    13
    context = {14
        "nome_pagina": "Registrar visitante",15
        "form": form,16
    }17
18
    return render(request, "registrar_visitante.html", context)19
Para passar o corpo da requisição para o formulário, basta utilizarmos a propriedade POST
do objeto request  e passá-lo como argumento ao criarmos a nova instância do 

## Página 110

formulário, como feito na linha 9 (form = VisitanteForm(request.POST) ). Feito isso, 
validamos as informações com o método is_valid()  e salvamos o formulário utilizando 
o método save() .
Conhecendo um pouco mais dos formulários
 
Ao acessarmos a página, podemos notar que todos os campos do modelo estão sendo 
exibidos no formulário, e não é isso que queremos, pois algumas das informações devem 
ser preenchidas mediante autorização de moradores e dependem outros eventos.
Para especiﬁcar os campos que devem ser exibidos e utilizados no formulário, vamos 
voltar ao arquivo forms.py  e alterar o atributo fields  da classe Meta  do nosso 
formulário. Abra o arquivo e substitua a string "__all__"  por uma lista com os nomes 
dos campos que vamos exibir. O atributo fields  ﬁcará assim:
from django import forms1
from visitantes.models import Visitante2
3
class VisitanteForm(forms.ModelForm):4
    class Meta:5
        model = Visitante6
        fields = [7
            "nome_completo", "cpf", "data_nascimento",8
            "numero_casa", "placa_veiculo",9
        ]10
Ao voltar para a página, vamos notar que agora apenas os campos que estão na lista 
fields  da classe Meta  estão sendo exibidos.
Tratando problema com atributo nulo
Quando criamos a classe modelo Visitante , falamos sobre o atributo registrado_por  
ser do tipo ForeignKey , um tipo de campo que cria um relacionamento entre as classes 
Visitante  e Porteiro . Olhando a classe VisitanteForm , podemos notar que o 

## Página 111

atributo não é colocado nos campos do formulário (fields ), mesmo este sendo uma 
informação obrigatória em nosso modelo. Se tentarmos adicionar um visitante por meio do
formulário, o Django apresentará um erro nos informando que o atributoregistrado_por  
do modelo não pode ser nulo.
Para resolver o problema, o que vamos fazer é possibilitar que o campo seja preenchido de 
maneira automática. Isto é, o campo receberá o valor referente ao porteiro que está logado 
na dashboard no momento do cadastro.
Para fazer isso, antes de salvar o formulário vamos deﬁnir diretamente um valor para o 
atributo registrado_por  na função de view. Vamos abrir o arquivo views.py  e criar 
uma variável para receber o retorno do método save  do formulário. Esse método aceita 
também um argumento opcional de nome commit , que quando deﬁnido como False , 
retorna uma instância do modelo utilizado no formulário que ainda não foi gravada no 
banco de dados. Isso é bem útil para quando queremos executar um processamento 
personalizado antes de salvar o objeto ou até mesmo utilizar outros métodos do modelo. O 
código vai ﬁcar assim:
from django.shortcuts import render1
from visitantes.forms import VisitanteForm2
3
def registrar_visitante(request):4
5
    form = VisitanteForm()6
    7
    if request.method == "POST":8
        form = VisitanteForm(request.POST)9
        10
        if form.is_valid():11
            visitante = form.save(commit=False)12
13
            visitante.registrado_por = request.user.porteiro14
            15
            visitante.save()    16
        17
    context = {18
        "nome_pagina": "Registrar visitante",19
        "form": form,20
    }21
22
    return render(request, "registrar_visitante.html", context)23

## Página 112

Agora, ao invés de salvarmos o formulário diretamente, estamos guardando o resultado do 
método save  com o argumento commit=False , deﬁnindo um valor para o atributo 
registrado_por  diretamente e salvando o objeto através da variável visitante . 
Somente no momento em que chamamos o método visitante.save()  que as alterações 
são registradas no banco de dados.
Lembra que falamos que a variável request  guarda algumas informações da 
requisição, como usuário logado e método utilizado? Pois bem, conseguimos 
pegar informações do usuário logado acessando a propriedade user  da 
variável request  (request.user ). No nosso caso, ainda estamos acessando 
uma outra propriedade do usuário, a propriedade porteiro  (
request.user.porteiro ).
Isso acontece devido à funcionalidade de acesso entre os modelos que o 
Django disponibiliza. Assim como podemos acessar porteiro.usuario , 
deﬁnido diretamente como atributo do modelo, podemos fazer o mesmo para o 
inverso da relação.
Feito isso, vamos apenas importar mais um dos shortcuts  do Django, além do render , 
que é o redirect . O que ele faz é exatamente redirecionar a view para uma URL que 
quisermos. Vamos utilizá-lo para evitar que os mesmos dados sejam enviados mais de 
uma vez ao nosso servidor. Sempre que um formulário for enviado e as informações forem 
salvas no banco de dados, vamos redirecionar a página. Para isso, basta importar o 
redirect  ao lado do render  e utilizá-lo passando o nome da URL para onde queremos 
mandar o usuário. O código ﬁcará assim:
from django.shortcuts import render, redirect1
from visitantes.forms import VisitanteForm2
3
def registrar_visitante(request):4
5
    form = VisitanteForm()6
    7
    if request.method == "POST":8
        form = VisitanteForm(request.POST)9

## Página 113

        10
        if form.is_valid():11
            visitante = form.save(commit=False)12
13
            visitante.registrado_por = request.user.porteiro14
            visitante.save()15
            16
            return redirect("index")17
        18
    context = {19
        "nome_pagina": "Registrar visitante",20
        "form": form,21
    }22
23
    return render(request, "registrar_visitante.html", context)24
Agora vamos voltar à página http://127.0.0.1:8000/registrar-visitante/ e registrar um 
visitante. O visitante deverá ser registrado e a requisição redirecionada para a página inicial
da dashboard.
O visitante registrado deverá estar listado na tabela de visitantes recentes
Exibindo uma mensagem para o usuário ao cadastrar novo 
visitante
 
Agora que o formulário está sendo exibido e funcionando corretamente, inclusive salvando 
os visitantes em nosso banco de dados, vamos melhorar um pouco a usabilidade da nossa
dashboard. Sempre que o sistema ﬁnaliza uma ação solicitada pelo usuário, é interessante 
que seja dado um feedback visual para facilitar o entendimento a respeito do que 
aconteceu. Desta forma, o que faremos agora é trabalhar na view para que, quando o 
visitante for registrado, uma mensagem seja exibida dizendo algo como "hey, cara, o 
visitante foi registrado com sucesso!".
Conhecendo o Django messages

## Página 114

O Django já nos disponibiliza o módulo messages  para resolver isso. Toda a conﬁguração 
necessária para o funcionamento de suas funcionalidades já vêm por padrão quando 
criamos um novo projeto Django, então o que precisamos fazer é apenas inserir o código 
from django.contrib import messages  para importar as funcionalidades e utilizá-las em 
nossas views. Vamos colocá-lo na primeira linha e o início do arquivo views.py  do 
aplicativo visitantes ﬁcará assim:
from django.contrib import messages1
from django.shortcuts import render, redirect2
from visitantes.forms import VisitanteForm3
4
# código abaixo omitido5
Com o módulo importado em nossa view, podemos utilizá-lo tranquilamente. Vamos 
adicionar uma mensagem de sucesso logo após a linha que salva a instância do visitante (
visitante.save() ) utilizando o método success  do módulo messages  e passando a 
ele a request  e um texto para ser exibido. O arquivo views.py  ﬁcará assim:
from django.contrib import messages1
from django.shortcuts import render, redirect2
from visitantes.forms import VisitanteForm3
4
def registrar_visitante(request):5
6
    form = VisitanteForm()7
    8
    if request.method == "POST":9
        form = VisitanteForm(request.POST)10
        11
        if form.is_valid():12
            visitante = form.save(commit=False)13
14
            visitante.registrado_por = request.user.porteiro15
16
            visitante.save()17
            18
            messages.success(19
                request,20
                "Visitante registrado com sucesso"21
            )22
            23

## Página 115

            return redirect("index")24
        25
    context = {26
        "nome_pagina": "Registrar visitante",27
        "form": form,28
    }29
30
    return render(request, "registrar_visitante.html", context)31
Alterando o template para exibir as mensagens
Nossa view para registro de visitantes está completa: estamos exibindo o formulário 
corretamente, veriﬁcando quando ocorre uma requisição do tipo POST, validando as 
informações enviadas, deﬁnindo automaticamente o porteiro que registrou o visitante, 
exibindo uma mensagem e ainda redirecionamos a requisição quando ﬁnalizamos todo o 
processo com sucesso. Ufa! É tanta coisa que ﬁcou até difícil de listar.
Com tudo isso feito, temos agora que disponibilizar um lugar em nosso template para que 
a mensagem seja exibida, como um alerta mesmo. Como estamos direcionando nosso 
usuário para a página inicial da dashboard, faz sentido que a gente coloque a mensagem 
no template index.html , pelo menos por hora.
Vamos abrir o template index.html  e, logo acima do primeiro elemento 
<div class="row"> do arquivo, vamos inserir o seguinte trecho de código:
{% if messages %}1
    {% for message in messages %}2
        <div class="alert alert-success" role="alert">3
            {{ message }}4
        </div>5
    {% endfor %}6
{% endif %}7
O módulo de mensagens do Django também nos disponibiliza uma variável chamada 
messages  que pode ser acessada nos templates. Com ela, conseguimos veriﬁcar se 
existem mensagens e, por meio de um loop, veriﬁcar as informações de cada mensagem. É 
o que estamos fazendo, primeiro veriﬁcamos se existem mensagem ({% if messages %} 

## Página 116

), caso positivo, nós executamos um loop e acessamos a mensagem utilizando a variável 
criada no loop ({{ message }} ).
Agora você pode cadastrar mais um visitante e ver a mensagem de sucesso sendo exibida!
Tratando possíveis erros em nosso formulário
 
Nossa mensagem de sucesso já está sendo exibida corretamente, mas o que acontece se 
ocorrer algum erro e os dados enviados não forem aceitos? Não podemos deixar que a 
aplicação pare e precisamos indicar para o usuário que os dados que ele inseriu estão 
incorretos.
Como nosso formulário de registro de visitante está no arquivo 
registrar_visitante.html , trabalharemos nele. Logo acima do elemento 
<form method="post"> , vamos inserir o seguinte trecho de código:
{% if form.errors %}1
    {% for field in form %}2
        {% if field.errors %}3
            {% for error in field.errors %}4
                <div class="alert alert-warning" role="alert">5
                    {{ error }}6
                </div>7
            {% endfor %}8
        {% endif %}9
    {% endfor %}10
{% endif %}11
A estrutura HTML é bem parecida com a utilizada para a mensagem de sucesso, mas com 
algumas pequenas diferenças. Mais uma vez, utilizaremos as tags {% if %}  e 
{% for %} . Primeiro vamos veriﬁcar se existem erros no formulário (
{% if form.errors %} ) e, caso verdadeiro, realizar um loop nos seus campos (
{% for field in form %} ). Desta vez, veriﬁcamos também se existem erros em cada 
campo ({% if field.errors %} ) e executamos um loop nesses erros (
{% for error in field.errors %} ), caso existam. 

## Página 117

Deixando nossas mensagens de erro mais claras
Um último detalhe para melhorarmos ainda mais a experiência do usuário ao utilizar nossa 
dashboard é certamente melhorar os textos das mensagens que são exibidas para o 
usuário em caso de erro. Muito mais que informar que ocorreu um erro, essas mensagens 
devem direcionar o usuário para o correto preenchimento das informações.
Para fazer isso, vamos atuar diretamente no arquivo forms.py  do aplicativo visitantes. O 
que faremos é adicionar o atributo error_messages  à classe Meta  da classe 
VisitanteForm , logo abaixo de fields .
O error_messages  é um dicionário que deve conter chaves com os nomes dos campos do
modelo. Desta forma, cada valor do dicionário error_messages  representa um campo do 
formulário e é também um dicionário, mas que, desta vez, recebe como chave os tipos de 
erros que podem acontecer nos formulários do Django seguido da mensagem a ser exibida 
para cada erro. Por hora utilizaremos os tipos required , que funciona para quando o 
campo não é preenchido e invalid , para quando o formato da informação enviada é 
inválido.
Nosso formulário, a classe VisitanteForm , ﬁcará assim:
class VisitanteForm(forms.ModelForm):1
    class Meta:2
        model = Visitante3
        fields = [4
            "nome_completo", "cpf", "data_nascimento",5
            "numero_casa", "placa_veiculo",6
        ]7
        error_messages = {8
            "nome_completo": {9
                "required": "O nome completo do visitante é obrigatório pa10
            },11
            "cpf": {12
                "required": "O CPF do visitante é obrigatório para o regis13
            },14
            "data_nascimento": {15
                "required": "A data de nascimento do visitante é obrigatór16
                "invalid": "Por favor, informe um formato válido para a da17
            },18
            "numero_casa": {19

## Página 118

                "required": "Por favor, informe o número da casa a ser vis20
            }21
        }22

## Página 119

Capítulo 10
Criando tela para exibir informações de visitante
Seguindo as especiﬁcações que recebemos do cliente, sabemos que existe a necessidade 
de visualização das informações do visitante na dashboard. Sendo assim, é necessário 
que a gente trabalhe para que seja possível buscar as informações de cada visitante 
registrado e exibir essas informações em um template à parte, aﬁm de mostrar mais 
detalhes de cada visitante.
Se você observar a tabela que lista os visitantes recentes na página inicial da dashboard, 
vai notar que existe um link para ver informações detalhadas de cada visitante. O que 
vamos fazer é desenvolver a view que vai buscar a informação de um visitante por vez e 
exibir essas informações de forma estruturada em um template HTML.
Criando a view
 
Como já sabemos, começaremos a trabalhar na funcionalidade pela função de view, no 
arquivo views.py . Abaixo da função registrar_visitante() , vamos criar a função 
informacoes_visitante() .
Essa função de view terá uma pequena diferença com relação à função 
registrar_visitante() , desta vez, além do argumento request , vamos também 
receber um argumento de nome id , que representará o id  do visitante a ser buscado 
em nosso banco de dados. É assim que vamos identiﬁcar qual visitante devemos buscar.
Já vamos aproveitar para criar a view e deixar algumas coisas prontas, como a variável 
context  e o retorno renderizando o template informacoes_visitante.html , que ainda 
vamos criar. Por hora, nossa função informacoes_visitante()  ﬁcará assim:
# código acima omitido1
2
def informacoes_visitante(request, id):3

## Página 120

    4
    context = {5
        "nome_pagina": "Informações de visitante",6
    }7
    8
    return render(request, "informacoes_visitante.html", context)9
Conhecendo o atalho get_model_or_404
Agora que nossa view está escrita e recebe um id , precisamos buscar o visitante em 
nosso banco de dados utilizando esse id . Existem várias formas de fazer isso, mas 
vamos utilizar o atalho get_model_or_404()  do Django. Para utilizá-lo, temos que passar 
uma classe modelo a ser utilizada na busca e o parâmetro pelo qual queremos buscar (em 
nosso caso, utilizaremos o id  e, por isso, vamos passá-lo como segundo argumento da 
função get_model_or_404() ).
Antes de tudo, claro, vamos importar a função get_model_or_404()  em nossa view 
juntamente com a classe modelo Visitante , pois também precisaremos dela. A função 
get_model_or_404()  está localizada no mesmo pacote que as funções render  e 
redirect , desta forma, vamos alterar as primeiras linhas do nosso código para o 
seguinte:
from django.contrib import messages1
from django.shortcuts import (2
    render, redirect, get_object_or_4043
)4
5
from visitantes.models import Visitante6
from visitantes.forms import VisitanteForm7
8
# código abaixo omitido9
Conforme vimos, para utilizar a função get_object_or_404() , precisamos passar a 
classe modelo e o atributo a ser utilizado para busca. Vamos passar a classe Visitante  
e dizer que vamos buscar o visitante pelo id  e que o id  é igual à variável que estamos 
recebendo como argumento da função informacoes_visitante() . Nosso código ﬁcará 
assim:

## Página 121

def informacoes_visitante(request, id):1
    2
    visitante = get_object_or_404(Visitante, id=id)3
    4
    context = {5
        "nome_pagina": "Informações de visitante",6
        "visitante": visitante7
    }8
    9
    return render(request, "informacoes_visitante.html", context)10
Não vamos nos esquecer de passar a variável visitante  no contexto, para que 
possamos acessá-la nos templates.
Criando URL para acessar informações de visitante
 
A essa altura você já deve ter percebido que precisamos mapear a nova view em uma URL 
para que a gente possa acessá-la através do navegador. Sendo assim, vamos trabalhar no 
arquivo urls.py  do nosso projeto e criar a URL de nome informacoes_visitante .
Essa URL vai ser um pouco diferente das que criamos até agora. Conforme visto, 
precisamos passar um id  como argumento para a função que será o identiﬁcador do 
visitante a ser buscado no banco de dados. Isso pode ser feito através da URL que será 
acessada, pois podemos passar o id  diretamente no endereço da URL. Por exemplo, se 
quisermos buscar as informações do visitante de id=1 , podemos acessar a URL 
http://127.0.0.1:8000/visitantes/1/.
O primeiro passo nós já ﬁzemos, que é receber o argumento na função de view que será 
mapeada na URL. Agora temos que criar a URL no arquivos urls.py  e utilizar a sintaxe 
<int:id>  para indicar que precisamos receber uma variável do tipo int  e de nome id . 
Nossa URL ﬁcará assim:
from django.urls import path1
from django.contrib import admin2
3

## Página 122

from usuarios.views import index4
5
from visitantes.views import (6
    registrar_visitante, informacoes_visitante7
)8
9
urlpatterns = [10
    # codigo acima omitido...11
    12
    path(13
        "registrar-visitante/",14
        registrar_visitante,15
        name="registrar_visitante",16
    ),17
18
    path(19
        "visitantes/<int:id>/",20
        informacoes_visitante,21
        name="informacoes_visitante",22
    )23
]24
Criando template para exibir informações de visitante
 
Com nossa view pronta, agora precisamos criar o arquivo informacoes_visitante.html  
na pasta templates do nosso projeto. Mais uma vez, você pode fazer download do 
template clicando no link abaixo:
Iniciar o download informacoes_visitante.zip - 947B
Após o download, coloque o arquivo na pasta templates do projeto e abra em seu editor de 
texto, pois ainda vamos alterar algumas coisas nele.
Ao abrir o arquivo, você vai perceber que as informações estão deﬁnidas diretamente no 
template. Para tornar o template dinâmico e funcional, vamos alterar os valores do atributo 
value  dos elementos field  do nosso HTML. A estrutura é bem parecida com a que 
utilizamos nos formulários, com a diferença que vamos renderizar todos os campos 
manualmente para que possamos personalizar melhor a estrutura do nosso template.

## Página 123

Como passamos a variável visitante  no contexto, podemos acessá-la diretamente 
utilizando a sintaxe {{ visitante.nome_do_atributo }} . Vamos alterar os valores 
estáticos para a sintaxe de template do Django e tornar nosso template dinâmico. Se você 
ﬁcar na dúvida sobre qual atributo deve exibir, o elemento  <label>  pode te ajudar!
Antes que a gente esqueça, vamos alterar também o texto que exibe o porteiro responsável 
pelo registro e o horário que o visitante foi registrado. Para isso, vamos alterar o texto de 
"Visitante registrado em 15/05/2018 por Walter White" para "Visitante registrado em 
{{ visitante.horario_chegada }}  por {{ visitante.registrado_por }} ". O template 
ﬁcará assim:
<div class="card-body">1
    <h4 class="mb-3 text-primary">2
        Informações gerais3
    </h4>4
5
    <form>6
        <div class="form-row">7
            <div class="form-group col-md-6">8
                <label>Horário de chegada</label>9
                <input type="text" class="form-control" value="{{ visitant10
            </div>11
12
            <div class="form-group col-md-6">13
                <label>Número da casa a ser visitada</label>14
                <input type="text" class="form-control" value="{{ visitant15
            </div>16
        </div>17
18
        <div class="form-row">19
            <div class="form-group col-md-4">20
                <label>Horário de autorização de entrada</label>21
                <input type="text" class="form-control" value="{{ visitant22
            </div>23
24
            <div class="form-group col-md-4">25
                <label>Entrada autorizada por</label>26
                <input type="text" class="form-control" value="{{ visitant27
            </div>28
29
            <div class="form-group col-md-4">30
                <label>Horário de saída</label>31
                <input type="text" class="form-control" value="{{ visitant32
            </div>33
        </div>34

## Página 124

    </form>35
36
    <h4 class="mb-3 mt-4 text-primary">37
        Informações pessoais38
    </h4>39
    40
    <form>41
        <div class="form-row">42
            <div class="form-group col-md-6">43
                <label>Nome completo</label>44
                <input type="text" class="form-control" value="{{ visitant45
            </div>46
47
            <div class="form-group col-md-6">48
                <label>CPF</label>49
                <input type="text" class="form-control" value="{{ visitant50
            </div>51
        </div>52
53
        <div class="form-row">54
            <div class="form-group col-md-6">55
                <label>Data de nascimento</label>56
                <input type="text" class="form-control" value="{{ visitant57
            </div>58
59
            <div class="form-group col-md-6">60
                <label>Placa do veículo</label>61
                <input type="text" class="form-control" value="{{ visitant62
            </div>63
        </div>64
    </form>65
            66
    <p class="mr-2 mt-3 mb-4 text-right">67
        <small>68
            Visitante registrado em {{ visitante.horario_chegada }} por {{ 69
        </small>70
    </p>71
72
    <div class="mr-1 text-right">73
        <a href="#" class="btn btn-secondary text-white" type="button">74
            <span class="text">Voltar</span>75
        </a>76
    </div>77
</div>78
Feito isso, vamos abrir o navegador e acessar o endereço 
http://127.0.0.1:8000/visitantes/1/. Você deverá visualizar as informações do primeiro 
visitante que registramos no banco de dados. 

## Página 125

Criando métodos personalizados para exibir informações 
do Visitante
Conforme exibimos os campos, você deve ter observado que alguns deles ainda não estão 
preenchidos no banco de dados e, por isso, exibem um valor em branco ou uma 
informação pouco clara do que, de fato, representa (None ). Para melhorar a exibição 
destes campos e, consequentemente, a melhorar a usabilidade da nossa dashboard, 
criaremos métodos personalizados nas classes modelo para que possamos exibir uma 
informação útil e clara, mesmo quando o campo não está preenchido.
Métodos são funções que existem dentro das classes e podem deﬁnir comportamentos 
para os objetos. Em nosso caso, criaremos métodos que alteram a forma com que as 
informações são exibidas para o usuário. Se, por exemplo, a entrada do morador ainda não 
tiver sido autorizada, podemos exibir algo como "Visitante aguardando autorização" nos 
campos horario_autorizacao  e morador_responsavel . O mesmo vale para o campo 
horario_saida , que só será preenchido no momento que a visita for ﬁnalizada.
Criando método para exibir horário de saída
Vamos criar métodos que vão substituir a exibição de alguns atributos, começando pelo 
horário de saída. Antes de tudo, você precisa saber que para criar um método dentro de 
uma classe, tudo que precisamos fazer é criar uma função dentro dessa classe que 
receberá o argumento self . Esse argumento nos possibilita acessar as propriedades da 
própria classe.
Os métodos que buscam informações, em geral, recebem o nome de getters e mantemos 
sempre a chave "get" no início de seus nomes. Abaixo do atributo registrado_por , vamos
escrever o método get_horario_saida() . Esse método, antes de tudo, precisa veriﬁcar se 
o atributo horario_saida  está preenchido e, caso não esteja, retornar o texto "Horário de 
saída não registrado". Para fazer isso, vamos utilizar a estrutura condicional if . O 
método ﬁcará assim:
# codigo acima omitido1
def get_horario_saida(self):2
    if self.horario_saida:3

## Página 126

        return self.horario_saida4
5
    return "Horário de saída não registrado"6
7
class Meta:8
    verbose_name = "Visitante"9
    verbose_name_plural = "Visitantes"10
    db_table = "visitante"11
12
    def __str__(self):13
        return self.nome_completo14
Criando métodos para exibir horário de autorização de entrada e 
morador responsável por autorizar a entrada
Faremos o mesmo para os atributos horario_autorizacao  e morador_responsavel , que 
serão exibidos somente se existir um valor a ser exibido. Caso contrário, vamos exibir um 
texto padrão. Vamos começar escrevendo o método get_horario_autorizacao() , que 
será bem parecido com o método get_horario_saida() .  O método 
get_horario_autorizacao()  ﬁcará assim:
def get_horario_autorizacao(self):1
    if self.horario_autorizacao:2
        return self.horario_autorizacao3
4
    return "Visitante aguardando autorização"5
Para o método get_morador_responsavel()  vamos fazer bem parecido. Nosso método 
ﬁcará assim:
def get_morador_responsavel(self):1
    if self.morador_responsavel:2
        return self.morador_responsavel3
4
    return "Visitante aguardando autorização"5

## Página 127

Criando método para exibir placa do veículo utilizado na visita
O método get_veiculo()  será parecido com os outros, mas também terá um outro texto 
padrão:
def get_placa_veiculo(self):1
    if self.placa_veiculo:2
        return self.placa_veiculo3
4
    return "Veículo não registrado"5
Utilizando métodos personalizados nos templates
 
Com nossos métodos criados, temos que alterar o template 
informacoes_visitante.html  para que exiba os métodos os invés dos atributos. A 
sintaxe para exibição de métodos nos templates é bem parecida com a que utilizamos 
para os atributos, inclusive.
Onde temos os atributos horario_autorizacao , morador_responsavel , horario_saida  
e placa_veiculo , vamos alterar para métodos criados. Ou seja, ao invés de 
{{ visitante.horario_autorizacao }} , utilizaremos 
{{ visitante.get_horario_autorizacao }} . O template ﬁcará assim:
<div class="card-body">1
    <h4 class="mb-3 text-primary">2
        Informações gerais3
    </h4>4
5
    <form>6
        <div class="form-row">7
            <div class="form-group col-md-6">8
                <label>Horário de chegada</label>9
                <input type="text" class="form-control" value="{{ visitant10
            </div>11
12
            <div class="form-group col-md-6">13

## Página 128

                <label>Número da casa a ser visitada</label>14
                <input type="text" class="form-control" value="{{ visitant15
            </div>16
        </div>17
18
        <div class="form-row">19
            <div class="form-group col-md-4">20
                <label>Horário de autorização de entrada</label>21
                <input type="text" class="form-control" value="{{ visitant22
            </div>23
24
            <div class="form-group col-md-4">25
                <label>Entrada autorizada por</label>26
                <input type="text" class="form-control" value="{{ visitant27
            </div>28
29
            <div class="form-group col-md-4">30
                <label>Horário de saída</label>31
                <input type="text" class="form-control" value="{{ visitant32
            </div>33
        </div>34
    </form>35
36
    <h4 class="mb-3 mt-4 text-primary">37
        Informações pessoais38
    </h4>39
    40
    <form>41
        <div class="form-row">42
            <div class="form-group col-md-6">43
                <label>Nome completo</label>44
                <input type="text" class="form-control" value="{{ visitant45
            </div>46
47
            <div class="form-group col-md-6">48
                <label>CPF</label>49
                <input type="text" class="form-control" value="{{ visitant50
            </div>51
        </div>52
53
        <div class="form-row">54
            <div class="form-group col-md-6">55
                <label>Data de nascimento</label>56
                <input type="text" class="form-control" value="{{ visitant57
            </div>58
59
            <div class="form-group col-md-6">60
                <label>Placa do veículo</label>61
                <input type="text" class="form-control" value="{{ visitant62
            </div>63
        </div>64

## Página 129

    </form>65
            66
    <p class="mr-2 mt-3 mb-4 text-right">67
        <small>68
            Visitante registrado em {{ visitante.horario_chegada }} por {{ 69
        </small>70
    </p>71
72
    <div class="mr-1 text-right">73
        <a href="#" class="btn btn-secondary text-white" type="button">74
            <span class="text">Voltar</span>75
        </a>76
    </div>77
</div>78
Não podemos esquecer do template index.html , onde também vamos utilizar os 
métodos get_horario_autorizacao  e get_morador_responsavel . O trecho de código 
ﬁcará assim:
<tbody>1
    {% for visitante in todos_visitantes %}2
        <tr>3
            <td>{{ visitante.nome_completo }}</td>4
            <td>{{ visitante.cpf }}</td>5
            <td>{{ visitante.horario_chegada }}</td>6
            <td>{{ visitante.get_horario_autorizacao }}</td>7
            <td>{{ visitante.get_morador_responsavel }}</td>8
            <td>9
                <a href="{% url 'informacoes_visitante' id=visitante.id %}10
                    Ver informações11
                </a>12
            </td>13
        </tr>14
    {% endfor %}15
</tbody>16
Você pode criar os métodos que quiser e exibir as informações conforme precisar. Existem 
diversas possibilidades e aplicações, então sinta-se livre para explorar essas 
possibilidades!
 

## Página 130

Utilizando o Django para renderizar nossas URLs
Para acessar as informações de cada visitante, precisamos acessar a URL 
http://127.0.0.1/visitantes/{id}/ , onde o {id}  será um valor diferente para cada 
visitante. Até agora ﬁzemos isso manualmente, mas você deve estar se perguntando: como
vamos fazer para renderizar uma URL diferente para cada de visitante de forma 
automática?
Quando criamos nosso modelo de visitante, não criamos o atributo id , mas o 
Django faz isso por nós para que possamos utilizá-lo como primary_key . 
Além disso, o atributo id  deverá ser único e, para cada novo visitante 
registrado, o valor será aumentado em um. Sendo assim, não existirá dois 
visitante de mesmo id .
Para nossa sorte, o pessoal responsável pelo Django já pensou em tudo por nós. Dentre as 
tags de template, existe a tag {% url %} . Ela tem a função de renderizar as URLs do 
nosso projeto de forma automática, bastando que a gente passe apenas o nome da URL 
da ser renderizada (sim, é exatamente o valor que deﬁnimos para o argumento name  na 
deﬁnição da URL no arquivos urls.py ).
Vamos abrir o arquivo index.html  e utilizar a tag {% url %}  para renderizar a URL que 
irá nos direcionar para o template de informações de cada visitante. Na tabela que exibe as 
informações dos visitantes recentes existe um link que exibe o texto "Ver detalhes". Vamos 
alterar o valor de href  do elemento <a>  de #  para 
{% url 'informacoes_visitante' id=visitante.id %} . Primeiro passamos nome da 
URL e depois podemos passar argumentos necessários que, para esse caso, é somente a 
id . Note também que, dentro do loop, o id  de cada visitante é acessado da mesma 
forma que os outros atributos. O loop ﬁcará assim:
{% for visitante in todos_visitantes %}1
    <td>{{ visitante.nome_completo }}</td>2
    <td>{{ visitante.cpf }}</td>3
    <td>{{ visitante.horario_chegada }}</td>4
    <td>{{ visitante.horario_autorizacao }}</td>5

## Página 131

    <td>{{ visitante.morador_responsavel }}</td>6
    <td>7
        <a href="{% url 'informacoes_visitante' id=visitante.id %}">8
            Ver detalhes9
        </a>10
    </td>11
{% endfor %}12
Para facilitar o acesso à URL de registro de visitantes, vamos inserir um botão ao lado do 
nome da página que deverá nos direcionar para a página http://127.0.0.1:8000/registrar-
visitante/. Abaixo do elemento 
<h1 class="h3 mb-0 text-gray-800">{{ nome_pagina }}</h1>  vamos inserir o seguinte 
trecho de código:
<a href="{% url 'registrar_visitante' %}" class="btn btn-primary btn-icon-1
    <span class="text">Registrar visitante</span>2
3
    <span class="icon text-white-50">4
        <i class="fas fa-user-plus"></i>5
    </span>6
</a>7
Como nossa URL registrar_visitante  não recebe argumentos, passamos para a tag 
apenas o nome da mesma.
Renderizando a URL para retornar à página inicial
Agora que já sabemos utilizar a tag {% url %}, vamos utilizá-la também para renderizar o 
endereço para nos direcionar à página inicial da dashboard. No menu lateral à esquerda 
existe um texto com um ícone e o escrito "Início", e é ele que vamos buscar em nosso 
template base.html . O trecho de código ﬁcará assim:
<a class="nav-link" href="{% url 'index' %}">1
    <i class="fas fa-home"></i>2
    <span>Início</span>3
</a>4

## Página 132

Capítulo 11
Criando funcionalidade para autorização de entrada de 
visitante
Nos capítulos anteriores, nos dedicamos à criação das funcionalidades para registro e 
visualização de informações de visitantes. Aprendemos um pouco sobre como requisições 
funcionam, aprendemos a utilizar os formulários do Django, adaptamos os templates e 
aprendemos um pouco mais como eles funcionam, conhecemos o 
django-widget-tweaks , o Django messages  e o get_object_or_404  e ainda criamos 
métodos personalizados para nosso modelo de visitantes. Olha só quanta coisa 
conseguimos absorver somente nesses últimos capítulos!
Com essas funcionalidades criadas, precisamos seguir o roteiro que criamos com base nas
necessidades do cliente, de modo que, agora, trabalharemos na funcionalidade que 
autoriza a entrada do visitante no condomínio. Quando um visitante chega na portaria e se 
identiﬁca, o mesmo deve aguardar que o colaborador responsável, no caso o porteiro, entre 
em contato com um morador da casa a ser visitada e autorize que este visitante adentre ao 
condomínio.
Ao receber a informação de que o visitante pode adentrar ao condomínio, o porteiro deverá 
registrar na dashboard qual o nome do morador que autorizou a entrada deste visitante. 
Para ﬁns de controle, também é necessário que o sistema registre o horário em que essa 
autorização ocorreu. Sendo assim, no momento da autorização do visitante, devemos 
registrar o horário e o nome do morador responsável pela autorização.
Criando um status diferente para cada estágio da visita
 
Antes de seguir em frente, precisamos analisar o cenário e extrair algumas informações 
com base nos ﬂuxos e eventos que ocorrem em uma visita. Existem três cenários para o 
visitante: quando ele chega na portaria e está aguardando autorização (status 1), quando 
ele está dentro do condomínio realizando a visita (status 2) e quando ele vai embora e 
ﬁnaliza a visita (status 3).

## Página 133

Deﬁnir e tornar esses status explícitos é interessante pois assim podemos diferenciar os 
estágios em que cada visitante se encontra e ainda contabilizar visitantes estão 
aguardando autorização, em visita dentro do condomínio e quantos já foram embora. 
Assim temos mais clareza com relação às informações e ainda conseguimos contabilizar 
esses números para exibir na página inicial da nossa dashboard.
Vamos voltar ao nosso arquivo models.py  do aplicativos visitantes e adicionar o atributo 
status  ao modelo de Visitante. Ele será do tipo CharField , mas com a diferença que 
receberá uma lista pré determinada de opções disponíveis para escolha. Essa lista deverá 
guardar as opções disponíveis e devemos deﬁnir sempre o valor que será salvo em nosso 
banco de dados e o valor que será exibido para o usuário ﬁnal. Antes de criar o atributo, 
vamos criar a variável STATUS_VISITANTE , que ﬁcará da seguinte forma:
class Visitante(models.Model):1
2
    STATUS_VISITANTE = [3
        ("AGUARDANDO", "Aguardando autorização"),4
        ("EM_VISITA", "Em visita"),5
        ("FINALIZADO", "Visita finalizada"),6
    ]7
    8
    # código abaixo omitido9
A lista STATUS_VISITANTE  segue o que foi dito anteriormente e deﬁne os status 
Aguardando autorização , Em visita  e Finalizado . O primeiro valor, em 
letras maiúsculas, será guardado no banco de dados e o segundo é o texto que 
será exibido para o usuário ﬁnal. Sendo assim, quando o visitante receber o 
status AGUARDANDO , o texto Aguardando autorização será exibido.
Com isso, agora vamos adicionar o atributo status  ao nosso modelo. Além dos 
argumentos verbose_name  e max_length  que já conhecemos, também vamos passar os 
argumentos choices  e default . O primeiro é a lista que criamos com as opções 
disponíveis para escolha e o segundo é o valor padrão a ser deﬁnido quando uma 
instância do modelo for criada. Nosso código ﬁcará assim:

## Página 134

class Visitante(models.Model):1
2
    STATUS_VISITANTE = [3
        ("AGUARDANDO", "Aguardando autorização"),4
        ("EM_VISITA", "Em visita"),5
        ("FINALIZADO", "Visita finalizada"),6
    ]7
    8
    status = models.CharField(9
        verbose_name="Status",10
        max_length=10,11
        choices=STATUS_VISITANTE,12
        default="AGUARDANDO",13
    )14
    15
    # código abaixo omitido16
O status default  será AGUARDANDO  pois sempre que um visitante chega à 
portaria, ﬁca aguardando a autorização de um morador
Criando o arquivo de migrações
Como vimos anteriormente, sempre que mudamos a estrutura do nosso modelo, 
precisamos criar um arquivo que registra essas alterações em formato de migração para 
que seja possível efetuar as alterações no banco de dados posteriormente. Mais uma vez, 
utilizaremos o comando makemigrations :
(env)$ python manage.py makemigrations visitantes
O terminal deverá mostrar algo parecido com isto:
Migrations for 'visitantes':1
  visitantes/migrations/0005_visitante_status.py2
    - Add field status to visitante3

## Página 135

Efetuando as alterações no banco de dados
Nada diferente do que já vimos, vamos agora utiliza o comando migrate  para efetuar as 
mudanças em nosso banco de dados:
(env)$ python manage.py migrate
Criando formulário para atualizar atributos especíﬁcos do 
visitante
 
Sabemos que precisamos registrar o nome do morador responsável por autorizar a entrada 
do visitante, além de salvar data e hora e, agora que temos um status, alterar esse status. 
Por padrão e uma questão lógica, como falamos no tópico anterior, sempre que criamos 
um visitante o mesmo recebe o status AGUARDANDO  e, quando sua entrada for autorizada, 
vamos alterar esse status para EM_VISITA .
Criaremos a funcionalidade na tela que exibe as informações do visitante, de forma que, 
quando o visitante estiver aguardando autorização, vamos exibir um botão para executar a 
funcionalidade que autorizará sua entrada. Utilizaremos um formulário para receber o 
nome do morador responsável e as informações referentes ao horário de autorização e 
status serão deﬁnidas diretamente na view.
Para começar, vamos abrir o arquivo forms.py  do aplicativos visitantes e criar o 
formulário AutorizaVisitanteForm , uma subclasse de ModelForm  bem parecida com a 
que já criamos, com a diferença que terá apenas o campo morador_responsavel  na lista 
fields :
class AutorizaVisitanteForm(forms.ModelForm):1
    morador_responsavel = forms.CharField(required=True)2
3
    class Meta:4
        model = Visitante5
        fields = [6

## Página 136

            "morador_responsavel",7
        ]8
        error_messages = {9
            "morador_responsavel": {10
                "required": "Por favor, informe o nome do morador responsá11
            }12
        }13
Ao criamos um formulário, podemos também sobrescrever os campos deﬁnidos 
automaticamente por causa da classe modelo, caso a gente queira complementar alguma 
informação ou personalizar algum comportamento. No nosso caso, como o atributo 
morador_responsavel  não é obrigatório no modelo, também não será no formulário, 
mesmo que a gente esteja recebendo apenas ele. Por isso vamos sobrescrever o campo no 
formulário, aﬁm de explicitar que ele deve ser obrigatório. Além disso, também vamos 
deﬁnir uma mensagem de erro para caso o campo não seja preenchido. Feito isso, já 
podemos utilizar o formulário em nossa view.
Alterando view para autorizar entrada de visitante
 
Agora que criamos um formulário para receber o nome do morador responsável, temos que 
realizar algumas alterações em nossa view e em nosso template para que o formulário 
seja exibido e funcione corretamente.
Já escrevemos um código bem parecido com o que vamos escrever agora, o da view 
registrar_visitante . Desta vez, vamos importar o formulário AutorizaVisitanteForm  
no arquivo views.py  do aplicativo visitantes. O trecho onde as importações são feitas 
ﬁcará assim:
from django.contrib import messages1
from django.shortcuts import (2
    render, redirect, get_object_or_4043
)4
5
from visitantes.models import Visitante6
from visitantes.forms import (7
    VisitanteForm, AutorizaVisitanteForm8
)9

## Página 137

10
# código abaixo omitido11
Com o formulário importado no arquivo views.py , vamos trabalhar na função 
informacoes_visitante() , exatamente da forma que ﬁzemos na função 
registrar_visitante() : criar a variável form, veriﬁcar se o método POST está sendo 
utilizado na requisição, passar o corpo da requisição para o formulário, veriﬁcar se as 
informações são válidas, salvar o formulário, exibir a mensagem de sucesso e redirecionar 
o usuário. Não podemos nos esquecer, claro, de passar o formulário no contexto da view. A 
função ﬁcará assim:
def informacoes_visitante(request, id):1
    2
    visitante = get_object_or_404(Visitante, id=id)3
    4
    form = AutorizaVisitanteForm()5
    6
    if request.method == "POST":7
        form = AutorizaVisitanteForm(8
            request.POST, instance=visitante9
        )10
        11
        if form.is_valid():12
            form.save()13
14
            messages.success(15
                request,16
                "Entrada de visitante autorizada com sucesso"17
            )18
19
            return redirect("index")20
    21
    context = {22
        "nome_pagina": "Informações de visitante",23
        "visitante": visitante,24
        "form": form,25
    }26
    27
    return render(request, "informacoes_visitante.html", context)28

## Página 138

Note que, desta vez, passamos também o argumento instance  para o nosso formulário. 
Quando fazemos isso, o Django entende que queremos atualizar o objeto em questão (o 
visitante com id  igual à passada para a função, no caso). Estamos dizendo para o 
Django atualizar o visitante em questão utilizando a informação do corpo da requisição.
Alterando template para exibir modal com formulário
 
Como passamos a variável form  no contexto, podemos agora alterar nosso template 
para que exiba esse formulário. Como as informações do visitante já ocupam grande parte 
do template, utilizaremos um elemento HTML conhecido como modal para exibir o 
formulário. Na verdade, ele é feito unindo as tecnologias HTML, CSS e Javascript e é um 
elemento que se sobrepõe aos outros, quase como um pop-up (aquelas janelas chatas que 
piscam na tela).
Antes de tudo, vamos adicionar o botão que será responsável por exibir o modal com o 
formulário. Abra o arquivo informacoes_visitante.html  e abaixo do elemento 
<h1 class="h3 mb-0 text-gray-800">  insira o seguinte trecho de código:
<!-- código acima omitido -->1
<h1 class="h3 mb-0 text-gray-800">{{ nome_pagina }}</h1>2
3
<!-- trecho de código a ser inserido -->4
<div>5
    <a href="#" class="btn btn-success btn-icon-split btn-sm" data-toggle=6
        <span class="text">Autorizar entrada</span>7
                    8
        <span class="icon text-white-50">9
            <i class="fas fa-user-check"></i>10
        </span>11
    </a>12
</div>13
<!-- código abaixo omitido -->14
O que estamos fazendo é adicionar um elemento <div>  ao lado do título da página que 
possui um link (elemento <a> ) para um elemento modal chamado de #modal1 , que 
ainda vamos inserir na página. O template ﬁcará parecido com isso:

## Página 139

Cabeçalho com título da página e botão verde escrito "Registrar visitante"
Feito isso, adicione também o código HTML do modal antes do fechamento da tag do 
elemento <div class="container"> :
<div class="modal fade" id="modal1" tabindex="-1" role="dialog" aria-label1
    <div class="modal-dialog" role="document">2
        <div class="modal-content">3
            <div class="modal-header">4
                <h5 class="modal-title" id="exampleModalLabel">Autorizar e5
                6
                <button type="button" class="close" data-dismiss="modal" a7
                    <span aria-hidden="true">&times;</span>8
                </button>9
            </div>10
            11
            <div class="modal-body">12
                <form method="post">13
                    {% csrf_token %}14
15
                    <div class="form-group">16
                        <label for="id_morador_responsavel" class="col-for17
                        {% render_field form.morador_responsavel placehold18
                    </div>19
                        20
                    <div class="modal-footer">21
                        <button type="button" class="btn btn-secondary" da22
                        <button type="submit" class="btn btn-primary">Auto23
                    </div>24
                </form>25
            </div>26
        </div>27
    </div>28
</div>29
Conforme falado, esse modal deve exibir nosso formulário de cadastro de morador 
responsável, e é isso que estamos fazendo. Criamos a estrutura HTML para o formulário 
dentro do elemento <div class="modal-body">  de forma bem parecida com que foi feito 
anteriormente para renderizar o campo, com a diferença que agora estamos acessando o 

## Página 140

Template de informações de visitante ao fundo e alerta bom formulário para registro do 
nome do morador responsável
campo morador_responsavel  do formulário diretamente para passá-lo para a tag 
{% render_field %} .
Já utilizamos a tag {% render_field %}  anteriormente, quando renderizamos nosso 
formulário para registro de novos visitantes. A dinâmica utilizada aqui será a mesma, com 
a diferença que vamos acessar o campo do formulário diretamente (
form.morador_responsavel ).
Note que o template baixado no capítulo anterior já possui a tag de importação 
do django-widget-tweaks ({% load widget_tweaks %} ).
Feito isso, vamos agora visualizar as informações de um visitante qualquer e tentar 
autorizar sua entrada por meio do formulário que criado. Note que, quando clicamos no 
botão, o modal com o formulário aparece na tela:
Atualizando os campos horario_autorizacao e status 
 

## Página 141

diretamente
Ao testar o formulário e constatar que tudo ocorreu bem, você deve ter notado que, apesar 
do nome do morador responsável ter sido atualizado, os valores de horario_autorizacao  
e status  continuaram os mesmos. Isso porque nosso formulário está atualizando 
apenas o campo morador_responsavel , e era isso que estávamos esperando, visto que 
colocamos apenas este campo na propriedade fields  do formulário em questão. Mas 
como vamos atualizar estes outros campos?
Atualizando o status
Quando criamos o formulário para registro de visitantes, deﬁnimos o valor do atributo 
registrado_por  diretamente e é o que faremos neste caso também. Para isso, vamos 
alterar a view para que seja possível setar esses valores diretamente.
# código acima omitido1
2
if form.is_valid():3
    visitante = form.save(commit=False)4
    5
    visitante.status = "EM_VISITA"6
7
    visitante.save()8
9
    messages.success(10
        request,11
        "Entrada de visitante autorizada com sucesso"12
    )13
14
    return redirect("index")15
16
# código abaixo omitido17
Dessa forma, já estamos deﬁnindo o valor que o status receberá caso o formulário seja 
válido e salvando o novo visitante, mas ainda precisamos registrar o horário em que essa 
autorização ocorreu, ou seja, o horário em que o formulário atualizou o atributo 
morador_responsavel  e alterou o status para EM_VISITA .

## Página 142

Conhecendo o timezone do Django
O Python, por padrão, possui um módulo para trabalhar com datas e horas que é o 
datetime , mas por algumas questões referentes aos horários diferentes que são 
suportados, o Django nos recomenda a utilização do módulo timezone . Esse módulo nos 
fornece inúmeras ferramentas para trabalharmos com datas de forma bem facilitada já 
considerando a timezone  em que nossa aplicação está contextualizada. O primeiro 
passo é importarmos o módulo na view.
from django.contrib import messages1
from django.shortcuts import (2
    render, redirect, get_object_or_4043
)4
5
from visitantes.models import Visitante6
from visitantes.forms import (7
    VisitanteForm, AutorizaVisitanteForm8
)9
10
from django.utils import timezone11
12
# código abaixo omitido13
O timezone  possui um método chamado now()  que nos retorna data e hora do 
momento em que a chamada ao método ocorreu. Sendo assim, caso o registro do visitante 
ocorra no dia 21 de agosto de 2020 às 15:00:00 , o método timezone.now()  retornaria 
exatamente essa data e hora. Dessa forma, tudo que precisamos fazer é igualar o atributo 
horario_autorizacao  à chamada do método timezone.now() . Nossa view ﬁcará assim:
# código acima omitido1
2
if form.is_valid():3
    visitante = form.save(commit=False)4
    5
    visitante.status = "EM_VISITA"6
    visitante.horario_autorizacao = timezone.now()7
8
    visitante.save()9
10

## Página 143

    messages.success(11
        request,12
        "Entrada de visitante autorizada com sucesso"13
    )14
15
    return redirect("index")16
17
# código abaixo omitido18
Dessa forma, atualizamos o nome do morador responsável através do formulário e, caso a 
informação seja válida, atualizamos os atributos status  e horario_autorizacao  
diretamente.

## Página 144

Capítulo 12
Criando função para ﬁnalizar visita
Agora que criamos a função para autorizar a entrada do visitante, precisamos também 
criar a função que ﬁnaliza a visita. Para a primeira, utilizamos o formulário 
AutorizaVisitanteForm  para atualiza o nome do morador responsável e deﬁnimos 
manualmente o status e o horário de autorização.
Desta vez, precisamos atualizar apenas o valor do atributo horario_saida  e alterar o 
status para FINALIZADO , que é o status para quando o visitante deixa o condomínio. 
Sendo assim, vamos criar uma outra view que será responsável por receber um id , 
buscar um visitante com este id  e atualizar essas informações. A view será um pouco 
parecida com a view informacoes_visitante . 
Abaixo da função informacoes_visitante  crie e função finalizar_visita :
# código acima omitido1
2
def finalizar_visita(request, id):3
4
    if request.method == "POST":5
        visitante = get_object_or_404(Visitante, id=id)6
7
        visitante.status = "FINALIZADO"8
        visitante.horario_saida = timezone.now()9
10
        visitante.save()11
12
        messages.success(13
            request,14
            "Visita finalizada com sucesso"15
        )16
17
        return redirect("index")18
A função finalizar_visita  deverá receber um id  como argumento e utilizar a função 
get_object_or_404  para buscar o visitante do id  que foi passado. Após isso vamos 

## Página 145

atualizar os atributos status  e horario_saida  diretamente e salvar o visitante. A 
diferença aqui é que não utilizaremos um formulário e nossa view será acessada somente 
através do método POST . Todo o resto continuará bem parecido com as funções que já 
escrevemos antes.
Para garantir que as operações serão realizadas somente quando o método POST  for 
utilizado, vamos escrever um if  para certiﬁcar essa informação (
if request.method == "POST": ) e, caso seja verdadeira, vamos executar as operações 
necessárias. Note que, mais uma vez, estamos utilizando o método timezone.now()  mas, 
desta vez, para o atributo horario_saida , e setando diretamente o status  que agora 
deve receber o status FINALIZADO . 
Criando URL
 
Assim como todas as outras funções de view que escrevemos, essa também será 
mapeada por meio de uma URL para que a gente possa acessá-la pelo navegador. Vamos 
para o nosso arquivos urls.py  e criar essa nova URL. 
A URL que irá mapear a função finalizar_visita  será bem parecida com a URL 
informacoes_visitante , mas a diferença é que adicionaremos, após o id , o trecho 
finalizar-visita/ . Com isso, conseguimos diferenciar qual função de view chamar 
para quando o usuário desejar apenas visualizar as informações de um visitante e para 
quando desejar ﬁnalizar uma visita. Nosso arquivo urls.py  ﬁcará assim:
from django.contrib import admin1
from django.urls import path2
3
from usuarios.views import index4
5
from visitantes.views import (6
    registrar_visitante, informacoes_visitante,7
    finalizar_visita8
)9
10
urlpatterns = [11
    path("admin/", admin.site.urls),12

## Página 146

13
    path(14
        "",15
        index,16
        name="index",17
    ),18
19
    path(20
        "registrar-vistante/",21
        vegistrar_visitante,22
        name="registrar_visitante",23
    ),24
25
    path(26
        "visitantes/<int:id>/",27
        informacoes_visitante,28
        name="informacoes_visitante",29
    ),30
31
    path(32
        "visitantes/<int:id>/finalizar-visita/",33
        finalizar_visita,34
        name="finalizar_visita"35
    )36
]37
Alterando template para exibir botão e modal para ﬁnalizar 
visita
 
Agora que temos a URL para onde devemos enviar uma requisição para sinalizar que 
queremos ﬁnalizar uma visita, vamos alterar as partes do template que vão possibilitar a 
interação do usuário com essa funcionalidade.
Assim como inserimos um botão para quando queremos autorizar a entrada de um 
visitante, vamos inserir um botão para quando quisermos ﬁnalizar a visita. Abra o template 
informacoes_visitante.html  e insira o seguinte trecho de código abaixo do botão 
responsável por autorizar a entrada do visitante:
<a href="#" class="btn btn-warning btn-icon-split btn-sm" data-toggle="mod1
    <span class="text">Finalizar visita</span>2

## Página 147

Template de informações de visitante agora também com botão amarelo escrito "Finalizar 
visita"
                    3
    <span class="icon text-white-50">4
        <i class="fas fa-door-open"></i>5
    </span>6
</a>7
O template ﬁcará assim:
Note que a estrutura é bem parecida com a que utilizamos no outro botão, mas quando 
observamos o atributo data-target  podemos notar que agora ele é igual a #modal2 . 
Isso porque vamos também criar um outro modal para ser exibido quando o usuário clicar 
no botão para ﬁnalizar uma visita. A função desse modal é obter a conﬁrmação se é isso 
mesmo que o usuário deseja fazer.
Ainda no mesmo arquivo, mas agora ao ﬁnal do arquivo, vamos colocar o seguinte trecho 
de código logo abaixo da estrutura HTML do primeiro modal:
<div class="modal fade" id="modal2" tabindex="-1" role="dialog" aria-label1
    <div class="modal-dialog" role="document">2

## Página 148

        <div class="modal-content">3
            <div class="modal-header">4
                <h5 class="modal-title" id="exampleModalLabel">Finalizar v5
                    6
                <button type="button" class="close" data-dismiss="modal" a7
                    <span aria-hidden="true">&times;</span>8
                </button>9
            </div>10
            11
            <div class="modal-body">12
                <div class="modal-body">13
                    <h5 class="mb-3">14
                        Realmente deseja encerrar a visita?15
                    </h5>16
17
                    <form method="post" action="{% url 'finalizar_visita' 18
                        {% csrf_token %}19
20
                        <input hidden>21
22
                        <div class="modal-footer">23
                            <button type="button" class="btn btn-secondary24
                            <button type="submit" class="btn btn-primary">25
                        </div>26
                    </form>27
                </div>28
            </div>29
        </div>30
    </div>31
</div>32
Nosso segundo modal será exibido da seguinte maneira:

## Página 149

Template de informações de visitante ao fundo com alerta solicitando conﬁrmação do 
usuário de que realmente deseja ﬁnalizar a visita
Esse segundo modal deverá exibir a mensagem "Realmente deseja encerrar a visita?" e 
conter um formulário que enviará uma requisição do tipo POST  para a URL que criamos 
anteriormente. Esse formulário precisa ter apenas o campo renderizado pela tag 
{% csrf_token %}  para identiﬁcar que as requisições podem ser aceitas pelo nosso 
servidor.
Estamos enviando uma requisição do tipo POST  para URL pois é recomendada 
a utilização deste método sempre que precisamos alterar informações em 
nosso banco de dados
O que muda tudo aqui é o atributo action  do formulário HTML. Graças a ele podemos 
direcionar um formulário para uma URL diferente da que estamos, diferentemente de como 
ﬁzemos com os outros formulários. Dessa forma, conseguimos enviar uma requisição do 
tipo POST  para a URL {% url 'finalizar_visita' id=visitante.id %}  com toda 
informação que precisamos para identiﬁcar o visitante a ser atualizado assim que o 
usuário clicar no botão "Finalizar visita" dom modal conﬁrmando a ação.
Vai em frente e teste a nova funcionalidade implementada! 

## Página 150

Prevenindo erros e operações desnecessárias
Nos passos anteriores, implementamos a funcionalidade que ﬁnaliza as visitas dentro da 
nossa dashboard. Você deve ter notado que mesmo quando a visita já foi ﬁnalizada, os 
botões são exibidos. Isso não é bom pois o usuário pode se confundir e clicar em um dos 
botões, alterando as informações existentes no nosso banco de dados.
Para prevenir que isso aconteça, vamos veriﬁcar o status do visitante e exibir os botões 
com base no valor desse status. Funcionará assim:
Se o visitante estiver com status AGUARDANDO , vamos exibir o botão para autorizar a 
entrada
Se o visitante estiver com status EM_VISITA , vamos exibir o botão para ﬁnalizar a 
visita 
E, ﬁnalmente, se o visitante estiver com status FINALIZADO , não vamos exibir botões
Exibição condicional de botões para autorizar entrada e ﬁnalizar visita
Para fazer isso, vamos utilizar a tag {% if %}  para veriﬁcar o status do visitante e 
renderizar um botão por vez. Primeiro, vamos criar a instrução if  para veriﬁcar se o 
status é AGUARDANDO  e renderizar o botão para autorizar a entrada do visitante.
Utilizando a tag {% if %}  vamos deﬁnir a condição 
visitante.status == "AGUARDANDO"  para que o botão apareça. Isto é, o HTML referente 
ao botão só será renderizado no template caso o status do visitante seja AGUARDANDO . 
Nosso código ﬁcará assim:
{% if visitante.status == "AGUARDANDO" %}1
    <a href="#" class="btn btn-success btn-icon-split btn-sm" data-toggle=2
        <span class="text">Autorizar entrada</span>3
                4
        <span class="icon text-white-50">5
            <i class="fas fa-user-check"></i>6
        </span>7
    </a>8
{% endif %}9

## Página 151

Abaixo do código que escrevemos, vamos criar uma outra condição com a tag {% if %} . 
Dessa vez, queremos veriﬁcar se o status é o EM_VISITA . O código completo ﬁcará assim:
<div class="d-sm-flex align-items-center justify-content-between mb-4">1
    <h1 class="h3 mb-0 text-gray-800">{{ nome_pagina }}</h1>2
        3
    <div class="">4
        {% if visitante.status == "AGUARDANDO" %}5
            <a href="#" class="btn btn-success btn-icon-split btn-sm" data6
                <span class="text">Autorizar entrada</span>7
                    8
                <span class="icon text-white-50">9
                    <i class="fas fa-user-check"></i>10
                </span>11
            </a>12
        {% endif %}13
14
        {% if visitante.status == "EM_VISITA" %}15
            <a href="#" class="btn btn-warning btn-icon-split btn-sm" data16
                <span class="text">Finalizar visita</span>17
                    18
                <span class="icon text-white-50">19
                    <i class="fas fa-door-open"></i>20
                </span>21
            </a>22
        {% endif %}23
    </div>24
</div>25
Se você acessar a página de informação de algum visitante, notará que os botões não 
estão aparecendo juntos mais. Além disso, se você for na página de informação de um 
visitante que já deixou as dependências do condomínio, isto é, ﬁnalizou sua visita, notará 
que nenhum botão é exibido. 
Dessa forma conseguimos evitar que operações desnecessárias sejam realizadas e que as 
informações do nosso banco de dados sejam alteradas de forma indevida.
Bloqueando o acesso à URL por métodos diferentes do 
POST
 

## Página 152

Ao contrário das outras funções que escrevemos, a função finalizar_visita  não poderá
ser acessada através do método GET . O método GET  é utilizado por uma requisição 
sempre que precisamos buscar informações em um servidor, como é o caso nas outras 
funções (estamos buscando o template e todo o contexto relacionado a ele antes de enviar 
informações para o usuário). Se você notar as funções registrar_visitante  e 
informacoes_visitante , vai perceber que deﬁnimos algumas variáveis fora da instrução 
if  que veriﬁca se o método utilizado é o POST . Isso porque precisamos dessas variáveis 
quando o usuário acessa a página, como é o caso do formulário que deverá ser exibido 
mesmo que uma requisição POST  não seja enviada.
Para garantir que nossa view possa ser acessada somente pelo método POST , vamos 
utilizar a classe HttpResponseNotAllowed  para nos ajudar. Ela é quem vai cuidar de toda 
parte de bloquear o acesso via método GET  e retornar uma mensagem para o usuário 
quando isso ocorrer. Antes de tudo, precisamos importá-la em nosso arquivo views.py  do 
aplicativo visitantes:
from django.contrib import messages1
from django.shortcuts import (2
    render, redirect, get_object_or_4043
)4
5
from django.http import HttpResponseNotAllowed6
7
from visitantes.models import Visitante8
from visitantes.forms import (9
    VisitanteForm, AutorizaVisitanteForm10
)11
12
from django.utils import timezone13
14
# código abaixo omitido15
Feito isso, tudo que precisamos fazer é utilizar a instrução else  e retornar a classe 
HttpResponseNotAllowed  passando uma lista com os métodos permitidos e uma 
mensagem a ser exibida caso o método utilizado pela requisição seja diferente. Nosso 
código ﬁcará assim:

## Página 153

def finalizar_visita(request, id):1
2
    if request.method == "POST":3
        visitante = get_object_or_404(Visitante, id=id)4
5
        visitante.status = "FINALIZADO"6
        visitante.horario_saida = timezone.now()7
8
        visitante.save()9
10
        messages.success(11
            request,12
            "Visita finalizada com sucesso"13
        )14
15
        return redirect("index")16
17
    else:18
        return HttpResponseNotAllowed(19
            ["POST"],20
            "Método não permitido"21
        )22
Com isso, permitimos que a view seja acessada somente pelo método POST  e que, 
quando outro método for utilizado, a view vai retornar o código HTTP 405  e exibir a 
mensagem "Método não permitido".
Se você quiser, teste em seu navegador: http://127.0.0.1:8000/visitantes/4/ﬁnalizar-visita/.

## Página 154

Capítulo 13
Implementando melhorias em nossos templates
Olha só que legal: ﬁnalizamos as funcionalidades de maior valor da nossa dashboard. Os 
porteiros já podem registrar visitantes, autorizar a entrada deles após contato com um 
morador e ainda sinalizar que a visita foi encerrada. Bem bacana, não?
Agora que temos as principais funcionalidades prontas, vamos nos concentrar em 
melhorar a experiência de utilização da dashboard e ainda melhorar a estrutura do nosso 
projeto, de modo que seja mais fácil realizar futuras manutenções.
Começaremos com algumas alterações nos templates que visam melhorar a experiência 
de utilização da dashboard.
Exibindo botão com função de "voltar" e "cancelar" em páginas de 
informações e registro de visitante
Nossa primeira melhoria será inserir os botões com as ações cancelar e voltar nas páginas 
de registro de visitante e informações de visitante. Vamos primeiro abrir o arquivo 
registrar_visitante.html  e procurar pelo seguinte trecho de código:
<div class="text-right">1
    <button class="btn btn-primary" type="submit">2
        <span class="text">Registrar visitante</span>3
    </button>4
</div>5
Acima do elemento <button class="btn btn-primary" type="submit">  vamos inserir 
um link para a página inicial da nossa dashboard com o texto "Cancelar", aproveitando 
algumas classes do Bootstrap para que o link tenha a aparência de um botão. O código 
ﬁcará assim:
<div class="text-right">1

## Página 155

    <a href="{% url 'index' %}" class="btn btn-secondary text-white" type=2
        <span class="text">Cancelar</span>3
    </a>4
5
    <button class="btn btn-primary" type="submit">6
        <span class="text">Registrar visitante</span>7
    </button>8
</div>9
Como a única maneira que podemos chegar até a página de registro de um 
novo visitante é pelo início da dashboard, faz sentido utilizarmos apenas um 
link ﬁxo para a home da dashboard
O template informacoes_visitante.html  já possui o botão com a ação voltar visível, 
mas não temos um link para onde o botão deve enviar o usuário. Vamos procurar pelo 
seguinte trecho de código e inserir o link para a URL index  em seu atributo href :
<div class="mr-1 text-right">1
    <a href="#" class="btn btn-secondary text-white" type="button">2
        <span class="text">Voltar</span>3
    </a>4
</div>5
O código ﬁcará assim:
<div class="mr-1 text-right">1
    <a href="{% url 'index' %}" class="btn btn-secondary text-white" type=2
        <span class="text">Voltar</span>3
    </a>4
</div>5
Melhorando a exibição do CPF do visitante

## Página 156

Uma outra melhoria interessante seria na exibição do CPF do visitante. Estamos exibindo 
os números todos sem nenhuma separação, como geralmente o número de CPF é 
apresentado. Aprendemos que é possível criar métodos nas classes modelo para alterar 
comportamentos e até já criamos métodos que utilizamos para melhorar a exibição de 
alguns atributos. Agora vamos criar o método get_cpf  que deverá retornar o CPF do 
visitante já formatado com pontos e traço.
Vamos abrir o arquivo models.py  e abaixo do método get_placa_veiculo  vamos criar o
método get_cpf  que, por enquanto, irá retornar o CPF caso o mesmo exista. O código 
ﬁcará assim:
# código acima omitido1
2
def get_placa_veiculo(self):3
    if self.placa_veiculo:4
        return self.placa_veiculo5
6
    return "Veículo não registrado"7
8
def get_cpf(self):9
    if self.cpf:10
        return self.cpf11
12
    return "CPF não registrado"13
14
# código abaixo omitido15
Conhecendo o f-strings do Python
Precisamos recortar a string algumas vezes, separar esses recortes e depois montar uma 
outra string com cada parte obedecendo aos pontos e ao traço do formato padrão para 
exibição de CPF (XXX.XXX.XXX-XX ). Esse processo pode parecer um pouco complicado 
mas não é.
Antes de tudo, vamos recortar as partes que compõem o CPF. Vamos utilizar os índices da 
variável cpf  (que será igual ao CPF do visitante) para recortar cada parte, os intervalos (
[0:3] , [3:6] , [6:9]  e [9:] ). Além disso, vamos também criar variáveis para 
guardar as partes do CPF:

## Página 157

def get_cpf(self):1
    if self.cpf:2
        cpf = str(self.cpf)3
        4
        cpf_parte_um = cpf[0:3]5
        cpf_parte_dois = cpf[3:6]6
        cpf_parte_tres = cpf[6:9]7
        cpf_parte_quatro = cpf[9:]8
        9
        # código abaixo omitido10
Com as quatro partes do CPF recortadas e guardadas em variáveis, temos agora que 
colocá-las em ordem no formato padrão do CPF. Para nos ajudar com isso, vamos utilizar 
um recurso do Python chamado strings literais ou f-strings .
Uma f-string (ou string literal) é toda cadeia de caracteres preﬁxada por f  ou F , onde 
pode conter também campos para substituição de variáveis ou expressões, delimitadas por
chaves {} . Utilizando uma string literal, podemos criar a string já formatada e inserir os 
intervalos recortados do CPF na ordem por meio dos campos de substituição. Abaixo 
temos a variável que vamos retornar no método, onde cada par de chaves {}  será 
substituído por um intervalo da string que representa o CPF do visitante:
cpf_formatado = f"{}.{}.{}-{}"
Agora vamos inserir as variáveis que representam as partes do CPF do vistante na ordem e 
dentro das chaves {}  da variável cpf_formatado , nossa string literal. E já que nosso 
objetivo é retornar o CPF já formatado, vamos retornar essa variável. O método ﬁcará 
assim:
def get_cpf(self):1
    if self.cpf:2
        cpf = self.cpf3
        4
        cpf_parte_um = cpf[0:3]5
        cpf_parte_dois = cpf[3:6]6
        cpf_parte_tres = cpf[6:9]7

## Página 158

        cpf_parte_quatro = cpf[9:]8
9
        cpf_formatado = f"{cpf_parte_um}.{cpf_parte_dois}.{cpf_parte_tres}10
11
        return cpf_formatado12
    13
    return "CPF não registrado"14
Feito isso, temos agora que substituir os acessos ao atributo cpf  do modelo pela 
chamada ao método get_cpf . Primeiro no template index.html  e depois no 
informacoes_visitante.html .
<!-- código acima omitido -->1
2
<tbody>3
    {% for visitante in pagina_obj %}4
        <tr>5
            <td>{{ visitante.nome_completo }}</td>6
            <td>{{ visitante.get_cpf }}</td>7
            8
            <!-- código abaixo omitido -->9
E agora no informacoes_visitante.html :
<!-- código acima omitido -->1
<div class="form-group col-md-6">2
    <label>CPF</label>3
    <input type="text" class="form-control" value="{{ visitante.get_cpf }}4
</div>5
<!-- código abaixo omitido -->6
Utilizando método para exibir o status do visitante
Ao contrário de alguns atributos que tivemos que criar métodos para exibi-los de maneira 
personalizada, para o atributo status  isso não é necessário.

## Página 159

Quando deﬁnimos as opções de escolha para o status , deﬁnimos uma string para ser 
salva no banco de dados e uma para funcionar como label  da string salva, como se 
fosse um nome descritivo mesmo. Por baixo dos panos o Django cria um método para 
exibir o label que nós deﬁnimos, bastando apenas que a gente utilize exatamente como 
ﬁzemos com os outros método. Por padrão, o nome do método é 
get_nomeatributo_display  que, para o nosso caso, é o get_status_display. 
Agora que sabemos como utilizar o método, vamos alterar alguns templates para que a 
gente exiba o status do visitante juntamente das informações do mesmo. Primeiro vamos 
abrir o arquivo informacoes_visitante.html  e procurar pelo seguinte trecho de código:
<div class="form-row">1
    <div class="form-group col-md-6">2
        <label>Horário de chegada</label>3
        <input type="text" class="form-control" value="{{ visitante.horari4
    </div>5
        6
    <div class="form-group col-md-6">7
        <label>Número da casa a ser visitada</label>8
        <input type="text" class="form-control" value="{{ visitante.numero9
    </div>10
</div>11
O trecho de código acima é o responsável por renderizar a primeira linha das informações 
gerais a respeito da visita no template em questão. Vamos alterá-lo para exibir ao lado do 
número da casa, o status em que o visitante se encontra. Para fazer isso, primeiro vamos 
alterar a classe col-md-6  presente nos elementos <div class="form-group col-md-6">  
para col-md-4 . Essa é uma classe de estilo do Bootstrap e nos ajuda a organizar as 
colunas de um template de modo que se dividam na tela. Caso você queira saber mais 
sobre o sistema de grid do Bootstrap, pode acessar esse link.
Feito isso, o que vamos fazer é inserir mais um elemento 
<div class="form-group col-md-4">  abaixo do que exiba o número da casa, desta vez 
para exibir o status do visitante. O código ﬁcará assim:
<div class="form-row">1
    <div class="form-group col-md-4">2

## Página 160

        <label>Horário de chegada</label>3
        <input type="text" class="form-control" value="{{ visitante.horari4
    </div>5
        6
    <div class="form-group col-md-4">7
        <label>Número da casa a ser visitada</label>8
        <input type="text" class="form-control" value="{{ visitante.numero9
    </div>10
    11
    <div class="form-group col-md-4">12
        <label>Status</label>13
        <input type="text" class="form-control" value="{{ visitante.get_st14
    </div>15
</div>16
Agora só precisamos inserir mais uma coluna na tabela do template index.html  para 
exibir o status do usuário logo ali na página inicial. Primeiro vamos procurar pelo elemento 
<thead>  e, abaixo do elemento <th>  com o texto "Horário de chegada", vamos inserir 
um elemento <th>  com texto "Status". O código ﬁcará assim:
<thead>1
    <th>Nome</th>2
    <th>CPF</th>3
    <th>Horário de chegada</th>4
    <th>Status</th>5
    <th>Horário da autorização</th>6
    <th>Autorizado por</th>7
    <th>Mais informações</th>8
</thead>9
Agora, claro, vamos adicionar também uma linha que será responsável por exibir o status 
utilizando o método get_status_display . Ficará assim: 
{% for visitante in pagina_obj %}1
    <tr>2
        <td>{{ visitante.nome_completo }}</td>3
        <td>{{ visitante.get_cpf }}</td>4
        <td>{{ visitante.horario_chegada }}</td>5
        <td>{{ visitante.get_status_display }}</td>6
        <td>{{ visitante.get_horario_autorizacao }}</td>7

## Página 161

        <td>{{ visitante.get_morador_responsavel }}</td>8
        <td>9
            <a href="{% url 'informacoes_visitante' id=visitante.id %}">10
                Ver informações11
            </a>12
        </td>13
    </tr>14
{% endfor %}15
Implementando melhorias na estrutura do nosso projeto
 
Uma alteração interessante que vamos implementar é criar uma pasta de nome apps  na 
raiz do nosso projeto para agrupar todos os nossos aplicativos. Vamos começar alterando 
o arquivo settings.py . Vamos importar o módulo sys  e depois adicionar a pasta 
apps  ao projeto.
import os1
import sys2
3
# código abaixo omitido4
Feito isso tudo que precisamos fazer é adicionar a seguinte linha de código abaixo da 
variável ALLOWED_HOSTS :
sys.path.append(1
    os.path.join(BASE_DIR, "apps")2
)3
Agora, vamos criar a pasta apps e mover as pastas dos nossos aplicativos para ela.

## Página 162

Capítulo 14
Captura de tela realizada a partir do template inicial da dashboard onde foca apenas nos 
blocos que exibem o número de visitantes aguardando autorização, em visita, visita 
ﬁnalizada e o total de visitantes registrados no mês
Criando aplicativo para administrar informações da 
dashboard
No capítulo anterior nós começamos a implementar algumas melhorias visando uma 
melhor experiência de utilização da nossa dashboard e ainda atuamos de forma a 
melhorar a estrutura do projeto para facilitar futuras manutenções. Seguindo nesse mesmo
caminho, vamos criar um aplicativo chamado dashboard para administrar melhor as 
informações relacionadas principalmente à página inicial da dashboard. É importante 
também a gente lembrar que os aplicativos de um projeto Django devem dividir 
responsabilidades e cada um deles ter um único objetivo. 
Apesar da gente ter ﬁnalizado as principais funcionalidades, ainda precisamos buscar 
alguns números para que sejam mostrados na página inicial. Se você observar o template, 
vai perceber que existem elementos que nos sugerem que devemos exibir o número de 
visitantes de cada status e quantos visitantes foram registrados no mês atual. Queremos 
fazer algo desse tipo, mas com dados dinâmicos:
Todas essas informações podem ser tiradas a partir da queryset que busca 
todos os visitantes no banco de dados. Em breve vamos aprender como 
podemos fazer isso e tornar os dados na nossa dashboard dinâmicos.
Para começar vamos criar o aplicativo utilizando o manage.py :

## Página 163

(env)$ python manage.py startapp dashboard
E depois adicionar o novo aplicativo ao arquivo de conﬁgurações, o settings.py :
INSTALLED_APPS += [1
    "usuarios",2
    "porteiros",3
    "visitantes",4
    "dashboard",5
]6
Não vamos executar as operações makemigrations  e migrate  pois não 
ﬁzemos nenhuma alteração relacionada com o banco de dados. Estamos 
apenas acessando e buscando os dados já existentes.
Migrando view "index" para aplicativo dashboard
 
Agora que nós temos um aplicativo para gerenciar as informações da nossa dashboard, 
vamos migrar a função de view index  para o aplicativo dashboard. Para isso, vamos 
copiar o código do arquivo usuarios/views.py  para dashboard/views.py . O arquivo 
views.py  do aplicativo usuários (usuarios/views.py ) ﬁcará vazio e o arquivo 
views.py  do aplicativo dashboard (dashboard/views.py ) ﬁcará assim:
from django.shortcuts import render1
from visitantes.models import Visitante2
3
def index(request):4
5
    todos_visitantes = Visitante.objects.all()6
7
    context = {8

## Página 164

        "nome_pagina": "Início da dashboard",9
        "todos_visitantes": todos_visitantes,10
    }11
12
    return render(request, "index.html", context)13
Para ﬁnalizar a migração da nossa view, vamos também alterar o arquivo urls.py . Ao 
invés de usuarios.views  vamos importar a nossa função de dashboard.views . O 
arquivo ﬁcará assim:
from django.contrib import admin1
from django.urls import path2
3
from dashboard.views import index4
5
from visitantes.views import (6
    registrar_visitante,7
    informacoes_visitante,8
    finalizar_visita,9
)10
11
urlpatterns = [12
    path("admin/", admin.site.urls),13
14
    path(15
        "",16
        index,17
        name="index"18
    ),19
    20
    # código abaixo omitido21
]22
Conhecendo o método ﬁlter das querysets
 
Agora que migramos a view para o aplicativo dashboard, vamos conhecer métodos para 
ﬁltrar os visitantes de modo que a gente consiga buscar e exibir os dados que precisamos: 
o número de visitantes em cada status e o número total de visitantes registrados no mês 
atual.

## Página 165

O primeiro método das querysets que vamos conhecer é o método filter() . Ele nos 
ajuda a ﬁltrar os resultados de uma queryset. Nos capítulos anteriores aprendemos que 
toda busca no banco de dados retorna uma queryset, um tipo especíﬁco do Django, e que 
podemos manipular esses resultados.
Na view que estamos trabalhando já existe uma queryset, que é a variável 
todos_visitantes . Ela guarda a lista de todos os visitantes existentes em nosso banco 
de dados, o que precisamos fazer é ﬁltrar essa lista de modo que seja possível classiﬁcar 
os visitantes por status. Ou seja, precisamos ter uma lista de visitantes com status 
aguardando, outra de visitantes com status em visita e outra com as visitas ﬁnalizadas.
Filtrando nossos visitantes por status
O primeiro passo será criar uma variável para receber os resultados. Vamos utilizar o nome 
visitantes_aguardando  pois por agora queremos apenas os visitantes que estão com o 
status AGUARDANDO . Para fazer isso vamos utilizar o método filter()  na variável 
todos_visitantes  passando a condição status="AGUARDANDO" como argumento para o 
método. Isto é, vamos ﬁltrar da queryset todos_visitantes  apenas os visitantes que 
estão com status  igual a AGUARDANDO .
def index(request):1
    2
    todos_visitantes = Visitante.objects.all()3
    4
    visitantes_aguardando = todos_visitantes.filter(5
        status="AGUARDANDO"6
    )7
    8
    context = {9
        "nome_pagina": "Início da dashboard",10
        "todos_visitantes": todos_visitantes,11
    }12
    13
    return render(request, "index.html", context)14
Vamos fazer isso com todos os outros status para que possamos ter uma lista de 
visitantes para cada status e passar as variáveis criadas para o contexto da função.

## Página 166

def index(request):1
    2
    todos_visitantes = Visitante.objects.all()3
    4
    # filtrando os visitantes por status5
    visitantes_aguardando = todos_visitantes.filter(6
        status="AGUARDANDO"7
    )8
9
    visitantes_em_visita = todos_visitantes.filter(10
        status="EM_VISITA"11
    )12
13
    visitantes_finalizado = todos_visitantes.filter(14
        status="FINALIZADO"15
    )16
    17
    context = {18
        "nome_pagina": "Início da dashboard",19
        "todos_visitantes": todos_visitantes,20
        "visitantes_aguardando": visitantes_aguardando,21
        "visitantes_em_visita": visitantes_em_visita,22
        "visitantes_finalizado": visitantes_finalizado,23
    }24
    25
    return render(request, "index.html", context)26
Contando os resultados de uma queryset
Agora que nós já ﬁltramos os visitantes por status, precisamos contar quantos registros 
existem em cada queryset, certo? É isso que o método count()  faz por nós. Tudo que 
precisamos fazer é utilizá-lo nas querysets visitantes_aguardando , 
visitantes_em_visita  e visitantes_finalizado . Podemos fazer isso no contexto 
mesmo:
context = {1
    "nome_pagina": "Início da dashboard",2
    "todos_visitantes": todos_visitantes,3
    "visitantes_aguardando": visitantes_aguardando.count(),4
    "visitantes_em_visita": visitantes_em_visita.count(),5
    "visitantes_finalizado": visitantes_finalizado.count(),6
}7

## Página 167

Feito isso, agora nós vamos exibir essas variáveis no template. Vamos abrir o template 
index.html  e utilizar a sintaxe para exibição de variáveis. O trecho de código ﬁcará 
assim:
<div class="row">1
    <div class="col-xl-3 col-md-6 mb-4">2
        <div class="card border-left-warning shadow h-100 py-2">3
            <div class="card-body">4
                <div class="row no-gutters align-items-center">5
                    <div class="col mr-2">6
                        <div class="text-xs font-weight-bold text-warning 7
                        <div class="h5 mb-0 font-weight-bold text-gray-8008
                    </div>9
                        10
                    <div class="col-auto">11
                        <i class="fas fa-user-lock fa-2x text-gray-300"></12
                    </div>13
                </div>14
            </div>15
        </div>16
    </div>17
18
    <div class="col-xl-3 col-md-6 mb-4">19
        <div class="card border-left-primary shadow h-100 py-2">20
            <div class="card-body">21
                <div class="row no-gutters align-items-center">22
                    <div class="col mr-2">23
                        <div class="text-xs font-weight-bold text-primary 24
                        <div class="h5 mb-0 font-weight-bold text-gray-80025
                    </div>26
                        27
                    <div class="col-auto">28
                        <i class="fas fa-user-clock fa-2x text-gray-300"><29
                    </div>30
                </div>31
            </div>32
        </div>33
    </div>34
35
    <div class="col-xl-3 col-md-6 mb-4">36
        <div class="card border-left-success shadow h-100 py-2">37
            <div class="card-body">38
                <div class="row no-gutters align-items-center">39
                    <div class="col mr-2">40
                        <div class="text-xs font-weight-bold text-success 41
                        <div class="h5 mb-0 font-weight-bold text-gray-80042

## Página 168

                    </div>43
                    <div class="col-auto">44
                        <i class="fas fa-user-check fa-2x text-gray-300"><45
                    </div>46
                </div>47
            </div>48
        </div>49
    </div>50
        51
    <div class="col-xl-3 col-md-6 mb-4">52
        <div class="card border-left-info shadow h-100 py-2">53
            <div class="card-body">54
                <div class="row no-gutters align-items-center">55
                    <div class="col mr-2">56
                        <div class="text-xs font-weight-bold text-info tex57
                        <div class="h5 mb-0 font-weight-bold text-gray-80058
                    </div>59
                    <div class="col-auto">60
                        <i class="fas fa-users fa-2x text-gray-300"></i>61
                    </div>62
                </div>63
            </div>64
        </div>65
    </div>66
</div>67
Se você atualizar a página inicial da dashboard, vai observar que agora os números estão 
dinâmicos e aparecendo conforme os registros do nosso banco de dados. Foi bem 
tranquilo resolver essa, certo? Então vamos para o próximo desaﬁo!

## Página 169

Capítulo 15
Aprendendo a ﬁltrar nossos visitantes por data
No capítulo anterior nós aprendemos um pouco sobre os métodos filter()  e count()  
e até já ﬁltramos os visitantes por status. Agora o que precisamos fazer é ﬁltrar os 
visitantes com base na data em que o mesmo foi cadastrado para que depois seja possível
ﬁltramos esses registros por um mês em especíﬁco, que é o nosso objetivo.
Para fazer isso, vamos novamente utilizar o método filter() , mas dessa vez passando 
uma condição diferente, pois agora o que queremos é ﬁltrar pela data de chegada. Por 
hora, vamos somente passar uma data para que o Django ﬁltre somente os visitantes 
registrados nessa data em especíﬁco
Conhecendo o ﬁeld lookups da Queryset API
 
Antes de ﬁltrar o horário de chegada pela data, precisamos conhecer os field lookups . 
Eles são ﬁltros que nos possibilitam especiﬁcar algumas condições para nossos campos 
ou acessar propriedades. Por exemplo, nosso campo horario_chegada  também recebe 
uma data, pois é do tipo DateTimeField . Sendo assim, podemos acessar somente a data 
existente no valor do campo.
Podemos utilizá-los com alguns métodos das querysets e entre eles o método filter() . 
Nós vamos utilizar __  após o nome do atributo que passamos como condição para o 
método filter() . Se a gente quiser ﬁltrar os visitantes pela data contida no atributo 
horario_chegada , podemos fazer isso:
visitantes_mes = todos_visitantes.filter(1
    horario_chegada__date="2020-04-04"2
)3

## Página 170

Nesse caso, estamos buscando apenas os visitantes que foram registrados no dia 04 de 
maio de 2020. Existem vários outros lookups e cada tipo de campo possui os seus.
Filtrando apenas os registros do mês atual
 
Agora que sabemos que é possível ﬁltrar por propriedades contidas em alguns atributos e 
até ﬁltramos os visitantes de um dia especíﬁco, vamos conhecer um outro field lookup , 
o month . Assim como nós podemos buscar somente pela data, que está contida no 
DateTimeField , podemos também buscar pelo mês, que é o que esse lookup faz. Dessa 
vez vamos buscar todos os visitantes registrados no mês de maio (mês 05).
visitantes_mes = todos_visitantes.filter(1
    horario_chegada__month="05"2
)3
Utilizando o timezone para descobrir o mês atual
Descobrimos como ﬁltrar nossos visitantes pelo mês em que foram registrados, mas ainda 
precisamos fazer com que o método ﬁltre os visitantes do mês atual de forma automática, 
isto é, que o mês atual seja reconhecido e passado para o método filter()  como uma 
variável.
Para fazer isso vamos utilizar um velho conhecido, o timezone.now() . Esse método 
retorna o valor referente a data e hora em que foi invocado e, a partir dessa data e hora, 
podemos buscar o mês. Para importar o módulo timezone  basta utilizar o seguinte 
código:
from django.utils import timezone
Feito isso, vamos criar a variável hora_atual  sendo igual ao método timezone.now()  e 
depois acessar a propriedade month  da variável hora_atual  para passá-la à variável 

## Página 171

que vamos criar de nome mes_atual .
# filtrando visitantes por data (mês atual)1
hora_atual = timezone.now()2
mes_atual = hora_atual.month3
4
visitantes_mes = todos_visitantes.filter(5
    horario_chegada__month=mes_atual6
)7
Agora temos o valor referente ao mês atual numa variável e podemos passá-la como valor 
para a condição do método filter() . Com isso nós já temos uma lista com os visitantes 
que foram registrados no mês atual. Vamos agora passar essa variável no contexto da 
função e depois exibi-la no template.
context = {1
    "nome_pagina": "Página inicial",2
    "visitantes": visitantes,3
    "visitantes_aguardando": visitantes_aguardando.count(),4
    "visitantes_em_visita": visitantes_em_visita.count(),5
    "visitantes_finalizado": visitantes_finalizado.count(),6
    "visitantes_mes": visitantes_mes.count(),7
}8
Agora vamos voltar para o arquivo index.html  e alterar o último trecho, onde vamos 
exibir a quantidade de visitantes registrados no mês atual:
<div class="col-xl-3 col-md-6 mb-4">1
    <div class="card border-left-info shadow h-100 py-2">2
        <div class="card-body">3
            <div class="row no-gutters align-items-center">4
                <div class="col mr-2">5
                    <div class="text-xs font-weight-bold text-info text-up6
                    <div class="h5 mb-0 font-weight-bold text-gray-800">{{ 7
                </div>8
9
                <div class="col-auto">10
                    <i class="fas fa-users fa-2x text-gray-300"></i>11

## Página 172

                </div>12
            </div>13
        </div>14
    </div>15
</div>16
Ao voltar para a página inicial da dashboard, o número de visitantes registrados no mês já 
estará sendo exibido.
Ordenando nossa lista de visitantes por horário de chegada
 
O último passo antes da gente ﬁnalizar mais um capítulo é ordenar a lista de visitantes 
recentes por horário de chegada. Isto é, queremos que os registros de visitantes sigam uma 
certa ordem e essa ordem seja baseada no horário de chegada, de forma que os registros 
mais recentes ﬁquem sempre no topo.
Para isso vamos utilizar o método order_by()  que funciona de forma parecida com o 
filter() , com a diferença que precisamos passar somente o nome do atributo que 
queremos utilizar como parâmetro. Vamos utilizá-lo em substituição ao método all() : 
todos_visitantes = Visitante.objects.order_by(1
    "-horario_chegada"2
)3
Note que estamos utilizando o operador (- ) antes do nome do atributo 
horario_chegada . O operador utilizado dessa forma faz com que os registros sejam 
listados em ordem descendente que, para data, tem o comportamento de ordenar do 
registro mais recente para o mais antigo.

## Página 173

Capítulo 16
Bloqueando o acesso para usuários não autenticados nas 
nossas views
Estamos chegando na reta ﬁnal do nosso projeto. Todos os requisitos descritos estão 
implementados e agora nós vamos cuidar de alguns requisitos que são chamados não 
funcionais. Esse tipo de requisito raramente é descrito mas está presente em praticamente 
todas as aplicações web existentes: telas de login, telas de logout e o bloqueio do acesso 
não autenticado a páginas com informações delicadas, por exemplo.
Daqui pra frente cuidaremos dos requisitos mencionados e vamos conhecer alguns 
recursos bem interessantes do Django que vão nos ajudar a poupar bastante tempo. O 
Django possui embutido em suas funcionalidades, alguns módulos voltados para a 
criação, administração e autenticação de usuários, conhecido por sistema de autenticação 
do Django. O comando createsuperuser , por exemplo, faz parte de suas 
funcionalidades.
Pense na dashboard que estamos criando: as informações que estamos exibindo ali são 
conﬁdenciais e não devem ﬁcar expostas para que qualquer um possa encontrá-las na 
web. Desta forma, nós precisamos bloquear as URLs para que somente usuários 
autenticados com e-mail e senha possam ter acesso e visualizar essas informações.
Conhecendo o decorator login_required
Para bloquear o acesso não autenticado às views, o Django nos fornece um caminho 
rápido para que a gente consiga implementar essa funcionalidade. Nós vamos utilizar o 
decorator login_required  para tornar nossas views acessíveis somente após 
autenticação. Caso o usuário não esteja autenticado, não poderá acessar a view e será 
direcionado para uma tela de login.
Um decorator nada mais é que um método que envolve e modiﬁca comportamentos de 
uma função. É isso que estamos fazendo: pedindo que o decorator login_required  faça 
a função ser acessível somente após autenticação e, com isso, estamos alterando o 
comportamento da função.

## Página 174

Para utilizar esse decorator vamos primeiro importá-lo no topo do arquivo views.py  do 
aplicativo dashboard:
from django.shortcuts import render1
from django.contrib.auth.decorators import login_required2
3
# código abaixo omitido4
Agora tudo que precisamos fazer é colocar um @  antes do nome do decorator em cima da
função index . O código ﬁcará assim:
@login_required1
def index(request):2
    3
    todos_visitantes = Visitante.objects.order_by(4
        "-horario_chegada"5
    )6
7
    # filtrando os visitantes por status8
    visitantes_aguardando = todos_visitantes.filter(9
        status="AGUARDANDO"10
    )11
12
    visitantes_em_visita = todos_visitantes.filter(13
        status="EM_VISITA"14
    )15
16
    visitantes_finalizado = todos_visitantes.filter(17
        status="FINALIZADO"18
    )19
20
    # filtrando visitantes por data (mês atual)21
    hora_atual = timezone.now()22
    mes_atual = hora_atual.month23
24
    visitantes_mes = todos_visitantes.filter(25
        horario_chegada__month=mes_atual26
    )27
    28
    context = {29
        "nome_pagina": "Início da dashboard",30
        "todos_visitantes": todos_visitantes,31
        "visitantes_aguardando": visitantes_aguardando.count(),32

## Página 175

        "visitantes_em_visita": visitantes_em_visita.count(),33
        "visitantes_finalizado": visitantes_finalizado.count(),34
        "visitantes_mes": visitantes_mes.count(),35
    }36
    37
    return render(request, "index.html", context)38
Agora, se você tentar acessar a URL http://127.0.0.1:8000/ sem estar autenticado, o 
Django irá exibir uma mensagem de erro. Esse erro ocorre porque quando utilizamos o 
decorator login_required , também é necessário conﬁgurar a URL de login e a URL para 
qual o usuário deverá ser direcionado após se autenticar.
Caso esteja autenticado, vá até o admin e clique em "encerrar sessão" ou cliquei 
nesse link: http://127.0.0.1:8000/admin/logout/
Vamos fazer isso em todas as view criadas que fazem parte da dashboard. São elas: 
registrar_visitante , informacoes_visitante  e finalizar_visita .
Alterando a URL padrão para login e redirecionamento 
após login
 
Agora que bloqueamos o acesso às views utilizando o decorator, precisamos deﬁnir as 
informações citadas anteriormente no arquivo settings.py . Vamos conﬁgurar as 
variáveis LOGIN_URL  e LOGIN_REDIRECT_URL . e deﬁnir seus valores como "login"  e 
"index" . O arquivo ﬁcará assim:
# código acima omitido1
STATICFILES_DIRS = [2
    os.path.join(BASE_DIR, "static")3
]4
5
LOGIN_URL = "login"6
LOGIN_REDIRECT_URL = "index"7

## Página 176

# código abaixo omitido8
Não se preocupe com a URL login. Vamos criá-la no próximo passo.
Utilizando o sistema de autenticação do Django para nos 
fornecer a view de login
 
Conforme dito, vamos utilizar o sistema de autenticação do Django para nos ajudar com 
todo código necessário para autenticar e deslogar os usuários da nossa dashboard. Para 
começar vamos abrir o arquivo urls.py  e importar os seguinte módulo:
from django.contrib import admin1
from django.urls import path2
3
from django.contrib.auth import views as auth_views4
5
import dashboard.views6
import visitantes.views7
8
# código abaixo omitido9
O que estamos fazendo é importar o arquivo de views do módulo django.contrib.auth . 
Fazendo isso, nós podemos utilizar as funções e classes disponíveis no módulo 
django.contrib.auth.views . Abaixo da função path()  que deﬁne a URL para o admin, 
vamos deﬁnir a nossa URL de login:
urlpatterns = [1
    path("admin/", admin.site.urls),2
3
    path(4
        "login/",5
        auth_views.LoginView.as_view(6
            template_name="login.html"7
        ),8
        name="login"9

## Página 177

    ),10
    11
    # código abaixo omitido12
]13
Como importamos o arquivo inteiro com o nome de auth_views , vamos acessar suas 
funções e classes por meio desse nome. Note que no lugar da view que deveríamos passar 
para a função path() , estamos passando uma classe existente no módulo auth_views  
e utilizando seu método as_view() . Esse método nos permite utilizar as views padrões 
do Django para autenticação que ainda nos permitem criar um template personalizado. O 
argumento template_name  serve para que a gente diga para o Django qual template deve 
ser utilizado na view.
Com essa conﬁguração, já temos uma URL de login. Agora precisamos de um template, 
claro.
Criando o template de login
 
Vamos criar o arquivo login.html  com o seguinte código:
<!DOCTYPE html>1
2
{% load static %}3
{% load widget_tweaks %}4
5
<html lang="pt-br">6
    <head>7
        <meta charset="utf-8">8
        <meta http-equiv="X-UA-Compatible" content="IE=edge">9
        <meta name="viewport" content="width=device-width, initial-scale=110
        11
        <title>Controle de Visitantes | Autenticação</title>12
        13
        <link href="https://fonts.googleapis.com/css?family=Nunito:200,20014
        15
        <link href="{% static 'css/sb-admin-2.min.css' %}" rel="stylesheet16
        <link href="{% static 'vendor/fontawesome-free/css/all.min.css' %}17
    </head>18

## Página 178

19
    <body class="bg-gradient-primary">20
        <div class="container">21
            <div class="row justify-content-center">22
                <div class="col-xl-10 col-lg-12 col-md-9">23
                    <div class="card o-hidden border-0 shadow-lg my-5">24
                        <div class="card-body p-0">25
                            <div class="row">26
                                <div class="col-lg-6 d-none d-lg-block bg-27
    28
                                <div class="col-lg-6">29
                                    <div class="p-5">30
                                        <div class="text-left mb-5">31
                                            <h1 class="h4 text-gray-900 mb32
    33
                                            <p>Faça login para continuar</34
                                        </div>35
    36
                                        <form method="post" class="user">37
                                            <p>ué cadê o formulário?</p>38
    39
                                            <button class="btn btn-primary 40
                                                <span class="text">Acessar 41
                                            </button>42
                                        </form>43
                                    </div>44
                                </div>45
                            </div>46
                        </div>47
                    </div>48
                    49
                </div>50
                51
            </div>52
        </div>53
        54
        <script src="{% static 'vendor/jquery/jquery.min.js' %}"></script>55
        <script src="{% static 'vendor/bootstrap/js/bootstrap.bundle.min.j56
        <script src="{% static 'js/sb-admin-2.min.js' %}"></script>57
    </body>58
</html>59
Se você preferir, pode fazer download do arquivo zipado e colocar na pasta templates do 
seu projeto clicando no link abaixo:

## Página 179

Iniciar o download login.zip - 1KB
Renderizando formulário de login
Quando utilizamos a classe LoginView  o Django nos dá tudo que precisamos para exibir 
o template, tratar a requisição, os possíveis erros do formulário e ainda autenticar o 
usuário. Junto disso tudo, temos a possibilidade de utilização da variável form  que 
representa nosso formulário de autenticação.
Quando criamos nosso modelo personalizado de usuário, o Django preparou um 
formulário baseado nesse modelo, de forma bem parecida com que ﬁzemos nos 
formulários que criamos. Vamos utilizar a mesma estratégia que utilizamos para 
renderizar o formulário de registro de visitante. O código do formulário ﬁcará assim e 
deverá substituir o elemento <p>  dentro do <form> :
<div class="form-row">1
    {% csrf_token %}2
                        3
    {% for field in form %}4
        <div class="form-group col-md-12">5
            {% render_field field placeholder=field.label class="form-cont6
        </div>7
    {% endfor %}8
</div>9
Vamos acessar novamente a URL http://127.0.0.1:8000/ e agora podemos notar que 
fomos direcionados para a tela de login que acabamos de criar. Essa é a nossa tela de 
login:

## Página 180

Página de login com escritos de boas vindas e um formulário contendo E-mail e Senha, 
além do botão azul para acesso à dashboard escrito "Acessar dashboard". O fundo da tela 
é azul e há também a foto de uma cachorrinho ao lado do formulário, como se estivesse 
encarando o usuário
Adicionando mensagem de erro em formulário de login
 
Agora que estamos exibindo nosso formulário, vamos adicionar só mais uma coisa no 
template: um alerta para caso o formulário retorne algum erro. Dessa vez vamos apenas 
informar que o e-mail ou a senha estão incorretos. O template completo ﬁcará assim:
<!DOCTYPE html>1
2
{% load static %}3
{% load widget_tweaks %}4
5
<html lang="pt-br">6
    <head>7
        <meta charset="utf-8">8
        <meta http-equiv="X-UA-Compatible" content="IE=edge">9
        <meta name="viewport" content="width=device-width, initial-scale=110
        11
        <title>Controle de Visitantes | Autenticação</title>12
        13
        <link href="https://fonts.googleapis.com/css?family=Nunito:200,20014

## Página 181

        15
        <link href="{% static 'css/sb-admin-2.min.css' %}" rel="stylesheet16
        <link href="{% static 'vendor/fontawesome-free/css/all.min.css' %}17
    </head>18
19
    <body class="bg-gradient-primary">20
        <div class="container">21
            <div class="row justify-content-center">22
                <div class="col-xl-10 col-lg-12 col-md-9">23
                    <div class="card o-hidden border-0 shadow-lg my-5">24
                        <div class="card-body p-0">25
                            <div class="row">26
                                <div class="col-lg-6 d-none d-lg-block bg-27
    28
                                <div class="col-lg-6">29
                                    <div class="p-5">30
                                        <div class="text-left mb-5">31
                                            <h1 class="h4 text-gray-900 mb32
    33
                                            <p>Faça login para continuar</34
                                        </div>35
                                        36
                                        {% if form.errors %}37
                                            <div class="alert alert-warnin38
                                                E-mail ou senha incorretos39
                                            </div>40
                                        {% endif %}41
    42
                                        <form method="post" class="user">43
                                            <div class="form-row">44
                                                {% csrf_token %}45
                                                                    46
                                                {% for field in form %}47
                                                    <div class="form-group 48
                                                        {% render_field fi49
                                                    </div>50
                                                {% endfor %}51
                                            </div>52
    53
                                            <button class="btn btn-primary 54
                                                <span class="text">Acessar 55
                                            </button>56
                                        </form>57
                                    </div>58
                                </div>59
                            </div>60
                        </div>61
                    </div>62
                </div>63
            </div>64
        </div>65

## Página 182

        66
        <script src="{% static 'vendor/jquery/jquery.min.js' %}"></script>67
        <script src="{% static 'vendor/bootstrap/js/bootstrap.bundle.min.j68
        <script src="{% static 'js/sb-admin-2.min.js' %}"></script>69
    </body>70
</html>71
Com o template ﬁnalizado, vamos novamente tentar acessar a URL http://127.0.0.1:8000/. 
Dessa vez, quando formos direcionados para a tela de login, vamos utilizar as credenciais 
que criamos (e-mail e senha) e acessar o sistema.
Criando URL para logout
 
Com a tela de login criada, vamos trabalhar para também criar a tela de logout, que será 
útil para quando o usuário quiser sair da dashboard. 
Antes de tudo, vamos criar a URL de logout  quase da mesma forma com que criamos a 
URL de login. Vamos abrir o arquivo urls.py  e utilizar a função path  para criar a URL 
logout . O Código ﬁcará assim:
# código acima omitido1
2
urlpatterns = [3
    path("admin/", admin.site.urls),4
5
    path(6
        "login/",7
        auth_views.LoginView.as_view(8
            template_name="login.html"9
        ),10
        name="login"11
    ),12
13
    path(14
        "logout/",15
        auth_views.LogoutView.as_view(16
            template_name="logout.html"17
        ),18
        name="logout"19

## Página 183

    ),20
    21
    # código abaixo omitido22
]23
Note que dessa vez estamos utilizando a classe LogoutView .
Criando template de logout
 
O processo será bem parecido com o executado para criação da URL da login. Como já 
criamos a URL, vamos agora partir para a criação do template que deverá ser exibido 
quando a URL logout  for acessada. Vamos criar o arquivo logout.html  na pasta 
templates com o seguinte código:
<!DOCTYPE html>1
2
{% load static %}3
{% load widget_tweaks %}4
5
<html lang="pt-br">6
    <head>7
        <meta charset="utf-8">8
        <meta http-equiv="X-UA-Compatible" content="IE=edge">9
        <meta name="viewport" content="width=device-width, initial-scale=110
        11
        <title>Controle de Visitantes | Logout</title>12
        13
        <link href="https://fonts.googleapis.com/css?family=Nunito:200,20014
        15
        <link href="{% static 'css/sb-admin-2.min.css' %}" rel="stylesheet16
        <link href="{% static 'vendor/fontawesome-free/css/all.min.css' %}17
    </head>18
19
    <body class="bg-gradient-primary">20
        <div class="container">21
            <div class="row justify-content-center">22
                <div class="col-xl-10 col-lg-12 col-md-9">23
                    <div class="card o-hidden border-0 shadow-lg my-5">24
                        <div class="card-body p-0">25
                            <div class="row">26
                                <div class="col-lg-6 d-none d-lg-block bg-27

## Página 184

    28
                                <div class="col-lg-6">29
                                    <div class="p-5">30
                                        <div class="text-left mb-5">31
                                            <h1 class="h4 text-gray-900 mb32
    33
                                            <p>Você escolheu sair da dashb34
                                        </div>35
    36
                                        <a href="{% url 'login' %}" class=37
                                            <span class="text">Voltar para 38
                                        </a>39
                                    </div>40
                                </div>41
                            </div>42
                        </div>43
                    </div>44
                </div>45
            </div>46
        </div>47
        48
        <script src="{% static 'vendor/jquery/jquery.min.js' %}"></script>49
        <script src="{% static 'vendor/bootstrap/js/bootstrap.bundle.min.j50
        <script src="{% static 'js/sb-admin-2.min.js' %}"></script>51
    </body>52
</html>53
Nosso template de logout exibe apenas uma mensagem dizendo que o usuário saiu do 
sistema e mostra um botão para ele voltar para a página de login, caso queira.
Mais uma vez, se você preferir, você pode fazer o download do arquivo zipado:
Iniciar o download logout.zip - 1KB
Inserindo link para logout em dashboard
 
Se em algum momento anterior você clicou no ícone da engrenagem, no canto superior 
direito, descobriu o botão sair .  Ele abre um modal pedindo que o usuário conﬁrme se 
realmente deseja sair:

## Página 185

Template da página inicial da dashboard ao fundo com um alerta pedindo a conﬁrmação 
de que o usuário realmente deseja sair do sistema
Vamos inserir o link para a página logout no botão que conﬁrma a ação que o usuário 
deseja sair. No template base.html , vamos procurar pelo modal de id logoutModal  e 
depois o link "sair" dentro do elemento <div class="modal-footer"> . O HTML do botão 
ﬁcará assim:
<a class="btn btn-primary" href="{% url 'logout' %}">Sair</a>
Com isso, quando o usuário clicar no botão "sair" conﬁrmando que deseja sair da 
dashboard, será direcionado para a página de logout.

## Página 186

Tela de logout contendo uma mensagem de despedida e dizendo que o usuário pode clicar 
no botão abaixo para retornar à página de login. Abaixo um botão azul escrito "Voltar para 
login" e à esquerda a foto do cachorro como na página de login


## Página 187

Capítulo ﬁnal
Chegamos ao capítulo ﬁnal da nossa apostila e agora temos um projeto web completo 
pronto para ser implantado em ambiente de produção. Tudo isso feito com Python e o 
Django framework.
Nossa aplicação web administra todo o ﬂuxo de entrada e saída de visitantes do 
condomínio, possibilitando desde o registro dos visitantes e exibição de informações, até 
as funcionalidades de autorização de entrada e ﬁnalização de visita.
No decorrer do material utilizamos os vários recursos que o Django nos fornece e 
aprendemos a utilizar as principais ferramentas na prática com o projeto que 
desenvolvemos. Daqui para frente, ainda temos muito chão para trilhar, é claro, mas com 
certeza iniciamos com uma base sólida que será aproveitada para os próximos projetos e 
estudos, por isso, não pare por aqui.
Eu espero que você tenha aproveitado e gostado de ter passado essas horas aqui comigo 
aprendendo sobre Django framework e, se você quiser aprender mais, continue 
acompanhando as redes sociais e o youtube:
Twitter
Github
Em caso de dúvidas, o fórum está à disposição para que possamos aproveitar ao máximo 
o espaço e resolver as dúvidas de todos.
Um forte abraço e nos vemos por aí!