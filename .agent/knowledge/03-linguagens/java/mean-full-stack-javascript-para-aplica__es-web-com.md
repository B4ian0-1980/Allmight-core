---json
{
  "id": "mean-full-stack-javascript-para-aplica__es-web-com",
  "title": "MEAN Full stack JavaScript para aplicações web com MongoDB, Express, Angular e Node",
  "categoria": "03-linguagens",
  "subcategoria": "java",
  "resumo": "**Arquivo Original:** `MEAN Full stack JavaScript para aplicações web com MongoDB, Express, Angular e Node.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "angular",
    "aplica",
    "com",
    "express",
    "full",
    "java",
    "javascript",
    "linguagens"
  ],
  "perguntas_tipo": [
    "Como utilizar MEAN Full stack JavaScript para aplicações web com MongoDB, Express, Angular e Node?",
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

# MEAN Full stack JavaScript para aplicações web com MongoDB, Express, Angular e Node

> **Arquivo Original:** `MEAN Full stack JavaScript para aplicações web com MongoDB, Express, Angular e Node.pdf`
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
Prefácio
ÉimpressionanteaquantidadedeconhecimentoqueoFláviocolocounesse
livro.Paramim,esseéomelhorresumodoquevocêestáporencontrarnas
próximaspáginas.
Vocêvaiaprenderumasoluçãopontaapontacompletíssimausando
JavaScriptnofront-endcomAngular,noback-endcomNodeeExpresseno
bancodedadoscomMongoDB.Masnãosó.Vocêvaivertestesdeunidadee
integraçãocontínua;vaiverbuilddefront-endcomGrunt.jseatéfazerdeploy
daaplicação.
Oconteúdomeimpressionaporquecobretodoodesenvolvimento,apre-
sentandoferramentasparatodasasetapas.Issoémuitoraroemumlivrosó.
Aomesmotempo,olivroéenxutoe na medida certa.Todooessencialestá
aqui,massempassardopontoeserextensodemais.
SevocêtrabalhacomWeb,recomendofortementeolivro.AMEANStack
comJavaScriptemtodasaspontaséinteressantíssima.Abremuitaspossibili-
dades.Masvoualémedigoquevocêvaiaprendermuitacoisaaqui,mesmose
nãoforusaralgumapartedoMEAN.Talvezsuaaplicaç ãonãoprecisedeAn-
gular;masoconhecimentodeExpresseMongopode-lheserútil.Outalvez
vocêváusaroutrobancodedados,masvaiaprendermuitodeAngular,Grunt
etestesaqui.
Conheço o Flávio há alguns anos já, trabalhando juntos na Caelum.
Seutrabalhosempreépautadopormuitaseriedade,fundamentaç ãoeuma
didáticaincrível.Sempreviissoemsuasaulasepalestras.Eagoravejoessas
boascaracterísticasaindamaisacentuadasnestelivro.Éumaexcelenteobra,
garantoquevocêvaiaproveitar.Boaleitura!
SérgioLopes
i

## Página 5

CasadoCódigo
Agradecimentos
AgradeçoaSérgioLopesporterreservadopartedoseuescassotempoparaa
leituraeelaboraçãodoprefáciodestelivro.Aproveitotambémparaagradecer
àCasadoCódigo,maisnotadamenteaoAdrianoAlmeidaeVivianMatsui
peloprofissionalismoetratodespendidosdurantetodasasetapasdecriaç ão
destelivro.
Porfim,nãopoderiadeixardeagradeceràminhaesposaCamilaAlmeida
peloapoioduranteosnovemesesdegestaç ãodestelivro,especialmentepor
compreenderaimportânciadomeusilêncioduranteasrevisõesmatinaise
noturnasrealizadasduranteanossatravessiaNiterói/Rio.
iii 

## Página 7

CasadoCódigo Sumário
Sumário
1 Introdução 1
1.1 MEANStack . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 UmaapostanoJavaScript . . . . . . . . . . . . . . . . . . . . . 4
1.3 Vantagensdastack . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.4 Visãogeraldanossajornada . . . . . . . . . . . . . . . . . . . 6
1.5 InstalaçãodoNode.js . . . . . . . . . . . . . . . . . . . . . . . 7
2 Express:frameworkwebparaNode.js 9
2.1 Expresseseupapel . . . . . . . . . . . . . . . . . . . . . . . . 10
2.2 Estruturadoprojetoepackage.json . . . . . . . . . . . . . . . 11
2.3 InstalandooExpressatravésdoNpm . . . . . . . . . . . . . . 13
2.4 CriandoomódulodeconfiguraçãodoExpress . . . . . . . . 14
2.5 Entendendovariáveisdeambienteemiddlewares . . . . . . . 16
2.6 Viewetemplateengine . . . . . . . . . . . . . . . . . . . . . . 18
2.7 Configurandorotas . . . . . . . . . . . . . . . . . . . . . . . . 20
2.8 Criandocontrollers . . . . . . . . . . . . . . . . . . . . . . . . 21
2.9 Carregandodependênciascomexpress-load . . . . . . . . . . 25
2.10 Listandocontatos . . . . . . . . . . . . . . . . . . . . . . . . . 27
2.11 UmpoucosobreRESTAPI . . . . . . . . . . . . . . . . . . . . 31
2.12 Retornandocontatodalista . . . . . . . . . . . . . . . . . . . 32
v

## Página 8

Sumário CasadoCódigo
3 Bower:gerenciadordedependênciasfront-end 37
3.1 Instalação . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
3.2 bower.jsonenossasdependências . . . . . . . . . . . . . . . . 39
3.3 Baixandodependênciasfront-end . . . . . . . . . . . . . . . . 41
3.4 Alterandoapastadestinocom.bowerrc . . . . . . . . . . . . 42
3.5 Outroscomandos . . . . . . . . . . . . . . . . . . . . . . . . . 43
4 AngularJS:oframeworkMVCdaGoogle 47
4.1 Umvelhoconhecido:DOM . . . . . . . . . . . . . . . . . . . 48
4.2 DificuldadesquesurgemdamanipulaçãodoDOM . . . . . . 49
4.3 CaracterísticasdoAngularJS . . . . . . . . . . . . . . . . . . . 52
4.4 Preparandooambiente . . . . . . . . . . . . . . . . . . . . . . 52
4.5 HabilitandooAngularJSemnossapágina . . . . . . . . . . . 54
4.6 NossoprimeiromódulocomAngularJS . . . . . . . . . . . . 55
4.7 Angularexpression(AE) . . . . . . . . . . . . . . . . . . . . . 56
4.8 Nossoprimeirocontrolller . . . . . . . . . . . . . . . . . . . . 57
4.9 $scope:acolaentrecontrollereview . . . . . . . . . . . . . . 59
4.10 AngularJSeomodeldoMVC . . . . . . . . . . . . . . . . . . 61
4.11 Executandoaçõesnocontrolleratravésdediretiva . . . . . . 62
4.12 Amágicadodatabinding . . . . . . . . . . . . . . . . . . . . . 63
4.13 Singlepageapplication(SPA)enossoprojeto . . . . . . . . . 64
4.14 OmódulongRoute . . . . . . . . . . . . . . . . . . . . . . . . 66
4.15 Criandoviewsparciais . . . . . . . . . . . . . . . . . . . . . . 68
4.16 Configurandorotascom $routeProvider . . . . . . . . . . . . 69
4.17 Oobjeto $routeParams . . . . . . . . . . . . . . . . . . . . . . 71
4.18 Bootstrap:visualprofissionalemnossasviews . . . . . . . . . 73
4.19 Adiretivang-repeat . . . . . . . . . . . . . . . . . . . . . . . . 77
4.20 Adiretivang-modelefiltragemdalista . . . . . . . . . . . . . 80
4.21 Revisandooqueaprendemos . . . . . . . . . . . . . . . . . . 81
vi

## Página 9

CasadoCódigo Sumário
5 IntegrandoAngularJSeExpress 85
5.1 Oserviço$http. . . . . . . . . . . . . . . . . . . . . . . . . . . 85
5.2 ProgramaçãoassíncronaecallbackHELL . . . . . . . . . . . 87
5.3 Promises:combatendoocallbackHELL . . . . . . . . . . . . 90
5.4 Obtendocontatoscom $http. . . . . . . . . . . . . . . . . . . 96
5.5 OmódulongResource:trabalhandoemaltonível . . . . . . 97
5.6 ConsumindoRESTEndpointscom $resource. . . . . . . . . 98
5.7 AdicionandorotadeexclusãoaoExpress . . . . . . . . . . . . 101
5.8 Express:organizandomelhornossasrotas . . . . . . . . . . . 104
5.9 Removendocontatosdalista . . . . . . . . . . . . . . . . . . . 105
5.10 Asdiretivasng-hideeng-show . . . . . . . . . . . . . . . . . 109
5.11 Exibindocontatoselecionado . . . . . . . . . . . . . . . . . . 111
5.12 Salvandoumcontato . . . . . . . . . . . . . . . . . . . . . . . 118
5.13 AdicionandorotadegravaçãoaoExpress . . . . . . . . . . . 120
5.14 Serviços:organizandomelhornossocódigo . . . . . . . . . . 122
6 MongoDB:bancodedadosbaseadoemdocumento 125
6.1 Relacionalvs.NoSQL:hábancovencedor? . . . . . . . . . . 125
6.2 Buscandoamenorimpedânciapossível:JSON“everywhere”127
6.3 InstalaçãodoMongoDB . . . . . . . . . . . . . . . . . . . . . 128
6.4 Utilizandoomongoshell . . . . . . . . . . . . . . . . . . . . . 129
6.5 Oconceitodedocumento . . . . . . . . . . . . . . . . . . . . 129
6.6 OtipoObjectId . . . . . . . . . . . . . . . . . . . . . . . . . . 130
6.7 Criandoobancodaaplicação . . . . . . . . . . . . . . . . . . 131
6.8 Collectionseinser çãodedocumentos . . . . . . . . . . . . . 132
6.9 Buscandodocumentos . . . . . . . . . . . . . . . . . . . . . . 134
6.10 Oobjetocursor . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
6.11 Buscandocomcritério . . . . . . . . . . . . . . . . . . . . . . 138
6.12 Queryselectors. . . . . . . . . . . . . . . . . . . . . . . . . . . 142
6.13 Indexandodocumentos. . . . . . . . . . . . . . . . . . . . . . 143
6.14 Retornandodocumentosparciais . . . . . . . . . . . . . . . . 144
6.15 Removendodocumentos . . . . . . . . . . . . . . . . . . . . . 146
vii 

## Página 10

Sumário CasadoCódigo
6.16 Atualizandodocumentos. . . . . . . . . . . . . . . . . . . . . 147
6.17 Realizandoupserts. . . . . . . . . . . . . . . . . . . . . . . . . 149
6.18 $set:modificadordeatualização . . . . . . . . . . . . . . . . . 151
6.19 Documentosembutidos(EmbeddedDocuments) . . . . . . 152
6.20 SimulandoJOINSnoladodaaplicação . . . . . . . . . . . . . 154
6.21 DBRefs:databasereferences . . . . . . . . . . . . . . . . . . . 156
7 IntegrandoExpresseMongoDB 159
7.1 MongoDriver . . . . . . . . . . . . . . . . . . . . . . . . . . . 159
7.2 Esquemafazfalta? . . . . . . . . . . . . . . . . . . . . . . . . . 161
7.3 MongooseObject-DocumentModeler . . . . . . . . . . . . . 161
7.4 Gerenciandoaconexão . . . . . . . . . . . . . . . . . . . . . . 163
7.5 Criandoesquemas . . . . . . . . . . . . . . . . . . . . . . . . . 167
7.6 Utilizandomodelos . . . . . . . . . . . . . . . . . . . . . . . . 173
7.7 Buscandodocumentos . . . . . . . . . . . . . . . . . . . . . . 174
7.8 BuscandopeloID . . . . . . . . . . . . . . . . . . . . . . . . . 176
7.9 Removendodocumentos . . . . . . . . . . . . . . . . . . . . . 177
7.10 Atualizandodocumentos. . . . . . . . . . . . . . . . . . . . . 178
7.11 FunçõesdepersistêncianoModelounodocumento? . . . . 180
7.12 Criandoreferências. . . . . . . . . . . . . . . . . . . . . . . . 181
7.13 Modificandonossaviewparaexibiremergências . . . . . . . 182
7.14 Adiretivang-options . . . . . . . . . . . . . . . . . . . . . . . 183
7.15 Afunçãopopulateebuscadereferências . . . . . . . . . . . . 185
8 AutenticaçãocomPassport 187
8.1 OAuth2.0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188
8.2 Registronoprovedordeautenticação . . . . . . . . . . . . . . 189
8.3 OAuth2.0comPassport . . . . . . . . . . . . . . . . . . . . . 191
8.4 Estratégiadeautenticação . . . . . . . . . . . . . . . . . . . . 193
8.5 DefinindoSchemadoUsuário . . . . . . . . . . . . . . . . . . 195
8.6 Mongooseeplugins . . . . . . . . . . . . . . . . . . . . . . . . 196
8.7 Serializaçãoedesserializaçãodousuário . . . . . . . . . . . . 198
viii

## Página 11

CasadoCódigo Sumário
8.8 Protegendorecursos . . . . . . . . . . . . . . . . . . . . . . . . 200
8.9 Combinandoviewsdoservidor/cliente . . . . . . . . . . . . . 205
8.10 ImplementandoLogout. . . . . . . . . . . . . . . . . . . . . . 206
8.11 RESTEndpoints:permitindoapenasacessoautenticado . . . 207
9 Tornandosuaaplicaçãoaindamaissegura 211
9.1 Helmet:middlewaresdeseguran ça . . . . . . . . . . . . . . . 212
9.2 MongoDB/APIREST:evitandoqueryselectorinjection . . . 215
9.3 Evitandoodocumentreplace . . . . . . . . . . . . . . . . . . 217
9.4 Tratando404 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220
10 Grunt:automaçãodetarefasfront-end 223
10.1 Bem-vindoaoGrunt . . . . . . . . . . . . . . . . . . . . . . . 224
10.2 OarquivoGruntfile.js . . . . . . . . . . . . . . . . . . . . . . . 225
10.3 Instalandonossoprimeiroplugin . . . . . . . . . . . . . . . . 226
10.4 Tarefas. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 226
10.5 Targets. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227
10.6 Atalhoparatarefas . . . . . . . . . . . . . . . . . . . . . . . . . 229
10.7 Astécnicasdeminificaçãoeconcatenação . . . . . . . . . . . 233
10.8 grunt-usemin:minificaçãoeconcatenaçãocomGrunt . . . . 234
10.9 AstasksusemineuseminPrepare . . . . . . . . . . . . . . . . 237
10.10Angulareminificação . . . . . . . . . . . . . . . . . . . . . . . 241
11 Testandoaaplicação 243
11.1 Karma:feedbackinstantâneodetestesdeunidade . . . . . . 244
11.2 Jasmine:frameworkdeteste . . . . . . . . . . . . . . . . . . . 246
11.3 Criandosuítesdetestes . . . . . . . . . . . . . . . . . . . . . . 247
11.4 RodandosuítesdetestesatravésdoKarma . . . . . . . . . . . 248
11.5 Angular-mockseintegraçãocomJasmine . . . . . . . . . . . 250
11.6 $httpBackend:“mockando”nossobackend. . . . . . . . . . 256
11.7 Testandodepontaaponta . . . . . . . . . . . . . . . . . . . . 261
11.8 Protractor:testesend-to-endcomAngularJS . . . . . . . . . 263
11.9 ConfigurandooProtractorparaaaplicação . . . . . . . . . . 264
ix 

## Página 12

Sumário CasadoCódigo
11.10 Automatizandoaautenticaçãodousuário . . . . . . . . . . . 264
11.11 Testandocenários. . . . . . . . . . . . . . . . . . . . . . . . . 268
11.12 PageObject:melhorandoalegibilidadeemanuten çãodetestes 276
12 Integraçãocontinua 281
12.1 TravisCI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 282
12.2 Configurando.travis.yml . . . . . . . . . . . . . . . . . . . . . 283
12.3 AssociandoseurepositórioaoTravis . . . . . . . . . . . . . . 286
12.4 TaaS:testasaservicecomSauceLabs . . . . . . . . . . . . . . 289
12.5 Preparandoaaplicaçãoparadiferentesambientes . . . . . . . 290
12.6 IntegrandoTraviseSauceLabs . . . . . . . . . . . . . . . . . . 295
13 Criandosuasprópriasdiretivas 303
13.1 DDO DirectiveDefinitionObject. . . . . . . . . . . . . . . . 304
13.2 Isolandooescopodenossadiretiva . . . . . . . . . . . . . . . 307
13.3 Transclusion. . . . . . . . . . . . . . . . . . . . . . . . . . . . 312
13.4 SeparandooDDOdeseutemplate . . . . . . . . . . . . . . . 314
13.5 Maisdiretivas. . . . . . . . . . . . . . . . . . . . . . . . . . . . 316
13.6 ManipulandoDOMatravésdediretiva . . . . . . . . . . . . . 318
13.7 Afunção $watch. . . . . . . . . . . . . . . . . . . . . . . . . . 323
13.8 Trabalhandocom $broadcast. . . . . . . . . . . . . . . . . . . 325
13.9 Testandodiretivas . . . . . . . . . . . . . . . . . . . . . . . . . 327
13.10 LidandocomtemplateUrlemtestes . . . . . . . . . . . . . . . 333
14 Deploydaaplicação 339
14.1 Deploycontínuo. . . . . . . . . . . . . . . . . . . . . . . . . . 340
14.2 OpenShift:platformasaservice(PaaS) . . . . . . . . . . . . . 340
14.3 Configurandooambientededeploy . . . . . . . . . . . . . . 342
14.4 Preparandoaaplicaçãoparadeploy . . . . . . . . . . . . . . . 344
14.5 IntegrandoTraviscomOpenShift . . . . . . . . . . . . . . . . 348
14.6 Consideraçõesfinais. . . . . . . . . . . . . . . . . . . . . . . . 353
Bibliografia 355
Versão:18.0.14
x

## Página 13

Capítulo1
Introdução
“O único homem educado é o homem que aprendeu a aprender”
–CarlRogers
Algumavezvocêjáprecisou:
• Debugarsuaaplicaçãononavegador,no serverenobancodedados?
• Realizarmigrationstodavezqueseuesquemadebancomudar?
• Criarumprotótipopararápidavalidaçãocomocliente?
• Gerenciarasdependênciasdeseuprojeto,tantodoservidorquantodo
cliente?
• Automatizaroprocessodebuilddesuaaplicação?

## Página 14

1.1. MEANStack CasadoCódigo
• ConsumirREST Endpointsdiretamentena view?
• Traduzirconsultasrelacionaisemobjetoseobjetosparaomundorela-
cional?
• ManipularoDOMadicionando,removendoealterandoelementosdi-
namicamente?
• Realizartestesunitárioseend-to-end?
• Realizarodeploydaaplicação?
• Criarcomponentesreutilizáveisnaview?
Podeparecerumtantoestranhoparaquemvemprocurarrespostasem
umlivrosedepararcomumasériedeperguntaslogodeinício.
Agorapensenaslinguagenseframeworksquevocêjáutilizouparasuprir
asnecessidadeslistadas. Pensou? Vocêprovavelmentedeveterchegadoa
milhõesdeframeworksediferenteslinguagens,certo?Eseeulhedissesseque
épossívelsupri-lascomapenasumalinguagem,oumelhor,comumquarteto
quefalaamesmalíngua?Sejabem-vindoàMEANStack.
1.1 MEANStack
OacrônimoMEANfoicunhadoem2013porValeriKarpovdotimedoMon-
goDB[3]paradenotarousodeuma stackcompletaparadesenvolvimentode
aplicaçõesincluindoMongoDB,Express,AngularJSeNode.js:
(M)ongoDB
MongoDB(http://www.mongodb.org)éumpoderosobancodedados
NoSQLflexíveleescalável.Combinaahabilidadedeescalarcomosmuitos
recursospresentesnosbancosdedadosrelacionaiscomoíndices,ordenaç ão
etc.[1].
NaMEANStack,MongoDBpermitearmazenarereaverumdadoem
umformatomuitosimilaraoJSON(JavaScript Object Notation)queveremos
maisàfrente.Éumbancofracamentetipado,oqueajudamuitopoucocom
2

## Página 15

CasadoCódigo Capítulo1. Introdução
validaçãodedados,demodoqueboapartedaresponsabilidadedasregrasde
validaçãoficanasmãosdosdesenvolvedores.
(E)xpress
Express(http://expressjs.com),criadoem2009porTJHolowaychuk,
é um framework weblight-weightque ajuda na organização de sua apli-
caçãowebnaarquiteturaMVCnoladodoservidor. Vocêpodeusaruma
sériedetemplatesenginescomoejs, jade, hogan. Apesardessesengines,
naMEANStack,oExpressgeralmentedisponibilizaRESTEndpoints(http:
//pt.wikipedia.org/wiki/REST)quesãoconsumidospelostemplatesdoAn-
gularJs,queporsuavezsãoatualizadoscombasenosdadosrecebidos.
(A)ngularJS
AngularJS (http://angularjs.org/) é um framework MVC no lado do
clientevoltadopara Single Page Web Applications(SPA)criadopelaGooglee
liberadoparaopúblicoem2009.Elesimplificabastanteodesenvolvimento,
manutençãoetestes. Diferentedamaneiratradicional,naqualdadoelóg-
icasãoprocessadosnoservidor,AngularJSfacilitaorecebimentodedadose
execuçãodelógicadiretamentenocliente.
NaMEANStack,AngularJSéoresponsávelporinterfacesdinâmicassem
manipulaçãodeDOMepermiteacessarfacilmenteRESTEndpointsdireta-
mentedoclienteatravésdeserviçosespecializados.
(N)odeJs
Node.js(http://nodejs.org)éumaplataformaparaaplicaçõesJavaScript
criadaporRyanDahlsoboambientedeexecuç ãoJavaScriptdoChrome.
Épossívelutilizarbibliotecasdesenvolvidaspelacomunidadeatravésdeseu
gerenciadordepacoteschamado npm.
NaMEANStack,Node.jséacondiç ão sine qua nonparaseufunciona-
mento,ocore.
3

## Página 16

1.2. UmaapostanoJavaScript CasadoCódigo
1.2 Uma aposta no Jav aScript
MEANapostanaonipresen çadalinguagemJavaScript,oquesignificaque
acomunidadepodecontribuircomnovasstacksbaseadasemJavaScriptna
plataformaNode.jsquetornemaindamaisprodutivoedivertidoodesen-
volvimentodeaplicaçõesweb[4].Umexemplodissoéa fullstackJavaScript
Meteor(https://www.meteor.com),tambémbaseadanoNode.jsenoMon-
goDB.
1.3 Vantagens da stack
Podemosfacilmentepensarque,porutilizarmosquatrotecnologiasdistin-
tas,teremosmaistrabalhonaimplementaç ãoequeodesenvolvimentoserá
menosprodutivo,certo?Naverdade,paraprovarocontrário,Karpovutilizou
astackemcompetiçõesdeHackathon,quesãocurtascompetiçõesdepro-
gramação,provandooquantoeraprodutiva.Devidoaestaprodutividade,a
stackfoiutilizadaemumdeseusprojetoscomerciais,chamadoAscotProject
(http://www.ascotproject.com),umaferramentade image-taggingparamar-
carprodutosemfotos.Épossívelaindalistaressasvantagens:
Integraçãodaequipe
Aonipresençadalinguagemajudanaintegraç ãodaequipe:front-ende
back-endtrabalhandocomamesmalinguagem!Issodiminuio truck factor.
Debugging
Debugaraaplicaçãotorna-semaisfácilquandoosobjetosarmazena-
dosnobancodedadossãopraticamentesemelhantesaosobjetosnoladodo
cliente.Porexemplo:
// no navegador
console.log(contato)
{
"_id": "5303e0649fd139619aeb783e"
"nome": "Flávio Almeida"
}
4

## Página 17

CasadoCódigo Capítulo1. Introdução
// recebido no servidor
console.log(contato)
{
"_id": "5303e0649fd139619aeb783e"
"nome": "Flávio Almeida"
}
// buscado do banco de dados
console.log(contato)
{
"_id": ObjectId("5303e0649fd139619aeb783e")
"nome": "Flávio Almeida"
}
Reparequeoúltimoexemplodevolveum ObjectId,queveremosmaisà
frentequandoabordarmosoMongoDB.
Prototipação
Protótiposajudamavalidarideias,tomardecisõesedescobrirnovaspos-
sibilidades.ComMEAN,desenvolvedoresconseguemprotótiposrápidos,já
quedeclaramomodelocomoPOJO(Plain Old JavaScript Object )noAngu-
larJS,esteúltimoutilizadooservidorExpressapenascomopontedeacessoao
MongoDB.Aestruturadodadoenviadoésemelhantenocliente,noservidor
enobanco,oquereduzdrasticamenteotempocomconversões.
Performance
Háapossibilidade,quandonecessária,deprocessartotalmenteoupar-
cialmentedadoselógicanocliente,onerandomenososervidor.
Build,testeegerenciamentodedependências
Nãoénecessárioutilizarferramentasdebuildoudegerenciamentode
pacotesfront-endemoutraslinguagens,tudopodeserfeitocomJavaScript.
VeremoscomoutilizarGrunt(http://gruntjs.com)paraautomatizartarefase
Bower(http://bower.io)paragerenciarnossospacotesdefront-end.
5

## Página 18

1.4. Visãogeraldanossajornada CasadoCódigo
Mascomovamosjuntartodasessaspe çaseconstruiralgorapidamente?
Quaispassosseguiremos?Éoqueveremosaseguir.
1.4 Visão geral da nossa jornada
OecossistemaemtornodoJavaScriptcontinuaaevoluir. AMEANStack
éumatentativadeaproveitá-lo,masnãoéumfimemsi. Háaquelesque
utilizam-naapenasparaprototipação,outrosporcuriosidadeouemapli-
caçõescomerciais.Estelivronãosecoadunacomnenhumdessesusos:cabe
aoleitordecidircomoempregaráastack,masparaissoeleprecisaestarin-
formado.
OlivroforneceráumavisãogeraldastacknocontextodeumCRUDde
contatoschamadoContatooh.AinstalaçãodoNode.jsseránossopontode
partida.Emseguida,entraremosnoExpress4eaprenderemoscomoexpor
RESTEndpointsatravésderotas.Nestaetapa,nãoteremosintegraç ãocom
banco,apenasdadosvoláteisnamemóriadoservidorserãoretornados.
Nasequência,passaremosparaoAngularJS.Primeiro,vamosaprender
seusconceitosfundamentais,paradepoisintegrá-locomoservidorExpress,
consumindoosRESTEndpointsqueforamcriados. Aproveitaremosesta
etapaparaaplicarcomzerodeesfor çoumvisualprofissionalàaplicação
atravésdoBootstrap,concluindoainterfacedaaplicação.Todasasdependên-
ciasfront-endserãobaixadasegerenciadaspeloBower.
Depois, nolugarderetornarmoseatualizarmosdadosvoláteis, inte-
graremosnossoback-endExpresscomoMongoDBatravésdoMongoose,
umabibliotecaquereduzsignificantementeaquantidadedecódigoutilizada
nestaintegração.
AtivaremosumsistemadeautenticaçãoutilizandooprotocoloOAuth2.0,
oquepermitiráqueapenasusuáriosautenticadostenhamacessoaosistema.
Nestemomento,játeremostodasasfuncionalidadesdoprojetoprontas.
Comtodasasfuncionalidadesdoprojetoestabelecidas, automatizare-
mostarefasdeotimizaçãodaaplicaçãoatravésdoGrunt.Vamoscriartestes
unitáriosutilizandooKarma/Jasmineetestesend-to-end(e2e)comProtrac-
tor.
IntegraremosnossaaplicaçãocomoTravis,umservidordeintegraç ão
6

## Página 19

CasadoCódigo Capítulo1. Introdução
contínuagratuitoparaprojetosopensource. Inclusive,vamosaprendera
rodarnossostestes e2enanuvem,integrandooTraviscomoSauceLabs,
umTaaS( test as a service )tambémgratuitoparaprojetosopensource.Em
seguida,vamosvercomocriaretestarnossospróprioscomponentesdeview
reutilizáveisatravésdasdiretivasdoAngularJS.
Porfim,realizaremosodeploydanossaaplicaçãonoOpenShift,umPaaS
( platform as a service )quepermiteodeploygratuitoemseu public PaaS.
OdeployserárealizadopeloTravis,nossoservidordeintegraç ão,apenassea
construçãodoprojetoforbem-sucedidaesetodosostestestiverempassado;
issopermitequetenhamos,paracadacommitdaaplicaç ão,umdeploy!
Por que não usar um gerador de código?
Existemnacomunidadegeradoresquefazem scaffolddaMEANStack
queacelerambastanteotempodedesenvolvimento. Porém, oautor
preferiuconstruirastackcomoleitor,passoapasso,paraquevocêcom-
preendacadatecnologiaindividualmenteaomesmoemqueintegracada
umadelasaolongodolivro.
NãoesgotaremoscadatecnologiadacomposiçãoMEAN,masoleitorterá
abaseparaseaprofundaraindamaisemcadaumadelas.ACasadoCódigo
possuiobrasquepodemajudá-lonestatarefa:
• Aplicaçõeswebreal-timecomNode.js
• REST:ConstruaAPI’sinteligentesdemaneirasimples
Damesmamaneiraqueumprédioprecisadeumafundaç ãoantesde
serconstruído,afundaçãodonossoprojetoseráoNode.js. Veremoscomo
instalá-loaseguir.
1.5 Instalação do Node.js
AinstalaçãodoNode.jsétãosimplesquantoclicarnobotão Installemseu
website(http://nodejs.org). Onavegadorinteligentementebaixaráaversão
parasuaplataforma,sejaelaLinux,MacouWindows.
7

## Página 20

1.5. InstalaçãodoNode.js CasadoCódigo
Comoarquivodeinstalaçãoemmãos,bastaexecutá-loeseguiroassis-
tentedeinstalaçãoatéofim.Épossívelverificarsetudoocorreubemexecu-
tandonoterminalocomando node -vnalinhadecomando.
Linux eNode.js
NasdistribuiçõesUbuntuederivadas, podehaverumconflitode
nomesquandooNodeéinstaladopelo apt-get. Nestecasoespecí-
fico,nolugardobináriosechamar node,elepassaasechamar nodejs.
Seoseusistemaéumadessasdistribuições,nãosepreocupe,bastatrocar
achamada nodepor nodejs.
Setudoestiverfuncionando,seráexibidanoconsoleaversãodoNode.js
instalada:
node -v
v0.10.33
VersõesdoNode.jssuperioresa0.6.2possuemporpadrãoonpminstal-
ado,oquefacilitaaindamaissuainstalaç ão.
8

## Página 21

Capítulo2
Express:frameworkwebpara
Node.js
“Bem começado, metade feito. ”
–Aristóteles
VimosnaintroduçãoqueoExpress(http://expressjs.com)éumframework
web light-weightcriadoem2009porTJHolowaychukqueajudanaorgani-
zaçãodesuaaplicaçãoweb,naarquiteturaMVCnoladodoservidor.Quala
razãodesuaexistência,umavezqueoNode.jsjápossuiacapacidadedeservir
conteúdonaweb?Vejamosumexemploprático,massemnospreocuparmos
comocódigoporenquanto.
Crieumarquivochamado node-server.jscomoseguintecódigo:
var http = require('http');
http.createServer(function (req, res) {

## Página 22

2.1. Expresseseupapel CasadoCódigo
res.writeHead(200, {'Content-Type' : 'text/plain'});
res.end('Sou um servidor criado pelo Node.js!\n');
}).listen(3000, '127.0.0.1');
Agora,rodeoscriptnoterminalatravésdocomando node:
node node-server
Para testar, abra a URL (http://localhost:3000) em seu navegador de
preferência.Eledeveexibiramensagem:
Sou um servidor criado pelo Node.js!
Apesardefuncional,nossoservidorélimitado. Eseagoraquisermos
acessarumrecursoapartirdeumaURLdiferente?Sequisermosusartem-
plates?Alistadenecessidadespodesermaior.ÉaíqueentraoExpress.
2.1 Express e seu papel
OExpressestendeascapacidadesdoservidorpadrãodoNode.jsadicionando
middlewareseoutrascapacidadescomoviewserotas.
Middlewares
Middlewaressãofun çõesquelidamcomrequisições.Umapilhademid-
dlewarespodeseraplicadaemumamesmarequisiç ãoparaseatingirdiversas
finalidades(segurança,logging,auditoriaetc.). Cadamiddlewarepassaráo
controleparaopróximoatéquetodossejamaplicados.
Revendoocódigoanterior,substituiríamosafun çãode callbackpas-
sadaparaafun ção http.createServerporumainstânciadoExpress,que
agecomoum request listener aplicandosuapilhademiddlewares.
http.createServer('Aqui entra o Express com seus middlewares')
.listen(3000, '127.0.0.1');
10

## Página 23

CasadoCódigo Capítulo2. Express:frameworkwebparaNode.js
Express3.X eConnect
Até a versão 3.X o Express utilizava o Connect (http://www.
senchalabs.org/connect). Elefoicriadoparaestenderascapacidades
doservidorHTTPdoNode.jsprovendo middlewaresdealtaperfor-
mance.Agora,cadamiddlewaredoExpresséummóduloemseparado
queprecisaserinstaladoatravésdo npm.Comestamudan ça,cadamó-
dulopoderárecebercorre çõeseatualizaçõesseminterferirnasversões
doExpress.
AgoraqueopapeldoExpressjáfoiesclarecido,podemospartirparaa
criaçãodoprojeto.
2.2 Estrutura do projeto e package.json
Nossoprimeiropassoserácriarodiretório contatoohquerepresentanosso
projeto,inclusivecomsubpastasparaajudaraseparareagruparnossocódigo:
contatooh
app
controllers -> controladores chamados pelas rotas da
aplicação
models -> models que representam o domínio do problema
routes -> rotas da aplicação
views -> views do template engine
config -> configuração do express, banco de dados etc.
public -> todos os arquivos acessíveis diretamente pelo
navegador
Opróximopassoserácriaroarquivo package.jsonnaraizdoprojeto.
package.json
Oarquivo package.jsonpossuiinformaçõessobreoprojeto(autor,
nome,versãoetc.) eumalistacomtodasasdependênciasdanossaapli-
cação,istoé,osmódulosdequedependemos. EleutilizaaestruturaJSON
(JavaScript Object Notation)familiaraprogramadoresJavaScript.
11 

## Página 24

2.2. Estruturadoprojetoepackage.json CasadoCódigo
Poderíamosatécriarnamãooarquivo package.json,masutilizare-
mosocomando npm init:
npm init
Umassistentefaráumasériedeperguntassobreoprojeto. Podemos
dar ENTERparatodasatéqueoassistentetermine. Nofinal,teremosum
package.jsoncomonomedoprojetoigualàpastaondeexecutamoso
npm:
$ npm init
This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sane
defaults.
See `npm help json ` for definitive documentation on these fields
and exactly what they do.
Use `npm install <pkg> --save` afterwards to install a package
and save it as a dependency in the package.json file.
Press ^C at any time to quit.
name: (x)
(ENTER para todas as perguntas)
Quando o assistente chegar ao final ele terá criado o arquivo
package.joncomaseguinteestrutura:
{
"name": "contatooh",
"version": "0.0.0",
"description": "",
"main": "index.js",
"scripts": {
"test": "echo \"Error: no test specified\" && exit 1"
},
"author": "",
"license": "ISC"
}
12

## Página 25

CasadoCódigo Capítulo2. Express:frameworkwebparaNode.js
2.3 Instalando o Express através do Npm
JápodemosinstalaroExpressatravésdo npm install passandoonomedo
móduloe,opcionalmente,suaversãocom @.Emnossocaso,trabalharemos
comaversão4:
npm install express@4.8 --save
Oparâmetro --savegravaem package.jsonadependênciaesua
versão.Visualizandomaisumaveznossoarquivo,temos:
{
"name": "contatooh",
"version": "0.0.0",
"description": "",
"main": "index.js",
"scripts": {
"test": "echo \"Error: no test specified\" && exit 1"
},
"author": "",
"license": "ISC",
"dependencies": {
"express": "^4.8.4",
}
}
npm install
É altamente encorajado distribuir sua aplicação sem a pasta
node_modules e deixar que as dependências listadas no arquivo
package.jsonsejambaixadasatravésdocomando npm install.A
razãodissoéqueoNode.jspodetercompiladoalgummódulonativa-
menteparasuamáquinaeissopodenãofuncionaremoutrosistemaop-
eracional.Rodando npm install,temosagarantiadequeosmódulos
serãocompiladosnamáquinaquerodaránossaaplicação.
Reparequeaexecuçãodocomandocriouapasta node_modules.Énela
queficamtodososmódulosdequeaaplicaç ãoprecisaparafuncionar,aliás,
13 

## Página 26

2.4. CriandoomódulodeconfiguraçãodoExpress CasadoCódigo
dentrodelatemosoExpressqueacabamosdeinstalar.
AgoraquejátemosoExpressbaixado,precisamosconfigurá-lo.Faremos
issocriandoummódulodoNode.jscomessafinalidade.
2.4 Criando o módulo de configuração do Ex-
press
Vamoscriaroarquivo config/express.jsqueconteráocódigodonosso
módulodeconfiguraçãodoExpress:
// config/express.js
var express = require( 'express');
OcódigoanteriornosdáumareferênciaaomódulodoExpressatravés
dafunçãorequire.Afun ção requiretemcomotarefacarregarosmódulos
dequeprecisamosemnossoscript.
O padrão CommonJS
ONode.jsutilizaopadrão CommonJS (http://wiki.commonjs.org/
wiki/Modules/1.1)paracriaçãodemódulos.
Avariável expressarmazenaumafun çãoque,aoserchamada,retorna
umainstânciadoExpress:
// config/express.js
var express = require( 'express');
var app = express();
AtéagorasóindicamosquenossomódulodependedoExpress,porém,
aindanãoprogramamosqualquerfuncionalidade.
Aresponsabilidadedomóduloseráretornarumainstânciaconfigurada
doExpress. Destamaneira,teremosasconfiguraçõescentralizadasemum
únicoarquivo:
14

## Página 27

CasadoCódigo Capítulo2. Express:frameworkwebparaNode.js
// config/express.js
var express = require('express');
module.exports = function() {
var app = express();
return app;
};
ReparequealinhaqueinstanciaoExpressestádentrodeumafun ção
passadacomoparâmetroparaoobjeto module.exports,disponívelim-
plicitamenteemcadamódulo.Tudoqueforadicionadoemsuapropriedade
exportsestarávisívelforadomódulo; emnossocaso, oqueestaremos
disponibilizandoéumafun çãoqueaoserchamadaretornaráumainstância
doExpress.Eagora?Temosummódulo,masondeutilizá-lo?
Criandoserver.js
Vamoscriarnapastaraizdoprojetooarquivo server.js.Énestear-
quivoquesubiremososervidoratravésdoNode.jsassociando-oàinstância
doExpress:
// server.js
var http = require('http');
var app = require('./config/express')();
http.createServer(app).listen(app.get('port'), function(){
console.log('Express Server escutando na porta ' +
app.get('port'));
});
Declaramosduasdependênciasnoarquivo. Aprimeiraédomódulo
http responsável por subir nosso servidor, e a segunda, o módulo que
acabamosdecriar,comadiferen çadequepassamosocaminhodenossoar-
quivo express.jsomitindoaextensão;inclusive,porseuretornoseruma
função,usamos ()paraexecutá-la.
Afunção http.createServerrecebecomoparâmetroum request
listener. Emnossocaso,éainstânciadoExpressqueseráaplicadaao
evento requestdisparadaemcadarequisição.
15 

## Página 28

2.5. Entendendovariáveisdeambienteemiddlewares CasadoCódigo
Agorapodemosrodarnossaaplicaçãoatravésdocomando nodeseguido
donomedoscript server.js.Vocêpodeomitiraextensãosepreferir:
node server
Noterminal,seráexibidaamensagem:
Express Server escutando na porta undefined
Parando o servidor
Vocêpodepararoservidornoterminalpressionando CONTROL +
Cou COMMAND + C noMACOSX.
Reparequeoservidornãoencontrouaconfiguraç ãodaporta,porissoo
valor undefined.Nãoéapenasaconfigura çãodaportaqueestáfaltando,
faltaadicionarasconfiguraçõesmínimasparaofuncionamentodoExpress.
2.5 Entendendo v ariáveis de ambiente e middle-
w ares
PodemosagruparasconfiguraçõesdoExpressemtrêsgrupos: variáveisde
ambiente,middlewareserotas,esteúltimoveremosmaisàfrente.
Variáveisdeambiente
Variáveisdeambientesãousadasparainicializarconfiguraçõespadrões
doExpress. Vamosconfiguraraportadaaplicaç ãoqueestavafaltandono
códigoanterior:
// config/express.js
var express = require( 'express');
module.exports = function() {
var app = express();
16

## Página 29

CasadoCódigo Capítulo2. Express:frameworkwebparaNode.js
// variável de ambiente
app.set('port', 3000);
};
Adicionamosoumodificamosvariáveisdeambienteatravésdafun ção
app.set,querecebeumachaveeumvalor.Achaveéavariáveldeambiente
quequeremosmodificar,ovalor,oquedesejamosatribuiràchave.
Noexemplo,configuramosoExpressparaescutarnaporta3000.Masdo
queadiantaumservidorescutandonaporta3000seousuárionãoconsegue
acessarconteúdo?Éaíqueentranossoprimeiromiddleware.
Omiddlewareexpress.static
Precisamosfazercomqueosarquivosdentrodapasta publicsejam
acessíveispelousuárioatravésdonavegador. Realizamosestaconfiguração
através da função app.use, que recebe como parâmetro o middleware
express.static:
// config/express.js
var express = require('express');
module.exports = function() {
var app = express();
// configuração de ambiente
app.set('port', 3000);
// middleware
app.use(express.static('./public'));
return app;
};
Reparequeomiddleware express.staticrecebecomoparâmetro
nossapasta ./public.O ./referenciaapastaondenossoscriptfoiexecu-
tadopelocomando node,emnossocaso,apasta contatooh.
Agoraquejátemosnossoservidorconfiguradoparacompartilharrecur-
sosestáticos,vamoscriarapágina public/index.htmlcomumamensagem
deboas-vindas:
17 

## Página 30

2.6. Viewetemplateengine CasadoCódigo
<!-- public/index.html -->
<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<title>Bem-vindo</title>
</head>
<body>
<h1>Bem-vindo ao Contatooh</h1>
</body>
</html>
Podemossubiroservidormaisumavez:
node server
Agora,eleexibirácorretamenteamensagem:
Express Server escutando na porta 3000
BastaacessaraURL:
http://localhost:3000
Pronto!JátemosnossoservidorExpressrodandoecompartilhandopági-
nasestáticas,masnemsempreissoésuficiente.Muitasvezesprecisamosde
páginasdinâmicasconstruídasapartirdealgumdado. Éoqueveremosa
seguir.
2.6 View e template engine
Expresssuportaumagrandevariedadedetemplatesengines. Utilizaremos
oengine EJS(http://embeddedjs.com)quepossuiumasintaxesimilarao
HTML,facilitandosuaaceitaçãoentredesigners. Precisamosinstalá-lona
pastaraizdonossoprojetoatravésdo npm:
npm install ejs@0.8 --save
NoExpress,templateenginessãoconfiguradosemvariáveisdeambi-
ente.Elassãoadicionadasoualteradasatravésdafun ção app.set:
18

## Página 31

CasadoCódigo Capítulo2. Express:frameworkwebparaNode.js
// config/express.js
// abaixo do middleware express.static
app.set('view engine', 'ejs');
app.set('views','./app/views');
...
Nocódigo,primeirodizemosqueaviewengineutilizadaé ejs. Em
seguida,definimosodiretórioondeficarãonossasviews,emnossocasso,
./app/views.Tudoatravésdevariáveisdeambiente.
No lugar de escrevermos outro HTML, moveremos o arquivo
public/index.html para a pasta app/views renomeando sua ex-
tensãopara .ejs:
<!-- app/views/index.ejs -->
<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<title>Bem-vindo</title>
</head>
<body>
<h1>Bem-vindo ao Contatooh</h1>
</body>
</html>
Umtemplatenormalmentepossuilacunasqueprecisamserpreenchidas,
écomosefosseumcontrato,memorandooucartanaqualapenasalgumas
informaçõessãoalteradas,mantendo-segrandepartedodocumentooriginal.
Vamosindicarquenossaviewdependedonomedoprojetousandoasintaxe
<%=nome %>:
<h1>Bem-vindo ao <%=nome %></h1>
Pronto,mastemosumproblema.Antes,conseguíamosacessarapágina
index.htmlporqueelaestavadentrodapastapública; agora, ninguém
poderáacessarnossaview, porqueelaestáemumapastadiferente. Pre-
cisamostornarpúblicoumcaminhodeacessoparanossapáginaefazemos
issonoExpressatravésde rotas.
19 

## Página 32

2.7. Configurandorotas CasadoCódigo
2.7 Configurando rotas
Precisamosconfigurarumarotadeacessoparanossaview index.ejs.
Poderíamosfazerissodentrode express.js,jáquetemosumainstância
doExpressconfigurada,masvamosutilizarummóduloseparado,chamado
app/routes/home.js.Comoasconfiguraçõesderotassãoaplicadasdire-
tamentenainstânciadoExpress,nossomóduloprecisareceberessainstância
comoparâmetro:
// app/routes/home.js
module.exports = function(app) {
}
Express3.X e rotas
Aversão3.XdoExpressnãovemcomseumiddlewareparacontrole
derotasativadoporpadrão.Suaativaç ãoésimples:
// config/express.js
...
// necessário apenas na versão 3.X
app.use(app.router);
...
Agora,precisamosimportaromódulodentrode config/express.js
passandocomoparâmetronossainstânciaconfiguradadoExpress:
// config/express.js
...
var home = require('./app/routes/home')
...
// abaixo da configuração do último middleware
home(app);
...
20

## Página 33

CasadoCódigo Capítulo2. Express:frameworkwebparaNode.js
Já temos tudo encaixado, vamos configurar a rota através da função
app.get.Emnossocaso,queremosresponderàURL /:
// app/routes/home.js
module.exports = function(app) {
app.get('/')
}
Afunção app.getequivaleaoverbo GETdohttp,istoé,umafun ção
preparadaparalidarcomrequisiçõesdotipo GET.Veremosoutrostiposà
medidaqueprecisarmos.
Nesteexemplo,quandoousuáriodigitaraURL http://localhost:3000/o
Expressverificaráseháalgumarotaregistradacomo /eexecutaráumaação
associadaàrota.Masespere!Nãoindicamosqualcódigoseráexecutado.No
modeloMVC,esteéopapeldo controller.
2.8 Criando controllers
No modelo MVC, o controller é a ponte de ligação entre nossa página
(view) e nossos dados (model). Criaremos nosso controller no arquivo
app/controllers/home.js. Repare que ele tem o mesmo nome do
arquivoderotas, justamenteparaindicarumaligaç ãoentreambos, mas
poderíamosterescolhidooutronome.Nossoarquivoseráummódulo,com
adiferençadequenãoreceberáainstânciadoExpresscomoparâmetro.
// app/controllers/home.js
module.exports = function() {
var controller = {};
return controller;
}
Omóduloretornaumobjeto.Énelequeadicionamosumaoumaisações
quepodemserchamadasporumarotaacessadapelousuário.Vamosaplicar
umaaçãoqueseráresponsávelpeloretornodanossapágina index.ejsaté
agorainacessívelparaomundoexterno:
21 

## Página 34

2.8. Criandocontrollers CasadoCódigo
module.exports = function() {
var controller = {};
controller.index = function(req, res) {
// retorna a página index.ejs
};
return controller;
}
Adicionamos no objetocontroller a propriedadeindex, que ar-
mazenaumafun çãocomdoisparâmetros: oprimeiro,oobjetoquerepre-
sentaofluxoda requisição;osegundo,ode resposta. Éatravésdoobjeto
resqueenviaremosapágina index.ejs:
module.exports = function() {
var controller = {};
controller.index = function(req, res) {
res.render('index', {nome: 'Express'});
};
return controller;
}
Lembre-sequenãopodemosdevolverdiretamenteapágina index.ejs,
porqueelanãoestácompletaeprecisadodado nome.Éporissoqueusamos
afunção res.render.Elarecebedoisparâmetros:oprimeiroéo nomeda
viewqueseráretornadaeosegundo,um objetoJavaScriptcomdados que
seráconsumidoporestaview.
UmadúvidaquepodeapareceragoraécomooExpressencontraráoar-
quivodenossaview.Porpadrão,eleadicionaosufixo .ejs(nossotemplate
engine)aonomedoarquivo,procurando-odentrodapasta app/views.
Lembradavariáveldeambiente views?
Processandootemplateantesdoenvio
Antesdarespostaserenviada, aviewengineprocessaráotemplatee
preencheráaexpressão <%=nome %> procurandonoobjetopassadocomo
parâmetroparaafun ção res.sendapropriedade nome. Nofinal,oque
serádevolvidoparaonavegadorcomorespostaéumnovoHTMLcomaex-
pressão <%= nome %> substituídapor Express.
22

## Página 36

2.8. Criandocontrollers CasadoCódigo
Porfim,exibindoocódigo-fontenonavegador:
<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<title>Bem-vindo</title>
</head>
<body>
<h1>Bem-vindo ao Express</h1>
</body>
</html>
nodemon
Precisamosreiniciaroservidortodavezquerealizarmosalterações.
Podemosresolveresteproblemausandoo nodemon:
npm install nodemon -g
nodemon server.js
Oúnicodetalheéquesomosobrigadosainformaraextensãodoar-
quivo.
Template no lado do servidor
Reparequenossotemplateémontadoprimeironoservidoredepois
enviadoparaonavegador.Veremosalgodiferentequandotrabalhamos
comAngularJS.Nele,acomposiç ãodotemplateéfeitanonavegador,
nãonoservidor.
Vocêjádeveterreparadoque,todavezquecriarmosumarquivoderota
emseparado,eleprecisaráimportaromódulodocontrollerqueseráuti-
lizado. Aindanãotemosnenhummodelcriado;setivéssemos,eletambém
precisariaserimportado,masdentrodoarquivodocontrolller:
24

## Página 38

2.9. Carregandodependênciascomexpress-load CasadoCódigo
npm install express-load@1.1 --save
Emseguida,precisamosimportaromódulodentrodonossoarquivode
configuraçãodoExpress:
// config/express.js
var load = require('express-load');
Porfim,substituímosachamadaàfun ção home(app)pelafunçãoload:
...
load('models', {cwd: 'app'})
.then('controllers')
.then('routes')
.into(app);
return app;
A função load carregará todos os scripts dentro das pastas
app/models, app/controllerse app/routes. Nofinal, afunção
intoadicionadinamicamentenainstânciadoExpresspropriedadesque
apontamparaessesmódulos.
Ordemdecarregamento
Umpontoimportanteéqueprecisamoscarregaraspastasseguindoaor-
dem models, controllers e routes,casocontrárionãoconseguiremos,porex-
emplo,teracessoaosnossoscontrollersemnossasrotascasoosmóduloscom
nossoscontrollerstenhamsidocarregadosporúltimo.
Pastapadrão
O parâmetro {cwd: ‘app’} foi necessário para mudar o diretório
padrão,poisafun çãoprocuraaspastasnodiretórioraiz contatoohepre-
cisamosqueelaconsidereapasta contatooh/app.
26

## Página 39

CasadoCódigo Capítulo2. Express:frameworkwebparaNode.js
Modificandonossoarquivoderotas
Precisamosalterarnossoarquivo app/routes/home.js,quenãofará
maisusodafun ção requireparacarregarseucontroller. Emvezdisso,
elaprocuraráocontrollerdiretamentenainstânciadoExpresspassadacomo
parâmetro:
// app/routes/home.js
module.exports = function(app) {
var controller = app.controllers.home;
app.get('/', controller.index);
};
Podemostestaroprojetoparaverificarsetudocontinuafuncionando:
http://localhost:3000/
Até aqui entendemos como o Express funciona e como configurá-lo,
inclusiveorganizamosnossaaplicaçãoemumaestruturaquefacilitarásua
manutenção.Agoraprecisamoscriarasrotasdequenossaaplicaç ãoprecisa.
Éoqueveremosnapróximase ção.
2.10 Listando contatos
Nossoservidorprecisaretornarumalistadecontatosquemaistardeserácon-
sumidapelonossofront-endusandoAngularJs.Disponibilizaremosestere-
cursoatravésdeumidentificador. NoprotocoloHTTP,usamosURLspara
isso:
http://localhost:3000/contatos
Lembre-sequenoExpressestaURLéchamadade rota(route)eprecisa
serconfigurada.Vamoscriaroarquivo app/routes/contato.js:
// app/routes/contato.js
module.exports = function(app) {
var controller = app.controllers.contato;
app.get('/contatos', controller.listaContatos);
};
27 

## Página 40

2.10. Listandocontatos CasadoCódigo
app.use
Comovimos, app.useéusadoparaassociar middlewaresànossa
instânciadoExpress. Eletambémpodeserusadoparaativarmiddle-
waresparaumarotaespecífica.Adiferen çaéqueeleconsideraráarota
independentedoverboutilizado,sejaele GET, PUT, DELETEou POST.
app.use('/' , function(req, res, next) {
console.log('middleware A');
next();
});
app.use('/', function(req, res, next) {
console.log('middleware B');
next();
});
Estecódigoexibiránoconsoleasmensagens:
middleware A
middleware B
Repareoparâmetro next.Éumafun çãoqueaoserexecutadachama
opróximomiddlewaredapilhaparaprocessararequisiç ão.Secomen-
tarmosachamadaà next()noprimeiromiddleware,oconsoleapenas
exibiráotexto‘middlewareA’,deixandodechamaropróximodapilha.
Lembre-se que não precisamos importar o módulo dentro de
config/express, já que o express-load se encarregará de carregar
o novo script, tornando-o disponível na instância do Express como
app.controlllers.contato.
O problema é que o código anterior referencia um controller
que ainda não existe. Precisamos criá-lo, através do arquivo
app/controllers/contato.js:
// app/controllers/contato.js
module.exports = function() {
var controlller = {};
28

## Página 41

CasadoCódigo Capítulo2. Express:frameworkwebparaNode.js
controller.listaContatos = function(req, res) {
};
return controller;
};
Nossocontrollerretornaráumalistadecontatospormeiodafun çãolista-
Contatos.Porenquanto,vamosretornarumalistacriadaemmemória.Não
sepreocupe,maistarderefatoraremosnossocódigoparaqueessalistavenha
doMongoDB:
// app/controllers/contato.js
var contatos = [
{_id: 1, nome: 'Contato Exemplo 1',
email: 'cont1@empresa.com.br'},
{_id: 2, nome: 'Contato Exemplo 2',
email: 'cont2@empresa.com.br'},
{_id: 3, nome: 'Contato Exemplo 3',
email: 'cont3@empresa.com.br'}
];
module.exports = function() {
var controlller = {};
controller.listaContatos = function(req, res) {
// envia a lista
};
return controller;
};
E a sessão do usuário?
Poderíamosterarmazenadoalistanasessãodousuário,masisso
acarretarianaconfiguraçãodeoutro middleware,quenãoénossofoco
agoraequeconfiguraremosmaisàfrente. Porenquanto,nãoestamos
preocupamossetodososusuáriosterãoacessoàmesmalista.
29 

## Página 42

2.10. Listandocontatos CasadoCódigo
Nossocontrollerestáquasepronto,faltaretornaralistadecontatos.
res.json
DiferentedocontrollerdahomequedevolveumapáginaHTMLdinami-
camentegeradapeloservidor,destavezretornaremosumalistadedadosno
formatoJSON,quemaistardeseráconsumidanoladodoclienteatravésdo
AngularJS.
OExpresspossuiafun ção res.jsonespecializadanoenviodestetipo
dedado:
...
module.exports = function() {
var controlller = {};
controller.listaContatos = function(req, res) {
res.json(contatos);
};
return controller;
};
Acessandooendere ço(http://localhost:3000/contatos)emnossonaveg-
ador,nossalistaéexibidanoseguinteformato:
[
{"_id":1,"nome":"Contato Exemplo 1",
"email":"cont1@empresa.com.br"},
{"_id":2,"nome":"Contato Exemplo 2",
"email":"cont2@empresa.com.br"},
{"_id":3,"nome":"Contato Exemplo 3",
"email":"cont3@empresa.com.br"}
]
30

## Página 43

CasadoCódigo Capítulo2. Express:frameworkwebparaNode.js
res.json vs. res.send
Deacordocomadocumentaç ãodoExpress, res.jsonéidên-
ticoa res.sendquandoumobjetoouarrayépassado. Adiferen ça
équeoprimeiroexplicitamenteconvertetiposnão-objetocomo null
e undefined.Usamos res.jsontambémparadeixarclaranossain-
tençãodetrabalharcomestetipodedado.
Precisamoscriaragoraumrecursoquepermitaretornarapenasumcon-
tatodadoseuidentificador.Algumasugestãodenome?Deveterpassadoem
suacabeçaváriosnomes,maspodemosadotarumpadrãoqueajudaráauni-
formizarnossasregrasdedefiniçãoderecurso.Estepadrãosechama REST.
2.11 Um pouco sobre RESTAPI
OacrônimoREST(Representational State Transfer )foicriadoporRoyField-
ing,umdosprincipaiscriadoresdoprotocoloHTTP.Eledefineumconjunto
deoperaçõesaplicáveisatodososrecursosdeinformaçãoutilizandoopro-
tocoloHTTP.Asoperaçõesmaisutilizadassão DELETE, GET, POSTe PUT.
EmREST,cadarecursodeveterumidentificadorúnico,oqueemHTTPé
suaURLdeacesso.
TrazendoessadefiniçãodoRESTparanossoservidorExpress, temos
alémdafunção app.getasfunçõesapp.delete,app.puteapp.post,cada
umacorrespondendoaumverboHTTPutilizadopelopadrãoREST,inclu-
sivesomoscapazesdecriarURLsúnicasemnossasrotas,quenadamaissão
doqueidentificadoresúnicos.
Para saber mais
VocêpodequererseaprofundarnaAPIREST,quevaimuitoalém
dadefiniçãodenomederecursos. Vocêpodeconsultarolivro REST:
ConstruaAPI’sinteligentesdemaneirasimplestambémdisponívelna
CasadoCódigo.
31 

## Página 44

2.12. Retornandocontatodalista CasadoCódigo
Játemosconfiguradaarota /contatos,masprecisamoscriaroutrapara
acessarumcontatoindividualmente.Eseeutedissessequepodemosusara
“mesma”URL/contatos.Confuso?Nãosepreocupe,éoqueveremosa
seguir.
2.12 Retornando contato da lista
Imaginequeparaobterumcontatovocêtenhaquepassarpelalistadecon-
tatos,comadiferen çadequeestáinteressadoapenasnocontatocomdeter-
minadoidentificador.Sendoassim,umaURLcondizentecomessaideiaseria
/contatos/1.Sequiséssemosocontatocomidentificador30,acessaríamos
aURL /contatos/30.
EssamaneiraéperfeitamenteaceitadentrodopadrãoREST,oproblemaé
queteríamosqueconfigurarumarotaparacadacontatocadastradoemnosso
sistema,algoimpraticável.
Parasolucionaresteproblema,oExpresspermiteregistrarrotasseguindo
estepadrãoutilizandoumcuringanolugardoidentificadordorecursocomo
/contatos/:id.Adicionandoarotaem app/routes/contato.js:
// app/routes/contato.js
...
module.exports = function(app) {
var controller = app.controllers.contato;
app.get('/contatos', controller.listaContatos);
app.get('/contatos/:id', controller.obtemContato);
};
IstosignificaqueURLscomo(http://localhost:3000/contatos/2)nãodis-
pararãoarota /contatos, masaquelacomocuringa. Maisqueisso,
aindaserápossívelcapturarnocontroladoroparâmetropassadoatravésde
req.params.id. Nestecaso, idéonomedocuringautilizadonarota.
Adicionandoanovaaçãoem app/controllers/contato.js:
// app/controllers/contato.js
...
controller.obtemContato = function(req, res) {
32

## Página 45

CasadoCódigo Capítulo2. Express:frameworkwebparaNode.js
console.log(req.params.id);
};
...
Agora,sóprecisamoscriarnossalógicaquedevolveocontatocomoid
enviadocomoparâmetro.Umaimplementaçãopossíveléaseguinte:
controller.obtemContato = function(req, res) {
var idContato = req.params.id;
var contato = contatos.filter(function(contato) {
return contato._id == idContato;
})[0];
contato ?
res.json(contato) :
res.status(404).send('Contato não encontrado');
};
Nessecódigo,quandoumcontatonãoéencontrado,alteramosostatus
darespostapara404(nãoencontrado)atravésdafun ção res.statuseen-
viamoscomorespostaumamensagemcomumapistadoproblemaocorrido.
Jápodemostestar:
http://localhost:3000/contatos/2
SeráexibidononavegadoroJSON:
{"_id":2,"nome":"Contato Exemplo 2",
"email":"cont2@empresa.com.br"}
ConsideraçãosobreosverbosDELETEePUT
Nemtodososnavegadoressuportamosverbos DELETEe PUT,inclusive,
háredesquefiltramrequisiçõesdestestipos.Umasoluçãoempregadaéusar
overbo POST,masadicionandono headerdarequisiçãoo Content-type
X-HTTP-Method-Override.Nele,informamosqualverbopretendemosuti-
lizar,porexemplo, DELETE.Oservidorprecisaestarpreparadoparaextrair
estainformaçãoechamararotaparaotipodeverbodesejado.
33 

## Página 46

2.12. Retornandocontatodalista CasadoCódigo
No Express, usamos o middlewaremethod-override (http://https://
github.com/expressjs/method-override)quecuidaráautomaticamentedeste
processoparanós,garantindoqueasrotasparaosverbossejamchamadas
corretamente. Para funcionar, ele depende de que a requisição seja
parseadaatravésdomiddleware body-parser(https://github.com/expressjs/
body-parser).Esteúltimopopula req.bodycomosparâmetrosdo POST.
Ambossãoinstaladosatravésdo npmexecutando-odentrodapastaraiz
doprojeto:
npm install body-parser@1.6 method-override@2.1 --save
Porfim,precisamosativaressesmiddlewaresnaconfiguraçãodoExpress:
// config/express.js
...
var bodyParser = require('body-parser');
...
// middleware
app.use(express.static('./public'));
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());
app.use(require('method-override')())
...
Repare no código anterior que estamos solicitando ao
bodyParser que realize o parse dejson e requisições com o corpo
x-ww-form-urlencoded. Isso permite acessar os dados da requisição
atravésde req.body,algoqueveremosnapráticamaistarde.
34

## Página 47

CasadoCódigo Capítulo2. Express:frameworkwebparaNode.js
urlencoded extended
Asprimeirasversõesdo body-parserparaExpress4adotavam
como padrão da chaveextendedo valor trueque utiliza como
parserabiblioteca qs. Porém, quandofalse, utilizaabiblioteca
querystring.Asversõesmaisrecentesdo middlewareimprimirão
noconsoleumamensagemdeavisosolicitandoaescolhadabiblioteca,
algoquepodemosresolverpassandoparaachave trueou false.Out-
rosmiddlewaresdoExpresstambémestãodeixandodeassumirvalores
padrões,inicialmenteexibindoapenasumavisodequenofuturoovalor
padrãonãoserámaissuportado.
Express3.x, body-parser e method-override
Até a versão 3.X, o Express herdava body-parser e
method-overridedoConnecteeramativadosdaseguintemaneira:
app.use(express.methodOverride());
app.use(express.bodyParser());
Repare que não era necessário indicar o parser dejson nem
urlencoded.Opadrãoeraparaambos,porémmuitosdesenvolvedores
achavamqueelesuportavamaiscoisascom multipart,oquenãoera
verdade.
Agora que nosso servidor lista e retorna contatos individualmente,
podemos dar uma pausa noserver-side e focar nossa atenção no
client-side.Oprimeiropassoseráobternossasbibliotecasfront-end.
35 

## Página 49

Capítulo3
Bower:gerenciadorde
dependênciasfront-end
“O homem realmente culto não se envergonha de fazer perguntas também aos
menos instruídos. ”
–Lao-tsé
Quantasvezesvocêjáprecisouabrirseunavegadorparaprocuraralguma
bibliotecafront-endparadepoisbaixá-la?Quantotempogastouparaachar
olinkdedownloadnosite?Eraaversãoquevocêqueria?Salvouoarquivo
nodiretóriocorretonoseuprojeto?Equandoprecisouatualizarabiblioteca?
Repetiuomesmociclo? Fezamesmacoisacomtodasasoutrasbibliotecas
dasuaaplicação? Resolveuconflitos? Eseeulhedissessequenãoprecisa
serassim? FoipensandoemquestõescomoessasqueaequipedoTwitter

## Página 50

3.1. Instalação CasadoCódigo
(https://twitter.com)criouumgerenciadordepacotesvoltadoparafront-end
chamadoBower.
O Bower (http://bower.io) é um gerenciador de pacotes para web
voltadoparafront-end querealizagrandepartedastarefasquefaríamos
manualmente,inclusivegerenciaasdependênciasdesuaaplicaç ão. Outro
pontointeressanteéqueelenãogerenciapacotesexclusivamenteJavaScript,
mastambémCSSeHTML.
Bower vs. npm
PodemoscompararoBowercom npm,comadiferen çadequeo
primeiroévoltadoparapacotesfront-endeosegundoparapacotesback-
end,apesardealgunsdesenvolvedorestentaremutilizaro npmparaas
duasfinalidades.
Faz todo sentido incluirmos o Bower dentro da MEAN Stack já que
elenadamaisédoqueummódulodoNode.js. Veremosaseguircomo
configurá-lo.
3.1 Instalação
SendoummódulodoNode.js,ainstalaç ãodoBoweréfeitaatravésdo npm:
npm install bower@1.3 -g
Oparâmetro -gtornaomóduloacessívelemqualquerlocalemnosso
terminal,istoé,globalmente. Issofaztodosentido,jáquequeremosbaixar
nossasdependênciasaqualquermomentoemqualquerumdenossosproje-
tos.
npm e o parâmetro -g
Paraqueoparâmetro -gfuncione,vocêprecisaterpermissãode
administrador,casocontrárioainstalaçãofalhará.
38

## Página 51

CasadoCódigo Capítulo3. Bower:gerenciadordedependênciasfront-end
PodemostestarainstalaçãodoBoweratravésdocomando bower:
$ bower
Usage:
bower <command> [<args>] [<options>]
Commands:
(exibe uma lista com todos os comandos possíveis)
Ocomandoanteriorexibiráumalistacomváriosparâmetrosquepodem
serutilizados.Focaremosnosmaisutilizados,masprimeiro,precisamosini-
cializaroBoweremnossoprojeto.Éoqueveremosaseguir.
3.2 bower.json e nossas dependências
PoderíamosjácomeçarautilizaroBowerparabaixarnossasdependências,
masqueremosquetodasfiquemlistadasemumarquivo,algosemelhanteao
quefizemoscomoarquivo package.json,queguardaonomeeaversão
dosmódulosutilizadospelonossoservidor.
No Bower, o arquivo que lista nossas dependências é chamado
bower.json.Dentrodapastaraizdoprojeto,elepodesercriadopeloco-
mando bower init:
$ bower init
[?] name: contatooh
[?] version: 0.0.0
[?] description:
[?] main file:
[?] what types of modules does this package expose?
[?] keywords:
[?] authors: flaviohenriquealmeida
[?] license: MIT
[?] homepage:
[?] set currently installed components as dependencies? Yes
[?] add commonly ignored files to ignore list? Yes
[?] would you like to mark this package as private which
39 

## Página 52

3.2. bower.jsonenossasdependências CasadoCódigo
prevents it from being
[?] would you like to mark this package as private which
prevents it from being
accidentally published to the registry? Yes
{
name: 'contatooh',
version: '0.0.0',
authors: [
'flaviohenriquealmeida <flaviohenriquealmeida@gmail.com>'
],
license: 'MIT',
private: true,
ignore: [
'**/.*',
'node_modules',
'bower_components',
'test',
'tests'
]
}
[?] Looks good? (Y/n)
Oarquivofaráumasériedeperguntascomoonomedoprojetoeasua
versão. Podemosdar ENTERparatodasasperguntas,masvaleoesclareci-
mentodealgumasdelas:
•Whattypesofmodulesdoesthispackageexpose? (Qualtipodemó-
duloestepacoteexpõe?):comoBower,tambémpodemoscriarpacotes
comomódulosquepodemserconsumidosporoutrasaplicações.No
universoJavaScript,existemalgunsformatosparacriaçãodemódulos.
OBowerdesejasaberqualformatoseupacoteutilizaráparadaruma
pistaparaaquelesqueoforemutilizar.Comonossaaplicaç ãonãoserá
umpacote,podemosdar ENTERparaestapergunta.
•Setcurrentlyinstalledcomponentsasdependencies? (Adicionaros
componentesjáinstaladoscomodependências?):podeserquevocêjá
40

## Página 53

CasadoCódigo Capítulo3. Bower:gerenciadordedependênciasfront-end
tenhabaixadopacotesantesdecriaro bower.jsoneoBowerfornece
aopçãodeincluirnoarquivoospacotesjábaixados.
•Wouldyouliketomarkthispackageasprivatewhichpreventsit
frombeingaccidentallypublishedtotheregistry? (Vocêgostariade
marcarestepacotecomoprivado,oqueevitaráqueelesejaacidental-
mentepublicadonoregistro?):estaémaisumaop çãoquesófazsentido
casonossocódigofosseempacotado.Elaevitaquepacotesprivadosse-
jampublicados,logo,acessíveisporqualquerumatravésdoBower.
bower.json vs component .js
O Bower utilizava nas versões anteriores à 0.9.0 o arquivo
component.jsparalistarasdependênciasdasuaaplicação. Apartir
destaversão, component.jsfoirenomeadopara bower.json.
Agoraquetemosnossoarquivo bower.jsoncriado,jápodemosbaixar
nossasdependênciasfront-end.
3.3 Baixando dependências front-end
Temos o Bower instalado e o arquivobower.json dentro da pasta
contatooh. Nossoprojetoutilizaráduasbibliotecas: AngularJSeBoot-
strap.AprimeiraéumabibliotecaJavaScript;asegunda,umabibliotecaCSS.
VamosinstalaroAngularJSprimeiroemaistardeoBootstrap.
Utilizamosocomando bower install passandocomoparâmetroo
nomedabibliotecaseguidoopcionalmentede #eonúmeroda versão.Uti-
lizaremosoparâmetro --savequeadicionaráabibliotecacomodependên-
ciaem bower.json.Queremosaversão1.3doAngularJS:
$ bower install angular#1.3 --save
bower not-cached git://github.com/angular/bower-angular.git#1.3
bower resolve git://github.com/angular/bower-angular.git#1.3
bower download https://github.com/angular/bower-angular/
41 

## Página 54

3.4. Alterandoapastadestinocom.bowerrc CasadoCódigo
archive/v1.3.2.tar.gz
bower extract angular#1.3 archive.tar.gz
bower resolved git://github.com/angular/
bower-angular.git#1.3.2
Visualizando bower.json,vemosqueoAngularJSfoiadicionadocomo
dependência:
{
...
...
...
"dependencies": {
"angular": "1.3"
}
}
Vamosanalisaroresultadodocomandoanterior.OBowercriouporcon-
vençãoapasta bower_componentsdentrododiretórioondefoichamado,
emnossocaso, contatooh,araizdenossoprojeto.Dentrodela,elecrioua
pasta angularquecontémscriptsminificadosenãominificados.Oprob-
lemaéque,porserumabibliotecafront-end,elaprecisaestardentrodapasta
public. PrecisamosalterarapastapadrãocriadapeloBowercriandoum
novoarquivodeconfiguração,oqueveremosaseguir.
3.4 Alterando a pasta destino com .bowerrc
PodemosalterarocaminhoeonomedapastacriadapeloBowerparaar-
mazenarnossasdependênciasatravésdoarquivooculto .bowerrc.Vamos
criaroarquivodentrodaraizdoprojetocomaseguinteestrutura:
// contatooh/.bowerrc
{
"directory": "public/vendor"
}
Repareque .bowerrctambéméumJSONassimcomo bower.jon
comadiferen çadequeoprimeiropossuiapenasumapropriedadechamada
42

## Página 55

CasadoCódigo Capítulo3. Bower:gerenciadordedependênciasfront-end
directory.Énestapropriedadequedefinimosolocalondeserãobaixados
ospacotesdoprojeto.Emnossocaso,alémdealterarmosocaminhodapasta,
tambémmudamosonomedodiretóriopara public/vendor.
Precisamosapagarapasta bower_componentspara,emseguida,baixar
novamentenossasdependênciasfazendocomquetodasfiquemnapastaque
acabamosdeconfigurar.Issoéfeitoatravésdocomando bower install:
$ bower install
bower cached git://github.com/angular/bower-angular.git#1.3.2
bower validate 1.3.2 against git://github.com/angular/
bower-angular.git#1.3
bower install angular#1.3.2
angular#1.3.2 public/vendor/angular
Assimcomo npm install,quelêasdependênciasnoladodoservi-
dornoarquivo package.json,oBowerbaixarátodasasdependências
listadasem bower.json, sóquedestavezassalvandodentrodapasta
public/vendor.
OBowerpossuioutroscomandosquepodemserúteisevaleapenadar
umaolhadaemalgunsdeles.
3.5 Outros comandos
Vimosqueocomando bower install pacote#versao --save seen-
carregadebaixarnossospacotes,adicionando-osem bower.json.Háout-
roscomandosquepodemserúteisnoworkflowdoprogramadorfront-end.
Vejamosmaisalgunsdeles.
search
Muitasvezesnãosabemosaocertoonomedeumabibliotecae,nesses
casos,teríamosquepesquisarnaweb. Bowerpossuiocomando search
quelistatodasasbibliotecasregistradasquepossuemotextoprocurado,por
exemplo:
bower search angular
43 

## Página 56

3.5. Outroscomandos CasadoCódigo
Serãolistadosnoterminalbibliotecasquecontenhamcomopartedeseu
nomeapalavra angular.
$ bower search angular
...
angularjs-google-maps git://github.com/jvandemo/
angularjs-google-maps
dt-angular-ui git://github.com/dt-bower/dt-angular-ui.git
angular-aop git://github.com/mgechev/angular-aop
angular-storage git://github.com/Aspera/angular-storage.git
...
info
Quais versões de uma determinada biblioteca estão disponíveis pelo
Bower?Podemosteressainformaçãofacilmentepelocomando:
bower info angular
Essecomandolistaránoterminaltodasasversõesdisponíveisequepo-
demserbaixadasatravésdoBower:
$ bower info angular
bower cached git://github.com/angular/bower-angular.git#1.3.2
bower validate 1.3.2 against git://github.com/angular/
bower-angular.git#*
{
name: 'angular',
version: '1.3.2',
main: './angular.js',
ignore: [],
dependencies: {},
homepage: 'https://github.com/angular/bower-angular'
}
Available versions:
- 1.3.3-build.3574+sha.e3764e3
- 1.3.3-build.3573+sha.4d4e603
44

## Página 57

CasadoCódigo Capítulo3. Bower:gerenciadordedependênciasfront-end
- 1.3.3-build.3572+sha.4d885cb
(outras versões)
uninstall
Oquefazerquandoumabibliotecadeixardeserumadependênciado
nossoprojeto?Precisamosapagarsuapastacomtodososseusarquivos,in-
clusivealterarnossoarquivo bower.jsonremovendoabiblioteca.
Podemosfazertudonumatacadasócomocomando:
bower uninstall angular --save
$ bower uninstall angular --save
bower uninstall angular
--offline
TodopacotebaixadopeloBowerficaarmazenadoemumcachequepode
serutilizadooffline,muitobem-vindoquandoestamossemacessoàinter-
netenãoqueremosperdertempo. Paraisso,bastaadicionaroparâmetro
--offlineemconjuntocomocomando bower install:
bower install angular#1.3 --save --offline
$ bower install angular#1.3 --save --offline
bower cached git://github.com/angular/
bower-angular.git#1.3.2
bower install angular#1.3.2
angular#1.3.2 public/vendor/angular
Pronto,játemostudodequeprecisamospararcome çarnossajornada
peloAngularJS.
45 

## Página 59

Capítulo4
AngularJS:oframeworkMVCda
Google
“ A verdade não resulta do número dos que nela creem. ”
–Galileu
Équasecertodequedurantesuatrajetóriacomodesenvolvedorwebvocê
játenhatrabalhadocomJavaScriptnonavegador,aindamaissendoa língua
francadaweb. MesmocomoadventodoNode.js,ocódigoqueescreve-
mosnoladodoclientemanipulaalgoquenãoexistenoladodoservidor:o
Document Object Model(DOM).Vamosrecapitularestevelhoconhecidoea
maneiratradicionalcomomanipulá-lo.

## Página 60

4.1. Umvelhoconhecido:DOM CasadoCódigo
4.1 Um velho conhecido:DOM
ODOMéumaárvoredeelementos,istoé,umespelhoemmemóriadenossa
páginacriadoautomaticamentepelonavegadorquandoelaécarregada.In-
clusive,elepossuifun çõesepropriedadesque,aoseremmodificadas,dis-
paramalteraçõesinstantâneasnoqueéexibidoparaousuário.
VejamosumexemplodemanipulaçãodoDOMqueincrementaototal
decontatoscadastradosparacadacliquenobotão.
PrimeirooHTML:
<!-- página html -->
<button class="botao-grava">Novo</button>
<p class="contatos">Contatos cadastrados: 0 </p>
AgoraoJavaScript:
var contatos = document.querySelector('.contatos');
var total = 0;
var botao = document.querySelector('.botao-grava');
botao.addEventListener('click', function(event) {
total++;
contatos.textContent = 'Contatos cadastrados: + total;
});
ApesardeserJavaScriptpuro,ocódigoétotalmentefuncional,mashá
aquelesqueutilizambibliotecasespecíficasparamanipulaçãodeDOM.Uma
muitofamosaéojQuery.
jQuery
Historicamente,oDOMnãoteveumbomcome ço,comcadanaveg-
adorimplementandofun çõesepropriedadesaseubel-prazer,oqueacabou
gerandoincompatibilidadesentreeles.Estefoiumdosmotivosquelevaram
àcriaçãodojQuery(http://jquery.com)edeoutras bibliotecasdemanipu-
laçãodeDOM quevisamblindaroprogramadordasidiossincrasiasdaAPI
DOMentrenavegadores,inclusiveadicionandoaçúcaressintáticos.
OexemploanterioragoracomjQuery:
48

## Página 61

CasadoCódigo Capítulo4. AngularJS:oframeworkMVCdaGoogle
var contatos = $('.contatos');
contatos.data('total', 0);
$('.botao-grava').click(function() {
var total = contatos.data('total') + 1;
contatos.data('total', total);
contatos.text('Contatos cadastrados: ' + total);
});
Por fim, mais um exemplo de manipulação de DOM usando apenas
jQuerydestavez. Ocódigodeveexibiroresultadodamultiplicaç ãoentre
doisnúmerosinformadospelousuário.PrimeirooHTML:
<p>
Quando é <input class="numero"> vezes <input class= "numero">
</p>
<p>Resultado: <span class="resultado" ></span></p>
Agora,oJavaScriptcomjQuery:
var numerosEl = $('.numero');
$(numerosEl).on('keyup', function() {
var resultado = 1;
$.each(numerosEl, function() {
resultado*= $(this).val();
});
$('.resultado').text(resultado);
});
Maisumavez,temosumcódigofuncional,apesardisso,nemtudoéper-
feitonamanipulaçãodoDOM.
4.2 Dificuldades que surgem da manipulação
doDOM
Apesardeserumatarefarotineiraparaprogramadoresfront-end,amanipu-
laçãodoDOMtrazalgumasdificuldades.
49 

## Página 62

4.2. DificuldadesquesurgemdamanipulaçãodoDOM CasadoCódigo
Presosàestrutura
Nosexemplosanteriores,pormaisquetenhamosutilizadoclassesnosse-
letoresparanãoficarmosamarradosàestruturadodocumento,aindasomos
obrigadosaconhecê-loparasaberqueoelementoXpossuiaclassetale,por-
tanto,podeserselecionado:
// preciso olhar a estrutura e ver que o elemento tem a classe
// .numero
var numerosEl = $('.numero');
Inclusiveprecisamossaberqualfun çãochamarparaobterovalordoele-
mento,porexemplo, val()ou text()usandojQuery:
// se fosse um input, seria val()
$('.resultado').text(resultado);
Esequisermosaindatestarnossocódigo?
Testabilidade
Outropontoquesaltaàvistaéqueanãoseparaç ãoentrealógicaeos
elementosdoDOMtornaotestedocódigoumatarefanãotrivial:
// obtém um elemento do DOM
var numerosEl = $('.numero');
Jápensouemcomorealizarumtestedeunidadenocódigoquevimos?
Comosimularapáginaduranteostestes?Eporaívai.
Consistênciaentremodeleview
Tambémsomososresponsáveisemgarantiraconsistênciaentreodado
esuaapresentação.Emoutraspalavras,todavezqueomodelforatualizado,
precisaremosatualizarsuaapresentaçãonaview.
var numerosEl = $('.numero');
var resultado = 1;
50

## Página 63

CasadoCódigo Capítulo4. AngularJS:oframeworkMVCdaGoogle
// alterando o equivalente ao model
$.each(numerosEl, function() {
resultado*=$(this).val();
});
// sincronizando o model com a view
$('.resultado').text(resultado);
});
SepensarmosnomodeloMVC,precisamosgarantiraconsistênciaen-
treomodeleaview.
Ausênciadeumpadrão
Outropontorelevanteéquenãohánadaqueimponhaumpadrãona
escritadocódigo. Porexemplo,amesmafuncionalidadecomjQueryque
vimospodeserescritadaseguintemaneira:
var numerosEl = $('input[type=text]');
$(numerosEl).keyup(function() {
var resultado = 1;
$.each(numerosEl, function() {
resultado*= $(this).val();
});
$('.resultado').text(resultado);
});
Éclaroqueaequipepodedefinirum,masteráquetransmiti-lopara
novosdesenvolvedores.
Outraop ção:frameworksMVCclient-side
Combasenosproblemaslistados,foramcriadosframeworksMVC client-
sidecomoBackBone(http://backbonejs.org),Amber(http://emberjs.com)
,Can(http://canjs.com)entreoutros. Umframeworkquevemganhando
muitaforçanacomunidadeéo AngularJS.Qualarazãodeseusucesso?Va-
mosver!
51 

## Página 64

4.3. CaracterísticasdoAngularJS CasadoCódigo
4.3 Características doAngularJS
AngularJS(http://angularjs.org)éumframeworkMVC client-sideque
trabalhacomtecnologiasjáestabelecidas:HTML,CSSeJavaScript.Criadona
Googleeliberadocomoprojetoopen-sourceparaopúblicoem2009,seufoco
residenacriaçãode Single Page Applications(SPA),emboraissonãooimpe ça
deserutilizadoemoutrostiposdeaplicaç ão.AngularJSéum high opinion-
ated framework,oquesignificaqueeleguiaodesenvolvedordemaneiraim-
placávelnaorganizaçãodeseucódigo.
SinglePageApplication(SPA)
SPA é uma aplicação entregue ao navegador que não recarrega a
páginaduranteseuuso,porissojácarregatodoJavaScripteCSSdeque
precisa.
MiškoHevery,paidoframework,procuroutrazerosmesmosbenefícios
domodeloMVCaplicadosnoladodoservidorparaonavegadorcomoa fa-
cilidadedemanutenç ão,reusabilidadeatravésdecomponentese testabili-
dade,umavezquealógicaédesacopladadeelementosdoDOM.Aindahá
recursoscomoinjeçãodedependências!
EnumerarascaracterísticasdoAngularJSnãoétãoesclarecedorquanto
vê-las na prática, muito menos apresentar todas de uma só vez. Nosso
primeiropassoserácriarumanovapáginacomAngularJShabilitado.
4.4 Preparando o ambiente
AgoraquevamostrabalharcomoAngularJS,deixaremosdeutilizarviews
processadasnoladodoservidor. Paraevitarconfusão,vamosrenomearos
arquivosgarantindoqueelesnãosejamcarregadospeloExpressetambém
paraquevocênãoosperca:
•app/views/index.ejspara app/views/index.ejs.old
•app/controllers/home.ejs para
app/controllers/home.ejs.old
52

## Página 66

4.5. HabilitandooAngularJSemnossapágina CasadoCódigo
4.5 Habilitando oAngularJS em nossa página
ParahabilitarmosoAngularJSemnossapágina public/index.html,pre-
cisamosprimeiroimportarseuscriptantesdatagdefechamento </body>:
<!-- public/index.html -->
...
<body>
<h1>Bem-vindo ao Contatooh</h1>
<button>Novo</button>
<p>Contatos cadastrados: 0</p>
<script src="vendor/angular/angular.js"></script>
</body>
...
Importarabibliotecanãoésuficiente. Precisamosadicionaroatributo
ng-appnaáreaqueserácontroladapeloAngularJS:
<!-- public/index.html -->
...
<html ng-app="contatooh">
...
<body>
<h1>Bem-vindo ao Contatooh</h1>
<button>Novo</button>
<p>Contatos cadastrados: 0</p>
<script src="vendor/angular/angular.js"></script>
</body>
</html>
Issoénecessário,porqueoAngularJSgerenciaapenasoblococomo
atributo ng-app. Emnossoexemplo,estamosgerenciandooHTMLin-
teiro,maspoderíamosgerenciarumaáreamenor,deixandoorestantepara
outrosframeworksquetambémgerenciamoHTML,comoEmberjs(http:
//emberjs.com/), evitandoconflito. Umpontocuriosoéqueoatributo
54

## Página 67

CasadoCódigo Capítulo4. AngularJS:oframeworkMVCdaGoogle
ng-appnãoexistenoHTML,sendouma diretivadoAngularJS.Diretivas
podemser atributos,tagseatémesmocomentáriosespeciaisqueampliam
ovocabuláriodonavegador.
Repareque,nadiretiva ng-app,atribuímosovalor contatooh,que
naverdadeéonomedomóduloprincipaldaaplicaç ão,aquelepeloqualre-
alizamosumasériedeconfigurações.Masondeéqueestáestemódulo?Pre-
cisamoscriá-loeéissoquefaremos.
4.6 Nosso primeiro módulo com AngularJS
Um módulo em AngularJS nada mais é do que um código JavaScript
declaradoemseuarquivo. Vamoscriaroarquivo public/js/main.js
importando-ologoemseguidaem public/index.html:
<! -- public/index.html -->
...
<script src="vendor/angular/angular.js"></script>
<script src="js/main.js"></script>
...
Editandooarquivo public/js/main.jsvamosprogramarnossomó-
dulo:
// public/js/main.js
angular.module('contatooh', []);
Espereumpouco?Deondeveiooobjeto angular?
Oobjetoangular
AngularJSdisponibilizaoobjeto angularglobalmente. Éatravésdele
queacessamosváriosrecursosdoframework,inclusiveodecriaç ãodemó-
dulos,justamenteaqueledequeprecisamos.
Criamosummóduloatravésdafun ção angular.module. Elarecebe
doisparâmetros: oprimeiroéo nomedomódulo; osegundo,um array
comtodasassuasdependências.Nãotemosnenhumadependênciaporen-
quanto,aindaassim,precisamospassaroarray vaziocomoparâmetro.
55 

## Página 68

4.7. Angularexpression(AE) CasadoCódigo
MóduloNode.js vs.M óduloAngularJS
Nãoconfundaomóduloquecriamosnoladodoservidorusando
Node.jscomomódulodoAngularJs. Oprimeirorodanoserver-side,
osegundonoclient-side.
Reparequeonomedomódulopossuiomesmovalordadiretiva ng-app,
garantindoaligaçãodenossapáginacomomóduloqueacabamosdecriar.
Nossapróximatarefaseráassociaralgumdadoànossaview.
4.7 Angular expression (AE)
Em public/index.html, nosso parágrafo exibe o total de contatos
cadastrados,masovalorestáfixo. Énecessárioqueessainformaç ãovarie
todavezqueousuárioclicarnobotão“Novo”.Paraisso,usaremosumaAn-
gularExpression(AE):
<p>Contatos cadastrados: {{total}}</p>
UmaAEérepresentadapor {{ }}.Tudooqueestiverentreaschaves
duplasserábuscadodealgumlugaremescladocomnossaview.Nesseponto,
podemosdizerquenossaviewéumaespéciede template,jáquepossuiuma
lacunaqueprecisaserpreenchida.Emnossocaso.usamosaAE {{total}}.
Verifiquemosoresultado:
http://localhost:3000
Fig.4.2:AngularExpression(AE)nãoavaliada
56

## Página 69

CasadoCódigo Capítulo4. AngularJS:oframeworkMVCdaGoogle
VocêdeveterreparadoqueaAngularExpressionnãoéexibidanonave-
gador,elaésimplesmenteignorada!IssoéumpadrãodoAngularJS: AEnão
resolvidasficamembranco.Aindaprecisamosquealgumvalorsejaexibido,
mesmoquesejaovalorzeroinicialmente.
Visualizando{{total}} em seu navegador?
Casovocêestejavisualizandononavegadorotexto {{total}},é
muitoprovávelquehajaalgumproblemanaconfiguraçãodoAngularJS
emsuapágina(importaçãodescriptfaltando, ng-appapontandopara
ummóduloquenãoexisteetc.).
SeoAngularJSéumframeworkMVC,queméoresponsávelemdisponi-
bilizarosdadosparaaview?Ocontroller!Precisamosdeumcontrollerque
disponibilizeodadodequenossaAEprecisa.
4.8 Nosso primeiro controlller
Adiretiva ng-appapenasindicaqueatag htmlégerenciadapeloAngu-
larJS,inclusivetodosseuselementosfilhos,masnãoindica quemfornecerá
osdados ouquemresponderáàsações levadascomesseselementos. Em
AngularJS,dizemosqueestassãoresponsabilidadesdeum controller.
Adiretivang-controller
Associamosum controlleraumelementodenossapáginaatravésda
diretiva ng-controller.Emnossocaso,elaseráassociadaàtag <body>:
<! -- public/index.html -->
...
<body ng-controller="ContatosController">
...
Noexemploanterior, ocontroller ContatosControllerseráorespon-
sável em fornecer o dado{{total}} para view, sendo assim, pre-
cisamos criá-lo. É uma boa prática do AngularJS criar cada con-
57 

## Página 70

4.8. Nossoprimeirocontrolller CasadoCódigo
troller em um arquivo em separado, inclusive podemos agrupá-los den-
tro de uma pasta chamadacontrollers. Vamos criar o arquivo
public/js/controllers/ContatosControlller.js:
// public/js/controllers/ContatosController.js
angular.module('contatooh').controller('ContatosController',
function() {
});
Nessecódigo,chamamosnovamenteafun ção angular.module,mas
dessavezpassamosapenasonomedomódulocomoparâmetro.Adiferen ça
éque,nolugardecriarmosummódulo,estamosacessandoumjáexistente.
Emseguida,encadeamosumachamadaàfun çãocontrollerparacriarmos
nossoprimeirocontrolador.
Afunção controllerrecebecomoprimeiroparâmetroo nomedocon-
troller,osegundo,a funçãoqueodefinirá.Seopapeldocontrollerédisponi-
bilizarparaaviewodadodequeelaprecisa,vamoscriaravariáveltotal:
// public/js/controllers/ContatosController.js
angular.module('contatooh').controller('ContatosController',
function() {
var total = 0;
});
Porfim,vamosimportaronossocontrollerimediatamenteapósaimpor-
taçãodonossomóduloprincipalem index.html:
<! -- public/index.html -->
...
<script src="vendor/angular/angular.js"></script>
<script src="js/main.js"></script>
<script src="js/controllers/ContatosController.js"></script>
...
58

## Página 72

4.9. $scope:acolaentrecontrollereview CasadoCódigo
Oobjetoespecial $scopefuncionadaseguintemaneira:tudooquefor
adicionandodinamicamenteneleestarádisponívelnaview.Mascomotere-
mosacessoaesseobjeto?Éaíqueentraosistemade injeçãodedependência
doAngularJS.
Injeçãodedependência
PodemossolicitaraoAngularJSoobjeto $scope,adicionando-ocomo
parâmetrodafun çãoquedefinenossocontroller:
// public/js/controllers/ContatosController.js
angular.module('contatooh').controller('ContatosController',
function($scope) {
var total = 0;
});
Osistemadeinje çãodedependênciasdoAngularJSébaseadononome
doparâmetro,logo,seusarmosqualqueroutronome,oframeworknãoserá
capazdeinjetá-loemnossocontroller.
$scopeéumPOJO
Temos o objeto que representa o escopo do nosso controller
ContatosController e sabemos que ele é a cola entre o controller e
aview. Eagora? $scopeéum Plain Old Javascript Object (POJO),logo,
podemosadicionarpropriedadesdinamicamenteeomaisfantásticoéque
elasserãoacessíveispelaviewatravésdeAE.
Vamossubstituiradeclaraçãodavariável totaladicionandoapro-
priedadedemesmonomeemnossoobjeto $scope. Aproveitaremospara
inicializarseuvalorcomzero:
// public/js/controllers/ContatosController.js
angular.module('contatooh').controller('ContatosController',
function($scope) {
$scope.total = 0;
});
60

## Página 73

CasadoCódigo Capítulo4. AngularJS:oframeworkMVCdaGoogle
Jápodemostestarabrindonossapáginanonavegador:
http://localhost:3000
Reparequeagoraotextoexibidoé:
Contatos cadastrados: 0
Isso prova que nossa AE conseguiu buscar no escopo de
ContatosControllerodadodequeprecisava,istoé,noobjeto $scope
querepresentaoescopodocontroller ContatosController.
Játemosviewecontroller,masondeestáomodeldoMVC?Éoquever-
emosaseguir.
4.10 AngularJS e o model doMVC
AngularJSnãoérígidonaescolhadeummodel,istoé,qualquertipoliteral
doJavaScriptouobjetopodemsermodels,logo,disponíveisnoescopodo
controller.
Porexemplo,poderíamoster:
// Object
$scope.contato = {
nome: 'Flávio Henrique',
sobrenome: 'Souza Almeida'
};
// boolean
$scope.exibir = true;
// Number
$scope.salario = 100.12;
// Date
$scope.admissao = new Date();
Éporissoqueagorachamaremos $scope.totaldemodel. Falando
emmodel,precisamosincrementá-lotodavezqueousuárioclicarnobotão
Novo.Paraisso,utilizaremosmaisumadiretivadoAngular.
61

## Página 74

4.11. Executandoaçõesnocontrolleratravésdediretiva CasadoCódigo
4.11 Executando ações no controller através
de diretiv a
Comoincrementarototalexibidoquandoobotãoforclicado?Éatravésda
diretiva ng-clickqueconseguiremosesteresultado:
<!-- public/index.html -->
...
<button ng-click="incrementa()">Novo</button>
...
Adiretiva ng-clicktemcomovalora chamadadeumafunç ão,em
nossocaso, incrementa(). Elasecomportadamesmamaneiracomose
tivéssemosassociadoafun çãoaoevento onclickemJavaScript.Seguindo
amesmalógica,existemdiretivascomo ng-blur, ng-mouseoveretc.O
AngularJSpossuiumaparacadatipodeeventodoJavaScript.
Masondenossadiretivaprocuraráafun ção incrementa()?Noescopo
denossocontroller,ondemaisseria?Vamosadicionarem $scopeafunção
queincrementaránossototal:
// public/js/controllers/ContatosController.js
angular.module('contatooh').controller('ContatosController',
function($scope) {
$scope.total = 0;
$scope.incrementa = function() {
$scope.total++;
};
});
Nossafunção,atribuídaa $scope.incrementasimplesmenteincre-
mentaapropriedade $scope.totaleseráchamadatodavezqueobotão
denossapáginaforclicado.Vamosvisualizarapáginaeclicaralgumasvezes
nobotão:
http://localhost:3000
62

## Página 76

4.13. Singlepageapplication(SPA)enossoprojeto CasadoCódigo
Consideração sobre templates server-side X client-
side
Vocêjádeveterpercebidoadiferen çaentre <%= > e {{ }}. O
primeiro,éumaexpressãoavaliadanoladodoservidorpeloExpress.
Depoisdeprocessada,oqueéenviadoparaonavegadoréoHTMLjá
mesclado,istoé,comainformaçãojásubstituída.
AAE,poroutrolado,éavaliadanonavegador.Vocêpodeatéexibir
ocódigo-fontedanossapágina.Nele,vocêveráqueaAE {{total}}
continualá,mas,sevocêinspecionaroelementodoDOMquecarrega
aAE,oqueéexibidoé‘0’,indicandoqueoAngularJSprocessouaAE
modificandooDOMnoladodocliente.
Aprenderemosnase ção5.4comocarregarosdadosdoservidorpara
alimentarnossostemplatesnoladodocliente.
AgoraquejásabemosumpoucomaisdeAngularJS,jápodemosiniciar
nossosestudossobreseusistemaderotasnapróximase ção.
4.13 Single page application(SPA) e nosso pro-
jeto
Nossa aplicação Contatooh por enquanto possui apenas a página
public/index.html. Além dela, mais duas serão necessárias: uma
quelistacontatoseoutraqueexibeumcontatoselecionadodalista.Faremos
issousandoaestratégia SinglePageApplication.
SinglePageApplication(SPA)
SinglePageApplication(SPA)éumaaplicaç ãoentregueparaonave-
gadorquenãorecarregaapáginaduranteseuuso. Aplicaçõesdestetipo
tendemadarumaexperiênciamaisfluidaparaosusuários,aomesmotempo
emquefavoreceoservidor,enviandoumaquantidadededadosmenorpara
serprocessada.
EmSPA,apáginaprincipal,porexemplo, index.html,écarregada
64

## Página 78

4.14. OmódulongRoute CasadoCódigo
deatualizarapáginaprincipalcomoconteúdodasparciais:
Exemplos de URLs
http://localhost:3000/index.html#/contatos
http://localhost:3000/index.html#/produtos
http://localhost:3000/index.html#/contato/1
OAngularJSpossuiseuprópriosistemaderotas. Éoqueveremosa
seguir.
4.14 O módulo ngRoute
AngularJSpossuiumsistemaderotasquevisablindarodesenvolvedorda
complexidadepelaatualizaçãodeáreasdapáginautilizandoAjax,maisuma
vez,evitandoqueelemanipuleoDOMdiretamente.
Necessidadedeumservidor
Umpontoimportantíssimoéque osistemaderotasdoAngularJSsó
funcionarásevocêestiverrodandosuaaplicaçãonumservidorweb (oque
nãoéumproblemaparanós),mesmoquevocêestejaapenasquerendotestá-
lo.IssoénecessárioporqueoAngularJSdispararequisiçõesAjaxparabuscar
doservidorparciaisqueeleprecisaexibir.
Antesdaversão1.2,oAngularJSjávinhacomosistemaderotas,mas
aequipedecidiumovê-lodocoreparaummóduloemseparadochamado
ngRoute.Precisamosbaixá-loatravésdoBowernalinhadecomando:
bower install angular-route#1.3 --save
Não podemos nos esquecer de importar o script em nossa página
public/index.htmlimediatamenteapósaimportaçãodoscriptdoAn-
gularJS:
<! -- public/index.html -->
...
<script src="vendor/angular/angular.js"></script>
<script src="vendor/angular-route/angular-route.js"></script>
66

## Página 79

CasadoCódigo Capítulo4. AngularJS:oframeworkMVCdaGoogle
<script src="js/main.js"></script>
<script src="js/controllers/ContatosController.js"></script>
Isso ainda não é suficiente, precisamos tornar nosso módulo
principal, contatooh, ciente deste módulo. Para isso, editaremos
public/js/main.js adicionando o módulongRoute como sua de-
pendência.Issoéimportante,casocontrário,nãoteremosacessoàartefatos
injetáveisdestemódulo.Vamosfazerissoadicionando-onoarraypassando
comosegundoparâmetrodafun ção angular.module:
// public/js/main.js
angular.module('contatooh', ['ngRoute']);
Sistemaderotasativado,porémnãoconfigurado!Antesdeconfigurá-lo,
vamosalterarapágina public/index.htmlsubstituindooconteúdoda
tag <body>poruma <div>comadiretiva ng-view,masmantendoa
importaçãodosscripts.
Não podemos esquecer deremovera diretiva ng-controller de
<body>, o que é necessário porque a associação do controller será feita
atravésdaconfiguraçãodenossasrotas. Issopermitequeparciaispossam
utilizarcontrollersdiferentesdeacordocomquemasusa.
Nossapáginadeveficarassim:
<!-- public/index.html -->
...
<body>
<div ng-view></div>
<script src="vendor/angular/angular.js"></script>
<script src="vendor/angular-route/angular-route.js"></script>
<script src="js/main.js"></script>
<script src="js/controllers/ContatosController.js"></script>
</body>
...
Adiretiva ng-viewsinalizaparaosistemaderotasaáreadapágina
quereceberáviewsparciais.Adiferen çadeumaviewparcialparaumaview
comoa index.htmléqueaprimeiranãopossuiastags <html>, <head>
67

## Página 80

4.15. Criandoviewsparciais CasadoCódigo
e <body>,logo,paraseremexibidas,precisamserincluídasdinamicamente
dentrodeumapáginacomadiretiva ng-view,emnossocaso,apágina
index.html.
4.15 Criando views parciais
Temosnossaviewprincipal index.htmlpronta,agoraprecisamoscriar
nossasprimeirasparciaisquepopularãoadiretiva ng-view.Vamoscriara
pasta app/public/partialsedentrodelaguardartodasasnossasviews
parciais.
Uma diretiv a, diferentes apresentações
No lugar de criarmos uma<div> com a diretiva ng-view,
poderíamosutilizaratag <ng-view></ng-view>. Lembre-seque
diretivasdoAngularJSpodemserutilizadascomotags,atributoseaté
mesmocomocomentário!Parasaberquaisformatosestãodisponíveis,
precisamosconsultaradocumentaçãodoAngularJS.
Primeirocriaremosaviewparcialqueseráresponsávelpelalistagemdos
contatos. Reparequemovemosparaelanossobotãoeoparágrafocoma
AngularExpression:
<!-- public/partials/contatos.html -->
<h1>Bem-vindo ao Contatooh</h1>
<button ng-click="incrementa()">Novo</button>
<p>Contatos cadastrados: {{total}}</p>
Anossaview,aindaincompleta,exibiráocontatodalista.
<!-- public/partials/contato.html -->
<h1>Contato</h1>
Agoratemostrêsarquivos:
68

## Página 81

CasadoCódigo Capítulo4. AngularJS:oframeworkMVCdaGoogle
•public/index.html:páginaprincipal,aquelaquereceberáviewsparci-
aisdeacordocomasrotasdaaplicaç ão.
•public/partials/contatos.html:viewparcialresponsávelpelalistagem
decontatos.
•public/partials/contato.html: viewparcialresponsávelpelaexibição
docontatoselecionadodalista.
Se abrirmos a página no navegador apenas veremos uma página em
branco. Precisamos configurar as rotas da aplicação e definir que a
URLhttp://localhost:3000/index.html#/contatosdevecarregaraviewparcial
public/partials/contatos.html.Preparado?
4.16 Configurando rotas com $routeP rovider
Aconfiguraçãodasrotasdaaplicaçãocostumaserfeitanomóduloprincipal
daaplicação,ouseja,noarquivo main.js.Utilizamosafun ção config,que
recebeumafun çãoquetemcomoparâmetroumartefatoinjetadopeloAn-
gularJSresponsávelpelacriaçãoderotas,oobjeto $routeProvider.Caso
nãotivéssemosimportadoomódulo ngRoute,elenãoestariadisponível
parainjeção:
// public/js/main.js
angular.module('contatooh', ['ngRoute'])
.config(function($routeProvider) {
$routeProvider.when('/contatos', {
templateUrl : 'partials/contatos.html',
controller: 'ContatosController'
});
});
Oobjeto $routeProviderpossuiafun ção when. Nelainformamos
arota(semo #)enosegundoparâmetroumobjetoquedefinequal tem-
plate(parcial)serácarregadoparaarotaequalseráseu controlleratravés
daspropriedades templateURLe controller,respectivamente.
69

## Página 82

4.16. Configurandorotascom $routeProvider CasadoCódigo
Um ponto importante é que toda rota configurada por
$routeProviderparaserdisparadadeveseracessadaatravésdaURLda
páginaprincipaladicionandooprefixo #,ofamoso hash.Porexemplo:
http://localhost:3000/index.html#/contatos
Comonossapágina index.htmlestádentrodapasta publicpodemos
acessá-ladiretamenteatravésdaURL /,éporissoquetambémpodemos
disparararotadoAngularJSdestamaneiramaisenxuta.Podemostestar:
http://localhost:3000/#/contatos
Fig.4.6:Testandorota #/contatos
Não podemos esquecer do#, porque se acessássemos a URL (http:
//localhost:3000/contatos)alistadecontatosdoservidorseriadevolvidapara
nós. Nãoqueremosdispararumarotadoservidor,queremosdispararuma
rotanoladodoclientequesaberáatualizarnossapágina index.htmljá
carregadanonavegadorcomdeterminadaparcial.
Maisumarota
Precisamos criar a rota responsável pela exibição da parcial
partials/contato.html. Esta página exibirá o contato selecionado
dalista,logo,precisarecebercomoparâmetrooiddocontatoselecionado:
$routeProvider.when('/contato/:contatoId', {
templateUrl : 'partials/contato.html',
controller: 'ContatoController'
});
70

## Página 83

CasadoCódigo Capítulo4. AngularJS:oframeworkMVCdaGoogle
Repare que a rota é um pouco diferente terminando com o
curinga :contatoId. É através deste nome que dentro do controller
ContatoControllerpodemosreferenciaro iddocontatopassadona
URL,porexemplo:
htttp://localhost:3000/index.html#/contato/1
Mascomoobtê-lo?Éoqueveremosadiante.
4.17 O objeto $routeP arams
Vimos na seção anterior a necessidade de obtermos o ID do contato
a partir de uma rota do AngularJS. Para isso, criaremos o controller
public/js/controllers/ContatoController.js:
// public/js/controllers/ContatoController.js
angular.module('contatooh').controller('ContatoController',
function($scope, $routeParams) {
console.log($routeParams.contatoId);
});
Repare que ContatoController recebe via injeção o objeto
$routeParams. Esteobjetosóestádisponívelporqueestamosutilizadoo
módulo ngRoute.
É acessando a propriedade$routeParams.contatoId que temos
acessoaoparâmetropassadoviaURL.Porenquanto,apenasoimprimire-
mosnoconsole,masnofuturo,precisaremosbuscarocontatoassociadoa
esteIDemnossoservidorExpress,queporsuavezobuscaránobancode
dadospara,nofim,serexibidoemnossaparcial.
Não podemos nos esquecer de importarContatoController em
public/index.html:
<!-- public/index.html -->
...
71

## Página 84

4.17. Oobjeto$routeParams CasadoCódigo
<body>
<h1>Bem-vindo ao Contatooh</h1>
<div ng-view></div>
<script src="vendor/angular/angular.js"></script>
<script src="vendor/angular-route/angular-route.js"></script>
<script src="js/main.js"></script>
<script src="js/controllers/ContatosController.js"></script>
<script src="js/controllers/ContatoController.js"></script>
</body>
...
Podemostestar:
http://localhost:3000/#/contato/1
Fig.4.7:Testandorota #/contato/1
Massearotaacessadanãoexistir?Podemosadicionarumarotapadrão.
Adicionandorotapadrão
Porfim,podemosadicionarumarotapadrãocasooendere çodarota
nãoexista.Fazemosissoatravésdafun ção $routeProvider.otherwise.
Nela,passamosumobjetocomapropriedade redirectTo,queapontapara
umrotaalternativa,emnossocaso,aquelaquelistaoscontatos:
$routeProvider.otherwise({redirectTo: '/contatos'});
AgoraquejáentendemoscomofuncionaomecanismoderotasdoAngu-
larJSprecisamosconcluirnossasparciais.Vamosfazerissocomuma“ajud-
inha”doBootstrapparadepoisvoltarmosparaoAngularJS.
72

## Página 86

4.18. Bootstrap:visualprofissionalemnossasviews CasadoCódigo
• Estilovisualbasepramaioriadastags
• Íconesatravésdoglyphicon
• Gridsprontosparauso
• ComponentesCSS
• PluginsJavaScript
• Tudoresponsivoemobile-first
BaixandooBootstrapatravésdoBower
BaixamosoAngularJSatravésdoBowereagorafaremosamesmacoisa
comoBootstrap. Paraisso,vamosexecutarocomandoaseguirdentroda
pastaraizdoprojeto:
$ bower install bootstrap --save
bower not-cached git://github.com/twbs/bootstrap.git#3.3
bower resolve git://github.com/twbs/bootstrap.git#3.3
bower download https://github.com/twbs/bootstrap/archive/
v3.3.1.tar.gz
...
bower resolved git://github.com/twbs/bootstrap.git#3.3.1
bower not-cached git://github.com/jquery/jquery.git#>= 1.9.1
bower resolve git://github.com/jquery/jquery.git#>= 1.9.1
bower download https://github.com/jquery/jquery/archive/
2.1.1.tar.gz
bower extract jquery#>= 1.9.1 archive.tar.gz
bower resolved git://github.com/jquery/jquery.git#2.1.1
bower install bootstrap#3.3.1
bower install jquery#2.1.1
bootstrap#3.3.1 public/vendor/bootstrap
jquery#2.1.1
jquery#2.1.1 public/vendor/jquery
74

## Página 87

CasadoCódigo Capítulo4. AngularJS:oframeworkMVCdaGoogle
UmpontocuriosoéqueoBowernãobaixouapenasoBootstrapparanós,
mastambémojQuery(http://jquery.com).IssoaconteceporqueoBootstrap
temcomodependênciaojQuery,utilizadoporalgunsdeseuscomponentes.
AgorafaltaintegraroBoostrapcomnossasviews.
AdicionandooBootstrapemnossaspáginas
O CSS do Bootstrap precisa ser importado. Como estamos criando
uma SPA, sua importação é na página principal, em nosso caso,
public/index.html.
<!-- public/index.html -->
...
<head>
<meta charset="UTF-8">
<title>Contatooh</title>
<link rel="stylesheet"
href="vendor/bootstrap/dist/css/bootstrap.css">
<link rel="stylesheet"
href="vendor/bootstrap/dist/css/bootstrap-theme.css">
</head>
Aproveiteaadicioneaclasse containerdoBootstrapnatag body:
...
<body class="container">
...
Aclasse containerfarácomquetodooconteúdodapáginafiquealin-
hadoaocentro.Vocêjápodevisualizaroresultado,inclusivepodeadicionar
eremoveraclasseparaveradiferen ça(visualizeemtelacheiaparafacilitara
percepção):
http://localhost:3000/#/contatos
Comotodasasparciaisserãoadicionadasdentroda <div>comadiretiva
ng-viewfilhadebody,todasserãocentralizadas.
Agoravamoscompletarapágina public/partials/contatos.html:
<!-- public/partials/contatos.html -->
75

## Página 88

4.18. Bootstrap:visualprofissionalemnossasviews CasadoCódigo
<div class="jumbotron">
<h1 class="text-center">
Bem-vindo ao Contatooh
</h1>
</div>
<button class="btn btn-primary" ng-click="incrementa()">
Novo
</button>
<p>Contatos cadastrados: {{total}}</p>
<div class="table-responsive">
<table class="table table-hover">
<tr>
<th>NOME</th>
<th>E-MAIL </th>
<th class="text-center">Ação</th>
</tr>
<tr>
<td>
<a>Contato</a>
</td>
<td>cont@empresa.com.br</td>
<td class="text-center">
<button class="btn btn-warning">
Remover
</buttom>
</td>
</tr>
</table>
</div>
ReparequeusamosumasériedeclassesdoBootstrap,sãoelas:
•btn:classequeforneceumvisualdiferenciadoparaobotão.
•btn-primary:destacaobotão(azuladoemaior)quandocombinada
comaclasse btn.
•btn-warning: destaca o botão, sem aumentar seu tamanho
colocando-onacorlaranja.
76

## Página 90

4.19. Adiretivang-repeat CasadoCódigo
ComAngularJS,acoisamudaumpouco:oAngularJSpedeaoservidor
osdadosdequeprecisaeseencarregadeatualizaraviewcomessesdadosno
ladodocliente,ofamoso data binding. Jásabemosquequalquerdado
“pendurado”noobjeto$scopeévisívelpelaview,sendoassim,vamoscriar
umalistadecontatosnoescopode ContatosController:
// public/js/controllers/ContatosController.js
angular.module('contatooh').controller('ContatosController',
function($scope) {
// código omitido
$scope.contatos = [
{
"_id": 1,
"nome": "Contato Angular 1",
"email": "cont1@empresa.com.br"
},
{
"_id": 2,
"nome": "Contato Angular 2",
"email": "cont2@empresa.com.br"
},
{
"_id": 3,
"nome": "Contato Angular 3",
"email": "cont3@empresa.com.br"
}
];
});
Muito bem, temos uma lista e sabemos que nossa parcial
contatos.htmlprecisaserconstruídaapartirdela,mascomo? Apelare-
mosparamaisumadiretivadoAngularJS,a ng-repeat.
EssadiretivapermitequeoAngularJSrepitaacriaç ãodeumelementode
nossapáginaapartirdosdadosdeumarray.Emnossocaso,vamosadicioná-
lana <tr>queexibeosdadosdocontato:
78

## Página 91

CasadoCódigo Capítulo4. AngularJS:oframeworkMVCdaGoogle
<!-- partials/contatos.html -->
...
<tr ng-repeat="contato in contatos">
<td>
<a>{{contato.nome}}</a>
</td>
<td>{{contato.email}}</td>
<td class="text-center">
<button class="btn btn-warning">
Remover
</buttom>
</td>
</tr>
...
Adiretivapossuiumvalorespecial:
ng-repeat="contato in contatos"
Nela,indicamosquallistaestamosvarrendo,emnossocaso contatos.
Mascomoteracessoacadacontatodalista? Paraisso,damosumapelido
paracadaitemdalista,emnossocaso,escolhemosoapelido contato.
Comotemostrêscontatosemnossalista,adiretiva ng-repeatserá
repetidatrêsvezeseatravésdaAEpodemosteracessoaosdadosdocontato,
porexemplo,com {{contato.nome}}acessamosseunome.Visualizemos
oresultado:
http://localhost:3000/#/contatos
79

## Página 92

4.20. Adiretivang-modelefiltragemdalista CasadoCódigo
Fig.4.10:Adiretivang-repeatemaç ão
Adiretiva ng-repeatébemesperta,permitindoaindafiltrarnossalista
compouquíssimoesfor ço.Éoqueveremosaseguir.
4.20 A diretiv a ng-model e filtragem da lista
Podemosfiltrarnossalistadecontatos,mas,primeiro,precisamosadicionar
um inputemnossaviewparcial contatos.html:
<button class="btn btn-primary" ng-click= "incrementa()">
Novo
</button>
<input type="search" placeholder="parte do nome">
<p>Contatos cadastrados: {{total}}</p>
NãopodemossimplesmenteutilizarumaAE {{}}emnosso input,
porquetodaAEésomenteleitura.Emnossocaso,queremosleregravarem
umapropriedadenoescopodocontroller,istoé,queremosfazer two-way
databinding.Paraisso,usamosadiretiva ng-model:
<input ng-model="filtro" type="search"
placeholder="parte do nome">
Agora,criamosapropriedadenoescopode ContatosController:
80

## Página 94

4.21. Revisandooqueaprendemos CasadoCódigo
AtivaçãodoAngularJSemnossapágina
Vimosqueoprimeiropassoparatornarmosumapáginagerenciadapelo
AngularJSéimportarseuscripteadicionaradiretiva ng-appnatagquede-
limitaráaáreadeatuaçãodoframework,normalmenteatag html.Diretivas
separecemcomatributosoutags,comadiferen çadequesãoprocessadas
peloAngularJS,adicionandonovoscomportamentosàpágina:
<html ng-app="contatooh">
Criaçãodomóduloprincipaldaaplicaç ão
Adiretiva ng-appapontaparaonomemóduloprincipaldaaplicaç ão
criadoatravésdoobjeto angular,disponívelglobalmentepeloframework,
chamandoafun ção angular.module.Elarecebeonomedomódulo,em
nossocaso, contatooh,eumarraycomsuasdependências,queporen-
quantodeixamosvazio.Acriaçãodomóduloeoutrasconfiguraçõessãofeitas
noarquivo main.js,masnadaimpedequeoutrosejautilizado:
angular.module('contatooh', []);
AngularExpression
Aprendemosquepáginaéviewequeelapodeterumalacunadefinida
atravésdeuma Angular Expression (AE)caracterizadapor {{ }} e
tudoqueestiverdentrodelaprecisaserbuscadodealgumlugar,destaforma,
viewsatuamcomotemplatesqueprecisamdedadosfornecidosporcon-
trollers:
<p>Contatos cadastrados: {{total}}</p>
Associaçãodaviewcomumcontroller
Umcontrolleréassociadoaoelementoqueutiliza AEouqualquerele-
mentopaidoqualelefaç aparteatravésdadiretiva ng-controller,que
possuicomovaloronomedocontrollercriado:
<body ng-controller="ContatosController">
82

## Página 95

CasadoCódigo Capítulo4. AngularJS:oframeworkMVCdaGoogle
Definiçãodeumcontroller
Nãoéincomumcriarcontrollersemarquivosseparadosiniciandocom
letramaiúsculaedefinidosatravésdafun ção controllerquerecebecomo
parâmetroonomedocontrollereafun çãoqueodefine.Estaúltima,nosdá
acessoaoobjeto $scope,aquelequeéa“cola”entreocontrollereaview.
Qualquerpropriedadeadicionadaem scopeéacessívelatravésdeAEno
controller:
angular.module('contatooh').controller('ContatosController',
function($scope) {
$scope.total = 0;
});
Injeçãodedependências
Tambémfoiapresentadoqueoacessoaoobjeto $scopeéfeitoatravés
dosistemadeinje çãodedependênciasdoAngularJS,dependentedonome
doparâmetro.Nãoprecisamoscriaroobjeto,apenasindicarqueprecisamos
dele.
Adiretivang-click
Porfim,vimosquehádiretivasquepermitemexecutaraçõesdefinidas
noescopodocontrollercomoadiretiva ng-click:
<button ng-click="incrementa()">Novo</button>
Nestadiretiva,evocamosumafun çãoque,quandopresentenocontroller,
seráexecutada.Durantesuaexecuçãopodemosalterardados“pendurados”
em $scopequeoAngularJSseencarregarádesincronizá-locomaview:
angular.module('contatooh').controller('ContatosController',
function($scope) {
$scope.total = 0;
$scope.incrementa = function() {
83

## Página 96

4.21. Revisandooqueaprendemos CasadoCódigo
$scope.total++;
};
});
Esseprocessoéchamadode one-way data binding,quepermite
apenaslerdadosnoescopodocontroller.
Adiretivang-repeat
Outrodiretivapoderosaquevimosfoia ng-repeat,quepermiterepetir
oelementonoqualelafoiatribuídacombaseemumarraydefinidonoescopo
docontroller:
<tr ng-repeat="contato in contatos">
<td>
<a>{{contato.nome}}</a>
</td>
<td>{{contato.email}}</td>
...
</tr>
...
ng-repeatefiltro
Inclusive,vimosquepodemosfiltraralistaadicionando | filter ao
finaldovalordadiretiva:
<tr ng-repeat="contato in contatos | filter: filtro">
ng-modeletwo-waydatabinding
Odado filtro,diferentedeAEedadiretiva ng-repeat,queapenas
lêemdadosdoescopodeumcontroller,permitetambémalterar,oquecarac-
terizao two-way data binding.Estaformadeassociaç ãoéfeitaatravés
dadiretiva ng-model:
<input ng-model="filtro" type="search"
placeholder="parte do nome">
AgoraquejáentendemososmecanismosbásicosdoAngularJS,nopróx-
imocapítulofaremossuaintegraçãocomnossoservidorExpress.
84

## Página 97

Capítulo5
IntegrandoAngularJSeExpress
“O homem tem mil planos para si mesmo. O destino, só um para cada. ”
–Mêncio
Nocapítuloanterior,vimosdesdeaconfiguraçãodoAngularJSemnosso
projetoatéousodediretivasparaampliarascapacidadesdonavegador,in-
clusivecomooAngularJSmantémnossomodelsincronizadocomnossaview
atravésde data binding. Porém,nãorealizamosnenhumaintegraçãoentre
front-endeback-end.Éjustamenteissoquefaremosnestecapítulo.
5.1 Oserviço $http
Nossofront-endatualmentetrabalhacomdadosestáticosdefinidosemnos-
soscontrollers.Aideiaagoraébuscaressesdadosdiretamentedenossoservi-
dor.

## Página 98

5.1. Oserviço$http CasadoCódigo
Nãoprecisamosnospreocuparcomoback-end,poisjácriamosserviços
queretornamdadosnoformatoJSON.Oquefaltaéa“cola”entrenossofront-
endenossoback-end.
OAngularJSpossuioserviço $httpresponsávelporrequisiçõesAjax.In-
jetamosesteserviçoemnossoscontrollerscomoqualqueroutroartefatodo
framework:
angular.module('contatooh').controller('ContatosController',
function($scope, $http) {
});
Injeção de dependências baseada em nomes
Nãoimportaaordemdosparâmetrosdonossocontroller, sãoos
nomes dos parâmetros que importam. Lembre-se que o sistema de
injeçãodedependênciasdoAngularJSébaseadoemnomes, logo, a
declaraçãoaseguirfuncionaperfeitamente,mesmorecebendoprimeiro
$http:
angular.module('contatooh').controller('ContatosController',
function($http, $scope) {});
Oserviço $httprecebecomoparâmetroumobjetocomasconfigu-
raçõesdarequisição.
{
method: /* método utilizado, pode ser GET, POST, PUT ou
DELETE */
url: /* endereço do recurso acessado */
data: /* objeto no qual cada propriedade será um parâmetro
na requisição */
}
Paraobtermosalistadecontatosdenossoservidoratravésdeumareq-
uisiçãodotipo GET,configuramososerviçodaseguintemaneira:
86

## Página 99

CasadoCódigo Capítulo5. IntegrandoAngularJSeExpress
$http({method: 'GET', url: '/contatos'});
Reparequeapropriedade datafoiomitidaporquenãoqueremosenviar
parâmetrosnarequisição.
AngularJSpossuiatalhosparaosmétodos GETe POSTatravésdas
funções$http.get(‘url’)e $http.post(‘url’).
Mascomoteracessoaoresultadodarequisiç ão?Parapodemosentender
comclarezacomoo $httpfunciona,precisamosrevisitarumadasformas
maisutilizadas:ousode callbacks.
5.2 Programação assíncrona e callback HELL
TodarequisiçãoAjaxéassíncronapornaturezaenuncasabemosquandoela
seráconcluídadefato. Éporissoqueumaestratégiacomumépassarpara
essasfunçõesumcallback,aquelafun çãoqueguardanossalógicaqueserá
chamadapelafun çãoassíncronaassimqueelaforconcluída.Inclusive,pode-
moscapturarnocallbackoresultadodafun ção.
Vejamosumexemplonoqualrealizaremoscincoaçõesassíncronasnase-
quência.Aprimeirabuscaoscontatosatravésdeumarequisiçãocom $http.
Logoemseguida,elessãoexibidosemodificados.Depois,osdadossãoen-
viadosnovamenteparaoservidor.Porfim,exibimosumamensagemparao
usuárioindicandoqueaoperaçãofoibem-sucedida:
function exibeContatos(contatos, callback) {
/*
Exibe os contatos na tela e logo em seguida
passa os contatos para a função de callback
*/
callback(contatos);
}
function modificaContatos(contatos, callback) {
/*
87

## Página 100

5.2. ProgramaçãoassíncronaecallbackHELL CasadoCódigo
Modifica os contatos seguindo algum critério
e depois chama o callback com contatos modificados.
*/
callback(contatos);
}
function atualizaContatos(contatos, callback) {
/*
Recebe os contatos modificados e
envia novamente para o servidor para que
sejam gravados. No final, chama o callback
*/
callback(contatos);
}
/* A seguir, a "pyramid of DOOM" ou ninho de amafagafa */
$http.get('/contatos', function(contatos) {
exibeContatos(contatos, function(contatos) {
modificaContatos(contatos, function(contatosModificados) {
atualizaContatos(contatosModificados,
function(contatos) {
$scope.mensagem = {
texto: 'Contatos atualizados com sucesso'
};
});
});
});
});
Vocênãoprecisameditardurantemuitotemposobreocódigoanterior
paraverquesualegibilidadenãoéumadasmelhoresequetodasasnossas
funçõesforamobrigadasareceberumcallback,oquepoluisuainterfacede
uso.Existeatéumnomeparaisso: callbackHELL.
88

## Página 101

CasadoCódigo Capítulo5. IntegrandoAngularJSeExpress
CallbackHELL
OcallbackHELLéumproblemaqueaparecenaprogramaç ãoassíncrona
quandoprecisamosexecutarcódigosassíncronosordenadamente.Paracon-
seguirmosoresultadodesejado,precisamosaninharcallbacks,oquecom-
prometelegibilidadeedificultamanuten çãodonossocódigo.
PyramidofDOOM
OcallbackHELLvisualmenteécaracterizadopela pyramidofDOOM,
umtriângulodeitadoqueficaevidentecomoaninhamentodasfun çõesde
callback.
Existeaindaoutroproblemaquetangeotratamentodeerros. Usarum
trye catchnãofuncionaráemnossocódigo:
/* não funciona */
try {
$http.get( '/contatos', function(contatos) {
exibeContatos(contatos, function(contatos) {
modificaContatos(contatos, function (contatosModificados) {
atualizaContatos(contatosModificados,
function(contatos) {
$scope.mensagem = {
texto: 'Contatos atualizados com sucesso'
};
});
});
});
});
} catch(erro) { /* nunca é chamado */
/* trata o erro */
};
Comoocódigoéassíncrono,elenãoestaránapilhanomomentoemque
o tryforavaliado.
Sãoporessesmotivosque $httpnãotrabalhadaformacomovimos.
Eleutilizaumpadrãobemdefinidoqueveremosaseguir.
89

## Página 102

5.3. Promises:combatendoocallbackHELL CasadoCódigo
5.3 Promises: combatendo o callbackHELL
O $http,nolugardereceberumcallbackdiretamenteemsuachamada,
trabalhaumpoucodiferente:eladevolveumvalor.
var contatos = $http({method: 'GET', url: '/contatos'});
Espereumpouco! Se $httpdevolveumvalorquenormalmenteseria
acessívelapenasemumafun çãodecallbackpassadacomoparâmetro,isso
significaquesuachamadaésíncrona? Suaexecuç ãobloqueiaaleiturado
nossocódigoatéquesejaconcluída?
Nãoexatamente. Oexemploaseguirexibenoconsoleotextoantesde
concluirarequisição:
var contatos = $http({method: 'GET', url: '/contatos'});
console.log("total de contatos " + contatos.length);
// exibe undefined
Seocódigoanteriortemproblema,porqueentãoo $http,emvezde
retornaralistadecontatosdoservidor,nãofazissodentrodeumafun çãode
callbackpassadacomoparâmetro? MesmoquecaiamosnocallbackHELL,
sabemosquenossocódigofuncionará.
OpadrãoPromise
Oprimeiropassoparaentenderestemistérioésaberque $httpnão
retornaalistadecontatos,masuma promise(promessa)dequeeletentará
buscaressesdados:
var promise = $http({method: 'GET', url: '/contatos' });
Uma promiseéumobjetoqueforneceráoresultadofuturodeuma
ação. Noexemploanterior,comoestamosexecutandoumarequisiç ãoas-
síncrona,nãosabemosquandoelanosdevolveráseuresultado,sendoassim,
ficamoscoma promessadesuadevolução,sua promise.
Fazendoumaanalogia:quandoalguémnosprometealgo,temosapenas
suapromessa,poisnãosabemosquandoelaserácumprida.Independentede
elaserrcumpridaounão,tocamosnossavida.Porém,sabemosoquepode
90

## Página 103

CasadoCódigo Capítulo5. IntegrandoAngularJSeExpress
acontecerseapromessaforcumpridaounão. Éporissoqueuma promise
possuiestados.
Estadosdeumapromise
Uma promisepossuitrêsestadosedependendodessesestados,açõessão
executadas:
•fulfilled:quandoa promiseébem-sucedida;
•rejected:quandoa promiseérejeitada;
•failed:quandonãoénembem-sucedidanemrejeitada.
Uma promise que foi fullfilled ou rejected não pode ser
fullfilledou rejectednovamente.
Asfunçõesthenecatch
Uma promisepossuiométodo then,querecebecomoparâmetroscall-
backs.Oprimeiroéexecutadoquandoostatusdapromisefor fulfilled;
osegundo,paraosestados rejectede failed.
function obterDados(retorno) {
/* faz algo com o retorno */
}
var promise = $http.get('/contatos');
promise
.then(obterDados, function(erro) {
console.log(erro.status)
console.log(erro.statusText)
});
);
Porém,oAngularJSintroduzafun ção catch,quepermiteisolarocall-
backdosestados rejectede failed:
function obterDados(retorno) {
/* faz algo com o retorno */
91

## Página 104

5.3. Promises:combatendoocallbackHELL CasadoCódigo
}
var promise = $http.get('/contatos');
promise
.then(obterDados)
.catch(erro) {
console.log(erro.status)
console.log(erro.statusText)
}
);
Nesseexemplo, atravésdoparâmetro retorno, temosacessoapro-
priedadesespeciaisquenospermitemacessarosdadosretornados,inclusive
obtermensagensdeerroenviadaspeloservidor:
•data:o bodydarespostatransformadoeprontoparausar;
•status:númeroqueindicaostatusHTTPdaresposta;
•statusText:textoHTTPdaresposta.
Aindaépossívelteracessoaoobjeto headere config,esteúltimocom
asconfiguraçõesutilizadasnarequisição.
Encadeamentodafunçãothen
Podemosencadearachamadaàfun ção then, garantindoquenosso
códigoexecutenasequência.Vejamosnossoexemplo,antesdominadopelo
callback HELLeagorautilizando promises:
function exibeContatos(contatos) {
/*
Exibe os contatos na tela
*/
return contatos;
}
function modificaContatos(contatos) {
92

## Página 105

CasadoCódigo Capítulo5. IntegrandoAngularJSeExpress
/*
Modifica os contatos seguindo algum critério
*/
return contatos;
}
function atualizaContatos(contatos) {
/*
Recebe os contatos modificados e
envia novamente para o servidor para que
sejam gravados.
*/
return contatos;
}
var promise = $http.get('/contatos');
promise
.then(exibeContatos)
.then(modificaContatos)
.then(AtualizaContatos)
.then(function(contatos) {
$scope.mensagem =
{texto: 'Contatos atualizados com sucesso'};
})
.catch(erro) { /* se algo der errado, trata */
console.log(erro.status)
console.log(erro.statusText)
}
);
Repare que cada função não precisou receber umcallbackcomo
parâmetro;utilizamosatéumretornonormaldefun ção.Esteretornoestará
disponívelparaapróximachamadaàfun ção then.
93

## Página 106

5.3. Promises:combatendoocallbackHELL CasadoCódigo
Tratamentodeerro
A promisepermitetratarerrosemumúnicolocal,dentrodafun çãocatch.
Seuma promisefor rejected, failedoualgumaexce çãoforlan çada,
temosumúnicolocalparatrataresseserros.
Asfunçõessuccesseerror
Oobjeto $httpadicionaconvenientementeemsuas promisesasfunções
successeerror. Aprimeirarecebeocallbackqueseráexecutadoquandoa
promisefor fulfilled.Jáasegunda,ocallbackqueseráexecutadoquando
a promisefor rejectedou failed.
var promise = $http.get('/contatos');
promise
.success(function(data, status, headers, config) {
$scope.contatos = data;
})
.error(function(statusText, status, headers, config) {
console.log(statusText);
console.log(status);
});
Aindapodemosomitiradeclaraçãodavariáveleomitirosparâmetros
quenãonosinteressam:
$http.get('/contatos')
.success(function(data) {
$scope.contatos = data;
})
.error(function(statusText) {
console.log(statusText);
});
94

## Página 107

CasadoCódigo Capítulo5. IntegrandoAngularJSeExpress
$http vs. $.ajax
ParaaquelesqueutilizamjQuery,o $httppossuisemelhançascom
$.ajax.AmbosfornecemumaAPIdebaixonívelpararealizarrequi-
siçõesAjax. Apesardecadaobjetotersuasfun çõesespecíficasparaa
tarefa,agrandediferen çaéaintegraçãode $httpcomociclodevida
doAngularJS,tambémchamadode digestcycle.
$httpnotificaráoframeworksemprequearequisiç ãoassíncrona
alteraralgummodel,garantindoasincronizaçãoentremodeleview.Se
poracasovocêutilizaro $.ajaxouqualqueroutrafun çãoespecializada
dojQueycomAngularJS,serávocêoresponsávelemavisaroframework
dasmodificaçõesrealizadas.chamando $scope.$apply():
$.ajax({
url: 'enderecoDoServico',
success: function(data, status, xhr) {
// atualiza informação em $scope
$scope.dadoQualquer = data;
// notifica o AngularJS da modificação
$scope.$apply();
}
})
Quandochamar $scope.$apply(),lembre-sequevocêestaráas-
sumindoaresponsabilidadedesincronizaraviewcomomodel,logo,
éaltamenterecomendadoquevocêutilize $httpououtroartefatodo
AngularJSquandonecessário.
Comopadrão promise,nossocódigoficamaislegível,poisganhacara
decódigosíncrono,mesmoquetenhamosumaoumaisfun çõesassíncronas.
Nãoprecisamosnemnospreocuparseafun çãoésíncronaouassíncrona,
poisteremosagarantiadequetodasserãoexecutadasnaordememqueas
chamarmosatravésdafunção then.
Otema promiseébemamploeporagoraoquesabemosésuficientepara
continuarmosnossacaminhadacomAngularJS.Casovocêqueirasabermais
95

## Página 108

5.4. Obtendocontatoscom $http CasadoCódigo
sobreoassunto, consulteaespecificaçãooficialem http://promises-aplus.
github.io/promises-spec/.
5.4 Obtendo contatos com $http
Agoraquevocêaprendeuque $httpretornauma promiseecomoexecutar
umcódigoquandoelaforbem-sucedida,jápodemosrefatorarnosso Con-
tatosControllerparadeixardetrabalharcomdadosestáticoseobtê-losdo
nossoback-endfeitocomExpress:
// public/js/controllers/ContatosController.js
angular.module('contatooh').controller('ContatosController',
function($scope, $http) {
$scope.contatos = [];
$scope.total = 0;
$scope.filtro = '' ;
$scope.incrementa = function() {
$scope.total++;
};
$http.get('/contatos')
.success(function(data) {
$scope.contatos = data;
})
.error(function(statusText) {
console.log("Não foi possível obter a lista de
contatos");
console.log(statusText);
});
});
Certifique-sedequeoservidorestejarodandoevejaoresultado. Tudo
devecontinuarfuncionando.
96

## Página 109

CasadoCódigo Capítulo5. IntegrandoAngularJSeExpress
Aúnicadiferen çaéquenossosdadosvieramdenossoservidor. Aliás,
vocêpodeconsultaroconsolecasoalgumacoisatenhasaídoerrada. Não
sepreocupeaindacomumamensagemamigávelparaousuário,atacaremos
esseproblemamaistarde.
Refatorandoaexibi çãodototaldecontatoscadastrados
Podemosaproveitareatualizarnossalógicaqueexibeototaldecon-
tatos cadastrados. Vamos remover a função $scope.incrementae o
atributo $scope.total. Agora, via AE,exibimosotamanhodoarray
$scope.contatosdiretamenteemnossaview:
<!-- public/partials/contatos.html -->
<p>Contatos cadastrados: {{contatos.length}}</p>
Todavezquenovoscontatosforemadicionadosouremovidos,nossaview
exibiráfidedignamenteototaldecontatosporcausado data binding.
$http?Existealgomaisabstrato?
Poderíamosusar $httppararealizara“cola”entrenossofront-ende
nossoback-end,porém,comoutilizamosopadrãoRESTemnossoservidor,
podemosutilizarumobjetoespecializadoedemaisaltonívelparaconsumir
nossos REST Endpoints.
5.5 O módulo ngR esource: trabalhando em
alto nível
VimoscomorealizarrequisiçõesAjax,assíncronaspornatureza,atravésdo
serviço$httpecomoeleutilizaopadrãopromiseparaajudarnalegibilidade
emanutençãodenossocódigo,evitandoassimo callback HELL.
Apesarde $httpserfuncional,AngularJSpossuiumserviçodemaisalto
nívelchamado $resource,específicoparaconsumirRESTEndpoints!Issoé
excelente,umavezquenossasrotascriadasnoExpressseguemestepadrão.
Oserviço $resourcenãofazpartedocoredoAngularJS,logo,pre-
cisamosdomódulo ngResourceparaqueeleestejadisponívelparanós.
Issonãoéumproblema,podemosbaixá-loatravésdo bower:
97

## Página 110

5.6. ConsumindoRESTEndpointscom $resource CasadoCódigo
bower install angular-resource#1.3 --save
Nãopodemosesquecerdeimportá-loemnossapágina index.html,
logoapósaimportaçãodomódulo ngRoute:
<script src="vendor/angular-resource/angular-resource.js">
</script>
Vocêdeveselembrarqueissoaindanãoésuficienteequeaindapre-
cisamosindicarquenossaaplicaçãofaráusodomóduloemnossoarquivo
main.js:
// public/js/main.js
var app = angular.module('contatooh',['ngRoute', 'ngResource']);
Reparequeagoranossaaplicaçãodependededoismódulos: ngRoute
e ngResource,ambosdefinidosnoarraypassadocomoparâmetroparaa
função angular.module.
Até aqui, toda burocracia a respeito da importação do módulo
ngResource já foi atendida. EmContatosController, precisamos
substituir $httppor $resource,artefatodisponibilizadopelomódulo
ngRoute:
angular.module('contatooh').controller('ContatosController',
function($scope, $resource) {
// código existente omitido
}
Muitobem!Substituímos $httppor $resourceparapodermostra-
balharemaltonívelcomnossosRESTEndpoints.Porém,aindafaltaalterar
alógicadenossocontrollerparaqueelafaç ausode $resource.
5.6 Consumindo RESTE ndpoints com $resource
Agoraquetemosinjetado $resourceemnossocontroller,podemosobter
umareferênciaparaorecurso contatosemnossoservidor.Paraisso,pas-
samospara $resourceoidentificadorúnicodesterecurso,emnossocaso,
/contatos:
98

## Página 111

CasadoCódigo Capítulo5. IntegrandoAngularJSeExpress
var Contato = $resource('/contatos');
Oserviço$resourcenosdevolveumobjetoquepermiterealizaruma
sériedeoperaçõesseguindoopadrãoRESTparaorecurso /contatos.O
nomedavariávelestáemmaiúscula,algointencionalparadiferenciá-lode
umapossívelvariávelquerepresenteomodelparacontato.
Nossoobjetivoérealizarumaconsultaaonossoserviçoeobteralistade
contatos.Paraestafinalidade,existeafun ção query.Afun ção,pordebaixo
dospanos,montaumarequisiçãodotipo GETparaorecurso /contatosem
nossoservidor.Ecomoestamostrabalhandocomumarequisiç ãoassíncrona,
podemospedirqueelanosdevolvauma promise:
var promise = Contato.query().$promise;
Otrâmiteaseguirjáéconhecido. Sabemosqueuma promisepossuias
funçõesthene catch.
promise
.then(function(contatos) {
$scope.contatos = contatos;
})
.catch(function(erro) {
console.log("Não foi possível obter a lista de contatos");
console.log(erro);
});
Umpoucoverbosonossocódigo? Podemosenxugá-lo. Nolugardere-
cebermosuma promise,podemospassarparaafun ção queryduasfunções:
aprimeira,umcallbackdesucesso;easegunda,umcallbackdeerro.Nosso
controllerficaráassim:
angular.module('contatooh').controller('ContatosController',
function($resource, $scope) {
$scope.contatos = [];
$scope.filtro = '' ;
99

## Página 112

5.6. ConsumindoRESTEndpointscom $resource CasadoCódigo
var Contato = $resource('/contatos');
Contato.query(
function(contatos) {
$scope.contatos = contatos;
},
function(erro) {
console.log("Não foi possível obter a lista de
contatos");
console.log(erro);
}
);
});
Deixandomaisclaranossaintenç ão
Podemosdeixaraindamaisclaranossainten çãodebuscaroscontatos
criandoafun ção buscaContatoemovendoparadentrodelaachamadade
Contato.query():
angular.module('contatooh').controller('ContatosController',
function($resource, $scope) {
$scope.contatos = [];
$scope.filtro = '';
var Contato = $resource('/contatos');
function buscaContatos() {
Contato.query(
function(contatos) {
$scope.contatos = contatos;
},
function(erro) {
console.log("Não foi possível obter a lista de
contatos");
console.log(erro);
}
100

## Página 113

CasadoCódigo Capítulo5. IntegrandoAngularJSeExpress
);
}
buscaContatos();
});
Deixando claro o que é executado na inicialização do
controller
Imaginequevocêtenhaváriasfun çõesparaseremchamadanaini-
cializaçãodeseucontroller. Nestecaso, vocêpoderiacriarafun ção
scope.init(ouqualqueroutronome)enelachamartodasasfun ções
dequeprecisanainicialização,deixandoseucódigomaisclaro:
$scope.init = function() {
buscaContatos();
tarefa1();
tarefa2();
};
$scope.init();
Emumprimeiromomento, $resourcenãoparecetrazergrandesvan-
tagens,maselasaparecerãoàmedidaqueformosrealizandooutrasoperações.
Aliás,precisamosimplementarafuncionalidadederemo çãodecontatos
denossalista.Primeiro,precisaremoscriararotadeexclusãoemnossoservi-
dorExpress,paradepoisaintegrarmoscomoAngularJS.
5.7 Adicionando rota de exclusão ao Express
VimosnoscapítulosanterioresqueestamosutilizandoopadrãoREST.Tanto
issoéverdadequeutilizamososerviço $resourcedoAngularJSespecial-
izadonestepadrão.
Precisamoscriarumarotaparaexclusãodecontatos.Umprerrequisitoé
queelasigaopadrãoRESTedevesercapazdereceberumidentificadorpara
ocontatoquedesejamosremoverdalista.
101

## Página 114

5.7. AdicionandorotadeexclusãoaoExpress CasadoCódigo
Configurandoarota
Se pensarmos em REST, o verbo HTTP indicado para nossa ação é
DELETE.ResolvemosissofacilmentecomoExpress,porque,alémdeeleuti-
lizarafun ção app.getpararotascomoverbo GET,eletambémpossui
app.post, app.puteaté app.delete.
Vamosadicioná-laemnossoarquivoderotasreferenteaorecursocon-
tato:
// contatooh/app/routes/contato.js
module.exports = function (app) {
var controller = app.controllers.contato;
/* rotas anteriores */
app.delete ('/contatos', controller.removeContato);
};
Criamos uma rota para o verboDELETE utilizando o identificador
/contatos. Tambémjáindicamosqualfunçãochamaremosequeainda
precisasercriadanocontrollerdecontatos.Porém,antesdeacriarmos,pre-
cisamosresolverumproblema.
Parametrizandonossarota
Emalgummomento,nossaaplicaçãoutilizandoAngularJSprecisaráen-
viaro IDdocontatoselecionadodalistaparaqueelesejaremovido.Como
capturaresse ID?
Bastaalterarumpouquinhooidentificadordenossorecurso. Desta
forma:
app.delete( '/contatos/:id', controller.removeContato);
Vimosemumdoscapítulosanterioresqueoidentificadorpodetrabalhar
comumcuringa.Emnossocaso,escolhemosonome :id.Oidentificador
/contatos/éconstante,oquemudaéocódigodorecursoquequeremos
apagar:
Vejamosumexemplo:
102

## Página 115

CasadoCódigo Capítulo5. IntegrandoAngularJSeExpress
http://localhost:3000/contatos/1
Omesmoendere çoparaorecurso,dependendodoverbo,geraações
diferentes.Sefor GET,retornaocontatoidentificadopelo ID1;seoverbo
for DELETE,apagaráocontato.
ObtendooIDdocontatonocontroller
Muito bem, já entendemos como configurar nossa rota de exclusão,
porém,comoacessaremoso IDdocontatopassadopelaURLdentronosso
controller?Jávimosissonase ção2.12.
Primeiro,vamoscriarafun ção removeContatoemnossocontroller.
// contatooh/app/controllers/contato.js
/* outras funções */
controller.removeContato = function(req, res) {
console.log('API: removeContato: ');
};
Existeapropriedade req.params. Nãocustalembrarquenelatemos
acessoaosparâmetrosenviadosnarequisição.Comoutilizamosnaconfigu-
raçãodenossarotaocuringa :id,podemosacessaro IDdocontatoenviado
atravésde req.params.id:
// contatooh/app/controllers/contato.js
/* outras funções */
controller.removeContato = function(req, res) {
var idContato = req.params.id;
console.log('API: removeContato: ' + idContato);
};
Agora basta implementar a lógica que busca o contato pelo seu ID,
removendo-o,casoexista:
103

## Página 116

5.8. Express:organizandomelhornossasrotas CasadoCódigo
// contatooh/app/controllers/contato.js
controller.removeContato = function(req, res) {
var idContato = req.params.id;
contatos = contatos.filter(function(contato) {
return contato._id != idContato;
});
res.send(204).end();
};
Reparenachamadaàfun ção res.send.Elarecebecomoparâmetroo
status code 204(No Content)daoperação.Emnossocaso,indicamosque
aoperaçãocorreunormalmente.
Agoraquejátemosnossarotadeexclusãodevidamenteconfigurada,va-
mosimplementarnoladodoclienteachamadadestarotaatravésdoAngu-
larJS.
5.8 Express: organizando melhor nossas rotas
CriamosnoExpressnossasrotas,porémvocêjádeveterreparadoquetanto
arotadelistagemquantoadeinclusãoutilizamomesmoidentificador,mu-
dandoapenasoverbo;amesmacoisaocorrecomasrotasdepesquisaeex-
clusão:
// app/routes/contato.js
module.exports = function (app) {
var controller = app.controllers.contato;
app.get('/contatos', controller.listaTodos);
app.post('/contatos', controller.salvaContato);
app.get('/contatos/:id', controller.obtemContato);
app.delete( '/contatos/:id', controller.removeContato);
};
Poderíamosatéisolarosidentificadoresqueserepetememumavariável
paradepoisreaproveitá-los,porémoExpress,apartirdasuaversão4,trouxe
umnovosistemaderotascomrecursosinteressantes.
104

## Página 117

CasadoCódigo Capítulo5. IntegrandoAngularJSeExpress
Umadasmaneirasdeinteragirmoscomosistemaderotasépormeiode
instânciadoExpressatravésdafun çãoroute,passandocomoparâmetroo
identificadordarota:
// app/routes/contato.js
module.exports = function (app) {
var controller = app.controllers.contato;
app.route( '/contatos');
app.route( '/contatos/:id');
};
Reparequeagoranãotemosmaisidentificadoresduplicados,massabe-
mosquecadaumdelesresponderáamaisdeumverboHTTP.Éporissoque
podemosencadearachamadaàsfun çõesget, post, deletee put:
module.exports = function (app) {
var controller = app.controllers.contato;
app.route( '/contatos')
.get(controller.listaTodos)
.post(controller.salvaContato);
app.route( '/contatos/:id')
.get(controller.obtemContato)
.delete(controller.removeContato);
};
Para um mesmo identificador, podemos associar diferentes verbos
HTTPs,tornandoadeclaraçãodenossasrotasmaisenxutaemaisfácilde
manter.
5.9 Removendo contatos da lista
Agoraqueadicionamosnoladodoservidorarotaparaexclusãodecontatos,
precisamosimplementarnoladodoclientesuachamadaatravésdoAngu-
larJS.
105

## Página 118

5.9. Removendocontatosdalista CasadoCódigo
Adiretivang-clickmaisumavez
Nosso primeiropasso será adicionara diretivang-clickno botão
Removerdenossaparcial contatos.html:
<!-- public/partials/contatos.html -->
...
<button
ng-click="remove(contato)"
class="btn btn-warning">
Remover
</buttom>
...
Reparequeestamoschamandoafun ção remove,queaindanãoexiste
emnossocontroller. Antesdecriá-la,percebaqueelarecebeumcontato
comoparâmetro.Masquecontatoéesse?Éocontatodalistanomomento
emquevocêclicarnobotão! Sendoassim,nossocontrollerserácapazde
receberumareferênciaparaestecontato!
Vamos criar a fun ção remove em nosso controller
ContatosController:
// public/js/controllers/ContatosController.js
$scope.remove = function(contato) {
console.log(contato);
};
Experimenterealizarumteste.Cliqueemcadacontatodalistaeverifique
seosseusdadosforamimpressosnoconsoledonavegador.
Agoraquejásabemoscomoobterumareferênciaaocontatoselecionado,
podemossubstituironossologporumachamadaaoserviço Contato,mas,
destavez,nolugardechamarmosafun ção query,chamaremosafun ção
delete:
$scope.remove = function(contato) {
Contato.delete();
};
106

## Página 119

CasadoCódigo Capítulo5. IntegrandoAngularJSeExpress
Oproblemaéquesuachamadaestámuitogenérica.Qualcontatoquer-
emosremover?Éporissoqueelarecebeumobjetocomoparâmetroe,nele,
indicamosonomedoparâmetroqueseráenviadonarequisiç ãoeseuvalor:
$scope.remove = function(contato) {
Contato.delete({id: contato._id});
};
Estamosdizendoparaqueoserviçoenvienoparâmetro idovalorde
contato._id,istoé,o IDdocontatoselecionado. Comonossoservidor
estápreparadoparaextrairessainformação,tudodeveriafuncionar,porém,
precisamosrealizarumanovaconsultalogoapósaexclusãodocontato,para
quenossalistasejaatualizada. Atépoderíamosremoveroitemdalistano
ladodocliente,masoptaremospelaprimeiraop ção.
Lembradas promises? Poisé, afunção deletepoderetornaruma
promise.Apartirdaí,jásabemosoquefazer:
$scope.remove = function(contato) {
var promise = Contato.delete({id: contato._id}).$promise;
promise
.then(buscaContatos)
.catch(function(erro) {
console.log("Não foi possível remover o contato");
console.log(erro);
});
};
Repareque,paraafun ção then,passamosafun ção buscaContatos,
queseráchamadaapenasquandoarequisiç ãoforbem-sucedida. Porfim,
nafunção catchtratamoseventuaiserrosquepossamacontecerdurantea
requisição.
Há um açúcar sintático para a função delete. Além do primeiro
parâmetro,queindicaosparâmetrosdarequisiç ão,podemospassarmais
dois:oprimeiro,umcallbackdesucesso;osegundo,umcallbackdefalha:
$scope.remove = function(contato) {
Contato.delete({id: contato._id},
buscaContatos,
107

## Página 120

5.9. Removendocontatosdalista CasadoCódigo
function(erro) {
console.log('Não foi possível remover o contato');
console.log(erro);
}
);
};
Porbaixodospanos,a promisecontinuasendoutilizada,porémocódigo
émenosverboso.
Nossocontrollerfinalficaráassim:
angular.module('contatooh').controller('ContatosController',
function($resource, $scope) {
$scope.contatos = [];
$scope.filtro = '';
var Contato = $resource('/contatos/:id');
function buscaContatos() {
Contato.query(
function(contatos) {
$scope.contatos = contatos;
},
function(erro) {
console.log(erro)
}
);
}
buscaContatos();
$scope.remove = function(contato) {
Contato.delete({id: contato._id},
buscaContatos,
function(erro) {
console.log('Não foi possível remover o contato');
console.log(erro);
}
);
108

## Página 121

CasadoCódigo Capítulo5. IntegrandoAngularJSeExpress
};
});
Jápodemostestaranovafuncionalidade. Experimenteremoverumou
outrocontato.Semprequevocêapagaralistainteira,bastapararereiniciar
oservidorparaquealistavolte.
5.10 As diretiv as ng-hide e ng-show
Podemosexibirparaousuárioamensagem“Nãohácontatoscadastrados”
quandoalistaestivervazia.Nãopodemossimplesmenteadicionarestetexto
emnossapágina,poiseleseriasempreexibido. Éaiqueentraadiretiva
ng-hide. Elementoscomestadiretivaficaminvisíveisquandoovalorde
ng-hidefor true.
Naparcial contatos.html,imediatamenteapósoparágrafoqueexibe
ototaldeusuárioscadastrados,vamosadicionarnossoavisoatravésdeoutro
parágrafocomadiretiva ng-hide. Elaconsultaráotamanhodoarrayde
contatos. EmJavaScript,qualquernúmerodiferentedezeroéconsiderado
true. Porfim,adicionaremosaclasse text-infodoBootstrapparadar
umapelovisual:
<p class="text-info" ng-hide="contatos.length">
Não há contatos cadastrados
</p>
Testeoresultado. Vocêveráqueoparágrafoéexibidoapenasquando
alistadecontatosestivervazia,masoproblemaéqueoparágrafoanterior
tambéméexibido.Aideiaéqueelefaçaocontráriodonossoparágrafo:ele
sódeveserexibidosehouverelementosnalista. Paraisso,existeadiretiva
ng-show.Oelementosóseráexibidoseoseuvalorfor true:
<p ng-show="contatos.length">
Contatos cadastrados: {{contatos.length}}
</p>
<p class="text-info" ng-hide="contatos.length">
Não há contatos cadastrados
</p>
109

## Página 122

5.10. Asdiretivasng-hideeng-show CasadoCódigo
Testemaisumavez,experimenteremovertodosositensdalista. Tudo
devecontinuarfuncionandocomoesperado.
Exibindoavisosparaousuário
Atéagora,tratamospossíveiserrosquepodemacontecerquandoaces-
samosnossoback-endatravésdoAngularJS,inclusivelogamosessasinfor-
mações. Oproblemaéqueousuárioficarásemumfeedbacksobreoque
aconteceu. Quetalusarmosamesmaestratégiaquefizemoscomospará-
grafosparaexibirmensagensamigáveisparaousuário?
Vamosadicionarumanovapropriedadenoescopodocontroller:
$scope.mensagem = {texto: ''};
Em contatos.html,adicionamosoparágrafoimediatamenteapósa
divcomaclasse jumbotron:
<!-- jumbotron vem antes -->
<p ng-show="mensagem.texto">
{{mensagem.texto}}
</p>
Aideiaésimples.Quandohouverumerro,preenchemosotextodoob-
jetomensagem.Setudocorrerbem,limpamosseuvalor.Usaremosadiretiva
ng-showparaexibiramensagem,apenasseelaexistir,pois undefinedé
avaliadocomo falseemJavaScript:
Alterandonossocontroller:
angular.module('contatooh').controller('ContatosController',
function($resource, $scope) {
$scope.contatos = [];
$scope.filtro = '';
$scope.mensagem = {texto: ''};
var Contato = $resource('/contatos/:id');
110

## Página 123

CasadoCódigo Capítulo5. IntegrandoAngularJSeExpress
function buscaContatos() {
Contato.query(
function(contatos) {
$scope.contatos = contatos;
$scope.mensagem = {};
},
function(erro) {
console.log(erro);
$scope.mensagem = {
texto: 'Não foi possível obter a lista'
};
}
);
}
buscaContatos();
$scope.remove = function(contato) {
Contato.delete({id: contato._id},
buscaContatos,
function(erro) {
$scope.mensagem = {
texto: 'Não foi possível remover o contato'
};
console.log(erro);
}
);
};
});
Agoraquejásabemoslistareremovercontatos,emostrarmensagensper-
sonalizadasparaousuário,precisamosadicionarmaisumafuncionalidade
emnossoprojeto:exibirocontatoselecionadodalista.
5.11 Exibindo contato selecionado
Vamosimplementarafuncionalidadedeexibiç ãodocontatoselecionado
na lista. Para isso, precisamos primeiro incrementar nossa página
contato.html,quesóexibeotítulodapágina.Utilizaremosmaisumavez
111

## Página 124

5.11. Exibindocontatoselecionado CasadoCódigo
oBootstrapparadarmosum“look”profissionalcompouquíssimoesforço:
<!-- partials/contato.html -->
<h1 class="text-center">Contato</h1>
<p ng-show="mensagem.texto">
{{mensagem.texto}}
</p>
<form>
<div class="form-group">
<label for="nome">Nome completo</label>
<input type="text" class="form-control" id="nome"
name="nome" required ng-model="contato.nome">
</div>
<div class="form-group">
<label for="email">Email</label>
<div class="input-group">
<span class="input-group-addon">@</span>
<input type="email" class="form-control" id="email"
placeholder="email@exemplo.com" name="email"
ng-model="contato.email" required>
</div>
</div>
<div>
<button type="submit" class="btn btn-primary">
Salvar
</button>
<a href="#/" class="btn btn-default">Voltar</a>
</div>
</form>
112

## Página 126

5.11. Exibindocontatoselecionado CasadoCódigo
// public/js/main.js
// ...
$routeProvider.when('/contato/:contatoId', {
templateUrl: 'partials/contato.html',
controller: 'ContatoController'
});
// ...
Rotas doAngularJS
Repare que, no lado do cliente, usamos a rota
/contato/:contatoId no singular para acessarmos um contato
específico,saindodopadrãoREST.Nãosepreocupe,poisestasrotassão
processadasnoladodoclienteeadiferen çadenomesentre /contatos
e /contatonosajudarácomosistemaderotasdoAngularJS.
Nossarotalocaltrabalhacomumcuringa.Estecuringa,quandopassado
paraarota /contato,atornaumarotaválida.Reparesuaassociaç ãocom
ContatoController:
// public/js/controllers/ContatoController.js
angular.module('contatooh').controller('ContatoController',
function($scope, $routeParams) {
console.log($routeParams.contatoId);
});
Emnossocontroller,temosacessoaoIDdocontatopassadonaURLpro-
cessadapelosistemaderotasdoAngularJS.AgoraprecisamosqueessaURL
sejamontadadinamicamentetodavezqueousuárioclicarsobreonomedo
contatodalista.
Vamosalterarapáginaprincipal contatos.html,adicionandoadire-
tiva ng-hefnaâncoraquecontémonomedocontato.
<!-- public/partials/contatos.html -->
<a ng-href="#/contato/{{contato._id}}">{{contato.nome}}</a>
114

## Página 127

CasadoCódigo Capítulo5. IntegrandoAngularJSeExpress
Repare que o valor da diretiva é composto por umaAngular
Expression que adiciona o ID do contato processado pela diretiva
ng-repeat.UmpontoimportanteéqueaURLcome çacom #,sinalizando
queaquelaURLdeveserprocessadanoladodocliente,evitandoqueelaseja
submetidaparaoservidor.
ng-href
Usamosadiretiva ng-hrefnolugardoatributo hrefparagarantir
queolinksófuncionedepoisdeoAngularJStersidocarregadoede-
poisdeeleteravaliadoaAngularExpressionassociadaàdiretiva.Nesse
ínterim,qualquercliquenolinkéinofensivo.
Agora que já conseguimos acessar qualquer contato de nossa lista,
disponibilizandoseuIDpara ContatoController,precisamosbuscá-lo
láemnossoservidorparaquepossamospopularosdadosdoformuláriocom
suasinformações.
Utilizaremosnovamente $resource,comadiferen çadequechamare-
mosafun ção getparabuscarocontatopeloseuID.Aideiaaquiétraduzir
arotadoAngularJSparaumaoperaç ãonoladodoservidor:
// public/js/controllers/ContatoController.js
// injetamos $resource
angular.module('contatooh').controller('ContatoController',
function($scope, $routeParams, $resource) {
// aqui continua no plural, é a rota no lado do servidor
var Contato = $resource('/contatos/:id');
Contato.get({id: $routeParams.contatoId},
function(contato) {
$scope.contato = contato;
},
function(erro) {
$scope.mensagem = {
115

## Página 128

5.11. Exibindocontatoselecionado CasadoCódigo
texto: 'Não foi possível obter o contato.'
};
console.log(erro);
}
);
});
Jápodemostestarselecionandoumcontatodalista.Emnossoservidor
Express,temosarota /contatos/:contatoIdqueesperareceberoIDdo
contatocomoparâmetro. Comoestamosutilizando $resource,afun ção
getéinteligenteosuficienteparamontaraURLparanossoRESTEndpoint!
ComojáhavíamosadicionadosasAEsnapágina contato.htmlno
iníciodocapítulo,oAngularJSsaberáexibirnossosdados.
Lidandocomnovoscontatos
Jáaprendemosabuscarcontatosselecionadosdalista,massevocêlem-
brardonossolayout,nossaparcial contatos.htmlpossuiobotão“Novo
Contato”,queemteoriadeveriaabriraparcial contato.htmlcomofor-
mulárioembrancoparaquepossamosadicionarumnovocontato.
Oproblemaéquearotaparaaparcialqueexibeocontatosóexibiráa
páginasealgumIDforpassado,enocasodeumnovocontatoaindanão
temosID!SeomitirmosoID,osistemaderotasdoAngularJSnãodetectará
arotacomoválidaenosdirecionaráparaaparcial contatos.html.
Podemos resolver esse problema adicionando uma nova rota em
main.jstambémparaaparcial contato.html,comadiferen çadeque
elanãorecebeparâmetros:
// public/js/main.js
// ...
$routeProvider.when('/contato', {
templateUrl: 'partials/contato.html',
controller: 'ContatoController'
});
// ...
Agora, se tentarmos acessar a URL (http://localhost:3000/#/contato)
nossocontrollerserácarregadoeapáginaexibida,porémnãofazsentido
116

## Página 129

CasadoCódigo Capítulo5. IntegrandoAngularJSeExpress
realizarmosumabuscanoservidorsempassarmosumID.
Podemosajustarissofacilmenteadicionandoumacláusula IFemnosso
controller:
// public/js/controllers/ContatoController.js
angular.module('contatooh').controller('ContatoController',
function($scope, $resource, $routeParams) {
var Contato = $resource('/contatos/:id');
if($routeParams.contatoId) {
Contato.get({id: $routeParams.contatoId},
function(contato) {
$scope.contato = contato;
},
function(erro) {
$scope.mensagem = {
texto: 'Contato não existe. Novo contato.'
};
}
);
} else {
$scope.contato = {};
}
});
Nocódigoanterior,realizaremosabuscaapenasseoIDdocontatofor
passadoparaosistemaderotasdoAngularJSeadicionamosumobjetosem
propriedades em $scope.contato. Isso não dará erro em nosso for-
mulário,quedependedosatributosdocontato? Não,porqueo two-way
data binding criaráaspropriedadesdinamicamentenoobjetocasoelas
nãoexistam,atravésdadiretiva ng-model.
Precisamosajustarnossobotão“NovoContato”.Aprimeiracoisaétorná-
loumlink,paraquepossamosdispararnossosistemaderotas.Depois,adi-
cionaradiretiva ng-href:
<a ng-href="#/contato" class="btn btn-primary">Novo Contato</a>
117

## Página 130

5.12. Salvandoumcontato CasadoCódigo
Pronto!Agoraquetemostudonolugar,jápodemosimplementarnossa
lógicaquesalvaocontato.
5.12 Salv ando um contato
Precisamosimplementaralógicaqueincluiouatualizaumcontato.Sabemos
queatravésdadiretiva ng-clickpodemosexecutaralgumalógicaemnosso
controller,porém,comoestamosutilizandocomponentesdoHTML5em
nossapágina,podemospegarcaronaemseusistemadavalidaç ão.
Adiretivang-submit
Nolugardeusarmosadiretiva ng-clicknobotão“Salva”,utilizaremos
adiretivang-submitnoformuláriodapágina,permitindoqueobrowserpro-
cesseseuscomponentes,logo,realizandoavalidaç ãodoformulário:
<!-- public/partials/contato.html -->
<form ng-submit="salva()">
Em ContatoController.js:
$scope.salva = function() {
// lógica de salvamento
};
Agora precisamos implementar a lógica de salvamento do contato.
Primeiro,vamosimaginarquevocêtenhaselecionadoocontatodalistae
desejaatualizá-lo. Vocêlembraquemretornouessecontatoparanós? Sim,
nossoserviçoContato,criadoatravésde $resource.Essecontatoretor-
nadopossuioutrascaracterísticasadicionadasdinamicamentepeloserviço
Contatoqueatéagoranemsabíamosqueexistiam. Então,parasalvarum
contatobasta:
$scope.salva = function() {
$scope.contato.$save();
};
Estaéumadasvantagensdetrabalharmoscom $resource. Qual-
querobjetoretornadoatravésdeleéincrementadocomumasériedefun ções
118

## Página 131

CasadoCódigo Capítulo5. IntegrandoAngularJSeExpress
voltadasparapersistência,emnossocaso,persistêncialigadaa REST End-
points.
Afun ção $savegerapordebaixodospanosumarequisiç ãodotipo
POSTqueenviapara http://localhost/contatososdadosdocontato.Esequis-
ermosexibirumamensagemdesucesso? Afun çãoretornauma promisee
sabemosqueelapossuiafun ção then:
$scope.salva = function() {
$scope.contato.$save()
.then(function() {
$scope.mensagem = {texto: 'Salvo com sucesso'};
// limpa o formulário
$scope.contato = new Contato();
})
.catch(function(erro) {
$scope.mensagem = {texto: 'Não foi possível salvar'};
});
};
Estamosquaselá! Oproblemaéquenossalógicafuncionaparaalter-
ação,masequandoforumnovocontato?Elenãoécriadoapartirdoserviço
$resource,logo,nãotemafun ção $save.
Podemosfacilmenteresolverisso.Quandoestivermoscriandoumnovo
contato,nolugardeelerecebercomovalor {},elereceberáumanovain-
stânciadoserviço Contato:
// public/js/controllers/ContatoController.js
// código omitido
$scope.contato = new Contato();
// código omitido
Pronto!Agorateremosacessoàfun ção $save.Nãocustalembrarqueos
atributosdocontatoserãoadicionadosdinamicamente,atravésdaassociação
ng-modelque,alémdeler,écapazdealterardadosdinamicamente.
Serealizarmosumteste,receberemosumamensagemamigáveldizendo
quenãofoipossívelsalvarocontato.Abrindooconsoledonavegador,vemos
amensagem:
119

## Página 132

5.13. AdicionandorotadegravaçãoaoExpress CasadoCódigo
failed to load resource: the server responded with a status of
404 (Not Found)
Issoaconteceporquenãotemosumarotapreparadaparalidarcomo
verboPOSTemnossoservidor.Precisamosprogramá-la.
Emnossoexemplo,usaremos POSTparainclusãoeatualização.Oservi-
dordistinguiráentreasduasoperaçõesverificandonocontatoapresen çaou
nãodeum ID.
E o verboPUT?
No mundo REST, atualização está associada ao verboPUT, mas
$resourcenãodásuporteaesteverbo.Atépoderíamosimplementá-lo
emnossoserviço,masoautorpreferiuutilizar POSTparaasduasoper-
ações,emumatentativadeseguirasconven çõesdoAngularJS.
Vamosvoltarparanossoback-endeimplementararotaqueestáfaltando.
5.13 Adicionando rota de grav ação ao Express
Precisamosimplementarnossarotaqueincluieatualizaumcontato. Para
isso,énecessárioregistrarprimeiroarota:
// contatooh/app/routes/contato.js
app.post('/contatos', contatoController.salvaContato);
AgoraprecisamosadicionaralógicanocontrollerdoExpress.Oprimeiro
passoéadicionarlogonoiníciodocontrollerumcontadorquejácome çaem
três,quefuncionarácomoIDdenovoscontatos:
// contatooh/app/controllers/contato.js
var ID_CONTATO_INC = 3 ;
Paraterminar,precisamosdalógicaqueadicionaoualteraumcontato.
Dealgumamaneira,devemosteracessoaocontatoquefoienviadoatravésda
requisição POST.NoExpress,bastaacessarmos req.bodyparateracesso
aocorpodamensagem,emnossocaso,ocontatocomsuaspropriedades:
120

## Página 133

CasadoCódigo Capítulo5. IntegrandoAngularJSeExpress
// contatooh/app/controllers/contato.js
controller.salvaContato = function(req, res) {
var contato = req.body;
contato = contato._id ?
atualiza(contato) :
adiciona(contato);
res.json(contato);
};
function adiciona(contatoNovo) {
contatoNovo._id = ++ID_CONTATO_INC;;
contatos.push(contatoNovo);
return contatoNovo;
}
function atualiza(contatoAlterar) {
contatos = contatos.map(function(contato) {
if(contato._id == contatoAlterar._id) {
contato = contatoAlterar;
}
return contato;
});
return contatoAlterar;
}
Reparequetantoaatualizaçãoquantoinclusãoretornamcomoresposta
ocontato.Nocasodeumainclusão,elejávemcomo IDpreenchido.
Pronto!Bastareiniciaroservidoretentarincluirecadastraralgunscon-
tatos.
121

## Página 134

5.14. Serviços:organizandomelhornossocódigo CasadoCódigo
5.14 Serviços: organizando melhor nosso
código
ImagineseemalgummomentoaURLdenosso REST Endpointmuda.Precis-
aríamosalterá-laemtodososlugaresqueelaforreferenciada.Pormaisínfimo
queissopossaparecer,seriainteressanteseconseguíssemoscompartilharum
mesmocódigoentrenossoscontrollerse,quandoocódigomudasse,todos
ficassemsabendodessaalteração.
OAngularJSpermitecriarserviçosreaproveitáveisentrecontrollers,aliás,
épossívelquecontrollerstroqueminformaçõesatravésdessesserviços.
Serviço guardando estado?
Podeparecerumpoucoestranhoparaalgunsumserviçoguardares-
tado,masnomundodoAngularJSelepodeservirparaestepropósito.
Aideiaaquiéisolarmososdetalhesdecriaç ãodenosso $resource,
jáquenossoscontrollersnãoprecisamconheceraURLdo REST Endpoint
utilizada.Queremosumbaixoacoplamento.
Oprimeiropassoécriaroarquivo ContatoService.js.Utilizaremos
osufixo“Service”paraevitarconfusãocomoutrosscriptsjáexistentes,oAn-
gularJSnãoérígidonaescolhadeseunome.
Claro,nãopodemosesquecerdeimportá-lo,depoisdocoredoAngularJS
eantesdaimportaçãodoscontrollers:
<!-- public/au -->
<script src="js/services/ContatoService.js"></script>
Utilizandoainstânciadenossomóduloprincipal,utilizamosafun ção
factory,querecebecomoprimeiroparâmetroonomedoserviçoe,nose-
gundo,afun çãoqueodefine.Reparequenafun çãotemoscomodependência
$resource:
// public/js/services/ContatoService.js
122

## Página 135

CasadoCódigo Capítulo5. IntegrandoAngularJSeExpress
angular.module('contatooh').factory('Contato',
function($resource) {
return $resource('/contatos/:id');
});
Pronto,oquenossoserviçoretornaéumainstânciade $resourcejá
configuradaeprontaparauso.Todaserviçocriadocom factorydevere-
tornarumobjeto.
E a função service?
AngularJS também possui a função service com o mesmo
propósito, porém, no lugar de retornar um objeto, ela retorna uma
função.NaprópriadocumentaçãodoAngularJS,elessugeremousode
factory,pois serviceentraráemdesuso.
Agora, basta trocarmos a injeção de $resource nos controllers
ContatoController e ContatosController pelo nome de nosso
serviço,Contato.Refatorandonossocódigo,temos:
// public/js/controllers/ContatoController.js
angular.module('contatooh').controller('ContatoController',
function($scope, $routeParams, Contato) {
// apagar a linha que constrói o resource
}
// public/js/controllers/ContatosController.js
angular.module('contatooh').controller('ContatosController',
function(Contato, $scope) {
// apagar a linha que constrói o resource
}
Testemaisumavezaaplicaç ão. Tudodevecontinuarfuncionandoper-
feitamente,poisnãoalteramosocomportamentodocódigo,apenassuaor-
ganização.
123

## Página 136

5.14. Serviços:organizandomelhornossocódigo CasadoCódigo
Excelente! Aolongodestecapítuloaprendemosaintegrarnossofront-
end com nosso back-end com AngularJS através dos serviços$http e
$resource,esteúltimoespecializadonoconsumode REST Endpoints.Vi-
mostambémque $resourcenãofazpartedocoredoAngularJSequefoi
precisobaixaromódulo ngResouce,aliásutilizamosoBowermaisumavez
paraestatarefa.
Ondeestáapersistência?
Nossaaplicaçãofuncionamasatéagoranãopersistimosdadosdever-
dade.PrecisamosintegrarnossosRESTEndpointscomumbancodedados.
SabemosqueoMongoDBéatecnologiadepersistênciadaMEANStack.
Antesderealizarmosessaintegraç ão,precisamosconhecerobásicodeste
bancoNoSQL.Éoqueveremosnopróximocapítulo.
124

## Página 137

Capítulo6
MongoDB:bancodedados
baseadoemdocumento
“Não é o tamanho do cão na luta, é o tamanho da luta no cão”
–MarkTwain
6.1 Relacional vs.NoSQL: há banco vencedor?
Talvezumdosmaisbem-sucedidosprojetosdesoftwareemnossahistória
sejaobancodedadosrelacional.Seusprincípioscriadosem1970continuam
firmesepresentesembancodedadoscomerciaiseopensources,constituindo
oparadigmarelacional.
Estetipodebancopossuiumaestruturatabularerelacionalbaseada
fortementeemesquemase,nele,realizamosconsultaseresolvemosseusrela-
cionamentosatravésdeumalinguagempadrãochamadaSQL(Structured

## Página 138

6.1. Relacionalvs.NoSQL:hábancovencedor? CasadoCódigo
Query Language),maisnotadamenteopadrãoANSI92adotadopordiver-
sosbancos.
Comotempo,umnovoparadigmaapareceu:oNoSQL.Essetermofoi
cunhadoem1998pelodesenvolvedorCarloStrozziemaistarderefor çado
porEricEvansparaindicarbancosquenãoseguemopadrãoSQL.Longede
serumtermopejorativo,aideiadoNoSQLéadebancosquenãosebaseiam
emrelacionamentosnememesquemas,tãoprezadosnosbancosdedados
relacionais. Nele,pelaausênciadeesquemas,avalidaçãoeintegridadedos
dadossãoderesponsabilidadedaaplicaç ão.
Umaquestãoarquitetural?
Cadaparadigmaapresentadoatacaproblemasdiferentesesuaescolha
nãoéumadecisãopuramentepreferencial,masdenecessidadedoprojeto,
tangendoaspectosarquiteturaisemaisabstratos.Realizarjuízodevalorem
cadaumadasabordagenssemumcontextopropriamenteditoprovavelmente
resultaráemdebatesinflamados.Precisamosdeumcontextoapartirdoqual
delimitaremosoquequeremosresolver.
Delimitandoocontexto:impedância
NocontextodenossaaplicaçãoContatooh,tantoumbancodedadosrela-
cionalquantoumNoSQLdemandarádodesenvolvedoratraduçãodosdados
retornadosdobancoparaalgomanipulávelnalinguagemdeprogramaçãoes-
colhida,emnossocaso,JavaScript.
Essadiscrepânciadaestruturadosdadosarmazenadosnobancodeda-
doseasestruturasdedadosemmemóriaéchamadade impedância[2]eem
algummomentoodesenvolvedorprecisaráresolvê-la. Quantomenorfora
impedância,menostrabalhodeconversãoodesenvolvedorteráentreasdi-
versascamadasquecompõemseusistema.
126

## Página 139

CasadoCódigo Capítulo6. MongoDB:bancodedadosbaseadoemdocumento
6.2 Buscando a menor impedância possível:
JSON“everywhere”
Emnossabuscapelamenorimpedânciapossível, équaseimpossívelnão
destacar o JSON, uma estrutura textual bastante semelhante ao objeto
JavaScript.Nãopodiaserdiferente,jáqueoprotocoloHTTPtransfereapenas
texto.Alémdisso,oformatoJSONdemandaqueaschavesvenhamsempre
entreaspas,diferentedeumobjetoJavaScriptnoqualseuusoéopcional.
Ascaracterísticasqueacabamosdeverrefor çamaideiadeimpedância
e,pormaisqueoJSONsejasemelhanteaumobjetoJavaScript,aindapre-
cisaráhaverumatraduçãodasinformações.Atéagorausamosostermosde
maneiraintercambiávelporqueoAngularJSrealizao parsedoJSONedeob-
jetosJavaScriptparanósdemaneiratransparente.Écomoseelefizessealgo
dotipo:
var contatoJSON = '{"nome":"nome do contato",
"email":"email do contato"}';
// transforma JSON em objeto
var contatoObjeto = JSON.parse(contatoJSON);
console.log(contatoObjeto);
Object {nome: "nome do contato", email: "email do contato" }
// transforma objeto em JSON/texto
contatoJSON = JSON.stringify(contatoObjeto);
'{"nome":"nome do contato","email":"email do contato"}'
JáutilizamosoJavaScriptObjectNotation(JSON)comoestruturadeda-
dostantoemnossoservidorNode.jsquantoemnossoclienteAngularJS.Será
quepodemosadotarumaestruturasemelhantenobancodedados?
BancosNoSQL
Existemnomercadobancosquearmazenamdadosemestruturasidên-
ticasousemelhantesaoJSON,comoo ApacheCouchDB (http://couchdb.
apache.org),JasDB(http://www.oberasoftware.com),NeDB(NodeEmbed-
dedDatabase)(https://github.com/louischatriot/nedb), Terrastore(https:
//code.google.com/p/terrastore)entreoutros.Qualdelesescolher?
127

## Página 140

6.3. InstalaçãodoMongoDB CasadoCódigo
QuetaloMongoDB?
Aboanotíciaéquejátemosumbancoescolhido,bastavoltarmosao
acrônimodaMEANStackparavermosqueo“M”éde MongoDB(http:
//www.mongodb.org/).
OMongoDBéumbancodedadosbaseadoemdocumentocomaltaper-
formanceedisponibilidadeedefácilescalabilidade.Porém,essascaracterísti-
castêmseupreço:nemtodasaspropriedadesACID(atomicidade,consistên-
cia,isolamentoedurabilidade)tãoprezadasnosbancosdedadosrelacionais
sãoimplementadaspelobanco.
Alternativ as aoMongoDB
Qualquerbancoquepermitagravarelerumaestruturadedados
semelhanteaoJSONébem-vindoàMEANStack,porém,oMongoDB
aindaéomaisevangelizado, inclusiveporValeriKarpov, criadordo
acrônimoequenapresentedatadaescritadesdelivrotrabalhanaem-
presacriadoradoMongoDB.
Começandodozero
Antesdepensarmosemqualquerintegraç ãodonossoback-endcom
nossobanco,precisamosinstalaroMongoDB.Depoisqueoambientees-
tiver pronto, aprenderemos os conceitos como documento,ObjectId,
collectionsecomorealizarconsultas.
6.3 Instalação do MongoDB
ExistemmuitasmaneirasdeseinstalaroMongoDB.Variamdeacordocom
seusistemaoperacionalepodemserconsultadasnoendere çohttp://docs.
mongodb.org/manual/installation.
Éaltamenterecomendávelutilizaraversãode64Bitsemproduç ãopelo
fatodeobanconaversãode32Bitsserlimitadoaumtamanhodenomáximo
doisgigabytes.Aversãoutilizadaduranteaelaboraç ãodestelivrofoia2.6.6
de64BitsparaMacOS.
128

## Página 141

CasadoCódigo Capítulo6. MongoDB:bancodedadosbaseadoemdocumento
Umaformadeverificarseainstalaç ãodoMongoDBestáfuncionandoé
trabalhandocomseuclientedelinhadecomando: o mongo shell. Éoque
veremosnase çãoaseguir.
6.4 Utilizando o mongo shell
OMongoDBpossuio mongoshell,umclienteemlinhadecomandoque
nospermiteinteragircomsuasinstâncias. Paraacessá-lo,bastadigitarmos
noterminalocomando mongoseguidodedoisparâmetros:
$ mongo --port 27017 --host localhost
MongoDB shell version: 2.6.6
connecting to: test
Reparequenocomandoanteriorpassamososparâmetros --porte
--hostcomosvalores 27017e localhost,respectivamente.Essesval-
oresjásãoopadrãodomongoshelljustamenteporelestambémseremo
padrãodainstânciadoMongoDBquerodaemsuamáquina.
Vamos parar o mongo shell com a tecla de atalhoCONTROL + C
(Windows e MacOS) echamá-loapenascomocomando mongo:
$ mongo
MongoDB shell version: 2.6.6
connecting to: test
Logodeinício,éexibidanoshellaversãodoclientequeestamosusandoe
queestamosconectadosaobanco test.EsteéobancopadrãodoMongoDB
noqualpodemosrealizarqualqueralteraçãosemmedo.
6.5 O conceito de documento
UmdospontosquetornaoMongoDBaindamaisinteressantenaMEAN
Stackéamaneiracomotrabalhacomdocumentos,conceitofundamental
paraestebancoNoSQL.
129

## Página 142

6.6. OtipoObjectId CasadoCódigo
Característicasdodocumento
Um documento pode ser armazenado em diferentes formatos hi-
erárquicoscomoXMLouJSONcomosdadosassociadosaumaestrutura
dechaveevalor.Éatravésdeumachaveespecíficadodocumentoquetemos
acessoaovalorassociado.Porém,dosdiversosformatosexistentesnomer-
cado,oMongoDBarmazenaseusdocumentosnoformato BSON(Binary
JSON),muitoparecidocomJSON.Comparemosaestruturadessesdoisfor-
matos:
// JSON
{
"nome" : "Flávio Almeida"
}
// BSON
{
"_id" : ObjectId( "5303e0649fd139619aeb783e")
"nome" : "Flávio Almeida"
}
Agrossomodo,adiferen çaentreBSONeJSONmoranaquantidadedos
tiposdedadossuportadosemcadaumadeles: enquantoJSONpossuiseis
tipos( Array, Boolean, null, Number, Objecte String)oBSON,pos-
suimaisde15tipos!Veremosalgunsdessestipos,porémháumquemerece
destaquenestemomento: ObjectId.
6.6 O tipoObjectId
TododocumentocriadopeloMongoDBrecebeautomaticamenteachave
_idcontendocomovalorpadrãoumobjetodotipo ObjectId.Voltando
aoexemplodase çãoanterior:
// BSON
{
"_id" : ObjectId( "5303e0649fd139619aeb783e")
"nome" : "Flávio Almeida"
}
130

## Página 143

CasadoCódigo Capítulo6. MongoDB:bancodedadosbaseadoemdocumento
Sefizermosumaanalogiacomobancodedadosrelacional, _idéuma
colunaquerepresentaachaveprimáriadatabela.Sendoassim,nãopodemos
termaisdeumdocumentocomummesmo ObjectId,contudo,veremos
maisàfrentequeoMongoDBtrabalhacomoconceitode collection,
algoquelembratabelasnomundorelacional. Dessamaneira,ummesmo
ObjectIdpodeexistiremdiferentes collections.
QuandovocêinstalaoMongoDBemsuamáquina,pelomenosuma
instânciavocêterárodando. Cadainstânciapodeterváriosbancosde
dadosecadabancopodetermuitas collections.
6.7 Criando o banco da aplicação
Estamosconectadosaobanco test,masseráqueexistemoutrosbancos?É
atravésdocomandoshowdbs quelistamostodososbancosdainstânciado
MongoDBaqueestamosconectados:
> show dbs
test 0.203125GB
Porenquanto,sótemosobanco testesomoscapazesdeverquantoele
ocupadeespaçoemdisco.
Precisamos agora criar um banco que contenha os dados da nossa
aplicação Contatooh. Por conveniência, criaremos um banco de mesmo
nome,apenascome çandocomletraminúsculaatravésdocomando use
contatooh:
> use contatooh
switched to db contatooh
Sabemosqueobancoaindanãoexiste, porém, oMongoDBirácriá-
lo. Omaisinteressanteéquerecebemosamensagem switched to db
contatooh.Omongoshellestánosavisandoqueoobjeto dbagoraaponta
paraobanco contatooh.Seráverdade?Seimprimirmosoobjeto db,ver-
emosqueelerealmenteapontaparanossonovobanco:
131

## Página 144

6.8. Collectionseinserçãodedocumentos CasadoCódigo
> db
contatooh
Avariáveldbnosforneceumatalhoparaobancoemqueestamostrabal-
handonomomento.Seporacasousássemosocomando use test,nossa
variáveldbapontariaparaobanco test.
Agoraquejásabemosacriarumbanco,aprenderemoscomoincluirdoc-
umentosatravésdomongoshell.
6.8 C ollections e inserção de documentos
O shell do MongoDB permite criar variáveis nos moldes da linguagem
JavaScript.Issoéfantástico,porqueseaestruturadedadosBSONdoMon-
goDB é parecida com JSON. Podemos criar um objeto JavaScript com a
seguinteestrutura:
> var contato = { "nome" : "Nome do Contato"}
Inclusive,podemosimprimiravariávelnoconsoleapenasdigitandoseu
nome:
> contato
{ "nome" : "Nome do Contato"}
Aideiaagoraéincluiresteobjetoemnossobanco contatooh. Não
sepreocupeseanossaestruturaaindanãoéumBSON,porqueopróprio
MongoDBresolveráessaimpedâncianomomentodainclusão.
Temos um problema: queremos adicionar um contato a uma tabela
chamada contatos, mas sabemos que o MongoDB não trabalha com
tabelase,sim, collectionsparaagrupardocumentos. Comocriaruma
collectionparadepoisincluirnossocontato?
Podemosfazerasduascoisasdeumasóvez! Vamosconvencionarque
onomeda collectionquearmazenaránossoscontatosserá contatos.
Logo,nossainclusãoficaráassim:
> var contato = { "nome" : "Nome do Contato" }
> db.contatos.insert(contato)
WriteResult({ "nInserted" : 1 })
132

## Página 145

CasadoCódigo Capítulo6. MongoDB:bancodedadosbaseadoemdocumento
Repareque,atravésdoobjeto db,acessamosumatributoinexistente
chamado contatos.PelanaturezadinâmicadeobjetosJavaScript,oatrib-
uto contatosseráadicionadodinamicamenteem dbeomaisfantás-
ticoéque,porconven ção,eleseráa collectionquedesejamoscriar.Na
mesmalinha,chamamosafun ção insert,querecebeunossoobjetocomo
parâmetro.
Criando collection pela primeira vez
Quandoadicionamosumdocumentoaomesmotempoemqueesta-
moscriandoumacollection,teremosumatrasonotempodegravaç ão.
Issosóacontecenaprimeirainclusão,devidoaotempogastoparacri-
açãoda collection.
Recebemoscomoresposta WriteResult({ "nInserted" : 1 }),
indicando que acabamos de incluir um documento nacollection
contatos.
Seráquetudorealmentefuncionou?Primeiro,vamoslistartodososban-
cosdenossainstânciaeverificarseobanco contatoohfoicriado:
> show dbs
contatooh 0.203125GB
test 0.203125GB
Ótimo,láestánossobanco contatooh! Agora,precisamoslistarsuas
collections:
> show collections
contatos
system.indexes
Excelente!Vemosquenossobancoexisteequea collectionfoicriada.
Vocêtambémdeveterreparadoem system.indexes. Comoopróprio
nomejádiz,elaéuma collectioncontendoosíndicesdenossodocu-
mento.
133

## Página 146

6.9. Buscandodocumentos CasadoCódigo
6.9 B uscando documentos
Jásabemoscriarbancose collections,eatéinserirdocumentosnelas,
porémaindanãoverificamosserealmentenossocontatofoigravado. Para
isso,pediremosànossa collectionque“ache”nossodocumentoatravés
dafunção find:
> db.contatos.find();
{
"_id" : ObjectId("53e1534bf8a1b188b3f276d1"),
"nome" : "Nome do Contato"
}
Aexecuçãodocomandoapresentaumaestruturadedadossemelhanteao
contatoqueincluímos,porémháapresen çadeumachaveausentenoobjeto
original: _id.
Deondeveio_idmesmo?
Comovimosnoiníciodocapítulo,documentossãogravadosnoformato
BSON,muitosemelhanteaoJSON,mascomsuportemaioratiposeque
possuicomoidentificadorum ObjectId. Éjustamenteum ObjectIdo
valordachave _id.Nãoentraremosnosdetalhesdecriaç ãoutilizadospara
geraressenúmeroautomaticamente,mastenhacertezadequenuncateremos
ObjectId’sduplicadosem collections.Dessamaneira,garantimosum
identificadorúnicoparanossodocumento.
Descartandobanco
Pronto,agoraqueaprendemosobásico,quetalcome çarmosnovamente
dozeroparairmosmaislonge?Precisamosapagarnossobancorecémcriado.
Como? Pedimosatravésdoobjeto db,querepresentanossobanco,oseu
descarteatravésdafun ção db.dropDatabase():
> db.dropDatabase()
{ "dropped" : "contatooh", "ok" : 1 }
134

## Página 147

CasadoCódigo Capítulo6. MongoDB:bancodedadosbaseadoemdocumento
Tenha certeza de que você está no banco certo!
Tomemuitocuidadonahoraemquefordescartarumbanco.Tenha
certezadequeoobjeto dbrealmenteapontaparaobancodesejado.Esta
operaçãoéirreversível.
Agoraquedescartamosnossobanco,podemoscome çarnovamentecom
umnovinhoemfolhaparacontinuarmosnossoaprendizado:
> use contatooh
switched to db contatooh
Criamospelasegundavezobanco contatooh.
Incluindováriosdocumentos
Paraquemaistardepossamosrealizarconsultas, precisamospopular
nossobanco. Primeiro,criaremostrêsobjetosquerepresentamumcontato
com nomee email:
> var contato1 = { "nome" : "Contato 1 Mongo",
"email" : "cont1@empresa.com.br" }
> var contato2 = { "nome" : "Contato 2 Mongo",
"email" : "cont2@empresa.com.br" }
> var contato3 = { "nome" : "Contato 3 Mongo",
"email" : "cont3@empresa.com.br" }
Agora,vamosadicioná-losemnossobanco:
> db.contatos.insert(contato1)
WriteResult({ "nInserted" : 1 })
> db.contatos.insert(contato2)
WriteResult({ "nInserted" : 1 })
> db.contatos.insert(contato3)
WriteResult({ "nInserted" : 1 })
Oqueacontecerásetentarmosadicionarumquartocontatoinexistente?
135

## Página 148

6.10. Oobjetocursor CasadoCódigo
> db.contatos.insert(contato4)
ReferenceError: conta4 is not defined
DamesmamaneiraqueemumcódigoJavaScriptrecebemosumamen-
sagemdeerro,omongoshellnosdáumapistadoproblema.Issoéinteres-
sante,principalmentesevocêfazusopesadodoclienteemlinhadecomando.
Eagora? Comolistarnossoscontatos? Utilizaremosamesmafun ção
findusadaanteriormente:
> db.contatos.find()
{
"_id" : ObjectId("530b825db61fac75624ccfd1"),
"nome" : "Contato 1 Mongo",
"email" : "cont1@empresa.com.br"
}
{
"_id" : ObjectId("530b8260b61fac75624ccfd2"),
"nome" : "Contato 2 Mongo",
"email" : "cont2@empresa.com.br"
}
{
"_id" : ObjectId("530b85aab61fac75624ccfd7"),
"nome" : "Contato 3 Mongo",
"email" : "cont3@empresa.com.br"
}
Vocêjádeveterpercebidoqueafun ção findretornatodososdocu-
mentosdenossa collection,porémhámaiscoisasdoqueseuolhopode
ver!
6.10 O objeto cursor
Aprendemosnase çãoanterioralistarnossosdocumentosatravésdafun ção
find.Quetalguardarmosoresultadodafun çãoemumavariávelparadepois
imprimirmosseuvalor?
> var contatos = db.contatos.find()
> contatos
136

## Página 149

CasadoCódigo Capítulo6. MongoDB:bancodedadosbaseadoemdocumento
{
"_id" : ObjectId("530b825db61fac75624ccfd1"),
"nome" : "Contato 1 Mongo",
"email" : "cont1@empresa.com.br"
}
{
"_id" : ObjectId("530b8260b61fac75624ccfd2"),
"nome" : "Contato 2 Mongo",
"email" : "cont2@empresa.com.br"
}
{
"_id" : ObjectId("530b85aab61fac75624ccfd7"),
"nome" : "Contato 3 Mongo",
"email" : "cont3@empresa.com.br"
}
Funciona!Nossavariável contatoscontémtodosnossoscontatos.Será
mesmo?Vamosimprimi-lanovamente:
> contatos
Destavez,nadaacontece!Porquê?Issoocorreporquealistaretornada
pelométodo findda collectionnãoéumarraydeobjetos,masum
cursorcriadopeloMongoDB,quebuscaránossosdadosapenasquandopre-
cisarmos.
Quandoexecutávamosafun ção finddiretamenteouquandoguardá-
vamosseuretornoemumavariáveledepoisaimprimíamos,oqueoshell
doMongoDBnaverdadefaziaerachamarafun ção next()docursor,que
retornavaumcontatoacadachamada.
Omongoshellerainteligentechamandoessafun çãováriasvezesatéque
todososcontatosfossemlistados.Éporissoque,aotentarmosimprimirno-
vamenteocursor,nadaéimpresso,porqueocursorjáatingiuofinaldalista.
Quetalfazermosumtesteparaverificarseissoérealmenteverdade?No
lugardeimprimirmosavariável contatosnoconsole,chamaremosman-
ualmenteométodo next():
> var contatos = db.contatos.find()
> contatos.next()
137

## Página 150

6.11. Buscandocomcritério CasadoCódigo
{
"_id" : ObjectId("530b825db61fac75624ccfd1"),
"nome" : "Contato 1 Mongo",
"email" : "cont1@empresa.com.br"
}
> contatos.next()
{
"_id" : ObjectId("530b8260b61fac75624ccfd2"),
"nome" : "Contato 2 Mongo",
"email" : "cont2@empresa.com.br"
}
> contatos.next()
{
"_id" : ObjectId("530b85aab61fac75624ccfd7"),
"nome" : "Contato 3 Mongo",
"email" : "cont3@empresa.com.br"
}
Realmente,paracadachamadade next,oprimeiro,osegundoeoter-
ceirocontatosãoimpressosnoconsole.Porém,sechamarmosafun çãopela
quartavezteremosumerro:
> contatos.next()
error hasNext: false at src/mongo/shell/query.js:127
Esteerroaconteceuporquenãohámaiselementosnocursor,ouseja,
elejáfoitotalmentepercorrido. Éporissoqueocursorpossuiafun ção
hasNext,queretorna trueapenasseexistirumpróximoelemento.
Quetalagoraavan çarmosumpoucomaisemtermosdeconsultano
MongoDB?Éissooqueveremosnapróximase ção.
6.11 Buscando com critério
Muitasvezesqueremosencontrarapenasumdocumento,porexemplo,o
primeiroqueencontrarmosemnossa collection.Paraissoexisteafun ção
findOnepresenteemtoda collection:
> db.contatos.findOne()
{
138

## Página 151

CasadoCódigo Capítulo6. MongoDB:bancodedadosbaseadoemdocumento
"_id" : ObjectId("530b825db61fac75624ccfd1"),
"nome" : "Contato 1 Mongo",
"email" : "cont1@empresa.com.br"
}
Repare que, dos três contatos que havíamos cadastrados, apenas o
primeirofoiretornado.Faremosamesmacoisanovamente,sóquedessavez
guardandooresultadoemumavariável:
> var contato = db.contatos.findOne()
> contato.next()
TypeError: Object [object Object] has no method 'next'
Espereumpouco! Aprendemosqueafun ção findretornaumcursor
quenospermiteacessartodososdocumentosdenossa collectionatravés
dafunção next,masissoparecenãofuncionarquandousamos findOne.
Issoaconteceporqueafun ção findOnesempreretornaumobjetodo
banco,nãoumcursor.Comonãoháanecessidadedeiterarsobreumalista
dedocumentos,nãohánecessidadedeumcursor. Destaforma,podemos
imprimirquantasvezesquisermosavariável contato,queelaserásempre
exibida. Casoelafosseumcursor,depoisdeteratingidoseuúltimodocu-
mento,nadamaisseriaimpressonoconsole:
> contato
{
"_id" : ObjectId("530b825db61fac75624ccfd1"),
"nome" : "Contato 1 Mongo",
"email" : "cont1@empresa.com.br"
}
> contato
{
"_id" : ObjectId("530b825db61fac75624ccfd1"),
"nome" : "Contato 1 Mongo",
"email" : "cont1@empresa.com.br"
}
Nem sempre queremos listar todos os documentos de nossa
collection e muitas vezes queremos utilizar critérios na hora da
139

## Página 152

6.11. Buscandocomcritério CasadoCódigo
consulta. Banco de dados relacionais utilizam SQL com esta finalidade,
porémoMongoDBpossuiumalinguagemdeconsultaprópriabaseadano
tãofamiliarJSON.
Criandocritérios
CritériossãocriadosatravésdaestruturadedadosJSONesãopassados
paraasfun çõesfinde findOneda collection:
> var criterio = { "email" : "cont2@empresa.com.br" }
> var contato = db.contatos.find(criterio)
> contato
{
"_id" : ObjectId("530b8260b61fac75624ccfd2"),
"nome" : "Contato 2 Mongo",
"email" : "cont2@empresa.com.br"
}
Noexemploanterior,criamosumcritérioquenadamaisédoqueum
JSONcomachave emailrecebendoovalorquedesejamosbuscarnobanco.
OMongoDBéinteligenteparacompararachave emailcomamesmachave
presenteemtodososdocumentosdenossobanco,retornandoapenasaqueles
queatenderemocritériopassado.
find vs. find({})
Afunção findsemprerecebeumcritério,mesmoquandoeleéomi-
tido.Nasuaomissão,oMongoDBseencarregadepassarumobjetosem
chavescomocritério.Sendoassim,aschamadas find()e find({})
retornamomesmoresultado.
ExistealgoparecidocomolikedoSQL?
Esequisermosencontrartodososcontatosquecontenhamovalor tato
comopartedonome,ignorandomaiúsculaouminúscula?Sevocêéconhece-
dordeexpressãoregular,jásabearesposta. Podemospassarcomocritério
expressõesregulares:
140

## Página 153

CasadoCódigo Capítulo6. MongoDB:bancodedadosbaseadoemdocumento
> var criterio = { "nome" : /tato/i }
> var contatos = db.contatos.find(criterio)
Essacaracterísticapermitecriarconsultasversáteis, utilizandotodoo
poderdasexpressõesregulares.
Quantoscontatoscadastrados?
Podemossaberquantoscontatostemoscadastradosnobancosempre-
cisarmosretornarumcursor. Issoéfeitoatravésdafun çãocountchamada
diretamentena collectionpesquisada:
> db.contatos.count()
2
Inclusive,podemospassarumcritérioparaafun ção count:
> db.contatos.count({ "nome" : /to 2/i })
1
Nesseexemplo,contamosquantospossuemcomopartedonomeaex-
pressão to 2 nomodo case insensitive.
Umpoucomaissobreconsultas
Nãoéincomumumcontatotermaisdeume-mail:
> var contatoComEmails =
{
"nome": "Contato com emails",
"emails": ["contato@email.com.br", "pessoal@empresa.com.br"]
}
> db.contatos.insert(contatoComEmails)
WriteResult({ "nInserted" : 1 })
Muitasvezesqueremosencontrarumcontatoapartirdedeterminado
e-mail:
> db.contatos.find({"emails" : "pessoal@empresa.com.br"})
{
141

## Página 154

6.12. Queryselectors CasadoCódigo
"_id" : ObjectId("53eb582e7514ce1e85529195"),
"nome" : "Contato com emails",
"emails" : [ "contato@email.com.br",
"pessoal@empresa.com.br" ]
}
Essaconsultabuscaráoe-mailprocuradonalistadee-mailsdocontato.
6.12 Query selectors
Qualquercritériopassadoparaasfun çõesfinde findOneterãosuaschaves
consideradascomocláusulas AND.Massequisermosrealizarum OR?Para
isso,utilizaremosumdosvários queryselectors doMongoDB:
> db.contatos.find({
"$or" : [
{
"email" : "cont2@empresa.com.br"
},
{
"nome" : "Contato 1 Mongo"
}
])
Reparequeafun ção findrecebecomoparâmetroumobjetocoma
chave $or, umquery selector. O valor desta chave é um array com as
condiçõesquedesejamosincluir. Ocódigoanteriorlistaráoscontatosque
atendamaonossocritério.
Podemosaindaobtertodososcontatosquenãocontenhamcomoe-mail
cont2@empresa.com.br,atravésdo query selector $ne:
> db.contatos.find({
"email" : {
"$ne" : "cont2@empresa.com.br"
}
});
Os query selectors $ore $nesãodosgrupos comparisone logical,re-
spectivamente. Essesgrupospossuemoutrosseletoreseháoutrosgrupos.
142

## Página 155

CasadoCódigo Capítulo6. MongoDB:bancodedadosbaseadoemdocumento
VocêpodeobternaprópriapáginadoMongoDB(http://docs.mongodb.org/
manual/reference/operator/query/)umalistadetodososseletoresseparados
porgrupos.
6.13 Indexando documentos
Imaginesetivéssemos30milhõesdecontatosedesseuniversoquisésse-
mosencontraraquelesquepossuemdeterminadoe-mail? Emtermosde
critério,nãoprecisamosfazernada,poisaprendemosarealizarconsultascom
critérios.Porém,seráqueanossaconsultaserárápidaosuficiente?
Écomumnomundorelacionalacriaç ãodeíndicesparacolunascomu-
menteconsultadasparaaumentaraperformancedasbuscas. Issotambém
épossívelnoMongoDB.Podemosindicarquedeterminadachavedodocu-
mentoéindexadaatravésdafun ção ensureIndex:
> db.contatos.ensureIndex({ "email" : 1 })
{
"createdCollectionAutomatically" : false,
"numIndexesBefore" : 1,
"numIndexesAfter" : 2,
"ok" : 1
}
Reparequeafun ção ensureIndexrecebecomoparâmetroumJSON
comachavequequeremosindexar. Ovalor 1indicaquequeremosum
índiceascendente,masépossíveltrabalharnaordemdecrescenteutilizando
-1comovalor.
Podemosaindalistartodososíndicedeuma collectionatravésdafunção
getIndexes:
> db.contatos.getIndexes()
[
{
"v" : 1,
"key" : {
"_id" : 1
},
143

## Página 156

6.14. Retornandodocumentosparciais CasadoCódigo
"name" : "_id_",
"ns" : "contatooh.contatos"
},
{
"v" : 1,
"key" : {
"email" : 1
},
"name" : "email_1",
"ns" : "contatooh.contatos"
}
]
Alémdisso,épossívelcriaríndicesúnicos.Primeiro,apagaremosoíndice
queacabamosdecriaratravésdafun ção dropIndexda collectionque
recebecomoparâmetroonomedoíndicecriado:
> db.contatos.dropIndex('email_1')
{ "nIndexesWas" : 3, "ok" : 1 }
Agora,criamosnovamente,masdestavezcomoúnico:
> db.contatos.ensureIndex( { email: 1 }, { unique: true } )
{
"createdCollectionAutomatically" : true,
"numIndexesBefore" : 1,
"numIndexesAfter" : 2,
"ok" : 1
}
VejaquepassamoscomosegundoparâmetroumJSONcomachave
unique com valor true. Existem outras possibilidade para a criação
deíndicesevocêpodeconsultá-lasem http://docs.mongodb.org/manual/
reference/method/db.collection.ensureIndex/.
6.14 Retornando documentos parciais
Nãoéraroquerermostrabalharapenascomalgumaschavesdodocumento.
Atéagoraretornamossempreodocumentointeiro.Podemosmodificaresse
144

## Página 157

CasadoCódigo Capítulo6. MongoDB:bancodedadosbaseadoemdocumento
comportamentoindicandoquaischavesqueremosretornarpassandoumse-
gundoparâmetroparaafun ção findou findOne:
> db.contatos.find({}, { "nome" : 1})
{
"_id" : ObjectId("530b825db61fac75624ccfd1"),
"nome" : "Contato 1 Mongo",
}
{
"_id" : ObjectId("530b8260b61fac75624ccfd2"),
"nome" : "Contato 2 Mongo",
}
{
"_id" : ObjectId("530b85aab61fac75624ccfd7"),
"nome" : "Contato 3 Mongo",
}
Utilizamos novamente a função find, que recebe como primeiro
parâmetroocritério {}quenosretornarátodososcontatos. Osegundo
parâmetroéanovidade.Oparâmetroéumobjetoquecontémaschavesde-
sejadaseemnossocasoqueremosapenasumachave,o nome. Umolhar
atentodemonstraqueachavepossuiovalor 1. Issoéimportante,jáque
indicaparaoMongoDBquequeremosincluiraquelachavenaconsulta.
Por padrão, os documentos retornados vêm com seus respectivos
ObjectIds,mesmosemtermossolicitadoessainformaç ão. Podemosre-
solverissofacilmenteindicandoquaischavesqueremosexcluirdodocu-
mentoresultantedaconsulta.Oprocedimentoéomesmoquefizemosantes,
porém,nolugarde 1,usamosovalor 0:
> db.contatos.find({}, { "nome" : 1, _id : 0 })
{
"nome" : "Contato 1 Mongo"
}
{
"nome" : "Contato 2 Mongo"
}
{
"nome" : "Contato 3 Mongo"
}
145

## Página 158

6.15. Removendodocumentos CasadoCódigo
Jásabemospesquisardocumentosseguindoalgunscritérios,masnem
semprequeremosatualizá-los,muitasvezesqueremosremovê-los!
6.15 Removendo documentos
AremoçãodedocumentosnoMongoDBéfeitaatravésdafun ção remove
chamadadiretamentena collectionalvo:
> db.contatos.remove({ "email" : "cont1@empresa.com.br" })
WriteResult({ "nRemoved" : 1 })
Reparequecriamosocritériodamesmamaneiraquecriamosparanossas
consultas.Alógicaéamesma.
Vamosverificarsenossocontatofoirealmenteremovido:
> db.contatos.find()
{
"_id" : ObjectId("530b8260b61fac75624ccfd2"),
"nome" : "Contato 2 Mongo",
"email" : "cont2@empresa.com.br"
}
{
"_id" : ObjectId("530b85aab61fac75624ccfd7"),
"nome" : "Contato 3 Mongo",
"email" : "cont3@empresa.com.br"
}
Cuidado!
Sequisermosapagarirreversivelmentetodososdocumentosdenossa
collection,bastachamarafun ção db.removesemargumentos:
> db.contatos.remove()
Já aprendemos a adicionar, listar e a remover documento de nossas
collections,faltaaindaentendercomooMongoDBlidacomatualizações.
146

## Página 159

CasadoCódigo Capítulo6. MongoDB:bancodedadosbaseadoemdocumento
6.16 Atualizando documentos
Umbancodedadosnãoarmazenadadosapenas,elepermitequeessesdados
sejamatualizadosdeacordocomalgumcritério. Porexemplo,precisamos
atualizarocontatocome-mail cont3@empresa.com.br. Jáaprendemos
comoobtercontatosdeacordocomumcritério.
> var criterio = { "email" : "cont3@empresa.com.br" }
> var contato = db.contatos.findOne(criterio);
> contato
{
"_id" : ObjectId("530b85aab61fac75624ccfd7"),
"nome" : "Contato 3 Mongo",
"email" : "cont3@empresa.com.br"
}
Utilizamosafun ção findOneporquetemosinteresseemapenasum
contato. Aliás,nãocustalembrarqueoretornoseráumobjetoquerepre-
sentanossocontatoenãoumcursor,poisnãoutilizamosafun ção find.
Temoscertezadequetemosoobjetoqueestamosprocurando.Seráque
alterarsuachave nomeésuficienteparasincronizá-locomobanco?
> contato.nome = "Nome Alterado"
Agora,vamosbuscarnovamentedobanco,massemguardaroresultado
emumavariável:
> db.contatos.findOne(criterio)
{
"_id" : ObjectId("530b85aab61fac75624ccfd7"),
"nome" : "Contato 3 Mongo",
"email" : "cont3@empresa.com.br"
}
Nãofuncionou.Issoaconteceporquesomosnósosresponsáveispelasin-
cronizaçãodonossoobjetocomobanco,istoé,precisamosatualizarodoc-
umentopersistidopeloMongoDBcomosdadosdonovoobjeto.
147

## Página 160

6.16. Atualizandodocumentos CasadoCódigo
Afunçãoupdate
Para atualizar documentos, utilizamos a função update, também
chamadadiretamentena collectionquecontémnossodocumento. Ela
recebecomoprimeiroparâmetroocritériododocumentoprocuradoe,como
segundo,aschavesquedesejamosmodificarnodocumento.Emnossocaso,
estamosenviandooobjetointeirocomtodasassuaschaves:
> db.contatos.update(criterio, contato)
WriteResult({ "nMatched" : 1, "nUpserted" : 0 })
Seráqueelefoirealmenteatualizado?Vamoslistarnovamentetodosos
documentoseverificaraalteração:
> db.contatos.find()
{
"_id" : ObjectId("530b8260b61fac75624ccfd2"),
"nome" : "Contato 2 Mongo",
"email" : "cont2@empresa.com.br"
}
{
"_id" : ObjectId("530b85aab61fac75624ccfd7"),
"nome" : "Nome Alterado",
"email" : "cont3@empresa.com.br"
}
Quando realizamos nosso update, o console exibiu a mensagem
WriteResult({ "nMatched" : 1, "nUpserted" : 0 }), indi-
candoqueapenasumdocumentofoiencontradocomocritériopassado
atravésdachave nMatchedequenenhum nUpsertedfoirealizado.Mas
oquesignificaesse nUpserted?Éoqueveremosaseguir.
DocumentReplace
Conseguimossincronizaramodificaçãorealizadaemnossoobjetocom
odocumentonobanco.Essaestratégiadesobreporodocumentodobanco
comumnovodocumentoéchamadade documentreplace.
148

## Página 161

CasadoCódigo Capítulo6. MongoDB:bancodedadosbaseadoemdocumento
WriteConcern:Fire and forget vs.S afeWrite
Sóapartirdaversão2.6oMongoDBcome çouautilizarparaescritas
opadrão safewrites,quenotificaaaplicaçãoemcasodefalhas.Versões
anterioresutilizamopadrão fire and forget. Estetipodeescrita
nãoaguardaumarespostadobanco,oquepermitequeumgrandevol-
umedeatualizaçõespossamserenviadassemquesuaaplicaç ãofique
bloqueadaaguardandoumaresposta.Porém,sealgumerroocorrerna
conexãoentresuaaplicaçãoeseubanco,aaplicaçãonãoseránotificada.
Dependendodocontexto,essecenáriodeincertezapodeserinadmis-
sível.
6.17 Realizando upserts
Muitasvezesqueremosrealizarumaatualização,mascasoodocumentonão
exista,queremosqueelesejaincluído.Podemossolicitaressecomportamento
passandoovalor truecomooterceiroargumentodafun ção update:
> var contato4 = { "nome" : "Contato 4 mongo",
"email" : "cont4@empresa.com.br" }
> db.contatos.update({ "nome" : /4/ }, contato4, true);
WriteResult({
"nMatched" : 0,
"nUpserted" : 1,
"nModified" : 0,
"_id" : ObjectId("53e8e3eaf988309060c64744")
})
Paratermoscertezadequenossoupdatefuncionou,listaremosmaisuma
veznossoscontatos:
> db.contatos.find()
{
"_id" : ObjectId("530b8260b61fac75624ccfd2"),
"nome" : "Contato 2 Mongo",
"email" : "cont2@empresa.com.br"
149

## Página 162

6.17. Realizandoupserts CasadoCódigo
}
{
"_id" : ObjectId("530b85aab61fac75624ccfd7"),
"nome" : "Nome Alterado",
"email" : "cont3@empresa.com.br"
}
{ "_id" : ObjectId("53e8e3eaf988309060c64744"),
"nome" : "Contato 4 mongo",
"email" : "cont4@empresa.com.br"
}
Nosso upsertfuncionou,excelente!
Umproblemanãoesperado
Imagineocenárionoqualqueremosmodificarapenasoe-maildeum
contato.Quetalaplicarum document replace?Éissoquefaremos!
> db.contatos.update({ "nome" : /2/ },
{ "email" : "somudei@email.com" })
WriteResult({ "nMatched" : 1, "nUpserted" : 0,
"nModified" : 1 })
Pronto!OshelldoMongoDBnosinformaqueumdocumentofoimodi-
ficado,excelente!Verificandoaalteração:
> db.contatos.find()
{
"_id" : ObjectId("530b8260b61fac75624ccfd2"),
"email" : "somudei@email.com"
}
Espereumminuto! Nãoerabemesteoresultadodesejado. Repareque
odocumentointeirofoisubstituídoporumdocumentoqueagoracontém
apenasachave email,apesardeo ObjectIdaindaseromesmo.Perdemos
informações!
150

## Página 163

CasadoCódigo Capítulo6. MongoDB:bancodedadosbaseadoemdocumento
6.18 $set: modificador de atualização
Podemosatualizardocumentosatravésde modifiers,modificadores.Suasin-
taxeéumpoucomaisverbosa,porémelapermitequesejamosprecisosna
atualizaçãododocumento:
> db.contatos.update(
{ "email" : "cont4@empresa.com.br"},
{
"$set" :
{
"nome" : "Mais uma alteração"
}
}
)
WriteResult({ "nMatched" : 1, "nUpserted" : 0 })
Vejamosasintaxeanterior.Nela,afun ção updaterecebecomoprimeiro
parâmetronossocritério,oquenãoénovidadeparanós.Aprendemostam-
bémqueosegundoparâmetroéumJSONquecontémaschavescomosval-
oresquedesejamosmodificarnosdocumentosqueatenderemnossocritério.
Porém,oobjetopassadocomosegundoparâmetronãorecebedireta-
menteachavequedesejamosmodificar. Elaédefinidacomovalordeuma
chaveespecialchamada $set.
Achave $setéummodificadorpermitindoquesejamospontuaisna
alteraçãodeumdocumento. Nolugardesobreporodocumento,comona
estratégia document replace,eleapenasalteraaschavesdefinidascomo
valorde $set.
Comosempre,verificaremosserealmenteamodificaç ãofoipontuallis-
tandotodososnossoscontatos:
> db.contatos.find()
{
"_id" : ObjectId("530b8260b61fac75624ccfd2"),
"email" : "cont2@empresa.com.br"
}
{
"_id" : ObjectId("530b85aab61fac75624ccfd7"),
151

## Página 164

6.19. Documentosembutidos(EmbeddedDocuments) CasadoCódigo
"nome" : "Nome Alterado",
"email" : "cont3@empresa.com.br"
}
{ "_id" : ObjectId("53e8e3eaf988309060c64744"),
"nome" : "Mais uma alteração",
"email" : "cont4@empresa.com.br"
}
Temosoresultadoesperado.
Onde esta a transação?
OMongoDBnãosuportatransação,apenasoperaçõesatômicas.Es-
tasoperaçõesconsistemnaatualizaçãododocumentoeoutrosdoc-
umentos embutidos. Caso algum erro aconteça, nada será modifi-
cado no documento. Caso você precise de uma transação que en-
volvaváriosdocumentos,aequipedoMongoDBcriouumpatternpara
“two phase commits”disponívelemhttp://docs.mongodb.org/manual/
tutorial/perform-two-phase-commits.
6.19 Documentos embutidos (Embedded Docu-
ments)
Imagineagoraquecadacontatopossuaumcontatodeemergência.Primeiro,
buscamosocontatoeemseguidasuaemergênciaparanofinalrealizarmosa
associação:
> var contato = db.contatos.findOne({ "email" : /cont2/ })
> var emergencia = db.contatos.findOne({ "email" : /cont3/})
> contato.emergencia = emergencia;
> db.contatos.update({ "_id": contato._id}, contato);
WriteResult({ "nMatched" : 1, "nUpserted" : 0,
"nModified" : 1 })
Oprimeiropontoadestacaréquenenhumerroaconteceu.ComooMon-
goDBnãofor çaumesquema,fomoscapazesdeincluirumanovainformaç ão
152

## Página 165

CasadoCódigo Capítulo6. MongoDB:bancodedadosbaseadoemdocumento
aodocumento. Osdocumentosjáexistentesna collection contatos
nãoterãoessainformação.
Osegundoponto,destavezemformadepergunta,éoseguinte:como
seráqueoMongoDBgravouainformação?Parasabermos,vamosbuscaro
contatoqueacabamosdemodificar:
> db.contatos.findOne({ "email" : /cont2/ })
{
"_id" : ObjectId("530b8260b61fac75624ccfd2"),
"email" : "cont2@empresa.com.br",
"emergencia" : {
"_id" : ObjectId("530b85aab61fac75624ccfd7"),
"nome" : "Nome Alterado",
"email" : "cont3@empresa.com.br"
}
}
Nossa busca retornou nosso documento, inclusive o seu contato de
emergência! EssetestedemonstraqueoMongoDBpermitearmazenarem
chavesoutrodocumentoquechamamosde documentosembutidos(embed-
ded documents).
Umavantagemdestaestratégiaéquebuscamosapenasumdocumento
semanecessidadederealizarmos JOINS,comonosbancosdedadosrela-
cionais.Umaconsequênciapositivadissoéarapideznasconsultas.
Hácenáriosondetrabalharcom Embedded Documents éextrema-
menteviável,porexemplo,umanotafiscalquejávemcomtodososseus
itens. Porém,noexemploanterior,podemosterinconsistênciaemnossos
dados.Vejamosumexemplo:
> var emergencia = db.contatos.findOne({ "email" : /cont3/})
> emergencia.nome = "Mais uma vez Alterado"
> db.contatos.update({"_id", emergencia._id}, emergencia)
> db.contatos.findOne({ "email" : /cont2/ })
{
"_id" : ObjectId("530b8260b61fac75624ccfd2"),
"email" : "cont2@empresa.com.br",
"emergencia" : {
"_id" : ObjectId("530b85aab61fac75624ccfd7"),
153

## Página 166

6.20. SimulandoJOINSnoladodaaplicação CasadoCódigo
"nome" : "Nome Alterado",
"email" : "cont3@empresa.com.br"
}
}
Repare que alteramos diretamente nacollection o contato de
emergência.Porém,essamodificaçãonãorefleteno embedded document:
temos um dado inconsistente. Mas será que o uso deembedded
documentssempregeraráinconsistência?Comcerteza,não.
Oexemplodanotafiscaleseusitensébastanteesclarecedor.Nele,bus-
camosanotafiscalcomtodosseusitens.Nestarelaç ãodecomposiçãonaqual
umitemnãoexistesemumanota,teremosacertezadequequalqueralter-
açãonoitemafetaráapenasanotadaqualelefazparte.Nestecaso,acriaç ão
da collection item éopcional.NomundoSQL,estemesmorelaciona-
mentoenvolveriaastabelas notae itemassociadasatravésdeum JOIN,o
queemteoriapodesermaislento.
Sendoassim,aperguntaquedevemosfazeré:terumcontatodeemergên-
ciacomoum embedded document podenoscausaralgumproblema?Sim,
poisnestarelaçãodeagregaçãonãoqueremoscorreroriscodenosbasear-
mosemdadosinconsistentes(e-maildesatualizadoetc.)nahoraemqueuma
fatalidadeacontecer.
Dentrodoqueacabamosdever,podeserqueparadeterminadotipode
aplicaçãooMongoDBnãosejaindicadoeparaoutroselesejaaltamentere-
comendado.Porém,emnossaaplicaçãopodemossimular JOINSdomundo
SQLnoladodaaplicação,oqueresolveriaoproblemadaconsistênciados
dadosentreumcontatoesuaemergência.
6.20 S imulando JOINS no lado da aplicação
OMongoDBnãonosofereceumamaneiranativadecriarmosrelacionamen-
tosdotipopresentenomundoSQL.Sequisermosrealizaralgoparecido,a
responsabilidadepelacriaçãoeresoluçãodessesrelacionamentosserádere-
sponsabilidadedodesenvolvedor.
Amaneiramaissimplesdefazermosissoé,nolugardeusarmosum
embedded document,gravarmosapenasseu ObjectId.
154

## Página 167

CasadoCódigo Capítulo6. MongoDB:bancodedadosbaseadoemdocumento
> var contato = db.contatos.findOne({ "email" : /cont2/ })
> var emergencia = db.contatos.findOne({ "email" : /cont3/})
> contato.emergencia = emergencia._id
> db.contatos.update({ "_id" : contato._id}, contato);
WriteResult({ "nMatched" : 1, "nUpserted" : 0,
"nModified" : 1 })
o prefixo_
Nãoéraroencontrarprogramadoresqueprefixamachavequeguarda
o ObjectIdcom _.Issoforneceumapistavisualindicandoqueachave
nãoguardaumvalorqualquer,masum ObjectId.
Vamosbuscarocontatonovamentedobancoparaverificarmosamu-
dança:
> contato = db.contatos.findOne( "_id", contato._id)
{
"_id" : ObjectId("530b8260b61fac75624ccfd2"),
"email" : "cont2@empresa.com.br",
"emergencia" : ObjectId("530b85aab61fac75624ccfd7")
}
Agora,precisamosexecutarumanovaconsultaparaobterocontatode
emergência:
> var emergencia =
db.contatos.findOne({ "_id" : contato.emergencia});
> emergencia
"_id" : ObjectId("530b85aab61fac75624ccfd7"),
"nome" : "Mais uma vez Alterado",
"email" : "cont3@empresa.com.br"
A solução anterior funciona porque sabemos que oObjectId ar-
mazenadonachave contato.emergenciafazparteda collection
contatos,porémumprogramadorqueacaboudeentraremnossaequipe
saberiacomclarezadessarelação?Émuitoprovávelqueeleprocurasseesse
155

## Página 168

6.21. DBRefs:databasereferences CasadoCódigo
ObjectIdemuma collectionchamada emergencias,quesequerex-
isteemnossobanco. Seráqueháalgumaformadefornecermosumauma
pistaparaodesenvolvedordequal collectionaquele ObjectIdfaz
parte?Éissoqueveremosaseguir.
6.21 DBRefs: database references
OMongoDBpossuiumrecursochamado DBRefs(database references)que
nosajudaasaberdequal collectionnossosIDspertencem.Antesdemais
nada,voltaremosparaorelacionamentoquevimosnase çãoanterior:
> var contato = db.contatos.findOne({ "email" : /cont2/ })
> contato
{
"_id" : ObjectId("530b8260b61fac75624ccfd2"),
"email" : "cont2@empresa.com.br",
"emergencia" : ObjectId("530b85aab61fac75624ccfd7")
}
> var emergencia =
db.contatos.findOne({ "_id" : contato.emergencia});
Naconsultaanterior,temoso ObjectIddeumcontatodefinidodire-
tamentenachave contato.emergencia,porémagoraeleseráovalorda
chave $iddeumobjeto DBRefs:
> contato.emergencia = {
"$ref" : "contatos",
"$id" : emergencia._id
}
Repareque,alémde $id,adicionamostambémapropriedade $refque
serveparaindicara collectionàqualnosso ObjectIdpertence.
$db
É possível adicionar a chave$db para indicar de qual banco a
collectiondefinidanachave $reffazparte,porémessainformação
nãoésuportadaportodososdrivers.
156

## Página 169

CasadoCódigo Capítulo6. MongoDB:bancodedadosbaseadoemdocumento
Agoraatualizaremosnossocontatonobancoatravésdeum document
replace:
> db.contatos.update({"_id" : contato._id}, contato);
WriteResult({ "nMatched" : 1, "nUpserted" : 0,
"nModified" : 1 })
Logoemseguida,buscaremosocontatodobanconovamenteguardando
oresultadonamesmavariável:
> contato = db.contatos.findOne({"_id" : contato._id});
> contato
{
"_id" : ObjectId("530b8260b61fac75624ccfd2"),
"email" : "cont2@empresa.com.br",
"emergencia" : DBRef("contatos",
ObjectId("530b85aab61fac75624ccfd7"))
}
>
Reparenoconsolequeotipodachave emergenciaéum DBRef.Que
talimprimirmosnoconsoleaemergênciadocontato?
> contato.emergencia
DBRef("contatos", ObjectId("530b85aab61fac75624ccfd7"))
Ondeestánossocontato?Reparequeomongoshellnãobuscaautomati-
camenteparanósnossocontato.Aresponsabilidadederesolverorelaciona-
mentocontinuasobresponsabilidadedaaplicaç ão,contudoalgunsdrivers
utilizamainformaçãodo DBRefpararesolverorelacionamento.
ResolvendorelacionamentosDBref
Podemossolucionaresteproblemanomongoshellcriadoumafun ção
especializada para resolver relacionamentos. Chamaremos a função de
refResolver:
> function refResolver(ref) {
return db[ref.$ref].findOne({"_id": ref.$id})
}
157

## Página 170

6.21. DBRefs:databasereferences CasadoCódigo
> var emergencia = refResolver(contato.emergencia);
> emergencia
{
"_id" : ObjectId( "530b85aab61fac75624ccfd7"),
"nome" : "Nome Alterado",
"email" : "cont3@empresa.com.br"
}
Pormaisquenossasoluçãofuncione,paracadaassociaçãodenossodoc-
umentoseránecessáriorealizarumaconsultaemseparadaparaobtercada
embedded document associado. Essecomportamentonãoétãoperfor-
máticoquantoos JOINSSQLquepermitemque,emumaúnicaconsulta,
resolvamostodososrelacionamentos.Esseproblemasetornamaiseminente
quandotemosumarraycomvários ObjectIdscomochavedeumdocu-
mento,poisgeraremosNconsultasparacadaumdelesalémdaconsultado
documentoprincipal.
AspossibilidadesdeconsultasnoMongoDBvãomuitoalémdoquevi-
mos. Casooleitorqueriaseaprofundar,oprópriositedoMongoDBdoc-
umentatodasaspossibilidadespossíveis(http://docs.mongodb.org/manual/
tutorial/query-documents/).
MongoDBeseuuniverso
Aprendemosnestecapítulocomocriarbancosdentrodeumainstância
doMongoDBeaorganizardocumentosatravésde collections. Tam-
bémaprendemosarealizarconsultasecomoremoverealterardocumentos
existentes.
Épossívelrealizarconsultasmaiscomplexas,inclusiveconfiguraroMon-
goDBparatrabalharemum clustereporaívai.Porém,oquevimosésufi-
cienteparacontinuarmoscomaimplementaçãodonossoprojetoContatooh.
Atualmentenossoback-endcomExpresstrabalhaapenascomdados
voláteisemmemóriasemsepreocuparempersisti-los.Todavezquereinici-
amososervidor,perdemostodasasinformaçõescadastradas.
Nossapróximatarefaseráintegrarnossoback-endcomoMongoDB,
garantindoapersistênciadosdadosdaaplicação.
158

## Página 171

Capítulo7
IntegrandoExpresseMongoDB
“ A coisa mais indispensável a um homem é reconhecer o uso que deve fazer do
seu próprio conhecimento. ”
–Platão
Nocapítuloanterior,aprendemosconceitosfundamentaisdoMongoDB,
inclusiveinteragimoscomseuclienteemlinhadecomando,omongoshell.
Exercitamosumasériedeoperaçõesparainclusão,alteração,remo çãoecon-
sultadedocumentos,porémaindafaltaintegrarnossoback-endcomoMon-
goDB.
7.1 Mongo Driver
É preciso que nossa aplicação seja capaz de se conectar e realizar op-
erações em nosso banco e normalmente isso é feito através de um

## Página 172

7.1. MongoDriver CasadoCódigo
driver.OMongoDBpossuiumdrivernativo(https://github.com/mongodb/
node-mongodb-native)criadoespecialmenteparaoNode.js.Suainstalaç ão
éfeitaatravésdo npmcomoqualqueroutromódulodoNode.js:
npm install mongodb@1.4 --save
Dentrodapasta contatooh,vamoscriaroarquivo consulta.jse
realizarumtestequebuscaumcontatopeloseuObjectIdcomoseguinte
código:
// contatooh/consulta.js
var MongoClient = require('mongodb').MongoClient;
var ObjectID = require('mongodb').ObjectID;
// ObjectID de algum contato existente
var _idProcurado = new ObjectID('53ee689e89bd201218944bba');
MongoClient.connect('mongodb://127.0.0.1:27017/contatooh',
function(erro, db) {
if(erro) throw err;
db.collection('contatos').findOne({_id : _idProcurado},
function(erro, contato) {
if(erro) throw err;
console.log(contato);
}
);
}
);
Agora,peloterminal,vamosexecutarnossocódigoatravésdoNode.js:
node consulta
CasovocêtenhafornecidoumIDválido,ocontatoseráimpressonoter-
minal,casocontrário,seráexibido null.Antesdeentrarmosnosdetalhes
dodriver,vamosrefletirsobreopapeldosesquemas.
160

## Página 173

CasadoCódigo Capítulo7. IntegrandoExpresseMongoDB
7.2 Esquema faz falta?
Imagineumaaplicaçãowebnaqualousuárioinformaseunomenolocal
destinadoàsuadatadenascimento.Sabemosqueessainformaç ãoseráper-
sistidae,comooMongoDBnãofor çaumesquema,eleaceitaráodocumento
comestainformaçãoinválida. Talvezseuchefeacheengraçadoveremum
relatórioonomedousuárionolugardesuadatadenascimento,outalvezele
nãosejatãobem-humoradoassim.
Esquemasim,masnaaplicaç ão
ApesardeoMongoDBnãofor çaresquemas,issonãoquerdizerquees-
quemasnãosejamimportantes,inclusiveaintegridadedosdadosnestebanco
NoSQLéderesponsabilidadedaaplicação,portanto,responsabilidadedode-
senvolvedor.
Mongodriverésuficiente?
Poderíamosrefatoraragoranossoback-endeutilizarodrivernativodo
mongo,mas,sendoumdriverdebaixonível,elenãotraznenhumaç úcarsin-
tático.Vocêdeveterreparadonoscallbacksaninhados,quepodemresultar
nocallbackHELL,dependendodacomplexidadedasuaconsulta.
Tambémsomososresponsáveispelatraduçãodestringspara ObjectId,
caso contrário, a função findONenão funcionará. Outra questão que
acabamosdeveréaimportânciadeimplementarmosesquemaspelaapli-
cação.
FoiporissoqueaprópriaequipedoMongoDBcriouumaabstraç ãosobre
odrivernativodoMongoDBquefacilitaenormementeacriaç ãodeesque-
maspelaaplicação,removendomuitoruídosintáticododrivernativo.Essa
abstraçãorecebeuonomede Mongoose.
7.3 Mongoose Object-Document Modeler
MongooseéumabibliotecadeODM(Object-Document Modeler )criadapela
equipedoMongoDB.ElaéumacamadaentornododriverdoMongoDBque
gerenciarelacionamentoseexecutavalidações,entreoutrasfuncionalidades.
161

## Página 174

7.3. MongooseObject-DocumentModeler CasadoCódigo
Mongoosefuncionadaseguintemaneira:noladodaaplicaç ão,criamos
esquemasqueservemcomomoldeparacriaç ãodosmodelosdaaplicaç ão.
Criamosobjetosapartirdesses modeloscomauxíliodoMongooseetoda
alteraçãorealizadanessesobjetosépersistidanobancoatravésdemétodos
específicospresentesnainstânciadomodelooudiretamentenoprópriomod-
elo.
Lembra de $resource?
Noladodocliente, usamos $resourceparaacessar REST end-
points.Vocêdevelembrarqueutilizamosorecursocomoumaespéciede
modelo,masquecarregavacódigodeinfraestrutura,algoquestionável.
Porém,issotornouconvenienteachamadadasfun çõesresponsáveispela
sincronizaçãodosdadosdomodelocomnossoserviço.Aideiaagoraé
fazeralgoparecidocomMongoose,masdestavezligandonossoserviço
comnossobanco.Podemosfazerumaanalogiacomopadrão ActiveRe-
cord(http://www.martinfowler.com/eaaCatalog/activeRecord.html)uti-
lizadopelacomunidadeRubyonRails.
Instalação
InstalaremosoMongooseatravésdo npm:
npm install mongoose@3.8 --save
O Mongoosejá tem como dependência o driver do MongoDB,
porémmanteremosodriverquebaixamosnoiníciodestase ção.Eleserá
utilizadonase ção12.6.
Nossopróximopassoseráprepararaconexãocomobancoatravésdo
Mongoose.
162

## Página 175

CasadoCódigo Capítulo7. IntegrandoExpresseMongoDB
7.4 Gerenciando a conexão
Nossaprimeiratarefaseráisolarocódigodeinicializaç ãodaconexãoem
seupróprioarquivo. Criaremosomódulo database.jsdentrodapasta
config, que terá como dependência o Mongoose. Ele receberá como
parâmetroaURLdobancodenossaaplicaç ãoquepassaremosparaoMon-
goose,esteúltimoresponsávelpelaaberturaegerenciamentodaconexão:
// config/database.js
var mongoose = require('mongoose');
module.exports = function(uri) {
mongoose.connect(uri);
}
Mesmosemtermosterminadonossomódulovocêdeveestarsepergun-
tandoquemochamará. Aideiaéquenossaconexãosejainiciadacomo
servidor.Éporissoquechamaremosnossomódulo database.jsatravés
denosso server.js:
// app/server.js
var http = require('http');
var app = require('./config/express')();
require('./config/database.js')('mongodb://localhost/contatooh');
http.createServer(app).listen(app.get('port'), function(){
console.log('Express Server escutando na porta ' +
app.get('port'));
});
Poderíamos até subir nossa aplicação, porém não teríamos nenhuma
informaçãosobreoestadodaconexão. Podemosresolveresteproblema
atravésdoseventos connected, disconnectede errordisparadospela
conexão. Bastapassarmosumcallbackparacadaumdelescomasinfor-
maçõesquequeremosexibirnoconsole:
// config/database.js
163

## Página 176

7.4. Gerenciandoaconexão CasadoCódigo
var mongoose = require('mongoose');
module.exports = function(uri) {
mongoose.connect(uri);
mongoose.connection.on('connected', function() {
console.log('Mongoose! Conectado em ' + uri);
});
mongoose.connection.on('disconnected', function() {
console.log('Mongoose! Desconectado de ' + uri);
});
mongoose.connection.on('error', function(erro) {
console.log('Mongoose! Erro na conexão: ' + erro);
});
}
164

## Página 177

CasadoCódigo Capítulo7. IntegrandoExpresseMongoDB
connect vs. createConnection
Afunção connectcriaumaconexãopadrãoacessívelpelos models
criadospeloMongoose,assuntoqueveremosmaisàfrente.Paranossa
aplicação,issoserásuficiente,porémháaplicaçõesqueacessammaisde
umbanco.Paraisso,existeafun ção createConnection,queretorna
aconexãocomobanco:
var connection = mongoose.createConnection(uri);
Entretanto,quandocriamosconexõesdessaforma,somososrespon-
sáveisemassociá-lasaosmodeloscriadospeloMongoose.Outroponto
équevocêteráquegarantirqueninguémcriaráduasconexõesparao
mesmobanco:
var mongoose = require('mongoose');
var connection;
module.exports = function(uri) {
if(!connection) {
connection = mongoose.createConnection(uri);
}
return connection;
}
Nesseexemplo,aconexãoserácriadaapenasnaprimeirachamada.
Qualquerchamadaposteriorretornaráaconexãojácriada.
Precisamos garantir que a conexão seja fechada quando nossa apli-
caçãoforterminada. Vamosinteragircomoobjeto processglobalmente
disponívelpeloNode.jseacessívelemqualquerlocaldenossaaplicaç ão.
Oobjeto processpossuioevento SIGINITdisparadoquandonossa
aplicaçãoéterminada(porexemplo: CONTROL + C noterminal).Éatravés
docallbackassociadoaesteeventoquepediremosaoMongoosequefeche
nossaconexãoatravésdafun ção close:
// config/database.js
165

## Página 178

7.4. Gerenciandoaconexão CasadoCódigo
var mongoose = require('mongoose');
module.exports = function(uri) {
mongoose.connect(uri);
// código anterior omitido
process.on('SIGINT', function() {
mongoose.connection.close(function() {
console.log('Mongoose! Desconectado pelo término da
aplicação');
// 0 indica que a finalização ocorreu sem erros
process.exit(0);
});
});
}
Subindonossoservidormaisumavez:
$ node server
Express Server escutando na porta 3000
Mongoose! Conectado em mongodb://localhost/contatooh
Reparenoconsolequeocallbackassociadoaoevento connectedfoi
chamadoenossamensagemexibida. Podemostestarseocallbackparao
evento disconnectedtambémseráchamadofinalizandonossaaplicação
atravésde CONTROL + C:
$ node server
Mongoose! Conectado em mongodb://localhost/contatooh
Mongoose! Desconectado
Mongoose! Mongoose! Desconectado pelo término da aplicação
166

## Página 179

CasadoCódigo Capítulo7. IntegrandoExpresseMongoDB
Pool de conexões
Afunção mongoose.connectcriaporpadrãoumpoolcomcinco
conexões,porémestaquantidadepodenãoseradequadaparatodasas
aplicações.Podemosalterarestaquantidadepassandoumaconfiguração
extraparaafun ção:
mongoose.connect(uri, { server: { poolSize: 15 }});
Excelente! JáconseguimosnosconectaraoMongoDBatravésdoMon-
goose. Agoraprecisamosaprendercomocriaresquemasecomoutilizá-los
paraconstruirmosmodelosqueserãoutilizadospelanossaaplicaç ão.
7.5 Criando esquemas
VimosqueoMongoDBéumbancosemesquemas,nãoexigindodeseus
documentosdeterminadaestrutura. Contudo, issonãotornaoesquema
menosimportante. ÉporissoqueoMongoosepossuioobjeto Schema,
quedefineaestruturadequalquerdocumentoqueseráarmazenadoemuma
collectiondoMongoDB.Elepermitedefinirtiposevalidardados.
Nosso primeiro passo será criar o módulocontato.js na pasta
app/models. Nele, declararemosumobjeto Schemaatravésdafun ção
mongoose.Schemaquerecebecomoparâmetroumasériedecritérios.Por
enquanto,passaremosumobjetovaziocomocritério:
// app/models/contato.js
var mongoose = require('mongoose');
module.exports = function() {
var schema = mongoose.Schema({});
};
167

## Página 180

7.5. Criandoesquemas CasadoCódigo
Nosso primeiro critério será garantir que as chavesnomee email
aceitemapenas strings:
// app/models/contato.js
var mongoose = require('mongoose');
module.exports = function() {
var schema = mongoose.Schema({
nome: {
type: String
},
email: {
type: String
}
});
};
Repare que adicionamos no objeto passado como parâmetro para a
função mongoose.Schemaaschavesquecorrespondemàsquequeremos
emnossodocumento,porémcadaumadelaspossuicomovalorum objeto
deconfiguração.
Noobjetodeconfiguração,indicamoso Schema Type aceitoporcada
chavedenossodocumentoatravésdachave type. Tantoo nomequanto
o emaildevemaceitarapenastexto,porissoatribuímosa typeovalor
String.Existemoutrostiposcomo Number, Date, Booleane Array,
masporenquantootipo Stringjáésuficiente.
168

## Página 181

CasadoCódigo Capítulo7. IntegrandoExpresseMongoDB
Esquema e arrays
QualquertipodeesquemadoMongoosepodeserconsideradoum
array,bastaenvolvê-loentrecolchetes:
mongoose.Schema({
emails: {
type: [String]
}
});
Dessa forma, garantiremos que apenas arrays contendo o tipo
Stringserãopermitidosemnossodocumento.
Queremostambémqueo nomeeo emailsejamobrigatórios. Issoé
feitoadicionandoachave requirednoobjetodeconfiguração:
// app/models/contato.js
var mongoose = require('mongoose');
module.exports = function() {
var schema = mongoose.Schema({
nome: {
type: String,
required: true
},
email: {
type: String,
required: true
}
});
};
Porfim,nãopodehavercontatoscomomesmoe-mail.Garantimosisso
adicionandomaisumachavedeconfiguração,destaveza index:
169

## Página 182

7.5. Criandoesquemas CasadoCódigo
// app/models/contato.js
var mongoose = require('mongoose');
module.exports = function() {
var schema = mongoose.Schema({
nome: {
type: String,
required: true
},
email: {
type: String,
required: true,
index: {
unique: true
}
}
});
};
Essasregrasjásãosuficientesparanossoesquema.Porém,paraquepos-
samosinteragircomobanco,nãotrabalharemoscomoesquema,mascom
ummodelocriadoapartirdele.
Model
Um Modeléumobjetoquecorrespondeauma collectiondenosso
bancoeutilizao Schemausadoemsuacriaçãoparavalidarqualquerdocu-
mentoquetenhamosna collection.
Éporissoqueaúltimalinhadonossomóduloretornaráum Modelcri-
adoapartirdonosso Schema:
// app/models/contato.js
var mongoose = require('mongoose');
module.exports = function() {
170

## Página 183

CasadoCódigo Capítulo7. IntegrandoExpresseMongoDB
// código omitido
return mongoose.model('Contato', schema);
};
Pronto!Aquestãoagoraésabercomodisponibilizaremoso Modelcri-
adopelonossomóduloparaorestantedaaplicaç ão.
express-loadnovamente
Na seção 2.9, utilizamos oexpress-load para disponibilizar to-
dos os controllers da pastaapp/controllers diretamente na instân-
cia do Express, permitindo que nossas rotas (também carregadas pelo
express-load)tivessemacessoaoscontrollerssemanecessidadedafun ção
require. Seabrirmosoarquivo config/express.js,veremosquejá
havíamosincluídoapasta models:
// config/express.js
// código omitido
load('models', {cwd: 'app'})
.then('controllers')
.then('routes')
.into(app);
// código omitido
Comoapasta modelsfoicarregadaantesda controllers,podemos
acessaromodelexportadodiretamentenocontrollerseguindoaconven ção
quejáaprendemos.Emnossocaso,opadrãodeacessoaomodelcarregado
pelo express-loadseráapp.models.contato.
Podemosrealizarumtesteparaversetudoestáfuncionando.Primeiro,
apagaremosobanco contatoohatravésdomongoshell:
$ mongo
MongoDB shell version: 2.6.6
connecting to: test
171

## Página 184

7.5. Criandoesquemas CasadoCódigo
> use contatooh
switched to db contatooh
> db.dropDatabase()
{ "dropped" : "contatooh", "ok" : 1 }
Agorasubiremosnossaaplicação:
$ node server
Express Server escutando na porta 3000
Mongoose! Conectado em mongodb://localhost/contatooh
Notequeestamosconectadosaobanco contatoohqueacabamosde
apagar!OMongooseextraiuonomedobancodaURLdeconexãocriando-o
paranós,inclusivecrioua collection contatos,adotandocomopadrão
onomepassadocomoprimeiroparâmetroparaafun ção mongoose.model,
porémemlowercaseenoplural.Paraficaraindamaisinteressante,oíndicede
unicidadeparaachave emailtambémfoicriado.Vejamostudoissoatravés
domongoshell:
$ mongo
MongoDB shell version: 2.6.6
connecting to: test
> show dbs
admin (empty)
contatooh 0.078GB
local 0.078GB
test 0.203GB
> use contatooh
switched to db contatooh
> show collections
contatos
system.indexes
> db.contatos.getIndexes()
// exibe detalhes do índice criado
172

## Página 185

CasadoCódigo Capítulo7. IntegrandoExpresseMongoDB
mongoose.debug
Vocêpodevisualizarnoterminaltodososcomandosexecutadospelo
Mongoosehabilitandoseu debbuger:
// config/database.js
mongoose.set('debug',true);
7.6 Utilizando modelos
Aprendemosnase çãoanterioracriarum Modelapartirdeum Schema.
Disponbilizamoso Modelparanossocontrolleratravésdo express-load
utilizando a convenção de acessoapp.models.contato. Agora, pre-
cisamosreescreverocódigodenossocontroller.
Vamoseditar app/controllers/contato.jsremovendoaimple-
mentaçãodetodasasfun çõesdocontrollereapagandoalistafixadecontatos
eavariáveldeautoincrementoquecriamos.Nofinal,nossocontrollerdeve
ficarassim:
// app/controllers/contato.js
module.exports = function (app) {
var controller = {};
controller.listaTodos = function(req, res) {};
controller.obtemContato = function(req, res) {};
controller.removeContato = function(req, res) {};
controller.salvaContato = function(req, res) {};
return controller;
};
173

## Página 186

7.7. Buscandodocumentos CasadoCódigo
Emseguida,vamosguardarumareferênciaao Modeldisponívelnain-
stânciadoExpresspassadacomoparâmetroparaomódulo:
module.exports = function (app) {
var Contato = app.models.contato;
// código omitido
};
Guardamosumareferênciaparao ModelnavariávelContatoiniciando
comletramaiúscula,umaconven çãobastanteutilizadaparafun çõesconstru-
toras.Essasfun çõespermitemutilizarooperador newparacriarmosnovas
instâncias,objetosquerepresentamnossosdocumentos.
7.7 Buscando documentos
Vamosiniciarpelafun ção controller.listaTodos. Nãotemosinter-
esseeminstanciarumcontato,apenaslistartodososcadastradosemnosso
banco. Paraisso,aprópriafun çãoconstrutora Contatopossuiafun ção
find.Comoqueremostodososcontatos,elanãoreceberáumcritériocomo
parâmetro.
Existemdiferentesmaneirasderealizarmosessaconsulta,porémafun ção
findpoderetornaruma promiseatravésdachamadaencadeadaàfun ção
exec:
module.exports = function (app) {
var Contato = app.models.contato;
var controller = {}
controller.listaTodos = function(req, res) {
var promise = Contato.find().exec();
};
// código omitido
174

## Página 187

CasadoCódigo Capítulo7. IntegrandoExpresseMongoDB
return controller;
};
Aprendemosnase ção5.3quetoda promisepossuiafun ção then. Isso
nãoédiferentecoma promisedoMongoose,maselanãopossuiafun ção
catch.Vamospassaroscallbacksdesucessoedefalhaparaafun ção then
eomitiremosadeclaraçãodavariável promise:
controller.listaTodos = function(req, res) {
Contato.find().exec()
.then(
function(contatos) {
res.json(contatos);
},
function(erro) {
console.error(erro)
res.status( 500).json(erro);
}
);
};
Recebemosnocallbackdesucessoalistadecontatosretornadaelogo
emseguidaaenviamosatravésdafun ção res.json.Jánocallbackdeerro,
logamosainformaçãoe,antesdeenviá-laparaocliente,modificamosostatus
darespostapara500(internal server error ).
175

## Página 188

7.8. BuscandopeloID CasadoCódigo
A função exec
Estamoschamandoafun ção execpararecebermosuma promise.
Porém,entreachamadadafun ção finde exec,podemoschamarout-
rasfun çõesdoMongoose. Porexemplo,sequisermosobterapenaso
nomeeo emaildeumcontato,usamosafun ção select:
Contato.find()
.select("nome email")
.exec();
Sequisermosagorafiltrarporpartedeume-mail,encadeamosuma
chamadaàfun ção whereseguidadeumadasmuitasfun çõesdecom-
paração. Emnossocaso,utilizaremosafun ção equals,querecebe
comoparâmetroumaexpressãoregular:
Contato.find()
.select("nome email")
.where("email").equals(/cont/)
.exec()
.then(function(nomeEhEmail) {
console.log(nomeEhEmail);
});
Apesardetermosapenasalistagemimplementadaemnossocontroller,já
podemostestareverificarsenossoscontatossãoexibidosnapáginaprincipal.
7.8 Buscando peloID
Nossopróximopassoseráimplementarabuscadeumcontato,sóquedessa
vezutilizaremosafun ção Contato.findById:
controller.obtemContato = function(req, res) {
var _id = req.params.id;
Contato.findById(_id).exec()
.then(
176

## Página 189

CasadoCódigo Capítulo7. IntegrandoExpresseMongoDB
function(contato) {
if (!contato) throw new Error("Contato não encontrado");
res.json(contato)
},
function(erro) {
console.log(erro);
res.status( 404).json(erro)
}
);
};
CasooIDprocuradonãoexistanobanco,receberemos undefined
comoresposta.Nestecaso,lan çaremosumaexce çãoinformandoqueocon-
tatonãofoiencontrado.Comoestamosusandoopadrão promise,nossocall-
backdeerroseráinvocadorecebendoaexce çãoquelan çamos. Depoisde
logarmosoerro,enviamoscomorespostaostatus404,juntodoJSONcom
amensagemdeerro.Setudocorrerbem,enviamosocontatocomoresposta
atravésde res.json.
Podemosreiniciarnossaaplicaçãoeverificarsenossasele çãodecontatos
realmentefunciona.
7.9 Removendo documentos
Agora atacaremos a remoção de contatos. Utilizaremos a fun ção
Contato.removequerecebecomocritérioo ObjectIdprocurado. Se
aoperaçãoforrealizadacomsucesso,enviaremosostatuspadrão200como
resposta.
controller.removeContato = function(req, res) {
var _id = req.params.id;
Contato.remove({"_id" : _id}).exec()
.then(
function() {
res.end();
},
function(erro) {
return console.error(erro);
177

## Página 190

7.10. Atualizandodocumentos CasadoCódigo
}
);
};
findByIdAndR emove
Um Model criado pelo Mongoose possui a fun ção
findByIdAndRemove que remove e passa para o callback o con-
tato removido. Em nosso caso, não temos interesse no documento
removido;éporissoqueafun ção removefoiutilizada.
Experimentereiniciaroservidoreremoveralgunscontatos. Tudodeve
funcionarconformeoesperado.
7.10 Atualizando documentos
Sófaltaimplementarmosnossalógicadegravaç ão. CasooIDdocontato
tenhasidodefinido,utilizaremosafun ção Contato.findByIdAndUpdate
paraatualizá-lo.SeuprimeiroparâmetroéoIDdocontatoprocurado;ose-
gundo,osdadosdocontato:
controller.salvaContato = function(req, res) {
var _id = req.body._id;
if(_id) {
Contato.findByIdAndUpdate(_id, req.body).exec()
.then(
function(contato) {
res.json(contato);
},
function(erro) {
console.error(erro)
res.status(500).json(erro);
}
);
} else {
// falta ainda
178

## Página 191

CasadoCódigo Capítulo7. IntegrandoExpresseMongoDB
}
};
update
UmModeldoMongoosepossuiafun ção update,porémelaape-
nasatualizaodocumentosemretorná-loapósamodificaç ão.Afun ção
findByIdAndUpdate,alémdeatualizar,nosdáacessoaodocumento
atualizado.
Precisamos implementar o else que adicionará um novo contato.
Nestasituação,utilizaremosafun ção Contato.create,querecebecomo
parâmetroosdadosdocontatoenviadosnarequisição.Diferentedasfun ções
depesquisa,nãoprecisamoschamarafun ção exec,poisaprópria create
járetornauma promiseporpadrão:
controller.salvaContato = function(req, res) {
var _id = req.body._id;
if(_id) {
Contato.findByIdAndUpdate(_id, req.body).exec()
.then(
function(contato) {
res.json(contato);
},
function(erro) {
console.error(erro)
res.status( 500).json(erro);
}
);
} else {
Contato.create(req.body)
.then(
function(contato) {
res.status( 201).json(contato);
},
function(erro) {
console.log(erro);
179

## Página 192

7.11. FunçõesdepersistêncianoModelounodocumento? CasadoCódigo
res.status(500).json(erro);
}
);
}
};
Agorapodemosreiniciaroservidorincluindoealterandocontatosever-
ificarsetudofuncionaconformeoesperado.
7.11 Funções de persistência no Model ou no
documento?
OMongoosepermiteexecutaroperaçõesdepersistênciadeduasmaneiras.
Utilizamosaprimeiranase çãoanteriorquandochamamosasfun çõesdeper-
sistênciadiretamenteno Model Contato.Asegundachamafun çõesapar-
tirdeumainstânciadonosso Model,quetambéméumafunçãoconstrutora.
Vejamosumexemplodestasegundaformacorrespondenteàinclusãodeum
contato:
var contato = new Contato(req.body);
contato.save(function(erro, contato) {
if(erro) {
res.status(500).end();
console.log(erro)
} else {
res.json(contato);
}
});
Reparequeinstanciamosumnovodocumentoatravésdooperador new,
passando para nosso Model os dados do contato acessíveis através de
req.body.
Oproblemaéquefun çõesdepersistênciadainstânciadeum Model
nãoretornam promises.Reparequenoexemploanteriorsomosobrigadosa
recebernamesmafun çãodecallbackumareferênciaparaerroeoutraparao
contatosalvo.
180

## Página 193

CasadoCódigo Capítulo7. IntegrandoExpresseMongoDB
7.12 Criando referências
Nossapartedepersistênciaestápronta,porémaindafaltamaisumrequisito
donossosistema. Vocêdeveselembrarquenase ção6.19associamosuma
emergênciaparaumcontatoatravésdomongoshell.Chegouahoradeim-
plementarmosamesmaassociaçãoatravésdoMongoose!
Oprimeiropassoéabrirmosoarquivo app/models/contato.jse
adicionarmosainformaçãodeemergênciaemnossoesquema.Contudo,seu
tiposeráum Schema.ObjectId:
var mongoose = require('mongoose');
module.exports = function() {
var schema = mongoose.Schema({
nome: {
type: String,
required: true
},
email: {
type: String,
required: true,
index: {
unique: true
}
},
emergencia : {
type: mongoose.Schema.ObjectId,
ref: 'Contato'
}
});
return mongoose.model('Contato', schema);
};
Repareque,alémdo type,adicionamostambémachave ref,quepos-
suicomovalorum Model,emnossocaso,o Model Contato.Issofaztodo
osentido,jáquetemosumautorrelacionamento. Esseexemplodemonstra
quepodemosadotarcomo typequalquer Modelcriadopornósatravésdo
Mongoose.
181

## Página 194

7.13. Modificandonossaviewparaexibiremergências CasadoCódigo
Muitobem,alteramosnossoesquema,masondeanovainformaç ãoserá
exibida?Éoqueveremosnase çãoaseguir.
7.13 Modificando nossa view para exibir
emergências
Precisamosadicionarnaviewparcial public/partials/contato.html
umacaixadesele ção,permitindoqueescolhamosdeumalistaqualdoscon-
tatoscadastradosseráaemergência.Aquestãoéquealistadeveserpopulada
comoscontatoscadastradosemnossosistema.
Primeiro, vamos disponibilizar no escopo do controller
public/js/controllers/ContatoController.js a lista que
seráacessadapelaview:
// public/js/controllers/ContatoController.js
angular.module('contatooh').controller('ContatoController',
function($scope, $routeParams, Contato) {
// código anterior omitido
Contato.query(function(contatos) {
$scope.contatos = contatos;
});
});
Agora,adicionaremosacaixadesele çãonaviewimediatamenteapóso
from-groupcomoe-maildocontato:
<! -- public/partials/contato.html -->
<div class="form-group">
<label for="emergencia">Emergência </label>
<select id="emergencia"
class="form-control" >
ng-model="contato.emergencia"
</select>
</div>
182

## Página 195

CasadoCódigo Capítulo7. IntegrandoExpresseMongoDB
Repare que adicionamos na tag<select> a diretiva ng-model.
Quando um contato de emergência for selecionado da lista e o usuário
clicar no botão salvar, seu ObjectId será salvo diretamente em
contato.emergencia.Aquestãoagoraésabercomoconstruiremosalista.
7.14 Adiretiv a ng-options
Vimosnase çãoanteriorousodatag <select>paraexibiruma combobox
comtodososcontatoscadastrados,masaindafaltapopularmosalista.Sabe-
mosquecadacontatodeverátersuarespectivatag <option>. Porém,
nolugardeadicionarmosváriastags <option>, utilizaremosadiretiva
ng-optionsdoAngularJSresponsávelporpopularatag <select>:
<! -- public/partials/contato.html -->
<div class="form-group">
<label for="emergencia">Emergência</label>
<select id="emergencia"
class="form-control" >
ng-model="contato.emergencia"
ng-options=
"contato._id as contato.nome for contato in contatos"
</select>
</div>
Adicionamos a diretiva ng-options, que possui comportamento
parecido com ng-repeat, porém a sintaxe "contato._id as
contato.nome" indica que o valor do elemento será oObjectId
docontatoeoqueseráexibidoparasele çãoseráseunome.Orestante "for
contato in contatos" percorreráalistadecontatosdisponibilizadano
escopodocontroller,construindocadaitemdenossalista.
Podemos salvar todas as alterações e experimentar associar algumas
emergênciasparaalgunscontatos:
183

## Página 196

7.14. Adiretivang-options CasadoCódigo
Fig.7.1:Associandoemergênciaaocontato
Porém, teremos um problema ao gravarmos um novo contato sem
emergênciaedepoistentarmosatualizarseunome,porexemplo. Receber-
emosnoconsoleamensagem:
[TypeError: Cannot read property '_id' of undefined]
Parasolucionaresteproblema,verificamosseovalordachaveemergência
é undefined;sefor,substituímosseuvalorpor null.Outrasoluçãoénão
incluirachave emergencianaatualizaçãocasoseuvalorseja undefined:
controller.salvaContato = function(req, res) {
var _id = req.body._id;
// testando por undefined
req.body.emergencia = req.body.emergencia || null;
if(_id) {
Contato.findByIdAndUpdate(_id, req.body).exec()
.then(
function(contato) {
res.json(contato);
},
function(erro) {
console.error(erro)
res.status(500).json(erro);
}
);
} else {
// código comentado
184

## Página 197

CasadoCódigo Capítulo7. IntegrandoExpresseMongoDB
}
};
Somos capazes de associar emergências aos contatos, mas seria
interessante exibirmos a emergência do contato em uma coluna lá
na listagem de contatos. Vamos adicionar uma nova coluna em
public/partials/contatos.htmlimediatamenteapósa <td>queex-
ibeoe-maildocontato:
<! -- imediatamente após o th com do e-mail -->
<th>Emergência</th>
...
<! -- imediatamente após a td com o e-mail do contato -->
<td>{{contato.emergencia.nome}}</td>
Terminamos! Porém,aorecarregarmosapágina,nenhumdoscontatos
comemergênciaassociadaexibeainformaçãoemsuacoluna.Porquê?Éo
queveremosnapróximase ção.
7.15 Afunção populate e busca de referências
Quandodefinimosumareferênciaemnossoesquema,apenasdamosuma
pistaparaoMongoosedecomoeledevebuscá-la,porémtemosqueexplicitar
issoemnossocódigoatravésdafun ção populate.
Emnossocontroller app/controllers/contato.js,temosafun ção
listaTodos.Nela,utilizamosafun ção Contato.findparalistartodosos
contatoscadastradoseque,nofinal,retornauma promiseatravésdachamada
àfunção exec. Precisamoschamara populateantesderetornamosa
promise,istoé,antesdachamadaà exec:
// app/controllers/contato.js
// anterior omitido
Contato.find().populate('emergencia').exec()
// código posterior omitido
Reparequepassamosparaafun ção populateareferênciaqueoMon-
goosedeveráresolverparanós.Nofinal,cadacontatodenossalista,nolugar
185

## Página 198

7.15. Afunçãopopulateebuscadereferências CasadoCódigo
deconterapenaso ObjectIddasuaemergência,conteráaemergênciain-
teiracomoum embedded document. Agoraquetemosumdocumento
completo,podemosacessarqualquerumadesuaspropriedadesemnossa
view:
Fig.7.2:Exibindocontatodeemergência
Perfeito!MaisumafuncionalidadeimplementadacomoauxíliodoMon-
goose.
Acessoliberadoparatodos?
Aprendemosarealizaroperaçõesdeconsulta,inclusão,remo çãoeatu-
alizaçãoatravésdoMongoose,eassimterminamosapartedepersistência
danossaaplicação.Porém,nossosistemaestáabertoparaqualquerumque
saibasuaURL.Precisamosgarantirqueapenasusuáriosautenticadospos-
samutilizarnossaaplicaçãoeéexatamenteesteassuntoqueabordaremosno
próximocapítulo.
186

## Página 199

Capítulo8
AutenticaçãocomPassport
“ Aprender sem pensar é esforço vão; pensar sem nada aprender é nocivo”
–Confúcio
Precisamosgarantirqueapenasusuáriosautenticadostenhamacessoà
nossaaplicação,porémnãoqueremosarmazenardadossensíveiscomosen-
hasporumaquestãodeseguran ça. Tambémnãodesejamosimplementar
nossopróprioservidordeautenticação.
Umasoluçãoéutilizarmosserviçosdeautenticaçãogratuitosfornecidos
nawebcomoosdoFacebook,doTwitterentreoutros.Utilizaremososerviço
doGitHub(https://github.com/).

## Página 200

8.1. OAuth2.0 CasadoCódigo
Conta no GitHub
CasovocênãotenhaumacontanoGithub,estaéahoradecriá-laem
https://github.com.Oregistroégratuitopararepositóriospúblicos.
OGitHubutilizaoprotocoloOAuth2.0paraautorizaç ão.Antesdeen-
trarmosnosdetalhesdesuaimplementaçãoemnossaaplicação,faremosum
apanhadogeraldecomooprotocolofunciona.
8.1 OAuth 2.0
OAuth2.0éumprotocoloabertoparaautenticação(quemvocêé)eautoriza-
ção(oquevocêpodefazer)quepermiteaplicaçõesacessaremosdadosuma
dasoutras.Eleveiosubstituiraversão1.0criticadapelasuacomplexidadee
usodecertificados.OAuth2.0utilizaapenasSSL/TSL.
Papéisenvolvidos
HáquatropapéisenvolvidosduranteofluxodoOAuth2.0.Sãoeles:
•DONODORECURSO:usuárioouaplicaç ãocujosrecursosdeseja
compartilhar.
•SERVIDOR DE RECURSOS: local dos recursos doDONO DO
RECURSO.
•APLICAÇÃOCLIENTE:acessarecursosdo DONO DO RECURSO em
um SERVIDOR DE RECURSOS.
•SERVIDORDEAUTORIZAÇÃO:autorizaa APLICAÇÃO CLIENTE
ateracessoaosrecursosdo DONO DO RECURSO emum SERVIDOR
DE RECURSOS.
188

## Página 201

CasadoCódigo Capítulo8. AutenticaçãocomPassport
Ofluxodoprotocolo
OOAuth2.0segueumfluxobemdefinido.Vejamosissonocontextoda
nossaaplicação:
1) OusuárionãoautenticadotentaacessaraAPLICAÇÃOCLIENTECon-
tatooh.
2) AAPLICAÇÃOCLIENTEredirecionaousuárioparaapáginadelogin
doGitHub,porémenviandonarequisiçãoo CLIENT_IDdaaplicação.
Dessamaneira,oSERVIDORDEAUTORIZAÇÃOsabequemestáten-
tandoacessarorecursoprotegido.
3) OusuárioseloganoGitHube,logoemseguida,éenviadoatravésdeuma
REDIRECT_URInovamenteparaaAPLICAÇÃOCLIENTE,inclusive
umCÓDIGODEAUTENTICAÇÃOéenviadonarequisiç ão.
4) Por baixo dos panos, a APLICAÇÃO CLIENTE se conecta direta-
menteaoSERVIDORDEAUTORIZAÇÃOenviandoseu CLIENT_ID,
CLIENT_PASSWORDeoCÓDIGODEAUTENTICAÇÃOrecebidono
redirecionamento.
5) O SERVIDOR DE AUTENTICAÇÃO devolve para a APLICAÇÃO
CLIENTEumCONSENTIMENTODEAUTORIZAÇÃOquepermite
acessoàsinformaçõesdoDONODORECURSO.
AgoraquejátemosumaideiadecomooprotocoloOAuth2.0funciona,
aprenderemosnapróximase çãoaregistrarnossaaplicaç ãoContatoohno
provedordeautenticaçãoescolhido.
8.2 Registro no provedor de autenticação
UtilizaremosoGitHubparaautenticarnossosusuáriosquedevempossuir
umacontanesteserviço.PrecisamosregistrarnossaaplicaçãoContatoohno
própriosite(https://github.com/).Geralmente,criamosumusuárioespecí-
ficoparaaaplicaçãoeneleregistramosaaplicaç ão,masnadaimpedeque
vocêuseasuamesmacontaparaessafinalidade.
189

## Página 202

8.2. Registronoprovedordeautenticação CasadoCódigo
Acessandoprofile
DepoisdelogaremsuacontanoGitHub,nocantosuperiordireitohá
umaengrenagemque,aoserclicada,olevarádiretamenteparaseuprofile:
Fig.8.1:Github:atalhoprofile
Registrandonovaaplicação
Napáginadeprofile,nocantoesquerdo,háumpainelcomumasériede
links.Olink Applicationsexibeumatelacomasaplicaçõesjáregistradase
obotão RegisternewApplication,paraquepossamoscadastrarnossaapli-
cação.Nateladeregistro,vocêprecisaráinformar:
•Applicationname: podemosutilizarqualquernome,emnossocaso
serácontatooh.
•HomepageURL:comonossaaplicaç ãowebaindarodalocalmente,
preenchacomhttp://localhost:3000.
•ApplicationDescription:coloqueumabrevedescriçãodasuaappou
deixeembranco.
•AuthorizationcallbackURL:oendere çodanossaaplicaçãoqueserá
chamadopeloGitHubapósaautenticação.Vamosutilizaroendere ço
http://localhost:3000/auth/github/callback.
Porfim,cliquenobotão Registerapplication parafinalizaroregistro.
Comaaplicaçãoregistrada,nocantosuperiordireitoseráexibidoo CLIENT
IDeoCLIENTSECRET.Tomenotadessasinformaçõespoiselasserãouti-
lizadasmaisàfrente:
190

## Página 204

8.3. OAuth2.0comPassport CasadoCódigo
Suainstalaçãoéfeitaatravésdo npm.Sónãoesque çadeexecutá-lodentro
dapastaraizdoprojeto,localdonossoarquivo package.json:
npm install passport@0.2 --save
AinicializaçãodoPassportdependedeoExpressestarconfiguradopara
trabalharcomsessões,algoqueaindanãofizemos.Éporissoqueinstalare-
mososmódulos express-sessioneo cookie-parser:
npm install express-session@1.7 cookie-parser@1.3 --save
Precisamosalteraragoranossoarquivo config/express.jsparaati-
varmosos middlewaresdecookie,sessãoedeinicializaç ãodoPassport:
// config/express.js
var cookieParser = require('cookie-parser');
var session = require( 'express-session');
var passport = require('passport');
// código abaixo vem antes do carregamento de rotas
app.use(cookieParser());
app.use(session(
{ secret: 'homem avestruz',
resave: true,
saveUninitialized: true
}
));
app.use(passport.initialize());
app.use(passport.session());
// código posterior omitido
Oprimeiromiddleware cookieParserrealizaoparserdo headerde
cookiesdarequisiçãopopulando req.cookiesearmazenaoIDdasessão.
Osegundomiddleware sessioncriaporpadrãoasessãodousuárioem
memória.Elerecebetrêsparâmetros:
192

## Página 205

CasadoCódigo Capítulo8. AutenticaçãocomPassport
•secret:ocookiedesessãoéassinadocomestesegredoparaevitaradul-
teração.
•resave: garantequeasinformaçõesdasessãoserãoacessíveisatravés
decookiesacadarequisição.
•saveUnitialized:essaop çãosolucionaproblemasqueenvolvemareq-
uisiçãodeumapermissãoantesdeatribuirumcookie.
Quando usamos Express, precisamos chamar a fun ção
passport.initializeparainicializaroPassport.Comonossaaplicaç ão
usasessõesdeloginpersistentes,tambémprecisamosutilizaromiddleware
passport.session.
Umpontoadestacaréqueainicializaç ãodasessãodoExpressdevevir
sempreantesde passport.sessionparagarantirmosqueasessãodelogin
sejarestauradanaordemcorreta.
middlew are hell
No Express, o desenvolvedor precisa saber exatamente em qual
posiçãodapilhaconfigurarumnovomiddlewareeseuimpactonosde-
mais. Quantomaioronúmerodemiddlewares,maisdifícilserásua
tarefa.Essacomplexidadeéapelidadade middlewarehell.
AntesquepossamosutilizaroPassportparaautenticarnossasrequisições,
umaestratégiadeautenticaçãoprecisaserconfigurada.
8.4 Estratégia de autenticação
OPassportpossuiváriasestratégiasdeautenticação,inclusivepodemoscriar
novasestratégias. Porém,jádefinimosquenosautenticaremosatravésdo
GitHube,porisso,baixaremosumaestratégiaespecíficaparaesteprovedor
deautorização:
npm install passport-github@0.1 --save
193

## Página 206

8.4. Estratégiadeautenticação CasadoCódigo
Precisamospassaralgumasconfiguraçõesparanossaestratégiaeregistrá-
lanoPassport.Criaremosummódulocomestafinalidade.Primeirocriare-
mosoarquivo config/passport.jseneleimportaremosoPassportea
estratégiadeautenticação:
// config/passport.js
var passport = require('passport');
var GitHubStrategy = require('passport-github').Strategy;
Utilizaremos como estratégia de autenticação uma instância de
GitHubStrategy que recebe dois parâmetros. O primeiro é um ob-
jetocomaschaves clientID, clientSecret, callbackURLcomseus
respectivosvaloresdisponibilizadosnaconfiguraçãodenossaaplicaçãono
GitHub.Osegundoparâmetroéumcallbackqueserá chamadoapenasuma
vezquandoousuárioseautenticar:
// config/passport.js
// código anterior omitido
module.exports = function() {
// código anterior omitido
passport.use(new GitHubStrategy({
clientID: 'SEU CLIENT ID',
clientSecret: 'SEU CLIENT PASSWORD',
callbackURL: 'SUA REDIRECT_URI'
}, function(accessToken, refreshToken, profile, done) {
}));
};
Reparequeocallbackrecebequatroparâmetros,masoquerealmente
nosinteressasãoosdoisúltimos: profilee done.Oprimeiroéumobjeto
querepresentaoperfildousuárionoGitHub. Osegundo,umafun çãode
callbackquedeverecebercomoparâmetroosdadosquequeremosmaistarde
armazenarnasessão. Quedadosserãoesses? Éoqueveremosnapróxima
seção.
194

## Página 207

CasadoCódigo Capítulo8. AutenticaçãocomPassport
8.5 DefinindoSchema do Usuário
Emumaaplicaçãotípica,associamosoprofiledoGitHubcomumusuário
emnossobanco,retornando-onolugardoprofileparaafun ção doneda
estratégiaquevimosnase çãoanterior.Éissoquefaremos.
Criaremos primeiro o arquivoapp/models/Usuario.js, no qual
definiremos um esquema para, logo em seguida, disponibilizarmos um
Modelapartirdele:
// app/models/Usuario.js
var mongoose = require('mongoose');
module.exports = function() {
var schema = mongoose.Schema({
login: {
type: String,
required: true,
index: {
unique: true
}
},
nome: {
type: String,
required: true,
},
inclusao: {
type: Date,
default: Date.now
}
});
return mongoose.model('Usuario', schema);
};
Reparequetemosumanovidade.Utilizamosotipo Dateparaachave
inclusaoeadotamoscomovalorpadrãoadataatualdosistema.Asnovi-
dadesaindanãoacabaram,veremosmaisumacomMongoosenapróxima
seção.
195

## Página 208

8.6. Mongooseeplugins CasadoCódigo
8.6 Mongoose e plugins
Criamosnase çãoanterioro Model Usuario paraquepossamosrealizar
operaçõesdeconsultaepersistênciaemnossobanco.Sabemosqueafun ção
decallbackpassadaparanossaestratégiadeautenticaç ãoseráchamadaape-
nasumavezquandoousuárioseautenticarequenelatemosacessoaoseu
perfilnoGitHubatravésdoparâmetro profile.Énestemomentoquebus-
caremosousuárioemnossobanco.
Utilizaremoscomocritériodebusca profile.username,criandoum
novousuárionobancocasoelenãoexista. Nofinal,passaremosousuário
existenteourecém-criadocomoparâmetroparaafun ção doneconcluindo
oprocesso.
Sabemosimplementaressatarefautilizandoasfun çõesfinde create,
porémqueremosalgomaisdiretocomo findOrCreate,justamenteuma
funçãoqueoMongoosenãoimplementaporpadrão.Podemosresolverisso
facilmenteutilizandoosistemadepluginsdoMongoose. Primeiro,através
do npminstalaremosoplugin:
npm install mongoose-findorcreate@0.1 --save
Agora,bastaimportamosopluginassociando-ocom Schema:
// app/models/Usuario.js
var mongoose = require('mongoose');
// importando o plugin
var findOrCreate = require('mongoose-findorcreate')
// código da declaração do esquema omitido
// associando plugin ao nosso esquema
schema.plugin(findOrCreate);
return mongoose.model('Usuario', schema);
};
Excelente!Agora,jápodemosimplementarnossalógicaquebuscaoucria
umusuárioparanósemnossobanco,disponibilizandonofinalousuárioen-
contradooucriado.Mastemosumproblema:nossomódulodeconfiguraç ão
196

## Página 209

CasadoCódigo Capítulo8. AutenticaçãocomPassport
doPassportnãopossuiumareferênciaparaoExpress.Comoteremosacesso
ao Model Usuario?Simples,podemossolicitaraopróprioMongooseum
Modelatravésdafunção mongoose.modelpassandoonomedo Model
comoparâmetro. Paraisso,precisaremosimportaroMongooseemnosso
módulo:
// config/passport.js
// código anterior omitido
var mongoose = require('mongoose');
module.exports = function() {
var Usuario = mongoose.model('Usuario');
// código anterior omitido
passport.use(new GitHubStrategy({
clientID: 'SEU CLIENT ID',
clientSecret: 'SEU CLIENT PASSWORD',
callbackURL : 'SUA REDIRECT_URI'
}, function(accessToken, refreshToken, profile, done) {
Usuario.findOrCreate(
{ "login" : profile.username},
{ "nome" : profile.username},
function(erro, usuario) {
if(erro)
console.log(erro);
return done(erro);
}
return done(null, usuario);
}
);
}));
};
197

## Página 210

8.7. Serializaçãoedesserializaçãodousuário CasadoCódigo
Promise?
Oplugin findOrCreatenãotemsuportea promises.
Afunção Usuario.findOrcreaterecebecomoprimeiroparâmetro
profile.usernamedoGitHub,nossocritériodebusca. Ousuárioserá
retornadocasoocritériosejaatendido,casocontrário,seráadicionadoum
novoemnossobanco,porémopadrãoéincluirapenasachavedocritériode
buscacomoinformação.Éporissoqueadicionamososegundoparâmetro,
quecontémosdadoscomplementares,emnossocaso,apenasachave nome,
quereceberátambémcomovaloro profile.usernamedoGitHub. No
final,passamosousuárioqueveiodonossobancoparaafun ção done.
Profile e normalização
OPassportpadronizaoobjeto profiledisponibilizandochavesco-
munscomo usernamee displayNameindependentedaestratégia
utilizada.
Oquefaremoscomessainformaç ãodisponibilizadaparaoPassport?
Gravaremosdiretamentenasessão?Ecomofaremosparaacessá-laemnos-
sasrequisições?PrecisamosdarumapistaparaoPassportdecomolidarcom
essassituações.
8.7 Serialização e desserialização do usuário
PrecisamosindicarparaoPassportcomoainformaç ãodousuárioseráseri-
alizadanasessão,processorealizadoapenasumavezquandoousuárioseau-
tenticar.Nãopodemossimplesmentepersistirousuáriototalmentenasessão.
Imaginesenovasinformaçõesfossemadicionadas?
198

## Página 211

CasadoCódigo Capítulo8. AutenticaçãocomPassport
SerializandooObjectIDdousuárionasessão
Nãoqueremoscorreroriscodeoneraramemóriadoservidorguardando
informações desnecessárias, motivo pelo qual serializaremos apenas o
ObjectIddousuárionasessão.Esseprocessoérealizadoatravésdafun ção
passport.serializeUser,querecebedoisparâmetros. Oprimeiroéo
usuárioquefoipassadopelaestratégiadeautenticaç ão. Osegundo,uma
função que recebe a informação do usuário que desejamos serializar na
sessão:
// config/passport.js
// código anterior omitido
module.exports = function() {
// código anterior omitido
/*
Chamado apenas UMA vez e recebe o usuário do nosso
banco disponibilizado pelo callback da estratégia de
autenticação. Realizará a serialização apenas do
ObjectId do usuário na sessão.
*/
passport.serializeUser(function(usuario, done) {
done(null, usuario._id);
});
};
Porém,todavezqueprecisarmosacessaroutrasinformaçõesdousuário
em nossos controllers, será necessário buscá-lo no banco através de seu
ObjectId. Aboanotíciaéquepodemosdelegaresseprocessode desse-
rializaçãoaoPassport.
Desserializandoousuáriodasessão
Emcadarequisição,oPassportchamarásuafun çãodedesserialização
passandocomoparâmetroo ObjectIddousuárioarmazenadonasessão.
199

## Página 212

8.8. Protegendorecursos CasadoCódigo
Usaremosessainformaçãoparabuscarousuárionobanco,inclusiveoPass-
portdisponibilizaráousuárioencontradoemcadarequestatravésdachave
req.user,tornando-ofacilmenteacessívelemnossoscontrollers:
// config/passport.js
// código anterior omitido
module.exports = function() {
// código anterior omitido
// Recebe o ObjectId do usuário armazenado na sessão
// Chamado a CADA requisição
passport.deserializeUser(function(id, done) {
Usuario.findById(id).exec()
.then(function(usuario) {
done(null, usuario);
});
});
};
Atéagora,inicializamosoPassportcomoExpress,configuramossuaes-
tratégiadeautenticaçãoeimplementamosasfun çõesdeserializaçãoedesse-
rializaçãodousuário.Porém,aindanãoestamosprotegendoosrecursosda
nossaaplicação,assuntoqueveremosaseguir.
8.8 Protegendo recursos
Aindafaltadefinirmosasrotasenvolvidasnoprocessodeautenticaç ão,prin-
cipalmenteaquelaqueprotegeránossosrecursos. Vamoscriaroarquivo
app/routes/auth.js:
// app/routes/auth.js
module.exports = function(app) {
app.get('/auth/github', passport.authenticate('github'));
200

## Página 213

CasadoCódigo Capítulo8. AutenticaçãocomPassport
app.get('/auth/github/callback',
passport.authenticate('github', {
successRedirect: '/'
}));
}
Aprimeirarota /auth/githubredirecionaráousuárioparaapágina
de login do GitHub enviando por baixo dos panos oCLIENT ID da
aplicação. Repare que utilizamos como controller o retorno da função
passport.authenticate(‘github’), que saberá lidar com a requi-
sição.
A segunda rota/auth/github/callback possui o mesmo iden-
tificador que cadastramos comoAuthorization callback URL no
GitHub. Quandoousuárioselogar,oGitHubchamaráarotapassandoo
CÓDIGODEAUTORIZAÇÃO.Comocódigorecebido,oPassportseco-
municaráporbaixodospanoscomoSERVIDORDEAUTENTICAÇÃOque
protegeoprofiledousuárionoGitHub,solicitandooCONSENTIMENTO
DEAUTORIZAÇÃOparadaíacessaroprofile. Seaautenticaç ãoforbem-
sucedida,ousuárioserádirecionandoparanossaaplicaçãoContatooh.
Verificandoautenticaçãodousuário
Nossasoluçãoaindanãoestácompleta, precisamosdirecionarparaa
páginadeloginqualquerusuárionãoautenticado.
O Passport convenientemente disponibiliza na requisição a função
isAutenticated,quenospermitesaberemnossoscontrollersseousuário
estáautenticadoounão.Seeleestiverautenticado,deixaremosqueaspróxi-
masrotasdefinidassejamprocessadas,casocontrário,eleseráredirecionado
paraumapáginacomapenasolink“EntrepeloGitHub”. Essapáginaserá
uma view ejs,logo,sópoderáseracessadaatravésdeumarotaespecífica.
Masqualrotautilizaremos?Criaremosumaqueserásempreativadain-
dependentedoidentificadordorecursoutilizado. Conseguimosissofacil-
mentecomoidentificador /:
// app/routes/auth.js
// código anterior omitido
201

## Página 214

8.8. Protegendorecursos CasadoCódigo
module.exports = function(app) {
// código anterior omitido
app.get('/', function(req, res, next) {
if(req.isAuthenticated()) {
// permite que outras rotas sejam processadas
return next();
} else {
// renderiza auth.ejs
res.render( "auth");
}
});
};
Repare que na própria declaração da rota já implementamos seu
controller através de uma função anônima, não havendo a necessi-
dade de criar um novo arquivo.js. Criaremos agora nossa view
app/views/auth.ejs:
<!-- app/views/auth.ejs -->
<!docytype html>
<html>
<head>
<title>Autenticação do Usuário</title>
<meta name="viewport" content="width=device-width">
<meta charset= "UTF-8">
<link rel="stylesheet"
href="vendor/bootstrap/dist/css/bootstrap.css">
<link rel="stylesheet"
href="vendor/bootstrap/dist/css/bootstrap-theme.css">
</head>
<body>
<div class="container">
<a href="/auth/github">
202

## Página 215

CasadoCódigo Capítulo8. AutenticaçãocomPassport
<h1 class="text-center">Entre pelo GitHub</h1>
</a>
</div>
</body>
</html>
Reparequeolink“EntrepeloGitHub”apontaparaarotaauth/github,
aquela de nossa aplicação responsável pelo redirecionamento e envio do
CLIENT ID da aplicação para o SERVIDOR DE AUTORIZAÇÃO do
GitHub.
Oproblemaéqueprecisamostercertezadequenossarotadeverificaç ão
daautenticaçãodousuáriosejaaprimeiraaserexecutada.Podemosgaran-
tirissocom express-loadexplicitandoqueeladeveseraprimeiraaser
carregada:
// config/express.js
// código anterior omitido
load('models', {cwd: 'app'})
.then('controllers')
.then('routes/auth.js')
.then('routes')
.into(app);
Agora,emnosso server.js,precisamoscarregarnossomódulode
configuraçãodoPassportimediatamenteapósaconfiguraç ãodoExpress:
// server.js
var http = require('http');
var express = require('express');
var app = express();
require('./config/express')(app);
require('./config/passport')();
require('./config/database')('mongodb://localhost/contatooh');
http.createServer(app).listen(app.get('port'), function(){
console.log('Express Server escutando na porta ' +
203

## Página 216

8.8. Protegendorecursos CasadoCódigo
app.get('port'));
});
Antesdetestarmosoresultado,tenhacertezadequenãoestejalogadono
GitHubparaquepossamosvertodasasetapasacontecendo.
Depoisdereiniciaroservidor,tenteacessaraaplicaç ão.Vocêdeveráser
redirecionadoparaaview auth.ejscomolink“EntrepeloGitHub”,que
ativaráarotadopassportresponsávelpeloenviodo CLIENT ID desuaapli-
caçãoparaoserviçodeautenticaçãodoGitHub.
Fig.8.3:Solicitaçãodelogin
Depoisdeclicarnolinkerealizaroprocessopelaprimeiravez,oSERVI-
DORDEAUTORIZAÇÃOdoGitHubsolicitaráumaconfirmaç ãoparaque
aaplicaçãoContatoohacesseorecurso.Nãosepreocupe,essaconfirmaç ão
serárealizadaapenasumavez.
Fig.8.4:AutorizaçãodeacessodaaplicaçãoàsuacontanoGitHub
ImplementamosautenticaçãoemnossosistemaatravésdeOAuth2.0com
ajudadoPassport,masaindafaltaexibirmosumainformaç ãomuitocomum
emsistemas:ousuáriologado.
204

## Página 217

CasadoCódigo Capítulo8. AutenticaçãocomPassport
8.9 C ombinando views do servidor/cliente
Precisamosexibirousuáriologadoemnossaaplicação,inclusivepodemosaté
criarumarotacomestainformaçãoacessívelpornossoclienteemAngularJS.
Porém,aprendemosnaseção2.6atrabalharcomtemplates ejsprocessados
noladodoservidor. Estaéumaboahoradefazermosaspazescomesta
tecnologiaeaproveitarmosomelhordosdoismundos.Apágina index.ejs
continuarásendoumaviewdoAngularJS,porémonavegadorjáareceberá
comainformaçãodousuáriologado.
Nossoprimeiropassoserámovernossapágina public/index.html
paraapasta app/views,renomeando-apara index.ejs. Emseguida,
adicionaremosumalacunaemnossotemplateindicandoqueeleprecisada
informação usuarioLogado:
<!-- app/views/index.ejs -->
<! -- antes da div com a diretiva ng-view -->
<div class="text-right">
<p>
Logado como: <span id="usuario-logado">
<%=usuarioLogado %>
<span>
</p>
</div>
Comonãotemosmaisapágina public/index.html,aURL http:
//localhost:3000 deixarádefuncionar. Vamoscriararota /pararecuper-
armosestepadrão,devolvendonossaview app/views/index.ejscom
a informação do usuário logado já preenchida. Vamos criar o arquivo
app/routes/index.ejs,quefarátodoessetrabalhoparanós. Nãopre-
cisamosnospreocuparemassociá-locomoExpressporqueestamosuti-
lizandoo express-load,quejáocarregaráautomaticamente:
// app/routes/index.js
module.exports = function(app) {
app.get('/', function(req, res) {
res.render( 'index', { "usuarioLogado" : req.user.login});
205

## Página 218

8.10. ImplementandoLogout CasadoCódigo
});
};
Reparequeestamosbuscandonarequisiçãoainformaçãodousuáriolo-
gado.Lembre-sequeessainformaçãosempreestarádisponívelporcausado
processodedesserializaçãodousuáriodasessãorealizadopeloPassport.
JápodemostestarreiniciandonossoservidoreacessandoaURL http:
//localhost:3000. Tudodevecontinuarfuncionando,aúnicadiferen çaéa
exibiçãodousuáriologadonotopodireitodenossapágina.
Fig.8.5:Usuáriologado
8.10 Implementando Logout
Nossaautenticaçãoestáfuncionando,inclusiveexibimosousuáriologadoem
nossapágina,porémfaltaaindaimplementarmosafuncionalidadedelogout.
Vamoseditarnossarota app/routes/auth.jsadicionandoarota
/logout.Nela,chamaremosafun ção req.logOutadicionadaautomati-
camentepeloPassportacadarequisição.Porfim,redirecionaremosousuário
paraapáginaprincipalatravésdarota /:
// app/routes/auth.js
// código anterior omitido
module.exports = function(app) {
// código anterior omitido
206

## Página 220

8.11. RESTEndpoints:permitindoapenasacessoautenticado CasadoCódigo
eexperimenteacessardiretamentepelonavegadornosso REST Endpointque
devolveumalistadecontatos:
http://localhost:3000/contatos
Paranossoespanto,elecontinuaacessível,mesmoparausuáriosnãoaut-
enticados.IssoaconteceporquenãoestamosverificandoemnossaAPIREST
aautenticaçãodousuário,masimagineconsultar req.isAutenticated
emcadaumdenossoscontrollers?Comcertezaestaríamoscolocandouma
responsabilidadequenãolhedizemrespeito.
A boa notícia é que podemos definir mais de uma função
de callback para o tratamento de rotas. Em nosso arquivo
app/controllers/contato.js, criaremos uma função com a re-
sponsabilidade de verificar se o usuário está autenticado. Se ele estiver,
damosachanceparaqueopróximocallbackprocessearequisiç ão, caso
contrário,enviaremoscomoresposta“Nãoautorizado”comostatus 401
(Unauthorized):
// app/controllers/contato.js
function verificaAutenticacao(req, res, next) {
if (req.isAuthenticated()) {
return next();
} else {
res.status('401').json('Não autorizado');
}
}
Emseguida,passaremosafun çãocomoprimeirocallbackparaotrata-
mentodasrotas:
// app/controllers/contato.js
// código anterior omitido
module.exports = function (app) {
var controller = app.controllers.contato;
app.route( '/contatos')
208

## Página 221

CasadoCódigo Capítulo8. AutenticaçãocomPassport
.get(verificaAutenticacao, controller.listaTodos)
.post(verificaAutenticacao, controller.salvaContato);
app.route('/contatos/:id')
.get(verificaAutenticacao, controller.obtemContato)
.delete(verificaAutenticacao, controller.removeContato);
};
VocêjádeveterpercebidoquerotasdoExpresstambémsãomiddlewares
equeaordemfaztodaadiferen ça.Emnossocaso,alémdaimportânciada
ordemdedeclaraçãodasrotas,elasrecebemagoradoisparâmetros.Anovi-
dadeéqueosegundocallbackpassadocomoparâmetro,nossocontroller,
seráchamadoapenasseousuárioestiverautenticado.
Podemosdeixaraindamelhornossocódigoisolandoocódigodeveri-
ficaçãodaautenticaçãoemseuprópriomódulo. Faztodosentido,porque
ela poderá ser reaproveitada por outros controllers de nossa aplicação,
não apenas app/controllers/contato.js. Vamos criar o módulo
contatooh/config/auth.js,quedevolvenossafun çãodeverificaçãono
lugardeumobjeto:
// contatooh/config/auth.js
module.exports = function(req, res, next) {
if (req.isAuthenticated()) {
return next();
} else {
res.status('401').json('Não autorizado');
}
};
Agora,vamosalterar app/controllers/contato.js,quenofinal
deveráestarassim:
var verificaAutenticacao = require('../../config/auth');
module.exports = function (app) {
var controller = app.controllers.contato;
209

## Página 222

8.11. RESTEndpoints:permitindoapenasacessoautenticado CasadoCódigo
app.route('/contatos')
.get(verificaAutenticacao, controller.listaTodos)
.post(verificaAutenticacao, controller.salvaContato);
app.route('/contatos/:id')
.get(verificaAutenticacao, controller.obtemContato)
.delete(verificaAutenticacao, controller.removeContato);
};
Pronto! Experimenteacessar(http://localhost:3000/contatos)semestar
autenticado.Vocêdevereceberamensagem“Nãoautorizado”.
Agorapodemosiralémdaautenticaçãoetornarnossaaplicaç ãoainda
maissegura,assuntodopróximocapítulo.
210

## Página 223

Capítulo9
Tornandosuaaplicaçãoainda
maissegura
“ Age sempre de tal modo que o teu comportamento possa vir a ser princípio de
uma lei universal. ”
–EmmanuelKant
Estecapítulodemonstrarácomoépossívelaplicarpequenasmodificações
emnossaaplicaçãotornando-aaindamaissegura.Sãoelas:
NoExpress:
• Adicionarouremoverinformaçõesdoheaderdasrequisições;
• Evitar“vazar”atecnologiautilizada.
NoMongoDB:

## Página 224

9.1. Helmet:middlewaresdesegurança CasadoCódigo
• Prevenirquery selector injection;
• Substituiraestratégiadocument replace.
Vamoscomeçarcontrolandoasinformaçõesdoheaderdasrequisições.
9.1 Helmet: middlew ares de segurança
Umpontoimportanteparagarantiraseguran çadenossaaplicaçãoécon-
trolandoasinformaçõespresentesnoheaderdasrequisições. Veremosque
aomissãodeumheaderouaadiç ãodeoutropodetrazerbenefíciosparaa
segurança.
Nadanosimpededepesquisarmosnainternetquaisinformaçõesre-
moveremosouadicionaremosemnossoheader,porémfoicriadoumprojeto
comestafinalidade:o Helmet.
OHelmet(https://github.com/evilpacket/helmet)possuiumacoletânea
demiddlewaresdetratamentodeheaderjáprontosparauso,tornandonossa
aplicaçãomaissegura.Suainstalaçãoéfeitacomoqualqueroutromódulodo
Node.js:
npm install helmet@0.4 --save
Sequisermoshabilitartodososseusmiddlewares,bastaadicionarmos:
// config/express.js
helmet = require('helmet');
// código anterior omitido
// imediatamente após a inicialização da sessão do Passport
app.use(helmet());
// código posterior omitido
Masquaissãoosmiddlewaresativados?Seráquerealmenteprecisamos
ativartodoseles?Elesprotegemcontraqualataque?Existealgumalimitaç ão?
212

## Página 225

CasadoCódigo Capítulo9. Tornandosuaaplicaçãoaindamaissegura
Oidealéativarmosapenasaquelesmiddlewaresquefaç amsentidoden-
trodocontextodanossaaplicação,entendendoqualtipodeataqueelespro-
tegem. VejamososproblemasquepodemacometeraMEANStackequais
middlewaresdoHelmetutilizar.
EsconderX-Powered-By
Nãoéincomumaplicaçõesadicionaremnoheader httpainformação
**X-Powered-By**indicandoqualtecnologiaestásendoutilizadapelo
servidor. Hackerspodemutilizaressainformaçãoparatentarexplorarvul-
nerabilidadesconhecidasdatecnologiautilizada.Podemosresolverissofacil-
mentenoExpressdeixandodeinformaroheader X-Powered-By:
// imediatamente após a inicialização da sessão do Passport
app.disable('x-powered-by');
Ouvocêpodequererdificultaraindamaisavidadopotencialinvasor:
// imediatamente após a inicialização da sessão do Passport
app.use(helmet.hidePoweredBy({ setTo: 'PHP 5.5.14' }));
Nessecódigo,fornecemosumainformaçãofalsaatravésdomiddleware
helmet.hidePoweredBy:
Aplicação acessível indevidamente dentro de um <frame> ou
<iframe>
Nem sempre você quer que sua aplicação seja colocada dentro de
um <frame> ou <iframe>, evitando possíveis ataques do tipo
clickjacking.Esseataquedisponibilizaum <iframe>invisívelouredi-
mensionadocontendoapáginaqueoatacantequerquevisitemossemsaber,
porémeleécolocadosobrealgumelementodapáginacomolinksebotões
aparentementeinofensivos.Quandoclicarmossobreolinkoubotão,estare-
mosexecutandoumcódigodapáginado <iframe>enãodapáginanoqual
nosencontramos.Porém,podemosresolverisso:
// imediatamente após a inicialização da sessão do Passport
app.use(helmet.xframe());
213

## Página 226

9.1. Helmet:middlewaresdesegurança CasadoCódigo
Éatravésdomiddleware helmet.xframequeevitamosquenossas
páginassejamreferenciadaspor <frame>ou <iframe>.
FiltroXSS
UmexemploclássicodeXSS(cross-site scripting )envolveopostdeum
blog. Alguém,comaintençãoveladadeprejudicaroutrapessoa,adiciona
emseupostatag <script>queapontaparaumscriptmalicioso.Quando
opostforvisualizado(umquenãofoisanitizadopreviamente)nonavegador,
atagindevidamenteseráprocessada.Umasoluçãoparcialparaoproblemaé
utilizaromiddleware helmet.xssFilter:
// imediatamente após a inicialização da sessão do Passport
app.use(helmet.xssFilter());
Essecódigoadicionaoheaderhtpp X-XSS-Protectionoriginalmente
criadopelaMicrosoft. AGooglegostoutantodaideiaquemaistardeadi-
cionouosuportedesteheaderaoChrome.Oheadersolicitaaonavegadora
ativaçãodeumaprote çãoespecialcontraXSS.HásuporteapenasaoIE9+e
Chrome,sendodesabilitadoparaoutrosnavegadores,principalmenteosmais
antigos.
NãopermitirqueobrowserinfiraoMIMEType
Algunsnavegadorespermitemcarregaratravésdastags linke script
arquivosquenãosejamdos MIME types text/csse text/javascript,
respectivamente:
<!-- arquivo que não é um script -->
<script src="arquivo.txt"></script>
Porém,senoheaderderespostahouver X-Content-Type-Options:
nosniffonavegadornãopermitiráesseabuso:
// imediatamente após a inicialização da sessão do Passport
app.use(helmet.nosniff());
Vimos apenas quatro de uma série de middlewares suportados pelo
Helmet. O leitor pode consultar sua documentação (https://github.com/
214

## Página 227

CasadoCódigo Capítulo9. Tornandosuaaplicaçãoaindamaissegura
evilpacket/helmet)paraconheceroutroseavaliarsefazemsentidodentroda
MEANStack.Porfim,teremosemnossoarquivo config/express.jsos
seguintesmiddlewaresativados:
helmet = require('helmet');
// código anterior omitido
// imediatamente após a inicialização da sessão do Passport
app.use(helmet.xframe());
app.use(helmet.xssFilter());
app.use(helmet.nosniff());
app.disable('x-powered-by');
VimosquestõesqueafetamoExpress,masháalgumaqueafetadireta-
menteoMongoDB?Éoqueveremosnapróximase ção.
9.2 MongoDB/APIREST: evitando query selec-
tor injection
UmpontobastantedestacadodoMongoDBéofatodeeleser injection free,
diferentedebancosSQLnosquaisoataque SQL injectionépossível,depen-
dendodecomoodesenvolvedorestruturaseucódigo.
Masseráqueestamosmesmolivresdeinjection?Vamosrevisitarnossa
RESTAPIqueremoveumcontatodobancopeloseu ObjectId:
// app/controllers/contato.js
// código anterior omitido
controller.removeContato = function(req, res) {
var _id = req.params.id;
Contato.remove({"_id" : _id}).exec()
.then(
function() {
res.end();
},
function(err) {
return console.error(erro);
}
215

## Página 228

9.2. MongoDB/APIREST:evitandoqueryselectorinjection CasadoCódigo
);
};
// código posterior omitido
Nossa API espera receber como parâmetro uma string contendo o
ObjectIddocontato,porémoqueaconteceráse,nolugardepassarmos
umastring,passarmosumobjetocomo query selector $nequevimosna
seção6.12?Porexemplo:
{ "$ne" : null}
Bem,teríamoscomocritériofinalparanossaconsulta:
{"_id" : { "$ne" : null}}
Oparâmetroanteriorresultarianaremo çãodetodososcontatosdenosso
banco! Essamesmaestratégiapoderiaserutilizadaemoutroslugaresque
esperamumcritériodeconsulta.
Parasolucionarmosoproblemadeinje çãoatravésde query selectors,de-
vemosaceitarapenasstringscomocritério.Porém,serecebermosumobjeto,
bastaremoverqualquerchavequecontenha $comovalor. Háumprojeto
querealizaessaverificaçãoparanós,o mongo-sanitize(https://github.com/
vkarpov15/mongo-sanitize).Suainstalaçãoéfeitaatravésdo npm:
npm install mongo-sanitize@1.0 --save
Agorasóprecisamosalterar app/controllers/contato.jsesani-
tizar req.params.id:
// app/controllers/contato.js
var sanitize = require('mongo-sanitize');
// código anterior omitido
controller.removeContato = function(req, res) {
var _id = sanitize(req.params.id);
Contato.remove({"_id" : _id}).exec()
.then(
216

## Página 229

CasadoCódigo Capítulo9. Tornandosuaaplicaçãoaindamaissegura
function() {
res.end();
},
function(erro) {
return console.error(erro);
}
);
};
Pronto!Chavesquecontenhamqueryselectorsserãoremovidasdoob-
jeto.
9.3 Evitando o document replace
Aprendemosnase ção6.16oquantoéconvenienteparaodesenvolvedoruti-
lizar document replace comoestratégiadeatualizaçãodedocumentos,
inclusiveelafoicolocadaempráticanase ção7.10.Porém,emumaaplicação
quenãosejaumprotótipo,estaestratégiapodecausarefeitosindesejados.
Vamos revisitar a parte do código de nosso controller
app/controllers/contato.jsqueatualizaoucriaumcontato:
// app/controllers/contato.js
// código anterior omitido
controller.salvaContato = function(req, res) {
var _id = req.body._id;
if(_id) {
Contato.findByIdAndUpdate(_id, req.body).exec()
.then(
function(contato) {
res.json(contato);
},
function(erro) {
console.error(erro)
res.status( 500).json(erro);
}
);
217

## Página 230

9.3. Evitandoodocumentreplace CasadoCódigo
} else {
Contato.create(req.body)
.then(
function(contato) {
res.status(201).json(contato);
},
function(erro) {
console.log(erro);
res.status(500).json(erro);
}
);
}
};
// código posterior omitido
Vejaquenosdoiscasosconfiamosque req.bodyconterádadosdocon-
tato. Porém,nadaimpedequealguéminjeteindevidamentenosdadosdo
postoutrasinformaçõesquenãodizemrespeitoaocontato.Porexemplo:
// req.body
{ "nome": "X", "email" : "Y", "emergencia": "Z",
"outra-chave" : "W"};
ComoestamosutilizandoMongoose,oODMignoraráchavesquenão
façampartedoesquema,excelente!Porém,imaginesenossocontato,além
daschavesqueacabamosdevertivesseoutraquearmazenaonúmerodevezes
queocontatofoicontactado,informaç ãoquenãoestápresentenatelade
cadastro:
// req.body
{ "nome": "X", "email" : "Y", "emergencia": "Z",
"contactado" : 500000};
Comoachave contactadofazpartedoesquema,oMongooseaatu-
alizarágerandoinconsistênciadenossosdados.
Podemos resolver isso facilmente pinçando de req.bodyapenas as
chavesquefazemsentidodentrodaquelecontexto:
// app/controllers/contato.js
218

## Página 231

CasadoCódigo Capítulo9. Tornandosuaaplicaçãoaindamaissegura
// código anterior omitido
controller.salvaContato = function(req, res) {
var _id = req.body._id;
/*
Independente da quantidade de parâmetros,
apenas selecionamos o nome, email e emergencia:
*/
var dados = {
"nome" : req.body.nome,
"email" : req.body.email,
"emergencia" : req.body.emergencia || null
};
if(_id) {
Contato.findByIdAndUpdate(_id, dados).exec()
.then(
function(contato) {
res.json(contato);
},
function(erro) {
console.error(erro)
res.status( 500).json(erro);
}
);
} else {
Contato.create(dados)
.then(
function(contato) {
res.status( 201).json(contato);
},
function(erro) {
console.log(erro);
res.status( 500).json(erro);
}
);
}
};
// código posterior omitido
219

## Página 232

9.4. Tratando404 CasadoCódigo
Repareque,pormaisquesejainteressanteutilizarnaíntegraosdados
enviadosnarequisição,éaltamenterecomendadorealizarmosumfiltroantes,
mesmoqueissoaumentenossaimpedância.
9.4 Tratando 404
Naseção9.1,aprendemosaomitiroheader X-Powered-Byeamascará-
loseassimdesejássemos. Aideiaeranãodeixarqueterceirossoubessema
tecnologiautilizadapelanossaaplicação,evitandoquevulnerabilidadeses-
pecíficasdatecnologiafossemexploradas.
Masseráqueaindaestamosdandoalgumapistadatecnologiautilizada?
Vamosexperimentaracessarumapáginaquenãoexiste:
http://localhost:3000/pagina-que-nao-existe
Vocêreceberácomorespostaaseguintemensagem:
Cannot GET /pagina-que-nao-existe
AmensagemépadrãodoExpress,dessaforma,informandoparaalguém
maisatentoqueestamosutilizandoesteframework.
Podemosresolverissofacilmentecriandoumarotacomoidentificador *,
ativadoparaqualquerendere ço,atéaquelesquenãotiveremumarotaequiv-
alente.Porém,eledevevirobrigatoriamentecomoúltimarotadaaplicaç ão,
dandochanceparaqueoutrassejamprocessadas.
Vamoseditaroarquivo config/express.jsadicionandoarotaime-
diatamenteabaixodachamadado express-load:
// código anterior omitido
load('models', {cwd: 'app'})
.then('controllers')
.then('routes/auth.js')
.then('routes')
.into(app);
// se nenhum rota atender, direciona para página 404
app.get('*' , function(req, res) {
220

## Página 233

CasadoCódigo Capítulo9. Tornandosuaaplicaçãoaindamaissegura
res.status(404).render('404');
});
// código posterior omitido
Vocêdeveseperguntaroporquêdeelanãoestaremumarquivoemsep-
arado. Precisamosteragarantiadequeelasejaaúltimarotaprocessadae
teremosessacertezacolocando-aimediatamenteapósocarregamentodero-
tascom express-load.
Reparequeadicionamosostatus 404edepoisrenderizamosaview404.
Utilizamosumaview ejsparaevitarqueapáginasejachamadapublica-
mente,ouseja,eladeveserchamadaapenasatravésdenossarotacasoa
URLacessadanãosejaencontradaemnossoservidor.Precisamoscriá-laem
app/views/404.ejs:
<!doctype html>
<html>
<head>
<title>Página não encontrada</title>
<meta name="viewport" content="width=device-width">
<meta charset="UTF-8">
<link rel="stylesheet"
href="vendor/bootstrap/dist/css/bootstrap.css">
<link rel="stylesheet"
href="vendor/bootstrap/dist/css/bootstrap-theme.css">
</head>
<body>
<div class="container">
<div class="jumbotron">
<h1>Página não encontrada!<h1>
</div>
<h2 class="text-center">
<a href="/">Voltar para a página principal</a>
</h2>
</div>
</body>
</html>
221

## Página 234

9.4. Tratando404 CasadoCódigo
Fig.9.1:Páginanãoencontrada
Reinicieoservidoreexperimenteacessarumapáginaquenãoexisteeveja
oresultado.Alémdenãodarmosumapistadequaltecnologiautilizamosno
servidor,melhoramosaexperiênciadousuário.
Aintençãodestecapítulonãofoicobrirtodososaspectosdeseguran ça
deumaaplicação,maspequenasalteraçõescomgrandeimpacto.
Nossopróximopassoseráotimizarnossaaplicaç ãoparaqueousuário
possateramelhorexperiênciapossível,porémnãofaremosissomanual-
mente.Utilizaremosum task runnerqueautomatizarágrandepartedenossa
tarefa.
222

## Página 235

Capítulo10
Grunt:automaçãodetarefas
front-end
“Qualquer coisa boa que construamos acaba por nos construir”
–JimRohn
Emalgummomentoemsuacarreiradedesenvolvedorvocêjádeveter
executadoumasériedetarefasmesmocomoprojetopronto,comoempacotá-
loparadepoisenviá-loviaftp.
Porexemplo,sevocêéumdesenvolvedorfront-endjádevetersepreocu-
padoemminificareconcatenarseusscripts,inclusivejádeveterexperimen-
tadoousodealgumpré-processadorcomo LESS.
Aqualidadeequantidadedepassosvariamdeacordocomasnecessi-
dadesdoseuprojetoeessasnecessidadesacabamgerandoumfluxo(work-

## Página 236

10.1. Bem-vindoaoGrunt CasadoCódigo
flow)identificávelequemuitasvezesédocumentadoparaserusadoportoda
aequipe.
Oproblemaéquetudoqueéfeitopeloserhumanoestásujeitoaerro.Por
maisquetenhamosummanualnosdizendooquefazer,nadanosimpedede
pularmosumdospassos,oquepodeafetardiretamenteoresultadofinal.
10.1 Bem-vindo ao Grunt
Parasolucionarproblemascomoesse,foramcriadasnomercadoferramentas
deconstrução(build)deprojetoscomoAnt,GradleeMaven,masháumaque
nasceuvoltadaespecialmenteparaprogramadoresfront-end:o Grunt.
OGruntéum task runner totalmentefeitoemJavaScript tornando-
oatrativonomundofront-end,inclusiveelepossuiumacervocommaisde
2.000pluginssuportandoasmaisdiversasfuncionalidades.
Instalação
OGruntnadamaisédoqueummódulodoNode.jsinstaladoatravésdo
npm:
npm install grunt@0.4 --save-dev
Repare que no comando anterior usamos--save-dev diferente
do que estávamos acostumados a fazer. A diferença é que dentro
do arquivo package.json o módulo será incluído dentro da chave
devDependencies. Énestachavequeindicamosasdependênciasquesó
fazemsentidonoambientededesenvolvimentoenãodeproduç ão.
grunt-cli
ParaoGruntfuncionaraindaprecisamosinstalarseuclienteemlinhade
comando,o grunt-cli:
npm install -g grunt-cli@0.1
Éimportantequevocêtenhapermissãodeadministradorjáqueestamos
instalandoomóduloglobalmenteatravésdoparâmetro -g .Estemódulo
nospermitechamarocomando gruntemqualquerlocalemnossoterminal.
224

## Página 237

CasadoCódigo Capítulo10. Grunt:automaçãodetarefasfront-end
Reparequenãousamosoparâmetro --save-dev .Nãonosimporta
qualversãodoclientedelinhadecomandoestamosusando,apenasaversão
doGruntdoprojeto.
InstalaroGruntporprojetopermitesuaatualizaç ãosemafetarosdemais
projetos,algoquenãoseriapossívelsefosseinstaladoglobalmente.
10.2 O arquivoGruntfile.js
Oarquivo Gruntfile.jséondeconfiguramostarefas(tasks). Nele,cri-
amosummódulodoNode.jsqueesperarecebercomoparâmetroumain-
stânciadoGrunt.
// contatooh/Gruntfile.js
module.exports = function(grunt) {
};
Masquemchamaráessafun çãopassandoestareferência?
Ocomandogrunt
Issoéfeitoatravésdocomando gruntnoterminal.Estecomandocar-
regaránosso Gruntfile.jspassandoparaomóduloumainstânciado
Grunt.
Antesdepensarmosemqualquertarefa,precisamosgarantirquetodas
elassejamaplicadasemumacópiadapasta contatoohdenossoprojeto,
garantindoaintegridadedosarquivosoriginais.
PoderíamosatétentarfazerissousandooscomandospadrõesdoGrunt,
ainda assim, precisaríamos varrer recursivamente a pasta que desejamos
copiareexecutarumasériedecomandosfragmentados.
Paraestatarefa,tãocorriqueira,podemosusarumplugindoGruntque
tambéméummódulodoNode.js.
225

## Página 238

10.3. Instalandonossoprimeiroplugin CasadoCódigo
10.3 Instalando nosso primeiro plugin
OprimeiroplugindoGruntqueutilizaremosseráo grunt-contrib-copy
(https://github.com/gruntjs/grunt-contrib-copy):
npm install grunt-contrib-copy@0.7 --save-dev
Pronto,masissoaindanãoésuficiente.Apesardeeletercriadoapasta
grunt-contrib-copydentroda node_modules,eleaindanãoéenxer-
gadopeloGrunt;precisamoscarregá-lo.OcarregamentodepluginsdoGrunt
éfeitono Gruntfile.jsatravésdafunção grunt.loadNpmTasks:
/* recebe o objeto grunt como parâmetro*/
module.exports = function(grunt) {
grunt.loadNpmTasks('grunt-contrib-copy');
};
Agora que entendemos a estrutura básica doGruntFile.js, pre-
cisamosconfigurarnossastarefas.
10.4 Tarefas
Plugins no Grunt são configurados através da fun ção
grunt.initConfig({ }):
module.exports = function(grunt) {
grunt.initConfig({
tarefa1: {
/* configurações da tarefa1 */
},
tarefa2: {
/* configurações do tarefa2 */
}
});
grunt.loadNpmTasks('grunt-contrib-copy');
};
226

## Página 239

CasadoCódigo Capítulo10. Grunt:automaçãodetarefasfront-end
Repare que a função grunt.initConfig recebe como parâmetro
um objeto JavaScript. Esse objeto tem como propriedades os nomes
das tasks que desejamos configurar. Sabemos pela documentação do
grunt-contrib-copyqueapropriedadequerepresentaataskdesteplugin
écopy.Assim,temos:
module.exports = function(grunt) {
grunt.initConfig({
copy: {} /* configurações da tarefa */
});
grunt.loadNpmTasks('grunt-contrib-copy');
};
Umatarefapodetersubtarefas,porémnadocumentaç ãodoGruntsão
chamadasde targets(alvos).Veremosaseguircomodefiniralvosdetarefas.
10.5 Targets
CadatarefadoGruntpodeconteralvos(targets)diferentes,quepodemser
entendidoscomosubtarefas. Porexemplo,podemosquerercopiarapasta
contatoohinteiraouapenasapasta contatooh/public:
grunt.initConfig({
copy: {
aplicacaoInteira: {/* copia a pasta contatooh */},
apenasPublic: {/* copia apenas a pasta contatooh/public */}
}
});
Noexemploanterior,nãoconfiguramosostargetsdatask copy,masse
jáestivessemcriados,poderíamosexecutarnoterminal:
grunt copy
O comando anterior executaria a task copy e seus targets
aplicacaoInteira e apenasPublic. Mas e se quiséssemos rodar
227

## Página 240

10.5. Targets CasadoCódigo
apenasumtargetespecífico?Podemosqualificarataskindicandoqualtarget
queremosexecutar:
grunt copy:aplicacaoInteira
Agoraqueentendemosomecanismodetasketarget,configuraremos
nossatask copy:
// contatooh/Gruntfile.js
module.exports = function(grunt) {
grunt.initConfig({
copy: {
project: {
expand: true,
cwd: '.',
src: ['**', '!Gruntfile.js', '!package.json',
'!public/bower.json'],
dest: 'dist'
}
}
});
grunt.loadNpmTasks('grunt-contrib-copy');
};
Vamosentenderosparâmetrosdatask copy:
•expand: quando trueativaomapeamentodinâmico. Nolugarde
definirmosonomedecadaarquivoeseudestino,indicamosodiretório
detrabalho( cwd),aorigem( src)eodestino( desc).
•cwd:diretóriopadrão(current work directory )noqualasdemaispro-
priedadessebasearão. Emnossocaso,queremosaprópriapastaque
contémnossoscriptGrunt,porissoutilizamos ‘.’.
•src:arraycomosarquivosquedevemsercopiados.Usamoso globbing
pattern‘**’paracopiartodososarquivosediretórios. Desconsider-
amosalgunsarquivosadicionandooprefixo !emcadaumdeles.
228

## Página 241

CasadoCódigo Capítulo10. Grunt:automaçãodetarefasfront-end
•dest:pastadedestino.Emnossocaso,apasta dist,queécriadacaso
nãoexista.
Agoraquetemostudoconfigurado,jápodemosrodaratask copyatravés
doGrunt:
$ grunt copy
Running "copy:project" (copy) task
Created 756 directories, copied 2875 files
Done, without errors.
Apasta distfoicriada,sendoumaréplicadapasta contatooh.
10.6 Atalho para tarefas
Tudofunciona,masimagineoseguintecenário: alguémapagoualgumar-
quivodoprojeto.Nossacópiaprecisarefletiroprojeto,logo,rodamosnova-
menteocomando grunt copy.Oproblemaéqueeleconteráoarquivoque
foiapagadodoprojetooriginaleissoéumproblema.
Ataskclean
Precisamosapagarapasta distantesderodarmosnovamentenossatask
copy. Paraisso,existeoplugin grunt-contrib-clean(https://github.com/
gruntjs/grunt-contrib-clean).Suainstalaçãoéfeitaatravésdocomando:
npm install grunt-contrib-clean@0.6 --save-dev
Nãopodemosnosesquecerderegistrá-loemnossoarquivo:
grunt.loadNpmTasks('grunt-contrib-clean');
E,porfim,configuraratask:
module.exports = function(grunt) {
grunt.initConfig({
copy: {
project: {
229

## Página 242

10.6. Atalhoparatarefas CasadoCódigo
expand: true,
cwd: '.',
src: ['**', '!Gruntfile.js', '!package.json',
'!public/bower.json'],
dest: 'dist'
}
},
clean: {
dist: {
src: 'dist'
}
}
});
grunt.loadNpmTasks('grunt-contrib-copy');
grunt.loadNpmTasks('grunt-contrib-clean');
};
Usamos cleanporqueesteéonomedataskfornecidoporsuadocu-
mentação.Escolhemosonome distcomoseutargetparadeixarclaroque
eleoperarásobreapasta dist,porémoquerealmentedefinequalpastaserá
apagadaéoobjetoqueotargetrecebecomoparâmetro.Esteobjetocontém
achave src.Nela,definimosodiretórioqueseráapagado.Testandoatask
clean:
$ grunt clean
Running "clean:dist" (clean) task
Cleaning dist...OK
Done, without errors.
Agoraésótorcerparanãoesquecermosdeexecutarastasksnaordem
correta:
grunt clean
grunt copy
Vocêaindapodeexecutarasduasdeumavez:
grunt clean copy
230

## Página 243

CasadoCódigo Capítulo10. Grunt:automaçãodetarefasfront-end
Queremosautomatizarnossastarefas,etermosquenoslembrardeexe-
cutarambasemordemnãosecoadunacomnossoobjetivo.
Pararesolverproblemascomoesse,oGruntpermiteregistrarnovastasks
quefuncionamcomoumaespéciedeatalho.Quandoelaforchamada,auto-
maticamenteoutrastasksserãochamadasnasequênciaquedefinirmos.Faze-
mosissoatravésdafun ção grunt.registerTask:
grunt.registerTask('dist', ['clean', 'copy']);
Reparequeessafun çãorecebecomoprimeiroparâmetroonomedanossa
task.OsegundoéumarraycomonomedastasksjáconfiguradaspeloGrunt.
Aordeméimportante,poisaprimeiraseráexecutadaantesdasegundaepor
aívai.Nossoscriptfinalfica:
module.exports = function(grunt) {
grunt.initConfig({
copy: {
project: {
expand: true,
cwd: '.',
src: ['**', '!Gruntfile.js', '!package.json',
'!public/bower.json'],
dest: 'dist'
}
},
clean: {
dist: {
src: 'dist'
}
}
});
grunt.registerTask('dist', ['clean', 'copy']);
grunt.loadNpmTasks('grunt-contrib-copy');
grunt.loadNpmTasks('grunt-contrib-clean');
};
231

## Página 244

10.6. Atalhoparatarefas CasadoCódigo
Agorabastaexecutarmosnoterminal:
$ grunt dist
Running "clean:dist" (clean) task
Running "copy:project" (copy) task
Created 756 directories, copied 2875 files
Done, without errors.
OGruntaindapermiteregistrarmosatask default. Elaseráexecu-
tadaquandoexecutarmosocomando gruntsemparâmetros.Modificando
nossoscript:
module.exports = function(grunt) {
grunt.initConfig({
copy: {
project: {
expand: true,
cwd: '.',
src: ['**', '!Gruntfile.js', '!package.json',
'!public/bower.json'],
dest: 'dist'
}
},
clean: {
dist: {
src: 'dist'
}
}
});
grunt.registerTask('default', ['dist']);
grunt.registerTask('dist', ['clean', 'copy']);
grunt.loadNpmTasks('grunt-contrib-copy');
grunt.loadNpmTasks('grunt-contrib-clean');
};
Bastaexecutarnoterminal:
232

## Página 245

CasadoCódigo Capítulo10. Grunt:automaçãodetarefasfront-end
$ grunt
Running "clean:dist" (clean) task
Cleaning dist...OK
Running "copy:public" (copy) task
Created 4 directories, copied 5 files
Done, without errors.
AgoraqueaprendemosobásicodoGrunt,jápodemosautomatizartare-
fasquepodemmelhoraraperformancedenossaaplicaç ão.
10.7 As técnicas de minificação e concatenação
Umapráticamuitocomumemaplicaçõeswebéaconcatenaçãoeminificação
dearquivos .csse .js.
Atécnicadeconcatenação
Atécnicadeconcatenaçãojuntaarquivos .cssemumúnicoarquivo,a
mesmacoisacomarquivos .js.Avantagemdissoéqueestaremosdimin-
uindoonúmeroderequisiçõesdebuscaaessesrecursosaocarregarmos
apágina. Quantomenoronúmeroderequisições,maisrapidamentesua
páginaserácarregada,aindamaissevocêestiveremumarededotipo3G
ondealatênciadomina.
Atécnicademinificação
Aminificaçãonãovisaatacaralatência,masalarguradebanda. Nela,
tantonosarquivos .cssquantonos .jsremovemosquebrasdelinhaes-
crevendotudoemumaúnicalinha!Comisso,conseguimoseconomizaral-
gunsbytesque,nosomatóriofinal,conseguemreduziraproximadamente10%
dotamanhooriginaldoarquivo. Porém,osarquivos .jsaindapermitem
renomearonomedefun çõeseseusparâmetrosparaamenorquantidade
possíveldecaracteres. Comcerteza,ocódigoficaráilegível,mascarregará
maisrápidonapáginadousuário.
233

## Página 246

10.8. grunt-usemin:minificaçãoeconcatenaçãocomGrunt CasadoCódigo
Nuncaaltereosarquivosoriginais!
Umpontoimportanteéquetantoaconcatenaç ãoquantoaminificação
nãodevemserfeitasnosarquivosoriginaisdoprojeto, casocontrário, a
manutençãodosistemasetornaráimpossível.Precisamosrealizaressepro-
cessoantesdodeploydaaplicação,istoé,antesdeelaentrarnoar.
Imaginerealizarconcatenaçãoeminificaçãomanualmentetodavezque
algumacoisamudaremnossosistema? Jáseimaginouconcatenandoar-
quivos csseaindaalterandoapágina index.ejsparaapontarparaoar-
quivoconcatenado? Impraticável,não? ÉporissoqueoGruntpossuiuma
sériedepluginsquepodemnosajudaraautomatizaressatarefa.
10.8 grunt-usemin: minificação e concatenação
com Grunt
Minificaçãoemergedearquivos .jse .csscomcertezasãoalgumasdas
tarefasmaisexecutadasnoGrunt.Porém,nãosãotarefasqueestãoprontas
porpadrão.Precisamosinstalaralgunsplugins.Ospluginsenvolvidosnestas
tarefassão:
•grunt-contrib-concat: https://github.com/gruntjs/
grunt-contrib-concatconcatenaarquivos .csse .js.
•grunt-contrib-uglify: https://github.com/gruntjs/
grunt-contrib-uglifyminificaarquivos .js.
•grunt-contrib-cssmin: https://github.com/gruntjs/
grunt-contrib-cssmin)minificaarquivos .css.
Comotodoplugin,precisamosinstalarcadaumdelesatravésdo npm:
npm install grunt-contrib-concat@0.5 grunt-contrib-uglify@0.6
grunt-contrib-cssmin@0.10 --save-dev
E carregá-los no Gruntfile.js através da fun ção
grunt.loadNpmTasks:
234

## Página 247

CasadoCódigo Capítulo10. Grunt:automaçãodetarefasfront-end
// contatooh/Gruntfile.js
// código anterior omitido
grunt.loadNpmTasks('grunt-contrib-concat');
grunt.loadNpmTasks('grunt-contrib-uglify');
grunt.loadNpmTasks('grunt-contrib-cssmin');
Oproblemaéqueseremosresponsáveispelaconfiguraç ãodastasksde
cadaumdeles. Podemosgerarautomaticamenteasconfiguraçõesdastasks
atravésdo grunt-usemin.
grunt-usemin
O grunt-usemin(https://github.com/yeoman/grunt-usemin)analisa
nossapáginaHTMLembuscademetadadose,apartirdasinformaçõesco-
letadas,geraconfiguraçõesparaastasksenvolvidasnoprocessodeconcate-
naçãoeminificação.Primeiro,precisamosinstalá-lo:
npm install grunt-usemin@2.6 --save-dev
Logoemseguida,devemoscarregá-loemnosso Grunfile.js:
// contatooh/Gruntfile.js
// código anterior omitido
grunt.loadNpmTasks('grunt-usemin');
Antes de configurarmos a task, precisamos adicionar metadados em
nossapágina index.ejs.
Adicionandometadadosatravésdecomentários
O grunt-useminfuncionadaseguintemaneira. Emnossaspáginas,
envolvemosemumcomentárioespecialarquivos .csseJavascriptquede-
sejamosconcatenareminificar:
<!-- build:TIPO RESULTADO -->
<!-- endbuild -->
235

## Página 248

10.8. grunt-usemin:minificaçãoeconcatenaçãocomGrunt CasadoCódigo
O TIPO aceita dois valores: css e js. RESULTADO é o ar-
quivogeradoesualocalizaçãoésemprerelativaàpágina.Emnossapágina
app/views/index.ejs,convencionaremosqueoresultadodaconcate-
naçãoeminificaçãodearquivosCSSdapáginaserá css/index.min.css,
edosarquivosJavaScript, js/index.min.js. Alterandonossapágina
index.ejs,temos:
<!-- build:css css/index.min.css -->
<link rel="stylesheet"
href="vendor/bootstrap/dist/css/bootstrap.css">
<link rel="stylesheet"
href="vendor/bootstrap/dist/css/bootstrap-theme.
css">
<!-- endbuild -->
<!-- build:js js/index.min.js -->
<script src="vendor/angular/angular.js"></script>
<script src="vendor/angular-route/angular-route.js"></script>
<script src="vendor/angular-resource/angular-resource.js">
</script>
<script src="vendor/angular-i18n/angular-locale_pt-br.js">
</script>
<script src="js/main.js"></script>
<script src="js/controllers/ContatosController.js"></script>
<script src="js/controllers/ContatoController.js"></script>
<script src="js/services/ContatoService.js"></script>
<!-- endbuild -->
Não podemos nos esquecer das páginasauth.ejs e 404.ejs.
Primeiro,vamosalterar auth.ejs:
<!-- build:css css/auth.min.css -->
<link rel="stylesheet"
href="vendor/bootstrap/dist/css/bootstrap.css">
<link rel="stylesheet"
href="vendor/bootstrap/dist/css/bootstrap-theme.css">
<!-- endbuild -->
Porfim, 404.ejs:
236

## Página 249

CasadoCódigo Capítulo10. Grunt:automaçãodetarefasfront-end
<!-- build:css css/404.min.css -->
<link rel="stylesheet"
href="vendor/bootstrap/dist/css/bootstrap.css">
<link rel="stylesheet"
href="vendor/bootstrap/dist/css/bootstrap-theme.css">
<!-- endbuild -->
Excelente! Agora,sónosrestaconfiguraro grunt-useminemnosso
GruntFile.js.
10.9 As tasks usemin e useminP repare
Para que a mágica dogrunt-usemin aconteça, precisamos config-
urar duas tasks distintas. A primeira se chama useminPrepare.
Ela gerará configurações dinâmicas paragrunt-contrib-concat,
grunt-contrib-uglify, grunt-contrib-cssmin, livrando-nos de
configurá-losemnosso Gruntfile.js.
Asegundatasksechama usemin.ElaalteraránossosarquivosHTML
fazendocomqueelesapontemparaosarquivosconcatenadoseminifica-
dosdefinidosnoscomentáriosespeciais,poisforamcriadosantespelatask
useminPrepare.
Nãosepreocupe,asduastaskssãotãosimplesquantoasquevimosante-
riormente:
usemin : {
html: 'dist/app/views/**/*.ejs'
},
useminPrepare: {
html: 'dist/app/views/**/*.ejs'
}
Repare que ambas recebem como parâmetro um objeto que con-
tém a chavehtml. É nele que indicamos quais páginas serão pro-
cessadas; em nosso caso, todas as que estiverem dentro da pasta
contatooh/dist/app/views/, evitando que as views originais em
contatooh/app/viewssejammodificadas.Porém,temosumproblema.
237

## Página 250

10.9. AstasksusemineuseminPrepare CasadoCódigo
Vocêlembraqueosarquivosdefinidosnosmetadadosdapáginasãocri-
adosrelativamenteàlocalizaçãodapágina?Issofarácomquesejamcriados
indevidamenteem contatooh/dist/app/views. Comoelesnãoestão
dentrodapáginapública,apáginacarregadanonavegadornãoconseguirá
baixá-los.
Podemos resolver isso indicando para a taskuseminPrepare,
aquela que cria nossos arquivos, que crie os arquivos dentro da pasta
contatooh/dist/public,passandoumtargetque,naverdade,agecomo
umobjetodeconfiguraçãointernadatask:
usemin : {
html: 'dist/app/views/**/*.ejs'
},
useminPrepare: {
options: {
root: 'dist/public',
dest: 'dist/public'
},
html: 'dist/app/views/**/*.ejs'
}
É importante frisar que não escolhemos qualquer nome para a task
options. VáriospluginsdoGruntutilizamessaconven çãoquandoquer-
emosalteraralgumaconfiguraçãopadrãodatask.Nela,passamosumobjeto
comaschaves roote destquepossuemcomovalorolocalondequeremos
queosarquivossejamgravados,emnossocaso, dist/public.
Regitrandotaskdeatalho
Paraquepossamosconcluirnossoscript,precisamosgarantiraexecuç ão
ordenadadasseguintestasks:
1) useminPrepare: lêosmetadadosdaspáginasecriaasconfigurações
paraastasks concat, uglifye cssmin.
2) concat:concatenaosarquivos .jse .cssutilizandocomonomedo
arquivoaconfiguraçãogeradapor useminPrepare.
238

## Página 251

CasadoCódigo Capítulo10. Grunt:automaçãodetarefasfront-end
3) uglify: minifica scripts com base na configuração gerada por
useminPrepare.
4) cssmin: minifica arquivos css com base na configuração gerada por
useminPrepare.
5) usemin:porfim,alteraoHTMLparaqueaponteparaosarquivoscon-
catenadoseminificados.
Paraisso,criaremosumatalhoparatodaselaschamado minifica:
grunt.registerTask('minifica', ['useminPrepare', 'concat' ,
'uglify', 'cssmin', 'usemin']);
Porúltimo,faremoscomquenossatask default,alémdecriarumacópia
doprojeto,chameautomaticamentenossatask:
grunt.registerTask('default', ['dist', 'minifica']);
Nossoscriptfinaldeveráestarassim:
module.exports = function(grunt) {
grunt.initConfig({
copy: {
project: {
expand: true,
cwd: '.',
src: ['**', '!Gruntfile.js', '!package.json',
'!public/bower.json'],
dest: 'dist'
}
},
clean: {
dist: {
src: 'dist'
}
},
usemin : {
239

## Página 252

10.9. AstasksusemineuseminPrepare CasadoCódigo
html: 'dist/app/views/**/*.ejs'
},
useminPrepare: {
options: {
root: 'dist/public',
dest: 'dist/public'
},
html: 'dist/app/views/**/*.ejs'
}
});
grunt.registerTask('default', ['dist', 'minifica']);
grunt.registerTask('dist', ['clean', 'copy']);
grunt.registerTask('minifica', ['useminPrepare', 'concat',
'uglify', 'cssmin', 'usemin']);
grunt.loadNpmTasks('grunt-contrib-copy');
grunt.loadNpmTasks('grunt-contrib-clean');
grunt.loadNpmTasks('grunt-contrib-concat');
grunt.loadNpmTasks('grunt-contrib-uglify');
grunt.loadNpmTasks('grunt-contrib-cssmin');
grunt.loadNpmTasks('grunt-usemin');
};
Vamosrealizarumtestecompleto. Rodenossatask defaultedepois
subaoprojetodentrodapasta contatooh/dist.Seoseuscriptestivercor-
reto,seráexibidaumasériedeinformaçõesnoterminal,inclusiveosparâmet-
rosdeconfiguraçãogeradospelo grunt-usemin.
Editeapágina contatooh/dist/app/views/index.ejseverifique
se a taskuseminconseguiu realizar a substituição das tags e se foram
geradososarquivos contatooh/dist/public/css/index.min.csse
contatooh/dist/public/js/index.min.css. Visualizecadaumde-
les.Sevocênãoconseguirentenderoqueelesexibeméumindíciodequeo
processodeminificaçãofuncionou.
Masseráquenossosistemaaindafuncionadepoisdetantaalteraç ão?En-
trenapasta contatoo/distesubanossoservidor:
240

## Página 253

CasadoCódigo Capítulo10. Grunt:automaçãodetarefasfront-end
node server
Autentique-selogoemseguida. Tudofunciona? Não! Assimquenos
autenticamos,nadaéexibidononavegador.Porquê?Seabrirmosoconsole
donavegador,veremosamensagemdeerro:
Uncaught Error: [$injector:modulerr] Failed to instantiate
module contatooh due to:
Error: [$injector:unpr] Unknown provider: a
Oproblemaéqueoprocessodeminificaçãodescriptsalterouonomedos
parâmetrosdeváriasfunções.Comoosistemadeinje çãodedependênciasdo
AngularJSbaseia-senonomesdosparâmetros,tudodeixoudefuncionar.
Temos duas saídas. Podemos anotar nossas dependências,
algo que deixará nosso código mais verboso. Por exemplo, nosso
ContatoControllerficariaassim:
angular.module('contatooh').controller('ContatoController',
['$scope', '$routeParams', 'Contato',
function($scope, $routeParams, Contato) {
// código do controller
}]);
Reparequesubstituímososegundoparâmetrodafun ção controller
porumarray.Nestearray,ostrêsprimeirosvaloresequivalemaosparâmetros
dafunção,últimoparâmetropassado.Porém,comosãodados,nãoserãoal-
teradosduranteoprocessodeminificaç ão. OAngularJSpassaasebasear
nessesdadosparasaberqualartefatosinjetardentrodafun ção. Pormais
queseusparâmetrossejamtrocadospeloprocessodeminificaç ão,teremos
acertezadequeoprocessodeinje çãofuncionarácomoesperado.
Outrasoluçãoédeixarocódigodojeitoqueestáeautomatizaressatarefa
paraserexecutadadentrodapasta contatooh/dist.Éoqueveremosna
próximaseção.
10.10 Angular e minificação
Ogrunt-ng-annotate(https://github.com/mzgol/grunt-ng-annotate)éum
plugindoGruntcapazdeanotarinje çõesdedependênciadoAngularJSem
241

## Página 254

10.10. Angulareminificação CasadoCódigo
nossocódigoautomaticamente.Suainstalaçãoéfeitavia npm:
npm install grunt-ng-annotate@0.5 --save-dev
Atask ngAnnotatealteranossosarquivosadicionandoasintaxeque
vimosnase çãoanteriorepreparandonossosarquivosparaoprocessode
minificação.Vamosconfigurá-laeregistrá-laemnosso Gruntfile.js:
// contatooh/Gruntfile.js
// código anterior omitido
ngAnnotate: {
scripts: {
expand: true,
src: ['dist/public/js/**/*.js']
},
}
// código posterior omitido
grunt.loadNpmTasks('grunt-ng-annotate');
Nãoesque çadeadicionaratasknalistadedanossatask minifica,mas
antesde uglify:
grunt.registerTask('minifica', ['useminPrepare', 'ngAnnotate',
'concat', 'uglify', 'cssmin', 'usemin']);
Pronto!Rodeocomando gruntnoterminal.Noconsole,seráexibidaa
mensagem:
Running "ngAnnotate:scripts" (ngAnnotate) task
>> 4 files successfully generated.
Porfim,experimenteentrarnapasta contatooh/distesubiraapli-
cação.Tudodevecontinuarfuncionando.
242

## Página 255

Capítulo11
Testandoaaplicação
“ A beleza das coisas existe no espírito de quem as contempla. ”
–DavidHume
Umaferramentadetestedecódigoéumprogramaqueutilizanosso
códigoecomparaoresultadodeumaexecuç ãocomumvalor,ouestadode
umobjeto,queesperamosquesejadevolvidooualterado.
Muitaslinguagensdeprogramaçãocontamcomferramentasqueauxil-
iamesteprocesso. UmadasferramentasparatestedeJavaScriptmaispop-
ularesdomercadoéo Jasmine. Estaferramentapodeserusadatantopara
testesdeunidadequantoparatestesdepontaaponta:
•Testedeunidade:noinglês, unit testing. Focaemumacoisaapenas,
porexemplo,umcontrollerdenossosistema.Nãohádependênciaex-
ternacomooacessoabancodedadosouserviços.

## Página 256

11.1. Karma:feedbackinstantâneodetestesdeunidade CasadoCódigo
•Testedepontaaponta:noinglês, end-to-end testing (e2e).Testaseo
fluxodorequisitodeumaaplicaçãodopontodevistadousuárioestá
funcionandocomoprojetadodoinícioaofim.
Porém,aequipedoAngularJSnãoestavasatisfeitacomotempoentre
aalteraçãodeumafuncionalidadedosistemaeaexecuç ãodeseutestede
unidade. Elesqueriamquealteraçõesfeitasemqualquerfuncionalidadedo
sistemadisparassemautomaticamenteseutestedeunidadeefornecessemum
feedbackimediatoparadesenvolvedor. Estafoiamotivaç ãodacriaçãodo
Karma.
Nãosatisfeitos,elestambémcriaramo Protractor,umaferramentaes-
pecíficaparatestes e2eemaplicaçõescomAngularJSquefacilitaenorme-
menteautilizaçãodoSelenium.Nestecapítulo,abordaremosessastecnolo-
giasecomointegrá-lasànossaaplicação.
11.1 Karma: feedback instantâneo de testes de
unidade
Karma(http://karma-runner.github.io/)éumambientedetestesfocadona
produtividadedodesenvolvedorlivrando-odeseusdetalhesdeconfiguraç ão.
Aideiaéqueodesenvolvedortenhaumfeedbackinstantâneodoresultadode
seustestesdeunidadequandoqualquerJavaScriptdaaplicaç ãoforalterado.
OKarmapossuioutrascaracterísticasqueotornamaindamaisinteressante:
•Testesemdispositivosreais:navegadorescomoChrome,Firefoxentre
outros.SuporteaoPhamtonJS(http://phantomjs.org/),umnavegador
headlessbaseadonoWebkit(https://www.webkit.org/),querodasem
interfacevisual.Tabletsesmartphonesentramnalista.
•Agnósticodoframeworkdeteste: você pode usar Jasmine (http:
//jasmine.github.io/),Mocha(http://visionmedia.github.io/mocha/),
QUnit(http://qunitjs.com/)oucriarumadapterparaseuframework
detestefavorito.
•Integração descomplicada: integração com Jenkins (http:
//jenkins-ci.org/) , Travis (https://travis-ci.org/) ou Semaphore
244

## Página 257

CasadoCódigo Capítulo11. Testandoaaplicação
(https://semaphoreapp.com/).
•Paratodos:nãoéexclusivodoAngularJS,podendoserutilizadopor
qualqueraplicaçãoquequeiraautomatizarseustesteseobterofeed-
backdeseustestesdeunidadeemtemporeal.
Instalação
OambientecriadopeloKarmarodasoboNode.jsesuainstalaç ãoéfeita
pelo npm:
npm install karma@0.12 --save-dev
Precisamostambémdeseuclientedelinhadecomandoinstaladoglobal-
mente(privilégiodeadministradornecessário)parapodermosiniciá-loem
qualquerdiretóriodenossosistemadearquivos.
npm install -g karma-cli@0.1
ComoKarmainstalado,jápodemosconfigurá-lo.
karma.config.js
ApesardeoKarmanosfornecerumambienteparaexecutarmosnossos
testesdeunidade,precisamosconfigurarseuarquivo karma.config.js.
Nele,informamosalocalizaçãodenossosscriptsebibliotecas,oframework
detesteescolhido,osnavegadoresutilizadosparatesteentreoutrasconfigu-
rações.
Nolugardecriarmosoarquivomanualmente,podemospediraoseu
assistentequecrieumparanós. Vamoscriaroarquivodentrodapasta
contatooh/config, porémrodaremosocomandodentrodapastaraiz
contatooh:
$ karma init config/karma.config.js
O sistema fará uma série de perguntas, mas apenas duas merecem
destaquenestemomento. Paraorestante,daremos ENTERatéterminaro
assistente:
245

## Página 258

11.2. Jasmine:frameworkdeteste CasadoCódigo
Which testing framework do you want to use ?
Press tab to list possible options. Enter to move to the next
question.
> jasmine
Utilizaremos o Jasmine como framework de teste, opção exibida por
padrãopeloKarma.
Do you want to capture any browsers automatically ?
Press tab to list possible options. Enter empty string to move
to the next question.
> Chrome
Precisamosindicarqualnavegadorutilizaremospararodarostestes,in-
clusivepodemosindicarmaisdeum.Emnossocaso,ficaremosapenascom
oChromeporenquanto.Maistarde,trabalharemoscomoPhamtomJS,um
browserseminterfacevisualmuitoutilizadoemservidoresdeintegraç ãocon-
tinua,assuntoqueabordaremosnopróximocapítulo.
Quandooprocessoterminar,dentrodapasta node_modulesserãoadi-
cionadososmódulos karma-jasminee karma-chrome-launcher.
OKarmadenadaservirásenãoelaborarmosnossostestesnoframework
detesteescolhido.ÉporissoqueaprenderemoscomooJasminefuncionana
próximaseção.
11.2 Jasmine: framework de teste
OJasmine(http://jasmine.github.io/)éumframeworkdetestesvoltadopara
JavaScriptquenãodependedeumnavegadorparafuncionar,muitomenos
doDOM.Elepossuiumconjuntodefun çõesquenosauxiliamnarealização
detestes.
Nosso primeiro candidato para testes será
public/js/controllers/ContatoController.js. Por convenção,
escrevemos testes em um arquivo de mesmo nome acrescido do sufixo
Spec, logo, teremos o arquivoContatoControllerSpec.js. Todos
nossos testes ficarão dentro da pastacontatooh/test/spec. Com
o arquivo contatooh/test/spec/ContatoControllerSpec.js
criado,jápodemosdarinícioànossaprimeirasuítedetestes.
246

## Página 259

CasadoCódigo Capítulo11. Testandoaaplicação
11.3 Criando suítes de testes
OJasminenospermitecriarsuítesdetestesatravésdafun ção describe
disponibilizadapelopróprioframework.Afun çãorecebedoisparâmetros:o
primeiroéadescriçãodenossasuíteeosegundoéumafun çãoqueconterá
umasériedetestesquenoJasminesãochamadosde Specs:
// contatooh/test/spec/ContatoControllerSpec.js
describe("ContatoController", function() {
});
Onomedasuíteétipicamenteonomedaclasse,fun çãooucomponente
quedesejamostestar.Éonomedasuítequeseráexibidocomoresultadode
seustestesnoterminal.Nossopróximopassoserádefiniroscomportamentos
de ContatoControllerquedesejamostestar.
CriandoSpecsatravésdafunç ãoit
Dentrodenossasuíte, criaremosumaafirmativa, nossa Spec, sobre
nossoobjeto ContatoControlleratravésdafunção it:
describe("ContatoController", function() {
it("Deve criar um Contato vazio quando
nenhum parâmetro de rota for passado", function() {
});
});
Oprimeiroparâmetro,nossaafirmação,deixaclaroparaquemestálendo
ocódigooqueestamosesperando, maséocomportamentodefinidona
funçãopassadacomosegundoparâmetroquetestaráessa expectativa.Éeste
comportamentoqueprecisamosdefinir.
247

## Página 260

11.4. RodandosuítesdetestesatravésdoKarma CasadoCódigo
Afunçãoexpect
OJasmineusaafun ção expectparatestaraexpectativadenossa Spec:
describe("ContatoController", function() {
it("Deve criar um Contato vazio quando
nenhum parâmetro de rota for passado", function() {
expect($scope.contato._id).toBeUndefined();
});
});
Repareque,nesseexemplo,afun ção expectrecebecomoparâmetroo
_iddocontatopresentenoescopode ContatoController.Emseguida,
encadeamosachamadadafun ção toBeUndefined,istoé,paraquenosso
testepasse,o _iddocontatodeveser undefined.Sabemosqueissodeve
acontecerquandonenhumparâmetroderotaforpassadoparaocontroller,
exatamenteadescriçãodafun ção it.
Paraumalistaexaustivadetodasasfun çõessuportadaspor expect,
acesseolink http://jasmine.github.io/2.0/introduction.html.
Masespereumpouco!Como $scopeapareceuemnossocódigo?Jas-
minesaberáinstanciar ContatoController?Antesdenospreocuparmos
seotestepassaráounão,queremosqueelesejaexecutadopeloKarma.
11.4 Rodando suítes de testes através do Karma
ParaqueoKarmasejacapazdeexecutarnossostestescriadospeloJasmine,
precisamoseditarseuarquivo contatooh/config/karma.config.jse
adicionarnachave filesocaminho ../test/spec/**/*Spec.js.
files: ['../test/spec/**/*Spec.js']
Descemosumnívelcom ..porqueodiretóriopadrãoqueoKarma
utilizará quando o rodarmos será o mesmo diretório de seu arquivo
248

## Página 262

11.5. Angular-mockseintegraçãocomJasmine CasadoCódigo
sChrome 37.0.2062:
Executed 1 of 1 (1 FAILED) ERROR (0.011 secs / 0.008 secs)
AsprimeirasinformaçõesdoterminaldizemrespeitoaoservidorKarma
criadoem http://localhost:9876/querodaeternamente,razãodotravamento
deseuterminal. Aindanoterminal,temosinformaçõescomoaversãodo
navegadorutilizado,entreoutras,masoquenosinteressaagoraésaberse
nossasuítedetestesfoiprocessadae,realmente,elafoi.Éfácilperceberque
suaúnica Specnãopassounoteste,poisconstaoestado FAILED.
Outropontoimportanteéo referenceError. Nele,temosamen-
sagem“$scopeisnotdefined”,ouseja,oJasminenãofoicapazderesolver
sozinhooescopodocontroladorquequeremostestare,porisso,aexce ção
invalidounossoteste.
Feedbackconstante
Precisamosfecharoterminalagora?Não!AideiaétermosoKarmaro-
dandootempotodoenquantocriamosnossostestes.Qualqueralteraç ãodos
arquivosdefinidosnachave filesde karma.config.jsdispararánovos
testesautomaticamente.Issopermitiráqueodesenvolvedorrecebaumfeed-
backomaisrápidopossívelcasoalgumtestefalhe!
Masaperguntaquevocêdeveestarfazendoé:comoconseguiremosin-
stanciar ContatoControlleremnossa Spec,umavezquenossocon-
trollersomenteécriadoatravésdoAngularJS?Arespostaestánacombinação
doJasminecomomódulo Angular-Mocks.
11.5 Angular-mocks e integração com Jasmine
ComooAngularJSutilizapesadamenteinje çãodedependências,podemos
solicitardiretamentedeseusistemadeinje çãoquaisartefatosprecisamosem
nossas Specs,tudoatravésdefun çõesespeciaisdisponibilizadaspelomó-
dulo Angular-Mocks.Tambémpodemostrocar,quandonecessário,esses
artefatosporobjetosfalsos(mocks)quemuitasvezesnosajudamnacriaç ão
denossostestes.Veremosissotudonaprática.
Instalamosomódulo angular-mocksatravésdobowerexecutandoo
comandoaseguirdentrodapasta contatooh:
250

## Página 263

CasadoCódigo Capítulo11. Testandoaaplicação
bower install angular-mocks#1.3 --save-dev
O próximo passo é fazer com que o Jasmine carregue o módulo
paraquepossamosutilizá-lo. Aproveitaremosparaadicionarocaminho
de todos os arquivos utilizados pelo projeto. Alterando nosso arquivo
contatooh/config/karma.config.js:
files: [
'../public/vendor/angular/angular.js',
'../public/vendor/angular-mocks/angular-mocks.js',
'../public/vendor/angular-resource/angular-resource.js',
'../public/vendor/angular-route/angular-route.js',
'../public/js/main.js',
'../public/js/controllers/**/*.js',
'../public/js/services/**/*.js',
'../test/spec/**/*Spec.js'
],
Alteração do karma.config.js
Todavezqueoarquivo karma.config.jsformodificado,você
precisaráreiniciaroKarma.
Excelente,agorajápodemosrefatorarnossaSpec.
Afunçãomodule
Sabemos que é através da diretivang-app da nossa página prin-
cipal que o AngularJS carrega o módulocontatooh definido no ar-
quivo contatooh/public/main.js,todaviaprecisamoscarregá-loman-
ualmente.
O Angular-Mocks possui a função module que recebe como
parâmetroonomedomóduloquequeremoscarregar.Contudo,emquelugar
denossasuítedetestescarregaremosomódulo contatooh?
251

## Página 264

11.5. Angular-mockseintegraçãocomJasmine CasadoCódigo
AfunçãobeforeEach
OJasminepossuiafun ção beforeEachsemprechamadaantesdaexe-
cuçãodecadaumadenossas Specs.Pareceserumbomlugar:
describe("ContatoController", function() {
beforeEach(function() {
module('contatooh');
});
it("Deve criar um Contato vazio quando
nenhum parâmetro de rota for passado", function() {
expect($scope.contato._id).toBeUndefined();
});
});
Carregamosatravésdafunção moduleomóduloprincipaldenossaapli-
cação,mascomoteremosacessoao ContatoControllerdentrodenossa
Spec?
Afunçãoinject
Paraquepossamosacessarcontrollersdentrodenossostestes,substi-
tuiremosocallbackdafun ção itporumachamadaàfun ção inject,
disponibilizadapelo Angular-Mocks.
describe("ContatoController", function() {
beforeEach(function() {
module('contatooh');
});
it("Deve criar um Contato vazio quando
nenhum parâmetro de rota for passado",
inject(function() {
expect($scope.contato._id).toBeUndefined();
}));
});
252

## Página 265

CasadoCódigo Capítulo11. Testandoaaplicação
Podemospediràfun ção injectqualquerartefatoinjetáveldoAngu-
larJS,masaindacontinuamoscomumproblema:controllersnãopodemser
injetados,apenasserviços.Eagora?
Oservi ço $controller
Nem tudo está perdido! O Angular-Mocks possui o serviço
$controllercomaresponsabilidadedeinstanciarcontrollers:
describe("ContatoController", function() {
beforeEach(function() {
module('contatooh');
});
it("Deve criar um Contato vazio quando
nenhum parâmetro de rota for passado",
inject(function($controller) {
$controller('ContatoController');
expect($scope.contato._id).toBeUndefined();
}));
});
Reparequeoserviço $controlleréumafunçãoconstrutoraquere-
cebecomoparâmetroonomedocontrollerquequeremosinstanciar.Exce-
lente,nossocontrollerécriadoetodasassuasdependênciassãoresolvidas
peloAngularJS,porémcaímosemumoutroproblema: $scopeéacessível
apenasdentrodocontroller!Comoreferenciá-loemnossafun ção expect?
Umasoluçãoésubstituirmoso $scopede ContatoControllerpor
umescopocriadopornós.Issopermitiráquenossareferênciatenhaacessoa
todasasinformaçõesadicionadasnoescopodocontroller,justamenteoque
precisamos.
$injectore $rootScope
Primeiro, vamos declarar uma variável chamada$scopedentro da
função describeparatorná-lavisívelemnossas Specs.Logoemseguida,
253

## Página 266

11.5. Angular-mockseintegraçãocomJasmine CasadoCódigo
vamosinicializá-lacomumcódigoespecialdentrodafun ção beforeEach
quejácriamos:
describe("ContatoController", function() {
var $scope;
beforeEach(function() {
module('contatooh');
inject(function($injector) {
$scope = $injector.get('$rootScope').$new();
});
});
it("Deve criar um Contato vazio quando
nenhum parâmetro de rota for passado",
inject(function($controller) {
$controller('ContatoController');
expect($scope.contato._id).toBeUndefined();
}));
});
Recorremosmaisumavezàfun ção inject,masnãopodemossimples-
mentesolicitarainje çãode $scopeporqueelesóéinjetadoemcontrollers.
Nãopodemosapenascriarumobjetoqualquercompapeldeescopo,poiso
escopodetodocontrollerherdade $rootScopeequivalenteaoelemento
ondecolocamosadiretiva ng-app. Éaíqueentraoserviço $injector
(nãooconfundacomafun ção inject).
Oserviço$injectorpermiteinstanciaroutrosartefatosdoAngularJS
quenãosejamserviços. Éatravésde $injector.get(‘$rootScope’)
quetemosacessoàdefiniç ãode $rootScope,masestamosinteressados
emumainstânciadestadefiniçãoquecriamosencadeandoumachamadaà
função $injector.get(‘$rootScope’).$new(). Conseguimoscriar
um $scopenovinhoemfolha!
Criamos nosso $scope, mas como o associaremos ao
ContatoControllercriadoemnossa Spec? Oserviçocontroller
254

## Página 267

CasadoCódigo Capítulo11. Testandoaaplicação
recebe,alémdonomedocontrollerquequeremosinstanciarumsegundo
parâmetro, umobjetocujachavesrepresentamosartefatosinjetadosque
desejamossubstituir.Sendoassim,temos:
describe("ContatoController", function() {
var $scope;
beforeEach(function() {
module('contatooh');
inject(function($injector) {
$scope = $injector.get('$rootScope').$new();
});
});
it("Deve criar um Contato vazio quando
nenhum parâmetro de rota for passado",
inject(function($controller) {
$controller('ContatoController',
{"$scope" : $scope});
expect($scope.contato._id).toBeUndefined();
}));
});
Pronto! Nossotesteinstanciou ContatoControllerenossafun ção
expecttemacessoaoseu $scope. Sabemosqueduranteainicialização
docontrolleréverificadosebuscamosumcontatoouinstanciamosumnovo.
Comoemnossotestenãoentramosnoméritodesteparâmetro,umnovocon-
tatoinstanciadodeveterseu _id undefined. Nãoselembradalógica?
Vocêpodeconsultá-lanaseção5.11.
Sevocênãoterminouaexecuç ãodoKarma,assimquevocêsalvaras
alteraçõesveráinstantaneamenteoresultadodotestenoterminal. Aliás,o
testedevepassar:
Chrome 37.0.2062: Executed 1 of 1 SUCCESS (0 secs / 0.035 secs)
Chrome 37.0.2062: Executed 1 of 1 SUCCESS (0.037 secs / 0.035
secs)
255

## Página 268

11.6. $httpBackend:“mockando”nossobackend CasadoCódigo
Agoraquenossaprimeira Specpassou,jápodemosirumpoucoalém
criandoumtestemaissofisticadonapróximase ção.
11.6 $httpB ackend:“mockando”nosso backend
Naseçãoanterior,aprendemosainstanciarumcontrolleremnossostestes,
inclusivecriamoseassociamosumescopoaele. Esteescopofoiutilizado
pelafunção expecdoJasmineparatestarnossaexpectativadoquedeveria
acontecer.
Criaremosumanova Specatravésdeoutrachamadaàfun ção it.Essa
Specverificaráacondiçãocontráriada Specquecriamos: deve preencher o
Contato quando parâmetro de rota for passado.
Destavez,quandoinstanciarmos ContatoController,alémdepas-
sarmosoescopoquecriamosparaocontroller,passamosumobjetoquerep-
resentaránosso $routeParams,aqueleartefatodoAngularJSqueconsul-
tamosemnossocontrollerparasabersealgumparâmetrofoipassado. A
diferençaéqueestipularemosovalor 1paraele.
describe("ContatoController", function() {
var $scope
// código anterior omitido
it("Deve preencher o Contato quando
parâmetro de rota for passado",
inject(function($controller) {
$controller('ContatoController', {
'$routeParams': {contatoId: 1},
'$scope': $scope
});
expect($scope.contato._id).toBeDefined();
}));
});
Assimquevocêsalvar, veránoterminal(sevocênãotiverfechadoo
Karma)quenossotestenãopassa.Recebemosaexce ção:
"TypeError: Cannot read property '_id' of undefined"
256

## Página 269

CasadoCódigo Capítulo11. Testandoaaplicação
Issoaconteceporque,quandopassamoso contatoId,nossocontroller
tentarárecuperarocontatoatravésdeumarequisiçãoparanossoRESTEnd-
point. Comonãoestamosrodandonossoservidor,ocallbackdeerrode
ContatoControllerseráchamado, destamaneira, $scope.contato
seráundefined.Reparequeoimportanteaquiétestarsenossalógicafun-
ciona,nãorealizarumaconexãorealcomobanco.
Para resolver problemas como esse, oAngular-Mocks possui o
$httpBackendparamockarmosnossoback-end. Issomesmo! Podemos
simulararespostaparaqualquerumdenossosRESTEndpoints. Aideia
éretornarmosumcontatocom _idigualaoqueestipulamosemnosso
$routeParams.
DefinindoasrespostasdenossosEndpoints
Precisamospedirumainstânciade $httpBackEndatravésdafunção
inject.Faremosissodentrodafun ção beforeEachdoJasmine:
describe("ContatoController", function() {
var $scope, $httpBackend;
beforeEach(function() {
module('contatooh');
inject(function($injector, _$httpBackend_){
$scope = $injector.get('$rootScope').$new();
$httpBackend = _$httpBackend_;
});
});
});
Declaramosavariável $httpBackend,queseráacessíveldentrodenos-
sas Specs,porémvocêdeveterreparadoque,dentrodafun ção inject,
injetamososerviço _$httpBackend_. Usamos underlinenonomedo
serviçoparadiferenciá-lodavariável$httpBackend.Internamente,osis-
temadeinje çãoremoveráos underlinesparaquenossocódigofuncione.Se
nãotivéssemosfeitoisso,teríamosproblemasemassociaro $httpBackend
recebidocomoparâmetrocomavariáveldeclaradademesmonome.
Aperguntaquevocêdeveestarsefazendoéomotivodenãotermosado-
257

## Página 270

11.6. $httpBackend:“mockando”nossobackend CasadoCódigo
tadooutronomedevariávelnolugarde $httpBackend,removendoassim
anecessidadedos underlinesdoparâmetroinjetado.Arazãoésimples:quer-
emosusarosmesmosnomesdosartefatosdoAngularJSemnossostestes.
Foiporissoquedeclaramosnotesteanterior $scopecomovariávelquear-
mazenaoescopodocontrollerenãooutronome.
Agora já podemos preparar as respostas paraquando a rota
/contato/1foracessada.
$httpBackend.when
Preparamos as respostas de nossos EndPoints através da função
$httBackend.when:
describe("ContatoController", function() {
var $scope, $httpBackend;
beforeEach(function() {
module('contatooh');
inject(function($injector, _$httpBackend_){
$scope = $injector.get('$rootScope').$new();
$httpBackend = _$httpBackend_;
$httpBackend.when('GET', '/contatos/1')
.respond({_id: '1'});
});
});
// código posterior omitido
});
Afunção $httBackend.whenrecebecomoparâmetroaURIdoEnd-
pointacessado.Emseguida,encadeamosumachamadaàfun ção respond,
quedevolveráocontatocriadopornós.Reparequeestamosdevolvendoape-
nasumobjetocomachave _id,suficienteparaatendernossoteste.
Pronto!Seráquenossotestepassa?Não!Parecequenossasoluç ãoainda
nãoestacompleta,poiscontinuamoscomomesmoerro:
TypeError: Cannot read property '_id' of undefined
258

## Página 271

CasadoCódigo Capítulo11. Testandoaaplicação
Parecequenossoback-enddementirinhanãofuncionou,masporquê?
$httpBackend.flush
Omotivodenossotesteterfalhadoépelofatode $httpBackendtra-
balharsincronamente.Comoassim?Reparequeachamadadenossafun ção
expectvemdepoisdacriaçãodocontroller. Se $httpBackendfosseas-
síncrono,nossafunção expectnãofuncionaria.Precisamosindicaremque
pontodenossotestequeremosqueasrequisiçõessejamresolvidasdeumasó
vez.Fazemosissochamando $httpBackend.flush:
describe("ContatoController", function() {
var $scope, $httpBackend;
it("Deve preencher o Contato quando
parâmetro de rota for passado",
inject(function($controller) {
$controller('ContatoController', {
$routeParams: {contatoId: 1},
'$scope': $scope
});
$httpBackend.flush();
expect($scope.contato._id).toBeDefined();
}));
});
ComoKarmarodando,vocêreceberáoutramensagemdeerro:
Error: Unexpected request: GET /contatos
No more request expected
Qualomotivodessavez?
MockeapenasEndpointsacessadosduranteoteste
Nosso flushfuncionou,porémquandousamos $httpBackendpre-
cisamosmockarosEndpointschamadospelocontroller. Nãoprecisamos
mockar todos os Endpoints, apenas aqueles acessados de acordo com o
259

## Página 272

11.6. $httpBackend:“mockando”nossobackend CasadoCódigo
critériodenossa Spec.Difícilselembrardeles?Nãosepreocupe,vocêrece-
beráumamensagemdeerroparacadaumatéqueprepareumarespostapara
todoseles.
OKarmapodeserusadoemduasfases.Aprimeira,enquantodesen-
volvemosparaobtermosfeedbackemtemporeal,easegunda,atravésde
umservidordeintegração,algoqueveremosnospróximoscapítulos.
Vamosrecordarque ContatoControllercarregaemsuainicialização
umalistadecontatos(estaéumaboahoradereverocódigonase ção5.6).
Sendoassim,vamosmockararespostaparaaURI /contatosretornando
umalistacomapenasumobjeto,inclusiveelenãoteráchavealguma. Não
sepreocupe,issoésuficientejáquenãotemosinteressenalistadecontatos,
apenasemresolveraexpectativadarequisiç ãoemnossoteste.
Porfim,nossotesteficaráassim:
describe("ContatoController", function() {
var $scope, $httpBackend;
beforeEach(function() {
module('contatooh');
inject(function($injector, _$httpBackend_){
$scope = $injector.get('$rootScope').$new();
$httpBackend = _$httpBackend_;
$httpBackend.when('GET', '/contatos/1')
.respond({_id: '1'});
$httpBackend.when('GET', '/contatos')
.respond([{}]);
});
});
it("Deve criar um Contato vazio quando
nenhum parâmetro de rota for passado",
inject(function($controller) {
$controller('ContatoController', {
'$scope': $scope
});
260

## Página 273

CasadoCódigo Capítulo11. Testandoaaplicação
expect($scope.contato._id).toBeUndefined();
}));
it("Deve preencher o Contato quando
parâmetro de rota for passado",
inject(function($controller) {
$controller('ContatoController', {
$routeParams: {contatoId: 1},
'$scope': $scope
});
$httpBackend.flush();
expect($scope.contato._id).toBeDefined();
}));
});
Atéaqui,nestecapítulo,vimoscomorealizartestesdeunidadecomJas-
mine,KarmaeAngular-Mocks,masaindafaltaaprendermoscomorealizar
testesdepontaaponta,osfamosos e2etests(end to end test).
11.7 Testando de ponta a ponta
Naseçãoanterior,testamospequenaspartesdenossosistemaatravésdetestes
deunidade. Masseráquetestarapenaspartesisoladasdenossosistemaé
suficiente?Talvezumaanalogiapossanosdarumaresposta.
Umametáfora,umproblema
Imaginequevocêtenhacriadoumquebra-cabe çadaquelesquefragmen-
tamafotodeumcenáriosurrealemzilhõesdepartes. Oacabamentode
cadapeçaémeticulosamentetestadoparagarantiramelhorqualidadepara
oclientefinal. Porém,umasemanaapósolan çamento,algunsclientesde-
volveramoprodutoalegandoquealgumaspe çasfaltavamouquealgumas
delasnãoseencaixavamouentãoseencaixavamcommuitofolga,prejudi-
candooresultadofinal.
Sepudessevoltaraopassado,oquevocêpoderiaterfeitoparaevitaressa
catástrofe?Comcertezadevemtervindoàsuacabe çamaisdeumaresposta,
masoqueachadetermontadocadaquebra-cabe çaantesdeembalá-lover-
261

## Página 274

11.7. Testandodepontaaponta CasadoCódigo
ificandooresultadofinal? Deslocarfuncionáriosparaestafinalidadecom
certezaseriaalgocustoso,inclusiveoprocessonãoseriaumdosmaisrápi-
dos.
Comotestarsuaaplicaç ãocomoumtodo?
Eseoquebra-cabe çafossenossaaplicaçãoContatooh? Comotestá-la
comoumtodo,istoé,nãononíveldeunidade,masseufuncionamentore-
cebendodados,interagindocomoservidorwebegravandonobancodeda-
dos?Seráqueumroteirocomtodosospassosquedevemsertestadosésufi-
ciente?Quemexecutaráessespassos,vocêousuaequipedequalidade?Ese
umerroacontecer?Eleseráreportadoemtempohábilparanãoacontecero
deploydeumaaplicaçãocomproblemas?
Automatizando,automatizando,automatizando
AprendemosaautomatizartarefascomGrunt,inclusiveaautomatizar
testesdeunidadecomKarma. Seráquenãopodemosfazeramesmacoisa
comnossostestesdepontaaponta?Imaginesenolugardoroteirotivésse-
mosumscriptexecutávelquesimulasseainteraç ãohomem-máquinaeque
procurasseporresultadosprevisíveis.Comcerteza,saberíamosquandoalgo
inesperadoacontecesse,inclusiveteríamosacertezadequenenhumpasso
seriapulado.Resumindo: queremosautomatizarnossostestes end-to-end
(e2e).
Testese2ecomSelenium
Testes end-to-end(e2e)procuramgarantirqueoscomponentesintegra-
dosdeumafuncionalidadedaaplicaç ãofuncionamcomoesperado.Todaa
aplicaçãoétestadaemumcenáriodomundoreal,taiscomoacomunicaç ão
comobancodedados,rede,hardwareeoutrasaplicações.
OSelenium(http://www.seleniumhq.org)éaferramenta de facto para
automatizartestese2eemnavegadores. Todamágicadeautomaçãoocorre
atravésdoseuWebDriverescritoparadiversosnavegadoresdomercado.
OstestesdoSeleniumsãoescritosnalinguagemJava,masissonãoim-
pedequeoutraslinguagenssejamutilizadas.Porexemplo,háoprojeto Web-
262

## Página 275

CasadoCódigo Capítulo11. Testandoaaplicação
DriverJs(http://webdriver.io/)criadoparaoNode.js.
11.8 Protractor: testes end-to-end com Angu-
larJS
Nossatarefanestase çãoserácriartestese2edanossaaplicaç ãoContatooh,
noentanto,háumproblemaqueprecisamosatacar.
Imaginequevocêtenhaautomatizadoocliquenobotão salvarda
páginadecadastrodecontatos. Sabemosqueotexto“Salvocomsucesso”
aparecerácasoocontatotenhasidosalvoenadamaisjustodoquetestarmos
porsuapresen çaparasabermosseelefoirealmenteincluído.Oproblemaé
queotesteserárealizadoantesdotérminodarequisiçãoassíncronaquegrava
ocontato,oqueinvalidarianossoteste.
Umasoluçãoéadicionartemporizadoresemnossostestesantesdecada
verificação,tornandooprocessodecriaçãodotesteaindamaiscomplexo.Foi
pensandonesteproblemaeemoutrosqueaequipedoAngularJScriouum
frameworkparatestese2echamado Protractor.
Protractor(http://angular.github.io/protractor)éumframeworkdetestes
end-to-endparaaplicaçõesfeitascomAngularJS.EleéconstruídosoboWeb-
Driverparainteragircomsuaaplicaç ãocomoumusuáriorealfaria. Em
outraspalavras,ProtractoréumacasquinhaqueenvolveoWebDriver,per-
mitindoquenossostestessejamexecutadossemnospreocuparmoscomtem-
porizadorestodavezquetestarmosnossaaplicaç ão.Hátambémfunçõesex-
clusivasquenosajudamainteragircomváriosrecursosdoAngularJS.
Instalação
Instalamos o Protractor globalmente (privilégio de administrador
necessário)atravésdo npm:
npm install -g protractor@1.5
Essecomando,alémdeinstalaroProtractor,seencarregarádainstalação
doWebDriverquedeveseratualizadologoemseguidapelocomando:
webdriver-manager update
263

## Página 276

11.9. ConfigurandooProtractorparaaaplicação CasadoCódigo
ParasubiroSeleniumServer:
webdriver-manager start
EssecomandoinicializaráoSeleniumServer,quereceberárequisições
detodososnossostestesfeitoscomProtractor. Oservidorcontrolaráseu
navegador localmente, inclusive podemos acessar seu status no endereço
(http://localhost:4444/wd/hub).
11.9 Configurando o Protractor para a apli-
cação
ParaqueoProtractorfuncione,precisamoscriarumarquivodeconfiguraç ão
quechamaremosde protractor.jsdentrodapasta config.Éneleque
indicamosocaminhodenossas Specs,nestecaso,específicasparatestes
e2e:
// config/protractor.js
exports.config = {
specs: ['../test/e2e/**/*.js']
};
JátemosoSeleniumServerrodandoeoProtractorconfigurado.Criare-
mososscripts contatosPageSpec.jse contatoPageSpec.jsdentro
dapasta contatooh/test/e2e.Oprimeiroconteráostestesparaaview
contatos.html,eosegundo,para contato.html. Seráquefaltamais
algumacoisaantesdecriarmosnossas Specs e2e?
11.10 Automatizando a autenticação do
usuário
Precisamosautomatizaroprocessodeautenticaçãodousuárioantesdaexe-
cuçãodenossostestes. Paraessafinalidade,podemosadicionarnoarquivo
deconfiguraçãodoProtractorachave onPrepare.Essachaverecebecomo
valorumafun çãoqueseráchamadaapenasumavezantesdaexecuç ãode
264

## Página 277

CasadoCódigo Capítulo11. Testandoaaplicação
nossassuítesdetestes. Éumbomcome çoparaaprendermoscomooPro-
tractorinteragecomoSelenium.
ÉrecomendadaacriaçãodeumacontanoGithubexclusivaparaesta
finalidade,masnadaimpedequevocêutilizesuamesmaconta(tomando
cuidadoparanãodivulgarsuasenha).
O primeiro passo é solicitar ao navegador que abra a páginahttp://
localhost:3000. Fazemosissoatravésdafun ção browser.get,mas,como
nossapágina auth.ejseapáginadelogindoGithubnãoutilizamAn-
gularJS,teremosproblemas:Protractoresperaeternamenteocarregamento
doAngularJS,oquenuncairáacontecernessaspáginas,oquetravanossos
testes.Lembre-sequeoProtractoréum wrapperemtornodeumainstância
doWebDriver,sendoassim,podemosinteragirdiretamentecomesteúltimo
atravésde browser.driver:
exports.config = {
specs: ['../test/e2e/**/*Spec.js'],
onPrepare: function() {
browser.driver.get('http://localhost:3000');
}
};
Sabemosqueparausuáriosnãoautenticadososistemaexibiráaview
auth.ejscomolink“EntrepeloGithub”. Precisamosterumareferência
paraestelinkemnossotesteparaquepossamosclicá-lo.Fazemosissoatravés
dafunção findElement:
exports.config = {
specs: ['../test/e2e/**/*.js'],
onPrepare: function() {
browser.driver.get('http://localhost:3000');
browser.driver.findElement(by.id('entrar')).click();
}
};
Vamosentendercomoessafun çãofuncionaecomoelatrabalhacomout-
rosobjetosglobais.
265

## Página 278

11.10. Automatizandoaautenticaçãodousuário CasadoCódigo
Desabilitando sincronização com
browser.ignoreS ynchronization
ExisteumaoutraformadeevitarqueoProtractorbusquepeloAngu-
larJSempáginasquenãooutilizem,evitandoanecessidadedeinteragir
comoWebDriverdiretamente.Porém,elanãofuncionoucorretamente
comaversão1.4doProtractor:
browser.ignoreSynchronization = true;
// comandos
browser.ignoreSynchronization = false;
OautorsugerequeestaformasejaevitadaatéqueaequipedoPro-
tractortenhaalgumaposiçãosobreseunãofuncionamento.
AfunçãofindElement
Afunção findElementnadamaisédoqueumafun çãoutilitáriapara
achareinteragircomelementosdoDOMdapáginaqueestamostestando.
Elarecebecomoúnicoparâmetroum locatorstrategy.
LocatorStrategy
Obtemosasestratégiasdelocalizaçãoatravésdoobjeto by. Emnosso
caso,procuramosoelementopeloseuID entrar(tenhacertezadetê-lo
digitadoquandocriouapágina auth.ejs). Emseguida,paraoelemento
retornado,solicitamosumclique.
Sabemos que o usuário será direcionado para a página de login do
GitHub. Nestapágina,precisamosinteragircomtrêselementos: osinputs
dologinesenhaeobotãoqueefetuaologin.Inspecionandoapágina,sabe-
mosfacilmentequeosinputspossuemosIDs login_fielde password
respectivamente.
AfunçãosendKeys
Preencheremososdoisinputsatravésdafun ção sendKeys:
266

## Página 279

CasadoCódigo Capítulo11. Testandoaaplicação
// config/protractor.js
exports.config = {
specs: ['../test/e2e/**/*.js'],
onPrepare: function() {
browser.driver.get('http://localhost:3000');
browser.driver.findElement(by.id('entrar')).click();
browser.driver.findElement(by.id('login_field'))
.sendKeys('email-de-teste');
browser.driver.findElement(by.id('password'))
.sendKeys('senha-do-email-de-teste');
}
};
Agorasónosrestaclicarnobotãoparaefetuarmosologin,porémele
nãopossuiumid,apenasoatributo namecomovalor commit.Podemos
selecionaroelementoatravésda locator strategy by.name:
// config/protractor.js
exports.config = {
specs: ['../test/e2e/**/*.js'],
onPrepare: function() {
browser.driver.get('http://localhost:3000');
browser.driver.findElement(by.id('entrar')).click();
browser.driver.findElement(by.id('login_field'))
.sendKeys('email-de-teste');
browser.driver.findElement(by.id('password'))
.sendKeys('senha-do-email-de-teste');
browser.driver.findElement(by.name('commit')).click();
}
};
Aindanãocriamosnossas Specs,masissonãonosimpedederodaro
Protractoreverificarseaautenticaç ãoestásendorealizada. Sóverifiquese
vocêcriouosarquivos contatosPageSpec.jse contatoPageSpec.js
mesmovaziosdentrodapasta contatooh/test/e2e,casocontrário,o
Protractorexibiráumamensagemdeerroalegandoquenenhumarquivofoi
267

## Página 280

11.11. Testandocenários CasadoCódigo
encontradodentrodapasta contatooh/test/e2e.RodamosoProtractor
atravésdocomando:
protractor config/protractor.js
Quandorodarmosnossoteste,onavegadorseráaberto,olink,clicado,e
apáginadelogindoGitHubpreenchidaautomaticamente.Noconsole,tere-
mosainformação:
Finished in 0 seconds
0 tests, 0 assertions, 0 failures
Masdenadaissoservesenãotestarmoscenárioschavesdenossaapli-
cação.
11.11 Testando cenários
Nossapróximatarefaserácriarumasuítedetestesespecíficaparaapágina
principal http://localhost:3000/#/contatos. Para essa suíte, criaremos uma
Spec que verificará se o usuário está logado. Utilizaremos a já con-
hecida função beforeEach do Jasmine para garantir que estamos na
páginacorretaantesdecadaumadenossasspecs. Vamoseditaroarquivo
test/e2e/contatosPageSpec.js:
// test/e2e/contatosPageSpec.js
describe('Página principal', function() {
beforeEach(function() {
browser.get('http://localhost:3000/#/contatos');
});
});
Repare que dessa vez utilizamos diretamente browser e não
browser.drivercomofizemosanteriormente.Agorafaztodosentidouti-
lizamoso wrapperdoWebDriverdisponibilizadopeloProtractorporquees-
tamostestandoumapáginaquepossuioAngularJScarregado.
Agoracriaremosnossaprimeira Specatravésdafunção it:
268

## Página 281

CasadoCódigo Capítulo11. Testandoaaplicação
// test/e2e/contatosPageSpec.js
describe('Página principal', function() {
beforeEach(function() {
browser.get('http://localhost:3000/#/contatos');
});
it('Deve estar logado', function() {
element(by.id('usuario-logado')).getText()
.then(function(texto) {
expect(texto.trim().length).toBeGreaterThan(0);
});
});
});
Repareque,nolugardeusarmosafun ção findElement,utilizamos
element,estaúltimatambémfornecidapeloProtractor. Suavantagemé
que,alémdas locator strategies quejáaprendemos,elaaceitaoutras
específicasdoAngularJS.
Nessecódigo,aprimeiracoisaquefazemosemnossa Specébuscaroel-
ementocomoID usuario-logado,nossatag spandaview index.ejs.
Depossedoelemento,chamamosafun ção getText,porémelanãoretorna
otextodoelemento,masuma promise.Issoacontecepelanaturezaassíncrona
dostestescomProtractor.Sabemosquetoda promisepossuiafun ção thene
nelatemosacessoaotextodoelemento.Porfim,usamosafun ção expectdo
Jasminequevimosnase ção11.2.Elatestaseotamanhodotextodoelemento
émaiorquezero.Rodandomaisumaveznossoteste:
protractor config/protractor.js
Noconsole,verificamosquenossotestepassou:
Finished in 8.475 seconds
1 test, 1 assertion, 0 failures
269

## Página 282

11.11. Testandocenários CasadoCódigo
Testandooutroscenários
Quetalagoracriarmosumtesteparanossocadastrodecontatos?Vamos
editaroarquivo test/e2e/contatoPageSpec.js:
describe('Cadastro de contatos', function() {
beforeEach(function() {
browser.get('http://localhost:3000/#/contato');
});
it('Deve cadastrar um contato', function() {
var aleatorio =
Math.floor((Math.random() * 10000000) + 1);
var nome = 'teste' + aleatorio;
var email = 'teste@email' + aleatorio;
});
});
Reparequeaquiabrimosateladecadastroe,logoemseguida,criamos
dadosaleatóriosparaocontato.Precisamosdeumareferênciaparaosinputs
quecapturamonomeeoe-maildocontato,masdestaveznãoutilizaremos
afunção by.idnem by.name.
by.model:locatorStrategyexclusivodoProtractor
OProtractordisponibilizaafun ção by.model,quepermiteselecionar
umelementopelovalordesuadiretiva ng-model:
// test/e2e/contatoPageSpec.js
describe('Cadastro de contatos', function() {
beforeEach(function() {
browser.get('http://localhost:3000/#/contato');
});
it('Deve cadastrar um contato', function() {
270

## Página 283

CasadoCódigo Capítulo11. Testandoaaplicação
var aleatorio =
Math.floor((Math.random() * 10000000) + 1);
var nome = 'teste' + aleatorio;
var email = 'teste@email' + aleatorio;
element(by.model('contato.nome')).sendKeys(nome);
element(by.model('contato.email')).sendKeys(email);
});
});
Preenchemosonomeeoe-mail,aindafaltaselecionarumaemergência
dalista. Osvaloresdadiretiva ng-optionsusadaparacriarnossalista
deemergênciassemprevãode“0”atéotamanhodalistamenosum. Por
debaixodospanos,oqueoAngularconsideramesmoéovalordomodel.
Destavez,procuraremosoelementoporumseletordeatributoatravésda
função by.css:
// test/e2e/contatoPageSpec.js
describe('Cadastro de contatos', function () {
beforeEach(function() {
browser.get('http://localhost:3000/#/contato');
});
it('Deve cadastrar um contato', function() {
var aleatorio =
Math.floor((Math.random() * 10000000) + 1);
var nome = 'teste' + aleatorio;
var email = 'teste@email' + aleatorio;
element(by.model('contato.nome')).sendKeys(nome);
element(by.model('contato.email')).sendKeys(email);
element(by.css('option[value="0"]')).click();
});
});
Pronto!Játemososcampospreenchidos,precisamosagorasalvarocon-
tato:
271

## Página 284

11.11. Testandocenários CasadoCódigo
// test/e2e/contatoPageSpec.js
describe('Cadastro de contatos', function() {
beforeEach(function() {
browser.get('http://localhost:3000/#/contato');
});
it('Deve cadastrar um contato', function() {
var aleatorio =
Math.floor((Math.random() * 10000000) + 1);
var nome = 'teste' + aleatorio;
var email = 'teste@email' + aleatorio;
element(by.model('contato.nome')).sendKeys(nome);
element(by.model('contato.email')).sendKeys(email);
element(by.css('option[value="0"]')).click();
element(by.css('.btn-primary')).click();
});
});
Porfim,precisamosverificarseamensagemdesucessofoiexibidapara
termoscertezadosalvamentodocontato. Lembre-sequeexibimosamen-
sagematravésdeuma Angular Expression(seção5.11).OProtractorpermite
selecionarumelementoatravésdesuaAEpelafun ção by.binding:
// test/e2e/contatoPageSpec.js
describe('Cadastro de contatos', function () {
beforeEach(function() {
browser.get('http://localhost:3000/#/contato');
});
it('Deve cadastrar um contato', function() {
var aleatorio =
Math.floor((Math.random() * 10000000) + 1);
var nome = 'teste' + aleatorio;
272

## Página 285

CasadoCódigo Capítulo11. Testandoaaplicação
var email = 'teste@email' + aleatorio;
element(by.model('contato.nome')).sendKeys(nome);
element(by.model('contato.email')).sendKeys(email);
element(by.css('option[value="0"]')).click();
element(by.css('.btn-primary')).click();
expect(element(by.binding('mensagem.texto'))
.getText())
.toContain('sucesso');
});
});
Depoisdotextoencontrado,verificamosseelecontémotexto“sucesso”.
Secontiver,nossotestepassará.Estánadúvida?Rodemaisumaveznossos
ostestes:
protractor config/protractor.js
Voltaremosparaoarquivo test/e2e/contatosPageSpec.jse,nele,
adicionaremosmaisuma Specquetestaráaremoçãodeumcontatodenossa
lista.
Parasabermosseumcontatofoiremovido,precisamosdototaldalista
antesedepoisdaremo çãocomparando-osnofinal. Paraisso, utilizare-
mosafun ção by.repeatquerecebecomoparâmetroovalordadiretiva
ng-repeat. Oselementoscriadosdinamicamentepela ng-repeattam-
bémganhamadiretivacomomesmovalor:
// test/e2e/contatosPageSpec.js
describe('Página principal', function () {
// código anterior omitido
it('Deve remover um contato da lista', function() {
// by repeater é coisa do protractor
var totalAntes = element
.all(by.repeater('contato in contatos'))
.count();
273

## Página 286

11.11. Testandocenários CasadoCódigo
});
});
Agoraquejátemosototaldecontatos,precisamosremoverumdelescli-
candonobotão“Remover”.Comoencontraremosessebotão?Podemosusar
afunção by.css,passandoumaclassecomoparâmetro,masteremosum
problema:obotão“Remover”érepetidoparacadaitemdalista,logo,teremos
elementosdiferentescomamesmaclasse. Umasoluçãoépegaraprimeira
linhadalistae,apartirdela,procuraroelementocomaclasse btn:
// test/e2e/contatosPageSpec.js
describe('Página principal', function() {
// código anterior omitido
it('Deve remover um contato da lista', function() {
var totalAntes = element
.all(by.repeater('contato in contatos'))
.count();
element(by.repeater('contato in contatos').row(0))
.element(by.css('.btn'))
.click();
});
});
Excelente! Agora,precisamoscontarototaldecontatosdalistaapósa
exclusãopara,emseguida,testarnossaexpectativa:
// test/e2e/contatosPageSpec.js
describe('Página principal', function() {
// código anterior omitido
it('Deve remover um contato da lista', function() {
274

## Página 287

CasadoCódigo Capítulo11. Testandoaaplicação
var totalAntes = element
.all(by.repeater('contato in contatos'))
.count();
element(by.repeater('contato in contatos').row(0))
.element(by.css('.btn'))
.click();
var totalDepois = element
.all(by.repeater('contato in contatos')).count();
expect(totalDepois).toBeLessThan(totalAntes);
});
});
Ésórodarmaisumaveznossostestes:
protractor config/protractor.js
Everificaroresultado:
Finished in 12.822 seconds
3 tests, 3 assertions, 0 failures
Paraquenossotestefuncione,precisamosternomínimoumcontato
cadastrado,casocontrário,nãoseremoscapazesdeescolherumcontato
nalistadecontatosdeemergência.Nãosepreocupe,napróximase ção
aprenderemoscomopopularumbancoespecíficoparatestesantesde
rodarmosnossostestese2e.
Executamosduassuítesdetestescomumtotaldetrês Specs,trêsas-
serçõesenenhumafalha.
Legebilidadedostestes
Aprendemosacriartestese2ecomProtractorquenadamaisédoqueuma
casquinhaemvoltadoWebDriverdoSeleniumquetraznovasestratégiasde
localizaçãodeelementos,inclusivenosremovearesponsabilidadedetrabal-
harmoscom timeoutstodavezqueformostestaralgumaaç ãoassíncrona.
275

## Página 288

11.12. PageObject:melhorandoalegibilidadeemanutençãodetestes CasadoCódigo
Masseráquenossostestessãolegíveis?Eseelestivessemotriplodein-
teraçõesdousuário?Eseoselementosdapáginamudassem(tag,IDs,classes
etc.)? Talvezestesejaumforteargumentocontratestese2e:manuten çãoe
legibilidade.
Napróximase ção,utilizaremosumpadrãodeprojetoquenosajudarána
manutençãoelegibilidadedenossostestese2e.
11.12 PageObject: melhorando a legibilidade e
manutenção de testes
Opadrãodeprojeto PageObject(http://martinfowler.com/bliki/PageObject.
html)procuraesconderosdetalhesdainterfacedousuáriodeoutroscom-
ponentesdosistema,emnossocaso,nossosscriptsdeteste. Eleconsegue
adicionandoemumobjetofun çõesdealtonívelcomo obterMensagem,
digitarNome, salvar,quedelegamseutrabalhoparaasfun çõesdema-
nipulaçãodeDOM,comoasdoProtractorqueutilizamos.SeoID,classeou
qualqueroutrapropriedadedeumelementodainterfacedousuáriomudar,
alteramosapenasemseu PageObjectenossotestecontinuaráintacto.
Vamoscriarapasta test/e2e/pageseconvencionarquetodososnos-
sos PageObjectsficarãonessapasta. Emseguida,criaremosoarquivo
test/e2e/pages/contatoPage.js,nosso PageObjectparaapágina
contato.html:
// test/e2e/pages/contatoPage.js
var contatoPage = function() {
this.visitar = function() {
browser.get('http://localhost:3000/#/contato');
};
this.digitarNome = function(nome) {
element(by.model('contato.nome')).sendKeys(nome);
};
this.digitarEmail = function(email) {
276

## Página 289

CasadoCódigo Capítulo11. Testandoaaplicação
element(by.model('contato.email')).sendKeys(email);
};
this.salvar = function() {
element(by.css('.btn-primary')).click();
};
this.obterMensagem = function() {
return element(by.binding('mensagem.texto')).getText()
};
this.selecionarPrimeiraEmergenciaDaLista = function() {
element(by.css('option[value="0"]')).click();
};
}
module.exports = contatoPage;
VejaquecriamosummódulodoNode.jsquedevolveumafun çãocon-
strutora. Agoravamosrefatorar test/e2e/contatoPageSpec.jspara
usarnosso PageObject.
// test/e2e/contatoPagesSpec.js
var ContatoPage = new require('./pages/contatoPage');
describe('Cadastro de contatos', function () {
var pagina = new ContatoPage();
beforeEach(function() {
pagina.visitar();
});
it('Deve cadastrar um contato', function() {
var aleatorio =
Math.floor((Math.random() * 10000000) + 1);
pagina.digitarNome('teste' + aleatorio);
pagina.digitarEmail('teste@email' + aleatorio);
pagina.selecionarPrimeiraEmergenciaDaLista();
277

## Página 290

11.12. PageObject:melhorandoalegibilidadeemanutençãodetestes CasadoCódigo
pagina.salvar();
expect(pagina.obterMensagem()).toContain('sucesso');
});
});
Você consegue agora enxergar em nosso teste alguma referência às
funçõesdemanipulaçãodeDOMdoProtractor?Ficoumaisfácildeler?E
seem contato.htmlobotãosalvarmudassesuaclassede btn-primary
para btn-default?Nossotestefalharia,comcerteza,porémcorrigiríamos
esseproblemaalterandoo PageObject,deixandonossotesteintacto.Va-
mosrodarnossotestemaisumavezeverificarsetudocontinuafuncionando:
protractor config/protractor.js
Que tal agora criarmos um PageObject para
test/e2e/contatosPageSpec.js? Vamos criar o arquivo
test/e2e/pages/contatosPage.js:
// test/e2e/pages/contatosPage.js
var contatosPage = function() {
this.visitar = function() {
browser.get('http://localhost:3000/#/contatos');
};
this.obterUsuarioLogado = function(nome) {
return element(by.id('usuario-logado')).getText();
};
this.obterTotalDeItensDaLista = function() {
return element.all(by.repeater('contato in contatos'))
.count();
};
this.removerPrimeiroItemDaLista = function() {
element(by.repeater('contato in contatos').row(0))
278

## Página 291

CasadoCódigo Capítulo11. Testandoaaplicação
.element(by.css('.btn'))
.click();
}
}
module.exports = contatosPage;
Por fim, vamos refatorartest/e2e/contatosPageSpec.js uti-
lizandonosso PageObject:
// test/e2e/contatosPageSpec.js
var ContatosPage = new require('./pages/contatosPage');
describe('Página principal', function() {
var pagina = new ContatosPage();
beforeEach(function() {
pagina.visitar();
});
it('Deve estar logado', function() {
pagina.obterUsuarioLogado().then(function(texto) {
expect(texto.trim().length).toBeGreaterThan(0);
});
});
it('Deve remover um contato da lista', function() {
var totalAntes = pagina.obterTotalDeItensDaLista();
pagina.removerPrimeiroItemDaLista();
var totalDepois = pagina.obterTotalDeItensDaLista();
expect(totalDepois).toBeLessThan(totalAntes);
});
});
Adiferençadalegibilidadedestaúltimaalteraç ãoficouaindamaisevi-
dente!Agoraésórodarnossostestes:
279

## Página 292

11.12. PageObject:melhorandoalegibilidadeemanutençãodetestes CasadoCódigo
protractor config/protractor.js
Tudodevecontinuarfuncionando,poissórefatoramosnossocódigo.
280

## Página 293

Capítulo12
Integraçãocontinua
“Nunca salte de um trampolim quebrado”
–WilliamShakespeare
CriamosaaplicaçãoContatoohpassoapassoeémuitoprovávelquevocê
tenhasidooúnicodesenvolvedornesteprocesso.Porém,nomundodede-
senvolvimentodesoftware,éextremamentecomumtermosequipesdosmais
diversostamanhostrabalhandoemummesmoprojeto.Jáimaginouintegrar
otrabalhodecadadesenvolvedordecadaequipe?Pormaisqueusemosum
sistemadecontroledeversãocomooGit,SubversionouMercurialnãoestare-
moslivresdeproblemasdeintegração.
Nocapítuloanterior,criamostestesdeunidadeee2eparagarantirmos
qualidadedenossosoftware.Equetalsenossostestesfossemexecutadosa
cadaintegraçãodecódigo?Aideiaéboa,masprimeiroprecisaríamosrealizar
aconstrução(build )denossaaplicaçãoacadaintegração,inclusivetorcer

## Página 294

12.1. TravisCI CasadoCódigo
paranãoesquecermosdeexecutarnossostestes.Muitaresponsabilidadepara
odesenvolvedor,não?Independentedadificuldade,oquequeremosrealizar
éaintegraçãocontínua denossaaplicaçãopararecebermosfeedbackomais
rápidopossívelsobrepossíveiserrosdeintegração.
Servidoresdeintegraç ão
Parasolucionarproblemascomoesse, foramcriadosservidoresespe-
cializadosnaconstruçãoeexecuçãodetestesdisparadosacadaintegraç ão
docódigodaaplicação. Elessãochamadosde servidoresdeintegraç ão.
Nomercadoexistemváriosservidorescomessafinalidade,comooJenk-
ins/Hudson,Semaphore,CruiseControl,entreoutros.Nestecapítulo,apren-
demosarealizarintegraçãocontínuautilizandoo Travis.
12.1 TravisCI
TravisCI(https://travis-ci.com/)éumservidordeintegraçãocontinuacomo
serviço. EleéintegradocomoGitHubesuportaváriasplataformascomo
Node.jseJava.Vocêpodeutilizargratuitamenteaversãoopensource(https:
//travis-ci.org/)ouoptarpelaversãopaga(https://magnum.travis-ci.com),
quepermitebuildconcorrenteentreoutrasvantagens.
OprimeiropassoparautilizarmosoTravisétermosumacontanoGithub
(https://github.com)eumrepositórioexclusivoparanossaaplicaç ãoConta-
tooh. NãonosaprofundaremosnosdetalhesdoGit,focaremosapenasnos
passosquedevemserfeitosparasuaintegraç ãocomoTravis.
Controlando versões com Git eGitHub
NãodominaGitaindaouquersabermais?Vocêencontranaprópria
CasadoCódigoolivro Controlando versões com Git e GitHub,deAlexan-
dreAquileseRodrigoFerreira.
Preparandoorepositório
NoGithub,criaremosorepositório contatooh. Antesdeassociarmoso
282

## Página 295

CasadoCódigo Capítulo12. Integraçãocontinua
repositóriocomnossoprojeto,crieoarquivo .gitignoredentrodapasta
local contatooh.Estearquivoserveparaindicarmosdequaisarquivosou
pastasnãoqueremoscontrolarversão.Nele,adicionaremos:
.tmp
.DS_Store
.DS_Store?
node_modules/
public/vendor/
dist/
script/
Emseguida,vamosassociá-loàpastalocal contatooh,nossaaplicação,
atravésdoscomandos:
git init
git add .
git commit -m "primeiro commit"
git remote add origin git@github.com:suaContaNoGit/contatooh.git
git push -u origin master
Excelente! Nossocódigojáestádisponibilizadonorepositóriopúblico
criadoemseuGithub.Nossapróximatarefaseráconfigurarnossorepositório
paraseintegrarcomoTravis.
12.2 Configurando .travis.yml
ParaquepossamosintegrarnossorepositóriocomoTravis,precisamoscriar
seuarquivo .travis.yml.Estearquivoestánoformato YAML(YAML Ain’t
Markup Language,http://www.yaml.org/),voltadoparaserializaçãodedados
legíveisporhumanos.Nãoentraremosnosdetalhesdessalinguagem,porém
éimportanterespeitarmosaindentaçãodoarquivo,casocontrário,eleterá
umaestruturainválida.
ExisteumutilitáriodeconfiguraçãodisponibilizadopeloTravisfeito
emRuby,porémoautorpreferiunãoutilizá-lonestaetapadoprojeto
paraqueoleitorentendamaisdetalhadamenteoarquivo .travis.yml
esuaimportância.Maistarde,eleseráutilizadonocapítulo 14.5.
283

## Página 296

12.2. Configurando.travis.yml CasadoCódigo
Crieoarquivo .travis.ymldentrodapasta contatooh. Nosso
primeiropassoserádefiniralinguagemeaversãoqueserãoutilizadaspelo
Travis,inclusiveume-maildenotificaç ãoquereceberámensagenssobreo
statusdobuild:
language: node_js
node_js:
- 0.10
notifications:
- seuemail@email.com
Éclaroqueessasconfiguraçõesaindanãosãosuficientes.Precisamosadi-
cionarmaisconfigurações.
CiclodeVida
O Travis possui umciclo de vida e sua primeira fase é chamada
before_install.Nela,baixamostodosarquivosdequeprecisamosantes
deoTravisautomaticamentechamarocomando npm install paranós.
Em nosso caso, instalaremos alguns módulos chaves globalmente, assim
comofizemosemnossamáquinalocal.Tambémsolicitaremosaobowerque
baixenossasdependênciasfront-endjáqueoTravisnãoochamaautomati-
camente:
before_install:
- npm install -g bower@1.3
- npm install -g grunt-cli@0.1
- npm install -g karma-cli@0.0
- npm install -g protractor@1.5
- webdriver-manager update
- bower install
Imediatamenteapósafase before_install,oTravisbaixarátodas
nossasdependênciasatravésdocomando npm install. Issonãoésufi-
ciente,poisprecisamosrodarnossoscriptdoGruntqueminificaeconcatena
nossosscripts.Éporissoqueexisteafase before_script.Elaéanteriorà
fasequeexecutanossostestes:
284

## Página 297

CasadoCódigo Capítulo12. Integraçãocontinua
before_script:
- grunt
- cd dist
ComoinstalamosoGruntglobalmentenabase before_install,o
comando gruntfuncionarágerandoapasta dist.Emseguida,mudamos
odiretóriodetrabalhoparaestapasta.Omotivoésimples:queremosrodar
nossostestescomoprojetodevidamenteminificadoeconcatenado,versão
quemaistardeentraráemprodução.
AgoraqueremosexecutarnossostestesunitáriosatravésdoKarma,mas
nãousandooChromeouFirefox. Paraquenossotesteroderapidamente,
utilizaremosoPhantomJS,umnavegadorseminterfacegráficaquepodeser
chamadoporlinhadecomando.Paraisso,precisamosinstalarseulan çador
especialmentefeitoparaoKarma:
npm install karma-phantomjs-launcher@0.1 --save-dev
Nãoesque çaquenovosarquivosprecisamseradicionadoscomoco-
mando git add equequalqueralteraçãofeitaprecisasersincronizada
comorepositórioatravésdocomando git push.
Agora,nafase scriptchamaremosoKarma,masindicandoqueele
utilizaráoPhantomJS,epassaremosoparâmetro --single-runparaque
eleexecuteostestesefinalizelogoemseguida.Issoénecessárioparaqueo
Karmanãotraveonossoservidordeintegraç ão,aliás,sófazsentidomoni-
torararquivosnoambientededesenvolvimento,nãodetestes.
script:
- karma start config/karma.config.js --single-run --browsers
PhantomJS
Excelente!Issojáésuficienteparaconstruirmoserodarmosnossostestes
deunidade.PrecisamosagoracriarumacontanoTravis.
285

## Página 298

12.3. AssociandoseurepositórioaoTravis CasadoCódigo
12.3 Associando seu repositório aoTravis
CriarumacontagratuitanoTraviséextremamentesimples. Bastaacessar
oendereço(https://travis-ci.org)e,nocantodireitosuperior,clicarnolink
“SigninGithub”.Naprimeiravez,seráexibidaumamensagemparaquevocê
confirmequeoTravispoderáteracessoaoseurepositório. Advinhemque
protocoloeleestáutilizando?OOAuth2.0,aquelemesmoprotocoloqueuti-
lizamosparaaautenticaçãodenossosistemanase ção8.1.
Depoisdeconfirmar,nocantoesquerdodatelaapareceráumaabacom
otítulo My repositories. Elaexibetodososrepositóriosmonitorados
peloTravis,mas,comoacabamosdecriarnossaconta,nenhuméexibido.
Adicionamosnovosrepositóriosatravésdobotãocomsinaldesoma:
Fig.12.1:Repositóriosmonitoradoseadiçãodenovosrepositórios
Seráexibidaumapáginaquelistarátodososseusrepositóriosdesuaconta
noGitHub.Casonenhumsejaexibido,bastaclicarnobotão sync now.Para
cadaum,haveráumbotãodeon/off. Precisamosligá-loparaorepositório
contatooh. Porém,oTravissórealizaráomonitoramentocasohajaoar-
quivo .travis.ymlnaraizdorepositório.
Fig.12.2:Liga/desligamonitoramentodorepositóriopeloTravis
Depois de ativar o repositório, ao voltarmos para a página (http://
286

## Página 300

12.3. AssociandoseurepositórioaoTravis CasadoCódigo
acessaroTravis,masseráqueexistealgumamaneiradeonossorepositório
nosfornecerestainformação? Sim! FoipensandonissoqueoTraviscriou
uma barra de status que pode ser adicionada noREADME.mdde nosso
repositóriodoGitHub:
Fig.12.5:RepositórionoGithubexibindostatusdobuild
Paraadicionarostatusexibidonaimagemanterior, bastaacessarseu
repositórionoTraviseclicarem build Unknown:
Fig.12.6:Statusdobuild/tiposdenotificações
Quandoclicado,seráexibidoumdiálogonoqualpoderemosescolherde
umalistaoformato Markdownutilizadopelo README.mddoGitHub:
Fig.12.7:Markdowndestatusdebuild
Agora é só copiar e colocar o conteúdo exibido noREADME.mddo
repositóriodenossaaplicação. Qualquerumqueacessarorepositórioterá
288

## Página 301

CasadoCódigo Capítulo12. Integraçãocontinua
umaformarápidadesaberemquesituaçãoencontra-seaconstruçãodopro-
jeto.
Enossostestese2ecomProtractor?
PoderíamospedirparaqueoTravisrodasseessestestesparanós,mas
alémdotempodeespera,quenãoseriaumdosmelhores,ficaríamoslimi-
tadosautilizaroPhamtonJSouoFirefox. Paranãotermoslimitesnoque
podemosconseguiremnossostestese2e,utilizaremosemconjuntocomo
Travisumserviçoespecializadopararodartestesdestetipo,assuntodapróx-
imaseção.
12.4 TaaS: test as a service com SauceLabs
Nolugardenospreocuparmoscomainfraestruturanaqualnossostestese2e
rodarão(configuraçãodoSeleniumServer,suporteatodososnavegadores
domercadosejamelesDesktopoumobileetc.)podemosrodarnossostestes
utilizandoserviçosdeterceiroscomestafinalidade,osfamososTaaS(test as
a service).
SauceLabs(http://saucelabs.com)éumTaaSgratuitoparaprojetosopen
sourceepagoparaprojetosfechados.Eleéfacilmenteintegradocomdiversos
servidoresdeintegraçãocontínuadomercado,inclusiveoTravisquevimos
naseçãoanterior.
Serviço gratuito
OservidorgratuitodoSauceLabsoferece:
• Duashorasdetestesautomatizados;
• TodososnavegadoresdeDesktopeMobile;
• Duasmáquinasvirtuaisconcorrentes.
289

## Página 302

12.5. Preparandoaaplicaçãoparadiferentesambientes CasadoCódigo
OSauceLabs,alémderodarnossostestesnosnavegadoresquedesejar-
mos,aindatiraumascreenshotdecadaaç ãodenossoscriptdetestequepode
serconsultado,inclusiveelecriaumscreencastcompostoportodasasscreen-
shotsparaquepossamosvisualizarcomootestefoirealizado. Oprimeiro
passoparautilizarmosoSauceLabsérealizarmosnossoregistroemseusite
(https://saucelabs.com/signup).
Depois do registro, precisamos preparar nosso sistema para adotar
parâmetrosdeconfiguraçãodiferentesdeacordocomoambienteemque
nossaaplicaçãoéexecutada.
12.5 Preparando a aplicação para diferentes
ambientes
Noambientedetestes,queremosutilizarobanco contatooh_testno
lugarde contatooh,inclusivequeremospopulá-locomalgunscontatos
antesde cadateste. Também precisamosdisponibilizarpara oTravis os
CLIENT_IDe CLIENT_SECRETdanossaaplicação,assimcomoousuário
esenhaqueutilizaremosemnossostestese2e.Nãopodemossimplesmente
deixaressasinformaçõesemnossorepositóriopúblicocorrendooriscode
elasvazarem.Aideiaécriarmosvariáveisdeambientediferentesparaoam-
bientededesenvolvimentoetestes.
Oobjetoglobalprocess
OnúcleodenossasoluçãomoranoobjetoglobaldoNode.jschamado
process.Éatravésde process.envquetemosacessoaqualquervariávelde
ambientedosistemaoperacional.Umpadrãomuitoutilizadoparaidentificar
emqualambientenossaaplicaçãoestárodandoéousodavariável NODE_ENV
comosvalores production, developmente test.Vejamosumexemplo:
// apenas exemplo, não entra em nenhum .js
var clientID, clientSecret;
if (process.env.ENV == "test") {
clientID = process.env.CLIENT_ID,
clientSecret = process.env.CLIENT_SECRET
290

## Página 303

CasadoCódigo Capítulo12. Integraçãocontinua
}
if (process.env.ENV == "development") {
clientID = "XXX",
clientSecret = "ZZZ"
}
// usa as variáveis clientID e clientSecret
Essecódigoidentificaemqualambienteestamosparasaberquaisvalores
adotarparao clientIDeo clientSecretdaaplicação.Oproblemadesta
soluçãoéqueteremosmuitos IFsespalhadospelonossocódigo.
Isolandoasconfiguraçõesdeambiente
Para resolvermos este problema, isolaremos as configurações
de cada ambiente em um módulo em separado. Dentro da pasta
contatooh/app/config/env,criaremososarquivos development.js
e test.js. Ainda não nos preocuparemos com as configurações de
produção.Tambémnãosepreocupecomasvariáveisqueaindanãovimos,
elasserãoelucidadasaindanestecapítulo:
// app/config/env/test.js
module.exports = {
env: 'test',
db: 'mongodb://localhost/contatooh_test',
sauceTestName: 'Contatooh E2E Testing',
sauceUser : process.env.SAUCE_USERNAME,
sauceKey : process.env.SAUCE_ACCESS_KEY,
travisJobNumber: process.env.TRAVIS_JOB_NUMBER,
travisBuild: process.env.TRAVIS_BUILD_NUMBER,
clientID: process.env.CLIENT_ID,
clientSecret: process.env.CLIENT_SECRET,
seleniumUser: process.env.SELENIUM_USER,
seleniumUserPassword: process.env.SELENIUM_USER_PASSWORD
};
// app/config/env/development.js
module.exports = {
291

## Página 304

12.5. Preparandoaaplicaçãoparadiferentesambientes CasadoCódigo
env: 'development',
db: 'mongodb://localhost/contatooh',
clientID: process.env.CLIENT_ID,
clientSecret: process.env.CLIENT_SECRET,
seleniumUser: process.env.SELENIUM_USER,
seleniumUserPassword: process.env.SELENIUM_USER_PASSWORD
};
Vamoscriarummóduloresponsávelpeloretornodaconfiguraç ãode
acordocomovalordavariável process.env.NODE_ENV.Paraisso,crie
oarquivo contatooh/app/config/config.js:
// app/config/config.js
module.exports = function() {
return require('./env/' + process.env.NODE_ENV + '.js');
}
Vejamosumexemplodeseuuso:
// exemplo apenas, não entra em nenhum js
var config = require('./config')();
console.log(config.seleniumUser);
console.log(config.seleniumUserPassword);
console.log(config.env);
Refatorandonossaaplicaçãoparautilizarnossoobjetoconfig
Agora precisamos refatorar nosso sistema para que ainda se-
jamos capazes de rodar nosso teste de integração, porém utilizando
nosso objeto de configuração. Vamos come çar alterando o arquivo
contatooh/app/config/protractor.js:
var config = require('./config')();
// código anterior comentado
browser.driver.findElement(by.id('login_field'))
.sendKeys(config.seleniumUser);
browser.driver.findElement(by.id('password'))
292

## Página 305

CasadoCódigo Capítulo12. Integraçãocontinua
.sendKeys(config.seleniumUserPassword);
// código posterior comentado
Agora,nossoarquivo contatooh/server.js:
var config = require( './config/config')();
// código anterior comentado
require('./config/database')(config.db);
// código posterior comentado
Não adicionamos CLIENT_ID nem o CLIENT_SECRET como
variáveis de ambiente à toa. Precisamos alterar nosso arquivo
app/config/passport.js.Nele,temosfixososvaloresde clientIDe
clientSecret.Agoravamoslê-losdenossoobjeto config:
// app/config/passport.js
var config = require( './config')();
// código comentado
clientID: config.clientID,
clientSecret: config.clientSecret,
// código comentado
Se estivermos em ambiente de desenvolvimento, nosso banco
será contatooh, mas se estivermos em ambiente de testes, ele será
contatooh_test.Seráquejápodemossubirnossaaplicação?Aindanão.
Scriptparainicializaç ãodasvariáveisdeambiente
Nomínimo,precisamosconfigurarasvariáveisdeambienteutilizadaspor
config/env/development.js.
Vamoscriardoisscriptsqueatribuirãoasvariáveisdeambientesdeque
precisamos.Oprimeiroseráresponsávelpelainicializaçãodenossoservidor
esechamará contatooh/script/server.sh:
export NODE_ENV=development
export SELENIUM_USER=nome_de_um_usuario_no_github
export SELENIUM_USER_PASSWORD=senha_do_usuario
293

## Página 306

12.5. Preparandoaaplicaçãoparadiferentesambientes CasadoCódigo
export CLIENT_ID=client_id_da_apliacao
export CLIENT_SECRET=senha_do_client
node server
Osegundo, contatooh/script/test.sh,criaráasvariáveisdeam-
bienteutilizadaspeloProtractor:
export NODE_ENV=development
export SELENIUM_USER=nome_de_um_usuario_no_github
export SELENIUM_USER_PASSWORD=senha_do_usuario
export CLIENT_ID=client_id_da_apliacao
export CLIENT_SECRET=senha_do_client
protractor config/protractor.js
Poderíamosteratribuídoessasvariáveisdiretamentenosistemaop-
eracional,fazendocomqueficassemsempredisponíveis,masoautor
preferiudeclará-lasemscriptsparaqueoleitornãopercaofocodaapli-
caçãoestudandodetalhesdosistemaoperacionalutilizado.
É muito importante não controlarmos as versões dos arquivos
server.sh e test.sh. Queremos esses arquivos apenas localmente
paraquetenhamosumamaneirarápidaeeficazdeatribuirmosasvariáveis
deambienteerodarmosnossaaplicação,inclusiveseustestes.Éporissoque
jáadicionamosapasta scriptemnossoarquivo .gitignore.
Jápodemosiniciarnossoservidoratravésdocomando:
sh scripts/server.sh
Rodarnossostestese2e:
sh scripts/test.sh
Ainicializaçãodoservidoreaexecuç ãodenossostestese2edevemcon-
tinuarafuncionarlocalmente, poissómudamosaorganizaç ãodenosso
código,nãoocomportamentofinaldaaplicaç ãoedostestes.
294

## Página 307

CasadoCódigo Capítulo12. Integraçãocontinua
12.6 Integrando Travis eSauceLabs
Nossaaplicaçãocontinuafuncionandolocalmentedepoisdasalteraçõesre-
alizadas na seção anterior. Agora precisamos completar nosso arquivo
app/config/env/test.js com as informações que serão necessárias
quandorodarmosnossaaplicaçãoenossostestesnoTravis.
Sevoltarmosparaoarquivo config/env/test.js,veremosqueele
dependedevariáveisdeambientesqueaindanãodefinimos.Aideiaédefini-
lascomovariáveisdeambientedoTravis.
LogadosnoTravis,notopodireitodatela,háumaengrenagemqueaoser
clicadaexibiráumalistacomaop ção settings.Éatravésdessaop çãoque
acessamosapágina Environment Variables.Nela,podemosadicionar
quantasvariáveisdeambientedesejarmos,inclusivepodemosoptarparaque
seuconteúdosejavisívelnologdeconstruçãodoprojeto(recomendadoape-
nasparafinsdedepuração).
Vamosadicionarasseguintesvariáveis:
•SAUCE_USERNAME:logindoseuusuário(apenasonome,sem@)
noSauceLabs.ÉutilizadopeloProtractorquandoexecutarmosnosso
testese2enoTravis.
•SAUCE_ACCESS_KEY: sua chave no Sauce Labs. Acesse (https:
//saucelabs.com/account) e no canto inferior direito aparecerá seu
Acess Key.
•SELENIUM_USER:nomedequalquerusuáriodoGithubcujasenha
vocêpossui.
•SELENIUM_USER_PASSWORD:senhadousuáriodoGithub.
•CLIENT_ID:cadastradoparaaaplicaçãocontatoohnoGitHub.
•CLIENT_SECRET:geradoparaaaplicaçãocontatoohnoGitHub.
295

## Página 308

12.6. IntegrandoTraviseSauceLabs CasadoCódigo
Fig.12.8:VariáveisdeambientesadicionadasnoTravis
As variáveis de ambiente TRAVIS_JOB_NUMBER e
TRAVIS_BUILD_NUMBER são disponibilizadas automaticamente pelo
TraviseserãousadaspeloSauceLabsatravésdoProtractorparacriarum
identificadordenossostestes. Issoéinteressante,porquesaberemosqueo
testeXnoSauceLabsequivaleaobuildYdoTravis.
AvariávelNODE_ENV
Depois de atribuirmos todas as variáveis de ambiente necessárias no
Travis,precisamosalterarnossoarquivo .travis.ymlparaqueelecriea
variávelNODE_ENV,sóquedestavezelaterácomovalor test:
env:
global:
- NODE_ENV: test
296

## Página 309

CasadoCódigo Capítulo12. Integraçãocontinua
ComunicaçãocomSauceLabs
Tambémqueremosqueelecarregueo proxyqueseráusadoparaquenos-
sostestescomProtractorsejamrodadosnoSauceLabs:
addons:
sauce_connect: true
Subindoaaplicaçãoeexecutandonossostestese2e
Estamosquasenofim! Precisamosaindasolicitarque,imediatamente
apósaexecuçãodenossostestescomKarma,oTravissubanossaaplicaç ãoe,
emseguida,executenossostestese2e:
script:
- karma start config/karma.config.js --single-run --browsers
PhantomJS
- node server &
- protractor config/protractor.js
SubindooMongoDB
NãopodemosnosesquecerdesubirumainstânciadoMongoDBparaque
possamosrodarnossostestese2e:
services:
- mongodb
Populandoobancoantesdostestes
PrecisamospopularobancocriadopeloTraviscomalgunscontatosantes
deexecutarmosnossostestes. Paraisso,criaremosumarquivocomessafi-
nalidade,chamado contatooh/test/data.js.Destavez,utilizaremoso
driverdoMongonolugardoMongoose:
// contatooh/test/data.js
var MongoClient = require('mongodb').MongoClient;
var contatos = [
297

## Página 310

12.6. IntegrandoTraviseSauceLabs CasadoCódigo
{nome: "xyz1", email: 'xyz1@email.com.br' },
{nome: "xyz2", email: 'xyz2@email.com.br' },
{nome: "xyz3", email: 'xyz3@email.com.br' },
];
MongoClient.connect('mongodb://127.0.0.1:27017/contatooh_test',
function(erro, db) {
if(erro) throw err;
db.dropDatabase(function(err) {
if(err) return console.log(err);
console.log('Banco apagado com sucesso')
db.collection('contatos').insert(contatos,
function(err, inserted) {
if(err) return console.log(err);
console.log('Banco populado com sucesso')
process.exit(0);
});
});
}
);
Porfim,precisamospedirqueoTravisexecutenossoscriptantesdeexe-
cutarnossostestese2e:
before_script:
- node test/data.js
- grunt
- cd dist
.travis.yml:arquivofinal
Casooleitortenhaseperdidonestemundodeconfigurações,segueo
.travis.ymlfinal:
language: node_js
notifications:
email: seuEmail
node_js:
298

## Página 311

CasadoCódigo Capítulo12. Integraçãocontinua
- 0.10
services:
- mongodb
env:
global:
- NODE_ENV: test
addons:
sauce_connect: true
before_install:
- npm install -g bower@1.3
- npm install -g grunt-cli@0.1
- npm install -g karma-cli@0.0
- npm install -g protractor@1.5
- webdriver-manager update
- bower install
before_script:
- node test/data.js
- grunt
- cd dist
script:
- karma start config/karma.config.js --single-run --browsers
PhantomJS
- node server &
- protractor config/protractor.js
Adequandoprotractor.jsaonovoambiente
Nossa última alteraç ão será em nosso arquivo
contatooh/config/protractor.js para que ele utilize as variáveis
deambientedefinidasemnossoservidordeintegraç ão. Nãosepreocupe
quandovocêrodarotesteemambientededesenvolvimento,mesmosemque
onossoarquivo config/env/development.jstenhadefinidoalgumas
delas. Elasserãosimplesmenteignoradas,algojusto,jáquemuitasdelassó
fazemsentidoquandorodarmosnossostestesatravésdoSauceLabs,oque
nãofaremosemambientededesenvolvimento.
// alterando contatooh/config/protractor.js
var config = require( './config')();
299

## Página 312

12.6. IntegrandoTraviseSauceLabs CasadoCódigo
exports.config = {
sauceUser : config.sauceUser,
sauceKey : config.sauceKey,
capabilities : {
'name': config.sauceTestName,
'browserName': 'chrome',
'tunnel-identifier': config.travisJobNumber,
'build': config.travisBuild
},
specs: ['../test/e2e/**/*Spec.js'],
onPrepare: function() {
browser.driver.get('http://localhost:3000');
browser.driver.findElement(by.id('entrar')).click();
browser.driver.findElement(by.id('login_field'))
.sendKeys(config.seleniumUser);
browser.driver.findElement(by.id('password'))
.sendKeys(config.seleniumUserPassword);
browser.driver.findElement(by.name('commit')).click();
}
};
Agorajáestamospontosparaexecutarnossostestese2epeloTravis.Logo
apóstersubidoparaorepositóriodoprojetotodasasalteraçõesquefizemos,
verifiqueaconstruçãodoprojetopeloTravis.Setudofoiconfiguradocorre-
tamente,nossostestesnoSauceLabsdevepassar.
PodemosacessarnossacontanoSauceLabseverificarostatusdenosso
teste,screenshotsescreencasts:
Fig.12.9:SauceLabs:testesrealizados
300

## Página 315

Capítulo13
Criandosuasprópriasdiretivas
“Cuidado para não chamar de inteligentes apenas aqueles que pensam como
você. ”
–UgoOjetti
Nossa aplicação está pronta, excelente! Porém, realizaremos mais
umamudan ça. Precisamosenvolverpartedoconteúdodenossasparciais
contatos.htmle contato.htmldentrodeum paneldoBootstrap.
Este paneléconstruídocomacombinaçãodeumasériedeelementoscom
classesespecíficasdoBootstrap:
<div class="panel panel-default">
<div class="panel-heading">
<h3 class="panel-title">Listagem de Contatos</h3>
</div>
<div class="panel-body">

## Página 316

13.1. DDO DirectiveDefinitionObject CasadoCódigo
<!-- conteúdo do painel fica aqui -->
</div>
</div>
Apesardefuncional,teremosestecódigorepetidonasduasparciaise
podemoscorreroriscodeesquecermosdeadicionarumaououtraclasse,
comprometendooresultadofinal.
Oproblemaéquenãotemosumamaneiradereutilizaramarcaç ão
quevimosnoladodocliente,eprecisaremosdotítulodopainelvariandode
acordocomocontextoemqueéutilizado.ImagineseoHTMLsuportassea
seguintetagemseuvocabulário:
<!-- public/partials/contatos.html -->
<meu-painel titulo="Listagem de Contatos">
<!-- conteúdo da parcial contatos.html -->
</meu-painel>
Comcertezapoderíamosreutilizá-laemqualquerpágina,escondendoa
complexidadedecriaçãodopaineldoBootstrap.Estaideianãoénovidadee
muitosservidoreswebtrabalhamcomoconceitodecomponente.
Um componente é um conjunto de código (Java,#C, HTML, CSS,
JavaScriptetc.)queencapsuladeterminadocomportamento,podendoserre-
utilizadofacilmenteemváriasaplicações.
VimosqueopróprioAngularJSpossuisuasdiretivas,quenaverdade
são componentes reutilizáveis que ampliam o vocabulário do navegador,
ensinando-onovostruques.Esepudéssemoscriarnossasprópriasdiretivas?
Éissoqueveremosnestecapítulo.
13.1 DDOD irectiveDefinitionObject
CriamosnossasprópriasdiretivasquandoqueremosumcomponenteHTML
ou um comportamento reutilizável, inclusive podemos querer ambos ao
mesmotempo. TambémutilizamosesterecursodoAngularJSquandopre-
cisamosinteragircomoDOM.Daremosinícionestase çãoàcriaçãodenossa
primeiradiretiva.
Vamoscomeçarcriandoummóduloemseparadoqueconteránossasdi-
retivas.Issopermitiráqueelassejamreutilizadasmaisfacilmente,bastando
304

## Página 317

CasadoCódigo Capítulo13. Criandosuasprópriasdiretivas
importaronovomódulo,semanecessidadedecarregarmostodososoutros
recursosdaaplicação.Vamoscriaroarquivo:
// public/js/directives/
// meus-componentes/meus-componentes.js
angular.module('meusComponentes', [])
.directive('meuPainel', function() {
var directive = {};
return directive;
});
Criamosomódulo meusComponentes,quenãopossuidependência
alguma. Emseguida,chamamosafun ção directive,querecebecomo
primeiroparâmetroonomedadiretiva.Reparequeseunomeutilizaopadrão
CamelCase,porém,quandoformosutilizá-laemnossapágina,separaremos
cadapalavraporumhífen:
<meu-painel></meu-painel>
Osegundoparâmetrodadiretivaéumafun çãoquesempredeveretornar
um directive definition object(DDO).Nossapróximatarefaseráconfigurar
esteobjeto.
Apropriedaderestrict
Nossaprimeiraconfiguraçãodizrespeitoàformadeutilizaç ãodadire-
tiva. Queremosutilizá-lacomo(E)lementooucomo(A)tributo. Paraisso,
adicionamosemnosso DDOapropriedade restrict:
// public/js/directives/
// meus-componentes/meus-componentes.js
angular.module('meusComponentes', [])
.directive( 'meuPainel', function() {
305

## Página 318

13.1. DDO DirectiveDefinitionObject CasadoCódigo
var directive = {};
directive.restrict = "EA";
return directive;
});
Vejamososdoisexemplos:
<!-- como (E)lemento -->
<meu-painel></meu-painel>
<!-- como (A)tributo -->
<div meu-painel ></div>
Masondedefiniremosamarcaçãodenossadiretiva?Éoqueveremosa
seguir.
Apropriedadetemplate
SabemosqueoAngularJSteráqueprocessarnossadiretivasubstituindo-
apelo paneldoBootstrap.Éporissoquenosso DDOpossuiapropriedade
template.Énestapropriedadequedefinimosamarca çãodonosso panel,
eutilizamosaAngularExpression {{titulo}}nolocaldaimpressãodo
titulo:
// public/js/directives/meus-componentes/
// meus-componentes.js
angular.module('meusComponentes', [])
.directive( 'meuPainel', function() {
var directive = {}
directive.restrict = 'EA';
directive.template =
'<div class="panel panel-default">' +
' <div class="panel-heading">' +
306

## Página 319

CasadoCódigo Capítulo13. Criandosuasprópriasdiretivas
' <h3 class="panel-title">{{titulo}}</h3>' +
' </div>' +
' <div class="panel-body">' +
' </div>' +
'</div>';
return directive;
});
Dojeitoquefizemos,nossadiretivasóconseguiráobterotítulodealgum
controllerquegerencieoelementodoDOMnoqualelaestáincluída. Isso
nãofazmuitosentido,poissetivéssemosdoispainéisgerenciadosporum
mesmocontroller,nãoconseguiríamosatribuirumtítulodiferenteparacada
umdeles.Comoresolver?Éoqueveremosnapróximase ção.
13.2 Isolando o escopo de nossa diretiv a
Queremosquenossadiretiva meu-painelrecebaseutítuloatravésdoatrib-
uto titulo,nossainterfacedecomunicaçãocomadiretiva:
<meu-painel titulo="Listagem de Contatos" >
<!-- conteúdo do painel -->
<meu-painel>
Masparaquecada meu-paineldenossapáginatenhaseuprópriotí-
tulo,precisamosquetodospossuamumescopoisolado.
Escopoisolado
Oescopoisolado deumadiretivaéindependentedoescopoemqueela
existe,istoé,nãoherdadoescopopainoqualestáinserida.Issoevitaqueadi-
retivatenteacessaralgoqueestejaforadosseuslimites,evitandoquebagunce
oescopopai.
Aspropriedadesdeumadiretivacomescopoisoladosópodemserusadas
dentrodela,sendoinvisíveisparaomundoexterior.Todasessascaracterísti-
caspermitemacriaçãodeumcomponentequepodeserusadoindependente
dolugarondeoinserimos,algofundamentalparaseureúso,inclusivepermi-
tiráquecada meu-paineltenhaseuprópriotítulo.
307

## Página 320

13.2. Isolandooescopodenossadiretiva CasadoCódigo
Podemoscriarumescopoisoladoadicionandoapropriedade scope(não
confundacom $scopedocontroller!) emnosso DDO.Estapropriedade
armazenaumobjetocujaschavessãoacessíveisdentrodadiretiva.Normal-
mente,armazenamosnessaschavesosvalorespassadosatravésdosatributos
denossasdiretivas:
<!-- apenas exemplo, não entra na aplicação ainda -->
<meu-painel titulo="Listagem de Contatos">
</meu-painel>
// apenas exemplo, não entra na aplicação ainda
directive.scope = {
titulo: '@titulo'
};
O código anterior busca o valor do atributotitulo da diretiva
meu-painelemuso.
API da diretiv a
Quandocriamosumadiretiva,suaAPInadamaisédoqueseusatrib-
utos.Sãoelesquepermitemqueadiretivasecomuniquecomomundo
exterior. Sequisermosumescopoisolado,porémsemexpor,umaAPI
usamos:
diretive.scope = true;
Vocêdeveterreparadono @antesdovalordochave titulo.Eleéum
dosmodificadores(veremosoutrosembreve)utilizadosparaindicarcomo
osvaloressãopassadosdomundoexternoparadentrodoescopoisoladoda
diretiva.Nestecaso, @indicaqueovalorquereceberemosserásempreuma
string,umacópiadovalorpresentenoatributodadiretivaemusonaview.
Écomosefosseumarelaçãounidirecional,ondenossadiretivapodelereste
valorvindodoescopopai,porémqualqueralteraç ãoneledentrodadiretiva
nãosepropagaráparaopai:
308

## Página 321

CasadoCódigo Capítulo13. Criandosuasprópriasdiretivas
<!--
Parâmetro válido, a string "Listagem de Contatos"
é passada para a diretiva
-->
<meu-painel titulo="Listagem de Contatos">
</meu-painel>
<!--
Parâmetro válido, o resultado da interpolação
é passado para a diretiva
-->
<meu-painel titulo="Listagem de {{nome}}">
</meu-painel>
<!--
Parâmetro válido, o resultado da AE
é passado para a diretiva
-->
<meu-painel titulo="{{nome}}}">
</meu-painel>
Outropontoadestacaréquandooatributodadiretivanaviewéigualao
nomedapropriedadeemnossoescopoisolado,podemosomitironomedo
atributodeixandoapenas @:
directive.scope = {
titulo: '@'
};
Nossadiretivaficaráassim:
// public/js/directives/meus-componentes/
// meus-componentes.js
angular.module('meusComponentes', [])
.directive( 'meuPainel', function() {
var directive = {}
directive.restrict = 'EA';
309

## Página 322

13.2. Isolandooescopodenossadiretiva CasadoCódigo
directive.scope = {
titulo: '@'
};
directive.template =
'<div class="panel panel-default">' +
' <div class="panel-heading">' +
' <h3 class="panel-title">{{titulo}}</h3>' +
' </div>' +
' <div class="panel-body">' +
' </div>' +
'</div>';
return directive;
});
Excelente! Já podemos testar nossa diretiva. Para isso, precisamos
importá-laemnossapágina app/views/index.ejscomoúltimoscript,
masaindadentrodocomentárioespecialdo grunt-usemin:
<!-- app/views/index.ejs -->
<!-- build:js js/index.min.js -->
<!-- scripts anteriores omitidos -->
<script src="js/directives/meus-componentes/
meus-componentes.js">
</script>
<!-- endbuild -->
Como criamos um novo módulo, precisamos importá-lo no módulo
principaldaaplicação:
// public/js/main.js
angular.module('contatooh',
['ngRoute', 'ngResource', 'meusComponentes'])
.config(function($routeProvider) {
// código omitido
});
310

## Página 323

CasadoCódigo Capítulo13. Criandosuasprópriasdiretivas
Porfim,vamosenvolverapenasa divdalistadecontatos.Utilizaremos
adiretivacomoelemento:
<!-- public/partials/contatos.html -->
<!-- tags anteriores omitidas -->
<p ng-show="contatos.length">
Contatos cadastrados: {{contatos.length}}
</p>
<meu-painel titulo="Listagem de contatos">
<!-- apenas a div da tabela dentro da diretiva -->
<div class="table-responsive">
<table class= "table table-hover">
<!-- dados da tabela omitido -->
</table>
</div>
<meu-painel> 311

## Página 324

13.3. Transclusion CasadoCódigo
O prefixo data-e v alidadoresHTML
Muitasvezes,éexigidoquesuapáginapasseporvalidadoresqueveri-
ficamaestruturadoseudocumento,maisnotadamenteosdaW3C.Com
certeza,asdiretivasdoAngularJSnãopassarãonoteste.Paracontornar
esteproblema,todasasdiretivasdoAngularJSpodemserprefixadascom
data-.Esteprefixoindicaparaovalidadorqueestamosutilizandoum
custom attribute,algoaceitodentrodoHTML5:
<p data-ng-repeat="objeto in objetos">
Noexemplodonossopainel,poderíamosutilizaradiretivanoseu
formatoatributo,inclusiveprefixando-acom data-:
<div data-meu-painel>
<!-- conteúdo aqui dentro -->
</div>
Visualizandooresultadodenossadiretiva,temos:
Fig.13.1:Diretivaemação,porémnenhumconteúdoéexibido
Reparequeadiretivaérenderizada,porémnadaéexibido! Écomose
elaignorassetudooquecolocamosdentrodela. Asoluç ãodesteproblema
encontra-senapróximase ção,curioso?
13.3 Transclusion
Naseçãoanterior,criamosnossadiretiva meu-painel,porémseuconteúdo
nãoéexibido. Issoocorreporque,aoavaliaradiretiva,oAngularJStroca
312

## Página 325

CasadoCódigo Capítulo13. Criandosuasprópriasdiretivas
aquelefragmentodoDOMporumnovo,ignorandotudooquetinhaantes
lá.Porém,podemossolicitarqueelemantenhaoconteúdodoelementoadi-
cionandoemnosso DDOapropriedade transclude:
// public/js/directives/meus-componentes/
// meus-componentes.js
angular.module('meusComponentes', [])
.directive( 'meuPainel', function() {
var directive = {}
directive.restrict = 'EA';
directive.scope = {
titulo: '@'
};
directive.transclude = true;
directive.template =
'<div class="panel panel-default">'
+ '<div class="panel-heading">'
+ '<h3 class="panel-title">{{titulo}}</h3>'
+ '</div>'
+ '<div ng-transclude class="panel-body">'
+ '</div>'
+ '</div>';
return directive;
});
Repare que, além de adicionarmos a propriedade
directive.transclude=true, também adicionamos a diretiva
ng-transclude no elemento de nosso template cujo conteúdo dev-
eráserpreservado.
Testandomaisumavez,opaineléexibido,maravilha!
313

## Página 326

13.4. SeparandooDDOdeseutemplate CasadoCódigo
Fig.13.2:Diretivaemação
Karma:atualizandoarquivodeconfiguraç ão
Nãopodemosnosesquecerdeincluirapasta
../public/js/directives/**/*.js
noarquivodeconfiguraçãodoKarma,casocontrário,nossostestesde
unidadefalharãopornãoencontraremomódulo meusComponentes,já
queoimportamosnomóduloprincipaldaaplicaç ão:
// config/karma.config.js
files: [
'../public/vendor/angular/angular.js',
'../public/vendor/angular-mocks/angular-mocks.js',
'../public/vendor/angular-resource/angular-resource.js',
'../public/vendor/angular-route/angular-route.js',
'../public/js/main.js',
'../public/js/controllers/**/*.js',
'../public/js/services/**/*.js',
'../public/js/directives/**/*.js',
'../test/spec/**/*Spec.js'
],
Podemosmelhoraraindamaisodesigndenossadiretiva, assuntoda
próximaseção.
13.4 Separando oDDO de seu template
Vocêdeveterreparadoqueescreverotemplatedopaineldentrodadiretiva
tornasuamanuten çãomaistrabalhosa. Imagineseotemplatefosseainda
314

## Página 327

CasadoCódigo Capítulo13. Criandosuasprópriasdiretivas
maiscomplexo? Aliás,temosmisturadasemumúnicoarquivoaconfigu-
raçãodadiretivaesuaapresentaç ão. Podemosisolarotemplatedadiretiva
emseupróprioarquivoHTML,comadiferen çadequenãousaremosmaisa
propriedade template,mas templateUrlqueapontaparaoarquivo.
Primeiro, vamos mover a marcaç ão do
nosso template para dentro do novo arquivo
public/js/directives/meus-componentes/meu-painel.html:
<!-- public/js/directives/
meus-componentes/meu-painel.html -->
<div class="panel panel-default">
<div class="panel-heading">
<h3 class="panel-title">
{{titulo}}
</h3>
</div>
<div ng-transclude class="panel-body">
</div>
</div>
Agora,emnossadiretiva,vamossubstituirapropriedade templatepor
templateUrlapontandoparanossonovoarquivo:
// public/js/directives/meus-componentes/
// meus-componentes.js
angular.module('meusComponentes', [])
.directive('meuPainel', function() {
var directive = {}
directive.restrict = 'EA';
directive.scope = {
titulo: '@'
};
directive.transclude = true;
315

## Página 328

13.5. Maisdiretivas CasadoCódigo
directive.templateUrl =
'js/directives/meus-componentes/meu-painel.html';
return directive;
});
Nossadiretivadevecontinuarcomomesmoresultado,poismudamos
apenasamaneiracomqueorganizamosseucódigo.
Agorapodemosusaranossadiretivaemqualquerpágina,inclusiveem
nossaparcial public/partials/contato.html.Porém,antesdequal-
querreúso,vamoscriarmaisumadiretiva,destavezobotãoremoverdenossa
lista.
13.5 Mais diretiv as
Emnossaparcial public/partials/contatos.html,temososeguinte
botãoresponsávelpelaremo çãodeumcontato:
<button ng-click="remove(contato)"
class="btn btn-warning">
Remover
</buttom>
Queremosqueelesetorneestadiretiva:
<meu-botao-aviso nome="Remover"
acao="remove(contato)">
</meu-botao-aviso>
Vamos adicionar uma nova diretiva em nosso módulo
meusComponentes, que se chamará meuBotaoAviso. Criaremos
umescopoisoladocomaspropriedades nomee acao:
// public/js/directives/meus-componentes/
// meus-componentes.js
angular.module('meusComponentes', [])
316

## Página 329

CasadoCódigo Capítulo13. Criandosuasprópriasdiretivas
.directive('meuPainel', function() {
// código omitido
})
.directive('meuBotaoAviso', function() {
var directive = {}
directive.restrict = 'E';
directive.scope = {
nome : '@',
acao : '&'
};
return directive;
});
Diferentede meu-painel,queremosqueanovadiretivasejautilizada
apenascomoelementoemnossaspáginas. Alémdisso,utilizamosomodi-
ficador &paraapropriedade acao. Omodificador &nospermiteavaliar
ouinvocarumaexpressão(fun ção)noescopodoelementonoqualadiretiva
estáinserida.Faztodosentido,porque,quandoousuárioclicarnobotãore-
mover,queremosqueocódigoexecutadosejaaquelenoescopodocontroller.
Adiretivanãofaráideiadoresultadodaexpressão.
Agorasónosrestadefinirotemplatedonossobotão.Destavez,mantere-
mossuadeclaraçãodentrodaprópriadefiniçãodadiretivacomapropriedade
template:
// public/js/directives/meus-componentes/
// meus-componentes.js
angular.module('meusComponentes', [])
.directive('meuPainel', function() {
// código omitido
})
.directive('meuBotaoAviso', function() {
var directive = {}
317

## Página 330

13.6. ManipulandoDOMatravésdediretiva CasadoCódigo
directive.restrict = 'E';
directive.scope = {
nome : '@',
acao : '&'
};
directive.template =
'<button ng-click="acao()" class="btn btn-warning">'
+ '{{nome}}'
+ '</buttom>';
return directive;
});
PodemossubstituirocomponentedoBootstrappelonossobotão:
<!-- public/partials/contatos.html -->
<meu-botao-aviso nome="Remover"
acao="remove(contato)">
</meu-botao-aviso>
Todavezqueprecisarmosdeumbotãodeaviso,poderemosrecorrerà
nossadiretiva.Quetaltentarmosalgomaissofisticadonapróximase ção?
13.6 ManipulandoDOM através de diretiv a
Nossaaplicaçãoestáficandocadavezmelhor,porémexperimentealterarum
contato.Comcerteza,eleseráalterado,nossoformuláriolimpo,porémofoco
docursorficarásobobotão salvar. Queremosqueelefiquesobobotão
voltar,umrequisitodeUXválido,não?Sabemosqueissopodeserfeitovia
JavaScript,acessandooelementodoDOM:
// ContatoController
// código ilustrativo, não entra na aplicação
$scope.salva = function() {
318

## Página 331

CasadoCódigo Capítulo13. Criandosuasprópriasdiretivas
$scope.contato.$save()
.then(function() {
// código anterior omitido
// manipulando DOM no controller, please, no!
document.querySelector('#botao-voltar')
.focus();
})
};
Porém,amanipulaçãodeDOMdentrodenossoscontrollersostornará
difíceisdetestar,inclusive,quasetudodoAngularJSquevimosatéagorafoi
paraevitarmosestetipodemanipulaç ãoparafocarmosapenasnalógicada
aplicação.ÉaíqueadiretivadoAngularvemnossalvar.
NadiretivapodemosrealizarmanipulaçãodeDOMàvontadequando
necessário. Porserumpedaçodecódigoisoladoetotalmentedesacoplado
denossoscontrollers,nãoháimpactonatestabilidadedessesúltimos.
Vamoscriarumadiretivaqueserácapazdeatribuirofocoemqualquer
elementodapáginacontantoqueovalordoatributo focusseja true.Por
exemplo:
<a id="botao-voltar" meu-focus focus="btnBackFocus"
href="#/" class="btn btn-default">
Voltar
</a>
Nesseexemplo,temosadiretiva meu-focusutilizadacomoatributo.
Faztodoosentido,poispodemosadicioná-laemqualquerelementodenossa
página.Emseguida,temosoatributodadiretivachamado focus.Esteatrib-
uto,quandorecebeumvalor true,indicaqueoelementodeverecebero
foco.Alógicadaatribuiçãodessevalorserárealizadapelonossocontroller,
algoparecidocom:
/*
ContatoController
319

## Página 332

13.6. ManipulandoDOMatravésdediretiva CasadoCódigo
apenas ilustrativo, ainda não entra
no código da aplicação.
*/
$scope.salva = function() {
$scope.contato.$save()
.then(function() {
// código anterior omitido
// sem manipulação de DOM, yeh!
$scope.btnBackFocus = true;
})
};
AgoraquejátemosumaideiadaAPIdenossadiretiva,jápodemoscriá-
la:
// public/js/directives/meus-componentes/
// meus-componentes.js
angular.module('meusComponentes', [])
.directive( 'meuPainel', function() {
// código omitido
})
.directive( 'meuBotaoAviso', function() {
// código omitido
})
.directive( 'meuFocus', function() {
var directive = {};
directive.restrict = 'A';
directive.scope = {
focus: '='
};
320

## Página 333

CasadoCódigo Capítulo13. Criandosuasprópriasdiretivas
return directive;
});
Consegueveranovidade?Usamos focus: ‘=’ noescopoisoladoda
diretiva. Estemodificadorpermitequenossadiretivaobtenhadoatributo
focusovalordaexpressãoatribuídaaele,equalquermudan çarealizada
peladiretivanestevaloratualizarátambémovalornoescopopai.Estemodi-
ficadoréumaespéciede two-way data binding,noqualtantooescopo
paiquantooescopoisoladodadiretivatêmamesmareferênciaparaaex-
pressão.Porém,comestemodificador,nãopodemosusar {{}}comovalor
dadiretiva,apenasexpressões:
<!-
Parâmetro válido: a diretiva recebe a expressão
"btnBackFocus", avaliada N vezes dentro da diretiva.
-->
<a meu-focus focus="btnBackFocus" Voltar</a>
<!-
Parâmetro inválido: a expressão é avaliada, retornando true
ou false. Em seguida, o retorno é passado para a diretiva.
Neste caso, a diretiva não tem mais uma referência
para a expressão.
-->
<a meu-focus focus="{{btnBackFocus}}" Voltar</a>
E o modificador@?
Setivéssemosutilizado @,ovalorde focusseriasempreastring
"btnBackFocus",enãoovalorcorrentedaexpressão.
Eagora? ComoteremosacessoaoelementodoDOMparapodermos
focá-lo?Primeiro,precisamosdeumaintroduçãosobreamaneirapelaqual
oAngularJSprocessasuasdiretivasquandosãoencontradas.
321

## Página 334

13.6. ManipulandoDOMatravésdediretiva CasadoCódigo
Umpoucosobrediretivaesuasfases
OAngularJSprocessadiretivasemduasfases. Aprimeiraéa compile
phase.Nestafase,oAngularJStransformaotemplatedenossasdiretivasem
elementosdoDOMpara,logoemseguida,adicioná-losnodocumento,sub-
stituindoouaprimorandoelementosjáexistentes. Raramenteinteragimos
comestafase,poiselafoicriadapararesolverproblemasdeperformance
quandoutilizamosomesmotemplatedeorigem(antesdecompilar)várias
vezes,comoéocasodadiretiva ng-repeat.Todacompilaçãoretornauma
funçãodelink,oquecaracterizaoiníciodasegundafase.
Asegundafaseéchamadade linkphase. Énestafasequeoescopoda
diretivaécriado,observaçõesdemudançasdepropriedadespodemserfeitas,
inclusivepodemosteracessoaoescopocriadoeaoelementodoDOMao
qualadiretivafoiassociada.Éjustamenteoqueprecisamosparapodermos
atribuirofocoaoelemento:
// public/js/directives/meus-componentes/
// meus-componentes.js
// código anterior omitido
.directive( 'meuFocus', function() {
var directive = {};
directive.restrict = 'A';
directive.scope = {
focus: '='
};
directive.link = function(scope, element) {
});
return directive;
});
322

## Página 335

CasadoCódigo Capítulo13. Criandosuasprópriasdiretivas
A função link e seus parâmetros posicionais
Os argumentos da função link são posicionais, não injeções. Se
tivéssemosinvertidoosparâmetrosnoexemploanterior,nossocódigo
deixariadefuncionar.
Noexemploanterior,estamosinteressadosapenasnoescopodadiretiva
enoelementodoDOMaoqualelaestáassociada.Precisamossolicitarqueo
Angularmonitoreovalordapropriedade scope.focus.
13.7 Afunção $w atch
Naseçãoanterior,temosoesqueletodocódigodenossadiretivacomafi-
nalidadedefocarelementosdenossapágina,inclusiveadicionamosnaAPI
denossadiretivaapropriedade focus.Porém,todavezqueapropriedade
focusmudar,precisaremostestarseoseuvaloré trueparadepoisfocar-
mosoelementodoDOM.
Realizamosessaobservaçãoatravésdafun ção scope.$watch,quere-
cebecomoparâmetroonomedapropriedadequedesejamosobservareuma
funçãodecallbackqueseráexecutadaacadamudan ça:
// public/js/directives/meus-componentes/
// meus-componentes.js
// código anterior omitido
.directive('meuFocus', function() {
var directive = {};
directive.restrict = 'A';
directive.scope = {
focus: '=focus'
};
directive.link = function(scope, element) {
scope.$watch('focus', function() {
323

## Página 336

13.7. Afunção $watch CasadoCódigo
if (scope.focus) {
element[0].focus();
scope.focus = false;
}
});
};
return directive;
});
Dentro da função de callback, realizamos um teste para saber o
valor atual de scope.focus. Em seguida, chamamos a função
element[0].focus()parafocarmosoelemento.
Nafunçãopassadacomosegundoparâmetro,temosacessoaovalor
atualeantigodoelementomonitorado:
scope.$watch('focus', function(valorAtual, valorAntigo) {
});
Acessamosoelementocomoseelefosseumarray,porqueinternamenteo
AngularutilizaojQLite(https://code.google.com/p/jqlite/),umsubconjunto
daAPISizzle(http://sizzlejs.com/)utilizadapelojQueryparanosajudarcom
amanipulaçãodeDOM.Porém,ojQLitenãopossuiafun ção focus().O
quefizemosfoiacessaroelementodoDOMencapsuladopelojQLite.
element como jQ ueryObject
SetivéssemoscarregadoojQueryemnossapáginaantesdoscriptdo
AngularJS, elementsetornariaumjQueryObject,permitindoacesso
atodasasfun çõesdojQuery,incluindoafun ção focus.
Já podemos alterar nossa parcial public/contato.html
substituindo a marcação do botão voltar por nossa
diretiva, e já adicionaremos no escopo do controller
324

## Página 337

CasadoCódigo Capítulo13. Criandosuasprópriasdiretivas
public/js/controllers/ContatoController.js a propriedade
btnBackFocus:
<!-- public/partials/contato.html -->
<a id="botao-voltar" meu-focus focus="btnBackFocus"
href="#/" class="btn btn-default">
Voltar
</a>
// public/js/controllers/ContatoController.js
$scope.contato.$save()
.then(function() {
// código omitido
// novidade entra aqui, última linha da função!
$scope.btnBackFocus = true;
})
Excelente! Agora,bastacadastramosumnovocontatoevermosqueo
botão voltarrecebeofocologoemseguida.
Todavezqueusamos $watch.gastamospodercomputacional,sendoas-
sim,devemosserparcimoniososcomseuuso.Oidealéutilizá-loquandonão
houveroutraalternativa.Porexemplo,pararesolvermosoproblemadofoco
queacabamosdever,podemostrabalharcomo event bus doAngularJS,
assuntodapróximase ção.
13.8 Trabalhando com $broadcast
Vamosmodificaradiretivaquefizemosnase çãoanterior.Nolugardeusar-
mosotãocaro $watch,utilizamoso event bus doAngularJS.
Primeiro,emnossocontroller
public/js/controllers/ContatoController.js
vamossubstituiralinha
$scope.btnBackFocus = true;
325

## Página 338

13.8. Trabalhandocom$broadcast CasadoCódigo
porestenovocódigo:
$scope.$broadcast('contatoSalvo');
Éatravésdafun ção $broadcastdenossoescopoquedisparamosum
evento.Afun çãorecebecomoparâmetroonomedoeventoquedesejamos
disparar,emnossocaso, contatoSalvo.VamosalterartambémaAPIde
nossadiretivaquereceberácomoparâmetroapropriedade evento.
Vamosajustarseuusonapágina public/partials/contato.html:
<a id="botao-voltar" meu-focus evento="contatoSalvo"
href="#/" class="btn btn-default">
Voltar
</a>
ReparequeanovaAPIdenossadiretivarecebecomoparâmetroum
evento.Oqueprecisamosfazeragoraéalterarnossadiretivaparaqueseja
capazderesponderaoeventoqueserádisparadoemnossocontroller:
// public/js/directives
/meus-componentes/meus-componentes.js
// código anterior omitido
.directive( 'meuFocus', function() {
var directive = {};
directive.restrict = 'A';
directive.scope = {
evento: '@'
};
directive.link = function(scope, element) {
scope.$on(scope.evento, function() {
element[0].focus();
});
};
return directive;
});
326

## Página 339

CasadoCódigo Capítulo13. Criandosuasprópriasdiretivas
Oescopoprivadodadiretivareceberáapenasastringcomonomedo
eventoquedesejamosescutar,porisso,usamosomodificador @.Emseguida,
dentrodanossafun ção lin,escutamosaoeventopassadocomoparâmetro
atravésdafunção $on.
$broadcast vs $emit
Alémdafunção $broadcast,existetambémafun ção $emit. A
diferençaéqueoeventodisparadopeloprimeirodescenahierarquia
doescopo,afetandoapenasseuselementosfilhos.Jáosegundosobena
hierarquia.
Oprimeiroparâmetrodafun ção $onéonomedoeventoquedesejamos
escutar,osegundo,umafun çãodecallbackexecutadatodavezqueoeventoé
disparado.Emnossocaso,quandooeventofordisparado,oelementoaoqual
adiretivafoiassociadareceberáofoco.Pronto,agoraésótestarmosoresul-
tado. Usamosumasoluçãomaisbarataeelegantepararesolveroproblema
dofocodobotão.
Excelente,temosnossasdiretivasprontas,masseráquenosesquecemos
dealgo?Aprendemosatestarnossoscontrollersnase ção11.2,inclusiveuti-
lizamosoKarmaparaautomatizaresteprocesso.Napróximase ção,apren-
deremosatestarnossasdiretivas.
13.9 Testando diretiv as
Aprendemosacriardiretivasnase çãoanterior,erealizamosmanipulaçãode
DOMatravésdelas.Porém,todocódigoqueinteragecomaAPIDOMtem
certafragilidade.Éporissoqueéextremamenteimportantearealizaç ãode
testesparatermosagarantiadequenossocódigoserácompatívelcomosmais
diversosnavegadoresdomercado.Nestase ção,criaremosumtesteparacada
diretivaquecriamos.
Vamoscomeçaradicionandooscriptdenossadiretivaaoarquivodecon-
figuração config/karma.config.js:
327

## Página 340

13.9. Testandodiretivas CasadoCódigo
files: [
// código anterior omitido
'../public/js/directives/**/*.js',
'../test/spec/**/*Spec.js',
],
Agora, já podemos criar nosso arquivo de teste
test/spec/meusComponentesSpec.js. Em seguida, utilizaremos
ajáconhecidafun ção describeparadescrevernossotesteeafun ção
beforeEach para prepararmos o ambiente antes de rodarmos nossas
Specs:
describe('meuBotaoAviso', function () {
var $scope;
var element;
beforeEach( function() {
module('meusComponentes');
inject(function($rootScope, $compile) {
$scope = $rootScope.$new();
});
});
});
Carregamos o módulomeusComponentese solicitamos ao serviço
de injeção de dependência do AngularJs os artefatos$rootScope e
$compile.Oprimeironãoénovidadeparanós,porémosegundoéoserviço
responsávelpelacompilaçãodasdiretivas.Nossopróximopassoserácriarum
elementodoDOMapartirdeumastringquerefletenossadiretivaemuso.
Fazemosissoatravésdafun ção angular.element:
describe('meuBotaoAviso', function () {
var $scope;
var element;
328

## Página 341

CasadoCódigo Capítulo13. Criandosuasprópriasdiretivas
beforeEach(function() {
module('meusComponentes');
inject(function($rootScope, $compile) {
$scope = $rootScope.$new();
element = angular.element(
'<meu-botao-aviso nome="Remover" acao="remove()">'
);
});
});
});
Oresultadode angular.elementseráumelementodoDOMquenão
fazpartedenenhumdocumento.Estaetapaéimportanteporqueelalan çará
umerrocasoamarcaçãoqueastringarmazenasejainválida.
Agora,precisamoscompilaresteelemento. Esteprocessoconsisteem
passá-locomoparâmetroparaoserviço$compile.Afun çãoretornaráuma
funçãodelink.Lembre-sequeéna link phase queassociamosumescopo
aoelemento,sendoassim,passamosnosso $scopequecriamosapartirdo
$rootScope.Vejamosumexemplo:
var lnkFunc = $compile(element);
lnkFunc($scope);
Podemosrealizaresseprocessoemumatacadasó,evitandoacriaç ãoda
variávellnkFunc:
describe('meuBotaoAviso', function () {
var $scope;
var element;
beforeEach(function() {
module('meusComponentes');
329

## Página 342

13.9. Testandodiretivas CasadoCódigo
inject(function($rootScope, $compile) {
$scope = $rootScope.$new();
element = angular.element(
'<meu-botao-aviso nome="Remover" acao="remove()">');
$compile(element)($scope);
$scope.$digest();
});
});
});
Veja que imediatamente após a compilação da diretiva chamamos
$scope.$digest. Lembre-sequeoAngularJSsuporta data binding,
permitindo que nossa view apresente o valor atualizado do modelo de
umescopo. Quemmonitoraomodeloverificandopormudan çassãoos
watchers,ejáaprendemosautilizá-losemumadenossasdiretivasperson-
alizadas. Todosos watchersdaaplicaçãosãoavaliadosnociclo digest
chamadoautomaticamentepeloAngularJS.Porém,quandotestamosnossas
diretivas,somososresponsáveisporsuainvocação.
Pronto,avariável elementguardanossadiretivacompiladaeproces-
sadapeloAngularJS.Jápodemoscriarnossaprimeira Specparatestarnossa
diretiva:
describe('meuBotaoAviso', function () {
var $scope;
var element;
beforeEach( function() {
// código omitido
});
it('deve criar um botão de aviso com texto e função',
function() {
330

## Página 343

CasadoCódigo Capítulo13. Criandosuasprópriasdiretivas
expect(element.text()).toContain('Remover');
expect(element.attr('acao')).toBe('remove()');
}
);
});
Usamos as funções element.text e element.attr porque
elementéumobjetocriadopelojQlitequenosforneceumaAPIcômoda
pararealizarmosmanipulaçãodeDOM.
Dentrodapasta contatooh,vamosrodaroKarmanoterminalcomo
comando:
karma start config/karma.config.js
Vamos deixá-lo aberto enquanto criamos novos testes. O teste que
acabamosdecriarpassará.
Agora,vamoscriarumnovotesteparanossadiretiva meu-foco.Para
isso,adicionaremosdentrodomesmoarquivo
public/js/directives/meus-componentes
/meus-componentes.js
outrachamadaàfun ção describe:
describe('meuBotaoAviso', function () {
// código omitido
});
describe('meuFocus', function() {
var $scope;
var element;
var evento = 'contatoSalvo';
beforeEach(function() {
module('meusComponentes');
inject(function($rootScope, $compile) {
331

## Página 344

13.9. Testandodiretivas CasadoCódigo
$scope = $rootScope.$new();
element = angular.element(
'<button meu-focus evento="' + evento +
'">Voltar</button>');
$compile(element)($scope);
$scope.$digest();
});
});
});
Reparequeessecódigoémuitoparecidocomocódigodotesteante-
rior, porém, precisamosresolveroseguinteproblema. Paratestarmosse
nossoelementoestáfocado,precisamosadicioná-loaodocumento,casocon-
trário, nãopoderemosrecorreràchamada document.activeElement
paradescobrirqualéoelementofocadonapágina.Fazemosissopromovendo
documentparaumobjetodojQliteparaquepossamosutilizarafun ção
append:
// código anterior omitido
describe('meuFocus', function() {
// código anterior omitido
it('Deve focar o botão', function() {
angular.element(document.body).append(element);
});
});
Ótimo!Nossoelementocompiladoagorafazpartedodocumento.Agora,
precisamos disparar o eventocontatoSalvo e verificar se o texto de
document.activeElementcorrespondeaotextodonossobotão:
332

## Página 345

CasadoCódigo Capítulo13. Criandosuasprópriasdiretivas
// código anterior omitido
describe('meuFocus', function() {
// código anterior omitido
it('Deve focar o botão', function() {
angular.element(document.body).append(element);
$scope.$broadcast(evento);
expect(angular.element(document.activeElement)
.text()).toBe('Voltar');
});
});
Maisumtestepronto! SevocênãofechouoKarma,receberemosum
feedbackemtemporealsobrestatusdonossoteste.
Nãoéincomumtermosvários Specparaoalvodenossoteste.Por
exemplo,poderíamostestarseanossadiretiva meu-focusnãoganha
ofococasooevento contatoSalvonãotenhasidodisparado.Aideia
étestarospossíveiscasoscujosresultadossabemosdeantemão.
Porfim,sónosrestatestarnossadiretiva meu-painel. Teremosuma
seçãodedicadaparaesteteste.
13.10 Lidando com templateU rl em testes
Nesta seção, vamos elaborar o teste da diretiva meu-painel adi-
cionando mais uma chamada à função describe em nosso arquivo
test/spec/meusComponentesSpec.js:
describe('meuBotaoAviso', function () {
// código omitido
333

## Página 346

13.10. LidandocomtemplateUrlemtestes CasadoCódigo
});
describe('meuFocus', function() {
// código omitido
});
describe('meuPainel', function() {
var $scope;
var element;
beforeEach(function() {
module('meusComponentes');
inject(function($compile, $rootScope) {
$scope = $rootScope.$new();
element = angular.element(
'<meu-painel titulo="Principal"><p>Oi</p></meu-painel>'
);
$compile(element)($scope);
$scope.$digest();
});
});
});
Aideiaésimples:verificamosseoconteúdodastags h3e pcorrespon-
demaotítuloeaoconteúdodopainel,respectivamente.Porém,recebemosa
seguintemensagemdeerronoterminalquandonossotesteéexecutado:
Error: Unexpected request: GET js/directives/meus-componentes/meu-
painel.html No more request expected
Esteerroaconteceporqueutilizamos templateUrlemnossadire-
tiva.OAngularJStentarealizarumarequisiç ãoAjaxparabaixarotemplate
meu-painel.htmle,comonãotemososervidorrodando,oerroacontece.
334

## Página 347

CasadoCódigo Capítulo13. Criandosuasprópriasdiretivas
Vimosqueévantajosoutilizarmos templateURLenãoiremosab-
dicardele! Parasolucionarmosesteproblema,precisamosfazercomqueo
meu-painel.htmlestejapresentenocachedetemplatesdoAngularJSantes
deonossocódigorodar.Estecacheéusadopordebaixodospanostodavez
queotemplatedeumadiretivaébuscado,justamenteparaevitarnovasreq-
uisições.
Nolugardeinteragirmoscomoserviço $templateCachequeoAngu-
larJsdisponibiliza,utilizaremosoKarmaparapré-processartodososnossos
templates,convertendo-osparaumarquivo .jsecolocando-osautomatica-
mentedentrodocachedetemplatesdoAngularJS.
Primeiro,precisamosinstalaroplugindoKarmaresponsávelporestepré-
processamento:
npm install karma-ng-html2js-preprocessor@0.1 --save-dev
Emseguida,precisamosadicionarno karma.config.jsocaminho
‘../public/js/directives/meus-componentes/*.html’, que
contémnossostemplates:
files: [
'../public/vendor/angular/angular.js',
'../public/vendor/angular-mocks/angular-mocks.js',
'../public/vendor/angular-resource/angular-resource.js',
'../public/vendor/angular-route/angular-route.js',
'../public/js/main.js',
'../public/js/controllers/**/*.js',
'../public/js/services/**/*.js',
'../public/js/directives/**/*.js',
'../test/spec/**/*Spec.js',
'../public/js/directives/meus-componentes/*.html'
],
Precisamos ainda indicar que nossos templates devem ser pré-
processadospelonossoplugin:
preprocessors : {
'../public/js/directives/**/*.html': 'ng-html2js'
},
335

## Página 348

13.10. LidandocomtemplateUrlemtestes CasadoCódigo
Issoaindanãoésuficiente. Aindano karma.config.js,precisamos
adicionaropluginnalistadepluginsutilizados:
plugins : [
'karma-ng-html2js-preprocessor',
'karma-chrome-launcher',
'karma-phantomjs-launcher',
'karma-jasmine'
],
Estamosquaselá! Precisamosresolveroseguinteproblema: quandoo
Karmapré-processarnossoarquivo meu-painel.html,eleguardaráno
cachedetemplatesoarquivocomseucaminhoabsoluto,comonesteexemplo:
/Users/flaviohenriquealmeida/Desktop/trab/reposi
torios/contatooh/public/js/directives/meus-
componentes/meu-painel.html.js
O problema é que o templateUrl de nossa diretiva aponta
para js/directives/meus-componentes/meu-painel.html.
Essa discrepância fará com que nosso template não seja lo-
calizado. Para resolvermos isso, utilizaremos a propriedade
ngHtml2JsPreprocessorparasolicitarmosaremo çãodetodoocaminho
/Users/flaviohenriquealmeida/Desktop/trab/repositorios/contatooh/
atravésdeumaexpressãoregular,inclusivedaremosumnomeparaomódulo
queelegeraránofinalparaquepossamosimportá-loemnossostestes:
ngHtml2JsPreprocessor: {
moduleName: 'templates',
stripPrefix: '.*/public/'
},
Pronto, terminamos de ajustar okarma.config.js. Agora, pre-
cisamosimportaromódulo templatesdentrodafun ção beforeEach
dotestedopainel:
// código omitido
describe('meuPainel', function() {
336

## Página 349

CasadoCódigo Capítulo13. Criandosuasprópriasdiretivas
var $scope;
var element;
beforeEach(function() {
module('meusComponentes');
// importando o módulo gerando pelo Karma
module('templates');
// código omitido
});
// código omitido
});
PrecisamosreiniciaroKarma,quelogoemseguidarodaránossoúltimo
teste.Excelente!
Diretivapersonalizadaéumassuntomuitoamploemuitobadaladoem
comunidades. Oleitorpodeseaprofundaraindamaisnoassuntoconsul-
tandoaprópriadocumentaçãodoAngularem https://docs.angularjs.org/
guide/directive.
Nopróximocapítuloveremosaúltimaetapadoworkflowdenossaapli-
cação:odeploy.
337

## Página 351

Capítulo14
Deploydaaplicação
“Just ship, baby”
–KentBack
Nossa aplicação está pronta e devidamente testada, mas onde a
hospedaremos?Emoutraspalavras:ondefaremososeu deploy?Alémdisso,
seráqueprecisaremosconfigurartodaainfraestruturanecessáriaparaque
nossaaplicaçãorode, porexemplo, instalareconfiguraroMongoDBeo
Node.js?
Aprendemosautilizarserviçosnawebcomonossoservidordeintegração
contínuaTraviseoSauceLabs(TaaS),retirandodenós,desenvolvedores,a
responsabilidadedemantê-los. Seráquenãopodemosfazeramesmacoisa
comodeploydaaplicação?Sim,podemos!
Nestecapítulo,aprendemosarealizarodeploydenossaaplicaç ão,mas
antesprecisamosdefinircomquefrequênciaeleserárealizado. Esteéoas-

## Página 352

14.1. Deploycontínuo CasadoCódigo
suntodaprimeirase çãodestecapítulo.
14.1 Deploy contínuo
Nãoéraroodesenvolvedorrealizarodeploydesuaaplicaç ãomanualmente,
porexemplo,parandoaaplicação,abrindoumaconexãoFTP,subindoseus
arquivos,alterandoconfiguraçõesdoambientedeproduç ãoeiniciandoa
aplicaçãonovamente.
Aprendemosaolongodestelivroquetudoqueéfeitomanualmentepelo
serhumanoestásujeitoaerros. Pormaisqueexistaalguémperfeitoque
nuncaerre,ofatortemposerásempreumaconstante. Quantotemposerá
gastopreparandotodoesteprocesso? Quantotempooclienteesperaráaté
receberumnovo releasedaaplicação?
Hoje,acada commit,nossoservidordeintegraç ãodisparao buildda
nossaaplicaçãoeexecutaumasériedetestesparagarantiraqualidadede
nossosoftware. Quetalseapósosucessodenossostestesrealizássemoso
deploydaaplicação? Umcommit,umdeploy! Podeserqueissonãofaç a
sentidodentrodocontextodeoutrasaplicações,masaaplicaç ãoContatooh
temumaestruturaquepermiteisso. Sendoassim,napróximase çãocon-
heceremososerviçoescolhidopararealizarmosodeploydaaplicaç ão.
14.2 OpenShift: platform as a service (PaaS)
OpenShift(http://www.openshift.com/)éuma platform as a service (PaaS)
criadopelaRedHat.UmaPaaSfacilitaodeploydaaplicaç ãoreduzindodras-
ticamenteacomplexidadeenvolvidanoprocesso,inclusiveforneceferramen-
tasquelidamcomosdetalhesdeinfraestruturasemquenospreocupemos
comeles.
Criandosuaconta
Precisamos, antes de mais nada, criar nossa conta emhttp://www.
openshift.com.Vocêreceberáume-mailcomaconfirmaçãodecadastro.De-
pois,bastaselogar,queumapáginadeboas-vindasseráexibida:
340

## Página 354

14.3. Configurandooambientededeploy CasadoCódigo
Usaremos o próprio servidor do OpenShift, por isso podemos teclar
ENTERparaestapergunta.
2) You can add more servers later using 'rhc server'.
Login to openshift.redhat.com: suaConta
Password: *******
O rhcprecisadologinedasenhadesuacontanoOpenShiftparaque
elepossainteragircomsuaaplicação.
3) OpenShift can create and store a token on disk which allows
to you to access the server without using your password. The key
is stored in your home directory and should be kept secret. You
can delete the key at any time by running 'rhc logout'.
Generate a token now? (yes|no) yes
O rhcseencarregarádecriarumachaveparaqueelepossasecomunicar
seguramentecomnossaaplicaçãonoOpenShift,porissoresponderemoscom
yes.Pronto,agorapodemoscriarnossaaplicaç ãonapróximase çãoatravés
do rhc.
14.3 Configurando o ambiente de deploy
Podemoscriarumaaplicaçãopelainterfaceweb,porémamaneiramaisráp-
idaerecomendadaéatravésdo rhc.Comocomando rhc create-app,
criamosnossaaplicação. Elerecebecomoprimeiroparâmetroonomeda
aplicaçãoe,comosegundo,aplataformautilizada. Porfim,podemosadi-
cionarumoumais cartridgesquecorrespondemarecursosdeinfraestru-
turacomooMongoDB.
rhc create-app contatooh nodejs-0.10 mongodb-2.4
O rhccriaráumrepositóriolocalparanossaaplicaçãoqueapontapara
orepositórioremotocriadonoOpenShift(nãoécriadonoGitHub!).Open-
Shiftutilizaogitparaquepossamossubirasalteraçõesdenossaaplicaç ão.
Porém,veremosmaisadiantequenãotrabalharemoscomesserepositório
localmente.AideiaéqueoTravisrealizeautomaticamenteodeploydenosso
projetocasoelepasseemtodosostestes.
342

## Página 356

14.4. Preparandoaaplicaçãoparadeploy CasadoCódigo
Excelente!Sequisermosvisualizarologdaaplicaç ãosempreatualizado
usamosocomando:
rhc tail contatooh
Esserecursoéinteressante,principalmentequandoqueremosdescobrir
problemasnodeploydaaplicação.
14.4 Preparando a aplicação para deploy
Tudooquefizemosatéagoraésuficienteparaodeploy?Comcerteza,não.
Aindafaltasaberqualoendere çodonossobancodedados,odomínioda
aplicação,seuIPeporta.Nãopodemossimplesmentearbitraressesvalores.
ÉporissoqueoOpenShiftdisponibilizaessasinformaçõestambématravés
devariáveisdeambiente,sãoelas:
•OPENSHIFT_MONGODB_DB_URL:endereçodoMongoDBcriado
peloOpenShift;
•OPENSHIFT_NODEJS_PORT: porta que precisaremos adotar em
nossoservidor;
•OPENSHIFT_NODEJS_IP:IPdonossoservidornoOpenShift;
•OPENSHIFT_APP_DNS:domíniodanossaaplicação.
Nosso primeiro passo será criar o arquivo
config/env/production.js, que conterá as configurações do am-
bientedeprodução:
// contatooh/config/env/production.js
module.exports = {
env: 'production',
db: process.env.OPENSHIFT_MONGODB_DB_URL + 'contatooh',
clientID: process.env.CLIENT_ID,
clientSecret: process.env.CLIENT_SECRET,
port: process.env.OPENSHIFT_NODEJS_PORT,
address: process.env.OPENSHIFT_NODEJS_IP,
domain: process.env.OPENSHIFT_APP_DNS
};
344

## Página 357

CasadoCódigo Capítulo14. Deploydaaplicação
Seráqueissoéosuficiente? Oproblemaéquenossaaplicaç ãoainda
nãoestápreparadaparatrabalharcomasconfigurações port, address,
domaine db. Antesderealizarmosqualquermodificaçãomaiscomplexa
naaplicação,vamosalterarosarquivosdeconfiguraç ão development.js
e test.jsparaquefaçamusodosnovosparâmetros:
// contatooh/config/env/development.js
module.exports = {
env: 'development',
db: 'mongodb://localhost/contatooh',
clientID: process.env.CLIENT_ID,
clientSecret: process.env.CLIENT_SECRET,
seleniumUser: process.env.SELENIUM_USER,
seleniumUserPassword: process.env.SELENIUM_USER_PASSWORD,
port: 3000,
address: 'localhost',
domain: 'localhost'
};
Agoraoarquivo test.js:
// contatooh/config/env/test.js
module.exports = {
env: 'test',
db: 'mongodb://localhost/contatooh_test',
clientID: process.env.CLIENT_ID,
clientSecret: process.env.CLIENT_SECRET,
sauceTestName: 'Contatooh E2E Testing',
sauceUser : process.env.SAUCE_USERNAME,
sauceKey : process.env.SAUCE_ACCESS_KEY,
seleniumUser: process.env.SELENIUM_USER,
seleniumUserPassword: process.env.SELENIUM_USER_PASSWORD,
travisJobNumber: process.env.TRAVIS_JOB_NUMBER,
travisBuild: process.env.TRAVIS_BUILD_NUMBER,
port: 3000,
address: 'localhost',
domain: 'localhost'
};
345

## Página 358

14.4. Preparandoaaplicaçãoparadeploy CasadoCódigo
Precisamosalterartodosospontosdanossaaplicaç ãoondetemosesses
valoresfixosesubstituí-lospelovalordenossoobjetodeconfiguraç ão.
Modificandopassport.js
Vamoscomeçarpeloarquivo config/passport.js:
// código anterior comentado
module.exports = function() {
// declarando uma variável para nos ajudar
var githubCallback = 'http://' + config.domain + ':'
+ config.port + '/auth/github/callback';
// código anterior omitido
// realizando a troca
passport.use(new GitHubStrategy({
clientID: config.clientID,
clientSecret: config.clientSecret,
callbackURL : githubCallback
// código posterior omitido
Quando estamos em ambiente de desenvolvimento, nosso
callbackURL apontará para localhost, porém, no ambiente de
produção,apontaráparaodomíniodaaplicaç ão. Oproblemaéquenão
temosumaaplicaçãocadastradanoGithubqueaponteparaestedomínio.
Nase ção 8.2,aprendemosacadastrarumaaplicaç ãonoGitHub,aplicação
àqualdelegamosoprocessodeautenticaç ãodenossosusuário.Precisamos
cadastrarumanova,masqueaponteparaodomíniodaaplicaç ãoqueserá
deployadanoOpenShift:
346

## Página 360

14.5. IntegrandoTraviscomOpenShift CasadoCódigo
ModificandoServer.js
Por fim, vamos alterar a linha que cria nosso servidor no arquivo
server.js:
// contatooh/server.js
// código anterior omitido
// alterando a criação do servidor
http.createServer(app).listen(config.port, config.address,
function(){
console.log('Express Https Server '
+ config.address
+ ' (' + config.env
+ ') escutando na porta ' + config.port);
});
ExperimenterodaraaplicaçãolocalmenteeverificarseoTravisainda
consegueconstruí-la.Tudodevecontinuarfuncionando.Casoalgumprob-
lemaaconteça,verifiqueasalteraçõesanteriores. Émuitocomumerrosde
digitaçãonestaetapa.
Estamosquasepreparadospararealizarmosodeploydanossaaplicaç ão,
porémqueremosqueelasejadeployadapeloTravis,sóassimteremoscerteza
dequeentraránoarumaaplicaçãoquepassouportodososnossostestes,que
sãoacondição sine qua nonparaodeploycontínuo.Veremoscomorealizar
aintegraçãoentreoTraviseoOpenShiftnapróximase ção.
14.5 Integrando Travis com OpenShift
QueremosqueoTravisrealizeodeployautomáticodanossaaplicaç ãono
OpenShiftacadacommit,contantoqueaconstruçãodoprojetopasseporto-
dosostestesdeunidadeee2e.Atéagora,editamosoarquivo .travis.yml
manualmente,maschegouahoradeinstalarmosseuclienteemlinhadeco-
mando,tambémfeitoemRuby,assimcomoo rhc.Instalamosoclienteem
linhadecomandodoTravisatravésdocomando:
sudo gem install travis
348

## Página 361

CasadoCódigo Capítulo14. Deploydaaplicação
Depois,precisamosestardentrodorepositóriodaaplicaç ão(oquecri-
amosnoGit,nãodoOpenShift!).Dentrodorepositório,executaremosoco-
mando:
travis setup openshift
OTravisfaráalgumasperguntasparaquepossaalterarautomaticamente
paranósoarquivo .travis.yml.Oassistenteperguntaráoseuusuáriono
Openshift(email),asenhadasuaconta,onomedaaplicaç ão,odomínio
dasuaaplicação. Perguntarátambémsequeremosrealizarodeployapenas
pelonossorepositórionoGitHub,justamenteoquedesejamos.
Shell completion not installed. Would you like to like to
install it now? |y| y
Detected repository as flaviohenriquealmeida/contatooh, is this
correct? |yes| yes
OpenShift user: seuUsuarioNoOpenShift@seuEmail.com
OpenShift password: *******
OpenShift application name: |contatooh|
OpenShift domain: contatooh-seuDominioNoOpenShift.rhcloud.com
Deploy only from usuarioGitHub/contatooh? |yes| yes
Encrypt Password? |yes| yes
Seeditarmosnossoarquivo contatooh/.travis.yml,veremosasno-
vasconfigurações:
deploy:
provider: openshift
user: seuUsuarioNoOpenShift@seuEmail.com
password:
secure: naoSePreocupeChaveEncriptadaPeloTravis
app: contatooh
domain: 'seuDominioNoOpenShift'
on:
repo: usuarioGitHub/contatooh
Estamosquaselá!Porém,precisamosresolverumproblemaantesdecon-
tinuarmos.Nosso script Gruntfile.jscriaumacópiadoprojetodentro
349

## Página 362

14.5. IntegrandoTraviscomOpenShift CasadoCódigo
dapasta disteissonoscausaráproblemas.OTravisnãoentendequeesta
pastaprecisaseratualizadanorepositóriodanossaaplicaç ãonoOpenShift.
Precisamos alterar a fase before_script do nosso arquivo
.travis.yml,quedeveráficarassim:
before_script:
- node test/data.js
- grunt minifica
Destavez, estamoschamandoocomando grunt minifica nolu-
gardatarefa default,inclusiveremovemosainstruç ãoqueentravanodi-
retório dist. Aconsequênciadissoéqueprecisaremostambémalterar
nosso Gruntfile.jspara que realize todo o processo diretamente na
pasta contatooh. Odesenvolvedorprecisarátomarcuidadoparanãoro-
dar grunt minifica emambientededesenvolvimento,correndoorisco
decomprometerseucódigo.Háoutrasmaneirasdenosprevenirmosquanto
aisso,comoacriaçãodebranches,masnãoentraremosemdetalhes.Nosso
Gruntfile.jsficaráumpoucomaissimples.Suaversãofinalficaráassim:
module.exports = function(grunt) {
grunt.initConfig({
usemin : {
html: 'app/views/**/*.ejs'
},
useminPrepare: {
options: {
root: 'public',
dest: 'public'
},
html: 'app/views/**/*.ejs'
},
ngAnnotate : {
scripts: {
expand: true,
src: ['public/js/**/*.js']
350

## Página 363

CasadoCódigo Capítulo14. Deploydaaplicação
},
}
});
grunt.registerTask('minifica', ['useminPrepare',
'ngAnnotate', 'concat', 'uglify', 'cssmin', 'usemin']);
grunt.loadNpmTasks('grunt-contrib-concat');
grunt.loadNpmTasks('grunt-contrib-uglify');
grunt.loadNpmTasks('grunt-contrib-cssmin');
grunt.loadNpmTasks('grunt-usemin');
grunt.loadNpmTasks('grunt-ng-annotate');
};
Como não usaremos mais o grunt-contrib-copy, nem o
grunt-contrib-clean, podemos desinstalá-los e removê-los de nosso
package.jsoncomocomando:
npm uninstall grunt-contrib-copy grunt-contrib-clean
SevocêestácomeçandocomGitenãosabetrabalharcom branches,
nadaimpedequevocêrealizeumacópiadoseuprojetolocalmenteeex-
ecuteatask grunt minifica paratercertezadequetudoestáfuncio-
nando.
Estamosnopenúltimopasso!Nossoprocessodeminificaç ãoalteraráos
dadosqueoTravistrouxedenossorepositório. Precisamosqueeleasleve
emconsideraçãonafasededeploy.Paraisso,existeafase before_deploy.
Nelacomitaremosasalteraçõesrealizadaspelonossoscript grunt:
before_deploy:
- git config --global user.email 'travis@travis-ci.com'
- git config --global user.name 'Travis CI'
- git checkout $TRAVIS_BRANCH
- git add --all
- git commit -am "Travis commit"
351

## Página 364

14.5. IntegrandoTraviscomOpenShift CasadoCódigo
Realizamosváriasmudançasemnossaaplicaçãoparaadequá-laaoOpen-
Shift,mascomoelesaberáiniciá-la? OOpenShiftsemprechamaráoco-
mando npm start apósodeploytersidorealizado. Paraqueelefun-
cione, precisamos alterar nosso arquivopackage.json modificando a
chave maineadicionandoachave startdentrode scripts:
{
...
"main": "server.js",
"scripts": {
"start": "node server"
"test": "echo \"Error: no test specified\" && exit 1"
}
...
}
Pronto,chegamosaomomentofinal! Vamosrealizarocommitdasal-
terações,masantesdeenviá-lasparanossorepositórionoGitatravésdoco-
mando git push,abriremosumterminalexclusivopararodarmosoco-
mando:
rhc tail contatooh
Lembre-sequeestecomandolerácontinuamenteoarquivodelogdasua
aplicaçãonoOpenShift.
Depoisderealizaro pushdasmodificações,observeaconstruçãodeseu
projetonapáginadoTravis.Depoisdetodosostestesseremexecutados,ele
inicializaráodeploydaaplicação.ComooTravisseintegrafacilmentecom
OpenShift,duranteesseprocessosuaaplicaçãoseráparadaautomaticamente,
osnovosarquivosserãoenviadose,porfim,elaseráinicializada,tudoisso
semsuainterven ção.Bastaacessaroendere çodaaplicaçãoecurtiroresul-
tadofinal:
https://contatooh-nomeDoSeuDominio.rhcloud.com
352

## Página 367

CasadoCódigo ReferênciasBibliográficas
ReferênciasBibliográficas
[1] DirolfChodorow.MongoDB: the definitive guide.2010.
[2] SaladageFowler. NoSQL Destilled, A Brief Guide to the Emerging World
of Polyglot Persistence.2012.
[3] Valeri Karpov.The mean stack: Mongodb, expressjs, angularjs and
node.js.2013.
[4] OddyOsmani.Full-stackjavascriptwithmeanandyeoman.2013.
355