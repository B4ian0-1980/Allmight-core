---json
{
  "id": "meteor_criando_aplica__es_web_realtime_com_javascript",
  "title": "Meteor Criando aplicações web realtime com JavaScript",
  "categoria": "03-linguagens",
  "subcategoria": "java",
  "resumo": "**Arquivo Original:** `Meteor Criando aplicações web realtime com JavaScript.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "aplica",
    "com",
    "criando",
    "java",
    "javascript",
    "linguagens",
    "meteor",
    "realtime"
  ],
  "perguntas_tipo": [
    "Como utilizar Meteor Criando aplicações web realtime com JavaScript?",
    "Quais as boas praticas de java?"
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
  "dono": "stack-java",
  "prioridade": 2
}
---

# Meteor Criando aplicações web realtime com JavaScript

> **Arquivo Original:** `Meteor Criando aplicações web realtime com JavaScript.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 2

© Casa do Código
Todos os direitos reservados e protegidos pela Lei nº9.610, de
10/02/1998.
Nenhuma parte deste livro poderá ser reproduzida, nem transmitida, sem
autorização prévia por escrito da editora, sejam quais forem os meios:
fotográficos, eletrônicos, mecânicos, gravação ou quaisquer outros.
Casa do Código
Livros para o programador
Rua Vergueiro, 3185 - 8º andar
04101-300 – Vila Mariana – São Paulo – SP – Brasil

## Página 3

CasadoCódigo
Agradecimentos
Obrigado,Deus,pormaisumaconquistaemminhavida! Obrigadopaie
mãepeloamor,for çaeincentivoemtodasasetapasdecisivasdeminhavida.
Obrigadoportudoeprincipalmenteporestaraomeuladoemtodososmo-
mentos.
UmagradecimentoespecialàminhanamoradaNatáliaSantos,obrigado
peloapoio,compreensãoecompanhia,seiqueemalgunsmomentosnãofoi
fácilparanós,masoimportanteéqueconseguimosjuntos,eessavitóriaeu
dedicototalmenteparavocêeminhafamília.
Agradeçoàsra.CharlotteBentodeCarvalho,peloapoioeincentivonos
meusestudosdesdeaescolaatéaminhaformaturanafaculdade.
ObrigadoaopessoaldaeditoraCasadoCódigo,emespecialaoPauloSil-
veiraeAdrianoAlmeida.Muitoobrigadopelosuporte,apoio,pelaconfian ça
epormaisestanovaoportunidade.
ObrigadoàgaleradacomunidadeNodeBReMeteorBrasil,Os feedbacks
devocêsajudarammuitoamelhorarestelivroetambémmeulivroanterior
deNode.js.
ObrigadotambémaosleitoresdoblogmeuUndergroundWebDev(http:
//udgwebdev.com)queacompanhamecomentamospostsfrequentemente.
Porúltimo,obrigadoavocê,prezadoleitor,poradquirirmeunovolivro.
Queesteseja,umaboareferênciadeestudossobreMeteor.
i

## Página 5

CasadoCódigo
Sobre o autor
Figura1:CaioRibeiroPereira
CaioRibeiroPereiratrabalhacomoWebDevelopernaBankFacil,bacharel
emSistemasdeInformaç ãopelaUniversidadeCatólicadeSantos,suaexpe-
riênciaébaseadanodomíniodessasopadeletrinhas: Node.js,Meteor,Ja-
vascript,Ruby,Java,LevelDB,MongoDB,Redis,FilosofiaLean,Scrum,XPe
TDD.
Blogueironostemposlivres,apaixonadopordesenvolvimentodesoft-
ware,web,tecnologias,filmeseseriados.Participanteativodascomunidades:
• NodeBR:ComunidadeBrasileiradeNode.js
• MeteorBrasil:ComunidadeBrasileiradeMeteor
• DevInSantos:GrupodeDesenvolvedoresdeSoftwareemSantos
Iniciou em 2011 como palestrante nos eventos DevInSantos e Exatec,
abordandotemasatuaissobreNode.jseJavascript. CriadordoNodeWeb
iii

## Página 6

CasadoCódigo
Modules(umsitequeapresentadadosestatísticossobreosframeworksweb
paraNode.js)efundadordoGoogleGroupsMeteorBrasil.
AutordosBlogs:UndergroundWebDeveUndergroundLinux.
iv

## Página 7

CasadoCódigo
Prefácio
As mudanças do mundo web
Atualmente,oJavaScriptjáéumaop çãorealeaceitávelnodesenvolvimento
server-sideemmuitosprojetos. Issotrazcomoumadasvantagensapossi-
bilidadedeconstruirumaaplicaç ãoutilizandoapenasumaúnicalinguagem,
tantonocliente(atravésdoclássicoJavaScriptcompatívelemtodosos brow-
sers)comonoservidor(atravésdoíncrivelepoderosoNode.js!).
GraçasaoNode.js,diversosframeworkswebsurgiram—diferentedas
outraslinguagens,existemmaisde30frameworkswebparaNode.js! Não
acredita?Entãovejacomseusprópriosolhosessalistadeframeworksaces-
sandoosite:
http://nodewebmodules.com
ExpresseMeteorsãoosframeworksquemaissedestacam,ambossãofra-
meworksparaNode.jscomcaracterísticasúnicas. OExpresséconsiderado
umframeworkminimalista,focadoemcriarprojetosatravésdeestruturas
customizadaspelodesenvolvedor. ComeleépossívelcriarserviçosREST,
aplicaçõeswebtantoempadrãoMVC (Model- View-Controller)comoMVR
(Model- View-Routes)outotalmentesempadrãoemumúnicoarquivo,tudo
vaidependerdasboaspráticasaplicadaspelodesenvolvedor.Umaaplicaç ão
Expresspodeserpequenaoudegrandeporte,tudovaidependerdosrequi-
sitose,principalmente,decomovaiorganizartodoscódigosnele,afinalcom
oExpressvocêtemopoderdeaplicarsuasprópriasconven çõeseorganiza-
çõesdecódigo. Outrodetalheéquevocêutilizaseupróprioframeworkde
persistênciadedados,entãotodocontroleficaemsuasmãos.
Aprincípio,sevocêpossuiumbomconhecimentosobreoExpresseos
demaisframeworksnecessáriosparaconstruirsuaaplicaç ão,entãovocêterá
velocidadesuficienteparadesenvolverumaaplicaç ãodeformaágil. Mase
v

## Página 8

CasadoCódigo
seexistisseumframeworkNode.js,cujofocoéprototipartelasemextrema
velocidade? Tudoissoutilizandocomponentesprontosquesãofacilmente
customizáveisecomconfiguraçõescomplexassimplificadasaltonívelpara
vocêutilizar(aplicandoosprincípiosdeconven çãosobreconfiguraç ão).No
mundoRuby,issodeucertoatravésdoinovadorframeworkRails;agorate-
mosumainovaç ãosemelhantenomundoNode.js,essainovaç ãosechama
Meteor.
A quem se destina este livro?
Esselivroédestinadoaosdesenvolvedoresquetenhampelomenosco-
nhecimentosbásicosdeNode.js,Javascriptearquiteturawebcliente-servidor.
Terdomíniodessesconceitos,mesmoqueanívelbásico,seránecessáriopara
quealeiturasejadefácilentendimento.
Como devo estudar?
Estelivroépraticamenteum hands-onquevisaensinarosprincipaiscon-
ceitosdoMeteoratravésdaconstruç ãodeumaaplicaç ãowebdozero.Aode-
correrdaleituraserãoapresentadosdiversosconceitosemuitocódigopara
implementarnoprojeto,aplicarnapráticaosconceitosteóricoseaprender
boaspráticaseconven çõesdestatecnologia.
vi

## Página 9

CasadoCódigo Sumário
Sumário
1 Introdu ção 1
1.1 Conhecendoseumundo . . . . . . . . . . . . . . . . . . . . . 1
1.2 Os7princípiosdoMeteor . . . . . . . . . . . . . . . . . . . . 3
2 Configurando o ambiente de desenvolvimento 9
2.1 Detalhessobreainstalaç ão . . . . . . . . . . . . . . . . . . . . 9
2.2 Node.js . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.3 MongoDB . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
2.4 InstalandooMeteor . . . . . . . . . . . . . . . . . . . . . . . . 16
2.5 RodandooMeteor . . . . . . . . . . . . . . . . . . . . . . . . . 17
2.6 Fazendodeployparatestes . . . . . . . . . . . . . . . . . . . . 20
2.7 GerenciandopackagescomMeteorite . . . . . . . . . . . . . 21
3 Criando uma rede social real-time 23
3.1 Projetopiloto:MeteorBird . . . . . . . . . . . . . . . . . . . . 23
3.2 Funcionalidadesdaaplicaç ão . . . . . . . . . . . . . . . . . . 23
3.3 Criandooprojeto . . . . . . . . . . . . . . . . . . . . . . . . . 24
4 Implementando uma timeline de posts 27
4.1 Estruturandoostemplates . . . . . . . . . . . . . . . . . . . . 27
4.2 Criandootemplatedatimeline . . . . . . . . . . . . . . . . . 30
4.3 Publicandopostsnatimeline . . . . . . . . . . . . . . . . . . . 33
4.4 Persistindoelistandopostsemtempo-real . . . . . . . . . . . 38
vii

## Página 10

Sumário CasadoCódigo
5 Signin e Signup de usuários 41
5.1 ExplorandoAccountsdoMeteor . . . . . . . . . . . . . . . . 41
5.2 Associandopostsaumusuário . . . . . . . . . . . . . . . . . 44
5.3 Exibindotimelinesomenteparalogados . . . . . . . . . . . . 46
5.4 AutenticaçãoviacontaFacebook . . . . . . . . . . . . . . . . 49
6 Perfil do usuário 53
6.1 Criandotemplatedeperfil . . . . . . . . . . . . . . . . . . . . 53
6.2 AutocompletandoperfilviasignindoFacebook . . . . . . . . 58
7 T ela de perfil público do usuário 61
7.1 Adaptandorotasnoprojeto . . . . . . . . . . . . . . . . . . . 61
7.2 Perfilpúblicodousuário . . . . . . . . . . . . . . . . . . . . . 63
8 Follow me I will follow you 69
8.1 Introduçãosobreafuncionalidade . . . . . . . . . . . . . . . 69
8.2 CriandoosbotõesdeFolloweUnfollow . . . . . . . . . . . . 72
8.3 Contadordeseguidoresnoperfil . . . . . . . . . . . . . . . . 82
8.4 Visualizandopostdequemvocêseguir . . . . . . . . . . . . . 86
9 Publications e Subscriptions 91
9.1 OqueéPubSub? . . . . . . . . . . . . . . . . . . . . . . . . . . 91
9.2 Entendendoseumecanismo . . . . . . . . . . . . . . . . . . . 92
9.3 AdaptandooPubSubnoprojeto . . . . . . . . . . . . . . . . . 95
10 T estes, testes e mais testes 101
10.1 FrameworksdetestesparaoMeteor . . . . . . . . . . . . . . 101
10.2 PrimeirospassoscomLaika . . . . . . . . . . . . . . . . . . . 103
10.3 Criandotestes . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
10.4 Desafio:testaromodeloPost . . . . . . . . . . . . . . . . . . . 109
11 Integraç ão contínua no Meteor 111
11.1 RodandoMeteornoTravis-CI . . . . . . . . . . . . . . . . . . 112
viii

## Página 11

CasadoCódigo Sumário
12 Preparando para produ ção 117
12.1 Monitorandoaaplicaçãoatravésdelogs . . . . . . . . . . . . 118
12.2 Habilitandocacheemarquivosestáticos . . . . . . . . . . . . 122
12.3 UtilizandooFastRender . . . . . . . . . . . . . . . . . . . . . 123
12.4 OtimizandoconsultasnoMongoDBcomFind-Faster . . . . 125
12.5 Configurandovariáveisdeambiente . . . . . . . . . . . . . . 126
13 Hospedando uma aplicaç ão Meteor 131
13.1 ConvertendoMeteorparaNode.jscomDemeteorizer . . . . 132
13.2 Ondehospedarumaaplicaç ãoMeteor? . . . . . . . . . . . . . 133
14 Como organizar um projeto Meteor 139
14.1 Convençõesdediretóriosearquivos . . . . . . . . . . . . . . 139
15 Continuando os estudos 143
Versão:17.2.5
ix

## Página 13

Capítulo1
Introdução
1.1 C onhecendo seu mundo
OMeteoréumframeworkwebfull-stack100%JavaScript,ouseja,comele
vocêvaiconstruiraplicaçõesprogramandoemtodasascamadas:cliente,ser-
vidorebancodedados,usandoJavaScript,Node.jseMongoDB,tudoisso
utilizandoapenasumaúnicalinguagemdeprogramaç ão,oJavaScript.
Outrodetalheimportanteéqueofocodesseframeworkéaprototipagem
rápida,fazendocomquetrabalhosquelevariammesessejamrealizadosem
semanas,ouatémesmoalgunsdias.Issoépossívelgraç asaosseusrecursos
quevisamautomatizartarefasrepetitivas,exibirrespostasimediatasnobrow-
ser,diversasconven ções,várioscomponentescustomizáveisprontosparauso
etambémasconfiguraçõescomplexasdebaixonívelqueestãosimplifica-
dasparaodesenvolvedor.Por default,suasaplicaçõesMeteorserãoemfor-
mato single-page real-time,mastambémépossívelcriaraplicações multi-page

## Página 14

1.1. Conhecendoseumundo CasadoCódigo
orientadoarotas.Esteframeworkéconsideradocomoum MVVM (Model-
View View-Model),ouseja,nãoexiste controllersou routespordefault,masé
customizá-locomopropósitodeadicionar controllers,routeseoutros patterns
atravésdainclusão packages third-party.
OMeteoréumaplataformadedesenvolvimentocompleta,sendoqueo
mecanismoprincipalresponsávelportodamagia back-endéoNode.js.As-
simcomooNode.jspossuiseugerenciadordemódulos—oNPM(Node
Package Manager),oMeteorpossuioseuprópriogerenciadorde packages
(sim,módulosepackagessãoamesmacoisa,ouseja,sãoframeworks),que
sechama Atmosphere.Estepermiteusarprojetos third-partycriadospelaco-
munidade,semcontarquetambémépossívelutilizaramaioria—masnão
todos—dosmódulosNPMdentrodeumaaplicaç ãoMeteor(algoqueserá
explicadonoscapítulosfuturos). Issopodeevitara“invençãodaroda”,po-
rémtudovaidependerdacompatibilidadedetalmóduloNodenocontexto
doMeteor.
TrabalharcomMeteorétrabalharcomJavaScript,eissofazcomquemui-
tosdesenvolvedorestenhamumacurvadeaprendizadorápida,eempoucos
diasdeestudosvocêterádominadoosprincipaispontoseaspectosdestefra-
mework.SevocênãoconheceNode.jsmasdominaJavaScript,nãotenhare-
ceiodeleresselivro,poispoucascoisassobreNode.jsserãoabordadasaqui.
Esteéumframeworkdemuitosrecursos,ouseja,constituídoporum
conjuntodeframeworksdomundoNode.jseJavaScript.Algumasbibliotecas
conhecidasquefazempartedelesão:
• SockJS—frameworkemuladordeWebSocketseresponsávelpelofun-
cionamentodoprotocoloDDP(Data Distribution Protocol ).
• MongoDB—bancodedadosdefault.
• Handlebars—templateengine.
• PubSub—bibliotecadeemissãoeescutadeeventosviapattern: pu-
blisher / subscriber.
• MiniMongo—APIclient-sidequepossuiamaioriadasfuncionalidades
doMongoDB.
2

## Página 15

CasadoCódigo Capítulo1. Introdução
• Connect—móduloNode.jscomfuncionalidadesparatrabalharcom
protocoloHTTP.
Essessãoalgunsframeworksinternosquesãoessenciaisparadarvidaao
Meteor.
1.2 O s 7 princípios doMeteor
OMeteoréumframeworktotalmenteinovador,eleenglobadiversasboas
práticasdeframeworkscomoRailsdoRuby,DjangodoPython,Expressdo
Node.js,alémdaprópriaequipeadotarsuasprópriasconven ções.Tudoisso
surgiubaseadoem7princípios,eelessão:
1 Data on the wire
Figura1.1:HandlebarséotemplateenginedoMeteor.
NãoenvieHTMLpelaredeesimapenasdados,deixandoqueocliente
3

## Página 16

1.2. Os7princípiosdoMeteor CasadoCódigo
decidacomoapresentá-los.
2 One language
Figura1.2:Node.js,JavascripteMongoDB.
EscrevacódigoJavaScriptemtodasascamadas:cliente,servidorebanco
dedados.Issosimplificaeagilizaodesenvolvimento,alémdegarantiruma
curvadeaprendizadobaixa.
3 Database anywhere
Figura1.3:Bancodedadoscompartilhadoentreclienteeservidor.
UtilizeumaAPIdeinterfaceúnicaetransparentequelhepermiteacessar
obancodedadostantonoclientecomonoservidor.
4

## Página 17

CasadoCódigo Capítulo1. Introdução
4 Latency compensation
Figura1.4:Latênciazeroaoacessardadosviacliente.
Noclienteéusado prefetchinge model simulationnaAPIclient-sidedo
bancodedadosparaatingirlatênciazeronoacessodeseusrecursos.
5 Full-Stack Reactivity
Figura1.5:Meteoréumframeworkfull-stackreal-time.
Pordefaulttudofuncionaem real-time.Etodasascamadasdaaplicaç ão
adotamoparadigmaorientadoaeventos,queéherdadodoNode.js.
5

## Página 18

1.2. Os7princípiosdoMeteor CasadoCódigo
6 Embrace the ecosystem
Figura1.6:Meteorémaisumainiciativaopen-source.
Totalmenteopen-source,oMeteorpossuisuasconven çõespelasquais
agreganovosconceitosevalores,emvezdeserumaferramentaquesubs-
tituiráoutrosframeworks.
6

## Página 19

CasadoCódigo Capítulo1. Introdução
7 Simplicity equals Productivity
Figura1.7:AumentesuaprodutividadetrabalhandocomMeteor!
Sejaprodutivo! Desenvolvademais featuresdeformarápidaesimpli-
ficada. OMeteormantémumconjuntodeAPIsfáceisdeimplementarea
comunidadeMeteorestásemprecolaborandoparaevoluç ãodoframework.
7

## Página 21

Capítulo2
Configurandooambientede
desenvolvimento
2.1 D etalhes sobre a instalação
ParainstalaroMeteor,primeirotemosqueteroNode.jseMongoDBinstala-
dos.Nestase çãoexplicareicomoinstalareconfiguraroambientededesen-
volvimentodecadadependênciadoMeteor.
2.2 N ode.js
Instalação
ParaconfiguraroambienteNode.js,independentedequalsistemaoperaci-
onalvocêutilizar,asdicasserãoasmesmas. Éclaroqueosprocedimentos

## Página 22

2.2. Node.js CasadoCódigo
serãodiferentesparacadasistema(principalmenteparaoWindows,masnão
seránadagrave).
Figura2.1:PáginadeDownloaddoNode.js.
Instalando Node.js:primeiropasso,acesseositeoficial:(http://nodejs.
org)ecliqueem Download. ParausuáriosdoWindowseMacOSX,basta
baixarosseusinstaladoreseexecutá-losnormalmente.Paraquemjáutiliza
Linuxcom Package Managerinstalado,acesseesselink(https://github.com/
joyent/node/wiki/Installing-Node.js-via-package-manager),queéreferente
àsinstruçõessobrecomoinstalá-loemdiferentessistemas.InstaleoNode.js
deacordocomseusistemae,casonãoocorraproblemas,bastaabriroseu
terminalconsoleoupromptdecomandoedigitarocomando: node -v
&& npm -vparaverasrespectivasversõesdoNode.jseNPM(Node Package
Manager)queforaminstaladas.
10

## Página 23

CasadoCódigo Capítulo2. Configurandooambientededesenvolvimento
Figura2.2:VersãodoNode.jseNPMutilizadanestelivro.
Aúltimaversãoestávelutilizadanestelivroé Node 0.10.26,juntodo
NPM 1.4.3.
A importância de instalar versões recentes do Node.js
É altamente recomendável utilizar uma versão igual ou superior
à v0.10.22,poisrecentementeforamidentificadasalgumasvulnerabi-
lidades que permitiam ataqueDoSvia HTTP em versões anteriores.
Veja mais detalhes no blog oficial:http://blog.nodejs.org/2013/10/22/
cve-2013-4450-http-server-pipeline-flood-dos
Configuração do ambiente
Para configurá-lo, basta adicionar uma variável de ambiente, o
NODE_ENVcomvalor“development”.EmsistemasLinuxouOSX,bastaaces-
saroarquivo .bash_profileou .bashrccomumeditordetextoqual-
quer,emmodosuperuser (sudo),eadicionaroseguintecomando: export
NODE_ENV=’development’.
NoWindows7,oprocessoéumpoucodiferente.
11

## Página 24

2.2. Node.js CasadoCódigo
Figura2.3:ConfigurandoavariávelNODE_ENVnoWindows7.
Clique com botão direito no íconeMeu Computador e selecione
a opção Propriedades. No lado esquerdo da janela, clique no link
Configurações avançadas do sistema. Najanelaseguinte,acessea
aba Avançadoecliquenobotão Variáveis de Ambiente...;agora
nocampo Variáveis do sistemacliquenobotão Novo...,em“nome
davariável”digiteNODE_ENVeemvalordavariável”digitedevelopment.
Apósfinalizaressatarefa,reinicieseucomputadorparacarregaressavariável
nosistemaoperacional.
Rodando o Node.js
Paratestarmosoambiente, executaremosonossoprimeiroprograma
Hello World. Executeocomando: nodeparaacessarmosseumodoREPL
(Read-Eval-Print-Loop),quepermiteexecutarcódigoJavaScriptdiretamente
noterminal.Digite console.log("Hello World");etecle ENTERpara
executá-lonahora.
12

## Página 25

CasadoCódigo Capítulo2. Configurandooambientededesenvolvimento
Figura2.4:HelloWorldviaREPLdoNode.js
2.3 M ongoDB
Instalação
ComNode.jsfuncionando,faltainstalarmaisumadependênciaimportante
doMeteor,oMongoDB.Nãohásegredosparainstalá-lo,tantoéqueutilizare-
mossuasconfiguraçõespadrõesdeambiente development.Vamoslá!Acesse
estelink: http://www.mongodb.org/downloadsefaçaodownloaddoMon-
goDBcompatívelcomseusistemaoperacional.
13

## Página 26

2.3. MongoDB CasadoCódigo
Figura2.5:PáginadedownloaddoMongoDB.
Nestelivro,utilizaremossuaúltimaversãoestável: 2.4.8. OMongoDB
seráinstaladoviaHomeBrew(http://mxcl.github.com/homebrew),queéum
gerenciadordepacotesparaMac.Parainstalá-loexecuteoscomandosase-
guir:
brew update
brew install mongodb
SevocêestivernoLinuxUbuntu,teráumpoucomaisdetrabalho,porém
épossívelinstalá-loviacomandoapt-get.Primeiroemmodo sudo(super
usuário),editeoarquivo /etc/apt/sources.list.d/mongodb.list,
adicionandonofinaldoarquivoocomando:
deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart
dist 10gen
Salve-oeexecuteospróximoscomandos:
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80
--recv 7F0CEB10
14

## Página 27

CasadoCódigo Capítulo2. Configurandooambientededesenvolvimento
sudo apt-get update
sudo apt-get install mongodb-10gen
JánoWindows,oprocessoétãomaistrabalhosoquenemapresentarei
nestelivro...brincadeira! InstalarnoWindowstambéméfácil,apenasbaixe
oMongoDB,crieaspastas C:\data\dbe C:\mongodb,edescompacteo
conteúdodoarquivo zipdoMongoDBdentrode C:\mongodb.
Sistema operacional utilizado neste livro
Todososframeworksapresentadosnestelivroserãotrabalhadosem
umsistemaMacOSXda Apple,massinta-seàvontadeparatrabalharem
outrossistemascomoLinuxouUnix.SomentenoWindowsvocêsofrerá
algunsproblemasmas,aindanesteanode2014,serálan çadaumaversão
comváriasotimizaçõesqueirãocompatibilizarcomWindows.
Configuração do ambiente
ParaexecutaroMongoDB,precisamosconfigurá-locomoserviçonosis-
tema.Paraisso,abraoterminaloupromptdecomandoesigaasinstruçõesa
seguirdeacordocomseusistemaoperacional:
•MacOSX:jávemconfiguradocomoserviçoatravésdohomebrew.
•Linux Ubuntu:jávemconfiguradocomoserviçoatravésdoapt-get.
•Windows:acesseesselink http://docs.mongodb.org/manual/tutorial/
install-mongodb-on-windowsesigapassoapassoparaconfigurá-lo
corretamentenoWindows,poishávariaçõesdeconfiguraç ãoentre
uma versão 32bits e 64bits do Windows.
Rodando o MongoDB
AgoraquetemosoMongoDBconfigurado,podemosusarseuscomandos
noterminal.
ParaacessarseuCLI,executeocomando: mongo
15

## Página 28

2.4. InstalandooMeteor CasadoCódigo
OMongoDBcria databasesdeformadinâmica,ouseja,aousaroco-
mando use nome_do_database,automaticamenteelecriaumnovoou
acessaumexistentedatabase.Omesmoconceitoéaplicadoemsuas collecti-
onseatributosdesuascollections.
Façaotestevocêmesmo!Executeessasequênciadecomandos:
use db_test;
db.users.insert({nome: "MongoDB", version: "2.4.8"});
db.users.insert({nome: "CouchDB", version: "1.5.0"});
db.users.insert({nome: "LevelDB", version: "1.1"});
db.users.insert({nome: "MariaDB", version: "10.0.7"});
db.users.find();
2.4 I nstalando o Meteor
Agoravamosaoqueinteressa! InstalareconfiguraroMeteoremsuamá-
quina.AversãodoMeteorusadanestelivroéa 0.8.0.
Instalação em ambiente Mac/Unix/Linux
InstalaroMeteorésupersimples,apenasexecute:
curl https://install.meteor.com | /bin/sh
Instalação em ambiente Windows
SomentenoWindowsexistemalgumasbarreirasparainstalaroMeteor,
mastudoissoseráresolvidonafutura versão 1.0.0. Enquantoisso,reco-
mendoquevocêinstaleumamáquinavirtualrodandoLinuxesigaasins-
truçõesdeinstalaç ãoanteriorparaprosseguirnolivro.
16

## Página 29

CasadoCódigo Capítulo2. Configurandooambientededesenvolvimento
Figura2.6:VersãodoMeteorusadanestelivro
2.5 Rodando o Meteor
Quetalcriarmosnossoappdeteste? Paramostraroquãofáciléfazeresta
magia,apenasexecuteesses3comandos:
meteor create meu-app-teste
cd meu-app-teste
meteor
Pordefault, oMeteorcriaumaplicativode“HelloWorld”semane-
cessidade de você codificá-lo. Seu comandoscaffoldgerou 3 arquivos (1
html, 1 css e 1 js) com o mesmo nomemeu-app-teste. O arquivo
meu-app-teste.htmlveiocomoseguintecódigo:
<head>
<title>meu-app-teste</title>
</head>
<body>
{{> hello}}
</body>
17

## Página 30

2.5. RodandooMeteor CasadoCódigo
<template name="hello">
<h1>Hello World!</h1>
{{greeting}}
<input type="button" value="Click" />
</template>
Reparenatag <template name="hello">: éumatagespecialdo
Handlebars,cujoconteúdoédinamicamenteinjetadodentrodatag <body>
atravésdamarcação {{> hello}}.Casovocêexcluaessamarcaç ão,otem-
platenãoserárenderizado. Querfazerumteste? Primeiroacesseemseu
browseroendere çohttp://localhost:3000. Agoraexcluaamarcaç ão {{>
hello}}. Repareque,instantaneamente,oMeteoratualizouoHTMLno
browser, afinalelepossuiomecanismomuitoprodutivo, conhecidopelo
nomede Hot-Pushes. Elefaz auto-reloadnonavegadoraoalterarqualquer
códigodoprojeto. Aotrabalharcom CSS,vocênahorarealizaasmudan-
çasdolayout,comoporexemplo,editeo meu-app-teste.cssinserindo
oconteúdoaseguir:
body {
margin: 0 auto;
text-align: center;
}
h1 {
font-size: 4em;
}
Parafinalizar,temostambémo meu-app-teste.js,umcódigoque
utilizafun çõesdeclienteeservidor.Nelecolocamoscódigosaseremexecu-
tadonoclientedentrodacondicional Meteor.isClient,eoquetiverque
serexecutadonoservidorcolocamosdentrode Meteor.isServer. Um
detalheimportanteéquetodososcódigosqueestiveremforadessasduas
condicionaisserãocarregadosemambascamadas.Pordefault,Meteorgerou
oseguintecódigoJavaScript:
if (Meteor.isClient) {
Template.hello.greeting = function () {
return "Welcome to meu-app-teste.";
18

## Página 31

CasadoCódigo Capítulo2. Configurandooambientededesenvolvimento
};
Template.hello.events({
’click input’ : function () {
// template data, if any, is available in ’this’
if (typeof console !== ’undefined’)
console.log("You pressed the button");
}
});
}
if (Meteor.isServer) {
Meteor.startup(function () {
// code to run on server at startup
});
}
Dentro de Meteor.isClient temos uma declaração da função
Template.hello.greeting, referente ao {{greeting}} que está
dentrodatag <template name="hello">. Estaéumadasconven ções
do Meteor em que você deve declarar funções para templates utilizando
a convenção Template.nome_do_template.nome_da_marcação.
Outro código importante no cliente foi a criação de eventos para
o mesmo template. Você sempre trabalhará com eventos de
forma imperativa no Meteor, semelhante ao framework Backbone
(http://backbonejs.org) . Para criar um evento, basta seguir a conven-
ção Template.nome_do_template.events e declarar um hash de
eventos,cujachaveéuma stringreferenteao“eventoseletor”eovaloréuma
funçãoJavaScript.
Em Meteor.isServer,temosafun çãoprincipaldestartupdoprojeto,
o Meteor.startup,cujocallbacknãopossuicódigo.Essafun çãotambém
possuiomesmocomportamentoaoserdeclaradanoladodocliente.Vamos
vero Meteor.startupemação?Editeo meu-app-teste.jsefaçaas
seguintesalterações:
if (Meteor.isClient) {
Meteor.startup(function () {
19

## Página 32

2.6. Fazendodeployparatestes CasadoCódigo
alert("Iniciando Cliente Meteor.");
});
Template.hello.greeting = function () {
return "Welcome to meu-app-teste.";
};
Template.hello.events({
’click input’ : function () {
// template data, if any, is available in ’this’
if (typeof console !== ’undefined’)
console.log("You pressed the button");
}
});
}
if (Meteor.isServer) {
Meteor.startup(function () {
console.log("Iniciando Servidor Meteor.");
});
}
Eviuasnovasmensagensgeradasnoservidorecliente?Senãofuncionou,
atualizeseubrowser.
De qualquer forma, temos um grande problema ao trabalhar com
essa estrutura gerada pelo Meteor. Dificilmente um projeto grande so-
breviveria mantendo todo seucore dentro de um único arquivo.js,
mesmoutilizandoinúmerasvezesasvariáveisglobais Meteor.isClient
e Meteor.isServer.Comocrescimentodoprojeto,éextremamenteim-
portantemanterorganizadaeescalávelsuaestruturadepastasecódigos.Mas
fiquetranquilo,nopróximocapítuloestemistérioserádesvendado!
2.6 F azendo deploy para testes
Sevocêéumdesenvolvedorquecurtepublicarcomfrequêncianovosup-
datesdaaplicaç ãoemumambiente betaou staging,oMeteordisponibiliza
gratuitamenteumamáquinanasnuvensparafazer deployemsubdomíniodo
20

## Página 33

CasadoCódigo Capítulo2. Configurandooambientededesenvolvimento
aplicacao.meteor.com. Estaéumamáquinacomconfiguraç ãofraca,
usadaapenasparatestarsuaaplicaç ãoouparapublicarsistemasdepequeno
porte.ElajávemcomNode.js,MongoDBe,principalmente,oMeteor.Nos
capítulosfuturosfalareiemmaisdetalhessobre deployingemambientesde
produção,masporenquantoexplicareiapenascomofazerno meteor.com.
Sigaoscomandos:
meteor deploy meu-app-teste --password=senha123
Obs.: Caso você não consiga fazer deploy com o nome:
meu-app-teste, tente um outro nome qualquer, pois provavelmente
oprimeiroleitordestelivrojárodouestecomandoeconseguiuregistrar-se
comessenome.
Tambémépermitido,nesteambiente,fazerredirecionamentodeDNS
paraoseuprópriodomínio. Paraisso,apenasconfigureseuserviçoDNS
apontandoum CNAMEpara origin.meteor.com.Emseguida,faç aode-
ploydoseuprojetoutilizandooseudomínio:
meteor deploy www.meuapp.com --password=senha123
2.7 G erenciando packages com Meteorite
Comoadicional,instalaremosoMeteorite,afinalnodecorrerdestelivrouti-
lizaremos packages third-partyquesãohospedadosnoAtmosphere.Nãouti-
lizaremosocomando meteoresimo mrtdoMeteoritequealémdepossuir
seuscomandosespecíficostambémexecutatodososcomandosdoMeteor.
Como funciona o Meteorite?
OMeteoritepossuiumcomportamentomuitoparecidocomoGemsdo
RubyeoNPMdoNode.js.Asinstalaçõesdospacotessãogerenciadasatravés
doarquivo smart.json,queécriadonaraizdoprojeto.Tambémécriado
o smart.lock,responsávelpormanterinformaçõessobreasatuaisversões
decadadependênciadoseuprojeto,bemcomoaversãoatualdoMeteor.Ao
apagaressearquivo,vocêfor çaoMeteoriteareinstalartudo(dependênciase
aúltimaversãodoMeteor),quandovocêexecutar,napróximavez,umdesses
comandos: mrt, mrt installou mrt update.
21

## Página 34

2.7. GerenciandopackagescomMeteorite CasadoCódigo
Comoreceitadebolo,vejaaseguirosprincipaiscomandosdoMeteorite:
•mrt—éumaliasdocomandometeor;suaúnicadiferen çaéque,antes
deiniciaroservidor,eleinstalaouatualizatodasasdependênciasdo
projeto.
•mrt create nome-do-app—étambémumaliasdocomandome-
teorcreate,cujodiferencialéqueelecriaoarquivo smart.json,o
qualexplicareinofinaldestecapítulo.
•mrt add nome-do-package—éumaliasdocomandometeoradd;
suadiferen çaéqueeleinstalaospacotesatravésdoAtmosphere. Ele
tambémcriaemantématualizadooarquivo smart.json,queseen-
contranodiretórioraizdoprojeto.
•mrt add nome-do-package --version 0.0.1 — instala um
pacotedeumaespecíficaversão.
•mrt install — instala todos pacotes que estão listado no
smart.json.
•mrt update—atualizaaversãodometeoredetodosospacotesdo
projeto.
Oarquivo smart.json,alémdemanterospackagesdependentesdo
projeto,tambéméumdescritordopróprioprojeto,oqualeleconsideracomo
umpackage.Vejaaseguiraestruturabásicadeumarquivo smart.json:
{
"name": "nome-do-projeto",
"description": "Descrição do projeto",
"author": "Usuário <usuario@mail.com>",
"version": "0.0.1",
"packages": {
"nome-do-package-1": {},
"nome-do-package-2": {}
}
}
22

## Página 35

Capítulo3
Criandoumaredesocial
real-time
3.1 P rojeto piloto: MeteorB ird
AgoraquetemosoambienteMeteorinstaladoefuncionandocorretamente,
vamoscriarnossoprojetopiloto,comoqual,nodecorrerdestelivro,explo-
raremososprincipaisrecursosdoMeteor,bemcomoexplicaremosdiversos
tópicoseconceitos.Oprojetoquevamoscriarseráumredesocial,umaver-
sãosimplificadadoTwitter(http://twitter.com),quechamaremosde Mete-
orBird.
3.2 F uncionalidades da aplicação
Nesteprojeto,implementaremosasseguintes features:

## Página 36

3.3. Criandooprojeto CasadoCódigo
• Atualizaçõesdatimelineemreal-time;
• Sign-upatravésdee-mailesenha;
• Sign-upatravésdeumacontanoFacebook;
• Acessarperfildeumusuário;
•Followe unfollowdepostsdeumusuário;
Sobre o código-fonte deste projeto
Casoqueirafazerum test-driveantes,pararodá-loemsuamáquina
vendonapráticacomofunciona,faç aodownloadocódigo-fonteatravés
domeugithubpessoal:
https://github.com/caio-ribeiro-pereira/meteor-bird
3.3 C riando o projeto
Nestase çãovamoscriaraestruturadesseprojeto,istoé,comoaestruturado
Meteoréflexívelemrelaçãoaosdiretórioschaves,listareinasequênciaquais
diretóriosserãoutilizadoseexploradosnodecorrerdestelivro.
Antesdecome çarmosisso,primeirovamoscriaroprojeto. Executeos
comandosaseguirparacriaroprojetoeexcluirosarquivosgerados:
mrt create meteor-bird
cd meteor-bird
rm meteor-bird.*
Agoracrieosseguintesdiretórios,osquaisexploraremosnoscapítulos
seguintes:
•client—diretóriodecódigosclient-side;
•server—diretóriodecódigosserver-side;
•models—diretóriodemodeloscompartilhadosentreclienteeservi-
dor,elessãoas collectionsdoMongoDB;
24

## Página 37

CasadoCódigo Capítulo3. Criandoumaredesocialreal-time
•public/resources—diretórioparaincluirarquivosestáticos(utilizare-
mosparaservirimagens);
•test—diretóriopararodartestesnaaplicaç ão.
Éclaroquenodecorrerdocaminhocriaremosalgunssubdiretórios,mas
comessaestruturainicialserámaisfácilseguirestelivrocomumano ção
básicasobreasconven çõesdecadaumdessesdiretórios.
Antesdecome çaroprojeto,utilizaremoso Twitter Bootstrap 3(http:
//getbootstrap.com)comoframeworkCSSparanosauxiliarnodesenvolvi-
mentodasinterfacedaaplicaç ão.OmaisbacanaéqueoMeteorjápossuium
packagechamado bootstrap-3prontoparauso,eparainstalá-lobastaro-
daroseguintecomando:
mrt add bootstrap-3
Agora que adicionamos nosso primeiro package, surgiu o arquivo
smart.jsonnaraízdoprojeto. Paradeixá-lomaisdescritivo,vamosadi-
cionaralgumasinformaçõessobreoprojetoMeteorBird.Paraisso,editeesse
arquivocombasenoseguinteconteúdo:
{
"name": "meteor-bird",
"description": "Meteor Bird Social Network",
"author": "Caio R. Pereira <caio.ribeiro.pereira@gmail.com>",
"version": "0.0.1",
"packages": {
"bootstrap-3": {}
}
}
Obs.:Mudeonomedocampo authorparaoseunomeee-mail.
Tambémcriaremosumsimplesarquivo cssqueirádefinirumacor
deplanodefundotamanhorealdo containerdaaplicação. Crieoarquivo
client/stylesheets/application.css,incluaeestilizeoselementos
aseguir:
25

## Página 38

3.3. Criandooprojeto CasadoCódigo
body {
background-color: #EFEFEF;
}
.container {
background-color: #FFF;
width: 780px;
}
Comissojátemosumaconjuntodeestilosparaconstruirpáginasbonitas
eamigáveisnaaplicação.
Nãoparedelerestelivro! Nopróximocapítulobotaremosasmãosna
massa!
26

## Página 39

Capítulo4
Implementandoumatimelinede
posts
4.1 E struturando os templates
Começandoodesenvolvimentodanossaredesocial,vamoscriarosprin-
cipais templates da aplicação: cabe çalho e rodapé. Todos os templa-
tes serão criados na pastaclient/views, mas somente o template
principal fica dentro da pastaclient e ele deve ser chamado de
client/index.html. Vamoscomeçarcriandoocabe çalhodapáginano
template client/views/header.html:
<template name="header">
<header class="container">
<nav class="navbar navbar-default">

## Página 40

4.1. Estruturandoostemplates CasadoCódigo
<div class="navbar-header">
<a class="navbar-brand">Meteor Bird</a>
</div>
</nav>
</header>
</template>
Emseguida,vamoscriarorodapéem client/views/footer.html:
<template name="footer">
<footer class="container">
<hr>
<p class="text-center">
<small>Meteor Bird</small>
</p>
</footer>
</template>
Combasenessesdoistemplates,jámontamosaestruturabásicadolayout.
Quetaltestar?LevanteoservidorMeteorrodandoocomando mrteacesse
http://localhost:3000paraverosresultados.
28

## Página 41

CasadoCódigo Capítulo4. Implementandoumatimelinedeposts
Figura4.1:Porqueapáginaestáembranco?
Masoquehouve? Porquenãoapareceunada? Cadêocabe çalhoero-
dapé?Calma!Esquecideexplicarumpequenodetalhe:pordefault,oHTML
nãorenderizaatag <template>equemtrabalhacomtodoconteúdodos
templatenoMeteoréoHandlebars. Eleo T emplate Engineresponsávelpor
injetaroconteúdodeumtemplatedentrodoHTMLprincipal(alémdeter
outrasfuncionalidadesfocadasemmanipularconteúdodinâmicoemuma
páginaHTML).
OMeteorabstraitodocódigoJavaScriptreferenteàsfun çõesdoHandle-
barsalémdeoutrasfun çõesdemanipulaç ãodeviewsatravésdorecentefra-
meworkintroduzidonaversão 0.8.x,chamadoBlaze.
https://github.com/meteor/meteor/wiki/Using-Blaze
GraçasaoBlazevocênãovaiprecisarcompilarumtemplateechamarfun-
çõescomplexaspararenderizá-lo,vocêapenasvaicriarostemplatenoprojeto
echamá-loondequiseratravésdamarcaç ão {{> nome_do_template}}.
IncluirumtemplatedentrodoHTMLprincipalémuitosimples,vejacomo
incluiremosocabe çalhoerodapéeditandoo client/index.html:
29

## Página 42

4.2. Criandootemplatedatimeline CasadoCódigo
<head>
<title>Meteor Bird</title>
</head>
<body>
{{> header}}
{{> footer}}
</body>
Figura4.2:Cabe çalhoerodapénapáginaprincipal
4.2 C riando o template da timeline
Nestase ção,vamoscriaratimelinedeposts,queseráaprimeira featuredo
projeto.Atimelinedevemostrarpostsdoprópriousuárioeprincipalmente
postsdeseusseguidores,porém focaremos no momento em apenas exibir
os posts do próprio usuário.Faremosestaimplementaçãoemduasetapas,a
primeiraserásomenteumarenderizaç ãosimplesdatimelinecomdados fa-
kes,paraprototiparseulayout.Nodecorrerdoscapítulos,implementaremos
ocódigofinaldessafuncionalidade.
30

## Página 43

CasadoCódigo Capítulo4. Implementandoumatimelinedeposts
Crieodiretório client/lib/helpers.Esteseráumdiretóriode hel-
pers,atravésdoqualcriaremosfun çõescomregrasdenegóciofocadasem
apresentaralgona viewdocliente. Nele,podemosutilizarfun çõesdascol-
lections,outrasestruturasdedadosouatémesmobibliotecasexternas. O
objetivodeumhelpernoMeteorédecriarfun çõesqueretornemresultados
apresentáveisnasviews.
Vamoscriarnossa timeline fake? Dentrode client/lib/helpers,
crieoarquivo timeline.js,comoseguintecódigo:
Template.timeline.helpers({
posts: function() {
return [
{message: "Ola!"},
{message: "tudo bem?"}
];
}
});
Agora,paraalcan çaroresultado,temosquecriarotemplatedatimeline.
Crieaview client/views/home/timeline.htmlcomotemplatease-
guir:
<template name="timeline">
<div class="row">
<fieldset class="col-sm-12">
<legend>últimos posts</legend>
{{#each posts}}
<blockquote class="lead">
<small>{{message}}</small>
</blockquote>
<hr>
{{else}}
<p class="lead text-center">
Nenhum post publicado.
</p>
{{/each}}
</fieldset>
</div>
</template>
31

## Página 44

4.2. Criandootemplatedatimeline CasadoCódigo
Repare nas convenções de namespace do Meteor. Criamos
o helper timeline.js, cujo código segue com o namespace
Template.timeline.helpers. Ele permite registrar funções hel-
persparaotemplate timeline. Criamosumafun çãochamada posts,
cujoobjetivoéretornarumarraydeobjetosreferentesaosdadosdeum
post. Apenasseguindoasconven çõesdenomesjáestamosaptosacriar
um template que renderize essa função helper. Basta apenas criar a tag
<template name="timeline"> e, internamente, utilizar sintaxe do
Handlebars que permite rodar um loop do array retornado pelo helper
posts,utilizandoamarcaç ão {{#each posts}}.
SevocêdeixouseuservidorMeteorrodando,reparequenadaaconte-
ceunobrowser.Issoocorreporquenãoadicionamosessetemplatenaview(
client/index.html),entãoadicioneoseguinteconteúdo:
<head>
<title>Meteor Bird</title>
</head>
<body>
{{> header}}
<main class="container">
<section class="col-sm-12">
{{> timeline}}
</section>
</main>
{{> footer}}
</body>
Agoraacessenovamenteobrowser,ou,seocorreralgumproblema,rei-
nicieoservidorteclandonoterminal CTRL+C(noLinuxouWindows)ou
Control+C(noMacOSX).Emseguida,executeocomando mrtevejao
resultado:
32

## Página 45

CasadoCódigo Capítulo4. Implementandoumatimelinedeposts
Figura4.3:Timelineestática.
4.3 P ublicando posts na timeline
Essatimelineestáestática,quetalcriarmosumacaixadetextopermitindo
queousuáriopubliqueseusprópriosposts? Paraisso,utilizaremosumre-
cursodoMeteor,quesechama Session.
Diferente das sessions convencionais de outras linguagens, uma
SessiondoMeteornãoarmazenadadosnamemóriadoservidor,esimno
cliente.Issofazcomqueumsimples refreshnobrowserlimpetodososdados
docliente.Outrodetalheimportanteéquea Sessionutilizainternamente
o pattern reactive,oprincipal patternutilizadoemmuitasclassesnativasdo
Meteor. Suautilidadeéfazer re-computation,ouseja,umobjetoqueadota
essepatterntemaproatividadedereexecutarsuasfun çõesdesaídatodavez
queoestadodeseusatributossofreralterações.
Por exemplo, o próprio objetoSession possui a função de saída
get(chave),ecomoentrada,elepossuiafun ção set(chave, valor).
33

## Página 46

4.3. Publicandopostsnatimeline CasadoCódigo
Todosospontosdaaplicaç ãoemquevocêutilizar Session.get("X")se-
rãoreexecutadostodavezqueumoutropontodaaplicaç ãoalterarovalorde
"X"executandoafun ção Session.set("X", "novo valor").NoMe-
teor,ascollectionsdoMongoDBadotamessepatternereexecutamsempre
queumacollectionmudadeestado,bemcomoquandoamesmaéexcluída
dobanco.
Essepattern,comoopróprionomediz,fazcomquesuasfun çõestraba-
lhemdeformareativa,ouseja,semudoualgointerno,reexecutesuafun ção
desaídareferenteaoatributoalterado.Noquesitoprodutividade,issoevita
quenós,programadores,implementemosessasrotinasdemudan çadeestado
deumobjeto,diminuindoincrivelmentemuitaslinhasdecódigo.
Voltando ao nosso projeto, vamos aplicar o conceito de programa-
çãoreativaatravésdaimplementaç ãodacaixadeposts. Primeiroediteo
client/lib/helpers/timeline.js:
Template.timeline.helpers({
posts: function() {
return Session.get("posts");
}
});
Comisso,jádeixamosnossatimelinepreparadapararetornarosposts
diretodeuma Session. Agoratemosquecriaroformulárioqueper-
mitepublicarposts—esteseráumnovotemplatequeincluiremosnaview
principal (client/index.html). Mas antes, vamos criar o template
client/views/home/post.htmlcomoformulárioquesegue:
<template name="post">
<div class="row">
<div class="col-sm-12">
<form class="form-horizontal">
<fieldset>
<legend>novo post</legend>
<div class="row">
<div class="col-sm-9">
<textarea rows="2"
class="form-control">
34

## Página 47

CasadoCódigo Capítulo4. Implementandoumatimelinedeposts
</textarea>
</div>
<div class="col-sm-1">
<button class="btn btn-lg">
Publicar
</button>
</div>
</div>
</fieldset>
</form>
</div>
</div>
</template>
Em seguida, vamos adicioná-lo na view principal, editando o
client/index.html:
<head>
<title>Meteor Bird</title>
</head>
<body>
{{> header}}
<main class="container">
<section class="col-sm-12">
{{> post}}
{{> timeline}}
</section>
</main>
{{> footer}}
</body>
Parafinalizaressafeature,criaremosum listennoevento submitdofor-
mulário,paraquecaptureamensagemdopostearmazene-aemumsim-
plesarraydentrode Session.set("posts", posts).OMeteortrataos
eventosdetemplatesdeformasemelhanteaoshelpers—adiferen çaéque
onossoeventoadotaráaconven ção Template.post.events().Basica-
mente,umeventonoMeteoréorganizadoatravésdaestrutura chave-valor
emqueachaveéumastringestruturadaporeventoeelemento( "evento
35

## Página 48

4.3. Publicandopostsnatimeline CasadoCódigo
elemento"),eovaloréumafun çãoemcujoparâmetroretornaoobjeto
event,semelhanteaoframework jQuery(http://jquery.com).
Atravésdosegundoparâmetro,chamadode template,temosacesso
àsfun ções template.finde template.findAll,queserãoutilizadas
pararetornarumelementointernodotemplate.Nonossocaso,o template
retornaotemplateatual,ecomissoépossívelnavegarentreseuselemen-
tosinternos.Utilizaremosafun ção template.find("textarea")para
obteratag <textarea>e,assim,capturarosdadosdamensagempubli-
cada. Emseguida,utilizamosum shortcutlógiconotrecho var posts
= Session.get("posts") || [];,quesimplesmenteretornaum array
vazioquando Session.get("posts")retornar undefined. Apósob-
termosoarraydeposts,incluiremosumnovopostnoarrayeoatualizare-
mosdentroda Session,via Session.set("posts", posts).Paraver
comoficou,crieoarquivo client/lib/events/post.js,seguindoaim-
plementaçãoadiante:
Template.post.events({
"submit form": function(e, template) {
e.preventDefault();
var textarea = template.find("textarea");
var posts = Session.get("posts") || [];
posts.push({message: textarea.value});
Session.set("posts", posts);
textarea.value = "";
}
});
Um detalhe final é que nesta função é obrigatório rodar a função
e.preventDefault()parafor çarobrowseranãorealizarumarequisi-
çãosíncronanoservidor—ouseja,paraqueelecanceleasubmissãopadrão
doformulário.
Vamosrodaroprojeto? Acesse http://localhost:3000 epubliqueseus
postsnatimeline.
36

## Página 49

CasadoCódigo Capítulo4. Implementandoumatimelinedeposts
Figura4.4:Timelinedinâmica!
Omaislegalévertudoissofuncionandoemtemporeal!Agoraabraum
novobrowsernomesmoendere çoepubliquenovosposts...
37

## Página 50

4.4. Persistindoelistandopostsemtempo-real CasadoCódigo
Figura4.5:Porqueatimelineestavazia?
Masqueestranho!Cadêospostsanterioresdatimeline?Esseproblema
ocorreudevidoaosimplesfatodequeaindanãofoiimplementadocódigo
queenvolvaobancodedados! Atéagorafizemosumatimeline client-side
visívelapenasparaoprópriousuárioutilizando Session.
4.4 P ersistindo e listando posts em tempo-real
Agoraquetemoso front-enddenossaprimeirafeature,vamosimplemen-
tarseu back-endparatorná-lo100%funcional.Basicamente,criaremosuma
collectionnoMongoDBparaarmazenarosnovospostsqueserãolistadosna
timelineemtempo-real.
Começandoaimplementaç ão,crieoarquivo models/post.jscom
conteúdoaseguir:
Post = new Meteor.Collection(’posts’);
Dessa forma, será instanciada acollection Post em variável global,
38

## Página 51

CasadoCódigo Capítulo4. Implementandoumatimelinedeposts
permitindoqueutilizemossuasfun çõestantonoclientecomonoservidor,
afinalodiretório modelsévisívelemambososlados. Feitoisso,faremos
uns refactorings nos códigos client/lib/helpers/timeline.js
e client/lib/events/post.js, e substituiremos o uso
do objeto Session pela collection Post. Abra e edite
client/lib/helpers/timeline.js,deixando-odaseguinteforma:
Template.timeline.helpers({
posts: function() {
return Post.find({});
}
});
Agoramodifiquetambémocódigo client/lib/events/post.js:
Template.post.events({
"submit form": function(e, template) {
e.preventDefault();
var textarea = template.find("textarea");
Post.insert({message: textarea.value});
textarea.value = "";
}
});
Done! Vamos testar a timeline? Reinicie o servidor e acessehttp://
localhost:3000.Agoratodosospostsnãoserãoexcluídosevocêtambémpo-
deráacessaressapáginaemquantasabasquisereemqualquernavegadorao
mesmotempo.
Parabéns! Terminamosnossaprimeirafuncionalidadedoprojeto: im-
plementamosdeformabemsimples,porém100%funcionalumatimelinede
posts. Continuelendopois,apóscriarmosasrestantesfeatures,voltaremos
nestatimelineparafazer refactoringsquepermitirãoalistagemdepostsde
usuáriosquevocêseguirnarede,masparaissoacontecer,vamoscriaroutras
funcionalidadesnoprojetoefaremosaintegraç ãodelascomatimeline.
39

## Página 53

Capítulo5
SignineSignupdeusuários
Nocapítuloanterior,exploramosoMeteordesenvolvendoolayouteafun-
cionalidademínimadeumatimelinedeposts.Come çamoscriandoostem-
plates,programamosomínimodecódigosuficienteparadarvidaàtimeline
efinalizamosocapítulopersistindoelistandoospostsnobancodedados
MongoDB.
Nestecapítulo,vamosaprofundarnossosconhecimentosdesenvolvendo
afuncionalidadede Signin(login)e Signup(cadastro),utilizandooconjunto
defuncionalidadesdopackage Accounts,queénativadoMeteor.
5.1 E xplorando Accounts do Meteor
O Accountspossuidiversasfun çõesreferentesaoprocessode login, logout,
recuperaçãodesenhas,mudan çadesenha,enviodee-mailverificadoreca-
dastrodeusuários.Eleétotalmenteextensivoepermiteaimplementaç ãode

## Página 54

5.1. ExplorandoAccountsdoMeteor CasadoCódigo
autenticações customizáveis através do consumo de APIs externas,como
porexemploautenticaç ãovia Google, Facebook, Twitter, Github, Meetup
etc.Diversasvariaçõesde AccountssãoencontradasnoAtmosphere:
https://atmospherejs.com/?q=accounts
Figura5.1:VariaçõesdopackageAccounts.
Combasenessaintroduç ão,vamosdesenvolverumsimplescadastroelo-
gindeusuáriodiretamentenabaselocaldoprojeto,emaisparafrenteimple-
mentaremosumaautenticaç ãoviaFacebook. Porenquanto,adicionaremos
trêsprincipaispackagesparacriarum signin/signupconvencional:
mrt add accounts-base
mrt add accounts-ui-bootstrap-3
mrt add accounts-password
O que faz cada package?
42

## Página 55

CasadoCódigo Capítulo5. SignineSignupdeusuários
•accounts-base:APInativaquecontémfun çõesessenciaispara sig-
nine signupdeusuários,persistindotodososdadosnoMongoDB;
•accounts-password:estepackageprovêfun çõespararealizarvali-
dação,mudan çaerecuperaç ãodesenha,alémdepossuirfun çõespara
enviodee-mail,comoe-maildeverificaç ãoe resetdesenha;
•accounts-ui-bootstrap-3: possui um conjunto de interfaces
prontaspararenderizarumformuláriodelogin,cadastroerecupera-
çãodesenha,tudoissoutilizandooframework Twitter Bootstrap 3.
Agora vamos botar a mão na massa! Edite o template
client/views/header.html: nele, vamos incluir o wid-
get {{> loginButtons}} que renderiza um template do
accounts-ui-bootstrap-3. Este último contém toda interface de
login,cadastroerecuperaç ãodeconta.
<template name="header">
<header class="container">
<nav class="navbar navbar-default">
<div class="navbar-header">
<a class="navbar-brand">Meteor Bird</a>
</div>
<div class="navbar-collapse collapse">
<ul class="nav navbar-nav navbar-right">
{{> loginButtons}}
</ul>
</div>
</nav>
</header>
</template>
Vejacomoficoulegal...
43

## Página 56

5.2. Associandopostsaumusuário CasadoCódigo
Figura5.2:SignIn/Upfornecidopeloaccounts-ui.
Omelhordetudoissoéquecarregamosestewidgetcomapenasuma
linhadecódigoetodoofluxodo back-end(cadastro,loginerecuperaç ãode
senha)jáfoifornecidopelo accounts-base+ accounts-password,ou
seja,sevocêcadastrarumaconta,umnovoregistronacollection usersserá
criado. Equandoprecisardosdadosdascollectionsdeusuários,vocêtem
disponívelafun çãonativa Meteor.users,queéomesmoquerodaressa
instância: Users = new Meteor.Collection('users').
5.2 A ssociando posts a um usuário
Nesta etapa, implementaremos um pouco deback-end. Vamos associar
nossatimelinecomo userIddousuário. Parafazerisso,utilizaremoso
Meteor.userId(),queretornao iddousuáriodasessãoe,emseguida,
vamosassociá-locomseuspostspublicados.Dessavez,criaremosométodo
Post.publishem models/post.jsparaabstrairacomplexidadedessa
funcionalidade.Vejacomofazer:
44

## Página 57

CasadoCódigo Capítulo5. SignineSignupdeusuários
Post = new Meteor.Collection(’posts’);
Post.publish = function(message) {
this.insert({
message: message,
date: new Date(),
userId: Meteor.userId()
});
};
Consequentemente faremos um refactoring em
client/lib/events/post.js, para utilizar esse novo método
Post.publish():
Template.post.events({
"submit form": function(e, template) {
e.preventDefault();
var textarea = template.find("textarea");
Post.publish(textarea.value);
textarea.value = "";
return false;
}
});
Parafinalizaraassociaç ão,vamoscriarumafun çãodentrodomodelo
Post,queseráumencapsulamentode Post.find({userId: userId}).
Elasechamará Post.list(userId)eficaráem models/post.js:
Post = new Meteor.Collection(’posts’);
Post.publish = function(message) {
this.insert({
message: message,
date: new Date(),
userId: Meteor.userId()
});
};
Post.list = function(userId) {
45

## Página 58

5.3. Exibindotimelinesomenteparalogados CasadoCódigo
return this.find({userId: userId});
};
Para o final, usaremos esta query de listagem para que ele
exiba somente posts do usuário logado, utilizando a fun ção
Meteor.userId() dentro do helper da timeline. Edite o arquivo
client/lib/helpers/timeline.js:
Template.timeline.helpers({
posts: function() {
return Post.list(Meteor.userId());
}
});
5.3 E xibindo timeline somente para logados
Agora temos que restringir a timeline para que somente usuários loga-
dos publiquem e visualizem os posts. Para resolver isso, existe uma
marcação especial do accounts-base chamada {{currentUser}},
que retorna os dados de um usuário quando o mesmo está logado
no sistema. Com isso, criaremos um template pai dentro do di-
retório client/views/home com o nome home.html, no qual
vamos incorporar os templates client/views/home/post.html e
client/views/home/timeline.html,somentequandoousuárioesti-
verlogadonaaplicaç ão.Quandonãoestiverlogadoo {{currentUser}}
retornaránuloecomissoseráexibidaamensagem: "Você não esta
logado, clique em Sign In / Up.".Parafazerisso,crieotemplate
client/views/home/home.htmlcomastagsaseguir:
<template name="home">
{{#if currentUser}}
<section class="col-sm-12">
{{> post}}
{{> timeline}}
</section>
{{else}}
<div class="text-center">
46

## Página 59

CasadoCódigo Capítulo5. SignineSignupdeusuários
<h1>Meteor Bird</h1>
<h3>Não esta logado? Clique em "Sign In/Up".</h3>
</div>
{{/if}}
</template>
Em seguida, vamos atualizar o template principal
client/index.html, deixando-o mais leve, apenas renderizando os
templates header, homee footer.
<head>
<title>Meteor Bird</title>
</head>
<body>
{{> header}}
<main class="container">
{{> home}}
</main>
{{> footer}}
</body>
Façaoteste!AcesseaURLdaaplicaç ãoem http://localhost:3000evisu-
alizeasnovastelasdedicadasparausuáriologadoeusuárionão-logado.
47

## Página 60

5.3. Exibindotimelinesomenteparalogados CasadoCódigo
Figura5.3:Usuáriologado.
Figura5.4:Usuárionão-logado.
48

## Página 61

CasadoCódigo Capítulo5. SignineSignupdeusuários
5.4 A utenticação via conta Facebook
O AccountsdoMeteorébemextensível,suasinterfacespermitemcriarva-
riaçõesde signine signupqueutilizemAPIdeaplicaçõesexternas.Existem6
variaçõesdessespackagesoferecidosnativamentepeloMeteore+60packages
third-partyexistentesno Atmosphere(https://atmospherejs.com).
Nesta seção, vamos focar na inclusão de apenas uma variação de
Accounts. Vamosutilizaro accounts-facebookparaqueosnossos
usuáriosseautentiquemnaaplicaç ãoatravésdeumacontaFacebook(http:
//facebook.com).
Habilitaro AccountsdoFacebooknaaplicaç ãoésimples,apartemais
chataécadastrarumaaplicaç ãonoFacebookparageraraschaves appIde
secretquesãousadasparaseautenticarnaredesocial.
Começandoaimplementação,vamosadicionaropackageaseguir:
mrt add accounts-facebook
Emseguida,adicionaremosumalistadepermissõesarespeitodosdados
queiremosconsumirdacontadousuárioquandoeleseautenticaremnosso
sistemaatravésdoFacebook.Quandoumusuáriopermitirseuacesso,eleli-
beradiversasinformaçõesdesuaconta,comoseue-mail,sualistadeamigos,
seusúltimosposts,seuperfilemuitomais.Cadainformaç ãovariadesistema
parasistema,eparaconhecertodasaspermissõesénecessárioconhecera
fundoadocumentaçãodesuaAPI(nonossocaso,temosqueestudaraAPIdo
Facebookatravésdo Facebook Developers).Antesdeumaaplicaç ãoexterna
permitirtalacesso,éexibidaumapáginadaprópriaaplicaç ãoavisandosobre
todasasinformaçõesqueserãoexpostasaoseautenticar.NoMeteor,utiliza-
mosafun ção Accounts.ui.config()paraconfiguraraspermissõesde
cadaautenticaçãoexternaviaatributo requestPermissions.Nopróximo
capítuloexplicareiemdetalhescomoautocompletaronomedousuárioque
entrarnaredeviaFacebook. PorémsevocênãopossuiumacontanoFa-
cebookepretendeentraratravésdocadastroconvencional,entãousaremos
oatributo extraSignupFieldsparaincluirumcampoextra,estecampo
seráonomedousuário. Paraaplicarestasconfiguraçõesnaaplicaç ão,crie
oarquivo client/lib/config/accounts_auth.jscomoscódigosa
seguir:
49

## Página 62

5.4. AutenticaçãoviacontaFacebook CasadoCódigo
Accounts.ui.config({
extraSignupFields: [{
fieldName: ’name’,
fieldLabel: ’Nome’
}],
requestPermissions: {
facebook: [’email’, ’user_about_me’]
}
});
Para que o cadastro convencional pré-preencha o nome do usuá-
rio, teremos que criar um código no servidor, responsável por in-
terceptar os dados do formulário durante o cadastro. Isso se faz
através do evento Accounts.onCreateUser(options, user).
Nesta função qualquer campo adicional será enviado através do
objeto options['profile']['campo_adicional'], ou seja,
options['profile']['name']. Por enquanto vamos apenas atri-
buiressecampo nameparaousuário,paraissotemosquecriaroarquivo
server/lib/accounts.jseimplementarocódigoabaixo:
Accounts.onCreateUser(function(options, user) {
user[’profile’] = options.profile;
return user;
});
Em nossa aplicação, vamos apenas consumir o email e
user_about_me (campos que contém dados básico do perfil — é lá
quepegaremosonomedeumusuárioFacebook). No server-side, temos
quedefiniraschavesparaacessaro serviço do Facebook,usandoaschaves
appIde secret. Paraconfiguraressaschavesvamosutilizarumnovo
packagequegerenciachavesdeserviçosexternos:
meteor add service-configuration
Com este package, poderemos configurar diversos ser-
viços de forma intuitiva, através das fun ções do modelo
ServiceConfiguration.configurations. Para evitar contas du-
plicadas ou triplicadas de um mesmo serviço, rodamos primeiro a
50

## Página 63

CasadoCódigo Capítulo5. SignineSignupdeusuários
função ServiceConfiguration.configurations.remove({})
para apagar todas as chaves dos serviços e, em seguida, rodamos
ServiceConfiguration.configurations.insert() para regis-
trar cada serviço no banco de dados. No nosso caso, vamos configurar
apenas o serviço de autenticaç ão do Facebook. Veja como fica essa
implementação, crieo server/lib/services.jseincluaocódigoa
seguir:
ServiceConfiguration.configurations.remove({});
ServiceConfiguration.configurations.insert({
service: ’facebook’,
appId: ’inserir appId gerado pelo Facebook’,
secret: ’inserir secret gerado pelo Facebook’
});
Obs.: Paracadastrarumaaplicaç ãonoFacebook, acesseosite https:
//developers.facebook.com. Registre uma aplicação (provavelmente com
outro nome, pois o Meteor Bird acabei de registrar), inclua o domí-
nio de redirect (pode serhttp://localhost:3000 ) para que, após o usuá-
rio se autenticar, ele consiga voltar para tela principal do nosso sistema
já autenticado. Ao registrar sua aplicação no Facebook, acesse odash-
board e procure pelos campos ID do aplicativo (appId) e o App Se-
cret (secret). Copie e cole os respectivos valores da função anterior
ServiceConfiguration.configurations.insert()dentrodosatri-
butos appIde secret.
Apósfinalizaressaetapa,sónosrestatestar.Reinicieoservidoreacesse
apáginadanossaaplicaç ão. Reparequeautomaticamenteumanovaop ção
delogin(via Facebook)foiincluídapelo Accounts UI,entãocliquenesta
opçãoeseautentiquecomsuacontadoFacebook.
51

## Página 64

5.4. AutenticaçãoviacontaFacebook CasadoCódigo
Figura5.5:AutenticaçãoviaFacebook.
Parabéns!Fechamosmaisumcapítulodesenvolvendoum signine signup
emnossaaplicaç ão,exploramososprincipaisrecursosdoobjeto Accounts
eseuspackagesauxiliares,tambémadicionamosumaautenticaç ãoviaFace-
bookparaagilizaro signindosusuários.Nopróximocapítulo,criaremosum
perfildeusuárioefaremosalguns refactoringsnaautenticaçãodo Facebook
paraconsumirosdadosdessacontaautocompletandonosdadosdoperfil.
52

## Página 65

Capítulo6
Perfildousuário
6.1 C riando template de perfil
Neste capítulo, criaremos uma tela para o perfil do usuário logado,
que será exibido no bloco lateral esquerdo, constituído pelos campos:
nome e descrição. De início, um novo usuário não terá esses da-
dos completos. Para isso, vamos criar um bloco que apresenta o
perfil (Template.profileBox), um template que será um formulá-
rio para atualizar o perfil (Template.profileForm) e, por último,
um template que será o intermediador entre os templates anteriores (
Template.profile). Começaremoscriandooblocodoperfil,queserá
umsubtemplatedodiretóriodotemplate home,ouseja,vamoscriarodire-
tório client/views/home/profile,dentrodoqualimplementaremoso
HTML client/views/home/profile/profile_box.html.Estetem-
platevaiutilizaramarcaç ão {{currentUser.profile}}paraapresentar

## Página 66

6.1. Criandotemplatedeperfil CasadoCódigo
operfildousuário:
<template name="profileBox">
{{#with currentUser.profile}}
<h4>{{name}}</h4>
<p>{{about}}</p>
<button class="btn btn-block">
Editar perfil
</button>
{{else}}
<p>Perfil incompleto</p>
<button class="btn btn-block">
Completar perfil
</button>
{{/with}}
</template>
Assim, como criamos o bloco de exibição do perfil, tam-
bém criaremos seu formulário para edição. Isso será no diretório
client/views/home/profile/profile_form.html, seguindo a
implementação:
<template name="profileForm">
<form class="form-horizontal">
<input type="text" class="form-control"
placeholder="Nome">
<input type="text" class="form-control"
placeholder="Descrição">
<button class="btn btn-success">
Atualizar
</button>
</form>
</template>
Agora que temos os templates, precisamos criar o mediador
entre eles. Ele basicamente utilizará a condicional da variável
Session.get('editProfile') para mostrar o bloco do perfil
quando seu valor forfalse, e mostrar o formulário quando seu valor
54

## Página 67

CasadoCódigo Capítulo6. Perfildousuário
for true. Além disso, esta variável será visível pelos templates atra-
vésdeumafun ção helper. Paracriarestaregra, primeirocrieohelper:
client/views/lib/helpers/profile.jscomaseguinteregra:
Template.profile.helpers({
editProfile: function() {
return Session.get("editProfile");
}
});
Em seguida, crie o seu respectivo template em
client/views/home/profile/profile.html:
<template name="profile">
{{#if editProfile}}
{{> profileForm}}
{{else}}
{{> profileBox}}
{{/if}}
</template>
Finalmente, incluiremos perfil dentro de seu template pai, que é o
client/views/home/home.html. Eleficaránalateralesquerdaatravés
datag <aside>,deacordocomcódigoaseguir:
<template name="home">
{{#if currentUser}}
<aside class="col-sm-3">
{{> profile}}
</aside>
<section class="col-sm-9">
{{> post}}
{{> timeline}}
</section>
{{else}}
<div class="text-center">
<h1>Meteor Bird</h1>
<h3>Não esta logado? Clique em "Sign In/Up".</h3>
</div>
55

## Página 68

6.1. Criandotemplatedeperfil CasadoCódigo
{{/if}}
</template>
Parabéns! Játemosostemplatesdefinidossobreoperfil. Quetalagora
darvidaaostemplates?Porexemplo,em profile_box.htmlpoderíamos
darfuncionalidadeaoslinks: “Editarperfil”e“Completarperfil”. Elesse-
rãoresponsáveisporapresentaroformulárioeambosexecutarãoamesma
coisa,queserárenderizaro Template.profileFormatravésdoevento
"click button"(cliquedobotão).Nestecaso,esteslinksapenasirãoatri-
buirovalor trueparaafun ção Session.set("editProfile")—e
como Sessionéumobjetoreativo,instantaneamenteseráfeitaessatransi-
çãoentreotemplatedeblocodoperfilparaotemplatedeformulário. Veja
comofazercriandoocódigo client/lib/events/profile_box.js:
Template.profileBox.events({
"click button": function(e) {
e.preventDefault();
Session.set("editProfile", true);
}
});
Com o formulário na tela, vamos agora codificar sua funcionali-
dade de atualizar os dados do perfil. Eles serão persistidos na collec-
tion usersdentrodoatributo profile,ouseja,em users.profile.
Esta atualização será realizada via função Meteor.user.update().
Em seguida, mudaremos o estado deeditProfilerodando a função
Session.set("editProfile", false),etambémutilizaremosafun-
ção e.preventDefault()paracancelarasubmissãopadrãodoformulá-
rio.
Criaremos a implementaç ão dessas regras no código
client/lib/events/profile_form.js,vejacomofazer:
Template.profileForm.events({
"submit form": function(e, template) {
e.preventDefault();
var inputs = template.findAll("input");
Meteor.users.update(
56

## Página 69

CasadoCódigo Capítulo6. Perfildousuário
{ _id: this.userId },
{ $set:
{ "profile.name": inputs[0].value,
"profile.about": inputs[1].value }
});
}
Session.set("editProfile", false);
});
Vejanasimagenscomoficaramoslayoutsdoperfildeusuário:
Figura6.1:Teladeperfilincompleto.
57

## Página 70

6.2. AutocompletandoperfilviasignindoFacebook CasadoCódigo
Figura6.2:Atualizandodadosdoperfil.
Figura6.3:Perfilatualizado.
6.2 A utocompletando perfil via signin do Face-
book
Nocapítuloanterior,foramcriadosdoismodosde signine signupnaapli-
cação. O primeiro modo é o convencional cadastro de nome, e-mail e
senha. Já o segundo, é osignin via conta doFacebook. Foi adicio-
58

## Página 71

CasadoCódigo Capítulo6. Perfildousuário
nadoopackage accounts-facebooketambémimplementamosoar-
quivo client/lib/config/accounts_auth.js,definindoaspermis-
sõesdeconsumodasinformaçõesdeumusuárioFacebookatravésdafun ção
Accounts.ui.config().Nele,adicionamosalistadepermissõesqueper-
miteconsumirosdadosdee-mailedadospúblicodousuário,tudoissoden-
trodoatributo requestPermissions.facebook.
Combasenessaimplementaç ão,iremosinterceptarnovamenteoevento
decadastrodeusuário,paraautocompletarosdadosvindosdeumaconta
do Facebook. Essainterceptaçãoseráapenasparaidentificarseo signinfoi
realizadoviaserviço Facebook;sesim,pegaremosonomedousuárioatra-
vésdoobjeto user.service.facebook.name,casocontrário,retorna-
mosofluxonormaldo callback. Parafazerisso, vamosextenderoatual
server/lib/accounts.jscomocódigoaseguir:
Accounts.onCreateUser(function(options, user) {
if (user.services.facebook) {
var facebook = user.services.facebook;
user[’profile’] = {
name: facebook.name
};
} else {
user[’profile’] = options.profile;
}
return user;
});
Feitoisso,façaoteste:realizeumloginviaFacebookcomoqual,aoaces-
sarapáginaprincipal,seráexibidonoperfildousuário,onomedelequeveio
deumaconta Facebook.
Foimaisumafeatureimplementadanaredesocial! Dessaveznósex-
ploramosumpoucoamaissobremanipulaç ãodetemplatesno client-side.
Continuelendo!Nospróximoscapítulosiremostrabalharmaisno server-side
daaplicação,explorandoalgunscomandosprincipaisdoMongoDB,alémde
usarnovospackagesdoMeteor.
59

## Página 73

Capítulo7
Teladeperfilpúblicodousuário
7 .1 A daptando rotas no projeto
Antesdecome çarmosafundoaimplementarateladeperfilpúblicodousuá-
rio,faremosalguns refactoringsimportantesparatornarocódigodaaplicaç ão
extensívelereutilizável,atravésdodesenvolvimentoderotas.
Nestaetapa,faremosalgumasalteraçõesemcódigosquejáimplementa-
mos,masantesadicionaremosumnovopackage,queseráomestreemge-
renciaremanipularrotas.Seunomeé iron-router.
mrt add iron-router
Este é um framework que trata toda parte de rotas na aplicação.
Mesmoquenossaaplicaç ãosejaemformato single-page,épossíveltorná-
lo multi-pageatravésdeumroteamentode paths. Diferentedasou-
tras linguagens em que as rotas redirecionavam para páginasHTML, o

## Página 74

7.1. Adaptandorotasnoprojeto CasadoCódigo
iron-routertrabalhamaisafundocommanipulaç ãodetemplates,ouseja,
comele,cada redirectseráumatransiçãodeumtemplateparaoutro. Ele
tambémpermiteterumcontrolemaiscompletosobreumarota,atravésda
implementaçãodopatternclassicamenteconhecidopor controller.
Voltandoaonossoprojeto,come çaremosabrincadeiracriandooarquivo
principalgerenciadorderotas,quesechama client/lib/routes.js.
Vejaaseguircomoseráseucódigo:
Router.map(function() {
this.route(’home’, {
path: ’/’
template: ’home’,
layoutTemplate: ’layout’,
});
});
Basicamentecriamosaprimeirarotadaaplicaç ão,querenderizaotem-
plate homeaoacessararotaraiz. Masparaqueessarotafuncionecor-
retamente,temosqueadaptaraviewprincipalparafazerfuncionaroro-
teamentodostemplates. Esteroteamentoinicia-sesomentequandovocê
criar o layoutTemplate incluindo nele a marcação {{> yield}}.
Nocódigoanterior( client/lib/routes.js)foidefinidoquemseráo
layoutTemplate. Estetemplatecriaremosapósatag <body>naview
principal;ouseja,abrao client/index.htmlefaçaasseguintesmodi-
ficações:
<head>
<title>Meteor Bird</title>
</head>
<body>
</body>
<template name="layout">
{{> header}}
<main class="container">
{{> yield}}
</main>
{{> footer}}
</template>
62

## Página 75

CasadoCódigo Capítulo7. Teladeperfilpúblicodousuário
Setudodercerto,ahomepagedaaplicaç ãocontinuarásuaexibiçãonor-
malmente,masagoraarenderizaç ãodostemplatesserãocontroladosatravés
dasrotasnocódigo client/lib/routes.js.Comessapequenaadapta-
ção,deixamosaaplicaç ãoflexívelparaainclusãodenovastelassemprecisar
adicionarcódigoscomplexosnoprojeto. Essaflexibilidadeocorreuporque
delegamostodocontroledetemplatesparao iron-router.
Essafoinossaprimeiraadaptaç ãonoprojetousandoesteframework.
Continuandoasadaptaçõesparausaro iron-router,vamosmigrarasfun-
çõesdemodelosexistentesemalguns helpersparaqueelassejamexecutadas
narotaprincipal. Em client/lib/routes.jsincluaoatributo data
comaseguintefun ção:
Router.map(function() {
this.route(’home’, {
path: ’/’,
template: ’home’,
layoutTemplate: ’layout’,
data: function() {
return {
posts: Post.list(Meteor.userId())
}
}
});
});
Utilizandooatributo data,podemosrodarfun çõesretornemobjetos
aseremrenderizadosnostemplates. Agoraquemigramosessafun çãode
listagemdeposts,nãohámaisnecessidadedemanterseuantigohelper,então
excluaoarquivo client/lib/helpers/timeline.js.
7 .2 P erfil público do usuário
Agoraqueadaptamosnossaaplicaç ãoparaopadrãoderotas,vamosfocar
nacriaçãodoperfilpúblicodousuário. Paraissofuncionar,cadausuário
precisaterumarotaprópriaecomidentificadorúnicoparaquetalperfilseja
facilmenteacessívelporoutrosusuários.
63

## Página 76

7.2. Perfilpúblicodousuário CasadoCódigo
Depoisdessabreveexplicaç ão,vamosfazerum refactoringcomoobjetivo
dereutilizaratimelineatualdentrodotemplatedeperfilpúblico.Paraisso,
vamosapenasmoverotemplate client/views/home/timeline.html
paraodiretórioacimaqueseráem client/views/timeline.html.
Feita essa pequena alteração, vamos come çar o desenvolvi-
mento do perfil criando seu template. Crie o template de perfil em
client/views/user/user.html:
<template name="user">
{{#if user}}
<div class="text-center">
{{#with user.profile}}
<h1>{{name}}</h1>
<p>{{about}}</p>
{{/with}}
{{> timeline}}
</div>
{{else}}
<h1>Usuário não identificado.</h1>
<a href="{{pathFor ’home’}}">Homepage</a>
{{/if}}
</template>
Nestaview,utilizamosumanovamarcaç ãoherdadado iron-router,
quesechama {{pathFor}}. Elabasicamenteretornaastringdeumaurl
definidaemsuarespectivarota. Nestecasoretornouaurlda 'home'via
função {{pathFor 'home'}}.
Agora vamos dar vida ao perfil público implementando suas opera-
ções necessárias para renderizar dados corretamente. Para isso, edite o
client/lib/routes.js:
Router.map(function() {
this.route(’home’, {
path: ’/’,
template: ’home’,
layoutTemplate: ’layout’,
data: function() {
return {
64

## Página 77

CasadoCódigo Capítulo7. Teladeperfilpúblicodousuário
posts: Post.list(Meteor.userId())
}
}
});
this.route(’user’, {
path: ’/user/:_id’,
template: ’user’,
layoutTemplate: ’layout’,
data: function() {
var _id = this.params._id;
return {
user: Meteor.users.findOne({_id: _id}),
posts: Post.list(_id);
}
}
});
});
Narota /user/:_id,temosumpequenodetalhequeéoseuidentifi-
cador: ":_id". Istosignificaquearotaaceitaráqualquervalordentrodo
padrãodessepath: /user/[qualquer-valor].Eessevalorseráinjetado
navariávelthis.params._id.Essepatterndecriaç ãodevariáveisatravés
deparâmetronasrotasexisteemdiversosframeworkswebcomoporexem-
plo:Rails,Express,VRaptoreoutros.
Acabamosdecriaroperfil.Parafazerum test-drive,cadastreumusuário
nosistemaouentreutilizandoumacontanoFacebook,eemseguidaabra
umanovajanelanoterminal.Viacomando cd,acesseodiretóriodoprojeto
paralogodepoisacessaroclienteMongoDBcomocomando:
meteor mongo
Comoclienterodando,executeafun ção db.users.findOne()para
buscaroprimeirousuáriodabase,jácomoresultadoJSONformatadona
tela.Doresultado,apenascopieovalordocampo "_id"ecole-onobrowser
formandooendere çohttp://localhost:3000/user/[_id].
65

## Página 78

7.2. Perfilpúblicodousuário CasadoCódigo
Figura7.1:Pegando_iddousuárioviaCLIdoMongoDB.
66

## Página 79

CasadoCódigo Capítulo7. Teladeperfilpúblicodousuário
Figura7.2:Inserindo_idnarota/users/:id.
Setudoocorrerbem,vocêveráateladeperfilcomosdadosdousuárioe
seusúltimospostspublicados.
Emaisumcapítulofinalizado,parabéns!Nãoparedelerestelivro,pois
nopróximoepisódioiremosimplementaraclássicafuncionalidadedeseguir
edeixardeseguirumusuário.
67

## Página 81

Capítulo8
FollowmeIwillfollowyou
8.1 I ntrodução sobre a funcionalidade
Esteseráumcapítulodedicadoaexplicarcomocriarafuncionalidadeclássica
degerenciarseguidoresnaredesocial.Afinal,oMeteorBirdébasicamente
umaversão light, diet,semaçúcardo Twitter(http://twitter.com),ecasovocê
nãosaibaosignificadodeseguirumusuário,eisumabreveexplicaç ão: o
objetivoprincipaldeumatimelineéexibirseuspostseprincipalmenteos
postsdeseusamigos;taisamigossãousuáriosquevocê seguenaredesocial.
Porisso,seguirumusuáriopermitequevocêtenhaacessoaconteúdosque
elepublicar.
Combasenessaexplicaç ão,vamosnestecapítulofocarapenasnacons-
truçãodessafuncionalidade,queserádivididaempequenasfuncionalidades
listadasaseguir:

## Página 82

8.1. Introduçãosobreafuncionalidade CasadoCódigo
• Botãofollow(seguir)e unfollow(deixardeseguir);
• Contadordeseguidoresnoperfildousuário.
Antesdecome çarmosapróximase ção,quetalprepararatimelinepara
receberonomedousuáriodecadapost? Assim,visualizaremosfacilmente
oautordecadapost.Paraisso,editeo models/post.jsadicionandoum
novoparâmetro:
Post.publish = function(message, name) {
var params = {
message: message,
time: new Date(),
userId: Meteor.userId(),
name: name
};
this.insert(params);
};
Em seguida, atualize o código de evento do post, o
client/lib/events/post.js. Nele, pegaremos o nome do usuá-
riologadoutilizandoafun ção Meteor.user().profile.name:
Template.post.events({
"submit form": function(e, template) {
e.preventDefault();
var textarea = template.find("textarea");
var name = Meteor.user().profile.name;
Post.publish(textarea.value, name);
textarea.value = "";
}
});
E para finalizar, adicione uma tag no template da timeline para
que exiba o nome do autor. É o que faremos editando a view
client/views/timeline.html:
<template name="timeline">
<div class="row">
70

## Página 83

CasadoCódigo Capítulo8. FollowmeIwillfollowyou
<fieldset class="col-sm-12">
<legend>últimos posts</legend>
{{#each posts}}
<blockquote class="lead">
<p>{{message}}</p>
<small>Autor:
<a href="/user/{{userId}}">{{name}}</a>
</small>
</blockquote>
<hr>
{{else}}
<p class="lead text-center">
Nenhum post publicado.
</p>
{{/each}}
</fieldset>
</div>
</template>
Pronto,vejacomoficouatimeline:
71

## Página 84

8.2. CriandoosbotõesdeFolloweUnfollow CasadoCódigo
Figura8.1:Exibindoautordopostnatimeline.
8.2 C riando os botões de Follow e Unfollow
Depoisdelimpartodaacasanocapítuloanterior,játemosespaçosuficiente
paracriarnovasfuncionalidadescomorientaç ãoàsrotasdaaplicaç ão.Nesta
seção,vamosfocarnaimplementaç ãodosbotões Seguire Deixar de seguir.
Paracome çar, vamoscodificarumnovomodeloquechamaremosde
Friendship.Eleteráumaestruturasimples,porémpoderosa!Basicamente,
elevaiarmazenarapenas2campos:
•userId: _iddousuáriologado;
•friendId: _iddousuárioquesepretendeseguir.
Combasenesses2campos,épossívelcriarasfuncionalidadesnecessárias
paraseguir,deixardeseguir,contarquantosseguidoresvocêtemequantos
72

## Página 85

CasadoCódigo Capítulo8. FollowmeIwillfollowyou
vocêsegue.Masindoporpartes,vamosprimeirocriaromodelocomasse-
guintesfun ções: follow, unfollowe isFollowing.Parafazerisso,crie
estecódigoem models/friendship.jsseguindootrecho:
Friendship = new Meteor.Collection(’friendships’);
Friendship.follow = function(friendId) {
this.insert({
userId: this.userId,
friendId: friendId
});
};
Friendship.unfollow = function(friendId) {
this.remove({
userId: this.userId,
friendId: friendId
});
};
Friendship.isFollowing = function(friendId) {
return this.findOne({
userId: this.userId,
friendId: friendId
});
};
Combasenessas3fun ções, atualizaremosarota /userecriaremos
2 novas rotas parafollow e unfollow de usuários. Abra e edite o
client/lib/routes.jsparafazerisso.
Router.map(function() {
// código da rota "this.route(’home’)"
this.route(’user’, {
path: ’/user/:_id’,
template: ’user’,
layoutTemplate: ’layout’,
data: function() {
var _id = this.params._id;
var isFollowing = Friendship.isFollowing(_id);
Session.set(’currentUserId’, _id);
73

## Página 86

8.2. CriandoosbotõesdeFolloweUnfollow CasadoCódigo
Session.set(’isFollowing’, isFollowing);
return {
user: Meteor.users.findOne({_id: _id}),
posts: Post.list(_id)
}
}
});
this.route(’follow’, {
path: ’/user/:_id/follow’,
action: function() {
var _id = this.params._id;
Friendship.follow(_id);
this.redirect(’/user/’ + _id);
}
});
this.route(’unfollow’, {
path: ’/user/:_id/unfollow’,
action: function() {
var _id = this.params._id;
Friendship.unfollow(_id);
this.redirect(’/user/’ + _id);
}
});
});
Agora que temos as regras defollow e unfollow, vamos dar
vidaaelescriandoseusrespectivosbotõesnotemplatedeperfilpúblico.
Mas antes, falta criar algumas regras em helpers: uma regra é evitar
queousuáriosigaseupróprioperfil(atravésdafun ção canFollow()),
e a outra regra é a transição entre os botõesSeguir e Deixar de se-
guir (via função isFollowing()). Vamos criá-las no novo helper
client/lib/helpers/follow_button.js:
Template.followButton.helpers({
canFollow: function() {
var userId = Meteor.userId();
return userId && Session.get(’currentUserId’) != userId;
},
isFollowing: function() {
74

## Página 87

CasadoCódigo Capítulo8. FollowmeIwillfollowyou
return Session.get(’isFollowing’);
}
});
Essehelperseráabaseparaimplementarotemplatedosbotõesquecria-
remosem client/views/user/follow_button.htmlcomoscódigos
aseguir:
<template name="followButton">
{{#if canFollow}}
{{#with user}}
{{#if isFollowing}}
<a href="{{pathFor ’unfollow’}}"
class="btn btn-primary btn-large">
Deixar de seguir
</a>
{{else}}
<a href="{{pathFor ’follow’}}"
class="btn btn-success btn-large">
Seguir
</a>
{{/if}}
{{/with}}
{{/if}}
</template>
Reparenoslinksdosbotões.Novamenteutilizamoso {{pathFor}}e,
incrivelmente,eledetectouo _idcorretodopath. Mascomoelefezessa
mágica?Oiron-routersegueconven çõesdeURLsREST,ouseja,quando
criamosasrotas /user/:_id/followe /user/:_id/unfollow,por
convenção REST, estamos dizendo no path que o:_id é do user.
Combasenisso, asfun ções: {{pathFor 'follow'}}e {{pathFor
'unfollow'}}incluíramo _idcorretamenteporqueutilizamosamarca-
ção {{#with user}}emvoltadesseslinks.Issofezcomqueautomatica-
menteo _iddeum userapareçanoslinks.
ParamaisdetalhessobreREST,recomendoaleituradesselivro:
http://www.casadocodigo.com.br/products/livro-rest
75

## Página 88

8.2. CriandoosbotõesdeFolloweUnfollow CasadoCódigo
Para finalizar, adicione o template dos botões dentro de
client/views/user/user.html:
<template name="user">
{{#if user}}
<div class="text-center">
{{#with user.profile}}
<h1>{{name}}</h1>
<p>{{about}}</p>
{{/with}}
{{> followButton}}
{{> timeline}}
</div>
{{else}}
<h1>Usuário não identificado.</h1>
<a href="{{pathFor ’home’}}">Homepage</a>
{{/if}}
</template>
Quetaltestarmosaaplicaç ãoseguindoalgunsusuários?Vamoslá!Crie
umnovousuáriocomonomequevocêquiser.Nomeucaso,criareioJoãoe
aMaria.Captureseusrespectivos _id—podesermanualmente,buscando
peloMongoDBatravésdoscomandos:
meteor mongo
db.users.find().pretty()
Oimportanteéquevocêacessenobrowseroperfilpúblicodessesdois
usuários,maslogadopelasuacontaatual. VejaaseguirosperfisdeJoãoe
Maria:
76

## Página 89

CasadoCódigo Capítulo8. FollowmeIwillfollowyou
Figura8.2:PerfilpúblicodeJoão.
Figura8.3:PerfilpúblicodeMaria.
77

## Página 90

8.2. CriandoosbotõesdeFolloweUnfollow CasadoCódigo
Agoracliquenobotão Seguirdosdoisperfis.Funcionounãoé!?Legal!
Masdepoisdeumcertotempo,vocêparoudefalarcomJoãoeagoraquer
deixardeseguirseuperfil;nisso,vocêclicounobotão Deixar de seguirdo
perfildele...
Figura8.4:Erro:ExceptionfromDepsrecompute.
Oquesignificaoerro Exception from Deps recompute?Esseerroocor-
rerásemprequesurgiralgumconflitonoPubSubdaaplicaç ão.Nomomento,
estamosusandoopackagedefault: autopublish.Elecriaautomaticamente
um Publisheum Subscribeparacadacollectionqueusarmosnoclient-
sidedaaplicação.Usá-loemambientedeproduç ãoéumafalhagravíssimade
segurançapoisvailiberaracessoaqualquerfun çãodoMongoDBviaconsole
deumbrowser. Utilize-oapenasparaprototiparsuaaplicaç ãoe,principal-
mente,paraterno çãodequaisoperaçõesserãoutilizadasdobancodedados.
Apósdefinirtodasasfun çõesdebancodedados,removaestepackageecrie
funçõesdepublishesubscribeparacadaoperaç ãoutilizadadascollections.
Fiquetranquilo,teremosumcapítulodedicadoacomousaroPubSubetam-
78

## Página 91

CasadoCódigo Capítulo8. FollowmeIwillfollowyou
bémcomoprepararumaaplicaç ãoMeteorparaambientedeproduç ão.
Voltandoaonossoproblemaatual,basicamenteesseerroocorrequando
algumaconexãoPubSubestáquebrada,porém,comodescobriroquecausou
esseerro?Aoatualizaratelaatualdoerro,surgiuumnovoerro,essesimé
maisespecíficoecausadordessecaosnaaplicaç ão.Vejaaimagemaseguir:
Figura8.5:Erro:Notpermitted.Untrustedcodemayonlyremovedocuments
byID.
EsseerroéumalertapadrãoqueopróprioMeteorgeraquandosetenta
atualizarouremoverdadosdeumacollectionviaclient-side.Ébasicamente
umatravadeseguran ça,queexigequeoperaçõesdessetiposejamexecutadas
noserver-sidedaaplicaç ãoparaevitarqueelassejamacessíveiseadulteradas
pelocliente. Paraentendermelhor,recomendoqueleiaesselinkdadocu-
mentaçãooficialdoMeteor:
http://docs.meteor.com/#allow
Agoraquesabemosqualorealerrodaaplicaç ão,vamosfocaremsua
solução. Neste caso, vamos aprender a fundo como utilizar as funções
79

## Página 92

8.2. CriandoosbotõesdeFolloweUnfollow CasadoCódigo
Meteor.methodse Meteor.call. Usamoso Meteor.methodspara
definir funções no servidor que serão chamadas pelo cliente através do
Meteor.call.Fazendoumacomparaç ãocomoutrastecnologias,podemos
compará-locomousodoAJAX(Asynchronous Javascript and XML),emque
ousamosnoclientepararealizarrequisiçõesassíncronasnoservidor.Ambos
funcionamdamesmaforma,adiferen çaéqueadupla Meteor.methodse
Meteor.callpossuiumníveldeabstraç ãodealtonível,apontodeapenas
chamarafun çãodoservidorereceberseurespectivoresultado.
Combasenessesconceitos, vamosresolveroproblemaquenãoper-
mite executar a operação de unfollowde um usuário, afinal esta função
foi programada para remover um registro do banco de dados. Na prá-
tica,vamosapenasencapsularafun ção Friendship.unfollowdentrode
Meteor.methods,emigrarasdemaisfun çõesde inserte updatedeoutros
modelosparaestepadrãotambém.
Crieoarquivo server/methods.jscomocódigoaseguir:
Meteor.methods({
followUser: function(friendId) {
Friendship.follow(friendId);
},
unfollowUser: function(friendId) {
Friendship.unfollow(friendId);
},
profileUpdate: function(name, about) {
Meteor.users.update(
{_id: this.userId},
{$set: {
"profile.name": name,
"profile.about": about
}}
);
},
publishPost: function(message, name) {
Post.publish(message, name);
}
});
Agoraquemigramosasprincipaisfun çõesdeinserir,atualizareremover
80

## Página 93

CasadoCódigo Capítulo8. FollowmeIwillfollowyou
dados,vamosmudarsuasrespectivaschamadasaomodeloparausaremo
Meteor.call,demodoquenãoprecisaremosmaisusaro package default
chamado insecure. Aliás,jamais o utilize em ambiente de produ ção,
afinalelepermiteaexecuç ãodiretadefun ções updatee removedascol-
lectionsviabrowser.O insecuree autopublish(esteúltimoexplicarei
emdetalhesnopróximocapítulo)sãopackagespré-instaladosporumúnico
motivo,queéauxiliaraprototipagemrápidadaaplicaç ão.Nãoprecisaremos
maisdeleentãorodeoseguintecomando:
mrt remove insecure
Começaremoso refactoringeditandoo client/lib/routes.js:
Router.map(function() {
// código da rota "this.route(’home’)"
// código da rota "this.route(’user’)"
this.route(’follow’, {
path: ’/user/:_id/follow’,
action: function() {
var _id = this.params._id;
Meteor.call("followUser", _id);
this.redirect(’/user/’ + _id);
}
});
this.route(’unfollow’, {
path: ’/user/:_id/unfollow’,
action: function() {
var _id = this.params._id;
Meteor.call("unfollowUser", _id);
this.redirect(’/user/’ + _id);
}
});
});
Emseguida,atualizaremosocódigo client/lib/events/post.js:
Template.post.events({
"submit form": function(e, template) {
e.preventDefault();
81

## Página 94

8.3. Contadordeseguidoresnoperfil CasadoCódigo
var textarea = template.find("textarea");
var name = Meteor.user().profile.name;
Meteor.call("publishPost", textarea.value, name);
textarea.value = "";
}
});
Eporúltimo,editeoarquivo client/lib/events/profile_form.js:
Template.profileForm.events({
"submit form": function(e, template) {
e.preventDefault();
var inputs = template.findAll("input");
var name = inputs[0].value;
var about = inputs[1].value;
Meteor.call("profileUpdate", name, about);
Session.set("editProfile", false);
}
});
Pronto!Depoisdessasdicas,agoravocêpodedeixardeseguiroperfildo
João.
8.3 C ontador de seguidores no perfil
Paradeixaroperfildousuáriomaisricoeminformações,vamoscriarum
templateparainformarototaldeseguidoresequantosusuárioselesegue.
Paramanterotemplatereusável,vamoscriá-lodeformaquesejaapresentado
nateladousuáriologadoetambémnoseuperfilpúblico.
Crieotemplate client/views/friendship.htmlcomocódigoa
seguir:
<template name="friendship">
<p>Seguidores: {{followers}}</p>
<p>Seguindo: {{followings}}</p>
</template>
Adicionaremos esse template dentro do perfil público em
client/views/user/user.html, através do marcador {{>
friendship}}:
82

## Página 95

CasadoCódigo Capítulo8. FollowmeIwillfollowyou
<template name="user">
{{#if user}}
<div class="text-center">
{{#with user.profile}}
<h1>{{name}}</h1>
<p>{{about}}</p>
{{/with}}
{{> friendship}}
{{> followButton}}
{{> timeline}}
</div>
{{else}}
<h1>Usuário não identificado.</h1>
<a href="{{pathFor ’home’}}">Homepage</a>
{{/if}}
</template>
E também adicionaremos este template em
client/views/home/home.html:
<template name="home">
{{#if currentUser}}
<aside class="col-sm-3">
{{> profile}}
{{> friendship}}
</aside>
<section class="col-sm-9">
{{> post}}
{{> timeline}}
</section>
{{else}}
<div class="text-center">
<h1>Meteor Bird</h1>
<h3>Não esta logado? Clique em "Sign In/Up".</h3>
</div>
{{/if}}
</template>
Feitasessasinclusões, vamoscriarasfun çõesparacalcularototalde
83

## Página 96

8.3. Contadordeseguidoresnoperfil CasadoCódigo
followerse followings,atravésdacollection Friendship. Abrae
editeocódigo models/friendship.js:
Friendship = new Meteor.Collection(’friendships’);
// código da função "Friendship.follow()"
// código da função "Friendship.unfollow()"
// código da função "Friendship.isFollowing()"
Friendship.followings = function(userId) {
return this.find({userId: userId}).count();
};
Friendship.followers = function(friendId) {
return this.find({friendId: friendId}).count();
};
Por fim, vamos usá-las nas rotasuser e home. Abra e edite o
client/lib/routes.jsefaçaessamágicadaseguintemaneira:
Router.map(function() {
this.route(’home’, {
path: ’/’,
template: ’home’,
layoutTemplate: ’layout’,
data: function() {
var _id = Meteor.userId();
return {
posts: Post.list(_id),
followers: Friendship.followers(_id),
followings: Friendship.followings(_id)
}
}
});
this.route(’user’, {
path: ’/user/:_id’,
template: ’user’,
layoutTemplate: ’layout’,
data: function() {
var _id = this.params._id;
var isFollowing = Friendship.isFollowing(_id);
Session.set(’currentUserId’, _id);
84

## Página 97

CasadoCódigo Capítulo8. FollowmeIwillfollowyou
Session.set(’isFollowing’, isFollowing);
return {
user: Meteor.users.findOne({_id: _id}),
posts: Post.list(_id),
followers: Friendship.followers(_id),
followings: Friendship.followings(_id)
}
}
});
// código da rota "this.route(’follow’)"
// código da rota "this.route(’unfollow’)"
Vejacomoficoubonitoessetemplate:
Figura8.6:Contadordeseguindoeseguidores.
85

## Página 98

8.4. Visualizandopostdequemvocêseguir CasadoCódigo
8.4 V isualizando post de quem você seguir
Parafinalizarocapítulo,vamosmelhorarnossatimeline. Játemostodosos
recursosimplementadosparaseguirusuários,masnadadissotemgraç ase
nãoforpossívelvisualizarospostsdessesusuários—omesmovaleparaas
pessoasqueoestãoseguindonestaredesocialporapenasummotivo: ver
seusposts.
Nacollection Friendshipsãomantidostodososidsdosusuáriosque
estãoseguindoesendoseguidosporoutrosusuáriosdarede.Paraincremen-
tarospostsdatimelinedeumusuário,bastaapenasbuscartodososidsqueo
usuárioestiverseguindoe,emseguida,usá-lacomocondiç ãonaconsultade
posts,atravésdafun ção Post.list.Dessamaneira,osresultadossãoorde-
nadosemordemcronológicadecrescente,ouseja,doúltimoparaoprimeiro
postpublicado.
Que tal implementar essa funcionalidade? Abra o arquivo
models/friendship.js. Nele, vamos criar uma função que precisa
retornarosidsdetodososperfisqueousuárioprincipalestiverseguindo
eincluirtambémoiddousuárioprincipal. Paraessatarefa,crieafun ção
Friendship.timelineIds(), quebasicamentefiltrarátodososdocu-
mentospertencentesao userIdemparâmetro. Porém, porquestãode
performance não pegaremos todos os dados de cada documento, e sim,
somenteoatributo friendId.Useafun ção mapparatransformaroarray
dedocumentosemumarrayde friendIde,porúltimo,incluaopróprio
userIdnestemesmoarray.Vejacomoficaalógicadessecódigo:
Friendship.timelineIds = function(userId) {
var timelineIds = this.find({
userId: userId
}).map(function(f) {
return f.friendId;
});
timelineIds.push(userId);
return timelineIds;
};
Agoraquetemosessafun çãoqueretornaumarraydeidsdeusuários,
vamosusá-laparabuscarosrecentespostsdessesusuários,tornandoatime-
86

## Página 99

CasadoCódigo Capítulo8. FollowmeIwillfollowyou
linefuncionaldeverdade. Editeo models/post.jsemodifiqueafun-
ção Post.listpararetornarpostscombasenoarraydeidsdeusuários
emparâmetro( userIds),ordenandodoúltimoparaoprimeiropostpubli-
cado,etambémpornomeemordemalfabética(atravésdoatributo {sort:
{time: -1, name: 1}}),vejaabaixo:
Post.list = function(userIds) {
return this.find(
{userId: {"$in": userIds}},
{sort: {time: -1, name: 1}}
);
};
Parafinalizar,atualizealistagemdepostsnasrotas 'home'e 'user'.
Abrao client/lib/routes.jseimplementeocódigoaseguir:
Router.map(function() {
this.route(’home’, {
path: ’/’,
template: ’home’,
layoutTemplate: ’layout’,
data: function() {
var _id = Meteor.userId();
var timelineIds = Friendship.timelineIds(_id);
return {
posts: Post.list(timelineIds),
followers: Friendship.followers(_id),
followings: Friendship.followings(_id)
}
}
});
this.route(’user’, {
path: ’/user/:_id’,
template: ’user’,
layoutTemplate: ’layout’,
data: function() {
var _id = this.params._id;
var timelineIds = Friendship.timelineIds(_id);
var isFollowing = Friendship.isFollowing(_id);
87

## Página 100

8.4. Visualizandopostdequemvocêseguir CasadoCódigo
Session.set(’currentUserId’, _id);
Session.set(’isFollowing’, isFollowing);
return {
user: Meteor.users.findOne({_id: _id}),
posts: Post.list(timelineIds),
followers: Friendship.followers(_id),
followings: Friendship.followings(_id)
}
}
});
// código da rota "this.route(’follow’)"
// código da rota "this.route(’unfollow’)"
Comessecódigoimplementadocorretamente,finalizamosalistagemde
postsdatimeline.Ouseja,teremosumresultadosemelhanteaestaimagem:
Figura8.7:Timelinecompostsmultiusuários.
Parabéns! Vocêacaboudeimplementarmaisuma featurecomsucesso.
88

## Página 101

CasadoCódigo Capítulo8. FollowmeIwillfollowyou
Nopróximocapítuloexploraremosafundoaado çãodePubSubdoMeteor
paratornarnossaaplicaç ão ready for production!,nãoperca!
89

## Página 103

Capítulo9
PublicationseSubscriptions
9.1 O que é PubSub?
OPubSub(Publications and Subscriptions),paraquemnãoconhece,éum
patterncujoconceitoérealizarmensageriaatravésdedoispersonagens:um
publisher(opublicador)eum subscriber(oassinante).
Esseconceitoéutilizadoemváriostiposdeaplicações,comoporexem-
plo: newsletters,chatseleitoresdeRSS.Elefuncionadaseguintemaneira:
o publisheréoresponsávelporemitirdadosparatodososseus subscribers,
etambémum subscriberpodeenviarmensagensparao publisher,fazendo
comqueo publishertrabalhedeformamaisespecíficacomesse subscriber.
Porexemplo,emumsistemanewsletter,você,usuário,éosubscribere,para
receberatualizaçõesdesseserviço(nestecasoreceberatualizaçõesdeumpu-
blisher),vocêprecisainformarseue-mailparaqueelesaibaquemvocêé—
ouseja,enviaralgunsdadosparaopublisher,paraqueelepasseaenviaratu-

## Página 104

9.2. Entendendoseumecanismo CasadoCódigo
alizaçõesparaseue-mail.
O Meteor já vem com uma biblioteca nativa de PubSub, então
implementá-loébemtranquilo,alémdomais,éumaobrigaç ãofazerisso
paraquesejaviávelsincronizardadosentreclienteeservidoremumambi-
entedeprodução.
TrabalharcorretamentecomPubSubnoMeteorvaigarantirodesenvolvi-
mentodeumaaplicaç ãosustentável,vistoqueumaimplementaç ãomal-feita
vaitornarosistemaumacarro ça,detãolentaqueseráavelocidadenasincro-
nizaçãodosdados.Outrodetalhedeextremaimportânciaéaseguran çados
dados,poisumapublicaç ãoqueliberardadoserradosparaousuáriovaigerar
vazamentodeinformaçõesnaaplicaç ão.Porisso,pe çoqueleiaestecapítulo
comaten ção,paraaprendercomofuncionaessemecanismodoMeteor.
9.2 E ntendendo seu mecanismo
Imagineumcenárioemquenossaaplicaç ãosejaacessadapormaisde10mil
usuários.Nele,temosumusuárioqueseguemuitosusuáriospopulares,cerca
demil.Comosabemos,oobjetivodoPubSubésincronizardadosentreoser-
vidorMongoDBeoclienteMinimongo,oquefazcomqueoMeteortrafegue
apenasdadosseguindoseuprincípio data on-the wire.Essasincronizaçãose
fazatravésdoprotocoloDDP(Data Distribution Protocol ).Emresumo,este
protocoloéoquefazabibliotecaPubSubenviarereceberdadosatravésde
objetoJSONemtemporeal.
92

## Página 105

CasadoCódigo Capítulo9. PublicationseSubscriptions
Um pouco sobre DDP
UmaaplicaçãoMeteoremexecuç ãotrabalhasimultaneamentecom
doistiposdeservidores:
•Servidor HTTP:responsávelporservirconteúdoestáticoetratar
requisiçãodocliente.Internamente,eleutilizaoframeworkCon-
nect(http://www.senchalabs.org/connect)doNode.jsparareali-
zaressetrabalho.
•Servidor DDP:esteéumservidorinteiramentededicadoalidar
comPubSub,Meteor.methodsefun çõesdoMongoDB.Seumeca-
nismofuncionagraçasaoSockJS(http://sockjs.org),quetrabalha
transportandoosdadosentreoclienteeoservidoremtemporeal.
Voltandoaocenárioemquetemosumaredesocialcom10milusuários,
queremosmostrarnatimelineosúltimospostsdecadausuárioseguido,e
paraisso,omaisóbvioésincronizaros10milusuáriosentreclienteeservidor,
issoé,paracadausuáriologadonosistema.Aofazeressaprática,vocêterá
umgargalomuitograndenaaplicaç ão,vistoqueacadausuárioteremosque
carregarnoclienteosdadosde10milusuários. Esseéocomportamento
padrãodo autopublishhabilitado. Afinal,somentequemdesenvolvea
aplicaçãoconseguiráfiltrarosdadoscorretamente.
Oideal,nestecaso,épublicarapenasomontantedeusuárioscoerente
aototaldeusuáriosseguidos,fazendocomquecadaumsincronizedeforma
eficientesomenteosdadosnecessáriosparaele.
93

## Página 106

9.2. Entendendoseumecanismo CasadoCódigo
Figura9.1:Publicandosomenteonecessárioparaocliente.
Outrodetalheéquevaleapenasincronizarummontanteaceitávelde
dados,vistoquetodamanipulaç ãorealizadano client-sideseráexecutadade
94

## Página 107

CasadoCódigo Capítulo9. PublicationseSubscriptions
formarápidagraçasaosmecanismosde prefetchinge model simulationdo
Minimongo,quebasicamentefazum cachedoresultadodeumapublicaç ão,
mantendonoclienteessesosdadosparausoemanipulaç ão.
9.3 A daptando o PubSub no projeto
ParaentendernapráticaosconceitosdePubSub,realizaremosalgumasmo-
dificaçõesnoMeteorBird.
Aprimeiratarefaseráremoveropackage autopublish,afinaleledeve
serusadoapenasparaprototiparumsistema,ecomojáterminamosaproto-
tipaçãodesteprojeto,nãohámotivosdeusá-lomais.Aliás deixá-lo instalado
em ambiente de produção vai gerar uma grande brecha de seguranç a,tor-
nandopossível rodar qualquer consulta do banco de dados através do con-
sole JavaScript de um browser,ouseja,nãohámaisnecessidadedemanter
essadependêncianaaplicação,poisnãoqueremosquequalquerumfaç auma
festaindesejada,adulterandoosregistrosdobancodedadosoupiorexcluir
todososregistrosconformeaimagemabaixo:
95

## Página 108

9.3. AdaptandooPubSubnoprojeto CasadoCódigo
Figura9.2:Cuidadocomautopublish!Desinstale-oemproduç ão.
Desinstaleo autopublish:
mrt remove autopublish
ReinicieoservidorMeteor.Reparequeapósremovero autopublisha
aplicaçãovaiparardefuncionarcorretamente.
96

## Página 109

CasadoCódigo Capítulo9. PublicationseSubscriptions
Figura9.3:Ué!Porqueatimelineparoudefuncionar?.
Fiquecalmo!EsteproblemaocorreuporquenenhumPubSubfoicriado.
Antes,com autopublishhabilitado,tudoerageradoautomaticamente,e
agorateremosquecriarumPubSubparacadaconsultanobancodedados.
Primeiro, criaremos os publishers, pois estes são os principais e
mais fáceis de implementar noserver-side do sistema. Crie o código
server/publications.js, que vai conter todos publishers da aplica-
ção. Para tornar as publicações reativas, vamos englobar cada função
Meteor.publishnocallbackdafun ção Meteor.autorun,fazendocom
queaqualqueralteraç ãonosmodelosocorraum recomputationdecadapu-
blicação.
Meteor.autorun(function() {
Meteor.publish("posts", function(_id) {
var timelineIds = Friendship.timelineIds(_id);
return Post.list(timelineIds);
97

## Página 110

9.3. AdaptandooPubSubnoprojeto CasadoCódigo
});
Meteor.publish("friendship", function(_id) {
return Friendship.followersAndFollowings(_id);
});
Meteor.publish("isFollowing", function(_id) {
return Friendship.isFollowing(_id);
});
Meteor.publish("user", function(_id) {
return Meteor.users.find({_id: _id});
});
});
Repare que emMeteor.publish("friendship") estamos utili-
zandoumanovafun ção: Friendship.followersAndFollowings.Seu
objetivoéretornartodosos followerse followingsdousuário,pois
seráesteresultadoquepublicaremosdoservidorparaoclienteassinar.Para
implementá-la,editeoarquivo models/friendship.jsincluindoafun-
çãoaseguir:
Friendship.followersAndFollowings = function(_id) {
return this.find({$or: [{userId: _id}, {friendId: _id}]});
};
Já noclient-side, teremos que adaptar as funções de algumas rotas,
e para isso utilizaremos uma nova função do iron-router, chamada
de onBeforeAction. No callback desta função, incluiremos todos os
subscribesnecessáriosparaasrotas 'home'e 'user'. Aoincluiros
subscribersnecessários,algumasfunçõesdemodelosserãoexcluídasda
rota,vistoqueelasjáserãopublicadaspeloservidor—esteéocasodafun ção
Friendship.timelineIds.Editeo client/lib/routes.jsefaçaas
seguintesalterações:
Router.map(function() {
this.route(’home’, {
98

## Página 111

CasadoCódigo Capítulo9. PublicationseSubscriptions
path: ’/’,
template: ’home’,
layoutTemplate: ’layout’,
onBeforeAction: function() {
var _id = Meteor.userId();
this.subscribe("posts", _id);
this.subscribe("friendship", _id);
},
data: function() {
var _id = Meteor.userId();
return {
posts: Post.find({}),
followers: Friendship.followers(_id),
followings: Friendship.followings(_id)
}
}
});
this.route(’user’, {
path: ’/user/:_id’,
template: ’user’,
layoutTemplate: ’layout’,
onBeforeAction: function() {
var _id = this.params._id;
this.subscribe("posts", _id);
this.subscribe("friendship", _id);
this.subscribe("isFollowing", _id);
this.subscribe("user", _id);
},
data: function() {
var _id = this.params._id;
var isFollowing = Friendship.isFollowing(_id);
Session.set(’currentUserId’, _id);
Session.set(’isFollowing’, isFollowing);
return {
posts: Post.find({}),
user: Meteor.users.findOne({_id: _id}),
followers: Friendship.followers(_id),
followings: Friendship.followings(_id)
}
99

## Página 112

9.3. AdaptandooPubSubnoprojeto CasadoCódigo
}
});
// função this.route(’follow’);
// função this.route(’unfollow’);
});
Alémdaexclusãode Friendship.timelineIds,tivemosumaoutra
alteraçãodefun çõesnasrotas.Reparequeafun ção Post.listfoisubsti-
tuídapelafun ção Post.find({}).Eomaisengraç adoéqueestafun ção
nãovairetornarospostsdetodomundoesimospostsdafun ção Post.list
quefoiimplementadonapublicaç ão Meteor.publish('posts').Omo-
tivodessecomportamentoéquefun çõesdecollectionsno client-sidesempre
executarãocombasenosresultadosquereceberemdeumapublicaç ão server-
side.Istoé,jáquecriamos Meteor.publish("post")pararetornarape-
nasospostsdousuárioedequemeleestiverseguindo,aoassinaremessa
publicação,omodelo Postno client-sidesomenteteráessesdadosparama-
nipular,entãoseforusar Post.list()ou Post.find({})osresultados
serãoomesmo.
Praticamenteterminamosaprototipagemdenossoprojeto, oMeteor
Bird.Nospróximoscapítulosfocaremosemtrabalharaaplicaç ãoparacoloca-
lánoarcomqualidade,ouseja,implementaremostesteserealizaremosal-
guns tuningsparagarantirquenossaaplicaç ãofuncioneperfeitamenteem
umambientedeproduç ão.
100

## Página 113

Capítulo10
Testes,testesemaistestes
10.1 Frameworks de testes para o Meteor
Nestecapítulovamosexplorarumtemaqueémuitoimportantenãoapenas
paraoMeteor,masparaqualquerlinguagemdeprogramaç ão:vamosfalar
sobrecriaçãodetestes.
OMeteorpossuialgunsframeworkdetestes.Atualmenteexistemquatro
emdestaque: RTD, TinyT est,Mocha Webe Laika.
Essesframeworkspermitemtestarummesmotrechodecódigonocliente
enoservidor,oquefazessasferramentassetornaremtotalmenteespecíficas
paratrabalharcomoMeteor.

## Página 114

10.1. FrameworksdetestesparaoMeteor CasadoCódigo
Por que devemos criar teste de códigos
Émuitoimportantequetododesenvolvimentodeclassesoumódulos
sejaacompanhadocomseurespectivocódigodetestes.Testarumcódigo
fazcomquevocêidentifiqueecorrijadiversoserrosantesdecolocaro
novocódigonoar. Criartesteséumapráticaextremamenterecomen-
dadaeadotadapormuitasempresaseprojetosopen-source. Alémde
garantirqueseucódigofuncionarácomoesperado,issopodeinfluen-
ciarnocódigoquevocêestacriando,fazendocomquevocêidentifique
emelhoreodesigndocódigo.Outravantagemdostesteséquetornam
oprojetomaisflexívelepreparadoparamudan çasderegrasdenegó-
cio,vistoqueostestesapontarãoquaisfun çõesquebrarãoaomudartal
trechodecódigonaaplicaç ão.
Existemvárioslivrosexplicandocomoequandocriartestes,alémde
ensinartécnicasparatornarumcódigomenosacopladoefacilmentetes-
tável. NaeditoraCasadoCódigoexistemtrêslivrossobreTDD(T est-
Driven Development):
• Test-DrivenDevelopmentcomJava
http://www.casadocodigo.com.br/products/livro-tdd
• Test-DrivenDevelopmentcom.NET
http://www.casadocodigo.com.br/products/livro-tdd-dotnet
• Test-DrivenDevelopmentcomRuby
http://www.casadocodigo.com.br/products/livro-tdd-ruby
Esteslivros,porexemplo,ensinamboaspráticasdetestesumcom
aplataformaJava,umcomaplataforma.NETeumcomRuby.Apesar
deseremespecíficosparaumadeterminadalinguagem,grandepartede
seusconceitossãoaplicáveisparaqualquerlinguagemdeprogramaç ão.
102

## Página 115

CasadoCódigo Capítulo10. Testes,testesemaistestes
10.2 P rimeiros passos com Laika
OLaikaéumframeworkfácildeconfiguraredesetrabalhar.Elefoiinspirado
noframeworkMocha(http://visionmedia.github.io/mocha)doNode.js,ou
seja,eleherdoualgumascaracterísticascomocriartestesnoestiloTDD(T est-
Driven Development)ouBDD(Behavior-Driven Development),customização
do reportdostestesecriaç ãodeumarquivodeconfiguraç ão.
ParainstalaroLaika, é necessário instalar o PhatomJS primeiro,poisele
serámuitoutilizadonabateriadetestesdo client-sidedoprojeto.Parausá-lo,
recomendoqueleiaseumanualdeinstalaç ãonestelink(http://phantomjs.
org/download.html)parainstalá-lodeacordocomseusistemaoperacional.
OLaikaéummóduloNode.js,presentenositeNPM.Instale-oemmodo
globalparahabilitarseuCLI(Command Line interface),paraissoexecuteo
comando:
npm install -g laika
OLaikarodaemumainstânciadefaultdoserviçoMongoDB,ouseja,ele
vaitrabalharcomumbancodetestesseparadodobancoatualdaaplicaç ão.
Aliás,elevairodaremcimadoMongoDBdefaultinstaladoemsuamáquina.
Adicaaseguir não é obrigatória, faç a apenas se quiser e, principal-
mente, se achar necessário. ÉpossívelconfiguraroMongoDBpararodar
ostestesmaisrápidoemambientededesenvolvimento.Paraisso,finalizeo
serviçoatualdoMongoDBeinicie-outilizandoestecomando:
mongod --smallfiles --noprealloc --nojournal
Comnossoframeworkdetesteinstalado,vamoscriarosnossosprimeiros
testes. Focaremosapenasemimplementartestesparaosmodelos,poisélá
queforamcriadasasprincipaisregrasdenegóciodaaplicaç ão.
10.3 C riando testes
CriartestesnoMeteorébemdiferentedoqueemoutrastecnologiascomo
Ruby,Java,PHPouNode.js. Issoocorreporque,noMeteor,ummodelo
écompartilhadoeacessadotantonoservidorcomonocliente,eporisso,
103

## Página 116

10.3. Criandotestes CasadoCódigo
dependendodasregrasdenegócio,seránecessáriocriartestesparaverificar
comoummodelosecomportaemambososladosdaaplicaç ão.
T estando o modelo Friendship
Começando nossa codificação, vamos criar os testes para o modelo
Friendship,vistoqueelepossuimuitasfun çõesimportantesqueprecisam
sertestadas. Criaremosseurespectivotesteem tests/friendship.js,
ondetestaremosprimeiroafun ção Friendship.follow. Parasimular
esseteste,teremosqueutilizarumobjeto serverparaqueatravésdocall-
backde server.eval,omodelo Friendshiprodeafun çãodeobservaç ão
deseuestado.Nestetesteobservaremosapenasseomodelorecebeuumnovo
registro,atravésdafun ção addedecasoessafun çãosejaexecutadaelairá
emitirumeventoenviandooestadodomodeloviafun ção emit("added",
obj).Essaobservaç ãosomenteseráexecutadaquandono client-side,através
docallback client.eval,afun ção Meteor.call('followUser')for
executada.Quandooevento emit("added")foracionado,utilizaremoso
callbackde server.once("added")pararealizarosdevidostestesatravés
dasfun çõesexistentesdoobjeto assert.Notesteabaixoapenasutilizare-
mosafun ção assert.equal()paraverificarseo friendIde userId
sãodoclientequeaexecutou.
var assert = require("assert");
suite("Friendship", function() {
test("follow", function(done, server, client) {
server.eval(function() {
Friendship.find().observe({
added: function(obj) {
emit("added", obj);
}
});
});
server.once("added", function(obj) {
assert.equal(obj.friendId, "123");
104

## Página 117

CasadoCódigo Capítulo10. Testes,testesemaistestes
assert.equal(obj.userId, this.userId);
done();
});
client.eval(function() {
Meteor.call("followUser", "123");
});
});
});
Basicamente, este teste simulou um cliente rodando a função
Friendship.follow("123") que está encapsulada dentro da fun-
ção Meteor.call("followUser", "123"), afinal nesta etapa já
removemos o packageinsecure, então qualquer função de inserção,
atualizaçãoouexclusãoseráexecutadanoclientevia Meteor.call.
Implementarotestedafun ção Friendship.unfollowéumpouco
parecidocomaanterior.Adiferen çaéqueprimeiroteremosqueregistrarum
followe,emseguida,fazerum unfollowdomesmo userId,paradepois
observarsenomodelo Friendshiphouveumaexclusãodesseregistro.O
códigoaseguirexemplificanapráticaesseteste:
var assert = require("assert");
suite("Friendship", function() {
// Código: test("follow")...
test("unfollow", function(done, server, client) {
server.eval(function() {
Friendship.find().observe({
removed: function(obj) {
emit("removed", obj);
}
});
});
server.once("removed", function(obj) {
assert.equal(obj.friendId, "A");
105

## Página 118

10.3. Criandotestes CasadoCódigo
assert.equal(obj.userId, this.userId);
done();
});
client.eval(function() {
Meteor.call("followUser", "A", function() {
Meteor.call("unfollowUser", "A");
});
});
});
});
Ecomofazparatestarafun ção Frienship.isFollowing()? Essa
émaissimples:faremosum followcom userIdválidoevamosrodara
função Frienship.isFollowingduasvezes,umacom userIdutilizado
pelo followeum userIdinexistente.Nofinal,checaremosseumobjeto
existeeseooutronãoexiste.
var assert = require("assert");
suite("Friendship", function() {
// Código: test("follow")...
// Código: test("unfollow")...
test("isFollowing", function(done, server, client) {
server.eval(function() {
Friendship.find().observe({
added: function(obj) {
var obj1 = Friendship.isFollowing("123");
var obj2 = Friendship.isFollowing("321");
emit("check", obj1, obj2);
}
});
});
server.once("check", function(obj1, obj2) {
assert.notEqual(obj1, undefined);
assert.equal(obj2, undefined);
106

## Página 119

CasadoCódigo Capítulo10. Testes,testesemaistestes
done();
});
client.eval(function() {
Meteor.call("followUser", "123");
});
});
});
Outro teste que vale a pena implementar é para a função
Friendship.timelineIds. Suaregraéretornartodosos friendIds
de um userId incluindo também o própriouserId no array. Para
simular esse teste, o cliente terá que seguir dois usuários"A" e "B".
No servidor, deixaremos o modeloFriendship observando via fun-
ção Friendship.find().observe() cada novo registro através do
evento addedAt. Esteéumeventomaisprecisodoqueo added,pois
emseucallbackeleretornaoobjetocadastrado, seuíndicederegistro(
index)etambémumobjetoanterioraele( before). Comisso,faremos
com que o servidor emita o eventoemit('timelineIds') somente
seo indexforiguala1, ouseja, somentesejáexistirem2registrosde
Meteor.call("followUser") na base, assim poderemos executar
a função Friendship.timelineIds e realizar os testes em cima do
resultadodessafun ção.
var assert = require("assert");
suite("Friendship", function() {
// Código: test("follow")...
// Código: test("unfollow")...
// Código: test("isFollowing")...
test("timelineIds", function(done, server, client) {
server.eval(function() {
Friendship.find().observe({
addedAt: function(obj, index, before) {
if (index == 1) {
var ids = Friendship.timelineIds(this.userId);
emit(’timelineIds’, ids);
107

## Página 120

10.3. Criandotestes CasadoCódigo
}
}
});
});
server.once(’timelineIds’, function(ids) {
assert.equal(ids.length, 3);
assert.equal(ids[0], "A");
assert.equal(ids[1], "B");
assert.equal(ids[3], this.userId);
done();
});
client.eval(function() {
Meteor.call("followUser", "A", function() {
Meteor.call("followUser", "B");
});
});
});
});
Ok!Játemostestessuficientesparaomodelo Friendship,quetalrodá-
losparaveroqueacontece?Executeocomandoaseguir:
laika tests
Setudodercerto,vocêveráoresultadodostestessemelhanteàimagem:
108

## Página 121

CasadoCódigo Capítulo10. Testes,testesemaistestes
Figura10.1:ResultadosdostestesnomodeloFriendship.
10.4 D esafio:testar o modelo Post
Basicamenteforamexplicadasasfun çõesnecessáriasdoLaikaeMongoDB
suficientesparasecriartestesnomodelo friendship.js.
Como lição de casa, ofereço um desafio! Você terá que criar testes
paraomodelo post.js. Desenvolvaostestesemcimadas2fun ções:
Post.liste Post.publish. Paraisso,desenvolvaostestesnoarquivo
em tests/post.jsemãosnamassa!
Obs.:Sevocêestivercomproblemas,participedogrupodestelivroenvi-
andosuasdúvidasatravésdesselink:
https://groups.google.com/forum/#!forum/livro-meteor
Casoqueiravercomoficaotestemínimodestemodelo,vocêpodevisu-
alizarocódigo-fontedessetesteatravésdesselink:
https://github.com/caio-ribeiro-pereira/meteor-bird/blob/master/tests/
post.js
Boasortenodesafioecontinuelendo,poisaindatemmuitocaminhopela
frente!
109

## Página 123

Capítulo11
IntegraçãocontínuanoMeteor
Nocapítuloanterior,aprendemosoquãoimportanteécriartestes.Criarmos
napráticatestesunitáriosnasfunçõesdosmodelosdanossaaplicaç ão,etudo
issofoiapresentadoexplorandoasfuncionalidadesdoframework:Laika.
Nestecapítulovamosincrementarnossoprojeto,adicionando-oaumser-
viçodeintegraç ãocontínua,noqualdeixaremosautomáticaaexecuç ãodos
testesunitáriostodavezqueenviarmosumnovo commitparaesteprojeto.
Oobjetivodestecapítuloéapenasexplicarcomoconfigurarumambiente
deintegraçãocontínuautilizandooMeteor. Utilizaremoscomoexemploo
serviçoTravis-CI(http://travis-ci.com),porémasdicastambémservemem
outrosserviçosdeintegraç ãocontínua.
OTravis-CIéumserviçoonlinegratuitoapenaspararepositóriospúbli-
cos.Emcasosderepositóriosprivados,énecessáriodesembolsarumagrana
paratanto.

## Página 124

11.1. RodandoMeteornoTravis-CI CasadoCódigo
Comonossoprojetoseráapenasparafinseducativos,vamoshospedá-
loemumrepositóriopúblico,porexemplo,emumrepositóriopúblicodo
Github(http://github.com).
11.1 Rodando Meteor no Travis-CI
ConfigurarumaaplicaçãoMeteornoTravis-CIrequeralgunsparâmetrosadi-
cionaisnoarquivo .travis.yml,masnãoénadacomplexo. Acome çar,
vocêvaiconfigurá-locomo language: node_js(Node.jscomolingua-
gemdeprogramação), service: mongodb(MongoDBcomoserviço).Até
aítudobem,nãohásegredo!MascomoéqueoTravis-CIvaiinstalaroMe-
teor,Meteorite,Laikaenofinalrodarostestes?
Nestecaso,seránecessárioincluirumscriptadicionaldentrodocampo
before_install. Este script será baixado viacurl e executado via
/bin/sh(ambiente bash script). ElevaibaixareinstalaroMeteor,Mete-
orite,Laikae,parafinalizar,executartodosostestesdaaplicaç ão.
Jav aScript e Node.js no Travis-CI
NadocumentaçãooficialdoTravis-CI,existeumartigoexplicando
algunstiposdeconfiguraçõesparaNode.js. Entreeles,existeummo-
deloprontopararodarumprojetoMeteorexecutandotestesviamódulo
Laika.ParaconheceroutrasconfiguraçõesparaambienteJavaScriptou
Node.js,vejaestelink:
http://docs.travis-ci.com/pt-BR/user/languages/
javascript-with-nodejs
Configurando o Travis-CI
Emnossoprojeto,faremosumapequenaalteraç ão,eorestoserãoapenas
configuraçõesnoserviçosTravis-CIeGithub(OTravis-CIjápossuisignin
diretodeumacontaGithub). Nodiretórioraizdoprojeto,crieoarquivo
.travis.ymlcontendooseguintecódigo:
language: node_js
112

## Página 125

CasadoCódigo Capítulo11. IntegraçãocontínuanoMeteor
node_js:
- "0.10"
before_install:
- "curl -L http://git.io/3l-rRA | /bin/sh"
services:
- mongodb
Obs.:aURLhttp://git.io/3l-rRAutilizadaparaprepararoambienteéape-
nasumaURLencurtadaquedireciona-separaoendere ço:
https://raw.github.com/arunoda/travis-ci-laika/master/configure.sh
Eoarquivo configure.sh,internamente,visaainstalaroMeteor,Me-
teoriteeLaikanoTravis-CI,ouseja,emcódigo,estescriptbasicamenteexe-
cutaosseguintescomandos:
#!/bin/sh
#configuring the system
wget
https://raw.github.com/arunoda/travis-ci-laika/master/Makefile
#install meteor
curl https://install.meteor.com | /bin/sh
#installing meteorite
npm install -g meteorite
#installing laika
npm install -g laika
AgoranosrestacadastrarumacontanoGithube,emseguida,noTravis-
CI. Você também pode utilizar uma conta existente.
Atenção: não entrarei em detalhes técnicos, visto que esses servi ços
com o passar do tempo podem mudar seus meios de interatividades e tam-
bém suas interfaces visuais.
Masbasicamente,vocêteráquefazerasseguintestarefas:
1) CriarumrepositórionoGithub;
113

## Página 126

11.1. RodandoMeteornoTravis-CI CasadoCódigo
2) Fazer umcommitdo código-fonte do Meteor Bird para o repositório
Github;
3) AssociarsuacontaGithubnoTravis-CI;
4) AdicionarorepositóriodoprojetonoTravis-CIparaeleexecutarostestes
duranteo build;
Comessastarefasfeitas,obuildestarápreparadoparaaç ão,executando
todosostestesunitáriosacadanovocommitqueforenviadoparaoreposi-
tóriodoprojeto.
Figura11.1:RepositórioGithubdoMeteorBird.
114

## Página 127

CasadoCódigo Capítulo11. IntegraçãocontínuanoMeteor
Figura11.2:RodandobuildnoTravis-CI.
115

## Página 128

11.1. RodandoMeteornoTravis-CI CasadoCódigo
Figura11.3:Obuildpassou!
116

## Página 129

Capítulo12
Preparandoparaprodução
Sevocêchegouatéestecapítuloeconseguiucriarumaaplicaç ãofuncionale
comtestes,meusparabéns: vocêaprendeuosprincípioseboaspráticasdo
frameworkMeteor!
Nestecapítulovamosaprofundaremconhecimentosavan çados,imple-
mentandonoprojetoalgunsdetalhesimportantesparadeixá-lo ready for pro-
duction.Naprática,vamosfocarnasseguintestarefas:
• Configurarlogsparamonitoraralgunspontosdaaplicação;
• Habilitarcachenosarquivosestáticos;
• UtilizaropackageFastRenderparacarregartemplatesmaisrápido;
• OtimizarleituranoMongoDBusandoopackageFind-Faster;
• Trabalharcomvariáveisdeambientenoprojeto.

## Página 130

12.1. Monitorandoaaplicaçãoatravésdelogs CasadoCódigo
12.1 M onitorando a aplicação através de logs
Paramonitorarosistemaatravésde logging,primeirotemosqueconfigurar
ospontosimportantesdoprojetopararegistrarumlogdoestadodosdados.
Atualmente,nãoexistenenhumpackagecompatívelcomMeteor,massim
diversosmódulosNode.jscompatíveis.ComoMeteoréconstruídoemcima
doNode.js,tambémtemosapossibilidadedeusarnãotodos,masamaioria
dosmódulosNode.jsexistentesnoNPM(Node Package Manager ).Maspor
quenemtodososmódulosNoderodamnoMeteor?OMeteoréumaplata-
formaquepossuiumcontextoespecífico,quetambémtrabalhafortemente
integradocombancodedadosMongoDB.ExemplosdemódulosNodeque
nãoserãocompatíveisnoMeteorsãoosmódulosdriversdebancodeda-
dos:MySQL,Redis,SQLServereoutros.Outroexemplodetiposmódulos
totalmenteincompatíveiscomMeteorsãoos web modules,responsáveispor
criarumaaplicaçãowebnoNode.js,como Express, Connect, Sails, Geddye
muitosoutrosexistentenesselink:
http://nodewebmodules.com
Defato,nãofazomenorsentidoadicionarumframeworkwebNode.js
noMeteor,vistoqueopróprioMeteoréumframeworkweb.Porisso,nem
todososmódulosNode.jsserãocompatíveisoufuncionarãocorretamente
dentrodoambienteMeteor. Dequalquerforma,paraosdemaismódulos
compatíveis(quesãomuitos!),vocêconsegueusá-losdentrodeumaaplica-
çãoMeteor,eseráestaatarefaquefaremosaqui.
118

## Página 131

CasadoCódigo Capítulo12. Preparandoparaprodução
Módulos Node.js, NPM e Meteor
MódulosNode.jsdentrodoMeteorjásãoutilizadosdesdeaversão
0.6.x.Alémdaincompatibilidadecomalgunsmódulosdevidoaocon-
textoespecíficodoMeteor,existemaisduasrestriçõesdoNPMnoMe-
teor:
1) OsmódulosNode.jssomentefuncionarãono server-sidedeumaapli-
caçãoMeteor;
2) Funçõesassíncronasprecisamseconverterparafun çõessíncronas.
Aoinstalaropackage npm, éliberadaafun ção Meteor.sync,
quepermiteexecutarfun çõesassíncronasdentrodeseucallback,
convertendo-asparaumaexecuç ãosincronizada.
Vocêpodeleroutrosdetalhessobreaintegraç ãodoNPMcomMeteor
noblogoficialdoMeteoratravésdestelink:
https://www.meteor.com/blog/2013/04/04/
meteor-060-brand-new-distribution-system-app-packages-npm-integration
Emvezdeinventararoda,vamosutilizarummóduloNode.jsparagerar
logs. MasprimeirotemosquehabilitaroNPMemnossoprojeto;paraisso
executeocomando:
mrt add npm
Comessepackageinstalado,crienodiretórioraizdoprojetooarquivo
packages.json(issomesmo!Crieo packages.jsonnopluralenãono
singular,oqueémuitocomumemprojetosNode.js.).Nestearquivo,vamos
adicionarosmódulosdoNPMparautilizarmosemnossaaplicaç ão. Para
gerarlogs,vamosusaromódulo winston,entãoediteo packages.json
incluindoestemódulodeacordocomcódigoaseguir:
{
"winston": "0.7.2"
}
119

## Página 132

12.1. Monitorandoaaplicaçãoatravésdelogs CasadoCódigo
Paraqueainstalaç ãotenhaefeito,apenasreinicieoservidorMeteor.Re-
pareque,automaticamente,osmódulosNode.jsserãoinstaladosquandose
iniciaraaplicaç ão.
Figura12.1:InstalandodependênciaNPMaoiniciaroMeteor.
Agoravamosdefinirospontosdaaplicaç ãoquevãoregistrarlogs.Você
podeescolherqualquerlocaldaaplicaç ãodesdequesejanoladodoservidor
paragerarumlog. Paraexemplificarseuuso,faremosalgumasadaptações
nos modelsdoservidorparausá-lo.
Para carregar qualquer módulo Node.js, utilize a fun ção
Meteor.require('nome_do_modulo') e será isso que faremos
parainiciarestemódulo. Pordefault, o winstongeralogsnoconsole
daaplicação,porém,emambientedeproduç ão,temosquegerarlogsem
arquivosparanãoperderasinformações. Configurá-loparagerararquivos
delogsémuitosimples,bastaadicionarum winston.transports.File
como transporte e informar o local que será criado os arquivos de log
via atributo filename. Veja em código como fazer isso, editando o
server/applications.js:
winston = Meteor.require(’winston’);
winston.add(winston.transports.File, {
filename: ’../application.log’,
maxsize: 1024
});
Meteor.startup(function() {
120

## Página 133

CasadoCódigo Capítulo12. Preparandoparaprodução
console.log("Iniciando Meteor Bird");
});
Com winstonconfigurado, vamosutilizá-loparamonitorarosmo-
delos da aplicação, primeiro fazendo umrefactoring apenas na função
Post.publishem models/post.js:
Post = new Meteor.Collection(’posts’);
Post.publish = function(message) {
var currentUser = Meteor.user();
var params = {
message: message,
time: new Date(),
userId: currentUser._id,
name: currentUser.profile.name
};
this.insert(params);
winston.info("Post.publish: ", params);
};
Em seguida, adotaremos as mesmas conven ções no código
models/friendship.js. Parasimplificaroexemplo,vamosgerarlogs
apenasnasfun ções Friendship.followe Friendship.unfollow.
Friendship = new Meteor.Collection(’friendships’);
Friendship.follow = function(friendId) {
var params = {
userId: this.userId,
friendId: friendId
};
this.insert(params);
winston.info("Friendship.follow: ", params);
};
Friendship.unfollow = function(friendId) {
var params = {
userId: this.userId,
121

## Página 134

12.2. Habilitandocacheemarquivosestáticos CasadoCódigo
friendId: friendId
};
this.remove(params);
winston.info("Friendship.unfollow: ", params);
};
Com os logs implementados, você agora poderá visualizá-
los via arquivo de log, que serão gerados no diretório
.meteor/local/build/programs/application.log.
Figura12.2:Arquivodelogsdosistema.
12.2 H abilitando cache em arquivos estáticos
Pordefault,oMeteorautomatizatodaatarefadeconcatenaç ãoeminificaç ão
decódigoJavaScripteCSSquandoaaplicaç ãoestáemambientedeproduç ão.
Issojáotimiza—emuito—avelocidadedecarregamentodosarquivosestá-
ticosdaaplicação,alémdeevitarquefaç amosessetrabalhodeautomatizaç ão
dessastarefas.Aúnicacoisaqueteremosqueimplementaréumcontrolede
cacheestáticoparagarantirumcarregamentomaisrápidodaaplicaç ãoetam-
bémevitarmúltiplasrequisiçõesnoservidorembuscadessesarquivos.
ParahabilitarocachenoMeteor,bastaincluiropackage appcache,que
éumdospackagesoficiaismantidospelo core-teamdoMeteor. Executeo
comando:
122

## Página 135

CasadoCódigo Capítulo12. Preparandoparaprodução
meteor add appcache
Feitoisso,nãosepreocupecommaisnada:opróprio appcacheseen-
carregadefazer cachingemtodooconteúdoestático.
12.3 U tilizando o Fast Render
Nestase ção,explicareiumadicarápida,porémpoderosa,cujoimpactoéau-
mentaravelocidadedarenderizaç ãodostemplates.Paraisso,vamosutilizar
umrecentepackageconhecidopelonome Fast Render.
Basicamente,esteframeworkmelhoraocarregamentoinicialdaaplica-
ção,fazendocomqueavelocidadederenderizaç ãodostemplatesseja10vezes
maisrápido,sendocomparávelaumcarregamentoSSR(Server Side Rende-
ring).Outropontoforteéqueeleéintegradoao Iron Router,tornandopos-
sívelconfigurá-lonocarregamentodasrotasdaaplicaç ão.
Instale-oatravésdocomando:
mrt add fast-render
Comonossaaplicaç ãoestatotalmenteorientadaàsrotas,vamosapenas
incluirumsimplesparâmetro( fastRender: true)nasrotasprincipais
'home'e 'user',vistoqueelassãoasúnicasrotasquecarregamtemplates.
Editeoarquivo client/lib/routes.jsefaçaasseguintesalterações:
Router.map(function() {
this.route(’home’, {
path: ’/’,
before: function() {
var _id = Meteor.userId();
this.subscribe("posts", _id);
this.subscribe("friendship", _id);
},
data: function() {
var _id = Meteor.userId();
return {
posts: Post.find({}),
followers: Friendship.followers(_id),
123

## Página 136

12.3. UtilizandooFastRender CasadoCódigo
followings: Friendship.followings(_id)
}
},
fastRender: true
});
this.route(’user’, {
path: ’/user/:_id’,
before: function() {
var _id = this.params._id;
this.subscribe("posts", _id);
this.subscribe("friendship", _id);
this.subscribe("isFollowing", _id);
this.subscribe("user", _id);
},
data: function() {
var _id = this.params._id;
var isFollowing = Friendship.isFollowing(_id);
Session.set(’currentUserId’, _id);
Session.set(’isFollowing’, isFollowing);
return {
posts: Post.find({}),
user: Meteor.users.findOne({_id: _id}),
followers: Friendship.followers(_id),
followings: Friendship.followings(_id)
}
},
fastRender: true
});
});
Comisso,játeremosumagrandemelhoriavisívelaosusuários:umau-
mentonavelocidadedocarregamentodostemplates.
124

## Página 137

CasadoCódigo Capítulo12. Preparandoparaprodução
12.4 O timizando consultas no MongoDB com
Find-Faster
DomesmocriadordoFastRender(oArunodaSusiripala-@arunoda),re-
centementeelelan çouumpackageextremamenteútil,quevisadiminuiro
tempodeleituranoMongoDBalémdereduzirousodeCPUdoservidor.
Comofunciona? OdriverMongoDButilizadopeloMeteorestaconstante-
menteconvertendoobjetosBSON(formatodeobjetosdoMongoDBseme-
lhanteaoJSONdoJavaScript)paraobjetosJSON.Estatarefaconsomemuito
aCPU,principalmentequandosuaaplicaç ãorealizarmúltiplasleiturasem
ummesmoregistro. NestecasooFind-Fasterentraemaç ão,simplesmente
fazendo cachingdessesobjetos,evitandoqueessasleiturassejamrealizadas
noMongoDB.
Parainstalá-loexecuteocomando:
mrt add find-faster
Apóssuainstalaç ão,bastasubstituirasfun ções finde findOnedo
MongoDBparaasrespectivasfun çõesdoFind-Fasterquesão findFaster
e findOneFaster.Faremosessapequenamodificaç ãonosdoismodelos.
Entãoediteo models/post.jsatualizandoafun ção Post.list.
Post = new Meteor.Collection(’posts’);
// Função: Post.publish...
Post.list = function(userIds) {
return this.findFaster(
{userId: {"$in": userIds}},
{sort: {time: -1, name: 1}}
);
};
Emseguidaediteo models/friendship.jseatualizeasfun ções:
isFollowing, timelineIdse followersAndFollowings:
Friendship = new Meteor.Collection(’friendships’);
125

## Página 138

12.5. Configurandovariáveisdeambiente CasadoCódigo
// Função: Post.follow...
// Função: Post.unfollow...
Friendship.isFollowing = function(friendId) {
return this.findOneFaster({
userId: this.userId,
friendId: friendId
});
};
Friendship.timelineIds = function(userId) {
var timelineIds = this.findFaster({
userId: userId
}).map(function(f) {
return f.friendId;
});
timelineIds.push(userId);
return timelineIds;
};
Friendship.followersAndFollowings = function(_id) {
return this.findFaster({
$or: [{userId: _id}, {friendId: _id}]
});
};
// Função: Post.followings...
// Função: Post.followers...
12.5 C onfigurando v ariáveis de ambiente
Pordefault,oMeteorreconheceeutilizaalgumasvariáveisdeambiente,que
são variáveis chaves,responsáveisporfazeraaplicaç ãoutilizarumserviço
externodoMongoDB,utilizarumdomíniopróprio,etambémumaportada
redediferentedaportapadrão.Essasvariáveis,respectivamente,sechamam
MONGO_URLe ROOT_URL(em ROOT_URLédefinidoo domínio + portada
aplicação).
Vocêmesmopodetestaragoraemseuambientededesenvolvimento,é
126

## Página 139

CasadoCódigo Capítulo12. Preparandoparaprodução
muitofácil.Primeiro,seestivercomaaplicaç ãorodando,pareoservidore,
emseguida,inicie-outilizandoocomando:
ROOT_URL=localhost:5000 meteor
Repare que dessa vez a aplicação está rodando no endereço: http://
localhost:5000
EstefoiapenasumexemplodecomoconfigurarumambientenoMeteor.
Épossívelutilizarcustomizaçõesmaisdetalhadasatravésdavariávelglobal
Meteor.settings.
Uma boa prática que podemos fazer agora é extrair as cha-
ves appId e secret do Facebook, que usamos através da função
ServiceConfiguration.configurations.insert. Para fazer essa
extração,primeirocrieoarquivo config/settings.json.Nestearquivo,
tenhaohábitodemanterasimportanteschavesecontasdeserviçosexternos
daaplicação,comoporexemploaschavesdaautenticaç ãoviaFacebook:
{
"FB_SERVICE": "facebook",
"FB_APPID": "INCLUIR APPID",
"FB_SECRET": "INCLUIR SECRET"
}
Vocêtambémpodedefinirvariáveispúblicasquesãoexpostasno client-
sidedaaplicação. Paraisto, bastaincluirsuasvariáveisdentrodachave
public,semelhanteaoquepodemosfazernocódigoaseguir:
{
"FB_APPID": "INCLUIR APPID",
"FB_SECRET": "INCLUIR SECRET",
"public": {
"FB_SERVICE": "facebook"
}
}
Dessaforma,avariável FB_SERVICEestávisíveltantonoservidorcomo
nocliente.
127

## Página 140

12.5. Configurandovariáveisdeambiente CasadoCódigo
Figura12.3:UsandoMeteor.settingsnocliente.
Depois de definir as chaves noconfig/settings.json, edite o
código server/lib/services.jsparaqueeleacesseosatributosde
Meteor.settings:
ServiceConfiguration.configurations.remove({});
ServiceConfiguration.configurations.insert({
service: Meteor.settings["FB_SERVICE"],
appId: Meteor.settings["FB_APPID"],
secret: Meteor.settings["FB_SECRET"]
});
AgoratodavezquelevantaroservidorMeteor,seránecessáriorodaro
comando:
mrt --settings config/settings.json
128

## Página 141

CasadoCódigo Capítulo12. Preparandoparaprodução
Como manter seguro o arquivo settings.json?
Manter a boa prática de guardar todas as chaves e senhas no
settings.jsongarantesuacentralizaç ãoemumúnicolugarefaci-
litaagestãodessasinformaçõesimportantesdaaplicaç ão.
T ome muito cuidado com esse arquivo!Evitedeixá-loexpostoem
ambientespúblicose,sepossível,crieestearquivonopróprioservidor
deproduçãoparaquesomenteaaplicaç ãofaçausodestearquivo.
Assimvocêevita,porexemplo,enviarestearquivoatravésdeum com-
mitparaseurepositóriopúblicodoGithub.Afinal,umrepositóriopú-
blicocomessasinformaçõesfacilitaparaqualquerusuáriomalintenci-
onadoinvadiremanipularoseusistema.
Comtodasessasalteraçõesfeitaserodandocomsucesso,játemosuma
aplicaçãoque,alémdefuncional,jáestápreparadaparaserenviadaparaum
serviçodehospedagememambientedeproduç ão.Nopróximocapítuloserão
apresentadasalgumasdicasparahospedarsuaaplicaç ãonasnuvens.
129

## Página 143

Capítulo13
Hospedandoumaaplicação
Meteor
Parabéns! Sevocêsobreviveuatéaqui,considere-seumvencedor! Afinal,
casonãotenhapercebido,vocêjádesenvolveuseuprimeiroprojetoutilizando
atecnologiaMeteor.
Parafecharcomchavedeouro,nestecapítulovamosaprenderalgumas
dicassobrecomoempacotarumprojetoMeteorparaenviá-loparaumser-
viçodehospedagemnasnuvens.
Nocapítulo2.6,foiapresentadocomohospedarumaaplicaç ãonosser-
vidoresgratuitosnosubdomíniodo meteor.com. Oambienteoferecido
porelesérecomendadoapenasparapequenasaplicaçõesouparahospedar
versõesbetas,poisessasmáquinaspossuemumprocessamentomuitofraco.
Namaioriadoscasos,orecomendadoécolocarnossaaplicaç ãoemservi-

## Página 144

13.1. ConvertendoMeteorparaNode.jscomDemeteorizer CasadoCódigo
doresmaispotentes,geralmentepagandoporserviçosdedicados,comopor
exemplo,autilizaç ãodeserviçosnasnuvensqueofere çaservidorespararo-
daraplicaçõesNode.jseMongoDB(afinal,oMeteoréconstituídoporessas
duastecnologias).
Nãoentraremosemdetalhessobrecomoutilizartecnicamenteumser-
viço cloudemuitomenosrecomendareiqualéomelhorserviçoparasehos-
pedarumaaplicaçãoMeteor.Porém,serãolistadosnofinaldestecapítulo,os
principaisserviçoscompatíveiscomMeteor.
13.1 C onvertendo Meteor para Node.js com De-
meteorizer
AlgomuitointeressantedoMeteoréquetemosaliberdadedehospedá-loem
qualquer serviço com suporte a Node.js e MongoDB.
Atualmente, é comum encontrar serviços com suporte a aplicações
Node.js,odifíciléacharumserviçoquetragaumjeitofácildefazer deploy
emumaaplicaç ãoMeteor.
Paraestecaso,podemosconverterumprojetoMeteorparaNode.jsutili-
zandoumaferramentachamada Demeteorizer.
Parainstalá-la,bastarodarocomando:
npm install -g demeteorizer
Comisso,habilitamosnoterminalumnovocomando: demeteorizer.
Sevocêjápossuiumserviçode hostcompatívelcomNode.js,simples-
menteconfigureasvaríaveisdeambiente MONGO_URLe ROOT_URL,de
acordocomosendere çosdisponibilizadospelopróprioserviçodehospeda-
gem.Seestivercomdúvidas,vejaadocumentaç ãodoserviçooupe çaajuda
àsuaequipedesuporte.
Comasvariáveisdeambienteconfiguradascorretamentenoambientede
produção,executenaraizdoprojetoocomando demeteorizer. Senão
surgirproblemas,oresultadoserásemelhanteàimagemaseguir:
132

## Página 145

CasadoCódigo Capítulo13. HospedandoumaaplicaçãoMeteor
Figura13.1:RodandoDemeteorizer.
Umapastacomnome .demeteorizedserágeradacomtodoocódigo-
fontedoprojetoemversãoNode.js. Casoqueriarodaraaplicaç ãoemsua
máquinaparaconferirseaversãoNode.jsestafuncionando,bastarodaros
seguintescomandos:
cd ./demeteorized
npm install
node main.js
Comessasdicasrealizadascorretamente,bastaenviartodooconteúdodo
diretório .demeteorizedparaoserviçodehospedageme,porfim,iniciar
oservidorNode.jsnoambientedeproduç ão,atravésdocomando:
npm install
node main.js
13.2 O nde hospedar uma aplicação Meteor?
HáváriosserviçosNode.jscomplanosgrátisepagos. Segueumalistacom
umabrevedescriç ãodealgumasplataformaspopulares:
133

## Página 146

13.2. OndehospedarumaaplicaçãoMeteor? CasadoCódigo
Figura13.2:GetupCloud
Éumserviçobrasileiro(issomesmo,temosalguémporaquiconstruindo
nuvemtambém!),suaplataforma open-sourceébaseadanoserviçoOpenShift
(http://openshift.com),infraestruturaAmazonecobran çaporhorae on-
demand.AlémderodarNode.js,tambémsuportamoutraslinguagens(Java,
PHP,Ruby,Python,Perl),frameworks(RubyonRails,CakePHP,Django,
Wordpress)ebancodedados(MySQL,PortgreSQLeMongoDB).Omaisle-
galéqueaplataformaofereceescalabilidadeautomáticaparaasaplicações,
criandoedestruindomáquinasdeacordocomovolumedeconexõessimul-
tâneas,semquevocêpreciseentenderde load balanceououtrosdetalhestéc-
nicos.
AadministraçãopodeserfeitapeloCLIatravésdocomando rhcoupelo
webadmindoprópriosite,eodeployéfeitoatravésdogit.
Asaplicaçõesrodameminstânciaschamadasde gear,queéumamáquina
nanuvem.Quandoos gearssãocriados,elesrecebemumaURLnoformato
http://nome_app-namespace.getup.io.ElespermitemincluircertificadoSSL
etambémousodeumdomíniopróprio.Oformatodepagamentoéatravés
134

## Página 147

CasadoCódigo Capítulo13. HospedandoumaaplicaçãoMeteor
depaypal,cobran çaporhoraeemreais.
Siteoficial: http://getupcloud.com
Figura13.3:Modulus
OModuluséumserviçoPaaSfocadoemNode.js.Umdosseusdiferenci-
aiséqueeletambémsuportanativamenteoMeteor.Debancodedadosvocê
terádisponívelapenasoMongoDB,ecasosuaaplicaç ãofuncioneemreal-
time,vocêpoderáusaroprotocoloWebSockets.Neleépossívelcustomizar
domínioecertificadoSSL.Aversãotrialoferece15$ decréditosparacolo-
carumaaplicaçãodepequenoporteemcimadeumservidorcom64MBde
databasee1GBde storage.
Siteoficial: https://modulus.io
Figura13.4:Heroku
135

## Página 148

13.2. OndehospedarumaaplicaçãoMeteor? CasadoCódigo
ConhecidapelosprogramadoresRuby,Java,PythoneClosure,eprinci-
palmenteoNode.js.OHerokupossuiumaCLIparaadministraç ãodeaplica-
çõeseelesoferecemgratuitamenteodomínio nome_app.herokuapp.com
aocriarumaaplicaç ão.Omaisinteressantedesseserviçoéqueelespossuem
diversos add-onsquepermitemaintegraç ãodeserviços third-partyemsua
aplicação.Umexemplodissosãoo add-onsqueseintegramcomoTwitter,
serviçosdaAmazon,serviçosdebancodedadosecache,pluginsparaserviço
demensageriaSMSemuitomais.
Nemtodosos add-onssãogratuitos,muitosdelessãooferecidoscomo
serviçosadicionaisaserempagos. Opagamentotambémé on-demand,ou
seja,vocêpagapeloqueusaroupagapelo add-onqueinstalar.
Odeployéefetuadoatravésdogitetodaaadministraç ãodaaplicaç ão
podeserfeitatantopeloseuwebadmincomopeloseuCLI,viacomando
heroku.
Siteoficial: http://heroku.com
Figura13.5:Nodejitsu
Comapropostadeumserviçodehospedagememnuvem,oNodejitsu
trazconsigodiversosmódulosparadesenvolveraplicaçõesNode.jsemsua
plataforma. Estaéumaplataforma100%Node.jsquepermitetantoahos-
pedagemdeaplicaçõesweb,comoahospedagemdemódulosprivadospara
Node.js.Possuiumadocumentaç ãobastanteclaraedidáticasobresuaAPIe
oferecegratuitamenteumdomínioparasuaaplicaç ãoatravésdosubdomínio
nome_app.nodejitsu.com. Alémdisso,tambémpossíveloredireciona-
mentodesuaaplicaç ãoparaumdomíniopróprio.
ElesoferecemsuporteaoWebSockets,suporteaosbancodedadosRedis,
CouchDBeMongoDB.Todagestãodeumaaplicaç ãoedeployéfeitaatravés
136

## Página 149

CasadoCódigo Capítulo13. HospedandoumaaplicaçãoMeteor
doseupróprioCLI,queéocomando jitsu.Esteéumserviçocloudtotal-
mentepagoededicadointeiramenteparaoNode.js—nãooferecenenhum
planogratuito.
Siteoficial: https://www.nodejitsu.com
137

## Página 151

Capítulo14
Comoorganizarumprojeto
Meteor
14.1 C onvenções de diretórios e arquivos
AlgomuitointeressantedoMeteorécomoeleestruturaeorganizaseuscódi-
gos,ouseja,suasconven çõesdediretóriosque,quandobemutilizadas,fazem
comqueosmódulossejamcarregadoscorretamenteemseusrespectivoscon-
textos.Dominaressesconceitosopouparádefuturosproblemasemrelaç ão
amódulosquenãoexecutamcorretamenteemseuprojeto.
Recomendoqueentendaosignificadodecadadiretórioetambémen-
tendasobrequetipodemódulosedevecriarneles.Vejaaseguirasprincipais
convençõesdenomesdediretóriosearquivos:
•lib:incluabibliotecasqueserãocarregadastantonoclientecomono

## Página 152

14.1. Convençõesdediretóriosearquivos CasadoCódigo
servidor.Umbomexemplosãocódigosderegrasdenegóciocompar-
tilháveisentreclienteeservidor.
•lib/environment.js:Javascriptdeconfiguraçõesgeraissobream-
biente.
•lib/methods.js:definiçõesderotinasparao Meteor.method.
•lib/external:bibliotecasexternasdeoutrosautores,exemplo:plu-
ginsdojQuery.
•models:definiçõesdemodelosquerepresentarãocollectionsdoMon-
goDB.
•client/lib:códigosespecíficosparaocliente.Todasessas libsserão
carregadasprimeiro,ouseja,antesdosdemaiscódigosdentrodapasta
client.
•client/lib/environment.js: configuraçõesdepacotesparao
cliente.
•client/lib/helpers: pasta dedicada para helpers e events dos
templates.
•client/application.js:códigodeinicializaç ãonocliente;geral-
mente,utilizam-sefun çõesde subscriptionsou rotinas internasaserem
executadascomocallbackdafun ção Meteor.startup.
•client/index.html:HTMLprincipal.
•client/index.js:Javascriptprincipalquecarregaprimeironoload
dapágina.Eletambémpodeserchamadode main.js.
•client/views/nome_do_template.html: template HTML
(mude nome_do_templateparaonomerealdotemplate).
•client/views/nome_do_template.js:códigoJavascriptparao
respectivotemplate(mude nome_do_templateparaonomerealdo
template).
140

## Página 153

CasadoCódigo Capítulo14. ComoorganizarumprojetoMeteor
•client/views/nome_do_sub_template: você também pode
criarsubtemplates,geralmenteconhecidoscomo partials,esãotrechos
detemplatesutilizadosemumoutrotemplate.
•client/stylesheets:diretórioCSS,noqualvocêpodecolocarcó-
digoCSS,LessouStylus,etodoselessãoautomaticamentecompilados
eminificados.
•client/stylesheets/application.styl: caso trabalhe com
CSSmodular,recomendoquecrieestearquivoe,dentrodele,insira
os @importdeseusmódulosdo Stylus.
•client/stylesheets/application.less:segueomesmocon-
ceitodadicaanterior,maséparaautilizaç ãodocompilador Less.
•server/application.js:códigodeinicializaç ãonoservidor;ge-
ralmente,utilizam-sefun çõesaseremexecutadascomocallbackda
função Meteor.startup.
•server/publications.js: definições de rotinas para o
Meteor.publish.
•server/lib/environment.js: configuraçõesdepacotesparao
servidor.
•packages:mantémpackagesdependentesdoprojeto,quesãoforne-
cidospeloMeteorite.
•public:pastadearquivosestáticos. Adicioneneleimagens,fontese
outrosarquivosqueserãoservidosestaticamente.
•tests:diretórioparacriaç ãodetestesunitários.Pordefault,nenhum
códigoaquiécarregadoaolevantarsuaaplicaç ãoMeteor.Estaéuma
pastadedicadaparaframeworksdetestes.
141

## Página 155

Capítulo15
Continuandoosestudos
Obrigadoporlerestelivro,paramiméumahonratê-locomoleitor! Se
vocêchegouaquiéporqueolivroacabou,eesperoterpassadoconteúdos
degrandeutilidadeparaseusestudossobreoMeteor.Comotudonomundo
daprogramaçãoestasempreevoluindo,listareialgunssitesrelevantespara
vocêcontinuarantenadonestatecnologia.
Sites, blogs, fóruns e slides
• SiteoficialMeteor—http://meteor.com
• Documentaçãooficial—http://docs.meteor.com
• Documentação não-oficial — https://github.com/oortcloud/
unofficial-meteor-faq

## Página 156

CasadoCódigo
• Atmosphere—https://atmospherejs.com
• SiteoficialNode.js—http://nodejs.org
• DocumentaçãoNode.js—http://nodejs.org/api
• SiteoficialMongoDB—https://www.mongodb.org
• DocumentaçãoMongoDB—http://docs.mongodb.org
• SQL to MongoDB —http://docs.mongodb.org/manual/reference/
sql-comparison
• Google Meteor Brasil —https://groups.google.com/forum/#!forum/
meteor-brasil
• Facebook Meteor Brasil —https://www.facebook.com/groups/
meteorbrasil
• UndergroundWebDev—http://udgwebdev.com
• NetTuts+—http://net.tutsplus.com
• MeteorHacks—http://meteorhacks.com
• Meteor,umoverviewsobreaplataforma—https://speakerdeck.com/
caioribeiropereira/meteor-um-overview-sobre-a-plataforma
• BlogManuelSchoebel—http://www.manuel-schoebel.com/blog
Eventos, screencasts, podcasts e cursos
• EventedMind—https://www.eventedmind.com
• CodersTV—http://coderstv.com
• MeteorPodcast—http://www.meteorpodcast.com
• MeetupMeteorSP—http://www.meetup.com/Meteor-Sao-Paulo
• EbookDiscoverMeteor—http://www.discovermeteor.com
144

## Página 157

CasadoCódigo Capítulo15. Continuandoosestudos
• EbookTestingMeteor—http://testingmeteor.com
Queessasreferênciassejamdegrandeutilidade. Obrigadoporlereste
livro!
145