---json
{
  "id": "jogos_em_html5_explore_o_mobile_e_f_sica_-_casa_do_codigo-1",
  "title": "Jogos em HTML5 Explore o mobile e física - Casa do Codigo-1",
  "categoria": "03-linguagens",
  "subcategoria": "go",
  "resumo": "**Arquivo Original:** `Jogos em HTML5 Explore o mobile e física - Casa do Codigo-1.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "casa",
    "codigo",
    "codigo-1",
    "explore",
    "html5",
    "jogos",
    "linguagens",
    "mobile"
  ],
  "perguntas_tipo": [
    "Como utilizar Jogos em HTML5 Explore o mobile e física - Casa do Codigo-1?",
    "Quais as boas praticas de go?"
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
  "dono": "stack-go",
  "prioridade": 2
}
---

# Jogos em HTML5 Explore o mobile e física - Casa do Codigo-1

> **Arquivo Original:** `Jogos em HTML5 Explore o mobile e física - Casa do Codigo-1.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 2

© Casa do Código
T odos os direitos reservados e protegidos pela Lei nº9.610, de
10/02/1998.
Nenhuma parte deste livro poderá ser reproduzida, nem transmitida, sem
autorização prévia por escrito da editora, sejam quais forem os meios:
fotográﬁcos, eletrônicos, mecânicos, gravação ou quaisquer outros.
Casa do Código
Livros para o programador
Rua Vergueiro, 3185 - 8º andar
04101-300 – Vila Mariana – São Paulo – SP – Brasil

## Página 3

CasadoCódigo
Introdução
Estelivroécontinuaçãodeminhaobraanterior, DesenvolvajogoscomHTML5
Canvas e JavaScript([5]). Nela, introduzi a tecnologia Canvas do HTML5
e, principalmente, guiei o leitor pelos conceitos mais básicos envolvidos na
criaçãodejogosem2D:sprites,loopsdeanimação,inputdousuárioeoutros,
semdependerdealgumframeworkespecífico. Agora,paraestenovolivro,eu
assumoquevocêjátenhaesseconhecimentobásico.
Oquenós,vocêeeu,iremosfazeraquiéaprofundarnossoscaminhosem
algumascoisasmaisespecíficas(leia-se frameworks),quesão:
• Apache Cordova: inicialmente chamado PhoneGap, consiste em
uma plataforma para a geração de aplicações HTML5 em diversos sis-
temasoperacionaismóveis(Android,iOS,WindowsPhoneetc.). Uma
mesmabasedecódigo,usandoastecnologiasweb,rodandocomoapps
emtodosessessistemas!
• Hammer.js: biblioteca que detecta gestos comuns em telas sensíveis
ao toque, como pinças, rotações e outros, complementando o suporte
doHTML5.
• Box2dWeb: a fantástica engine de simulação física Box2D, criada em
C++ por Erin Catto, foi portada para inúmeras outras linguagens, in-
c l u s i v e ,c l a r o ,J a v a S c r i p t .E s p e r oq u es óe s t ef a t oj áf a ç av a l e rap e n aa
leituradestelivroparavocê,poiséamesmaAPI(conjuntodeclassese
métodos)paraC++,Java,JavaScripteoutros.
Não que eu pretenda que este livro esteja totalmente amarrado ao
outro mas, para facilitar, vou pegar muitos códigos criados anteriormente e
i

## Página 4

CasadoCódigo
reutilizá-los (aprendi no meu jardim de infância da programação que é para
isto que serve a orientação a objetos). Não se preocupe, caso não tenha lido
a primeira obra. Darei uma recapitulada. Se você não a leu, será como mais
umframeworkzinhoquevocêestáusando.
Olivroestádivididoemduaspartes: MobileeFísica. Naprimeiraparte,
estãooscapítulos:
• 1. Instalação do Apache Cordova:este framework permite trans-
formar páginas HTML em apps para diversos sistemas operacionais
m ó v e i s .A q u ie x p l i c ooq u eéoC o r d o v a ,c o m of u n c i o n aes u ai n s t a -
laçãopassoapasso.Eleseapoiaemmuitosoutrosprogramasquevocê
deveráterinstaladosemsuamáquinadedesenvolvimento.
• 2.Criandooprimeiroprojeto: vocêaprenderátodoociclodecriação
de um app Cordova, desde a configuração do projeto até a geração do
pacoteAPKdoAndroidassinadoparadistribuição.
• 3. Eventostouch: conheceremos a especificação e a API do HTML5
para tratamento de eventos touchscreen. Aprenderemos a verificar as
coordenadas, a cruzá-las com algum objeto no Canvas e como fazer
paraojogadordeslocarspritesarrastando-oscomodedo.
• 4. Incrementandoojogodenave: o jogo de guerra espacial que cri-
amos no primeiro livro ganhará duas versões mobile: na primeira, a
nave será controlada tocando botões na tela; na segunda, o jogador
terá que inclinar o dispositivo móvel na direção em que ele quer que
a nave se mova. Para isso, teremos que fazer a leitura do acelerômetro
doaparelho. TambémconheceremosaAPIdemultimídiadoCordova,
quepermitirá ousode somemaparelhoscuja webviewnativa não su-
portaaAPIdeáudiodoHTML5.
• 5.InteraçõesavançadascomHammer.js: você aprenderá a usar este
frameworkparadetectargestosdepinça,rotação,deslocamentoseout-
ros. Aqui,criaremoscontrolesparamovimentarumtacodebilhar,que
seráusadoemumprojetopráticodejogonasegundapartedolivro.
ii

## Página 5

CasadoCódigo
Nasegundaparte,éfeitaumaintroduçãodosfundamentosdoBox2dWeb
e, em seguida, guio o leitor na construção de um jogo de bilhar, mostrando
como unir a lógica de física com a lógica de negócios e de interação com o
jogador:
• 6.IntroduçãoaoBox2dWeb: conceitosbásicosdestaenginedefísica.
Criaçãodomundofísico,corpos,fixturesegravidade.
• 7. Configuração e movimento de corpos:crie corpos de diversos
formatos, configure sua elasticidade e atrito, aplique forças e impulsos
paramovimentá-los.
• 8. Iniciandoojogodebilhar: construiremos um jogo utilizando a
Box2dWeb para controlar os movimentos com física realista. Progra-
maremos os sprites, posicionaremos as bolas na mesa e simularemos
umatacada,vendo-asseespalharempelocenário.
• 9.I n t e r a ç ã oc o moj o g a d o rel ó g i c a sd en e g ó c i o :incorporamos
ao jogo os controles criados com o Hammer.js e executaremos lógicas
de acordo com os eventos que ocorrerem, como fazer uma bola en-
caçapadadesaparecerouretornaraoseupontoinicial,casosejaabola
branca.
• 10. Simulações internas: usaremos o Box2dWeb puramente em
memóriaparatestardiversasjogadasqueocomputadorpoderealizar.
• 11. Finalizando o jogo: determinaremos qual variedade de bilhar
seráimplementada,eaplicaremossuasregrasparaselecionaramelhor
tacadaa u to má ticaeparaarb i traroandamen todojogo .
O jogo de bilhar pode ser jogado agora mesmo em seu celular ou tablet,
noendereço:
http://gamecursos.com.br/livro2/
iii

## Página 6

CasadoCódigo
Figura1: Jogodebilharaserdesenvolvidonolivro
Procure jogá-lo com o dispositivo móvel na posição paisagem (deitado).
Parajogar:
1) Coloque2dedosnaáreacircularegire
2) Puxeasetaazulpararegularaforça
3) CliquePow!
Vocêdeveacertarabrancanaboladavezindicadanatela;qualvocêen-
caçapaéindiferente. Ganhaojogoquemencaçaparabola9.
Todososcódigos,imagensesonsdejogosdestelivropodemserbaixados
em:
https://github.com/EdyKnopfler/games-js-2/archive/master.zip
OjogodebilharédisponibilizadosobalicençaGNU,nãosendopermi-
tidoousodeseucódigoemaplicaçõescomerciais. Osoutroscódigoseexer-
cíciosestãodisponíveissobalicençaApache,estes,sim,podendoserusados
comercialmente.
Vocêtambémprecisarádosmateriaisdomeulivroanterior:
http://github.com/EdyKnopfler/games-js/archive/master.zip
Continuo à disposição no Google Groups, onde já presto suporte aos
leitores:
http://groups.google.com/forum/#!forum/livro-jogos-html5-canvas
iv

## Página 7

CasadoCódigo
A instalação do Apache Cordova é um bocado trabalhosa. No primeiro
capítulo, tratarei desse assunto exaustivamente. No entanto, reconhecendo a
necessidade de uma demonstração prática para tantos detalhes, gravei uma
rápida videoaula como material complementar, na qual demonstro uma in-
stalaçãodoframeworkemambienteWindows. Acesseovídeoem:
https://www.youtube.com/watch?v=Rf85Y0iNJIE
Prepare-se! Desejo-lhe uma ótima leitura e ainda mais ótimas experiên-
ciasfuturascomaprogramaçãodegames!
v

## Página 9

CasadoCódigo
Introdução
Estelivroécontinuaçãodeminhaobraanterior, DesenvolvajogoscomHTML5
Canvas e JavaScript([5]). Nela, introduzi a tecnologia Canvas do HTML5
e, principalmente, guiei o leitor pelos conceitos mais básicos envolvidos na
criaçãodejogosem2D:sprites,loopsdeanimação,inputdousuárioeoutros,
semdependerdealgumframeworkespecífico. Agora,paraestenovolivro,eu
assumoquevocêjátenhaesseconhecimentobásico.
Oquenós,vocêeeu,iremosfazeraquiéaprofundarnossoscaminhosem
algumascoisasmaisespecíficas(leia-se frameworks),quesão:
• Apache Cordova: inicialmente chamado PhoneGap, consiste em
uma plataforma para a geração de aplicações HTML5 em diversos sis-
temasoperacionaismóveis(Android,iOS,WindowsPhoneetc.). Uma
mesmabasedecódigo,usandoastecnologiasweb,rodandocomoapps
emtodosessessistemas!
• Hammer.js: biblioteca que detecta gestos comuns em telas sensíveis
ao toque, como pinças, rotações e outros, complementando o suporte
doHTML5.
• Box2dWeb: a fantástica engine de simulação física Box2D, criada em
C++ por Erin Catto, foi portada para inúmeras outras linguagens, in-
c l u s i v e ,c l a r o ,J a v a S c r i p t .E s p e r oq u es óe s t ef a t oj áf a ç av a l e rap e n aa
leituradestelivroparavocê,poiséamesmaAPI(conjuntodeclassese
métodos)paraC++,Java,JavaScripteoutros.
Não que eu pretenda que este livro esteja totalmente amarrado ao
outro mas, para facilitar, vou pegar muitos códigos criados anteriormente e
vii

## Página 10

CasadoCódigo
reutilizá-los (aprendi no meu jardim de infância da programação que é para
isto que serve a orientação a objetos). Não se preocupe, caso não tenha lido
a primeira obra. Darei uma recapitulada. Se você não a leu, será como mais
umframeworkzinhoquevocêestáusando.
Olivroestádivididoemduaspartes: MobileeFísica. Naprimeiraparte,
estãooscapítulos:
• 1. Instalação do Apache Cordova:este framework permite trans-
formar páginas HTML em apps para diversos sistemas operacionais
m ó v e i s .A q u ie x p l i c ooq u eéoC o r d o v a ,c o m of u n c i o n aes u ai n s t a -
laçãopassoapasso.Eleseapoiaemmuitosoutrosprogramasquevocê
deveráterinstaladosemsuamáquinadedesenvolvimento.
• 2.Criandooprimeiroprojeto: vocêaprenderátodoociclodecriação
de um app Cordova, desde a configuração do projeto até a geração do
pacoteAPKdoAndroidassinadoparadistribuição.
• 3. Eventostouch: conheceremos a especificação e a API do HTML5
para tratamento de eventos touchscreen. Aprenderemos a verificar as
coordenadas, a cruzá-las com algum objeto no Canvas e como fazer
paraojogadordeslocarspritesarrastando-oscomodedo.
• 4. Incrementandoojogodenave: o jogo de guerra espacial que cri-
amos no primeiro livro ganhará duas versões mobile: na primeira, a
nave será controlada tocando botões na tela; na segunda, o jogador
terá que inclinar o dispositivo móvel na direção em que ele quer que
a nave se mova. Para isso, teremos que fazer a leitura do acelerômetro
doaparelho. TambémconheceremosaAPIdemultimídiadoCordova,
quepermitirá ousode somemaparelhoscuja webviewnativa não su-
portaaAPIdeáudiodoHTML5.
• 5.InteraçõesavançadascomHammer.js: você aprenderá a usar este
frameworkparadetectargestosdepinça,rotação,deslocamentoseout-
ros. Aqui,criaremoscontrolesparamovimentarumtacodebilhar,que
seráusadoemumprojetopráticodejogonasegundapartedolivro.
viii

## Página 11

CasadoCódigo
Nasegundaparte,éfeitaumaintroduçãodosfundamentosdoBox2dWeb
e, em seguida, guio o leitor na construção de um jogo de bilhar, mostrando
como unir a lógica de física com a lógica de negócios e de interação com o
jogador:
• 6.IntroduçãoaoBox2dWeb: conceitosbásicosdestaenginedefísica.
Criaçãodomundofísico,corpos,fixturesegravidade.
• 7. Configuração e movimento de corpos:crie corpos de diversos
formatos, configure sua elasticidade e atrito, aplique forças e impulsos
paramovimentá-los.
• 8. Iniciandoojogodebilhar: construiremos um jogo utilizando a
Box2dWeb para controlar os movimentos com física realista. Progra-
maremos os sprites, posicionaremos as bolas na mesa e simularemos
umatacada,vendo-asseespalharempelocenário.
• 9.I n t e r a ç ã oc o moj o g a d o rel ó g i c a sd en e g ó c i o :incorporamos
ao jogo os controles criados com o Hammer.js e executaremos lógicas
de acordo com os eventos que ocorrerem, como fazer uma bola en-
caçapadadesaparecerouretornaraoseupontoinicial,casosejaabola
branca.
• 10. Simulações internas: usaremos o Box2dWeb puramente em
memóriaparatestardiversasjogadasqueocomputadorpoderealizar.
• 11. Finalizando o jogo: determinaremos qual variedade de bilhar
seráimplementada,eaplicaremossuasregrasparaselecionaramelhor
tacadaa u to má ticaeparaarb i traroandamen todojogo .
O jogo de bilhar pode ser jogado agora mesmo em seu celular ou tablet,
noendereço:
http://gamecursos.com.br/livro2/
ix

## Página 12

CasadoCódigo
Figura2: Jogodebilharaserdesenvolvidonolivro
Procure jogá-lo com o dispositivo móvel na posição paisagem (deitado).
Parajogar:
1) Coloque2dedosnaáreacircularegire
2) Puxeasetaazulpararegularaforça
3) CliquePow!
Vocêdeveacertarabrancanaboladavezindicadanatela;qualvocêen-
caçapaéindiferente. Ganhaojogoquemencaçaparabola9.
Todososcódigos,imagensesonsdejogosdestelivropodemserbaixados
em:
https://github.com/EdyKnopfler/games-js-2/archive/master.zip
OjogodebilharédisponibilizadosobalicençaGNU,nãosendopermi-
tidoousodeseucódigoemaplicaçõescomerciais. Osoutroscódigoseexer-
cíciosestãodisponíveissobalicençaApache,estes,sim,podendoserusados
comercialmente.
Vocêtambémprecisarádosmateriaisdomeulivroanterior:
http://github.com/EdyKnopfler/games-js/archive/master.zip
Continuo à disposição no Google Groups, onde já presto suporte aos
leitores:
http://groups.google.com/forum/#!forum/livro-jogos-html5-canvas
x

## Página 13

CasadoCódigo
A instalação do Apache Cordova é um bocado trabalhosa. No primeiro
capítulo, tratarei desse assunto exaustivamente. No entanto, reconhecendo a
necessidade de uma demonstração prática para tantos detalhes, gravei uma
rápida videoaula como material complementar, na qual demonstro uma in-
stalaçãodoframeworkemambienteWindows. Acesseovídeoem:
https://www.youtube.com/watch?v=Rf85Y0iNJIE
Prepare-se! Desejo-lhe uma ótima leitura e ainda mais ótimas experiên-
ciasfuturascomaprogramaçãodegames!
xi

## Página 15

CasadoCódigo Sumário
Sumário
Mobile 1
1 InstalandooApacheCordova 3
1.1 OqueéoCo r do vaeoquetemaverco moPho neGa p .... 4
1.2 Instalandoosprerrequisitos ................... 4
1.3 Consideraçõesespecíficasdesistemaoperacional ....... 1 1
1.4 Testandoaconexãocomodispositivo ............. 1 5
2 Criandooprimeiroprojeto 17
2.1 O projeto Cordova ......................... 1 7
2.2 Oarquivoconfig.xml ....................... 1 8
2.3 ConfigurandooAndroidparadepuraçãoUSB ........ 2 0
2.4 Rodandooprojetopadrão .................... 2 2
2.5 Umpequenoprojetodozero: animaçãocomoCanvas .... 2 4
2.6 UmpolyfillpararequestAnimationFrame ........... 2 8
2.7 GerarpacoteAPKassinadoparaoAndroid .......... 3 1
2.8 Consideraçõesfinais ........................ 3 5
3 Eventostouch 37
3.1 Arrastandoumobjeto ....................... 3 8
3.2 Controlandoadireção ...................... 4 6
3.3 ToqueemCanvasresponsivo ................... 5 0
xiii

## Página 16

Sumário CasadoCódigo
4 Incrementandoojogodenave 55
4.1 Revisãodasclassesdojogo .................... 5 6
4.2 Esqueletodoprojeto ........................ 5 7
4.3 APIdesomdoCordova ...................... 6 6
4.4 Criandoumcontroledirecional ................. 7 0
4.5 Precisãocommúltiplosdedos .................. 8 0
4.6 APIdoacelerômetrodoCordova ................ 8 3
4.7 A da p tandooCan vasaotamanhodatela ............ 8 8
5 InteraçõesavançadascomHammer.js 93
5.1 ConhecendooHammer.js .................... 9 4
5.2 Barradea justedefo r ça ...................... 1 0 1
5.3 Rotacionandoumtacodebilhar ................. 1 1 0
5.4 Animandoatacada ........................ 1 1 7
Física 123
6 IntroduçãoaoBox2dWeb 125
6.1 Umprimeirotutorial ....................... 1 2 7
6.2 Objetosfundamentais ....................... 1 2 8
6.3 Animaçãodomundofísico .................... 1 3 7
7 Configuraçõesemovimentodecorpos 141
7.1 Formas ............................... 1 4 2
7.2 Movimentandocorpos ...................... 1 5 2
7.3 Propriedadesfísicas ........................ 1 5 6
8 Iniciandoojogodebilhar 161
8.1 Preparaçãodoprojeto ....................... 1 6 2
8.2 Primeirossprites .......................... 1 6 7
8.3 A sbolasdeb ilhar ......................... 1 7 5
8.4 Executandoatacada ........................ 1 8 2
8.5 Ângulodatrajetória ........................ 1 8 6
xiv

## Página 17

CasadoCódigo Sumário
9 Interaçãocomojogadorelógicasdenegócio 191
9.1 Controlesdatacada ........................ 1 9 2
9.2 Execu tandoatacadanoânguloco rr eto ............. 1 9 6
9.3 Posicionandootaco ........................ 1 9 9
9.4 Tratamentodascolisões ...................... 2 0 1
10 Simulaçõesinternas 209
10.1 Realizandováriassimulaçõesapartirdoinício ........ 2 1 0
10.2 Salvandoerecuperandooestadodomundofísico ...... 2 1 3
10.3 Executandoatacadaemtempocurto .............. 2 1 5
10.4 Tratadordecolisõesparaasimulação .............. 2 1 8
11 Finalizandoojogo 223
11.1 RegrasdoBola9 .......................... 2 2 4
11.2 Mostradores ............................ 2 3 4
Conclusão 239
ÍndiceRemissivo 239
Bibliografia 241
xv

## Página 19

ParteI
Mobile

## Página 21

Capítulo1
I nstalandooA pacheCo r do va
Estápreparado? Nestecapítulo,vocêtomarácontatocomoqueeuconsidero
uma das ideias mais brilhantes para o desenvolvimento de software. Tudo o
que foi feito no primeiro livro, rodando em navegadores desktop, se tornará
realidade em dispositivos móveis. Ao longo deste livro, iremos criar versões
móveisdojogodenave,simularpartidasdebilhar,alémdediversosexercícios
comtelastouchefísica.
Preciso avisar-lhe: para isto se tornar realidade, você terá que instalar
várias ferramentas em seu computador. Este primeiro capítulo é dedicado
aensiná-locomofazerisso. Podeserque,comodesenvolvedor,vocêjátenha
uma ou mais delas. Em todo caso, pegue um café e um prato de biscoitos,
ponhaumamúsicarelaxanteevamoscomeçar.

## Página 22

1.1. OqueéoCo r do vaeoquetemaverco moPho neGa p CasadoCódigo
1.1 O que é o Cordova e o que tem a ver com o
PhoneGap
Se eu lhe perguntar: qual plataforma de software roda em qualquer dispos-
itivo moderno, não importando seu tamanho físico, velocidade, memória...
Java? Talvez, mas existe uma outra: a web. Uma página web pode ser criada
para todos os dispositivos imagináveis. Como a tecnologia Canvas faz parte
dopadrãoatualdaweb(HTML5),podemosdizeromesmodejogoscriados
comele.
Por que, portanto, não utilizar as tecnologias da web para desenvolvi-
mentomóvel?
Em 2008, a Nitobi (hoje adquirida pela Adobe) começou a trabalhar
no PhoneGap, um sistema que empacota páginas HTML na forma de apps
para diversas plataformas móveis. Não há mágica: são, na realidade, apli-
caçõeshíbridas,nasquaisocomponentenativoderenderizaçãowebdecada
plataforma é usado para processar o conteúdo em formato web. Sendo apps
nativas,podemserdistribuídasnaslojasdeaplicativoserodarlocalmente.
Em2011,oprojetofoidoadoàFundaçãoApache,ondepassouachamar-
se Cordova. A Adobe adquiriu a Nitobi logo em seguida e deu foco especial
àmanutençãodoprojeto ,passandoaoferecerumserviçodegeraçãodeapps
em nuvem, oAdobe PhoneGap Build(https://build.phonegap.com/),m a n -
tendo o nome original. Este serviço, no entanto, é oferecido gratuitamente
apenas para projetos de código livre. Por esta razão é que dou preferência,
nestelivro,àinstalaçãolocaldabibliotecabase.
Mas não se engane: não se trata apenas de um simples renderizador. A
WebViewpadrão de cada plataforma é estendida com APIs JavaScript para
acessoadiversosrecursosdosdispositivos,comotelefone,contatos,câmera,
acelerômetro, GPS, sistema de arquivos e outros. Enfim, uma plataforma
completa para desenvolvimento de apps, tendo como base mas não se limi-
tando aoformatoweb.
1.2 Instalandoosprerrequisitos
A partir da versão 3.0, o Cordova traz uma interface de linha de comando,
aCordova CLI (Command Line Interface). É muito prática de se usar, porém
4

## Página 23

CasadoCódigo Ca p í tulo1. I nstalandooA pacheCo r do va
utilizainternamentediversasoutrasferramentasconhecidaspordesenvolve-
doresdesoftware.
Aseguir,asferramentas,seuslinksparadownloa deodevidopo r quê.
Node.js
http://nodejs.org/download
Engine de execução de código JavaScript, sobre a qual a CLI roda. Esta
será instalada como um plugin do Node.js. A CLI, em si, é uma aplicação
JavaScriptdoNode.js.
Para Windows e Mac OS X são fornecidos instaladores. No Linux, você
deveextrairoarquivocompactadoparaolocaldesuapreferênciaeconfigurar
o path de seu sistema (mais detalhes na seção1.3) para enxergar a subpasta
bin,o ndeseenco n traoexecu tá veldoN ode.jseou tili tárionpm.
Figura1.1: OpçõesdedownloaddoNode.js
OnpmserveparabaixarextensõesdoNode.js,dasquaisum aéoCordova
CLI.Parainstalá-lo,digiteoseguinteemumterminaloupromptdecomando:
5

## Página 24

1.2. Instalandoosprerrequisitos CasadoCódigo
Nesteponto,oCordovaCLIestáinstalado,masaindatemostrabalhoaté
podergerarumappparaumadeterminadaplataforma.
ApacheAnt
http://ant.apache.org/bindownload.cgi(sim,é“bindownload”tudojunto)
FerramentadeautomaçãobemconhecidapordesenvolvedoresJava,ére-
querida pela CLI na hora de gerar projetos Android nativos. Se esta ferra-
mentanãoestiverinstalada,vocêverámensagensdeerronahoradeadicionar
aplataformaAndroidaoseuprojetoCordova.
Váaoendereçoindicadoeroleapáginaparaencontraroslinksdaversão
atual(CurrentReleaseofAnt ). Vocênovamenteteráqueextrairosarquivose
configurarasubpasta
binnopathdoseusistema.
Figura1.2: OpçõesdedownloaddoApacheAnt
Git
http://git-scm.com/downloads
Apartirdaversão3.0,asdiferentesAPIsdoCordovaforamquebradasem
plugins, quedevemserbaixadose instaladosnosdevidosprojetos. Quem se
encarregadessesdownloadséoGit,conhecidaferramentadegerenciamento
derepositórios(comooGitHub). OCordovatambémcuidadechamá-lono
mo men todainstalaçãodeumpl ugin.
6

## Página 25

CasadoCódigo Ca p í tulo1. I nstalandooA pacheCo r do va
SDKs
• Android (requer Java SDK): primeiro http://www.oracle.
com/technetwork/pt/java/javase/downloads, depois http:
//developer.android.com/sdk/
• iOS: http://developer.apple.com/programs/ios/
• WindowsPhone: http://developer.windowsphone.com/
SoftwareDevelopmentKits dasdiversasplataformas,usadosparacompilar
os componentes nativos. Estes são só alguns exemplos, veja a lista completa
em http://goo.gl/NkIfhK. Vou dar o exemplo da configuração de um ambi-
enteAndroid,masqueroquevocêtenhaemmentequeestelinktrazdetalhes
sobreaconfiguraçãoemcadaplataformasuportadapeloCordova.
Ou seja, não há nenhuma mágica: se o Cordova é capaz de gerar apps
para diversas plataformas, é porque foi criada a comunicação com cada um
dos SDKs nativos. Você pode instalar todos, ou somente aqueles que deseja
usar. Nestelivro,focareinoAndroid.
OAndroidSDKrequeroSDKdaplataformaJava(OracleJDK)parafun-
cionar. Programadores Java já o têm instalado no computador; se não é o
seucaso,dirija-seàprimeiraURLindicadaeroleatelaparaencontraroJDK
7. Infelizmente,enquantoescrevoestelivro,aplataformaAndroidaindanão
su po rtaoJ a va8.
7

## Página 26

1.2. Instalandoosprerrequisitos CasadoCódigo
Figura1.3: DownloaddoJDK7
Após instalado o JDK, você deve configurar a variável de ambiente
JAVA_HOME (1.3), apontando para a pasta onde ele está instalado, por exem-
plo: C:\Program Files\Java\jdk1.7.0 .
O SDK do Android em si pode ser baixado de duas formas: ADT
Bundle e stand-alone. Para desenvolvimento com o Cordova CLI, us-
aremos o stand-alone (se você já desenvolve para Android com o ADT,
não precisa baixar, pode usar a SDK integrada). Para baixá-lo, clique no
link
Get the SDK for an existing IDE eemseguidaem Download
the stand-alone ... .
8

## Página 27

CasadoCódigo Ca p í tulo1. I nstalandooA pacheCo r do va
Figura1.4: DownloaddoAndroidSDK
Após instalar o Android SDK, configure no path as subpastastools e
platform-tools(estaúltimaaindaaserinstalada). Inicieumterminalou
promptdecomando(noWindows,comoadministrador)edigite:
Será aberto oSDK Manager, onde você terá que fazer o download dos
itensmarcadosnasfiguras 1.5e1.6:Platform-tools,Build-toolseSDKPlatform
daAPI19doAndr o id:
Figura1.5: FerramentasdebuilddoAndroidSDK:toolseplatform-tools
9

## Página 28

1.2. Instalandoosprerrequisitos CasadoCódigo
Figura1.6: APIAndroidmaisrecente(marqueaSDKPlatform)
APIsAndroid
No momento em que finalizo este livro, o Cordova não dá suporte à
API 20 do Android. Você pode tentar posteriormente atualizar o Cor-
dovaeverificarqualSDKPlatformeleestásuportando.
Emuladoresvs.dispositivosreais
O Android SDK possui um emulador. Para usá-lo, você deve insta-
lar pelo menos umaSystem Imagede uma determinada API no SDK
Manager (há uma instalada na figura1.6). No entanto, o emulador é
muito lento. Pode ter desempenho aceitável para testar apps comuns,
emmáquinascomprocessadoresrápidosebastantememória.
Nocasodejogos,procureutilizarumdispositivorealparatestá-los.
10

## Página 29

CasadoCódigo Ca p í tulo1. I nstalandooA pacheCo r do va
1.3 Considerações específicas de sistema op-
eracional
Windows
Para testar jogos em dispositivos conectados no Windows, é preciso instalar
um driver USB. Há uma lista emhttp://developer.android.com/tools/extras/
oem-usb.html#Drivers. Apósinstalarodriver,procurereiniciaramáquina.
Muito provavelmente você sabe como configurar o path do sistema op-
eracionaloucriaravariáveldeambiente JAVA_HOME,noentanto,deixoaqui
registradosospassos:
• Clique com o botão direito em Computador ee s c o l h a
Propriedades.
• À esquerda da tela, escolha Configurações Avançadas do
Sistema.
• Cliquenobotão Variáveis de Ambiente .
11

## Página 30

1.3. Consideraçõesespecíficasdesistemaoperacional CasadoCódigo
Figura1.7: EntrandonasvariáveisdeambientedoWindows
Paraacrescentarumapastaaopath:
• Procureemumadaslistasavariável PATHecliqueem Editar.
• Acrescenteumpontoevírgulaaofinaldoscaminhoseinsiraonovo.
12

## Página 31

CasadoCódigo Ca p í tulo1. I nstalandooA pacheCo r do va
Figura1.8: Acrescentandoumapastanopath(ApacheAnt,noexemplo)
Linux
No Linux, é preciso configurar uma permissão de acesso via USB para
aparelhosdedeterminadofabricante:
• ConecteseudispositivoaocomputadorpelocaboUSB.
• Abra o terminal e digite o comandolsusb. Procure na saída do co-
mando o seu dispositivo e anote o primeiro código hexadecimal. Ele
correspondeaocódigodofabricante:
13

## Página 32

1.3. Consideraçõesespecíficasdesistemaoperacional CasadoCódigo
Figura1.9: Encontrandoocódigodofabricante(odaMotorolaé22b8)
• Editecomoadministradoroarquivo:
• Insiraalinha(podeseraofinaldoarquivo,casoelejáexista):
Istodefineumaregradandoaosistemaapermissãodeacessoaosdispos-
itivosdaquelefabricante.
• Mudeapermissãodoarquivopara 644:
No caso, o 6 representa as permissões de leitura e gravação (4 + 2) ao
usuário corrente (que é o administrador, devido ao uso dosudo); o 4, a
permissão de leitura para o grupo a que o usuário pertence; e o outro 4, a
permissãodeleituraaosoutrosusuários.
• Mudeoproprietáriodoarquivoparaoadministrador(root):
As variáveis de ambiente podem ser configuradas editando-se como ad-
ministradoroseguintearquivo(ereiniciandoamáquinadepois):
14

## Página 33

CasadoCódigo Ca p í tulo1. I nstalandooA pacheCo r do va
AocontráriodoWindows,osdiretóriossãoseparadospordois-pontos:
Figura1.10: ConfiguraçãodepatheJAVA_HOMEnoLinux. Cadapathcon-
figuradomanualmenteédestacadocomumacor,parafacilitaravisualização
Apósrealizartodasasedições,reinicieamáquina.
1.4 Testandoaconexãocomodispositivo
Em qualquer caso (Windows ou Linux), podemos testar se o SDK consegue
“conversar”comocelularoutablet.
Abra um prompt de comando ou terminal e dê o comando
adb
devices.EsteéumcomandodoAndroidSDKquelistaosaparelhosconec-
tados:
Figura1.11: Dispositivosconectados
15

## Página 34

1.4. Testandoaconexãocomodispositivo CasadoCódigo
Se aparecerem vários pontos de interrogação ou a indicação “no permis-
sions”, confira os passos citados para seu sistema operacional. Mais detalhes
podemserobtidosem http://developer.android.com/tools/device.html,eem
http://goo.gl/42Xilapodemos ver uma descrição detalhada de como config-
uraroacessoaodispositivomóvelnoLinux.
Se seu dispositivo aparece como “device” após o comando adb
devices, abra uma cerveja! Estamos prontos para finalmente começar a
usaroApacheCordova. Játemosasferramentasnecessáriasparatrazerpara
o mundo mobile todas as experiências que somos capazes de criar com o
HTML5. Para dar continuação ao processo, já no próximo capítulo, você
aprenderá a criar projetos e rodá-los em seu celular ou tablet, e poderá ver
animações em Canvas funcionando. Em breve nossos esforços se transfor-
marãoemjogosreaisedivertidos.
Sugestãodeleitura
Apache Cordova 3 Programming,deJ ohnM.W argo([3]).
16

## Página 35

Capítulo2
Criandooprimeiroprojeto
Éhoradetiraraprovadosnove: vamosusarainterfacedelinhadecomando
(CLI)doCordovaparacriarumpequenoprojetoHTML5. Sealgodererrado,
certifique-se deque todas asferramentas instaladasestejam configuradas no
pathdosistema,conformedescritoexaustivamentenocapítuloanterior.
2.1 OprojetoCordova
NoPromptdeComandodoWindows,ounoTerminaldoLinux,navegueaté
apastaondevocêpretendesalvaroscó digosdestelivro. Estandonessapasta,
dêocomando:
cordova create primeiro
OCordovacriaapasta primeirodentrodaatual. Vamosabri-la:

## Página 36

2.2. Oarquivoconfig.xml CasadoCódigo
Os próximos comandos atuarão no projeto configurado nesta pasta. Va-
mosadicionaraplataformaAndroid:
Vale a pena darmos uma olhada na estrutura de pastas do projeto.
Destaqueparaoarquivo config.xml,aserdescritonapróximaseção,para
ap a s t awww,o n d efi c aop r o j e t ow e b ,eplatforms,o n d eoC o r d o v ac r i a
projetosnativosparaosSDKsdasplataformasadicionadas:
Figura2.1: EstruturadepastasdeumprojetoCordova
Nosso trabalho será praticamente todo feito na pastawww,p o i sél áq u e
deverãosersalvososarquivosHTML,CSSeJavaScriptdenossosappsejogos.
Recomenda-senãoeditardiretamenteoconteúdodapasta platforms,pois
este é sempre re-gerado automaticamente a cada execução do projeto. Nada
impede, porém, que copiemos o projeto Android nativo para outro local e o
oabramosnoADT,porexemplo.
2.2 Oarquivoconfig.xml
Nestearquivo,configuramosalgumaspropriedadesdoprojetousadasnager-
ação da app nativa. Destaque para o atributo
id da tag <widget>,o n d e
definimos opacote, nome que identificará nosso app de forma exclusiva.
Editei o arquivo como a seguir; sinta-se livre para colocar os seus próprios
dados:
18

## Página 37

CasadoCódigo Ca p í tulo2. Criandoop rimeir op r o jeto
<?xml version= ' 1.0 ' encoding= ' utf-8 ' ?>
<widget id="br.com.casadocodigo.livrojogoshtml2.primeiro"
version="0.0.1"
xmlns="http://www.w3.org/ns/widgets"
xmlns:cdv="http://cordova.apache.org/ns/1.0" >
<name>Primeiro Projeto Cordova</name>
<description>
Primeiro teste de empacotamento de páginas HTML
em apps móveis.
</description>
<author email="ederson_cassio@yahoo.com.br"
href="http://gamecursos.com.br">
Éderson Cássio
</author>
<content src= "index.html" />
<access origin="*" />
</widget>
Uma vez publicado o app na Play Store, o nome do pacote não de-
verá mais mudar. A convenção, já conhecida por programadores Java,
é usar a URL reversa, colocando ao final o nome que identifica o app
ou jogo. Por exemplo:
br.com.casadocodigo.livrojogoshtml2,
onde br.com.casadocodigo corresponderia ao seu URL na web, e
livrojogoshtml2 identifica este livro. Vamos continuar colocando mais
pontosenovosnomes,paraidentificarcadajoguinhocriadoaqui.
19

## Página 38

2.3. ConfigurandooAndroidparadepuraçãoUSB CasadoCódigo
Íconedoaplicativo
No config.xmlvocêpodedefiniroíconedeumaplicativoatravés
datag <icon>:
<icon src="res/icon.png" />
Maisdetalhespodemserobtidosem http://goo.gl/Q6Nmz3.
2.3 Configurando o Android para depuração
USB
SevocêjádesenvolveparaAndroid,sinta-selivreparapularestaparte.
Por razões de segurança, não se pode sair copiando aplicativos para os
aparelhos. Paradesenvolvimento,temosquehabilitara DepuraçãoUSB:
• Procurenasconfiguraçõesdeseuaparelhoaopção Desenvolvedor
ou Programador,co nfo rmeomodelo .
Habilitando as opções de desenvolvedor no Android
4.2eposteriores
A partir do Android 4.2, a opção Desenvolvedor das
Configurações estáoculta. Parafazê-laaparecer,entreem Sobre o
telefone, nas configurações, e toque sete vezes a opçãoNúmero da
versão(figura2.2).
• HabiliteomododesenvolvedoreadepuraçãoUSB(figura 2.3).
20

## Página 39

CasadoCódigo Ca p í tulo2. Criandoop rimeir op r o jeto
Figura2.2: HabilitandoasopçõesdedesenvolvedorapartirdoAndroid4.2
21

## Página 40

2.4. Rodandooprojetopadrão CasadoCódigo
Figura2.3: HabilitandoadepuraçãoUSB
2.4 Rodandooprojetopadrão
O Cordova já inseriu alguns arquivos na pastawww. Vamos rodar o projeto
paranoscertificarmosdequeestátudook.
• Conecte o aparelho. A partir do Android 4.2.2, a cada computador
diferente conectado, aparecerá no display um pedido de autorização
paraumachaveRSAespecíficaparaaquelecomputador:
22

## Página 41

CasadoCódigo Ca p í tulo2. Criandoop rimeir op r o jeto
Figura2.4: ConfirmaçãoparadepuraçãoUSBapartirdoAndroid4.4.2
• A b raop r o m p to uterminaleen tr enapastadeseup r o jeto:
cd primeiro
• Mande rodar o projeto:
cordova run android
O primeiro build leva alguns minutos. Se tudo estiver ok e o Android
SDKconseguircomunicar-secomodispositivo,vocêveránoterminalamen-
sagem LAUNCH SUCCESS eoprojetopadrãodoCordovarodandonodisplay.
Nestaaltura,comoforammuitasconfigurações,podeserqueocorramerros.
Certifique-sedequetodasasferramentasutilizadaspeloCordovalistadasna
seção 1.2tenham sido instaladas, reveja as considerações sobre os sistemas
operacionais (1.3) e garanta que os paths estejam devidamente configurados,
conformeafigura 1.10. Podeserque,apósalgumainstalaçãoouconfiguração,
sejaprecisoreiniciarocomputador.
23

## Página 42

2.5. Umpequenoprojetodozero: animaçãocomoCanvas CasadoCódigo
Figura2.5: ProjetopadrãodoCordovarodandonodispositivomóvel
2.5 Umpequenoprojetodozero: animaçãocom
oCanvas
Apáginainicial
Vamos apagar os arquivos presentes na pastawww ec o m e ç a rr e c r i a n d oo
index.html. Esterepresentaapáginainicialdoprojeto. Noteastags <meta
name="viewport"...>e <script src="cordova.js"> :
<!DOCTYPE html>
<html>
<head>
<meta charset= "utf-8">
<title>Primeiro Projeto </title>
<meta name="viewport"
content="width=device-width, height=device-height,
user-scalable=no, initial-scale=1,
maximum-scale=1, minimum-scale=1" >
<script src="cordova.js"></script>
<script>
// Aqui vai nosso tratamento do Canvas
</script>
24

## Página 43

CasadoCódigo Ca p í tulo2. Criandoop rimeir op r o jeto
Oviewport éconhecidodequemjátrabalhacomwebdesignresponsivo.
Trata-sedotamanhodoconteúdo. Senãoestiverdefinido,odispositivotrata
a página como sendo para desktop, com um viewport maior que 900 pixels
(o valor padrão varia entre os dispositivos), como uma forma de lidar com
páginasnãopreparadasparaastelaspequenas. Éporissoquevemosmuitos
sites totalmente comprimidos na minúscula tela e temos que fazer a pinça
(zoom)atodomomento:
Figura 2.6: Um site para desktop aparece minúsculo no dispositivo móvel
(imagemeditadaparasuprimiranúncios)
Em nosso caso, os atributos
width=device-width e
height=device-height estão definindo as dimensões do viewport
notamanhoreportadopeloaparelho. Osatributosusadossão:
• width: larguradoviewport;
• height: alturadoviewport;
25

## Página 44

2.5. Umpequenoprojetodozero: animaçãocomoCanvas CasadoCódigo
• user-scalable: define se o usuário pode dar zoom. Para jogos, em
muitos casos é interessante setar comono (sem zoom), mas isso de-
penderádascaracterísticasdojogo;
• initial-scale: zoominicial. Ovalor 1defineozoom“normal”(100%).
Valores abaixo (ex.:0.5) reduzem a visão da página, e valores acima
(ex.: 2)ampliam;
• maximum-scale: zoommáximopermitido;
• minimum-scale: zoommínimopermitido.
Definimosaquicaracterísticasbastanterestritivasparaozoom. Parasites,
istoétotalmentecontraosbonsprincípiosdeusabilidade,masaquiestamos
falando de jogos (ou apps) em geral. Nesses casos, permitir ou não o zoom,
emquequantidadeeemquesituações,sãodecisõesdoprojeto.
T emostambémoscript
cordova.js,cujoarquivo... nãoexistenopro-
jeto! Ele estará acessível somente no webview do Cordova. Enquanto não
usarmos nenhuma API específica do Cordova, poderemos até mesmo testar
nosso jogo no browser do desktop e ignorar este arquivo. Porém, a partir
do momento em que chamamos APIs do Cordova, estas só rodarão em seu
ambiente,esópoderemostestá-lascomumaparelhomóvelouemulador.
IniciandoaAPI
Para aguardar a página carregar no navegador, nós fazemos o seguinte
script(podeincluí-lonatag <script>vazia):
window.onload = function() {
// Nosso código de inicialização
}
No Cordova, ainda temos de aguardar o carregamento de suas APIs. O
amb ien tenosfo rneceoeven todeviceready:
window.onload = function() {
document.addEventListener( ' deviceready ' , iniciar);
}
26

## Página 45

CasadoCódigo Ca p í tulo2. Criandoop rimeir op r o jeto
function iniciar() {
// Nosso código de inicialização
}
Mas não temos esse evento no browser, caso queiramos testar. Bastaria
chamarafunção iniciardiretamentenoevento onload:
//document.addEventListener( ' deviceready ' , iniciar);
iniciar();
QuandonãoestamosusandoAPIsmóveisespecíficas,issopodenosper-
mitir depurar melhor o jogo (através do console do Google Chrome ou do
plugin Firebug do Firefox, por exemplo). Lógicas de Canvas ou de engines
físicas(comoaBox2dWeb,queaprenderemosnaParte2dolivro)nãoneces-
sitam necessariamente de dispositivos móveis para rodar e podem ser depu-
radas em ambiente desktop. Entradas simples via teclado ou mouse podem
serusadasparasimulareventoschaveaseremtestados.
E vamos para a inicialização: obtenção do Canvas e seu contexto grá-
fico, disparo do loop de animação... Façamos algo básico e conhecido por
enquanto,ocomplexoproblemamatemáticoda bolinhaquicando:
var canvas, context;
var x, y, raio =1 0 ;
var vX =1 0 ,v Y= -20; // Velocidades
window.onload = function() {
//document.addEventListener( ' deviceready ' , iniciar);
iniciar();
}
function iniciar() {
canvas = document .getElementById( ' primeiro ' );
context = canvas.getContext( ' 2d ' );
// Começar no meio da tela
x = canvas.width /2 ;
y = canvas.height /2 ;
27

## Página 46

2.6. UmpolyfillpararequestAnimationFrame CasadoCódigo
requestAnimationFrame(animar);
}
Estamos disparando um loop de animação com a funçãoanimar,p o r -
tantovamoscriá-la:
function animar() {
// Não deixar passar das bordas
/ /C o m oxeys ã oo centro, descontamos o raio
// Se passou do limite, invertemos o sentido da velocidade
if (x < raio || x > canvas.width - raio)
vX *= -1;
if (y < raio || y > canvas.height - raio)
vY *= -1;
x += vX;
y += vY;
context.clearRect(0, 0, canvas.width, canvas.height);
context.beginPath();
context.arc(x, y, raio, 0, Math.PI*2);
context.fill();
requestAnimationFrame(animar);
}
Seabrirmosapáginanobrowser,jáveremosabolinhaquicando. Nocelu-
lar ou tablet, pode ser que sim, pode ser que não. Por quê? Veja na próxima
seção.
2.6 UmpolyfillpararequestAnimationFrame
O suporte para o requestAnimationFrame em dispositivos móveis é
bem recente. O browser do Android somente o aceita a partir da versão 4.4
(http://caniuse.com/requestanimationframe) ! Um jogo hospedado na web,
28

## Página 47

CasadoCódigo Ca p í tulo2. Criandoop rimeir op r o jeto
acessado pelo Chrome ou Firefox devidamente atualizados, pode rodar nor-
malmente. As aplicações Cordova, no entanto, usam o webview padrão do
sistema operacional. No Safari do iOS, o suporte já existia há algumas ver-
sõesatrás,mastambémérecente.
Nessescasos,asoluçãoéusarum polyfill: umaimplementaçãoJavaScript
que tenta emular o comportamento de uma funcionalidade recente e ainda
não completamente suportada. No caso do
requestAnimationFrame,o
velho setTimeoutpodeserusadoparaconstruirumpolyfill.
Um exemplo simples poderia ser como o mostrado a seguir. Primeiro
checamos a existência, por ordem deprioridade, da especificação padrão
requestAnimationFrame ou das versões prefixadas comwebkit, moz
ou ms(específicasdenavegador,dequandonãotínhamosumaespecificação
definida). Usamos para isso oou lógico( ||), que fará retornar a primeira
referência que for diferente denull. Caso nenhuma delas exista (todas
null),retornamosumafunçãoconstruídausandoo setTimeout,quetenta
simular60framesporsegundo:
window.requestAnimationFrame =
// Especificação padrão
window.requestAnimationFrame ||
// Chrome, Safari e outros
window.webkitRequestAnimationFrame ||
// Firefox
window.mozRequestAnimationFrame ||
// IE
window.msRequestAnimationFrame ||
// Função substituta
function(callback) {
window.setTimeout(callback, 1000 / 60 );
};
Dividindo1segundo(1000ms)por60,nossopolyfilltentaráchegarperto
dos60fps,tantoquantoaprecisãodo setTimeoutpermitir. Issofoisóuma
formamaiscompactadesefazer:
// Exemplo teórico
var funcao;
29

## Página 48

2.6. UmpolyfillpararequestAnimationFrame CasadoCódigo
if (window.requestAnimationFrame)
funcao = window.requestAnimationFrame;
else if ( ... ) // etc.
window.requestAnimationFrame = funcao;
ErikMöller,alemãovice-diretordaWikimediaFoundationedesenvolve-
dor, criou um polyfill bastante robusto, que pode ser obtido emhttps://gist.
github.com/paulirish/1579671.E s t ep o l y fi l lm e d eot e m p oe n t r eof r a m ea n -
terior e o atual, e desconta o atraso para a próxima chamada. Salve o código
dopolyfillnapasta wwwefaçaolinkco mapáginanaseção <head>:
<script src="rAF.js"></script>
Etr oqueachamadaàfunção iniciar:
document.addEventListener( ' deviceready ' , iniciar);
//iniciar();
Agoravocêpodefazernovamente:
cordova run android
AanimaçãofuncionaráemqualqueraparelhoAndroid.
Figura 2.7: Animação com Canvas e requestAnimationFrame na forma de
app Android
30

## Página 49

CasadoCódigo Ca p í tulo2. Criandoop rimeir op r o jeto
2.7 GerarpacoteAPKassinadoparaoAndroid
Hora de gerar os arquivos.apk, os pacotes de aplicativos Android. Estes
pacotesdevemserassinadosparaquepossamserpublicadosnaPlayStoreou
instaladosdiretamentenosaparelhos.
Gerandoumachavedeassinatura
Primeiro devemos gerar uma chave de assinatura, usando o co-
mando keytool,p r e s e n t en aJ D K .E s t ac h a v es e r ás a l v ae mu ma r q u i v o
.keystore,quepodeconterumaoumaischaves. Sigaospassos:
• Abra o terminal ou prompt em uma pasta separada do projeto (pode
sernapastapadrãodousuário,ondeopromptcomeça).
• Dêocomandoparacriarachave. Aquieuquebreiemváriaslinhaspara
facilitar, masvocêdeverádigitart udoemumaúnicalinhaesubstituir
“ederson-cassio”porseunomeouempresa,naturalmente. Nestecaso,a
chavepossuiráoalias(nome)
ederson_cassio,seráarmazenadano
arquivo ederson-cassio.keystoreesuavalidadeseráde 10000
dias(aproximadamente27anos,maisqueosuficiente):
keytool
-genkey -v
-keystore ederson-cassio.keystore
-alias ederson_cassio
-keyalg RSA
-keysize 2048
-validity 10000
• Informeasenhadakeystore(serápedidaconfirmação,emcasodenova
keystore).
• Informe os dados de identificação pedidos (seu nome, empresa, local-
idade). Achaveserágeradaemseguida.
• Aofinal,pede-seasenhadanovachave. Vocêpodeapenasdar Enter
sequiserusaramesmasenhadakeystore.
31

## Página 50

2.7. GerarpacoteAPKassinadoparaoAndroid CasadoCódigo
GerandooAPKparadistribuição
A go raváparaapastadop r o jetoedêoco mando:
cordova build android --release
Serágeradooarquivo PrimeiroProjetoCordova-release-unsigned.apk,
na subpasta platforms/android/ant-build. T a m b é me s t ã oa l io s
APKs de debug gerados anteriormente, que só podem ser usados nos
aparelhoscomdepuraçãoUSBativada.
AssinandooAPK
Parafacilitar,movaoarquivo PrimeiroProjetoCordova-release-
unsigned.apk para a pasta onde está a keystore. Você poderá renomeá-lo
paraalgomaissignificativo,como MeuJogo.apk.
De volta ao prompt, na pasta inicial, podemos assinar o arquivo através
do comando a seguir. Perceba que os três últimos parâmetros referem-se ao
arquivo .keystore,aoar quivo .apkeaoaliasarmazenado:
jarsigner
-verbose -sigalg SHA1withRSA -digestalg SHA1
-keystore ederson-cassio.keystore
MeuJogo.apk
ederson_cassio
Bastainfo rmarasenhadakeysto r eeoar quivoseráassinado .
InstalandooAPKdiretamentenoaparelho
ParapoderinstalarumaplicativodiretamentedoAPK,énecessáriocon-
figuraroAndroidparaaceitarappsdefontesdesconhecidas:
• Entrenas Configuraçõese,emseguida,em Segurança.
• Roleatéencontraraopção Fontes desconhecidas emarque-a:
32

## Página 51

CasadoCódigo Ca p í tulo2. Criandoop rimeir op r o jeto
Figura2.8: ConfigurandooAndroidparaaceitarAPKsestranhos
O Android dará um aviso de segurança. Recomendo que você não o ig-
nore;apósinstalaroaplicativo,procuredesativaressaopção.
Figura2.9: Nãodigaquenãofoiavisado...
• Copieoarquivo .apk paraoaparelhoelocalize-o. Podeserquevocê
tenha que instalar um gerenciador de arquivos. No meu celular, estou
usandoo ES File Explorer,queégra tui to:
33

## Página 52

2.7. GerarpacoteAPKassinadoparaoAndroid CasadoCódigo
Figura2.10: ProcurandooarquivoAPK
PermissõesdoAndroid
QueméusuáriodoAndroidsabeque,parainstalarumaplicativoou
jogo,esterequerumcertonúmerodepermissõesdosistemaoperacional.
OCordova,porpadrão,colocanoprojetoumpedidodepermissãopara
acesso à internet. Se seu jogo utilizar apenas recursos locais, podemos
removerestapermissão:
•N a s u b p a s t a
platforms/android,a b r aoa r q u i v o
AndroidManifest.xml
• Removaaseguintetag:
<uses-permission
android:name="android.permission.INTERNET" />
Muito cuidado, porém: a instalação de plugins do Cordova, que
aprenderemos em4.3, poderá adicionar pedidos de diversas permissões
requeridas pelas APIs. Não remova os novos requerimentos que apare-
cerem,ouasAPIsnãoirãofuncionar. Vocêpodecolocardevoltaaper-
missãoparainternetcasotenhaconstatadoalgumafalha.
34

## Página 53

CasadoCódigo Ca p í tulo2. Criandoop rimeir op r o jeto
2.8 Consideraçõesfinais
É muita coisa técnica! Mas isso tudo é necessário para termos nossos jogos
na forma de apps Android. Dominando todo este ciclo de desenvolvimento,
jápodemosnosconcentraremcriarcoisasmaisdivertidas. Nopróximocapí-
tulo,brincaremoscomainteraçãoportoque.
OqueocorreéqueousodoHTML5éumatendênciarecente,porémem
crescimento, para o desenvolvimento de aplicativos em diversas plataformas
(como é o caso do Windows 8 e do Firefox OS). Ainda não há IDEs e fer-
ramentas de produtividade. Aplicações híbridas (como as geradas pelo Cor-
dova)tendemasermaislentasqueasnativas,emespecialnosaparelhosmais
simples,masapotênciadelessótendeaaumentar. AideiadeusaroHTML5
paraalcançarqualquerplataformaestásefirmando.
DocumentaçãodoCordova
Paraaprofundarseusestudos,deixo-lheolinkparaadocumentação
doprojeto:
http://cordova.apache.org/docs/en/3.5.0/
Lá você poderá aprender sobre as opções da CLI, configurações do
config.xml,APIs,pluginsemuitomais.
35

## Página 55

Capítulo3
Eventostouch
VamostrataragoradaespecificaçãodoHTML5paraeventostouch. Existem
frameworks para auxiliar no tratamento de gestos complexos e usuais (mais
adiante, no capítulo5, abordarei oHammer.js), que são bastante trabalhosos
de tratar. Ainda assim, devemos saber como tratar pelo menos as interações
básicascomoHTML5“cru”.
Aespecificaçãodefineosseguinteseventos:
• touchstart: iníciodotoque;
• touchmove: u s uá ri om o v eod ed on at e laapa rti rd oo b je t oq u er ec e -
beuoeven to;
• touchleave: odedoabando naaár eadoob jeto;
• touchenter: odedoen tradevol tanaár eadoob jeto;

## Página 56

3.1. Arrastandoumobjeto CasadoCódigo
• touchend: fimdotoque(usuáriosoltaodedo);
• touchcancel: ocancelamen todotoqueocorreseaáreadapáginasair
dofocodeinteração(porexemplo,sesurgirumacaixadealerta).
3.1 Arrastandoumobjeto
Éabasedeinteraçãoemmúltiplosjogosparatelastouch(quemnuncajogou
AngryBirds ouPou?). Comoauxíliodoseventos touchstart, touchmove
e touchend, podemos obter as coordenadas da tela onde o toque ocorreu,
verificarseoobjetoseencontraporaliemovê-lo.
Preparei uma pequenaspritesheet para controlarmos com o dedo. Em
http://www.iconarchive.com/e muitos outros sites você pode obter diversos
ícones,apartirdosquaisvocêpoderámontarspritesheetsusandoumeditor
deimagens:
Figura3.1: Éumpássaro? Éumavião? Usesuaimaginação!
Oesqueleto
CrieumnovoprojetoCordova:
cordova create touch
AdicioneaplataformaAndroid:
cd touch
cordova platform add android
38

## Página 57

CasadoCódigo Capítulo3. Eventostouch
Coloqueoseguinteesqueletono index.html:
<!DOCTYPE html>
<html>
<head>
<meta charset= "utf-8">
<title>Arrastando Objeto Via Touch </title>
<meta name="viewport" content="width=device-width,
height=device-height,user-scalable=no,
initial-scale=1,maximum-scale=1,minimum-scale=1" >
<script src="cordova.js"></script>
<script src="rAF.js"></script>
<script>
// Código do app
</script>
</head>
<body>
<canvas id="touch" width="320" height="240"></canvas>
</body>
</head>
Façamos a inicialização básica discutida no capítulo anterior. Quando
tudoestiverpronto,vocêdeverátrocarachamadadiretaàfunção iniciar
peloevento devicereadydoCordova:
var canvas,context;
window.onload = function() {
// Troque as linhas quando for fazer deploy no aparelho
//document.addEventListener( ' deviceready ' ,iniciar);
iniciar();
}
function iniciar() {
canvas = document .getElementById( ' touch ' );
context = canvas.getContext( ' 2d ' );
39

## Página 58

3.1. Arrastandoumobjeto CasadoCódigo
// inicializações virão aqui
requestAnimationFrame(animar);
}
Afunçãodeanimação,primeiramente,cuidarádelimparatelaechamar
opróximociclo:
function animar() {
context.clearRect(0, 0,canvas.width,canvas.height);
// desenhos virão aqui
requestAnimationFrame(animar);
}
Antes de continuarmos, abra a página no browser e verifique se não
aparecem erros no Console só para garantir que tudo foi digitado correta-
mente: nomes de variáveis, parênteses etc. O browser dará falta do arquivo
cordova.js, mas este erro pode ser ignorado até o momento em que for
necessáriousaralgumaAPIprópriadoCordova.
Posicionandoedesenhando
Vamosdefiniragoraaposiçãodoobjeto. Inicialmentedesenharemosum
círculosimplesparatestaroseventosdetouche,emseguida,osubstituiremos
pelabruxa.
Declar easvariá veis
x, ye raiojun toco maso u trasglobaisdapágina:
var canvas,context;
var x,y,raio =3 2 ;
Nafunção iniciar,comeceposicionandooobjetonocentrodoCanvas
econfigurandooseventos touchstart, touchmovee touchend:
function iniciar() {
canvas = document .getElementById( ' touch ' );
context = canvas.getContext( ' 2d ' );
40

## Página 59

CasadoCódigo Capítulo3. Eventostouch
x = canvas.width /2 ;
y = canvas.height /2 ;
canvas.addEventListener( ' touchstart ' , touchStart);
canvas.addEventListener( ' touchmove ' , touchMove);
canvas.addEventListener( ' touchend ' , touchEnd);
requestAnimationFrame(animar);
}
Desenheocírculoem animar:
function animar() {
context.clearRect(0, 0, canvas.width, canvas.height);
context.save();
context.fillStyle = ' red ' ;
context.strokeStyle = ' blue ' ;
context.lineWidth =2 ;
context.beginPath();
context.arc(x, y, raio, 0, Math.PI*2);
context.fill();
context.stroke();
context.restore();
requestAnimationFrame(animar);
}
Programaçãodoseventos
Vamos agora capturar a posição onde o toque iniciou, na função
touchStart. O parâmetro de evento recebido possui o atributo
changedTouches,queéumarrayrepresentandotodososdedosatualmente
natela. Osatributos pageXe pageYnosdãoaposiçãodotoquenapágina ,
nãorelativamenteaoCanvas:
41

## Página 60

3.1. Arrastandoumobjeto CasadoCódigo
function touchStart(e) {
console.log( ' x: ' + e.changedTouches[0].pageX +
' ,y : ' + e.changedTouches[0].pageY);
}
function touchMove(e) {
}
function touchEnd(e) {
}
Neste ponto, faça outro teste no navegador: você deverá ver uma bola
vermelha,debordaazul(useascoresquedesejar).
Osatributosdeposiçãodo changedTouchessão:
• pageXepageY:posiçãorelativaàdimensãocompletadapágina(view-
port),considerandoaposiçãoderolagem;
• clientX eclientY: posição relativa à área de renderização do browser
(semconsiderararolagem);
• screenX escreenY: posição relativa à tela do computador ou disposi-
tivo.
Como você deve ter percebido, os eventos touch não nos dão a posição
exatadetoque naáreadoCanvas ,queéoqueprecisamos.Mastodoelemento
deumapáginaHTMLpossuiosatributos offsetLefte offsetTop,que
nosdãoaposiçãoatualdeumelementodentrodoviewport. SenossoCanvas
seencontranaposição(10,10)dapágina,porexemplo,otoqueem(10,10)na
teladevecorrespondera(0,0)noCanvas. Ouseja,basta subtrairosoffsets:
42

## Página 61

CasadoCódigo Capítulo3. Eventostouch
Figura 3.2: Subtraindo os offsets e obtendo a posição de toque dentro de um
elemento
Dessaforma,podemosdefinirascoordenadasdoobjeto:
function touchStart(e) {
x = e.changedTouches[0].pageX - canvas.offsetLeft;
y = e.changedTouches[0].pageY - canvas.offsetTop;
console.log( ' x: ' + x + ' ,y: ' + y);
}
Vamosverificarseotoqueocorreunaáreadocírculo. Paraisso,contamos
com a ajuda do nosso velho conhecido Teorema de Pitágoras (figura3.3). A
distânciaemlinharetaentreopontodotoqueeaposiçãoatualdocírculocor-
responde à hipotenusa (a). Asdistânciashorizontaleverticalcorrespondem
aoscatetos( bec):
43

## Página 62

3.1. Arrastandoumobjeto CasadoCódigo
Figura3.3:Triânguloretânguloformadocomadistânciaentreopontotocado
eocírculo
Seahipotenusaformenorouigualaoraio,tocamosdentrodocírculo!
Figura3.4: Posiçãodetoquedentrodaáreadocírculo: ahipotenusaémenor
queoraio
Vamosaocódigo. Usamos
Math.absparaobterasdistânciasemvalores
absolutos,poisnãoimportaqualposiçãoéanteriorouposterioraqual( x-
xToquepodesernegativose x < xToque ). Seotoquefoinaáreadocírculo,
sinalizamosqueomovimentocomeçou(variável arrastando)emudamos
asvariáveis xe y:
function touchStart(e) {
var xToque = e.changedTouches[0].pageX - canvas.offsetLeft;
44

## Página 63

CasadoCódigo Capítulo3. Eventostouch
var yToque = e.changedTouches[0].pageY - canvas.offsetTop;
var distanciaX = Math .abs(x - xToque);
var distanciaY = Math .abs(y - yToque);
// Pitágoras
if (
distanciaX *distanciaX + distanciaY*distanciaY <= raio*raio) {
arrastando = true;
x = xToque;
y = yToque;
}
}
T emosquedeclararavariá vel arrastandocomoglobal:
var canvas, context;
var x, y, raio =3 2 ;
var arrastando;
Parafinalizar,nafunção touchMove,verificamosseestamosarrastando
abolinhaeatualizamosaposição,igualfeitoanteriormente. Em touchEnd,
mudamos a variável arrastando para false, indicando que a bola não
devemaissemover:
function touchMove(e) {
if (arrastando) {
x = e.changedTouches[0].pageX - canvas.offsetLeft;
y = e.changedTouches[0].pageY - canvas.offsetTop;
}
}
function touchEnd(e) {
arrastando = false;
}
Vamostestarnonavegador. OGoogleChromepossuiumaformadeem-
ulardispositivosmóveisemsuasdimensõeseeventostouch. Sigaospassos:
•T e c l eCtrl + Shift + J paraabriroConsole.
45

## Página 64

3.2. Controlandoadireção CasadoCódigo
• Co mof oc on oCo n s o l e ,t e c l eEsc. Será aberto um novo conjunto de
guias.
• Na guia Emulation, selecione um modelo pré-configurado qualquer e
cliqueem Emulate.
• Atualizeapágina( F5).
Figura3.5: EmulandodispositivosmóveisnoGoogleChrome
Você pode agora provocar eventos de toque com o mouse no Chrome!
Infelizmente, no Android ainda não vai funcionar, mas é por causa de um
bug. Acrescenteasseguinteslinhasaoevento touchstart:
Podefazer cordova run android epuxarabolinhacomodedo!
3.2 Controlandoadireção
Para usarmos adequadamente a spritesheet da figura3.1, precisamos contro-
lar a direção para onde ocorrem os movimentos, se para a direita ou para a
esquerda.
46

## Página 65

CasadoCódigo Capítulo3. Eventostouch
Oevento touchmoveégeradocontinuamenteconformenosmovimen-
tamos. Para definir se vamos para a direita ou para a esquerda, temos que
guar daraposiçãonoúltimoeven to ,ecom pararcomaposiçãodoeven toa t-
ual. Declareasvariáveis
xAnteriore yAnterior:
var canvas, context;
var x, y, raio =3 2 ;
var arrastando;
var xAnterior, yAnterior;
Guardenelasaposiçãoinicialdomovimento:
function touchStart(e) {
// ...
// Pitágoras
if (
distanciaX *distanciaX + distanciaY*distanciaY <= raio*raio) {
arrastando = true;
x = xToque;
y = yToque;
xAnterior = x; // Guardar a posição
yAnterior = y;
}
// ...
}
E,aomudaraposição,guardeosvalores anteriores:
function touchMove(e) {
if (arrastando) {
xAnterior = x; // Guardar a posição
yAnterior = y;
x = e.changedTouches[0].pageX - canvas.offsetLeft;
y = e.changedTouches[0].pageY - canvas.offsetTop;
}
}
47

## Página 66

3.2. Controlandoadireção CasadoCódigo
Usandoaspritesheet
No pacote de download, no projeto da pastatouch,e s t áp r e s e n t eoa r -
quivo bruxa.png,umaspritesheetcomduasimagens96x96(192x96noto-
tal).
Sabendo as posições atual e anterior, a cada disparo dotouchmove,
podemos desenhar a figura certa da spritesheet. Vamos mudar a função
animar para chamar outra, desenharBruxa, que cuidará do clipping
(recorte):
function animar() {
context.clearRect(0, 0, canvas.width, canvas.height);
desenharBruxa();
requestAnimationFrame(animar);
}
Nessa nova função, consideraremos x e y, definidos nos eventos de
touch, como o centro da imagem. Desta forma, descontamos metade da
largura e da altura de destino ao posicionar. Cada bruxa na imagem pos-
sui 96x96 pixels, mas vamos renderizá-la menor, em 64x64. Para definir a
posiçãodoclipping,comparamosasvariáveis
xe xAnterior,eassimsabe-
mosseestamosindoparaadireitaouparaaesquerda:
function desenharBruxa() {
var largOrigem =9 6 , largDestino =6 4 ;
var xOrigem = (x >= xAnterior)
?0 // Direita
:9 6 ; // Esquerda
context.drawImage(imgBruxa,
xOrigem, // x na spritesheet
0, // y na spritesheet
largOrigem,
largOrigem,
x - largDestino/2 , // x no Canvas
y - largDestino/2 , // y no Canvas
largDestino,
largDestino);
}
48

## Página 67

CasadoCódigo Capítulo3. Eventostouch
Qualquer trabalho análogo na vertical poderia ser feito comparandoy
com yAnterior.
Precisamos carregar a imagem. Altere a inicialização do app para ficar
comosegue. Parafacilitaragora,podemosmanteroraio,deixandoaáreade
touchcircular(maspodemosaumentá-loumpoucoparadarmaisconforto):
Rodeoappnodispositivoeleveabruxinhadeumladoparaooutro:
Figura3.6: Elávamosnós!
49

## Página 68

3.3. ToqueemCanvasresponsivo CasadoCódigo
3.3 ToqueemCanvasresponsivo
NossoCanvasestácomtamanhofixo,podendofaltarespaçoparaelenosdis-
positivos menores, ou sobrar espaço na página, nos maiores. É interessante
podermos usar um pouco de CSS para tornar nosso Canvas responsivo, ou
seja, adaptado à tela do dispositivo. Também, como estamos criando apps
que rodam localmente, não é nada mau termos imagens um pouco maiores,
sendoreduzidasconformenecessário(jáquenãoseráfeitodownloaddelas).
Mastemosumpequenoproblema. AimagemdoCanvassempreépro-
cessadacomasdimensõesinformadasnatag. Em um Canvas responsivo,
elaapareceredimensionada. Aotocarouclicar,oseventosreportamaposição
relativaaotamanhorenderizadoemtela,masnaimagemrealessasposições
sofremdeslocamento,exigindoaconversãoentretamanhodarenderizaçãoe
tamanhodaimagemr eal.
Pormaiscomplicadoquepareça,resolverissoémuitosimples. Bastafazer
umaregradetrês. Porexemplo,seoCanvasestásendorenderizadocom960
pixelsdelarguraeeutoconaposição450(em x),emqualposiçãodaimagem
realeutoquei,seatagindica800?
Tamanho Posição
960 ===> 450 (renderizado)
800 ===> x (real)
x = 800 * 450 / 960
Omesmoraciocícioseaplicaàposição y.
É fácil descobrir o tamanho com que um elemento da página HTML é
renderizadoemtela:bastalerosatributos offsetWidthe offsetHeight.
Assim,podemosterumafunçãoquerecebeascoordenadascapturadaspelos
eventoseastransformamemcoordenadasdaimagemreal,atravésdocálculo
descrito:
function converterParaCanvas(xToque, yToque) {
return {
x: canvas.width * xToque / canvas.offsetWidth,
y: canvas.height * yToque / canvas.offsetHeight
}
}
50

## Página 69

CasadoCódigo Capítulo3. Eventostouch
Devemos,também,alterarasfunçõesquecapturameventosparachamar
afunçãodeconversão. Modifique touchStart:
function touchStart(e) {
var posicao = converterParaCanvas(
e.changedTouches[0].pageX - canvas.offsetLeft,
e.changedTouches[0].pageY - canvas.offsetTop
);
var xToque = posicao.x;
var yToque = posicao.y;
// O restante continua igual
}
E touchMove:
function touchMove(e) {
if (arrastando) {
xAnterior = x; // Guardar a posição
yAnterior = y;
var posicao = converterParaCanvas(
e.changedTouches[0].pageX - canvas.offsetLeft,
e.changedTouches[0].pageY - canvas.offsetTop
);
x = posicao.x;
y = posicao.y;
}
}
DimensionandooCanvas
Agora podemos dimensionar o Canvas de forma que fique responsivo,
sem causar problemas. Para isso, coloque uma tag <style> na seção
<head>(o ucrieumlinkparaumar quivo .css).
Nafolhadeestilo,definaocorpodapágina( body)comoocupandotoda
a área disponível do browser (ou webview, em nosso caso), pois ela servirá
comoumareferênciaparaoCanvassedimensionar:
51

## Página 70

3.3. ToqueemCanvasresponsivo CasadoCódigo
body {
margin:0 ;
width: 100%;
height: 100%;
}
VamosdimensionaroCanvas,primeiramente,tendoemmenteaposição
retrato (aparelho em pé), ou seja, com a largura menor que a altura. Ocu-
pamos toda a largura (width: 100%; ) e mantemos a altura na proporção
paraaimagemnãoficardistorcida( height: auto; ):
/* Padrão (largura < altura) */
canvas {
width: 100%;
height: auto;
display: block ;
}
Para a posição paisagem (deitado), faremos umamedia query(consulta
do dispositivo) que determina uma razão mínima entre a larguraeaa l tura.
Acimadessarazão,valeráanovaformatação. Estarazãodeveserpassadana
fo rmadefração ,po rexem plo:
• 2/1indicaquealarguraéodob r odaal tura;
• 1/2indicaoco n trário ,quealarguraéametadedaal tura;
• 1/1indicaumaáreaquadrada(ambososladosiguais).
Qualquerfraçãopodeserusada(como 322/423),masproporçõessim-
ples são mais fáceis de mentalizar. Tudo que for abaixo de1/1 é retrato, e
acimaépaisagem. Comonossaformataçãopadrãotrataolayoutemretrato,
vamosestabeleceromínimode
1/1paraaforma taçãodepaisagem,a tra vés
doatributo min-aspect-ratiodamediaquery:
/* A partir de 1/1 (iguais ou largura > altura) */
@media (min-aspect-ratio: 1/1) {
}
52

## Página 71

CasadoCódigo Capítulo3. Eventostouch
Dentro da media query, basta fazer o contrário da formatação padrão:
ocupar100%daalturaeajustaralarguraproporcionalmente. Tambémpode-
mosdarumamargemautomáticaparacentralizaroCanvas:
/* A partir de 1 (iguais ou largura > altura) */
@media (min-aspect-ratio: 1/1) {
canvas {
height: 100%;
width: auto;
margin:0auto;
}
}
Também podemos adicionar background-color ou
background-image para compor o cenário, fica a seu critério. Vamos
brincarumpouco!
Figura3.7: Canvasseajustandoaotamanhododispositivo
53

## Página 72

3.3. ToqueemCanvasresponsivo CasadoCódigo
Webdesignresponsivoemobile
E m b o r as e j ai m p o r t a n t en ac r i a ç ã od ej o g o s ,n ã oéoo b j e t i v oa q u i
ficarfalandosobrewebdesignresponsivo;casoqueirasaberemdetalhes,
vocêpodelerolivrodeTárcioZemel([ 4]):
http://www.casadocodigo.com.br/products/
livro-web-design-responsivo
Também recomendo muito a leitura doAW e bM o b i l e, de Sérgio
Lopes([2]):
http://www.casadocodigo.com.br/products/livro-web-mobile
Ambosforamfontesdereferênciafundamentaisparaestelivro.
54

## Página 73

Capítulo4
Incrementandoojogodenave
Este capítulo é dedicado a transformar o jogo construído no meu primeiro
livro em aplicação móvel. Você aprenderá a criar um controle direcional
suave para touchscreen e conhecerá as APIs do Cordova para multimídia e
acelerômetro.
Caso você não o conheça, pode jogá-lo agora, em seu desktop ou note-
book, em: http://gamecursos.com.br/livro/jogo. É um jogo de nave e tiro,
ondesuamissãoédestruirdiscosvoadoresenãosedeixarseratingido.
Osarquivos-fontedessejogopodemserobtidosem:
http://github.com/EdyKnopfler/games-js/archive/master.zip
Dentrodo
zip,aspastasestãonumeradaspeloscapítulos. Procurepegar
osarquivosdoúltimocapítulo(pasta 09),poisestãoemsuasversõesfinais.

## Página 74

4.1. Revisãodasclassesdojogo CasadoCódigo
4.1 Revisãodasclassesdojogo
O jogo de nave possui um pequeno game engine composto pelas seguintes
classesdeutilidadegeral:
• Animacao: ocoraçãodogameengine. Realizaogameloopeinterage
comosspriteseprocessamentosgeraisassociadosaele.
• Teclado: realizaacapturadecomandospeloteclado. Nãoseráusado
aqui;emseulugarcriaremosaclasse Direcional.
• Colisor: detectaacolisãoentreosspritesassociadosaele.
• Spritesheet: anima folhas de sprites, dividindo a imagem em
quadrosdeigualtamanhoeselecionandooquadroatualdeacordocom
otem poeavelocidadedaanimação .
Jáasseguintesclasseseramespecíficasdojogodenave,mascomoobje-
tivodedemonstrarcomoosspritestrabalhamemumjogo. Tinhamquepos-
suir os métodos
atualizar e desenhar, para que aAnimacao pudesse
interagircomeles:
• Fundo: fazarolagemdasimagensdocenário.
• Nave: a nave controlada pelo jogador. Realizava constantemente a
leiturado Tecladoparasemovimentar.
• Ovni: oinimigoaserdestruído. Retirava-sedaanimaçãoapóspercor-
r ertodaatela,paranãoseacum ularnamemó ria.
• Tiro: disparodanave. Tambémseretiravadaanimaçãoaosairdatela.
• Painel: mostradordevidasepontuação.
A maioria destas classes manterá seu funcionamento idêntico na versão
mobiledojogo.
56

## Página 75

CasadoCódigo Ca p í tulo4. I ncr emen tandoojogodena ve
4.2 Esqueletodoprojeto
VamoscomeçarcriandooprojetoeadicionandoaplataformaAndroid:
cordova create nave-mobile-1
cd nave-mobile-1
cordova platform add android
Depois, copieparaapasta www osscriptsquevocêbaixou(comexceção
de teclado.js),etambémaspastas imge snd(imagensesons).
Façamosumaconfiguraçãoparatravarojogonaposiçãoretrato(empé)
doaparelho. Porpadrão,porserpáginadaweb,umappCordovaacompanha
aorientaçãodatelaconformeviramosodispositivo. Parafixaratelaemuma
determinada orientação, podemos inserir uma tag
<preference> no ar-
quivo config.xml. Atagaceitaosvalores portrait(empé), landscape
(deitado)e default(omesmoquenãousá-la,permitindogirarlivremente
atela):
<?xml version= ' 1.0 ' encoding= ' utf-8 ' ?>
<widget ...>
...
<preference name="Orientation" value="portrait" />
</widget>
Oa r q u i v oindex.html do projeto irá linkar os scriptscordova.js,
rAF.js(oucomovocênomeouopolyfillpara requestAnimationFrame)
eosscriptsquevocêbaixou. NocorpotemosoCanvaseolinkparaobotão
Jogar:
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Jogo de Nave - controlado via touch </title>
<meta name="viewport" content="width=device-width,
height=device-height, user-scalable=no,
57

## Página 76

4.2. Esqueletodoprojeto CasadoCódigo
initial-scale=1, maximum-scale=1, minimum-scale=1" >
<script src="cordova.js"></script>
<script src="rAF.js"></script>
<script src="animacao.js"></script>
<script src="spritesheet.js"></script>
<script src="colisor.js"></script>
<script src="fundo.js"></script>
<script src="nave.js"></script>
<script src="ovni.js"></script>
<script src="painel.js"></script>
<script src="tiro.js"></script>
<script src="explosao.js"></script>
<script>
// A aventura vai começar no celular!
</script>
</head>
<body>
<canvas id="jogo_nave" width="500" height="500"></canvas>
<div id="link_jogar">
<a href="javascript: iniciarJogo()" >Jogar</a>
</div>
</body>
</html>
As variáveis da página são praticamente as mesmas já presentes no jogo.
Ainicializaçãoéquemudaráumpouco,paraficarnoformatodoCordova:
var canvas, context;
var imagens, animacao, colisor, nave, painel, criadorInimigos;
var totalImagens =0 , carregadas =0 ;
window.onload = function() {
//document.addEventListener( ' deviceready ' , iniciar);
iniciar();
58

## Página 77

CasadoCódigo Ca p í tulo4. I ncr emen tandoojogodena ve
}
function iniciar() {
canvas = document .getElementById( ' jogo_nave ' );
context = canvas.getContext( ' 2d ' );
carregarImagens();
}
A partir daqui, vamos pegar as funções presentes no jogo original, uma
por uma. A página HTML está no arquivojogo-definitivo.html,n a
p a s t ad oc a p í t u l o09. Em alguns casos, vou indicar modificações. Para fa-
cilitar, você pode copiar e colar os códigos para o projeto Cordova, e depois
adaptá-los. Afunçãodecarregamentodasimagenspermaneceamesma:
function carregarImagens() {
imagens = {
espaco: ' fundo-espaco.png ' ,
estrelas: ' fundo-estrelas.png ' ,
nuvens: ' fundo-nuvens.png ' ,
nave: ' nave-spritesheet.png ' ,
ovni: ' ovni.png ' ,
explosao: ' explosao.png '
};
for (var i in imagens) {
var img = new Image();
img.src = ' img/ ' + imagens[i];
img.onload = carregando;
totalImagens++;
imagens[i] = img;
}
}
Para podermos ir mais direto ao que nos interessa agora, que é a trans-
formaçãodojogoemappmobile,simplifiqueialgumasfunções. Umadelasé
afunçãoqueverificaquaisimagensjácarregaram,poisaquiocarregamento
émaisrápido. Sinta-selivrepararecriarabarradeprogresso(oscódigoses-
tãolá!) ouquaisquerefeitosvisuaisquedesejar: splashscreens,logos.E s t a n d o
todasasimagenscarregadas,obotão
Jogardeverásurgir:
59

## Página 78

4.2. Esqueletodoprojeto CasadoCódigo
function carregando() {
carregadas++ ;
if (carregadas == totalImagens) {
iniciarObjetos();
document.getElementById( ' link_jogar ' ).style.display =
' block ' ;
}
}
Ainicializaçãodosobjetosdojogotambémmudoupouco. Nãohámaiso
objeto teclado,eporissotambéma navenãoorecebemaisnoconstrutor:
function iniciarObjetos() {
animacao = new Animacao(context);
//teclado = new Teclado(document);
colisor = new Colisor();
espaco = new Fundo(context, imagens.espaco);
estrelas = new Fundo(context, imagens.estrelas);
nuvens = new Fundo(context, imagens.nuvens);
// O construtor da nave não recebe mais o teclado
nave = new Nave(context, imagens.nave, imagens.explosao);
painel = new Painel(context, nave);
animacao.novoSprite(espaco);
animacao.novoSprite(estrelas);
animacao.novoSprite(nuvens);
animacao.novoSprite(painel);
animacao.novoSprite(nave);
colisor.novoSprite(nave);
animacao.novoProcessamento(colisor);
configuracoesIniciais();
}
M udandooco nstru to rdaNave(em nave.js):
60

## Página 79

CasadoCódigo Ca p í tulo4. I ncr emen tandoojogodena ve
function Nave(context, imagem, imgExplosao) {
this.context = context;
//this.teclado = teclado;
// ...
}
Vamos, por enquanto, comentar os trechos em que aNave faz uso do
teclado. Nométodo atualizar:
atualizar: function() {
var incremento =
this.velocidade * this.animacao.decorrido / 1000;
/*
if (this.teclado.pressionada(SETA_ESQUERDA) && this.x > 0)
this.x -= incremento;
if (this.teclado.pressionada(SETA_DIREITA) &&
this.x < this.context.canvas.width - 36)
this.x += incremento;
if (this.teclado.pressionada(SETA_ACIMA) && this.y > 0)
this.y -= incremento;
if (this.teclado.pressionada(SETA_ABAIXO) &&
this.y < this.context.canvas.height - 48)
this.y += incremento;
*/
},
Etambémem desenhar:
desenhar: function() {
/*
if (this.teclado.pressionada(SETA_ESQUERDA))
this.spritesheet.linha = 1;
else if (this.teclado.pressionada(SETA_DIREITA))
this.spritesheet.linha = 2;
else
61

## Página 80

4.2. Esqueletodoprojeto CasadoCódigo
this.spritesheet.linha = 0;
*/
this.spritesheet.desenhar( this .x, this.y);
this.spritesheet.proximoQuadro();
},
Devoltaao index.html,asconfiguraçõesiniciaistambémnãomudam:
function configuracoesIniciais() {
espaco.velocidade =6 0 ;
estrelas.velocidade = 150;
nuvens.velocidade = 500;
nave.posicionar();
nave.velocidade = 200;
criacaoInimigos();
nave.acabaramVidas = function() {
animacao.desligar();
gameOver();
}
colisor.aoColidir = function(o1, o2) {
if ( (o1 instanceof Tiro && o2 instanceof Ovni) ||
(o1 instanceof Ovni && o2 instanceof Tiro) )
painel.pontuacao += 10;
}
}
Enemainicializaçãodoobjetoquecriainimigosacadasegundo:
function criacaoInimigos() {
criadorInimigos = {
ultimoOvni : Date.now(),
processar: function() {
var agora = Date.now();
var decorrido = agora - this.ultimoOvni;
62

## Página 81

CasadoCódigo Ca p í tulo4. I ncr emen tandoojogodena ve
if (decorrido > 1000){
novoOvni();
this.ultimoOvni = agora;
}
}
};
animacao.novoProcessamento(criadorInimigos);
}
Este chama a criação do disco voador, que usavaMath.random para
sortearumavelocidadeeumaposição,lembra-se?
function novoOvni() {
var imgOvni = imagens.ovni;
var ovni = new Ovni(context, imgOvni, imagens.explosao);
ovni.velocidade =
Math.floor( 500 + Math .random() * (1000 - 500 + 1 )) ;
ovni.x =
Math.floor( Math.random() *
(canvas.width - imgOvni.width +1 )) ;
ovni.y =- imgOvni.height;
animacao.novoSprite(ovni);
colisor.novoSprite(ovni);
}
Até aqui, faça um pequeno teste no navegador: ao carregar a página, o
único erro no Console deverá ser a falta docordova.js.M a sa i n d an ã o
dá para clicar emJogar, pois não há a funçãoiniciarJogo.T a m b é m
resolvi simplificá-la; a música será programada posteriormente pela API do
Cordova:
function iniciarJogo() {
criadorInimigos.ultimoOvni = Date.now();
63

## Página 82

4.2. Esqueletodoprojeto CasadoCódigo
document.getElementById( ' link_jogar ' ).style.display =
' none ' ;
painel.pontuacao =0 ;
animacao.ligar();
}
Damesmaforma,tambémsimplifiqueiafunçãoquefinalizaojogo:
function gameOver() {
document.getElementById( ' link_jogar ' ).style.display = ' block ' ;
nave.vidasExtras =3 ;
nave.posicionar();
// A nave é reintroduzida por ter sido retirada na explosão
animacao.novoSprite(nave);
colisor.novoSprite(nave);
removerInimigos();
alert( ' Game Over ' );
}
Ela chama uma outra função para remover elementos que sobraram na
tela:
function removerInimigos() {
for (var i in animacao.sprites) {
if (animacao.sprites[i] instanceof Ovni ||
animacao.sprites[i] instanceof Tiro)
animacao.excluirSprite(animacao.sprites[i]);
}
}
VamosaoCSS.OCanvasiráocupartodaalargura,deixandoorestanteda
alturaparaodirecional. Obotão Jogarinicia-seoculto,eolinkdentrodele
teráoformatodaimagem botao-jogar.png,quejádeveestarpresentena
subpasta www/img:
64

## Página 83

CasadoCódigo Ca p í tulo4. I ncr emen tandoojogodena ve
body {
margin:0 ;
width: 100%;
height: 100%;
}
#jogo_nave {
width: 100%;
height: auto;
}
#link_jogar {
display: none ;
text-align : center;
padding: 20px ;
}
#link_jogar a {
color: yellow ;
background : url(img/botao-jogar.png);
font-size:2 0 p x ;
font-family: sans-serif;
text-decoration: none;
text-shadow: 2px 2px 5px black;
display: inline-block;
width: 52px;
height: 26px;
padding: 23px 10px;
}
F a ç ao u tr ot e s t en ob r o w se r .P od ese rp r ec i sor o l a rapá gi n apa r ae n c o n -
tra robo tãoJogar. Aaçãojádeveráacontecerdocomeçoaofim,dobotão
Jogar ao Game Over , embora ainda não se consiga controlar a nave. Mas
nãoépossívelrodarnocelular,poisawebviewpadrãodoAndroidaindanão
suporta a API de áudio do HTML5 (http://caniuse.com/audio-api).V a m o s
usaraAPIdoCo r do vaparagaran tirmaio rco m pa tib ilidade,embo raelanão
estejadentrodaespecificaçãodaW3C.
65

## Página 84

4.3. APIdesomdoCordova CasadoCódigo
4.3 APIdesomdoCordova
Comovimos,oCordovapossuiumaAPIprópriaparatratararquivosdemul-
timídia. A partir do Cordova 3.0, as APIs foram quebradas em plugins, de-
vendocadaumserinstaladonoprojetoparapoderserusado.
APIsdoCordova
Vocêpodeencontraralistaoficialdepluginsem:
http://goo.gl/aP905E
(EncurteiaURLporserumendereçobastantelongo)
Para instalar o plugin de multimídia, abra o terminal/prompt, navegue
atéapastaprincipaldoprojetoedêocomandoaseguir:
cordova plugin add org.apache.cordova.media
Esseplugindependedeoutro,deacessoaarquivos,easaídadocomando
noconsoleindicaráqueambosforaminstalados:
Fetching plugin "org.apache.cordova.media" via plugin registry
Installing "org.apache.cordova.media" for android
Fetching plugin "org.apache.cordova.file" via plugin registry
Installing "org.apache.cordova.file" for android
Os sons do jogo, baixados do pacote do livro anterior, estão
na subpasta snd do projeto original. Mova-os para a subpasta
platforms/android/assets do projeto Cordova (a partir da pasta
principal). Arquivos que serão acessados programaticamente através de
códigonativoAndroidpodemficarnessapasta.
Noarquivo tiro.js,aslinhasiniciaisdoscriptcarregamosomdodis-
paro. Remova-as:
// Remova estas linhas
var SOM_TIRO = new Audio();
SOM_TIRO.src = ' snd/tiro.mp3 ' ;
SOM_TIRO.volume = 0.2;
SOM_TIRO.load();
66

## Página 85

CasadoCódigo Ca p í tulo4. I ncr emen tandoojogodena ve
Noconstrutor,executamososomcadavezqueumtiroécriado. Também
removaaslinhasindicadas:
function Tiro(context, nave) {
// ...
// Remova estas também
SOM_TIRO.currentTime = 0.0;
SOM_TIRO.play();
}
Omesmodeveráserfeitoparaoarquivo explosao.js.
Agora,acrescenteasvariáveisquereferenciarãoossonsno index.html:
var canvas, context;
var imagens, animacao, colisor, nave, criadorInimigos;
var totalImagens =0 , carregadas =0 ;
var musicaAcao, somTiro, somExplosao;
Na função iniciar,chame carregarSons:
function iniciar() {
canvas = document .getElementById( ' jogo_nave ' );
context = canvas.getContext( ' 2d ' );
carregarImagens();
carregarSons();
}
Ecrieessafunção. NaAPIdemultimídiadoCordova,umobjeto Media
recebe o arquivo de som no construtor. Na plataforma Android, arquivos
napasta assetspodemserindicadosescrevendo file:///android_asset/meu_
arquivo:
function carregarSons() {
musicaAcao =
new Media( ' file:///android_asset/musica-acao.mp3 ' );
somTiro = new Media( ' file:///android_asset/tiro.mp3 ' );
somExplosao =
new Media( ' file:///android_asset/explosao.mp3 ' );
}
67

## Página 86

4.3. APIdesomdoCordova CasadoCódigo
Na função iniciarJogo, inicie a reprodução do som. O método
seekTo seleciona a posição no som em milissegundos setamos para zero
paravoltaramúsicanoinício. Depoisésóchamar play:
function iniciarJogo() {
// ...
musicaAcao.seekTo(0);
musicaAcao.play();
}
Na função gameOver,mandepausar:
function gameOver() {
musicaAcao.pause();
// ...
}
Oseventosdecolisãoestãoem configuracoesIniciais. Acrescente
asequência seekTo- playnoseventosdecolisão:
function configuracoesIniciais() {
// ...
// Pontuação e som das explosões
colisor.aoColidir = function(o1, o2) {
// Tiro com Ovni
if ( (o1 instanceof Tiro && o2 instanceof Ovni) ||
(o1 instanceof Ovni && o2 instanceof Tiro) ) {
painel.pontuacao += 10;
somExplosao.seekTo( 0);
somExplosao.play();
}
// Nave com Ovni
if ( (o1 instanceof Nave && o2 instanceof Ovni) ||
(o1 instanceof Ovni && o2 instanceof Nave) ) {
somExplosao.seekTo( 0);
somExplosao.play();
68

## Página 87

CasadoCódigo Ca p í tulo4. I ncr emen tandoojogodena ve
}
}
}
Já é possível rodar o projeto no dispositivo móvel, com o comando
cordova run android .
Observações
Semprequefortestaralgonocelular,nãoseesqueçademudaroscript
deinicializaçãoparacomeçarno deviceready:
window.onload = function() {
document.addEventListener( ' deviceready ' , iniciar);
//iniciar();
}
69

## Página 88

4.4. Criandoumcontroledirecional CasadoCódigo
Figura4.1: Nossovelhojogodenavevirandoumappmóveleportável
4.4 Criandoumcontroledirecional
Paracontrolaranave,primeirovamoscriarumcontroledirecionalparatelas
touch. Ouseja,recriaratravésdeíconesajogabilidadedosmaravilhososjoy-
sticksdosanos90!
70

## Página 89

CasadoCódigo Ca p í tulo4. I ncr emen tandoojogodena ve
Figura4.2: ControledoconsoleSNES,daNintendo
Nessescontroles,osquatrobotõesunidosfisicamenteemcruzoucírculo
faziam com que, levando o dedo para a diagonal, dois deles ficassem pres-
sionadosjuntos,forçandoadireçãodiagonalcorrespondente:
Figura4.3: Pressionandoduasdireçõesjuntasparairparaadiagonal
Em nosso caso, como não há união física entre os botões, todas as di-
reções deverão possuir seu ícone correspondente, inteiramente contido em
sua célula, sem invadir a área de outro. A célula do centro servirá como
posiçãodedescansododedo:
71

## Página 90

4.4. Criandoumcontroledirecional CasadoCódigo
Figura4.4: Criandoumcontroledirecional
No pacote de downloadsdeste livro (https://github.com/EdyKnopfler/
games-js-2/archive/master.zip),e s t áap a s t ar e l a t i v aae s t ep r o j e t o ,
nave-mobile-1.N a s u b p a s t awww/img,s ee n c o n t r aoa r q u i v o
direcional.png. Copie-oparaa www/imgdoseuprojeto.
Ao final da tag<body>, acrescente uma novadiv contendo esse dire-
cionaleumbotãoparadisparo:
<div id="controles">
<img src="img/direcional.png" id="direcional">
<img src="img/botao-jogar.png" id="disparo">
</div>
SeuposicionamentoseráfeitoviaCSS.Adiv controlesinicialmentese
encontraoculta,poissódeveráaparecerquandoclicarmosnobotão Jogar.
O direcional é posicionado no canto inferior esquerdoeobo tã o ,n oi n f e ri o r
direito,umpoucoafastadodasbordasdatela:
#controles {
display: none;
}
#direcional {
position: absolute;
bottom:0 ;
left:0 ;
}
72

## Página 91

CasadoCódigo Ca p í tulo4. I ncr emen tandoojogodena ve
#disparo {
position: absolute;
right: 40px;
bottom: 64px;
}
Sinta-selivreparamudarasposiçõesetamanhos,semseesquecerqueas
medidasreaisdascélulasinfluirãonaprogramaçãoposteriormente.
Quandoojogoseinicia, oscontrolesdeverãoaparecer. Acrescenteoco-
mandonafunção iniciarJogo:
document.getElementById( ' controles ' ).style.display =
' block ' ;
Etambémosfaçadesaparecerem gameOver:
document.getElementById( ' controles ' ).style.display =
' none ' ;
Configurar o disparo é fácil, basta capturar o eventotouchstart.E m
configuracoesIniciais,faça:
function configuracoesIniciais() {
// ...
// Disparo
document.getElementById( ' disparo ' ).addEventListener(
' touchstart ' ,
function(){
nave.atirar();
somTiro.seekTo(0);
somTiro.play();
}
);
}
JádápraatiraredestruirunsOVNIs! Masvamosiniciarodirecionalem
iniciarObjetos. Seu construtor receberá a imagem na página. Ele tam-
bémserápassadoparaoconstrutorda Nave,comoerafeitocomo Teclado
naversãodesktopdojogo:
73

## Página 92

4.4. Criandoumcontroledirecional CasadoCódigo
function iniciarObjetos() {
// ...
direcional = new Direcional(
document.getElementById( ' direcional ' ));
nave = new Nave(context, direcional, imagens.nave,
imagens.explosao);
// ...
}
Criemos agora a classe Direcional no arquivo direcional.js.
Primeiro, definimos nomes para as direções e recebemos a imagem a ser us-
adanoconstrutor. Osvaloresnãoimportam,contantoquesejamúnicos:
var DIRECAO_NENHUMA =0 ;
var DIRECAO_N =1 ; // norte
var DIRECAO_S =2 ; // sul
var DIRECAO_L =3 ; // leste
var DIRECAO_O =4 ; // oeste
var DIRECAO_NE =5 ; // nordeste
var DIRECAO_NO =6 ; // noroeste
var DIRECAO_SE =7 ; // sudeste
var DIRECAO_SO =8 ; // sudoeste
function Direcional(imagem) {
this.imagem = imagem;
this.direcao = DIRECAO_NENHUMA;
// continua...
}
O que temos que fazer é atribuir eventos de toque à imagem. Vamos
atribuir as funções de evento a variáveis, de forma que cada uma possa ser
usadaemma isdeumev en t o .U made lasér es po n sá v e lpo rca p t ura rascoo r -
denadas,jádescontandoaposiçãodaimagem(offsets ),passando-asparaque
o método
direcaoPonto, a ser criado logo mais, determine a direção. A
outraserviráparafinalizaromovimento,atribuindo DIRECAO_NENHUMAao
direcional:
function Direcional(imagem) {
// ...
74

## Página 93

CasadoCódigo Ca p í tulo4. I ncr emen tandoojogodena ve
var direcional = this ;
var funcaoToque = function(e) {
direcional.direcaoPonto(
e.changedTouches[0].pageX - imagem.offsetLeft,
e.changedTouches[0].pageY - imagem.offsetTop
);
}
var funcaoCancela = function() {
direcional.direcao = DIRECAO_NENHUMA;
}
// continua...
}
Tendoasfunçõesemmãos,vamosatribuí-lasatodososeventosdescritos
no início do capítulo3.N a s e ç ã o3.1foi dito que, no Android, temos que
chamar o preventDefault no touchstart para contornar um bug que
impedeo touchmovedeocorrer:
function Direcional(imagem) {
// ...
imagem.addEventListener( ' touchstart ' , function(e) {
funcaoToque(e);
if( navigator.userAgent.match( /Android/i))
e.preventDefault();
});
imagem.addEventListener( ' touchmove ' , funcaoToque);
imagem.addEventListener( ' touchend ' , funcaoCancela);
imagem.addEventListener( ' touchleave ' , funcaoCancela);
imagem.addEventListener( ' touchenter ' , funcaoToque);
imagem.addEventListener( ' touchcancel ' , funcaoCancela);
}
Permitircontinuarmudandoadireçãono touchmovetornaránossodi-
recional mais suave, sem exigir que o jogador tire o dedo de um ícone para
tocar outro. Já tentei jogar jogos onde não tomaram esse cuidado e achei a
experiênciamuitofrustrante.
75

## Página 94

4.4. Criandoumcontroledirecional CasadoCódigo
A função que recebe o comando de toque passa a responsabilidade de
determinar a direção para o métododirecaoPonto.E s t ed i v i d eaá r e ad a
imagememtrêspartesiguais,tantonalarguraquantonaaltura,edetermina
qualcélulafoitocada. Vejacomofoitestadaaprimeiracolunae,dentrodela,
testamospelaalturaasdireçõesnoroeste,oesteesudoeste:
Direcional.prototype = {
direcaoPonto: function(x, y) {
var larguraCelula = this.imagem.width /3 ;
var alturaCelula = this.imagem.height /3 ;
// 1 ª coluna
if (x < larguraCelula) {
// Verifica qual linha
if (y < alturaCelula)
this.direcao = DIRECAO_NO;
else if (y < alturaCelula *2 )
this.direcao = DIRECAO_O;
else
this.direcao = DIRECAO_SO;
}
// continua...
}
}
Seguindoesteraciocínio,nasegundacoluna,testamosonorte,aposição
dedescansoeosul;enater ceiratestamosonordeste,olest eeosudoeste:
// 2 ª coluna
else if (x < larguraCelula *2 ){
if (y < alturaCelula)
this.direcao = DIRECAO_N;
else if (y < alturaCelula *2 )
this.direcao = DIRECAO_NENHUMA; // Centro do direcional
else
this.direcao = DIRECAO_S;
}
76

## Página 95

CasadoCódigo Ca p í tulo4. I ncr emen tandoojogodena ve
// 3 ª coluna
else {
if (y < alturaCelula)
this.direcao = DIRECAO_NE;
else if (y < alturaCelula *2 )
this.direcao = DIRECAO_L;
else
this.direcao = DIRECAO_SE;
}
Ac l a s s eDirecional está pronta, temos agora que incluí-la no jogo.
Adicioneoscriptno <head>:
<script src="direcional.js"></script>
C o m oe s t a m o sp a s s a n d ooo b j e t od i r e c i o n a ln oc o n s t r u t o rd aNave,
receba-ona functiondaclasseecrieoa trib u toco rr espo nden te:
function Nave(context, direcional, imagem, imgExplosao) {
this.context = context;
this.direcional = direcional;
// ...
}
Da mesma forma que fazia com oTeclado, a nave deverá ler o estado
do Direcionalparadeterminarseusdeslocamentosem xey. Poderíamos
testar direção por direção, mas isso iria darmuito trabalho para testarmos
tambémoslimitesdoCanvasemcadacaso:
// Exemplo teórico
if (dir.direcao == DIRECAO_NO) {
if (this.x >0 )
this.x -= incremento;
if (this.y >0 )
this.y -= incremento;
}
// outras direções...
77

## Página 96

4.4. Criandoumcontroledirecional CasadoCódigo
Emvezdisso,vamostestarporesquerda,direita,acimaeabaixoisolada-
mente. Por exemplo: noroeste, oeste e sudoeste são movimentos para a es-
querda; ou sudoeste, sul e sudeste são movimentos para baixo etc. Comece
testandoessascondiçõesnométodo
atualizarda Nave:
atualizar: function() {
var incremento =
this.velocidade * this.animacao.decorrido / 1000;
var dir = this.direcional;
var esquerda = dir.direcao == DIRECAO_NO ||
dir.direcao == DIRECAO_O ||
dir.direcao == DIRECAO_SO;
var direita = dir.direcao == DIRECAO_NE ||
dir.direcao == DIRECAO_L ||
dir.direcao == DIRECAO_SE;
var acima = dir.direcao == DIRECAO_NO ||
dir.direcao == DIRECAO_N ||
dir.direcao == DIRECAO_NE;
var abaixo = dir.direcao == DIRECAO_SO ||
dir.direcao == DIRECAO_S ||
dir.direcao == DIRECAO_SE;
// continua ...
},
Conseguimos reduzir aos quatro casos originais, para saber se há movi-
mentoem xe/ouem y:
atualizar: function() {
// ...
if (esquerda && this.x >0 )
this.x -= incremento;
if (direita && this.x < this .context.canvas.width -3 6 )
this.x += incremento;
if (acima && this.y >0 )
78

## Página 97

CasadoCódigo Ca p í tulo4. I ncr emen tandoojogodena ve
this.y -= incremento;
if (abaixo && this.y < this.context.canvas.height -4 8 )
this.y += incremento;
},
O método desenhar só precisa testar pela esquerda ou direita, para
sabercomquallinhadaspritesheetvaiexecutaraanimação:
desenhar: function() {
var dir = this.direcional;
if (dir.direcao == DIRECAO_NO ||
dir.direcao == DIRECAO_O ||
dir.direcao == DIRECAO_SO)
this.spritesheet.linha =1 ;
else if (dir.direcao == DIRECAO_NE ||
dir.direcao == DIRECAO_L ||
dir.direcao == DIRECAO_SE)
this.spritesheet.linha =2 ;
else
this.spritesheet.linha =0 ;
this.spritesheet.desenhar( this .x, this.y);
this.spritesheet.proximoQuadro();
},
Por fim, emgameOver,f a ç ac o mq u eom o v i m e n t oc e s s e ,p a r aan a v e
não sair desembestada na próxima partida. Quando temos janelas de alerta,
elas interferem no foco da aplicação, fazendo com que os eventos touch na
imagemnãosejamouvidos. Porexemplo,tirarodedoparadar“OK”noalerta
não força um
touchend na imagem. Por isso, façamos os ajustesantesdo
alerta:
function gameOver() {
// ...
79

## Página 98

4.5. Precisãocommúltiplosdedos CasadoCódigo
direcional.direcao = DIRECAO_NENHUMA;
alert( ' Game Over ' );
}
Tentejogar. Tudofuncionaquasenormalmente... Vejamosporquê.
Figura4.5: Jogodenavecomdirecionaltouch
4.5 Precisãocommúltiplosdedos
Sevocêconseguiujogar,podeacontecerqueanavevásempreparaadireita,
n ãoim po rta n doemq ualposiçãododir ecio n alv ocêes táco modedo .N ãoé
toda hora que acontece, mas é o suficiente para incomodar e fazer com que
alguém dê nota negativa para seu jogo na Play Store. Isto ocorre especifi-
80

## Página 99

CasadoCódigo Ca p í tulo4. I ncr emen tandoojogodena ve
camente se você primeiro der um disparo, mantiver o dedo no botão e, em
seguida,tocarodirecionalcomoutrodedo:
Figura4.6: Comodedonobotãodedisparo,anavemove-separaadireita!
Lembra-sedequeoatributo changedTouchesdoeventoé,naverdade,
um array com todos os dedos na tela? Se já havia um dedo no botão, ele é o
elementozero;otoquenaimagementãocriaoelementonúmero1. Estamos
sempre testando o elemento zero, e como o botão fica mais à direita, nosso
algoritmointerpretaquetocamosaterceiracoluna:
O primeiro passo é, justamente, colocar um limite final, em vez de um
else simples. No métododirecaoPonto da classe Direcional, modi-
fiqueo elsedaterceiracolunaparaincluiracondição:
81

## Página 100

4.5. Precisãocommúltiplosdedos CasadoCódigo
Também vale a pena colocarmos limites noselses finais internos, que
testamaposição y:
// 1 ª coluna
if (x < larguraCelula) {
// ...
else if (y < alturaCelula *3 )
return DIRECAO_SO;
}
// Faça para todas as colunas!
Por fim, no construtor, ao invés de testar somente a posição zero do
changedTouches, vamos fazer um loop e testar todo o array. Não importa
qual a ordem dos dedos, se algum estiver dentro dos limites de uma célula,
deveráserconsiderado. Atenção: nolugardezero,usamosavariáveldeloop
i:
function Direcional(imagem) {
// ...
var funcaoToque = function(e) {
for (var i in e.changedTouches) {
direcional.direcaoPonto(
e.changedTouches[i].pageX - imagem.offsetLeft,
e.changedTouches[i].pageY - imagem.offsetTop
);
}
}
// ...
}
Perceba que, se testarmos os limites exatos de uma área de toque, pode-
mos verificar todo o array de dedos, sem nos preocuparmos com qual ele-
mento do array representa aquele toque. Agora sim nosso controle tem um
tratamentomaisprofissional.
E assim concluímos a primeira versão móvel de nosso jogo de nave! E a
82

## Página 101

CasadoCódigo Ca p í tulo4. I ncr emen tandoojogodena ve
aventura só está começando, porque em um dispositivo móvel inúmeras são
aspossibilidadesdejogabilidade.
4.6 APIdoacelerômetrodoCordova
O acelerômetro é o sensor de movimento de seu dispositivo móvel: aquele
que detecta se você está usando o aparelho em retrato (em pé) ou paisagem
(deitado), por exemplo. Mas ele é capaz de muito mais que isso. Joysticks
comoodoNintendoWiitambémsãobaseadosemacelerômetros. Oqueele
fazédetectarmovimentosnosseguinteseixos:
Figura4.7: Eixosdemovimentaçãomonitoradospeloacelerômetro
Podemoscopiartodaapasta nave-mobile-1 para nave-mobile-2,
ondeiremostrabalharagora. Acesseestapastadoterminal/prompteadicione
opluginparaleituradoacelerômetro:
cordova plugin add org.apache.cordova.device-motion
Na página index.html, deixe somente botão de disparo na div
controles. Se quiser, você pode deletar deste projeto todos os arquivos
83

## Página 102

4.6. APIdoacelerômetrodoCordova CasadoCódigo
relacionados ao direcional (imagem e script), e também a tag<script
src="direcional.js">.
<div id="controles">
<img src="img/botao-jogar.png" id="disparo">
</div>
Na função iniciarObjetos,nãoserámaisiniciadoodirecional,nem
passadoparaoco nstru to rdaNave:
function iniciarObjetos() {
// ...
// Remova esta linha
//direcional = new Direcional(document.getElementById(
// ' direcional ' ));
// Não passe mais o direcional
nave = new Nave(context, imagens.nave, imagens.explosao);
// ...
}
Removatambém,dafunção gameOver,alinhaqueresetaadireção:
direcional.direcao = DIRECAO_NENHUMA;
Oco nstru to rdaclasseNaveficaumpoucomaisenxutosemele:
function Nave(context, imagem, imgExplosao) {
this.context = context;
// Remova
//this.direcional = direcional;
// ...
}
Deixe,porenquanto,osmétodos atualizare desenharcomoscor-
pos comentados. Logo mais, esses métodos vão se valer dos dados do acel-
erômetro. Noentanto,elesnãofarãoasualeituradiretamente,poisfazerisso
84

## Página 103

CasadoCódigo Ca p í tulo4. I ncr emen tandoojogodena ve
no loop de animação émuito lento. Em vez disso, vamos deixar o código
nativodoCordovamonitoraroacelerômetroparanós.
atualizar: function() {
/* comente */
},
desenhar: function() {
/* comente */
},
No index.html,função iniciarJogo,configurelogonoiníciouma
chamadaa navigator.accelerometer.watchAcceleration,quere-
cebeumafunçãodecallbackaserchamadadetemposemtempos. Afrequên-
ciaéconfiguradaemmilissegundos,emumobjetonoúltimoparâmetro. Fiz
vários testes até chegar a um valor que me agradou; você pode experimen-
tar outros intervalos e ajustar conforme cada jogo exigir uma sensibilidade
diferente:
function iniciarJogo() {
acelerometro = navigator.accelerometer.watchAcceleration(
function(aceleracao) {
var msg =
' X: ' + aceleracao.x + ' <br> ' +
' Y: ' + aceleracao.y + ' <br> ' +
' Z: ' + aceleracao.z;
document.getElementById( ' controles ' ).innerHTML = msg;
},
function() {
alert( ' Erro! ' );
},
{ frequency:2 5}
);
// ...
}
Rodeoprojetoevejaosvalores. Obotãodedisparosomeporqueestamos
sobrescrevendotodooconteúdoda div(masissoétemporário):
85

## Página 104

4.6. APIdoacelerômetrodoCordova CasadoCódigo
Figura4.8: Obtendodadosdoacelerômetro
Balanceoaparelhoeconfiraosvaloresconformeadireçãodeinclinação:
• Esquerda: x>0
• Direita: x<0
• Cima: y<0
• Baixo: y>0
Para nossos propósitos, o eixoz não é necessário. Podemos então passar
osvaloresobtidosparaanave:
86

## Página 105

CasadoCódigo Ca p í tulo4. I ncr emen tandoojogodena ve
function iniciarJogo() {
acelerometro = navigator.accelerometer.watchAcceleration(
function(aceleracao) {
nave.aceleracao.x = aceleracao.x;
nave.aceleracao.y = aceleracao.y;
},
function() {
alert( ' Erro! ' );
},
{ frequency:25 }
);
// ...
}
Reparequecriamosoatributo aceleracaonanave. Vamosiniciá-lono
construtor com um objeto contendo os dois eixos usados e o valor zero para
cadaum:
function Nave(context, imagem, imgExplosao) {
// ...
this.aceleracao = {x :0 ,y :0 };
}
O método atualizar fará a leitura dos dados e movimentará a nave
conforme o sentido em que balançamos o aparelho, cujos testes vimos há
pouco:
atualizar: function() {
var incremento =
this.velocidade * animacao.decorrido / 1000;
var acc = this.aceleracao;
if (acc.x >0& &this.x >0 )
this.x -= incremento;
if (acc.x <0& &this.x < this.context.canvas.width -3 6 )
this.x += incremento;
87

## Página 106

4.7. AdaptandooCanvasaotamanhodatela CasadoCódigo
if (acc.y <0& &this.y >0 )
this.y -= incremento;
if (acc.y >0& &this.y < this.context.canvas.height -4 8 )
this.y += incremento;
},
Omesmovaleparaométodo desenhar:
desenhar: function() {
var acc = this.aceleracao;
if (acc.x >0 )
this.spritesheet.linha =1 ;
else if (acc.x <0 )
this.spritesheet.linha =2 ;
else
this.spritesheet.linha =0 ;
this.spritesheet.desenhar( this .x, this.y);
this.spritesheet.proximoQuadro();
},
Na função gameOver, vamos parar de monitorar o acelerômetro
chamando navigator.accelerometer.clearWatch:
function gameOver() {
navigator.accelerometer.clearWatch(acelerometro);
// ...
}
Comeceasedivertir! Faleaverdade,ficouemocionante,nãoficou?
4.7 AdaptandooCanvasaotamanhodatela
Em3.3,aprendemosacriarumCanvasqueseadaptaàtelaviaCSS.Comoas
imagens geradas eram dimensionadas, isto requeria que cada elemento grá-
ficotivesseumtamanhorazoável,afimdeseadaptaratelasmaiores.
88

## Página 107

CasadoCódigo Ca p í tulo4. I ncr emen tandoojogodena ve
Vamos fazer diferente agora: configurar dinamicamente o Canvas para
o tamanho exato disponível na tela. Estamos configurando os atributos da
tag, width e height. Os valores vêm dos atributos availWidth e
availHeight do objeto screen, que nos dão a largura e a altura da tela,
descontadas barras de tarefas, de botões e de ícones indicadores do sistema
operacional. Façamos isto na função
iniciar, onde ocorre a inicialização
doapp:
function iniciar() {
canvas = document .getElementById( ' jogo_nave ' );
context = canvas.getContext( ' 2d ' );
canvas.width = screen.availWidth;
canvas.height = screen.availHeight;
carregarImagens();
carregarSons();
}
Como o Canvas vai ocupar a tela toda, temos que fazer uso do atributo
z-index do CSS para que os botõesJogar e de disparo fiquem por cima.
Estesr ecebemovalo r1,enquan tooCan vasr ecebeovalo rzer o:
body { /* não mudou */ }
#jogo_nave {
position: absolute;
z-index:0 ;
}
#link_jogar {
display: none ;
position: absolute;
z-index:1 ;
bottom: 20px;
width: 100%;
text-align : center;
}
#link_jogar a { /* não mudou */ }
89

## Página 108

4.7. AdaptandooCanvasaotamanhodatela CasadoCódigo
#controles { /* não mudou */ }
#direcional { /* desaparece */ }
#disparo {
position: absolute;
right: 10px;
bottom: 10px;
z-index:1 ;
}
As adaptações ao jogo de nave acabam aqui. Você agora tem uma base
bastante robusta para criar jogos móveis em estilo arcade, além de mais di-
versãoparaafiladobancooudosupermercado! Nopróximocapítulo,dare-
mos início à construção de uma mesa de bilhar móvel, usando o framework
Hammer.jsparacontrolarastacadas.
90

## Página 109

CasadoCódigo Ca p í tulo4. I ncr emen tandoojogodena ve
Figura4.9: Jogocomacelerômetroocupandoatela
91

## Página 111

Capítulo5
Interaçõesavançadascom
Hammer.js
Neste capítulo, você aprenderá a capturar gestos comuns, porém mais com-
plexos,deformapráticacomabiblioteca Hammer.js. Apartirdaqui,umpe-
queno jogo de bilhar começará a tomar forma. Deixaremos o jogador rota-
cionarotacocomosdedoseregularaforçadatacadaarrastandoumponteiro
natela.

## Página 112

5.1. ConhecendooHammer.js CasadoCódigo
Figura5.1: Tacodebilhartouch
5.1 ConhecendooHammer.js
Gestoscomuns
Você está navegando na internet e surge uma página com letras miúdas. O
quevocêprecisafazer? Darzoom. Comodarzoomnobrowserdodispositivo
móvel? Com o gesto chamadopinch (pinça), que consiste em colocar dois
dedosnatelaeafastá-losouaproximá-los. Afastandoosdedos,vocêdázoom;
aproximando,vocêtiraozoom.
94

## Página 113

CasadoCódigo Capítulo5. InteraçõesavançadascomHammer.js
Figura5.2: Fazendoapinçaparaajustarozoom
Existetambémumgestousadoparagirarcoisas. Ogestoderotação( ro-
tate) é usado, por exemplo, no Google Earth. Você coloca dois dedos na tela
egiracomoseestivessecochandoumparafuso:
95

## Página 114

5.1. ConhecendooHammer.js CasadoCódigo
Figura5.3: Girandooglobocomogestorotate
Outrosgestosusuaissão:
• Tap(toque): toquerápido;
• Press (pressionar): manter o dedo sobre um objeto por um curto in-
stan te.N o rmalmen teab r eummen uco n textual;
• Swipe(deslizar): moverodedorapidamentedeumpontoaoutro. Us-
adoparapassarfotosnatela,abrirmenusocultosemappsevirarpági-
naseme-books;
• Panoudrag(arrastar): deslocamentodeumobjetocomodedo.
96

## Página 115

CasadoCódigo Capítulo5. InteraçõesavançadascomHammer.js
Tecnicamente,adiferençaentreo swipeeo panéavelocidade: o swipesó
ocorreapartirdeumavelocidademínimadefinida.
Implementar esses gestos usando a API de mais baixo nível do HTML5
é relativamente complexo. Para reconhecer um simplespress, por exemplo,
você iniciaria a contagem do tempo notouchstart e a interromperia no
touchend. Umtimeoutpoderiaserdisparadoseodedofoimantidonoob-
jetopelotempoquevocêdeterminar:
// Exemplo teórico
elemento.addEventListener( ' touchstart ' , function() {
timeout = setTimeout(press, 500);
});
elemento.addEventListener( ' touchend ' , function() {
clearTimeout(timeout);
});
function press() {
// Executo minha ação
}
Isso porque não estamos considerando se o usuário moveu o dedo ou
não. Se quiséssemos evitar, teríamos que cancelar otimeout também no
touchmove. No capítulo3, implementamos umpan para fazer uma bruxa
voar pelo Canvas. Se quiséssemos restringir o movimento somente na verti-
calounahorizontal,láseiammaisumaslinhasdecódigo. O pincheorotate
jásãoumcasoapartedecomplexidade.
Felizmente, todos esses eventos já se encontram implementados na bib-
liotecaHammer.js. Eoqueémelhor: sãoreconhecidosnãosóemtelastouch,
mastambématravésdomouse!
UsandooHammer.js
Odo wnloaddab iblio tecapodeserfei toem:http://hammerjs.github.io/.
Tendo linkado o arquivo na página, se quisermos reconhecer o gesto de
arrastar, primeiro devemos instanciar um objetoHammer,p a s s a n d ooe l e -
m e n t od ap á g i n an oc o n s t r u t o r .D e p o i s ,om é t o d oon manda o Hammer.js
reconhecerumevento. Passoparaeleastring 'pan'eocallback:
97

## Página 116

5.1. ConhecendooHammer.js CasadoCódigo
<script src="hammer.min.js"></script>
<script>
var canvas = ...
var hammer = new Hammer(canvas);
hammer.on( ' pan ' , function(e) {
console.log(e.center.x + ' , ' + e.center.y);
});
</script>
Os eventos podem ser destrinchados: em vez de simplesmentepan,
poderíamos dizer panstart, panmove ou panend. E, melhor ainda:
panleft, panright, panup, pandown!( panup e pandown ainda não
funcionam,maslogovocêsaberáporquê.)
EventosreconhecidospeloHammer.js
AquiestãooseventospadrãodoHammer.jseseusvariantes:
• tap
• press
• pan e panstart, panmove, panend, pancancel, panleft, panright,
panup,pandown
• swipeeswipeleft,swiperight,swipeup,swipedown
• pinchepinchstart,pinchmove,pinchend,pinchcancel,pinchin,pin-
chout
• rotateerotatestart,rotatemove,rotateend,rotatecancel
Mas calma: nem tudo isso funcionará de imediato. Os eventospinch
e rotate são desabilitados por padrão, e opan eo swipe só detectam
98

## Página 117

CasadoCódigo Capítulo5. InteraçõesavançadascomHammer.js
inicialmente movimentos na horizontal. O motivo disso é que esses gestos
são reservados em páginas web: fazer a pinça para dar zoom e arrastar na
verticalpararolarapágina. Obrowsernãointerpretao rotate, masosdedos
podemseafastarouaproximareum pinchocorrerá. Nocasodejogoseapps
em geral, como estamos sempre restringindo a tela, podemos habilitar esses
gestos:
hammer.get( ' pinch ' ).set({ enable : true });
hammer.get( ' rotate ' ).set({ enable : true });
Etambémhabilitarasdireçõesdesejadasparao paneo swipe:
hammer.get( ' pan ' ).set({ direction : Hammer.DIRECTION_ALL });
hammer.get( ' swipe ' )
.set({ direction: Hammer.DIRECTION_VERTICAL });
Asconstantesem Hammersão:
• DIRECTION_NONE
• DIRECTION_LEFT
• DIRECTION_RIGHT
• DIRECTION_UP
• DIRECTION_DOWN
• DIRECTION_HORIZONTAL
• DIRECTION_VERTICAL
• DIRECTION_ALL
Uma configuração a que devemos prestar atenção é athreshold,q u e
define o deslocamento mínimo para um evento ocorrer. No caso dopan,o
valorpadrãoé10pixels! Podemossetá-lacomozero,paraumdeslocamento
sua ve.P arapodermosarrastarumob jetolivr emen te,ocódigofica:
99

## Página 118

5.1. ConhecendooHammer.js CasadoCódigo
hammer.get( ' pan ' ).set({
direction: Hammer.DIRECTION_ALL,
threshold:0
});
hammer.on( ' pan ' , function(e) {
// ...
});
Nocallback,umdosatributosmaisimportantesdoeventoé center,que
contémascoordenadas xe ydopontocentralentreosdedos,oudopróprio
dedo,sehouverumsó,comonoúltimoexemplo. Nocasodeum rotateou
pinch,porexem plo ,aposiçãodecadadedoestarianoa tributo pointers,
queéumarra yco mosdedosnatela:
hammer.get( ' rotate ' ).set({ enable : true });
hammer.on( ' rotate ' , function(e) {
console.log( ' Centro: ' + e.center.x + ' , ' + e.center.y);
console.log( ' Dedo 1: ' + evento.pointers[0].pageX + ' , ' +
evento.pointers[0].pageY);
console.log( ' Dedo 2: ' + evento.pointers[1].pageX + ' , ' +
evento.pointers[1].pageY);
});
TendofeitoestaintroduçãoaoHammer.js,podemoscomeçarautilizá-lo
emnossojogodeb ilhar .
DocumentaçãodoHammer.js
Vocêpodeobtermaisinformaçõesem:
http://hammerjs.github.io/getting-started/
LáseencontraumadescriçãodetalhadadaAPIedoseventos(recog-
nizers).
100

## Página 119

CasadoCódigo Capítulo5. InteraçõesavançadascomHammer.js
5.2 Barradeajustedeforça
Vamos começar pelo mais fácil: uma barra para o jogador ajustar a força da
tacada. Elapossuiráumponteiroarrastáveldentrodosseuslimites.
Comece criando o projeto taco-bilhar, adicione a plataforma An-
droideadicioneoplugindemultimídia:
cordova create taco-bilhar
cd taco-bilhar
cordova platform add android
cordova plugin add org.apache.cordova.media
No pacote de download do livro, na pasta
taco-bilhar/platforms/android/assets, existe o arquivo
colisao.mp3. Esteéosomdatacada. Copie-oparaapastade assetsdo
seuprojeto. Copietambémasimagensdapasta www/img.
Tambémconfigureno config.xmlaorientação landscape(deitado),
eumíconeparaoprojeto. Nodownloadjáháumíconenapastadeimagens.
Sedesejar,vocêpodeprocuraroucriaraimagemquepreferir:
<preference name="Orientation" value= "landscape" />
<icon src="www/img/icone.png" />
C o l o q u en ap a s t awww os scripts do requestAnimationFrame ed o
Hammer.js. Oesqueletodo index.htmlficaráassim:
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,
height=device-height, user-scalable=no,
initial-scale=1, maximum-scale=1, minimum-scale=1" >
<title>Taco de Bilhar</title>
<script src="cordova.js"></script>
<script src="rAF.js"></script>
<script src="hammer.min.js"></script>
101

## Página 120

5.2. Barradeajustedeforça CasadoCódigo
<script src="barra-forca.js"></script>
<script src="taco.js"></script>
<script>
// inicialização
</script>
<style>
/* folha de estilo */
</style>
</head>
<body>
<canvas id="taco_bilhar"></canvas>
</body>
</html>
Dentrodatag <style>,coloqueoCSSparaajustaroCanvasconforme
aprendemos,deixando-oresponsivodeacordocomaalturadatela:
body {
margin:0 ;
width: 100%;
height: 100%;
background :# 3 3 3 ;
}
canvas {
height: 100%;
width: auto;
display: block ;
margin:0auto;
}
Façamos a inicialização do jogo, configurando o Canvas e carregando as
imagensesons. Aslinhasquenãorodamnobrowserdesktopforamcomen-
tadas,vocêpoderádescomentá-lasdepoisquandoformostestarnocelularou
tablet:
102

## Página 121

CasadoCódigo Capítulo5. InteraçõesavançadascomHammer.js
var canvas, context;
var imgTaco, imgPonteiro, somTacada;
var taco, barraForca;
window.onload = function() {
canvas = document .getElementById( ' taco_bilhar ' );
context = canvas.getContext( ' 2d ' );
canvas.width = screen.availWidth;
canvas.height = screen.availHeight;
//document.addEventListener( ' deviceready ' , iniciar);
iniciar();
}
function iniciar() {
imgTaco = new Image();
imgTaco.src = ' img/taco.png ' ;
imgPonteiro = new Image();
imgPonteiro.src = ' img/ponteiro.png ' ;
//somTacada = new Media( ' file:///android_asset/colisao.mp3 ' );
iniciarObjetos();
requestAnimationFrame(animar);
}
Afunção iniciarObjetoscriaráosobjetos tacoe barraForca.O
controledotacodebilharpossuiráumaáreacircular,dentrodaqualfaremos
ogestoderotação. Jáabarradeforçaseráretangular:
function iniciarObjetos() {
taco = new Taco(context, imgTaco);
taco.raio = 120;
taco.x = 125;
taco.y = canvas.height /2-5 0 ;
barraForca = new BarraForca(context, imgPonteiro, taco);
barraForca.x = taco.x - 100;
barraForca.y = taco.y + taco.raio +2 5 ;
103

## Página 122

5.2. Barradeajustedeforça CasadoCódigo
barraForca.largura = 200;
barraForca.altura =5 0 ;
}
Por enquanto, o loop de animação será feito através de uma função sim-
ples. Basicamente pintamos o Canvas de verde, desenhamos o taco e a barra
deforçaechamamosopróximociclo:
function animar() {
// Fundo verde
context.save();
context.fillStyle = ' #050 ' ;
context.fillRect(0, 0, canvas.width, canvas.height);
context.restore();
taco.desenhar();
barraForca.desenhar();
requestAnimationFrame(animar);
}
Para podermos testar no Console sem ver nada faltando, já crie o es-
queletodaclasse Taconoarquivo taco.js:
function Taco(context, imagem) {
this.context = context;
this.imagem = imagem;
this.raio =0 ;
this.x =0 ;
this.y =0 ;
this.rotacao =0 ;
this.forca =0 ;
}
Taco.prototype = {
desenhar: function() {
}
}
Eodaclasse BarraForcaem barra-forca.js:
104

## Página 123

CasadoCódigo Capítulo5. InteraçõesavançadascomHammer.js
function BarraForca(context, ponteiro, taco) {
this.context = context;
this.ponteiro = ponteiro;
this.taco = taco;
this.x =0 ;
this.y =0 ;
this.largura =0 ;
this.altura =0 ;
this.forca =0 ;
}
BarraForca.prototype = {
desenhar: function() {
}
}
Até aqui, teste no navegador. O único erro deve ser a falta do
cordova.js.
Vamos desenhar a barra de força. Veja na figura5.1q u ee l ap o s s u id o i s
retângulos: um interno, representando a força atual, e um externo que de-
limita a área. O externo é desenhado na largura total da barra, saindo um
pouco fora de seus limites para não encobrir o outro. Já o interno é desen-
hado de acordo com a força atualmente setada no objeto multipliquei essa
f o r ç ap o r2p a r aab a r r an ã ofi c a rm u i t op e q u e n a .Ap o s i ç ã od op o n t e i r oé
calculada por outro método,
posicaoPonteiro, já pensando que vamos
precisardessaposiçãoaodetectaro pansobreele:
desenhar: function() {
var ctx = this.context;
// Contêiner
ctx.strokeRect(this.x -2 , this.y -2 , this.largura +4 ,
this.altura +4 );
// Força
ctx.save();
ctx.fillStyle = ' #900 ' ;
105

## Página 124

5.2. Barradeajustedeforça CasadoCódigo
ctx.fillRect(this.x, this.y, this.forca *2 , this.altura);
ctx.restore();
// Ponteiro
var pos = this.posicaoPonteiro();
ctx.drawImage(this.ponteiro, pos.x, pos.y,
this.ponteiro.width, this.ponteiro.height);
}, // Atenção para a vírgula
Em posicaoPonteiro, precisamos colocar a ponta da seta, que hor-
izontalmente está no meio da imagem, na mesma posiçãox que o final da
barra de força. Por isso multiplicamos a força por 2 e descontamos metade
dalarguradaimagem. Jáaposição yénametadedabarra,masnadaimpede
quesejaumpoucoacimaouabaixo:
posicaoPonteiro: function() {
var x = this.x + this.forca *2-this.ponteiro.width /2 ;
var y = this.y + this.altura /2 ;
return {x:x, y:y};
}
Atribuadiferentesvaloresaoatributo forca,noconstrutor,evátestando
n ob r o w s e r . .Ab a r r ai n t e r n aeop o n t e i r od e verão se ajustar. Volte depois o
valorpadrãoparazero.
Vamosagoradetectarotoquenoponteiro. Em iniciarObjetos,inicie
oH ammer .jsejáopassetan toparao tacoquantoparaa barra:
function iniciarObjetos() {
var hammer = new Hammer(canvas);
taco = new Taco(context, imgTaco, hammer);
// ...
barraForca =
new BarraForca(context, imgPonteiro, taco, hammer);
// ...
}
106

## Página 125

CasadoCódigo Capítulo5. InteraçõesavançadascomHammer.js
Faça o construtor da BarraForca recebê-lo e detectar os eventos de
pan. Nãofizemosoajustedadireçãoporquequeremosmovimentarsomente
naho rizo n tal,queéopadrãopermitidopeloevento:
function BarraForca(context, ponteiro, taco, hammer) {
// ...
var barra = this;
hammer.get( ' pan ' ).set({ threshold :0});
hammer.on( ' panstart ' , function(e) {
barra.iniciarAjusteForca(e);
});
hammer.on( ' panmove ' , function(e) {
barra.ajustarForca(e);
});
hammer.on( ' panend ' , function(e) {
barra.finalizarAjusteForca(e);
});
}
No panstart, chamamos o métodoiniciarAjusteForca.C o m o
nossoCanvaséresponsivo,temosprimeiroqueconverteraposiçãodotoque
em coordenadas da imagem processada em memória, como vimos em3.3.
Quemfaráistoéométodo converterParaCanvas:
posicaoPonteiro: function() {
// ...
}, // Não esqueça da vírgula quando for acrescentar métodos!
iniciarAjusteForca: function(evento) {
var canvas = this.context.canvas;
// Coordenadas na imagem do Canvas
var toque = this.converterParaCanvas(
evento.center.x - canvas.offsetLeft,
evento.center.y - canvas.offsetTop
);
107

## Página 126

5.2. Barradeajustedeforça CasadoCódigo
// continua...
},
Em seguida, verificamos se a posição tocada se encontra nos limites do
ponteiro. Seoponteirofoitocado,sinalizamosqueestamosmexendonaforça
ejáchamamosométodoquefazoa juste:
iniciarAjusteForca: function(evento) {
// ...
// Posição do ponteiro
var pos = this.posicaoPonteiro();
var largura = this.ponteiro.width;
var altura = this.ponteiro.height;
// Testar os limites
if (toque.x >= pos.x && toque.x <= pos.x + largura &&
toque.y >= pos.y && toque.y <= pos.y + altura) {
this.ajustandoForca = true;
this.ajustarForca(evento);
}
}, // Ainda tem mais métodos...
Somente relembrando, converterParaCanvas faz uma regra de três
correspondendoàsdimensõesemteladoCanvas( offsets)comassuasdimen-
sõesdeimagem“real":
converterParaCanvas : function(x, y) {
var canvas = this.context.canvas;
return {
x: canvas.width * x / canvas.offsetWidth,
y: canvas.height * y / canvas.offsetHeight
}
},
N o t eq u eom é t o d oajustarForca, além de ser o tratador do evento
panmove, foi também chamado nopanstart para iniciar o movimento.
108

## Página 127

CasadoCódigo Capítulo5. InteraçõesavançadascomHammer.js
Testamosseummovimentoválido(dentrodoslimites)foiiniciado,converte-
mosaposiçãoparaoCanvasesetamosaforçadeacordocomaposiçãodentro
dabarra. Observequedividimosanovamedidapor2,poisaforçaémostrada
emtelacomodobrodotamanho. Tambémlimitamosaforçaentrezeroe100,
esetamosafo r çanoob jeto
Tacoassociado:
ajustarForca: function(evento) {
// Está dentro do limite?
if (this.ajustandoForca) {
var canvas = this.context.canvas;
// Converter para Canvas
var toque = this.converterParaCanvas(
evento.center.x - canvas.offsetLeft,
evento.center.y - canvas.offsetTop
);
// Nova força
this.forca = (toque.x - this.x) /2 ;
// Limites
if (this.forca <0 ) this.forca =0 ;
if (this.forca > 100) this.forca = 100;
// Força do taco
this.taco.forca = this.forca;
}
},
Noevento panend,ométodo finalizarAjusteForcaapenasrealiza
oúltimomovimentonoponteiroesinalizaofimdamovimentação:
finalizarAjusteForca : function(evento) {
if (this.ajustandoForca) {
this.ajustarForca(evento);
this.ajustandoForca = false;
}
} // Esta classe acabou!
109

## Página 128

5.3. Rotacionandoumtacodebilhar CasadoCódigo
F a ç aot e s t e ,t a n t on ob r o w s e rc o m oa g o r an oa p a r e l h om ó v e l .S ev o c ê
fez tudo direitinho, já é possível mexer o ponteiro dentro do limite da barra,
tantocomomousequantonatelatouch.
5.3 Rotacionandoumtacodebilhar
Nesta seção, iremos nos divertir um pouco com o eventorotate do Ham-
mer.js. Forneceremosumaáreacircular,ondeojogadorpoderádefiniroân-
gulodotacorealizandoumarotaçãocomdoisdedos.
Primeiro, em
taco.js, no métododesenhar da classe, desenhe essa
á r eaeota c o .E s t epo s s u i1 5p i x e l sd el a rgura, portanto descontamos 7 pixels
daposição xparaficaraproximadamentenomeio. Naposição y,so mamos
afo r çaasera plicada:quan tomaio rafo r ça,maio radistância:
desenhar: function() {
var ctx = this.context;
// Área de controle
ctx.beginPath();
ctx.arc(this.x, this.y, this.raio, 0, Math.PI*2);
ctx.stroke();
// Taco
ctx.drawImage(this.imagem, this.x -7 ,
this.y + this.forca,
this.imagem.width,
this.imagem.height);
}
Já é possível controlar a força pela barra: o taco se move junto, experi-
mente! Istoocorreporque,aomovimentarabarradeforça,estasetaoatrib-
uto forcadotaco.
Para desenhar o taco rotacionado, podemos usar o métodorotate do
contexto gráfico, que rotaciona o Canvas. Considerando que queremos tra-
balharemgraus,precisamosconverterarotaçãopararadianos. Émuitoim-
portantefazermosusodo
saveedo restoreparadesfazerarotaçãoassim
queotacofordesenhado:
110

## Página 129

CasadoCódigo Capítulo5. InteraçõesavançadascomHammer.js
desenhar: function() {
var ctx = this.context;
// Área de controle
ctx.beginPath();
ctx.arc(this.x, this.y, this.raio, 0, Math.PI*2);
ctx.stroke();
// Taco
var radianos = this.rotacao * Math.PI / 180;
ctx.save();
ctx.rotate(radianos);
ctx.drawImage(this.imagem, this.x -7 , this.y + this.forca,
this.imagem.width, this.imagem.height);
ctx.restore();
}
Experimente testar, no construtor, valores diferentes no atributo
rotacao. O taco fica meio deslocado! Se o valor for muito alto, ele chega
asairdatela. IssoaconteceporqueocentroderotaçãodoCanvaséseuponto
deorigem(0,0):
111

## Página 130

5.3. Rotacionandoumtacodebilhar CasadoCódigo
Figura5.4: OCanvasrotacionapenduradonoponto(0,0)
Felizmente, também temos o métodotranslate, que desloca o ponto
(0, 0) para onde quisermos. Colocando a origem do Canvas na posição do
taco, podemos então rotacioná-lo. Repare nos parâmetros dodrawImage:
comoCanvastransladado,éapartirdoponto(0,0)queinformamosodeslo-
camentodotaco:
// Taco
var radianos = this.rotacao * Math.PI / 180;
ctx.save();
ctx.translate(this.x, this.y);
ctx.rotate(radianos);
ctx.drawImage(this.imagem, -7, this.forca,
this.imagem.width, this.imagem.height);
ctx.restore();
112

## Página 131

CasadoCódigo Capítulo5. InteraçõesavançadascomHammer.js
Figura 5.5: Deslocando a origem do Canvas, rotacionamos e fazemos o de-
senhoapartirde(0,0)
Capturandooevento rotate
N ãoseesq ueçader eseta roa tri b u t orotacao parazero. Arotaçãoserá
definidapelacapturadoevento rotatedoHammer.js. Noconstrutor,con-
figureoseventosàsemelhançadoquefizemoscomabarradeforça:
function Taco(context, imagem, hammer) {
// ...
var taco = this;
hammer.get( ' rotate ' ).set({ enable: true, threshold:0});
hammer.on( ' rotatestart ' , function(e) {
taco.iniciarRotacao(e);
});
hammer.on( ' rotatemove ' , function(e) {
taco.rotacionar(e);
});
hammer.on( ' rotateend ' , function(e) {
taco.finalizarRotacao(e);
});
}
113

## Página 132

5.3. Rotacionandoumtacodebilhar CasadoCódigo
Também semelhantemente à outra classe, vamos converter as posições
para o Canvas eminiciarRotacao. Só que agora são dois dedos. Nosso
objetivo é saber se os pontos tocados estão na área delimitada. Para isso,
chamamosométodo naArea: seesteretornarverdadeiroparaosdoisdedos,
sinalizamosoiníciodarotação:
// Atenção para as vírgulas!
iniciarRotacao: function(evento) {
var canvas = this.context.canvas;
var dedo1 = this.converterParaCanvas(
evento.pointers[0].pageX - canvas.offsetLeft,
evento.pointers[0].pageY - canvas.offsetTop
);
var dedo2 = this.converterParaCanvas(
evento.pointers[1].pageX - canvas.offsetLeft,
evento.pointers[1].pageY - canvas.offsetTop
);
if (this.naArea(dedo1.x, dedo1.y) &&
this.naArea(dedo2.x, dedo2.y)) {
this.rotacionando = true;
this.rotacaoInicial = this.rotacao;
this.rotacionar(evento);
}
},
Ométodo converterParaCanvaséomesmo:
converterParaCanvas : function(x, y) {
var canvas = this.context.canvas;
return {
x: canvas.width * x / canvas.offsetWidth,
y: canvas.height * y / canvas.offsetHeight
}
},
114

## Página 133

CasadoCódigo Capítulo5. InteraçõesavançadascomHammer.js
Ométodo naAreaverifica,peloTeoremadePitágoras,seumpontoper-
tenceaumaáreacircular(figura 3.3):
naArea: function(x, y) {
var distanciaX = Math .abs(this.x - x);
var distanciaY = Math .abs(this.y - y);
// Pitágoras
if (distanciaX * distanciaX + distanciaY * distanciaY <=
this.raio * this.raio)
return true ;
else
return false ;
},
A rotação continua: o método rotacionar obtém o atributo
rotationdoevento,queédadoemgraus. Nãopodemosirapenassomando
os valores pois, a cadarotatemove que chama este método, aumentamos
a rotação naquela quantidade de graus. Em vez disso, sempre partimos da
rotaçãoinicial. Também,parasimplificar,mantemosovalordentrodolimite
de360graus:
rotacionar: function(evento) {
if (this.rotacionando) {
var rotacao = this.rotacaoInicial + evento.rotation;
this.rotacao = rotacao % 360;
}
},
115

## Página 134

5.3. Rotacionandoumtacodebilhar CasadoCódigo
Arcoscôngruos
Existearcode2100°? Sim,istosignificadar5voltasnacircunferência
eandarmais300°:
Figura5.6: 2100°e300°sãocôngruos,poisparamnomesmoponto
Se a nova rotação do taco de bilhar passar de 360°, o resto da sua di-
visãopor360éumarcoequivalente. Porissousamosooperadormódulo
( % )doJavaScript,quedevolveorestodeumadivisãodeinteiros.
Ométodo finalizarRotacaoapenasfazomovimentofinalesinaliza
quearotaçãoterminou:
finalizarRotacao: function(evento) {
if (this.rotacionando) {
this.rotacionar(evento);
this.rotacionando = false;
}
}
Tente fazer o movimento de rotação com 2 dedos dentro da área, e tam-
bém controle a força da tacada. Você pode achar que ainda não está muito
fácilrotacionarotaco. Vejamosporquê.
Capturandodoisoumaisgestosjuntos
É difícil fazer umrotatepuro com os dedos, de forma que o Hammer.js
detecte o gesto exatamente como umrotate. Com um pouco de treino, até
se “pega o jeito”, mas não é exatamente isso que um jogador frustrado pode
116

## Página 135

CasadoCódigo Capítulo5. InteraçõesavançadascomHammer.js
pensar. A razão é que qualquer deslocamento mínimo dos dedos pode ser
interpretadocomoum pinch.
Podemos tornar o movimento mais suave solicitando que os dois gestos
sejam reconhecidos juntos. No construtor, antes de atribuir os tratadores de
evento, obtenha referências ao
pinch ea o rotate e, em seguida, chame o
método recognizeWithemumdeles,passandoooutrocomoparâmetro:
function Taco(context, imagem, hammer) {
// ...
// Configuração dos gestos para serem reconhecidos juntos
var pinch = hammer.get( ' pinch ' );
var rotate = hammer.get( ' rotate ' );
hammer.get( ' pinch ' ).set({ enable : true, threshold:0});
hammer.get( ' rotate ' ).set({ enable : true, threshold:0});
pinch.recognizeWith(rotate);
// Eventos
var taco = this;
hammer.on( ' rotatestart ' , function(e) {
taco.iniciarRotacao(e);
});
// ...
}
Experimentenovamente. Ficoumaisfácil,não?
5.4 Animandoatacada
V a m o sd i s p a r a rot a c oc o mt o d aaf o r ç a !N oindex.html, acrescente uma
imagemapósatag <canvas>. Jáháumaimagemnopacote,masvocêpode
escolherumadeseugosto:
<img src="img/tacada.png" id="tacada" >
NoCSS,posicione-aondequiser:
117

## Página 136

5.4. Animandoatacada CasadoCódigo
#tacada {
position: absolute;
right: 20px;
top: 20px;
}
Nafunção iniciarObjetos,vamosprogramaro touchstartdaim-
agem. Nocallback,preparamososomeiniciamosatacada,comduraçãode
50ms:
function iniciarObjetos() {
// ...
var imgTacada = document.getElementById( ' tacada ' );
imgTacada.addEventListener( ' touchstart ' , function() {
somTacada.seekTo(0);
taco.darTacada(50);
});
}
Não esqueça de descomentar a linha que instancia o som na função
iniciar:
somTacada = new Media( ' file:///android_asset/colisao.mp3 ' );
Devoltaàclasse Taco,ométodo darTacadavaiiniciarindiretamente
uma animação, apenas sinalizando que a tacada está ocorrendo. Por isso,
guardamos o instante em que a tacada começou, para calcular a posição do
taconodecorrerdaanimação:
darTacada: function(duracao) {
this.tacada = true;
this.duracaoTacada = duracao;
this.inicioTacada = Date.now();
},
Podemos disparar animações apenas setando um atributo de um objeto,
seemalgumlugarnoseuciclodeanimaçãoeleseencarregardeleresseatrib-
uto. Ao desenhar a imagem, em vez de deslocar o taco emy pelo montante
118

## Página 137

CasadoCódigo Capítulo5. InteraçõesavançadascomHammer.js
da força, vamos chamar um método,deslocamento, que verificará se a
animaçãodatacadaestáocorrendo:
desenhar: function() {
// ...
ctx.drawImage(this.imagem, -7, this.deslocamento(),
this.imagem.width, this.imagem.height);
// ...
},
Nessenovométodo,primeiroverificamosseaanimaçãoestáocorrendo.
Casocontrário,usamosaforçaparadeslocarotaco:
deslocamento: function() {
// Não foi disparada tacada
if (! this.tacada) return this .forca;
// continua ...
}
Continuando, para calcular o deslocamento temos que saber quanto
temposepassoudesdeoiníciodaanimação. Seaforçaé100equerodeslocar
em 50ms, dá 2 unidades de força por milissegundo (100/50). Multiplico isso
pelotempodecorridoeseiquantootacovaisedeslocarnaquelequadro:
// Tempo decorrido
var agora = Date.now();
var decorrido = agora - this .inicioTacada;
// Deslocamento acumulado
var distancia = this.forca / this.duracaoTacada * decorrido;
Depois, verificamos se o tempo excedeu. Em caso positivo, podemos
deslocar o taco no montante exato da força e finalizar a animação. A nova
posição do taco será a força (afastamento máximo) menos o deslocamento
atual(quantootacovoltaemdireçãoaocentrodocírculo):
119

## Página 138

5.4. Animandoatacada CasadoCódigo
// Completou
if (decorrido >= this.duracaoTacada) {
distancia = this.forca;
this.tacada = false;
}
return this .forca - distancia;
Quando um evento se encerra, podemos receber uma notificação para
começaroutro. Porexemplo, quandoatacadaterminar,ojogopodereceber
umavisoparacomeçaraanimaçãodasbolasnamesa:
// Completou
if (decorrido >= this.duracaoTacada) {
distancia = this.forca;
this.tacada = false;
// Notificar o jogo
if (this.aposTacada) this.aposTacada();
}
No index.htmlpassamosumcallbackparaatacada:
function iniciarObjetos() {
// ...
taco.aposTacada = tacada;
}
Ecriamosessecallback. Aqui,vamosapenasreproduzirosom:
function tacada() {
somTacada.play();
}
Tambémconvémimpedirumatacadadecomeçarenquantooutraestiver
emandamento:
darTacada: function(duracao) {
if (this.tacada) return; // Já está em uma tacada
120

## Página 139

CasadoCódigo Capítulo5. InteraçõesavançadascomHammer.js
this.tacada = true;
this.duracaoTacada = duracao;
this.inicioTacada = Date.now();
},
Tudopronto,podetestarnoaparelhomóvel! Guardeocódigodestecapí-
tulocomcarinho,poisseráreutilizadoquandoformosdarsequênciaaojogo.
E aqui finalizamos a primeira parte do livro, sobre plataformas móveis!
Napróximaparte,trataremosdefísicaeabiblioteca Box2dWeb,essencialpara
quempretendelevarasérioaáreadegames. Elaseráresponsávelportodaa
açãoemcimadamesadebilhar.
121

## Página 141

ParteII
Física

## Página 143

Capítulo6
IntroduçãoaoBox2dWeb
Façamos um rápido exercício mental. Com o que temos, o que é necessário
parafazerumheróipular?
Basicamente,deslocá-loparacimaporuminstante,edepois,devoltapara
ba ix o .M ascla r oq uenãoésóisso .Se,nasub ida,elesechoca rco motetoo u
umaplataforma,omovimentodeveseinverterantecipadamente. Nadescida,
acolisãocomochãoéresponsávelporpararomovimento. Foraquepodemos
teranimaçõesdespritediferentesparaasubidaeparaadescida.

## Página 144

CasadoCódigo
Figura6.1: Umacolisãoalterandoosentidodemovimentodeumsprite.
Por mais complexo que pareça, isso pode ser feito de maneira relativa-
mente simples se soubermos definir bem osestados do sprite: dividir seus
movimentosemetapas(ostaisestados),sendoqueemcadaumaelesecom-
portaesedesenhademaneiradiferente,egerenciaras transiçõesdeestado ,
ouseja,detectarmomentosquandoospritepassadeumestadoaoutro. Caso
queira saber mais sobre gerenciamento de estados, falei sobre isso em meu
livroanterior,nocapítulo 4-Spritesheets .
Um recurso muito utilizado, no entanto, é o uso deenginesfísicas ,o u
motoresdefísica. Sãobibliotecas,frameworks,quepretendemsimularfísica
realista em um computador, poupando o programador de conhecer fórmu-
las e inúmeros detalhes. No mundo físico, nosso herói é simplesmente um
corpo,noqualaplicamosuma forçadebaixoparacima, fazendo-osaltar. A
gravidade se encarrega de fazê-lo voltar para o chão, e a colisão com este é
tratada automaticamente pelo engine, que o faz parar ou até mesmo quicar,
sedesejarmos.
E s t aéap r o p o s t ad oBox2D, biblioteca desenvolvida em C++ por Erin
Catto,programadornaBlizzardEntertainment. Oprimeiroprotótipofoicri-
ado como uma demonstração na Game Developers Conference, em 2006, e
desdeentãoabibliotecafoiportadaparaváriasoutraslinguagens,tamanhafoi
suaaceitação. AAPIépraticamenteidênticaemC++,Java,C#,Lua,Action-
ScripteJavaScript. Paraestaúltima,iremosusaroportchamado Box2dWeb,
convertidoapartirda Box2DFlashdesenvolvidaemActionScript.
126

## Página 145

CasadoCódigo Capítulo6. IntroduçãoaoBox2dWeb
Download
FaçaodownloaddaBox2dWebem:
https://code.google.com/p/box2dweb/downloads/list
Existe outro port da Box2D para JavaScript, oBox2DJS.E l en ã oéa t u a l -
izado há bastante tempo e requer outras bibliotecas, mas acho interessante
mencioná-loporquenasuahomepagevocêpodeverexemplosdaengineem
ação:
http://box2d-js.sourceforge.net/
Convenceu-se? Um leque de possibilidades abre-se para nós a partir de
agora.
6.1 Umprimeirotutorial
Emboranãosejaumaenginedifícildeusar,aBox2Douseusportsrequerem
algumapráticaepodemassustaroprogramadoriniciante. AAPIécomposta
de inúmeros objetos, e é fundamental saber o papel de cada um na engine.
A intenção deste capítulo é mostrar-lhe uma teoria básica, acompanhada de
suaaplicaçãoprática. Trabalharemoscomomundofísico,gravidade,corpos,
fixtureseformas.
Este exercício pode ser feito como uma simples página web, embora no
pacote de download esteja configurado como um projeto Cordova, de nome
box2dweb-intro. Segue o esqueleto daindex.html. O Canvas possui
tamanhofixo,poisnãoqueremosnestemomentopoluirocódigocomoutras
preocupaçõesquenãosejamsobreaBox2dWeb:
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,
height=device-height, user-scalable=no,
initial-scale=1, maximum-scale=1, minimum-scale=1" >
127

## Página 146

6.2. Objetosfundamentais CasadoCódigo
<title>Introdução ao Box2dWeb </title>
<script src="cordova.js"></script>
<script src="rAF.js"></script>
<script src="Box2dWeb-2.1.a.3.min.js"></script>
<script>
// Inicialização aqui
</script>
</head>
<body>
<canvas id="box2dweb" width="640" height= "480"></canvas>
</body>
</html>
Ainicializaçãonãoédiferentedoquejávimos:
var canvas, context;
window.onload = function() {
canvas = document .getElementById( ' box2dweb ' );
context = canvas.getContext( ' 2d ' );
//document.addEventListener( ' deviceready ' , iniciar);
iniciar();
}
function iniciar() {
// Aqui começará a física realista!
}
Esqueleto pronto, vamos entrar nos conceitos da engine, uma etapa por
vez.
6.2 Objetosfundamentais
128

## Página 147

CasadoCódigo Capítulo6. IntroduçãoaoBox2dWeb
Mundo(b2World)
Oprimeiroobjetocriadoésempreo mundo,querepresentaoespaçoondeos
corpos interagem. Normalmente só existe um mundo físico por jogo, pois a
necessidadedeprocessamentoéelevada.
Figura6.2: Omundofísicoemumjogo
É preciso ressaltar que esse mundo existe apenas na memória do com-
putador. A cada quadro de animação, nós avançamos o mundo físico no
tempo e a engine recalcula as posições dos objetos dentro dele, detecta col-
isões,entreoutrascoisas,deacordocomasforçasqueestiverematuandoem
cada corpo. Cabe a nós obter as posições de todos os corpos e desenhar os
sprites.
A Box2dWeb preserva o sistema de espaços de nomes presente na en-
gine original, na forma de objetos que agrupam outros objetos. Por ex-
emplo, para criar um
b2World,t e r í a m o sq u er e f e r e n c i a roc o n s t r u t o r
Box2D.Dynamics.b2World:
Parareduziracomplicação,ocomuméobterreferênciasaessesconstru-
tores no início do código. Posteriormente, usamos essa referência para in-
stanciarosobjetosdaengine:
129

## Página 148

6.2. Objetosfundamentais CasadoCódigo
// Variáveis do jogo
var canvas, context, mundo;
// ...
// Criando o mundo
function iniciar() {
mundo = new b2World( ... ); // O que passamos aqui?
}
Oco nstru to rb2Worldrequerosparâmetros:
• umobjeto b2Vec2representandoagravidade(vejalogoaseguir);
• um booleano (true/ false) indicando se os corpos podemdormir
duranteasimulação.
Umcorpo“dorme”quandoestáparadoenãoháforçasatuandosobreele,
eaengineo“acorda”automaticamenteseissoacontecer. Umcorpodormindo
éignoradopelaengineduranteesseestado,oqueeconomizaprocessamento.
Vetor (b2Vec2)
Parapodermoscriarummundofísico,temosquepassarparaeleumvetor
representando a gravidade. Em Física, umvetoré toda grandeza que possui
direçãoesentido. Porexemplo, agravi dadepossuidireçãoverticalesentido
para baixo. A direção de um vetor pode ser diagonal, mas o mais comum é
pensarmosseparadamentenoscomponenteshorizontal( x)evertical( y).
130

## Página 149

CasadoCódigo Capítulo6. IntroduçãoaoBox2dWeb
Figura 6.3: Uma trajetória é um vetor, portanto pode ser decomposta em x e
y
Agravidadeatuasomenteparabaixo,comdeterminadovalor y,enquanto
ov a l o rx é zero. A gravidade da Terra é de 9,81 metros por segundo ao
quadrado,ouseja,avelocidadedeumcorpoemquedalivre,semaresistência
doar,aumenta9,81metrosporsegundo acadasegundo.
A Box2D e seus ports representam grandezas vetoriais através do objeto
b2Vec2. Seu construtor recebe os valores nos eixosx e y. Para criar um
mundo com essa gravidade, permitindo que os corpos durmam, temos que
fazer:
131

## Página 150

6.2. Objetosfundamentais CasadoCódigo
Definiçõesdecorposefixtures( b2BodyDef eb2FixtureDef)
Dentrodomundo,o corporepresentaumobjetoindivisívelsujeitoàação
deforças. Umabola,umhomem,umapedrasãocorposnomundofísico.
Um corpo é formado por uma ou maisfixtures, que são suas unidades
materiais. Cada fixture possui uma forma e propriedades como densidade,
atritoeelasticidade.
Figura6.4: Corpofísicoesuasunidades(fixtures)
Fixture:fixação?
fixturefix.ture1fixação,fixidez. 2pessoaoucoisapermanentemente
ligadaaumlugar. 3acessório,pertence,instalação. [...]
Fonte:http://michaelis.uol.com.br/moderno/ingles/
Uma“fixture”podeserentendidacomoalgoqueéfixoemumaestru-
tura, como uma peça de um carro ou um relógio pendurado na parede:
a m b o sfi c a mi m ó v e i sn ae s t r u t u r ad oc a r r oo ud ac o n s t r u ç ã o . M u i t a s
traduções são dadas para a palavra, como “fixação” ou “acessório”, mas
nenhumamesoabememportuguês,razãoporqueoptoemusarotermo
eminglês: fixture.
Esseselementossãorepresentadosnaenginepor b2Bodye b2Fixture,
mas nós não os instanciamos diretamente. O que criamos são objetos de
132

## Página 151

CasadoCódigo Capítulo6. IntroduçãoaoBox2dWeb
definição, que contêm as informações usadas pela engine para criar os ver-
dadeiros corpos e fixtures. Os objetos de definição são b2BodyDef e
b2FixtureDef:
// Construtores
// ...
var b2BodyDef = Box2D.Dynamics.b2BodyDef;
var b2FixtureDef = Box2D.Dynamics.b2FixtureDef;
Para criar uma definição de corpo, o mínimo necessário é definir sua
posição (x, y) em metros. Para passar valores em pixels, divida-os por uma
escala:
// Variáveis do jogo
// ...
var escala =30 ; // pixels por metro
function iniciar() {
// ...
// Definição de corpo
var corpoDef = new b2BodyDef();
corpoDef.position.Set( 200/escala, 100/escala);
// continua ...
}
133

## Página 152

6.2. Objetosfundamentais CasadoCódigo
MedidasnoBox2D
Um detalhe muito importante é o uso das unidadesmetro, quilo-
grama esegundo nas simulações físicas. Nossa atenção se voltará prin-
cipalmente para os comprimentos, que sempre devem ser convertidos
de pixels para metros, ao configurar os objetos, e de metros para pix-
els novamente, ao ler suas posições. Isso não é difícil de se fazer: basta
definirmos uma
escala,u mn ú m e r od ep i x e l sp o rm e t r oas e ru s a d o
nasimulação:
var escala =3 0 ;
Ao criar um objeto, dividimos o tamanho em pixels desejado pela
escala. Umexemplosimples: seaescalaforde100pixelspormetro,um
objetode50pixelsterámeiometro(50/100).
var larguraMetros =2 5/ escala; // 25 pixels
Ao obter a posição ou tamanho de um objeto em metros, fazemos o
processoinverso: multiplicamosovalorpelaescalaparaobterempixels:
var larguraMetros = ...;
var larguraPixels = larguraMetros * escala;
Para dar formato ao corpo, criamos uma ou mais fixtures. O mínimo
necessário é dar à fixture umaforma, que corresponde a uma figura ge-
ométrica simples. No próximo capítulo veremos as opções de formas exis-
tentes. Combinando várias fixtures, podemos obter um corpo com formato
maiscomplexo. Aqui,criamosumaformacircularde25pixelsderaio:
function iniciar() {
// ...
// Definição de fixture
var fixtureDef = new b2FixtureDef();
fixtureDef.shape = new b2CircleShape(25/escala);
134

## Página 153

CasadoCódigo Capítulo6. IntroduçãoaoBox2dWeb
// continua...
}
Claro, acrescente a referência ao construtorb2CircleShape no início
docódigo:
// Construtores
// ...
var b2CircleShape = Box2D.Collision.Shapes.b2CircleShape;
Porfim,temosquecriarocorponomundoecriarneleafixture:
function iniciar() {
// ...
// Criar o corpo
var bola = mundo.CreateBody(corpoDef);
bola.CreateFixture(fixtureDef);
// continua...
}
Renderizaçãográficadedebug( b2DebugDraw)
Comoditoanteriormente,omundofísicoexistesomenteemmemória. A
enginefísicanãorealizatarefasderenderização. Nãopodemossimplesmente
passarimagensparaelaedeixarqueelacuidedissoparanós.
No entanto, a Box2D original oferece a possibilidade de se implemen-
tar umDebug Draw: um renderizador simples, voltado para testes, que nos
permitiria acompanhar o que está acontecendo no mundo físico. Certa-
mente,háinúmerosdelesimplementadosporaí,paracada
port daengine.
A Box2dWeb já vem com um Debug Draw pronto para uso, herdado do
Box2DFlash.
135

## Página 154

6.2. Objetosfundamentais CasadoCódigo
Figura6.5: DebugDrawrenderizandoomundofísicocomdesenhossimples
AsvantagensdeseusaroDebugDrawsão:
• poder trabalhar no desenvolvimento enquanto a equipe de arte tra-
balhanosgráficos;
• ajuda a localizar melhor a origem de bugs. Se o Debug Draw desenha
osobjetosnasposiçõescorretas,oerroénasualógicaderenderização
desprites;casocontrário,énalógicafísica.
Aindanafunção iniciar,acriaçãodeumDebugDrawenvolveascon-
figuraçõesaseguir. Destaqueparaométodo SetFlags,ondeconfiguramos
que componentes da engine queremos desenhar. A variávele_shapeBit
solicitaodesenhodasformasassociadasàsfixtures:
136

## Página 155

CasadoCódigo Capítulo6. IntroduçãoaoBox2dWeb
mundo.SetDebugDraw(debugDraw);
}
Nãoseesqueçadeadicionarareferênciaaoconstrutor b2DebugDraw:
// Construtores
// ...
var b2DebugDraw = Box2D.Dynamics.b2DebugDraw;
Osobjetosdenossomundoestãoconfigurados. Precisamosagorafazera
físicaacontecernele.
6.3 Animaçãodomundofísico
Avançandootemponaanimação
Vamos terminar a funçãoiniciar disparando a animação. Temos de con-
trolar quanto tempo há entre um ciclo e outro, para saber quanto tempo
avançar no mundo físico. Por isso, guardamos a hora atual na variável
ultimoCiclo:
function iniciar() {
// ...
// Iniciar a animação
ultimoCiclo = Date.now();
requestAnimationFrame(animar);
}
A função de animação necessita avançar o mundo físico no tempo. O
método Stepdomundopedeumtempoemsegundos,porissodividimoso
valor que temos (em milissegundos) por 1000. Os valores 8 e 3 representam
os números de iterações que o mundo vai realizar para movimentar os obje-
toseparaverificarsobreposições,respectivamente. Quantomaioronúmero
de iterações, maior a acurácia e menor o desempenho. Esses são os valores
recomendados pelo próprio Erin Catto no manual da Box2D, e podem ser
usadoscomopadrãocasonãotenhamosexcessodeobjetoseodesempenho
sejasatisfatório.
137

## Página 156

6.3. Animaçãodomundofísico CasadoCódigo
Tendo avançado o tempo, chamamos o métodoDrawDebugData do
mundoparadesenharasformasnoCanvaspeloobjetoDebugDraw:
Rode o projeto. Vemos um círculo estático no Canvas, com uma linha
traçada no raio. Essa linha serve para visualizarmos a rotação da forma cir-
cular,quandoforemaplicadasforçasnocorpo.
Figura6.6: Nossocorponãosemove!
Corposestáticosedinâmicos
Por padrão, os corpos sãoestáticos, isto é, ficam parados no seu lugar.
Servem de barreira para outros corpos se movimentando, mas eles mesmos
nãoreagemaestímulos,comocolisõesouaplicaçãodeforças.
Se quisermos que nossa bola caia em função da gravidade,
temos que transformá-la em um corpo dinâmico. N ot r e c h oe m
que criamos o b2BodyDef, vamos setar o atributo type como
b2Body.b2_dynamicBody:
138

## Página 157

CasadoCódigo Capítulo6. IntroduçãoaoBox2dWeb
E,claro,referenciar b2Body:
// Construtores
// ...
var b2Body = Box2D.Dynamics.b2Body;
Fizasreferênciasumaauma,conformenecessário,paravocêtomarcon-
tato com os principais objetos do Box2dWeb. Nossos próximos projetos já
podemcomeçarcomumconjuntodereferênciaspronto.
Agora a bola cai! Repare que ela mudou de cor: objetos dinâmicos são
representadosemroxopeloDebugDraw,enquantoosestáticoseramverdes.
Sevocêacharqueelaestácaindomuitodepressa,diminuaovalor ydovetor
da gravidade e note que ela cairá mais devagar. Faça experiências: coloque
umvalornegativoeveja-asubir;atribuaumvaloraoeixo xeelasedeslocará
paraolado.
Desempenho da animação: requestAnimationFrame x
setTimeout
O Box2dWeb trabalha bem com o velho setTimeout,a l -
iás, foi feito para ser usado com ele! Faz pouco tempo que o
requestAnimationFrame passouaseradotadoemlargaescalapelos
browsers.
Ousocomuméavançarmos60quadrosporsegundo,dividindo1000
milissegundospor60:
setTimeout(animar, 1000/60);
Já o avanço do tempo no Box2dWeb é dado em segundos, ou seja, 1
segundodivididopor60:
mundo.Step(1/60, 8, 3);
No próximo capítulo, você aprenderá que aplicando forças a um corpo
podemosmudarasuatrajetória. Umabolapodeserarremessadaparacima,
139

## Página 158

6.3. Animaçãodomundofísico CasadoCódigo
subindoatéumaalturamáximadeacordocomaforçaaplicada,eagravidade
afarádescernovamente. Sequisermos,podemospararomovimentoemuma
altura determinada, e deixá-la à mercê da gravidade. Se a bola for lançada
emsentidodiagonal,aengineautomaticamentetraçaumatrajetóriaemarco.
Tambémpodemosmovimentarumcorpomanualmente,comosefosseanave
ouosOVNIsdocapítulo 4.
Figura6.7: UmobjetodinâmicoapareceroxonoDebugDraw
Sugiroqueestudebastanteestesconceitosbásicos,poiselessãoabasede
tudooquefaremoscomoBox2dWeb. Nopróximo,vamosconhecertodasas
formasquepodemserusadas,aprenderaconfigurarpropriedadesfísicasdos
objetoseaplicarforças,impulsosevelocidadeneles.
DocumentaçãooriginaldaBox2D
OfuncionamentodaengineeasuaAPIforamdescritaspelopróprio
criador,ErinCatto,em:
http://box2d.org/manual.pdf
Sugestãodeleitura
Box2DforFlashGames ,deEman ueleF er o na to([1]).
140

## Página 159

Capítulo7
Configuraçõesemovimentode
corpos
No capítulo anterior, aprendemos a criar um mundo físico e as etapas
necessáriasparacolocarumcorponele. Sóesse“básico”jáexigedenóscon-
hecerasequência:
1) criarmundo;
2) criardefiniçãodecorpo(
b2BodyDef);
3) criardefiniçãodefixture( b2FixtureDef);
4) criarumaformaeassociá-laao b2FixtureDef;
5) criarocorpoesuafixtureapartirdasdefinições.

## Página 160

7.1. Formas CasadoCódigo
Indoumpassoalém,vamosconhecermaisdetalhesediversasopçõesque
temosemcadaumdessespassos. Talvezvocêestejaseperguntandoporque
temos que criar fixtures, em vez de associar a forma diretamente ao corpo.
Veremosqueelassãomaisdoqueumsimplesintermediárioentreocorpoe
umaforma.
7.1 Formas
Ocorpoquecriamosnoúltimoexercíciotinhaformaredonda,criadaatravés
de um
b2CircleShape.E s s af o r m aéa t r i b u í d aàp r o p r i e d a d eshape da
definiçãodafixture:
fixtureDef.shape = new b2CircleShape(25/escala);
Vamoscriarumanovapáginaweb. Nopacotededownload,esteprojeto
seencontranapasta formas,jáconfiguradaparaoCordova. Osarquivosde
scriptindicadospodemserobtidosdopacoteoudosprojetosanteriores:
<!DOCTYPE html>
<html>
<head>
<meta charset= "utf-8">
<meta name="viewport" content="width=device-width,
height=device-height, user-scalable=no,
initial-scale=1, maximum-scale=1, minimum-scale=1" >
<title>Formas</title>
<script src="cordova.js"></script>
<script src="rAF.js"></script>
<script src="Box2dWeb-2.1.a.3.min.js"></script>
<script>
// Inicialização aqui
</script>
</head>
<body>
<canvas id="formas" width="640" height="480"></canvas>
142

## Página 161

CasadoCódigo Capítulo7. Configuraçõesemovimentodecorpos
</body>
</html>
Vamos iniciar o código fazendo referência aos principais construtores e
criandoomundofísico:
var b2Vec2 = Box2D.Common.Math.b2Vec2;
var b2World = Box2D.Dynamics.b2World;
var b2BodyDef = Box2D.Dynamics.b2BodyDef;
var b2FixtureDef = Box2D.Dynamics.b2FixtureDef;
var b2CircleShape = Box2D.Collision.Shapes.b2CircleShape;
var b2PolygonShape = Box2D.Collision.Shapes.b2PolygonShape;
var b2DebugDraw = Box2D.Dynamics.b2DebugDraw;
var b2Body = Box2D.Dynamics.b2Body;
var canvas, context, mundo;
var escala =3 0 ; // pixels por metro
window.onload = function() {
canvas = document .getElementById( ' formas ' );
context = canvas.getContext( ' 2d ' );
mundo = new b2World( new b2Vec2(0, 9.81), true);
debugDraw();
iniciar();
//document.addEventListener( ' deviceready ' , iniciar);
}
Abstraímos para a funçãodebugDraw a tarefa de configurar a render-
izaçãopadrãodedebug. Estecódigopodesercopiadoapartirdoprojetodo
capítuloanterior:
function debugDraw() {
var debugDraw = new b2DebugDraw();
debugDraw.SetSprite(context);
debugDraw.SetDrawScale(escala);
debugDraw.SetFillAlpha( 0.6);
debugDraw.SetLineThickness( 1.0 );
debugDraw.SetFlags(b2DebugDraw.e_shapeBit); // Formas!!
143

## Página 162

7.1. Formas CasadoCódigo
mundo.SetDebugDraw(debugDraw);
}
Retângulosbásicos(caixas)
Começaremos criando algumas paredes delimitando a área do Canvas,
paraqueoutroscorposnãoconsigamsair. Essasparedesserãocorposestáti-
cosdeformatoretangular:
Figura7.1: Formasretangulares
NoBox2Deseusports,temosdoistiposderetângulos,sendoqueambos
sãodefinidosapartirdocentro:
• Caixas: retângulosbásicos,quetêmaposiçãodocorpocomocentro;
• Caixasorientadas: podem ter inclinação e seu centro pode ser deslo-
cadorelativamenteàposiçãodoco rpo .
144

## Página 163

CasadoCódigo Capítulo7. Configuraçõesemovimentodecorpos
Figura7.2: Caixacomum(centro)ecaixasorientadasinclinadasedeslocadas
apartirdocen tr odoco rpo
Vamos usar primeiro as caixas comuns, para criar as paredes. Como
são quatro, convém criar uma função separada,parede, a ser chamada em
iniciar. Passamos para ela as coordenadas e dimensões que queremos em
pixels:
Podemoscomeçarafunção paredeajustandoosvaloresconformeaes-
caladefinida. Lembre-sequeomundofísicorequerosdadosemmetros,não
empixels:
145

## Página 164

7.1. Formas CasadoCódigo
altura /= escala;
// continua...
}
Se estamos recebendox e y como o canto superior esquerdo, temos que
somarmetadedalarguraedaalturaparadeterminarocentro:
function parede(x, y, largura, altura) {
// ...
// Meia caixa
var meiaLargura = largura /2 ;
var meiaAltura = altura /2 ;
var corpoDef = new b2BodyDef();
corpoDef.position.Set(x + meiaLargura, y + meiaAltura);
// continua...
}
Caixas são criadas usandob2PolygonShape.Om é t o d oSetAsBox
criaumacaixasimples,tomandoaposiçãodocorpocomocentro. Devemos
passarparaeleas metadesdalarguraedaalturaquequeremos. Depoisdisso,
bastacriarafixtur eco mafo rmaeoco rponom undo:
function parede(x, y, largura, altura) {
// ...
// Formato retangular
var forma = new b2PolygonShape();
forma.SetAsBox(meiaLargura, meiaAltura);
var fixtureDef = new b2FixtureDef();
fixtureDef.shape = forma;
// Criar
var corpo = mundo.CreateBody(corpoDef);
corpo.CreateFixture(fixtureDef);
}
146

## Página 165

CasadoCódigo Capítulo7. Configuraçõesemovimentodecorpos
Para podermos ver os corpos, vamos chamar a função de animação ao
fimde iniciar:
function iniciar() {
// ...
ultimoCiclo = Date.now();
requestAnimationFrame(animar);
//setTimeout(animar, 1000/60);
}
Procure depois fazer experiências tanto com
requestAnimationFrame quanto com o setTimeout. Com poucos
corpos, você não notará grandes diferenças, mas no jogo de bilhar você se
surpreenderáaoverqueo setTimeoutapresentarámelhordesempenho.
Afunçãodeanimaçãosimplesmenteavançaotempodecorrido,desenha
oDebugDrawechamaopróximociclo:
function animar() {
var agora = Date.now();
var decorrido = agora - ultimoCiclo;
mundo.Step(decorrido /1000, 8, 3);
mundo.DrawDebugData();
ultimoCiclo = agora;
requestAnimationFrame(animar);
//setTimeout(animar, 1000/60);
}
Asparedesjápodemservistas!
Retângulosorientados
Se só pudéssemos criar retângulos a partir do centro do corpo, fi-
caríamos de mãos atadas. Para corpos complexos, com várias fixtures, quer-
emos definir a posição de cada uma. O métodoSetAsOrientedBox,d o
b2PolygonShape,permite-nosposicionaraformarelativamenteaocentro
docorpoetambémdefinirumângulodeinclinação.
147

## Página 166

7.1. Formas CasadoCódigo
Vamos criar um corpo em forma de “X”. Para isso, precisamos de dois
retângulosinclinados:umemsentidohorário,outroemsentidoanti-horário:
Figura7.3: Formasretangularesorientadascominclinação
Em iniciar, chame a funçãoxis. Pode ser antes ou depois das pare-
des,nãoimporta. Elereceberáascoordenadasdocentro,ocomprimentodo
braço (meia-largura do retângulo), a espessura (meia-altura)eoâ n g u l od e
inclinação:
Comece a função xis criando as caixas retangulares. O método
SetAsOrientedBox recebe a meia-largura, a meia-altura, a posiçãorela-
tivaaocentrodocorpo e o ângulo de inclinação. Para a posição, criamos
um b2Vec2 com valores zerados, para colocá-los exatamente no centro do
corpo. Reparequeumdosângulosdeinclinaçãodevetersinalnegativo,para
inverterosentido:
148

## Página 167

CasadoCódigo Capítulo7. Configuraçõesemovimentodecorpos
var ret1 = new b2PolygonShape();
ret1.SetAsOrientedBox(braco /escala, espessura /escala,
posicao, angulo);
var ret2 = new b2PolygonShape();
ret2.SetAsOrientedBox(braco /escala, espessura /escala,
posicao, -angulo);
// continua...
}
Porfim,bastacriarocorpo. Emcasodecorposcomváriasfixtures,você
podeusaromesmo b2FixtureDef,apenasalterandoaspropriedadescon-
formecriacadafixture:
function xis(x, y, braco, espessura, inclinacao) {
// ...
// Criar corpo e fixtures
var bodyDef = new b2BodyDef();
bodyDef.position.Set(x /escala, y/ escala);
var corpo = mundo.CreateBody(bodyDef);
var fixtureDef = new b2FixtureDef();
fixtureDef.shape = ret1;
corpo.CreateFixture(fixtureDef);
fixtureDef.shape = ret2; // Mudando a forma do b2FixtureDef
corpo.CreateFixture(fixtureDef);
}
Ocenáriojátemumobstáculo!
Polígonos
Claro que ob2PolygonShape, tendo o nome que tem, não serve ape-
nasparacriarretângulos. OBox2Deportspermitemacriaçãodepolígonos
convexos,sem“aberturas”. Polígonoscôncavosnãopodemsercriadosdireta-
mente,maspodemosjuntardoisoumaisconvexosparaformarumcôncavo:
149

## Página 168

7.1. Formas CasadoCódigo
Figura7.4: Polígonosconvexosecôncavos
Convexoecôncavo
Sevocê,comoeu,édaquelesqueprecisampararparapensarquando
temquedistinguirconvexodecôncavo,vaiaíumadica: convexoéolado
detrásdacolher . Oladoquetemaaberturaé côncavo(“comcavidade”).
Figura7.5: Ladosconvexoecôncavodacolher
Pense sempre nas costas da colher ao criar um polígono no
Box2dWeb.
150

## Página 169

CasadoCódigo Capítulo7. Configuraçõesemovimentodecorpos
Vamos criar um triângulo. Em iniciar,c h a m eu m an o v af u n ç ã o ,
triângulo:
function iniciar() {
triangulo();
// ...
}
Nessa nova função, temos que criar um array de pontos que formarão
os vértices do polígono. O Box2dWeb processará esses pontos emsentido
horário, portanto, caso haja erros na definição de seus polígonos, confira se
esses pontos, sendo percorridos dessa forma, formam a figura desejada. Os
valorescontinuamsendorelativosaocentrodocorpo. Essespontossãopassa-
dosparaométodo
SetAsVector,quetambémrecebeonúmerodevértices
aseremprocessados:
function triangulo() {
var pontos = [
new b2Vec2(0, -30/ escala),
new b2Vec2(30/escala, 0),
new b2Vec2(-30/ escala, 0)
]
var forma = new b2PolygonShape();
forma.SetAsVector(pontos, 3);
// continua...
}
Procedaàcriaçãodocorpo. Paravê-locaindo,vamostorná-lodinâmico:
function triangulo() {
// ...
// Corpo
var corpoDef = new b2BodyDef();
corpoDef.type = b2Body.b2_dynamicBody;
corpoDef.position.Set( 320/escala, 100/escala);
151

## Página 170

7.2. Movimentandocorpos CasadoCódigo
Jáépossívelverocorpotriangularcaindosobreo“X”pelaaçãodagravi-
dade. Eoqueémaisinteressante,a colisãoentrediferentesformasjáétratada
peloBox2dWeb!
Mas... esequisermosdar-lhealgumtrajetodiferente?
Figura7.6: Corpopoligonal
7.2 Movimentandocorpos
Existem três formas de movimentar corpos: aplicando forças, aplicando im-
pulsos ou setando a velocidade diretamente. Vamos criar um novo projeto
para testar essas três formas, de nome
movimento. O esqueleto e o script
de inicialização do Box2dWeb e do Canvas são os mesmos do projeto ante-
rior (7.1), por isso não vou repeti-los aqui. Copie-os e também as funções
debugDrawe animar.
Voucomeçaraexplicaçãopelafunção iniciar,ondevamoscriaruma
bolinhaeumchãonoqualelapodeseapoiar .Precisamosguardarumarefer-
ênciaàbolasequisermosmovimentá-ladepois.
152

## Página 171

CasadoCódigo Capítulo7. Configuraçõesemovimentodecorpos
chao(320, 470 , 10 );
ultimoCiclo = Date.now();
// Escolha qual tivermelhordesempenho par a SEU jogo
//requestAnimationFrame(animar);
setTimeout(animar, 1000/60);
}
Adicionea bolaàsdeclaraçõesdevariáveisdapágina:
var canvas, context, mundo, bola;
var escala =3 0 ; // pixels pormetr o
A função criarBola não tem novidades: ela cria a forma circular, as
definiçõeseoc o r p oap a r t i rd e l a s .Oc o r p oc r i a d oér e t o r n a d op a r aq u ea
referênciapossaserguardada:
function criarBola(x, y, raio) {
var forma = new b2CircleShape(raio/escala);
var fixtureDef = new b2FixtureDef();
fixtureDef.shape = forma;
var corpoDef = new b2BodyDef();
corpoDef.type = b2Body.b2_dynamicBody;
corpoDef.position.Set(x /escala, y/escala);
var corpo = mundo.CreateBody(corpoDef);
corpo.CreateFixture(fixtureDef);
return corpo;
}
Paraafunção chaonãoficarmuitoconfusa,járecebemosascoordenadas
como o centro do retângulo. A largura será a mesma do Canvaseaa l t u r aé
o parâmetro espessura. Estes valores devem ser divididos por 2, pois o
SetAsBoxrecebemeia-larguraemeia-altura:
153

## Página 172

7.2. Movimentandocorpos CasadoCódigo
J ápodemosverabolasob r eochão:
Figura7.7: Bolacaindonochão
Aplicandoforças
Vamos, a cada quadro da animação, aplicar uma força na bola,
fazendo-a subir. Para isso, vamos obter seu centro de massa, dado pelo
método GetWorldCenter,ea p l i c a raf o r ç an e s s ep o n t o ,c o mom é t o d o
ApplyForce:
A bola faz um movimento acelerado para cima, como um foguete! Uma
força deve ser aplicada continuamente, por isso nós a aplicamos dentro do
loopdeanimação.
154

## Página 173

CasadoCódigo Capítulo7. Configuraçõesemovimentodecorpos
Aplicandoimpulsos
Seaplicarmosaforçaapenasumavez,seuefeitoseráinócuo. Noentanto,
podemosaplicarumimpulsoumaúnicavez,edeixarqueagravidadeatuea
partirdaí.
Retire ou comente as linhas que aplicam a força emanimar. Agora,
vamosaplicarumimpulsoúnicoem iniciar:
function iniciar() {
// ...
var centro = bola.GetWorldCenter();
bola.ApplyImpulse(new b2Vec2(3, -10), centro);
}
Comvalores xeynovetor,aboladáumsaltoparaolado!
Alterandoavelocidade
Podemos também setar diretamente a velocidade da bola com o método
SetLinearVelocity,semdependerdocentrodemassa:
function iniciar() {
// ...
bola.SetLinearVelocity( new b2Vec2(10, -200));
}
Movimentandoarbitrariamente
Aposiçãodeumcorpotambémpodeseralteradacomosefosseumsprite
comum,comavantagemdejátermosascolisõescomoutroscorposproces-
sadaspelaenginefísica. Paraisso,usamosométodo SetPosition. Sequis-
ermosdeslocarrelativamenteàposiçãoatual,usamosantes GetPosition:
function animar() {
var posicao = bola.GetPosition();
posicao.y -= 1; // Movimento de subida
bola.SetPosition(posicao);
155

## Página 174

7.3. Propriedadesfísicas CasadoCódigo
// ...
}
7.3 Propriedadesfísicas
A bola cai no chão, porém não quica. Isso ocorre porque nem ela, nem o
chãopossuemelasticidade,umapropriedadefísicaqueprovocaumimpulso
quandoumcorpocolidecomoutro.
As propriedades físicas são configuradas na fixture, ou seja, cada fixture
de um corpo pode ter propriedades físicas diferentes. São elas:elasticidade
(restituição),atritoedensidade.
Você pode testar a elasticidade no último projeto trabalhado, desde que
estejautilizandooimpulsoúnico,disparadoem
iniciar. Deixenocódigo
as linhas indicadas, e comente ou retire qualquer outra mudança de veloci-
dadeouposiçãoeaplicaçãodeforça:
function iniciar() {
// ...
var centro = bola.GetWorldCenter();
bola.ApplyImpulse(new b2Vec2(3, -10), centro);
}
Na função criarBola, defina o atributo restitution da
b2FixtureDef.Estea trib u todever eceberumvalo ren tr e0e1:
var fixtureDef = new b2FixtureDef();
fixtureDef.shape = forma;
fixtureDef.restitution = 0.5; // Elasticidade
Isso é tudo! Varie os valore:0.1, 0.2 etc., até 1.0 e veja a bolinha
quicar.
Projetoparademonstraraspropriedades
Vamos criar um projeto semelhante ao anterior, de nome
propriedades. Neste projeto, faremos uso das três propriedades físi-
casmencionadas,acomeçarpeloatrito.
156

## Página 175

CasadoCódigo Capítulo7. Configuraçõesemovimentodecorpos
Novamente, no início da seção7.1encontram-se o esqueleto do HTML
e o código de inicialização. Copie-os e também as funçõesdebugDraw e
animar. Alémdisso,copieafunção parededoprojeto formas.
Tendotudoarrumado,vamoscriarduas“paredes”nocenário,sendoque
umaseráochãoeaoutra,ummuro. Seacharqueistonãoestámuitosemân-
tico,sinta-selivrepararenomearafunção paredeparaalgomaisadequado.
Aqui, vou manter o nome. Também criaremos um bloco retangular e apli-
car emosneleumim p ulsoparaadir ei ta:
Figura7.8: Demonstrandoatrito,elasticidadeedensidade
157

## Página 176

7.3. Propriedadesfísicas CasadoCódigo
A fixture do bloco é iniciada com valores considerados médios para as
propriedadesfísicas:
function criarBloco() {
var corpoDef = new b2BodyDef();
corpoDef.type = b2Body.b2_dynamicBody;
corpoDef.position.Set( 100/escala, 436/escala);
var forma = new b2PolygonShape();
forma.SetAsBox(25/escala, 25/escala);
var fixtureDef = new b2FixtureDef();
fixtureDef.shape = forma;
fixtureDef.friction =0. 5 ; // Atrito
fixtureDef.restitution =0. 5 ; // Elasticidade
fixtureDef.density =1 ; // Densidade
var bloco = mundo.CreateBody(corpoDef);
bloco.CreateFixture(fixtureDef);
return bloco;
}
Tambémconfigureessesvaloresparaadefiniçãodefixtureda parede:
function parede(x, y, largura, altura) {
// ...
var fixtureDef = new b2FixtureDef();
fixtureDef.shape = forma;
fixtureDef.friction =0. 5 ; // Atrito
fixtureDef.restitution =0. 5 ; // Elasticidade
fixtureDef.density =1 ; // Densidade
// ...
}
Nossolaboratórioestámontadoparaexperiências!
158

## Página 177

CasadoCódigo Capítulo7. Configuraçõesemovimentodecorpos
Atrito
Vamossetarvaloresnoatributo friction,sabendoqueelepodevariar
de0a1:
• Coloque o atrito do bloco como 1 e rode a simulação. O bloco nem
chegaatocarapar ede.
• Coloque os atritos do bloco e da parede como 1. O bloco tomba! É o
mesmo atrito provocado caso você aperte com força o freio da frente
dabicicleta,emaltavelocidade.
• Coloque os atritos como zero. O bloco desliza à vontade, quica e vai
embora.
Conclusão: o atrito final depende dos coeficientes de atrito dos dois ob-
jetossendofriccionados.
Elasticidadeourestituição
Vamoszerarosatritoseexperimentarcomoatributo restitution:
• Coloque a elasticidade do bloco como1ev e j a - oq u i c a rn ap a r e d e .O
blocochegaasaltitar,devidoaoimpulsoquerecebedochão.
• Coloque ambas elasticidades como1ev e j aa g o r a .Ap a r e d ec h u t ao
blocoparalo nge!
Conclusão: assimcomonoatrito,oimpulsoprovocadopelaelasticidade
tambémdependedasconfiguraçõesdosdoiscorpos.
Densidade
A densidade define amassa de um corpo. Quanto maior o valor, maior
a força ou impulso necessário para deslocá-lo uma dada distância. Experi-
m e n t em u d a roa t r i b u t o
density do bloco: 0.5, 1, 1.5, 2 etc. Não há
restrição de valor. Apenas observe que, conforme aumentamos a densidade
(e, consequentemente, a massa), o deslocamento do corpo com o impulso
159

## Página 178

7.3. Propriedadesfísicas CasadoCódigo
dado é menor. Você pode obter efeitos semelhantes com densidades difer-
entes,desdequeasforçaseimpulsossejamproporcionais.
Experimente variar densidades também na bolinha do projeto
movimento.N as u af u n ç ã ocriarBola:
var fixtureDef = new b2FixtureDef();
fixtureDef.shape = forma;
fixtureDef.restitution = 0.5;
fixtureDef.density =1 ; // Experimente valores diversos
Vocênotaráque,quantomenoradensidade,maisaltoabolapula,como
acontececomobjetosdomundoreal. Éadiferençaentrebateremumapeteca
eemumab igo rna.
Quantateoria! Masissoénecessáriosequisermosdominaraengine. Es-
peroestartornandoascoisasfáceisparavocê. Nopróximocapítulo,passare-
mos a construir a física do jogo de bilhar. Muitos conceitos sobre a engine
aindaserãoaprendidos.
DominandooBox2dWeb
Se você quer realmente dominar a engine, recomendo que invente
seus próprios cenários e “personagens”, ainda que meros quadradinhos
ou bolinhas, dê movimento a eles e experimente com as propriedades
físicas. Soltesuaimaginação!
160

## Página 179

Capítulo8
Iniciandoojogodebilhar
Chegou a hora de aplicar o que aprendemos sobre o Box2dWeb em um jogo
deverdade. Aofinaldessajornada,vocêdeveráconhecerosaspectosenvolvi-
dos na criação de um jogo com uma engine física, e como integrá-la com os
conceitosmaisbásicos,comosprites,loopdeanimaçãoeinteração.

## Página 180

8.1. Preparaçãodoprojeto CasadoCódigo
Figura8.1: Jogodebilharaserconstruído
Nopacotededownload,estápresenteoprojeto jogo-bilhar,jápronto
efuncional. Recomendoquevocêorodeemseucelular,afimdeterumaideia
exata do que será construído. Para dar uma tacada, basta rotacionar o taco
com dois dedos dentro da área circular, puxar o ponteiro da barra de força e
tocarobo tão
POW!nocantosuperiordireito.
Está pronto?
8.1 Preparaçãodoprojeto
Sigaosseguintespassosparaprepararoprojeto:
• Crie um projeto Cordova em seu computador, adicione a plataforma
Androidetambémoplugindemultimídia:
cordova create jogo-bilhar
cd jogo-bilhar
cordova platform add android
cordova plugin add org.apache.cordova.media
• Apague todos os arquivos da pastawww, porém mantendo as pastas
imge js,parafacilitar;
• Copieapasta imgdopacotededownload(dentrode www)paraoseu
projeto;
162

## Página 181

CasadoCódigo Capítulo8. Iniciandoojogodebilhar
• Copieosarquivosdesomdapasta platforms/android/assets;
• BaixeasbibliotecasHammer.jseBox2dWebparaapasta js,oucopie-
asdodownload;
• Copie também os arquivosanimacao.js e spritesheet.js do
jogodenave;
• Configureno config.xmloíconedoprojetoeaorientaçãopaisagem:
<icon src="www/img/icone.png" />
<preference name="Orientation" value="landscape" />
Oprópriodisplaydoaparelhoseráamesa,portantonãoháanecessidade
deviraraimagemconstantemente.
Segue o esqueleto inicial do arquivo index.html.O s c r i p t
construtores.js será criado logo depois. O mundo físico possuigravi-
dadezero , exigida por jogos cujo cenário é visto por cima. Para facilitar os
trabalhos mais adiante, guardamos a escala em pixels por metro como um
atributo do mundo. A classeAnimacao, criada em meu livro anterior e us-
ada no jogo de nave, vai passar a receber o mundo físico no construtor, pois
seráresponsávelporavançarotempo:
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Jogo de Bilhar</title>
<meta name="viewport" content="width=device-width,
height=device-height, user-scalable=no,
initial-scale=1, maximum-scale=1, minimum-scale=1" >
<script src="cordova.js"></script>
<script src="js/Box2dWeb-2.1.a.3.min.js"></script>
<script src="js/hammer.min.js"></script>
<script src="js/construtores.js" ></script>
<script src="js/animacao.js"></script>
163

## Página 182

8.1. Preparaçãodoprojeto CasadoCódigo
<script src="js/spritesheet.js" ></script>
<script>
var canvas, context, mundo, animacao;
var ESCALA =3 0 ;
window.onload = function() {
canvas = document.getElementById( ' bilhar ' );
context = canvas.getContext( ' 2d ' );
// Gravidade zero!
mundo = new b2World(new b2Vec2(0, 0), true);
mundo.escala = ESCALA; // Armazenando a escala
// Passe o mundo para a Animacao
animacao = new Animacao(context, mundo);
debugDraw();
iniciar();
//document.addEventListener( ' deviceready ' , iniciar);
}
function iniciar() {
// Criaremos mais coisas...
animacao.ligar();
}
function debugDraw() {
var debugDraw = new b2DebugDraw();
debugDraw.SetSprite(context);
debugDraw.SetDrawScale(ESCALA);
debugDraw.SetFillAlpha( 0.6);
debugDraw.SetLineThickness( 1.0);
debugDraw.SetFlags(b2DebugDraw.e_shapeBit);
mundo.SetDebugDraw(debugDraw);
}
</script>
</head>
164

## Página 183

CasadoCódigo Capítulo8. Iniciandoojogodebilhar
<body>
<canvas id="bilhar" width="700" height="400"></canvas>
</body>
</html>
Oa r q u i v oconstrutores.js é linkado logo após o Box2dWeb e ini-
ciará as referências aos principais objetos do Box2dWeb. O único que ainda
não foi usado é ob2ContactListener, responsável por tratar eventos de
colisãodisparadospelaengine:
var b2Vec2 = Box2D.Common.Math.b2Vec2;
var b2World = Box2D.Dynamics.b2World;
var b2BodyDef = Box2D.Dynamics.b2BodyDef;
var b2FixtureDef = Box2D.Dynamics.b2FixtureDef;
var b2CircleShape = Box2D.Collision.Shapes.b2CircleShape;
var b2PolygonShape = Box2D.Collision.Shapes.b2PolygonShape;
var b2DebugDraw = Box2D.Dynamics.b2DebugDraw;
var b2Body = Box2D.Dynamics.b2Body;
var b2ContactListener = Box2D.Dynamics.b2ContactListener;
Adaptandoaclasse Animacao
Precisamosadaptaraclasse Animacao(arquivo animacao.js)auma
novanecessidade. Essaclasseéresponsávelporcontrolaroloopdeanimação,
permitindo colocar e retirar dinamicamente sprites e rotinas de processa-
mento. Ela terá agora que chamar o
Step do mundo, o método que avança
omundofísiconotempo(seção 6.3). Porisso,receba-oemseuconstrutor:
function Animacao(context, mundo) {
this.context = context;
this.mundo = mundo;
// ...
}
Oc o r a ç ã od ac l a s s eéom é t o d oproximoFrame, que é nada mais que
a função de animação em si. Vamos modificá-lo para que limpe a tela com
165

## Página 184

8.1. Preparaçãodoprojeto CasadoCódigo
o fundo verde da mesa de bilhar, avance o tempo do mundo e permita-nos
optarentre setTimeoute requestAnimationFrame. Comooprimeiro
oferece bom desempenho com o Box2dWeb, podemos nos livrar da preocu-
pação de usar polyfills e suportar aparelhos antigos (que ainda não são tão
antigosassim):
proximoFrame: function() {
if ( ! this.ligado ) return;
// Fundo verde
var ctx = this.context;
ctx.save();
ctx.fillStyle = ' #050 ' ;
ctx.fillRect(0, 0, ctx.canvas.width, ctx.canvas.height);
ctx.restore();
var agora = Date.now();
if (this.ultimoCiclo == 0) this.ultimoCiclo = agora;
this.decorrido = agora - this.ultimoCiclo;
// Mundo físico
this.mundo.Step(1/60, 10, 5);
//this.mundo.DrawDebugData(); // Usado em caso de bugs
for (var i in this .sprites)
this.sprites[i].atualizar();
for (var i in this .sprites)
this.sprites[i].desenhar();
for (var i in this .processamentos)
this.processamentos[i].processar();
this.processarExclusoes();
this.ultimoCiclo = agora;
// Próximo ciclo com setTimeout
var animacao = this;
setTimeout(function() {
166

## Página 185

CasadoCódigo Capítulo8. Iniciandoojogodebilhar
animacao.proximoFrame();
}, 1000/60);
/*
requestAnimationFrame(function() {
animacao.proximoFrame();
});
*/
},
ImportânciadoDebugDraw
Perceba que comentei uma chamada aDrawDebugData. Se algo
der errado no processo, descomente essa linha. Dessa forma, podemos
capturar discrepâncias entre a posição real dos corpos e onde os sprites
sãodefatodesenhados. Neménecessáriodizerquepreciseidissomuitas
vezesenquantocriavaojogo.
AbraapáginanonavegadorevasculheoConsole. Porenquanto,oúnico
errodeveráserafaltado cordova.js.Oloopdeanimaçãoeomundofí sico
jáestãorodando,emboranãohajaspritesnemcorpos.
8.2 Primeirossprites
Vamoscomeçarcomosspritesmaissimples: asparedeseascaçapas. Oobje-
tivoémostrar-lhecomointegraroBox2dWebcomalógicadossprites.
167

## Página 186

8.2. Primeirossprites CasadoCódigo
Paredesdamesa
Figura8.2: Paredesdamesadebilhar
Na função iniciar, coloque uma chamada acriarParedes.C o m o
são várias, passamos um array contendo vários objetos (um par de colchetes
[]contendochaves {}):
Essa função vai simplesmente percorrer o array e instanciar objetos
Parede,adicionando-oscomospritesaoloopdeanimação. Percebaquepas-
samosomundoparaoconstrutor,delegandoparaaclasseacriaçãodocorpo:
168

## Página 187

CasadoCódigo Capítulo8. Iniciandoojogodebilhar
for (var i in arr) {
var p = new Parede(context, arr[i].x, arr[i].y,
arr[i].largura, arr[i].altura, mundo);
animacao.novoSprite(p);
}
}
Crieumlinkparaoarquivo parede.js,napasta js:
<script src="js/parede.js"></script>
E vamos criar esse arquivo. O construtor vai começar criando o corpo
no Box2dWeb. Nem precisaríamos configurar um novob2BodyDef como
estático,masfizissoparadarênfase. Adefiniçãodocorpotambémpodecar-
regarumatributo userData,deusolivredoprogramador. Estamosusando-
oparaassociarocorpoaosprite. Eleseráimportantedurantetratamentosde
colisão na engine, para executar ações sobre o sprite. Também, ao definir a
posiçãoeotamanho,usamosoatributo
escalaarmazenadonomundo. No
mais,semnovidades. Emcasodedúvidarevejaoscapítulos 6e7:
function Parede(context, x, y, largura, altura, mundo) {
// Corpo físico
var corpoDef = new b2BodyDef();
corpoDef.type = b2Body.b2_staticBody;
corpoDef.userData = this; // Sprite associado
var fixtureDef = new b2FixtureDef();
fixtureDef.density =1 ;
fixtureDef.friction = 0.5;
fixtureDef.restitution = 0.5;
var meiaLargura = largura /2 ;
var meiaAltura = altura /2 ;
var centroX = x + meiaLargura;
var centroY = y + meiaAltura;
// Usando a escala
corpoDef.position.Set(centroX / mundo.escala,
169

## Página 188

8.2. Primeirossprites CasadoCódigo
centroY/mundo.escala);
var retangulo = new b2PolygonShape();
retangulo.SetAsBox(meiaLargura /mundo.escala,
meiaAltura /mundo.escala);
fixtureDef.shape = retangulo;
var parede = mundo.CreateBody(corpoDef);
parede.CreateFixture(fixtureDef);
// continua...
}
Apóscriarocorpo,podemosprocederaosafazerescomunsdetodosprite:
armazenar seus atributos, atualizá-lo e desenhá-lo. O métodoatualizar,
tão importante no jogo de nave, perderá espaço porque quem posiciona os
o b j e t o sa g o r aéaBox2dWeb. Recomento que, ao criar seus jogos, mantenha
esse método com corpo vazio, para o caso de algum sprite precisar de al-
guma atualização extra que não tenha a ver com a física. Caso ele se revele
desnecessário, ou seja, não haveria nada para executar em lógica de negó-
cio ou de posicionamento, você poderá removê-lo de seus sprites e (não se
esqueça!) tirarachamadafeitanaclasse
Animacao.
function Parede(context, x, y, largura, altura, mundo) {
// ...
// Dados do sprite
this.context = context;
this.x = x;
this.y = y;
this.largura = largura;
this.altura = altura;
}
Parede.prototype = {
atualizar: function() {
//
170

## Página 189

CasadoCódigo Capítulo8. Iniciandoojogodebilhar
Podemoscarregaraimagemlogoaocarregaroscript,poisrodandolocal-
mentenãotemosqueterpreocupaçãocomquaisimagensjáestãocarregadas:
FaçaotesteeverifiqueseoCanvasaparececomonafigura 8.2.
Caçapas
Figura8.3: Mesacomcaçapas
Ascaçapasdamesadevemserdesenhadassobreasparedes,portanto,os
171

## Página 190

8.2. Primeirossprites CasadoCódigo
spritesdevemseradicionadosàanimaçãodepois. Aspritesheetdascaçapasé
formadaporseisimagense,parafacilitar,vamoscriá-lasnamesmasequência
emqueestãodesenhadasnoarquivo. Alémdasimagens,cadacaçapateráum
pequenocorpoaserusadocomosensordecolisão:
function iniciar() {
// ...
criarCacapas([
{imgX:0 , imgY:0 , sensorX:3 0 , sensorY:3 0 },
{imgX: 328, imgY:0 , sensorX: 350, sensorY:2 5 },
{imgX:65 6, imgY:0 , sensorX:67 0 , sensorY:3 0 },
{imgX:0 , imgY: 356, sensorX:3 0 , sensorY: 370},
{imgX: 328, imgY:3 5 6 , sensorX : 350, sensorY: 375},
{imgX:65 6, imgY:3 5 6 , sensorX :67 0 , sensorY: 370}
]);
animacao.ligar();
}
Figura8.4: Spritesheetdascaçapas
Cada caçapa criada usará uma coluna da spritesheet, atribuída pelo
númerodeordem(variáveldeloop i):
function criarCacapas(arrayDados) {
var arr = arrayDados;
for (var i in arr) {
var c = new Cacapa(context, arr[i].imgX, arr[i].imgY,
arr[i].sensorX, arr[i].sensorY, mundo);
c.spritesheet.coluna = i;
animacao.novoSprite(c);
}
}
172

## Página 191

CasadoCódigo Capítulo8. Iniciandoojogodebilhar
Nãoseesqueçadelinkaroarquivodaclasse:
<script src="js/cacapa.js"></script>
Evamoscriaraclasse Cacapa. Oscorposfísicosserãopequenosquadra-
dos, os sensores, posicionados estrategicamente nos pontos de entrada de
cada caçapa. O atributoisSensor da definição da fixture faz com que ela
nãoimpeçaapassagemdeoutrocorpo,enquantoaenginepodereportarque
elesestãoemcontato. Asbolasatravessarãoossensorescomosenãohouvesse
umcorpoali.
var SENSOR =1 ; // Meia largura/altura
function Cacapa(context, imgX, imgY, sensorX, sensorY, mundo) {
// Corpo do Box2dWeb (sensor)
var corpoDef = new b2BodyDef();
corpoDef.position.Set(sensorX / mundo.escala,
sensorY/mundo.escala);
corpoDef.type = b2Body.b2_staticBody;
corpoDef.userData = this;
var quadrado = new b2PolygonShape();
quadrado.SetAsBox(SENSOR /mundo.escala, SENSOR/mundo.escala);
var fixtureDef = new b2FixtureDef();
fixtureDef.shape = quadrado;
fixtureDef.isSensor = true; // Sensor!
this.corpo = mundo.CreateBody(corpoDef);
this.corpo.CreateFixture(fixtureDef);
// continua ...
}
Da mesma forma que com as paredes, vamos carregar a imagem e ar-
mazenarosatributosdosprite:
var SENSOR =1 ;
173

## Página 192

8.2. Primeirossprites CasadoCódigo
var SPRITE_CACAPA = new Image();
SPRITE_CACAPA.src = ' img/cacapa-spritesheet.png ' ;
function Cacapa(context, imgX, imgY, sensorX, sensorY, mundo) {
// ...
// Atributos do sprite
this.context = context;
this.mundo = mundo;
this.imgX = imgX;
this.imgY = imgY;
this.sensorX = sensorX;
this.sensorY = sensorY;
this.spritesheet = new Spritesheet(context, SPRITE_CACAPA,
1, 6);
}
E também desenhar a caçapa. No método desenhar do sprite,
chamamosométodohomônimodaspritesheet,quedesenhaconformeacol-
unaatribuídaanteriormente:
Cacapa.prototype = {
atualizar: function() {
//
},
desenhar: function() {
this.spritesheet.desenhar( this .imgX, this.imgY);
}
}
Façaotesteevejaseascaçapasaparecem. Paravermosossensores,abra
aclasse Animacao,descomenteachamadaao DrawDebugDataecomente
oloo pquechama desenharnos sprites:
// Descomente esta linha
this.mundo.DrawDebugData();
// ...
174

## Página 193

CasadoCódigo Capítulo8. Iniciandoojogodebilhar
Figura8.5: DebugDrawdamesadebilhar
Sempre faça este procedimento para certificar-se de que o mundo físico
estádeacordocomoquevocêdesejaemseusjogos.
8.3 Asbolasdebilhar
Asbolasdojogorepresentamumtipodespritecommaisdetalhesparalidar.
Emprimeirolugar,éinútilarmazenarmosatributosdeposição,poisaengine
físicaosdeslocaráotempointeiro. Aposiçãodedesenhodecadaboladeverá
sempre ser lida da engine. Faremos uso de uma folha de sprites animada e,
nãobastasseisso,oângulodedesenhodaboladeverácorresponderaoângulo
dasuatrajetória. Cuidaremosdistonestaenaspróximasseções. Preparado?
175

## Página 194

8.3. Asbolasdebilhar CasadoCódigo
Figura8.6: Nãosounenhumartista,portantoperdoem-me.
Vamosinicialmentedeclararvariáveisquefarãoreferênciasàsbolas:
E mandar criá-las após as caçapas. O número de cada bola corresponde
à linha da sua cor na spritesheet (figura8.6) .Ab o l ab r a n c as ee n c o n t r an a
linhazero.
176

## Página 195

CasadoCódigo Capítulo8. Iniciandoojogodebilhar
Asfunções criarBolaBrancae criarBolasColoridasinstanciam
objetos Bola,configuramoatributo idcomonúmeroeasadicionamcomo
s p r i t e sn aa n i m a ç ã o . P a r aab o l ab r a n c a ,ém e l h o rc r i a ru m ac o n s t a n t e(
BOLA_BRANCA) do que escrever diretamente um valor (zero, negativo ou o
quequerqueseja),paradefinirquesetratadabolabranca:
function criarBolaBranca(x, y) {
var b = new Bola(context, x, y, 12, mundo); // raio = 12
b.id = BOLA_BRANCA;
animacao.novoSprite(b);
return b;
}
function criarBolasColoridas(arrayDados) {
var arr = arrayDados;
var bolas = new Array(arr.length);
for (var i in arr) {
// raio = 10
var b = new Bola(context, arr[i].x, arr[i].y, 10, mundo);
b.id = arr[i].numero;
animacao.novoSprite(b);
bolas[i] = b;
}
return bolas;
}
T emosquecriaraclasse Bola.F açaolinkparaoscri p t:
<script src="js/bola.js"></script>
Esegueaprimeiraversão. Definimosaconstante BOLA_BRANCA,carreg-
amos a spritesheet, criamos o corpo e guardamos os atributos essenciais. A
definiçãodecorpopossuiumatributo bullet,queaprimoraadetecçãode
colisãoemaltavelocidade(maisdetalhesaseguir). Nãoénecessárioguardar
a trib u tosdeposiçãonosp ri te:
var BOLA_BRANCA =0 ;
177

## Página 196

8.3. Asbolasdebilhar CasadoCódigo
var BOLA_SPRITE = new Image();
BOLA_SPRITE.src = ' img/bola-spritesheet.png ' ;
function Bola(context, x, y, raio, mundo) {
// Corpo do Box2dWeb
var corpoDef = new b2BodyDef();
corpoDef.position.Set(x /mundo.escala, y/mundo.escala);
corpoDef.type = b2Body.b2_dynamicBody;
corpoDef.bullet = true; // Colisão de corpos velozes
corpoDef.userData = this;
var fixtureDef = new b2FixtureDef();
fixtureDef.shape = new b2CircleShape(raio /mundo.escala);
fixtureDef.density =1 ;
fixtureDef.friction = 0.5;
fixtureDef.restitution = 0.7;
this.corpo = mundo.CreateBody(corpoDef);
this.corpo.CreateFixture(fixtureDef);
// Atributos da bola
this.id =0 ;
this.context = context;
this.raio = raio;
this.mundo = mundo;
// Spritesheet
var sheet = new Spritesheet(context, BOLA_SPRITE, 10 , 19 );
this.spritesheet = sheet;
}
178

## Página 197

CasadoCódigo Capítulo8. Iniciandoojogodebilhar
Atributo bullet
Por padrão, o Box2D e ports calculam a posição de um corpo no
tempoeoposicionamdiretamente,damesmaformacomoestamosacos-
tumadosafazercomnossosspritessemenginefísica. Noentanto,corpos
muitopequenosevelozespodempassarporbarreiras“deumavez”entre
umquadroeoutro,impedindoadetecçãodacolisão.
Figura8.7: Semumdetectordecolisãoapurado,estabolaatravessariaomuro
Quando uma definição de corpo possui o valortrue no atributo
bullet, o Box2D realiza uma detecção mais apurada, considerando os
pontos intermediários da trajetória. Isto não é feito por padrão porque
requermuitoprocessamento;vocêdeveconfigurarcomo
bulletsape-
nascorposmuitovelozesqueapresentaremoproblemadeatravessarout-
rosinadvertidamente.
Para desenhar, façamos um primeiro teste. Primeiro lemos a posição da
bola com o métodoGetPosition do corpo. Depois convertemos as coor-
denadas para pixels, multiplicando-as pela escala. Por último, desenhamos
círculosbásicosparanoscertificarmosdequeasbolinhasestãosendodesen-
hadasnasposiçõescorretas:
179

## Página 198

8.3. Asbolasdebilhar CasadoCódigo
// Posição
var posicao = this.corpo.GetPosition();
var x = posicao.x * this.mundo.escala;
var y = posicao.y * this.mundo.escala;
// Simples por enquanto
var ctx = this.context;
ctx.beginPath();
ctx.arc(x, y, this.raio, 0, Math.PI*2);
ctx.fill();
}
}
Rodeapáginaevejasebolaspretasaparecemsobreamesa. Vamosentão
aplicaraspritesheet. Alinhacorrespondeaoatributo id dabola. Ométodo
proximoQuadro,paraquemnãoconhecedomeuoutrolivro,avançaaani-
maçãonotempo. Emseguida,mandamosdesenharoquadroatual:
desenhar: function() {
var posicao = this.corpo.GetPosition();
var x = posicao.x * this.mundo.escala;
var y = posicao.y * this.mundo.escala;
var sheet = this.spritesheet;
sheet.linha = this .id;
sheet.proximoQuadro();
sheet.desenhar(x - this.raio, y - this.raio,
this.raio *2 , this.raio *2 );
}
As bolinhas ficam girando mesmo paradas, o que será tratado mais
à frente. Primeiro, quero chamar a atenção para algo errado: o método
desenhar da classe Spritesheet não recebe a largura e a altura! Pre-
cisamosdissopoisabolabrancapossuiumtamanhodiferentedasoutras,de-
terminadopeloraio. Vamosmodificaressemétodoparaquerecebaopcional-
mente a largura e a altura do desenho. As chamadas antigas que não pas-
sarem estes parâmetros continuarão desenhando o tamanho real do quadro
daspritesheet:
180

## Página 199

CasadoCódigo Capítulo8. Iniciandoojogodebilhar
Perceba que agora a spritesheet respeita as dimensões passadas, e a bola
brancaaparecemaior. FaçaotestecomoDebugDrawtambém.
Figura8.8: Bolasposicionadasnamesa
181

## Página 200

8.4. Executandoatacada CasadoCódigo
8.4 Executandoatacada
Estápensandonoqueeuestoupensando? Quetalaplicarumimpulsonabola
brancaesimularumatacada? Paratratarodesenhocorretodasbolassemovi-
mentando, precisamos provocar primeiro um movimento. Em
iniciar,
acrescenteumachamadaàfunção tacada:
function iniciar() {
// ...
tacada();
}
Nessafunção,começamosdefinindooângul oeaforçaque,lembre-se,são
atributos presentes na classeTaco criada no capítulo5. Criamos um objeto
Tacada, que é acrescentado como um processamento do loop de animação,
echamamosummétodo disparar:
function tacada() {
// Virão do Taco depois :D
var angulo =0 ;
var forca = 100;
var t = new Tacada(bolaBranca, bolasColoridas);
animacao.novoProcessamento(t);
t.disparar(angulo, forca);
}
T emosquecriaraclasse Tacada.F açaumno volink:
<script src="js/tacada.js"></script>
Esegueumesqueletoparaaclasse. Presteatençãoaoatributo rodando:
qualquerprocessamentopodeserligadoedesligadotestando-seumatributo
desse tipo, permitindo-nos controlar melhor sua configuração e até mesmo
setaratributosimportantesantesdecomeçaroprocessamento:
function Tacada(branca, coloridas) {
this.branca = branca;
this.coloridas = coloridas;
182

## Página 201

CasadoCódigo Capítulo8. Iniciandoojogodebilhar
this.rodando = false;
}
Tacada.prototype = {
disparar: function(angulo, forca) {
},
processar: function() {
if (!this.rodando) return;
// Faremos algo aqui
}
}
No método disparar, temos que determinar os componentesx e y da
força a ser aplicada, com a ajuda do seno e do cosseno (ver box adiante).
Depois, aplicamos essa força como um impulso na bola branca, sinalizamos
que o processamento está rodando e marcamos o instante do início, para
cronometrarotempo:
disparar: function(angulo, forca) {
var radianos = angulo * Math.PI / 180;
var forcaX = forca * Math.cos(radianos);
var forcaY = forca * Math.sin(radianos);
var forca = new b2Vec2(forcaX, forcaY);
var centro = this.branca.corpo.GetWorldCenter();
this.branca.corpo.ApplyImpulse(forca, centro);
this.rodando = true;
this.inicio = Date.now();
},
183

## Página 202

8.4. Executandoatacada CasadoCódigo
Decomposiçãodevetorem x e y
Dadosovalordeumaforça,tambémchamado módulodessaforça,e
oângulodeaplicação,podemosdeterminarseuscomponentes xeypelas
fórmulas:
Atacadajáacontece,aindacomasbolinhasgirandoloucamente. Asbolas
que entram na caçapa seguem adiante para fora, pois atravessam os corpos
sensores. Omundofísiconãopossuibarreiras.
Figura8.9: Pow!
Sóqueaaçãonãotermina! Oscorposcontinuamemmovimentoporque
as paredes não oferecem resistência suficiente para dissipar sua energia. No
método
processar, vamos verificar o tempo decorrido e mandar as bolas
frearem gradativamente. Por isso, guardamos todas elas em um array único,
usandoométodo
concatdoarray coloridas,parajuntá-lascomabranca.
Depois,ométodo IsAwakedocorpoverificaseeleestáacordado,poiscon-
figuramos o mundo do Box2dWeb para adormecer corpos que pararem. A
variável
mexendosinalizaráseaindaháounãobolasemmovimento:
184

## Página 203

CasadoCódigo Capítulo8. Iniciandoojogodebilhar
processar: function() {
if (!this.rodando) return;
var decorrido = Date.now() - this.inicio;
var mexendo = false;
var bolas = this.coloridas.concat([ this.branca]);
for (var i in bolas) {
var b = bolas[i];
// Monitorar o movimento
if (b.corpo.IsAwake()) {
mexendo = true;
// Frear a bola
if (decorrido >= 7000 )
b.frear(5.0);
else if (decorrido >= 5000)
b.frear(1.0);
else if (decorrido >= 3000)
b.frear(0.7);
}
}
// continua...
}
Os valores passados para o métodofrear da Bola, a ser criado logo
mais, representarão a desaceleração que os corpos sofrerão. Esses valores, e
também os intervalos de tempo, foram obtidos após vários testes, de acordo
com o tempo que eu considerei adequado para a animação durar não há
mágicaparadeterminarisso,vocêpodefazerseusprópriostestesdepoisque
estaparteestiverpronta.
Apósiterarportodasasbolas,senenhumamaisestiversemexendo,deve-
mosreverteradesaceleraçãodetodaselas,setandoovalorzero. Issoéimpre-
scindível para que elas não parem e passem a ir em sentido contrário! Sinal-
izamosofimdaexecuçãodatacadaechamamosumcallbackporondeojogo
poderádarcontinuidadeaseuprocessamento:
185

## Página 204

8.5. Ângulodatrajetória CasadoCódigo
processar: function() {
// ...
if ( ! mexendo ) {
// Reverter a desaceleração
for (var i in bolas)
if (!bolas[i].foraDeJogo) bolas[i].frear( 0);
if (this.aposTacada) this.aposTacada();
this.rodando = false;
console.log( ' tacada finalizada ' );
}
}
Éb o ap r á t i c a“ d o c u m e n t a r ”oa t r i b u t oaposTacada inicializando-o
como nullno construtor:
this.aposTacada = null;
Precisamos agora criar o métodofrear na classe Bola. Os métodos
SetLinearDamping e SetAngularDamping configuram uma desaceler-
açãogradativaparaasvelocidadeslinear(detrajetória)eangular(derotação),
respectivamente:
frear: function(desaceleracao) {
this.corpo.SetLinearDamping(desaceleracao);
this.corpo.SetAngularDamping(desaceleracao);
}
Podeexperimentaratacada! Quandoaanimaçãocompletar7segundos,
a desaceleração vai ser tal que elas pararão em pouco tempo e a mensagem
“tacadafinalizada”poderáservistanoconsole. Experimenteconfigurarout-
r osângulosefo r çasnafunção
tacada!
8.5 Ângulodatrajetória
Vamos resolver o problema da animação da spritesheet. Se fosse apenas an-
imar quando estiverem em movimento, seria fácil. Mas o desenho da bola
deveser rotacionadodeacordocomasuatrajetória:
186

## Página 205

CasadoCódigo Capítulo8. Iniciandoojogodebilhar
Figura8.10: Bolasrotacionadasemtrajetóriasdiferentes
Para nossa sorte, dado um vetor com componentes (x, y), como a ve-
locidade, o JavaScript nos fornece o métodoMath.atan2, que devolve o
ângulo desse vetor com relação à horizontal, exigindo somente os parâmet-
ros na ordem invertida: (y, x). Obtemos a velocidade do corpo com
GetLinearVelocityeeusamos Math.atan2paradeterminaroângulo.
V amosr eco nstruirométododesenhardaclasse Bola:
Agora, peço que se detenha e preste bastante atenção. A classe
Spritesheet possuioatributo intervalo,quedefineotempoentreum
quadro e outro. Esse intervalo éinversamente proporcionalà velocidade:
quanto mais rápida a bola, menor o intervalo da animação, fazendo-a girar
maisrápido. Masháumpequenoporém: umavelocidade negativaématem-
aticamente menor que uma positiva de 0,001 ou mesmo zero. Mas o sinal
negativoaquisignificaapenaso sentidoemqueabolapercorreamesa. De-
vemos trabalhar em valores absolutos, considerando que -20 é maior que 5,
porexemplo.
Tendooscomponentes
vXe vYdavelocidade,vamosobterseusvalores
absolutos e ver qual o maior. Se for zero, não definimos intervalo (atribuí-
mos
null). Se for maior que zero, o intervalo será o inverso da velocidade
187

## Página 206

8.5. Ângulodatrajetória CasadoCódigo
(1/velocidade). Isso, claro, gera intervalos em valores decimais menores que
1, portanto multiplicamos por algum fator, no caso 50, para obter interva-
los maiores. Quanto tudo estiver pronto, você poderá fazer vários testes al-
terando esse valor e ver que o intervalo entre os quadros da spritesheet au-
mentaoudiminui,massempredeformainversaàvelocidadedomovimento:
Confesso,estafoiapartequemaismedeutrabalhodebolar!
Finalmente,temosqueobteraposiçãodabolaedesenhá-larotacionada.
Comoaprendemosem 5.3,paradesenharumobjetorotacionado,temosque
transladaroCanvasparaolocaldesejadoparadepoisrotacionar:
Figura8.11: ComorotacionarabolanoCanvas
Esse conceito é muito importante para desenharmos qualquer objeto
rotacionado! Leia então a posição do corpo e faça as alterações no contexto
doCanvas:
188

## Página 207

CasadoCódigo Capítulo8. Iniciandoojogodebilhar
// Posição
var posicao = this.corpo.GetPosition();
var x = posicao.x * this.mundo.escala;
var y = posicao.y * this.mundo.escala;
// DESENHAR ROTACIONADA
var ctx = this.context;
ctx.save();
// Ponto de desenho
ctx.translate(x, y);
// Rotaciona
ctx.rotate(angulo);
// continua ...
},
Podemosagorafazerodesenho,descontandooraiodaboladaposiçãoat-
ualdoCanvas. Casotenhamosdefinidoumintervaloanteriormente(bolaem
movimento),nósoaplicamosnasprite sheetemandamosavançaraanimação.
Não se esqueça de chamar orestore quando fizer alterações drásticas no
contextográfico!
desenhar: function() {
// ...
// Desenha
var sheet = this.spritesheet;
sheet.linha = this.id;
if (intervalo) {
sheet.intervalo = intervalo;
sheet.proximoQuadro();
}
sheet.desenhar(-this.raio, -this.raio, this.raio *2 ,
189

## Página 208

8.5. Ângulodatrajetória CasadoCódigo
this.raio *2 );
ctx.restore();
},
Terminamosaprimeiraetapa! Temostodososspritesnecessáriosejáso-
moscapazesdeconduzirumatacadanojogo,disparando-aesabendoquando
aaçãoterminou.
No próximo capítulo, incorporaremos ao jogo as classes Taco e
BarraForca, criadas no capítulo5, para adicionar interação, e aprendere-
mos como reagir a colisões no Box2dWeb, disparando sons e fazendo as bo-
lassumiremquandocolidiremcomossensoresdacaçapa. Esperoqueesteja
gostando!
190

## Página 209

Capítulo9
Interaçãocomojogadorelógicas
denegócio
Vamos agora permitir aos jogadores de nosso bilhar virtual controlar a sua
tacadaeencaçaparasbolas,fazendo-asdesaparecer.
Nocapítulo 5,nóscriamosoprojeto taco-bilhar,quecontémoscon-
trolesdeinteraçãocomojogodestelivro. Nocaso,umcontrolederotaçãodo
tacoeumabarraderegulagemdaforçadatacada. Copieparaoprojetoatual
(
jogo-bilhar)o sa r q u i v o staco.js e barra-forca.js, e também a
bibliotecaHammer.js. Vocêpodeobteressesarquivosnopacotededownload
oudapastaondevocêsalvouseusexercícios.
Certifique-sedequeoprojetojápossuitodosossonseimagenscopiados
paraaspastascorretas. Emcasodedúvidas,revejaoiníciodocapítulo 8.
Confiraoconjuntodosscriptsquedevemserlinkadosatéaqui:

## Página 210

9.1. Controlesdatacada CasadoCódigo
<script src="cordova.js"></script>
<script src="js/Box2dWeb-2.1.a.3.min.js"></script>
<script src="js/hammer.min.js"></script>
<script src="js/construtores.js" ></script>
<script src="js/spritesheet.js" ></script>
<script src="js/animacao.js"></script>
<script src="js/bola.js"></script>
<script src="js/parede.js"></script>
<script src="js/cacapa.js"></script>
<script src="js/tacada.js"></script>
<script src="js/taco.js"></script>
<script src="js/barra-forca.js" ></script>
Vamos começar!
9.1 Controlesdatacada
Preparação
Napastadasimagens,existeoarquivo tacada.png,querepresentaobotão
que dispara a tacada. Você pode usar outra figura, se desejar. Na seção
<body>,acrescenteatagdaimagemlogoapósatag <canvas>:
<body>
<canvas id="bilhar" width="700" height="400"></canvas>
<img src="img/tacada.png" id="tacada" >
</body>
EvamosposicionarestebotãoviaCSS,tambémaproveitandoparadeixar
oCanvasresponsivo,comoaprendemosem 3.3.N aseç ã o<head>,acrescente
umatag <style>efaçaasconfiguraçõesaseguir:
body {
margin:0 ;
width: 100%;
height: 100%;
background :# 3 3 3 ;
}
192

## Página 211

CasadoCódigo Capítulo9. Interaçãocomojogadorelógicasdenegócio
canvas {
height: 100%;
width: auto;
display: block;
margin:0auto;
}
#tacada {
position: absolute;
right: 20px;
top: 20px;
}
AcrescentetambémreferênciasaoHammer.js,aoscontroleseaoarquivo
desomdatacada,nasdeclaraçõesdevariáveisdapágina:
var canvas,context,mundo,animacao;
var ESCALA =3 0 ;
var bolaBranca,bolasColoridas;
var hammer,taco,barraForca,somTacada;
E modifique o eventoonload d ap á g i n ap a r ac a r r e g a ros o meoH a m -
mer.js. Vamos, por enquanto, deixar comentadas as linhas que só rodam
em dispositivo móvel, para podermos realizar testes no console do Google
Chromenodesktop:
window.onload = function() {
canvas = document .getElementById( ' bilhar ' );
context = canvas.getContext( ' 2d ' );
//somTacada = new Media( ' file:///android_asset/colisao.mp3 ' );
mundo = new b2World( new b2Vec2(0, 0), true);
mundo.escala = ESCALA;
animacao = new Animacao(context,mundo);
hammer = new Hammer(canvas);
debugDraw();
193

## Página 212

9.1. Controlesdatacada CasadoCódigo
iniciar();
//document.addEventListener( ' deviceready ' , iniciar);
}
Em iniciar, fizemos uma chamada à funçãotacada somente para
testaralógica. Retireessachamada:
function iniciar() {
// ...
// Remova
//tacada();
}
Criaçãodoscontroles
As classes Taco e BarraForca estão recebendo as imagens pelo con-
strutor, seguindo a linha de carregar as imagens na inicialização. Esta é uma
boa prática para jogos que devem ser publicados na internet, mas para um
jogo local vamos simplificar os construtores. Abra o arquivo
taco.js, in-
siraaslinhasquecarregamaimagememodifiqueoconstrutorcomosegue:
var IMG_TACO = new Image();
IMG_TACO.src = ' img/taco.png ' ;
function Taco(context, hammer) {
this.context = context;
this.imagem = IMG_TACO;
// ...
}
Omesmoem barra-forca.js:
var IMG_PONTEIRO = new Image();
IMG_PONTEIRO.src = ' img/ponteiro.png ' ;
function BarraForca(context, taco, hammer) {
this.context = context;
this.ponteiro = IMG_PONTEIRO;
194

## Página 213

CasadoCódigo Capítulo9. Interaçãocomojogadorelógicasdenegócio
// ...
}
Temos então que criar os controles. Eminiciar, instanciaremos o
Tacoeconfiguraremosodisparopelotoquenobotãodatacada. Aindaman-
ter emosco men tadooco mandoquer ebob inaoso m:
function iniciar() {
// Paredes, caçapa e bolas
// ...
taco = new Taco(context, hammer);
taco.raio =12 0 ;
taco.x =12 5 ;
taco.y = canvas.height /2-5 0 ;
var imgTacada = document.getElementById( ' tacada ' );
imgTacada.addEventListener( ' touchstart ' , function() {
//somTacada.seekTo(0);
taco.darTacada(50);
});
taco.aposTacada = tacada;
animacao.novoSprite(taco);
// Aqui virá a barra de força
animacao.ligar();
}
Omesmosesucederácomabarradeforça:
function iniciar() {
// ...
barraForca = new BarraForca(context, taco, hammer);
barraForca.x = taco.x -10 0 ;
barraForca.y = taco.y + taco.raio +2 5 ;
barraForca.largura = 200;
195

## Página 214

9.2. Executandoatacadanoângulocorreto CasadoCódigo
barraForca.altura =5 0 ;
animacao.novoSprite(barraForca);
animacao.ligar();
}
Como os controles estão sendo adicionados como sprites na animação,
estesdevemterométodo atualizar,aindaquevazio. Nocapítuloanterior,
eudisseque,seo atualizarsemostrardesnecessárioemalgumjogo,você
poderáremovê-lodosspritesetambémsuachamadapelaclasse Animacao.
Modifiqueambososcontroles:
Taco.prototype = {
atualizar: function() {
//
},
// ...
}
BarraForca.prototype = {
atualizar: function() {
//
},
// ...
}
Façaotestenonavegadorevejasenãoháerrosdecodificaçãonoconsole,
exceto o docordova.js. Você pode também rodar no seu celular e testar
oscontroles.
9.2 Executandoatacadanoângulocorreto
A função tacada, atualmente, está definindo arbitrariamente a força e o
ângulo. Vamos modificá-la para que leia esses dados do controle do taco.
Também vamos impedir uma tacada com força nula e mandar esconder
196

## Página 215

CasadoCódigo Capítulo9. Interaçãocomojogadorelógicasdenegócio
os controles enquanto a ação acontece. Perceba que criamos um callback,
bolasPararam,parareagirquandoaanimaçãotiverterminado:
function tacada() {
if (taco.forca == 0) return;
// Esconder os controles
taco.podeDesenhar = false;
barraForca.podeDesenhar = false;
// Realizar a tacada
var tacada = new Tacada(bolaBranca, bolasColoridas);
animacao.novoProcessamento(tacada);
tacada.aposTacada = bolasPararam;
tacada.disparar(taco.rotacao, taco.forca);
//somTacada.play();
}
function bolasPararam() {
// Aqui executaremos outras regras de negócio!
taco.podeDesenhar = true;
barraForca.podeDesenhar = true;
}
Nosconstrutores,tantodo Tacoquantoda BarraForca,inicieonovo
atributo podeDesenharcomo true:
this.podeDesenhar = true;
Em seus métodos desenhar, faça-os considerarem o atributo logo no
início:
desenhar: function() {
if (!this.podeDesenhar) return;
// ...
}
197

## Página 216

9.2. Executandoatacadanoângulocorreto CasadoCódigo
Rode no celular. Gire o taco e aperte o botão da tacada. Deve funcionar,
masabolanãopareceirnadireçãocorreta!
Na verdade, ela vai. Se você deixar o ângulo padrão (0°), a bola branca
é impulsionada para a direita, porém o taco é desenhado em pé, porque sua
imagem é em pé. Isso é fácil de ser resolvido, basta desenhar a imagem 90°
(pi/2) a mais que a rotação definida no controle. No método
desenhar do
Taco,modifiquealinhaquecalculaoângulodaimagememradianos:
Figura9.1: Somando90°àimagemdotaco,eleficaalinhadocorretamenteao
ângulodatacada
Experimentenovamenteevejaqueabolabrancavainadireçãoparaonde
vocêgirouotaco.
198

## Página 217

CasadoCódigo Capítulo9. Interaçãocomojogadorelógicasdenegócio
TestandoatacadapeloConsole
Pelocelularémuitomaisinterativo,masdemoraparacarregar. Testes
rápidospodemserfeitospeloGoogleChrome. Abarradeforçapodeser
puxadacomomouse,poiségeridapeloHammer.js. Arotaçãoexigedois
dedosnatelatouch,maspodemossetaroatributoedispararumatacada
diretamentepeloconsole:
Figura9.2: DandocomandosaojogopeloconsoledoGoogleChrome
9.3 Posicionandootaco
Embora tudo esteja começando a funcionar bem, ainda está estranho ver o
tacosemprenomesmolocal,enquantoabolabrancavagapelamesa. Vamos
criar uma nova função que cuidará de posicionar a imagem do taco junto
à bola branca, no início e após cada tacada. Na função
iniciar,c o m e c e
chamando posicionarTacoapósasuainstanciação:
199

## Página 218

9.3. Posicionandootaco CasadoCódigo
posicionarTaco();
Afunção posicionarTacovaileraposiçãodabolabrancanomundo
físicoeconfigurarosnovosatributos brancaXe brancaY,aseremusados
somente para o desenho do taco. Os atributosx e y n ã om u d a m ,po i sc o n -
tinuarão correspondendo ao centro do controle circular. Também é preciso
especificar um raioDistancia para afastar a ponta do taco do centro da
bola,evitandoqueosdesenhossesobreponham:
function posicionarTaco() {
var pos = bolaBranca.corpo.GetPosition();
var x = pos.x * ESCALA;
var y = pos.y * ESCALA;
taco.brancaX = x;
taco.brancaY = y;
taco.raioDistancia = bolaBranca.raio;
}
No construtor doTaco, inicie esses atributos para documentá-los devi-
damente:
this.brancaX =0 ;
this.brancaY =0 ;
this.raioDistancia =0 ;
Enométodo desenhar,o translatepassaaserfeitoparaesseponto
desejado. O deslocamento do taco não será apenas de acordo com a força,
mastambémsomadocomoraiodedistânciadocentrodabolabranca:
desenhar: function() {
// ...
// Taco
var radianos = this.rotacao * Math.PI / 180 + Math.PI /2 ;
ctx.save();
ctx.translate(this.brancaX, this.brancaY);
ctx.rotate(radianos);
ctx.drawImage(this.imagem, -7,
200

## Página 219

CasadoCódigo Capítulo9. Interaçãocomojogadorelógicasdenegócio
this.deslocamento() + this.raioDistancia,
this.imagem.width, this.imagem.height);
ctx.restore();
},
Sabemos quando a tacada terminou, portanto nesse momento vamos
reposicionar o taco e zerar as forças. Acrescente as seguintes linhas em
bolasPararam:
function bolasPararam() {
// ...
posicionarTaco();
barraForca.forca =0 ;
taco.forca =0 ;
}
Façamosumtestemaisamplonocelular .A tiveoevento deviceready,
descomenteoscomandosenvolvendoo somTacadaecertifique-sedequea
t a c a d ad i s p a r aos o meot a c oa c o m p a n h aab o l ab r a n c aac a d ajogada. Isto
estáficandodivertido!
9.4 Tratamentodascolisões
Sóatacadavaifazersom? Precisamosfazeroschoquesentrebolas,entreuma
bolaeumaparede,eentreumabolaeumsensordecaçapaproduziremsons
também. Portanto, vamos aprender como reagir a colisões entre corpos no
Box2dWeb. Adetecção de colisõese n t r ed i v e r s a sf o r m a sg e o m é t r i c a sj áér e -
alizadaautomaticamentepelaengine,bastando-nosrealizaroseu tratamento
nojogo.
No evento
onloaddapágina,mandecarregartodosossons:
somTacada = new Media( ' file:///android_asset/colisao.mp3 ' );
somMadeira = new Media( ' file:///android_asset/knock.mp3 ' );
somCacapa = new Media( ' file:///android_asset/hit.mp3 ' );
Em iniciar, vamos instanciar um novo objeto,ColisaoListener,
a ser criado logo mais. Este objeto será o responsável por receber os
201

## Página 220

9.4. Tratamentodascolisões CasadoCódigo
eventos de colisão do Box2dWeb. Para inseri-lo no mundo, usamos
SetContactListener:
function iniciar() {
// ...
colisaoListener = new ColisaoListener(somTacada, somMadeira,
somCacapa);
mundo.SetContactListener(colisaoListener);
animacao.ligar();
}
Atualizeasvariáveisdapáginacomosegue:
var canvas, context, mundo, animacao;
var ESCALA =3 0 ;
var bolaBranca, bolasColoridas;
var hammer, taco, barraForca;
var somTacada, somMadeira, somCacapa, colisaoListener;
Efaçaolinkpara colisao-listener.js:
<script src="js/colisao-listener.js"></script>
V a m o sa g o r ac r i a ran o v ac l a s s eColisaoListener. O construtor so-
mentearmazenaráreferênciasaossons:
function ColisaoListener(somBola, somMadeira, somCacapa) {
this.somBola = somBola;
this.somMadeira = somMadeira;
this.somCacapa = somCacapa;
}
Um objeto ouvinte de colisões do Box2dWeb deve seguir uma interface,
ouseja,implementarumcertoconjuntodemétodos. Noentanto,comonem
todoselespodemnosinteressar,existeoobjeto b2ContactListener,que
já implementa todos eles, porém com corpos vazios. Devemos fazer nossa
classe herdar os métodos existentes em
b2ContactListener es o b r e s c r -
everaquelesquenosinteressarem. EmJavaScript,umaherançaentreclasses
202

## Página 221

CasadoCódigo Capítulo9. Interaçãocomojogadorelógicasdenegócio
podesersimuladadefinindoumobjetocomoprotótipodeoutro. Nasequên-
ciadocódigo:
// ColisaoListener herda os métodos de b2ContactListener
ColisaoListener.prototype = new b2ContactListener();
Continuando,vamosredefinirométodo BeginContact. Destaveznão
podemos atribuir um novo protótipo, mas modificar o método do protótipo
recém-criado. EssemétodoéchamadopeloBox2dWeblogonoiníciodeum
contato entrefixtures de corpos, e recebe um parâmetrocom os dados desse
contato.
ColisaoListener.prototype.BeginContact = function(contato) {
// tratamento da colisão aqui
}
Preste atenção ao “caminho” até chegar aos corpos e seus sprites associ-
ados. Os métodos GetFixtureA e GetFixtureB, do objeto contato,
obtêm as fixtures em colisão. Para saber quais seus corpos correspondentes,
chamamos
GetBody. Eospritetinhasidoassociadoaocorpocomoum user
data,p o r t a n t oGetUserData deve nos retornar umaBola,u m Taco ou
uma Parede!
ColisaoListener.prototype.BeginContact = function(contato) {
var corpoA = contato.GetFixtureA().GetBody();
var corpoB = contato.GetFixtureB().GetBody();
var objetoA = corpoA.GetUserData();
var objetoB = corpoB.GetUserData();
// continua...
}
Testemos os tipos dos objetos. Para facilitar, salvamos os testes em var-
iáveis. Temos que testar a possibilidade de serem duas bolas se chocando,
perguntando se
objetoA e objetoB s ã od ot i p oBola, e a possibilidade
deuma Bolasechocarcom Paredeou Cacapa,nãoimportandoqualé A
ouB:
203

## Página 222

9.4. Tratamentodascolisões CasadoCódigo
ColisaoListener.prototype.BeginContact = function(contato) {
// ...
var bola1 = (objetoA instanceof Bola ? objetoA : null);
var bola2 = (objetoB instanceof Bola ? objetoB : null);
var bola = bola1 || bola2; // Quem quer que seja a Bola!
var parede = (objetoA instanceof Parede ? objetoA :
objetoB instanceof Parede ? objetoB : null);
var cacapa = (objetoA instanceof Cacapa ? objetoA :
objetoB instanceof Cacapa ? objetoB : null);
// continua...
}
Podemos, enfim, reagir às colisões, disparando os respectivos sons. No
c a s od es e rb o l ac o mc a ç a p a ,c h a m a m o soc a l l b a c kencacapou na bola, de
modoaexecutaralógicadenegócio:
ColisaoListener.prototype.BeginContact = function(contato) {
// ...
if (bola1 && bola2) {
this.somBola.play();
this.somBola.seekTo(0); // Rebobinar para a próxima
}
else if (bola && parede) {
this.somMadeira.play();
this.somMadeira.seekTo( 0);
}
else if (bola && cacapa) {
this.somCacapa.play();
this.somCacapa.seekTo(0);
if (bola.encacapou) bola.encacapou(bola);
}
}
Noconstrutorda Bola,documenteessecallbacketambémcrieumatrib-
uto foraDeJogo,comovalor false,parapodermosexecutaralgunstestes
204

## Página 223

CasadoCódigo Capítulo9. Interaçãocomojogadorelógicasdenegócio
adiante:
this.encacapou = null;
this.foraDeJogo = false;
No index.html,e m criarBolaBranca, atribua um callback antes
do return:
function criarBolaBranca(x, y) {
// ...
b.encacapou = encacapouBranca;
return b;
}
Eatribuaoutroem criarBolasColoridas,dentrodoloopquecriaas
bolas:
function criarBolasColoridas(arrayDados) {
// ...
for (var i in arr) {
// ...
b.encacapou = encacapouColorida;
}
// ...
}
Temos que criar esses callbacks. O da bola branca vai reposicioná-la, e
o das coloridas irá excluí-las quando encaçapadas. Mas aqui é preciso muita
cautela.Não devemos mudar o estado de um corpo durante um tratamento de
colisão, pois o passo (Step) ainda está sendo processado!Em outras palavras,
nada de reposicionar ou excluir os corpos: simplesmente não funcionará. E
agora?
Temos que agendar essa tarefa para após o
Step. Felizmente, já temos
ummecanismoparaisso: podemosadicionarprocessamentosaoloopdean-
imação,paraseremexecutadosaofimdecadaciclo!
No callback
encacapouBranca, crie um processamento. Lá dentro,
sinalize que a bola está fora do jogo, pare seu movimento e posicione-a do
205

## Página 224

9.4. Tratamentodascolisões CasadoCódigo
ladodeforadamesa,paranãoatrapalharomovimentodasoutras. Nofinal,
oprocessamentodeveserexcluído:
function encacapouBranca(bola) {
// Somente ao fim do ciclo
animacao.novoProcessamento({
processar: function() {
bola.foraDeJogo = true;
bola.corpo.SetLinearVelocity( new b2Vec2(0, 0));
bola.corpo.SetPosition( new b2Vec2(-1000, -1000));
// Excluir para executar apenas uma vez
animacao.excluirProcessamento( this);
}
});
}
Em bolasPararam,querespondeaofimdeumatacada,vamosverificar
se a bola branca foi encaçapada, reposicioná-la e retorná-la para o jogo. Isso
deveserfei toan tesdachamadaa posicionarTaco:
function bolasPararam() {
if (bolaBranca.foraDeJogo) {
bolaBranca.corpo.SetPosition(
new b2Vec2(150/ ESCALA, 200/ESCALA));
bolaBranca.foraDeJogo = false;
}
// posicionarTaco() por aqui...
}
Etemosooutrocallback, encacapouColorida. Quandoumabolacol-
oridaéencaçapada,eladevesairdojogo. Essalógicadenegócioserádelegada
paraaclasse Bola:
function encacapouColorida(bola) {
animacao.novoProcessamento({
processar: function() {
bola.tirarDoJogo();
206

## Página 225

CasadoCódigo Capítulo9. Interaçãocomojogadorelógicasdenegócio
animacao.excluirProcessamento( this);
}
});
}
O método tirarDoJogo,n ac l a s s eBola, vai executar todas as ações
necessárias: excluir o corpo do mundo físico, excluir o sprite da animação e
sinalizarqueaquelabolaestáforadojogo:
tirarDoJogo : function() {
this.mundo.DestroyBody( this.corpo);
this.animacao.excluirSprite( this);
this.foraDeJogo = true;
}
Devoltaàclasse Tacada,verifiqueseabola não(símbolo !)estáforade
jogo, alémdeestar acordada, para considerá-laativa. Dessaforma, qualquer
bolaqueforemborapelascaçapasnãoprecisaaguardarumbomtemposendo
freada:
processar: function() {
// ...
// Monitorar o movimento
if (!b.foraDeJogo && b.corpo.IsAwake()) {
// ...
}
Ainteraçãocomojogadorestáfinalizada! Fomoscapazesde:
• integraroscontrolesdotacoedabarradeforçaaojogo;
• alinharodesenhodotacocomoângulodetacadaecolocarsuaponta
nabo r dadabola;
• dispararumatacadanoânguloecomaforçadefinidosnoscontroles;
• aguar darasbolasparar emparato maro u trasmedidas;
207

## Página 226

9.4. Tratamentodascolisões CasadoCódigo
• “sumir”comabolabrancaeretorná-laaoiníciodojogo,seforencaça-
pada;
• excluirdeverdadeasbolascoloridasencaçapadas.
Nopróximocapítulo,veremoscomoocomputadorpoderácalcularuma
tacadaautomática,aproveitando-sedofatodequeaBox2dWebpodefazeras
simulações físicas somente em memória. Brinque um pouco, o jogo começa
ago raaficarvician te!
208

## Página 227

Capítulo10
Simulaçõesinternas
Nestecapítulo,discutocomopodemosfazeramáquinapensarparadetermi-
nar sua jogada. Usando uma engine física, calcular a jogada automática não
requerconhecimentoseminteligênci aartificial. SabendoqueoBox2Desuas
variaçõesemoutraslinguagens( ports)trabalhamemmemória,podemosre-
alizardiferentestacadasporbaixodospanos,analisarosresultadosemostrar
natelaaquelaquequeformaisvantajosa.
Issoparecesimples,erealmenteé,masháconsideraçõesimportantesase
fazer:
• a cada simulação feita em memória, devemos retornar todas as bolas
paraasposiçõesemqueseencontravamnoinício;
• o processamento da tacada só termina após passado um período de
tempo,quandosecomeçaafrearomovimentodasbolas;

## Página 228

10.1. Realizandováriassimulaçõesapartirdoinício CasadoCódigo
• nosso tratador de colisões está disparando sons e tirando as bolas do
jogo.
V amospensaremcadaumdestesp r oblemaspo rvez.
10.1 Realizando várias simulações a partir do
início
Simularemos diversas tacadas, em diversos ângulos. Só para testar, forçare-
mosoco m p u tado radarumatacadalogoaofimdafunção iniciar:
function iniciar() {
// ...
tacadaComputador();
}
Na função tacadaComputador, criamos um objeto
TacadaAutomatica e o mandamos fazer os testes, devolvendo os da-
dos da tacada que deu os melhores resultados. Tudo de forma abstraída,
delegandoparaessaclasseoserviçopesado:
function tacadaComputador() {
var automatica = new TacadaAutomatica(mundo, bolaBranca,
bolasColoridas);
var melhorTacada = automatica.realizarTestes();
taco.rotacao = melhorTacada.rotacao;
taco.forca = melhorTacada.forca;
tacada();
}
Crie o arquivo tacada-automatica.js. Para simular uma tacada,
temos que distinguir a bola branca das coloridas (veja a classeTacada), e
tambémprecisamosdomundoparasimularos Steps:
function TacadaAutomatica(mundo, branca, coloridas) {
this.mundo = mundo;
this.branca = branca;
this.coloridas = coloridas;
210

## Página 229

CasadoCódigo Capítulo10. Simulaçõesinternas
}
TacadaAutomatica.prototype = {
realizarTestes: function() {
}
}
Em realizarTestes,vamosdelegarparaaclasse Snapshot atarefa
de salvar e recuperar a posição das bolas. Chamamossalvar no início e
reverterapóscadasimulação. Asimulaçãoéfeitanométodo executar,
querecebeoânguloeaforçaaseremtest ados,edeveráretornarosdadosque
obteremosdatacada:
realizarTestes: function() {
var estadoJogo = new Snapshot(this.mundo);
estadoJogo.salvar(); // Guarda no início
var resultados = [];
// De 5 em 5 graus para não onerar o processador
for (var i =0 ;i<= 360;i+= 5){
var tacada = this.executar(i, 75); // ângulo, força
resultados.push(tacada);
estadoJogo.reverter(); // Reverte após cada uma
}
// Como decidir qual foi a melhor simulação?
return resultados[0];
}, // vírgula pois terá o executar
O salto de 5 em 5 graus é mais um detalhe a que não cheguei logo de
primeira. Fizváriostestesaofimdaimplementação,osquaisrecomendovocê
fazer também. Dar 360 tacadas, voltando as bolas para suas posições após
cada uma, leva bastante tempo. Também evitei testar diferentes valores de
força para cada ângulo. Se quiser, você pode, como um exercício, encontrar
umbalanceamentoadequadoentrequantosângulosequantasforçaspodem
sertestadasparacadaum.
211

## Página 230

10.1. Realizandováriassimulaçõesapartirdoinício CasadoCódigo
Ainda não temos como decidir qual simulação deu o melhor resultado,
poisnãodefinimosquaisregrasdejogovamosadotar. Faremosissonopróx-
imocapítulo. Masvamospelomenosnoscertificardequeassimulaçõesestão
acontecendoequeodesempenhodesseprocessamentosejaaceitável.
No método
executar, criamos um objeto Tacada e “em-
purramos” o processamento com um loop while,e mv e zd eu s a r
requestAnimationFrameou setTimeout. Oloopécontroladopelavar-
iável continua,queésetadapara falsequandooprocessamentoreportar
ofimdaaçãonocallback aposTacada:
executar: function(angulo, forca) {
var tacada = new Tacada(this.branca, this.coloridas);
var continua = true;
tacada.aposTacada = function() {
continua = false;
}
tacada.disparar(angulo, forca);
while (continua) {
this.mundo.Step(1/60, 10, 5);
tacada.processar();
}
// Obteremos depois outros dados
return { rotacao: angulo, forca: forca };
}
Nossa prática até aqui tem sido avançar o mundo físico, em cada ciclo
doloopdeanimação,nomesmotempomedidopelorelógiodocomputador,
criandoumasimulaçãoemtemporeal. Aindaassim,nadaimpedequetodos
os passos (
Steps) de uma tacada sejam simulados de forma seguida, em
loops for ou while comuns, sem nos atrelarmos ao relógio. ABox2dWeb
calculaaposiçãodoscorposnotempo,independentementedeessetempoter
sepassadonorelógioounão.
212

## Página 231

CasadoCódigo Capítulo10. Simulaçõesinternas
10.2 Salvando e recuperando o estado do
mundofísico
Para tudo isso funcionar, temos que implementar a classeSnapshot.N e l a ,
guardaremosasposiçõesdasbolas. Crieoarquivo snapshot.js:
function Snapshot(mundo) {
this.mundo = mundo;
this.posicoes = [];
}
Snapshot.prototype = {
salvar: function() {
},
reverter: function() {
}
}
O método salvar vai fazer loop nos corpos e guardar as posições.
Perceba que não guardamos diretamente os objetos devolvidos por
GetPosition,e,sim,copiamososvaloresparanovosobjetos. Fazemosisso
porque variáveis de objetos sãoreferências, ou seja, estaríamos na verdade
referenciandoosobjetosdeposiçãoreaisdoscorpos,quepoderãoestaralter-
adosnahoradereverter.
salvar: function() {
var arrPosicoes = [];
var corpo = this.mundo.GetBodyList();
while (corpo) {
var pos = corpo.GetPosition();
var obj = { corpo: corpo, x : pos.x, y : pos.y };
arrPosicoes.push(obj);
corpo = corpo.GetNext();
}
this.posicoes = arrPosicoes;
},
213

## Página 232

10.2. Salvandoerecuperandooestadodomundofísico CasadoCódigo
Algoritmoparaiterarportodososcorpos
Aprimeirareferênciaéobtidapor GetBodyList; aspróximas, por
GetNext. Quandofordevolvido null,osco rposseacabaram:
var corpo = this.mundo.GetBodyList();
while (corpo) {
// ...
corpo = corpo.GetNext();
}
O método reverter só precisa fazer um loop no array de posições
guardadasechamar SetPositionparareatribuí-lasaoscorpos:
reverter: function() {
for (var i in this .posicoes) {
var pos = this.posicoes[i];
pos.corpo.SetPosition( new b2Vec2(pos.x, pos.y));
}
}
Quero frisar que, para a nossa necessidade aqui, apenas guardar e re-
tornar as posições dos corpos é suficiente, já que cada jogada é feita com
as bolas paradas. Você pode estender a classeSnapshot para guardar ve-
locidades lineares e angulares, com os métodosGetLinearVelocity e
GetAngularVelocity, respectivamente, e recuperá-las com osSetsc o r -
respondentes.
Nãoseesqueçadelinkarosscriptsdasduasclassesnovas:
<script src="js/tacada-automatica.js"></script>
<script src="js/snapshot.js"></script>
214

## Página 233

CasadoCódigo Capítulo10. Simulaçõesinternas
10.3 Executandoatacadaemtempocurto
Seexecutarmosojogonopontoemqueestá,veremosatelaparadaenquanto
as simulações acontecem. Dá até para ouvir os sons. Mas lembre-se de que
a
Tacada faz uma desaceleração progressiva das bolas, sendo que depois
de 7 segundos ela “pisa mais fundo” no freio. Fazendo isso 72 vezes (360/5),
imagine o tempo que leva. Não adianta nada fazermos os
Stepsd ef o r m a
seguidaseaclasse Tacadasótrabalhacomorelógio.
Figura10.1: Aguardandoassimulaçõesacontecerem
Vamos flexibilizá-la para que trabalhe também com contagem de
quadros. Sabendo que cada quadro leva 1/60 de segundo, basta contar os
quadros para saber quanto tempo uma tacada levou, sem precisar esperar
esse tempo passar de verdade. Podemos assim fazer simulações mais ráp-
idas, enquanto a animação pode (e deve) continuar dependendo do relógio,
acontecendonavelocidadeemqueoseventosfísicosaconteceriamnomundo
real.
No método
executarda TacadaAutomatica,estamosinstanciando
a Tacada. Configuredoisnovosatributos, porRelogioe tempoAvanco:
executar: function(angulo, forca) {
var tacada = new Tacada( this.branca, this.coloridas);
tacada.porRelogio = false;
tacada.tempoAvanco = 1/60;
215

## Página 234

10.3. Executandoatacadaemtempocurto CasadoCódigo
// ...
}
No construtor daTacada, inicie o atributoporRelogio como true,
paranãoquebrarocomportamentopadrão. O tempoAvanco podeserini-
ciado como zero, para documentação de atributos, pois só será usado se for
parasimulaçãorápida:
function Tacada(branca, coloridas) {
// ...
this.porRelogio = true;
this.tempoAvanco =0 ;
}
Na simulação rápida, devemos fazer uma contagem de quadros para de-
terminarotempoavançado. Em disparar,inicieumatributo quadrocom
zero:
disparar: function(angulo, forca) {
// ...
this.quadro =0 ;
},
Eem processar,incrementamosocontadoredecidimosseéporreló-
gio ou por contagem de quadros. Se for por relógio, determinamos o tempo
decorrido da mesma forma como estávamos fazendo. Se for por contagem,
sabemosquantosquadrosforamavançadosequantotempofoisimulado,pelo
atributo
tempoAvanco:
processar: function() {
if (!this.rodando) return;
this.quadro++;
// Quantos segundos já se passaram
var sete, cinco, tres;
if (this.porRelogio) {
// Esta linha vem para cá
var decorrido = Date .now() - this.inicio;
sete = (decorrido >= 7000);
216

## Página 235

CasadoCódigo Capítulo10. Simulaçõesinternas
cinco = (decorrido >= 5000);
tres = (decorrido >= 3000 );
}
else {
var segundos = this.quadro * this.tempoAvanco;
sete = (segundos >= 7);
cinco = (segundos >= 5);
tres = (segundos >= 3);
}
// ...
}
Basta-nosentãousarasvariáveisdostestesparafrearasbolas. Modifique
otr echode processaremqueissoocorre:
processar: function() {
// ...
// Frear a bola
if (sete)
b.frear(5.0 );
else if (cinco)
b.frear(1.0 );
else if (tres)
b.frear(0.7 );
// ...
}
Ac l a s s eTacada poderia trabalhar somente com contagem de
quadros,mesmonoloopdeanimação,poisestejácontrolaotempoen-
tre os passos. Mas isso nos obrigaria, a cada tacada criada, a informar
o
tempoAvancoasersimulado,razãoporquepreferimantê-laflexível.
Estejaàvontadeparaexperimentaressaabordagem,sequiser.
E x p e r i m e n t ee x e c u t a rn od i s p o s i t i v om ó v e ln e s t em o m e n t o . Ot e m p o
de simulação já melhorou bastante, embora ainda esteja longe do adequado,
217

## Página 236

10.4. Tratadordecolisõesparaasimulação CasadoCódigo
e também escutamos os sons disparados pelo tratador de colisão. As bolas
queforamencaçapadasnessepercursosomem,poiséoquemandamosfazer
nessescasos. Tendoresolvidoprimeiroosproblemasdedesempenho,vamos
resolverestes.
10.4 Tratadordecolisõesparaasimulação
Vamoscriaroutraclassetratadoradecolisãovoltadaparaassimulações. Esta
classenãodispararásonsedetectaráinicialmentesomenteasencaçapadas.
Nafunção
tacadaComputador,altereotratadordecolisãonoinício,e
retorne ao original após o fim das simulações, mas antes de realizar a tacada
“real”dojogo:
function tacadaComputador() {
mundo.SetContactListener(simulacaoListener);
// ...
mundo.SetContactListener(colisaoListener);
tacada();
}
Declareavariável simulacaoListenernapágina:
var canvas, context, mundo, animacao;
var ESCALA =30 ;
var bolaBranca, bolasColoridas;
var hammer, taco, barraForca, somTacada;
var somTacada, somMadeira, somCacapa;
var colisaoListener, simulacaoListener;
Instancieoseuobjetoem iniciar(podeserjuntocomoprimeiro):
function iniciar() {
// ...
simulacaoListener = new SimulacaoListener();
colisaoListener = new ColisaoListener(somTacada, somMadeira,
218

## Página 237

CasadoCódigo Capítulo10. Simulaçõesinternas
somCacapa);
mundo.SetContactListener(colisaoListener);
// ...
}
Nãoseesqueçadelinkaroarquivodescript:
<script src="js/simulacao-listener.js"></script>
Evamoscriá-lo. Percebaqueéumaversãobastantereduzidadoprimeiro,
já que sua função por enquanto é reportar somente contato entreBola e
Cacapa:
function SimulacaoListener() {
this.encacapou = null;
}
SimulacaoListener.prototype = new b2ContactListener();
SimulacaoListener.prototype.BeginContact = function(contato) {
var objA = contato.GetFixtureA().GetBody().GetUserData();
var objB = contato.GetFixtureB().GetBody().GetUserData();
var bola = (objA instanceof Bola ? objA :
objB instanceof Bola ? objB : null);
var cacapa = (objA instanceof Cacapa ? objA :
objB instanceof Cacapa ? objB : null);
if (bola && cacapa && this.encacapou)
this.encacapou(bola);
}
Respondendoaocallback
Façacomquea TacadaAutomaticarecebaessesimuladornoconstru-
tor. Comoessaclasseéresponsávelporcalcularajogadadocomputador,ela
forneceráumcallbackqueverificaráasbolasencaçapadas:
219

## Página 238

10.4. Tratadordecolisõesparaasimulação CasadoCódigo
function tacadaComputador() {
mundo.SetContactListener(simulacaoListener);
var automatica = new TacadaAutomatica(mundo, bolaBranca,
bolasColoridas, simulacaoListener);
// ...
}
Noseuconstrutor,recebemosocolisorecriamosumcallbackquechama
ono vométodo aoEncacapar:
function TacadaAutomatica(mundo, branca, coloridas, colisor) {
// ...
var tacadaAuto = this ;
colisor.encacapou = function(bola) {
tacadaAuto.aoEncacapar(bola);
}
}
Nesse método, precisaríamos fazer algo para tirar a bola da mesa, para
evitar que continue colidindo com outras (caso não tenha saído para fora).
Porém, lembre-se de que, durante o tratamento de colisão, isso não pode ser
feito(seção 9.4). Portantoaquivamosapenasregistrarqueabolafoiencaça-
pada:
// Chamado dentro do Step pelo tratador de colisão
aoEncacapar : function(bola) {
this.encacapadas.push(bola);
}
Em executar, inicie o arrayencacapadas a n t e sd ep r o c e s s a rt o d o s
os passos. Após cadaStep, podemos chamar um método para cuidar das
bolas quedeverão “sumir”,deslocarEncacapadas. Por fim, tendo as bo-
lasencaçapadasdevidamenteregistrad aspelocallback,podemosretorná-las
comoresultado:
executar: function(angulo, forca) {
// ...
220

## Página 239

CasadoCódigo Capítulo10. Simulaçõesinternas
// Zerar o array antes de processar os ciclos
this.encacapadas = [];
while (continua) {
this.mundo.Step(0.1, 10, 5);
tacada.processar();
// Após o Step podemos dar um jeito nas bolas que se foram
this.deslocarEncacapadas();
}
// Ao fim podemos retornar os resultados (return no final!!)
return {
rotacao: angulo,
forca: forca,
encacapadas : this.encacapadas
};
},
Em deslocarEncacapadas,podemosfazercomasbolasomesmoque
fazemoscomabolabrancaemumatacada“normal": pararseumovimentoe
deslocá-lasparaalémdasparedes,paranãointerferirnomovimentodasque
ficam:
deslocarEncacapadas : function() {
var arr = this.encacapadas;
for (var i in arr) {
arr[i].corpo.SetLinearVelocity( new b2Vec2(0, 0));
arr[i].corpo.SetPosition( new b2Vec2(-1000, -1000));
}
}
Se você rodar o aplicativo, o aparelho já consegue “pensar” por uns in-
stantes, testando tacadas em todos os ângulos que determinamos, antes de
disparar uma tacada para valer. Aindaf a l t ae s c o l h e rq u a lom e l h o râ n g u l o ,
mas para isso temos que ter claras as regras do jogo. No próximo capítulo
discutiremosmaisafundoqueregrasvamosadotar,poisexistemmuitasvar-
iedadesdebilharesinuca. Poderemos entãofacilmentedeterminaramelhor
221

## Página 240

10.4. Tratadordecolisõesparaasimulação CasadoCódigo
tacada, bem como gerenciar a partida, alternando jogadas do humano e do
computadoredeterminandoquandoumvenceu. Faltapoucoagora!
222

## Página 241

Capítulo11
Finalizandoojogo
Estamos quase lá! Precisamos agora determinar as regras do jogo para po-
dermos fazer a máquina raciocinar sobre suas tacadas e sobre a partida. Por
que deixei isto somente para o final do livro, se o correto é iniciarmos o de-
senvolvimentocomasregrasdefinidas? Porqueexisteminúmerasvariaçõesde
jogosdebilharousinuca. Tendoprogramadotodaamecânicademovimento,
podemos reaproveitá-la em diferentes versões do jogo. Se quiser, mantenha
uma cópia reservada do jogo até este ponto. Você pode depois implementar
asregrasdeoutravariaçãoquecostumajogar.

## Página 242

11.1. RegrasdoBola9 CasadoCódigo
Figura11.1: Resultadofinalaseratingido
11.1 RegrasdoBola9
Aqui implementaremos oBola 9, uma variedade de bilhar, de acordo com o
queestádescritoem http://pt.wikipedia.org/wiki/Bilhar:
• oob jetivodojogoéencaça paraboladen úmer o9;
• a bola branca deve sempre atingir primeiro a de menor número ainda
namesa;
• seencaçaparalgumabolacolorida,desdequeapartirdaboladeordem,
ojogadordavezcontinua;
• se a bola 9 for encaçapada dentro dessas condições, em qualquer mo-
mento,ojogadordavezganhaapartida;
• se a branca não acertar nenhuma bola ou acertar uma bola inválida, o
jogadorpassaavez,mesmoqueencaçape;
• se a branca for encaçapada, ela retorna para sua posição inicial. O
mesmo ocorre com a bola 9 encaçapada de maneira ilegítima. Nesses
casos,ojogadortambémpassaavez.
Primeiro, vamos declarar todas as variáveis de página responsáveis pelo
tratamentodasregras. Confiraarelaçãofinaldedeclarações:
224

## Página 243

CasadoCódigo Capítulo11. Finalizandoojogo
var canvas, context, mundo, animacao;
var ESCALA =3 0 ;
var bolaBranca, bolasColoridas;
var hammer, taco, barraForca;
var somTacada, somMadeira, somCacapa;
var colisaoListener, simulacaoListener;
var bolaOrdem, jogadorDaVez, primeiraAtingida, encacapadas,
mostrador;
var JOG_HUMANO =1 , JOG_COMPUTADOR =2 ;
Agora, configure o início de uma partida. Na funçãoiniciar, retire a
chamadadiretaa tacadaComputadoremudeparadefinirqueméjogador
davezequalaprimeirabolaaseracertada:
function iniciar() {
// ...
// O final fica:
jogadorDaVez = JOG_HUMANO;
bolaOrdem = bolasColoridas[0];
animacao.ligar();
// Remova
//tacadaComputador();
}
Sorteandoojogador
Sedesejar,use Math.randomparadeterminarquemsainaprimeira
partida.
Determinandoaprimeirabolaatingida
Antes de tudo, vamos determinar qual foi a primeira bola atingida pela
bola branca em uma tacada. Para isso, temos que ouvir eventos de colisão
e n t r eb o l a s .I s s oj áe s t ás e n d of e i t oe mColisaoListener, mas não em
SimulacaoListener. Altereaclasseparaquedetecteessasituaçãoechame
umcallback:
225

## Página 244

11.1. RegrasdoBola9 CasadoCódigo
SimulacaoListener.prototype.BeginContact = function(contato) {
var objA = contato.GetFixtureA().GetBody().GetUserData();
var objB = contato.GetFixtureB().GetBody().GetUserData();
// Detecte ambas as bolas
var bola1 = (objA instanceof Bola ? objA : null);
var bola2 = (objB instanceof Bola ? objB : null);
var bola = (bola1 || bola2);
var cacapa = (objA instanceof Cacapa ? objA :
objB instanceof Cacapa ? objB : null);
if (bola && cacapa && this.encacapou)
this.encacapou(bola);
// Callback de colisão
if (bola1 && bola2)
this.colisaoBolas(bola1, bola2);
}
Em TacadaAutomatica, no método executar, inicie o atributo
primeiraAtingida como null antes do loop que processa os passos da
tacadadesimulação:
this.encacapadas = [];
this.primeiraAtingida = null;
while (continua) {
// ...
}
Noconstrutor,crieumcallbackqueverificaqualaprimeirabolaatingida
p e l ab r a n c a .S eoa t r i b u t oj áe s t i v e rs e t a d o ,n a d ad e v es e rf e i t o .S eab r a n c a
nãopegaremnenhuma,oeventonãoocorreráeoatributocontinuará null:
function TacadaAutomatica(mundo, branca, coloridas, colisor) {
// ...
colisor.colisaoBolas = function (bola1, bola2) {
226

## Página 245

CasadoCódigo Capítulo11. Finalizandoojogo
if (tacadaAuto.primeiraAtingida) return;
if (bola1.id == BOLA_BRANCA)
tacadaAuto.primeiraAtingida = bola2;
else if (bola2.id == BOLA_BRANCA)
tacadaAuto.primeiraAtingida = bola1;
}
}
Analogamente, a classeColisaoListener também deve disparar um
callbackemcasodecolisãoentrebolas:
if (bola1 && bola2) {
this.somBola.play();
this.somBola.seekTo(0);
if (this.colisaoBolas) this.colisaoBolas(bola1, bola2);
}
Claro,documenteocallbacknoconstrutor:
function ColisaoListener(somBola, somMadeira, somCacapa) {
// ...
this.colisaoBolas = null;
}
Agora,atribuaessecallbacknapáginaHTML,nafunção iniciar(pode
serlogoapósainstanciação):
colisaoListener = new ColisaoListener(somTacada, somMadeira,
somCacapa);
colisaoListener.colisaoBolas = colisaoEntreBolas;
Por fim, crie a função colisaoEntreBolas, com a mesma lógica
de determinação da primeira bola atingida, mas referenciando a variável
primeiraAtingidadapágina:
function colisaoEntreBolas(bola1, bola2) {
if (primeiraAtingida) return;
if (bola1.id == BOLA_BRANCA)
227

## Página 246

11.1. RegrasdoBola9 CasadoCódigo
primeiraAtingida = bola2;
else if (bola2.id == BOLA_BRANCA)
primeiraAtingida = bola1;
}
Analisandoasjogadas
Sabendoqualaprimeirabolaquefoiatingidapelabrancaemumatacada,
seja em simulação ou numa tacada real do jogo, podemos aplicar as regras
para analisar a jogada. Vamos delegar essa tarefa para uma nova classe,
AnaliseJogada, para podermos usar as mesmas regras em todas as situ-
ações. Portanto,façaseulinknapágina:
<script src="js/analise-jogada.js" ></script>
Antes de programá-la, é preciso definir o que esperar dela, conforme
nossa prática habitual de primeiro “mandar” na classe, para depois fazê-la
obedecer. Na classe
TacadaAutomatica, no métodorealizarTestes,
vamos fazer a análise ao fim de cada ciclo do loop que testa os ângulos,
guardando os resultados. Tão logo ocorreralgo favorável, podemos parar os
testes e retornar o objeto com os dados, economizando tempo de processa-
mento. Perceba que, para analisarmos corretamente uma tacada, temos que
saber qual a bola de ordem (da vez), por isso a recebemos como parâmetro
noinício:
// Receba a bola de ordem
realizarTestes: function(bolaOrdem) {
// ...
for (var i =0 ;i<= 360;i+= 5){
// ...
var analise = new AnaliseJogada();
analise.analisar(this.primeiraAtingida, bolaOrdem,
tacada.encacapadas);
// Guarda a análise junto no resultado
tacada.analise = analise;
228

## Página 247

CasadoCódigo Capítulo11. Finalizandoojogo
// Por ordem de prioridade
if (analise.ganhouJogo)
return tacada;
else if (analise.encacapou)
return tacada;
}
// ...
}
Ao fim do método, se não foi encontrada nenhuma tacada favorável, fi-
camoscomaprimeiraqueforlegal:
realizarTestes: function(bolaOrdem) {
// ...
// Encontrar a primeira tacada válida
for (var i in resultados) {
if (resultados[i].analise.jogadaLegal)
return resultados[i];
}
// Se não foi possível fazer nenhuma válida...
return resultados[0];
},
Na função tacadaComptuador,passeaboladeordem,jádefinidaan-
teriormente,quandochamar realizarTestes:
function tacadaComputador() {
// ...
var melhorTacada = automatica.realizarTestes(bolaOrdem);
// ...
}
Agoracomeceaimplementaraclasse AnaliseJogada.N oc o n s t r u t o r ,
documentaremostodasassituaçõespossíveis:
229

## Página 248

11.1. RegrasdoBola9 CasadoCódigo
function AnaliseJogada() {
this.jogadaLegal = false;
this.encacapouBranca = false;
this.encacapou = false;
this.ganhouJogo = false;
}
No método analisar, começamos montando um array somente com
osnúmerosdasbolas,afimdefacilitaraanálise. Definimosqueumajogadaé
legalcasoaprimeirabolaatingidasejaaboladeordemeabrancanãotenha
sido encaçapada. Em caso de jogada legal, podemos determinar se houve
encaçapadanormal(paraojogadorpodercontinuar)esehouvevitória(bola
9encaçapadaemumajogadalegal):
AnaliseJogada.prototype = {
analisar: function(primeiraAtingida,bolaOrdem,encacapadas){
// Números (IDs)
var ids = [];
for (var i in encacapadas)
ids.push(encacapadas[i].id);
// Jogada foi válida?
this.encacapouBranca = (ids.indexOf(BOLA_BRANCA) >= 0);
this.jogadaLegal = (primeiraAtingida &&
primeiraAtingida.id == bolaOrdem.id &&
!this.encacapouBranca);
// Resultados
this.encacapou = (this.jogadaLegal && ids.length >0 );
this.ganhouJogo =
(this.jogadaLegal && ids.indexOf(9) >= 0);
}
}
O aparelho já levará bem menos tempo para encontrar uma tacada que
dêalgumresultadoou,pelomenos,sejavá lidapelasregrasdojogo. Sequiser
fazer o teste, coloque novamente uma chamada atacadaComputador ao
fimdafunção iniciar.
230

## Página 249

CasadoCódigo Capítulo11. Finalizandoojogo
Controlandoapartida
Analogamente, temos que fazer as mesmas verificações em uma tacada
real, seja do computador, seja do jogador, para controlar o andamento da
partida. Na função tacada, vamos iniciar as variáveisencacapadas e
primeiraAtingida,damesmaformaquenasimulação:
function tacada() {
// ...
// Realizar a tacada
encacapadas = [];
primeiraAtingida = null;
var tacada = new Tacada(bolaBranca, bolasColoridas);
// ...
}
Nas funções encacapouBranca e encacapouColorida, acrescente
a bola encaçapada no array. Não é preciso fazer nenhuma distinção, pois a
classe AnaliseJogada cuida de verificar se a bola branca foi encaçapada,
requerendoapenasumarraycomtodaselas:
function encacapouBranca(bola) {
encacapadas.push(bola);
// ...
}
function encacapouColorida(bola) {
encapapadas.push(bola);
// ...
}
Ocallback bolasPararaméchamadopela Tacadaquandoaanimação
finaliza. Vamoschamaraliumanovafunçãoresponsávelporanalisarajogada
edeterminarorumodapartida:
231

## Página 250

11.1. RegrasdoBola9 CasadoCódigo
function bolasPararam() {
// ...
analisarJogada();
}
Chegamos ao coração da partida, ao árbitro do jogo. A função
analisarJogadasolicitaosserviçosdaclasse AnaliseJogadadamesma
forma que a TacadaAutomatica. Se houve vitória, é exibida uma men-
sagemeapáginaérecarregada. Seencaçapou,nãoalteramosnadaparaper-
mitiraojogadordavezcontinuar. Porém,casonãohajaencaçapadalegítima,
trocamosojogadordavez:
function analisarJogada() {
var analise = new AnaliseJogada();
analise.analisar(primeiraAtingida, bolaOrdem, encacapadas);
// Se ganhou, notifica e reinicia
if (analise.ganhouJogo) {
alert(jogadorDaVez == JOG_HUMANO ? ' Você venceu! ' :
' Você perdeu... ' );
location.reload();
return;
}
// Se não encaçapou legalmente, passa a vez
else if (!analise.encacapou) {
jogadorDaVez = (jogadorDaVez == JOG_HUMANO ?
JOG_COMPUTADOR : JOG_HUMANO );
}
// continua...
}
Também é preciso determinar a bola da vez. No caso, a de menor
número ainda na mesa. Também, se for vez do computador, chamamos
tacadaComputadorpararealizarajogadaautomática:
function analisarJogada() {
// ...
232

## Página 251

CasadoCódigo Capítulo11. Finalizandoojogo
// Mudar a bola de ordem
for (var i in bolasColoridas) {
var b = bolasColoridas[i];
if (!b.foraDeJogo) {
bolaOrdem = b;
break;
}
}
if (jogadorDaVez == JOG_COMPUTADOR)
tacadaComputador();
}
Finalmente, tomemos uma providência com relação à bola 9. Se ela for
encaçapada de maneira ilegítima, temos que retorná-la à mesa. Na função
encacapouColorida,s eon ú m e r od ab o l af o r9 ,d a m o sae l aom e s m o
tratamentoqueàbolabranca:
function encacapouColorida(bola) {
encapapadas.push(bola);
animacao.novoProcessamento({
processar: function() {
if (bola.id == 9){
bola.foraDeJogo = true;
bola.corpo.SetLinearVelocity( new b2Vec2(0, 0));
bola.corpo.SetPosition( new b2Vec2(-100/ESCALA,
-100/ESCALA));
}
else {
bola.tirarDoJogo();
}
animacao.excluirProcessamento( this);
}
});
}
233

## Página 252

11.2. Mostradores CasadoCódigo
Tambémnafunção bolasPararam,queavoltaráparaseulugarinicial.
Isso pode ser feito em qualquer posição da função (pode ser antes ou após a
verificaçãodabolabranca,sóparaagruparlógicassemelhantes):
function bolasPararam() {
var bola9 = bolasColoridas[8]; // começa em zero
if (bola9.foraDeJogo) {
bola9.corpo.SetPosition(
new b2Vec2(560/ ESCALA, 200/ESCALA));
bola9.foraDeJogo = false;
}
// ...
}
Uau! Já é possível jogar uma partida completa! E o computador é
impiedosoetrapaceiro!UsaoBox2dWebparapreverofuturo!
Níveldedificuldade
Você pode inserir fatores aleatórios comMath.random na classe
TacadaAutomatica para fazer o computador rejeitar jogadas fa-
voráveis de vez em quando, diminuindo assim o nível de dificuldade.
Outra sugestão é fazer os testes de 10 em 10 graus (ou outro intervalo),
tornandooprocessamentomaisrápidoeaumentandoaschancesdenão
encontrarumatacadaconveniente.
11.2 Mostradores
Para melhorar a experiência final do jogador, vamos criar um sprite que
mostraqualaboladeordem.
Umúltimoscriptparalinkar:
<script src="js/mostrador.js"></script>
Em iniciar, instancie o sprite e insira-o na animação. Isso deve ser
feitoapósadefiniçãodaboladeordem:
234

## Página 253

CasadoCódigo Capítulo11. Finalizandoojogo
function iniciar() {
// ...
jogadorDaVez = JOG_HUMANO;
bolaOrdem = bolasColoridas[0];
// Quebra aqui para criar o mostrador
mostrador = new Mostrador(context);
mostrador.bolaOrdem = bolaOrdem;
animacao.novoSprite(mostrador);
animacao.ligar();
}
Segue o esqueleto da classe. No construtor, passamos a constante
BOLA_SPRITE, criada embola.js, claramente criando uma dependência
entreosscripts:
function Mostrador(context) {
this.context = context;
this.bolaOrdem = null;
this.sheet = new Spritesheet(context, BOLA_SPRITE, 10, 19);
}
Mostrador.prototype = {
atualizar: function() {
//
},
desenhar: function() {
}
}
Imprimimos o texto “Próxima” e desenhamos a bola em tamanho re-
duzido:
desenhar: function() {
var ctx = this.context;
ctx.save();
235

## Página 254

11.2. Mostradores CasadoCódigo
ctx.fillStyle = ' white ' ;
ctx.font = ' 10px ' ;
ctx.fillText( ' Próxima: ' , 380, 370);
this.sheet.linha = this.bolaOrdem.id;
this.sheet.desenhar(430, 362, 10, 10);
ctx.restore();
}
De volta à página HTML, na função analisarJogada,a t r i b u aa o
mostradoranovaboladeordemquandohouvermudança:
function analisarJogada(){
// ...
// Mudar a bola de ordem
for (var i in bolasColoridas){
var b = bolasColoridas[i];
if (!b.foraDeJogo){
bolaOrdem = b;
mostrador.bolaOrdem = b;
break;
}
}
// ...
}
Oj o g od eb i l h a re s t áp r o n t o !O b v i a m e n t e ,h ám u i t oe s p a ç op a r am e l -
horas e incrementos na jogabilidade, na funcionalidade, na arquitetura, que
você pode implementar como forma de se exercitar e fixar seus novos con-
hecimentos. Não quis, nem de longe, criar o jogo perfeito, e preferi me ater
aoessencial. Masespero,comsinceridade,quetenhagostado.
Nósaprendemosa:
• capturargestosemtelastouchcomoHammer.js;
236

## Página 255

CasadoCódigo Capítulo11. Finalizandoojogo
• associarcorposfísicosaossprites;
• detectar eventos de colisão e agendar a modificação ou exclusão dos
corposparadepoisdo Step;
• disparar callbacks para o jogo e suas classes implementar as regras de
negócionesseseventos.
Sugestõesparamelhorarojogo
• Uma funcionalidade que faz sumir os controles e botões,
permitindo-nosvertodaamesa.
• Mudar de lado o controle do taco, a barra de força e o botão da
t a c a d ad ea c o r d oc o mol a d od am e s ae mq u es ee n c o n t r aab o l a
branca.
• Ou, quem sabe, sumir com o controle circular do taco,
permitindo-nos fazer orotateem qualquer ponto da mesa. Isto
certamente traria um grande ganho de jogabilidade, e só preferi
fazerdomodomaisrestritoparademonstrarcomolimitaraárea.
• Menusdeconfiguraçãoeníveisdedificuldade.
• JogomultiplayercomAjaxetecnologiasdeservidorweb.
• Eoquemaissuaimaginaçãocriar.
237

## Página 257

ParteIII
Conclusão
Chega ao fim mais uma jornada pelo fantástico mundo do Canvas do
HTML5 e suas possibilidades. Nem de longe eu quis esgotar os assuntos.
Acredito que a maior lição que tem de ficar de todo este esforço é que de-
senvolvimentodejogos,comoqualquerdesenvolvimentodesoftware,requer
estudoconstante,umavidadedicadaaestudareapraticar. Porissodeixeitan-
tos links no livro, para que você possa se aprofundar da mesma forma como
eutivequemeaprofundaremcadatópico. Vocêpodeedevesaberqueexiste
maisalémdoqueeutrouxeaqui.
Estareiesperandolinksparaosjogosfeitospormeusleitores,sejaonline,
na Play Store, na Apple Store... Divulgue suas criações para nós no Google
Groups:
http://groups.google.com/forum/#!forum/livro-jogos-html5-canvas
Bomdesenvolvimento!
ÉdersonCássioLacerdaFerreira

## Página 259

CasadoCódigo Capítulo11. Finalizandoojogo
ReferênciasBibliográficas
[1] EmanueleFeronato. Box2DforFlashGames . 2012.
[2] Sérgio Lopes. AW e bM o b i l e-P r o g r a m ep a r au mm u n d od em u i t o sd i s -
positivos. 2013.
[3] JohnM.Wargo. Apache Cordova 3 Programming. 2013.
[4] Tárcio Zemel.Web Design Responsivo - Páginas adaptáveis para todos os
dispositivos. 2013.
[5] ÉdersonCássio. DesenvolvaJogoscomHTML5CanvaseJavaScript.2 0 1 4 .
241