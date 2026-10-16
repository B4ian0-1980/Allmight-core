---json
{
  "id": "ruby_on_rails_coloque_sua_aplica__o_web_nos_trilhos_1",
  "title": "Ruby on Rails Coloque sua aplicação web nos trilhos",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Arquivo Original:** `Ruby on Rails Coloque sua aplicação web nos trilhos.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "aplica",
    "coloque",
    "linguagens",
    "nos",
    "php",
    "rails",
    "ruby",
    "sua"
  ],
  "perguntas_tipo": [
    "Como utilizar Ruby on Rails Coloque sua aplicação web nos trilhos?",
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

# Ruby on Rails Coloque sua aplicação web nos trilhos

> **Arquivo Original:** `Ruby on Rails Coloque sua aplicação web nos trilhos.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 2

© Casa do Código
T odos os direitos reservados e protegidos pela Lei nº9.610, de 10/02/1998.
Nenhuma parte deste livro poderá ser reproduzida, nem transmitida, sem auto-
rização prévia por escrito da editora, sejam quais forem os meios: fotográﬁcos,
eletrônicos, mecânicos, gravação ou quaisquer outros.
Casa do Código
Livros para o programador
Rua Vergueiro, 3185 - 8º andar
04101-300 – Vila Mariana – São Paulo – SP – Brasil

## Página 5

tasa do tódigo
ígradecimentos
Monsters are realn and ghosts are real toop￿ey live inside usn and sometimesn they
winp
– Étephen }ing
vste livro não existiria sem a ajuda dos meus grandes amigos –atheus sodo\
àillian –olinari\ Éérgio Échezar e âinícius ázêda\ que me acompanharam nesse
processo quase todos os dias\ revisando\ criticando e opinando minuciosamente o
conteúdo desse livro_ –uito obrigadoQ
–uito obrigado também a família tasa do tódigo e taelum\ pela oportunidade
de escrever esse livro e pelos ensinamentos\ especialmente ao rdriano rlmeida\ pelo
difícil trabalho de colocar ordem às minhas palavras_
rgradecimentos especiais também ao xáÁá]Éø Xxrupo de ásuários Áuby de
Éão øauloY\ à ølataformaÍ ec e aos amigos do zt–t]áÉø \ pois se sei alguma coisa\
devo tudo a eles_
rgrade ço também a minha família e amigos\ pela for ça e por tolerarem meses
sem notícias enquanto me mudo para outro país_
øor ￿m\ agradeço principalmente a você leitor\ por investir seu tempo a aprender
uma tecnologia que eu pessoalmente gosto tanto_ vspero sinceramente que seja uma
jornada divertida e lucrativa ao mesmo tempoQ
i

## Página 7

tasa do tódigo Éumário
Sumário
￿ Introdução ￿
￿_￿ •ova edi ção\ atualizado para Áails￿Q ___________________ ￿
￿_￿ øara quem é este livro ____________________________ ￿
￿_￿ ”rganiza ção _________________________________ ￿
￿_￿ Éocorro\ estou perdidoQ –e ajudeQ_____________________ ￿
￿ õonhecendo a aplica ção ￿
￿_￿ rrquitetura de aplica ções web _______________________ ￿
￿_￿ Áecursos ao invés de páginas ________________________ ￿
￿_￿ Áecursos no tolcho_net ___________________________ ￿
￿_￿ tonhecendo os componentes _______________________ ￿
￿_￿ ”s modelos __________________________________ ￿
￿_￿ tontrole ____________________________________ ￿￿
￿_￿ rpresenta ção _________________________________ ￿￿
￿_￿ Áotas ______________________________________ ￿￿
￿_￿ Éuporte ____________________________________ ￿￿
￿_￿￿ tonsidera ções ￿nais _____________________________ ￿￿
￿ Primeiros passos com Rails ￿￿
￿_￿ znstalação do Áails ______________________________ ￿￿
￿_￿ xerar o alicerce da aplica ção ________________________ ￿￿
￿_￿ ”s ambientes de execu ção _________________________ ￿￿
￿_￿ ”s primeiros comandos ___________________________ ￿￿
￿_￿ ”s arquivos gerados pelo sca ￿old _____________________ ￿￿
iii

## Página 8

Éumário tasa do tódigo
￿ Implementação do modelo para o cadastro de usuários ￿￿
￿_￿ ” usuário ___________________________________ ￿￿
￿_￿ vvite dados errados_ waça validações ___________________ ￿￿
￿ Tratando as requisições W eb ￿￿
￿_￿ Áoteie as requisições para o controle ___________________ ￿￿
￿_￿ zntegre o controle e a apresentação ____________________ ￿￿
￿_￿ tontrole o massoassignment ________________________ ￿￿
￿_￿ vxibição do per￿l do usuário ________________________ ￿￿
￿_￿ øermita a edição do per￿l __________________________ ￿￿
￿_￿ Áeaproveite as apresentações com partials ________________ ￿￿
￿_￿ –ostre os erros no formulário _______________________ ￿￿
￿_￿ ton ￿gure a ação raiz XrootY ________________________ ￿￿
￿ Melhore o projeto ￿￿
￿_￿ “i ção obrigatóriak sempre aplique criptogra￿a para armazenar senhas ￿￿
￿_￿ tomo adicionar plugins ao projetop ____________________ ￿￿
￿_￿ ásando hasúsecureúpassword no modelo ________________ ￿￿
￿_￿ –igra ção da tabela users __________________________ ￿￿
￿_￿ rutomatizando tarefas de manuten ção com rake ____________ ￿￿
￿_￿ –elhoria de templates e tÉÉ ________________________ ￿￿
￿_￿ Írabalhe com layout e templates para melhorar sua apresenta ção _ _ _ ￿￿
￿_￿ ” que é o rsset øipelinep __________________________ ￿￿￿
￿_￿ triando os novos stylesheets ________________________ ￿￿￿
￿_￿￿ weedback em erros de formulário _____________________ ￿￿￿
￿_￿￿ uuplica ção de lógica na apresentação nunca mais_ áse os yelpers _ _ ￿￿￿
￿ Faça sua aplicação falar várias línguas ￿￿￿
￿_￿ ” processo de internacionaliza ção Xz￿￿nY_________________ ￿￿￿
￿_￿ Íraduza os templates ____________________________ ￿￿￿
￿_￿ vxtrak alterar o idioma do site _______________________ ￿￿￿
iv

## Página 9

tasa do tódigo Éumário
￿ O cadastro do usuário e a con ￿rmação da identidade ￿￿￿
￿_￿ vntenda o rction–ailer e use o –ailtatcher ______________ ￿￿￿
￿_￿ Í emplates de email\ eu preciso delesp ___________________ ￿￿￿
￿_￿ –ais emails e a con ￿rmação da conta de usuário ____________ ￿￿￿
￿_￿ ám pouco de callbacks para realizar tarefas pontuais __________ ￿￿￿
￿_￿ Áoteamento com restrições _________________________ ￿￿￿
￿_￿ vm resumo __________________________________ ￿￿￿
￿ Login do usuário ￿￿￿
￿_￿ Írabalhe com a sessão ____________________________ ￿￿￿
￿_￿ tontroles e rotas para o novo recurso ___________________ ￿￿￿
￿_￿ Éessões e cookies _______________________________ ￿￿￿
￿_￿ tonsultas no banco de dados _______________________ ￿￿￿
￿_￿ vscopo de usuário con ￿rmado _______________________ ￿￿￿
￿￿ õontrole de acesso ￿￿￿
￿￿_￿ yelpers de sessão ______________________________ ￿￿￿
￿￿_￿ •ão permita edi ção do per￿l alheio ____________________ ￿￿￿
￿￿_￿ Áelacionando seus objetos _________________________ ￿￿￿
￿￿_￿ Áelacione quartos a usuários ________________________ ￿￿￿
￿￿_￿ “imite o acesso usando relacionamentos _________________ ￿￿￿
￿￿_￿ vxibição e listagem de quartos _______________________ ￿￿￿
￿￿ ívalia ção de quartosl relacionamentos muitos para muitos e organização
do código ￿￿￿
￿￿_￿ Áelacionamentos muitos]para]muitos __________________ ￿￿￿
￿￿_￿ Áemovendo objetos sem deixar rastros __________________ ￿￿￿
￿￿_￿ triando avalia ções com pitadas de r{rã _________________ ￿￿￿
￿￿_￿ uiga adeus a regras complexas de apresenta çãok use presenters _ _ _ _￿￿￿
￿￿_￿ j®uery e Áailsk fazer requisi ções r{rã ￿cou muito fácil ________ ￿￿￿
￿￿_￿ –édia de avalia ções usando agregações __________________ ￿￿￿
￿￿_￿ rplica ções modernas usam fontes modernas ______________ ￿￿￿
￿￿_￿ vu vejo estrelas ] usando tÉÉ e {avaÉcript para melhorar as avalia ções ￿￿￿
￿￿_￿ vncerrando __________________________________ ￿￿￿
v

## Página 10

Éumário tasa do tódigo
￿￿ Polindo o õolchonnet ￿￿￿
￿￿_￿ waça buscas textuais apenas com o Áails _________________ ￿￿￿
￿￿_￿ áÁ“s mais amigáveis através de slugs ___________________ ￿￿￿
￿￿_￿ øaginação de dados de forma descomplicada ______________ ￿￿￿
￿￿_￿ ápload de fotos de forma simples _____________________ ￿￿￿
￿￿_￿ toloque a aplica ção no ar com o yeroku _________________ ￿￿￿
￿￿ Próximos passos ￿￿￿
Índice Remissivo ￿￿￿
óibliogra ￿ a ￿￿￿
â ersãok ￿￿_￿_￿￿
vi

## Página 11

t ￿￿￿￿￿￿￿ ￿
zntrodução
Quemn de três milêniosn q Não é capaz de se dar conta q Vive na ignorâncian na
sombran q À mercê dos diasn do tempop
– xoethe
Ée você desenvolve para a à eb\ provavelmente já ouviu falar sobre Áuby on
Áails_ ” Áuby on Áails Xou também apenas “Áails”Y é um framework openosource
para desenvolvimento de aplicações web\ criado por uavid yeinemeier yansson Xou
“uyy”Y_ ” framework\ escrito na linguagem Áuby\ foi extraído de um produto de
sua empresa\ o sasecamp® Xhttpk‘‘basecamp_comY em￿￿￿￿_
uesde então ele ￿cou muito famoso\ levando também a linguagem Áuby\ ante]
riormente apenas conhecida no {apão e em poucos lugares dos vstados ánidos\ ao
mundo todo_ –as por que cresceu tantop ” que a linguagem e o framework trouxe]
ram de novo para sair do anonimato e praticamente dominar o mercado de startups
nos vstados ánidos e no mundop
®uanto ao Áails\ na época em que foi lan çado\ trouxe uma visão diferente ao
desenvolvimento à eb_ •aquele momento\ desenvolver para à eb era cansativo\ os

## Página 12

￿_￿_ •ova edi ção\ atualizado para Áails￿Q tasa do tódigo
frameworks eram complicados ou resultavam em sistemas difíceis de se manter e de
baixa qualidade_
” uyy\ ao desenvolver o sasecamp\ pensou principalmente nos seguintes as]
pectosk
• “tonvention over con ￿guration” \ ou convenção à con ￿guraçãok ao invés de
con￿gurar um conjunto de arquivos ã–“\ por exemplo\ adota]se a conven ção
e apenas muda]se o que for necessáriol
• “uont Áepeat é ourself ” \ ou “não se repitaRk nunca você deve fazer mais de uma
vez o que for necessário Xcomo checar uma regra de negócioYl
• rutoma ção de tarefas repetidask nenhum programador deve perder tempo em
tarefas repetitivas e sim investir seu tempo em resolver problemas interessan]
tes_
vsses conceitos são amplamente explorados no clássico ￿e Pragmatic Programo
mer” From Journeyman to Master [ ￿]\ leitura recomendada_ vsta soma de tecnolo]
gias e práticas são bastante prazerosas de se trabalharl é possível realizar muito com
pouco tempo e você verá\ capítulo a capítulo\ como essas ideias são representadas
em todos os aspectos do framework_
￿n￿ N￿￿ ￿ ￿￿￿￿￿￿l ￿￿￿￿￿￿￿￿￿￿ ￿￿￿￿ R￿￿￿￿￿￿
•a primeira edi ção\ tínhamos duas partes\ a primeira\ na qual víamos uma intro]
dução a Áuby e\ na segunda\ cobríamos Áails_ •essa edi ção\ vamos fazer uma coisa
diferente_ â ou assumir que você\ leitor\ já sabe Áuby\ e vamos cobrir Áuby on Áails
￿\ recentemente lançadoQ Éão muitas novidades\ e portanto vamos dedicar o livro
completamente ao Áails_ vste livro também possui uma revisão completa do texto e
do conteúdo técnico\ com a colaboração dos leitores da edição anterior_
Ée você não sabe Áuby\ recomendo que você adquira o livro “Áubyk rprenda
a programar na linguagem mais divertida” \ de “ucas Éouza_ â ocê pode comprar
a sua cópia em formato físico ou digital no site da tasa do tódigok httpk‘‘www_
casadocodigo_com_br‘products‘livro]ruby_
￿n￿ P￿￿￿ ￿￿￿￿ ￿ ￿￿￿￿ ￿￿￿￿￿
” objetivo deste livro é apresentar um pouco da linguagem Áuby e aprender os pri]
meiros passos a desenvolver com o framework Áuby on Áails_ –ais além\ vamos
￿

## Página 13

tasa do tódigo tapítulo ￿_ zntrodução
aprender a desenvolver aplicativos com Áails_ rlgumas vezes usaremos inclusive
componentes feitos em Áuby puro_ vsses momentos são muito importantes para
aprendermos também algumas boas práticas_
Í endo isso em mente\ este livro serve para pessoas quek
• {á leram a primeira edi ção do livro\ mas querem conhecer as novidades da
nova versão do Áailsl
• {á conhecem as versões anteriores do Áails\ mas quer ￿car por dentro das mu]
danças do frameworkl
• {á conhecem Áails\ mas não estão confortáveis em como fazer aplica ções bem
organizadasl
• {á conhecem Áails super ￿cialmente\ mas querem aprimorar conhecimentos e
boas práticas_
￿n￿ O￿￿￿￿￿￿￿￿￿￿
r primeira parte do livro é dedicada a entender o contexto que o Áuby on Áails traba]
lha_ vssa é a parte teórica\ na qual vamos entender quais são os principais conceitos
por trás do framework_ â amos ver também\ em alto nível\ quais são os componentes
do Áails e como eles se relacionam_
r segunda parte é onde vamos fazer a aplica ção com Áails_ øasso a passo\ vamos
implementar uma aplica ção do início ao ￿m e\ durante a constru ção de cada fun]
cionalidade\ aprender como juntar as partes do framework_ â amos comparar o que
existia nas versões anteriores e o que veio na nova versão_ â amos revisitar funciona]
lidades\ aprimorando]as\ e mostrar como é o processo de cria ção de uma aplica ção
real\ de forma que você aprenda uma das possíveis maneiras de construir suas apli]
cações no futuro_
â amos construir um aplicativo chamado tolcho_net_ ” tolcho_net é um site
para você publicar um espaço sobrando na sua casa para hospedar alguém por uma
ou mais noites_ ” site vai terk
• tadastro de usuário\ com encripta ção de senhal
• “ogin de usuáriosl
• vnvio de emailsl
￿

## Página 14

￿_￿_ Éocorro\ estou perdidoQ –e ajudeQ tasa do tódigo
• znternacionaliza çãol
• øublica ção e administração de quartosl
• rvalia ção de quartos e rankingl
• susca textuall
• URL slugsl
• áploads e thumbnails de fotos_
• ueploy da aplica ção no yeroku
vmbora este livro tenha sido construído de forma que a leitura progressiva seja
fácil\ ele pode servir como consulta_ â amos dividir o sistema que será construído
em algumas funcionalidades principais e desenvolvê]las individualmente em cada
capítulo_
￿n￿ S￿￿￿￿￿￿ l ￿￿￿￿￿ ￿￿￿￿￿￿￿￿M￿ ￿￿￿￿￿￿
rcompanhado desse livro\ existe uma lista de discussões no Google Groups\ locali]
zado em httpk‘‘colcho_net‘lista_ wique à vontade para mandar dúvidas sobre o seu
progresso com o livro\ ou sobre qualquer coisa relacionada com Áails_ •ela\ eu e ou]
tros leitores voluntários poderão te ajudar com qualquer aspecto relacionado a Áuby\
Áails e ao livro_ â ocê pode mandar sugestões\ críticas e correções ao livro nessa lista_
￿

## Página 15

t ￿￿￿￿￿￿￿ ￿
tonhecendo a aplica ção
Para cada fato existe um conjunto in￿nito de hipótesesp Quanto mais você observan
mais você enxergap
– Áobert øirsig\ em êen and the rrt of –otorcycle –aintenance
rntes de come çarmos\ você sabe qual a diferen ça entre um framework e uma
bibliotecap ®uando usamos uma biblioteca\ nós programadores escrevemos nosso
código\ chamando a biblioteca quando necessário_ r camada entre a biblioteca e o
nosso código é bastante distinta_
” mesmo não acontece quando usamos um framework_ øara se ter uma ideia\
muitas vezes o ponto inicial do sistema não é um código que você escreve_ •osso
código faz o intermédio com diversas outras bibliotecas que compõem oframework\
de forma que o resultado torna]se mais poderoso do que a soma das partes_
” Áuby on Áails não é diferente_ vle é um framework usando uma estrutura
chamada –ât -- Model View íontroller \ bastante conveniente para a construção de
aplicativos à eb_ ” Áails também é usado por muitos desenvolvedores já há bastante
tempo\ portanto já foi testado em diversas situa ções\ como alta carga\ ou grande

## Página 16

￿_￿_ rrquitetura de aplica ções web tasa do tódigo
número de usuários_ É fácil começar com Áails pois ele faz muito trabalho por você\
mas se aprofundar no Áails te dá ainda mais poder_
É muita coisa para aprender\ mas não se preocupe\ este livro está em seu poder
justamente para facilitar esta tarefa_ â amos então ver como vamos modelar nossa
aplicação e em seguida vamos ver como o Áuby on Áails vai nos ajudar a construí]la_
￿n￿ í ￿￿￿￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿￿￿ ￿￿￿
tonstruir aplica ções bem feitas em Áuby on Áails é um pouco mais complicado do
que simplesmente criar páginas atrás de páginas_ r razão disso é que ele é prepa]
rado para criar aplica ções modernas e arrojadas_ zsso signi ￿ca que não somente
deve responder yÍ–“ aos usuários\ mas também responder de maneira adequada
para aplicações ricas em clientoside\ interagindo com frameworks como sackbone_js
Xhttpk‘‘backbonejs_org‘Y \ vmber_js Xhttpk‘‘emberjs_com‘Y ou outros_
O ￿￿￿ ￿￿￿ ￿￿￿￿￿￿￿￿￿￿ ￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿m￿￿￿￿￿
uepois da repopulariza ção do {avaÉcript com o uso intensivo de
r{rã\ os browsers tem se tornado muito mais poderosos do que antiga]
mente\ inclusive com os benefícios incorporados pelo yÍ–“ ￿_ Í endo
isso em mente\ programadores estão criando aplica ções cada vez mais
complexas\ executando grande parte\ ou até mesmo totalmente no brow]
ser_
•os últimos anos\ diversos frameworks tem sido lan çados\ tal como
os mencionados anteriormente_ uessa forma\ existem aplica ções à eb
que a parte de backoendtornou]se uma camada de persistência que está
totalmente independente da apresentação ￿nal ao usuário_
￿n￿ R￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿
øara que nossas aplicações ￿quem elegantes\ precisamos parar de pensar na maneira
antiquada de se criar aplica ções à eb cheias de páginas e intera ções complexas en]
tre si\ e pensarmos em recursos_ É uma mudan ça não trivial\ mas vamos usar este
pensamento durante o livro todo\ então até o￿nal\ você ￿cará mais confortável com
essa ideia_
￿

## Página 17

tasa do tódigo tapítulo ￿_ tonhecendo a aplica ção
Ée você já ouviu falar ou sabe o que é ÁvÉÍ X Representational State Transfer\
ou Íransferência de estado de representa çãoY\ entender como vamos usar recursos
para modelar nossa aplica ção será bem mais fácil_ Ée você quiser se aprofundar no
assunto\ recomendo a leitura do livro Rest in Practice [￿]_
￿n￿ R￿￿￿￿￿￿￿ ￿￿ õ ￿￿￿￿￿ n￿￿￿
ám recurso\ em uma aplica ção web\ é qualquer coisa que uma aplicação pode servir
aos seus usuários_ øor exemplo\ em uma rede social\ recursos podem ser mensagens\
fotos\ vídeos_ áma aplicação web\ quando serve um recurso\ permite que você inte]
raja com ele_ øor exemplo\ é possível criar novas mensagens\ listá]las ou até mesmo
deletá]las_ ám recurso também possui uma apresenta ção\ como por exemplo um
documento yÍ–“ ou um objeto em {É”•_
” tolcho_net é um aplicativo em que os seus usuários podem mostrar quartos
vagos\ ou até um colchonete que pode ser usado em sua sala em troca de uma grana
e quem sabe fazer novas amizades_
rssim\ o primeiro recurso que podemos identi ￿car é o “®uarto” _ vm nosso sis]
tema\ será possível listar quartos\ exibir detalhes de um quarto\ criar um novo quarto\
editar um quarto já existente e\ por ￿m\ removê]lo_
Áecursos assim são fáceis de serem mapeados\ pois estão diretamente ligados a
uma unidade lógica do sistema_ øorém\ existem recursos que são menos óbvios_ ám
exemplo de recurso não tão trivial é o recurso “Éessão” _ øoderemos criar uma sessão
ou destruí]la\ porém nada mais além disso_
vm sistemas ÁvÉÍ \ ações com recursos são mapeados em duas partesk um verbo
yÍÍø Xuma opera çãoY\ uma áÁ“ Xidenti￿cação do recursoY_ øodemos também ter
uma representação\ porém opcional_ â eja os seguintes exemplosk
￿

## Página 18

￿_￿_ tonhecendo os componentes tasa do tódigo
O ￿￿￿ ￿￿￿ ￿￿￿￿￿￿ HTTP￿
â erbos yÍÍø são a ções que podem ser executadas em um recurso
identi￿cado por uma áÁ“_ r implementa ção do comportamento ￿ca a
critério do servidor\ não existe um padrão_ ”s verbos usados no Áuby on
Áails sãok
• GET ] para retornar um recurso especí ￿co ou uma coleçãol
• POST ] para enviar um novo elemento à uma cole çãol
• PUT ] para alterar um elemento existentel
• DELETE ] para remover um elemento_
• GET /rooms.html k â erbo GET na áÁ“ /rooms mapeia para a listagem de
todos os quartos\ com uma representação em yÍ–“l
• POST /rooms k â erbo POST na áÁ“ /rooms mapeia para a inser ção de
mais um novo quarto na cole ção de quartos\ e sua representação é dada pelo
cabeçalho yÍÍø ‘tontent]type’l
• DELETE /rooms/123 k â erbo DELETE na áÁ“ /rooms/123 mapeia para
a remoção do quarto cujo identi ￿cador único é “ ￿￿￿” \ sendo a representação
irrelevante\ pois não há a transmissão de dados\ apenas uma ação_
” Áails considera esses conceitos em seu design\ portanto\ se seguirmos esses
conceitos\ o Áails nos ajuda bastante e de quebra ganhamos facilidade ao usar frao
meworks de clientosidequando necessário_
vssa é a visão externa da arquitetura de aplica ções à eb_ â amos entrar então na
arquitetura interna_
￿n￿ õ ￿￿￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿￿￿￿
” Áuby on Áails é um framework que adota o padrão de arquitetura chamado
Model-View-Controller (MVC) \ ou –odelo\ rpresenta ção e tontrole_
￿

## Página 19

tasa do tódigo tapítulo ￿_ tonhecendo a aplica ção
Modelos possuem duas responsabilidadesk eles são os dados que sua aplica ção
usa\ normalmente persistidos em um ou mais banco de dados Xseu per￿l de usuário\
por exemploY_ vles também fazem parte da regra de negócio\ ou seja\ cálculos e
outros procedimentos\ como veri ￿car se uma senha é válida ou o fechamento de
uma fatura_
” õontrole é a camada intermediária entre a à eb e o seu sistema_ vle traduz
os dados que vem de representa ções web Xsejam por parâmetros na áÁ“\ formulá]
rios enviados ou dados {É”• enviados por uma aplica ção clienteY e repassa para os
modelos\ que vão fazer o trabalho pesado_ vm seguida\ preparam os resultados de
forma a serem usados na camada de rpresenta ção_
r ípresenta ção é como o aplicativo mostra o resultado das operações e os dados_
•ormalmente podem ser uma bela página usando as novas tecnologias de tÉÉ ￿ e
yÍ–“ ￿ a até representações de objetos em {É”• ou ã–“_
￿n￿ O￿ ￿￿￿￿￿￿￿
®uando criamos aplica ções Áuby on Áails\ basicamente usamos um componente
chamado ActiveRecord_ ” ActiveRecord é uma implementa ção de Objecto
RelationaloMapping\ ou seja\ uma biblioteca que faz o mapeamento de estruturas re]
lacionais Xleia]se É®“ e bancos de dados relacionaisY a objetos Áuby\ transformando\
por exemplo\ chaves estrangeiras em relacionamento entre objetos através de méto]
dos_
” ActiveRecord internamente usa uma biblioteca bastante poderosa cha]
mada Arel_ tom o uso do Arel o ActiveRecord consegue transformar cha]
madas de métodos Áuby em complexas consultas É®“ e depois mapear de volta em
objetos Áuby_ zsso tudo é muito conveniente\ veja alguns exemplosk
+oom:_ll
@ qmõml? *rooms*:[ n+)p *rooms*
+oom:whyry{4low_tion h- / 'qão %_ulo 'c '+io xy ó_nyiro '3}
@ qmõml? *rooms*:[ n+)p *rooms* s#m+m *rooms*:*low_tion*
@ o( { 'qão %_ulo 'c '+io xy ó_nyiro '}
rlém disso\ o ActiveRecord traz diversas facilidades para integra ção com o
restante de uma aplicação web\ através do ActiveModel_ ” ActiveModel é um
componente que inclui diversas ferramentas para valida ção de atributos\ callbacks
￿

## Página 20

￿_￿_ tontrole tasa do tódigo
em momentos oportunos Xcomo antes de atualiza ção ou cria çãoY\ integração com
formulários\ tradução de atributos\ entre outras_
”s modelos não necessariamente precisam ser objetos ActiveRecord_ É bas]
tante comum separarmos regras complexas em diversas classes em Áuby puro_ zsso
é importante para evitar que os modelos ou controles ￿quem grandes e complexos_
â amos ver um exemplo disso no capítulo “￿ “ogin do usuário” _
•o caso do tolcho_net\ o ®uarto se encaixa perfeitamente como um modelo_
rssim\ podemos criar valida ções como a presen ça de uma localidade ou calcular a
disponibilidade dele em uma certa data_
￿n￿ õ ￿￿￿￿￿￿￿
r camada de controle é o intermédio entre os dados que vem dos usuários do site
e os –odelos_ ”utro principal papel da camada de controle é gerenciar sessão e
cookies de usuário\ de forma que um usuário não precise enviar suas credenciais a
todo momento que ￿zer uma requisição_
rpós obter os dados na camada de modelos\ é papel da camada de tontrole
determinar a melhor maneira de representar os dados\ seja via a renderiza ção de
uma página yÍ–“ ou na composi ção de um objeto {É”•_
•o Áuby on Áails\ os componentes que trabalham nessa camada são o
ActionDispatch eo ActionController\ ambos parte do pacote denominado
ActionPack_” ActionDispatch trabalha no nível do protocolo yÍÍø \ fazendo
o parsing dos cabeçalhos\ determinando tipos –z–v\ sessão\ cookies e outras ativi]
dades_
{á o ActionController dá ao desenvolvedor o suporte para escrever o seu
código de tratamento das requisi ções\ invocando os modelos e as regras de negó]
cio adequadas_ vle também dá suporte a ￿ltros\ para\ por exemplo\ veri￿car se um
usuário está logado no sistema para fazer uma reserva no site_
” ActionDispatch é um componente de menor nível\ então não vamos in]
teragir diretamente com este componente_ øorém\ o ActionController é um
dos componentes centrais de aplica ções Áails\ então vamos\ a todo momento\ usar
facilidades dele_
￿n￿ í ￿￿￿￿￿￿￿￿￿￿￿
r camada de apresenta ção é onde prepara]se a resposta para o usuário\ depois da
execução das regras de negócio\ consultas no banco de dados ou qualquer outra ta]
￿￿

## Página 21

tasa do tódigo tapítulo ￿_ tonhecendo a aplica ção
refa que sua aplicação deva realizar_
rs maneiras mais comuns de se exibir dados atualmente na web é através de
páginas yÍ–“_ •o Áuby on Áails\ conseguimos construí]las com o auxílio da bibli]
oteca ActionView Xtambém membro do ActionPackY_ Íambém é possível ter a
representação {É”• dos dados\ via a serializa ção de objetos Xtransformação de ob]
jetos Áuby puro em {É”•Y ou via a constru ção de templates com o JBuilder\p o r
exemplo_
uepois que a apresenta ção ￿nal é montada\ ela é entregue ao usuário via um
servidor web\ como por exemplo\ uma página mostrando todas as informa ções de
um quarto\ ou um objeto {É”•_
øor ￿m\ o Áails ainda possui uma estrutura complexa para gerenciar imagens\
stylesheets e javascripts\ chamada Asset Pipeline \ pré]processando os arquivos
e preparando]os para entregar da melhor forma para o usuário_
￿n￿ R￿￿￿￿
É necessário informar ao Áails quais as áÁ“s que a aplica ção é capaz de responder
e qual tontrole deverá ser invocado_ vsses mapeamentos são chamados de rotas_ ”
mapeamento de rotas no Áails é baseado na forma de recursos Xveja na se ção ￿_￿Y\
mas é possível também fazer rotas customizadas_
âe j a a￿gura ￿_￿_ •ela é possível ver a intera ção entre as diversas camadas –ât
e o roteador quando o usuário requisita uma página de edi ção do recurso “quartoRk
￿￿

## Página 22

￿_￿_ Éuporte tasa do tódigo
wigura￿_￿k wluxo do –ât
￿n￿ S￿￿￿￿￿￿
vm volta de todo os componentes que mencionamos antes\ temos o
ActionSupport_ ” ActiveSupport não é uma camada em si\ pois está
presente em todas as outras camadas_ É no ActiveSupport que ￿cam diversas
ferramentas e extensões ao Áuby\ para deixá]lo ainda mais fácil de usar_ â eja o
exemplo a seguirk
e:x_ys:_0o
@ h- qunc dé óun ed$e d$4df4éé k+? çdé4dd
vssa linha de código imprime a data de dois dias atrás_ vssa funcionalidade não
existe por padrão no Áuby\ mas\ por ser bastante conveniente\ o ActiveSupport
￿￿

## Página 23

tasa do tódigo tapítulo ￿_ tonhecendo a aplica ção
faz essa extensão para você_
vxistem vários outros métodos implementados pelo ActionSupport\ mas não
vale a pena entrar em detalhe sobre cada método_ â ale a pena ler a documenta ção
o￿cial sobre esse módulo emk httpk‘‘guides_rubyonrails_org‘activeúsupportúcoreú
extensions_html_
￿n￿￿ õ ￿￿￿￿￿￿￿￿￿￿￿￿ ￿￿￿￿￿￿
•ão se preocupe em decorar todos os nomes que foram vistos nesse capítulo_ â ocê
pode consultar o livro sempre que precisar saber_ É importante porém saber que eles
existem para que você possa procurar ajuda ou documenta ção_
rliás\ falando em documenta ção\ você aprenderá com o decorrer do livro que
a røz do Áails é bem extensa e cheia de métodos interessantes_ rmbiente]se a de]
senvolver com o site da documentação o￿cial do Áails aberta_ vla está disponível em
httpk‘‘api_rubyonrails_org‘_ Éempre que tiver alguma dúvida sobre algum método do
Áails\ você pode procurar que estará lá_ ”utra ferramenta bastante útil são os Áails
xuides\ ou o xuia do Áails\ ótimo para tirar dúvidas gerais sobre cada componente_
” xuia do Áails ￿ca em httpk‘‘guides_rubyonrails_org‘_
” que é extremamente importante entender desse capítulo\ porém\ são as ideias
de recursos e entender o que cada parte do –ât faz devidamente_ zsso signi ￿ca
que\ sempre que possível\ devemos modelar nossas aplicações como recursos e que
nunca\ jamais\ devemos colocar regras importantes de negócio em tontroles\ por
exemplo\ pois não é o papel dele_
vntendido isso\ vamos continuar_ rgora é hora de voltar a programarQ
￿￿

## Página 25

t ￿￿￿￿￿￿￿ ￿
ørimeiros passos com Áails
íonhecer seus limites já é estar a frente delesp
– xeorg àilhelm wriedrich yegel
￿n￿ I￿￿￿￿￿￿￿￿￿ ￿￿ R￿￿￿￿
øara começar\ é necessário ter o Áuby e o Áuby on Áails para continuar_ â eja a seguir
instruções especí￿cas para cada Éistema ”peracional_
Instalação no OSX
øara quem está iniciando com Áuby on Áails\ a forma mais simples é usar o Áâ–\
ou Áuby enâironment –anager_ rntes de instalar o Áâ–\ porém\ é necessário ins]
talar os pacotes de desenvolvimento da rpple_
Ée você não tem o ãcode\ vá na página do rpple ueveloper Í ools X httpsk‘‘
developer_apple_com‘downloads‘index_actionY e baixe o ‘tommand “ine Íools for
ãcode’ \ versão mais atual e siga os passos de instala ção_ Ée tiver o ãcode mais re]

## Página 26

￿_￿_ znstalação do Áails tasa do tódigo
cente\ você pode abri]lo\ ir nas øreferências o uownloads e instalar o ‘tommand
“ine Í ools’ _
uepois de instalar o tommand “ine Í ools\ basta executar o seguinte comando
no terminalk
wurl çõ 0yt:rvm:io | v_sh çs st_vly ççr_ils
sourwy ã#)pm,:rvm,swripts,rvm
rproveite e vá tomar um café\ vai demorar um pouco_ ro￿nalizar\ este comando
deixará instalado tudo que você precisa para come çar a desenvolver com Áuby on
Áails_
Instalação no Linux
Íanto quanto usuários ”Éã\ a forma mais simples de começar com Áuby on Áails
no “inux é usar o Áâ–\ ou Áuby enâironment –anager_
ørimeiramente é necessário instalar os pacotes de desenvolvimento do seu sis]
tema_ ørocure o manual da sua distribui ção para saber como instalar_ •o ábuntu\
por exemplo\ basta instalar o pacote build-essential e mais algumas outras
bibliotecas de dependênciask
suxo _ptç0yt inst_ll vuilxçyssynti_l livry_xlinyçxyv livsslçxyv wurl t
livsqlityéçxyv
vm seguida\ basta executark
wurl çõ 0yt:rvm:io | v_sh çs st_vly ççr_ils
sourwy ã#)pm,:rvm,swripts,rvm
vste comando irá instalar o Áâ– e também\ automaticamente\ irá instalar a ver]
são mais atual do Áuby e do Áails e todas as dependências_ rproveite para tomar um
café ou um chá\ pois demora um pouco_
Instalação no Windows
znfelizmente não há maneira fácil de se instalar o Áuby on Áails ￿ no àindows_
” instalador Áailsznstaller Xhttpk‘‘www_railsinstaller_orgY ainda não está atualizado
ep o r t a n t o \ar e c o m e n d ação é usar uma distribuição “inux virtualizada_ kX
￿￿

## Página 27

tasa do tódigo tapítulo ￿_ ørimeiros passos com Áails
￿n￿ G￿￿￿￿ ￿ ￿￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿￿
•o ￿nal deste capítulo\ vamos ter o esqueleto preparado para começar o tolcho_net_
øara criar um novo projeto\ precisamos executar no terminal o comando rails
new\ passando em seguida o nome do projeto que será criado\ no caso\colchonet_
ro come çar a instalar\ aproveite para pegar mais café ou sua bebida favorita\ pois
pode demorar um pouco_
ã r_ils nyw wolwhonyt
wry_ty
wry_ty +mj<pm:rxow
wry_ty +_kyzily
wry_ty wonzi0:ru
wry_ty :0iti0nory
:::
7our vunxly is womplyty~ "sy 'vunxly show /0ymn_my3 '
to syy whyry _ vunxlyx 0ym is inst_llyx:
tomo vimos no tapítulo ￿\ vamos escrever código dentro do framework_ øor
causa disso\ o framework impõe uma estrutura de pastas Xmais uma aplica ção da
ideia tonven ção sobre con￿guraçãoY que você deverá seguir_ rlgumas vezes\ inclu]
sive\ você deverá inserir código dentro de arquivos gerados pelo framework\ outras
vezes iremos criar novos arquivos_
r estrutura de pasta do Áails é bastante importante\ e cada pasta possui uma
utilidade especí￿ca_ â eja a estrutura de pastas gerada nas ￿guras ￿_￿e ￿_￿_
￿￿

## Página 28

￿_￿_ xerar o alicerce da aplica ção tasa do tódigo
wigura￿_￿k vstrutura de pastas geradas ] ￿
￿￿

## Página 29

tasa do tódigo tapítulo ￿_ ørimeiros passos com Áails
wigura￿_￿k vstrutura de pastas geradas ] ￿
â amos entender o que é cada uma delask
• app ] É onde ￿ca o código principal da sua aplicação_ tontroles ￿cam na pasta
controllers\ apresentações em views\ javascript e tÉÉ em assets e modelos em
models_ r pasta helpers guarda códigos auxiliares usados em apresenta ções e
mailers são classes para o envio de emails_
• con￿g ] ton ￿guração da aplicação\ como informações sobre bancoXsY de da]
dos\ internacionalização de strings Xz￿￿nY\ time zone\ e outras coisas_
• db ] rrmazena migra ções e o esquema do banco de dados usado na aplicação_
• doc ] Í oda a documentação de sua aplicação deve estar aí_
• lib ] rrmazena código externo à sua aplica ção mas que não faz parte de gems_
rí também ￿cam tarefas rake customizadas\ código que deve ser executado
fora do ambiente à eb_
• log ] ”nde ￿carão seus logs e\ se tudo der certo\ uma pasta que você raramente
terá que acessar_
￿￿

## Página 30

￿_￿_ ”s ambientes de execu ção tasa do tódigo
• public ] rrquivos estáticos como favicon.ico\ robots.txt\ 404.html
e 500.html\ que serão exibidos nos casos de página não encontrada e erro
de servidor\ respectivamente_
• script ]x u a r d aos c r i p trails\ usado para gerar código Xvamos ver mais
detalhes sobre esse comando a seguirY_
• test ] Í estes unitários\ integração\ funcionais e performance ￿cam aqui_ vste
é um tópico bastante complicado e merece seu próprio livro\ então\ ao invés
de vermos o assunto pela metade\ indico a leitura doRSpec êook [ ￿] ou o Guia
Rápido de RSpec [￿]_
• tmp ] •esta pasta ￿cam arquivos temporários como øzus\ cache\ entre outros_
• vendor ] É onde você deverá instalar plugins de terceiros que não são gems_
Íambém é uma boa ideia instalar eventuais plugins javascript e tÉÉ aqui\ para
separar o código da sua aplica ção_
P￿￿￿￿ ￿￿￿￿￿￿ o￿￿￿￿￿￿￿
•as versões anteriores ao Áails ￿\ era possível instalarplugins na pasta
vendor/plugins\ porém essa funcionalidade foi removida_ rtual]
mente\ os plugins devem existir na forma de gems_
uê uma olhada no conteúdo das pastas e abra alguns arquivos\ apenas por curi]
osidade\ para quebrar o gelo\ já que você e o Áails ainda são estranhos entre si_ uê
uma atenção especial ao arquivo config/application.rb\ o arquivo de con￿]
gurações gerais da sua aplicação_
￿n￿ O￿ ￿￿￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿
” Áails possui o conceito de ambientes de execu ção do aplicativo e cada um deles
possui um conjunto próprio de con￿gurações_ ”s ambientes existentes no Áails sãok
• developmentk É o ambiente padrão\ onde o Áails é totalmente con￿gurado
para facilitar o desenvolvimento\ localmente em nossos computadoresl
• test ] ” ambiente test é o ambiente carregado quando são executados os
testes unitários e integraçãol
￿￿

## Página 31

tasa do tódigo tapítulo ￿_ ørimeiros passos com Áails
• production ] ” ambiente production XproduçãoY é o ambiente em que a
aplicação deverá ser executada quando exposta ao mundo e os dados devem
ser reais_
ám exemplo de con ￿guração que varia por ambiente é o caching de classes\ ou
seja\ todo o código Áuby presente na pasta app será carregado apenas uma vez\
caso o caching esteja ligado_ uesligar essa con ￿guração é bastante útil em desen]
volvimento pois\ uma vez que salvamos um arquivo Áuby modi ￿cado\ a próxima
requisição à eb já irá executar o novo código_ vsse processo é bastante lento e por]
tanto\ devemos desligá]lo no ambiente de produção\ senão vamos tornar a aplicação
muito mais lenta_
tada ambiente deverá possuir seu próprio banco de dados_ ” arquivo
config/database.yml possui a de ￿nição da con ￿guração de banco de dados
para cada ambiente_ â eja o exemplo para o ambiente de desenvolvimento\ usando o
adaptador para o øostgreÉ®“k
xyvylopmynt4
_x_ptyr4 post0rysql
x_t_v_sy4 wolwhonytuxyv
host4 low_lhost
usyrn_my4 viniv_00io
p_ssworx4
pool4 8
timyout4 8ddd
vssa separa ção é bastante importante pois não queremos que dados usados em
desenvolvimento inter￿ram com dados em teste ou em produ ção\ ou que\ quando
executamos os testes unitários\ o banco de desenvolvimento seja apagado_
”utros arquivos relacionados com ambientes ￿cam na pasta
config/environments\ no qual cada arquivo é carregado automaticamente
de acordo com o ambiente em execução_
￿￿

## Página 32

￿_￿_ ”s primeiros comandos tasa do tódigo
V￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿ RíILS_ENV
r variável de ambiente RAILS_ENV é usada para determinar em que
ambiente o Áails irá executar\ por padrão sendo development_ rssim\
é possível executar comandos especí￿cos para cada ambiente\ basta fazer\
por exemplok
+joõqum(rhproxuwtion r_ky xv4wry_ty
uentro da aplica ção\ é possível saber qual ambiente estamos execu]
tando através do método Rails.envk
+_ils:ynv
@ h- *xyvylopmynt*
+_ils:ynv:proxuwtioni
@ h- z_lsy
+_ils:ynv:xyvylopmynti
@ h- truy
￿n￿ O￿ ￿￿￿￿￿￿￿￿￿ ￿￿￿￿￿￿￿￿
tom seu terminal aberto na pasta do projeto X colchonetY\ execute o comando
rails server k
￿￿

## Página 33

tasa do tódigo tapítulo ￿_ ørimeiros passos com Áails
õ ￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿
r partir de agora vamos ver diversos comandos de terminal e suas
respostas_ øor isso\ nessas listagens você deve digitar apenas o que segue
o símbolo ￿ XdinheiroY\ ou se por um acaso a linha for muito longa\ será
quebrada com o símbolo óXcontra]barraY_ vxemplosk
ã r_ils syrvyr
h- kootin0 smkriwk
•esse caso\ você deverá digitar apenas rails server e apertar a
tecla vnter_ ” que não tiver esse pre ￿xo será uma saída aproximada do
que você vai ver ao digitar o comando_
ã r_ils syrvyr
h- kootin0 smkriwk
h- +_ils ê:d:d _ppliw_tion st_rtin0 in xyvylopmynt on http4,,d:d:d:d4éddd
h- +un ￿r_ils syrvyr çh ￿ zor mory st_rtup options
h- ltrlçl to shutxown syrvyr
/ed$éçd!ç$= d54é54d5 3 o(n) smkriwk $:é:$
/ed$éçd!ç$= d54é54d5 3 o(n) ruvy $:5:é {ed$eç$$ç$d} / xf=u=êçx_rwin$e:e:d3
/ed$éçd!ç$= d54é54d5 3 o(n) smkriwk44#??%qyrvyr@st_rt4 pixh=f!ê porthéddd
rbra o seu browser em httpk‘‘localhostk￿￿￿￿‘ e voilà\ você verá uma página pre]
parada pela equipe do Áuby on Áails te felicitando por estar rodando Áails_ •essa
página\ há algumas sugestões de passos\ como usar o comando rails generate
para criar modelos e controles_
￿￿

## Página 34

￿_￿_ ”s primeiros comandos tasa do tódigo
wigura￿_￿k Éeja bem vindo ao Áuby on Áails
” comando rails generate é um comando bastante útil_ Ée você digitá]lo
sem parâmetros\ pode ver uma lista do que pode ser gerado_ vssa lista pode aumen]
tar\ dependendo das gems que você instalar no seu projeto Xbastando adicionar no
arquivo GemfileY_
” Áails inclui várias ferramentas para você e o script de geração de templates é
um exemplo de como a ferramenta te ajuda a automatizar tarefas repetitivas_ •esse
espírito\ vamos agora começar a criar nosso primeiro recurso no sistema\ o recurso
quarto\ ou Room\ que terá um título\ uma descrição e uma localização_ waremos isso
através do comando rails generate scaffold \ que irá gerar vários arquivosk
ã r_ils 0ynyr_ty sw_zzolx room titly low_tion xyswription4tyxt
invoky _wtivyuryworx
wry_ty xv,mi0r_ty,ed$éd!$=$=êéééuwry_tyurooms:rv
wry_ty _pp,moxyls,room:rv
invoky tystuunit
wry_ty tyst,moxyls,roomutyst:rv
￿￿

## Página 35

tasa do tódigo tapítulo ￿_ ørimeiros passos com Áails
wry_ty tyst,zixturys,rooms:yml
invoky rysourwyurouty
routy rysourwys 4rooms
invoky sw_zzolxuwontrollyr
wry_ty _pp,wontrollyrs,roomsuwontrollyr:rv
invoky yrv
wry_ty _pp,viyws,rooms
wry_ty _pp,viyws,rooms,inxyx:html:yrv
wry_ty _pp,viyws,rooms,yxit:html:yrv
wry_ty _pp,viyws,rooms,show:html:yrv
wry_ty _pp,viyws,rooms,nyw:html:yrv
wry_ty _pp,viyws,rooms,uzorm:html:yrv
invoky tystuunit
wry_ty tyst,wontrollyrs,roomsuwontrollyrutyst:rv
invoky hylpyr
wry_ty _pp,hylpyrs,roomsuhylpyr:rv
invoky tystuunit
wry_ty tyst,hylpyrs,roomsuhylpyrutyst:rv
invoky jvuilxyr
wry_ty _pp,viyws,rooms,inxyx:json:jvuilxyr
wry_ty _pp,viyws,rooms,show:json:jvuilxyr
invoky _ssyts
invoky wozzyy
wry_ty _pp,_ssyts,j_v_swripts,rooms:js:wozzyy
invoky swss
wry_ty _pp,_ssyts,stylyshyyts,rooms:wss:swss
invoky swss
wry_ty _pp,_ssyts,stylyshyyts,sw_zzolxs:wss:swss
tom um simples comando\ o Áails gerou muitos arquivos_ rntes de entrar em
detalhe o que é cada um deles\ vamos primeiro ver detalhadamente o comando que
executamos\ mostrado na ￿gura ￿_￿k
wigura￿_￿k øarâmetros do comando rails
￿￿

## Página 36

￿_￿_ ”s primeiros comandos tasa do tódigo
•essa ￿gura vemos a composição do comando anterior_ wazemos o generate
de um sca￿old\ ou “andaime” _Sca￿olds são interessantes pois já geram desde o mo]
delo até a apresentação e páginas yÍ–“\ para que possamos ter uma base simples e
funcional_ zsso é bastante conveniente\ pois alterar uma base pronta para deixar da
forma que quisermos é muito mais simples do que começar do zero\ principalmente
quando estamos conhecendo o framework_
r próxima parte do comando é onde especi ￿camos o nome do recurso e seus
atributos_ øor padrão\ todos os campos serão “string” \ ou um campo de texto curto_
øorém\ ainda é possível especi￿car o tipo\ como é o caso dedescription\ a descri]
ção de um quarto pode ser bem longa_ øara isso\ podemos usar o : para especi￿car
o tipo daquele dado_
” comando sca￿old já gera tudo que é necessário para que possamos fazer as
operações mais comuns em um recurso\ o famoso tÁáu_ tÁáu nada mais é do
que create\ retrieve\ update e delete\ ou criar\ buscar‘listar\ editar e remover_ øara tal\
primeiro precisamos criar o banco de dados_ •ão se preocupe em con ￿gurar um
servidor –yÉ®“ ou øostgreÉ®“ por enquanto\ pois vamos usar um banco de dados
bom e simples para o nosso propósito no momento\ o É®“ite_ øara criar o banco de
dados e deixar tudo pronto para ver o resultado do sca￿old\ basta executar\ na pasta
do projeto\ os comandos rake db:create e rake db:migrate k
ã r_ky xv4wry_ty
ã r_ky xv4mi0r_ty
hh lry_ty+ooms4 mi0r_tin0 hhhhhhhhhhhhhhhhhhhhhhh
çç wry_tyut_vly {4rooms}
ç- d:dd$!s
hh lry_ty+ooms4 mi0r_tyx {d:ddees} hhhhhhhhhhhhhh
￿￿

## Página 37

tasa do tódigo tapítulo ￿_ ørimeiros passos com Áails
õ ￿￿￿￿￿￿￿￿￿ ￿￿￿￿￿￿￿ ￿￿￿￿
r aplica ção Áails toma um tempo para iniciar e isso pode se tornar
um pouco inconveniente conforme a aplica ção cresce_ uessa forma\ é
possível combinar os comandos em apenas uma chamada_ zsso irá fazer
com que as tarefas rake compartilhem alguns dos passos que são repeti]
dos quando executamos em duas linhas separadask
ã r_ky xv4wry_ty xv4mi0r_ty
hh lry_ty+ooms4 mi0r_tin0 hhhhhhhhhhhhhhhhhhhhhhhh
çç wry_tyut_vly {4rooms}
ç- d:dd$!s
hh lry_ty+ooms4 mi0r_tyx {d:ddees} hhhhhhhhhhhhhhh
rake db:create irá criar o banco de dados\ se não existir_ •o caso
do É®“ite\ o comando irá criar os arquivos db/development.sqlite3\
db/test.sqlite3 e db/production.sqlite3_
vm seguida\ o rake db:migrate irá criar a tabela rooms no banco de da]
dos usando a migra ção gerada_ â eremos no futuro o que é uma migra ção\ não se
preocupe se você não souber o que é isso_
õ ￿￿￿￿￿￿ ￿￿￿￿ ￿ ￿￿￿￿￿￿￿ ￿￿￿￿￿
” rake\ ou “ruby make” \ é uma ferramenta para executar tarefas de
manutenção de uma biblioteca ou aplica ção\ independente do Áails_ ”
Áails\ porém\ adiciona diversas tarefas pertinentes\ como cria ção e mi]
gração de banco de dados\ executar testes unitários\ entre outros_ øara
saber todos os comandos rake que você pode executar no seu aplicativo\
execute rake -T _
” comando rails\ porém\ em geral executa scripts que não depen]
dem do ambiente da sua aplica ção\ ou seja\ não dependem de conexão
com banco de dados ou carregar o seu código Áuby\ com exce ção do
server_
rgora\ vamos executar o servidork
￿￿

## Página 38

￿_￿_ ”s primeiros comandos tasa do tódigo
r_ils syrvyr
rbra um browser em httpk‘‘localhostk￿￿￿￿‘rooms e você será apresentado pela
tela padrão gerada pelo sca￿oldk
wigura￿_￿k øágina de quartos
rproveite para dar uma navegada\ clique nos links e preencha os formulários_
wuncional\ apesar de simples_ rgora vamos passo a passo inspecionar os arquivos
gerados pelo gerador_
Logs
Í oda a requisição que você ￿zer\ você vai ver que o servidor do Áails mostra um
monte de coisas\ desde consultas É®“ executadas até quando o servidor serve arqui]
vos estáticos_ Í odo este texto será enviado também para a pasta log\ no arquivo
com o nome do ambiente em execução Xpor exemplo\log/development.logYk
qt_rtyx 9m? *,rooms* zor $e!:d:d:$ _t ed$eçdfç$ê e$48f4$8 çd!dd
%rowyssin0 vy +oomslontrollyr@inxyx _s #?põ
+oom õo_x {d:ems} qmõml? *rooms*:[ n+)p *rooms*
+ynxyryx rooms,inxyx:html:yrv within l_youts,_ppliw_tion {e:$ms}
lomplytyx edd )1 in $ems {riyws4 $d:éms | jwtivy+yworx4 d:ems}
É sempre importante estar de olho nessas requisições_ øodemos observar os pa]
râmetros enviados pelo usuário\ as consultas É®“s resultantes\ o tempo gasto em
cada parte da aplicação e o código de resposta enviado ao usuário_
￿￿

## Página 39

tasa do tódigo tapítulo ￿_ ørimeiros passos com Áails
￿n￿ O￿ ￿￿￿￿￿￿￿￿ ￿￿￿￿￿￿￿ ￿￿￿￿ ￿￿￿￿￿￿￿￿
âimos há pouco tempo que o scaffold gerou vários arquivos para nós_ â ejamos
agora o que signi￿ca cada um deles\ o que fazem e qual o seu impacto no projeto_
Migrações
–igra ções são pequenos deltas de um banco de dados\ ou seja\ elas registram
as modi￿cações que o schema\ ou esquema\ do banco de dados vai passando_ áma
migração contém três informações importantesk uma informação de versão\ um có]
digo de regressão e um código de incremento e todas elas ￿cam dentro do diretório
db/migrate do projeto_
” código de incremento de versão ￿ca em um método chamado up_ ®uando
houver a necessidade de se regredir uma versão\ o método executado será o down_
” nome da versão da migra ção encontra]se no nome do arquivo\ que nada mais é
do que uma data Xano\ mês\ dia\ hora\ minuto e segundoY_
” Áails é capaz de saber o comando de regressão para um comando de in]
cremento_ øor exemplo\ o comando drop_table é o oposto do comando
create_table_ rssim\ é possível usarmos o método change em uma migração_
•esse método\ escrevemos o comando de incremento e\ quando precisarmos fazer
uma regressão\ o Áails automaticamente sabe o comando análogo a ser executado_
øara desfazer uma migra ção\ você pode executar rake db:rollback k
ã r_ky xv4rollv_wk
hh lry_ty+ooms4 ryvyrtin0 hhhhhhhhhhhhhhhhhhhh
çç xroput_vly {*rooms*}
ç- d:dd$ds
hh lry_ty+ooms4 ryvyrtyx {d:dd$es} hhhhhhhhhhh
ã r_ky xv4mi0r_ty
hh lry_ty+ooms4 mi0r_tin0 hhhhhhhhhhhhhhhhhhhh
çç wry_tyut_vly {4rooms}
ç- d:dd!ês
hh lry_ty+ooms4 mi0r_tyx {d:dd!=s} hhhhhhhhhhh
âe j a a p ast a db/migrate_ “á haverá um arquivo que inicia com uma
data\ que depende da hora que você executou o comando\ e termina com
_create_rooms.rbk
wl_ss lry_ty+ooms > jwtivy+yworx44pi0r_tion
xyz wh_n0y
￿￿

## Página 40

￿_￿_ ”s arquivos gerados pelo sca ￿old tasa do tódigo
wry_tyut_vly 4rooms xo |t|
t:strin0 4titly
t:strin0 4low_tion
t:tyxt 4xyswription
t:timyst_mps
ynx
ynx
ynx
âimos que\ para executar as migra ções pendentes\ basta executark
r_ky xv4mi0r_ty
•o capítulo ￿\ vamos revisitar e aprofundar em outros comandos de migrações_
Modelo
” arquivo room.rb gerado pelo sca￿old no diretório app/models é o modelo
que tem seus dados guardados no banco de dados quando você clica no botão “treate
Áoom” _ •esse arquivo também ￿cam as regras de valida ção\ relacionamentos com
outros modelos e outras coisas_ ” código atual é simples e veremos como customizá]
lo em breve_
wl_ss +oom > jwtivy+yworx44k_sy
ynx
”s próximos dois arquivos são relacionados a testes_
T este unitário
Í estes unitários são artefatos muito importantes para um sistema de qualidade_
vscrever teste\ porém\ é algo bastante complicado para iniciantes\ pois existe muita
subjetividade em como escrever um teste_ øor exemplo\ devemos escrever um teste
antes do código de produ ção Xou seja\ código que vai ser de fato executado quando
o site estiver no arY ou depoisp uevo usar qual técnicap tomo usar mocks e quando
usar stubsp
vsse assunto deve ser abordado por si só\ dada a sua importância\ portanto re]
comendo a leitura dos livros ￿e RSpec êookn [ ￿] e o T estoóriven óevelopment” êy
ﬀxample [ ￿]_ r comunidade Áails leva testes tão a sério que o próprio framework
vem com um conjunto de ferramentas para auxiliar o desenvolvedor a criar criá]los_
￿￿

## Página 41

tasa do tódigo tapítulo ￿_ ørimeiros passos com Áails
ám exemplo disso são os arquivos gerados_ Í oda vez que o Áails gera um mo]
delo\ controle ou apresentação\ arquivos equivalentes para cada unidade são criados_
”utro artefato gerado são as ￿xtures\ ou acessório\ em uma tradução grosseira_ rs
￿xtures são arquivos no formato é r–“ X httpk‘‘yaml_org‘Y \ uma linguagem simples
para serialização de dados\ que será inserido no banco de dados antes de executar os
testes unitários_ vles são úteis para testar consultas ou para construir um cenário em
que um código deve ser executado para que tudo funcione Xpor exemplo\ para testar
uma autenticação\ é necessário que haja um usuário no banco de dadosY_
Rotas
ørosseguindo\ a próxima modi￿cação é no arquivo de rotas_ ” arquivo de rotas
é onde o Áails mapeia a áÁ“ da requisi ção à um controle que você escreve_ Ée você
se lembra bem\ falamos na se ção ￿_￿ que o Áails é bastante voltado à recursos_ zsso
pode ser observado no arquivo routes.rb\ no diretório configk
rysourwys 4rooms
vssa linha é tudo o que você precisa dizer para ganhar as seguintes rotask
• GET /rooms ]a ção index ] lista todos os quartos disponíveisl
• GET /rooms/new ]a ção new ] mostra uma página com um formulário para
a criação de novos quartosl
• POST /rooms ]a ção create ] cria um novo recurso na cole ção de quartosl
• GET /rooms/:id ]a ção show ] exibe detalhes de um quarto cuja chave pri]
mária Xfamoso idY seja especi￿cada na áÁ“ Xid ￿￿￿para a áÁ“ ‘rooms‘ ￿￿￿\
por exemploY
• GET /rooms/:id/edit ]a ção edit ] exibe o formulário para a edição de um
quartol
• PATCH /rooms/:id ] a ção update ] altera alguma informa ção do recurso
cujo id seja especi ￿cado pelo parâmetro kidl
• PUT /rooms/:id ]a ção update ] o mesmo que o PATCH
• DELETE /rooms/:id ]a ção destroy ] destrói o objeto identi￿cado pelo pa]
râmetro kid
￿￿

## Página 42

￿_￿_ ”s arquivos gerados pelo sca ￿old tasa do tódigo
vssas a ções são geradas por padrão e são todas as a ções mais básicas que quei]
ramos fazer em um recurso Xo “tÁáu”Y_ É claro que dá para customizar\ remover
algumas dessas a ções ou fazer áÁ“s mais interessantes\ mas sempre que ￿zermos
recursos dessa forma\ vamos poupar trabalho_
P o rq u eP U TeP í T õ H ã
” Áails ￿ introduz o suporte ao método PATCH em atualizações de recursos\
sendo que\ nas versões anteriores\ já existia o suporta ao métodoPUT para o mesmo
￿m_
r razão disso é que o método PATCH é uma adi ção mais recente ao protocolo
yÍÍø e tem um signi ￿cado um pouco diferente do PUT_ r ideia é que\ quando
executamos um PUT\ o recurso identi￿cado pela áÁ“ será completamente substi]
tuído pelo objeto sendo entregue\ enquanto o PATCH suporta atualizações parciais\
ou seja\ o que será alterado é apenas o que foi enviado_
r diferen ça pode parecer um pouco sutil\ mas pode ser vista da seguinte maneirak
o resultado ￿nal de um recurso sempre será o mesmo após o resultado de um método
PUT\ enquanto no PATCH\ o resultado nunca será previsível\ pois só temos o controle
de uma parcela do conteúdo a ser atualizado_
øor ￿m\ este comportamento de PATCH e PUT é uma especi ￿cação de servi]
ços ÁvÉÍ que\ por ￿m\ cabe a nós desenvolvedores implementar o comportamento
apropriado_ ” Áails\ por padrão\ não diferencia os dois métodos e acaba sempre
atualizando os recursos parcialmente_
õontrole
” próximo conjunto de modi ￿cações pertence ao controle em si_ •o código do
controle\ você pode observar exatamente as sete a ções mencionadas anteriormente
e um código que realiza as opera ções da maneira mais simples possível_
ípresenta ções
vm seguida\ temos as seguintes páginas\ apresenta ções de algumas das a ções
mencionadask
wry_ty _pp,viyws,rooms,inxyx:html:yrv
wry_ty _pp,viyws,rooms,yxit:html:yrv
wry_ty _pp,viyws,rooms,show:html:yrv
￿￿

## Página 43

tasa do tódigo tapítulo ￿_ ørimeiros passos com Áails
wry_ty _pp,viyws,rooms,nyw:html:yrv
wry_ty _pp,viyws,rooms,uzorm:html:yrv
yá três coisas importantes nessa lista_ r primeira é que você pode ver que que os
arquivos são todos terminados em “erb” _ ” vÁs é a linguagem detemplate padrão do
Áails\ ou seja\ é possível embutir código Áuby em páginas yÍ–“ para que possamos
gerar páginas dinamicamente\ dependendo deste código_ rlém do vÁs\ o Áails pode
usar outras linguagens detemplate\ como yr–“ e “iquid\ bastando que você instale
os plugins apropriados_
øara simpli￿car\ vamos usar vÁs durante esse livro\ então não se preocupe com
outra linguagem de template por enquanto_ vla não é nada de especial na verdade\ é
o Áuby comum embutido dentro de tags yÍ–“_
r segunda observa ção é que não há sete ações e que não necessariamente todas as
páginas mapeiam para uma ação no controle‘rota_ zsso deve]se ao fato que algumas
rotas não possuírem uma apresenta ção em si\ apenas redirecionam ou apresentam
outras_ ám exemplo é a a ção create\ que\ quando há sucesso\ redireciona o usuário
à ação index\ e quando há erro\ o formulário da a ção new é reapresentado\ com a
adição de marcação de erro_
r terceira e última observa ção é que há um arquivo iniciado com__ zsso signi￿ca
que essa página é umapartial\ ou seja\ o conteúdo dela é embutido em outras páginas_
•esse caso\ o _form.html.erb é incluído tanto na páginanew.html.erb quanto
em edit.html.erb pois o formulário é o mesmo\ evitando problemas deCtrl-C
Ctrl-V e duplicidade de código_ rlterando em um lugar\ as mudan ças se re￿etem
em todas as páginas que usam essa partial_
rgora o projeto está criando vida_ â amos então à nossa primeira funcionalidadek
cadastro de usuários_
￿￿

## Página 45

t ￿￿￿￿￿￿￿ ￿
zmplementação do modelo para o
cadastro de usuários
É bom perseguir um objetivo para uma jornadan mas no￿m o que realmente importa
é a jornada em sip
– ársula xuin
•ossa aplica ção está come çando a tomar alguma forma_ {á temos um recurso\
quartos\ e já podemos cadastrá]lo\ editá]lo e removê]lo e ￿zemos tudo isso com a
ajuda de geradores de código_
–as agora que já temos uma breve noção da estrutura do nosso projeto e também
do próprio framework\ podemos começar a construir uma funcionalidade do início
ao ￿m\ e bastante importante para o tolcho_netk cadastro e autenticação de usuários\
o login_
ørimeiramente\ vamos construir o modelo de usuários_ â amos garantir integri]
dade das informações\ ou seja\ construir validações para que um usuário cadastrado
com sucesso no site possua todos os dados necessárias_

## Página 46

￿_￿_ ” usuário tasa do tódigo
áma vez que tivermos o modelo pronto\ vamos montar as páginas de cadastro
e edi ção de per ￿l e por ￿m\ visualização de per ￿l_ uurante esse trabalho\ vamos
montar as rotas e construir as ações do controle sem o auxílio de geradores_
vm seguida\ vamos aprimorar o modelo\ garantindo que o usuário possua uma
senha encriptada no banco de dados\ para que ninguém\ nem mesmo os adminis]
tradores do sistema\ consigam acesso a uma informação tão sigilosa_
”s templates estarão bem crus\ então vamos aplicar um pouco de tÉÉ e yÍ–“
para tornar as telas mais interessantes_ â amos aprender como fazer tudo isso\ e\
em seguida\ iremos aprender a usar o sistema de internacionaliza ção do Áails para
traduzir as páginas para múltiplos idiomas_
øara concluir o cadastro de usuários\ vamos enviar um e]mail para o usuário
para que ele possa con ￿rmar sua conta\ uma prática muito comum nos sites atuais
para evitar cadastros falsos_
￿n￿ O ￿￿￿￿￿￿￿
øara o modelo de usuários\ vamos precisar dos seguintes camposk
• •ome completo
• v]mail
• Éenha
• “ocalidade
• sio
øara criar esse modelo\ vamos usar o gerador de modelos_ vle é bastante útil\
pois já cria a classe User e também já gera a migra çãok
ã r_ils 0ynyr_ty moxyl usyr zullun_my ym_il p_ssworx low_tion vio4tyxt
￿￿

## Página 47

tasa do tódigo tapítulo ￿_ zmplementação do modelo para o cadastro de usuários
G￿￿￿￿￿￿￿￿
â ocê pode observar que muitas vezes vamos usar os geradores que
o Áails provê_ øorém\ é completamente possível desenvolver sem o uso
de nenhum gerador e criar todos os arquivos necessários na mão_ Áe]
comendo tomar esse caminho para quando você estiver mais experiente
com o framework e tiver mais conforto para decidir o que é mais útil para
você_
â ejamos a migração geradak
wl_ss lry_ty"syrs > jwtivy+yworx44pi0r_tion
xyz wh_n0y
wry_tyut_vly 4usyrs xo |t|
t:strin0 4zullun_my
t:strin0 4ym_il
t:strin0 4p_ssworx
t:strin0 4low_tion
t:tyxt 4vio
t:timyst_mps
ynx
ynx
ynx
vra de se esperar ver É®“\ já que estamos tratando de banco de dados\ mas ao
invés disso vemos Áuby_ zsso é uma grande vantagem\ já que infelizmente código
É®“ pode diferenciar entre sistemas de bancos de dados_ ” ActiveRecord já sabe
lidar com essas diferen ças e portanto apenas escrevemos em uma única linguagem
comum_
r migra ção nada mais é do que uma classe que herda de
ActiveRecord::Migration_ Í oda vez que o banco for migrado para uma
versão superior\ o Áails irá executar o que estiver no método #change\ ou seja\
criando a tabela users no banco de dados_ ®uando o banco for migrado para
uma versão inferior\ o equivalente do método create_table será executado\ o
drop_table\ removendo essa tabela_
uentro do bloco associado ao método create_table\ os campos serão criados
com os tipos que declaramos na execução do gerador_ øor￿m\ o Áails adicionou por
￿￿

## Página 48

￿_￿_ ” usuário tasa do tódigo
conta própria os campos relacionado à timestamps_ Éão eles o created_at eo
updated_at_ vsses campos são geridos pelo próprio Áails\ ou seja\ quando criamos
um novo registro no banco\ o created_at será automaticamente preenchido_ ”
updated_at é atualizado toda vez que o modelo é gravado novamente no banco\
na forma de atualização_
rltere o código da migra ção para que ela ￿que da seguinte formak
wl_ss lry_ty"syrs > jwtivy+yworx44pi0r_tion
xyz wh_n0y
wry_tyut_vly 4usyrs xo |t|
t:strin0 4zullun_my
t:strin0 4ym_il
t:strin0 4p_ssworx
t:strin0 4low_tion
t:tyxt 4vio
t:inxyx 4ym_ilc uniquy4 truy
t:timyst_mps
ynx
ynx
ynx
tom essa altera ção\ estaremos criando um índice no campo email da tabela
users com uma propriedade especialk unicidade_ â ejamos o resultado disso em
ação_ ørimeiro\ façak
ã r_ky xv4mi0r_ty
hh lry_ty"syrs4 mi0r_tin0 hhhhhhhhhhhhhhhhhhhhhhhh
çç wry_tyut_vly {4usyrs}
ç- d:dd5és
hh lry_ty"syrs4 mi0r_tyx {d:d$êds} hhhhhhhhhhhhhhh
vste comando irá criar a tabela no banco de dados e adicionar o índice_ rgora
vamos ao console do Áails\ digitando $ rails console _ vsse comando nos leva
ao zÁs\ porém com todo o ambiente do Áails carregado\ portanto é possível fazer
alterações diretas ao banco de dados_
￿￿

## Página 49

tasa do tódigo tapítulo ￿_ zmplementação do modelo para o cadastro de usuários
N￿￿￿￿￿￿￿ R￿￿￿￿￿z￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿￿
•as versões anteriores a versão ￿\ era necessário chamar o mé]
todo add_index\ que só podia ser executado fora do contexto do
create_tablek
_xxuinxyx 4usyrsc 4ym_ilc uniquy4 truy
tom a inclusão do index nas tabelas\ é possível fazer como ￿zemos
na migração anteriork
@ :::
t:inxyx 4ym_ilc uniquy4 truy
@ :::
øor ￿m\ ainda é possível criar um índice diretamente em chaves es]
trangeiras Xnão se preocupe se você não sabe o que é isso\ teremos um
capítulo só para issoYk
@ :::
t:ryzyrynwys 4usyrc inxyx4 truy
@ :::
￿￿

## Página 50

￿_￿_ ” usuário tasa do tódigo
í ￿￿￿￿￿￿ ￿￿￿￿ ￿ ￿￿￿￿￿￿￿ ￿￿￿￿￿
” comando rails possui alguns atalhos para não termos que digitar
o nome completo do comando_ â eja a lista de atalhos a seguirk
• rails c ] equivalente ao rails console
• rails s ] equivalente ao rails server
• rails g ] equivalente ao rails generate
• rails db ] equivalente ao rails dbconsole Xabre o console
do cliente de banco de dados\ dependendo do qual estiver sendo
usadoY
"syr:wry_ty ym_il4 '_xminíyx_mply:wom'
@ j s_íx_ é _ sy0uinty {quyvr_x_ ym linh_s p_r_ z_wilit_r _ lyitur_}4
@ h- @>"syr ix4 $c
@ zullun_my4 nilc
@ ym_il4 *_xminíyx_mply:wom*c
@ p_ssworx4 nilc
@ low_tion4 nilc
@ vio4 nilc
@ wry_tyxu_t4 *ed$eç$$çe5 d!4ee4ê8*c
@ upx_tyxu_t4 *ed$eç$$çe5 d!4ee4ê8*-
øodemos observar algumas coisas importantes neste exemplo_ ørimeiro é que o
Áails criou o campo id mesmo sem qualquer declaração na migração_ vsse campo é
uma chave primária\ ou seja\ um identi￿cador único de uma entrada na tabela_ vste
campo é muito comum no desenvolvimento de projetos\ portanto o Áails sempre
criará este campo para você_
øodemos ver vários atributos como nil\ o que é esperado\ pois não damos ne]
nhum valor a eles_ øorém\ podemos ver que o Áails automaticamente populou os
campos created_at e updated_at_ vsses campos também são automaticamente
gerenciados pelo Áails\ caso os campos existam_ øorém\ a existência desses campos
não é obrigatória nada acontecerá se eles não existirem_
￿￿

## Página 51

tasa do tódigo tapítulo ￿_ zmplementação do modelo para o cadastro de usuários
D￿￿￿z￿￿￿￿￿￿￿ ￿￿ R￿￿￿￿ ￿￿ ￿￿￿￿ ￿￿￿￿￿￿￿
É muito comum fazermos alguns testes manualmente\ criando\ alte]
rando ou deletando objetos do banco de dados_ øara que nossos testes
não ￿quem poluindo o sistema\ é possível iniciar o console usando uma
chave para sandboxk rails console --sandbox _ ®uando você
iniciar a sessão do console\ o Áails irá emitir um início de transa ção no
banco por todo o tempo_ ®uando você sair\ um ROLLBACK será enviado
ao banco\ desfazendo todas as alterações_
â ejamos o modelo usuário\ localizado em app/models/user.rbk
wl_ss "syr > jwtivy+yworx44k_sy
ynx
Ée você observar no exemplo que executamos noconsole\ poderá ver que muitos
campos ￿caram em branco_ øara evitar cadastros muito ruins ou até mesmo aciden]
tes\ vamos colocar algumas valida ções\ garantindo que o usuário coloque todos os
dados necessários_
￿n￿ E￿￿￿￿ ￿￿￿￿￿ ￿￿￿￿￿￿￿ nF￿￿￿ ￿ ￿￿￿￿￿￿￿￿￿
” ActiveRecord nos disponibiliza diversos tipos de valida ções já prontas para
grande parte das situações comuns\ tais como validar presença\ formato\ inclusão em
uma lista X“sexo” em “masculino” ou “feminino” \ por exemploY\ entre vários outros\
além de disponibilizar ferramentas para criarmos as nossas próprias valida ções_
Í udo isso é feito de forma bastante conveniente\ usando class macros_ â amos
então validark
• a presen ça do email\ nome completo\ localização e senhal
• a con ￿rmação de senha\ ou seja\ o usuário precisa preencher um campo con]
tendo a senha e outro para veri￿car se o usuário não cometeu erros de digita]
çãol
• mínimo de ￿￿ caracteres para a bio_
â amos primeiro adicionar as valida ções de presen ça\ informações obrigatórias
no formuláriok
￿￿

## Página 52

￿_￿_ vvite dados errados_ waça validações tasa do tódigo
wl_ss "syr > jwtivy+yworx44k_sy
v_lix_tysuprysynwyuoz 4ym_ilc 4zullun_myc 4low_tionc 4p_ssworx
ynx
Éalve o arquivo\ pois vamos experimentar essas validações no console Xbasta exe]
cutar novamente o comando rails console Yk
usyr h "syr:nyw
usyr:v_lixi @ h- z_lsy
usyr:s_vy @ h- z_lsy
usyr h "syr:nyw
usyr:ym_il h 'jo_oíyx_mply:wom'
usyr:zullun_my h 'óoão'
usyr:low_tion h 'qão %_uloc kr_sil '
usyr:p_ssworx h 'sy0ryxo'
usyr:v_lixi @ h- truy
usyr:s_vy @ h- truy
®uando executamos o método #valid? no modelo\ o ActiveRecord irá
executar a série de valida ções que o modelo tiver e retornar o resultado_ Ée o objeto
estiver válido\ retornará true\e false caso contrário\ como é de se esperar_
” #save irá executar todas as valida ções Xvia o método #valid?Y e se o mo]
delo estiver válido\ tentará salvar o modelo no banco de dados e retornar verdadeiro_
øorém\ se algum problema ocorrer no processo\ seja valida ção ou falha ao salvar o
objeto no banco de dados\ o método #save retornará falso_
D￿ ￿￿￿￿ ￿￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿ ￿￿￿￿￿￿￿￿￿￿
®uando criamos nossos modelos e os fazemos herdar de
ActiveRecord::Base\ automaticamente\ o Áails disponibiliza
os métodos de leitura e escrita de todas as colunas que a tabela possui_
som\ já temos uma ideia de como funcionam as valida ções\ então vamos adici]
onar uma novak
wl_ss "syr > jwtivy+yworx44k_sy
v_lix_tysuprysynwyuoz 4ym_ilc 4zullun_myc 4low_tionc 4p_ssworx
￿￿

## Página 53

tasa do tódigo tapítulo ￿_ zmplementação do modelo para o cadastro de usuários
v_lix_tysuwonzirm_tionuoz 4p_ssworx
ynx
D￿￿￿z￿￿￿￿￿￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿
Ée você alterar o modelo e não reiniciar sua sessão do console do Áails\
você não vai conseguir interagir com as suas novas altera ções_ øara não
haver a necessidade de sair e entrar novamente no console\ basta executar
o comando reload! que o Áails irá recarregar tudo o que estiver dentro
da pasta app_
” funcionamento do validates_confirmation_of é bem interessante_ r
partir do momento que adicionamos essa validação\ para salvar um objeto no banco
de dados\ é necessário usar um novo atributo “virtual” \ ou seja\ um atributo que não
existe no banco de dados\ chamado password_confirmation_ Ée ele não estiver
igual ao campo de senha XpasswordY\ o modelo não pode ser gravado no banco_
í ￿￿￿￿￿￿￿￿ ￿￿￿￿￿￿￿￿
tomo o Áails interage com os métodos padrão de leitura e es]
crita do Áuby\ é possível criar atributos que não são persistidos no
banco de dados\ mas que interagem com o Áails_ øor exemplo\ o
próprio ActiveRecord::Base cria um atributo virtual chamado
password_confirmation e realiza valida ções em password com
este novo atributo_
vssa técnica é bastante útil para simpli￿car a interface externa de uma
classe\ de modo a esconder detalhes de implementa ção para outros ele]
mentos_
tom o mesmo console aberto\ podemos executark
rylo_x~
@ +ylo_xin0:::
@ h- truy
usyr h "syr:nyw
￿￿

## Página 54

￿_￿_ vvite dados errados_ waça validações tasa do tódigo
usyr:ym_il h 'jo_oíyx_mply:wom'
usyr:zullun_my h 'óoão'
usyr:low_tion h 'qão %_uloc kr_sil '
usyr:p_ssworx h 'sy0ryxo'
usyr:p_ssworxuwonzirm_tion h 'yrryiuousy0ryxo'
usyr:v_lixi @ h- z_lsy
usyr:yrrors:myss_0ys
@ h- {4p_ssworxh-/*xoysn 't m_twh wonzirm_tion*3}
®uando a valida ção é executada Xtanto pelo método #valid? quanto pelo
#saveY\ o ActiveRecord popula um atributo especial no modelo\ chamado
errors_ tom ele é possível veri ￿car\ em mensagens legíveis\ quais foram os erros
de validação_
rgora vamos a última valida ção\ o tamanho da biok
wl_ss "syr > jwtivy+yworx44k_sy
v_lix_tysuprysynwyuoz 4ym_ilc 4zullun_myc 4low_tionc 4p_ssworx
v_lix_tysuwonzirm_tionuoz 4p_ssworx
v_lix_tysulyn0thuoz 4vioc minimum4 édc _llowuvl_nk4 z_lsy
ynx
” validates_length_of faz diversos tipos de valida ção com tamanho
de texto_ •esse caso\ aplicamos ao atributo “bio” apenas duas restri çõesk o
tamanho mínimo de ￿￿ caracteres e ele não pode ser em branco_ øorém\ o
validates_length_of aceita outras opções\ entre elask
• :maximumk “imita o tamanho máximol
• :ink ro invés de passar :minimum e :maximum\ basta fazer\ por exemplo\
in: 5..10 para validar o mínimo de ￿ e o máximo de ￿￿ caracteresl
• :isk “imita o tamanho exato do textol
• :allow_blankk øermite que o atributo￿que em branco\ e\ quando presente\
respeite as condições de tamanhol
vxistem algumas outras op ções menos usadas_ øara saber quais são\ recomendo
olhar a documentação o￿cial do Áails_
” ActiveRecord ainda possui diversas outras valida ções que não usamos
nessa classe\ mas que são bastante úteis_ vxemplosk
￿￿

## Página 55

tasa do tódigo tapítulo ￿_ zmplementação do modelo para o cadastro de usuários
• validates_format_ofk â alida o formato de um texto com uma expressão
regularl
• validates_inclusion_ofk â alida a inclusão de um elemento em um enu]
merável\ ou seja\ um número em um range ou um texto dentre uma lista de
opçõesl
• validates_numericality_ofk â alida se o atributo passado é realmente
um número\ com algumas opções interessantes\ por exemplo\ :less_than\
:greater_than\ entre outros_
rlém das valida ções citadas\ ainda é possível criar validações customizadas\ que
é o que vamos fazer agora_ â amos validar o formato do email\ pois é possível colocar
qualquer coisa\ mesmo que não seja um e]mail válido_ ”bserve que é possível im]
plementar essa mesma validação com o validates_format_of\ mas vamos usar
uma validação customizada para entender como ela funciona_
øara isso\ vamos usar uma valida ção simples_ vla não é nem de longe ideal e
não é compatível com o Áwt de e]mails Xveja em httpk‘‘bit_ly‘validacao]emailuma
expressão regular compatível\ se estiver curiosoY\ mas é su￿ciente para informar ao
usuário que algo está errado_ {á que vamos enviar um email de con ￿rmação para o
usuário poder usar o sistema\ não é necessária tanta formalidade_
â amos usar uma expressão regular extraída da biblioteca uevise X httpk‘‘github_
com‘plataformatec‘devise Y \ uma biblioteca complexa de autoriza ção de usuários_
rpesar de completa\ a biblioteca não é recomendada para quem está come çando
com Áails\ portanto não vamos usá]la no tolcho_net_
wl_ss "syr > jwtivy+yworx44k_sy
mpjoõu+m9m;% h ,tj/2í3]í{/2ít:3]t:}]/2ít:3]tz,
v_lix_tysuprysynwyuoz 4ym_ilc 4zullun_myc 4low_tionc 4p_ssworx
v_lix_tysuwonzirm_tionuoz 4p_ssworx
v_lix_tysulyn0thuoz 4vioc minimum4 édc _llowuvl_nk4 z_lsy
v_lix_ty 4ym_iluzorm_t
priv_ty
@ mss_ v_lix_ção poxy syr ryprysynt_x_ x_ sy0uinty zorm_4
@ v_lix_tysuzorm_tuoz 4ym_ilc with4 mpjoõu+m9m;%
￿￿

## Página 56

￿_￿_ vvite dados errados_ waça validações tasa do tódigo
xyz ym_iluzorm_t
yrrors:_xx{4ym_ilc 4inv_lix} unlyss ym_il:m_twh{mpjoõu+m9m;%}
ynx
ynx
r class macro validate aceita um símbolo com o nome do método a ser cha]
mado ou um bloco_ ” efeito seria o mesmo se tivéssemos feito da seguinte formak
v_lix_ty xo
yrrors:_xx{4ym_ilc 4inv_lix} unlyss ym_il:m_twh{mpjoõu+m9m;%}
ynx
”bserve a forma que anotamos que um atributo é inválidok chamamos o método
add XadicionarY no objetoerrors com o nome do atributo e\ em seguida\ o tipo
do erro_ ” tipo do erro é usado para determinar a mensagem que será exibida ao
usuário e pode ser qualquer coisa que você quiser_ ásamos :invalid pois o Áails
já usa e sabe traduzir_ â eja a lista a seguir\ contendo as mensagens mais interessantes\
retirada do arquivo de traduções do Áails Xhttpsk‘‘github_com‘svenfuchs‘rails]i￿￿n‘
blob‘master‘rails‘locale‘en_yml ￿“ ￿￿￿Y
• acceptedk must be accepted Xprecisa ser aceitoY
• blankk can’t be blank Xnão pode￿car em brancoY
• confirmationk doesn’t match con￿rmation Xnão é igual a con￿rmaçãoY
• emptyk can’t be empty Xnão pode￿car vazioY
• equal_tok must be equal to￿ {count} Xprecisa ser igual a countY
• exclusionk is reserved Xé reservadoY
• greater_thank must be greater than ￿ {count} Xprecisa ser maior que
countY
• greater_than_or_equal_tokm u s tb eg r e a t e rt h a no re q u a lt o￿ {count}
Xmaior ou igual que countY
• inclusionk is not included in the list Xnão está na listaY
• invalidk is invalid Xé invalidoY
• less_thank must be less than￿ {count} Xprecisa ser menor que countY
￿￿

## Página 57

tasa do tódigo tapítulo ￿_ zmplementação do modelo para o cadastro de usuários
• less_than_or_equal_tok must be less than or equal to ￿ {count} Xmenor
ou igual que countY
• not_a_numberk is not a number Xnão é um númeroY
•o capítulo ￿ “waça sua aplicação falar várias línguas” \ vamos ver mais detalhes
sobre o sistema de internacionalização do Áails_
â amos também criar uma valida ção de unicidade para emails\ ou seja\ emails
cadastrados não poderão existir previamente no site_ É importante ressaltar que
o validates_uniqueness_of possui um problemak primeiro o Áails veri ￿ca
a existência do email a ser cadastrado e depois cria o modelo no banco\ se o resto es]
tiver ”}_ É possível que\ entre a veri ￿cação e a criação\ o email seja criado no banco
e o Áails tentará criar o modelo de qualquer forma_ É por isso que criamos a valida]
ção de unicidade também no banco de dados\ e estamos criando essa valida ção no
modelo apenas para feedback ao usuário\ resultando no seguinte códigok
wl_ss "syr > jwtivy+yworx44k_sy
mpjoõu+m9m;% h ,tj/2í3]í{/2ít:3]t:}]/2ít:3]tz,
v_lix_tysuprysynwyuoz 4ym_ilc 4zullun_myc 4low_tionc 4p_ssworx
v_lix_tysuwonzirm_tionuoz 4p_ssworx
v_lix_tysulyn0thuoz 4vioc minimum4 édc _llowuvl_nk4 z_lsy
v_lix_tysuuniquynyssuoz 4ym_il
@ mss_ v_lix_ção poxy syr ryprysynt_x_ x_ sy0uinty zorm_4
@ v_lix_tysuzorm_tuoz 4ym_ilc with4 mpjoõu+m9m;%
v_lix_ty xo
yrrors:_xx{4ym_ilc 4inv_lix} unlyss ym_il:m_twh{mpjoõu+m9m;%}
ynx
ynx
￿￿

## Página 58

￿_￿_ vvite dados errados_ waça validações tasa do tódigo
S￿￿￿￿￿￿ ￿￿￿￿￿￿￿￿￿￿ ￿ ￿￿￿￿ ￿ ￿￿￿￿￿￿￿￿￿
vxiste uma outra sintaxe para valida ções_ â eja as duas valida ções a
seguirk
v_lix_tys 4ym_ilc prysynwy4 truy
v_lix_tysuprysynwyuoz 4ym_il
rmbas possuem o mesmo comportamento\ porém a sintaxe usando
a class macro validates foca no atributo a ser validado\ de
forma que você possa adicionar diversas valida ções de uma vez_ ”
validates_presence_of\ em contrapartida\ foca na validação em si\
podendo passar diversos atributos de uma vez_ â eja outro exemplok
v_lix_tys 4ym_ilc prysynwy4 truyc
zorm_t4 { with4 ,tj/2í3]í/2ít:3]tz, }c
uniquynyss4 truy
rinda é possível colocar múltiplos atributos na valida çãok
v_lix_tys 4ym_ilc 4zullun_myc 4low_tionc prysynwy4 truy
tomo não há diferen ça de comportamento\ você pode converter as
validações que ￿zemos com a sintaxe tradicional para a sintaxe alterna]
tiva e veri￿car qual você mais gosta_
•osso modelo usuário está bom o su ￿ciente para prosseguir_ â amos agora co]
meçar a fazer o ￿uxo de cadastro\ criando o controle e customizando as páginas_
￿￿

## Página 59

t ￿￿￿￿￿￿￿ ￿
Íratando as requisi ções à eb
ﬀu não desanimon pois cada tentativa incorreta descartada é mais um passo a frentep
– ￿omas r_ vdison
￿n￿ R￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿￿￿￿ ￿￿￿￿ ￿ ￿￿￿￿￿￿￿￿
â amos começar a ligar as outras partes do sistema com o modelo que criamos no
capítulo anterior_ â amos fazer tudo com o mínimo uso de geradores do Áails\ para
entendermos cada passo do projeto\ diferente do que￿zemos com o modelo “quarto” _
rntes de prosseguirmos\ temos que criar algum código para que o roteador do
Áails saiba interpretar requisições em uma certa áÁ“_ â amos alterar o roteador de
maneira a adicionar as seguintes ações para o recurso usuáriok
• index ] “ista todas as entradas do recursol
• show ] vxibe uma entrada especí ￿ca do recursol
• new ] øágina para entrar com os dados para uma nova entradal

## Página 60

￿_￿_ Áoteie as requisições para o controle tasa do tódigo
• create ]r ção de criar uma nova entradal
• edit ] øágina para editar uma entrada já existentel
• update ]r ção de atualização de uma entrada existentel
• destroy ] Áemoção de uma entrada existentel
áma vez que indicarmos no roteador essas rotas\ precisamos também indicar
qual controle irá responder pelas requisições_ øara fazer isso\ vamos editar o roteador
Xconfig/routes.rbY da seguinte formak
lolwhonyt44jppliw_tion:routys:xr_w xo
rysourwys 4rooms
rysourwys 4usyrs
@ jqui yst_rão vários womyntários 0yr_xos pylo +_ils p_r_
@ ty _jux_r _ lymvr_r y yntynxyr womo zunwion_
@ o roty_xor:
ynx
rgora\ com o servidor do Áails em execu ção Xlembre]se\ basta executar rails
server na pasta do projetoY\ abra o browser e acesse o endere ço para o nosso re]
cursokhttpk‘‘localhostk￿￿￿￿‘users‘new _
â ocê vai encontrar uma tela de errok
￿￿

## Página 61

tasa do tódigo tapítulo ￿_ Íratando as requisi ções à eb
wigura￿_￿k vrrok Áouting error ] vrro de roteamento
” Routing error Xerro de roteamentoY é um erro comum_ ” roteador do Áails
tenta passar a execução de requisições de um recurso para o seu controle correspon]
dente_ •o caso do modelo usuário\ o Áails tentará passar requisi ções em rotas que
iniciam com /users para o controle UsersController\ que ainda não existe_
®uando especi ￿camos resources :rooms \ o roteador espera que exista um
controle UsersController que responda às sete ações que vimos anteriormente\
no início desse capítulo_ ” mesmo acontece com o recurso quartos X resources
:roomsY_ tomo usamos o gerador para o recurso quarto\ o controle foi criado au]
tomaticamente_ •o caso de usuários\ vamos criá]lo manualmente\ em seguida_
￿￿

## Página 62

￿_￿_ Áoteie as requisições para o controle tasa do tódigo
N￿￿￿￿￿￿￿ R￿￿￿￿￿z T￿￿￿￿ ￿￿ ￿￿￿￿￿
áma novidade do Áails ￿ é que as telas de erro de roteamento são
muito mais informativas_ •o ￿nal da página\ há uma lista de rotas que
sua aplicação dá suporte ordenadas por prioridade_ ”u seja\ caso alguma
rota que você tenha entre em con ￿ito com outra\ a rota que tiver maior
prioridade será executada_
”s controles vivem na pasta app/controllers\ portanto crie o arquivo
users_controller.rb de acordo com o seguintek
wl_ss "syrslontrollyr > jppliw_tionlontrollyr
ynx
tomo você pode observar\ um controle é uma classe Áuby comum\ que herda
da classe ApplicationController_ ” ApplicationController é um
controle “abstrato” \ ou seja\ não terá uma rota que aponta diretamente para ela\
porém ela de ￿ne características globais em sua aplica ção_ vssa classe é gerada
quando a aplica ção é criada\ ou seja\ quando executamos\ na linha de comando\
o comando rails new e portanto\ vive em seu projeto_ ro abrir o arquivo
app/controllers/application_controller.rb\ temos o código a seguir\
gerado pelo Áailsk
wl_ss jppliw_tionlontrollyr > jwtionlontrollyr44k_sy
@ %ryvynt lq+n _tt_wks vy r_isin0 _n yxwyption:
@ nor j%osc you m_y w_nt to usy 4nullusyssion insty_x:
protywtuzromuzor0yry with4 4yxwyption
ynx
” ApplicationController herda\ por sua vez\ do
ActionController::Base\ um componente interno do Áails_ •essa classe
há uma class macro bastante importante\ protect_from_forgery_ vssa macro
faz com que todos os controles da aplica ção exijam uma chave de autentica ção em
ações de altera ção de dados X create\ update e destroyY de modo a evitar ataques
de falsi ￿cação de requisi ção XRequest Forgery Y_ øortanto\ é bastante importante
deixá]la ativada sempre que possível_
￿￿

## Página 63

tasa do tódigo tapítulo ￿_ Íratando as requisi ções à eb
F￿￿￿￿￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿￿￿
rtaques de falsi ￿cação de requisição entre sites Xoucrossosite request
forgery ] tÉÁwY consistem em enviar uma requisi ção de um site a ou]
tro fazendo uma a ção que o usuário não desejou_ øor exemplo\ imagine
que no colcho_net\ para você deletar sua conta\ haja o endereço hipoté]
tico httpk‘‘colcho_net‘usuarios‘deletarúconta_ ám usuário malicioso pode
colocar em um site qualquer uma imagem com a seguinte tagk
<img src=" httpk‘‘colcho_net‘usuarios‘deletarúconta” />
ro entrar nesse site\ o browser irá tentar baixar o conteúdo dessa ima]
gem\ que na verdade é a ação para deletar sua conta e bumQ\ sua conta foi
deletada_ øara proteger seu site contra isso\ o Áails faz um mecanismo tal
que\ para cada a ção de modi ￿cação de estado\ é necessário enviar uma
chave de segurança gerada aleatoriamente_
ørosseguindo com o projeto\ vamos adicionar uma a ção ao controle de usuá]
rios_ vssa a ção será a a ção de cadastro\ ou seja\ a cria ção de um novo ob]
jeto usuário_ øara isso\ criaremos a a ção new\ no UsersController X
app/controllers/users_controller.rbYk
wl_ss "syrslontrollyr > jppliw_tionlontrollyr
xyz nyw
ynx
ynx
øor agora não faremos nada nessa a ção\ portanto o método new ￿ca vazio_
ro acessarmos httpk‘‘localhostk￿￿￿￿‘users‘new \ um erro diferente é apresentadok
T emplate is missing\ ou “template ausente” _ r ação é encontrada\ porém o Áails não
consegue encontrar a apresentação daquela açãok
￿￿

## Página 64

￿_￿_ Áoteie as requisições para o controle tasa do tódigo
wigura￿_￿k vrrok Í emplate is missing ] template ausente
”s templates ￿cam na pasta app/views_ uentro dela\ existe uma hierarquia_
–ais uma vez o Áails adota uma conven ção_ ua mesma maneira que o nome do
controle é derivado do nome do recurso\ o nome da pasta é derivado do nome do
controle_ øor exemplo\ se tivéssemos o controle UserSessionsController\ os
templates deste controle serão procurados na pasta app/views/user_sessions_
uessa forma\ os templates para o controle UsersController serão procurados na
pasta app/views/users_
•ote que na pasta app/views existe também a pasta layouts_ vssa pasta é
uma pasta especial_ ”s templates presentes nessa pasta são usados por um ou mais
controles e servem como a base em que vamos injetar o template de cada a ção_ øara
entender melhor\ observe a ￿gura ￿_￿_
￿￿

## Página 65

tasa do tódigo tapítulo ￿_ Íratando as requisi ções à eb
wigura￿_￿k tomposi ção de página usando layouts
” uso de layouts dessa forma é bastante prático_ •ão há a necessidade
de repetir diversos comandos e tags Xevitando também um tedioso trabalho de
busca‘substituição quando você faz alguma alteraçãoY\ basta escrever o yÍ–“ espe]
cí￿co da sua página que será injetado no código do layout mais genérico para a sua
aplicação_
” que difere layouts de templates de a ções é a execução do comando yield_”
yield diz ao Áails que\ naquele exato ponto\ deverá ser injetado um outro template_
â eja o exemplo a seguirk
application.html.erbk
>html-
>voxy-
<%= yiylx %>
>,voxy-
>,html-
rgora imagine que o template da a ção new do controle UsersController
seja da seguinte formak
￿￿

## Página 66

￿_￿_ Áoteie as requisições para o controle tasa do tódigo
>h$-l_x_stro>,h$-
®uando executarmos\ no controle\ o seguinte códigok
rynxyr *nyw*c l_yout4 *_ppliw_tion*
” Áails irá renderizar para o usuário o seguinte resultado ￿nalk
>html-
>voxy-
>h$-l_x_stro>,h$-
>,voxy-
>,html-
É possível também ter mais de um layout em um sistema_ zsso é útil\ por exemplo\
quando há diversas “personas” em um site\ como um administrador e um usuário
comum\ ou um lojista e o cliente_
P￿￿￿￿￿￿￿
øersona é um personagem ￿ctício de um possível usuário do seu site_
É importante pensarmos em como cada persona vai interagir com o sis]
tema que estamos elaborando_ rssim\ é mais fácil ter ideias de como
melhorar a experiência do usuário_
•o caso do colcho_net\ temos duas personask o “hospedado” \ usuário
que procura lugar para dormir e o “an ￿trião” \ usuário que tem um lugar
sobrando_
â amos agora criar o template para a a ção new_ øara isso\ crie a pasta users
em app/views e crie o arquivo app/views/users/new.html.erb_ ” nome
do arquivo possui três signi￿cadosk ação new\ que vai ser pré]processado pelo vÁs\
resultando em um arquivo htmlk
>h$-l_x_stro>,h$-
øor enquanto esse template está muito sem gra ça_ â amos usar o controle
UsersController para preparar os dados para que possamos criar o formulário
de cadastro_
￿￿

## Página 67

tasa do tódigo tapítulo ￿_ Íratando as requisi ções à eb
￿n￿ I￿￿￿￿￿￿ ￿ ￿￿￿￿￿￿￿￿ ￿ ￿ ￿￿￿￿￿￿￿￿￿￿￿￿
âamos voltar ao UsersController para criar a tela de cadastro de novo usuáriok
wl_ss "syrslontrollyr > jppliw_tionlontrollyr
xyz nyw
íusyr h "syr:nyw
ynx
ynx
uuas coisas acontecem no trecho de código anteriork a primeira é que usamos
o método .new no modelo User_ {á vimos esse método anteriormente\ ele cria
uma nova instância do modelo User\ sem gravar no banco de dados_ vm seguida\
armazenamos o novo objeto em uma variável de instância\ @user_ ” controle com]
partilha todas as variáveis de instância com o template\ ou seja\ toda variável com @
estará disponível no template renderizado pela ação_
•ote que nunca especi ￿camos o template a ser renderizado_ øor padrão\ quando
não especi ￿camos o template\ o Áails irá buscar pelo nome equivalente da a ção
na pasta de templates do controle_ tomo a a ção é new\oÁ a i l si r áb u s c a rp o r
app/views/users/new.html.erb_
zsso signi￿ca que já podemos acessar esse objeto no template_ ásaremos ele para
construir o formulário_ vsse formulário terá vários campos para preencher o objeto_
rbra o arquivo app/views/users/new.html.erb e altere para que ele ￿que da
seguinte formak
>h$-l_x_stro>,h$-
<%= zormuzor íusyr xo |z| %>
>p-
<%= z:l_vyl 4zullun_my %> >vr ,-
<%= z:tyxtuziylx 4zullun_my %>
>,p-
>p-
<%= z:l_vyl 4low_tion %> >vr ,-
<%= z:tyxtuziylx 4low_tion %>
>,p-
>p-
<%= z:l_vyl 4ym_il %> >vr ,-
<%= z:tyxtuziylx 4ym_il %>
>,p-
￿￿

## Página 68

￿_￿_ zntegre o controle e a apresentação tasa do tódigo
>p-
<%= z:l_vyl 4p_ssworx %> >vr ,-
<%= z:p_ssworxuziylx 4p_ssworx %>
>,p-
>p-
<%= z:l_vyl 4p_ssworxuwonzirm_tion %> >vr ,-
<%= z:p_ssworxuziylx 4p_ssworxuwonzirm_tion %>
>,p-
>p-
<%= z:l_vyl 4vio %> >vr ,-
<%= z:tyxtu_ry_ 4vio %>
>,p-
>p-
<%= z:suvmit %>
>,p-
<% ynx %>
vsse código que criamos é um exemplo de como é um template vÁsk trechos
de yÍ–“ envolto de código Áuby_ vm vÁs\ todo código Áuby que não terá seu
conteúdo impresso no yÍ–“ resultante deve ser envolto de <<% %<> _ taso você
queira que o código seja impresso no yÍ–“ resultante\ temos que envolver o código
Áuby com <%= %> Xobserve o =Y_
â ocê pode ver também que este código faz uso extensivo de métodos auxili]
ares do Áails_ •esse caso\ utilizamos alguns métodos\ como o text_field e
password_field\ para construir o formuláriok
• form_for ] znicia a construção de um formulário para um modelol
• label ] Label XetiquetasY correspondente a um campo do formuláriol
• text_field ] tampo simples de textol
• password_field ] tampo mascarado de senhal
• text_area ] Área grande de texto\ para escrevermos a biol
• submit ] sotão de Éubmit XvnviarY\ para enviar os dados ao servidorl
” form_for é o que chamamos de construtor de formulários para modelos_
vsse método é bastante integrado com todas as camadas do Áails_ øor exemplo\ ele
￿￿

## Página 69

tasa do tódigo tapítulo ￿_ Íratando as requisi ções à eb
sabe construir exatamente a rota que deverá ser chamada quando enviamos o for]
mulário Xvia botão “Éubmit”Yk ele usa o método #new_record? no modelo para
determinar se o objeto está gravado no banco de dados\ e portanto\ sabe diferenciar
se deve rotear o usuário para a a ção create ou update_
vle sabe também que o objeto possui atributos Xexperimente mudar um dos cam]
pos do formulário para algum atributo qualquer\ não existente no modelo e veja o
que aconteceY e portanto faz o mapeamento correto para que o atributo seja facil]
mente usado no controle\ para gravar o objeto_ rlém disso\ se o objeto já existir no
banco de dados\ ele irá popular as caixas de texto com os valores associados a cada
atributo_
â ejamos o resultado deste templatek
wigura￿_￿k wormulário de cadastro de usuário
ro preencher o formulário e clicar em “treate áser” Xcriar usuárioY\ vamos ser
apresentados ao erro Unknown action\ ou ação desconhecida\ create_ zsso signi￿ca
￿￿

## Página 70

￿_￿_ zntegre o controle e a apresentação tasa do tódigo
que o formulário enviou os dados para uma a ção que ainda não existe_ øois vamos
criá]la_ •essa a ção\ temos que obter os dados do formulário e gravá]los como um
novo objeto no banco de dados_ Ée o objeto for gravado com sucesso\ vamos apre]
sentar o usuário com uma mensagem de sucesso\ e\ caso contrário\ apresentamos o
formulário novamente\ anotado com erros\ para que o usuário possa corrigi]los e
enviar os novos dados_
ra ção create possuirá a seguinte lógicak
• tria novo usuário baseado nos dados vindos do formulário\ via o método
paramsl
• Ée o usuário foi salvo com sucesso X#save retorna sempre true ou falseY\
redireciona ele para a página de seu per ￿l e exibe uma mensagem de sucessol
• taso não seja possível salvar\ renderiza o formulário novamente_
rbra novamente o UsersController X
app/controllers/users_controller.rbY e deixe]o da seguinte maneirak
wl_ss "syrslontrollyr > jppliw_tionlontrollyr
xyz nyw
íusyr h "syr:nyw
ynx
xyz wry_ty
íusyr h "syr:nyw{p_r_ms/4usyr3}
iz íusyr:s_vy
ryxirywtuto íusyrc
notiwy4 'l_x_stro wri_xo wom suwysso~ '
ylsy
rynxyr _wtion4 4nyw
ynx
ynx
ynx
â amos entrar em detalhe em cada linhak
íusyr h "syr:nyw{p_r_ms/4usyr3}
” método params Xlembre]se que em Áuby\ para chamar métodos\ não precisa]
mos de parêntesesY retorna um hash com todos os parâmetros enviados pelo usuário\
￿￿

## Página 71

tasa do tódigo tapítulo ￿_ Íratando as requisi ções à eb
seja via formulário XPOSTY ou via query string Xparâmetros pela áÁ“\ por exem]
plo httpk‘‘google_compqnhello\ via GETY_ ®uando usamos os métodos auxiliares do
Áails para formulários\ o params se parece com o seguintek
{
*_uthyntiwityutokyn*h-*ozi(õó."jõ,p8v;fzdwy](8_m5htó<oj"kh*c
*usyr*h- {
*zullun_my*h-*riniwius*c
*low_tion*h-*q_n nr_nwiswoc lj* c
*ym_il*h-*viniv_00ioíyx_mply:wom*c
*p_ssworx*h-*sy0ryxo*c
*p_ssworxuwonzirm_tion*h-*sy0ryxo*c
*vio*h-*)lác tuxo vomi pyu nomy é riníwius:*
}c
*wommit*h-*lry_ty "syr* c
*_wtion*h-*wry_ty*c
*wontrollyr*h-*usyrs*
}
F￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿￿
Ée você observar o log do servidor\ notará algumas diferen ças entre
os atributos que vimos anteriormente e o que de fato é passado no hash
params_ r principal diferen ça é que o Áails\ por padrão\ ￿ltra qualquer
parâmetro que contenha a palavra “password” no nome_ zsso é bastante
importante pois\ se algum usuário obter os logs do servidor\ ele não será
capaz de recuperar nenhuma informação sensível_
øara adicionar ou mudar esta lista de atributos\ basta alterar o arquivo
config/initializers/filter_parameter_logging.rbk
@ ky sury to ryst_rt your syrvyr whyn you moxizy this zily:
@ lonzi0ury synsitivy p_r_mytyrs whiwh will vy
@ ziltyryx zrom thy lo0 zily:
+_ils:_ppliw_tion:wonzi0:ziltyrup_r_mytyrs ]h /
4p_ssworxc
4p_ssworxuwonzirm_tion
3
￿￿

## Página 72

￿_￿_ zntegre o controle e a apresentação tasa do tódigo
â ocê pode ver que todos os campos do formulário vieram dentro de uma hash
só\ a hash users_ É esse conteúdo que passamos para o método .new do modelo_
õ ￿￿￿￿ ￿￿ ￿￿￿￿ ￿￿ ￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿
” hash params é\ normalmente\ uma coisa confusa para iniciantes
pois você pode acessá]lo usando chaves como símbolos ou strings_ zsso
signi￿ca que\ por exemplo\params["user"] e params[:user] pro]
duzem o mesmo resultado_
zsso acontece pois o Áails cria um tipo especial de hashes\ chamado
HashWithIndifferentAccess\ que pode ser usado da mesma ma]
neira que um hash comum_
” método .new aceita um hash contendo todos os atributos a serem associados_
vsse é um conceito chamadomassoassignment\ ou seja\ associação em massa_ É muito
mais prático do que ￿car chamando cada método individualmente dessa maneira_
øorém\ essa associação em massa pode gerar problemas de segurança_ â eremos esse
assunto logo em seguida\ na seção
tontinuando\ com o objeto populado de atributos que vieram do formulário\
tentaremos salvá]lo no banco de dados_ Ée tudo der certo\ ou seja\ #save retornar
true\ as linhas a seguir serão executadask
ryxirywtuto íusyrc
notiwy4 'l_x_stro wri_xo wom suwysso~ '
” método redirect_to envia ao browser do usuário um código de resposta
“￿￿￿” que signi￿ca “Moved Temporarily” \ dizendo ao navegador que ele deve ir para
outro endereço_ •o conteúdo da resposta\ um endere ço é informado\ fazendo o
browser seguir esta nova localiza ção_ øor sua vez\ passamos o modelo @user para
o redirect_to\ que\ como o form_for sabe montar a áÁ“ correta a partir do
objeto_ •este caso\ o Áails irá redirecionar para a a ção show com o zu do objeto
@user_
” segundo parâmetro do método redirect_to éu mh a s hd eo pções_ •esse
caso\ estamos usando um atalho para escrever uma mensagem via flash_
” flash é fundamentalmente um hash\ que nesse caso estamos escrevendo na
chave :notice_ øortanto a linha poderia ser reescrita da seguinte formak
￿￿

## Página 73

tasa do tódigo tapítulo ￿_ Íratando as requisi ções à eb
zl_sh/4notiwy3 h 'l_x_stro wri_xo wom suwysso~ '
ryxirywtuto íusyr
áma característica importante do flash é que seu conteúdo é guardado na
sessão do usuário e o conteúdo é descartado em toda requisi ção_ ®uando você es]
creve no flash\ o conteúdo só estará disponível na próxima requisição_ øor isso\ é
normalmente utilizado em conjunto com redireções_
winalmente\ se o objeto não pôde ser salvo\ executamosk
rynxyr _wtion4 4nyw
zsso porquê a ação create não possui um template‘apresentação para si\ então re]
aproveitamos o template donew para apresentar novamente o formulário e o usuário
ter a oportunidade de corrigir os dados_ tomo já obtivemos o modelo do usuário
na variável @user\ ela já estará disponível no template_ •ote que chamar o mé]
todo render não redireciona o usuário e também não executa a a ção indicada por
completo\ apenas usa o seu template_
￿￿￿￿￿￿￿￿_￿￿ ￿￿ ￿￿￿￿￿￿￿
É comum em a ções create e update redirecionar o usuário para uma
outra página quando tudo está certo_ øorém\ no caso de erros no objeto
não é recomendado redirecionar_ r razão é que\ ao redirecionar\ perde]
mos todos os parâmetros que o usuário enviou e também as mensagens
de erro de valida ção quando executamos o método #save_ øara essas
situações\ devemos usar o #render\ que não causa o redirecionamento_
￿n￿ õ ￿￿￿￿￿￿￿ ￿ ￿￿￿￿-￿￿￿￿￿￿￿￿￿￿
rgora que entendemos bem o que a a ção create faz\ vamos executá]laQ â á ao for]
mulário de cadastro Xhttpk‘‘localhostk￿￿￿￿‘users‘new Y e preencha o formulário_ ro
clicar em ‘treate áser’ ___
jwtivypoxyl44norvixxynjttrivutysmrror in "syrslontrollyr@wry_ty
r exce ção ForbiddenAttributesError ocorre quando usamos o params
para construir objetos sem listarmos\ manualmente\ todos atributos que podem ser
￿￿

## Página 74

￿_￿_ tontrole o massoassignment tasa do tódigo
atualizados a partir do formulário_ vsta situa ção é na verdade uma prote ção para
o seu site_ zmagine a situa ção hipotética em que tivéssemos o campo admin no
modelo User\ que é um campo booleano Xou seja\ aceita apenas valores true ou
falseY_
–esmo sem o campo admin existir no formulário\ um usuário mal intencionado
pode forjar uma requisição da seguinte formak
{
*usyr* h- {
*zullun_my*h-*%ir_t_ p_l_nxro* c
*low_tion*h-*l_rivy*c
*ym_il*h-*m_l_nxroíyx_mply:wom*c
*p_ssworx*h-*$eé*c
*p_ssworxuwonzirm_tion*h-*$eé*c
*vio*h-*+árr~ rou _xquirir _wysso xy _xmin~* c
*_xmin*h-*$*
}
}
–esmo seu formulário não tendo o campo admin\ o modelo User iria marcá]
lo como true e pronto\ facilmente um usuário pode forjar dados em seu sistema
sem você perceber_
” Áails ￿ introduziu um novo mecanismo para determinar quais campos são
seguros\ e para isso precisamos alterar o controle_
￿￿

## Página 75

tasa do tódigo tapítulo ￿_ Íratando as requisi ções à eb
í ￿￿￿￿￿￿￿￿￿￿ ￿￿ R￿￿￿￿￿
Ée você já conhece o Áails ￿\ vai notar que há uma grande diferen çak
os atributos não são mais marcados como seguros no modelo\ mas sim
no controle_ ” grande benefício é que mais de um controle pode alte]
rar um modelo\ dependendo da regra de negócio daquele controle_ øor
exemplo\ um administrador poderia alterar mais campos no painel de
administração do que um usuário comum_
”utra grande vantagem é a possibilidade de alterar modelos mais na]
turalmente em processos que não envolvam controles de requisições web\
como processamento de dados em background_
Ée você quiser ainda usar o mesmo mecanismo do Áails ￿ em um
projeto Áails ￿\ basta adicionar a gem protected_attributes no
Gemfile do seu projeto_ øor sua vez\ se quiser usar o novo mecanismo
em projetos Áails ￿\ basta instalar a usar a gem strong_parameters\
lembrando que não há necessidade de instalá]la em projetos Áails ￿_
øara criar uma lista de atributos permitidos\ vamos criar um método que irá
garantir que os parâmetros incluem apenas dados permitidosk
wl_ss "syrslontrollyr > jppliw_tionlontrollyr
@ :::
priv_ty
xyz usyrup_r_ms
@ )s *pontos* no zin_l x_ linh_ não são opwion_is~
p_r_ms:
ryquiry{4usyr}:
pyrmit{4ym_ilc 4zullun_myc 4low_tionc 4p_ssworxc
4p_ssworxuwonzirm_tionc 4vio}
ynx
ynx
–uita coisa está acontecendo neste método_ ørimeiro\ chamamos o mé]
todo require no objeto retornado pelo método params Xnote o “ponto” no
￿nal da linhak apenas estamos quebrando a linha para melhorar legibilidadeY_
￿￿

## Página 76

￿_￿_ tontrole o massoassignment tasa do tódigo
vste método irá veri ￿car pela presen ça da chave :user nos parâmetros vin]
dos do usuário_ Ée essa chave não existir\ o método irá disparar a exce ção
ActionController::ParameterMissing_ Ée existir\ os parâmetros presentes
a partir dessa chave serão retornados_
•a linha seguinte\ usamos o retorno do método require para fazer a veri ￿]
cação dos atributos_ –ais uma vez estamos usando o “ponto” no ￿nal da linha\ de
modo a encadear chamadas de métodos_ ” permit tem um papel diferentek ele irá
retornar um hash com apenas os parâmetros listados\ excluindo os outros atributos
não especi￿cados_
â eja o exemplo a seguir\ executados em uma mesma requisi ção_ ”
método params[:user] retorna todos os parâmetros dentro da chave
:user\ sem nenhum ￿ltro de mass assignment aplicado a ele_ ” método
params.require(:user).permit(:email, :full_name) irá ￿ltrar todos
os atributos com exce ção de :email e :full_name_ •o último exemplo\ colo]
camos a :bio a mais_
p_r_ms/4usyr3
@ {
@ *zullun_my*h-*?ysty*c
@ *low_tion*h-*tysty*c
@ *ym_il*h-*viniv_00ioí0m_il:wom*c
@ *p_ssworx*h-*$eéqwy*c
@ *p_ssworxuwonzirm_tion*h-*$eéqwy*c
@ *vio*h-*msty é um tysty xy vio p_r_ o lolwho:nyt*
@ }
p_r_ms:
ryquiry{4usyr}:
pyrmit{4ym_ilc 4zullun_my}
@ {
@ *ym_il*h-*viniv_00ioí0m_il:wom*c
@ *zullun_my*h-*?ysty*
@ }
p_r_ms:
ryquiry{4usyr}:
pyrmit{4ym_ilc 4zullun_myc 4vio}
@ {
@ *ym_il*h-*viniv_00ioí0m_il:wom*c
@ *zullun_my*h-*?ysty*c
￿￿

## Página 77

tasa do tódigo tapítulo ￿_ Íratando as requisi ções à eb
@ *vio*h-*msty é um tysty xy vio p_r_ o lolwho:nyt*
@ }
E￿￿￿￿￿￿￿ ￿￿￿￿￿￿￿￿ ￿￿￿￿ ￿ ￿￿￿￿￿￿￿
vnquanto desenvolvemos o colcho_net\ encontramos vá]
rias exce ções\ como RoutingError\ ou até mesmo o
ActionController::ParameterMissing_ øode parecer es]
tranho exibir essas exceções\ porém o Áails apenas faz isso em ambiente
de desenvolvimento\ para facilitar a depuração de bugs_
•o ambiente de produ ção\ essas exceções mapeiam para erros espe]
cí￿cos\ como “￿￿￿ •ot wound” \ “￿￿￿ sad Áequest” e\ se alguma exce ção
não for conhecida pelo Áails ou não for tratada pelo desenvolvedor\ o
Áails irá apresentar o erro “ ￿￿￿ znternal Éerver vrror” _ â eja uma lista
abaixo das exceções e a qual resposta elas são mapeadask
• íctionõontrollerzzRoutingError ] “￿￿￿ •ot wound”
• íbstractõontrollerzzíctionNotFound ] “￿￿￿ •ot wound”
• íctionõontrollerzzMethodNotíllowed ] “ ￿￿￿ –ethod •ot rl]
lowed”
• íctionõontrollerzzNotImplemented ] “￿￿￿•ot zmplemented”
• íctionõontrollerzzUnknownFormat ] “￿￿￿ •ot rcceptable”
• íctionõontrollerzzInvalidíuthenticityT oken ] “ ￿￿￿ ánproces]
sable vntity”
• íctionõontrollerzzóadRequest ] “￿￿￿ sad Áequest”
• íctiveRecordzzRecordNotFound ] “￿￿￿ •ot wound”
• íctiveRecordzzRecordInvalid ] “￿￿￿ ánprocessable vntity”
øara aplicar a prote ção de mass assignment\ basta alterar a linha que usamos
params[:user] e usar o método que acabamos de criar\ o user_params_ ” re]
sultado ￿nal do controle deverá ￿car da seguinte maneirak
￿￿

## Página 78

￿_￿_ vxibi ção do per￿l do usuário tasa do tódigo
wl_ss "syrslontrollyr > jppliw_tionlontrollyr
xyz nyw
íusyr h "syr:nyw
ynx
xyz wry_ty
@ õymvryçsy xy _ltyr_r _ linh_ _ sy0uir~
@ muxy xy p_r_ms/4usyr3 p_r_ usyrup_r_ms:
íusyr h "syr:nyw{usyrup_r_ms}
iz íusyr:s_vy
ryxirywtuto íusyrc
notiwy4 'l_x_stro wri_xo wom suwysso~ '
ylsy
rynxyr _wtion4 4nyw
ynx
ynx
priv_ty
xyz usyrup_r_ms
p_r_ms:
ryquiry{4usyr}:
pyrmit{4ym_ilc 4zullun_myc 4low_tionc 4p_ssworxc
4p_ssworxuwonzirm_tionc 4vio}
ynx
ynx
uepois dessas altera ções\ reenvie o formulário\ com todos os dados_ Ée não hou]
veram erros no formulário\ um novo erro será exibidok Unknown action Xação des]
conhecidaY\show_ rpesar do erro\ o caminho tomado no código foi o caminho de
sucesso e\ portanto\ o usuário é redirecionado para a ação show_ øara comprovar que
o objeto foi gravado\ vá ao console do Áailsk
@ kusw_ o último ovjyto no v_nwo xy x_xos {vi_ ix}
"syr:l_st
@>"syr ix4 $c zullun_my4 *riniwius*c :::-
￿n￿ E￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿
rgora vamos criar a a ção e o template de show\ para não haver mais erros_ øri]
meiro\ precisamos buscar o objeto no banco de dados\ de modo a popular os
￿￿

## Página 79

tasa do tódigo tapítulo ￿_ Íratando as requisi ções à eb
dados adequados na tela_ øara isso\ vamos criar um novo método no controle
UsersController\ que buscará o objeto no banco de dados e irá montar o tem]
plate com os dados desse objeto_
vm projetos Áails\ usamos o zu do objeto na rota_ ”u seja\ quando quisermos
renderizar a a ção show para o objeto de zu ￿\ basta seguirmos a rota /users/1_
”bserve a linha relativa a a ção show no comando rake %routes k
usyr 9m? ,usyrs,4ix{:4zorm_t} usyrs@show
L￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿
•o Áails ￿\ é possível visualizar todas as rotas de sua aplica ção den]
tro do browser\ basta visitar httpk‘‘localhostk￿￿￿￿‘rails‘info‘routes _v s s a
rota só está disponível no ambiente de desenvolvimento_
zsso signi￿ca que\ qualquer coisa após a segunda barra e que não contenha ponto
será disponibilizado como o parâmetro :id e\ qualquer coisa depois do ponto\ virá
como o parâmetro :format_ â eja alguns exemplosk
• /users/123 ] idk 123\ formatk nil
• /users/123.json ] idk 123\ formatk "json"
• /users/abcdef.xml ] idk abcdef\ formatk "xml"
â amos usar então o params[:id] para buscar o objeto no banco de dados_
rltere o arquivo app/controllers/users_controller.rbk
wl_ss "syrslontrollyr > jppliw_tionlontrollyr
xyz show
íusyr h "syr:zinx{p_r_ms/4ix3}
ynx
xyz nyw
íusyr h "syr:nyw
ynx
xyz wry_ty
íusyr h "syr:nyw{usyrup_r_ms}
￿￿

## Página 80

￿_￿_ vxibi ção do per￿l do usuário tasa do tódigo
iz íusyr:s_vy
ryxirywtuto íusyrc
notiwy4 'l_x_stro wri_xo wom suwysso~ '
ylsy
rynxyr _wtion4 4nyw
ynx
ynx
priv_ty
xyz usyrup_r_ms
p_r_ms:
ryquiry{4usyr}:
pyrmit{4ym_ilc 4zullun_myc 4low_tionc 4p_ssworxc
4p_ssworxuwonzirm_tionc 4vio}
ynx
ynx
E ￿￿￿￿￿￿ ￿ ￿￿ ￿￿￿ ￿￿￿￿￿￿￿
vxiste a possibilidade do usuário digitar um id não existente\ ou
um link estar incorreto_ ®uando isso acontecer\ o ActiveRecord irá
disparar uma exceção chamada ActiveRecord::RecordNotFound_
tomo já vimos anteriormente\ o Áails irá exibir um erro “ ￿￿￿ •ot
wound” \ que é exatamente o que deve ocorrer quando um objeto não
existe_
â amos ao template_ trie o arquivo app/views/users/show.html.erb
conforme o código a seguirk
>p ixh*notiwy*-<%= notiwy %> >,p-
>he-%yrzil4 <%= íusyr:zullun_my %> >,he-
>ul-
>li-õow_liz_ção4 <%= íusyr:low_tion %> >,li-
>li-kio4 <%= íusyr:vio %> >,li-
>,ul-
<%= linkuto 'mxit_r %yrzil 'c yxituusyrup_th{ íusyr} %>
￿￿

## Página 81

tasa do tódigo tapítulo ￿_ Íratando as requisi ções à eb
r estrutura desse template é um pouco diferente\ pois estamos usando menos
métodos auxiliares do Áails e mais yÍ–“_ •a verdade\ a estrutura de templates de
aplicações tendem a ser mais dessa forma\ uma mistura de yÍ–“ com pinceladas
de vÁs e métodos auxiliares_
” método notice é um método auxiliar do Áails para retornar o conteúdo do
flash[:notice]_ –as o método mais importante para nós neste momento é o
método link_to_
” método link_to serve para gerar links\ através da tag <a>_ ” primeiro
atributo é o texto que vai no link\ e o segundo é o endereço que o link irá direcionar
o usuário_
” método edit_user_path(@user) é um método gerado pelo roteador de
acordo com seu arquivo de rotas_ ” método edit_user_path(@user) vai gerar
a rota correta para a a ção de edit do usuário @user_
tom o template pronto\ quando você criar um novo usuário\ você verá a seguinte
imagemk
wigura￿_￿k øer￿l do usuário\ depois de efetuar um cadastro
￿n￿ P￿￿￿￿￿￿ ￿ ￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿
r imagem anterior mostra que temos uma tela bem simples\ mas já estamos come]
çando a amarrar toda a funcionalidade de cadastro_ rinda faltam as a ções de edit e
update_ vlas são bem parecidas com as ações new e create_
â amos primeiro à a ção edit_ ” que precisamos fazer nessa a ção é buscar o
objeto usuário no banco de dados e então vamos exibir o formulário com os da]
dos que o usuário já preencheu anteriormente_ â amos usar o que já aprende]
mos nas a ções new e showk para buscar o objeto\ vamos usar o mesmo código
￿￿

## Página 82

￿_￿_ øermita a edição do per￿l tasa do tódigo
da a ção show_ •o formulário\ basta lembrar que o form_for sabe tratar obje]
tos que já existem no banco de dados\ populando os campos para que o usuário
possa realizar alguma altera ção necessária_ â amos então ao UsersController X
app/controllers/users_controller.rbYk
wl_ss "syrslontrollyr > jppliw_tionlontrollyr
@ )mitinxo _s outr_s _çõys p_r_ não _tr_p_lh_r:::
@ show
@ nyw
@ wry_ty
xyz yxit
íusyr h "syr:zinx{p_r_ms/4ix3}
ynx
@ :::
ynx
” template da a ção edit Xapp/views/users/edit.html.erbY será quase o
mesmo da ação new\ vamos apenas alterar o títulok
>h$-mxit_r pyrzil >,h$-
<%= zormuzor íusyr xo |z| %>
>p-
<%= z:l_vyl 4zullun_my %> >vr ,-
<%= z:tyxtuziylx 4zullun_my %>
>,p-
>p-
<%= z:l_vyl 4low_tion %> >vr ,-
<%= z:tyxtuziylx 4low_tion %>
>,p-
>p-
<%= z:l_vyl 4ym_il %> >vr ,-
<%= z:tyxtuziylx 4ym_il %>
>,p-
>p-
<%= z:l_vyl 4p_ssworx %> >vr ,-
<%= z:p_ssworxuziylx 4p_ssworx %>
>,p-
￿￿

## Página 83

tasa do tódigo tapítulo ￿_ Íratando as requisi ções à eb
>p-
<%= z:l_vyl 4p_ssworxuwonzirm_tion %> >vr ,-
<%= z:p_ssworxuziylx 4p_ssworxuwonzirm_tion %>
>,p-
>p-
<%= z:l_vyl 4vio %> >vr ,-
<%= z:tyxtu_ry_ 4vio %>
>,p-
>p-
<%= z:suvmit %>
>,p-
<% ynx %>
rgora direcione o browser para a página de edi ção do modelo_ r rota é
/users/:id/edit\ então substitua :id pelo zu gerado pelo Áails anteriormente_
Í eremos o formulário já previamente preenchido com os dados do usuário e\ ao cli]
car no botão Update User\ que ainda não faz nada_
￿n￿ R￿￿￿￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿￿￿￿￿￿ ￿￿￿ ￿￿￿￿￿￿￿￿
Ée você comparar o formulário da página edit e new\ verá que as páginas são prati]
camente idênticas\ havendo apenas o título da página de diferença_ •ão é por acaso\
realmente queremos que os dois formulários sejam exatamente iguais_
” problema da solu ção que temos agora é que\ toda vez que quisermos alterar
o formulário\ será necessário alterar os dois arquivos_ vsse processo é um processo
altamente propenso a erros\ ou seja\ é bastante comum que esses dois arquivos não
￿quem a par depois de um tempo_ vxiste uma maneira melhor de resolver esse pro]
blema_
” componente de templates do Áails X ActionViewY possui um recurso cha]
mado partials\ que são mini]templates que podem ser embutidos em outros templa]
tes\ ou seja\ uma partial não é usada para renderizar diretamente uma a ção\ mas é
usada para compor um pequeno peda ço de uma página_
øara criar uma partial\ basta criar um template com seu nome iniciando em
__ ”u seja\ nesse caso\ vamos criar a partial “form” _ øortanto\ crie o arquivo
_form.html.erb\n ap a s t aapp/views/users/k
<%= zormuzor íusyr xo |z| %>
>p-
<%= z:l_vyl 4zullun_my %> >vr ,-
￿￿

## Página 84

￿_￿_ Áeaproveite as apresentações com partials tasa do tódigo
<%= z:tyxtuziylx 4zullun_my %>
>,p-
>p-
<%= z:l_vyl 4low_tion %> >vr ,-
<%= z:tyxtuziylx 4low_tion %>
>,p-
>p-
<%= z:l_vyl 4ym_il %> >vr ,-
<%= z:tyxtuziylx 4ym_il %>
>,p-
>p-
<%= z:l_vyl 4p_ssworx %> >vr ,-
<%= z:p_ssworxuziylx 4p_ssworx %>
>,p-
>p-
<%= z:l_vyl 4p_ssworxuwonzirm_tion %> >vr ,-
<%= z:p_ssworxuziylx 4p_ssworxuwonzirm_tion %>
>,p-
>p-
<%= z:l_vyl 4vio %> >vr ,-
<%= z:tyxtu_ry_ 4vio %>
>,p-
>p-
<%= z:suvmit %>
>,p-
<% ynx %>
vsse formulário é o que já vimos anteriormente_ tomo a partial está dentro do
contexto da ação\ apartial também possui acesso a todas as variáveis de instância do
controle_ tomo as a ções edit e new usam o mesmo nome de variável\ compartilhar
a partial que acabamos de criar entre as duas a ções é bastante simples_
rgora vamos aos templates app/views/users/new.html.erb e
app/views/users/edit.html.erbk
app/views/users/new.html.erbk
>h$-l_x_stro>,h$-
<%= rynxyr 'zorm' %>
• o t eq u eon o m ed apartial não deverá incluir o __ øor convenção\ o Áails sabe
que nomes de partials iniciam com _ e o incluirá automaticamente_
￿￿

## Página 85

tasa do tódigo tapítulo ￿_ Íratando as requisi ções à eb
app/views/users/edit.html.erbk
>h$-mxit_r pyrzil >,h$-
<%= rynxyr 'zorm' %>
uepois de editar os dois arquivos\ salve]os e navegue nas páginas_ ” funciona]
mento é o mesmo do anterior\ porém evitamos o “copiar e colar” \ que resulta em
trabalho repetitivo e propenso a erros_
rgora que os templates estão melhorados\ vamos implementar a a ção update_r
ação update será bem parecida com a ação create\ com a única diferença que\ ao invés
de criarmos um novo objeto\ vamos buscar o objeto existente do banco de dados e
atualizar seus atributos\ através do método update_ •ote que o método update
também é um método de mass assignment\ ou seja\ atualizará muitos atributos de
uma vez_ øor essa razão\ vamos ter que usar o método user_params\ que fará a
veri￿cação de atributos válidos a serem atualizados_
UPDATE ￿￿n UPDATE _ATTRIBUTES
•o Áails ￿\ foi introduzido o método update\ que se comporta da
mesma maneira que o update_attributes_ Ée você já conhece Áails
e está acostumado com a usar update_attributes\ ele ainda está dis]
ponível_
rbra o controle UsersController Xapp/controllers/users_controller.rbY
e crie o novo método updatek
wl_ss "syrslontrollyr > jppliw_tionlontrollyr
@ )mitinxo _s outr_s _çõys p_r_ não _tr_p_lh_r:::
@ nyw
@ show
@ wry_ty
xyz yxit
íusyr h "syr:zinx{p_r_ms/4ix3}
ynx
￿￿

## Página 86

￿_￿_ –ostre os erros no formulário tasa do tódigo
xyz upx_ty
íusyr h "syr:zinx{p_r_ms/4ix3}
iz íusyr:upx_ty{usyrup_r_ms}
ryxirywtuto íusyrc
notiwy4 'l_x_stro _tu_liz_xo wom suwysso~ '
ylsy
rynxyr _wtion4 4yxit
ynx
ynx
@ :::
ynx
Ée a atualização do per￿l ocorrer com sucesso\ o usuário é redirecionado para a
página do seu per ￿l\ contendo uma mensagem de sucesso\ como é possível ver na
￿gura ￿_￿
wigura￿_￿k rtualização de per￿l com sucesso
Ée na atualização ocorrer algum erro\ o formulário de edição será exibido nova]
mente\ com marcações em vermelho de forma que o usuário possa corrigir os dados_
￿n￿ M￿￿￿￿￿ ￿￿ ￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿￿￿
®uando o formulário é enviado com dados que não passam nas valida ções\ os cam]
pos ￿cam marcados com a cor vermelha_ zsso acontece pois o form_for automa]
ticamente adiciona classes tÉÉ aos campos do formulário que possuem erros_ zsso é
possível graças ao método errors\ que vimos anteriormente_
” sca￿old que geramos no capítulo ￿ já cria estilos tÉÉ de forma que os campos
￿￿

## Página 87

tasa do tódigo tapítulo ￿_ Íratando as requisi ções à eb
do formulário ￿quem com a cor vermelha\ destacando para o usuário quais campos
necessitam correção_
wigura￿_￿k –arca ção de erros no formulário
” principal problema desse formulário é que ele não informa exatamente oXsY
erroXsY ocorridos\ para que o usuário possa tomar uma decisão informada de como
corrigir o campo_ Éem nenhuma informação\ é praticamente impossível que o usuá]
rio entenda o que precisa ser alterado_ øor isso\ vamos adicionar essa dica_
tomo a partial do formulário é exibida tanto na a ção edit quanto na new\
a partial criada\ _form\ torna]se uma excelente candidata a receber a exibi ção
de erros_ øor isso\ vamos adicionar nessa partial todas as informa ções que o
método errors tiver\ caso o objeto esteja inválido_ øara isso\ abra o arquivo
app/views/users/_form.html.erb e adicione o seguinte código no início do
arquivok
<% iz íusyr:yrrors:_nyi %>
>xiv ixh*yrroruyxpl_n_tion*-
>he-onzylizmynty não zoi possívyl womplyt_r
_ _ção pois o zormulário possui os sy0uintys yrros4 >,he-
>ul-
<% íusyr:yrrors:zullumyss_0ys:y_wh xo |myss_0y|%>
￿￿

## Página 88

￿_￿_ –ostre os erros no formulário tasa do tódigo
>li-<%= myss_0y %> >,li-
<% ynx %>
>,ul-
>,xiv-
<% ynx %>
<%= zormuzor íusyr xo |z| %>
:::
<% ynx %>
” que esse código faz é veri ￿car se há algum erro Xo método #any? retorna
true se pelo menos um elemento de uma Array é diferente de nilY_ Ée houver
um ou mais erros\ cria]se a div com uma mensagem e em seguida lista todas as
mensagens de erro_ ” resultado é o seguintek
wigura￿_￿k –ensagem de erro com mensagem amigável
rgora o usuário pode ler a mensagem e tomar uma a ção para corrigir seus er]
ros_ ” funcionamento das páginas está correto\ porém vamos adicionar links para
melhorar a navegação_
￿￿

## Página 89

tasa do tódigo tapítulo ￿_ Íratando as requisi ções à eb
￿n￿ õ ￿￿￿￿￿￿￿￿ ￿ ￿￿￿￿ ￿￿￿￿ h￿￿￿￿ i
ra ção raiz\ ouroot\éaa ção que é executada quando vamos ao endereço raiz do site\
por exemplo\ httpk‘‘www_colcho_net\ ou httpk‘‘localhostk￿￿￿￿‘ _ ” que temos agora
é ainda a página de boas vindas do Áails_ â amos mudar isso_
øor padrão\ o Áails de￿ne a rota raiz como a página que vimos_ sasta criar a en]
trada root no arquivo config/routes.rb para apontar para a página principal\
que ainda vamos criark
lolwhonyt44jppliw_tion:routys:xr_w xo
rysourwys 4rooms
rysourwys 4usyrs
root 'homy@inxyx'
ynx
r nota ção de controles\ quando mencionados manualmente\ é o seu nome
Xpor exemplo\ “users” para o UsersControllerY\ sustenido X ￿\ ou tam]
bém ‘jogo da velha’Y e o nome da a ção_ uessa forma\ “home ￿index”
aponta para o controle HomeController\ a ção index_ trie o arquivo
app/controllers/home_controller.rbk
wl_ss #omylontrollyr > jppliw_tionlontrollyr
xyz inxyx
ynx
ynx
ó ￿￿ ￿￿￿￿￿￿￿z￿￿￿￿￿￿ ￿￿￿￿￿￿￿ ￿￿￿￿￿ ￿￿ ￿￿￿￿￿
®uando uma a ção não faz nada\ é possível simplesmente não im]
plementar nenhum método no controle e apenas criar o template_ ”
HomeController\ por exemplo\ não necessitaria do método index\
pois tem o template para exibir a página e não contém absolutamente
nada_
øorém\ é sempre interessante declarar todos os métodos que o con]
trole responde\ para que￿que claro ao leitor do código quais ações aquele
controle responde_
￿￿

## Página 90

￿_￿_ ton ￿gure a ação raiz XrootY tasa do tódigo
rgora\ crie a pasta app/views/home e o template
app/views/home/index.html.erbk
>h$-lolwho:nyt>,h$-
>p-
mswolh_ um_ x_s _çõys _ sy0uir4
>ul-
>li-<%= linkuto *l_x_stro*c nywuusyrup_th %> >,li-
>li-<%= linkuto *risu_liz_r qu_rtos* c roomsup_th %> >,li-
>,ul-
>,p-
rgora temos links para as principais páginas da nossa aplica ção até o momento_
â amos adicionar dois novos links\ para que o usuário possa desistir de cadastrar ou
atualizar o seu per￿lk
app/views/users/new.html.erbk
>h$-l_x_stro>,h$-
<%= rynxyr 'zorm' %>
<%= linkuto *rolt_r*c rootup_th %>
app/views/users/edit.html.erbk
>h$-l_x_stro>,h$-
<%= rynxyr 'zorm' %>
<%= linkuto *rolt_r*c íusyr %>
•ote que\ como as rotas são diferentes\ não colocamos na partial\ mas no tem]
plate em si_ •a a ção edit usamos a capacidade do Áails de determinar a rota de
show de um recurso\ apenas colocando o objeto como parâmetro_
øor ￿m\ vamos editar a página do per ￿l do usuário\
app/views/users/show.html.erb\ adicionando um link ao ￿nalk
:::
<%= linkuto 'mxit_r %yrzil 'c yxituusyrup_th{ íusyr} %>
<%= linkuto '#omy'c rootup_th %>
￿￿

## Página 91

tasa do tódigo tapítulo ￿_ Íratando as requisi ções à eb
rr o t a root_path é especial\ e aponta para a raiz do site_ øronto\ agora temos
interligação entre todas as páginas do site\ inclusive à área de quartos que deixa]
mos intocado por enquanto_ rgora vamos focar apenas nos modelos\ aprimorando
a qualidade dos dados armazenados_
￿￿

## Página 93

t ￿￿￿￿￿￿￿ ￿
–elhore o projeto
Se longe enxerguei foi porque me apoiei no ombro de gigantesp
– zsaac •ewton
￿n￿ L￿￿￿￿ ￿￿￿￿￿￿￿￿￿￿￿z￿￿￿￿￿￿ ￿￿￿￿￿￿￿ ￿￿￿￿￿￿￿￿￿￿￿￿
￿￿￿￿ ￿￿￿￿￿￿￿￿￿ ￿￿￿￿￿￿
vu tenho calafrios toda vez que faço um cadastro em um site e recebo um email com a
minha senha\ que deveria ser algo secreto_ ” problema que este email revela é gravek
a senha está sendo armazenada em texto puro\ sem nenhuma cifra ou encripta ção_
–esmo sendo um problema resolvido\ não é rara a notícia de que algum site de al]
guma importância tenha seu banco de dados vazado e distribuídos_ v o colcho_net\
por enquanto\ não é nem um pouco diferente_
"syr:zirst
@ >"syr ix 4 $c
@ zullun_my 4 *riniwius*c

## Página 94

￿_￿_ “i ção obrigatóriak sempre aplique criptogra￿a para armazenar senhas tasa do tódigo
@ ym_il 4 *viniv_00ioíyx_mply:wom*c
@ p_ssworx 4 *sy0ryxo*c
@ low_tion 4 *q_n nr_nwiswoc lj*c
@ vio 4 *) myu pyrzil _ntyrior:::*c
@ wry_tyxu_t 4 *ed$eçd=çe$ d84é!4éê*c
@ upx_tyxu_t 4 *ed$eçd=çee d= 4 é= 4 85*-
øara resolver esse problema\ basta usar uma funcionalidade embutida
no Áails\ que usa a encripta ção strypt_ vssa funcionalidade chama]se
has_secure_password e\ para usá]la\ precisamos fazer as seguintes alterações no
modelo ásuáriok
￿Y ásar a funcionalidade has_secure_password no modelol
￿Y triar a coluna password_digestl
￿Y tifrar a senha atual do usuáriol
￿Y ueletar a coluna passwordl
￿￿

## Página 95

tasa do tódigo tapítulo ￿_ –elhore o projeto
E￿￿￿￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿
” algoritmo usado pelo Áails para cifrar senhas é o strypt_ •esse
algoritmo\ a senha em texto puro passa por cálculos matemáticos que a
torna cifrada_ vsse processo é irreversível\ ou seja\ uma vez calculada a
cifra\ é impossível fazer a volta_
øara veri￿car a validade de uma senha\ fornecemos o que o usuário
digitar ao algoritmo_ tomparamos o resultado ￿nal com o que está ar]
mazenado_ Ée os resultados forem os mesmos\ o usuário digitou a senha
corretamente_
” strypt é usado pois as chances de colisão são muito pequenas\ ou
seja\ duas cadeias de caracteres diferentes raramente terão a mesma cifra
￿nal_ øor isso\ se o banco de dados vazar\ não será possível usar as senhas
dos usuários_
vste não é um processo infalível mas é estatisticamente seguro_ rnti]
gamente usava]se algoritmos como –u ￿ e Éyr ￿\ mas já provou]se que
são ruins\ pois há maiores chances de colisão_
øor ￿m\ jamais invente o seu próprio mecanismo\ por mais que a
ideia soe tentadora_ triptogra ￿a é um dos problemas mais difíceis da
computação e eu recomendo que deixamos isso na mão de especialistas_
￿n￿ õ ￿￿￿ ￿￿￿￿￿￿￿￿￿ ￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿
” Áails não implementa o algoritmo strypt\ portanto é necessário instalar uma gem
que implementa esse algoritmo_ r gem é a bcrypt-ruby e\ para que o Áails consiga
usá]la\ abra o arquivo Gemfilek
@ ?o usy jwtivypoxyl h_susywuryup_ssworx
0ym 'vwryptçruvy'c '~- é:d:d '
vm seguida\ no terminal\ vá à raiz do projeto e execute o comando bundlek
ã vunxly
"sin0 r_ky {$d:$:d}
"sin0 i$fn {d:=:ê}
"sin0 minityst {ê:!:8}
￿￿

## Página 96

￿_￿_ ásando hasúsecureúpassword no modelo tasa do tódigo
"sin0 multiujson {$:!:!}
"sin0 _tomiw {$:$:$d}
:::
"sin0 _ryl {ê:d:d}
"sin0 _wtivyryworx {ê:d:d}
onst_llin0 vwryptçruvy {é:d:$} with n_tivy yxtynsions
"sin0 vunxlyr {$:é:d}
:::
7our vunxly is womplyty~
vsse comando instalará a gem em seu sistema_ ” arquivo Gemfile e o comando
bundle fazem parte de uma ferramenta chamada sundler X httpk‘‘gembundler_
com‘Y _ vla é uma ferramenta para o gerenciamento de dependências de aplicati]
vos Áuby_ ” Áails usa]o para carregar todas as bibliotecas com as versões corretas_ ”
trabalho pesado ￿ca para a ferramenta\ nos resta apenas manter o arquivoGemfile
organizado_
rpós a execu ção do bundle\ o bundler irá gerar uma nova versão do
Gemfile.lock\ que contém exatamente todas as dependências e versões de gems
que satisfazem as dependências da aplicação Áails_ rbrindo esse arquivo\ dá para ver
todas as dependências de uma gem_
R￿￿￿￿￿￿￿￿￿￿ ￿ ￿￿￿￿￿￿￿ ￿ ￿ ￿￿￿￿￿￿￿￿
vm mudan ças como essa\ é necessário reiniciar tanto o console
quanto o servidor\ mesmo com o uso doreload!_ tomo o Áails carrega
suas dependências no momento que é iniciado\ portanto o reload!
conseguirá levar em conta essas alterações_
￿n￿ U￿￿￿￿￿ ￿￿￿ _￿￿￿￿￿￿_￿￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿
znstalada a gem\ alteraremos o modelo_ Éegundo a documenta ção do
has_secure_password Xprocure por has_secure_password no site
httpk‘‘api_rubyonrails_orgpara detalhesY\ essa class macro já nos dá as valida]
ções de con￿rmação de senha e a presença de senha_ rlém disso\ ela cria dois novos
atributos virtuais\ o password e password_confirmation_
rnteriormente fazíamos essas valida ções manualmente\ portanto temos que
tirá]las\ substituindo pelo uso da class macro has_secure_password_ tomo im]
￿￿

## Página 97

tasa do tódigo tapítulo ￿_ –elhore o projeto
plementamos usando os mesmos nomes de atributos\ não é necessário alterar ne]
nhum formulário_
rlteremos o modelo usuário X app/model/user.rbY da seguinte formak
wl_ss "syr > jwtivy+yworx44k_sy
mpjoõu+m9m;% h ,tj/2í3]í{/2ít:3]t:}]/2ít:3]tz,
@ õymvryçsy xy tir_r _s v_lix_çõys xy synh_~
@ ) h_susywuryup_ssworx já o z_z p_r_ vowê:
v_lix_tysuprysynwyuoz 4ym_ilc 4zullun_myc 4low_tion
v_lix_tysulyn0thuoz 4vioc minimum4 édc _llowuvl_nk4 z_lsy
v_lix_tysuzorm_tuoz 4ym_ilc with4 mpjoõu+m9m;%
h_susywuryup_ssworx
ynx
tom essas altera ções no modelo\ já temos todo o código necessário para encrip]
tar as senhas\ só resta as alterações de banco de dados_
￿n￿ M￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿ ￿￿￿￿￿
” has_secure_password requer que modelos possuam a coluna
password_digest no banco de dados\ portanto vamos criá]la_ vxecute\ na
pasta raiz do projeto\ o comando que irá gerar a migraçãok
ã r_ils 0 mi0r_tion _xxup_ssworxuxi0ystutouusyrs p_ssworxuxi0yst
invoky _wtivyuryworx
wry_ty xv,mi0r_ty,ed$éd!$5d8df8du_xxup_ssworxuxi0ystutouusyrs:rv
r migra ção irá criar um arquivo_ ” nome do dele irá variar conforme a hora que
o comando foi executado\ mas a saída irá mostrar o caminho que você pode usar
para editá]lo_
wl_ss jxx%_ssworx<i0yst?o"syrs > jwtivy+yworx44pi0r_tion
xyz wh_n0y
_xxuwolumn 4usyrsc 4p_ssworxuxi0ystc 4strin0
ynx
ynx
vxecutemos a migra ção com a tarefa rake rake db:migrate k
￿￿

## Página 98

￿_￿_ –igra ção da tabela users tasa do tódigo
ã r_ky xv4mi0r_ty
hh jxx%_ssworx<i0yst?o"syrs4 mi0r_tin0 hhhhhhhhhhhhhhhhh
çç _xxuwolumn {4usyrsc 4p_ssworxuxi0ystc 4strin0 }
ç- d:de5es
hh jxx%_ssworx<i0yst?o"syrs4 mi0r_tyx {d:de5=s} hhhhhhhh
P￿￿ ￿￿￿ ￿￿￿ ￿￿￿￿￿￿￿ ￿￿￿￿￿ ￿￿￿￿￿ ￿ ￿￿￿￿￿￿￿
vssa é uma pergunta natural de ser feita\ e a resposta é simples_ É
raro o dia em que sabemos toda a modelagem do nosso sistema logo de
início_ É certo que um dia será necessário alterar o modelo por causa de
alguma decisão tomada ou algum conhecimento adquirido_ ” Áails dá
ferramentas para dar suporte a esse tipo de desenvolvimento\ ao invés de
gastar dias e dias com modelagem\ o Áails abraça a ideia do crescimento
orgânico de um sistema_
áma vez o banco de dados migrado\ podemos usar a funcionalidade por
completo_ •o exemplo a seguir\ vamos criar um novo objeto usando os mé]
todos password= e password_confirmation=_ vm seguida\ vamos bus]
car esse objeto do banco de dados e veri ￿car se a senha está correta_ â amos
usar o método authenticate\ adicionado automaticamente pela class macro
has_secure_password\ que irá retornar false quando a senha estiver inválida e
o próprio objeto quando estiver corretak
v h "syr:nyw
@ h- @>"syr ix4 nilc
@ zullun_my4 nilc
@ ym_il4 nilc
@ low_tion4 nilc
@ vio4 nilc
@ wry_tyxu_t4 nilc
@ upx_tyxu_t4 nilc
@ p_ssworxuxi0yst4 nilc
@ p_ssworx4 nil-
v:zullun_my h 'riniwius k_00io nuyntys '
@ h- *riniwius k_00io nuyntys*
v:ym_il h 'viniv_00ioíyx_mply:wom'
￿￿

## Página 99

tasa do tódigo tapítulo ￿_ –elhore o projeto
@ h- *viniv_00ioíyx_mply:wom*
v:low_tion h 'q_n nr_nwiswoc ljc m"j '
@ h- *q_n nr_nwiswoc ljc m"j*
v:vio h '<ysynvolvyxor syvc prinwip_lmynty wom +uvy on +_ils '
@ h- *<ysynvolvyxor syvc prinwip_lmynty wom +uvy on +_ils*
v:p_ssworx h 'sy0ryxo'
@ h- *sy0ryxo*
v:p_ssworxuwonzirm_tion h 'sy0ryxo'
@ h- *sy0ryxo*
v:s_vy~
u h "syr:zinxuvyuym_il 'viniv_00ioíyx_mply:wom'
@ h- @>"syr ix4 5c ::: -
u:_uthyntiw_ty 'inv_lixo'
@ h- z_lsy
u:_uthyntiw_ty 'sy0ryxo'
@ h- @>"syr ix4 5c ::: -
â amos usar esse mecanismo no capítulo ￿ com mais detalhes para fazer o con]
trole do login do usuário\ mas já podemos garantir a qualidade do armazenamento
das senhas_ vm seguida\ vamos atualizar os dados antigos\ de modo a funcionarem
com o novo mecanismo_
￿n￿ í ￿￿￿￿￿￿￿￿￿￿￿￿ ￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿￿￿ ￿￿￿
￿￿￿￿
” sistema neste momento ainda possui as senhas antigas armazenadas no campo
password_ øorém\ agora que usamos o has_secure_password\ o método
password já não age da forma anterior -- retornar o resultado da coluna no banco
de dadosk
usyr
@ h- @>"syr ix4 fc
@ zullun_my4 *?ysty*c
@ ym_il4 *viniv_00io]$eéíyx_mply:wom*c
@ p_ssworx4 *$eé$eé*c
@ low_tion4 *tysty*c
@ vio4 *msty é um tysty xy vio p_r_ o lolwho:nyt*c
￿￿

## Página 100

￿_￿_ rutomatizando tarefas de manuten ção com rake tasa do tódigo
@ wry_tyxu_t4 *ed$eç$eç$e d=4ee4êê*c
@ upx_tyxu_t4 *ed$eç$eç$e d=4ee4êê*c
@ p_ssworxuxi0yst4 nil-
usyr:p_ssworx
@ h- nil
øor isso\ para acessar os dados brutos do banco de dados\ podemos usar o mé]
todo attributes\ que retorna a hash com todos os valoresk
usyr:_ttrivutys
{*ix*h-fc
*zullun_my*h-*?ysty*c
*ym_il*h-*viniv_00io]$eéí0m_il:wom*c
*p_ssworx*h-*$eé$eé*c
*low_tion*h-*tysty*c
*vio*h-*msty é um tysty xy vio p_r_ o lolwho:nyt* c
*wry_tyxu_t*h-syxc $e <yw ed$e d= 4ee4êê "?l ]dd4ddc
*upx_tyxu_t*h-?uyc ee ó_n ed$é d8 4ê54éé "?l ]dd4ddc
*p_ssworxuxi0yst*h-nil}
øara encriptar a senha que temos no banco de dados\ vamos criar uma tarefa
rake_ rs tarefas rake são comandos executados no terminal que alteram o estado
atual do sistema_ Í odas as tarefasrakes devem ￿car na pasta lib/tasks e devem
ser um arquivo do tipo .rake_
r tarefa rake precisará ler a senha do banco de dados e vamos associar aos atri]
butos password e password_confirmation de todos os usuários_ zsso fará com
que o has_secure_password faça o trabalho de encriptar a senha_ triaremos o
arquivo lib/tasks/migrar_senhas.rakek
@ ynwoxin04 utzçf
n_mysp_wy 4_pp xo
xysw *mnwript_ tox_s _s synh_s t
quy _inx_ não zor_m prowyss_x_s t
no v_nwo xy x_xos*
t_sk mi0r_rusynh_s4 4ynvironmynt xo
ynx
ynx
￿￿

## Página 101

tasa do tódigo tapítulo ￿_ –elhore o projeto
O￿￿￿￿￿ ￿￿￿￿z ￿￿￿ ￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿
￿￿￿￿￿￿
” comentário na primeira linha do arquivo não é opcional_ ” co]
mentário # encoding: utf-8 indica ao interpretador Áuby que o ar]
quivo deverá ser processado como utf-8 e\ portanto\ aceitará caracteres
não rÉtzz_ “embre]se de con ￿gurar seu editor para salvar o arquivo em
modo utf-8Q
r anatomia de tarefas rake é a seguintek
• ám namespace\ ou seja\ um nome para agrupar todas as suas tarefas\ de
modo que não haja con ￿ito com tarefas previamente de ￿nidas_ •esse caso\
chamamos de app_
• áma descri ção da tarefa\ para tentar explicar de forma sucinta o que a tarefa
irá fazer\ via o comando desc_
• r tarefa deve vir logo em seguida à chamada desc_ ” parâmetro é o
nome da tarefa que vamos executar no console\ junto com a sua dependên]
cia_ •esse exemplo\ o nome da tarefa é migrar_senhas e ela depende da
tarefa environment\ que carregará o ambiente Áails_
tom apenas isso já é possível observar o resultado quando executamos a listagem
de tarefas rake do projetok
ã r_ky ç?
:::
r_ky _pp4mi0r_rusynh_s @ mnwript_ tox_s _s
synh_s quy _inx_ não
zor_m prowyss_x_s no
v_nwo xy x_xos
:::
â amos ao código_ ørimeiro\ vamos veri￿car se as senhas já foram migradas_ â a]
mos usar a existência da coluna password no banco de dados_ Ée ela não mais
existir\ todas as migrações já foram executadas e portanto não é possível mais mi]
grar os dados_
￿￿

## Página 102

￿_￿_ rutomatizando tarefas de manuten ção com rake tasa do tódigo
vm seguida\ vamos alterar todos os usuários no banco de dados_ ásaremos o
método find_each\ que busca objetos em lotes de ￿￿￿￿_ vvitamos assim carregar
todos os objetos em memória\ que pode causar problemas sérios em um servidor_
tom o objeto em mãos\ basta ler o atributo do banco de dados direta]
mente\ sem usar os acessores\ e sobrescrevemos\ usando os métodos gerados pelo
has_secure_password_ ” resultado é o seguintek
@ ynwoxin04 utzçf
n_mysp_wy 4_pp xo
xysw *mnwript_ tox_s _s synh_s quy
_inx_ não zor_m prowyss_x_s no v_nwo xy x_xos*
t_sk mi0r_rusynh_s4 4ynvironmynt xo
unlyss "syr:_ttrivutyun_mys:inwluxyi *p_ssworx*
puts *js synh_s já zor_m mi0r_x_sc tyrmin_nxo:*
ryturn
ynx
"syr:zinxuy_wh xo |usyr|
puts *pi0r_nxo usuário @@{ usyr:ix} @{ usyr:zullun_my}*
unynwriptyxup_ssworx h usyr:_ttrivutys/*p_ssworx*3
usyr:p_ssworx h unynwriptyxup_ssworx
usyr:p_ssworxuwonzirm_tion h unynwriptyxup_ssworx
usyr:s_vy~
ynx
ynx
ynx
øara executar\ vá ao terminal e executek
ã r_ky _pp4mi0r_rusynh_s
pi0r_nxo usuário @= óoão
pi0r_nxo usuário @! ?ysty
pi0r_nxo usuário @f ?ysty
￿￿

## Página 103

tasa do tódigo tapítulo ￿_ –elhore o projeto
E￿￿￿￿ ￿￿ ￿ ￿￿￿￿￿￿￿￿
É muito provável que você tenha erros de valida ção e a tarefa rake
termine abruptamente_ zsso é esperado\ já que é possível que você tenha
criado usuários antes de termos criados as valida ções_ â ocê tem duas
opçõesk pode corrigir os modelos que estão gravados no banco ou apenas
pode deletá]los_
áma vez os dados migrados\ podemos criar a migra ção para remover a coluna
que não usamos mais_ ” procedimento é o mesmo do que ￿zemos anteriormente --
geraremos uma migração\ adicionaremos o código e a executaremosk
ã r_ils 0 mi0r_tion rymovyup_ssworxuzromuusyrs
invoky _wtivyuryworx
wry_ty xv,mi0r_ty,ed$éd!$5d8$édfurymovyup_ssworxuzromuusyrs:rv
wl_ss +ymovy%_ssworxnrom"syrs > jwtivy+yworx44pi0r_tion
xyz up
rymovyuwolumn 4usyrsc 4p_ssworx
ynx
xyz xown
_xxuwolumn 4usyrsc 4p_ssworxc 4strin0
ynx
ynx
”bserve que nessa migra ção não usamos o método #change_ ” Áails não con]
segue gerar a migra ção contrária a partir da remo ção da coluna\ já que não espe]
ci￿camos o tipo da coluna_ øor esse motivo\ criamos os métodos #up e #down
manualmente_
ã r_ky xv4mi0r_ty
hh +ymovy%_ssworxnrom"syrs4 mi0r_tin0 hhhhhhhhhhhhhhhh
çç rymovyuwolumn {4usyrsc 4p_ssworx }
ç- d:dê8és
hh +ymovy%_ssworxnrom"syrs4 mi0r_tyx {d:dê8ês} hhhhhhh
￿￿

## Página 104

￿_￿_ –elhoria de templates e tÉÉ tasa do tódigo
￿n￿ M￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿￿ ￿ õSS
rté agora estamos usando o tÉÉ gerado pelo sca￿old do Áails_ vmbora seja funcio]
nal\ ele é bem cruk
wigura￿_￿k Éite com o layout do sca￿old
”s formulários são visualmente agressivosk
wigura￿_￿k wormulário com erro
￿￿

## Página 105

tasa do tódigo tapítulo ￿_ –elhore o projeto
tom um pouco de yÍ–“ e tÉÉ\ deixaremos o site mais bonito Xconsiderando
a minha falta de habilidade com artes visuaisYk
wigura￿_￿k •ova home
â amos também melhorar a exibição de erros para que as mensagens￿quem lado
a lado aos campos a serem corrigidosk
￿￿

## Página 106

￿_￿_ –elhoria de templates e tÉÉ tasa do tódigo
wigura￿_￿k wormulário com melhor noti￿cação de erros
øara fazer isso\ trabalharemos na camada de apresentação do site\ alterando tem]
plates\ criando tÉÉ e criando métodos auxiliares para tornar a constru ção do tem]
plate mais fácil_
õ ￿￿￿￿￿￿￿￿￿￿￿￿ ￿￿ HTML ￿ õSS
znfelizmente não dá para explicar em detalhes cada parte do que va]
mos fazer em seguida\ pois este não é o foco do livro_ Ée você gostaria
de aprender mais sobre esses assuntos Xrecomendado se você quiser se
tornar um pro￿ssional completo de webY\ recomendo a leitura do livro
HTML￿ e íSS ￿” óomine a web do futuro \ escrito pelo “ucas –azza_
￿￿

## Página 107

tasa do tódigo tapítulo ￿_ –elhore o projeto
￿n￿ T￿￿￿￿￿￿￿ ￿￿￿ ￿￿￿￿￿￿ ￿ ￿￿￿￿￿￿￿￿￿ ￿￿￿￿ ￿￿￿￿￿ m
￿￿￿ ￿￿￿ ￿￿￿￿￿￿￿￿￿￿￿￿
” primeiro passo é alterar o layout da aplicação para incluir o cabeçalho com o menu\
na direita_ rlém disso\ vamosk
• zncluir o código tÉÉ usar a fonte “øaci ￿co” \ disponível no xoogle à eb wonts\
para o logotipo Xnão se preocupe se você não tiver acesso a internet\ vamos
usar fontes fallbackYl
• r cria ção da tag header e seu conteúdo\ o logotipo e o menu de navegaçãol
• vmbrulhar o yield em uma tag content\ para centralizar todo o conteúdo
dos templates_
rltere o arquivo app/views/layouts/application.html.erb para que
ele ￿que da seguinte formak
<!DOCTYPE html>
>html-
>hy_x-
>titly-lolwho(yt>,titly-
>link hryzh'http4,,zonts:0oo0ly_pis:wom,wssiz_milyh%_wiziwo'
rylh'stylyshyyt' typyh'tyxt,wss'-
<%= stylyshyytulinkut_0 *_ppliw_tion*c
myxi_4 *_ll*c
*x_t_çturvolinksçtr_wk* h- truy %>
<%= j_v_swriptuinwluxyut_0 *_ppliw_tion*c
*x_t_çturvolinksçtr_wk* h- truy %>
<%= wsrzumyt_ut_0s %>
>,hy_x-
>voxy-
>hy_xyr-
>xiv ixh*hy_xyrçwr_p*-
>h$-<%= linkuto *wolwho:nyt*c rootup_th %> >,h$-
>n_v-
>ul-
>li-<%= linkuto *.u_rtos*c roomsup_th %> >,li-
>li-<%= linkuto *l_x_stro*c nywuusyrup_th %> >,li-
>,ul-
￿￿

## Página 108

￿_￿_ Írabalhe com layout e templates para melhorar sua apresenta ção tasa do tódigo
>,n_v-
>,xiv-
>,hy_xyr-
>xiv ixh*wontynt*-
<% iz notiwy:prysynti %>
>p ixh*notiwy*-<%= notiwy %> >,p-
<% ynx %>
<% iz _lyrt:prysynti %>
>p ixh*_lyrt*-<%= _lyrt %> >,p-
<% ynx %>
<%= yiylx %>
>,xiv-
>,voxy-
>,html-
â amos tirar a referência aoflash da ação show do usuário controle de usuários
e alterar a tag h2 para h1k
>h$-%yrzil4 <%= íusyr:zullun_my %> >,h$-
>ul-
>li-õow_liz_ção4 <%= íusyr:low_tion %> >,li-
>li-kio4 <%= íusyr:vio %> >,li-
>,ul-
<%= linkuto 'mxit_r %yrzil 'c yxituusyrup_th{ íusyr} %>
tomo agora temos o nome do site e o menu em todas as páginas\ aquela página
inicial Xou “home”Y que criamos na seção ￿_￿ ￿ca redundante_ â amos alterá]la para
mostrar ao usuário até três quartos que já foram cadastrados_
rntes de alterar o template\ porém\ precisamos alterar o controle
HomeController para buscar os três quartos mencionados anteriormente_
ásaremos o método .take que retornará objetos do banco de dados\ sem ordem
determinada_ øodemos passar um número para esse método\ que irá limitar o
número de objetos retornados_ øor￿m\ a consulta É®“ resultante ék
qmõml? *rooms*:[ n+)p *rooms* õopo? é
vdite portanto o arquivo app/controllers/home_controller.rbk
￿￿

## Página 109

tasa do tódigo tapítulo ￿_ –elhore o projeto
wl_ss #omylontrollyr > jppliw_tionlontrollyr
xyz inxyx
írooms h +oom:t_ky{é}
ynx
ynx
rgora vamos editar o template do controle HomeController\a ção index Xar]
quivo app/views/home/index.html.erbYk
>h$-.u_rtos rywém post_xos >,h$-
>ul-
<% írooms:y_wh xo |room| %>
>li-<%= linkuto *@{room:titly}c @{ room:low_tion}*c room %> >,li-
<% ynx %>
>,ul-
tom essas altera ções será possível observar a listagem de quartos\ caso você te]
nha cadastrado algum objeto no banco de dados_ øorém\ há um pequeno problema
no template anterior que devemos corrigir_
â ocê pode estar se perguntandok “qual o problema desse códigop” _ v a resposta
é simplesk esse é um típico caso em que estamos violando uma regra de negócio
que parece inofensivak o nome completo de um quarto_ –as em casos como esse
é comum que os programadores acabem repetindo a composi ção diversas vezes em
templates espalhados_ v o dia que a lógica for alterada\ será necessário realizar vários
“buscar e substituir” _ øara manter o código consistente\ vamos fazer do jeito certok o
template deve saber o mínimo possível de como o modelo é feito_
rbra agora o então intocado modelo Room Xapp/models/room.rbY e adici]
one o método #complete_namek
wl_ss +oom > jwtivy+yworx44k_sy
xyz womplytyun_my
*@{titly}c @{ low_tion}*
ynx
ynx
â oltando ao template Xapp/views/home/index.html.erbYk
>h$-.u_rtos rywém post_xos >,h$-
>ul-
<% írooms:y_wh xo |room| %>
>li-<%= linkuto room :womplytyun_myc room %> >,li-
￿￿

## Página 110

￿_￿_ ” que é o rsset øipelinep tasa do tódigo
<% ynx %>
>,ul-
rntes de come çarmos a modi￿car os stylesheets XtÉÉsY da aplicação\ vamos parar
um pouco e entender mais sobre um dos componentes mais controversos\ em minha
opinião\ do Áails_
￿n￿ O ￿￿￿ ￿ ￿ í ￿￿￿￿P￿￿￿￿￿￿￿￿
” ésset Pipeline veio para resolver um problema complicado da web modernak a
entrega de assets\ ou arquivos estáticos_ ” que parece simples como a entrega de um
arquivo javascript ou stylesheet ao browser do usuário pode se tornar uma tarefa
complicada_
tomo as aplica ções web tem se tornado complexas\ diversas ferramentas estão
sendo usadas para tornar o desenvolvimento de javascripts e stylesheets mais produ]
tivo_ rlém disso\ é necessário diminuir ao máximo o tempo que o browser leva para
baixar e processar esses arquivos\ para que as aplicações web não passem a percepção
de serem lentas_
uessa forma\ é comum que aplica ções web possuam uma ou mais das seguintes
fases para a entrega de um arquivo estáticok
￿Y øré]compilaçãok Íransformação de um ÉtÉÉ ou “vÉÉ em tÉÉ puro\ ou to ￿eeÉ]
cript em {avaÉcriptl
￿Y toncatena çãok {untar todos os arquivos tÉÉ ou {avaÉcript em apenas uml
￿Y “–ini ￿caçãoRk uso de técnicas para diminuir o tamanho dos scripts\ como reno]
mear variáveis Xde “essaâ ariavelvhxrande” para “a”Yl
￿Y tompressãok ásar compressão xêip para diminuir ainda mais o tamanho do
arquivo\ caso o browser tenha suporte Xtodos os browsers modernos possuem
esse suporteY_
SõSS ￿ õ ￿￿￿￿￿S￿￿￿￿￿ ￿￿￿ ￿￿￿￿￿￿￿￿￿
øor padrão\ o Áails já instala ÉrÉÉ Xe por consequência\ ÉtÉÉY e tof]
feeÉcript em seu projeto_ øorém\ o uso de ÉtÉÉ e to￿eeÉcript é opcional\
ou seja\ você pode continuar escrevendo {avaÉcript e tÉÉ puro e ainda
aproveitar dos outros benefícios do rssets øipeline_
￿￿￿

## Página 111

tasa do tódigo tapítulo ￿_ –elhore o projeto
vm conjunto com o processo anterior\ existe outra preocupaçãokcaching_ rlém
do seu browser\ existem diversos elementos de rede que podem fazer caching de aso
sets\ como seu provedor de internet\ ￿rewalls\ tu•s X íontent óelivery Network \o u
rede de entrega de conteúdoY\ equipamentos de rede XroteadoresY\ entre outros_ ”
problema é que\ quando você atualiza um arquivo no servidor\ o conteúdo desse ar]
quivo pode estar emcache e portanto os usuários do site podem receber um conteúdo
antigo_
” ésset Pipeline ajuda na resolução de todos os problemas mencionados\ desde
que estejamos dispostos a cooperar com ele\ ou seja\ seguir as suas convenções_
ørimeiro\ o Áails\ através de uma biblioteca chamada sprockets\ lê cada ma]
nifesto da sua aplica çãol um arquivo que contém diretivas declarando quais são os
arquivos em que seu aplicativo depende_
tom essa lista de arquivos\ o Áails compila cada um de acordo com as extensões
utilizadas_ øor exemplo\ se o nome do seustylesheet for users.css.scss.erb\o
stylesheet vai primeiro ser pré]processado em vÁb e\ em seguida\ ÉrÉÉ XÉrÉÉ e ÉtÉÉ
são pré]processados pelo próprio ÉrÉÉY\ gerando um arquivo tÉÉ ￿nal_
rpós obter todos os arquivos pré]compilados\ o Áails irá juntar todos os arquivos
de um manifesto e gerará um arquivo com mesmo nome_ øor exemplo\ se o mani]
festo application.css mencionar os arquivos footer.css e reset.css e
o manifesto admin.css mencionar apenas o reset.css\ o resultado ￿nal desse
processo serão dois arquivos\ o application.css\ contendo o footer.css eo
reset.css concatenados e o admin.css\ apenas o reset.css_
r razão desse processo é que cada browser possui um limite de quantos arquivos
ele baixará simultaneamente_ øor exemplo\ se o seu site usa dez imagens e o browser
possui limite de cinco downloads simultâneos\ o sexto arquivo só será baixado a par]
tir do momento que um dos cinco downloads anteriores terminarem_ vsses valores
podem variar de acordo com o browser e com o seu site\ mas em geral\ concatenar
os arquivos dessa forma é uma boa estratégia_
rpós a concatena ção\ o que acontece é a mini ￿cação_ ” Áails Xou mais especi]
￿camente\ o sprocketsY gera uma versão mini￿cada de cada arquivo gerado no
passo anterior_ ” processo de mini ￿cação gera um arquivo javascript ou stylesheet
completamente válido\ mas ilegível_ Áeduzir o arquivo dessa maneira possui duas
implicações importantesk diminuir o tempo que o browser tem para baixar o ar]
quivo e\ consequentemente\ inicia o download de outros arquivos bloqueados pelo
browser\ se houver_
thegando ao ￿nal do processo\ o Áails calcula o digest –u ￿ do arquivo e adici]
￿￿￿

## Página 112

￿_￿_ triando os novos stylesheets tasa do tódigo
ona ao nome do arquivo_ øor exemplo\ se o arquivo chama]seapplication.css\
ele se tornará algo parecido comk
_ppliw_tionçydê5_=êd!dê$8=yê$ez=yy!5x__vw!z=:wss
vsse código gerado depende do conteúdo do arquivo\ portanto se uma nova ver]
são desse asset for gerada\ o código será alterado_ zsso fará com que o mecanismo de
caching não seja acionado caso uma nova versão do asset seja compilada_
øor ￿m\ há a compressão desses assets com o algoritmo xêip\ gerandok
_ppliw_tionçydê5_=êd!dê$8=yê$ez=yy!5x__vw!z=:wss:0z
tom o suporte a xêip de servidores como rpache X httpk‘‘httpd_apache_org‘Yo u
nginx Xpronuncia]se “engine x” \ ou ênginéxY Xhttpk‘‘httpk‘‘nginx_com‘Y e dos brow]
sers\ a entrega dessesarquivos torna]se muito mais e￿ciente\ diminuindo ainda mais
o tempo total de carga_
•ote que\ para esse mecanismo funcionar\ é estritamente necessário que execu]
temos a pré]compilação desses assets nos servidoresk
r_ky _ssyts4prywompily
zsso irá gerar os arquivos de assets\ que não serão entregues pelo Áails\ mas sim
pelo seu servidor web_
•o modo de desenvolvimento de aplica ções Áails\ que é o modo que estamos
executando\ as coisas são um pouco mais simples_ ro invés de serem concate]
nados e compactados\ os assets são apenas pré]compilados automaticamente por
cada página_ É possível ver no yÍ–“ gerado que há tags de inclusão de javas]
cript‘stylesheets para cada arquivo mencionado no manifesto_
rgora que entendemos um pouco do que é o rsset øipeline\ vamos usá]lo para
criar stylesheets para o tolcho_net_
￿n￿ õ ￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿ ￿￿￿￿￿￿￿￿￿￿￿
rbra o arquivo app/assets/stylesheets/application.css_ â ocê pode ver
que não há nenhum código tÉÉ de fato\ mas há um conjunto de comentários impor]
tantes que estão lá para compor o que chamamos de “manifestoRk
,[
[h ryquiryusylz
[h ryquiryutryy :
[,
￿￿￿

## Página 113

tasa do tódigo tapítulo ￿_ –elhore o projeto
vsses dois comentários são diretivas do sprockets Xnote o “n” na linhaY_ ”
require_self faz com que qualquer tÉÉ que esteja no arquivo do manifesto seja
incluído antes do restante\ e o require_tree varre toda a árvore de diretórios a
partir do diretório especi￿cado Xno caso\ “ _ ” \ ou pasta atualY e inclui osstylesheets no
manifesto_
zsso nos diz\ em termos práticos\ que qualquer tÉÉ que incluirmos na pasta
app/assets/stylesheets/ será incluído no manifesto ￿nal\ e isso é su ￿ciente
para nós_
•ão vamos utilizar o estilo gerado pelo sca￿old\ então vamos deletá]lo_ øara isso\
basta apagar o arquivo app/assets/stylesheets/scaffolds.css.scss_
â ocê pode apagar também o tÉÉ gerado pelo sca￿old para o controle
RoomsControllerk app/assets/stylesheets/rooms.css.scss_
â amos começar a criar o nosso próprio stylesheet_ tomo a maioria dos brow]
sers não possuem padrões razoáveis\ é comum usar um stylesheet chamado reset\
que deixa todos os estilos em um mesmo padrão para que\ a partir daí\ possamos
construir o nosso próprio_
É recomendado usar um reset popular e que já foi testado em vários browsers_
” “vric –eyer’ s Áeset” X httpk‘‘meyerweb_com‘eric‘tools‘css‘reset‘ Y é recomendado\
porém\ caso você não possua internet\ vamos usar um reset bem simpli￿cado_ trie
o arquivo app/assets/stylesheets/reset.css da seguinte formak
[ {
m_r0in4 d g
p_xxin04 d g
tyxtçxywor_tion4 nonyg
}
li { listçstyly4 nonyg }
vsse tÉÉ deixa o padding e a margin em valores zerados_ •ão contempla
diversos browsers\ porém serve como uma base_ vm seguida\ veremos em blocos o
tÉÉ ￿nal do site_
trie o arquivo app/assets/stylesheets/default.css.scss_ •ote que
esse não é um arquivo de tÉÉ comum e portando deve ter a extensão .scss_ zsso
signi￿ca que esse tÉÉ é um ÉtÉÉ\ uma extensão de tÉÉ que adiciona funcionalidades
como regras aninhadas\ variáveis\ mixins e outros_ øara entender como funciona o
ÉtÉÉ\ veja o site o￿cial do projeto ÉrÉÉ Xhttpk‘‘sass]lang_comY_
r primeira parte é a declara ção de variáveis em ÉtÉÉ\ de forma a centralizar
algumas con￿gurações globaisk
￿￿￿

## Página 114

￿_￿_ triando os novos stylesheets tasa do tódigo
ãhy_xyrçhyi0ht4 88 pxg
ãwontyntçwixth4 !dd pxg
ãsyrizçz_miliys4 *%_wiziwo*c *9yor0i_*c syrizg
ãs_nsçsyrizçz_miliys4 *#ylvytiw_*c s_nsçsyrizg
ãyrrorçtyxtçwolor4 @k5êjêf g
ãsuwwyssçtyxtçwolor4 @ê=ffê! g
vm seguida\ declaramos o estilo geral da página\ como cor do fundo\ tamanho e
família da fonte do texto do site Xusando a variável $sans-serif-familiesYk
[ {
zontçz_mily4 ãs_nsçsyrizçz_miliysg
zontçsizy4 $ê pxg
}
voxy { v_wk0rounxçwolor4 @z8z8z8 g }
ueclaramos um mixin para facilitar a declara ção de box-shadow\ colocando
todos os vendor pre￿xes quando necessáriok
ímixin sh_xow{ãwolorc ãxc ãyc ãr_xius} {
çmozçvoxçsh_xow4 ãwolor ãx ãy ãr_xius g
çwyvkitçvoxçsh_xow4 ãwolor ãx ãy ãr_xius g
voxçsh_xow4 ãwolor ãx ãy ãr_xius g
}
vm seguida\ vamos criar a barra de navegação\ que￿ca no topo_ triamos a cor de
fundo da barra e uma sombra na parte inferior_ triamos também o#header_wrap\
que é responsável pelo alinhamento do conteúdo da barra de navegação em conjunto
com o conteúdo_ øor￿m\ estilizamos o logotipo_ •ote que vamos usar omixin criado
anteriormente via @include\ evitando ter que repetir três regras para cada vendor
pre￿x_
hy_xyr {
íinwluxy sh_xow{@wwwc dc é pxc = px}g
vorxyrçvottom4 $ px solix @=f=g
m_r0inçvottom4 $8 pxg
￿￿￿

## Página 115

tasa do tódigo tapítulo ￿_ –elhore o projeto
@hy_xyrçwr_p {
wixth4 ãwontyntçwixthg
m_r0in4 d _utog
}
hyi0ht4 ãhy_xyrçhyi0htg
v_wk0rounxçwolor4 @5mlm!$ g
h$ {
zlo_t4 lyztg
_ {
wolor4 @ééé g
zontçz_mily4 ãsyrizçz_miliysg
zontçwyi0ht4 êdd g
zontçsizy4 e:8 ymg
\4hovyr {
wolor4 @ddd g
}
}
}
}
r segunda parte da barra superior\ o estilo do menu de navega çãok
hy_xyr n_v {
zlo_t4 ri0htg
ul {
xispl_y4 inlinyçvlowkg
vyrtiw_lç_li0n4 mixxlyg
linyçhyi0ht4 88 pxg
}
li {
xispl_y4 inlinyçvlowkg
linyçhyi0ht4 eê pxg
v_wk0rounxçwolor4 @8ê=zéw g
p_xxin04 é px $dpxg
çmozçvorxyrçr_xius4 8 pxg
vorxyrçr_xius4 8 pxg
vyrtiw_lç_li0n4 mixxlyg
￿￿￿

## Página 116

￿_￿_ triando os novos stylesheets tasa do tódigo
_ {
xispl_y4 vlowkg
zontçsizy4 $e pxg
zontçwyi0ht4 =dd g
wolor4 @zzz g
}
}
}
” estilo do conteúdo das páginas ￿cará dentro da div
com id content\ como deixamos no layout da aplica ção X
app/views/layouts/application.html.erbY_ •ote como podemos
fazer referência a um seletor pai usando &_
@wontynt {
tyxtç_li0n4 lyztg
wixth4 ãwontyntçwixthg
m_r0in4 d _utog
h$ {
zontçsizy4 $:8 ymg
}
_c _4visityxc _4hovyr {
wolor4 @eêe g
\4hovyr {
tyxtçxywor_tion4 unxyrlinyg
}
}
ulc zormc p {
m_r0in4 $d px dg
}
}
øara o formulário\ temos o seguinte tÉÉk
zorm {
l_vyl {
xispl_y4 vlowkg
m_r0in4 8 px dg
￿￿￿

## Página 117

tasa do tódigo tapítulo ￿_ –elhore o projeto
wolor4 @êêê g
}
input/typyhtyxt3c input/typyhp_ssworx3c tyxt_ry_ {
wolor4 @êêê g
zontçsizy4 $e pxg
vorxyr4 $ px solix @wwwg
p_xxin04 8 pxg
wixth4 edd pxg
outliny4 d g
íinwluxy sh_xow{r0v_{dcdcdc d:$ }c d pxc d pxc f px}g
\4zowus {
vorxyr4 $ px solix @w5w5w5g
}
}
tyxt_ry_ {
wixth4 êdd pxg
hyi0ht4 edd pxg
}
}
øor ￿m\ temos as classes relacionadas com a informação de erros e flashk
:ziylxuwithuyrrors {
xispl_y4 inlinyg
l_vyl { wolor4 ãyrrorçtyxtçwolorg }
input/typyhtyxt3c input/typyhp_ssworx3c tyxt_ry_ {
vorxyr4 $ px solix r0v_{$f5c!êc!ec d:8 }g
íinwluxy sh_xow{r0v_{$f5c!êc!ec d:e }c d pxc d pxc f px}g
\4zowus { vorxyr4 $ px solix r0v_{$f5c!êc!ec d:= }g }
}
}
:yrrorumyss_0y {
m_r0inçlyzt4 8 pxg
xispl_y4 inlinyg
wolor4 ãyrrorçtyxtçwolorg
￿￿￿

## Página 118

￿_￿￿_ weedback em erros de formulário tasa do tódigo
}
:p_xxyxuzl_sh {
p_xxin04 $d pxg
m_r0in4 $d px dg
zontçwyi0ht4 volxg
wixth4 8dd pxg
}
@yrroruyxpl_n_tion {
vorxyr4 $ px solix ãyrrorçtyxtçwolorg
wolor4 ãyrrorçtyxtçwolorg
v_wk0rounxçwolor4 @ne<m<m g
íyxtynx :p_xxyxuzl_shg
}
@notiwy {
wolor4 ãsuwwyssçtyxtçwolorg
vorxyr4 $ px solix ãsuwwyssçtyxtçwolorg
íyxtynx :p_xxyxuzl_shg
v_wk0rounxçwolor4 @<nnd<fg
}
@_lyrt {
wolor4 ãyrrorçtyxtçwolorg
vorxyr4 $ px solix ãyrrorçtyxtçwolorg
íyxtynx :p_xxyxuzl_shg
v_wk0rounxçwolor4 @ne<m<mg
}
Éalve o arquivo e navegue_ rgora sim\ bem melhorQ –as ainda não concluímos\
precisamos corrigir o formulário de erros\ que exigirá algumas mudan ças no tem]
plate_
￿n￿￿ F￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿￿￿
â amos limpar o formulário de cadastro de usuário_ Áemoveremos as tags <br/>\
pois os labels já possuem layout de bloco X display: block Y e simpli￿caremos a
noti￿cação de erros\ já que ￿ca difícil para o usuário entender o que deverá corrigir_
tolocando as mensagens logo ao lado do campo\ o usuário consegue agir muito mais
￿￿￿

## Página 119

tasa do tódigo tapítulo ￿_ –elhore o projeto
rapidamente_ â eja o exemplo para o campo “full name” \ ou “nome completoRk
>p-
<%= z:l_vyl 4zullun_my %>
<%= z:tyxtuziylx 4zullun_my %>
<% iz íusyr:yrrors:h_sukyyi 4zullun_my %>
>xiv wl_ssh*yrrorumyss_0y*-
<%= íusyr:yrrors/4zullun_my3:zirst %>
>,xiv-
<% ynx %>
>,p-
•o código anterior\ veri￿camos se há algum erro no atributo full_name_t a s o
isso seja verdade\ criamos uma tag div com classe error_message e mostramos
então o primeiro erro\ apenas para simpli￿car a tela_
wigura￿_￿k tampo com noti ￿cação de erro
￿n￿￿ D￿￿￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿￿￿￿￿ ￿￿￿￿￿
￿￿￿￿nU￿￿ ￿￿H￿￿￿￿￿￿
ro expandir as altera ções para exibi ção de erros para os outros campos\ nota]se
como o código ￿nal ￿ca repetitivo_ ”s problema é que\ para cada campo do for]
mulário\ repetimos uma lógica Xum ifY_ wazer uma alteração parecida para o for]
mulário de quartos seria bastante trabalhoso e ￿ca clara a necessidade de se corrigir
este problema_
•ão faz sentido\ porém\ colocar esse tipo de lógica em qualquer uma das cama]
das que vimos\ ou seja\ esse código não pertence nem a controles e nem a modelos_
øor essa razão\ o Áails disponibiliza um local para você colocar esse tipo de lógicak
view helpers\ ou conhecido apenas como helpers_
￿￿￿

## Página 120

￿_￿￿_ uuplica ção de lógica na apresentação nunca mais_ áse os yelpers tasa do tódigo
õ ￿￿￿￿￿￿ ￿￿￿ ￿￿￿￿￿￿ ￿￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿
“embre]se que código complexo pode ser um mal sinal\ ainda pior
quando eles estão em helpers_ Ée você encontrar helpers com muitas li]
nhas de código\ ou muito if\ tome isso como um alerta -- você pode
estar escrevendo regras de negócio na camada errada\ ou ainda\ tentando
fazer muita coisa em um lugar só_ rs maneiras de resolver esse problema
são mover regras de negócio para a sua camada\ ou então criar classes
que estruturam os dados de formas mais adequadas para os templates_
triaremos então o primeiro helper_ ”s geradores do Áails criam um ar]
quivo de helper por controle Xpor exemplo\ rooms_helper.rb para o
controle RoomsControllerY e é uma boa maneira de organizá]los_ øorém\
como vamos usar o helper em outros controles\ vamos colocar no helper ge]
ral\ o ApplicationHelper_ •esse helper\ vamos colocar o resultado da ex]
tração do código do template como um método_ øortanto\ abra o arquivo
app/helpers/application_helper.rbk
moxuly jppliw_tion#ylpyr
xyz yrrorut_0{moxylc _ttrivuty}
iz moxyl:yrrors:h_sukyyi _ttrivuty
wontyntut_0{
4xivc
moxyl:yrrors/_ttrivuty3:zirstc
wl_ss4 'yrrorumyss_0y'
}
ynx
ynx
ynx
”s métodos dos helpers são inclusos no mesmo contexto dos templates\ portanto
temos acesso aos modelos via variáveis de instância\ da mesma forma que fazemos
no template_ øorém\ usá]las é desaconselhado\ já que geramos uma dependência
do código que não ￿ca clara_ uessa forma\ passaremos o modelo como parâmetro\
seguido pelo atributo que queremos veri ￿car a existência de erros_ ” restante é o
mesmo que ￿zemos quando direto no template\ com a diferença de que\ ao invés de
gerar o yÍ–“ manualmente\ usamos um helper do Áails para criar a tag_
￿￿￿

## Página 121

tasa do tódigo tapítulo ￿_ –elhore o projeto
yá uma outra maneira de resolver o problemak retornar o yÍ–“ como texto e
imprimir o resultado no template\ mas não é recomendado_ r razão é que o Áails\
por padrão\ faz o escaping de todo o conteúdo que não é marcado como seguro\
evitando injeção de código malicioso_ øortanto\ é mais seguro e mais simples usar os
métodos do próprio Áails_ ” resultado visual é o mesmo\ mas o template ￿ca muito
mais limpok
>p-
<%= z:l_vyl 4zullun_my %>
<%= z:tyxtuziylx 4zullun_my %>
<%= yrrorut_0 íusyrc 4zullun_my %>
>,p-
Áepetindo essa altera ção no restante dos campos\ o template
app/views/users/_form.html.erb ￿ca assimk
<% iz íusyr:yrrors:_nyi %>
>xiv ixh*yrroruyxpl_n_tion*-
#á yrros no zormulárioc por z_vor vyriziquy:
>,xiv-
<% ynx %>
<%= zormuzor íusyr xo |z| %>
>p-
<%= z:l_vyl 4zullun_my %>
<%= z:tyxtuziylx 4zullun_my %>
<%= yrrorut_0 íusyrc 4zullun_my %>
>,p-
>p-
<%= z:l_vyl 4low_tion %>
<%= z:tyxtuziylx 4low_tion %>
<%= yrrorut_0 íusyrc 4low_tion %>
>,p-
>p-
<%= z:l_vyl 4ym_il %>
<%= z:tyxtuziylx 4ym_il %>
<%= yrrorut_0 íusyrc 4ym_il %>
>,p-
>p-
<%= z:l_vyl 4p_ssworx %>
<%= z:p_ssworxuziylx 4p_ssworx %>
￿￿￿

## Página 122

￿_￿￿_ uuplica ção de lógica na apresentação nunca mais_ áse os yelpers tasa do tódigo
<%= yrrorut_0 íusyrc 4p_ssworx %>
>,p-
>p-
<%= z:l_vyl 4p_ssworxuwonzirm_tion %>
<%= z:p_ssworxuziylx 4p_ssworxuwonzirm_tion %>
<%= yrrorut_0 íusyrc 4p_ssworxuwonzirm_tion %>
>,p-
>p-
<%= z:l_vyl 4vio %>
<%= z:tyxtu_ry_ 4vio %>
<%= yrrorut_0 íusyrc 4vio %>
>,p-
>p-
<%= z:suvmit %>
>,p-
<% ynx %>
Éalve o arquivo e envie o formulário\ com erros\ e veja o resultado do trabalho_
sem melhor\ não é mesmop tomo exercício\ adicione algumas validações no modelo
Room\ faça as alterações no formulário para usar o helper e veja o resultado_
￿￿￿

## Página 123

t ￿￿￿￿￿￿￿ ￿
waça sua aplicação falar várias
línguas
Lembrarose que morreremos um dia é a melhor forma que conheçop a r ae v i t a ra
armadilha de pensar que temos algo a perderp
– Éteve {obs
￿n￿ O ￿￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿￿￿￿￿￿￿￿￿￿￿￿hI￿￿￿i
rté então\ todos os formulários estão em inglês\ inclusive as mensagens de erro_ wi]
zemos dessa forma de propósito\ pois vamos usar o sistema de internacionaliza ção
Xapesar de\ em português\ a palavra “internacionalização” possuir ￿￿ letras\ em in]
glês ela possui ￿￿\ internationalization\ e portanto é comumente abreviada por z [ ￿￿
letras [ n\ ou i ￿￿nY do próprio Áails_
” sistema de z ￿￿n do Áails funciona com uma árvore de pares chave valor\ sendo
que a chave é um identi ￿cador de uma mensagem e o valor é o seu texto_ Í odo o

## Página 124

￿_￿_ ” processo de internacionaliza ção Xz￿￿nY tasa do tódigo
conjunto de mensagens possui uma chave raiz que é o uma sigla representando o
idioma_ vssa árvore é armazenada em um arquivo é r–“_ â amos a um exemplo
hipotéticok
ptçk+4
usyrs4
si0nuup4
suwwyss4 l_x_stro ry_liz_xo wom suwysso:
z_ilyx4 (ão zoi possívyl ry_liz_r o w_x_stro:
vssa árvore representa duas mensagens no idioma português\ a mensagem de su]
cesso e a de erro_ øara para acessar uma mensagem\ basta montar uma string com a
sequência dos passos da árvore_ •o caso da mensagem de sucesso\ precisamos mon]
tar a string "users.sign_up.success"_ •ote que não mencionamos o idioma\
pois isso é con￿gurado de maneira global -- uma vez que con￿guramos o sistema de
z￿￿n com um idioma\ todas as chaves a serem traduzidas usarão esse mesmo idioma_
M￿￿ ￿￿￿￿ ￿￿ ￿ ￿￿ ￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿￿l ￿￿￿￿￿￿￿ ￿￿￿￿ ￿ I￿￿￿￿
É considerada uma boa prática deixar seu sistema sempre traduzido
c o moz￿￿n_ r vantagem é que os templates ￿carão muito mais limpos e
mais fáceis de serem revistos por pessoas não técnicas_
•a pasta config/locales ￿cam os arquivos contendo as tradu ções_ Ée você
abrir o arquivo config/locales/en.yml\ que já vem com o Áails\ você observará
a seguinte estruturak
yn4
hyllo4 *#yllo worlx*
zsso signi￿ca que\ quando o sistema estiver usando olocale “en” XinglêsY\ quando
traduzirmos a chave hello\ o resultado será “yello world” _
”s contribuidores do Áails já ￿zeram a tradu ção dos erros de valida ção para
o português e portanto vamos usá]la como ponto de partida_ saixe o arquivo
de tradu ção Xvá para httpk‘‘colcho_net‘rails]i￿￿n e clique em “Áaw”Y e salve como
config/locales/rails.pt-BR.yml_ ” nome do arquivo não importa\ mas va]
mos separar nossas mensagens das mensagens do Áails para organização_
￿￿￿

## Página 125

tasa do tódigo tapítulo ￿_ waça sua aplicação falar várias línguas
rpós salvar o arquivo\ vamos alterar o idioma padrão do tolcho_net para por]
tuguês brasileiro_ øara isso\ abra o arquivo config/application.rb e altere as
linhas que estão comentadas por padrão para que ￿quem da seguinte formak
@ qyt ?imy:zony xyz_ult to thy spywiziyx zony
@ _nx m_ky jwtivy +yworx _utoçwonvyrt to this zony:
@ +un *r_ky ç< timy* zor _ list oz
@ t_sks zor zinxin0 timy zony n_mys: <yz_ult is "?l:
wonzi0:timyuzony h 'kr_sili_'
@ ?hy xyz_ult low_ly is 4yn _nx _ll
@ tr_nsl_tions zrom wonzi0,low_lys,[:rvcyml _ry _uto lo_xyx:
@ +_ils:_ppliw_tion:wonzi0:i$fn:lo_xup_th
@ ]h <ir/+_ils:root:join{ 'my'c 'low_lys'c '[:{rvcyml}'}:tous3
wonzi0:i$fn:xyz_ultulow_ly h 4*ptçk+*
É necessário reiniciar o servidor para que o Áails possa carregar as novas con ￿]
gurações_ vm seguida\ vá a um dos formulários e tente enviar os dados em branco_
ﬀt voilàQ vrros em portuguêsk
wigura￿_￿k vrros traduzidos com o sistema de i￿￿n
”s nomes dos atributos ainda continuam em inglês_ øara traduzi]los\ te]
mos que seguir as conven ções do Áailsk activerecord.models.<modelo>\
substituindo <modelo> pelo nome do modelo\ de modo a traduzir o tra]
duzir o botão “treate áser” \ por exemplo_ øara atributos\ o caminho é um
pouco mais longok activerecord.attributes.<modelo>.<atributo>_
￿￿￿

## Página 126

￿_￿_ ” processo de internacionaliza ção Xz￿￿nY tasa do tódigo
â amos aplicar essas tradu ções ao modelo User\ portanto crie o arquivo
config/locales/pt-BR.ymlk
ptçk+4
_wtivyryworx4
moxyls4
usyr4 "suário
_ttrivutys4
usyr4
vio4 kio0r_zi_
ym_il4 mm_il
zullun_my4 (omy womplyto
low_tion4 õow_liz_ção
p_ssworx4 qynh_
p_ssworxuwonzirm_tion4 lonzirmy su_ synh_
vm seguida\ reinicie o servidor do Áails e atualize a página para ver os resultados_
â amos colocar os atributos também para quartosk
ptçk+4
_wtivyryworx4
moxyls4
room4 .u_rto
usyr4 "suário
_ttrivutys4
usyr4
vio4 kio0r_zi_
ym_il4 mm_il
zullun_my4 (omy womplyto
low_tion4 õow_liz_ção
p_ssworx4 qynh_
p_ssworxuwonzirm_tion4 lonzirmy su_ synh_
room4
xyswription4 <yswrição
low_tion4 õow_liz_ção
titly4 ?ítulo
®uando o arquivo é r–“ já existe e apenas foi modi ￿cado\ o Áails levará em
conta as alterações\ portanto não é necessário reiniciar o servidor_ rssim\ vá ao for]
mulário de novos quartos e veri￿que se os campos foram traduzidos corretamente_
￿￿￿

## Página 127

tasa do tódigo tapítulo ￿_ waça sua aplicação falar várias línguas
wigura￿_￿k wormulário com atributos traduzidos
￿n￿ T￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿￿
rgora que temos a integra ção de z ￿￿n com o ActiveRecord\ vamos traduzir os
templates_ øara isso\ vamos ter que chamar o mecanismo de z￿￿n manualmente_ zsso
é feito com helpers t Xatalho para translateY\ para tradução das chaves que já
vimos\ e l Xatalho para localizeY para a localização de datas\ ou seja\ mostrar
uma data no formato do idioma em uso_
â amos traduzir a página de cadastro\ que possui apenas um título X
app/views/users/new.html.erbY_ Írocamos o texto “tadastro” pela tradução
da chave users.new.titlek
￿￿￿

## Página 128

￿_￿_ Íraduza os templates tasa do tódigo
>h$-<%= t 'usyrs:nyw:titly' %> >,h$-
<%= rynxyr 'zorm' %>
<%= linkuto t{ 'links:v_wk'}c rootup_th %>
â eja o resultado\ mesmo sem criar a tradução no é r–“_ ” Áails imprime a úl]
tima chave numa tentativa de não deixar a página em branco_ øorém\ o Áails gera
um yÍ–“ especí ￿co para chaves não traduzidask
>h$-
>sp_n wl_ssh*tr_nsl_tionumissin0*
titlyh*tr_nsl_tion missin04 ptçk+:usyrs:nyw:titly* -
?itly
>,sp_n-
>,h$-
:::
øara corrigir isso\ vamos ao é r–“ de tradu ção X
config/locale/pt-BR.ymlY e adicionamos as chaves que acabamos de
criar_
ptçk+4
usyrs4
nyw4
titly4 l_x_stro
links4
v_wk4 rolt_r
_wtivyryworx4
@ wontinu_ :::
ro recarregar a página\ veremos o título e o link traduzidos corretamente_
￿￿￿

## Página 129

tasa do tódigo tapítulo ￿_ waça sua aplicação falar várias línguas
D￿￿￿z￿￿￿￿￿￿ ￿￿￿￿ ￿ ￿￿￿￿￿￿õSS “ ￿￿￿￿￿￿￿￿￿￿￿_￿￿￿￿￿￿￿”
•o ambiente de desenvolvimento\ podemos colocar um tÉÉ es]
pecí￿co para ajudar a identi ￿car onde faltam elementos para serem
traduzidos_ áma maneira de se fazer isso é criar um novo tÉÉ\
app/assets/stylesheets/translation_missing.css.erb\
com o seguinte conteúdok
<% iz +_ils:ynv:xyvylopmynti %>
:tr_nsl_tionumissin0 {
vorxyr4 épx x_shyx ryxg
}
<% ynx %>
rssim\ textos a serem traduzidos possuirão uma marcação visual\ sem
impactar ambientes de produção ou testes_
yá uma melhoria que podemos fazer_ ” Áails automaticamente coloca o nome
do controle e da ação no “escopo” das chaves de tradução caso você queira\ bastando
iniciar a chave com “ _ ” _ øor exemplo\ se mudarmos o título para.title\ a chave
utilizada será users.new.title_ vm um outro exemplo\ no controle de quartos\
ação index\ac h a v es e r i arooms.index.title_ â amos aplicar esse atalhok
>h$-<%= t ':titly' %> >,h$-
<%= rynxyr 'zorm' %>
<%= linkuto t{ 'links:v_wk'}c rootup_th %>
wazendo o mesmo na ação edit Xapp/views/users/edit.html.erbYk
>h$-<%= t ':titly' %> >,h$-
<%= rynxyr 'zorm' %>
<%= linkuto t{ 'links:v_wk'}c íusyr %>
T￿￿￿￿￿￿￿￿ ￿￿￿￿ ￿￿￿￿￿￿￿
”s templates de quarto podem ser traduzidos da mesma
maneira_ rproveite para fazer o mesmo nos outros tem]
plates de quartok app/views/rooms/new.html.erb e
app/views/rooms/edit.html.erb_
￿￿￿

## Página 130

￿_￿_ Íraduza os templates tasa do tódigo
ra ção show será um pouco diferente_ tomo no título temos o nome do usuário\
precisaremos descobrir como passar parâmetros para o sistema de z ￿￿n_ zsso é feito
usando a notação %{}_ â eja como￿ca o título dessa páginak
ptçk+4
usyrs4
nyw4
titly4 l_x_stro
yxit4
titly4 mxit_r pyrzil
show4
titly4 *%yrzil4 b{usyrun_my}*
yxit4 'mxit_r pyrzil '
low_tion4 *õow_liz_ção4 b{low_tion}*
vio4 *kio4 b{vio}*
@ :::
â eja que o uso de aspas é obrigatório para esse caso_ øara passar os parâmetros\
basta passar um hash mapeando os atributos a serem interpoladosk
>h$-<%= t ':titly'c usyrun_my4 íusyr:zullun_my %> >,h$-
>ul-
>li-<%= t ':low_tion'c low_tion4 íusyr:low_tion %> >,li-
>li-<%= t ':vio'c vio4 íusyr:vio %> >,li-
>,ul-
<%= linkuto t{ ':yxit'}c yxituusyrup_th{ íusyr} %>
øor ￿m\ vamos à partial de formulário X
app/views/users/_form.html.erbYk
<% iz íusyr:yrrors:_nyi %>
>xiv ixh*yrroruyxpl_n_tion*-
<%= t '0ynyr_l:zormuyrror' %>
>,xiv-
<% ynx %>
:::
”l a y o u t(app/layouts/application.html.erbYk
￿￿￿

## Página 131

tasa do tódigo tapítulo ￿_ waça sua aplicação falar várias línguas
:::
>n_v-
>ul-
>li-<%= linkuto t{ 'l_yout:rooms'}c roomsup_th %> >,li-
>li-<%= linkuto t{ 'l_yout:si0nup'}c nywuusyrup_th %> >,li-
>,ul-
>,n_v-
:::
v no é r–“ X config/locales/pt-BR.ymlYk
@ :::
links4
v_wk4 rolt_r
l_yout4
rooms4 .u_rtos
si0nup4 l_x_stro
0ynyr_l4
zormuyrror4 #á yrros no zormulárioc por z_vor vyriziquy:
_wtivyryworx4
@ :::
øronto\ todos os templates estão prontos para receberem outros idiomas_ •o
próximo capítulo\ iremos trabalhar na última parte da funcionalidade de cadastrok o
envio de e]mail de boas vindas e con ￿rmação de conta_ øorém\ antes de chegarmos
lá\ vamos ver como trocamos o idioma de acordo com o usuário_
￿n￿ E￿￿￿￿ z￿￿￿￿￿￿￿ ￿ ￿￿￿￿￿￿ ￿￿ ￿￿￿￿
âimos durante este capítulo como usar o mecanismo de internacionalização do Áails
e con ￿guramos o idioma padrão como português brasileiro\ mas não vimos ne]
nhuma maneira de usar outro idioma_ â amos deixar o tolcho_net apenas em portu]
guês\ mas é importante saber qual é a melhor forma de fazer seu site suportar mais
de um idioma simultaneamente_
r maneira mais simples de suportar idiomas diferentes no seu site é especi ￿]
cando o idioma via áÁ“_ øor exemplo\ para o idioma inglês\ poderíamos criar a
áÁ“ www.colcho.net/en/users/new_
￿￿￿

## Página 132

￿_￿_ vxtrak alterar o idioma do site tasa do tódigo
r principal razão é o cachingk vm geral\ o caching é feito por áÁ“ e ter páginas
diferentes Xuma para cada idiomaY em uma mesma áÁ“ pode tornar o cache mais
difícil de ser construído_ ®uando o idioma faz parte da áÁ“\ não há necessidade de
alterações no mecanismo de caching_
øara que as rotas com idiomas funcionem\ usamos uma funcionalidade chamada
scope_ ”s scopes em rotas servem para agrupar um conjunto de controles em
um segmento de rota\ como por exemplo\ se criamos o recurso rooms no scope
admin\aa ção new mapeará para a áÁ“ /admin/rooms/new_ øorém\ esse recurso\
usado essa maneira\ não resolve nosso problema de uma maneira ￿exívelk teríamos
que criar uma entrada scope para cada idioma_
O ￿￿￿ ￿ ￿￿ ￿￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿
Éegmento de caminho Xpath segmentsY é uma parte da áÁ“ que é se]
parada por “‘” Xcomo se fossem “pastas”Y_ øor exemplo\ na imagem a
seguir\ o caminho XpathYé /users/new\ sendo users e new segmen]
tos distintosk
wigura￿_￿k rlgumas partes de uma áÁ“
É possível fazer com que o escopo torne]se um parâmetro\ e é exatamente isso
que precisamos fazer para que possamos detectar\ via áÁ“\ o idioma que o usuário
está requisitando_ øara isso\ usamos a sintaxe de símbolos para a rota_ triamos o
scope com o nome de :locale e\ en￿m\ podemos acessar o conteúdo deste trecho
da áÁ“ através da hash paramsk
lolwhonyt44jppliw_tion:routys:xr_w xo
swopy *4low_ly* xo
rysourwys 4rooms
￿￿￿

## Página 133

tasa do tódigo tapítulo ￿_ waça sua aplicação falar várias línguas
rysourwys 4usyrs
ynx
root 'homy@inxyx'
ynx
•ote que ao usar os helpers de rota do Áails\ esse parâmetro será automati]
camente incluído\ portanto não é necessário alterar nenhum outro códigok o idioma
inicialmente selecionado pela áÁ“_
r partir de agora\ em todas as requisi ções\ o que estiver na áÁ“ no segmento
:locale será passado como parâmetro_ â amos trabalhar de forma a tornar essa
variável disponível a todos os controles_
Ía l como o ActiveRecord\ os controles também possuem callbacks_ •esse
caso\ criaremos ￿ltros\ métodos que são executados antes de ações_ vsses ￿ltros\ em
geral\ possuem duas naturezask preparar dados para serem acessados nos controles
ou afetar a navegação\ por exemplo\ bloquear acessos de requisições não autentica]
das_
wiltros são criados através das class macros k before_action\ para mé]
todos executados antes da a ção\ after_action para depois\ ou em volta\
via around_action_ ” ￿ltro mais usado é o before_action\ e é ele que
vamos usar_ toncluindo\ vamos criar um ￿ltro no ApplicationController
X app/controllers/application_controller.rbY\ para con ￿gurar o
locale do sistema de internacionalizaçãok
wl_ss jppliw_tionlontrollyr > jwtionlontrollyr44k_sy
@ %ryvynt lq+n _tt_wks vy r_isin0 _n yxwyption:
@ nor j%osc you m_y w_nt to usy 4nullusyssion insty_x:
protywtuzromuzor0yry with4 4yxwyption
vyzoryu_wtion xo
o$fn:low_ly h p_r_ms/4low_ly3
ynx
ynx
￿￿￿

## Página 134

￿_￿_ vxtrak alterar o idioma do site tasa do tódigo
M￿￿￿￿￿￿￿ ￿￿￿￿ R￿￿￿￿￿z￿￿￿￿￿￿￿
” before_action é um novo novo para os ￿ltros de controle_ •as
versões anteriores\ os ￿ltros eram conhecidos como before_filter\
after_filter e around_filter_ vles ainda continuam funcio]
nando\ mas vamos usar a sintaxe mais moderna para o Áails ￿_
Ée acessarmos a áÁ“ /pt-BR/users/new\ será possível ver o cadastro tra]
duzido para o português_ Éubstituindo pt-BR por en\ veremos as páginas com
marcações\ pois não criamos todas as entradas para o inglês_ øorém\ após alterar
o arquivo de rotas e o controle\ não será mais possível acessar alguma das páginas\
vamos encontrar erros_ zsso porquê os helpers de áÁ“ do Áails agora precisam do
locale para gerar corretamente_
wigura￿_￿k Éite em inglêsk marcação vermelha onde não temos tradução
â amos continuar o desenvolvimento do site apenas no português_
õonstraints em rotas
ám problema das rotas até este momento é que\ se um usuário mudar o segmento
￿￿￿

## Página 135

tasa do tódigo tapítulo ￿_ waça sua aplicação falar várias línguas
de idioma para algo que não temos tradução\ como jp\ verá um site incompleto ou
não funcional_ øara evitar esse problema\ criaremos uma constraint\ ou restri ção\
rota\ de forma que a rota não seja válida no caso do idioma não ser suportado\ exi]
bindo ao usuário a mensagem de erro ￿￿￿_
øodemos usar expressões regulares para criar restrições_ ásaremos uma expres]
são regular que valida se o :locale é en ou pt-BRk
lolwhonyt44jppliw_tion:routys:xr_w xo
swopy *4low_ly*c low_ly4 ,yn|pttçk+, xo
rysourwys 4rooms
rysourwys 4usyrs
ynx
root *homy@inxyx*
ynx
øor ￿m\ ainda existe um problemak se o usuário tentar acessar a home\ ou rota
raiz do sitep ” Áails não conseguirá criar as rotas para os quartos na listagem\ e o mo]
tivo é simplesk as rotas para os controlesRoomsController e UsersController
só existem se o parâmetro :locale existir e\ no caso da home\ ela não existe_
Segmentos opcionais nas rotas
øara solucionar o problema\ vamos tornar a presen ça do :locale opcional\
tornando o idioma padrão do site como português_ Í omando como exemplo a rota
de novo cadastro\ teremos as seguintes possibilidadesk
• /users/new ] cadastro em portuguêsl
• /pt-BR/users/new ] cadastro em portuguêsl
• /en/users/new ] cadastro em inglêsl
• /jp/users/new ] erro “página não encontrada” Xjp\ es\ ou qualquer outro
idioma que não seja pt-BR ou enY
øara segmentos opcionais\ o Áails usa a mesma notação de campos opcionais em
expressões regularesk
lolwhonyt44jppliw_tion:routys:xr_w xo
swopy *{4low_ly}*c low_ly4 ,yn|pttçk+, xo
￿￿￿

## Página 136

￿_￿_ vxtrak alterar o idioma do site tasa do tódigo
rysourwys 4rooms
rysourwys 4usyrs
ynx
root *homy@inxyx*
ynx
rinda falta a rota na home que responde a diferentes idiomas_ ro acessar ahome\
ela será tratada como se não houvesse nenhum idioma\ indo para o padrão portu]
guês_ øara que a raiz também responda a outros idiomas\ temos que adicionar uma
nova rota usando o get_
r rota do tipo get é o tipo de rota mais simples_ â ocê pode desenhar qualquer
rota e ainda usar a notação ":segmento" para usar segmentos dentro do params_
rdicionamos também a restri ção de idiomas\ extraindo a expressão regular para uma
constantek
lolwhonyt44jppliw_tion:routys:xr_w xo
õ)ljõmq h ,yn|pttçk+,
swopy *{4low_ly}*c low_ly4 õ)ljõmq xo
rysourwys 4rooms
rysourwys 4usyrs
ynx
0yt ',4low_ly' h- 'homy@inxyx'c low_ly4 õ)ljõmq
root *homy@inxyx*
ynx
õ ￿￿￿￿￿￿ ￿￿￿ ￿￿￿￿￿ GET
Í ome cuidado com rotas get\ pois elas deixam suas rotas mais com]
plexas_ ám tipo de bug comum ocasionado por esse tipo de rotas é
quando elas entram em con￿ito\ ou seja\ mais de uma regra satisfaz uma
áÁ“_ •esse caso\ o Áails sempre escolherá a primeira rota encontrada\
de cima para baixo\ no arquivo de rotas_
ám problema que essa rota opcional gera é que todos os links da sua aplica ção
teriam que passar a opção locale: I18n.locale para todos os helpers de rota\ já
￿￿￿

## Página 137

tasa do tódigo tapítulo ￿_ waça sua aplicação falar várias línguas
que ela pode não existir_ ” Áails consegue centralizar essa opção se implementarmos
um método chamado default_url_options_
ørecisamos também atualizar o ￿ltro para que\ caso o :locale não
esteja de ￿nido\ vamos usar o idioma con ￿gurado como padrão no arquivo
config/application.rb_
øor ￿m\ o ApplicationController X
app/controllers/application_controller.rbY deverá ￿car da seguinte
formak
wl_ss jppliw_tionlontrollyr > jwtionlontrollyr44k_sy
@ %ryvynt lq+n _tt_wks vy r_isin0 _n yxwyption:
@ nor j%osc you m_y w_nt to usy 4nullusyssion insty_x:
protywtuzromuzor0yry with4 4yxwyption
vyzoryu_wtion xo
o$fn:low_ly h p_r_ms/4low_ly3 || o$fn:xyz_ultulow_ly
ynx
xyz xyz_ultuurluoptions
{ low_ly4 o$fn:low_ly }
ynx
ynx
vssas funcionalidades usam alguns recursos que requerem bastante conheci]
mento do framework\ portanto não se assuste se você achou complicado_ Áotas e
links podem se tornar complexas em aplica ções de grande porte\ portanto existem
diversas ferramentas para dar suporte a este tipo de requisito_
•ote também que existem outras maneiras de detectar o idioma\ como por
exemplo via diferentes domínios\ via headers yÍÍø ou até xeozø \ um banco de
dados que\ através do zø do usuário\ determina]se o país e por consequência\ seu
idioma_ vssas op ções não serão abordadas dada a sua complexidade_ Ée você qui]
ser mais informa ções\ veri￿que o guia o ￿cial do Áails no assuntok httpk‘‘guides_
rubyonrails_org‘i￿￿n_html_
￿￿￿

## Página 139

t ￿￿￿￿￿￿￿ ￿
”c a d a s t r od ou s u á r i oea
con￿rmação da identidade
“Suor mais sacrifício é igual a sucesso”
– tharles winley
￿n￿ E￿￿￿￿￿￿ ￿ í ￿￿￿￿￿M￿￿￿￿￿ ￿ ￿￿￿ ￿M￿￿￿õ ￿￿￿￿￿￿
” Áails possui uma ferramenta de envio de emails chamada ActionMailer_ vla
funciona como se fosse um controle\ ou seja\ possui diversos pontos de entrada Xem
análogo com as actionsY e resulta em um template que será enviado por email
para o usuário_
øara facilitar o desenvolvimento da entrega de emails\ usaremos uma ferramenta
chamada mailcatcher_” mailcatcher é uma gem Áuby que disponibiliza dois
serviçosk um servidor de envio de emails É–Íø \ que será usado pelo Áails\ e um
servidor à eb\ no qual observamos os emails que foram enviados\ como uma caixa

## Página 140

￿_￿_ vntenda o rction–ailer e use o –ailtatcher tasa do tódigo
de entrada_ •ela poderemos ver as versões yÍ–“\ texto e os dados brutos que foram
enviados pelo Áails_
øara instalá]la\ basta executark
ã 0ym inst_ll m_ilw_twhyr
:::
quwwysszully inst_llyx m_ilw_twhyrçd:8:$e
f 0yms inst_llyx
ro executar o comando mailcatcher\ temosk
ã m_ilw_twhyr
qt_rtin0 p_ill_twhyr
hh- smtp4,,$e!:d:d:$4$de8
hh- http4,,$e!:d:d:$4$dfd
[[[ p_ill_twhyr now runs _s _ x_ymon vy xyz_ult: 9o to thy wyv intyrz_wy
to quit:
tom o mailcatcher em execução\ vamos voltar ao Áails_ triaremos um maio
ler chamado Signup_ vssa classe irá agrupar todos os emails relacionados com o
cadastro Xsign upY e é essa a natureza dosmailersk cada classe é um contexto comum
a uma série de emails_ ám outro exemplo de mailer poderia ser Notifications\
no qual todos os emails de noti ￿cação\ como um um novo anúncio de quarto\ um
novo comentário ou uma nova avaliação_
G￿￿￿￿￿￿￿￿ ￿￿￿￿ ￿￿￿￿￿￿￿
” Áails possui geradores para –ailers\ mas eles são bem simples_ øor
esse motivo\ vamos criar manualmente_
” Signup irá herdar de ActionMailer::Base\ que possui um comporta]
mento muito parecido com o ActionController::Base_ yerdar dessa classe
irá adicionar diversos métodos facilitadores para criar emails_ øor exemplo\ podere]
mos colocar valores padrão\ como o campo “uek” \ ou “wromk” _
tada método criado no Signup funciona equivalentemente com as actions de
um controle\ ou seja\ no caso dos emails de con ￿rmação de conta\ criaremos um
método chamado confirm_email que será responsável pela montagem do email_
”utro paralelo com os controles é a forma de como comunicamos variáveis com o
￿￿￿

## Página 141

tasa do tódigo tapítulo ￿_ ” cadastro do usuário e a con ￿rmação da identidade
templatek através de variáveis de instância_ øor￿m\ os métodos deverão retornar um
objeto Mail_ øara isso\ chamamos o método mail\ passando a ele os campos de
email\ como assunto XsubjectY\ destinatário XtoY\ entre outros_
â amos então criar o email de con￿rmação_ •ele\ teremos o link de con￿rmação\
que vamos criar depois\ o destinatário XtoYeot í t u l oXsubjectY do email_ â amos tam]
bém usar um truque bem útilk colocar um email de nosso controle comobcc\ ou seja\
cópia oculta_
” resultado do Signup Xapp/mailers/signup.rbY é o seguintek
wl_ss qi0nupp_ilyr > jwtionp_ilyr44k_sy
xyz_ult zrom4 'noçryplyíwolwho:nyt'
xyz wonzirmuym_il{usyr}
íusyr h usyr
@ õink tymporário pois _ zunwion_lix_xy _inx_
@ não yxistyc v_mos wri_r _inx_ nysty w_pítulo
íwonzirm_tionulink h rootuurl
m_il{{
to4 usyr :ym_ilc
vww4 /'si0n ups >si0nupsíwolwho:nyt- '3c
suvjywt4 o$fn:t{'si0nup:wonzirmuym_il:suvjywt'}
}}
ynx
ynx
E￿￿￿￿￿ ￿￿￿óõõ
É uma boa ideia enviar emails para você mesmo usando o stt_ Áe]
cebendo esses emails\ você pode ver exatamente o que o usuário vê\ para
tentar ajudá]lo caso haja algum problema técnico ou na experiência de
usuário_
”utro uso do stt é para envio de emails em massa\ para evitar que
os emails de todos os usuários ￿quem à mostra_
￿n￿ T￿￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿l ￿￿ ￿￿￿￿￿￿￿ ￿￿￿￿￿￿
É boa prática enviar conteúdo yÍ–“ e texto puro em um mesmo email_ rssim\ ￿ca
a critério do seu usuário a maneira que ele prefere ler emails_ øortanto é necessário
￿￿￿

## Página 142

￿_￿_ Í emplates de email\ eu preciso delesp tasa do tódigo
criar dois templates para cada “ação” _ ro seguir a convenção do Áails\ ele já faz o tra]
balho de criar um email que contém as duas representações Xchamado demultipartY
e enviar para o destinatário_
trie a pasta signup na pasta app/views e lá vamos criar o template
confirm_email.html.erb\ a versão yÍ–“ do emailk
>h$-<%= t ':titly' %> >,h$-
>p-
<%= t ':voxy'c zullun_my4 íusyr:zullun_my %>
>,p-
>p-
<%= t ':wonzirmulinkuhtml'c
link4 linkuto{ íwonzirm_tionulinkc íwonzirm_tionulink} %>
>,p-
>p-
<%= t ':th_nksuhtml'c link4 linkuto{ 'lolwho:nyt'c rootuurl} %>
>,p-
rgora vamos fazer o template para o email em texto puro_ trie o arquivo
app/views/signup/confirm_email.text.erb com o seguinte conteúdok
<%= t ':titly' %>
<%= t ':voxy'c zullun_my4 íusyr:zullun_my %>
<%= t ':wonzirmulinkuhtml'c link4 íwonzirm_tionulink %>
<%= t ':th_nksuhtml'c link4 rootuurl %>
í ￿￿￿￿￿￿ ￿￿￿ ￿￿￿￿￿ ￿￿￿ ￿￿￿￿￿￿￿
øreste atenção nos links que estamos criando nos templates de maio
ler_ vstamos usando o su ￿xo _url e não o _path_ ®uando estamos na
à eb\ o browser infere o servidor e por isso só o path é su￿ciente\ mas
não no caso de emails_ vssa confusão porque sempre usamos _path nos
templates\ portanto é comum confundirmos_
øara os textos traduzidos\ adicione as seguintes linhas no é r–“ do idioma por]
tuguês Xconfig/locales/pt-BR.ymlY\ tomando o cuidado para colocar no nível
correto\ já que a identação é importantek
￿￿￿

## Página 143

tasa do tódigo tapítulo ￿_ ” cadastro do usuário e a con ￿rmação da identidade
ptçk+4
@ :::
si0nup4
wonzirmuym_il4
suvjywt4 'lolwho:nyt ç lonzirmy syu ym_il '
titly4 'qyj_ vym vinxo _o lolwho:nyt~ '
voxy4 |
qyj_ vym vinxo _o lolwho:nytc b{zullun_my}:
) lolwho:nyt é o lu0_r ixy_l p_r_ vowê _lu0_r _quyly qu_rto
sovr_nxo n_ su_ w_s_ y _inx_ wonhywyr 0ynty xo munxo intyiro:
wonzirmulinkuhtml4 '%_r_ vowê womyç_r _ us_r o sityc _wyssy o
link4 b{link} '
th_nksuhtml4 ')vri0_xo por sy w_x_str_r no b{link}: '
links4
@ :::
õ ￿￿￿￿￿ ￿￿￿ ￿￿￿￿￿￿ _￿￿￿￿
•a se ção ￿_￿￿ falamos de escaping de tags yÍ–“ e inje ção de código
malicioso_ ” sistema de z￿￿n também se preocupa com isso_ vntão\ para
evitar que todos os seus links virem texto\ é necessário colocar o su ￿xo
_html nas chaves de tradu ção\ para que o texto ￿nal seja um yÍ–“
válido_
rssumindo que temos um usuário cadastrado no banco de dados\ vamos tentar
enviar um email para elek
qi0nup:wonzirmuym_il{"syr:zirst}
@ jr0umyntmrror4 pissin0 host to link to~
@ %ly_sy provixy thy 4host p_r_mytyrc
@ syt xyz_ultuurluoptions/4host3c or syt 4onlyup_th to truy
￿￿￿

## Página 144

￿_￿_ Í emplates de email\ eu preciso delesp tasa do tódigo
í ￿￿￿￿￿￿ z￿￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿
vm mailers\ mesmo de ￿nindo métodos de instância\ devemos
chamá]los diretamente na classe\ já que o mailer é construído de acordo
com o método a ser chamado_
” problema está na hora de gerar links_ øode parecer simples\ mas para o Áails
saber em que endere ço ele está não é uma tarefa trivial_ •a verdade\ ele não tem
como saber\ dadas as maneiras que um servidor pode ser con ￿gurado_ øor isso\ o
que o Áails faz é con ￿ar nos cabe çalhos yÍÍø Xvários deles\ dependendo de onde
veio a requisiçãoY para montar a áÁ“ completa_
” problema é que\ frequentemente\ os mailers são executados fora do contexto
de requisição web\ ou seja\ em uma tarefa Áake\ ou em jobs em segundo plano\ e\
portanto\ impossível saber o host do servidor_ uessa forma\ o Áails requer que você\
manualmente\ de￿na o host para essas situações_ vssa con￿guração pode ser de￿nida
por cada ambiente Xdesenvolvimento\ teste e produçãoY_ â amos corrigir para o nosso
ambiente de desenvolvimento_
øara isso\ abra o arquivo config/environments/development.rb e adi]
cione a linha relacionada a default_url_options\ antes do end no ￿nalk
wonzi0:_ssyts:xyvu0 h truy
@ jpont_ o host p_r_ o _mviynty xy xysynvolvimynto
wonzi0:_wtionum_ilyr:xyz_ultuurluoptions h {
host4 *low_lhost4éddd*
}
ynx
rpós reiniciar o console\ conseguimos enviar o emailk
m_il h qi0nup:wonzirmuym_il{"syr:zirst}
@ +ynxyryx si0nupum_ilyr,wonzirmuym_il:html:yrv {$:8ms}
@ +ynxyryx si0nupum_ilyr,wonzirmuym_il:tyxt:yrv {$:!ms}
@ h- @>p_il44pyss_0y4!def8$fe8ef!êdc ::: -
irv{m_in}4ddé4d- m_il:xylivyr
@ lontyúxo xo ym_il:::
￿￿￿

## Página 145

tasa do tódigo tapítulo ￿_ ” cadastro do usuário e a con ￿rmação da identidade
”bjetos criados e email enviado para o limbo\ mas isso não signi￿ca muita coisa_
â amos con￿gurar o Áails para que ele possa enviar emails de verdade\ usando o
serviço de É–Íø do mailcatcher_
øara isso\ abra novamente o config/environments/development.rb e
coloque as seguintes linhas abaixo da linha que adicionamos anteriormentek
@ jpont_ o host p_r_ o _mviynty xy xysynvolvimynto
wonzi0:_wtionum_ilyr:xyz_ultuurluoptions h {
host4 *low_lhost4éddd*
}
wonzi0:_wtionum_ilyr:xylivyryumythox h 4smtp
wonzi0:_wtionum_ilyr:smtpusyttin0s h {
_xxryss4 *low_lhost*c
port4 $de8
}
ynx
Áeinicie o console do Áails e tente novamentek
qi0nup:wonzirmuym_il{"syr:zirst}:xylivyr
@ h- @>p_il44pyss_0y4!dé$=8fd8é88ddc pultip_rt4 truyc :::-
rponte o seu browser para o endere ço web do mailcatcher Xhttpk‘‘localhostk
￿￿￿￿Y e veja seus emails_ •ote que você pode ver também a versão puro texto_ rgora
que conseguimos enviar emails\ vamos plugar essa classe no momento do cadastro
do usuário_
ørecisamos alterar o controle UsersController e\ no momento que uma
conta é criada com sucesso\ disparamos o email_ â á ao controle e adicione a linha
logo após o ifk
wl_ss "syrslontrollyr > jppliw_tionlontrollyr
@ :::
xyz wry_ty
íusyr h "syr:nyw{p_r_ms/4usyr3}
iz íusyr:s_vy
qi0nup:wonzirmuym_il{íusyr}:xylivyr
ryxirywtuto íusyrc notiwy4 'l_x_stro wri_xo wom suwysso~ '
ylsy
￿￿￿

## Página 146

￿_￿_ –ais emails e a con ￿rmação da conta de usuário tasa do tódigo
rynxyr 4nyw
ynx
ynx
@ :::
ynx
“embre]se de reiniciar o servidor do Áails\ caso não o tenha feito após as al]
terações no arquivo config/environments/development.rb_ ro fazer um
cadastro\ o email será disparado e capturado pelo mailcatcher_
Í erminamos o envio de email de con ￿rmação_ “embre]se que colocamos um
link temporário no email e portanto\ vamos corrigi]lo\ colocando a implementação
correta_
￿n￿ M￿￿￿ ￿￿￿￿￿￿ ￿ ￿ ￿￿￿￿￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿ ￿￿ ￿￿￿￿ m
￿￿￿
–esmo ainda não tendo login veri ￿cado por email e senha\ vamos limitar o acesso
a contas não con￿rmadas_ â amos deixar tudo pronto para implementarmos o login
completo no próximo capítulo_
triaremos agora a última parte que resta para terminar a funcionalidade de ca]
dastro\ que é a con ￿rmação de email_ ” que devemos fazer ék enviar o email ao
usuário e\ quando ele clicar em um link único para a conta dele\ a conta estará con]
￿rmada_ waremos isso gerando um token único para cada usuário_ ®uando o usuário
for à pagina de con￿rmação com o token que foi incluído no email\ podemos assumir
que o usuário recebeu o email e está clicando no link_
øara implementar essa ideia\ vamos criar dois novos campos no modelo ásuáriok
con￿rmation_token e con￿rmed_at_ ” primeiro campo\ confirmation_token\
será gerado automaticamente no momento do cadastro do usuário_ vm seguida\
enviamos o email Xque acabamos de fazerY com um link\ contendo o token gerado_
” token tem que ser grande e aleatório\ de maneira que seja praticamente impossível
ser adivinhado e com grande probabilidade de ser único por usuário_ ” segundo
é o confirmed_at\ o campo que vamos marcar quando o usuário seguir o link
recebido no email\ tornando o cadastro do usuário totalmente válido_
øara isso\ vamos gerar uma nova migraçãok
ã r_ils 0ynyr_ty mi0r_tion _xxuwonzirm_tionuziylxsutouusyrs t
wonzirmyxu_t4x_tytimy wonzirm_tionutokyn
￿￿￿

## Página 147

tasa do tódigo tapítulo ￿_ ” cadastro do usuário e a con ￿rmação da identidade
invoky _wtivyuryworx
wry_ty xv,mi0r_ty,
ed$éd!$5d=$ee5u_xxuwonzirm_tionuziylxsutouusyrs:rv
r migra ção gerada serák
wl_ss jxxlonzirm_tionniylxs?o"syrs > jwtivy+yworx44pi0r_tion
xyz wh_n0y
_xxuwolumn 4usyrsc 4wonzirmyxu_tc 4x_tytimy
_xxuwolumn 4usyrsc 4wonzirm_tionutokync 4strin0
ynx
ynx
M￿￿￿￿￿ ￿￿￿￿￿￿￿ ￿￿ ￿￿￿ ￿￿￿￿￿￿￿￿
Ée você quiser adicionar muitas colunas a uma tabela\ pode usar o
change_table_ tom o change_table\ você informará o nome da
tabela apenas uma vez e usará a mesma sintaxe do create_table_ r
migração anterior ￿caria da seguinte formak
wh_n0yut_vly 4usyrs xo |t|
t:x_tytimy 4wonzirmyxu_t
t:strin0 4wonzirm_tionutokyn
ynx
vxecute as migra çõesk
ã r_ky xv4mi0r_ty
hh jxxlonzirm_tionniylxs?o"syrs4 mi0r_tin0 hhhhhhhhhhhh
çç _xxuwolumn {4usyrsc 4wonzirmyxu_tc 4x_tytimy }
ç- d:dd$ês
çç _xxuwolumn {4usyrsc 4wonzirm_tionutokync 4strin0 }
ç- d:dddês
hh jxxlonzirm_tionniylxs?o"syrs4 mi0r_tyx {d:ddeds} hhh
￿￿￿

## Página 148

￿_￿_ ám pouco de callbacks para realizar tarefas pontuais tasa do tódigo
￿n￿ U￿ ￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿￿ ￿￿￿￿ ￿￿￿￿￿￿￿￿ ￿￿￿￿￿￿￿
￿￿￿￿￿￿￿￿
rgora vamos gerar o token_ øara isso\ usaremos callbacks do ActiveRecord_ ”
ActiveRecord possui uma série de eventos durante o processo de salvar um objeto_
øor exemplo\ ao criar um objeto\ a ordem de chamada é a seguintek
￿Y before_validation ] rntes da valida ção
￿Y validate ] vxecuta as valida ções no modelo
￿Y after_validation ] rpós todas as valida ções
￿Y before_save ] rntes de salvar
￿Y before_create ] rntes de criar
￿Y create ] vxecuta a cria ção do modelo
￿Y after_create ] uepois de criar
￿Y after_save ] uepois de salvar
￿Y after_commit ]u e p o i sd e￿nalizar a transação no banco de dados
” mesmo acontece para atualiza ção de um modelo\ a diferen ça é que\ ao invés
de usar a palavra]chave create\ usamos update_ vm cada um desses eventos é
possível plugar código para que possamos executar alguma opera ção_ â amos usar o
evento before_create para preencher o token automaticamente_
õ ￿￿￿￿￿￿ ￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿￿
É muito conveniente usar callbacks\ mas é muito importante ter cau]
tela por inúmeras razões_ r primeira é que\ se você ￿zer muitas opera]
ções\ salvar um modelo torna]se algo demorado_ r segunda é que você
pode acabar gerando loops in￿nitos e situa ções complicadas de depu]
rar_ Í ome bastante cuidado e faça coisas muito simples nesses callbacks_
Ée precisar de lógicas complexas\ crie métodos e chame]os quando ade]
quado_
￿￿￿

## Página 149

tasa do tódigo tapítulo ￿_ ” cadastro do usuário e a con ￿rmação da identidade
•o modelo User Xapp/models/user.rbY\ vamos adicionar o código respon]
sável para gerar o tokenk
wl_ss "syr > jwtivy+yworx44k_sy
@ )mitinxo wontyúxo _ntyrior:::
h_susywuryup_ssworx
vyzoryuwry_ty xo |usyr|
usyr:wonzirm_tionutokyn h qywury+_nxom:urls_zyuv_sy=ê
ynx
ynx
” before_create aceita símbolo com o nome do método a ser chamado ou
um um bloco associado\ como ￿zemos nesse caso_ •o bloco\ usamos a biblioteca
SecureRandom\ que gera números aleatórios o su ￿ciente para nosso uso_ â amos
usar também uma forma que seja possível ser passado via áÁ“s e o SafeRandom
já possui um método para isso_ “embre]se de não chamar o método #save\p o i sa
gravação do objeto será realizada em um outro momento\ assim que todos os callo
backs estiverem concluídos_ ro chamar o método #save em callbacks\ você gerará
um loop in￿nito_
øara testar\ crie um novo usuário via o browser e depois vá ao console do Áailsk
"syr:l_st:wonzirm_tionutokyn
@ h- *ofio)lx"zo;jivrõsz"jf0*
N￿￿ ￿￿￿￿￿￿￿￿ ￿ ￿￿￿￿￿￿￿￿￿￿￿￿_￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿
vste é um campo que\ se permitirmos ser atualizado via formulário\
mesmo que de forma indireta\ podemos prejudicar a seguran ça da apli]
cação\ portanto não permita que o campo confirmation_token seja
passível de mass assignment_
triaremos o método #confirm!\ que marca a data e a hora da con ￿rmação e
limpa o token do usuário\ de forma que o link de con￿rmação só funcione uma única
vez_ â amos também criar o #confirmed?\ que veri￿cará se a conta do usuário foi
con￿rmadak
￿￿￿

## Página 150

￿_￿_ Áoteamento com restrições tasa do tódigo
wl_ss "syr > jwtivy+yworx44k_sy
@ :::
vyzoryuwry_ty xo |usyr|
usyr:wonzirm_tionutokyn h qywury+_nxom:urls_zyuv_sy=ê
ynx
xyz wonzirm~
ryturn iz wonzirmyxi
sylz:wonzirmyxu_t h ?imy:wurrynt
sylz:wonzirm_tionutokyn h ''
s_vy~
ynx
xyz wonzirmyxi
wonzirmyxu_t:prysynti
ynx
ynx
” método confirm! marca o campo confirmed_at com a hora corrente\
limpa o token e salva o modelo_ vxperimente no consolek
usyr h "syr:l_st
@ h- @>"syr ix4 $c zullun_my4 *riniwius k_00io nuyntys*c :::-
usyr:wonzirm~
@ h- truy
usyr:wonzirmyxi
@ h- truy
usyr:wonzirm_tionutokyn
@ h- **
tom este código\ estamos quase prontos_ ”s últimos passos sãok criar a rota\ o
controle e corrigir o link no mailer_
￿n￿ R￿￿￿￿￿￿￿￿￿ ￿￿￿ ￿￿￿￿￿￿￿￿￿￿
â amos adicionar uma nova rota no arquivo config/routes.rbk
￿￿￿

## Página 151

tasa do tódigo tapítulo ￿_ ” cadastro do usuário e a con￿rmação da identidade
lolwhonyt44jppliw_tion:routys:xr_w xo
rysourwys 4rooms
rysourwys 4usyrs
rysourwy 4wonzirm_tionc only4 /4show3
root *homy@inxyx*
ynx
•ote que há uma diferença nesse recursok não usamos resources\ mas sim
resource\ no singular_” motivo é que\para quem está navegando Xouo cliente de
uma røzY\não existe mais de uma con￿rmação Xouseja\ não faz sentido existir uma
ação indexYno sistema_zsso é chamado de recurso singleton_vm seguida\ passamos
uma opção\que é :only => [:show]_zsso signi￿ca que só queremos que a ação
show seja criada\ que é a ação que mais se aproxima do que queremos fazer_
øara entender o que essa rota gera\ podemos executar o comando rake
routes na raiz do projetok
ã r_ky routys
:::
wonzirm_tion 9m? ,wonzirm_tion{:4zorm_t} wonzirm_tions@show
âam o s criar o controle ConfirmationsController_ •ote que ainda te]
mos que usar o plural no nome e o motivo é que você ainda pode usar o
mesmo controle para rotas não]singleton_ •esse controle\ vamos buscar o usuá]
rio a partir do token e\ se ele de fato existir\ con￿rmaremos a conta e então re]
direcionamos o usuário para a sua página do per￿l_ vntão criemos o arquivo
app/controllers/confirmations_controller.rb\ com o seguinte con]
teúdok
wl_ss lonzirm_tionslontrollyr > jppliw_tionlontrollyr
xyz show
usyr h "syr:zinxuvy{wonzirm_tionutokyn4 p_r_ms/4tokyn3}
iz usyr:prysynti
usyr:wonzirm~
ryxirywtuto usyrc
notiwy4 o$fn:t{'wonzirm_tions:suwwyss'}
ylsy
￿￿￿

## Página 152

￿_￿_ Áoteamento com restrições tasa do tódigo
ryxirywtuto rootup_th
ynx
ynx
ynx
” find_by aceita um hash com os parâmetros para fazer a
busca\ e retornará o primeiro resultado encontrado_ rdicionare]
mos a chave confirmations.success no é r–“ de traduções X
config/locales/pt-BR.ymlYk
ptçk+4
wonzirm_tions4
suwwyss4 mm_il wonzirm_xo wom suwyssoc ovri0_xo~
@ :::
E ￿￿ ￿￿￿￿￿￿￿ ￿￿￿￿￿￿￿￿
Ée você leu a primeira edição do livro\ ou já programa em
Áails ￿\ notará que a mesma busca pode ser feita com o método
find_by_confirmation_token_ vssa sintaxe foi extraída do Áails
e se tornará obsoleta na próxima versão\ portanto use escopos ou o
find_by_
v ￿nalmente\vamos corrigir o link no mailer do cadastro\que tínhamos deixado
como root_path Xapp/mailers/signup.rbYk
wl_ss qi0nup > jwtionp_ilyr44k_sy
xyz_ult zrom4 'noçryplyíwolwho:nyt'
xyz wonzirmuym_il{usyr}
íusyr h usyr
íwonzirm_tionulink h wonzirm_tionuurl{{
tokyn4 íusyr:wonzirm_tionutokyn
}}
m_il{{
to4 usyr:ym_ilc
vww4 /'si0n ups >si0nupsíwolwho:nyt-'3c
￿￿￿

## Página 153

tasa do tódigo tapítulo ￿_ ” cadastro do usuário e a con￿rmação da identidade
suvjywt4 o$fn:t{'si0nup:wonzirmuym_il:suvjywt'}
}}
ynx
ynx
øronto\ terminamosQ ro fazer um cadastro\ recebemos um e]mail no
mailcatcherk
wigura￿_￿kvmail de con￿rmação no mailcatcher
ro seguir o link no email\ temos o seguinte resultadok
￿￿￿

## Página 154

￿_￿_ vm resumo tasa do tódigo
wigura￿_￿kvmail con￿rmado
øronto\o cadastro está funcionando por completoQ
￿n￿ E￿ ￿￿￿￿￿￿
øassamos os últimos capítulos exclusivamente desenvolvendo a funcionalidade de
cadastro_âe j ao que você aprendeu até agorak
• õomandos ] tomandos básicos do Áails e do rake\como geradores\visualizar
rotas\ executar servidor e consolel
• Migrações ] tomo gerar migrações que criam tabelas\ adicionam índices e
colunasl
• Modelos ] tomo criar modelos\ incluindo validações e callbacksl
• Segurança ] tomo evitar injeção de código malicioso via helpers\como evitar
ataques via mass assignment\como encriptar senha dos usuários e o que é íross
Site Request Forgeryl
• Emails ] vnvio de emails usando multipart\ enviando yÍ–“ e texto puro ao
mesmo tempol
￿￿￿

## Página 155

tasa do tódigo tapítulo ￿_ ” cadastro do usuário e a con￿rmação da identidade
• Rotas ] tomo construir rotas simplesl
• ísset Pipeline ] rprendeu como um dos componentes mais complexos do
Áails funciona e como trabalhar com elel
• õontrole ] tontrole de ￿uxo de navegação e mensagens ￿ashl
• I￿￿n ] znternacionalização das mensagens da aplicaçãol
• Te mp l ate se Helpers ] tria ção de templates\ layouts\ partials\ view helpers e
deixar seus templates elegantesl
r lista é enorme\parabénsQâam o sagora usar um pouco de tudo para construir
a funcionalidade de login_
￿￿￿

## Página 157

t ￿￿￿￿￿￿￿ ￿
“ogin do usuário
Foco é uma questão de decidir as coisas que você não irá fazerp
– {ohn tarmack\ cofundador da idÉo￿ware
ám usuário agora pode se cadastrar\con￿rmando sua conta através do link en]
viado no email de boas vindas_øorém\ ainda não temos nenhum controle de sessão\
ou seja\ qualquer visitante pode alterar qualquer informação no site_
tonstruiremos então o recurso “sessão” \que será criado toda vez que um usuário
realizar o login_ r sessão do usuário durará todo o tempo de navegação\ até que o
usuário faça o “logout” \ou seja\ destruir o recurso “sessão” _triaremos os templates
e o controle correspondente a esse ￿uxo de navegação e vamos usar a autenticação
provido pelo has_secure_password_
øor ￿m\ vamos modi￿car o cadastro de quartos para que quartos sejam associ]
ados ao criador e criar permissões\ de forma que apenas o criador do quarto possa
remover ou atualizar um quarto_

## Página 158

￿_￿_ Írabalhe com a sessão tasa do tódigo
￿n￿ T￿￿￿￿￿￿￿ ￿￿￿ ￿ ￿￿￿￿￿￿
øara que o usuário só preencha o login apenas uma vez\ precisamos guardar essa
informação de alguma forma_r maneira que usamos para guardar estado entre re]
quisições\ ou seja\ saber que alguma ação foi feita anteriormente\é usando cookies\
dados que são “anexados” a todas as requisições_ ” Áails usa cookies para gravar a
sessão_
ásaremos a sessão do Áails para gravar dados de modo a indicar que as requisi]
ções seguintes pertencem a um usuário especí￿co_ásamos a sessão como um hash\
ou seja\ um conjunto chave]valor_øor exemplo\ podemos indicar que o user_id
daquela sessão é o número hipotético ￿￿_rssim\ antes de realizar qualquer proces]
samento na aplicação\buscamos no banco de dados\ o usuário com id ￿￿_
walandode recursos\ a criação do recurso sessão será feita quando o usuário en]
via suas credenciais_®uando elas estiverem corretas\ escreveremos o zu do usuário
na sessão_øor sua vez\ quando destruirmos a sessão\ limparemos esse dado_
õ ￿￿￿ ￿￿￿￿￿￿￿￿ ￿ ￿￿￿￿￿￿￿￿￿ ￿￿￿ ￿￿￿￿￿￿￿￿
É importante lembrar que os cookies são gravados no browser do
usuário_ zsso signi￿ca que é possível que um usuário veja todo o con]
teúdo dos cookies\ ou seja\ poderá ver seu user_id_ ” que impedirá\
portanto\que algum usuário malicioso forje o cookie com o zu de outra
pessoap
” Áails assina digitalmente os cookies gravados no brow]
ser com uma chave que é secreta -- apenas o servidor sabe e
nunca é compartilhado com os clientes Xveja a chave no arquivo
config/initializers/secret_token.rbY_®uando um usuário
malicioso altera ou cria um cookie\ a sessão se tornará inválida\ pois não
será assinada com a chave\e o Áails irá rejeitar a sessão_
•ote que\mesmo que seja difícil criar sessões forjadas\ainda é possí]
vel ler o conteúdo\portanto lembre]se de nunca gravar dados importan]
tes na sessão\ de preferência apenas zus numéricos\ por exemplo_
tome çaremos criando a classe UserSession_vssa classe vai possuir as seguin]
tes responsabilidadesk
• Íradu ção de atributos Xviaz￿￿nYl
￿￿￿

## Página 159

tasa do tódigo tapítulo ￿_ “ogin do usuário
• â alidações em formuláriol
• âe r i￿car as credenciais do usuário Xemaile senhaYl
• xravar a sessão do usuário nos cookies_
øara tradução de atributos e validações de usuários\vamos usar um componente
do Áails chamado ActiveModel_ vle contém a lógica de callbacks\ validações e
traduções do ActiveRecord\ além de outras coisas_rlém disso\o ActiveModel
de￿ne a interface que modelos fazem com as outras camadas\ como por exemplo\
determinar rota e métodos auxiliares de construção de formulários_
–esmo não gravando os dados do UserSession em banco de dados\podemos
usar o ActiveModel para que essa classe interaja bem com as outras camadas do
Áails e usufruir dos mecanismos de validação\bastante conveniente para a constru]
ção de formulários_
” ActiveModel possui uma lista grande de componentes úteis\ alguns exem]
plos interessantes sãok
• ActiveModel::Callbacks ] íallbacks no ciclo de vida\ na forma que vi]
mos com o ActiveRecordl
• ActiveModel::Conversion ] ásado para detectar templates e rotasl
• ActiveModel::Dirty ] Éuportea atributos “sujos” \ou seja\detectar quando
um atributo foi alterado e guardar o valor antigol
• ActiveModel::Naming ] ásado para criar nomes legíveis para humanos\
além de rotasl
• ActiveModel::Translation ] ásado para traduzir atributos com o z￿￿nl
• ActiveModel::Validations ] â alidação de atributos Xunicidade\pre]
sença\ etc_Y_
rlguns componentes são mais focados na integração com o ActiveRecord
Xcomoo ActiveModel::AttributeMethodsY\útil para desenvolvedores que
estão fazendo bibliotecas e querem maior integração com o Áails Xcomopor exem]
plo\suporte ao –ongous Xhttpk‘‘mongodb_orgY\uma forma diferente de armazenar
dadosY_•a documentação de cada componente existe como você deve usá]lo e os
benefícios_
￿￿￿

## Página 160

￿_￿_ Írabalhe com a sessão tasa do tódigo
•ovo no Áails ￿\ usaremos o ActiveModel::Model\ que nos dá as seguintes
funcionalidadesk
• â alidaçõesl
• zntegração com formulários e rotasl
• Íradu ções
• znicialização de objetos com hashesl
vsse componente facilita muito a criação de modelos que interagem com o Áails
mas que não mapeiam diretamente para modelos ActiveRecord_
D￿￿￿￿￿ ￿￿￿ ￿￿ ACTIVE MODEL ::MODEL
rlgumas vezes é necessário criar um formulário complicado\ envol]
vendo mais de um modelo\por exemplo_Áequerbastante esforço realizar
essa tarefa sem resultar em um código de qualidade questionável_
r dica é criar um modelo usando ActiveModel::Model_ tom
esse modelo\ você pode criar atributos virtuais que mapeiam para cada
campo do formulário\ inclusive com validações_ áma vez o formulário
construído\ você pode criar código dentro da classe que irá resultar na
gravação de todos os outros modelos envolvidos\deixando o código dos
templates muito mais simples_
âam o scriar a classe UserSession_•ela\ vamos usar validações\ como se es]
tivéssemos lidando com um modelo ActiveRecord_ ueclararemos os atributos
email e password_trie então o arquivo app/models/user_session.rbk
wl_ss "syrqyssion
inwluxy jwtivypoxyl44poxyl
_ttru_wwyssor 4ym_ilc 4p_ssworx
v_lix_tysuprysynwyuoz 4ym_ilc 4p_ssworx
ynx
ásando o console do Áails\ vamos observar o comportamento da classe
UserSession\ com o que temos até agorak
￿￿￿

## Página 161

tasa do tódigo tapítulo ￿_ “ogin do usuário
syssion h "syrqyssion:nyw
@ h- @>"syrqyssion4dxdd!zyy$xév!e_f-
syssion:v_lixi
@ h- z_lsy
syssion:yrrors:zullumyss_0ys
@ h- /*mm_il não poxy ziw_r ym vr_nwo*c
@ *%_ssworx não poxy ziw_r ym vr_nwo*3
syssion h "syrqyssion:nyw{ym_il4 'viniv_00ioíyx_mply:wom'c
p_ssworx4 'sy0ryxo'}
@ h- @>"syrqyssion4dxdd!zzv_êxfw$yd
@ íym_ilh*viniv_00ioíyx_mply:wom*c
@ íp_ssworxh*sy0ryxo*-
syssion:v_lixi
@ h- truy
tom poucas linhas de código\ temos um comportamento bastante complexo\
graças a modularidade do Áails ￿_ rinda há muito o que se trabalhar nessa classe\
porém primeiro vamos criar os templates e o controle\ para que possamos testar a
parte de autenticação a partir da tela_
￿n￿ õ ￿￿￿￿￿￿￿￿ ￿ ￿￿￿￿￿ ￿￿￿￿ ￿ ￿￿￿￿ ￿￿￿￿￿￿￿
âam o sentão criar as rotas do recurso\que haverão apenas as ações create\ new e
destroy_øara isso\criaremos mais uma entrada no arquivo config/routes.rbk
lolwhonyt44jppliw_tion:routys:xr_w xo
rysourwys 4rooms
rysourwys 4usyrs
rysourwy 4wonzirm_tionc only4 /4show3
rysourwy 4usyrusyssionsc only4 /4wry_tyc 4nywc 4xystroy3
root *homy@inxyx*
ynx
vm seguida\ criamos o controle UserSessionsController X
app/controllers/user_sessions_controller.rbY e vamos mostrar
￿￿￿

## Página 162

￿_￿_ tontroles e rotas para o novo recurso tasa do tódigo
o formulário de login_ásamos a mesma técnica que usamos com modelos normaisk
criamos a variável no controle e a usamos no templatek
wl_ss "syrqyssionslontrollyr > jppliw_tionlontrollyr
xyz nyw
íusyrusyssion h "syrqyssion:nyw
ynx
xyz wry_ty
@ jinx_ não 4ç}
ynx
xyz xystroy
@ jinx_ não 4ç}
ynx
ynx
âam o scriar o template para a ação new\ bem similar aos formulários que ￿ze]
mos até então_r única diferença é que vamos mostrar erros que não estão em um
atributo em si\ mas no objeto como um todo_®uando um usuário digita um email
ou senha incorretamente\devemos mostrar que as credenciais estão inválidas_waze]
mos isso por medida de segurançaknão deixamos transparecer ao usuário se o email
é válido ou não_øara isso\adicionamos o erro no “atributo” :base_
ørecisamos criar a pasta app/views/user_sessions e o arquivo
%app/views/user_sessions/new.html.erbk
>h$-<%= t ':titly' %> >,h$-
<% iz íusyrusyssion:yrrors:h_sukyyi 4v_sy %>
>xiv ixh*yrroruyxpl_n_tion*-
<%= íusyrusyssion:yrrors/4v_sy3:join{'c '} %>
>,xiv-
<% ynx %>
<%= zormuzor íusyrusyssion xo |z| %>
>p-
<%= z:l_vyl 4ym_il %>
<%= z:tyxtuziylx 4ym_il %>
<%= yrrorut_0 íusyrusyssionc 4ym_il %>
>,p-
>p-
￿￿￿

## Página 163

tasa do tódigo tapítulo ￿_ “ogin do usuário
<%= z:l_vyl 4p_ssworx %>
<%= z:p_ssworxuziylx 4p_ssworx %>
<%= yrrorut_0 íusyrusyssionc 4p_ssworx %>
>,p-
>p-
<%= z:suvmit %>
>,p-
<% ynx %>
>p-<%= linkuto t{':si0nuup'}c nywuusyrup_th %> >,p-
ro direcionar o browser na página de nova sessão de usuário Xhttpk‘‘localhostk
￿￿￿￿‘userúsessions‘new Y\temos o seguintek
wigura￿_￿køágina de login
rs bordas vermelhas estão gritando\ então vamos criar as traduções que estão
faltando no arquivo z￿￿n Xconfig/locales/pt-BR.ymlY_
@ :::
show4
yxit4 'mxit_r pyrzil'
titly4 *%yrzil4 b{usyrun_my}*
low_tion4 *õow_liz_ção4 b{low_tion}*
vio4 *kio4 b{vio}*
@ (ov_ p_rty4
usyrusyssions4
nyw4
titly4 'õo0in'
￿￿￿

## Página 164

￿_￿_ tontroles e rotas para o novo recurso tasa do tódigo
si0nuup4 'l_x_stryçsy'
si0nup4
wonzirmuym_il4
@:::
•o ￿m do arquivo\ vamos criar mais duas “seções” \contendo as traduções do
ActiveModel e a tradução especí￿ca do botão de logink
room4
xyswription4 <yswrição
low_tion4 õow_liz_ção
titly4 ?ítulo
@ jxiwiony4
_wtivymoxyl4
_ttrivutys4
usyrusyssion4
ym_il4 mm_il
p_ssworx4 qynh_
yrrors4
myss_0ys4
inv_lixulo0in4 '"suário ou synh_ inválixos'
hylpyrs4
suvmit4
usyrusyssion4
wry_ty4 'mntr_r'
•ote a porção ￿nal do z￿￿n\ um trecho especial para os formulários_âo c êpode
criar uma tradução especí￿ca para cada modelo como ￿zemos\ usando as chaves
adequadas_” padrão que abrange todos os modelos é o seguinte\extraído da tradu]
ção padrão do Áails que baixamos Xconfig/locales/rails.pt-BR.ymlYk
@ (ão woloquy no syu ptçk+:ymlc
@ vowê já tym isso no r_ils:ptçk+:yml
ptçk+4
@ :::
hylpyrs4
suvmit4
wry_ty4 lri_r b{moxyl}
￿￿￿

## Página 165

tasa do tódigo tapítulo ￿_ “ogin do usuário
suvmit4 q_lv_r b{moxyl}
upx_ty4 jtu_liz_r b{moxyl}
É interessante dar uma olhada no z￿￿n padrão do Áails caso você tenha interesse
em customizar uma mensagem\de modo a evitar mensagens genéricas e sem perso]
nalidade_ásando o nome do modelo como escopo de chaves\você pode personalizar
a mensagem sem ter que alterar o template_
rgora vamos para a parte mais legal do capítulo\a criação da sessão do usuário_
￿n￿ S￿￿￿￿￿￿￿ ￿￿￿￿￿￿￿
âam o snos lembrar de uma lição muito importantek não é interessante colocar a
lógica de negócio nos controles_” que seria lógica de negóciop •esse caso\ é tudo
que não é roteamento\mensagem de erro ou decidir a melhor representação para o
recurso_
” que vamos fazer no controle é apenas tentar criar a sessão via o modelo
UserSession_Ée algum erro acontecer\simplesmente vamos mostrar ao usuário o
template com os erros\ e se ocorrer sucesso\direcionaremos o usuário para a página
principal com a mensagem apropriada_
øorém\ essa ação não será exatamente igual às ações que relacionam]se com o
ActiveRecord_”s controles possuem os cookies\e portanto teremos que passar ao
modelo em qual objeto iremos gravar a sessão do usuário Xmasnão como e quando\
isso é muito importanteQY_
•os controles do Áails\temos duas maneiras de acessar os cookies dos usuários\
via o método session e via o método cookies_rmbos os métodos se comportam
muito parecido com os já famosos params e flash ] na forma de hashes_
”s cookies são simples formas de guardar estado entre requisições yÍÍø _ vles
são passados pelo usuário o usuário ao servidor em cada requisição_ øor exemplo\
se tivermos um controle cuja ação execute o código a seguir\ o Áails irá criar uma
resposta com o cookie informado que\por padrão\irá durar apenas a sessão de nave]
gação do usuário\ou seja\ ao fechar o browser\o cookie será removido pelo browser_
xyz wry_ty
wookiys/4pyr0unt_3 h 'kiswoito ou vol_wh_i'
ynx
” cabeçalho da resposta yÍÍø será algo parecido com o seguinte_ •ote\ na
penúltima linha\ o comando para guardar o cookie com o que con￿guramosk
￿￿￿

## Página 166

￿_￿_ Éessões e cookies tasa do tódigo
#??%,$:$ edd )1
lontyntç?ypy4 tyxt,htmlg wh_rsythutzçf
;ç"_çlomp_tivly4 omhmx0y
mt_04 *5$w58d8d!ê=$5dzze!yvéê_ddê5!x5$v*
l_whyçlontrol4 m_xç_0yhdc priv_tyc mustçryv_lix_ty
;ç+yquystçox4 =$5êywwwd_exddzêzê!exd_!5zef=xxê
;ç+untimy4 d:dedfê5
lontyntçõyn0th4 e$88
qyrvyr4 smkriwk,$:é:$ {+uvy,$:5:é,ed$eçdêçed}
<_ty4 ?uyc $d óul ed$e d848!485 9p?
lonnywtion4 1yypçjlivy
qytçlookiy4 pyr0unt_hkiswoito]ou]vol_wh_béng p_thh, qytçlookç
iy4 uwolwhonytusyssionhkjh!:::::::::::::ff8!g p_thh,g #ttp)nly
øor ￿m\ podemos ver no console do browser Xxoogle throme\ nesse casoYo
resultado do cookie guardadok
wigura￿_￿ktookie com a chave ‘pergunta’
•ote também que temos outra chave de cookie\a _colchonet_session_v s s a
é gerenciada automaticamente pelo Áails para controlar o tÉÁw Xtross]Éite Áequest
worgery\visto na seção ￿_￿Y_
” nosso objetivo é armazenar o ID do usuário autenticado no cookie_ø o r t a n t o \
se o email e a senha estiverem corretos e a conta estiver con￿rmada\ salvamos o ID
do usuário no cookie e resgatamos o objeto User em cada requisição_
øorém\ não é inteligente da nossa parte simplesmente gravar o ID do usuá]
rio no cookie e sentar no sofá esperando a bonança_ zsso porquê\ ao fazer
cookies[:user_id] = 1\ um usuário mal intencionado pode muito bem pegar
o cookie local e colocar um outro zu e começar a agir como um outro usuário_vsse
ataque é conhecido como Session Hijackingq￿e￿ ou sequestro ou roubo de sessão_
￿￿￿

## Página 167

tasa do tódigo tapítulo ￿_ “ogin do usuário
” Áails já sabe disso e sabe a melhor maneira de prever ataques como esse_ v
é justamente essa a grande diferença entre o cookie e o sessionl o session
assinada usando uma chave secreta\de forma que o usuário poderá ler o conteúdo da
sessão\ porém\ ao modi￿cá]la\ a assinatura torna]se inválida_øortanto\di￿cilmente
conseguirá forjar uma sessãok
kjh!kdki<é(lwé(pve8z_s.9)06n+kkió?kkpenm(?lk(<wyt
(erh(<ók6?+h7zmê7j.d7jw8)9ókkjsjrmkimn5jwéóm;é+v_erukjsj+kkit
prh$(npv"són)95p.d(svj+kvnxuwnh?6;mz_"ld(<jrrkn.r#r?6i5l6lm5t
kjsj+0bé<bé<çç$dd_yfêv_xêyeeeyvx$!_édzêêx_w!êeê8ê5y5êz
” conteúdo antes do “--” é a sessão do usuário\ codi￿cada em sase ￿￿_ r se]
gunda parte é a assinatura\ calculada usando um token secreto\ que ￿ca no arquivo
config/initializers/secret_token.rb_
@ qtrin0 loooooooon0_::::
lolwhonyt44jppliw_tion:wonzi0:sywrytukyyuv_sy h '55ef5_z :::'
É muito importante que você nunca divulgue de forma alguma o
secret_key_base de sua aplicação_ ueixar em controle de versão não tem
problema Xdesdeque não seja open sourceQY\mas não deixe isso disponível para
seus usuários\ pois eles podem ter suas contas roubadasQ
Ée por algum motivo você suspeitar que o secret_key_base deixou de ser se]
gredo ou que você tem usuários com sessões roubadas\você pode substituir o código
atual gerando um novo viak
ã r_ky sywryt
8$évêéze=wy::::
zsso invalidará todas as sessões e os usuários terão que fazer um novo login\ mas
é melhor garantir a segurança das informações_
￿￿￿

## Página 168

￿_￿_ Éessões e cookies tasa do tódigo
í ￿￿￿￿￿￿￿￿￿￿ ￿￿￿￿￿￿￿￿￿￿￿ ￿ R￿￿￿￿￿
•o Áails ￿\ as sessões não são encriptadas\apenas assinadas_zsso sig]
ni￿ca que\ mesmo sem a palavra secreta\ os usuários podem ver o con]
teúdo da sessão\ só não modi￿cá]la_
•o Áails ￿\ o conteúdo da sessão é encriptada por padrão\ que é in]
compatível com as sessões da versão anterior_tontudo\ existe uma forma
forma de migrar as sessões dos seus usuários das sessões assinadas para
a sessão encriptada de forma transparente para os usuários_
øara fazer a migração\ basta que\ no arquivo
config/initializers/secret_token.rb\ você con￿gure
ambas as opções secret_key_base\ usada para encriptação XnovoY\
e a secret_token\ usada para assinatura dos cookies XantigoY_tom
ambas as chaves presentes\ o Áails poderá fazer a migração dos cookies
assinados para os cookies encriptados automaticamente_
øor exemplo\ se o tolchonet\ antes usando Áails ￿\ possuía o
secret_token.rb da seguinte formak
lolwho(yt44jppliw_tion:wonzi0:sywrytutokyn h *$eé $eé $eé*
•o Áails ￿\ basta especi￿car também o secret_key_base\ resul]
tando emk
lolwho(yt44jppliw_tion:wonzi0:sywrytutokyn h *$eé $eé $eé*
lolwho(yt44jppliw_tion:wonzi0:sywrytukyyuv_sy
h *m(l+o%?j<) m(l+o%?j<)*
zsso fará com que as sessões dos usuários atuais continuem funcio]
nando e\ após o primeiro acesso\ o Áails automaticamente irá converter
a forma encriptada_ Ée necessário\ use o rake secret para gerar o
novo valor da chave privada de maneira segura_
￿￿￿

## Página 169

tasa do tódigo tapítulo ￿_ “ogin do usuário
S￿￿￿￿￿￿￿ ￿￿￿￿￿￿￿￿￿￿￿￿
É importante lembrar que cookies\apesar de não houver limite em sua
especi￿cação XÁwt￿￿￿￿Y\cookies possuem uma limitação prática de ￿ks\
portanto tome cuidado com o que você vai gravar_
”utro problema que pode pegar você de surpresa é a serialização_
Sempre guarde IDs para que objetos sempre estejam em sua versão mais
atual quando usados_yá objetos também que não podem ser serializa]
dos\ como por exemplo\ ponteiros a arquivos e objetos de z”\ e podem
causar exceções na hora de gerar o cookie_
uepois de todos esses conceitos sobre cookies e sessões\ vamos à implementação
das sessões de usuário_ øara relembrar\ devemos usar a session para gravar o
zu do usuário caso ele seja autenticado com sucesso_øara isso\ vamos criar a ação
create que irá criar uma nova instância da classe UserSession_ thamaremos
então o método authenticate!\ que ainda vamos criar_ vle fará o trabalho de
gravar na sessão\ caso as credenciais estejam corretas_â amos\por ￿m\ redirecionar
o usuário para as páginas correspondentes_
” resultado da ação create do controle UserSessionsController X
app/controllers/user_sessions_controller.rbYserák
wl_ss "syrqyssionslontrollyr > jppliw_tionlontrollyr
xyz nyw
íusyrusyssion h "syrqyssion:nyw{syssion}
ynx
xyz wry_ty
íusyrusyssion h "syrqyssion:nyw{syssionc p_r_ms/4usyrusyssion3}
iz íusyrusyssion:_uthyntiw_ty~
@ (ão ysquyç_ xy _xiwion_r _ wh_vy no i$fn~
ryxirywtuto rootup_thc notiwy4 t{'zl_sh:notiwy:si0nyxuin'}
ylsy
rynxyr 4nyw
ynx
ynx
xyz xystroy
￿￿￿

## Página 170

￿_￿_ Éessões e cookies tasa do tódigo
ynx
ynx
ørimeiro\ precisamos criar o método construtor para aceitar os parâmetros do
formulário e a sessão que vem do controlek
xyz initi_lizy{syssionc _ttrivutysh{}}
ísyssion h syssion
íym_il h _ttrivutys/4ym_il3
íp_ssworx h _ttrivutys/4p_ssworx3
ynx
” método authenticate! é o método que veri￿ca os dados entrados pelo
usuário_zsso será feito através do método User#authenticate\ que ainda vamos
criar_Ée tudo estiver correto\ ou seja\ se existir um usuário cujo email e senhas são
válidos\ guarda a sessão\caso contrário\marca]se um erro a ser exibido no formulá]
rio_
xyz _uthyntiw_ty~
usyr h "syr:_uthyntiw_ty{íym_ilc íp_ssworx}
iz usyr:prysynti
story{usyr}
ylsy
yrrors:_xx{4v_syc 4inv_lixulo0in}
z_lsy
ynx
ynx
âe j aque nesse caso estamos delegando a lógica de veri￿car se o usuário tem o
email e senha válido no modelo User_”u seja\ é o modelo usuário que deve saber
como a autenticação deve ser feita_É importante centralizar esse tipo de lógica para
que\ se um dia mudarmos a forma de como o login é feito\basta alterar apenas um
lugar_
ásando a røz de erros do ActiveModel é fácil criar um erro customizado_
•essa situação\ o erro não é no atributo email e nem no atributo password_øor
essa razão\adicionamos o erro no base\que é o objeto como um todo_tomo vimos
no template\esse erro será exibido no topo do formulário_
øor ￿m\ temos o método store\ que grava o zu do usuário na sessãok
￿￿￿

## Página 171

tasa do tódigo tapítulo ￿_ “ogin do usuário
xyz story{usyr}
ísyssion/4usyruix3 h usyr:ix
ynx
øor ￿m\ o resultado do modelo UserSession X
app/models/user_session.rbYék
wl_ss "syrqyssion
inwluxy jwtivypoxyl44poxyl
_ttru_wwyssor 4ym_ilc 4p_ssworx
v_lix_tysuprysynwyuoz 4ym_ilc 4p_ssworx
xyz initi_lizy{syssionc _ttrivutysh{}}
ísyssion h syssion
íym_il h _ttrivutys/4ym_il3
íp_ssworx h _ttrivutys/4p_ssworx3
ynx
xyz _uthyntiw_ty~
usyr h "syr:_uthyntiw_ty{íym_ilc íp_ssworx}
iz usyr:prysynti
story{usyr}
ylsy
yrrors:_xx{4v_syc 4inv_lixulo0in}
z_lsy
ynx
ynx
xyz story{usyr}
ísyssion/4usyruix3 h usyr:ix
ynx
ynx
âam o sagora ao modelo usuário_
￿n￿ õ ￿￿￿￿￿￿￿￿￿￿ ￿￿￿￿￿ ￿￿ ￿￿￿￿￿
rntes de continuar\ vamos entender como consultamos o banco de dados através
do ActiveRecord\ buscando no banco de dados sem escrever comandos É®“_ É
￿￿￿

## Página 172

￿_￿_ tonsultas no banco de dados tasa do tódigo
importante entender que o ActiveRecord faz o possível\ mas não é infalível_øor
isso\ é bastante importante entender a chamada gerada e\ eventualmente\ escrever
chamadas É®“ manualmente_
øara fazer buscas\ o ActiveRecord possui uma lista métodos que lembram
cláusulas É®“_ øor exemplo\o método limit irá limitar o número de objetos retor]
nados\sem nenhuma ordem especí￿ca_øara fazer buscas ￿ltradas\usamos o método
.where\ e assim por diante_âe j aa lista de métodos a seguirk
• where ] –apeia cláusulas WHEREl
• select ] vspeci ￿ca o que será retornado no SELECT\ ao invés de *l
• group ] –apeia cláusulas GROUP BYl
• order ] –apeia cláusulas ORDER BYl
• reorder ] Éobrescreve cláusulas de ordem de default_scope Xveremoso
que é default_scope ainda nesse capítuloYl
• reverse_order ] znverte a ordem especi￿cada Xcrescenteou decrescenteYl
• limit ] –apeia cláusula LIMITl
• offset ] –apeia cláusula OFFSETl
• joins ] ásado para inner joins ou quaisquer outer joinsl
• includes ] wazjoins automaticamente com modelos relacionados\ veremos
relacionamentos no capítulo ￿￿l
• lock ] Írava atualizações de objetos para atualizaçãol
• readonly ] Íor n aos objetos retornados marcados como apenas leitural
• from ] –apeia cláusula FROMl
• having ] –apeia cláusula HAVING￿ l
âe j aos exemplos abaixok
￿￿￿

## Página 173

tasa do tódigo tapítulo ￿_ “ogin do usuário
"syr:limit $
@ "syr õo_x {d:$ms} qmõml? *usyrs*:[ n+)p *usyrs* õopo? $
@ h- @>jwtivy+yworx44+yl_tion
@ /@>"syr ix4 $$c zullun_my4 *riniwius k_00io nuyntys*c ::: -3-
"syr:whyry ym_il4 'viniv_00ioíyx_mply:wom'
@ "syr õo_x {d:$ms} qmõml? *usyrs*:[ n+)p *usyrs*
@ s#m+m *usyrs*:*ym_il* h 'viniv_00ioíyx_mply:wom'
@ h- @>jwtivy+yworx44+yl_tion
@ /@>"syr ix4 $$c zullun_my4 *riniwius k_00io nuyntys*c ::: -3-
Escopos
D￿￿￿zõ ￿￿￿￿￿￿￿ SQL ￿￿ ￿￿￿￿￿￿￿
øara facilitar o seu aprendizado e também tirar dúvidas\ é possível
fazer com que o ActiveRecord imprima o comando É®“ gerado no
zÁs_øara fazer isso\ crie o arquivo .irbrc na sua pasta home com o
seguinte conteúdok
iz m(r:inwluxyi{'+joõqum(r'}
ryquiry 'lo00yr'
+_ils:lo00yr h õo00yr:nyw{q?<)"?}
ynx
“embre]se de reiniciar o console do Áails\ reload! não é su￿ciente_
rs buscas ￿cam interessantes quando combinadas ®uando chamamos um mé]
todo de consulta X.limit e .where\ por exemploY\o método retorna um objeto
especial chamado ActiveRecord::Relation_ vsse objeto pode\ por sua vez\
receber novamente métodos de consulta\ acumulando comandos que já foram cha]
mados anteriormente_âe j ao exemplo a seguirk
"syr:whyry{ym_il4 'viniv_00ioíyx_mply:wom'}:limit{e}
@ "syr õo_x {d:éms} qmõml? *usyrs*:[ n+)p *usyrs*
@ s#m+m *usyrs*:*ym_il* h 'viniv_00ioíyx_mply:wom'
￿￿￿

## Página 174

￿_￿_ tonsultas no banco de dados tasa do tódigo
@ õopo? e
@ h- >jwtivy+yworx44+yl_tion /:::3-
mosturywynt h "syr:orxyr{'wry_tyxu_t <mql'}
mosturywynt:limit{$}
@ qmõml? *usyrs*:[ n+)p *usyrs* )+<m+ k7 wry_tyxu_t <mql õopo? $
@ (oty quy _ wh_m_x_ _o :limit _ntyrior não _ltyr_
@ o ovjyto mosturywynt
mosturywynt:whyry{ym_il4 'viniv_00ioíyx_mply:wom'}
@ qmõml? *usyrs*:[ n+)p *usyrs*
@ s#m+m *usyrs*:*ym_il* h 'viniv_00ioíyx_mply:wom'
@ )+<m+ k7 wry_tyxu_t <mql
vssa composição de métodos é o que chamamos de escopo de busca_øor exem]
plo\ a variável most_recent que criamos é um escopo em User que sempre irá
retornar os usuários em ordem decrescente pela data de criação Xcreated_atY_
É bom entender como o query planner Xcomponenteque planeja como será a
melhor forma de executar a consulta É®“Y do banco de dados vai executar uma con]
sulta_ vm banco de dados tradicionais como –yÉ®“ e øostgreÉ®“\ é possível ob]
servar informações importantes como uso ou não de índices\ tabelas temporárias\
entre outras coisas\de modo que possamos alterar a consulta para obter melhor per]
formance_øara esses bancos de dados\ basta executar EXPLAIN na consulta_tom
o ActiveRecord\ conseguimos fazer isso ￿ chamando o método .explaink
"syr:whyry{ym_il4 'viniv_00ioíyx_mply:wom'}:
orxyr{'wry_tyxu_t <mql'}:
yxpl_in
@ qmõml? *usyrs*:[ n+)p *usyrs*
@ s#m+m *usyrs*:*ym_il* h 'viniv_00ioíyx_mply:wom'
@ )+<m+ k7 wry_tyxu_t <mql
@ m;%õjo( ."m+7 %õj( qmõml? *usyrs*:[ n+)p *usyrs*
@ s#m+m *usyrs*:*ym_il* h 'viniv_00ioíyx_mply:wom'
@ )+<m+ k7 wry_tyxu_t <mql
@ h- *m;%õjo( zor4 qmõml? t*usyrst*:[ n+)p t*usyrst*
@ s#m+m t*usyrst*:t*ym_ilt* h 'viniv_00ioíyx_mply:wom'
@ )+<m+ k7 wry_tyxu_t <mql
￿￿￿

## Página 175

tasa do tódigo tapítulo ￿_ “ogin do usuário
@ d|d|d|qmj+l# ?jkõm usyrs
@ "qo(9 o(<m; inxyxuusyrsuonuym_il {ym_ilhi} {~$d rows}
@ d|d|d|"qm ?mp% kç?+mm n)+ )+<m+ k7*
” ActiveRecord também permite criar os named scopes\ ou escopos nome]
ados\ de modo que você chame .most_recent\ ao invés de .order('created
DESC')\ tornando as chamadas de métodos bastante legíveis_zmagine que a classe
User tenha o seguinte códigok
wl_ss "syr > jwtivy+yworx44k_sy
swopy 4mosturywyntc ç- { orxyr{'wry_tyxu_t <mql'} }
swopy 4zromus_mp_c ç- { whyry{low_tion4 'qão %_ulo'} }
@ :::
ynx
E￿￿￿￿￿￿￿
Ée você tentar executar esse exemplo e esbarrar com o seguinte pro]
blemak
qynt_xmrror4 usyr:rv4é4 inv_lix multivyty wh_r {"qçjqloo}
usyr:rv4é4 inv_lix multivyty wh_r {"qçjqloo}
usyr:rv4é4 synt_x yrrorc unyxpywtyx ãynxc yxpywtin0 '}'
swopy 4zromus_mp_c ç- { whyry{4low_tion h- 'qão %_ulo'} }
zsso deve]se ao fato de que o Áuby não reconheceu esse caractere no
código]fonte_øara que o caractere seja reconhecido\ coloque o seguinte
conteúdo na primeira linha do arquivok
@ ynwoxin04 utzçf
￿￿￿

## Página 176

￿_￿_ tonsultas no banco de dados tasa do tódigo
í ￿￿￿￿￿￿￿￿￿￿z￿￿￿￿￿￿￿ ￿￿￿￿￿￿￿￿
•a versão ￿ do Áails\era possível criar escopos nomeados da seguinte
forma\ sem blocos lambdak
swopy 4zromus_mp_c whyry{low_tion4 'qão %_ulo'}
” suporte a essa forma foi abandonado_âo c êdeverá atualizar para a
forma com lambdas ou usar métodos de classe diretamente_
uessa forma\podemos chamar os named scopes da mesma maneira que chama]
mos os outros métodos de buscak
"syr:mosturywynt:limit{8}
@ qmõml? *usyrs*:[ n+)p *usyrs*
@ )+<m+ k7 wry_tyxu_t <mql
@ õopo? 8
"syr:mosturywynt:zromus_mp_
@ qmõml? *usyrs*:[ n+)p *usyrs*
@ s#m+m *usyrs*:*low_tion* h 'qão %_ulo'
@ )+<m+ k7 wry_tyxu_t <mql
rinda é possível criar named_scopes com parâmetrosk
wl_ss "syr > jwtivy+yworx44k_sy
swopy 4mosturywyntc ç- { orxyr{'wry_tyxu_t <mql'} }
swopy 4zromus_mp_c ç- { whyry{low_tion4 'qão %_ulo'} }
swopy 4zromc ç-{low_tion} { whyry{low_tion4 low_tion} }
@ :::
ynx
"syr:zrom{'q_n nr_nwiswoc lj'}:mosturywynt
@ qmõml? *usyrs*:[ n+)p *usyrs*
@ s#m+m *usyrs*:*low_tion* h 'q_n nr_nwiswoc lj'
@ )+<m+ k7 wry_tyxu_t <mql
@ qy wonxiçõys sy rypytirymc _pyn_s _ últim_ syrá m_ntix_4
￿￿￿

## Página 177

tasa do tódigo tapítulo ￿_ “ogin do usuário
"syr:zrom{'q_n nr_nwiswoc lj'}:zromus_mp_
@ qmõml? *usyrs*:[ n+)p *usyrs*
@ s#m+m *usyrs*:*low_tion* h 'qão %_ulo'
øor ￿m\ ainda é possível criar um escopo padrão\ ou seja\ um escopo que será
sempre aplicado\ via o default_scope_ vsse escopo não é sobrescrito e se você
de￿nir outros default_scope\ eles são acumulados_
wl_ss "syr > jwtivy+yworx44k_sy
xyz_ultuswopy ç- { whyry{'wonzirmyxu_t oq ()? ("õõ'} }
@ :::
ynx
"syr:_ll
@ qmõml? *usyrs*:[ n+)p *usyrs* s#m+m {wonzirmyxu_t oq ()? ("õõ}
"syr:whyry{low_tion4 'q_n nr_nwiswoc lj'}
@ qmõml? *usyrs*:[ n+)p *usyrs*
@ s#m+m *usyrs*:*low_tion* h 'q_n nr_nwiswoc lj'
@ j(< {wonzirmyxu_t oq ()? ("õõ}
õ ￿￿￿￿￿￿￿ ￿￿￿ ￿ DEFAULT _SCOPE
” default_scope tem utilidades interessantes\como implementar
so￿ delete\ ou seja\ destruir objetos nada mais é do que marcá]lo como
destruído e não ser incluso nas buscas_øortanto\um default_scope
cuja busca ￿ltre esses objetos é uma ótima ideia_
øorém\tome cuidado_áma das boas práticas da programação sugere
que você deve evitar surpresas desagradáveis\ e fazer ￿ltros complexos
no default_scope é uma surpresa infeliz_r razão disso é que o com]
portamento torna]se implícito e di￿cilmente o programador que estiver
lendo o código Xinclusivevocê mesmoYlembrará da existência de um
default_scope_Ée necessário\peque pelo excesso de clareza ao decla]
rar um escopo nomeado\e não o contrário_
rntes de voltarmos ao projeto\vamos entrar um pouco mais a fundo no where\
pois ele tem algumas funcionalidades imprescindíveis ao desenvolvedor Áails_
￿￿￿

## Página 178

￿_￿_ tonsultas no banco de dados tasa do tódigo
óuscas tradicionais
rs buscas mais simples são as buscas que já vimos\ para buscar com valores exa]
tos_ øara isso\ basta passar um hash com a chave sendo a coluna e o valor sendo o
valor da buscak
"syr:whyry{low_tion4 'q_n nr_nwiswoc lj'}
@ qmõml? *usyrs*:[ n+)p *usyrs*
@ s#m+m *usyrs*:*low_tion* h 'q_n nr_nwiswoc lj'
rlém disso\podemos fazer buscas negadas\ usando o notk
+oom:whyry:not{low_tion4 'q_n nr_nwiswoc lj'}
@ qmõml? *rooms*:[ n+)p *rooms*
@ s#m+m {*rooms*:*low_tion* ~h 'q_n nr_nwiswoc lj'}
óuscas manuais
” ActiveRecord não possui mapeamento para buscas mais rebuscadas_•es]
ses casos\ precisamos fazer uma busca manualmente_øara isso\ basta colocarmos a
string com o conteúdo da busca diretamentek
"syr:whyry{'wonzirmyxu_t oq ()? ("õõ'}
@ qmõml? *usyrs*:[ n+)p *usyrs* s#m+m {wonzirmyxu_t oq ()? ("õõ}
É bastante importante notar que\ nesse caso\ não usamos nenhuma entrada do
usuário_uessa forma\não precisamos nos preocupar com É®“ znjectionXouinjeção
de É®“Y_zssoé útil para usar funcionalidades especí￿cas do banco de dados_øorém\
raramente é o caso que não precisamos passar um valor para efetuar buscas no banco_
￿￿￿

## Página 179

tasa do tódigo tapítulo ￿_ “ogin do usuário
O ￿￿￿ ￿ SQL ￿￿￿￿￿￿￿￿￿￿
É®“ znjection\ ou injeção de É®“\ é um ataque a um site de forma
que alguém injete códigos É®“ maliciosos_ ”s resultados podem ser
drásticos\ como conseguir poder de administrador\ deletar uma tabela
ou roubar dados importantes_–esmo aparentando ser um ataque sim]
ples\ainda é bastante utilizado_r fatídica queda da ølaystation •etwork®
em ￿￿￿￿\que afetou o sistema durante meses e milhões de usuários foram
prejudicados\foi uma única injeção de É®“_ âe j ao exemplo a seguirk
ym_il h 'viniv_00ioíyx_mply:wom'
"syr:whyry{*ym_il h '@{ym_il}'*}
@ qmõml? *usyrs*:[ n+)p *usyrs*
@ s#m+m {ym_il h 'viniv_00ioíyx_mply:wom'}
@
@ h- /@>"syr ix4 $$c zullun_my4 *riniwius ::: -3
ym_il h *' )+ $h$} çç*
"syr:whyry{*ym_il h '@{ym_il}'*}
@ qmõml? *usyrs*:[ n+)p *usyrs*
@ s#m+m {ym_il h '' )+ $h$} çç'}
@
@ h- /@>"syr ix4 $$c ::: -3
vsse é um exemplo simples mas prova o ponto que\se você não tomar
cuidado com os parâmetros\é possível que um usuário mal intencionado
ganhe acesso irrestrito ao seu site_
óuscas parametrizadas via írray
r forma mais simples de busca parametrizada é a forma clássica de consultas
que evitam É®“ znjection_øara esse tipo de parametrização\usamos o símbolo ? na
consulta e o ActiveRecord irá limpar os parâmetros e substituir os símbolos ?_
øara isso\passe uma rrray cujo primeiro valor é um “template”da busca e o restante
serão os valores a serem substituídos_vxemplok
ym_il h *viniv_00ioíyx_mply:wom*
"syr:whyry{/*ym_il h i*c ym_il3}
￿￿￿

## Página 180

￿_￿_ tonsultas no banco de dados tasa do tódigo
@ qmõml? *usyrs*:[ n+)p *usyrs*
@ s#m+m {ym_il h 'viniv_00ioíyx_mply:wom'}
@ h- /@>"syr 4ix4 $$c :::-3
ym_il h *' )+ $h$} çç*
"syr:whyry{/*ym_il h i*c ym_il3}
@ qmõml? *usyrs*:[ n+)p *usyrs*
@ s#m+m {ym_il h ''' )+ $h$} çç'}
@ h- /3
óuscas parametrizadas via hash
tom muitos parâmetros para substituir\usar o ? torna o template ilegível_øor
isso\ é possível usar símbolos no template para substituição de parâmetros_ ” se]
gundo parâmetro deverá ser um hash que mapeia cada símbolo para um valork
"syr:whyry{/*low_tion õo1m 4low_tion j(< ym_il h 4ym_il*c {
low_tion4 'bljb'c
ym_il4 'viniv_00ioíyx_mply:wom'
}3}
@ qmõml? *usyrs*:[ n+)p *usyrs*
@ s#m+m {
@ low_tion õo1m 'bljb'
@ j(< ym_il h 'viniv_00ioíyx_mply:wom'
@ }
óuscas em listas e intervalos
tom o where ainda é possível fazer buscas em listas e intervalos via o comando
É®“ IN ou BETWEEN_øara fazer esse tipo de busca\ basta usar a busca tradicional\
usando hashes e um rrrayk
"syr:whyry{ix4 /$c $dc $$c ed3}
@ qmõml? *usyrs*:[ n+)p *usyrs*
@ s#m+m *usyrs*:*ix* o( {$c $dc $$c ed}
"syr:whyry{ix4 $::$d}
@ qmõml? *usyrs*:[ n+)p *usyrs*
@ s#m+m {*usyrs*:*ix* km?smm( $ j(< $d}
vssas buscas são bastante úteis em datask
￿￿￿

## Página 181

tasa do tódigo tapítulo ￿_ “ogin do usuário
"syr:whyry{wonzirmyxu_t4 $:wyyk:_0o::?imy:now}
@ qmõml? *usyrs*:[ n+)p *usyrs*
@ s#m+m {
@ *usyrs*:*wonzirmyxu_t*
@ km?smm( 'ed$eçd!çd8 d!4é!4é5:5deée$'
@ j(< 'ed$eçd!ç$e d!4é!4é5:55$!5e'
@ }
￿n￿ E￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿ ￿￿￿￿￿￿￿￿￿￿
rgora que temos o conhecimento de como fazer buscas e escopos\ implementare]
mos um método chamado .authenticate no modelo usuário_vle receberá dois
parâmetros\ email e senha_ørecisaremos veri￿car\em todos os usuários válidos do
sistema Xouseja\ usuários que con￿rmaram seu emailY\qual possui o email e a senha
digitados_
øara isso\ criaremos um escopo nomeado que retornará todos os usuários que
con￿rmaram sua conta\ou seja\ confirmed_at é nulo_rdicione o seguinte scope
no modelo User Xapp/models/user.rbYk
wl_ss "syr
@ :::
swopy 4wonzirmyxc ç- { whyry:not{wonzirmyxu_t4 nil} }
@ :::
ynx
vm seguida\ criaremos o método .authenticate\ que faz a veri￿cação do
email e senha_âam o sencadear algumas chamadaskprimeiro buscaremos o usuário
pelo email_vm seguida\ executaremos o método #authenticate no usuário re]
tornado_vsse método irá retornar o próprio objeto se a senha estiver correta\ caso
contrário\retornará falsek
xyz sylz:_uthyntiw_ty{ym_ilc p_ssworx}
usyr h wonzirmyx:zinxuvy{ym_il4 ym_il}
iz usyr:prysynti
usyr:_uthyntiw_ty{p_ssworx}
ynx
ynx
É possível evitar o if usando um método do Áuby chamado #try_•esse mé]
todo\ passamos o nome do método que queremos executar\em seguida os seus pa]
râmetros_®uando o objeto é nil\ o método não será executado_Ée o objeto existir\
￿￿￿

## Página 182

￿_￿_ vscopo de usuário con￿rmado tasa do tódigo
o método será executado normalmente\ com os parâmetros especi￿cados_ âe j aos
exemplos a seguirk
strin0 h *ov_* @ h- *ov_*
strin0:try{4upw_sy} @ h- *)kj*
strin0 h nil @ h- nil
strin0:try{4upw_sy} @ h- nil
” resultado\aplicando o tryk
xyz sylz:_uthyntiw_ty{ym_ilc p_ssworx}
usyr h wonzirmyx:
zinxuvy{ym_il4 ym_il}:
try{4_uthyntiw_tyc p_ssworx}
ynx
â oltemos ao modelo UserSession Xapp/models/user_session.rbYk
xyz _uthyntiw_ty
usyr h "syr:_uthyntiw_ty{íym_ilc íp_ssworx}
iz usyr:prysynti
story{usyr}
ylsy
yrrors:_xx{4v_syc 4inv_lixulo0in}
z_lsy
ynx
ynx
•esse método\ que já ￿zemos\ o usuário só será retornado caso o email e senha
sejam válidos e o usuário esteja con￿rmado_vssa parte é muito importanteka classe
UserSession não precisa saber que existe a lógica de con￿rmação de usuários\ e
portanto\delegamos essa lógica apenas ao modelo que deve saber disso_
tom todos os objetos interligados\é possível testar o ￿uxo completo_•a página
httpk‘‘localhostk￿￿￿￿‘userúsessions‘new \ ao digitar as credenciais corretamente\te]
mos o seguinte resultadok
￿￿￿

## Página 183

tasa do tódigo tapítulo ￿_ “ogin do usuário
wigura￿_￿k“ogin com credenciais corretas
rgora\ quando digitamos as credenciais de forma incorretak
wigura￿_￿k“ogin com credenciais inválidas
tom o login construído\ no próximo capítulo vamos melhorar a estrutura da
nossa aplicação de forma a mostrar ao usuário autenticado\na barra de navegação\
links para editar o per￿l e fazer logout_taso o usuário não estiver logado\ mostra]
remos um link para que ele possa fazer o login_
âam o stambém fazer o controle de acesso\ como por exemplo\impedir que um
usuário edite o per￿l de outro usuário\ e que um usuário só possa cadastrar um
quarto quando estiver autenticado_
￿￿￿

## Página 185

t ￿￿￿￿￿￿￿ ￿￿
tontrole de acesso
Formação em íiência da íomputa ção consegue tornar qualquer pessoa um excelente
programador tanto quanto estudar pincéis e pigmentos torna qualquer pessoa um
excelente pintorp
– vric Áaymond\autor de ‘r catedral e o bazar’
tadastro e login prontos\agora focaremos no controle de acesso_ørimeiro\ va]
mos alterar nosso template para exibir uma barra de navegação diferenciada para o
usuário logado_rtualmente\ a barra é assimk
wigura￿￿_￿ksarra de navegação sem informações de sessao
•a versão para o visitante\que não está logado\deverá ￿car assimk

## Página 186

￿￿_￿_ yelpers de sessão tasa do tódigo
wigura￿￿_￿ksarra de navegação sem login
øor ￿m\ quando o usuário estiver logado\o resultado serák
wigura￿￿_￿ksarra de navegação com per￿l do usuário
vm seguida\ vamos controlar o ￿uxo para que um usuário só possa editar o seu
próprio per￿l_ Íamb ém vamos corrigir as ações de login e cadastro apenas para
quando o usuário não estiver logado_
âam o sgarantir que\ para um usuário cadastrar um quarto\ ele precisa estar lo]
gado_{unto a isso\vamos associar o quarto cadastrado a ele\aprendendo como criar
relacionamento entre modelos ActiveRecord_øor ￿m\ vamos também controlar
o acesso de edição de quartos\ dando a permissão apenas a seus donos\ uma lição
importante de segurança de dados_
￿￿n￿ H￿￿￿￿￿￿￿￿ ￿￿￿￿￿￿
rntes de alterar a nossa barra\vamos criar métodos para nos auxiliar com a sessão do
usuário_tomo esse conceito é inerente à aplicação inteira\ vamos criar os seguintes
métodos no ApplicationControllerk
• user_signed_in? ] –étodo que veri￿ca se o usuário possui uma sessão
autenticadal
• current_user ] Áetorna o objeto da classe User que está na sessão atuall
• require_authentication ] wiltro que força a autenticação de usuários\
redirecionando]o à pagina de login caso não esteja logado\e não fazendo nada
caso o usuário esteja com uma sessão válidal
￿￿￿

## Página 187

tasa do tódigo tapítulo ￿￿_ tontrole de acesso
• require_no_authentication ] wiltropara evitar que usuários cadastra]
dos tentem acessar páginas que só deverão ser acessadas quando o usuário não
tiver um login Xcomopáginas de cadastro e de loginY_
âam o sláQøara criar essa lógica\ vamos ter que adicionar um pouco de com]
portamento na classe de sessões de usuário\a UserSession_triaremos o método
que buscará o usuário na sessão Xcurrent_userY_ørecisamos saber também se a
sessão do usuário é válida\ portanto veri￿caremos a presença do zu do usuário na
sessão\ no método Xuser_signed_in?Yk
wl_ss "syrqyssion
@:::
xyz wurryntuusyr
"syr:zinx{ísyssion/4usyruix3}
ynx
xyz usyrusi0nyxuini
ísyssion/4usyruix3:prysynti
ynx
ynx
tom esses dois métodos no UserSession\ conseguimos fazer tudo o que pre]
cisamos no ApplicationController_ “embre]se que\ ao criar um método no
ApplicationController\ todas os controles da aplicação que herdam dela tam]
bém terão esses métodos_rdicionaremos então métodos para obter as informações
sobre a sessão e então\ criaremos os métodos que serão usados como ￿ltros de re]
quisições_
vm primeiro lugar\criaremos o método user_session\ que criará uma ins]
tância do UserSession baseada na sessão do usuário_ ”s outros devem chamar
comportamentos que já implementamos na classe UserSession\ portanto\usare]
mos o método delegate_ ” delegate\ extensão do ActiveSupport\ criará
métodos na classe que repassarão a mensagem para o objeto mencionado_r princí]
pio parece ser trabalhoso\ mas é importante lembrar das responsabilidades de cada
componente_
wl_ss jppliw_tionlontrollyr > jwtionlontrollyr44k_sy
xyly0_ty 4wurryntuusyrc 4usyrusi0nyxuinic to4 4usyrusyssion
@ :::
￿￿￿

## Página 188

￿￿_￿_ yelpers de sessão tasa do tódigo
xyz usyrusyssion
"syrqyssion:nyw{syssion}
ynx
ynx
”s ￿ltros serão doisk o require_authentication\ que irá redirecionar o
usuário à pagina de login caso a sessão não seja válida\ com uma mensagem_vm se]
guida\ o require_no_authentication irá redirecionar o usuário para a página
principal\ com uma mensagem_
wl_ss jppliw_tionlontrollyr > jwtionlontrollyr44k_sy
@ :::
xyz ryquiryu_uthyntiw_tion
unlyss usyrusi0nyxuini
ryxirywtuto nywuusyrusyssionsup_thc
_lyrt4 t{'zl_sh:_lyrt:nyyxsulo0in'}
ynx
ynx
xyz ryquiryunou_uthyntiw_tion
iz usyrusi0nyxuini
ryxirywtuto rootup_thc
notiwy4 t{'zl_sh:notiwy:_lry_xyulo00yxuin'}
ynx
ynx
ynx
É importante ressaltar um comportamento de ￿ltrosk se o ￿ltro executar uma
redireção ou alguma renderização de template Xvia redirect_to ou renderY\a
ação e ￿ltros seguintes não serão executados_ zsso é bastante conveniente para os
￿ltros require_authentication e require_no_authentication\ mas é
importante lembrar desse fato em ￿ltros que você criar no futuro_zsso é quase tudo
que precisamos_
”s métodos current_user e user_signed_in? podem ser usados em con]
troles\mas é importante usá]los também nos templates_øara disponibilizar um mé]
todo do controle nos templates\usamos a class macro helper_method_sasta fazerk
wl_ss jppliw_tionlontrollyr > jwtionlontrollyr44k_sy
xyly0_ty 4wurryntuusyrc 4usyrusi0nyxuinic to4 4usyrusyssion
￿￿￿

## Página 189

tasa do tódigo tapítulo ￿￿_ tontrole de acesso
hylpyrumythox 4wurryntuusyrc 4usyrusi0nyxuini
@ :::
ynx
Te mp l ate sda barra
rgora que temos os métodos de controle de sessão do usuário\ já é possível
aprimorar nossa barra de navegação_ øara isso\ vamos ao layout da aplicação X
app/views/layouts/application.html.erbYe vamos extrair a barra de na]
vegação em uma partialk
:::
>hy_xyr-
>xiv ixh*hy_xyrçwr_p*-
>h$-<%= linkuto *wolwho:nyt*c rootup_th %> >,h$-
<% iz usyrusi0nyxuini %>
<%= rynxyr 'l_youts,usyrun_vv_r' %>
<% ylsy %>
<%= rynxyr 'l_youts,visitorun_vv_r' %>
<% ynx %>
>,xiv-
>,hy_xyr-
:::
rgora vamos criar o template app/views/layouts/_visitor_navbar.html.erb_
•ote que tivemos que especi￿car o caminho da partial_zsso deve]se ao fato de que\
como o layout é executado em todas as ações\ o caminho de busca de templates ￿ca
relativo a cada controle_vspeci ￿cando o caminho\ garantimos que\ não importa o
controle em execução\a partial sempre será achada_Í emos que fazer o mesmo com
as chaves de traduçãok
>n_v-
>ul-
>li-<%= linkuto t{'l_yout:rooms'}c roomsup_th %> >,li-
>li-<%= linkuto t{'l_yout:si0nup'}c nywuusyrup_th %> >,li-
>li-<%= linkuto t{'l_yout:si0nin'}c nywuusyrusyssionsup_th %> >,li-
>,ul-
>,n_v-
” resultado é o seguintek
￿￿￿

## Página 190

￿￿_￿_ yelpers de sessão tasa do tódigo
wigura￿￿_￿ksarra de navegação sem login
r barra de navegação para usuários logados ￿ca da seguinte forma X
app/views/layouts/_user_navbar.html.erbYk
>n_v-
>ul-
>li-<%= linkuto t{'l_yout:nywuroom'}c nywuroomup_th %> >,li-
>li-<%= linkuto t{'l_yout:rooms'}c roomsup_th %> >,li-
>li-
<%= linkuto t{'l_yout:myuprozily'}c
usyrup_th{wurryntuusyr} %>
>,li-
>li-
<%= linkuto t{'l_yout:si0nout'}c usyrusyssionsup_thc
mythox4 4xylyty %>
>,li-
>,ul-
>,n_v-
øara fazer o logout\ o que precisamos é apagar a sessão do usuário\ via a ação
destroy_ ue acordo com a nossa rota\ para executar essa ação\ precisamos fazer
DELETE /user_sessions_ ” problema é que essa ação yÍÍø não é suportada
por todos os browsers\portanto o Áails tem um mecanismo para executar esse tipo
de operaçãok
>_ hryzh*,ptçk+,usyrusyssions* x_t_çmythoxh*xylyty*
rylh*nozollow*-
õo0out
>,_-
” código anterior possui um atributo data-*\ válido no yÍ–“ ￿_vle é usado
para colocar\ em templates yÍ–“\ dados que possam ser usados de outra forma\
como por exemplo\{avaÉcript_
” Áails então usa o data-method via {avaÉcript para simular o DELETE_r
forma que isso é feito é através da criação de um formulário Xusando POSTY\e in]
￿￿￿

## Página 191

tasa do tódigo tapítulo ￿￿_ tontrole de acesso
cluindo um campo chamado _method_•o processamento da requisição\esse atri]
buto faz com que o Áails interprete a requisição como DELETE_tom outros tipos
de clientes yÍÍø browsers\ é possível chamar o DELETE diretamente_
øor ￿m\ adicionamos novas chaves na seção “layout” do arquivo de z￿￿n X
config/locales/pt-BR.ymlYk
l_yout4
rooms4 .u_rtos
nywuroom4 l_x_stry syu qu_rto~
si0nup4 l_x_stro
si0nin4 õo0in
myuprozily4 pyu pyrzil
si0nout4 õo0out
” resultado ék
wigura￿￿_￿ksarra de navegação com per￿l do usuário
Í odos os links estão funcionais e traduzidos\ porém ainda não implementamos
aa ção de destruir a sessão do usuário\e é isso que vamos fazer agora_
Logout
âam o sprimeiro à classe UserSession Xapp/models/user_session.rbY_
øara removermos um item da sessão\ basta associar nil ao itemk
wl_ss "syrqyssion
@ :::
xyz xystroy
ísyssion/4usyruix3 h nil
ynx
ynx
zsso é su￿ciente para que todo o login seja desfeito\ ou seja\ o cookie será al]
terado e todo o resto da aplicação não detectará o usuário como logado_ rgora
precisamos chamar esse método no controle UserSessionsController X
app/controllers/user_sessions_controller.rbYk
￿￿￿

## Página 192

￿￿_￿_ •ão permita edição do per￿l alheio tasa do tódigo
wl_ss "syrqyssionslontrollyr > jppliw_tionlontrollyr
@ :::
xyz xystroy
usyrusyssion:xystroy
ryxirywtuto rootup_thc notiwy4 t{'zl_sh:notiwy:si0nyxuout'}
ynx
ynx
” método user_session foi criado no ApplicationController e vamos
usá]lo para tornar o uso desse objeto mais fácil_sasta agora incluir essa mensagem
no z￿￿n Xconfig/locales/pt-BR.ymlYe acabamos a barraQ
zl_sh4
_lyrt4
nyyxsulo0in4 *rowê prywis_ yst_r lo0_xo p_r_ wontinu_r*
notiwy4
si0nyxuin4 'õo0in yzytu_xo wom suwysso~'
si0nyxuout4 'õo0out yzytu_xo wom suwysso: jté lo0o~'
_lry_xyulo00yxuin4 *rowê já ystá lo0_xo:*
wigura￿￿_￿k–ensagem de logout após clicar no link
￿￿n￿ N￿￿ ￿￿￿￿￿￿￿ ￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿￿￿￿￿
uepois do cadastro e do login\ ainda é possível editar qualquer per￿l_øara ver isso
funcionando\basta ir ao seu per￿l e mudar o ID na rota para outro usuário que você
tenha cadastrado_
øara prevenir essa situação\ vamos usar um ￿ltrokveri￿camos se o usuário está
logado e se o usuário logado é o mesmo que tentamos editar ou atualizar_sasta então
￿￿￿

## Página 193

tasa do tódigo tapítulo ￿￿_ tontrole de acesso
comparar o ID do usuário na rota com o usuário da sessão_taso não sejam iguais\
redirecionamos o usuário apenas para a visualização do per￿l_rplicaremos o ￿ltro
apenas nas ações edit e update_
” ￿ltro can_change\ no controle de usuários X
app/controllers/users_controller.rbY\￿cará assimk
wl_ss "syrslontrollyr > jppliw_tionlontrollyr
vyzoryu_wtion 4w_nuwh_n0yc only4 /4yxitc 4upx_ty3
@ :::
priv_ty
xyz usyrup_r_ms
p_r_ms:
ryquiry{4usyr}:
pyrmit{4ym_ilc 4zullun_myc 4low_tionc 4p_ssworxc
4p_ssworxuwonzirm_tionc 4vio}
ynx
xyz w_nuwh_n0y
unlyss usyrusi0nyxuini \\ wurryntuusyr hh usyr
ryxirywtuto usyrup_th{p_r_ms/4ix3}
ynx
ynx
xyz usyr
íusyr ||h "syr:zinx{p_r_ms/4ix3}
ynx
ynx
ásamos no método user uma expressão idiomática de Áuby chamada memoio
zation Xou“memorização”Y_•essa expressão\ apenas associamos a variável Xepor
consequência\ fazemos a busca no banco de dadosYcaso ela nunca tenha sido inici]
ada_âo c êpode pensar nisso como um cache de variável_
rproveitando que estamos no controle de usuários\ vamos forçar que\ para a
página de cadastro\ é necessário não estar logado_øara isso\ basta usar o ￿ltro que
criamos\ require_no_authentication_–esmo que não haja acesso através das
páginas\ é uma boa ideia proteger essas açõesk
￿￿￿

## Página 194

￿￿_￿_ •ão permita edição do per￿l alheio tasa do tódigo
wl_ss "syrslontrollyr > jppliw_tionlontrollyr
vyzoryu_wtion 4ryquiryunou_uthyntiw_tionc only4 /4nywc 4wry_ty3
vyzoryu_wtion 4w_nuwh_n0yc only4 /4yxitc 4upx_ty3
@:::
ynx
rdicionaremos o mesmo ￿ltro na ação de login Xtanto para o formulá]
rio quanto para a ação createY\no controle UserSessionsController X
app/controllers/user_sessions_controller.rbY_wiltraremostambém a
ação destroy para apenas usuários logados Xcomo único intuito de evitar ver o
flash mesmo não tendo feito ação algumaYk
wl_ss "syrqyssionslontrollyr > jppliw_tionlontrollyr
vyzoryu_wtion 4ryquiryunou_uthyntiw_tionc only4 /4nywc 4wry_ty3
vyzoryu_wtion 4ryquiryu_uthyntiw_tionc only4 4xystroy
@ :::
ynx
triaremos esses ￿ltros para o cadastro e atualização de quartos Xaproveitamos
para fazer uma limpeza\ tal como colocar z￿￿n\ remover os comentários e remo]
ver o tratamento para respostas em {É”•Y\ no controle RoomsController X
app/controllers/rooms_controller.rbYk
wl_ss +oomslontrollyr > jppliw_tionlontrollyr
vyzoryu_wtion 4ryquiryu_uthyntiw_tionc
only4 /4nywc 4yxitc 4wry_tyc 4upx_tyc 4xystroy3
xyz inxyx
írooms h +oom:_ll
ynx
xyz show
íroom h +oom:zinx{p_r_ms/4ix3}
ynx
xyz nyw
íroom h +oom:nyw
ynx
￿￿￿

## Página 195

tasa do tódigo tapítulo ￿￿_ tontrole de acesso
xyz yxit
íroom h +oom:zinx{p_r_ms/4ix3}
ynx
xyz wry_ty
íroom h +oom:nyw{p_r_ms/4room3}
iz íroom:s_vy
ryxirywtuto íroomc notiwy4 t{'zl_sh:notiwy:roomuwry_tyx'}
ylsy
rynxyr _wtion4 *nyw*
ynx
ynx
xyz upx_ty
íroom h +oom:zinx{p_r_ms/4ix3}
iz íroom:upx_ty{p_r_ms/4room3}
ryxirywtuto íroomc notiwy4 t{'zl_sh:notiwy:roomuupx_tyx'}
ylsy
rynxyr _wtion4 *yxit*
ynx
ynx
xyz xystroy
íroom h +oom:zinx{p_r_ms/4ix3}
íroom:xystroy
ryxirywtuto roomsuurl
ynx
ynx
￿￿￿

## Página 196

￿￿_￿_ Áelacionando seus objetos tasa do tódigo
P￿￿ ￿￿￿ ￿￿￿￿￿￿￿￿ ￿￿￿￿￿ ￿￿ ￿￿￿￿￿ ￿￿￿ ￿￿￿￿￿￿￿￿
øara todas as opções de segurança\ pre￿ra ser especí￿co_ •o caso
anterior\poderíamos fazerk
vyzoryu_wtion 4ryquiryu_uthyntiw_tionc
yxwypt4 /4inxyxc 4show3
øorém\ novas ações automaticamente terão o ￿ltro
require_authentication aplicado e não necessariamente isso
é o que nós queremos_ rlém disso\ ao ser especí￿co\ é mais fácil
perceber o que está acontecendo e ajuda a nos lembrar a con￿gurar as
permissões corretamente_
toncluímos a parte de ￿ltros\fazendo com que o usuário tenha que estar logado
XounãoYem algumas situações_ rinda temos que fazer o controle de permissões\
ou seja\ não permitir que um usuário não possa editar um quarto que não pertença
a ele_ øara que possamos adicionar posse de objetos no sistema\ é necessário criar
relacionamentos_Áelacionamentosentre objetos no ActiveRecord é bastante fácil
de usar\e é isso que vamos estudar em seguida_
￿￿n￿ R￿￿￿￿￿￿￿￿￿￿￿ ￿￿￿￿￿￿￿￿￿￿￿
vm sistemas envolvendo bancos de dados\ é necessário identi￿car um objeto uni]
vocamente_ r estratégia mais comum para gerar essa identi￿cação é via a gera]
ção de números sequenciais_ vssa estratégia é tão comum que a maioria dos ban]
cos de dados possuem uma implementação embutida_ uessa maneira\ ao anotar o
campo como um identi￿cador\ ou chave primária\ toda vez que criarmos um ob]
jeto\o banco de dados poderá\ automaticamente\incrementar o valor do contador e
associá]lo ao novo registro_
É possível armazenar chaves primárias em outras tabelas\ de modo a criar uma
espécie de ponteiro_vsse campo é conhecido como chave estrangeira\ou pelo nome
em inglês\ foreign key_tom as chaves estrangeiras\ é possível implementar diversos
tipos de relacionamentos_
” relacionamento mais simples é conhecido como o relacionamento um]para]
um\ ou seja\ um objeto possui uma referência direta a outro_ám exemplo seria uma
￿￿￿

## Página 197

tasa do tódigo tapítulo ￿￿_ tontrole de acesso
conta de usuário\ na tabela profiles\ que possuiria uma foto de per￿l\ da tabela
profile_pictures_•a tabela profile_pictures criamos registros que pos]
suam a chave estrangeira user_id\ apontando para o usuário que é dono da foto_
É comum também referirmos a esse relacionamento como profile_pictures
pertence a Xbelongs toY users_
wigura￿￿_￿kuiagrama do relacionamento um]para]um
r modelagem um]para]muitos é a modelagem mais popular_•ela\ um objeto
pode possuir nenhum\um\ ou muitos outros objetos relacionados_ám exemplo é o
que teremos no próprio colcho_netkum usuário pode ter nenhum quarto\um quarto
apenas ou o número que quiser cadastrar\ sem restrições_ r implementação desse
relacionamentoé da mesma maneira que o relacionamento um]para]um\porém não
há imposições lógicas de quantos elementos associados podem existir_
wigura￿￿_￿kuiagrama do relacionamento um]para]muitos
øor ￿m\ o último tipo de relacionamento que o Áails nos ajuda a fazer é o relaci]
onamento muitos]para]muitos_øara essa associação existir\é necessário uma tabela
intermediária\ chamada tabela de ligação_zmagine uma situação em que um usuá]
￿￿￿

## Página 198

￿￿_￿_ Áelacione quartos a usuários tasa do tódigo
rio possa participar de vários projetos e que um projeto possua vários membros_É
necessário criar uma tabela que contenha duas chaves]estrangeiras\uma apontando
ao usuário e outra apontando ao projeto_
É natural que as tabelas de ligação acabem ganhando vida própria como um
conceito dentro do sistema\ ou seja\ elas possuam outros atributos além de apenas
chaves]estrangeiras_øara o caso do exemplo anterior\é natural chamar a tabela de
ligação de “participação” _
wigura￿￿_￿kuiagrama do relacionamento muitos]para]muitos
” ActiveRecord possui facilidades para os três tipos de relacionamentos que
vimos_ âam o s aprender na prática como vamos criar uma associação um]para]
muitos e muitos]para]muitos_ ueixaremos a implementação de relacionamentos
um]para]um de lado pois a implementação é praticamente a mesma dos relacio]
namentos muitos]para]muitos_
￿￿n￿ R￿￿￿￿￿￿￿￿￿￿￿￿￿￿￿ ￿ ￿￿￿￿￿￿￿￿
” que vamos fazer é criar a associação um]para]muitos entre usuários e quartos_ám
usuário poderá ter nenhum\ um\ ou vários quartos_øara isso\precisamos adicionar
uma chave]estrangeira no modelo Room para apontar para User_ triamos então
uma migraçãok
ã r_ils 0 mi0r_tion _xxuusyruixutourooms usyr4ryzyrynwys
invoky _wtivyuryworx
wry_ty xv,mi0r_ty,ed$éd!$5d!8éééu_xxuusyruixutourooms:rv
tomo usamos references como tipo da coluna\ o Áails já gerou o código
apropriado para criar a chave]estrangeira\ adicionando uma referência Xnocaso do
Áails\ um campo de números inteirosYque possui um índice\ para tornar o acesso
mais rápido_
￿￿￿

## Página 199

tasa do tódigo tapítulo ￿￿_ tontrole de acesso
wl_ss jxx"syrox?o+ooms > jwtivy+yworx44pi0r_tion
xyz wh_n0y
_xxuryzyrynwy 4roomsc 4usyrc inxyx4 truy
ynx
ynx
õ ￿￿￿￿￿￿￿￿ ￿￿￿￿￿ ￿￿￿￿￿￿m￿￿￿￿￿￿￿￿￿￿￿￿
r melhor maneira é seguir os padrões do Áails e usar os métodos que
ele provê para você_ rssim você poderá usar o máximo de funcionali]
dades que o Áails possui\ sem a necessidade de ter que reimplementar o
que o Áails já faz_
taso não seja possível fazer como ￿zemos anteriormente\ é pos]
sível ainda garantir o funcionamento de relacionamentos com o
ActiveRecord_ sasta que você nomeie sua chave]estrangeira como
nome_do_relacionamento [ _id\ nesse caso\ user_id_ wazendo
dessa maneira\o ActiveRecord é capaz de derivar automaticamenteo
nome da coluna para fazer uniões de tabelas_
•ote que o ActiveRecord não cria nenhum mecanismo de chaves]
estrangeiras no banco de dados XcomoconstraintsY\portanto se você tiver interesse
em fazer isso\deverá executar É®“ manualmente\usando o método execute\lem]
brando que isso resultará no acoplamento de suas migrações em um banco de dados
especí￿co_
D￿￿￿￿￿￿￿￿￿ ￿￿￿￿￿ ￿￿ ￿￿￿￿￿
É recomendado que você estude o sistema que está usando com cui]
dado Xcomotoda ferramentaQYe aplicar con￿gurações e boas práticas de
uso_øor exemplo\se seu sistema de banco de dados suporta constraints
de chaves]estrangeiras\tal como o øostgreÉ®“\ não tenha medo de usá]
lo só porque o Áails não possui um método para tal_
rpós executar rake db:migrate\ editaremos o modelo Room X
app/models/room.rbY e colocar uma class macro para indicar que o mo]
delo quarto pertence a um usuário_
￿￿￿

## Página 200

￿￿_￿_ Áelacione quartos a usuários tasa do tódigo
tom a class macro belongs_to\é possível associar os objetos na relação quarto
-> usuário_ ” ActiveRecord já sabe qual objeto deve criar devido ao nome do
relacionamento X:userYe também já sabe qual campo usar para buscar o objeto
devido Xuser_idYk
wl_ss +oom > jwtivy+yworx44k_sy
vylon0suto 4usyr
@ :::
ynx
âe j ao seguinte exemplok
usyr h "syr:zirst
@ h- @>"syr ix4 $$c ::: -
room h +oom:zirst
@ h- @>+oom ix4 éc :::c usyruix4 nil-
room:usyr h usyr
@ h- @>"syr ix4 $$c ::: -
room:s_vy
@ h- truy
room:usyr
@ h- @>"syr ix4 $$c :::-
tom esse relacionamento\já é possível mostrar\na página de um quarto\ o seu
dono_–as antes de chegar lá\ ainda não é possível saber quais quartos um usuário
possui_ Éeguindo todas as convenções do Áails\ adicionar a outra parte do relacio]
namento é apenas chamar a class macro has_many_
r class macro has_many faz várias coisas para descobrir o relacionamento_
ørimeiro\ como é um relacionamento um]para]muitos Xhas many signi￿ca\ literal]
mente\“tem muitos”Y\o nome do relacionamento deverá estar no plural e portanto\
o modelo é o Room_ uada a natureza do relacionamento\o ActiveRecord sabe
também que o modelo room deverá ter um campo para o próprio modelo user
Xuser_idYe então ￿nalmente\ consegue buscar todos os quartos que pertencem a
um usuário_
sasta então adicionar uma única linha no modelo User X
app/models/user.rbYk
￿￿￿

## Página 201

tasa do tódigo tapítulo ￿￿_ tontrole de acesso
wl_ss "syr > jwtivy+yworx44k_sy
mpjoõu+m9m;% h ,tj/2í3]í{/2ít:3]t:}]/2ít:3]tz,
h_sum_ny 4rooms
@ :::
ynx
âe j ao exemplo abaixok
usyr h "syr:zirst
@ h- @>"syr ix4 $$c ::: -
usyr:rooms
@ h- @>jwtivy+yworx44jssowi_tions44lollywtion%roxy
@ /@>+oom ix4 ec ::: 3-
•ote no exemplo anterior como o relacionamento rooms retorna algo parecido
com um Array_ •a verdade\ esse objeto nada mais é que um escopo_ zsso signi]
￿ca que ainda é possível aplicar qualquer método de busca que vimos na seção “￿_￿
tonsultas no banco de dados” \inclusive escopos nomeadosk
usyr:rooms:whyry{'titly liky i'c 'bvi0b'}
@ qmõml? *rooms*:[ n+)p *rooms*
@ s#m+m *rooms*:*usyruix* h $$ j(< {titly liky 'bvi0b'}
@
@ h- @>jwtivy+yworx44+yl_tion /@>+oom ix4 éc titly4 *ki0 vyxroom*c :::-3-
øronto\ o relacionamento um]para]muitos está criadoQâ eremos no capítulo ￿￿\
“ rvaliação de quartos\relacionamentosmuitos para muitos e organização do código”
como criar o tipo de relacionamento muitos]para]muitos_
E ￿ ￿￿￿￿￿￿￿￿￿￿￿￿￿￿ ￿￿ m￿￿￿￿m￿￿￿
” relacionamento um]para]um é quase igual ao relacionamento
um]para]muitos_ r diferença é que\ ao invés de usar a class macro
has_many\ você usa o has_one Xdeixandoo nome no singular\como
user ao invés de usersY_É importante que o belongs_to sempre
￿que no modelo que possui a chave]estrangeira_
Áelacionamentos prontos\ vamos dar início ao tratamento de segurança de da]
dos_
￿￿￿

## Página 202

￿￿_￿_ “imite o acesso usando relacionamentos tasa do tódigo
￿￿n￿ L￿￿￿￿￿￿ ￿￿￿￿￿￿￿￿￿￿￿￿ ￿￿￿￿￿￿￿￿￿￿￿￿￿￿￿
”s escopos são ótimos para controlar permissões de acesso e permitir apenas que da]
dos interessantes sejam exibidos_tomo os relacionamentos também são\ é possível
usá]los para limitar o que o usuário pode alterar_
øara isso\vamos usar a seguinte técnicakao invés de fazer a busca Xcomo .findY
do modelo via seu id\ sempre que formos criar\ atualizar ou deletar um objeto do
banco\vamos limitar o escopo de acesso ao usuário logado_uessa forma\se o usuário
logado não tiver permissão para acessar aquele objeto\o usuário irá deparar]se com
um erro de øágina não encontrada X￿￿￿Y_
ásar a associação possui outra vantagemkconstruir novos objetos usando a as]
sociação fará com que o objeto criado já tenha a sua chave]estrangeira preenchida
corretamente_âe j ao exemplok
usyr h "syr:zirst
@ h- @>"syr ix4 $$c ::: -
usyr:rooms:vuilx titly4 '.u_rto _wonwhy0_nty'c
xyswription4 '.u_rto 0r_nxy wom muit_ luz n_tur_l:'
@ h- @>+oom ix4 nilc
@ titly4 *.u_rto _wonwhy0_nty*c
@ low_tion4 nilc
@ xyswription4 *.u_rto 0r_nxy wom v_st_nty luz n_tur_l:*c
@ wry_tyxu_t4 nilc
@ upx_tyxu_t4 nilc
@ usyruix4 $$-
room:usyr
@ h- @>"syr ix4 $$c :::-
zssoé útil para não termos que associar nos preocupar em ligar os objetos_âam o s
aplicar essa ideia no controle RoomsController\mas antes vamos fazer uma pausa
para uma lição importanteksegurança de dados_
” uiaspora Xhttpk‘‘joindiaspora_comYé uma alternativa livre ao wacebookXhttpk
‘‘facebook_comY_Éuaproposta é que\ao contrário do wacebook\os dados dos usuá]
rios são realmente privados e a plataforma possui código]fonte livre para ser inves]
tigado_ âo c êpode\ por exemplo\ instalar o uiaspora em um servidor privado seu
e possuir sua própria rede social_ øor causa de sua causa nobre\ fez bastante baru]
lho nos vstados ánidos no seu lançamento\ porém\ também foi um grande ￿asco
técnico no lançamento_
￿￿￿

## Página 203

tasa do tódigo tapítulo ￿￿_ tontrole de acesso
r plataforma que deveria ser segura e privada possuía grandes falhas de segu]
rança de forma que qualquer usuário poderia ver\criar e editar fotos e outros conteú]
dos de qualquer usuário_”bviamente os desenvolvedores do uiaspora aprenderam
com os erros e já melhoraram a plataforma_ rpesar de uma falha simples\ muitas
aplicações Áails possuem o mesmo problema_
” problema estava nos controles\ e temos exatamente a mesma situação ocor]
rendo no controle do recurso quartok como só buscamos o objeto por id\ pode]
mos forjar uma requisição de alteração apenas alterando a áÁ“_ tom isso\podemos
acessar e alterar recursos que eu\ como usuário\não deveria ter acesso_âe j ao nosso
controle RoomsController\ no qual buscamos o quarto pelo parâmetro na áÁ“k
wl_ss +oomslontrollyr > jppliw_tionlontrollyr
vyzoryu_wtion 4ryquiryu_uthyntiw_tionc
only4 /4nywc 4yxitc 4wry_tyc 4upx_tyc 4xystroy3
@ :::
xyz upx_ty
íroom h +oom:zinx{p_r_ms/4ix3}
iz íroom:upx_ty{p_r_ms/4room3}
ryxirywtuto íroomc notiwy4 t{'zl_sh:notiwy:roomuupx_tyx'}
ylsy
rynxyr _wtion4 *yxit*
ynx
ynx
ynx
” que acontece é que temos o ￿ltro para impedir que um usuário não logado
faça atualizações Xeoutras ações também\ como removerYem qualquer objeto\mas
isso não implica que um usuário não pode atualizar um quarto que não pertence a
ele_
øara explorar essa falha de segurança\basta abrir um formulário de edição de um
quarto que pertença a você\alterar o zu do quarto na áÁ“\ e submeter o formulário_
” código irá buscar pelo quarto\que existe e é valido\e irá atualizar o objeto_
r melhor forma de impedir isso é sempre usar escopos quando ￿zermos bus]
cas de objetos_ •o nosso caso\ o usuário atual possui quartos\ então vamos usar o
has_many a nosso favork
￿ wl_ss +oomslontrollyr > jppliw_tionlontrollyr
￿ vyzoryu_wtion 4ryquiryu_uthyntiw_tionc
￿￿￿

## Página 204

￿￿_￿_ “imite o acesso usando relacionamentos tasa do tódigo
￿ only4 /4nywc 4yxitc 4wry_tyc 4upx_tyc 4xystroy3
￿
￿ @ :::
￿
￿ xyz upx_ty
￿ íroom h wurryntuusyr:rooms:zinx{p_r_ms/4ix3}
￿
￿￿ iz íroom:upx_ty{roomup_r_ms}
￿￿ ryxirywtuto íroomc notiwy4 t{'zl_sh:notiwy:roomuupx_tyx'}
￿￿ ylsy
￿￿ rynxyr _wtion4 *yxit*
￿￿ ynx
￿￿ ynx
￿￿
￿￿ @:::
￿￿
￿￿ priv_ty
￿￿
￿￿ xyz roomup_r_ms
￿￿ p_r_ms:
￿￿ ryquiry{4room}:
￿￿ pyrmit{4titlyc 4low_tionc 4xyswriptions}
￿￿ ynx
￿￿ ynx
r única alteração foi a linha ￿\ ao invés de buscarmos no modelo\ busca]
mos pelos quartos que o usuário tem acesso_ uessa forma\ mesmo se um usuá]
rio mal intencionado alterar o zu do recurso no formulário\ a atualização do mo]
delo não irá ocorrer_ zsso acontece porque\ ao tentar buscar em seus quartos\
o objeto não será encontrado_ ” ActiveRecord então irá disparar a exceção
ActiveRecord::RecordNotFound e o controle irá retornar um erro 404 Not
found XnãoencontradoYpara o usuário\o comportamento correto_
rplicando essa correção segurança X e aproveitando para fa]
zer limpezas no códigoY\ o controle RoomsController X
app/controllers/rooms_controller.rbY￿ca\ por ￿mk
wl_ss +oomslontrollyr > jppliw_tionlontrollyr
vyzoryu_wtion 4ryquiryu_uthyntiw_tionc
only4 /4nywc 4yxitc 4wry_tyc 4upx_tyc 4xystroy3
￿￿￿

## Página 205

tasa do tódigo tapítulo ￿￿_ tontrole de acesso
xyz inxyx
@ mxyrwíwio pr_ vowê~ lriy um yswopo p_r_ orxyn_r
@ os qu_rtos xos m_is rywyntys _os m_is _nti0os:
írooms h +oom:mosturywynt
ynx
xyz show
íroom h +oom:zinx{p_r_ms/4ix3}
ynx
xyz nyw
íroom h wurryntuusyr:rooms:vuilx
ynx
xyz yxit
íroom h wurryntuusyr:rooms:zinx{p_r_ms/4ix3}
ynx
xyz wry_ty
íroom h wurryntuusyr:rooms:vuilx{roomup_r_ms}
iz íroom:s_vy
ryxirywtuto íroomc notiwy4 t{'zl_sh:notiwy:roomuwry_tyx'}
ylsy
rynxyr _wtion4 *nyw*
ynx
ynx
xyz upx_ty
íroom h wurryntuusyr:rooms:zinx{p_r_ms/4ix3}
iz íroom:upx_ty{roomup_r_ms}
ryxirywtuto íroomc notiwy4 t{'zl_sh:notiwy:roomuupx_tyx'}
ylsy
rynxyr _wtion4 *yxit*
ynx
ynx
xyz xystroy
íroom h wurryntuusyr:rooms:zinx{p_r_ms/4ix3}
íroom:xystroy
￿￿￿

## Página 206

￿￿_￿_ vxibição e listagem de quartos tasa do tódigo
ryxirywtuto roomsuurl
ynx
priv_ty
xyz roomup_r_ms
p_r_ms:
ryquiry{4room}:
pyrmit{4titlyc 4low_tionc 4xyswriptions}
ynx
ynx
Q￿￿￿￿￿￿ ￿￿￿￿￿￿￿￿￿￿￿￿
Ée você já tem algum quarto cadastrado antes dessas alterações\ você
não vai mais conseguir editá]los ou removê]los_ ” jeito é destruir to]
dos os quartos Xfazendo Room.destroy_all no consoleYou atualizar
todos de modo que você seja o dono XRoom.update_all :user_id
=> User.first.idY_
tom essa modi￿cações\ garantimos a segurança dos dados de forma simples e
legível_ rgora vamos melhorar os templates para não exibir os links de remoção e
edição caso o usuário não seja o dono e vamos aproveitar para melhorar o visual em
geral_
￿￿n￿ E￿￿￿￿￿￿￿￿ ￿￿￿￿￿￿￿￿￿￿ ￿￿￿￿￿￿￿
øor enquanto\temos a listagem da seguinte formak
￿￿￿

## Página 207

tasa do tódigo tapítulo ￿￿_ tontrole de acesso
wigura￿￿_￿￿k“istagem de quartos sem nenhum tratamento
zsso ainda pode melhorar_vmbora o sca￿old seja bom para começar e ter uma
ideia do que queremos\o resultado dele sempre precisa ser trabalhado_” objetivo é
tornar a listagem mais elegantek
wigura￿￿_￿￿k“istagem de quartos com estilo
rntes de criar o template\vamos precisar de um helper_vsse helper veri￿]
cará se o usuário está logado e se o quarto pertence a ele_âam o susar ele para exibir
￿￿￿

## Página 208

￿￿_￿_ vxibição e listagem de quartos tasa do tódigo
os links de edição e remoção do modelo apenas aos donos_rbra o RoomsHelper
Xapp/helpers/rooms_helperYe crie o método belongs_to_user como a
seguirk
moxuly +ooms#ylpyr
xyz vylon0sutouusyr{room}
usyrusi0nyxuini \\ room:usyr hh wurryntuusyr
ynx
ynx
vm seguida\ vamos alterar o template da ação index X
app/views/rooms/index.html.erbY\ para apenas exibir os links de edi]
ção e remoção caso o modelo pertença ao usuário logado\ além de outros detalhes
como link para o xoogle –aps e i￿￿nk
>h$-<%= t ':titly' %> >,h$-
<% írooms:y_wh xo |room| %>
>_rtiwly wl_ssh*room*-
>he-<%= linkuto room:titlyc room %> >,he-
>sp_n wl_ssh*wry_tyx*-
<%= t ':ownyruhtml'c
ownyr4 room:usyr:zullun_myc
whyn4 l{room:wry_tyxu_tc zorm_t4 4short} %>
>,sp_n-
>p-
>sp_n wl_ssh*low_tion*-
<%= linkuto room:low_tionc
*https4,,m_ps:0oo0ly:wom,iqh@{room:low_tion}*c
t_r0yt4 4vl_nk %>
>,sp_n-
>,p-
>p-<%= room:xyswription %> >,p-
<% iz vylon0sutouusyr{room} %>
>ul-
>li-<%= linkuto t{':yxit'}c yxituroomup_th{room} %> >,li-
>li-<%= linkuto t{':xystroy'}c roomup_th{room}c
mythox4 4xylytyc x_t_4
{wonzirm4 t{'xi_lo0s:xystroy'}}
%> >,li-
>,ul-
￿￿￿

## Página 209

tasa do tódigo tapítulo ￿￿_ tontrole de acesso
<% ynx %>
>,_rtiwly-
<% ynx %>
•o template anterior temos uma novidadek o uso do l_ ” l\ atalho para
localize\ faz parte do sistema de internacionalização\ mas com um papel dife]
rente_ ” l faz a “tradução” de datas e horário\ usando o formato adequado para
cada idioma_ øor exemplo\ no srasil usamos datas no formato dia\ mês e ano_øo]
rém\ nos vstados ánidos\ o mais comum é usar mês\ dia e ano_ áma vez tendo o
arquivo de suporte do idioma\ o z￿￿n faz essa “tradução” automaticamente_
” localize ainda aceita alguns formatos de data\ tal como :short\ :long
e o padrão X:default\ no é r–“Y_ âo c êpode ainda criar os formatos que quiser\
seguindo o padrão strftime Xpadrãode formatação de hora e data de sistemas
ø”ÉzãY_âe j aos formatos que já vem com o Áailsk
zorm_ts4
xyz_ult4 ~ 'bjc bx xy bk xy b7c b#4bp h'
lon04 ~ 'bjc bx xy bk xy b7c b#4bp h'
short4 ~ 'bx,bmc b#4bp h'
øara saber o que é cada símbolo\você pode consultar a documentação do Áuby
no método strftime\ ou digitar man strftime\ caso você esteja em ”É ã ou
“inux_
Partials de modelos
áma convenção importante do Áails são as partials de modelos_âe j ao exemplo
a seguirk
<%= rynxyr íroom %>
Ée o objeto @room for uma instância do modelo Room\ o Áails irá buscar pela
partial _room.html.erb\e é exatamente o que vamos fazer para deixar o template
mais limpok
>h$-<%= t ':titly' %> >,h$-
<% írooms:y_wh xo |room| %>
<%= rynxyr room %>
<% ynx %>
￿￿￿

## Página 210

￿￿_￿_ vxibição e listagem de quartos tasa do tódigo
rlém disso\ o Áails é capaz de renderizar coleções\ ou seja\ se você passar um
Array ou relacionamentos do ActiveRecord\ por exemplo\ o Áails irá rende]
rizar cada elemento da lista_ tom ambas as alterações\ a listagem de quartos X
app/views/rooms/index.html.erbY￿ca da seguinte maneirak
>h$-<%= t ':titly' %> >,h$-
<%= rynxyr írooms %>
va partial Xapp/views/rooms/_room.html.erbYk
>_rtiwly wl_ssh*room*-
>he-<%= linkuto room:titlyc room %> >,he-
>sp_n wl_ssh*wry_tyx*-
<%= t ':ownyruhtml'c
ownyr4 room:usyr:zullun_myc
whyn4 l{room:wry_tyxu_tc zorm_t4 4short} %>
>,sp_n-
>p-
>sp_n wl_ssh*low_tion*-
<%= linkuto room:low_tionc
*https4,,m_ps:0oo0ly:wom,iqh@{room:low_tion}*c
t_r0yt4 4vl_nk %>
>,sp_n-
>,p-
>p-<%= room:xyswription %> >,p-
<% iz vylon0sutouusyr{room} %>
>ul-
>li-<%= linkuto t{':yxit'}c yxituroomup_th{room} %> >,li-
>li-<%= linkuto t{':xystroy'}c roomup_th{room}c
mythox4 4xylytyc x_t_4
{wonzirm4 t{'xi_lo0s:xystroy'}}
%> >,li-
>,ul-
<% ynx %>
>,_rtiwly-
•ote que na partial fazemos referência ao quarto usando a variável room_zsso
acontece porque\quando usamos render em um objeto\o Áails mapeia o nome do
objeto a ser renderizado pelo nome da partial_Íome cuidado\ pois isso é implícito
e ￿ca difícil de descobrir o que está acontecendo em algumas situações_ Ée você
preferir\podemos ser explícito em qual objeto devemos mapear para a partial
￿￿￿

## Página 211

tasa do tódigo tapítulo ￿￿_ tontrole de acesso
<%= rynxyr p_rti_l4 'room'c ovjywt4 wurryntuusyr:rooms:zirst %>
” nome do objeto na partial ainda será room\ por causa do nome da partial\
mas o objeto que estamos renderizando é o current_user.rooms.first_
øor ￿m\ ainda é possível especi￿car o nome do objeto através do uso do
:localsk
<%= rynxyr p_rti_l4 'room'c low_ls4 {thyuroom4 wurryntuusyr:rooms:zirst} %>
•esse caso\ dentro da partial\ teremos acesso a variável the_room\ contendo
current_user.rooms.first_” locals é útil para casos em que a partial de]
pende de outras variáveis_
rgora vamos trabalhar no tÉÉ_” que temos que fazer é extrair o mixin shadow
do default.css.scss para um arquivo separado para que possamos usar tanto
no default.css.scss quanto no novo tÉÉ_ øara isso\vamos criar um novo tÉÉ
para a função de sombra Xapp/assets/stylesheets/shadow.css.scssYk
ímixin sh_xow{ãwolorc ãxc ãyc ãr_xius} {
çmozçvoxçsh_xow4 ãwolor ãx ãy ãr_xiusg
çwyvkitçvoxçsh_xow4 ãwolor ãx ãy ãr_xiusg
voxçsh_xow4 ãwolor ãx ãy ãr_xiusg
}
uepois de apagar o mixin do default.css.scss\ temos que incluir a função
que acabamos de extrair_wazemosisso com o uso do @importk
íimport *sh_xow*g
ãhy_xyrçhyi0ht4 88pxg
ãwontyntçwixth4 !ddpxg
:::
v para ￿nalizar o tÉÉ\ vamos criar estilo para quartos X
app/assets/stylesheets/room.css.scssYk
íimport *sh_xow*g
:room {
v_wk0rounxçwolor4 whityg
p_xxin04 edpx e8pxg
￿￿￿

## Página 212

￿￿_￿_ vxibição e listagem de quartos tasa do tódigo
m_r0inçtop4 $dpxg
íinwluxy sh_xow{@wwwc dc épxc =px}g
}
:room he {
xispl_y4 inlinyg
_ { zontçsizy4 $:éymg }
}
øronto_r próxima parte é o z￿￿n Xconfig/locales/pt-BR.ymlYk
ptçk+4
@ :::
xi_lo0s4
xystroy4 'rowê tym wyrtyz_ quy quyr rymovyri'
rooms4
inxyx4
titly4 '.u_rtos xisponívyis'
room4
ownyruhtml4 '\mx_shg b{ownyr} {b{whyn}}'
yxit4 'mxit_r'
xystroy4 '+ymovyr'
@ :::
“embre]se que o _html é necessário para que o z￿￿n retorne entidades yÍ–“
Xmdash;Y_
øor ￿m\ a última alteração que precisamos fazer é atualizar o template da ação
show Xapp/views/users/show.html.erbYk
<%= rynxyr íroom %>
øronto\ terminamos as regras de acessoQ•o próximo capítulo\ vamos estudar
como fazer avaliação de quartos\ dando uma pontuação de ￿ a ￿ para um quarto\
usando éJéX e associações um pouco mais complicadas do que vimos até então_
￿￿￿

## Página 213

t ￿￿￿￿￿￿￿ ￿￿
rvalia ção de quartos\
relacionamentos muitos para muitos
e organização do código
Ruby foi construído para tornar os programadores mais felizesp
– é ukihiro “–atz” –atsumoto
r estrutura de dados e templates já está completa_” que vamos fazer nesse ca]
pítulo é possibilitar a avaliação de quartos\ assim usuários do colcho_netpodem ob]
servar as melhores localidades_
ørimeiro\ precisamos criar o modelo de avaliação_ vm seguida\ criaremos os
relacionamentos entre os modelos Usuario ] User e Quarto ] Room\ com vali]
dações_tom esses relacionamentos\vamos criar as ações de controle para alterar e
criar avaliações_
•o frontoend\vamos alterar o template do quarto para incluir as opções de fazer a

## Página 214

tasa do tódigo
avaliação\via r{rã_ øara isso funcionar\vamos criar o controle com ações um pouco
diferentes\para responder requisições r{rã_ ” resultado ￿nal será o seguintek
wigura￿￿_￿kvstrelas para avaliação
øor ￿m\ na listagem de todos os quartos\ vamos aprender a usar as funções de
cálculo Xnessecaso\ média de pontuaçãoYdo Áails e também vamos ver como exe]
cutar consultas É®“ mais complicadas_
￿￿￿

## Página 215

tasa do tódigo tapítulo ￿￿_ rvalia ção de quartos\ relacionamentos muitos para muitos e_ _ _
wigura￿￿_￿krvalia ções na listagem com estrelas
￿￿n￿ R￿￿￿￿￿￿￿￿￿￿￿￿￿￿ ￿￿￿￿￿￿m￿￿￿￿m￿￿￿￿￿￿
áma avaliação é um modelo que pertence a um quarto e um usuário ao mesmo
tempo_zsso signi￿ca que para uma avaliação ser única\ ela depende de duas chaves
estrangeiraskuma para o quarto e outra para o usuário avaliador_
øara ter esse resultado\vamosk
￿Y triar modelo Review com chaves estrangeiras user_id e room_id\ além de
outros camposl
￿Y triar índice para garantir unicidade do par user_id e room_id\ ou seja\ um
usuário não pode avaliar um mesmo quarto mais de uma vezl
￿Y triar validações no novo modelo\como por exemplo\não permitir que o usuário
avalie o seu próprio quartol
￿Y triar o relacionamento no modelo quartol
￿￿￿

## Página 216

￿￿_￿_ Áelacionamentos muitos]para]muitos tasa do tódigo
￿Y triar o relacionamento no modelo usuário_
õriando chaves estrangeiras
âam o susar o gerador para gerar o modelo Review\já com os relacionamentosk
ã r_ils 0 moxyl ryviyw usyr4ryzyrynwys room4ryzyrynwys points4inty0yr
invoky _wtivyuryworx
wry_ty xv,mi0r_ty,ed$éd!$5df$8$5uwry_tyuryviyws:rv
wry_ty _pp,moxyls,ryviyw:rv
invoky tystuunit
wry_ty tyst,unit,ryviywutyst:rv
wry_ty tyst,zixturys,ryviyws:yml
r migração gerada será assimk
wl_ss lry_ty+yviyws > jwtivy+yworx44pi0r_tion
xyz wh_n0y
wry_tyut_vly 4ryviyws xo |t|
t:vylon0suto 4usyrc inxyx4 truy
t:vylon0suto 4roomc inxyx4 truy
t:inty0yr 4points
t:timyst_mps
ynx
ynx
ynx
ørecisamos alterar essa migração\pois vamos tirar os índices individuais em cada
chave estrangeira e vamos colocar o índice no par [user_id, room_id]k
wl_ss lry_ty+yviyws > jwtivy+yworx44pi0r_tion
xyz wh_n0y
wry_tyut_vly 4ryviyws xo |t|
t:vylon0suto 4usyr
t:vylon0suto 4room
t:inty0yr 4points
t:inxyx /4usyruixc 4roomuix3c uniquy4 truy
t:timyst_mps
￿￿￿

## Página 217

tasa do tódigo tapítulo ￿￿_ rvalia ção de quartos\ relacionamentos muitos para muitos e_ _ _
ynx
ynx
ynx
øara efetivar essas alterações no banco de dados\ executamos o comando rake
db:migratek
ã r_ky xv4mi0r_ty
hh lry_ty+yviyws4 mi0r_tin0 hhhhhhhhhhhhhhhhhhhh
çç wry_tyut_vly{4ryviyws}
ç- d:dd5ês
hh lry_ty+yviyws4 mi0r_tyx {d:dd58s} hhhhhhhhhhh
•enhuma novidade até então_” modelo Review Xapp/models/review.rbY
também não tem muitos segredos -- o Áails até já criou o modelo com os
belongs_to necessáriosk
wl_ss +yviyw > jwtivy+yworx44k_sy
vylon0suto 4usyr
vylon0suto 4room
ynx
âam o susar uma funcionalidade do Áails chamada counter cache\ ou seja\ cao
che de contadores_tomo precisaremos calcular o número de avaliações\ o Áails já
guarda esse valor pré]calculado em uma coluna do banco de dados automaticamente\
desde que usemos a opção counter_cache: true no belongs_tok
wl_ss +yviyw > jwtivy+yworx44k_sy
vylon0suto 4usyr
vylon0suto 4roomc wountyruw_why4 truy
ynx
ørecisamos criar uma nova coluna na tabela de quartos de modo a guardar essa
contagemk
ã r_ils 0 mi0r_tion _xxuwountyruw_whyutourooms ryviywsuwount4inty0yr
invoky _wtivyuryworx
wry_ty xv,mi0r_ty,ed$éd!$5df$!8=u_xxuwountyruw_whyutourooms:rv
ã r_ky xv4mi0r_ty
hh jxxlountyrl_why?o+ooms4 mi0r_tin0 hhhhhhhhhhhhh
çç _xxuwolumn{4roomsc 4ryviywsuwountc 4inty0yr}
￿￿￿

## Página 218

￿￿_￿_ Áelacionamentos muitos]para]muitos tasa do tódigo
ç- d:ddéés
hh jxxlountyrl_why?o+ooms4 mi0r_tyx {d:ddéês} hhhh
øorém\ isso não é su￿ciente_ørecisamos colocar algumas validações no modelo
de avaliaçõesk
wl_ss +yviyw > jwtivy+yworx44k_sy
@ lri_mos um jrr_y xy 8 ylymyntosc _o invés xy r_n0y:
%)o(?q h {$::8}:tou_
vylon0suto 4usyr
vylon0suto 4roomc wountyruw_why4 truy
v_lix_tysuuniquynyssuoz 4usyruixc swopy4 4roomuix
v_lix_tysuprysynwyuoz 4pointsc 4usyruixc 4roomuix
v_lix_tysuinwlusionuoz 4pointsc in4 %)o(?q
ynx
vssas validações são bem similares com as que já vimos\ com exceção da opção
scope aplicada à validação uniqueness_ vla limita o escopo em que a veri￿ca]
ção de unicidade ocorre\ ou seja\ neste exemplo\ o user_id pode repetir caso o
room_id seja diferente_
rgora vamos ao modelo Room Xapp/models/room.rbY_•ele vamos criar o
relacionamento um]para]muitoskum quarto possui muitas avaliações_
wl_ss +oom > jwtivy+yworx44k_sy
h_sum_ny 4ryviyws
vylon0suto 4usyr
@:::
ynx
￿￿￿

## Página 219

tasa do tódigo tapítulo ￿￿_ rvalia ção de quartos\ relacionamentos muitos para muitos e_ _ _
R￿￿￿￿￿￿￿￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿ m￿m￿￿￿￿￿
vm relacionamentos muitos]para]muitos\ é comum precisarmos
acessar o modelo da outra ponta da tabela de ligação\ ou seja\ no tol]
cho_net\é interessante um usuário saber todos os quartos que ele tem
algum voto_r ideia é juntar todos os registros de avaliação que o usuário
possui e\ através desses registros\buscar os quartos_
” ActiveRecord te ajuda a resolver esse problema_ áma vez de]
￿nido o relacionamento has_many :reviews\ podemos criar o se]
guinte relacionamentok
wl_ss +oom > jwtivy+yworx44k_sy
@ É nywyssário xyzinir o h_sum_ny primyiro~
h_sum_ny 4ryviyws
h_sum_ny 4ryviywyxuroomsc throu0h4 4ryviywsc sourwy4 4room
@ :::
ynx
vsse exemplo cria o relacionamento reviewed_rooms que\ atra]
vés de todas as avaliações que um usuário tem Xespeci￿cado pela opção
:throughY\irá buscar o relacionamento :room\ retornando todos os
quartos que satisfazem estes relacionamentos_
øor ￿m\ vamos criar o relacionamento no modelo User X
app/models/user.rbY\ para que possamos ter acesso às avaliações daquele
usuáriok
wl_ss "syr > jwtivy+yworx44k_sy
mpjoõu+m9m;% h ,tj/2í3]í{/2ít:3]t:}]/2ít:3]tz,
h_sum_ny 4ryviyws
h_sum_ny 4rooms
@ :::
ynx
ørontoQÍ odos os relacionamentos foram criados_ rntes de continuar\ veja o
￿￿￿

## Página 220

￿￿_￿_ Áemovendo objetos sem deixar rastros tasa do tódigo
exemplo a seguirk
@ õymvryçsy xo s_nxvox p_r_ yvit_r _ pyrx_ xy x_xos~
@ %_r_ us_r o s_nxvoxc v_st_ z_zyr *r_ils w ççs_nxvox*
room h +oom:l_st
@ h- @>+oom ix4 8c ::: -
ryviyw h room:ryviyws:vuilx points4 é
ryviyw:usyr h "syr:l_st
ryviyw:s_vy
@ h- @>+yviyw ix4 $c ::: -
+yviyw:_ll
@ h- /@>+yviyw ix4 $c ::: -3
room:xystroy
@ h- @>+oom ix4 8c -
r h +yviyw:zirst
@ h- @>+yviyw ix4 $c -
r:room
@ h- nil
” que acontece é que removemos o objeto room\ porém ainda temos referên]
cias inválidas no banco de dados_øara arrumar isso\ poderíamos criar um callback
no momento que um objeto está sendo destruído Xafter_deleteYe remover os
objetos referenciados_ vssa solução funciona\ porém\ o ActiveRecord facilita a
nossa vida_
￿￿n￿ R￿￿￿￿￿￿￿￿ ￿￿￿￿￿￿￿￿￿￿ ￿￿￿￿￿￿ ￿￿￿￿￿￿￿
•o momento que vamos destruir um objeto\é possível destruir também objetos rela]
cionados_øara isso\adicionamos uma opção nas associações que queremos remover
quando o objeto for destruído\chamada dependent_Éeu comportamento é muito
parecido com a opção CASCADE do É®“k
• destroy ] vxecuta #destroy em todos os objetos associados\ executando
os callbacks de cada uml
￿￿￿

## Página 221

tasa do tódigo tapítulo ￿￿_ rvalia ção de quartos\ relacionamentos muitos para muitos e_ _ _
• delete_all ] ueleta os objetos associados via É®“ apenas\sem execução de
callbacksl
• nullify ] rpenas marca as chaves estrangeiras dos objetos relacionados com
NULLl
• restrict ] zmpede a remoção do objeto se houver objetos relacionados_
•esse caso\ queremos usar a opção :destroy\ para que os callbacks sejam de
fato chamados\precisamos destruir todas as avaliações associadas ao usuário quando
ele é destruído_øara isso\ basta colocar uma opção no has_many_âe j acomo deve
￿car o modelo User Xapp/models/user.rbYk
wl_ss "syr > jwtivy+yworx44k_sy
mpjoõu+m9m;% h ,tj/2í3]í{/2ít:3]t:}]/2ít:3]tz,
@ jprovyity _ oportunix_xy p_r_ _tu_liz_r o outro
@ ryl_wion_mynto4
h_sum_ny 4roomsc xypynxynt4 4xystroy
h_sum_ny 4ryviywsc xypynxynt4 4xystroy
@ :::
ynx
v\ por ￿m\ no modelo Room Xapp/models/room.rbYk
wl_ss +oom > jwtivy+yworx44k_sy
h_sum_ny 4ryviywsc xypynxynt4 4xystroy
vylon0suto 4usyr
@ :::
ynx
￿￿￿

## Página 222

￿￿_￿_ Áemovendo objetos sem deixar rastros tasa do tódigo
D￿￿￿￿￿￿￿￿￿￿￿￿￿ #DESTROY ￿ #DELETE
” ActiveRecord possui dois métodos para destruir objetos no
banco de dadosko #destroy eo #delete_É muito importante lem]
brar que eles possuem comportamentos diferentes_
” #destroy é o método que normalmente deve ser usado_vle exe]
cuta todos os callbacks e deleta o objeto no banco de dados_” #delete\
por sua vez\ apenas executa o DELETE no banco de dados_zsso signi￿ca
que nenhum callback e nenhum dependent: destroy serão execu]
tados_
õ ￿￿￿￿￿￿ ￿￿￿ ￿ DEPENDENT : :DESTROY
rpesar da grande conveniência\ o dependent: :destroy pode
ser perigoso_tomo o ActiveRecord tem que instanciar cada objeto e
chamar o método #destroy\ que por sua vez\ pode ter seus relaciona]
mentos\ que vai instanciar todos os objetos\ e___ueu pra entender onde
isso vai parar\nép
rlém de lento\ esse procedimento pode ser perigoso_ Ée o seu
banco de dados tiver muitos registros\ o Áails irá instanciar um objeto
ActiveRecord para cada linha\ resultando em muita alocação de me]
mória e muitas interrupções do garbage collector para limpar objetos não
usados_øior\seu sistema pode entrar em swap e parar de responder_
vm situações assim\ você pode considerar uma das seguintes solu]
çõesk
• –arcar os objetos a serem removidos por um serviço que executa
de tempos em temposl
• ásar dependent: delete e usar chaves estrangeiras com on
delete cascade\ no próprio banco\ fazendo com que o banco
de dados ￿que responsável pela limpeza dos dados_
￿￿￿

## Página 223

tasa do tódigo tapítulo ￿￿_ rvalia ção de quartos\ relacionamentos muitos para muitos e_ _ _
￿￿n￿ õ ￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿￿￿￿ ￿￿￿￿￿￿￿￿￿ íJíX
øronto\ agora que temos o modelo de avaliação\ vamos implementar o frontoend\
usar uma nova fonte e incluir o {avaÉcripte chamadas r{rã_
øara isso\ primeiro vamos criar o ponto de entrada para o recurso
Review_ tomo um Room possui muitos reviews\ vamos montar a áÁ“
de modo a representar esse relacionamento_ r áÁ“ ￿cará da seguinte formak
/rooms/:room_id/reviews_ zsso dará ao nosso projeto uma noção de que um
quarto possui pelo menos uma avaliação_
” Áails representa essas rotas através do aninhamento de resources_ âe j a
como ￿cará a rota para reviewsk
lolwhonyt44jppliw_tion:routys:xr_w xo
@:::
rysourwys 4rooms xo
rysourwys 4ryviywsc only4 /4wry_tyc 4upx_ty3
ynx
@ :::
ynx
â ejamos o resultado executando rake routesk
roomuryviyws %)q? {,4low_ly},rooms,4roomuix,ryviyws{:4zorm_t}
ryviyws@wry_ty
{4low_lyh-,yn|pttçk+,}
roomuryviyw %"? {,4low_ly},rooms,4roomuix,ryviyws,4ix{:4zorm_t}
rooms,ryviyws@upx_ty
{4low_lyh-,yn|pttçk+,}
Éeguindo a convenção\ o Áails tentará carregar o controle como
ReviewsController em app/controllers/reviews_controller.rb_
øorém\ depois de alguns meses ou anos de projetos\ deixar todos os controles
nessa pasta ￿ca uma bagunça sem tamanho_ zmagine uma pasta com mais de ￿￿￿
controles\cada um em uma rota diferente_
øor essa razão\organizaremos controles que possuem aninhamento em módulos
distintos_rs principais vantagens dessa prática sãokextrair comportamento comum\
￿￿￿

## Página 224

￿￿_￿_ triando avaliações com pitadas de r{rã tasa do tódigo
como buscar o elemento a qual o recurso pertence Xporexemplo\ buscar o objeto
room no controle de avaliaçõesYou ￿ltros\ e a organização dos arquivos_
øara modularizar componentes\o Áails requer que você crie uma subpasta com
o nome do módulo e então ele será automaticamente de￿nido para você_ rpli]
cando a este caso\ queremos criar o módulo rooms_ øara isso\ basta criar a pasta
app/controllers/rooms_vm seguida\ todo controle dentro dessa pasta deverá
ser de￿nido de acordo com o módulo_øara o caso do controle reviews\ devemos
criar o arquivo app/controllers/rooms/reviews_controllers.rb_•esse
arquivo\a classe a ser de￿nida será Rooms::ReviewsController_rs rotas\ po]
rém\ necessitam de alterações para poder reconhecer o módulo_
âam o s alterar a rota que criamos de forma que o Áails busque o con]
trole na pasta app/controllers/rooms/ e a classe do controle seja
Rooms::ReviewsController_øara isso\basta de￿nir a opção modulek
lolwhonyt44jppliw_tion:routys:xr_w xo
@:::
rysourwys 4rooms xo
rysourwys 4ryviywsc only4 /4wry_tyc 4upx_ty3c moxuly4 4rooms
ynx
@ :::
ynx
” que precisamos fazer no controle de reviews é criar uma nova entrada no
banco de dados quando um usuário ￿zer uma nova avaliação_ørecisamos também
garantir que\quando o usuário faça uma nova avaliação\apenas atualizaremos a en]
trada já existente_ É possível fazê]lo com o que já vimos até agora\ mas é possível
realizar essa operação de forma que o código ￿que bem mais limpo_
rs o l ução mais natural é fazer uma busca e\se o objeto não existir\criar um novo_
vm seguida\ atualizamos o objeto para ter o novo valor_É possível fazer isso de uma
só vez\ usando o método find_or_initialize_by_ vsse método fará exata]
mente o que precisamoskbuscará o objeto e\ se não existir\ criará um novo objeto
com o valor preenchido_tom este objeto\podemos preencher os outros atributos e
salvá]lo no banco de dados_•ote que esse método não salva o modelo no banco de
dados_øara tal\ você pode usar o find_or_create_by_
ra ção create ￿cará da seguinte formakfaremos a busca em todas as avaliações
do quarto especi￿cado a partir do usuário logado Xcurrent_userY_vm seguida\
￿￿￿

## Página 225

tasa do tódigo tapítulo ￿￿_ rvalia ção de quartos\ relacionamentos muitos para muitos e_ _ _
preencheremos o restante dos atributos vindos do formulário_
Xapp/controllers/rooms/reviews_controller.rbY_
wl_ss +ooms44+yviywslontrollyr > jppliw_tionlontrollyr
vyzoryuziltyr 4ryquiryu_uthyntiw_tion
xyz wry_ty
ryviyw h room:ryviyws:
zinxuoruiniti_lizyuvy{usyruix4 wurryntuusyr:ix}
ryviyw:upx_ty~{ryviywup_r_ms}
hy_x 4ok
ynx
xyz upx_ty
wry_ty
ynx
priv_ty
xyz room
íroom ||h +oom:zinx{p_r_ms/4roomuix3}
ynx
xyz ryviywup_r_ms
p_r_ms:
ryquiry{4ryviyw}:pyrmit{4points}
ynx
ynx
M￿￿￿￿￿￿ ￿￿￿￿￿￿￿￿￿ ￿￿ R￿￿￿￿￿
r maioria dos dynamic finders se tornaram obsoletos no Áails ￿_
øor exemplo\não será mais possível chamar o método find_by_email
no modelo User\como vimos anteriormente_” mesmo vale para os mé]
todos %find_or_create_by... e find_or_initialize_by..._
￿￿￿

## Página 226

￿￿_￿_ triando avaliações com pitadas de r{rã tasa do tódigo
tomo vamos responder apenas a requisições r{rã\ não precisamos renderi]
zar nenhum conteúdo_ øortanto\ apenas respondemos com o código yÍÍø 201
Created quando há sucesso\ por isso usamos o método head_ vsse método re]
torna o cabeçalho yÍÍø contendo o código de resposta Xnocaso\￿￿￿Ye como corpo\
apenas um espaço em branco_
õ ￿￿￿￿￿￿￿￿￿￿z ￿￿￿￿￿￿ ￿￿￿￿ ￿ ￿ ￿￿￿￿￿￿￿￿￿￿ ￿￿￿￿￿￿ ￿￿
￿￿￿￿￿￿
” método head não precisaria emitir um espaço em branco_øorém\
versões antigas do znternetvxplorer ignoram a resposta do servidor caso
o corpo esteja vazio_
uependendo da biblioteca {avaÉcript que você usa\ isso pode trazer
um problema_ sibliotecas que fazem r{rã podem tentar fazer a inter]
pretação do resultado como se fosse objetos {É”•\ resultando em falhas
no script e interrompendo a execução_
•esse caso\como o único input do usuário é um valor pré]selecionado\não deve]
mos encontrar erros_Ée por um acaso encontrarmos\há algum problema em nosso
projeto e portanto usamos o método bang no #update!\ de forma a disparar exce]
ções e\ portanto\facilitar a depuração_
” comportamento do update deverá ser o mesmo do create\ portanto
apenas chamamos o método_ r única diferença é que objeto será encontrado no
find_or_initialize_by_
F￿￿￿￿ ￿￿￿￿￿￿￿￿￿￿￿￿n￿￿￿￿￿ “￿￿￿￿￿￿￿￿￿￿ ”
®uando desenvolvemos aplicações\ temos a tendência de tentar tra]
tar ou silenciar erros\ evitando que usuários sejam apresentados a uma
página de erro_
øorém\ é importante salientar que\ quando fazemos isso\ ￿ca mais
difícil descobrir que algo está errado e tentar caçar algum bug misterioso_
®uando algo inesperado acontece\ é melhor ver um stack trace do que
tentar adivinhar\ fazendo debug por horas para descobrir porque uma
variável está nil\ por exemplo_
￿￿￿

## Página 227

tasa do tódigo tapítulo ￿￿_ rvalia ção de quartos\ relacionamentos muitos para muitos e_ _ _
D￿￿￿zR￿￿￿￿ ￿￿ ￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿￿
•ão precisamos criar abstrações no nosso exemplo_øorém\na neces]
sidade de compartilhar código entre vários controles em um mesmo mó]
dulo\ podemos criar uma classe chamada Rooms::BaseController
e nela colocar ￿ltros e outros métodos auxiliaresk
wl_ss +ooms44k_sylontrollyr > jppliw_tionlontrollyr
vyzoryuziltyr 4ryquiryu_uthyntiw_tion
priv_ty
xyz room
íroom ||h +oom:zinx{p_r_ms/4ix3}
ynx
ynx
vm seguida\ basta herdar desse controle e o comportamento será
compartilhadok
wl_ss +ooms44+yviywslontrollyr > +ooms44k_sylontrollyr
xyz wry_ty
ryviyw h room:ryviyws:
zinxuoruiniti_lizyuvy{usyruix4 wurryntuusyr:ix}
@ :::
ynx
ynx
øor ￿m\ vamos acertar o controle RoomsController X
app/controllers/rooms_controller.rbY para construir um objeto de
avaliação a ser usado no template_waremosisso para que os helpers de formulário
do Áails já popule os campo user_id apropriadamente_
wl_ss +oomslontrollyr > jppliw_tionlontrollyr
@ :::
xyz show
íroom h +oom:zinx{p_r_ms/4ix3}
￿￿￿

## Página 228

￿￿_￿_ triando avaliações com pitadas de r{rã tasa do tódigo
iz usyrusi0nyxuini
íusyruryviyw h íroom:ryviyws:
zinxuoruiniti_lizyuvy{usyruix4 wurryntuusyr:ix}
ynx
ynx
@:::
ynx
tontroles prontos\ vamos aos templates_âam o scolocar as tradicionais estrelas
de avaliação\ mas a priori focaremos na funcionalidade_ âam o susar radio buttons
para que o usuário escolha a pontuação\de ￿a ￿k
wigura￿￿_￿krvalia ção de quartos com radio buttons
øara fazer isso\ vamos criar um formulário na partial de quartos X
app/views/rooms/_room.html.erbYk
>_rtiwly wl_ssh*room*-
>he-<%= linkuto room:titlyc room %> >,he-
<%= rynxyr p_rti_l4 'ryviyw'c ovjywt4 íusyruryviyw %>
>sp_n wl_ssh*wry_tyx*-
<%= t ':ownyruhtml'c
ownyr4 room:usyr:zullun_myc
whyn4 l{room:wry_tyxu_tc zorm_t4 4short} %>
>,sp_n-
￿￿￿

## Página 229

tasa do tódigo tapítulo ￿￿_ rvalia ção de quartos\ relacionamentos muitos para muitos e_ _ _
:::
>,_rtiwly-
triemos a partial review Xapp/views/rooms/_review.html.erbY_•ela\
precisamos criar um formulário contendo os radio buttons\ caso o usuário esteja lo]
gado_taso contrário\ exibimos uma mensagem dizendo que essa operação só está
disponível para usuários já autenticadosk
>sywtion wl_ssh*ryviyw*-
<% iz usyrusi0nyxuini %>
<%= zormuzor /ryviyw:roomc ryviyw3 xo |z| %>
<% +yviyw44%)o(?q:y_wh xo |point| %>
<%= z:r_xiouvutton 4pointsc point %>
<%= z:l_vyl 4pointsc pointc v_luy4 point %>
<% ynx %>
<%= z:suvmit %>
<% ynx %>
<% ylsy %>
>sp_n wl_ssh*lo0inuryquiryx*-
<%= t{':lo0inutouryviyw'} %>
>,sp_n-
<% ynx %>
>,sywtion-
r primeira notável diferença é a construção da rota para o form_for_ tomo
o recurso “avaliação” é aninhado ao recurso “quarto”\é necessário identi￿car a qual
quarto pertence a nova avaliação que criamos no controle de quartos Xlembre]sede
como as rotas foram criadasY_ásando a notação de rrray\ dizemos ao Áails todas as
dependências da rota_
•ote que isso causa um problema com a listagem de quartos Xação indexY_r
razão é que a listagem usa a mesma partial de quartos\ porém não possui a revisão
pré construída_âam o sdeixar esse problema de lado por enquanto até concluirmos
a exibição de quartos_
￿￿￿

## Página 230

￿￿_￿_ triando avaliações com pitadas de r{rã tasa do tódigo
R￿￿￿￿ ￿￿￿ ￿￿￿￿￿￿￿￿￿￿
É possível criar rotas com namespaces\ ou seja\ um nome que na ver]
dade não representa um recurso\mas que divide a aplicação em “módu]
los” _øor exemplo\uma área de administração Xou“admin”Ypode ser um
namespace_øara declará]los nas rotas\ basta fazerk
n_mysp_wy 4_xmin xo
rysourwys 4proxuwts
ynx
øara você identi￿car namespaces nos formulários\você deve também
usar a notação de rrrayk
<%= zormuzor /4_xminc íproxuwt3 xo |z| %>
:::
®uando criamos formulários em yÍ–“\ os campos de label possuem um atri]
buto chamado for\ que deve possuir o name ou id do elemento à que este label
se associa_wazendoisso\ clicar no texto do label irá selecionar o campo de texto\ se
associado com um campo de texto\ selecionar um elemento de um grupo de radio
buttons e assim por diante_
øara tornar radio buttons em um mesmo grupo Xouseja\ selecionando um irá
desmarcar o outroY\é necessário usar um mesmo name_ zsso quebra com a forma
de que o label funciona\ ou seja\ todos os labels de um mesmo grupo\ se usando
os helpers do Áails\iriam apontar para um mesmo botão\ deixando de funcionar da
maneira esperada_
É aí que entra a opção :value do helper label_ âo c êdeve usar essa opção
tanto para labels em elementos do tipo radio button ou check boxes_ ” helper irá
construir o atributo for apontando para o elemento correto_
øor ￿m\adicione as seguintes regras tÉÉ para os botões alinharem da forma cor]
reta e estilizar o texto de login Xapp/assets/stylesheets/room.css.scssYk
,, "s_mos o @wontynt p_r_ _umynt_r _ yspywiziwix_xy xo sylytorc
,, ou syj_c torn_r yss_ ry0r_ m_is import_nty quy outr_s:
@wontynt :ryviyw zorm {
m_r0in4 dg
￿￿￿

## Página 231

tasa do tódigo tapítulo ￿￿_ rvalia ção de quartos\ relacionamentos muitos para muitos e_ _ _
}
@wontynt :ryviyw {
m_r0in4 dg
p_xxin04 dg
zlo_t4 ri0htg
vorxyr4 nonyg
}
:ryviyw l_vyl {
xispl_y4 inlinyg
}
:ryviyw :lo0inuryquiryx {
zontçsizy4 d:fymg
wolor4 @===g
zontçv_ri_nt4 sm_llçw_psg
}
wigura￿￿_￿kÍ exto de login necessário
Íraduzimos o modelo Reviewk
ptçk+4
@ :::
_wtivyryworx4
moxyls4
room4 .u_rto
usyr4 "suário
ryviyw4 jv_li_ção
￿￿￿

## Página 232

￿￿_￿_ uiga adeus a regras complexas de apresentaçãokuse presenters tasa do tódigo
v traduzimos a mensagem de logink
ptçk+4
:::
rooms4
inxyx4
titly4 '.u_rtos xisponívyis'
room4
ownyruhtml4 '\mx_shg b{ownyr} {b{whyn}}'
yxit4 'mxit_r'
xystroy4 '+ymovyr'
ryviyw4
lo0inutouryviyw4 n_ç_ o lo0in p_r_ _v_li_r qu_rtos
￿￿n￿ D￿￿￿ ￿￿￿￿￿ ￿ ￿￿￿￿￿￿ ￿￿￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿￿m
￿￿￿ z￿￿￿ ￿￿￿￿￿￿￿￿￿￿
Íe m algo que muito me incomoda nesse código\para ser sincero_Í emos uma regra
de template repetida tanto no RoomsController quanto no template_
•o RoomsControllerk
iz usyrusi0nyxuini
íusyruryviyw h íroom:ryviyws:
zinxuoruiniti_lizyuvy{usyruix4 wurryntuusyr:ix}
ynx
vn o templatek
<% iz usyrusi0nyxuini %>
<%= zormuzor /ryviyw:roomc ryviyw3 xo |z| %>
<%# ::: %>
<% ylsy %>
<%# ::: %>
<% ynx %>
øara resolver esse problema\ vamos criar uma classe que vamos usar tanto nos
templates quanto no controle_”s presenters\ou apresentadores\são responsáveis por
fazer essa ligação\resolvendo o problema de templates ou controles complexos_
âam o s criar então o RoomPresenter_ trie o arquivo e a pasta
app/presenters/room_presenter.rb_
￿￿￿

## Página 233

tasa do tódigo tapítulo ￿￿_ rvalia ção de quartos\ relacionamentos muitos para muitos e_ _ _
r ideia dessa classe é a seguintekpodemos passar um quarto a qual a avaliação irá
pertencer e o contexto que o presenter se aplicakpode ser tanto um template quanto o
próprio controle_ørecisamos deste contexto para saber se o usuário está logado\por
exemplo_”utras informações são usadas pelo Áails para renderizar links de modelos
Xto_param e model_nameY\e o restante servirá para simpli￿car o template_
wl_ss +oom%rysyntyr
xyly0_ty 4usyrc 4wry_tyxu_tc 4xyswriptionc 4low_tionc 4titlyc
4toup_r_mc to4 4íroom
xyz sylz:moxylun_my
+oom:moxylun_my
ynx
xyz initi_lizy{roomc wontyxtc showuzormhtruy}
íwontyxt h wontyxt
íroom h room
íshowuzorm h showuzorm
ynx
xyz w_nuryviywi
íwontyxt:usyrusi0nyxuini
ynx
xyz showuzormi
íshowuzorm
ynx
xyz ryviyw
íryviyw ||h íroom:ryviyws:
zinxuoruiniti_lizyuvy{usyruix4 íwontyxt:wurryntuusyr:ix}
ynx
xyz ryviywurouty
/íroomc ryviyw3
ynx
xyz routy
íroom
ynx
￿￿￿

## Página 234

￿￿_￿_ uiga adeus a regras complexas de apresentaçãokuse presenters tasa do tódigo
xyz ryviywupoints
+yviyw44%)o(?q
ynx
@ n_z wom quy _ p_rti_l 'room' syj_ rynxyriz_x_ qu_nxo wh_m_mos o 'rynxyr'
@ wom o ovjyto x_ wl_ssy room prysyntyr:
xyz toup_rti_lup_th
'room'
ynx
ynx
rs ações show e index do controle RoomsController X
app/controllers/rooms_controllerY￿cam da seguinte formak
wl_ss +oomslontrollyr > jppliw_tionlontrollyr
@ :::
xyz inxyx
@ ) métoxo @m_pc xy wolyçõysc rytorn_rá um novo jrr_y
@ wontynxo o rysult_xo xo vlowo: <yss_ zorm_c p_r_ w_x_
@ qu_rtoc rytorn_rymos o prysyntyr yquiv_lynty:
írooms h +oom:mosturywynt:m_p xo |room|
@ (ão yxivirymos o zormulário n_ list_0ym
+oom%rysyntyr:nyw{roomc sylzc z_lsy}
ynx
ynx
xyz show
roomumoxyl h +oom:zinx{p_r_ms/4ix3}
íroom h +oom%rysyntyr:nyw{roomumoxylc sylz}
ynx
ynx
r partial room Xapp/views/rooms/_room.html.erbY\por sua vez\ ￿cak
>_rtiwly wl_ssh*room*-
>he-<%= linkuto room:titlyc room:routy %> >,he-
<%= rynxyr p_rti_l4 'ryviyw'c low_ls4 {room4 room} %>
>sp_n wl_ssh*wry_tyx*-
￿￿￿

## Página 235

tasa do tódigo tapítulo ￿￿_ rvalia ção de quartos\ relacionamentos muitos para muitos e_ _ _
<%# ::: ã-
>b iz vylon0sutouusyr{room} b-
>ul-
>li-<%= linkuto t{':yxit'}c yxituroomup_th{room:routy} %> >,li-
>li-<%= linkuto t{':xystroy'}c roomup_th{room:routy}c
mythox4 4xylytyc
x_t_4 {wonzirm4 t{'xi_lo0s:xystroy'}} %>
>,li-
>,ul-
<% ynx %>
>,_rtiwly-
øor ￿m\ vamos extrair o formulário de review X
app/views/rooms/_review.html.erbY\em uma nova partial\ review_form
Xapp/views/rooms/_review_form.html.erbY_
r partial app/views/rooms/_review.html.erb ￿cará assimk
>sywtion wl_ssh*ryviyw*-
<% iz room:showuzormi %>
<%= rynxyr p_rti_l4 'ryviywuzorm'c low_ls4 {room4 room} %>
<% ynx %>
>,sywtion-
v a partial app/views/rooms/_review_form.html.erb ￿cará como a se]
guirk
<% iz room:w_nuryviywi %>
<%= zormuzor room:ryviywurouty xo |z| %>
<% room:ryviywupoints:y_wh xo |point| %>
<%= z:r_xiouvutton 4pointsc point %>
<%= z:l_vyl 4pointsc pointc v_luy4 point %>
<% ynx %>
<%= z:suvmit %>
<% ynx %>
<% ylsy %>
>sp_n wl_ssh*lo0inuryquiryx*-
<%= t{':lo0inutouryviyw'} %>
>,sp_n-
<% ynx %>
vsse trabalho com as partials facilitará o nosso trabalho toda vez que quisermos
reusar a revisão de quartos_
￿￿￿

## Página 236

￿￿_￿_ j®uery e Áailskfazer requisições r{rã ￿cou muito fácil tasa do tódigo
￿￿n￿ ￿Q￿￿￿￿ ￿ R￿￿￿￿z ￿￿￿￿￿ ￿￿￿￿￿￿￿￿￿￿￿íJíX ￿￿￿￿￿
￿￿￿￿￿ ￿￿￿￿￿
” código que temos atualmente cria avaliações\ porém clicar no botão ‘triar rvali]
ação’ irá nos exibir uma página em branco_r ação foi projetada para que façamos a
requisição via r{rã\ e é isso que vamos fazer agora_
âo c êdeve estar pensandok“bom\ vamos primeiro instalar nosso framework {a]
vascript preferido XZahamZj®ueryY e usá]lo para facilitar nossa vida” _tertíssimoQ
rtualmente é difícil o site que use {avaÉcripte não possua o j®uery\ para o bem ou
para o mal_
” Áails\ como um framework que quer te ajudar a colocar o seu site no ar\ já
instala o j®uery Xhttpk‘‘jquery_com‘Yem sua aplicação_v mais ainda\ o Áails ainda
integra o j®uery em muito dos helpers\ incluindo formulários via r{rã_
øortanto\ para fazer nosso formulário usar r{rã e enviar as requisições assin]
cronamente\basta alterar uma linha_
rltere o form_for na partial do formulário de review X
app/views/rooms/_review_form.html.erbYpara incluir a opção remote:
truek
<% iz room:w_nuryviywi %>
<%= zormuzor room:ryviywuroutyc rymoty4 truy xo |z| %>
<%# ::: %>
<% ynx %>
<% ylsy %>
<%# ::: %>
<% ynx %>
ørontoQro usar o remote: true\ o Áails criará um atributo data chamado
data-remote_r partir daí\um script chamado “ánobtrusive scripting adapter” \ou
adaptador para script não]intrusivo\ irá observar o evento submit do formulário\
capturá]lo e enviar todos os dados via r{rã\ ao invés da forma tradicional_
vsse adaptador está intimamente ligado ao j®uery\ mas existem outras imple]
mentações dele\ fazendo essa ligação a outros frameworks\ como o prototype_js
Xhttpk‘‘prototypejs_org‘Y_
Ée você ainda desejar usar outro framework de sua preferência\não é difícil criar
o seu próprio\basta remover a entrada gem 'jquery-rails' do Gemfile\ que
é quem habilita o j®uery no projeto_
￿￿￿

## Página 237

tasa do tódigo tapítulo ￿￿_ rvalia ção de quartos\ relacionamentos muitos para muitos e_ _ _
” adaptador também disponibiliza alguns eventos para que possamos regis]
trar callbacks e fazer alguma customização de comportamento_ âam o s usar es]
ses eventos para travar o botão do formulário durante o envio da requisição X
ajax:beforeSendYe sinalizar sucesso Xajax:successYou erro Xajax:errorY
ao usuário_r lista completa de eventos ék
• ajax:before ] rntes de preparar a requisição r{rã Xouseja\ antes de cap]
turar os campos do formulário e preparar as opções de envio da requisiçãoYl
• ajax:beforeSend ] thamado antes de enviar a requisição\porém com tudo
já pronto para enviol
• ajax:success ] uepois do término da requisição e a resposta foi bem suce]
didal
• ajax:error ] uepois do término da requisição e a resposta foi mal sucedidal
• ajax:complete ] thamado depois do término da requisição\ não impor]
tando o resultado_
D￿￿￿￿￿￿￿￿￿￿￿￿ J￿￿￿S￿￿￿￿￿￿￿￿￿￿￿￿￿￿￿￿
Ée você preferir\é possível não usar o adaptador do Áails e fazer tudo
“na mão” _” que temos\ por ￿m\ é a própria biblioteca j®uery\ então
podemos usá]la da forma que quisermos_
øor ￿m\ se você quiser\pode usar to ￿eeÉcript\bastando adicionar a
extensão .coffee e escrever o código equivalente_ásaremos {avaÉcript
no livro_
trie o arquivo app/assets/javascripts/room.js_•ele\ criaremos callo
backs para três eventosk ajax:beforeSend Xenão ajax:beforeY\ajax:error
e ajax:success_ •o evento ajax:beforeSend\ desativamos todos os inputs\
pois eles não serão mais operacionais Xnãopodemos votar mais de uma vezY_Ée tudo
der certo\ substituímos o botão por um ícone de sucesso X“v”Ye se der errado\ por
um “xRk
ã{zunwtion{} {
v_r ãryviyw h ã{':ryviyw'}g
￿￿￿

## Página 238

￿￿_￿_ –édia de avaliações usando agregações tasa do tódigo
ãryviyw:on{'_j_x4vyzoryqynx'c zunwtion{} {
ã{this}:zinx{'input'}:_ttr{'xis_vlyx'c truy}g
}}g
ãryviyw:on{'_j_x4yrror'c zunwtion{} {
rypl_wykutton{thisc 'iwonçrymovy'c '@k5êjêf'}g
}}g
ãryviyw:on{'_j_x4suwwyss'c zunwtion{} {
rypl_wykutton{thisc 'iwonçok'c '@ê=ffê!'}g
}}g
zunwtion rypl_wykutton{wont_inyrc iwonuwl_ssc wolor} {
ã{wont_inyr}:zinx{'input4suvmit'}:
rypl_wysith{ã{'>i,-'}:
_xxll_ss{iwonuwl_ss}:
wss{'wolor'c wolor}}g
}g
}}g
￿￿n￿ M￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿￿￿￿￿￿￿ ￿￿￿￿￿￿￿￿￿￿
vstamos quase terminando a funcionalidade de avaliações_r última coisa que vamos
fazer antes das mudanças visuais é exibir a nota média de avaliações do quarto_
øara isso\ criaremos um método no modelo de avaliações para retornar o valor
da média de pontos\usando uma função de cálculo do ActiveRecord_rs funções
de cálculo sãok
• average ] médial
• minimum ] mínimol
• maximum ] máximol
• count ] contageml
• sum ] soma_
•esses métodos\você deverá passar o nome do campo cujos valores serão calcu]
lados_ øoderá passar também algumas opções de con￿guração_âe j aalguns exem]
plosk
￿￿￿

## Página 239

tasa do tódigo tapítulo ￿￿_ rvalia ção de quartos\ relacionamentos muitos para muitos e_ _ _
+yviyw:_vyr_0y{'points'}
@ qmõml? jr9{*ryviyws*:*points*} jq _v0uix n+)p *ryviyws*
@ h- @>ki0<ywim_l4!zfvéêvxfyxfc'd:e$m$'c$f{ê8}-
+yviyw:_vyr_0y{'points'}:touz
@ h- e:$
@ nunwion_ wom yswopos~
+oom:zirst:ryviyws:_vyr_0y{'points'}:touz
@ qmõml? jr9{*ryviyws*:*points*} jq _v0uix
@ n+)p *ryviyws* s#m+m *ryviyws*:*roomuix* h ê
@
@ h- e:e8
+yviyw:_vyr_0y{4pointsc 0roup4 4room}
@ qmõml? jr9{*ryviyws*:*points*} jq _vyr_0yupointsc
@ roomuix jq roomuix n+)p *ryviyws* 9+)"% k7 roomuix
@
@ h- {@>+oom ix4 êc :::-h-@>ki0<ywim_l4!zfvéê5_vé$fc'd:ee8m$'c$f{ê8}-c
@ @>+oom ix4 8c :::-h-@>ki0<ywim_l4!zfvéê5__!vdc'd:em$'c5{ê8}-}
+yviyw:m_ximum{4points}
@ qmõml? pj;{*ryviyws*:*points*} jq m_xuix n+)p *ryviyws*
@ h- 8
+yviyw:minimum{4points}
@ qmõml? po({*ryviyws*:*points*} jq minuix n+)p *ryviyws*
@ h- $
+yviyw:wount
@ qmõml? l)"(?{[} n+)p *ryviyws*
@ h- $d
r principal vantagem desses métodos de cálculo é que\como você pôde observar\
eles são todos feitos via É®“ e portanto serão bene￿ciados pelos índices do banco de
dados e não há o custo de alocar um objeto na memória para cada registro_
ásando o método .average do ActiveRecord\ calcularemos a média de es]
trelas a partir de uma coleção de avaliações_ásando o método #round de números\
arrendondamos as estrelas para um número inteiro_{untando esses dois métodos\
vamos criar um método de classe no modelo Review Xapp/models/review.rbY
￿￿￿

## Página 240

￿￿_￿_ –édia de avaliações usando agregações tasa do tódigo
-- também aplicáveis a escopos_
wl_ss +yviyw > jwtivy+yworx44k_sy
@ :::
xyz sylz:st_rs
{_vyr_0y{4points} || d}:rounx
ynx
ynx
âe j aexemplos de usok
+oom:zirst:ryviyws:st_rs
@ h- e
+yviyw:st_rs
@ h- e
âam o s então usar esse método no presenter para quartos X
app/presenters/room_presenter.rbY\ criando os métodos #stars e
total_reviewsk
wl_ss +oom%rysyntyr
@ :::
xyz ryviywupoints
+yviyw44%)o(?q
ynx
xyz st_rs
íroom:ryviyws:st_rs
ynx
xyz tot_luryviyws
íroom:ryviyws:sizy
ynx
@ :::
ynx
￿￿￿

## Página 241

tasa do tódigo tapítulo ￿￿_ rvalia ção de quartos\ relacionamentos muitos para muitos e_ _ _
D￿￿￿z￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿
tomo escopos se comportam como rrrays\ eles podem causar pro]
blemas sem mesmo perceber_rrrays possuem três métodos que contam
o número de objetosk #length\ #count e #size_Í odos eles funcio]
nam da mesma maneira_
øorém\isso não se re￿ete em escopos e modelos ActiveRecord_” s
três métodos existem\ mas com comportamentos diferentesk
• #length ] É o mesmo do rrray\ portanto faz com que o
ActiveRecord busque todos os objetos no banco\ instancie]os
e depois faz a contageml
• #count ] tonta quantos objetos existem no banco de dados\ fa]
zendo uma consulta É®“ Xvimosagora poucokfaz parte dos méto]
dos de cálculoYou usando o counter cachel
• #size ] thama a contagem pelo método #length caso os ob]
jetos tenham sido carregados\ caso contrário\conta via o método
#count_
uessa forma\ sempre que for fazer contagem de objetos\ pre￿ra usar
o #size_Ée você precisar usar a coleção completa de objetos Xcuidado
com o uso de memóriaQY\use o #length_
âam o s mostrar então no template de avaliações X
app/views/rooms/_review.html.erbYesses númerosk
>sywtion wl_ssh*ryviyw*-
<% iz room:showuzormi %>
<%= rynxyr p_rti_l4 'ryviywuzorm'c low_ls4 {room4 room} %>
<% ylsy %>
<%= t ':st_ts'c _vyr_0y4 room:st_rsc
m_x4 room:ryviywupoints:m_xc
wount4 room:tot_luryviyws %>
<% ynx %>
>,sywtion-
￿￿￿

## Página 242

￿￿_￿_ –édia de avaliações usando agregações tasa do tódigo
v no arquivo de z￿￿n Xconfig/locales/pt-BR.ymlY\usamos a funcionali]
dade para pluraisk
ptçk+4
@ :::
rooms4
@:::
ryviywuzorm4
lo0inutouryviyw4 'n_ç_ o lo0in p_r_ _v_li_r qu_rtos'
ryviyw4
st_ts4
zyro4 '(ão há _v_li_çõys'
ony4 'b{_vyr_0y},b{m_x} {$ _v_li_ção}'
othyr4 'b{_vyr_0y},b{m_x} {b{wount} _v_li_çõys}'
” que acontece é que\ quando usamos a chave :count na tradução\ podemos
criar mensagens diferenciadas para cada valor de :countkzero para zero\one para
um e other para o restante\assim não precisamos nos preocupar em fazer regras para
cada valor_
￿￿￿

## Página 243

tasa do tódigo tapítulo ￿￿_ rvalia ção de quartos\ relacionamentos muitos para muitos e_ _ _
wigura￿￿_￿krvalia ções com estatísticas básicas
￿￿n￿ í ￿￿￿￿￿￿￿￿￿￿￿￿￿￿￿￿￿ ￿￿￿￿ ￿￿￿￿￿￿ ￿￿￿￿￿￿￿￿
øor muito tempo\ designers sofriam na criação de páginas àeb_ “imitados a não
mais que ￿￿fontes\eles tinham que fazer milagres para tornar um site elegante e não
cair em clichés_øorém\ isso mudou completamente desde que os browsers passaram
a aceitar fontes embutidas via a diretiva @font-face_tom ela\ é possível que um
site use uma fonte não instalada no sistema do usuário_
rlém disso\ o xoogle criou o serviço Google Webfonts
Xwww_google_com‘webfonts‘Y\serviço gratuito e que possui diversas fontes de
alta qualidade e é muito fácil de usar_ É exatamente isso que estamos usando no
tolcho_net para usar a fonte “øaci￿co” _
Áecentemente\as webfonts tem sido usadas para outro propósito_tom a criação
de dispositivos com altíssima densidade de pixels Xo“•ovo iøad” e os –acsooks
com “Áetina uisplay”Y\os browsers acabam escalonando as imagens para que elas
￿quem no tamanho con￿gurado_zssoresulta em defeitos e degradação da qualidade
das imagens em um site_âe j ao exemplo a seguirk
￿￿￿

## Página 244

￿￿_￿_ rplica ções modernas usam fontes modernas tasa do tódigo
wigura￿￿_￿kÍâ ￿_orgkÉite não preparado para alta densidade
âe j aa diferença entre a qualidade da fonte\que é um elemento facilmente esca]
lonável e as imagens_®uando elas são ampliadas\ muitos defeitos visuais ocorrem_
tompare com o exemplo do site tÉÉ Íricks Xhttpk‘‘www_css]tricks_comY\ que é oti]
mizado para “Áetina uisplayRk
￿￿￿

## Página 245

tasa do tódigo tapítulo ￿￿_ rvalia ção de quartos\ relacionamentos muitos para muitos e_ _ _
wigura￿￿_￿ktÉÉ]Íricks_comk”timizado para alta densidade
rlcan çar esse resultado não é simples\ é necessário aplicar vários truques com
tÉÉ e repetir imagens de forma a ter uma versão com pouca e outra com alta den]
sidade de pixels\ ou através do uso de imagens Éâx XemvetorY_”utra solução é
transformar seus ícones e imagens bastante utilizadas em fontes_ tomo as fontes
são facilmente escalonáveis Xpoissão vetores\e não mapa de pixelsYe relativamente
simples de serem criadas\ muitos designers e desenvolvedores de frontoendestão op]
tando por essa solução_
vxiste uma fonte open source e disponível para uso comercial chamada “wont
rwesome” Xhttpk‘‘fortawesome_github_com‘wont]rwesome‘Y _ rlém de possuir
grande qualidade\ ela possui vários pictogramas úteis e é de graça_
øortanto\antes de continuar com o desenvolvimento do site\vamos instalá]la no
tolcho_net_ øara isso\ existe uma gem para que possamos usar a wontrwesome no
rssets øipeline_rdicione ao xem ￿lek
0ym *zontç_wysomyçr_ils*
ã vunxly
:::
￿￿￿

## Página 246

￿￿_￿_ vu vejo estrelas ] usando tÉÉ e {avaÉcriptpara melhorar as avaliações tasa do tódigo
onst_llin0 zontç_wysomyçr_ils {é:e:$:e}
:::
øor ￿m\ basta incluir a linha do wontrwesome no application.css\ resul]
tando emk
,[
[ :::
[h ryquiryusylz
[h ryquiryutryy :
[h ryquiry zontç_wysomy
[,
øronto\temos a wontrwesome instalada e pronta para uso_
￿￿n￿ E￿ ￿￿￿￿ ￿￿￿￿￿￿￿￿m￿￿￿￿￿￿ õSS ￿ J￿￿￿S￿￿￿￿￿￿￿￿￿
￿￿￿￿￿￿￿￿ ￿￿ ￿￿ ￿￿￿￿￿￿￿￿
tom backoend e as interações prontos\ vamos colocar a “wontrwesome” para usok
usaremos estrelas para mostrar as pontuações de ￿a ￿ na listagem_øara isso\ vamos
mudar um pouco o template\ o tÉÉ e o z￿￿n_
tomecemos pelo template de avaliações X
app/views/room/_review.html.erbY_ ørimeiro\ criamos o número de
estrelas preenchidas Xfilled_starYe depois criamos o número de estrelas não
preenchidas Xsubtraindoo número de estrelas do quarto do total de ￿Y_” resultado
é o seguintek
>sywtion wl_ssh*ryviyw*-
<% iz room:showuzormi %>
<%= rynxyr p_rti_l4 'ryviywuzorm'c low_ls4 {room4 room} %>
<% ylsy %>
<% room:st_rs:timys xo %>
>sp_n wl_ssh*st_r zillyxust_r*->,sp_n-
<% ynx %>
<% {room:ryviywupoints:m_x ç room:st_rs}:timys xo %>
>sp_n wl_ssh*st_r ymptyust_r*->,sp_n-
<% ynx %>
<%= t ':st_ts'c wount4 room:tot_luryviyws %>
￿￿￿

## Página 247

tasa do tódigo tapítulo ￿￿_ rvalia ção de quartos\ relacionamentos muitos para muitos e_ _ _
<% ynx %>
>,sywtion-
øor exemplo\ no caso de ￿￿ avaliações que resultam em ￿ estrelas\ o yÍ–“ re]
sultante serák
>sywtion wl_ssh*ryviyw*-
>sp_n wl_ssh*st_r zillyxust_r*->,sp_n-
>sp_n wl_ssh*st_r zillyxust_r*->,sp_n-
>sp_n wl_ssh*st_r zillyxust_r*->,sp_n-
>sp_n wl_ssh*st_r ymptyust_r*->,sp_n-
>sp_n wl_ssh*st_r ymptyust_r*->,sp_n-
{e! _v_li_çõys}
>,sywtion-
rtualizamos também o z￿￿n Xconfig/locales/pt-BR.ymlYpara alterar a
mensagemk
ptçk+4
rooms4
ryviywuzorm4
lo0inutouryviyw4 'n_ç_ o lo0in p_r_ _v_li_r qu_rtos'
ryviyw4
st_ts4
ony4 '{$ _v_li_ção}'
othyr4 '{b{wount} _v_li_çõys}'
v\ por ￿m\ o tÉÉ Xapp/assets/stylesheets/room.css.scssYk
:ryviyw :st_r {
zontçz_mily4 *nontjwysomy*g
zontçsizy4 $fpxg
}
:ryviyw :zillyxust_r {
wolor4 0olxg
tyxtçsh_xow4 $px $px @555g
\4vyzory { wontynt4 *tzdd8*g }
}
￿￿￿

## Página 248

￿￿_￿_ vu vejo estrelas ] usando tÉÉ e {avaÉcriptpara melhorar as avaliações tasa do tódigo
:ryviyw :ymptyust_r {
wolor4 @___g
\4vyzory { wontynt4 *tzdd=*g }
}
ásamos o :before para adicionar um caractere especial da “wontrwesome”
antes das estrelas_uepois dessas alterações\ temos a listagem com estrelask
wigura￿￿_￿krvalia ções na listagem com estrelas
rgora\ para ￿nalizar\tornaremos a votação mais interessante\vamos usar as es]
trelas de modo que o usuário possa votar apenas no clique_øara isso\ alteraremos o
tÉÉ de forma que o cursor do mouse indique ao usuário que ele pode interagir com
a estrela\ com diferentes cores e apresentações_
øara isso\ primeiro altere o tÉÉ do formulário X
app/assets/stylesheets/room.css.scssYk
@wontynt :ryviyw {
m_r0in4 dg
p_xxin04 dg
￿￿￿

## Página 249

tasa do tódigo tapítulo ￿￿_ rvalia ção de quartos\ relacionamentos muitos para muitos e_ _ _
zlo_t4 ri0htg
vorxyr4 nonyg
,[ jxiwiony _ sy0uinty linh_4 [,
position4 ryl_tivyg
}
vm seguida\ adicione as regras para posicionar os símbolos de ”} e erro em um
lugar de forma que as estrelas não saiam do lugar quando o formulário for enviado_
:ryviyw :iwonçokc
:ryviyw :iwonçrymovy {
position4 _vsolutyg
ri0ht4 dg
}
rs próximas ￿ regras são para estilizar a estrela de acordo com o novo yÍ–“ do
formulário\que veremos em seguida_
:ryviyw l_vyl i {
zontçsizy4 $fpxg
tyxtçsh_xow4 $px $px @555g
wursor4pointyrg
wolor4 @wwwg
}
:ryviyw l_vyl:to00lyx i {
wolor4 0olxg
}
r última regra é para sumir com os botões radio e o “enviar” _
:ryviyw zorm - input {
xispl_y4nonyg
}
” novo templatedo formulário Xapp/views/rooms/_review_form.html.erbY
deve ￿car assimk
<% iz room:w_nuryviywi %>
<%= zormuzor room:ryviywuroutyc rymoty4 truy xo |z| %>
<% room:ryviywupoints:y_wh xo |point| %>
<%= z:r_xiouvutton 4pointsc point %>
￿￿￿

## Página 250

￿￿_￿_ vu vejo estrelas ] usando tÉÉ e {avaÉcriptpara melhorar as avaliações tasa do tódigo
<%= z:l_vyl 4pointsc v_luy4 point xo %>
>i wl_ssh*iwonçst_r*->,i-
<% ynx %>
<% ynx %>
<%= z:suvmit %>
<% ynx %>
<% ylsy %>
>sp_n wl_ssh*lo0inuryquiryx*-
<%= t{':lo0inutouryviyw'} %>
>,sp_n-
<% ynx %>
r diferença está na maneira que construímos o label_ro invés de colocarmos o
valor\vamos simplesmente desenhar uma estrela\de acordo com o “wont]rwesome” _
øara encerrar essa funcionalidade\ adicionamos o código {avaÉcriptpara alterar
a cor das estrelas quando o usuário passar o mouse sobre elas\ e com isso mostrar ao
usuário que ele está de fato alterando a sua avaliação_
øara isso\ adicione o seguinte código {avaÉcript no arquivo
app/assets/javascripts/rooms.jsk
ã{zunwtion{} {
,, :::
zunwtion hi0hli0htqt_rs{ylym} {
ylym:p_rynt{}:whilxryn{'l_vyl'}:rymovyll_ss{'to00lyx'}g
ylym:_xxll_ss{'to00lyx'}:pryvjll{'l_vyl'}:_xxll_ss{'to00lyx'}g
}
hi0hli0htqt_rs{ã{':ryviyw input4whywkyx ] l_vyl'}}g
v_r ãst_rs h ã{':ryviyw input4yn_vlyx ~ l_vyl'}g
ãst_rs:on{'mousyyntyr'c zunwtion{} {
hi0hli0htqt_rs{ã{this}}g
}}g
ãst_rs:on{'mousyly_vy'c zunwtion{} {
hi0hli0htqt_rs{ã{':ryviyw input4whywkyx ] l_vyl'}}g
}}g
￿￿￿

## Página 251

tasa do tódigo tapítulo ￿￿_ rvalia ção de quartos\ relacionamentos muitos para muitos e_ _ _
ã{':ryviyw input'}:on{'wh_n0y'c zunwtion{} {
ãst_rs:ozz{'mousyyntyr'}:ozz{'mousyly_vy'}:ozz{'wliwk'}g
ã{this}:p_rynt{'zorm'}:suvmit{}g
}}g
}}g
r primeira função\ highlightStars\ é a responsável por adicionar e remo]
ver o destaque das estrelas_ saseado no elemento passado como parâmetro\ pri]
meiro remove]se o destaque de todas as estrelas XclassetÉÉ toggledYe em seguida
adiciona]se a mesma classe apenas ao elemento em destaque e os anteriores_
ásando essa função\ativamos as estrelas previamente selecionadas pelo usuário_
zsso é importante para mostrar ao usuário que a ação dele teve efeito_ vste seletor
executa no momento que a página é carregada_
r primeira parte\ input:checked irá retornar todos os inputs que estão mar]
cados Xválidosomente para check boxes e radio buttonsY_ásando o +\ retornamos
apenas o primeiro objeto imediatamente ao redor deste input_ zsso signi￿ca que o
seletor irá retornar o label imediatamente ao lado de um input que está selecionado_
âe j aa seguir o resultadok
wigura￿￿_￿kwormuláriode avaliação enviado
v_r ãst_rs h ã{':ryviyw input4yn_vlyx ~ l_vyl'}g
•a linha anterior\ selecionamos todos os labels XasestrelasYem inputs que es]
tão habilitados_ ” comportamento é parecido com o seletor input:checked +
label\ porém dessa vez procuramos todos que estão habilitados_” objetivo é que
só iremos dar destaque quando o formulário estiver habilitado\ou seja\ apenas antes
de ser enviado_
￿￿￿

## Página 252

￿￿_￿_ vncerrando tasa do tódigo
ãst_rs:on{'mousyyntyr'c zunwtion{} {
hi0hli0htqt_rs{ã{this}}g
}}g
ãst_rs:on{'mousyly_vy'c zunwtion{} {
hi0hli0htqt_rs{ã{':ryviyw input4whywkyx ] l_vyl'}}g
}}g
vsses blocos são responsáveis pelos eventos do mouse_ ” primeiro evento\ o
mouseenter\ ocorre quando o usuário posiciona o mouse em cima de uma estrela_
•esse momento\vamos destacar a estrela clicada e as anteriores_
•o evento mouseleave\ vamos voltar ao estado inicial do formulário\ou seja\
se já havia uma estrela marcada\ tornamos ela marcada novamente_
winalmente\temos o seguinte blocok
ã{':ryviyw input'}:on{'wh_n0y'c zunwtion{} {
ãst_rs:ozz{'mousyyntyr'}:ozz{'mousyly_vy'}:ozz{'wliwk'}g
ã{this}:p_rynt{'zorm'}:suvmit{}g
}}g
” evento change é executado após o click em uma estrela_ •esse momento\
desligamos todos os ﬀvent handlers que criamos\ ou seja\ desabilitamos a animação
de estrelas e ativamos o evento de submit do formulário\ fazendo o envio do for]
mulário via r{rã_
￿￿n￿ E￿￿￿￿￿￿￿￿￿
øarabénsQâo c êperseverou até o ￿m das funcionalidades principais do tolcho_netQ
woium caminho longo e difícil\ especialmente nesse capítulo_–as você aprendeu a
fazer muita coisak
• rssocia ções muitos]para]muitosl
• Áemover objetos com segurançal
• ásar fontes e webfonts para deixar seu design bonito e escalonávell
• tustomizar o rssets øipelinel
• •ovas funcionalidades do ActiveRecordl
￿￿￿

## Página 253

tasa do tódigo tapítulo ￿￿_ rvalia ção de quartos\ relacionamentos muitos para muitos e_ _ _
• ”rganiza ção de controles complexosl
• ”rganiza ção de rotas complexasl
• ásar o ActiveRecord para fazer contas de maneira e￿cientel
• ”p ções avançadas de z￿￿nl
• vxtra ção e organização de templates complexosl
• áso de presenters para simpli￿car templates complexosl
• ásar j®uery e r{rãl
uepois de tudo isso\ você já está preparado para criar sua própria aplicação do
zero_”s conhecimentos vistos nesse capítulo já cobrem muitas funcionalidades usa]
das em aplicações de verdade\ com bastante complexidade_ É lógico que livro ne]
nhum irá substituir a experiência de construir as suas próprias aplicações\mas agora
você já tem a base para colocar suas ideias em prática_
•o próximo capítulo\vamos colocar algumas funcionalidades satélites\úteis mas
não essenciais para o funcionamento da aplicação_vssas funcionalidades\porém\são
muito comuns em grande parte das aplicações web e portanto é importante saber_
￿￿￿

## Página 255

t ￿￿￿￿￿￿￿ ￿￿
øolindo o tolcho_net
Não importa se você vai devagarno que importa é você nunca parar
– tonfúcio
vste é o último capítulo em que vamos desenvolver funcionalidades no tol]
cho_net_âo c êestá chegando ao ￿nal\e a aplicação já está bem funcional_•ós vamos
fazer algumas melhorias na aplicação\ desenvolvendo as seguintes funcionalidadesk
busca textual\ URL slugs usando a gem friendly_id\ paginação usando a gem
kaminari\ upload de fotos usando a gem carrierwave e\ ￿nalmente\ colocar o
tolcho_net online\ no yeroku_
￿￿n￿ F￿￿￿ ￿￿￿￿￿￿ ￿￿￿￿￿￿￿￿￿￿￿￿￿￿ ￿￿￿ ￿ R￿￿￿￿
•o tolcho_net há três informações importantes pelas quais um usuário pode pes]
quisarklocalidade\ título e a descrição de um quarto_ørecisamos de uma busca que
nos permita pesquisar nesses três “textos” \ou seja\ precisamos de uma busca textual\
um pouco diferente das buscas que temos feito até então_

## Página 256

￿￿_￿_ waça buscas textuais apenas com o Áails tasa do tódigo
susca textual é um assunto bastante complexo e existe muita literatura sobre
o assunto\ portanto vamos fazer uma funcionalidade simpli￿cada e cobrir o que é
possível criar com apenas o uso do Áails_
r funcionalidade é a seguintekvamos criar um campo de texto próximo ao título
de listagem de quartos_suscaremos também o conteúdo da caixa de texto e procurar
nos campos mencionados anteriormente_uos resultados encontrados\ vamos mar]
car visualmente para o usuário facilmente identi￿car o trecho que está procurando_
ørimeiro\ vamos construir a funcionalidade no backoend_øara isso\vamos criar
um método chamado .search no modelo de quartos Xapp/models/room.rbYk
wl_ss +oom > jwtivy+yworx44k_sy
@ :::
xyz sylz:sy_rwh{quyry}
iz quyry:prysynti
whyry{/'low_tion õo1m 4quyry )+
titly õo1m 4quyry )+
xyswription õo1m 4quyry'c quyry4 *b@{quyry}b*3}
ylsy
swopyx
ynx
ynx
@ ::
ynx
•este método\ se a busca estiver presente\ fazemos o ￿ltro usando o operador
LIKE do É®“ para fazer a busca nos campos mencionadosk location\ title e
description_taso contrário\vamos retornar o escopo atualk
+oom:sy_rwh{'q_o'}
@ qmõml? *rooms*:[ n+)p *rooms* s#m+m {low_tion õo1m 'bq_ob' )+
@ titly õo1m 'bq_ob' )+
@ xyswription õo1m 'bq_ob'}
@ h- >jwtivy+yworx44+yl_tion /@>+oom ix4 êc ::: -3-
+oom:sy_rwh{''}
@ qmõml? *rooms*:[ n+)p *rooms*
@ h- >jwtivy+yworx44+yl_tion /@>+oom ix4 êc ::: -3-
￿￿￿

## Página 257

tasa do tódigo tapítulo ￿￿_ øolindo o tolcho_net
P￿￿ ￿￿￿ ￿￿￿￿ ￿￿￿￿￿￿ ￿ ￿￿￿ ￿￿￿￿
Éeria natural pensar em usar o método .all no caso da busca não
estiver presente\ pois retorna todos os objetos_ øorém\ se este método
for usado em conjunto com outros escopos\ o que é bastante comum\ o
.all iria cancelar todos os outros escopos e o comportamento ￿nal seria
bem inesperado_” .scoped faz esse papel de manter o escopo_
tomo o modelo já faz todo o trabalho pesado\ no controle de quartos X
app/controllers/rooms_controller.rbYvamos apenas chamar o método
que acabamos de criar_r ação index ￿ca da seguinte formak
wl_ss +oomslontrollyr > jppliw_tionlontrollyr
@ :::
xyz inxyx
ísy_rwhuquyry h p_r_ms/4q3
rooms h +oom:sy_rwh{ísy_rwhuquyry}
írooms h rooms:mosturywynt:m_p xo |room|
+oom%rysyntyr:nyw{roomc sylzc z_lsy}
ynx
ynx
@ :::
ynx
âam o s diferenciar o template de índice X
app/views/rooms/index.html.erbY apenas para mostrar um título dife]
rente caso estejamos exibindo resultado de buscas_ øara isso\ vamos veri￿car a
presença de um termo de busca Xsearch_queryY_ âam o s incluir no topo do
template o formulário de busca_” resultado ék
<%= rynxyr 'sy_rwh' %>
>h$-
<% iz ísy_rwhuquyry:prysynti %>
<%= t ':sy_rwhurysults' %>
<% ylsy %>
￿￿￿

## Página 258

￿￿_￿_ waça buscas textuais apenas com o Áails tasa do tódigo
<%= t ':titly' %>
<% ynx %>
>,h$-
<%= rynxyr írooms %>
•a partial contendo o formulário Xapp/views/rooms/_search.html.erbY
não será possível usar o helper form_for\pois não estamos criando um formulário
de modelo_” Áails possui também helpers para esta situaçãok
<%= zormut_0 roomsup_thc mythox4 40ytc wl_ss4 'sy_rwh' xo %>
<%= tyxtuziylxut_0 4qc ísy_rwhuquyryc
pl_wyholxyr4 t{':sy_rwhuzor'} %>
<% ynx %>
” que fazemos é enviar os dados à ação index do controle de quartos via o
parâmetro q\ que possui o conteúdo para ￿ltrar a listagem_”bserve que temos que
declarar o método yÍÍø para GET para que o roteador não nos envie para a ação
create_
rtualizamos as chaves z￿￿n Xconfig/locales/pt-BR.ymlY\para adicionar
as mensagens relativas às buscask
rooms4
inxyx4
titly4 '.u_rtos xisponívyis'
sy_rwhurysults4 '+ysult_xos x_ vusw_'
sy_rwh4
sy_rwhuzor4 'kusw_r por:::'
vm seguida\ usamos o helper highlight do Áails\para destacar os resultados
da busca\ na partial de quarto_ rlteraremos o título\ a descrição e a localidade do
quarto Xapp/views/rooms/_room.html.erbYk
>_rtiwly-
:::
>he-
<%= linkuto hi0hli0ht{room:titlyc ísy_rwhuquyry}c room:routy %>
>,he-
:::
>p-
>sp_n wl_ssh*low_tion*-
￿￿￿

## Página 259

tasa do tódigo tapítulo ￿￿_ øolindo o tolcho_net
<%= linkuto hi0hli0ht{room:low_tionc ísy_rwhuquyry}c
*https4,,m_ps:0oo0ly:wom,iqh@{room:low_tion}*c
t_r0yt4 4vl_nk %>
>,sp_n-
>,p-
>p-<%= hi0hli0ht{room:xyswription || ''c ísy_rwhuquyry} %> >,p-
:::
>,_rtiwly-
øor ￿m\ adicionamos o estilo tÉÉ para o campo de busca_ ása]
mos a “wont rwesome” para adicionar o clássico ícone da lupa X
app/assets/stylesheets/room.css.scssY\ e vamos estilizar os cam]
pos destacados pela função highlightk
@wontynt :sy_rwh {
zlo_t4 ri0htg
m_r0in4 dg
position4 ryl_tivyg
\4_ztyr {
p_xxin04 8pxg
zontçsizy4 $êpxg
zontçz_mily4 'nontjwysomy'g
position4 _vsolutyg
wontynt4 *tzdde*g
wolor4 @vvvg
top4 dg
ri0ht4 dg
}
}
:hi0hli0ht {
zontçsizy4 inhyritg
zontçwyi0ht4 inhyritg
v_wk0rounxçwolor4 0olxg
}
tom essas alterações\ ao realizarmos uma pesquisa\ seu resultado é exibido com
o destaque no termo procurado_
￿￿￿

## Página 260

￿￿_￿_ áÁ“s mais amigáveis através de slugs tasa do tódigo
wigura￿￿_￿kÁesultado de buscas destacados
øor ￿m\é necessário lembrar que essa busca é uma busca simples_Ée você quiser
fazer buscas mais rebuscadas\ é interessante usar tecnologias como o Éolr Xhttpk‘‘
lucene_apache_org‘solr‘Y_tom o Éolr\você é capaz de criar índices complexos\fazer
busca facetada\ ￿ltros e outras funcionalidades avançadas_ Ée você tiver interesse\
veri￿que a gem sunspot Xhttpsk‘‘github_com‘outo￿ime‘sunspotY\ que integra o
Áails com o Éolr_
￿￿n￿ URL￿ ￿￿￿￿ ￿￿￿￿￿￿￿￿￿￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿
®uando você acessa o site da tasa do tódigo\ para ver esse livro\você entra no ende]
reço httpk‘‘www_casadocodigo_com_br‘products‘livro]ruby]on]rails_znternamente\esse
livro possui um zu\ e poderia ser usado para busca_ rcontece que essa áÁ“ não é
nada amigável\números soltos dessa forma não traz nenhum signi￿cado ao usuário_
thamamos essa técnica de mapear nomes amigáveis à zus de URL Slugs
URL slugs são áÁ“s que não usam zus e sim uma áÁ“ mais interessante_”u seja\
ao invés de usar algo como httpk‘‘localhostk￿￿￿￿‘rooms‘ ￿ \ usamos httpk‘‘localhostk
￿￿￿￿‘rooms‘colchonete]na]sala _ vsta técnica também traz vantagens na otimização
para mecanismos de busca XouSﬀO oSearch ﬀngine OptimizationY_
øara implementar essa funcionalidade\podemos alterar a forma que as URL helo
pers do Áails constroem as rotas a partir do modelo_”s helpers chamam o método
#to_param de modelos_vsse método é usado para criar uma string que representa
o objeto em áÁ“s_ r implementação padrão do Áails irá retornar o zu do objetok
￿￿￿

## Página 261

tasa do tódigo tapítulo ￿￿_ øolindo o tolcho_net
room h +oom:zirst
@ h- @>+oom ix4 êc ::: -
room:toup_r_m
@ h- *ê*
rlém disso\ podemos aproveitar o fato de que\ em Áuby\strings são ignoradas
em conversões de númerosk
*$eéçissoçv_içxys_p_rywyr*:toui
@ h- $eé
zsso signi￿ca que\quando uma busca for feita por zu\ apenas a parte numérica é
utilizada_
øortanto\ podemos apenas então alterar o método to_param no modelo de
quartos para incluir uma descrição amigável do quarto\ e tudo continuará funcio]
nandok
wl_ss +oom > jwtivy+yworx44k_sy
@ :::
xyz toup_r_m
*@{ix}ç@{titly:p_r_mytyrizy}*
ynx
ynx
+oom:zinx{e}
@ h- @>+oom ix4 ec titly4 *l_s_ xy pr_i_ womplyt_*c :::-
+oom:zinx{'eçw_s_çxyçpr_i_çwomplyt_'}
@ h- @>+oom ix4 ec titly4 *l_s_ xy pr_i_ womplyt_*c :::-
•esse exemplo\ o link gerado ék httpk‘‘localhostk￿￿￿￿‘rooms‘
￿]casa]de]praia]completa
vssa solução funciona\ porém\ há vários detalhes que temos que tomar cuidado
com essa implementação_ øor exemplo\ o que fazer com con￿itos de slugsp –ais
ainda\ como lidar com detalhes difíceis de prever\tal como transliteração de carac]
teres\ ou seja\ transformar símbolos como “ø”ou “ã”em “oe”e “aRp
øortanto\ ao invés de ter que nos preocupar com estas situações Xeoutras não
listadas aqui tambémY\podemos nos aproveitar da experiência de outros desenvol]
vedores\usando ferramentas open source_
￿￿￿

## Página 262

￿￿_￿_ áÁ“s mais amigáveis através de slugs tasa do tódigo
øara resolver o problema de slugs\ vamos usar a gem friendly_id\ feita pelo
•orman tlarke\ desenvolvedor que atua na comunidade Áuby e Áails há anos_ r
ferramenta encontra]se emkhttpsk‘‘github_com‘wriendlyzd‘friendlyúid
øara instalar esta gem\ o primeiro passo é adicioná]la no Gemfilek
õ ￿￿￿￿￿￿ ￿￿￿ ￿￿￿￿ ￿￿ ￿￿￿￿￿￿￿￿￿￿￿￿￿￿￿￿
znfelizmentea gem ainda não está completamentepreparada para uso
com o Áails ￿_ âam o susá]la de qualquer forma pois é uma questão de
pouco tempo para que ela se torne estável e sua versão ￿ seja liberada_
Ée for utilizar a gem friendly_id\lembre]se de remover o método
to_param que implementamos manualmente_
0ym 'zriynxlyuix'c 0ithuv4 'nriynxlyox,zriynxlyuix'c vr_nwh4 'm_styr'
v usar o bundler para instalar as dependênciask
ã vunxly
:::
nytwhin0 0it4,,0ithuv:wom,nriynxlyox,zriynxlyuix:0it
:::
"sin0 zriynxlyuix {8:d:d:_lph_$}
zrom 0it4,,0ithuv:wom,nriynxlyox,zriynxlyuix:0it {_t m_styr}
:::
vm seguida\ a gem precisa que você crie um campo extra\ chamado slug\ na
tabela quarto\ que é a informação que teremos a áÁ“ amigável_ øara isso\ vamos
criar uma nova migraçãok
ã r_ils 0 mi0r_tion _xxuslu0sutourooms slu04strin04inxyx
invoky _wtivyuryworx
wry_ty xv,mi0r_ty,ed$éd!$5d5ddééu_xxuslu0sutourooms:rv
ørecisamos adicionar um índice de unicidade_øor isso\ alteraremos a migração
geradak
wl_ss jxxqlu0s?o+ooms > jwtivy+yworx44pi0r_tion
xyz wh_n0y
_xxuwolumn 4roomsc 4slu0c 4strin0
￿￿￿

## Página 263

tasa do tódigo tapítulo ￿￿_ øolindo o tolcho_net
_xxuinxyx 4roomsc 4slu0c uniquy4 truy
ynx
ynx
âam o s também ter que criar uma tabela para guardar os slugs antigos_ ”
friendly_id já faz isso para nós\ basta executark
ã r_ils 0ynyr_ty zriynxlyuix
xv,mi0r_ty,ed$éd!$5d5é8éduwry_tyuzriynxlyuixuslu0s:rv
vxecutamos as migraçõesk
ã r_ky xv4mi0r_ty
rlteraremos o modelo quarto X app/models/room.rbY para usar o
friendly_id_ øara isso\ segundo a documentação da gem\ é necessário es]
tender o módulo FriendlyId\ adicionar uma validação de modo que slugs sejam
obrigatórios no banco de dados e por ￿m\ con￿gurar o módulo friendly_id\
para usar as funcionalidades :slugged\ que é o modo padrão de operação da gem
ea :history\ para gravar o histórico de slugsk
wl_ss +oom > jwtivy+yworx44k_sy
yxtynx nriynxlyox
@:::
v_lix_tysuprysynwyuoz 4titly
v_lix_tysuprysynwyuoz 4slu0
zriynxlyuix 4titlyc usy4 /4slu00yxc 4history3
@:::
ynx
øor ￿m\ precisamos alterar a busca de quartos_ øara isso\ mudaremos todas as
chamadas de Room.find para Room.friendly.find no controle de quartosk
wl_ss +oomslontrollyr > jppliw_tionlontrollyr
vyzoryu_wtion 4ryquiryu_uthyntiw_tionc
only4 /4nywc 4yxitc 4wry_tyc 4upx_tyc 4xystroy3
xyz inxyx
ísy_rwhuquyry h p_r_ms/4q3
￿￿￿

## Página 264

￿￿_￿_ áÁ“s mais amigáveis através de slugs tasa do tódigo
rooms h +oom:sy_rwh{ísy_rwhuquyry}
írooms h rooms:mosturywynt:m_p xo |room|
@ (ão yxivirymos o zormulário n_ list_0ym
+oom%rysyntyr:nyw{roomc sylzc z_lsy}
ynx
ynx
xyz show
roomumoxyl h +oom:zriynxly:zinx{p_r_ms/4ix3}
íroom h +oom%rysyntyr:nyw{roomumoxylc sylz}
ynx
xyz nyw
íroom h wurryntuusyr:rooms:vuilx
ynx
xyz yxit
íroom h wurryntuusyr:rooms:zriynxly:zinx{p_r_ms/4ix3}
ynx
xyz wry_ty
íroom h wurryntuusyr:rooms:vuilx{roomup_r_ms}
iz íroom:s_vy
ryxirywtuto íroomc notiwy4 t{'zl_sh:notiwy:roomuwry_tyx'}
ylsy
rynxyr _wtion4 *nyw*
ynx
ynx
xyz upx_ty
íroom h wurryntuusyr:rooms:zriynxly:zinx{p_r_ms/4ix3}
iz íroom:upx_ty{roomup_r_ms}
ryxirywtuto íroomc notiwy4 t{'zl_sh:notiwy:roomuupx_tyx'}
ylsy
rynxyr _wtion4 *yxit*
ynx
ynx
￿￿￿

## Página 265

tasa do tódigo tapítulo ￿￿_ øolindo o tolcho_net
xyz xystroy
íroom h wurryntuusyr:rooms:zriynxly:zinx{p_r_ms/4ix3}
íroom:xystroy
ryxirywtuto roomsuurl
ynx
priv_ty
xyz roomup_r_ms
p_r_ms:
ryquiry{4room}:
pyrmit{4titlyc 4low_tionc 4xyswriptions}
ynx
ynx
ørontoQâo c êjá tem a funcionalidade de URL slugs_ øara testar\ crie um novo
quarto e veja a áÁ“ como ￿ca Xlembre]sede reiniciar o servidor do Áails\ caso já
não tenha feitoY_
í ￿￿￿￿￿￿￿￿￿￿ ￿￿￿￿￿￿￿ ￿￿￿￿￿￿￿￿￿￿￿￿￿
” FriendlyId irá funcionar com quartos sem slug\ ou seja\ irá usar
o zu do modelo caso não seja possível usar o slug_ øorém\ para termos
consistência\podemos atualizar os modelos para usarem slugs\ basta ati]
var os callbacks de save que o FriendlyId irá fazer o restok
+oom:zinxuy_wh{\4s_vy}
” find_each é uma alternativa ao all para fazer alterações em
lotes\ caso você tenha muitos registros no banco de dados_
￿￿n￿ P￿￿￿￿￿￿￿￿ ￿￿ ￿￿￿￿￿ ￿￿ ￿￿￿￿￿ ￿￿￿￿￿￿￿￿￿￿￿￿￿
zmagine o tolcho_net no futuro\explodindo de sucesso e com mais de ￿￿￿ quartos
cadastrados_r listagem ￿cará lenta\pois são muitos objetos para se exibir e calcular
a média da pontuação_øara essa situação\ é normal paginar o resultado das buscas\
de modo que os resultados menos relevantes ￿quem ao ￿nal_
vssa funcionalidade não é complicada de se criar usando escopos_ –as a gem
kaminari Xhttpsk‘‘github_com‘amatsuda‘kaminariYtorna isso ainda mais fácil_
￿￿￿

## Página 266

￿￿_￿_ øaginação de dados de forma descomplicada tasa do tódigo
âam o sprimeiro instalar a gem_tomo de costume\basta colocá]la no Gemfile
e fazer o bundlek
0ym 'k_min_ri'
ã vunxly
:::
onst_llin0 k_min_ri {d:$ê:$}
:::
” kaminari insere\ através de meta]programação\ alguns métodos no
ActiveRecord para fazer a paginação_øorém\o uso de presenters irá atrapalhar\já
que estamos usando esses objetos ao invés dos modelos diretamente_
ørecisamos criar um outro presenter para que possamos chamar os métodos de
paginação do kaminari_”utra coisa que precisamos fazer é tornar essa nova classe
uma espécie de coleção\para que o render collection: @rooms continue fun]
cionando_
znfelizmente o Áails não de￿niu uma interface para este tipo de interação_øor]
tanto precisamos implementar o método #to_ary\ que faz uma conversão do ob]
jeto atual para rrray quando isso for necessário Xviaconversão implícitaY_âe j ao
exemplo a seguirk
wl_ss ompliwitjrr_y
xyz tou_ry
/$cecé3
ynx
ynx
@ h- nil
/4_3 ] ompliwitjrr_y:nyw
@ h- /4_c $c ec é3
Áepare que ao juntarmos o rrray de :a\ com a instância de ImplicitArray\
o resultado foi um novo rrray com a junção de :a e o resultado do método to_ary
de ImplicitArray\ chamado pelo próprio Áuby_
tom isso em mente\ vamos criar o presenter RoomCollectionPresenter X
app/presenters/room_collection_presenter.rbY\que irá delegar os mé]
todos de paginação para a coleção ActiveRecord e criar presenters de quarto
quando o collection presenter for convertido para rrray_
￿￿￿

## Página 267

tasa do tódigo tapítulo ￿￿_ øolindo o tolcho_net
wl_ss +oomlollywtion%rysyntyr
xyly0_ty 4wurryntup_0yc 4numup_0ysc 4limituv_luyc 4tot_lup_0ysc
to4 4írooms
xyz initi_lizy{roomsc wontyxt}
írooms h rooms
íwontyxt h wontyxt
ynx
xyz tou_ry
írooms:m_p xo |room|
+oom%rysyntyr:nyw{roomc íwontyxtc z_lsy}
ynx
ynx
ynx
R￿￿￿￿ ￿￿￿ ￿￿￿￿￿￿￿￿￿￿
vste é o tipo de código que sempre precisamos\ portanto você pode
aplicar em seus próprios projetos_ Ée preferir usar um presenter mais
completo\ vale a pena checar a gem draperk httpsk‘‘github_com‘
drapergem‘draper
rlteramos a ação index do RoomsController X
app/controllers/rooms_controller.rbY_ ásaremos a paginação no
modelo de quarto\via o uso dos métodos .page\ que de￿ne a página a ser buscada
e o método .per\ que de￿ne a quantidade de objetos por página_•a última linha
da ação\embrulhamos a coleção no presenter que acabamos de criark
wl_ss +oomslontrollyr > jppliw_tionlontrollyr
%m+u%j9m h $d
@ :::
xyz inxyx
ísy_rwhuquyry h p_r_ms/4q3
rooms h +oom:sy_rwh{ísy_rwhuquyry}:
p_0y{p_r_ms/4p_0y3}:
pyr{%m+u%j9m}
￿￿￿

## Página 268

￿￿_￿_ øaginação de dados de forma descomplicada tasa do tódigo
írooms h +oomlollywtion%rysyntyr:nyw{rooms:mosturywyntc sylz}
ynx
ynx
tom isso pronto\ para usar a paginação do kaminari\ basta colocar o helper
paginate no template da ação index Xapp/views/rooms/index.html.erbYk
:::
<%= rynxyr írooms %>
<%= p_0in_ty írooms %>
zsso é tudo que precisamos para fazer a paginação funcionar_
âam o smelhorar um pouco mais\criando um novo conjunto de chaves z￿￿n para
o kaminari\ no arquivo config/locales/pt-BR.pagination.ymlk
ptçk+4
viyws4
p_0in_tion4
zirst4 *\l_quog %rimyir_*
l_st4 *Últim_ \r_quog*
pryvious4 *\ls_quog jntyrior*
nyxt4 *%róxim_ \rs_quog*
trunw_ty4 *:::*
øor ￿m\ um pouco de tÉÉ para ajustar a exibição da paginação X
app/assets/stylesheets/default.css.scssYk
:p_0in_tion {
m_r0in4 edpx dg
}
:p_0in_tion sp_n {
p_xxin04 8pxg
m_r0in4 d épxg
v_wk0rounxçwolor4 @zzzg
vorxyr4 $px solix @wwwg
íinwluxy sh_xow{@wwwc dc épxc =px}g
}
” resultado é o seguintek
￿￿￿

## Página 269

tasa do tódigo tapítulo ￿￿_ øolindo o tolcho_net
wigura￿￿_￿k“inks para paginação no ￿m da página
øronto\ agora você tem uma paginação feita\ sem trazer dados demais para a
memória e sem exibir informações demais na tela_
￿￿n￿ U￿￿￿￿￿ ￿￿ ￿￿￿￿￿ ￿￿ ￿￿￿￿￿ ￿￿￿￿￿￿￿
zmaginevocê alugando um quarto ou um apartamento sem conseguir ver fotos desse
lugarp uifícil\ nãop øara isso\ precisamos permitir que fotos sejam associadas ao
quarto\através de upload de arquivos de imagens_
øara fazer o upload de fotos de quartos\ vamos usar uma gem chamada
carrierwave_ tom ela é possível criar thumbnails de fotos automaticamente
e até enviar essa foto para ser servida de serviços como o É￿\ da rmazon Xhttpk
‘‘aws_amazon_com‘s￿‘ You tloud wiles\da Áackspace Xhttpk‘‘www_rackspace_com‘
cloud‘public‘ ￿les‘ Y_
øara instalá]la\a receita é parecidakcolocar a gem no Gemfile e fazer o bundle_
r diferença é que temos que declarar a dependência à gem rmagick manualmente_
zsso deve]se ao fato de que o carrierwave funciona com outras gems de proces]
samento de imagem_
0ym 'w_rriyrw_vy'
0ym 'rm_0iwk'
ã vunxly
:::
onst_llin0 w_rriyrw_vy {d:f:d}
onst_llin0 rm_0iwk {e:$é:e} with n_tivy yxtynsions
:::
” funcionamento do carrierwave é o seguintekprimeiro\ é necessário criar
um uploader\ uma classe com a descrição das transformações que a imagem vai pas]
sar Xcriação de thumbnails\ por exemploYe onde guardar o arquivo enviado pelo
￿￿￿

## Página 270

￿￿_￿_ ápload de fotos de forma simples tasa do tódigo
usuário__øara facilitar esse trabalho\ o carrierwave instala um gerador_vntão\
vamos criar o uploader para fotos de quartosk
ã r_ils 0 uplo_xyr %iwtury
wry_ty _pp,uplo_xyrs,piwturyuuplo_xyr:rv
” arquivo gerado possui diversos comentários sobre a forma de utilizar o uploao
der e os parâmetros con￿guráveis_” resultado\das linhas não comentadas deve ser
o seguintek
@ ynwoxin04 utzçf
wl_ss %iwtury"plo_xyr > l_rriyrs_vy44"plo_xyr44k_sy
inwluxy l_rriyrs_vy44+p_0iwk
inwluxy qprowkyts44#ylpyrs44+_ils#ylpyr
stor_0y 4zily
@ <irytório onxy os _rquivos syrão _rm_zyn_xos
xyz storyuxir
*uplo_xs,@{moxyl:wl_ss:tous:unxyrswory},@{mountyxu_s},@{moxyl:ix}*
ynx
@ +yximynsion_ _ im_0ym p_r_ ziw_r no t_m_nho xy
@ no máximo 8ddx8ddc m_ntynxo o _spywto y wort_nxo
@ _ im_0ymc sy nywyssário:
prowyss 4rysizyutouzill h- /8ddc 8dd3
@ <imynsõys xo thumvn_il
vyrsion 4thumv xo
prowyss 4rysizyutouzill h- /$ddc $dd3
ynx
@ onzorm_ os zorm_tos pyrmitixos
xyz yxtynsionuwhityulist
bw{jp0 jpy0 0iz pn0}
ynx
ynx
￿￿￿

## Página 271

tasa do tódigo tapítulo ￿￿_ øolindo o tolcho_net
õ ￿￿￿￿￿￿￿ ￿￿￿￿￿￿ ￿ ￿￿ ￿￿￿￿ ￿￿￿￿￿￿￿
rpesar de conter muitas facilidades para o upload de imagens\ ele
pode ser usado com qualquer outro formato de arquivo\desde que você
desative as funcionalidades especí￿cas para imagens\ como processa]
mento de tamanho_rs outras ferramentas de upload para serviços ainda
funcionam_
áma vez criado o uploader\ precisamos criar uma coluna no banco de dados
para que o carrierwave guarde o nome do arquivo e saiba recuperá]lo na hora de
exibir a foto_øara isso\criemos e executemos a migração a seguirk
ã r_ils 0 mi0r_tion _xxupiwturyutourooms piwtury
wry_ty xv,mi0r_ty,ed$edf$éd$êdê8u_xxupiwturyutourooms:rv
ã r_ky xv4mi0r_ty
hh jxx%iwtury?o+ooms4 mi0r_tin0 hhhhhhhhhhhhhh
çç _xxuwolumn{4roomsc 4piwturyc 4strin0}
ç- d:dd$es
hh jxx%iwtury?o+ooms4 mi0r_tyx {d:dd$és} hhhhh
vm seguida\ precisamos associar o uploader ao modelo quarto_ zsso é feito
através da class macro mount\ método que o carrierwave adiciona ao
ActiveRecord_øortanto\no modelo quarto Xapp/models/room.rbY\basta adi]
cionar o seguinte códigok
wl_ss +oom > jwtivy+yworx44k_sy
@ :::
mountuuplo_xyr 4piwturyc %iwtury"plo_xyr
zriynxlyuix 4titlyc usy4 /4slu00yxc 4history3
@ :::
ynx
vssa class macro irá tornar o campo picture do modelo quarto em um
PictureUploader\ ao invés de uma simples string_r partir daí\ basta colocar]
mos mais um campo no formulário de quartos\ para que o arquivo seja informado_
vntão\ no app/views/rooms/_form.html.erbk
￿￿￿

## Página 272

￿￿_￿_ ápload de fotos de forma simples tasa do tódigo
:::
<%= zormuzor{íroom} xo |z| %>
:::
>p-
<%= z:l_vyl 4piwtury %>
<%= z:zilyuziylx 4piwtury %>
<%= yrrorut_0 íroomc 4piwtury %>
>,p-
>xiv wl_ssh*_wtions*-
<%= z:suvmit %>
>,xiv-
<% ynx %>
rdicione também a chave para traduzir o novo campo no arquivo de z￿￿n X
config/locales/pt-BR.ymlYk
ptçk+4
@:::
_wtivyryworx4
@:::
_ttrivutys4
@ :::
room4
xyswription4 <yswrição
low_tion4 õow_liz_ção
titly4 ?ítulo
piwtury4 noto
øara que as fotos possam ser gravadas\precisamos adicionar o campo picture
na lista de atributos permitidos pelo controle_rltere o método room_params\n a
classe RoomsControllerk
xyz roomup_r_ms
p_r_ms:
ryquiry{4room}:
pyrmit{4titlyc 4low_tionc 4xyswriptionsc 4piwtury}
ynx
øor ￿m\vamos alterar o presenter\yÍ–“ e o tÉÉ para exibir a imagem_rltere o
presenter de quartos para incluir os métodos que veri￿cam se há uma imagem\prepa]
ram o thumbnaile a própria imagem Xapp/presenters/room_presenter.rbYk
￿￿￿

## Página 273

tasa do tódigo tapítulo ￿￿_ øolindo o tolcho_net
wl_ss +oom%rysyntyr
@ :::
xyz piwturyuurl
íroom:piwturyuurl
ynx
xyz thumvuurl
íroom:piwtury:thumv:url
ynx
xyz h_supiwturyi
íroom:piwturyi
ynx
ynx
” template de quartos Xapp/views/rooms/_room.html.erbY￿ca assimk
>_rtiwly wl_ssh*room*-
:::
>xiv wl_ssh*roomçxyswription*-
<%= linkuto{
im_0yut_0{room:thumvuurl}c
room:piwturyuurl
} iz room:h_supiwturyi %>
>p-<%= hi0hli0ht{room:xyswription || ''c ísy_rwhuquyry} %> >,p-
>,xiv-
:::
>,_rtiwly-
” tÉÉ para a imagem de quartos Xapp/assets/stylesheets/room.css.scssY
ék
:roomçxyswription {
pc im0 {
zlo_t4 lyztg
m_r0inçri0ht4 $dpxg
}
}
:roomçxyswription ] ul {
p_xxin0çtop4 $dpxg
￿￿￿

## Página 274

￿￿_￿_ toloque a aplicação no ar com o yeroku tasa do tódigo
wly_r4 vothg
}
ﬀt voilàQ”s quartos agora possuem fotok
wigura￿￿_￿k®uarto com uma foto
￿￿n￿ õ ￿￿￿￿￿￿ ￿ ￿￿￿￿￿￿￿￿￿ ￿￿ ￿￿ ￿￿￿ ￿ H￿￿￿￿￿
rntigamente\ colocar um aplicativo web no ar era complicado e exigia bastante co]
nhecimento de con￿guração de servidor_ yoje em dia\ contudo\ existem serviços
que oferecem hospedagem de aplicativos sem a noção de termos um servidor_Plato
form as a service o PaaS\ ou “ølataforma como serviço”\é uma das facetas de íloud
íomputing \na qual um usuário contrata uma plataforma e poder de processamento\
ao invés de contratar servidores\ sejam de metal ou virtual_
ám desses serviços é o yeroku Xwww_heroku_comY_•ão existe forma mais fácil
de colocar uma aplicação Áails no ar do que usar o yeroku_ øor isso\vamos usá]loké
de graça para pouco processamento de requisição X￿requisição por segundoY\que é
o bastante para nossa aplicação_rntes de continuar\crie sua conta no site\é bastante
simples_
Preparando a aplicação para o Heroku
É necessário fazer algumas alterações no aplicativo para tornar compatível com
o serviçoko yeroku funciona com øostgreÉ®“ e estamos usando o É®“ite ￿_øor esse
￿￿￿

## Página 275

tasa do tódigo tapítulo ￿￿_ øolindo o tolcho_net
motivo\é necessário colocar a gem pg no Gemfile\responsável pela conectividade
a bancos øostgreÉ®“ e alterar uma consulta É®“_ ørimeiro\ vamos a alteração do
Gemfile e execute bundle em seguidak
@ 0ym 'sqlityé'
0ym 'p0'
ã vunxly
:::
onst_llin0 p0 {d:$ê:$} with n_tivy yxtynsions
:::
âam o sagora alterar a consulta É®“ problemáticak no øostgreÉ®“\ a consulta
LIKE é sensível a maiúsculas e minúsculas\ enquanto a ILIKE não_âam o salterar
o método Room.search Xapp/models/room.rbYpara usar a nova consultak
wl_ss +oom > jwtivy+yworx44k_sy
@ :::
xyz sylz:sy_rwh{quyry}
iz quyry:prysynti
whyry{/'low_tion oõo1m 4quyry )+
titly oõo1m 4quyry )+
xyswription oõo1m 4quyry'c quyry4 *b@{quyry}b*3}
ylsy
swopyx
ynx
ynx
@ :::
ynx
Desenvolvimento usando PostgreSQL
znfelizmente esse comportamento do LIKE vs_ ILIKE é incompatível no É®]
“ite_ øor isso\pode ser interessante desenvolver diretamente no øostgreÉ®“_
Ée você usa “inux\ veri￿que os pacotes de sua distribuição_ue preferência\ins]
tale uma versão igual ou superior a ￿_ •o ”É ã\ para usuários de ￿￿_￿ X“ionYou
superior\você já tem o øostgreÉ®“_ øara àindows\ você pode usar o instalador do
site o￿cialkhttpk‘‘postgresql_org_
￿￿￿

## Página 276

￿￿_￿_ toloque a aplicação no ar com o yeroku tasa do tódigo
vm seguida\ altere a parte development e test do arquivo
config/database.yml para re￿etir as alterações_ •ão é necessário ter
production\ ele será criado pelo próprio yeroku_ âe j ao exemplo de como deve
￿car o arquivo\lembrando de trocar vinibaggio pelo seu usuário de sistemak
xyvylopmynt4
_x_ptyr4 post0rysql
x_t_v_sy4 wolwhonytuxyv
host4 low_lhost
usyrn_my4 viniv_00io
p_ssworx4
pool4 8
timyout4 8ddd
tyst4
_x_ptyr4 post0rysql
x_t_v_sy4 wolwhonytutyst
host4 low_lhost
usyrn_my4 viniv_00io
p_ssworx4
pool4 8
timyout4 8ddd
øor ￿m\ executek
ã r_ky xv4wry_ty xv4mi0r_ty
hh lry_ty+ooms4 mi0r_tin0 hhhhhhhhhhhhhhhhhhhhh
çç wry_tyut_vly{4rooms}
:::
hh jxx%iwtury?o+ooms4 mi0r_tin0 hhhhhhhhhhhhhhh
çç _xxuwolumn{4roomsc 4piwturyc 4strin0}
ç- d:dd$$s
hh jxx%iwtury?o+ooms4 mi0r_tyx {d:dd$es} hhhhhh
õolocando a aplicação no ar
øara começar a usar o yeroku\ é necessário instalar o git\ criar uma conta no
yeroku e baixar o yeroku Ío ol s _áma vez com tudo instalado\ basta ir na pasta do
projeto\e criar um repositório git e fazer um commitk
ã 0it init :
oniti_lizyx ympty 9it rypository in ,vook,woxy,wolwhonyt,:0it,
￿￿￿

## Página 277

tasa do tódigo tapítulo ￿￿_ øolindo o tolcho_net
ã 0it _xx :
ã 0it wommit çm *%rimyiro wommit*
/m_styr {rootçwommit} _eyxêvy3 %rimyiro wommit
$d= zilys wh_n0yxc é$=5 insyrtions{]}
wry_ty moxy $dd=êê :0iti0nory
wry_ty moxy $dd=êê 9ymzily
wry_ty moxy $dd=êê 9ymzily:lowk
wry_ty moxy $dd=êê +mj<pm:rxow
:::
O ￿￿￿ ￿ ￿￿￿￿õ ￿￿￿ ￿￿￿￿￿￿￿￿￿
” git é um sistema de versionamento de código]fonte_ Ée você já
ouviu falar em tâÉ\ Éâ• ou –ercurial\ o git é uma ferramenta similar_
øara saber mais\veja o screencast “tome çando com xit” \do wábiorkita\
em httpk‘‘colcho_net‘comecando]com]git_•ele você poderá saber como
funciona o git e como instalá]lo_
áma vez com o commit criado\ vamos usar o heroku tools para criar um
repositório remoto chamado heroku e preparar o nosso novo site_
ã hyroku lo0in
mntyr your #yroku wryxynti_ls:
mm_il4 ;;;í;;;:wom
%_ssworx {typin0 will vy hixxyn}4
juthyntiw_tion suwwysszul:
ã hyroku wry_ty
lry_tin0 w_lmçv_xl_nxsçf=êf::: xonyc st_wk is wyx_r
http4,,w_lmçv_xl_nxsçf=êf:hyroku_pp:wom, |
0itíhyroku:wom4w_lmçv_xl_nxsçf=êf:0it
9it rymoty hyroku _xxyx
ørecisamos adicionar um addoon ao novo site para que possamos entregar os
e]mails de cadastro_âam o susar o –ailgun\ é de graça e possui integração simples
com o yerokuk
￿￿￿

## Página 278

￿￿_￿_ toloque a aplicação no ar com o yeroku tasa do tódigo
ã hyroku _xxons4_xx m_il0un4st_rtyr
jxxin0 m_il0un4st_rtyr on w_lmçv_xl_nxsçf=êf::: xonyc vf {zryy}
"sy ￿hyroku _xxons4xows m_il0un4st_rtyr￿ to viyw xowumynt_tion:
ørecisamos atualizar o ambiente production X
config/environments/production.rbY\ pois é neste ambiente que o
yeroku executa a nossa aplicação_ ørecisamos atualizar as con￿gurações do
ActionMailer para usar a nova áÁ“ do site e as con￿gurações do –ailgun
Xconformevimos na seção ￿_￿Yk
lolwhonyt44jppliw_tion:wonzi0ury xo
@:::
wonzi0:_wtionum_ilyr:xyz_ultuurluoptions h {
host4 *ziyrwyçyvyr0l_xysçe!êê:hyroku_pp:wom*
}
wonzi0:_wtionum_ilyr:xylivyryumythox h 4smtp
wonzi0:_wtionum_ilyr:smtpusyttin0s h {
port4 m(r/'pjoõ9"(uqp?%u%)+?'3c
_xxryss4 m(r/'pjoõ9"(uqp?%uqm+rm+'3c
usyrun_my4 m(r/'pjoõ9"(uqp?%uõ)9o('3c
p_ssworx4 m(r/'pjoõ9"(uqp?%u%jqqs)+<'3c
xom_in4 'ziyrwyçyvyr0l_xysçe!êê:hyroku_pp:wom'c
_uthyntiw_tion4 4pl_inc
}
ynx
rs con￿gurações do –ailgun são colocadas como variáveis de ambiente\ bas]
tante conveniente para não termos que gerenciar chaves de røz_ vm seguida\execute
o seguinte comando\que irá publicar a aplicaçãok
ã 0it push hyroku m_styr
lountin0 ovjywts4 $!ec xony:
<ylt_ wompryssion usin0 up to e thry_xs:
lompryssin0 ovjywts4 $ddb {$é8,$é8}c xony:
sritin0 ovjywts4 $ddb {$!e,$!e}c 5ff:fd 1ik | e=! 1ik,sc xony:
?ot_l $!e {xylt_ ee}c ryusyx $!e {xylt_ ee}
ççççç- +uvy,+_ils _pp xytywtyx
ççççç- "sin0 +uvy vyrsion4 ruvyçe:d:d
￿￿￿

## Página 279

tasa do tódigo tapítulo ￿￿_ øolindo o tolcho_net
:::
ççççç- <iswovyrin0 prowyss typys
%rowzily xywl_rys typys ç- {nony}
<yz_ult typys zor +uvy,+_ils ç- wonsolyc r_kyc wyvc workyr
ççççç- lompilyx slu0 sizy is $e:êpk
ççççç- õ_unwhin0::: xonyc vê
http4,,w_lmçv_xl_nxsçf=êf:hyroku_pp:wom xyployyx to #yroku
?o 0itíhyroku:wom4w_lmçv_xl_nxsçf=êf:0it
[ /nyw vr_nwh3 m_styr ç- m_styr
®uase pronto___øor ￿m\ temos que migrar o banco de dados recém criadok
ã hyroku run r_ky xv4mi0r_ty
+unnin0 ￿r_ky xv4mi0r_ty￿ _tt_whyx to tyrmin_l::: upc run:$
lonnywtin0 to x_t_v_sy spywiziyx vy <j?jkjqmu"+õ
pi0r_tin0 to lry_ty+ooms {ed$ed=$ddê8=df}
:::
uepois que o comando terminar\basta acessar a áÁ“ que você recebeu e já pode
passar para sua família e amigosQ–uito bom\ não é mesmop øarabénsQâo c êcom]
pletou o tolcho_netQ
￿￿￿

## Página 281

t ￿￿￿￿￿￿￿ ￿￿
øróximos passos
égoran isso não é o ￿mpNem sequer é o início do ￿mpMas éntalvezno ￿m do começop
– Éir àinston thurchill
rgora que você já é familiar ao Áails\está na hora de fazer as suas próprias apli]
cações_ Éeria muita pretensão deste livro te ensinar tudo que existe no ecossistema
Áails\portanto\depois da leitura deste livro\ainda é necessário buscar mais material_
Lista de email
Ée você quer tirar alguma dúvida sobre este livro\ você pode se juntar à lista de
emails do livro em httpk‘‘colcho_net‘listae poderá enviar sua pergunta_ ”s parti]
cipantes dela\ incluindo eu\ o autor\ tentarão te ajudar_ “embre]se sempre de ser
educado_
õonhecimentos de Rails
” primeiro lugar que você deve buscar para tirar dúvidas e entender o fun]

## Página 282

tasa do tódigo
cionamento especí￿co de algum componente do Áails são os Áailsxuides Xhttpk
‘‘guides_rubyonrails_orgY_•ele você poderá buscar informações sobre os principais
componentes do Áails\tais como ActiveRecord\ templates\ etc_
Ée sua dúvida for mais especí￿ca\ talvez seja interessante consultar a documen]
tação da røz\ que ￿ca em httpk‘‘api_rubyonrails_org_r documentação é fácil de na]
vegar\bastando que você saiba o método que quer procurar_
Ée você quiser aprender receitas de como resolver certos problemas\o Áyan sa ]
tes\ bastante famoso na comunidade Áails\ faz o Áailstasts Xhttpk‘‘railscasts_comY_
tada screencast é uma receita de como resolver um problema\e o inglês que ele fala
é claro\ sendo uma ótima maneira de aprender_Ée você ainda não está confortável
em entender uma narração em inglês\pode ler os rsciitasts Xhttpk‘‘asciicasts_com‘Y
\ que é praticamente uma transcrição do Áailstasts_
Ée você prefere livros\ terá que aguardar um pouco_ r maioria dos livros para
o Áails ￿ ainda está em seta\ ainda não ￿nalizados\ e todos em inglês_Ée você esti]
ver confortável em comprar um livro ainda em beta\ recomendo o “tra ￿ing Áails ￿
rpplications” Xhttpk‘‘colcho_net‘cra￿ing]rails]appsY_•este livro\ o {osé â alim\ um
dos principais desenvolvedores do próprio framework\ te guia para um mergulho de
cabeça nas profundidades do Áails_øode ser um pouco difícil para iniciantes\mas é
um livro de altíssima qualidade e te dará conhecimento o su￿ciente para conseguir
fazer funcionalidades bem complexas_
Dominando o Ruby
Ée você quer se tornar um desenvolvedor Áuby e Áails pro￿ssional\ recomendo
aprofundar]se na linguagem\ pois é de extrema importante um pro￿ssional conhe]
cer bem as ferramentas que está trabalhando_ –inha recomendação para este ￿m
é o livro de Áuby\da tasa do tódigok httpk‘‘www_casadocodigo_com_br‘products‘
livro]ruby\ totalmente em português_
”utro livro que pode ser interessante é o “vloquent Áuby” \do Áuss ”lsen Xhttpk
‘‘colcho_net‘eloquent]rubyY
Dominando testes
r comunidade Áuby e Áails em geral gosta bastante de testes unitários e ar]
gumentam que esta prática melhora o design de código e ajuda a reduzir o nú]
mero de bugs_ É interessante entender as ideias\ por isso recomendo a leitura
do “Í est]uriven uevelopment” \ do }ent seck Xhttpk‘‘colcho_net‘tddY _ vm se]
￿￿￿

## Página 283

tasa do tódigo tapítulo ￿￿_ øróximos passos
guida\ é interessante ler como Íuu se aplica no Áuby\ com ÁÉpec e tucumber_
vm português\ o meu amigo yugo saraúna está trabalhando no tucumber e Ás]
pec\ publicado pela tasa do tódigo httpk‘‘www_casadocodigo_com_br‘products‘
livro]cucumber]rspec]tdd]bdd _”utro livro interessante\em inglês\ é o “￿e ÁÉpec
sook” Xhttpk‘‘colcho_net‘rspec]bookY_
É difícil no começo\não se preocupe se tiver di￿culdades\ é normal_ám pouco
de perseverança e você poderá sentir os benefícios dessa prática_wiqueà vontade de
mandar perguntas sobre esse assunto na lista de discussões desse livro_
Envolvimento na comunidade
r comunidade rubista brasileira é bastante ativa_ vm Éão øaulo\ por exemplo\
existe o xáÁá]Éø \ porém é possível encontrar outros grupos de Áuby e Áails pelo
srasil e pelo mundo_ørocure as listas de email\ participe e ￿que atento aos encon]
tros\você pode aprender muitoQ•ão deixe de participar também em outros eventos
de programação que existem no srasil\ pois exposição a tecnologias e novas ideias
sempre te ajudarão com qualquer linguagem ou framework_
Open source e leitura de código
r comunidade de Áubye Áails é bastante envolvida em open source e se envolver
em um projeto é uma grande forma de\ além de contribuir\ aprender com outros
desenvolvedores_r leitura de código também é encorajada_áma ótima maneira é
procurar sua gem favorita no xityub Xhttpk‘‘www_github_comYe navegar pelo código
fonte_
￿￿￿

## Página 284

Índice Áemissivo tasa do tódigo
Índice Remissivo
save\￿￿
validp\￿￿
_limit\￿￿
rction–ailer\ ￿￿￿
rction–ailerkksase\ ￿￿￿
rctive–odel\ ￿￿\ ￿￿￿
rctiveÁecord\ ￿
rctiveÉupport\ ￿￿
a￿erúaction\￿￿￿
rrel\ ￿
aroundúaction\￿￿￿
rsset øipeline\ ￿￿￿
backbone_js\￿
strypt\ ￿￿
beforeúaction\￿￿￿
belongsúto\￿￿￿
callbacks\ ￿￿￿
cookies\ ￿￿￿
tÉÁw \￿￿
defaultúlocale\￿￿￿
defaultúscope\￿￿￿
delegate\￿￿￿
emails multipart\￿￿￿
ember_js\￿
vÁs\ ￿￿
execute\ ￿￿￿
￿nders dinâmicos\ ￿￿￿
￿xtures\￿￿
￿ash\ ￿￿
formúfor\￿￿
formútag\ ￿￿￿
from\ ￿￿￿
geradores\￿￿
group\￿￿￿
hasúsecureúpassword\￿￿
having\ ￿￿￿
helpers\ ￿￿￿
z￿￿n\ ￿￿￿
i￿￿n_defaultúlocale\￿￿￿
includes\ ￿￿￿
joins\ ￿￿￿
l\ ￿￿￿
label\ ￿￿
limit\ ￿￿￿\ ￿￿￿
linkúto\￿￿
localize\ ￿￿￿
lock\ ￿￿￿
mass]assignment\￿￿
match\￿￿￿
migração\￿￿
migrações\ ￿￿
￿￿￿

## Página 285

tasa do tódigo Índice Áemissivo
–ât\ ￿
notice\ ￿￿
o￿set\ ￿￿￿
order\￿￿￿
params\ ￿￿
partial\ ￿￿
passwordú￿eld\ ￿￿
permit\ ￿￿
protectúfromúforgery\￿￿
protectedúattributes\￿￿
Áails\￿
readonly\￿￿￿
recurso singleton\ ￿￿￿
redirectúto\￿￿
render\￿￿
reorder\￿￿￿
require\￿￿
requireúself\￿￿￿
requireútree\￿￿￿
ÁvÉÍ \￿
reverseúorder\￿￿￿
rootúpath\￿￿
rotas\ ￿￿
scope\ ￿￿￿\ ￿￿￿
secretútoken\￿￿￿
select\ ￿￿￿
session\ ￿￿￿
Éession yijack\ ￿￿￿
sprockets\￿￿￿
str￿ime\ ￿￿￿
strongúparameters\￿￿
submit\￿￿
textúarea\￿￿
textú￿eld\ ￿￿
textú￿eldútag\ ￿￿￿
try\￿￿￿
updateúattributes\￿￿
validatesúcon￿rmationúof\￿￿
validatesúlengthúof\￿￿
validatesúpresenceúof\￿￿
view helper\￿￿￿
webfonts\￿￿￿
where\ ￿￿￿\ ￿￿￿
￿￿￿

## Página 287

tasa do tódigo Áeferências sibliográ ￿cas
Referências óibliográ ￿ cas
í￿ô uavid ￿omas rndrew yunt_ ￿e Pragmatic Programmer”From Journeyman to
Master_rddison]à esley ørofessional\ ￿￿￿￿_
í￿ô }ent seck_ T estoórivenóevelopment” êy ﬀxample_rddison]à esley ørofessional\
￿￿￿￿_
í￿ô êach uennis rslak yellesøy sryan yelmkamp uan •orth uavid thelimsky\
uave rstels_ ￿e RSpec êook” êehaviouroóriven óevelopment with RSpecníu o
cumbernand Friends_øragmatic sookshelf\ ￿￿￿￿_
í￿ô zan Áobinson {im àebb e r\ Éavas øarastatidis_ Rest in Practice”Hypermedia and
Systems érchitecture _”’Áeilly –edia\ ￿￿￿￿_
í￿ô •ando âieira_ xuia rápido de rspec_httpk‘‘colcho_net‘guia]rspec\ ￿￿￿￿_
￿￿￿