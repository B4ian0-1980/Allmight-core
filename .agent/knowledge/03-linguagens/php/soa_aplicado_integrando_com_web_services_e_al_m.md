---json
{
  "id": "soa_aplicado_integrando_com_web_services_e_al_m",
  "title": "SOA aplicado Integrando com web services e além",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Arquivo Original:** `SOA aplicado Integrando com web services e além.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "aplicado",
    "com",
    "integrando",
    "linguagens",
    "php",
    "services",
    "soa",
    "web"
  ],
  "perguntas_tipo": [
    "Como utilizar SOA aplicado Integrando com web services e além?",
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

# SOA aplicado Integrando com web services e além

> **Arquivo Original:** `SOA aplicado Integrando com web services e além.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 2

© Casa do Código
Todos os direitos reservados e protegidos pela Lei nº9.610, de 10/02/1998.
Nenhuma parte deste livro poderá ser reproduzida, nem transmitida, sem auto-
rização prévia por escrito da editora, sejam quais forem os meios: fotográficos,
eletrônicos mecânicos, gravação ou quaisquer outros.
Casa do Código
Livros para o programador
Rua Vergueiro, 3185 - 8º andar
04101-300 – Vila Mariana – São Paulo – SP – Brasil

## Página 5

CasadoCódigo
“ A g r a d eço à m i n h af amí l i a ,m i n h anamorada e a todos os q u eacreditaram em m i m
— mesmo quando eu mesmo não acreditei. ”
–AlexandreSaudate
i

## Página 7

CasadoCódigo
Prefácio
SOA passa por i n t e g r ação, mas i n t e g r ação não éSOA
PorquemeapaixoneipeloestilodedesenvolvimentobaseadoemSOA?
Hámuitosanos,quandodesenvolviapuramenteparaumaplataformaespecífica,
fazermeusoftwareseintegraraoutroerapraticamenteum Jihad.
Essanecessidadecomeçouaficarmaisfortequandoprecisavaexporfunciona-
lidadesaclientesouparceirosdenegóciodacompanhiaparaqualprestavaserviço,
poisnãopoderiaobrigarosseusdesenvolvedoresautilizarnossaplatormaelingua-
gem.
Imaginemuma startupcomoPayPalcriandoseulequedeAPIsparaparceiros
denegóciopoderemreutilizarsuasfunções básicasde gatewaydepagamento,de-
tecçãodepadrões defraudeetc.Fazsentidoqueasmesmassósejamdisponíveisa
desenvolvedoresDelphi?Provavelmenteessa startupteriafalido.
Diversastécnicasdeintegraçãocomeçaramentãoaseremdesenvolvidas,desde
trocadearquivoscomum layoutespecífico,basedoEDI, Eletronic Da taInterchange,
a“tabelinhasintermediárias”,utilizadaserroneamentepordiversasequipes.Masvol-
tandoaoexemploanterior,comofariaumachamada onlineaumaAPI?Nocaso
deum e-commerce,atualmenteprecisofazeropagamentonomesmoinstante,os
compradoresnãoqueremmaisesperardiasparasaberemsesuacomprafoiounão
processada.
Cadadiamais,todososprocessoscomeçaramasetornar onlineeacreditoque
esseimpulsoveiodaconcorrênciademercadoentreasempresas,ofertandocadavez
maiscomodidadeaosseusclientes.
Comprarumcelularnumalojadeumaoperadoraeesperar3diasparaserlibe-
radaautilizaçãoéumaexperiênciapoucofeliz.Seaconcorrênciacomeçaraante-
ciparpara1horaouimediatamente,quemestiverforadessecontextoperderáuma
massaconsideráveldenovosclientes.
iii

## Página 8

CasadoCódigo
Então,fazerseu softwareresponder onlineamuitasplataformaseraumatarefa
árduamasnecessária!
Tecnicamenteprecisávamoslidarcomquestões comointerfacecomumdeco-
municaçãoatodasaslinguagenseplataformas,protocolopara marshalle unmarshall
dosobjetosserializados,transaçãoentreplaformas,segurançaetc.Eramtantosde-
talhesparapensar—entãomedepareicomumaespecificaçãoregidaporumcomitê
quevinhaevoluindodesde1991,eclareoudiversasquestões: Common Object Request
B r o k e r—CORBA.
ExporumaAPIonlineemCORBA,seriaasoluçãoparaquediversosoutrospro-
gramadorespudessemusarminhafunçãobásicade gatewaydepagamento,naquele
exatoinstante,levandosatisfaçãoaoclientefinal.Assimelejáteriaasoluçãodeseu
pedidoprocessado,jácomrespostasobreseucréditodeformaimediata.
Então vemapergunta,oqueéSOAafinal? SOA,comochamamosaquina
SOA|EXPERT,éumacrônimo para S m a r tOriented APIs,quenadamaiséque
produzirseu softwarecomAPIsricas, "inteligentes”epoderosamente reutilizáveis,
sendoquequalquerplataformaelinguagempossafazerusodasuafuncionalidade.
Issoélindo!
Comotudoemtecnologia,sobretudoemdesenvolvimentode software,astéc-
nicastendemaficarmaisfáceisdeseimplementarem.Aolongodosanos,vamos
tendoentendimentosobrecomosefazermelhoremaisfácil,cortandoumasériede
burocraciaseabstraindododesenvolvedorcomplexidadesdemasiadas.
PorissoSOAnãotemavercomumatecnologiaespecífica.SOAéoconceitode
modelarsuaAPIinteligente,ricaepoderosaparareutilização.
Atecnologiaqueutilizamosatualmentevemevoluindorapidamente.Começa-
moscomCORBAlátrás,ehojeutilizamos WebServices,oestiloarquiteturalRest,
algunsoutrosmodeloscomoAtomPub, WebSocketsentreváriascombinações pos-
síveisnumaarquitetura.(CQRS,ODataetc.)
Começamosadefinir patternsparaosproblemasmaiscomunseessesvãoevo-
luindoàmedidaquenossoentendimentoficamaisclaro,fazendocomqueessepro-
cessodedesenvolvimentodeAPIsinteligentessejamaissimpleseintuitivoparao
desenvolvedor.
Atualmente,omundoestátotalmenteinterligado,diversosaplicativosnasredes
sociaisestãoentrelaçados,fazendousodassuasfunçõesbásicasdecomunicação,por
exemplo: Twitter.Aliás,hojeseusequipamentos twittam,seuNikeplusexibeseus
dadosdecorridanasredessociais.
StartupsutilizammapasgeográficosdefornecedorescomoGoogleMapsenão
iv

## Página 9

CasadoCódigo
importamsualinguagemdeprogramaçãoouplataforma.Todospodemsevalerdo
esforçodaequipedoGoogleecriarumFourSquareàpartirdessapoderosaAPIde
mapas.
GostodepensarqueSOAéasocialização dasuaAPI:torná-lasocial,demo-
cráticaecominfinitaspossibilidadesdeutilização,dandoliberdadeàcriativadedos
desenvolvedores.
Contudo,oqueaconteceriaseoGoogleMapssaíssedoar?Quantas startupse
atémesmoaplicativosinternosdoGoogleseriamimpactados?
DesenvolveressetipodeAPIexigebastanteresponsabilidadedodesenvolvedor,
tantonaqualidadedamesma,quantonamanutençãodoseuestado.
Astecnologiasassociadasaessemodelodedesenvolvimento,comoESB,BPEL,
SCA,CEP,BRMS,BPM,BAM,Governança,entreoutras,são resultadodoestudo
dasmaisamplasnecessidadeseservemparagerenciarasproblemáticaseociclode
vidadeuma S m a r tAPI.
Esselivrocomeçarácomosaspectosmaisimportantes,definiçãoemodelagem
dasuaAPIutilizandodoismodelosdedesenvolvimento: W e bServicesClássicoe
Restful,passandoporintegraçãocomoframework Enterprise Service B u s.
Háaindaumconjuntograndedetecnologiasqueserão abordadasemfuturos
volumes,poisapesardefazerempartedoecossistema,sãobemespecíficaseamplas
paraseremabordadasemumúnicolivro.
Casoestejamumpoucocuriosossobreassiglascitadas,fareiumarápidaexpla-
naçãoparacontextualizá-losecolocá-losnum roadmapdeestudos:
-Comopegoumafunçãodeumsistemalegado, mainframeouERPeadeixo
simplesparaoutrosdesenvolvedoresacessarem?Infelizmentenãopodemosreescre-
vertodosos softwaresexistentesdeumacompanhia,entãovamosnecessitardeum
framework de integração,queapliqueasmelhorespráticas:Enterprise Integration
Patterns.O ESBéo fr a mewo r kdentrodesseuniverso,queiráfazeraimplementação
desses patternsetornarsimplesparaodesenvolvedorautilizaçãodefunçõeslegadas.
-Comocontroloumcontextotransacionaledou r o l l b a c kentretecnologiasdis-
tintas?SeestivéssemossomenteemJava,poderíamosacionaroJTA.Contudo,como
propagoo r o l l b a c kpara.NETououtrasplataformas? ADSL BPELresolveessae
muitasoutrasquestões.
-Comoconstruonovasregrasdenegócio,fazendojunção(M a s h u p s)entreAPIs
defornecedoresexternos?Essaéumadasinfinitaspossibilidadescomummotorde
regras: BRMS.
v

## Página 10

CasadoCódigo
-Comocontroloumprocessode workflowentreAPIsmescladasàintervenção
humana?OBPMtornarásimplesessatarefaevocênãoprecisaráperdernoitespen-
sandoemmáquinadeestados,compensaçãoetc.
OutrastecnologiasouconceitosassociadosaouniversoSOAnascemdasamplas
possibilidadesdetermosnossoecossistemaaberto,comoo B A M(Business A c t i v i t y
Monitoring),comoqualficafácilmonitorarmosonegóciodoclienteemtemporeal,
jáquetemosAPIsexpostasepodemoscolocarsensoresnasmesmasparacoletar
dados.
HátantaspossibilidadesdentrodeSOA,atémesmocomoconstruirumaaplica-
çãodistribuídaparamelhoriadeescalabilidadee performance,jáquenapráticavocê
estámontandoumsistemadistribuído,efazermelhorusode cloud computing,pois
esseestiloestáintimamenteligadoaomesmo.Serialidarcomsistemasem r e a ltime
com s t re amdeeventosetc.
Contudo,éimportantelembrarqueapesardetodasastecnologiascitadasao
redor,SOAénaessênciaamodelagemdeAPIseissoprecisaestarclaroavocês.
U m aalusãoquesemprepassoemsaladeaula:“SOAéumaAPIquebrilhano
escuro”.Abrincadeiradidáticaserveparaenaltecerqueémaisqueumasimples
integração. Integração porsisóélevarinformação deumpontoaooutro. Criar
uma API q u ebrilhaémodelarpensandoemdiversasreutilizações, eplataformase
devicescomoTVdigital, mobileetc.
OlivrodomeuamigoAlexandreSaudateéumótimopontodeinício,principal-
menteaosdesenvolvedoresJava,poistiroutodaaburocraciadoslivrostradicionais
e,demaneirapragmática,mostracomoseimplementarseusistemaorientadoaAPIs
semrodeios.
Esperodeverdadequevocêtambémseapaixoneporesseestilodedesenvolvi-
mentode software,poisnão fazsentidomaisdesenvolvermospresosaumaúnica
plataformacomosefosse softwaredecaixinha,semcomunicaçãocomomundolá
fora.
Aosnovosdesenvolvedores,tambémgostariadeconvidá-losaparticiparda
nossacomunidadeSOACLOUD-http://www.soacloud.com.br/,ondepaulatina-
mentevocêpoderátestarseusconhecimentos,expordúvidasenovospensamentos
adquiridosatravésdesselivro.
Boaleitura,
FelipeOliveira
FundadordaSOA|EXPERT.
vi

## Página 11

CasadoCódigo
Introdução
Comeceiaprogramardeformarelativamentetardia,porvoltadosquinzeanos.
AprendinumcursotécnicoeminformáticaalinguagemV i s u a lBasic6. Quatro
anosdepois,passeiatrabalharcomprogramaçãoprofissionalmente,comamesma
linguagemqueaprendinomeucursotécnico.Desdeentão,noteiqueossistemas
quedesenvolviaerammonolíticos,eoutrossistemassópodiaminteragircomestes
atravésdemecanismosarcaicos,comoescritadearquivosempastasespecíficasou
diretamentepelobancodedados.
Emfevereirode2008,eucomeceiatrabalharemumapequenaconsultoriade
SãoPaulo.Estaconsultoriaestavacomeçandoaencerrarofocodesuasatividades
emJEE,ereadaptandoestefocoparaSOA—ArquiteturaOrientadaaServiços.
V o c êpodeseperguntar:qualadiferença?
Paraleigos,não existemuita. Porém,àmedidaquevocêseenvolvecomeste
tipodearquitetura,percebequemuitasdecisões devemsertomadasporestasimples
mudançadefoco.Aoexporserviçoscomofocodesuasaplicações, muitasdecisões
devemsertomadas:oqueexporcomoserviços?Comoexpor?E,maisimportante,
porquê?
Ofocodestelivroéresponder,principalmente,a comoexpor web services. A
propostaéforneceravocê,leitor,osinsumosparaquepossaprosseguirsuaspróprias
investigações arespeitodeSOAedescobrirarespostaparaoutrasquestões.
Do q u es etrata o livro?
Estelivroestádivididoemnovecapítulos.
Ocapítuloumapresentaamotivaçãoparausode web services.T a m b é mmostra
comorealizaracriaçãodeum web servicesimplesemJava,assimcomooconsumo
domesmo,tantoemJavaquantoemumaferramentademercadochamada SoapUI.
Ocapítulodoismostradetalhesdosmecanismosenvolvidosnacomunicação
realizadanocapítuloum.EledetalhaaestruturadoWSDL,SOAPe XML Schemas.
vii

## Página 12

CasadoCódigo
Ocapítulotrêsmostracomoadaptarosdocumentosapresentadosnocapítulo
doisparasuasnecessidades.ElemostracommaisdetalhesasAPIsJavaqueregem
ofuncionamentodestesmecanismos,ouseja,JAX-WSeJAXB.
Ocapítuloquatromostracomotirarproveitodeservidoresdeaplicaçãoparare-
alizaraimplantaçãodeseus web services.Alémdisso,mostracomoaliaratecnologia
envolvidaem web servicescomconceitosdeJEE,como Enterprise JavaBeans.
Ocapítulocincomostraumaabordagemdiferenciadaparacriaçãoeconsumo
de web services—osserviçosREST.
Nocapítuloseis,vocêiráaprenderainstalareconfigurarmecanismosdese-
gurançanosserviços,tantoclássicos(WS-*)quantoREST.V o c êverá,também,o
primeiromodelodeintegraçãoentreumserviçoWS-*eREST.
Nocapítulosete, vocêveráalgunsdos design patternsmaisimportantesde
SOA:modelocanônico,desenvolvimento contract-firsteserviçosassíncronos(com
WS-Addressing).
Nocapítulooito,vocêverácomoinstalar,configurare utilizaro Oracle
Service Bus,umdosprincipais Enterprise Service B u sdaatualidade.
Nocapítulonove,vocêverácomoinstalar,configurareutilizaro Oracle SOA
Suite,estandohabilitado,então,autilizaro Oracle BPEL.
Recursos do livro
T o d oocódigofontedestelivroestádisponívelnomeugithub:https://github.
com/alesaudate/soa. Casovocêtenhadúvidasadicionais/sugestões/ reclamações
sobreolivro,vocêpodepostá-lasnumgrupodediscussãoespecífico,localizadoem
https://groups.google.com/forum/?fromgroups=#!forum/soa-aplicado.
Boaleitura!
viii

## Página 13

CasadoCódigo Sumário
Sumário
1 C o m eçando um projeto SOA 1
1.1 Coisasinesperadasacontecem!. . . . . . . . . . . . . . . . . . . . . . . 1
1.2 Formatosdearquivos:CSV. . . . . . . . . . . . . . . . . . . . . . . . . 2
1.3 Discussãosobreformatos:linguagensdemarcação . . . . . . . . . . . 3
1.4 Qualcamadadetransporteutilizar?. . . . . . . . . . . . . . . . . . . . 4
1.5 Eagora,comotestarumserviço? . . . . . . . . . . . . . . . . . . . . . 8
1.6 CrieoprimeiroclienteJava. . . . . . . . . . . . . . . . . . . . . . . . . 12
1.7 OK,eoqueumwebservicetemavercomSOA?. . . . . . . . . . . . 14
1.8 Sumário. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
2 Entendendo o fluxo de dados 17
2.1 ComofuncionaaestruturadenamespacesdoXML . . . . . . . . . . 17
2.2 ConheçaofuncionamentodoSOAP . . . . . . . . . . . . . . . . . . . 19
2.3 EntendaoenormeWSDL. . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.4 Adefiniçãodostiposeaseçãotypes . . . . . . . . . . . . . . . . . . . 21
2.5 Anecessidadedaseçãomessages . . . . . . . . . . . . . . . . . . . . . 24
2.6 AseçãoportType . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
2.7 AdiferençaentreosWSDLsabstratoseconcretos . . . . . . . . . . . 26
2.8 Aseçãobinding . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
2.9 Definiçãodosendereçoscomaseçãoservice . . . . . . . . . . . . . . 29
2.10 Finalmente,oqueaconteceu? . . . . . . . . . . . . . . . . . . . . . . . 30
2.11 CustomizeaestruturadoXMLcomoJAXB. . . . . . . . . . . . . . . 31
2.12 Resolvamétodosdenomesiguaiseadiçãodeparâmetros. . . . . . . 35
2.13 Enviearequisiçãopelocliente . . . . . . . . . . . . . . . . . . . . . . . 41
2.14 Sumário. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
ix

## Página 14

Sumário CasadoCódigo
3 Novos desafios e os ajustes finos pa racontroles de exceçõ e s e adaptação
de dados 45
3.1 Customizeosistemadeparâmetros. . . . . . . . . . . . . . . . . . . . 46
3.2 Conheçaosistemadelançamentodeexceções . . . . . . . . . . . . . 49
3.3 Customizeasessãodedetalhes . . . . . . . . . . . . . . . . . . . . . . 51
3.4 Customizeaindamaisolançamentodeexceções . . . . . . . . . . . . 53
3.5 EmbarcandomaisafundonoJAXB. . . . . . . . . . . . . . . . . . . . 55
3.6 Tireproveitodeadaptadores. . . . . . . . . . . . . . . . . . . . . . . . 57
3.7 TrabalhecomJAXBusandoherança . . . . . . . . . . . . . . . . . . . 60
3.8 Trabalhecomenums . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
3.9 Modelesuasclassescomcomportamentosdenegócioemantenha-
asmapeadascomJAXB. . . . . . . . . . . . . . . . . . . . . . . . . . . 66
3.10 Sumário. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
4 Embarcando no Enterprise - Application Servers 7 3
4.1 ComousarumServletContainer-Jetty . . . . . . . . . . . . . . . . . 7 4
4.2 IntroduçãoaEJBs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
4.3 Habilitandopersistênciaetransacionalidade. . . . . . . . . . . . . . . 80
4.4 U mnovosistema. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
4.5 Sumário. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
5 Desenvolva a p l i c açõ e spa raa web com REST 89
5.1 OqueéREST? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
5.2 EntendaoHTTP. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
5.3 URLspararecursos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
5.4 MétodosHTTPeusodeMIMEtypes . . . . . . . . . . . . . . . . . . 98
5.5 UtilizaçãoefetivadeheadersHTTP. . . . . . . . . . . . . . . . . . . .100
5.6 Utilizaçãodecódigosdestatus. . . . . . . . . . . . . . . . . . . . . . . 102
5.7 Utilizaçãodehipermídiacomomotordeestadodaaplicação . . . . .106
5.8 ComodesenvolverserviçosREST . . . . . . . . . . . . . . . . . . . . . 107
5.9 Mapeamentoavançado:tratandoimagens . . . . . . . . . . . . . . . . 114
5.10 IncluindolinksHATEOAS. . . . . . . . . . . . . . . . . . . . . . . . . 119
5.11 Testandotudo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
5.12 Programandoclientes . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
5.13 Sumário. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
x

## Página 15

CasadoCódigo Sumário
6 Segurança em web se rvic e s 137
6.1 Ataques:Man-in-the-middleeeavesdropping. . . . . . . . . . . . . . 138
6.2 ProteçãocontrainterceptaçãocomHTTPS . . . . . . . . . . . . . . .140
6.3 U s a n d omecanismosdeautenticaçãoHTTP . . . . . . . . . . . . . . . 143
6.4 Habilitandosegurançaemaplicações REST . . . . . . . . . . . . . . . 146
6.5 ConhecendoWS-Security . . . . . . . . . . . . . . . . . . . . . . . . . 151
6.6 A j u s t e sdeinfra-estrutura. . . . . . . . . . . . . . . . . . . . . . . . . . 161
6.7 Ocallbackdeverificaçãodasenha. . . . . . . . . . . . . . . . . . . . . 165
6.8 Aatualizaçãodoserviçodeusuários. . . . . . . . . . . . . . . . . . . 166
6.9 Aimplementaçãodométododebusca . . . . . . . . . . . . . . . . . . 171
6.10 Realizeacomunicaçãoentreosdoissistemas . . . . . . . . . . . . . . 173
6.11 TestescomSoapUI. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 180
6.12 Crieoclienteseguro. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 184
6.13 Sumário. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190
7 Design Patterns e SOA 191
7 . 1IntegraçãoversusSOA . . . . . . . . . . . . . . . . . . . . . . . . . . . 191
7 . 2OModeloCanônico . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 192
7 . 3Desenvolvimentocontract-first . . . . . . . . . . . . . . . . . . . . . . 199
7 . 4ServiçosassíncronoscomWS-Addressing . . . . . . . . . . . . . . . . 210
7 . 5Sumário. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .220
8 Flexibilizando sua a p l i c ação com um ESB 221
8.1 ComoinstalaroOracleWebLogiceoOEPE. . . . . . . . . . . . . . . 222
8.2 AinstalaçãodoOSB. . . . . . . . . . . . . . . . . . . . . . . . . . . . .228
8.3 ConfiguraçãodoOSB . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232
8.4 ConceitosdoOSB . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .243
8.5 CrieumarotanoOSB. . . . . . . . . . . . . . . . . . . . . . . . . . . .244
8.6 Sumário. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .248
9 C o o r d e n ese rviços com BPEL 2 4 9
9.1 Conheçaorquestraçãoecoreografia. . . . . . . . . . . . . . . . . . . .250
9.2 instaleoOracleSOASuite . . . . . . . . . . . . . . . . . . . . . . . . .250
9.3 InstaleoJDeveloper . . . . . . . . . . . . . . . . . . . . . . . . . . . . .260
9.4 IntroduçãoaBPEL. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .264
9.5 Sumário. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 274
xi

## Página 16

Sumário CasadoCódigo
10 Conclusão 275
Bibliografia 277
Versão: 16.2.5
xii

## Página 17

Capítulo1
ComeçandoumprojetoSOA
“ E mtodas as coisas, o sucesso depende de preparação p ré v i a .”
–Confúcio
1.1 Coisasinesperadas acontecem!
V o c êfoi contratado como arquiteto de um novo projeto: desenvolver um e-
commerce,chamadoknight.com,paraumaeditoradelivros.Comoarquiteto,tudo
oquevocêsabeinicialmenteéquedeveserumsistemademédioporte.V o c êde-
cidecomeçarodesenvolvimentodoprojetopelapartequelhepareceumaunanimi-
dade:ocontroledeestoque.Paraisso,criaumprojetobaseadoemJavaEEchamado
knight-estoque.war.Esteprojetopossuiaseguinteestrutura:
* knight-estoque.war
* vários pacotes distintos...
* com.knight.estoque.modelos;
* com.knight.estoque.daos;
* com.knight.estoque.controllers;

## Página 18

1.2.Formatosdearquivos:CSV CasadoCódigo
Depoisdeváriosmesesdedesenvolvimento,omóduloélançado.Elepareceser
funcionaleprontoparaserutilizadoemoutrasaplicações, massurgeumproblema:
porquestões denegócios,agerênciadecideque,paraqueosistemafaçasucesso,
deveserpossívelinteragircomomesmo.
T a lrequisitoéabsolutamenteagnósticoemtermosdelinguagemdeprograma-
ção:deveserpossívelinteragircomosistemaatravésdecelulares,aplicações escritas
emJava,C#,PHPediversasoutras(atémesmoporAPIsderedessociais).V o c ênão
estavapreparadoparaisso,afinal,vocêsóestavaacostumadocomodesenvolvimento
desistemasdeumaúnicalinguagem,quenãoprecisavainteragircomnadaexterno.
1.2 Formatos de arquivos : CSV
Oseuprimeiropensamentoérealizaraintegração atravésdetrocasdearquivos,
porexemplo,osfamososarquivosCSV(Comma-Separated V a l u e s). Paraavaliaro
formato,vocêescolheaprincipalclassedosistema, Livro:
package com.knight.estoque.modelos;
import java.util.List;
public class Livro {
private String nome;
private List<String> autores;
private String editora;
private Integer anoDePublicacao;
private String resumo;
// getters e setters..
}
Todososatributosdaentidadelivrosãoperfeitamenteelegíveisparaseremin-
cluídosemumaúnicalinhadoCSV,excetoalistagemdeautores:porserumalista
(ouseja,nãoterumadefiniçãoexatadonúmerodeautores),vocêdecidequeame-
lhorestratégiaparalidarcomelaécolocaremumasegundalinha.Assim,oformato
fica:
[nome];[editora];[ano de publicação];[resumo];
[autores (separados por ponto-e-vírgula)]
2

## Página 19

CasadoCódigo Capítulo1.ComeçandoumprojetoSOA
Noentanto,oseguintepensamentovemàsuamente:eseumaterceiralinha
(paracomportarumanovalistagem)precisarseradicionada?Esemaisumcampo
foradicionado?E,pior:eseumcampoprecisarserremovido?Porexemplo,supo-
nhaqueoseguintearquivoCSVégerado:
Guia do Programador;Casa do Código;2012; Vá do "nunca programei" ...;
Paulo Silveira;Adriano Almeida;
Ruby on Rails;Casa do Código;2012;Crie rapidamente aplicações web;
Vinícius Baggio Fuentes;
Nocasoacima,seocampo editora,porexemplo,tiverqueserremovido,todas
asaplicações clientesdevemseralteradasparareconheceroformatonovo.Casoas
alterações nãosejamreprogramadas,duascoisaspodemacontecer:ouasaplicações
passamaidentificaroanocomoeditora,oresumocomoano(!) eacharquenão
existeresumoalgum,ouelaspodemsimplesmentedetectaroproblemaepassara
lançarexceções.
Ambososcasossãoindesejáveis,assimcomonotificartodasasaplicações clien-
tespodeserimpraticável,dependendodonúmerodeclientesqueexistirem.
1.3 Discussão sobre formatos : linguagens demarca -
ção
V o c ênota,então,queesseéumcasodeusoidealparaumalinguagemdemarcação
qualquer,jáque,emgeral,aslinguagensdemarcaçãopossuemboasdefinições do
quecadacamporepresenta,nãooriginamproblemascasoalgumcamposejaadici-
onadoeminimizamimpactoscasohajaumaremoçãodecampos.
V o c êdecideentãoavaliaroXML(eXtensible M a r k u pLanguage),porqueéuma
daslinguagensdemarcaçãomaisantigasemaisbemaceitasemtermosdeinterope-
rabilidadeentrelinguagens,vistoquepertenceàmesmafamíliadoHTML(queéo
formatoutilizadoportodasaspáginasdaWeb).
Porexemplo,adefinição doexemplodelivros,mostradanaseção 1.2,ficaria
assimemXML:
<livros>
<livro>
<anoDePublicacao>2012</anoDePublicacao>
<autores>
<autor>Paulo Silveira</autor>
3

## Página 20

1.4.Qualcamadadetransporteutilizar? CasadoCódigo
<autor>Adriano Almeida</autor>
</autores>
<editora>Casa do Código</editora>
<nome>Guia do Programador</nome>
<resumo>Vá do "nunca programei" ...</resumo>
</livro>
<livro>
<anoDePublicacao>2012</anoDePublicacao>
<autores>
<autor>Vinícius Baggio Fuentes</autor>
</autores>
<editora>Casa do Código</editora>
<nome>Ruby on Rails</nome>
<resumo>Crie rapidamente aplicações web</resumo>
</livro>
</livros>
Alémdetudoisso,vocênotaque,nãoimportaaordememqueoscamposapa-
reçam,elescontinuamautoidentificados,tendoinclusiveobônusdeserfacilmente
legívelporsereshumanos.Destaforma,vocêdecideutilizarXML.Agora,sóprecisa
definiramaneiradeenviaresseXMLparaoutrossistemaserecebê-lostambém.
1.4 Qu a lcamada de transporte utilizar?
Aopçãomaisóbviaquevemàsuamentepararealizaressatransferênciaseriauma
leituradiretadedisco,talvezcomutilização deNA S(Network-Attached Storage,
quebasicamenteconsistenaideiadeterumservidordedicadoaoarmazenamento
derede)oumesmoSAN(Storage A r e aN e t w o r k,queconsistedeutilizarumarede
completadearmazenamento,comgerenciamentoviasoftware,segurançaintrínseca
etc.).Porém,diversosimpedimentossãoapontados:pelofatodehaverváriosclien-
tes,podemexistirconflitosdesegurança,sobrescritadearquivosetc. Alémdisso,
existemosproblemasdequepessoascapacitadasemgerenciamentoderecursos
dessanaturezadevemserempregadasetambéma(quasecerta)burocraciaquepode
existiraoredordogerenciamentodessesrecursos.
Comtantosimpedimentoscirculandoaleituradireta,aopçãoquelogovemà
cabeça,nesseaspecto,éoFTP.Alémdeserumrecursomuitomaisbaratoporvários
pontosdevista,tambémtemformasdesegurançainternas.Noentanto,ogerenci-
amentodesegurançanãoémuitoabrangente,semcontarquepodenãoapresentar
tantainteroperabilidadeemrelaçãoaváriaslinguagensdeprogramação.Alémdisso,
4

## Página 21

CasadoCódigo Capítulo1.ComeçandoumprojetoSOA
dequalquermaneira,vocêprecisadeumsistemaeficientenaquestãodeenviarere-
ceberdadosdeforma online,nãoapenasescritadedados(dequalquermaneiraque
elaseja).
Destemodo,amelhorsoluçãoquelhevemàmenteéenviardadospormeiode
sockets.V o c êfazalgunstesteselheparecebom.Noentanto,cominvestigações mais
aprofundadas,vocêcomeçaaperceberalgumasfalhas.Primeiro,afaltaumproto-
colodetransportedificultaapassagemdequaisquermetadados,alémdedificultara
encriptaçãodedados.Alémdisso,aindaéaltamenteinsegurofazertráfegodedados
atravésdessetipodecomunicação,pois hackerspodemaproveitaressabrechapara
atacaraaplicação—motivopeloqualnenhumanalistadesegurançairiapermitir
essetráfego.
Oquefazer,então?Amelhorsoluçãoparacontornartodosestesproblemasseria
fazerusodeHTTP(HyperT extTransfer Protocol).Esteprotocoloimplementapas-
sagemdemetadadosatravésdecabeçalhos,podetransportarosdadosdemaneira
segura(atravésdasobreposiçãodeSSL—Secure Sockets Layer),semcontarqueé
praticamenteonipresente(todasaspáginasdeinternetsãotrafegadasutilizandoesse
protocolo),fazendo-otergrandeaceitaçãonasdiferenteslinguagensdeprograma-
ção.
V o c êdecidepesquisarmaisarespeitodacombinaçãoXML/HTTPquandovocê
achaumartigosobreW e bServices.Aideiaébemsimples:trafegarXMLutilizando
HTTPcomoprotocolodetransporte.Alémdisso,acrescentaumcontratodeserviço,
quemostraoqueéesperadocomoentrada/saídadoprovedordedados.
WebServicese o protocolo de transporte
OsW e bServicestradicionaisnãoestãorestritosàutilizaçãoapenas
deHTTP.Noentanto,pelagrandeaceitação desseprotocolo,agrande
maioriadosserviçosimplementadosemempresassão exclusivospara
HTTP,enãoexistemmuitosprovedoresdeW e bServicesemoutrostipos
deprotocolo.
Atítulodecuriosidade,alinguagemJavaprovêmecanismospara
transporteutilizandoprotocolosRMI,JMS,entreoutros.Paramaisin-
formações, vejaoprojetoA p a c h eWSIFemhttp://ws.apache.org/wsif/.
V o c êdecidefazerumtestesobreumadasfuncionalidadesdomódulodeesto-
5

## Página 22

1.4.Qualcamadadetransporteutilizar? CasadoCódigo
ques,chamada“ o b t e rcatálogo”.Elanadamaisfazdoqueobteralistagemdelivros
disponíveisparavenda.Ocódigoinicialdoserviçoéoseguinte:
package com.knight.estoque.servicos;
// imports omitidos
public class ListagemLivros {
public List<Livro> listarLivros() {
LivroDAO livroDAO = obterDAO();
return livroDAO.listarLivros();
}
// outros métodos
}
Para transformar esta classe em web service, basta anotá-la com
javax.jws.@WebService;eparaexporestewebservice,ouseja,deixá-lopronto
parausoemoutrasaplicações, bastautilizaraclasse javax.xml.ws.Endpoint.
Nãosepreocupe,tudoissoestáinclusonaJDK,apartirdoJava6.
J A X - W Se a compatibilidadede bibliotecas
Nasversões anterioresaoJava6,oJAX-WSeoJAXBprecisavamser
baixadoseempacotadosjuntodaaplicação. Comváriosproblemasde
incompatibilidadeentreváriasimplementações deambos,acabou-sede-
cidindoqueelesdeveriamestardisponíveisdiretamentenaJREdoJava
—oquecausaalgunsproblemasemaplicações projetadaspararodarem
Java5equenaverdade,executamemJava6.T e n h asempremuitocui-
dadocomessecenário.
Aclasseanotada,ejácomummétodoqueinicializaoserviço,ficaassim:
package com.knight.estoque.servicos;
// imports omitidos
6

## Página 23

CasadoCódigo Capítulo1.ComeçandoumprojetoSOA
@WebService
public class ListagemLivros {
public List<Livro> listarLivros() {
LivroDAO livroDAO = obterDAO();
return livroDAO.listarLivros();
}
// Outros métodos...
public static void main(String[] args) {
Endpoint.publish("http://localhost:8080/livros",
new ListagemLivros());
System.out.println("Serviço inicializado!");
}
}
Alémdisso,vocêtambémprecisaidentificarasclassesqueirão trafegarpela
redeperanteosistemade parsingdedados. Paraisto,énecessáriocolocarum
arquivochamado jaxb.indexqueiráreferenciarestasclassesapartirdopa-
coteondeeleestá.Porexemplo,setivermosumaclasseJavacomnomecompleto
com.knight.estoque.modelos.Livro,ecolocarmosoarquivo jaxb.index
nopacote com.knight.estoque.modelos,oconteúdodomesmoserásomente
alinha Livro.
Então,noarquivo jaxb.index,podemoster:
Livro
Ocódigocompletoficariaassim:
7

## Página 24

1.5.Eagora,comotestarumserviço? CasadoCódigo
Figura1.1:Primeirasclassesdoprojeto
1.5 E agora , co mo testar u m serviço?
Aorodarestecódigo,vocêpercebeumdetalhe:nãofazamenorideiadecomoin-
teragircomoserviço!V o c êlêmaisarespeitoedescobrequeumdoselementosde
umwebserviceéumcontrato,chamado WSDL.
Seuserviçoestánoar.V o c êdeuaeleoendereçohttp://localhost:8080/livros,
e,porconseguinte,vocêconsegueocontratodeleemhttp://localhost:8080/livros?
wsdl.
Co m o encontrar o WSDL
Emgeral,oWSDLdeserviçosfeitosemJavasão encontradosadi-
cionando?wsdlaofinaldoendereçodoserviço.Essanãoéumaregra
formal;algumaslinguagensdisponibilizamessecontratocom.wsdlao
finaldoendereçodoserviçoeoutraspodemnemsequerdisponibilizá-
lopelarede.
Acessandoocontrato,vocêencontraumdocumentoquepareceextremamente
complexo,epraticamenteimpossíveldeentender,aodarumarápidaolhada.V o c ê
procuraumpoucomaisnainterneteachaumaferramentachamadaSoapUI,dis-
ponívelemhttp://soapui.org/,queéusadapararealizartestesdewebservices.A p ó s
odownloadeinstalaçãodaferramenta,vocêvêumatelacomoaseguinte:
8

## Página 25

CasadoCódigo Capítulo1.ComeçandoumprojetoSOA
Figura1.2:T e l ainicialdoSoapUI
NoSoapUI,épossívelcolocaroWSDLcomoentradaerealizartestessobreele,
assimcomomostramasfiguras1.3e1.4:
9

## Página 26

1.5.Eagora,comotestarumserviço? CasadoCódigo
Figura1.3:CriandoumprojetocomoSoapUI
Fazendo,então,ainclusãodoprojeto,vocêreparaqueoSoapUIcriouaseguinte
estrutura:
10

## Página 27

CasadoCódigo Capítulo1.ComeçandoumprojetoSOA
Figura1.4:ComeçandoostestescomoSoapUI
Aoclicarduasvezessobre Request 1,vocêsedeparacomumXMLformatado:
ochamado envelope SOAP.
SOAP
SOAPéumasiglapara Simple Object Access Protocol,ouProtocolo
SimplesdeAcessoaObjetos,numatraduçãolivre. Maisàfrente,você
veráemdetalhesesteprotocoloecomomanipulá-locorretamente.
OenvelopeSOAPcontémtodososdadosnecessáriosparaquenossoserviçoin-
terpretecorretamenteosdadosqueestamosfornecendo.Respeitandoopropósito
dainteroperabilidade,eleéinteiramentebaseadoemXML,quedeveser“traduzido”
emtermosdalinguagemqueorecebenaponta.Nonossocaso,elenãopossuiquais-
querparâmetrosainda,eparanós,bastasubmeterarequisiçãodojeitocomoestá.
11

## Página 28

1.6.CrieoprimeiroclienteJava CasadoCódigo
Paraisso,bastaapertarumbotãoverde,emformatode“play”,napartesuperiordo
SoapUIeaoladoesquerdodoendereçodoserviço.
Quandovocêofaz,obtémoseguinteretorno:
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
<S:Body>
<ns2:listarLivrosResponse
xmlns:ns2="http://servicos.estoque.knight.com/">
<return>
<anoDePublicacao>2012</anoDePublicacao>
<autores>Paulo Silveira</autores>
<autores>Adriano Almeida</autores>
<editora>Casa do Código</editora>
<nome>Guia do Programador</nome>
<resumo>Vá do "nunca programei" ...</resumo>
</return>
<return>
<anoDePublicacao>2012</anoDePublicacao>
<autores>Vinícius Baggio Fuentes</autores>
<editora>Casa do Código</editora>
<nome>Ruby on Rails</nome>
<resumo>Crie rapidamente aplicações web</resumo>
</return>
</ns2:listarLivrosResponse>
</S:Body>
</S:Envelope>
1.6 Cr i eo primeiro clienteJa v a
A t éaqui,oseuserviçoestáplenamenteoperacional: écapazdeenviarumXML
contendoumnomedeumaoperação(ouseja,adescriçãodoquevocêquerqueseja
feito),equandoenviaesseXML,umcódigoéexecutadonoservidor,trazendocomo
respostaumXMLcontendodados.Masvocênãoquerpararporaí: vocêq u e rver
código J a v afazendo isso,damelhormaneira.
Existemváriosmeiosdecriarclientesdewebservices—quasetodossão “tu-
nados”pormeiodeIDEs—masojeitomaisfácilcontinuasendo,semdúvidas,
peloprograma wsimport,localizadonapasta bindaJDK.Comoseuserviçosendo
executado,vocêpodecolocarocódigodoclientedoserviçonapasta generated
(relativaapartirdapastaatual)comoseguintecomando:
12

## Página 29

CasadoCódigo Capítulo1.ComeçandoumprojetoSOA
Windows:
%JAVA_HOME%/bin/wsimport.exe -s generated
-keep http://localhost:8080/livros?wsdl
Linux:
$JAVA_HOME/bin/wsimport.sh -s generated
-keep http://localhost:8080/livros?wsdl
Comestecomando,vocêpodeobservarqueaseguinteestruturafoicriada:
V o c êpodecopiarapenasosarquivosdeextensão .javaparaseuprojeto.Estes
arquivoscompõemumclienteJAX-WScompleto,sendoqueaprincipalclasse,aqui,
éListagemLivrosServicequeimplementaainterface ListagemLivros.Po-
demosusá-losparacriarumclientecomoseguintecódigo:
package com.knight.estoque.servicos;
13

## Página 30

1.7.OK,eoqueumwebservicetemavercomSOA? CasadoCódigo
import java.util.List;
public class Client {
public static void main(String[] args) {
//Inicia a fábrica dos proxies
ListagemLivrosService listagemLivrosFactory =
new ListagemLivrosService();
//Obtém um proxy
ListagemLivros listagemLivros =
listagemLivrosFactory.getListagemLivrosPort();
//Executa o método remoto
List<Livro> livros = listagemLivros.listarLivros();
for (Livro livro : livros) {
System.out.println("Nome: " + livro.getNome());
}
}
}
Aexecuçãodessecódigovaiproduziraseguintesaída:
Nome: Guia do Programador
Nome: Ruby on Rails
1.7 O K ,e o que u m web servicetem a ver co m SOA?
A t éaqui,umwebservicedosistemafoiexposto.Issofazcomquevocêtenhaimple-
mentadoSOAnoseuprojeto?Não,nãofaz.Esevocêimplementarmaisdez?Vinte?
Trinta?Talveznão.
Adefiniçãodoquefazumsistemaserorientadoaserviçosnãoéonúmerode
webservicesqueelepossui(aliás,vocêpoderiaconstruirumsistemaorientadoa
serviçossemnenhumwebservice—ver[2]paradetalhes).Noentanto,vocêdeve
enxergaralémdasimplestecnologiaparaentenderoqueéSOA.Nãosetratadeweb
services,massim,de exposição de lógica de negócios a t r a v é sde meios agnósticos
—ouseja,SOAnãoébaseadaemwebservices,massimemquantodosistemapode
seracessadopormecanismosexternosaoprópriosistema,demaneiraindependente
delinguagem.
14

## Página 31

CasadoCódigo Capítulo1.ComeçandoumprojetoSOA
Issoimplica,automaticamente,queseuwebservicenãoprecisanecessariamente
serfeitocomSOAPeumWSDL.Existemoutrosmecanismosparaseofereceroque
sechamadeserviço(dentreessesmecanismos,omaisproeminenteé,semsombra
dedúvidas,REST[6]).NotequeSOA,emsi,étotalmenteagnóstico—representa
maisumconceitodoquesimplesmenteumguiadecomoseraplicado.
Aliás,oqueéumserviço?Arespostaparaessaperguntafoi,emgrandeparte,
responsávelpelagrandeconfusãoemqueSOAesteveenvolvidanosúltimosanos.
Segundo(http://www.soaglossary.com/service.php),umserviçoé:
“(...) u m aunidade de lógica da solução em q u ea orientação a serviços foi aplicada de
maneira significativa. ”
–
Ouseja,umaarquiteturaorientadaaserviçosédefinidaemtermosdeserviços,
queporsuavez,são definidosemtermosdeorientação aserviços. Aorientação
aserviços,conformevistoemhttp://www.soaglossary.com/service_orientation.php
(etambémnolivrodeThomasErl SOA Principles o fService Design[3]),é
“(...)um paradigma de design pretendido para a criação de unidades de lógica de
solução q u esão individualmente moldadas para q u epossam ser coletivamente e
repetidamente utilizadas para r e a l i z a ru mconjunto específico de o b j e t i v o s(...)”
–
Destavezoglossáriofornecequaissão osprincípiosquecompõem essepara-
digma,quesão:
•Contratodeserviçospadronizado;
•Baixoacoplamento;
•Abstração;
•Reutilização;
•Autonomia;
•Nãomanterestado;
•Habilidadedepoderserdescoberto;
15

## Página 32

1.8.Sumário CasadoCódigo
•Habilidadedepodersercomposto.
Ouseja,vocêdevemoldarsuaaplicaçãoparaqueaparterelevantedalógicade
negóciossejaexpostaemformadeserviços,quedevemrespeitarestesprincípios.Ao
teraarquiteturadoseusistemaprojetadacomissoemmente,fazcomqueamesma
sejaorientadaaserviços.
Aolongodestelivro,vocêverácadaumdessesprincípiosseraplicadoemexem-
plospráticos,semprecomadevidamotivação paracadaum. V o c êveráqueSOA
nãoéumbichodesetecabeças,epodeserutilizadohoje,nasuaprópriaaplicação,
epassaracolherosresultadosdissooquantoantes.Divirta-se!
1.8 Sumário
V o c êviu,nestecapítulo,quaisasnecessidadesparasecriarumwebserviceeoque
fazdelesumaótimasoluçãoparaproblemasdecomunicaçãoentrelinguagens.V o c ê
tambémviucomocriarumwebservicesimplesemJava,comorealizartestes(através
daferramentaSoapUI)ecomocriarumclienteparaestewebservice.
V o c êtambémviuque,deacordocomdefinições, emgeralnãosepodechamar
umaaplicaçãodeSOAseelapossuirapenasum web service.V o c êtambémviualguns
dosprincípiosSOAdecriaçãodeaplicações.
Claro,deixamosdevermuitacoisaemdetalhes,aindaestamossónocomeçoda
jornada.V a m o saindaverafundocomoconfiguraroJAXB,asopções decustomi-
zaçãodisponíveisdoJAX-WSequandodevemosusá-las.Enfim,hámuitoporvir,
então,vamoscontinuar?
16

## Página 33

Capítulo2
Entendendoofluxodedados
“ Aignorância afirma o unega veementemente; a ciênciaduvida. ”
–V o l t a i r e
Jáfizemosbastanteatéomomento.Criamosumserviço,conseguimosconsumi-
loatravésdeoutrocódigo,testamoscomoSoapUI,enfim,tudopareceótimo.Mas
muitoaindanãofoiexplicado:comofoifeitaacriaçãodoWSDL?Comofoifeitaa
traduçãode/paraXML?Equantoaocliente,comoelesabiacomoenviarasinforma-
ções?
Paraentenderisso,precisamosprimeirorevisartrêsconceitos-chave: namespa-
cesXML,SOAPeWSDL.
2.1 Co m o funciona a estrutura de namespaces d o
XML
Basicamente,oXMLpossuiumaestruturadeidentificação bastantesemelhanteà
estruturadenomenclaturaemJava(naverdade,depraticamentequalquerlingua-

## Página 34

2.1.ComofuncionaaestruturadenamespacesdoXML CasadoCódigo
gemdeprogramaçãomoderna).Paraevitarconfusãodeconceitos,éutilizadauma
estruturade namespaces,quesãoutilizadosparadiferenciaruma t agdeoutra.Por
exemplo,considereumXMLdeusuários:
<usuarios>
...
</usuarios>
Estariatudobemseessamesma t agnãofosseutilizadaemdiversossistemasdife-
rentes!Paraevitarconflitosentreestruturasdenomesiguais,os namespacespodem
serutilizadosdamesmamaneira,passandoaficarassim:
<usuarios xmlns="http://meusistema.com">
...
</usuarios>
Essaéumagrandeideiaparaevitarconflitosentresistemasquesecomunicam
porXML.Noentanto,àsvezesnãoqueremosdiferenciarascoisas,aocontrário:no
casodeserviçosdesenvolvidosdentrodeumamesmaempresa,édesejávelqueas
t ag susadassejamsemprejustamenteiguais.
Comovocêpôde vernocapítulo1,asferramentasdegeração de web services
criamalgumasestruturasde namespacesautomaticamente.Vejamosnovamenteo
XMLderetornodonossoprimeiroserviço:
<!-- algumas marcações... -->
<ns2:listarLivrosResponse
xmlns:ns2="http://servicos.estoque.knight.com/">
<return>
<!-- Corpo da resposta.. -->
</return>
</ns2:listarLivrosResponse>
NesteXML,onamespaceéhttp://servicos.estoque.knight.com/.Elepodeserre-
ferenciadoemqualquerpontodoXMLemquestão,atravésdoprefixo ns2.Desta
maneira,quandooelementoXMLéns2:listarLivrosResponse,sabemosau-
tomaticamentequeéoelemento listarLivrosResponsedefinidononamespace
http://servicos.estoque.knight.com/.
18

## Página 35

CasadoCódigo Capítulo2. Entendendoofluxodedados
2.2 Conheça o funcionamento d oSOAP
SOAPéumasiglaquesignifica Simple Object Access Protocol(http://www.w3.org/
TR/soap/).Elefoicriadoeémantidopelo W o r l dWide W e bConsortium,ousim-
plesmenteW3C.EletambéméconhecidocomoEnvelopeSOAP,jáqueseuelemento
raizéoEnvelope.Eleobedeceaoseguinteformatogeral:
<soapenv:Envelope
xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ser="http://servicos.estoque.knight.com/"/>
<!-- Aqui pode ter, ou não, um elemento soapenv:Header -->
<soapenv:Body>
<ser:listarLivros />
</soapenv:Body>
</soapenv:Envelope>
Oelemento Envelopeépuramenteum containerparaoselementos Headere
Body.Oelemento Bodycontémocorpodarequisição,propriamentedito:onome
daoperação,parâmetrosetc.Jáoelemento Headercontémmetadadospertinentes
àrequisição,comoinformações deautenticação,endereçoderetornodamensagem
etc.Veremossobreissomaisadiantenolivroecomoesseelementoserve,emgrande
parte,comoelementodeextensibilidadeparaaaplicação deespecificações dere-
cursosadicionaisrelativosawebservices,comoWS-Addressing,WS-Transaction,
WS-Securityeváriosoutrosrecursos.
2.3 Entenda o enorme WSDL
Nocapítulo1,aoacessarmosoendereçohttp://localhost:8080/livros?wsdlparavi-
sualizaroWSDL,nosdeparamoscomumenormeXML,queparaodesenvolvedor
quenuncaoviu,podeserumcódigograndeeassustador:
<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
xmlns:tns="http://servicos.estoque.knight.com/"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns="http://schemas.xmlsoap.org/wsdl/"
targetNamespace="http://servicos.estoque.knight.com/"
name="ListagemLivrosService">
<types>
<xsd:schema>
19

## Página 36

2.3.EntendaoenormeWSDL CasadoCódigo
<xsd:import
namespace="http://servicos.estoque.knight.com/"
schemaLocation="http://localhost:8080/livros?xsd=1">
</xsd:import>
</xsd:schema>
</types>
<message name="listarLivros">
<part name="parameters" element="tns:listarLivros">
</part>
</message>
<message name="listarLivrosResponse">
<part name="parameters" element="tns:listarLivrosResponse">
</part>
</message>
<portType name="ListagemLivros">
<operation name="listarLivros">
<input message="tns:listarLivros"></input>
<output message="tns:listarLivrosResponse"></output>
</operation>
</portType>
<binding name="ListagemLivrosPortBinding"
type="tns:ListagemLivros">
<soap:binding transport="http://schemas.xmlsoap.org/soap/http"
style="document">
</soap:binding>
<operation name="listarLivros">
<soap:operation soapAction=""></soap:operation>
<input>
<soap:body use="literal"></soap:body>
</input>
<output>
<soap:body use="literal"></soap:body>
</output>
</operation>
</binding>
<service name="ListagemLivrosService">
<port name="ListagemLivrosPort"
binding="tns:ListagemLivrosPortBinding">
<soap:address location="http://localhost:8080/livros">
</soap:address>
</port>
20

## Página 37

CasadoCódigo Capítulo2. Entendendoofluxodedados
</service>
</definitions>
Agoraquejápassouotraumaeosustocomessecódigo,vamosentendê-locom
calma.
Nota-sequeoWSDLpossuicincoseções bemdefinidas: types, message
(ondepodeexistirmaisdeumelemento), portType, bindinge service.
2.4 A definição d o stipos e a seção types
OJAXB(J a v aArchitecture f o rXML Binding)éoresponsável,emJava,porgerar
tiposem XML SchemasapartirdeclassesJavaevice-versa.Porexemplo,tomando
comoparâmetroaseguinteclasse:
package com.knight.estoque.modelos;
// imports omitidos
@XmlAccessorType(XmlAccessType.FIELD)
public class Livro {
private Integer anoDePublicacao;
private List<String> autores;
private String editora;
private String nome;
private String resumo;
//Getters e setters...
}
OJAXBvaimapearestaclasseparaoseguinteconteúdonum XML Schema:
<xs:complexType name="livro">
<xs:sequence>
<xs:element name="anoDePublicacao" type="xs:int" minOccurs="0">
</xs:element>
<xs:element name="autores" type="xs:string" nillable="true"
minOccurs="0" maxOccurs="unbounded">
</xs:element>
<xs:element name="editora" type="xs:string" minOccurs="0">
</xs:element>
21

## Página 38

2.4. Adefiniçãodostiposeaseçãotypes CasadoCódigo
<xs:element name="nome" type="xs:string" minOccurs="0">
</xs:element>
<xs:element name="resumo" type="xs:string" minOccurs="0">
</xs:element>
</xs:sequence>
</xs:complexType>
Isto mostra que as classes são, preferencialmente, mapeadas para
complexTypes ao invésde elementos. V o c êpode notar que os campos da
classe Java foram todos mapeados com seus equivalentes em uma linguagem
chamada XML Schema(naseção2.11vocêverácommaisdetalhescomocustomizar
omapeamentodecampos). Oatributo type, assimcomonumaclasseJava,
determinaatipagemdoelementoemquestão. Essestipospodemsersimples,
como string, int, booleaneoutros(alistagemcompletaestádisponívelem
http://www.w3.org/TR/xmlschema-2/). T a m b é mpodemsercomplexos,comoa
própriaentidade livro.
Ofatodeaclasseserdefinidacomo complexTypequerdizerqueelanãopode
serutilizadadiretamentenoXML.T r açandoumparaleloentreaprogramaçãoJava
eo XML Schema,écomoseo complexTypefosseadefinição deumaclasse. A
maneiradeinstanciarestaclasseéusandoum element,quecontémasdefini-
ções corretasdenúmerodeocorrências,tipagemeoutrosatributosespecíficos.O
atributo minOccurse maxOccursdeterminam,respectivamente,onúmeromí-
nimodeocorrênciaseomáximo.Nocasodelistagens,porexemplo,ovalorde
maxOccurspodeseriguala unbounded,oquequerdizerquenãohálimitesupe-
riorparaonúmerodeelementoscomestenome.
Aseção types,doWSDL,contémessasdefinições deformatosdedadosde
acordocomoqueéesperadopelocódigoJava.Os XML Schemas(tambémchama-
dosdeXSDs),são oformatoidealparaessasdefinições, jáquepossuemumfor-
matodevidamentepadronizadopelaW3C,órgãoqueregulamentaformatosdeda-
dos,normaseregrasdetráfegoeoutrosassuntosrelacionadosàpassagemdedados
pelaweb.Nonossocaso,oesquemacontidonaseção typesfazumaimportação
deumarquivoexterno,referenciadopelaURLhttp://localhost:8080/livros?xsd=1.O
conteúdodestearquivoéoseguinte:
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:tns="http://servicos.estoque.knight.com/"
xmlns:xs="http://www.w3.org/2001/XMLSchema"
version="1.0"
22

## Página 39

CasadoCódigo Capítulo2. Entendendoofluxodedados
targetNamespace="http://servicos.estoque.knight.com/">
<xs:element name="listarLivros"
type="tns:listarLivros">
</xs:element>
<xs:element name="listarLivrosResponse"
type="tns:listarLivrosResponse">
</xs:element>
<xs:complexType name="listarLivros">
<xs:sequence></xs:sequence>
</xs:complexType>
<xs:complexType name="listarLivrosResponse">
<xs:sequence>
<xs:element name="return"
type="tns:livro"
minOccurs="0"
maxOccurs="unbounded">
</xs:element>
</xs:sequence>
</xs:complexType>
<xs:complexType name="livro">
<xs:sequence>
<xs:element name="anoDePublicacao"
type="xs:int"
minOccurs="0">
</xs:element>
<xs:element name="autores"
type="xs:string"
nillable="true"
minOccurs="0"
maxOccurs="unbounded">
</xs:element>
<xs:element name="editora"
type="xs:string"
minOccurs="0">
</xs:element>
<xs:element name="nome"
23

## Página 40

2.5.Anecessidadedaseçãomessages CasadoCódigo
type="xs:string"
minOccurs="0">
</xs:element>
<xs:element name="resumo"
type="xs:string"
minOccurs="0">
</xs:element>
</xs:sequence>
</xs:complexType>
</xs:schema>
Reparequetemosadefiniçãodo complexType livro,assimcomoadefini-
çãodetipos listarLivrose listarLivrosResponse,quecontémrespecti-
vamenteosdadosdeentradaedesaídadométodolistarLivros.Estestipossão,por
suavez,referenciadosporelementosdemesmonome.Estareferênciafaz-seneces-
sáriaparaqueesteselementos,esomenteestes,sejamacessíveispelosusuáriosdo
esquema,ouseja,osclientesdo web service.
O poder d o sXML Schemas
U mXMLSchemapodeserusadoparadefinirmuitascoisasdentrode
umXML,emtermosdevalores:valorespredefinidos,números,sequên-
ciadebytes,eatémesmoexpressões regularesaqueosvaloresdevem
estardeacordo.Noentanto,estenãoéofocodestelivro;casodesejesa-
bermaissobredefinições deschemas,consulteabibliografiadestelivro.
2.5 A necessidaded aseção messages
Oobjetivodaseção messagesé“amarrar”diversoselementos,presentesouimpor-
tadosnaseção types,paracomporosdadosquetrafegarãoefetivamentede/para
oserviço. Lembre-sedeque,atéaqui,nãoexistedefinição algumaquantoaofor-
matodosdadosquetrafegarãoparaoserviço—sabemosqueéXML,masnãote-
mosnenhumadefiniçãodeprotocolodecamadadeaplicação. Nestecaso,aseção
messageséútilparafazeraamarração docorpodamensagemcomcabeçalhos,
porexemplo.
Oconteúdodestaseçãoécompostoporumoumaiselementos part.Cadaum
delessóprecisaconterum name(delivreescolha)eumatributo typeou element,
24

## Página 41

CasadoCódigo Capítulo2. Entendendoofluxodedados
referenciando,respectivamente,um XML type( simpleTypeou complexType)
ouum element.
Repareque,nocasodonossoWSDLgeradoautomaticamente,duasmensagens
foramdefinidas:
<message name="listarLivros">
<part name="parameters" element="tns:listarLivros">
</part>
</message>
<message name="listarLivrosResponse">
<part name="parameters" element="tns:listarLivrosResponse">
</part>
</message>
Osnomesdasmensagenssãogeradosdeacordocomonomedaoperaçãocor-
respondente,eduasmensagens(umaparaarequisiçãoeoutraparaaresposta)são
criadas.Noentanto,podehaverquantoselementos messageforemnecessários,já
queváriasoperações podemserdefinidasnumúnicoWSDL.
2.6 A seção p o r tType
Aseção portTypecontémadefiniçãodasoperações doserviçoemquestão.Elepode
conterumaoumaisdefinições deoperações, comdiversosformatos,asaber:
•Request-response;
•One-way;
•Solicit-response;
•Notification.
Cadaumdessesformatospossuiummecanismodiferentedemensagem. No
modelo request-response,umamensagemdeentradaeumadesaídasãodefinidase
arespostaéobtidademaneirasíncrona(tornando-se,portanto,omeiomaiscomum
detrocademensagens).
Nomodelo one-way,apenasumamensagemdeentradaéespecificada,deforma
queaoperação, comodizonome,édeumaúnicavia,enquantoquenomodelo
solicit-response,umamensagemdeentradaeumadesaídasãodefinidas,porém,a
comunicaçãoéfeitademodoassíncrono.
25

## Página 42

2.7.AdiferençaentreosWSDLsabstratoseconcretos CasadoCódigo
Nomodelo notification,apenasumamensagemdesaídaéespecificada,sendo
umanotificaçãodiretadoservidorparaocliente.
Os modelos request -response e solicit-response
DopontodevistadoWSDL,ambososmodelossãodesenhadosda
mesmamaneira.Omecanismodetransportedevedecidirqualamelhor
formadeenviarumarespostaparaocliente. Emgeral,esseproblema
ésolucionadoatravésdaaplicaçãodomecanismoWS-Addressing,aser
apresentado,queveremosemdetalhesnocapítulo7
2.7 A diferença entre os WSDLs abstratos econcre -
tos
Todososelementosdefinidosatéagorasãoobrigatórios.Osrestantes, bindinge
service,sãoasexceções. Istoporqueoselementosdefinidosatéagorasãousados
para definir o modelo de mensagens. Emoutraspalavras,elesnãotêmqualquer
relaçãocomomeiodetransporteemsi,esão,portanto,agnósticosemtermosde
modelodetransporte.
SeoWSDLfossedefinidoapenascomoselementosqueforamexplicadosaté
agora,eleseriachamadode WSDL abstrato;ouseja,eleapenasdefineosmodelos
demensagem,nãoosdetalhes.Destemodo,elepoderiaficarassim:
<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
xmlns:tns="http://servicos.estoque.knight.com/"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns="http://schemas.xmlsoap.org/wsdl/"
targetNamespace="http://servicos.estoque.knight.com/"
name="ListagemLivrosService">
<types>
<xsd:schema>
<xsd:import
namespace="http://servicos.estoque.knight.com/"
schemaLocation="http://localhost:8080/livros?xsd=1">
</xsd:import>
</xsd:schema>
</types>
26

## Página 43

CasadoCódigo Capítulo2. Entendendoofluxodedados
<message name="listarLivros">
<part name="parameters" element="tns:listarLivros">
</part>
</message>
<message name="listarLivrosResponse">
<part name="parameters" element="tns:listarLivrosResponse">
</part>
</message>
<portType name="ListagemLivros">
<operation name="listarLivros">
<input message="tns:listarLivros"></input>
<output message="tns:listarLivrosResponse"></output>
</operation>
</portType>
</definitions>
Destamaneira,elepoderiaserreutilizadoemváriosoutrosWSDLsdiferentes,
paradefinirváriosformatosdiferentesdeprotocolodetransporteeométodode
transporteemsi.IssoconferegrandeflexibilidadeaoWSDLque,comomencionado
anteriormente,podeterumagrandegamadeprotocolosdetransporteaplicados.O
padrãoJAX-WSéoprotocoloSOAP(Simple Object Access Protocol)sobreHTTP,e
esteseráofocodestelivro.
O WSDL e os modos de transporte
OWSDL,narealidade,nãoélimitadoanenhummodelodetrans-
porteemparticular,epodeseraplicadovirtualmenteaqualquerum.
Noentanto,comorecentecrescimentodosRESTservices,eletemsido
expandidoparacomportaromodeloRESTtambém.Estemodeloex-
pandidoéoWSDL2.0.ComoaespecificaçãoJAX-WS(eamaioriados
serviçosproduzidoshoje)aindanãotrabalhacomestemodelo,concen-
traremosoestudonoWSDL1.1.
2.8 A seção binding
Aseção bindingdonossoWSDLqueabrimosnocapítuloanteriorapresentao
seguinteconteúdo:
27

## Página 44

2.8. Aseçãobinding CasadoCódigo
<binding name="ListagemLivrosPortBinding"
type="tns:ListagemLivros">
<soap:binding transport="http://schemas.xmlsoap.org/soap/http"
style="document">
</soap:binding>
<operation name="listarLivros">
<soap:operation soapAction=""></soap:operation>
<input>
<soap:body use="literal"></soap:body>
</input>
<output>
<soap:body use="literal"></soap:body>
</output>
</operation>
</binding>
O atributo type refere-seao nomedo portType a que este binding
estásendovinculado. Notequetodososelementosapresentamum namespace
XML,referenciadoemtodoodocumentopeloprefixo tns. Destamaneira,uma
referênciaao portType devevir acompanhadadoprefixo tns, tornando-se
tns:ListagemLivros.
Nasequência,oelemento soap:bindingcriaumelementoespecíficoparaopro-
tocoloSOAP1.1(onamespaceestádefinidonoelementoraizdoWSDL, definitions).
ÉesteelementoquemdizqueoprotocolodeaplicaçãoutilizadoseráoSOAP,versão
1.1.Alémdisso,eletambémdefinequeopadrãoSOAPutilizadoseráo document
style.
Jáno elemento operation, são definidos os modelos de tráfego,entre
literalou encoded(conformevistonoboxanterior).T a m b é mdentrodele,háa
definiçãodeumelemento soap:operation,queseencarregadedefinirumcabe-
çalhoHTTP,muitocomumemtráfegoSOAP,chamado SoapAction.Noentanto,
eleéopcional,eéutilizadoapenasparafacilitaroendereçamentodaoperaçãopara
ométodoJavaaserexecutadoemdefinitivo.
SOAP e os padrões de codificação
Osseguintessub-modelosdetransporte,noSOAP,sãoaceitos:
•Document/literalstyle;
•Document/literalwrappedstyle;
28

## Página 45

CasadoCódigo Capítulo2. Entendendoofluxodedados
•Document/encodedstyle;
•RPC/literalstyle;
•RPC/encodedstyle.
Adiferençaentreo document s t y l eeo r p cs t y l eébemsutil:trata-seapenasdeco-
locarounãoaoperaçãoqueestásendoinvocadanoservidornocorpodamensagem
SOAP.Enquantoo documenttrafegaapenasosparâmetrosdasoperações, oRPC
enriqueceestesdadosutilizandoonomedométodoqueestádefinidonoWSDL.No
entanto,o document stylepodeserdifícildeserendereçadonoservidor,por
nãoconteronomedaoperação(lembre-sedequemétodosJavapodemsersobre-
carregados)eo rpcutilizaosnomesdasoperações queestãodefinidosnoWSDL
eque,porestaremseparadosdorestodoconteúdo,tambémpodemserdifíceisde
validar.
Asoluçãoparaestedilemaéousodo document w r a p p e ds t y l e:trata-sede do-
cument s t y l e,porémcomosnomesdasoperações definidosnospróprios schemas.
Comestemecanismo,épossívelreduzirasfraquezasdeambososestilos.
Quantoao literal/ encoded,adiferençaresidequantoapassarinformações
detiposnaprópriamensagemounão.Noentanto,normalmenteousode encoded
apenastraz overheaddeprocessamento,edeveserevitado. Parasabermaissobre
essastipagens,consultehttp://www.ibm.com/developerworks/webservices/library/
ws-whichwsdl/.
2.9 Definição d o sendereços co m a seção service
Finalmente,naseção service,oWSDLtemoseguintetrecho:
<service name="ListagemLivrosService">
<port name="ListagemLivrosPort"
binding="tns:ListagemLivrosPortBinding">
<soap:address location="http://localhost:8080/livros">
</soap:address>
</port>
</service>
Oelemento servicepodeterumoumaissubelementos port,queporsua
vezéutilizadopararelacionaro bindingaendereçosespecíficos.Nonossocaso,
29

## Página 46

2.10.Finalmente,oqueaconteceu? CasadoCódigo
eledefineumsubelemento soap:address,queéresponsávelpordizeraoconsu-
midordoserviçoparaqualendereçoenviaroenvelopeSOAPemquestão.Assim,o
servidorjáestácientedequenaqueleendereçoéesperadoreceberváriasrequisições
atravésdeenvelopesSOAP,assimcomotambémtemnoções decomorespondera
estasmensagens.
2.10 Finalmente , o que aconteceu?
Enviamososeguinteconteúdoparaoendereçohttp://localhost:8080/livros:
<soapenv:Envelope
xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ser="http://servicos.estoque.knight.com/"/>
<!-- Aqui pode ter, ou não, um elemento soapenv:Header -->
<soapenv:Body>
<ser:listarLivros />
</soapenv:Body>
</soapenv:Envelope>
Aofazermosisso,oservidorHTTPqueestavahabilitadonaporta8080danossa
máquinaidentificouqueocontextoera /livros. Estecontexto,porsuavez,es-
tavadiretamenterelacionadoànossaclasse ListagemLivros.Aomandarmosa
t ag ser:listarLivrosdentrodoelemento Body,mostramosaoservidorque
essaeraumarequisiçãoparaaoperaçãolistarLivros,semparâmetros.Oservidor,ao
receberesseconteúdo,realizouaextraçãodoconteúdodoelemento Bodyefez par-
singutilizando(nocasodalinguagemJava)oJAXBparaaconversãodesteconteúdo
emobjetos.
30

## Página 47

CasadoCódigo Capítulo2. Entendendoofluxodedados
J A X Be a conversão de XML para objetos e vice-versa
V o c êpodeterreparadoquenãoexiste,emlugaralgumdonossocó-
digo,umaclassechamada ListarLivrosoualgoassim.Então,como
oJAXBsoubecomorealizar parsingdesteconteúdo?
Arespostaparaestaperguntaresidenoprópriomecanismodecria-
çãodeclassesdaJVM.Aclasse ListarLivroségeradaemtempode
execução (vocêpodeconferirestedetalhenoprópriologdaaplicação,
quandoexecutaroexemplodo1),assimcomoaclasseListarLivrosRes-
ponse,queseráutilizadaparaarmazenaroresultadodaexecução.Caso
necessário,épossívelalterarestasclassesemtempodecompilação —
mostrareicomonocapítulo3.
2.11 Customize a estrutura d oXML co m o J A X B
U m avezquevocêconheceessasinformações, vocêpodeusá-lasaseufavor.Por
exemplo,onossoXMLderetornonãoestáexatamentedamaneiraquequeremos.
Inicialmente,deparamo-noscomoseguinteXMLderespostadonossoserviço:
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
<S:Body>
<ns2:listarLivrosResponse
xmlns:ns2="http://servicos.estoque.knight.com/">
<return>
<anoDePublicacao>2012</anoDePublicacao>
<autores>Paulo Silveira</autores>
<autores>Adriano Almeida</autores>
<editora>Casa do Código</editora>
<nome>Guia do Programador</nome>
<resumo>Vá do "nunca programei" ...</resumo>
</return>
<return>
<anoDePublicacao>2012</anoDePublicacao>
<autores>Vinícius Baggio Fuentes</autores>
<editora>Casa do Código</editora>
<nome>Ruby on Rails</nome>
<resumo>Crie rapidamente aplicações web</resumo>
</return>
31

## Página 48

2.11.CustomizeaestruturadoXMLcomoJAXB CasadoCódigo
</ns2:listarLivrosResponse>
</S:Body>
</S:Envelope>
Noentanto,aformatação desseXMLestáumtantoesquisita. Qualomotivo
deoselementosderespostaserem return? Porquecadaautorestánuma t ag
autores,aoinvésdetercadaautordentrodeuma t ag-pai,queseria autores?
Para customizar o elemento autores, podemos usar a anotação
javax.xml.bind.annotation.XmlElementWrapper. Esta anotação pode
sercolocadatantonoatributoquantoemseu getter. Noentanto,sugiroquevocê
coloquenoatributo,paraquesuaclassenãofiquepoluídacom getterse setters,que
muitasdasvezessãodesnecessários.
Emqualquerquesejaolugaremquevocêcoloqueasanotações, éprecisoorien-
taroJAXBquantoaondeeledeveretiraressasinformações. Paraisso,vocêdeveuti-
lizaraanotação javax.xml.bind.annotation.XmlAccessorType,comum
parâmetrodotipo javax.xml.bind.annotation.XmlAccessType.Aclasse
XmlAccessTypenaverdadeéum enum,quepossuiosseguintesvalores:
•PROPERTY:EstaconfiguraçãofazcomqueoJAXBmapeieos getterse setters
paraXML;
•FIELD:Estaconfiguraçãofazcomqueoscamposdasclassessejammapeados
paraXML(sejamestespúblicosounão);
•PUBLIC_MEMBER:Estaconfiguraçãofazcomqueosmembrospúblicos(cam-
posou getters/setters)sejammapeados. Éaconfiguraçãopadrão,casonada
sejainformado.
•NONE:Estaconfiguraçãofazcomquenenhummembrosejamapeadoautoma-
ticamente,anãoserqueoJAXBsejaexplicitamenteinformadodocontrário.
Desta maneira, a melhor configuração é FIELD, já que mapeia
automaticamente os campos (mesmo que sejam privados). Para os
campos onde queremos modificar informações, utilizamos a anotação
javax.xml.bind.annotation.XmlElement, que pode ser utilizada para
informaraoJAXBonomeda t ag,seéobrigatóriaounão,dentreoutrascaracterísti-
cas.
Podemosconfigurarcompletamenteaclasse Livrodaseguinteforma:
32

## Página 49

CasadoCódigo Capítulo2. Entendendoofluxodedados
package com.knight.estoque.modelos;
// imports omitidos
@XmlAccessorType(XmlAccessType.FIELD)
public class Livro {
private Integer anoDePublicacao;
@XmlElementWrapper(name="autores")
@XmlElement(name="autor")
private List<String> autores;
private String editora;
private String nome;
private String resumo;
// getters e setters...
}
Destamaneira,nossoXMLderetornoficamelhorestruturadoe,consequente-
mente,maiscompreensível:
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
<S:Body>
<ns2:listarLivrosResponse
xmlns:ns2="http://servicos.estoque.knight.com/">
<return>
<anoDePublicacao>2012</anoDePublicacao>
<autores>
<autor>Paulo Silveira</autor>
<autor>Adriano Almeida</autor>
</autores>
<editora>Casa do Código</editora>
<nome>Guia do Programador</nome>
<resumo>Vá do "nunca programei" ...</resumo>
</return>
<return>
<anoDePublicacao>2012</anoDePublicacao>
<autores>
<autor>Vinícius Baggio Fuentes</autor>
</autores>
33

## Página 50

2.11.CustomizeaestruturadoXMLcomoJAXB CasadoCódigo
<editora>Casa do Código</editora>
<nome>Ruby on Rails</nome>
<resumo>Crie rapidamente aplicações web</resumo>
</return>
</ns2:listarLivrosResponse>
</S:Body>
</S:Envelope>
Apróxima t agaserajustadaé return,atravésdeumaconfiguraçãodoJAX-
WSqueéfeitapelaanotação javax.jws.WebResult,colocadadiretamenteno
métodoqueéinvocadocomoserviço.Destamaneira,aclassedonosso web service
ficaassim:
package com.knight.estoque.servicos;
// imports omitidos
@WebService
public class ListagemLivros {
@WebResult(name="livro")
public List<Livro> listarLivros() {
LivroDAO livroDAO = obterDAO();
return livroDAO.listarLivros();
}
// outros métodos...
}
Destaforma,oretornodonossoserviçoficaconformeodesejado:
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
<S:Body>
<ns2:listarLivrosResponse
xmlns:ns2="http://servicos.estoque.knight.com/">
<livro>
<anoDePublicacao>2012</anoDePublicacao>
<autores>
<autor>Paulo Silveira</autor>
<autor>Adriano Almeida</autor>
</autores>
34

## Página 51

CasadoCódigo Capítulo2. Entendendoofluxodedados
<editora>Casa do Código</editora>
<nome>Guia do Programador</nome>
<resumo>Vá do "nunca programei" ...</resumo>
</livro>
<!-- Restante da resposta -->
</ns2:listarLivrosResponse>
</S:Body>
</S:Envelope>
2.12 Resolv amétodos denomes iguaiseadição dep a-
râmetros
Comovocêdeveternotado,nossoserviçonãopossuiatéomomentoquaisquerpa-
râmetros,porém,apartirdeagora,vocêdecidelistarosdadosdeformapaginada.
Confiandonatécnicadesobrecargademétodos,vocêcriaummétododenome
igual,porémpassandocomoparâmetrosonúmerodapáginaeotamanho:
package com.knight.estoque.servicos;
// Imports omitidos
@WebService
public class ListagemLivros {
@WebResult(name="livro")
public List<Livro> listarLivros() {
LivroDAO livroDAO = obterDAO();
return livroDAO.listarLivros();
}
public List<Livro> listarLivros(Integer numeroDaPagina,
Integer tamanhoDaPagina) {
LivroDAO livroDAO = obterDAO();
return livroDAO.listarLivros(numeroDaPagina, tamanhoDaPagina);
}
private LivroDAO obterDAO() {
return new LivroDAO();
35

## Página 52

2.12.Resolvamétodosdenomesiguaiseadiçãodeparâmetros CasadoCódigo
}
public static void main(String[] args) {
Endpoint.publish("http://localhost:8080/livros",
new ListagemLivros());
System.out.println("Serviço inicializado!");
}
}
Porém,aorodarestaclasse,vocêtemumasurpresaaoverqueumaexceçãoé
lançadacomaseguintemensagem:
class com.knight.estoque.servicos.jaxws.ListarLivros do not have a
property of the name arg0
Amensagemdizqueaclasse com.knight.estoque.servicos.jaxws.ListarLivros
nãotemumapropriedadedenome arg0.V o c êprocuranoseuprojetoenãoacha
classealgumacomessenome.Oqueaconteceu,então?
Estaclasseégeradaemtempodeexecução, runtime. AenginedoJAX-WSé
quemagera,combasenonomedométodoqueestásendoexposto,obedecendo
porpadrãoàseguinteregra:utilizaonomedopacoteondeoserviçoestá,acrescenta
jaxwse,então,onomedaoperação. Noentanto,aoperaçãojáexistia,poishavia
doismétodoscomessenome,entãoa enginedoJAX-WSfezacriaçãodaclassepara
oprimeirométodoenãoachounecessáriorecriarparaosegundo(jáqueelestêmo
mesmonome).Comoestaclassefoicriadaparaoprimeirométodo,elanãocontém
osparâmetrosnecessáriosparainvocarosegundo.Daíaexceçãolançada.
É possível customizar esta classe gerada utilizando a anotação
javax.xml.ws.RequestWrapper,eocódigoficaassim:
@WebResult(name="livro")
public List<Livro> listarLivros() {
LivroDAO livroDAO = obterDAO();
return livroDAO.listarLivros();
}
@RequestWrapper(className=
"com.knight.estoque.servicos.jaxws.ListarLivrosPaginacao")
public List<Livro> listarLivros(Integer numeroDaPagina,
36

## Página 53

CasadoCódigo Capítulo2. Entendendoofluxodedados
Integer tamanhoDaPagina) {
LivroDAO livroDAO = obterDAO();
return livroDAO.listarLivros(numeroDaPagina, tamanhoDaPagina);
}
Noentanto,umnovoproblemaacontecequandovocêtentaexecutarestecódigo:
Two classes have the same XML type name
"{http://servicos.estoque.knight.com/}listarLivros".
Use @XmlType.name and @XmlType.namespace to assign different
names to them.
this problem is related to the following location:
at com.knight.estoque.servicos.jaxws.ListarLivrosPaginacao
this problem is related to the following location:
at com.knight.estoque.servicos.jaxws.ListarLivros
Estanovaexceção aconteceporqueasclassesgeradasforammapeadasparao
mesmoelementodo XSD Schemagerado.Comisso,énecessárioutilizarumdedois
atributosdaexceção @RequestWrapper:ou localNameou targetNamespace.
Casoutilizemos localName,devemosatribuirumnomequeaindanãoexistano
XSD,eseforo targetNamespace,devemostomarcuidadoparaqueoelemento
listarLivrosaindanãoexistaneste namespace.
Escolhendo utilizar localName, colocamos o valor
listarLivrosPaginacao. No entanto, os mesmos problemas ocorrem e,
seguindo a mesma linha de raciocínio,temosquemapeara resposta também,
utilizandoaanotação javax.xml.ws.ResponseWrapper.Ocódigoficaassim:
@RequestWrapper(
className="com.knight.estoque.servicos.jaxws.ListarLivrosPaginacao",
localName="listarLivrosPaginacao")
@ResponseWrapper(
className=
"com.knight.estoque.servicos.jaxws.ListarLivrosPaginacaoResponse",
localName="livrosPaginados")
public List<Livro> listarLivros(Integer numeroDaPagina,
Integer tamanhoDaPagina) {
LivroDAO livroDAO = obterDAO();
return livroDAO.listarLivros(numeroDaPagina, tamanhoDaPagina);
}
37

## Página 54

2.12.Resolvamétodosdenomesiguaiseadiçãodeparâmetros CasadoCódigo
Assim,finalmenteocódigoinicializa;porém,nãosemumavisodoJAX-WS:
WARNING: Non unique body parts! In a port, as per BP 1.1 R2710
operations must have unique operation signature on the wire for
successful dispatch. Methods [ listarLivros, listarLivros] have
the same request body block
{http://servicos.estoque.knight.com/}listarLivrosPaginacao. Method
dispatching may fail, runtime will try to dispatch using SOAPAction.
Another option is to enable AddressingFeature to enabled runtime to
uniquely identify WSDL operation using wsa:Action header.
Estamensagemestádizendoque,apesardoJAX-WSterconseguidogeraros
documentos,problemasderoteamento(ouseja,fazeroXMLchegaratéocódigo
Java)podemacontecercasovocêinsistaemutilizarestecódigo,poisasoperações na
seção portTypecontinuamdefinidascomomesmonome.Eledizqueaindaassim
podetentarfazeroroteamento(utilizandoo header SOAPAction);noentanto,este
mecanismopodeapresentarfalhas.V o c êtentaimportaroprojetonoSoapUIeele
dáumamensagemdeerro:
ERROR:An error occured [Duplicate operation with name=listarLivros,
inputName=:none, outputName=:none, found in portType
'{http://servicos.estoque.knight.com/}ListagemLivros'.], see error log
for details
Para alterar o nome do método, vocêpode utilizar a anotação
javax.jws.Webmethod. Com esta anotação, vocêconsegue configurar o
nomequeaoperaçãoteránoWSDL.Ocódigoficaassim:
@RequestWrapper(
className="com.knight.estoque.servicos.jaxws.ListarLivrosPaginacao",
localName="listarLivrosPaginacao")
@ResponseWrapper(
className=
"com.knight.estoque.servicos.jaxws.ListarLivrosPaginacaoResponse",
localName="listarLivrosPaginacaoResponse")
@WebResult(name="livro")
@WebMethod(operationName="listarLivrosPaginacao")
public List<Livro> listarLivros(int numeroDaPagina,
int tamanhoDaPagina) {
LivroDAO livroDAO = obterDAO();
return livroDAO.listarLivros(numeroDaPagina, tamanhoDaPagina);
}
38

## Página 55

CasadoCódigo Capítulo2. Entendendoofluxodedados
Finalmente,vocêconsegueinicializaroserviço,semquaisqueralertas.Sevocê
checarasseções portTypee bindingdoWSDL,veráqueelasficaramassim
(algumasinformações foramomitidasparamelhorlegibilidade):
<portType name="ListagemLivros">
<operation name="listarLivros">
<input message="tns:listarLivros"></input>
<output message="tns:listarLivrosResponse"></output>
</operation>
<operation name="listarLivrosPaginacao">
<input message="tns:listarLivrosPaginacao"></input>
<output message="tns:listarLivrosPaginacaoResponse"></output>
</operation>
</portType>
<binding name="ListagemLivrosPortBinding" type="tns:ListagemLivros">
<soap:binding transport="http://schemas.xmlsoap.org/soap/http"
style="document" />
<operation name="listarLivros">
<soap:operation soapAction=""></soap:operation>
<input>
<soap:body use="literal"></soap:body>
</input>
<output>
<soap:body use="literal"></soap:body>
</output>
</operation>
<operation name="listarLivrosPaginacao">
<soap:operation soapAction=""></soap:operation>
<input>
<soap:body use="literal"></soap:body>
</input>
<output>
<soap:body use="literal"></soap:body>
</output>
</operation>
</binding>
Nofinaldascontas,ficaumalição aprendida: usarsobrecargademétodos
em web services émuitodifícil. Existemtécnicasquepodem possibilitar,mas
nofinaldascontas,acabasendotrabalhosodemaispararesolverumproblema
quenós poderíamostersolucionadosimplesmenterenomeandoométodopara
39

## Página 56

2.12.Resolvamétodosdenomesiguaiseadiçãodeparâmetros CasadoCódigo
listarLivrosPaginacao,porexemplo.
J A X - W Se o mapeamento de métodos
Assimcomoacontecemdiversosproblemascommétodossobrecarre-
gadosemumamesmaclasse,algumas enginesJAX-WStambémtêmpro-
blemascommétodosdenomesiguais,aindaqueelesestejamemclasses
diferentes.Emgeral,nãoérecomendadotermétodosdenomesiguais
empontoalgumdoprojeto—oque,aliás,écondizentecomalgunsprin-
cípiosdeSOAqueveremosaolongodestelivro.
Quandorenomeamosométodo,tudoégeradocomsucesso.Aoregeraroprojeto
noSoapUI,observamosaseguinterequisiçãoprégerada:
<soapenv:Envelope
xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ser="http://servicos.estoque.knight.com/">
<soapenv:Header/>
<soapenv:Body>
<ser:listarLivrosPaginacao>
<!--Optional:-->
<arg0>?</arg0>
<!--Optional:-->
<arg1>?</arg1>
</ser:listarLivrosPaginacao>
</soapenv:Body>
</soapenv:Envelope>
Sefizermosarequisiçãoassim,obteremososeguinteretorno:
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
<S:Body>
<S:Fault xmlns:ns4="http://www.w3.org/2003/05/soap-envelope">
<faultcode>S:Server</faultcode>
<faultstring>java.lang.NullPointerException</faultstring>
</S:Fault>
</S:Body>
</S:Envelope>
40

## Página 57

CasadoCódigo Capítulo2. Entendendoofluxodedados
Issoquerdizerquea engineJAX-WScapturouuma NullPointerException
internamente.Seobservamoso stack trace,nasaídapadrãodanossaaplicação,va-
moschegaràconclusãodequeissoaconteceuporqueosparâmetroseram,naver-
dade,nulos.IssoporqueoJAX-WSnãofezaatribuiçãoda ?aosparâmetros(que
eramdotipo Integer). Ouseja,elepreferiusimplesmenteignorarosvalores.
Issoporque,comovocêdeveterobservado,colocamososparâmetroscomoobje-
tos w r a p p e r,ouseja,objetosparaarmazenarinternamenteosvaloresdosnúmeros.
Épossívelcolocartiposprimitivoscomoparâmetros;noentanto,elessempre
serãopopuladoscomvalores defaultseassimofizermos,enãoteremoscondições
dediferenciarseorequisitantepassouounãoparâmetrosparaoserviço.Portanto,
geralmenteéumaboapráticacolocarobjetos w r a p p e rcomoparâmetros.
2.13 Envie a requisição p e l ocliente
V o c êjácumpriuquasetodasasetapas:reescreveuoserviço,checouaexistênciade
problemasnainicializaçãoeotestoucomSoapUI.U m avezfuncionandodamaneira
esperada,vocêexecutaoclientequehaviaescritoanteriormentequandovocêtem
umasurpresa:nadaacontece.Oclienteaparentementeéexecutado;noentanto,ele
nãoimprimenadanasaída.Oqueaconteceu?
Lembre-sedequevocêfezalterações naestruturaderetorno.Issofazcomqueo
c l i e n tnãoapresenteproblemasdeexecuçãooucompilação,mastambémnãoconsiga
atribuirosresultadosdaexecuçãoaobjetosJava.Ouseja, lembre-se de q u euma
alteração nos web services nunca originarão problemas de compilação, apenas
em t e m p ode execução.Portanto,tenhaemmentequeumaboapolíticadetestes
deveseraplicadanosseusambientessempre.
V o c êtambémpoderiautilizar scriptsnumservidordeintegraçãocontínuapara
sempreregerarosclientesdosseus web servicesquandovocêfizeralterações neles,
assimcomoumaferramentade b u i l dparautilizarsempreasversões maisrecentes
destes clients.
Casovocêfaçaumaalteraçãonoseuserviço,comoinclusãodemétodo(semne-
nhumaalteraçãonosmétodosjáexistentes),nadaacontecerá.Noentanto,sevocê
retirarummétodo(aindaquevocênãoestejautilizandoessemétodoemlugaral-
gum),oseguinteproblemaacontecerá:
Method listarLivrosPaginacao is exposed as WebMethod, but there is no
corresponding wsdl operation with name listarLivrosPaginacao in the
wsdl:portType{http://servicos.estoque.knight.com/}ListagemLivros
41

## Página 58

2.14.Sumário CasadoCódigo
Issoporqueaclassequefaráacomunicaçãopropriamenteditacomoservidor
tambémégeradaemtempodeexecução,doladodocliente.Masessaclasseseráge-
radaimplementandoumainterfaceJava.Seummétodonãoexistirmaisdoladodo
servidor(checagemqueéfeitapeloWSDL),a enginedoJAX-WSnãoterácondições
degeraressaclasse,originandoaexceção.
Existeapossibilidadedecontornaresteproblema(ediversosoutros, como
overheaddetrazerumacópiadoWSDLacadacriaçãode c l i e n t)mantendoum cache
local—ouseja,noladodocliente—doWSDL.Essaabordagempodeterproblemas
comversionamentodocontrato;mas,dopontodevistadeproduçãoémaisvanta-
josomanteresse cache,jáqueasaplicações jáestarãotestadasenãodevem,ounão
deveriam,pelomenos,teressetipodeproblema.
Ocódigodoclienteficacomo:
public static void main(String[] args) {
ListagemLivrosService listagemLivrosService =
new ListagemLivrosService(Client.class.getResource("/livros.wsdl"));
ListagemLivros listagemLivros =
listagemLivrosService.getListagemLivrosPort();
List<Livro> livros = listagemLivros.listarLivrosPaginacao(0, 2);
for (Livro livro : livros) {
System.out.println("Nome do livro: " + livro.getNome());
}
}
2.14 Sumário
Nestecapítulo,vocêviualgunsdosmecanismosmaiselementaresdefuncionamento
deXML.Notavelmente,umdosmecanismosmaisutilizadoséosistemade names-
paces,quesãoutilizadosparafazerreferênciasaelementosXML.V o c êtambémviu
quaissãoasseçõesdeumenvelopeSOAPeasseçõesdeumWSDL.Finalmente,você
viucomocadaumadessasseções trabalhaemconjuntoparatiraromaiorproveito
emtermosdeextensibilidadeebaixoacoplamento.
V o c êtambémviucomoo web serviceJavatrabalhapararealizarainterpretação
dessasinformações, demaneiraqueexecutecorretamenteométodono web servicee
42

## Página 59

CasadoCódigo Capítulo2. Entendendoofluxodedados
retorneosdadosparaocliente.V o c êtambémviualgunsdospossíveisproblemasda
geraçãodo web service,comoanomenclaturadosmétodos,sistemadeparâmetros
eacriação/destruiçãodemétodos.
Nopróximocapítulo,vocêveráalgumastécnicasparamanterseuprojetosus-
tentável,demaneiraadiminuiralgunsdospossíveisproblemasdecomunicação.
43

## Página 61

Capítulo3
N o v o sdesafioseosa j u s t e sfinos
paracontrolesdeexceções e
adaptaçãodedados
“ N ó ssomos o q u efazemos repetidas vezes. Portanto, a excelêncianão éu ma t o ,mas
u mhábito. ”
–Aristóteles
Seu web serviceestácrescendo.U m anovasolicitaçãodadiretoriapedequevocê
crieumnovométodonoseuserviço,paraqueseususuáriossejamtambémcapazes
decriarnovoslivrosemexposição. Noentanto,estacriaçãorequerumsistemade
autorizaçãodeusuários—nãobastaapenasexporoserviço.V o c êdecideentãocriar
aseguinteassinaturaparaométodo:
public void criarLivro (Livro livro, Usuario usuario)
throws UsuarioNaoAutorizadoException

## Página 62

3.1.Customizeosistemadeparâmetros CasadoCódigo
Todavia,vocêaindanãosabecomoosistemavaisecomportarcomapassagem
deparâmetroseotratamentodeexceções. Oquefazer?
3.1 Customize o sistema de parâmetros
Quandovocêcriaessecódigo,aseguinteentradaparaoseuserviçoégeradopelo
SoapUI:
<!-- declarações de namespaces omitidas -->
<soapenv:Envelope>
<soapenv:Header>
</soapenv:Header>
<soapenv:Body>
<ser:criarLivro>
<!--Optional:-->
<arg0>
<!--Optional:-->
<anoDePublicacao>?</anoDePublicacao>
<!--Optional:-->
<autores>
<!--Zero or more repetitions:-->
<autor>?</autor>
</autores>
<!--Optional:-->
<editora>?</editora>
<!--Optional:-->
<nome>?</nome>
<!--Optional:-->
<resumo>?</resumo>
<!--Optional:-->
<dataDeCriacao>?</dataDeCriacao>
</arg0>
<arg1>
<!--Optional:-->
<nome>?</nome>
<!--Optional:-->
<login>?</login>
<!--Optional:-->
<senha>?</senha>
</arg1>
</ser:criarLivro>
46

## Página 63

CasadoCódigo Capítulo3.Novosdesafioseosajustesfinosparacontrolesdeexceções e...
</soapenv:Body>
</soapenv:Envelope>
Oprimeiroproblemaédetectadoassimquevocêvêarequisição:oqueé arg0
e arg1? Osnomesdessesparâmetrosdeveriamser,respectivamente, livroe
usuario,certo?Oqueaconteceu?
Ograndeproblema,aqui,équeoJavanão possuinenhumsistemacapazde
“avisá-lo”dequaissãoosparâmetros.Emoutraspalavras,nãoépossívelarmazenar
onomedosparâmetrosjáqueoJavanãoretémessainformação.T a m b é mnãoseria
sábiosimplesmenteusarosnomesdasclasses,jáqueaassinaturadosmétodospo-
deriaconterváriosparâmetrosdiferentesutilizandoamesmaclasse(porexemplo,
seosparâmetrosdosmétodosfossem String,nãoseriaelegantecolocarosnomes
dosparâmetros,no web service,como string).
Para“contornar”esteproblema,pode-seanotarosprópriosparâmetroscoma
anotação @WebParam,ficandoassim:
public void criarLivro (@WebParam(name="livro") Livro livro,
@WebParam(name="usuario") Usuario usuario)
throws UsuarioNaoAutorizadoException
AovisualizaranovarequisiçãonoSoapUI,vocêvêoseguinteXML:
<soapenv:Envelope>
<soapenv:Header/>
<soapenv:Body>
<ser:criarLivro>
<livro>
<!--Elementos de livro-->
</livro>
<usuario>
<!-- Elementos de usuário -->
</usuario>
</ser:criarLivro>
</soapenv:Body>
</soapenv:Envelope>
Nadamal!Aocolocaraanotação @WebParamnosparâmetros,vocêtemuma
formadedizeraoJAX-WSodeveserfeitocomcadaum.Quandovocêutilizauma
IDEeusao auto-completenosatributosdaanotação,vocêpercebealgunsinteres-
santes:
47

## Página 64

3.1.Customizeosistemadeparâmetros CasadoCódigo
•name
•partName
•targetNamespace
•mode
•header
Destes,umemparticularlhechamaaatenção: header.Esteatributoédefinido
comoum boolean.Oqueissoquerdizer?V o c êalteraaanotação,então,paraficar
assim:
public void criarLivro (@WebParam(name="livro")Livro livro,
@WebParam(name="usuario", header=true) Usuario usuario) ...
AorefazerarequisiçãonoSoapUI,vocêvêoseguinteXML:
<soapenv:Envelope>
<soapenv:Header>
<ser:usuario>
<!-- elementos de usuario -->
</ser:usuario>
</soapenv:Header>
<soapenv:Body>
<ser:criarLivro>
<livro>
<!-- elementos de livro -->
</livro>
</ser:criarLivro>
</soapenv:Body>
</soapenv:Envelope>
V o c ênotouque,agora,emvezde usuariosercolocadodentrodoelemento
Body,eleestáem Header.Qualadiferença?
Emgeral,oelemento Header,numenvelopeSOAP,éutilizadoparapassagem
demetadadoseitensquenãofazempartedarequisiçãopropriamentedita.Nonosso
caso,estamosinvocandoaoperaçãodecriarumlivro.Ousuárioéapenasumele-
mentodesegurança,quenão fazpartedacriação propriamenteditadolivro. Na
verdade,ousuárioéapenasumelementodesegurança—elepode,ounão,seruti-
lizadopelarequisição.
48

## Página 65

CasadoCódigo Capítulo3.Novosdesafioseosajustesfinosparacontrolesdeexceções e...
SOAP e Segurança
PelosimplesfatodeSOAPser“íntimo”doWSDL,pode-seutilizardi-
versosesquemasdeautenticação/autorizaçãoquesãodefinidosnopró-
prioWSDL.Quandooclientelêessesesquemas,jáestácientedeque
devepassarcertasinformações amais,relativasàsegurança.Oconjunto
depráticasdesegurançaéconhecidocomo WS-Security,queveremos
nocapítulo6.
3.2 Conheça o sistema de lançamento de exceções
V o c êdecidecolocarnoseumétodoumcódigoparatratamentodeautenticaçãodo
usuário.Inicialmente,vocêsimplesmenteprojetaaaplicaçãoparalançarumaexce-
ção,casoousuárionãosejaautenticado.Seucódigoficaassim:
public void criarLivro (@WebParam(name="livro") Livro livro,
@WebParam(name="usuario", header=true) Usuario usuario)
throws UsuarioNaoAutorizadoException, SOAPException {
if (usuario.getLogin().equals("soa") &&
usuario.getSenha().equals("soa")) {
obterDAO().criarLivro(livro);
} else {
throw new UsuarioNaoAutorizadoException("Não autorizado");
}
}
Paratestaressecódigo,vocêfazumarequisiçãocominformações inválidasde
autorizaçãoeobtémaseguinteresposta:
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
<S:Body>
<S:Fault xmlns:ns4="http://www.w3.org/2003/05/soap-envelope">
<faultcode>S:Server</faultcode>
<faultstring>Usuário não autorizado</faultstring>
<detail>
<ns2:UsuarioNaoAutorizadoException
xmlns:ns2="http://servicos.estoque.knight.com/">
<message>Não autorizado</message>
49

## Página 66

3.2.Conheçaosistemadelançamentodeexceções CasadoCódigo
</ns2:UsuarioNaoAutorizadoException>
</detail>
</S:Fault>
</S:Body>
</S:Envelope>
Analisandoocódigo,vocênotaqueoconteúdoda t ag Bodynãoémaisalgo
como criarLivroResponse, massim, uma t ag Fault (quealiás,possuio
mesmo namespacequeas t ag sBodye Envelope).
Esta t agrepresenta, no SOAP,que uma falha foi lançada. No conteúdo
do elemento, temos trêsoutros elementos: faultcode, faultstring e
detail. O campo faultcode aceita quatrovalores: VersionMismatch,
MustUnderstand, Client e Server (veja http://www.w3.org/TR/2000/
NOTE-SOAP-20000508/ #_Toc478383510paramaisinformações arespeito).Nesse
aspecto,oscamposqueanossaaplicação deveaplicarsão, defato, Client(que
indicaumproblemanarequisiçãoenviada)e Server(queindicaumproblemano
processamentorealizadopeloservidor).Veremosnaseção3.4comomanipularesse
campo.
Alémdisso,temososcampos faultstring,quecontémumadescrição do
problema,eocampo detail.Este,porsuavez,contémumadescriçãodetalhada
daexceçãolevantada,nocaso, UsuarioNaoAutorizadoException.
SOAP e a sexceções no corpo d amensagem
AespecificaçãoSOAPproíbequeasexceções trafegadasnocorpoda
mensagemsejamrelativasaproblemasdedadospassadosnoelemento
Header.Noentanto,tenhaemmentequeestesproblemasdeautentica-
çãosãotratadospelaespecificação WS-Security.
Ocódigodaclasse UsuarioNaoAutorizadoExceptionéoseguinte:
package com.knight.estoque.servicos;
public class UsuarioNaoAutorizadoException extends Exception {
public UsuarioNaoAutorizadoException() {}
public UsuarioNaoAutorizadoException(String message) {
50

## Página 67

CasadoCódigo Capítulo3.Novosdesafioseosajustesfinosparacontrolesdeexceções e...
super(message);
}
public UsuarioNaoAutorizadoException(Throwable cause) {
super(cause);
}
public UsuarioNaoAutorizadoException(String message,
Throwable cause) {
super(message, cause);
}
//Construtor JDK 1.7
public UsuarioNaoAutorizadoException(String message, Throwable cause,
boolean enableSuppression, boolean writableStackTrace) {
super(message, cause, enableSuppression, writableStackTrace);
}
}
Comovocêpodenotar,éumaexceçãocomum.Ocampo message,presente
noXMLderetornodamensagem,éprovenientedométodogetMessage,presente
emtodaahierarquiadeexceções Java.
3.3 Customize a sessão de detalhes
Examinemosaseçãodedetalhesdaexceçãolançada:
<ns2:UsuarioNaoAutorizadoException
xmlns:ns2="http://servicos.estoque.knight.com/">
<message>Usuário não autorizado</message>
</ns2:UsuarioNaoAutorizadoException>
Oqueaconteceseoclientenão desejar,noentanto,terumcampo message
mapeado? Oqueacontecese,poracaso,vocêdesejarproduzirummapeamento
maisdetalhadodaexceção(trocaro namespace,trocaronomedoelementoetc)?
Esse mapeamento customizado éprovido, em partes, atravésda anotação
@WebFault. Porexemplo,suponhaquequeiramostrocaro namespacedestaex-
ceção para http://servicos.estoque.knight.com/excecoes/eonomedoelementopara
UsuarioNaoAutorizado.Bastaqueanotemosaclasseassim:
51

## Página 68

3.3.Customizeasessãodedetalhes CasadoCódigo
@WebFault(
targetNamespace="http://servicos.estoque.knight.com/excecoes/",
name="UsuarioNaoAutorizado")
public class UsuarioNaoAutorizadoException extends Exception {
//Construtores
}
Quandofazemosestaalteraçãoeenviamosarequisiçãonovamente,oresultado
ficaassim:
<ns3:UsuarioNaoAutorizado
xmlns:ns3="http://servicos.estoque.knight.com/excecoes/"
xmlns:ns2="http://servicos.estoque.knight.com/">
<message>Usuário não autorizado</message>
</ns3:UsuarioNaoAutorizado>
Noentanto,ocampo messagecontinualá.Éimpossíveltiraressemapeamento
(jáqueoJAXB,porpadrão,mapeiaoscamposquecomeçamcom geteométodo
getMessagepertenceàclasse Exception).Oquefazer,então?
Pensando neste problema, o JAX-WS fornece um método chamado
getFaultInfo. Estemétodopoderetornarumobjeto(compatívelcomJAXB)
paraserusadocomoomapeamentodaprópriaexceção. Porexemplo,supondo
quequeiramosqueoelemento UsuarioNaoAutorizadocontenhaumatributo
mensagem,tendoamensagemquefoiusadacomodescriçãodaexceção,podemos
teroseguintecódigo:
@WebFault(
targetNamespace="http://servicos.estoque.knight.com/excecoes/",
name="UsuarioNaoAutorizado")
public class UsuarioNaoAutorizadoException extends Exception {
// construtores
public UsuarioFaultInfo getFaultInfo() {
return new UsuarioFaultInfo(getMessage());
}
@XmlAccessorType(XmlAccessType.FIELD)
public static class UsuarioFaultInfo {
@XmlAttribute
52

## Página 69

CasadoCódigo Capítulo3.Novosdesafioseosajustesfinosparacontrolesdeexceções e...
private String mensagem;
public UsuarioFaultInfo(String mensagem) {
this.mensagem = mensagem;
}
public UsuarioFaultInfo() { }
}
}
O código de lançamento da exceção pode permanecer inalterado (algo
como throw new UsuarioNaoAutorizadoException("Usuário não
autorizado");).Aindaassim,quandotestamosestecódigo,obtemososeguinte
retorno:
<ns3:UsuarioNaoAutorizado mensagem="Usuário não autorizado"
xmlns:ns3="http://servicos.estoque.knight.com/excecoes/"
xmlns:ns2="http://servicos.estoque.knight.com/"/>
3.4 Customize ainda mais o lançamento de exceções
A t éaqui,todaamanipulação deexceções foifeitaatravésdolançamentodelas.
Aindaassim,ocódigonão éflexívelobastante: lembre-sedequeaindaexisteo
campo faultcodeaserpreenchidodemaneiramaisadequada;alémdisso,existe
umcampochamado faultactorquesequerfoipopulado. Comoresolvereste
problema?
AtravésdaAPIdoJAX-WS,épossívelrealizarmanipulação dasexceções por
meiodemanipulaçãodiretadeXML,usandoummecanismohíbridodaAPIJAX-
WSeDOM(Document Object Model).Issopodeserinicializadoapartirdaclasse
SOAPFactory,quecontémmétodosutilitáriosparacriaçãode templatesSOAP.Por
exemplo,paramanipularmoslivrementeestescampos,podemosutilizaroseguinte
código:
SOAPFault soapFault = SOAPFactory.newInstance().createFault(
"Usuário não autorizado",
new QName(SOAPConstants.URI_NS_SOAP_1_1_ENVELOPE,
"Client.autorizacao"));
soapFault
.setFaultActor("http://servicos.estoque.knight.com/LivrosService");
53

## Página 70

3.4.Customizeaindamaisolançamentodeexceções CasadoCódigo
throw new SOAPFaultException(soapFault);
Estecódigoiráproduziraseguintesaída:
<S:Fault xmlns:ns4="http://www.w3.org/2003/05/soap-envelope">
<faultcode>S:Client.autorizacao</faultcode>
<faultstring>Usuário não autorizado</faultstring>
<faultactor>
http://servicos.estoque.knight.com/LivrosService
s</faultactor>
</S:Fault>
Ocampo faultcode,deacordocomaespecificação SOAP,deveserpreen-
chidocomoprefixoXMLquereferenciao namespaceSOAP(ouseja,http://schemas.
xmlsoap.org/soap/envelope/),seguidodeumdosseguintesvalores:
•VersionMismatch
•MustUnderstand
•Client
•Server
Deumamaneiraprática,osúnicoscamposquenosinteressam,nodiaadia,
são oscampos Cliente Server,queindicam,respectivamente,errosnare-
quisiçãopassadapeloclienteouumproblemanoprocessamentointerno.Apartir
daí,informações amaissão incluídascom .(comonoexemplo,ondeoretorno
é Client.autorizacao,indicandoumproblemadeautenticaçãonarequisição
enviadapelocliente).
Quando o campo faultcode épopulado, énecessárioutilizar um pre-
fixo XML, que em nosso caso S referencia o namespace http://schemas.
xmlsoap.org/soap/envelope/ , que o código Java enxerga a partir da constante
URI_NS_SOAP_1_1_ENVELOPE,presentenainterface SOAPConstants.
Ocampo faultactor, poroutrolado,deveserpopuladocomumaURI
quereferenciaocomponentequeoriginouoproblema(nonossocaso,oserviço
LivrosService).
54

## Página 71

CasadoCódigo Capítulo3.Novosdesafioseosajustesfinosparacontrolesdeexceções e...
Porúltimo,umavezqueoobjeto SOAPFaultépopulado,bastalançaruma
exceçãodotipo SOAPFAultException,passandoo SOAPFaultcriadonocons-
trutor. Estaexceção fazpartedaAPIparamanipulação deSOAP,equandoelaé
lançada,vocêestáautomaticamentedizendoaoJAX-WSoquefazer.
Particularmente, a abordagem que me parece mais atraente entre as
duas é o lançamento de uma exceção de negócios (como no caso da
UsuarioNaoAutorizadoException). No entanto, em cenárioscríticos —
ondeovolumededadostrafegadodeveseromenorpossível—podesernecessário
diminuí-loaomáximo.Nestecaso,asegundaopçãopodesermaisinteressante.
3.5 Embarcando mais a fundo no J A X B
Podeserinteressante(parafinsde debugging,porexemplo)queasexceções carre-
gueminformações dedata/hora. OJAXBécompatívelcomostiposqueexistem
nativamentenaAPIJava,como Calendare Date.V o c êdecide,então,modificara
classe UsuarioFaultInfo,quecarregaasinformações daexceçãodeautorização,
paraquecontenhaadatadecriaçãodaexceção.Ocódigopoderiaficarassim:
@XmlAccessorType(XmlAccessType.FIELD)
public static class UsuarioFaultInfo {
@XmlAttribute
private String mensagem;
private Calendar data = Calendar.getInstance();
public UsuarioFaultInfo(String mensagem) {
this.mensagem = mensagem;
}
public UsuarioFaultInfo() {}
}
Destaforma,aexceçãolançadaficariaassim:
<ns3:UsuarioNaoAutorizado mensagem="Usuário não autorizado">
<data>2012-09-30T23:58:35.648-03:00</data>
</ns3:UsuarioNaoAutorizado>
Noentanto,estainformaçãoparececomplexademais.Elaestánoseguintefor-
mato:
55

## Página 72

3.5.EmbarcandomaisafundonoJAXB CasadoCódigo
{ano}-{mês}-{dia}T{hora}:{minutos}:{segundos}.{milissegundos}-{timezone}
EsteéoformatoparadatascompletasutilizadoemXML.Noentanto,elepode
sofrerreduções detamanhobaseadoemregrasarbitrárias.
Pararealizarestasalterações, noentanto,énecessárioutilizarumaclassees-
pecial,chamada XMLGregorianCalendar. Aoutilizá-la,épossívelmodificar
estesvalores,bemcomoremovê-loscompletamente. Noentanto,estaclasseadi-
cionasuaprópriacamadadecomplexidade,comoofatodenão liberaracria-
ção daclassediretamente,sendonecessárioutilizarumaclassedeapoiochamada
DatatypeFactory:
import javax.xml.datatype.DatatypeConfigurationException;
import javax.xml.datatype.DatatypeConstants;
import javax.xml.datatype.DatatypeFactory;
import javax.xml.datatype.XMLGregorianCalendar;
// demais imports
@XmlAccessorType(XmlAccessType.FIELD)
public static class UsuarioFaultInfo {
@XmlAttribute
private String mensagem;
private XMLGregorianCalendar data;
public UsuarioFaultInfo(String mensagem) {
this.mensagem = mensagem;
try {
this.data = DatatypeFactory.newInstance()
.newXMLGregorianCalendar(new GregorianCalendar());
} catch (DatatypeConfigurationException e) {
throw new RuntimeException(e);
}
}
}
Por si só, este código produz a mesma saída que utilizar um
GregorianCalendar comum. No entanto, épossívelusar métodosacessó-
rios,emconjuntocomaclasse DatatypeConstants,paradesconfigurarvalores.
56

## Página 73

CasadoCódigo Capítulo3.Novosdesafioseosajustesfinosparacontrolesdeexceções e...
Porexemplo,suponhaquevocêpreciseremoverasinformações demilissegundose
timezone.Épossívelfazerissoatravésdoseguintecódigo:
this.data.setMillisecond(DatatypeConstants.FIELD_UNDEFINED);
this.data.setTimezone(DatatypeConstants.FIELD_UNDEFINED);
Destamaneira,asaídadoserviçoficaráassim:
<data>2012-10-01T00:32:02</data>
3.6 Tireproveito de adaptadores
Sejamosfrancos: érudimentaradaptaronossosistemaemrelação aosistemade
formatação paraXML.Acoisacertaafazerseria adaptar o sistema de formata-
ção,enãoadaptaraclasse.Pensandonesseprincípio,oJAXBpossuioconceitode
adaptadores.
U madaptadoréumaclasseJavaespecializadaemfazertradução deforma-
tos,ouseja,transformarumaclasseJavaemoutra. Estatradução éútilquando
temosumaclasse(oumesmoumainterface)quenão conseguimosmapearpor-
que,dealgumaforma,elaéfechadaparanós. Algunsexemplosdissosão aclasse
java.util.Date,aclasse java.util.Calendar,ainterface java.util.Map
etc.
Estatraduçãoérealmentemuitosimples.Trata-seapenasdecriaraclasseadap-
tadoraedizeraoJAXBqualclasseutilizarparafazeratraduçãodetipos.Porexem-
plo,suponhaquevocêqueiraincluirumcampo dataDeCriacaonaclasse Livro.
Estaclassefazpartedoseumodeloepodesermapeadaparaumbancodedados
utilizandoJPAe,portanto,fazmaissentidoutilizarnessemapeamentoumaclasse
compatívelcomJPA,como Dateou Calendar.
57

## Página 74

3.6. Tireproveitodeadaptadores CasadoCódigo
Mapeando classes de WebServicespara o banco de d a-
d o s
É perfeitamentepossívelmapearasclassesquecontêmanotações
JAXBparaobancodedados. Noentanto,éconsideradamelhorprá-
ticasepararummapeamentodooutro.Porexemplo,sevocêconfigurar
oJAXBparaacessarosdadosdasuaclassediretamentepeloscampos,
vocêdeveconfiguraroJPAparaacessarestesdadospor getterse setters(e
vice-versa).Alémdisso,notequeéperfeitamentepossívelcolocarcom-
portamentosdenegócionasclassesanotadascomJAXBeJPA—você
verámaisàfrentetécnicasmaiselaboradasparafazerisso.
Vejamosaclasse:
@XmlAccessorType(XmlAccessType.FIELD)
public class Livro {
private Integer anoDePublicacao;
@XmlElementWrapper(name = "autores")
@XmlElement(name = "autor")
private List<String> autores;
private String editora;
private String nome;
private String resumo;
private Date dataDeCriacao = new Date();
// getters e setters
}
Sevocêfizerumarequisiçãoparaseuserviçodessamaneira,obterá,entreoutras
coisas,resultadoscomooseguinte:
<dataDeCriacao>2012-10-02T01:13:14.960-03:00</dataDeCriacao>
Comojávimosantes, esses dados contéminformações minuciosassobrea
data, como os milissegundos da data e a informação de timezone. No en-
tanto,sequisermosmapearestesdadosdeoutraforma,podemosutilizaraclasse
58

## Página 75

CasadoCódigo Capítulo3.Novosdesafioseosajustesfinosparacontrolesdeexceções e...
XMLGregorianCalendar-que,noentanto,nãoécompatívelcomnossonegócio;
émaisumaclassedeadaptaçãoparaoformatodeXML.
Aqui,podemosutilizarumadaptador,queirátransformarainstânciade Date
emumainstânciade XMLGregorianCalendar.Paraisso,osegredoécriaruma
classequeestenda javax.xml.bind.annotation.adapters.XmlAdapter.
Estaclassepossuidoismétodosabstratos, marshale unmarshal,quevão,respec-
tivamente,fazeratraduçãoparaotipoquedeveserconsideradoválidoparatráfego
peloXMLefazeratraduçãoapartirdeste.
Porexemplo,podemoscriaroseguinteadapterpararealizaratradução entre
Datee XMLGregorianCalendar:
package com.knight.estoque.adaptadores;
// imports omitidos
public class AdaptadorDate extends
XmlAdapter<XMLGregorianCalendar, Date> {
public XMLGregorianCalendar marshal(Date date) throws Exception {
GregorianCalendar calendar = new GregorianCalendar();
calendar.setTime(date);
XMLGregorianCalendar xmlGregorianCalendar = DatatypeFactory
.newInstance().newXMLGregorianCalendar(calendar);
xmlGregorianCalendar
.setMillisecond(DatatypeConstants.FIELD_UNDEFINED);
xmlGregorianCalendar
.setTimezone(DatatypeConstants.FIELD_UNDEFINED);
return xmlGregorianCalendar;
}
public Date unmarshal(XMLGregorianCalendar v) throws Exception {
Date date = v.toGregorianCalendar().getTime();
return date;
}
}
Na sequencia, anotamos o campo que queremos adaptar com
javax.xml.bind.annotation.adapters.XmlJavaTypeAdapter:
59

## Página 76

3.7.TrabalhecomJAXBusandoherança CasadoCódigo
@XmlJavaTypeAdapter(AdaptadorDate.class)
private Date dataDeCriacao = new Date();
Agora,quandofizermosumanovarequisição paraoserviço,obteremosose-
guinteresultado:
<dataDeCriacao>2012-10-02T01:13:14</dataDeCriacao>
T a m b é mépossívelutilizaradaptadoresatravésdopacoteinteiro,utilizandouma
combinaçãodedescriçãodopacoteeo XMLAdapter.Bastaquesecrieumarquivo
package-info.java,nodiretóriodopacote,contendoadeclaração packagee
aanotação:
@javax.xml.bind.annotation.adapters.XmlJavaTypeAdapter(
type = java.util.Date.class,
value = com.knight.estoque.adaptadores.AdaptadorDate.class)
package com.knight.estoque.modelos;
Assim,mesmoqueretiremosaanotação XmlJavaTypeAdapterdaclasse
Livro,atraduçãodetiposiráfuncionar.
3.7 Trabalhe co m J A X Busando herança
U mrecursoquetambémpodesermuitoútilquandotrabalhamoscomJAXBéa
questãodaherança.Porexemplo,suponhaquequeiramosmapearumaclassecha-
mada EBook,queestende Livro:
package com.knight.estoque.modelos;
import java.util.List;
public class EBook extends Livro {
private String formato = "PDF";
public EBook() {
super();
}
public EBook(Integer anoDePublicacao, List<Autor> autores,
String editora, String nome, String resumo) {
60

## Página 77

CasadoCódigo Capítulo3.Novosdesafioseosajustesfinosparacontrolesdeexceções e...
super(anoDePublicacao, autores, editora, nome, resumo);
}
public String getFormato() {
return formato;
}
public void setFormato(String formato) {
this.formato = formato;
}
}
Mesmoquefaçamosainserçãodestaclassenoarquivo jaxb.index,a engine
doJAXBnãorealizaráomapeamento.Issoporqueestanãoéjulgadacomonecessá-
ria,postoquenãohá,nocódigo,nenhumareferênciaexplícitaaestaclasse.Ouseja,
elanãoéreferenciadacomoparâmetroemlugaralgumoucomoretorno;apenasre-
ferênciasàclasse Livrosãofeitas.Destaforma,nãoénecessárioincluirestaclasse
noarquivo jaxb.index.Para“forçar”omecanismodoJAXBareconhecê-la,você
precisautilizaraanotação javax.xml.bind.annotation.XmlSeeAlso.
EstaanotaçãofarácomqueoJAXBdetecteaclasse“extra”efaçaomapeamento.
Porexemplo,parafazeromecanismoreconheceraclasse EBook,podemosinserir
aanotaçãonaclasse Livro,destaforma:
package com.knight.estoque.modelos;
//imports omitidos
@XmlAccessorType(XmlAccessType.FIELD)
@XmlSeeAlso({ EBook.class })
public class Livro {
// conteúdo da classe
}
IstofarácomqueoJAXB(e,consequentemente,oJAX-WS)entendaapresença
daclasse EBook. Sevocêderumaolhadano XML Schemagerado,perceberáo
seguintetrecho:
<!-- Código referente ao mapeamento da classe Livro -->
<xs:complexType name="livro">
61

## Página 78

3.7.TrabalhecomJAXBusandoherança CasadoCódigo
<xs:sequence>
<xs:element name="anoDePublicacao" type="xs:int" minOccurs="0"/>
<xs:element name="autores" minOccurs="0">
<xs:complexType>
<xs:sequence>
<xs:element name="autor"
type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
</xs:sequence>
</xs:complexType>
</xs:element>
<xs:element name="editora" type="xs:string" minOccurs="0"/>
<xs:element name="nome" type="xs:string" minOccurs="0"/>
<xs:element name="resumo" type="xs:string" minOccurs="0"/>
<xs:element name="dataDeCriacao" type="xs:anySimpleType"
minOccurs="0"/>
</xs:sequence>
</xs:complexType>
<!-- Código referente ao mapeamento da classe EBook -->
<xs:complexType name="eBook">
<xs:complexContent>
<xs:extension base="tns:livro">
<xs:sequence>
<xs:element name="formato" type="xs:string" minOccurs="0"/>
</xs:sequence>
</xs:extension>
</xs:complexContent>
</xs:complexType>
Notequeoconteúdodo complexType eBookcontéma t ag extension.
Esta t agrepresenta,emum XML Schema,aherançadeelementosdeumsupertipo
—exatamentedaformacomoaconteceemJava. Apartirdestaextensão, o XML
Schemainseriumaiselementos,nestecaso,oelemento formato.
Pararealizarotráfegodestasinformações, noentanto,oJAXBintroduzmais
sutileza.Suponhaqueo e-bookde SOA Aplicadosejainseridonabasededados.
Aorecuperarestasinformações utilizandooSoapUI,oseguinteéretornado:
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
<S:Body>
<ns2:listarLivrosResponse
xmlns:ns2="http://servicos.estoque.knight.com/"
62

## Página 79

CasadoCódigo Capítulo3.Novosdesafioseosajustesfinosparacontrolesdeexceções e...
xmlns:ns3="http://servicos.estoque.knight.com/excecoes/">
<!-- outros livros -->
<livro xsi:type="ns2:eBook"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<anoDePublicacao>2012</anoDePublicacao>
<autores>
<autor>Alexandre Saudate</autor>
</autores>
<editora>Casa do Código</editora>
<nome>SOA Aplicado</nome>
<resumo>Aprenda SOA de forma prática</resumo>
<dataDeCriacao>2012-12-14T17:10:48</dataDeCriacao>
<formato>PDF</formato>
</livro>
</ns2:listarLivrosResponse>
</S:Body>
</S:Envelope>
Noteadeclaração doprefixo xsi,parao namespace http://www.w3.org/2001/
XMLSchema-instance . Este namespaceépadronizado pela especificação XML
Schemaparaquesejapossívelrealizaradiferenciação detiposemtempodeexe-
cução. Notequeestetipoprecisareferenciaroqueestáprevistonopróprio XML
Schema,ouseja,fazreferênciaao complex typedenome eBook,enãoàclasse
EBookemsi.
3.8 Trabalhe co m enums
OutrorecursointeressantedoJAXBéapossibilidadedesetrabalharcom enums.
EsteéumrecursopresentenalinguagemJavaparatrabalharcomenumerações de
valoresdemaneiraspreestabelecidas. Porexemplo,jávimoscomotrabalharcom
formatosde e-books.Suponhaquequeiramoslimitarnossasopções etrabalharape-
nascomtrêsformatospreestabelecidos:PDF,MOBIeEPUB.Podemosmodelarum
enumparatrabalharcomestesformatos:
package com.knight.estoque.modelos;
public enum FormatoArquivo {
PDF, MOBI, EPUB;
}
Destaforma,alteramosaclasse EBookparatrabalharcomesteformato:
63

## Página 80

3.8.Trabalhecomenums CasadoCódigo
package com.knight.estoque.modelos;
import java.util.List;
public class EBook extends Livro {
private FormatoArquivo formato = FormatoArquivo.PDF;
public EBook() {
super();
}
public EBook(Integer anoDePublicacao, List<Autor> autores,
String editora, String nome, String resumo) {
super(anoDePublicacao, autores, editora, nome, resumo);
}
// getters e setters
}
Aoinicializaresteserviço,aseguintemodificação natipagemdo complex
type eBookterásidorealizada:
<xs:complexType name="eBook">
<xs:complexContent>
<xs:extension base="tns:livro">
<xs:sequence>
<xs:element name="formato" type="tns:formatoArquivo"
minOccurs="0"/>
</xs:sequence>
</xs:extension>
</xs:complexContent>
</xs:complexType>
Note que, agora, o elemento formato faz referênciaa um novo tipo,
formatoArquivo.Maisàfrente,nomesmo XML Schema,estáadefiniçãodesse
tipo:
<xs:simpleType name="formatoArquivo">
<xs:restriction base="xs:string">
<xs:enumeration value="PDF"/>
64

## Página 81

CasadoCódigo Capítulo3.Novosdesafioseosajustesfinosparacontrolesdeexceções e...
<xs:enumeration value="MOBI"/>
<xs:enumeration value="EPUB"/>
</xs:restriction>
</xs:simpleType>
Aindapodemosrealizaracustomizaçãodonomedotipoutilizandoaanotação
javax.xml.bind.annotation.XmlEnum.T a m b é mpodemoscustomizarosva-
loresutilizandoaanotação javax.xml.bind.annotation.XmlEnumValue.
Porexemplo,suponhaquequeiramosquetodososvaloresdaenumeraçãoestejam
emletrasminúsculas.Podemosescrevê-ladaseguintemaneira:
package com.knight.estoque.modelos;
//imports omitidos
@XmlEnum
public enum FormatoArquivo {
@XmlEnumValue("pdf")
PDF,
@XmlEnumValue("mobi")
MOBI,
@XmlEnumValue("epub")
EPUB;
}
Aorealizarmosestamodificação,oseguinteapareceráno XML Schema:
<xs:simpleType name="formatoArquivo">
<xs:restriction base="xs:string">
<xs:enumeration value="pdf"/>
<xs:enumeration value="mobi"/>
<xs:enumeration value="epub"/>
</xs:restriction>
</xs:simpleType>
Sequisermosalteraronomedeste simple type,podemostambémutilizar
aanotação javax.xml.bind.annotation.XmlType. Eladáopoderdealte-
rarasdefinições dequaisquertipos—simplesoucomplexos.Paraalteraronome
65

## Página 82

3.9.Modelesuasclassescomcomportamentosdenegócioemantenha-asmapeadascomJAXBCasadoCódigo
do simple type formatoArquivo,porexemplo,podemosrealizaraseguinte
definiçãodo enum:
@XmlEnum
@XmlType(name = "formato")
public enum FormatoArquivo {
//valores presentes no enum
}
Destaforma,otipoalteradofica:
<xs:simpleType name="formato">
<xs:restriction base="xs:string">
<xs:enumeration value="pdf"/>
<xs:enumeration value="mobi"/>
<xs:enumeration value="epub"/>
</xs:restriction>
</xs:simpleType>
3.9 Modelesuas classes co m comportamentos de ne -
gócio e mantenha -a smapeadas co m J A X B
EricEvans,emseulivroDomain-DrivenDesign[5],eMartinFowleremseuartigo
sobreAnemicDomainModel[7]ressaltamaimportânciadecriarumacamadare-
levantedeclasses,quemodelamdeformaadequadaonegócioemumaaplicação.
Manterclassesqueapenasmantenhamdados,com getterse settersenadamais,faz
comqueosistemafiqueengessado,incapazdeserresponsivoamudanças.
Quandodesenvolvemos web servicesemJavaeutilizamosaabordagemdegera-
çãodoWSDLapartirdocódigo(abordagemconhecidacomo code fi r s t),podemos
(edevemos!)tirarproveitodetécnicasdemapeamentoavançadasdeJAXB,dema-
neiraquepodemosmodelarocomportamentodenegócionasprópriasclassesque
utilizamosparatrafegarnossosdadosemXML.
66

## Página 83

CasadoCódigo Capítulo3.Novosdesafioseosajustesfinosparacontrolesdeexceções e...
Restrições em relação a comportamento de negócio e
web services
Aplicarcomportamentodenegóciosem web servicespodeserma-
ravilhoso;noentanto,deve-setomarmuitocuidadocomomodelode
desenvolvimento.SevocêforcriarasclassesapartirdeXMLSchemas,
vocêprovavelmenteperderáocódigoadicionado.Portanto,tenhacer-
tezadequevocêestádesenvolvendoutilizandoomodelo code fi r s tou
algumaferramentaquemantenhacódigopreexistente(nãoéocasodo
wsimport).
Algunsdosprincipaisproblemasrelacionadosaessetipodedesenvolvimento
estãoligadosaotráfegoindesejadodeinformações de/paraosclientes.Porexemplo,
suponhaquequeiramosmodelarumaclasse Autor:
public class Autor {
private String nome;
private Date dataNascimento;
// getters e setters
}
Portanto,parecelógicoquequeiramosmodificarnossaclasse Livroparatra-
balharcomessaclassenova:
@XmlAccessorType(XmlAccessType.FIELD)
public class Livro {
@XmlElementWrapper(name = "autores")
@XmlElement(name = "autor")
private List<Autor> autores;
//private List<String> autores;
// outros campos
}
Noentanto,nósjápossuíamosantesomapeamentoparaumalistade Strings,
enão gostaríamosdesubstituiromapeamentoantigo. Assim,podemoscriarum
mapeamentoparaconvertersomenteestecampo:
67

## Página 84

3.9.Modelesuasclassescomcomportamentosdenegócioemantenha-asmapeadascomJAXBCasadoCódigo
public static class AdaptadorAutores extends XmlAdapter<String, Autor> {
@Override
public String marshal(Autor autor) throws Exception {
return autor.getNome();
}
@Override
public Autor unmarshal(String autor) throws Exception {
return new Autor(autor, null);
}
}
Agora,bastaquemodifiquemosaclasse Livroparaqueonovomapeamento
estejacompleto:
@XmlElementWrapper(name = "autores")
@XmlElement(name = "autor")
@XmlJavaTypeAdapter(value = AdaptadorAutores.class)
private List<Autor> autores;
Destaforma,reparequeo XML Schemanãoseráalterado,poisoJAXBdetecta
osadaptadoreseinterpretaasdiferenças(ouseja,paratodososefeitos,écomose
tivéssemosmantidooatributo autorescomo List<String>).
Mas e se, por acaso, não quiséssemos trafegar, nunca, o atributo
dataNascimento da classe Autor? É claro, poderíamos anotar a classe
com @XmlAccessorType(XmlAccessType.NONE)e,então,anotaroscampos
quegostaríamosquefossemmapeadoscom @XmlElementou @XmlAttribute:
@XmlAccessorType(XmlAccessType.NONE)
public class Autor {
@XmlElement(name="nome")
private String nome;
private Date dataNascimento;
}
Contudo,umaalternativaqueseria,certamente,maisinteligentenessecasoé
utilizaraanotação @XmlTransient:
68

## Página 85

CasadoCódigo Capítulo3.Novosdesafioseosajustesfinosparacontrolesdeexceções e...
public class Autor {
private String nome;
@XmlTransient
private Date dataNascimento;
}
Destaforma,ocampo dataNascimentoseráignoradoemarquivos xsd,e
casoqueiramosalterarqualquercoisanaclasse Autor,estasmudançasficarãosem-
prebemmaisfáceis.
Comessesrecursos,vocêpodecolocarcomportamentosorientadosanegócios
nasuaprópriaclasse,semproblemascomotráfegodeinformações! Considerea
classe Autor:
public class Autor {
private String nome;
private Date dataNascimento;
public Autor() {
}
public Autor(String nome, Date dataNascimento) {
super();
this.nome = nome;
this.dataNascimento = dataNascimento;
}
public List<URL> getRefs() throws HttpException, IOException {
// Realiza uma busca no Google pelas referências àquele autor.
}
// getters e setters
}
Aclasse Autornão possuinenhumainformação arespeitodemapeamento
JAXB.Nestecaso,aconfiguraçãopadrãoéutilizartodososparesde getterse setters
ecampospúblicos.Noentanto,ométodo getRefsnão possuiumequivalente
(ouseja,nãoexisteummétodo setRefs).Assim,oJAXBnãoiráconsiderareste
69

## Página 86

3.9.Modelesuasclassescomcomportamentosdenegócioemantenha-asmapeadascomJAXBCasadoCódigo
camponotráfegodeinformações, esecriarmosumserviçodelistagemdeautores,
estemétodoserádesconsiderado.T e n t ecriaroserviço:
@WebService
public class AutoresService {
public List<Autor> listarAutores() {
Autor adrianoAlmeida = new Autor("Adriano Almeida", new Date());
Autor pauloSilveira = new Autor("Paulo Silveira", new Date());
Autor viniciusBaggio = new Autor("Vinicius Baggio", new Date());
return new ArrayList<>(Arrays.asList(adrianoAlmeida, pauloSilveira,
viniciusBaggio));
}
public static void main(String[] args) {
Endpoint.publish("http://localhost:8080/autores",
new AutoresService());
}
}
QuandoinvocamosestecódigocomoSoapUI,obtemososeguinteretorno:
<ns2:listarAutoresResponse
xmlns:ns2="http://servicos.estoque.knight.com/">
<return>
<dataNascimento>2012-10-06T12:11:59</dataNascimento>
<nome>Adriano Almeida</nome>
</return>
<return>
<dataNascimento>2012-10-06T12:11:59</dataNascimento>
<nome>Paulo Silveira</nome>
</return>
<return>
<dataNascimento>2012-10-06T12:11:59</dataNascimento>
<nome>Vinicius Baggio Fuentes</nome>
</return>
</ns2:listarAutoresResponse>
Eainda,semudarmosdeideia,podemosmodificarométodo getRefspara
sermapeado,assim:
70

## Página 87

CasadoCódigo Capítulo3.Novosdesafioseosajustesfinosparacontrolesdeexceções e...
@XmlElementWrapper(name = "refs")
@XmlElement(name = "ref")
public List<URL> getRefs() throws HttpException, IOException
Dessaforma,sereiniciarmosonossoserviçoerefizermosarequisição,elavirá
assim:
<return>
<dataNascimento>2012-10-06T12:26:39</dataNascimento>
<nome>Adriano Almeida</nome>
<refs>
<ref>https://twitter.com/ADRIAN0almeida</ref>
<ref>http://twitter.com/adriano_</ref>
<ref>http://www.crmllc.com/people_research.aspx</ref>
<ref>http://en-gb.facebook.com/adriano.almeida.370177</ref>
</refs>
</return>
O mapeamento de métodos com J A X B
OJAXBsópossuiahabilidadedemapearmétodosquesão getters
e setters. Nonossocaso,foipossívelinstalaromapeamentodevidoao
fatodequeométodo getRefspodeserconsideradoum getter. Seo
nomedestemétodonãocomeçassecom get,nãoseriapossívelmapeá-
loparaJAXB—noentanto,aindaseriaperfeitamentepossívelmantê-lo
naclassemapeada.
3.10 Sumário
Nestecapítulo,vocêviumodosavançadosdefazermapeamentosutilizandoJAX-WS
eJAXB.V i uváriasmaneirasdefazer/refazermapeamentosutilizandoestastecnolo-
gias,eviucomoaliarestesconhecimentosamodoselegantesdemodelarsuasclasses
utilizando Domain-Driven Design.
Noentanto,aindaestárestandoalgo.Nopróximocapítulo,vocêverácomoreu-
nirtodosestesconhecimentosparacriaraplicações robustas,capazesdeseremres-
ponsivasadiversoscenáriosdeutilizaçãoemempresas.V a m o semfrente?
71

## Página 89

Capítulo4
EmbarcandonoEnterprise-
ApplicationServers
“Todaempresa p re c i s at e rgente q u eerra, q u enão t e mmedo de errar e q u ea p r e n d e
com o erro. ”
–BillGates
Aofinaldacriaçãodoseumodelodeautores,vocêdecidiucriarmaisumserviço,
AutoresService:
package com.knight.estoque.servicos;
// imports omitidos
@WebService
public class AutoresService {
public List<Autor> listarAutores() {

## Página 90

4.1.ComousarumServletContainer-Jetty CasadoCódigo
Autor adrianoAlmeida = new Autor("Adriano Almeida", new Date());
Autor pauloSilveira = new Autor("Paulo Silveira", new Date());
Autor viniciusBaggio = new Autor("Vinicius Baggio", new Date());
return new ArrayList<>(Arrays.asList(adrianoAlmeida, pauloSilveira,
viniciusBaggio));
}
public static void main(String[] args) {
Endpoint.publish("http://localhost:8080/autores",
new AutoresService());
}
}
Masquandovocêtentainicializaresteserviçoemconjuntocomodelistagem
delivros,vocêtemaseguintemensagem:
java.net.BindException: Address already in use
Basicamente, a mensagem significa que o método publish, da classe
Endpoint,não écapazdepublicarmaisdeumserviçonamesmaporta. Épos-
sívelutilizaressaclasseparapublicarmaisdeum web service;noentanto,como
númerodeserviçoscrescendo,emdiferentespartesdosistema,começaasercom-
plicadogerenciartudo.Oquefazer,então?
4.1 Co m o usar u m Servlet Container - Je t t y
EsseproblemaacontecequandotentamosinicializarumservidorHTTPnumaporta
quejáestásendoutilizada.Entretanto,épossívelmodificarestaabordagemsefor
possívelutilizarumservidorHTTPjáinicializadoquetenhaacapacidadederedi-
recionarrequisições paraos web services.
V o c êleuqueamelhormaneiraderealizaressegerenciamentoéatravésdeum
application server,ouseja,umsistemaqueiráefetuarogerenciamentodesuasapli-
cações demaneirauniforme.V o c êfazumapesquisaedescobreo Jetty,um servlet
container(queécomosefosseummodelosimplificadode application server)real-
mentemuitosimpleseleve,quedeveservirbemàssuasnecessidades.Noentanto,é
precisofazeralgumasalterações noseuprojetoparautilizá-lo.
7 4

## Página 91

CasadoCódigo Capítulo4. EmbarcandonoEnterprise-ApplicationServers
OJavapossuidiversosmodelosdearquivosparasereminstaladosemum a p p l i-
cation server,comoo EAR(Enterprise A r c h i v e),o ejb-jareo WAR(W e bA p p l i-
cation A r c h i v e).V o c êprecisatransformaroseuprojetoem WARparainstalá-lono
Jetty. Issorequerumdiretório WEB-INF,naraizdoseuprojeto,contendoum
arquivochamado web.xml.
ApróximaalteraçãoaserfeitaéadicionarumaimplementaçãoJAX-WSaoseu
classpath. A t éomomentodaescritadestelivro,existemváriasimplementações
(JBossWS,Metro,A p a c h eCXF,aimplementaçãodereferência,eoutros).Porques-
tão desimplicidade,vocêdecidecolocarno classpathoJAX-WSRI—jáque,na
realidade,quandoutilizamosaclasse Endpoint,estávamosutilizandoestaimple-
mentação.
O código fonte d olivro
O código fonte deste livro (disponível em https://github.com/
alesaudate/soa)estáutilizando,comosistemadeconstrução, umfra-
meworkJavachamadoMaven. Eleéutilizadoparasimplificaraadi-
ção/remoçãodebibliotecasdo classpath,edeveserdegrandeutilidade
naconstruçãodeaplicações Java,sejamelasdotipoJAR,W A R ,ouEAR.
A adição do JAX-WSno classpathpode ser feita apenas adicio-
nandoumaentradanoarquivodegerenciamentodoMaven,chamado
pom.xml.
O web.xmldeveteroseguinteconteúdoparahabilitaraimplementação:
<web-app>
<listener>
<listener-class>
com.sun.xml.ws.transport.http.servlet.WSServletContextListener
</listener-class>
</listener>
<servlet>
<servlet-name>jaxws-servlet</servlet-name>
<servlet-class>
com.sun.xml.ws.transport.http.servlet.WSServlet
</servlet-class>
</servlet>
75

## Página 92

4.1.ComousarumServletContainer-Jetty CasadoCódigo
<servlet-mapping>
<servlet-name>jaxws-servlet</servlet-name>
<url-pattern>/*</url-pattern>
</servlet-mapping>
</web-app>
EstearquivoéresponsávelpordizeraoJettyqueeledeveinicializaromeca-
nismodoJAX-WSduranteainicializaçãodoprojeto.Issorequerumarquivocha-
mado sun-jaxws.xml,devidamentecolocadonapasta WEB-INF.Estearquivo,
porenquanto,deveteroseguinteconteúdo:
<endpoints xmlns="http://java.sun.com/xml/ns/jax-ws/ri/runtime"
version="2.0">
<endpoint name="livros"
implementation="com.knight.estoque.servicos.ListagemLivros"
url-pattern="/livros" />
<endpoint name="autores"
implementation="com.knight.estoque.servicos.AutoresService"
url-pattern="/autores" />
</endpoints>
Este XML indica para a engine do JAX-WS RI que a
classe com.knight.estoque.servicos.LivrosService
deve ser mapeada para a URL (relativa) /livros, e a classe
com.knight.estoque.servicos.AutoresService,paraaURL /autores.
Istovaiinicializara enginecorretamente,eeleiráprocurarsemprepeloarquivo
sun-jaxws.xmlnapasta WEB-INF.
OpróximopassoéinicializaroJettyenavegaratéasURLsdosWSDLs(http:
//localhost:8080/livros?wsdlparaoserviçodelivrosehttp://localhost:8080/autores?
wsdlparaoserviçodeautores)paraconferirseosdoisforamcriadoscorretamente.
Utilizando o Maven para inicializaro Jet t y
U m adascapacidadesdoMavenéfacilitaroprocessodeinstalaçãoda
aplicaçãoJavaemum containercomooJetty.Sevocêchecarocódigo-
fontedolivro(disponívelemhttps://github.com/alesaudate/soa),verá
queoconteúdodessecapítulopodeserinicializadoutilizandooco-
mando mvn jetty:run.
76

## Página 93

CasadoCódigo Capítulo4. EmbarcandonoEnterprise-ApplicationServers
4.2 Introdução a EJBs
Conformesuaaplicaçãovaicrescendo,vocêsenteanecessidadedeferramentalmais
completo. Porexemplo,aaplicação aindanão possuiumbomgerenciamentode
transaçõesembancodedados.AcomunicaçãoentreasprópriasaplicaçõesJavatam-
bémaindaéproblemática,poisexistemoutrasaplicações Javautilizandoaaplicação
degerenciamentodeestoques,masnão parece“certo”queasmesmassecomuni-
quemvia web servicesafinal,sendoamesmalinguagem,porqueutilizartradução
de/paraXML?.
V o c êpesquisaarespeitodoassuntoquandodescobreaespecificaçãode E n t e r-
p r i s eJavaBeans(EJB).V o c êaprendequepodeadicionarnãosóisso,mascomode-
senvolvero front-enddaaplicaçãoutilizandoatecnologia JavaServer Faces(JSF),que
seintegrabemaEJBs.Noentanto,existeumproblema:oJettynãosuportaEJBs.O
quefazer?
Fazendoumapesquisaentreos applicationserversquesuportamessatecnologia,
vocêtemváriasopções: OracleWebLogic,IBMWebsphere,Glassfisheoutros.Mas
oquemaislheagradaéoJBossApplicationServer,porser ope nsource,fácilpara
usarerápidoparadesenvolver(aúltimaversãodoJBossApplicationServerpode
serinicializadaempouquíssimossegundos).
Antesdecomeçar,vocêfazumapesquisaparadescobrirquaissão ostiposde
EJBsdisponíveis:
•Beansdesessãocominformaçãodeestado;
•Beansdesessãoseminformaçãodeestado;
•Beansdeentidades;
•Beansorientadosamensagens.
Osúnicosquesãoadequadosa web servicessãoos beanscomeseminformações
deestado.Qualescolher?
Nestecaso,umdosprincípiosdeorientaçãoaserviçosquevêmàtonaéodafalta
demanutençãodeestado.Esteprincípiodizqueumserviçonãodeve,nunca,manter
informações arespeitodoestado.Emoutraspalavras,umarequisiçãoNnuncapode
serdependentedeumarequisiçãoanterior.Oquefazdos beansseminformaçãode
estadoaescolhaadequadapara web services.
77

## Página 94

4.2. IntroduçãoaEJBs CasadoCódigo
V o c êdecidefazerotestetransformandoumadasclassesde web servicesdo
seu projeto em EJB (que, na prática,consiste apenas de anotar a classe com
@Stateless):
package com.knight.estoque.servicos;
import javax.ejb.Stateless;
//Outros imports excluídos
@WebService
@Stateless
public class LivrosService {
// métodos do serviço
}
Maven e a transição entre Jet t y e JBoss Application
Server
Sevocêcompararocódigofontedaaplicação,veráqueexisteumadi-
ferençaenormeentreosarquivosdeinfraestruturadoprojetofeitopara
JettyedoprojetofeitoparaJBossApplicationServer.
QuandoutilizamosJbossAS,nãoénecessáriomaisutilizaroarquivo
sun-jaxws.xml(jáqueoJBossASfazdescobertadosrecursosquede-
vemserexpostoscomo web services),nemoarquivo web.xml.T a m b é m
énecessárioalteraro pluginde deployeogerenciamentodedependên-
cias,jáqueestamostrabalhandocomJBossASeEJBs.
Agora,vocêsóprecisainicializaroJBosse,comovocêjádeveteroplugindo
Maveninstalado,utilizarocomando mvn jboss-as:deploy.U m avezrealizado
o deploy,vocêenxerganoconsoledasuaIDEoseguinte:
21:04:47,380 INFO [org.jboss.wsf.stack.cxf.metadata.MetadataBuilder]
id=com.knight.estoque.servicos.AutoresService
address=http://localhost:8080/soa-cap04-0.0.1-SNAPSHOT/AutoresService
implementor=com.knight.estoque.servicos.AutoresService
78

## Página 95

CasadoCódigo Capítulo4. EmbarcandonoEnterprise-ApplicationServers
invoker=org.jboss.wsf.stack.cxf.JBossWSInvoker
serviceName={http://servicos.estoque.knight.com/}AutoresServiceService
portName={http://servicos.estoque.knight.com/}AutoresServicePort
wsdlLocation=null
mtomEnabled=false
21:04:47,409 INFO [org.jboss.wsf.stack.cxf.metadata.MetadataBuilder]
id=LivrosService
address=http://localhost:8080/soa-cap04-0.0.1-SNAPSHOT/LivrosService
implementor=com.knight.estoque.servicos.LivrosService
invoker=org.jboss.wsf.stack.cxf.JBossWSInvoker
serviceName={http://servicos.estoque.knight.com/}LivrosServiceService
portName={http://servicos.estoque.knight.com/}LivrosServicePort
wsdlLocation=null
mtomEnabled=false
Estetextoéa“prova”dequeseusserviçosestãocorretamenteinstalados.V o c ê
podechecarseelesforaminstaladoscorretamenteindoatéoconsoledeadministra-
çãodoJBoss,localizadoemhttp://localhost:9990/console(casosejaaprimeiravez
quevocêacessaoconsole,vaiprecisarcriarumusuáriodegerenciamentoparavê-lo.
Paraisso,sigaasinstruções dapáginadeerroquevaiapareceraoinvésdoconsole).
79

## Página 96

4.3.Habilitandopersistênciaetransacionalidade CasadoCódigo
Figura4.1:ConsoledoJBosscomosserviçosinstalados
AoexploraroconsoledoJBosséquevocêsedácontadopoderdegerencia-
bilidadequeéconferidoàsuaaplicação: épossívelalteraraportaemqueseus web
servicesserãodisponibilizados,configurarumaportasegura(comHTTPS)paradis-
ponibilização,alteraro hostnamequeseráutilizadoparaofereceressesserviçoseas-
simpordiante.Alémdisso,tambémépossívelcriar datasources(ouseja,serviçosde
persistência),serviçosde cachedistribuído,transacionalidadeemuitomaisrecursos.
AoconfigurarseusserviçoscomoEJBs,vocêestádandoaelesacapacidadede
seremgerenciáveisdessaforma.Issofacilitaráaconfiguraçãodebancosdedados,
transações, cacheseoutrasfuncionalidadesrequeridasemambientesdedesenvolvi-
mentodeempresas.Issotambémfacilitaráatransiçãoentreambientesdedesenvol-
vimento,homologaçãoeprodução.
4.3 Habilitandopersistência e transacionalidade
A t éentão,amanutençãodoestadodobancodedadoséfeitaatravésdeclassesJava,
semhaverumapersistênciaefetiva. Parahabilitarpersistênciaembancodeda-
80

## Página 97

CasadoCódigo Capítulo4. EmbarcandonoEnterprise-ApplicationServers
dos,énecessáriomodificarasentidadesdoserviço,transformando-osem Entity
Beans(ouseja,EJBs).Paraisto,bastaanotá-loscom @Entity,definirumaidenti-
dade(dopontodevistadobancodedados)eadicionarquaisinformações demape-
amentoemrelaçãoaoutrasentidadesqueforemnecessárias.Porexemplo,aclasse
Autorpassaaficarassim:
package com.knight.estoque.modelos;
import javax.persistence.*;
//outros imports omitidos
@Entity
public class Autor {
@Id
@GeneratedValue(
strategy = GenerationType.IDENTITY)
private Long id;
private String nome;
private Date dataNascimento;
// O método refs, assim como getters e setters para os campos
}
Notequeéamesmaclasseutilizadanosserviços,apenasmodificadaparaper-
sistênciaem banco de dados. Em relação ao serviço de autores,basta incluir
uma referênciaao gerenciadorde banco de dados (representadopela interface
EntityManager),eanotá-lacom @PersistenceContextparaqueoJBossin-
cluaasinformações depersistênciaembancodedados:
@WebService
@Stateless
public class AutoresService {
@PersistenceContext
private EntityManager em;
public List<Autor> listarAutores() {
81

## Página 98

4.3.Habilitandopersistênciaetransacionalidade CasadoCódigo
return em.createQuery("select a from Autor a", Autor.class)
.getResultList();
}
}
Paracompletaressaconfiguração,énecessárioadicionarumarquivodeespe-
cificação dasinformações demapeamentodestesobjetosparaobanco,chamado
persistence.xml;e,ainda,umarquivoparadescriçãodaconexãocomobanco
dedadosemsi(oconectoremsiéchamadode datasource).
Oarquivodepersistênciapodeserconfiguradocomooseguinte:
<persistence version="2.0"
xmlns="http://java.sun.com/xml/ns/persistence"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="
http://java.sun.com/xml/ns/persistence
http://java.sun.com/xml/ns/persistence/persistence_2_0.xsd">
<persistence-unit name="primario">
<jta-data-source>java:jboss/datasources/KnightDS</jta-data-source>
<properties>
<property name="hibernate.hbm2ddl.auto" value="create-drop" />
<property name="hibernate.show_sql" value="true" />
</properties>
</persistence-unit>
</persistence>
Não se preocupe com as configurações gerais. Por enquanto, éimpor-
tantenotarapenaso elemento jta-data-source, querepresenta, do ponto
de vista do application server, qual datasource deve ser utilizado. Esse
datasourcepodesercriadoapartirdeumarquivochamado,nonossoexemplo,
de knight-estoque-ds.xml:
<datasources xmlns="http://www.jboss.org/ironjacamar/schema"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://www.jboss.org/ironjacamar/schema
http://docs.jboss.org/ironjacamar/schema/datasources_1_0.xsd">
<datasource jndi-name="java:jboss/datasources/KnightDS"
pool-name="knight-datasource" enabled="true"
use-java-context="true">
<connection-url>
jdbc:h2:mem:knight-estoque;DB_CLOSE_ON_EXIT=FALSE
82

## Página 99

CasadoCódigo Capítulo4. EmbarcandonoEnterprise-ApplicationServers
</connection-url>
<driver>h2</driver>
<security>
<user-name>sa</user-name>
<password>sa</password>
</security>
</datasource>
</datasources>
Notequeestearquivopossuiumaconfiguraçãoespecíficaparafuncionamento
comoJBoss,enãoiráfuncionaremoutros applicationservers.Eleéútil,noentanto,
pararealizartransições entreambientesdedesenvolvimento,homologação epro-
dução,jáqueexisteapossibilidadedecriaro datasourceapartirdoconsolede
gerenciamentodoJBoss,enãodentrodaaplicação,comoestamosfazendo.
Co m o ir a fundo n a JP A
AJPAéumaespecificaçãopoderosíssimapraintegraraplicações Java
combancosdedados,fazendoopapeldeumbibliotecaquefazomape-
amentoobjetorelacional.Dessaforma,permitequevocêtrabalheorien-
tadooobjetoseabstraiatodaacomplexidadenecessáriaparaseintegrar
combancosdedados.
Paraaprendermaissobreessamaravilhosaespecificaçãoesuasimple-
mentações, comooHibernate,recomendoaleituradolivro“Aplicações
JavaparawebcomJSFeJPA”,disponívelpelaEditoraCasadoCódigo.
4.4 Um novo sistema
Adiretoriaestáapreciandoseutrabalhocomosistemadeestoques.Noentanto,o
sistemadecriaçãodelivrosaindaédeficiente.Aosolhosdadiretoriatécnica,resta
criarumgerenciamentoavançadodeusuários.Énecessáriocriarumnovosistema
paraisso.
SOAtemalgumasdasboaspráticasdaprogramaçãoorientadaaobjetos,como
aaltacoesão eobaixoacoplamento. Destepontodevista,éexcelentecriaruma
novaaplicaçãoparagerenciamentodeusuários,jáqueamesmavaioferecerchances
dereusabilidadedalógica(vistoqueváriossistemasdistintospodemutilizarum
cadastrocentralizadodeusuários).Alémdisso,vaipromoverobaixoacoplamento
83

## Página 100

4.4. Umnovosistema CasadoCódigo
entreosserviçoseo“acobertamento”dedetalhesdeusuáriosdopontodevistade
todasasaplicações (dadoque,aoutilizarum web serviceparafazerogerenciamento
deusuários,qualquersistemapodeserutilizado—LDAP,Bancodedados,outros
web services—e,aindaassim,oclienteiráenxergaromesmo web service,mesmo
queosistemamude).Ouseja,apartirdosprincípiosdeorientaçãoaserviçosque
vocêviunocapítulo1,osserviçosdestenovosistemaatenderão:
•Baixoacoplamento;
•Abstração;
•Reutilização;
•Habilidadedepoderemserrecompostos;
SOA e o b a i x oacoplamento
QuandoutilizamosSOA(eprincipalmentequandonossos web servicesestão
funcionandosobreHTTP),podemosrecorreracapacidadesdeelasticidadedanossa
aplicação. Porexemplo,suponhaque,numcenáriode p r o d ução,osistemadege-
renciamentodeusuáriosestejahospedadonomesmoservidordeaplicação queo
sistemadeestoque,comumservidordebalanceamentodecargaintermediandoas
requisições doclienteatéoservidor.Ouseja,umservidorunificadopararepassar
requisições doclienteparaváriosapplication serversquehospedam,defato,asapli-
cações. O layoutgeraldosistemaficariaassim:
Figura4.2:Estruturasimplificadadosserviços
84

## Página 101

CasadoCódigo Capítulo4. EmbarcandonoEnterprise-ApplicationServers
Noentanto,considerequeacargadosserviçosaumenteequeacargadoserviço
deusuárioscresçamuito.Épossíveltomarasseguintesações:
•Colocaroserviçodeusuáriosem application serversseparados;
•Colocarservidoresde cacheparaquenemtodasasrequisições sejamfeitas
diretamenteaos application servers;
•Modificaraestruturadearmazenamento:debancodedadosparaLDAP;
Comessasmodificações, o layoutgeraldosistemaficariaassim:
Figura4.3:Estruturaseparadadosserviços
Noteque,dopontodevistadocliente,nãohádiferençaalguma.Aindaassim,a
separaçãoderegrasdenegócioemserviçosdiferentesnosdáachancederedimensi-
onarainfraestruturanecessáriaparaatenderaestesdiferentesaspectosdenegócio,
semqueosclientesdosnossosserviçostenhamquaisquermodificações paraisso.
Notequeissonãoseriapossívelsenossosserviçosfossemfortementeacoplados,
oumesmointerdependentesentresi.Nesteponto,umaspectomuitoimportantede
SOAvemàtona:anão-manutençãodeestadoporpartedosserviços.Seestesservi-
çosmantivessemestado,nãoseriatãosimplesredimensionaracapacidadedeaten-
dimentodeles,jáquecadaservidorteriaque“conhecer”oestadodosseusvizinhos.
Comonãoéocaso,podemosadicionarouretirarmáquinasàvontadedecadagrupo
deserviços(estacapacidadeéconhecidacomo escalabilidade horizontal).
85

## Página 102

4.5.Sumário CasadoCódigo
Ma sainda assim, falta algo...
Desenvolveronovoserviçodegerenciamentodeusuários,aessaaltura,lhepa-
recesimples. Porém,restamalgumasquestões aseremrespondidas:seráquenão
existenada,naespecificaçãode web services,quepromovaogerenciamentodese-
gurançaapartirdeummodelouniversal(postoqueestaéumaquestãorecorrente
emdesenvolvimentode software)?
V o c êpesquisaarespeitoeencontraaespecificação WS-Security.Parecebom,já
queéummodelopadronizado,enãodevedarmuitosproblemasparacolocarno
projeto.Noentanto,aofazerumabuscanainternetarespeitodecomoimplementar
essemodelo,vocêdescobrequeo application serverquevocêestáutilizando(JBoss)
requerodesenvolvimentodoWSDL antesdocódigo(técnicaconhecidacomode-
senvolvimento contract-first).
Aquestão temaindaalgunsagravantes:adiretoriacolocaumnovorequisito,
queéodesenvolvimentodeumacamadavisualparagerenciamentodestesserviços.
Maslhepareceaindameiocomplicadointeragircomessesserviçosapartirdeuma
camadavisual,enãosoaumaboaideiainteragircomasuaaplicaçãoapartirdomo-
delotradicional,jáquevocêquertercertezadequeseus web servicessãoplenamente
funcionaisdopontodevistadocliente.Aopesquisarsobreisso,vocêsedeparacom
ummodelodedesenvolvimentomaiságildestepontodevista,o REpresentational
State Transfer(REST).
Nodecorrerdospróximoscapítulos,vocêverácomodominarestesassuntos,
demaneiraquevocêserácapazdegerenciardamelhormaneirapossívelcadauma
destasquestões. V a m o semfrente?
4.5 Sumário
Nestecapítulo,vocêconheceuoJetty,um servlet containerextremamenteágil,para
realizardesenvolvimentodeserviçosdemaneiramuitíssimoeficiente.Porém,você
viuque,quandosetratadequestões maiscomplexas,podesermuitoútilconverter
seus web servicesemEJBs.Paraisso,vocêutilizaum application serverque,alémde
ágil,tambémécapazdeendereçarestasquestões: oJBossApplicationServer.
V o c êtambémviucomoSOAéutilizadoparaendereçarquestões deescalabi-
lidadehorizontal,comredirecionamentoderequisições HTTPparamúltiplosa p-
plication servers,ecomoestashabilidadessãoutilizadaspara“esconder”docliente
detalhesdeimplementação,demaneiraqueestenãosejaafetadopormodificações
internasdeinfraestrutura.
86

## Página 103

CasadoCódigo Capítulo4. EmbarcandonoEnterprise-ApplicationServers
Aofinal,vocêpôde perceberquequestões maiscomplexasdedesenvolvimento
aindanãoforamrespondidas:qualamelhormaneiradeintegrarsegurançanasapli-
cações? Comomanteraestabilidadedeumcenáriocom múltiplasaplicações? E
comoresolveraquestão decomunicação diretadeumainterfacevisualcomseus
web services?
Nospróximoscapítulos,vocêverácomoendereçarcadaumadestasquestões.
V o c êpassaráatercontatocomambientesheterogêneos,multiprotocoloeaprenderá
ainterligarestasoperações damaneiramaiseficientepossível.
87

## Página 105

Capítulo5
Desenvolvaaplicações paraaweb
comREST
“Construímosm u i t o sm u r o se poucas pontes”
–SirIsaacNewton
Comanecessidadedeconstrução deumnovosistema,dessavezdeusuários,
vocêdecidereaproveitaroqueviuatéaqui,jáquevocêjásabequeesseéumsistema
queseráutilizadopordiversasoutrasaplicações dentrodaknight.com.Noentanto,
dessavezorequisitomudouumpouco:adiretoriapediuumainterfacedeadminis-
tração web,demaneiraquesejapossívelcriar,atualizaredesabilitarusuáriospela
interfacegráficadosistema.
Contudo,essejásetornouumdesafiodiferentedaquiloaquevocêestáacos-
tumado. SeuscompanheirosespecialistaseminterfacegráficaeUX(U s e rExperi-
ence)falaramquepodesercomplicadodesenvolversistemasdamaneiratradicional
eusando web services. Issoporque,deacordocomaespecificação JavaEE6,jáé

## Página 106

5.1.OqueéREST? CasadoCódigo
possíveldesenvolverinterfacesutilizandoEJBs,damaneiracomovocêviuanterior-
mente,eutilizando JavaServer FacesparasecomunicarcomEJBs.Porém,esta
especificaçãoémaisvoltadaaodesenvolvimentodeinterfacespelosprópriosdesen-
volvedores,evocêgostariadefazeralgocombomapelovisual—algoquesópode
serfeitoporumespecialistaeminterfacescomusuários,nãodesenvolvedores.
V o c êgostaria,então,deapresentaraopessoaldedesignsuasideiasdecomuni-
caçãocom web servicesSOAP;porém,paraqueelesrealizemessacomunicação,eles
precisariamdenovasbibliotecasparacomunicaçãocomosserviços.Aoconversar
comseupessoal,vocêvêqueelesestãoacostumadoscomumabibliotecachamada
jQuery,que,porsuavez,temgrandecapacidadedecomunicação comserviços
REST.
5.1 O que é REST?
RESTéumasiglaquesignifica Representational State Transfer.RESTéummodelo
arquiteturalconcebidoporumdosautoresdoprotocoloHTTP(odoutorRoyFi-
elding),etemcomoplataformajustamenteascapacidadesdoprotocolo,ondese
destacam:
•Diferentes métodos(ou verbos)decomunicação( GET, POST, PUT, DELETE,
HEAD, OPTIONS);
•Utilizaçãode headersHTTP(tantopadronizadosquantocustomizados);
•Definiçãodearquivoscomo recursos(ouseja,cadaumcomseupróprioen-
dereço);
•Utilizaçãode media types.
V o c êpodenotarqueaprópria webébaseadanessesprincípios,equandovocê
navegaporumapágina,automaticamenteestáutilizandoessesconceitos.
Porexemplo,aorealizarumarequisição paraositehttp://www.casadocodigo.
com.br/peloseu browser,naverdadevocêestárealizandoumarequisição parao
recursohttp://www.casadocodigo.com.br/index.html,utilizandoométodoGET.Ao
realizarestarequisição,oconteúdodoarquivo index.htmlserácarregado.Este
arquivoécarregadocomo media type text/html,oqueindicaao browserqueeste
éumarquivodotipoHTML.
90

## Página 107

CasadoCódigo Capítulo5.Desenvolvaaplicações paraawebcomREST
PorserumHTML,o browsersabequedeveprocurarreferênciasporoutrosar-
quivos,comofolhadeestilos, scriptseimagens. Asimagens,especificamente,são
referenciadaspela t ag img,quedáindicações ao browserdeondeestãoessasima-
genspropriamenteditas.Aopuxaressasindicações, o browserfaznovasrequisições,
utilizandoométodo GET.Destavez,asimagenspropriamenteditassãoretornadas
com media typesdeacordocomotipodaimagem(JPEG,GIF,PNG,BMPetc.),que
indicamcomoasrenderizarapropriadamente.
Figura5.1:Interaçãoentreousuário,obrowsereoservidor
Apartirdessesconceitos,épossívelvisualizaromecanismodefuncionamento
deumapossívelaplicaçãobaseadaemREST:apartirdeumarequisiçãoparauma
URLpredefinida,oconteúdoretornadopodeserpré-acordadoentreoclienteeo
servidore,utilizandoindicações presentesnoresultado,oclientepodecarregarda-
dosnovos.
91

## Página 108

5.2.EntendaoHTTP CasadoCódigo
5.2 Entenda o HTTP
ParacompreendercorretamentecomoutilizarREST,noentanto,deve-senotarque
achavedosucessodatécnicaestánospadrões eascapacidadesdoprotocoloHTTP.
Começandopelosmétodosutilizados,notequecadaumpossuiumafinalidadedi-
ferente.Ométodo GET,porexemplo,éutilizadoparacarregarrecursosexistentes.
Quandovocêfazumarequisição GETparahttp://www.casadocodigo.com.br/
index.html,vocêestácarregandoorecursolocalmente.Damesmaforma,suponha
quevocêfaçaumarequisiçãoparahttp://www.knight.com/usuarios.Estarequisição
poderiatetrazercomoresultado,digamos,umXMLcomoseguinteformato:
<usuarios>
<usuario>
<id>1</id>
<nome>Alexandre</nome>
<sobrenome>Saudate</sobrenome>
<login>alesaudate</login>
</usuario>
<usuario>
<id>2</id>
<nome>Adriano</nome>
<sobrenome>Almeida</sobrenome>
<login>adrianoalmeida7</login>
</usuario>
<usuario>
<id>3</id>
<nome>Paulo</nome>
<sobrenome>Silveira</sobrenome>
<login>paulo_caelum</login>
</usuario>
</usuarios>
OformatoHTTPdarequisiçãoseriaassim:
GET /usuarios HTTP/1.1
Host: www.knight.com
Accept: application/xml
Lembre-sedeque,narealidade,muitosoutroscabeçalhossão enviados. Estes
sãoapenasosmaisbásicos.
Arespostadanossarequisiçãoficariaassim:
92

## Página 109

CasadoCódigo Capítulo5.Desenvolvaaplicações paraawebcomREST
HTTP/1.1 200 OK
Date: Sun, 14 Oct 2012 01:21:35 GMT
Last-Modified: Thu, 11 Oct 2012 20:40:32 GMT
Content-Length: 450
Content-Type: application/xml; charset=UTF-8
<usuarios>
<!-- conteúdo -->
</usuarios>
Notetambémqueépossíveldiminuiroconjuntoretornadoatravésdaprópria
requisição.Porexemplo,sequisermosapenasousuáriodeID1,podemosfazeruma
requisição parahttp://www.knight.com/usuarios/1. Destamaneira,onossoresul-
tadoseriaapenasoseguinte:
<usuario>
<id>1</id>
<nome>Alexandre</nome>
<sobrenome>Saudate</sobrenome>
<login>alesaudate</login>
</usuario>
DamesmaformaqueutilizamosométodoGETpararecuperarosrecursosexis-
tentes,podemosutilizarométodo POSTpararealizaracriaçãodenovosrecursos.
Assim,podemosfazeraseguinterequisição:
POST /usuarios HTTP/1.1
Host: www.knight.com
Content-Length: 149
Content-Type: application/xml
<usuario>
<nome>Usuário</nome>
<sobrenome>Novo</sobrenome>
<login>usuario_novo</login>
<senha>aY3BnUicTk23PiinE+qwew==</senha>
</usuario>
Noteque,diferentedométodoGET,o POSTsuportaqueoconteúdosejaenviado
comocorpodarequisição.Issoeliminaváriosproblemas,comolimitesdetamanho
darequisição,codificaçãoetc.
93

## Página 110

5.2.EntendaoHTTP CasadoCódigo
GET e o tamanho d aURL
NãohánenhumtamanhoformalmentedefinidodasURLsrequisi-
tadasatravésdométodo GET.Noentanto,existeumalimitaçãoprática
porpartedeváriosservidorese browsers(queaindanãoédefinidaevaria
entreestes).ÉpreferívelqueURLsmaioresdoque255caracteressejam
evitadas.
Comarequisição POSTenviada,estamosdizendoaoservidorquedesejamos
criarumnovousuario,comosdadospassadoscomoparâmetro.Deformaseme-
lhante,ométodo PUTpodeserutilizado;noentanto,esteépreferencialmenteuti-
lizadopara atualizarrecursos,aoinvésdecriá-los.Destaforma,podemosrealizar
umarequisição paraaURLhttp://www.knight.com/usuarios/1,sinalizandonosso
desejodeatualizarousuáriodeID1.Nossarequisiçãoficariaassim:
PUT /usuarios/1 HTTP/1.1
Host: www.knight.com
Content-Length: 149
Content-Type: application/xml
<usuario>
<nome>Usuário</nome>
<sobrenome>Novo</sobrenome>
<login>usuario_novo</login>
<senha>aY3BnUicTk23PiinE+qwew==</senha>
</usuario>
Destaforma,sefizéssemosoutrarequisição GETparaaURLhttp://www.knight.
com/usuarios,nossoresultadoseriaoseguinte:
<usuarios>
<!-- Este é o usuário que foi atualizado pela requisição PUT -->
<usuario>
<id>1</id>
<nome>Usuário</nome>
<sobrenome>Novo</sobrenome>
<login>usuario_novo</login>
</usuario>
<usuario>
94

## Página 111

CasadoCódigo Capítulo5.Desenvolvaaplicações paraawebcomREST
<id>2</id>
<nome>Adriano</nome>
<sobrenome>Almeida</sobrenome>
<login>adrianoalmeida7</login>
</usuario>
<usuario>
<id>3</id>
<nome>Paulo</nome>
<sobrenome>Silveira</sobrenome>
<login>paulo_caelum</login>
</usuario>
</usuarios>
E,finalmente,podemosutilizarométodo DELETEparaapagarumrecurso:
DELETE /usuarios/1 HTTP/1.1
Host: www.knight.com
Aorealizaressarequisição,apagaríamosousuáriodeID1,epassaríamosater
somenteoseguinteconjuntodeusuários:
<usuarios>
<!-- O usuário de ID 1 foi apagado -->
<usuario>
<id>2</id>
<nome>Adriano</nome>
<sobrenome>Almeida</sobrenome>
<login>adrianoalmeida7</login>
</usuario>
<usuario>
<id>3</id>
<nome>Paulo</nome>
<sobrenome>Silveira</sobrenome>
<login>paulo_caelum</login>
</usuario>
</usuarios>
Qual a rel ação do HTTP com REST?
RESTéfortementeligadoaoHTTP,apontodenão poderserexecutadocom
sucessoemoutrosprotocolos. Eleébaseadoemdiversosprincípiosquefizeram
comqueaprópria webfosseumsucesso.Estesprincípiossão:
95

## Página 112

5.3.URLspararecursos CasadoCódigo
•URLsbemdefinidaspararecursos;
•UtilizaçãodosmétodosHTTPdeacordocomseuspropósitos;
•Utilizaçãode media typesefetiva;
•Utilizaçãode headersHTTPdemaneiraefetiva;
•UtilizaçãodecódigosdestatusHTTP;
•UtilizaçãodeHipermídiacomomotordeestadodaaplicação.
5.3 URLs para recursos
EmREST,cadarecursodeveterumaURLbemdefinida.Porexemplo,oconjunto
dosnossosusuáriospodetermapeadaparasiumaURLhttp://www.knight.com/
usuarios.CasoqueiramosapenasousuáriodeID1,essaURLsetornahttp://www.
knight.com/usuarios/1.
Parâmetrosadicionais,quenão fazempartedadefinição dorecursopropria-
menteditoe/ousejamopcionaispodemserpassadosemformatode q u e r ystring,
ouseja,dados“anexados”àURL.Porexemplo,casoqueiramosutilizarpagina-
ção emnossalistagemdeusuários,podemosrealizarumarequisição parahttp:
//www.knight.com/usuarios?dadoInicial=0&tamanhoPagina=1.
NotequenemsempreéfácildefiniressasURLs.Elasgeralmentepodemseriden-
tificadasquandotemosemmãosumcasoclássicodesistemaparamapeamentode
CRUDs(C r e a t e ,Retrieve, Update, Delete—asfamosasquatrooperações embanco
dedados); noentanto,casosmaiscomplicadossurgemquandoprecisamos,por
exemplo,definiroperações depuralógica.
T o m ecomoexemploumsistemadevalidaçãodeCPF,porexemplo:nãoexiste
umaoperaçãodebancodedados.Nãoexisteumrecursoaserrecuperadodelugar
algum,masapenasumalgoritmoaserexecutadoremotamente.Arequisiçãopara
estealgoritmoéfacilmentedefinidaemSOAP,ouqualquerprotocoloRPC(Remote
Procedure Call—ChamadaaProcedimentoRemoto).Noentanto,emRESTesteé
umproblemamaisamplo.Nestecaso,devemosnosperguntar:qualéorecursoque
estamoschamando?Oquequeremosdele?Quaissãoaspossíveisrespostasqueele
podenosdar?
Nocasodeumsistemadevalidação,portanto,sabemosqueestamosrealizando
umainvocaçãoaumvalidador,desubtipoCPF,equeremosqueeleretorneseodado
éválidoounão.Nestecaso,podemosmapearaURLdesterecursoassim:
96

## Página 113

CasadoCódigo Capítulo5.Desenvolvaaplicações paraawebcomREST
Figura5.2:EstruturadedefiniçãodeURL
Noteque,assumindoestamesmaorientação,épossíveldefinirURLsparaamai-
oriadosproblemas.V o l t a n d oaoproblemadenossosusuários,porexemplo,note
que,setemosumaURL /usuarios/1, /usuariosénosso recurso principale1
éoidentificadordonossorecurso(enãotemosquaisquersubtiposmapeados).No
entanto,sequisermos,porexemplo,apenasoendereçodeumdeterminadousuário,
osensocomumditariaqueteríamosumaURL /usuarios/endereco/1,certo?
Errado.
NotequeasURLsseguemumaestrutura hierárquica,ouseja,oelementose-
guinteobedeceaumrelacionamentocomoelementoanterior.Ouseja,noexemplo
dosendereçosdosusuários,devemosobterprimeiroousuárioemquestãoe,depois,
oendereço.Assimsendo,aURLcorretaseria /usuarios/1/endereco.Noen-
tanto,sequiséssemosobterapenasoendereçodetodososusuários,aíteríamosuma
URL /usuarios/endereco—enderecoobedeceaumaestruturahierárquica
emrelaçãoausuários.
Casoqueiramosadicionaralgumdadoànossarequisição quenão necessa-
riamenteobedeceàhierarquia, ounão éumidentificador,podemosutilizaras
chamadas q u e r ystrings. Elassão muitoutilizadasemsitesdainternetparapas-
sar parâmetrosadicionaisa recursos. Dessa forma, em nosso exemplode va-
lidação do CPF,podemos supor que haja um serviço realmente muito com-
pleto: ele valida tanto o númeroem si, utilizando o algoritmo de módulo 11
(disponívelem http://pt.wikipedia.org/wiki/CPF) , quantoa existênciado CPF
naReceitaFederal. Queremosdaraousuárioapossibilidadedeusarqualquer
97

## Página 114

5.4.MétodosHTTPeusodeMIMEtypes CasadoCódigo
dosalgoritmos, ouambos. Assim, podemos definirumaURLcomoformato
/validador/cpf/(número)?algoritmo=todos:osdadosquevêmdepoisda
interrogaçãocontémosvaloresadicionais,empareschave-valor(ouchave=valor),
separadospor&.
5.4 Métodos HTTP e uso de MIME types
AlémdeURLsbemdefinidas,os web servicesRESTtambémdevemtermétodos
HTTPbemdefinidospararealizarasoperações.
V o l t a n d oaoquestionamentoemrelaçãoaosrecursos:oquequeremosdele?Se
quisermosquealgosejainseridoemnossabasederecursos,utilizamosométodo
POST.Sequisermosrecuperardados,utilizamosométodo GET.Sequisermosatu-
alizar/apagardados,utilizamos PUTou DELETE,respectivamente.
Podemos,alémdisso,utilizar HEADemcasosparticularesdeumarequisição
GETsemdadosaseremretornados.Porexemplo,nonossosistemadevalidação,é
possívelefetuarumarequisição GETparaobterasmensagensrelativasaoresultado
davalidação.Oscódigosde statusHTTPsãofornecidosparadaruma“visãogeral”
doresultado(ouseja,searequisiçãotevesucessoounão).Nocasodeumarequisição
GET,épossívelretornarmensagensdeerromaisdetalhadasnocorpodarequisição
—oque,noentanto,aumentaotráfegoderede. Casooclientenão desejeobter
essasmensagens,ésuficienteutilizar HEAD.T a m b é mpodemosutilizar OPTIONS
paradescobrirmosquaisoperações podemosrealizarcomumadeterminadaURL.
Eporfalaremobtençãoeinserçãoderecursos,oquê,exatamente,querdizer,
inserirumrecursonoservidor?Noteque,aorealizarmosumarequisição GETao
servidor,nãoesperamosreceberarepresentaçãodaquelerecurso,massimarepre-
sentaçãoem formato agnóstico.Porexemplo,emJava,émuitocomumutilizarmos
páginasJSPparacriarmossaídasemformatoHTMLdoservidor.Emoutraspala-
vras,construímosummecanismo(JSP)querealizaráproduçãodeumrecursoem
formatoagnóstico(HTML).Assim,oHTMLproduzidopodeserlidopordiversos
browsersdiferentes.
Damesmaforma,quandoconstruímosserviçosRESTestamosconstruindome-
canismossemelhantes.Porém,nãoestamoslimitadosasimplesmentesolicitarre-
cursosdoservidor.AtravésdosdiferentesmétodosHTTP,podemostantosolicitar
recursosexistentescomocriarnovos;tantoatualizarquantoapagar.
Quantoàrepresentação doquequeremos,issoénegociávelatravésdetipos
MIME.OstiposMIMEsãoomecanismopadrãodenegociaçãodeconteúdonain-
98

## Página 115

CasadoCódigo Capítulo5.Desenvolvaaplicações paraawebcomREST
ternet,esão representadospor stringscontendootipogenérico<barra>umtipo
maisespecializado.Seguetabeladostiposmaiscomuns:
•HTML- text/html;
•XML- text/xmlou application/xml;
•PNG- image/png;
•JPG- image/jpg;
•JSON- application/json;
•PDF- application/pdf.
Aorealizaressanegociaçãodeconteúdoscomoservidor,épossívelterdiversas
representações damesmacoisa. Porexemplo,sefizermosumarequisição dotipo
GETparaumaURL /usuarios/1,podemosobterarepresentaçãodousuáriode
ID1comoXML,JSONouatémesmocomoimagem(oque,nestecaso,retornariao
retratodousuárioemquestão).
Estanegociaçãoéfeitaatravésdedois headersHTTPpadronizados: Accepte
Content-Type. Acceptéenviadodoclienteparaoservidor,informandoqual
tipoMIMEseráaceitocomoresultadodarequisição; Content-Typeéenviadodo
servidorparaoclienteinformandoqualtipoderepresentaçãoestáenviandoparao
cliente.Porexemplo,sequisermosqueoservidornosenviearepresentaçãodeum
usuáriocomoXML,podemosenviaraseguinterequisiçãoHTTP:
GET /usuarios/1 HTTP/1.1
Host: www.knight.com
Accept: application/xml
Noteque,casoqueiramosoretratodousuário,podemosenviarumarequisição
paraamesmaURL,comomesmométodoHTTP;bastaquealteremosotipode
retornoesperado:
GET /usuarios/1 HTTP/1.1
Host: www.knight.com
Accept: image/png
99

## Página 116

5.5.UtilizaçãoefetivadeheadersHTTP CasadoCódigo
Notetambém,quenãoprecisamosrestringiranossarequisiçãoaumtipoespecí-
fico.Porexemplo,sequisermosreceberumarepresentaçãoemformatodeimagem,
massemestarmospresosanenhumtipoespecífico,podemosutilizar*(asterisco),
quefuncionacomoumcuringa. Amesmarequisição poderia,portanto,serfeita
assim:
GET /usuarios/1 HTTP/1.1
Host: www.knight.com
Accept: image/*
Destamaneira,oservidorselecionaotipodeconteúdoenosenviaumaresposta
comoseguinteformato:
HTTP/1.1 200 OK
Date: Sun, 14 Oct 2012 01:21:35 GMT
Content-Length: 18695
Content-Type: image/png
<!-- imagem -->
5.5 Utilização efetiv ade headers HTTP
AlémdeutilizarmétodosHTTPeMIMEtypes,umconceitosemprepresenteem
RESTéousode headers.Os headersHTTPpossuemalgumasmetainformações a
respeitodaquiloqueseestácomunicando/recebendodoservidor,esãoummeca-
nismomuitoútilparasetransmitirinformações quandoarepresentaçãodonosso
recursonãosuportaessasinformações amais.Porexemplo,sequisermosinserira
descriçãodaimagemnacriaçãodamesma,bastaqueenviemosaseguinterequisição
paraoservidor:
POST /usuarios/1 HTTP/1.1
Host: www.knight.com
Content-Length: 18695
Content-Type: image/png
Descricao: Meu retrato no dia 21/10/2012
<!-- imagem -->
Notequeocabeçalhoétotalmentecustomizado,eseuenvio não éobrigatório.
Estaéumainformaçãoimportante:porsetratardeummetadado,vocêdevefazer
opossívelparanãotornarinformações nocabeçalhoobrigatórias.
100

## Página 117

CasadoCódigo Capítulo5.Desenvolvaaplicações paraawebcomREST
Alémdecabeçalhoscustomizados,certos headerssão especialmenteúteis.A
especificação HTTPhabilita,entreoutrascoisas,ousonativodemecanismosde
cache. Destaforma,paraeconomizarousoderede,épossível“negociar”como
servidorapassagemdeinformações.
Issoépossível,dentreoutrasformas,atravésdo header If-Modified-Since.
Noteque,semprequerealizamosumarequisiçãoqualquer,porpadrão oservidor
nosmandaumarequisiçãocontendoadataemqueorecursofoienviado.Estadata
estácontidano header Date.
Apartirdessemomento,oclientepodemanterarepresentaçãodesserecurso,em
conjuntocomadata.Seporventuraoclienteprecisarsolicitarorecursonovamente,
bastaenviareste header,comadataemqueoclienterecebeuaúltimaatualizaçãoda
mensagem.Seorecursonãotiversidoatualizado,oservidorenviaráumcódigode
status304edeixarádeenviarnovamentearepresentaçãodorecurso,indicandoque
oclientepodereutilizaraanterior.
Porexemplo,suponhaaseguinterequisição GET:
GET /usuarios/1 HTTP/1.1
Host: www.knight.com
Accept: image/png
Arespostadestarequisiçãoseráalgocomo:
HTTP/1.1 200 OK
Date: Sun, 14 Oct 2012 01:21:35 GMT
Content-Length: 18695
Content-Type: image/png
<!--imagem-->
Supondoquemantenhamosoresultadodaprimeirarequisiçãoem cache,pode-
mosenviarrequisições subsequentesdaseguinteforma:
GET /usuarios/1 HTTP/1.1
Host: www.knight.com
If-Modified-Since: Sun, 14 Oct 2012 01:21:35 GMT
Accept: image/png
Destamaneira,podemosrecebertantoumarespostaidênticaàprimeira,quanto
umarespostaassim:
101

## Página 118

5.6. Utilizaçãodecódigosdestatus CasadoCódigo
HTTP/1.1 304 Not Modified
Date: Sun, 14 Oct 2012 01:23:22 GMT
Notequeumarespostacomstatus304,diferentementedeumacomstatus200,
nãotrazosresultadosdarequisiçãonocorpo,economizandoosrecursosderede.
5.6 Utilização de códigos de status
Noteque,parautilização efetivadenossosserviçosREST,podemos(edevemos)
utilizaroscódigosdestatusHTTPpararealizaracomunicaçãocomnossosserviços.
Issofacilitaoreconhecimentodoestadodarequisição: setevesucessoounão,se
tevefalhaounão,esetiverocorridoalgumafalha,qualfoi.Porexemplo,nonosso
mecanismodeusuários,vocêjásabeque,quandosolicitamosalistagemdeusuários,
ocódigodestatusé200e,quandoé304,significaquenadamudoudesdeaúltima
vezemquefizemosasolicitação. Noentanto,podeserútil,nacriaçãodeumnovo
usuário,utilizarumcódigodestatusdiferente:201(Created).Estecódigodestatus
indicaapresençadeum header Location,quetrazaURIondeonovorecursoestá
hospedado.Seenviarmosarequisiçãocomcamposrequeridosfaltando,épossível
enviar,narespostaparaocliente,ocódigo400(BadRequest).
Emgeral,oscódigosdestatusseguemaseguinteordem:osquecomeçamcom
1sãoinformativos(nãosepreocupecomestes,geralmentenãosãoutilizados).Os
quecomeçamcom2indicamsucessodaoperação, comvariações. Porexemplo,
200éumarespostadesucessogenérica.201significaqueorecursofoicriado,e
estápresenteemumadeterminadaURL,eassimpordiante.Osquecomeçamcom
3indicamqueoclientedevetomaralgumaespéciedeação. V o c êjáviuocampo
304,porexemplo,queindicaqueorecursonãofoimodificadoequeoclientedeve
reutilizaroconteúdoquejátinha.Oscódigosquecomeçamcom4indicamalguma
espéciedefalhanarequisiçãoeoscódigosquecomeçamcom5indicamfalhasno
processamentodarequisição.
Oscódigosmaisutilizadossão:
•200 OK
•201 Created
•202 Accepted
•204 No Content
102

## Página 119

CasadoCódigo Capítulo5.Desenvolvaaplicações paraawebcomREST
•304 Not Modified
•400 Bad Request
•401 Unauthorized
•403 Forbidden
•404 Not Found
•405 Method Not Allowed
•409 Conflict
•415 Unsupported Media Type
•500 Internal Server Error
Naprática,oscódigosquesãoencaradoscomo“sucesso”sãoosdasfamílias2xx
e3xx.Comovocêjáviuantes,umcódigo200OKéumcódigogenéricoqueindica
quearequisiçãofoiprocessadacomsucesso.Jáo201Createdéutilizadocomores-
postapararequisições POST.Indicaquearequisiçãofoiprocessadacomsucessoe
orecursoestápresenteemumaURL(apresentadano header Location).
Ostatus202Acceptedindicaquearequisiçãofoiaceita;noentanto,elanãoserá
processadaimediatamente.Écomumenteutilizadoemserviçosassíncronos,sendo
queaURLondeseconfereoresultadopodeestarpresenteno header Location.
Alémdisso,ostatus202poderetornarconteúdonocorpodaresposta,contendoao
menosotempoestimadodeprocessamento(segundo[10]).
Jáostatus204NoContentécomumenteutilizadocomoresultadoderequisi-
ções POST, PUTou DELETE,indicandoquearequisiçãofoiprocessadamasnão
hánenhumcorpodarequisiçãoaserpreenchido.E,finalmente,ocódigo304Not
Modifiedéusadoparaindicarqueorecursonãofoialterado.
Oscódigosdeerrosãoosdasfamílias4xxe5xx.Ocódigo400BadRequesté
umcódigogenéricoparaindicaralgumproblemanoconteúdodarequisição.Éco-
mumenteutilizadoquandoalgumcamponãofoipreenchido,oupreenchidoincor-
retamente.Ocódigo401Unauthorizedsignificaqueoclientenãoestáautorizadoa
visualizarumdeterminadorecurso(tendofornecidocredenciaisquenãodãoacesso
àquelerecursooumesmonãotendofornecidocredencialalguma).
Ocódigo403Forbiddenéparecidocom401,comadiferençadequeéutili-
zadoquandooservidorreconhecequeorecursosolicitadoexiste. Ocódigo404
103

## Página 120

5.6. Utilizaçãodecódigosdestatus CasadoCódigo
NotFound,porsuavez,indicaqueorecursonãoexiste.Ocódigo405MethodNot
AllowedindicaqueométodoHTTPutilizadonãoésuportado.Porexemplo,supo-
nhaqueumdeterminadorecursonãopodeserapagado,depoisdecriado;mesmo
assim,oclienteenviaumarequisição DELETE.Assim,oservidorpoderesponder
comostatus405.Ostatus409Conflict,porsuavez,indicaqueháumconflitoentre
recursos.Paragarantirqueosclientesestejamtrabalhandocomaversãomaisatual
deumdeterminadorecurso,oservidorpodeutilizarumcampodeversão. Assim,
considereoseguintecenário:
Figura5.3:Solicitaçãoderecursocomversionamento
Noteque, apartirdessemomento,oclienteAtemumacópia detrabalho
dousuário1. SeumclienteBfizeramesmarequisição, eletambémobteráuma
cópia desseusuário,comamesmaversão (notequeesteéopadrão deprojeto
Optimistic Offline Lock,comodescritoporMartinFowleremseulivro P a t-
terns o fEnterprise Application Architecture[8]).
SeoclienteBfizerumaatualização,aversãodoservidorseráautomaticamente
incrementadapara2.Noentanto,seoclienteAfizerumaalteração,eledeverádizer
104

## Página 121

CasadoCódigo Capítulo5.Desenvolvaaplicações paraawebcomREST
aoservidorqueaversãoquepossuié1(queestá,portanto,desatualizada).Estanova
requisiçãoserárespondidacomumcódigo409Conflict,indicandoaoclienteAque
estedeveobterumaversãomaisatualizada(nestecaso)antesderealizarumaedição.
Figura5.4:Controledeversões comREST
Aindanafamília4xx,ocódigo415UnsupportedMediaT y p eéenviadoquando
oclientemandaumarequisição comformatonãoreconhecidopeloservidor. Por
exemplo,supondoqueoclienteenvieumarequisiçãoemformatoJSON(JavaScript
Object Notation),masoservidornãosuporteesteformato,estecódigodestatusé
enviadopeloservidor.
Finalmente,ocódigodestatus500InternalServerErrorsignificaquealguma
condiçãoinesperada,porpartedoservidor,ocorreu.Estecódigodestatuséenviado
quandoalgumaexceção ocorreuinternamentenoservidor,eelenão soubeoque
fazerparaserecuperar.Noentanto,arequisiçãopodeserreenviadapelocliente—
lembre-se,porém,deevitarreenviararequisiçãomuitasvezes,paraqueoservidor
nãoseja“derrubado”porfaltaderecursos.
105

## Página 122

5.7.Utilizaçãodehipermídiacomomotordeestadodaaplicação CasadoCódigo
5.7 Utilização de hipermídiaco mo motor de estado
d aaplicação
U mrecursomuitosubestimado,porémprevistonadissertaçãodeRoyFielding[6],
éousodehipermídiacomomotordeestadodaaplicação(conhecidonasiglaem
inglêscomoHATEOAS- Hypermedia A sThe Engine Of Application State).Consiste
deumatécnicajámuitoconhecidadetodosnós,nousodepáginasweb.
Quandosolicitamosumapáginaweb,emgeralobtemos,emconjuntocomo
textopropriamentedito,inúmerosrecursosadicionais:folhasdeestilo, scripts,ima-
gensetc.Porém,quandosolicitamosapágina,geralmenteestesrecursosadicionais
nãoestãopresentesnoHTML,masapenasasreferênciasaestes.Quandoo browser
solicitaapágina,omesmofazumavarreduranoHTMLparadescobrirondeestão
osrecursosadicionaisqueestãopresentesnesta.Assim,obtendoasreferências,ele
temcondições defazernovasrequisições paracarregá-los.
Damesmamaneira,RoyFieldingpreviuqueseriaexcelenteparaasaplicaçõesse,
aoinvésdemanterasURLsparanovosrecursosnaprópriaaplicação,seriamaisin-
teressantesecadaretornoderecursotrouxesseconsigoURLsparanovasoperações.
ParadescobriroquefazercomcadaURL,bastaqueaaplicaçãoutilizeosmétodos
jápadronizados: GETparaobterorecurso, POSTparacriar,eassimpordiante.
Porexemplo,quandorequisitamosalistagemdeusuáriosdosistema,oideal
seriaqueobtivéssemosalgocomooseguinte:
<usuarios xmlns:links="http://knight.com/links">
<usuario>
<id>1</id>
<nome>Alexandre</nome>
<login>asaudate</login>
<links:link href="/usuarios/1" rel="self" />
</usuario>
<!-- Outros 19 usuários -->
<links:link href="/usuarios" rel="self" />
<links:link href="/usuarios?offset=20&limit=20" rel="nextPage" />
<links:link href="/usuarios?offset=40&limit=20" rel="lastPage" />
</usuarios>
Noteapresençadoselementos link. Elescontêmtantoareferênciaparao
quesepodefazercomorecursoemquestãoquantoarelaçãodelescomorecurso.
Porexemplo,oselementosquecontêm rel="self"referem-seaoprópriore-
curso. Repare,noentanto,napresençadoselementoscom rel="nextPage"e
106

## Página 123

CasadoCódigo Capítulo5.Desenvolvaaplicações paraawebcomREST
rel="lastPage".Elesindicamqueprovavelmenteesserecursoépaginado,eeles
contêmoslinkstantodapróximapáginaquantodaúltima.
Noteque,destaforma,aaplicaçãonãoprecisaconhecerquaissãooslinkspara
aspróximaspáginas,masapenasconheceroslinkscomasrelações nextPagee
lastPage. Issofazcomqueoclientefiquemaisdesacopladodoservidor,jáque
nãoénecessárioatualizarocódigocasoalgumdesteslinksmude.
Co m o definiros links
Paradefinirseus links, recomendoutilizaralgosimilar aos links
HTML.Não háumadefinição formalaesserespeito,emboraexista
umesforçodaW3Cnestesentido,chamado XML Linking Language
(XLink), que pode ser conferido em http://www.w3.org/TR/xlink/.
Particularmente,euconsideroestemodelopoucointuitivo,eprefiroal-
ternativas,comoojámencionadomodeloutilizadoemHTMLparacar-
regarfolhasdeestilo.
5.8 Co m o desenvolver serviços REST
Atualmente,osserviçosRESTestãopadronizadossobumaúnicaespecificação,em
Java,chamadaJAX-RS.Estaespecificaçãofuncionanomesmomoldequeoutrases-
pecificações, ouseja,provêumconjuntodeanotações/classes edeixaacargode
váriosfr a mewo r ksofuncionamentopropriamentedito. Dentreosprincipais fr a-
meworks,possodestacar:
•Jersey(queéaimplementaçãodereferência);
•RESTEasy;
•A p a c h eCXF;
Alémdisso,existetambémumaimplementaçãobrasileiradeREST,queéofra-
mework Restfulie(criadoporGuilhermeSilveira).
Nonossocaso,quandodesenvolvemosutilizandooJBossAS,normalmenteuti-
lizamosoRESTEasy,quejáestáinclusonadistribuiçãopadrão.
Emgeral,todoserviçoJAX-RSprecisaconter:
107

## Página 124

5.8.ComodesenvolverserviçosREST CasadoCódigo
•U m aoumaisanotações @Path(quepodeserincluídatantoemclassesquanto
eminterfacesemétodos);
•U m aoumaisanotações @Consumes(quesegueamesmaregrade @Path);
•U mnúmeroqualquerdeanotações @Produces;
•DefiniçãodosmétodosHTTPaseremutilizados,atravésdasanotações @GET,
@POST, @PUT, @DELETE, @HEADou @OPTIONS.
Porexemplo,paradefinirmosummétodoparalistagemdeusuáriosquesempre
produzacódigocomotipoMIME application/xml,podemosutilizaroseguinte
código:
import javax.ws.rs.*;
import javax.ws.rs.core.*;
// Outros imports
@Path("/usuarios")
@Produces(MediaType.APPLICATION_XML)
@Consumes(MediaType.APPLICATION_XML)
public class UsuariosService {
@PersistenceContext
private EntityManager em;
@GET
public Usuarios listarUsuarios() {
return new Usuarios(em.createQuery("select u from Usuario u")
.getResultList());
}
}
Notequeumaclasseadicional, Usuarios,foicriadaparaquepossamosretor-
naracoleçãodeusuários.Ocódigodelaéoseguinte:
package com.knight.usuarios.modelos;
//Imports omitidos
108

## Página 125

CasadoCódigo Capítulo5.Desenvolvaaplicações paraawebcomREST
@XmlRootElement
@XmlAccessorType(XmlAccessType.FIELD)
public class Usuarios {
@XmlElement(
name = "usuario")
private Collection<Usuario> usuarios;
public Usuarios() {
}
public Usuarios(Collection<Usuario> usuarios) {
this.usuarios = usuarios;
}
// getter e setter para o campo usuarios
}
Além disso, é necessárioincluir a seguinte informação no arquivo
WEB-INF/web.xml:
<web-app>
<servlet-mapping>
<servlet-name>javax.ws.rs.core.Application</servlet-name>
<url-pattern>/services/*</url-pattern>
</servlet-mapping>
</web-app>
Aoexecutaressecódigo,bastaapontaro browserparaaURL <caminho da
aplicação>/services/usuarioseconferiroresultado:
<usuarios>
<usuario>
<id>1</id>
<nome>Alexandre</nome>
<login>admin</login>
<senha>admin</senha>
</usuario>
</usuarios>
T a m b é mqueremosquehajaumaURLparabuscadeumusuárioespecífico
(comoformato <caminho da aplicação>/services/usuarios/<id do
109

## Página 126

5.8.ComodesenvolverserviçosREST CasadoCódigo
usuario>),então,podemosincluirumaanotação @Pathadicional. Essaanota-
çãoadicionaliráconteraespecificaçãodoquefazercomoIDdousuário.Paraque
possamosreceberesseID,anotamosoparâmetrocom @PathParam:
@Path("/usuarios")
@Produces(MediaType.APPLICATION_XML)
@Consumes(MediaType.APPLICATION_XML)
public class UsuariosService {
@PersistenceContext
private EntityManager em;
//Método de busca de todos os usuários
@GET
@Path("/{id}")
public Usuario find(@PathParam("id") Long id) {
return em.find(Usuario.class, id);
}
}
A classe Response
Noteque,comotemosvárioscódigosdestatusHTTPdiferentes,precisamos
deummecanismoparaquepossamoscontrolarotráfegoHTTP.Aespecificação
JAX-RSforneceaclasse javax.ws.rs.core.Responseparaisso.Porexemplo,
ocódigopararecuperarumusuáriopodeserreescritoassim:
@GET
@Path("/{id}")
public Response find(@PathParam("id") Long id) {
Usuario usuario = em.find(Usuario.class, id);
if (usuario != null) {
return Response.ok(usuario).build();
}
return Response.status(
javax.ws.rs.core.Response.Status.NOT_FOUND
).build();
}
110

## Página 127

CasadoCódigo Capítulo5.Desenvolvaaplicações paraawebcomREST
Nesta situação, caso o usuário não seja encontrado, o servi-
dor retorna o código de status 404 (representado pela constante
javax.ws.rs.core.Response.Status.NOT_FOUND). Caso ele seja en-
contrado, utilizamos o método ok() da classe Response, passando como
parâmetroousuárioencontrado. Ousodestemétodoserátraduzidocomouma
respostadestatus200OK,contendoousuárioencontradonocorpodaresposta.
C o n s t r ução de URI
Nocasodométododecriação denovosusuários,podemosutilizaraclasse
Responsedamesmamaneiracomonosmétodosdelocalização deusuários.No
entanto,comoditonaseção 5.6,omelhorcódigodestatusaserutilizadonares-
postadecriaçãoderecursoséo201Created,queéarespostapadrãoparainvocação
atravésdométodoHTTP POST.Lembre-sedequeestecódigodevetrazero header
Location,quecontémaaURIondeorecursorecém-criadopodeserencontrado.
Ouseja,precisamosdeummecanismoquefaçaaconstruçãodaURIparanós.
Qu a la diferença entre URL e URI?
SegundoaRFC3986(http://www.ietf.org/rfc/rfc3986.txt),umaURI
podeserclassificadacomoumlocalizador,umnome,ouambos.Jáuma
URLéumsubconjuntodasURIsque,alémdeidentificarumrecurso,
provêmeiosparalocalizarorecursoatravésdadescriçãodomecanismo
deacessoprimário.Emgeral,podemosidentificarseumdeterminado
caminhoéumaURLseamesmacontiveroprotocoloutilizadopara
acesso.
AespecificaçãoJAX-RSdáacessoaalgumasfuncionalidadesdessetipoatravés
dainterface javax.ws.rs.core.UriInfo.Estainterfaceégerenciadapelapró-
pria enginedoJAX-RS,enãoprecisamosinstanciá-la;bastaapenasinjetá-lanonosso
serviço,utilizandoaanotação javax.ws.rs.core.Context.Podemosutilizar
essemecanismoparainjetarumainstânciade UriInfonaprópriaclassedeserviço,
comoumatributo,oucomoparâmetrodeummétodo.
Dentreosváriosmétodosutilitáriosfornecidospelainterface UriInfo,está
getAbsolutePathBuilder. EstemétodotrazaURLquefoiinvocada(exceto
q u e r ystrings)parachegaraométodoatualemum builder;ouseja,épossíveladicio-
nardadosàURIinvocada.Destaforma,serealizarmosumarequisição POSTpara
111

## Página 128

5.8.ComodesenvolverserviçosREST CasadoCódigo
acriaçãodeumrecurso,podemosutilizaressesmétodosparaaconstruçãodaURI
ondeoclientepodebuscarodado.
Combasenessasinformações, oseguintecódigoéescrito:
@POST
public Response create(@Context UriInfo uriInfo, Usuario usuario) {
em.persist(usuario);
// Constrói a URL onde o recurso estará disponível
UriBuilder uriBuilder = uriInfo.getAbsolutePathBuilder();
URI location = uriBuilder.path("/{id}").build(usuario.getId());
return Response.created(location).build();
}
Comopodeservisto,anotaçãoutilizadaparaconstruiraURIéidênticaànota-
çãoutilizadaparadescreverométodoquebuscaumúnicousuário.Ousuáriopas-
sadonocorpodarequisiçãoépersistidoe,casoapersistênciatenhasucesso,oID
geradoéutilizadoparacomporaURIdorecurso.Nasequência,ométodocreated
daclasse Responseéutilizadopararetornarumaresposta201Createdparaocli-
ente(eoparâmetroparaestemétodoseráutilizadono header Location).
Recebendo e enviando headers
Para enviar e receber headers HTTP, a anotação
@javax.ws.rs.HeaderParam pode ser utilizada. Ela éusada em assinatu-
rasdemétodos,erecebecomoparâmetroonomedocabeçalhoemquestão.
Vejamos uma aplicação prática: você se lembra do cabeçalho
If-Modified-Since, apresentadona seção 5.5? Ele éutilizado para enviar
umadataparaoservidor,dizendoaestequeoclientesó desejaoresultadoda
requisição seorecursotiversidomodificadodesdeentão. Nessecaso,podemos
utilizar esta anotação em nossos métodosde busca para interagir diretamente
comestecabeçalho,eentão,alteramosnossométododebuscaparateraseguinte
assinatura:
@GET
@Path("/{id}")
public Response find(@PathParam("id") Long id,
@HeaderParam("If-Modified-Since") Date modifiedSince)
Notequeoretornodométodofoialteradoparautilizaraclasse Response,
paraquepossamosmanipularocódigodestatusutilizadonarespostaHTTP.Além
112

## Página 129

CasadoCódigo Capítulo5.Desenvolvaaplicações paraawebcomREST
disso,estamosexplicitamentedeclarandoocabeçalho If-Modified-Sincecomo
java.util.Date,paraquepossamosinteragircomessadata.
Paraqueissosejaefetivo,precisamos,noentanto,alterarnossaclasse Usuario
paraconteradatadeatualizaçãodorecurso.Reparequeestaéumainformaçãoque
podeseraproveitadaportodasasnossasclassesdemodelo,então,podemosmodelar
essainformaçãonumasuperclasse, EntidadeModelo:
@MappedSuperclass
public abstract class EntidadeModelo {
@Temporal(TemporalType.TIMESTAMP)
private Date dataAtualizacao;
@XmlTransient
public Date getDataAtualizacao() {
return dataAtualizacao;
}
@PreUpdate
@PrePersist
protected void ajustarDataAtualizacao() {
this.dataAtualizacao = new Date();
}
}
Percebaqueestamosusandoalgumasanotações básicasdaJPA,paratornaras
informações persistentes.ParasabermaissobreJPA,recomendoolivrodaCasado
Códigosobreoassunto.
Aclasseestádevidamenteanotadacom @MappedSuperclass,indicandopara
oJPAqueosdadoscontidosneladevemserpersistidos.Alémdisso,notequeo getter
docampo dataAtualizacaoestámarcadocom @XmlTransient.Issoporque
este getterserálidopela enginedoJAXB,aindaqueestaclasse,ousuassubclasses,
estejamanotadasparamapearoscamposdiretamente.
Ainda,noteométodo ajustarDataAtualizacao:porconterasanotações
@PreUpdatee @PrePersist,estemétodoseráinvocadosemprequeumadesuas
subclassessejaatualizada(comportamentoajustadopor @PreUpdate)oucriada
nobancodedados(comportamentoajustadopor @PrePersist).
Tendoacessoàdatadeatualizaçãodousuário,podemoscompletaronossomé-
todo:
113

## Página 130

5.9.Mapeamentoavançado:tratandoimagens CasadoCódigo
@GET
@Path("/{id}")
public Response find(@PathParam("id") Long id,
@HeaderParam("If-Modified-Since") Date modifiedSince) {
Usuario usuario = em.find(Usuario.class, id);
if (usuario != null) {
if (modifiedSince == null
|| (modifiedSince != null && usuario.getDataAtualizacao()
.after(modifiedSince))) {
return Response.ok(usuario).build();
}
return Response.notModified().build();
}
return Response.status(Status.NOT_FOUND).build();
}
Reparequeénecessáriotestarseoparâmetrofoipassado;senãotiversido,o
valorde modifiedSinceseránull.
5.9 Mapeamento av ançado : tratando imagens
A t éaqui,vocêviucomoutilizarasanotações JAX-RSparafazerobásico,ouseja,
manipulação básicade headersvindosdocliente,métodosHTTPestatusderes-
posta,alémdetervistoobásicodamanipulaçãodetiposMIME.Noentanto,ese
osusuáriosdosistemativeremretratos?Comorealizaramanipulaçãocorretadesse
tipodeinformação,nomodeloREST?
V a m o scomeçarmodelandoaclassequecontémaimagem.Fazemosissonuma
classeseparada,paraquepossamosarmazenar,juntodaimagem,umadescriçãoda
mesma:
@Entity
public class Imagem extends EntidadeModelo {
@Id
@GeneratedValue(
strategy = GenerationType.IDENTITY)
private Long id;
114

## Página 131

CasadoCódigo Capítulo5.Desenvolvaaplicações paraawebcomREST
@Lob
private byte[] dados;
private String tipo;
private String descricao;
//getters e setters
}
Notequenãoénecessáriocolocaranotações JAXBnessaclasse,jáqueelanão
serátrafegadacomoXMLoucomoqualquerlinguagemdemarcação.Aoinvésdisso,
colocamosumcampo tipoparaarmazenarotipoMIMEdessaimagem,bemcomo
umcampo dados,queiráconteraimagempropriamentedita.Essecampoprecisa
conteraanotação @Lobparaindicarà engineJPAqueestecampodevesermapeado
paraumBLOB,ouseja,umcampodearmazenamentodedadosbinários.
Feitaamodelagemdaclassedeimagens,inserimosomapeamentodestapara
usuários.Comoestaéumaclassequetemumrelacionamentodiretocomapenas
umainstânciadeumusuário,ecadausuáriotemapenasumretrato,esteéchamado
derelacionamentoum-para-um.Estetipoderelacionamentoécriadoutilizandoa
anotação @OneToOne.Assim,mapeamosoretratodaseguintemaneira:
@OneToOne(
cascade = { CascadeType.ALL }, orphanRemoval = true)
@XmlTransient
private Imagem imagem;
Notequeosatributos cascadee orphanRemovalforaminseridosparagaran-
tirqueasoperações sobreumusuáriosejamrefletidasparaaimagemeparagarantir
quenão hajanenhumaimagem“ ó r f ã ” ,ouseja,semrelacionamentocomnenhum
usuário.Alémdisso,aanotação @XmlTransientfoiinseridaparaqueoJAXBnão
interpreteestecampocomopartedousuário(novamente,lembre-sequeaimagem
nãoserátrafegadacomoXML,masemseuformatopuro).
Mapeamento com JP A
SequiserconhecermaisafundoomapeamentocomJPA,sugirove-
rificarolivro“Aplicações JavaparaawebcomJSFeJPA”,disponívelem
http://www.casadocodigo.com.br/products/livro-jsf-jpa.
115

## Página 132

5.9.Mapeamentoavançado:tratandoimagens CasadoCódigo
Feitoestemapeamento,precisamosescreverocódigoquefaráabusca/criação
deimagens.Nossosrequisitossão:
•Fazercomqueoclientetenhaapercepçãodequeaimagembináriaeosdados
trafegadoscomoXMLpertençamàmesmaentidade;
•T r a t a rimagensdeumamaneiragenérica,ouseja,não fazerdistinção entre
PNG,JPG,GIFououtrosformatos;
•Fazercomqueoclientetenhaapossibilidadedecachearoresultadodebusca;
•Poderinseriradescriçãodaimagem,bemcomoretornarestadescriçãoem
conjuntocomaimagemquandosolicitada.
Perceba que, quando criamos o serviço de usuários,utilizamos as anota-
ções @Consumes e @Produces diretamentenadeclaração declasse,paraas-
sinalarquegostaríamosqueotipoMIMEpadrão paratratarosrecursosfosse
application/xml. Noentanto,gostaríamosqueessaimagemtivesseomesmo
endereçodoserviçodeusuários,apenasalternandoosmodosderespostaquando
oclientesolicitaressamudança.Destaforma,criamosnossoserviçodebuscapara
sinalizarqueeleproduzimagens,utilizandooMIMEtype image/*(ondeo“*”é
umcuringa,ouseja,nãoespecificaqualotipodeimagem):
@Produces("image/*")
@GET
public Response recuperarImagem()
Assim,essemétodoseráselecionadopelocliente,quandoesteenviaro header
Acceptcomvalor image/*. Issoquerdizer,dopontodevistadocliente,que
eleaceitacomorespostadoserviço,qualquertipodeimagem(diferentementedo
padrãodesteserviço, application/xml).
Restafazercomqueoclienteobtenhaaimagemdeumclienteespecífico.Para
isso,utilizamosnovamenteasanotações @Pathe @PathParam:
@GET
@Path("/{id}")
@Produces("image/*")
public Response recuperarImagem(@PathParam("id") Long id)
Porúltimo,acrescentamoso header If-Modified-Since,paraquepossamos
acrescentarapossibilidadedoclientefazer cachedaimagemretornada:
116

## Página 133

CasadoCódigo Capítulo5.Desenvolvaaplicações paraawebcomREST
@GET
@Path("/{id}")
@Produces("image/*")
public Response recuperarImagem(@PathParam("id") Long id,
@HeaderParam("If-Modified-Since") Date modifiedSince)
Agora,precisamoscodificarocorpodarequisição.Lembre-sedequeoIDper-
tenceaousuário(enão àprópriaimagem),bemcomodevemosincluirocampo
descricaonoretornodabusca. Paraisso,utilizamosométodo header()da
classe Response,oquefarácomqueadescrição daimagemsejaincluídacomo
headerHTTPnarespostadarequisição.
Alémdisso,nométodook(),passamoscomoparâmetrotantoo a r r a yde b y t e s
dequeaimageméformadacomootipo.Otipopodeserincluídocomoumsegundo
parâmetroparaestemétodo;assim,ocódigocompletodométododebuscapela
imagemfica:
@GET
@Path("/{id}")
@Produces("image/*")
public Response recuperarImagem(@PathParam("id") Long id,
@HeaderParam("If-Modified-Since") Date modifiedSince) {
Usuario usuario = em.find(Usuario.class, id);
if (usuario == null) {
return Response.status(Status.NOT_FOUND).build();
}
Imagem imagem = usuario.getImagem();
if (modifiedSince != null && imagem.getDataAtualizacao()
.before(modifiedSince)) {
return Response.notModified().build();
}
return Response.ok(imagem.getDados(), imagem.getTipo())
.header("Descricao", imagem.getDescricao()).build();
}
Agora,restacriarométododecriação/atualizaçãodaimagem.Comoumusuá-
riojáprecisaexistirparaquepossamosatribuirumretratoaele,não fazsentido
atribuirissoaummétodo POST;émaisadequadoparaummétodo PUT.Além
disso,nossométodoprecisaestarcientedequesóconsomerequisições deimagens.
Assim,nóscriamosométodoeoanotamoscom @Consumes,daseguinteforma:
117

## Página 134

5.9.Mapeamentoavançado:tratandoimagens CasadoCódigo
@PUT
@Path("/{id}")
@Consumes("image/*")
public Response adicionarImagem(@PathParam("id") Long idUsuario)
Noteque,comoimagenssãodetipobinário,declaramosoconteúdocomoum
a r r a yde b y t e s.Comoprecisamostambémdadescrição,podemosincluiradefinição
dessecamponaassinaturadométodo.Dessaforma,aassinaturadonossométodo
ficaassim:
@PUT
@Path("/{id}")
@Consumes("image/*")
public Response adicionarImagem(
@HeaderParam("Descricao") String descricao,
@PathParam("id") Long idUsuario,
byte[] dadosImagem)
Finalmente,devemosteracessoaotipodeconteúdoenviadoparaquepossa-
mosincluirnainstânciade Imagem(eutilizarcomoretornodométododebusca).
Poderíamosmapearo header Content-Typedamesmamaneiracomofizemos
anteriormente,masporfinsdidáticos,faremosdeoutrojeito.
Aclasse HttpServletRequest,definidapelaAPIde ServletsJava,possuio
método getContentType,queéutilizadopararecuperaresseconteúdo.Iremos
acessaressemétodo,injetandoainstânciacorretade HttpServletRequestno
nossométodoatravésdaanotação @Context.Dessemodo,aassinaturacompleta
dométodoficaassim:
@PUT
@Path("/{id}")
@Consumes("image/*")
public Response adicionarImagem(
@HeaderParam(CAMPO_DESCRICAO_IMAGEM) String descricao,
@PathParam("id") Long idUsuario,
@Context HttpServletRequest httpServletRequest,
byte[] dadosImagem)
Restaapenasacodificaçãodestemétodo.Bastaapenasquefaçamosabuscado
usuário(retornando404NotFoundcasoelenãoexista)eaatribuiçãodaimagem
aele.Nasequência,precisamosatualizarousuárionobancodedados,utilizando
118

## Página 135

CasadoCódigo Capítulo5.Desenvolvaaplicações paraawebcomREST
ométodo mergedonosso EntityManager.Destaforma,ocódigocompletodo
métodoficaassim:
@PUT
@Path("/{id}")
@Consumes("image/*")
public Response adicionarImagem(
@HeaderParam(CAMPO_DESCRICAO_IMAGEM) String descricao,
@PathParam("id") Long idUsuario,
@Context HttpServletRequest httpServletRequest,
byte[] dadosImagem) {
Usuario usuario = em.find(Usuario.class, idUsuario);
if (usuario == null) {
return Response.status(Status.NOT_FOUND).build();
}
Imagem imagem = new Imagem();
imagem.setDados(dadosImagem);
imagem.setDescricao(descricao);
imagem.setTipo(httpServletRequest.getContentType());
usuario.setImagem(imagem);
em.merge(usuario);
return Response.noContent().build();
}
5.10 Incluindo links HATEOAS
Oúltimopassoparaquepossamosdeixarnossoserviçointeiramentedeacordocom
opropostoporRoyFielding[6]éainclusãodelinksemnossasentidades.Esseslinks
devemlevaraoutrosrecursos,quedealgumaformaestãorelacionadosaorecurso
atual.Porexemplo,seincluirmospaginaçãoemnossosrecursos,podemosmodelar
aURLdepaginaçãodaseguinteforma:
/usuarios* *?inicio=0&tamanhoPagina=5* *
Comoexplicadoanteriormente,essesparâmetrossãoopcionais(podemassumir
valores-padrão).SeincluídosnaURL,elesvãomodificaramaneiracomoorecurso
seapresenta(nocasodapaginação,porexemplo,otamanhodaentidade usuarios
serálimitadoacertotamanho,alémdecontervaloresdiferentesdepáginaparapá-
gina).Assim,oresultadodanossarequisiçãocompaginaçãopoderáconteroslinks
paraaprimeirapágina,últimapágina,páginaanterior,posterior,eassimpordiante.
Parautilizarvalores-padrãoemnossasrequisições, podemosutilizaraanotação
119

## Página 136

5.10.IncluindolinksHATEOAS CasadoCódigo
javax.ws.rs.DefaultValue.Estaanotaçãopodeserutilizadaparadefinirva-
loresdetiposprimitivos,classesbemconhecidasdaAPI(como String,classes
w r a p p e r, BigDecimal,eassimpordiante)eatéenums. IssofazcomqueaAPI
fiquelimpa,semnecessidadedeutilizar i f ’sparatestarseovalorfoipassadoounão.
Porexemplo,paraquepossamosfazerapaginaçãodanossalistagemdeusuários,
podemosmodificaraassinaturadonossométododelistagemparaficarassim:
public Response listarUsuarios(
@HeaderParam("If-Modified-Since") Date date,
@QueryParam("inicio") @DefaultValue("0") Integer inicio,
@QueryParam("tamanhoPagina") @DefaultValue("20")
Integer tamanhoPagina)
Dessamaneira,seosparâmetros inicioe tamanhoPaginanãoforeminfor-
madospelocliente,eleiráassumirosvalores0e20,respectivamente.
Considerando cinco usuárioscadastrados no banco de dados, e as devi-
das modificações no código para incluir a paginação, uma requisição para
/usuarios?inicio=0&tamanhoPagina=2trariaosseguintesresultados:
<usuarios>
<usuario>
<id>1</id>
<nome>Alexandre</nome>
<login>admin</login>
<senha>admin</senha>
</usuario>
<usuario>
<id>2</id>
<nome>Rafael</nome>
<login>rafael</login>
<senha>rafael</senha>
</usuario>
</usuarios>
Noteque,dessaforma,nãotemoscomosaberseexisteumapróximapáginaou
qualéaúltimapáginaetc.OmodeloHATEOAStransformariaocasodapaginação
paraficardaseguintemaneira:
<usuarios>
<usuario>
<id>1</id>
120

## Página 137

CasadoCódigo Capítulo5.Desenvolvaaplicações paraawebcomREST
<nome>Alexandre</nome>
<login>admin</login>
<senha>admin</senha>
</usuario>
<usuario>
<id>2</id>
<nome>Rafael</nome>
<login>rafael</login>
<senha>rafael</senha>
</usuario>
<link href="usuarios?inicio=0&amp;tamanhoPagina=2"
rel="primeiraPagina"/>
<link href="usuarios?inicio=2&amp;tamanhoPagina=2"
rel="proximaPagina"/>
<link href="usuarios?inicio=4&amp;tamanhoPagina=2"
rel="ultimaPagina"/>
</usuarios>
Repareque,agora,oslinksparaqueoclientesaibaquaispassosaseguirestão
presentesnocorpodapróximarequisição. Oslinksapresentamosatributos href
(paraqueoclientesaibaqualoendereçoaserseguido), rel(parasaberquala
relaçãodestelinkcomorecursoatual)e,opcionalmente, type(paraqueocliente
saibaqualoMIMEtypeoferecidopelolink).Porexemplo,nocasodarepresentação
dosnossosusuárioscomoimagens,oretornodalistagemdeusuáriospodeficar
assim:
<usuarios>
<usuario>
<id>1</id>
<nome>Alexandre</nome>
<login>admin</login>
<senha>admin</senha>
<link href="usuarios/1" rel="imagem" type="image/*"/>
</usuario>
<usuario>
<id>2</id>
<nome>Rafael</nome>
<login>rafael</login>
<senha>rafael</senha>
<link href="usuarios/2" rel="imagem" type="image/*"/>
</usuario>
121

## Página 138

5.10.IncluindolinksHATEOAS CasadoCódigo
<link href="usuarios?inicio=0&amp;tamanhoPagina=2"
rel="primeiraPagina"/>
<link href="usuarios?inicio=2&amp;tamanhoPagina=2"
rel="proximaPagina"/>
<link href="usuarios?inicio=4&amp;tamanhoPagina=2"
rel="ultimaPagina"/>
</usuarios>
Paraproduziressasalterações, noentanto,énecessárioalterarnossasclassesde
modelo,paraincluiroslinksaseremseguidos.
HATEOASe a modificação d a sclasses de modelo
AlgunsframeworksjátêmsuporteaHATEOAS,demaneiraqueestes
linksnãosejamintrusivosemrelaçãoàsclassesdemodelo.Todavia,este
suporteaindaédifícildeserutilizadomesmonessesframeworks,enada
dissoépadronizadopelaespecificaçãoJAX-RS1.0.Esteéumrecursoque
estáprevistoparalançamento(ouseja,padronização) naespecificação
JAX-RS2.0.
Porexemplo,arepresentaçãodoslinkséfeitapelaclasse Link:
package com.knight.usuarios.modelos.rest;
// imports omitidos
@XmlType(namespace = "http://knight.com/links")
@XmlAccessorType(XmlAccessType.FIELD)
public class Link {
@XmlAttribute
private String href;
@XmlAttribute
private String rel;
@XmlAttribute
private String type;
122

## Página 139

CasadoCódigo Capítulo5.Desenvolvaaplicações paraawebcomREST
public Link(String href, String rel) {
this.href = href;
this.rel = rel;
}
public Link(String href, String rel, String type) {
this(href, rel);
this.type = type;
}
public Link() {}
// getters e setters
}
Notequesetratadeumaclassecomum,aserutilizadapelasnossaspróprias
classesdemodelo.Porseralgocomumentreosmodelos,vamosrepresentaruma
entidadeRESTcomaseguinteinterface:
package com.knight.usuarios.modelos.rest;
public interface RESTEntity {
void adicionarLink(Link link);
}
Percebaqueestainterfacepodesermodificadaparaatenderaoutrasnecessida-
des,quesejamcomunsamodelosREST.
Nossaclasse Usuarios,aoimplementarestainterface,ficaassim:
//declaração de pacote e imports omitidos
@XmlRootElement
@XmlAccessorType(XmlAccessType.FIELD)
public class Usuarios implements RESTEntity {
@XmlElement(name = "usuario")
private Collection<Usuario> usuarios;
@XmlElement(name = "link")
123

## Página 140

5.10.IncluindolinksHATEOAS CasadoCódigo
private Collection<Link> links;
public Usuarios() { }
public Usuarios(Collection<Usuario> usuarios, Link... links) {
this.usuarios = usuarios;
this.links = new ArrayList<>(Arrays.asList(links));
}
@Override
public void adicionarLink(Link link) {
if (links == null)
links = new ArrayList<>();
links.add(link);
}
//getters e setters
}
Observeque,dessaforma,quandoaclasse Usuariosforserializadadevolta
paraocliente,elavaiconteroslinksqueprogramarmosparaseremtransmitidos.
Ocódigodaclasse UsuariosServicedeveseratualizadoparautilizarainterface
UriInfo,demaneiraaconferirmaisflexibilidadeparanossaclasse.
Porexemplo,paracriaroslinksdepaginação,énecessáriodescobrirocaminho
ondeousuárioestáatualmenteparacriarolink.Apartirdapáginaatualedonú-
merodeusuários,façoalgunscálculosparadescobrirquaissãoaprimeirapágina,
apáginaanterioràatual,apróximaeaúltima.Ométododecriaçãodoslinksde
paginaçãoficaassim:
private Link[] criarLinksUsuarios(UriInfo uriInfo,
Integer tamanhoPagina, Integer inicio, Long numeroUsuarios) {
Collection<Link> links = new ArrayList<>();
double numeroUsuariosDouble = numeroUsuarios;
double tamanhoPaginaDouble = tamanhoPagina;
// Arrendondamento para cima, para fornecer o número certo de
// páginas
Long numeroPaginas = (long) Math.ceil(numeroUsuariosDouble
/ tamanhoPaginaDouble);
124

## Página 141

CasadoCódigo Capítulo5.Desenvolvaaplicações paraawebcomREST
// O resultado da divisão será um int.
Long paginaAtual = new Long(inicio / tamanhoPagina);
Link linkPrimeiraPagina = new Link(
UriBuilder.fromPath(uriInfo.getPath())
.queryParam(PARAM_INICIO, 0)
.queryParam(PARAM_TAMANHO_PAGINA, tamanhoPagina).build()
.toString(), "primeiraPagina");
links.add(linkPrimeiraPagina);
//criação dos outros links
return links.toArray(new Link[] {});
}
Jáocódigoalteradodalistagemficaassim:
@GET
public Response listarUsuarios(
@HeaderParam("If-Modified-Since") Date modifiedSince,
@QueryParam(PARAM_INICIO) @DefaultValue("0") Integer inicio,
@QueryParam(PARAM_TAMANHO_PAGINA) @DefaultValue("20")
Integer tamanhoPagina,
@Context UriInfo uriInfo) {
Collection<Usuario> usuarios = em
.createQuery("select u from Usuario u", Usuario.class)
.setFirstResult(inicio).setMaxResults(tamanhoPagina.intValue())
.getResultList();
// Recuperamos o número de usuários presentes em nossa base
// para que possamos realizar o cálculo de páginas
Long numeroUsuarios = em.createQuery(
"select count(u) from Usuario u", Long.class).getSingleResult();
boolean atualizado = false;
if (modifiedSince != null) {
for (Usuario usuario : usuarios) {
if (usuario.getDataAtualizacao().after(modifiedSince)) {
atualizado = true;
break;
}
125

## Página 142

5.11.Testandotudo CasadoCódigo
}
} else {
// Se a data não tiver sido passada, deve considerar os recursos
// como 'mais atuais'
atualizado = true;
}
if (atualizado) {
for (Usuario usuario : usuarios) {
Link link = criarLinkImagemUsuario(usuario);
usuario.adicionarLink(link);
}
return Response.ok(
new Usuarios(usuarios, criarLinksUsuarios(uriInfo,
tamanhoPagina, inicio, numeroUsuarios))).build();
} else {
return Response.notModified().build();
}
}
Porquestões detamanho,ocódigo completonão serápostadoaqui. Caso
vocêqueiraconferir,confiraorepositóriodecódigodolivro: http://github.com/
alesaudate/soa.
5.11 Testando tudo
Paraquepossamosdesenvolverqualqueraplicaçãoeficientemente,énecessárioque
tenhamosmeioseficientesdetestes.Comaplicações orientadasaserviço,issonãoé
diferente.
ParatestarserviçosdesenvolvidoscomREST,noentanto,devemosadaptarnos-
sasestratégias.OSoapUIpossuifuncionalidadesparadesenvolvimentodetestesde
serviçosREST;noentanto,eunãooconsideroamelhorferramentaparaisso.Exis-
temtrêsferramentasqueeugostodeutilizarpararealizartestes,cadaqualcomvan-
tagensedesvantagens(quedevemserexploradasdeacordocomocenário).Essas
ferramentassão: Poster,curleaprópriaAPIdoframeworkqueestamosutilizando
paradesenvolvimentodosserviços.
126

## Página 143

CasadoCódigo Capítulo5.Desenvolvaaplicações paraawebcomREST
T estescom P o s t e r
OPosteréum plugindoFirefox.Comotal,deveserinstaladonopróprionave-
gador(podeserobtidoemhttps://addons.mozilla.org/pt-br/firefox/addon/poster/)
.U m avezinstalado,énotávelqueéumaferramentadeusobemsimpleseintuitivo,
comopodeservistonaimagem:
Figura5.5:Poster
Natelainicial,comaaba Content to Sendhabilitada,aáreadigitávelmais
abaixodateladeveconterosdadosaseremenviadosnocorpodarequisição. Por
exemplo,paraenviarumnovousuárioparaoserviço,essaáreadeveconteroXML
aserenviadoparaoserviço. T a m b é mépossívelenviardadosdearquivos(como
imagens,porexemplo),utilizandoocampo File.
OpontofracodoPosteréotratamentoemrelaçãoadadosbinários.Quando
umaimagemésolicitada,porexemplo,não seobtémaimagememsi,masare-
presentação bináriadamesma. Essacombinação fazcomqueoPostersejauma
ferramentafácildeutilizar,porémincompleta.
127

## Página 144

5.11.Testandotudo CasadoCódigo
T estescom curl
Comcurl,épossívelescrever scripts( .shnoLinuxe .batnoWindows)para
realizarostestes. NoUbuntu,épossívelinstalarocurlutilizandooseguinteco-
mando:
sudo apt-get install curl
Paraoutrasplataformas,confiraositedoprograma:http://curl.haxx.se/.
Parautilizarocurl,bastaescreveroscomandosnoterminal.Porexemplo,para
obteralistagemdeusuários,vocêpodeutilizaroseguintecomando:
curl http://localhost:8080/soa-cap05-0.0.1-SNAPSHOT/services/usuarios
Noteque,destaforma,o curlassumiu,automaticamente,ousodométodo
GETparaobtençãodosdados.Casoqueiramosutilizarummétododiferente,basta
adicionaroparâmetro -X;sequisermosadicionardados,podemosutilizaropa-
râmetro --data,seguidodosdados(seessesdadosforemprecedidospor@,ele
assumequedeveenviarosdadosdeumarquivo).
Ainda,paraadicionarcabeçalhos,podemosutilizaroparâmetro -H.Porexem-
plo,paratestaraatualizaçãodeimagens,podemosutilizaroseguintecomando:
curl -X PUT --data @saudate.png -H"Content-Type: image/png"
http://localhost:8080/soa-cap05-0.0.1-SNAPSHOT/services/usuarios/1
Desta forma, ele faráo envio da imagem referenciada pelo arquivo
saudate.png para a URL http://localhost:8080/soa-cap05-0.0.1-SNAPSHOT/
services/usuarios/1,utilizandoométodo POST.Repare,também,queajustamoso
cabeçalho Content-Typeparaserdotipo image/png.
Adesvantagemdocurléque,porserumaaplicaçãodelinhadecomando,deve-
seexecutaràpartedoprograma(ouseja,realizarainstalação eexecutarmanual-
menteostestes)ouadaptaropróprio scriptde deployparaexecutaroprograma(fer-
ramentasdeintegraçãocontínuacomooJenkinstambémpodemseradaptadaspara
executarestetipode script).Aindaassim,éumaboapedidaparaautomatizarseus
testesdeintegração.
T estescom a API do RESTEasy e Maven
U m aboaabordagemparatestarseusserviçospodeserutilizaraprópriaAPIdo
fr a mewo r kquevocêestáutilizandoparadesenvolverseusserviços(nonossocaso,
RESTEasy).Quasetodosos fr a mewo r ksJavaparadesenvolvimentodeserviçosREST
128

## Página 145

CasadoCódigo Capítulo5.Desenvolvaaplicações paraawebcomREST
doladodoservidortambémpossuemAPIsparadesenvolvimentodoladodocliente,
eéumaboaalternativacombinaressacapacidadecomoMaven,quepossuium
sistemadeexecuçãodetestesintegradosembutido.
T e n h aemmentequeostestesdequeestamosfalandoatéomomentosãotestes
simplesparaverificarafuncionalidadedosistema. OqueoMavenpossuiembu-
tidosãotestesdeintegraçãoautomatizadose“repetíveis”,ouseja,elessempreserão
executadosdemaneiraautomatizada.
ParahabilitaressetipodetestenoMaven,bastaincluiroseguintetrechono
arquivo pom.xml:
<build>
<plugins>
<plugin>
<artifactId>maven-failsafe-plugin</artifactId>
<version>2.6</version>
<executions>
<execution>
<goals>
<goal>integration-test</goal>
<goal>verify</goal>
</goals>
</execution>
</executions>
</plugin>
<!-- Outros plugins -->
</plugins>
</build>
Aseguir,bastaincluirumaclassecomnomesqueterminamcom ITou ITCase
napastadefontesdetestes( src/test/java),devidamenteconfiguradodeacordo
comnossoframeworkdetestes.Porexemplo,aclassedetestesdoserviçodeusuários
(configuradaparautilizaroJUnit)podeteroseguintecódigo:
package com.knight.usuarios.servicos.testes.integração;
// imports omitidos
public class UsuariosServiceIT {
public static String SERVICES_CONTEXT =
129

## Página 146

5.12.Programandoclientes CasadoCódigo
"http://localhost:8080/soa-cap05-0.0.1-SNAPSHOT/services";
public static String USUARIOS_CONTEXT =
SERVICES_CONTEXT + "/usuarios";
private byte[] fotoSaudate;
@Before
public void setup() throws IOException {
// Ajustes iniciais, como a carga da imagem, por exemplo
}
@Test
public void testRecepcaoImagens() throws Exception {
// códigos dos testes
}
}
EstestestesserãorealizadosutilizandoaAPIdopróprio fr a mewo r k,assimcomo
qualquercliente.
5.12 Programando clientes
AAPIdoRESTEasyprovêfacilidadesparadesenvolverclientesdeserviçostantode-
senvolvidosemJavaquantoemqualqueroutralinguagem.Adiferençaentreasduas
abordagenséque,casooserviçotenhasidofeitoemJava,épossívelgerarum p rox y
baseadoemumainterfacepararealizaressacomunicação,demaneirabastantese-
melhanteaclientesremotosEJB,porexemplo.Noentanto,notequeestaabordagem
promovealtoacoplamentocomaAPI.
CasovocêqueirarealizarodesenvolvimentodeseusclientesJavautilizandoesta
abordagem,bastaextrairosmétodosdasuaclassedeserviçoparaumainterface
(incluindoasanotações JAX-RS).V o c êpode,inclusive,removerestasanotações da
implementação,deixandosuaclassedeserviçomaislimpa.Ainterfacevaiconter,
então,váriosmétodosrelacionadosaformasdepesquisa,algunsparamodificação
dedadoseoutrosparatratamentodeimagens.
Aseção detratamentodebuscascontémosmétodos listarUsuarios e
find,daseguinteforma:
130

## Página 147

CasadoCódigo Capítulo5.Desenvolvaaplicações paraawebcomREST
package com.knight.usuarios.servicos;
// imports omitidos
@Path("/usuarios")
@Produces(MediaType.APPLICATION_XML)
@Consumes(MediaType.APPLICATION_XML)
public interface UsuariosServiceInterface {
static final String PARAM_INICIO = "inicio";
static final String PARAM_TAMANHO_PAGINA = "tamanhoPagina";
@GET
public Response listarUsuarios(
@HeaderParam("If-Modified-Since") Date modifiedSince,
@QueryParam(PARAM_INICIO) @DefaultValue("0") Integer inicio,
@QueryParam(PARAM_TAMANHO_PAGINA) @DefaultValue("20")
Integer tamanhoPagina,
@Context UriInfo uriInfo);
@GET
@Path("/{id}")
public Response find(@PathParam("id") Long id,
@HeaderParam("If-Modified-Since") Date modifiedSince);
// outros métodos
}
Observequeosmétodosdebuscasãoaquelesquetêmmaiorcomplexidade,por
aceitaremdiversasformas.Nonossocaso,aindapoderíamosexpandiraspossibili-
dadesparaumabuscaporexemplos,por r a n g e sespecíficosdedadosetc.;parafins
desimplicidade,mantemosapenasestesdois.
Ospróximosmétodospresentesnainterfacesão osrelativosamodificaçãode
dados—inserção,atualizaçãoeremoção.Notequeosmétodosdeatualizaçãoere-
moçãopermitemqueoIDdousuárioaserremovidovenhatantonaURLquanto
diretamentenocorpodarequisição(ouseja,dentrodoXMLrepresentandoousuá-
rio):
@POST
public Response create(@Context UriInfo uriInfo, Usuario usuario);
131

## Página 148

5.12.Programandoclientes CasadoCódigo
@PUT
public Response update(Usuario usuario);
@PUT
@Path("/{id}")
public Response update(@PathParam("id") Long id, Usuario usuario);
@DELETE
public Response delete(Usuario usuario);
@DELETE
@Path("/{id}")
public Response delete(@PathParam("id") Long id);
Porúltimo,temososmétodosdemanipulaçãodeimagens:
public static final String CAMPO_DESCRICAO_IMAGEM = "Descricao";
@PUT
@Path("/{id}")
@Consumes("image/*")
public Response adicionarImagem(
@HeaderParam(CAMPO_DESCRICAO_IMAGEM) String descricao,
@PathParam("id") Long idUsuario,
@Context HttpServletRequest httpServletRequest, byte[]
dadosImagem);
@GET
@Path("/{id}")
@Produces("image/*")
public Response recuperarImagem(@PathParam("id") Long id,
@HeaderParam("If-Modified-Since") Date modifiedSince);
}
Com esta interface, o teste com RESTEasy pode ser feito atra-
vés da criação de um p rox y. Para isso, basta utilizar a classe
org.jboss.resteasy.client.ProxyFactory, passando como parâme-
trooendereçodaaplicaçãoeainterfacedoserviço.Dessaforma,oseguintecódigo
podesercriado:
132

## Página 149

CasadoCódigo Capítulo5.Desenvolvaaplicações paraawebcomREST
UsuariosServiceInterface usuariosService = ProxyFactory.create(
UsuariosServiceInterface.class,
"http://localhost:8080/soa-cap05-0.0.1-SNAPSHOT/services");
Osmétodosdeserviçopodemsertestadoscomoseestivessemsendoexecutados
localmente.Porexemplo,casonossaclassedeserviçoretorneumPOJO,essePOJO
éautomaticamentemapeado.Suponhaquenossoserviçodelistagemdeusuáriosre-
torneumainstânciadaclasse Usuarios.Dessamaneira,oseguintecódigopoderia
serutilizado:
Usuarios usuarios = usuariosService.listarUsuarios();
Não éocasodosnossosserviços. T o d a sasentidadesestão mapeadascom
Response.Nestecaso,nossainvocaçãodeveesperarumarespostadessetipo.Para
evitarproblemascom castderetorno,devemosfazero castdessarespostaparaa
classe org.jboss.resteasy.client.ClientResponse,quecontémmétodos
quefacilitamarecuperaçãodosdados.
Lembre-sequenossométododelistagemdeusuários,porexemplo,possuíaqua-
troparâmetros:o header If-Modified-Since,doisparâmetrosparapromover
paginação e UriInfo,paraquepossamosrecuperardadosdocontextodainvo-
cação. Nãotemosacessoaesteúltimopelocliente,então,deixaremossempreem
branco( null).Dessaforma,ainvocaçãoparaestemétodoficaassim:
ClientResponse<Usuarios> response =
(ClientResponse<Usuarios>) usuariosService
.listarUsuarios(null, null, null, null);
U m avezquetemosacessoaessaresposta,devemostestarostatusdaresposta.
Casoseja200,podemosrecuperarosusuáriosutilizandoométodo getEntity,
passandocomoparâmetroaclasseparaqualdeveserfeitoo castdaresposta(no
caso, Usuarios):
Usuarios usuarios = response.getEntity(Usuarios.class);
Assim,podemosinteragirnormalmentecomnossoserviço;noentanto,sequi-
sermos,tambémpodemosterumainteração avançadacomserviçosRESTfeitos
emoutraslinguagens,também.Paraisso,utilizamosumaabordagemdiferente:
a classe org.jboss.resteasy.client.ClientRequest.ClientRequest
(nocasodeutilizarmosRESTEasycomo fr a mewo r k).Essaclasserecebecomopa-
râmetroparaoconstrutorum templatedeURI(semelhanteaoutilizadonoladodo
servidor).Parapopularmosesse template,utilizamosométodopathParameters.
133

## Página 150

5.12.Programandoclientes CasadoCódigo
U m avezcriadooformatodarequisição,bastaexecutarométodo(daclasse)de
nomeigualaométodoHTTP( GETsetorna get(), POSTsetorna post(),e
assimpordiante).Podemospassarcomoparâmetroparaestemétodoaclasseaser
utilizadaparaajustarotipoderetorno.Porexemplo,paraexecutarmosabuscapor
umusuárioespecífico,podemosexecutaroseguintecódigo:
ClientResponse<Usuario> response = new ClientRequest(
"http://localhost:8080/soa-cap05-0.0.1-SNAPSHOT" +
"/services/usuarios/{id}").pathParameters(1).get(Usuario.class);
Usuario usuario = response.getEntity();
Podemos tambémajustar o tipo de conteúdoaceito utilizando o método
accept(),ométodo header()paraajustar headersHTTPeométodo body
paraajustarocorpodarequisição. Porexemplo,parasolicitararepresentaçãodo
usuáriocomoimagem,utilizamososeguintecódigo:
ClientResponse<byte[]> response = new ClientRequest(
"http://localhost:8080/soa-cap05-0.0.1-SNAPSHOT/" +
"services/usuarios/{id}")
.pathParameters(1).accept("image/*").get(byte[].class);
byte[] imagem = response.getEntity();
Eparainserirumanovaimagem:
ClientResponse<?> response = new ClientRequest(
"http://localhost:8080/soa-cap05-0.0.1-SNAPSHOT/" +
"services/usuarios/{id}")
.pathParameters(1).header("Descricao", "descricao da imagem")
.body("image/png", arrayDeBytesContendoUmaFoto)
.put();
Assim,nossoclientejáestáflexívelobastanteparatratarserviçostantodesenvol-
vidosemJavaquantoemqualqueroutralinguagem,concluindonossocasodeuso.
T a m b é mépossívelescreverclientesemJavascriptparaserviçosREST,tornandopos-
síveldesenvolverinterfaces(páginasweb)completamentedesacopladasdo backend
daaplicação. Nãofazpartedoescopodestelivrotratardessescasos. Casodeseje,
consultelivrosespecializadosemJavaScript/jQueryparasabermaisarespeito.
134

## Página 151

CasadoCódigo Capítulo5. DesenvolvaaplicaçõesparaawebcomREST
5.13 S umário
Nestecapítulo,vocêviuemdetalhescomodesenvolver,consumiretestarservi ços
REST.Nossocasodeusoparaissofoiacria ção,recuperação,atualizaçãoedele çãode
usuários,comvariaçõesparacobrircasoscomopagina ção,tratamentodeimagens
etc.
Paraisso,vocêviudesdeocome çoosprincípiosdofuncionamentodoprotocolo
HTTP.Vocêconferiuemdetalhescomofuncionamoscódigosdestatus, headers,
tiposMIMEeoutrosdetalhesdoprotocolo.Dessaforma,vocêobteveembasamento
sobreabasedeREST.Depois,vocêconferiuosdetalhesdeREST—funcionamento
derecursos,tiposMIME,HATEOASeoutros.
Aofinal,vocêconferiucomorealizaracria çãodeclientes,tantoparaservi ços
desenvolvidosnapróprialinguagemJavaquantoemoutraslinguagens,tornando-os
tantofáceisdedesenvolver,porémacoplados,comomaisdifíceis,porémflexíveise
comcapacidadesdecomunica çãocomoutraslinguagens.
Aindarestasabercomoutilizaracria çãodessesusuáriosnaseguran çadenossos
aplicativos.Nopróximocapítulo,vocêverácomorealizarotratamentodeseguran ça
emserviços,tantoutilizandoWSDLsquantoosmodelosemREST.
135
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 152

E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 153

Capítulo6
Segurançaemwebservices
“Há mais coisas entre o céu e a terra, Horácio, do que sonha a nossa vã filosofia”
–WilliamShakespeare
Finalmente,seusistemadegerenciamentodeusuáriosestácompleto.Masficaa
dúvida,comoutilizarestesservi çosatravésdosseussistemas?Váriosdesafiosestão
presentesnestemomento:
• Comopreveniroroubodessasinformações?
• Comopreveniracriaçãodedadosdemaneiranão-autorizada?
• Comopreveniraalteraçãodessesdadosdemaneiranão-autorizada?
• Comoimpedirumatacantedeusarinformaçõeslegítimas?
• eoutros...
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 154

6.1. Ataques:Man-in-the-middleeeavesdropping CasadoCódigo
Nestemomento,portanto,suaprincipaltarefaéprotegerseusistemadegeren-
ciamentodeusuários. Noentanto,antes,vocêprecisasaberquaisproblemasvocê
desejaevitar.
Pelanaturezacliente-servidordeaplica çõesSOA,seuproblemaprincipalépro-
tegeromecanismodetransporte(jáqueaseguran çadoladodoservidoréquestãode
proteçãoemoutrosníveis—porexemplo,usuárioscomacessoaosistemadearqui-
vosdosistemaoperacional—nãocobertosporestelivro).Comoestamosusandoo
protocoloHTTPcomotransporte,vamosutilizaromecanismopadrãodeprote ção,
oHTTPS.Contudo,vamosverprimeiroquaisosproblemasdeseguran çadosquais
devemosnosproteger.
6.1 A taques : Man -in-the -middle e eavesdropping
Quandoutilizamosainternet(eoprotocoloHTTP,emgeral),nossasrequisi ções
geralmentepassamporváriosequipamentosderede.Muitasvezes,nãosabemosao
certoquaiselessão,muitomenossuasinten ções.Aoexecutarocomando tracert
noWindows(ou traceroutenoLinux),temosumabrevevisãodessescaminhos.
Aousaressecaminhoapontadopara www.google.com.br,porexemplo,podemosob-
terresultadoscomoosseguintes(dadosligeiramentealterados):
traceroute to www.google.com.br (190.98.170.25), 30 hops max,
60 byte packets
1 my.router (192.168.1.1) 4.938 ms 5.028 ms 5.023 ms
2 * * *
3 201-0-90-86.dsl.telesp.net.br (201.0.90.86) 13.770 ms 13.863 ms
20.184 ms
4 201-0-6-5.dsl.telesp.net.br (201.0.6.5) 8.062 ms
5 187-100-53-13.dsl.telesp.net.br (187.100.53.13) 72.049 ms
6 213.140.51.113 (213.140.51.113) 38.417 ms
7 Xe9-0-6-0-grtsanem1.red.telefonica-wholesale.net (84.16.15.25)
17.514 ms
Estaéumalistagemparcialdocaminhopercorridopelospacotesentreomeu
computadoratéositedoGoogle.Noentanto,acertopontoasinforma çõescome çam
aficarnebulosas,comoaparecimentodeservidoresdesconhecidos,comoéocaso
doservidordenúmero6,nalistagemacima,quenãopossuiumendere çoDNS(ou
seja,nãotemnome).
Essassituaçõesocorremporcontadapróprianaturezadainternet,queéade
umarededistribuída,semumcontroladordeterminado.Destaforma,fogeaonosso
138
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 155

CasadoCódigo Capítulo6. Segurançaemwebservices
controledeterminarquaisrecursosestãoounãoautorizadosacontrolaroredireci-
onamentodospacotesderede,emaisainda,controlaraleituradestesrecursos.Esse
problemaacabasendoaraizdedoisataquesnainternet: man-in-the-middlee eaves-
dropping.
Figura6.1:Atacanteinterceptandorequisi ções
Eavesdrop,emumatradu çãoliteraldoinglês,significaouvirescondido,eremete
aaçõescomoouvirpordetrásdeumaportaouutilizarumgrampotelefônico.Em
computação,significaapuraesimplesintercepta çãodemensagenselerseucon-
teúdo—sem,noentanto,alterá-lo.Esteataquepodeserutilizadoparainterceptar
senhas,porexemplo,paraqueoatacanteutilizeemmensagensseparadas(subse-
quentesàmensageminterceptada).
Jáoataque man-in-the-middleéumainterceptaçãocontrolada:umatacantein-
terceptaaschamadasemodificaosdados,demaneiraquetantooclientequantoo
servidornãosabemqueaconexãoestásendocontroladaporumterceiroator.Pode
serutilizadaparaalteraronúmerodevolumescompradosemnossalivraria,por
exemplo.
139
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 156

6.2. Proteçãocontraintercepta çãocomHTTPS CasadoCódigo
Interceptação de mensagens e sniffers
Nãoénecessárioirlongeparaverificaroestadodesuasconexões.
SoftwarescomooWireshark(http://www.wireshark.org/)podemreali-
zaressaintercepta çãodedadossemmuitoesfor ço. Esteéumfamoso
sniffer(ouseja,softwarederastreamentoeescuta),disponívelparaWin-
dowseMac.
6.2 P roteção contra interceptação com HTTPS
Asolu çãomaisusadaparaoproblemadaintercepta çãoéousodeHTTPS( Hy-
pertext Transfer Protocol over Secure Sockets Layer),ebaseia-senaaplica çãodeuma
camadadeseguran çacomSSL( Secure Socket Layer)sobreoHTTP.Estacamadauti-
lizacertificadosdigitaisparaencriptarascomunica çõesegarantiraautenticidadedo
servidore,opcionalmente,docliente.
Estescertificadossãoamplamenteutilizadosnainternet. Todavezquevocê
acessaumaURLcujoendere çocome çacom https, estemecanismoestápre-
sente.Porexemplo,aoacessaroGmail(cujoendere çorealestápresenteemhttps:
//accounts.google.com),épossívelvisualizarasinforma çõesdocertificado:
140
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 157

CasadoCódigo Capítulo6. Segurançaemwebservices
Figura6.2:Informa çõesdocertificadoGoogle
Estecertificadoéusadoparaqueoclienteconfirmeaautenticidadedoservidor
(pelasinformaçõescontidasnase ção Emitido para)ecriptografeasinforma ções
utilizando-o.Paraqueoclientepossatercertezadaconfiabilidadedessecertificado,
elepodeseremitidoporumaautoridadecertificadora( Certification Authority—
CA).Estaautoridadeébemconhecidaentreosclientes,queconfiamnamesma.
Emalgunscasos,ocertificadotambémpodeserautoassinado,ouseja,emitidopelo
própriosite—oqueotornamenosconfiável.
Damesmaforma,estescertificadostambémpodemserlevantadospelocliente
paraqueoservidorconfirmeaidentidadedocliente—maisoumenosdomesmo
141
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 158

6.2. Proteçãocontraintercepta çãocomHTTPS CasadoCódigo
modoqueumaautentica çãoutilizandousuárioesenha.Estamaneira,noentanto,é
maiscomplicadadeserutilizadanainternete,emgeral,éutilizadaapenasemcasos
muitoespecíficos.
Aoutilizarcertificadosdigitais,oservidorprovêummecanismodecriptografia
baseadoemchavespúblicaseprivadas. Estemecanismoébaseadoemalgoritmos
queutilizamduaschaves,umapúblicaeumaprivada. Achavepúblicaéutilizada
paraencriptardados;eaprivada,paradecriptar. Elasrecebemestesnomespor-
queaideiageraléqueachavepúblicasejaconhecidaportodososclientesdeum
determinadoserviço,eaprivada,apenaspeloprovedordoservi ço.
Achavepúblicadoscertificadosdigitaissãogeralmenteutilizadasparaencriptar
umoutrotipodechaves,quesãoconhecidascomochaves simétricas.Estaschaves,
porsuavez,sãoasmesmastantoparaencriptarquantoparadecriptardados.Com
osistemadechavepúblicaeprivada,oclienteeoservidortêmachancedenegociar
estachavesimétrica—queéutilizadanasduaspontasparaencriptarasmensagens.
AlinguagemJavaprovêumsistemapróprioparaarmazenamentodecertifica-
dos,chamadoJKS- Java Key Store.UmarquivoJKScontémumacole çãodecerti-
ficados,cadaumdevidamenteidentificadoporum alias.Essescertificadospodem
sercriadosearmazenadosutilizandoumaferramentachamada keytool,presente
naJDK.
ParautilizaroJKS,vocêdevenavegaratéapasta bindasuaJDK,alémdepos-
suirumasériedeinforma ções,comoodomíniodawebondeeleseráutilizado,o
períododuranteoqualessecertificadoseráválidoeoalgoritmoqueseráutilizado
paraencriptaredecriptarseusdados.Porexemplo,paragerarumcertificadoválido
duranteumano,comalgoritmoRSA(comcomprimentodechavede2048bits)e
válidoparaoendereço localhost,oseguintecódigopodeserutilizado:
keytool -genkey -keyalg RSA -alias knight_usuarios -keystore
../jre/lib/security/cacerts -storepass changeit -validity 360
-keysize 2048
Estecomandolevaráaumasériedequestionamentosemrela çãoàempresa.Es-
tesdadospodemserpopuladosnormalmente,deacordocomasquestões,exceto
oprimeiro(emumaJDKemportuguês,aperguntaé“Qualéoseunomeesobre-
nome?”).Nestecampo,deve ser inserido o domínio onde a aplica ção será hospe-
dada—nonossocaso, localhost.
142
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 159

CasadoCódigo Capítulo6. Segurançaemwebservices
Figura6.3:Questionamentosemrela çãoàcria çãodocertificado
6.3 U sando mecanismos de autenticação HTTP
Emaplicaçõesqueutilizamseguran ça,geralmenteénecessáriofornecermecanismos
paraqueoclientepossaseidentificar.Apartirdestaidentifica ção,oservidorcheca
seascredenciaisfornecidassãoválidasequaisdireitosestascredenciaisdãoaele.
Estesprocedimentosrecebemonomedeautentica ção(ouseja,oclientefornecendo
credenciaisválidas)eautorização(oservidorchecandoquaisdireitosoclientetem).
OprotocoloHTTPoferecedoistiposdeautentica ção: basice digest. Aau-
tenticação basicérealmentemuitosimples; consisteempassaro headerHTTP
Authorizationobedecendoaoseguintealgoritmo:
Basic Base64({#usuário}:{#senha})
Considerandousuário alexandreesenha alexandre,ocabe çalhopassaria
ateroseguintevalor:
Authorization: Basic YWxleGFuZHJlOmFsZXhhbmRyZQ==
143
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 160

6.3. UsandomecanismosdeautenticaçãoHTTP CasadoCódigo
Notequeestesistemanãoapresentamuitaseguran ça:casoumatacanteinter-
cepteestarequisi ção,oalgoritmoBase64éfacilmentereversível,levandoaosdados
originais.
O algoritmo Base64
OalgoritmoBase64éamplamenteconhecidopelainternet.Apesarde
ser(tecnicamentefalando)umalgoritmodecriptografia,eleémaisutili-
zadonainternetparatráfegodedadosbinários(jáqueconvertequalquer
espéciedeformatobinárioemcódigoalfanumérico).Paramaisinforma-
çõesarespeito,leiahttp://tools.ietf.org/html/rfc989,se ção4.3.
Destaforma,amaiorpartedossistemasqueutilizamautentica ção basic,utili-
zamtambémHTTPS,paraqueumatacantenãodescubraousuárioesenhaqueestão
sendotrafegados.Mesmoassim,arequisi çãoficaexpostaaintercepta ções,queum
atacantepodeusarparareenviarumarequisi çãocomosefosseoclientelegítimo.
Apesardeoatacantenãosaberexatamenteoqueestáenviando,elepodeperfeita-
mentereenviarumarequisi çãoquejáhaviasidoenviadaanteriormentepelocliente
legítimo.
Paracontornaresteseoutrosproblemas,oalgoritmo digestpodeserutilizado.
Estealgoritmousaváriasinforma çõesalémdousuáriopararealizaraautentica ção:
uma stringaleatória(conhecidacomo nonce),uma stringcontendooníveldeprote-
ção(conhecidacomo qop),ocontextodoservidor(conhecidocomo realm),eoutros
parâmetrosopcionais,quesãofornecidospeloservidorapósumaprimeiratentativa
deobterumrecursoprotegido.
Suponha a seguinte interação: um cliente tenta acessar uma URI
/services/usuarios, utilizando o métodoGET. Ao fazer isso (sem auto-
rizaçãoalgumapresente),elerecebeaseguinteresposta:
401 Unauthorized
WWW-Authenticate: Digest realm="MyRealm",
qop="auth",
nonce="0cc194d2c0f4b6b765d448a578773543",
opaque="92ea7eedd41225f43d534bc544c2223"
Essarespostaéchamadade desafio. Oservidor,parasecertificardequeo
clienteéquemdizser,mandaumadescri çãodocontextoondeoclientedeveseau-
tenticar(nestecaso, MyRealm),oníveldequalidadedaprote ção(nestecaso auth)
144
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 161

CasadoCódigo Capítulo6. Segurançaemwebservices
euma stringaleatória,queseráutilizadacomogarantiadequearequisi çãoutilizada
nãopassarápeloschamados replay attacks,ouseja,umatacantenãointerceptaráa
requisiçãoereenviará,comosefosseoclientelegítimo.
Paracalculararespostadodesafio, oclientetemumtrabalhoconsideravel-
mentemaior.Tendocomoparâmetroosdadosdodesafioacimaeusuárioesenha
alexandre,ocálculoaserfeitoéoseguinte:
#método=GET
#path=/services/usuarios
#realm=MyRealm
#nonce=0cc194d2c0f4b6b765d448a578773543
#qop=auth
#contador=00000001
#nonceDoCliente=4a7a0b7765d657a756e2053d2822
#usuário=alexandre
#senha=alexandre
a1 = HEXADECIMAL(MD5({#usuário}:{#realm}:{#senha}))
a2 = HEXADECIMAL(MD5({#método}:{#path}))
a3 = HEXADECIMAL(MD5({a1}:{#nonce}:{#contador}:
{#nonceDoCliente}:{#qop}:{a2}))
// Valor de a3: f08528d7e052986e6563a905ab5b1b7b
O algoritmo MD5
OalgoritmoMD5,assimcomoBase64,tambéméamplamenteco-
nhecido. Todavia,nãoéumalgoritmodecriptografia,esim,de hash.
Porteressanatureza,umavezcalculado,nãopodeserrevertido. Para
maisinformações,consultehttp://www.ietf.org/rfc/rfc1321.txt.
Comavariável a3,oclientepode“devolver”arequisiçãocomadevidaautori-
zação:
GET /services/usuarios HTTP/1.1
Host: localhost
Authorization: Digest username="alexandre",
145
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 162

6.4. Habilitandosegurançaemaplica çõesREST CasadoCódigo
realm="MyRealm",
nonce="0cc194d2c0f4b6b765d448a578773543",
uri="/services/usuarios",
qop=auth,
nc=00000001,
cnonce="4a7a0b7765d657a756e2053d2822",
response="f08528d7e052986e6563a905ab5b1b7b",
opaque="92ea7eedd41225f43d534bc544c2223"
Comessesdados,oservidorcalculao hashdamesmaforma. Casoaresposta
obtidasejaigual,oclienteestáautorizado;casocontrário,não.Notequeoservidor
precisaterconhecimentodousuárioesenha(alémdosdadospassadospelocliente)
paratercondi çõesdecalcularesse hash. Semqueomesmotenhaconhecimento,
antecipadamente,dequaléousuárioesenha,nãoépossívelcalculá-lo.Alémdisso,
umpossívelinterceptadordarequisi çãonãoconseguereenviaramesmainforma ção,
jáqueelementosaleatóriossãointroduzidosnamensagemedescartadosquando
utilizados.
6.4 H abilitando segurança em aplicações REST
Tendoestesconceitosemmente,vocêéplenamentecapazdeaplicá-losemseusser-
viçosREST.Lembre-sedeque,portratar-sedeservi çosbaseadosemHTTP,oscon-
ceitosdeseguran çaaplicam-seaREST,também.Então,damesmaformacomovocê
habilitariasegurançaempáginasJSPouServlets,vocêhabilitaaseguran çaemREST.
Paraisso,aprimeiracoisaaserfeitaéfazercomqueseuservidorJBossenxergue
ocertificadoquevocêcriouanteriormente.Apesardenãoserorecomendado,você
podefazeressaedi çãodiretamentenoarquivo standalone.xml.
Edição de parâmetros JBoss
O modo mais recomendado para desenvolvedores editarem con-
figurações no servidor JBoss é pela interface gráfica, presente em
http://<endereço-da-máquina>:9990/console. Seaconfiguraçãodese-
jadanãoforacessívelpelainterface,deve-seutilizaroCLI( Command-
Line Interface).Paramaisdetalhes,consulteadocumenta ção.
Parainstalarocertificadonoservidor,vocêdeveencontraradefini çãodosub-
sistema webedefinirumconectorHTTPS.Paraencontrarosubsistema,utilizeum
146
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 163

CasadoCódigo Capítulo6. Segurançaemwebservices
editordetextoeacheaentrada urn:jboss:domain:web:1.1. Adefiniçãodo
conectorficaassim:
<connector name="https" protocol="HTTP/1.1" scheme="https"
socket-binding="https" secure="true" />
Nãosepreocupecomessasinforma ções.Aúnicareferênciaadadoslocalizados
naprópriaconfigura çãoestánoatributo socket-binding,masessainforma ção
jáestápresentenaconfiguração.
Opróximopassoéconfiguraresteconector,paraquetodavezqueumrecurso
HTTPSforacessado,ocertificadocriadosejautilizado. Paraisso,bastautilizara
definiçãodocertificadocomoaseguinte:
<connector name="https" protocol="HTTP/1.1" scheme="https"
socket-binding="https" secure="true">
<ssl name="ssl" key-alias="knight_usuarios"
certificate-key-file=
"<localização da JDK>/jre/lib/security/cacerts"
protocol="TLSv1"
ca-certificate-file=
"<localização da JDK>/jre/lib/security/cacerts"/>
</connector>
Notequeestadefini çãoutilizaomesmo aliasdocertificadocriado,comaloca-
lizaçãodomesmo.Parafinsdetestes,épossívelutilizarorepositóriojáembarcado
naJDK(ouseja,o cacerts).Noentanto,éaltamenterecomendávelcriarumre-
positórioseparado,paraqueogerenciamentodestescertificadossejafacilitado.
Além disso, uma configuração adicional deve ser inserida no subsis-
tema de segurança do JBoss (que pode ser localizado utilizando a entrada
urn:jboss:domain:security:1.1). Énecessáriocolocaralgumasinforma-
çõesrelativasaocertificadodeseguran çatambémnocontextodaaplica ção web,de
acordocomoseguinte:
<subsystem xmlns="urn:jboss:domain:security:1.1">
<security-domains>
<!-- Configurações de domínios de segurança -->
<security-domain name="jboss-web-policy" cache-type="default">
<authorization>
<policy-module code="Delegating" flag="required"/>
</authorization>
147
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 164

6.4. Habilitandosegurançaemaplica çõesREST CasadoCódigo
<jsse keystore-password="changeit"
keystore-url=
"<localização da JDK>/jre/lib/security/cacerts"
truststore-password="changeit"
truststore-url=
"<localização da JDK>/jre/lib/security/cacerts"
server-alias="knight_usuarios" protocols="TLS"/>
</security-domain>
</subsystem>
Substitua os locais onde encontra localização da JDK"pelo
caminho da sua instalação. Por exemplo, se sua JDK estiver
instalada em /usr/lib/jvm/java-7-oracle (no caso de um sistema
operacional Linux), então o caminho do arquivo cacerts será
/usr/lib/jvm/java-7-oracle/jre/lib/security/cacerts . Em caso de um sistema
operacional Windows, será algo similar a C:\Program Fi-
les\Java\jdk1.7.0_07\jre\lib\security\cacerts . A senha (referenciada na
listagem como changeit
Feitoisso,seuJBossestáprontopararesponderasrequisi çõescomocertificado
certo.
Opróximopassoéconfigurarosservi çosparaqueelessópossamatenderrequi-
siçõesutilizandoHTTPS.Paraisso,énecessárioeditaroarquivo web.xml,descre-
vendoaURLqueseráprotegida,omodelodeautentica ção,osistemadeprote ção
dacamadadetransporteeopapelqueoclientequeacessarestaURLdeveráter.
Paraisso,descrevemosopapelcomo admin,aURLcomoqualquerumaapartir
de /services(ouseja,todososservi çosdestepacote)eutilizandoqualquermé-
todoHTTP.Alémdisso,informamosqueacamadadetransporteseráprotegidapor
HTTPSeautentica ção BASIC.Destaforma,oseguinteconteúdodeveserinserido:
<security-role>
<description>Administrador</description>
<role-name>admin</role-name>
</security-role>
<security-constraint>
<web-resource-collection>
<web-resource-name>Todos os serviços</web-resource-name>
<url-pattern>/services/*</url-pattern>
<http-method>GET</http-method>
148
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 165

CasadoCódigo Capítulo6. Segurançaemwebservices
<http-method>POST</http-method>
<http-method>PUT</http-method>
<http-method>DELETE</http-method>
<http-method>HEAD</http-method>
<http-method>OPTIONS</http-method>
</web-resource-collection>
<auth-constraint>
<role-name>admin</role-name>
</auth-constraint>
<user-data-constraint>
<transport-guarantee>CONFIDENTIAL</transport-guarantee>
</user-data-constraint>
</security-constraint>
<login-config>
<auth-method>BASIC</auth-method>
</login-config>
Aprimeirase çãodestaconfigura ção( security-role)declaraopapel admin.
Asegundaparte, security-constraint,determinaquetodosquequiserem
acessaraURL /services(esubURLs)utilizandoosmétodos GET, POST, PUT,
DELETE, HEADe OPTIONSdeverãoteropapel admin.Alémdisso,estase çãodeter-
minaqueoprotocolodetransportedeveserseguro(ouseja,deveutilizarHTTPS).
Porúltimo,aseção login-configdeterminaqueasURLsprotegidasdeverãousar
autenticação BASIC.
O próximo passo é determinar como o servidor realizará a obtenção dos
usuários. O mecanismo padrão para realizar este tipo de tarefas em Java é o
JAAS —Java Authentication and Authorization Service . No JBoss 7, para rea-
lizar a declaração do mecanismo, basta acrescentar um domínio de segurança
nosubsistemadeseguran ça,quepodeserencontradorealizandoumabuscapor
urn:jboss:domain:security:1.1.
VáriostiposdesistemasdeloginsãoaceitospeloJAAS.OJboss7jávempré-
configuradopararealizararmazenamentodeusuáriosemarquivosdepropriedades;
noentanto,gostaríamosdemanternossosdadosarmazenadosembancodedados,
jáquesetratadeummecanismomaisflexível.Pararealizaressadefini ção,contudo,
precisamosdealgumasinforma çõessobreessebanco,taiscomo: nomeJNDIdo
datasource, queryparalocalizaçãodasenha, queryparalocalizaçãode rolesdesegu-
rança,algoritmode hashutilizadoparaarmazenagemealgoritmoparacodifica ção
dasenha.
149
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 166

6.4. Habilitandosegurançaemaplica çõesREST CasadoCódigo
Nonossocaso,utilizaremosum datasourcequeseráinstaladopelaprópriaapli-
cação,denomeJNDI java:jboss/datasources/KnightUsuariosDS.Utili-
zaremos,paraarmazenamentodenossosusuáriosesenhas,umatabelachamada
usuario_privilegiado,comcolunas logine senha,respectivamente.Oal-
goritmode hashutilizadoparaarmazenarassenhasseráo SHA-256,eoalgoritmo
decodificação, Base64.Váriosvaloressãoaceitoscomoalgoritmode hash,como
MD5e SHA-1.IssoédependentedaJVM,demaneiraqueépossívelinstalarnovos
algoritmos.Assim,adefini çãododomíniodeseguran çaficariaassim:
<security-domain name="MyRealm">
<authentication>
<login-module code="Database" flag="required">
<module-option name="dsJndiName"
value="java:jboss/datasources/KnightUsuariosDS"/>
<module-option name="principalsQuery"
value=
"select senha from usuario_privilegiado where login=?"/>
<module-option name="rolesQuery"
value="select 'admin','Roles' from
usuario_privilegiado where login=?"/>
<module-option name="hashAlgorithm" value="SHA-256"/>
<module-option name="hashEncoding" value="base64"/>
</login-module>
</authentication>
</security-domain>
O que significam os parâmetros na query de roles?
Comovocêpôdenotar,a queryparasele çãodepapéisdevebuscar
duascolunas. Aprimeirairácontera roleemsi(nocaso,sempreserá
admin). Asegundacontémumadescri çãoda role,eécomummanter
Roles.
Finalmente,pararealizaraliga çãodaaplica çãocomodomíniodeseguran ça,
bastacriarumarquivochamado jboss-web.xmlnapasta WEB-INFdopro-
jeto,referenciandoo security domain quefoicriadonoJBoss(atravésdonome:
MyRealm):
150
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 167

CasadoCódigo Capítulo6. Segurançaemwebservices
<?xml version="1.0" encoding="UTF-8"?>
<jboss-web>
<security-domain>MyRealm</security-domain>
</jboss-web>
Notequeoconteúdoda tag security-domainéonomedodomíniodese-
gurança.
Feito isso, basta realizar o deploy da aplicação no servidor e na-
vegar para a URL do servi ço de usuários: https://localhost:8443/<
contexto-da-aplicação>/services/usuarios e comprovar tanto a
utilizaçãodocertificadoquantoasolicita çãodesenha(casovocêestejafazendoo
testecomaaplica çãocontidanoGitHub,ousuárioesenhasão admin).
Figura6.4:Oservi çodefornecimentodeusuários,jácomcertificadoinstalado
6.5 C onhecendo WS-Security
Vocêaprendeuacriareprotegerservi çosREST.Issoporqueessetipodeservi ço
funcionabaseadonoprotocoloHTTP;maseservi çosbaseadosemSOAP?Estes
nãofuncionamsemprebaseadosemHTTP;sãolivresdeprotocolodetransporte.
Apesardeserperfeitamentepossívelinserirautentica çãoeautoriza çãoHTTPem
serviçosbaseadosemWS-*eSOAP,estenãoéomelhormecanismoparaprote ção
151
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 168

6.5. ConhecendoWS-Security CasadoCódigo
deserviçosdessetipo.
Pensandonesseproblema,aOASIS( Organization for the Advancement of Struc-
tured Information Standards—OrganizaçãoparaoAvan çodePadrõesemInforma-
çõesEstruturadas)desenvolveuo WS-Security(tambémabreviadocomo WSS),
queéumaextensãoparaojáconhecidosistemadecomunica çãoentreservi çosbase-
adosemcontratosWSDL.Essaextensãocontémváriosmecanismosquepermitem
arealizaçãodecomunica çõessegurasmesmoquandooprotocolodetransportenão
éseguro,garantindoassimconfiabilidadeparaasmensagenssobqualquersistema
detransporteutilizado.
Segurança de informações e a NF-e
NoBrasil,umsistemadegera çãodeassinaturadigitalvoltadoaXML
(XML Signature)temsidomuitoutilizadoemprojetosdeintegra çãocom
osistemadeNotaFiscalEletrônicadosGovernosEstaduaiseFederal.
Apesardeserumaformadeprotegeraintegridadedosdados,nãoéum
sistemacompletodeseguran ça,jáqueumatacantepodeinterceptaros
dadosesimplesmenterefazeraassinatura. ANF-econtatambémcom
aproteçãooferecidapeloHTTPS,demaneiramútua,ouseja,ocliente
deveapresentarseucertificadoparaoservidorantesdepoderrealizara
comunicação.
O WS-Securitypossuiumsistemabemricoparaproverseguran ça,tanto
em termos de confidencialidade (como mencionado nobox Segurança de
informações e a NF-e ), quanto em termos de autenticação/autorização. O
sistema de autenticação funciona com diversos mecanismos (inclusive customi-
zados), sendo os mais conhecidos: autenticação via token SAML (Security As-
sertion Markup Language), via ticketKerberos, via fornecimento de usuário
e senha (tanto com senha em texto puro quanto com hash) e via certificado
X.509. Alémdisso,o WS-Securitypossuiváriasextensões(como WS-Trust,
WS-SecureConversation, WS-Federationeoutras)paraomecanismocomo
umtodo,demaneiraqueestasextensõesendere çamalgunsdosproblemasquea
própriaespecificação WS-Securitynãofaz.
Oladonegativodo WS-SecurityparadesenvolvedoresJavaéqueoJAX-WS
nãooferecepadroniza çãoparaestaespecifica ção. Issofazcomqueodesenvolvi-
mentodeservi çossegurossejadependentedo frameworkutilizado,ouatémesmodo
152
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 169

CasadoCódigo Capítulo6. Segurançaemwebservices
servidorutilizado(dependendodacapacidadedestedemodifica çãodo framework
deserviçosutilizados).
O WS-Securityfuncionaemconjuntocomasespecifica ções WS-Policy
e WS-SecurityPolicy. Estas duas especificações têm por objetivo, respec-
tivamente, estabelecer políticas gerais a respeito de segurança, SLA, qualidade
de serviço, confiabilidade etc.; e estabelecer, especificamente, quais são as po-
líticas de segurança aplicáveis a um determinado serviço. A especificação da
WS-Policypodeserencontradaemhttp://www.w3.org/TR/ws-policy-attach/,e
ada WS-SecurityPolicy,emhttp://bit.ly/Y40i4H. Cadaumaérazoavelmente
grandeecomplicada—recomendoaleituraapenasemcasodenecessidade.
Utilizando as definições de políticas
A WS-Policy,porsisó,érazoavelmentefácildeserutilizada(postoquese
trataapenasdeuma“cápsula”paraoutrasespecificações). Paradefinirumapolí-
ticadeseguran ça,bastaincluiroelemento Policyemumaposi çãodoseuWSDL
(preferencialmente,apósadefini çãodeservi ço,oumesmoemumWSDLàparte)
edefinirumIDparaessapolítica. Porexemplo,paradefinirumapolíticaemum
WSDLàparte,pode-sedefinirodocumentotodoassim:
<wsdl:definitions
targetNamespace="http://servicos.estoque.knight.com/"
xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
xmlns:wsp="http://schemas.xmlsoap.org/ws/2004/09/policy"
xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-
200401-wss-wssecurity-utility-1.0.xsd">
<wsp:Policy wsu:Id="DefaultSecureServicePolicy">
<!-- conteúdo da política -->
</wsp:Policy>
</wsdl:definitions>
Note que a definição desse ID é, na verdade, originária de umXML
Schema de apoio, localizado em http://docs.oasis-open.org/wss/2004/01/
oasis-200401-wss-wssecurity-utility-1.0.xsd.
Dentrodoelemento Policy,existeumconjuntodeelementosquepodeser
utilizado,ondeosmaisimportantessão All(todos)e ExactlyOne(exatamente
um).
Esteselementossãoutilizadosparaquesejapossívelcriarcombina çõesdepolí-
ticasaplicáveis.Comoosprópriosnomesindicam,doselementosencapsuladosem
153
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 170

6.5. ConhecendoWS-Security CasadoCódigo
ExactlyOne,exatamenteumdeveseratendidoporumarequisi ção.Jádoselemen-
tosencapsuladosem All,todasaspolíticascompreendidasdevemseratendidas.
Paraquepossamosdefinirumservi çoseguro,váriasquestõesdevemsercon-
sideradas: qualprotocolodetransporteseráutilizado? Emcasodeintercepta ção
damensagemporumatacante,eleserácapazdeinterpretarosdadospassados?
Sendoounãocapazdeinterpretaressesdados,eleserácapazdereenviararequi-
sição,passando-sepeloclientelegítimodoservi ço?Equantoaoservidor,terápro-
teçãosuficienteparaqueumasenhanãosejainterceptadaaochegarnoservidor?
Equantoaumambientemaisamplo,deváriosservi ços,comogarantirqueumelo
fracodeumacomunica çãofeitaentreváriosservi çosnãoacabecomprometendoa
segurançadetodos?
Vamosrevisaraarquiteturadasaplica çõesdaKnight.comeentenderoqueserá
feito:
Figura6.5:Arquiteturadasaplica çõesknight.com
Comovocêpôdeconferirnafigura6.5,nossoservi çodeusuáriosdeveráperma-
necerisoladodorestantedasaplica ções,demaneiraquesejapossívelalterarqual-
154
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 171

CasadoCódigo Capítulo6. Segurançaemwebservices
quercoisano back-enddoserviçodeusuários(lembre-sedeque,mantendoocon-
trato,detalhesdaimplementa çãodoservi çosãoapenasdetalhes).
Nessaarquitetura,portanto,váriosdesafiosestarãopresentes,pelanaturezade
comunicaçõesentreosdiversosservi ços.Vamoscome çarrespondendoaquestões
fundamentais,relativasapenasaonossoservi çodeestoquedelivros. Depois,nos
concentraremosnoecossistemadasaplica ções.
NossoserviçoutilizaHTTPcomocamadadetransporte.Assim,omelhorme-
canismoquepodemosutilizarpararealizaraprote çãodessacamadaéoSSL,trans-
formandonossoservi çoemHTTPS.Issoiráimpediroatacantedeinterpretaros
dadostrafegados.
Paraimpediroatacantedereenviaressesdados,utilizaremosummecanismode-
finidona WS-Security,chamado Timestamp.Estemecanismodefineumajanela
detempoduranteoqualarequisi çãoseráválida(sendoautomaticamenteinvalidada
seestiverforadessajanela).Essajaneladetempoéinformadapeloclienteparaoser-
vidor.Comoessesdadosserãotrafegadosdemaneiraencriptada(pelomecanismo
doHTTPS),umatacantenãotemcomomodificá-los.
Quantoàprote çãodosdados,nossoservi çoestarácomprometido,desdejá,a
nãorecebersenhasemestadopuro,masapenasaquelasquepassarempormeca-
nismode hashing.Issofarácomquesejaimpossívelreverteroprocesso,eoservidor
deverácompararapenasos hashesdassenhas,enãoassenhasemestadopuro.
Nocasodoambientemaisamplo,oidealseriaqueutilizássemos tokens SAMLou
Kerberos,demaneiraqueoservi çonuncativesseacessoàssenhasdosusuários,
emformatoalgum.Noentanto,parafinsdesimplicidade,utilizaremospassagemde
usuárioesenha(esta,tratadacom hash),eeumostrareicomoutilizarcriptografia
dechavepúblicaeprivadaparatrafegarestesdados.
Aplique políticas de transporte
Paracomeçarautilizarasdefini çõesdepolíticasdeseguran ça,precisamos“in-
crementar”nossoWSDLcomo namespacedessaspolíticas. Este namespaceéo
http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702,eeledeixaráoWSDL
quevimosanteriormenteassim:
<wsdl:definitions
targetNamespace="http://servicos.estoque.knight.com/"
xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
xmlns:wsp="http://schemas.xmlsoap.org/ws/2004/09/policy"
xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-
155
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 172

6.5. ConhecendoWS-Security CasadoCódigo
200401-wss-wssecurity-utility-1.0.xsd"
xmlns:sp="http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702">
<wsp:Policy wsu:Id="DefaultSecureServicePolicy">
<!-- conteúdo da política -->
</wsp:Policy>
</wsdl:definitions>
Feitaestamodifica ção,incluiremosasdefini çõesemrela çãoaomecanismode
transporte.Comovocêjáviuanteriormente,amelhormaneiradeprotegernossos
serviçoséutilizandooHTTPS.Noentanto,osclientesdesseservi çoprecisamsaber
dessedetalhe,então,vamosadicionaradefini çãodeusodoHTTPSporpartedo
servidorutilizandoas tags TrasportTokene HttpsToken.Essasdefini çõessão
instaladasdentrodeumadefini çãomaisgenérica,relativaaomecanismodetrans-
porte,queéa tag TransportBinding.Dessaforma,adefini çãoficaassim:
<!-- Definições de namespaces omitidas -->
<wsp:Policy wsu:Id="DefaultSecureServicePolicy">
<wsp:ExactlyOne>
<wsp:All>
<sp:TransportBinding>
<wsp:Policy>
<sp:TransportToken>
<wsp:Policy>
<sp:HttpsToken RequireClientCertificate="false" />
</wsp:Policy>
</sp:TransportToken>
</wsp:Policy>
</sp:TransportBinding>
</wsp:All>
</wsp:ExactlyOne>
</wsp:Policy>
Definições de políticas, a tag Exactly One e All
Você deve ter notado que, nas definições de políticas, a tag
ExactlyOneencapsulaa tag All.Averdadeéquearazãoparaissonão
estáexplícitanadocumentação—massabe-seque,seestas tagsnãoti-
veremesseformato,oJBossWSeoApacheCXF(mecanismosutilizados
noJBossAS7)nãoconseguemdetectarcorretamenteasconfigura ções.
156
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 173

CasadoCódigo Capítulo6. Segurançaemwebservices
Portanto, ao incluir atag HttpsToken, fica definido que o cliente deve
utilizar o HTTPS como mecanismo de transporte. Lembre-se de que o
HTTPS utiliza certificados para garantir a segurança. Neste caso, o atributo
RequireClientCertificateserveparaassinalarseénecessárioounãoqueo
clienteenvieoprópriocertificado(nestecaso,nossoWSDLdemonstraquenãoé
necessário).
Opróximopassoérealizaradefini çãodeummecanismoquenosprotejacon-
tra replay attacks,ouseja,algoqueimpe çaqueumatacanteinterceptearequisi-
çãoeareenvieparaoservidor.Nestecaso,podemosutilizarumadefini çãodeum
timestamp,ouseja,operíododuranteoqualamensageméválida.Paraisso,utili-
zamosa tag IncludeTimestamp,diretamentenadefini çãopolíticasdetransporte.
Esta tagiráforçaroclienteaincluirumcabe çalho(ouseja,conteúdodentrodatag
Header)contendoesteperíodo.Adefini çãodepolíticasficarádestaforma:
<!-- Definições de namespaces omitidas -->
<wsp:Policy wsu:Id="DefaultSecureServicePolicy">
<wsp:ExactlyOne>
<wsp:All>
<sp:TransportBinding>
<wsp:Policy>
<sp:TransportToken>
<wsp:Policy>
<sp:HttpsToken RequireClientCertificate="false" />
</wsp:Policy>
</sp:TransportToken>
<sp:IncludeTimestamp/>
</wsp:Policy>
</sp:TransportBinding>
</wsp:All>
</wsp:ExactlyOne>
</wsp:Policy>
Porúltimo,incluímosumadefini çãodequeordemomecanismodeveráefetuar
oprocessamentodoscabe çalhosdamensagem.Incluímosestedadocasodesejemos
passarmaisalgumainforma çãonocabe çalho,eparanãosermoslimitadosemrela-
çãoàordem.Pararemoverestalimita ção,incluímosuma tagdenominada Layout,
contendoa tag Lax:
<!-- Definições de namespaces omitidas -->
<wsp:Policy wsu:Id="DefaultSecureServicePolicy">
157
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 174

6.5. ConhecendoWS-Security CasadoCódigo
<wsp:ExactlyOne>
<wsp:All>
<sp:TransportBinding>
<wsp:Policy>
<sp:TransportToken>
<wsp:Policy>
<sp:HttpsToken RequireClientCertificate="false" />
</wsp:Policy>
</sp:TransportToken>
<sp:IncludeTimestamp/>
<sp:Layout>
<wsp:Policy>
<sp:Lax />
</wsp:Policy>
</sp:Layout>
</wsp:Policy>
</sp:TransportBinding>
</wsp:All>
</wsp:ExactlyOne>
</wsp:Policy>
Destaforma,nossomecanismodetransporteestátotalmenteprotegido.Resta,
então,adefini çãoemrela çãoàcamadadeaplica ção,ouseja,comorealizaremosa
proteçãodenossoservi çoforçandooclienteapassarusuárioesenha.
Defina a política de autenticação
Políticasdeautenticaçãoporusuárioesenhasãodenominadas,nojargãoWS-*,
deautenticaçãoporusuárioe token.Váriostiposde token,naverdade,sãopermi-
tidos,masoquenosinteressanomomentoé HashPassword.Estetipode token
érepresentadopelasenha,queépassadaporumalgoritmode hash.Estealgoritmo
segueaseguinteregra:
Password_Digest = Base64 ( SHA-1 ( nonce + created + password ) )
Ouseja,o hashdasenhadeveráserfeitoatravésdaconcatena çãodo nonce,adata
decriaçãoeasenha,propriamentedita. Essesdadostambémserãopassadospara
oservi ço. Oconjuntopassaráporalgoritmode hash SHA-1e,depois,codificada
em Base64.Estealgoritmoirárealizaraprote çãodenossasenhaparaqueelanão
sejapassadaemseuestadopuro(seguindoosprincípiosdaautentica ção Basicdo
HTTPS,porexemplo).
158
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 175

CasadoCódigo Capítulo6. Segurançaemwebservices
Além disso, podemos realizar a definição quanto à nossa vontade de re-
ceber de volta o usuário e senha utilizados para a autenticação. Como não
é necessário, realizamos o ajuste utilizando o atributoIncludeToken, na
tag UsernameToken. Ao utilizar o valor http://docs.oasis-open.org/ws-sx/
ws-securitypolicy/200702/IncludeToken/AlwaysToRecipientnadefiniçãodesteatributo,
informamosaomecanismoquenãoénecessáriodevolveroconjuntousuário/senha.
Pararealizarestasdefini ções,incluímososeguintenanossapolíticadesegu-
rança:
<wsp:Policy wsu:Id="DefaultSecureServicePolicy">
<wsp:ExactlyOne>
<wsp:All>
<!-- Definições do mecanismo de transporte -->
<sp:SignedSupportingTokens>
<wsp:Policy>
<sp:UsernameToken
sp:IncludeToken="http://docs.oasis-open.org/
ws-sx/ws-securitypolicy/200702/IncludeToken/
AlwaysToRecipient">
<wsp:Policy>
<sp:HashPassword />
</wsp:Policy>
</sp:UsernameToken>
</wsp:Policy>
</sp:SignedSupportingTokens>
</wsp:All>
</wsp:ExactlyOne>
</wsp:Policy>
Assim,adefini çãocompletadapolíticadeseguran çafica:
<wsp:Policy wsu:Id="DefaultSecureServicePolicy">
<wsp:ExactlyOne>
<wsp:All>
<sp:TransportBinding>
<wsp:Policy>
<sp:TransportToken>
<wsp:Policy>
<sp:HttpsToken RequireClientCertificate="false"/>
</wsp:Policy>
</sp:TransportToken>
159
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 176

6.5. ConhecendoWS-Security CasadoCódigo
<sp:Layout>
<wsp:Policy>
<sp:Lax/>
</wsp:Policy>
</sp:Layout>
<sp:IncludeTimestamp/>
</wsp:Policy>
</sp:TransportBinding>
<sp:SignedSupportingTokens>
<wsp:Policy>
<sp:UsernameToken
sp:IncludeToken="http://docs.oasis-open.org/ws-sx/
ws-securitypolicy/200702/IncludeToken/AlwaysToRecipient">
<wsp:Policy>
<sp:HashPassword/>
</wsp:Policy>
</sp:UsernameToken>
</wsp:Policy>
</sp:SignedSupportingTokens>
</wsp:All>
</wsp:ExactlyOne>
</wsp:Policy>
Noteoatributo Idnadefiniçãodapolítica.Eleidentificaoconjuntodapolítica
desegurançacomoumtodo.Paraaplicá-la,bastautilizara tag PolicyReference.
Esta tagdeveserutilizadaparareferenciarapolíticaemquestão—oqueéfeito
atravésdoatributo URI.Esta tagpodeserinseridatantoimediatamentedentroda
tag binding,noWSDL,quantonadefini çãodeopera ções. Istoirádiferenciara
aplicaçãodaspolíticas,tantoparatodasasopera çõesdefinidasno binding,quanto
paraalgumaopera çãoespecífica.Nonossocaso,pararealizaraaplica çãoparatodas
asoperações,fazemososeguinte:
<wsdl:binding name="AutoresServiceServiceSoapBinding"
type="tns:AutoresService">
<soap:binding style="document"
transport="http://schemas.xmlsoap.org/soap/http"/>
<wsp:PolicyReference URI="#DefaultSecureServicePolicy"/>
<wsdl:operation name="listarAutores">
<soap:operation soapAction="" style="document"/>
<wsdl:input name="listarAutores">
<soap:body use="literal"/>
160
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 177

CasadoCódigo Capítulo6. Segurançaemwebservices
</wsdl:input>
<wsdl:output name="listarAutoresResponse">
<soap:body use="literal"/>
</wsdl:output>
</wsdl:operation>
</wsdl:binding>
Percebaapresen çada tag PolicyReference,assimcomooatributo URI.
EsteatributodeveráterovalordoIDdapolítica,precedidopor #.Destaforma,o
contratoestápronto.Salvetudo(incluindoasdefini çõesdepolíticasdeseguran ça)
napasta WEB-INF/wsdl,comonomede AutoresService.wsdl.Maistarde,
faremosaimplementaçãodo web servicetrabalharcomestanovaversãodocontrato.
6.6 A justes de infra -estrutura
Alguns ajustes extras, além dos já realizados, são necessários. Você deve
abrir novamente o arquivo standalone.xml e localizar o subsistema
urn:jboss:domain:webservices:1.1. Feito isso, basta determinar quais
sãoasportasquedevemserutilizadasparaoservidorparaservirtantoservi ços
semprote çãoquantocomprote ção. Issoéfeitoatravésdas tags wsdl-porte
wsdl-secure-port,respectivamente(ressaltando,novamente,queesteprocedi-
mentopodeserfeitoapenasparamáquinasdedesenvolvimento. Casooservidor
emquestãosejadeprodu ção,utilizeoJBossCLI).Dessaforma,oconteúdodo
subsistemaficaassim:
<subsystem xmlns="urn:jboss:domain:webservices:1.1">
<modify-wsdl-address>true</modify-wsdl-address>
<wsdl-host>${jboss.bind.address:127.0.0.1}</wsdl-host>
<wsdl-port>8080</wsdl-port>
<wsdl-secure-port>8443</wsdl-secure-port>
<endpoint-config name="Standard-Endpoint-Config"/>
<endpoint-config name="Recording-Endpoint-Config">
<pre-handler-chain name="recording-handlers"
protocol-bindings="##SOAP11_HTTP
##SOAP11_HTTP_MTOM ##SOAP12_HTTP ##SOAP12_HTTP_MTOM">
<handler name="RecordingHandler"
class="org.jboss.ws.common.invocation.RecordingServerHandler"/>
</pre-handler-chain>
</endpoint-config>
</subsystem>
161
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 178

6.6. Ajustesdeinfra-estrutura CasadoCódigo
Em seguida, é necessário configurar a própria aplicação para intercep-
tar as requisições aos serviços, de maneira que aengine de segurança faça
a validação dos dados. A valida ção dos dados de usuário e senha é
feita de maneira programática, através de umcallback instalado especial-
mente para este propósito. Ele é definido através de uma interface chamada
javax.security.auth.callback.CallbackHandler.Porexemplo,parade-
finirmoseste callback,definimosaseguinteclasse:
package com.knight.estoque.servicos.seguranca
import javax.security.auth.callback.*;
public class CallbackSeguranca implements CallbackHandler {
public void handle(Callback[] callbacks) throws IOException,
UnsupportedCallbackException {
}
}
A definição de uso destecallback será colocada num arquivo chamado
jaxws-endpoint-config.xml.Estearquivodeverádefinirumapropriedadees-
pecial,chamada ws-security.callback-handler. EladiráaoApacheCXF
qualclassedeveráserusadapararealizaro callback.Oconteúdodoarquivoseráo
seguinte:
<?xml version="1.0" encoding="UTF-8"?>
<jaxws-config xmlns="urn:jboss:jbossws-jaxws-config:4.0"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:javaee="http://java.sun.com/xml/ns/javaee"
xsi:schemaLocation="urn:jboss:jbossws-
jaxws-config:4.0 schema/jbossws-jaxws-config_4_0.xsd">
<endpoint-config>
<config-name>Endpoint WS-Security</config-name>
<property>
<property-name>ws-security.callback-handler</property-name>
<property-value>
com.knight.estoque.servicos.seguranca.CallbackSeguranca
</property-value>
</property>
</endpoint-config>
</jaxws-config>
162
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 179

CasadoCódigo Capítulo6. Segurançaemwebservices
Masnossaconfigura çãoaindanãoestáfinalizada.Aúltimacoisaquedevemos
fazeréeditaro web servicepararealizaroseguinte:encontrarocontratoquedefi-
nimosmanualmente,encontraradefini çãodo callbackeadaptá-loparaserseguro.
Estasdefiniçõessãodadaspelasanota ções @WebService, @EndpointConfige
@WebContext,respectivamente.
AssumindoqueoWSDLeditadofoisalvonapasta WEB-INF/wsdl,como
nome AutoresService.wsdl,anovadefini çãodaimplementa çãoéfeitadase-
guinteforma:
package com.knight.estoque.servicos;
// imports omitidos
@WebService(portName = "AutoresServicePort",
serviceName = "AutoresServiceService",
targetNamespace = "http://servicos.estoque.knight.com/",
wsdlLocation = "WEB-INF/wsdl/AutoresService.wsdl")
@Stateless
public class AutoresService {
public List<Autor> listarAutores() {
// Implementação omitida
}
}
Notequeasdefini çõesdosatributosdaanota ção @WebServiceforamfeitas
combasenoWSDL: portNameédiretamenteequivalenteàdefini çãode port
(localizadadentroda tag service); serviceNameédiretamenteequivalenteà
definiçãoencontradana tag service; targetNamespaceéaprópriadefini ção
de namespacedoservi ço,encontradana tag definitions;e wsdlLocationé
referenteàlocaliza çãodocontratojáeditado.
O próximo passo é configurar este serviço para trabalhar com ocall-
back implementado anteriormente. Para isso, utilizamos a anota ção
org.jboss.ws.api.annotation.EndpointConfig, onde podemos defi-
nironomedoarquivodeconfigura çãoaserutilizadopararastrearo callbackeo
nomedadefini ção,dentrodestearquivo,aserutilizada. Nonossocaso,devemos
referenciaroarquivo WEB-INF/jaxws-endpoint-config.xml,eadefini ção
Endpoint WS-Security.Aimplementa çãodoservi çoficaassim:
163
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 180

6.6. Ajustesdeinfra-estrutura CasadoCódigo
package com.knight.estoque.servicos;
// imports omitidos
@WebService(portName = "AutoresServicePort",
serviceName = "AutoresServiceService",
targetNamespace = "http://servicos.estoque.knight.com/",
wsdlLocation = "WEB-INF/wsdl/AutoresService.wsdl")
@EndpointConfig(configFile = "WEB-INF/jaxws-endpoint-config.xml",
configName = "Endpoint WS-Security")
@Stateless
public class AutoresService {
public List<Autor> listarAutores() {
// Implementação omitida
}
}
E, finalmente, devemos dizer ao JBoss que este serviço deve ser se-
gurado através de HTTPS (além de arrumar a URL do serviço, posto
que a engine do JBoss AS modificou). Isso é feito através da anotação
org.jboss.ws.api.annotation.WebContext,daseguinteforma:
package com.knight.estoque.servicos;
// imports omitidos
@WebService(portName = "AutoresServicePort",
serviceName = "AutoresServiceService",
targetNamespace = "http://servicos.estoque.knight.com/",
wsdlLocation = "WEB-INF/wsdl/AutoresService.wsdl")
@EndpointConfig(configFile = "WEB-INF/jaxws-endpoint-config.xml",
configName = "Endpoint WS-Security")
@WebContext(secureWSDLAccess = true,
transportGuarantee = "CONFIDENTIAL",
urlPattern = "AutoresService")
@Stateless
public class AutoresService {
public List<Autor> listarAutores() {
// Implementação omitida
}
164
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 181

CasadoCódigo Capítulo6. Segurançaemwebservices
}
Destaforma,oservi çoestáfinalmenteprontoparatrabalharcomseguran ça.
6.7 O callback de verificação da senha
Conforme definido no arquivo jaxws-endpoint-config.xml
(visto em 6.6, você deve agora criar uma classe que fará a verifi-
cação da senha passada pelo cliente. Esta classe deverá se chamar
com.knight.estoque.servicos.seguranca.CallbackSeguranca
e, de acordo com aengine do Apache CXF, deve implementar a interface
javax.security.auth.callback.CallbackHandler. O código inicial
ficaassim:
package com.knight.estoque.servicos.seguranca;
import java.io.IOException;
import javax.security.auth.callback.*;
public class CallbackSeguranca implements CallbackHandler {
public void handle(Callback[] callbacks) throws IOException,
UnsupportedCallbackException {
}
}
Ométodo handleseráinvocadoacadachamadaprotegidadosservi ços.Nesta
invocação,um arrayde callbacksépassadocomoparâmetro. Cada callbacktem
umaresponsabilidadediferente,deacordocomaverifica çãodeseguran çadesejada
(lembre-sedequeépossívelinserirváriasverifica çõesdiferentes).Pararealizarave-
rificaçãodasenha,oApacheCXFforneceumaimplementa çãode Callbackatravés
daclasse org.apache.ws.security.WSPasswordCallback. Parautilizá-la
corretamente,deve-se,portanto,fazer castdeum callback,destaforma:
public void handle(Callback[] callbacks) throws IOException,
UnsupportedCallbackException {
for (int i = 0; i < callbacks.length; i++) {
if (callbacks[i] instanceof WSPasswordCallback) {
165
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 182

6.8. Aatualizaçãodoservi çodeusuários CasadoCódigo
WSPasswordCallback pc = (WSPasswordCallback) callbacks[i];
}
}
}
Aoutilizarestaclasse,deve-serecuperarousuárioquefezarequisi çãoatravés
dométodo getIdentifier.Estemétodoretornauma stringcontendoonomedo
usuário.Apartirdessainforma ção,deve-serecuperarasenhadousuárioeinformá-
laao callback,demaneiraque,pormotivosdeseguran ça,oprogramadornãotem
acessoàsenhainformada.Destaforma,ocódigopodeserimplementadocomo:
public void handle(Callback[] callbacks) throws IOException,
UnsupportedCallbackException {
for (int i = 0; i < callbacks.length; i++) {
if (callbacks[i] instanceof WSPasswordCallback) {
WSPasswordCallback pc = (WSPasswordCallback) callbacks[i];
Usuario usuario = encontreUsuario(pc.getIdentifier());
if (usuario == null)
return;
pc.setPassword(usuario.getSenhaDecodificada());
}
}
}
ComoestamosfalandodeSOAetemosduasaplica çõesdistintas(deusuáriose
degerenciamentodeestoque),ocorretoasefazerébuscarousuárionosistemade
gerenciamentodeusuários,atravésdosservi çosRESTexpostos.Noentanto,preci-
samosrealizaralgumasaltera çõesnele,paraqueissofuncione.
6.8 A atualização do serviço de usuários
Aprimeiramodifica çãoaserrealizadanonossoservi çoéincluirumaopera ção
que recupere o usuário corretamente. Como você viu no capítulo 5, isso deve
serrealizadoapartirdeummétodo GET,ondeo logindousuáriopodeserpas-
sadocomopartedaURL.Alémdisso,tambémvamosrealizaromapeamentone-
cessárioparaquepossamosnosbeneficiardo cachedeusuários, como header
If-Modified-Since.Aversãoinicialdonossométodoficaassim:
@GET
@Path("/{login}")
166
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 183

CasadoCódigo Capítulo6. Segurançaemwebservices
public Response find(@PathParam("login") String login,
@HeaderParam("If-Modified-Since") Date modifiedSince);
Entretanto,existeoproblemadasenha.Noteque,quandorealizamosacria ção
dousuárioanteriormente,salvamosassenhasemsuaformapura(oqueéerrado,do
pontodevistadaseguran ça—procuresempresalvarassenhascomalgumaforma
decriptografiaou,aindamelhor,apliquesistemasde hashesseguros).Comoestamos
usandoSSL,nãonecessariamenteprecisamosmodificarotráfegodasenha;porém,
eugostariadeapresentarummecanismodecriptografiaparailustraralgunsconcei-
tos.
Paraencriptarassenhasqueserãotrafegadas,nossaaplica çãodegerenciamento
deusuáriosdeveaceitarummecanismodechavepúblicaeprivada(gerenciadoma-
nualmente)paraquesejapossívelobtertantoflexibilidadenotratamentodessasse-
nhasquantoseguran ça.
XML Encryption e Jav a
Existeumpadrão(definidopelaW3C— World Wide Web Consor-
tium)paratratamentodecriptografiaemXML,quepodeserencontrado
emhttp://www.w3.org/TR/xmlenc-core/.Essepadrãocontémummeca-
nismoparatratamentodecomunica çõesbaseadasemRSA(ummeca-
nismodecriptografiadechavepública/privada);contudo,realizarouso
dessemecanismoemJavaédemasiadamentecomplicado,eesteautor
nãolocalizounenhummecanismoquefizesseessetratamentodeuma
maneirasatisfatóriaparaalinguagemJava.
UmachavepúblicaRSAtembasicamenteduaspartes, moduluse exponent.Dessa
forma,podemosmodelaratransmissãodessachavepúblicautilizandooseguinte
mapeamentonoJAXB:
package com.knight.usuarios.servicos.seguranca;
// imports omitidos
@XmlAccessorType(XmlAccessType.FIELD)
@XmlRootElement(name = "RSA")
public class RSAPublica {
167
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 184

6.8. Aatualizaçãodoservi çodeusuários CasadoCódigo
private BigInteger modulus;
private BigInteger publicExponent;
}
Observequeambososatributossãomodeladosutilizando BigInteger.Isso
porqueaespecifica çãoRSAdeclaraqueambososvaloressãointeirosmuitograndes
(especialmente modulus).Assim, BigIntegeréamelhorclassepararealizaressa
modelagem.
Nossopróximopassoéalteraraassinaturadométodoparaquesejapossível
receberessamensagem.Porém,notequeexistemsériosproblemas:oprimeiro,os
númerosquesãoutilizadosnachaveRSAsãomuitograndes,enãoficaesteticamente
agradávelutilizá-losemumarequisiçãodotipo GET.Outroproblemaéquenãoé
aconselháveltrafegardadossensíveispelométodo GET,comosenhasouchavescrip-
tográficas,jáqueasinformaçõesfornecidaspor GETtrafegamcomo query strings,
queos browsersarmazenamemhistórico—possibilitandoaumusuárionãoautori-
zadoavisualiza çãodestesdados.Assim,surgeumconflito:estamosrealizandouma
buscadedados,masnãopodemosutilizar GET.
Obviamente,existemmaneirasdetrataresteproblema(transmitindoosdados
dachaveRSAcomo headersHTTP,porexemplo).Noentanto,estecenárioexibealgo
quepodeacontecercommaisoumenosfrequênciaemREST:nemsempreépossí-
velatendertodasasespecifica çõesdemaneiraeficiente. Porexemplo,umabusca
complexadeinforma ções(comoumabuscaporexemplos)poderiaserprejudicada
poressemodelo GET.Destaforma,realizoaquiumaquebradeprotocolo:alteroo
métodoHTTPpara POST.
168
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 185

CasadoCódigo Capítulo6. Segurançaemwebservices
Busca de informações utilizando POST
Nãoéaprimeiravezquealguémfazestamodifica çãoemumaAPI.
Defato,aprópriaAPIdoTwitter,paramencionarumexemplo,temalgo
semelhante,vistoemhttps://dev.twitter.com/docs/api/1.1/post/statuses/
filter.Nestedocumento,édetalhadoquesetratadeumabuscade status
porfiltros—todavia,osfiltrospodemsermuitograndeseseremrejei-
tadosporcomprimentodeURL.
Particularmente,euacreditoqueacomplexidadedebuscaséainda
maisgravedoqueocomprimentodaURL,pelofatodeque query strings
são,naturalmente,desprovidasdeelementos-paiouqualquercoisaque
sugiraumaestruturahierárquica.
Sendoassim,alteramosométodoparateroseguinteformato:
@POST
@Path("/{login}")
public Response find(@PathParam("login") String login,
@HeaderParam("If-Modified-Since") Date modifiedSince,
RSAPublica chaveCriptografica);
Tendoinseridoessadefini çãodométodonainterface,restaimplementarabusca,
propriamentedita. Antesdisso,porém,vouinserirummétodoutilitárionaclasse
querepresentaachavepública,chamado encripta.Essemétodoreceberácomo
parâmetroum arrayde bytes,queconteráodadoasercriptografado,eretornaráuma
String—ouseja,asenhajácriptografadaecodificadacomoalgoritmo Base64.
Paraisso,devoutilizarumaAPIjácontidana Virtual Machine,chamadaJCE—
Java Cryptography Extension.EssaAPIjácontémosmecanismosnecessáriospara
trabalharmoscomcriptografiaemJava,demaneiraquepodemosaproveitá-lana
nossaclasse.
Para nos beneficiarmos dessa facilidade, utilizamos inicialmente a classe
java.security.spec.RSAPublicKeySpec. Esta classe representa a es-
pecificação de uma chave pública RSA perante aengine do JCE. Por ser
apenas uma especificação, precisamos materializar a chave, utilizando a
classe java.security.KeyFactory, que contém um método chamado
generatePublic, que irá criar uma instância condizente com a interface
java.security.PublicKey.
169
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 186

6.8. Aatualizaçãodoservi çodeusuários CasadoCódigo
Apartirdeentão,bastaalimentaromecanismodecriptografiadoJCE,repre-
sentadopelaclasse javax.crypto.Cipher.Estaclassecontém,principalmente,
osmétodos init(queirárealizaraalimenta çãodomecanismodecriptografia)e
doFinal(queirárealizaropróprioprocedimentodecriptografia).Aofinal,utiliza-
mosaclasse org.apache.commons.codec.binary.Base64(doApacheCom-
monsCodec)pararealizaracodifica çãodoresultadoem Base64.
package com.knight.usuarios.servicos.seguranca;
// imports omitidos
@XmlAccessorType(XmlAccessType.FIELD)
@XmlRootElement(name = "RSA")
public class RSAPublica {
private BigInteger modulus;
private BigInteger publicExponent;
public String encripta(byte[] bytes) throws ExcecaoCriptografia {
try {
PublicKey publicKey = criaChave();
Cipher cipher = Cipher.getInstance("RSA");
cipher.init(Cipher.ENCRYPT_MODE, publicKey);
return Base64.encodeBase64String(cipher.doFinal(bytes));
} catch (Exception e) {
throw new ExcecaoCriptografia(e);
}
}
protected PublicKey criaChave() throws InvalidKeySpecException,
NoSuchAlgorithmException {
RSAPublicKeySpec publicKeySpec = new RSAPublicKeySpec(modulus,
publicExponent);
return KeyFactory.getInstance("RSA").generatePublic(publicKeySpec);
}
}
Notequeométodo encriptalançaumaexce ção, ExcecaoCriptografia.
Elafoicriadaparaencapsularasexce çõesparticularesdoJCE(quesãomuitas)em
umaúnica,facilitandoousodaAPI.Suadefini çãoéaseguinte:
170
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 187

CasadoCódigo Capítulo6. Segurançaemwebservices
package com.knight.usuarios.servicos.seguranca;
public class ExcecaoCriptografia extends Exception {
// Construtores herdados de Exception
}
6.9 A implementação do método de busca
A seguir, realizamos a implementação do método de busca na classe
UsuariosService. Para facilitar a busca, criamos umaNamed Query na
classe Usuario,demaneiraaconcentrarnumúnicopontoestabuscaespecífica.
Trata-sedeuma querysimples, quefiltraosusuáriospelo login, comovistona
listagem:
@NamedQueries(
@NamedQuery(
name = "usuario.encontrar.login",
query = "select u from Usuario u where u.login = ?")
)
public class Usuario extends EntidadeModelo implements RESTEntity
Apartirdessecódigo,utilizamoso Entity Managerpararealizarabuscausando
a named querycriada:
public Response find(String login, Date modifiedSince,
RSAPublica chaveCriptografica) {
Usuario usuario;
try {
usuario = em
.createNamedQuery("usuario.encontrar.login", Usuario.class)
.setParameter(1, login).getSingleResult();
} catch (NoResultException e) {
return Response.status(Status.NOT_FOUND).build();
}
// O restante do código...
}
Umavezlocalizadoousuário,éimportanteselembrardeutilizarométodo
detach,contidono entity manager,para“desligar”ousuáriodocontextotransa-
171
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 188

6.9. Aimplementaçãodométododebusca CasadoCódigo
cional.Issoéporque,quandorealizarmosacriptografiadasenha,oprópriousuário
recuperadoseráutilizadoparadevolveroresultadodaconsulta.Porém,sefizermos
essaatualizaçãodasenhanumusuárioaindaconectadoaobanco,asaltera çõesque
fizermosserãoautomaticamentepersistidasnobanco—oquefarácomquerequi-
siçõessubsequentesfalhem.
Realizadooprocedimento,bastaajustarasenhadousuáriocomoasenhajácrip-
tografada(atravésdométodo encriptadaclasse RSAPublica)erealizarospro-
cedimentosjáconhecidosparatratamentode caches.Ocódigocompleto,portanto,
éoseguinte:
public Response find(String login, Date modifiedSince,
RSAPublica chaveCriptografica) {
Usuario usuario;
try {
usuario = em
.createNamedQuery("usuario.encontrar.login", Usuario.class)
.setParameter(1, login).getSingleResult();
} catch (NoResultException e) {
return Response.status(Status.NOT_FOUND).build();
}
em.detach(usuario);
if (modifiedSince != null) {
if (usuario.getDataAtualizacao().after(modifiedSince)) {
criptografarSenhaUsuario(usuario, chaveCriptografica);
return Response.ok(usuario).build();
}
return Response.notModified().build();
} else {
criptografarSenhaUsuario(usuario, chaveCriptografica);
return Response.ok(usuario).build();
}
}
private void criptografarSenhaUsuario(Usuario usuario,
RSAPublica chave) {
try {
usuario.setSenha(chave.encripta(usuario.getSenha()
172
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 189

CasadoCódigo Capítulo6. Segurançaemwebservices
.getBytes()));
} catch (Exception e) {
throw new
WebApplicationException(Status.INTERNAL_SERVER_ERROR, e);
}
}
6.10 R ealize a comunicação entre os dois sistemas
Voltando ao sistema de estoques, devemos implementar na classe
CallbackSeguranca o método encontreUsuario, que deverá realizar a
comunicaçãocomoservi çodeusuários,emREST.
Para fazer isso, no entanto, ele deve ser capaz de prover uma chave pú-
blica para o serviço de usuários e ainda manter uma chave privada. Para re-
alizar a geração destas chaves, podemos novamente recorrer ao JCE e à classe
java.security.KeyPairGenerator.Épossívelinformaraestaclassequalal-
goritmoseráutilizadoparaagera çãodopardechavese,ainda,qualotamanho.Para
geraressaschaves(assumindo2048bitsdecomprimento)esalvá-lasemumarquivo,
porexemplo,temososeguintecódigo:
import java.io.*;
import java.security.*;
public class GeradorChaves {
public static void main(String[] args) throws Exception {
KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA");
kpg.initialize(2048);
KeyPair kp = kpg.generateKeyPair();
Key publicKey = kp.getPublic();
Key privateKey = kp.getPrivate();
ObjectOutputStream oos = new ObjectOutputStream(
new FileOutputStream("public.key"));
oos.writeObject(publicKey);
oos.flush();
oos.close();
oos = new ObjectOutputStream(new FileOutputStream("private.key"));
oos.writeObject(privateKey);
173
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 190

6.10. Realizeacomunicaçãoentreosdoissistemas CasadoCódigo
oos.flush();
oos.close();
}
}
Umavezgeradososarquivos public.keye private.key,temosasnos-
saschavesRSA.Opróximopassoéconstruirumcódigoquesejaadequadoparao
consumodoservi çoREST(lembre-sedequeaclassedevesercompatívelcomaquilo
queéesperadopeloservi çodeusuários).Parafacilitaroprocessodecarregarachave
emmemória,construímosummétodoparacarregarestaticamenteaclasseetam-
bémreferenciá-lanocallback.Ocódigodecargadaclasseéoseguinte(assumaque
oarquivo public.keyestánaraizdodiretóriodefontes):
package com.knight.estoque.servicos.seguranca;
// imports omitidos
@XmlRootElement(name = "RSA")
@XmlAccessorType(XmlAccessType.FIELD)
public class ChaveRSA {
private BigInteger modulus;
private BigInteger publicExponent;
public static ChaveRSA carregar() throws IOException,
ClassNotFoundException {
try (InputStream inputStream = ChaveRSA.class
.getResourceAsStream("/public.key")) {
ObjectInputStream ois = new ObjectInputStream(inputStream);
RSAPublicKey rsaPublicKey = (RSAPublicKey) ois.readObject();
ChaveRSA chaveRSA = new ChaveRSA();
chaveRSA.modulus = rsaPublicKey.getModulus();
chaveRSA.publicExponent = rsaPublicKey.getPublicExponent();
return chaveRSA;
}
}
}
174
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 191

CasadoCódigo Capítulo6. Segurançaemwebservices
Estaclasseseráutilizadaparatrafegarosdadosatéoservi çocorretamente.Na
sequência,bastainserirocódigopararealizaracargadestachaveno callback:
public class CallbackSeguranca implements CallbackHandler {
private static ChaveRSA chaveRSA;
static {
try {
chaveRSA = ChaveRSA.carregar();
} catch (Exception e) {
throw new RuntimeException(e);
}
}
//Restante da implementação...
}
Opróximopassoéescreveraclassequeiráreceberosdadosdoservi çoREST,
ouseja,ousuário:
package com.knight.estoque.servicos.seguranca;
// imports omitidos
@XmlAccessorType(XmlAccessType.FIELD)
@XmlRootElement
class Usuario {
private String nome;
private String login;
private String senha;
private Date dataAtualizacao;
}
Noteapresen çadocampo dataAtualizacao. Estecamponãoéforne-
cido como parte da entidade, propriamente dita. No entanto, existe umhea-
der padronizado pelo HTTP chamadoDate. Nós vamos preencher o campo
dataAtualizacaocomoconteúdodo header Date,demaneiraquetenhamos
ummecanismoparamanterum cachedeusuários.
Alémdisso,observequeasenhavirádeformaencriptada.Podemosincluirum
mecanismo,naprópriaclasse Usuario,capazdedecriptarasenha. Novamente,
175
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 192

6.10. Realizeacomunicaçãoentreosdoissistemas CasadoCódigo
recorremosaoJCE,demaneiraquetudooquetemosquefazerécarregaroarquivo
contendoachaveprivadaeinicializarumainstânciade Cipher,queficarápronta
paradecriptarassenhas.Parafazerisso,bastautilizaroseguintecódigo:
@XmlAccessorType(XmlAccessType.FIELD)
@XmlRootElement
class Usuario {
private String nome;
private String login;
private String senha;
private Date dataAtualizacao;
private static Cipher cipher;
static {
try {
InputStream keyStream = Thread.currentThread()
.getContextClassLoader().getResourceAsStream("private.key");
ObjectInputStream ois = new ObjectInputStream(keyStream);
Key decodeKey = (Key) ois.readObject();
ois.close();
cipher = Cipher.getInstance("RSA");
cipher.init(Cipher.DECRYPT_MODE, decodeKey);
} catch (Exception e) {
throw new RuntimeException(e);
}
}
// getters
public String getSenhaDecodificada() {
try {
return new String(cipher.doFinal(Base64.decodeBase64(senha.
getBytes())));
} catch (Exception e) {
throw new RuntimeException(e);
}
}
}
176
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 193

CasadoCódigo Capítulo6. Segurançaemwebservices
Finalmente,temosqueescreveroclientedoservi çoREST.Comoissojáfoiexi-
bidonocapítulo5,nãovouentraremgrandesdetalhesdaimplementa ção. Basta
quevocêseatenteaalgunsdetalhes;oprimeiroéaautentica ção.Comoelaédotipo
Basic,bastainseriro header Authorizationnarequisiçãocomovalor Basic
eousuárioesenha,separadospordois-pontosecodificadosem Base64.Ouseja,
podemospreparararequisi çãodaseguinteforma:
private static String ENDERECO_SERVICO_USUARIOS =
"https://localhost:8443/soa-cap06-usuarios-0.0.1-SNAPSHOT/services/";
private static String USUARIO = "admin";
private static String SENHA = "admin";
private Usuario encontreUsuario(String login) throws IOException {
Usuario usuario = null;
try {
ClientRequest request = new ClientRequest(ENDERECO_SERVICO_USUARIOS
+ "usuarios/{login}")
.pathParameters(login)
.header("Authorization", getAuth())
.body(MediaType.APPLICATION_XML, chaveRSA)
.accept(MediaType.APPLICATION_XML);
// restante do método encontreUsuario
}
private String getAuth() {
return "Basic "
+ Base64.encodeBytes((USUARIO + ":" + SENHA).getBytes());
}
Saibaqueousuárioesenhanãodeveriamficarcarregadosemmemóriadema-
neirapura;elesestãocolocadosdestaformaapenasparasimplificarocódigo.
Nasequênciadapreparaçãodocódigo,checamoso cachedeusuáriosparasaber
setemoscomoincluiro header If-Modified-Sinceounão.Onosso cachepode
serimplementadocomummapa;noentanto,vocênãodeveconfiarnoservidorpara
mantersempreamesmainstânciadestaclasse. Assim,elefoiincluídodemaneira
estáticanaclasse CallbackSeguranca. Comoissopodeoriginarproblemasde
concorrência,utilizamosum java.util.concurrent.ConcurrentHashMap
177
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 194

6.10. Realizeacomunicaçãoentreosdoissistemas CasadoCódigo
paralidarmelhorcomessaquestão.Assim,todoocódigoparatratamentode cache
ficadestaforma:
private static Map<String, Usuario> cache = new ConcurrentHashMap<>();
private Usuario encontreUsuario(String login) throws IOException {
Usuario usuario = null;
try {
ClientRequest request = new ClientRequest(ENDERECO_SERVICO_USUARIOS
+ "usuarios/{login}")
.pathParameters(login)
.header("Authorization", getAuth())
.body(MediaType.APPLICATION_XML, chaveRSA)
.accept(MediaType.APPLICATION_XML);
if (cache.containsKey(login)) {
usuario = cache.get(login);
request.header("If-Modified-Since",
org.jboss.resteasy.util.DateUtil.
formatDate(usuario.getDataAtualizacao()));
}
ClientResponse<Usuario> response = request.post();
if (response.getStatus() == Status.NOT_MODIFIED.getStatusCode()) {
return usuario;
}
// restante do método encontreUsuario
}
Restaapenasfazerotratamentodedadosemcasodeoservi çoinformarqueos
dadosnãoestãono cacheoudousuárionãotersidolocalizado.Ocódigocompleto
debuscadeusuáriosficaassim:
private Usuario encontreUsuario(String login) throws IOException {
Usuario usuario = null;
try {
ClientRequest request = new ClientRequest(ENDERECO_SERVICO_USUARIOS
+ "usuarios/{login}").pathParameters(login)
.header("Authorization", getAuth())
.body(MediaType.APPLICATION_XML, chaveRSA)
.accept(MediaType.APPLICATION_XML);
178
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 195

CasadoCódigo Capítulo6. Segurançaemwebservices
if (cache.containsKey(login)) {
usuario = cache.get(login);
request.header("If-Modified-Since",
org.jboss.resteasy.util.DateUtil.
formatDate(usuario.getDataAtualizacao()));
}
ClientResponse<Usuario> response = request.post();
if (response.getStatus() == Status.NOT_MODIFIED.getStatusCode()) {
return usuario;
}
if (response.getStatus() == Status.OK.getStatusCode()) {
usuario = response.getEntity(Usuario.class);
Date date = org.jboss.resteasy.util.DateUtil.
parseDate(response.getHeaders().getFirst(
"Date"));
usuario.setDataAtualizacao(date);
cache.put(login, usuario);
return usuario;
}
if (response.getStatus() == Status.NOT_FOUND.getStatusCode()) {
return null;
}
throw new Exception("Usuário não localizado");
} catch (Exception e) {
throw new IOException(
"Não foi possível recuperar as informações do usuário");
}
}
Finalmente, o código do nossocallback de usuários está pronto. Caso
seja necessário acessar dados de segurança no serviço, podemos utilizar o
mecanismo de injeção do Application Server. Para isso, basta injetar uma
instância de javax.xml.ws.WebServiceContext, utilizando a anotação
javax.annotation.Resource:
179
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 196

6.11. TestescomSoapUI CasadoCódigo
import org.apache.ws.security.WSUsernameTokenPrincipal;
//outros imports omitidos
public class AutoresService {
@Resource
private WebServiceContext context;
@PersistenceContext
private EntityManager em;
public List<Autor> listarAutores() {
WSUsernameTokenPrincipal principal =
(WSUsernameTokenPrincipal) context.getUserPrincipal();
System.out.println("O usuário " + principal.getName()
+ " está listando autores");
return em.createQuery("select a from Autor a", Autor.class)
.getResultList();
}
}
Ocódigodoladodoservidorestá,então,completo.Restaagorarealizarostestes
eescreveroclienteparanossoservi ço.
6.11 T estes com SoapUI
Finalmente, podemos realizar os testes a respeito do funcionamento da segu-
rançadaaplica ção. SevocêacessaroconsoledoJBoss,veráumase çãochamada
Webservices.Essase çãocontémquais web servicesestãoemopera çãonosistema.
Sevocêclicarsobre AutoresService,veráaURLdoWSDLjámodificada:
180
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 197

CasadoCódigo Capítulo6. Segurançaemwebservices
Figura6.6:consoledoJBossmostrandooendere çoalteradodoWSDL
Depossedesseendere ço,épossívelacessá-lopelo browserparachecarseocon-
tratoestácorretamenteexposto.
Umavezchecado,podemosprosseguirrumoaostestescomSoapUI.Acria-
çãodoprojeto,inicialmente,éigualàquefizemosanteriormente,ouseja,basta
clicarcomobotãodireitodomousesobre Projects,selecionar New SoapUI
Projecte,então,preencherocampo Initial WSDL/WADL comoendere çodo
WSDL.Feitoisso,aestruturainicialdeprojetosdoSoapUIdeveaparecer:
181
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 198

6.11. TestescomSoapUI CasadoCódigo
Figura6.7:estruturadoprojetonoSoapUI
Aoselecionar Request 1,umacaixachamada Request properties deve
aparecerpoucoabaixo.Nestacaixa,existemduasse ções, Usernamee Password.
Estasduascaixasdevemconterousuárioesenha,respectivamente,deumusuário
existentenoservi çodeusuários.
Figura6.8:Caixacomentradaparausuárioesenha
182
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 199

CasadoCódigo Capítulo6. Segurançaemwebservices
.
Aorealizarduplocliquesobre Request 1,atelacomarequisi ção“crua”deve
aparecer. Deacordocomocontrato,deve-sepreenchertantoousuárioeasenha
darequisi ção,quantoinserirum timestamp. Parapreencherprimeiroousuário,
bastaclicarcomobotãodireitosobrearequisi çãoeselecionaraop ção Add WSS
Username Token. Issodeveabrirumacaixacomotítulo Specify Password
Type.
Nossocontratoespecificaquedesejarecebero digestdasenha,então,selecione
aopção PasswordDigestecliqueemOK.Issodeveráalimentararequisi çãopara
queamesmacontenhaaestruturanecessáriaparapassagemdeusuárioesenha.
Parainseriro timestamp,bastaclicarcomobotãodireitosobrearequisi çãoe
clicarem Add WS-Timestamp.Aofazerisso,oSoapUIabriráumacaixadediálogo
comotítulo Specify Time-To-Live Value ,ouseja,vocêdevefornecercomo
entradaointervalodevalidadedo timestamp,emsegundos. Deixe60ecliqueem
OK.
Noteque,casovocêqueirafazeroutrasrequisi ções,deveráapagarotrechoque
contémo timestamperealizaresseprocedimentonovamente(jáquearequisi ção
temprazodevalidade).
Finalmente,bastaclicarnobotãocomasetaverde(aoladodoendere çodoser-
viço)parasubmeterarequisi ção.Seestivertudocorreto,alistagemdeautoresdeve
aparecer:
Figura6.9:Respostadoservi ço
183
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 200

6.12. Crieoclienteseguro CasadoCódigo
6.12 C rie o cliente seguro
Paracriaroclientesegurodoservi ço,bastaseguirosmesmospassosvistosnoca-
pítulo1,comocomando wsimport. Oqueserádiferenteéamaneiracomoos
cabeçalhosdevemsercriados.Paracriá-los( UsernameTokene Timestamp),re-
alizaremosaintercepta çãodarequisi ção,atravésde HandlersdoJAX-WS.Estes han-
dlersatuamdemaneiraainterceptartantoaentradacomoasaídadarequisi ção,de
maneiraquetemosacapacidadedeutilizaroservi çonormalmente,comofazíamos
antes.
Paracriaro handlerqueinterceptaránossarequisi ção,bastacriarumaclasse
que implemente a interfacejavax.xml.ws.handler.soap.SOAPHandler.
Estainterfacedefineosmétodos close, handleFault, handleMessagee
getHeaders. Destes,vamosnosconcentrarno handleMessage,poisestemé-
todoseráexecutadoantesdeenviarmosarequisi ção.
Ainterfacequeimplementamos, javax.xml.ws.handler.soap.SOAPHandler,
possui um tipo genérico como parâmetro. Utilizamos a interface
javax.xml.ws.handler.soap.SOAPMessageContext como tipo gené-
rico para esta interface. Assim, o métodohandleMessage receberá como
parâmetroumainstânciadestainterface:
package com.knight.estoque.servicos;
// imports omitidos
public class WSSecurityHandler
implements SOAPHandler<SOAPMessageContext> {
@Override
public void close(MessageContext context) {
}
@Override
public boolean handleFault(SOAPMessageContext context) {
return true;
}
@Override
public boolean handleMessage(SOAPMessageContext context) {
return true;
184
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 201

CasadoCódigo Capítulo6. Segurançaemwebservices
}
@Override
public Set<QName> getHeaders() {
return null;
}
}
Quantoàcria çãodos headersdesegurança,vamosutilizaro framework WSS4J
paracriaroscabe çalhos(queéomesmo frameworkutilizadopeloApacheCXFpara
realizarasopera çõesdeseguran ça).Este frameworkconduzoperaçõessobreSOAP
noníveldoXML,oqueotornaidealparaserutilizadodentrodeum handler.
As classes que nos interessam do WSS4J são
org.apache.ws.security.message.WSSecHeader
(que representa o conjunto de cabe çalhos seguros),
org.apache.ws.security.message.WSSecUsernameToken
(que representa o header de usuário/senha) e
org.apache.ws.security.message.WSSecTimestamp (que representa
o timestamp).
Inicialmente, utilizamos WSSecHeader para “instalar” o mecanismo de
segurança. Para isso, utilizamos a interfaceorg.w3c.dom.Document, que
representa o XML da mensagem. Esta informação pode ser obtida a par-
tir da classe javax.xml.soap.SOAPMessage, que, por sua vez, é obtida a
partir de SOAPMessageContext, passado como parâmetro para o método
handleMessage. Para realizar a instalação, então, basta executar o método
insertSecurityHeader,daclasse WSSecHeader:
SOAPMessage message = context.getMessage();
WSSecHeader header = new WSSecHeader();
//obtém o Document da mensagem e insere o cabeçalho seguro
header.insertSecurityHeader(message.getSOAPBody()
.getOwnerDocument());
Feito isso, passamos para o próximo passo: inserir informações de usuá-
rio e senha. Para isso, é preciso ajustar as informações em uma instância de
WSSecUsernameTokenerealizarainstala çãonainstânciade WSSecHeaderque
foicriada.Bastaexecutaroseguinte:
185
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 202

6.12. Crieoclienteseguro CasadoCódigo
WSSecUsernameToken usernameToken = new WSSecUsernameToken();
usernameToken.setUserInfo(username, password);
//realiza o mesmo procedimento, de obter o Document da mensagem
usernameToken.prepare(message.getSOAPBody().getOwnerDocument());
//realiza a inserção do cabeçalho de usuário/senha
usernameToken.appendToHeader(header);
Opcionalmente,podemosutilizarestaclasseparatrabalharcomsenhascodifi-
cadasem Base64,utilizandoométodo setPasswordsAreEncoded.
Finalmente,utilizamosaclasse WSSecTimestampparainseriro headerde ti-
mestamp.Autiliza çãodestaclasseémaissimples:bastaexecutarométodo build,
passandocomoparâmetroo Documentobtidodamensagem(comonasoutrasve-
zes)eainstânciade WSSecHeader.Assim:
WSSecTimestamp timestamp = new WSSecTimestamp();
timestamp.build(message.getSOAPBody().getOwnerDocument(),
header);
Feitoisso,temosqueproverumretornoparaométodo(quedeveserdotipo
boolean). Esteretornoé true,casooprocessamentodarequisi çãodevaconti-
nuar,ou false,casodevaparar.Issosetornarámaisclaroquandorealizarmosa
instalaçãodo handlernosistemacliente.
Note que este método será executado tanto na saída de dados (ou seja, no
enviodeXMLparaoservidor)quandonaentrada(ouseja,norecebimentode
XMLdoservidor). Paraexecutarestemétodoapenasnasaídadedados,utiliza-
mosumavariávelpresentenocontexto,queéreferenciadaapartirdaconstante
javax.xml.ws.handler.MessageContext.MESSAGE_OUTBOUND_PROPERTY.
Estavariávelédotipo Boolean,tendoovalor truecasoocontextosejadesaída
dedadose falsecasosejadeentrada.
Destaforma,ocódigocompletodessaclasseficaassim:
package com.knight.estoque.servicos;
import java.util.Set;
import javax.xml.namespace.QName;
import javax.xml.soap.*;
import javax.xml.ws.handler.*;
import javax.xml.ws.handler.soap.*;
186
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 203

CasadoCódigo Capítulo6. Segurançaemwebservices
import org.apache.ws.security.*;
import org.apache.ws.security.message.*;
public class WSSecurityHandler
implements SOAPHandler<SOAPMessageContext> {
private String username;
private String password;
private boolean encoded;
public WSSecurityHandler(String username, String password) {
this(username, password, false);
}
public WSSecurityHandler(String username, String password,
boolean encoded) {
this.username = username;
this.password = password;
this.encoded = encoded;
}
public void close(MessageContext context) {}
public boolean handleFault(SOAPMessageContext context) {
return true;
}
public boolean handleMessage(SOAPMessageContext context) {
Boolean outbound = (Boolean) context
.get(MessageContext.MESSAGE_OUTBOUND_PROPERTY);
if (outbound) {
try {
SOAPMessage message = context.getMessage();
WSSecHeader header = new WSSecHeader();
header.insertSecurityHeader(message.getSOAPBody()
.getOwnerDocument());
WSSecUsernameToken usernameToken = new WSSecUsernameToken();
usernameToken.setUserInfo(username, password);
usernameToken.setPasswordsAreEncoded(encoded);
187
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 204

6.12. Crieoclienteseguro CasadoCódigo
usernameToken.prepare(message.getSOAPBody()
.getOwnerDocument());
usernameToken.appendToHeader(header);
WSSecTimestamp timestamp = new WSSecTimestamp();
timestamp.build(message.getSOAPBody().getOwnerDocument(),
header);
} catch (WSSecurityException | SOAPException e) {
e.printStackTrace();
return false;
}
}
return true;
}
public Set<QName> getHeaders() {
return null;
}
}
Agora,parainstalareste handlernocliente,temosquerealizarumasériedepas-
sos.Aprimeira,éinstanciaroservi çodeautores,comoanteriormente:
AutoresService service = new AutoresServiceService()
.getAutoresServicePort();
Com a engine JAX-WS, podemos realizar ocast do nosso port (no caso,
AutoresService)para javax.xml.ws.BindingProvider.Estainterfaceirá
conterumasériedemétodosúteisparatratamentodebaixonívelsobreoconsumo
donosso web service.Umdosmétodosdessainterfaceé getHandlerChain,que
irádevolverumalistade handlersparaoservi ço.Umavezretornadaestalista,basta
queadicionemosumainstânciadonossopróprio handlereutilizemosométodo
setHandlerChain,destaforma:
AutoresService service = new AutoresServiceService()
.getAutoresServicePort();
BindingProvider bindingProvider = (BindingProvider) service;
List<Handler> handlerChain = bindingProvider.getBinding()
188
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 205

CasadoCódigo Capítulo6. Segurançaemwebservices
.getHandlerChain();
handlerChain.add(new WSSecurityHandler("alexandre", "alexandre"));
bindingProvider.getBinding().setHandlerChain(handlerChain);
List<Autor> autores = service.listarAutores();
for (Autor autor : autores) {
System.out.println(autor.getNome());
}
Pararealizarmosoconsumodoservi ço,noentanto,aindarestarealizarumúl-
timopasso.Comonossoservi çoéexpostoviaHTTPS,precisamosincluirno clas-
spathmecanismosquesejamcapazesdetrataresteaspecto.Paraisso,realizamosa
adiçãodedoisJARsdoApacheCXFao classpath: cxf-rt-frontend-jaxwse
cxf-rt-transports-http.
O github do projeto
Para checar esse e outros aspectos do projeto, consulte ogithub
que contém os códigos-fonte. O projeto do cliente, especifica-
mente,estápresenteemhttps://github.com/alesaudate/soa/tree/master/
soa-cap06-estoque-cliente.
Finalmente, aoexecutarmosocódigo, oApacheCXFseráautomaticamente
instalado,provendosuítesparacomunica çãoviaHTTPSeoutrosaspectos. Desta
forma,aprimeiraexecu çãodoclienteserálenta,aopassoqueexecu çõessubsequen-
tesserãofeitasdemaneiramaisrápida.Aoexecutarestecódigo,obtemosumasérie
de logs,nasaídapadrãodoconsole.Finalmente,então,obtemososdadosqueesta-
mosesperando:
Paulo Silveira
Adriano Almeida
Vinicius Baggio Fuentes
Destaforma,então,estáconcluídoocliente.Vocêpodeefetuarnovostestesfa-
zendoainclusãodenovosusuáriosnosistemadeusuários,econsultandoesteser-
viçoutilizandoousuáriorecém-criado.Casoestejatudofuncionando,vocêconcluiu
comsucessoaetapadeadi çãodeseguran çaàsuaaplica çãoorientadaaservi ços.
189
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 206

6.13. Sumário CasadoCódigo
6.13 S umário
Nestecapítulo,vocêcomeçouadesfrutardosbenefíciosdeumaaplica çãoorientadaa
serviços.Aorealizaracomunica çãoseguraentreseusservi ços,vocêestádesfrutando
deflexibilidadeconsiderável,postoqueaimplementa çãodoservi çodeusuáriosnão
afetaemnadaaimplementa çãodoservi çodetratamentodeestoquedasualivraria.
Ocaminhoatéaquifoiárduo. Vocêpôdeconferir,nestecapítulo,váriasdas
formasdeseguran çaaplicáveistantoaservi çosRESTcomoaservi çosWS-*.Você
pôdeconferirdetalhesdefuncionamentodeservi çosRESTcomHTTP Basice
Digest,bemcomoalgumasdasformasdeseguran çapresentesnaespecifica ção
WS-Security.
Seuspróximospassos,agora,estarãorelacionadosàmanuten çãodeproblemas
maisligadosànaturezadessasaplica ções,comoamanuten çãodaescalabilidade,
estabilidadeeoutrosrequisitosfuncionaisenão-funcionais.
190
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 207

Capítulo7
DesignPatternseSOA
“Não são as ervas más que sufocam a boa semente e sim a negligência do lavrador”
–Confúcio
Graçasavocê,aKnight.comestácrescendo.Cadavezmais,novosclientesvão
aparecendo,esempreelevandoousodasAPIsdoseusistema. Comisso,ospri-
meirosproblemasvãoaparecendo:algunssistemassaemdoar(causandoafalhade
outros),amanuten çãodosservi çoscomeçaasetornarumproblemaetc.Enquanto
buscaasolu ção,vocêsedeparacomumcatálogode Design PatternsparaSOA.Você
decidedarumaolhada.
7 .1 I ntegração versus SOA
Doscatálogosdedesign patternsSOA,omaisnotórioé SOA Design Patterns,de Tho-
masErl[4].Noentanto,muitosdospadrõesapresentadosporelenãoapresentam
detalhesdeimplementa ção,massim,sãodenívelmaisalto,comoaquelesreferentes
àmodelagemdeformatosdedados,protocolosetc.
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 208

7.2. OModeloCanônico CasadoCódigo
IssoporqueSOAnãodizrespeitoadetalhesdeimplementa ção. Nesteponto,
muitosdosdetalhesdecomoimplementarumaarquiteturaorientadaaservi çosse
confundemcomtécnicasdepuraintegra çãodesistemas.Ouseja,fazcomqueSOA
utilizetécnicasdeintegra çãoparaser“fisicalizada”.Noentanto,váriasdastécnicas
aplicáveisaintegraçãodesistemasnãosãoaplicáveisemSOA,oquefazcomque
ambasapenascompartilhemalgumascaracterísticasemcomum,semseremequiva-
lentes.
Figura7.1:RelaçãodeSOAeintegra ção
Paranosmantermosfocadosnaprática,mostrareiaqui design patternsorare-
lacionadosaSOA,orarelacionadosaintegra çãodesistemas. Noteque,pelofato
deseremassuntosquesemisturam(conformemostradonafigura7.1),fazsentido
utilizá-lasemprojetosSOA.Vamosapresentarapenasos design patternsmaisrele-
vantes,edeixoaoencargodoleitorpesquisarnabibliografia design patternsaplicá-
veisacenáriosmaisespecíficos.
7 .2 O M odeloCanônico
OModeloCanônicoéumdos design patternsmaisimportantesdeSOA.Elesin-
tetizaofocodeSOAnareusabilidadeesepara çãoderesponsabilidades,atravésde
192
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 209

CasadoCódigo Capítulo7. DesignPatternseSOA
umatécnicabastantesimples—que,apesardisso,éignoradaemprojetospurosde
integração,sendoumdospontosdedivergênciaentreosdoismodelos.
Paranotaraexistênciaeperceberanecessidadedeummodelocanônico,tome
omodelodearquiteturaqueestásendodesenvolvidoparaaKnight.com:atéagora,
existeumsistemadegerenciamentodeusuárioseumsistemadegerenciamentode
estoques.Casoestesistemaprecisedealgorelacionadoausuários,elenãodesenvolve
opróprio,masreutilizaoquejáexistenosistemadeusuários.
Parapromoverestasepara çãoderesponsabilidades,utiliza-seoModeloCanô-
nico. Atécnicaconsiste,simplesmente,emmanter XML Schemas separadospor
modelodedomínioparatodaaempresa. Destaforma,suponhaoseguinte XML
Schemaparaosistemadeusuários:
<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://www.w3.org/2001/XMLSchema"
xmlns:tns="http://knight.com/usuarios/domain/v1"
targetNamespace="http://knight.com/usuarios/domain/v1">
<annotation>
<documentation>
Schema canônico para o sistema de usuários, versão 1.0
</documentation>
</annotation>
<complexType name="usuario">
<sequence>
<element name="id" type="long" />
<element name="nome" type="string" />
<element name="login" type="string" />
<element name="senha" type="string" />
</sequence>
</complexType>
</schema>
Este XML Schema éfeito antesdodesenvolvimentodosistema. Istoporque
opadrãodáprioridadeparaaintera çãoentreasaplica çõesenvolvidas,aoinvésde
preferirafacilidadedagera çãodedocumentosdeformaautomatizada. Issofará
comqueodesenvolvedortenhaplenocontroledasintera çõesnecessáriasentreos
serviços,reduzindocustosdetransforma çõesdedados.
Noteo targetNamespacedeste schema, http://knight.com/usuarios/domain/v1
. Não por acaso, ele recebe o seguinte formato: http://<site da aplicação, sem
193
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 210

7.2. OModeloCanônico CasadoCódigo
www>/<nomedaaplica ção>/<aqueserefere,naaplica ção>/<versão,comomajor
number>.Esteformatonãoéobrigatório,maséidentificadoempiricamentecomo
sendoomaisadequadonamaioriadoscasos. Estetipode namespacevaiajudara
diferenciarosmodelosdedomíniodasaplica ções,bemcomosuasversões.
Umavezdefinidoeste schema(queéchamadode schemacanônico,porperten-
ceràdefini çãodomodelocanônico),elepoderáserreaproveitadoporoutrasapli-
cações.Porexemplo,considereo XML Schema paraosistemadeestoque:
<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://www.w3.org/2001/XMLSchema"
xmlns:tns="http://knight.com/estoque/domain/v1"
xmlns:usuarios="http://knight.com/usuarios/domain/v1"
targetNamespace="http://knight.com/estoque/domain/v1">
<import
namespace="http://knight.com/usuarios/domain/v1"
schemaLocation="usuarios_v1_0.xsd" />
<complexType name="autor">
<sequence>
<element name="id" type="long" minOccurs="0"/>
<element name="dataNascimento" type="date" />
<element name="nome" type="string" />
<element name="usuario" type="usuarios:usuario" />
</sequence>
</complexType>
</schema>
Noteapresen çadoatributo usuarionadefiniçãode autor.Estaéumade-
finiçãoimportadadosistemadeusuários,daíapresen çada tag import. Reali-
zamosadefini çãodo namespacedeusuárioslogonotopo(repareadefini çãoda
tag schema—existeumalinhacontendo“xmlns:usuarios="http://knight.com/
usuarios/domain/v1” ”).Paratratarestesdadoscorretamente,realizamosaimporta-
çãodoconteúdo,dandoao schemaalocalizaçãodeondeo schemadeusuáriosestá.
Destaforma,nãoestamosfazendoqualquerredefini çãodedados,masreaprovei-
tandooquejáexiste.
Paraaproveitarestesdados,podemosdefinirasclassesqueutilizaremosdireta-
menteatravésdestes schemas,utilizandoaajudadeeditorescomooEclipseoupor
ferramentasdelinhadecomandopresentesnaJDK.Porexemplo,pararealizarmos
194
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 211

CasadoCódigo Capítulo7. DesignPatternseSOA
adefiniçãodasclassesutilizandooEclipse,bastaclicarcomobotãodireitoemcima
do schemadesejado,apontarpara Generateeclicarem JAXB Classes...,de
acordocomafigura:
Figura7.2:GerandoasclassesJAXBapartirdosschemas
Feitoisso,bastaselecionaroprojetoondeposicionarasclassesgeradas:
195
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 212

7.2. OModeloCanônico CasadoCódigo
Figura7.3:SelecioneoprojetoondecolocarasclassesgeradaspeloJAXB
Nasequência,eleabriráumajanelaparacustomiza çãodedetalhesdagera ção.
Nãoseimportecomnenhumdosdetalhes,bastaclicarem Finish:
196
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 213

CasadoCódigo Capítulo7. DesignPatternseSOA
Figura7.4:Customiza çãodedetalhesdagera çãodecódigo
Dadoisso,oJAXBemitiráumalertadizendoque,casoalgumaclassegerada
entreemconflitocomumapré-existente,aessaúltimaseráentãosobrescrita.Clique
em Y es:
197
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 214

7.2. OModeloCanônico CasadoCódigo
Figura7.5:AlertadesobrescritadeclassesdoJAXB
Finalmente,oJAXBrealizaráacompila çãodetodosos schemasenvolvidose
criaráasclassesnecessárias:
Figura7.6:EstruturadeclassesgeradaspeloJAXB
Casoqueira,tambémépossívelatingiromesmoresultadoutilizandoumaferra-
mentadaJDKchamada xjc.ParaatingiromesmoresultadoobtidocomoEclipse,
bastautilizarestaferramentafornecendooargumento -dparaespecificarodestino
198
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 215

CasadoCódigo Capítulo7. DesignPatternseSOA
dosarquivosgerados:
$JDK_HOME/bin/xjc -d $WORKSPACE/$PROJETO/$PASTA_DE_FONTES
$WORKSPACE/$PROJETO/schemas/estoque_v1_0.xsd
Porexemplo,emumUbuntu,vocêpodeefetuaralgocomooseguintecomando:
/usr/lib/jvm/java-7-oracle/bin/xjc
-d ~/workspace/soa/soa-cap07-modelocanonico/src/main/java/
~/workspace/soa/soa-cap07-modelocanonico/schemas/estoque_v1_0.xsd
Notequeumadasdesvantagensdestemodeloéqueeledificultaaado çãode
Domain-Driven Design,jáqueasclassesgeradaspodemsersobrescritas(deacordo
comafigura7.2).Noentanto,vocêpodeacharusoparaopadrão Adapterdescrito
pelo Gang of Four[1]—sendoestatécnicaaconselhadaporEricEvans[5].
7 .3 D esenvolvimento contract -first
Umaextensãonaturaldodesenvolvimentodomodelocanônicoéatécnicaconhe-
cidacomodesenvolvimento contract-first. Estatécnicaconsisteemdesenvolveros
WSDLs antesdocódigopropriamentedito,dandoaodesenvolvedortotalcontrole
sobreotráfegodedados.Comovocêviunocapítulo2,existemváriasse çõesase-
remtratadasemWSDLs,elidarcomelasnãoéexatamentefácil.Noentanto,como
vocêpodeconferirnocapítulo6,podesernecessárioobtertotaldomíniosobreos
WSDLsparanãodeixarqueelestedominem.
Obviamente,tambémnãoénecessáriodesenvolvertodooconteúdodoWSDL
manualmente—podemosutilizaraIDEparaajudarnestesentido. Parautilizar
oEclipse,porexemplo,bastaclicarcomobotãodireitosobreapastaondedeseja
colocaroWSDLgerado,apontarpara Neweclicarem Other...:
199
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 216

7.3. Desenvolvimentocontract-first CasadoCódigo
Figura7.7:Menudecria çãodoWSDLpeloEclipse
Feitoisso,bastaselecionaro wizard WSDL File eclicarem Next:
200
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 217

CasadoCódigo Capítulo7. DesignPatternseSOA
Figura7.8:Sele çãodewizardparaWSDL’sdoEclipse
Nasequência,dêumnomeparaoarquivodonovoWSDLecliqueem Next:
201
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 218

7.3. Desenvolvimentocontract-first CasadoCódigo
Figura7.9:DêumnomeparaoarquivoqueiráconterseuWSDL
Finalmente,especifiqueasop çõesparacria çãodoWSDL.Note,nafigura,que
estásendocriadooWSDLparaoservi çodeautores,como namespacehttp://knight.
com/estoque/services/AutoresService/v1.Quantoaoresto,deixecomoestáecliqueem
Finish:
202
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 219

CasadoCódigo Capítulo7. DesignPatternseSOA
Figura7.10:Opçõesdecria çãodoWSDL
Aofinal,oEclipsegerouum templatedoWSDLparavocê.Agora,vocêdeverá
customizarocontratomanualmente. Lembre-sedoquevocêleunocapítulo2e
comecepelase ção types.Nestase ção,crieprimeirooselementosquevãoconter
osparâmetrosdeentradaesaídadoseuservi ço,destaforma:
<wsdl:definitions xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
xmlns:tns="http://knight.com/estoque/services/AutoresService/v1"
xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
name="AutoresService"
targetNamespace=
"http://knight.com/estoque/services/AutoresService/v1">
<wsdl:types>
<xsd:schema targetNamespace=
203
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 220

7.3. Desenvolvimentocontract-first CasadoCódigo
"http://knight.com/estoque/services/AutoresService/v1">
<xsd:element name="listarAutores">
<xsd:complexType />
</xsd:element>
<xsd:element name="listarAutoresResponse">
<xsd:complexType>
<xsd:sequence>
<xsd:element name="out" type="xsd:string" />
</xsd:sequence>
</xsd:complexType>
</xsd:element>
</xsd:schema>
</wsdl:types>
<!-- restante do WSDL -->
</wsdl:definitions>
Agora,restavocêreferenciar,efetivamente,oselementosdoseumodelocanô-
nico.Comoase ção typescontém,naverdade,um XML Schema,bastautilizara
tag import,damesmamaneiracomovimosnadefini çãodopróprio schema.Além
disso,vocêtambémdevecriarumprefixoparao namespaceimportado,porexemplo,
estoque:
<wsdl:types>
<xsd:schema
targetNamespace="http://knight.com/estoque/services/AutoresService/v1"
xmlns:estoque="http://knight.com/estoque/domain/v1">
<xsd:import namespace="http://knight.com/estoque/domain/v1"
schemaLocation="../schemas/estoque_v1_0.xsd" />
<xsd:element name="listarAutores">
<xsd:complexType />
</xsd:element>
<xsd:element name="listarAutoresResponse">
<xsd:complexType>
<xsd:sequence>
<xsd:element name="autor" type="estoque:autor"
maxOccurs="unbounded"/>
</xsd:sequence>
</xsd:complexType>
</xsd:element>
</xsd:schema>
204
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 221

CasadoCódigo Capítulo7. DesignPatternseSOA
</wsdl:types>
Nasequência,vocêdevemodelaraseção messages.Novamente,nãoexistepa-
dronizaçãoparaisso,masoEclipsenosdáumadicademanteronomedaopera ção
ecolocar Requestou Responseaofinaldonomedecada message.Seguindo
estadica,obtemososeguinte:
<wsdl:message name="listarAutoresRequest">
<wsdl:part element="tns:listarAutores" name="parameters" />
</wsdl:message>
<wsdl:message name="listarAutoresResponse">
<wsdl:part element="tns:listarAutoresResponse" name="parameters" />
</wsdl:message>
Feitoisso,modelamosase ção portType. OEclipse,inicialmente,geraase-
guinteestrutura:
<wsdl:portType name="AutoresService">
<wsdl:operation name="NewOperation">
<wsdl:input message="tns:NewOperationRequest" />
<wsdl:output message="tns:NewOperationResponse" />
</wsdl:operation>
</wsdl:portType>
Tudooquetemosquefazeraquiéadaptaronomedaopera çãoedasmensagens
deentradaesaída.Destaforma,obtemososeguinte:
<wsdl:portType name="AutoresService">
<wsdl:operation name="listarAutores">
<wsdl:input message="tns:listarAutoresRequest" />
<wsdl:output message="tns:listarAutoresResponse" />
</wsdl:operation>
</wsdl:portType>
Apróximase çãoé binding.Comoelafazreferênciaa portType,bastaalte-
raronomedaopera çãoe soapActionparaterumvalormaiscondizentecoma
operação listarAutores.Dessemodo,deixamosestase çãodaseguinteforma:
<wsdl:binding name="AutoresServiceSOAP" type="tns:AutoresService">
<soap:binding style="document"
transport="http://schemas.xmlsoap.org/soap/http" />
<wsdl:operation name="listarAutores">
205
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 222

7.3. Desenvolvimentocontract-first CasadoCódigo
<soap:operation
soapAction="AutoresService/ListarAutores" />
<wsdl:input>
<soap:body use="literal" />
</wsdl:input>
<wsdl:output>
<soap:body use="literal" />
</wsdl:output>
</wsdl:operation>
</wsdl:binding>
Finalmente,precisamosmodificarase ção service.Aúnicainforma çãodesta
seçãoqueprecisamosalteraréoendere çodoservi ço.Contudo,quandoformosreali-
zaro deploydesteserviço,éesperadoqueoservidoraltereestase çãoparaoendere ço
efetivo.Portanto,podemoscolocarqualquervalorcomoendere çodoservi ço.Para
deixarestainten çãoexplícita,colocamosalgumvalorqualquer,como ENDERECO:
<wsdl:service name="AutoresService">
<wsdl:port binding="tns:AutoresServiceSOAP"
name="AutoresServiceSOAP">
<soap:address location="ENDERECO" />
</wsdl:port>
</wsdl:service>
Finalmentepodemosgeraraimplementa çãodoservi ço.Poderíamosutilizaro
Eclipseparageraraimplementa ção;contudo,podesermaiscomplicadogeraressa
implementaçãopelaIDEdoquepelaferramentadelinhadecomando.Então,vamos
utilizaro wsimportpararealizaressagera ção.
Ousodo wsimportésemelhanteaodo xjc:
$JDK_HOME/bin/wsimport -s $WORKSPACE/$PROJETO/$PASTA_DE_FONTES
$WORKSPACE/$PROJETO/contracts/AutoresService.wsdl
Aoparâmetro -sinformamosodiretórioondeosarquivos-fontesserãogerados.
Umexemplodecomandoseria:
/usr/lib/jvm/java-7-oracle/bin/wsimport
-s ~/workspace/soa/soa-cap07-contractfirst/src/main/java/
~/workspace/soa/soa-cap07-contractfirst/contracts/AutoresService.wsdl
Issovaigeraraseguinteestrutura:
206
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 223

CasadoCódigo Capítulo7. DesignPatternseSOA
Figura7.11:Estruturageradapelowsimport
Notequeopropósitodo wsimporté,naverdade,gerarclientesparaosservi-
ços. ComoaJDKnãopossuiferramentasparagera çãodeservi çosapartirdestes
contratos,utilizamosainterfacegeradapelo wsimportpararealizaracria çãodo
serviço.Ainterfacequenosinteressa,nocaso,é AutoresService,quepossuio
seguintecódigo:
package com.knight.estoque.services.autoresservice.v1;
// imports omitidos
207
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 224

7.3. Desenvolvimentocontract-first CasadoCódigo
@WebService(
name = "AutoresService",
targetNamespace =
"http://knight.com/estoque/services/AutoresService/v1")
@XmlSeeAlso({
com.knight.estoque.domain.v1.ObjectFactory.class,
com.knight.estoque.services.autoresservice.v1.ObjectFactory.class,
com.knight.usuarios.domain.v1.ObjectFactory.class
})
public interface AutoresService {
@WebMethod(action = "AutoresService/ListarAutores")
@WebResult(name = "autor", targetNamespace = "")
@RequestWrapper(localName = "listarAutores",
targetNamespace =
"http://knight.com/estoque/services/AutoresService/v1",
className =
"com.knight.estoque.services.autoresservice.v1.ListarAutores")
@ResponseWrapper(localName = "listarAutoresResponse",
targetNamespace =
"http://knight.com/estoque/services/AutoresService/v1",
className =
"com.knight.estoque.services.autoresservice.v1."
+ "ListarAutoresResponse")
public List<Autor> listarAutores();
}
Agoraprecisamosimplementarestainterface:
package com.knight.estoque.services.autoresservice.v1;
// imports omitidos
public class AutoresServiceImpl implements AutoresService {
@WebMethod(action = "AutoresService/ListarAutores")
@WebResult(name = "autor", targetNamespace = "")
@RequestWrapper(localName = "listarAutores",
targetNamespace =
"http://knight.com/estoque/services/AutoresService/v1",
className =
208
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 225

CasadoCódigo Capítulo7. DesignPatternseSOA
"com.knight.estoque.services.autoresservice.v1.ListarAutores")
@ResponseWrapper(localName = "listarAutoresResponse",
targetNamespace =
"http://knight.com/estoque/services/AutoresService/v1",
className = "com.knight.estoque.services.autoresservice" +
".v1.ListarAutoresResponse")
public List<Autor> listarAutores() {
// TODO Auto-generated method stub
return null;
}
}
Reparequeestaclasse,agora,precisadaanota ção @WebServiceparaquepossa
serdevidamenteinstalada.Noentanto,antes,énecessáriomoveroscontratosesche-
masparaapasta WEB-INFdoprojeto.Feitoisso,bastaincluirosseguintesatributos:
•endpointInterface: deve conter o nome completamente
qualificado da interface que o servi ço implementa (no caso,
com.knight.estoque.services.autoresservice.v1.AutoresService)
•serviceName: corresponde ao valor do atributoname presente natag
service,noWSDL.Nonossocaso,é AutoresService.
•portName: correspondeaovalordoatributo namepresentena tag port
(queéfilhade service).Nonossocaso,é AutoresServiceSOAP.
•targetNamespace:correspondeao namespacedoWSDL.Nonossocaso,é
http://knight.com/estoque/services/AutoresService/v1.
•wsdlLocation:correspondeaocaminhodoWSDL,dentrodoprojeto.Mo-
vendoapasta contractse schemasparadentrodapasta WEB-INF,o
valornonossocasoé WEB-INF/contracts/AutoresService.wsdl.
Assim,adefini çãodaclassefica:
@WebService(
endpointInterface =
"com.knight.estoque.services.autoresservice.v1.AutoresService",
portName = "AutoresServiceSOAP",
serviceName = "AutoresService",
targetNamespace =
209
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 226

7.4. ServiçosassíncronoscomWS-Addressing CasadoCódigo
"http://knight.com/estoque/services/AutoresService/v1",
wsdlLocation = "WEB-INF/contracts/AutoresService.wsdl")
public class AutoresServiceImpl implements AutoresService {
// implementação da classe
}
Aorealizaro deploydaclasse,oseguintedeveaparecerno consoledoJBoss:
id=com.knight.estoque.services.autoresservice.v1.AutoresServiceImpl
address=http://localhost:8080/soa-cap07-contractfirst-0.0.1-SNAPSHOT
/AutoresService
implementor=com.knight.estoque.services.autoresservice.v1.
AutoresServiceImpl
invoker=org.jboss.wsf.stack.cxf.JBossWSInvoker
serviceName={http://knight.com/estoque/services/AutoresService/
v1}AutoresService
portName={http://knight.com/estoque/services/AutoresService/
v1}AutoresServiceSOAP
wsdlLocation=null
mtomEnabled=false
Quando este conteúdo aparecer, significa que odeployfoi realizado corre-
tamente. Osdadosdoservi çoimplantadopodemserobtidosapartirdehttp:
//localhost:8080/soa-cap07-contractfirst-0.0.1-SNAPSHOT/AutoresService?wsdl
(endereçoinferidoapartirdasinforma çõesdaimplanta ção).
7 .4 S erviços assíncronos com WS-Addressing
Muitasvezes,podesernecessárioinvocarumaopera çãocujoresultadonãopode
seroferecidoimediatamente. Estessãoocasoderelatóriosemitidospelosistema.
Quandoumvolumedeinforma çõesmuitograndedeveserlevantado,geralmenteé
maisinteressanterealizaraopera çãodemaneiraassíncrona,ouseja,oclientefaz
arequisi çãoerecebeimediatamenteumarespostadizendoquearequisi çãoserá
processada. Oservidor,então,iniciaoprocessamentoequandoterminar,invoca
osolicitante.
Aespecifica çãoresponsávelporproverfacilidadesrelacionadasaoendere ça-
mentodemensagenséa WS-Addressing.Comestaespecifica ção,épossívelredi-
recionarmensagens,eéapartirdestaquepodemosinformaraoservidorqualoen-
dereçopararespostadeumadeterminadaopera ção.Assimcomoa WS-Security,
210
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 227

CasadoCódigo Capítulo7. DesignPatternseSOA
a WS-Addressingéativadautilizando WS-Policycomoapoio.Noentanto,as
alteraçõesrealizadaspela WS-AddressingvãopermeartodooWSDL.
Aseguir, vocêveráasalteraçõesnecessáriasparacriarumaopera çãoassín-
cronaparasolicita çãoderelatóriosdecria çãodeautoresnosistemadeestoquesda
Knight.com.
Namespaces
Os namespacesaseremreferenciadosnoWSDLsãoosseguintes: http://www.w3.
org/2007/05/addressing/metadatae http://www.w3.org/2006/05/addressing/wsdl, além
do namespacede WS-Policy, http://www.w3.org/ns/ws-policy.Adefini çãodos na-
mespacesnocontratodoservi çodeautoresficaassim:
<wsdl:definitions xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
xmlns:tns="http://knight.com/estoque/services/AutoresService/v1"
xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:wsam="http://www.w3.org/2007/05/addressing/metadata"
xmlns:wsaw="http://www.w3.org/2006/05/addressing/wsdl"
xmlns:wsp="http://www.w3.org/ns/ws-policy"
name="AutoresService"
targetNamespace=
"http://knight.com/estoque/services/AutoresService/v1">
As mensagens de entrada e saída
Porestarmostratandodeumservi çoassíncrono,oservi çoquereceberáares-
postadarequisi çãonãonecessariamenteseráomesmoqueenviouamesma. No
entanto,amensagemderespostatrafegadapeloservi çoprocessadordarequisi ção
deveser exatamente igualàmensagemqueoservi çoqueareceberáespera.Neste
ponto,torna-sebastanteútilaabordagem contract-first,poistemosahabilidadede
controlaristodemaneirasmaisfáceisdoquepelasanota çõesJAXB/JAX-WS.
Vamos supor a adição de mais uma operação no serviço de autores,
solicitarRelacaoDeAutores.Estaopera çãoterá WS-Addressinghabilitado,
masnãonecessariamentedeverárespondersempredemodoassíncrono,apenas
quandoexplicitamentesolicitadopelocliente.
Asdefini çõesdarequisi çãonovaserãoexatamenteiguaisàsnormais,coma
adiçãodeelementos WS-Addressing. Esteselementosirãopermearasse ções
portTypee binding,bemcomorequereracria çãodeumase çãocontendoa
211
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 228

7.4. ServiçosassíncronoscomWS-Addressing CasadoCódigo
política WS-Addressing.
A seção portType
Aseção portTypedeveráseralteradaparaincluirinforma çõesde actions.Estas
actionsirãodizeraomecanismo WS-Addressingqualométodoparaasquaisas
mensagensdevemserentregues,edevemserdefinidasnasse ções inpute output
do portType,destaforma:
<wsdl:portType name="AutoresService">
<!-- definição de listagem de autores, que permanece inalterada -->
<wsdl:operation name="solicitarRelacaoDeAutores">
<wsdl:input message="tns:solicitarRelacaoDeAutoresRequest"
wsam:Action="AutoresService/solicitarRelacaoDeAutores"/>
<wsdl:output message="tns:solicitarRelacaoDeAutoresResponse"
wsam:Action=
"AutoresService/solicitarRelacaoDeAutoresResponse" />
</wsdl:operation>
</wsdl:portType>
</wsdl:portType>
As actionspodemterqualquervalor—vocêapenasdevecertificar-sedequeelas
sãoúnicas.
A seção binding
Aseção bindingéamaisafetadapelainclusãode WS-Addressing.Como
queremosincluirestaespecifica çãoapenasparaumaúnicaopera ção,incluímosas
informaçõesparausode WS-Addressingedapolíticadeusodamesmaapenas
nadefiniçãodaopera ção solicitarRelacaoDeAutores,destaforma:
<wsdl:binding name="AutoresServiceSOAP" type="tns:AutoresService">
<!-- Definição da operação listarAutores, inalterada -->
<wsdl:operation name="solicitarRelacaoDeAutores">
<soap:operation soapAction="" />
<wsaw:UsingAddressing />
<wsp:PolicyReference URI=
"#WSAddressingAutoresServiceSoapBinding_WSAM_Addressing_Policy" />
<wsdl:input>
<soap:body use="literal" />
212
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 229

CasadoCódigo Capítulo7. DesignPatternseSOA
</wsdl:input>
<wsdl:output>
<soap:body use="literal" />
</wsdl:output>
</wsdl:operation>
</wsdl:binding>
Notequeadefini çãodoatributo soapAction,aqui, deve ser mantida va-
zia. Isto porque pode haver conflitos entre esta informação e as definições de
WS-Addressing.Observe,também,queoelemento UsingAddressingcontém
oatributo required,comvaloriguala false.Esteéumdosmecanismosneces-
sáriosparadesobrigaroclienteapassarinforma çõesrelativasa WS-Addressing.
Casovocêqueiraobrigá-lo,apenasremovaestadeclaraçãoeadeclara çãodeopcional
napolítica,asermostradaaseguir.
A definição da política WS-Addressing
Assimcomoem WS-Security, WS-Addressingtambémrequeradefinição
deumapolíticaparauso. Noentanto,estaébemmaissimples: bastadeclararo
elemento Addressingnapolítica:
<wsp:Policy
xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-
200401-wss-wssecurity-utility-1.0.xsd" wsu:Id=
"WSAddressingAutoresServiceSoapBinding_WSAM_Addressing_Policy">
<wsam:Addressing wsp:Optional="true">
<wsp:Policy />
</wsam:Addressing>
</wsp:Policy>
Perceba,aqui,oelemento Optional,comvalor true.Esteéummecanismo
utilizadoparadesobrigaroclienteatransmitirinforma çõesde WS-Addressing
(ouseja,transformandooservi çoemsíncrono/assíncrono,dependendodarequisi-
çãodocliente).Casovocêqueiraobrigarosclientesasempretransmitiremasinfor-
mações,bastaretirarestadeclara ção.
O receptor da mensagem
Oreceptordasmensagensseráum web servicesimples,comduasaltera ções:o
métodoquereceberáoresultadodarequisi ção(ouseja,o callback)nãodevepos-
suirretorno(ouseja,adeclara ção output)eamensagemdeentradadeveserigualà
213
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 230

7.4. ServiçosassíncronoscomWS-Addressing CasadoCódigo
mensagemdesaídadoservi çoqueoriginaamensagem.Assim,comoarequisi ção
terácomoresultadoumalistadeautores,aentradado callbacktambémseráuma
listagemdeautores.Segueabaixoadefini çãodograndeWSDLdo callback:
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<wsdl:definitions xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
xmlns:tns="http://knight.com/estoque/services/AutoresService/v1"
xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:wsam="http://www.w3.org/2007/05/addressing/metadata"
xmlns:wsaw="http://www.w3.org/2006/05/addressing/wsdl"
xmlns:wsp="http://www.w3.org/ns/ws-policy"
name="AutoresService"
targetNamespace=
"http://knight.com/estoque/services/AutoresService/v1">
<wsdl:types>
<xsd:schema targetNamespace="http://knight.com/estoque/services
/AutoresService/v1"
xmlns:estoque="http://knight.com/estoque/domain/v1" >
<xsd:import namespace="http://knight.com/estoque/domain/v1"
schemaLocation="../schemas/estoque_v1_0.xsd" />
<xsd:element name="solicitarRelacaoDeAutoresResponse">
<xsd:complexType>
<xsd:sequence>
<xsd:element name="autor"
type="estoque:autor"
maxOccurs="unbounded" />
</xsd:sequence>
</xsd:complexType>
</xsd:element>
</xsd:schema>
</wsdl:types>
<wsdl:message name="solicitarRelacaoDeAutoresResponse">
<wsdl:part element="tns:solicitarRelacaoDeAutoresResponse"
name="parameters" />
</wsdl:message>
<wsdl:portType name="AutoresServiceCallback">
<wsdl:operation name="solicitarRelacaoDeAutoresCallback">
<wsdl:input message="tns:solicitarRelacaoDeAutoresResponse" />
</wsdl:operation>
</wsdl:portType>
214
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 231

CasadoCódigo Capítulo7. DesignPatternseSOA
<wsdl:binding name="AutoresServiceCallbackSOAP"
type="tns:AutoresServiceCallback">
<soap:binding style="document"
transport="http://schemas.xmlsoap.org/soap/http" />
<wsdl:operation name="solicitarRelacaoDeAutoresCallback">
<soap:operation soapAction="" />
<wsdl:input>
<soap:body use="literal" />
</wsdl:input>
</wsdl:operation>
</wsdl:binding>
<wsdl:service name="AutoresServiceCallback">
<wsdl:port binding="tns:AutoresServiceCallbackSOAP"
name="AutoresServiceCallbackSOAP">
<soap:address location="ENDERECO" />
</wsdl:port>
</wsdl:service>
</wsdl:definitions>
Agera çãodesteservi ço,deacordocomatécnicamencionadanasele ção7.2,
produzaseguinteinterface:
@WebService(name = "AutoresServiceCallback",
targetNamespace =
"http://knight.com/estoque/services/AutoresService/v1")
@SOAPBinding(parameterStyle = SOAPBinding.ParameterStyle.BARE)
@XmlSeeAlso({
com.knight.estoque.domain.v1.ObjectFactory.class,
com.knight.estoque.services.autoresservice.v1.ObjectFactory.class,
com.knight.usuarios.domain.v1.ObjectFactory.class
})
public interface AutoresServiceCallback {
@WebMethod
@Oneway
public void solicitarRelacaoDeAutoresCallback(
@WebParam(name = "solicitarRelacaoDeAutoresResponse",
targetNamespace =
"http://knight.com/estoque/services/AutoresService/v1",
partName = "parameters")
SolicitarRelacaoDeAutoresResponse parameters);
215
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 232

7.4. ServiçosassíncronoscomWS-Addressing CasadoCódigo
}
Notequeaclasse SolicitarRelacaoDeAutoresResponsefoigeradapor-
queonomedaopera çãoedoparâmetroparaaopera çãosãoincompatíveis. De
qualquerforma,estaclassecontémumalistadeautores;bastaexecutarométodo
getAutor.
T estando com SoapUI
PararealizarostestescomoSoapUI,bastaimportaroprojetonormalmente.Pri-
meiro,elehabilitaráasrequisi çõesparaambasasopera çõesnormalmente.Sevocê
fizerarequisi çãopara solicitarRelacaoDeAutoressemqualquermodifica-
ção,obteráumarespostasíncrona.Parahabilitararequisi çãoassíncrona,vocêdeve
incluirnocabe çalhoasinforma çõesde WS-Addressing.Oconjuntomínimoque
vocêdevepassaré Actione MessageID;parahabilitararequisi çãoassíncrona,
bastapassarcomoparâmetrooelemento ReplyTo.
A Actiondeveráterovalordoqueestánaimplementa çãodoservi ço-nonosso
caso, AutoresService/solicitarRelacaoDeAutores. A MessageID,por
suavez,éoIDdamensagem. Trata-sedeumaimplementa çãodopadrãodein-
tegração Correlation Identifier(http://eaipatterns.com/CorrelationIdentifier.html).
ReplyTo,porsuavez,iráconteroendere çoderetornodarequisi ção.
“O padrão Correlation Identifier”
Ousodeum correlation identifieréimportanteparaqueoremetente
damensagemmantenhaumrastreamentodasmensagensqueenviou.
Numcenárioemqueváriasmensagenssãoenviadaserecebidasdevolta,
o correlation identifieréomecanismoqueoclienteutilizaparasaberdo
quesetrataamensagem.Aimplementa ção,emsi,ébemsimples:trata-
seapenasdeumID(comosefosseoIDdeumalinhaemumbancode
dados),quereferenciacadamensagemdemaneiraúnica.
ArequisiçãodoSoapUIdeveráteroseguinteformato:
<soapenv:Envelope
xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:v1="http://knight.com/estoque/services/AutoresService/v1">
216
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 233

CasadoCódigo Capítulo7. DesignPatternseSOA
<soapenv:Header xmlns:wsa="http://www.w3.org/2005/08/addressing">
<wsa:Action>AutoresService/solicitarRelacaoDeAutores</wsa:Action>
<wsa:MessageID>
4585ee4b-5e25-4e82-a91f-0f79bb330b6a
</wsa:MessageID>
<wsa:ReplyTo>
<wsa:Address>
<!-- Endereço do serviço de callback -->
</wsa:Address>
</wsa:ReplyTo>
</soapenv:Header>
<soapenv:Body>
<v1:solicitarRelacaoDeAutores>
<desde>2012-12-12</desde>
</v1:solicitarRelacaoDeAutores>
</soapenv:Body>
</soapenv:Envelope>
Apósoenviodarequisi ção,aseguinterespostadeveráserexibidanoconsoledo
SoapUI:
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
<soap:Header>
<MessageID xmlns="http://www.w3.org/2005/08/addressing">
urn:uuid:b7a9385d-a1f3-4600-910d-6767002a7da4
</MessageID>
<To xmlns="http://www.w3.org/2005/08/addressing">
http://www.w3.org/2005/08/addressing/anonymous
</To>
<ReplyTo xmlns="http://www.w3.org/2005/08/addressing">
<Address>http://www.w3.org/2005/08/addressing/none</Address>
</ReplyTo>
<RelatesTo xmlns="http://www.w3.org/2005/08/addressing">
http://www.w3.org/2005/08/addressing/unspecified
</RelatesTo>
</soap:Header>
<soap:Body/>
</soap:Envelope>
Issosignificaquearequisi çãofoiaceita.Casooservi çode callbackestejaimple-
mentadocorretamente,algocomooseguintedeveráaparecernoconsoledoJBoss:
217
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 234

7.4. ServiçosassíncronoscomWS-Addressing CasadoCódigo
17:24:40,061 INFO [stdout] (default-workqueue-3) Callback imprimindo:
17:24:40,062 INFO [stdout] (default-workqueue-3) Alexandre Saudate
17:24:40,063 INFO [stdout] (default-workqueue-3) Adriano Almeida
17:24:40,063 INFO [stdout] (default-workqueue-3) Paulo Silveira
Implementando um cliente Java
Finalmente,oúltimopassoécriaroclientequefaráessarequisi ção. Infeliz-
mente,esteéumdospassosmaiscomplexos,jáque,atéomomento,esteautornão
localizounenhumabibliotecaquefa çaestasadapta çõesnarequisi çãodeformasa-
tisfatória.Portanto,arequisi çãodeveráseradaptadadeformaapenassemiautoma-
tizada,utilizando handlers(damesmaformacomofoifeitanotratamentodesegu-
rança).
Oprimeiropassoégeraroclientenormalmente. Depois,faremosusodeuma
feature(ouseja,umaclassequeestende javax.xml.ws.WebServiceFeature)
quefazoreconhecimentodequestõesmaistriviaisrelacionadasa WS-Addressing.
Esta featureé javax.xml.ws.soap.AddressingFeature,edeveserpassada
comoparâmetroduranteaobten çãodarepresenta çãodoservi ço,assim:
service = new AutoresService_Service().
getAutoresServiceSOAP(new AddressingFeature());
Depois,faremosaadapta çãocomo handler.Eledeveendere çarduasquestões
principais:inseriroendere çodoservi çopararespostaassíncronaecuidarparaque
osclientesassíncronosnãotenhamumaexce ção(comooelemento Bodyvemvazio
narequisiçãoassíncrona,o parserJAX-WStentafazero parsee,nãoconseguindo,
lançaumaexce ção).Estaadapta çãoéfeitaatravésdeumamisturadaAPIparatra-
tamentodemensagensSOAPedaAPIdetratamentodeXML-DOM.
Para endereçar estas questões, tudo o que faremos será obter o elemento
Address(quejádeverátersidocolocadopela engineJAX-WS)eobteroprimeiro
elementodocorpodarequisi ção,acrescentando Responseaofinal. Istoéfeito
atravésdocódigo:
private void trataRequisicao(SOAPMessageContext context)
throws SOAPException {
SOAPMessage soapMessage = context.getMessage();
NodeList nodeList = soapMessage.getSOAPHeader().getElementsByTagName(
"Address");
Node node = nodeList.item(0);
218
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 235

CasadoCódigo Capítulo7. DesignPatternseSOA
node.setTextContent(enderecoResposta);
Node requestNode = soapMessage.getSOAPBody().getFirstChild();
String namespace = requestNode.getNamespaceURI();
String nodeName = requestNode.getLocalName() + "Response";
QName qName = new QName(namespace, nodeName);
this.responseQName = qName;
}
Notequeoelementodarequisi çãofoiatribuídoaumavariáveldainstânciado
handler.Quandoestarequisi çãoretornar,oseguinteseráexecutado:
private void trataResposta(SOAPMessageContext context)
throws SOAPException {
SOAPMessage soapMessage = context.getMessage();
soapMessage.getSOAPBody().addChildElement(this.responseQName);
}
Finalmente,aoenviararequisi ção,bastaqueoclienteassíncronoinformeoen-
dereçopararespostaatravésdainstânciado handler.Ocódigodoclienteficaassim:
private static boolean ehAssincrono = true;
private String enderecoResposta =
"http://localhost:8080/soa-cap07-wsaddressing-servidor-0.0.1-SNAPSHOT"
+ "/AutoresServiceCallback";
public static void main(String[] args) {
AutoresService service = null;
if (ehAssincrono) {
service = new AutoresService_Service()
.getAutoresServiceSOAP(new AddressingFeature());
List<Handler> handlerChain = ((BindingProvider) service)
.getBinding().getHandlerChain();
handlerChain.add(new AddressingHandler(enderecoResposta));
((BindingProvider) service).getBinding()
.setHandlerChain(handlerChain);
} else {
219
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 236

7.5. Sumário CasadoCódigo
service = new AutoresService_Service().getAutoresServiceSOAP();
}
List<Autor> autores = service.solicitarRelacaoDeAutores(null);
for (Autor autor : autores) {
System.out.println(autor.getNome());
}
}
Dessaforma,aosubmeterestarequisi ção,ajustandoovalorde ehAssincrono
para true,nadaseráimpressopelocliente—arespostadeveráaparecernoconsole
doJBoss.Seovalorfor false,ovalordosautoresdosistemadeveráaparecerno
consoledocliente.Seuservi çofoihabilitadoparatratamentoderequisi çõesassín-
cronas.
7 .5 S umário
Nestecapítulo,vocêviualgunsdospadrõesdeprojetomaiscomunsemSOA.Você
descobriualgunsdosbenefíciosdodesenvolvimentoorientadoporcontratos(ou
seja,atécnicaconhecidacomo contract-first),assimcomoosbenefíciosde
seterummodelopadronizadoparatratamentodesuasentidadesdenegócio—o
famoso Modelo Canônico.
Finalmente,vocêconheceuumatécnicaparatratamentoassíncronoderequisi-
ções,atravésdaespecifica ção WS-Addressing,eviucomoelapodeteajudarao
realizartratamentodegrandesvolumesdedados.
Noentanto,muitoaindaédesconhecido.Restamuitoaservisto—comoenglo-
barosprincipaispadrõesdeintegra ção,comocoordenarcorretamenteaexecu ção
deváriosserviços,comotratarasespecifica çõesWS-*demaneiramaiseficienteetc.
Paraisso,vocêdeveráconhecerduasdasferramentasmaisfamosasdomundoSOA:
ESB( Enterprise Service Bus)eBPEL( Business Process Execution Language).
220
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 237

Capítulo8
Flexibilizandosuaaplica çãocom
umESB
“O futuro começa com uma simples iniciativa”
–AlbertEinstein
Agoraquevocêjáconheceosmecanismosparaexporsuasaplica çõesdemaneira
orientadaaservi ços,umadúvidavemàmente:comotrabalharcomambientesque
nãosãocompatíveiscomoquejáfoicriadoporvocê?Porexemplo,comointeragir
comumsistemadeCRMproprietário,queexpõe web servicesnopróprioformato?
Comotornarsuaaplica çãoflexívelosuficienteparaincluirfuncionalidadespareci-
dascomasantigas,semquehajanecessidadedemodificarosclientesparaqueeles
enxerguemestasnovasfuncionalides?
Estaseoutrasquestõessãoendere çadaspeloESB( Enterprise Service Bus).Trata-
sedaimplementa çãodeumpadrãodeprojetoSOA(catalogadopor ThomasErl[4])
cujopropósitoéabstrairasimplementa çõesdeservi çosdosclientes,conferindoa
estes,certograudedesacoplamentoemrela çãoàimplementa çãodoservi ço.Istoé
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 238

8.1. ComoinstalaroOracleWebLogiceoOEPE CasadoCódigo
feitoatravésdacapacidadedoESBdeexpôruma interface de servi ço(ouseja,um
contratoqualquer)etransformararequisi çãodoclienteparaestainterfaceemalgo
quesejacompatívelcomaimplementa çãorealdoservi ço.
Comestastransforma ções,oESBconsegueimplementartodos(ouquaseto-
dos)ospadrõesdeprojetodeintegra çãoexistentes(sendooprincipalcatálogo
olivrodeGregorHohpeeBobbyWoolf, Enterprise Integration Patterns: Desig-
ning, Building, and Deploying Messaging Solutions[9],tambémdisponívelemhttp:
//eaipatterns.com/),conferindograndeflexbilidadeàsaplica çõesorientadasaser-
viços.
Nestecapítulo,vocêaprenderáainstalareutilizaro Oracle Service Bus
(OSB),umdosESBsmaispoderososdaatualidade.
8.1 C omo instalar o Oracle WebLogic e oOEPE
OOSBé,naverdade,umaaplica çãoquerodasobreo Application ServerdaOra-
cle,o WebLogic. Portanto,antesderealizarainstala çãodoOSB,vocêdeveins-
talarprimeiroo WebLogic.Alémdisso,parainteragircomo Oracle Service
Bus,érecomendávelquevocêinstale,emconjuntocomo WebLogic,o Oracle
Enterprise Pack for Eclipse —OEPE.Trata-sedeumaversãodoEclipse
comváriospluginsjáhabilitadosparaquevocêpossatrabalharcorretamentecomo
WebLogiceoutrosprodutosdaOracle,comooOSB.
Pararealizarodownloaddo WebLogicdoOSB,vocêdeveiratéapáginade
download do OSB: http://www.oracle.com/technetwork/middleware/service-bus/
downloads/index.html. Lá,vocêencontrarádiversasopçõesdeinstala çãoparao
OSBeseuspré-requisitos.Paratodososprocedimentosaseguir,serãoutilizadosos
componentesdaversão11.1.1.6.0,emJVM32-bitsparaWindows.
Aspectos Legais da instalação do OSB
ParainstalaroOSB,vocêprecisaterusuárioesenhana Oracle T ech-
nology Network(OTN)eaceitarostermosdalicen ça.Tenhaemmentede
quealicen çaparadesenvolvedoreségratuita,masparaquaisqueroutros
usos,não.Emcasodedúvidas,entreemcontatocomaOracle.
Ainstalaçãodo WebLogicedoOEPEébemsimples.Aorealizaro downloaddo
mesmo,bastadarumduplo-cliquesobreoinstalador,oque,apósumbreveperíodo
decarga,vaiabrirsuateladeboasvindas:
222
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 239

CasadoCódigo Capítulo8. FlexibilizandosuaaplicaçãocomumESB
Figura8.1:Teladeboasvindasdainstala çãodoOEPE
Nasequência,serásolicitadaaseleçãodapastaondeo Middleware Homeestará
localizado.CasovocêjápossuaalgumprodutoOracleinstalado,recomendoacria-
çãodeum Middleware Homediferentedosjáexistentes.Casocontrário,bastadeixar
comoestá:
223
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 240

8.1. ComoinstalaroOracleWebLogiceoOEPE CasadoCódigo
Figura8.2:Teladecria çãodoMiddlewareHome
Napróximatela,serásolicitadoumendere çode e-mailparaquevocêpossare-
cebermensagenssobreatualiza çõesdeseguran ça.Comodesenvolvedor,nãoéne-
cessáriofornecerumendereço,evocêpodedesmarcarasele çãodacaixa“Gostaria
dereceberatualiza çõesdeseguran çaatravésdoMyOracleSupport”(vocêdeverá,
alémdisso,marcar“Sim”najanelapop-upqueiráaparecernasequência):
224
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 241

CasadoCódigo Capítulo8. FlexibilizandosuaaplicaçãocomumESB
Figura8.3:Teladesolicita çãoderecebimentodeatualiza çõesdeseguran ça
Aseguir,apareceráumatelaondevocêpodeselecionarqualotipodeinstala ção
desejada—típicaoupersonalizada. Bastadeixarmarcadacomotípicaeclicarem
Próximo:
225
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 242

8.1. ComoinstalaroOracleWebLogiceoOEPE CasadoCódigo
Figura8.4:Teladesele çãodetipodeinstala ção
Apróximatelasolicitaráosdiretóriosnosquaissedesejainstalarosprodutos
selecionados( WebLogic, Coherencee OEPE).Bastadeixarcomoestáeclicarem
Próximo:
226
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 243

CasadoCódigo Capítulo8. FlexibilizandosuaaplicaçãocomumESB
Figura8.5:Teladesele çãodediretórios
Aspróximastelassolicitarãooslocaisparaposicionamentodosatalhos(no
menuIniciardoWindows)eapresentarãoumresumodoqueseráinstalado.Basta
clicarem Próximonasduastelaspararealizarainstala ção.Aofinal,ateladeconclu-
sãodeveserapresentada,comumacaixaparasolicita çãodeexecu çãode quickstart.
Desmarqueestacaixaecliqueem Concluído:
227
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 244

8.2. AinstalaçãodoOSB CasadoCódigo
Figura8.6:Conclusãodainstala ção
8.2 A instalação do OSB
Umavezrealizadoesteprocedimento,oOEPEeo WebLogicestãoinstalados. O
próximopassoéinstalaroOSB.Realizadooseu download,descompacte-oemuma
pastadesuapreferênciae,apartirdoaplicativodelinhadecomando,executeainsta-
laçãofornecendoocaminhodasuaJDK,atravésdoargumento -jreLoc(atenção:
instalesuaJDKemumdiretórioquenãocontenhaespa çosnonome):
Disk1\setup.exe -jreLoc C:\Java\jdk1.7.0_09
Aprimeiratelaserádeboas-vindas. Asegunda,serárelativaàsinstala çõesde
software. Novamente,comodesenvolvedor,vocênãodevesepreocuparcomeste
detalhe,epodeignorarestasatualiza ções:
228
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 245

CasadoCódigo Capítulo8. FlexibilizandosuaaplicaçãocomumESB
Figura8.7:Teladesolicita çãodeatualiza çõesdoOSB
Nasequência,serásolicitadoocaminhodo Middleware Home.Casonadaesteja
marcado,forneçaocaminhodo Middleware Homecriadonainstala çãodoOEPEe
cliqueem Próximo:
229
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 246

8.2. AinstalaçãodoOSB CasadoCódigo
Figura8.8:Sele çãodoMiddlewareHome
Aseguir,seráquestionadoqualotipodainstala ção(típicaoupersonalizada)e
umachecagemdospré-requisitosparautiliza çãodoOSBserárealizada.Casoesta
verificaçãotenhasucesso,oseguintedeveráserapresentado:
230
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 247

CasadoCódigo Capítulo8. FlexibilizandosuaaplicaçãocomumESB
Figura8.9:Verifica çãodospré-requisitos
Verificação de pré -requisitos
Estaverificaçãodepré-requisitosétrivialemplataformasWindows.
Emoutrasplataformas, costumasermaisexigente—devidoàpree-
xistênciadecertasaplicaçõesdoSistemaOperacional,espa ço swapetc.
CasovocêdesejeinstalaroOSBemplataformaLinux,observecomaten-
çãoospré-requisitosparaisto.
Aspróximastelasquestionarãoalocaliza çãodo WebLogicedoOEPE,bemcomo
apresentarãooresumodoqueseráinstalado.Aoclicarem Próximoemambas,a
instalaçãodoOSBteráinício. Setudocorrerbem,aseguinteteladeveráserapre-
sentada:
231
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 248

8.3. ConfiguraçãodoOSB CasadoCódigo
Figura8.10:Finaliza çãodainstala çãodoOSB
Aoclicarem Próximo,umateladefinaliza çãodainstala çãoserámostrada.
Bastaclicarem Finalizar.
8.3 C onfiguração do OSB
Agora,opróximopassoéconfiguraroOSBparafuncionamento. Istoéfeitoatra-
vésdacria çãodeumnovodomíniodo WebLogic, habilitadoparaexecu çãodo
OSB.Antesdefazerisso,noentanto,énecessárioterumbancodedadosinsta-
lado(preferencialmente,Oracle)eexecutarumaferramentadeconfigura çãocha-
mada Repository Creation Utility —RCU.Estaferramentapodeserob-
tidanapáginade downloadsdo Oracle SOA Suite -http://www.oracle.com/
technetwork/middleware/soasuite/downloads/index.html.
Aorealizaro downloaddoRCU,descompacte-oemumapastadesuapreferência
232
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 249

CasadoCódigo Capítulo8. FlexibilizandosuaaplicaçãocomumESB
e,nasequência,acesseapasta BINeexecuteoarquivo rcu.bat(emambiente
Linux,apenas rcu).Apósateladeboasvindas,umateladesele çãodecria çãoou
remoçãodeesquemasaparecerá.Deixe Criarselecionadoecliqueem Próximo.
Apróximatelaquestionaráarespeitodasinforma çõesdobanco. Assumindoum
banconaprópriamáquina,dotipo Oracle XE,vocêdeverámanterconfigurações
semelhantesàsseguintes:
Figura8.11:Teladeentradadeconfigura çõesdebancodedados
Notequeénecessáriofornecerumusuáriocomprivilégios DBAou SYSDBA.
ParaumbancodedadosOracleXE,porexemplo,esteusuárioé SYS.
Nasequência,oRCUiráiniciarostestesparaverificaracompatibilidadedo
bancodedados.Noteque,paraumbancodedadosOracleXE,umalertadecom-
patibilidadeéemitido.
233
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 250

8.3. ConfiguraçãodoOSB CasadoCódigo
Figura8.12:AlertadecompatibilidadecomoOracleXE
EstealertaocorreporqueoOracleXEnãoétotalmentecompatívelparauma
instalaçãodeprodu ção,maséaceitávelparaumamáquinadedesenvolvimento.
Opróximaetapaéselecionarotipodeprepara çãodobancodedadosquedeverá
serrealizado.ParaoOSB,vocêdevemarcaraop ção Infraestrutura SOA:
234
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 251

CasadoCódigo Capítulo8. FlexibilizandosuaaplicaçãocomumESB
Figura8.13:Seleçãodeconfigura çãodebancodedados
Emseguida,podemosrealizaradefini çãodassenhasdosesquemas(noOracle
XE,écriadoumusuárioporesquema).Sugiromanteramesmasenhaparatodosos
esquemas,conformeaimagem:
235
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 252

8.3. ConfiguraçãodoOSB CasadoCódigo
Figura8.14:Defini çãodassenhasdosesquemas
Finalmente,bastaseguirasinstru çõesatéofinalparaterminaradefini çãodo
formatodobancodedados.
Agora, você deve configurar o OSB. Para isso, basta executar o programa
config.cmd,localizadonapasta common\bindodiretóriodo WebLogic.Assu-
mindoquevocêmanteveosdiretóriospadronizadosatéagora,esteprogramaestará
localizadonapasta C:\Oracle\Middleware\wlserver_10.3\common\bin.
Feitoisso,oconfiguradorirásolicitaracria çãodeumnovodomínio.Aoclicarem
Próximo,aseguinteteladeveráaparecer:
236
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 253

CasadoCódigo Capítulo8. FlexibilizandosuaaplicaçãocomumESB
Figura8.15:CriaçãododomínionoWebLogic
Para uma máquina de desenvolvimento, basta assinalar a opção Oracle
Service Bus for developers (asdependênciasdesteserãoautomaticamente
assinaladas).
Aseguir,vocêdevefornecerumnomeparaodomínio.Sugirocriarumdomínio
comnome osb_domain:
237
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 254

8.3. ConfiguraçãodoOSB CasadoCódigo
Figura8.16:Nomeandoodomínio
Nasequência,vocêdevecriarumasenhaparaousuário weblogic.Estasenha
deveseralfanumérica,ouseja,conterpelomenosumnúmeroeumaletra.
Opróximopassoéselecionaromododeinicializa çãodo WebLogiceaJDKde
operação. Novamente,paramáquinasdedesenvolvimento,érecomendadodeixar
asopçõespadrão,istoé,manteremmododedesenvolvimentoecomaJDKSun:
238
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 255

CasadoCódigo Capítulo8. FlexibilizandosuaaplicaçãocomumESB
Figura8.17:Sele çãodomododeinicializa çãoeJDK
Apróximatelapedeasinforma çõesdebancodedados.Oesquemasolicitadoé
DEV_SOAINFRA,ouseja,vocêdevefornecerasinforma çõesquesejamcompatíveis
comaquelasutilizadasnadefini çãodesteesquema:
239
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 256

8.3. ConfiguraçãodoOSB CasadoCódigo
Figura8.18:Formuláriodeinformaçõesdobancodedados
Atelaseguinterealizaráumtestedeconectividadecomobancodedados(é
importantequeseubancoestejaplenamenteoperacionalnestemomento). Casoo
testetenhasucesso,vocêdeveráverumatelacomoaquesegue:
240
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 257

CasadoCódigo Capítulo8. FlexibilizandosuaaplicaçãocomumESB
Figura8.19:Testedeconectividadedobancodedados
Finalmente,bastaseguiroinstaladoratéofinal.Casotudotenhasucesso,você
deveráverumatelacomoapróxima:
241
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 258

8.3. ConfiguraçãodoOSB CasadoCódigo
Figura8.20:Teladefinaliza çãodacria çãododomínio
Se você deixar a caixaIniciar Servidor Admin marcada, a inicializa-
ção do servidor será realizada. Quando você realizar a inicialização posterior-
mente,bastaacessarodomíniodoOSBeexecutaro script startWebLogic.bat.
Sevocêtiverseguidotodosospassospassadosatéaquiàrisca, estediretórioé
C:\Oracle\Middleware\user_projects\domains\osb_domain.
Aofinaldainicializa ção,vocêdeveenxergarumatelasemelhanteàseguinte:
242
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 259

CasadoCódigo Capítulo8. FlexibilizandosuaaplicaçãocomumESB
Figura8.21:Inicializa çãodoservidorOSB
Noteapresen çadapalavra RUNNING.Esteéoindicadordequeseuservidor
WebLogicestáoperante.ParavisualizaroconsoledoOSB,bastaacessaraURLhttp:
//localhost:7001/sbconsoleepreencheroformuláriodeautentica çãocomousuário
weblogiceasenhafornecidaduranteainstala ção.
8.4 C onceitos do OSB
OOSBcentralizaemsiosartefatosutilizadospelacomunica ção,comoWSDL’se
XSD Schemas.Acomunica çãofeitacomcadaservi çoérealizadaatravésde Business
Services(ou“ServiçosdeNegócio”,naversãoemportuguês). Adefiniçãodos Bu-
siness Servicescarregadiversasconfigura çõesalémdaespecifica çãodo web service
emsi,comoosistemadeseguran çautilizado,qualacodifica çãodacomunica ção,
mecanismosparabalanceamentodecargaetc.
Jáosmecanismosderoteamento,transforma çãodedados,enriquecimentode
mensagenseoutrastécnicassãoincorporadospelos Proxy Services(ou Serviços
de Proxy,naversãoemportuguês).Um Proxy Servicerecebearequisi çãoepode
efetuardiversostiposdefiltragem,transforma çãoeenriquecimentoatéfinalmente
entregá-laaum(oumais) Business Services.Alémdisso,um Proxy Servicepodeser
criadodiretamenteapartirdeum Business Servicesemcomplicações.Valelembrar:
opontodeacessoaosservi çosdevesersemprefeitovia Proxy Service,enuncavia
243
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 260

8.5. CrieumarotanoOSB CasadoCódigo
Business Service.
8.5 C rie uma rota no OSB
Paraospróximospassos,vocêdeveinicializaroOEPE.Casoelenãoestejadisponível
nomenuIniciardoWindows,bastaacessara Middleware Homeelocalizarumapasta
chamada oepe_<versão>.Nestapasta,estácontidooprograma eclipse.exe,
quecontémopacotedoOEPE.
Umavezaberto,énecessárioverificarseo WebLogicquecontémoOSBestá
presente.Casonãoesteja,bastaadicioná-lodamesmaformacomovocêadicionaria
outroservidorqualquer.
Emseguida,vocêprecisacriardoisprojetos. Oprimeiro,paraconterasespe-
cificaçõesdaconfigura çãogeraldoseuprojeto(querecebeonomede Oracle
Service Bus Configuration Project ). Osegundo, paraconterartefatos
específicos (que recebe o nome deOracle Service Bus Project ). Para
demonstrar o uso destes, criei umOracle Service Bus Configuration
Project com o nome deKnightELibrary e um Oracle Service Bus
Projectcomonomede Estoque. Esteúltimodevesercriadosempreassoci-
adoaum Oracle Service Bus Configuration Project .
Criando os projetos do Oracle ServiceBus
Acria çãodosprojetos Oracle Service Bus noOEPEétrivial;
bastaprocederdamesmamaneiracomovocêfariaemoutrosprojetos.
Tenhaemmente,noentanto,quemelhoresresultadosserãoatingidosao
ajustaraperspectivapara Oracle Service Bus .
Uma vez criados os projetos, crie duas pastas sob o projetoEstoque:
artefatosServicos e artefatosOSB. A primeira conterá o WSDL de
AutoresServiceeos XML Schemas. Asegundaconteráo Business Serviceque
iráreferenciaroserviçodeautoreseo Proxy Servicequeforneceráoacessoaeste.
O projeto que contém os artefatos e uma implementa ção via
Endpoint.publish está disponível no github, sob nomehttps://github.com/
alesaudate/soa/tree/master/soa-cap08. Lá,bastacopiaroWSDLeos Schemasparaa
pasta artefatosServicos.
244
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 261

CasadoCódigo Capítulo8. FlexibilizandosuaaplicaçãocomumESB
Feitoisso,cliquecomobotãodireitosobreapasta artefatosOSBeaponte
para New -> Business Service .Issoabriráacaixadediálogoparaacria ção
deumnovo Business Service,quevocêpodedaronome BSAutoresService:
Figura8.22:Telaparacria çãodoBusinessServicedeAutores
Selecioneaop ção WSDL Web Service ecliqueem Browse. Feitoisso,se-
lecioneoarquivo AutoresService.wsdleoexpandaparautilizaro binding
AutoresServiceSOAP.CliqueemOK.
Aseguir,vocêdeveinseriro endpointnoqualoseuservi çoiráresponder.Para
isso,mudeasele çãoparaaaba Transporte,nase ção Endpoint URI,coloque
oendereço http://localhost:9090/autoresService,cliqueem Addedepoissalve. Seu
Business Serviceestápronto.
Opróximopassoécriaro Proxy Servicequefaráaconexãocomo Business Ser-
vice. Paraisso,cliquenovamentesobreoprojeto Estoqueecrieum Proxy Ser-
vice,dessavez,chamado PSAutoresService. Damesmaformacomovocêfez
emrela çãoao Business Service,crieo Proxy Service baseadoemumWSDL—o
mesmoWSDLutilizadono Business Service.Feitoisso,vocêdevemudarparaaaba
Messaging Flow,ondevocêdeveconfigurarasop çõesderoteamentoutilizadas
peloOSB:
245
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 262

8.5. CrieumarotanoOSB CasadoCódigo
Figura8.23:Telaparaconfigura çãodoProxyServicenoOEPE
Agora, cliquecomobotãodireitosobreoíconedoenvelopeeapontepara
Insert Into -> Route . Aseguir,cliquecomobotãodireitosobre Insert
Into -> Communication -> Routing .Issocriaráumacaixadentrodacaixa
RouteNode1. Cliquenestacaixainternaeselecioneaaba Properties,mais
abaixo.Nocampo Service,cliqueem Browseeselecioneo Business Serviceque
vocêcriouhápouco.
Nestemomento,suaconfigura çãoestápronta.Paratestá-la,cliquecomobotão
direitosobreaconfigura ção,apontepara Export -> Oracle Service Bus -
Resources to Server . Preservetodasasconfigura çõescomoestiverem. Caso
estejatudoconfiguradocorretamente,vocêdevesercapazdeveroprojetonocon-
soledoOSB,disponívelem http://localhost:7001/sbconsole.
Pararealizaroteste,bastaexpandiraaba Resource Browser e,aseguir,clicar
em Serviços de Proxy .O Proxy Service PSAutoresServicedeveráaparecer
nalistagem.Bastaclicarsobreopequenoinseto( bug)àdireitadomesmoparaser
direcionadoparaateladetestedoservi ço.
246
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 263

CasadoCódigo Capítulo8. FlexibilizandosuaaplicaçãocomumESB
Figura8.24:Teladetestedoproxyservice
Finalmente,bastaselecionaraopera çãodesejadaemodificaro payload(ouseja,
ocorpodarequisi ção)àvontade.Paraenviarachamada,bastaclicarem Executar.
Casotudoestejabem,algocomooseguintedeveserapresentadonatela Documento
de Resposta (lembre-sederealizarotestecomoservi çodeautoresinicializado):
<soapenv:Envelope
xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
<soapenv:Header/>
<S:Body xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
<ns2:listarAutoresResponse
xmlns:ns2=
"http://knight.com/estoque/services/AutoresService/v1">
<autor>
<nome>Alexandre</nome>
</autor>
</ns2:listarAutoresResponse>
247
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 264

8.6. Sumário CasadoCódigo
</S:Body>
</soapenv:Envelope>
CasovocêdesejecriaroclienteJava,bastautilizarWSDLdisponibilizadopelo
OSBem http://localhost:7001/Estoque/artefatosOSB/PSAutoresService?wsdl.
8.6 S umário
Neste capítulo, você aprendeu a instalar, configurar e utilizar oOracle
Enterprise Pack for Eclipse eo Oracle Service Bus .Vocêaprendeu
queessetipodeferramentaéutilizadapararotearmensagens,transformá-laseou-
trosaspectosde patternsdeintegração.
Restaaindavercomoreunirváriosservi çosemumacoisasó,ouseja,expor
váriosserviçosdemaneiracoordenada,deformaquesuaimplementa çãoSOAseja
aindamaisflexível.
248
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 265

Capítulo9
CoordeneserviçoscomBPEL
“Não está ocioso apenas aquele que não faz nada, mas também aquele que poderia
fazer algo melhor. ”
–Sócrates
Vocêjátemasrespostasparaastradicionaisquestõesquepodemsurgirdurante
aimplementaçãodeumaarquiteturaorientadaaservi ços.Oúltimodesafioquese
fazpresenteé:comocriar,demaneiraadequada,composi çõesdeservi ços?Emou-
traspalavras,comoendere çardesafioscomotransacionalidadeeheterogeneidadena
comunicaçãoentreváriosservi çosdeumamaneirasimples,adaptávelamudan ças?
Obviamente,existemaisdeummododerealizarcomunica çãoentreváriosser-
viços. Vocêvaiconhecerosmecanismosmaiscomunsecomofazerissodeuma
formainteligenteerápida.
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 266

9.1. Conheçaorquestraçãoecoreografia CasadoCódigo
9.1 C onheça orquestração e coreografia
Ascomposiçõesdeservi çossãocomumentedescritascomo orquestrações ou co-
reografias. Umacoreografiaéumacomposi çãodeservi çosdescentralizada. Na
coreografia,cadaparticipante( web service)devesaberespecificamentequaisa ções
executar.Jánaorquestraçãoexisteumcontroladorcentralizado,dizendoacada web
serviceamaneiradeprosseguiratrocadedados.
Naprática,istosetraduzentrerealizarestastrocasdeinforma çõescomcódigo
puro(ouseja,expôrum web servicedamaneiratradicional,comcódigo)oufazer
istoutilizandoumaferramentaexpostanumservidorpróprioparaisso.
Ambasasabordagenspossuemvantagensedesvantagens. Umadasvantagens
daformadescentralizadaéqueestaémaisescalável,postoquevocêpodefornecer
maismáquinasparaatenderasrequisi ções. Alémdisso,ocontroledosformatos
dedadosnãoestánecessariamentepresoaXML—porexemplo,sevocêtivervários
EJBsexpostoscomo web servicesequisercoordenarrequisi çõesentreeles,vocêpode
expôrumterceiroEJBcomo web serviceefazeracomunica çãoentreseusservi ços
demaneiradireta,comcódigoJava.
Issofacilitaoestabelecimentodetransa çõesentreeles,demaneiraqueédes-
necessárioutilizarmecanismosmaiscomplexosparaisso.Noentanto,issosetorna
umadesvantagemdopontodevistadoacoplamento—sevocêquisermodificar
algumdessesservi ços,osoutrospossivelmentesofreramimpactos.
Jánaorquestração,aomantertudodemaneiracentralizada,todaacomunica ção
éfeitaobrigatoriamenteatravésdainterfacepúblicadestesservi ços,istoé,comoum
clientecomumdo web service. Issoestimulaodesenvolvimentovoltadoaomodo
comoosclientesvãoutilizaroservi ços.Alémdisso,tambémfacilitaamanuten ção
dosservi çosemestadoconsistente,jáqueumnócentralizadoconseguedetectar
falhasnosoutrosecolocartodosemestadoconsistente.
Entreasduasformas,aquetemsidomaisadotadapelomercadoéaorquestra-
ção.ElaéimplementadaatravésdoBPEL( Business Process Execution Language),que
éumalinguagemespecificamentecriadacomopropósitodecoordenaracomunica-
çãoentreváriosserviços.Dentreasimplementa çõesdeBPEL,umadasversõesmais
utilizadaséoOracleBPEL,quevocêiráconhecernestecapítulo.
9.2 instale o Oracle SOA Suite
OOracleBPELéformadodeumconjuntodeaplica ções,quesãopartedeumpro-
dutochamado SOA Suite. Esteprodutoéinstaladodemaneirasemelhanteao
250
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 267

CasadoCódigo Capítulo9. CoordeneserviçoscomBPEL
Oracle Service Bus ,ouseja,bastaexecutaroRCUeinstalaroSOASuitesobre
o WebLogic.
Existemváriasmaneirasdeinstalaro SOA Suite levandoemcontanossains-
talaçãopréviadoOSB.Comoestamosfalandodeumamáquinadedesenvolvimento,
vocêaprenderáainstalaroOSBeoSOASuitejuntos.
Suaprimeiratarefadevesercriarosbancosdedadosdetrabalhodo SOA
Suite.Paraisso,vocêdeveexecutaroRCUnovamente—destavez,marcandoa
opção SOA Infrastructure e BPM Infrastructure ecriandoumprefixo
novoparaoconjunto,comomostraafigura:
Figura9.1:CriandoastabelasnecessáriasparaofuncionamentodoSOASuite
Aseguir,vocêdeveinstalaro SOA Suite,propriamentedito. Ainstala çãoé
semelhanteàdoOSB:bastarealizaro downloaddosarquivosreferentesaomesmo
e,umavezconcluídos,descompactá-losemumapastadesuapreferência.Aseguir,
inicializeaaplica çãodeexecu çãodelinhasdecomandodoWindows(o cmd),nave-
gueatéapasta ofm_soa_generic_11.1.1.6.0_disk1_1of2/Disk1eexecute
251
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 268

9.2. instaleoOracleSOASuite CasadoCódigo
aaplicação setup.exe.
Tomeocuidadodeforneceroparâmetro -jreLoc,comalocaliza çãodesua
JDK/JRE(tomeocuidado,também,detê-lainstaladaemumapastasemespa çosno
nome).
Figura9.2:Inicializandoainstala çãodoSOASuite
Ainstalaçãodo SOA Suite ébemsimples,diferenciandopoucodainstala ção
do OSB.Umadasdiferen çasseráoquestionamentodequalservidordeaplica ção
deveráserutilizado(nonossocaso,o WebLogic):
252
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 269

CasadoCódigo Capítulo9. CoordeneserviçoscomBPEL
Figura9.3:QuestionamentosobrequalApplicationServerutilizar
Outra diferença é que, em certo ponto da instalação (ou seja, com
a transferência de arquivos já inicializada), o instalador deverá solici-
tar a localização dos discos 4 e 5. Quando isso acontecer, basta navegar
até as pastas ofm_soa_generic_11.1.1.6.0_disk1_2of2/Disk4 e
ofm_soa_generic_11.1.1.6.0_disk1_2of2/Disk5,respectivamente:
253
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 270

9.2. instaleoOracleSOASuite CasadoCódigo
Figura9.4:Selecionandoodiscodeinstala çãocorreto
Uma vez finalizado o procedimento para instalação, você deve realizar a
configuração. Isso é feito utilizando o mesmo aplicativo que utilizamos para
configurar o OSB, ou seja, o Configuration Wizard do WebLogic.
O Configuration Wizard pode ser encontrado, mais uma vez, em
MIDDLEWARE_HOME/wlserver_10.3/common/bin/config.cmd . A diferença
entre nossa configuração anterior e a atual é que, ao invés
de criarmos um novo domínio, vamos estender o já existente,
que contém o OSB . Para fazer isso, selecionamos a opção
Ampliar um domínio WebLogic existente na tela inicial do
ConfigurationWizard
254
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 271

CasadoCódigo Capítulo9. CoordeneserviçoscomBPEL
Figura9.5:UtilizandooConfigurationWizardparaampliarumdomíniodoWebLo-
gic
Umavezselecionadaestaop ção,o Configuration Wizard iráquestionara
respeitododomínioaserampliado.Bastaselecionarapastaondeodomínioestá:
255
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 272

9.2. instaleoOracleSOASuite CasadoCódigo
Figura9.6:SelecionandoodomíniodoWebLogic
Selecionadoodomínio,o Configuration Wizard iráexibiroquejáexiste
nodomínio(naformadebotõesesmaecidos)eofereceráasop çõesdeamplia-
ção.Bastamarcarasop ções Oracle SOA Suite for developers e Oracle
Enterprise Manager (ospré-requisitosparaainstala çãodeambosserãoauto-
maticamenteselecionadostambém):
256
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 273

CasadoCódigo Capítulo9. CoordeneserviçoscomBPEL
Figura9.7:ConfigurandooSOASuitenodomíniodoOSB
Aoprosseguir,o Configuration Wizard questionaráarespeitodeondeco-
locarasaplica ções.Bastadeixaracaixadesele çãocomoestá:
257
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 274

9.2. instaleoOracleSOASuite CasadoCódigo
Figura9.8:Apontandoapastaondeasaplica çõesdoSOASuitedeverãoficar
Depois,o Configuration Wizard questionaráarespeitodasinforma ções
debancodedados. Umasutilezaestarápresente:asinforma çõesdeproprietários
deesquemas(ou schema owners,naversãoeminglês)estaráconfiguradacomopre-
fixo DEV.Vocêdeveselecionarumaaumadasconfigura çõesdoSOASuitepara
reconfigurarcomoprefixo DEV1(tomecuidadoparanãoreconfigurartambémo
componente OSB JMS Reporting Provider ,quedeveserdeixadocomoestá).
Umavezrealizadoesteprocedimento,vocêpodemarcartodososcomponentespara
configurarasinforma çõesdebancosdedadosdeumavezsó.Afiguramostracomo
suaconfiguraçãodeveficar:
258
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 275

CasadoCódigo Capítulo9. CoordeneserviçoscomBPEL
Figura9.9:ConfigurandoosesquemasdebancosdedadosdoSOASuite
Aperteobotão Selecionar Tudo e,emseguida, Testar Conexões. O
Configuration Wizard realizaráotestedetodasasconfigura çõesdebancosde
dadose,casotudoestejabem,o statusdetodosdeveficarverde:
259
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 276

9.3. InstaleoJDeveloper CasadoCódigo
Figura9.10:Statusdaconfigura çãodecomponentesdoSOASuite
Apartirdesteponto,bastaprosseguiratéofinal.Seu SOA Suite estápronto.
9.3 I nstale o JDeveloper
A IDE utilizada para desenvolvimento com o Oracle SOA Suite é o
JDeveloper. Napáginade downloaddopróprio SOA Suite,vocêiráencon-
traroarquivodo JDeveloper.Umavezfeitoo download,executeoarquivo(este
podeserum .exe,seo downloadfoifeitoparaWindows,ou .jarparaplataforma
genérica).
Apósaextra çãodopacote,oprocedimentoparainstala çãoseráiniciado. Um
dospontosprincipaisaosquaisvocêdeveestaratentoéasele çãodo Middleware
Homeparao JDeveloper.Notequeestedeveserdiferentedaquelejáreconhecido
(ouseja,algocomo C:\Oracle\Middleware),porqueoJDeveloperjávemcom
um WebLogicpróprio,oquepodecausarasobrescritadoquejáestápresenteno
seu Middleware Home antigo.Emsuma,bastaselecionarumnovo(porexemplo,
260
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 277

CasadoCódigo Capítulo9. CoordeneserviçoscomBPEL
C:\Oracle\IDE):
Figura9.11:CriandoumnovoMiddlewareHomeparaoJDeveloper
Apartirdaqui,ainstala çãodeveserbastanteintuitiva;bastaseguiroprocedi-
mentoatéofinal.
Sob Windows, um atalho para oJDeveloper deve ter sido criado na
sua área de trabalho ou no menu Iniciar. Caso isso não tenha acontecido,
basta ir até a pasta de instalação do JDeveloper e executar o arquivo
jdeveloper\jdeveloper.exe.Inicializadoo JDeveloper,umacaixaparase-
leçãode rolesdeveaparecer.Casonãoqueirapensarnissoagora,bastadeixarcomo
está:
261
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 278

9.3. InstaleoJDeveloper CasadoCódigo
Figura9.12:Sele çãoderolesparaaexecu çãodoJDeveloper
A segunda seleção que deverá aparecer será a quais arquivos associar o
JDeveloper. Sugiromarcarasduasprimeirasedeixarasoutrasduasdesmarca-
das:
262
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 279

CasadoCódigo Capítulo9. CoordeneserviçoscomBPEL
Figura9.13:SeleçãodetiposdearquivosaosquaisassociaroJDeveloper
Opróximopassoéinstalaro pluginparaquesejapossíveltrabalharcomo SOA
Suite.Paraisso,bastairatéomenu Helpeselecionar Check for Updates... ,
conformeaimagem:
Figura9.14:Acioneomenudeinstala çãodepluginsdoJDeveloper
Feito isso, a tela de boas-vindas à checagem de atualizações é exibida.
Aperte Next e a tela de seleção de fontes de atualizações é exibida. Mar-
queasfontes Oracle Fusion Middleware Products e Official Oracle
Extensions and Updates :
263
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 280

9.4. IntroduçãoaBPEL CasadoCódigo
Figura9.15:Acioneomenudeinstala çãodepluginsdoJDeveloper
Uma vez feita a checagem porplugins, marque oplugin Oracle SOA
Composite Editor eprossiga. Aofinal,o JDeveloperirásolicitarreiniciali-
zação.Aotérminodareinicializa ção,ainstala çãoeconfigura çãodoJDeveloperestá
concluída.
9.4 I ntrodução a BPEL
Está disponível no github (em https://github.com/alesaudate/soa/tree/master/
KnightServices)umprojetodo JDeveloperchamado KnightServices. Este
projetocontémumarquivochamado KnightServices.jws.Aodarumduplo-
cliquesobreele,eleseráabertocomo JDeveloper,permitindoavocêvisualizar
suaestrutura:
264
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 281

CasadoCódigo Capítulo9. CoordeneserviçoscomBPEL
Figura9.16:EstruturadoprojetoBPEL
Aorealizarduplo-cliquesobreoarquivo ListarAutoresBPEL.bpel,ase-
guinteestruturadeveráseabrir:
265
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 282

9.4. IntroduçãoaBPEL CasadoCódigo
Figura9.17:VisualizaçãodofluxoBPEL
Este fluxo irá realizar a listagem de autores, delegando para oweb service
exposto no OSB a função de listagem de autores, mapeando os resultados e
retornando-osparaocliente. Pararealizaraimplanta çãodestefluxonoservi-
dor,cliquecomobotãodireitosobreoprojeto,apontepara Deployecliqueem
ListarAutoresBPEL...:
266
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 283

CasadoCódigo Capítulo9. CoordeneserviçoscomBPEL
Figura9.18:IniciandoodeploydoBPEL
Suaprimeiraimplanta çãovairequereradefini çãodo Application Serverondeo
BPELseráinstalado.Umacaixadesele çãoquestionaráarespeitodotipodeimplan-
tação:diretano Application Serverouparaum SAR—Service ARchive (oque,
naprática,significaumarquivoJARquepodeserimplantadoemqualquerservidor).
Marqueaop ção Deploy to Application Server ecliqueem Next.
Aseguir, umacaixadeop çõesdeimplanta çãoseráexibida. Marqueaop-
ção Overwrite any existing composites with the same revision
ID.ecliqueem Next,deacordocomaimagem:
267
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 284

9.4. IntroduçãoaBPEL CasadoCódigo
Figura9.19:Op çõesdeimplanta çãodoBPEL
Depoisdisso,umalistagemde Application Serversseráexibida,embranco.Para
adicionarum Application Server,cliquenosímbolodemaisverde,notopoàdireita:
268
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 285

CasadoCódigo Capítulo9. CoordeneserviçoscomBPEL
Figura9.20:Defini çãodenovoapplicationservernoJDeveloper
Na caixa que aparecerá, dê um nome para a conexão (sugiro, no caso,
localhost). Cliqueem Next. Napróximacaixa,vocêdeveráfornecero login
esenhadousuário weblogic:
269
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 286

9.4. IntroduçãoaBPEL CasadoCódigo
Figura9.21:FornecimentodologinesenhadoApplicationServer
Emseguida,vocêdeveráfornecerdetalhessobreainstala çãodo SOA Suite,
ouseja,vocêdeveráforneceroendere çoIP,aportaeodomíniodo WebLogic.
Paraestestrêsvalores,vocêdeveráfornecer localhost, 7001e osb_domain,
respectivamente:
270
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 287

CasadoCódigo Capítulo9. CoordeneserviçoscomBPEL
Figura9.22:DetalhesdoApplicationServer
Napróximatela,apareceráumatelaparatestedaconfigura ção,queseráativada
aoclicarnobotão Test Connection.Seaconfigura çãoestivercorreta(eo SOA
Suiteestiveremexecu ção),eladeveráficarassim:
271
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 288

9.4. IntroduçãoaBPEL CasadoCódigo
Figura9.23:Testedaconfigura ção
Nasequência,aoclicarem Finish,vocêdeverávoltaràteladesele çãode Ap-
plication Servers.Selecioneorecém-criadoecliqueem Next.Asuainfraestrutura
deveserexibidadaseguinteforma:
272
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 289

CasadoCódigo Capítulo9. CoordeneserviçoscomBPEL
Figura9.24:Exibi çãodainfraestruturaSOASuite
Nestemomento,vocêpodeclicarem Finish.Seucódigovaisercompiladoe,
casopassedesteestágio,seráimplantadonoservidor.O statusdestespassospodeser
conferidonoconsoledo JDeveloper,emváriasabaspresentesnaparteinferior
domesmo.
Pararealizartestes, vocêpodenavegaratéo Enterprise Manager (uma
aplicaçãoparagerenciamentodo SOA Suite eoutroscomponentes),disponível
emhttp://localhost:7001/em(vocêprecisaráfornecero loginesenhadousuário
weblogicparaacessaraaplica ção).Umavezlogado,existeumpainelàesquerda
listandoascomposições—bastaexpandiromenu SOA.Expandindocompletamente
asopções,vocêdeveobteroconsoledegerenciamentodasuacomposi çãoBPEL.
Aoclicarnobotão Testar,vocêtemduasop ções:poderealizarostestespelo
próprio browser,peloformulárioqueestarápresente,oupodeobteroWSDLdo
fluxo,disponívelnestamesmapágina.
Nestemomento,seufluxoestápronto.Vocêpodefazermodifica çõesnofluxoa
273
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 290

9.5. Sumário CasadoCódigo
partirdoJDeveloper,erefazeraimplanta çãosemprequequiser,repetindoosmes-
mospassoscitados.
9.5 S umário
Nestecapítulo,vocêvisualizouumadasprincipaisferramentasdouniversoSOA,
BPEL.Vocêviucomoinstalareconfiguraro Oracle SOA Suite ,umadasprin-
cipaisferramentasdestesegmento.Vocêtambémpôdeconferircomoinstalarecon-
figuraro JDeveloper,aIDEpadrãoparadesenvolvimentocomoSOASuite.
Porúltimo,vocêteveumvislumbredo Enterprise Manager,aferramenta
degerenciamentodo WebLogic.Estaferramentapermite,entreoutrascoisas,vi-
sualizaregerenciarseusfluxosBPELimplantadosnoSOASuite.
274
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 291

Capítulo10
Conclusão
“Nossas dúvidas são traidoras e nos fazem perder o bem que poderíamos conquistar,
se não fosse o medo de tentar. ”
–WilliamShakespeare
Vocêviu,atéaqui,todaabaseparaseconstruirumprojetoSOAadequadamente.
Nosprimeiroscapítulos,vocêpôdevislumbrarcomoconstruireutilizar web services
—abaseparatodaarquiteturaorientadaaservi çosmoderna.
Obviamente,nãoparaporaí.Muitasquestõesforamrespondidas;vocêconhe-
ceu,nosquatrocapítulosiniciais,a enginedoJAX-WSecomotrabalharcomoscha-
mados web servicesclássicos,ouseja,aquelesbaseadosemSOAPeWS-*.Nocapítulo
5,vocêconheceuREST,umaabordagemdiferenteparaoproblemadatransmissão
dedadosentreaplica ções.
Apartirdocapítulo6,vocêfoiapresentadoaproblemasnovos,ecome çoua
visualizarousorealdeSOA:vocêpassoua reutilizarserviços,enãoapenasconstruí-
los.
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 292

CasadoCódigo
Docapítulo7emdiante,vocêfoiapresentadoatécnicasdedesenvolvimento
utilizadasemprojetosreais—comoeparaqueutilizaro modelo canônico,como
desenvolverserviçosbaseadosemseusWSDLs( contract-first),comocoordenarcha-
madascomBPEL,etc.
Hámuitoaindaporvir. ComomeuamigoFelipeOliveiramencionounopre-
fácio,existemdiversastécnicasnomundodaorienta çãoaservi çosquepodeme
devemserutilizadasemprojetosreais,equedariamvidaàmuitoslivrossobreos
assuntos. Porém,vocêdeveconsideraresteumpontodeinícioparaseusestudos
deSOA,enãoumpontofinal.Umsegundolivroestásendoescritopormim,para
continuaromesmotema.Nestepróximolivro,esperodarcontinuidadeaostópicos
apresentadosneste,mostrandoconceitosaindamaisavan çados.
Paracontinuarseusestudos,existemdiversasfontes.Eutenhomantidoalguns
artigosemrevistasespecializadasdoramodedesenvolvimento,ondeescrevosobre
temasrelacionadosaSOA.Alémdisso,tambémparticipodefóruns—nomomento,
tantooGUJ(http://www.guj.com.br/)comooSOACloud(http://soacloud.com.br/)
.Alémdisso,oInfoQ(http://www.infoq.com/br)tambémtemsessõesespecializa-
dasnossegmentosdeSOAe cloud computing,eéumafontedeestudosfortemente
recomendada.
Comomencionadonaintrodu ção,vocêtambémestáconvidadoafazerparte
dogrupodediscussãoprópriodestelivro,emhttps://groups.google.com/forum/
?fromgroups=#!forum/soa-aplicado. Lá,vocêpodeentraremcontatocomoutros
leitoresdolivro,tirardúvidas,fazersugestõesetc.
OmercadodeSOAmantém-semuitopromissorparatodos,sejamanalistas,
desenvolvedores,arquitetosououtrospapéis. Esperoque,comestelivro,vocêse
sintacapazdelidarcomosdesafiospresentesnesteuniversoe,também,sinta-se
capazdeprosseguircomsuaprópriapesquisa.
Bonsestudos!
--AlexandreSaudate
276
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com

## Página 293

CasadoCódigo ReferênciasBibliográficas
Referências Bibliográficas
[1] RalphJohnsonJohnVlissidesErichGamma,RichardHelm. Designpatterns:
Elementsofreusableobject-orientedsoftware.1994.
[2] ThomasErl.Service-orientedarchitecture:Concepts,technologydesign.2005.
[3] ThomasErl.Soaprinciplesofservicedesign.2008.
[4] ThomasErl.Soadesignpatterns.2009.
[5] EricEvans. Domain-drivendesign:Tacklingcomplexityintheheartofsoft-
ware.2003.
[6] RoyThomasFielding. Architecturalstylesandthedesignofnetwork-based
softwarearchitectures.2000.
[7] MartinFowler.Anemicdomainmodel.2003.
[8] MartinFowler.Patternsofenterpriseapplicationarchitecture.2003.
[9] BobbyWoolfGregorHohpe.Enterpriseintegrationpatterns:Designing,buil-
ding,anddeployingmessagingsolutions.2003.
[10] SamRubyLeonardRichardson.Restfulwebservices.2007.
277
E-book gerado especialmente para Danilo Ferreira - danilocsf@gmail.com