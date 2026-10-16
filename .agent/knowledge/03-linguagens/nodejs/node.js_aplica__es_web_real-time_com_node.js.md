---json
{
  "id": "node-js_aplica__es_web_real-time_com_node-js",
  "title": "Node.js Aplicações web real-time com Node.js",
  "categoria": "03-linguagens",
  "subcategoria": "nodejs",
  "resumo": "**Arquivo Original:** `Node.js Aplicações web real-time com Node.js.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "aplica",
    "com",
    "linguagens",
    "node",
    "node.js",
    "nodejs",
    "real",
    "real-time"
  ],
  "perguntas_tipo": [
    "Como utilizar Node.js Aplicações web real-time com Node.js?",
    "Quais as boas praticas de nodejs?"
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
  "dono": "stack-nodejs",
  "prioridade": 2
}
---

# Node.js Aplicações web real-time com Node.js

> **Arquivo Original:** `Node.js Aplicações web real-time com Node.js.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 2

© Casa do Código
Todos os direitos reservados e protegidos pela Lei nº9.610, de 10/02/1998.
Nenhuma parte deste livro poderá ser reproduzida, nem transmitida, sem auto-
rização prévia por escrito da editora, sejam quais forem os meios: fotográficos,
eletrônicos, mecânicos, gravação ou quaisquer outros.
Casa do Código
Livros para o programador
Rua Vergueiro, 3185 - 8º andar
04101-300 – Vila Mariana – São Paulo – SP – Brasil

## Página 5

CasadoCódigo
Agradecimentos
Primeiramente,queroagradeceraDeusportudoquefizesteemminhavida!Agra-
deçotambémaomeupaieminhamãepeloamor,for ça,incentivoeportodoapoio
desdeomeuiníciodevida.Obrigadoportudoeprincipalmenteporestaraomeu
ladoemtodososmomentos.
UmagradecimentoespecialaminhanamoradaNatáliaSantos,afinalcome ça-
mosanamorarnamesmaépocaquecomeceiestelivro,esuacompanhia,compre-
ensãoeincentivoforamessenciaisparapersistirnesteprojeto.
Agradeçoasra.CharlotteBentodeCarvalho,peloapoioeincentivonosmeus
estudosdesdeaescolaatéaminhaformaturanafaculdade.
UmagradecimentoaomeuprimoCláudioSouza. Foigraç asaelequeentrei
nessemundodatecnologia.Elefoiaprimeirapessoaameapresentarocomputador
emeaconselhouanosdepoisaentraremumafaculdadedeTI.
UmagradecimentoaoBrunoAlvaresdaCosta,LeandroAlvaresdaCostaeLe-
onardoPinto,essescarasmeapresentaramummundonovodaáreadedesenvolvi-
mentodesoftware.Foramelesquemeinfluenciaramaescreverumblog,apalestrar
emeventos,aparticipardecomunidadesefóruns,eprincipalmenteanuncacair
nazonadeconforto,aaprendersempre. Foiumahonratrabalharjuntocomeles
em2011.Ehoje,mesmomuitacoisatendomudado,aindatenhoahonradetraba-
lharcomoLeandronumanovastartupquejáestávirandoumaempresa,queéa
BankFacil.
ObrigadopessoaldaeditoraCasadoCódigo,emespecialaoPauloSilveirae
AdrianoAlmeida.Muitoobrigadopelosuporteepelaoportunidade!
ObrigadogaleradacomunidadeNodeBR.Seus feedbacksajudaramamelhorar
estelivroetambémagrade çoatodososleitoresdoblogUndergroundWebDev.Afi-
nalaessênciadestelivrofoibaseadonospostssobreNode.jspublicadoslá.
Porúltimo,obrigadovocê,prezadoleitor,poradquirirestelivro.Esperoqueeste
livrosejaumaótimareferênciaparati.
i

## Página 7

CasadoCódigo
Comentários
VejaabaixoalgunscomentáriosnoblogUndergroundWebDevarespeitodocon-
teúdoquevocêestaprestesaler.
ParabénspeloPost!Adorei,muitoexplicativo.Acomunidadebrasileiraagradece.
–RafaelHenriqueMoreira-virtualjoker@gmail.com-“http://nodebr.com”
TiveoprazerdetrocarexperiênciaseaprendermuitocomoCaio.Umcarasingularà
“instância”,dotípiconerdqueabraçaumproblemaenãodesgrudaatéresolvê-lo.
Obrigadopelaajudadurantenossotempotrabalhoenãovoudeixardeacompanhar
essasaulas.Parabéns!
–MagnoOzzyr-magno_ozzyr@hotmail.com
DignodereconhecimentooempenhodoCaionoprojetodecontribuircomo
desenvolvimentoepropagaçãodessatecnologia.Issocombinacomoestiloambicioso
epersistentequesempredemonstrounoprocessodeforma ção.Sucesso!Continue
compartilhandoosfrutosdoseutrabalhoparaassimdeixarsuamarcanahistóriada
computação.
–FernandoMacedo-fernando@fmacedo.com.br-“http://fmacedo.com.br”
Ótimoconteúdo,frutodemuitotrabalhoededica ção.ConhecioCaioaindana
faculdade,sempreenérgico,àsvezesimpacienteporcausadesuaânsiapelonovo.
Continueassimbuscandoaprendermaisecompartilhandooquevocêconhececomos
outros.Parabénspelotrabalho!
–ThiagoFerauche-thiago.ferauche@gmail.com
Wow,muitobacanaCaio!EumesmoestouensaiandoparaaprenderJavascriptecia.
HojetrabalhomaiscomHTML/CSS,eessaideiade“paraLeigos”meinteressamuito!
Ficonoaguardodospróximosposts!!=)
–MarcioToledo-mntoledo@gmail.com-“http://marciotoledo.com”
iii

## Página 8

CasadoCódigo
Caião,parabénspelainiciativa,pelotrabalhoepelacontribui çãoparaacomunidade.
Trabalhamosjuntoseseiquevocêéumapessoaextremamentededicadaeansiosopor
novosconhecimentos.Continueassimesucesso!
–LeonardoPinto-leonardo.pinto@gmail.com
Caio,parabénspelocursoepeloconteúdo.Ésemprebomcontarcommaterialde
qualidadeproduzidonoBrasil,poisprecisamosdifundirousodenovastecnologiase
encorajarseuuso.
–EvaldoJunior-evaldojuniorbento@gmail.com-“http://evaldojunior.com.br”
Parabénspelainiciativa!Acreditoquenofuturovocêeoutrosfa çammaiscursosdo
mesmo,semprebuscandocompartilharoconhecimentopraquemqueraprender.
–JadsonLourenço-“http://twitter.com/jadsonlourenco”
iv

## Página 9

CasadoCódigo
Sobreoautor
Figura1:CaioRibeiroPereira
SouWebDeveloper nastartupBankFacil,minhaexperiênciabaseia-senodomínio
dessasopadeletrinhas:Node.js,ModularJavascript,ModularCSS,Ruby,Java,Mon-
goDB,Redis,Agile,FilosofiaLean,Scrum,XP,KanbaneTDD.
BacharelemSistemasdeInformaçãopelaUniversidadeCatólicadeSantos,blo-
gueironostemposlivres,apaixonadoporprogramaç ão,web,tecnologias,filmese
seriados.
Participantedascomunidades:
• NodeBR:ComunidadeBrasileiradeNode.js
• MeteorBrasil:ComunidadeBrasileiradeMeteor
• DevInSantos:GrupodeDesenvolvedoresdeSoftwareemSantos
Inicieiem2011comopalestrantenoseventosDevInSantoseExatec,abordando
temasatuaissobreNode.jseJavascript.
AutordosBlogs:UndergroundWebDeveUndergroundLinux.
v

## Página 11

CasadoCódigo
Prefácio
Asmudançasdomundoweb
Tudonawebsetratadeconsumismoeproduç ãodeconteúdo.Lerouescreverblogs,
assistirouenviarvídeos,veroupublicarfotos,ouvirmúsicaseassimpordiante.Isso
fazemosnaturalmentetodososdiasnainternet.Ecadavezmaisaumentaaneces-
sidadedessainteraçãoentreosusuárioscomosdiversosserviçosdaweb.Defato,o
mundointeiroquerinteragirmaisemaisnainternet,sejaatravésdeconversascom
amigosemchats,jogandogamesonline,atualizandoconstantementesuasredesso-
ciaisouparticipandodesistemascolaborativos.Essestiposdeaplicaçõesrequerem
umpoderdeprocessamentoextremamenteveloz,paraquesejaeficazainteraç ão
emtemporealentreclienteeservidor.Emais,istoprecisaaconteceremumaescala
massiva,suportandodecentenasamilhõesdeusuários.
Entãooquenósdesenvolvedoresprecisamosfazer?Nósprecisamoscriaruma
comunicaçãoemtemporealentreclienteeservidor—quesejarápido,atendamuitos
usuáriosaomesmotempoeutilizerecursosdeI/O(dispositivosdeentradaousaída)
deformaeficiente.Qualquerpessoacomexperiênciadesenvolvimentowebsabeque
oHTTPnãofoiprojetadoparasuportarestesrequisitos.Epior,infelizmenteexis-
temsistemasqueosadotamdeformaineficienteeincorreta,implementandosolu-
çõesworkaround(“Gambiarras”)queexecutamconstantementerequisiçõesassín-
cronasnoservidor,maisconhecidascomo long-polling.Parasistemastrabalharem
emtemporeal,servidoresprecisamenviarereceberdadosutilizandocomunica-
çãobidirecional,aoinvésdeutilizarintensamenterequisiç ãoerespostadomodelo
HTTPatravésdoAjax.Etambémtemosquemanteressetipocomunicaçãodeforma
leveerápidaparamanterescalável,reutilizávelefácildemanterodesenvolvimento
alongoprazo.
Aquemsedestinaesselivro?
Esselivroédestinadoaosdesenvolvedoresweb,quetenhampelomenosconhe-
cimentosbásicosdeJavascriptearquiteturacliente-servidor. Terdomíniodesses
vii

## Página 12

CasadoCódigo
conceitos,mesmoquesejaumconhecimentobásicodeles,seráessencialparaquea
leituradesselivrosejadefácilentendimento.
Comodevoestudar?
Aodecorrerdaleituraserãoapresentadosdiversosconceitosecódigos,paraque
vocêaprendanapráticatodaaparteteóricadolivro. Apartirdocapítulo4atéo
capítulofinal,iremosdesenvolvernapráticaumprojetoweb,utilizandoosprincipais
frameworkseaplicandoasboaspráticasdedesenvolvimentoJavascriptparaNode.js.
viii

## Página 13

CasadoCódigo Sumário
Sumário
1 Bem-vindoaomundoNode.js 1
1.1 Oproblemadasarquiteturasbloqueantes . . . . . . . . . . . . . . . . 1
1.2 EassimnasceuoNode.js . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.3 Single-thread . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.4 Event-Loop . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.5 Instalaçãoeconfiguração . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.6 GerenciandomóduloscomNPM . . . . . . . . . . . . . . . . . . . . . 7
1.7 Entendendoopackage.json . . . . . . . . . . . . . . . . . . . . . . . . . 8
1.8 Escoposdevariáveisglobais . . . . . . . . . . . . . . . . . . . . . . . . 10
1.9 CommonJS,Comoelefunciona? . . . . . . . . . . . . . . . . . . . . . 10
2 Desenvolvendoaplicaçõesweb 13
2.1 Criandonossaprimeiraaplicaçãoweb . . . . . . . . . . . . . . . . . . 13
2.2 Comofuncionaumservidorhttp? . . . . . . . . . . . . . . . . . . . . . 14
2.3 Trabalhandocomdiversasrotas . . . . . . . . . . . . . . . . . . . . . . 15
2.4 SeparandooHTMLdoJavascript . . . . . . . . . . . . . . . . . . . . . 18
2.5 Desafio:Implementarumroteadordeurl . . . . . . . . . . . . . . . . 19
3 Porqueoassíncrono? 21
3.1 Desenvolvendodeformaassíncrona . . . . . . . . . . . . . . . . . . . 21
3.2 AssincronismoversusSincronismo . . . . . . . . . . . . . . . . . . . . 24
3.3 EntendendooEvent-Loop . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.4 EvitandoCallbacksHell . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
ix

## Página 14

Sumário CasadoCódigo
4 IniciandocomoExpress 31
4.1 Porqueutilizá-lo? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
4.2 Instalaçãoeconfiguração . . . . . . . . . . . . . . . . . . . . . . . . . . 32
4.3 Criandoumprojetodeverdade . . . . . . . . . . . . . . . . . . . . . . 33
4.4 Gerandoscaffolddoprojeto . . . . . . . . . . . . . . . . . . . . . . . . 35
4.5 Organizandoosdiretóriosdoprojeto . . . . . . . . . . . . . . . . . . . 38
5 DominandooExpress 43
5.1 Estruturandoviews . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
5.2 Controlandoassessõesdeusuários . . . . . . . . . . . . . . . . . . . . 44
5.3 CriandorotasnopadrãoREST . . . . . . . . . . . . . . . . . . . . . . 49
5.4 Aplicandofiltrosantesdeacessarasrotas . . . . . . . . . . . . . . . . 54
5.5 Indoalém:criandopáginasdeerrosamigáveis . . . . . . . . . . . . . 56
6 Programandosistemasreal-time 61
6.1 Comofuncionaumaconexãobidirecional? . . . . . . . . . . . . . . . 61
6.2 ConhecendooframeworkSocket.IO . . . . . . . . . . . . . . . . . . . 62
6.3 Implementandoumchatreal-time . . . . . . . . . . . . . . . . . . . . 63
6.4 OrganizandoocarregamentodeSockets . . . . . . . . . . . . . . . . . 69
6.5 Socket.IOeExpressemumamesmasessão . . . . . . . . . . . . . . . 70
6.6 Gerenciandosalasdochat . . . . . . . . . . . . . . . . . . . . . . . . . 73
6.7 Notificadoresnaagendadecontatos . . . . . . . . . . . . . . . . . . . 77
6.8 PrincipaiseventosdoSocket.IO . . . . . . . . . . . . . . . . . . . . . . 80
7 Integraçãocombancodedados 83
7.1 BancosdedadosmaisadaptadosparaNode.js . . . . . . . . . . . . . . 83
7.2 MongoDBnoNode.jsutilizandoMongoose . . . . . . . . . . . . . . . 85
7.3 ModelandocomMongoose . . . . . . . . . . . . . . . . . . . . . . . . . 86
7.4 ImplementandoumCRUDnaagendadecontatos . . . . . . . . . . . 87
7.5 PersistindoestruturasdedadoscomNoSQLRedis . . . . . . . . . . . 91
7.6 Mantendoumhistóricodeconversasdochat . . . . . . . . . . . . . . 92
x

## Página 15

CasadoCódigo Sumário
8 Preparandoumambientedetestes 97
8.1 Mocha,oframeworkdetestesparaNode.js . . . . . . . . . . . . . . . 97
8.2 CriandoumEnvironmentparatestes . . . . . . . . . . . . . . . . . . . 98
8.3 InstalandoeconfigurandooMocha . . . . . . . . . . . . . . . . . . . .100
8.4 RodandooMochanoambientedetestes . . . . . . . . . . . . . . . . . 101
8.5 Testandoasrotas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
8.6 Deixandoseustestesmaislimpos . . . . . . . . . . . . . . . . . . . . . 109
9 AplicaçãoNodeemprodu ção 111
9.1 Oquevamosfazer? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
9.2 ConfigurandoClusters . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
9.3 Rediscontrolandoassessõesdaaplicaç ão . . . . . . . . . . . . . . . . 114
9.4 Monitorandoaplicaçãoatravésdelogs . . . . . . . . . . . . . . . . . . 116
9.5 OtimizaçõesnoExpress . . . . . . . . . . . . . . . . . . . . . . . . . . . 118
9.6 OtimizandorequisiçõesdoSocket.IO . . . . . . . . . . . . . . . . . . . 119
9.7 AplicandoSingletonnasconexõesdoMongoose . . . . . . . . . . . . 122
9.8 MantendoosistemanoarcomForever . . . . . . . . . . . . . . . . . . 122
9.9 IntegrandoNginxnoNode.js . . . . . . . . . . . . . . . . . . . . . . . 124
10 Continuandoosestudos 129
ÍndiceRemissivo 131
xi

## Página 17

Capítulo1
Bem-vindoaomundoNode.js
1.1 Oproblema das arquiteturas bloqueantes
Ossistemasparawebdesenvolvidossobreplataforma .NET,Java,PHP,Rubyou
Pythonpossuemumacaracterísticaemcomum:elesparalisamumprocessamento
enquantoutilizamumI/Onoservidor.Essaparalisaç ãoéconhecidacomomodelo
bloqueante(Blocking-Thread).Emumservidorwebpodemosvisualizá-lodeforma
amplaefuncional.Vamosconsiderarquecadaprocessoérequisiç ãofeitapelousuá-
rio. Comodecorrerdaaplicação,novosusuáriosvãoacessando-a,gerandouma
requisiçãonoservidor.Umsistemabloqueanteenfileiracadarequisiç ãoedepoisas
processa,umaauma,nãopermitindomúltiplosprocessamentosdelas. Enquanto
umarequisiçãoéprocessadaasdemaisficamemespera,mantendoporumperíodo
detempoumafiladerequisiçõesociosas.
Estaéumaarquiteturaclássica,existenteemdiversossistemaspeloqualpossui
umdesignineficiente. Égastograndepartedotempomantendoumafilaociosa
enquantoéexecutadoumI/O.Tarefascomoenviare-mail,consultarobancode
dados,leituraemdisco,sãoexemplosdetarefasquegastamumagrandefatiadesse

## Página 18

1.2. EassimnasceuoNode.js CasadoCódigo
tempo,bloqueandoosistemainteiroenquantonãosãofinalizadas.Comoaumento
deacessosnosistema,afrequênciadegargalosserãomaisfrequentes,aumentando
anecessidadedefazerum upgradenoshardwaresdosservidores.Mas upgradedas
máquinaséalgomuitocustoso,oidealseriabuscarnovastecnologiasquefaçambom
usodo hardwareexistente,queutilizemaomáximoopoderdoprocessadoratual,
nãoomantendoociosoquandoomesmorealizartarefasdotipobloqueante.
1.2 E assim nasceu o Node.js
Figura1.1:LogotipodoNode.js.
Foibaseadonesteproblemaque,nofinalde2009,RyanDahlcomaajudainicialde
14colaboradorescriouoNode.js.Estatecnologiapossuiummodeloinovador,sua
arquiteturaétotalmente non-blockingthread (não-bloqueante),apresentandouma
boaperformancecomconsumodememóriaeutilizandoaomáximoedeforma
eficienteopoderdeprocessamentodosservidores,principalmenteemsistemasque
produzemumaaltacargadeprocessamento.UsuáriosdesistemasNodeestãolivres
deaguardarempormuitotempooresultadodeseusprocessos,eprincipalmente
nãosofrerãode dead-locksnosistema,porquenadabloqueiaemsuaplataformae
desenvolversistemasnesseparadigmaésimpleseprático.
Estaéumaplataformaaltamenteescaláveledebaixonível,poisvocêvaiprogra-
mardiretamentecomdiversosprotocolosderedeeinternetouutilizarbibliotecas
queacessamrecursosdosistemaoperacional,principalmenterecursosdesistemas
baseadoemUnix.OJavascriptéasualinguagemdeprogramaç ão,eissofoipossível
graçasàengineJavascriptV8,amesmautilizadanonavegador GoogleChrome.
2

## Página 19

CasadoCódigo Capítulo1. Bem-vindoaomundoNode.js
1.3 Single-thread
Suasaplicaçõesserãosingle-thread,ouseja,cadaaplicaçãoteráinstânciadeumúnico
processo. Sevocêestaacostumadoatrabalharcomprogramaçãoconcorrenteem
plataformamulti-thread,infelizmentenãoserápossívelcomNode,massaibaque
existemoutrasmaneirasdesecriarumsistemaconcorrente,comoporexemplo,
utilizandoclusters(assuntoaserexplicadonocapítulo 9.2),queéummódulonativo
doNode.jseésuperfácildeimplementá-lo. Outramaneiraéutilizaraomáximo
aprogramaçãoassíncrona. Esseseráoassuntomaisabordadoduranteodecorrer
destelivro,peloqualexplicareidiversoscenárioseexemplospráticosemquesão
executadosemparalelofun çõesembackgroundqueaguardamoseuretornoatravés
defunçõesdecallbacketudoissoétrabalhadoformanão-bloqueante.
1.4 Event-L oop
Node.jséorientadoaeventos,elesegueamesmafilosofiadeorientaç ãodeeventos
doJavascriptclient-side;aúnicadiferen çaéquenãoexistemeventosde clickdo
mouse, keyupdotecladoouqualquereventodecomponentesHTML.Naverdade
trabalhamoscomeventosdeI/Odoservidor,comoporexemplo:oevento connect
deumbancodedados,um opendeumarquivo,um datadeum streamingde
dadosemuitosoutros.
OEvent-Loopéoagenteresponsávelporescutareemitireventosnosistema.Na
práticaeleéumloopinfinitoqueacadaiteraçãoverificaemsuafiladeeventosseum
determinadoeventofoiemitido.Quandoocorre,éemitidoumevento.Eleoexecuta
eenviaparafiladeexecutados.Quandoumeventoestáemexecuç ão,nóspodemos
programarqualquerlógicadentrodeleeissotudoacontecegraç asaomecanismode
funçãocallbackdoJavascript.
Odesignevent-drivendoNode.jsfoiinspiradopelosframeworksEventMachine
doRuby(http://rubyeventmachine.com)eTwisteddoPython(http://twistedmatrix.
com).Porém,o Event-loopdoNodeémaisperformáticoporqueseumecanismoé
nativamenteexecutadodeformanão-bloqueante.Issofazdeleumgrandediferencial
emrelaçãoaosseusconcorrentesquerealizamchamadasbloqueantesparainiciaros
seusrespectivos Event-loops.
3

## Página 20

1.5. Instalaçãoeconfiguração CasadoCódigo
1.5 Instalação e configuração
ParaconfiguraroambienteNode.js,independentedequalsistemaoperacionalvocê
utilizar,asdicasserãoasmesmas.Éclaroqueosprocedimentosserãodiferentespara
cadasistema(principalmenteparaoWindows,masnãoseránadagrave).
Figura1.2:PáginadeDownloaddoNode.js.
InstalandoNode.js: Primeiropasso,acesseositeoficial: (http://nodejs.org)
e clique emDownload, para usuários doWindows e MacOSX, basta baixar os
seus instaladores e executá-los normalmente. Para quem já utilizaLinuxcom
PackageManager instalado,acesseesselink(https://github.com/joyent/node/wiki/
Installing-Node.js-via-package-manager)queéreferenteasinstruçõessobrecomo
instalá-loemdiferentessistemas.InstaleoNode.jsdeacordocomseusistema,caso
nãoocorraproblemas,bastaabriroseuterminalconsoleoupromptdecomando
edigitarocomando: node -v && npm -vparaverasrespectivasversõesdo
Node.jseNPM (NodePackageManager) queforaminstaladas.
4

## Página 21

CasadoCódigo Capítulo1. Bem-vindoaomundoNode.js
Figura1.3:VersãodoNode.jseNPMutilizadanestelivro.
A última versão estável utilizada neste livro éNode0.10.22 eNPM1.3.14.
Alias é altamente recomendável utilizar esta versão ou superior, pois recen-
temente foi identificado uma vulnerabilidade de ataqueDoS em versões an-
teriores, veja mais detalhes no blog oficial: (http://blog.nodejs.org/2013/10/22/
cve-2013-4450-http-server-pipeline-flood-dos) Dica: Todo conteúdo deste livro
serácompatívelcomversõesdoNode.js 0.8.0ousuperiores. Configurandoambi-
entededesenvolvimento: Paraconfigurá-lobastaadicionarumavariáveldeam-
bienteNODE_ENVnosistemaoperacional. Emsistemas Linux ou OSX,basta
acessar com um editor de texto qualquer e em modo super user(sudo) o ar-
quivo .bash_profileou .bashrceadicionaroseguintecomando: export
NODE_ENV=’development’.NoWindows7,oprocessoéumpoucodiferente.
5

## Página 22

1.5. Instalaçãoeconfiguração CasadoCódigo
Figura1.4:ConfigurandoavariávelNODE_ENVnoWindows7.
Cliquecombotãodireitonoícone MeuComputador eselecioneaop çãoPro-
priedades,noladoesquerdodajanela,cliquenolink Configuraçõesavançadasdo
sistema.Najanelaseguinte,acesseaaba Avançadoecliquenobotão Variáveisde
Ambiente...,agoranocampo Variáveisdosistemacliquenobotão Novo...,em
nomedavariáveldigite NODE_ENVeemvalordavariáveldigite: development.
Apósfinalizaressatarefareinicieseucomputadorparacarregaressavariávelnosis-
temaoperacional.
RodandooNode: Paratestarmosoambiente,executaremosonossoprimeiro
programaHelloWorld.Executeocomando: nodeparaacessarmosoREPL (Read-
Eval-Print-Loop)quepermiteexecutarcódigoJavascriptdiretamentenoterminal,
digite console.log("Hello World");etecleENTERparaexecutá-lonahora.
6

## Página 23

CasadoCódigo Capítulo1. Bem-vindoaomundoNode.js
Figura1.5:HelloWorldviaREPLdoNode.js
1.6 Gerenciando módulos com NPM
Assimcomoo GemsdoRubyouo MavendoJava,oNode.jstambémpossuioseu
própriogerenciadordepacotes,elesechamaNPM (NodePackageManager). Ele
setornoutãopopularpelacomunidade,quefoiapartirdaversão 0.6.0doNode.js
queeleseintegrounoinstaladordoNode.js,tornando-seogerenciador default.Isto
simplificouavidadosdesenvolvedoresnaépoca,poisfezcomquediversosprojetos
seconvergissemparaestaplataforma.Nãolistareitodos,masapenasoscomandos
principaisparaquevocêtenhano çõesdecomogerenciarmódulosnele:
•npm install nome_do_módulo:instalaummódulonoprojeto.
•npm install -g nome_do_módulo:instalaummóduloglobal.
•npm install nome_do_módulo --save: instalaomódulonoprojeto,
atualizandoo package.jsonnalistadedependências.
•npm list:listatodososmódulosdoprojeto.
•npm list -g:listatodososmódulosglobais.
•npm remove nome_do_módulo:desinstalaummódulodoprojeto.
7

## Página 24

1.7. Entendendoopackage.json CasadoCódigo
•npm remove -g nome_do_módulo:desinstalaummóduloglobal.
•npm update nome_do_módulo:atualizaaversãodomódulo.
•npm update -g nome_do_módulo:atualizaaversãodomóduloglobal.
•npm -v:exibeaversãoatualdonpm.
•npm adduser nome_do_usuário:criaumacontanonpm,atravésdosite
(https://npmjs.org).
•npm whoami: exibedetalhesdoseuperfilpúbliconpm(énecessáriocriar
umacontaantes).
•npm publish: publicaummódulonositedonpm,énecessárioteruma
contaantes.
1.7 Entendendo o package.json
TodoprojetoNode.jséchamadodemódulo,masoqueéummódulo?Nodecorrer
daleitura,percebaquefalareimuitosobreotermomódulo,bibliotecaeframework,
enapráticaelespossuemomesmosignificado.Otermomódulosurgiudoconceito
dequeaarquiteturadoNode.jsémodular.Etodomóduloéacompanhadodeum
arquivodescritor,conhecidopelonomede package.json.
EstearquivoéessencialparaumprojetoNode.js.Um package.jsonmales-
critopodecausarbugsouimpedirofuncionamentocorretodoseumódulo,poisele
possuialgunsatributoschavesquesãocompreendidospeloNode.jseNPM.
Nocódigoabaixoapresentareium package.jsonquecontémosprincipais
atributosparadescreverummódulo:
{
"name": "meu-primero-node-app",
"description": "Meu primeiro app em Node.js",
"author": "Caio R. Pereira <caio@email.com>",
"version": "1.2.3",
"private": true,
"dependencies": {
"modulo-1": "1.0.0",
"modulo-2": "~1.0.0",
"modulo-3": ">=1.0.0"
8

## Página 25

CasadoCódigo Capítulo1. Bem-vindoaomundoNode.js
},
"devDependencies": {
"modulo-4": "*"
}
}
Com esses atributos, você já descreve o mínimo possível o que será
sua aplicação. O atributo name é o principal, com ele você descreve
o nome do projeto, nome pelo qual seu módulo será chamado via função
require('meu-primeiro-node-app'). Em descriptiondescrevemoso
queseráestemódulo. Eledeveserescritodeformacurtaeclaraexplicandoum
resumodomódulo. O authoréumatributoparainformaronomeeemaildo
autor,utilizeoformato: Nome <email>paraquesitescomo(https://npmjs.org)
reconheçacorretamenteessesdados.Outroatributoprincipaléo version,écom
elequedefinimosaversãoatualdomódulo,éextremamenterecomendadoquete-
nhaesteatributo,senãoseráimpossívelinstalaromóduloviacomando npm. O
atributo privateéumbooleano,edeterminaseoprojetoterácódigoabertoou
privadoparadownloadno(https://npmjs.org).
OsmódulosnoNode.jstrabalhamcom 3níveisdeversionamento.Porexem-
plo,aversão 1.2.3estadivididanosníveis: Major(1),Minor(2)ePatch(3).Repare
quenocampo dependenciesforamincluídos4módulos,cadamóduloutilizou
umaformadiferentededefiniraversãoqueseráadicionadanoprojeto.Oprimeiro,
o modulo-1somenteseráincluídosuaversãofixa,a 1.0.0.Utilizeestetipover-
sãoparainstalardependênciascujasuasatualizaçõespossamquebraroprojetopelo
simplesfatodequecertasfuncionalidadesforamremovidaseaindaasutilizamosna
aplicação.Osegundomódulojápossuiumacertaflexibilidadedeupdate.Eleutiliza
ocaractere~quefazatualizaçõesanívelde patch (1.0.x),geralmenteessasatua-
lizaçõessãoseguras,trazendoapenasmelhoriasoucorre çõesdebugs.O modulo-3
atualizaversõesquesejamaiorouiguala 1.0.0emtodososníveisdeversão.Em
muitoscasosutilizar ”>=”podeserperigoso,porqueadependênciapodeseratua-
lizadaanível majorouminor,contendograndesmodificaçõesquepodemquebrar
umsistemaemprodução,comprometendoseufuncionamentoeexigindoquevocê
atualizetodocódigoatévoltaraonormal.Oúltimo,o modulo-4,utilizaocaractere
"*”,estesemprepegaráaúltimaversãodomóduloemqualquernível.Eletambém
podecausarproblemasnasatualizaçõesetemomesmocomportamentodoversio-
namentodo modulo-3.Geralmenteeleéutilizadoem devDependencies,que
sãodependênciasfocadasparatestesautomatizados,easatualizaçõesdosmódulos
9

## Página 26

1.8. Escoposdevariáveisglobais CasadoCódigo
nãoprejudicamocomportamentodosistemaquejáestánoar.
1.8 Escopos de v ariáveis globais
Assimcomonobrowser,utilizamosomesmoJavascriptnoNode.js,eletambém
utilizaescoposlocaiseglobais devariáveis. Aúnicadiferençaécomosãoimple-
mentadosessesescopos.Noclient-sideasvariáveisglobaissãocriadasdaseguinte
maneira:
window.hoje = new Date();
alert(window.hoje);
Emqualquerbrowserapalavra-chave windowpermitecriarvariáveisglobais
quesãoacessadasemqualquerlugar.JánoNode.jsutilizamosumaoutra keyword
paraaplicaressamesmatécnica:
global.hoje = new Date();
console.log(global.hoje);
Aoutilizar globalmantemosumavariávelglobal,acessívelemqualquerparte
doprojetosemanecessidadedechamá-lavia requireoupassá-laporparâmetro
emumafun ção.Esseconceitodevariávelglobaléexistentenamaioriadaslingua-
gensdeprogramação,assimcomosuautilização,peloqualérecomendadotrabalhar
comomínimopossíveldevariáveisglobais,paraevitarfuturosgargalosdememória
naaplicação.
1.9 CommonJS,C omo ele funciona?
ONode.jsutilizanativamenteopadrão CommonJSparaorganizaçãoecarregamento
demódulos.Naprática,diversasfun çõesdestepadrãoseráutilizadacomfrequência
emumprojetoNode.js. Afun ção require('nome-do-modulo')éumexem-
plodisso,elacarregaummódulo. EparacriarumcódigoJavascriptquesejamo-
dularecarregávelpelo require,utilizam-seasvariáveisglobais: exportsou
module.exports. Abaixoapresento-lhedoisexemplosdecódigosqueutilizam
essepadrãodo CommonJS,primeirocrieocódigo hello.js:
module.exports = function(msg) {
console.log(msg);
};
10

## Página 27

CasadoCódigo Capítulo1. Bem-vindoaomundoNode.js
Etambémcrieocódigo human.jscomoseguintecódigo:
exports.hello = function(msg) {
console.log(msg);
};
Adiferençaentreo hello.jseo human.jsestanamaneiradecomoeles
serãocarregados. Em hello.jscarregamosumaúnicafun çãomodulareem
human.jsécarregadoumobjetocomfun çõesmodulares.Essaéagrandediferença
entreeles.Paraentendermelhornapráticacrieocódigo app.jsparacarregaresses
módulos,seguindoocódigoabaixo:
var hello = require('./hello');
var human = require('./human');
hello('Olá pessoal! ');
human.hello('Olá galera!');
Tenhacertezadequeoscódigos hello.js, human.jse app.jsestejamna
mesmapastaerodenoconsoleocomando: node app.js.
Eentão,oqueaconteceu? Oresultadofoipraticamenteomesmo,o app.js
carregouosmódulos: hello.jse human.jsvia require(),emseguidafoi
executadoafun ção hello()queimprimiuamensagem Olá pessoal!eporúl-
timooobjeto humanqueexecutousuafun ção human.hello('Olá galera!').
PercebamoquãosimpleséprogramarcomNode.js!Combasenessespequenos
trechosdecódigojáfoipossívelcriarumcódigoaltamenteescalávelemodularque
utilizaasboaspráticasdopadrão CommonJS.
11

## Página 29

Capítulo2
Desenvolvendoaplicaçõesweb
2.1 Criando nossa primeira aplicação web
Node.jsémultiprotocolo,ouseja,comeleserápossíveltrabalharcomosprotoco-
los:HTTP,HTTPS,FTP,SSH,DNS,TCP,UDP,WebSockets etambémexistemoutros
protocolos,quesãodisponíveisatravésdemódulosnão-oficiaiscriadospelacomu-
nidade.Umdosmaisutilizadosparadesenvolversistemaswebéoprotocolo HTTP.
Defato,éoprotocolocomamaiorquantidadedemódulosdisponíveisparatrabalhar
noNode.js.Napráticadesenvolveremosumsistemawebutilizandoomódulonativo
HTTP,mostrandosuasvantagensedesvantagens.Tambémapresentareisoluçõesde
módulosestruturadosparadesenvolveraplicaçõescomplexasdeformamodulare
escalável.
Todaaplicaçãowebnecessitadeumservidorparadisponibilizartodososseus
recursos.Naprática,comoNode.jsvocêdesenvolveuma "aplicaçãomiddleware”,ou
seja,alémdeprogramarasfuncionalidadesdasuaaplicação,vocêtambémprograma
códigosdeconfiguraçãodeinfraestruturadasuaaplica ção.Inicialmenteissoparece
sermuitotrabalhoso,poisoNode.jsutilizaomínimodeconfiguraçõesparaservir

## Página 30

2.2. Comofuncionaumservidorhttp? CasadoCódigo
umaaplicação,masessetrabalhopermitequevocêcustomizeaomáximooseuser-
vidor. Umavantagemdissoépoderconfiguraremdetalhesosistema,permitindo
desenvolveralgoperformáticoecontroladopeloprogramador.
Casoperformancenãosejaprioridadenodesenvolvimentodoseusistema,reco-
mendoqueutilizealgunsmódulosadicionaisquejávêmcomomínimonecessário
deconfiguraçõesprontasparavocênãoperdertempotrabalhandocomisso.Alguns
módulosconhecidossão: Connect(https://github.com/senchalabs/connect),Ex-
press(http://expressjs.com),Geddy(http://geddyjs.org ),CompoundJS(http:
//compoundjs.com),Sails(http://balderdashy.github.io/sails) .Essesmódulosjá
sãopreparadosparatrabalhardesdeumainfraestruturamínimaatéumamaisen-
xuta,permitindotrabalhardesdearquiteturas RESTFul,padrãoMVC (Model-View-
Controller)etambémcomconexõesreal-timeutilizando WebSockets.
Primeirousaremosapenasomódulonativo HTTP,poisprecisamosentender
todooconceitodessemódulo,vistoquetodososframeworkscitadosacimaouti-
lizamcomoestruturainicialemseusprojetos.Abaixomostroavocêsumaclássica
aplicação HelloWorld. Crieoarquivo hello_server.jscomoseguintecon-
teúdo:
var http = require('http');
var server = http.createServer(function(request, response){
response.writeHead(200, {"Content-Type": "text/html"});
response.write("<h1>Hello World!</h1>");
response.end();
});
server.listen(3000);
Esseéumexemploclássicoesimplesdeumservidornode.js.Eleestásendoexe-
cutadonaporta3000,porpadrãoelerespondeatravésda rotaraiz“/”umresultado
emformatohtmlcomamensagem: Hello World!.
Váparaalinhadecomandoerode node hello_server.js. Façaoteste
acessando,noseunavegador,oendere çohttp://localhost:3000.
2.2 Como funciona um servidor http?
Umservidornode.jsutilizaomecanismo Eventloop,sendoresponsávelporlidar
comaemissãodeeventos.Naprática,afun ção http.createServer()érespon-
sávelporlevantarumservidoreoseucallback function(request, response)
14

## Página 31

CasadoCódigo Capítulo2. Desenvolvendoaplicaçõesweb
apenaséexecutadoquandooservidorrecebeumarequisição.Paraisso,o Eventloop
constantementeverificaseoservidorfoirequisitadoe,quandoelerecebeumare-
quisição,eleemiteumeventoparaquesejaexecutadooseucallback.
ONode.jstrabalhamuitocomchamadasassíncronasquerespondematravés
callbacksdojavascript.Porexemplo,sequisermosnotificarqueoservidorestáde
pé,mudamosalinha server.listenparareceberemparâmetroumafun çãoque
fazesseaviso:
server.listen(3000, function(){
console.log('Servidor Hello World rodando! ');
});
Ométodolistentambéméassíncronoevocêsósaberáqueoservidorestáde
péquandooNodeinvocarsuafun çãodecallback.
SevocêaindaestácomeçandocomJavaScript,podeestranharumpoucoficar
passandocomoparâmetrouma functionportodososlados,masissoéalgomuito
comumnomundoJavascript. Comosintaxealternativa,casooseucódigofique
muitocomplicadoemencadeamentosdediversosblocos,podemosisolá-loemfun-
çõescomnomesmaissignificativos,porexemplo:
var http = require('http');
var atendeRequisicao = function(request, response) {
response.writeHead(200, {"Content-Type": "text/html"});
response.write("<h1>Hello World!</h1>");
response.end();
}
var server = http.createServer(atendeRequisicao);
var servidorLigou = function() {
console.log('Servidor Hello World rodando! ');
}
server.listen(3000, servidorLigou);
2.3 Trabalhando com diversas rotas
Atéagorarespondemosapenasoendere ço/,masqueremospossibilitarquenosso
servidortambémrespondaaoutrosendere ços.Utilizandoumpalavreadocomum
entredesenvolvedoresrails,queremosadicionarnovas rotas.
15

## Página 32

2.3. Trabalhandocomdiversasrotas CasadoCódigo
Vamosadicionarduasnovasrotas,umarota /bemvindoparapáginade“Bem-
vindoaoNode.js!” eumarotagenérica,quelevaparaumapáginadeerro. Fare-
mosissoatravésdeumsimplesencadeamentodecondições,emumnovoarquivo:
hello_server3.js:
var http = require('http');
var server = http.createServer(function(request, response){
response.writeHead(200, {"Content-Type": "text/html"});
if(request.url == "/"){
response.write("<h1>Página principal</h1>");
}else if(request.url == "/bemvindo"){
response.write("<h1>Bem-vindo :)</h1>");
}else{
response.write("<h1>Página não encontrada :(</h1>");
}
response.end();
});
server.listen(3000, function(){
console.log('Servidor rodando! ');
});
Rodenovamenteefaçaotesteacessandoaurl http://localhost:3000/bemvindo,e
tambémacessandoumaoutra,diferentedesta.Viuoresultado?
Reparemnacomplexidadedonossocódigo:oroteamentofoitratadoatravésdos
comandosifeelse,ealeituradeurléobtidaatravésdafun ção request.url()que
retornaumastringsobreoquefoidigitadonabarradeendere çodobrowser.Esses
endereçosutilizampadrõesparacapturarvaloresnaurl. Essespadrõessão: query
strings(?nome=joao)e path(/admin).Emumprojetomaior,tratartodasasurls
dessamaneiraseriatrabalhosoeconfusodemais.NoNode.js,existeomódulonativo
chamado url,queéresponsávelporfazer parsereformataçãodeurls.Acompanhe
comocapturamosvaloresdeumaquerystringnoexemploabaixo.Aproveiteecrie
onovoarquivo url_server.js:
var http = require('http');
var url = require('url');
var server = http.createServer(function(request, response){
response.writeHead(200, {"Content-Type": "text/html"});
response.write("<h1>Dados da query string</h1>");
var result = url.parse(request.url, true);
16

## Página 33

CasadoCódigo Capítulo2. Desenvolvendoaplicaçõesweb
for(var key in result.query){
response.write("<h2>"+key+" : "+result.query[key] +"</h2>");
}
response.end();
});
server.listen(3000, function(){
console.log('Servidor http. ');
});
Nesteexemplo,afun çãourl.parse(request.url,true)fezumparserdaurlobtida
pelarequisiçãodocliente (request.url).
Essemóduloidentificaatravésdoretornodafun çãourl.parser()osseguintes
atributos:
•href: Retorna a url completa: ‘http://user:pass@host.com:8080/p/a/t/h?
query=string#hash’
•protocol:Retornaoprotocolo:‘http’
•host:Retornaodomíniocomaporta:‘host.com:8080’
•auth:Retornadadosdeautenticação:‘user:pass’
•hostname:Retornaodomínio:‘host.com’
•port:Retornaaporta:‘8080’
•pathname:Retornaospathnamesdaurl:‘/p/a/t/h’
•search:Retornaumaquerystring:‘?query=string’
•path: Retorna a concatenação de pathname com query string:
‘/p/a/t/h?query=string’
•query:RetornaumaquerystringemJSON:{‘query’:’string’}
•hash:Retornaancoradaurl:‘#hash’
Resumindo,omódulourlpermiteorganizartodasasurlsdaaplicaç ão.
17

## Página 34

2.4. SeparandooHTMLdoJavascript CasadoCódigo
2.4 Separando oHTML doJav ascript
AgoraprecisamosorganizaroscódigosHTML,eumaboapráticaésepará-losdo
Javascript,fazendocomqueaaplicaçãorenderizecódigoHTMLquandoousuário
solicitarumadeterminadarota.Paraisso,utilizaremosoutromódulonativo FS(File
System).Eleéresponsávelpormanipulararquivosediretóriosdosistemaoperaci-
onal.Omaisinteressantedessemóduloéqueelepossuidiversasfun çõesdemani-
pulaçãotantodeformaassíncronacomodeformasíncrona.Porpadrão,asfun ções
nomeadascomofinal Sync()sãoparatratamentosíncrono.Noexemploabaixo,
apresentoasduasmaneirasdelerumarquivoutilizando FileSystem:
var fs = require('fs');
fs.readFile('/index.html', function(erro, arquivo){
if (erro) throw erro;
console.log(arquivo);
});
var arquivo = fs.readFileSync('/index.html');
console.log(arquivo);
DiversosmódulosdoNode.jspossuemfun çõescomversõesassíncronasesín-
cronas.O fs.readFile()fazumaleituraassíncronadoarquivo index.html.
Depoisqueoarquivofoicarregado,éinvocadoumafun çãocallbackparafazerostra-
tamentosfinais,sejadeerroouderetornodoarquivo.Jáo fs.readFileSync()
realizouumaleiturasíncrona,bloqueandoaaplicaç ãoatéterminarsualeituraere-
tornaroarquivo.
Limitações do FileSystem nos sistemas operacionais
Umdetalheimportantesobreomódulo FileSystem équeelenãoé
100%consistenteentreossistemasoperacionais. Algumasfun çõessão
específicasparasistemasLinux,OSX,Unix eoutrassãoapenaspara Win-
dows.
Paramelhoresinformaçõesleiasuadocumentaç ão: http://nodejs.
org/api/fs.html
Voltando ao desenvolvimento da nossa aplicação, utilizaremos a função
fs.readFile()pararenderizarhtmldeformaassíncrona.Crieumnovoarquivo,
chamado site_pessoal.js,comoseguintecódigo:
18

## Página 35

CasadoCódigo Capítulo2. Desenvolvendoaplicaçõesweb
var http = require('http');
var fs = require('fs');
var server = http.createServer(function(request, response){
// A constante __dirname retorna o diretório raiz da aplicação.
fs.readFile(__dirname + '/index.html', function(err, html){
response.writeHeader(200, {'Content-Type ': 'text/html'});
response.write(html);
response.end();
});
});
server.listen(3000, function(){
console.log('Executando Site Pessoal');
});
Paraqueissofuncione,vocêprecisadoarquivo index.htmldentrodomesmo
diretório.Segueumexemplodehelloquepodeserutilizado:
<!DOCTYPE html>
<html>
<head>
<title>Olá este é o meu site pessoal!</title>
</head>
<body>
<h1>Bem vindo ao meu site pessoal</h1>
</body>
</html>
Rodeo node site_pessoal.jseacessenovamente http://localhost:3000.
2.5 Desafio:Implementar um roteador de url
Antesdefinalizaressecapítulo,queroproporumdesafio.Jáqueaprendemosautili-
zarosmóduloshttp,urlefs(filesystem),quetalreorganizaranossaaplicaç ãopara
renderizarumdeterminadoarquivoHTMLbaseadonopathdaurl?
Asregrasdodesafiosão:
• Crie3arquivosHTML:artigos.html, contato.html e erro.html;
• Coloquequalquerconteúdoparacadapáginahtml;
19

## Página 36

2.5. Desafio:Implementarumroteadordeurl CasadoCódigo
• Aodigitarnobrowseropath:/artigosdeverenderizarartigos.html;
• Aregraanteriortambémseaplicaparaoarquivocontato.html;
• Aodigitarqualquerpathdiferentede /artigose/contatodeverenderizar
erro.html;
• Aleituradosarquivoshtmldeveserassíncrona;
• Arotaprincipal"/”deverenderizarartigos.html;
Algumasdicasimportantes:
1) Utilizeoretornodafun ção: url.parse()paracapturaro pathnamedigitado
erenderizarohtmlcorrespondente. Seo pathnameestivervaziosignificaque
deverenderizarapáginadeartigos,eseestivercomumvalordiferentedonome
dosarquivoshtml,renderizeapáginadeerros.
2) Vocêtambémpodeinserirconteúdohtmlnafunção: response.end(html),
economizando linha de código ao não utilizar a fun ção:
response.write(html).
3) Utilizeafunção: fs.exists(html)paraverificarseexisteohtmlcomo
mesmonomedopathnamedigitado.
Oresultadodessedesafioseencontranapáginagithubdestelivro:
https://github.com/caio-ribeiro-pereira/livro-nodejs/tree/master/desafio-1
20

## Página 37

Capítulo3
Porqueoassíncrono?
3.1 Desenvolvendo de forma assíncrona
Éimportantefocarnousodaschamadasassíncronasquandotrabalhamoscom
Node.js,assimcomoentenderquandoelassãoinvocadas. Ocódigoabaixoexem-
plificaasdiferen çasentreumafun çãosíncronaeassíncronaemrelaç ãoalinhado
tempoqueelasãoexecutadas.Basicamentecriaremosumloopde5iterações,acada
iteraçãoserácriadoumarquivotextocomomesmoconteúdo Hello Node.js!.
Primeirovamoscome çarcomocódigosíncrono.Crieoarquivo text_sync.js
comocódigoabaixo:
var fs = require('fs');
for(var i = 1; i <= 5; i++) {
var file = "sync-txt" + i + ".txt";
var out = fs.writeFileSync(file, "Hello Node.js!");
console.log(out);
}

## Página 38

3.1. Desenvolvendodeformaassíncrona CasadoCódigo
Agoravamoscriaroarquivo text_async.js,comseurespectivocódigo,di-
ferenteapenasnaformadechamarafun ção writeFileSync,queseráaversão
assíncrona writeFile,recebendoumafun çãocomoargumento:
var fs = require('fs');
for(var i = 1; i <= 5; i++) {
var file = "async-txt" + i + ".txt";
fs.writeFile(file, "Hello Node.js!", function(err, out) {
console.log(out);
});
}
Vamos rodar? Execute os comandos:node text_synce depois node
text_async. Seforgerado10arquivosnomesmodiretóriodocódigo-fonte,en-
tãodeutudocerto.Masaexecuç ãodeambosfoitãorápidaquenãofoiperceptível
verasdiferen çasentreo text_asynceo text_sync.Paraentendermelhoras
diferenças,vejaas timelinesqueforamgeradas.O text_syncporserumcódigo
síncrono,invocouchamadasdeI/Obloqueante,gerandoográficoabaixo:
Figura3.1:Timelinesíncronabloqueante.
Reparenotempodeexecução,o text_syncdemorou1000milissegundos,200
milissegundosparacadaarquivocriado.
Jáemtext_asyncforamcriadososarquivosdeformatotalmenteassíncrona,
ouseja,aschamadasdeI/Oeramnão-bloqueantes,sendoexecutadastotalmenteem
paralelo:
22

## Página 39

CasadoCódigo Capítulo3. Porqueoassíncrono?
Figura3.2:Timelineassíncronanão-bloqueante.
Istofezcomqueotempodeexecuç ãolevasse200milissegundos,afinalforam
invocados5vezesemparaleloafun ção fs.writeFile(),maximizandoproces-
samentoeminimizandootempodeexecuç ão.
Threads vs Assincronismos
Pormaisqueasfun çõesassíncronaspossamexecutaremparalelová-
riastarefas,elasjamaisserãoconsideradasuma Thread(porexemploTh-
readsdoJava).Adiferen çaéque Threadssãomanipuláveispelodesen-
volvedor,ouseja,vocêpodepausaraexecu çãodeuma Threadoufazê-la
esperarotérminodeumaoutra.Chamadasassíncronasapenasinvocam
suasfunçõesnumaordemdequevocênãotemcontrole,evocêsósabe
quandoumachamadaterminouquandoseucallbackéexecutado.
Podeparecervantajosoterocontrolesobreas Threadsafavordeum
sistemaqueexecutatarefasemparalelo,maspoucodomíniosobreeles
podetransformarseusistemaemumcaosdetravamentos dead-locks,afi-
nalThreadssãoexecutadasdeformabloqueante.Esteéograndediferen-
cialdaschamadasassíncronas,elasexecutamemparalelosuasfun ções
semtravarprocessamentodasoutraseprincipalmentesembloquearo
sistemaprincipal.
ÉfundamentalqueoseucódigoNode.jsinvoqueomínimopossíveldefun-
çõesbloqueantes.Todafunçãosíncronaimpedirá,naqueleinstante,queoNode.js
continueexecutandoosdemaiscódigosatéqueaquelafun çãosejafinalizada. Por
23

## Página 40

3.2. AssincronismoversusSincronismo CasadoCódigo
exemplo,seessafun çãofizerum I/Oemdisco,elevaibloquearosistemainteiro,
deixandooprocessadorociosoenquantoeleutilizaoutrosrecursosdehardware,
comoporexemploleituraemdisco,utilizaç ãodaredeetc.
Semprequepuder,utilizefun çõesassíncronasparaaproveitaressacaracterística
principaldoNode.js.
Talvezvocêaindanãoestejaconvencido.Apróximase çãovailhemostrarcomo
equandoutilizarbibliotecasassíncronasnão-bloqueantes,tudoissoatravésdeteste
prático.
3.2 Assincronismo versus Sincronismo
Paraexemplificarmelhor,oscódigosabaixorepresentamumbenchmarkcompa-
randootempodebloqueiodeexecuç ãoassíncronavssíncrona.Paraissocrie3ar-
quivos: processamento.js, leitura_async.jse leitura_sync.js.Cri-
aremosisoladamenteocódigo leitura_async.jsquefazleituraassíncrona:
var fs = require('fs');
var leituraAsync = function(arquivo){
console.log("Fazendo leitura assíncrona");
var inicio = new Date().getTime();
fs.readFile(arquivo)
var fim = new Date().getTime();
console.log("Bloqueio assíncrono: "+(fim - inicio)+ "ms");
};
module.exports = leituraAsync;
Emseguidacriaremosocódigo leitura_sync.jsquefazleiturasíncrona:
var fs = require('fs');
var leituraSync = function(arquivo){
console.log("Fazendo leitura síncrona");
var inicio = new Date().getTime();
fs.readFileSync(arquivo);
var fim = new Date().getTime();
console.log("Bloqueio síncrono: "+(fim - inicio)+ "ms");
};
module.exports = leituraSync;
Para finalizar carregamos os dois tipos de leituras dentro do código
processamento.js:
24

## Página 41

CasadoCódigo Capítulo3. Porqueoassíncrono?
var http = require('http');
var fs = require('fs');
var leituraAsync = require('./leitura_async');
var leituraSync = require('./leitura_sync');
var arquivo = "./node.exe";
var stream = fs.createWriteStream(arquivo);
var download = "http://nodejs.org/dist/latest/node.exe";
http.get(download, function(res) {
console.log("Fazendo download do Node.js");
res.on('data', function(data){
stream.write(data);
});
res.on('end', function(){
stream.end();
console.log("Download finalizado!");
leituraAsync(arquivo);
leituraSync(arquivo);
});
});
Rodeocomando node processamento.jsparaexecutarobenchmark. E
agora,ficouclaraadiferen çaentreomodelobloqueanteeonão-bloqueante?
Parecequeométodo readFileexecutoumuitorápido,masnãoquerdizerque
oarquivofoilido. Elerecebeumúltimoparâmetro,queéumcallbackindicando
quandooarquivofoilido,quenãopassamosnainvocaç ãoquefizemos.
Ao usar o fs.readFileSync(), bastaria fazer var conteudo =
fs.readFileSync(). Masqualéoproblemadessaabordagem? Elasegura
todoomecanismodoNode.JS!
Basicamenteestecódigofezodownloaddeumarquivogrande(código-fontedo
node.js)e,quandoterminou,realizouumbenchmarkcomparandoo tempodeblo-
queioentreasfun çõesdeleiturasíncrona (fs.readFileSync())eassíncrona
(fs.readFile())doNode.js.
Abaixoapresentooresultadodobenchmarkrealizadoemminhamáquina:
• Modelo:MacBookAir2011
• Processador:Corei5
• Memória:4GBRAM
25

## Página 42

3.3. EntendendooEvent-Loop CasadoCódigo
• Disco:128GBSSD
Vejaapequena,porémsignificantediferen çadetempoentreasduasfun çõesde
leitura.
Figura3.3:BenchmarkdeleituraAsyncvsSync.
Seessetestefoicomumarquivodemaisoumenos50MB,imagineesseteste
emlargaescala,lendomúltiplosarquivosde1GBaomesmotempoourealizando
múltiplosuploadsemseuservidor?EsseéumdospontosfortesdoNode.js!
3.3 Entendendo o Event-L oop
Realmentetrabalhardeformaassíncronatemótimosbenefíciosemrelaç ãoaproces-
samentoI/O.Issoacontecedevidoaofato,dequeumachamadadeI/Oéconsiderada
umtarefamuitocustosaparaumcomputadorrealizar.Tãocustosaquechegaaser
perceptívelparaumusuário,porexemplo,quandoeletentaabrirumarquivode1
GBeosistemaoperacionaltravaalgunssegundosparaabri-lo.Vendoocontextode
umservidor,pormaispotentequesejaseu hardware,elesterãoosmesmosbloqueios
perceptíveispelousuário,adiferençaéqueumservidorestarálidandocommilhares
usuáriosrequisitandoI/O,comagrandeprobabilidadedeseraomesmotempo.
ÉporissoqueoNode.jstrabalhacomassincronismo.Elepermitequevocêde-
senvolvaumsistematotalmenteorientadoaeventos,tudoissograç asao Event-loop.
Eleéummecanismointerno,dependentedasbibliotecasdalinguagemC: libev
(http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod)e libeio(http://software.
schmorp.de/pkg/libeio.html),responsáveisporproveroassíncronoI/OnoNode.js.
AilustraçãoabaixoapresentacomofuncionaoEvent-Loop:
26

## Página 43

CasadoCódigo Capítulo3. Porqueoassíncrono?
Figura3.4:Event-LoopdoNode.js.
Basicamenteeleéumloopinfinito,queemcadaiteraç ãoverificaseexistemno-
voseventosemsua filadeeventos.Taiseventossomenteaparecemnestafilaquando
sãoemitidosdurantesuasinteraçõesnaaplicação.O EventEmitter,éomódulo
responsávelporemitireventoseamaioriadasbibliotecasdoNode.jsherdamdeste
módulosuasfuncionalidadesdeeventos. Quandoumdeterminadocódigoemite
umevento,omesmoéenviadoparaa filadeeventos paraqueo Event-loopexecute-
o,eemseguidaretorneseu callback.Talcallbackpodeserexecutadoatravésdeuma
funçãodeescuta,semanticamenteconhecidapelonome: on().
Programarorientadoaeventosvaimantersuaaplicaç ãomaisrobustaees-
truturadaparalidarcomeventosquesãoexecutadosdeformaassíncronanão-
bloqueantes. Paraconhecermaissobreasfuncionalidadesdo EventEmitter
acessesuadocumentação:
http://nodejs.org/api/events.html
27

## Página 44

3.4. EvitandoCallbacksHell CasadoCódigo
3.4 EvitandoCallbacksHell
Defato,vimosoquantoévantajosoeperformáticotrabalhardeformaassíncrona,
porémemcertosmomentos,inevitavelmenteimplementaremosdiversasfun çõesas-
síncronas,queserãoencadeadasumanaoutraatravésdassuasfun çõescallback.
Nocódigoaseguirapresentareiumexemplodessecaso.Crieumarquivochamado
callback_hell.js,implementeeexecuteocódigoabaixo:
var fs = require('fs');
fs.readdir(__dirname, function(erro, contents) {
if (erro) { throw erro; }
contents.forEach(function(content) {
var path = './' + content;
fs.stat(path, function(erro, stat) {
if (erro) { throw erro; }
if (stat.isFile()) {
console.log('%s %d bytes ', content, stat.size);
}
});
});
});
Reparemnaquantidadedecallbacksencadeadosqueexistememnossocódigo.
Detalhe:eleapenasfazumasimplesleituradosarquivosdeseudiretórioeimprime
natelaseunomeetamanhoembytes. Umpequenatarefacomoessadeveriater
menosencadeamentos,concorda? Agora,imaginecomoseriaaorganizaç ãodisso
pararealizartarefasmascomplexas?Praticamenteoseucódigoseriaumcaosetotal-
mentedifícildefazermanuten ções.Porserassíncrono,vocêperdeocontroledoque
estáexecutandoemtrocadeganhoscomperformance,porém,umdetalheimpor-
tantesobreassincronismoéquenamaioriadoscasososcallbacksbemelaborados
possuemcomoparâmetroumavariáveldeerro.Verifiquenasdocumentaçõessobre
suaexistênciaesemprefaçaotratamentodelesnaexecuç ãodoseucallback: if
(erro) { throw erro; },issovaiimpediracontinuaçãodaexecuçãoaleatória
quandoforidentificadoumerro.
UmaboapráticadecódigoJavascriptécriarfun çõesqueexpressemseuob-
jetivo e de forma isoladas, salvando em variável e passando-as como callback.
Ao invés de criar funções anônimas, por exemplo, crie um arquivo chamado
callback_heaven.jscomocódigoabaixo:
28

## Página 45

CasadoCódigo Capítulo3. Porqueoassíncrono?
var fs = require('fs');
var lerDiretorio = function() {
fs.readdir(__dirname, function(erro, diretorio) {
if (erro) return erro;
diretorio.forEach(function(arquivo) {
ler(arquivo);
});
});
};
var ler = function(arquivo) {
var path = './' + arquivo;
fs.stat(path, function(erro, stat) {
if (erro) return erro;
if (stat.isFile()) {
console.log('%s %d bytes ', arquivo, stat.size);
}
});
};
lerDiretorio();
Vejaoquantomelhoroualegibilidadedoseucódigo. Dessaformadeixamos
maissemânticoelegívelonomedasfun çõesediminuímosonúmerodeencade-
amentosdasfun çõesdecallback. Aboapráticaéterobomsensodemanterno
máximoatédoisencadeamentosdecallbacks.Aopassardissosignificaqueestána
horadecriarumafun çãoexternaparaserpassadacomoparâmetronoscallbacks,
emvezdecontinuarcriandoum callbackhellemseucódigo.
29

## Página 47

Capítulo4
IniciandocomoExpress
4.1 Por que utilizá-lo?
ProgramarutilizandoapenasaAPIHTTPnativaémuitotrabalhoso! Conforme
surgemnecessidadesdeimplementarnovasfuncionalidades,códigosgigantescosse-
riamacrescentados,aumentandoacomplexidadedoprojetoedificultandofuturas
manutenções.
Foiapartirdesseproblemaquesurgiuumframeworkmuitopopular,quese
chamaExpress.Eleéummóduloparadesenvolvimentodeaplicaçõeswebdegrande
escala.SuafilosofiadetrabalhofoiinspiradapeloframeworkSinatradalinguagem
Ruby.Ositeoficialdoprojetoé:(http://expressjs.com).

## Página 48

4.2. Instalaçãoeconfiguração CasadoCódigo
Figura4.1:FrameworkExpress.
Elepossuiasseguintescaracterísticas:
• MVR(Model-View-Routes);
• MVC(Model-View-Controller);
• Roteamentodeurlsviacallbacks;
• Middleware;
• InterfaceRESTFul;
• SuporteaFileUploads;
• Configuraçãobaseadoemvariáveisdeambiente;
• Suporteahelpersdinâmicos;
• Integraçãocom TemplateEngines;
• IntegraçãocomSQLeNoSQL;
4.2 Instalação e configuração
Suainstalaçãoémuitosimpleseháalgumasop çõesdeconfiguraçõesparacomeçar
umprojeto. Paraaproveitartodososseusrecursos,recomendoqueinstale-oem
modoglobal:
npm install -g express
32

## Página 49

CasadoCódigo Capítulo4. IniciandocomoExpress
Feitoisso,seránecessáriofechareabrirseuterminalparahabilitarocomando
express,queéum CLI(CommandLineInterface) doframework.Elepermitegerar
umprojetoinicialcomsuporteasessões,Templateengine(porpadrãoeleincluio
frameworkJade)eumCSSengine(porpadrãoeleutilizaCSSpuro).Paravisualizar
todasasop çõesexecuteocomando: express -h
Figura4.2:Op çõesdoExpressemmodoCLI.
4.3 Criando um projeto de verdade
VamoscriarumaaplicaçãodeverdadecomExpress?Dessavez,criaremosumpro-
jetoqueserátrabalhadoduranteosdemaiscapítulosdolivro, ecriaremosuma
agendadecontatosemqueseuscontatosserãointegradosemumwebchatfun-
cionandoemreal-time.
Osrequisitosdoprojetosão:
• Ousuáriodevecriar,editarouexcluirumcontato;
• Ousuáriodeveselogarinformandoseunomeee-mail;
• Ousuáriodeveconectaroudesconectarnochat;
• Ousuáriodeveenviarerecebermensagensnochatsomenteentreoscontatos
online;
OnomedoprojetoseráNtalk (Nodetalk)eutilizaremosasseguintestecnologias:
•Node.js:Backenddoprojeto;
•MongoDB:BancodedadosNoSQLorientadoadocumentos;
33

## Página 50

4.3. Criandoumprojetodeverdade CasadoCódigo
•Redis:BancodedadosNoSQLparaestruturasdechave-valor;
•Express:Frameworkparaaplicaçõesweb;
•Socket.IO:Móduloparacomunicaçãoreal-time;
•MongooseJS:ODM (ObjectDataMapper) MongoDBparaNode.js;
•NodeRedis:ClienteRedisparaNode.js;
•EJS:Templateengineparaimplementaçãodehtmldinâmico;
•Mocha:Frameworkparatestesautomatizados;
•SuperTest:Móduloparaemularrequisi çõesqueseráutilizadonotestedein-
tegração;
•Nginx:ServidorWebdealtaperformanceparaarquivosestáticos;
Exploraremosestastecnologiasnodecorrerdessescapítulos,entãomuitacalma
eboaleitura!
Casovocêestejacompressadeveresteprojetorodando, vocêpodecloná-
lo através do meu repositório público: (https://github.com/caio-ribeiro-pereira/
livro-nodejs).
Parainstalá-loemsuamáquinafaçaoscomandosaseguir:
git clone git@github.com:caio-ribeiro-pereira/livro-nodejs.git
cd livro-nodejs/projeto/ntalk
npm install
npm start
Edepoisacessenoseunavegadorfavoritooendere ço:
http://localhost:3000
Agorasevocêqueraprenderpassoapassoadesenvolveresteprojeto,continue
lendoestelivro,seguindotodasasdicasqueireipassar.
CriaremosodiretóriodaaplicaçãojácomalgunsrecursosdoExpressqueége-
radoapartirdeseuCLI.Paracome çar,executeosseguintescomandos:
express ntalk --ejs
cd ntalk
npm install
Parabéns!Vocêacaboudecriaroprojeto ntalk.
34

## Página 51

CasadoCódigo Capítulo4. IniciandocomoExpress
4.4 Gerando scaffold do projeto
Aoacessarodiretóriodoprojeto,vejacomofoigeradooseu scaffold:
Figura4.3:EstruturadoExpress.
•package.json:contémasprincipaisinformaçõessobreaaplicaçãocomo:
nome,autor,versão,colaboradores,url,dependênciasemuitomais.
•public: pastapúblicaquearmazenaconteúdoestático,porexemplo: ima-
gens,css,javascriptetc.
•app.js: arquivoqueinicializaoservidordoprojeto,atravésdocomando:
node app.js.
•routes:diretórioquemantémtodasasrotasdaaplicaç ão.
•views:diretórioquecontémtodasas viewsquesãorenderizadaspelasrotas.
Aorodarmosocomando npm install,porpadrãoeleinstalouasdependên-
ciasexistentesno package.json.Nestecaso,eleapenasinstalouoExpresseoEJS
(EmbeddedJavascript).
Vamosfazeralgumasalteraçõesnoscódigosgeradospelo scaffolddoExpress.O
primeiropassoserácriarumadescriçãosobreonossoprojetoedefinir falseo
atributo private.Issotudoserámodificadonoarquivo package.json,vejao
códigoabaixocomoficou:
35

## Página 52

4.4. Gerandoscaffolddoprojeto CasadoCódigo
{
"name": "ntalk",
"description": "Node talk - Agenda de contatos",
"private": false,
"version": "0.0.1",
"scripts": {
"start": "node app.js"
},
"dependencies": {
"express": "3.4.7",
"ejs": "0.8.5"
}
}
Tambémmodificaremoso app.js,deixando-ocomomínimodecódigopos-
sívelparaexplicarmosem baby-stepsoquerealmenteseránecessárionodesenvolvi-
mentodesteprojeto.Recomendoqueapagueocódigogeradopelo scaffoldecoloque
ocódigoabaixo:
var express = require('express')
, routes = require('./routes');
var app = express();
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
app.use(express.static(__dirname + '/public'));
app.get('/', routes.index);
app.get('/usuarios', routes.user.index);
app.listen(3000, function(){
console.log("Ntalk no ar.");
});
Essaversãoinicialmenteatendeosrequisitosmínimosdeumaaplicaç ãoExpress.
Abrincadeiracome çaquandoexecutamosafun ção express(),poisoseuretorno
habilitatodasassuasfuncionalidadesdeseuframework,peloqualarmazenamosna
variávelapp.
Com app.listen()fazemosalgoparecidocomo http.listen(),ouseja,
eleéumaliasresponsávelporcolocaraaplicaçãonoar.
36

## Página 53

CasadoCódigo Capítulo4. IniciandocomoExpress
Osmétodos app.get(), app.post(), app.put() e app.del()são
funçõesderoteamento,cadaumadelasassociaseusrespectivosmétodosdopro-
tocoloHTTP (GET,POST,PUTeDELETE).Seuprimeiroparâmetroéumastring
referenteaumarotadaaplicaç ãoeosegundoéumafun çãocallbackquecon-
tém uma requisição e uma resposta. Exemplo: app.get('/contatos',
function(request, response));
O app.set(chave, valor) é uma estrutura de chave e valor man-
tida dentro da variávelapp. Seria o mesmo que criar no javascript o có-
digo: app["chave"] = "valor";. Um exemplo prático são as configura-
çõesde viewsqueforamdefinidosnocódigoanterior: (app.set('views',
'/views'))e (app.set('view engine', 'ejs')).
Amaioriadasfun çõeschamadasdiretamentepelavariável expresssãoher-
dadasdeseussubmódulos Connecte HTTP.
Detalhes sobreConnect
O Connect (https://github.com/senchalabs/connect) é um mid-
dlewareparaservidoresHTTP.Comeleépossívelconfiguraraspectos
doservidoratravésdoconceitodepilha,ouseja,osprimeirositensin-
seridossãoosprimeirosaseremexecutadosantesdechegarnasfun ções
callbacksdasrotas.OExpressherdoutodasasfuncionalidadesdoCon-
nect,porissoérecomendávelcompreenderaordemreferenteaositens
aseremincluídosno stackdeconfigurações. Casovocênãorespeitea
ordemdeinser çãodecadaelemento,suaaplicaçãonãoirásecomportar
bem,gerandoerrosinesperadosounãorealizandotaisrotinasquefo-
ramestabelecidas.Paraisso,énecessáriosempredarumaolhadanado-
cumentação(http://www.senchalabs.org/connect)parasabermaissobre
essesitensetambémsobreaordemdecadaum.Umdetalheimportante
équenaprópriadocumentaçãoessesitensjáestãolistadosnaordemem
quecadaumdeveserincluídona stackdesuaaplicação.
Emnossaaplicaçãoapenasinserimosdoisitensna stackdeconfigurações:otem-
plateengineEJS(EmbeddedJavaScript)eodiretóriodearquivosestáticos.Nodecor-
rerdestelivroserãoincluídoseexplicadosnovositensnonossoprojeto.
Também deixei apenas duas rotas:/ e /usuarios, repare em como
foram executados os seus callbacks; eles vieram da variávelvar routes =
37

## Página 54

4.5. Organizandoosdiretóriosdoprojeto CasadoCódigo
require('./routes')peloqualfoichamadoumdiretórioenãoumcódigoja-
vascript.
Pordefault,achamada routes.indexbuscaoarquivo index.jsquecon-
tenhaafun ção: exports.index,estaéumaconven çãodoExpressparaincluira
rotaraizdaaplicação.Jáo routes.users.indexseguiuaregranormaldecarre-
gamentodoarquivo users.jsesuarespectivafun ção exports.index.
4.5 Organizando os diretórios do projeto
Quandooassuntoéorganizaçãodecódigos,oExpresssecomportadeformabem
flexíveleliberal. Apesardeutilizaroseu scaffolddegeraçãoinicial,temosatotal
liberdadedemodificarsuaestruturadediretóriosearquivos.Tudovaidependerda
complexidadedoprojeto.Porexemplo,seoprojetoforumsistema single-page,você
podedesenvolvertodobackenddentrocódigo app.js,ouseoprojetopossuirdi-
versasrotas,views,modelsecontrollers,oidealseriamontarumaestruturamodular
utilizandoo patternMVC(Model-View-Controller).
EmnossoprojetoutilizaremosopadrãoMVC,paraissofaltacriarosseguinte
diretórios: modelse controllers,deixandosuaestruturadessaforma:
Figura4.4:Estruturadediretóriosdontalk.
Cadamodelqueforutilizadoemum controllerrealizaráumachamadaafun-
ção require('/models/nome-do-model');.Em controllers,ouqualquerou-
38

## Página 55

CasadoCódigo Capítulo4. IniciandocomoExpress
trocódigo,diversaschamadasafun ção requireserãorealizadaseissovaigerar
umapoluiçãonoscódigos.Oidealéutilizarmosapenasparachamadasdemódulos
externosouutilizarcomfrequênciaafun ção requiredentrode app.js. Com
basenesseproblema,surgiuum pluginquevisaminimizaressaschamadas,elese
chamaexpress-load,sendoresponsávelpormapeardiretóriosparacarregareinje-
tarmódulosdentrodeumavariávelquedefinirmosnafun ção into.Paraentender
melhoroqueseráfeito,adicione-ocomodependênciano package.json:
"dependencies": {
"express": "3.4.7",
"express-load": "1.1.8",
"ejs": "0.8.5"
}
Façaumupdatedosmódulosparainstalaro express-load,executandoo
comando: npm install.
Agorafaremosum refactoringno app.jsparaimplementarmosestemóduloe
utilizarmossuafun ção load():
var express = require('express')
, load = require('express-load')
, app = express();
// ...stack de configurações do servidor...
load('models')
.then('controllers')
.then('routes')
.into(app);
// ...app.listen(3000)...
Éimportantecolocaremordemosrecursosaseremcarregadospelafun ção
load(). Nestecasoos modelssãocarregadosprimeiro,emseguidavêmos con-
trollers,eporúltimoos routes.
Continuandoo refactoring, excluaoarquivo routes/user.jsquefoige-
rado pelo Express. E o códigoroutes/index.js, vamos renomeá-lo para
routes/home.js.Nelevamosincluiroseguintecódigo,queseráumaadaptaç ão
paraqueeleutilizeavariável appvindado express-load:
39

## Página 56

4.5. Organizandoosdiretóriosdoprojeto CasadoCódigo
module.exports = function(app) {
var home = app.controllers.home;
app.get('/', home.index);
};
O express-load criou um objeto chamadocontrollers dentro de
app. Ele cria uma estrutura de objetos de acordo com o diretório e ar-
quivo. Nestecasoo app.controllers.homeestasereferenciandoaoarquivo
controllers/home.js. Agoraparaestarotafuncionarcorretamente, vamos
criarocontroller home.jseincluirsuaprimeira actionchamadade index,se-
guindooexemploabaixo:
module.exports = function(app) {
var HomeController = {
index: function(req, res) {
res.render('home/index');
}
};
return HomeController;
};
Pronto!Parafinalizarofluxoentre routese controllers,excluaoarquivo
views/index.ejsecrieodiretório views/home.Anossahomepageseráuma
simplesteladeloginparaacessarosistema. Parafinsilustrativosafuturalógica
desseaplicativoserádeimplementarumloginqueautocadastraumnovousuário,
quandoforinformadoumloginnovonosistema.Em views/homecrieoarquivo
index.ejs,peloqualimplementaremosumformulárioqueconteráoscampos
nomee email.Vejacomoseráesta viewcombasenaimplementaçãoabaixo:
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Ntalk - Agenda de contatos</title>
</head>
<body>
<header>
<h1>Ntalk</h1>
<h4>Bem-vindo!</h4>
</header>
<section>
40

## Página 57

CasadoCódigo Capítulo4. IniciandocomoExpress
<form action="/entrar" method="post">
<input type="text" name="nome" placeholder="Seu nome">
<br>
<input type="text" name="email" placeholder="Seu e-mail">
<br>
<button type="submit">Entrar</button>
</form>
</section>
<footer>
<small>Ntalk - Agenda de contatos</small>
</footer>
</body>
</html>
Vamosrodaroprojeto?Executenoterminalocomando: node app.js,em
seguidaacesseemseu browseroendereço:http://localhost:3000Setudodeucerto
vocêveráumatelacomformuláriosemelhanteaimagemabaixo:
Figura4.5:TeladelogindoNtalk.
Umdetalheainformar,nosexemplosdestelivronãoseráimplementadocódigo
cssouboaspráticasdehtml,poisvamosfocarapenasemcódigoJavascript.Algumas
imagensdoprojetoserãoapresentadoscomumlayoutcustomizado.Aversãocom-
pletadesteprojetoqueincluiocódigoCSSeHTMLdeacordocomos screenshots
podeseracessadaatravésdolinkdomeugithub:
http://github.com/caio-ribeiro-pereira/livro-nodejs/tree/master/projeto/ntalk
41

## Página 58

4.5. Organizandoosdiretóriosdoprojeto CasadoCódigo
Parabéns!Acabamosdeimplementarofluxodatelainicialdoprojeto.
42

## Página 59

Capítulo5
DominandooExpress
5.1 Estruturando views
OmóduloEJSpossuidiversasfuncionalidadesquepermitemprogramarconteúdo
dinâmicoemcódigohtml. Nãoentraremosafundonesteframework,apenasuti-
lizaremosseusprincipaisrecursospararenderizarconteúdodinâmicoeminimizar
repetiçõesdecódigo.Comisso,isolaremosemoutras views,conhecidascomo par-
tials,possíveiscódigosqueserãoreutilizadoscommaiorfrequência.Dentrododi-
retório views,vamoscriardoisarquivosqueserãoreaproveitadosnahomepage.O
primeiroseráocabeçalhocomonome header.ejs:
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Ntalk - Agenda de contatos</title>
</head>
<body>

## Página 60

5.2. Controlandoassessõesdeusuários CasadoCódigo
Eosegundoseráorodapé footer.ejs:
<footer>
<small>Ntalk - Agenda de contatos</small>
</footer>
</body>
</html>
Agoramodificaremosanossahomepage,a views/home/index.ejsparaque
chamemesses partialsatravésdafunção include:
<% include ../header %>
<header>
<h1>Ntalk</h1>
<h4>Bem-vindo!</h4>
</header>
<section>
<form action="/entrar" method="post">
<input type="text" name="usuario[nome]"
placeholder="Digite o nome">
<br>
<input type="text" name="usuario[email]"
placeholder="Digite o e-mail">
<br>
<button type="submit">Entrar</button>
</form>
</section>
<% include ../footer %>
Agoraasuahomepageficoumaisenxuta,fácildelereestruturadaparareutili-
zaçãode partials.
5.2 Controlando as sessões de usuários
Paraosistemafazer loginelogouténecessárioterumcontroledesessão.Essecon-
trolepermitiráqueousuáriomantenhaseusprincipaisdadosdeacessoemmemória
noservidor,poisessesdadosserãoutilizadoscommaiorfrequênciaporgrandeparte
dosistema.Trabalharcomsessãoémuitosimples,eosdadossãomanipuladosatra-
vésdeobjetoJSONdentrodavariável: req.session.
44

## Página 61

CasadoCódigo Capítulo5. DominandooExpress
Vamosaplicarumcontroledesessão?.Primeiro,temosquecriarduasnovasro-
tasdentrode routes/home.js,sendoqueumaseráo app.post('/entrar',
home.login)eaoutra app.get('/sair', home.logout):
module.exports = function(app) {
var home = app.controllers.home;
app.get('/', home.index);
app.post('/entrar', home.login);
app.get('/sair', home.logout);
};
Depoisimplementaremossuasrespectivas actionsno controller/home.js,
seguindo a convenção de nomeslogin e logout, que foram utilizados no
routes/home.js.Na actionlogin seráimplementadaumasimplesregradevali-
daçãodoscampos nomee emailvindosdoformulário.Seoscampospassaremna
validação,essesdadosserãoarmazenadosnasessãoem req.session.usuario,
assimcomocriarmosumarrayvazio( usuario['contatos'] = [];)decon-
tatosparanofuturoutilizá-lonagestãodecontatos. Emseguidaseráfeitoum
redirecionamento para rota/contatos. Na action logouté chamada a função:
req.session.destroy(),queirálimparosdadosdasessãoegerarumanova.
module.exports = function(app) {
var Usuario = app.models.usuario;
var HomeController = {
index: function(req, res) {
res.render('home/index');
},
login: function(req, res) {
var email = req.body.usuario.email
, nome = req.body.usuario.nome;
if(email && nome) {
var usuario = req.body.usuario;
usuario['contatos'] = [];
req.session.usuario = usuario;
res.redirect('/contatos');
} else {
res.redirect('/');
}
},
logout: function(req, res) {
45

## Página 62

5.2. Controlandoassessõesdeusuários CasadoCódigo
req.session.destroy();
res.redirect('/');
}
};
return HomeController;
};
Vamostestaressaimplementação? Dêumrestartnoservidor. Paraissofina-
lizeoservidoratualteclandonoterminal CTRL+C(noWindowsouLinux)ou
Command+C(noMacOSX),emseguidaexecute node app.jsedepoisemseu
browsertentefazerumloginnosistema.
Figura5.1:Infelizmentedeumensagemdeerro.
Oquehouve? Euimplementeitudocerto! Então,meuamigo,esseerroacon-
teceuporquefaltouhabilitarumnovoitemna stackdeconfigurações. Esseitemé
responsávelporreceberosdadosdoformuláriohtmlefazerum parserparaobjeto
JSON,afinalelenãoreconheceuoobjeto req.body.usuario.Jáadiantando,tam-
bémvamosincluirnastackumcontroledesessãoecookiesparaquenapróximavez
tudofuncionecorretamente.Abaixosegueemordemcorretaosnovositensda stack
deconfiguraçõesdonossoservidor:
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
app.use(express.cookieParser('ntalk'));
app.use(express.session());
app.use(express.json());
app.use(express.urlencoded());
app.use(express.static(__dirname + '/public'));
46

## Página 63

CasadoCódigo Capítulo5. DominandooExpress
É necessário incluir o express.cookieParser(), pois o
express.session() utiliza-o para codificar e ou decodificar oSessionID
que foi persistido no cookie. Outra configurações habilitadas foram o
express.json() e express.urlencoded(), que são responsáveis
por criar objetos JSON vindos de um formulário HTML. Ele
cria um objeto através dos atributos name e value, existentes
nas tags <input> , <select> e <textarea> . Ao submeter um
formulário com a tag: <input name="usuario[idade] value="23”>será
criado um objeto dentro de req.body . Neste caso, será criado
req.body.usuario.idade
Alguns cuidados ao trabalhar com Sessions
Qualquer nome informado para o req.session será
armazenado como um atributo deste objeto, por exemplo:
req.session.mensagem = "Olá". Cuidado para não so-
brescrever os nomes de suas funções nativas, como por exemplo:
req.session.destroyou req.session.regenerate. Aofazer
isso, você sobrescreve essas funções desabilitando suas respectivas
funcionalidades. Com isso, no decorrer de sua aplicação possíveis
inesperados bugs acontecerão no sistema. Para entender melhor as
funçõesdasession,vejaadocumentaçãodoConnect:
http://www.senchalabs.org/connect/session.html
Para finalizar, antes de testarmos as modificações, precisamos criar
um controller e routes para contatos. Afinal temos a fun ção
res.redirect('/contatos') e até agora não foi implementada nenhuma
lógicapararealizaresteredirecionamento.
Arota /contatospermiteentraremumanovaáreadosistema,queseráuma
dasprincipaisáreasqueiremosexplorarnodecorrerdestelivro.Porenquantovamos
simplificaraimplementaçãocriandoum controller,umrotaeuma viewparaele.
Crieodiretório contatosdentrode viewsecodifiqueoarquivo index.ejs
comoseguinteconteúdo:
<% include ../header %>
<header>
47

## Página 64

5.2. Controlandoassessõesdeusuários CasadoCódigo
<h2>Ntalk - Agenda de contatos</h2>
</header>
<section>
<p>Bem-vindo <%- usuario.nome %></p>
</section>
<% include ../exit %>
<% include ../footer %>
Nestaviewvamosrenderizaronomedousuáriologado,paraissoutilizamos
afunção: <%- usuario.nome %>. Esteobjetoseráenviadopelocontrollerque
implementaremosaseguir. Reparequedestavezreaproveitamoso header.ejs
e footer.ejseissotornoumuitomaislimpoesta view.Tambémincluímosum
novopartial- <% include ../exit %>. Basicamente,elepossuiolink Sair,
quesimplesmentefaz logoutnosistema.Eleseráreaproveitadoporgrandepartedo
sistema,entãoiremoscriá-lodentrode views/exit.ejs:
<section>
<a href='/sair'>Sair</a>
</section>
Agoravamoscriaroseucontrollerchamadode contatos.js,contendoape-
nasa action index.Elebasicamentevaipegarosdadosdeumusuáriologadoatra-
vésdavariávelreq.session.usuarioevaienviá-losparaviewatravésdafunção:
res.render().
module.exports = function(app) {
var ContatoController = {
index: function(req, res) {
var usuario = req.session.usuario
, params = {usuario: usuario};
res.render('contatos/index', params);
}
}
return ContatoController;
};
Parafinalizar,criaremosumnovo routes,porconven ção,utilizamosomesmo
nomedoseu controllereporenquanto, vamosincluirarotaGETcomopath:
/contatos.
48

## Página 65

CasadoCódigo Capítulo5. DominandooExpress
module.exports = function(app) {
var contatos = app.controllers.contatos;
app.get('/contatos', contatos.index);
};
Vamostestarnovamente? Reinicieoservidorteclandonoterminal CTRL+C
(noWindowsouLinux)ou Command+C(noMacOSX),emseguidaexecute node
app.js,porúltimoacesseemseubrowser: http://localhost:3000.Façanovamente
umloginnosistema,dessaveztemosumanovatelanosistema,aagendadecontatos.
Acabamosdeexpandirnossoprojeto,incluímosaáreaprincipal.Aprendemos
comohabilitarsessionparaimplementarumcontrolede loginelogout. Deixamos
todasasviewsenxutas,isolandopossíveistrechosderepetiç ãodecódigohtml,além
explorarmosnovositensda stackdeconfiguraçãodoservidorNode.
5.3 Criando rotas no padrão REST
Anossaagendadecontatosprecisatercomorequisitomínimoummeiodepermi-
tirousuáriocriar,listar,atualizareexcluircontatos. Esseéoconjuntoclássicode
funcionalidades,maisconhecidocomoCRUD (Create,Receive,UpdateeDelete).
AsrotasqueutilizaremosparaimplementaroCRUDdaagendadecontatosserá
aplicandoopadrãoderotasREST.Essepadrãoconsisteemcriarrotasutilizandoos
principaismétodosdoHTTP (GET, POST, PUT e DELETE).Paraissoteremos
quehabilitarumnovoitemna stackdeconfiguraçõesno app.js:
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
app.use(express.cookieParser('ntalk'));
app.use(express.session());
app.use(express.json());
app.use(express.urlencoded());
app.use(express.methodOverride());
app.use(app.router);
app.use(express.static(__dirname + '/public'));
Incluímoso express.methodOverride()quepermiteutilizarummesmo
pathentreosmétodosdoHTTP,fazendoumasobrescritademétodos.Tambémfoi
adicionadoo middleware app.router,quegerenciaasrotasdaaplicaç ão,permi-
tindoaimplementaçãoderotasparapáginasdeerros(muitacalma!Issoaindaserá
49

## Página 66

5.3. CriandorotasnopadrãoREST CasadoCódigo
explicadonestecapítulo.)erotasparaarquivosestáticos,semconflitarcomasrotas
daaplicação.
Abraoarquivo routes/contatos.js,nelevamosimplementarasfuturas
rotasparaimplementaroCRUDdaagendadecontatos:
module.exports = function(app) {
var contatos = app.controllers.contatos;
app.get('/contatos', contatos.index);
app.get('/contato/:id', contatos.show);
app.post('/contato', contatos.create);
app.get('/contato/:id/editar', contatos.edit);
app.put('/contato/:id', contatos.update);
app.del('/contato/:id', contatos.destroy);
};
Comasrotascriadas,precisamosagoraimplementarasregrasdenegócioden-
trodocontroller contatos.js. Comoaindanãoutilizaremosumbancodeda-
dos,todososdadosserãopersistidosnaprópriasessãodousuário,ouseja,todosos
contatosserãogravadosemmemóriaenãoemumbancodedadosdedicado. Em
controller/contatos.jsimplementeaseguintelógicana action index:
module.exports = function(app) {
var ContatoController = {
index: function(req, res) {
var usuario = req.session.usuario
, contatos = usuario.contatos
, params = {usuario: usuario
, contatos: contatos};
res.render('contatos/index', params);
},
// continuação do controller...
}
Jánaaction createutilizaremosumsimples arrayparapersistiroscontatosdo
usuário—usuario.contatos.push(contato);—paraemseguidaredireci-
onarousuáriopararota /contatos:
create: function(req, res) {
var contato = req.body.contato
, usuario = req.session.usuario;
usuario.contatos.push(contato);
50

## Página 67

CasadoCódigo Capítulo5. DominandooExpress
res.redirect('/contatos');
},
// continuação do controller...
Em show e edit enviamos via parâmetro no path, o ID do usuário.
Nestecaso, passamosapenasoíndicedocontatoreferenteasuaposi çãonoar-
rayeemseguidaenviamosocontatoparaarenderizaç ãodesuarespectivaview
res.render('contatos/show')e res.render('contatos/edit');:
show: function(req, res) {
var id = req.params.id
, contato = req.session.usuario.contatos[id]
, params = {contato: contato, id: id};
res.render('contatos/show', params);
},
edit: function(req, res) {
var id = req.params.id
, usuario = req.session.usuario
, contato = usuario.contatos[id]
, params = {usuario: usuario
, contato: contato
, id: id};
res.render('contatos/edit', params);
},
// continuação do controller...
Agoratemosa actions update.Elarecebeosdadosdeumcontatoatualizado
quesãosubmetidospeloformuláriodaview contatos/edit.Emseguidautiliza-
mosseuíndicevia req.params.idparaatualizarnoarrayocontato.
update: function(req, res) {
var contato = req.body.contato
, usuario = req.session.usuario;
usuario.contatos[req.params.id] = contato;
res.redirect('/contatos');
},
// continuação do controller...
Por último temos aaction destroy, que basicamente recebe o índice
através da variávelreq.params.id e exclui o contato do array via função
usuario.contatos.splice(id, 1).
51

## Página 68

5.3. CriandorotasnopadrãoREST CasadoCódigo
destroy: function(req, res) {
var usuario = req.session.usuario
, id = req.params.id;
usuario.contatos.splice(id, 1);
res.redirect('/contatos');
}
// fim do controller...
return ContatoController;
};
Essefoiumesbo çomuitobásicodaagendadecontatos.Porém,comesseesboço
foipossívelexploraralgumascaracterísticasdoExpressparaaimplementaç ãodeum
CRUD.
Parafinalizar,vamoscriarasviewsparaousuáriointeragirnosistema.Dentro
dodiretório views/contatosvamosmodificaraview index.ejspararende-
rizarumalistadecontatoseumformulárioparacadastrarnovoscontatos:
<% include ../header %>
<header>
<h2>Ntalk - Agenda de contatos</h2>
</header>
<section>
<form action="/contato" method="post">
<input type="text" name="contato[nome]" placeholder="Nome">
<input type="text" name="contato[email]" placeholder="E-mail">
<button type="submit">Cadastrar</button>
</form>
<table>
<thead>
<tr>
<th>Nome</th>
<th>E-mail</th>
<th>Ação</th>
</tr>
</thead>
<tbody>
<% contatos.forEach(function(contato, index) { %>
<tr>
<td><%- contato.nome %></td>
<td><%- contato.email %></td>
<td>
52

## Página 69

CasadoCódigo Capítulo5. DominandooExpress
<a href="/contato/<%- index %>">Detalhes</a>
</td>
</tr>
<% }) %>
</tbody>
</table>
</section>
<% include ../exit %>
<% include ../footer %>
Agoranomesmodiretório,vamoscriaro edit.ejseimplementarumformu-
lárioparaousuárioatualizarosdadosdeumcontato:
<% include ../header %>
<header>
<h2>Ntalk - Editar contato</h2>
</header>
<section>
<form action="/contato/<%- id %>" method="post">
<input type="hidden" name="_method" value="put">
<label>Nome:</label>
<input type="text" name="contato[nome]"
value="<%- contato.nome %>">
<label>E-mail:</label>
<input type="text" name="contato[email]"
value="<%- contato.email %>">
<button type="submit">Atualizar</button>
</form>
</section>
<% include ../exit %>
<% include ../footer %>
Porúltimoemaisfácildetodos,crieaview show.ejs.Nela,vamosrenderizar
osdadosdeumcontatoqueforselecionado.Incluiremosdoisbotões: Editar(para
acessararotadeediçãodocontato)e Excluir(botãoquevaiexcluirocontatoatual).
<% include ../header %>
<header>
<h2>Ntalk - Dados do contato</h2>
</header>
<section>
<form action="/contato/<%- id %>" method="post">
53

## Página 70

5.4. Aplicandofiltrosantesdeacessarasrotas CasadoCódigo
<input type="hidden" name="_method" value="delete">
<p><label>Nome:</label><%- contato.nome %></p>
<p><label>E-mail:</label><%- contato.email %></p>
<p>
<button type="submit">Excluir</button>
<a href="/contato/<%- id %>/editar">Editar</a>
</p>
</form>
</section>
<% include ../exit %>
<% include ../footer %>
UtilizandoPUT eDELETE doHTTP
Infelizmente,asespecificaçõesatuaisdoHTTPnãodãosuportepara
utilizarosverbos PUTe DELETEdeformasemânticaemumcódigo
html,comoporexemplo:
<form action="/editar" method="put">
<form action="/excluir" method="delete">
Asoluçãopaliativaécriaratag <input>comonome _methode
ovalor putou delete,parasobrescreverométodoPOSTouGETda
tag <form>.Vejaoexemploabaixo:
<input type="hidden" name="_method" value="put">
<input type="hidden" name="_method" value="delete">
5.4 Aplicando filtros antes de acessar as rotas
Jápercebeuquequandoacessamosarota /contatossemlogarnosistemaacon-
teceumbug?Não?Tenteagoramesmo!Masoquerealmenteprovocouesteerro?
Bem,quandofazemosumlogincomsucesso,armazenamososprincipaisdados
dousuárionasessãoparautilizá-losnodecorrerdaaplicaç ão. Quandoacessa-
mos /contatossemantesterfeitoumlogin,ocontrollertentaacessaravariá-
vel req.session.usuarioquenãoexisteainda. Issocausaoseguintebugna
aplicação:
54

## Página 71

CasadoCódigo Capítulo5. DominandooExpress
Figura5.2:Bug:Cannotreadproperty‘usuario’ofundefined.
DiferentedoRails,SinatraouDjango,oExpressnãopossuifiltrosdeformaex-
plícitaeemcódigolegível. Nãoexisteumafun ção beforeou afterpelaqual
sepossaprocessaralgoantesoudepoisdeentraremumarota. Mascalma! Nem
tudoestaperdido! GraçasaoJavascripttemosasfun çõesdecallback,eopróprio
mecanismoderoteamentodoExpressutilizamuitobemesserecurso,permitindo
acriaçãodecallbackencadeadosemumarota. Resumindo,quandocriamosuma
rota,apósinformarnoprimeiroparâmetroasuastring,nosegundoparâmetroem
dianteépossívelincluircallbacksquesãoexecutadosdeformaordenada,porexem-
plo: app.get('/', callback1, callback2, callback3).
Paraimplementarmosisso,primeirovamoscriarofiltrodeautenticaç ão. Ele
seráacriaçãodonossoprimeiro middlewareeseráutilizadonamaioriadasrotas.
Naraizdoprojetocrieapasta middlewareincluindooarquivo autenticador.js,
neleimplementealógicaabaixo:
module.exports = function(req, res, next) {
if(!req.session.usuario) {
return res.redirect( '/');
}
return next();
};
Esse filtro faz uma simples verificação se existe um usuário dentro da ses-
são. Seousuárioestiverautenticado,ouseja,estiverna session,seráexecu-
tadoocallback return next()responsávelporpularestefiltroeindoparafun-
çãoaolado. Casoautenticaçãonãoaconte ça,executamosumsimples return
55

## Página 72

5.5. Indoalém:criandopáginasdeerrosamigáveis CasadoCódigo
res.redirect('/'),quefazousuáriovoltarparapáginainicialeimpedindo
queocorraobug.
Com esse filtro implementado, agora temos que injetá-lo nos call-
backs das rotas que precisam desse tratamento, faremos essas alterações no
routes/contatos.js,deacordocomocódigoaseguir:
module.exports = function(app) {
var autenticar = require('./../middleware/autenticador')
, contatos = app.controllers.contatos;
app.get('/contatos', autenticar, contatos.index);
app.get('/contato/:id', autenticar, contatos.show);
app.post('/contato', autenticar, contatos.create);
app.get('/contato/:id/editar', autenticar, contatos.edit);
app.put('/contato/:id', autenticar, contatos.update);
app.del('/contato/:id', autenticar, contatos.destroy);
};
Basicamenteinserimosocallback autenticarantesdafun çãoprincipalda
rota.Issonospermitiuemularaexecuç ãodeumfiltro before.Casoqueiracriar
umfiltro after,nãohásegredos:apenascoloqueocallbackdofiltroporúltimo.
Oimportanteécolocarasfun çõesnaordemlógicadesuasexecuções.
5.5 Indo além: criando páginas de erros amigáveis
OExpressoferecesuportepararoteamentoerenderizaç ãodeerrosdoprotocolo
HTTP.Elepossuiapenasduasfun ções,umaespecíficaparatratamentodofamoso
erro404(páginanãoencontrada)eumafun çãogenéricaquerecebeporparâmetro
umavariávelcontendodetalhessobreostatusemensagemdoerroHTTP.
Sobre o código de erros do HTTP
OprotocoloHTTPtemdiversostiposdeerros. OórgãoW3Cpos-
suiumadocumentaçãoexplicandoemdetalhesocomportamentoecó-
digodecadaerro. Paraficarpordentrodesseassuntovejanesselink
(http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)aespecifica-
çãodosstatusdeerrogeradosporesteprotocolo.
56

## Página 73

CasadoCódigo Capítulo5. DominandooExpress
Quetalimplementarmosumcontroledeerrospararenderizaraosusuáriospá-
ginascustomizadasemaisamigáveis? Primeiro,crieduasnovasviews,umapara
apresentarateladoerro404conhecidanawebcomo "Páginanãoencontrada”,seu
nomeseránot-found.ejs...
<% include header %>
<header>
<h1>Ntalk</h1>
<h4>Infelizmente essa página não existe :(</h4>
</header>
<hr>
<p>Vamos voltar <a href="/">home page?</a> :)</p>
<% include footer %>
...eaoutraseráfocadaemmostrarerrosgeradospeloprotocoloHTTPcomo
nomede server-error.ejs:
<% include header %>
<header>
<h1>Ntalk</h1>
<h4>Aconteceu algo terrível! :(</h4>
</header>
<p>
Veja os detalhes do erro:
<br>
<%- error.message %>
</p>
<hr>
<p>Que tal voltar <a href="/">home page?</a> :)</p>
<% include footer %>
Feitoisso,agorasóprecisamosadicionardoisnovositensna stackdeconfigura-
çõesdoapp.jspararenderizarasrespectivasviewsdeerros:
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
app.use(express.cookieParser('ntalk'));
app.use(express.session());
app.use(express.json());
app.use(express.urlencoded());
app.use(app.router);
app.use(express.static(__dirname + '/public'));
57

## Página 74

5.5. Indoalém:criandopáginasdeerrosamigáveis CasadoCódigo
app.use(function(req, res, next) {
res.status(404);
res.render('not-found');
});
app.use(function(error, req, res, next) {
res.status(500);
res.render('server-error', error);
});
Paraminimizaressapoluiçãodecódigona stackdoservidor,exporteasfun ções
deerrosparaumnovoarquivochamado error.jsdentrododiretório middleware,
deixando-asdaseguinteforma:
exports.notFound = function(req, res, next) {
res.status(404);
res.render('not-found');
};
exports.serverError = function(error, req, res, next) {
res.status(500);
res.render('server-error', {error: error});
};
Emseguidamodifiqueo stackdo app.jsparaficarmaislimpo:
var express = require('express')
, app = express()
, load = require('express-load')
, error = require('./middleware/error');
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
app.use(express.cookieParser('ntalk'));
app.use(express.session());
app.use(express.json());
app.use(express.urlencoded());
app.use(app.router);
app.use(express.static(__dirname + '/public'));
app.use(error.notFound);
app.use(error.serverError);
Vamostestaronossocódigo? Reinicieoservidore,nobrowser,digitepro-
positalmenteumanomedeumarotaquenãoexistanaaplicaç ão,porexemplo:
58

## Página 75

CasadoCódigo Capítulo5. DominandooExpress
http://localhost:3000/url-errada. Estafoiarenderizaçãodateladeerroparapágina
nãoencontrada(erro404).
Figura5.3:Teladeerro404.
Eparatestarapáginadeerrointernodoservidor? Estatelasomenteseráexi-
bidaemcasosdeerrosgravesnosistema. Parafor çarumsimplesbugnosistema,
removaumfiltrodarota /contatos,forçandoobugqueocorrianase çãoanterior
quefalávamossobreaimplementaçãodefiltros.
Figura5.4:Teladeerro500.
Parabéns! Agoratemosumaaplicaçãoquecadastra,edita,excluielistaconta-
tos.UtilizamosopadrãoderotasREST,criamosumsimplescontroledeloginque
mantémousuárionasessão,implementamosfiltrosparabarraracessodeusuários
nãoautenticadoseprafinalizar,implementamosarenderizaç ãodepáginasdeer-
59

## Página 76

5.5. Indoalém:criandopáginasdeerrosamigáveis CasadoCódigo
rosamigáveis—afinalerrosinesperadospodemocorreremnossaaplicaçãoeseria
desagradávelousuárioverinformaçõescomplexasnatela.
60

## Página 77

Capítulo6
Programandosistemasreal-time
6.1 Como funciona uma conexão bidirecional?
Estecapítuloserámuitointeressante,poisfalaremossobreumassuntoemergente
nossistemasatuaisqueestásendolargamenteutilizadonoNode.js. Estoufalando
sobredesenvolvimentodeaplicaçõesreal-time.
Tecnicamente,estamosfalandodeumaconexãobidirecional,que,naprática,é
umaconexãoquesemantémaberta (connectionkeep-alive)paraclienteseservidores
interagirememumaúnicaconexão.Avantagemdissoficaparaosusuários,poisa
interaçãonosistemaseráemtemporeal,trazendoumaexperiênciadeusuáriomuito
melhor.

## Página 78

6.2. ConhecendooframeworkSocket.IO CasadoCódigo
Figura6.1:Imagemexplicandosobreconexãobidirecional.
ONode.jssetornoupopularporoferecerbibliotecasdebaixonívelquesupor-
tamdiversosprotocolos (HTTP,HTTPS,FTP,DNS,TCP,UDPeoutros).Orecente
protocoloWebSocketstambémécompatívelcomNode.jseelepermitedesenvolver
sistemasdeconexãopersistenteutilizandoJavascripttantonoclientequantonoser-
vidor.
Infelizmenteoúnicoproblemaemutilizaresteprotocolo,équenemtodosos
browserssuportamesserecurso,tornandoinviáveldesenvolverumaaplicaçãoreal-
timecross-browser.
6.2 Conhecendo o framework Socket.IO
Diantedesseproblema,nasceuoSocket.IO.Eleresolveaincompatibilidadeentreo
WebSocketscomosnavegadoresantigos,emulando,porexemplo, Ajaxlong-polling
ououtrostransportsdecomunicaçãoembrowsersquenãopossuem WebSockets,de
formatotalmenteabstraídaparaodesenvolvedor.Seusiteoficialé:(http://socket.io)
Figura6.2:FrameworkSocket.IO.
62

## Página 79

CasadoCódigo Capítulo6. Programandosistemasreal-time
OSocket.IOfuncionadaseguintemaneira:éincluídoumscriptnoclienteque
detectainformaçõessobreobrowserdousuárioparadefinirqualseráamelhorco-
municaçãocomoservidor.Os transportsdecomunicaçãoqueeleexecutasão:
1)WebSocket;
2) AdobeFlashSocket;
3) AJAXlongpolling;
4) AJAXmultipartstreaming;
5) Foreveriframe;
6) JSONPPolling;
Seonavegadordousuáriopossuircompatibilidadecom WebSocketsouFlashSoc-
kets(utilizandoAdobeFlashPlayer donavegador),serárealizadaumacomunicação
bidirecional.Casocontrário,seráemuladaumacomunicaçãounidirecional,queem
curtosintervalosdetempofazrequisiçõesAJAXnoservidor.Éclaroqueodesem-
penhoéinferior,porémgarantecompatibilidadecombrowsersantigosemantémo
mínimodeexperiênciareal-timeparaousuário.Omaisinteressantedetudoissoé
queprogramarutilizandooSocket.IOémuitosimplesetodadecisãocomplexaéele
quefaz,simplificandoavidaodesenvolvedor.
6.3 Implementando um chat real-time
Vamosvercomofuncionanaprática?Criaremosowebchatnontalk,comoqual
ousuárioenviarámensagensparaosusuáriosonlinedaagendadecontatos. Inte-
graremosoframeworks: Socket.IOnoExpress. Primeiro,instalaremosomódulo
atualizandoo package.json:
"dependencies": {
"express": "3.4.7",
"express-load": "1.1.8",
"ejs": "0.8.5",
"socket.io": "0.9.16"
}
63

## Página 80

6.3. Implementandoumchatreal-time CasadoCódigo
Utilizaremosaversão 0.9.16doSocket.IO,agoravamosinstalá-loexecutando
noconsole: npm install
Vamosadaptaro app.jscomonovomódulo.Afun çãolistendoservidorweb
serárealizadaviamódulohttpatravésdafun ção server.listen(3000)para
queoSocket.IOutilize-aparacriarseupontodecomunicaç ãoatravésdoprotocolo
HTTP.
var express = require('express')
, app = express()
, load = require('express-load')
, error = require('./middleware/error')
, server = require('http').createServer(app)
, io = require('socket.io').listen(server);
// ...código do stack de configurações...
// ...código da função load()...
io.sockets.on('connection', function (client) {
client.on('send-server', function (data) {
var msg = "<b>"+data.nome+":</b> "+data.msg+"<br>";
client.emit('send-client', msg);
client.broadcast.emit('send-client', msg);
});
});
server.listen(3000, function(){
console.log("Ntalk no ar.");
});
Instanciamos os módulos: express, http e socket.io. É ne-
cessário seguir esta ordem, pois o Socket.IO funciona a partir de uma
instância do módulo http. Toda brincadeira começa a partir do evento:
io.sockets.on('connection'). Esta função espera um cliente interagir
com um de seus eventos internos. Por enquanto, o único evento interno é o
client.on('send-server'),cujasuaexecuçãoocorrequandoumclienteen-
viaumamensagemparaoservidor.Percebaquepoucocódigofoiincluídoeoservi-
dorrespondeaseusclientesatravésdasfun çõesclient.emit('send-client')
e client.broadcast.emit('send-client'). Resumindo, o fluxo básico
é o cliente enviar uma mensagem para o servidor e o servidor responde o
próprio cliente (viaclient.emit()) e seus demais clientes conectados (via
64

## Página 81

CasadoCódigo Capítulo6. Programandosistemasreal-time
client.broadcast.emit()). Para compreender melhor, veja as ilustrações
abaixo:
Figura6.3:Enviamensagensparaoclienteouservidor.
Figura6.4:Enviamensagensparatodososclientes,excetoopróprioemissor.
Comoback-enddoSocket.IOimplementado,vamosmodificarofront-endpara
interagirnestemeiodecomunicação.Dentrode views/contatos/index.ejs
modificaremosalistagemdoscontatosincluindoumlink "Conversar”,eleteráo
path:/chat/email-do-contato,queseráusadoparacriarasaladochatrespectiva
paraoseucontato.
65

## Página 82

6.3. Implementandoumchatreal-time CasadoCódigo
<% contatos.forEach(function(contato, index) { %>
<tr>
<td><%- contato.nome %></td>
<td><%- contato.email %></td>
<td>
<a href="/contato/<%- index %>">Detalhes</a>
<a href="/chat/<%- contato.email %>">Conversar</a>
</td>
</tr>
<% }) %>
Vamosimplementarolayoutdonossochateprincipalmenteoseventosdeco-
municaçãodoclienteparainteragircomoservidor. Crieumnovocontrollerem
controller/chat.js:
module.exports = function(app) {
var ChatController = {
index: function(req, res){
var resultado = {email: req.params.email,
usuario: req.session.usuario};
res.render('chat/index', resultado);
}
};
return ChatController;
};
Crieoseurespectivoroutes routes/chat.js:
module.exports = function(app) {
var chat = app.controllers.chat;
app.get('/chat/:email', chat.index);
};
E,porúltimo,criesuaviewem views/chat/index.ejs.Utilizaremosjavas-
criptpuroparamanipulaçãodohtml,massinta-seàvontadeparautilizarqualquer
frameworkdogênero,comoporexemplo: jQuery(http://jquery.com)ou ZeptoJS
(http://zeptojs.com).
Oimportanteécarregaroscript /socket.io/socket.io.jsparaquea
brincadeiracomece.Aliás,nãosepreocupedeondeveioessescript,poiseleédis-
tribuídoautomaticamentepeloframework socket.io-clientquejávemcomo
66

## Página 83

CasadoCódigo Capítulo6. Programandosistemasreal-time
dependênciadoSocket.IO,eeleéresponsávelpelacomunicaçãodoclientecomo
servidor.
Épelafun ção io.connectqueoclienteseconectacomoservidorecome çaa
trocarmensagenscomele.EssainteraçãoocorreatravésdotráfegodeobjetosJSON.
Vamosincluirno index.ejsasfunçõesdeenviarerecebermensagens:
<% include ../header %>
<script src="/socket.io/socket.io.js"></script>
<script>
var socket = io.connect('http://localhost:3000');
socket.on('send-client', function (msg) {
document.getElementById('chat').innerHTML += msg;
});
var enviar = function() {
var nome = document.getElementById('nome').value;
var msg = document.getElementById('msg').value;
socket.emit('send-server', {nome: nome, msg: msg});
};
</script>
<header>
<h2>Ntalk - Chat</h2>
</header>
<section>
<pre id="chat"></pre>
<input type="hidden" id="nome" value="<%- usuario.nome %>">
<input type="text" id="msg" placeholder="Mensagem">
<button onclick="enviar();">Enviar</button>
</section>
<% include ../exit %>
<% include ../footer %>
Emseguida,vamosreiniciaraaplicaç ãocomocomando node app.jsede-
poisacessá-lonoendereçohttp://localhost:3000pelobrowser.
Paraentendermelhorcomotudofunciona,acesseomesmoendere çoemoutro
browserparaterduasjanelasnamesmaaplicaç ão.Cadastredoisusuários,cadaum
emsuarespectivajanela,emseguidaadicioneemcontatosonomeee-maildooutro
usuário,porexemplo,najanelado UsuárioAadicionecomocontatoosdadosdo
UsuárioBevice-versa. Agoracliqueemnolink "Conversar”eenviemensagem
paraousuário.
67

## Página 84

6.3. Implementandoumchatreal-time CasadoCódigo
Figura6.5:UsuárioAconversandocomUsuárioB.
Figura6.6:UsuárioBrespondendomensagensdoUsuárioA.
Setudodeucerto,parabéns!Owebchatcomomínimoderecursosfuncionais
eemtemporealestanoar. Mesmoquevocêuseumnavegadorantigo,comoo
InternetExplorer6,tudofuncionarábem!PoisoSocket.IOfaráotrabalhodeemular
acomunicaçãoentreambos,mesmosemapresen çadoprotocoloWebSocket.
68

## Página 85

CasadoCódigo Capítulo6. Programandosistemasreal-time
6.4 O rganizando o carregamento de Sockets
Anossaaplicaçãoteráduasfuncionalidadescomrespostaemtemporeal:ochate
onotificadordemensagens.Emsistemasmaiorespodemsurgirdiversasfunciona-
lidadesnessamodalidadeecodificartodasasfun çõesdoSocket.IOemumúnico
arquivoficariaterrivelmenteassustadorparafazermanuten ções.Oidealéseparar
asfuncionalidadesdeformamodulareescalável—essapráticaésemelhanteaoque
fizemoscomasviews,modelsecontrollers.Combasenesseproblema,crieodiretó-
rio socketseadicioneneleoarquivo chat.js.Paraessearquivoiremosmigrar
ocódigoSocket.IOdo app.js,vejaoexemploabaixo:
module.exports = function(io) {
var sockets = io.sockets;
sockets.on('connection', function (client) {
client.on('send-server', function (data) {
var msg = "<b>"+data.nome+":</b> "+data.msg+"<br>";
client.emit('send-client', msg);
client.broadcast.emit('send-client', msg);
});
});
}
Dessaformadeixamoso app.jscommenoscódigo.Umdetalheimportante
équeo chatserácarregadoporumanovachamadaafun ção load()pelaqual
passaremoscomoparâmetroavariável io:
var express = require('express')
, app = express()
, load = require('express-load')
, error = require('./middleware/error')
, server = require('http').createServer(app)
, io = require('socket.io').listen(server)
;
// stack de configurações...
load('models')
.then('controllers')
.then('routes')
.into(app);
load('sockets')
.into(io);
// server.listen()...
69

## Página 86

6.5. Socket.IOeExpressemumamesmasessão CasadoCódigo
Emaisumavezutilizamosboaspráticasdecódigomodular,organizandome-
lhoroprojetoepreparando-oparatrabalharcomdiversasfun çõesdoSocket.IOem
conjuntocomExpress.
6.5 Socket.IO eExpress em uma mesma sessão
OSocket.IOconsegueacessaremanipularumasessioncriadapeloservidorweb.
Implementaremosessecontroledesessioncompartilhada,poisémaissegurodoque
passarosdadosdousuáriologadoatravésdatag:
<input type="hidden" id="nome" value="<%- usuario.nome %>">
Comoissofunciona?Naprática,quandologamosnosistema,oExpresscriaum
IDdesessionparaousuário.Essasessionépersistidaemmemóriaoudisconoser-
vidor(essadecisãoficaacritériodosdesenvolvedores).OSocket.IOnãoconsegue
acessaressesdados,eleapenaspossuiumcontroleparaautorizarumaconexãodo
cliente.Comisso,podemosutilizarasfun çõesdesessionecookiesdoExpressden-
trodessafun çãodeautorizaçãobuscandoevalidandoumasession—seomesmo
forválido,armazenamosnoclienteSocket.IO,autorizandosuaconexãonosistema.
Resumindo,precisamoscriarumcontroleparacompartilharsessionentreoEx-
presseSocket.IO.VamosconfigurarnoExpressparaisolaremvariáveisasfun ções:
express.cookieParsere express.session.Tambémcriaremosduascons-
tanteschamadas: KEYe SECRETqueserãoutilizadasparabuscaroIDdasession
ecarregarosdadosdousuáriologadoutilizandooobjeto MemoryStore.Faremos
essasmodificaçõesno app.js,seguindootrechodocódigoabaixo:
// carregamento dos módulos...
const KEY = 'ntalk.sid', SECRET = 'ntalk';
var cookie = express.cookieParser(SECRET)
, store = new express.session.MemoryStore()
, sessOpts = {secret: SECRET, key: KEY, store: store}
, session = express.session(sessOpts);
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
app.use(cookie);
app.use(session);
app.use(express.json());
app.use(express.urlencoded());
70

## Página 87

CasadoCódigo Capítulo6. Programandosistemasreal-time
app.use(express.methodOverride());
app.use(app.router);
app.use(express.static(__dirname + '/public'));
app.use(error.notFound);
app.use(error.serverError);
Comessesrecursoshabilitados,serápossívelutilizarsessionnoSocket.IO.Va-
mosimplementarumcontroledeautorizaç ãovia io.set('authorization')
paraqueacadaconexãooSocket.IOvalideoSessionIDpermitindoounãorecu-
perarosdadosdousuáriopresentenosistema. Aseguir,implementamosdiversas
condicionaisparaessevalidação:
// require dos módulos...
// stack de configurações...
io.set('authorization', function(data, accept) {
cookie(data, {}, function(err) {
var sessionID = data.signedCookies[KEY];
store.get(sessionID, function(err, session) {
if (err || !session) {
accept(null, false);
} else {
data.session = session;
accept(null, true);
}
});
});
});
// load()...
// server.listen()...
A função accept() é a responsável pela autorização da conexão e a va-
riável data contém informações do cliente, isso inclui headers, cookies e
outras informações do HTTP. Buscamos osessionID através da variável
data.signedCookies[KEY],emseguidabuscamososdadosdasessionquees-
tãonamemóriadoservidoratravésdafun ção store.get().Setudoocorrercom
sucesso,incluímosasessionnavariável dataeliberamosaconexãopelafun ção
accept(null, true).
Pronto! AgoraoSocket.IOestahabilitadoparaleremanipularosobjetosde
umasessioncriadapeloExpress.Comisso,podemostrafegarosdadosdousuário
71

## Página 88

6.5. Socket.IOeExpressemumamesmasessão CasadoCódigo
logadodentrodonossochat.Parafinalizaressatarefa,faremosalguns refactors.Pri-
meirovamosdeixarmaisenxutaaview: chat/index.ejsremovendoasvariáveis
referentesaonomedousuário:
<% include ../header %>
<script src="/socket.io/socket.io.js"></script>
<script>
var socket = io.connect('http://localhost:3000 ');
socket.on('send-client', function (msg) {
var chat = document.getElementById('chat');
chat.innerHTML += msg;
});
var enviar = function() {
var msg = document.getElementById('msg');
socket.emit('send-server', msg.value);
};
</script>
<header>
<h2>Ntalk - Chat</h2>
</header>
<section>
<pre id="chat"></pre>
<input type="text" id="msg" placeholder="Mensagem">
<input type="button" onclick="enviar();" value="Enviar">
</section>
<% include ../exit %>
<% include ../footer %>
Tambémvamosremoverdocontroller chat.jsavariávelreferenteaosdados
usuáriodasession req.session.usuario:
module.exports = function(app) {
var ChatController = {
index: function(req, res){
var params = {email: req.params.email};
res.render('chat/index', params);
}
};
return ChatController;
};
72

## Página 89

CasadoCódigo Capítulo6. Programandosistemasreal-time
Comavieweocontrollermaislimpa,vamosadaptarno sockets/chat.js
oevento sockets.on('connection')paraconcatenarastringdemensagens
comonomedousuário.Aúnicadiferen çaéqueagoraserãocarregadospelavariável
client.handshake.sessionosdadosdousuárioconectado:
module.exports = function(io) {
var sockets = io.sockets;
sockets.on('connection', function (client) {
var session = client.handshake.session
, usuario = session.usuario;
client.on('send-server', function (msg) {
msg = "<b>"+usuario.nome+":</b> "+msg+"<br>";
client.emit('send-client', msg);
client.broadcast.emit('send-client', msg);
});
});
}
6.6 G erenciando salas do chat
Parafinalizaronossochat,vamosaprimorá-loimplementandoumcontroledesala
one-to-oneparaassegurarquecadaconversasejaentredoisusuáriosnonossobate-
papo,prevenindoqueoutrosusuáriosentremnomeiodeumaconversaadois.
Desenvolver essa funcionalidade é muito simples, apenas temos que
criar uma string que será o nome da sala e utilizá-la através da função:
sockets.in('nome_da_sala').emit(). Outro detalhe dessa função é
queelaemiteumeventoparatodososusuáriosdasala,incluindooprópriousuário
emissor.
Paraimplementarumasala one-to-onetemosquegarantirqueemumasalaen-
tremnomáximodoisclientes.Paraimplementardeformaseguratemosquecriar
nomesdesalasdifíceisdeseremdecifrados,paraissoutilizaremosummódulona-
tivodoNode.jsparacriptografaronomedeumasala.Eleseráum HashMD5deum
timestampcriadopeloprimeirousuárioquecome çarumaconversa.
73

## Página 90

6.6. Gerenciandosalasdochat CasadoCódigo
Dicas sobre criptografia noNode.js
AcadanovaversãodaAPICryptodoNode.jséaprimoradonovas
melhoriasenovasfun ções. PorémessaAPItrabalhacomrecursosbá-
sicosdecriptografia,casovocêsejaumdesenvolvedorfocadoemsegu-
rança,utilizeomóduloBCrypt,quepossuiumasériedefuncionalidades
ealgoritmosdecriptografiamaisdifíceisdesequebrar.Paraconhecero
BCryptemdetalhesesuasfuncionalidadesacessesuadocumentaç ão:
https://github.com/ncb000gt/node.bcrypt.js
Vejanapráticacomogerenciaremosassalasdosusuários.Primeirocarregare-
mososmódulosdecriptografiaparagerarovalor hashdasala.
module.exports = function(io) {
var crypto = require('crypto')
, md5 = crypto.createHash('md5')
, sockets = io.sockets;
// ...continuação do código...
}
Dentrodoevento sockets.on('connection'),criaremosumnovoevento
client.on('join'),queseráemitidoquandoumusuárioentrarnochat.Imple-
mentaremosumsimplescondicionalparacriaro hashdasalaquandonãoexistire
emseguidaarmazenamosemmemóriavia client.set('sala', sala).
client.on('join', function(sala) {
if(sala) {
sala = sala.replace('?','');
} else {
var timestamp = new Date().toString();
var md5 = crypto.createHash('md5');
sala = md5.update(timestamp).digest('hex');
}
client.set('sala', sala);
client.join(sala);
});
Paracontrolarasaídadeusuáriosnasala,vamosutilizaroevento defaultdoSoc-
ket.IOchamadode client.on('disconnect'),queseráutilizadoparaexcluir
74

## Página 91

CasadoCódigo Capítulo6. Programandosistemasreal-time
umusuáriodasala.Paradescobrirmosemqualsalaousuárioestaconectadousa-
remosafun ção client.get('sala')pararecuperarasala,eemseucallback
iremosremoverousuárioatravésdafun ção: client.leave(sala).
client.on('disconnect', function () {
client.get('sala', function(erro, sala) {
client.leave(sala);
});
});
Parafinalizar,vamosatualizaroevento client.on('send-server'),para
queeleenvieumamensagemsomenteparausuáriosdeumasalaatravésdafun ção
sockets.in(sala).emit('send-client', msg).Tambémvamoscriarum
novoeventochamado: client.broadcast.emit('new-message', data);
—suavariáveldataterácomoparâmetrooe-mailesaladoclienteeeleseráexe-
cutadoparaatualizaraurldobotão ’Conversar’docontatoquereceberumamen-
sagem.
client.on('send-server', function (msg) {
var msg = "<b>"+ usuario.nome +":</b> "+ msg +"<br>";
client.get('sala', function(erro, sala) {
var data = {email: usuario.email, sala: sala};
client.broadcast.emit('new-message', data);
sockets.in(sala).emit('send-client', msg);
});
});
Comonossoback-endimplementado,resta-nosprepararofront-end. Preci-
samosincluirobotão ’Conversar’enviandoemsuaurlo hashdasala. Comisso,
vamoscriarumnovopontodeconexãocomSocket.IO.Estepontoseráimplemen-
tadonaagendadecontatosem views/contatos/index.ejs. Crieumnovo
partialchamado notify_script.ejs,comoseguintecódigo:
<script src="/socket.io/socket.io.js"></script>
<script>
var socket = io.connect('http://localhost:3000');
socket.on('new-message', function(data) {
var chat = document.getElementById('chat_' + data.email);
chat.href += '?' + data.sala;
});
</script>
75

## Página 92

6.6. Gerenciandosalasdochat CasadoCódigo
Agora,atualizeaview contatos/index.ejsparaincluireste partial.Tam-
bémiremosinserirobotão ’Conversar’,permitindoqueonossochataconteçaatra-
vésdanossaagendadecontatos:
<% include .. /header %>
<header>
<h2>Ntalk - Agenda de contatos</h2>
</header>
<section>
<!-- Formulário de novo contato -->
<table>
<thead>
<tr>
<th>Nome</th>
<th>E-mail</th>
<th>Ação</th>
</tr>
</thead>
<tbody>
<% contatos.forEach(function(contato, index) { %>
<tr>
<td><%- contato.nome %></td>
<td><%- contato.email %></td>
<td>
<a href="/contato/<%- index %>">Detalhes</a>
<a href="/chat/<%- contato.email %>"
id="chat_<%- contato.email %>">
Conversar
</a>
</td>
</tr>
<% }) %>
</tbody>
</table>
</section>
<% include notify_script %>
<% include .. /exit %>
<% include .. /footer %>
Reinicieoservidorefaçaoteste!Setudodercerto,significaqueimplementamos
umchatintegradocomosusuáriosdenossaagendadecontatos.
76

## Página 93

CasadoCódigo Capítulo6. Programandosistemasreal-time
6.7 Notificadores na agenda de contatos
Parafinalizarestecapítulocomchavedeouro,vamoscriarumsimplesnotificador
naagendadecontatos.Essenotificadorvaiinformarostatusdecadacontato,que
teráapenastrêsestados:Online,OfflineeMensagem. Visualmenteeleseráum
novocamponatabeladecontatoseiremosexplorarnovasfun çõesdoSocket.IO
paratorná-loreal-time.
Abra o código sockets/chat.js e implemente no início do evento
sockets.on('connection'),umnovaregraqueseguiráaseguintelógica:ar-
mazenaroe-maildousuárioonlineedepoisrodarumloopquecontémtodosos
usuáriosconectadosparaqueemcadaiteraçãosejaenviadoose-mailsviafun ção:
client.emit('notify-onlines', email)paranotificarprópriousuárioe
tambématravésdafunção: client.broadcast.emit('notify-onlines',
email),atualizandoosdemaisusuáriosconectados. Vejacomofaremosissono
códigoaseguir:
sockets.on('connection', function (client) {
var session = client.handshake.session
, usuario = session.usuario;
client.set('email', usuario.email);
var onlines = sockets.clients();
onlines.forEach(function(online) {
var online = sockets.sockets[online.id];
online.get('email', function(err, email) {
client.emit('notify-onlines', email);
client.broadcast.emit('notify-onlines', email);
});
});
// continuação dos eventos...
});
NoSocket.IOtemosafun çãoquepermitequeestabrincadeiraaconte ça. Ela
sechama: sockets.clients()eretornaum arraycontendoosidsdoscli-
entes conectados. Com base noid, retornamos um cliente através da fun-
ção: sockets.sockets[online.id]e em seguida pegamos o seu email (
online.get('email')).NesteprojetotemosdoispontosdeconexõescomSoc-
ket.IO:agendadecontatosechat. Sendoassim,ficainviávelutilizarestalógica
77

## Página 94

6.7. Notificadoresnaagendadecontatos CasadoCódigo
utilizandoo client.id, poisesteidéautogeradoacadavezqueentramose
saímos de um ponto de conexão. Por causa desse motivo utilizamos o e-mail
dousuáriocomoidentificadorchaveatravésdafun ção client.set('email',
usuario.email)antesderodaroloop,possibilitandoiteraro arraydeclientes
cujoatributo store,quecontémosdadosdousuário.
Játemosumnotificadorparausuáriosonlines,agoravamoscriarosnotificado-
resparaosstatus: OfflineeMensagem.Nãohásegredoparaimplementá-los,apenas
temos que reutilizar a função client.broadcast.emit('new-message')
para atualizar o status deMensagem no usuário e implementar a fun-
ção client.broadcast.emit('notify-offline') dentro do evento
client.on('disconnect'),seguindoocódigoabaixo:
client.on('send-server', function (msg) {
var msg = "<b>"+ usuario.nome +":</b> "+ msg +"<br>";
client.get('sala', function(erro, sala) {
var data = {email: usuario.email, sala : sala};
client.broadcast.emit('new-message', data);
sockets.in(sala).emit('send-client', msg);
});
});
client.on('disconnect', function() {
client.get('sala', function(erro, sala) {
var msg = "<b>"+ usuario.nome +":</b> saiu.<br>";
client.broadcast.emit('notify-offline', usuario.email);
sockets.in(sala).emit('send-client', msg);
client.leave(sala);
});
});
Com o back-end desenvolvido, vamos finalizar esta tarefa codificando o
comportamento da view contatos/index.ejs para que sejam renderiza-
dos os status na lista de contatos, vamos fazer essas modificações na view
contatos/notify_script.ejs:
<script src="/socket.io/socket.io.js"></script>
<script>
var socket = io.connect('http://localhost:3000');
var notify = function(data) {
var id = 'notify_' + data.el;
78

## Página 95

CasadoCódigo Capítulo6. Programandosistemasreal-time
var notify = document.getElementById(id);
notify.textContent = data.msg;
};
socket.on('notify-onlines', function(email) {
notify({el: email, msg: 'Online'});
});
socket.on('notify-offline', function(email) {
notify({el: email, msg: 'Offline'});
});
socket.on('new-message', function(data) {
notify({el: data.email, msg: 'Mensagem'});
var id = 'chat_' + data.email;
var chat = document.getElementById(id);
chat.href += '?' + data.sala;
});
</script>
Comissoimplementado,bastaatualizaralistadecontatosparavisualizaras
mensagensdenotificação,editeaview contatos/index.ejsincluindoumatag
<span id="notify_<%- contato.email %>">paraqueocódigojavascript
anteriorfaçaamagia!
<% contatos.forEach(function(contato, index) { %>
<tr>
<td><%- contato.nome %></td>
<td><%- contato.email %></td>
<td><span id="notify_<%- contato.email %>">Offline</span></td>
<td>
<a href="/contato/<%- index %>">Detalhes</a>
<a href="/chat/<%- contato.email %>"
id="chat_<%- contato.email %>">
Conversar
</a>
</td>
</tr>
<% }) %>
Agoratemosonossonotificadorpronto!Paratestá-lo,reinicieoservidor,crie3
contasnoNtalkcadastrandoose-mailsdecadacontacomocontatoentreelaspara
possibilitarumaconversanochat.Porexemplo,cadastrodacontaA,B,Ceoscon-
tatosdacontaAsãoosusuáriosdacontaBeCeassimfaç aomesmocomasdemais
79

## Página 96

6.8. PrincipaiseventosdoSocket.IO CasadoCódigo
paracriaumarededecontatos.
DepoisdissoconversenochatacontaAcomaB,reparequeagoraosstatusvão
sealteraremtemporealdeacordocomainteraç ãodousuário.
Figura6.7:NotificaçõesdaagendadecontatosdoUsuárioA.
6.8 P rincipais eventos doSocket.IO
Paracomplementarseusestudoscomestemódulo,apresentareiabaixoosprincipais
eventosdo Socket.IO,tantonoservidorcomoparacliente.
Noladodoservidor:
•io.sockets.on(‘connection’, function(client))- Evento que
acontecequandoumnovoclienteseconectanoservidor.
•client.on(‘message’, function(mensagem, callback)) -
Ocorrequandoumclientesecomunicaatravésdafun ção send(),ocallback
desseeventorespondeautomaticamenteoclientenofinaldesuaexecuç ão.
•client.on(‘qualquer-nome-de-evento’, function(data))-São
eventoscriadospelodesenvolvedor,qualquernomepodeserapelidadoaqui,
excetoosnomesdoseventosprincipaiseoseucomportamentoédeapenas
receberobjetosatravésdavariável data. Emnossochatcriamosoevento
'send-server'.
80

## Página 97

CasadoCódigo Capítulo6. Programandosistemasreal-time
•client.on(‘disconnect’, callback)-Quandoumclientesaidosis-
temaéemitidooevento 'disconnect'paraoservidor.Tambémépossível
emitiresseeventonoclientesemprecisarsairdosistema.
Noladodocliente:
•client.on(‘connect’, callback)–Ocorrequandooclienteseco-
nectanoservidor.
•client.on(‘connecting’, callback)–Ocorrequandooclienteestá
seconectandonoservidor.
•client.on(‘disconnect’, callback)–Ocorrequandooclientese
desconectadoservidor.
•client.on(‘connect_failed’, callback)–Ocorrequandoocliente
nãoconseguiuseconectarnoservidordevidoafalhasdecomunicaç ãoentre
clientecomservidor.
•client.on(‘error’, callback)–Ocorrequandooclientejáseconec-
tou,porémumerronoservidorocorreuduranteastrocasdemensagens.
•client.on(‘message’, function(message, callback))–Ocorre
quandooclienteenviaumamensagemderespostarápidaaoservidor,cujoo
retornoaconteceatravésdafun çãode callback.
•client.on(‘qualquer-nome-de-evento’, function(data)) –
Eventocustomizadopelodesenvolvedor.Noexemplodowebchatcriamoso
evento 'send-client'queenviamensagemparaoservidor.
•client.on(‘reconnect_failed’, callback)–Ocorrequandoocli-
entenãoconseguesereconectarnoservidor.
•client.on(‘reconnect’, callback)–Ocorrequandooclientesere-
conectaaoservidor.
•client.on(‘reconnecting’, callback)–Ocorrequandoocliente
estásereconectandonoservidor.
Emaisumavezimplementamosumaincrívelfuncionalidadeemnossosistema.
Nopróximocapítuloiremosotimizaraagendadecontatosadicionandoumbanco
dedadosparapersistiroscontatosdosusuáriosetambémincluiremosumhistórico
deconversasnochat.
81

## Página 99

Capítulo7
Integraçãocombancodedados
7.1 Bancos de dados mais adaptados para Node.js
Noscapítulosanteriores(emespecialocapítulo 4,5e6)aplicamosummodelosim-
plesdebancodedados,maisconhecidocomo MemoryStore.Elenãoéummodelo
adequadodepersistênciadedados,poisquandoousuáriosairdaaplicaçãoouoser-
vidorforreiniciado,todososdadosserãoapagados.Utilizamosessemodeloapenas
paraapresentarosconceitossobreosmódulosExpresseSocket.IO.
Nestecapítulo,vamosaprofundarnossosconhecimentostrabalhandocomum
bancodedadosdeverdadeparaNode.js.AlgofortementeligadoaoNode.jssãoos
bancodedadosNoSQL.ÉclaroqueexistemmódulosdebancodedadosSQL,mas
defato,módulosNoSQLsãomaispopularesnestaplataforma.
Agrandevantagemdetrabalharcomessemodelodebancodedadoséagrande
compatibilidadeesuportemantidopelacomunidadeprópriaNode.js. OsNoSQL
popularessão:MongoDB(http://www.mongodb.org),Redis(http://redis.io/),Cou-
chDB(http://couchdb.apache.org)eRiakJS(http://riakjs.com).Dosbancosdeda-

## Página 100

7.1. BancosdedadosmaisadaptadosparaNode.js CasadoCódigo
dosSQLexistemalgunsmódulosparaMySQL(http://www.mysql.com),SQLite
(http://www.sqlite.org)ePostgre(http://www.postgresql.org).
Casoqueiravertodosos driverscompatíveiscomNode.jsvejaestelink:
https://github.com/joyent/node/wiki/Modules#wiki-database
Figura7.1:NoSQLMongoDB.
Nestelivro,utilizaremosoMongoDB,eleéumbancodedadosNoSQL,man-
tidopelaempresa10genefoiescritoemlinguagemC/C++. EleutilizaJavascript
comointerfaceparamanipulaçãodedadoseapersistênciadosdadoséfeitaatravés
deobjetosJSON.Neletrabalhamoscomoconceito schema-less,ouseja,nãoexiste
relacionamentosdetabelas,nemchavesprimáriasouestrangeirasesim documents
quepossuem embeddeddocumentsetudomantidodentrodeuma collection.Outra
vantagemdoschema-lesséqueosatributossãoinseridosouremovidosem runtime,
semanecessidadedetravaruma collection,tornandoestebancodedadosflexívela
grandesmudanças.Comodisseantes,comoMongoDBpodemospersistir embed-
deddocumentsdentrodeum document,queseriaomesmoquecriarrelacionamento
entretabelas,porémnesteconceitotudoéinseridoemumamesmatabela(emum
mesmodocument).Issodiminuionúmerodeconsultascomplexasnobancodeda-
doseprincipalmenteevitacriar joinsparacarregardiversasinformaçõesdeumavez.
NãovamosentraremdetalhessobrecomoinstalaroMongoDBouutilizá-lo.
Parasimplificaronossoaprendizadoutilizaremosasconfiguraçõespadrõesquejá
vemaoinstalá-lo.Parainstalaretambémconhecermaisafundoessebancodedados
visiteseusiteoficial:
http://mongodb.com
84

## Página 101

CasadoCódigo Capítulo7. Integraçãocombancodedados
7.2 MongoDB noNode.js utilizandoMongoose
OMongoosepossuiumainterfacemuitofácildeaprender.Empoucoscódigos,você
vaiconseguircriarumaconexãonobancodedadoseexecutarumaqueryouper-
sistirdados. ComoMongoDBinstaladoefuncionandoemsuamáquina,vamos
instalaromódulo mongoose,queéumframeworkresponsávelpormapearobjetos
doNode.jsparaMongoDB.Atualizeno package.json:
"dependencies": {
"express": "3.4.7",
"express-load": "1.1.8",
"ejs": "0.8.5",
"socket.io": "0.9.16",
"mongoose": "3.8.4"
}
Eemseguidaexecuteocomando:
npm install
Paraaaplicaçãoseconectarcomobancodedados,no app.js,utilizaremos
avariável dbemmodoglobalparamanterumaconexãocomobancodedados
compartilhandoseusrecursosemtodoprojeto:
var express = require('express')
, app = express()
, load = require('express-load')
, error = require('./middleware/error')
, server = require('http').createServer(app)
, io = require('socket.io').listen(server)
, mongoose = require('mongoose');
global.db = mongoose.connect('mongodb://localhost/ntalk');
Quando é executada a função mongoose.connect cria-se uma conexão
comobancodedadosMongoDBparaoNode.js. ComooMongoDBé schema-
less, na primeira vez que a aplicação se conecta com o banco através da url
'mongodb://localhost/ntalk'automaticamenteem run-timeécriadauma
basededadoscomonome ntalk.
85

## Página 102

7.3. ModelandocomMongoose CasadoCódigo
7.3 Modelando com Mongoose
OMongooseéummódulofocadoparaacriaç ãode models, issosignificaque
comelecriaremosobjetospersistentesmodelandoseusatributosatravésdoobjeto
mongoose.Schema. Apósaimplementaçãodeummodelo,temosqueregistrá-
lo no banco de dados, utilizando a função db.model('nome-do-model',
modelSchema),querecebeummodeloecriasuarespectiva collectionnoMon-
goDB.
VamosexplorarasprincipaisfuncionalidadesdoMongooseaplicandonaprá-
ticaemnossoprojeto. Comisso,faremosdiversos refactoringsemtodaaplicação
parasubstituiromodelodepersistênciavia sessionparaomodelodoMongooseque
armazenadadosnoMongoDB.
Para começar vamos criar o modelo usuario.js no diretório mo-
dels. Ele será o modelo principal e terá os seguintes atributos:nome,
email e contatos. A modelagem dos atributos acontece através do objeto
require('mongoose').Schema,vejaabaixocomoficaráestamodelagem:
module.exports = function(app) {
var Schema = require('mongoose').Schema;
var contato = Schema({
nome: String
, email: String
});
var usuario = Schema({
nome: {type: String, required: true}
, email: {type: String, required: true
, index: {unique: true}}
, contatos: [contato]
});
return db.model('usuarios', usuario);
};
Reparequeforamcriadosdoisobjetos usuarioe contato,eapenasfoiregis-
tradoomodelo usuario,pois contatoseráumsubdocumentode usuarioeo
registroocorreviafun ção app.db.model().Outrodetalheimportante:incluímos
doistiposdevalidaçõesnestemodelo,quesão: requirede unique.Paraquem
nãoconheceo required: truevalidaseoseuatributopossuialgumvalor,ou
86

## Página 103

CasadoCódigo Capítulo7. Integraçãocombancodedados
seja,elenãopermitepersistirumcampovazio.Jáo unique: truecriaumíndice
devalorúnicoemseuatributo,semelhantenosbancosdedadosSQL.Estasvalida-
çõesgeramumerroqueéenviadonocallbackdequalquerfun çãodepersistência
domodelo,porexemplo, usuario.create()ou usuario.update().
7.4 Implementando um CRUD na agenda de contatos
Comomodeloimplementado,oquenosrestaafazeréalteraroscontrollerspara
utilizaremsuasfun ções. Começandodomaisfácil,vamosmodificarocontroller
home.js.Nele,executaremosafun ção findOne,queretornaapenasumobjeto,
eafun ção select('name email'),quefiltraesseobjetoretornandoumnovo
objetocontendoapenasosatributos namee email.Comisso,evita-sequesejacar-
regadoosubdocumento contatos.Naprática,estaqueryseriaalgoqueembanco
dedadosSQLfaríamoscomoseguintecomando: SELECT * FROM usuario
LIMIT 1. Casonãosejaencontradoumusuário,cadastraremosumnovoatravés
dafunção Usuario.create.Vejaabaixoocódigo-fonte:
login: function(req, res) {
var query = {email: req.body.usuario.email};
Usuario.findOne(query)
.select('nome email ')
.exec(function(erro, usuario){
if (usuario) {
req.session.usuario = usuario;
res.redirect('/contatos');
} else {
Usuario.create(req.body.usuario, function(erro, usuario) {
if(erro){
res.redirect('/');
} else {
req.session.usuario = usuario;
res.redirect('/contatos');
}
});
}
});
}
Reparequecomo Mongooseépossívelcriarqueriescomplexaschamandofun-
çõesqueemseuretornopermitechamarumaoutrafun ção.Issoformaumencade-
87

## Página 104

7.4. ImplementandoumCRUDnaagendadecontatos CasadoCódigo
amentodefun çõeseofinaldesseencadeamentoocorrequandochamamosafun ção
exec().Umbomexemplodissoéaqueryabaixo:
Usuario.findOne(req.body.usuario)
.select('nome email ')
.exec(function(erro, usuario) {
// continuação do código...
});
Afunção Usuario.createpersisteumobjetoquetenhaosmesmoatributos
deseumodelo,casocontrárioocorreráumerroeosdetalhesdeleseráenviadopara
variávelerropresentenocallback.Porestemotivoérecomendávelsempretratar
esseserrosparagarantirestabilidadenosistema.
Parabéns!Comocontroledeloginfuncionandocorretamente,sófaltamodifi-
carocontroller contatos.jsesuasrespectivasviews.Nestaetapaexploraremos
novasfunçõesdoMongoDBatravésdomodelo Usuario,vejaabaixoasmudan ças
decada action:
index: function(req, res) {
var _id = req.session.usuario._id;
Usuario.findById(_id, function(erro, usuario) {
var contatos = usuario.contatos;
var resultado = { contatos: contatos };
res.render('contatos/index', resultado);
});
}
Naaction indexutilizamosafun ção Usuario.findById()queretornaape-
nasumusuáriobaseadono _idemparâmetro,essafun çãoseráosuficientepara
retornarosdadosdousuárioetodososseuscontatos.
create: function(req, res) {
var _id = req.session.usuario._id;
Usuario.findById(_id, function(erro, usuario) {
var contato = req.body.contato;
var contatos = usuario.contatos;
contatos.push(contato);
usuario.save(function() {
res.redirect('/contatos');
});
});
}
88

## Página 105

CasadoCódigo Capítulo7. Integraçãocombancodedados
Jánaaction create,temosapenasqueatualizaralistadecontatosincluindoum
novocontato. Paraisso,buscamosousuárioviafun ção Usuario.findById()
e em seu callback atualizamos oarray usuario.contatos com a fun-
ção: contatos.push(contato) e em seguida é executado a função
usuario.save().
show: function(req, res) {
var _id = req.session.usuario._id;
Usuario.findById(_id, function(erro, usuario) {
var contatoID = req.params.id;
var contato = usuario.contatos.id(contatoID);
var resultado = { contato: contato };
res.render('contatos/show', resultado);
});
},
edit: function(req, res) {
var _id = req.session.usuario._id;
Usuario.findById(_id, function(erro, usuario) {
var contatoID = req.params.id;
var contato = usuario.contatos.id(contatoID);
var resultado = { contato: contato };
res.render('contatos/edit', resultado);
});
}
As actions show e edit possuem o mesmo comportamento. Eles
retornam os dados de um específico contato do usuário através da função
usuario.contatos.id(contatoID)queéumafunçãodo embeddeddocument
contatosqueretornaumcontatobaseadoemseu _id.
update: function(req, res) {
var _id = req.session.usuario._id;
Usuario.findById(_id, function(erro, usuario) {
var contatoID = req.params.id;
var contato = usuario.contatos.id(contatoID);
contato.nome = req.body.contato.nome;
contato.email = req.body.contato.email;
usuario.save(function() {
res.redirect('/contatos');
});
89

## Página 106

7.4. ImplementandoumCRUDnaagendadecontatos CasadoCódigo
});
}
Nestaaction,aimplementaçãodo updatenãotemsegredos.Como contatos
éumembeddeddocument,seutratamentoésemelhanteàsfun çõesdeum array,
porissopraticamentebuscamosousuáriodeacordocomseu _idviafun ção
Usuario.findById().Emseguida,buscamososeurespectivocontatocombase
emseu contatoID,eatualizamosseusatributosnormalmente.Quandoexecuta-
mosafun ção usuario.save(),ocontatoseráatualizadonabasededados.
destroy: function(req, res) {
var _id = req.session.usuario._id;
Usuario.findById(_id, function(erro, usuario) {
var contatoID = req.params.id;
usuario.contatos.id(contatoID).remove();
usuario.save(function() {
res.redirect('/contatos');
});
});
}
Em destroy, temos três ações para excluir um contato. Primeiro,
buscamos um contato via função Usuario.findById(), em seguida, bus-
camos um específico contato do usuário já o excluindo através da linha
usuario.contatos.id(contatoID).remove()eparafinalizaratualizamos
osdadosdousuárioexecutando: usuario.save().
Parafinalizarvamosatualizarasviewsdocontato.Aediç ãoserábemsimples,
vamosapenastrocaramaneiracomoelesrenderizamo iddocontatonasurls.
Vejaabaixocomofaremosestaatualiza ção. Abraasviews contatos/edit.ejs
e contatos/show.ejs,nelesmudeapenasaurlda actiondeseusrespectivos
form,renderizandooatributo contato._id:
<form action="/contato/<%- contato._id %>" method="post">
Agoranaview contatos/index.ejsalteraremosasurlsdoslinkgeradosna
iteraçãodoloopdecontatos:
<% contatos.forEach(function(contato) { %>
<tr>
<td><%- contato.nome %></td>
90

## Página 107

CasadoCódigo Capítulo7. Integraçãocombancodedados
<td><%- contato.email %></td>
<td>
<span id="notify_<%- contato.email %>" class="label">
Offline
</span>
</td>
<td>
<a href="/contato/<%- contato._id %>">Detalhes </a>
<a href="/chat/<%- contato.email %>"
id="chat_<%- contato.email %>">Conversar
</a>
</td>
</tr>
<% }) %>
Comasviewsfinalizadasterminamosonosso refactoringnaagendadeconta-
tos. Paraverificarsetudoocorreubem,reinicieoservidoreconfiraasnovidades
nosistema. DessaveztemosumsistemaintegradoaoMongoDB,persistindoseus
contatos,cadastrandousuárioefazendologincorretamente.
7.5 Persistindo estruturas de dados com NoSQLR e-
dis
ComnossaagendaintegradaaoMongoDBepersistindocontatosnobancodedados,
precisamosagorapersistirdadosdasconversasdochatdaaplicaç ão,paraqueele
mantenhaumhistóricodeconversas.
Comoochatéseráumaáreademaioracesso,precisamosarmazenarseusdados
emumaestruturasimplesdechave-valorequepermitaleiturasmuitorápido.Para
manterestetipodeestruturaoMongoDBnãoseriaumaboasoluç ão,poisprecisa-
mosdeumbancodedadosquemantenhadadosfrequentementeemmemóriapara
garantirumaleiturarápidadeles.ElesechamaRedis.
91

## Página 108

7.6. Mantendoumhistóricodeconversasdochat CasadoCódigo
Figura7.2:NoSQLRedis.
ORedisguardaebusca,emsuabasededados,elementoschave-valor,dema-
neiraextremamenterápida,poismantémosdadosemgrandepartedotempona
memória,fazendoemcurtosperíodosasincroniza çãodosdadoscomdiscorígido.
EleéconsideradoumNoSQLdotipoemchave-valor,emqueachaveéoidentifica-
doreovalorpodeserdiversostiposdeestruturasdedados.
Asestruturasdedadosqueeletrabalhasão: Strings,Hashes,Lists,SetseSor-
tedSets. EelepossuiumCLI(atravésdocomando redis-cli)quepermiteem
runtimebrincarcomseusinúmeroscomandos—aliás,sãovárioscomandosquere-
alizamoperaçõescomosdados,valeapenadarumaolhadaemsuadocumentaç ão:
http://redis.io/commands
7.6 Mantendo um histórico de conversas do chat
UtilizaremosoRedisparaimplementarohistóricodeconversasdonossochat.Basi-
camentevamospersistircadamensagememumalista,agrupando-aemumachave
queseráo iddasaladochat. Issovaifazercomqueousuárioquereceberuma
mensagemconsigavisualizá-laapósclicarnobotão "Conversar”.
AssimcomofoinoMongoDB,nãoentraremosemdetalhessobrecomoinstalar
econfiguraroRedis. Etodososexemplosdestelivrofoiutilizadoaconfiguraç ão
padrãodele.ParabaixareinstalaroRedisvisiteestelink:
http://redis.io/download
JáconsiderandoqueoRedisestainstalandoefuncionandocorretamenteemsua
máquina,instalaremosseudrivercompatívelcomNode.jseummóduloadicional,
éumwrapperqueaumentaperformancedoRediscomNode.js,permitindoproces-
samentoassíncronoeoutrasotimizaçõesdebaixonívelnasoperaçõesdoRedis,ele
92

## Página 109

CasadoCódigo Capítulo7. Integraçãocombancodedados
sechamaHi-Redis,apenasinstale-oqueoprópriomóduloRedisutilizaráautomati-
camente.Noterminal,executeocomando:
npm install redis hiredis --save
ComoRediseseurespectivodriverinstaladoscorretamente,vamosaoquein-
teressa,queéimplementarohistóricodochat.Abraocódigo sockets/chat.js,
será nele que iremos conectar o driver com o servidor Redis para habili-
tar seus comandos na aplicação. É a partir da execução de redis =
require('redis').createClient(),quecome çatudo.Praticamente,elecar-
rega o driver e retorna um cliente Redis. Como o banco Redis e a aplicação
Node.jsestãohospedadosnamesmamáquinaeutilizamosasconfiguraçõespa-
drõesdoRedis,entãonãohánecessidadedeenviarparâmetrosextrasparafun ção
createClient().Casovocênecessiteconectardeumlocaldiferente,apenasin-
cluaosseguintesparâmetros: createClient(porta, ip). Vejaabaixocomo
seráonossocódigo:
module.exports = function(io) {
var crypto = require('crypto')
, redis = require('redis').createClient()
, sockets = io.sockets;
// continuação dos eventos do socket.io...
}
AgoracomumclienteRedisemação,vamosimplementaralgumasdesuasfun-
çõesparapesquisarepersistirasmensagens.Utilizaremosaestruturalistaparaar-
mazenarasmensagens.Cadalistateráumasalacomochaveparapesquisa.Primeiro
vamosimplementá-lanoevento client.on('join'):
client.on('join', function(sala) {
if(sala){
sala = sala.replace('?','');
} else {
var timestamp = new Date().toString();
var md5 = crypto.createHash('md5');
sala = md5.update(timestamp).digest('hex');
}
client.set('sala', sala);
93

## Página 110

7.6. Mantendoumhistóricodeconversasdochat CasadoCódigo
client.join(sala);
var msg = "<b>"+usuario.nome+":</b> entrou.<br>";
redis.lpush(sala, msg, function(erro, res) {
redis.lrange(sala, 0, -1, function(erro, msgs) {
msgs.forEach(function(msg) {
sockets.in(sala).emit('send-client', msg);
});
});
});
});
Basicamenteutilizamosduasdesuasfun ções: primeiroexecutamosafunção
redis.lpush(sala, msg)queadicionanalistaamensagem. Depoisemseu
callbackutilizamosafun ção redis.lrange(sala, 0, -1)queretornaumar-
raycontendooselementosapartirdeumrangeinicialefinaldalista.Orangeutiliza
doisíndices,enestecasooíndiceinicialé 0eofinalé -1. Quandoinformamos
ovalor -1noíndicefinalindicamosqueorangeserátotal,retornandotodosos
elementosdalista.Porúltimo,nocallbackdo redis.lrange()iteramosoarray
demensagensemitindomensagempormensagemparaocliente.
Agora para finalizar o nosso histórico do chat, implementaremos a função
redis.lpushnoseventos send-servere disconnect. Comoesteseven-
tosenviamumaúnicamensagem, simplificaremosocódigoincluindoafun ção
redis.lpush(sala, msg)semutilizarcallbacks:
client.on('send-server', function (msg) {
var msg = "<b>"+ usuario.nome +":</b> "+ msg +"<br>";
client.get('sala', function(erro, sala) {
redis.lpush(sala, msg);
var data = {email: usuario.email, sala : sala};
client.broadcast.emit('new-message', data);
sockets.in(sala).emit('send-client', msg);
});
});
client.on('disconnect', function() {
client.get('sala', function(erro, sala) {
var msg = "<b>"+ usuario.nome +":</b> saiu.<br>";
redis.lpush(sala, msg);
client.broadcast.emit('notify-offline', usuario.email);
94

## Página 111

CasadoCódigo Capítulo7. Integraçãocombancodedados
sockets.in(sala).emit('send-client', msg);
client.leave(sala);
});
});
Emaisumavezterminamosumexcelentecapítulo!Agoratemosumaaplicaç ão
100%funcionalqueutilizadoisbancodedadosNoSQL.Acredite,oquejátemos
aquijáéosuficienteparacolocaraaplicaçãonoar.Mascontinuelendo,afinalnos
próximoscapítulosvamosaprofundarnossosconhecimentoscodificandotestese
tambémotimizandoosistemaparaqueeleentreemumambientedeproduç ãode
formaeficiente.
95

## Página 113

Capítulo8
Preparandoumambientedetestes
8.1 Mocha, o framework de testes para Node.js
Testesautomatizadoséalgocadavezmaisadotadonomundodedesenvolvimento
desistemas.Existemdiversostiposdetestes:testeunitário,testefuncional,testede
aceitação,entreoutros.Nestecapítulofocaremosapenasnotestedeaceitaç ão,parao
qualtemosalgunsframeworkspararealizá-lo.Omaisrecenteequeandaganhando
visibilidadepelacomunidade,éoMocha,seusiteé
http://visionmedia.github.io/mocha

## Página 114

8.2. CriandoumEnvironmentparatestes CasadoCódigo
Figura8.1:Mocha-Frameworkparatestes
EleémantidopelomesmocriadordoExpress(TJHolowaychuk),efoicriado
comasseguintescaracterísticas:testenoestiloTDD,testesnoestiloBDD,cobertura
decódigo,relatórioemHTML,testedecomportamentoassíncrono,integraç ãocom
osmódulos: shoulde assert.Praticamente,eleéumambientecompletopara
desenvolvimentodetestes.Possuidiversasinterfacesdeapresentaç ãodoresultado
dostestes.Nasse çõesaseguir,apresentareioMocha,desdeasuaconfiguraç ãoatéa
implementaçãodetestesnoprojetoNtalk.
8.2 Criando um Environment para testes
Antesdeentrarmosafundonostestes,primeirotemosquecriarumnovoambi-
entecomconfiguraçõesespecíficasparatestes. Issoenvolvecriarumafun çãoque
contenhainformaçõesparaseconectaremumabancodedadosdetestesedede-
senvolvimento. Comissovamosmigrarafun ção mongoose.connectparaeste
novoarquivo,paraqueeleretorneumaconexãodebancodedadosdeacordocom
oambiente.Paraidentificaremqualambienteestaoprojeto,utilizamosavariável
process.env.NODE_ENV.
Vamoscriarumnovodiretório,responsávelpormanterbibliotecasexternas,ela
sechamaráde lib,nelevamoscriaroarquivo db_connect.jseinseriralógica
abaixo:
module.exports = function() {
var mongoose = require('mongoose');
var env_url = {
"test": "mongodb://localhost/ntalk_test"
98

## Página 115

CasadoCódigo Capítulo8. Preparandoumambientedetestes
, "development": "mongodb://localhost/ntalk"
};
var url = env_url[process.env.NODE_ENV || "development"];
return mongoose.connect(url);
};
Lendo v ariáveis de ambiente no Node
Quandosetrabalhacomvariáveisdeambienteémuitocomumper-
sistirdadosdeconfiguraçõesnosistemaoperacional. Urldeacessoa
bancodedadosououtrosserviços,assimcomosenhasechavesimpor-
tantesdeacessoasistemasexternossãoalgunsexemplosdevariáveis
deambiente. Essesdadossãoconfiguradosemumarquivonopróprio
sistemaoperacional. Nocapítulo1foiexplicadocomocriaravariável
NODE_ENV,paraoutrasvariáveissefazomesmoprocedimento. Eno
Node.jspodemoslê-lasatravésdo process.env["VARIAVEL"],que
éumobjetoJSONquecontémtodasasvariáveisdosistemaoperacional.
Comessafun çãopreparada,podemosremoverocarregamentodo mongoose
esuavariável global.dbdentrodo app.js.Afinalquantomenosvariáveisglo-
baisexistiremnaaplicaçãomelhor. Comopreparamosuma libqueretornauma
conexãodeacordocomavariáveldeambiente NODE_ENV,ocarregamentodo
db_connect.jsserádiretamentenomodelo models/usuario.js:
module.exports = function(app) {
var db = require('../lib/db_connect')()
, Schema = require('mongoose').Schema;
var contato = Schema({
nome: String
, email: String
});
var usuario = Schema({
nome: { type: String, required: true }
, email: { type: String, required: true
, index: {unique: true} }
, contatos: [contato]
99

## Página 116

8.3. InstalandoeconfigurandooMocha CasadoCódigo
});
return db.model( 'usuarios', usuario);
};
Dessa forma mantemos nossa aplicação com nenhuma variável global, e a
variável db que mantém uma conexão com MongoDB será gerenciada pelo
db_connect.js.
Pronto! Essafoiumademonstraçãosimplesdecomosuaaplicaç ãovaiseau-
toconfigurar. Comessasconfiguraçõeselaestarápreparadaparadesenvolvimento
multi-ambiente.Aprincípiosócriamosuma libqueretornaumainstânciadecone-
xãocombancodedadosdeacordocomsuavariáveldeambiente,masemaplicações
maiscomplexas,utiliza-semuitodesseconceitoparacriaroutrostiposde libs.
8.3 Instalando e configurando o Mocha
ParacomeçarmoscomoMochavamosinstalá-loemmodoglobalparaautilizaç ão
doseuCLI.Emseuconsoleexecuteocomando:
npm install -g mocha
O Mocha é um módulo focado em testes e vamos adicioná-lo no
package.json, porém ele não será incluído dentro dedependencies. O
motivoéquedefatoeleémuitopesadoenãoéumframeworkparasercarregado
em um ambiente de produção. Neste caso, existe um outro atributo chamado
devDependencies, que é utilizado para integrar módulos específicos para
automatizaçãodetestesedeploy.
"devDependencies": {
"mocha": "*"
}
Na seção seguinte implementaremos alguns testes utilizando interface BDD
(Behavior Driven-Development)para usar funções como describe, it,
beforeEach, shouldeoutras. Afunção shouldfazverificaçõesemcimados
resultadosdecadatestes,porémelanãoénativadoframeworkMocha,comisso
teremosquehabilitá-lainstalandooseuprópriomódulo,o should.
"devDependencies": {
"mocha": "*",
100

## Página 117

CasadoCódigo Capítulo8. Preparandoumambientedetestes
"should": "*"
}
ParaexplorarmosoMocha,implementaremosapenastestesfuncionalsobreas
rotasdaaplicação.Pararealizaressetipodetesteprecisamosdeummóduloquefaç a
requisiçõesemnossoservidor.Testarrequisiçõessobreasrotasémuitoútil,poisper-
miteverificarcomoseráocomportamentodeumarequisiç ãofeitaporumusuário.
Pararealizaressestestes,utilizaremosomódulo supertestquetambémnasceu
peloosmesmoscriadoresdoMocha. Adicioneessemódulono package.json,
seguindoocódigoabaixo:
"devDependencies": {
"mocha": "*",
"should": "*",
"supertest": "*"
}
Parafinalizar,crieodiretório test,queseráolocalemquecodificaremosos
testesdaaplicação,einstaletodososmódulosatravésdocomando: npm install.
8.4 Rodando o Mocha no ambiente de testes
Assimcomocriamoso db_connect.js,queéumsimplesscriptqueretornauma
conexãoMongoDBbaseadonovalordavariável NODE_ENV,temosqueexecutaros
testesutilizandoestavariávelcomvalor 'test'pararodarostestesnoseudevido
ambiente. ParaexecutartestescomoMocha,umsimplescomandonoterminal:
mocha testjáseráosuficiente,masnestecasoelenãoseráexecutadonoambiente
detestes.Ocomandocorretoé NODE_ENV=test mocha test,poiseledefineo
valorde NODE_ENVpara test.Masexecutaressecomandolongoseriaumpouco
cansativo,ecomoumbomprogramadortemqueserpreguiçoso,quetalsimplificá-
lo?
Umaboapráticaparasimplificarestecomandoéutilizaro package.json
paradefinircomandosdentrodoatributo "scripts". Eleseráconvertidopara
umcomandoexecutávelvia npm—pordefault,jáexisteumcomandono npm
paraexecutarestetipodetarefa.Vejaocódigoabaixo,queseráincluídodentrodo
package.json:
"scripts": {
"start": "node app",
101

## Página 118

8.5. Testandoasrotas CasadoCódigo
"test": "NODE_ENV=test ./node_modules/mocha/bin/mocha test/*.js"
}
Porque usamos o mocha da pasta node_modules?
Dentrodonossoprojeto,cadadependênciadeleficalocalizadaden-
trodapasta node_modules.Apenasmódulosglobais,ficamforadesta
pasta,afinalelessãoarmazenadosemumapastaespecíficaquevariade
acordocomosistemaoperacional. Quandoutilizamososcomandos
npm testou npm start,qualquerutilizaçãodemódulodeveobri-
gatoriamenteserchamadadentrododiretório node_modules,porque
estecomandogeralmenteéutilizadoporserviçosdeterceiros.Umbom
exemplodeserviçoéoTravisCI(http://travis-ci.org),umserviçode
deploycontínuocompatívelcomdiversaslinguagens,inclusiveNode.js.
Elerodaostestesdoseuprojetoatravésdocomando npm testdoseu
package.json.Elenãoinstalamódulosglobais,apenasutilizaosmó-
dulosexistentesno node_modules.
Foramadicionadosdois "scripts",o "start"eo "test".Estessãoosco-
mandosatalhosdo npm,ouseja,agoraostestesserãoexecutadosviacomando npm
testeaaplicaçãoseráiniciadaviacomando npm start. Dentrode scripts
vocêpodecriarquantoscomandosquiseretodoselesserãoexecutadosviacomando:
npm run [nome-do-comando].
8.5 Testando as rotas
Omódulo supertestseráintensivamenteusadoeantesdecriarmosostesteste-
mosqueexportaravariável appdo app.jsparaqueautomaticamentelevanteuma
instânciadeservidorparaostestes.Este refactoringémuitosimples,apenasin-
cluanaúltimalinhado app.jsoseguintetrecho:
// Trecho final do app.js...
module.exports = app;
Feitoissoagorapodemoscriarostestes.Dentrododiretório testcrieoarquivo
home.js.Noprimeirotestesimularemosumarequisiç ãoparaarotaprincipal "/”
esperandoqueretorneostatus200comosucessodarequisiç ão.
102

## Página 119

CasadoCódigo Capítulo8. Preparandoumambientedetestes
var app = require('../app')
, should = require('should')
, request = require('supertest')(app);
describe('No controller home', function() {
it('deve retornar status 200 ao fazer GET / ', function(done){
request.get('/')
.end(function(err, res){
res.status.should.eql(200);
done();
});
});
// continuação...
Nomesmoarquivo,implementaremosotesteabaixoquefazumarequisiç ãopara
rota"/sair”,eseucomportamentodesucessoéreceberumredirecionamentopara
rotaprincipal"/”,queseráoretornodavariável:res.headers.location.
it('deve ir para rota / ao fazer GET /sair ', function(done){
request.get('/sair')
.end(function(err, res){
res.headers.location.should.eql('/');
done();
});
});
Aquijácomplicamosoteste,simulamosumPOSTenviandoparâmetrosválidos
(nome e email),quefazumlogineéredirecionadopararota "/contatos”.
it('deve ir para rota /contatos ao fazer POST /entrar ', function(done){
var login = {usuario: {nome: 'Teste', email: 'teste@teste'}};
request.post('/entrar')
.send(login)
.end(function(err, res){
res.headers.location.should.eql('/contatos');
done();
});
});
Esteúltimoteste,ésemelhanteaoanterior,adiferen çaéqueenviamosparâme-
trosinválidosdelogin,paraquesejatestadoocomportamentoderedirecionamento
darota.
103

## Página 120

8.5. Testandoasrotas CasadoCódigo
it('deve ir para rota / ao fazer POST /entrar ', function(done){
var login = {usuario: {nome: '', email: ''}};
request.post('/entrar')
.send(login)
.end(function(err, res){
res.headers.location.should.eql('/');
done();
});
});
}); // fim da função describe()
Essefoionossotestecomarota home.js.Cadatestedeixeibemdescritivoe
atômico,realizandoapenasumaúnicaverificaçãoatravésdafunção should.Vamos
rodarostestesparaversetudodeucerto?
Paraexecutarostestes,ésimples!Comojáconfiguramosno package.jsono
scriptparaexecuçãodetestes,executenoterminalocomando npm test.Evejao
resultadodosseustestessemelhantesaodaimagemabaixo:
Figura8.2:Ostestesemhome.jspassaramcomsucesso.
Reparemquesurgiramdoisprintsdosistemaquesóaparecemquandolevanta-
mososervidor,eemseguidaapareceoresultadodostestes. Issoaconteceporque
em app.jsexportamosavariávelquecontémasfun çõesdoservidordaaplica-
ção,o module.exports = app. Nostestes,quandocarregamosestemóduloe
injetamosdentrodo require('supertest')(app),eleseencarregadeiniciar
oservidorparaqueo supertesttenhaasinformaçõesnecessáriasparaemular
requisiçõeseassimpermitirquefaçamosostestesfuncionaisdasrotas.
104

## Página 121

CasadoCódigo Capítulo8. Preparandoumambientedetestes
Agorairemosexplorarnovasfun çõesdoMocha,testandoasrotasdocontrol-
ler contatos.js.Comoestecontrollerpossuiumfiltroqueverificaseexisteum
usuáriologadonosistema,implementaremosdoiscasosdetestes:umcasodetestes
parausuáriologadoeumcasoparaumusuárionãologado.
Crieoarquivo test/contatos.js.Nelevamoscriarum describescom
dois sub-describesqueserãoutilizadosparacriaroscasosdetestesparausuário
logadoenãologado.
var app = require('../app')
, should = require('should')
, request = require('supertest')(app);
describe('No controller contatos', function() {
describe('o usuario nao logado ', function() {
// testes aqui...
});
describe('o usuario logado ', function() {
// testes aqui...
});
});
Nocasodetestesparausuárionãologadoimplementaremosossimplestes-
tesdeverificações,semelhanteaoqueutilizamosno test/home.js. Afinal,em
routes/contatos.js,existeumfiltroqueirábarrarumusuárionãologado,fa-
zendocomquearequisiçãosejaredirecionadaparaarotaprincipal: ’/’.
Para simplificar, seguem todos os testes que serão inseridos dentro de
describe('o usuario nao logado'):
it('deve ir para / ao fazer GET /contatos ', function(done){
request.get('/contatos').end(function(err, res) {
res.headers.location.should.eql('/');
done();
});
});
it('deve ir para / ao fazer GET /contato/1 ', function(done){
request.get('/contato/1').end(function(err, res) {
res.headers.location.should.eql('/');
105

## Página 122

8.5. Testandoasrotas CasadoCódigo
done();
});
});
it('deve ir para / ao fazer GET /contato/1/editar ', function(done){
request.get('/contato/1/editar').end(function(err, res) {
res.headers.location.should.eql('/');
done();
});
});
it('deve ir para / ao fazer POST /contato ', function(done){
request.post('/contato').end(function(err, res) {
res.headers.location.should.eql('/');
done();
});
});
it('deve ir para / ao fazer DELETE /contato/1 ', function(done){
request.del('/contato/1').end(function(err, res) {
res.headers.location.should.eql('/');
done();
});
});
it('deve ir para / ao fazer PUT /contato/1 ', function(done){
request.put('/contato/1').end(function(err, res) {
res.headers.location.should.eql('/');
done();
});
});
Reparemqueotestedentrode describe('o usuario nao logado')foi
muitorepetitivo. Issoocorrepoisofiltroqueaplicamosno capítulo4 vaibarrar
qualquerrequisiçãodeusuárionãoautenticadopelologin,porissooresultadocor-
retoéquetodosostestesredirecionemparaarotaprincipaldosistema,queéatela
delogin.
Maisumavezvamosrodarostestesparateracertezadequetudoocorreubem
naimplementaçãodostestes.Dessavezvamosveremmaisdetalhesosresultados.
Paraisso,executeocomando mocha test --reporter spec,eosresultados
serãoapresentadosnoformatosemelhanteaoframeworkRSpecdalinguagemRuby,
igualàimagemabaixo:
106

## Página 123

CasadoCódigo Capítulo8. Preparandoumambientedetestes
Figura8.3:ResultadodostestesutilizandoReporterSpec.
OmaislegaldoMochaéqueelepossuidiversos reporters,permitindoquevocê
tenhaváriasopçõesparacustomizaroresultadodeseustestes.Paraconheceroutros
formatosdereportersvejaestelink:
http://visionmedia.github.io/mocha/#reporters
No describe('o usuario logado'),teremosqueemularumusuárioau-
tenticado,ouseja,umusuárioquefezumloginnosistema.Paraissoutilizaremos
duasestratégias:
1) Cadatestedeve,antes,fazerumarequisição POSTnarotadelogin.
2) Omesmotestedevemanterum cookieválido,geradoapósologinobtersucesso,
parapularofiltro.
Para implementar essa rotina, utilizaremos a função beforeEach(), que
é executada antes de cada teste. Dentro dessa função, faremos um lo-
gin no sistema para capturar o seucookie, que é encontrado dentro de
res.headers['set-cookie']. Nisso,armazenaremosseuresultadoemuma
variável que estará no mesmo escopo da função describe('o usuario
107

## Página 124

8.5. Testandoasrotas CasadoCódigo
logado')paraquesejareutilizadoemcadaumdeseustestes.Paraentenderme-
lhor,vejaocódigoabaixo:
describe('o usuario logado', function() {
var login = {usuario: {nome: 'Teste', email: 'teste@teste'}}
, contato = {contato: {nome: 'Teste', email: 'teste@teste'}}
, cookie = {};
beforeEach(function(done) {
request.post('/entrar')
.send(login)
.end(function(err, res) {
cookie = res.headers['set-cookie'];
done();
});
});
// implementação dos testes...
});
Comavariávelcookierecebendoosdadosdeumusuárioautenticado,ficaviá-
veltestarocomportamentodasrotaspós-filtro.Paraexecutarostestes,temosque
injetaro cookieemcadarequisição,eissosefazvia req.cookies = cookie.
Vamosimplementá-los?Abaixoutilizaremosestatécnica,masinfelizmentetestare-
mosapenasalgumasrotas.Apósaapresentaç ãodostestesexplicareiomotivo.
AquitestamosumarequisiçãoGETnarota /contatos:
// função beforeEach()...
it('deve retornar status 200 em GET /contatos', function(done){
var req = request.get('/contatos');
req.cookies = cookie;
req.end(function(err, res) {
res.status.should.eql(200);
done();
});
});
Notesteabaixo,emulamosumarequisiç ãoPOSTnarota /contato,testandoo
comportamentodocadastrodeumcontato:
it('deve ir para rota /contatos em POST /contato ', function(done){
var contato = {contato: {nome: 'Teste', email: 'teste@teste'}};
108

## Página 125

CasadoCódigo Capítulo8. Preparandoumambientedetestes
var req = request.post('/contato');
req.cookies = cookie;
req.send(contato).end(function(err, res) {
res.headers.location.should.eql('/contatos');
done();
});
});
}); // fim da função describe()
Eentãovemapergunta,porquenãoforamtestadastodasasrotasparaumusuá-
riologado?Testesdeaceitaçãotestamocomportamentodosistemasimulandouma
requisiçãoreal,peloqualtestamosasrotas.Estetipodetesteaquiestáautomatizado,
masporeleserumtípico testedecaixa-preta,tambémépossívelrealizá-lomanu-
almente,comoumusuárioacessandoosistema. Asrotasde contatos.js,que
passamum idcomoparâmetro,precisamdeum idválidoqueretorneumobjeto
dobancodedados,ecomotestamossomenteoretornodasrequisições,nãoháa
possibilidadedecriarobjetos fakes,impossibilitandoaelaboraçãodestestestes.
8.6 D eixando seus testes mais limpos
Algoquepoluimuitooscódigosdetestesãoasvariáveisprincipais,quesãocarre-
gadasnotopo. Éclaroqueporquestõesdelegibilidadeeentendimentodotesteé
necessáriodeclará-losemcadateste,porémépossívelcriarumarquivodeconfi-
guraçãodopróprioMochaparaquesejamcentralizadosemumúnicoarquivoos
parâmetrosiniciaisdeexecuçãodoMochaeseusmódulosauxiliares.Estearquivo
deveserincluídodentrododiretório test,comonome mocha.opts. Basica-
menteelepermiteutilizarosparâmetrosdeconfiguraç ãodoseupróprioCLI,assim
comotambémpermitecarregaralgunsmódulosauxiliares: should.Eissoseráo
suficienteparadeixarostestesmaislimpos.
Dentrode test,crieoarquivo mocha.opts,seguindoosparâmetrosdocó-
digoabaixo:
--require should
--report spec
Alémdecarregarmoso should,tambémfoiadicionadoumnovoparâmetro,
o --report spec,quedefineolayoutdoresultadodostestes.Casoqueriaincluir
outrosparâmetrosemseu mocha.opts,executenoterminalocomando mocha
-hparavisualizartodasop çõesdeconfiguração.
109

## Página 126

8.6. Deixandoseustestesmaislimpos CasadoCódigo
Figura8.4:ParâmetrosopcionaisdoMocha.
Agora, só para finalizar, remova a fun ção var should =
require('should') de todos os testes, pois eles serão automaticamente
carregadosvia mocha.opts.
110

## Página 127

Capítulo9
AplicaçãoNodeemprodução
9.1 O que v amos fazer?
Enfim,chegamosnoúltimocapítulodesselivro!Naspróximasse çõesserãoaborda-
dostemasimportantesparaprepararonossoprojetoparaoambientedeproduç ão.
Oobjetivoaquiéapresentaralgunsconceitoseferramentasparamanterumaaplica-
çãoNodedeformaseguraecomboaperformance.OtimizaremosoprojetoNtalk,
preparando-oparaentraremambientedeprodu ção,alémdegarantirtodamonito-
riadosistemaatravésde loggings.
9.2 Configurando Clusters
Infelizmente,oNode.jsnãotrabalhacom threads,issoéalgoquenaopiniãodeal-
gunsdesenvolvedoreséconsideradocomoumpontonegativo,peloqualdesperta
umcertodesinteresseemaprenderoulevarasérioestatecnologia.Masapesardo
Nodesersingle-threadépossível,sim,prepará-loparatrabalharcomprocessamento
paralelo.Paraissoexistenativamenteummódulochamadode Cluster.

## Página 128

9.2. ConfigurandoClusters CasadoCódigo
Elebasicamenteinstancianovosprocessosdeumaaplicaç ão,trabalhandode
formadistribuídaecompartilhandoamesmaportadarede.Onúmerodeproces-
sosaseremcriadosquemdeterminaévocê,eéclaroqueaboapráticaéinstanciar
umtotaldeprocessosrelativoàquantidadedenúcleosdoprocessadordoservidor.
Porexemplo,setenhoumprocessadordeoitonúcleos,entãopossoinstanciaroito
processos,criandoassimumarededeoito clusters.
Paragarantirqueos clusterstrabalhemdeformadistribuídaeorganizadaéne-
cessárioqueexistaumprocessopai,maisconhecidocomo clustermaster. Eleéo
processoresponsávelporbalancearacargadeprocessamento,distribuindoentreos
demaisprocessosquesãochamadosde clusterslave. Implementaressatécnicano
Node.jsémuitosimples,vistoquetodadistribuiçãoentreos clusterséexecutadade
formaabstraídaparaodesenvolvedor. Outravantageméqueos clusterssãoinde-
pendentesunsdosoutros,ouseja,casoum clustersaiadoar,osdemaiscontinuarão
servindoaaplicaçãomantendoosistemanoar.Porém,énecessáriogerenciarasins-
tanciaseencerramentodessesprocessosmanualmente.Combasenessesconceitos,
vamosaplicarnapráticaaimplementaçãode clusters.Crienodiretórioraizoarquivo
clusters.js,paraqueatravésdelesejacarregadoclustersdanossaaplicaç ão,veja
ocódigoabaixo:
var cluster = require('cluster')
, cpus = require('os').cpus()
;
if (cluster.isMaster) {
cpus.forEach(function(cpu) {
cluster.fork();
});
cluster.on('listening', function(worker) {
console.log("Cluster %d conectado", worker.process.pid);
});
cluster.on('disconnect', function(worker) {
console.log('Cluster %d esta desconectado. ', worker.process.pid);
});
cluster.on('exit', function(worker) {
console.log('Cluster %d caiu fora. ', worker.process.pid);
});
} else {
require('./app');
}
Dessavez,paralevantaroservidorseráviacomando node clusters.jspara
112

## Página 129

CasadoCódigo Capítulo9. AplicaçãoNodeemprodução
queaaplicaçãorodedeformadistribuídaeparacomprovarquedeucerto.Vejano
terminalquantasvezesserepetiuamensagem: "Ntalk no ar".
Figura9.1:RodandoNode.jsemclusters.
Basicamente, carregamos o módulocluster e primeiro verificamos se
ele é ocluster mastervia função cluster.isMaster. Caso ele seja, roda-
mos um loop cuja suas iterações é baseada no total decpus que ocorre atra-
vés do trechocpus.forEach(), que retorna o total de núcleos do servidor.
Emcadaiteraçãorodamoso cluster.fork()que, naprática, instanciaum
child process(processofilho)destaaplicação. Quandonasceumnovopro-
cesso(nestecasoumprocesso-filho),consequentementeelenãocainacondicio-
nal: if(cluster.isMaster). Comissoéiniciadooservidordaaplicaç ãovia
require('./app')atravésdeumclusterslave.
Tambémforamincluídosalgunseventosemitidospelo clustermaster,nocódigo
existemapenasosprincipaiseventos:
•listening:acontecequandoum clusterestáescutandoumaportadoservi-
dor.Nestecaso,anossaaplicaçãoestáescutandoaporta4000.
•disconnect:executaseucallbackquandoum clustersedesconectadarede.
•exit:ocorrequandoumprocesso-filhoéfechadonosistemaoperacional.
113

## Página 130

9.3. Rediscontrolandoassessõesdaaplicação CasadoCódigo
Desenvolvimento em Clusters
Muitopodeserexploradonodesenvolvimentode clustersnoNode.js.
Aquiapenasaplicamosoessencialparamanternossaaplicaç ãorodando
emparalelo,mascasotenhaanecessidadedeimplementarmaisdetalhes
queexploremaomáximoos clusters,recomendoqueleiaadocumen-
tação—(http://nodejs.org/api/cluster.html)—paraficarpordentrode
todososeventosefun çõesdestemódulo.
Parafinalizaredeixarautomatizadoo startdoservidoremmodo clusterviaco-
mando npm,atualizeemseu package.jsonnoatributo scriptsdeacordocom
ocódigoabaixo:
"scripts": {
"start": "node clusters",
"test": "NODE_ENV=test ./node_modules/mocha/bin/mocha test/*.js"
}
Pronto! Agoravocêpodeexecutarsuaaplicaç ãoatravésdocomando npm
start.
9.3 Redis controlando as sessões da aplicação
QuandodesenvolvemosnoNode.jsumaaplicaç ãoorientadaaclusters,aliadoao
frameworkExpresseSocket.IO,seusmecanismosdefaultdepersistênciadeSessions
paramdefuncionarcorretamente.Nãoacredita?Entãovejavocêmesmo!Execute
oservidorvia npm start,agorafaçaumloginnosistema,atéagoraestatudook,
correto?Tentecadastrarumnovocontatoouverosdetalhesdeumexistente.Repare
queautomaticamentevocêfoiredirecionadoparateladelogin,masqueestranho!
Porqueaconteceuisso?Nomomentoutilizamosumcontroledesessãoemmemória
(conhecidopelonome: MemoryStore). Anaturezadessetipodecontrolenão
conseguecompartilhardadosentreosclusters,poiselefoiprojetadoparatrabalhar
comapenasumprocesso.OExpresseSocket.IOsãoframeworksqueutilizampor
padrãosessãoemmemória. Asoluçãoparaesteproblemaéadotarumnovotipo
destoreparaasessão,sendooRedisumaótimaalternativa.Comojáoutilizamos
dentrodochatdaaplicaçãoteremosagoraapenasqueadaptá-loparaomecanismo
sessionstoredoExpressedoSocket.IO.
114

## Página 131

CasadoCódigo Capítulo9. AplicaçãoNodeemprodução
Essa adaptação é simples, e seu resultado visa manter a aplicação rodando
perfeitamente em clusters. Implantaremos esse upgrade no mecanismo de ses-
sãodoExpresseSocket.IO.Primeirocriaremosumanova libfocadoemgeren-
ciarconexõesdoRedis,esteteráfun çõespararetornarumsimplesclienteRedis,
umRedisStore paraoExpresseum RedisStore paraoSocket.IO.Crieoarquivo
lib/redis_connect.jseimplementeocódigoabaixo:
var redis = require('redis')
, redisStore = require('connect-redis')
, express = require('express')
, socketio = require('socket.io')
;
exports.getClient = function() {
return redis.createClient();
}
exports.getExpressStore = function() {
return redisStore(express);
}
exports.getSocketStore = function() {
return socketio.RedisStore;
}
Agoraparaqueestecódigofuncioneexecutenoterminalocomando: npm
install connect-redis --save.Eparafinalizarfaremoso upgradedasstores,
atravésdorefactoringnocódigo app.js:
var express = require('express')
, app = express()
, load = require('express-load')
, server = require('http').createServer(app)
, error = require('./middleware/error')
, io = require('socket.io').listen(server)
, redis = require('./lib/redis_connect')
, ExpressStore = redis.getExpressStore()
, SocketStore = redis.getSocketStore()
;
const SECRET = 'Ntalk', KEY = 'ntalk.sid';
var cookie = express.cookieParser(SECRET)
, storeOpts = {client: redis.getClient(), prefix: KEY}
, store = new ExpressStore(storeOpts)
115

## Página 132

9.4. Monitorandoaplicaçãoatravésdelogs CasadoCódigo
, sessOpts = {secret: SECRET, key: KEY, store: store}
, session = express.session(sessOpts);
// stack de configurações do Express...
io.set('store', new SocketStore);
// io.set('authorization ')...
// load()...
// server.listen()...
Tambémmodificaremoso sockets/chat.jsparaqueelerecebaumacone-
xãoRedisdiretamentedessa lib:
module.exports = function(io) {
var crypto = require('crypto')
, redis_connect = require('../lib/redis_connect')
, redis = redis_connect.getClient()
, sockets = io.sockets;
// continuação dos eventos do socket.io...
}
Comesseupgradeimplementadoagoraosistemavairodarperfeitamenteem
clusters,semcausarbugsnocontroledesessãoetodasassessõesserãocompartilha-
dasentreosclustersexistentes.
9.4 Monitorando aplicação através de logs
Quandocolocamosumsistemaemproduç ão,aumentamososriscosdeacontece-
rembugsquenãoforamidentificadosduranteostestesnodesenvolvimento. Isso
énormal,etodaaplica çãojápassououvaipassarporestasituaç ão.Oimportante
nestecasoéterummeiodemonitorartodocomportamentodaaplicaç ão,atravésde
arquivosdelogs.TantooExpressquantooSocket.IOpossuemum middlewarepara
monitoraregerar logs.Suainstalaçãoésimples,abrao app.jseadicionenotopo
dastackdeconfiguraçõesdoExpressafun ção app.use(express.logger()):
app.use(express.logger());
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
app.use(cookie);
116

## Página 133

CasadoCódigo Capítulo9. AplicaçãoNodeemprodução
app.use(session);
app.use(express.json());
app.use(express.urlencoded());
app.use(express.methodOverride());
app.use(app.router);
app.use(express.static(__dirname + '/public'));
app.use(error.notFound);
app.use(error.serverError);
Para configurar os logs no Socket.IO é simples também! Adicione
no app.js a função io.set('log level', 1) antes da função
io.set('authorization').
io.set('log level ', 1);
Agoraoseusistemaestágerandologscommaiordetalhedetodocomporta-
mentodaaplicação.Oúnicoproblemaaquiéqueesteslogsserãoimpressosnatela
deconsole.Emumsistemaemproduç ão,seriamuitotediosoficarcomconsoledo
sistemaabertoparaveroslogs,afinalvocêtambémtemumavidanomundoreal
paraviver! Sedonadaacontecerumproblemanosistemaevocênãoestiverpre-
senteparaveroerrogeradonoconsole,vocêperderáinformaçõesúteisdedebug
daaplicação.Pararesolveresteproblema,énecessárioumsimplescomandonoter-
minal.Aoexecutarocomando node clusters >> app.logoterminalparade
imprimirlogsnatelaepassaescreveroslogsdentrodoarquivo app.log.Epara
simplificaraindamais,vamosmanterestecomandodentrodo alias npm start.
Abrao package.jsonealtereaseguintelinha:
"scripts": {
"start": "node clusters >> app.log",
"test": "NODE_ENV=test ./node_modules/mocha/bin/mocha test/*.js"
}
Agorasuaaplicaçãoestapreparadaparagerarlogsemarquivodetexto. Para
testarasalteraçõesexecuteocomando npm start.Reparequedestavezoterminal
vaificarcongeladosemexibirnenhumamensagemnatela,vejaaimagemabaixo:
117

## Página 134

9.5. OtimizaçõesnoExpress CasadoCódigo
Figura9.2:Teladoterminalnãoemitindologs.
Em contrapartida, todas as mensagens serão persistidas dentro do arquivo
app.log.
Figura9.3:Logsdaaplicaçãonoarquivoapp.log.
9.5 Otimizações no Express
Nestaseçãopretendopassaralgumasdicasquevisamaumentaraperformancedo
sistema.SerãoadicionadasalgumasconfiguraçõestantoparaoExpresscomoparao
118

## Página 135

CasadoCódigo Capítulo9. AplicaçãoNodeemprodução
Socket.IOeMongoose,comoobjetivodeotimizartantoserver-sidecomooclient-
sidedaaplicação.
Todaotimizaçãoseráfeitadentrodo app.js,afinalelefazo bootdanossa
aplicação,peloqualelecarregaeexecutatodosseussubmódulos. Vamoscome çar
otimizandooExpress.Faremosnele2otimizações:habilitarcompactaçãogzipatra-
vésdonovostack express.compress()eadicionaremoscacheparaosarquivos
estáticosincluindodentrode express.staticoatributo maxAge.Vejaabaixo
comoseráessasalteraçõesno app.js:
const SECRET = 'Ntalk', KEY = 'ntalk.sid'
, MAX_AGE = {maxAge: 3600000}
, GZIP_LVL = {level: 9, memLevel: 9};
// configurações de session e cookies...
app.use(express.logger('dev'));
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
app.use(cookie);
app.use(session);
app.use(express.json());
app.use(express.urlencoded());
app.use(express.methodOverride());
app.use(express.compress(GZIP_LVL));
app.use(app.router);
app.use(express.static(__dirname + '/public', MAX_AGE));
app.use(error.notFound);
app.use(error.serverError);
9.6 O timizando requisições do Socket.IO
JánoSocket.IO,habilitaremos minification + cache + gzip + etagpara
otimizarasrequisiçõesemudaremosseuníveldelogsparainformarapenasquando
ocorrererrosnaaplicação:
io.enable('browser client cache ');
io.enable('browser client minification ');
io.enable('browser client etag ');
io.enable('browser client gzip ');
io.set('log level ', 1);
119

## Página 136

9.6. OtimizandorequisiçõesdoSocket.IO CasadoCódigo
io.set('store', new SocketStore);
/// io.set('authorization ') ...
Paradeixarmais cleannosso app.js,podemosdeixarexternoessasconfigura-
ções,chamando-asviacomando requirequealémdecarregarmódulos,também
carregaarquivos .json.Paraissocrienaraizdoprojetooarquivo config.json
comositensabaixo:
{
"SECRET": "Ntalk",
"KEY": "ntalk.sid",
"MAX_AGE": {
"maxAge": 3600000
},
"GZIP_LVL": {
"level": 9,
"memLevel": 9
}
}
Agoravoltandoem app.jscarregaremoso config.jsonviacomando var
cfg = require('./config.json'):
var express = require('express')
, app = express()
, load = require('express-load')
, server = require('http').createServer(app)
, error = require('./middleware/error')
, cfg = require('./config.json')
, io = require('socket.io').listen(server)
, redis = require('./lib/redis_connect')
, ExpressStore = redis.getExpressStore()
, SocketStore = redis.getSocketStore()
;
Atualizaremosasconstantesatuaisparaseremchamadaspelavariável cfg,pri-
meiromodificaremosasconfiguraçõesdecookieesessions:
var cookie = express.cookieParser(cfg.SECRET)
, storeOpts = {client: redis.getClient(),
prefix: cfg.KEY}
, store = new ExpressStore(storeOpts)
120

## Página 137

CasadoCódigo Capítulo9. AplicaçãoNodeemprodução
, sessOpts = {secret: cfg.SECRET,
key: cfg.KEY,
store: store}
, session = express.session(sessOpts)
;
Eparafinalizaratualizaremosasconfiguraçõesde middlewaresdoExpresseSoc-
ket.IO:
app.use(express.logger('dev'));
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
app.use(cookie);
app.use(session);
app.use(express.json());
app.use(express.urlencoded());
app.use(express.methodOverride());
app.use(express.compress(cfg.GZIP_LVL));
app.use(app.router);
app.use(express.static(__dirname + '/public', cfg.MAX_AGE));
app.use(error.notFound);
app.use(error.serverError);
io.enable('browser client cache ');
io.enable('browser client minification ');
io.enable('browser client etag ');
io.enable('browser client gzip ');
io.set('log level ', 1);
io.set('store', new SocketStore);
io.set('authorization', function(data, accept) {
cookie(data, {}, function(err) {
var sessionID = data.signedCookies[cfg.KEY];
store.get(sessionID, function(err, session) {
if (err || !session) {
accept(null, false);
} else {
data.session = session;
accept(null, true);
}
});
});
});
121

## Página 138

9.7. AplicandoSingletonnasconexõesdoMongoose CasadoCódigo
9.7 AplicandoSingleton nas conexões do Mongoose
NoMongoose,apenasaplicaremoso designpatternSingleton parainstanciarasco-
nexõesdobancodedados.Issoseráimplementadocomoobjetivodegarantirque
apenasumaúnicaconexãosejainstanciadaecompartilhadaportodaaplica ção.No
arquivo lib/db_connect.js,codifiqueaplicandoasseguintesmudan ças:
var mongoose = require('mongoose')
, single_connection
, env_url = {
"test": "mongodb://localhost/ntalk_test",
"development": "mongodb://localhost/ntalk"
}
;
module.exports = function() {
var env = process.env.NODE_ENV || "development"
, url = env_url[env];
if(!single_connection) {
single_connection = mongoose.connect(url);
}
return single_connection;
};
9.8 M antendo o sistema no ar com Forever
ONode.jsépraticamenteumaplataformadebaixonível,comeletemosbibliotecas
comacessodiretoaosrecursosdosistemaoperacional,eprogramamosentrediver-
sosprotocolos,comoporexemplo,oprotocolohttp.Paratrabalharcomhttp,temos
queprogramarcomoseráoservidorhttpetambémsuaaplicaç ão.Quandocoloca-
mosumaaplicaçãoNodeemproduçãodiversosproblemasebugssãoencontrados
comopassardotempo,equandosurgeumbuggraveoservidorcai,deixandoa
aplicaçãoforadoar.Defato,programaremNode.jsrequerlidarcomessesdetalhes
deservidor.
OForeveréumaferramentaquesurgiupararesolveresseproblemadequedado
servidor.Seuobjetivoémonitorarumservidorrealizando pingsacadacurtoperíodo
predeterminadopelodesenvolvedor.Quandoeledetectaqueaaplicaç ãoestáforado
ar,automaticamenteeledáumrestartnela.Eleconseguefazerissoporquemantém
aaplicaçãorodandoem backgroundnosistemaoperacional.
Existemduasversõesdesteframework,umaéaversãoCLIemquetodatarefaé
122

## Página 139

CasadoCódigo Capítulo9. AplicaçãoNodeemprodução
realizadanoterminal.Aoutramaneiradesetrabalharcomo foreverédeforma
programávelemcódigoNode,utilizandoomódulo forever-monitor.Esteúl-
timo,éomaisrecomendadoaseutilizarquandosuaaplicaç ãoestahospedadaem
umambientecujoterminalpossuirestriçõesdeseguran çaquenãopermiteinsta-
larprogramasdotipoCLI.Eomecanismodo forever-monitoréomesmoque
o forever.Suaúnicadiferen çaéquesuaconfiguraçãoéfeitaviaJavascript,eele
instanciaumaplicaçãoNodevia child process.
Sua instalação é simples, basta executar o comando: npm install
forever-monitor --save, para instalá-lo e auto atualizar o seu
package.json.
Agoravamoscriarumnovocódigochamadode server.jsdentrododiretório
raizdoprojeto.Algointeressantedo forever-monitoréque,alémdeelereiniciar
oservidor,elegeraarquivosdelogsdaaplicaç ãoseparadosporlogsdoforever(
logFile),logsdaaplicação( outFile)elogsdeerrosdaaplicaç ão( errFile).
Vejaabaixomaisdetalhesdecomoseráestecódigo-fonte:
var forever = require('forever-monitor');
var Monitor = forever.Monitor;
var child = new Monitor('clusters.js', {
max: 10,
silent: true,
killTree: true,
logFile: 'forever.log',
outFile: 'app.log',
errFile: 'error.log'
});
child.on('exit', function () {
console.log('O servidor foi finalizado.');
});
child.start();
Tudocomeçaquandoinstanciamosoobjeto Monitor.Nelepassamosdoispa-
râmetrosemseuconstrutor,oprimeiroéocódigodaaplicaçãoquedesejamosexecu-
tar(nonossocasoéo cluster.js)enosegundoparâmetropassamosumobjeto
comosatributosdeconfiguraçãodo forever-monitor. Emmaxdefinimoso
totaldevezesquepoderáreiniciaroservidorquandoelecair,lembrandoque,ao
123

## Página 140

9.9. IntegrandoNginxnoNode.js CasadoCódigo
passardestetotal,suaaplicaçãoserátotalmentefinalizada.Infelizmenteestaéuma
limitaçãodo forever-monitor,poiso foreverporserumCLI,permiterei-
niciarinfinitamentesuaaplicação.Oatributo silentapenasocultaaexibiçãode
logsnoterminal.Aohabilitaroatributo: killTree,todososprocessos-filhosda
suaaplicaçãoserãofinalizadosacadarestartdoservidor.
Agoraquetemoso forever-monitorconfiguradoegerandologsporconta
própria,vamosatualizarocomando npm startparaqueeleexecutediretamente
o server.jsaoinvésdoatual clusters.js.Combasenocódigoabaixo,edite
oseu package.json:
"scripts": {
"start": "node server",
"test": "NODE_ENV=test ./node_modules/mocha/bin/mocha test/*.js"
}
Estafoiumaconfiguraçãobásicaparautilizaro forever-monitor. Caso
suanecessidadesejairalémdoquefoiapresentadoaqui, visiteogithuboficial
dosprojetos(https://github.com/nodejitsu/forever)e(https://github.com/nodejitsu/
forever-monitor).Cadaumpossuisuasvantagensedesvantagens,bastasaberqual
alternativaterámelhorresultadodeacordocomoambientequeseráhospedadosua
aplicaçãoNode.js.Lembrandoqueemambienteslimitadosquenãopermitemins-
talarCLIsamelhoralternativaéusaro forever-monitor.
Agora,nossaaplicaçãoestáotimizadaparaoambientedeprodução.Napróxima
seçãofaremosumaintegraçãointeressantecomoservidorNginx,queéconsiderado
comoumótimoservidordearquivosestáticos.
9.9 I ntegrando Nginx no Node.js
Enfim,estamosnaúltimase ção.Durantetodoopercursoimplementamosumaapli-
caçãoNode.jsqueutilizaowebframeworkExpress,persistedadostantoparaoMon-
goDB,comoparaoRediserealizacomunicaç ãobidirecionalatravésdoSocket.IO.
Tambémconfiguramosclusters,logsecodificamostestesdeaceitaç ãoutilizandoo
Mocha+Supertest.EmespecialtivemosdoiscapítulosdedicadosaoExpress,afinal
eleéabaseprincipaldanossaaplicaç ão,comeledesenvolvemosrotaseincluímos
diversasstacksquevisamotimizarofluxodoservidorhttp.Nestase çãoiremosin-
tegraroNode.jscomoservidorNginx.
124

## Página 141

CasadoCódigo Capítulo9. AplicaçãoNodeemprodução
Figura9.4:ServidorNginx.
Oobjetivodessaintegraçãovisaaumentarperformancedaaplicaç ãopeloqual
criaremosum proxydoNginxcomNode.jsetambémdelegaremostodoprocessa-
mentodearquivosestáticoparaoNginx,deixandoapenasqueoNode.jscuidedo
processamentodesuasrotas.Issodiminuionúmeroderequisiçõesdiretasemnossa
aplicação.
Atenção:NãoentraremosemdetalhessobrecomoinstalaroNginxemsuamá-
quina.Parainstalá-lorecomendoqueacesseseusiteoficial:(http://nginx.org).Tam-
bémrecomendoqueleiasua Wikiquecontémdiversasdicasdecomoconfigurá-lo:
(http://wiki.nginx.org/Main).Aversãoutilizadanestelivroéaversão 1.5.2,re-
comendoquenãoutilizeversõesanterioresaesta,poiséprovávelquenãofuncione
adicadeconfiguraçãoqueexplicareiabaixo.Outrodetalheimportanteéquefoia
partirdaversão 1.3.13queoNginxpassouadarsuporteaoprotocoloWebSocket,e
nissooseuservidorestaráhabilitadoparaprocessaroWebSocketdoSocket.IOem
browserscompatíveis.
AgoraquetemosoNginxinstaladoefuncionandocorretamenteemsuamá-
quina, vamos configurá-lo para que ele comece a servir arquivos estáticos de
nossa aplicação, tudo isso será feito dentro de seu arquivo principal chamado
nginx.conf.Alocalizaçãodestearquivovariadeacordocomosistemaoperacio-
nal,entãorecomendoqueleiasuadocumentaç ãooficial:(http://nginx.org/en/docs)
paradescobrirondeeleseencontra.
125

## Página 142

9.9. IntegrandoNginxnoNode.js CasadoCódigo
AbaixoapresentoumaversãosimplificadadeconfiguraçãodoNginx.Estaconfi-
guraçãofaráoNginxservirosarquivosestáticosaoinvésdoExpress,eparafinalizar
aplicamosum proxydoNginxparaasrotasdanossaaplicaç ão.
worker_processes 1;
events {
worker_connections 1024;
}
http {
include mime.types;
default_type application/octet-stream;
sendfile on;
keepalive_timeout 65;
gzip on;
server {
listen 80;
server_name localhost;
access_log logs/access.log;
location ~ ^/(javascripts|stylesheets|images) {
root /var/www/ntalk/public;
expires max;
}
location / {
proxy_pass http://localhost:3000;
}
}
}
Praticamenteadicionamosalgumasmelhoriasemcimadasconfiguraçõespa-
drõesdo nginx.conf.Comoobjetivodeotimizaroservidorestático,habilitamos
compactaçãogzipnativa,atravésdotrecho: gzip on;ecriamosdois locations
dentrode server. Oprimeiro locationéoresponsávelporservirconteúdo
estático.
location ~ ^/(javascripts|stylesheets|images) {
root /var/www/ntalk/public;
126

## Página 143

CasadoCódigo Capítulo9. AplicaçãoNodeemprodução
expires max;
}
Édentrodeledefinimosalocalizaçãodapasta publicdanossaaplicaçãoatra-
vésdotrecho: root /var/www/ntalk/public;. Estalocalizaçãodefinidano
item rootsebaseianoendere çoondeficaapasta publicdoprojetoemseu
sistemaoperacional,sejaeleUnix,MacOSouLinux. SeoseusistemaéWindows
altereoendere çoparaopadrãodediretóriosdele,queéalgosemelhantea root
C:/www/ntalk/publicouparaqualqueroutroendere çoquevocêdesejamanter
esteprojeto. Tambémaplicamosdentrodesse locationumcachedosarquivos
atravésdoitem: expires max;.
No últimolocation, aplicamos um simples controle deproxy. O item
proxy_passpraticamenteredirecionaasdemaisrotasparanossaaplicaç ão,que
estaráativaatravésdoendereço:http://localhost:3000.
location / {
proxy_pass http://localhost:3000;
}
ComoNginxjáconfiguradoerodando,quetaltestaressaintegraç ão?Reinicie
oNginxatravésdocomando: nginx -s reloadetambémnossaaplicaçãovia
comando npm start.Seatéagoranenhumproblemaaconteceu,bastaacessarsua
aplicaçãoatravésdonovoendere ço:http://localhost.
127

## Página 145

Capítulo10
Continuandoosestudos
Finalmentechegamosaofimdestelivro,ecomoestatecnologiaestaconstantemente
emevolução,comcertezaésemprebomsemanteratualizadocomseusnovosre-
cursos,lereacompanharnovasreferênciassobreestaplataforma.Comissolistarei
algumasexcelentesreferênciasparavocêcontinuarestudandomaisemaisNode.js!
Sites,blogs,fórunseslides
• SiteoficialNode.js-http://nodejs.org
• GithubdoNode.js-http://github.com/joyent/node
• DocumentaçãodoNode.js- http://nodejs.org/api
• BlogdoNode.js-http://blog.nodejs.org
• NPMRegistry-http://npmjs.org
• BlogdacomunidadeNodeBR-http://nodebr.com

## Página 146

CasadoCódigo
• FórumdoNodeBR-http://groups.google.com/forum/#!forum/nodebr
• UndergroundWebDev(autordestelivro)-http://udgwebdev.com
• HowtoNode-http://howtonode.org
• Scoop.itdoNode.js-http://scoop.it/t/nodejs-code
• TJHolowaychuk(autordoExpress,EJSeMocha)-http://tjholowaychuk.com
• NodeCloud-http://nodecloud.org
• DailyJS-http://dailyjs.com
• NetTuts+-http://net.tutsplus.com
• Blogmetaduck-http://metaduck.com
• BlogWaib-http://www.waib.com.br/Blog
• BlogCaelum-http://blog.caelum.com.br
• BlogCabaré-http://caba.re
• NodeSchool-http://nodeschool.io
• GUJ(discutasobreJavascripteNode.js)-http://guj.com.br
Eventos,screencasts,podcastsecursos
• Node Knockout (Hackaton Node.js inspirado em Rails Rumble) -http://
nodeknockout.com
• DevCast-Node.jseMongoDB,Ocasamentoperfeito- http://youtube.com/
watch?v=-OpUd1Rov2c
• DevCast - Javascript dos novos tempos -http://youtube.com/watch?v=
LlUTi5DM4ws
• GrokPodcast Node.js Parte 1 -http://grokpodcast.com/2011/02/17/
episodio-19-node-js-parte-1
• GrokPodcast Node.js Parte 2 -http://grokpodcast.com/2011/02/24/
episodio-20-node-js-parte-2
130

## Página 147

CasadoCódigo Capítulo10. Continuandoosestudos
• GrokPodcast Node.js Parte 3 -http://grokpodcast.com/2011/03/03/
episodio-21-node-js-parte-3
• Nodecasts(InspiradonoRailscast)-http://nodecasts.net
• SailsCasts (Screencasts do Framework Sails.js) -http://irlnathan.github.io/
sailscasts/blog/archives
• Nodetutsscreencasts-http://nodetuts.com
• Nodeuppodcasts-http://nodeup.com
• Codeschool: Real time with Node.js -http://codeschool.com/courses/
real-time-web-with-nodejs
• Tuts+Courses:BuildingwebappswithNode.jsandExpress- http://tutsplus.
com/course/building-web-apps-in-node-and-express
• PeepcodeNode.jsscreencasts-http://peepcode.com/products/nodejs-i
• Alura:DesenvolvaaplicaçõesemtemporealcomSocket.IOeNode.JS-http:
//www.alura.com.br/cursos-online-ferramenta/nodejs-socketio
Enfim,esperoquesejadegrandeutilidadeessasreferências,tenhabonsestudos
eobrigadoporlerestelivro.
131