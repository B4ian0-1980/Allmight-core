---json
{
  "id": "postgresql_banco_de_dados_para_aplica__es_web_modernas",
  "title": "ISBN",
  "categoria": "05-banco-dados",
  "subcategoria": "postgresql",
  "resumo": "Guia tecnico e referencias sobre ISBN.",
  "gatilhos": [
    "aplica",
    "banco",
    "dados",
    "isbn",
    "modernas",
    "para",
    "postgresql",
    "web"
  ],
  "perguntas_tipo": [
    "Como utilizar ISBN?",
    "Quais as boas praticas de postgresql?"
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
  "dono": "stack-postgresql",
  "prioridade": 2
}
---


--------------------------------------------------


--------------------------------------------------

Impresso e PDF: 978-85-5519-255-5

EPUB: 978-85-5519-256-2

MOBI: 978-85-5519-257-9

Você pode discutir sobre este livro no Fórum da Casa do
Código: http://forum.casadocodigo.com.br/.

Caso você deseje submeter alguma errata ou sugestão, acesse
http://erratas.casadocodigo.com.br.

# ISBN


--------------------------------------------------

Eu sempre consumi muitos livros de desenvolvimento de
software brasileiros. Antes de conhecer a Casa do Código, eu tinha
uma grande frustação com os livros dedicados ao desenvolvimento
de software em português, e até mesmo com alguns internacionais.

Se você já leu algum livro da Casa do Código, ele é diferente
desde a capa e todo seu conteúdo. Tem uma abordagem mais
moderna e menos ortodoxa do que os outros livros possuem. Pois,
na minha opinião, livros da área de desenvolvimento de software
deveriam ter essa pegada mais leve e gostosa de ler.

E o que me levou a escrever meu primeiro livro, lançado em
2015 pela Casa do Código, foi a vontade de criar um que eu gostaria
de ler. Isso quer dizer, com um conteúdo prático, que o leitor
pudesse se desenvolver nível a nível sem se frustrar com o que
estivesse começando a aprender. E o mais importante, na minha
opinião, com cenários e problemas comuns do dia a dia do
desenvolvedor.

Este livro é para quem está começando a se aventurar no
maravilhoso mundo do desenvolvimento de software e quer
começar a trabalhar com um banco de dados. Este livro é para quem
já conhece SQL e quer se aperfeiçoar na utilização de um
gerenciador de banco de dados. Este livro também é para quem
conhece o PostgreSQL e quer construir um projeto utilizando-o.

Do começo ao fim, vamos desenvolver um projeto que pode ser
aplicado na prática. Em cada exemplo, busquei aplicar problemas

# PREFÁCIO

## ESCREVENDO O LIVRO QUE EU GOSTARIA
## DE LER


--------------------------------------------------

comuns do dia de um desenvolvedor.

O código-fonte de todos os códigos gerados durante o nosso
projeto neste livro estão disponíveis em meu repositório no GitHub.
Lá você vai encontrá-los separados por capítulos.

https://github.com/viniciuscdes/postgresql_codigos

Feedback é muito importante para todos os profissionais. Após
lançar meu primeiro livro, tive muitos feedbacks positivos e muitos
que trouxeram oportunidades de melhoria que pude aplicar neste
meu segundo livro.

Será um imenso prazer para mim saber o que você tem a dizer
sobre este meu trabalho. Você pode enviar sua dúvida ou feedback
para o e-mail a seguir:

viniciuscdes@gmail.com

Se preferir, pode acessar meu site pessoal também. Lá você
encontrará todas as minhas redes sociais e contatos.

http://www.viniciuscdes.net

## CÓDIGO-FONTE

## ENVIE SEU FEEDBACK


--------------------------------------------------


--------------------------------------------------

Quando lancei meu primeiro livro, uma das primeiras coisas
que eu fiz foi ir até a faculdade na qual me formei para doá-lo à
biblioteca da instituição através das mãos de uma professora, a qual
também foi minha orientadora. Este ato singelo foi um pequeno
gesto para demonstrar a minha gratidão por aqueles que se dedicam
a compartilhar seu conhecimento todos os dias com centenas de
pessoas durante todos os anos de sua vida. Os **professores**.

Desde o primeiro dia que entrei na faculdade, sempre tive em
minha mente que os melhores amigos que eu poderia fazer seriam
os professores. Isso porque sabia que eles estavam dispostos a
ensinar todos os dias e, de vez em quando, eu também conseguia
compartilhar o que eu sabia e também ensiná-los. Durante a minha
faculdade, sempre busquei essa troca de conhecimento que aquele
ambiente nos proporciona.

Com os professores, desde de pequeno, aprendi que
compartilhar conhecimento nunca é demais. E cada vez que você
compartilha algo, você aprende muito mais. Eu sempre fui inquieto
e me perguntei como estou compartilhando o que aprendi durante
todos esses anos, e como eu vou deixar para as outras pessoas esse
conhecimento. Foi então que surgiu a grande vontade de escrever
um livro.

Então, dedico este livro a todos os professores que eu tive
durante todos esses anos de vida. Acredito que uma das grandes
realizações de um professor é saber como estão os alunos que
passaram por suas turmas. Ser professor é algo, muitas vezes,
estressante. É uma dedicação diária em tentar fazer a diferença em
uma sala de aula.

# AGRADECIMENTO


--------------------------------------------------

Só gostaria de deixar registrado que vocês fizeram a diferença
em minha vida. Sempre que encontro um professor antigo, tento
passar essa mensagem. Creio que sirva de incentivo para que eles
continuem se dedicando e que o trabalho que eles desenvolvem não
é em vão.

Gostaria de agradecer aos meus primeiros professores. Minha
mãe, Juraci, meu pai, Nelson, e meus irmãos, Anderson, Judson e
Nelson Jr. Além de serem professores das minhas primeiras
palavras, são os de meu caráter.

E não poderia de deixar de agradecer minha esposa, Thais, pelo
incentivo em todos os meus projetos.


--------------------------------------------------

Vinícius Carvalho teve seu primeiro contato com o computador
em um curso de MS-DOS com Windows 95 e, desde então,
apaixonou-se pela computação. Ao longo da adolescência, procurou
aperfeiçoar-se e fazer alguns cursos até chegar a hora de escolher sua
formação na faculdade. Essa parte foi fácil! Formou-se em Sistemas
de Informações, pós-graduou-se em Engenharia de Software e não
parou de aprender coisas novas.

Apaixonado pela busca pelo conhecimento, procura manter-se
atualizado nas tendências de desenvolvimento de software,
tecnologia e tem como meta aprender algo novo todos os dias.

Na sua carreira profissional, teve oportunidades de trabalhar
como analista de suporte, desenvolvedor, gerente de projetos,
consultor e como um empreendedor incansável, arriscando-se a ter
seu próprio negócio. É apaixonado por tecnologia e informação.
Vive em constante aprendizagem.

Teve chance de palestrar em congresso de software livre, como o
VOL DAY, evento criado pela comunidade Viva o Linux; publicar
artigos em diversos congressos no Brasil; e ministrar aulas de
graduação no Centro Universitário Filadélfia (UniFil), faculdade
referência em cursos de graduação e pós-graduação no Paraná, na
qual se formou.

Lançou seu primeiro livro em 2015, sobre MySQL, que você
pode 
encontrar 
em:
https://www.casadocodigo.com.br/products/livro-banco-mysql.

Sua página pessoal é http://www.viniciuscdes.net. Lá você pode
conferir seu currículo e outras informações.

# SOBRE O AUTOR


--------------------------------------------------

**1**

1

3

10

11

20

**21**

21

22

30

**31**

33

34

36

39

41

45

48

52

**# Sumário**

**1 Introdução**

1.1 Banco de dados

1.2 PostgreSQL

1.3 O que dizem os desenvolvedores

1.4 Instalando e configurando

1.5 Para pensar!

**2 Comece a desenvolver com o PostgreSQL**

2.1 PL/pgSQL

2.2 DataTypes: do básico ao avançado

2.3 Para pensar!

**3 Nosso primeiro projeto**

3.1 Entendendo nossos dados

3.2 A estrutura das tabelas

3.3 Chaves primárias e chaves estrangeiras

3.4 Criando nossas tabelas

3.5 Constraints: integridade de seus dados

3.6 Criando sequências para as nossas tabelas

3.7 E os nossos registros? Já podemos inserir!

3.8 Consultando nossos registros

Sumário
Casa do Código


--------------------------------------------------

55

**56**

56

61

62

67

68

68

69

**70**

70

71

74

75

79

82

88

100

105

**107**

107

108

117

120

**121**

121

123

3.9 Para pensar!

**4 Functions — Agilizando o dia a dia**

4.1 Functions para poupar esforços

4.2 Utilizando a function

4.3 Functions sem return

4.4 Alterando functions

4.5 Excluindo functions

4.6 Vantagens da utilização das functions

4.7 Para pensar!

**5 Funções, operadores e operações**

5.1 Funções embutidas

5.2 Operadores lógicos

5.3 Operadores de comparação

5.4 Operadores e funções matemáticas

5.5 Funções de texto

5.6 Funções data/hora

5.7 Funções agregadoras

5.8 Consultas utilizando like

5.9 Para pensar!

**6 Banco de dados rápido nos gatilhos**

6.1 Triggers — Gatilhos para agilizar tarefas

6.2 Triggers: insert, update e delete

6.3 Desabilitando, habilitando e deletando uma trigger

6.4 Para pensar!

**7 Turbinando as consultas com joins e views**

7.1 Subconsultas

7.2 Consultas entre duas ou mais tabelas através das joins

Casa do Código
Sumário


--------------------------------------------------

129

133

**135**

135

136

138

143

150

**152**

152

153

157

162

**163**

163

163

**188**

189

**190**

193

193

203

7.3 Views

7.4 Para pensar!

**8 Administração do banco e outros tópicos**

8.1 Administrador de banco de dados vs. desenvolvedor

8.2 Comandos úteis

8.3 Backups

8.4 Índices e performance das consultas

8.5 Para pensar!

**9 Tipos de dados especiais**

9.1 Tipos de campos especiais

9.2 Campos array

9.3 Campos do JSON

9.4 Para pensar!

**10 Exercícios de concurso**

10.1 Concursos pelo Brasil

10.2 Exercícios

**11 Gabarito**

11.1 Para pensar!

**12 Apêndice A — Profissão DBA**

12.1 Comandos básicos e úteis

12.2 Trabalhando com pgAdmin

12.3 Para pensar e agradecer!

Sumário
Casa do Código


--------------------------------------------------

CAPÍTULO 1

"Toda empresa precisa de gente que erra, que não tem medo de
errar e que aprenda com o erro". — Bill Gates

Tecnologias de banco de dados dão suporte diário para
operações e tomadas de decisões nos mais diversos níveis da
empresa, da operação à gerência. Eles são vitais para as organizações
modernas que querem se manter competitivas no mercado e no
cenário atual de extrema concorrência.

O entendimento dos seus registros da empresa é crucial para a
formulação de consultas e perguntas para o negócio. Isso é possível
se a empresa tem o suporte de um bom banco de dados para essas
questões.

Umas das palavras que mais temos ouvido nos últimos 3 anos é
o tal do **big data**, que em poucas palavras é: extrair e, de alguma
maneira, relacionar a maior quantidade de dados sobre o seu
negócio. Entretanto, poucas empresas estão tirando proveito das
informações que elas possuem em seus bancos de dados, e
transformando isso em inteligência de negócio, devido a pouco
conhecimento da gerência ou por não possuírem ferramentas
necessárias.

**Big data** é um assunto tão extenso quando o PostgreSQL. Se

# INTRODUÇÃO

## 1.1 BANCO DE DADOS

1 INTRODUÇÃO 
**1**


--------------------------------------------------

você se interessar por análise de dados, vale a pena buscar se
informar sobre como implantar e gerenciar softwares para extrair
dados de bancos e implantar o big data em sua empresa ou para seus
clientes.

Quando digo dados, estou querendo dizer todas as informações
e registros gravados em um banco de dados da empresa, seja esse
banco conectado a um ERP, CRM etc. A análise e uma boa
administração desses dados são vitais para o negócio e tomadas de
decisões dentro de uma organização. Volto a frisar a importância de
ter uma boa ferramenta para administrar esse bem tão precioso da
empresa. E será essa ferramenta para fazer a administração de seus
dados que veremos neste livro, o PostgreSQL.

Se você enviou um e-mail hoje, escreveu um post no Facebook
ou no Twitter, ou enviou uma mensagem de celular, essas
informações que você publicou ficaram lá armazenadas. E esse
armazenamento é feito em um **banco de dados**.

Estamos conectados a diversos bancos de dados diariamente.
Eles estão no computador, no celular, no tablet, no videogame e em
até em alguns eletrodomésticos como algumas geladeiras modernas
que salvam listas de compras.

Os bancos de dados gerenciam de forma automatizada os dados
lá armazenados. Eles são conhecidos como Sistemas Gerenciadores
de Banco de Dados Relacional (SGBDR), ou apenas Sistemas
Gerenciadores de Banco de Dados (SGBD). O modelo de banco de
dados relacional é o mais usado, principalmente por sua capacidade
de manter a integridade dos dados quando existe alteração nas
estruturas das tabelas. Isso porque seus mecanismos que interligam
as tabelas relacionadas fazem com que seja muito seguro o trabalho
com um SGBD relacional. Veremos esses mecanismos no decorrer

**### Princípios de um SGBD relacional**

**2** 
1.1 BANCO DE DADOS


--------------------------------------------------

do livro.

O conceito básico de SGBD relacional é um conjunto de **tabelas**
relacionadas, e estas são compostas por alguns elementos básicos:
**colunas**, **linhas** e **campos**. Além desses elementos, o SGBD possui
outros que também serão apresentados aqui. Cada um deles será
demonstrado e analisado, não se preocupe em conhecê-los agora.

Os dados de uma empresa, se não forem o elemento mais
precioso, 
estão 
entre 
eles. 
Uma 
informação 
armazenada
incorretamente, ou de forma desordenada, pode custar todo o
negócio. Sabendo disso, não tenha medo de desenhar esquemas,
testar os esquemas das tabelas, trocar opiniões com outros
desenvolvedores na hora de modelar um banco de dados.

Realizar uma manutenção na estrutura de suas tabelas após o
sistema em produção é um custo muito caro para o projeto. Além
de ter um impacto na ocupação do tempo dos programadores, caso
você esteja modelando o banco, custará o seu tempo de retrabalho,
como também pode ter um impacto diretamente em seus usuários,
podendo gerar muita reclamação ou o encerramento do seu projeto.

Sempre que tenho a oportunidade de falar sobre projetos de
software, principalmente sobre a construção de banco de dados,
deixo muito claro que esta etapa dirá muito sobre a qualidade do
seu sistema no futuro. É claro, conforme seu sistema vai crescendo,
pode surgir a necessidade de fazer alterações em algumas estruturas.
Mas se a modelagem for feita pensando em um cenário escalável,
suas chances de sucesso vão aumentar consideravelmente.

**### Importância do banco de dados no projeto de**
**### construção de software**

## 1.2 POSTGRESQL

1.2 POSTGRESQL 
**3**


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------

Para fazer essa instalação, estou usando o Mac OS X 10.10
Yosemite. Você pode usar a versão disponível no site, ou utilizar
uma versão mais simples e fácil. Para MAC OS, existe um aplicativo
chamado PostgreApp, que é a maneira mais simples de usar o
PostgreSQL no MAC OS. Ele roda como um serviço. Você baixa e
executa-o. Muito simples.

Primeiro, vá até o site http://http://postgresapp.com/ e faça o
download. Quando ele estiver baixado, abra-o. Ao abrir, você verá
que, ao lado do relógio, aparecerá uma imagem de um elefante que
mostrará o serviço do PostgreSQL rodando, como mostra a figura
na sequência.

Figura 1.1: Serviço do PostgreSQL rodando

Quando você abre, também abrirá uma tela inicial do Postgre
App. Ela possui o botão **open psql** para você iniciar o console para
começar a criar e manipular seu banco de dados.

**12** 
1.4 INSTALANDO E CONFIGURANDO


--------------------------------------------------

Figura 1.2: Tela de inicio do Postgre App

Será no console da aplicação onde escreveremos nossos scripts e
comandos de criação e manipulação do nosso futuro banco de
dados. Mais à frente, mostrarei esses comandos.

Na página de download, você poderá encontrar versões
disponíveis para as distribuições do Linux, como: Red Hat, Debian,
Ubuntu, Suse e para versões genéricas. Para realizar a instalação,
vou utilizar o Ubuntu, versão 14.04.

No Ubuntu, temos as opções de baixar pacotes de instalação
compilados, ou via comandos. Eu particularmente prefiro fazer a
instalação via comandos, uma vez que é mais rápido e simples.

Primeiramente, atualizaremos os pacotes com:

$> sudo sh -c "echo  'deb http://apt.postgresql.org/pub/repos/apt/

  precise-pgdg main' > /etc/apt/sources.list.d/pgdg.list";

$> wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4
CF8.asc | sudo apt-key add -

Para manter sempre atualizado os pacotes de programas no
Linux, utilizamos o comando:

**### Instalando no Linux**

1.4 INSTALANDO E CONFIGURANDO 
**13**


--------------------------------------------------

$> sudo apt-get update

$> sudo apt-get install postgresql-common

Após a atualização, podemos baixar a nova versão desejada, com
o seguinte comando:

$> sudo apt-get install postgresql-9.6;

Como queremos baixar uma versão específica, é preciso escrever
como fizemos. Se tivéssemos escrito apenas:

$> sudo apt-get install postgresql;

Seria baixada a última versão liberada. Pronto, já podemos
utilizá-lo.

Para acessá-lo, abra o terminal e digite o comando:

$> sudo -i -u postgres psql

O  postgres  é o nosso usuário e banco de dados criado por
padrão do PostgreSQL.

Ao logar, altere a senha do nosso usuário com o comando:

$> alter user postgres with password 'senha';

Agora saia do terminal usando  \q , e acesse novamente usando
o comando:

$> psql -U postgres postgres -h localhost

Informe a senha, e pronto. Já podemos brincar com o nosso
banco!

Depois de ter feito o download no site do PostgreSQL para o
Windows, execute o arquivo. Ele abrirá a tela seguinte. Em seguida,
clique em Next.

**### Instalando no Windows**

**14** 
1.4 INSTALANDO E CONFIGURANDO


--------------------------------------------------

Figura 1.3: Instalação no Windows — Passo 1

Escolha a pasta onde será instalado e novamente Next.

1.4 INSTALANDO E CONFIGURANDO 
**15**


--------------------------------------------------

Figura 1.4: Instalação no Windows — Passo 2

Agora escolha a pasta na qual seus arquivos de dados ficarão.

**16** 
1.4 INSTALANDO E CONFIGURANDO


--------------------------------------------------

Figura 1.5: Instalação no Windows — Passo 3

Depois, digite uma senha de sua escolha para o usuário padrão

 postgres de seu banco de dados, e então em Next.

1.4 INSTALANDO E CONFIGURANDO 
**17**


--------------------------------------------------

Figura 1.6: Instalação no Windows — Passo 4

Na tela seguinte, terá um input box com a porta de acesso de
gerenciador de banco de dados. Por padrão, o PostgreSQL utiliza a
porta  5432 . Se você não possuir muito conhecimento, aconselho
deixar a padrão e clicar em Next.

**18** 
1.4 INSTALANDO E CONFIGURANDO


--------------------------------------------------

Figura 1.7: Instalação no Windows — Passo 5

As duas últimas telas serão Next e depois Finish para você
concluir a sua instalação e começar a utilizar o PostgreSQL.

Os comandos de criação de novos bancos e outras coisas serão
os mesmos para todos os sistemas. Por isto, mostrarei mais à frente.
No decorrer do livro, também darei exemplos de ferramentas para
manipulação de dados, entre outras ferramentas para utilizar em
mais de um sistema operacional.

Durante o desenvolvimento do projeto deste livro, usarei um
Linux 
como 
meu 
sistema 
operacional 
principal 
para
desenvolvimento. Se houver algum comando que fizer que é
diferente em outros sistemas, mostrarei ambos, não se preocupe.
Você pode programar com o sistema operacional que mais lhe
agradar.

1.4 INSTALANDO E CONFIGURANDO 
**19**


--------------------------------------------------

Se você vai desenvolver um sistema que várias pessoas vão
utilizar, você precisa instalar o PostgreSQL em um servidor. A
maioria dos desenvolvedores prefere servidores com Linux, e
realmente são melhores. Mas nada impede que você tenha um
servidor com Windows. Para o desenvolvimento, utilize o sistema
operacional que você mais gostar e com o qual se sente bem. E neste
caso, você tem essas três opções.

Seu projeto será offline ou online? Você conhece as ferramentas
de desenvolvimento do sistema operacional que você usa? Se seu
sistema rodar offline, você sabe como montar uma rede? Se ele for
rodar na web, você conhece as plataformas de hospedagem?

Pense um pouco nas perguntas anteriores como preparação para
iniciarmos o projeto que desenvolveremos durante o livro. Neste
capítulo, conhecemos um pouco sobre o SQL e o PostgreSQL. No
próximo, vamos conhecer um pouco mais sobre os padrões de
dados do PostgreSQL e começar a esboçar o nosso projeto. Darei
mais detalhes na sequência.

## 1.5 PARA PENSAR!

**20** 
1.5 PARA PENSAR!


--------------------------------------------------

CAPÍTULO 2

"As únicas grandes companhias que conseguirão ter êxito são
aquelas que consideram os seus produtos obsoletos antes que os
outros o façam". — Bill Gates

Se você trabalha ou já trabalhou com o Oracle, sabe o que é o
PL/SQL. É a linguagem procedural do banco de dados Oracle que
permite a inclusão de lógica no SGBD. Já o PL/pgSQL (Procedural
Language/PostgreSQL) é a linguagem de programação procedural do
PostgreSQL. Com ela, é possível inserir lógica em seu banco de
dados.

Neste momento, você deve estar se perguntando por que
precisaríamos de lógica ou de uma linguagem para trabalhar com
banco de dados, já que os comandos SQL conseguem apenas
manipular os dados seu em SGBD. E utilizamos alguns objetos
quando precisamos criar processos automatizados ou que tenham a
necessidade de serem aplicados rotineiramente. Mas eu explicarei e
mostrarei esses processos nos capítulos Functions — Agilizando o
dia a dia, Funções, operadores e operações, Banco de dados rápido
nos gatilhos e Turbinando as consultas com joins e views. Aproveite
esses três primeiros capítulos para absorver bem a introdução de

# COMECE A DESENVOLVER
# COM O POSTGRESQL

## 2.1 PL/PGSQL

2 COMECE A DESENVOLVER COM O POSTGRESQL 
**21**


--------------------------------------------------

vários conceitos e base de seus estudos sobre banco de dados.

PL/pgSQL é uma linguagem procedural que você grava no
sistema de banco de dados PostgreSQL. Os objetivos do PL/pgSQL
foram criar uma linguagem procedural carregável que pode ser
usada para criar funções e procedimentos de gatilhos, acrescentar
estruturas de controle à linguagem SQL, poder realizar cálculos
complexos, e herdar todos os tipos, funções e operadores definidos
pelo usuário. Ela pode ser definida para ser confiável para o servidor
e ser fácil de usar.

Funções criadas com PL/pgSQL podem ser usadas em qualquer
lugar em que funções internas são utilizadas. Por exemplo, é
possível criar funções de cálculo condicional complexos e depois
usá-las em chamadas de triggers, como veremos no capítulo
Funções, operadores e operações, ou em eventos agendados, como
será mostrado no capítulo Turbinando as consultas com joins e
views.

Nos próximos capítulos, entraremos em assuntos em que vamos
usar PL/pgSQL. Conforme formos fazendo os exemplos, vou
explicando a melhor maneira de utilizar em seus projetos e tudo vai
ficar mais claro.

Neste capítulo, conheceremos algumas características dos tipos
de dados que o PostgreSQL suporta e iniciaremos a descrição do
nosso projeto que vamos desenvolver no decorrer deste livro.

Cada informação deve ser armazenada com o seu tipo correto.
Isto é, um campo em que serão inseridos apenas números deverá ser
do tipo numérico. É extremamente importante e crítico fazer a
escolha do tipo de cada informação que você vai armazenar.

## 2.2 DATATYPES: DO BÁSICO AO AVANÇADO

**22** 
2.2 DATATYPES: DO BÁSICO AO AVANÇADO


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------

XML, ame ou odeie. Há uma grande quantidade de dados em
formatos XML, e esse fato não está mudando rapidamente devido a
um grande investimento em XML. Ocasionalmente, inserir dados
XML em um banco de dados relacional pode render uma vitória
quando a integração com fontes de dados externas fornece dados
em XML.

PostgreSQL tem a capacidade de manipular dados XML com
SQL, permitindo um caminho para integrar dados XML em
consultas SQL. A declaração deste tipo de campo é como a dos
outros tipos. Mais adiante, quando formos desenvolver exemplos
deste tipo de campo, veremos na prática a sua utilização e como
podemos nos beneficiar.

PostgreSQL tem suporte a JSON já algum tempo. Na versão 9.2,
foi adicionado suporte nativo a este tipo de dados, e os usuários
deste poderoso gerenciador de banco de dados começaram a utilizar
o PostgreSQL como um banco "NoSQL". Este que é um banco não
relacional. Mas este assunto fica de tarefa de casa para vocês.

Na versão 9.4, foi adicionado a funcionalidade para armazenar
JSON como JSON Binário (JSONB), que remove os espaços em
branco insignificantes (não que seja um grande negócio), acrescenta
um pouco de sobrecarga quando inserir dados, mas fornece um
benefício enorme ao consultar.

Se você estava pensando em trocar o seu banco de dados
relacional por um NoSQL, pode começar a rever seus conceitos. Isso
porque, se você tem a possibilidade usar os benefícios de um banco
NoSQL no PostgreSQL, então por que mudar?

Veremos na prática, em nosso projeto, como extrair do
PostgreSQL os benefícios de um banco NoSQL utilizando campos

**### Tipo JSON**

**28** 
2.2 DATATYPES: DO BÁSICO AO AVANÇADO


--------------------------------------------------


--------------------------------------------------

comando  create type , no qual podemos criar um novo tipo de
campo. Ele pode ser composto por vários campos, ou pode ser uma
lista de valores.

Conhecemos diversos tipos de campos e cada um para
armazenar um tipo de informação. Citei várias vezes a importância
da utilização do tipo de campo certo para cada informação que será
armazenada. Se você estiver realizando algum projeto de banco de
dados, tente observar se algum campo que você criou poderia ser
alterado e melhorado. Ou baseado no projeto proposto, pense em
quais campos vamos criar para cada tabela e seus respectivos tipos.
Tente também imaginar quais seriam as implicações na escolha de
um tipo errado para um campo.

Agora que já conhecemos os tipos de campos que podemos criar
e os tipos de dados que podemos armazenar, podemos iniciar o
desenvolvimento de nosso projeto. Vamos começar pelo projeto e a
descrição dele, e depois partiremos para a criação dos códigos.

## 2.3 PARA PENSAR!

**30** 
2.3 PARA PENSAR!


--------------------------------------------------

CAPÍTULO 3

"Não se preocupe se não funcionar direito. Se tudo funcionasse,
você estaria desempregado". — Lei de Mosher da Engenharia de
Software

Não canso de falar como é produtivo e muito mais fácil
aprender a programar quando temos de fazer um projeto real ou
baseado na realidade de algum tipo de negócio. Durante o livro, não
será diferente. Vamos criar um projeto que vai nos acompanhar
durante toda a leitura, e nos basear em sua regra de negócio para
trabalhar com o PostgreSQL.

Vamos imaginar que fomos contratados para desenvolver um
sistema para um restaurante. Então, precisamos pensar no esquema
de tabelas para atender esta demanda. Vamos criar algo que será
simples, no entanto, conseguiremos testar todos os aspectos do
banco de dados, inclusive todos os tipos de dados. Devemos
imaginar tudo que será preciso para o funcionamento básico para
vendas e pedidos de um restaurante, como: mesas, produtos,
vendas, funcionários e as comissões dos funcionários.

Para visualizarmos melhor como ficará o schema do banco de
dados, vamos criar um D.E.R. (Diagrama de entidade e
relacionamento). Com isso, teremos uma forma visual para
conhecer as tabelas e seus relacionamentos para criar os scritps.

# NOSSO PRIMEIRO
# PROJETO

3 NOSSO PRIMEIRO PROJETO 
**31**


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------

especificação dos requisitos a serem desenvolvidos. É o princípio da
engenharia de software.

A modelagem de dados sempre deve estar contida em sua
especificação de requisitos, e sempre dê uma atenção especial para
ela. Além da experiência do usuário entender os dados do seu
sistema, é muito importante entender como os dados se relacionam,
o que será armazenado em cada tabela e em cada campo, entender
como armazenar cada informação e como elas serão apresentadas
para o usuário. Tudo isso é vital para seu projeto.

Estes cuidados estão diretamente ligados ao desempenho e
longevidade de sua aplicação. Isso porque, se o banco estiver mal
projetado, você não conseguirá escalar sua aplicação, e isso terá um
custo alto no futuro.

Costumo desenhar e criar rascunhos das tabelas do projeto antes
de iniciar a desenvolver. Além de escrever, na mão mesmo, crio
testes de mesas para entender o fluxo dos dados e ver se o resultado
é o esperado. E quando crio as tabelas no banco, faço uma inserção
de dados manualmente para ver se realmente o meu projeto está
consistente.

Se estiver com dúvida, mostre para os desenvolvedores. Não
tenha medo de mostrar seu código. Se tiver algo errado, será bom,
pois você vai aprender e corrigirá seu erro. Sempre que tiver a
oportunidade, compartilhe conhecimento e mostre seus códigos
para alguém. Você só terá a ganhar.

Após a concepção, modelagem e revisão do seu projeto de banco
de dados, chegou a hora de escrever os códigos para criar os objetos
no seu SGBD. Volto a frisar o quão importante é esta etapa no

## 3.2 A ESTRUTURA DAS TABELAS

**34** 
3.2 A ESTRUTURA DAS TABELAS


--------------------------------------------------

processo de desenvolvimento de um aplicativo. Mas o que são
tabelas? E como são suas estruturas?

Segundo escritor e especialista em banco de dados, Bob Bryla,
uma tabela é uma unidade de armazenamento em um banco de
dados. Sem tabelas, um banco de dados não tem valor para uma
empresa. Independentemente do tipo de tabela, os seus dados são
armazenados em linhas e colunas, similar ao modo como os dados
são armazenados em uma planilha. Mas as semelhanças terminam
aí. A robustez de uma tabela de banco de dados torna uma planilha
uma segunda opção ineficiente ao decidir sobre um local para
armazenar informações importantes.

Imagine um banco de dados como um grande armário com
várias gavetas, e cada gaveta como uma tabela. Cada gaveta
armazenará um tipo de objeto, e no caso do banco, cada tabela
armazenará um tipo de informação. Se tem uma gaveta apenas para
as camisetas, terá uma tabela para armazenar as informações sobre
as camisetas no estoque de uma empresa. E diferentemente de uma
gaveta, uma tabela vai conter  n  colunas que conterá diversas
informações sobre essas camisetas.

Para identificarmos e conseguirmos buscar registro de uma
tabela no SGBD, temos de determinar uma identificação única para
cada registro, assim como identificar o relacionamento entre as
tabelas. Esses dois elementos é o que chamamos de chave primária e
chave estrangeira, pois, em vez de duplicarmos uma informação em
uma tabela, nós criamos tabelas com valores que não vão mudar e
fazemos a referência em outras tabelas.

Vamos imaginar a nossa tabela para guardar as informações
sobre as camisetas. Imagine quais informações podemos armazenar.
Eu escolhi colocar em nossa tabela uma coluna que será a
identificação única de nossa tabela, uma coluna para descrever a cor
de nossa camiseta, uma coluna para informarmos o tamanho e uma

3.2 A ESTRUTURA DAS TABELAS 
**35**


--------------------------------------------------

para informar o tipo do tecido.

Em vez de repetirmos o tipo do tecido várias vezes, o melhor é
criarmos uma tabela de tecidos, na qual terá todos os tipos e, em
nossa tabela de camisetas, apenas fazer uma referência a esta. Veja a
figura a seguir.

Figura 3.2: Identificação única da tabela e referência a outra tabela

Com isso, já começamos a ter uma base sobre o que é chave
primária, ou primary key (PK), e chave estrangeira, ou foreign key
(FK). Na sequência estará detalhado cada um com novos exemplos.

Como já citado, o PostgreSQL é um banco de dados relacional.
O princípio dos bancos de dados relacionais é o relacionamento
entre uma ou mais tabelas, que é feito por meio de uma chave única,
chamada de primary-key (ou chave primária).

Vamos exemplificar este cenário. Vamos imaginar que uma
tabela é a representação da rua na qual você mora, e sua casa e as
demais são os registros da tabela. Geralmente, temos apenas uma
sequência numérica, única, de casas em uma rua — ao menos,
deveríamos ter. Imagine o número da casa como sendo uma "chave"
única, algo que vai identificá-la das demais.

## 3.3 
## CHAVES 
## PRIMÁRIAS 
## E 
## CHAVES
## ESTRANGEIRAS

**### Chave primária**

**36** 
3.3 CHAVES PRIMÁRIAS E CHAVES ESTRANGEIRAS


--------------------------------------------------

Nas tabelas do nosso banco, é exatamente isso que acontece.
Temos de ter uma chave única para identificar os registros que se
encontram em uma determinada tabela. Dentro deste cenário,
conseguiremos manter a integridade dos dados.

Você deve ter uma chave primária, pois será um registro que
não sofrerá alteração e nem se repetirá. Sempre será único e
imutável. Só assim você terá a consistência de seus dados. Para
alterar um registro na tabela, você deve buscá-lo por sua PK, assim
não ocorrerá de alterar um registro incorreto.

Figura 3.3: A identificação única das casas em uma rua

Em uma tabela de banco de dados, teríamos:

3.3 CHAVES PRIMÁRIAS E CHAVES ESTRANGEIRAS 
**37**


--------------------------------------------------

Figura 3.4: A identificação única dos registros em uma tabela

**D****ICA****!**

Procure usar mecanismos de autoincremento em suas chaves
primárias. Assim, você não precisará se preocupar em inserir
e/ou criar uma forma de incrementar e não repetir a sequência.
Ainda neste capítulo, vou demonstrar como criar uma

 sequence que lhe auxiliará neste quesito.

As chaves estrangeiras, ou foreign-keys, são identificadores
únicos que fazem referência à chave primária de outra tabela. Se
tivermos uma FK em nossa tabela, não conseguimos inserir um
registro que não esteja contido na tabela referenciada.

O exemplo a seguir mostra duas tabelas: uma de funcionários e
uma de cargos. O  ID  da tabela  CARGOS , que é uma chave

**### Chave estrangeira**

**38** 
3.3 CHAVES PRIMÁRIAS E CHAVES ESTRANGEIRAS


--------------------------------------------------

primária, passa a ser uma chave estrangeira na tabela

 FUNCIONARIOS , chamada  CARGO_ID . Ela, por sua vez, não vai
permitir a inserção de nenhum cargo que não esteja cadastrado na
tabela  CARGOS , dando para sua tabela consistência e evitando erros.

Figura 3.5: PK sendo referenciada como uma FK

Sabendo a importância e o objetivo da utilização de PKs e FKs
nas tabelas, já podemos finalmente criar nossos códigos. Então,
agora mãos no teclado e vamos começar.

Abra o terminal de comandos instalado na instalação do
PostgresSQL para criarmos os objetos em nosso banco.

O  create table  é o comando usado para criar tabelas.
Sabendo disso, vamos à criação delas.

# tabela para gravar registro das mesas

create table mesas (

    id               int not null primary key,
    mesa_codigo      varchar(20),
    mesa_situacao    varchar(1) default 'A',
    data_criacao     timestamp,
    data_atualizacao timestamp);

# tabela para gravar registro dos funcionários
create table funcionarios(

    id                    int not null primary key,
    funcionario_codigo    varchar(20),
    funcionario_nome      varchar(100),

## 3.4 CRIANDO NOSSAS TABELAS

3.4 CRIANDO NOSSAS TABELAS 
**39**


--------------------------------------------------

    funcionario_situacao  varchar(1) default 'A',
    funcionario_comissao  real,
    funcionario_cargo     varchar(30),
    data_criacao          timestamp,
    data_atualizacao      timestamp);   

# tabela para gravar registro das vendas
create table vendas(

    id               int not null primary key,
    funcionario_id   int references funcionarios (id),
    mesa_id          int references mesas(id),
    venda_codigo     varchar(20),
    venda_valor      real,
    venda_total      real,
    venda_desconto    real,
    venda_situacao   varchar(1) default 'A',
    data_criacao     timestamp,
    data_atualizacao timestamp);

# tabela para gravar registro dos produtos
create table produtos(

    id               int not null primary key,
    produto_codigo   varchar(20),
    produto_nome     varchar(60),
    produto_valor    real,
    produto_situacao varchar(1) default 'A',
    data_criacao     timestamp,
    data_atualizacao timestamp);    

# tabela para gravar registro dos itens das vendas
create table itens_vendas(

    id                int not null primary key,
    produto_id        int not null references produtos(id),
    vendas_id int not null references vendas(id),
    item_valor        real,
    item_quantidade   int,
    item_total       real,
    data_criacao      timestamp,
    data_atualizacao  timestamp);     

# tabela para gravar registro do cálculo das comissões
create table comissoes(

    id                int not null primary key,
    funcionario_id    int references funcionarios(id),
    comissao_valor    real,
    comissao_situacao varchar(1) default 'A',
    data_criacao      timestamp,
    data_atualizacao  timestamp);

**40** 
3.4 CRIANDO NOSSAS TABELAS


--------------------------------------------------

Após criadas todas as nossas tabelas, para você ver se realmente
estão criadas no banco de dados, utilize o comando  \dt , como a
figura a seguir. Uma lista com as tabelas será mostrada para você:

Figura 3.6: \d para listar as tabelas criadas no banco

Os tipos de dados são uma forma para limitar o tipo de dados
que pode ser armazenado em uma tabela. Para muitas aplicações,
contudo, a restrição que eles fornecem é demasiadamente grosseira.

Por exemplo, uma coluna contendo preços de produtos
provavelmente só pode aceitar valores positivos. Mas não há
nenhum tipo de dados padrão que aceite apenas números positivos.
Outra questão é que você pode querer restringir os dados de uma
coluna com relação a outras colunas ou linhas, como: em uma
tabela contendo informações sobre o produto deve haver apenas
uma linha para cada número de produto.

Assim, o SQL permite definir restrições em colunas e tabelas.
Restrições darão tanto controle sobre os campos como em suas
tabelas, como você desejar. Se um usuário tentar armazenar dados
em uma coluna que possa violar uma restrição, será gerado um erro.

## 3.5 CONSTRAINTS: INTEGRIDADE DE SEUS
## DADOS

3.5 CONSTRAINTS: INTEGRIDADE DE SEUS DADOS 
**41**


--------------------------------------------------

Na sequência, estarei demonstrando os tipos de  constraints  e
demonstrando os tipos de erros que podemos enfrentar.

As contraints podem ser para a validação de valores como de
chave primária e estrangeira. Observe que, na criação de nossas
tabelas, nós especificamos quais os campos que seriam as PKs e as
FKs de cada uma.

Para visualizarmos as constraints de uma tabela, use o comando

 \d nome_tabela  como mostra a figura a seguir. Observe que,
além de listar as constraints, este comando serve para listar os
campos de uma tabela. Vamos utilizá-lo para visualizar as colunas
da tabela  vendas .

postgres=# \d vendas;

E como resultado, teremos:

Figura 3.7: \d \d vendas - listas dos campos da tabela e suas constraints

Em vez de criarmos as constraints de PK e FK na criação da
tabela, podemos criá-las separadamente. Vamos excluir uma tabela
e criá-la novamente, só que agora criaremos as constraints de PK e
FK posteriormente à sua criação.

Criar separado ou junto é uma questão de padrão de

**### Constraint de PK e FK**

**42** 
3.5 CONSTRAINTS: INTEGRIDADE DE SEUS DADOS


--------------------------------------------------

desenvolvimento. Como sempre falo, cada um tem o seu, o que for
mais prático no dia a dia de cada desenvolvedor. Eu gosto de criar
separado para ter um maior controle dos códigos de um projeto.
Assim, consigo separar os códigos de uma determinada função em
arquivos separados.

Para excluir uma tabela, use o comando:

postgres=> drop table comissoes;

Agora crie novamente a tabela, sem as constraints.

create table comissoes(

    id                int not null,
     funcionario_id   int ,
    comissao_valor    real,
    comissao_situacao varchar(1) default 'A',
    data_criacao      timestamp,
    data_atualizacao  timestamp);

A tabela será criada sem uma chave primária e sem chave
estrangeira. Vamos criar as constraints. Primeiro a PK:

postgres=> alter table comissoes 

          add constraint comissoes_pkey primary key(id);

Agora a FK que referencia a tabela  FUNCIONARIOS :

postgres=> alter table comissoes 

          add foreign key (funcionario_id) references funcionario
s(id);

Para verificarmos que tudo ocorreu bem, vamos listar os campos
e as constraints com o comando  \d comissoes , como mostra a
figura a seguir.

3.5 CONSTRAINTS: INTEGRIDADE DE SEUS DADOS 
**43**


--------------------------------------------------

Figura 3.8: \d vendas - listas dos campos da tabela e suas constraints

Se em algum momento você precisar deletar uma constraint,
algo que não aconselho, utilize o comando:

postgres=> alter table comissoes 

          drop constraint comissoes_funcionario_id_fkey;

**C****UIDADO****!**

Para você deletar uma  constraint , você deve ter certeza de
qual é a sua finalidade e se ela não está mais sendo usada. Isso
porque, na maioria das vezes, este recurso é utilizado para fazer
validações e criar maneiras de se manter a integridades dos
dados.

As constraints para validação de dados também são usadas para
dar mais segurança para seus dados através de validações. Imagine a
situação em que o valor de suas vendas está ficando negativo, algo
que não pode acontecer. Como você controlará esta situação?
Podemos criar uma constraint para validar se o valor total da venda
é positivo. Assim, não será necessário criar uma validação na
aplicação e nem se preocupar com futuros imprevistos.

Vamos criar uma constraint que dirá para o nosso banco testar

**### Constraints de validações**

**44** 
3.5 CONSTRAINTS: INTEGRIDADE DE SEUS DADOS


--------------------------------------------------

se o campo  venda_total é maior que zero (positivo) a cada novo
registro que estiver sendo inserido.

postgres=> alter table vendas add check (venda_total > 0 );

Quando criamos nossas tabelas em alguns campos, usamos  not

null , isto é, o campo não pode ser nulo. Mas também podemos
criar uma constraint que chegará se o campo está recebendo um
valor nulo na inserção de um novo registro.

Sabendo disso, vamos criar uma constraint na tabela

 FUNCIONARIOS para não permitir que seja inserido nulo no campo

 funcionario_nome . Assim, o nosso banco vai verificar se
tentamos inserir um valor nulo, assim como o  not null faria.

postgres=> alter table funcionarios 

            add check( funcionario_nome <> null);

Em todas nossas tabelas, temos uma chave primária. Em nosso
padrão, adotei um campo chamado  id  como padrão para as
nossas chaves primárias. Como este campo deve conter uma
sequência numérica única, nada mais lógico do que termos um
mecanismo para gerar este  id  único e automaticamente. Por isso
temos as chamadas  sequences , que são sequências numéricas
autoincrementadas.

Criando uma  sequence  para cada tabela, o campo  id  vai se
autoincrementar a cada inserção em cada tabela. Como comentei
anteriormente, as chaves primárias, como boas práticas de
programação, não é aconselhável utilizá-las para mostrar na tela.

Para cada tabela do projeto, vamos criar uma  sequence ,
utilizando o comando  CREATE SEQUENCE . Para o nome de nossas

## 3.6 CRIANDO SEQUÊNCIAS PARA AS NOSSAS
## TABELAS

3.6 CRIANDO SEQUÊNCIAS PARA AS NOSSAS TABELAS 
**45**


--------------------------------------------------

 sequences , usaremos o padrão  _NOMETABELA_NOMECOLUNA_SEQ_ .
Este padrão é como eu gosto de utilizar. Você pode (e eu aconselho)
criar o seu também. Com este padrão, o nome da  sequence para a
tabela  mesas  ficaria:  mesas_id_seq . Então, vamos criar todas as
sequências com os seguintes códigos:

postgres=> create sequence mesa_id_seq;
postgres=> create sequence vendas_id_seq;
postgres=> create sequence itens_vendas_id_seq;
postgres=> create sequence produtos_id_seq;
postgres=> create sequence funcionario_id_seq;
postgres=> create sequence comissoes_id_seq;

Depois das sequências criadas, devemos vincular cada

 sequence com suas respectivas tabelas, da seguinte maneira:

postgres=> alter table mesas 

          alter column id set default nextval('mesa_id_seq');
postgres=> alter table vendas 

          alter column id set default nextval('vendas_id_seq');
postgres=> alter table itens_vendas 

          alter column id set default nextval('itens_vendas_id_se
q');
postgres=> alter table produtos 

          alter column id set default nextval('produtos_id_seq');
postgres=> alter table funcionarios 

          alter column id set default nextval('funcionario_id_seq
');
postgres=> alter table comissoes 

          alter column id set default nextval('comissoes_id_seq')
;

Com todas as  sequences  criadas, não precisamos nos
preocupar como vamos preencher cada campo. A vantagem da
utilização das  sequences  é que, caso não quisermos mais usá-las,
apenas deletamos a  sequence e utilizamos outro meio para inserir
a sequência da chave primária. No entanto, não aconselho fazer isso,
pois, usando este método de incremento numérico, tenho mais
segurança e controle da função que está gerando e gravando os
números para mim.

**46** 
3.6 CRIANDO SEQUÊNCIAS PARA AS NOSSAS TABELAS


--------------------------------------------------

Para deletar uma  sequence , usamos o comando  drop

sequence da seguinte maneira:

postgres=> drop sequence funcionario_id_seq cascade;

O resultado deverá ser o mostrado na figura a seguir.

Figura 3.9: Drop sequence ... cascade

Devemos utilizar o comando  cascade  no final do nosso
comando para o banco também deletar o vínculo feito com a tabela

 FUNCIONARIOS . Se fosse apenas uma  sequence  que não é
utilizada em alguma tabela, não o usaríamos.

Vamos criar uma  sequence  que não usaremos, e depois
faremos um drop. Criando a  sequence :

postgres=> create sequence proximo_numero;

Por ela não estar vinculada com alguma tabela, o comando será:

postgres=> drop sequence proximo_numero;

Nada mais comum do que a necessidade de fazermos alterações
em nossas tabelas posteriormente à criação delas. Como alterações
em uma tabela, podemos considerar: inserção de novos campos,
exclusão de campos e alteração no tipo de um campo.

Vamos imaginar que surgiu a necessidade de inserirmos mais
um campo na tabela  COMISSOES , o campo de  DATA_PAGAMENTO ,
para informar a data que a comissão foi ou será paga. Imagine que já
começamos a inserir registros nessa tabela. Com isso, deletá-la está
fora de cogitação. Mesmo que não tenhamos registros inseridos,

**### Alterando tabelas**

3.6 CRIANDO SEQUÊNCIAS PARA AS NOSSAS TABELAS 
**47**


--------------------------------------------------

deletar e criar a tabela novamente não é muito viável. Então,
realizamos um comando para inserir um novo registro na tabela.

Vamos inserir o novo campo na tabela com o comando  alter

table...add colun... .

postgres=> alter table comissoes 

            add column data_pagamento int;

Ops! Observe que criamos um campo que será usado para
armazenar data com o tipo  int , que é usado para armazenar
números inteiros. Nesta situação, como não há ainda registros nesta
nova coluna, temos duas escolhas: ou excluímos o campo e criamos
novamente, ou modificamos o seu tipo.

Para excluir uma coluna, utilizamos o comando  alter

table...drop column .

postgres=> alter table comissoes 

                 drop column data_pagamento;
postgres=> alter table comissoes 

                  add column data_pagamento timestamp;

Se escolhermos apenas modificar o tipo da coluna, usamos o
comando  alter table...alter column...type... .

postgres=> alter table comissoes 

          alter column data_pagamento type timestamp 
          using data_pagamento_timestamp;

Com todas as nossas tabelas criadas, agora podemos começar a
inserir registros em todas elas. Vamos inserir os registros que vamos
utilizar em todo o livro. Fique à vontade para inserir os registros que
desejar.

Na tabela de funcionário, escolha nome de pessoas que você

## 3.7 E OS NOSSOS REGISTROS? JÁ PODEMOS
## INSERIR!

**48** 
3.7 E OS NOSSOS REGISTROS? JÁ PODEMOS INSERIR!


--------------------------------------------------

conhece. Na tabela de produtos, utilize objetos com que você tenha
familiaridade.

Para inserir registros, vamos utilizar o comando  INSERT

INTO... VALUES... . Usamos constantemente este recurso de
inserção manual principalmente quando desejamos testar uma
aplicação. Muitas vezes você ainda não terá a aplicação para testar se
a modelagem dos dados está correta. Esta inserção funciona como
um teste de mesa para a nossa modelagem. Sempre que criar um
banco de dados, procure fazer a inserção manual de registros.

Vou inserir alguns registros em cada tabela que criamos.

postgres=> insert into mesas (mesa_codigo,

                             mesa_situacao,
                             data_criacao,
                             data_atualizacao)
                     values ('00001',
                             'A',
                             '01/01/2016',
                             '01/01/2016');

postgres=> insert into mesas (mesa_codigo,

                             mesa_situacao,
                             data_criacao,
                             data_atualizacao)
                    values ('00002',
                            'A',
                            '01/01/2016',
                            '01/01/2016');

Observe que, no comando, nós suprimos o campo  id da tabela

 MESAS . Isso porque nós criamos uma  sequence  para inserir esse
valor de todas as tabelas. Vamos continuar com a inserção dos
registros.

postgres=>  insert into funcionarios(funcionario_codigo,

                                    funcionario_nome,
                                    funcionario_situacao,

**### Inserindo registros**

3.7 E OS NOSSOS REGISTROS? JÁ PODEMOS INSERIR! 
**49**


--------------------------------------------------

                                     funcionario_comissao,
                                     funcionario_cargo,
                                     data_criacao)
                             values('0001',
                                    'VINICIUS CARVALHO',
                                    'A',
                                     5,
                                    'GERENTE',
                                    '01/01/2016');

postgres=> insert into funcionarios(funcionario_codigo,
                                    funcionario_nome,
                                    funcionario_situacao,
                                    funcionario_comissao,
                                    funcionario_cargo,
                                    data_criacao)
                             values('0002',
                                    'SOUZA',
                                    'A',
                                     2,
                                    'GARÇOM',
                                    '01/01/2016');

postgres=> insert into produtos (produto_codigo,
                                 produto_nome,
                                 produto_valor,
                                 produto_situacao,
                                 data_criacao,
                                 data_atualizacao)
                         values ('001',
                                 'REFRIGERANTE',
                                 10,
                                 'A',
                                 '01/01/2016',
                                 '01/01/2016');

postgres=> insert into produtos (produto_codigo,
                                 produto_nome,
                                 produto_valor,
                                 produto_situacao,
                                 data_criacao,
                                 data_atualizacao)
                          values ('002',
                                  'AGUA',
                                  3,
                                  'A',
                                  '01/01/2016',
                                  '01/01/2016');

**50** 
3.7 E OS NOSSOS REGISTROS? JÁ PODEMOS INSERIR!


--------------------------------------------------

postgres=> insert into produtos (produto_codigo,
                                 produto_nome,
                                 produto_valor,
                                 produto_situacao,
                                 data_criacao,
                                 data_atualizacao)
                         values ('003',
                                 'PASTEL',
                                 7,
                                 'A',
                                 '01/01/2016',
                                 '01/01/2016');

postgres=> insert into vendas (funcionario_id,
                               mesa_id,
                               venda_codigo,
                               venda_valor,
                               venda_total,
                               venda_desconto,
                               venda_situacao,
                               data_criacao,
                               data_atualizacao)
                        values (2,
                                1,
                                '0001',
                                '20',
                                '20',
                                '0',
                                'A',
                                '01/01/2016',
                                '01/01/2016');

postgres=> insert into vendas (funcionario_id,
                               mesa_id,
                               venda_codigo,
                               venda_valor,
                               venda_total,
                               venda_desconto,
                               venda_situacao,
                               data_criacao,
                               data_atualizacao)
                        values (2,
                                2,
                                '0002',
                                '21',
                                '21',
                                '0',

3.7 E OS NOSSOS REGISTROS? JÁ PODEMOS INSERIR! 
**51**


--------------------------------------------------

                               'A',
                               '01/01/2016',
                               '01/01/2016');                    

postgres=> insert into itens_vendas (produto_id,

                                    vendas_id,
                                    item_valor,
                                    item_quantidade,
                                    item_total,
                                    data_criacao,
                                    data_atualizacao)
                            values (1,
                                    1,
                                    10,
                                    2,
                                    20,
                                    '01/01/2016',
                                    '01/01/2016');    

postgres=> insert into itens_vendas(produto_id,

                                   vendas_id,
                                   item_valor,
                                   item_quantidade,
                                   item_total,
                                   data_criacao,
                                   data_atualizacao)
                               values(1,
                                      2,
                                      7,
                                      3,
                                      21,
                                      '01/01/2016',
                                      '01/01/2016');

Não vamos inserir registro na tabela  COMISSOES , pois nesta
criaremos um processo que vai populá-la automaticamente. Por se
tratar de uma tabela que vai gerar as comissões dos funcionários, o
melhor é criar um processo que faça isso sozinho. No capítulo
seguinte, vamos trabalhar com esse processo.

Com registros em nosso banco, o mais lógico é criarmos

## 3.8 CONSULTANDO NOSSOS REGISTROS

**52** 
3.8 CONSULTANDO NOSSOS REGISTROS


--------------------------------------------------

consultas para visualizá-los. O comando para criarmos consultas é o

 SELECT... FROM... .

Vamos consultar os registros da tabela  MESAS . Para isso,
usaremos o  SELECT e o  FROM . Este é o responsável por dizer para
o banco de dados qual é tabela que desejamos consultar. Nosso
comando e o resultado ficarão da seguinte maneira:

postgres=> select * from mesas;

Figura 3.10: Selecionando todas as mesas

Observe que não foi necessário informar nenhum campo em
nosso comando para fazer a consulta. Apenas usamos o  * 
(asterisco), assim o banco entendeu que era para buscar todos os
campos da tabela informada logo após o  FROM . Mas se desejarmos
selecionar apenas algumas colunas, o nosso comando ficaria da
seguinte maneira:

postgres=> select mesa_codigo, data_criacao from mesas;

Nessas duas consultas, o resultado foi todos os registros, porém
podemos ter a necessidade de buscar apenas um ou alguns registros.
Para fazermos isso, devemos informar qual registro que queremos
buscar. Com o comando  where , vamos informar qual o registro
que desejamos buscar. Vamos então consultar a mesa que possui o

 mesa_codigo igual a dois.

postgres=> select * from mesas where mesa_codigo = '00002';

Observe que o código  00002  foi colocado entre aspas simples.
Isto porque, para fazer comparação de strings, devemos deixar entre
aspas simples, tanto nas consultas como nas inserções e alteração de

3.8 CONSULTANDO NOSSOS REGISTROS 
**53**


--------------------------------------------------

dados. Observe na inserção dos registros que campos de caracteres e
datas estão com aspas simples, e os numéricos não estão.

Fizemos a inserção manual dos registros para conseguirmos
trabalhar durante o desenvolvimento do projeto que estamos
criando no livro. Se desejarmos apenas modificar um registro em
uma tabela em vez de inserir um novo e excluir algum outro,
usamos o comando  UPDATE .

Vamos alterar o produto de  id = 2 , que é o produto  AGUA ,
colocando um novo valor para ele. Agora ele passará a custar 4.

postgres=> update produtos set produto_valor = 4

                      where id = 2;

Observe que utilizamos também o comando  WHERE  para
indicar qual produtos que queríamos fazer a alteração. Se não
usássemos o  where  no comando, seria atualizado o campo

produto_valor  para todos os registros da tabela. Vamos fazer
uma alteração sem  where , e atualizar o  data_criacao  de todos
os produtos.

postgres=> update produtos set data_criacao = '31/12/2016';

Utilize o  select  para visualizar todas as datas alteradas na
tabela  PRODUTOS .

postgres=> select data_criacao from produtos;

Inserimos, consultamos e alteramos nossos registros. Nada mais
normal haver situações nas quais será necessária a exclusão de
registros. Para isso, temos o comando  DELETE .

Vamos excluir uma mesa que não estamos usando atualmente.

**### Atualizando registros**

**### Excluindo registros**

**54** 
3.8 CONSULTANDO NOSSOS REGISTROS


--------------------------------------------------

postgres=> delete from mesas where id = 2;

Muita atenção ao realizar comandos  delete  no PostgreSQL,
pois você não vai recuperar o seu registro perdido. Se não colocar o

 where no comando de  delete , você está enviando a informação
para deletar todos os registros da tabela.

Em nosso comando, deixei especificado que era para deletar
apenas o registro com  id = 2 . O  delete  sem  where  é muito
famoso em pregar peças nos desenvolvedores desatentos.

Observe que apenas inserimos poucos registros em nossas
tabelas. Para colocar em prática o que vimos neste capítulo, insira
mais registros nelas. Insira pelo menos mais três em cada tabela.

Tente escrever os códigos. Depois que você tiver aprendido e
fixado como utiliza cada comando, então poderá usar o  CTRL+C  e

 CTRL+V .

Temos as tabelas e sabemos como alterar suas estruturas. Temos
registros, sabemos manipulá-los, inseri-los e alterá-los. Já temos o
básico para conseguirmos trabalhar com o PostgreSQL. Já podemos
partir para assuntos mais complexos. Treine um pouco o que já
aprendemos e #PartiuPróximoCapítulo.

## 3.9 PARA PENSAR!

3.9 PARA PENSAR! 
**55**


--------------------------------------------------

CAPÍTULO 4

"Você não precisa ser um gênio ou visionário — nem mesmo
graduado em uma faculdade sobre qualquer assunto — para ser bem-
sucedido. Você precisa apenas de estrutura e um sonho". — Michael
Dell

Funções são um conjunto de procedimentos escritos em  SQL 
que são armazenados no banco de dados a fim de executar uma
determinada função. Para mim, functions são procedimentos
armazenados no banco de dados que servem para agilizar o dia a dia
e otimizar seus códigos. Nelas podemos escrever instruções para
realizar operações como: consultar e retornar valores, realizar
cálculos e retornar ou não valores, chamar outros procedimentos, e
mais.

É comum no cotidiano dos desenvolvedores criar algumas
consultas para retornar dados básicos de uma tabela. Por exemplo,
se eu preciso consultar o nome de um funcionário e eu só tenho o
seu  id , eu crio uma  function  na qual passo o  id  como
parâmetro e, como retorno, tenho o nome do funcionário e
qualquer outra informação que desejo. Eu posso utilizar essa

 function em qualquer processo que desejar ou em consultas mais

# FUNCTIONS —
# AGILIZANDO O DIA A DIA

## 4.1 FUNCTIONS PARA POUPAR ESFORÇOS

**56** 
4 FUNCTIONS — AGILIZANDO O DIA A DIA


--------------------------------------------------

complexas. Vamos exemplificar para ficar mais claro.

Criaremos uma  function que retorne o nome do funcionário,
concatenando o campo  funcionario_situacao . Para isso, vamos
levar em consideração a seguinte tabela de possíveis valores para o
campo  funcionario_situacao .

**Sigla**
**Descrição**

A
Ativo

I
Inativo

Em nossa  function , passaremos como parâmetro o  id  e
verificaremos a situação. Em seguida, vamos concatenar a descrição
da situação com o seu nome.

No código, vamos passar como parâmetro o  id  do
funcionário, e depois teremos uma consulta para buscar o
funcionário e, como retorno, teremos o nome e a situação dele. Na
sequência, verificamos o tipo da situação e fazemos a concatenação
do nome e da descrição da situação. Vamos ao código.

postgres=# create or replace function 

           retorna_nome_funcionario(func_id int) 
           returns text as 
           $$              
           declare 
           nome     text;   
           situacao text;
           begin

             select funcionario_nome,
                    funcionario_situacao
               into nome, situacao
               from funcionarios
              where id = func_id;    

              if situacao = 'A' then
                return nome || ' Usuário Ativo';                 
              else                  
                return nome || ' Usuário Inativo';               

4.1 FUNCTIONS PARA POUPAR ESFORÇOS 
**57**


--------------------------------------------------

              end if;  

           end
           $$ 
           language plpgsql;

Em nosso código, temos alguns símbolos diferentes dos quais já
vimos. Não se preocupe, pois agora na sequência vou explicá-los.

Você percebeu algo diferente em nosso código? Os  $$  são
usados para limitar o corpo da função, e para o banco de dados
entender que tudo o que está dentro dos limites do cifrão duplo é
código de uma única função.

Cifrão não é parte do padrão SQL, mas muitas vezes é uma
forma mais conveniente para escrever  strings  literais
complicadas do que a sintaxe simples compatível com o padrão

 SQL . Observe que, além de nosso código ser grande, tivemos de
quebrar em algumas linhas para conseguirmos entendê-lo. O cifrão
está dizendo para o banco que todo o código contido entre eles
pertence ao mesmo código.

Se pesquisar na internet exemplos de  functions , você pode
encontrar o seguinte:

 $palavra_qualquer$
   begin

     Instruções da function();

   end
 $palavra_qualquer$

Observe que, em vez de utilizar apenas  $$ , escrevemos

 $palavra_qualquer$ . O cifrão é apenas um limitador e, por isso,
você pode usar uma outra palavra para limitar seu código.

**### Cifrão duplo ($$)**

**58** 
4.1 FUNCTIONS PARA POUPAR ESFORÇOS


--------------------------------------------------

Em processos de  function , temos a necessidade de utilizar
variáveis para armazenar informações temporariamente. Por isso,
precisamos fazer a declaração das variáveis, colocando o seu nome e
o seu tipo. Todas as variáveis que você precisar utilizar deverão ser
declaradas logo abaixo do  declare .

Em nosso código, nós fizemos a declaração da seguinte maneira:

   declare 
     nome     text;   
     situacao text;

No final do nosso bloco de instruções, devemos colocar

 language plpgsql , que é a linguagem que usamos para escrever
nossa  function . Ela, linguagem utilizada pelo PostgreSQL, está
para o PostgreSQL, assim como o PL/SQL está para o Oracle.

Nós colocamos no final do código, pois temos de informar que
estamos usando a linguagem  plpgsql . Isso porque, no
PostgreSQL, podemos utilizar outra linguagem de programação,
como a linguagem C. No entanto, este assunto não será abordado
neste livro, por se tratar de algo que não é muito utilizado no
mercado.

Em nossa  function , também utilizamos as declarações
condicionais  if... then... else . Se você ainda não está
familiarizado com alguma linguagem de programação, nós usamos
essas condições para testar uma condição e verificar se é verdadeira.

Em nosso exemplo, testamos se o  funcionario_situacao  do
funcionário era igual a  A , e escrevemos a instrução para que, se ele

**### Declare**

**### language plpgsql**

**### If e else**

4.1 FUNCTIONS PARA POUPAR ESFORÇOS 
**59**


--------------------------------------------------

fosse igual, concatenasse as palavras  Usuário Ativo  com o seu
nome. Caso contrário ( else ), ele concatenaria as palavras

 Usuário Inativo .

Há a possibilidade de testarmos quantas condições que
quisermos. Basta apenas utilizar as outras declarações do  if .
Vamos pegar apenas o corpo de nossa  function  e reescrevê-lo
colocando outras condições.

Vamos testar se o  funcionario_situacao  é igual a  A ,  I ,
vazio ou diferente das três condições.

$$
begin

 if situacao = 'A' then

   'Usuário Ativo';

 elsif situacao = 'I' then

    'Usuário Inativo'

 elsif situacao is null then

   'Usuário Sem status'

 else 

   'Usuário com status diferente de A e I'

 end if;  

end
$$

Veja que, após o primeiro  if , usamos  elsif  para verificar a
condição seguinte. Só quando eu não quero mais verificar nenhuma
condição, eu utilizo o  else .

Sempre que concluir a declaração de um  if , não esqueça de
escrever a sua finalização, o  end if . Só assim o PostgreSQL vai

**60** 
4.1 FUNCTIONS PARA POUPAR ESFORÇOS


--------------------------------------------------

entender que você está finalizando aquele bloco condicional.

Após termos criado e entendido como criar uma function,
vamos 
aprender 
como 
usá-la. 
A 
function 
criada, 
a

 retorna_nome_funcionario , tem um retorno, certo? Sim, pois
criamos para buscar o nome de um funcionário. E como ela possui
um retorno, que é o nome do funcionário e sua situação, devemos
utilizá-la em uma consulta. Portanto, vamos criar uma consulta.

Como parâmetro, devemos passar o  id  do funcionário.
Sabendo disso, vamos passar como parâmetro o  id 1 .

postgresql=> select retorna_nome_funcionario(1);

O resultado da nossa consulta será:

Figura 4.1: Resultado da função retorna_nome_funcionario

Com o tempo, você vai criando  functions automaticamente e
conseguindo enxergar onde poderá utilizá-las. É muito comum no
começo, quanto estamos aprendendo alguma linguagem ou
tecnologia, não conseguirmos saber onde e quando usar. Mas isso só
a prática lhe dirá.

Para fixar ainda mais, vamos criar outra  function  que vai
retornar o valor da porcentagem de comissão de cada funcionário,
pois vamos utilizar mais à frente para criar um processo que
calculará um valor de comissão de cada venda. Então, vamos lá,

## 4.2 UTILIZANDO A FUNCTION

4.2 UTILIZANDO A FUNCTION 
**61**


--------------------------------------------------

mãos no teclado.

Novamente vamos passar como parâmetro o  id  do
funcionário e, como retorno, pegaremos o valor do campo

 funcionario_comissao .

postgresql=> create or replace function 

           rt_valor_comissao(func_id int)
           returns real as 
           $$
           declare             
             valor_comissao real;

           begin              
             select funcionario_comissao
               into valor_comissao
               from funcionarios
              where id = func_id;               
              return valor_comissao;
           end
           $$
           LANGUAGE plpgsql;

Vamos testar nossa  function .

postgresql=> select rt_valor_comissao(1);

E como resultado, temos:

Figura 4.2: Resultado da função rt_valor_comissao

No PostgreSQL, temos as functions que possuem algum retorno
e podemos utilizá-lo por meio das consultas. Temos também as que

## 4.3 FUNCTIONS SEM RETURN

**62** 
4.3 FUNCTIONS SEM RETURN


--------------------------------------------------

não possuem retorno. Elas são usadas para executar determinados
processos internamente no banco de dados.

Usamos esse tipo de function quando desejamos realizar um
processamento que envolve vários registros. Para não precisarmos
executar cada consulta ou processo isoladamente, colocamos várias
instruções dentro da function e falamos para o banco de dados
executar essas instruções quando necessário.

Vamos criar agora uma  function  que fará o cálculo de
comissionamento de todos funcionários das vendas que tiveram em
algum período. Aproveite este exemplo para exercitar a inserção de
valores nas tabelas e popule a tabela  vendas  e  itens_vendas ,
para que você tenha vários registros para trabalhar, além dos que
inserimos anteriormente. Agora, mãos no teclado e vamos a nossa

 function .

Para este cenário, vamos supor que a sua empresa realiza o
cálculo de comissionamento levando em consideração um período
de vendas. Nele vamos passar por parâmetro uma data inicial e uma
final, para o nosso processo buscar todas as vendas que foram feitas
nesse intervalo.

A nossa consulta também vai levar em consideração apenas as
vendas cujo campo  venda_situacao  seja igual a  A . Isso porque,
após calcular a comissão da venda, vamos fazer um  udpate  nesse
campo para  C , para indicar que a venda já foi comissionada, e não
corra o risco de ser comissionada novamente. O nosso processo vai
pegar todas as vendas que foram realizadas e todos os funcionários,
calcular suas comissões e inserir na tabela  comissoes .

create or replace function 

            calc_comissao(data_ini timestamp,
                          data_fim timestamp)
            returns void as $$
            declare 

4.3 FUNCTIONS SEM RETURN 
**63**


--------------------------------------------------

            -- declaração das variáveis que vamos
            -- utilizar. Já na declaração elas
            -- recebem o valor zero. Pois assim
            -- garanto que elas estarão zeradas
            -- quando for utilizá-las.

               total_comissao  real := 0;
               porc_comissao   real := 0;

            -- declarando uma variável para armazenar 
            -- os registros dos loops
               reg             record;

            --cursor para buscar a % de comissão do funcionário

              cr_porce CURSOR (func_id int) IS 
                  select rt_valor_comissao(func_id);

             begin

            -- realiza um loop e busca todas as vendas
            --  no período informado

                for reg in( 
                  select vendas.id id,
                         funcionario_id,
                         venda_total
                    from vendas
                   where data_criacao >= data_ini
                     and data_criacao <= data_fim 
                     and venda_situacao = 'A')loop         

            -- abertura, utilização e fechamento do cursor

                  open cr_porce(reg.funcionario_id);
                  fetch cr_porce into porc_comissao;
                  close cr_porce;

                  total_comissao := (reg.venda_total * 
                                    porc_comissao)/100;

            -- insere na tabela de comissões o valor 
            -- que o funcionário irá receber de comissão
            -- daquela venda

                  insert into comissoes(
                                        funcionario_id,

**64** 
4.3 FUNCTIONS SEM RETURN


--------------------------------------------------

                                       comissao_valor,
                                       comissao_situacao,
                                       data_criacao,
                                       data_atualizacao) 
                 values(reg.funcionario_id,
                        total_comissao,
                        'A',
                        now(),
                        now());

           -- update na situação da venda 
           -- para que ela não seja mais comissionada

                 update vendas set venda_situacao = 'C'
                  where id = reg.id;

           -- devemos zerar as variáveis para reutilizá-las

                  total_comissao := 0;
                  porc_comissao  := 0;

           -- término do loop

               end loop;                                    

            end
            $$ language plpgsql;

Para executar este processo, usaremos o seguinte comando:

postgresql=> select calc_comissao('01/01/2016 00:00:00','01/01/201
6 00:00:00');

Como resultado, teremos:

Figura 4.3: Resultado da função calc_comissao

Agora vamos ver os registros na tabela  comissoes . Vamos
consultar as comissões do funcionário  id = 1 .

4.3 FUNCTIONS SEM RETURN 
**65**


--------------------------------------------------

postgresql=> select comissao_valor,

                   data_criacao
              from comissoes;

Com isso, temos cada comissão gerada de todas as vendas do
funcionário.

Figura 4.4: Comissões geradada do funcionário id = 1

Assim como vimos alguns elementos novos quando em nossa
primeira function, nesta última, podemos observar alguns
elementos com que ainda não tínhamos trabalhado.

Um pouco mais de código, não é mesmo? E eu utilizei um
conceito novo. Declarei um cursor  cr_porce , usado para
armazenar uma consulta e onde o desejamos no código. Em vez de
colocarmos o  select  ao meio do código, nós declaramos um
cursor com essa consulta e o utilizamos onde desejamos na

 function . Com isso, separamos o processo das consultas
auxiliares, e o código fica mais limpo.

Mas cuidado com o excesso de cursores, pois é consumido um
pouco de memória do servidor em cada abertura de um  cursor .
Para usá-lo, não esqueça de abri-lo e fechá-lo.

**### Cursor**

**66** 
4.3 FUNCTIONS SEM RETURN


--------------------------------------------------

O  fetch  é utilizado para pegar o valor da consulta e jogá-lo
para uma variável. Não tem um número exato mínimo ou máximo
de cursores que devemos usar. Com a prática, você aprenderá a
otimizar seu código e observar o que deixa o código rápido ou lento.

A instrução  loop  define um laço incondicional, repetido
indefinidamente até ser terminado. O  for  cria um laço que
interage em um intervalo de valores inteiros. A variável  reg  é
definida automaticamente como sendo do tipo  integer , e
somente existe dentro do laço.

Em nosso exemplo, utilizamos o  for... loop  para varrer
todas as vendas que foram realizadas em um determinado período e
fazer os cálculos de comissionamento.

É muito comum alterações nas regras de negócios que impactam
nos códigos de seus projetos, e você acaba tendo de modificar e criar
novamente as  functions . Observe na sintaxe de criação onde
escrevemos  create or replace . Isso significa que, ao inserir o
código no terminal de comando do PostgreSQL, o gerenciador vai
criar ou substituir o procedimento. Isso quer dizer que, se você fizer
qualquer alteração nos códigos, é só inserir novamente que o SGBD
vai atualizar o procedimento em questão.

Há a possibilidade da alteração de uma  function , mas eu não
recomendo, pois isso pode impactar e ocasionar erros em outras
partes de seu sistema nas quais ela possa estar sendo utilizada.
Prefira criar uma nova  function  com o nome que deseja, e se
necessário exclua a que não desejar mais, e tenha certeza de que ela
não está sendo utilizada em nenhum trecho.

**### For... loop... end loop**

## 4.4 ALTERANDO FUNCTIONS

4.4 ALTERANDO FUNCTIONS 
**67**


--------------------------------------------------

Para excluir uma function, usaremos o comando  drop

function... . Vamos excluir a  calc_comissoes com o comando:

postgresql=> drop function calc_comissoes();

**A****TENÇÃO****!**

Ao excluir uma function, tenha certeza de que ela não está
sendo usada em nenhum processo em seu projeto.

A principal vantagem da utilização desse procedimento é a
reutilização em qualquer lugar no projeto de banco de dados. Você
escreve uma vez e reutiliza onde desejar.

O conceito da programação das regras de negócio no banco de
dados (isto é, deixar a parte de cálculos e regras em procedimentos
armazenados no banco) é algo que gera muitas discussões. Isto por
causa de linguagens de programação que fazem isso bem, como o
Java, Ruby on Rails, entre outras. Mas isso vai depender do cenário
em que você estiver trabalhando e também da tecnologia.

Não há dúvidas de que o processamento direto no banco é
muito rápido. Porém, isso também dependerá de seu código ser
consistente. E como é comum aos desenvolvedores fazerem a
refatoração de suas aplicações, no banco de dados não é diferente.
Conforme as consultas vão se tornando complexas, vai se exigindo
mais do banco de dados. Por isso, elas devem estar em constante

## 4.5 EXCLUINDO FUNCTIONS

## 4.6 
## VANTAGENS 
## DA 
## UTILIZAÇÃO 
## DAS
## FUNCTIONS

**68** 
4.5 EXCLUINDO FUNCTIONS


--------------------------------------------------

refatoração.

Otimizar e automatizar. Algo que vimos bastante neste capítulo.
São duas palavras muito presentes na vida do programador.
Estamos sempre otimizando e procurando uma maneira de
melhorar códigos e processos. Tenha isso em mente e sempre terá
excelentes códigos em seus projetos.

Agora, se estiver trabalhando em algum projeto que não seja este
do livro, pense em como otimizar seus códigos por meio de
function! Se não tiver nenhum código, crie novas funções para as
outras tabelas que não fizemos.

Gostou de criar functions que podemos reutilizar? E de criar
processos para automatizar? Vamos trabalhar mais um pouco com
funções, mas agora com as embutidas no SGBD. Elas são muito
úteis. #PartiuConsultar

## 4.7 PARA PENSAR!

4.7 PARA PENSAR! 
**69**


--------------------------------------------------

CAPÍTULO 5

"Mova-se rapidamente e quebre as coisas. A menos que você não
esteja quebrando coisas, você não está se movendo rápido o
suficiente". — Mark Zuckerberg

Nativamente no PostgreSQL, assim como em outros bancos,
como MySQL e Oracle, possui funções e operadores para os tipos de
dados nativos, que fazem determinadas tarefas e estão armazenadas
nele. Tarefas que rotineiramente necessitamos quando estamos
desenvolvendo software, por exemplo, calcular a quantidade de
caracteres em uma  string  ou o valor máximo armazenado em
uma coluna de uma determinada tabela.

Estes são exemplos de funções que estão embutidas no banco de
dados e podemos utilizar em nossas consultas e processos. São
muito úteis, uma vez que são operações simples que seriam muito
trabalhosas para fazer na mão.

Separei este capítulo para mostrar essas funções. Elas estão
divididas em grupos: as funções numéricas, utilizadas para
manipularmos números e extrair informações deles; as funções para
trabalharmos com cadeias de caracteres, utilizadas para criar
funções com texto; e as funções para trabalhamos com datas e

# FUNÇÕES, OPERADORES E
# OPERAÇÕES

## 5.1 FUNÇÕES EMBUTIDAS

**70** 
5 FUNÇÕES, OPERADORES E OPERAÇÕES


--------------------------------------------------

horários e extrair informações destes tipos de dados.

Uma preocupação levada em consideração nos mais variados
SGBD, ao usarem este padrão, é a possibilidade da portabilidade.
Isso torna as funcionalidades do PostgreSQL compatíveis e
consistentes entre as várias implementações em outros bancos.

Antes de apresentar cada grupo de função, serão apresentados
os operadores de grupo. Por exemplo, antes de apresentar as
funções 
matemáticas, 
serão 
apresentados 
os 
operadores
matemáticos, e assim sucessivamente.

Mas antes de apresentar os operadores possuidores de funções,
temos de conhecer os operadores lógicos e os de comparação.

Até o momento em que aprendemos a trabalhar com

 functions , não tínhamos feito consultas usando outros
operadores além do  where . Quando criamos a  function

calc_comissao , utilizamos o operador lógico  AND , como mostra a
consulta a seguir:

  select venda_id,
         funcionario_id,
         venda_total
   from  vendas
  where data_criacao >= 'data_ini'
    and data_criacao <= 'data_fim'
    and produto_situacao = 'A'

Os operadores lógicos que o PostgreSQL possui são os três
habituais. Se você já começou ao menos a estudar lógica de
programação, já deve ter esbarrado com eles.

**Operador**
**Descrição**

AND
Utilizamos quando queremos incluir duas ou mais condições em nossa
operação. Os registros recuperados em uma declaração que une duas

## 5.2 OPERADORES LÓGICOS

5.2 OPERADORES LÓGICOS 
**71**


--------------------------------------------------

condições com este operador deverão suprir as duas ou mais condições

OR
Utilizamos quando queremos combinar duas ou mais condições em nossa
operação. Os registros recuperados em uma declaração que une duas
condições com este operador deverão suprir uma das duas condições

NOT
Utilizamos quando não queremos que uma das condições seja cumprida. Os
registros recuperados em uma declaração que exclui uma condição não
deverão trazer aqueles que cumprem a condição que se está testando

Vamos consultar para exemplificar os outros operadores que
ainda não usamos. Para isso, inseriremos um novo produto.

postgres=> insert into produtos (produto_codigo,

                                produto_nome,
                                produto_valor,
                                produto_situacao,
                                data_criacao,
                                data_atualizacao)
                         values ('2832',
                                 'SUCO DE LIMÃO',
                                  15,
                                 'C',
                                 '02/02/2016',
                                 '02/02/2016');

Agora vamos consultar os produtos que possuem os produtos
cancelados **E** os produtos que estão ativos.

postgres=> select * 

            from produtos
           where produto_situacao = 'A'
             and produto_situacao = 'C';

Figura 5.1: Consulta com o operador AND

Como você pode ver, o resultado de nossa consulta não nos
trouxe nada. Isso acontece pois não temos nenhum produto que
está ativo e cancelado ao mesmo tempo. Agora, vamos modificá-la
um pouco e consultar os produtos que estão ativos **OU** os que estão

**72** 
5.2 OPERADORES LÓGICOS


--------------------------------------------------

cancelados.

postgres=> select * 

            from produtos
           where produto_situacao = 'A'
              or produto_situacao = 'C';

Figura 5.2: Consulta com o operador OR

O resultado mudou um pouco, não é mesmo? Pois temos
produtos que estão ativos e temos outros que estão cancelados.

Agora vamos criar uma consulta para buscar os produtos que
não possuam o campo  produto_nome  igual a  SUCO DE LIMÃO .
Vamos ao nosso código.

postgres=> select * 

            from produtos
           where not produto_nome = 'SUCO DE LIMÃO';

Figura 5.3: Consulta com o operador NOT

Na última consulta, negamos a condição declarada, que era

 produto_nome = 'SUCO DE LIMÃO' .

Além de utilizá-los separadamente, podemos criar consultas
unindo-os. Mãos no teclado. Vamos criar uma consulta para buscar
os produtos que estão ativos **OU** que estejam cancelados **E** possuam

5.2 OPERADORES LÓGICOS 
**73**


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------

Existem recursos disponíveis em cada tipo de linguagem de
programação ou banco de dados que usamos diariamente. As
funções, sejam elas matemáticas ou de caracteres, são algo que
utilizamos nas mais diversas situações. É importante que você sabia
que elas existem, mas não é necessário decorar cada uma delas.
Sabendo que um recurso existe, você saberá onde deve procurá-lo.

**Funções**
**Descrição**
**Exemplo**
**Resultado**

abs(variável)
Para calcular o
valor absoluto de
uma variável
select abs(-5);
5

cbrt(variável)

Para calcular o
valor da raiz
cúbica de uma
variável

select cbrt(8);
2

ceil(variável)

Para calcular o
menor valor que
seja maior ou igual
à variável

select ceil(14.2);
15

ceiling(variável)
O mesmo que o
ceil
*select
ceil(-51.1);v
-31

degrees(variável)

Utilizado para
converter um valor
de radianos para
graus

select degrees(1)
57.2957795130823

div(variável x,
variável y)

Utilizado para
fazer a divisão
entre dois
números

select div(8,4);
2

exp(variável)
Utilizado para
fazer cálculo de
exponenciação
select exp(2);
7.38905609893065

floor(variável)

Utilizado para
encontrar o maior
número inteiro
não maior que a
variável

select
floor(-12.9);
-13

ln(variável)

Calcular e mostrar
o valor do
select ln(2.0)
0.693147180559945

**### Funções matemáticas**

5.4 OPERADORES E FUNÇÕES MATEMÁTICAS 
**77**


--------------------------------------------------

logaritmo comum

log(variável)
Utilizado para
calcular logaritmo
na base 10
select log(10)
2

log(variável b,
variável k)
Logaritmo na base
b
select log(100.2);
2.0008677215312267

mod(variável x,
variável y)

Cálculo do resto da
divisão de dois
números
select mod(11,2);
1

pi()
Retorna o valor de
pi
select pi();
3.14159265358979

power(variável x
, variável y)

Faz o cálculo
exponencial da
variável x pela y

select power(9.0,
3.0);
729

radians(variável)
Faz o cálculo de
conversão para
graus radianos
select rad(12);
0.20943951023932

round(variável)

Faz o
arredondamento
da variável
informada

select
round(25.2);
25

round(variável
x, variável y)

Realiza o
arredondamento
para o número
especificado
depois da vírgula

select
round(54.123,2);
54.12

sqrt(variável)
Calcula a raiz
quadrada de um
número
selecr sqrt(9);
3

trunc(variável)

Utilizado para
separar o número
inteiro dos
decimais

select
trunc(335.23);
335

trunc(variável x,
variável y)

Utilizado para
separar uma
quantidade
específica de
números decimais

select
trunc(335.123,2);
335.12

Há também algumas funções trigonométricas. São elas:

**Function**
**Descrição**
**Exemplo**
**Resultado**

**78** 
5.4 OPERADORES E FUNÇÕES MATEMÁTICAS


--------------------------------------------------

acos(variável
X)
Utilizado para calcular o
inverso do cosseno
select
acos(0);
1.5707963267949

asin(variável
X)
Utilizado para calcular o
inverso do seno
select
asin(0.2);
0.201357920790331

atan(variávelx)
Utilizado para calcular o
inverso da tangente
select
atan(2);
1.10714871779409

cos(variávelx)
Utilizado para calcular o
valor do cosseno
select
cos(3);
-0.989992496600445

cot(variávelx)
Utilizado para calcular o
valor do cotangente
select
cot(3);
-7.01525255143453

sin(variávelx)
Utilizado para calcular o
valor do seno
select
sin(3);
0.141120008059867

tan(variávelx)
Utilizado para calcular o
valor da tangente
select
tan(3);
-0.142546543074278

Para trabalharmos com caracteres do tipo  string , temos
algumas funções específicas.

Utilizando as tabelas criadas no banco, vamos concatenar o
código de um funcionário com seu nome. A consulta vai juntar o
código e o nome em uma só coluna:

postgres=# select funcionario_codigo || funcionario_nome 

              from funcionarios
             where id = 1;

Fica estranho tudo junto, não é mesmo? Vamos colocar mais
um item em nossa concatenação.

select (funcionario_codigo ||' '|| funcionario_nome)

 from funcionarios
 where id = 1;

## 5.5 FUNÇÕES DE TEXTO

**### || para concatenar strings**

5.5 FUNÇÕES DE TEXTO 
**79**


--------------------------------------------------

Incluir um caractere de espaço no resultado ficou bem melhor.
Não necessariamente temos de ter apenas caracteres do tipo

 string . Poderíamos ter um do tipo numérico no lugar do de
espaço.

select (funcionario_codigo ||8|| funcionario_nome)

 from funcionarios
 where id = 1;

Você já deve ter se deparado com sites que possuem formulário
de cadastro, nos quais a senha ou o nome de usuário deve possuir
um número mínimo de caracteres. Podemos fazer essa contagem de
caracteres através de uma função que o SGBD possui. Vamos contar
os caracteres do nome de um funcionário.

postgres=# select char_length(funcionario_nome)

              from funcionarios
             where id = 2;

Como uma função dessas, você já pode verificar se um
determinado campo já está sendo preenchido corretamente.

Em determinados sistemas, é muito comum as informações que
estão armazenadas no banco de dados estarem todas maiúsculas,
por uma questão de padronização de quem está desenvolvendo o
sistema, como por uma questão de estética, quando forem
mostradas para os usuários. Essa função pode lhe ajudar nessa
tarefa.

Vamos selecionar todos os nomes de funcionários. Se algum

**### Contando **
**### os **
**### caracteres **
**### de **
**### uma **
**### string **
**### com**
**### char_length(string) ou length(string)**

**### Transformando letras minúsculas em maiúsculas com**
**### upper(string)**

**80** 
5.5 FUNÇÕES DE TEXTO


--------------------------------------------------

registro estiver salvo no banco com letras minúsculas, será mostrado
como maiúscula.

postgres=# select upper(funcionario_nome)

              from funcionarios;

Como nenhum exemplo de inserção de registro no banco foi
feito com letras minúsculas, para você ver melhor o efeito de
alteração das letras, utilize a seguinte consulta:

postgres=# select upper('livro postgresql');

E para deixar apenas as primeiras letras de cada palavra em
maiúsculo, podemos usar o comando  initcap . Como resultado,
teremos  Livro Postgresql .

postgres=# select initcap('livro postgresql');

Assim como temos uma função para transformar letras
minúsculas em maiúsculas, temos uma função que faz o contrário:
transforma maiúsculas em minúsculas. Vamos deixar todos os
nomes de funcionários em letras minúsculas.

postgres=# select lower(funcionario_nome)

             from funcionarios;

Se você se deparar em alguma situação em seu sistema, na qual
precisa ocultar ou substituir alguma parte de uma  string , você
pode utilizar esta função. É muito comum, em alguns sites,
ocultarem uma parte de seu nome ou e-mail por uma questão de
segurança.

Utilizando novamente o nome de um funcionário que está em

**### Transformando maiúsculas em minúsculas com**
**### lower(string)**

**### Substituindo string com overlay() e extraindo com**
**### substring()**

5.5 FUNÇÕES DE TEXTO 
**81**


--------------------------------------------------

nosso banco de dados, vamos substituir uma parte de seu nome com
caracteres  000000 . Para isso, temos de informar a partir de qual
caractere e até qual caractere a substituição deve ocorrer.

postgres=# select overlay(funcionario_nome placing '000000' 

                          from 3 for 5) 
              from funcionarios 
             where id = 1;

Fizemos a substituição de uma parte da  string . Agora vamos
realizar a extração desse mesmo trecho da  string . A nossa
consulta vai ficar só um pouco diferente. Mãos no código.

postgres=# select substring(funcionario_nome from 3 for 5)

              from funcionarios
             where id = 1;

Quando estamos fazendo aquela pesquisa da Wikipédia e
estamos com preguiça de procurar um determinado termo, nada
melhor que utilizar o bom e velho  CTRL + F  e pesquisar o termo
dentro de um texto. Esta função tem o objetivo de identificar em
qual posição se encontra um caractere ou se inicia uma  string .

Utilizando o nome do funcionário com  id = 1  cujo nome é

 VINICIUS , vamos localizar em qual posição se encontra a  string

CIUS .

postgres=# select position('CIUS' in funcionario_nome) 

              from funcionarios
             where id = 1;

Se você já trabalha com programação ou se não trabalha, vai
descobrir que trabalhar com data e hora em seu sistema dá um
pouco de trabalho. Não importa a linguagem, de cada três

**### Localizando uma string position()**

## 5.6 FUNÇÕES DATA/HORA

**82** 
5.6 FUNÇÕES DATA/HORA


--------------------------------------------------

desenvolvedores, dois já tiveram problemas neste quesito.

As funções para data/hora dão uma grande ajuda, pois já
existem algumas prontas para tarefas, como calcular a quantidade
de dias que há entre duas datas ou a quantidade de anos de uma
determinada pessoa, apenas informando uma data de entrada como
parâmetro.

**D****ICA**

O formato de data que usamos aqui no Brasil é Dia/Mês/Ano,
diferente do de outros países. A maioria dos gerenciadores de
banco 
de 
dados 
utilizam 
como 
padrão 
o 
formato
Mês/Dia/Ano, ou Ano/Mês/Dia. E para você saber em qual
formato está o seu banco de dados e mudar para o desejado,
vamos fazer o seguinte.

Primeiro, vamos utilizar um comando para descobrir o
formato de data atual do banco. Nós consultaremos a variável
do banco de dados que armazena esta informação, que é o

 datestyle .

postgres=# show datestyle;

Como resultado, descobri que o meu banco de dados está no
formato Mês/Dia/Ano.

Figura 5.6: Formato de datas atual do banco de dados

5.6 FUNÇÕES DATA/HORA 
**83**


--------------------------------------------------

Sabendo disso, vamos alterar o formato do nosso banco para o
que queremos, que é o formato Dia/Mês/Ano. Para isso,
faremos um comando que alterará a variável  datestyle .

postgres=# alter database postgres set datestyle to iso, dmy;

E se você estiver logado no terminal do banco de dados, você
pode executá-lo para aplicar essa alteração na sessão em que
estiver logado.

postgres=# set datestyle to iso, dmy;

Se consultarmos novamente o formato do banco, vamos obter
como resultado:

Figura 5.7: Formato de datas atual do banco de dados

Com essa alteração, podemos prosseguir com o projeto e utilizar
datas no formato que conhecemos durante o nosso projeto.

Para criar uma função manualmente que traga quantos anos,
meses e dias você tem é algo muito trabalhoso. O PostgreSQL e
outros banco de dados sabem disso, e sabem que é uma função
muito usada. O SGBD já possui uma função que realiza essa tarefa, a

 age() .

Vamos calcular agora a minha idade. Você pode usar a sua data

**### Funções de idade**

**84** 
5.6 FUNÇÕES DATA/HORA


--------------------------------------------------

de aniversário para saber sua idade exatamente. Mãos no teclado e
vamos ao nosso código.

postgres=# select age(timestamp '04/11/1988');

Figura 5.8: Calculando a idade

É possível também calcular a idade baseado em duas datas da
seguinte maneira:

postgresq=# select age(timestamp '07/05/2016', 

                      timestamp '12/05/2007');

Figura 5.9: Calculando a idade entre duas datas

A todo momento estamos olhando no relógio para saber o
horário. E no desenvolvimento de software, por uma infinidade de
motivos, temos de consultar a data e hora para criar validações em
nosso sistema.

Imagine que você precise bloquear o acesso dos usuários depois
que a conta deles esteja vencida. Para isso, você deverá conferir a
data de vencimento delas com a data atual. E muitas vezes, deverá
também levar em consideração o horário em que está fazendo a
consulta para realizar o bloqueio.

**### Funções para consultar data, hora e data/hora atuais**

5.6 FUNÇÕES DATA/HORA 
**85**


--------------------------------------------------

Para a nossa salvação, o PostgreSQL fornece algumas maneiras
para consultarmos data, hora e data/hora atuais. Essas funções estão
relacionadas na tabela a seguir.

**Função**
**Descrição**
**Exemplo**

clock_timestamp()
Data e hora atual
select clock_timestamp();

current_date
Data atual
select current_date;

current_time
Hora atual
select current_time;

current_timestamp
Data e hora atual
select current_timestamp;

localtime
Hora atual
select localtime;

localtimestamp
Data e hora atual
select localtimestamp;

now()
Data e hora atual
select now();

statement_timestamp()
Data e hora atual
select
statement_timestamp();

timeofday()
Data e hora atual no formato de
texto
select timeofday();

Muitas dessas funções de datas e horários podem ser utilizadas
para a mesma finalidade. Escolha a que desejar!

Para trabalharmos com data e horário, também temos à nossa
disposição as funções:

**Função**
**Descrição**
**Exemplo**

date_part('day',
timestamp)
Extrai o dia da data/hora
informada

select date_part('day',
timestamp '04/11/1988
20:38:40');

date_part('month',
timestamp)
Extrai o mês da data/hora
informada

select date_part('day',
timestamp '04/11/1988
20:38:40');

date_part('year',
timestamp)
Extrai o ano da data/hora
informada

select date_part('day',
timestamp '04/11/1988
20:38:40');

date_part('hour',
timestamp)

Extrai a hora da data/hora
informada
select date_part('day',
timestamp '04/11/1988
20:38:40');

**86** 
5.6 FUNÇÕES DATA/HORA


--------------------------------------------------

date_part('minute',
timestamp)
Extrai os minutos da data/hora
informada

select date_part('day',
timestamp '04/11/1988
20:38:40');

date_part('second',
timestamp)
Extrai os segundos da
data/hora informada

select date_part('day',
timestamp '04/11/1988
20:38:40');

justify_days(intervalo)
Conta a quantidade de meses
em um invervalo de dias

select
justify_days(interval
'43 days');

justify_hours(intervalo)
Conta a quantidade de dias em
um intervalo de horas

select
justify_hours(interval
'32 hours');

justify_interval(intervalo)
Calcula a quantidade de meses,
dias ou horas, subtraindo
meses com horas

select
justify_interval(interval
'2 mon - 25 hours');

justify_interval(intervalo)
Calcula a quantidade de meses,
dias ou horas, subtraindo
meses com dias

select
justify_interval(interval
'2 mon - 14 days');

justify_interval(intervalo)
Calcula a quantidade de meses,
dias ou horas, subtraindo dias
com horas

select
justify_interval(interval
'3 days - 8 hour');

justify_interval(intervalo)
Calcula a quantidade de meses,
dias ou horas, somando meses
com horas

select
justify_interval(interval
'4 mon - 28 hour');

Uma outra função muito interessante é o  extract . Com ela, é
possível extrair diversas informações de uma variável de data/hora,
data ou somente hora. Ela sempre vai retornar um resultado do tipo

 double . As informações mais relevantes que essa função pode
extrair são:

**Função**
**Descrição**
**Exemplo**

century
Para extrair o século de uma
determinada data
select extract (century from
timestamp '04/11/1988 12:21:13');

day
Para extrair o dia de uma
determinada data
select extract (day from timestamp
'04/11/1988 12:21:13');

decade
Para a extrair a década de uma
determinada data
select extract (decade from
timestamp '04/11/1988 12:21:13');

doy
Para extrair o dia do ano de uma
select extract (doy from timestamp

5.6 FUNÇÕES DATA/HORA 
**87**


--------------------------------------------------

determinada data
'04/11/1988 12:21:13');

hour
Para extrair a hora de um
determinado horário
select extract (hour from timestamp
'04/11/1988 12:21:13');

year
Para extrair o ano de uma
determinada data
select extract (year from timestamp
'04/11/1988 12:21:13');

minute
Para extrair os minutos de um
determinado horário
select extract (minute from
timestamp '04/11/1988 12:21:13');

month
Para extrair o mês de uma
determinada data
select extract (month from
timestamp '04/11/1988 12:21:13');

second
Para extrair o valor dos segundos de
um determinado horário
select extract (second from
timestamp '04/11/1988 12:21:13');

Para utilizar o  extract em uma das tabelas do nosso projeto, o
código será:

postgres=# select extract(year from data_criacao) 

            from funcionarios where id = 1;

Essas funções que extraem informações de uma determinada
data e horário são muito úteis quando estamos desenvolvendo uma
aplicação e precisamos exibir ao usuário alguma informação
baseada em datas do sistema. Para não precisarmos programar os
cálculos, o banco de dados já tem essas funções para nos auxiliar.

As funções agregadoras são, sem sombra de dúvidas, as mais
importantes e as mais usadas nas consultas do dia a dia de um
programador. Isso porque é com elas que fazemos cálculos e
extraímos informações importantes dos nossos dados.

Sem olhar no banco de dados, você sabe quantos registros já
temos na tabela  funcionarios ? Conforme a quantidade de
registros no banco de dados vai aumentando, é claro que não

## 5.7 FUNÇÕES AGREGADORAS

**### Contando nossos registros com count(*)**

**88** 
5.7 FUNÇÕES AGREGADORAS


--------------------------------------------------

conseguimos acompanhar e saber quantos uma tabela contém. Para
nos auxiliar nessa tarefa, temos uma função muito bacana, o

 count(*) .

Vamos contar quantos registros a nossa tabela possui. Mãos no
teclado e vamos escrever essa consulta.

postgres=# select count(*)

            from funcionarios;

Figura 5.10: Contando os registro da tabela funcionarios

**D****ICA****!**

Quando a tabela não possui muitos registros nem muitos
campos, podemos usar o  *  (asterisco) entre parênteses. No
entanto, quando uma tabela possui muitos registros e campos,
procure utilizar um campo entre parênteses, de preferência a
chave primária da tabela.

Quando o  *  é usado, o banco utiliza todos os campos para
fazer a contagem. Isso faz com que ele fique lento e a consulta
demore. Quando indicamos um campo, a consulta ganha
performance. Ela ficaria da seguinte maneira:  select

count(**id**) from funcionarios .

**### Somando as colunas utilizando sum()**

5.7 FUNÇÕES AGREGADORAS 
**89**


--------------------------------------------------

O foco dos sistemas que estamos desenvolvendo durante o livro
são vendas. Então, saber a soma de todas as vendas é um dos
objetivos quando se tem um sistema de vendas. Vamos calcular o
total de vendas que fizemos até agora.

postgres=# select sum(venda_total)

            from vendas;

Levando em consideração que você não tenha inserido
nenhuma outra venda, além das que inserimos no começo do livro,
como resultado você também terá:

Figura 5.11: Somando nossas vendas

Se você inseriu mais registros, não tem problema. Você está de
parabéns, isso mostra que você está praticando bem os assuntos de
que estamos tratando.

Agora que já possuímos o valor total de todas as vendas, vamos
calcular a média de preço dos produtos que comercializamos. Para
essa tarefa, usaremos a função  avg() .

postgres=# select avg(produto_valor)

            from produtos;

**### Calculando a média dos valores com avg()**

**90** 
5.7 FUNÇÕES AGREGADORAS


--------------------------------------------------

Figura 5.12: Calculando o valor médio dos produtos

Temos a média dos valores dos produtos. A média varia com os
maiores e menores preços dos produtos. E para saber qual o
produto de maior valor e o de menor? Também temos uma função
para nos auxiliar nessa tarefa. É a função  max()  e  min() , para
encontrarmos o maior e o menor valor, respectivamente. Então,
mãos no teclado e vamos lá!

postgres=# select max(produto_valor), min(produto_valor)

            from produtos;

Figura 5.13: Valor máximo e mínimo

Descobrimos algumas informações interessantes sobre os nossos
dados. Descobrimos o total de vendas, o valor médio de nossos
produtos e o maior e o menor valor de um produto que temos em
nosso banco. Agora vamos criar uma consulta para buscarmos a
venda de cada produto vendido. Usaremos uma função que já
conhecemos, a  sum() , e conheceremos uma nova função
agregadora, a  group by .

**### Valores máximos e mínimos de uma coluna com max()**
**### e min()**

**### Agrupando registros iguais com group by**

5.7 FUNÇÕES AGREGADORAS 
**91**


--------------------------------------------------

Vamos utilizá-la para agrupar os registros iguais para criar
algum tipo de totalizador, que no nosso caso será a soma das vendas
de cada produto. Mãos no teclado e vamos à nossa consulta. Mas
antes de criarmos, vamos inserir mais alguns registros nas tabelas

vendas e  itens_vendas para termos mais dados para testarmos.

postgres=> insert into vendas (id, 

 funcionario_id,
 mesa_id,
 venda_codigo,
 venda_valor,
 venda_total,
 venda_desconto,
 venda_situacao,
 data_criacao,
 data_atualizacao)
 values (10000,

 1,
 1,
 '10201',
 '51',
 '51',
 '0',
 'A',
 '01/01/2016',
 '01/01/2016');

postgres=> insert into itens_vendas (produto_id,

 vendas_id,
 item_valor,
 item_quantidade,
 item_total,
 data_criacao,
 data_atualizacao)
 values (4,

 10000,
 15,
 2,
 30,
 '01/01/2016',
 '01/01/2016');

postgres=> insert into itens_vendas (produto_id,

 vendas_id,
 item_valor,
 item_quantidade,

**92** 
5.7 FUNÇÕES AGREGADORAS


--------------------------------------------------

                                    item_total,
                                    data_criacao,
                                    data_atualizacao)
                            values (3,
                                    10000,
                                    7,
                                    3,
                                    21,
                                    '01/01/2016',
                                    '01/01/2016');               
postgres=> insert into vendas (id, 

                              funcionario_id,
                              mesa_id,
                              venda_codigo,
                              venda_valor,
                              venda_total,
                              venda_desconto,
                              venda_situacao,
                              data_criacao,
                              data_atualizacao)
                       values (10001,
                               1,
                               1,
                               '10201',
                               '20',
                               '20',
                               '0',
                               'A',
                               '01/01/2016',
                               '01/01/2016');

postgres=> insert into itens_vendas (produto_id,

                                    vendas_id,
                                    item_valor,
                                    item_quantidade,
                                    item_total,
                                    data_criacao,
                                    data_atualizacao)
                            values (1,
                                    10001,
                                    10,
                                    2,
                                    20,
                                    '01/01/2016',
                                    '01/01/2016');  

postgres=> insert into vendas (id, 

5.7 FUNÇÕES AGREGADORAS 
**93**


--------------------------------------------------

                              funcionario_id,
                              mesa_id,
                              venda_codigo,
                              venda_valor,
                              venda_total,
                              venda_desconto,
                              venda_situacao,
                              data_criacao,
                              data_atualizacao)
                       values (10002,
                               1,
                               1,
                               '10002',
                               '45',
                               '45',
                               '0',
                               'A',
                               '01/01/2016',
                               '01/01/2016');

postgres=> insert into itens_vendas (produto_id,

                                    vendas_id,
                                    item_valor,
                                    item_quantidade,
                                    item_total,
                                    data_criacao,
                                    data_atualizacao)
                            values (4,
                                    10002,
                                    15,
                                    3,
                                    45,
                                    '01/01/2016',
                                    '01/01/2016');

Agora que temos vários registros, montaremos a consulta.
Vamos buscar os produtos e somar o total vendido de cada item.
Conseguiremos fazer isso se agruparmos todos os registros iguais no
campo  produto_id . Por isso, vamos utilizar a função de
agrupamento.

postgres=# select produto_id , sum(iten_total)

            from itens_vendas
           group by produto_id;

Como resultado da nossa consulta, temos:

**94** 
5.7 FUNÇÕES AGREGADORAS


--------------------------------------------------

Figura 5.14: Valor vendido de cada produto

Não ficou muito legal a apresentação, pois só temos o  id  de
cada produto. Vamos utilizar um recurso que já aprendemos para
mostrar o nome do produto. Logo, criaremos uma função que busca
o seu nome. Mãos no teclado e vamos colocar em prática um
recurso já aprendido.

postgres=# create or replace function 

           retorna_nome_produto(prod_id int) 
           returns text as 
           $$              
           declare 
           nome     text;   
           begin
             select produto_nome                     
               into nome
               from produtos
              where id = prod_id;                
                return nome;
           end
           $$ 
           language plpgsql;

Agora que temos uma função que retorna o nome do produto,
vamos reescrever a consulta que fizemos com os totais de cada
produto vendido.

postgres=# select retorna_nome_produto(produto_id) , sum(iten_tota
l)

            from itens_vendas
           group by produto_id;

5.7 FUNÇÕES AGREGADORAS 
**95**


--------------------------------------------------

Figura 5.15: Valor vendido de cada produto e uma function para retornar o nome do produto

Muito melhor, não é mesmo? Agora conseguimos saber qual
produto está listado. Mas ainda podemos melhor um pouco mais
nossa consulta.

Vamos ordenar o nosso resultado e apelidar as colunas. Ficou
meio bagunçada essa última consulta, pois, se você ver o nome da
coluna no seu resultado, o nome é  sum . Se você estivesse vendo
pela primeira vez esse resultado, você não saberia dizer do que se
trata. Então, vamos melhorar o nosso código.

postgres=# select retorna_nome_produto(produto_id) PRODUTO, 

                 sum(item_total) VL_TOTAL_PRODUTO
            from itens_vendas
           group by produto_id
           order by vl_total_produto, produto;

Figura 5.16: Valor vendido de cada produto, uma function para retornar o nome do produto e
ordenado e apelidado

Observe como conseguimos evoluir o nosso código. Para você

**96** 
5.7 FUNÇÕES AGREGADORAS


--------------------------------------------------

apelidar uma coluna, basta colocar um nome qualquer na frente
dela. Quando você executar a consulta, o que será apresentado
como resultado é o seu apelido.

A ordenação é feita usando o comando  order by . Na consulta,
informamos que gostaríamos que o resultado fosse ordenado
primeiro pelo campo  vl_total_produto , e depois pela coluna

 produto . Por padrão, o PostgreSQL ordena de forma ascendente.
Poderíamos ter solicitado uma ordenação de forma descendente. O
código ficaria da seguinte maneira:

postgres=# select retorna_nome_produto(produto_id) PRODUTO, 

                 sum(item_total) VL_TOTAL_PRODUTO
            from itens_vendas
           group by produto_id
           order by vl_total_produto desc, produto;

Para trabalhar juntamente com a cláusula  group by() , temos
o  having count() , que vai eliminar as linhas de um agrupamento
que você não deseja que seja exibido. Vamos supor que surgiu a
necessidade de extrairmos de nossos projetos a quantidade vendida
de cada produto. Utilizando somente o  group by() , podemos
fazer uma consulta que nos retornará o nome do produto e contará
quantas vezes ele foi vendido. Mãos no teclado e vamos criar a
seguinte consulta:

postgres=#   select retorna_nome_produto(produto_id), 

                   count(id) QTDE
              from itens_vendas
             group by produto_id;

Como resultado, teremos:

5.7 FUNÇÕES AGREGADORAS 
**97**


--------------------------------------------------

Figura 5.17: Número de vendas por produto

Agora que sabemos a quantidade vendida de cada produto,
vamos filtrar nela apenas os produtos que tiveram vendas iguais ou
superiores a 2. Agora que entra a cláusula  having count() . Como
usamos o  count()  anteriormente para contar os itens, vamos
utilizar o  having count()  em nossa consulta para indicar que
queremos apenas os produtos que possuam contagem maior ou
igual a 2, e ordenar pela quantidade contada. Vamos ao nosso
código.

postgres=#   select retorna_nome_produto(produto_id) produto, 

                   count(id) qtde
              from itens_vendas
             group by produto_id
            having count(produto_id) >= 2
             order by qtde;

E como resultado de nossa consulta, teremos:

Figura 5.18: Having count como forma de filtrar as linhas apresentadas

**98** 
5.7 FUNÇÕES AGREGADORAS


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------

postgres=> insert into funcionarios(funcionario_codigo,
                                    funcionario_nome,
                                    funcionario_situacao,
                                    funcionario_comissao,
                                    funcionario_cargo,
                                    data_criacao)
                             values('0101',
                                    'VINICIUS SOUZA MOLIN',
                                    'A',
                                     2,
                                    'GARÇOM',
                                    '01/03/2016');

postgres=> insert into funcionarios(funcionario_codigo,
                                    funcionario_nome,
                                    funcionario_situacao,
                                    funcionario_comissao,
                                    funcionario_cargo,
                                    data_criacao)
                             values('0102',
                                    'VINICIUS RANKEL C',
                                    'A',
                                     2,
                                    'GARÇOM',
                                    '01/03/2016');

postgres=> insert into funcionarios(funcionario_codigo,
                                    funcionario_nome,
                                    funcionario_situacao,
                                    funcionario_comissao,
                                    funcionario_cargo,
                                    data_criacao)
                             values('0103',
                                    'BATISTA SOUZA LUIZ',
                                    'A',
                                     2,
                                    'GARÇOM',
                                    '01/03/2016');

postgres=> insert into funcionarios(funcionario_codigo,
                                    funcionario_nome,
                                    funcionario_situacao,
                                    funcionario_comissao,
                                    funcionario_cargo,

5.8 CONSULTAS UTILIZANDO LIKE 
**101**


--------------------------------------------------

                                   data_criacao)
                            values('0104',
                                   'ALBERTO SOUZA CARDOSO',
                                   'A',
                                    2,
                                   'GARÇOM',
                                   '01/03/2016');

postgres=> insert into funcionarios(funcionario_codigo,

                                   funcionario_nome,
                                   funcionario_situacao,
                                   funcionario_comissao,
                                   funcionario_cargo,
                                   data_criacao)
                            values('0105',
                                   'CARLOS GABRIEL ALMEIDA',
                                   'A',
                                    2,
                                   'GARÇOM',
                                   '01/03/2016');

postgres=> insert into funcionarios(funcionario_codigo,

                                   funcionario_nome,
                                   funcionario_situacao,
                                   funcionario_comissao,
                                   funcionario_cargo,
                                   data_criacao)
                            values('0106',
                                   'RENAN SIMOES SOUZA',
                                   'A',
                                    2,
                                   'GARÇOM',
                                   '01/03/2016');

Se você não inseriu nenhum outro registro no banco, apenas os
exemplos 
que 
estão 
no 
livro, 
caso 
consulte 
o 
campo

funcionario_nome na tabela de funcionários, o resultado será:

**102** 
5.8 CONSULTAS UTILIZANDO LIKE


--------------------------------------------------

Figura 5.19: Consultando com like

Agora imagine se tivéssemos uma lista com mais de mil nomes
de funcionários e quiséssemos consultar apenas aqueles cujo
primeiro nome seja igual a  VINICIUS . Seria um trabalho grande
selecionar todos e procurar os códigos desses registros.

Com o  like , podemos criar uma consulta que buscará todos
os registros que iniciam com  VINICIUS  e não levará em
consideração a continuação do nome. Mãos no teclado e vamos ao
nosso código.

postgresql=# select funcionario_nome
               from funcionarios
              where funcionario_nome like 'VINICIUS%';

Veja no resultado a seguir que o banco trouxe todos os registros
que iniciavam com  VINICIUS , ignorando todo o restante do nome
em cada registro. Isso ocorreu porque, no final da  string ,
inserimos o caractere  % . Quando não sabemos uma parte da

 string , usamos esse caractere para dizer para o banco de dados
que não sabemos o que está escrito depois dele e que é para ele
buscar todos os resultados.

5.8 CONSULTAS UTILIZANDO LIKE 
**103**


--------------------------------------------------

Figura 5.20: Resultado da consulta com like

Também podem ocorrer situações em que não sabemos onde o
termo que queremos consultar se encontra. Vamos supor que
precisamos consultar todos os nomes que possuem a palavra

 SOUZA . Não sabemos se está no início, no meio ou no final do
nome. Apenas sabemos que há nomes que contêm a palavra

 SOUZA . Novamente, usaremos o sinal  % , só que agora vamos
colocar duas vezes. Vamos ao nosso código.

postgresql=# select funcionario_nome

              from funcionarios
             where funcionario_nome like '%SOUZA%';

Figura 5.21: Consultando com like no meio

Nessa última consulta, não sabíamos onde a palavra ou o termo
se encontrava. Apenas sabíamos que existia em algum lugar. Foi isso

**104** 
5.8 CONSULTAS UTILIZANDO LIKE


--------------------------------------------------

que fizemos, instruímos o banco de dados para buscar todos os
registros que continham a palavra  SOUZA .

Diferentemente do  like , quando usamos o sinal de  = , temos
de saber com exatidão o conteúdo do campo. Se não, o banco de
dados não vai encontrar resultados na consulta. Você pode até
tentar utilizar o sinal  %  com o sinal de igual, só que não terá
resultado. Faça a consulta:

postgresql=# select funcionario_nome

              from funcionarios
             where funcionario_nome = 'VINICIUS%';

Verá que não trará nenhum registro. Agora utilize a seguinte
consulta:

postgresql=# select funcionario_nome

              from funcionarios
             where funcionario_nome = 'VINICIUS SOUZA';

Agora deu certo, pois informamos com exatidão a  string  que
o banco deveria procurar. Também não é obrigatório usar o sinal

%  nas consultas com o  like . Você pode utilizá-lo da mesma
maneira que o sinal  = .

Conseguimos produzir muitas linhas de código neste capítulo, e
o mais legal foi que, em algumas partes, conseguimos inserir
assuntos e recursos que aprendemos nos capítulos anteriores. É
assim que vamos fixando os assuntos aprendidos. Pegue essas
funções que aprendemos e tente aplicar nas outras tabelas que
foram criadas no banco de dados. Crie vários outros registros, se
necessário.

Lembra dos nossos processos que fazem alguns cálculos? E se
pudéssemos executá-los a partir de ações que acontecem em nosso

## 5.9 PARA PENSAR!

5.9 PARA PENSAR! 
**105**


--------------------------------------------------

banco de dados de uma forma automática? Seria muito legal, certo?
É exatamente isso que nos espera no próximo capítulo. Vá tomar
um café e, em seguida, vire a página e vamos para o próximo
capítulo!

**106** 
5.9 PARA PENSAR!


--------------------------------------------------

CAPÍTULO 6

"Nós somos aquilo que fazemos com frequência. Excelência,
então, não é um ato, mas um hábito". — Aristóteles

Segundo a documentação oficial do PostgreSQL 9.4, uma trigger
é uma instrução ao banco de dados que deve automaticamente
executar uma função específica quando uma operação específica for
feita. Elas podem ser para tabelas, views e chaves estrangeiras.

Podemos dizer que triggers, ou gatilhos, são procedimentos
armazenados no banco de dados, que utilizamos para disparar ações
automaticamente ou realizar uma tarefa automática, como por
exemplo, gravar  logs de alterações de uma tabela. Podemos pedir
para o banco de dados gravar em uma tabela de logs todas as
alterações que houver em determinada tabela.

Vamos imaginar uma máquina de lavar roupa, dessas
automáticas que lavam, enxaguam e secam. Você apenas a
programa uma vez e ela faz uma operação assim que a outra
termina. É exatamente assim que as  triggers  funcionam:
disparam automaticamente uma função quando uma outra termina.

# BANCO DE DADOS RÁPIDO
# NOS GATILHOS

## 6.1 TRIGGERS — GATILHOS PARA AGILIZAR
## TAREFAS

6 BANCO DE DADOS RÁPIDO NOS GATILHOS 
**107**


--------------------------------------------------

Existem três eventos em que usamos as triggers: de inserção
(insert), na alteração (update) e na exclusão de registros (delete).
Cada um desses eventos pode ocorrer em dois momentos: antes da
execução do evento (before) ou depois da execução do evento
(after). Algo muito legal é que podemos incluir mais de um
momento para executar uma trigger. Isso facilita para não termos de
repetir o mesmo código várias vezes.

Imagine o cenário do cálculo da comissão do vendedor. A
trigger dispararia no evento insert, ao inserir o registro de venda, e
depois (after) do registro da venda ter sido inserido. Simples, não é
mesmo? Se ficar na dúvida, lembre-se de que, para inserir a trigger,
você precisa escolher em qual evento ela vai disparar e em que
momento deve acontecer.

Se ainda está com dúvida, não se preocupe. Vamos exemplificar
cada evento e todos os momentos que podemos usar os gatilhos.
Para isso, usaremos como base as tabelas que criamos e os registros
que inserimos. Vamos criar cenários reais, tudo baseado em nosso
projeto.

Vamos criar uma  trigger  que disparará uma função que vai
gravar os registros que estão sendo alterados. Vamos pedir para
armazenar o registro antigo e os novos.

Para isso, precisaremos criar alguns objetos que aprendemos
anteriormente. Criaremos uma tabela para armazenar os logs da
tabela de produtos. Nela, vamos incluir todos os mesmos campos da
tabela de produtos duas vezes, pois na mesma linha gravaremos o
valor antigo do campo e o novo valor. Além da tabela, vamos
precisar criar uma função que vai fazer o processo de inserção dos
registros nesta nova tabela. Diferente dos tipos de funções que já

## 6.2 TRIGGERS: INSERT, UPDATE E DELETE

**108** 
6.2 TRIGGERS: INSERT, UPDATE E DELETE


--------------------------------------------------

criamos, esta terá o retorno do tipo trigger.

Em PostgreSQL, um gatilho (trigger) pode executar qualquer
função definida pelo usuário em uma de suas linguagens
procedurais Java, C, Perl, Python ou TCL, além de por meio da
linguagem SQL. Em MySQL, gatilhos são ativados por comandos
SQL, mas não por APIs, já que estas não transmitem comandos SQL
ao servidor MySQL.

A nossa  trigger  vai se chamar  tri_log_produtos  e será
disparada após haver uma inserção, uma alteração ou exclusão de
registro na tabela  produtos . Então, mãos no teclado e vamos ao
código.

Primeiro, vamos criar a nossa tabela. A tabela se chamará

 logs_produtos . Nos campos em que serão armazenados os
valores antigos, vamos colocar um sufixo  _old ao final do nome. E
para os campos nos quais serão armazenados os valores novos,
colocaremos o sufixo  _new  ao final do nome. Esta é uma
convenção que eu, particularmente, gosto de usar. Você pode criar a
sua. :)

Vou criar uma coluna em nossa tabela chamada  alteracao 
que vai armazenar o tipo de operação que foi feita na tabela, ou seja,
gravará se foi uma inserção, uma alteração ou exclusão de registros.
Isso é possível pois, durante a execução da  function  que retorna
um tipo trigger, cria variáveis na memória que armazena os valores
antigos e novos, além de armazenar o tipo da operação executada.

A variável que vai nos retornar o tipo da ação é a  TG_OP , e os
valores antigos e novos são as variáveis  old.nome_coluna  e

 new.nome_coluna , respectivamente.

postgres=> create table logs_produtos(

            id                    int not null primary key, 
            data_alteracao        timestamp,
            alteracao             varchar(10),

6.2 TRIGGERS: INSERT, UPDATE E DELETE 
**109**


--------------------------------------------------

            id_old                int,
            produto_codigo_old    varchar(20),
            produto_nome_old      varchar(60),
            produto_valor_old     real,
            produto_situacao_old  varchar(1) default 'A',
            data_criacao_old      timestamp,
            data_atualizacao_old  timestamp,
            id_new                int,
            produto_codigo_new    varchar(20),
            produto_nome_new      varchar(60),
            produto_valor_new     real,
            produto_situacao_new  varchar(1) default 'A',
            data_criacao_new      timestamp,
            data_atualizacao_new  timestamp );

Vamos criar uma  sequence para a nossa tabela de logs.

postgres=> create sequence logs_produto_id_seq;

Agora vamos vincular a  sequence  à coluna  id  da tabela

 logs_produtos .

postgres=> alter table logs_produtos 

          alter column id set default 
          nextval('logs_produto_id_seq');

Pronto! A tabela está pronta para receber os logs de alterações
da tabela  produtos . Vamos agora criar a função e o nosso gatilho.

Primeiro, vamos criar a function. Mas antes devemos fazer uma
análise da situação. Nós usaremos a mesma trigger para o  insert ,

 update  e  delete , correto? Sim. E queremos armazenar o valor
antigo do campo e o valor novo. Mas se analisarmos, nós temos o
valor anterior e o novo para um determinado campo, por exemplo,
quando fazemos um  update , pois, se vamos inserir um registro,
não temos um valor antigo, apenas o novo. E se fizermos um

 delete , não teremos um valor novo, apenas o antigo, já que o
registro deixa de existir.

Pois bem, pensando nisso, vamos fazer um tratamento
utilizando os condicionais que aprendemos, o  if  e o  else . Se
não fizermos o tratamento ao consultar as variáveis criadas em

**110** 
6.2 TRIGGERS: INSERT, UPDATE E DELETE


--------------------------------------------------

tempo de execução, o SGBD não encontrará registro e ocorrerá um
erro, dizendo que a variável não possui valor. Mãos no teclado e
vamos ao código.

create or replace function gera_log_produtos() 
returns trigger as

$$

Begin

 if TG_OP = 'INSERT' then 

   insert into logs_produtos (              
              alteracao
             ,data_alteracao
             ,id_new
             ,produto_codigo_new   
             ,produto_nome_new     
             ,produto_valor_new    
             ,produto_situacao_new 
             ,data_criacao_new     
             ,data_atualizacao_new
            ) 

      values (
               TG_OP 
              ,now()
             ,new.id
             ,new.produto_codigo   
             ,new.produto_nome     
             ,new.produto_valor    
             ,new.produto_situacao 
             ,new.data_criacao     
             ,new.data_atualizacao 

              );
        return new;

 elsif TG_OP = 'UPDATE' then

     insert into logs_produtos (              
                  alteracao
                 ,data_alteracao
                 ,id_old
                  ,produto_codigo_old   

6.2 TRIGGERS: INSERT, UPDATE E DELETE 
**111**


--------------------------------------------------

                  ,produto_nome_old     
                  ,produto_valor_old    
                  ,produto_situacao_old 
                  ,data_criacao_old     
                  ,data_atualizacao_old 
                  ,id_new
                  ,produto_codigo_new   
                  ,produto_nome_new     
                  ,produto_valor_new    
                  ,produto_situacao_new 
                  ,data_criacao_new     
                  ,data_atualizacao_new
                 ) 

           values (
                    TG_OP 
                   ,now()
                   ,old.id
                  ,old.produto_codigo  
                  ,old.produto_nome    
                  ,old.produto_valor   
                  ,old.produto_situacao
                  ,old.data_criacao    
                  ,old.data_atualizacao
                  ,new.id
                  ,new.produto_codigo   
                  ,new.produto_nome     
                  ,new.produto_valor    
                  ,new.produto_situacao 
                  ,new.data_criacao     
                  ,new.data_atualizacao 

                   );
             return new;

    elsif TG_OP = 'DELETE' then 

      insert into logs_produtos (              
                   alteracao
                  ,data_alteracao
                  ,id_old
                   ,produto_codigo_old   
                  ,produto_nome_old     
                  ,produto_valor_old    
                  ,produto_situacao_old 
                  ,data_criacao_old     
                  ,data_atualizacao_old 
                 ) 

**112** 
6.2 TRIGGERS: INSERT, UPDATE E DELETE


--------------------------------------------------

          values (
                   TG_OP 
                  ,now()
                  ,old.id
                 ,old.produto_codigo  
                 ,old.produto_nome    
                 ,old.produto_valor   
                 ,old.produto_situacao
                 ,old.data_criacao    
                 ,old.data_atualizacao

                  );
            return new;

   end if;    

end;

$$ language 'plpgsql';

Com esta function, o banco de dados vai verificar a operação
que foi executada e, com isso, fazer o  insert  na tabela de log,
inserindo a operação que foi executada. E agora finalmente,
criaremos a  trigger .

postgres=>  create trigger tri_log_produtos

           after insert or update or delete on produtos
           for each row execute 
           procedure gera_log_produtos();

Para sabermos que a trigger está criada corretamente na tabela
que desejamos, podemos listar os objetos dessa tabela usando o
comando  \d nome_tabela .

postgres=> \d produtos;

6.2 TRIGGERS: INSERT, UPDATE E DELETE 
**113**


--------------------------------------------------

Figura 6.1: Os itens da tabela de produtos

Agora que criamos todo o fluxo para gravarmos os logs da tabela
produtos, vamos realizar alterações nela que possibilitem a
visualização dos registros nessa nova tabela. Vamos inserir três
novos produtos. Fiquem à vontade para criar quantos registros você
quiser. Quanto mais, melhor!

postgres=> insert into produtos (produto_codigo,

                                produto_nome,
                                produto_valor,
                                produto_situacao,
                                data_criacao,
                                data_atualizacao)
                        values ('1512',
                                'LAZANHA',
                                46,
                                'A',
                                '01/01/2016',
                                '01/01/2016');

postgres=> insert into produtos (produto_codigo,

                                produto_nome,
                                produto_valor,
                                produto_situacao,
                                data_criacao,
                                data_atualizacao)
                        values ('1613',
                                'PANQUECA',
                                38,
                                'A',
                                '01/01/2016',
                                '01/01/2016');

postgres=> insert into produtos (produto_codigo,

                                produto_nome,

**114** 
6.2 TRIGGERS: INSERT, UPDATE E DELETE


--------------------------------------------------

                                produto_valor,
                                produto_situacao,
                                data_criacao,
                                data_atualizacao)
                        values ('733',
                                'CHURRASCO',
                                72,
                                'A',
                                '01/01/2016',
                                '01/01/2016');

A inserção de dados na tabela produtos já deve ter gerado logs
nela. Vamos verificar. Como sabemos as colunas que tiveram
inserção de dados, vamos consultar apenas elas.

postgres=> 

       select alteracao
             ,data_alteracao
             ,id_new
             ,produto_codigo_new   
             ,produto_nome_new     
             ,produto_valor_new    
             ,produto_situacao_new 
             ,data_criacao_new     
             ,data_atualizacao_new 
        from logs_produtos;

Figura 6.2: Os primeiros logs

Observe que o campo  alteracao  gravou corretamente o tipo
da operação que realizamos, um  insert  na tabela. Mas agora
vamos fazer uma alteração na tabela  produtos , e atualizar o preço
do  'CHURRASCO' .

postgres=> 

     update produtos set produto_valor = 99
      where produto_nome = 'CHURRASCO';

6.2 TRIGGERS: INSERT, UPDATE E DELETE 
**115**


--------------------------------------------------

Como sabemos que o  update realiza uma inserção em todos os
campos da tabela de logs, vamos realizar uma consulta completa na
tabela.

postgres=> select * 

            from logs_produtos;

Figura 6.3: Logs de inserção (insert) e alteração (update)

Agora que fizemos o  insert  e o  update , só nos restou
deletar um registro para visualizarmos como ficará os logs da tabela
de produtos. Logo, deletaremos a  'PANQUECA' do nosso sistema.

postgres=> delete from produtos where produto_nome = 'PANQUECA';

Executando a mesma consulta:

postgres=> select * 

            from logs_produtos;

Figura 6.4: Logs de inserção (insert), alteração (update) e exclusão (delete)

A partir de agora, todas as alterações realizadas na tabela de
produtos serão gravadas nesta tabela de logs. Existem muitos outros

**116** 
6.2 TRIGGERS: INSERT, UPDATE E DELETE


--------------------------------------------------

modelos para armazenar logs de uma tabela. Este pode não ser o
mais elegante, mas para iniciarmos um projeto já é o suficiente.

Se utilizarmos o comando  truncate  para excluir os registros
de uma tabela, ele não vai disparar as  triggers que estiverem
configuradas para disparar  on delete , pois o  truncate 
ignora qualquer  trigger .

As regras de sistemas estão sempre mudando, e nós sempre
devemos nos adequar a elas. É muito comum, por mudança de regra
ou até por uma necessidade de manutenção do sistema, surgir a
necessidade de não usar uma  trigger  por um período sem
precisarmos excluí-la. Por isso, temos as possibilidades de
desabilitar e habilitar uma trigger, além de deletá-la.

Vamos desabilitar a trigger que criamos:

postgres=> alter table produtos 

          disable trigger tri_log_produtos;

Vamos inserir um registro em nossa tabela para verificar se a
trigger está realmente desabilitada.

postgres=> insert into produtos (produto_codigo,

                                produto_nome,
                                produto_valor,
                                produto_situacao,
                                data_criacao,
                                data_atualizacao)
                        values ('912',
                                'SORVETE',
                                 6,
                                'A',

## 6.3 
## DESABILITANDO, 
## HABILITANDO 
## E
## DELETANDO UMA TRIGGER

6.3 DESABILITANDO, HABILITANDO E DELETANDO UMA TRIGGER 
**117**


--------------------------------------------------

                                '01/01/2016',
                                '01/01/2016');

Agora se consultarmos a nossa tabela de logs, verificaremos que
não houve inserção de registros na tabela de produtos.

postgres=> select * 

            from logs_produtos;

Figura 6.5: O banco não registrou a inserção, pois a trigger está desabilitada

Muito cuidado ao deixar uma trigger desabilitada, porque, se ela
for importante, como por exemplo, salva o log de uma determinada
tabela, podemos perder o rastreamento das alterações.

Agora vamos habilitar a trigger novamente:

postgres=> alter table produtos 

          enable trigger tri_log_produtos;

Vamos alterar o preço do  'SORVETE' .

postgres=> update produtos set produto_valor = 10

           where produto_nome = 'SORVETE';

Consultando novamente:

postgres=> select * 

            from logs_produtos;

**118** 
6.3 DESABILITANDO, HABILITANDO E DELETANDO UMA TRIGGER


--------------------------------------------------

Figura 6.6: Trigger voltando a gravar as alterações

E nossa trigger voltou a funcionar. Agora se você desejar
realmente deletar a trigger, você pode usar o seguinte comando:

postgres=> drop trigger tri_log_produtos on produtos;

Se verificarmos os itens da tabela, veremos que ela não consta
mais.

postgres=> \d produtos

Figura 6.7: Ausencia da trigger

Para excluir uma trigger, tenha certeza de que ela não será mais
necessária, uma vez que a exclusão pode prejudicar processos, tanto
simples, como a gravação de logs, ou até mesmo cálculos que são
executados por esses gatilhos. Por exemplo, imagine que você tem
uma  trigger  que grava os logs de todas transações do banco de
dados. Se você a excluir, o processo vai parar de ser executado e,
consequentemente, os logs vão parar de ser armazenados.

6.3 DESABILITANDO, HABILITANDO E DELETANDO UMA TRIGGER 
**119**


--------------------------------------------------

Logs são muito importantes para um sistema, principalmente
para segurança, já que é uma das maneiras de saber quem alterou
algo no sistema, e até mesmo uma maneira para restaurar registros
deletados indevidamente. Você agora pode criar uma tabela de log
para cada tabela que criamos em nosso projeto. Uma maneira para
você colocar em prática o que aprendeu neste capítulo.

Além de logs, é possível automatizar outros processos no
sistema, mas isso vai da sua imaginação. Poderíamos, por exemplo,
criar uma trigger faça os cálculos de comissão dos vendedores, após
a inserção de um registro. Podemos também criar triggers para
validação de informações que estão sendo inseridas utilizando as
variáveis criadas em tempo de execução.

Agora você já sabe criar e deletar triggers. Delete as que criamos
e tente criá-las sem olhar o código que fizemos. No começo, pode
colar um pouco, mas só um pouco! ;)

Os gatilhos nos ajudam bastante, pois disparam processos
automaticamente após eventos que ocorrem em determinada tabela.
Já conseguimos fazer diversas coisas no banco de dados. Mas até
agora, criamos apenas consultas simples. Já está na hora de criarmos
algumas consultas mais complexas. #PartiuPróximoCapítulo

## 6.4 PARA PENSAR!

**120** 
6.4 PARA PENSAR!


--------------------------------------------------

CAPÍTULO 7

"Eu sempre fiz alguma coisa para a qual eu não estava muito
pronta. Acho que é assim que você cresce. Quando há aquele
momento de 'Uau, eu não tenho tanta certeza de que posso fazer isso',
e aí você insiste nesses momentos; é aí que você tem um progresso". —
Marissa Mayer

Existem algumas formas de se fazer consultas para extrair dados
de uma ou mais consultas, seja por meio de consultas simples ou de
funções que retornam dados. Entretanto, muitas vezes, precisamos
criar ligações entre as tabelas em forma de dependência.

Por exemplo, se quisermos criar um  select  para consultar os
funcionários relacionados com uma ou mais vendas. Neste caso, já
saberíamos criar as duas consultas: uma para buscar os funcionários
e outra para buscar as vendas. Mas com essas duas consultas
separadas não conseguimos extrair valor para o nosso projeto, uma
vez que precisaríamos colocar o resultado delas em uma planilha, a
fim de fazer algum relacionamento. E isto está fora de cogitação! :)

Uma maneira para relacionar duas tabelas é por meio de uma

# TURBINANDO AS
# CONSULTAS COM JOINS E
# VIEWS

## 7.1 SUBCONSULTAS

7 TURBINANDO AS CONSULTAS COM JOINS E VIEWS 
**121**


--------------------------------------------------

subconsulta, na qual buscaremos os funcionários que possuem
vínculo com uma ou mais vendas.

postgres=# select funcionario_nome

            from funcionarios
           where id in (select funcionario_id
                          from vendas);

Figura 7.1: Consulta com subconsulta

As subconsultas são úteis em diversas situações, no entanto, não
são tão performáticas, uma vez que se não passarmos um parâmetro
para ela, ela faz uma busca completa na subtabela para passar um
parâmetro para a consulta externa, fazendo com que a consulta seja
lenta. Isso foi mostrado no exemplo, no qual não foi passado um
parâmetro para a subconsulta e o banco teve de realizar uma busca
em toda a tabela de vendas para retornar os funcionários.

Poderíamos realizar a mesma consulta apenas buscando as
vendas realizadas em 2016. Assim restringiríamos um pouco a busca
e melhoraríamos a sua performance, ainda não com o cenário ideal.
Vamos utilizar uma função ensinada neste livro para extrair apenas
o ano da data atual e passar como parâmetro.

postgres=# select funcionario_nome

            from funcionarios
           where id in (select funcionario_id
                          from vendas
                         where date_part('year', data_criacao) = 
'2016');

**122** 
7.1 SUBCONSULTAS


--------------------------------------------------

Figura 7.2: Consulta com subconsulta e parâmetros

Observe que trouxe alguns funcionários repetidos como
resultado. Isso acontece pois estamos retornando cada venda que o
funcionário teve, e pedindo para selecionar o nome dele. Como o
nosso interesse é apenas exibir o nome dos funcionários, podemos
pedir para o banco exibir os nomes distintos. Fazemos isso usando o

 DISTINCT  antes da coluna que estamos selecionando. Além disso,
vamos ordenar em ordem alfabética; isso é fácil, pois já aprendemos.

postgres=# select distinct funcionario_nome

            from funcionarios
           where id in (select funcionario_id
                          from vendas)
           order by funcionario_nome;

Figura 7.3: Consulta com subconsulta agrupando registros sem repetição

Uma maneira mais performática para realizar o relacionamento
entre tabelas é pelas  joins , ou no bom e velho português, junções.

## 7.2 CONSULTAS ENTRE DUAS OU MAIS
## TABELAS ATRAVÉS DAS JOINS

7.2 CONSULTAS ENTRE DUAS OU MAIS TABELAS ATRAVÉS DAS JOINS 
**123**


--------------------------------------------------

Criando  joins , não precisamos realizar subconsultas e fazer o
relacionamento direto entre as tabelas. Vamos recriar a mesma
consulta, mas desta vez usaremos uma  join para construí-la.

postgres=# select distinct funcionario_nome

            from funcionarios, vendas
           where funcionarios.id = vendas.funcionario_id
           order by funcionario_nome;

Figura 7.4: Consulta com join

Veja 
que 
fizemos 
uma 
consulta 
em 
duas 
tabelas
simultaneamente, e instruímos ao banco para comparar o  id  do
funcionário de ambas as tabelas da consulta. Fazemos isso para
manter a integridade das buscas, uma vez que, se não fizermos esse
relacionamento, o SGBD se perde. Vamos fazer a seguinte consulta:

postgres=# select distinct funcionario_nome

            from funcionarios, vendas  
           order by funcionario_nome;

**124** 
7.2 CONSULTAS ENTRE DUAS OU MAIS TABELAS ATRAVÉS DAS JOINS


--------------------------------------------------

Figura 7.5: Consulta com join distinguindo os registros e os ordenando

Quando houver relacionamento entre tabelas, não podemos
esquecer a igualdade entre os campos que as relacionam.

Esta é a forma mais popular para se escrever uma  join , e o
jeito mais simples para ler as consultas. Eu, particularmente, prefiro
escrevê-las desta maneira. Você verá nos exemplos a seguir como
escrever  joins  de maneiras mais tradicionais. Ambos os jeitos
estão corretos.

Alguns dizem que, da maneira tradicional, há um ganho de
performance. Mas muitos autores divergem a respeito disso. E se
houver ganho de performance, este ganho será mínimo. Como eu
sempre comento sobre programação, cada um deve avaliar o
contexto em que está trabalhando e escolher a maneira que melhor
se encaixa.

**### Inner join**

7.2 CONSULTAS ENTRE DUAS OU MAIS TABELAS ATRAVÉS DAS JOINS 
**125**


--------------------------------------------------

Utilizando a sintaxe  inner join , teremos a mesma consulta
realizada anteriormente, com a diferença no modo de sua escrita.
Vamos repetir a última consulta, só que desta vez usando a sintaxe
do  inner join .

postgres=# select distinct funcionario_nome 

            from funcionarios 
           inner join vendas 
              on (funcionarios.id = vendas.funcionario_id)
           order by funcionario_nome;

Figura 7.6: Consulta utilizando inner join

Observe que obtivemos o mesmo resultado. Tivemos uma
diferença apenas na sintaxe, e podemos simplificar ainda mais.
Podemos escrever apenas  join , que teremos o mesmo resultado.

postgres=# select distinct funcionario_nome

            from funcionarios
            join vendas
              on (funcionarios.id = vendas.funcionario_id)
           order by funcionario_nome;

Figura 7.7: Consulta utilizando join

As duas maneiras estão corretas e correspondem à mesma

**126** 
7.2 CONSULTAS ENTRE DUAS OU MAIS TABELAS ATRAVÉS DAS JOINS


--------------------------------------------------

consulta. Apenas teremos diferença no resultado quando utilizamos
o  outer join , que veremos a seguir.

Diferentemente do  inner join , o  outer join  possui dois
tipos. Temos o  left outer join  e o  right outer join . Em
ambos os casos, o SGBD vai retornar todos os campos da tabela à
esquerda (quanto utilizado o  left outer join ), ou da tabela à
direita (quando usado o  right outer join ).

**Left outer join ou left join**

Utilizando o  left outer join , o SGBD realizará uma junção
interna e, para cada linha listada da primeira tabela que não
satisfizer a condição de relacionamento com a segunda tabela, vai
ser adicionada uma linha juntada com valores nulos nas colunas da
segunda tabela. Com isso, o resultado de nossa consulta possuirá, no
mínimo, uma linha para cada linha da primeira tabela.

Vamos criar uma consulta baseada na usada anteriormente, que
vai ficar mais claro para visualizarmos este cenário.

postgres=# select funcionario_nome, v.id

            from funcionarios f
            left join vendas v
              on f.id = v.funcionario_id
           order by funcionario_nome desc;

**### Outer join**

7.2 CONSULTAS ENTRE DUAS OU MAIS TABELAS ATRAVÉS DAS JOINS 
**127**


--------------------------------------------------

Figura 7.8: Consulta utilizando left outer join ou left join

Analisando o resultado de nossa consulta, podemos observar
que ela trouxe todos os registros da tabela  funcionario  para as
linhas que satisfazem a igualdade, e trouxe o valor na coluna  v.id ,
que é o identificador da venda. E para os funcionários que não
possuem nenhum registro na tabela  vendas , a consulta trouxe em
branco.

**Right outer join ou right join**

Agora vamos fazer o contrário e buscar as vendas fazendo uma
junção externa com a tabela de funcionários. O SGBD vai utilizar o
mesmo critério para apresentar a busca, só que desta vez buscará
todas as vendas e verificará qual possui vínculo com o funcionário.

postgres=# select v.id, v.venda_total, funcionario_nome

            from vendas v

**128** 
7.2 CONSULTAS ENTRE DUAS OU MAIS TABELAS ATRAVÉS DAS JOINS


--------------------------------------------------

           right join funcionarios f
              on v.funcionario_id = f.id
           order by v.venda_total;

Figura 7.9: Consulta utilizando right outer join ou right join

Se você ainda não trabalha com programação, não se preocupe
em decorar cada um deles, pois você acaba absorvendo a construção
das consultas de forma natural. E por mais que tenha todos esses
tipos de  joins , acabamos utilizando mais a primeira forma de
escrita, uma vez que a leitura das consultas fica mais simples e
consegue-se o mesmo resultado que com os outros tipos de junções.

Você percebeu como pode ser comum fazermos uma mesma
consulta diversas vezes? Pois pense como o cliente que está

## 7.3 VIEWS

7.3 VIEWS 
**129**


--------------------------------------------------

contratando você para desenvolver o sistema. Pode ser muito
comum em seu dia a dia querer consultar os funcionários que estão
vinculados às vendas, ou saber qual o seu produto mais vendido.

Sabendo disso, melhor do que criarmos uma mesma consulta
em diversos lugares do sistema ou diversas vezes, é criar uma visão
estática da consulta no banco de dados, em forma de um objeto.
Assim, sempre que quisermos o resultado que ela fornece, nós
fazemos a consulta em cima da  view , e não diretamente com as
tabelas.

Vamos criar uma visão que nos trará os produtos mais vendidos
no dia por ordem alfabética e por ordem de maior venda. Para
trazer as vendas que tivemos no dia, usaremos a função

 current_date , mas como provavelmente não temos vendas no dia
em que você estará fazendo essa consulta, vou colocar nela a data
que coloquei nos  scripts  de inserção de dados. Agora fique à
vontade em inserir dados e substituir a data da consulta pela função
que retorna a data atual.

postgres# create or replace view vendas_do_dia as

               select distinct produto_nome
                    , sum(vendas.venda_total)
                 from produtos, itens_vendas, vendas
                where produtos.id = itens_vendas.produto_id
                  and vendas.id   = itens_vendas.vendas_id
                  and vendas.data_criacao = '01/01/2016'
                group by produto_nome;

Figura 7.10: Criando views para agilizar o dia a dia

Agora que temos esta visão criada em nosso banco de dados,

**130** 
7.3 VIEWS


--------------------------------------------------

podemos consultá-la quando desejarmos, da seguinte maneira:

postgres# select * from vendas_do_dia;

Figura 7.11: Resultado da consulta da view

Podemos ainda fazer consultas em nossa view com outras
cláusulas, como por exemplo, buscar se um determinado produto
foi vendido no dia inserido na visão.

postgres=# select * 

            from vendas_do_dia
           where produto_nome = 'PASTEL';

Figura 7.12: Adicionando cláusula em consulta com views

Podemos também criar uma visão que traria diversos campos e
você poderia passar outros parâmetros.

postgresq# create or replace view produtos_vendas as

              select produtos.id PRODUTO_ID
                   , produtos.produto_nome PRODUTO_NOME
                   , vendas.id VENDA_ID
                   , itens_vendas.id ITEM_ID
                   , itens_vendas.item_valor ITEM_VALOR
                   , vendas.data_criacao DATA_CRIACAO
                from produtos, vendas, itens_vendas

7.3 VIEWS 
**131**


--------------------------------------------------

               where vendas.id   = itens_vendas.vendas_id
                 and produtos.id = itens_vendas.produto_id
               order by data_criacao desc;

Agora podemos consultar qualquer uma das colunas que estão
contidas na  view e também realizar comparações com elas.

postgres=# select *

            from produtos_vendas;

Figura 7.13: Uma view com diversos campos

postgres=# select produto_nome

            from produtos_vendas
           where data_criacao = '01/01/2016';

Figura 7.14: Selecionando apenas um campo da view com uma condição

Todas as  views  que criamos foram com colunas. Será que
podemos criar visões de uma tabela inteira? Claro que sim! Vamos
criar uma visão da nossa tabela de produtos.

**132** 
7.3 VIEWS


--------------------------------------------------

postgres=# create or replace view produtos_estoque as

              select * 
                from produtos;

Agora podemos consultar qualquer campo da tabela, só que
agora pela  view .

postgres=# select produto_nome

            from produtos_estoque;

Figura 7.15: View de uma tabela inteira

Mas você deve estar se perguntando qual seria a vantagem ou o
sentido de se fazer isso, não é mesmo? Além dos motivos que citei
anteriormente, é muito comum termos de fornecer acesso à nossa
base de dados para outras pessoas. Em vez de fornecemos acesso a
toda base de dados, fornecemos apenas a algumas  views por meio
dos direitos de usuários. É uma maneira de permitir acesso a apenas
alguns campos e tabelas da maneira que desejar.

Ampliamos um pouco mais o nosso leque de opções para
trabalhar com consultas. Esta é a principal função de um SGBD:

## 7.4 PARA PENSAR!

7.4 PARA PENSAR! 
**133**


--------------------------------------------------

extrair dados. Estamos saindo deste capítulo sabendo realizar
consultas com várias tabelas juntas.

Imagine as possibilidades de integrar as views com  functions ,
ou as  joins  naquelas  functions  que utilizamos para retornar
valores. Nunca me canso de falar que é a prática que faz um bom
programador. Insira mais registros em sua base de dados e faça
consultas à vontade. Crie  views  para cada tabela que nós temos.
Pratique!

No próximo capítulo, vamos conhecer um pouco de
administração de banco de dados, pois todo programador deve
conhecer um pouco de infraestrutura. Além de administração,
aprenderemos um pouco sobre performance de nosso banco e de
consultas.

**134** 
7.4 PARA PENSAR!


--------------------------------------------------

CAPÍTULO 8

"Não faz sentido olhar para trás e pensar: devia ter feito isso ou
aquilo, devia ter estado lá. Isso não importa. Vamos inventar o
amanhã e parar de nos preocupar com o passado". — Steve Jobs

A pessoa responsável pela administração do banco de dados é
conhecida como DBA (Data Base Administrator, ou no bom e velho
português, Administrador de Banco de Dados). Em muitas
empresas, vocês podem se deparar com o próprio desenvolvedor
fazendo o papel de administrador do banco de dados. Isto é muito
comum, principalmente em pequenas empresas que não têm um
capital disponível para a contratação de um profissional capacitado
para esta função.

O DBA é responsável por administrar aspectos de infraestrutura
do banco, como performance, arquitetura, criação, importação e
backup. Mas como nem sempre as empresas possuem esse papel,
essas e muitas outras funções ficam a cargo do desenvolvedor.

Muitas pessoas divergem sobre até onde o desenvolvedor deve

# ADMINISTRAÇÃO DO
# BANCO E OUTROS
# TÓPICOS

## 8.1 ADMINISTRADOR DE BANCO DE DADOS
## VS. DESENVOLVEDOR

8 ADMINISTRAÇÃO DO BANCO E OUTROS TÓPICOS 
**135**


--------------------------------------------------

influenciar no banco de dados. Alguns dizem que ele deveria apenas
escrever os códigos que devem ser aplicados no banco de dados, e
quem deveria aplicar no banco e fazer a validação dos códigos é o
administrador do banco. Atualmente, como existem vários
frameworks que criam automaticamente as tabelas e os código do
banco de dados, acaba que, para o administrator, fica a tarefa de
administrar aspectos da performance, segurança e a estrutura do
banco.

Se você não é e não pretende ser um desenvolvedor, você deve se
preocupar com aspectos da estrutura do servidor do banco de
dados, como saber otimizar consultas e melhorar performance, pois
é o que o ocorre no dia a dia de um administrador do banco de
dados cobra, além de saber comandos para a configuração e
otimização do servidor. E se você é um desenvolvedor e não tem
disponível um profissional para executar essas tarefas, é importante
que você tenha algum conhecimento.

Agora se você é desenvolvedor e tem a disponibilidade de um
administrador para fazer o trabalho da administração do servidor de
banco de dados, você pode se preocupar em apenas aprender os
aspectos referentes a modelar o banco e a utilização da linguagem de
programação. De qualquer forma, aprender alguns comandos de
administração sempre será útil.

Para auxiliá-lo na utilização e administração do cotidiano, temos
alguns comandos que são de extrema importância. Se você dominá-
los, não terá necessidade da utilização de uma ferramenta.
Dominando os comandos em um terminal, você terá condição de
dominar qualquer ferramenta visual de gerenciamento de banco de
dados.

## 8.2 COMANDOS ÚTEIS

**136** 
8.2 COMANDOS ÚTEIS


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------

algum outro lugar que não seja a máquina em que o servidor atual
se encontra. Vamos agora entender como fazer backup do seu
banco e como usá-lo posteriormente, além de conhecer as maneiras
como o backup pode ser realizado.

Para verificarmos que nosso arquivo de backup está correto,
devemos importá-lo em algum banco de dados. Para isso,
precisamos criar um banco e importar o arquivo exportado.

Vamos criar o nosso novo banco de dados, e aproveitar e criar
também um novo usuário. Então, mãos no teclado.

postgres=> create user nomedousuario superuser;

Alteramos a senha do novo usuário:

postgres=> alter user nomedousuario password 'senha2'

Feito isso, vamos sair novamente do terminal e conectar com o
usuário criado:

$> psql -U nomedousuario postgres -h localhost

E finalmente vamos criar o novo banco de dados, que chamarei
de  novobanco :

postgres=> create database newbase;

Em vez de sair do terminal e entrar com outro usuário e banco
de dados, no próprio terminal do PostgreSQL podemos fazer a troca
utilizando o comando  \c .

postgres=# \c nomedousuario newbase;

Você pode observar que, no cursor do terminal, agora aparece

 'newbase=# . Podemos listar os bancos de dados e visualizar o que
criamos e o usuário. Na lista de comandos anterior, existe o
comando  \l  que lista os bancos de dados e seus respectivos
usuários.

8.3 BACKUPS 
**139**


--------------------------------------------------

newbase=# \l;

Se você não criou nenhum outro banco, você obterá o resultado
a seguir:

Figura 8.1: Bancos de dados criados

Observe que a lista dos bancos criados e dos usuários que os
criaram. Até agora estávamos usando o banco de dados  postgres 
e o usuário  postgres . E desse banco de dados, vamos exportar os
objetos e registros.

Agora que temos um novo banco de dados para receber uma
importação do banco que estamos trabalhando deste do início de
nosso projeto, vamos exportar o banco de dados  postgres . Saia
do terminal do Postgre e digite o comando a seguir, que exportará
todos os objetos e registros do banco  postgres .

$> pg_dump --host localhost --port 5432 --username postgres --form
at tar --file nomearquivo.backup postgres

Pronto! Muito simples, não é mesmo? A frequência com que
você vai fazer o backup do seu banco de dados será você que
decidirá. O aconselhável é que ele seja feito diariamente, pois se algo
acontecer, você sempre terá um arquivo de recuperação, pronto
para ser usado.

**### Exportação**

**### Importação**

**140** 
8.3 BACKUPS


--------------------------------------------------

A importação é ainda mais simples. Vamos digitar o comando
passando o nome do banco cuja importação queremos fazer e o
usuário. O comando ficará da seguinte maneira:

$> pg_restore --host localhost --port 5432 --username nomedousuari
o --dbname newbase nomearquivo.backup

Para verificarmos se foram importados todos os objetos, vamos
utilizar o comando  d .

newbase=# \d;

Figura 8.2: Objetos criados com a importação

Utilizar planilhas para armazenar dados é a prática mais adotada
por pequenas empresas em estágio inicial, por ser uma solução de
baixo custo. Alguns estudos mostram que 50% das pequenas
empresas armazenam seus dados em planilhas, e a importação de

**### Importação via planilha CSV**

8.3 BACKUPS 
**141**


--------------------------------------------------

dados via arquivo CSV é tarefa frequente e importante no dia a dia
de muitos administradores de banco de dados.

Para realizarmos a importação dos dados de uma planilha CVS
para uma tabela específica do nosso banco de dados, vamos criar
uma planilha com dados e importá-los para a tabela de
funcionários. Abra uma planilha e, na primeira linha, adicione um
registro para cada coluna da tabela.

Figura 8.3: Dados na planilha CSV

Depois de ter criado e salvo a planilha com o nome

 funcionarios.csv , vamos usar o comando a seguir e fazer a
importação dos dados. Observe no comando que vamos dizer para
qual tabela copiaremos os dados e descrever para quais campos
desta tabela os dados serão importados.

Note que, na planilha, as colunas devem ficar na mesma ordem
em que as colunas no comando a seguir. No lugar do

 /local_do_arquivo/ , substitua pelo caminho onde seu arquivo se
encontra. O CSV é um arquivo que delimita os registros por  ; , por
isso, no comando tem  DELIMITER ';' . Se você criou um arquivo
CSV cujos registros possuem outro caractere separador, basta
substituir o ponto e vírgula pelo seu caractere limitador.

postgres=# 

COPY funcionarios
( 

  funcionario_codigo,
  funcionario_nome,
  funcionario_situacao,
  funcionario_comissao,
  funcionario_cargo,

**142** 
8.3 BACKUPS


--------------------------------------------------

  data_criacao,
  data_atualizacao
)    
FROM '/local_do_arquivo/funcionarios.csv'
DELIMITER ';'
CSV HEADER;

Exportar e importar dados é algo muito simples. Não tem
desculpa para não os fazer. Então, não se esqueça: backup
diariamente!

A criação de índices é uma solução muito utilizada a fim de
melhorar o desempenho das consultas no banco de dados. Segundo
o próprio manual do PostgreSQL, o índice permite ao servidor de
banco de dados encontrar e trazer linhas específicas muito mais
rápido do que faria sem o índice.

Ele consegue um melhor desempenho em uma consulta, pois o
índice ordena os registros da coluna onde está criado, de forma que
a consulta seja mais eficiente. Porém, existe uma desvantagem ao
optar pela criação de índices, algo que ocorre em qualquer banco de
dados: as instruções de  insert ,  update  e  delete  de registros
podem ficar mais lentas. Isso ocorre pois utilizar um desses
comandos em uma tabela que possui índice provoca uma
reorganização dos índices. Por isso, deve ser usado com cautela.

Vamos usar nossa tabela de funcionários. Atualmente, se
executarmos a consulta:

postgres=# select * from funcionarios where funcionario_cargo = 'G
ARÇOM';

Como não temos um índice nesta tabela, o banco de dados vai
percorrer toda ela, linha a linha, para encontrar todos os registros

## 8.4 
## ÍNDICES 
## E 
## PERFORMANCE 
## DAS
## CONSULTAS

8.4 ÍNDICES E PERFORMANCE DAS CONSULTAS 
**143**


--------------------------------------------------

que correspondam à consulta. Imagine se tivéssemos mais muitos
registros nessa tabela, e essa consulta nos retornasse diversos
resultados.

Sem o índice, o banco de dados percorreria linha a linha para
encontrar os que correspondem a  funcionario_cargo =

'GARÇOM' . No entanto, se criarmos um índice na coluna

 funcionario_cargo , o banco de dados ordenaria os registros
dessa tabela usando um método mais eficiente para localizar as
linhas correspondentes.

Um exemplo que o manual do PostgreSQL cita é o método
utilizado por alguns livros, no qual os termos e os conceitos
procurados frequentemente pelos leitores são reunidos em um
índice alfabético colocado no final do livro. O leitor interessado
pode percorrer o índice rapidamente e ir direto para a página
desejada, em vez de ter de ler o livro por inteiro em busca do que
está procurando.

Assim como é tarefa do autor prever os itens que os leitores
mais provavelmente vão procurar, é tarefa do programador de
banco de dados prever quais índices trarão benefícios. Sabendo
disso, temos de entender qual será a utilidade do índice em uma
determinada tabela para o projeto.

Procure criar índice para colunas que serão constantemente
utilizadas para pesquisa em seu projeto. Outra dica é criar índice em
colunas nas quais o resultado, na maioria das vezes, vai buscar mais
de um registro. Por se usado em coluna, onde as consultas
resultarão em apenas uma linha, o índice não será eficiente, uma vez
que o banco de dados terá dificuldade para ordenar os registros e
buscá-los.

Voltando ao exemplo que estamos utilizando, vamos criar um
índice na coluna  cargo na tabela  funcionarios .

**144** 
8.4 ÍNDICES E PERFORMANCE DAS CONSULTAS


--------------------------------------------------

postgres=# create index idx_cargo on funcionarios(funcionario_carg
o);

Observe que, para o nome do índice  idx_cargo , usei um
prefixo como padrão. Durante o nosso projeto, venho frisando a
importância da utilização de padrões na criação de objeto no banco
de dados, pois é algo muito importante para manutenções futuras e
para manter a qualidade do nosso projeto. O uso de um padrão
permite que alguém que não conhece o projeto, ao ver o código,
consiga entender a que se refere uma determinada nomenclatura.

Se você observar que um índice não está sendo eficiente, você
não só pode como deve excluí-lo, pois lembre-se de que ele pode
prejudicar algumas execuções no banco. Sendo assim, para excluir
um índice, você vai utilizar o comando a seguir:

posgtres=# drop index idx_cargo;

Temos alguns tipos de índices no PostgreSQL, sendo que cada
um usa um algoritmo diferente para cada tipo de consulta. Por
padrão, com o comando que utilizamos para a criação do índice na
tabela de funcionários, o PostgreSQL usa o índice B-tree.

Ele é o mais adequado para as situações comuns de consultas.
Vamos conhecer os principais tipos com que você poderá esbarrar
no dia a dia.

**B-tree**

O B-tree é o tipo padrão. Sempre que utilizamos o comando

 create index , estamos criando índice deste tipo. Os B-trees
podem tratar consultas de igualdade e de faixa, em dados que
podem ser classificados em alguma ordem.

O SGBD, ao planejar as consultas, levará em consideração a

**### Tipos de índices**

8.4 ÍNDICES E PERFORMANCE DAS CONSULTAS 
**145**


--------------------------------------------------


--------------------------------------------------

O PostgreSQL nos disponibiliza um tipo de índice para essas
circunstâncias. Os índices concorrentes são bem úteis para essas
situações, nas quais é necessário criarmos um índice em ambiente
de produção que não pode ser interrompido.

Para criar este tipo de índice, usamos o comando:

postgres=# create index concurrentyle idx_nome on 

             funcionarios btree (funcionario_nome);

**Multicolunas**

Durante o nosso projeto, aprendemos a fazer consultas em mais
de uma coluna de uma vez. Os índices de uma única coluna não
serão úteis para melhorar a performance de consultas onde serão
comparadas mais de uma coluna. Para isso, podemos criar um
índice que seja utilizado para duas colunas ao mesmo tempo.

Para criar este tipo de índice, usamos o comando:

postgres=# create index idx_funcionario_id_codigo on 

             funcionarios(id, funcionario_codigo);

Este tipo de índice seria útil para consultas do tipo:

postgres=# select *

            from funcionarios
           where id > 10
             and funcionario_codigo < '1000';

Anteriormente, aprendemos a criar  constraints  de chave
primária e chave estrangeira. Também vimos que uma chave
primária de tabela é um registro único. Se quisermos que qualquer
outra coluna de uma determinada tabela tenha um valor único,
podemos criar um índice que tornará o valor de uma coluna
exclusivo.

Vamos transformar a coluna  funcionario_codigo única. Para

**### Índices únicos**

8.4 ÍNDICES E PERFORMANCE DAS CONSULTAS 
**147**


--------------------------------------------------

isso, usaremos o comando:

postgres=# create unique index idx_unique_codigo on 

                funcionarios(funcionario_codigo);

Para sabermos se este índice está funcionando corretamente,
vamos tentar inserir um novo registro na tabela  funcionarios  e,
no  insert  do registro, utilizar um código de funcionário que já
exista na tabela. Primeiro, vamos fazer uma consulta para poder
pegar um  funcionario_codigo  de um funcionário existente no
banco.

postgres=# select funcionario_codigo

            from funcionarios;

Em minha base, tenho um funcionário com o código  0001 . Se
você vem seguindo o projeto e adicionando todos os registros
sugeridos, você também deve tê-lo.

Agora vamos inserir um registro na tabela de funcionários e
tentar utilizar esse mesmo código que já existe na base.

postgres=# insert into funcionarios(funcionario_codigo, funcionari
o_nome)

           values('0001', 'DANIEL VINICIUS SOUZA');

Ao clicarmos  enter , será exibido o erro:

Figura 8.4: Erro de unique key

Utilize em coluna que ainda não possua itens duplicados, ou
antes de duplicar itens, pois se a coluna já possuir itens em
duplicidade, este erro também será exibido.

Com o índice criado em nossa tabela de funcionários, o banco

**### Analyze**

**148** 
8.4 ÍNDICES E PERFORMANCE DAS CONSULTAS


--------------------------------------------------

de dados vai atualizar o índice automaticamente quando houver
uma modificação. A otimização nas consultas é realizada quando ele
julgar mais eficiente do que a busca linha a linha.

O PostgreSQL consegue julgar a forma mais eficiente de fazer as
consultas por meio de estatísticas retiradas das tabelas. Além dessa
ordenação que o próprio SGBD executa, é importante nós
executarmos o comando  analyze  periodicamente. Este comando
coleta estatísticas sobre o conteúdo das tabelas do banco de dados e
armazena 
os 
resultados 
em 
uma 
tabela 
do 
sistema, 
a

 pg_statistic .

O SGBD usa essas estatísticas para ajudar a determinar qual a
forma mais eficiente de executar as consultas em seu banco de
dados. Se não passarmos nenhum parâmetro para o comando

 analyse , o SGBD analisará todas as tabelas do banco de dados que
você estiver conectado. Mas podemos passar parâmetros para
analisar determinados objetos.

Primeiro, vamos pedir para que sejam analisadas todas as tabelas
do nosso banco:

postgres=# analyze verbose;

Será exido o resultado da análise das estatísticas de todas as
tabelas. Agora, pediremos para que seja analisada a tabela de
funcionários.

postgres=# analyze verbose funcionarios;

Neste caso, apenas será atualizado as estatísticas da tabela de
funcionários. Podemos ir além e pedir para executar a análise
apenas da coluna  funcionario_cargo .

postgres=# analyze verbose funcionario(funcionario_cargo);

Dentre os itens coletados pelo comando  analyze , as listas de
alguns valores mais comuns de cada coluna e um histograma

8.4 ÍNDICES E PERFORMANCE DAS CONSULTAS 
**149**


--------------------------------------------------

mostrando a distribuição aproximada dos dados de cada coluna
auxiliam a organização dos registros. Vale lembrar de que as
estatísticas podem mudar a cada execução do  analyze , assim
alterando a forma com que o SGBD executa a otimização das
consultas, mesmo que não tenha alteração de registros. Por isso,
devemos fazer periodicamente a análise das tabelas.

Mesmo realizando o  analyze  constantemente, o desempenho
do índice pode ser pedido com o tempo e pode tornar o índice
ineficiente. Se for percebida a perda do desempenho do índice,
temos a opção de fazer a reindexação do índice.

Ela refará o processo de indexar os registros de onde ele for
criado. Essa ação fará com que o índice volte a performar melhor
em seu SGBD. Para fazer essa reindexação, vamos usar o comando:

postgres=# reindex table funcionarios;

Após esse comando, o SGBD vai reindexar os índices da tabela
de funcionários.

Agora que você fez o backup do seu banco, tabelas e registros, e
ele está salvo em algum lugar seguro (assim espero), quero que você
tente reutilizar todos os métodos de backup e importação para
outras tabelas que não fizemos. Se for preciso, crie outros bancos e
faça a importação dos dados.

Lembra da frase do Aristóteles, em um dos capítulos anteriores,
na qual ele diz que a repetição leva a perfeição? #FicaADica.

Outro ponto que vimos neste capítulo foi a importação via CSV.
É muito útil quando você precisa fazer uma migração de uma base

**### Reindexação**

## 8.5 PARA PENSAR!

**150** 
8.5 PARA PENSAR!


--------------------------------------------------

de dados para outra, ou até mesmo de um banco de dados diferente.
Se você conhece alguém que quer sair das planilhas e utiliza um
banco de dados, você já poderá ajudá-lo.

8.5 PARA PENSAR! 
**151**


--------------------------------------------------

CAPÍTULO 9

"Sempre entregue mais do que o esperado". — Larry Page

Além dos tipos de campos que aprendemos anteriormente, o
PostgreSQL possui alguns tipos de dados especiais que outros
bancos de dados relacionais, como o MySQL, não possuem. A
utilização de tipo de dados diferentes vai depender do projeto no
qual você estiver trabalhando.

Sempre avalie o que você está desenvolvendo, pesquise por
soluções e aplique aquela que melhor se encaixar em seu problema.
Também não se prenda a apenas uma solução. Em desenvolvimento
de software, muito dificilmente existirá apenas uma forma de
resolver um problema. Não tenha preguiça de testar mais de uma
solução.

Essa é minha dica para você usar estes dois principais tipos de
campos especiais do PostgreSQL. Não entrarei em detalhes de
outros tipos especiais, pois muito dificilmente você vai utilizá-los
em suas aplicações.

Os tipos de campos  array  e  JSON , você verá que terá uma
boa aplicação em nosso projeto e poderá lhe ser útil futuramente no

# TIPOS DE DADOS
# ESPECIAIS

## 9.1 TIPOS DE CAMPOS ESPECIAIS

**152** 
9 TIPOS DE DADOS ESPECIAIS


--------------------------------------------------

desenvolvimento de aplicações web modernas.

Se você já conhece alguma linguagem de programação, já está
familiarizado com o termo  array  e sua funcionalidade. Se você
ainda não está familiarizado, um  array  é uma lista de objetos.
Enquanto os tipos de campos que conhecemos até agora conseguem
armazenar apenas um objeto, um  array  pode armazenar uma
lista.

Provavelmente, você já deve ter se deparado com algum lugar
exibindo uma lista de objetos como na figura a seguir, como se fosse
uma lista de objetos que se referem à mesma coisa.

Figura 9.1: Utilização de listagem

Você já consegue imaginar onde podemos utilizar esse campo
em nosso projeto? Vamos supor que precisamos categorizar nossos
produtos, mas não somente uma característica para cada um, mas
sim uma lista de categoria para cada produto. Para isso, vamos criar
um novo campo chamado  produto_categoria do tipo  array , e
entender como podemos usar esse campo.

A criação do tipo de campo  array  é parecida com o que
aprendemos anteriormente, apenas adicionamos o elemento
colchetes à frente do tipo do campo que queremos criar. Se
quiséssemos criar um campo do tipo  string , normalmente
faríamos  produto_categoria text . No entanto, como queremos
que ele seja do tipo  array , devemos declará-lo como

## 9.2 CAMPOS ARRAY

9.2 CAMPOS ARRAY 
**153**


--------------------------------------------------

 produto_categoria text[] .

Os colchetes depois do campo dizem ao nosso banco de dados
que este campo poderá armazenar uma string ou uma lista de
strings. Mãos no teclado para criamos o código para criação do
nosso campo.

postgresql=# alter table produtos 

              add column produto_categoria text[];

Para utilizar o novo campo, vamos inserir um novo produto, e
aprender como devemos adicionar registro neste novo tipo de
campo que acabamos de conhecer.

postgresql=# 

insert into produtos (produto_codigo,

                     produto_nome,
                     produto_valor,
                     produto_situacao,
                     data_criacao,
                     data_atualizacao,
                     produto_categoria)
             values ('03251',
                     'ESFIRRA',
                      5,
                     'A',
                     '01/01/2016',
                     '01/01/2016',
                     '{"CARNE", "SALGADO", "ASSADO" , "QUEIJO"}');

Observe que a inserção em campo do tipo  array  é um pouco
diferente dos outros. Como se trata de uma lista de strings,
precisamos de alguma maneira limitar cada string, por isso devemos
usar as aspas simples para indicar ao banco de dados que vamos
inserir uma string, seguido do elemento chaves para indicar que se
trata de uma lista de objetos. Depois, usamos as duplas para limitar
cada string, e vírgula para separar cada item da lista, tendo a lista
que formamos em nosso código:  {"CARNE", "SALGADO",

"ASSADO" , "QUEIJO"} .

**154** 
9.2 CAMPOS ARRAY


--------------------------------------------------

Após fazer a inserção deste novo registro em nossa tabela,
podemos fazer uma consulta para verificar como ficam os dados no
banco de dados. Mãos no teclado e vamos fazer uma consulta
usando somente o campo que criamos agora.

postgresql=# select produto_categoria

              from produtos
             where produto_nome like 'ESFIRRA';

Como resultado, teremos:

Figura 9.2: Inserindo uma lista de strings

Além de fazermos uma consulta para verificar todos os
elementos da lista, podemos criar uma consulta para extrair apenas
um item ou uma faixa de itens da lista que o campo array possui. Na
inserção que fizemos, adicionamos uma lista com quatro elementos,
como mostra a figura:

Figura 9.3: Elementos do nosso array

Observando esta imagem, vemos todos os itens da lista inseridos
no campo  produto_categoria . E se em vez de selecionar todos os
elementos da lista, quiséssemos consultar o somente segundo item
da lista?

9.2 CAMPOS ARRAY 
**155**


--------------------------------------------------

Baseando-se nesta figura dos itens, podemos deduzir que cada
item encontra-se em uma posição e, sabendo disso, o PostgreSQL
nos permite fazer consultas nos itens de um  array  pela sua
posição. Desta vez, em vez de selecionarmos todos os elementos da
lista, consultaremos apenas o segundo elemento da lista. Vamos
fazer isso passando como parâmetro o número dois, indicando para
o banco de dados que desejamos que ele nos retorne o item que está
na posição 2 da lista. Mãos no teclado e vamos para o nosso código.

postgresql=# select produto_categoria[2]

              from produtos
             where produto_nome like 'ESFIRRA';

Simples, não é mesmo?! Em vez de colocarmos apenas o nome
do campo, passamos entre colchetes a posição que queríamos. E
como resultado, temos:

Figura 9.4: Busca em uma posição do array

Além de um consultar uma posição de um  array , podemos
consultar um intervalo de posições. Agora vamos criar uma
consulta para buscar os itens da posição 2 até a posição 4 da lista.

postgresql=# select produto_categoria[2:4]

              from produtos
             where produto_nome like 'ESFIRRA';

Observe em nosso código que agora usamos dois pontos para
separar a posição inicial da final. Como resultado, teremos:

Figura 9.5: Busca em um intervalo de posições do array

**156** 
9.2 CAMPOS ARRAY


--------------------------------------------------

O tipo  array  pode ser muito útil dependendo do contexto de
seu projeto. Para treinar, agora insira mais registros na tabela de
produtos e atualize os registros existentes, adicionando informação
no campo  produto_categoria . Pratique!

O próximo tipo que conheceremos é o  JSON . Antes da versão
9.2 do PostgreSQL, armazenar dados neste formato era
exclusividade dos bancos NoSQL. Estes são classificados como não
relacionais, pois, diferentemente dos bancos MySQL e PostgreSQL,
não possuem um esquema rígido no qual os relacionamentos entre
as tabelas precisam se relacionar. Se você quiser se aprofundar em
banco de dados NoSQL, aconselho conhecer os livros sobre o
assunto da Casa do Código sobre NoSQL "NoSQL Como armazenar
os dados de uma aplicação moderna" e sobre MongoDB "MongoDB
Construa novas aplicações com novas tecnologias".

Até algum tempo atrás, o formato universal mais usado para
troca de informações e dados era o  XML , até que o  JSON  se
popularizou e hoje em dia é o método mais utilizado para troca de
informações. Seu significado é JavaScript Object Notation, mas
apesar do nome, ele pode ser manipulado por diversas linguagens
de programação. São muitas as que dão suporte ao JSON.

Para usarmos este tipo de campo em nosso projeto, vamos
alterar novamente a tabela de produtos. Vamos inserir o campo

 produto_estoque . Ele vai armazenar informações sobre o estoque
de cada produto.

Não tem segredo para a utilizar este tipo de campo. Basta apenas
informar  produto_estoque json . Então, vamos ao código.

postgresql=# alter table produtos 

              add column produto_estoque json;

## 9.3 CAMPOS DO JSON

9.3 CAMPOS DO JSON 
**157**


--------------------------------------------------

Agora vamos conhecer a estrutura que devemos inserir os
registros nesta nova coluna. A estrutura básica de um objeto JSON é
a seguinte:

{"ObjetoPai": "valor"}

E o objeto pai pode ter objetos filhos:

{
"ObjetoPai":{

   "ObjetoFilho":"valor"
 }
}

Basicamente será isso que deveremos inserir em nosso código.
Eu vou adicionar um objeto pai chamado  info_estoque , e os
objetos filhos  tem_estoque  para indicar se o produto tem no
estoque, o objeto filho  quantidade para indicar quantos produtos
possui no estoque e o objeto filho  ultima_compra  para indicar a
data da última compra. Da mesma maneira que descrevi, também
informaremos um valor para cada objeto. Vamos ao nosso código.

postgresql=#

insert into produtos(produto_codigo,
                     produto_nome,
                     produto_valor,
                     produto_situacao,
                     data_criacao,
                     data_atualizacao,
                     produto_categoria,
                     produto_estoque)
           values('6234',
                  'COCA-COLA',
                  6,
                  'A',
                  '01/01/2016',
                  '01/01/2016',
                  '{"REFRIGERANTE", 
                    "LATA", 
                    "BEBIDA" , 
                    "COLA"}',
                  '{ "info_estoque": 

**### Cenário simples**

**158** 
9.3 CAMPOS DO JSON


--------------------------------------------------

                     { "tem_estoque": "SIM", 
                       "quantidade": 17, 
                       "ultima_compra": "01/01/16" } 
                   }'
                  );

Observe que o código possui a mesma estrutura básica do JSON.
Após a inserção desse registro, vamos criar uma consulta para
visualizarmos como esse tipo de registro fica em nosso banco.

postgresql=# select produto_estoque 

              from produtos 
             where produto_nome like 'COCA-COLA';

E como resultado, teremos:

Figura 9.6: Campo do tipo JSON

Da mesma maneira que aprendemos que, em campos do tipo

 array , podemos selecionar o item que quisermos de uma lista, em
campos do tipo JSON também temos a possibilidade de selecionar o
conteúdo do objeto que desejarmos. Vamos montar uma consulta
para nos retornar apenas o objeto filho  quantidade .

Para isso, temos de fazer a busca através do objeto pai. Sabendo
disso, teremos o nosso código:

postgresql=#

 select produto_estoque->'info_estoque'->>'quantidade' 
        as quantidade 
   from produtos  
  where produto_nome like 'COCA-COLA';

E como resultado, teremos o valor inserido no objeto filho

 quantidade .

**### Operadores -> e ->>**

9.3 CAMPOS DO JSON 
**159**


--------------------------------------------------

Observe que, nesta última consulta, foi usado o operador  ->> e
o banco de dados retornou o valor em formato de texto do objeto. E
se usássemos o operador  -> , teríamos como retorno um objeto
JSON.

Vamos aplicar na prática e identificar a diferença. Montaremos
uma consulta para buscar o valor do objeto  ultima_compra ,
primeiro com o operador  -> e, em seguida, com o operador  ->> .

postgresql=#

 select produto_estoque->'info_estoque'->'ultima_compra' 
        as ultima_compra 
   from produtos  
  where produto_nome like 'COCA-COLA';

Como retorno, teremos  "01/01/16" . Observe que o resultado
foi o objeto da forma que foi inserido no banco de dados, entre
aspas duplas. Agora vamos fazer a consulta com o operador  ->> .

postgresql=#

 select produto_estoque->'info_estoque'->>'ultima_compra' 
        as ultima_compra 
   from produtos  
  where produto_nome like 'COCA-COLA';

Como retorno, teremos  01/01/16 . Agora tivemos como
retorno apenas o texto do objeto, sem as aspas. Conhecendo estes
operadores, podemos passar para um exemplo um pouco mais
complexo.

Nesta primeira utilização de JSON, usamos um cenário simples,
no qual tínhamos apenas um objeto pai e alguns filhos. Agora
vamos inserir um JSON um pouco mais complexo. A única
diferença que este próximo JSON terá mais um objeto pai, que
chamaremos de  ultima_venda , em que será indicada a data da
última venda do produto.

**### Cenário complexo**

**160** 
9.3 CAMPOS DO JSON


--------------------------------------------------

postgresql=#

insert into produtos(produto_codigo,
                     produto_nome,
                     produto_valor,
                     produto_situacao,
                     data_criacao,
                     data_atualizacao,
                     produto_categoria,
                     produto_estoque)
           values('77978',
                  'GATORADE',
                  6,
                  'A',
                  '01/01/2016',
                  '01/01/2016',
                  '{"ISOTONICO", 
                    "GARRAFA", 
                    "BEBIDA" }',
                  '{ "info_estoque": 
                     { "tem_estoque": "SIM", 
                       "quantidade": 17, 
                       "ultima_compra": "01/01/16" },
                      "ultima_venda": "02/01/2016" 
                   }'
                  );

Em seguida, após inserir este novo registro, em vez de
buscarmos um objeto específico como fizemos anteriormente,
vamos utilizar os parâmetros de JSON na cláusula  where  para
buscar o conteúdo do campo  produto_estoque . Vamos criar uma
consulta que nos retornará o JSON do campo  produto_estoque 
que possui o valor do objeto  ultima_venda igual a  02/01/2016 .

postgresql=# 

  select produto_estoque 
    from produtos 
   where produto_estoque->>'ultima_venda' = '02/01/2016';

Como 
resultado, 
teremos 
o 
conteúdo 
do 
campo

 produto_estoque .

9.3 CAMPOS DO JSON 
**161**


--------------------------------------------------

Figura 9.7: Consulta com JSON com mais de um objeto pai

Observe como é muito simples trabalhar com JSON no
PostgreSQL, mesmo tendo um ou mais objetos pais. Este tipo de
campo pode ser muito útil em seu projeto. Se você for desenvolver
aplicações web, certamente você utilizará JSON e trocará objetos
JSON com outras aplicações. Com campo deste tipo em seu banco
de dados, ficará mais fácil você receber e armazenar esses dados.

Como já comentei anteriormente, tente sempre criar situações
reais quando você estiver aprendendo algo novo, pois fica mais fácil
absorver novos conceitos. É exatamente isto que eu tento fazer em
cada capítulo. Sempre utilizando o mesmo projeto e inserindo um
contexto que pode acontecer de verdade.

Tente fazer isso sempre que você perceber que fica mais simples
para aplicar novos conceitos em seu dia a dia. Agora que você
aprendeu esses dois novos tipos de campos, aplique-os nas demais
tabelas do projeto. Pense em situações que podem acontecer no
cotidiano da utilização do projeto que estamos construindo, e tente
aplicar soluções usando esses novos campos. Pratique sempre e cada
dia mais.

Para o próximo capítulo, teremos algumas questões para você
treinar conceitos aprendidos neste livro. São questões sobre banco
de dados extraídas de concursos públicos. Boa sorte! Keep
Programming! :)

## 9.4 PARA PENSAR!

**162** 
9.4 PARA PENSAR!


--------------------------------------------------

CAPÍTULO 10

"A sua maior frustração pode se transformar em sua maior ideia"
— Troy Osinoff

Cada dia mais vem crescendo o número de concursos na área de
desenvolvimento de software e Tecnologia de Informação no Brasil.
E a tendência desse número é aumentar.

95% dos concursos possuem perguntas sobre banco de dados, e
muitas vezes sobre um SGBD específico. Assim, fiz um compilado
de exercícios de várias provas de concursos aplicadas ao redor do
Brasil, sendo que as respostas para todas as perguntas estão no meio
dos capítulos que compõem este livro.

Algumas perguntas que extraí de provas de concursos adaptei
para o cenário do nosso projeto para que fique claro o conceito e a
pergunta que está sendo feita. Bora estudar?

# EXERCÍCIOS DE
# CONCURSO

## 10.1 CONCURSOS PELO BRASIL

## 10.2 EXERCÍCIOS

**### [0000 0001] O comando a seguir permite adicionar à**
**### tabela **** itens_vendas ****###  uma chave estrangeira com o**

10 EXERCÍCIOS DE CONCURSO 
**163**


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------

Tabela: **Bancos**

**Código**
**Nome**

001
Banco do Brasil

033
Santander

237
Bradesco

341
Itaú

Tabela: **Pessoas**

**CPF**
**Nome**

86277635697
Jóse da Silva

88208811874
Manoel da Silva

66516764743
Maria dos Santos

Tabela: **Conta_Corrente**

**Banco**
**Pessoa**
**Número**

033
86277635697
98876788

237
86277635697
96645727

341
66516764743
9102947

001
88208811874
8120938

a)  SELECT Nome, Numero FROM Pessoas, Conta_Corrente

WHERE Pessoa = CPF AND Banco IN (SELECT Codigo AS Banco

FROM Bancos WHERE Nome='Banco do Brasil') 

b)  SELECT Nome, Numero FROM Pessoas, Conta_Corrente,

Bancos WHERE Pessoa=CPF AND Banco IN (SELECT Codigo AS

Banco FROM Bancos WHERE Nome='Banco do Brasil') 

c)  SELECT Nome, Numero FROM Pessoas, Conta_Corrente

WHERE Pessoa=CPF AND Banco='Banco do Brasil' 

10.2 EXERCÍCIOS 
**169**


--------------------------------------------------

d)  SELECT Nome, Numero FROM Pessoas, Conta_Corrente,

Bancos WHERE Pessoa=CPF AND Nome='Banco do Brasil' 

e)  SELECT Nome, Numero FROM Pessoas, Conta_Corrente

WHERE Nome='Banco do Brasil' 

a)  chgstr 

b)  altertext 

c)  initcap 

d)  upper 

e)  toupper 

a)  create base escola; 

b)  create database escola; 

c)  create new database escola; 

d)  create escola as database; 

e)  create escola; 

**### [0000 1111] Em PostgreSQL, a função que converte a**
**### primeira letra da string informada em letra maiúscula,**
**### alterando todas as letras subsequentes dessa string**
**### para minúsculas, chama-se:**

**### [0001 0000] Em PostgreSQL, qual o comando correto**
**### para a criação de um banco de dados com o nome**

** escola ****### .**

**### [0001 0001] Quando queremos iniciar uma nova**
**### transação no banco de dados PostgreSQL, qual o**
**### comando que podemos usar?**

**170** 
10.2 EXERCÍCIOS


--------------------------------------------------

a)  alter 

b)  rollback 

c)  transfer 

d)  begin 

e)  create 

a)  ROLLBACK 

b)  END 

c)  TRANSFER 

d)  EFFECTIVE 

e)  SELECT 

a)  dateinit 

b)  styledate 

c)  datastyle 

d)  confinit 

e)  datestyle 

**### [0001 0010] Qual o nome do comando usado para**
**### recuperar os dados deletados de uma transação?**

**### [0001 0011] Dois países diferentes podem possuir o**
**### formato de datas diferente um do outro. O formato de**
**### datas do PostgreSQL pode ser alterado através da**
**### alteração de um parâmetro do banco de dados. Qual é**
**### esse parâmetro?**

10.2 EXERCÍCIOS 
**171**


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------

campo tipo  BYTEA .

Assinale a alternativa correta:

a) Somente as afirmativas 1 e 2 são verdadeiras.

b) Somente as afirmativas 2 e 3 são verdadeiras.

c) Somente a afirmativa 1 é verdadeira.

d) Somente a afirmativa 2 é verdadeira.

e) Somente a afirmativa 3 é verdadeira.

CREATE TABLE mec (

       cidade varchar(80),
       temp_baixa int,
       temp_alta int,
       nivel_precip int, 
       data timestamp );

Qual alternativa a seguir corresponde ao comando de inserção
de dados na tabela  mec ?

a)  INSERT IN mec(cidade, temp_baixa, temp_alta,

nivel_precip, data) VALUES ('Brasilia', 20, 34, 0.2,

'13/09/2015'); 

b)  INSERT ON mec(cidade, temp_baixa, temp_alta,

nivel_precip, data) VALUES ('Brasilia', 20, 34, 0.2,

'13/09/2015'); 

c)  INSERT FROM mec(cidade, temp_baixa, temp_alta,

nivel_precip, data) VALUES ('Brasilia', 20, 34, 0.2,

'13/09/2015'); 

d)  INSERT OVER mec(cidade, temp_baixa, temp_alta,

**### [0010 0011] Um DBA criou uma tabela em um Banco**
**### de Dados usando o seguinte comando:**

10.2 EXERCÍCIOS 
**177**


--------------------------------------------------

nivel_precip, data) VALUES ('Brasilia', 20, 34, 0.2,

'13/09/2015'); 

e)  INSERT INTO mec(cidade, temp_baixa, temp_alta,

nivel_precip, data) VALUES ('Brasilia', 20, 34, 0.2,

'13/09/2015'); 

CREATE TABLE OBJETOS(

   NOME varchar(20),
   TIPO varchar(30));

Se o DBA tentar criar uma view com o mesmo nome, qual
mensagem o banco vai retornar?

a) ERROR: syntax error at or "create"

b) ERROR: relation "objetos" already exists

c) ERROR: column "objetos" of relation "objetos" already exists

d) Não retornará erro e sim apenas uma advertência sobre os
nomes duplicados.

e) Não retornará erro e deixará fazer a criação da  view .

a)  UPDATE LIVROS AUTOR = 'VINICIUS CARVALHO'; 

b)  UPDATE LIVROS INTO AUTOR = 'VINICIUS CARVALHO'; 

c)  UPDATE LIVROS OVER 'AUTOR' = 'VINICIUS CARVALHO': 

**### [0010 0100] Um DBA criou uma tabela em um banco**
**### de dados utilizando o comando:**

**### [0010 0101] O DBA está com dúvida de qual comando**
**### usar para fazer update em uma coluna **** AUTOR ****### da tabela**

** livros ****### . Ajude-o informando o comando correto.**

**178** 
10.2 EXERCÍCIOS


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------

1. INT

2. PERSONALIZADO

3. NUMBER

4. VARCHAR2

5. TIMESTAMP

Escolha a opção correta:

a) 1 e 3.

b) 1, 2 e 5.

c) 2 e 4.

d) 1, 2 e 3.

e) 1, 2 e 4.

a)  CREATE TABLE mytable(f1 number, f2 float, f3

varchar2(20)); 

b)  CREATE TABLE mytable(f1 int, f2 float, f3

number); 

c)  CREATE TABLE mytable(f1 int, f2 float, f3

varchar2(10)); 

d)  CREATE TABLE mytable(f1 int, f2 float, f3 text); 

**### [0010 1101] Quais tipos de dados a seguir são válidos**
**### para o PostgreSQL?**

**### [0010 1110] Na criação de uma tabela, está sendo**
**### retornando um erro de sintaxe. Qual comando a seguir**
**### está correto?**

10.2 EXERCÍCIOS 
**181**


--------------------------------------------------

1. O valor do status de cada fornecedor está no intervalo de 500
a 900, inclusive.

2. Se houver peças, uma delas tem de ser amarela.

3. Dois fornecedores diferentes não têm o mesmo número de
fornecedor.

4. Cada fornecedor com negócios no Brasil tem status 700.

5. Cada remessa envolve um fornecedor existente.

6. Nenhum fornecedor com status menor que 700 fornece peça
alguma com uma quantidade maior que 350.

O exemplo descrito caracteriza o termo denominado de
restrição de:

a) Atividade

b) Integridade

c) Confiabilidade

d) Disponibilidade

**### [0010 1111] Em bancos de dados, um termo representa**
**### uma expressão booleana associada a um BD e que**
**### precisa ser avaliada como **** TRUE ****### , por todo o tempo.**
**### Vamos supor um banco de dados de fornecedores e**
**### peças.**

**### [0011 0000] Armazenar dados do tipo JSON, além de**
**### ser muito esperada, foi uma necessidade muito bem**
**### recebida pela comunidade de desenvolvedores que**
**### utilizam PostgreSQL, que passaram a armazenar JSON**
**### no banco de dados. Com base em seu conhecimento**

**182** 
10.2 EXERCÍCIOS


--------------------------------------------------

a)

insert into produtos(produto_codigo,
                     produto_nome,
                     produto_valor,
                     produto_situacao,
                     data_criacao,
                     data_atualizacao,
                     produto_categoria,
                     produto_estoque)
           values('6234',
                  'COCA-COLA',
                  6,
                  'A',
                  '01/01/2016',
                  '01/01/2016',
                  '{"REFRIGERANTE", 
                    "LATA", 
                    "BEBIDA" , 
                    "COLA"}',
                  '{ "info_estoque": 
                     { "tem_estoque": "SIM", 
                       "quantidade": 17, 
                       "ultima_compra": "01/01/16" } 
                   }'
                  );

b)

insert into produtos(produto_codigo,
                     produto_nome,
                     produto_valor,
                     produto_situacao,
                     data_criacao,
                     data_atualizacao,
                     produto_categoria,
                     produto_estoque)
           values('6234',
                  'COCA-COLA',
                  6,
                  'A',
                  '01/01/2016',
                  '01/01/2016',

**### sobre inserção de JSON em tabelas do banco de dados,**
**### selecione a inserção correta de um campo do tipo**
**### JSON.**

10.2 EXERCÍCIOS 
**183**


--------------------------------------------------

                  {"REFRIGERANTE", 
                    "LATA", 
                    "BEBIDA" , 
                    "COLA"},
                  '{ "info_estoque": 
                     { "tem_estoque": "SIM", 
                       "quantidade": 17, 
                       "ultima_compra": "01/01/16" } 
                   }'
                  );

c)

insert into produtos(produto_codigo,
                     produto_nome,
                     produto_valor,
                     produto_situacao,
                     data_criacao,
                     data_atualizacao,
                     produto_categoria,
                     produto_estoque)
           values('6234',
                  'COCA-COLA',
                  6,
                  'A',
                  '01/01/2016',
                  '01/01/2016',
                  {"REFRIGERANTE", 
                    "LATA", 
                    "BEBIDA" , 
                    "COLA"},
                  { "info_estoque": 
                     { "tem_estoque": "SIM", 
                       "quantidade": 17, 
                       "ultima_compra": "01/01/16" } 
                   }
                  );

d)

insert into produtos(produto_codigo,
                     produto_nome,
                     produto_valor,
                     produto_situacao,
                     data_criacao,
                     data_atualizacao,
                     produto_categoria,
                     produto_estoque)

**184** 
10.2 EXERCÍCIOS


--------------------------------------------------

           values('6234',
                  'COCA-COLA',
                  6,
                  'A',
                  '01/01/2016',
                  '01/01/2016',
                  {"REFRIGERANTE", 
                    "LATA", 
                    "BEBIDA" , 
                    "COLA"}',
                  '{ "info_estoque": 
                     { "tem_estoque": "SIM", 
                       "quantidade": 17, 
                       "ultima_compra": "01/01/16" } 
                   }
                  );

e)

insert into produtos(produto_codigo,
                     produto_nome,
                     produto_valor,
                     produto_situacao,
                     data_criacao,
                     data_atualizacao,
                     produto_categoria,
                     produto_estoque)
           values('6234',
                  'COCA-COLA',
                  6,
                  'A',
                  '01/01/2016',
                  '01/01/2016',
               '{"REFRIGERANTE", 
                    "LATA", 
                    "BEBIDA" , 
                    "COLA"}',
                  '{ "info_estoque": 
                     { "tem_estoque": "SIM", 
                       "quantidade": 17, 
                       "ultima_compra"  "01/01/16" } 
                   }
                  );

**### [0011 0001] PGSQL é uma linguagem procedural**
**### carregável desenvolvida para o sistema de banco de**
**### dados PostgreSQL. Como a maioria dos produtos de**

10.2 EXERCÍCIOS 
**185**


--------------------------------------------------

a)  query 

b)  media 

c)  med 

d)  avg 

e)  like 

Paulo usou, em linha de comando, a instrução:

a)  pg_dump -Ec -h trt13 > tribunal.tar 

**### banco de dados relacional, o PostgreSQL suporta**
**### funções de agregação. Uma função de agregação**
**### computa um único resultado para várias linhas de**
**### entrada. Por exemplo, para calcular a média, deve ser**
**### usada a seguinte função de agregação:**

**### [0011 0010] Paulo utiliza o **** pg_dump ****###  do PostgreSQL**
**### para fazer cópia de segurança de um banco de dados.**
**### Normalmente, ele faz cópias de segurança no formato**

** tar ****###  e usa o **** pg_restore ****###  para reconstruir o banco de**
**### dados, quando necessário. O **
** pg_restore ****###  pode**
**### selecionar o que será restaurado, ou mesmo reordenar**
**### os itens antes de restaurá-los, além de permitir salvar e**
**### restaurar objetos grandes. Certo dia, Paulo fez uma**
**### cópia de segurança do banco de dados chamado **** trt13 **
**### para o arquivo **** tribunal.tar ****### , incluindo os objetos**
**### grandes. Paulo utilizou uma instrução que permitiu a**
**### seleção manual e reordenação de itens arquivados**
**### durante a restauração. Porém, a ordem relativa de itens**
**### de dados das tabelas não pôde ser alterada durante o**
**### processo de restauração.**

**186** 
10.2 EXERCÍCIOS


--------------------------------------------------

b)  pg_dump -Ft -b trt13 > tribunal.tar 

c)  pg_dump -tar -a trt13 > tribunal.tar 

d)  pg_dump -tar -c trt13 > tribunal.tar 

e)  pg_dump -Fp -b trt13 > tribunal.tar 

10.2 EXERCÍCIOS 
**187**


--------------------------------------------------

CAPÍTULO 11

**Pergunta**
**Reposta**
**Pergunta**
**Reposta**

**[0000 0001]**
Errado
**[0001 1010]**
Errado

**[0000 0010]**
E
**[0001 1011]**
Certo

**[0000 0011]**
Certo
**[0001 1100]**
Certo

**[0000 0100]**
Certo
**[0001 1101]**
Certo

**[0000 0101]**
B
**[0001 1110]**
Errado

**[0000 0110]**
A
**[0001 1111]**
E

**[0000 0111]**
Errado
**[0010 0000]**
C

**[0000 1000]**
Errado
**[0010 0001]**
Certo

**[0000 1001]**
A
**[0010 0010]**
E

**[0000 1010]**
B
**[0010 0011]**
E

**[0000 1011]**
D
**[0010 0100]**
C

**[0000 1100]**
Errado
**[0010 0101]**
D

**[0000 1101]**
Certo
**[0010 0110]**
Certo

**[0000 1110]**
A
**[0010 0111]**
Errado

**[0000 1111]**
C
**[0010 1000]**
Errado

**[0001 0000]**
B
**[0010 1001]**
Errado

**[0001 0001]**
D
**[0010 1010]**
Errado

**[0001 0010]**
A
**[0010 1011]**
E

**[0001 0011]**
E
**[0010 1100]**
C

**[0001 0100]**
Errado
**[0010 1101]**
B

# GABARITO

**188** 
11 GABARITO


--------------------------------------------------

**[0001 0101]**
Certo
**[0010 1110]**
D

**[0001 0110]**
Errado
**[0010 1111]**
B

**[0001 0111]**
Errado
**[0011 0000]**
A

**[0001 1000]**
Certo
**[0011 0001]**
D

**[0001 1001]**
A
**[0011 0010]**
B

E aí? Como foi nos exercícios? Espero que tenha ido bem, para
se sair bem nos próximos concursos de que for participar. A ideia
foi dar uma noção de como são os exercícios das provas de
concursos, e também para você colocar um pouco em prática a
teoria aprendida no decorrer deste livro.

Se a sua intenção é fazer algum concurso público, existem vários
sites com perguntas e gabaritos de provas já aplicadas, direcionadas
para a área de tecnologia da informação. Eu retirei algumas questões
do site  https://www.qconcursos.com Bons estudos!

Sempre que existe aquela fase bônus no jogo é muito divertido.
Que tal agora uma fase bônus no próximo capítulo para
relaxarmos?! Aproveite! #Bônus

## 11.1 PARA PENSAR!

11.1 PARA PENSAR! 
**189**


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------

console do banco de dados e linha de comando para realizar todas
as tarefas. Fizemos tudo na "unha"! Mas existe uma outra forma de
manipular os dados, por uma ferramenta visual. Ela possibilita fazer
tudo o que fizemos até agora, só que de uma maneira mais simples.

Umas das ferramentas mais utilizadas para trabalhar com o
PostgreSQL é o pgAdmin. É uma ferramenta open source que tem
suporte para Windows, Linux e Mac OS. Você pode baixá-la em
https://www.pgadmin.org/, e lá escolher a versão para o seu sistema
operacional.

Após baixar e instalar, ao abrir pela primeira vez, o pgAdmin vai
identificar os servidores do PostgreSQL que estão executando em
sua máquina e solicitar a senha que você criou para o seu servidor.
Desde o começo do nosso projeto, a minha senha é  senha . E se
você não alterou a sua, então também será. Na figura a seguir
mostra onde você vai inserir a sua senha.

Figura 12.1: Informando a senha para se conectar ao servidor

Após estar conectado, a página inicial do pgAdmin apresenta
algumas informações estatística do banco de dados, as quais você
pode conhecer mais no site da ferramenta, e do lado esquerdo
encontrará a estrutura dos bancos que seu servidor possui.
Conforme vamos expandindo os itens, conseguimos visualizar os

**194** 
12.2 TRABALHANDO COM PGADMIN


--------------------------------------------------

objetos do nosso banco de dados.

Figura 12.2: Tela inicial do pgAdmin

Executamos todos os nossos códigos até agora no console do
PostgreSQL, e agora com pgAdmin os comandos podem ser
executados na ferramenta através da Query Tool. Ela pode ser
acessada por meio do  Menu > Tools > Query Tool , conforme
mostra a figura a seguir.

12.2 TRABALHANDO COM PGADMIN 
**195**


--------------------------------------------------

Figura 12.3: Área para executar os comandos

Ao acessar a Query Tool, abrirá um espaço no qual podemos
escrever os comandos e mandar executar, conforme mostra a figura
seguinte. Nela escrevi o comando o  select , que vai retornar os
registros da tabela  funcionarios .

Figura 12.4: Fazer consulta na ferramenta

**196** 
12.2 TRABALHANDO COM PGADMIN


--------------------------------------------------

Observe que o resultado da consulta foi exibido na parte abaixo
do espaço onde os comandos serão inseridos. Tudo que fizemos via
console podemos fazer aqui na ferramenta. Então, é possível
criarmos um banco de dados e uma tabela por ela.

Para criar um banco de dados, selecione do lado esquerdo

 Databases e, em seguida, vamos até a opção do menu  Object >

Create > Database .

Figura 12.5: Criando um novo banco de dados pela ferramenta

Isso abrirá uma tela de configurações do banco de dados. Vamos
inserir o nome do novo banco de dados  banco2  no campo

 Database , e clicar no botão  Save .

12.2 TRABALHANDO COM PGADMIN 
**197**


--------------------------------------------------

Figura 12.6: Inserindo o nome do novo banco

Após salvar a criação do novo banco, podemos visualizá-lo na
lista dos objetos do servidor.

**198** 
12.2 TRABALHANDO COM PGADMIN


--------------------------------------------------

Figura 12.7: Criando um novo banco de dados pela ferramenta

Agora, utilizando o novo banco de dados criado, criaremos uma
tabela através da ferramenta. Podemos escrever o código no espaço
através da Query Tool, mas isso já sabemos fazer, por isso vamos
criar a nova tabela pela ferramenta.

Na lista do lado esquerdo, navegue até  Tables  e, com o botão
direito do mouse, clique em  Create > Table . Uma tela aparecerá
para nos auxiliar nessa criação.

12.2 TRABALHANDO COM PGADMIN 
**199**


--------------------------------------------------

Figura 12.8: Criando tabela pela ferramenta

Primeiro, vamos informar o nome da tabela na aba  General . A
nossa nova tabela vai se chamar  tabela_produto .

**200** 
12.2 TRABALHANDO COM PGADMIN


--------------------------------------------------

Figura 12.9: Nomeando a nova tabela

Na sequência na aba  Columns , vamos inserir as suas colunas.
Em vez de escrever qual a configuração de cada coluna, da maneira
que fazemos quando escrevemos o comando, agora selecionaremos
o tipo de cada coluna, o tamanho (se for necessário), se poderá ser
nula e se o campo é uma chave primaria. Então, faremos a adição
dos campos pelo botão com o sinal  + , no canto superior direito.

Figura 12.10: Inserindo colunas na nova tabela

12.2 TRABALHANDO COM PGADMIN 
**201**


--------------------------------------------------

Inserindo as colunas, passamos para a aba  Constraints .
Como a coluna  id será uma chave primária, ela já vai aparecer na
listagem. Precisamos apenas nomeá-la, conforme a próxima figura.

Figura 12.11: Constraint na nova tabela

Após fazer as configurações das tabelas, vamos até a aba  SQL .
Lá visualizaremos o código para criação da tabela que será aplicado
no banco de dados. Na sequência, basta clicar no botão  Save , que
a tabela será criada.

Figura 12.12: SQL gerado pela ferramenta

**202** 
12.2 TRABALHANDO COM PGADMIN


--------------------------------------------------

Muito simples, não é mesmo!? Esta ferramenta facilita bastante a
nossa vida. Depois que você já conhece os comandos, não precisa
ficar escrevendo eles na mão. Dependendo do cenário que você
estiver trabalhando, até necessite utilizar o console do SGBD. Mas
em outras ocasiões, poderá usar uma ferramenta visual como o
pgAdmin.

Para melhor aprendizado, foi interessante ter trabalhado até
agora somente com o console do PostgreSQL, pois é uma forma de
entendermos e fixarmos bem todos os comandos aprendidos. Agora
que os conhecemos bem, podemos migrar para o pgAdmin, já que
ele nos dará mais produtividade durante o dia a dia.

Há quem prefira trabalhar apenas pelo console. Fica a seu
critério. Dependendo do cenário em que você estiver trabalhando,
poderá trabalhar tanto pelo console quanto pela ferramenta visual.

E aí, ficou com vontade de se tornar um DBA? É uma excelente
e promissora carreira. Você tem a possibilidade de se aperfeiçoar em
diversos bancos, ou se aprofundar em apenas um. Se quer conhecer
outros gerenciadores de banco de dados, procure os outros livros da
Casa do Código. Tem sobre Oracle "SQL: Uma abordagem para
bancos de dados Oracle" e "PL/SQL: Domine a linguagem do banco
de dados Oracle", MySQL (o meu primeiro livro) "MySQL: Comece
com o principal banco de dados open source do mercado" e NoSQL
"NoSQL: Como armazenar os dados de uma aplicação moderna".

Outra dica é procurar certificações focadas em determinados
banco de dados. Elas são muito bem conceituadas no mercado de
trabalho. Vale muito a pena.

Muito obrigado por chegar até aqui. Espero que tenha gostado

## 12.3 PARA PENSAR E AGRADECER!

12.3 PARA PENSAR E AGRADECER! 
**203**


--------------------------------------------------

do conteúdo do livro e que utilize em seu dia a dia. Qualquer dúvida
ou dica, pode me adicionar nas redes sociais. Terei o prazer em lhe
ajudar.

Nunca pare de estudar e se aperfeiçoar. Isso que vai lhe
diferenciar no mercado de trabalho. Ótimos estudos!

"Keep Coding" — Vinícius Carvalho

**204** 
12.3 PARA PENSAR E AGRADECER!

