---json
{
  "id": "ios_programe_para_iphone_e_ipad_1",
  "title": "iOS Programe para iPhone e iPad",
  "categoria": "04-frameworks",
  "subcategoria": "mobile",
  "resumo": "**Arquivo Original:** `iOS Programe para iPhone e iPad.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "frameworks",
    "ios",
    "ipad",
    "iphone",
    "mobile",
    "para",
    "programe"
  ],
  "perguntas_tipo": [
    "Como utilizar iOS Programe para iPhone e iPad?",
    "Quais as boas praticas de mobile?"
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
  "dono": "stack-mobile",
  "prioridade": 2
}
---

# iOS Programe para iPhone e iPad

> **Arquivo Original:** `iOS Programe para iPhone e iPad.pdf`
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
Àquelesque,antesdetodos,emmimacreditaram:Daniel,Everson,GuilhermeePaulo.
i

## Página 7

CasadoCódigo Sumário
Sumário
1 Introdu ção 1
1.1 DesenvolvendoparaoiOS . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 Comoolivroestáorganizadoefocado . . . . . . . . . . . . . . . . . . 2
1.3 Códigosparadownloadelistadediscussão . . . . . . . . . . . . . . . 3
2 Hello World, seu primeiro programa em iOS 5
2.1 Instalandoaferramentadedesenvolvimento-Xcode . . . . . . . . . 6
2.2 Seuprimeiroprograma . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.3 Dandovidaaoaplicativo . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.4 Associesuatelacomocódigo . . . . . . . . . . . . . . . . . . . . . . . 14
2.5 Escondendoemostrandoaview . . . . . . . . . . . . . . . . . . . . . . 20
2.6 Adicionaranimaç ão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
2.7 Bônus-Acessaradocumentaç ãodedentrodoXcode . . . . . . . . . 22
3 Mais Objective-C e Xcode 23
3.1 Criandooprojeto . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.2 EntendamelhorainterfacedoXcode . . . . . . . . . . . . . . . . . . . 26
3.3 Criarateladeinser çãodeempresa . . . . . . . . . . . . . . . . . . . . 27
3.4 Adicionarcomponentesvisuais . . . . . . . . . . . . . . . . . . . . . . 29
3.5 Aten çãoparaaspropriedadessimuladas . . . . . . . . . . . . . . . . . 31
3.6 Conectandooseventosecomponentesaocódigo . . . . . . . . . . . . 32
3.7 Umaclassepararepresentarumaempresa . . . . . . . . . . . . . . . . 35
3.8 Cabe çalhoseimplementações . . . . . . . . . . . . . . . . . . . . . . . 37
3.9 Informandoaquantidadedefuncionários . . . . . . . . . . . . . . . . 38
3.10 Trabalhecomobjetos:instanciandoumaEmpresa . . . . . . . . . . . 39
iii

## Página 8

Sumário CasadoCódigo
3.11 ComosãoasstringsemObjective-C? . . . . . . . . . . . . . . . . . . . 40
3.12 Formatandostrings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
3.13 Guardandotodasempresasemmemória . . . . . . . . . . . . . . . . . 41
3.14 Listandotodasasempresasdocatálogo . . . . . . . . . . . . . . . . . . 43
3.15 VençaasintaxedoObjective-C:invocaç ãodemétodos . . . . . . . . 44
3.16 Criandoinstânciasdeobjetos . . . . . . . . . . . . . . . . . . . . . . . 46
3.17 Melhoria:esconderotecladoautomaticamente . . . . . . . . . . . . . 48
3.18 Melhoria:mostrandoamensagemdesucessosomenteaosalvar . . . 49
4 Coordenando o trabalho com controladores 51
4.1 Passandodeumcontroladorparaoutro . . . . . . . . . . . . . . . . . 53
4.2 Fecharumcontroladormodal . . . . . . . . . . . . . . . . . . . . . . . 60
4.3 NavegarpordiferentestelascomoUINavigationController . . . . . . 60
4.4 Prepararatelaprincipal . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
4.5 Conectarasaçõesdosbotões . . . . . . . . . . . . . . . . . . . . . . . . 65
4.6 CriarateladeAdicionarEmpresa . . . . . . . . . . . . . . . . . . . . . 65
4.7 Navegardeumcontroladorparaoutro . . . . . . . . . . . . . . . . . . 66
4.8 AssociarumUINavigationControlleraoprojeto . . . . . . . . . . . . 66
4.9 Criarosdemaiscontroladores . . . . . . . . . . . . . . . . . . . . . . . 68
4.10 Esconderabarrasuperiordenavegaç ão . . . . . . . . . . . . . . . . . 71
5 Storyboards 73
5.1 Projetoeconceitosgerais . . . . . . . . . . . . . . . . . . . . . . . . . . 74
5.2 Adicionarosdemaiscontroladores . . . . . . . . . . . . . . . . . . . . 84
5.3 NavegardevoltadiretamenteparaaSegueinicial . . . . . . . . . . . . 90
5.4 PassardadosdeumaSegueparaoutra . . . . . . . . . . . . . . . . . . 92
6 Realizando operaç ões com a Internet 95
6.1 Conhe çaabibliotecaAFNetworking . . . . . . . . . . . . . . . . . . . 96
6.2 Criandoainterfacededownload . . . . . . . . . . . . . . . . . . . . . 97
6.3 Conectandooscomponentescomocódigo . . . . . . . . . . . . . . . 99
6.4 Realizaraoperaç ãodedownload . . . . . . . . . . . . . . . . . . . . . 104
6.5 TrabalhandocomJSONeimagensremotas . . . . . . . . . . . . . . . 106
6.6 Configuraros blocksdesucessoeerrodoAFNetworking . . . . . . . 112
6.7 Configuraroscrollepré-geraroscomponentesdeimagens . . . . . . 114
iv

## Página 9

CasadoCódigo Sumário
6.8 Carregarumadeterminadaimagem . . . . . . . . . . . . . . . . . . . . 116
6.9 Carregarasoutrasimagensàmedidaqueinteragimoscomoscroll . 118
6.10 Façaseuaplicativofuncionaremtodasasorientações . . . . . . . . . 119
7 Trabalhando com tabelas - UITableView 123
7.1 Criandoaprimeiratableview-conceitoseexemplo . . . . . . . . . . 125
7.2 Oaplicativodelistadecontatos . . . . . . . . . . . . . . . . . . . . . . 127
7.3 Carregandooscontatosapartirdeumarquivoplist . . . . . . . . . . 128
7.4 Tornandoatabelafuncional . . . . . . . . . . . . . . . . . . . . . . . . 133
7.5 Informandoaquantidadedeitensquetemos . . . . . . . . . . . . . . 134
7.6 Exibindodadosemcadalinha . . . . . . . . . . . . . . . . . . . . . . . 135
7.7 Permitindointeraç ãocomositensdatabela . . . . . . . . . . . . . . . 138
7.8 Removendoelementosdatableview . . . . . . . . . . . . . . . . . . . 138
7.9 Removendodiversaslinhas . . . . . . . . . . . . . . . . . . . . . . . . . 140
7.10 Crieumatabelaparaonossocatálogodeempresas . . . . . . . . . . . 143
8 Trabalhando com reconhecedores de gestos 145
8.1 Sistemadeeventostradicional . . . . . . . . . . . . . . . . . . . . . . . 146
8.2 Umaabordagemmaisprática:ddegestos . . . . . . . . . . . . . . . . 151
8.3 ConvertendooexemploCirculoViewparagestos . . . . . . . . . . . . 152
8.4 Tremedeiracomtoquelongo . . . . . . . . . . . . . . . . . . . . . . . . 154
8.5 DeslizandoumaviewcomogestoSwipe . . . . . . . . . . . . . . . . . 159
9 Trabalhe com mapas e GPS na sua aplicaç ão 163
9.1 Asbibliotecasnecessárias . . . . . . . . . . . . . . . . . . . . . . . . . . 163
9.2 Adicionandoomapaàaplicaç ão. . . . . . . . . . . . . . . . . . . . . . 164
9.3 Simulandomúltiplostoques . . . . . . . . . . . . . . . . . . . . . . . . 165
9.4 Posicionandoomapaautomaticamentenalocalizaç ãodousuário . . 166
9.5 Trabalhecomozoom . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168
9.6 Adicionandopinosaomapa . . . . . . . . . . . . . . . . . . . . . . . . 169
9.7 Detectetoquesnospinos . . . . . . . . . . . . . . . . . . . . . . . . . . 171
v

## Página 10

Sumário CasadoCódigo
10 Componentes gráficos customizados 173
10.1 Criandoviews . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174
10.2 Animandoviews. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175
10.3 Animandodaformaproceduraletradicional . . . . . . . . . . . . . . 176
10.4 Animandocomousodeblocos . . . . . . . . . . . . . . . . . . . . . . 176
10.5 Criandoviewscustomizadas . . . . . . . . . . . . . . . . . . . . . . . . 177
10.6 UtilizaraviewcustomizaLoginView . . . . . . . . . . . . . . . . . . . 181
10.7 ConstruirocomponenteLoginViewutilizandoumarquivoXIBde
interface. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 181
10.8 ComoutilizarviewscriadoscomarquivosXIB . . . . . . . . . . . . . 185
11 Conceitos fundamentais de Objective-C 187
11.1 Umapequenahistória . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187
11.2 Nomeeassinaturadométodo . . . . . . . . . . . . . . . . . . . . . . . 188
11.3 Propriedades. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189
11.4 Acessosomenteleitura . . . . . . . . . . . . . . . . . . . . . . . . . . . 191
11.5 Utilizandopropriedadesdentrodaprópriaclasse . . . . . . . . . . . . 193
11.6 Definindoprotocolos . . . . . . . . . . . . . . . . . . . . . . . . . . . . 195
11.7 Trabalhandocomcategorias . . . . . . . . . . . . . . . . . . . . . . . . 197
11.8 Gerenciamentodememória . . . . . . . . . . . . . . . . . . . . . . . .200
11.9 Gerenciamentomanualdememória(paraoscuriosos) . . . . . . . .202
11.10 Simplificandoascoisascomliterais . . . . . . . . . . . . . . . . . . . .205
12 Como criar uma conta no portal de desenvolvimento da Apple 209
12.1 Registre-secomoumdesenvolvedorApple . . . . . . . . . . . . . . . .209
12.2 FazendoaassinaturanoiOSDeveloperProgram . . . . . . . . . . . . 211
12.3 Ostiposdecertificados . . . . . . . . . . . . . . . . . . . . . . . . . . . 215
13 Rodando os aplicativos no seu iDispositivo 217
13.1 Crieeinstaleocertificado . . . . . . . . . . . . . . . . . . . . . . . . . 218
13.2 Crieaidentidadedoseuaplicativo-AppIDs . . . . . . . . . . . . . . 222
13.3 Adicionandodispositivosparadesenvolvimento . . . . . . . . . . . .224
13.4 Limiteanualdedispositivos . . . . . . . . . . . . . . . . . . . . . . . . 225
13.5 Crieocertificadodeprovisionamento . . . . . . . . . . . . . . . . . .226
13.6 AssocieoarquivodeprovisionamentonoXcode . . . . . . . . . . . . 227
13.7 Rodeseuaplicativonodispositivo . . . . . . . . . . . . . . . . . . . . .230
13.8 Verificandoainstalaçãodosperfisnodispositivo . . . . . . . . . . . . 231
vi

## Página 11

CasadoCódigo Sumário
14 Uma palavra final + bônus 233
14.1 Bônus-livroselinks . . . . . . . . . . . . . . . . . . . . . . . . . . . . 234
vii

## Página 13

Capítulo1
Introdução
OiPhoneeoiPadsãofenômenos.
Nãosóseusmarketsharespossuemnúmerosimpressionantes,mastambémo
númerodevendasdaAppStoretrazânimoparanós,desenvolvedores.
MesmocomonúmeroexpressivodedispositivosAndroid,éestimadoqueaApp
Storesejaresponsávelpor85-90%dofaturamentodetodasosaplicativosmóveisjá
vendidos(http://bit.ly/appstoreNumeros),tendorevertidoquase4bilhõesdedóla-
resaosdesenvolvedoresdeiPadeiPhone.
EoBrasil?Deacordocomositedeanálisemobileflurry.com,omercadobrasi-
leiroatingiu,em2012,adécimaposiç ãomundialemnúmerodesmartphones.São
maisde13milhõesdedispositivos,emsuagrandemaioriaiPhoneseAndroids.Este
sitedoGooglepodeagregarmaisinformações:
http://www.thinkwithgoogle.com/mobileplanet/pt-br/
Vocêencontramaissobreomarketsharededispositivosmóveisatravésdossites:
http://www.netmarketshare.com/http://gs.statcounter.com/
Vocêpodeestarlendoestelivroparacriarsuaprópriaaplicaç ão.Mastalvezesteja

## Página 14

1.1. DesenvolvendoparaoiOS CasadoCódigo
procurandoumnovoemprego,paratrabalharcomtecnologiasnovas.Essetambém
éumgrandemercado,comumnúmerodevagascrescendo.
Paraestarnessemercado,sejacomumempregonovoouparadesenvolversua
própriaaplicaçãoecolocá-lanaAppStore,vocêprecisasaberprogramarparaosis-
temaoperacionaliOS.
1.1 D esenvolvendo para o iOS
Em2007,comolan çamentodoiPhone,osistemaoperacionalquerodadentrodo
dispositivotinhaocriativonomedeiPhoneOS.Comaevoluç ãodosdispositivose
achegadadoiPad,osistemamudoudenomeparaiOS.OiOSnasceudojáantigo
sistemaoperacional,oOSX.
Curiosamente,noinícionãohaviacomodesenvolverparaoiPhone. Okitde
desenvolvimento,oSDK,sóficoudisponívelem2008. Nessaépocaeleerapago,
tornando-segratuitoem2010(apesardisso,osbetassópodemserutilizadospelos
desenvolvedoresquepossuemumacontapaganaApple).
ParainstalaroSDKeprogramarparaoiOS,vocêvainecessariamenteprecisarde
umcomputadorquerodeoOSX.Basicamentevocêsópoderádesenvolvercomum
Mac.Sim,éumcomputadorbemmaiscarodoqueovalorqueestamoshabituados.
VocêpodecomprarseuMacemdiversoslugares,sendoquealgunsapresentamaté
preçosmelhoresquenaprópriaAppleStore.Nocasodevocêserestudante,háum
descontosignificativode10%,fiqueatento:
http://store.apple.com/br/browse/home/education_routing
AtualmenteoiOSSDKvemjuntocomaferramentaqueauxiliaadesenvolver
ocódigo,aIDE,quesechamaXcode. Vocêfaráapenasumúnicodownloadque
conteráambos.Veremosesseprocessodeinstalaç ãonopróximocapítulo.
1.2 C omo o livro está organizado e focado
EstelivroabordaospilaresfundamentaisdedesenvolvimentoparaiOS,cobrindo
desdeaestruturabásicadeumaplicativo,passandopordetalhesdaprincipalferra-
mentadedesenvolvimento,oXcode.Tambémveremosalgunstópicosmaisavan ça-
dos,comorequisiçõesderedeeexecuç ãoconcorrentedetarefas,alémdedetalhes
dalinguagem.Paravocêterummelhorproveitodesselivro,éimportantejápossuir
umaboaexperiênciacomumaoutralinguagemdeprogramaç ão,equesesintacon-
fortávelparautilizarestruturasdecontroleeatuarnasoluç ãodeproblemaslógicos.
2

## Página 15

CasadoCódigo Capítulo1. Introdução
Umadasprincipaispreocupaçõesquetiveaoescreverolivrofoibalancearapro-
fundidadecomaqualassuntosmaisbásicosefundamentaissãoabordados,porém
semdeixardeladoosleitoresmaisávidospordetalhestécnicos. Aapresentaç ão
defuncionalidadeserecursos,inclusivedaferramentadedesenvolvimento,muitas
vezesseráfeitademaneiraorgânica,contextualizadaemdiversosaplicativos,oque
possibilitaacriaç ãodeexemplosrelevantesepráticos.Foidadamuitaaten çãopara
acriaçãodematerialquelheinstigueaquerersemprecontinuaradiante.Todofeed-
backémaisquebemvindo.
Praticaréosegredo.Faç atestes,usesuacriatividade.Nãoseatenhaaosdiversos
exemplosquetemosaqui.Apesardeseremmuitos,aproveiteparacriareiralém.
1.3 C ódigos para download e lista de discussão
Todososprojetosapresentadosnolivroestãodisponíveisparadownloadnoende-
reçohttps://github.com/rafaelsteil/livro-ios-exemplos,incluindoaseventuaiscorre-
çõesemodificações.Alémdisso,criamosumalistaparaperguntaserespostastanto
sobreolivroquantosobreprogramaç ãoparaiOSemgeral.Oacessoélivre,através
doseguinteendere ço:
https://groups.google.com/d/forum/programacaoios
3

## Página 17

Capítulo2
HelloWorld,seuprimeiroprograma
emiOS
AplicativosparaiOSseguemumaestruturarelativamentesimples,seformoscom-
pararcomaplicaçõesquerodamemumbrowserounodesktop. Alémdisso,ao
contráriodeoutrossistemasmobile,comoAndroid,detalhesnoiOSsãomaispa-
dronizados,existindoumaquantidademuitomenordedispositivoseresoluçõesde
tela,oquesimplificamuitoavidanahoradecriaraplicativos.Quemjáfezaplica-
çõesparaawebsabeoquãodifícilécriarumsistemaquefuncionebememdiversos
tamanhosdetelas,configuraçõesvariadasdoscomputadorese,alémdissotudo,em
diferentesbrowsers.ComiOSestesproblemassãomuitomenores,poissevocêfizer
umaplicativoparaiPhone,poderáteracertezaqueelerodarádamesmamaneira
paratodososusuários.Claro,amedidaemqueosistemavaievoluindoenovasver-
sõessãolan çadasnomercado,temosquelidarasvariaçõesdeprocessador,memória
edensidadedetela.

## Página 18

2.1. Instalandoaferramentadedesenvolvimento-Xcode CasadoCódigo
Compreendendo mais a fundo resoluções e densidades
de pixel
Umaleituramuitointeressanteéopost“Pixels,pixelsoupixels?”,na
URLhttp://bit.ly/A6odLG.
Ocódigo-fontedestecapítuloestádisponívelnapasta“HelloWorld”(lembrando
queoendere çodositecomoscódigosestánaintroduç ãodolivro).
2.1 I nstalando a ferramenta de desenvolvimento -
Xcode
AAppledisponibilizagratuitamentetodasasferramentasedocumentaç ãoparade-
senvolverparaiOS,incluindoumsimuladordeiPhoneeiPadquefuncionaincri-
velmentebem,alémdoXcode,queéondetodoocódigoéescritoecompilado.A
maneiramaisfácildeobteroXcodeéatravésdaMacAppStore,disponíveldesde
versão10.6.6doOSX.
Bastaprocurarpor“Xcode”einstalargratuitamente. Ouacesseowebsiteda
ferramentaecliqueem“ViewinMacAppStore":https://developer.apple.com/xcode/
ValelembrarqueoXcodejácontémtodasasferramentasdoSDKparaoiOS(e
paraoOSXtambém!).
2.2 S eu primeiro programa
Nestase çãovamosvercomocriarumasimplesaplicaç ãoparaiPhone,doinícioao
fim.OprincipalintuitoéintroduzirasprincipaistelasefuncionalidadesdoXcode,
eirsefamiliarizandocomoeditordecódigosesintaxedalinguagem.Paratodosos
projetosdestelivrofoiutilizadaaversão5doXcode.
CrieumnovoprojetonoXcode(File->New->Project ),eescolhaotemplate
SingleViewApplication,conformeafigura 2.1,edepoiscliqueem Next:
6

## Página 19

CasadoCódigo Capítulo2. HelloWorld,seuprimeiroprogramaemiOS
Figura2.1:Selecionandootipodeprojetoasercriado
Napróximatela,demonstradanafigura 2.2,devemosinseriralgumasinforma-
çõesbásicasarespeitodoprojeto,comonome(ProductName),identificadordaem-
presa(CompanyIdentifier),eumprefixoparaaclasse(Classprefix ).Insiraosvalores
“HelloWorld”,“com.teste”e“HW”respectivamente.
OProductname éonomedoprojeto(quedepoispodesercustomizado),o
campoCompanyIdentifier éoidentificadordoprojetoqueseráutilizadonaiden-
tificaçãotécnicadoprodutoquandovocêforcadastrá-lojuntoàApple,noiTunes
Connect.Todooprocessoderegistrodoaplicativoeutilizaç ãodoiTunesConnect
serãoabordadosmaisadiantenolivro. Nãoháumaregraespecíficaparaovalor
destecampo,excetoqueeledeveserúnico. Porém,comoconven ção,costuma-se
utilizaralgoparecidocomoospackagesdoJava,normalmenteoendere çowebda
empresa,seguidodonomedoprojeto. Reparequeexisteumlabelembaixocha-
madoBundleIdentifier,queéajun çãodo CompanyIdentifiercomo ProductName.
Estasinformaçõesserãoúteismaisadiantequandoformoscadastraroprodutono
iTunesConnect,masporenquantonãosepreocupemuitocomosvaloresquefor
utilizar,jáqueestamosapenascriandoumaplicativodetestes.
7

## Página 20

2.2. Seuprimeiroprograma CasadoCódigo
Figura2.2:Informaçõessobreoprojeto
Porsuavez,ocampoopcional ClassPrefix denotaumaboapráticadeprogra-
maçãoObjective-C,queéadecolocarumprefixononomedetodasasclassespara
evitarconflitosdenomes.QuemestáacostumadocomlinguagenscomoJava,C# ou
mesmoC++,temumaliadoamaisparaevitaresteproblema,quesãoospackagesou
namespaces.EmObjective-Cnãoexisteesteconceito,portantoprecisamosgarantir
quenãoexistamnomesduplicadosemnossoprojetoe—muitoimportante—em
nenhumaoutrabibliotecadequefaç amosuso.Casoocorraumconflitodenomes,
ocompiladoriráacusarumerroeterminaroprocessodecompilaç ãodoprograma.
Nocasodesteexemplo,foiutilizadooprefixo HW,de HelloWorld.
Porúltimo,selecione“iPhone”nocampo“Devices”,poisesteaplicativoseráape-
nasparaiPhone.Asoutrasop çõespossíveissão“iPad”e“Universal”,queéumtipo
deprojetoquepoderodartantoemiPhonequantoemiPad.
CliqueemNext,eoXcodepediráparavocêsalvaroprojeto.Escolhaodiretório
desuapreferênciaecliqueem“Create”
Nestepontojátemosoprojetocriadocomasdefiniçõespadrão,evocêdeverá
verumatelaparecidacomadafigura 2.3.
8

## Página 21

CasadoCódigo Capítulo2. HelloWorld,seuprimeiroprogramaemiOS
Figura2.3:TeladoXcodeapósacriaç ãodoprojeto
Oprojetofoicriadocom5arquivos:
•HWAppDelegate.he HWAppDelegate.m
•HWViewController.he HWViewController.m
•Main.storyboard
Aclasse HWAppDelegateéaresponsávelpor,dentreoutros,eventosdeiniciali-
zaçãoetérminodoaplicativo.Éestaclassequeinicializaonossocontrollerprincipal
epermitequeousuáriopossautilizaroaplicativo.
Aclasse HWViewControlleréonossocontrollerprincipal,responsávelpor
gerenciardiversoseventosdoaplicativo—comorotaç ão,navegaç ãoparaoutros
controllersegerenciamentodaview—,eéumadasclassescomquemaistraba-
lharemosaoconstruiraplicativosparaiOS.
Porúltimo,oarquivo Main.storyboardéutilizadoparadesenharatelado
aplicativo.Maisadiantenolivroveremosafundoofuncionamentodestoryboards,
porenquantobastasaberqueéneleondeastelasserãocriadas.
9

## Página 22

2.3. Dandovidaaoaplicativo CasadoCódigo
2.3 D ando vida ao aplicativo
Aideiadesteaplicativoéesconderemostrarumatela(view )atravésdotoqueem
umbotão.Nofim,teremosvisto:
1) Comocustomizarateladocontrollerprincipal
2) ComoadicionarelementosnatelautilizandooStoryboard
3) Comolidarcomeventosdebotões
4) Comofazerumaanimaçãosimples
Editor visual de telas
Atéaversão3doXcode,astelaseramrepresentadasapenasporar-
quivoscomaextensão .xib,eeditadosatravésdeumprogramaàparte
chamadoInterfaceBuilder.Porém,apartirdaversão4,elefoiintegrado
diretamentecomoXcode. Existemdiversasformasdeintegraraparte
visualdeumarquivo .xibcomocódigo-fontepropriamentedito,oque
podecausarumpoucodeconfusãonoiníciodoaprendizado.
Alémdisso,apartirdoXcode4.2aAppleintroduziuoconceitode
Storyboards,possibilitandoassimacriaç ãoegerenciamentodetodasas
telasdoaplicativoemumúnicoarquivo,aoinvésdediversos“xibs”.De
qualquermaneira,Xibscontinuamsendoumamaneiratotalmentevá-
lidadecriarinterfaces.
Aquinolivrodetalharemosospassosnecessáriosparaquevocênão
fiqueperdidocomaquantidadedeinformações,porémnãoseapeguea
umaúnicamaneiradedesenharasinterfaces,enãodesanimecasopare ça
difícilnoinício.Rapidamentevocêveráqueofluxoébastantelógico,e
passaráatrabalharcommaisprodutividade.
Paracome çar,vamoscriaroselementosgráficosqueserãomanipulados. Para
isso,cliquenoarquivo Main.storyboard,evocêdeveráverumatelacomoada
figura2.4.
10

## Página 23

CasadoCódigo Capítulo2. HelloWorld,seuprimeiroprogramaemiOS
Figura2.4:TelainicialdoInterfaceBuilder
Oscomponentesquepodemseradicionaisnaview,comooutrasviews,botões,
seletoresdeop ções,camposdetextoeafinsestãodisponíveisna Object Library,
acessívelatravésdomenu View -> Utilities -> Show Object Library,
queporpadrãoestarálocalizadanocantoinferiordireito,conformeaimagem 2.5.
11

## Página 24

2.3. Dandovidaaoaplicativo CasadoCódigo
Figura2.5:AObjectLibrary
Nesta lista, selecione o componenteView (que é uma instância da classe
UIView)earraste-oparaateladoiPhone. AofazerissovocênotaráqueoXcode
tentaráadicionaraviewdetalformaquepreenchatodooespaçodisponível,porém
épossívelmudarotamanhosemproblemas. Feitoisso,selecioneo SizeInspector
atravésdomenuView->Utilities->ShowSizeInspector,quedeveráestarlocalizado
nocantosuperiordatela.Estajanelapermitealterardiversaspropriedadesdocom-
ponente,comotamanhoeposiç ão,cordefundoetransparência. Porhora,mude
otamanhonoscampos Widthe Heightpara 280e 150,respectivamente,e
posicione-ono Xe Y 20.Vocêpodefazerestaoperaç ãocomomousetambém.
Reparequetantoofundodatelaquantoaviewqueacabamosdeadicionartem
fundobranco-umfantasmanumatempestadedeneve.Paratrocaracordefundoda
viewselecioneo AttributesInspectoremView->Utilities->ShowAttributesInspector,
eemseguidamudeocampo“Background”parapreto,ouqualqueroutracorquelhe
agradar.
12

## Página 25

CasadoCódigo Capítulo2. HelloWorld,seuprimeiroprogramaemiOS
Figura2.6:Localizaç ãodacordefundodocomponente,noAttributesInspector
Opróximopassoéadicionardoisbotões,umparaesconderaview,eoutropara
mostrá-lanovamente.Osbotõessãodotipo UIButton.Napaletadecomponentes,
elesestãolistadoscomo Button. Botõespodemsertransparentestambém,assim
comoutilizarumaimagemcomofundo.Oprimeirobotãoseráchamado Esconder,
eosegundoseráchamado Mostrar.ExistemduasformasdefazerissopeloInterface
Builder:dandodoiscliquesemcimadobotãoeinserindootexto;ouacessando View
->Utilities->ShowAttributesInspector epreenchendoapropriedade Title.
Attributes Inspector
OAttributesInspectorpermitedefinirdiversaspropriedadesdoscom-
ponentes,variandodeacordocomotipodecadaum.Porhora,apenas
otítulodobotãonosinteressa.
Apósterfeitoestespassos,ateladeveráestarcomoafigura 2.7.
13

## Página 26

2.4. Associesuatelacomocódigo CasadoCódigo
Figura2.7:Estadodaviewapósadicionaroscomponentes
2.4 A ssocie sua tela com o código
Umaveztendocriadoatela,énecessárioassociaroscomponentescomocódigo
propriamentedito.ParaissooXcodefornecealgumasfacilidadesdearrastaresol-
tarquenoslivramdeescrevercódigorepetitivootempotodo. Ospassossãoos
seguintes:
1) AtivaroAssistantEditordoXcode
2) Escondertelasdesnecessárias
14

## Página 27

CasadoCódigo Capítulo2. HelloWorld,seuprimeiroprogramaemiOS
3) Ligaroscomponentescomocódigo-fonte
Oprimeiropassoéativaro AssistantEditor(“Editorassistente”,emumatradução
literal)doXcode,queéummododetrabalhonoqualpodemosveraomesmotempo
tantoainterfacegráficaquandoocódigo-fonte. Acesseomenu View->Assistant
Editor->ShowAssistantEditor (tecladeatalho Option + Command + Enter),
oquedeverámostrarumanovatelacomoarquivo HWViewController.haolado
dainterfacegráficaqueacabamosdemontar.
Teclas de atalho
Reparequemuitosdosmenustêmteclasdeatalho,quesãograndes
aliadasdosprogramadores.Maisadiantenolivroveremosumarelaç ão
dediversasteclasdeatalhobastanteúteisnodiaadia.
Afigura2.8mostracomofazeromesmoprocedimentoutilizandobotõesexis-
tentesnoXcode.
Figura2.8:Botãoparaativaroeditorassistente
15

## Página 28

2.4. Associesuatelacomocódigo CasadoCódigo
Agora,sevocêestivercomasconfiguraçõespadrõesdoXcode,ateladeveráestar
umaconfusãocomoadafigura 2.9,especialmenteseoseumonitornãoformuito
grande.
Figura2.9:EditorbastanteconfusodoXcode
Podemossimplificarissoescondendoastelas NavigatoreUtilities,queficamà
esquerdaeàdireita,respectivamente.Paraisso,selecioneomenu View->Navigators
->HideNavigator eView->Utilities->HideUtilities.
16

## Página 29

CasadoCódigo Capítulo2. HelloWorld,seuprimeiroprogramaemiOS
Verifique se o arquivo fonte selecionado é o.h
Importante: ospassosaseguirdevemserfeitoscomoarquivo“
HWViewController.h”selecionadonoAssistantEditor,porémalgu-
masvezesoXcodeabreinicialmenteoarquivo“ .m”.Paraefetuaratroca,
cliquenonomedoarquivonabarrasuperiordenavegaç ão,eselecione
“HWViewController.h”,conformeexemplificadonasimagens2.10e
2.11
Figura2.10:Barradesele çãodearquivo
Figura2.11:Selecioneoarquivo.h
Paraconectarcadabotãocomumaaç ãonocódigo-fontefaç aoseguinte:
17

## Página 30

2.4. Associesuatelacomocódigo CasadoCódigo
• SelecioneobotãoEscondernoInterfaceBuilder
• SegureateclaCTRL,depoiscliquecomobotãoesquerdodomouseearraste.
Vocêveráqueumalinhaaparecenatela.
• Arraste a linha para o código-fonte à esquerda (arquivo
HWViewController.h), posicionando-a logo abaixo da declaração
@interface,esolteomouse.Vejaafigura 2.12parareferênciavisualdestes
passos.
• Deveráaparecerumajanelaflutuantecomoadafigura2.13.Selecioneaop ção
ActionemConnection,enocampo Nameinsiraovalor hideView,queéo
nomedométodoquecriaremosparamanipularoaplicativo.
• Deixeorestodoscamposcomosvalorespadrão,ecliquenobotão Connect
• Repitaaoperaçãoparaobotão Mostrar,enocampo Namepreenchacom
showView
Figura2.12:Ligandoaaç ãodobotãoaocódigo
18

## Página 31

CasadoCódigo Capítulo2. HelloWorld,seuprimeiroprogramaemiOS
Figura2.13:Popupparainseriraç ãoaumbotão
Aúltimacoisaquefaltaparaquepossamoscome çaracolocaramãonocódigo
éassociara UIViewcomocódigo. Façaomesmoprocedimentorealizadopara
osbotões(selecionar,depois CTRL+arrastar),porémselecione Outletnocampo
Connection,eem Nameinsiraovalor workingView.Oresultadofinaldoarquivo
HWViewController.hdeverásercomoodalistagemabaixo:
# import <UIKit / UIKit.h>
@interface HWViewController : UIViewController
- (IBAction)hideView:(id)sender;
- (IBAction)showView:(id)sender;
@property (weak, nonatomic) IBOutlet UIView *workingView;
@end
Outlets
OutletéadenominaçãoqueoInterfaceBuilderutilizaparasere-
ferenciaraumcomponentenoarquivo .storyboardou .xibque
éreferenciadonoarquivo .h,ondeérepresentadopelapalavra-chave
IBOutlet.EleétratadodeformaespecialpeloXcode.Semosoutlets,
nãoseriapossívelacessaroscomponentescriados.
EstamosnaretafinaldonossoprimeiroaplicativoparaiOS.Oquedevemosfazer
agoraécriarocódigoqueiráesconderemostraraviewdeacordocomosbotões.
Paraissoprecisamostrabalharnoarquivo HWViewController.m,queéondefica
ocódigodefato.
19

## Página 32

2.5. Escondendoemostrandoaview CasadoCódigo
Arquivos .h e .m
AocontráriodelinguagenscomoJavaeC#,oObjective-C(assim
comoCeC++)requerumarquivoparaasdefiniçõesgeraisdaclasse,e
outroparaocódigodefato,tendoaextensão .he .mrespectivamente.
Nocapítulosobrealinguagemveremosmaisafundoofuncionamento
deles.
Paraalternarparaoarquivo .m( HWViewController.m),abranovamenteo
painelNavigator(View->Navigators->ShowNavigator,ou Command+0)eseleci-
oneoarquivonalistagem.Casoqueirafecharo AssitantEditorevoltarparaomodo
deediçãocomumúnicoarquivoporvez,selecione View->StandardEditor->Show
StandardEditor(ou Command+ENTER).
Reparequeocódigodoarquivo HWViewController.mjácontémoesque-
letodosmétodos hideViewe showView,queforamcriadospeloXcodequando
conectamososcomponentesdoarquivo Main.storyboardcomoarquivo .h.
2.5 E scondendo e mostrando a view
Comoanossa workingViewjáseiniciavisível,vamosprimeirofazerocódigopara
escondê-la.Paraisso,implementeométodo hideViewconformeexemploabaixo:
- (IBAction)hideView:(id)sender {
self.workingView.alpha = 0;
}
Éumcódigobastantesimpleseautoexplicativo,emquemudamosaopacidade
docomponentepara0,tornando-oassiminvisívelaousuário.Jáocódigoparamos-
trarnovamenteocomponenteconsisteemfazeraoperaç ãocontrária—ouseja,
mudarapropriedade alphaparaovalor 1,conformemostraalistagemabaixo:
- (IBAction)showView:(id)sender {
self.workingView.alpha = 1;
}
ParacompilarerodaroaplicativonosimuladordoiPhone,selecioneomenu
Product -> Run ( Command+R).Oresultadodeverásercomoodafigura 2.14.
20

## Página 33

CasadoCódigo Capítulo2. HelloWorld,seuprimeiroprogramaemiOS
Figura2.14:ResultadodoprimeiroaplicativoparaiPhone
2.6 A dicionar animação
Parafinalizaresteprimeiroaplicativo,podemostornarasoperaçõesdeescondere
mostrarocomponentealgovisualmentemaisagradável,atravésdeanimações.Para
tanto,modifiqueosmétodosconformeoexemploabaixo:
- (IBAction)hideView:(id)sender {
[UIView beginAnimations:nil context:nil];
self.workingView.alpha = 0;
[UIView commitAnimations];
}
21

## Página 34

2.7. Bônus-Acessaradocumentaç ãodedentrodoXcode CasadoCódigo
- (IBAction)showView:(id)sender {
[UIView beginAnimations:nil context:nil];
self.workingView.alpha = 1;
[UIView commitAnimations];
}
Rodenosimuladornovamente( Command+R)evejaadiferen ça.Muitomelhor,
não?!
2.7 B ônus - A cessar a documentação de dentro do
Xcode
AAPIdoiOSéenorme,esimplesmentenãohácomosabermosdememóriaonome
detodasclasses,métodos,propriedadeseasinfinitasregrasqueosregem.Paraisso
existeadocumentação,eoXcodetornabastantefáciloacessoaela:bastaabriropai-
nelQuickHelp(“Ajudarápida”,literalmente)atravésdoatalhoOption + Command
+ 2,ouatravésdomenu View->Utilities->ShowQuickHelpInspector,edepoiscli-
carnoeditordecódigosemcimadaclasseacujadocumentaç ãosedesejateracesso,
conformemostraafigura 2.15.
Figura2.15:Acessandoaajudarápida
22

## Página 35

Capítulo3
MaisObjective-CeXcode
AgoraquejávimosaestruturabásicadeumaplicativoiOS,tendopassadopelopro-
cessodecriaçãodeumprojeto,algumasteclasdeatalhoefuncionalidadesdoXcode,
vamosdarumpassoadianteecriarumaplicativoumpoucomaiselaborado. Ao
mesmotempo,exploraremosmaisafundooXcodee,principalmente,alinguagem
Objective-C.Detalharemosmaisalinguagemdeprogramaç ão,porémsementrar
emaspectosavan çados,oqueéfeitonocapítulo 11.
Oaplicativoqueiremoscriarconsistenocadastrodeempresasparaumcatálogo,
mostrandoalistagemdetodasempresascadastradascadavezqueumnovoregistro
éinserido. Afigura3.1mostraondechegaremoscomonossoaplicativo. Durante
aconstruçãodeste,nãodeixedetestarideiasedeixarsuacuriosidadeajudá-loa
aprendermais.

## Página 36

3.1. Criandooprojeto CasadoCódigo
Figura3.1:Oaplicativoqueiremosconstruir
Ocódigo-fontedestecapítuloestádisponívelnapasta“CatalogoEmpresas”(lem-
brandoqueoendere çodositecomoscódigosestánaintroduç ãodolivro).
3.1 C riando o projeto
AbraoXcodeecrieumnovoprojetoatravésdomenu File->New->Project (tecla
deatalhoSHIFT+Command+N )eselecioneotipo SingleViewApplicationeclique
nobotão Next.Napróximatelainsiraonome CatalogoEmpresasnocampoPro-
ductName,em CompanyIdentifiercoloque com.teste,deixeocampo ClassPrefix
embrancoeselecione“iPhone”emDeviceFamily.Vejaafigura 3.2parareferência.
Cliqueem Nextparasalvaroprojeto.
24

## Página 37

CasadoCódigo Capítulo3. MaisObjective-CeXcode
Figura3.2:Op çõesdonovoprojeto
Os diferentes templates de projetos
Apesardonome,otemplatedeprojeto SingleViewApplication (ou
“aplicaçãocomumaúnicaview”)nãoélimitadoaumaúnicatela,mas
simqueocódigoinicialqueoXcodeirácriarparavocêteráumatelaini-
cial,ficandoacargododesenvolvedorcriaroquemaisprecisar.Osou-
trostiposdetemplatesseguemamesmalógica,porémadicionandopor
padrãoalgumascoisasamais,comooa TabbedApplication,quecriaaes-
truturabaseparaumprojetoqueuseuma“tabbar”(aquelecomponente
comumabarrainferiorcomváriosícones),oua UtilityApplication,que
criaumprojetojácomduasviewseumbotãoparaalternarentreelas.
Nosexemplosdestelivroiremossempreutilizara SingleViewAp-
plicationporseramaispráticaparaospropósitosapresentados. Aliás,
estemuitoprovavelmenteseráotemplatequevocêmaisutilizaráquando
criarseusprópriosaplicativos.
25

## Página 38

3.2. EntendamelhorainterfacedoXcode CasadoCódigo
3.2 E ntenda melhor a interface do Xcode
Afigura3.3mostraaestruturageraldoXcode,comospossíveispainéisdetrabalho
abertos,sendoquecadaumdestespainéiséutilizadoparadiferentespropósitos—
nessafigura,apresentamosapenasumadascombinaçõespossíveis,queéaseguinte:
1) Navegadordoprojeto,ouapenas Navigator,oqualcontémarelaç ãodearquivos
doprojeto( Command + 1),errosdecompilaç ão,logs,buscaeoutrasfuncio-
nalidades. Tecladeatalho: Command + 1 paraabrir,e Command + 0 para
esconder(menu View->Navigators paraarelaç ãocompleta)
2) Editorprincipaldecódigoecriaç ãodetelas, chamadooficialmentede Stan-
dardEditor.Dependendodaconfiguraç ãopodemostrarmaisdeumarquivoao
mesmotempo.Tecladeatalho: Command + ENTER.Paraalternarparaomodo
detrabalhoempar,noqualatelaficadivididaentredosarquivosdiretamente
relacionados,atecladeatalhoé Command + Option + ENTER.
3) Paineldedebugging(“depuração”)emensagensdeloggeradaspeloaplicativo.
Teclasdeatalho: Command + SHIFT + Y e Command + SHIFT + C (menu
View->DebugArea)
4) PainelUtilities,oqualcontémutilidadesgeraisdeacordocomoarquivoaberto
noStandardEditor,taiscomodocumentaç ão(quandoeditandocódigo-fonte)ou
propriedadesdealgumcomponentevisual(quandoeditandoarquivos .xib)
5) Botõesdeacessorápidoparaoseditoresepainéisjádescritos.
26

## Página 39

CasadoCódigo Capítulo3. MaisObjective-CeXcode
Figura3.3:OspainéisdoXcode
Termos em inglês
Aoreferenciarmenuseop çõesdoXcodeutilizaremosprimeiroo
termooriginaleminglêse,quandopertinente,umatraduç ãoliteralem
português,poisdestaformaserámaisfácilparavocêprocurarajudae
documentaçãonaInternet,mesmoquenãodominetotalmenteoinglês.
3.3 C riar a tela de inserção de empresa
Oprimeiropassoémontaratelaparaquepossamosposteriormenteacessaroscom-
ponentesgráficosnocódigo-fonte.Selecioneoarquivo Main.storyboardnoPro-
jectNavigator( Command + 1)evocêseráapresentadocomatelaquecorresponde
àquelaqueserávistapelousuárioaorodaroaplicativo.Oobjetivoaquiéconstruí-la
damesmaformacomofoiapresentadonafigura 3.1noiníciodocapítulo.
27

## Página 40

3.3. Criarateladeinser çãodeempresa CasadoCódigo
Passos detalhados
Aoescreverestelivronospreocupamosbastanteparamanterumbom
balanceamentoentremostrarpassoapassocomorealizardeterminadas
coisas,versusapresentarumainstruç ãomaiscurtaedireta.Noscapítulos
iniciais,eespecialmentenesteemqueapresentamosemmaisdetalheso
funcionamentodoXcodeeObjective-C,éfeitobastanteusodeimagens
paraguiaroleitorparadeterminadosmenusebotões(alémdeexplicar
osatalhosdeteclado),poisoXcodeutilizaosmesmospainéisparadife-
rentestarefas,oqueàsvezespodeficarbastanteconfuso.
Vamosmodificaracordefundodatelaprincipal,colocandoumtomdecinza
claro. Cliqueemqualquerpartedateladoaplicativoeabrao AttributesInspector
(“Inspetordeatributos”)utilizandoatecladeatalho Option + Command + 4,
ouatravésdomenu View->Utilities->ShowAttributesInspector.Vejaafigura 3.4
parareferência.
Figura3.4:AbriroAttributesInspector
Paramodificaracordefundocliquenoitem“Background ”paraabrirajanela
flutuante“Colors”,eselecioneaopção“ColorSliders”nabarrasuperior.Emseguida,
selecione“RGBSliders”einsiraovalor“250”paraostrêscampos,conformemostra
afigura3.5.Fecheajanela“Colors”.
28

## Página 41

CasadoCódigo Capítulo3. MaisObjective-CeXcode
Figura3.5:Modificandoacordeumcomponente-nocaso,acordefundodatela
3.4 A dicionar componentes visuais
Abraa ObjectLibrary naparteinferiordopainel Utilitiesutilizandoatecladeata-
lho CTRL + Option + Command + 3,ouatravésdomenu View->Utilities->
ShowObjectlibrary,eadicioneosseguintescomponentes,posicionando-osparaque
fiquemcomoafigura 3.1,mostradanoiníciodestecapítulo.
•Labelcomotexto“Nome da empresa”(dêduplocliquenolabel,ouentão
preenchaapropriedade TextnoAttributesInspector).
• UmcomponenteTextField paraousuáriodigitaronomedaempresa. No
AttributesInspectorlocalizeaop çãoPlaceholderedigite“Informe o nome
da empresa”-umplaceholderéumvalorpadrãoqueo TextFieldirámostrar
enquantoousuárionãoinseriralgumtexto.
•Labelcomotexto“Funcionários”.
29

## Página 42

3.4. Adicionarcomponentesvisuais CasadoCódigo
• OutrocomponenteTextField,paraaquantidadedefuncionários. No Attri-
butesInspectorlocalizease çãoControledesmarqueocheckbox Enabled,pois
queremosqueousuáriomodifiqueocampoutilizandoocomponente Stepper
(vejaabaixo).Nocampo Textinsiraovalor“0”,queseráaquantidadeinicial
defuncionáriosdaempresa.
• UmcomponenteStepper: queseráutilizadoparaaumentaroudiminuira
quantidadedefuncionários.
• UmbotãoButtoncomotexto“Salvar”(propriedadeTitle,ouduploclique
nocomponente).
• UmcomponenteLabelcomotexto“Dadossalvoscomsucesso”,alinhadoao
centro(propriedade AlignmentnoAttributesInspector),edalarguradatela.
NotequeaomodificarotamanhodocomponenteoInterfaceBuildermostra
linhasguiaparaauxiliaroposicionamento,conformeafigura 3.6.
Sãomuitoscomponentes!Pratiqueosdiversostipos,emespeciaisosqueesta-
mosutilizandoagora.Elesserãonecessárionagrandemaioriadassuasaplicações.
Figura3.6:GuiasdoXcodeauxiliandonoposicionamentoealinhamentodoscom-
ponentes
30

## Página 43

CasadoCódigo Capítulo3. MaisObjective-CeXcode
Rodeoaplicativonosimuladoratravésdatecladeatalho Command + R,ou
pelomenu Product->Run,paraveroresultadoatéomomento. Sevocêinteragir
comoselementosveráquenãoacontecerámuitacoisa,poisaindanãoconectamos
oseventosaocódigo,oqueseráfeitoemseguida.
3.5 A tenção para as propriedades simuladas
OAttributesInspectortemumase çãochamada SimulatedMetrics,queserveunica-
mentepara simularalgunselementosdeinterface,parafacilitaroposicionamento
doscomponentesemcertostiposdeaplicativos.Contudo,tenhaemmenteque,em-
boraousodaspropriedadesdase çãoSimulatedMetricsresulteemalteraçõesvisuais,
elassãoapenastemporárias,nãotendoqualquerimpactopráticonoaplicativo.Veja
afigura3.7parareferência.
Obs:casovocêestejanoarquivo Main.storyboard,oboxdaspropriedades
simuladassomenteirãoaparecercasoselecioneabarrapretanaparteinferiordatela
(aquelaquetemtrêsbotões,umamarelo,outrolaranjaeoúltimoverde). Sevocê
apenasclicarna“tela”(apartequeembrancoquerepresentaoiPhone),oboxnão
aparecerá.
31

## Página 44

3.6. Conectandooseventosecomponentesaocódigo CasadoCódigo
Figura3.7:Elementosdeinterfacesimuladosapenas.Elesnãoirãoaparecernoapli-
cativodefato.
Apossibilidadede simularalgumascoisaspodeserútilparavocêconstruirde
maneiramaisfácilatela,seemalgummomento(muitoprovavelmenteviacódigo)
pretendeinseriroscomponentes“deverdade”.
3.6 C onectando os eventos e componentes ao có-
digo
Damesmamaneiraquefizemosnocapítuloanterior,precisamosconectaroscompo-
nentesgráficoscomocódigoparaquesejapossívelacessá-losdefato—atéentão,o
queéfeitonoarquivo Main.storyboardnãotemqualquerrelaç ãocomcódigo.A
primeiracoisaafazeréabriro AssistantEditor( Option + Command + ENTER)
paravisualizaroarquivo ViewController.haoladodo Main.storyboard.
Lembre-seque,casooarquivoexibidosejao ViewController.m(aoinvésdo“
.h”),vocêdeveprimeiroalterná-los.
32

## Página 45

CasadoCódigo Capítulo3. MaisObjective-CeXcode
Alternando entre os arquivos .h e .m
Épossívelalternarrapidamenteentrearquivos .he .mrelacionados
utilizandoatecladeatalho CTRL + Command + Seta para cima
(lembre-sedeprimeiroclicarnaáreaondetemalgumcódigo),ouentão
clicandononomedoarquivonabarradenavegaç ão,conformeafigura
3.8.
Figura3.8:Alternandoentrearquivosutilizandoabarradenavegaç ão
Fechando os painéis desnecessários
ÉmuitofácildeixardiversospainéisabertosnoXcode,aumentando
bastanteapoluiçãovisualeconsequentementediminuindoaáreadispo-
nívelparatrabalhar,especialmentesevocêestáemumatelapequena.
Nessescasosbastaesconderoquenãoforvital, comoo Navigator(
Command + 0,ou View->Navigators->HideNavigator ),opainelde
Debug( Command + Shift + Y,ou View->DebugArea->HideDe-
bugArea)eopainel Utilities( Option + Command + 0,ou View->
Utilities->HideUtilities::)
Aconexãodoscomponentesdeveserfeitadaseguinteforma:
33

## Página 46

3.6. Conectandooseventosecomponentesaocódigo CasadoCódigo
• Selecioneocampodetextodonomedaempresa,segureCTRLecliqueear-
rasteparaoarquivo ViewController.h,posicionandoentre @interface
e end.Najanelaflutuantequeabrirselecioneovalor“Outlet”napropriedade
Connectioneinsiraoovalor“nomeField”napropriedadeName.Issoirácriar
avariáveljácomaspropriedadescorretas.
• Repitaomesmoprocessoparaocampodetextodaquantidadedefuncioná-
rios,colocandocomonomeovalor“quantidadeField”
• ParaocomponenteStepper,queéaquelecomumbotão -eoutro +,realize
omesmoprocedimentodeconexão,porémnocampo Connectionselecioneo
valor“Action”paragerarummétododeaçãoaoinvésdecriarumavariável
simples. NocampoNameinsiraovalor“incrementadorAlterado”,queserá
onomedométodoqueseráexecutadotodavezqueousuáriointeragircom
ocomponente,edeixeosoutroscamposcomosvalorespadrão(Type “ID”,
Event“Valuechanged”eArguments“Sender”)
• Paraobotãosalvar,crieaConnectiondotipo“Action”,comoName“salvar”,e
oaceiteovalorpadrãodorestodoscampos
• Porúltimo,conecteolabelquetemotexto“Dadossalvoscomsucesso”cri-
andouma Connectiondotipo“Outlet”,eoName“avisoSucessoLabel”
Nestepontooarquivo ViewController.hdeveráestarcomoocódigoabaixo:
# import <UIKit / UIKit.h>
@interface ViewController : UIViewController
@property (weak, nonatomic) IBOutlet UITextField *nomeField;
@property (weak, nonatomic) IBOutlet UITextField *quantidadeField;
@property (weak, nonatomic) IBOutlet UILabel *avisoSucessoLabel;
- (IBAction)incrementadorAlterado:(id)sender;
- (IBAction)salvar:(id)sender;
@end
Sevocêabriroarquivo ViewController.mveráqueoXcodejácriouparaa
genteocorpodosmétodos incrementadorAlterado:e salvar:.
34

## Página 47

CasadoCódigo Capítulo3. MaisObjective-CeXcode
O que exatamente é IBOutlet e IBAction?
Osmodificadores IBOutlete IBActionsãousadosunicamente
comomarcadoresparaintegrarcomponentesdoInterfaceBuildercom
ocódigo-fonteemarquivos .h.Oprimeiroéusadoquandoqueremos
referenciarocomponentenocódigoatravésdeumavariável,eosegundo
éusadoexclusivamenteparaaçõesdoscomponentes,comootoqueem
umbotão. Portrásdospanos,oqueoXcodefazéanalisarocódigoe
automaticamenterealizarasdevidasconexõesentreainterfacegráficae
onossocódigo.
3.7 U ma classe para representar uma empresa
Agoraquejátemosatelacriada,éhoradecolocaramãonocódigo,eoprimeiro
passoécriaraclasse Empresaparaarmazenarasinformaçõespreenchidaspelo
usuário. Paraisso,abraajaneladeadiç ãodearquivos( Command + N,ouentão
File->New->File...),eselecioneotemplate Objective-Cclass.Cliquenobotão Next,
insiraovalor“Empresa”nocampoClass,eem Subclassofselecioneoitem“NSObject”.
CliqueemNext::parasalvaroarquivo.
Importante
Aoincluirarquivosemqualquerprojetoquefortrabalhar,certifique-
sedequeaop çãoTargetsestejaselecionadanacaixadediálogodesalvar
arquivoconformemostraafigura 3.9.Issoénecessárioparaassociaro
arquivocomoprojeto—docontrário,oXcodeignorá-lo-ianahorade
compilareempacotaroprojetoparadistribuiç ão. 35

## Página 48

3.7. Umaclassepararepresentarumaempresa CasadoCódigo
Figura3.9:Targetcorretamenteselecionado
Alternando nov amente entre os painéis
TrabalharnoXcodeéumprocessoconstanteentreesconder,mostrar
emudarotipodospainéisdeacordocomatarefaaserfeita,demodo
quenossaprodutividadeaumente.Nocasodestase ção,ondejácriamos
atelaevamosfocarmaisemcódigo,nãoénecessáriomanteroarquivo
Main.storyboardabertoenemopainel Utilities.Alterneparao Stan-
dardEditor utilizandoatecladeatalho Command + ENTER,eesconda
ooutropainelcomoatalho Option + Command + 0,eselecioneo
arquivo ViewController.mnoNavigator( Command + 1)
Anossaempresatemduaspropriedades: nome(umastring)equantidadede
funcionários(númerointeiro).Abraoarquivo Empresa.hemodifique-oparaficar
comoocódigoabaixo:
1 # import <Foundation / Foundation.h>
2
36

## Página 49

CasadoCódigo Capítulo3. MaisObjective-CeXcode
3 @interface Empresa : NSObject
4
5 @property (nonatomic, retain) NSString *nome;
6 @property (nonatomic, assign) int quantidadeFuncionarios;
7
8 @end
Nãoénecessáriofazerqualquermodificaç ãonoarquivo“Empresa.m”.
3.8 C abeçalhos e implementações
EmObjective-C,adeclaraç ãoeimplementaç ãodaclasseficamemarquivosdiferen-
tes. Adeclaração,ou—usandootermocorreto— interface,ficaemumarquivo
comaextensão .h,de header(cabeçalho),enquantoqueaimplementaç ãoficaem
umarquivocomaextensão .m.Diferentementedeoutraslinguagens,nasquaisse
usaapenasumarquivoparatudooquedizrespeitoàclasse,emObjective-Cvocê
sempreprecisarádadupla .he .m.
Noarquivodecabe çalho(comoo Empresa.h)ficaadeclaraç ãodaclasse,das
variáveisdeinstância,daspropriedades,dosmétodosdeinstânciaedosmétodosde
classe.
Nota sobre @interface
Adeclaração @interfaceésemanticamentemuitodiferenteda
mesmapalavra-chavenoJavaeC#, emquerepresentaumdetermi-
nadocontratoqueaclassedeveseguir.EmObjective-C, @interface
serveunicamenteparadeclararaclasse,eoequivalentedapalavrachave
interfacedoJavaedoC# é @protocol,queveremosemumoutro
capítulo.
Enquantoocabe çalhodefineapenasaestruturageraldaclasse,enãoocó-
digopropriamentedito,oarquivo .mcontémo“códigodeverdade”,comoarquivo
ViewController.mou Empresa.m.
37

## Página 50

3.9. Informandoaquantidadedefuncionários CasadoCódigo
Curiosidade sobre a extensão .M
Aextensão .mdoObjective-Coriginou-seapartirde“mensagens”
(dotermoeminglêsmessages),aqualserefereaumdosprincipaiscon-
ceitosdalinguagem.
3.9 I nformando a quantidade de funcionários
Estamosnametadedocaminho,masorestoésócódigo!Agoraquetemosatelaea
classe Empresavamoscolocarasaçõesnosmétodosdeincrementaraquantidade
defuncionáriosesalvaraempresaemsi. Comovistonafigura 3.1atelacontêm
doiscomponentesquedevemtrabalharemconjuntoparaalteraraquantidadede
funcionarios:umcampodetexto(UITextField )eumincrementador(UIStepper ).O
quequeremosqueaconte çaéquequandoousuáriotocaremalgumdosbotões,o
valorcorrespondenteapare çano UITextFieldaolado.
No arquivo ViewController.h criamos uma IBAction chamada
incrementadorAlterado:, que é o método a implementar. Abra o arquivo
ViewController.mefaçaoseguinte:
1 - (IBAction)incrementadorAlterado:(id)sender {
2 UIStepper *incrementador = (UIStepper *)sender;
3 self.quantidadeField.text = [NSString stringWithFormat:@"%d",
4 (int)incrementador.value];
5 }
Ométodo incrementadorAlterado:segueumpadrãobastantecomumem
Objective-C,queéodereceberumargumentodotipo idchamado senderquando
forassociadoaalgumevento. Nocaso, idpodeserlidocomo“qualquercoisa”,e
sender(“remetente”,“quemenviou”)éapenasonomedavariável—vocêpode
modificarparaoqueacharmaisapropriado,apesardeesteseronomeutilizado
emtodadocumentaç ão. Levandoissoemconsideraç ão,nalinha2convertemos
senderparaotipo UIStepper,poissabemosqueestemétodoseráchamadoape-
nasquandoo UIStepperdatelaformodificado.Jánaslinhas3e4convertemos
parastringovalornuméricodocomponenteexistentenapropriedade value,pois
o UITextFieldnãoaceitanúmerosdiretamente.
Rodeoaplicativoatravésdoatalho Command + R ouatravésdomenu Product
->Run ecliquenosbotões -e +,paraverocampodetextoreceberosvalores.
38

## Página 51

CasadoCódigo Capítulo3. MaisObjective-CeXcode
3.10 T rabalhe com objetos: instanciando uma Em-
presa
Paracriarumanovaempresaprecisamosdeinstânciasdaclasse Empresaepreen-
cheraspropriedades nomee quantidadeFuncionarios.Issoseráfeitonaaç ão
dobotão“Salvar”,conformemostrandonocódigoabaixo:
1 - (IBAction)salvar:(id)sender {
2 Empresa *e = [[Empresa alloc] init];
3 e.nome = self.nomeField.text;
4 e.quantidadeFuncionarios = [self.quantidadeField.text intValue];
5
6 NSLog(@"Empresa criada. Nome=%@, funcionários=%d",
7 e.nome, e.quantidadeFuncionarios);
8 }
Na linha 2 criamos uma nova instância da classeEmpresa, enquanto que
naslinhas3e4preenchemosaspropriedadescomosvaloresdoscomponentesda
tela. Estassãoaquelasmesmasvariáveiscom @propertyexistentesnoarquivo
Empresa.h.Naslinhas6e7escrevemososvaloresnoconsoleparafinsdedebug-
ging.
Compile o projeto com o atalhoCommand + B. Funcionou? A menos
que você tenha importado o arquivoEmpresa.h logo no início do arquivo
ViewController.m,oXcodedeveráteracusadoerrosdecompilaç ãoinformando
queaclasse Empresanãoexiste. Pararesolveresteproblema,adicionealinha
#import "Empresa.h" notopodoarquivo ViewController.m,recompileo
projetoerode-ocom Command + R.
O painel de debug e console do Xcode
Rodeoaplicativo,insiraonomeequantidadedefuncionáriosecliquenobotão
salvar.OXcodedeverámostrarautomaticamenteumamensagemdelognopainel
inferior(casocontrário,abra-oatravésdoatalho Command + Shift + C,oupelo
menuView->DebugArea->ActivateConsole),conformeafigura 3.10.Comovocê
jáassociou,afun ção NSLogserveparajogarinformaçõesnoconsoledoXcode,
oqueéútilemdiversosmomentosduranteociclodedesenvolvimentoetestesdo
aplicativo.
39

## Página 52

3.11. ComosãoasstringsemObjective-C? CasadoCódigo
Figura3.10:LocalizaçãodoconsolededebugcomsaídadoNSLog
3.11 C omo são as strings em Objective-C?
StringsemObjective-Csãorepresentadaspelaclasse NSString,eseusvaloresde-
vemserprecedidospelocaractere @(arroba).Issoénecessárioparasedistinguirdo
arraydecaracteresdalinguagemC(tecnicamente,instruçõescomo char *),na
qualObjective-Céfundamentada.
AformacorretadecriarstringsemObjective-Cémostradaabaixo:
// OK - utiliza '@'
NSString *nome = @"Rafael Steil";
40

## Página 53

CasadoCódigo Capítulo3. MaisObjective-CeXcode
// ERRO - o código abaixo não irá funcionar
NSString *ops = "ObjC não funciona assim";
3.12 F ormatando strings
Épossívelconstruirstringsutilizandoalgunscaracteresespeciaisdeformataç ãoatra-
vésdométodo stringWithFormat:,conformemostradoabaixo:
double faturamento = 1234.567;
NSString *mensagem = [NSString stringWithFormat:
@"A empresa %@ tem %d funcionários, e faturamento de R$ %f",
e.nome, e.quantidadeFuncionarios, faturamento];
Alistadeformatadoresérelativamenteextensa,porémosmaiscomunssão:
•%@ :paraqualquertipode objeto,incluindooutras NSStrings
•%d :númerosinteiros( inte unsigned int)
•%f :númerosdepontoflutuante( floate double)
Afun ção NSLogjáaceitapordefiniç ãoestamesmaestruturadeformataç ão,
semsernecessárioautilizaç ãode stringWithFormat:.
3.13 G uardando todas empresas em memória
Ocódigoquefizemosatéagoracriaaempresa,masnãoaarmazenaemnenhum
lugar,porémnósqueremosmanterumarelaç ãodetodososregistrosqueforamin-
seridosemostrarnoconsolearelaç ãocompletaacadanovaempresa. Existeuma
infinidadedemaneirasderealizarestatarefa,eparaopropósitodestecapítulo—
queéapresentaremmaioresdetalhesoXcodeealinguagemObjective-C—vamos
nosconcentraremalgosimpleseprático,comoumalistaemmemória,utilizandoa
classe NSArray.
NSArray versus array
Apesardeconterapalavra“array”nonome,tecnicamenteaclasse
NSArraynãoéumarraynoconceitoformaldalinguagem,massimse
equivalemuitomaisauma lista,algocomoaclasse ArrayListdeJava
eC#.
41

## Página 54

3.13. Guardandotodasempresasemmemória CasadoCódigo
Aprimeiracoisaafazeréirparaoarquivo ViewController.h(tecladeata-
lho CTRL + Command + Seta para cima)edeclararumavariávelchamada
catalogodotipo NSMutableArray,conformeexemplificadoabaixo:
1 # import <UIKit / UIKit.h>
2
3 @interface ViewController : UIViewController { // Abre chave aqui
4 NSMutableArray *catalogo;
5 } // Fecha chave aqui
6
7 // Este código abaixo já havia sido feito anteriormente
8 @property (weak, nonatomic) IBOutlet UITextField *nomeField;
9 @property (weak, nonatomic) IBOutlet UITextField *quantidadeField;
10 @property (weak, nonatomic) IBOutlet UILabel *avisoSucessoLabel;
11 - (IBAction)incrementadorAlterado:(id)sender;
12 - (IBAction)salvar:(id)sender;
13
14 @end
Ocódigoreferenteaestase çãoéodalinha4, lembrandoqueénecessário
adicioná-loentrechaves(finaldalinha3elinha5),comofoiexplicadoanterior-
mentenase çãodaclasse Empresa.Dalinha8emdianteéocódigoquecriamos
anteriormente,efoiadicionadonalistagemapenasparareferência.
Voltandooarquivo ViewController.m(lembradatecladeatalho?),vamos
criarométodoparaarmazenarasempresasnoobjeto catalogo,edepoischamaro
métodonaaçãodobotão“Salvar”.Adicioneoseguintecódigologoantesdométodo
- (IBAction)salvar:(id)sender:
1 -(void) salvaEmpresa:(Empresa *) novaEmpresa {
2 if (!catalogo) {
3 catalogo = [[NSMutableArray alloc] init];
4 }
5
6 [catalogo addObject:novaEmpresa];
7 }
Nalinha6adicionamosnalistaoobjeto novaEmpresapassadocomoargu-
mentoaométodo.Jáaslinhas2e3precisamdeumaexplicaç ãomaisdetalhada:em
Objective-Cobjetosnão-instanciadoscontêmporpadrãoovalor nil(queéum
primopróximodo NULLdeJava,C# edopróprioCeC++).Alémdisso,nalingua-
gemosvalores nile 0(zero)sãotratadoscomo“falso”emexpressõescondicionais,
42

## Página 55

CasadoCódigo Capítulo3. MaisObjective-CeXcode
damesmaformaque qualquercoisaquenãoseja nilou 0éconsideradacomo“ver-
dadeiro”emcondicionaisbooleanas.Emoutraspalavras,osseguintescódigossão
equivalentes:
// OK
if (!catalogo) {
}
// OK - mesmo efeito do exemplo anterior
if (catalogo == nil) {
}
Porfim,nalinha3criamosumanovainstânciadefatodo NSMutableArray
NSArray versus NSMutableArray - imutável e mutável
AlgumasclassesdoSDKdoiOScontêmversõesimutáveis(queapós
criadasnãopodemmaissermodificadas)eversõesmutáveis(quepo-
demsermodificadaslivremente),comoéocasodo NSArray(imutá-
vel)e NSMutableArray(mutável).Saberquandousarumaversãoou
outradependeexclusivamentedasnecessidadesdecadapartedocódigo.
Outrasclassesimutáveisquetêmversõesmutáveissão NSDictionary,
NSSet, NSDatae NSString.
3.14 L istando todas as empresas do catálogo
Aproveitandoqueestamosembalados,vamoscriartambémumoutrométodoque
listatodasasempresasadicionadasao catalogo.Adicioneoseguintecódigologo
apósométodo salvaEmpresa:
-(void) mostraCatalogo {
NSLog(@"******* Listando todas empresas *******");
for (Empresa *empresa in catalogo) {
NSLog(@"A empresa %@ tem %d funcionários",
empresa.nome, empresa.quantidadeFuncionarios);
}
}
43

## Página 56

3.15. VençaasintaxedoObjective-C:invocaç ãodemétodos CasadoCódigo
Modifiqueométodo salvar:pararemoveraantigachamadaa NSLog,ein-
voqueosdoisnovosmétodosquecriamos.Confiraabaixo:
- (IBAction)salvar:(id)sender {
Empresa *e = [[Empresa alloc] init];
e.nome = self.nomeField.text;
e.quantidadeFuncionarios = [self.quantidadeField.text intValue];
[self salvaEmpresa:e];
[self mostraCatalogo];
}
Rodenovamenteoaplicativonosimuladoratravésdatecladeatalho Command
+ R (oupelomenu...vocêaindalembraqualé?)einsiraalgumasempresas,paraver
oresultadodoaplicativoatéomomento.
3.15 V ença a sintaxe do Objective-C:invocação de
métodos
AassinaturademétodosemObjective-Céalgobastanteparticulardalinguagem,e
podeserumpoucocriptográficonumaprimeiraolhada.Umadasinten çõesdoscri-
adoresdalinguagemfoicriarumasintaxedeclarativaefácildeler,quenãodeixasse
margemparadúvidasemrelaç ãoaoquesereferecadavalorpassadoaométodo.Se
issoéalgobomouruim,cabeavocêdecidir.
Considereoseguintecódigo,retiradodaclasse NSMutableArray:
- (void) insertObject:(id) objeto atIndex:(NSInteger) indice;
Adeclaraçãodométodocome çacomotipodeacesso,seguidodotipoderetorno
edonomedométodo.Seométodocome çacomosinaldesoma( +)significaqueele
éummétododeclasse(queéalgopróximoao staticdoJavaeC#),esecome çar
comosinaldesubtraç ão( -),éummétododeinstância.Veremosmaissobreisso
nocapítulosobreObjective-Cavan çado.O retornopodeserqualquertipoválidode
Objective-CouC,como int, float, id, NSInteger, voidetc.
Parapassar umargumentoparaométodoébastantesimples,bastandoutilizaro
sinaldedoispontos(“:”)parasepararonomedométododavariável.Porexemplo,
ocódigoabaixoinsereumaempresaemumaposiç ãoespecífica:
[catalogo insertObject:empresa atIndex:3];
44

## Página 57

CasadoCódigo Capítulo3. MaisObjective-CeXcode
Todainvocaçãodemétodoprecisaserfeitaentrecolchetes,aninhando-oscon-
formenecessário(ouseja,colchetedentrodecolchetedentrodecolchete). Sim,o
códigoficaumpoucodifícildeler,emespecialenquantovocêestáaprendendomais
dalinguagem.
Jáummétodoquerecebemúltiplosargumentospodeassustarumpoucomais
(pelomenosassustouamim,porsemanas),porémcompreendersuaestruturaé
fundamental. Considereoseguintemétodo,tambémde NSMutableArray,que
serveparasubstituirumapartedoselementoscomobjetosdeoutro NSArray:
- (void)replaceObjectsInRange:(NSRange) range
withObjectsFromArray:(NSArray *) outroArray
range:(NSRange) rangeDoOutroArray
Paraefeitosdecomparaç ão,omesmométodoemJavaseriadeclaradoparecido
comisso::
void replaceObjectsInRange(NSRange range, NSArray outroArray,
NSRange rangeDoOutroArray);
Paravisualizarmelhoraformaç ãoda assinaturadométodo,vejaafigura 3.11
Figura3.11:EstruturadaassinaturadeummétodoemObjective-C
Noteque,emboraassustadoremumprimeiromomento,opadrãodeconstruç ão
paraosdemaisargumentosserepete,sendoformadosemprepor3partes:apalavra
quefarápartedo nomedométodo,otipodavariáveleonomedavariávelemsi.
45

## Página 58

3.16. Criandoinstânciasdeobjetos CasadoCódigo
Éestaúltimaqueseráutilizadadentrodométodo.Muitasvezes,apalavraquefaz
partedonomedométodoeavariávelcostumamseriguais,masissonãoéumaregra.
Anomenclaturairávariardeacordocomcadacaso,sendoqueomaisimportante
équevocêutilizenomesquefaçamsentidoaocontextodeuso.Considereoexemplo
abaixo,deummétodoquerecebeonomeequantidadedefuncionáriosdeuma
empresa,eretornaumainstânciadaclasse:
-(Empresa *) criaEmpresaComNome:(NSString *) nome
comNumeroDeFuncionarios:(int) quantidade {
Empresa *e = [[Empresa alloc] init];
e.nome = nome;
e.quantidadeFuncionarios = quantidade;
return e;
}
Parainvocar,fazemos:
Empresa *novaEmpresa = [self criaEmpresaComNome:@"Jujubas LTDA"
comNumeroDeFuncionarios:3];
Averbosidadedonomedosmétodostemummotivoespecial,queéfazercom
queocódigosejafácildelereexpressebemodomínionoqualéaplicado.
3.16 C riando instâncias de objetos
ParapodercriarinstânciasdeclassesemObjective-Csãonecessáriosdoispassos:
alocarmemória,einiciaroobjeto.Estespassosgeralmentesãofeitosemconjunto,e
oobjetosomentepoderáserutilizadodepoisqueestesdoispassostiveremsidocom-
pletadoscomsucesso.Tambémnãoexisteoconceitode construtorespropriamente
ditos,massimde inicializadores,queporpadrãochama-se init. Vejaocódigo
abaixo:
Empresa *e = [[Empresa alloc] init];
Aprimeirapartedoprocessodeinstanciaç ãoocorrecomométodo alloc,
oqualreservamemórianecessáriaparatodasasvariáveisdeinstânciaeasinicia
comosvalorespadrão. Emseguida,ométodo initpreparaainstânciadefato,
permitindoquesejautilizada. Ométodo initretornaumtipo id,queécomo
um“ponteiroparaqualquerobjeto";pensenelecomosendoumprimodo Object
46

## Página 59

CasadoCódigo Capítulo3. MaisObjective-CeXcode
deJavaeC#,contudo muitomaisabrangente(existeotipo NSObject,porém).
initédisponibilizadoporpadrão,nãosendonecessárioquevocêimplemente-o
todavez.Entretanto,casoqueirafazerumarotinadeinicializaç ãodoobjeto,basta
sobrescrevê-lo:
1 -(id) init {
2 self = [super init];
3
4 if (self) {
5 // Se chegou aqui, a inicialização ocorreu com sucesso
6 }
7
8 return self;
9 }
Alinha2invocaométodo initnaclasse-pai(queserápelomenos NSObject),
enquantoalinha4verificaseoprocessoocorreucomsucesso.Casotenhafalhado,
selfiráconterovalor nil.
Épossívelcriarinicializadorescustomizados,exatamentecomofaríamoscomo
qualqueroutrométodo,prestandoaten çãoapenasnanecessidadedechamaralgum
outroinicializadordaclasse-pai(ouumoutronamesmaclasse,queeventualmente
chameodaclasse-pai).Porexemplo,poderíamoscriaruminicializadorparaaclasse
Empresaquejárecebeonomeeaquantidadedefuncionários:
-(id) initWithNome:(NSString *) nome eQuantidadeFuncionarios:(int)
quantidade {
if ((self = [super init])) {
self.nome = nome;
self.quantidadeFuncionarios = quantidade;
}
return self;
}
Paracriarumanovainstância:
Empresa *ep = [[Empresa alloc] initWithNome:@"Jujubas LTDA"
eQuantidadeFuncionarios:17];
47

## Página 60

3.17. Melhoria:esconderotecladoautomaticamente CasadoCódigo
3.17 M elhoria: esconder o teclado automatica-
mente
Umproblemacomonossoaplicativoéque,umavezqueotecladoaparece,elenunca
maissome,nemmesmoapóssalvarmosaempresa. Alémdisso,aimagemdesu-
cessoficaescondida.IssoocorreporqueemiOSnãoexisteexatamenteoconceitode
“foco”noscomponentescomotemosemaplicaçõestradicionaisoumesmonaWeb,
massimalgochamadode responder,quesãoobjetosquepodemlidarcomdiversos
tiposdeeventos.Nocasodecomponentescomoo UITextFieldqueutilizamos
noaplicativodestecapítulo,elesaceitamasmensagensdeentradadetexto(quedis-
paramoteclado),porémoutroscomponentescomobotões(o UIButtonnonosso
caso)ignoramtaiseventos.Então,ocomponentequeinicialmentepegouoteclado
ficacomeleatéqueoutrocomponenteope çaou,então,queexplicitamenterecebam
umamensagemparaliberá-lo.Eéissooquefaremos.
A cadeia de eventos
Tecnicamenteosmotivossãoumpoucomaisdensos,enaexplicaç ão
destase çãooptamosporapresentardeumaformamaiscurtaesimples
paranãosairdofocodocapítulo.Parasabermaisarespeito,procurepor
“UIResponderChain”naInternet.
No método salvar: adicione uma chamada ao método
resignFirstResponder do componente de nome da empresa, conforme o
códigoabaixo:
1 - (IBAction)salvar:(id)sender {
2 // Libera o teclado
3 [self.nomeField resignFirstResponder];
4
5 // Restante do método
6 }
Ocódigodalinhatrêsdizalgocomo“eumeabstenhoderesponderpeloseventos
porenquanto”,fazendocomqueotecladodesapare ça.Sequiserfor çarotecladoa
aparecer,bastausarométodo becomeFirstResponder.
48

## Página 61

CasadoCódigo Capítulo3. MaisObjective-CeXcode
3.18 M elhoria: mostrando a mensagem de sucesso
somente ao salv ar
Atéomomentoamensagem“Dadossalvoscomsucesso”apareceotempotodo,
quandonapráticadeveriaaparecerapósadicionarmosumanovaempresa,eainda
assim apenas por alguns momentos. Para solucionar isso primeiro precisamos
escondê-laaoiniciaroaplicativo,emostrá-lanaaç ãodobotão“Salvar”.
Paraaprimeiraprimeiraparte,atribuaovalor YESàpropriedade hiddenda
variável avisoSucessoLabel,issotudonométodo viewDidLoaddoarquivo
ViewController.m,conformeocódigoabaixo:
- (void)viewDidLoad {
[super viewDidLoad];
self.avisoSucessoLabel.hidden = YES;
}
Emtempo:todocomponentetemapropriedade hidden.Paraasegundaparte
—mostraramensagemporalgunsinstantes—vamosnovamentemodificaromé-
todo salvar:.Adicioneocódigoabaixoaofinaldométodo:
1 - (IBAction)salvar:(id)sender {
2 // Código já existente omitido apenas no livro
3
4 self.avisoSucessoLabel.alpha = 0;
5
6 [UIView animateWithDuration:1 animations:^{
7 self.avisoSucessoLabel.hidden = NO;
8 self.avisoSucessoLabel.alpha = 1;
9 } completion:^(BOOL finalizado) {
10 [UIView animateWithDuration:1 delay:2 options:0 animations:^{
11 self.avisoSucessoLabel.alpha = 0;
12 } completion:^(BOOL finalizado) {
13 self.avisoSucessoLabel.hidden = YES;
14 }];
15 }];
16 }
Sevocêseassustoucomesteúltimopedaçodecódigo,nãosepreocupe:você
nãoéoúnico.Objective-Cpodeserumtantoamedrontadoremcertosmomentos.
Alémdisso,ocódigoficouumpoucomaiorporqueestamosfazendoduasanima-
ções:aprimeiraparamostraroaviso,easegundaparaescondê-lanovamenteapós
49

## Página 62

3.18. Melhoria:mostrandoamensagemdesucessosomenteaosalvar CasadoCódigo
umcertotempo. Maisadiante,nocapítulosobre UIViewsmostraremosafundo
ofuncionamentodosblocosdeanimaç ão,quesãoumrecursomaisavan çadoda
linguagem.
Criação do bloco de animação
Reparequeoblocodeanimaç ãocriadonaúltimalistagemdecódigo
utilizaocaractercircunflexo( ^)paraindicaroiníciodeumpedaçode
código.Emalgunstecladosénecessárioapertarateclaquecontêmeste
símbolo,seguidodabarradeespaço.
Rodeoaplicativo,insiraumaempresa,evocêveráamensagemaparecendode
maneiraanimada,edepoisde2segundostornandoadesaparecerautomaticamente.
Vocêestáficandobomnisso!
50

## Página 63

Capítulo4
Coordenandootrabalhocom
controladores
Diferentesplataformascontêmdiferentesmaneirasderesolverumanecessidadebas-
tantecomum,queéadegerenciardiversastelasefuncionalidades. Alémdisso,é
necessárioqueanavegaçãoetransiç ãoentreelassejamumatarefaintuitivaparao
usuárioelógicaparaodesenvolvedor.EmaplicativosiOSissoéfeitocomousode
controladores(controllers),quesãoclassesque—comoopróprionomesugere—
controlam(ougerenciam)umconjuntodefuncionalidadesdiretamenterelaciona-
das.
Controladores(doinglês“controllers”)sãoclassesnormais,eportantopodem
conterqualquertipodelógicaeregradenegócios,embora—aomenosteorica-
mente—oidealéquesejamusadoscomoumintermediário,comoumfacilitador
detrabalhoentreacamadavisual(as views)ealógicadenegócios.Naprática,mui-
tosdesenvolvedoresacabammisturandoascoisasemumúnicolugar,oquepode
levaradificuldadesparamantereevoluiroaplicativoalongoprazo.

## Página 64

CasadoCódigo
Ocódigo-fontedestecapítuloestádisponívelnaspastas“ViewControllerAni-
mations”e“NavigationControllerDemo”(lembrandoqueoendereçodositecomos
códigosestánaintroduçãodolivro).
Oobjetivodestecapítuloémostrardiferentesmaneirasdeinteragirentre View
Controllers,quesãoasclassesresponsáveisporcoordenarotrabalhoemaplica-
çõesiOS,taiscomoredimensionamentode views,eventosderotaç ãododispositivo
enavegaçãoentreasdiversaspartesdoaplicativo.Afigura 4.1mostraopapeldeum
controladorfrenteadiversasoutraspartesdeumaplicativo.
Figura4.1:Papeldocontrolador.Fonte:Apple
Controladoresporsisónãosãocomponentesvisuais.Pensenelescomoumes-
queleto,queemboranãopossaservisto,évitalparaquetudoseencaixe.Ainterface
comousuárioéfeitaatravésde views,tantoqueeletemasuaprópriapropriedade
chamada view.
52

## Página 65

CasadoCódigo Capítulo4. Coordenandootrabalhocomcontroladores
Controladores e Storyboards
Todooconteúdoapresentadonestecapítuloéfundamentalparao
corretoentendimentodeumdosprincipaispilaresdeaplicaçõesiOS,e
temdiretaligaç ãocomoconteúdodopróximocapítulo, 5.
4.1 P assando de um controlador para outro
Existemdiversasformasdefazeratransiç ãoentrecontroladores,comoapresentá-
losdeforma modal,ouentãoutilizandoumnavegadorespecializado.Veremosessas
duasabordagensnestecapítulo.
Controladoresdotipo Modalfuncionamdamesmamaneiracomo janelasmo-
daisemaplicativosdesktop,queéaquelecomportamentonoqual,quandoumcom-
ponentedesseséapresentado,nadadocomponenteanteriorpodeseracessadoen-
quantoestenãoforfechado.
Crieumnovoprojetodotipo SingleViewApplication (File->New->Pro-
ject -> Single View Application) chamado “ViewControllerAnimations” e
selecioneiPhonecomoDevice. OXcodeirácriarumprojetocomosarquivos
AppDelegate.me .h,eoutraclassechamada ViewController.me .h,além
doarquivo Main.storyboard.
Abraoarquivo Main.storyboard,eadicionequatrocomponentesdotipo
Button,comostextos“Dissolver”,“Virarpágina”,“Subirvertical”e“Girarhorizontal”
—estasserãoasoperaçõesquerealizaremos.
53

## Página 66

4.1. Passandodeumcontroladorparaoutro CasadoCódigo
Figura4.2:Localizaç ãodoRoundRectButton,noXcode
Ateladeveráficarcomoadafigura 4.3.
54

## Página 67

CasadoCódigo Capítulo4. Coordenandootrabalhocomcontroladores
Figura4.3:Telacomosbotõesposicionados
Opróximopassoéconectarasaçõesdestesbotões. Abrao AssistantEditor (
View -> Assistant Editor -> Show Assistant Editor,ou Option +
Command + Enter),econecteumaaç ãoparacadaumdosbotõesnoarquivo“
ViewController.h”,daseguinteforma:
• Texto:“Dissolver”,nomedométodo:“showDissolve”
• Texto:“Virarpágina”,método:“showPageCurl”
• Texto:“Subirvertical”,método:“showVertical”
• Texto:“Girarhorizontal”,método:“showHorizontal”
Ocódigodoarquivo ViewController.hdeveráestarcomomostradoabaixo:
55

## Página 68

4.1. Passandodeumcontroladorparaoutro CasadoCódigo
# import <UIKit / UIKit.h>
@interface ViewController : UIViewController
- (IBAction)showDissolve:(id)sender;
- (IBAction)showPageCurl:(id)sender;
- (IBAction)showVertical:(id)sender;
- (IBAction)showHorizontal:(id)sender;
@end
Cadaumdosmétodosqueiremosimplementarterácomotarefamostrarou-
trocontroladoraousuário,sobrepondooprincipaltemporariamente.Aformaque
veremoséumadasváriaspossíveismaneiras,emaisadianteserámostradocomo
utilizaraclasse UINavigationControllerparafazeranavegaç ãoentreelesde
maneiraorganizadaegerenciável.
Paraqueosbotõespossamabrirumnovocontroladorénecessárioprimeirocriá-
los.Paratanto,acesseomenu File -> New -> File... eselecioneotemplate
Objective-Cclass,ecliquenobotãoNext.Napróximateladevemosinformaronome
daclasseasercriada,equalseráaclassepai.Chame-ade“OpcoesController”,eem
“Subclassof”selecioneaopção“UIViewController”. Marquetambémocheckbox
“WithXIBforuserinterface”,conformemostradonafigura4.4.
56

## Página 69

CasadoCódigo Capítulo4. Coordenandootrabalhocomcontroladores
Figura4.4:Criandoocontroladorparaateladeop ções
QuandooXcodeperguntarondeoarquivodeverásersalvo,selecioneapasta
raizdoprojeto,nomesmolugarondeestãoosoutrosarquivos. Vocêdeverátero
arquivo“OpcoesController”nasextensões“.h”,“.m”e“.xib”.
Reparembemquetodososarquivostêmomesmonome,mudandoaextensão.
Emboranãosejaobrigatórionomeardestejeito,estaéamaneiraquetodososde-
senvolvedorescostumamutilizar.Alémdisso,quandotrabalhamoscominterfaces
gráficasutilizandoarquivos .xib,respeitaraconven çãodenomessimplificaocó-
digo,poisocomportamentopadrãodoiOSéprocuraro .xibquetenhaomesmo
nomedaclasse.
Abraoarquivo“OpcoesController.xib”eadicioneumcomponentedotipo
“Label”nomeiodatela,comotexto“Opções”,apenasparatermosumaindicação
visualquandoeleforexibido.
Agoraváaoarquivo ViewController.m,ondevocêiráencontrarocorpo
dosmétodosqueforamconectadosanteriormente(pelo Main.storyboard)ao
arquivo ViewController.h. Cabeanósimplementarcadaumadasaçõesdos
botões.Oprimeirométodoéo showVertical,querepresentaaanimaç ãopadrão
57

## Página 70

4.1. Passandodeumcontroladorparaoutro CasadoCódigo
doiOSparaotipodeoperaç ãoqueiremosrealizar. Oquedeveserfeitoécriar
umainstânciado OpcoesController,especificarotipodaanimaç ãoeinvocaro
método presentModalViewController.
Vamosprimeiroveraimplementaç ãocompletadométodo,conformealistagem
abaixo:
1 - (IBAction)showVertical:(id)sender {
2 OpcoesController *c = [[OpcoesController alloc] init];
3 c.modalTransitionStyle = UIModalTransitionStyleCoverVertical;
4
5 [self presentViewController:c animated:YES completion:nil];
6 }
Obs: não esque ça de adicionar a instruç ão #import
"OpcoesController.h"noiníciodoarquivo.
Na linha 3 é definido o tipo de animação desejado, que no caso é
UIModalTransitionStyleCoverVertical. Estaéaanima çãopadrão,epo-
demosomitirissonaprática. Porém,comonestecasodesejamostestartodasas
animaçõespossíveis,éinteressanteatribuirmosexplicitamenteotipodesejado.
Jáalinha5éaresponsávelpormostrardefatoonomecontrolleraousuário,
atravésdométodo presentViewController:animated:completion.
Rodeoaplicativo( Command+R)ecliquenobotão“Subirvertical”.Vocêdeverá
vero OpcoesControllercobrirtodaatela,vindodebaixoparacima.Estafoia
primeiraanimação.Opróximométodoaimplementaréo showHorizontal,que
mostraráutilizandoumefeitodegiraratelahorizontalmente. Aimplementaç ão
completaestáabaixo:
- (IBAction)showHorizontal:(id)sender {
OpcoesController *c = [[OpcoesController alloc] init];
c.modalTransitionStyle = UIModalTransitionStyleFlipHorizontal;
[self presentViewController:c animated:YES completion:nil];
}
Rodenovamenteoaplicativoecliquenobotão“Girarhorizontal”,evejaadife-
rençanoefeitodaanimaç ão.Bacana,não?
Repare bem na implementação dos métodos showVertical e
showHorizontal, e veja que a maior parte do código deles é igual, mu-
dandoapenasotipodeanimaç ãodesejada. Comotemosmaisduasanimações
58

## Página 71

CasadoCódigo Capítulo4. Coordenandootrabalhocomcontroladores
paraimplementar,oidealseriaisolarocódigoemcomumatodososmétodose
centralizá-loemumúnicolugar,evitandoassimaduplicaç ãodetrabalho.Embora
estejamosfazendoapenasumaplicativodetestes,quantomaiscedoadotaraprática
dereutilizarcódigo,maisrapidamenteelasetornaránatural,econsequentementeo
seusistemaficarámaisfácildemanter.
Portanto,antesdeimplementarosdemaismétodos,vamosprimeirocriarum
métodoquefarátodootrabalhorepetitivo,recebendocomoparâmetrootipode
animaçãoaserutilizada.Vejaaimplementaç ãocompletaabaixo:
-(void) mostraControllerComAnimacao:(UIModalTransitionStyle) estilo {
OpcoesController *c = [[OpcoesController alloc] init];
c.modalTransitionStyle = estilo;
[self presentViewController:c animated:YES completion:nil];
}
Ométodo mostraControllerComAnimacao:épraticamenteigualaocó-
digoquefizemosanteriormente,comadiferen çadequeelerecebeumargumento
especificandootipodeanimaç ão.Coloqueaimplementaç ãodeleemqualquerlugar
daclasse(porexemplo,logoabaixode @implementation),eimplementeoresto
dosmétodosdaseguintemaneira:
- (IBAction)showDissolve:(id)sender {
[self
mostraControllerComAnimacao:UIModalTransitionStyleCrossDissolve];
}
- (IBAction)showPageCurl:(id)sender {
[self
mostraControllerComAnimacao:UIModalTransitionStylePartialCurl];
}
- (IBAction)showVertical:(id)sender {
[self
ostraControllerComAnimacao:UIModalTransitionStyleCoverVertical];
}
- (IBAction)showHorizontal:(id)sender {
[self
mostraControllerComAnimacao:UIModalTransitionStyleFlipHorizontal];
}
59

## Página 72

4.2. Fecharumcontroladormodal CasadoCódigo
Bemmaissimpleseprático,esemduplicarcódigo.Rodenovamenteoaplicativo
etestecadaumdosbotões.
4.2 Fechar um controlador modal
Umacoisaquevocêdeveternotadoéque,depoisdeabirumcontroladorusando
presentViewController, nãohavianenhumamaneiradefechá-loouvoltar
paraatelaanterior.Contudo,issoébastantesimplesdeseresolveratravésdomé-
todo dismissViewControllerAnimated:completion,quedeveseradicio-
nadocomoaç ãodeumbotãonaclasse OpcoesController. Sigaosseguintes
passos:
Abraoarquivo OpcoesController.xibeadicioneumbotãocomotexto
“Fechar”,econecteumaactionchamada“close”noarquivoOpcoesController.h
(lembre-se de usar oAssistant Editorpara ver o arquivo.xib e .h lado a
lado). Emseguida,abraoarquivo OpcoesController.mechameométodo
dismissViewControllerAnimated:completion,conformeabaixo:
- (IBAction)close:(id)sender {
[self dismissViewControllerAnimated:YES completion:nil];
}
Rodenovamenteoaplicativo“clique”nobotão“Fechar”,paraqueocontrolador
sejafechado.
4.3 N avegar por diferentes telas com o UINavigati-
onC ontroller
Umadasformasdenavegaç ãomaiscomumemaplicativosiOSéaquelaemque,feita
umadeterminadaação,umanovateladeslizadadireitaparaaesquerdaporcimada
anterior. Depois,atravésdeumtoqueemumbotãonocantosuperioresquerdo
(geralmenteumbotãoescrito“Back”ou“Voltar”),volta-separaatelaanterior.Ou
seja,éumanavegaçãohierárquica.
Estetipodenavegaç ãochama-se“ControladordeNavegação”,ounotermotéc-
nico, UINavigationController.Nosexemplosiremosnosreferiraestecom-
ponentepelonome navigationcontroller,poiséumtermobastanteconhecidoem
desenvolvimentoiOS,eacostumar-secomelefacilitaráabuscaporinformaçõesna
Internet,posteriormente.Afigura 4.5mostracomoelefunciona.Eladevepermitir
60

## Página 73

CasadoCódigo Capítulo4. Coordenandootrabalhocomcontroladores
quetroquemosdeumatelaparaoutra,deumafuncionalidadeparaoutra,atravésde
umainterfacesimples.
Figura4.5:FuncionamentodeumUINavigationController
Navigationcontrollerssãope çasmuitoimportantesemaplicaçõesiOS,poisper-
mitematransiç ãodeumcontrollerparaoutrosemquehajaperdadeestado. Em
outraspalavras,oaplicativoliteralmentevaiempilhandooscontroladores,semtirá-
losdamemória,permitindoqueanavegaç ãoreversasejafeitademaneiranatural.
Gerenciamento de memória de controladores
Emcondiçõesnormaisdefuncionamento,oscontroladoresqueestão
nahierarquiadeumNavigationControllersãosempremantidosemme-
mória.Porém,nãodevemostrabalharcomapremissadequeissoserá
sempreverdade,poisnocasodefaltadememória,oiOSpode“descar-
regar”algunsdeles,recriando-osquandonecessário.
Paraentendermelhorofuncionamentodo UINavigationController,va-
moscriarumaplicativodeumcatálogodeempresas,noqualépossíveladicionar
novosregistroserealizarconfigurações.
Crieumnovoaplicativodotipo“SingleViewApplication”,nosmesmosmol-
des dos exemplos anteriores, e chame-o de “NavigationControllerDemo”. Você
deverá ter um projeto padrão, com oAppDelegate e uma classe chamada
61

## Página 74

4.3. NavegarpordiferentestelascomoUINavigationController CasadoCódigo
ViewController.Reparequeestenome,“ViewController”,queoXcodecriajunto
comoprojeto,éapenasparanossaconveniência,porémvocênãoprecisaficaramar-
radoaele.
Paracome çar,vamosmudaronomedaclasse“ViewController”paraalgose-
manticamentemelhor.Umadasmaneirasdefazerissoérenomearmanualmenteos
arquivos ViewController.me .h,porémissodámuitotrabalhoecorremoso
riscodeesqueceralgumacoisa.Umamaneiramaisinteligenteéutilizarafunciona-
lidadede refatoraçãodoXcode,quefazparanóstodotrabalhopesado.
Abraoarquivo ViewController.me,nalinhadedefiniç ãodaclasse(onde
tem @implementation ViewController)cliquecomobotãodireitoeseleci-
oneaop ção Refactor -> Rename...,conformeafigura 4.6.
Nacaixadediálogoqueabrir,informeovalor“RootController ”nocampode
texto,edeixemarcadaaop ção“Renamerelatedfiles”,paraqueoXcoderenomeie
todososarquivosquetenhamrelaç ãoaooriginal ViewController.
Aoclicarnobotão“Preview”,oXcodeirámostrarumresumodasoperações
queserãorealizadas.Cliquenobotão“Save”,ecasooXcodemostreumamensagem
perguntandosedevefazerbackupdoconteúdo,cliqueem“Enable”.
62

## Página 75

CasadoCódigo Capítulo4. Coordenandootrabalhocomcontroladores
Ao término da operação, repare que tanto os arquivos em disco como
as próprias definições da classe ViewController foram renomeadas para
RootController.
4.4 P reparar a tela principal
Agoraprecisamoscolocarbotõesno RootControllerparachamarosoutroscon-
troladores,umparaafictíciateladeadicionarempresasaocatálogo,eoutroparaa
—adivinhem—tambémfictíciateladeconfigurações. Oobjetivoprincipaldesta
seçãoédemonstrarcomonavegardeumlugarparaooutro,enãonaimplementaç ão
realdeumcatálogopropriamentedito.
Abraoarquivo Main.storyboardecoloque2botões,oprimeirocomotexto
“Adicionar”,eosegundocomotexto“Configurações”,conformemostraafigura4.6.
63

## Página 76

4.4. Prepararatelaprincipal CasadoCódigo
Figura4.6:Desenhodatelaprincipaldoaplicativo
64

## Página 77

CasadoCódigo Capítulo4. Coordenandootrabalhocomcontroladores
Por que editar o arquivo Main.storyboard?
O motivo pelo qual, neste ponto, é necessário editar o arquivo
Main.storyboard,sedeveaofatoqueeleéaformapadrãopelaqual
oXcodecriaprojetosdotipo“Single View Application”(alémdeal-
gunsoutros),sendoopontodepartidadaapp. Estaétambémuma
formadaAppleestimularousodeStoryboardsemdetrimentodoan-
tigoformatoquesebaseadaapenasemarquivos“ .xib”. Somadoa
isso,vocêdeveselembrarquetodonovoprojetotambéminiciacom
aclasse“ViewController”,queanteriormenterenomeamospara“
RootController”,eestamesmaclassetambémestáconfiguradacomo
sendoaprimeiraqueoaplicativodeveráutilizar,quandooaplicativofor
iniciado.
Nocapítulo5veremosmaisafundoesteassunto.
4.5 C onectar as ações dos botões
Damesmaformacomojáfizemosdiversasoutrasvezesduranteolivro,paraque
osbotõestenhamutilidadeénecessárioconectarasaçõesdelesaocódigo,utili-
zandoajáconhecidaabordagem“Selecionarcomponente->ArrastarcomCTRL
paraoarquivo .h->Connectiondotipo Action”.Maisfácilquedevorarobolode
chocolatedavovó.Chameaaç ãodobotão“Adicionar”de“abrirAdicionar”,e
parasegundobotãonomeieaaç ãode“abrirConfiguracoes”. Oseuarquivo
RootController.hdeveráficarassim:
# import <UIKit / UIKit.h>
@interface RootController : UIViewController
- (IBAction)abrirAdicionar:(id)sender;
- (IBAction)abrirConfiguracoes:(id)sender;
@end
4.6 C riar a tela de Adicionar Empresa
Adicioneumanovaclasse( Command + N)chamada AdicionarControllerda
mesmaformacomocriamoso RootController,lembrandodeselecionaraop ção
65

## Página 78

4.7. Navegardeumcontroladorparaoutro CasadoCódigo
paracriaroarquivo .xib,eadicioneapenasum labelcomotexto“Telaadicionar
empresa”noarquivoAdicionarController.xib. Lembre-sequeoobjetivoé
focarnanavegaç ãoentreoscontroladores,enãonafuncionalidadedeadicionar
empresaspropriamentedita.
4.7 N avegar de um controlador para outro
A classe UIViewController contém uma propriedade cha-
mada navigationController que representa a instância do
UINavigationController utilizada pelo aplicativo, sendo que os princi-
paismétodossãodois:
•pushViewController:animated,paranavegarparaumoutrocontrola-
dor
•popViewControllerAnimated,paravoltarumnívelnahierarquia.
Parairdo RootControllerparaateladeadicionarempresa,implementeo
método abrirAdicionarnoarquivo“RootController.m”daseguinteforma
(obs:lembre-sedeimportaroarquivo AdicionarController.h):
- (IBAction)abrirAdicionar:(id)sender {
AdicionarController *c = [[AdicionarController alloc] init];
[self.navigationController pushViewController:c animated:YES];
}
Rodeoaplicativo( Command+R)einterajacomobotão“Adicionar”. Acon-
teceu alguma coisa? Muito provavelmente não, pois apesar da propriedade
navigationControllerfazerpartedaAPIdaclasse UIViewController,ova-
lordelanãoécriadoautomaticamentepeloiOS.Portanto,énossaresponsabilidade
disponibilizarum UINavigationControllereinstruiroaplicativoautilizá-lo.
4.8 A ssociar um UINavigationC ontroller ao pro-
jeto
Conceitualmenteum UINavigationControllernãodeveserestendido,mas
simserutilizadodiretamente.Imagineonavigationcontrollercomosendoum ge-
renciador,querecebeumareferênciaparaocontroladorinicial,eapartirdaipermite
anavegaçãoparaosoutrosatravésdométodo pushViewController:animated.
66

## Página 79

CasadoCódigo Capítulo4. Coordenandootrabalhocomcontroladores
Apropriedade navigationControllerdaclasse UIViewControlleré
vaziaemcontrollersquenãofaç ampartedahierarquiadeumnavigationcontrol-
ler(oquefazbastantesentido). Porém,apartirdomomentoemquecriamosum
UINavigationController,oiOSatribuiautomaticamenteumvalorválidopara
apropriedadedocontroladorprincipaledetodososoutrosquefizeremparteda
navegação. Issoébastanteprático,poisnãoprecisamosnospreocuparemmanter
umareferênciaglobalaonavigationcontrollereatribuí-lomanualmenteaosdemais.
Para adicionar um navigation controller ao projeto, abra o arquivo
Main.storyboard e selecione a barra preta na parte inferior, conforme
mostra a imagem4.7, e em seguida acesse o menu “Editor -> Embed In
-> Navigation Controller”.Oresultadoficarácomoodaimagem 4.8.
Figura4.7:Cliquenabarraparaselecionarocontrolador
67

## Página 80

4.9. Criarosdemaiscontroladores CasadoCódigo
Figura4.8:NavigationControllerassociadoaoprojeto
Rodenovamenteoaplicativoeinterajacomobotão“Adicionar”,evejaquedesta
vezatelado AdicionarControlleréexibidacorretamente. Umaoutracoisa
novaéqueoaplicativoapresentaumabarrasuperiordenavegaç ão—chamadade
“NavigationBar”—,ondeumbotãocomotítulo“Back”aparecenocantosupe-
rioresquerdoquandonavegamosdeumlugarparaooutro.Tecnicamentefunciona
destamaneira:aoexecutarmos pushViewController:animated,oiOSusaráo
títulodocontrolador anterior(representadopelapropriedade title)comotexto
dobotãoe,casonãohajanenhumtítulodefinido,otexto“Back”éutilizado.
4.9 C riar os demais controladores
Onossoaplicativotambémprecisadeumahipotéticateladeconfigurações—aliás,
duas. Aprimeiradelascontémalgumascoisasgerais,comoseocatálogodeveser
utilizadoem“Modoseguro”eseosdadosdevemsersalvosautomaticamenteou
68

## Página 81

CasadoCódigo Capítulo4. Coordenandootrabalhocomcontroladores
não.Alémdisso,precisamosdosdadosdeacessodousuário.Paraoprimeirocaso
crieumnovocontroladorchamado ConfguracoesControllercomofeitoante-
riormente,eadicionealgunscomponentesparaparecerqueeletemutilidade,como
exemplificadonafigura 4.9.
Figura4.9:Exemplodatelaprincipaldeconfigurações
Implemente o método A B R I RCO N F I G U R A C O E S:
Não esque ça de implementar o corpo do método
abrirConfiguracoes:noarquivo RootController.m,seguindo
amesmalógicadoquefoifeitoparaométodo abrirAdicionar:,
porémdestavezinstanciandoo ConfiguracoesController.
Alémdisso,estateladeveráchamarumaoutratela,portantoconecteaaç ãodo
botão“Dadosdeacesso”aométodoabreDadosAcesso:,conformealistagem
abaixo:
69

## Página 82

4.9. Criarosdemaiscontroladores CasadoCódigo
// ConfiguracoesController.h
# import <UIKit / UIKit.h>
@interface ConfiguracoesController : UIViewController
- (IBAction)abreDadosAcesso:(id)sender;
@end
Paraatelade“Dadosdeacesso”,crieumnovocontroladorchamado“DadosA-
cessoController”eadicionealgunscampos,conformeafigura4.10.Paraestatelanão
hánecessidadedecódigoadicionalporenquanto.
Figura4.10:Exemplodasconfiguraçõesdeacesso
Agora,noarquivo ConfiguracoesController.m,implementeocorpodo
método abreDadosAcesso:paraqueo DadosAcssoControllersejaaberto
quandosolicitado,conformedemonstradoabaixo:
70

## Página 83

CasadoCódigo Capítulo4. Coordenandootrabalhocomcontroladores
- (IBAction)abreDadosAcesso:(id)sender {
DadosAcessoController *c = [[DadosAcessoController alloc] init];
[self.navigationController pushViewController:c animated:YES];
}
Executeoaplicativo( Command + R)enavegueentreoscontroladores,eveja
comoo UINavigationControllercuidadapartedetransiç ãoentreeles.Neste
pontodeveráserpossívelnavegarconformedemonstradonafigura 4.11.
Figura4.11:Estruturadanavegaç ão
4.10 E sconder a barra superior de navegação
Certas vezes não há a necessidade de deixar a barra de navegação superior
(a “Navigation Bar”) doUINavigationController visível o tempo todo,
caso ela não agregue funcionalidade, e o ideal seria escondê-la e mostrar so-
mente quando necessário. Para obter este resultado basta executar o método
setNavigationBarHidden:animateddo UINavigationController,lem-
brandoqueeleérepresentadopelapropriedade navigationController.Adici-
71

## Página 84

4.10. Esconderabarrasuperiordenavegaç ão CasadoCódigo
onealinhadecódigoabaixonométodo viewWillAppear:animateddaclasse
RootViewController,erodenovamenteoaplicativo.
// RootController.m
-(void) viewWillAppear:(BOOL)animated {
[self.navigationController setNavigationBarHidden:YES animated:YES];
}
Contudo,quandonavegamosnahierarquiaparaoutrocontrolador,abarrade
navegaçãocontinuaescondida,impossibilitandodenavegarmosparaonívelan-
terior. Parasolucionaresteproblemabastafazeroprocessoinversonasclasses
ConfguracoesControllere AdicionarController,conformedemonstrado
abaixo:
// Nos controladores Configurações e Adicionar
-(void) viewWillAppear:(BOOL)animated {
[self.navigationController setNavigationBarHidden:NO animated:YES];
}
Rodenovamenteoaplicativo(menu Product->Run)evejaadiferen çanofun-
cionamento.
72

## Página 85

Capítulo5
Storyboards
Historicamente,amaneiradeconstruiraplicaçõesiOSconsistiaemcriarumasérie
decontroladores,cadaumdemaneiraindependentedooutro,efrequentemente
comarquivos .xibparaacriaç ãodolayout. Comovimosnocapítulo 4,ainda
épossívelconstruiraplicaçõesdestaforma,porémagoraexisteaop çãodeutilizar
storyboardsnolugardecontroladoresindependentes.
Agrandevantagemdestoryboardséqueelesnospermitemdefinirvisualmente
comoasinteraçõesentreasmuitastelasdosaplicativosirãoocorrer,tudoissoemum
únicoarquivo,oquenosdáumavisãoampladetodasasrotaspossíveis.Aplicativos
costumamterumúnicostoryboard,emboratecnicamentesejapossívelhavermais
deles.
Tenhaemmentequestoryboardssãoumamaneiradecriarcontroladoresedefi-
nircomoelesinteragementresi-porexemplo,comoirdeumparaooutro-,porém
nadamuitoalémdisso.Tudooquejáfoimostradonolivro,etudomaisoqueainda
serádemonstrado,podetrabalhar emconjuntocomstoryboards.

## Página 86

5.1. Projetoeconceitosgerais CasadoCódigo
Os termos de storyboards
QuandofalamosdestoryboardsemiOS,frequentementeveremosos
seguintesabaixo.Comocuriosidade,esteéumtermoqueaAppleem-
prestoudeoutrasartes,comofilmeseteatro.
•Scene:termoeminglêspara“Cena”,daquelamesmadeteatroou
TV,queécadatelaemsi.Nolivroutilizaremosotermoeminglês,
poiséalgobemprópriodestoryboardselheajudaráemfuturas
pesquisassobreoassunto.NapráticaScenesecontroladores(vide
abaixo)estãodiretamenteligados,nãosendopossívelterumsem
ooutro.
•View Controller:jávimosbastantesobrecontroladores,eelesfor-
mamumapartefundamentaldestoryboards,trabalhandodireta-
menteemconjuntocomscenes.Tudooquevocêjáaprendeusobre
controladoresnolivroseaplicanocasodestoryboards.
•Segue:éoconceitoquedefiniatransiç ãodeumasceneparaoutra.
Otermoeminglêseportuguêssãoiguais.
5.1 P rojeto e conceitos gerais
Crie um novo projeto do tipo “Single View Application” com as configurações
padrão, chamado “DemonstracaoStoryboards”, e em seguida abra o arquivo “
Main.storyboard”.Aimagem5.1mostraaestruturainicialdeumastoryboard.
74

## Página 87

CasadoCódigo Capítulo5. Storyboards
Figura5.1:Aestruturainicialdeumastoryboard
Asetaindicadapeloitem1informaqueestecontroladoréopontodepartida
(controladorinicial)dastoryboard,oitem2éaScene(queéapor çãodaview),
enquantoqueoitem3éocontroladorpropriamentedito.Portanto,sevocêquiser
definirpropriedadesdaScene(oudaview,utilizandoumoutrotermo)cliqueem
qualqueráreadaregiãobranca,indicadapelonúmero2.Poroutrolado,casoqueira
definirpropriedadesdocontrolador,comotítulo,op çõesdetransiç ãoparaoutras
Scenes,métricasdesimulaç ãodeinterfaceeafins,cliquenabarrapretalocalizada
naparteinferiordaScene,indicadapelonúmero3naimagem-naprática,ocon-
troladoréoelementoamarelolocalizadonaextremidadeesquerdadabarrapreta.
Nestecapítuloserámostradoofuncionamentodestoryboardssemfocaremde-
talhesdeumprogramaespecífico-maisadiantenolivroconstruíremosumaplica-
tivomaiscompletoquetambémfaráusomaisextensivodestoryboards,ajudando
assimafirmarosconceitos.Porenquanto,oimportanteéfocarnamaneiracomoele
funciona,oqueébastantesimples.Oaplicativoconsisteemumaseriedetelasfic-
tícias,comalgunsníveisdenavegaç ãoauxiliadosporumpornavigationcontroller,
75

## Página 88

5.1. Projetoeconceitosgerais CasadoCódigo
comosquaisserãodemonstradosasformasdeconexãoenavegaç ãodeumSegue
paraoutro,comoinvocarmanualmenteumSegue,ecomoretornarparaoinícioda
appsemterquevoltarmanualmentetelaportela.
Aimagem 5.2mostraoestadodastoryboarddoprojetodestacapítuloquando
estiverfinalizada.Atelafoidiminuidadetamanhoparapodercabertudoemuma
únicaimagem.Notequeépossívelvisualizartodaaestruturadenavegaç ãodoapli-
cativo,sabendoquandoéatelainicialeospossíveiscaminhosdeumatelaparaoutra.
Figura5.2:Resultadofinaldastoryboarddestecapítulo
Aoabriroarquivo“Main.storyboard”vocêencontraráumatelacomoada
imagem5.1,ondejáháumcontrolador,oqualseráatela(Scene)inicialdoapli-
cativo. Insiranestecontrolador3botões,chamados“Listarcompromissos”,“Inserir
novocompromisso”e“Sobreesteaplicativo”,respectivamente.Aimagem5.3mostra
oresultado.
76

## Página 89

CasadoCódigo Capítulo5. Storyboards
Figura5.3:Telainicialdoaplicativo
Nível de zoom e organizar controladores na storyboard
Umacoisaruimdoeditordestoryboardséque,quantomaiscontroladoresvocê
adicionar,maisdifícilficavisualizá-loseorganizá-losnoeditor,oqueéaindamais
sofrívelcasovocêtenhaummonitorpequeno(ou,pior,apenasateladonotebook,
comomuitaspessoas).OtimedaAppleaindaprecisatrabalharbastanteemdiversas
questõesdeusabilidade.
Utilizeoscontrolesdisponíveisnocantoinferiordireitodatelaparaalteraro
níveldezoomdoeditor,conformemostraaimagem[ref-lablsb2.png]. Obotão
domeio,representadopelosímbolodeigualdade(“=”)retornaozooma100%.Já
paraarrastarocontroladorparaoutrapartedatela(comoquandoquisermudá-lo
deposição,porexemplo)cliqueearrasteabarrapreta.
77

## Página 90

5.1. Projetoeconceitosgerais CasadoCódigo
Figura5.4:Controlesdezoom
Construir a Segue ‘Sobre’
Comovocêpodededuzirpelaimagem 5.3,existemtrêsSeguesparaasquais
épossívelnavegarapartirdaSegueinicial. Vamoscome çarpela“Sobreesteapli-
cativo”. Como“Main.storyboard”aberto,abraaObjectLibrary( View ->
Utilities -> Show Object Library)earrasteparaastoryboardumitemdo
tipo“ViewController”,eemseguidaadicionenestecontroladorumUILabelcom
otexto“DemonstraçãoApp1.0”.Aimagem5.5mostraoresultadoparcial.
78

## Página 91

CasadoCódigo Capítulo5. Storyboards
Figura5.5:Resultadoparcialcomatela‘Sobre’
Nestepontotemosdoiscontroladores,porémsemqualquerligaç ãoentreeles.
Oqueprecisaserfeitoentãoéinformarque,apartirdotoquenobotão“Sobreeste
aplicativo”,ocontrolador“Sobre”sejaadicionado.Anteriormenteastoryboardseste
processoerafeitomanualmente,atravésdacriaç ãodeuma actionparaobotão,e
amanualinstanciaç ãodocontrolador.Jácomstoryboardsahistóriaficabemmais
fácil,podendoserfeitotudovisualmentepeloeditor,semqualquernecessidadede
código.
Cliquenobotão“Sobreesteaplicativo”,segureCTRLecliqueearrasteemdire ção
aocontrolador“Sobre”,detalformaquesuaáreafiqueazulada,eentãosolteoclique.
Issofarácomqueumaconexão-oumelhor,aSegue-sejafeitadobotãoparaeste
controlador,conformemostraaimagem 5.6.Natelapopupqueaparecer,selecione
oitem“Push”.
79

## Página 92

5.1. Projetoeconceitosgerais CasadoCódigo
Figura5.6:CriarSeguedobotãoparaocontrolador
Rodeoaplicativoecliquenobotão.Oqueaconteceu?Provavelmenteoseguinte
erro:
Terminating app due to uncaught exception 'NSGenericException', reason:
'Push segues can only be used when the source controller is managed by
an instance of UINavigationController. '
EstamensagemdeerroestádizendoqueeventosSeguedotipo“Push”,quefoi
oqueselecionamosnopopupnahoradefazeraconexão,precisamqueexistaum
UINavigationControllerassociado,casocontrárionãoépossívelnavegaren-
treasScenes.Pararesolverissoébemsimples:selecioneocontroladorquetemos
botões,jáqueeleéaprimeirateladoaplicativo,eentãováaomenu“ Editor ->
Embed In -> Navigation Controller”,queoXcodeiráadicionareconfigu-
rareleparanós.Oresultadodeveráficarcomoodaimagem 5.7
80

## Página 93

CasadoCódigo Capítulo5. Storyboards
Figura5.7:Storyboardapósaadiç ãodonavigationcontroller
Comopodever,oprimeirocontroladordastoryboard(representadopelaseta
maisaesquerda)passouaseronavigationcontroller,quenapráticaéumcontrola-
dorespecialquegerenciaanavegaç ãoentreoutroscontroladores.Sevocêselecioná-
lo(lembre-sequeparaselecionarocontroladorénecessárioclicarnabarrapreta)
eabriroAttributesInspector(“ View -> Utilities -> Show Attributes
Inspector”)veráqueeleestámarcadocomosendoaSceneinicial,conformemos-
traaimagem 5.8.
81

## Página 94

5.1. Projetoeconceitosgerais CasadoCódigo
Figura5.8:Navigationcontrollerdefinidocomosendooprimeiro
Rodeoaplicativonovamenteecliquenobotão,evejaqueagoraelefunciona
corretamente.
Ver a conexão e tipo de transi ção
Sevocêclicarnasetaentredoiscontroladores,poderávisualizarobotãocomo
qualaaç ãoestáassociada,conformemostraaimagem 5.9,ondeobotãoéidentifi-
cadocomumasele çãoazul.Dequebra,noAttributesInspectorépossívelmodificar
otipodetransiç ão,quenonossocasofoidefinidacomo“Push”.
82

## Página 95

CasadoCódigo Capítulo5. Storyboards
Figura5.9:Verificarcomqualbotãoatransiç ãodaSegueestáassociado
Título dos controladores
Comoagoratemosumnavigationcontroller,eleporpadrãoadicionaumabarra
superiornoscontroladores,ondeépossíveldefinirumtítuloparaatela.Alémdisso,
nocantosuperioresquerdoeletambémcolocaautomaticamenteumbotãoparavol-
tarparaatelaanterior,comovocêjádeveternotado.Seguindoaimagem 5.10,dêum
duplocliquenaregiãodetítuloindicadopelaseta,eescrevaumtextocurtoeclaro
paraidentificarocontroladoremquestão-porexemplo,“Início”e“Sobre”. Veja
aindaque,nase ção“NavigationItem”doAttributesInsepector,existemtrêscampos
detexto,sendoqueosmaisinteressantessão“Title”,paraotextoqueiráaparecerna
barra(éomesmotextodefinidpeloduploclique)e“BackButton”,queéotextoque
iráserutilizadonobotãopararetornaratelaanterior-casonenhumvalorsejainfor-
mado,onavigationcontrolleriráautomaticamenteutilizarotítulodatelaanterior.
Obs:otextodobotão“BackButton”deveserdefinidonocontrolador“anterior”,ou
seja,aqueleparaqualanavegaç ãoiráretornar.Façaalgunstestesparaseacostumar
comofuncionamento.
83

## Página 96

5.2. Adicionarosdemaiscontroladores CasadoCódigo
Figura5.10:Propriedadesdenavegaç ão
5.2 A dicionar os demais controladores
Agoraquesabemosofuncionamentodestoryboards,vamosadicionarosdemais
controladores.Oprocessoéigualparatodos,mudandoapenasotítulodecadacon-
trolador.Façaassim:
1) Adicione na storyboard um componente do tipo “View Controller”
localizado na Object Library (View -> Utilities -> Show Object
Library)
2) CrieaSeguedobotão“ListarCompromissos”paraestenovocontrolador(clique
nobotãoedepois CTRL + clique e arraste),escolhendo“Push”como
ação. Obs: issonãopodeserfeitoseozoomestiverhabilitado,oXcodenão
permite
3) Coloqueumtítulonabarrasuperiordestecontrolador(porexemplo,“Listar”)
4) Repitaospassos1a3paraatela“Inserirnovocompromisso”,comotítulo“Inserir”
Nestemomentooseuresultadodeveráestarcomoodaimagem 5.11. Rodeo
aplicativoenavegueparacertificar-sequetudofunciona.
84

## Página 97

CasadoCódigo Capítulo5. Storyboards
Figura5.11:Propriedadesdenavegaç ão
A tela de Listar e seus controladores, via código
Atela“Listar”permiteduasaçõesadicionais:editareverosdetalhesdeumde-
terminadoregistro.Abraocontroladorcomotítulo“Listar”eadicionedoisnovos
botões,umcomotexto“Editar”eoutrocomotexto“VerDetalhes”,porém desta
vez não crie as Segues ainda,poisiremosfazerdeumamaneiraalternativa,viacó-
digo. Aprenderafazerviacódigoéútilquandofornecessárionavegarparaoutra
Seguedeumamaneiranãotradicional,comoainteraç ãocomacéluladeumaTable
View,ouumbotãocomaçõescondicionais(comoumbotão“Login”quedepoisvira
85

## Página 98

5.2. Adicionarosdemaiscontroladores CasadoCódigo
“Logout”).
Existemduascoisasqueprecisamserfeitas:aprimeiraéqueaSeguedeveser
criadasemestarassociadacomumbotãoespecífico,massim“decontroladorpara
controlador”. IssoéfeitocriandoaSegueatravésdoitem“ViewController”na
barrapresta,utilizandoamesmatécnicade“ CTRL+clique e arraste”,con-
formemostraaimagem 5.12.
Figura5.12:CriandoaSeguesemassociarelaaumbotão
Repitaoprocessomaisumavez,agoraparaooutrocontrolador(lembre-se:um
paraeditar,eoutroparaverdetalhes).Oresultadodestapartedeveráestarcomoa
imagem5.13.
86

## Página 99

CasadoCódigo Capítulo5. Storyboards
Figura5.13:SeguescriadasdateladeListarparaEditareDetalhes,semassociaç ão
comalgumbotão
87

## Página 100

5.2. Adicionarosdemaiscontroladores CasadoCódigo
ParaquesejapossívelnavegarentreSeguesviacódigoénecessárioadicionar
identificadoresúnicosaelas. Paraisso,cliquenasetaqueuneasSeguesepreen-
chaocampo“Identifier”noAttributesInspector,conformemostraaimagem 5.14.
Lembre-sedeutilizarnomesúnicosparacadasegue. Comosugestão,utilizeuma
combinaçãodonomedaSeguedeorigemededestino.Nocasodesteexemplo,“Lis-
tar->Editar”deveserchamadade“listarParaEditarSegue”e“Listar->De-
talhes”de“listarParaDetalhesSegue”.
Figura5.14:AdicionaridentificaraumaSegue
Atéagoratodootrabalhoquerealizamosfoiunicamentenastoryboard,sem
precisarcriarumaúnicaclasseoulinhadecódigo.Contudo,sabemosquenavida
realasregrasdenegóciosãoescritasemObjective-C,eparaissoénecessárioter
umaclassecustomizadaassociadaaocontroller,comojávimosdiversasvezesno
livro.ComoagoraqueremosirdaSegue“Listar”paraoutrasduas,vamoscriaruma
classeespecialparaela.
Váaomenu“File -> New -> File...”,selecione“Objective-CClass”ecli-
queem“Next”.Nocampo“Class”insiraovalor“ListarViewController”,enocampo
“Subclassof”certifique-sequeaopção“UIViewController”estejaseleciona,pois
queremoscriarumcontroladorcustomizado.Asop ções“TargetedforiPad”e“With
XIBforUserInterface”devemestardesmarcadas.
Agoravolteaostoryboard,selecioneaSegue“Listar”,abrao“IdentityInspector”
(“View -> Utilities -> Show Identity Inspector”)enase ção“Cus-
88

## Página 101

CasadoCódigo Capítulo5. Storyboards
tomClass”insiraovalor“ListarViewController”,conformemostraaimagem
5.15.
Figura5.15:IdentificadordaSegue
Tendo feito isso, abra o Assistant Editor (“CTRL+ENTER”) e crie as acti-
onsparaosdoisbotões. Comosugestão, paraodeEditarchameaactionde“
abrirEditarScene”,e“abrirDetalhesScene”paraodeDetalhes.Oarquivo
ListarViewController.hdeveráestarcomoocódigoabaixo:
# import <UIKit / UIKit.h>
@interface ListarViewController : UIViewController
- (IBAction)abrirEditarScene:(id)sender;
- (IBAction)abrirDetalhesScene:(id)sender;
@end
Todo controlador já contêm um método chamado
performSegueWithIdentifier, que serve para navegar dele para ou-
tra Segue utilizando o identificador definido anteriormente. O arquivo
ListarViewController.mdeveconteraimplementaç ãodosmétodos“abrir”
conformeabaixo:
- (IBAction)abrirEditarScene:(id)sender {
[self performSegueWithIdentifier:@"listarParaEditarSegue"
sender:sender];
}
- (IBAction)abrirDetalhesScene:(id)sender {
[self performSegueWithIdentifier:@"listarParaDetalhesSegue"
89

## Página 102

5.3. NavegardevoltadiretamenteparaaSegueinicial CasadoCódigo
sender:sender];
}
Rodeoaplicativoeinterajacomosbotõesparaveroresultado.
5.3 N avegar de volta diretamente para a Segue ini-
cial
UmadascoisasatreladasaousodeNavigationControllerséque,amedidaemque
navegamosdeumcontroladorparaoutro,elesvãosendocolocadosemumapilha,
umemcimadooutro,eparavoltarparaastelasanterioréprecisoirclicandono
botão“Voltar”(aqueledocantosuperioresquerdo).Sóquequandoqueremosvoltar
paraalgummaisdistante,énecessáriofazerissováriasvezes.
Comstoryboardsexisteumamaneiradetornaresteprocessoumpoucomais
fácil,atravésdousodaaç ãode“Saída”,dotermoeminglês“Exit”. Naverdade,o
termoutilizadopeladocumentaç ãoé“UnwindSegue”,porémnoXcodeapalavra
“Exit”éutilizado,paranosconfundirumpouco!
Funcionaassim,emdoispassos:adicionamosummétodocomqualquernome
naSegueparaondedeseja-se retornar(porexemplo,“resetarNavegacao”)eque
recebaumargumentodotipo UIStoryboardSegue,eainaSeguede origem,que
irádispararaação,fazemosumlinkentreobotãoeaaç ãode Unwind,ouExit.
Para demonstrar, vamos definir que queremos voltar da Segue “Detalhes”
( Inicio -> Listar -> Detalhes) para o início da app. Para isso, adi-
cione uma nova classe chamada “InicioViewController” que herde de
UIViewControllercomofeitoanteriormente(nãoesque çadeinformaronome
delanocampo“CustomClass”doIdentityInspectornaStoryboard).Aiabraoar-
quivo“InicioViewController.m”eadicioneoseguintecódigo:
-(IBAction)resetarNavegacao:(UIStoryboardSegue *) segue {
// Nao precisa de código
}
Vejaqueocorpodométodoévaziomesmo,emboravocêpossacolocaralgum
códigocasoqueira-porémissonãoéobrigatório.
Paraosegundopasso,váatéaSegue“Editar”naStoryboard(nãoénecessá-
riocriarumaclassecustomizada)eadicioneumbotãocomotexto“Voltarparao
90

## Página 103

CasadoCódigo Capítulo5. Storyboards
início”. Emseguida,selecioneobotão,segure CTRLeclique+arrasteparaobo-
tãoverde,conformemostraaimagem 5.16.Nopopupqueabrir,selecioneoitem“
resetarNavegacao”.
Figura5.16:Associaraaç ãoUnwindaumbotão
Rodeoaplicativoevejaoresultado.
91

## Página 104

5.4. PassardadosdeumaSegueparaoutra CasadoCódigo
Informar se a Segue pode aceitar a aç ão de Unwind
Existeummétododeimplementaç ãoopcionalqueserveparaindicarseaquele
controladorpodeoudeveaceitaraaç ãodeUnwind,combaseemcondicionaiscri-
adaspelodesenvolvedor,comolocal(Segue)deorigemededestino.Casoestemé-
todoretorne“YES”.Umoutrocasoqueelepodesernecessárioéquandoaaç ão
deUnwindpassapordiversasSeguesintermediáriaseoretornoacabaparando“no
meiodocaminho”,mesmoquandonãodeveria.Nestescasos,portando,implemente
ométodoeretorne“NO”.Vejaocódigoabaixo:
-(BOOL) canPerformUnwindSegueAction:(SEL)action
fromViewController:(UIViewController *)fromViewController
withSender:(id)sender {
return YES;
}
Retornar“YES”indicaqueocontroladorpodemanipularaaç ãodeUnwind,
ondenestecasodeverátertambémimplementadoométodoindicadonopopupdo
botãoverde,comofeitoanteriormente.Já“NO”fazaaçãopassardireto.
5.4 P assar dados de uma Segue para outra
Umdetalhefundamentalcomousodestoryboardséqueoscontroladoressãocria-
dosautomaticamente,portantonãotemoscomopassarobjetoseoutrasreferências
peloconstrutor,comogeralmenteéfeitodaformamanual.Aabordagemconsiste,
portanto,emsobrescreverummétodoespecialexistenteem UIViewController
chamado“prepareForSegue”,oqualéexecutadomomentosantesdatransição
paraapróximaSegue.
EstemétodopassacomoargumentoinformaçõessobreaSeguequeestáparaser
executada,incluindoseuidentificadoreareferênciaparaocontrolador.Comisso,
objetospodemseratribuídosatravésdepropriedades.Parademonstraroconceito
énecessáriomexeremdoiscontroladores-odeorigemeodedestino.Nocaso,a
intençãoépassardadosparaocontrolador“Detalhes”(queaindanãofoicriado),
vindodo“Listar”(oqualjácriamos).
Primeirocrieumnovocontroladorchamado“DetalhesViewController”,e
associe-oàteladedetalhesatravésdocampo“CustomClass”noIdentityInspector.
Alémdisso,adicionetambémum UILabel,fazendoadevidaligaç ãocomoar-
92

## Página 105

CasadoCódigo Capítulo5. Storyboards
quivo“DetalhesViewController.h”,atravésdatécnicade“CTRL + clique
e arraste”.Aimagem5.17servedereferência.
Figura5.17:SeguedeDetalhescomaclassedefinida
AproveitandoqueestamosmexendonocontroladordeDetalhes,adicioneuma
propriedadechamada“descricaoDetalhes”,queseráaquelapreenchidaantes
denavegarparaaSegue,atravésdateladelistagem.Ocódigodeveráficarassim:
@interface DetalhesViewController : UIViewController
@property (weak, nonatomic) IBOutlet UILabel *infoLabel;
@property (nonatomic, retain) NSString *descricaoDetalhes;
@end
Feitoisso,opróximopassoéinterceptaroeventodenavegaç ãoparaaSegue,e
definirumvalorparaapropriedade“ descricaoDetalhes". Abra a classe
"ListarViewController.m
// Obs: não esqueça de importar o arquivo "%%DetalhesViewController.h%%"
-(void) prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
if ([segue.identifier isEqualToString:@"listarParaDetalhesSegue"]) {
DetalhesViewController *dc = segue.destinationViewController;
93

## Página 106

5.4. PassardadosdeumaSegueparaoutra CasadoCódigo
dc.descricaoDetalhes = @"Conteúdo vindo da tela de listagem";
}
}
Ocódigonãotemmaioresmistérios: primeiroverifica-seseaSeguequeirá
serexibidaéaquequeremosmanipular,atravésdoidentificadordefinidoanterior-
mente,eemseguidasimplesmentepegamosareferênciaaocontroladorparadefinir
algumvalorapropriedade“descricaoDetalhes”.Essepadrãopode-aliás,deve
-serrepetidosemprequevocêquiserpassardadosdeumaSegueparaoutra.
Rodeoprogramaevejaoresultado. Apareceunatelaotextoquefoidefi-
nido? Provavelmentenão,poisesquecemosdeumdetalhe: configurarotextoda
UILabel.Abraoarquivo“DetalhesViewController.m”eimplementeomé-
todo“viewDidLoad”conformeabaixo:
- (void)viewDidLoad
{
[super viewDidLoad];
_infoLabel.text = _descricaoDetalhes;
}
Simples,não?! Agoravocêjásabetudooqueénecessárioparatrabalharcom
storyboards.
94

## Página 107

Capítulo6
Realizandooperaçõescoma
Internet
AgoravocêjáconhecetodooessencialdaAPIdoiOS.Alémdisso,semprepreci-
samosutilizardiversasbibliotecasextras,sejamelasdaprópriaAPIfornecidapela
Appleouatravésdebibliotecasopensourcequerealizamasmaisdiferentestarefas.
Vamosaprenderausarumabibliotecaexternacomumasituaç ãobemcomum:
baixararquivospelaredeparapoderutilizá-los,sejamfiguras,arquivosdeconfigu-
raçãooudados.
Ocódigo-fontedestecapítuloestádisponívelnapasta“VisualizadorImagens”
e“ExemploDownload”(lembrandoqueoendereçodositecomoscódigosestána
introduçãodolivro).

## Página 108

6.1. ConheçaabibliotecaAFNetworking CasadoCódigo
6.1 C onheça a biblioteca AFNetworking
Realizaroperaçõesderede,comodownloadouuploaddearquivos,alémdeintera-
gircomAPIsdeserviçoscomoTwittereFacebook,sãooperaçõesbastantecomuns
emaplicativosiOS.Comoamadurecimentodaplataforma,diversasbibliotecasque
antesexistiamapenasparaMacOSforamportadasparaiOS,tornandooacessoà
documentação,exemplosesoluç ãodeproblemasalgomuitomaisfácildeconseguir
atualmente.
Abiblioteca AFNetworking, queabordaremosnestecapítulo, éumadasque
maissedestacamnacomunidadededesenvolvedoresdevidoàsuaAPImoderna
eativacomunidade. AFNetworkingfuncionatantoemiOSquantoemMacOS
X.Elaéfeitasobafundaç ãodenetworkingdoprópriosistemaoperacional, ti-
randoproveitodoquehádemelhorparatrabalharcomcomunicaç ãoderede,
tendoporpadrãoinclusiveclassesparalidarcomconteúdoXMLeJSON(além
dasoperaçõesnormais),oqueédegrandeutilidade. Apáginaoficialdoprojeto
éhttps://github.com/AFNetworking/AFNetworking,enolivroutilizamosaversão
2.0.
Oprimeiroexemploconsisteemfazerodownloaddeumarquivoparaumapasta
dentrodonossoaplicativo,mostrandoaousuárioumabarradeprogressoàmedida
queodownloadérealizado.
CrieumnovoprojetonoXcodedotipo SingleViewApplicationchamado“Exem-
ploDownload”.
Em seguida, baixe o projeto disponível no endereço https://github.com/
AFNetworking/AFNetworking/zipball/masteredescompacte-oemqualquerdiretó-
rio.Nestepacote,copieapasta“AFNetworking”paraodiretóriodoprojeto“Exem-
ploDownload”ondeseencontramasoutrasclassesdoprojeto(AppDelegate,View-
Controllereoutras).
Tendofeitoisso,precisamosadicionarasclassesdoAFNetworkingnonosso
projeto. Para tanto, selecione o menuFile -> Add Files to "Exemplo
Download"eselecioneodiretóriodoAFNetworkingquevocêcopiounopassoan-
terior(selecioneodiretóriomesmo,nãoosarquivosdentrodele). Oresultadono
Xcodedeveráficarcomoodafigura 6.1.
96

## Página 109

CasadoCódigo Capítulo6. RealizandooperaçõescomaInternet
Figura6.1:EstruturadoprojetoapósimportaroAFNetworking
Compileoprojeto( COMMAND+B),esecorreutudosemproblemas,vocêdeverá
terumresultadocomoodafigura 6.2.
6.2 C riando a interface de download
Oobjetivodesteaplicativoésolicitaraousuáriooendere çodeumarquivoaserbai-
xado,emostraroprogressoamedidaemqueodownloadocorre.Nãofazdiferen ça
97

## Página 110

6.2. Criandoainterfacededownload CasadoCódigo
seforumarquivoZIP,Imagemouqualqueroutroformato,oidealéapenasqueseja
grandeosuficienteparaverabarradeprogressoemfuncionamento(ex:3MBpara
umaconexãolenta,30MBparaconexõesumpoucomaisrápidas).Aotérminodo
downloadserámostradoumalertacomotamanhototaldoarquivobaixado.
Abraoarquivo Main.storyboardeadicioneosseguintescomponentes:
1) Label,comotexto“URLdoarquivo”
2) TextField,ondeseráinformadooarquivoabaixar
3) UmButtoncomotexto“Download”
4) Umcomponente“ProgressView”,queseráanossabarradeprogresso
5) Umcomponente“ActivityIndicatorView”,queéaquela“rodinha”queficagi-
randoenquantoalgumaaç ãoestáacontecendo
Afigura6.2 mostracomodeveráficarainterface.
98

## Página 111

CasadoCódigo Capítulo6. RealizandooperaçõescomaInternet
Figura6.2:Resultadodaconstruç ãodainterfacedoaplicativo
6.3 C onectando os componentes com o código
AgoraquetemosaUI(“UserInterface”,ouinterfacecomousuário)criada,precisa-
mosconectaroscomponentesaocódigo,afimdepodermosmanipulá-los.Lembre-
sequeoarquivo .storyboardcontémapenasarepresentaçãovisualdoselementos
deumadeterminadatela,eaconexãocomocódigo-fontedeveserfeitamanual-
mente.Existemduasformasdistintasdefazerisso:
1) Usandoo“mini-wizard”doXcode,quefaztodootrabalhopesado(jáutilizada
emcapítulosanteriores)
2) Daformatradicional(comoeraatéoXcode3)
99

## Página 112

6.3. Conectandooscomponentescomocódigo CasadoCódigo
Dependendodotamanhodoseumonitor,aquantidadedepainéisabertosno
Xcodepodetornaratelabastante“poluída”,portantopessoalmentecostumofazero
seguinte:
• AbraoAssitantEditor(View->AssistantEditor->ShowAssistantEditor)
• FecheopainelNavigator(View->Navigators->HideNavigator)
• AbraopainelUtilities(View->Utilities->ShowUtilities)
Lembrandoqueestaéapenasumaconfiguraç ãosugerida,porémvocêdevetra-
balhardamaneiraqueacharmaisprodutivoeconfortável.Contudo,paraasexpli-
caçõesabaixoassume-sequeaconfiguraç ãodetelassugeridaéaqueestarásendo
utilizada.
Aprimeiramaneirajávimoscomofazernoscapítulosanteriores,queéaquela
ondeseguramos CTRLearrastamosumalinhadocomponenteatéoarquivo .h.A
segundamaneiraconsisteemprimeirodeclararmanualmenteocódigorelevanteno
arquivo .h,paraemseguidarealizarasconexões.
Comosarquivos Main.storyboarde ViewController.habertosladoa
lado(vejaaimagem 6.3),comeceeditandooarquivo ViewController.hparaque
fiqueconformealistagemabaixo:
1 @interface ViewController : UIViewController
2 @property (nonatomic, weak) IBOutlet UITextField *downloadField;
3 -(IBAction)startDownload:(id)sender;
4 @end
Nalinha2declaramosocampodetextoqueseráusadoparainformaraURL
doarquivoabaixar,enalinha5édeclaradaaassinaturadométodoparainiciaro
downloademsi.
100

## Página 113

CasadoCódigo Capítulo6. RealizandooperaçõescomaInternet
Figura6.3:Main.storyboardeViewController.hladoalado
Agorafaçaosseguintespassos:
• SelecioneotextfieldnoarquivoMain.storyboard
• Abra o painel Connections, através do menuView -> Utilities ->
Show Connections Inspector
• NopainelConnections,cliqueearrasteabolinha“NewReferencingOutlet”
paracimadadeclaraç ãodoUITextFieldnoarquivo .h
Vejaafigura 6.4parareferência.
101

## Página 114

6.3. Conectandooscomponentescomocódigo CasadoCódigo
Figura6.4:PassosparaconectaroOutletaotextfield
Dessaforma,conectamosapropriedade downloadFieldquefoideclaradano
arquivo .hcomocomponentevisual,permitindomanipulá-lodamaneiraquefor
necessária. Casocontrário,otextfieldseriaapenasumartefatopuramentevisual,
semqualquerutilidade.
Opróximopassoéconectaraaç ãodobotãoquerealizaodownload.Osproce-
dimentossãomuitoparecidoscomodeconectarotextfield,comadiferen çaque
usaremosa IBAction.Ospassossão:
• SelecioneobotãonoarquivoMain.storyboard
• NopainelConnectionsapareceráumgrupochamado“SendEvents”,comuma
sériedeeventospossíveisqueestebotãopodereceber.Oquenosinteressaé
oTouchUpInside,queéoresponsávelporlidarcomumtoque(ou“clique”,se
fosseumaplicativoweboudesktop).ArrasteoconectordoTouchUpInside
paracimadadeclaraçãoda IBActioncriadaanteriormente.Sevocêfizercerto,
iráaparecerumboxdizendo“ConnectAction”
Vejaafigura 6.5parareferência.
102

## Página 115

CasadoCódigo Capítulo6. RealizandooperaçõescomaInternet
Figura6.5:Conectandoaaç ãodobotãodedownload
Repita o mesmo procedimento para os componentes restantes: a
barra de progresso ( UIProgressView) e o indicador de atividade (
UIActivityIndicatorView).Paraaprimeira,utilizeonome progressBar,e
paraosegundo, loading.
Apóstudoisso,ocódigodoarquivo ViewController.hdeveráestarcomoo
exemploabaixo:
@interface ViewController : UIViewController
@property (nonatomic, weak) IBOutlet UITextField *downloadField;
@property (nonatomic, weak) IBOutlet UIProgressView *progressBar;
@property (nonatomic, weak) IBOutlet UIActivityIndicatorView *loading;
-(IBAction)startDownload:(id)sender;
@end
Volte para o “Standard editor” (View -> Standard Editor ->
Show Standard Editor) e abra o arquivo ViewController.m (COM-
MAND+SHIFT+O)paraimplementarocorpodométododobotãodedownload.
Issoénecessárioporquecriamosaconexãodelemanualmenteanteriormente.Veja
noarquivo.mqueométodo -(IBAction)startDownload:(id)sendernão
existenoarquivo.Emqualquerlugar,implemente-odestamaneira:
103

## Página 116

6.4. Realizaraoperaçãodedownload CasadoCódigo
-(IBAction)startDownload:(id)sender {
}
6.4 R ealizar a operação de download
Aimplementaçãocompletadométodo startDownload:émostradaabaixo,eé
umpoucomaislongadoqueosoutroscódigosquevimosatéagora.Contudo,apesar
dotamanho,sãopoucosospontosquemerecemumaexplicaç ãomaisdetalhada.
1 -(IBAction)startDownload:(id)sender {
2 NSURL *url = [NSURL URLWithString:_downloadField.text];
3 NSURLRequest *request = [NSURLRequest requestWithURL:url];
4 NSString *saveFilename =
5 [self downloadSavePathFor:url.lastPathComponent];
6
7 NSLog(@"Salvando o arquivo em %@", saveFilename);
8
9 AFHTTPRequestOperation *operation = [[AFHTTPRequestOperation alloc]
10 initWithRequest:request];
11
12 operation.outputStream = [NSOutputStream
13 outputStreamToFileAtPath:saveFilename append:NO];
14
15 [operation setCompletionBlockWithSuccess:
16 ^(AFHTTPRequestOperation *op, NSHTTPURLResponse *response) {
17 [_loading stopAnimating];
18 _loading.hidden = YES;
19 [self showMessage:@"Download finalizado com sucesso"];
20 }
21 failure:^(AFHTTPRequestOperation *op, NSError *error) {
22 [self showMessage:
23 [NSString stringWithFormat:@"Erro no download: %@",
24 [error localizedDescription]]];
25 }
26 ];
27
28 [operation setDownloadProgressBlock:
29 ^(NSUInteger read, long long totalRead,
30 long long totalExpected) {
31 _progressBar.progress = (float)totalRead / (float)totalExpected;
104

## Página 117

CasadoCódigo Capítulo6. RealizandooperaçõescomaInternet
32 }];
33
34 _progressBar.hidden = NO;
35 _progressBar.progress = 0;
36 _loading.hidden = NO;
37 [_loading startAnimating];
38
39 [operation start];
40 }
MuitasrequisiçõescomoAFNetworking,sejamparaenviaroureceberdados,
utilizamum NSURLRequestparafazerasoperações. Essecódigoéconstruídonas
linhas2e3,enquantoquenalinha9iniciamosoobjetoqueirálidarcomasrequi-
siçõesemsi,atravésdaclasse AFHTTPRequestOperation.Oobjeto NSURLRequest
encapsulatudoarespeitodeumarequisiç ãoHTTP,incluindoaURL,osmétodos
(GET,POST,PUT,DELETE),osheadersecorpodarequisiç ão.
Ocódigoqueseinicianalinha15, setCompletionBlockWithSuccess:,
utilizaumrecursoavan çadodeObjective-Cchamado blocks,que—falandodeuma
maneirabemgeral—sãoobjetosquecontêmumcomportamentoespecífico,que
seráexecutadoemumdeterminadomomento.Blockssãotratadosemdetalhesno
capítulosobreObjective-C.Ocódigocompletodométodoinicianalinha15,com
aoperaçãoquedeveráserexecutadanocasodesucessodaoperaç ão,eterminana
linha26. Alinha21contêmadeclaraç ãodoblockdecódigoqueseráexecutado
nocasodarequisiç ãofalharporalgummotivo. Aassinaturacompletadométodo
é setCompletionBlockWithSuccess:failure:.Nocasodaoperaç ãocom-
pletarcomsucesso,paramosoindicadordeatividadeeoescondemos,conformeas
linhas17e18.
Nalinha28definimosaoperaç ãoqueseráexecutada(quetambémutiliza blocks)
todavezquerecebermosdadosdoservidor—nocaso,pedaçosdoarquivoqueire-
mosbaixar.Nalinha30atualizamosabarradeprogressocomaporcentagematéo
momento,lembrandoqueosvaloresda UIProgressBarvãode0até1(ouseja,
73%érepresentadocomo0.73).
Oscódigosdefinidosemblocossãosempreexecutadosemumoutromomento,
aocontráriodemétodos“normais”.Elessãooschamadoscallbackmethods.OAF-
Networkingtrabalhaautomaticamenteembackground,oqueevitaqueaUIfique
“congelada”,oquefariaousuáriopensarqueoaplicativotravou.
Ocódigodométodo downloadSavePathFor:estáimplementadoabaixo:
105

## Página 118

6.5. TrabalhandocomJSONeimagensremotas CasadoCódigo
1 -(NSString *) downloadSavePathFor:(NSString *) filename {
2 NSArray *paths =
3 NSSearchPathForDirectoriesInDomains(NSDocumentDirectory,
4 NSUserDomainMask, YES);
5 NSString *documentsPath = [paths objectAtIndex:0];
6 return [documentsPath stringByAppendingPathComponent:filename];
7 }
Nalinha1e2pegamosareferênciaparaocaminhododiretório Documentsdo
aplicativo,enalinha3concatenamoscomonomedoarquivoqueseráfeitoodown-
load.Notequeéumcódigorelativamentecomplicadoparaumatarefatãosimples;
comovocênecessitarádocaminhoparaodiretórioDocumentsdiversasvezesemseu
aplicativocasoqueirasalvararquivos,éumaboapráticaimplementá-loemalgum
lugarquepossaserreaproveitado.
Porsuavez,ocódigodométodo showMessage:nãotemnenhummistério,
comovistoaseguir:
-(void) showMessage:(NSString *) message {
UIAlertView *alert = [[[UIAlertView alloc] initWithTitle:@"Aviso"
message:message
delegate:nil
cancelButtonTitle:@"OK"
otherButtonTitles:nil] autorelease];
[alert show];
}
6.5 T rabalhando com JSON e imagens remotas
Alémdaclassedeusogeral AFHTTPRequestOperation,oAFNetworkingvem
comalgumasoutrasclassesbastantepráticasparalidarcomJSON,XMLecarrega-
mentoassíncronodeimagens—estaúltimasedestacaporserumagrandemãona
roda,poisnoslivradeterqueprogramarmuitacoisacasofossemosterquefazero
processomanualmente.
106

## Página 119

CasadoCódigo Capítulo6. RealizandooperaçõescomaInternet
JSON
JSONéumformatosimplesparatransferirdados.Éumsubconjunto
danotaçãodeobjetodeJavaScript,masseuusonãorequerJavaScriptex-
clusivamente.ÉumaalternativaaoXMLetambémpossibilitaorganizar
osdadosdeformahierárquica,conformeexemplificadoabaixo:
// Exemplo de JSON, retirado da API do site 500px.com
{
id: 54007966,
name: "winner and loser",
times_viewed: 2548,
rating: 74.8,
votes_count: 985,
image_url: "http://.....",
images: [
{
size: 4,
url: "http://....."
}
]
}
OpróximoexemplomesclaráousodeJSONcomcarregamentoremotoeassín-
cronodeimagens,paracriarumvisualizadordeimagensdacomunidadefotográfica
500px(http://500px.com). Aoiniciar,oaplicativobuscaráno500pxarelaç ãodas
últimasimagensenviadaspelosusuários,processaroresultadoemostrarasimagens
emcomponentedescrollàmedidaqueousuáriovaiinteragindocomoaplicativo.O
código-fontecompletodesteexemploestálocalizadonapasta VisualizadorImagens,
enafigura 6.6vocêvêumapréviadoaplicativofinalrodando.
107

## Página 120

6.5. TrabalhandocomJSONeimagensremotas CasadoCódigo
Figura6.6:Appmostrandoimagenspúblicasdo500px.com
Comececriandoumnovoaplicativodotipo“SingleViewApplication”,comas
mesmasconfiguraçõesutilizadasnoexemploanteriorechame-ode“VisualizadorI-
magens”.Depoisdecriaroprojeto,nãoesque çadeincluiropacotedoAFNetwor-
king,copiandoodiretóriocomonaappanterior.
Ainterfacedoaplicativoébastantesimples,consistindoapenasdeumcompo-
nente UIScrollView.Abraoarquivo Main.storyboardemudeacordefundo
aviewparaumtomescuro,comoRGB40,40,40.Paraisso,abrao AttributesIns-
pector( View -> Utilities -> Show Attributes Inspector)ecliqueno
componente“Background”,queabriráaminijanela“Colors”(obs:casonãoapareça
nadaparavocê,cliquenaáreabrancadateladoaplicativoqueaparecenostorybo-
ard).Nela,selecioneaop ção“ColorSliders”(segundodaesquerdaparaadireita)e
depois“RGBSliders”,nocombologoabaixodalupa.Insiraosvaloresefecheajanela
Colors.Vejaafigura 6.7parareferência.
108

## Página 121

CasadoCódigo Capítulo6. RealizandooperaçõescomaInternet
Figura6.7:Mudandoacordefundodocomponente
Emseguida,adicioneocomponente“ScrollView”,disponívelnaObjectLibrary
( View -> Utilities -> Show Object Library),arrastando-oparaquefi-
quecentralizadoeocupetodooespaçodisponível(OXcodejádeverádeixarocom-
ponenteautomaticamentedotamanhodatela,cabendoavocêapenascentralizar).
Porúltimo,precisamosconectaro Outletdoscrollcomocódigodocontroller,etam-
bémdefiniromesmocontrollercomoclasseresponsávelparatratardoseventosque
ocomponenteirágerar.Emoutraspalavras,vamostornaraclasseViewController
comosendoo delegatedoScrollView.
Delegates
Delegateéumpadrãodeprojetonoqualumobjeto delegaotraba-
lhoaserfeitoparaalgumoutroobjeto(odelegatepropriamentedito).
Umadasprincipaisvantagenséqueaclassepodedelegartrabalhopara
algumoutrolugar,melhorandoaseparaç ãoderesponsabilidadesesem
terqueficaramarradaaumadeterminadaimplementaç ão.Delegatessão
utilizadosfrequentementenodesenvolvimentocomObjective-C.
109

## Página 122

6.5. TrabalhandocomJSONeimagensremotas CasadoCódigo
Paraconectarooutletoprocessoéomesmodesempre:comoAssistantEditor
aberto,selecioneocomponentenoInterfaceBuilder,segureCTRLearrasteparao
arquivoViewController.haolado,ecrieaconnectionOutletcomonome“scroll”.
Jáconectaroeventodedelegateenvolvealgunspassosamais,masemborapossa
parecercomplicadonumaprimeiratentativa,éalgoquerapidamentevocêdominará:
• Primeiramenteabrao“DocumentOutline”,clicandonapequenasetaquetem
nocantoinferioresquerdo,noInterfaceBuilder
• Selecioneoscroll,entãosegureCTRLearrasteparacimadoitem“ViewCon-
troller”,noDocumentOutline
• Nopequenopopupqueaparecer,selecioneaopção“delegate”
• FecheoDocumentOutline,clicandonamesmasetausadaparaabri-lo
Vejaafigura 6.8parareferência.
110

## Página 123

CasadoCódigo Capítulo6. RealizandooperaçõescomaInternet
Figura6.8:Conectandoodelegatedoscrollview
Oqueacabamosdefazerfoiconfiguraroscrollviewparaqueuseaclasse
ViewController como sendo a responsável por lidar com os eventos do de-
legate dele. Para finalizar esta parte da configuração, é necessário modificar
o arquivo ViewController.h para que ele possa lidar com os eventos correta-
mente. Para isso, modifique a declaração @interface ViewController
: UIViewController para @interface ViewController :
UIViewController<UIScrollViewDelegate>.
AproveitandoqueestamosmexendonoarquivoViewController.h,declareuma
variável de instância do tipoNSArray chamada elementos, e outra do tipo
NSMutableArraychamadaimagens,poisfaremosusodelaslogomais.Ocódigo
doarquivodeveráficarassim:
@interface ViewController : UIViewController<UIScrollViewDelegate>
111

## Página 124

6.6. ConfigurarosblocksdesucessoeerrodoAFNetworking CasadoCódigo
@property (retain, nonatomic) NSMutableArray *imagens;
@property (retain, nonatomic) NSArray *elementos;
@property (weak, nonatomic) IBOutlet UIScrollView *scroll;
@end
Agoratemosdiversastarefasparafazer,detalmaneiraque,aoiniciar,oaplicativo
conecte-seaAPIdo500px,baixeasinformaçõesdasúltimasfotospostadaspelos
usuários,emostre-asemumscrollnamedidaqueinteragimoscomele.Alistade
tarefaspodeserresumidadestamaneira:
• ConfigurarosblocksdesucessoeerrodoAFNetworking
• Configuraroscroll,paraquetenhatamanhosuficienteparacomportartodas
asimagens
• Pré-geraroscomponentesdeimagens(porémsemcarregá-lasainda)
• Códigoparacarregarumadeterminadaimagem
• Carregarasoutrasimagensàmedidaqueinteragimoscomoscroll
6.6 C onfigurar os blocks de sucesso e erro do AF-
Networking
Aprimeirapartedocódigoficaránométodo viewDidLoad,queéummétodode-
claradonaclasse UIViewControllerdaqualanossaclasse ViewControllerherda
(notequeosnomessãomuitoparecidos,cuideparanãofazerconfusão).Eleéexe-
cutadoautomaticamentepeloiOSassimqueaviewdocontrollerécarregadaem
memória,portantoéumbomlugarparaprepararocontrollerparauso,comoinici-
alizarvariáveis,criaroutrasviewsauxiliaresetc.
Lembre-se dos imports
Nãoesque çadeimportaroarquivo AFNetworking.h,atravésda
instrução #import "AFNetworking.h" logonoiníciodoarquivo
ViewController.m
112

## Página 125

CasadoCódigo Capítulo6. RealizandooperaçõescomaInternet
1 -(void) viewDidLoad
2 {
3 [super viewDidLoad];
4
5 NSString *url = @"http://bit.ly/livroios-500px";
6 AFHTTPRequestOperationManager *manager =
7 [AFHTTPRequestOperationManager manager];
8
9 manager.responseSerializer = [AFJSONResponseSerializer serializer];
10
11 [manager GET:url parameters:nil
12 success:^(AFHTTPRequestOperation *operation, id json) {
13 _elementos = json[@"photos"];
14 [self mostraMensagem:[NSString
15 stringWithFormat:@"%d imagens encontradas",
16 _elementos.count]];
17
18 if (_elementos.count > 0) {
19 [self inicializaScroll];
20 }
21 }
22 failure:^(AFHTTPRequestOperation *operation, NSError *error) {
23 [self mostraMensagem:[NSString stringWithFormat:@"Erro: %@",
24 [error localizedDescription]]];
25 }
26 ];
27 }
Alinha9configuraorequestparalidarcomdadosJSON,utilizandoumaclasse
própriaparaissodoAFNetworking,a AFJSONResponseSerializer.Nalinha
12declaramosoblocodesucesso,sendoqueoúltimoparâmetro— id json —é
oqueconteráosdadosdoJSONemsi,porémjáconvertidosparaum NSDictionary
peloAFNetworking.Estaéaparteemqueusar AFJSONResponseSerializeré
vantajoso,poiscasocontrárioteríamosquelidarmanualmentecomalgumabiblio-
tecaJSON.Nalinha13pegamostodosositensretornadospelo500px,eguardamos
parausoposteriornaclasse.
113

## Página 126

6.7. Configuraroscrollepré-geraroscomponentesdeimagens CasadoCódigo
Como saber o que terá no NSDictionary?
Doisdetalhesimportantes: primeiro,adeclaraç ãodobloco success
passaoparâmetro“json”comosendodotipoid,queéumtipocoringa.
SevocêconheceJavaouC#,écomosefosseo“Object”destaslingua-
gens.Alémdisso,adocumentaç ãodoAFNetworkingnãodiznadaex-
plicitamentequeotipopassadoseráumNSDictionary,porémnostestes
realizadosfoiesteocaso,entãoassume-sequeaomenosseráumtipo
compatível.Emsegundolugar,umamaneirafácildedescobriraestru-
turadosdadosnodicionário(quefoiausadaaprimeiravezqueutili-
zeiabiblioteca)ésimplesmentejogaroconteúdonoconsole,atravésde
NSLog(@"%@", json). Comovocêpodever,nãohánenhuma“má-
gica”envolvida,apenasumpoucode“programaçãoorientadaàtentativa
eerro”
Oblock failure,nalinha22,simplesmentemostraamensagemdeerroaousuá-
rio,casoarequisiç ãofalheporqualquermotivo.
6.7 C onfigurar o scroll e pré-gerar os componen-
tes de imagens
Ocomponente UIScrollViewqueadicionamosnoarquivoMain.storyboardfoi
criadoapenascomasconfiguraçõespadrão,eagoravamosdefinirotamanhodaárea
emqueousuáriopoderánavegar,assimcomoadicionarasoutrasviewsqueserão
responsáveispormostrarasimagens. Umadaspropriedadesmaisimportantesdo
UIScrollViewéa contentSize,queespecificaalarguraealturadoconteúdoeque,
dependendodosvaloresinformadosedotamanhodatela,permitequeousuário
façascrollparacimaouparabaixo.Otipodapropriedade contentSizeéCGSize,
queéumaestruturaquecomportalarguraealtura,compontoflutuante( float),
eérelativaaotamanhodo framedoscroll. Portanto,seoscrolltem320x480de
tamanho,um contentSizecomasmesmasdimensõesnãopermitiráarolagemdo
conteúdo,porémseocontentSizeforde,digamos,3200x500,serápossívelrolaruma
grandequantidadenahorizontal,eumpouconavertical.Simplesassim.
1 -(void) inicializaScroll {
2 float largura = self.scroll.bounds.size.width;
114

## Página 127

CasadoCódigo Capítulo6. RealizandooperaçõescomaInternet
3 float altura = self.scroll.bounds.size.height;
4
5 self.scroll.contentSize = CGSizeMake(largura * _elementos.count,
6 altura);
7 self.scroll.pagingEnabled = YES;
8
9 _imagens = [[NSMutableArray alloc] init];
10
11 // Cria todos os lugares onde uma imagem pode
12 // aparecer, para facilitar as coisas na hora
13 // de carregar a imagem de fato do Flickr
14 int indice = 0;
15
16 for (NSDictionary *item in _elementos) {
17 CGRect posicao = CGRectMake(indice++ * largura, 0, largura,
18 altura);
19 UIImageView *img = [[UIImageView alloc] initWithFrame:posicao];
20
21 [_scroll addSubview:img];
22 [_imagens addObject:img];
23 }
24
25 // Adiciona a primeira imagem só para não ficar com a tela vazia
26 [self carregaImagemRemota:0];
27 }
Ocódigodalinha5fazexatamenteoquefoidescritonoparágrafoanterior,defi-
nindoaáreaderolagemhorizontalcomosendootamanhodocomponentedescroll
pelonúmerodeimagensquetemos.Alémdisso,queremosqueousuáriopossaro-
laroconteúdoprecisamenteimagemporimagem,dandoaqueleefeitodequeum
simplesarrastarjápasseparaapróximaimagem.Issoéfeitocomocódigodalinha
6.Nosseustestes,mudeovalordapropriedade pagingEnabledparaNOevejaa
diferençanocomportamentodarolagem.
O NSMutableArrayiniciadonalinha8seráutilizadoparatermosacessorá-
pidoefácilatodososcomponentesdeimagenscriadosmaisabaixonométodo.
Existemoutrasmaneirasdeobteromesmoresultadosemprecisardeumavariável
auxiliarcomoestamosfazendoestecaso,porémaabordagemmostradanesteexem-
ploébastantepráticaenãotemimpactossignificativosnousodamemória,pois
apenasguardaremosreferências.
115

## Página 128

6.8. Carregarumadeterminadaimagem CasadoCódigo
EmiOS,semprequevocêquisermostrarumaimagemaousuário,faráusodo
componente UIImageView.Estecomponente,assimcomotodas views,precisaser
posicionadodemaneiraabsoluta—nãoexisteoconceitodeposicionamentorelativo
emiOS.Ocódigodalinha16criaaposiç ãoondecadaimagemficará,enalinha17
écriadaaimageviewemsi.Senãotivéssemosaconta“ indice++ * largura”,
todasasimagensficariamnomesmolugar,sesobrepondo.Afigura 6.9demonstra
esteprocedimento.
Figura6.9:Representaç ãográficadoposicionamentodasimagensnocomponente
scroll
Comoqueremosqueasimagenssejamroladasatravésdonossocomponente
scrollasadicionamoscomofilhasdomesmo,conformeocódigodalinha19.
6.8 C arregar uma determinada imagem
NopassoanteriorconfiguramosoUIScrollViewejáadicionamostodososcompo-
nentesqueirãocarregarasimagensdo500px,deixandooterrenopreparadopara
omomentodemostrarcadauma.Emborapoderíamoscriarcada UIImagemView
somentequandoousuáriochegassenopontodoscrollemqueelafossenecessá-
ria,issodemandariaumpoucomaisdetrabalho,alémdecorreroriscodecausar
aqueleefeitode“travada”nainterface. Porém,comonãovamosmostrarmilhares
deimagens,pré-gerarfacilitabastanteascoisas.
116

## Página 129

CasadoCódigo Capítulo6. RealizandooperaçõescomaInternet
1 -(void) carregaImagemRemota:(int) indice {
2 NSDictionary *item = _elementos[indice];
3 NSDictionary *imageInfo = item[@"images"][0];
4 NSString *url = imageInfo[@"url"];
5
6 NSLog(@"Carregando a URL %@", url);
7
8 UIImageView *img = _imagens[indice];
9 img.contentMode = UIViewContentModeScaleAspectFit;
10 [img setImageWithURL:[NSURL URLWithString:url]];
11 }
Ocódigodalistagemacimarecebecomoargumentooíndicedaimagemaser
carregada,relativoaoconteúdodoarray imagens,pegaaURLdodicionáriocriado
peloAFNetworkinglánoprimeiropasso,esolicitaodownloadeposteriorexibiç ão
daimagemnatela. Nalinha8pegamosareferênciaaoUIImageViewcriadono
passoanterior,einformamosatravésdapropriedade contentModequeaimagem
deveserrenderizadadetalmaneiraqueapare çaporcompleto,porémrespeitando
asdimensõesdatelaeasdevidaspropor ções.Semestapropriedade,aimagemteria
umaspecto“esticado”,foradasproporçõesoriginais.
Umaparteinteressantedestecódigoestánalinha10,queutilizamaisumrecurso
doAFNetworkingatravésdométodo setImageWithURL:.Estemétodonãoexiste
naAPIpadrãodocomponenteUIImageView,masoAFNetworking—pormeiodo
recursode“Categorias”,oqualéexplicadoemdetalhesnocapítulosobreObjective-
C—adicionaestafuncionalidade.Elaseencarregadefazerodownloaddaimagem
emsegundoplano(ouem“background”,notermomaiscomum)e,casoelajátenha
sidobaixada,deutilizarocachelocaldamesma.Dessaforma,últimaschamadasa
setImageWithURL:comummesmoendere çofarãoapenasumúnicodownload.
Issoéumagrandemãonaroda,poissefossemosterquefazerissomanualmente,o
trabalhoseriagrande.
117

## Página 130

6.9. Carregarasoutrasimagensàmedidaqueinteragimoscomoscroll CasadoCódigo
Importar a biblioteca auxiliar de imagens
Paraqueocódigocompilecorretamenteénecessárioimportaral-
gumasclassesadicionaisquevemjuntocomoAFNetworking. Váao
menu“File->AddfilestoVisualizadorImagens”elocalizeapasta“UI-
Kit+AFNetworking”nodiretórioondedescompactouabibliotecaante-
riormente.
Cliqueem“Add”eemseguidaadicioneaseguintelinhalogonoinício
doarquivo ViewController.m:
# import "UIImageView+AFNetworking.h"
6.9 C arregar as outras imagens à medida que inte-
ragimos com o scroll
Aúltimapartedocódigoéresponsávelporcarregarasdemaisimagensàmedida
quenavegamospeloscroll.Ométodo scrollViewDidScroll:éummétodoes-
pecial,especificadono UIScrollViewDelegatequedeclaramosnoarquivoViewCon-
troller.hanteriormente.OUIScrollViewDelegatetemdiversosmétodosquepodem
serimplementados,comoinícioefimdezoom,animaç ãoeaceleraç ão. Ocom-
portamentodo scrollViewDidScrolléserexecutadodiversasvezes,permitindopor
exemploquealgumaaç ão(comocarregaraimagem)sejafeita enquantooscrollestá
sendorolado.Contudo,optamosporfazerestatarefaapenasquandoousuárioesti-
ver“parado”emumadeterminadaposição:
-(void) scrollViewDidScroll:(UIScrollView *)scrollView {
int x = (int)self.scroll.contentOffset.x;
int largura = self.scroll.frame.size.width;
// Somente carrega a próxima imagem
// caso o scroll tenha parado em uma página
if (x % largura == 0) {
int pagina = x / largura;
[self carregaImagemRemota:pagina];
}
}
118

## Página 131

CasadoCódigo Capítulo6. RealizandooperaçõescomaInternet
Apropriedade contentOffset,utilizadanalinha1,contêmaposiç ãoxeyem
quearolagemdoscrollseencontra.Elaédotipo CGPoint.Casoqueiravisualizar
emdetalhesosvaloresdestapropriedade,vocêpodejogarnoconsoledestaforma:
NSLog("contentOffset: %@",
NSStringFromCGPoint(self.scroll.contentOffset));
Rodeoaplicativo( Command + R)enaveguepelasfotos.Ocódigocompletodo
aplicativoencontra-senapasta VisualizadorImagens.
6.10 F aça seu aplicativo funcionar em todas as ori-
entações
Umdosproblemasqueonossoaplicativoteméque,sevocêtentargirá-loparaaori-
entaçãolandscape(ou“horizontal”,comomuitaspessoasutilizam,especialleigos),
veráqueascoisassimplesmenteficamtotalmentetortas,conformemostraafigura
6.10.
Figura6.10:Aplicativocomproblemasparafuncionaremlandscape
119

## Página 132

6.10. Façaseuaplicativofuncionaremtodasasorientações CasadoCódigo
Simulando funcionalidades de um dispositivo real
OiOSSimulatorquevemcomXcodefuncionasurpreendentemente
bem,sendoinclusivepossívelsimulardiferentesorientações,Geoloca-
lizaçãoealertasdememória. Vocêencontradiversasop çõesnomenu
Hardwaredosimulador.Eisalgumascomumenteutilizadas:
•Girar a tela para a esquerda: Command + Seta para
esquerda
•Girar a tela para a direita: Command + Seta para direita
•Chacoalhar: CTRL + Command + Z
•T ela em escala 100%: Command + 1
•T ela em escala 75%: Command + 2
•T ela em escala 50%: Command + 3
Parasolucionaroproblemaprecisamosreorganizarasimagensdepoisqueoapli-
cativomudardeorientaç ão,posicionando-asnolugarcorreto.Issoénecessáriopor-
que,quandoiniciamosoaplicativopelaprimeiravez,eleabreemportrait(ou“ver-
tical”),etantoocomponente UIScrollViewquandocada UIImageViewnele
adicionadaslevamemconsideraç ãootamanhodatela. Aomudaraorientaç ão,o
tamanhodatelatambémmuda,etemosquelidarcomissocasoacaso.
Vamosprecisardetrêscoisas: umavariáveldecontroleparasabermosqual
é o índice da imagem sendo visualizada no momento, permitir a rotação para
todas orientações, e lidar com o evento de rotação do dispositivo. Para a pri-
meiraparte,declareumavariáveldotipo intnoarquivo ViewController.h
chamada paginaAtual. Em seguida, salve nela o valor passado ao método
carregaImagemRemota:,conformeopedaçodecódigoabaixo:
1 -(void) carregaImagemRemota:(int) indice {
2 // Armazena o índice da imagem atual para usar no evento de rotação
3 paginaAtual = indice;
4
120

## Página 133

CasadoCódigo Capítulo6. RealizandooperaçõescomaInternet
5 // Restante do código já existente no método
6 // ...
7 }
Para permitir rotação para todas as orientações, o método “
shouldAutorotate:”precisaretornarYES,conformeabaixo:
- (BOOL)shouldAutorotate {
return YES;
}
Agoraprecisamosreorganizarasimagensdepoisqueatelagirar,eparaissobasta
sobrescreverométodo didRotateFromInterfaceOrientation::
1 -(void) didRotateFromInterfaceOrientation:
2 (UIInterfaceOrientation)orientacao {
3 float largura = self.scroll.frame.size.width;
4 float altura = self.scroll.frame.size.height;
5 int indice = 0;
6
7 self.scroll.contentSize = CGSizeMake(largura * _elementos.count,
8 altura);
9
10 for (UIImageView *img in self.scroll.subviews) {
11 if (img.frame.size.width > 7 && img.frame.size.height > 7) {
12 img.frame = CGRectMake(indice++ * largura, 0, largura,
13 altura);
14 }
15 }
16
17 CGPoint novaPosicao = CGPointMake(largura * paginaAtual, 0);
18 [_scroll setContentOffset:novaPosicao animated:NO];
19 }
Nalinha7definimosonovotamanhodo scroll,jáquealarguraealturasão
diferentesemcadaorientaç ão. Jáentreaslinhas9a13iteramosporcadaumadas
subviewsdo scrollparacolocá-lasnanovaposiç ão. Acondicionaldalinha
10nãoéexatamenteumaboaprática,porémparaefeitosdesimplicidadedaexem-
plificaçãoelaresolveoproblema. Maisespecificamente,asbarrasderolagemque
aparecemporpadrãona UIScrollViewsãoimagenstambém,comalturaoular-
gurade7pixels,masqueremosmodificarapenasasfotosquevieramdoFlickr.Na
linha10calculamosanovaposiç ãodasfotos.
121

## Página 134

6.10. Façaseuaplicativofuncionaremtodasasorientações CasadoCódigo
Porfim,ocódigodaslinhas15e16colocamo scrollnolugarcorreto,levando
emconsideraçãooíndicedaúltimaimagemvisualizada.
Rodeoaplicativonovamenteegireatela( Command + Seta para direita)
paraveroresultado.
122

## Página 135

Capítulo7
Trabalhandocomtabelas-
UITableView
Apresentaçãodedadostabulareséumadastarefasmaiscomunsqueexistemem
qualquerplataforma,enocasodeiOS,sistemasinteirospodemserdesenvolvidos
emcimadestaformadeapresentaç ãodedados,atravésdaclasse UITableView.
Podemosutilizarumatableviewparaasmaisvariadastarefas:
• Listadepaíses
• Favoritos
• Receitas
• Opçõesdeconfiguraç ão
• Listadecontatos
• Númerosdetelefone

## Página 136

CasadoCódigo
• Tarefasaseremrealizadas
AAPIdeixarelativamenteabertooquepodemosfazercomela,emboraaprincí-
pionãohajanecessidadedemuitacustomizaç ão—atéporqueprecisamoslevarem
contaqueousuárioestaráusandoumdispositivomóvelcomosdedos,enãocom
ummouse.Emsuma,atableviewdisponibilizasuporteaconteúdoadicionadoem
diversaslinhas,quepodemopcionalmenteseremseparadasemse ções.Ospróprios
iDevicescontamcomdiversosaplicativosconstruídosemcimadetableviews: Set-
tings,Contacts,Reminders,favoritosdoSafari,listadeálbunsdo Photoseopróprio
aplicativodaAppStore.Afigura 7.1mostraalgunsexemplosda UITableView.
Figura7.1:DiversasformasdaUITableView
Apesardeter tablenonome,ocomponenteemsinãoatuacomoumatabelade
diversaslinhasecolunas,massimapenasdediversaslinhas,salvopequenascusto-
mizaçõesquepodemserfeitas.Certamenteépossívelcriarcélulastotalmenteespe-
cializadas,emboraissonãosejamuitocomumporquestõesdeusabilidade.Outro
pontoimportanteéque,emboraoconceitoda UITableViewsejabastantesim-
ples,aprenderausaraAPIdemaneiraeficientelevaumcertotempo,comotudo
relacionadoàprogramaçãoparaiOS.Lembroqueasminhasprimeirasexperiências
comestecomponentenãoforamdasmaisagradáveisjustamenteporquefiqueiin-
sistindoemquererentendê-loeusá-loàfor ça,oquefoialgoumtantotraumático.
Conheça-oaospoucos,comofaremosaqui.
O código-fonte deste capítulo está disponível nas pastas “
TableViewSimpleContactList”, “ TableViewDelete” e “
TableViewMultipleDelete” (lembrando que o endereço do site com os
124

## Página 137

CasadoCódigo Capítulo7. Trabalhandocomtabelas-UITableView
códigosestánaintroduçãodolivro).
7 .1 C riando a primeira table view - conceitos e
exemplo
Ok,sevocênãodesistiudeler,entãoaindaháesperan ça.Lembre-sesempre:acurva
inicialdeaprendizadodatableviewéumpoucoíngreme,masdepoistudoficabas-
tanteclaroefluído.Justamenteporestemotivoémuitoimportantequenãopuleesta
pequenaparteconceitual(afinal,oávidoaprendizquerveralgofuncionandologo,
certo?).
Parafuncionar,atableviewprecisasemprequedoistiposdedelegatessejam
implementados:O UITableViewDataSource,oqualprovêosdadoseinforma-
çõesestruturaisgeraisparaa UITableView,e UITableViewDelegate,oqualé
responsávelporlidarcomeventosdeintegraç ãoecustomizaçõesdecadalinha.As
principaisresponsabilidadesdecadaumsão:
A fonte de dados - UITableViewDataSource
Odatasourceéoprotocoloqueforneceosdadosdefatoparaatableview,eo
únicoquetemalgunsmétodosdeimplementaç ãoobrigatóriapelocompilador.
• Númerodeseçõesdatabela
• Númerodelinhas(obrigatório)
• Eventosdereordenação,inser çãoesele çãodedados
• Títulodocabeçalhoerodapé
• Forneceroconteúdoemsideumadeterminadalinha(obrigatório)
Configurações e aç ões - UITableViewDelegate
Emborao UITableViewDelegatenãotenhanenhummétododeimplemen-
taçãoobrigatória,écomelequedefatointeragimoscomatableviewemsi.
• Alturadalinha
• Lidarcominteração(toque)deumadeterminadalinha
125

## Página 138

7.1. Criandoaprimeiratableview-conceitoseexemplo CasadoCódigo
• Lidarcomaediçãodealgumalinha
Estas são os principais eventos que precisamos implementar, independente-
mentedotipodeconteúdoqueseráapresentadonatableview,poiselessãoospilares
paraocorretofuncionamento.Nãoesperoquevocêconsigaselembrarsemprede
cabeçaquaissãoasassinaturasdetodososmétodosquedevemserimplementados
paracolocarumatableviewparafuncionar—eumesmonãolembrodetudoaté
hoje. Oimportanteévocêsaberoquedeveserfeito,comofazere,talvezomais
importantedetudo,saber ondeencontraradocumentaçãonocasodedúvidas.
Aprincipalinten çãodoprimeiroexemplonoqualtrabalharemos—umalista
decontatos—éfocarnaformadecriaç ãoeorganizaç ãodocódigonecessáriopara
tera UITableViewfuncionando.Seemalgummomentovocêpensar“...masisso
émuitocódigoparapoucacoisa...”,lembre-sequeatableviewprecisadeumcon-
juntomínimodeinformaçõesparafuncionar,independentementesemostraremos
umúnicoregistroouummilhão.Afigura 7.2mostraaaplicaçãodepoisdefinalizada.
Figura7.2:PrimeiroexemplocomUITableView
126

## Página 139

CasadoCódigo Capítulo7. Trabalhandocomtabelas-UITableView
7 .2 O aplicativo de lista de contatos
Começaremoscomumnovoexemplo,paradepoisvocêpraticarcomonossocatá-
logodeempresas.
Oaplicativoquecriaremosaseguirconsisteemumahipotéticalistadecontatos,
quemostraonomeeotelefonedeumdeterminadoitemquandoalgumelemento
databelarecebeoeventodetoque.Paracome çar,crieumnovoprojetodotipo Sim-
pleViewApplication chamado“TableViewSimpleContactList”,utilizandoasopções
padrão.Feitoisso,sigaospassosabaixo:
1) Abraoarquivo Main.storyboard;
2) InsiraumLabelcentralizadonotopo,comotexto“Listadecontatos";
3) Adicioneocomponente“TableView”logoabaixodolabel,redimensionando-o
paraocuparorestodoespaçodatela;
4) Com oAssistant Editoraberto (View -> Assistant Editor -> Show Assistant
Editor), cliqueemcimadocomponentetableview, segureCTRLearrasteo
mouseparaoarquivo ViewController.h,inserindouma Connectiondotipo
Outletchamada tabelaContatos(obs:seocorrerdoXcodemostraroarquivo
.m,certifique-seprimeirodealternarparao .hutilizandoabarrasuperior.Você
deveráveronomedoarquivonela );
5) Agoracliquecomobotãodireitoemcimadocomponentetableviewparaabriro
menudeop ções,earrasteabolinhadosoutlets datasourcee delegatepara
oViewController,queérepresentadoporumcírculoamarelo. Vejaafigura 7.3
parareferência;
6) Para que a nossa classeViewController receba os eventos da table
view,énecessárioaindaespecificarosprotocolos UITableViewDelegatee
UITableViewDataSourcenadeclaraçãoda @interface;
7) Porúltimo,precisamosdeumarrayparaarmazenaroscontatosqueserãocarre-
gadosdeumarquivodeconfiguraç ão.Paraisso,declareummembrodeinstância
dotipo NSMutableArraychamado contatos.
127

## Página 140

7.3. Carregandooscontatosapartirdeumarquivoplist CasadoCódigo
Figura7.3:Conectandoaspropriedadesdatasourceedelegate
Vejanalistagemabaixocomodeveráficaroseuarquivo ViewController.h:
# import <UIKit / UIKit.h>
@interface ViewController : UIViewController<UITableViewDataSource,
UITableViewDelegate> {
NSMutableArray *contatos;
}
@property (weak, nonatomic) IBOutlet UITableView *tabelaContatos;
@end
7 .3 C arregando os contatos a partir de um arquivo
plist
A UITableViewnãoimpõequaisquerrestriçõesdeondeosdadosdeverãovir,o
queéexcelente. Elaapenaspede“porfavor,meforne çaosdadosdalinhaX ”,eaí
128

## Página 141

CasadoCódigo Capítulo7. Trabalhandocomtabelas-UITableView
ficaanossocargobuscartalinformaç ãoondequerqueseja.Nocasodoaplicativo
delistadecontatos,asinformaçõesestãoemumarquivo plist,ou“PropertyList”
(particularmentepronunciocomo“pêlist”),queéumformatorelativamentecomum
emaplicaçõesMaceiOSparaarmazenarcoisassimples.Naprática,nadamaiséque
umdocumentoXMLcomalgumastagsespecíficas.Suautilidadeécomoadeum
dicionário(chaveevalor),comadiferen çadequeépossívelespecificarotipode
dados.
Crieoarquivo contatos.plistemFile->New->File...->Resource->Pro-
pertyList,eabra-onoXcode.Existemtrêscolunas: Key,queobviamenteéonome
dachavedodicionário, Typeparainformarotipodedados(dicionário,array,nú-
mero,string,data,booleanoouconteúdo“genérico”),eValue,queéovalordachave
defato.
Logoapóscriaroarquivo,vocêveráqueexisteumachavechamada“Root”do
tipo“Dictionary”,eoconteúdoqueformosadicionardeveráserfilhodestachave.
Cliquecomobotãodireitoeselecioneaop ção“Add Row”,eemseguidanomeie
“contatos”eselecione“Array”como“Type”. Cadaumdoselementosdestearray
seráoutrodicionáriocontendoaschaves“nome”e“telefone”,osquaisiremoslere
organizaremumaestruturadedadosespecializadanahoraemqueoaplicativofor
iniciado.
Cliquecomobotãodireitoemcimade“contatos”eselecioneAddRow.A Keydo
itempodeserqualquercoisa(usei“Item0”,“Item1”etc.),enquantoqueoTypedeve
serconfiguradopara Dictionary.Insiraduaschavesdotipo String,umapara
onomeeoutraparaotelefonedocontato.Repitaaoperaç ãoatécansar.Afigura 7.4
mostracomodeveráficaroseuarquivo.
129

## Página 142

7.3. Carregandooscontatosapartirdeumarquivoplist CasadoCódigo
Figura7.4:Organizaçãodoarquivocontatos.plist
Corrigindo o aninhamento
Casooselementosnãoestejamsendocriadosnahierarquiaesperada,
épossívelaninhá-loscomoitemdemenu“ShiftRowRight”paratornar
oelementofilhodoqueseencontralogoacima,e“ShiftRowLeft ”paraa
operaçãocontrária.Cliquecomobotãodireitonoelementoeselecione
aop çõadesejada.
Paracarregaroconteúdodoarquivousamosaclasse NSDictionary,enaprá-
ticaissojáseriasuficienteparatrabalharmoscomatableview.Porém,dicionários
commuitosdadossãochatosdetrabalharemuitosuscetíveisaerrosdedigitaç ão.
Oideal,portanto,éutilizarumaestruturadedadosespecializada,e“transformar”o
dicionárioeminstânciasdestaestrutura.Crieumanovaclassechamada Contato
comduaspropriedadesdotipo NSString(jáqueaschavesnopropertylistsão
“strings”)chamadasnomee telefone,conformeocódigoabaixodo Contato.h:
# import <Foundation / Foundation.h>
130

## Página 143

CasadoCódigo Capítulo7. Trabalhandocomtabelas-UITableView
@interface Contato : NSObject
-(id) initWithNome:(NSString *) nome andTelefone:(NSString *) telefone;
@property (nonatomic, retain) NSString *nome;
@property (nonatomic, retain) NSString *telefone;
@end
Eaquido Contato.m:
# import "Contato.h"
@implementation Contato
-(id) initWithNome:(NSString *) nome andTelefone:(NSString *) telefone {
if ((self = [super init])) {
self.nome = nomeInicial;
self.telefone = telInicial;
}
return self;
}
@end
Játemosprontoalistadecontatosemumarquivopróprioeaestruturadeda-
dos Contatopararepresentarnocódigocadaregistrodaquelearquivo. Opró-
ximopassoconsiste,portanto,emjuntarestesdoispedaços,carregandooconteúdo
doarquivo contatos.plistemmemória,armazenandoosregistrosnavariável
contatos.Confiraabaixoométodo loadContacts,quedeveserimplementado
noarquivo ViewController.m:
1 -(void) loadContacts {
2 NSString *plistCaminho = [[NSBundle mainBundle]
3 pathForResource:@"contatos" ofType:@"plist"];
4 NSDictionary *pl = [NSDictionary
5 dictionaryWithContentsOfFile:plistCaminho];
6 NSArray *dados = [pl objectForKey:@"contatos"];
7
131

## Página 144

7.3. Carregandooscontatosapartirdeumarquivoplist CasadoCódigo
8 contatos = [[NSMutableArray alloc] init];
9
10 for (NSDictionary *item in dados) {
11 NSString *nome = [item objectForKey:@"nome"];
12 NSString *telefone = [item objectForKey:@"telefone"];
13
14 Contato *c = [[Contato alloc] initWithNome:nome
15 andTelefone:telefone];
16 [contatos addObject:c];
17 }
18 }
Obs:nãoseesque çadeimportaroheaderdeContato,comainstru ção #import
"Contato.h"logonoiníciodoarquivo
ComoparafinspráticosparaoiOSumarquivoPropertyListéumdicionário,
carregá-loemmemóriaébastantesimples,conformealinha4: bastaiterarpelos
registrostransformando-osem Contatos.
A classe NSBundle
Aclasse NSBundlecontémmétodosparaencontrarecarregarcoisas
quefaçampartedopacotedoseuaplicativo. Porexemplo,ométodo
pathForResource:utilizadoem loadContactsprocuraoarquivo
especificadoapartirdaraizdoprojeto.
Paraqueométodosejaexecutadoaoiniciaroaplicativo,chame-onométodo
viewDidLoad,conformeabaixo:
- (void)viewDidLoad {
[super viewDidLoad];
[self loadContacts];
}
132

## Página 145

CasadoCódigo Capítulo7. Trabalhandocomtabelas-UITableView
Nome das v ariáveis no método initW ithNome
Algumas pessoas irão reparar que as variáveis do mé-
todo initWithNome tem o mesmo nome das @property.
Para evitar conflitos em casos como esse, usa-se a instrução
self.nome e self.telefone para referenciar os membros
da classe. Algumas pessoas preferem utilizar underline nes-
tas situações, como initWithNome:(NSString *) _nome
andTelefone:(NSString *) _telefone,masissoéalgocomple-
tamentedegostopessoal.
7 .4 T ornando a tabela funcional
Agoraquejátemosaestruturageraldoaplicativoconstruída,incluindoalistade
contatosquedeveráserapresentadaaousuário,éhoradefazeraspartesespecíficas
datableview,quesãotrês.Teremosdeinformarquantositenstemosparamostrar,
fornecerosdadosdecadaumdoscontatosparacadalinhaelidarcomoeventode
toqueemumdeterminadocontato.
Osdoisprimeirositensfazempartedoprotocolo UITableViewDataSource,
enquantooterceiropertencea UITableViewDelegate.Ecomoeuseiisso?Fácil,
lendoadocumentaç ão.Depoisdealgumtempovocêprovavelmenteiráselembrar
dememóriaoqueficaemquallugar,portantonãosepreocupedemaisemquerer
decorartudo—apenaslembre-sesempre: senãosouberondeestáalgo,acessea
documentação.
133

## Página 146

7.5. Informandoaquantidadedeitensquetemos CasadoCódigo
Acessando a documentação da API peloXcode
Existeumamaneirabemfácilepráticadeacompanhareacessarado-
cumentaçãodaAPIdoiOSdiretamentepeloXcode,atravésdoinspetor
QuickHelp,conformemostradonafigura 7.5.Parahabilitar,vánomenu
View->Utilities->ShowQuickHelpInspector,eapareceráumpainel
comumabrevedescriç ãodaclasseondeocursordomouseseencontra,
noeditordecódigos.
Figura7.5:Funcionamentodopaineldeajudarápida
7 .5 I nformando a quantidade de itens que temos
Aprimeiracoisaafazeréinformarquantaslinhasatableviewdeveráter,conforme
ocódigoaseguir:
134

## Página 147

CasadoCódigo Capítulo7. Trabalhandocomtabelas-UITableView
- (NSInteger)tableView:(UITableView *)tableView
numberOfRowsInSection:(NSInteger)section {
return contatos.count;
}
7 .6 E xibindo dados em cada linha
Ocomponente UITableViewutilizaumaabordagemumpoucodiferenteparaexi-
birregistros,naqual—aoinvésdemontarmosaslinhascomtudooqueatabela
deveráconter—éprecisoentregarregistroporregistrodemaneiraindireta,dei-
xandoacargodatableviewotrabalhodeconstruiraslinhasegerenciarmemóriae
performance.Emoutraspalavras,éatableviewquemsolicitaoquedeveexibirem
umadeterminadalinha,fazendousodométodo cellForRowAtIndexPathdefi-
nidonoprotocolo UITableViewDataSource(lembre-se:“datasource”significa,
literalmente,“fontededados”emportuguês).
Ocódigoabaixofazexatamenteisso:implementamosométodododatasource,
oqualnospassaoíndicedoelementodesejado,detalformaqueacéluladatable
viewcontenhacomotextoo nomedocontato.
1 - (UITableViewCell *)tableView:(UITableView *)tableView
2 cellForRowAtIndexPath:(NSIndexPath *)indexPath {
3
4 static NSString *CelulaContatoCacheID = @"CelulaContatoCacheID";
5 UITableViewCell *cell = [self.tabelaContatos
6 dequeueReusableCellWithIdentifier:CelulaContatoCacheID];
7
8 if (!cell) {
9 cell = [[UITableViewCell alloc]
10 initWithStyle:UITableViewCellStyleDefault
11 reuseIdentifier:CelulaContatoCacheID];
12 }
13
14 Contato *contato = [contatos objectAtIndex:indexPath.row];
15 cell.textLabel.text = contato.nome;
16
17 return cell;
18 }
Rodeoaplicativo( Command + R,ou Product->Run)evejaoscontatosapare-
135

## Página 148

7.6. Exibindodadosemcadalinha CasadoCódigo
ceremnatabela.Toqueemalgunsregistrostambém.Acontecealgumacoisa?Vere-
moslogomaiscomoimplementarestaparte.
Existemalgunsconceitosimportantesnaformadeconstruç ãodestecódigo,
sendooprincipaldelesemrelaç ãoaperformance.Paraentendermelhor,considere
quea UITableViewéumcomponentequepodeserutilizadoparaumainfini-
dadedesituações,apresentandoaousuárioumaquantidadeilimitadadeelementos.
Comooaplicativorodaemdispositivosmóveisondeosrecursosdehardwaresão
maislimitados—especialmentememória—,édevitalimportânciaquefaç amos
usodemecanismospara reaproveitaralgumascoisas.Emborafossepossívelfazero
códigodalistagemanteriordemaneiramaissimples,omesmopodeeventualmente
serpéssimoemtermosdeperformance.
Testando questões de performance no simulador ver-
sus no device
OiOSsimulatoréumaexcelenteferramentaparaauxiliarodesen-
volvimentodeaplicativos,poisevitaquetenhamosquefazerdeploydi-
retamenteemalgumdispositivo.Porém,algumascoisas—comoocom-
passooueventosdeinclinaç ão—nãopodemsersimuladasnele,eou-
tras,comomemóriaeprocessador,sãoirreais,umavezqueosimulador
rodasoboMacOSX.Portanto,aúnicamaneiradesabercomooapli-
cativosecomportacommuitainformaç ãoeatémesmoparasaberseas
animaçõesestãofluídas,étestardiretamentenodevice.
Paraauxiliarnestequesito,a UITableViewnosforneceaop çãodereutilizaras
UITableViewCellsqueperten çamaumamesmacategoriadedados(oquedeve
representaramaiorpartedoscasosemseusaplicativos),oqueéfeitonaslinhas5
e6comométodo dequeueReusableCellWithIdentifier:. Elerecebeum
identificadorqueéutilizadointernamenteparapegar cellsdeumcachesempreque
possível.Nocasodonossoaplicativo,oidentificadoréaquelerepresentadopelocó-
digodalinha4,quechamamosde CelulaContatoCacheID,queéumvalorarbitrário,
semnenhumsignificadoespecial.
Casovocêestejaseperguntandoseexisteapossibilidadedeocorreralgumtipo
deproblemacomestaabordagemdereutilizaç ãodecélulas,arespostaé“talvez”.
Ouseja,separtirmosdoprincípioqueaoinvésdecriar1000instânciasdacélulaa
tabelacriaapenas20easreutilizaparatodooconjuntodedados,éresponsabilidade
136

## Página 149

CasadoCódigo Capítulo7. Trabalhandocomtabelas-UITableView
doprogramadorgarantirquetodasaspropriedadesrelevantessejampreenchidas,
casocontrárioovalordefinidoporquemutilizouacélulaporúltimoseráexibido.
Façaumtesteecomprovevocêmesmo.
Na linha 10 iniciamos a célula com o estilo padrão (
UITableViewCellStyleDefault), o qual mostra uma linha de texto ape-
nas,queéaqueleatribuídonalinha15.Asoutrasop çõessãoaslistadasabaixo,ena
figura7.6háumademonstraçãodecadaumdosestilos.
•UITableViewCellStyleSubtitle:Títuloemnegritoalinhadonocanto
superioresquerdo,eumsubtítulocinzaalinhadonocantoinferioresquerdo,
acessívelpelapropriedade detailTextLabel
•UITableViewCellStyleValue1:Textonacorpretaalinhadoàesquerda,
eumoutrotextonacorazulalinhadoàdireita,acessívelpelapropriedade
detailTextLabel
•UITableViewCellStyleValue2:Textodapropriedade textLabelàes-
querdaenacorazul,eovalordapropriedade detailTextLabelàdireita
nacorpreta
Figura7.6:Osdiferentesestilospré-configuradosdeumaUITableViewCell
137

## Página 150

7.7. Permitindointeraçãocomositensdatabela CasadoCódigo
7 .7 P ermitindo interação com os itens da tabela
Toda vez que o usuário toca em uma linha da table view, o método
didSelectRowAtIndexPath: é disparado, dando-nos a chance de realizar
alguma ação — que no nosso caso será mostrar uma mensagem utilizando
UIAlertView.Comomuitosdosoutroseventosdatableview,estemétodorecebe
oíndicedalinhaselecionada,queusaremosparapegarorespectivoregistrona
variávelcontatos:
1 - (void)tableView:(UITableView *)tableView
2 didSelectRowAtIndexPath:(NSIndexPath *)indexPath {
3
4 Contato *contato = [contatos objectAtIndex:indexPath.row];
5 NSString *msg =
6 [NSString stringWithFormat:@"Nome: %@\nTelefone: %@",
7 contato.nome, contato.telefone];
8
9 UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"Contato"
10 message:msg
11 delegate:nil
12 cancelButtonTitle:@"OK"
13 otherButtonTitles:nil];
14 [alert show];
15
16 [self.tabelaContatos deselectRowAtIndexPath:indexPath animated:YES];
17 }
Ocódigodalinha13fazcomquealinhaautomaticamentepercaasele çãoapós
ainteração(removaalinhaevejaoqueacontece).Rodenovamenteoaplicativoe
interajacomosregistros.
7 .8 R emovendo elementos da table view
Em aplicativos iOS, uma operação que os usuários estão acostumados a fa-
zer é realizar o movimento deswipe da direita para esquerda (ou, tecnica-
mente umswipe left), que é aquele movimento de deslizar rapidamente o
dedo no eixo horizontal. Tanto por conveniência quando para manter um
comportamento padrão nos aplicativos aUITableView (através do delegate
UITableViewDelegate)jádisponibilizatalfuncionalidade,bastandoimplemen-
138

## Página 151

CasadoCódigo Capítulo7. Trabalhandocomtabelas-UITableView
tarmosométodo tableView:commitEditingStyle:forRowAtIndexPath:
conformeabaixo:
1 -(void) tableView:(UITableView *)tableView
2 commitEditingStyle:(UITableViewCellEditingStyle)editingStyle
3 forRowAtIndexPath:(NSIndexPath *)indexPath {
4
5 [contatos removeObjectAtIndex:indexPath.row];
6 [self.tabelaContatos reloadData];
7 }
Ofuncionamentoéoseguinte:oiOSverificaseexisteaimplementaç ãodeste
métodonanossaclasse,ecasopositivo,habilitaaoperaç ãode swipeleftpararemover
algumalinha,invocandoométodoemsiquandoousuáriointeragecomobotão.
Vejanafigura 7.7oresultado.
Figura7.7:Interfacepadrãodobotãodeletar
139

## Página 152

7.9. Removendodiversaslinhas CasadoCódigo
Note que o texto padrão no botão está em inglês. Para
especificar outro texto, temos que implementar o método
tableView:titleForDeleteConfirmationButtonForRowAtIndexPath:
-(NSString *) tableView:(UITableView *)tableView
titleForDeleteConfirmationButtonForRowAtIndexPath:
(NSIndexPath *)indexPath {
return @"Remover";
}
7 .9 R emovendo diversas linhas
Umaoutramaneiraderemoverregistroséaqueleemqueousuáriotocaemum
botãoEditareatableviewmostraumasériedepequenosbotõesredondoscomum
símbolodesubtraç ão,conformemostradonafigura 7.8. Paraobteresteresultado,
adicioneumbotãonainterfacechamado botaoEditar,econecteumaaç ãoaele
chamada botaoEditarTap,ondeiremosenviarumamensagemàtabelaparaque
elaentreemmododeediç ão.Porúltimo,especificamosotipodeoperaç ãoaserfeito
emcadaumadaslinhas.
140

## Página 153

CasadoCódigo Capítulo7. Trabalhandocomtabelas-UITableView
Passos para adicionar o botão
Casotenhaficadonadúvida, ospassossãoesses: abraoarquivo
Main.storyboard,adicioneumcomponente“Button”aoladodola-
bel“Listadecontatos”,ativeoAssistant editor,certifique-seque
oarquivo ViewController.hestejaselecionadonopaineldadireita,
CTRL+cliqueearrastedobotãoparaoarquivo.hparacriarumOutlet
comonomede“botaoEditar”,eemseguidamaisumCTRL+cliqueear-
rasteparacriarumaActioncomonome“botaoEditarTap”.
Ocódigodoarquivo“ViewController.h”deveráestarassim:
# import <UIKit / UIKit.h>
@interface ViewController : UIViewController<UITableViewDataSource,
UITableViewDelegate> {
NSMutableArray *contatos;
}
@property (weak, nonatomic) IBOutlet UIButton *botaoEditar;
@property (weak, nonatomic) IBOutlet UITableView *tabelaContatos;
- (IBAction)botaoEditarTap:(id)sender;
@end
Confiraocódigoabaixo:
1 // Executado quando o usuário toca no botão Editar
2 - (IBAction)botaoEditarTap:(id)sender {
3 if ([self.botaoEditar.titleLabel.text isEqualToString:@"Editar"]) {
4 [self.tabelaContatos setEditing:YES animated:YES];
5 [self.botaoEditar setTitle:@"Pronto"
6 forState:UIControlStateNormal];
7 }
8 else {
9 [self.tabelaContatos setEditing:NO animated:YES];
10 [self.botaoEditar setTitle:@"Editar"
11 forState:UIControlStateNormal];
12 }
13 }
141

## Página 154

7.9. Removendodiversaslinhas CasadoCódigo
14
15 // Tipo de operação a ser feita. Neste caso em específico,
16 // queremos permitir apenas a remoção de elementos
17 // (é possível inserir novos também)
18 -(UITableViewCellEditingStyle) tableView:(UITableView *)tableView
19 editingStyleForRowAtIndexPath:(NSIndexPath *)indexPath {
20 return UITableViewCellEditingStyleDelete;
21 }
Ocódigodométodo botaoEditarTap:nãotemmuitomistério,sendoque
aaçãodecolocaratableviewemmododeediç ãoesairdeleéfeitonaslinhas4e
8respectivamente.Deresto,verificamosotextodobotãoparaalteraramensagem
mostradaaousuário.Jánalinha17informamosexplicitamentequeaúnicaoperaç ão
quequeremospermitiréaderemo çãodeelementos—aoutrapossíveléinserir
novosregistros.Orestodotrabalhoéfeitopelocódigovistonosexemplosanteriores.
Figura7.8:Removendomúltiplaslinhas
142

## Página 155

CasadoCódigo Capítulo7. Trabalhandocomtabelas-UITableView
7 .10 C rie uma tabela para o nosso catálogo de em-
presas
Eisumdesafio:utilizarosconhecimentosaprendidosatéagoraparamodificaroapli-
cativodecatálogodeempresasfeitonocapítulo 3,paraquealistagemdasempresas
sejamostradaemumatableviewaoinvésdeexibirapenasnoconsole. Aideiaé
que,apósclicarnobotãosalvar,oatualmétodo mostraCatalogoapresentadona
seção 3.16instancieumnovocontrolador,oqualreceberácomoargumentoalista
deempresasdisponíveisnavariável catalogo,econstruiráatableviewcomos
dados.Utilizeo UINavigationController(apresentadonocapítulo 4)parair
deumcontroladorparaoutro.
Comopontodepartida,vocêpodeseguirosseguintespassos: crieumanova
classechamada“ExibeCatalogoController”queestendaUIViewController,uti-
lizandoaop çãodecriaroarquivo .xibconjuntamente. Adicioneumcompo-
nente UITableVieweconecte-oaoarquivo ExibeCatalogoController.h,
aproveitandoparadeclarartambémuma @propertyparaavariável catalogo
que será passada pela outra classe. Não esqueça de informar os protocolos
UITableViewDataSourcee UITableViewDelegate.
Oesqueletomínimodanovaclassedeveráseparecercomocódigoabaixo:
// ExibeCatalogoController.h
# import <UIKit / UIKit.h>
@interface ExibeCatalogController :
UIViewController<UITableViewDelegate, UITableViewDataSource>
@property (weak, nonatomic) IBOutlet UITableView *tabela;
@property (nonatomic, assign) NSArray *catalogo;
@end
// ExibeCatalogoController.m
# import "ExibeCatalogController.h"
# import "Empresa.h"
@implementation ExibeCatalogController
@synthesize tabela, catalogo;
- (NSInteger)tableView:(UITableView *)tableView
143

## Página 156

7.10. Crieumatabelaparaonossocatálogodeempresas CasadoCódigo
numberOfRowsInSection:(NSInteger)section {
return self.catalogo.count;
}
- (UITableViewCell *)tableView:(UITableView *)tableView
cellForRowAtIndexPath:(NSIndexPath *)indexPath {
return nil;
}
@end
Jánométodo mostraCatalogo,chameonovocontroladordestaforma:
-(void) mostraCatalogo {
ExibeCatalogController *c = [[ExibeCatalogController alloc] init];
c.catalogo = catalogo;
[self.navigationController pushViewController:c animated:YES];
}
Boasorte!Todainformaç ãodequevocêprecisaestánoscapítulosapresentados
atéagoranolivro.
144

## Página 157

Capítulo8
Trabalhandocomreconhecedores
degestos
Diferentementedeaplicativosquesãofeitosparaseremutilizadosemcomputadores
commouseetecladofísicos,ainteraç ãocomoiOSdá-seunicamentepordiversos
tiposdetoquesnatela,indomuitoalémdoqueépossívelfazerapenascomum
mouse.Aoperaç ãomaispadrãoenaturaléadetocarumaúnicaveznatelacomose
estivéssemosclicando.Éalgotãosimplesquenãoprecisademaioresexplicações—
umacrian çade1anodeidadeouumapessoade95anossemafinidadetecnológica
sesairámuitobemcomestaoperaç ão.
Emcontrapartida,existemumasériedeoutrasinteraçõesquerequeremum
poucomaisdetrabalhoparainterpretarcorretamente,comodeslizarodedo(swipe),
tocaresegurar(longpress),movimentodepin ça(pinch),doistoques(doubletap)e
oquemaisaimaginaç ãopermitir.
Existemduasmaneirasdelidarcomeventosdetoque:trabalhandocomosis-
temaemmaisbaixonível,quepermiteomáximodecustomizaç ão(etambémrequer

## Página 158

8.1. Sistemadeeventostradicional CasadoCódigo
muitomaistrabalhoparaimplementar),eosreconhecedoresdegestos,quesãoal-
gumasclassesprontasparaasoperaçõesmaiscomuns.
Ocódigo-fontedestecapítuloestádisponívelnaspastas“GestoSwipe”,“TapCir-
culos”,“TremeTreme”e“ViewTouchEventEx1”(lembrandoqueoendereçodosite
comoscódigosestánaintroduç ãodolivro).
8.1 S istema de eventos tradicional
Osistemadeeventostradicional—assimchamavaaúnicaabordagemqueexistiaaté
oiOS3.2—consistenotrabalhoconjuntodeumasériedemétodosque,emboramais
trabalhososdeimplementar,permitemomáximodecustomizaç ãonamaneiracomo
ostoquesqueousuáriofaznatelasãointerpretados.Todososmétodospertencemà
classe UIView(maisprecisamente,pertencema UIResponder,dequem UIView
herda)epodemsersobrescritosconformeforemnecessários.Osprincipaissão:
•-(void)touchesBegan:(NSSet *)touches withEvent:(UIEvent
*)event
•-(void)touchesMoved:(NSSet *)touches withEvent:(UIEvent
*)event
•-(void)touchesEnded:(NSSet *)touches withEvent:(UIEvent
*)event
•-(void)touchesCancelled:(NSSet *)touches
withEvent:(UIEvent *)event
O método touchesBegan ocorre quando o usuário inicialmente toca a
tela, e o touchesEnded é disparado quando o usuário remove o dedo. Já
touchesCancelledédisparadopeloiOSquandoalgumacoisaocorreemalgum
lugarqueobrigaoseventosdetoqueaseremcancelados—osmotivosvariambas-
tante.Porúltimo, touchesMovedserveparalidarmoscomoscasosondeousuário
arrastaodedopelatela.
146

## Página 159

CasadoCódigo Capítulo8. Trabalhandocomreconhecedoresdegestos
Interação com componentes comuns do dia a dia
Algoimportantearessaltaréquetodainformaç ãodestecapítulo
aplica-seaviewscustomizadasqueconstruímos. Oscomponentespa-
drãododiaadia,como UIButton, UITableView, UITextViewe
afinsjátêmosseusprópriosmecanismosparalidarcominteraçõesdo
usuário. Aspossibilidadesdecustomizaçãoquesãoapresentadasaqui
sãoummecanismoparacasosespeciais.
Paramelhordemonstrarcomolidarcomesteseventos,vamosfazerumaplica-
tivoquedesenhacírculosvermelhosemcadaregiãodetoque.Crieumnovoprojeto
chamado“ViewTouchEventEx1”elogoemseguidaadicioneumanovaclassecha-
mada CirculoView,queherdade UIView(File->New->File->CocoaTouch->
Objective-CClass->SubclassofUIView ). Arazãodecriarmosumaviewcustomi-
zadaéqueoseventosdetoqueprecisamsersobrescritose,alémdisso,paradesenhar
oscírculosénecessáriotambémimplementarmanualmenteocódigodedesenho.
Como a intenção é desenhar todos os pontos de toque, e não apenas o
último, precisamos guardar cada uma das interações. Para isso, usamos um
NSMutableArray(jáqueo NSArraynãopodesermodificadoapóssercriado),
conformeocódigoabaixo,doarquivo CirculoView.h:
// CirculoView.h
# import <UIKit / UIKit.h>
@interface CirculoView : UIView {
NSMutableArray *circulos;
}
@end
Adiversãoocorrenoarquivo CirculoView.m. Aprimeirapartedocódigo
consisteemregistrarumlogdequandoousuáriotocanatela(unicamenteporques-
tõesdevisualizaraordemdoseventos),eregistraropontodetoquequandoodedo
forretiradodatela.Vejaocódigoabaixo:
1 // CirculoView.m - Código parcial
2 -(void) touchesBegan:(NSSet *)touches withEvent:(UIEvent *)event {
3 NSLog(@"Recebido touchesBegan");
4 }
147

## Página 160

8.1. Sistemadeeventostradicional CasadoCódigo
5
6 -(void) touchesEnded:(NSSet *)touches withEvent:(UIEvent *)event {
7 if (!circulos) {
8 circulos = [[NSMutableArray alloc] init];
9 }
10
11 NSLog(@"Recebido touchesEnded. Registrando o ponto de toque");
12
13 UITouch *toque = [touches anyObject];
14 CGPoint localizacaoToque = [toque locationInView:self];
15
16 // Precisamos encapsular o CGPoint dentro dentro de um NSValue
17 // o CGPoint não é um objeto propriamente dito
18 [circulos addObject:[NSValue valueWithCGPoint:localizacaoToque]];
19
20 [self setNeedsDisplay];
21 }
Porconveniênciainiciamosapropriedade circulosnaslinhas7a9,porém
geralmenteomaiscomuméfazerissoemalgummétodo init—masnãoexiste
umaregra,enapráticaacabavalendomuitomaisapraticidadeetipodecódigo
sendofeito.
Nalinha13pegamosoobjetodetoqueemsi,representadopelaclasse UITouch.
Notequeopedaçocorrespondentea [touches anyObject] éumpoucoestra-
nho,masparaestecontextoésegurolê-locomo“retorneo UITouchmaisconveni-
ente”.Umaveztendoobtidooobjetoquerepresentaotoque,precisamossaberem
qualpartedatelaousuáriocolocouodedo,paradesenharocírculonaquelaposiç ão.
Issoéfeitonalinha14atravésdométodo locationInViewda UITouch,quere-
cebeumaoutraviewcomoparâmetro(nocaso,anossaprópriaview)eretornauma
structdotipo CGPointcomaposiçãoconvertidaparaosistemadecoordenadas
danossaview.
Anossalista circulossomentetrabalhacomobjetos,eo CGPoint,porser
uma struct,acabasendoincompatível.Paraisso,nalinha18adicionamosapo-
siçãoobtidanalista circulosencapsulandoavariável localizacaoToqueem
um NSValue,quepodeserconsideradocomoum“objetocoringa”paracarregar
diversostiposprimitivosemlugaresondeapenasobjetossãoaceitos.
Porúltimo,nalinha20,informamosaoiOSqueénecessárioredesenharaview,
paraqueocírculosejamostradonatela.Issoéfeitonocódigoabaixo:
148

## Página 161

CasadoCódigo Capítulo8. Trabalhandocomreconhecedoresdegestos
1 -(void) drawRect:(CGRect)rect {
2 CGContextRef contexto = UIGraphicsGetCurrentContext();
3 CGContextSetLineWidth(contexto, 2.0);
4 CGColorRef corFundo = [UIColor redColor].CGColor;
5 CGContextSetFillColor(contexto, CGColorGetComponents(corFundo));
6 int tamanho = 25;
7
8 for (NSValue *item in circulos) {
9 CGPoint ponto = [item CGPointValue];
10 CGRect regiao = CGRectMake(ponto.x, ponto.y, tamanho, tamanho);
11 CGContextAddEllipseInRect(contexto, regiao);
12 CGContextFillEllipseInRect(contexto, regiao);
13 }
14
15 CGContextStrokePath(contexto);
16 }
Ométodo drawRectéoresponsávelporrealizarastarefasdedesenhonanossa
view,eoiOSchama-oautomaticamentequandonecessário.Numaprimeiraolhada
ocódigocompletodométodoassusta,poisébastantecoisaparapoucoresultado,
utilizandoaAPIproceduraldo CoreGraphicsparafazerosdesenhos.Apartemais
relevanteconcentra-seentreaslinhas8e13,ondeiteramosportodosospontosde
toqueregistradosnométodo touchesEnded,desenhandooscírculosnatela.
Comoalista circuloscontémobjetosdotipo NSValue,nalinha9utilizamos
ométodo CGPointValuepararecuperaro CGPointadicionadoquandoousuário
interagiucomoaplicativo,enalinha10definimosaárea,enquantoqueocódigodas
linhas11e12pintaocírculopropriamentedito.
A propriedade userInteractionE nabled
Toda UIView contém uma propriedade chamada
userInteractionEnabled, que quando definida para o valor
YES, permite a interação do usuário com a view através de eventos
detoque. Porpadrãoestevalorédefinidopara YES,porémalgumas
classes, comoa UIImageView, definemestapropriedadepara NO,
sendoentãonecessáriohabilitá-lamanualmente.
Para utilizar a “CirculoView”, crie uma nova instância dela no método
loadViewnoarquivo“ViewController.m”,conformeabaixo:
149

## Página 162

8.1. Sistemadeeventostradicional CasadoCódigo
# import "ViewController.h"
# import "CirculoView.h"
@implementation ViewController
-(void) loadView {
CirculoView *c = [[CirculoView alloc] init];
c.backgroundColor = [UIColor whiteColor];
self.view = c;
}
@end
Oresultadodoaplicativoestádemonstradonafigura 8.1.
Figura8.1:Resultadodoaplicativoquedesenhacírculos
150

## Página 163

CasadoCódigo Capítulo8. Trabalhandocomreconhecedoresdegestos
8.2 U ma abordagem mais prática: d de gestos
Damesmaformaqueoseventosdetoquepermitemumelevadoníveldecustomi-
zaçãoecontrolesobreasinteraçõesdousuáriocomatela,elespodemfacilmentese
tornarmaiscomplicadosdedesenvolveremanterdoquepoderíamosdesejar.Para
auxiliarnestequesito,aAppleintroduzirnaAPIdoiOSoconceitodereconhece-
doresdegestos(dotermoeminglês GestureRecognizer),quesãorepresentadospor
umconjuntodeclassesparaasoperaçõesmaiscomunsdodiaadia,alémdapos-
sibilidadedequeosnossosprópriosgestossejamcriados(sugestão:funcionalidade
especialnoseuaplicativoparaquemdesenharumdiscovoadorutilizandogestos).
OsseisgestospadrãoquevemcomoiOSsãoosseguintes:
• Toque(tap):classeUITapGestureRecognizer
• Pinça, para zoom (pinch in e pinch out ): classe
UIPinchGestureRecognizer
• Arrastar(panning): UIPanGestureRecognizer
• Deslizar(swipe):UISwipeGestureRecognizer
• Rotacionar:UIRotationGestureRecognizer
• Toquelongo(longpress):UILongPressGestureRecognizer
Comomencionamosnoiníciodolivro,aquestãosobretraduzirounãodetermi-
nadostermosemlivrostécnicosésemprepolêmica,enocasodosreconhecedoresde
gestos(gesturerecognizers)aindaexisteocomplicadorquemuitosdostermosorigi-
naissereferemàsprópriasclasseseconceitos.Nestecapítulomostraremossempre
quepossívelotermoemportuguêsseguidodotermoeminglês,porduasrazões:
aprimeiradelaséqueosclienteseusuáriosleigostêmmaisfacilidadeparaenten-
derinstruçõescomo“façaomovimentodepin ça”doque“façaum pinch”,eisso
ajudamuitoemreuniõeseoutrasconversas.Osegundomotivo—mostrartambém
otermoeminglês—éparafacilitaraidentificaç ãodosmétodoseclassesdaAPI,
assimcomofacilitarnabuscaporconteúdonaInternet.
Existeumadiferen çaquasesutilentreosgestosdearrastar(panning )edeslizaro
dedo(swipe)quepodenãoficarmuitoclaranoinício:aprimeiraconsisteemcolocar
odedonadelaearrastá-locontinuamente,paramoverumaviewdeumlugarpara
outro,porexemplo.Jáodeslizaréummovimentoqueseassemelhaaarrastar,porém
151

## Página 164

8.3. ConvertendooexemploCirculoViewparagestos CasadoCódigo
ocorremaisrapidamenteedeumaúnicavez,sendomuitoutilizadopara“folhear”
jornaiserevistasepassardeumaimagemparaoutranagaleriadefotos.
Gestossãosempreassociadosaalgumaview. Quandoidentificados,osistema
operacionalenviamensagensàclassedeeventosquefoiespecificadanacriaç ãodo
gesto. Alémdisso,sãocategorizadosemdoistipos:contínuos,emquemensagens
doeventosãoenviadascontinuamenteenquantoousuárioestácomodedonatela
—taiscomoogestodedeslizar(panning )—,edescontínuos,queocorremapenas
umaúnicavez—taiscomotoque(tap)oudeslizar(swipe).Oeventodetoquepode
serutilizadotantoparatoquesimples(singletap)comoparaduplo(doubletap)ou
mesmomais:bastaespecificaraquantidadedetoquesdesejadasnahoradecriara
classe.
8.3 C onvertendo o exemplo CirculoView para ges-
tos
Crieumnovoprojetochamado TapCirculosdamesmaformadoprojetofeitono
iníciodestecapítulo,porémadicioneaclasse TapCirculoViewdestavez(aoinvés
da CirculoViewquefoiutilizadaanteriormente).Oarquivo TapCirculoView.hé
igual:
// TapCirculoView.h
# import <UIKit / UIKit.h>
@interface TapCirculoView : UIView {
NSMutableArray *circulos;
}
@end
Aprincipalmudan çaseránaclasse TapCirculoView,ondeprecisamosregis-
traroeventodetoquedesejado,elidarcomamensagemenviadapeloiOSquando
ousuáriointeragircomoaplicativo.Aprimeirapartedocódigoestáabaixo:
1 // TapCirculoView.m
2 # import "TapCirculoView.h"
3
4 @interface TapCirculoView()
5 -(void) registraEventos;
6 @end
7
152

## Página 165

CasadoCódigo Capítulo8. Trabalhandocomreconhecedoresdegestos
8 @implementation TapCirculoView
9
10 -(id) init {
11 if ((self = [super init])) {
12 [self registraEventos];
13 }
14
15 return self;
16 }
O código das linhas 4 a 6 apenas declara a existência do método
registraEventos somente para o compilador não emitir um alerta, con-
formevimosnocapítulosobreObjective-C.Jánométodo init(queéoconstrutor
daclasse),aproveitamospararegistraroseventosdetoque,conformeabaixo:
1 // TapCirculoView.m
2 -(void) registraEventos {
3 UITapGestureRecognizer *toque = [[UITapGestureRecognizer alloc]
4 initWithTarget:self action:@selector(toqueRecebido:)];
5
6 toque.numberOfTapsRequired = 1; // Valor padrão é 1
7 [self addGestureRecognizer:toque];
8 }
Aocontráriodoexemploapresentadonoiníciodocapítulo,quesobrescreviaos
métodos touchesBegane touchesEndeddaclasse UIView,osreconhecedo-
resdegestosãoclassesindependentes,podendoinclusivesercriadasemqualquer
outraclasse.Nonossocaso,issoéfeitonométodo registraEventos.Aclasse
UITapGestureRecognizercontémapropriedade numberOfTapsRequired,
queserveparainformarquantostoquesousuáriodeveráfazerparaqueaaç ãoseja
disparada,oqueéfeitonalinha6.Nalinha7adicionamosogestonaview,paraque
oiOSpossaidentificarasaçõesnomomentoemqueforapropriado—ouseja,sem
ocódigodalinha7,nadaaconteceria.
Todosreconhecedoresdegestosseguemamesmaestruturadeconstruç ão,es-
perandoaclassequeirátrataroseventos( initWithTarget)eométodonaquela
classe( action)queseráresponsávelpelaaçãoemsi.Issoéfeitonaslinhas3e4,
ondepassamosaprópriaviewcomodelegate,ea“referência”aométodoquedeverá
serexecutado,cujaimplementaç ãoestáabaixo:
1 // TapCirculoView.m
2 -(void) toqueRecebido:(UIGestureRecognizer *) gesto {
153

## Página 166

8.4. Tremedeiracomtoquelongo CasadoCódigo
3 if (!circulos) {
4 circulos = [[NSMutableArray alloc] init];
5 }
6
7 CGPoint localizacaoToque = [gesto locationInView:self];
8 [circulos addObject:[NSValue valueWithCGPoint:localizacaoToque]];
9 [self setNeedsDisplay];
10 }
Ovalordoargumento actiondeveseguirumdosdoisformatosabaixo:
- (void) gestoRecebido;
- (void) gestoRecebido:(UIGestureRecognizer *) gesto;
Adiferen çaentreamboséqueosegundorecebecomoargumentooreconhece-
dordegesto(tap,swipe,panning etc.)queenviouamensagem,oquepodeserútil
tantoparautilizaromesmométodoparadiversoseventos,ou—ocasomaiscorri-
queiro—paraobteralgumasinformaçõesadicionaisnecessáriasparaaexecuç ãoda
lógica.
O método toqueRecebido: é o correspondente aotouchesEnded do
exemploanterior,nãohavendodiferen çassubstanciaisnalógica,tantoqueocó-
digodalinha7évirtualmenteigualàoutraimplementaç ão,porémutilizandoum
UIGestureRecognizer.
Aclasse TapCirculoViewaindaprecisadométodo drawRect:,quevocê
podecopiarintegralmentedoexemploanterior. Lembre-setambémdemudaro
método loadViewdaclasse ViewControllerparaoseguinte:
-(void) loadView {
TapCirculoView *c = [[TapCirculoView alloc] init];
c.backgroundColor = [UIColor whiteColor];
self.view = c;
}
8.4 T remedeira com toque longo
OsíconesdoiOSsãobastantemedrosos,bastandosegurá-losporalgumtempopara
quecomecematremerdesesperadamente.Parademonstrarogestodetoquelongo
(longpress)eousodemaisdeumgestonamesmaview,vamosfazerumaplicativo
quetambémfaztremerasviews,porémdandoaop çãodeacabarcomosofrimento
154

## Página 167

CasadoCódigo Capítulo8. Trabalhandocomreconhecedoresdegestos
delasrealizandoumduplotoque(doubletap). Alémdisso,esteexemplomostrará
recursosmaisavan çadosdedecoraç ãodasviews.
Crieumnovoprojetochamado“TremeTreme”comasconfiguraçõespadrão
de sempre, e já adicione uma classe chamadaTremeTremeView, que estende
de UIView. Como o código é um pouco maior que de costume, iremos ver
a implementação por partes. Todo o código a seguir é referente ao arquivo
TremeTremeView.m,nãohánenhumcódigono TremeTreme.hdestavez.
1 # import "TremeTremeView.h"
2 # import <QuartzCore / QuartzCore.h>
3
4 # define RADIANS(degrees) ((degrees * M_PI) / 180.0)
5
6 @interface TremeTremeView ()
7 -(void) registraGestos;
8 -(void) enfeitaView;
9 @end
10
11 @implementation TremeTremeView
12
13 -(id) initWithFrame:(CGRect)frame {
14 if ((self = [super initWithFrame:frame])) {
15 [self enfeitaView];
16 [self registraGestos];
17 }
18
19 return self;
20 }
Entreaslinhas1e9temosalgumasdeclaraçõesgeraisparaqueorestodaclasse
possafuncionarcorretamente,sendoqueapartenovaéalinha2,queimportao
frameworkdeanimaç ãoQuartz,ealinha4quedefineumaconstante RADIANS
paraconvertergrauspararadianos. Alémdisso,notequenalinha13estamosde-
clarandooinicializador initWithFrame:aoinvésdeapenas init,poiséomé-
todoqueseráutilizadomaisadiantenocontroladorparacriarinstânciasdestaview
jáespecificandoseutamanho. Muito importante: comoestamossobrescrevendo
initWithFrame:,nalinha14énecessáriotambémexecutaro initWithFrame:
de super,casocontráriooseuaplicativosecomportarádemaneirasestranhas.
Seguindo,temosométodo enfeitaView:
155

## Página 168

8.4. Tremedeiracomtoquelongo CasadoCódigo
1 -(void) enfeitaView {
2 self.layer.masksToBounds = NO;
3 self.layer.cornerRadius = 8;
4 self.layer.shadowOffset = CGSizeMake(-2, 2);
5 self.layer.shadowRadius = 5;
6 self.layer.shadowOpacity = 0.5;
7 }
Ocódigodestemétododependedaqueleimportdo QuartzCorefeitoanteri-
ormente,paraquepossamosacessarapropriedade layer.Nalinha3dizemosque
asbordasdaviewdevemserarredondadasem8pixels.Nalinha4éadicionadouma
pequenasombracomotamanhodocódigoexistentenalinha5,enquantoqueali-
nha6especificaem50%aopacidadedasombra.Comestasop çõesoaspectovisual
ficarámuitomaisagradávelparaousuário(experimenteremoverestemétodo,para
veradiferen çacausada).
Osgestossãocriadosnométodo registraGestos:
1 -(void) registraGestos {
2 UILongPressGestureRecognizer *toqueLongo =
3 [[UILongPressGestureRecognizer alloc] initWithTarget:self
4 action:@selector(iniciaTremedeira:)];
5 toqueLongo.minimumPressDuration = 0.3;
6 [self addGestureRecognizer:toqueLongo];
7
8 UITapGestureRecognizer *toqueParar =
9 [[UITapGestureRecognizer alloc] initWithTarget:self
10 action:@selector(pararAnimacao)];
11 toqueParar.numberOfTapsRequired = 2;
12 [self addGestureRecognizer:toqueParar];
13 }
Aprincipalnovidadeéaclasse UILongPressGestureRecognizer,utilizada
paragestosquandoousuáriotocaatelaemantémodedopressionadoporum
determinadotempoatédispararoeventodeiniciaratremedeiradaview,queno
nossocasosão300milissegundos,conformefeitonalinha4. Alémdisso,preci-
samosdeumamaneiradefazeraviewparardetremer,eparatantoéutilizadoo
UITapGestureRecognizercom2toques.Resumindo:toqueesegureodedoem
cimadaviewporpelomenos300milissegundosparafazê-lacome çaratremer,e
depoistoque2vezesrapidamenteparaparar.
Ocódigoqueiniciaatremedeiraestáabaixo:
156

## Página 169

CasadoCódigo Capítulo8. Trabalhandocomreconhecedoresdegestos
1 -(void) iniciaTremedeira:(UIGestureRecognizer *) gesto {
2 CGAffineTransform oscilaEsquerda = CGAffineTransformRotate(
3 CGAffineTransformIdentity, RADIANS(-5.0));
4
5 CGAffineTransform oscilaDireita = CGAffineTransformRotate(
6 CGAffineTransformIdentity, RADIANS(5.0));
7
8 self.transform = oscilaEsquerda;
9
10 UIViewAnimationOptions opcoes = UIViewAnimationOptionRepeat
11 | UIViewAnimationOptionAllowUserInteraction
12 | UIViewAnimationOptionAutoreverse
13 | UIViewAnimationCurveEaseInOut;
14
15 [UIView animateWithDuration:0.1 delay:0 options:opcoes animations:^{
16 self.transform = oscilaDireita;
17 } completion:nil];
18 }
Alógicaéaseguinte:queremosfazeraviewgirarrapidamente5grausparaa
esquerdae5grausparaadireita,oqueéconseguidocomousode transformaçõesdo
Core Animation.Naslinhas2e3definimosaoscilaç ãoparaaesquerda,enquanto
naslinhas5e6,aoscilaç ãoparaadireita,easaplicamosnapropriedade transform
daprópriaview,conformeaslinhas8e16. Entreaslinhas15e17criamoseini-
ciamosaanimaç ão,daseguintemaneira:cadaoscilaç ãodeverádurar100milisse-
gundos( animateWithDuration:0.1),sendoquedevecome çarimediatamente
( delay:0).Paraquetudofuncionecorretamente,passamosumasériedeop ções
dotipo UIViewAnimationOptionsquesãodeterminadasentreaslinhas10e
13. UIViewAnimationOptionRepeatinformaqueoblocodeanimaç ãodevese
repetirindefinidamente, UIViewAnimationOptionAllowUserInteraction
énecessárioparaqueoduplotoquedepararsejaidentificado,poiscasocontrá-
riooiOSiráignorarinteraçõescomaviewenquantoelaestiversendoanimada.
UIViewAnimationOptionAutoreverseespecificaque,aochegarnofinal,aani-
maçãodeveautomaticamentevoltarparaopontoinicial(queéodalinha8),en-
quantoqueaop ção UIViewAnimationCurveEaseInOutéumajustefinonama-
neiracomoaanimaç ãoocorre.
Parapararatremedeira,implementeoseguintemétodo:
1 -(void) pararAnimacao {
2 UIViewAnimationOptions opcoes =
157

## Página 170

8.4. Tremedeiracomtoquelongo CasadoCódigo
3 UIViewAnimationOptionBeginFromCurrentState;
4
5 [UIView animateWithDuration:0 delay:0 options:opcoes animations:^{
6 self.transform = CGAffineTransformIdentity;
7 }completion:nil];
8 }
A lógica deste código pode não ser muito clara a princípio, porém funci-
ona assim: cada UIView independente somente pode ter um bloco de ani-
mação sendo executado por vez, e não existe um método “parar animação”.
Portanto, o que fazemos é dispararoutraanimação que dura zero segundos (
animateWithDuration:0),queretornaaviewparaoestadonormal,conforme
alinha5. Ocódigodalinha2éimportanteparaqueatransiç ãosejafeitaapartir
doestadoemqueaviewseencontranomomento—emoutraspalavras,paraficar
maissuave.
Aúltimapartedocódigoconsistenaclasse ViewController.m,conforme
abaixo:
1 # import "ViewController.h"
2 # import "TremeTremeView.h"
3
4 @implementation ViewController
5
6 -(void) criaTremeTremeView:(CGPoint) posicao comCor:(UIColor *) cor {
7 CGRect r = CGRectMake(posicao.x, posicao.y, 60, 60);
8 TremeTremeView *t = [[TremeTremeView alloc] initWithFrame:r];
9 t.backgroundColor = cor;
10 [self.view addSubview:t];
11 }
12
13 - (void)viewDidLoad {
14 [super viewDidLoad];
15 self.view.backgroundColor = [UIColor whiteColor];
16
17 [self criaTremeTremeView:CGPointMake(50, 50)
18 comCor:[UIColor blueColor]];
19 [self criaTremeTremeView:CGPointMake(200, 150)
20 comCor:[UIColor greenColor]];
21 [self criaTremeTremeView:CGPointMake(110,250)
22 comCor:[UIColor purpleColor]];
158

## Página 171

CasadoCódigo Capítulo8. Trabalhandocomreconhecedoresdegestos
23 }
24 @end
Ométodo CriaTremeTremeView:comCor:daslinhas6a11éutilizadonas
linhas17,19e21,sendoresponsávelporcriarinstânciasda TremeTremeViewem
umlugarcentralizado—afinal,duplicarcódigonuncaébom,certo?!
Oresultadodesteaplicativoestánafigura 8.2.
Figura8.2:Viewstremendodemedo.Reparenashabilidadesvisuaisdoautor
8.5 D eslizando uma view com o gesto Swipe
Opróximoexemplodemonstraousodogesto swipe,queéummovimentoquese
assemelhaajogar(aoinvésdearrastar)algodeumadire çãoparaoutracomodedo,
comonavegarpelasimagensdeumagaleriadefotos.Oprogramaconsistememum
retânguloquepodeserjogadodeumladoparaooutro.Crieumnovoprojetocha-
mado“GestoSwipe”edeclareumavariáveldotipoUIViewchamada“quadrado”no
159

## Página 172

8.5. DeslizandoumaviewcomogestoSwipe CasadoCódigo
arquivo ViewController.h,conformeexemplificadoabaixo.Esteseráoobjeto
quemanipularemoscomogesto.
// ViewController.
# import <UIKit / UIKit.h>
@interface ViewController : UIViewController {
UIView *quadrado;
}
@end
Feito isso, precisamos implementar a lógica em si, no arquivo
ViewController.m. Como os gestos devem necessariamente estar funcio-
nandoquandooaplicativoestiverprontoparaouso,precisamosregistrá-losde
maneiraautomáticaquandoatelaforcarregada,paraquenãohajaapossibilidade
deesquecermosdefazerissomanualmenteemalgumoutromomento. Ométodo
viewDidLoaddaclasse UIViewControllerpodesersobrescritoparafazereste
trabalho,poiséexecutadoautomaticamenteumaúnicavez,duranteainicializaç ão
docontrolador.Vejaocódigoabaixo.
// ViewController.m
- (void)viewDidLoad {
[super viewDidLoad];
[self criaQuadrado];
[self registraGestos];
}
Aprimeiracoisaafazerécriaraviewqueserámanipuladaemcadagesto,re-
presentadapelavariável quadrado:
-(void) criaQuadrado {
quadrado = [[UIView alloc]
initWithFrame:CGRectMake(100, 100, 100, 100)];
quadrado.backgroundColor = [UIColor yellowColor];
[self.view addSubview:quadrado];
}
Jáométodo registraGestos,responsávelporadicionaros swipes,segue
abaixo:
160

## Página 173

CasadoCódigo Capítulo8. Trabalhandocomreconhecedoresdegestos
1 -(void) registraGestos {
2 [self adicionaGesto:UISwipeGestureRecognizerDirectionRight];
3 [self adicionaGesto:UISwipeGestureRecognizerDirectionLeft];
4 }
5
6 -(void) adicionaGesto:(UISwipeGestureRecognizerDirection) direcao {
7 UISwipeGestureRecognizer *swipe = [[UISwipeGestureRecognizer alloc]
8 initWithTarget:self action:@selector(jogaQuadrado:)];
9 swipe.direction = direcao;
10 [self.view addGestureRecognizer:swipe];
11 }
Énométodo adicionaGesto:queotrabalhodeadicionarosgestoséfeitode
fato.Notequeprecisamosfazerissoparacadadire çãodesejada,queéespecificada
napropriedade direction,nalinha9.Jáométodoquelidacomo swipeprecisa
primeiroverificarseousuáriofezomovimentodentrodaáreadoretângulo,eentão
deslocaromesmoparaaesquerdaouparaadireita:
1 -(void) jogaQuadrado:(UIGestureRecognizer *) gesto {
2 CGPoint location = [gesto locationInView:quadrado];
3
4 if ([quadrado pointInside:location withEvent:nil]) {
5 UISwipeGestureRecognizer *swipe =
6 (UISwipeGestureRecognizer *)gesto;
7
8 float novoX = swipe.direction ==
9 UISwipeGestureRecognizerDirectionLeft ? 0
10 : (self.view.frame.size.width - quadrado.frame.size.width);
11
12 [UIView animateWithDuration:0.3 delay:0
13 options:UIViewAnimationOptionCurveEaseInOut
14 animations:^ {
15 CGRect frame = quadrado.frame;
16 frame.origin.x = novoX;
17 quadrado.frame = frame;
18 } completion:nil];
19 }
20 }
Nalinha4verificamosseotoqueocorreunaáreadoquadradopropriamente
dito,ecasoissosejaverdade,definimosanovaposiç ãohorizontaldoquadradode
161

## Página 174

8.5. DeslizandoumaviewcomogestoSwipe CasadoCódigo
acordocomadire çãodo swipe,naslinhas7a9.Orestantedométodosimplesmente
animaatrocadeposiç ãoparaaposiç ãodo novoX.
Rodeoapplicationcom Command + R efaçaosmovimentosdogesto(se
forcomomouse,cliqueearrasteparasimularomesmoefeitododedo). Aview
quadradodeverádeslizarparaadire çãodeterminada.
162

## Página 175

Capítulo9
TrabalhecommapaseGPSnasua
aplicação
Esteésemdúvidaumrecursoqueapareceemmuitasaplicações,àsvezesemcon-
textostotalmentediferentesdoqueesperamos.AAPInãoécomplicadaevocêverá
quecomoconhecimentoqueobteveatéaquiéfácilatacarumanovabiblioteca.Até
aversão5doiOSosistemademapasutilizadoéodoGoogle,enquantoqueapartir
doiOS6osmapassãodaApple.
Ocódigo-fontedestecapítuloestádisponívelnapasta“MinhaLocalizacao”(lem-
brandoqueoendere çodositecomoscódigosestánaintroduç ãodolivro).
9.1 A s bibliotecas necessárias
Crieumnovoprojetocomosugestivonomede MinhaLocalizacao,utilizando
asmesmasconfiguraçõespadrãodosoutrosprojetosfeitosatéagoranolivro.
Aprimeiracoisaafazeréadicionarasbibliotecasnecessáriasparatrabalharcom

## Página 176

9.2. Adicionandoomapaàaplicação CasadoCódigo
mapas,chamadade MapKit,eadelocalizaç ão,chamada CoreLocation.Abraas
propriedadesdoprojeto,selecioneaaba BuildPhases,eexpandaase çãoLinkBinary
withLibraries,conformemostraafigura 9.1. Cliquenobotão +eadicioneoitem
MapKit.frameworke CoreLocation.framework.
Figura9.1:AdicionandoasbibliotecasMapKiteCoreLocation
9.2 A dicionando o mapa à aplicação
Adicionarmapasaosnossosaplicativoséumatarefasurpreendentementesimples,
poisoSDKdoiOSjávemcomumcomponenteprontocomvirtualmentetudooque
énecessárioparateromapafuncionando.Nãoénecessárionospreocuparmoscom
questõesderede,posicionamentodeimagens,performanceeafins,oquenosdeixa
livreparaconcentraresfor çonalógicadenegóciosprincipal.
Abraoarquivo Main.storyboardeadicioneocomponente Map View,loca-
lizadona ObjectLibrary( CTRL + Option + Command + 3,oupelomenu View
->Utilities->ShowObjectLibrary ),posicionando-odetalformaqueocupetodaa
áreavisíveldoaplicativo.Alémdissovamosprecisarmanipularomapadiretamente
pelocódigo,portantoénecessáriocriarum Outletparaele:abrao AssistantEditor
( Option + Command + ENTER),selecioneomapa,segureo CTRLearrastepara
oarquivo ViewController.h,dandoosugestivonome“mapa”.
SevocêtentarcompilaroaplicativoveráqueoXcodereclamaquenãosabe
oquesignificaotipo MKMapView-issodeve-seaofatoqueeleestálocalizado
164

## Página 177

CasadoCódigo Capítulo9. TrabalhecommapaseGPSnasuaaplicaç ão
emumarquivodecabe çalhoespecífico, MapKit/MapKit.h. Altereoarquivo
ViewController.hconformeocódigoabaixo. Reparequenalinha2importa-
mosocabe çalhocorretodo MapKit.
1 # import <UIKit / UIKit.h>
2 # import <MapKit / MapKit.h>
3
4 @interface ViewController : UIViewController
5 @property (retain, nonatomic) IBOutlet MKMapView *mapa;
6
7 @end
Rodeoaplicativoeinterajacomomapa:arraste-o,dêduplocliquepararealizar
zoom,evejaquetudofuncionamuitobem!
9.3 S imulando múltiplos toques
Diversosaplicativosfazemusodemúltiplostoquespararealizarcertasações. No
casodemapas,toqueduplocomumúnicodedo(duplocliquedomousenosimu-
lador)aumentaozoom,enquantoqueumtoquesimplescom doisdedosdiminuio
zoom. Parasimulartoquecomdoisdedosbastaseguraratecla Optionefazero
movimentode pinchin epinchout comomouse. Afigura 9.2mostraoaplicativo
rodandoeoindicadorvisualdetoquesmúltiplos.
165

## Página 178

9.4. Posicionandoomapaautomaticamentenalocalizaç ãodousuário CasadoCódigo
Figura9.2:Indicadorvisualdetoquesmúltiplos
9.4 P osicionando o mapa automaticamente na loca-
lização do usuário
Paramostraralocalizaç ãoatualdousuário,precisamosapenasdefinirapropriedade
showsUserLocationpara YES:
- (void)viewDidLoad {
[super viewDidLoad];
self.mapa.showsUserLocation = YES;
}
Rodeoaplicativonovamenteeeledeverámostrarumamensagemsolicitando
permissãoparaacessarasualocalizaç ãoatual,conformeafigura 9.3. Cliqueem
“OK”parapermitir.
166

## Página 179

CasadoCódigo Capítulo9. TrabalhecommapaseGPSnasuaaplicaç ão
Figura9.3:Aplicativosolicitandoacessoàlocalizaç ãodousuário
Parafacilitarostestes,oiOSSimulatorpermiteainser çãomanualdequalquer
latitudeelongitude,conformemostraafigura 9.4.Bastaacessaromenu Debug->
Location->CustomLocation...
Figura9.4:Inserindomanualmenteumadeterminadalatitudeelongitude
167

## Página 180

9.5. Trabalhecomozoom CasadoCódigo
9.5 T rabalhe com o zoom
Emboraoaplicativomostreanossaposiç ão,avisãodomapaestásendovistamuito
decima,eoquequeremoséapresentaraousuárioquaseaoníveldarua.Paradefinir
oníveldezooménecessárioespecificarotamanhodesejadodaáreavisível,oqualé
representadoemumsistemadecoordenadasprópriodo MapKit.Existemdiversas
maneirasemomentosemqueépossívelrealizarestaaç ão,eaqueapresentaremos
comoexemploconsisteemmodificarozoomnomomentoemqueomaparecebe
aquelepininhoazulqueapontaalocalizaç ãodousuário.
O componente Map View tem diversos eventos os quais podemos es-
cutar, e um deles diz respeito ao momento em que algum pino é adicio-
nado ao mapa — omapView:didAddAnnotationViews:, definido no
delegate MKMapViewDelegate, sendo necessário importá-lo no arquivo
ViewController.hconformeocódigoabaixo:
@interface ViewController : UIViewController<MKMapViewDelegate>
@property (weak, nonatomic) IBOutlet MKMapView *mapa;
@end
Faltainformarao mapaondeestarãoimplementadososmétodosdodelegate,
nocaso,aprópria ViewController.m:
- (void)viewDidLoad {
[super viewDidLoad];
self.mapa.showsUserLocation = YES;
// Define a própria classe ViewController como tendo os métodos
// do delegate do MapKit
self.mapa.delegate = self;
}
Eaimplementaçãodométodo mapView:didAddAnnotationViews: :
1 -(void) mapView:(MKMapView *)mapView
2 didAddAnnotationViews:(NSArray *)views {
3 MKAnnotationView *v = [views objectAtIndex:0];
4 CLLocationDistance distancia = 400;
5 MKCoordinateRegion regiao = MKCoordinateRegionMakeWithDistance(
6 [v.annotation coordinate], distancia, distancia);
7 [self.mapa setRegion:regiao animated:YES];
8 }
168

## Página 181

CasadoCódigo Capítulo9. TrabalhecommapaseGPSnasuaaplicaç ão
Aslinhas4e5definemaregiãodozoomcombasenadistânciaemmetrosde-
finidanalinha3. Rode-onovamente,eoresultadodeveráseralgocomoafigura
9.5.
Figura9.5:Mapacomzoomaplicado
9.6 A dicionando pinos ao mapa
Parafinalizaroaplicativodemapas,vamospermitirqueousuárioinsirapinosem
qualquerlugaraorealizarumtoquelongodepelomenos500milissegundos,ecen-
tralizaromapanaregiãodestepino.Aprimeiracoisaafazeréadicionaraomapa
umgestodotipo UILongPressGestureRecognizer,conformeocódigoabaixo:
- (void)viewDidLoad {
[super viewDidLoad];
self.mapa.showsUserLocation = YES;
self.mapa.delegate = self;
169

## Página 182

9.6. Adicionandopinosaomapa CasadoCódigo
// Adiciona ao mapa o gesto de toque longo
UILongPressGestureRecognizer *toqueLongoMapa =
[[UILongPressGestureRecognizer alloc] initWithTarget:self
action:@selector(adicionaPino:)];
toqueLongoMapa.minimumPressDuration = 0.5;
[self.mapa addGestureRecognizer:toqueLongoMapa];
}
Aimplementaçãodométodo adicionaPino:segueabaixo:
1 -(void) adicionaPino:(UIGestureRecognizer *) gesto {
2 if (gesto.state == UIGestureRecognizerStateBegan) {
3 CGPoint ponto = [gesto locationInView:self.view];
4
5 CLLocationCoordinate2D coordenadas =
6 [self.mapa convertPoint:ponto toCoordinateFromView:self.mapa];
7
8 MKPointAnnotation *pino = [[MKPointAnnotation alloc] init];
9 pino.coordinate = coordenadas;
10 [self.mapa addAnnotation:pino];
11 }
12 }
Averificaçãonalinha2énecessáriaparaqueopinosejaadicionadoapenas
umaúnicavez,dadoqueogestodetoquelongodisparaoeventoquandoodedoé
retiradodatelatambém. Naslinhas5e6convertemosaposiç ãodotoquenatela
paraosistemadecoordenadasdomapa. Orestodométodosimplesmentecriao
pinoeadiciona-oaomapa.
Aorealizarumtoquelongo,ométodo mapView:didAddAnnotationViews:
implementadoanteriormenteseráautomaticamenteexecutadopeloiOS,centrali-
zandoopinonatela,conformemostraafigura 9.6.
170

## Página 183

CasadoCódigo Capítulo9. TrabalhecommapaseGPSnasuaaplicaç ão
Figura9.6:Resultadodoaplicativoapósaadiç ãodediversospinos
9.7 D etecte toques nos pinos
Odelegate MKMapViewDelegatetemdiversosmétodosinteressantes, comoo
mapView:didSelectAnnotationView:,queéexecutadotodavezqueousuário
interagecomalgumpino.Vejaumexemplonocódigoabaixo,ondeapenasmostra-
mosumamensagemdelogquandoissoocorre—umusomaiscriativoficacomo
liçãodecasaparavocê!
- (void)mapView:(MKMapView *)mapView
didSelectAnnotationView:(MKAnnotationView *) pino {
NSLog(@"Pino %@ selecionado", pino);
}
171

## Página 185

Capítulo10
Componentesgráficoscustomizados
Comrarasexce ções,todososcomponentesgráficosnoiOS—botões,seletoresde
datasevalores,camposdetexto,imagens,barrasdenavegaç ãoetantosoutros—
descendemdaclasse UIView,queétambémaclassequedevemosestenderpara
criarnossospróprioscomponentesvisuaiscustomizados. Napráticaelaérelati-
vamentesimples,definindoumaárearetangularnatelaeasinterfacesparageren-
ciarconteúdonaquelaárea,taiscomodesenhoeanimaç ão,eventos,layouteoutras
views-filhas.
Nestecapítuloveremosasprincipaispropriedadeseestruturada UIView,detal
formaquesejapossívelaplicaroconhecimentonaconstruç ãodeaplicativosricose
interativos,assimcomocriarseuspróprioscomponentes.Aocontráriodorestodo
livro,aquioconteúdoéapresentadonumestilomaispróximodeguiadereferência,
inclusiveporsuasimplicidade.
Viewspodemsercriadastotalmentenamão,comcódigopuro,oucomummix
decódigoelayoutvisual,feitoemconjuntocomarquivos .xibatravésdoInter-
faceBuilder.Oresultadopráticoéidêntico,sendoquearquivosXIBsãoúteispara

## Página 186

10.1. Criandoviews CasadoCódigo
elementosestáticos-casoqueiramanipularoqueapareceequandoaparece,será
necessáriofazerviacódigoapartedinâmica.
GeralmenteamelhoralternativaécriaratelaemarquivosXIB,efazerviacódigo
oquefordinâmicoe/oucondicional.
Desenho e animação
- O conteúdo é desenhado utilizando tecnologias comoUIKit, Core
Graphicse OpenGL ES.-Certaspropriedadesdaviewpodemsermodificadas
utilizandoefeitosdeanimaç ão.Veremoscomofazerissonestecapítulo.
Gerenciamento de layout e views-filhas
-Uma UIViewpodeopcionalmenteconterdiversasoutrasviews-filhas,chama-
dasde subviews. -Cadaviewpodedefinirasregrasderedimensionamentoem
relaçãoàview-pai.-Umaview-paipodemodificarotamanhodasviews-filhas.
Gerenciamento de eventos
-Todaviewpodelidarcomeventosdetoqueeoutrostiposdeinteraç ãofeitos
pelousuário.
10.1 C riando views
Porserretangular,paracriarviewsénecessárioespecificarascoordenadasxey,além
dalarguraealtura,conformeoexemploabaixo:
1 CGRect retangulo = CGRectMake(20, 20, 200, 200);
2 UIView quadradoView = [[UIView alloc] initWithFrame:retangulo];
AAPIde UIViewutilizaonome frame(quadro,moldura)parasereferenciar
àscoordenadasedimensõesdaview.Vocêtrabalharábastantecomestapropriedade.
Paramodificaroframeénecessáriopassarum CGRectcompletonovamente,como
noexemploabaixo:
retangulo.frame = CGRectMake(50, 100, 150, 300);
Tecnicamenteo frameérepresentadoporuma structchamada CGRect,que
porsuavezcontêmoutrasduas structschamadas size(queédotipo CGSize)
174

## Página 187

CasadoCódigo Capítulo10. Componentesgráficoscustomizados
e origin(dotipo CGPoint),quecorrespondesaotamanhoeposiç ãorespectiva-
mente.Issosignificaquepara pegarotamanhoouposiç ãodequalquerview,basta
fazercomonoexemploabaixo:
float x = retangulo.frame.origin.x;
float y = retangulo.frame.origin.y;
float largura = retangulo.frame.size.width;
float altura = retangulo.frame.size.height;
Poroutrolado,para modificarapenasalgumasumadaspropriedades( x, y,
widthou height)énecessárioumpoucomaisdetrabalho,poiséprecisoprimeiro
atribuiro frame%aumavariáveltemporária,modificá-laeatribuirdevoltaao
frame.Vejaoexemploabaixo:
1 CGRect frame = retangulo.frame;
2 frame.origin.x = 350;
3 retangulo.frame = frame;
Escreverapenas retangulo.frame.origin.x = 350 nãofuncionaria,pois
comoestamoslidandocomstructsemC,eframeéumvalor(nãoumponteiro)de
UIView,tentaralterá-lodessaformanãosurtiriaefeito(alterariaacópiadoframe
emmemória),eocompiladornãopermitiria.Éumcódigobastanterepetitivo,eno
capítulosobreObjective-Cavan çadoveremosumaformadetornaressatarefamais
simples.
10.2 A nimando views
Alémdedaremumaspectomaisbonitoparaasuaaplicaç ão,animaçõessãomanei-
rasmuitoúteisdeinformaraousuárioquealgumacoisaestáacontecendo.Apró-
priaApplerecomendaqueousodesterecursosejasempreconsiderado. Diversas
propriedadesda UIViewtêmsuporteàanimaçãodemaneiraextremamentefácil,
bastandoapenasinformarquedesejamosrealizá-la,emodificarapropriedadeem
si.Asseguintespropriedadespodemseranimadasdestaforma:
•frame:paraanimartamanhoeposiç ão
•bounds:tamanhoeposiç ão
•center:animaraposiç ão
175

## Página 188

10.3. Animandodaformaproceduraletradicional CasadoCódigo
•transform:pararotacionaroufazerscale
•alpha:paraanimaramudan çadeopacidade
•contentStretch:paramodicaramaneiracomoaviewseestica
Um lugar onde animações são bastante úteis é em transição de telas ou
propriedades — sem contar, é claro, os aspectos puramente estéticos. Existem
duasmaneirasdeanimarestaspropriedades: umaprocedural,utilizandoadupla
beginAnimatione commitAnimation,eoutramais“OO”comousodeblocos.
Oresultadoéexatamenteomesmoindependentementedatécnica,contudoapartir
doiOS4amaneiramaisutilizadaéacomblocos.
10.3 A nimando da forma procedural e tradicional
Amaneiramaistradicionaldeanimarpropriedadesdoscomponentesébastantepro-
ceduralesimplesdeentendereescrever.Atécnicaconsisteem marcaroinícioda-
quiloquedesejamosanimar,edepois aplicaraanimaçãopropriamentedita.
Ocódigoabaixodemonstraisso:
1 [UIView beginAnimations:nil context:nil];
2 [UIView setAnimationDuration:2];
3
4 minhaView.frame = CGRectMake(20, 308, 280, 132);
5 minhaView.alpha = 0.3;
6
7 [UIView commitAnimations];
Nalinha1preparamosoambiente,indicandoqueocódigoquevemabaixode-
veráserexecutadoemumblocodeanimaç ão,enquantoqueonalinha7informamos
ofimdestainstruç ão—tudooquevemnomeioseráanimado.Ocódigonalinha2
especificaaduraç ãodaanimaç ão,sendoqueovalorpadrãoéemtornode300mi-
lissegundos.Jánaslinhas4e5éfeitoocódigoqueseráanimadodefato.Ocódigo
completoestánoprojetodeexemplo AnimacaoTradicionalEx1.
10.4 A nimando com o uso de blocos
BlocoséumconceitoqueapareceunoiOS4equetornamuitomaissimples(do
pontodevistadeexigirmenoscódigo)aexecuç ãodediversastarefas,incluindoade
176

## Página 189

CasadoCódigo Capítulo10. Componentesgráficoscustomizados
animaçãodeviews.Pararealizaramesmaoperaç ãodoexemploanteriorutilizando
blocos,ocódigoficariaconformeexemplificadoabaixo:
1 [UIView animateWithDuration:2 animations:^ {
2 minhaView.frame = CGRectMake(20, 308, 280, 132);
3 minhaView.alpha = 0.3;
4 }];
Apesardasintaxeumtantoestranha,ocódigoficamuitomaisenxuto.
10.5 C riando views customizadas
Viewscustomizadassãomuitoúteisquandoháanecessidadedereutilizarcódigo
decomponentesvisuais—porexemplo,seuprópriobotão,componentedeimagem
quejáapresentaumadescriç ãodafoto,menucomsuporteaeventos,desenhoe
virtualmentequalquercoisaquevocêpossaimaginar. Alémdisso,ébemsimples
fazerisso:bastaestenderaclasse UIView.Paramelhorexemplificar,vamoscriarum
componentepararealizarumhipotéticologinnaaplicaç ão,comcampodeusuário,
senhaeobotãoparavalidarosdados,conformemostradonaimagem 10.1.Ocódigo
doaplicativodeexemplofocaránapartedecriaratelacustomizada,deixandode
ladoqualquerlógicaespecíficadeautenticaç ãopropriamentedita.
177

## Página 190

10.5. Criandoviewscustomizadas CasadoCódigo
Figura10.1:Componentedeloginadicionadonoaplicativo
Crieumnovoprojetodotipo SingleViewApplication eemseguidaadicione
umanovaclassechamada“LoginView”(Command+N),selecionandoUIViewno
campo“Subclassof”.Ateladeloginpoderáserposicionadaemqualquerlugar,po-
rémaalturaelarguradeverãosersempreasmesmas.
Coloque tudo em LoginView.m
Todososfragmentosdecódigoaseguirdeverãoseradicionadosnoarquivo
LoginView.m.
Fragmentos para simplicidade e foco
CriareconfigurarcomponentesvisuaisnoiOSéumatarefabastantemonótona
erepetitiva,frequentementeacompanhadadedezenasdelinhasdecódigocujaúnica
funçãoédefinirpropriedadesdecadaumdoscomponentes.Paramanteraobjetivi-
dade,aquinolivroiremoscolocarapenasospedaçosprincipais,detalformaqueseja
178

## Página 191

CasadoCódigo Capítulo10. Componentesgráficoscustomizados
possíveldemonstraroquefaremosporémsempoluirdemaisaspáginas.Ocódigo
completovocêpodebaixarnoendere çohttp://bit.ly/ios-ViewCustomizada.
O que devemos fazer
Usandoaimagem 10.1comoreferência,ocomponente LoginViewprecisater
ofundocomsombraqueconterátodaaestrutura,umacaixacomcantosarredon-
dadosonde,dentrodela,existemdoiscomponentesdetextoparaonomedeusuário
esenha,edoiscomponentesparaousuárioinformarosrespectivosvalores. Por
último,háumbotãoazul.Todoselesprecisamserinstanciadoseconfiguradosma-
nualmente,incluindoasdimensõeselocalizaç ão.
Paracome çarvamossobrescreverométodo initparaque,aoserinstanciado,
ocomponentejáseautoconfigure,evitandoassimqueodesenvolvedortenhaquese
lembrardefazerajustesmanualmentetodavez.Confiraoseguintecódigo:
-(id) init {
if ((self = [super init])) {
[self constroiTela];
}
return self;
}
Estaparteébastantesimples,ebasicamentedelegaatarefadecriaroscompo-
nentesaométodo constroiTela,cuja primeiraparteestáabaixo:
1 -(void) constroiTela {
2 self.frame = CGRectMake(0, 0, 300, 150);
3 self.backgroundColor = [UIColor colorWithRed:210.0/255.0
4 green:210.0/255.0 blue:210.0/255.0 alpha:1];
5
6 // Restante do método
7 }
Nalinha2definimoso framedocomponente,paraquecomecenaposiç ão0
equetenha300pixelsdelargurae150dealtura. Naslinhas3e4definimosacor
defundoparacinzaclaro,porémasintaxeépeculiar:aoinvésdaclasse UIColor
permitirqueumacorsejacriadaapenascomosvaloresRGB(210paraostrêsneste
caso),énecessáriopassarocódigodacornafaixade0.0(preto)a1.0(branco),razão
pelaqualocódigoRGBédividopor255—maluquicesdaApple.
179

## Página 192

10.5. Criandoviewscustomizadas CasadoCódigo
Orestantedométodo constroiTelaconsisteemcriarcadaumdoscom-
ponentesrestantesmanualmente,definindoo framedecada,op çõesespecíficas
(comocordotextooutipodefonte)eassimpordiante—nãoháqualquerregrade
negócios.Porestemotivo,ocódigoabaixocontêmapenasalgunsfragmentospara
serviremdeguiaparavocê,enquantoqueocódigocompletopodeserbaixadono
endereçohttp://bit.ly/ios-ViewCustomizada.
// Borda
UIView *borda = [[UIView alloc]
initWithFrame:CGRectMake(10, 10, 280, 95)];
// Detalhes omitidos no livro
[self addSubview:borda];
// Labels
UILabel *usuarioLabel = [[UILabel alloc]
initWithFrame:CGRectMake(10, 15, 100, 20)];
usuarioLabel.text = @"Usuário";
[borda addSubview:usuarioLabel];
UILabel *senhaLabel = [[UILabel alloc]
initWithFrame:CGRectMake(10, 60, 100, 20)];
// Detalhes omitidos no livro
[borda addSubview:senhaLabel];
// Campos texto
UITextField *usuarioField = [[UITextField alloc]
initWithFrame:CGRectMake(110, 15, 150, 20)];
// Detalhes omitidos
[borda addSubview:usuarioField];
UITextField *senhaField = [[UITextField alloc]
initWithFrame:CGRectMake(110, 60, 150, 20)];
// Detalhes omitidos
[borda addSubview:senhaField];
// Linha horizontal divisória entre os campos
UIView *linhaFina = [[UIView alloc]
initWithFrame:CGRectMake(20, 50, 240, 1)];
linhaFina.backgroundColor = [UIColor greyColor];
[borda addSubview:linhaFina];
180

## Página 193

CasadoCódigo Capítulo10. Componentesgráficoscustomizados
// Botao
UIButton *botaoLogin = [[UIButton alloc]
initWithFrame:CGRectMake(0, 113, 180, 30)];
// Detalhes omitidos
[botaoLogin setTitle:@"Login" forState:UIControlStateNormal];
[self addSubview:botaoLogin];
Estecódigoestáresumidoapenasparaquevocêpossaterumaideiadotrabalho
envolvidonaadiçãomanualdecomponentesàtela.
10.6 U tilizar a view customiza Login View
Umavezqueaviewtenhasidocriada, bastainstanciá-lacomoqualqueroutra
classe,eadicionarcomo subviewemalgumlugar-emumcontroller.porexem-
plo.Nocasodaappdedemonstraç ão“ViewCustomizada”issoéfeitonométodo“
viewDidLoad”daclasseViewController.m,conformeoseguintecódigo:
1 - (void)viewDidLoad
2 {
3 [super viewDidLoad];
4
5 LoginView *lv = [[LoginView alloc] init];
6 CGRect lvFrame = lv.frame;
7 lvFrame.origin = CGPointMake(
8 (self.view.frame.size.width - lvFrame.size.width) / 2, 30);
9 lv.frame = lvFrame;
10
11 [self.view addSubview:lv];
12 }
Nalinha5ocomponentedeloginquecriamoséinstanciadosemqualquerdife-
rençaatudooquejávimosnolivro,enquantoqueentreaslinhas6a9posicionamos
emumlugarespecíficodatela-nocaso,y30ecentralizadonoeixohorizontal.Por
último,alinha11faza“mágica”deadicionarocomponenteàtela.
10.7 C onstruir o componente Login View utilizando
um arquivo XIB de interface
Fazernamãodáumatrabalheira,não?! Portanto,outraalternativaéutilizarum
arquivoXIBparacriaroqueforpossívelvisualmente,atravésdoInterfaceBuilder,
181

## Página 194

10.7. ConstruirocomponenteLoginViewutilizandoumarquivoXIBdeinterface CasadoCódigo
efazerviacódigoapenascoisasmuitoespecíficasoudinâmicas.
Crie uma nova classe chamada “LoginViewVisual” (CMD + N ->
Objective-C Class) que herde de “UIView” (selecione no campo “Sub-
class of”), e em seguida adicione um novo arquivo (CMD + N novamente) do
tipo“View”,localizadonaseção“UserInterface”,conformemostraaimagem10.2.
Chameoarquivode“LoginViewVisual.xib”,conformeaimagem10.3.
Figura10.2:LocalizaçãodotemplatedeXIBs
Figura10.3:NomeandooarquivoXIB
182

## Página 195

CasadoCódigo Capítulo10. Componentesgráficoscustomizados
Atenção aos nomes
Reparequetantoonomedaclasse(arquivos .he .m)quandoo
arquivodeinterface( XIB)chamam-se“LoginViewVisual”-aúnica
coisaquemudaéaextensão.Émuitoimportanteprestaraten çãoaeste
detalhe,poisdocontrárioascoisasnãofuncionarãocorretamentemais
adiante.
Figura10.4:Mesmonome,extensõesdiferentes
Agoraabraoarquivo“LoginViewVisual.xib”,econstruaateladamesma
maneiracomojáfizemostantasoutrasvezesnolivro. Otamanhodocomponente
deveser300pixelsdelargura,e150dealtura.Paraconseguirisso,certifique-seque
ocampo“Size”noAttributesInspectorestejaselecionadocomaopção“Freeform”,
conformemostraaimagem 10.5.
183

## Página 196

10.7. ConstruirocomponenteLoginViewutilizandoumarquivoXIBdeinterface CasadoCódigo
Figura10.5:Selecione‘Freeform’paraconseguiralterarotamanhonoInterfaceBuil-
der
NemtudoémágicanomundodoiOS,eparaoarquivoXIBsaberqueele
estáassociadoaalgumaclasse,devemosinformaronomedelanocampo“Cus-
tomClass”doIdentityInspector( View -> Utilities -> Show Identity
Inspector)-nocaso,“LoginViewVisual”.Vejaaimagem10.6
Figura10.6:NomedaclasseassociadaaoXIB
184

## Página 197

CasadoCódigo Capítulo10. Componentesgráficoscustomizados
Crieatelautilizandocomoreferênciaaimagem 10.7e,casonecessário,também
ocódigoanteriorquefizemosparaoarquivo“LoginView.m”.
Figura10.7:ConstruçãodatelanoInterfaceBuilder
Conecte também os Outlets
ArquivosXIB,assimcomoStoryboards,representamapenascompo-
nentesvisuais,nadamais. Paraquesejapossívelinteragircomelesvia
códigoéprecisoconectartodososoutletseactionsqueforemnecessá-
rios. Nocasodateladelogin,crieoutletsparaoscamposdelogine
senha.Oseuarquivo .hdeveráficarassim:
# import <UIKit / UIKit.h>
@interface LoginViewVisual : UIView
@property (weak, nonatomic) IBOutlet UITextField *userField;
@property (weak, nonatomic) IBOutlet UITextField *passwordField;
@end
10.8 C omo utilizar views criados com arquivos XIB
Ao contrário de componentes criados puramente com código, aqueles que te-
nham arquivos XIB associados precisam ser obtidos de uma outra maneira,
185

## Página 198

10.8. ComoutilizarviewscriadoscomarquivosXIB CasadoCódigo
através da classeNSBundle. Confira o código abaixo, referente ao arquivo
ViewController.m:
1 // ViewController.m
2 - (void)viewDidLoad
3 {
4 [super viewDidLoad];
5
6 LoginViewVisual *lv = [[NSBundle mainBundle]
7 loadNibNamed:@"LoginViewVisual" owner:self options:nil][0];
8
9 CGRect lvFrame = lv.frame;
10 lvFrame.origin = CGPointMake(
11 (self.view.frame.size.width - lvFrame.size.width) / 2, 30);
12 lv.frame = lvFrame;
13
14 [self.view addSubview:lv];
15 }
Adiferen çaestánaslinhas6e7onde,aoinvésdeinstanciaraclasseutilizando
adobradinha“alloc/init”,obtemosatravésdométodoloadNibNamed,daclasse
NSBundle.Orestodocódigoéigualaoexemploanterior.Rodeoexemploevejao
resultado.
Não está idêntico?
Vocêdeveterreparadoqueatelanãoéexatamenteigualàanterior-emespecial,
asbordasnãoestãoarredondadaseobotãonãotemocontornopreto.Essesdeta-
lhessomentepodemserfeitosviacódigo,enãopeloInterfaceBuilder. Ficaaqui,
portanto,estedesafio:utilizandoosconhecimentosadquiridosatéagora,faç aore-
sultadovisualdocomponente“LoginViewVisual”seridênticoàqueleobtidocom
“LoginView”.
186

## Página 199

Capítulo11
Conceitosfundamentaisde
Objective-C
Objective-Cé,nofundo,C,masC comesteroides.Maisprecisamente,Objective-C
adicionaumconjuntodeextensõesàlinguagemC,comoorientaç ãoaobjetos. A
sintaxeéparticularmentediferente,mastudooquefuncionaemCiráfuncionar
emObjective-C,inclusivebibliotecasdeterceirosquenemsabemdaexistênciada
“nova”linguagem.ÉtambémaprincipalformadecriaraplicativosparaMacOSX
eiOS,tendosidofeitapelaAppleem1983.
Aquivocêpoderevisaralgunsconceitos,jáqueoenfoquedolivrofoibastante
prático.
11.1 U ma pequena história
Dependendodecomovocêencararoaprendizado,Objective-Cpodeserfácileagra-
dável,ouextremamenteirritanteefrustrante.Fácileagradáveléumaop çãomelhor,

## Página 200

11.2. Nomeeassinaturadométodo CasadoCódigo
maseisumapequenahistória:quandoeutivequeaprenderObjective-Cparapoder
desenvolveraplicativosparaiOS,eununcatinhavistoalinguagemnafrente,com
exceçãodealgumaslidasrápidasemartigosonline.Apressãoparacome çaracriar
aplicativoseraimensa,precisávamosmostraraomercadoquetínhamosumpro-
dutoparaatenderasdemandas.Issofoilogoapósolan çamentomundialdoiPad,
eatéentãoencontrardesenvolvedoresqualificados—ouaomenosinteressados—
emObjective-CedesenvolvimentoparaiOSnoBrasileraalgoextremamentedifícil.
Portanto,durante6diasseguidos,das9damanhãàs01damanhãdodiaseguinte,
minhaúnicatarefaduranteodiatodoeraestudar,tentandoassimilaraavalanchede
informação.
Estaimersãodechoqueacabouditandoodesenrolardaspróximassemanas.
Olhandoparatrás,umdosmaioreserrosquefizfoitercriadoexpectativaserra-
dassobrecomoObjective-Cdeveriafuncionar,especialmenteemrelaç ãoàsintaxe.
EuqueriaqueasintaxefossecomoJava,C#,C,Javascript,qualquercoisaassim,e
demoreiparaaceitarquedeveriaencararalinguagemcomodiferente. Muitosar-
tigoselivrosdescrevemObjective-Ccomosendoumalinguagemfácildelerede
aprender(etalvezporissoeutenhatidoexpectativasirrealistas),masnapráticanão
éexatamenteassim.
Portanto,omeuconselhodeouroparaquemestiveraprendendoObjective-C:
aceitealinguagemdojeitoqueelaé,etenteescreverocódigodamaneiramaisorga-
nizadaquepuder.Asintaxeéestranhaemuitasvezestemosquedarmaisvoltasque
orazoável.Masétambémumalinguagempoderosa,que,quandocompreendidasua
maneiradefuncionar,torna-seagradáveldetrabalhar.Procuremaneiraseficientes
eprodutivasdeutilizá-la,masnãoserevoltecontraela.
11.2 N ome e assinatura do método
Estesdoistermossãofáceisdeconfundire,grandepartedotempo,écomumosde-
senvolvedoresreferenciarem-seaelescomosendoamesmacoisa,porémexisteuma
diferençafundamental:o nomedométodoécompostopelassuaspartessemquais-
querreferênciasaostiposdosdados,enquantoaassinaturacompreendeoconjunto
completo.Exemplo:
Assinatura: -(void) criaEmpresaComNome:(NSString *) nome
eNumeroFuncionarios:(int) quantidade
Nome: criaEmpresaComNome:eNumeroFuncionarios:
MétodosemObjective-Csãoumdosprincipaispontosdeconfusãoereclamaç ão
188

## Página 201

CasadoCódigo Capítulo11. ConceitosfundamentaisdeObjective-C
pormuitosusuários,principalmentenosprimeiroscontatoscomalinguagem.Eles
sãofeios,verbososeparecemrepetirpartes,masdepoisquepegamosojeitoéaté
possívelverumacertaelegância.Asinten çõesexpressasnocódigoacabamficando
maisclaras,evitandoidasfrequentesàdocumentaç ãoapenasparasaberaquese
referecadaumdosargumentos.
Procurecriarmétodossemanticamentebons,queexpressemdemaneiraclaraa
intençãoequesejamautodescritivos.Muitasvezesissoiráresultaremnomesmais
longos,masessaéumapráticacomum,feitaportodasbibliotecas. Éimportante
utilizaraconven çãojáexistentenoecossistemaObjective-C.
Alémdisso,emboratenhamosusadoapalavra métodoemtodoolivro,otermo
corretoemObjective-Cé“mensagem”(message),poisaimplementaçãodeOrienta-
çãoaObjetosdalinguagemébaseadanoconceitode“enviodemensagens”.Desta
forma,nósnão“invocamosummétodo”,massim“enviamosumamensagem”aum
determinadoobjeto. Esteéumconceitoimportante,eemboranamaiorpartedo
temponãofaç adiferen çacomoestemecanismofunciona,éimportanteentender,
mesmoquesuperficialmente,oqueocorreportrásdospanos.
Diferentedemuitasoutraslinguagens,emObjective-Co destino(“target”)da
mensagemédecididoemtempodeexecuç ão,comoobjetointerpretandoamensa-
gemenviada.Aprincipalconsequênciadissoéqueestesistemadeenviodemensa-
gensnãofazverificaçãodetipos,enapráticapodemosenviarqualquer mensagem
aqualquer destino(ou,emoutraspalavras,podemosinvocarqualquermétodoem
qualquerobjeto). Contudo,issonãosignificaqueiráfuncionar,poiscasoumob-
jetorecebaumamensagemdaqualnãotemconhecimento,umerroemtempode
execuçãoserágerado,muitoprovavelmentefazendooaplicativoquebrar. Essaca-
racterísticanãodeveserencaradacomonegativa,muitopelocontrário,poiséum
dospilaresquetornaalinguagemdinâmicaepermitedesenvolverdeformasque
nãosãopossíveisemoutraslinguagens.
Contudo,durantetodoolivrousamosaexpressão“método”e“invocar”(como
em“... invocarométodocriaUsuario”),aoinvésdostermossemanticamente
corretossegundoaespecificaç ãodalinguagem.Elessãomaisamigáveisaopúblico
alvo,eacabaminvariavelmentesendoutilizadospelamaioriadosblogselivros.
11.3 P ropriedades
Umdosprincípiosdeprogramaç ãoOrientadadaObjetoséoencapsulamento,em
queosatributosdeumaclassenuncasãoacessadosdiretamente,massimatravésde
189

## Página 202

11.3. Propriedades CasadoCódigo
métodos.Muitasvezessurgemmétodosdeacessoemodificaç ão—popularmente
conhecidoscomo gettersesetters—,oquepermitecontrolesobreogerenciamento
deestadodosdados,alémdeexporapenasoquerealmenteénecessário.
IssoéfacilitadoemObjective-Ccomousode propriedades.Propriedadespro-
vêmumasintaxesimpleselimpaparamétodosdeacesso,alémdetornarfácila
definiçãodasregrasdegerenciamentodememóriaecontroledeconcorrênciamúl-
tipla.
Adeclaraçãodepropriedadeséfeitajuntamentecomosdemaismétodosda
classe,protocolooucategoria(estesdoisúltimossãoabordadosmaisadianteneste
capítulo),etemumasintaxeprópria.Considereoexemploabaixo,retiradodaclasse
Empresaquejáusamosnestelivro:
@property (nonatomic, retain) NSString *nome;
Adiretiva @propertydeclaraapropriedade,enquantoqueosvaloresentre
parêntese—(nonatomic, retain) —sãoopcionais(porémgeralmenteutiliza-
dos)eprovêmdetalhesadicionaissobreocomportamentodapropriedade.Utilizar
umapropriedadeéequivalenteadeclararosmétodosdeacessomanualmente.Dessa
forma,ocódigoficaassim:
@property NSString *nome;
éequivalenteaocódigo:
-(NSString *) nome;
-(void) setNome:(NSString *) novoNome;
Aparteentreparêntesesnadeclaraç ãodapropriedadepodeterosseguintesva-
lores,quepodemsercombinadoscomvírgula:
Acesso readwriteinformaqueapropriedadepodeserutilizadatantopara
leitura(getter)quantoparaescrita(setter).Esteéovalorpadrão.
readonlymarcaapropriedadecomosendoapenasparaleitura,ouseja,não
serápossívelatribuirvalores.
Atribuição assigninformaqueumaatribuiç ãosimplesseráfeita.Seutilizado
emobjetos,estaop çãoimplicaque,casoovalororiginalsejaliberadodamemória,a
propriedadepassaráareferenciar“lixo”.Estaopçãodevenecessariamenteserusada
casoapropriedadesejaumtipoprimitivo(como inte float)ouderivadode
alguma struct,como CGRect.
190

## Página 203

CasadoCódigo Capítulo11. ConceitosfundamentaisdeObjective-C
retaindeterminaqueumamensagem retainsejaenviadaaoobjetonahora
deatribuirovalor. Dessemodo,oobjetopassaaparticipardogerenciamentode
memória.Casoapropriedadetenhaalgumoutrovalornahoradaatribuiç ão,uma
mensagem releaseseráenviadaaele.Essefuncionamentoéespecialmenteútil,
poisevitaquetenhamdelidarcomessasquestõesexplicitamente.
copyéumatributodeusomaisrestrito,noqualaatribuiç ãoéfeitaatravésdo
enviodamensagem copy,sendoaindaválidoapenasparatiposqueimplemen-
temoprotocolo NSCopying.Ovaloranteriordapropriedaderecebeamensagem
releaseantesdonovovalorseratribuído.
Acesso concorrente Porpadrão,todoacessoàpropriedadeéfeitodemaneira
atômica,comprote çãodeacessoconcorrente.Napráticaissosignificaqueapenas
umathreadporvezteráacessoaela.Casooseuprogramanãotenhaessanecessidade
(oqueé99%doscasos),utilizeoatributo nonatomic.
Umacoisaboaparanóséquecompropriedadesnãoprecisamosnecessaria-
mentedeclararvariáveisdeinstância. Contudo,vocêpodeestarseperguntando:
“massendoassim,propriedadesnãoacabamsendoexatamenteamesmacoisaqueva-
riáveisdeinstânciapúblicas?”. Estaéumaobservaçãobastanteinteressante,epara
entenderoporquêdenãoseramesmacoisa,vejaosexemplosaseguir.
11.4 A cesso somente leitura
Oacessoàspropriedadespodeserconfiguradoparanãopermitirmudan çasnovalor,
pelomenosnãoparaqualquercódigoquenãosejaodaprópriaclasse:
1 // Empresa.h
2 @interface Teste : NSObject
3 @property (nonatomic, readonly) double lucroAnual;
4 @end
5
6 // Empresa.m
7 @implementation Empresa
8
9 -(id) init {
10 if ((self = [super init])) {
11 // Repare no uso de underline ("_")
12 _lucroAnual = 100;
13 }
14
191

## Página 204

11.4. Acessosomenteleitura CasadoCódigo
15 return self;
16 }
17
18 -(void) calculaLucroAnual {
19 // Internamente podemos modificar a variável
20 // sem qualquer tipo de restrição
21 _lucroAnual = 3500;
22 }
23 @end
24
25 // OutraClasse.m
26 Empresa *e = [[Empresa alloc] init];
27
28 // OK, estamos lendo apenas. Imprime "100"
29 NSLog(@"Lucro atual: %f", e.lucroAnual);
30
31 // Erro, "lucroAnual" é "readonly"
32 e.lucroAnual = 700;
33
34 [e calculaLucroAnual];
35
36 // Imprime "3500"
37 NSLog(@"Lucro recalculado: %f", e.lucroAnual);
Reparequenaslinhas12e21foiutilizadoumunderline(“_”)comoprefixoda
propriedade lucroAnual. Issoépossíveldevidoaumafuncionalidadedocom-
piladorchamada“Propriedadesautomáticas”(doinglês“AutoProperties”),oneele
automaticamente“declara”avariávelcomunderlineparapoderserutilizadadentro
daclasseondefoidefinida.Vocêpodeaindautilizar“ self.lucroAnual”nasli-
nhas12e21,porémnaslinhas29,32e37nãopodeusaroprefixocomunderline,pois
aqueleéumcódigoexternoaclasse“Empresa”,ondeapropertyfoideclarada.
Código customizado para o getter ou setter
Casohajanecessidade, vocêpodesobrescreveraimplementaç ãodométodo
getter ou setter (ou ambos). Imagine que umChuveiro tenha limites de
temperaturaquenãopossamserultrapassados:
// Chuveiro.h
@interface Chuveiro : NSObject
@property (nonatomic, assign) int temperatura;
192

## Página 205

CasadoCódigo Capítulo11. ConceitosfundamentaisdeObjective-C
@end
// Chuveiro.m
@synthesize temperatura;
-(void) setTemperatura:(int) valor {
// Evita que o chuveiro congele ou queime a pessoa
if (valor < 10 || valor > 30) {
@throw [NSException exceptionWithName:@"Argumento inválido"
reason:@"A temperatura deve ser entre 10 e 30 graus"
userInfo:nil];
}
// Repare no underline
_temperatura = valor;
}
Aregradenomenclaturaé setNomeDaPropriedade,tomandoocuidadode
queoprimeirocaracteredonomedapropriedadenestecasotemqueseremcaixa
alta. Fazendodessaforma,oObjective-Csabequedeveráutilizaroseumétodo
setPosicao:.
11.5 U tilizando propriedades dentro da própria
classe
Emborapossaparecercontraintuitivo,existeumadiferen çasingular—masimpor-
tante—namaneiracomoacessamospropriedades dentro:daclasseondeforamde-
finidas,atravésdapalavra-chave self:
1 // Chuveiro.h
2 @interface Teste : NSObject
3 @property (nonatomic, assign) int temperatura;
4
5 -(void) acessaViaPropriedade;
6 -(void) acessaDireto;
7
8 @end
9
10 // Chuveiro.m
193

## Página 206

11.5. Utilizandopropriedadesdentrodaprópriaclasse CasadoCódigo
11 @implementation Teste
12
13 -(void) acessaViaPropriedade {
14 self.temperatura = 15;
15 }
16
17 -(void) acessaDireto {
18 _temperatura = 99;
19 }
20
21 -(void) setTemperatura:(int) novaTemperatura {
22 NSLog(@"Mudando a temperatura de %d para %d", _temperatura,
23 novaTemperatura);
24 _temperatura = novaTemperatura;
25 }
26 @end
Nalinha14estamosacessandoapropriedadedefato,atravésde self. Desta
forma,todasasregrasdefinidasnadeclaraç ãodapropriedadenalinha3sãoaplica-
das—porexemplo,setivéssemosdefinido-acomo readonly,nãoseriapossível
fazer self.temperatura = 15.Nalinha21sobrescrevemosométodosetterda
propriedadeparaadicionarlogs. Nalinha18nãousamos self,oquenaprática
acabafuncionandocomose _temperaturanestecasofosseumavariáveldeins-
tânciacomoqualqueroutra.Repareque,comomencionadoanteriormente,ocom-
piladorautomaticamentecriavariáveiscomonomedapropriedadeprefixadascom
underline,quepodemseracessadasdentrodaclasseondeforamdeclaradas.
// OutraClasse.m
Chuveiro *c = [[Chuveiro alloc] init];
[c acessaViaPropriedade];
[c acessaDireto];
NSLog(@"Temperatura atual: %d", c.temperatura);
Oresultadodesteprogramaé:
Mudando a temperatura de 0 para 15
Temperatura atual: 99
194

## Página 207

CasadoCódigo Capítulo11. ConceitosfundamentaisdeObjective-C
11.6 D efinindo protocolos
ProtocolossãoparaObjective-CoqueinterfacessãoparaJavaeC#:elesdeterminam
umcontratoqueasclassesquefizeremusodelesseguem. Protocolospermitema
definiçãodemétodosopcionais,aocontráriodeJavaeC#,onde todososmétodos
devemserimplementados. Issosignificaque,naprática,umProtocolorepresenta
umcontratoquepodetercláusulasopcionais,eportantoénecessáriotomaralgumas
precauçõesnahoradelidarcomeles.Chamamosestetipode protocolosinformais,
emcontrasteaos protocolosformais,quesãoaquelesdeimplementaç ãoobrigatória.
Protocolos também permitem aplicar o conceito de herança múltipla em
Objective-C,poisépossívelqueumamesmaclasseatendaadiversosprotocolosde
umaúnicavez,enquantoquesópodeherdardeumaúnicaclasse.
Protocolosinformais contêmumalistademétodosqueasclassespodemoptar
ounãoporimplementá-los,oqueébastanteútilparaaimplementaç ãode delega-
tes(delegadores,quesãodemonstradosmaisadiantenestecapítulo).Porexemplo,
imagineumcomponentederolagemdeconteúdo(scroll),quetemeventosparacada
mudançanaposiç ãodoconteúdo,níveldezoomeestadodaanimaç ãoderolagem.
Comautilizaç ãodeumprotocoloinformal,diferentesclassespodemlidarapenas
comoseventosquelheinteressam,semprecisarsepreocuparemproverimplemen-
taçõesvaziasdosoutrosmétodos.
Emcontrapartida, protocolosformaisdefinemumconjuntodemétodosquede-
vemobrigatoriamenteserimplementados,oqueéverificadopelocompilador.Um
exemplodeusodestetipodeprotocoloéumaclasseresponsávelporrealizardown-
loaddearquivos,quedeterminaqueummétodo downloadFinalizadosejaobri-
gatoriamenteimplementado,casocontrárionãoseriapossíveldisponibilizaràsclas-
sesoarquivobaixado.
Nãoexisteumaregrasobrequandoutilizarprotocolosformaisouinformais,
sendopossívelinclusivecombiná-losemumúnicoprotocolomisto.
Vocêpodetentardefiniroprotocoloemumarquivodecabe çalho(extensão .h)
próprio,comoemconjuntocomadefiniç ãodeumaclasse.Nocasodeutilizarum
arquivodecabe çalhopróprio,nãoénecessárioacriaç ãodoarquivo .m—afinal,o
protocolodefineapenasocontrato.
Asintaxeéaseguinte:
@protocol EventosDeDownload <NSObject>
-(void) downloadFinalizado:(NSData *) conteudo;
-(void) downloadErro:(NSError *) erro;
@end
195

## Página 208

11.6. Definindoprotocolos CasadoCódigo
Porpadrãotodososmétodosdeumprotocolosãodeimplementaç ãoobrigató-
ria.Casovocêqueiraquealguns(outodos)sejamopcionais,utilizeapalavra-chave
@optional:
// Arquivo "EventosDeDownload.h"
@protocol EventosDeDownload <NSObject>
-(void) downloadFinalizado:(NSData *) conteudo;
// Todos os métodos definidos daqui para baixo serão opcionais
@optional
-(void) downloadErro:(NSError *) erro;
@end
Sevocêquiserserexplícito,podeutilizarapalavra-chave @requiredparamar-
carosmétodosquedevemserobrigatoriamenteimplementados.Paraimplementar
umprotocolo,asintaxeéaseguinte:
# import "EventosDeDownload.h"
@interface AlgumaClasse : NSObject<EventosDeDownload>
@end
Para implementar diversos protocolos, basta separá-los por vírgula:
@NSObject<EventosDeDownload, OutroProtocolo>. Agora é só im-
plementar os métodos na classe respeitando a assinatura do método conforme
definidonadeclaraçãodoprotocolo:
// Arquivo AlgumaClasse.m
@implementation AlgumaClasse
-(void) downloadFinalizado:(NSData *) conteudo {
}
-(void) downloadErro:(NSError *) erro {
}
@end
196

## Página 209

CasadoCódigo Capítulo11. ConceitosfundamentaisdeObjective-C
Uma nota sobre <NSObject>
Nadeclaraçãodoprotocolo EventosDeDownloadfoiadicionadaa
instrução <NSObject>,oqueliteralmentesignificaqueoprotocoloem
questãoimplementaoprotocolo NSObject(nãoconfundircoma classe
NSObject).Emboraissonãosejaobrigatório,éumapráticasemprede-
clarardestaforma,poispermiteautilizaç ãodemétodoscomo retain
e release,assimcomooutrosmétodosdefinidosem NSObject.
11.7 T rabalhando com categorias
UmadasfuncionalidadesmaispoderosaseúteisdoObjective-Csãoas Categorias,
quepermitemestenderasfuncionalidadesde qualquerclasse,assimcomosubstituir
métodosjáexistentes.Categoriasgeralmentesãocriadasemseusprópriosarquivos,
emborasejapossíveladicionarváriasemummesmoarquivo-fonte,poisocompi-
ladordoObjective-Cnãoimpõeregrasdestalinha(aocontráriodeJava).Alémde
poderadicionaresubstituirmétodosdequalquerclasse,estafuncionalidadedalin-
guagempodeatuartambémcomoumamaneiradeorganizaroprojeto,distribuindo
aimplementaçãodaclassesemarquivosdistintos,agrupadosporresponsabilidade
—aocontráriodecolocartudoemumúnicoarquivogigantesco.Elastambémsão
úteisparadeclararmétodosprivadosemalgumaclassesua.
Qualquerquesejaoseumotivo,Categoriassãoextremamentepoderosasesim-
plesdeutilizar,edopontodevistadoprograma,elasfuncionamcomoseperten-
cessemàclasseoriginal,podendoinclusiveacessarqualquerpropriedadeemétodo,
inclusiveosprivados.Épossíveladicionarmétodostantoparaassuasprópriasclas-
ses,quantoparaasclassesdaprópriaAPIoficialdalinguagem,enãoénecessário
terocódigo-fontedaclasse. Porviaderegra,nãoépossíveladicionarvariáveisà
classe,apenasmétodos—contudo,existemalgumatécnicasquepermitemsimular
ocomportamentodevariáveisdeinstância,oqueéigualmenteútil.
C#eVisualBasic.NETtêmumrecursosimilarchamado ExtensionMethods,em-
boranãopermitamoacessoamembrosprivados.JáacomunidadeRubysereferea
istocomoMonkeyPatching(quenaverdadeéumadefiniç ãodoconceito,nãosendo
exclusivodeRuby).
Comoprimeiroexemplo,vamosadicionarummétodonaclasse NSStringpara
inverteroconteúdodastring:
197

## Página 210

11.7. Trabalhandocomcategorias CasadoCódigo
1 // Arquivo NSString+Customizacoes.h
2 @interface NSString (Customizacoes)
3 -(NSString *) inverter;
4 @end
Nãoexisteumaregraparaonomedosarquivos, porémumpadrãocomu-
menteutilizadoé <NomeDaClasse>+<NomeDaCategoria>.extensão,quenonosso
casovirou NSString+Customizacoes.h. Nalinha2,reparequedeclaramosa
@interfacecomomesmonomedaclasse NSString,porémcomumadiferen ça
muitoimportante:aadiç ãode (Customizacoes),queéamaneiracomoascate-
goriassãodeclaradasemObjective-C.Vocêpodeutilizarqualquerstringdentrodos
colchetes,desdequeuseomesmovalornoarquivodeimplementaç ão,conformeo
códigoabaixo:
// Arquivo NSString+Customizacoes.m
@implementation NSString (Customizacoes)
-(NSString *) inverter {
char tmp[self.length + 1];
for (int i = self.length - 1; i >= 0; i--) {
char c = [self characterAtIndex:i];
tmp[self.length - i - 1] = c;
}
tmp[self.length] = '\0';
return [NSString stringWithUTF8String:tmp];
}
@end
O código da listagem acima é autoexplicativo, apenas atente ao deta-
lhe que a declaração da @implementation contém o nome da categoria (
(Customizacoes))exatamentedamesmaformacomofoideclaradanoarquivo
.h.Ométodo inverteragoraestáacessíveldiretamentenaclasse NSString:
NSString *s = @"uma palavra";
NSLog(@"%@", [s inverter]); // Resultado: "arvalap amu"
Categoriastambémsãomuitoúteisparatornarmaisfáceiscódigosrepetitivos.
Umbomexemplodissoéamanipulaç ãodaspropriedadesdetamanhoeposiç ão
198

## Página 211

CasadoCódigo Capítulo11. ConceitosfundamentaisdeObjective-C
deuma UIView. Considereporuminstanteocódigoabaixo,quenãofazusode
categorias:
1 // Obtêm a posição atual da view
2 float x = self.view.frame.origin.x;
3
4 // Diminui pela metade a posição
5 CGRect frame = self.view.frame;
6 frame.origin.x = x / 2;
7 self.view.frame = frame;
Emboraocódigodalinha2nãosejacomplicado,eocupeapenasumalinhade
código,aindaassimébastantechatoterquepassarpordiversaspropriedadesaté
obteraposiç ão“x”daview.Jáocódigodaslinhas5a7jáémuitomaisentendiante,
etê-loquerepetirdiversasvezesduranteociclodoprogramaéalgofrustrante.Com
categoriaspodemossimplificarbastanteoprocesso:
// Arquivo UIView+AdicoesFrame.h
@interface UIView (AdicoesFrame)
-(void) setX:(float) newX;
// Em Objective-C evita-se o padrão "getX" de outras linguagens
-(float) x;
@end
// Arquivo UIView+AdicoesFrame.m
@implementation UIView (AdicoesFrame)
-(void) setX:(float) novoX {
CGRect frame = self.frame;
frame.origin.x = novoX;
self.frame = frame;
}
-(float) x {
return self.frame.origin.x;
}
@end
199

## Página 212

11.8. Gerenciamentodememória CasadoCódigo
Tendofeitoestecódigo,amanipulaç ãodaviewficamuitomaissimples:
UIView *v = [[UIView alloc] init];
v.x = 45;
float posicaoX = v.x;
Vocêpodeestenderamesmaabordagemparaoutraspropriedades,como y,
widthe height.
11.8 G erenciamento de memória
Todoaplicativo,independentementedalinguagememquefoidesenvolvidoedapla-
taformaqueroda,precisalidarcomgerenciamentodememória—oquemuda,po-
rém,équeméresponsávelporestatarefa.EmJavaeC# issovem“degraça”naforma
deumcoletordelixoautomático,assimcomoRuby.Poroutrolado,C,C++deixam
estatarefaparaoprópriodesenvolvedor.JácomObjective-Carespostaé“depende”,
poisexistemdoisconceitos:gerenciamentomanual,egerenciamentoautomático.
TodaaplicaçãoqueforcriadaapartirdoXcode5automaticamenteteráhabili-
tadaporpadrãoosuporteagerenciamentoautomáticodememória,dotermo ARC
-“AutomaticReferenceCounting”(algocomo“contadorautomáticodereferências”).
FazerusodeARCéamaneirarecomendadadeconstruiraplicaçõesmodernas,ha-
vendoraríssimosmotivosparanãoutilizá-lo. Nãoénecessárionenhumaconfigu-
raçãoespecialnoseuprojeto,opróprioXcodejápreparaoambientecomsuportea
ARC.
Objective-Cem iOS versus Mac versus contador de re-
ferências
EmMacexisteoconceitodecoletordelixo(doinglês“garbagecol-
lector”),porémissoaindanãoérealidadeemiOS.ComosuporteaARC
noiOS,ocompiladorseencarregadecolocaraschamadasaosmétodos
deliberaçãodememórianosdevidoslugares.Emboranãochegueaser
umcoletordelixopropriamentedito,éumagrandemãonaroda.Para
utilizaresserecursoénecessáriorealizaralgumasconfiguraçõesespeci-
aisnoprojeto,alémdetomaralgunscuidadosnahoradedesenvolver.
200

## Página 213

CasadoCódigo Capítulo11. ConceitosfundamentaisdeObjective-C
Apesardeparecerassustador,arealidadeémuitomaistranquila,bastandoseguir
algumasreceitasdebolobastantesimplesparaquetudofuncioneemharmonia.
Contando referências
Objective-Ctrabalhacomoconceitodecontadordereferências,emque,aoins-
tanciaroobjetoetodavezquealguémoretém,umcontadorinternoéincrementado.
Equandoumamensagemparaquesejaliberadoéexecutada,ocontadorédecre-
mentado.Quandoelechegaremzero,amemóriaéliberada.Afigura 11.1exemplifica
esteconceito.
Figura11.1:Exemplificaçãodocontadordereferências.Fonte:Apple
Como ARC é a maneira recomendada e padrão de criar projetos modernos
para iOS, isso é tudo o que você precisa saber sobre gerenciamento de memó-
ria.Confienocompiladoreelefarátodootrabalhopesadoparavocê.Casoesteja
curioso,aimagem 11.2mostraondehabilitaroudesabilitarosuporteaARC.
201

## Página 214

11.9. Gerenciamentomanualdememória(paraoscuriosos) CasadoCódigo
Figura11.2:Chavedeconfiguraç ãoparaARC-‘Yes’éopadrão
11.9 G erenciamento manual de memória (para os cu-
riosos)
EmboravocêsempredevadesenvolvedorseusprojetosutilizandoARC(queéopa-
drão),estase çãoirádescrevercomofuncionaogerenciamentomanualdememória
emObjective-C,tantoporrazõeshistóricasquantoparavocêcompreendermelhor
oquesepassanosbastidores.
Caso queira, pode pular para a próxima se ção sem medo.Napráticasãobem
remotasaschancesdevocêterquemanualmentefazerogerenciamentodememória.
Decidiucontinuaraler?Entãovamoslá.Tudoseresumeatrêsregrasbastante
simpleseumpoucodeaten çãododesenvolver,nadamais.E,sealgodererrado,o
máximoqueaconteceráéoseuaplicativoquebrarimediatamente,ouvazarmemória
atéqueeventualmentequebre.
Asregrassão:
• Sevocêéodono,libere;
• Sevocênãoéodono,nãolibere;
• Sobrescrevaométododeallocemsuasclasses,paraliberarasvariáveisque
possuir.
Primeira regra: quando você é o dono
Vocêéconsiderado“dono”dealgumobjetoquandoutilizaexplicitamenteos
métodos alloc, copy, newou retain.Exemplo:
1 NSArray *dados = [[NSarray alloc] init];
2
202

## Página 215

CasadoCódigo Capítulo11. ConceitosfundamentaisdeObjective-C
3 // Trabalha com o NSArray
4
5 // Regra: somos donos, então liberamos
6 [dados release];
Nalinha1utilizamos alloc,portandoprecisamosliberaranossaparte,através
dométodo releasenalinha3.Arespeitode retain,vejaaregra3.
Segunda regra: Se você não é o dono, não libere
Bastaseguiralógicainversadaprimeiraregra.Sevocêtemoucriaalgo,masnão
usou alloc, new, copyou retain,deixeparalá.Porexemplo:
1 NSMutableDictionary *config = [NSMutableDictionary dictionary];
2 [config setObject:@"true" forKey:@"acesso.seguro"];
3 [config setObject:@"superSenha2000" forKey:@"senha.db"]
4
5 // Não é necessário fazer nada para liberar
Quandoconstruímoso NSMutableDictionarynalinha1dalistagemante-
rior,nãoexistenadade allocnemnenhumdeseusparentes,portandonãoprecisa-
mosnospreocuparemliberaramemóriamanualmente—magianegra(oualguma
coisaassim)resolveoproblema.
T erceira regra: Libere memória no métododealloc
Enquantoqueemvariáveislocaisamemóriatambémdeveserliberadanoes-
copodoblocodecódigo,emvariáveisdeinstânciaenasmarcadascom @property
aliberaçãodeveocorrernummétodoespecialchamado dealloc,oqualvocê
devesobrescrever. Parasimplificaraexplicaç ão,considereumahipotéticaclasse
CarrinhoCompras,aqualpertenceaum Clienteepodeconterdiversos itens:
1 // CarrinhoCompras.h
2 @interface CarrinhoCompras : NSObject {
3 NSMutableDictionary *cache; // Algum cache para operacoes internas
4 }
5
6 @property (nonatomic, retain) Cliente *cliente;
7 @property (nonatomic, readonly) NSMutableArray *itens;
8 @property (nonatomic, assign) BOOL estaPago;
9
203

## Página 216

11.9. Gerenciamentomanualdememória(paraoscuriosos) CasadoCódigo
10 @end
11
12 // CarrinhoCompras.m
13 @implementation CarrinhoCompras
14
15 -(id) init {
16 if ((self = [super init])) {
17 _itens = [[NSMutableArray array] retain];
18 cache = [[NSMutableDictionary alloc] init];
19 }
20
21 return self;
22 }
23
24 -(void) dealloc {
25 [_cliente release];
26 [cache release];
27 [_itens release];
28 [super dealloc];
29 }
30 @end
Parasabermosquaismembrosdaclasseprecisamdegerenciamentomanual
dememóriabastaaplicarasregrasdoitem1,comadiferen çaqueaschamadasa
releasedevemserfeitasnométodo dealloc,conformeaslinhas25a28.Note
que,naslinhas17e18iniciamosasvariáveis itense cachecom retaine alloc
respectivamente,eambasseencaixamnaprimeiradasregrasquevimos.Contudo,
omembro clienteestádeclaradodeumamaneiraligeiramentediferente,através
dousode @propertycomomodificador retain-nestecaso,oObjective-Cse
encarregadepartedotrabalhoparanós,porémaindaassiménecessárioocódigoda
linha25,casocontrárioocontadordereferênciasnãoseriadecrementado.Se,por
outrolado,usássemos assign,então nãopoderíamosinvocar release.
Quandodeallocéexecutado? deallocéexecutadoautomaticamentequando
fornecessário. Contudo, vocênuncapodechamar deallocdiretamente, exceto
nocasode [super dealloc]; (linha28), queéobrigatório. Lembre-se: use
releaseparainformarquevocêestáliberandooobjeto,enão dealloc.
204

## Página 217

CasadoCódigo Capítulo11. ConceitosfundamentaisdeObjective-C
ARC precisa estar desabilitado
Parausar retaine releaseosuporteaARCprecisaestardesa-
bilitado. Nomesmolugarmostradomaisacimanaimagem 11.2,mude
aop çãopara“NO”.Contudo,tenhaemmentequecadavezmaisbibli-
otecasdeterceirosestãosendoatualizadasparautilizarARCtambém,
oqueresultariaemdiversoserrosdecompilaç ãocasoestaconfiguraç ão
sejadesabilitada.
Naprática,émuitodifícilconseguircombinarcódigoARCcomcó-
digonãoARC-épossível,masigualmentefácildedaralgumtipode
problema.
11.10 S implificando as coisas com literais
UmadasfuncionalidadesintroduzidasnoXcode4.5éoconceitodeliterais(doin-
glêsLiterals),queéumamaneirabemmaissimplesepráticadeiniciarcole çõesde
objetos NSArraye NSDictionary,alémdaconstruç ãocommenoscódigode
objetos NSNumber.
Literais para NSNumber
A classe NSNumber é muito utilizada para encapsular tipos primiti-
vos( char, short, int, long, long long, float, double, BOOL e
bool)paraquepossamserpassadoscomoargumentosparamétodosqueesperam
objetos.Historicamenteissotinhaqueserfeitodaseguintemaneira:
// Encapsulando tipos primitivos em um NSNumber da maneira tradicional,
// existente até o Xcode 4.4
NSNumber *letra = [NSNumber numberWithChar:'A'];
NSNumber *inteiro = [NSNumber numberWithInt:42];
NSNumber *yes = [NSNumber numberWithBool:YES];
JácomoXcode4.5omesmocódigopodeserescritodaseguinteforma:
// Mesmo código feito no Xcode 4.5 em diante
NSNumber *letra = @'A';
NSNumber *inteiro = @42;
NSNumber *yes = @YES;
205

## Página 218

11.10. Simplificandoascoisascomliterais CasadoCódigo
Adiferen çaestáemadicionarocaracter‘@’nafrentedovaloraseratribuído.
Literais para NSArray
Ascoisasficarambemmaissimplesparacriarinstânciasde NSArraytambém,
poisatéoXcode4.4ainicializaç ãosomentepoderiaserfeitadaseguinteforma:
// Criando NSArrays até o Xcode 4.4
NSArray *frutas = [NSArray arrayWithObjects:@"laranja", @"maçã",
@"limão", @"melão", @"morango", nil];
NSString *morango = [frutas objectAtIndex:4];
NSArray *codigos = [NSArray arrayWithObjects:
[NSNumber numberWithInt:33],
[NSNumber numberWithInt:4345],
[NSNumber numberWithInt:999],
[NSNumber numberWithInt:17],
nil];
int dezessete = [[codigos objectAtIndex:3] intValue];
JáapartirdoXcode4.5omesmocódigopodeserfeitodemaneiramuitomais
sucinta:
// Mesma construção, no Xcode 4.5 em diante
NSArray *frutas = @[@"laranja", @"maçã",
@"limão", @"melão", @"morango"];
NSString *morango = frutas[4];
NSArray *codigos = @[@33, @4345, @99, @17];
int dezessete = codigos[3];
Aregraéamesmado NSNumber,bastandoprefixarosvalorescomocaracter‘@’.
Alémdisso,paraacessarumdeterminadoitempeloíndicebastacolocarovalorentre
colchetes,aoinvésdeutilizarométodo objectAtIndex.Umdetalheimportanteé
queestaformadeinicializaç ãoirácriarapenasobjetosimutáveis.Paracriarinstância
deum NSMutableArray(quepermiteadicionarouremoverobjetosaqualquer
momento)façadaseguinteforma:
NSMutableArray *codigos =
[NSMutableArray arrayWithArray:@[@45, @98, @1234]];
206

## Página 219

CasadoCódigo Capítulo11. ConceitosfundamentaisdeObjective-C
[codigos addObject:@[@897]];
[codigos addObject:@[@333]];
[Literaispara NSDictionary]Outraclassequetiragrandeproveitodeliterais
éa NSDictionary,poisalémdosvaloresemsiénecessárioespecificaraschaves
paracadaumdosvalores,oquetornaocódigoumtantochatodeler,conforme
mostradoabaixo:
// Criando e acessando NSDictionary até o Xcode 4.4
NSDictionary *dados = [NSDictionary
dictionaryWithObjectsAndKeys:@"valor1", @"chave1"
@"valor2", @"chave2",
@"valor3", @"chave3",
@"valor4", @"chave4",
nil];
NSString *valorChave2 = [dados objectForKey:@"chave2"];
UtilizandoosliteraisapartirdoXcode4.5,omesmocódigopodeserescritoda
seguinteforma:
// Versão Xcode 4.5 em diante
NSDictionary *dados = @{
@"chave1" : @"valor1",
@"chave2" : @"valor2",
@"chave3" : @"valor3",
@"chave4" : @"valor4",
};
NSString *valorChave2 = dados[@"chave2"];
A inicialização foi simplificada com o uso de@{}, e a separação entre
chaveevaloréfeitacomocaracteredois-pontos(“:”). Demaneirasimilarao
NSArray,umadeterminadachavepodeseracessadautilizandocolchetes(como
dados[@"chave2"])aoinvésdométodo objectForKey:.
207

## Página 221

Capítulo12
Comocriarumacontanoportalde
desenvolvimentodaApple
AAppledisponibiliza,atravésdo iOSDeveloperProgram,asuítecompletadefer-
ramentas,documentaçãoecódigosdeexemploparavocêdesenvolveredistribui
aplicativosparaiOS.Paracome çaracriaraplicativostudooquevocêprecisafazeré
criarumacontagrátisnositededesenvolvedores.
12.1 R egistre-se como um desenvolvedor Apple
OprimeiropassoéseregistrarcomoumdesenvolvedorApple,oquepodeserfeito
deduasmaneirasdistintas: criandoum AppleID dozero,ouentãoutilizaroseu
loginexistentedoiTunes(omesmoutilizadoparabaixaraplicativosdaAppStore,
casovocêtenhaumiPhone,iPodTouchouiPad). Oresultadofinaldeambosos
processoséomesmo.
SevocêjátemumAppleIDbastaacessaroendere çohttp://developer.apple.com/

## Página 222

12.1. Registre-secomoumdesenvolvedorApple CasadoCódigo
devcenter/ios,clicarnobotão Loginefornecerasmesmascredenciaisutilizadaspara
baixaraplicativosnaAppStore.Simplesassim.
CasovocêaindanãotenhaumAppleIDacesseolink https://developer.apple.
com/programs/registerecliquenobotão CreateAppleID.Notequetodasasinfor-
maçõesdevemserinseridaseminglês,evitandocaracteresacentuados.Informeda-
doscomoe-mail,senha,endere çoeoquemaisforsolicitado.Senãosouberoque
preenchernocampo Company/Organization,informe Private. Nofinaldopro-
cessoaAppleenviaráumemailparaoendere çoinformado;abra-oecliquenolink
deverificação.
Depoisquevocêcriouasuacontaouentroucomumaexiste,serásolicitado
algumasinformaçõesgeraissobrevocê,comoperfilprofissionaleparaquaisplata-
formasApplepresentedesenvolver,conformemostraafigura 12.1. Obs:casovocê
utilizeumacontaApplecriadaanteriormente,podeacontecerdenãoapareceratela
daimagem 12.1,esimcairdiretono“iOSDevCenter”. Nestecasoasinformações
devemtersidoinseridosemalgumoutromomento.
Figura12.1:Primeirapartedoprocessodecriaç ãodoAppleID
210

## Página 223

CasadoCódigo Capítulo12. ComocriarumacontanoportaldedesenvolvimentodaApple
12.2 F azendo a assinatura no iOS D eveloper Pro-
gram
Acesseoendere çohttps://developer.apple.com/devcenter/iosparateracessoatodos
osdownloads,documentaç ãoecódigosdeexemplo.
Enquantoqueoacessoaoportaldedesenvolvimento,juntamentecomasferra-
mentasedocumentaçãosãodisponibilizadasgratuitamentepelaApple,pararodaro
aplicativoemdispositivosedistribuí-lonaAppStoreénecessáriofazeraassinatura
doiOSDeveloperProgram,independentementeseoseuaplicativoserágratuitoou
pago.Aassinaturadesteprogramadedesenvolvimentoéanual,ecustaUS$ 99,00
tantoparapessoasfísicasquantoparaempresas.
Assinatura versus conta grátis
Paracome çaradesenvolveraplicativosparaiOSnãoénecessáriore-
alizaraassinaturadoiOSDeveloperProgram,bastandoapenasocadas-
trosimplesexplicadoanteriormentenestecapítulo,quepermiterodaros
aplicativosnosimuladorqueéinstaladocomoXcode.
Para realizar a assinatura, acesse o endereço https://developer.apple.com/
programs/iosecliquenobotão EnrollNow. Oprocessotodoéfeitodaseguinte
forma:
Fornecer os dados de acesso
Aprimeiraparte,identificadacomo SigninorcreateanAppleID,consisteem
informarsevocêdesejarealizarocadastrocomumAppleIDexistenteoucriarum
novo.ConsiderandoquevocêjátemoAppleID,selecioneaop çãoSigninwithyour
AppleID econtinue.Obs:casojáestejalogadonoportaldedesenvolvimento,você
veráaopção“ExistingAppleID”comumbotão“Continue”.Cliqueneleseforoseu
caso.
Assinar uma conta individual ou como empresa
Épossívelrealizaraassinaturacomopessoafísica(containdividual),oucomo
empresa,sendoqueaprincipaldiferen çaentreelaséqueumacontaindividualper-
mitequeapenasumdesenvolvedor(você)tenhapermissãoparaacessaroportalde
211

## Página 224

12.2. FazendoaassinaturanoiOSDeveloperProgram CasadoCódigo
desenvolvimento,enquantoqueacontaempresarialpermitecriartimesdedesen-
volvedores.Selecioneaop çãoIndividualnofimdapágina,eforne çaoseuAppleID
esenhacasosolicitado.
Informações pessoais para validaç ão de seguranç a
Apósrealizadoologiniráaparecerumatelacomotítulo Enteryourbillingin-
formationforidentityverification,conformemostradopelafigura 12.2.Naprimeira
parte,chamada YourName,informeoseunome exatamentecomoaparecenoseu
cartãodecréditointernacionalqueseráutilizadopararealizaropagamentodaas-
sinaturamaisadiante,eem Yourcreditcardbillingaddress informeoendere çode
correspondênciadafaturadocartãodecrédito.Cliqueem Continue.
Figura12.2:Informaçõespessoais
212

## Página 225

CasadoCódigo Capítulo12. ComocriarumacontanoportaldedesenvolvimentodaApple
Selecionar o tipo de assinatura
Apróximatela,demonstradanafigura 12.3,pedeparainformarmosqualassi-
naturadesejamosfazer.Selecione iOSDeveloperProgram(US$99/year) ecliqueno
botão“Continue”.
Figura12.3:Selecionaroprograma
Revisar as informações
Apróximatela, Reviewyourenrollmentinformation&submit,pedeapenaspara
vocêverificarsetodasasinformaçõesfornecidasatéomomentoestãocorretas.Pode
continuar.
Contrato padrão
AtelaProgramLicenseAgreement pedeparavocêlereaceitarocontratopadrão
queéapresentado. Selecioneocheckboxconfirmandooaceiteecliquenobotão I
Agree.
Dados do cartão de crédito
Natela“Enteryourpaymentinformation”vocêdeveinserirosdadosdoseucar-
tãodecréditointernacional,comoemqualqueroutralojadeecommerce.Preencha
asinformaçõessolicitadasecliqueem“Continue”nofinaldapágina.Apróximatela
lheapresentaráumresumodetodasasinformaçõesinseridasatéagora,reviseseestá
tudoOKecliquenobotão“PlaceOrder”,conformeaimagem12.4.
213

## Página 226

12.2. FazendoaassinaturanoiOSDeveloperProgram CasadoCódigo
Figura12.4:Códigodeidentificaç ãodasuaconta,guarde-omuitobem
Guarde muito bem o Enrollment ID
Atenção:guardemuitobemocódigodo EnrollmentID,poiselesse-
rãonecessáriosparaarenovaçãodaassinaturanospróximosanos.AAp-
plenãodisponibilizaemnenhumoutrolugarestecódigo,porémsolicita-
onoprocessoderenovaç ão.
Aofinal,vocêseráapresentadocomumatelacomoadaimagem 12.5.AApple
dizlevaratédoisdiasúteisparaprocessaroseucartãodecrédito,porémébastante
comumeleserraremousimplesmenteesqueceremoseupedido,pormaisabsurdo
queissopossaparece. Sepassarmuitotempodoprazoevocênãotiverrespostas,
liguenosuportetécnicodaApplenosEstadosUnidos(infelizmentenãohácanal
diretodeatendimentonoBrasil)erelateoocorrido.JáaconteceudaApplecobrar
maisdeumavezomesmopedido,efrequentementepassamdiassemdarqualquer
informação,portantoomelhorcanaléviatelefone.
214

## Página 227

CasadoCódigo Capítulo12. ComocriarumacontanoportaldedesenvolvimentodaApple
Figura12.5:Telafinal
12.3 O s tipos de certificados
TodoaplicativoquerodanoiOSprecisaserassinadodigitalmentecomachavedo
desenvolvedoreumacontra-chavedaApple,quejuntasgarantemalegitimidade
doseuaplicativo.Existemcertificadosparadesenvolvimento,homologaç ãoepara
produção,chamadosnostermoseminglêsde Development,Ad-hoceDistribution
respectivamente.Oscertificadosdedesenvolvimentoeproduç ãovocêutilizarácom
certeza,enquantoqueodehomologaç ão(Ad-hoc)somenteénecessáriosedese-
jarmosenviaroaplicativoparaoutraspessoastestá-loantesdeenviaroficialmente
paraaAppStore. Porém,comoéexplicadonestecapítulo,existeumlimiteanual
paradispositivosdehomologaç ão.
Paratestarosaplicativosduranteoprocessodedesenvolvimento,épossíveluti-
lizarosimuladordeiOSqueéinstaladojuntamentecomoXcode,oqualnãoprecisa
deumcertificadoespecífico,erodá-lonoseuiPhoneouiPadatravésdocertificado
dedesenvolvimento.
215

## Página 229

Capítulo13
Rodandoosaplicativosnoseu
iDispositivo
AtéagoratodososaplicativosquefizemosnolivrorodaramnosimuladordoiOS
quevemjuntocomoXcode,enestecapítuloiremosverospassosnecessáriospara
rodarosmesmosaplicativosdiretamentenodispositivo,sejaeleumiPhone,iPadou
iPodTouchouqualqueroutroiGadgetqueposteriormenteaApplevenhaalan çar.
Arazãodededicarmosumcapítulointeiroparaesteassuntoéque,aocontráriodo
simulador,osiDevicessomentepodemrodaraplicativosassinadosdigitalmente,o
querequertantoumcertificadododesenvolvedorquantoumcertificadodaApple,
numprocessochamado“provisionamento”,dotermoeminglês“provisioning”
Existemtrêstiposdeprovisionamento:paradesenvolvimento,paratesteseho-
mologação,eparadistribuiç ãonaAppStore.Odedesenvolvimentopermiterodare
debugaroaplicativonodispositivoatravésdeumcaboUSB,diretamentepeloXcode.
Oparatestesehomologaç ão,chamadode“Ad-hoc”,éútilparadistribuiroaplicativo
paraqueoutraspessoaspossamajudaratestarouvalidar—ocasomaiscomuméo

## Página 230

13.1. Crieeinstaleocertificado CasadoCódigo
clienteparaoqualvocêestácriandoaapp.Jáodedistribuiç ão(doinglês“distribu-
tion”)éutilizadoparaenviaraversãofinalparaaAppStoredefato.
Emborafocaremosnoprovisionamentodedesenvolvimento,ospassosnecessá-
riosparaodeAd-DoceDistribuiç ãosãovirtualmenteosmesmos.
Utilize oSafari caso tenha problemas em alguns pas-
sos
Poralgummotivoinexplicávelesemrazãoalguma,énecessárioreali-
zarospassosdestecapítuloutilizandooSafariaoinvésdequalqueroutro
browser,poismuitofrequentementeosistemaonlinedaAppleiráacu-
sarqueosarquivosenviadosviauploadestãocorrompidos.Utilizando
oSafariesteproblemanãoocorre.
Emboravocêtalvezconsigarealizarosprocedimentoscomsucesso
comoutrobrowser,omaisseguromesmoénãoabusardasorte,eirpelo
Safari.
T odos os passos descritos neste capítulo assumem que você já tenha a conta
paga de desenvolvedor.
13.1 C rie e instale o certificado
Oprimeiropassoéobterocertificadodigitalqueseráutilizadoparacriaraschaves
deprovisionamento.Acesseo iOSProvisioningPortalnoendere çohttps://developer.
apple.com/account/overview.action,cliquenolink Certificatesnomenuesquerdo,e
depoisnobotãocomosímbolodesoma,conformeafigura 13.1.Natelaqueseabrir,
selecione“iOSAppDevelopment”ecliqueem“Continue”.
218

## Página 231

CasadoCódigo Capítulo13. RodandoosaplicativosnoseuiDispositivo
Figura13.1:Primeiropassoparasolicitarocertificadodigital
Atelaseguintedeveráserumacomotítulo“AboutCreatingaCertificateSigning
Request(CSR)”,quecontêmapenasumaexplicaçãogeral.Cliquemaisumavezem
“Continue”.
Paracriarocertificadoprimeiroprecisamosenviarumarquivodesolicitaç ão
paraaApple,chamadode CertificateSigningRequest(CSR),oqualcontémuma
chavedecriptografiapública,queaAppleutilizaráparaemitirocertificado“dever-
dade”.Eleéoqueficarávinculadoàsuacontadedesenvolvedorparatodosospro-
pósitos.NoseuMac,abraoaplicativo KeychainAccess(localizadoem Applications
->Utilities),eacesseomenu KeychainAccess->CertificateAssistant->Requesta
CertificatefromaCertificateAuthority conformeafigura 13.2
Figura13.2:MenudoKeychainparaacessar
Na tela que abrir, informe o seu endereço de e-mail no campoUser email
219

## Página 232

13.1. Crieeinstaleocertificado CasadoCódigo
address, e selecione a opção Saved to disk, conforme a figura13.3. Depois
clique no botãoContinue, e o Keychain irá pedir para você salvar o arquivo
CertificateSigningRequest.certSigningRequestemalgumlugar. Este
éoarquivoquedeveráserenviadoparaoportaldedesenvolvimento.
Figura13.3:Primeirateladecriaç ãodachavepública
Apóssalvaroarquivo CertificateSigningRequest.certSigningRequest
emdisco,volteparaatela Certificatesdoportaldedesenvolvimento,selecioneo
arquivonobotão ChooseFile,ecliquenobotão Submit,conformeafigura 13.4.
Lembre-sedefazerestepassopeloSafaricasosejainformadaalgumamensagemde
erroaoenviar.
220

## Página 233

CasadoCódigo Capítulo13. RodandoosaplicativosnoseuiDispositivo
Figura13.4:EnviandooCSRparaaApple
Setudoocorrersemproblemas,obrowserseráredirecionadodevoltaparaatela
decertificados,Seestiveraparecendoapenasamensagem PendingIssuance,espere
algunsminutosedêrefreshnatela,poisàsvezesosistemademoraumpoucopara
liberarodownloaddocertificado.
Nateladafigura 13.5cliqueemcimadonomedocertificadoparaexpandiras
opções,ecliquenobotão“Download”.Parainstalá-losbastadarumduplocliqueno
arquivo,eeleseráimportadoparadentrodo Keychain,conformeafigura 13.5.Note
quedeveráaparecero“AppleWorldwideDeveloperRelationsCertificationAuthority”,
eoseu“iPhoneDeveloper”dotipoCertificateePrivateKey-sehouverapenasalgum
deles(geralmentesomenteo Certificate),algumpassofoirealizadoincorretamente.
Obs: o“AppleWorldwideDeveloperRelationsCertificationAuthority”éinstalado
automaticamentepeloXcode,portantovocênãodeveterproblemas.
221

## Página 234

13.2. Crieaidentidadedoseuaplicativo-AppIDs CasadoCódigo
Figura13.5:Certificadosinstaladoscomsucesso
Certificados de desenvolvimento e distribuição
Éimportantefrisarqueexistemdoiscertificadosquevocêiráeven-
tualmenteprecisar:oprimeiroéodeDesenvolvimento(Development ),
queacabamosdecriar,eserveparaafasededesenvolvimentodoaplica-
tivo.OoutroéocertificadodeDistribuiç ão(Distribution),utilizadopara
enviarparaclienteshomologaremantesdeentrarnaAppStoreeparaen-
viarparaaAppStoredevez,paraopúblicofinal.Oprocedimentopara
criarocertificadodeDistribuiç ãoéomesmododeDesenvolvimento,
apenasdevendoserfeitonaaba“Distribution”domenu“Certificates”.
13.2 C rie a identidade do seu aplicativo- AppIDs
Umapartevitaldoseuaplicativoésuaidentificaç ão,chamadade AppID,aqualéuti-
lizadaemtodasaspartesdoecossistemadoiOS,inclusiveparadistribuiç ãonaApp
Store.OAppIDéumidentificadorúnico,sendoqueexisteapossibilidadedecriar
umcoringaparaasuaconta,paraquepossaserutilizadoemdiversosaplicativos
(comrestrições,porém).
ParacriarumnovoAppIDselecioneaop çãoAppIDs nomenulateraleemse-
guidacliquenobotãorepresentadopelosinaldesoma,queabriráapáginadafigura
13.6. Oprimeirocampo(AppIDDescription)éumabrevedescriç ãodoaplicativo
222

## Página 235

CasadoCódigo Capítulo13. RodandoosaplicativosnoseuiDispositivo
apenasparaoseuprópriocontroleinterno,enosegundocampodoformulário(App
IDPrefix)selecioneaop çãoTeamID.Oterceirocampo(BundleID)seráoidentifi-
cadoremsi,queporviaderegradeveserúnicodentre todosaplicativosexistentes
naAppStore. Arecomendaç ãodaprópriaAppleéutilizarumestilodenomen-
claturaqueseassemelheaumdomíniodeinternetreversoseguidodonomedo
aplicativoemsi,como br.com.example.MeuSuperApp.Pessoalmentevouum
passoalémecolococomosufixoaplataforma(iPhoneouiPad)casoexistaapossi-
bilidadedelan çarversõesdiferentesdoaplicativoparaiPhoneeiPad—nestecaso,
oAppIDficariasendoalgocomo com.rafaelsteil.MeuSuperApp.iphonee
com.rafaelsteil.MeuSuperApp.ipad.
Figura13.6:FormuláriodecriaçãodeumnovoAppID
Apóspreencheroformulárioeclicarnobotão Submitvocêdeverávoltarparaa
223

## Página 236

13.3. Adicionandodispositivosparadesenvolvimento CasadoCódigo
teladelistagemanterior,naqualestarálistadooaplicativo.Sevocêclicaremcima
donomedele,umboxiráexpandirmostrandooqueestáhabilitado. Cliqueno
botãoEdit:paramostraratelaondeépossívelhabilitarsuportea PushNotifications,
iCloud:: eoutrasfuncionalidadesopcionais. Porhoranãoénecessáriomodificar
nada,epodemosprosseguirparaopróximopasso.
AppID coringa
AApplepermiteacriaç ãodeumAppIDcoringa,quepodeseruti-
lizadoparadiversosaplicativosdistintossemquehajaanecessidadede
criarumIDespecificoparacadaum,oqueébastantevantajosoquando
estamoscriandováriosaplicativosdetestes.ParacriaroAppIDcoringa
bastaselecionaraop ção“WildcardAppID”einserir*(asterisco)no
campoBundleID)dafigura 13.6.
SomenteépossívelcriarumAppIDcoringaporconta.AAppleuti-
lizaonome CatchAllparasereferenciaraestetipodeAppID.
13.3 A dicionando dispositivos para desenvolvi-
mento
Paraquesejapossívelrodarosseusaplicativosduranteafasededesenvolvimento,é
necessárioprimeirocadastrá-losnoiOSDevelopmentPortal.Ocadastrododisposi-
tivo,quepodeserqualqueriDevice,éfeitocomofornecimentodeumIDúnicocha-
madoUDID,dotermoeminglês UniqueDeviceIdentifier (ou“Identificadorúnico
dedispositivo”),queéumcódigocom40caracteres.Paralocalizá-lo,conecteoseu
dispositivoaoMacviacaboUSB,abraoXcodeeacesseomenu Window->Orga-
nizer,eselecione-onase çãoDevicesdomenuesquerdo,conformemostraafigura
13.7.OUDIDéaquelecódigoaoladodotexto“Identifier ”.Copieocódigo(repare
queéumcampodetextoselecionável).
224

## Página 237

CasadoCódigo Capítulo13. RodandoosaplicativosnoseuiDispositivo
Figura13.7:LocalizandooUDIDdoseudispositivo
Reparequenafigura 13.7existeumbotãochamado UseforDevelopment,que
habilitaodispositivoparaserutilizadoparatarefasdedesenvolvimento,comorodar
diretamentedoXcodeeutilizarosrecursosdedebug. Certifique-sedeselecionar
estaop ção.
TendooUDIDemmãos,acesseaop ção Devicesnoportalecliquenobotão
comosímbolodesoma. Noformulárioqueseabrecoloqueumnomedescritivo
dodispositivonocampo Name,eoUDIDobtidoanteriormentenocampo UDID.
Cliqueem Submiteeledeveráaparecernalistagem.
13.4 L imite anual de dispositivos
AAppleimpõeumlimiteanualde100dispositivosparaseremutilizadosparates-
tesehomologaç ão,permitindoresetarocadastroumaúnicavezporano,apósa
renovaçãodacontadedesenvolvimento.Estenúmerode100dispositivosésempre
incrementalduranteoano,nemmesmodiminuindosevocêremoveralgumregis-
tro.Emboraparaodesenvolvedorindependenteestarestriç ãonãochegaaserum
grandeproblema,nocasodeempresasqueatendemadiversosclienteséumfator
bastantepreocupante,poisumavezatingidoolimiteanualnãoháqualquermaneira
deconseguircadastrarmaisdispositivos,sendonecessárioesperaroperíododere-
225

## Página 238

13.5. Crieocertificadodeprovisionamento CasadoCódigo
novaçãodaconta.
Depoisderenovaracontado iOSDeveloperProgram,ase çãoDevicesdoportal
irámostrarumavisoemamareloinformandoquevocêtemagoraaop çãodere-
mover“deverdade”osregistrosquedeseja.Faça isso antes de adicionar qualquer
outro dispositivo,poisaoadicionarumnovoregistroasuacontaficarátravadapor
maisumano.
13.5 C rie o certificado de provisionamento
Agoraquejátemosanossachaveprivada,ocertificadodaApple,oAppIDeo
dispositivodetestesdevidamenteregistrado,oúltimopassoéobteroarquivode
provisionamento(ProvisioningProfile). Eleéutilizadoparaassinardigitalmenteo
aplicativodetalformaquesejapossívelrodá-lonosdispositivoscadastradossem
passarpelaAppStore.Paratanto,acesseomenu Developmentdase ção“Provisioning
Profiles”nomenulateral,eemseguidacliquenobotãocomosímbolodesoma.
Noformulárioqueabrirselecione“iOSAppDevelopment ”ecliquenobotão
“Continue”,napróximatelaselecioneo“AppID”,natelaseguintemarqueocerti-
ficadoautilizar(deveráhaverumúnico).Depoisdeclicarem“Continue”maisuma
vez,selecioneodispositivonalistaecliquenovamentenobotãodecontinuar.Por
último,coloqueumnomedescritivoparaoprofile,ecliquenobotão“Generate”.
Reconfigure o provisioning após adicionar um novo
dispositivo
Lembre-sequetodavezquevocêcadastrarumnovodispositivoéne-
cessárioreconfiguraroarquivodeprovisionamento,bastandoparaisso
clicarnolink Editedepoisem Modifynatelaprincipaldolink Provisi-
oningdomenulateral(amesmamostradanafigura 13.8),eporúltimo
marcarosdispositivosdesejados.
Nalistagemdosprovisionamentos,cliqueemcimadonomedoquefoicriado
nopassoanterior,eemseguidanobotão“Download ”.
Casotudotenhaocorridocomsucessovocêdeveráveroarquivodeprovisiona-
mentolistadonatelaprincipaldomenu Provisioning,eobotão Downloadhabilitado,
conformemostraafigura 13.8. Façaodownloaddestearquivo(eleteráaextensão
226

## Página 239

CasadoCódigo Capítulo13. RodandoosaplicativosnoseuiDispositivo
.mobileprovision)edêduplocliqueparaabri-lono OrganizerdoXcode.Apósaim-
portação,eledeveráestarlistadocomostatus ValidProfile,nase ção Provisioning
ProfilesdaLibrarydoorganizer,conformemostraafigura 13.8.
Figura13.8:Provisionamentoimportadocorretamente
13.6 A ssocie o arquivo de provisionamento no
Xcode
Oúltimopassoparapoderrodarosaplicativosnosdispositivoscadastradoséconfi-
guraroXcodeparautilizaroarquivodeprovisionamentoapropriado.Abraaspro-
priedadesdoprojetodesejado,selecioneo Targetapropriado(porpadrãosomente
existiráum,correspondenteaonomedoprojeto)nomenulateral,eselecioneaaba
BuildSettings.Nela,vocêdeverálocalizarase çãoCodeSigning->CodeSigningIden-
tity,quedeveráterovalor::Don’tCodeSign”,oqualiremosmodificar.Vejaafigura
parareferência13.9.
227

## Página 240

13.6. AssocieoarquivodeprovisionamentonoXcode CasadoCódigo
Figura13.9:Localizandoase çãoparasele çãodoarquivodeprovisionamento
Nalinhado CodeSigningIdentity cliqueemcimade Don’tCodeSignparaabriro
menudesele çãodeperfisdeprovisionamento,eselecioneaop çãoiPhoneDeveloper,
conformemostraafigura 13.10.Aop çãoiPhoneDeveloper seencarregadeautoma-
ticamenteutilizaroperfildeprovisionamentomaisapropriado.Porviaderegra,ele
iráverificarovalordocampo BundleIdentifier naaba Summaryecompararcom
osperfisexistentes,utilizandoalgumidentificadorquesejaigualaocadastradona
seçãoAppIDs noportaldaApple(vejaafigura 13.6).Casocontrário,iráutilizaro
CatchAll(coringa)casoexista.
228

## Página 241

CasadoCódigo Capítulo13. RodandoosaplicativosnoseuiDispositivo
Reforçando a importância do Bundle Identifier
Prestebastanteaten çãoemrelaç ãoaofluxoqueédescritonesteca-
pítulo,poisumavírgulaerradapoderáfazervocêperdermuitashoras
detrabalho(efiosdecabelo)tentandoencontraroquedeuerrado.Isso
éespecialmenteválidoparao BundleIdentifier,oqualdevesercorres-
pondentenoXcodeaovalorcadastradonase çãoAppIDs noportalda
Apple.
Porexemplo,senoterceirocampodafigura 13.6vocêinseriuovalor
“com.exemplo.MeuSuperApp.iphone”,éexatamenteestevalorquedeverá
serutilizadonocampo BundleIdentifiernoXcode(Propriedadesdopro-
jeto->Summary->BundleIdentifier ).
Figura13.10:SelecionandooperfiliPhoneDeveloper
Umavezselecionadooperfil,oresultadodeveráficarconformeodafigura 13.11
229

## Página 242

13.7. Rodeseuaplicativonodispositivo CasadoCódigo
Figura13.11:Perfilselecionadocorretamenteparatodasasop ções
13.7 Rode seu aplicativo no dispositivo
Agoraquetemostudoconfigurado, pararodaroaplicativonodispositivobasta
conectá-loaoMacviacaboUSBeselecioná-locomodestinonoXcode,conforme
mostradonafigura 13.12. Compileoprojeto(Command+B)erode-outilizando
Command+R.Casoapare çaumacaixadediálogopedindopermissãoparautilizar
asuachave(aquelacriadaanteriormente,noiníciodocapítulo),selecioneaop ção
“AlwaysAllow”(“Permitirsempre”).
Figura13.12:Selecionandoodispositivopararodaroaplicativo
230

## Página 243

CasadoCódigo Capítulo13. RodandoosaplicativosnoseuiDispositivo
CasooXcodeapontealgumproblemacomoodafigura 13.13,verifiqueseoperfil
iPhoneDeveloperestáselecionadoemtodasaslinhasdase çãoCodeSigningIdentity,
conformeafigura 13.11.
Figura13.13:Falhaaocompilardevidoaerronaconfiguraç ãodoperfildeprovisio-
namento
13.8 V erificando a instalação dos perfis no disposi-
tivo
Paraverificarosperfisinstaladosemumdeterminadodispositivobastaacessaraapp
Settings,irnase çãoGeneraleprocurarpelosperfisnofinaldatela,conformemostra
afigura13.14.
Figura13.14:Localizaçãodoperfildeprovisionamentonodispositivo
231

## Página 245

Capítulo14
Umapalavrafinal+bônus
Umadaslições(vindaemformadeconselho)maisimportantesqueaprendilogo
quecomeceiatrabalharcomdesenvolvimentodesoftware,eaqualdecertaforma
memoldouemdiversosaspectos,foiaseguinte:onossotrabalhoéencontrarso-
luções,nãoreclamarquetudoédifícileque“nãodáparafazer”,ficandosemaç ão.
Seoproblemaestámuitodifícil,quebre-oempedaçosmenoresatéquesejapossível
resolvê-lo.Esenãodáparafazerdamaneirasolicitada,entãoencontreumaforma
possível.
Asempresastêmproblemasqueprecisamsersolucionados,eparaissotentam
contratarasmelhorespessoaspossíveis. Você,aofazerpartedaequipe,temares-
ponsabilidadedeencontraredesenvolverasoluç ão.Senãofizer,quemfará?Pense
nisso.
Abraço,Rafael

## Página 246

14.1. Bônus-livroselinks CasadoCódigo
14.1 B ônus - livros e links
Conhecimentonuncaédemais,eabaixoestãoalgunslivrosesitesextremamente
úteis.
• LearnObjective-CforJavaDevelopers,ISBN978-1430223696(http://amzn.
to/PwFyQl)
• Objective-CforAbsoluteBeginners, ISBN978-1430236535(http://amzn.to/
Q3m0Tm)
• Stackoverflow(http://bit.ly/oW30Ca)
• PrincipaldocumentaçãodaApplesobredesenvolvimentoiOS(http://bit.ly/
dGP5Cm)
• GuiadaAppleparadesenvolvimentodeaplicativos(http://bit.ly/PXZEW4)
• http://www.icodeblog.com(blogeartigos)
•http://iosdevelopertips.com(blogeartigos)
•http://maniacdev.com(blogeartigos)
•http://www.raywenderlich.com(blog bastante famoso, com artigos muito
bemelaborados)
•http://www.cocoacontrols.com (muitos componentes e projetos Open
Source)
234