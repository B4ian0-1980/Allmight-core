---json
{
  "id": "direto_ao_ponto_criando_produtos_de_forma_enxuta",
  "title": "COMO LER ESTE LIVRO",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "Guia tecnico e referencias sobre COMO LER ESTE LIVRO.",
  "gatilhos": [
    "como",
    "criando",
    "direto",
    "enxuta",
    "este",
    "forma",
    "ler",
    "linguagens"
  ],
  "perguntas_tipo": [
    "Como utilizar COMO LER ESTE LIVRO?",
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


--------------------------------------------------

© Casa do Código

Todos os direitos reservados e protegidos pela Lei nº9.610, de 

10/02/1998.

Nenhuma parte deste livro poderá ser reproduzida, nem transmitida, sem 

autorização prévia por escrito da editora, aseja quais forem os meios: fo-

tográficos, eletrônicos, mecânicos, gravação ou quaisquer outros.

Edição

Adriano Almeida

Vivian Matsui

Revisão e diagramação

Bianca Hubert

Vivian Matsui

[2015]

Casa do Código

Livro para o programador

Rua Vergueiro, 3185 – 8º andar 

04101-300 – Vila Mariana – São Paulo – SP – Brasil

www.casadocodigo.com.br


--------------------------------------------------

© Casa do Código

Todos os direitos reservados e protegidos pela Lei nº9.610, de 

10/02/1998.

Nenhuma parte deste livro poderá ser reproduzida, nem transmitida, sem 

autorização prévia por escrito da editora, aseja quais forem os meios: fo-

tográﬁcos, eletrônicos, mecânicos, gravação ou quaisquer outros.

Edição

Adriano Almeida

Vivian Matsui

Revisão e diagramação

Bianca Hubert

Vivian Matsui

[2015]

Casa do Código

Livro para o programador

Rua Vergueiro, 3185 – 8º andar 

04101-300 – Vila Mariana – São Paulo – SP – Brasil

www.casadocodigo.com.br


--------------------------------------------------

5

# COMO LER ESTE LIVRO

Do começo ao fim! Este é um livro curto e prático. Conforme o próprio 
título diz: Direto ao Ponto. Logo, você o deve ler todo, e na sequência.

O livro está estruturado em três partes: contexto, receita e apêndices.

O contexto é formado pelo prefácio e pelos capítulos Produto mínimo 
viável e Inception Enxuta. 

O prefácio fornece o contexto sobre as influências que me levaram a 
escrever este livro. É muito importante tê-lo em mente para compre-
ender a minha visão sobre o assunto.

O livro se baseia no conceito de MVP, em inglês Minimum Viable Pro-
duct. O capítulo Produto mínimo viável apresenta tal ideia com o seu 
histórico e a minha visão sobre o tema, bem como a evolução de pro-
dutos enxutos.

# PARTE I – CONTEXTO


--------------------------------------------------

6

Direto ao Ponto é uma receita, uma sequência de atividades colabo-
rativas e dinâmicas que gerarão o canvas MVP, uma representação 
visual do plano de criação e evolução do produto enxuto. Todos os 
passos desta receita estão detalhados seguindo a ordem dos capítu-
los, começando pelo capítulo 3 – O produto e terminando no capítulo 
8 – Calculando esforço, tempo e custo,

Um livro com título Direto ao Ponto obriga o autor a fazer uso do 
apêndice. Considero todo o conteúdo do livro essencial, entretanto 
ficou no apêndice o que foi acrescentado com o tempo, baseado no 
feedback dos leitores.

Apêndice A traz um exemplo real do entendimento e planejamento 
de um produto enxuto a partir da receita Direto ao Ponto aplicada em 
uma Inception superenxuta: realizada em apenas seis horas! Alguns 
leitores me relataram que primeiro leram este apêndice (disponível no 

# PARTE II – RECEITA

# PARTE III – APÊNDICES

O capítulo de Inception Enxuta explica em detalhes o formato de 
workshop colaborativo que vai ajudá-lo a entender, alinhar e planejar 
o produto enxuto a ser construído. Talvez seja o início de um projeto 
ágil em uma grande corporação, ou o alinhamento sobre o que cons-
truir em uma pequena start-up. O estilo colaborativo e dinâmico da 
Inception Enxuta é o segredo do chef desta receita.


--------------------------------------------------

7

meu blog e na revista InfoQ) e depois leram o livro a partir do início. 
Os apêndices B, C, D e E fornecem, respectivamente, o glossário dos 
termos do livro, uma classificação sobre os níveis de competência do 
facilitador, um detalhamento sobre a agenda burn-up, e algumas ati-
vidades quebra-gelo.

Boa leitura e seja bem-vindo ao grupo dos facilitadores Direto ao 
Ponto.


--------------------------------------------------

8


--------------------------------------------------

9

# PREFÁCIO

Neste livro, compartilho uma receita: uma sequência de atividades 
rápidas e efetivas para entender e planejar a criação de produtos 
enxutos, baseadas no conceito de produto mínimo viável (em inglês, 
Minimum Viable Product, MVP). 

Venho utilizando e compartilhando-a desde 2010 e percebi que, 
quanto mais o fazia, mais pessoas interessavam-se pelo assunto e 
retribuíam, compartilhando os seus resultados. O desfecho é este li-
vro, que agora está fundamentado na experiência prática de muitas 
empresas (de startups a grandes corporações) e pessoas interessa-
das em criar e evoluir produtos de forma enxuta.

Com o sucesso de tal receita, resolvi parar e refletir sobre o caminho 
que me levou a criá-la e, consequentemente, conceber este livro. 
Olhando para minha própria linha de tempo profissional (de 2000 
até 2015), destaquei os três principais movimentos que julgo terem 
influenciado na criação de ambos: Lean startup, métodos ágeis e 
design thinking.


--------------------------------------------------

10

De 2000 a 2007, vivi no Vale de Silício, na Califórnia (Estados 
Unidos), trabalhei em seis diferentes startups, e tive contato 
com inúmeras pessoas de várias outras. Nessa época, senti 
na pele o longo ciclo para criação de produtos, mesmo nas 
startups, e esse sentimento acabou afastando-me delas. Virei 
consultor e passei a trafegar por grandes corporações. Toda-
via, segui como expectador e torcedor do movimento Lean 
startup, o qual culminou com Eric Ries publicando seu incrível 
livro, The Lean Startup, em 2010.

Desde 2000, tenho utilizado (e abusado) de metodologias 
ágeis. A minha primeira sessão em uma conferência inter-
nacional foi na Object-Oriented Programming, Systems, Lan-
guages & Applications 2000 (OOPSLA), na qual apresentei 
o resultado de minha tese de mestrado sobre Orientação a 
Objetos e design patterns. Lá, tietei Kent Beck por admirá-lo 
na questão de design patterns e acabei comprando seu livro 
recém-lançado, eXtreme Programming explained. Assim, deu-
-se início um caminho sem volta: estava exposto e infectado 
pela primeira de muitas metodologias ágeis. 

Em 2006, entrei na ThoughtWorks e fui apresentado a brilhan-
tes agilistas (Martin Fowler, Jez Humble, Jim Highsmith, dentre 
vários outros). Lá, usei e divaguei sobre metodologias ágeis, 
como: Lean, Scrum, Kanban, continuous delivery etc. Depois 
de alguns anos aplicando métodos ágeis, meu entendimento 
foi além de práticas e ferramentas – princípios e valores co-
meçaram a ser naturais a mim.


--------------------------------------------------

11

Fui pela primeira vez apresentado para design thinking vários 
anos atrás, por Jeff Patton, e foi na ThoughtWorks que tive a 
oportunidade de trabalhar com ele. Fiquei impressionado com 
sua habilidade de conduzir reuniões e atividades colaborati-
vas e visuais. Aprendi e utilizei atividades sobre personas, jor-
nadas de usuários e mapeamento de história. Hoje, entendo 
que fui influenciado e segui utilizando ideias e práticas que 
foram denominadas design thinking. Isso explica (e muito) o 
estilo colaborativo e visual que adotei como ferramental bási-
co em meu trabalho, que fica evidenciado neste livro.


--------------------------------------------------

12


--------------------------------------------------

13

# AGRADECIMENTOS

Gostaria de expressar o meu muito obrigado a todos que leram as 
primeiras versões do e-book e forneceram valiosos feedbacks. Vo-
cês participaram ativamente deste projeto colaborativo e de melho-
ria contínua. A nossa experiência coletiva gerou um resultado muito 
melhor e mais fundamentado do que a minha isolada.

Muito obrigado a TC Caetano, coautor do livro FunRetrospectives. 
Nesse trabalho, TC foi também organizador de várias ideias sobre 
Inception e atividades de Inception. Junto com TC, Mauricio San-
ches e eu escrevemos um capítulo sobre Inception de uma semana 
para o livro Thoughtworks Brasil - Antologia (2014).

Aos colegas coaches e facilitadores de Inceptions e todos tipos de 
reuniões e workshops desafiadores. A Bethlem Migot, Rafael Ma-
grin, Nelice Heck, Lourenço Soares, Alexandre Klaser, dentre vários 
outros colegas da Thoughtworks Brasil por participarem e compar-
tilharem de interesses comuns nesta área de Inception e criação de 
produtos enxutos. Seguimos crescendo profissionalmente, apren-
dendo e compartilhando conhecimento juntos. 


--------------------------------------------------

14

A Alexandre Klaser, criador do nome deste livro, bem como cola-
borador em várias ideias sobre melhorias em análise de negócios e 
gerenciamento de projeto.  

À equipe de User eXperience & Design thinking da Thoughtworks 
Brasil, especialmente Natalia Arsand, Juliana Dorneles, Gabriel 
Albo, Glauber Ramos, e Tassia Spinelli. Pelas inúmeras conversas e 
compartilhamento de conhecimento nesta área.

A Gabriela Guerra, pelo exemplo de profissional e por me motivar a 
organizar e a lecionar o primeiro workshop sobre o assunto.

A Ronaldo Ferraz por motivar e acreditar no meu trabalho. Suas pa-
lavras inspiradoras alimentaram meu interesse e empenho em com-
partilhar conhecimento e escrever este livro.

A Martin Fowler pelas conversas e sessões de coaching. Muito obri-
gado pelos conselhos, direcionamento e interesse sobre este e ou-
tros assuntos relacionados. É uma honra e privilégio desfrutar do 
seu apoio e aconselhamento.

A todos colegas e amigos da Thoughtworks que me convidaram 
para facilitar Inceptions, ou a ajudar em projetos, seja para produ-
tos enxutos ou não-enxutos. Aprendi e continuo aprendendo graças 
aos desafios e conquistas que alcançamos juntos.

À minha família, em especial ao meu pai, Carlos Caroli, pelo cari-
nho e apoio ao meu trabalho. É com muito orgulho que compartilho 
cada conquista com quem sempre acompanhou e comemorou cada 


--------------------------------------------------

15

passo deste caminho. Não é apenas que o fruto não cai longe da 
árvore, mas sim que carrega em si o DNA, e desfruta da sombra e 
influência daquela.


--------------------------------------------------

16


--------------------------------------------------

17

# SUMÁRIO

Produto Mínimo Viável
21
1.1	
Origem
22
1.2	
Incrementos do MVP
23
1.3	
Pequenas hipóteses, grandes negócios
25
1.4	
Um exemplo de evolução via MVP
29

Inception Enxuta
33
2.1	
O que é uma Inception Enxuta
34
2.2	 Direto ao Ponto, a técnica
35
2.3	 Colaboração
36
2;4	 Divirta-se com quebra-gelos
37
2.5	 Paulo Pontual
38
2.6	 Colocação
39
2.7	 A sala de guerra
40
2.8	 Post-its coloridos
42
2.9	 A agenda burn-up
42
2.10	 Agenda planejada e a agenda burn-up
44
2.11	 Parque em lote
46
2.12	 Checklist para a Inception
48

Produto
49
3.1	
Escrevendo a visão do produto colaborativamente
50
3.2	 O Produto É / Não é / Faz / Não faz
53
3.3	 Esclarecendo o objetivo
55
3.4	 Entendendo os trade-offs
57

Personas
61
4.1	
Quadrantes para identificar tipos de personas
62

# 1

# 2

# 3

# 4


--------------------------------------------------

18

4.2	 Criando mapas de empatia
65

Features
69
5.1	
Descobrindo as features
70
5.2	 Entendimento técnico e entendimento de negócio
73
5.3	 Esforço e valor de negócio
77
5.4	 Features mais bem compreendidas
82

Jornada do usuário
85
6.1	
Descrevendo jornadas
87
6.2	 Features nas jornadas
90

Planejando MVPs
95
7.1	
O canvas MVP
97
7.2	 As ondas no canvas MVP
98
7.3	 As regras para cada onda
98
7.4	 Convergindo regras e jornadas
99
7.5	 Identificando MVP no canvas MVP
102

Calculando esforço, tempo e custo
105
8.1	
Detalhando a amostra de features
106
8.2	 Estimativa comparativa
111
8.3	 Definindo tamanhos
112
8.4	 Entendendo custo e tempo
113
8.5	 Tirando a média
116

# APÊNDICES

A. Exemplo de Inception Enxuta
121
9.1	
Introdução
123
9.2	 Kick-off
124
9.3	 Visão do produto
124
9.4	 O Produto É - Não é - Faz - Não faz
127
9.5	 Esclarecendo objetivos
129
9.6	 Identificando personas
129

# 5

# 7

# 6

# 8


--------------------------------------------------

19

9.7	 Descobrindo as features
132
9.8	 Features mais bem compreendidas
134
9.9	 Descrevendo jornadas
138
9.10	 Features nas jornadas
140
9.11	 O Canvas MVP
142

B. Glossário
145
10.1	 MVP
146
10.2	 Visão do produto
146
10.3	 Objetivos
147
10.4	 Personas
147
10.5	 Feature
147
10.6	 Jornada
149

C. Facilitador
151
11.1	
Níveis de competência
152

D. Agenda burn-up
155
12.1	 Os eixos da agenda
157
12.2	 Os tópicos da agenda
158
12.3	 Os intervalos de tempo
158
12.4	 A linha de escopo
159
12.5	 O ritmo da Inception
160
12.6	 Verificando o progresso
161
12.7	 Fazendo escolhas
162

E. Atividades quebra-gelo
165
13.1	 Localização geográfica
166
13.2	 Telefone visual
168
13.3	 Um Dois Ping Quatro Pong
170
13.4	 Formando triângulos
172
13.5	 Zip Zap Zoom
174
13.6	 Desembaracem-se
176
13.7	 Peças complexas
178
13.8	 Costas com costas
180
13.9	 Encontre seu par
181

Referências bibliográficas
185


--------------------------------------------------

20


--------------------------------------------------

# PRODUTO 
# MÍNIMO 
# VIÁVEL

# 1.


--------------------------------------------------

22

Produto mínimo viável (em inglês, Minimum Viable Product, MVP) é 
a versão mais simples de um produto que pode ser disponibilizada 
para a validação de um pequeno conjunto de hipóteses sobre um 
negócio.

Basicamente, você não quer desperdiçar tempo, dinheiro e esforço 
construindo um produto que não vai atender às suas expectativas. 
Para isso, é preciso entender e validar as hipóteses sobre o negó-
cio. O MVP ajuda nessa validação e no aprendizado da forma mais 
rápida possível.

Seu objetivo é somente a validação do primeiro passo do produto mí-
nimo, bem menos elaborado do que sua versão final, o que é bem 
diferente quando comparamos com produtos criados da forma tradi-
cional, que normalmente têm um período longo de criação de protóti-
po, de análise e de elaboração. O MVP foca no produto mínimo, mas 
que já é viável para verificar se o direcionamento está correto; ou seja, 
o conjunto inicial de funcionalidades necessárias para o processo de 
validação de hipóteses e aprendizagem sobre o negócio.

# ORIGEM

A ideia de MVP está originalmente vinculada aos conceitos populariza-
dos pelo estilo Toyota de manufatura enxuta (WOMACK, 1990, 2003; 
OHNO, 1988). Steve Blank (2006), um empreendedor do Vale do Si-
lício, criou uma metodologia baseada no desenvolvimento do cliente. 


--------------------------------------------------

23

Este foi o início do movimento Lean Startup, o qual teve seu ápice com 
Eric Ries (2011) e o lançamento de seu livro de mesmo nome.

Acredita-se que Eric Ries popularizou o MVP a partir da publicação 
de sua obra. Entretanto, o termo já estava em uso vários anos an-
tes do surgimento desse movimento, especialmente entre as star-
tups com seus empreendedores e investidores do Vale do Silício. A 
expressão Minimum Viable Product apareceu pela primeira vez em 
2000 em um artigo de Willian Junk (2000), de título O equilíbrio 
dinâmico entre custo, cronograma, recursos e qualidade em projetos 
de desenvolvimento de software, em português.

# INCREMENTOS DO MVP

MVP não significa que o produto não vá evoluir e incrementar suas 
funcionalidades; muito pelo contrário, sua ideia é o incremento va-
lidado e guiado pelos resultados iniciais. A correção ou a confirma-
ção do curso é que guiará os incrementos a seguir. Incrementos, 
estes, que são MVP: novos produtos mínimos adicionados aos pro-
dutos mínimos já validados. 

Mais uma vez: produtos mínimos, mas, ao mesmo tempo, viáveis 
para fazer novas verificações sobre seu direcionamento. O produto, 
agora, é mais elaborado, talvez com uma base maior de usuários, 
permitindo validar novas hipóteses ainda mais aprimoradas. É muito 
importante compreender que o MVP promove uma criação evoluti-


--------------------------------------------------

24

va. Logo, a arquitetura, bem como o ferramental da construção do 
produto, devem permitir essa característica de evolução gradual e 
contínua.

Em 2010, Jez Humble e David Farley (2010) publicaram o livro Conti-
nuous Delivery, no qual elaboram sobre um processo de entrega rá-
pido e de baixo custo, permitindo a criação incremental de produtos 
de software. Eles definem Continuous Delivery (em português, Entre-
ga Contínua) como uma disciplina de desenvolvimento de software 
que promove entregas mais rápidas e com maior frequência. 

Apesar de o livro entrar em detalhes sobre produtos de software e 
o fluxo de trabalho para sua criação, a essência da ideia de Entre-
ga Contínua é a mesma que Eric Ries recomenda em seu livro Lean 
StartUp: ciclos rápidos para validação das hipóteses.

Ciclos rápidos e frequentes permitem tempos de liberação muito 
curtos e com baixos custos de experimentação. Porém, não é fácil 
implementar esse tipo de abordagem, já que os criadores de produ-
tos no estilo MVP precisarão de estruturas e práticas diferentes da-
quelas utilizadas tradicionalmente para produtos com um ciclo lento. 

Este livro tem o foco em atividades de análise e planejamento efe-
tivo baseado em MVP. Continuous Delivery é a bíblia para entender 
o ferramental necessário para produtos de software; mesmo que, 
para outros tipos de produto, ainda devam-se aplicar as técnicas e o 
aprendizado compartilhado pelos autores Jez Humble e David Farley.


--------------------------------------------------

25

# PEQUENAS HIPÓTESES, 
# GRANDES NEGÓCIOS

O produto é construído de forma incremental com MVPs recém-
-criados sendo adicionados ao produto consolidado já existente. A 
entrega contínua e incremental proporciona o aumento do valor do 
produto ao longo do tempo, enquanto que o processo de criação de 
produto tradicional não fornece qualquer valor até o final, quando 
ele todo está pronto.

Você precisa ganhar altura? Subiria um degrau para isso?

Você precisa ganhar mais altura? Subiria mais um degrau para isso?


--------------------------------------------------

26

Você precisa ganhar ainda mais altura? Subiria outro degrau para isso?

Você precisa ganhar mais altura? Espera a construção de um elevador?

Resultado final: para subir, use a escada ou o elevador!


--------------------------------------------------


--------------------------------------------------

28

Em essência, uma ideia (ou grandes hipóteses de negócio) é se-
quenciada em uma série de hipóteses menores, mais simples e, 
logo, mais fáceis de entender. Como resultado, elas são elaboradas 
mais rapidamente e disponibilizadas no produto para o usuário final. 
Por exemplo: se houvesse uma ponte neste local, quantos pedestres 
a usariam por semana? 

Nesse caso, o usuário final (ou quem valida o MVP) fornece dados 
para a validação do incremento do produto. Isso é essencial por 
duas razões: 

Correções e mudanças podem ser feitas em 
um estágio inicial do produto, em vez de só 
aparecerem no final da concepção, reduzin-
do, assim, seu risco; 

A complexidade de análise das hipóteses é re-
duzida, e os idealizadores do produto e o usu-
ário final têm acesso antecipado a algo fun-
cional e viável. Dessa forma, as decisões dos 
próximos passos e seus incrementos são ba-
seados no próprio produto, em vez de serem 
hipóteses sobre outras hipóteses. Esse padrão 
de trabalho permite a construção de produtos 
bem elaborados, com passos pequenos, po-
rém bem fundamentados.

# 1

# 2


--------------------------------------------------


--------------------------------------------------

30

Essa figura mostra como MVP oferece validações pequenas 
ao longo do tempo, ao passo que a forma tradicional de 
criação de produtos só o validaria em sua versão final. 

Por exemplo, o trator cortador de grama (MVP 8) representa 
o produto final e o tesourão de cortar grama é o primeiro 
MVP. Existe alguma grama para cortar? Existe alguém para 
lidar com um aparelho de cortar grama? A validação das 
hipóteses conduz a evolução do produto para o próximo 
MVP. Talvez, algo mais conveniente: um aparelho de cor-
tar grama com um cabo. E se tal aparelho tivesse rodas? E 
assim por diante, até que o produto evolua de MVP a MVP.

A validação mais importante, apesar de indesejada, é a res-
posta negativa. Existe alguma grama para cortar? Não. Em 
tal caso, o tesourão não vai ser usado. E digo mais, um ex-
celente (e caro) trator de cortar grama também não o seria. 
A hipótese é falsa; portanto, um produto totalmente evolu-
ído teria sido um grande desperdício de tempo e dinheiro!

Esse exemplo ilustra como o mínimo produto viável pro-
move uma abordagem gradual em que apenas uma pe-
quena parte de uma ideia mais abrangente é tratada na-
quele tempo. Cada um desses MVPs é concebido, criado 
e preparado para ser adicionado ao produto. Em essência, 
uma ideia do produto é sequenciada em uma série de va-
lidações menores, mais simples e mais fáceis de se enten-
der, criar e validar. 


--------------------------------------------------

31

Vale a pena lembrar que, felizmente, produtos de software 
não são manufaturados. No mundo do software, um trator 
de cortar grama pode ser criado por meio da adição de 
rodas, volante, motor e cadeira a um tesourão.


--------------------------------------------------

32


--------------------------------------------------

# INCEPTION 
# ENXUTA

# 2.


--------------------------------------------------


--------------------------------------------------

35

# DIRETO AO PONTO, 
# A TÉCNICA

Durante a Inception Enxuta, são realizadas atividades dinâmicas 
para definição dos objetivos, das estratégias e do escopo do pro-
duto, bem como o mapeamento e a priorização das funcionalida-
des desejáveis para serem entregues gradualmente, construindo os 
MVPs. O principal objetivo do workshop é fazer com que a equipe 
descubra e compreenda coletivamente o que vai ser desenvolvido. 
Ao seu final, o time deve estar mais entrosado e com uma visão mais 
clara do caminho a seguir.

Direto ao Ponto é uma técnica que ajuda a entender e a planejar a 
entrega incremental de MVPs. Ela organiza ideias e recursos em um 
modelo que busca compreender a principal finalidade do produto 
ao considerar as jornadas de seus usuários, para realizar as entre-
gas incrementais de produtos viáveis. Como um livro de receitas que 
contém uma sequência de atividades rápidas e eficazes, a técnica 
vai permitir que a equipe:

Descreva a visão do produto;

Priorize os objetivos do produto;

Descreva os principais usuários, seus perfis e suas necessidades;


--------------------------------------------------

36

Entenda as principais funcionalidades;

Compreenda os níveis de incerteza, esforço e valor de negócio por 
funcionalidade;

Descreva as jornadas mais importantes dos usuários;

Crie um plano de entrega incremental do produto, impulsionado 
pelo conceito de MVP;

Estime o esforço por amostragem;

Calcule os custos e especifique datas e cronograma de entrega.

As seções a seguir exploram conceitos fundamentais para a Incep-
tion Enxuta, enquanto os próximos capítulos detalham as ativida-
des que alcançam cada uma dessas ações.

# COLABORAÇÃO

Colaboração é o ato de trabalhar em conjunto para fazer uma tare-
fa e alcançar objetivos comuns. O sucesso de uma Inception está 
diretamente ligado à capacidade do grupo envolvido em colabo-
rar efetivamente em cada atividade descrita neste livro. A Inception 
propõe um processo colaborativo de descoberta e esclarecimento 
em que as pessoas envolvidas trabalham juntas em uma sequência 


--------------------------------------------------

37

# DIVIRTA-SE COM 
# QUEBRA-GELOS

de atividades, com o objetivo de compreender opções e elaborar 
MVPs. As práticas apresentadas nos capítulos seguintes represen-
tam métodos estruturados de colaboração, buscando um ambien-
te criativo com partilha de conhecimento, aprendizagem e cons-
trução de consenso. Elas visam aumentar o sucesso da equipe e 
melhorar como ela envolve-se no esclarecimento e na resolução 
de cada passo na direção ao MVP.

Nunca subestime o poder da diversão. Por meio do divertimento e 
do riso, seus níveis de estresse diminuem significativamente e você 
estará muito mais aberto a trabalhar com outras pessoas. Quando 
você está feliz e relaxado, está muito mais receptivo para tentar coi-
sas novas e, assim, aumentar a sua participação nesse workshop 
altamente interativo: a Inception Enxuta.

Pessoas altamente envolvidas, participativas, contentes e ativas nas 
atividades colaborativas: com isso em mente, você precisa quebrar 
o gelo e elevar o estado de espírito dos participantes. Quebra-ge-
los ajudam a criar um ambiente amigável e tornar as pessoas mais 
confortáveis para participar das atividades.

Elas são rápidas, divertidas e podem ser executadas para aquecer 


--------------------------------------------------

38

a equipe e promover sua interação. São excelentes para se começar 
qualquer tipo de reunião do grupo, e ainda mais valiosas para os 
estágios iniciais de suas formações, quando as pessoas pouco se 
conhecem, o que tipicamente é o caso para Inceptions Enxutas.

Você deve selecionar uma atividade quebra-gelo coesa para o mo-
mento em questão. Nos primeiros dias, eu recomendo exercícios 
que se concentrem em compartilhamento de informações, tais 
como nomes e hobbies. Já após o almoço, você deve selecionar um 
para despertar as pessoas. Finalmente, você também deve conhecer 
os quebra-gelos que ajudam a transmitir mensagens simples, como 
“sistemas complexos são difíceis de lidar”, ou “documentação escrita 
não é o suficiente”. Além de serem divertidos e enérgicos, eles co-
municam ideias importantes.

Segue um exemplo de quebra-gelo bom para compartilhar nomes. 
No apêndice D você encontrará mais atividades e ideias.

# PAULO PONTUAL

Esta é uma atividade rápida para ajudar os membros da equipe a 
lembrarem os nomes uns dos outros. Como funciona:

Solicite aos participantes para pensarem em 
um adjetivo que comece com a mesma letra 
de seus nomes;

# 1


--------------------------------------------------

39

# COLOCAÇÃO

Forme um círculo e peça para cada participan-
te dizer seu nome com o adjetivo, um de cada 
vez (“Oi, eu sou o Paulo Pontual!”);

Depois que todos falarem, peça para que, em 
sentido horário, falem o nome e o adjetivo da 
pessoa ao seu lado;

Depois de algumas voltas, peça que os parti-
cipantes repitam o passo 3, agora no sentido 
anti-horário.

Além de darem algumas risadas e quebrarem o gelo, essa atividade 
também ajuda a equipe a associar os nomes das pessoas a algum 
adjetivo, o que torna mais fácil lembrá-los.

# 2

# 3

# 4

Não subestime o valor da interação face a face. Tecnologias ino-
vadoras, como videoconferência e documentos compartilhados, fa-
cilitam o trabalho remoto entre as pessoas. No entanto, durante a 
Inception, essa interação possibilita o árduo trabalho nas atividades. 
É a garantia de que todos estarão presentes e participativos.

Quando todos estão na mesma sala, o nível de participação aumen-
ta. Você não pode simplesmente sentar-se em um canto e virar as 


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------

42

# POST-ITS COLORIDOS

# A AGENDA BURN-UP

Faça as anotações em post-its ou cartões coloridos. Escreva e colo-
que-os ou na mesa, ou na parede. Reúna as pessoas ao seu redor, 
fale sobre eles e, então, escreva um pouco mais. Agrupe-os. Sepa-
re-os. Rasgue-os e escreva de novo. Faça uso de cores. Reorgani-
ze-os. A colaboração gerada a partir de tal aparato tão simples não 
tem como ser alcançada por qualquer alternativa digital. 

Não há substituto para as ações de escrever, reescrever, agrupar ou 
rasgar post-its coloridos. Isso promove a interação entre as pessoas 
e ajuda no processo criativo de experimentação, construindo um 
caminho, sem medo de tentar, errar ou refazer. Logo que a infor-
mação vai para o computador, ela não volta ao papel. Isso reduz a 
interação entre as pessoas, pois não há nada em cima da mesa ou 
nas paredes visíveis a todos e que possa facilmente ser rasgado, 
reagrupado ou reescrito.

A agenda burn-up (em detalhes no apêndice C) ajuda com o gerencia-
mento de tempo e escopo de um workshop de Inception. Ter a agen-
da visível constrói a confiança na gestão do tempo e no progresso das 
atividades como um todo. É uma ferramenta simples e eficaz para pla-
nejar e facilitar o workshop e, também, para chegar direto ao ponto.


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------

45

O modelo de agenda planejada apresenta dois tipos de 
sessões (em cores laranja e azul), que correspondem aos 
níveis de participação: stakeholders e membros ativos. 

Stakeholder é qualquer pessoa impactada pelo projeto. São 
pessoas altamente interessadas no direcionamento e resul-
tado da Inception, mas que não têm tempo para participar 
de todas as sessões. Elas podem ser os patrocinadores, os 
usuários finais, jurídico, vendas e marketing.

Já o membro ativo é qualquer pessoa diretamente envolvida 
pela compreensão e implementação do produto. Estas são 
as que devem participar ativamente de todas as sessões do 
workshop, podendo ser: product owners, desenvolvedores, 
testadores, gerentes de projeto e experiência do usuário. 

Note na agenda planejada que as atividades de kick-off 
e showcase do workshop estão marcadas em cor laranja, 
respectivamente no início e no final da semana. No mundo 
ideal, todos estarão presentes na sala de guerra durante a 
semana. Entretanto, raramente temos a disponibilidade de 
agenda dos stakeholders. O mínimo necessário é que eles 
participem das sessões de kick-off e showcase, nas quais 
são apresentadas as expectativas do negócio para a sema-
na, bem como o resultado obtido pelo time dedicado ao 
workshop. Os demais dias são tomados por uma sequência 
de atividades intensas, seguidas por períodos de consoli-
dação. As atividades a serem seguidas devem estar listadas 
na agenda burn-up.


--------------------------------------------------


--------------------------------------------------

47

uma parede na sala de guerra. Se o item em discussão ainda não 
estiver escrito em um post-it, faça-o e coloque-o no Parque em lote. 
Certifique-se de explicar brevemente o conceito da ferramenta, e 
retorne a atividade em questão. É importante ser bem assertiva com 
os participantes da Inception Enxuta sobre o Parque em lote:

A conversa estava desviando do foco da atividade em 
questão, e por isso tal item foi para o Parque em lote.

Este item está estacionado por agora; mas vamos voltar 
a ele mais tarde.

Todavia é igualmente importante ouvir e respeitar as opiniões, ideias 
e pensamentos dos participantes da Inception. Portanto, o Parque 
em lote deve ser utilizado conforme prometido:

De fato, no final de cada dia da Inception, você deve usar 10 minutos 
para rever os itens no Parque em lote. Desta forma, uma destas duas 
ações é tomada para cada item: (1) o item é removido do Parque em 
lote (o tema já foi abordado ou não precisa mais ser tratado); ou (2) 
o item permanece no Parque em lote para a próxima revisão.

A última revisão deve acontecer no final da Inception. Nessa última 
avaliação é muito importante esclarecer todos itens remanescentes 
e compartilhar com todos o que vai acontecer com eles.


--------------------------------------------------

48

# CHECKLIST PARA 
# A INCEPTION

A lista a seguir é projetada para auxiliar o processo de planejamento 
do workshop de Inception. Por favor, certifique-se de ter todos os 
itens programados antes de iniciar uma inception.

Participantes selecionados e convidados (stakeholders e membros 
ativos);

Facilitador experiente (ver o apêndice B);

Reserva de sala (manter a mesma sala durante o período da Incep-
tion);

Flipchart, cartões, post-it, papel A4 e canetas para todos;

Coffee break.


--------------------------------------------------

# PRODUTO

# 3.


--------------------------------------------------

50

Com a ajuda de uma visão clara 
do produto, você pode determinar 
quais e como as primeiras peças 
do seu quebra-cabeça do negócio 
se juntarão. Você deve decidir so-
bre qual característica do produto 
o caminho inicial será trilhado e 
qual será a sua estratégia de posi-
cionamento.

# ESCREVENDO A 
# VISÃO DO PRODUTO 
# COLABORATIVAMENTE

Em algum lugar entre a ideia e o lançamento, a visão do produto 
ajuda a trilhar o caminho inicial. Ela define a essência do seu valor 
de negócio e deve refletir uma mensagem clara e convincente para 
seus clientes. Essa atividade ajudará a definir colaborativamente a 
visão do produto.


--------------------------------------------------

51

Template visão do produto

Para [cliente final],
cujo [problema que precisa ser resolvido],
o [nome do produto]
é um [categoria do produto]
que [benefício-chave, razão para adquiri-lo].
Diferentemente da [alternativa da concorrência],
o nosso produto [diferença-chave].

A visão do produto, foi descrita no livro Crossing the chasm: mar-
keting and selling high-tech products to mainstream customers, de 
Geoffrey A. Moore (1999).

# COMO FUNCIONA:

Escreva o template visão do produto em um 
quadro branco ou flipchart de forma que seja 
visível para toda a equipe;

Divida a equipe em grupos menores e solicite 
que cada um deles preencha uma lacuna se-
paradamente (ou mais, dependendo do seu 
tamanho);

Reúna o resultado de cada grupo, formando 
uma única frase.

# 1

# 2

# 3


--------------------------------------------------


--------------------------------------------------

53

# O PRODUTO É / NÃO É / 
# FAZ / NÃO FAZ

A atividade É / Não é / Faz / Não faz ajuda a definir um produto. Por 
vezes, é mais fácil descrever algo pelo que tal coisa não é ou deixa 
de fazer. Ela busca clarificações ao indagar especificamente cada 
aspecto positivo e negativo sobre o produto ser ou fazer algo.

# PASSO A PASSO DA ATIVIDADE:

Divida um quadro branco ou flipchart em 
quatro áreas (É / Não é / Faz / Não faz);

Escreva o nome do produto em destaque aci-
ma dos quadrantes;

Solicite que cada participante descreva o 
produto em post-its e colocando-os nas áre-
as devidas;

Leia e agrupe as notas semelhantes.

# 1

# 2

# 3

# 4


--------------------------------------------------


--------------------------------------------------

55

# ESCLARECENDO O OBJETIVO

Cada membro da equipe deve compartilhar o que entende como 
objetivo para quem usa o produto e os vários pontos de vista devem 
ser discutidos para que se chegue a um consenso sobre o que é 
realmente importante. Essa atividade auxilia no levantamento e es-
clarecimento desses objetivos.

# PASSO A PASSO DA ATIVIDADE:

Solicite a cada membro da equipe que es-
creva, individualmente, três respostas para a 
seguinte pergunta: *Se você tiver que resumir 
este produto em três objetivos para seus usuá-
rios, quais seriam eles?*;

Solicite aos participantes que compartilhem 
o que escreveram em um _canvas_ comum, 
agrupando-os por similaridade;

Solicite à equipe que reescreva os objetivos, 
agora coletivamente. Nesse momento, ficará 
claro que alguns dos elementos listados não 
são realmente objetivos do produto, devendo, 
portanto, ser descartados. Com isso, ficará ní-
tido para a equipe qual o foco do projeto.

# 1

# 2

# 3


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------

58

# PASSO A PASSO DA ATIVIDADE:

Descreva todas as categorias relevantes para 
o produto em post-its (exemplo: segurança, 
usabilidade, escalabilidade);

Coloque as categorias no quadro branco ou flip-
chart como títulos de linhas. Em seguida, dese-
nhe uma linha horizontal para cada categoria; 

Desenhe linhas verticais (o mesmo número de 
linhas horizontais). Escrever mais (importante) 
em cima da linha, mais à esquerda, e menos em 
cima da linha, mais à direita; 

Peça aos participantes para marcar suas iniciais 
em vários post-its e colocar um por linha. A res-
trição é que cada coluna deve ter um com suas 
iniciais (por exemplo, apenas uma das catego-
rias vai ser marcada como mais importante); 

Equalize os trade-offs. Com um post-it de cor 
diferente (uma tira de post-it verde na foto 
ilustrativa), faça a marcação devida para cada 
categoria de mais a menos importante. Essa 
marcação será relativamente fácil, já que são 
considerados os post-its com os votos de todos.

# 1

# 2

# 3

# 4

# 5


--------------------------------------------------


--------------------------------------------------

60


--------------------------------------------------

# PERSONAS

# 4.


--------------------------------------------------

62

Para identificar efetivamente as funcionalidades de um sistema, é 
importante ter em mente seus usuários e objetivos. A maneira nor-
malmente utilizada para representar estes usuários é por meio de 
personas (PATTON, 2010).

Uma persona representa um usuário do sistema, descrevendo não 
só o seu papel, mas também suas necessidades específicas. Isto cria 
uma representação realística, auxiliando o time a descrever funcio-
nalidades do ponto de vista de quem interagirá com o produto final.

# QUADRANTES PARA 
# IDENTIFICAR TIPOS 
# DE PERSONAS

A seguinte atividade é utilizada para descrição de tipos de personas. 
Ela é simples, ilustrativa, divertida e rápida.

# PASSO A PASSO DA ATIVIDADE:

Solicite ao time que se divida em pares ou trios 
e entregue o seguinte template de personas 
para cada grupo;

# 1


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------

65

# CRIANDO MAPAS DE 
# EMPATIA

O mapa de empatia é um template visual para identifica-
ção e visualização de uma persona. Criado originalmente 
para análise de segmentos de consumidores, ele é uma 
excelente ferramenta para classificar, explorar e entender 
os diferentes tipos de personas.

Foi originalmente descrito por Dave Gray como um dos 
métodos da XPLANE – empresa de visual thinking fundada 
em 1993 – para compreender usuários, clientes e outros 
envolvidos no negócio. Ficou ainda mais conhecido des-
de que foi destacado no livro Business model generation, 
de Osterwalder e Pigneur (2009), como uma ferramenta 
para descobrir insights sobre os clientes.

O mapa apresenta quatro áreas principais, as quais pre-
enchem a frase: 

O que eu ____ (vejo / penso / ouço / falo)?

Além dessas quatro áreas principais, a versão original 
apresenta mais duas: as dores (pain, em inglês) e ganhos 
(gain) para tal persona.


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------

# FEATURES

# 5.


--------------------------------------------------

70

Feature é a descrição de uma ação ou interação de um usuário com 
o produto. Por exemplo: imprimir nota fiscal, consultar extrato deta-
lhado, e convidar amigos do facebook. 

A descrição de uma feature deve ser o mais simples possível. O usu-
ário está tentando fazer uma coisa. O produto dever ter uma feature 
para isso. Que feature é essa?

Dado que já temos as personas e os principais objetivos do produto. 
A seguinte pergunta ajuda com a descoberta de features:

O que precisa ter no produto para que tal persona alcance tal 
objetivo?

# DESCOBRINDO 
# AS FEATURES

A seguinte atividade é utilizada para descoberta de features. Note 
que ela depende da lista de objetivos e personas que já devem ser 
artefatos adquiridos em atividades anteriores:

# PASSO A PASSO DA ATIVIDADE:

Solicite que a equipe coloque os objetivos em 
# 1


--------------------------------------------------

71

um canvas comum, em ordem de prioridade, da 
esquerda para direita, como títulos de colunas;

Peça à equipe que coloque as personas no 
mesmo canvas, em ordem de prioridade, de 
cima para baixo, como títulos de linhas;

Promova um brainstorm de features. A discus-
são deve ser guiada para que se descubram 
quais são necessárias para atender os objetivos 
e as personas. Uma pergunta para ajudar nes-
se processo é: O que se precisa ter no produto 
para que tal persona alcance tal objetivo?.
A equipe deve guiar-se no canvas, repetindo essa pergunta para 
cada combinação de persona e objetivo, começando com os de 
mais alta prioridade. Desse modo, as candidatas a features de alta 
prioridade surgirão primeiro.

O controle de tempo é essencial para todas as atividades, mas 
esta requer atenção especial. Se um grande número de objetivos 
e personas for selecionado (nos passos 1 e 2), inúmeras features 
poderão ser levantadas pela equipe. Isso será contraprodutivo e 
pode levá-la a gastar muito tempo falando sobre as que não farão 
parte dos primeiros MVPs.
Para evitar tal cenário, é altamente recomendável que o número 
de objetivos e personas seja limitado para poucos (como três ou 
quatro principais).

# 2

# 3


--------------------------------------------------


--------------------------------------------------

73

Embora o canvas seja semelhante a uma matriz, não 
necessariamente haverá uma feature para cada in-
terseção. Pode haver múltiplas features para uma 
persona alcançar um objetivo específico, assim 
como é possível haver personas que não necessi-
tem de uma feature para determinado objetivo.

Caso sejam identificados objetivos e features que 
não atendem as necessidades de nenhuma per-
sona, estes devem ser descartados ou repensa-
dos, pois o seu valor não está claramente asso-
ciado a um usuário.

# ENTENDIMENTO TÉCNICO E 
# ENTENDIMENTO DE NEGÓCIO

Esta atividade tem o objetivo de discutir como a 
equipe se sente em relação ao entendimento técni-
co e o entendimento de negócio para cada feature. 
A partir dela, novas notas são capturadas, e discor-
dâncias e dúvidas ficam mais aparentes.


--------------------------------------------------


--------------------------------------------------

75

Solicite a um membro da equipe que leia uma 
feature em voz alta e a posicione no gráfico 
de acordo com o seu entendimento sobre ela 
(técnico e de negócio);

Questione a equipe se todos compartilham 
daquela opinião. Se alguém não concordar, 
ela deve discutir os requisitos e a tecnologia 
envolvidos de forma que haja um consenso 
sobre a feature. Tudo o que for mencionado e 
que ajude a alcançar uma melhor compreen-
são deve ser anotado e anexado nela;

Anote na feature o nível de entendimento. Por 
exemplo, a figura a seguir mostra features em 
post-it que foram colados em index cards ver-
des, amarelos ou vermelhos, indicando, res-
pectivamente, um nível alto, médio ou baixo de 
entendimento;

Para cada feature capturada anteriormente, repita os passos de 2 a 4.
No eixo X, o objetivo é verificar o entendimento da equipe em re-
lação aos desafios técnicos, às dependências e aos requisitos de 
infraestrutura. No eixo Y, a proposta é verificar a clareza sobre seu 
objetivo, o benefício para o negócio e o que deve ser feito.

Seguem alguns exemplos de features categorizadas em relação ao en-
tendimento técnico de negócio – verde, amarelo ou vermelho, respec-
tivamente, representando níveis de entendimento alto, médio e baixo.

# 2

# 3

# 4


--------------------------------------------------


--------------------------------------------------

77

Ao final da atividade, as features marcadas com um index card verme-
lho com um X representam riscos altíssimos para o projeto. Normal-
mente, a equipe decide dividi-las em pedaços menores de trabalho.

# ESFORÇO E 
# VALOR DE NEGÓCIO

Esta atividade tem o objetivo de discutir como a equipe entende o 
esforço para fazer a feature, bem como seu valor de negócio asso-
ciado. A partir dela, novas marcações serão feitas para a cada uma.


--------------------------------------------------

78

# PASSO A PASSO DA ATIVIDADE:

Crie, em um canvas comum, um gráfico, onde 
o eixo X representa o esforço (o nível de tra-
balho para fazer), e o Y, o entendimento sobre 
o valor de negócio (qual retorno ou economia 
isso vai trazer);

Solicite a um membro da equipe que leia uma 
feature em voz alta e a posicione no gráfico 
de acordo com o seu entendimento sobre ela 
(esforço e valor de negócio);

Questione a equipe se todos compartilham 
daquela opinião. Se alguém não concordar, 
ela deve discutir os requisitos e a tecnologia 
envolvidos de forma que haja um consenso 
sobre a feature. Tudo o que for mencionado e 
que ajude a alcançar uma melhor compreen-
são deve ser anotado e anexado nela;

Anote, na feature, o nível de esforço e o va-
lor de negócio. Por exemplo, a figura abaixo 
mostra features em index cards, nas quais fo-
ram adicionadas marcações de $, $$ ou $$$, 
para valor de negócio alto, muito alto e altíssi-
mo respectivamente; bem como E, EE, ou EEE, 
para nível de esforço baixo, médio e alto;

# 1

# 2

# 3

# 4


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------

# JORNADA DO 
# USUÁRIO

# 6.


--------------------------------------------------

86

A jornada do usuário descreve seu percurso por uma 
sequência de passos dados para alcançar um objetivo. 
Alguns desses passos representam diferentes pontos de 
contato com o produto, caracterizando a interação do 
usuário com ele. 

Seguindo uma abordagem simples e eficaz, a descrição 
do percurso começa por identificar um usuário e um ob-
jetivo. Ações descritas em post-its demonstram os peque-
nos passos dados no percurso para alcançar o objetivo. A 
jornada fica aparente quando eles são alinhados em uma 
ordem lógica e sequencial, representando o comporta-
mento do cliente e fluxo das interações com o produto. 

Questionamentos, acordos e desacordos conduzirão a 
conversa para a construção da jornada. Talvez, mais de 
uma opção de jornada será levantada, por exemplo: a 
jornada otimista, a realista, a pessimista, a principal, a 
excepcional caso isso, a excepcional caso aquilo etc. As 
opções vão forçar a priorização e a definição clara do 
objetivo e, com isso, o foco em algumas delas. As prio-
rizadas complementarão e ajudarão na busca do MVP. 

Seu nível de detalhamento não deve ser nem muito alto, 
nem muito baixo. Ao mesmo tempo que uma jornada 
proporciona um passo a passo da interação do usuá-
rio, ela também é uma síntese; um nível mais elevado e 
simplificado do fluxo, sem as informações redundantes 
e os detalhes mais profundos.


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------

94


--------------------------------------------------

# PLANEJANDO 
# MVPS

# 7.


--------------------------------------------------

96

Esta feature é importante?

Sempre obtive uma resposta positiva quando fiz tal pergunta. Por 
isso, não a faço mais. A pergunta mais relevante para ajudá-lo a pla-
nejar a ordem das features a serem criadas seria, então: Qual dessas 
duas é a mais prioritária?

Dessa forma, as features são priorizadas em relação umas às outras. 
Essa pergunta é muito útil e deve ser usada; entretanto, antes é ne-
cessário um ponto de partida. 

Previamente, você apontou o usuário mais importante, bem como 
a jornada preferencial. Logo, o melhor ponto de partida seria a pri-
meira feature desta jornada. Talvez, haja mais de uma nela ou em 
várias que possam ser criadas ao mesmo tempo. Daí sim, em tal 
cenário, você deve perguntar qual das duas features em questão 
é prioritária.

Felizmente, nas etapas anteriores, alguns parâmetros já foram adi-
cionados às features, como: o valor de negócio ($, $$ ou $$$), o es-
forço (E, EE ou EEE) e a marcação de nível de incerteza (cartão verde 
para baixo, amarelo para médio ou vermelho para alto). Eles o aju-
darão com o seu planejamento e com as suas prioridades relativas. 

Então, qual é a combinação mínima de features que devem ser dis-
ponibilizadas para validar um pequeno conjunto de hipóteses sobre 
o negócio? Agora é a hora de visualizar e conceituar o primeiro MVP 
e seus incrementos subsequentes.


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------

99

# CONVERGINDO 
# REGRAS E JORNADAS

Regra 3: Uma onda não pode conter três features, somente em car-
tões amarelos e vermelho.
Regra 4: A soma de esforço das features não pode ultrapassar 5 Es.
Regra 5: A soma de valor das features não pode ser menos de 4 $s.
Regra 6: Uma onda tem de conter no mínimo 2 features.

A regra 1 limita o número de features que estão sendo trabalhadas 
ao mesmo tempo. Isso evita o acúmulo de features parcialmente 
completas, aumentando o foco para as poucas features priorizadas 
por onda. Já as regras 2, 3 e 4 evitam um período de trabalho dese-
quilibrado com muita incerteza, ou muito esforço; e as 5 e 6 garan-
tem o foco constante na entrega de alto valor para o negócio.

Regras simples são adicionadas ao template com as ondas. Agora, 
basta buscar a primeira feature da primeira jornada. Aí você deve 
buscar a próxima. Respeitando as regras, você decide se tal feature 
entra na onda n ou n+1. 

Caso você fique em dúvida entre duas delas que respeitam as re-
gras, basta responder a pergunta: Qual delas é mais prioritária?. 

A seguir, mostro uma sequência com duas fotos, na qual a primeira 


--------------------------------------------------


--------------------------------------------------

101

Duplicar ou utilizar o mesmo post-it/cartão?

Uma feature com suas marcações está posicionada 
em uma jornada. Você está prestes a pegar tal car-
tão e colocá-lo em outro template, o canvas MVP. 
Além das informações descritas nele, o seu posi-
cionamento no template carrega mais dados, sendo 
que isso também ocorre com a feature na jornada e 
no Canvas MVP.  Neste momento, você acaba per-
guntando-se: duplico ou utilizo o mesmo cartão? 

Minha sugestão é que tire uma foto antes de qualquer 
coisa para, então, considerar a replicar o cartão, desde 
que isso não deixe a atividade mais lenta e o ambiente 
mais confuso (com inúmeros papéis coloridos).

Adiante, uma foto típica de um time utilizando o canvas MVP. Note 
seu envolvimento e como ele posiciona-se em frente ao template. 
Nesse momento, todos estão bem alinhados em relação às prin-
cipais jornadas e suas features (com suas marcações de incerteza, 
valor de negócio e esforço).


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------

# CALCULANDO 
# ESFORÇO, 
# TEMPO 
# E CUSTO

# 8.


--------------------------------------------------

106

Os incrementos de MVP e as ondas do canvas MVP 
deixam visíveis e tangíveis as entregas do produto. 
Mesmo assim, ainda precisamos definir o esforço, tem-
po e custos associados a cada MVP.

A sequência de atividades até este momento, bem 
como as regras do canvas MVP, geram ondas de ta-
manho similar. Isso simplifica a estimativa do produto e 
seus MVPs, pois nos permite usar seu tamanho médio. 
Em vez de tentar detalhar todas as features em relação 
ao esforço, ao tempo e ao custo, você as utilizará ape-
nas como amostras para entender tais parâmetros.

# DETALHANDO A 
# AMOSTRA DE FEATURES

O tamanho das ondas é parecido. Logo, escolha três delas e use-as 
para gerar informação detalhada de esforço, tempo e custo. Três 
são suficientes para dar uma boa noção de tais parâmetros e gerar 
uma média efetiva.

# PASSO A PASSO DA ATIVIDADE:

Selecione três ondas a serem detalhadas; 
# 1


--------------------------------------------------


--------------------------------------------------

108

Ao selecionar as ondas de amostragem (passo 1), lembre-se que, 
neste momento, você está interessado na estimativa do todo e no 
seu tamanho médio, e não no detalhamento do trabalho em si. Por 
isso, as ondas a serem escolhidas devem prover boa combinação 
do nível de incerteza (marcados pelas cores dos cartões), bem como 
uma boa variação na soma dos níveis de esforço (marcados com Es).

As primeiras ondas são boas candidatas, pois tal detalhamento 
será útil não apenas para estimar o todo, mas também para ajudar 
na descrição dos pedaços menores para a construção das featu-
res iniciais do MVP.

O pedaço menor (passo 3) deve ser algo que faz sentido para o 
time. Times de desenvolvimento de software que seguem a meto-
dologia Scrum costumam usar histórias do usuário como tais pe-
daços menores (SABBAGH, 2013; SCHWABER & BEEDLE, 2001; 
COHN, 2004; HELM & WILDT, 2015). Já outros times preferem 
chamá-los de tarefas e descrevê-los sem um formato predefinido. 
O mais importante é que o time esteja confortável com o deta-
lhamento desses pedaços menores e, logo, consiga estimar seu 
tamanho e esforço.

Seguem dois exemplos de dois times diferentes detalhando uma 
feature em pedaços menores. No primeiro exemplo, os pedaços 
menores seguem o padrão de histórias de usuário, enquanto no 
segundo, os pedaços menores são descritos como tarefas.


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------

111

Ao final dessa atividade, as features selecionadas como amostra es-
tarão detalhadas com suas várias tarefas.

# ESTIMATIVA COMPARATIVA

Esta atividade é usada para o entendimento do esforço relativo das 
tarefas. 

# PASSO A PASSO DA ATIVIDADE:

Em uma canvas comum (tipicamente, uma mesa 
ou no chão), identifique um extremo como sen-
do + (mais), e outro como sendo – (menos);

Selecione duas tarefas e faça a seguinte pergun-
ta: Como essa tarefa compara-se (em esforço) 
com esta outra? Mais, menos ou parecido?;

Coloque ambas as tarefas no canvas, indican-
do como se comparam em relação ao nível de 
esforço. Coloque uma ao lado da outra, caso 
ambas exigirem o mesmo nível, ou uma abaixo 
da outra, caso uma requeira mais esforço;

Enquanto houver tarefas a serem comparadas, 

# 1

# 2

# 3

# 4


--------------------------------------------------

112

coloque-as no canvas ao lado de uma outra e 
repita os passos 2 e 3.

Ao final da atividade, todas as tarefas estarão no canvas, onde po-
dem ser compreendidas em relação ao nível de esforço e como se 
comparam umas com as outras.

# DEFININDO TAMANHOS

Esta atividade é muito simples e essencial para ser efetiva com o 
tempo e gerar números para cálculo. 

# PASSO A PASSO DA ATIVIDADE:

Escreva em post-it os seguintes tamanhos de 
camisa: pequeno, médio, grande e extragrande;

Coloque essa marcações de tamanho no can-
vas, sendo o pequeno mais próximo à extremi-
dade de menos esforço e o extragrande mais 
próximo à extremidade de mais esforço;

Defina as demarcações entre os tamanhos e 
reposicione as tarefas para ficar claro seu ta-
manho.

# 1

# 2

# 3


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------

115

Ao final da atividade, todas as tarefas possuirão uma 
estimativa de tempo e custo. Por exemplo, o resultado 
mostrado na figura anterior foi obtido em uma instância 
dessa atividade: um dia para tarefas pequenas, três dias 
para médias, e quatro para tarefas grandes.
As respostas de tempo vão influenciar o resultado final. 
Por isso, seja bem enfático em relação à pergunta. Se 
possível, compare com trabalhos passados, e tente en-
tender a motivação e a capacidade das pessoas respon-
dendo tal pergunta.

Desenvolvedores não gostam de responder tal pergunta:

Quanto tempo leva para uma pessoa completar 
tal tarefa? 

Por isso, é muito importante que todos estejam muito à 
vontade com a descrição da tarefa. Caso haja qualquer 
desconforto em relação a uma tarefa, reescreva-a e consi-
dere quebrá-la em pedaços ainda menores. 
Outra forma de fazer tal pergunta é colocá-la no plural:


--------------------------------------------------

116

Considere um par de desenvolvedores. Um sabe 
mais do negócio, outro menos. Um mais sênior, 
outro mais júnior. Um mais experiente na tecno-
logia, outro mais novato. Quanto tempo leva para 
um par de desenvolvedores completar tal tarefa?

Na minha experiência, todos ficam mais à vontade dando tal res-
posta considerando pares de desenvolvedores atuando juntos para 
completar uma tarefa.

# TIRANDO A MÉDIA

A partir do entendimento de esforço da atividade anterior, somamos 
o tempo estimado para cada tarefa de cada feature, e com isso so-
mamos a duração prevista por features de cada onda escolhida do 
canvas MVP. Dessa forma, chegamos a uma média de esforço para 
cada onda, definido por pessoa e por unidade de tempo. 

As duas fotos a seguir demonstram como o cálculo foi realizado 
para um time. Elas mostram, respectivamente, as ondas escolhidas 
para amostragem e o cálculo realizado para obter a média do tempo 
estimado por onda.


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------

120

Podemos escolher trabalhar com um par de de-
senvolvedores e entregar uma onda de features 
em, aproximadamente, um mês (ou 20 dias úteis). 
Outra opção seria dobrar o custo mensal, tendo 
dois pares de desenvolvedores entregando, apro-
ximadamente, duas ondas mensais.


--------------------------------------------------

# EXEMPLO DE 
# INCEPTION 
# ENXUTA

# apêndice A


--------------------------------------------------

122

“Gostaria de ver um exemplo completo de uma Inception Enxuta”. 
Este foi um pedido recorrente que recebi de leitores deste livro. 
Imagino que a leitura seja mais fácil para quem já participou de um 
workshop, ou de uma Inception no estilo Direto ao Ponto. Por mais 
que o livro explique os itens da receita e o passo a passo de cada 
atividade, entendo que ainda seja válido demonstrar um exemplo 
completo. É como seguir uma receita para fazer um brownie especial 
de chocolate após ter experimentado o tal brownie especial de cho-
colate. É isto que venho compartilhar neste capítulo.

Por motivos de confidencialidade das empresas que me contrata-
ram para facilitar as tais  Inceptions Enxutas, não posso comparti-
lhar o resultado das atividades para os seus produtos. Muitos deles 
começaram como produtos enxutos, com seus MVPs incrementais, 
e hoje são produtos diferenciadores nos seus ramos de atuação. 
Por tal motivo, selecionei um exemplo real, bem ilustrativo, e que 
pode ser compartilhado. Este produto enxuto foi idealizado durante 
um workshop Direto Ao Ponto em uma conferência nacional. Como 
havia mais de 20 participantes, o produto foi idealizado e comparti-
lhado entre todos os presentes.

Como o workshop duraria 8 horas, a agenda semanal típica de 
uma Inception Enxuta foi compactada de forma a caber em poucas 
horas. A agenda burn-up foi essencial para manter todos alinha-
dos sobre quão rápido seria o ritmo que teríamos que seguir para 
aquele evento.

Reitero que o conteúdo e fotos que seguem é de um exemplo ilus-
trativo realizado em um dia, portanto, provavelmente reduzido na 


--------------------------------------------------


--------------------------------------------------

124

os nomes. Começamos o dia com bastante energia e dando boas 
risadas.

# KICK-OFF

Em vez do kick off típico, geralmente realizado por stakeholders fa-
lando sobre o produto ou ideia a ser concebida durante a Incep-
tion Enxuta, o kick off do workshop de simulação teve outro estilo. 
Perguntei aos participantes quem tinha ideia de produto e queria 
explorá-lo como exemplo do workshop durante o dia. Três ideias 
foram apresentadas, e em seguida todos participantes votaram em 
qual queriam utilizar.

# VISÃO DO PRODUTO

O produto mais votado era um app para peladeiros. Aquelas pes-
soas que gostam de jogar futebol com seus amigos do trabalho, da 
academia, ou de algum grupo que esteja marcando uma pelada.

Para (1) ajudar os três idealizadores a descrever suas ideias, (2) fo-
mentar a participação de todos, e (3) prover uma votação com um 
bom entendimento de cada opção, utilizamos o template de visão 
do produto para cada ideia de produto, em grupos de sete pessoas. 


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------

128

Veja a transcrição dos textos nos post-its da foto:

O produto é...

•	
app

•	
app mobile

•	
multiplataforma

•	
facilitador para organizar 

peladas

•	
gratuito

•	
gratuito

O produto faz...

•	
marca jogos (agenda)

•	
agenda quadras

•	
lista partidas

•	
localiza peladas próximas

•	
geolocalização

•	
avisos sobre ocorrências

•	
notifica usuários

•	
rating usuário

•	
guarda reputação

O produto não é...

•	
FB, Twitter, Whatsapp

•	
site

•	
site

•	
não é chat

•	
messenger (chat)

O produto não faz...

•	
organiza jogos

•	
define times por ordem de 

pedido

•	
organiza jogos e times

•	
cria times

•	
gerencia pagamentos

•	
pagamento online da pelada

•	
não faz jogos privados

•	
não organiza campeonatos

•	
campeonatos


--------------------------------------------------

129

# ESCLARECENDO OBJETIVOS

Após as atividades Visão do Produto e O Produto É - Não é - Faz - Não 
faz, realizamos a atividade para esclarecer os objetivos do produto. 
Neste momento, foi solicitado a todos os participantes que compar-
tilhassem o entendimento que tinham para os três principais obje-
tivos do produto. Cada um escreveu três post-its. Ao recolhê-los e 
colocá-los em grupos de afinidade, foram identificados três princi-
pais objetivos para o produto:

Encontrar peladas
Divulgação
Opções de partidas

# IDENTIFICANDO 
# PERSONAS

Após um bom entendimento do produto, foi a hora de mudar o foco 
e buscar um bom entendimento em relação às personas, os usuário 
do sistema. Para isso, utilizamos o template dos quadrantes para 
identificar os tipos de personas. Com tal template, criamos apelidos 
para cada tipo, descrevemos seus respectivos perfis, suas caracte-
rísticas comportamentais e suas necessidades específicas. Mesmo 
com o tempo curto, todos os participantes participaram de grupos 


--------------------------------------------------


--------------------------------------------------

131

Apelido
Gordinho bom de bola
Perfil
28 anos
casado
jogador frustrado
bancário
formado
Comportamento

reclamão
competitivo
assíduo
exigente com a quadra
passa horas nas redes sociais
Necessidade

jogar toda semana com qualquer pessoa e local
mas procura partidas de alto nível
jogar à noite nos fins de semana


--------------------------------------------------


--------------------------------------------------

133

vas para que as features sejam descobertas. Com isso, o facilitador 
pode promover um brainstorm sobre as features:

O que precisa ter no sistema para que tal persona alcance tal 
objetivo?

Com essa pergunta, a discussão é guiada para que se descubram 
quais features são necessárias para atender objetivos e personas. 
Elas são anotadas em post-it e colocadas no canvas. A pergunta é 
repetida para cada combinação de persona e objetivo, com isso, 
priorizamos os principais objetivos e as principais personas. 

Segue a transcrição dos post-its de features:

consulta de peladas com geolocation
consulta de peladas sem geolocation
classificação de quadras
rankear um jogador
detalhamento da pelada (local, horário e data)
ranking dos jogadores (visualização)
detalhes financeiros da pelada
cadastro do peladeiro
cadastro da pelada
convidar amigo para pelada
filtro detalhado
módulo de notificação
confirmação de presença


--------------------------------------------------

134

notificação de pelada confirmada
notificação de pelada cancelada
cancelar presença
 cancelar pelada

# FEATURES MAIS 
# BEM COMPREENDIDAS

As features foram descobertas, entretanto foram 
aceitas sem ressalvas, sem perder muito tempo 
entendendo-as em detalhes, fazendo anotações 
e conversando sobre incertezas, esforço e valor 
para o negócio. Entretanto, essas conversas e in-
formações mais detalhadas são muito úteis para 
uma melhor compreensão e planejamento de cria-
ção de produtos enxutos. As atividades e gráficos 
Entendimento técnico e entendimento de negócio e 
Esforço e valor de negócio buscam tais informações 
de forma rápida e eficiente.


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------

139

Seguem dois exemplos de jornadas:

Gordinho bom de bola: cadastra uma pelada

1.	
acorda cedo para o trabalho

2.	
exagera no café da manhã

3.	
chega ao trabalho às 9:00 am

4.	
durante uma reunião decide fazer alguma atividade física

5.	
no almoço convence um amigo do trabalho a jogar futebol no fim do dia

6.	
liga e reserva uma quadra

7.	
abre o easy-bola

8.	
cadastra a pelada para 8:00 pm naquele mesmo dia

9.	
coloca informação da quadra

10.	 envia convite para os amigos

Amigo do trampo: aceita convite para uma pelada

1.	
acorda atrasado para o trabalho

2.	
come uma barra de cereal no metrô

3.	
chega no trabalho as 9:30 am

4.	
vai para a academia na hora do almoço

5.	
durante uma reunião, recebe uma notificação do easy-bola

6.	
verifica as informações da pelada

7.	
verifica a classificação da quadra

8.	
confirma sua presença na pelada

9.	
sai da reunião para outra reunião

10.	 às 5:14 pm recebe a confirmação da pelada


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------

144

Segue a transcrição do canvas MVP do easy-bola apresentado na 
foto, com seus MVPs identificados e suas respectivas features.

Feature
MVP
cadastro da pelada
1
cadastro do peladeiro
1
consulta de peladas sem geolocation
1
confirmação de presença
2
detalhamento da pelada (local, horário e data)
2
cancelar presença
2
cancelar pelada
3
módulo de notificação
3
notificação de pelada confirmada
3
notificação de pelada cancelada
3
detalhes financeiros da pelada
3
convidar amigo para pelada
4
ranking dos jogadores (visualização)
4


--------------------------------------------------

# GLOSSÁRIO

# apêndice B


--------------------------------------------------

146

Segue uma breve lista de termos utilizados neste livro. Cada um dos 
conceitos é explorado em detalhes nos capítulos. Entretanto, julgo ne-
cessário um esclarecimento em âmbito geral para esses termos desde 
o início.

Essa lista deve estar visível durante o workshop de Inception. Sugiro 
que imprima esse glossário e coloque-o na parede da sala de guerra.

# MVP

# VISÃO DO PRODUTO

O produto mínimo viável – em inglês, Minimum Viable Product 
(MVP) – é a versão mais simples de um produto que pode ser dis-
ponibilizada para o negócio. Ele determina quais são as funciona-
lidades mais essenciais para que se tenha o mínimo de produto 
funcional que possa agregar valor para o negócio (produto míni-
mo) e que possa ser efetivamente utilizado e validado pelo usuário 
final (produto viável).

A visão do produto é uma breve descrição de para onde você quer 
levar sua ideia do produto.


--------------------------------------------------

147

# OBJETIVOS

# PERSONAS

# FEATURE

Um objetivo é um resultado desejado previsto para o produto. Com-
preender os objetivos do produto serve como uma ferramenta eficaz 
para estabelecer um acordo do que ele deve ter para cumprir a visão 
do produto.

Uma persona representa um usuário do sistema, descrevendo não 
só o seu papel, mas também suas características e necessidades 
específicas. Isto cria uma representação realística de usuários, au-
xiliando o time a descrever funcionalidades do ponto de vista de 
quem interagirá com o produto final.

Feature é um agrupamento de funcionalidades semelhantes. Isso 
o ajuda com a compreensão sobre o requisito como um todo, bem 
como das suas partes menores e complementares. O entendimen-
to de feature variará de time para time. O importante é que tal 
agrupamento faça sentido para sua equipe e que estejam alinha-


--------------------------------------------------

148

dos com os objetivos do produto.

# ENTENDIMENTO TÉCNICO DA FEATURE

O entendimento da feature de acordo com os desafios técnicos e 
os requisitos de infraestrutura. Se ao responder: Você já fez isso 
antes? Você sabe como fazê-lo?, você obtiver uma resposta posi-
tiva bem firme, isso indica elevado nível de entendimento técnico.

# ENTENDIMENTO DE NEGÓCIO DA 
# FEATURE

A clareza do objetivo da feature, o benefício para o negócio e o 
que deve ser feito. O que fazer? Uma resposta direta e clara indica 
um alto nível de concordância.

# NÍVEL DE INCERTEZA DA FEATURE

O nível de incerteza da feature refere-se ao grau em que ela é in-
certa, a partir do ponto de vista do entendimento de negócio e do 
entendimento técnico. Isso é indicado pela cor do cartão de índice: 
verde, amarelo ou rosa, indicando níveis baixo, médio ou alto de 
incerteza, respectivamente.


--------------------------------------------------

149

# ESFORÇO DA FEATURE

O nível do trabalho que precisa ser feito para a feature. O entendi-
mento da equipe de acordo com a dificuldade e o trabalho que vai 
ser necessário para completá-la.

# VALOR DO NEGÓCIO DA FEATURE

O valor de negócio associado à feature; uma medida do negócio 
sobre o valor previsto para ela. Qual é o retorno no investimento 
– ROI (Return On Investment) – ou a economia que a feature vai 
trazer? A resposta deve variar entre alto, muito alto ou altíssimo.

# JORNADA

A jornada do usuário descreve o seu percurso por uma sequência 
de passos dados para alcançar um objetivo. Alguns desses passos 
representam diferentes pontos de contato com o produto, caracte-
rizando sua interação com ele.


--------------------------------------------------

150


--------------------------------------------------

# FACILITADOR

# apêndice C


--------------------------------------------------


--------------------------------------------------

153

Facilitador iniciante: pessoas que estão parti-
cipando do workshop Inception pela primeira 
vez;

Facilitador intermediário: pessoas que já par-
ticiparam, mas ainda não facilitaram nenhuma 
atividade durante um workshop Inception;

Facilitador aprendiz: pessoas que já participa-
ram e facilitaram uma ou mais das atividades 
realizadas em workshops;

Facilitador: pessoas que já facilitaram um 
workshop e sentem-se seguras para fazê-lo;

Facilitador avançado: pessoas que já facilita-
ram pelo menos cinco workshops Inception e 
sentem-se seguras para serem coachs de facili-
tadores aprendizes;

Facilitador evangelista: pessoas que já facilita-
ram mais de dez e, atualmente, estão compar-
tilhando as técnicas para o público interessado 
em workshops Inception.

# 1

# 2

# 3

# 4

# 5

# 6


--------------------------------------------------

154


--------------------------------------------------

# AGENDA 
# BURN-UP

# apêndice D


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------

158

# OS TÓPICOS DA AGENDA

Os tópicos e atividades a serem realizadas devem ser agrupados de 
forma que suas durações sejam semelhantes. Por exemplo, se sua 
agenda tem 5 tópicos e você espera que os tópicos 1 e 2 levem meia 
hora cada, os 3 e 4 levem uma hora e o 5 leve duas horas, então 
você deve considerar ter os tópicos agrupados da seguinte forma: 

Tópico 1 e 2 
Tópico 3 
Tópico 4 
Tópico 5.1 
Tópico 5.2 

Note que, dessa forma, cada agrupamento tem uma expectativa 
de duração semelhante. Outro aspecto importante é que eles si-
gam uma ordem cronológica: primeiro vamos cobrir isso, depois 
aquilo, e assim por diante. Sua sequência e atividade devem ser 
claramente definidas.

# OS INTERVALOS DE 
# TEMPO

Os intervalos de tempo no eixo horizontal devem ser simétricos, co-


--------------------------------------------------

159

# A LINHA DE ESCOPO

meçando no início da Inception e terminando no seu final esperado. 
Nos exemplos de agenda burn-up, tal intervalo é de meia hora. Sua 
unidade de tempo (minutos, horas ou dias) deve estar relacionada à 
duração esperada para os tópicos e suas atividades. 

Considere que você está construindo uma agenda para um 
workshop de 5 dias com 10 tópicos. Usar intervalos de tempo com 
base em horas seria muito pequeno. Nesse caso, intervalos de um 
ou meio dia seria mais apropriado.

Uma informação importante da agenda burn-up é a linha de esco-
po: a linha horizontal acima do último tópico planejado. Ela define 
claramente se e quando novos tópicos foram adicionados ou remo-
vidos durante a Inception. Ela também permite que você visualize a 
interseção dessa linha horizontal para a vertical, que representa o 
fim do workshop. 

Tudo em discussão deve ser um tópico. Se novos temas surgem, eles 
devem ser adicionados à lista de tópicos, e a linha de escopo deve 
ser ajustada. Dessa forma, a nova linha permite identificar facilmen-
te quando eles estão sendo adicionados, o que afetará o tempo de 
conclusão da Inception. 

O ato de adicionar um novo tópico é um sinal importante de que o 


--------------------------------------------------


--------------------------------------------------


--------------------------------------------------

162

Quando as duas linhas se encontram, a agenda planejada estará 
completa. A distância entre elas é uma medida poderosa de quão 
perto você está de completar a agenda planejada. 

Verificar regularmente o progresso é uma parte importante da ges-
tão do tempo. Há dois movimentos básicos para os post-its e ambos 
são horizontais: 

O tempo mudou; o post-it com uma grande 
seta que representa a hora atual deve ser mo-
vido para a direita até a posição que represen-
ta a hora atual;

A discussão sobre um tópico da agenda termi-
nou; o respectivo post-it deve ser movido para 
a direita para a hora atual. 

Esse mecanismo de movimento dos post-its permite identificar, de 
imediato, um desvio na duração esperada para os tópicos da agen-
da. Assim que constatado, esse problema deve ser discutido e ações 
corretivas devem ser tomadas ainda em um estágio inicial, e não 
quando for tarde demais.

# 1

# 2

# FAZENDO ESCOLHAS

Considere o instantâneo da agenda burn-up representado na próxi-


--------------------------------------------------


--------------------------------------------------

164


--------------------------------------------------

# ATIVIDADES 
# QUEBRA-GELO

# apêndice E


--------------------------------------------------

166

Quebra-gelo são atividades que servem para aquecer e promover 
a interação do grupo. São um ótimo começo para qualquer reunião 
de equipe, e muito valiosos para fases iniciais de formação de times 
e Inceptions Enxutas. Uma atividade, chamada Paulo Pontual, já foi 
demonstrada no capítulo 2: Inception Enxuta.

Este apêncide traz mais nove atividades, completando uma dezena 
de atividades quebra-gelo para sua Inception Enxuta. Tais atividades 
foram cedidas do site e livro Fun Retrospectives [CAROLI e CAETA-
NO, 2014].

# LOCALIZAÇÃO GEOGRÁFICA

Esta atividade é ótima para quebrar o gelo e também ajuda os mem-
bros da equipe a saberem um pouco sobre cada um. 

# COMO FUNCIONA:

Explique aos participantes que cada um será 
uma localização geográfica (por exemplo, seu 
país, cidade ou bairro);

Mostre onde é o Norte e o Sul na sala;

Peça a cada participante para ir para onde ele 

# 1

# 2

# 3


--------------------------------------------------

167

se localiza, fazendo, um mapa o mais realista 
possível;

Depois que todos estiverem em seus lugares, 
peça a um voluntário desenhar um mapa re-
presentando a sala.

# 4

Desenho ilustrativo: localização geográfica


--------------------------------------------------

168

# TELEFONE VISUAL

Telefone visual é um ótimo estímulo para deixar todos engajados e 
promover uma discussão sobre comunicação e suas interpretações.

# COMO FUNCIONA:

Divida o grupo maior em conjuntos de três pes-
soas (um ou dois grupos podem ter 4 pessoas);

Coloque três post-its e uma caneta na frente de 
cada um;

Peça para todo mundo escrever uma frase (no 
post-it) e, então, coloque um post-it em branco 
em cima do primeiro (neste ponto, apenas o au-
tor da frase a conhece);

Todo mundo passa o post-it para o lado, no 
sentido horário;

Cada um lê a frase do post-it à sua frente e 
cria um desenho no post-it em branco, repre-
sentando-a;

Todo mundo passa o post-it para o lado no sen-
tido horário;
# 6

# 5


--------------------------------------------------

169

Em um novo post-it, cada pessoa escreve uma 
frase sobre o desenho a sua frente e coloca em 
cima do conjunto de post-its (agora, este tem 
três: um com a frase original, um com o dese-
nho e um com a nova frase);

Todos passam os post-its para o lado no sen-
tido horário (para os grupos de três pessoas, o 
conjunto deve parar na frente do autor da pri-
meira frase);

Abra o conjunto de post-its para que todos pos-
sam ver as frases e seus desenhos respectivos.

# 7

# 8

# 9

Desenho ilustrativo: telefone visual


--------------------------------------------------

170

Normalmente, os participantes riem e divertem-se comparando os 
desenhos e as frases.

Essa é um ótima atividade com uma mensagem sutil sobre co-
municação (visual e escrita), contexto e interpretações. Ela é uma 
adaptação de uma atividade que aprendemos em um workshop UX 
(User eXperience), dos meus queridos amigos Natalia Arsand, Glau-
ber Ramos, Juliana Dorneles e Gabriel Albo. Eles a aprenderam no 
workshop da IDEO, Human Centered Design.

# UM DOIS PING 
# QUATRO PONG

Esta é uma atividade curta para começar uma reunião em um bom 
clima e deixar os participantes engajados.

# COMO FUNCIONA:

Peça para os participantes formarem um círculo;

Os participantes devem decidir em que senti-
do seguir (horário ou anti-horário);

Alguém começa dizendo qualquer número po-

# 1

# 2

# 3


--------------------------------------------------

171

sitivo que não seja múltiplo de 3 ou 5; 

A próxima pessoa, seguindo a direção deci-
dida por todos, mentalmente adiciona 1 ao 
número. Então:

Se o número não é múltiplo de 3 ou 5: ela diz o número.
Se o número é múltiplo de 3: diz ping e bate palma.
Se o número é múltiplo de 5: diz pong e pula.

# 4

Desenho ilustrativo: 

um dois ping quatro pong


--------------------------------------------------

172

Para grandes grupos, é recomendado remover uma pessoa dele 
caso ela erre ou acuse alguém erroneamente. Logo, todos estarão 
rindo e torcendo para os que permanecerem no círculo.

# FORMANDO TRIÂNGULOS

Esta atividade é um ótimo _energizer_ com uma mensagem valiosa, 
sendo muito útil para começar uma conversa sobre equipes auto-
-organizadas. Ela é divida em duas partes.

# COMO FUNCIONA:

Primeira parte

Peça aos membros do grupo para andarem in-
dividualmente em uma direção aleatória;

Depois de um tempo, diga a palavra mágica 
“triângulo”: cada membro do grupo terá que 
achar outras duas pessoas e formar um triân-
gulo equilátero (cada um é um vértice do tri-
ângulo e deve apontar o braço em direção às 
outras duas pessoas, representando os outros 
vértices. Cada pessoa é um vértice de apenas 
um triângulo);


--------------------------------------------------

173

Cronometre quanto tempo levou para o grupo 
formar os triângulos.

# 1

# 2

# 3

# 3

Desenho ilustrativo: formando triângulos

Segunda parte

Selecione uma pessoa para ser o orientador 
do grupo;

Peça aos membros do grupo para andar em 
uma direção qualquer;

Depois de um tempo, diga a palavra mágica 
“triângulo”: o orientador do grupo tem de for-
mar triângulos equiláteros com todos os mem-


--------------------------------------------------

174

bros do grupo (incluindo ele mesmo em um 
dos triângulos);

Cronometre quanto tempo levou para o grupo 
formar os triângulos.

A primeira parte mostra um grupo auto-organizado; a segunda, um 
grupo guiado por um organizador.

Normalmente, a formação do triângulo auto-organizado é mais 
rápida que sua contrapartida, e a equipe sente-se mais engajada 
na atividade.

Ela foi feita por Heitor Roriz (https://twitter.com/hroriz), um co-
lega e coach de equipes. Deixo aqui meus parabéns a ele por 
aplicar uma atividade divertida que ajuda a promover a discussão 
sobre um conceito essencial para equipes ágeis bem-sucedidas: 
a auto-organização.

# 4

# ZIP ZAP ZOOM

Este é um bom início para reuniões, especialmente para novas equi-
pes. Traz energia para a sala e a dinâmica da atividade ajuda os 
participantes a lembrar os nomes uns dos outros.


--------------------------------------------------

175

# COMO FUNCIONA:

Peça ao time para formar um círculo e a cada 
participante para fechar suas mãos, enquanto 
apontam com seus dedos indicadores.

Explique os comandos Zip, Zap e Zoom.

Peça para um participante fazer o primeiro 
movimento, dizendo um dos comandos ver-
bais e escolhendo a direção inicial (horário ou 
anti-horário).

Os comandos:

Zip: aponte para a pessoa exatamente ao seu lado, mantendo a di-
reção anterior.

Zap: aponte para a pessoa exatamente ao seu lado, mudando a di-
reção anterior.

Zoom: aponte para qualquer pessoa no círculo, dizendo seu nome. O 
receptor deve decidir a direção para o próximo movimento na sua vez.

Quando um participante executar um comando errado, um que não 
existe ou apontar para a direção errada em um comando zip/zap, 
ele deve ser removido do círculo.

# 1

# 2

# 3


--------------------------------------------------

176

Desenho ilustrativo: zip zap zoom

Essa atividade não é apenas um bom estímulo, mas também dá aos 
participantes foco e os ajuda a lembrar os nomes uns dos outros.

# DESEMBARACEM-SE

Desembaracem-se é um ótimo estímulo para movimentar as pes-
soas e passa uma mensagem muito interessante sobre achar uma 
solução em uma situação complicada.


--------------------------------------------------

177

# COMO FUNCIONA:

Peça ao grupo para formar um círculo (o tama-
nho do grupo tem de ser mais que seis pessoas. 
Para grupos muito grandes, separe em meno-
res, com aproximadamente 12 pessoas cada);

Peça para todo mundo colocar as mãos para 
cima;  

Dê as instruções para se embaraçarem: Com 
sua mão direita, pegue a mão esquerda de al-
guém. Com sua mão esquerda, pegue a mão di-
reita de alguém. Você não pode pegar a mão de 
pessoas ao seu lado.  

Peça ao grupo para se desembaraçar sem sol-
tar as mãos e tentar formar um círculo.
# 4

# 1

# 2

# 3

Desenho ilustrativo: desembaracem-se


--------------------------------------------------

178

O grupo vai pular as mãos, alternar-se e achar uma saída, seja for-
mando um ou mais círculos. Às vezes, é impossível desembaraçar-
-se. Neste cenário, peça ao grupo para remover uma pessoa. As 
mãos que ficarem livres devem conectar-se com a pessoa remanes-
cente no grupo embaraçado.

# PEÇAS COMPLEXAS

Peças complexas é um ótimo _energizer_ para fazer as pessoas in-
teragirem enquanto conversam sobre sistemas complexos e peças 
interconectadas.

# COMO FUNCIONA:

Todos ficam em pé e andando.
Cada pessoa pensa em duas outras pessoas.
Sem dizer nomes, cada pessoa deve ficar 
igualmente distante das duas pessoas em 
quem pensou. Isso deve levar um minuto, en-
quanto elas se movem.
Depois que todos pararem, peça para a pes-
soa mais alta do grupo ir a um canto da sala.
# 4

# 1

# 2

# 3


--------------------------------------------------

179

Peça para todos encontrarem suas distâncias 
iguais de novo.
# 4

Desenho ilustrativo: peças complexas

Aprendi esta atividade com Bethlem Migot. Ela a usava como ener-
gizer durante um workshop de análise. A atividade deixou todos 
energizados antes de ela ter uma breve conversa sobre sistemas 
complexos, mudanças e requerimentos interconectados. Vale apon-
tar que ela funciona melhor em grupos de dez a trinta pessoas.


--------------------------------------------------

180

# COSTAS COM COSTAS

Costas com Costas é uma atividade enérgica e divertida que passa 
uma mensagem forte e simples sobre trabalho colaborativo.

# COMO FUNCIONA:

Diga para os participantes acharem um par 
com altura e peso parecidos com o seu.
Peça para todos sentarem-se no chão, com os 
pares um de costas para o outro.
Peça para os pares entrelaçarem os braços, 
enquanto ficam de costas um para o outro.
Diga para todos que o objetivo é ficar em pé, 
mantendo braços e costas juntos.
# 4

# 1

# 2

# 3

Desenho ilustrativo: 

costas com costas


--------------------------------------------------

181

# 1

# 2

# 3

Essa atividade é muito divertida e fará as pessoas rirem. Normal-
mente, poucos pares conseguirão ficar em pé rapidamente, en-
quanto outros terão dificuldade. Considere não fazê-la se você 
perceber que algum participante não é capaz de ficar em pé, ou 
que não gostará de sentar-se no chão.

# ENCONTRE SEU PAR

Este é um energizer muito divertido para mover as pessoas e fazê-
-las rir.

# COMO FUNCIONA:

Conte o número de participantes (um número 
par de participantes é necessário, então deci-
da se participará ou não baseando-se nisso).
Divida o número de participantes em dois para 
decidir quantos animais existirão (se forem 20 
participantes, então existirão 10 animais dife-
rentes).
Para cada animal, escreva o nome em dois 
post-its.


--------------------------------------------------

182

Distribua os post-its para os participantes e 
diga a eles não os mostrarem para ninguém.
Peça para todo mundo andar pela sala.
Diga a todos para cobrirem os olhos com as 
mãos, fazerem o som do animal e tentarem 
descobrir onde está seu par.

# 4

# 5

# 6

Desenho ilustrativo: encontre seu par


--------------------------------------------------

183

Aprendi essa atividade com Bethelm Migot. Confesso que demorei 
um pouco para usá-la, mas decidi tentar depois de vê-la sendo usa-
da várias vezes e, então, perceber como as pessoas gostavam. Ape-
nas recomendo cuidado com diferenças culturais e tenha certeza 
que os participantes estão acostumados com energizers.


--------------------------------------------------

184


--------------------------------------------------

# REFERÊNCIAS 

# BIBLIOGRÁFICAS


--------------------------------------------------

186

BLANK, Steve G. The four steps to the epiphany: successful strategies 
for products that win. 2. ed. K&S Ranch, 2013.

CAROLI, Paulo et al. Thoughtworks Antologia Brasil: Histórias de 
aprendizado e inovação. São Paulo: Casa do Código, 2014.

CAROLI, Paulo e CAETANO, Tainã. Fun Retrospectives: activities and 
ideas for making agile retrospectives more engaging. LeanPub, 2014. 
Disponível em  www.FunRetrospectives.com.

COHN, Mike. User stories applied: for agile software development. 
Indiana: Addison-Wesley Professional, 2004.

HELM, Rafael; WILDT, Daniel. Histórias de Usuário — Por que e como 
escrever requisitos de forma ágil?. Porto Alegre: Wildtech, 2015. Dis-
ponível em  http://www.wildtech.com.br/historias-de-usuario

HUMBLE, Jez; FARLEY, David. Continuous delivery. Indiana: Addison-
-Wesley Professional, 2010.

MOORE, Geoffrey A. Crossing the chasm: marketing and selling hi-
gh-tech products to mainstream customers. New York: Harper Busi-
ness Essentials, 1999.

OHNO, Taiichi. Toyota production system: beyond large-scale pro-


--------------------------------------------------

187

duction. London: Productivity Press, 1988.

OSTERWALDER, A.; PIGNEUR, Y. Business model generation: a han-
dbook for visionaries, game changers, and challengers. Amsterdam: 
OSF, 2009.

PATTON, Jeff. Pragmatic personas. StickyMinds, jan. 2010. Disponí-
vel em http://www.stickyminds.com/article/pragmatic-personas.

RIES, Eric. The Lean startup: how today’s entrepreneurs use conti-
nuous innovation to create radically successful businesses. Crown 
Publishing, 2011.

SABBAGH, Rafael. Scrum: gestão ágil para projetos de sucesso. São 
Paulo: Casa do Código, 2013.

SCHWABER, Ken; BEEDLE, Mike. Agile software development with 
Scrum. New York: Pearson, 2001.

WILLIAM, S. Junk. The dynamic balance between cost, schedu-
le, features, and quality in software development projects. Moscow: 
Computer Science Department, University of Idaho, SEPM-001, 
abr. 2000. Disponível em http://www.researchgate.net/publica-


--------------------------------------------------

188

tion/267550205_The_Dynamic_Balance_Between_Cost_Sche-
dule_Features_and_Quality_in_Software_Development_Projects

WOMACK, James P.; JONES, Daniel T.; ROOS, Daniel. The machine 
that changed the world: the story of lean production. New York: Har-
per Perennial, 1990.

WOMACK, James P.; JONES, Daniel T. Lean thinking: banish waste 
and create wealth in your corporation. London: Productivity Press, 
2003.

