---json
{
  "id": "guia_front-end_o_caminho_das_pedras_para_ser_um_dev_front-end",
  "title": "Guia Front-End O caminho das pedras para ser um dev Front-End",
  "categoria": "03-linguagens",
  "subcategoria": "java",
  "resumo": "**Arquivo Original:** `Guia Front-End O caminho das pedras para ser um dev Front-End.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "caminho",
    "das",
    "dev",
    "end",
    "front",
    "front-end",
    "guia",
    "java"
  ],
  "perguntas_tipo": [
    "Como utilizar Guia Front-End O caminho das pedras para ser um dev Front-End?",
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

# Guia Front-End O caminho das pedras para ser um dev Front-End

> **Arquivo Original:** `Guia Front-End O caminho das pedras para ser um dev Front-End.pdf`
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

CasadoCódigo Sumário
Sumário
1 Introdu ção 1
2 HTML 5
2.1 Tudocome çaeterminanoHTML . . . . . . . . . . . . . . . 5
2.2 Hipertexto . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.3 Marcação . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.4 Microdata . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.5 W3CeWHATWG Amoreódio . . . . . . . . . . . . . . . . 11
3 CSS 15
3.1 Ascamadasdedesenvolvimento . . . . . . . . . . . . . . . . . 16
3.2 ProgressiveEnhancementeFaultTolerance . . . . . . . . . . 17
3.3 Organizandoseusassets Breveexplicação . . . . . . . . . . . 19
3.4 Organizandoocódigo . . . . . . . . . . . . . . . . . . . . . . . 20
3.5 CSSOM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.6 UmpoucodeCSS3D . . . . . . . . . . . . . . . . . . . . . . . 24
3.7 SobreFrameworksCSS . . . . . . . . . . . . . . . . . . . . . . 28
3.8 SobreStyleGuides . . . . . . . . . . . . . . . . . . . . . . . . . 31
3.9 Leiturarecomendada . . . . . . . . . . . . . . . . . . . . . . . 32
4 Um pitaco sobre editores 35
4.1 EsqueçaoseditoresWYSIWYG . . . . . . . . . . . . . . . . . 36
4.2 SublimeText . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
4.3 Outroseditores . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
i

## Página 4

Sumário CasadoCódigo
5 Cuidando do seu código 43
5.1 EsqueçaoFTP . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
5.2 Sobrecontrolesdeversão . . . . . . . . . . . . . . . . . . . . . 44
6 JavaScript 51
6.1 AprendapelomenosobásicodeJavaScript . . . . . . . . . . 53
6.2 Escopodevariáveis . . . . . . . . . . . . . . . . . . . . . . . . 53
6.3 ModulePatternJavaScript . . . . . . . . . . . . . . . . . . . . 56
6.4 AprendajQuery . . . . . . . . . . . . . . . . . . . . . . . . . . 61
7 Web Mobile 63
7.1 OqueéoAdaptiveWebDesign . . . . . . . . . . . . . . . . . 66
7.2 MediaQueries . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
7.3 MetatagViewport . . . . . . . . . . . . . . . . . . . . . . . . . 74
7.4 UnidadesemREM . . . . . . . . . . . . . . . . . . . . . . . . . 78
7.5 Imagens . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
7.6 Muitomais . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
8 Performance 89
8.1 Oprocesso . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
8.2 SaibaoqueéRefloweRepaint . . . . . . . . . . . . . . . . . . 91
8.3 OndecolocaraschamadasdeCSSeJS? . . . . . . . . . . . . 93
8.4 Paraestudarmais . . . . . . . . . . . . . . . . . . . . . . . . . 95
9 Acessibilidade 97
9.1 Oqueéacessibilidadeparaweb? . . . . . . . . . . . . . . . . 97
9.2 Acessopeloteclado . . . . . . . . . . . . . . . . . . . . . . . . 98
9.3 InputTypes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
9.4 WAI-ARIA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
10 Pré-processadores CSS 103
10.1 Porqueusarpré-processadores?. . . . . . . . . . . . . . . . . 103
10.2 UmpoucodeSASS . . . . . . . . . . . . . . . . . . . . . . . . 104
10.3 Pontosparapensar. . . . . . . . . . . . . . . . . . . . . . . . . 112
ii

## Página 5

CasadoCódigo Sumário
11 Ferramentário (T ooling) 117
11.1 Grunt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118
11.2 Bower. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
11.3 DevInspector . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
11.4 Consoledosbrowsers . . . . . . . . . . . . . . . . . . . . . . . 128
11.5 Sobreousodoterminal . . . . . . . . . . . . . . . . . . . . . . 137
12 Produzindo sites com código estático 139
12.1 Paraosnovatos:UsandoIncludesPHP . . . . . . . . . . . . . 140
12.2 GerandositesestáticoscomMiddlemanouJekyll . . . . . . . 141
13 Compartilhando o que sabe 147
14 T extos extras 149
14.1 Últimoconselho:nãoqueiraseropróximoZeno . . . . . . . 149
14.2 SobreosPavõesdoFront-end . . . . . . . . . . . . . . . . . . 152
14.3 Sobreodesignoco . . . . . . . . . . . . . . . . . . . . . . . . . 153
15 Até mais e obrigado pelos peixes 159
15.1 Devsquevocêdeveseguir . . . . . . . . . . . . . . . . . . . . 160
15.2 50palavras . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164
iii

## Página 7

Capítulo1
Introdução
Sempreouvimuitasreclamaçõesdeiniciantesdizendoquefaltaminforma-
çõesmostrandoo“caminhodaspedras”,ensinandocomoeporondecomeçar
nomercadodefront-end.Sãotantastecnologias,metodologias,boaspráticas
eoutrostantostópicosquesurgemtodososdias,queeuconfesso:realmente,
ficamuitodifícilacompanhartudo.Alémdasobrecargaenormequeéficar
testandotodasasnovidades.Eumesmotenhoquefiltrarbastanteosassuntos
aaprender.Geralmente,eunãomeatenhoanadaqueeunãopreciseutilizar
emalgumprojeto.Nãovouaprenderautilizarum frameworkouumaferra-
menta,simplesmenteporquetodomundoestácomentandoporaí.Eupreciso
trabalhar,afinaldecontas.TenhoquegarantiroJackDanielsdascrian ças.
Mas,seriapedirmuitoteralguémaomeuladonoiníciodaminhacar-
reiradizendooqueéperdadetempo?Muitosdevsquedecidemseaventu-
raraprendemtodaamatériasozinhos. Eununcaentendiisso. Eumesmo,
quandoadolescenteinconsequente,nãoqueria,nemapau,estudarporconta

## Página 8

CasadoCódigo
própria.Issomudoudepoisquecomeceiatrabalharcomweb.Coisasestra-
nhasdavida!Aprenderalgosozinhoéinteressante!Certamente,vocêpode
acabarperdendobastantetempotentandodescobriroquevaitorná-loou
nãoprodutivo.Éumprocessochatoetrabalhosoenemsemprevocêacerta.
Quandoestamossozinhos,équasecertoquedeixaremospassarinformações
importantesnoprocessodeaprendizado. Jávitantosbonsdesenvolvedo-
resfront-endqueiniciaramsuacarreiracomoautodidatas,masnãotinham
ideiadoqueeracontroledeversão,WAI-ARIAou,atémesmo,propriedades
corriqueirasdoCSS.Nãoporqueeleseramdesatentos,masporqueestavam
focadosemoutrostópicos.Issoénormalacontecerquandoaprendemosalgo
deformanãolinear,emisturandofontesdoconteúdo.Porisso,étãoimpor-
tanteteralguémquemostre,pelomenos,adire çãocorreta.Vocêeconomiza
tempoe,talvez,atéalgumdinheironesseprocesso.
A missão deste guia
Esteguiatemamissãodeajudarqualquerpessoaquequeirainiciarna
áreadeweb. Foquei-meemdesenvolvedoresfront-endporqueéaáreano
qualosprofissionaispossuemmaiorfamiliaridadequandodesejamentrarno
mercadodeweb.Mesmoassim,sevocêéumapenasumcuriososobreoas-
sunto,masquerentendermelhorsobreotema,talvezestelivropossaajudar.
Esteguiavaiapresentarosassuntosmaisbásicoseimportantes,tentandoau-
xiliaraquelesquejáadentraramouqueremadentrar,agora,omercadode
web.
Organização por prioridade
Nãosepareiostópicosporordemdedificuldade,massimporordemde
prioridade.Querodeixarclaroqueaescolhadasprioridadesatendeaminha
opinião. Ouseja,hámilharesdepessoasaíaforaquepensamdiferentede
mim.Eudecidi,aqui,oqueseriamaisoumenosimportanteaprenderpara
ingressarnaárea.Outraressalvaquefaçoéque,talvez,vocêpreciseaprender
umassuntomaiscomplicadoantesdepassarparatópicostidocomomais
fáceis.Porexemplo:émaissignificativoqueumdevfront-endsaibaprimeiro
obásicodeJavaScriptdoquedeSEO.Vocêatéencontraumbomemprego
sabendoapenasHTML,CSSeSEO,mas,namaioriadoscasos,JavaScript
2

## Página 9

CasadoCódigo Capítulo1. Introdução
costumasermaisrelevante.
O que este guia não é?
Definitivamente,esteguia nãoéumlivrodidático,logo,elenãovaien-
sinarnadadocome çoaofim,nemtãopoucocódigo.Estelivrosepropõea
mostraro“caminhodaspedras”,ditandooquevocêprecisaaprender,mos-
trandotodososassuntospertinentesparasetornarumdevfront-endequais
osassuntosmaiscomentadosporaí.
Issonãoquerdizerquevocêpreciseaprendertudooqueestálistadoaqui.
Pelocontrário!Estelivrovaiajudá-loadecidiroqueaprenderprimeiro.Mas,
semdúvida,vocêprecisasaberqueestesassuntosexistem.Voutentarindicar
linksdereferências(eminglêseemportuguês)paraestudoduranteopercor-
rerdolivro.Tometempoparavisitá-loseestudá-lostambém.Sãolinkscom
muitoconteúdoimportante.
Ensinaro“caminhodaspedras”.Inspirarsuacuriosidade.Fazê-loentrar
damaneiracorretanomundododesenvolvimentoweb.Éissoqueestelivro
sepropõeafazer.Boaleitura!
3

## Página 11

Capítulo2
HTML
2.1 T udo começa e termina no HTML
Sevocêtivessequeaprenderapenasumassuntosobretudooqueestelivro
comenta,esseassuntoseria,semdúvida,HTML.SemoHTMLepe çolicença
paraincomunscomparações,oCSSnãopassadeumaperigueteempereque-
tadaeoJavaScript,umcarasolitáriochorandodesconsoladamente.OHTML
éopontofocaldetudooquesefazemdesenvolvimentoweb.Nãoimportao
quevocêfaça,oHTMLéoquehádemaisimportantenaweb.
Nãohácomovocêsetornarumdevfront-endsemdominarHTML.Ele
estarápresentedesdeoiníciodoprojetoeseráresponsávelpormuitaspar-
tescruciaisdurantetodaasuaelaboraç ão.OHTMLéocódigoqueperpassa
todasasequipesevocê,sendoumdevfront-end,éoresponsávelporele.
Mesmoqueosprogramadoresback-endfaçamalgoerrado,évocêquezelará
pelaqualidade,performance,estruturaesemânticadoHTML.Seasemântica

## Página 12

2.2. Hipertexto CasadoCódigo
estámalfeita,ositenãoiráaparecernosresultadosdebusca,aacessibilidade
ficaráprejudicada,amanutençãoserádanificadacomotempo,nãoexistirá
portabilidadee,certamente,vocêteráproblemasgigantescomocódigole-
gado.Pareceexagero,masnãoé.Tudocome çaeterminanoHTML.
A essência
EuseiquevocêjádeveterlidoexaustivamentesobreasintaxedoHTML.
Maseupróprioli,empoucoslugares,averdadeiraimportânciadoHTML.
Poressemotivo,escolhidoisassuntosinteressantesquelhedarãoalgumavan-
tagemsobreoidiota,sentadoaoseulado,nodiadaentrevistadeemprego.
Listo:hipertextoemarcação(estruturaçãosemântica).Vocêpodeaprender
aescrevercódigoHTMLemqualquerlugarnaweb. Existemmilharesde
sitesbrasileiroseestrangeirosqueensinamisso.Contudo,materialsobrehi-
pertextoousemânticasãogeralmenteescassoseosqueencontramos,prin-
cipalmenteosimportados,sãobempesados.Queromostraroiníciodestes
assuntosparaquevocêpesquisemais,posteriormente,afimdeseaprofundar.
Mesmoassim,oquevocêabsorveraquijáserádegrandeajudaemprojetos
detodosostamanhos.
2.2 H ipertexto
Comoqualquercrian çanaidadeescolar,eufaziatrabalhosescolaresotempo
todo.Oprocessoquasesempreeraassim:aprofessoradefiniaoassuntoe,ao
chegaremcasa,eupegavaumbocadodepapelalmaço(lembra-se?)eiapara
casadaminhatia.Láeraondeasenciclopédiasficavam.Seeuprecisassefazer
umtrabalhoescolar,certamente,taisenciclopédiasmeajudariamnatarefa.
Asenciclopédiaserampesadas. Chatasdeseremusadas. Porém,conti-
nhamtudoouquasetudodoqueeuprecisavaparacompletaromeutrabalho.
Oqueeugostavanasenciclopédiaseraafacilidadedeencontrarasinfor-
maçõesdequeeuprecisava.Funcionavamaisoumenosassim:seeuquisesse
sabersobre“automóveis”,euprocuravanaprimeiraenciclopédia.Aofinaldo
texto,semprehaviaumareferênciaparaumassuntorelacionado,nestecaso,
porexemplo,sobre“motores”,quemelevavaparaumasegundaenciclopé-
diaeassimpordiante. Eusempreconseguiaencontrar,rapidamente,oque
6

## Página 13

CasadoCódigo Capítulo2. HTML
desejava.
Organizando a informação
Ainformação–umtexto,porexemplo–podeserorganizadadeforma
linearounãolinear.Imagineumlivro.Todaainformaç ãocontidanolivro
estáestruturadadeformalinear,issoé,hácomeço,meioefim.Vocênãocon-
segueabsorvertodoosignificadodeumahistóriaseiniciarsualeiturapela
metadedolivro. Vocêprecisa,necessariamente,come çarlendooprimeiro
capítuloatéchegaraoúltimo,paraabsorvereentenderomáximopossívelde
informaçãosobreahistóriacontada.
Asenciclopédiaspossueminformaçõesorganizadasdeformanãolinear,
ouseja,asinformaçõesnãoestãoemumaordemespecífica,massim,de
formarelacionaleassociativa.Exemplo:quandovocêprocurainformações
sobre“veículosautomotores”emumaenciclopédia,aofinaldotexto,você
podeencontrarumasériedereferênciasdosassuntosrelacionados,como,
porexemplo:“motoresdecombustãointerna”,“rodas”,“tiposdecombustí-
veis”,“mecânica”etc.
Essamaneiranãolineardeorganizarainformaç ãoébaseadaemcomoa
suamentefunciona.Quandovocêpensaemumassunto,seucérebrofazuma
sériedeassociaçõesparaformarumaideia,trazeràtonaumamemóriaou
umalembrança.Poressemotivo,seucérebroconsegueguardarinformações
quepodemserrecuperadasquandopensamosdiretamentenelasouquando
pensamosemassuntosrelacionados.
V annevar Bush
Entendersobrecomoorganizarinformaçãoéentendercomofuncionaa
internet. EstudiososcomoVannevarBusheTedNelsonforamospioneiros
emformarideiassobrecomosistematizargrandesvolumesdeinformaç ão,
nãocontendoapenastextos,mastambém,imagens,vídeosesons.TedNelson
cunhouotermo Hipermídia.Elecrioutodooconceitodelinkagemdetex-
tos,porvoltade1960.Entretanto,muitoantes,em1945,VannevarBushdes-
creveuemseuartigo As We May Think(http://bit.ly/BushAsWeMayThink)
umdispositivochamadoMemex.Estedispositivoarmazenariaumagrande
quantidadedeinformaçõesrelacionadaseconectadasentresi,possibilitando
7

## Página 14

2.3. Marcação CasadoCódigo
arecuperaçãodetaisdadosdemaneirafácil,semdispendermuitotrabalho
manual.
Selevarmosesseconceitoparaweb,percebemosqueapenasumatagfaz
essetrabalhodereferênciaeassociaçãodeinformação:o link.Naweb,relaci-
onamosinformações,sitesequalqueroutroobjetousandoatag“A”.Quando
vocêlinkaumtexto,umaimagem,umgráfico,vocêassociaestainformação
aodestinodolink.Vocêestáreferenciandoassuntos,comonaenciclopédia.
Nósusamosolinktodososdiaseapostoquemetadedosdesenvolvedores
nãomensuraaimportânciadessatag.Semoslinks,nãoháweb.Nãoconse-
guimosassociarnadaacoisaalguma.Perde-seareferência.
Sugiroquevocêpesquisemaissobreahistóriado hipertexto.Vocêvaien-
tenderaamplitudedoquesignificaorganizarinformaç ãoesuaimportância
paraosdiasdehoje,tantoparaweb,quantoparaomundoemsi.Éumassunto
fascinante!Sequiser,comeceporaqui: http://bit.ly/History_of_hypertext.
2.3 M arcação
Nãoadiantalinkarerelacionarinformaçõesnawebseessasinformaçõesnão
detiveremsignificado.
Vocêsabediferenciarumtítulodeumparágrafoporqueéumserhumano
letrado(assimespero).Vocêconseguefazerissoporquereconheceascarac-
terísticasdecadaelemento:otítulotemletrasgrandese,geralmente,poucas
palavras;oparágrafotemletraspequenaseéformadopormuitaspalavras.
Essascaracterísticasfazemseucérebrodiferenciarumelementodooutro.As-
simécomtodososoutroselementosnoHTML.
Osmeiosdeacessocomoossistemasdebusca,leitoresdetelas,browsers,
scriptsouquaisqueroutrosquetentemlerseucódigoHTMLnãopossuem
essainteligênciaeprecisamdeajudaparaentendercadaumdesseselementos.
Essaajudaéoquechamamosdetags. Astagssãomarcaçõesqueformam
cadaelementodoHTML.Umparágrafoémarcadocomatag <p>,umtítulo
importantecomatag <h1>etc.Cadatagtemsuafun çãoeseusignificado.
Logo,oHTMLservepara dar significado à informação,eaissonome-
amosde semântica.
Ótimo! Agoraquesabemosbasicamenteoquesignificasemântica,fica
8

## Página 15

CasadoCódigo Capítulo2. HTML
maisfácilentendersobreaestruturaçãosemânticadelayouts.Asnovastags
(nemtãonovasassim)doHTML5foramcriadasparaquepossamosexter-
narasemânticadocódigo,nãodeixandoosignificadoapenasparaseucon-
teúdo,mastambémparaaestruturaondeoconteúdoseencontra. Explico
melhor:imaginedoistítulosnapágina umnocabe çalhoeoutronorodapé.
Vocêsabequeotítulodocabe çalhoémaisimportantedoqueotítulodo
rodapé.Masossistemasdebusca,comooGoogle,nãodiscernemessefato.
Paraele,sãodoistítulosepronto.Umnocome çodapáginaeoutronofinal.
Poressemotivo,existemastags <header>e <footer>.Dessaforma,em
vezdecriarmos <div class="cabecalho">,podemoscriar <header
class="cabecalho">.Ossistemasdebuscaouqualqueroutracoisacon-
seguemsaberqueatag HEADER,porexemplo,setratadeumcabe çalho.Em
consequênciadisso,éfácilidentificaredefiniraimportânciadecadainfor-
maçãodeacordocomolocalnoqualelafoiinserida.
AstagsdoHTML5nosderamapossibilidadeparaacabarcoma“sopa
deDIVs”queeramoswebsitesesistemasweb. Ocódigoficouorganizado
visualmentee,definitivamente,maissemântico.
2.4 M icrodata
Oconceitode Microdatanãoénovo.SevocêjáouviufalarsobreMicrofor-
mats,vaisefamiliarizarfacilmentecommicrodados.
Paraquemaindadesconhece,pensenoseguinte:comovocêdizparaal-
gumsistemadebuscaqueumdeterminadotextonositeéumaresenha?Ou,
comovocêdisponibilizaasinformaçõessobreseuevento,comoolocaledata
paraserviçosdeterceirosnainternet?
OsMicrodadossãoatributosinseridosnastagsdoHTMLcominforma-
çõesparacomplementarseusignificado.
AespecificaçãodeMicrodadosdoHTMLdefineummecanismoqueper-
mitequemeiosdeacessocomodispositivos,scripts,sistemas,serviçosetc.
reconheçamdadosquepossamserinseridosemdocumentosHTMLcomfa-
cilidade.Essesdadosdevemserlegíveisparasereshumanoseparamáquinas,
devendosertambémcompatíveiscomoutrosformatosdedadosexistentes,
como RDFou JSON.
9

## Página 16

2.4. Microdata CasadoCódigo
OGooglenosforneceumexemplomuitointeressante. Vejaaseguiro
texto:
<div>
Meu nome é James Bond, mas todos me chamam de Bond.
Este é o meu site: <a href="#">example.com</a>
Moro em Londres, Inglaterra, e trabalho como detetive secreto.
</div>
Quandovocê,serhumano,lêestetexto,entendetodasasinformações.
Oproblemaéqueas“máquinas”nãoconsegueminterpretartextos(ainda).
Porisso,éinteressantequeindiquemosessasinformaçõesparaquepossamos
reutilizá-lasemoutrosprojetos.Taisinformaçõescomplementaressãoúteis
parascriptsquecriamostodososdiasemnossossistemas.
Agora,essemesmocódigorecheadodeMicrodados:
<div itemscope itemtype="http://data-vocabulary.org/Person">
Meu nome é <span itemprop="name">James Bond</span>
mas todos me chamam de <span itemprop="nickname">Bond</span>.
Esta é a minha página inicial:
<a href="#" itemprop="url">example.com</a>
Moro em Londres, Inglaterra, e trabalho como
<span itemprop="title">detetive secreto</span>
na <span itemprop= "affiliation">ACME Corp </span>.
</div>
Nesse código, indicamos que o texto se trata de uma pessoa (
itemtype),cujonome( itemprop="name")éJamesBond,masoape-
lido( itemprop="nickname")éBond. Eletambémtemumwebsite(
itemprop="url"),édetetivesecreto( itemprop="title")etrabalha(
itemprop="affiliation")naACMECorp.
Aideiaéqueainformaçãosejaacessívelparaqualquercoisa.Qualquer
coisamesmo.Sevocêconsegueler,umamáquinadeveconseguirlertambém.
Seumamáquinapodeler,elaprecisainterpretaressesdados,comoseucé-
rebrofaz.Porisso,éimportantequeumamesmalinguagemsejaconversada
entremáquinaeserhumano,demodoquetodainformaç ãopodeserusada
paraoutrosfins.
10

## Página 17

CasadoCódigo Capítulo2. HTML
Aideiadeexistiremcomplementosparaexpandiremosignificadodein-
formaçõesemelementosdoHTMLnãoénova.Os Microformatsjáhaviam
tentadoentraremvogaumavez,semsucesso.Houvepoucosadeptos,emui-
tosserviçosebrowsersempotencialsimplesmentenãoadotaramatecnolo-
gia.Agora,comumanovaépocanodesenvolvimentoweb,emquediversas
necessidadestêmsurgido,principalmenteemumaeranaqualdispositivos
usamainternetcomoplataforma,algumasempresasvoltaramaseinteres-
sarpeloassunto. UmexemplodissoéotrabalhoqueoGoogle,oYahoo,o
BingeaYandextemfeitocomopadrãoSchema(http://schema.org),oqual
ébaseadonopadrãodeMicrodata.
Lembre-sequeoobjetivoprincipaléentregarconteúdoparaousuário,
nãoimportacomoeleestejaacessandoessainformaç ão.Seforpormeiode
umAppouumsistemaweb,seforporumcelularouporumóculos(não
importa!),eledeveconseguirconsumirainformaç ãoquedesejare,princi-
palmente,poderreutilizá-la.
2.5 W3C e WHATWG A mor e ódio
Sevocêénovonaárea,deveentenderqueodesenvolvimentoparainternet
passouporváriasrevoluções. OTablelessnasceudeumadelas. Umadas
revoluçõesmaisrecentes,equevocêdeveteracompanhadodeperto,foio
nascimentodoHTML5.Naverdade,poucagentesabecomotudoaconteceu,
masfoibemsimples.
OWHATWG(The Web Hipertext Application T echnology Working Group)
éumgrupodedesenvolvedoresquenãoseconformavamcomavelocidade
comqueascoisasaconteciamnoW3C.ElessãoumgruposeparadodoW3C.
FoifundadopormembrosdaMozilla,AppleeOperaporvoltade2004.Eles
resolveraminiciaraescritadeumanovarecomendaç ãoparaoHTML,jáque
oW3CiriaabandonaroHTMLefocarseusesfor çosemlinguagensbaseadas
emXML.Éporissoque,algumdianoseupassado,vocêcome çouafechar
astags BRcomumabarranofinal( <br/>).Sugiroqueleiaestecapítulodo
livro HTML5 For Web Designers(http://html5forwebdesigners.com/history/
index.html#the_schism_whatwg_tf).
Hoje,entendemosqueesseseriaumcaminhobemruim. Portanto,o
11

## Página 18

2.5. W3CeWHATWG Amoreódio CasadoCódigo
WHATWGresolveuiniciaressadocumentaçãodeformaindependente,de
modoqueosdesenvolvedoreseosbrowserspudessemavan çarodesenvol-
vimentowebcomumatecnologianovaetotalmentefocadaeminovações.
Deucerto.Comoosmembrostinhaminfluêncianacomunidadeetambém
dentrodosbrowsers,oHTML5logosetornoupopular.Osbrowserscome ça-
ramaadotarasnovidadesimediatamenteeosdesenvolvedorescome çarama
implementá-lasemseusprojetos.
Contudo,apartirdessemomento,iniciou-seumarixaentreoWHATWG
eoW3C.OpróprioTimBerners-Lee,todavia,admitiuemoutubrode2006
(http://dig.csail.mit.edu/breadcrumbs/node/166)queastentativasdelesde
dirigirawebdoHTMLparaXMLnãoestavamfuncionandomuitobem.Foi
poressemotivoqueoW3CdecidiucriarumHTMLWorkingGroup,come-
çandodozeroeusandoasespecificaçõesdoWHATWGcomobaseparaa
futuraversãodoHTML.Issofoibomeruimaomesmotempo:oW3Cini-
ciouumgrupoqueiriatrabalharnoHTML5(noteoespaçoantesdo5)e
oWHATWGestavatrabalhandonaversãoHTML5(semespaços),queseria
usadapelopróprioW3Ccomobase!
Umdosproblemasfoioseguinte:quandoháduasespecificações,qualos
desenvolvedoresdevemseguir?Apostoquevocê,hojeemdia,recorrepouco
àdocumentaçãodoW3C,nãoé?Normalmente,asinformaçõesdenovidades
noHTML5vêmdeblogsespecializadosnoassunto.Masdeondeessesblogs
tiramessasinformações?EugostobastantedoWHATWG,porqueadocu-
mentaçãodelesébastanteativa.Elesescrevem-nabaseando-seempequenos
pedaçosenãocomoalgomonolítico,quemudadetemposemtempos,depois
demuita,muitarevisão.Elessãomaiságeis.
MozillaChiefTechnology Officer, Andreas Gal
“Generally we tell developers to look at the WHATWG version, which
tends to be developed with better technical accuracy, ”
HáumartigonaC|Netmuitopertinentequediscorresobreessapicui-
nhaentreosdoisgrupos.Sevocêquiserentendermaissobreoassunto,leia:
12

## Página 19

CasadoCódigo Capítulo2. HTML
HTML5 is done, but two groups still wrestle over Web’s future (bit.ly/html5-
web-future),escritopeloStephenShankland.
Masquemdecidequaisasnovidadesvindouras?OW3Cestátrabalhando
noHTMl5.1,queincluiumasériedenovidadesemCanvase drag-and-drop.
Entretanto,oWHATWGtambémestátrabalhandoemcoisasdessegênero.
HáoutroproblemaapontadopeloWHATWG,quealegaqueoW3Cviveco-
piandosuaspartesdarecomendaçãoeusandoemsuasdocumentaçõesofici-
ais.NoartigoqueoStephenescreveu,háumexemplocomentandoaespeci-
ficaçãosobreospadrõesdeURL,noqualoW3Cpossuiumrascunhosobreo
assunto,masemalgunsmomentos,oW3CapontaorascunhodoWHATWG
comosendoaúltimaversão.
OW3Ctemtentadosemovermaisrápidonoprocessodetransformar
rascunhosemrecomendações.Noentanto,issonãoétãofácilassim.Sevocê
semoverápido,vocêprecisasedesapegardealgumascoisas.AideiadoW3C
équetudosejaaltamenteestável.Nãodáparacorrereentregaralgumacoisa
seaquilo,emalgummomento,vaitravar. Essaéagrandediferen çaentreo
W3CeoWHATWG.Paramim,ébastantecompreensível.
Existemtrêspilaresprincipais:W3C,browsersedevs.Eeusemprepresto
atençãoaosbrowsers.Seosbrowsersachambacanaumadeterminadaespe-
cificação,elescome çamaadotá-la,deformaqueosdevsimplementamessa
novidadeemseusprojetos. OquesobraparaoW3C?Seupapelébastante
importantepararegulamentarestespadrões.NãocreioqueoW3Cvásairde
cenaoualgodotipo. Eleéimprescindívelparaodesenvolvimentodaweb.
Masprecisaseguiravelocidadedosdevs,assimcomoosbrowserstêmfeito.
Porisso,éimportanteaatuaçãoderepresentantesdosprópriosbrowsersnos
gruposdetrabalhodoW3C.Tambémqueémuitoimportanteque vocêparti-
cipedaslistasdediscussãodosgruposdetrabalho.Aqui,estãotodasaslistas
dee-maildequevocêpodeparticipardoW3C(http://lists.w3.org/).
Vamosvercomoissotudosedesenrola.Participe.Nãosejaumdevpas-
sivoàsmudan ças.
13

## Página 21

Capítulo3
CSS
Ah,oCSS.Criadoem10deOutubrode1994porH åkonWiumLieeBert
BosporcontadanecessidadedeformatardocumentosHTML,formatando
decentementepelaprimeiravezainformaçãoqueerapublicadanainternet.
Aprincipaldiferen çadoCSS,comparadoaoutraslinguagensparecidas,
eraapossibilidadedaheran çadeestilosemcascatadoselementos.Issoex-
plicaonome Cascading Style Sheets.Aideiaéquevocênãoprecisaformatar
elementoporelemento,masquecadaestilosejaherdadoparafacilitaredar
liberdadeparamodificaraformataçãodainformação. Logo,sevocêquiser
quetodososparágrafosdapáginasejamdacorazul,bastaescreverumalinha
etodososparágrafosficarãoazuis.

## Página 22

3.1. Ascamadasdedesenvolvimento CasadoCódigo
3.1 A s camadas de desenvolvimento
Valedarumaexplicaçãorápidadeumconceitobastanteantigoequeestá
paramudar,masquemesmoassimregeaformacomquenosorganizamos
nocódigo:existem3camadasnodesenvolvimentoweb:ainformaç ão,forma-
taçãoecomportamento.Acamadade informação,normalmentecontrolada
peloHTML,exibeedásignificadoàinformaç ãoqueousuárioconsome.É
nelaquevocêmarcaoqueéumtítulo,umparágrafoetc.,dandosignificado
eestruturandocadapedaçodeinformaçãopublicada.
Acamadade formataçãoénormalmentecontroladapeloCSS.Énelaque
vocêcontrolacomoainformaçãoseráformatada,transformandoolayout
feitopelodesigneremcódigo.OCSSéoresponsávelpordarformaàinfor-
maçãomarcadacomHTML,paraqueelasejabem-vistaemqualquertipode
dispositivo.
Jáacamadade comportamentoeracontroladapeloJavaScript.Masagora
oCSStambémestátendoalgumaresponsabilidadenesseterreno. Nesta
camada é onde controlamos qual será o comportamento da informação.
Quandoumamodalseabreouumsliderdeimagensfunciona,éoJavaScript
queestáentrandoemação.
Essassãodescriçõesbembásicasdecadacamada. Expliqueiissotudo
paraquevocêentendaoprincipalobjetivodoCSS,queécontrolaraforma-
taçãodainformação.
Contudo,entendaoseguinte:oCSSnuncavaidarsignificadoaqualquer
informação,emboraelepossaproduziralgumapseudo-informaç ãonatela
usandoos pseudo-elementos :aftere :before(marqueparaestudardepois).O
CSStambémnãoéumalinguagemquefazascoisasfuncionarem,tipouma
linguagemserver-side. Masissovocêjádevesaber. OlugardoCSSébem
definido:formatarainformação.
OfuturodoCSSaindaéumaincógnita.Durantemuitotempopintamos
quadradinhos,literalmente,comCSS.Hojefazemoselementos3Decontro-
lamosanimaçõesetransiçõesnatela. Nósatésubstituímosalgumastarefas
queanteseramfeitascomJavaScript.MasninguémsabeaindacomooCSS
vaicaminhardaquiparaafrente. Seráqueelevaiganharumalinguagem
secundáriaparacuidardeanimação?Ouseráquesuasintaxeprecisasermo-
dificadaparacontemplartodasaspossibilidades?
16

## Página 23

CasadoCódigo Capítulo3. CSS
Sãodúvidascomquevocênãoprecisasepreocuparagora,massaibaque
daquialgunsanosvocênãoestarádigitandomaisCSScomofazemoshoje.
3.2 P rogressive Enhancement e Fault Tole-
rance
NãohácomofalarsobreProgressiveEnhancementantesdefalardeFault
Tolerance.
FaultToleranceécomoasmáquinastratamumerroquandoeleacontece.
Éahabilidadedosistemadecontinuaremoperaç ãoquandoumafalhaines-
peradaocorre. Issoaconteceatodomomentocomseucérebro. Osistema
nãopodepararatéqueesseerrosejaresolvido,logoeledáumjeitoparaque
esseerronãoafetetodooresto.Anaturezainteiratrabalhadessaforma.Os
browserstrabalhamdessaforma.Éporissoquevocêconseguetestarascoisas
maravilhosasdoCSS3edoHTML5semsepreocuparcombrowsersantigos.
Porexemplo,quandoescrevemosumapropriedadedeCSSqueobrow-
sernãoreconhece,elesimplesmenteignoraaquelalinhaepassaparaapró-
xima.IssoaconteceotempointeiroquandoaplicamosnovidadesdoCSSou
doHTML.Lembra-sequandoosbrowsersnãoreconheciamosnovostipos
decamposdeformuláriosdoHTML5?Obrowsersimplesmentesubstituíao
campodesconhecidopelocampocomumdetexto.Issoéimportanteporque
oquesefazhojenodesenvolvimentodeumwebsite,continuaráfuncionando
dealgumaformadaquia10anos. Comoosbrowserstêmessatolerânciaa
falhas,linguagenscomoHTMLeCSSganhampoderparaevoluirotempo
inteiro,semosbloqueiosdaslimitaçõesdopassado.
Tudo sobre acessibilidade
Fundamentalmente, ProgressiveEnhancementétudosobreacessibili-
dade.Naverdade,otermo acessibilidadeénormalmenteusadoparaindicar
queoconteúdodeveseracessívelparapessoascomnecessidadesespeciais.
OProgressiveEnhancementtrataissomasnaóticadequetodomundotem
necessidadesespeciaiseporissooacessodeveriaserfacilitadoparaqualquer
pessoaemqualquertipodecontexto.Issoincluifacilmentepessoasqueaces-
samwebsitesviasmartphones,porexemplo,cujatelaépequenaealgumas
17

## Página 24

3.2. ProgressiveEnhancementeFaultTolerance CasadoCódigo
dasfacilidadesqueexistemnodesktopsestãoausentes.
Níveis e tolerância
Nóspassamosporalgunsníveisaodesenvolveralgotendocomométodo
oProgressiveEnhacement.Essesníveistêmcomoobjetivosempreservirpri-
meirooconteúdoedepoistodasasfuncionalidadesecomportamentosque
podemmelhoraroconsumodesteconteúdoetambémdetodaapágina.
Abaseparatolerarerrosésempremanterumfallbackquandoalgoruim
acontecer. Aprimeiracamadageralmenteédarumfallbackbásico,conhe-
cidopelamaioriadosdispositivos,paraservirumconteúdoemformade
texto.Issoéóbvioporquetextoéacessívelparapraticamentequalquercoisa.
MuitosdoselementosdoHTMLtêmumfallbackdetextoparacasosonde
elementonãosejacarregadoounãosejareconhecido. Lembradoatributo
ALT?Atémesmonastagsdevídeoeáudio,comoaseguir:
<video src="video.ogg" controls>
Texto de fallback.
</video>
AsegundacamadaéasemânticadoHTML.CadaelementodoHTML
temsuafun çãoeprincipalmenteseusignificado. Elesacrescentamsignifi-
cadosaqualquerinformaçãoexibidapeloHTMLemuitasvezesestendemo
significadoqueotextosozinhonãoconseguiriapassar.
O texto é universal
Aterceiracamadadeexperiênciaéacamadavisual,ondeoCSSetam-
bémasimagens,áudiosevídeossãoresponsáveis.Éondeacoisaficabonita
einterativa.Aquivocêsentemaisatolerânciadosbrowsersafalhas.Usamos
otempointeiropropriedadesquenosajudarãoamelhoraraimplementaç ão
delayouts,masqueembrowsersantigospodemnãoserrenderizados.Expe-
rimentamosissoatodomomento.
Aquartacamadaéacamadadeinteratividadeoucomportamento.OJa-
vaScripttomacontadessapartecontrolandooselementosdoHTML,muitas
vezescontrolandopropriedadesdoCSSpararealizaraçõesdeacordocomas
interaçõesdousuário.
18

## Página 25

CasadoCódigo Capítulo3. CSS
AcamadafinaléumaextensãodasemânticadoselementosdoHTML.
AíéondeinserimosasiniciativasdeWAI-ARIA.Éondevamosguiarleitores
detelaseoutrosmeiosdeacessoparaelementosepontosimportantesna
estruturaemqueolayoutsebaseia,indicandoquaisregiõeseelementossão
referênciadenavegação.
Háoutroladoépensarem Gracefull Degradation,queéexatamenteo
opostodoProgressiveEnhancement.OGracefullDegradationéaformade
fazerseuwebsitedegradarharmoniosamente,ouseja,emvezdevocêpensar
emumabasesólidaparaquetodososbrowsersantigosconsigamrenderi-
zarseusitesemproblemas,oGracefullDegradationnivelasempretudopor
cima.Aideiaéquevocêinicieodesenvolvimentofazendotudooqueháde
melhornaslinguagens,mastentandoprevercomooselementosficarãocaso
umbrowsernãoconsigareconhecer,porexemplo,umapropriedadedoCSS.
OGracefullDegradationéumaabordagemumpoucoarriscadaporque
vocênuncaconseguepreveremtodososcenáriosoqueexatamenteobrowser
dousuáriovaideixarderenderizar.Porisso,aabordagemdoProgressiveé
algomaiscorreto,umavezquevocêjápreparouaspossibilidadesparacaso
umproblemaaconte ça.
Naminhaopinião,vocênãoprecisasepreocuparcomissotudo,basta
teremmentequeoclienteprecisateramelhorexperiênciaqueodispositivo
eosoftwarepodemdar. Essaéaformamaisseguraemaisprodutivadese
trabalhar.
3.3 O rganizando seus assets Breve explicação
AprenderCSSnãoéalgocomplicado.Asintaxeébastantesimplesdeenten-
dereosresultadossãovistosfacilmentenobrowser. Vocêescreve,atualiza
apáginaeboom,osresultadosestãologoali.Masquandosetratadaorga-
nizaçãodocódigoedaestruturadearquivos,acoisatodapodecomplicar
dependendodotamanhodoprojeto.EmboraasintaxedoCSSsejabastante
simples,tudopodeirporáguaabaixoseaestruturadosseusarquivosnão
forembemplanejados.
19

## Página 26

3.4. Organizandoocódigo CasadoCódigo
Organizando os arquivos
VocêtemumasériedemaneirasparaorganizarseuCSS.Masamaneira
maiscomumémodularizarosarquivos. Cadaarquivoficaresponsávelpor
umapartedosite. Adecisãoquevocêvaitomaré:dividirosarquivospor
áreasdositeouporcomponentes.
Normalmente,dividimososarquivosdeCSSporáreasquandooprojeto
épequeno,porexemplo,emumprojetodewebsiteinstitucional.Vocêpode
criarumarquivoparaformatarasidebareseuconteúdo.Outroparaformatar
oheader,outroparaofooter,outroparaapáginainternadetextoeassimpor
diante.
Emprojetosmaiores,comograndesportaisdeconteúdoouprodutos,é
muitomelhorsepararosarquivosdeCSSpormódulosecomponentesde
layout.VocêvaiterumCSSquevaiformatartodososbotõesdosite,outro
paratipografia,outroCSSvaiformatarlistas,omenu,aslistasdenotíciasda
sidebaretc.Emsitesmaiores,vocêvaicriarmaispáginascombinandoestes
elementos.
Claro,háexceções. Masgeralmenteessasduasformasdeorganizarseu
CSScobremtodasassuasnecessidades.Aestruturadepastasédegostopes-
soal. EU(portanto,éojeitocomoeugostodetrabalhar)separoumapasta
naraizdoprojetochamada assets. Dentrodela,tereioutrasduascomo
nomede JavaScriptse stylesheets.Vocêpodechamaressaspastas
de jse cssseacharmelhor.Temgentequenãogostadonomedapastano
plural...Denovo,gostopessoal.
Apastadeimagenspodeounãoficardentrodessapasta assets. Eu
costumocolocá-lasdentro.
UmaboaideiaéfuçaremprojetosalheiospeloGitHubparaencontrar
umaestruturadequevocêgostemaisouquevocêentendaquesejaamais
comum.Masoimportanteémanterseucódigoorganizado.
3.4 O rganizando o código
Sevocêtrabalhacomumaequipe,ocódigoescritoprecisaparecerquefoi
produzidoporumapessoa.Essaéaregradeouroemprojetoscomequipes
pequenasougrandes. Vocêprecisatransitarpeloprojetotodoesentirque
20

## Página 27

CasadoCódigo Capítulo3. CSS
aquilofoiescritoporvocê.Paratanto,cadaumdaequipeprecisaescrevero
códigodoprojetoseguindoumasériedepadrõesdeescrita,paraquenofinal,
oresultadosejaalgohomogêneo.
O @mdo (twitter.com/mdo), um dos criadores do Twitter Bootstrap,
criouumguiaderegrasdecodificaç ãobastanteinteressante,eeuconcordo
comamaioriadasregras. Seriabastanteinteressantequevocêlessedepois
naíntegra http://diegoeis.github.io/code-guide/ etentasseapresentaressas
regrasparaseuscolegasdetrabalho.Aprodutividadevaisernotadalogonas
primeirassemanas.
Aquivãoalgumasdasdicas:
• AtributosHTMLdevemusarestaordememparticularparafacilitara
leituradocódigo:class,id,data-*,for,typeouhref,title,alt,aria-*,role.
• Semprequepossível,eviteelementospaissupérfluosquandoescrever
HTML.Muitasvezesénecessárioumainteraçãoourefatoração,mas
issoproduzpoucoHTML.
• Assegure-serapidamentedequearenderizaçãodoseuconteúdode-
clareoencodingdecaracteresexplicitamente:metacharset=“UTF-8”.
• Usesoft-tabscomdoisespaços.
• Quandoagruparseletores,deixeseletoresindividuaisemumalinha.
• Incluaumespaçoantesdeabrirumcolchete.
• Coloqueofechamentodocolcheteemumanovalinha.
• Incluaumespaçodepoisdosdoispontos:emcadadeclaraçãodepro-
priedade.
• Cadadeclaraçãodeveestaremsuapróprialinhaparaencontrarmos
melhoroserros.
• Fechetodasasdeclaraçõescomponto-vírgula;.
• Valoresseparadosporvírguladevemincluirumespaçologodepoisda
vírgula(ex. box-shadow).
21

## Página 28

3.5. CSSOM CasadoCódigo
• Não inclua espaços depois das vírgulas, como em coresrgb(),
rgba(), hsl(), hsla()ou rect().Istoajudaadiferenciarmúlti-
plosvalores(vírgulas,semespaço)decoresdepropriedadesmúltiplas
(vírgulas,comespaço). Tambémnãocoloquevaloresiniciadoscom
zero(ex. .5emvezde 0.5).
• Deixetodososvaloreshexadecimaisemcaixabaixa: #fff. Letras
comcaixabaixasãomaisfáceisdeseremlidaseentendidasquando
queremosscanearodocumento.
• Usecoresemhexadecimalabreviadasquandopuder, porexemplo:
#fffemvezde #ffffff.
• Coloque aspas nos valores em seletores com atributos:
input[type="text"].
• Eviteespecificarunidadesquandoosvaloresforem0: margin: 0;
emvezde margin: 0px;.
3.5 CSSOM
OCSSOMéumassuntopoucofaladonomercado. Nãoquenãosejaim-
portante,porqueé,maselenãoafetadiretamentesuaprodutividade. Éum
daquelesassuntosteóricosquediferenciaumbomdevdeumótimodevfront-
end.Porisso,eisminhapreocupaçãoemfazervocêconheceresseassunto.
OHTMLtemaDOM,eoCSStemaCSSOM,acrônimode CSS Object
Model.QuandoobrowserestácarregandooDOMdoHTML,queéaárvore
deobjetosdoHTML,eleencontraumchamadoparaumcódigoCSSeco-
meçaamontaroutraárvore,baseadanosseletoresdoCSS.Essaárvorefaz
umareferênciaentreosseletores,quevairepresentaroselementosnoHTML
esuaspropriedadesvisuaisqueserãomodificadaspeloCSS.
OGoogletemumaimagemmuitobacanaquenosajudaaexplicar:
22

## Página 30

3.6. UmpoucodeCSS3D CasadoCódigo
3.6 U m pouco de CSS 3D
OCSS3DésemdúvidaumadasfeaturesdoCSSmaisaguardadasportodas
ascriançasdoBrasil.Falaaverdade!Fazerefeitoscomsombra,gradientes,
transparênciasetc.umdiajáfoialgobacananavidadodesenvolvimento.Mas
fazercomqueoselementossecomportememumespaço3Désensacional.
OCSS3Dtrazparaawebefeitosvisuaisnuncaantesvisto.
Masnãoseanimemuito.Euseiquevocêestáansiosoparasairporaíco-
locandoefeitos3DdeCSSemtudoquantoéaplicaç ão.Mascalma...Entenda
queoCSSfoifeitoparaestilizardocumentos. Vocêoutilizaparamelhorar
aexperiênciadosusuáriosnosdiversosdispositivosenãoparaenfeitarseu
websitecomosefosseumapenteadeira.Lembra-sedoswebsitescheiosdegifs
animados? Poisé,cuidadoparanãocairnomesmoerro. Vocêestaráutili-
zandooCSS3Ddamaneiracertaseseusefeitospassaremdespercebidospelo
usuárioaoutilizarseusistema.Encherseusistemacomefeitosacadaclique
ouacadaaçãopodefazercomqueousuáriopercatempoeapaciência.
Tudo é uma questão de perspectiva
Parafalarde3D,precisamosfalarsobreperspectiva. Paramanipular
umaárea3Doelementoprecisarádeperspectiva.Vocêpodeaplicarapers-
pectivaaoelementodeduasformas: utilizandodiretamenteapropriedade
perspectiveouadicionandoumvalor perspective()napropriedade
transform.
div {
perspective: 600;
}
ou
div {
transform: perspective(600);
}
24

## Página 32

3.6. UmpoucodeCSS3D CasadoCódigo
Fig.3.2:ExemplosdeperspectivausandoCSS3D.
CSS 3D Transforms
VocêdeveestaracostumadoatrabalharcomoseixosXeYnoCSSpa-
drão. NoCSS3DpodemosmanipulartambémoeixoZ,querepresentaa
profundidade.
Vejanaimagemlogoaseguir, estouutilizandoosvalores rotateY,
rotateXe translateZ.Percebaqueno translateZeuutilizeivalo-
resnegativosepositivos.Quandoutilizoovalornegativo,oobjetofica“mais
longe”e,secolocovalorespositivos,oobjetofica“maisperto”.
26

## Página 33

CasadoCódigo Capítulo3. CSS
Fig.3.3:Diferen çasdoCSStransformcomosvaloresderotateetranslate.
.pai {
border:1px solid #000;
padding:0;
float:left ;
margin:50px 100px;
}
.pai div {
width:200px;
height:200px;
color:#333 ;
font:bold 15px verdana;
27

## Página 34

3.7. SobreFrameworksCSS CasadoCódigo
padding:20px;
background:rgba(255,255,255,0.7);
border:1px solid #000;
perspective: 500;
}
.pai div.translateY {
transform: translateZ(-100px);
}
.pai div.translateZ {
transform: translateZ(100px);
}
.pai div.rotateY {
transform: rotateY(45deg);
}
.pai div.rotateX {
transform: rotateX(45deg);
}
Nóspodemosutilizartambémalgunsatalhosparaessesvaloresondepo-
demosdefinirastrêsdimensõesdeumavez:
• translate3d(x,y,z)
• scale3d(x,y,z)
• rotate3d(x,y,z,angle)
Muitoimportante:aoutilizaraspropriedadesresumidas,osbrowsersati-
vamautomaticamenteaaceleraçãoporhardwarenoSafariparaqueasani-
maçõestenhamumamelhorperformance.
3.7 S obre Frameworks CSS
Sevocêtrabalhaemumgrandeprojetoondeháelementosdiferentesevá-
rioscomportamentos,talvezsejaumaótimaideiacriarumframeworkpara
28

## Página 35

CasadoCódigo Capítulo3. CSS
esseprojeto. Normalmente,eucriopequenosframeworksparaprojetoses-
pecíficos,geralmenteprodutos.Dificilmentecrioframeworksquandoestou
fazendowebsites,masalgunsprincípiosaindasemantêmeissoémuitobom
porque,emboranãohajaumframeworkportrás,háumaltoníveldeorgani-
zaçãodecódigo,queotornalegívelparamanuten çõesposteriores.
Por que criar um framework?
Existemdiversosmotivosparavocêcriarumframeworkparaseuprojeto.
Algunsdelessão:
Prototipação
Paraprovarumateoria,éimportantequepossamoscriarprotótiposde
telaoudeumfluxointeirodoprojeto.Éimportantequeosprotótipostenham
ainterfacemuitofielàinterfacefinal. Édiferentequandovocêpedeparao
usuáriotestardeterminadatelaseelaaindaestácomcaradewireframe.Nesse
caso,oframeworkajudabastante. Tendotodososmóduloseoscomporta-
mentosprontos,vocêequalquerumdaequipeconseguemumfluxodetelas
emalgumashoras,mesmonãosendoumdesenvolvedorfront-end.
Usandooframeworkparafazeresseprotótipo,vocêtemagarantiadeque
ovisualseráexatamenteoqueiráparaaproduç ãoeousuárionãosentirá
aquelaestranhezadeinterfaceinacabada.Nãoháanecessidadenesseponto
deterqualquerback-endfeito. Vocêestánafasedeprototipaçãoeporisso
tudocomoqueousuáriointeragirseráfake,resumindo:serãoapenaspáginas
estáticas,comlinkssimplesquelevamparaoutrastelas.
Padronização
Umframeworknãocriaapenaspadronizaçãodeinterface,maspadroni-
zaçãodecódigoecomportamentos.Émuitoimportantequeousuárioutilize
deformauniformeoprodutointeiro.Ousuárioseacostumacomoselemen-
tos,seusfuncionamentosecomportamentos.Todosessespontosjuntosfor-
mamumpadrãodeusoimportanteparaqueousuárionãosepercadurante
ofluxo.
29

## Página 36

3.7. SobreFrameworksCSS CasadoCódigo
Produtividade e manutenção
Seocódigodetodososmódulosjáexiste,aconstruç ãodeumanovatela
émuitorápida.Nãoénecessáriaaajudadedesignersotempointeirojáque
háumpadrãodeinterface. Amanuten çãodecódigoémínimajáquevocê
conseguecontrolartodososmódulosdeformaindividual.
Seosback-endsprecisamfazerpequenasmodificaçõesnatela,comuma
documentaçãobemfeita,elesconseguemsevirarsemaajudadefront-end
oudotimedeUX.Issoéimportanteparaqueexistaomínimodeburocracia
narotinadaequipe.
Por que não criar um framework?
Emborahajabonsmotivosparacriarmosnossoframework,hátambém
cenáriosruinsquevocêprecisarelevar:
Layouts diferentes
Nãoaconselhoacriarumframeworkparaumwebsiteinstitucional,um
hotsiteouumsitepequeno. Websitestêmtelasmuitodiferentesumasdas
outras,nãohámaneiradecriarumframeworkqueseadequeatodososde-
signs.Porisso,seastelasdoprojetosãototalmentediferentes,semrepetiç ão
deelementos,sempadrãovisual,acriaçãodeumframeworkpodetrazermais
problemasdoquesoluções.
Código que não para de crescer
Paragrandesprojetos,vocêprecisaterumplanejamentoparaprevenira
quantidadedecódigoqueseuframeworkgera.Seseuframeworkétãogrande
quecomeçaaprejudicaraperformancedosistema,algoestáerrado.Seule-
gadonãodeveestarsendobemgerenciadoevocêpodeestarmantendocó-
digomortonoprojeto.
T empo inicial
Paraconstruirumframeworkdozero,vocêprecisaráterotempodasua
equipeetalvezdeoutrasequipesparadecidiraideiainicialdoframework,
30

## Página 37

CasadoCódigo Capítulo3. CSS
como:quaisproblemaseleiráresolver,quaistecnologiasserãousadas,padrão
decódigo,padrãovisualvindodotimedeUX,comoosback-endsusarãoo
framework,comoseráadocumentaçãoentreoutrospontosimportantes.Isso
alémdotempogastoinicialmenteparacodificarabasedoframeworketodo
odesenvolvimentoposterior.
Já existem outros frameworks no mercado
Tenteestudarasop çõesquejáexistem.Euseiquemuitoprovavelmente
nenhumframeworkdisponíveliráseadequaraodesigndoseuprojeto,mas
tenteconsiderarquetalvezvocênãoprecisedoframeworkinteiro;àsvezes
utilizarapenasoGRIDdeumdeterminadoframeworksejaosuficientepara
oseuprojeto.
3.8 S obre Style Guides
EmboraváriosStyleGuidessejamapresentadoscomoframeworks,umStyle
Guidetemumaideiaumpoucodiferente.UmStyleGuideéapenasumguia
paraserseguidopordiversasequipes.Elesnãotêmnecessariamenteelemen-
tosemódulosprontos,mastêmumadocumentaçãobemacabadaedefinida
dediversospontoscomotipografia,grid,cores,dimensõesemedidas.Mas,
comoeudisse,nãoháummóduloprontodebotões,háasespecificaçõesde
comoumbotãoserá.
Geralmente,osStyleGuidessãofeitospelosdesignersoupelotimede
UX.SãoelesquedetêmosPSDs,osWireframeseoutrasinformaçõessobre
ainterface.Esteéumpontoimportanteaseconsiderar.Existemequipesde
UXquenãofazemessadocumentaç ãoeemmuitoscasosesseéoproblema
deinterfacesmalacabadas,comtipografiatoscaeoutrosproblemas.
Vejaporexemploo brand toolkitdaMozilla(bit.ly/mozilla-styleguide),
quemostracomoequipeseparceirosdevemtratarobrandeoestilovisual
doselementosdewebsitesligadosàempresa.
Estilosdedesignepadrõesdecódigosãoumamaneiraimportantedese
certificardequeainterfaceseráconsistente. Muitasvezes,doStyleGuide,
surgemframeworksbemacabadosecompletos.
Querumexemplo? VejaoStyleGuidefeitopelopessoaldaBBC: http:
31

## Página 38

3.9. Leiturarecomendada CasadoCódigo
//www.bbc.co.uk/gel
Exemplos de frameworks usados em empresas
Umasériedegrandesempresastemseusprópriosframeworks.Sãocom
elesqueaconsistênciadelayouteinterfaceconseguemperdurarentreequipes
ediversosprojetosinternos.Confiraalgunsframeworks:
•Locaweb Styleéumframeworkfeitopelaequipequeeucoordeneina
Locaweb. ElecontemplatodososprojetosinternosdaLocawebeos
produtosusadosportodososclientes. Comoéumframeworkopen
source,tambémpodeserusadoporqualquerumforadaLocaweb http:
//locaweb.github.io/locawebstyle/
•Y elp!:http://www.yelp.com/styleguide
•The Guardian:https://github.com/guardian/frontend
•Style Guide e Design StandardsdosetordetransportepúblicodeLon-
dres:bit.ly/london-transporte-design-standards
•West Virginia University:http://brand.wvu.edu/
•Style Guide e Design Patterns daIBM: http://www.ibm.com/design/
language/index.shtml
•Apple Human Interface Guidelines:bit.ly/apple-human-interface
Segueumsitecomexemplos,artigoselivrossobreStyleGuidesefra-
meworks:http://styleguides.io/
3.9 L eitura recomendada
Continueseusestudoscomoslinksaseguir:
• IntroduçãoaoCSS3D ExemplodeCardFlip http://tableless.com.br/
introducao-ao-css-3d-flip-card/
32

## Página 39

CasadoCódigo Capítulo3. CSS
• CSS modular: construindo front-ends flexíveis e escaláveishttp://
www.infoq.com/br/presentations/css-modular
• ModulandooCSShttp://tableless.com.br/modulando-o-css/
• PrincípiosparaescreverCSSdeformaconsistentehttp://tableless.com.
br/principios-para-escrever-css-de-forma-consistente/
• 6estratégiasparamelhoraraorganizaçãodoseuCSS http://tableless.
com.br/6-estrategias-para-melhorar-a-organizacao-do-seu-css-2/
33

## Página 41

Capítulo4
Umpitacosobreeditores
Editoressãoaprincipalferramentadosdesenvolvedores.Énoseueditorque
vocêvaipassarboapartedoseudia.Mesmoassim,muitosdesenvolvedores
nãogostamdeperderumaouduashorasaprendendosobresuaprincipalfer-
ramentadetrabalho.Éaíquemuitosperdemaoportunidadedesetornarem
produtivoseágeisnastarefasdiárias.
Entendercomoseueditorfuncionaéessencial.Saberquaissuaslimita-
ções,atéondevocêpodeestendersuasfuncionalidades,conhecerquaisplu-
ginsfacilitamoseuprocessodetrabalhoetc. Porisso,quandoescolherseu
editordocoração,passeumtempocomele,aprendendoseusmeandrose
conhecendoseustruques.
Nãoimportaqualeditorvocêvaiusar.Euvouexporminhaopiniãosobre
oseditoresWYSIWYGnapróximase ção,masessaéminhaopinião.Sevocê
quiserusarumeditorassim,nãoháproblemanenhum,contantoquevocête-

## Página 42

4.1. EsqueçaoseditoresWYSIWYG CasadoCódigo
nhacontrolesobreseucódigofinal.Aregrabásicaé:quemmandanocódigo
évocêenãoseueditor.
4.1 E squeça os editores WYSIWYG
QuerodeixarclaroquenãosoucontraDreamweaver. Euatéusavaquando
estavainiciandonaárea. OproblemadoDreamweaveréqueelenãoajuda
noaprendizado.Eleviraumamuletacomopassardotempoevocêviraum
desenvolvedormalacostumado.Issofazvocêpararnotempo.
ODreamweaverdecertaformaajudoubastanteodesenvolvimentoweb.
Quandoastabelassetornarampopulares,omodoWYSIWYGdoDreamwe-
avereraimprescindível.Comoninguémfaziawebsitesdecentes,escreverta-
belasnaunhaeraumparto. ODreamweaver,porsuavez,facilitavatodoo
processoemtemposdetabelasaninhadas,comcódigoinútilewebsitescom
obesidademórbida.
Durantemuitotempo,oDreamweaverformougeraçõesegeraçõesde
desenvolvedoreseempresas. ErarealmenteoeditorquematariaoFront-
Page... QueDeusotenha. ODreamweaverconseguiuserumdoseditores
maispopularesnasuaépoca.Eleerarealmentecompleto.
Comaprofissionalizaçãodaárea,maisemaisdesenvolvedorescome ça-
ramaescreverseuscódigosmanualmenteeoDreamweavercome çouaper-
dermercado.Qualquerumqueficasseumpoucomaisespertopercebiaque,
apesardasfacilidades,comotempoocódigoautomáticosetornavaumpé
nosacoeamanuten ção,impossível. Atéentão,todooprocessodeatuali-
zaçãodecódigo(leia-seFTP)ajudavaoDreamweaveraficarnalideran ça.
EuouviadiversosdesenvolvedoresdizendoqueoDreamweavereramatador
simplesmenteporcausadafacilidadedeacessaroFTPemudarocódigodos
arquivosdiretonoservidor.Atéhojelembrodomedoqueissomecausava.
EditoresmaissimplesemaispoderososqueoDreamweaversurgiram.
HomesiteeEditPluseramosmeusprediletos. Aescolhadoeditordetexto
étotalmentepessoaleporissoeunãovouficarchateadosevocênãogostar
daminhaindicaçãoaqui,queéoSublimeText.Maséminhaobrigaç ãodizer
queoSublimeTextéusadopelamaioriadosdevsatualmenteatéoanode
2015.
36

## Página 43

CasadoCódigo Capítulo4. Umpitacosobreeditores
Sendomaisespecífico:oDreamweaveréumsímbolo.Qualquereditorou
ferramentaquevireumamuletaparaodevéalgoruim.Vocêprecisadigitar
eentenderdecaboaraboosignificadodocódigoescrito.Sevocêtemuma
ferramentaquefaztudosozinha,vocênãoéumdesenvolvedor,vocêéapenas
umoperadordesoftware.
Procuresempreproduzirseucódigomanualmente. Sevocêestácome-
çandoetemalgumeditorcomooSublimeText,queficaautocompletando
tudooquevocêescreve,desabiliteessafun ção,pelomenosporenquanto.
Issovaiobrigá-loapesquisar,aprocurararesposta,vaifor çá-loalembrar
daquelenegóciodequevocêesqueceu.Issovailhefazerpensar.
Não,issonãoquerdizerquevocêprecisaaprenderVIMparapoderse
transformaremumdevcool. Longedisso. OVIMémuitolegal,massua
curvadeaprendizadoébastantelonga. Vocêatévaisetornarbastantepro-
dutivocomele,masachoquesevocêestáiniciandonessaárea,nãocomece
peloVIM.
4.2 Sublime Text
OSublimeTextéhojeoeditormaispopularentrequalquerumquedigite
código.Nãoporqueeleésimplesaomáximo,masporcausadafacilidadede
personalizaçãodefun çõeseinterface.
HáumaquantidadeenormedepluginsparaSublimequeajudamame-
lhoraraprodutividadedoseudesenvolvimento,seguemalgunsdeles:
•Package ControléumgerenciadordepluginsparaSublime.Vocêcon-
segueprocurareinstalarpluginsdiretamentepeloseueditor,semter
quebaixararquivosexternosnemnada.Aconselhoinstalá-loprimeiro
antesdeinstalarosoutrosplugins.Vaifacilitarsuavida.
•GitStatusmonitoramudançasdearquivosestatusdoarquivonorepo-
sitóriodoprojeto.
•Emmetdásuporteaofamosoevelhoex-ZenCoding.
•EditorConfigfazoSublimereconhecero .editorconfigcomas
configuraçõesdeformataçãodosarquivos.
37

## Página 44

4.2. SublimeText CasadoCódigo
•SideBarEnhancementscolocaumasériedenovasop çõesnomenucon-
textualdasidebarfacilitandoogerenciamentodearquivosdiretodo
editor.
•SassdásuporteahighlightdesintaxedoSassparaSublime.
•AngularJStrazsnippetsparaquemgostadeAngularJS.
ExisteumasériedeoutrospluginsnoPackageControlquepodemser
instaladosagoranoseuSublime,alémdeváriasoutrasfuncionalidadesqueo
transformamemumeditorbastantepoderosoeprodutivo.
Suas preferências
UmadasprimeirascoisasquevocêprecisasaberéqueoSublimeguarda
suaspreferênciasemumarquivoemformatoJSON,porissoébemfácil
deentender. Osdoisarquivosquevocêprecisasaber: umparaseusata-
lhosdeteclado,queficaem Sublime Text 2 > Preferences > Key
Bindings - User eoutroparaasdefiniçõesgerais,em Sublime Text
2 > Preferences > Settings - User ou CMD + ,.
Nessesdoisarquivosvocêmudaoquequiser. Sevocêtiverquemudar
qualquercoisa,lembre-sedemudarsemprenoarquivode USER,queéoseu
arquivo.Assimvocêmantémasdefiniçõesdefaultintactas.
Umasacadaécolocá-losdentrodasuapastadeDropbox,noGITouem
qualqueroutrolugar,deformaquevocêconsigarecuperá-losquandoforma-
taramáquinaouquandoquiserconfiguraroSublimeemoutrocomputador.
EucoloqueiosmeusdentrodeumapastanoDropboxefizumlinksimbólico
paraoSublime.
Sevocêquiserdescobrironomedeumdeterminadoatalhoreferentea
umcomandodeteclado,bastaabriroconsoledoSublimecomoatalho CMD
+ ‘ eacadacomandodetecladoquevocêexecutar,vocêveráonomedo
comandoreferenteaesteatalho.
Lista de comandos
Sublimetemmuitoscomandosescondidosquepodemnãoestarlistados
38

## Página 45

CasadoCódigo Capítulo4. Umpitacosobreeditores
nosmenus.Vocêpodeacioná-lospelocontroledeacesso CMD + SHIFT +
P.Lindo,não?
GoT o Anything
Querencontrarfun ções,classesouIDsdentrodosseusarquivos?Useo
atalho CMD + P.EssecomandoabreosearchgeraldoSublime.Nessesearch
vocêpodeprocurararquivos,comonoexemploanterior,ousevocêiniciara
buscacomum @,vaipossibilitaraprocuradefun ções,classes,IDsetc. no
arquivoaberto.
Sevocêquiserirparaumalinhaespecífica,vocêpodecome çarabusca
com :(doispontos)ecolocaronúmerodalinha,ouaindauseoatalho CTRL
+ G enúmerodalinha.
NãovoupassartodasasdicassobreSublimeTextaqui,issomereceum
livrooupostgigante.Masvocêpodeencontrarmuitacoisaútilnesseslinks:
•http://simplesideias.com.br/configurando-o-sublime-text-2
•http://tableless.com.br/7-plugins-sublime-text-que-voce-deveria-conhecer/
•http://tableless.com.br/dicas-truques-sublime-text/
•https://github.com/fnando/sublime-text-screencasts
4.3 O utros editores
Sim,euindicooutroseditoresalémdoSublimeText,sãoeles: Bracketse
Atom.
Brackets by Adobe
OBracketséumeditorcriadopelaaAdobe,parafazerpartedoseunovo
pacotedeferramentasparadesenvolvimentochamadaAdobeEdge. Sóque
aAdobe,aocontráriodasuaantigacultura,disponibilizouocódigo-fonte
soblicençaMIT.DesdeentãoocódigoabertoéencontradoviaGitHubeé
39

## Página 46

4.3. Outroseditores CasadoCódigo
mantidopelacomunidade.OBracketséescritoemHTML,CSSeJavaScript,
oqueébastanteinteressante.
Bracketsémeusegundoeditorpredileto. Emboraeuoacheumpouco
maislentoqueoSublimeText,asfeaturesqueelevemadotando,principal-
menteemparceriacomaAdobe,sãomaravilhosasetotalmentefocadasem
produtividade.
UmadasfeaturesquetemodedodaAdobeéoExtract,umserviçodo
CreativeCloudequenoBracketséalgonativo.Aideiaésimplesmenteassim:
vocêsobeumPSDparaoExtract,eleabreoPSDemumainterfacediretodo
seubrowser.Vocêclicanoselementosdetexto,coretc.eoserviçolhepassao
códigoCSS.Ocódigoébastanteenxuto.Soubastantecontracoisasquefazem
códigosfront-enddeformaautomática,masesteestáindonocaminhocerto.
MesmoassimvocêpodeusaresseserviçosemutilizaroBrackets.
LeiamaissobreoBrackets:
• Siteoficialhttp://brackets.io
• ExtractforBracketshttp://www.adobe.com/br/creativecloud/extract.
html
• GitHubdoprojetohttps://github.com/adobe/brackets
Atom by GitHub
OAtomfoifeitopelopessoaldoGitHubeoseuprincipalapeloéainte-
graçãoentreoeditoreoserviçoGitHub.
ÉquaseimpossívelnãocompararoAtomcomoSublime.OSublimecra-
vouumpadrãocomseusshortcuts,suainterfaceesuacole çãodecomandos
queémuitodifícilignorar.OAtomtemacaradoSublime,diferentedoBrac-
kets,queébemdiferentetantonainterfacequantonosshortcuts. Façouso
doBracketsparaalgumascoisaseestougostandobastante. Masacurvade
aprendizado,quandoacostumadocomoSublime,émuitogrande. Como
Atomvocêjávaiconhecermeiadúziadeshortcuts,facilitandomuitoami-
gração.
OAtomseguiuomesmocaminho.ElepegoutudoqueerabomdoSu-
blimeeaindateveideiasoriginaisegeniaisparafacilitaraindamaisanossa
40

## Página 47

CasadoCódigo Capítulo4. Umpitacosobreeditores
vida.ÉcomoseoAtomfosseumanovaversãodoSublime.Édifícilatéde
pensaroqueoSublimemudariaparamelhorareatéconcorrercomoAtom.
Essasimilaridadeentreoseditoresnãoéruim. Masoquevaiimportar
mesmosãoasfeaturesextrasquecadaumpodetrazernofuturo. Descrevi
algumasfeatureslegaisquemechamarammaisaaten çãoequesediferenciam
totalmentedoSublime.
NoAtom,apersonalizaçãodainterfaceémuitomaisfácil,jáqueéfeita
viaCSS.Sim,CSS.Seguindoomenu Atom > Open Your Stylesheet,
oAtomabreumarquivoCSSondevocêcustomizaoquequisernatela.
Mudacordetexto,font,background,margin,padding,Tudo.Aívemaper-
gunta:mascomovousaberoselementosquedevoformatar?Simples,abra
umInspector.Sigaomenu View > Developer > Toggle Developer
Tools.OInspectorqueseabreéopadrãodoWebkit.
UmacoisadequesintofaltanoSublimeéumapartedeconfigurações
ondeeupossamudaroqueeuquisernoEditor.OAtomtemumaáreadessa,
muitobemacabadaeorganizada.NoSublimevocêmudaessaspreferências
diretonosarquivosdeconfiguraçãodoeditor.Issoégenialnaprimeiravez,
masdepoisvocêsentealgumafaltadeapertarbotões,saberquetudoestáfun-
cionando,tercertezadequenãoalterounadaquevádestruirseusshortcuts,
temaeoutrasconfigurações.JáoAtomtemessateladeconfigurações,como
qualqueroutroprograma.Nele,vocêgerenciaospackages(plugins),temase
shortcuts.
OinteressantenoAtoméquetudoétratadocomomódulos. OAtom
chamaseuspluginsdePackages.Estespackagesfazempartedasconfigura-
çõesdoeditorousãoapenaspluginsqueestendemasfuncionalidadesjáexis-
tentes.TodosessespackagessãomódulosindependenteseestãonoGithub,
prontosparaseremforkados,compartilhadosetc.
SeguemdoislinksqueexplicamessaseoutrascoisasmaisnoAtom.
• Atom, o novo editor do GitHub http://tableless.com.br/
atom-o-novo-editor-github/
• PrimeirasimpressõesdoZenocomoAtomhttp://www.youtube.com/
watch?v=5BwwUnJVIIs
41

## Página 49

Capítulo5
Cuidandodoseucódigo
5.1 E squeça o FTP
Simplesmenteesqueça.NinguémmaisusaFTPparaatualizarseucódigoem
produção.
OprotocolodeFTPéalgomuitosimplesedurantemuitotempocumpriu
bemseutrabalho.Masapartirdomomentoemquevocêprecisagerenciar
bemolegadodecódigodoseusistema,elepassaanãoserumaboaalternativa
porváriosmotivos.
Entendaqueoseufluxodedeploydeveserseguro. Algumasempresas
burocratizamoprocesso,outrastentamsimplificaromáximopossível,mas
todasdevemseateraseguran çadefazerrollbackouatualizarocódigoem
produçãosemperigose,sepossível,demodoautomatizado.
ComovocêfazodeploydeumsiteinteirocomFTP?Nãoimportaota-
manhodosite,vocênuncasabeexatamentequalarquivofoimodificado.Na

## Página 50

5.2. Sobrecontrolesdeversão CasadoCódigo
dúvida,vocêacabacopiandotodososarquivos,paranãotererro.Issotudo
manualmente.AlgunsclientesdeFTPtentamfazerumasincronizaç ãocom-
parandodatademodificaçãoetamanhodearquivo. Masgeralmenteessa
comparaçãodemoramuitoenãoéconfiável.
Hátambémanecessidadede,poralgummotivo,vocêprecisarvoltarao
cenárioanteriorcasoalgodêerradonatransferênciadosarquivos. Sevocê
nãofezumbackupantesdecopiarosarquivos,vocêvaiterumproblemão.
Usarumcontroledeversãoéalgoindispensávelnosdiasdehoje.Épor
issoqueeudigopravocê:paredeusarFTPeaprendaGITouqualqueroutro
sistemadecontroledeversãocomoSVNouMercurial.Euegrandepartedos
devspreferimosGIT.Hojeeleépadrãodemercadoemuitoprovavelmente
vocêvaiesbarrarcomelenasempresasemquevocêtrabalhar.
5.2 S obre controles de versão
Vocênãoprecisatrabalharemumaequipegrandeparasaberqueháumpro-
blemaparacontrolarocódigodoseuprojeto.Pararesolverissoexistemsiste-
masquecontrolamseucódigo,monitorandocadamudan çaejuntandotodas
asmodificaçõesdeformaquenãoocorramconflitosquandoduaspessoas
editamamesmalinhadeummesmoarquivo.
Durantemuitotempo,ocontroledeversãomaisconhecidoeraoSVN
(ApacheSubversion). IssomudoudepoisqueoGIT,criadoporLinusTor-
valds,chegou.ExistemoutroscontrolesdeversãocomooBazaarouoMer-
curial,masoquevocêprecisasabermesmo,atéodiaemqueestouescrevendo
estetexto,éoGIT.
O básico sobre qualquer controle de versão
Esteéobásicoquevocêprecisasaberparaentenderqualquercontrolede
versão.Apartirdaqui,vocêestaráseguroparasaberpelomenosofunciona-
mentobásicodequalquercontroledeversãoatéentão.
Branchs e Trunks
Aúltimarevisão,amaisatual,normalmenteéchamadade HEAD.Exis-
temmomentosondeteremosvários HEADspoisoprojetotemvários BRAN-
44

## Página 51

CasadoCódigo Capítulo5. Cuidandodoseucódigo
CHES.Umbranchéumacópiadoprojeto.Cadabranchpodesereditadoe
evoluídoindependentemente.
Fig.5.1:Branchssãocomogalhosdeumaárvore.
Imaginequeexistaaversãodeproduç ão,queéaquelaqueestánoar.É
aversãoqueousuárioestáutilizando.Nãoéaversãomaisatual,poisamais
atualéaqueestánasuamáquina,masaversãoqueestáemproduçãoé(oude-
veriaser)aversãomaisestável.Essaversãoestánumabranch,normalmente,
chamada MASTER.NemsempresechamaMaster,dependedaequipe. Há
pessoasquechamamdeProd,porexemplo.
Versionamento
Versionamentoéumadascaracterísticasmaisbásicasdocontroledecó-
digo.Quandocomeceiadesenvolver,normalmenteeutrabalhavaguardando
pastascomnomesdotipo nomeDoProjeto-v1, nomeDoProjeto-v2etc. Estas
pastasguardavamapenasasversõescomgrandesmodificaçõesdeprojeto,
algocomomudan çageraldelayout,umafeatureimportanteoualgodotipo.
Oproblemasãoaspequenasedições.Quandojuntamosaspequenasmodifi-
cações,temosumagrandemodificação.Émuitoprovávelque,sevocêperder
essaversão,vocênãoselembredetodasaspequenasmodificaçõesfeitase
issoémuitoinconveniente.Eunãotenhosaudadesdessaépoca.
Emumsistemadecontroledeversão,todavezqueodesenvolvedorter-
minaumadeterminadatarefa,elegeraum commit.Ocommitéondeode-
senvolvedoratrelaasmodificaçõesdocódigocomumaexplicaç ãoexatado
queelefeznaquelatarefa. Cadacommitgeraumaversãodoseucódigo. A
graçaéquesevocêtemversõesdocódigo,praticamenteumundogigantedo
45

## Página 52

5.2. Sobrecontrolesdeversão CasadoCódigo
seuprojeto.Sedepoisdeumadeterminadamodificaç ão,dequalquerumda
equipe,seuprojetocome çouaapresentarproblemas,bastavoltarasversões
atéencontrarexatamenteemqualdoscommitsosproblemasiniciaram.Você
temumlogcompletodospassosdoprojeto.
Euconfessoquenoinícioeuachavamuito,masmuitochatoterquees-
crevercommitscomexplicaçõessobreasmudan çasquefiznaquelatarefa.Eu
achavaqueestavaperdendotempo,quetudoeramuitoburocráticoechato.
Masdepoisquepercebiovalornesseprocesso,comeceiaescrevercommits
maiselaborados.Oquenoslevaaopróximotópico:Log.
Log
Acadacommitfeito,odesenvolvedoradicionaumamensagemexpli-
candooqueelefeznaquelatarefa. Éimportantequeessamensagemseja
claraericaemdetalhes,masnãoumtextogigante,apenasosuficientepara
quevocêmesmoououtraspessoasenvolvidasentendamoqueaquelasub-
missãosignifica.
Issopodeservircomodocumentodepois,facilitandoquenovosintegran-
tesdaequipeentendamohistóricodoprojetoeparaqueaequipeinteiraesteja
cientedasmodificaçõesfeitaspeloscolegas.
Existemequipesquelevamtãoasérioasdescriçõesdoscommits,queo
logdoprojetosetornaumaverdadeiradocumentaç ãodoprojeto.Vocêcon-
segueentenderquaisforamospassosdecadadesenvolvedor,quaisosproble-
masresolvidosequaissoluçõesaplicadas.
Diffs
OsDiffssãocomparaçõesdasmodificaçõesfeitasnocódigo,mostrando
todasasalterações,dele ções,inserçõesetc. Écomoagentecomparaduas
versõesdeummesmocódigo.VejaumexemplodiretodoGitHub:
46

## Página 53

CasadoCódigo Capítulo5. Cuidandodoseucódigo
Fig.5.2:VisualizandoumGitDiffnoappdoGitHub.
HátambémapossibilidadedefazerumDiffviaconsole. Eu,particu-
larmente,nãogosto.Ainterfaceébastanteruimeconfusa.Sevocêutilizar
serviçoscomoGitHubouBitBucket,prefiraasversõesdeDiffdeles. Vejaa
seguircomosepareceoDifffeitopeloGITdiretopeloterminal:
Fig.5.3:GitDiffdiretopeloterminal.Coisafeia,né?
Merge
Lembro-medeequipesinteirasperdendoarquivosepartesdecódigopois
doismembrosabriamomesmoarquivoparaeditar.Obviamentenunca,mas
nuncadavacerto.Issofaziacomquegrandesequipescriassemmecanismos
daidadedaspedrasparaavisarorestodopessoalquedeterminadoarquivo
estavasendousado.Otrabalhoremotonuncaerapossível.Comocontrole
deversãoissomuda.Qualquerumpodeeditarqualquerarquivoaqualquer
hora.
Osistemadecontroledeversãocomparaasmodificaçõesfeitasnoar-
47

## Página 56

5.2. Sobrecontrolesdeversão CasadoCódigo
• Iniciando com GIT Parte 2 (http://tableless.com.br/
iniciando-no-git-parte-2/)
• Contribuindo para projetos Open Source (http://tableless.com.br/
contribuindo-em-projetos-open-source-com-o-github/)
• Livro: Controlando versões com Git e GitHub (http://www.
casadocodigo.com.br/products/livro-git-github)
50

## Página 57

Capítulo6
JavaScript
Vocêpodedividiraslinguagensfront-endem3(atéagora): HTML,CSSe
JavaScript. Durantemuitotempo,oJavaScriptestevelongedosholofotes.
Muitosprogramadoresnãoseaprofundavamosuficientenalinguagem,mas
osquefaziamseapaixonavam.ComooHTMLeoCSS,oJavaScriptpassou
pormomentosruinsnaguerradosbrowsers.Massemprefoiumalinguagem
pioneira.
Comováriaslinguagens,oJavaScripttemváriassoluçõesparaumúnico
problema.Serumalinguagemflexíveltemsuasvantagensedesvantagens,por
issoéimportantequevocêleiamuito,muitosobrepatternseostruquesque
alinguagempodeguardar.
EunãoqueromostrarparavocênestecapítuloquaisAPIs,fun çõesetéc-
nicasvocêdeveaprender.Masabordeidoisassuntosimportantes:jQuerye
Patterns.MuitosnovatosnempensamemestudarDesignPatternsdoJavaS-
criptquandoestãoiniciando.

## Página 58

CasadoCódigo
OJavaScriptganhoutantofoconosúltimosanosquesurgiramdiversas
iniciativas.Algumasdelastrouxeramnovasideiasemelhoriasparaalingua-
gememsi,outrasforamapenasfogodepalha.Oimportanteéquealingua-
gemevoluiumuito. AversãoES6estáprestesaserlan çadaoficialmenteno
momentoqueestelivroéescrito,comimportantesnovidades.
Naminhaopinião,oquefezcomquepessoasolhassemofront-endde
formadiferentefoioJavaScript.Deumahoraparaoutra,umasériedeinicia-
tivassurgiramederepentetodomundoconcordouqueoJavaScripterauma
linguagemmaravilhosa.Principalmenteosdevsback-end,queachavamque
anossaáreaerasóescreverHTMLepintarquadradinhoscomCSS.
ONode.jsabriuosolhosdemuitagentequenãodavanadaparaessemer-
cado,trazendograndesoportunidades.Vocênãoprecisaseaprofundarnesse
assuntoagora,masébomsaberquealgumahoravocêvaiusaralgobaseado
emNode.js,sejaumgeradordesiteestático(queabordamosaquinestelivro
também)ouumframeworkcomoBackbone.ONode.jséuminterpretador
deJavaScriptquepermiterodarcódigoJavaScriptnoservidor.Issoébome
ruim.ÉmuitopolêmicoaindaescreverJSnoservidor.Empresas,principal-
mentebrasileiras,aindaestãoperdidasquantoaisso.
Meuconselhoaquié:nãoqueiraaprendernadasevocênãovaiusaragora.
Claro,nãoestoudizendoquenãoprecisaestudar,pelocontrário. Vocêvai
estudarcoisasmaisimediatas,quevãomelhorarsuaprodutividade.Sevocê
nãovaiusarBackboneagora,sóaprendase quiser (ou precisar).
Alémdisso,umdevfront-endnãoésóaquelequeescreveJavaScript.En-
volvemuitomais. Naverdadeesseéoutroproblema. Paramimnãoexiste
front-end,existedesignereprogramador.Masestaéoutrahistória.
Sevocêfornovato,nãofiqueafobado.VocênãoprecisaaprenderBack-
boneouqualqueroutracoisaparasetornarumdesenvolvedorfront-end.
Essaáreacresceutantoqueháespaçoparatodomundo. Éclaroquevocê
nãovaiescapardeescreverJavaScript,vocênãoprecisasabertudo,maspre-
cisaentenderobásico.
52

## Página 59

CasadoCódigo Capítulo6. JavaScript
6.1 A prenda pelo menos o básico de Jav aScript
Édifícilentenderqualéestebásicoquevocêprecisaaprender.Tudodepende
doseuobjetivo.Sevocêtemumatendênciamaisparaodesign,aprendero
básicotalvezsignifiqueaprenderosuficienteparamanipulareventosecom-
portamentosdoDOM.Sevocêestámaisparaserumprogramador,oseu
básicosignificaaprendermuitosobreorientaçãoaobjetos,JSnoservidor,
patternsetc.
Tudovaidependertambémdeondevocêtrabalha.Sevocêtrabalhaem
umaagênciaweb,suasnecessidadesdeJavaScriptsãodiferentesdeumaem-
presaquefazprodutoparaweb.Talveznaagênciasejainteressantesefocar
emcomportamentoseanimação,jáquevocêvaifazerpe çasdelayoutsin-
terativos. Emempresasdeproduto,vocêvaiprecisarentendermaissobre
arquitetura,talvezumpoucosobrealinguagemserver-sideutilizada,como
manipularbemarquivos json,fazer ajaxdeformadecente.Sãodiferentes
necessidades.
Porisso,nãoqueiraaprendertudoqueaparecenasuafrente.Estejabem
atentoaocontextodaempresaemquevocêtrabalhaeprincipalmentenopro-
jetoatual.Mesmoassim,existemalgunspontosquesãocomunsemqualquer
lugarqueuseJavaScript.TenteiabordaraquiumpoucosobreEscopodeva-
riáveisebempouco(mesmo)sobrePatternsdoJavaScript,mostrandoapenas
oModulePattern,queébemfácildeentender.
6.2 E scopo de v ariáveis
Variáveiséumadasprimeirascoisasquealguémaprendequandoestáco-
meçandoaprogramar.Elasestãoemtodasaslinguagensdeprogramaç ãoe
muitasvezes,emborasejamfáceisdeentender,causamconfusãoparaquem
estáiniciando,principalmentequandosetratadeescopo.
Voutentarseromenostécnicopossívelaqui,masnãodáparamostrar
comofuncionaescopodevariáveissemterquemostrarumpoucodecódigo.
Imagineasvariáveiscomocaixinhas.Cadacaixinhadessatemumnome
quevocêdeuevaiguardarumdeterminadotipodedado. Comoemuma
caixanormal,vocêpodesubstituirseuconteúdonahoraemquequiser. O
problemaéquevocênãopodeusarumavariávelseelaestiverforadocon-
53

## Página 60

6.2. Escopodevariáveis CasadoCódigo
texto,oucomopodemosfalar,foradoseuescopo.Existemdoistiposdees-
copo:globaloulocal.
Quandoumavariávelécriadaforadasfun çõesdasuaaplicação,elaé
chamadade variável global.Avariávelglobalsempreestarádisponívelpara
serusadaportodaaaplicaçãoeporqualquerfun çãocriada.
Quandovocêtemumafunção,quefazumatarefaespecífica,edentroela
háumavariável,essavariáveltemoquechamamosde escopo local,epoderá
seracessadaapenasporessafun ção.
Segueumcódigobemsemvergonhaparamostrarcomofuncionaessa
coisatoda.Primeiro,vejaoexemplodevariávelglobal:
var varGlobal = 'Variável Global';
console.log(varGlobal);
// log: Variável Global
Agora,emumescopodefun ção:
var varGlobal = 'Variável Global';
console.log(varGlobal);
function umaFuncao() {
var outraVar = 'Uma outra variável';
console.log(outraVar);
}
umaFuncao();
// log: Variável Global
// log: Uma outra variável
Ótimo, até aqui sem problemas. Se eu tentar chamar um
console.log(outraVar) fora da função umaFuncao(), veja o
queacontece:
var varGlobal = 'Variável Global';
console.log(varGlobal);
54

## Página 61

CasadoCódigo Capítulo6. JavaScript
function umaFuncao() {
var outraVar = 'Uma outra variável';
console.log(outraVar);
}
umaFuncao();
console.log(outraVar);
// log: Variável Global
// log: Uma outra variável
// log: outraVar is not defined
Obrowsernãoconsegueencontraro outraVarporqueelaéumavariá-
vellocal,seuescopoestáapenasdentrodocontextodafun ção.
Masháumporém:percebaquesempreantesdenomearasvariáveiseu
coloqueiapalavramágica var. Quandodefinimosissoemumavariável
dentrodeumafun ção,estamosexplicitandoqueaquelavariávelélocal.Seeu
retiraro vardedentrodafun ção,seuescopopassaaserglobal.Nocódigo
aseguireusimplesmenteretireio vardafrentedavariável:
var varGlobal = 'Variável Global';
console.log(varGlobal);
function umaFuncao() {
outraVar = 'Uma outra variável';
console.log(outraVar);
}
umaFuncao();
console.log(outraVar);
// log: Variável Global
// log: Uma outra variável
// log: Uma outra variável
Issoébastanteperigosoporque,emumcódigomuitogrande,ondetoda
aequipeestátrabalhandojunto,ovalordavariávelpodesermodificadapor
qualquerfunçãodoprojeto.Eupossofazerumavariávelcomomesmonome
55

## Página 63

CasadoCódigo Capítulo6. JavaScript
• Patternsprovamsoluções.
• Patternspodemserfacilmentereutilizados.
• Patternspodemserexpressivos.
Quandoolhamosumpattern,vocêencontraumaestruturaeumvoca-
bulárioqueajudamaexpressarumasoluç ãodeformaelegante. Nãoésó
escrever,fazerfuncionarepronto.Éescreverdeformaquenãoapenasvocê,
masqualquerum,anosdepois,entendacomoaqueledeterminadoproblema
foisolucionadoeporquefoisolucionadodaquelaforma.
Mesmoassim,terumpatterndefinidonoseuprojetonãoquerdizerque
eleéumasoluçãoexata.Vocêpoderiaterresolvidoesseproblemacomoutro
patterneoutraestrutura.
Decara,issoparecesercomplicado. Masnãoé. Aprenderumpattern
JavaScriptpodelheensinarmaissobrealinguagemdoquemuitocursinho
poraí.
Module Pattern
EucostumousaremmeusprojetosumpadrãochamadoModulePattern.
Eleébastantesimplesdeentendereémuitoflexívelparaprojetosdetodosos
tamanhos.EleéumpatternbastanteusadoemprojetoscomojQuery,Dojo
eoutros.
OModulePatternéobásicoparainiciarseuentendimentosobreencap-
sulamentoemodularizaçãoemJavaScript.Ointeressantedessepatternéque
elereduzoescopoglobaldevariáveis.Porissoserámuitodifícilterproble-
masrecorrentesdeescopodevariáveisglobaisemprojetosgrandesoucom
muitosintegrantesnaequipe.Essacaracterísticapermitecriarcontextospri-
vados,ondeasvariáveisefun çõessãoacessadasapenasdedentroenãode
foradafun çãoprincipal. Suautilizaçãoébastantesimples. Nãovouentrar
nosmínimosdetalhespoisalgunsconceitos(closures,fun çõesanônimasetc.)
podemsercomplicadosparaquemestácome çando,mashálinksnofinaldo
textoquevocêpodeseguirparaentendermaissobreseufuncionamento.
Percebaocódigoaseguir:
57

## Página 64

6.3. ModulePatternJavaScript CasadoCódigo
var contador = (function() {
var placar = 0;
function mudaPlacar(valor) {
placar += valor;
}
return {
aumenta: function() {
mudaPlacar(1);
},
diminui: function() {
mudaPlacar(-1);
},
valor: function() {
return placar;
}
}
})();
Tudo sempre em inglês
Euuseiosnomesdasfun çõesemportuguêsnesteseemoutrosexem-
plosparaquevocêtenhafacilidadedeentenderaexplicaç ão.Masame-
lhorpráticaécodificartudoeminglês,ouseja,éimportantequenomes
devariáveis,funçõeseatécomentáriossejamescritoseminglês.
O contadoréumavariávellocalquearmazenaumfun çãoanônima,
queseseráautoexecutadaassimqueodocumentoterminardecarregar. A
função mudaPlacareavariável placarsãoprivadas.Apenasasfun ções
queestãodentrodo returnsãopúblicasepodemseracessadasporoutras
pormeiodafun ção contador,porexemplo: contador.aumenta()
Primeiro,crieumarquivo .jsecoloqueocódigoanterior.Depoiscrie
umarquivo HTMLecoloqueolinkdessearquivo JS.Feitoisso,abraesse
arquivo HTMLnoseunavegador.Agoravamosfazerumtesterápido.Digite
noconsole contador..Vejaqueelevaimostrartodasasfun çõespermitidas
paraexecução.
58

## Página 65

CasadoCódigo Capítulo6. JavaScript
Fig.6.1:Acessandoasfun çõespermitidaspeloescopo.
Fig.6.2:Asfun çõessãoexecutadasnormalmente.
Percebaqueafun ção mudaPlacar()nãopodeseracessadaouava-
59

## Página 66

6.3. ModulePatternJavaScript CasadoCódigo
riável placarnãopodeseralteradaanãoserporintermédiodasfun ções
aumenta, diminuie valor.
Semudarmosumpoucoaformacomoescrevemos,entramosemumou-
trotipodepatternchamado Revealing Module Pattern.Nessecaso,todasas
funçõesevaloresdomódulosãoacessíveisnoescopolocal.Ficaassim:
var contador = (function() {
var placar = 0;
function mudaPlacar(valor) {
placar += valor;
}
function aumenta() {
mudaPlacar(1);
}
function diminui() {
mudaPlacar(-1);
}
function valor() {
return placar;
}
return {
aumenta: aumenta,
diminui: diminui,
valor: valor
}
})();
EssepatternéumaboamaneiradetrabalharmoscommódulosnoJavaS-
cript.Modularizarfun çõesesuasdependênciaséumaformadereduziruma
sériedeproblemascomplexosquetemosnomomentododesenvolvimento.
Nósseparamosmelhorasfun çõeseseusinteresses.Amanuten çãotambém
ficabastantesimpleseconcentrada.
EuseiqueoModulePatternpodeintroduzirdeumavezvárioscontextos
60

## Página 68

6.4. AprendajQuery CasadoCódigo
Animações,manipulaçãodoDOM,incluireremoverclassesemuitasou-
traspequenastarefascorriqueirasnuncaforamtãofáceisdefazer.Masessa
facilidadetemseupre ço.MuitagentepulouoaprendizadobásicodoJavaS-
criptindodiretoparaajQuery.Vocêprecisaentenderquandoestáusandoa
linguagemoriginalouabiblioteca.Éimportantequevocêsaibaolimiteonde
acabaoJavaScriptecome çaajQuery.
Eu escrevi um artigo um pouco polêmico no Tableless um tempo
atrás com o títuloConsidere não usar jQuery (http://tableless.com.br/
considere-nao-usar-jquery/),quefalasobrevocêconsiderarousodeJavaS-
criptpuroemfun çõessimplesouemwebsitesondeacargadeJavaScriptnão
serámuitograndeequemuitoprovavelmentenãohaveráproblemasdecom-
patibilidadeentrebrowsers.
EunãoaconselhoanãousarjQueryemgrandessites.Nessecaso,apro-
dutividadequevocêganhaégiganteeoapoiodotimeéde100%. Porisso,
saibadosar. Paraprojetospessoais,sevocêpreferirseaventurar,váfundo,
masnavidareal,euaconselhoousodejQuerysempestanejar.
EporquejQueryenãooutrabibliotecacomooMooTools?Simples:co-
munidadeepopularidade.Praticamentetodososdesenvolvedoresconhecem
jQuery. Eleémuitopopulareéusadopormaisdametadedoswebsitesda
internet(http://blog.jquery.com/2014/01/13/the-state-of-jquery-2014/).
Paralermais:
•http://youmightnotneedjquery.com/
•http://tableless.com.br/considere-nao-usar-jquery/
•http://simplesideias.com.br/redescobrindo-o-JavaScript-com-jquery
•http://api.jquery.com/
62

## Página 69

Capítulo7
WebMobile
Osproblemasquetemoshojeaodesenvolverfront-endnãomudarammuito
daépocaemqueeucomecei,hámaisdeumadécadaatrás(ok,mesentium
malaeumvelhoagora). Masasvariáveiscomqueeumepreocupavapara
construirumprojetoeramresumidamente:
1) Resoluçãodatela:basicamentesearesoluç ãoera640x480,800x600ou
1024x768.
2) CompatibilidadedeBrowser:basicamentecomafamíliadoIE5,5.5e6.
AsvezesoIEparaMac.Mozilla,Firefox(quefoichamadodePhoenixno
começo)eOperanãoeramumapreocupação.
Esó.
Eupraticamenteignoravaopessoalde640x480,fazendowebsitescom
largura mínima de 768, para caber com folga nas resoluções acima de

## Página 70

CasadoCódigo
800x600. Alémdissoeumelascavaparafazerositefuncionarnessasver-
sõesdoIE.Basicamenteessaeraarotina.
Atualmentevocêprecisasepreocuparcomessespontos,mastudoficou
bemmaiscomplexo.Partedosbrowsersseatualizaquasequesemanalmente.
AtémesmooInternetExplorer,queeraumexemplodapreguiça,estáfazendo
lançamentosmaisregularesdesuasversõesecadavezmaiscompatíveiscom
ospadrões.Asresoluçõessãomaisnumerosasdoqueantigamenteeparece
queissosótendeaaumentar,jáqueasempresasnuncavãoparardefabricar
novosaparelhos.
Quandoasprimeiraspreocupaçõescomosbrowsersmobilesurgiram,os
celularestinhamtelastãopequenaseconexõestãoruinsqueeraimpraticável
fazerqualquercoisaquerealmentefuncionassecomumaexperiênciaagra-
dável.Passou-semuitotempoatéqueosmobilessetransformassememuma
prioridade.Mesmoassim,oOperafoiodestaquedaquelaépocadandouma
grandeajudaparaomundointeiroaolan çaroOperaMini,quefoiopri-
meirobrowsermobiledecente.RodavalindamentenomeuNokia6111,que
tinhaumaresoluçãode128x160. OOperatentavadarumjeitonabagun ça
toda,paramelhoraraformacomonavegávamosnainternetemaparelhos
comtelasno-touche,principalmente,emtelasmenoresqueoburacodefe-
chadura.
64

## Página 71

CasadoCódigo Capítulo7. WebMobile
Fig.7.1:Quesaudadesdessetempo!
Claro, tudo mudou quando o primeiro iPhone chegou. Seguindo a
mesmalinhadoOpera,oSafarilevouanavegaç ãoemmobilesparaoutro
nível.MassevocêachoumaravilhosaaideiadaApple,aomostrarositeem
miniaturanoSafari,saibaqueissofoiideiaoriginaldoOpera.Naverdade,os
browsersincorporaramváriasideiasdoOpera,comoabas,porexemplo.
DepoisqueoiPhonesetornouummarco,acorridadoourocome çou
e,claro,aspreocupaçõessóaumentaram,jáquenãohavianenhumpadrão
decenteparadesenvolvermosparamobile.OW3Cfaziaumasériedereco-
mendações,masaúnicacoisaquepodíamosfazeratéentãoeraformataro
layoutparacelularesusandoa media type para handheld.
A base do desenvolvimento web mobile
Estecapítulovaimostrarumasériedeassuntosquesãoabaseparacons-
truirwebsitesqueserãobem-vistosemqualquertamanhodetela.Sãoabase
do Responsive Web Design,queéapontadoicebergdeumacole çãodeme-
todologiaschamada Adaptive Web Design. EntendaqueoResponsiveWeb
Design(RWD)nãoésuficienteparafazermoswebsitesprontosparadiver-
65

## Página 72

7.1. OqueéoAdaptiveWebDesign CasadoCódigo
sostamanhosdetelas. Existemumasériedepreocupaçõescomquevocê
vaiprecisarseimportarcomopassardotempo,conformeseuprojetovai
crescendoouseusclientesvãosediversificando. Eufizumaapresentaç ão
(http://www.slideshare.net/diegoeis/o-bla-bla-bla-do-responsive)sobreisso
quepodelheserbastanteesclarecedora.
7 .1 O que é o Adaptive WebDesign
Osprincípiosdodesenvolvimentomobiletêmseaglutinadoemumtermo
chamado Adaptive Web Design. Algunsdesenvolvedoresconfundemeste
termocom Responsive Web Design,masnãoseengane:oResponsiveéuma
dassoluçõesquecompõemotermoAdaptiveWebDesign.
Criarumwebsiteadaptativotemsetornadocadavezmaiscomplexo.São
váriasmetodologiasetécnicasquemuitasvezesfazemcomqueessatarefade
produzirsitesmobilesepare çamaiscomplicadadoqueelaé.Deacordocom
o Brad Frost(http://bradfrostweb.com/),vocêpoderesumiroAdaptiveWeb
Designem5pontos:
1) Ubiquidade
2) Flexibilidade
3) Performance
4) Enhancement(deaprimoramento,melhoramento)
5) Future-Friendly
Eletemumartigomuito,muitoimportante(http://bradfrostweb.com/
blog/post/the-principles-of-adaptive-design/)queexplicaexatamentecada
umdessesprincípios.
Aideiadecriarumwebsiteúnicoéradiante,masquepodeconfundir
equipesinteiras,incluindogestores. Ébomquevocêleiamuitosobreeste
assuntoparatomarboasdecisõesfuturamente.Produzirumwebsiteprepa-
radoparaqualquertipodetelaéumdesafioemváriosmomentos. Manter
umaperformancedecente,comcódigolegíveleorganizado,compatívelcom
todososbrowserséumdesafioparavidatoda.
66

## Página 73

CasadoCódigo Capítulo7. WebMobile
Mobile First
MobileFirstéumtermomuitopopularizadopeloLukeWroblewski,um
dosgurusquandosetratadedesignparamobiles.AideiadoMobileFirsté
muitosimples:foque-seprimeiroemdispositivoscomtelaspequenas,depois
váadaptandoseusiteouprodutoparatelasgrandes.
Quandoessaloucuradewebmobileiniciou,nãohaviamuitooqueos
desenvolvedorespudessemfazer.Osmobilesmaisusadoseramfeaturespho-
nes,lerdos,comumsistemaoperacionalhorrívelebrowserspéssimos.Eraa
épocadoWindowsMobile.EraaépocadoSymbian(esseeratop).Sevocê
fordasantigas,jádeveterusadoumPalmOSouumPowerPCcomorgulho.
Eraumaépocainteressanteporqueosaparelhosmóveiseramnovidade.Era
difícilencontraralguémnaruacomumcelular,aindamaiscomumcelular
queseconectavacomainternet.
Esseeraummercadobagun çadoemuitonovo.Ecomoemtodomercado
novo,nãohaviaboaspráticasemquepudéssemosnosapoiarparadesenvol-
verwebsitesparadispositivosmóveis. DepoisqueoiPhonemudoutodoo
mercado,nóspassamosadesenvolverwebsitesmobiledamesmamaneira
quedesenvolvíamosparadesktop. Claro,comaajudadasMediaQueries,
fazerversõesmobileficoumuitomaisfácil.Masmesmoassimametodolo-
giaaindaeraamesma:fazíamosumwebsitesefocandoemdesktops,depois
adaptávamosparaMobile.Issoincluíacolocar display: none; emtudo
oquevocênãoqueriaqueaparecessenocelular.
Opontoeraqueinvariavelmenteoscelularesprecisamdemuitaaten-
ção. Elessãoaparelhoscommenospoderdeprocessamentoqueosdesk-
tops/notebooks,temumcontextomaisrestritivoporcausadotamanhoda
telaeasformasdeusosãototalmentediferentesdoqueosusuáriosestão
acostumados.Simplesmentemudarotamanhodasimagens,ostamanhosde
textoeoposicionamentodoselementosnãoésuficiente. Épraticamenteo
trabalhodefazerdoiswebsites... nãofaziasentido.FoiaíqueoLukeWro-
blewskicunhouotermoMobileFirst.
AideiadoMobileFirstéquevocêsefoqueprimeiroemtelaspequenas,
depoisnastelasgrandes.Issoquerdizerquevocêiniciatodooplanejamento,
designecódigodoprojetocomfocoprimeiroemtelaspequenas. Issolhe
traráumasériedevantagensposteriormente,quandoforomomentodede-
67

## Página 74

7.1. OqueéoAdaptiveWebDesign CasadoCódigo
senvolveraversãodesktop.Quandovocêpensaprimeiroemtelaspequenas,
vocêprecisasepreocuparcomumasériederestrições.Porexemplo,perfor-
mance.
Mesmoqueoscelularesdehojeemdiasejampoderososerápidos,ainda
nãodáparacompararcomopoderdeprocessamentodeumdesktop.Por-
tanto,aofazerumwebsitepensandoprimeironaversãomobile,vocêserá
obrigadoapensarnaperformancedosite. Essanãoeraumapreocupaç ão
tãoconstanteantes,masagoravocêprecisaentregarumwebsiterápidopor
causadocontextodosmobiles,ondeaconexãoépéssimanamaioriadasve-
zes.Notequesevocêjápensounamelhorperformancepossível,quandovocê
fizeraversãodesktopdowebsite,performancejánãoseráumapreocupaç ão
constante.
Issoacontecerácomumasériedeoutrasrestrições,comodefluxodena-
vegação,quantidadedetextos,agrupamentoinformaçãoeadaptaçãodecom-
ponentes.Háalgumasdicasimportantesqueprecisamserlevadasasérioao
fazerumsitemobile:
•Se o fluxo é longo, diminua.Lembre-sequeousuárioestáemumdis-
positivomóveleprovavelmenteeleestaráemumcontextoestranho,
comodirigindo,andandonaruaounoônibuscheio. Ofluxodena-
vegaçãonãopodesercomplexonemcomprido.Tentefazerumfluxo
maisbrandoesimples,tantoparamobilequantoparadesktop.
•Mantenha comportamentos similares. Tentesempremanteromesmo
comportamentodeinteraçõesentreosdispositivos.Sevocêabreuma
modalnoDesktop,tenteabriressamesmamodalnoMobile.Claro,na
medidadopossível,existemcenáriosemquenãoépossívelmantero
mesmocomportamentoemdispositivostãodiferentes,mesmoassim,
semprepriorizemantercomportamentossimilaresentreosaparelhos.
•Imagens. Aospoucosoproblemadasimagensvaiseresolvendo. O
Googletemseesfor çadocomopadrãoWebPeoW3Coficializouatag
picture.Atéqueessastecnologiasestejamusáveis,nãopercatempo
fazendováriostiposdeimagens.
•Não abuse dos elementos adaptados.Hámomentosemqueoselementos
68

## Página 76

7.2. MediaQueries CasadoCódigo
O que é Responsive Web Design?
ResponsiveWebDesignéacimadetudoumconceito.Nósnosresponsa-
bilizamosporapresentarainformaçãodeformaacessíveleconfortávelpara
diversosmeiosdeacesso.Muitoswebsitesrestringemoconceitoaaparelhos
comtelasdediversostamanhos,masoconceitoémuitomaisabrangente.
Mesmoassim,vourestringirosprimeirosexemplosadispositivosquete-
nhamtelasequeestãomaispresentesatualmente.Nãovoumeestendermuito
ameiosdeacessocomoleitoresdetela,robôsdebuscaououtrosdispositivos.
Oprimeiropassoparartornarawebmaisacessívelparaqualquermeio
deacessoéfazercomqueosbrowsersformatemdemaneiramaiseficiente
nossoslayouts. Issoépossívelfazendocomqueelerenderizeumblocode
CSSdeacordocomascaracterísticasdosdispositivos. Issoéfeitocomas
MediaTypeseasMediaQueriesquevocêvailermaisparaafrente.
Osegundopassoéfazercomqueolayoutsejaamigável.Paraisso,você
precisaentenderosdilemasdosseuslayoutseresolvê-lossemqueodesign
mudenosdispositivosdaáguaparaovinho,mantendoasmesmascaracterís-
ticasehistóriasdeuso.AspremissasqueenvolvemoResponsiveWebDesign
sãoasseguintes:
1) Gridfluído
2) ImagensFlexíveis
3) MediaQueries
7 .2 M ediaQueries
EunãopossoexplicarsobreMediaQueriessemfalarantesdasMediaTy-
pes.AsMediaTypesforamaprimeiraversãodeumesfor çoparadirecionar
aformataçãoCSSparadeterminadostiposdemeiosdeacesso.
OHTMLfoicriadoparaserportável,ouseja,eledeveserlidoeinter-
pretadoporqualquertipodedispositivo.CadaumexibeHTMLdeumade-
terminadamaneira. Logo,aformacomovocêformataolayoutprecisaser
diferenteparacadadispositivo. Porexemplo,sevocêvisitaumsiteporum
desktop,aexperiênciaserátotalmentediferentecasovocêvisiteomesmosite
70

## Página 77

CasadoCódigo Capítulo7. WebMobile
porumdispositivomóvel.Sãodiferentes,comformastotalmentedistintasde
navegaçãoeuso.
Masoexemploanteriorémuitocomum. Existemoutroscenáriosque
precisamospreverparacontrolaraformataçãodosite,porexemplo,quando
ousuárioimprimesuapágina.Quandoalguémimprimeapáginadeumar-
tigonositedoUOL,Terraouqualquersitedeconteúdo,várioselementos
setornaminúteis,come çandopelomenu,barralateral,rodapéetc.Otexto
poderiasermaisbemformatadoparaquealeituraempapelfiquemaiscon-
fortável.Essadiferençaentredispositivosécontroladapelas Media Types.
VejaumalistadoquepodesercontroladoviaCSS:
•all:estevaloréusadoparaqueocódigoCSSsejaaplicadoparatodos
osdispositivos.
•brailleparadispositivostáteis.
•embossedparadispositivosqueimprimememBraille.
•handheldparadispositivosdemão,celulareseoutrosdispositivosdeste
perfil.Normalmentecomtelaspequenasebandalimitada.
•printparaimpressãoempapel.
•projectionparaapresentações,comoPowerPoint.Estevalorfoiinven-
tadopelopessoaldaOpera. muitoútil.
•screenparadispositivoscomtelascoloridasealtaresoluç ão.
•speechparasintetizadoresdevoz. OCSS2temumaespecificaç ão
deCSSchamadaAural(http://www.w3.org/TR/CSS2/aural.html)com
quepodemos“formatar”avozdeleitoresdetelaeoutrossintetizadores.
•ttyparadispositivosqueutilizamumagradefixaparaexibiç ãodeca-
racteres,comoteletypes,terminais,dispositivosportáteiscomdisplay
limitado.
•tvparadispositivoscomotelevisores,ouseja,combaixaresoluç ão,com
boaquantidadedecoresescrolllimitado.
71

## Página 78

7.2. MediaQueries CasadoCódigo
Aaplicaçãoémuitosimples: bastaadicionaralinhacomumde link
paraseuCSS,inserindoumatributo mediaeadicionandoovalordesejado:
<link rel="stylesheet" href="estilo.css" media="handheld">
NotequenesseexemploestouchamandoumarquivoCSS,queserádesti-
nadoparafuncionaremdispositivosdemedia HANDHELD:aparelhosmó-
veis,celularescomtelapequenaeaparelhossimilares(jáusouPalmTop?).
Logo,esseCSSnãoseráaplicadoquandoousuáriovisitarositeutilizando
umdesktop.Paratanto,teríamosqueutilizarmedia SCREEN:
<link rel="stylesheet" href="estilo.css" media="screen">
O problema
Vocêjánotouquetododiasurgemnovosdispositivos,comdiversosta-
manhosehardwaresparecidoscomosdesktops?Qualquercelularmeia-boca
hojetemaconfiguraçãomaisparrudaquequalquercomputadorantigo.Prin-
cipalmenteaconfiguraçãodatela,àqualosfabricantestêmdadomaisaten-
çãonosúltimosanos. Logo,nãohámotivoparaprepararmosumlayoute
umCSScommediatype HANDHELDparaoiPhone,jáqueelenãoseen-
caixanessacategoria.Entretanto,oiPhonetambémnãoénemdelongeum
desktop.Aíexisteoproblema:amediatypescreenseencaixariaparadireci-
onarmosaformataçãoparaoiPhoneeoutrossmartphonesmodernos,mas
aespecificaçãoéclaraquandodizqueamediatypescreenéparadesktopse
computadores.Comofazeragora?
A solução: Media Queries
AsMediaQueriesdefinemcondiçõesparaqueoCSSsejautilizadoem
cenáriosespecíficos.Seessascondiçõesforemaprovadas,ouseja,seodispo-
sitivoseadequaratodasascondiçõesestabelecidasnasuaMediaQuerie,o
CSSseráaplicado.Vejaumexemplo:
<link href="estilo.css" media="screen and (max-width: 480px)">
Especificamosqueoarquivo estilo.cssseráaplicadoemdispositivos
queseenquadramnacondiçãode screen(ouseja,quetêmumatelacom
altacapacidadedecores)ecomumalarguramáximade480px.
72

## Página 79

CasadoCódigo Capítulo7. WebMobile
Háumalistadecaracterísticasquevocêpodeutilizaraquiparaselecionar
osdispositivosquevocêquiser:
• width
• height
• device-width
• device-height
• orientation
• aspect-ratio
• device-aspect-ratio
• color
• color-index
• monochrome
• resolution
• scan
• grid
Geralmente,usamosasMediaQueriesdentrodocódigoCSS.Vocêlinka
seuCSSno HEADdodocumentoassim:
<link rel="stylesheet" href="estilo.css">
DentrodocódigoCSS,vocêvaisepararosfamosos breakpoints,quesão
ascondiçõesdetamanhodastelasdosdispositivos.Essetamanhovaidefinir
quandocadablocodeCSSseráutilizado.Vejaocódigoaseguir:
73

## Página 80

7.3. MetatagViewport CasadoCódigo
/*
Código que será herdado por qualquer dispositivo.
Se você já conhecer a ideia do Mobile First,
esse primeiro código será destinado para mobiles.
*/
a {color: blue;}
/*
Pra dispositivos que têm uma largura mínima de 768 pixels.
Tablets, por exemplo.
*/
@media (min-width: 768px) {
a {color: yellow;}
}
/*
Com uma largura mínima de 992 pixels. Monitores por exemplo.
*/
@media (min-width: 992px) {
a {color: green;}
}
/*
Dispositivos com largura mínima de 1200 pixels. Por exemplo
grandes monitores e TVs.
*/
@media (min-width: 1200px) {
a {color: black;}
}
EassimvocêvaiescrevendoseuCSSemanipulandoaformataç ãodo
layoutdeacordocomodispositivodesejado.
7 .3 M etatag Viewport
O viewportéaáreaondeseuwebsiteaparece. Éaquelaáreabrancaonde
owebsiteémontadopelobrowser. Éaáreanaqualvocêsepreocupaseo
layoutvaiounãocabernahoradacriaç ão.Otamanhodoviewportdepende
74

## Página 81

CasadoCódigo Capítulo7. WebMobile
muitodaresolução,tamanhodomonitoredispositivoutilizado.Emmáqui-
nasdesktop,nósnãoprecisamosnospreocuparmuito,jáestamosacostuma-
doscomumdeterminadotamanhodetelaeresoluç ãomédiautilizadapelos
usuários,quehojegiraemtornodenomínimo1024delargura.Masquando
começamosavariarmuitootamanhodastelas,alarguradoviewportcome ça
aserumapreocupaçãoporqueafetadiretamenteaformacomoousuáriouti-
lizaseuwebsite.
Hojeexisteumagamamuitograndedeaparelhoscomtelasdetamanhos
variados.Comeceapensarpelosnetbooksedepoisvádiminuindoatéchegar
emumsmartphonepopularcomooiPhoneetc.Avariaç ãodostamanhosé
muitogrande.AlarguradateladoiPhonenaposiç ãoretratoéde320px.Mas
suaresoluçãopadrãoé980px.Porisso,tenhaemmenteque tamanho de tela
ébemdiferentede resolução. Issoquerdizerque,sevocêfizerumHTML
simples,colocarumaimagemde980pxdelarguraevisualizarnoiPhonenão
existirábarraderolagem.Obviamenteaimagemficará miniaturizada,como
mostradoaseguir:
75

## Página 82

7.3. MetatagViewport CasadoCódigo
Fig.7.2:Semmetatagviewport,ocelularredimensionaaimagem.
Issoéinteressanteporquepossibilitaaboavisualizaç ãodewebsitesque
nãoestãopreparadosparamobiles.Vemosositeinteirominiaturizado,com
possibilidadedefazerzoomemqualquerpartedolayout.
Manipulando a meta tag Viewport
Mesmoassim,ossmartphonestêmtelaspequenasquepodemdificultar
aleiturasefizermosumsistemaplanejadoparagrandesresoluções.Porisso,
éinteressantequepossamoscustomizaroviewportparaqueeleseadequeà
realidadedessesdispositivos.Éaíqueentraa metatag viewport.
Comessametatag,vamosprepararoviewportparaaresoluç ãoqueo
browserdeverenderizar.Dessaforma,podemosprepararwebsitescomreso-
76

## Página 83

CasadoCódigo Capítulo7. WebMobile
luçõespersonalizadasparasmartphoneseoutrosaparelhos.Asintaxeémuito
simplesedevesercolocada,comosempre,natag head.Vejaocódigoinicial:
<meta name="viewport" content="width=device-width">
Osvaloresde contentsãoosseguintes:
•widthdefineumalarguraparaoviewport.Osvalorespodemserem
PXou device-width, quedeterminaautomaticamenteumvalor
igualàlarguradateladodispositivo.
•heightdefineumaalturaparaoviewport.Osvalorespodemserem
PXou device-height,quedeterminaautomaticamenteumvalor
igualàalturadateladodispositivo.
•initial-scaledefineaescalainicialdoviewport.
•user-scalablehabilitaapossibilidadedeousuáriofazerzoomna
tela. Éativadoquandoousuáriobateduasvezescomodedoemum
lugardatelaoufazomovimentode pinch.
Para facilitar o uso, definimos que o viewport irá sempre renderizar
ositecomalarguradefaultdodispositivousadopelousuáriocomova-
lor device-width na propriedade width. Existe também o valor
device-height,queéusadanapropriedade height,quandoseulayout
mudarádeposiçãocasoaalturadaviewportsejamodificada(comoquando
ousuáriousarumaparelhocomumaalturamaiordoqueonormal).
<meta name="viewport" content="width=device-width">
Esteéumassuntoquemerecemuitoestudoeporissoseguemalguns
linksparaquevocêseaprofundemais.Émuitonecessárioparaaproduç ão
delayoutsparacelulares.
• Lista de tamanhos de viewports dos principais dis-
positivos (http://i-skool.co.uk/mobile-development/
web-design-for-mobiles-and-tablets-viewport-sizes/)
77

## Página 84

7.4. UnidadesemREM CasadoCódigo
• ArtigodaMozillaDeveloperNetwork(https://developer.mozilla.org/
pt-BR/docs/Mozilla/Mobile/Viewport_meta_tag)
• Manipulando a metatag Viewport (http://tableless.com.br/
manipulando-metatag-viewport/)
• Aregra@viewport(http://tableless.com.br/regra-viewport/)
7 .4 U nidades em REM
AquinoBrasil,émuitocomumusarmospixelsparadefiniç ãodetamanhode
textos.LáforaagaleragostamuitodeusarEM.Masqualadiferen ça?
Pixels
Unidadeempixelsémaisvelhoqueandarparatrás. Vocêutilizapixels
paradefiniralarguradeumelemento,otamanhodotexto,aespessurada
bordaeoutrascoisas.
UnidadeemPixelséutilizadoporqueéamedidamaisexataquevocê
podeencontrar.Pornãoserumamedidavariável,ospixelssãofáceisdecon-
trolar.Fáceisdecalcular.VocêabreseuPhotoshop,medeepassaosvalores
paraCSSfacilmente. Étudomuitoeficiente. Éporissoqueamaioriados
devssemprepreferiuutilizarpixelsnosprojetos.
Mas,antigamente,definirunidadesdetextoempixelstraziaumadesvan-
tagemherdadadoInternetExplorer:quandoousuáriotentavamudarota-
manhodotextopelobrowser,poralgummotivobizarrooIEnãoaumentava
afontporqueelaestavadefinidaempixels.Umproblemasériodeacessibili-
dade.Éporissoquemuitosdevs,duranteumtempo,definiramotamanho
dotextoutilizando%(porcentagem).Oproblemaéquetrabalharcompor-
centageméalgomuitoinstável.Haviadiferençasdetamanhosdetextosentre
osbrowserseporcausadissoolayoutnuncaficavaigual.
Unidades em EM
EMéumaunidadedemedidatipográficaeseunomeestárelacionado
àletra M.Otamanhobasedessaunidadederivada largura da letra M em
maiúscula.Dizemque 1 emequivaleaproximadamentea 16 pontos.
78

## Página 85

CasadoCódigo Capítulo7. WebMobile
Não sou eu que estou falando isso, é a Wikipedia (http://tableless.
com. br/unidade-pixels-em-rem/“http://en.wikipedia.org/wiki/Em_(typo-
graphy)”).;-)
OproblemadeutilizarfontsemEMéqueelas,comoasporcentagens,são
variáveis.Diferentementedautilizaçãodepixels,temosquefazerumpouco
dematemáticaparaplanejarnossasunidadesnoprojeto.Nãoénadadeoutro
mundo,entãoparedepreguiça.
Afórmulaéfácildeentender.Voumanterostermoseminglêsparavocê
entendermelhorquandoforprocurarmaisinformaçõessobreesteassunto:
target÷ context= result
Umexemplo:imagineumtítulocomo font-sizede20px.
h1 {
font: 20px verdana, arial, tahoma, sans-serif;
}
O target(queéoelementoquequeremosmodificar)é 20px. Nesse
caso,o BODYéopaidonossoH1,portantoeleénosso context,quecomo
jádissemostemovalorpadrãode 16px.
20÷ 16= 1.25.
h1 {
font: 1.25em verdana, arial, tahoma, sans-serif;
}
SeesteH1estiverdentrodeoutroelemento, tipoumdiv, ovalorde
contextagoraéotamanhodafontdodiv.TenhacomoexemploesteHTML:
<div>
<h1>Um título bacana</h1>
<p>Um texto grande e bacana para fazermos parágrafos.</p>
</div>
OCSScomasfontsemPX:
div {
font: 30px verdana, arial, tahoma, sans-serif;
}
79

## Página 86

7.4. UnidadesemREM CasadoCódigo
h1 {
font-size: 20px;
}
p {
font-size: 12px;
}
Primeiroparágrafo:12px(target)÷ 30px(context[div])= 0.4em
Título: 20px(target)÷ 30px(context[div])= 0.67em
Div: 30px(target)÷ 16px(context[body])= 1.88em
body {font: 100% verdana, arial, tahoma, sans-serif;}
div {
font-size: 1.88em;
}
h1 {
font-size: 0.67em;
}
p {
font-size: 0.4em;
}
Emvezdevocêmudarasfontsdecadaelemento,vocêpodesimplesmente
mudarovalordafontdotarget,ouseja,dobodypara120%oupara80%,isso
farácomquetodasasfontsdositeaumentemoudiminuemproporcional-
menteemrelaçãoàporcentagemdobody.
Infelizmenteissonãoéparatodososbrowsers: Firefox3.6+,Chrome,
Safari5eIE9suportamaunidadeREM.Maseosquenãosuportam?Bom,
useafontemPX.Cáentrenós,dessalistadebrowserssófaltouoIE8,jáque
oIE7e6jáforamembora.SevocênãosuportaroIE8emseusprojetos,faç a
umfallbackcomooexemploaseguir.Vocêvaiescreverumpoucomaisde
código,masvaigarantiracompatibilidadedoIE8.
80

## Página 87

CasadoCódigo Capítulo7. WebMobile
body {font: 100% verdana, arial, tahoma, sans-serif ;}
div {
font-size: 30px;
font-size: 1.88rem;
}
h1 {
font-size: 20px;
font-size: 1.25rem;
}
p {
font-size: 12px;
font-size: 0.75rem;
}
EnquantooREM/EMsãomaisflexíveisenosdáavantagemdaacessi-
bilidade,poroutroladoenvolveumpoucodematemática. Mesmoassim,
utilizarREMtemsidoumaótimapráticaenãotemtrazidomuitosproble-
mas,naminhaexperiência.ComousoSASS,façoumaMixinparacalcular
REMetransformaremPX.
7 .5 I magens
Trabalharcomimagensemlayoutsresponsivossemprefoialgolimitado.An-
tesdeapareceratag pictureeo srcset,podíamosnomáximomanipular
otamanhodaimagemcom max-widthouusarpluginmalucosparapro-
curarememnossosservidoresumaimagemcommaisoumenosqualidade
dependendodonossodispositivos. Tudoeraumagrandegambiarra. Mas
agoraacoisamudou.Adiante,vocêconheceráduastecnologiasquenosaju-
damaservirimagensdeformainteligenteparasitesresponsivos.
Existeumgrupochamado Responsive Images Community Group (http:
//responsiveimages.org/)formadopordesenvolvedoresparadiscutiredesen-
volversoluçõesparaoproblemadasimagensresponsivas,comumasoluç ão
client-side,padronizadaebaseadanascapacidadesdodispositivousadopelo
usuário.Issomelhoraogastoexcessivodebandaeotimizaousodeimagens
81

## Página 88

7.5. Imagens CasadoCódigo
paraosdiferentestiposdetelaetambémparaimpressão.
Nessegruposãodiscutidasumasériedeop ções,masassoluçõesque
jásaíramdopapeleestãosendosuportadasporalgunsbrowserssãoatag
<picture>eoatributo srcset.
Casos de uso
Existemdiversoscasosemqueprecisamosmostraramesmaimagem,
mascomresoluçõesdiferentes.Aseguir,descrevialgunsdestescasos.Uma
listamaisdetalhadaecompletapodeservistadadocumentaç ãodoW3C:
Baseado em resolução Geralmente,queremosmostraramesmaimagem
emmúltiplasresoluções. Emdispositivoscomumaresoluçãoótima,pode-
mosservirimagenscommaisqualidadedoqueparaaparelhoscomresolu-
çõespiores.
Fig.7.3:Váriosdispositivos,váriasresoluções.
Baseado no viewport Podemostambémservirimagenssebaseadono
viewportdousuário,detectandoseeleestáusandoumaparelhocomtelape-
quenaoucomtelagrande. Porexemplo:emsitesquetêmaquelasimagens
gigantescobrindoo header,aoestilodoMedium.Aquelaimagemgrande
ficamuitobememaparelhoscomviewportgrande,masparaaparelhospe-
quenos,aimagemémuitograndeepesadaprasercarregada.
82

## Página 89

CasadoCódigo Capítulo7. WebMobile
Fig.7.4:Lembre-se:viewportéaáreadisponívelondeositeiráaparecer.
Densidade de pixels Hátambémocenárioondequeremosmostrarima-
gensmelhoresparadispositivosquetêmumadensidadedepixelsmaior,
evitandoservirparaimagenscombaixaqualidadeparaessesdispositivos.
Quantomaioradensidadedepixelsdoaparelho,maioraquantidadedepixels
aimagemprecisater.
83

## Página 90

7.5. Imagens CasadoCódigo
Fig.7.5:Osdispositivostêmdensidadedepixelsdiferente,independentedo
seutamanho.
Direção de arte Éumcenárioondepodemosmostraramesmaimagem,
comrecortesdiferentes.
84

## Página 91

CasadoCódigo Capítulo7. WebMobile
Fig.7.6:Mesmaimagem,recortesdiferentes.
Link da documentação com os casos de uso: http://usecases.
responsiveimages.org/#use-cases
O atributo SRCSET
Oatributo srcsetpermiteespecificarumalistadefontesparaumacha-
madadeimagem,entregandoaimagemcorretadeacordocomadensidade
depixelsdateladousuário.Ocódigoficaassim:
<img src="imagem-baixa-resolucao.jpg"
srcset="imagem-alta-resolucao.jpg 2x">
Sevocêquisercontemplartelascomumadensidadedepixelsmaior,basta
acrescentarmaisop ções:
<img src="imagem-baixa-resolucao.jpg"
srcset="imagem-alta-resolucao.jpg 2x, imagem-maior-ainda.jpg 3x">
Muitosimples,nãoé?Obrowsersimplesmentemostraaimagemdebaixa
resoluçãocomopadrãoeseousuárioestiverusandoumateladealtaresolu-
85

## Página 92

7.6. Muitomais CasadoCódigo
ção,obrowserseencarregademostraraimagememalta.Esseéumtruque
quevocêpodeusaragora.Seobrowsernãoreconheceroatributo srcset,
elesimplesmentevaiignorareseusitenãovaiquebrar.
Porcuriosidade:rolouumagrandediscussãosobreasemânticadoatri-
buto srcset. Uns dizem que um atributo serve para que o elemento
herdealgumascaracterísticas. Issoquerdizerqueusarumatributocomo
fallback para servir outras fontes de arquivos é errado. Mas convenha-
mos,asintaxeémuitosimples. Vocêpodeverocontextodessadiscussão
sobreasintaxenesseartigodoAListApart: http://alistapart.com/article/
responsive-images-and-web-standards-at-the-turning-point
Éaíqueentraatag <picture>.
O elemento picture
Oelemento pictureéumpadrãodemarcaçãoquepermitedeclarar
umasériedefontesalternativasparaumaimagem.UsandoMediaQueries,
temoscontroledequandomostrarcadaumadessasimagensparaousuário.
Asintaxeébastantesimples:
<picture>
<source media= "(min-width: 980px)" srcset="large.jpg">
<source media= "(min-width: 768px)" srcset="med.jpg">
<img src="small.jpg" alt="The president giving an award.">
</picture>
Notealiqueháumatributo mediaemcadaelement sourcedentrode
picture. Eledefineobreakpointqueobrowservaibaixaraquelaimagem
específica.
Éporissoquehátantadiscussãoquantoaousodoelemento picture:
teoricamenteeleresolveapenasocenáriode“direçãodearte”,queéquando
precisamosservirumamesmaimagemcomrecortesoutamanhosdiferentes.
Emoutroscenários,oatributo srcsetresolvebastantebem.
7 .6 M uito mais
Existemmuitos,masmuitosassuntosquepoderiamserabordadosaqui,mas
aíestelivrosetornariaexclusivamentesobredesenvolvimentomobile.Como
86

## Página 93

CasadoCódigo Capítulo7. WebMobile
estenãoémeuintuito,prefirodeixarváriosassuntosparavocêestudarese
divertirumpouco,ok? Sãomateriaisdepesquisaquepouparãoumtempo
valioso. Achoimportanteavisarquealgunslinksestãoeminglês,masnem
precisodizerquesaberinglêsérequisitomínimoparavocêtrabalharcom
web,né?
• Artigo: Nãouseoelementpicturenamaioriadavezes(http://blog.
cloudfour.com/dont-use-picture-most-of-the-time/)
• Artigo:OcenáriodoWebDesignResponsivo(http://tableless.com.br/
o-cenario-do-web-design-responsivo/)
• Artigo: Design Responsivo por uma web Única (http:
//sergiolopes.org/responsive-web-design/) Artigo: Responsive
Web Design Adaptação vs Otimização (http://tableless.com.br/
responsive-web-design-adaptacao-vs-otimizacao/)
• Artigo: Tudo o que você precisa saber sobre resoluções, telas re-
tina, devicePixelRatio, DPI,CSSPixelseetc(http://sergiolopes.org/
resolucoes-dpi-pixel-ratio-retina/)
• Artigo: TextosdoJasonGrigsbysobreimagensresponsivas(http://
blog.cloudfour.com/?s=responsive+images)
• Artigo: As muitas faces do Mobile First (http://tableless.com.br/
as-muitas-faces-do-mobile-first/)
• Artigo: WebKit Has Implemented srcset, And It’s A Good
Thing (http://www.smashingmagazine.com/2013/08/21/
webkit-implements-srcset-and-why-its-a-good-thing/)
• Artigo: “RWD Is Bad for Performance” Is Good
for Performance (http://timkadlec.com/2014/07/
rwd-is-bad-for-performance-is-good-for-performance/)
• Responsive Web Design Newsletter (http://responsivedesignweekly.
com/)
87

## Página 94

7.6. Muitomais CasadoCódigo
• Slides: Comosuportartelasdealtaresoluçãoeficientementenaweb
(http://sergiolopes.org/palestra-retina-web/#slide-capa)
• Slides: Este é essencial : For a Future-Friendly
Web (http://www.slideshare.net/bradfrostweb/
for-a-futurefriendly-web-webvisions-chicago-2012)
• Slides: O blá blá blá do Responsive Web Design ou Os
cuidados do Web mobile (http://pt.slideshare.net/diegoeis/
o-bla-bla-bla-do-responsive)
• Slides: Responsive Design Vs Separate Mobile Sites: Presidential
SmackdownEdition(http://bit.ly/1E5rSnW)
• Slides: Multi-device Web Design (http://www.lukew.com/presos/
preso.asp?31)
• Slides:Mobileinput(http://www.lukew.com/presos/preso.asp?23)
• Slides:MobileFirst(http://www.lukew.com/presos/preso.asp?26)
• Slides:Designfortouch(http://www.lukew.com/presos/preso.asp?33)
• Livro: Mobile First (http://www.lukew.com/resources/mobile_first.
asp)
• Livro: Web Design Responsivo: Páginas adaptáveis para to-
dos os dispositivos (http://www.casadocodigo.com.br/products/
livro-web-design-responsivo)
• Livro:AWebMobile:Programeparaummundodemuitosdispositi-
vos(http://www.casadocodigo.com.br/products/livro-web-mobile)
• Diretório com vários links escolhidos pelo Sérgio Lopes (http://
sergiolopes.org/diretorio-design-responsivo/)
88

## Página 95

Capítulo8
Performance
Geralmente,80%daperformancedeumwebsiteouumprodutodeinternet
estãoconcentradosnofront-end.Mesmoassim,performanceéumdaqueles
assuntosquetodomundosabequeéimportante,masquegrandepartedas
equipes,pordiversosmotivos,nãotratamcomoumafeaturedoprojeto. A
grandemaioriasóvaipensaremmelhoraravelocidadedoprojetoapenasno
finaldodesenvolvimento,quandoseuHTML,CSSeJSjáforamfeitosouaté
pior,quandooprodutojáestápublicadoefuncionando.Ocorretoéqueisso
sejaumapreocupaçãodurantetodooprocessodedesenvolvimento.
Oidealéqueosdevscomecemapensaremperformancedesdeoplane-
jamentodoprojeto,juntocomowireframe.ExistemmuitasdecisõesdeUX,
porexemplo,quepodeminfluenciarbastanteaagilidadeeocarregamentodo
produto.EsteéumdosmotivospeloqualpensamossempreemMobileFirst.
Esteéumassuntobastanteextenso,queroapenasabordarumaspoucas
coisasquejulgoseremmaisimportantesparavocê,queéiniciante.Guarde

## Página 96

8.1. Oprocesso CasadoCódigo
tambémestetermoparaumapesquisaposterior: Performance as a feature.
Essaéumaexpressãoquetemsidousadaparademonstrarapreocupaç ão
comperformancecomosefosseumafeaturedoprojeto.
8.1 O processo
Obrowserseguealgunspassosimportantesantesdemostrarsuapáginana
teladousuário. Éimportantevocêconheceroqueaconteceporbaixodos
panosparaentendermelhortunarseuproduto.Ospassossão:
1) ObrowsermontaoDOM(Document Objecto Model )dodocumento. O
DOMéumarepresentaçãodoqueseráseuHTML.Eleéessencialparao
browserentenderarelaçãoqueoselementostêmentresi.Maslembre-se:
oDOMnãoéoHTML.OHTMLéoresultadofinal.
2) ObrowsermontaoCSSOM(CSS Object Model ),queéumarepresenta-
ção,comooDOM,queguardaasregrasdeformataç ãodoselementosdo
HTML.
3) Obrowserjuntaasduasárvores,oDOMeoCSSOM,emumaúnicaár-
vorechamada RenderTree. NaRenderTreeobrowsermontaumaárvore
baseadanoselementosqueserãovisíveisparaousuário. Issoquerdizer
queelementosquetêm display: none nãovãoconstarnaRenderTree.
4) Depoisjuntarasduasárvores,obrowsercalculaageometriadoselemen-
tos,colocandolarguraealtura.Feitoissoeleposicionaoelementonatela.
EssafasesechamaLayout.
5) Sabendodoseutamanhoesuaposição,obrowserentradafasechamada
Paint.Nessafaseeleirápintaroselementoseseusfilhosnatela,renderi-
zandocoresdebackground,imagensdebackground,borda,drop-shadow
eoutraspropriedades.
Existemuitaciêncianesseassuntoquepoderáajudá-loaentregarumpro-
dutomaisrápidoeágil. OChromeDevToolspodecontribuirbastanteno
monitoramentoeanálisedesseprocesso,fornecendodadosimportantespara
vocêentenderosgargalos.
90

## Página 97

CasadoCódigo Capítulo8. Performance
8.2 S aiba o que éReflow e Repaint
ObrowserfazduascoisasaojuntarseuHTMLcomoCSS:eleposicionato-
dososelementosnofluxoquevocêdefiniuaoimplementarolayoutede-
poisospinta,colocandocoresnobackground,notexto,definindoasimagens
defundoetc.ElefazissotudonocarregamentodoCSS.Quandoumbrow-
serprecisareposicionarumelementodoDOMporcausadealgumaaç ãodo
usuáriooudoseuJavaScript,issosechama Reflow.Quandoobrowserprecisa
pintar/desenharnovamenteumelementonatela,issosechamade Repaint.
GeralmenteoRefloweoRepaintsãocausadosquandovocêmodificaa
árvoredoDOMpormeiodoJavaScript. OReflow,principalmente,exige
bastantedocomputadordousuário inclusiveCPU poisobrowserprecisa
fazerumasériedecálculosparareposicionaroelementonolugarcorreto.
Quandovocêfazamodificaçãodealgumelemento,nãoéapenaselequeé
recalculadoereposicionado,mastodososoutroselementosqueoenvolvem
também.Alémdisso,quandooReflowéexecutado,obrowserbloqueiato-
dasasoperaçõesdousuário.Ouseja,ousuárionãopodeexecutarnenhuma
tarefacomoclicarourolarapágina.
Profundidade de código
Aquiéumbommomentodefalarsobreaprofundidadedoseucódigo
HTML.QuandovocêproduzumcódigoHTML,émuitoimportantequevocê
odeixeomaissimplespossível.Ouseja,quantomenosprofundidadeexistir,
melhor.Umexemploéocódigoaseguir:
<nav class="menu">
<div class="menu-inner">
<ul class="menu-options">
<li><a href="" title="">...</a></li>
</ul>
</div>
</nav>
Seriamelhorsefosseassim:
<nav class="menu">
<ul class="menu-options">
91

## Página 99

CasadoCódigo Capítulo8. Performance
8.3 O nde colocar as chamadas de CSS e JS?
Pareceumaperguntabesta,masnãoé. Arespostaésimples:chamadasde
CSSficamdentrodatag HEAD.Aschamadasdos JSficamsempreantesde
fecharo BODY.Basicamenteéisso.Claro,háexce ções,masgeralmentevocê
disponibilizaráseusCSSeJSdessaforma.Vamosvermaisdetalhes.
Chamando o CSS
OCSSéumrecursobloqueante. Umrecursobloqueantefazobrowser
pararderenderizarqualquercoisanapáginaenquantoesserecursonãofor
carregado.Issosignificaqueobrowserparatudoquandoencontraumacha-
madadeCSSnoseucódigo.Seelenãofizesseisso,elecarregariaseuHTML
emostrariaparaousuárioositetotalmentesemestilos;poucossegundosde-
pois,ositeiriapiscareboom,olayoutapareceria. Ousuárioteriaumlixo
deexperiência.IssoacontecesevocêcolocaroCSSnofinaldodocumento.
ElevaicarregarseuHTMLinteiroeousuárioveráositeprimeirosemne-
nhumestilo.Quandoobrowserchegaraofinaldodocumentoeencontrara
chamadadoCSS,sóentãovaicarregá-loeseuusuárioveráositemudarbrus-
camente.OGooglechamaesse“acontecimento”deFOUC:Flash of Unstyled
Content.
QuandooCSSécarregadodepois,issocausaRefloweRepaint,jáqueo
browsertemquerecalculartodooHTMLjácarregadoeentãoposicioná-lo
epintá-lonovamentenatela.
QuandoinserimosachamadadeCSSno HEAD,elevaicarregartodoo
CSSedepoisvaicontinuarocarregamentodoHTML.Ocarregamentoépro-
gressivo,ouseja,obrowsermostraoselementosnatelaconformelêseucó-
digo.Essefeedbackvisualéimportantíssimoparaaexperiênciadousuário,
poisdiminuiaesperaemostraparaeleumindicativodequeapáginaestá
funcionando.
Chamando o JS
OJavaScriptéocaraquemanipulaoHTMLeoCSS.Exatamenteporisso
eleprecisasercarregadoapenasdepoisqueseuHTMLeseuCSSforamcarre-
gadospelobrowser.Vocêdevechamarseusscriptslogoantesdofechamento
93

## Página 102

8.4. Paraestudarmais CasadoCódigo
• Compilação, Minificaç ão e concatenaç ão de
CSS, JS e HTML http://csswizardry.com/2013/01/
front-end-performance-for-web-designers-and-front-end-developers/
#section:gzipping-and-minifying
• Prefetch: http://csswizardry.com/2013/01/
front-end-performance-for-web-designers-and-front-end-developers/
#section:resource-prefetching http://calendar.perfplanet.com/2012/
speed-up-your-site-using-prefetching/
• EntendacomofuncionaatagSCRIPTeseusatributos:http://www.w3.
org/TR/html5/scripting-1.html#the-script-element
• Otimizaçãodeimagens
• ImagensemWebP
• ElementoPicture
• Atributosrcset
Aquivãomaisalgunslinksinteressantes:
•http://browserdiet.com/pt/
•http://tableless.com.br/performance-frontend-parte1/
•http://tableless.com.br/performance-frontend-parte2/
•https://developers.google.com/speed/articles/reflow
•https://developers.google.com/web/fundamentals/performance/
critical-rendering-path/render-tree-construction?hl=pt-br
•https://dev.opera.com/articles/efficient-JavaScript/?page=3#reflow
•http://www.phpied.com/css-and-the-critical-path/
•https://developers.google.com/web/fundamentals/
96

## Página 103

Capítulo9
Acessibilidade
9.1 O que é acessibilidade para web?
Respostarápida:émanterainformaçãoacessívelparaqualquerpessoa,em
qualquercondição,emqualquerdispositivooumeiodeacesso.
Aideiaéqueainformaçãofiqueaoalcancedequalquerum,nãoimporta
seessapessoatenhaalgumadeficiênciaounão,seestáusandoounãoalgum
dispositivo,leitordetelaouqualqueroutracoisaqueaajudeaconsumirinfor-
mação.Acessibilidadenawebétudosobremanterainformaç ãodisponível
paraqualquercoisaouqualquerumconsumirnahoraemquequiser.
Entendaqueacessibilidadenãoéaltruísmo. Vocênãomantémainfor-
maçãoacessívelparaleitoresdetelacomooJAWSouNVDAsóporquetem
dódepessoascegas.
Atéomomentodaescritadesselivro,acessibilidadenawebaindaéuma
barreiraemdiversasempresas. Paraadiretoria,faltamnúmerosparajusti-

## Página 104

9.2. Acessopeloteclado CasadoCódigo
ficar. Paraosdesenvolvedores,faltatempoeinteresse. Emempresasonde
háumpoucodeinteresse,oassuntodemoraparasedesenrolaratéquehaja
algumaatitudedeverdade.
OquepoucossabeméqueaacessibilidadeenvolveUX,front-end,back-
end,produçãodeconteúdo,QAeatémarketing/vendas. Cadaumadessas
áreasdeveriaterumpoucodepreocupaçãocomesteaspecto.
Acessibilidadenawebémuito,masmuitointeressante,maséumassunto
bastanteextenso.Porisso,queromostrarapenasalgunstópicosparaquevocê
estudemaisdaquiapouco.
9.2 A cesso pelo teclado
Obásicoparaqualquersistemaouwebsiteéquesejamacessíveisviateclado.
Umasuposiçãoquefazemostodososdiasédequequalquervisitanteusa
mouse.Essaéumaconclusão,nomínimo,equivocada.Sementrarnoque-
sitodequeseusvisitantespodemestarusandoumsmartphoneoutablet,é
necessárioqueseusitesejafacilmentenavegávelviateclado.
Otecladoéaindaasegundainterfaceentreoseuprodutoeousuário.
Existemduasmaneirasdeprepararseuprodutoouwebsiteparaquesejam
acessíveisviateclado:caminhode tabse AccessKey. Vamosfalarumpouco
maissobreasequênciadetabs,queeujulgosermaisimportante.
Ocaminhodetabsésimples: bastainseriroatributo tabindexnos
elementosHTMLcomolinks,inputsebotõesparaquefiquemacessíveisao
apertaratecla TABdoteclado.Vejaocódigoaseguir:
<a href="#" tabindex="1">Primeiro link</a>
<a href="#" tabindex="3">Segundo link</a>
<a href="#" tabindex="2">Terceiro link</a>
Percebaosvaloresdoatributo tabindex. Quandoousuárioapertar
TAB,o primeiro linkganharáfoco.Aoapertaratecla TABoutravez,o ter-
ceiro link ganharáfoco,jáqueovalor tabindexestácomo2. Aoaper-
tar TABnovamente,o segundo link ** ganhará foco, já que seu
tabindexSabendodisso,vocêpodefazerumasequênciadetabsemseusis-
tema,levandoousuárioparapontosestratégicosdoseuproduto.Issoémuito
98

## Página 105

CasadoCódigo Capítulo9. Acessibilidade
útilparatelascomformulários,porexemplo,ondeousuáriopodeevitarain-
teraçãocommouse.
Hámuitosusuáriosquetêmalgumadeficiênciamotora,comaqualé
muitodifícilmanusearomouseeautilizaç ãodotecladosetornaimprescin-
dível.Osusuárioscomdeficiênciavisualtambémutilizambastanteoteclado,
jáqueoleitordetelanarraoconteúdodoselementosqueganhamfoco,prin-
cipalmenteoslinks.
9.3 I nput Types
OHTML5iniciouseuprojetoremodelandooscamposdeformuláriosdoan-
tigoHTML.AtéacriaçãodoHTML5,nósusávamosformuláriosdamesma
formadesdeoiníciodainternet.Haviaapenasumpunhadodetiposdecam-
posqueerampossíveisdeusar.Comoavan çodainternet,essescamposse
tornaramcadavezmaislimitadoseanecessidadedenovostiposdeformulá-
riosfoiinevitável.
Hoje,osnovoscamposnãoapenasajudamnotrabalhododesenvolvi-
mento,massefocamprincipalmentenafacilidadeparapreenchermosdi-
versasnovasinformações. Camposnovoscomo: date, number, emailaju-
dammuitoemdispositivoscomtelaspequenas,modificandoasteclas.Vejao
exemploaseguir,ondeotecladomudadeacordocomoformulário.Aima-
gemdaesquerdanãotemamarcaç ãoapropriada,porissootecladoaparece
comletras.Jánasegundaimagem,oformuláriofoimarcadocomonovotipo
decampochamado number,fazendocomquemostrasseapenasnúmeros:
99

## Página 106

9.4. WAI-ARIA CasadoCódigo
Fig.9.1:Diferen çadetecladodoiPhone
EsteéolinkparaadocumentaçãooficialdoW3C,ondeháumalistacom
todosostiposdecamposquejápodemserusadosemnossosprojetos: http:
//www.w3.org/TR/html5/forms.html#states-of-the-type-attribute.
Umadica:quandoobrowsernãosuportaalgumtipodessesnovoscam-
pos, elesimplesmentemostraparaousuárioocamposimplesdetexto(
type="text").Assimnadaaparecequebradoeousuárioconsegueseguir
seufluxonormalmente. Issosechama Fault T olerance. Masaíjáéassunto
paraoutrahora.
9.4 W AI-ARIA
OHTMLserveparaapenasumacoisa:darsignificadoàinformaç ão.Elefaz
issomarcandoainformaçãocomtags.Depoisdisso,vocêescreveseuCSSeo
100

## Página 107

CasadoCódigo Capítulo9. Acessibilidade
JavaScript,queficarãocomasresponsabilidadesdeformataressainformaç ão
emanipularseucomportamento.
Opontoéqueasemânticanãoficaapenasnahorademarcarainformaç ão
comHTMLpuro.Comovocêfazparaqueumusuáriocomdeficiênciavisual
saibaqueainformaçãoqueeleprocuraestádentrodeumatab,eessatabestá
fechada?Comovocêavisaqueaquelelugarondeeleestánavegandoéolugar
maisimportantedapágina?Queaquelemontedelinksdequeoleitordetela
estáfalandoéomenuprincipaldosite?
Estendendo o significado
AWAI-ARIAserveparaestenderosignificadodasinteraçõesdoseusite.
QuandoastagsdoHTML5vieram,elasjácome çaramumtrabalhoimpor-
tantededarsignificadoàsestruturasdolayout.Vocêconseguemarcaroqueé
ummenudenavegação,umasidebar,umheader,umfooteretc.Essetrabalho
émuitoimportanteporqueajudaadefiniraimportânciaquecadaelemento
contém.AntesdoHTML5issoeraimpossível,tudoeraDIV.
AsemânticaqueasMicrodatastrazemtambémsãoumamaneiradees-
tenderosignificadodoconteúdo.Elepodeterinformaçõesimportanteseque
passamdespercebidaspelosrobôsdebuscaeoutrosmeiosdeacesso.
AWAI-ARIAvaiajudarmuitoemaplicaçõesondeainformaç ãoédivi-
didaemváriaspor çõesnatelaemdiversoselementosqueprecisamdeinte-
rações(comooclique)paraquesejavisualizada,fazendocomqueaacessibi-
lidadesejaprejudicadaeousuárionãoconsigaacessartodasaspartesdesse
layoutdemaneiralinear.Aideiaéquetodaequalquerinformaç ão,escondida
emumamodal,tab,collapsesetc.sejaacessível.
Roles, States e Properties
Paraquevocêpesquisemelhorquandoforestudaroassunto,aWAI-
ARIAdivideasemânticaemduaspartes: Roles,quedefinequetipodeele-
mentoousuárioestáinteragindoe States/Propertiesquesãosuportadaspelas
Rolesedefinemoestadodoelemento.
ComaRolevocêfalaquedeterminadoelementoéum collapse,ecomos
States/Propertiesvocêdizseessacollapseestáabertaoufechada. Issotudo
vocêvaidefinirdiretonoHTML,pormeiodosatributos.
101

## Página 108

9.4. WAI-ARIA CasadoCódigo
São4tiposderoles.Cadatipoderoleéresponsávelporumdeterminado
gênerodeelemento.
•Abstractparadefiniçãodeconceitosgerais. Nãodevemosusarpara
marcarconteúdo. Confessoqueaindaestoutentandoentenderesse
tipodeRole.“Conceitosabstratos”éalgomuitoabstratoparamim.:-)
•Widgetsparamarcarelementosdeinterfacesoltos, comocaixasde
alerta,botões,checkbox,links,tabsetc.
•Document Structureparadefinirestruturasdeorganizaçãodapágina
quenãosãointerativascomooheader,footer,sidebar,mainetc.
•Landmarkspararegiõesdepáginaquesãopontosimportantespara
ondeousuárionavegaria,porexemplo: buscas,conteúdoprincipal,
sidebar,formuláriosetc.
NãodáparamostraraquitodasasRolesqueexistemporquesãomui-
tas. Paravertodaalista,vádiretoaositedoW3C(http://www.w3.org/TR/
wai-aria/roles#roles_categorization).Lávocêvaiencontrartodasascatego-
rias.
Posso inserir W AI-ARIA via JavaScript?
Sim. MuitosatépreferemcolocarestesatributosviaJavaScript. Nãohá
problemaalgum.Insiraosatributosemcadaumadassuasfun çõesdecom-
portamento. Issofacilitaotrabalho. Poroutrolado,sevocêsabequeoseu
públicodesativaosuportedeJavaScriptdoBrowser(oqueémuito,muitodi-
fícil),prefiracolocardiretamentenocódigoHTMLdoelemento.Assimvocê
garantequeoWAI-ARIAvaifuncionarmesmoqueousuáriodesabiliteoJS.
Eu tenho alguns slides de uma apresentação sobre o as-
sunto, segue o endere ço: https://www.slideshare.net/diegoeis/
waiaria-interaes-acessveis-na-web.
102

## Página 109

Capítulo10
Pré-processadoresCSS
ImaginesevocêpudessecriarvariáveisnoCSS.Imaginetambémsevocêpu-
desseusarcondiçõescomo ifou whilenoseucódigoCSS...Essaseoutras
funçõessãopossíveisseutilizarmosumpré-processador.
Nestecapítulo,veremosbastantesobreSASS,queéopré-processador
maisutilizadoemaiscompletoqueexisteatéagora.Eutambémestoumais
familiarizadocomele,jáqueousonomeudiaadia.Existemváriosoutros
pré-processadores,comoStyluseLess,quenãovouabordaraqui,masnaes-
sênciatodostêmquaseamesmasintaxe.
10.1 P or que usar pré-processadores?
Umdosprincipaismotivosseriaautomatizareevitarrepetiç ãodecódigo.Em
algunsmomentos,emqualquerlinguagem,vocêprecisaescreverblocosde

## Página 110

10.2. UmpoucodeSASS CasadoCódigo
códigoquepodemserepetiremváriaspartesdoprojeto.Evamossersince-
ros:oCSSéumalinguagemumpoucoburraquandosetratadelógica.Tudo
émuitomanualenãoépossívelautomatizaragrandemaioriadastarefas.
Areutilizaçãodecódigoémínima,oquenosobrigaalidarcomcódigoem
excesso. Éaíqueagraçadospré-processadoressedestaca. Autilizaçãode
mixins,variáveis,funçõesecondiçõesaproximaalógicadocódigoCSS.
Outropontoéotempodemanuten ção. Apartirdomomentoemque
vocêcomeçaautilizarasfeaturesdeumpré-processador,vocêprecisaape-
nassepreocuparcompequenosblocosdecódigo.Asvariáveissãoumbom
exemplodisso. Quemnuncateveproblemasparamudarumadeterminada
corhexadecimaleprecisoumudarovalorarquivoporarquivo,linhaporli-
nha?Sevocêtivesseessacorgravadaemumavariável,bastavamudarocó-
digohexadecimalemapenasumlugaretudoestariaresolvido.
Masafun çãoprincipaldeumpré-processadoréqueeleajudaageren-
ciarseCSS.Tudonospré-processadoresépensandoemcomovocêconsegue
melhorarmaisseucódigoecomoelepodeficarmaisorganizado.Essaideia
começanamaneiracomovocêorganizaseusarquivosevaiatéaformacom
quevocêescreveseucódigo.
CSSémuitosimples. Masumamáorganizaçãopodelevarequipesin-
teirasàloucuraemlongoprazo.Ospré-processadoresajudamagerenciaras
partesfracasdoCSS,queelenãoconsegueresolversozinho.Énissoquevocê
temquesefocar.Nãoimportaqualpré-processadorvocêvaiusar,mastenha
emmentequeelenãoéumaferramentaparaescrevermenosCSS,maspara
organizarseuCSS.
10.2 U m pouco de SASS
SASSéopré-processadormaisutilizadonomomento.Existemoutroscomo
oLESSeoStylus,masoSASSqueganhouogostodosdevs. Nofinalde
tudo,elesserãopraticamenteamesmacoisa.Algumaspequenasmudan ças
drásticasentreumeoutro,masaessênciasempreseráamesma.
HojeeuusoSASSempraticamentetodososmeusprojetos.Porisso,vale
apenatentarincluirnoseustackdedesenvolvimento.Seguemalgunsexem-
plosquepodemserencontradosemoutrospré-processadorescomalgumas
104

## Página 111

CasadoCódigo Capítulo10. Pré-processadoresCSS
diferençasnasintaxe.Elesresolvemproblemasreais,quetemostodososdias
emprojetosdetodosostamanhos.
Usando variáveis
Paraentendermelhor,peguecomoexemploocódigoaseguir:
.tema-azul body {
background-color: #0176bb;
}
.tema-vermelho body {
background-color: #e3413e;
}
.tema-amarelo body {
background-color: #f8e042;
}
Reparequenósrepetimosmuitocódigonesseexemplo.Vejacomofaría-
mosissocomSASS:
$azul: #0176bb;
$vermelho: #e3413e;
$amarelo: #f8e042;
.tema-azul body {
background-color: $azul;
}
.tema-vermelho body {
background-color: $vermelho;
}
.tema-amarelo body {
background-color: $amarelo;
}
Jámelhoramosbastanteseparandooshexadecimaisemvariáveis,asquais
105

## Página 112

10.2. UmpoucodeSASS CasadoCódigo
podemosusaremqualquerlugardodocumento.Masnóspodemosautoma-
tizaraindaacriaçãodosseletores.Vejaoexemplo:
$cores: (
azul: #0176bb,
vermelho: #e3413e,
amarelo: #f8e042
);
@each $tema, $cor in $cores {
.tema-#{tema} body {
background-color: $cor;
}
}
O $temaseriacadaumadaschaves,nonossocasoazul,vermelhoe
amarelo. O $corseriacadaumdosvaloresdostemas,ouseja,osvalores
hexadecimais.Afun ção @eachestádizendoassim:acadavalordostemas
(azul,vermelho,amarelo)queencontrarnomapa $cores,repitaoblocode
código.
Vejaqueaquantidadedecódigoescritaéequivalenteeatémaiordoquea
versãodeCSSdoprimeiroexemplo.Maspensenamanuten çãodisso.Preci-
saríamosinserirumanovalinhaeadicionarumhexadecimalnovoparacriar
umacor.Afun ção @eachvaitratardecriarosblocosdeCSScomonome
dotemaeohexadecimal.
Escrevi um artigo que fala sobre como organizar temas de cores
usandoSASSemprojetoscomplexosaquinestelink: http://tableless.com.br/
utilizando-maps-sass/.
Condicionais
Masoquemedeixamaisempolgadocomospré-processadoreséapos-
sibilidadedeusarcondicionais.Fun çõescomo if, else, while, eache
for,quenormalmentevemosemoutraslinguagens,podemserusadasagora
noCSSpormeiodospré-processadores.Criarcondiçõeséincrivelmenteútil
emváriosmomentosdotrabalhocomCSS.
106

## Página 113

CasadoCódigo Capítulo10. Pré-processadoresCSS
if
Sealgoforqualquercoisadiferentede falso,executedeterminadoco-
mando.
UmusobastantesimplesédaprópriadocumentaçãodoSASS:
$type: monster;
p {
@if $type == ocean {
color: blue;
} @else if $type == matador {
color: red;
} @else if $type == monster {
color: green;
} @else {
color: black;
}
}
Comoeradeseesperar,existeum @elseparanosdartodooapoio.Esse
exemplofoibastantesimples. Sevocêtemumavariávelqualquer,nonosso
caso monster,elapodemudardevaloremdeterminadolugardocódigo.Se
mudar,háumasériedecondiçõesali.
Vamosparaumexemplomaisreal:
$color1: #f9f9f9;
p {
@if (lightness ($color1) < 30) {
background-color: white
} @else {
background-color: black
}
}
Estamosmedindoaquantidadedebrancoquehánavariável $color1,
quevaireceberumcódigodecor.Seformenorque30%deluz(claridade),
background blacknoelemento,casocontrário,background white.
107

## Página 114

10.2. UmpoucodeSASS CasadoCódigo
for
Iniciaumavariáveleexecutaumaação,incrementandoessavariávelum
determinadonúmerodevezes.Paracadarepetição,umavariáveldecontador
éusadaparaajustarocódigodesaída.
Émuitoútilparavocêfazercódigoscomooseguinte:
.item-1 {
width: 10px;
font-size: 10px;
}
.item-2 {
width: 20px;
font-size: 20px;
}
.item-3 {
width: 30px;
font-size: 30px;
}
.item-4 {
width: 40px;
font-size: 40px;
}
Vocêfariaumacondiçãoassim:
@for $i from 1 through 4 {
.item-#{$i} {
width: 10px * $i;
font-size: 10px * $i;
}
}
Outrotruqueinteressanteéque,sevocêcolocaroprimeironúmeromaior
queosegundo,assim: @for $i from 4 through 1,afun çãovaidecre-
mentaraoinvésdeincrementaravariável.Oresultado:
.item-4 {
width: 40px;
font-size: 40px;
108

## Página 115

CasadoCódigo Capítulo10. Pré-processadoresCSS
}
.item-3 {
width: 30px;
font-size: 30px;
}
.item-2 {
width: 20px;
font-size: 20px;
}
.item-1 {
width: 10px;
font-size: 10px;
}
Simplelikethat.
each
Defineumavariávelparaitemdeumalistadevalores,produzindoblocos
decódigoutilizandoosvaloresdalista.
Vamosaumexemplorápido.Paraumcódigoassim:
.tema-azul body {
background-color: #0176bb;
}
.tema-vermelho body {
background-color: #e3413e;
}
.tema-amarelo body {
background-color: #f8e042;
}
VocêteriaumSASSassim:
$cores: (
azul: #0176bb,
109

## Página 116

10.2. UmpoucodeSASS CasadoCódigo
vermelho: #e3413e,
amarelo: #f8e042
);
@each $tema, $cor in $cores {
.tema-#{tema} body {
background-color: $cor;
}
}
VocêgerenciabasicamenteumblocodeCSSeasvariáveisparaadicionar
ouremovercores.
while
Repeteumdeterminadoblocoecódigoenquantodeterminadoestadofor
verdadeiro.
Oexemplomaisbacanaquepodesermostradoaquiéacriaç ãodeum
gridbásico.Paraterumcódigocomooseguinte:
.column-grid-1{
width: 60px;
}
.column-grid-2 {
width: 150px;
}
.column-grid-3 {
width: 240px;
}
.column-grid-4 {
width: 330px;
}
.column-grid-5 {
width: 420px;
}
110

## Página 117

CasadoCódigo Capítulo10. Pré-processadoresCSS
.column-grid-6 {
width: 510px;
}
.column-grid-7 {
width: 600px;
}
.column-grid-8 {
width: 690px;
}
.column-grid-9 {
width: 780px;
}
.column-grid-10 {
width: 870px;
}
.column-grid-11 {
width: 960px;
}
.column-grid-12 {
width: 1050px;
}
Ocódigoseriaalgomaisoumenosassim:
$i: 1
$column-width: 60px
@while $i < 13 {
.grid-#{$i } {
column-width: $column-width;
}
$column-width: $column-width + 90px;
111

## Página 118

10.3. Pontosparapensar CasadoCódigo
$i: $i + 1;
}
Claro,parafazerumgridumpoucomaiscomplexo,usandoporcenta-
gens,guardandoovalordo gutteremumavariável, roasetc.vocêprecisade
umpoucomais.
10.3 P ontos para pensar
Eusempredissequeerameiocontraautilizaç ãodepré-processadores.Mas
confessoquedepoisdeusá-los,vimuitavantagemnodesenvolvimentodiá-
rio. Hámotivosparavocêpensarseéocasodevocêadotarounãoalgum
pré-processadorCSSnoseuprojeto.
OMillerMedeiros(http://blog.millermedeiros.com/about/)escreveuum
ótimo artigo com o nome deThe problem with CSS pre-processors (http:
//blog.millermedeiros.com/the-problem-with-css-pre-processors/). Láele
citaalgunsmotivosinteressantessobrenãousarpré-processadores. Sugiro
quevocêleia.
Pré-processadorespodemajudarcomotambémpodemmaltratarbas-
tanteoprojeto. Bastaumescorregãoparaqueseuprojetovireuminferno.
Mesmoassimeuincentivoquevocêexperimenteetiresuasprópriasconclu-
sões.Naspróximaslinhasdoumeusdoiscentavossobreoassunto.
Curva de aprendizado de novos integrantes
Écomumrecebermosnovosintegrantesnaequipe. Pessoasvêmevão.
Issoénormalemqualquertime.Oproblemaéquesemprequealguémnovo
chega,eleprecisaaprenderdepreferênciaomaisrápidopossívelosdetalhes
doprojeto.Prafacilitaressacurvadeaprendizado,asequipespodemmanter
ummanualexplicandoasboaspráticasdeescritadecódigo. Masnãoim-
portaquantasreuniõesvocêfaça,ocabrasóvaiconseguirconhecermesmo
otamanhodoprojetoquandocolocaramãonamassa.
Quandoocódigofoiescritosemnenhumpré-processador,acurvade
aprendizadoémuitomenor.Elenãoprecisaaprenderoscostumesdaequipe
quantoàspreferênciasdousodasfeaturesdopré-processadorescolhido.Se
112

## Página 119

CasadoCódigo Capítulo10. Pré-processadoresCSS
aequipeestiverusandoSASS,porexemplo,podeexistirumasériederegras
demixinseextendsquepodemdemorarparafazersentido.Semcomentaro
aninhamento(nesting)deseletoresparaevitarorepetiç ãodeelementos.Jáé
difícilentendertodasasrelaçõesdeelementosesuasformataçõesnamaneira
normal,imagineusandoindentaçãoparahierarquizarosseletores.
Issopodeprejudicarbastanteamanuten ção,principalmentesequema
fizerforumnovatonoprojetoque, pornãoconhecerosmiúdosdocó-
digo, podeacabaralterandoalgumvalorqueéreutilizadoemváriosmi-
xins/extendseseuscorrelatos.
Paraevitarproblemasassim,adocumentaçãodeveriasermuitobematu-
alizada,apontandotodasasrelaçõesdemixins,extends,variáveisetc. Ese
vocêjáseaventurouatentarmanterumadocumentaçãoatualizada,sabeque
équaseimpossívelter100%decomprometimentoparaatualizarosmínimos
detalhes.Principalmentedetalhesquemudamotempointeiro.
O caminho de ida é fácil, o de volta nem tanto
Quandodecidimosusarumpré-processadoréumcaminhosemvolta.
Atéondepesquisei,umavezqueseuprojetofoiescritosobasregrasde
umpré-processador,nãohácomovoltaratrás,anãoserquevocêutilizea
versãojáprocessadadessecódigo.Masaíentramosemoutroproblema:ge-
ralmentepré-processadoresescrevemmaiscódigodoquevocêescreveriama-
nualmente.Duasop ções:corrigiroexcessodecódigodoprojetointeirona
mãoouignorareseguiremfrente.
Nunca será como se fosse escrito manualmente
Comojácitamos,ocódigogeradopelopré-processadornuncaserácomo
ocódigoescritoporvocêmanualmente.Nuncavinadaquetentegerarcódigo
automaticamentefazeralgoquenãofosseduvidoso.
Háequipesquesearrependemedecidemquedestepontoemdiantees-
creverãoCSSpuro,semutilizarasfeaturesdopré-processador.Masaíperde
todaagraçaenãohávantagemnenhuma.
Vejaumexemplosimplesdeusodo mixindoSASS:
@mixin alert {
113

## Página 120

10.3. Pontosparapensar CasadoCódigo
color: red;
border: 2px solid red ;
}
.alert-default {
@include alert ;
}
.alert-special {
@include alert ;
background-color: gray;
}
Resultado:
.alert-default {
color: red;
border: 2px solid red ;
}
.alert-special {
color: red;
border: 2px solid red ;
background-color: gray;
}
Entendeaduplicaçãocódigode bordere colordasduaspropriedades?
Claro,noexemploacimaseriamuitomelhorterusadoum extendemvez
de mixin.Maseseumdesavisadocometeresseerro?
Usando extend,ficaassim:
.alert {
color: red;
border: 2px solid red ;
}
.alert-default {
@extend alert;
}
114

## Página 121

CasadoCódigo Capítulo10. Pré-processadoresCSS
.alert-special {
@extend alert;
background-color: gray;
}
Quejápodesercompiladopara:
.alert, .alert-default, .alert-special {
color: red;
border: 2px solid red;
}
.alert-special {
background-color: gray;
}
Cedo ou tarde o CSS vai amadurecer
OW3Ctemtrabalhadobastanteparaoficializaromaisrápidopossível
asnovidadesdoCSS.Osfabricantesdebrowserstambémtêmseesfor çado
paramanterseusnavegadoresatualizados,trazendosemprenovidadespara
experimentarmoseusarmosemprojetoshoje,agora.CedooutardeoCSSvai
terfeaturescomoasdospré-processadoresparanosajudarcomamanuten ção
eeconomiadecódigo.Nãoéalgoimediato,claro,massabemosquevirá.
Comcertezavaiserbemmelhordoquetemoshojeemváriossentidos.
Porissovocêpodeesperarpraver.
Concluindo
Euusoospré-processadoressemprequeposso.Emprojetospequenosou
grandes,nãoimporta. Hojemeuprocessoenvolveusar Middlemane SASS
nosprojetosdoTableless.Issomeajudoumuitonosprojetos,principalmente
nosmaiscomplexos.Paraprojetoscompoucaspessoasounosquaisapenas
euestouenvolvido,terocontroledetudoémuitoimportante.
Tenteexperimentar.FizumartigonoTablelessqueexplicacomoinstalar
SASSnasuamáquinademaneirafácil.Segueolink: http://tableless.com.br/
instalando-sass-na-maquina-video/
115

## Página 122

10.3. Pontosparapensar CasadoCódigo
Comcerteza,depoisquevocêultrapassaracurvadeaprendizado,você
nuncamaisvaiquererescreverCSSpuro.
116

## Página 123

Capítulo11
Ferramentário(Tooling)
Durantemuito,masmuitotempo,nósnãotínhamosferramentasquenos
auxiliassemnodesenvolvimentofront-end. Lembro-mequemuitosdesen-
volvedoresvibraramquandoaextensãoWebDeveloperToolbarfoilan çada
noMozilla/Firefox,poiselapossibilitavaexecutarumasériedepequenasta-
refascotidianas.Eunãoseiqualdosbrowserslan çouoWebInspector,muito
provavelmenteoOpera,masdurantemuitotempooInspectorfoinossaúnica
ferramentaalémdoeditordetextoemesmoassimerabastantelimitada.
Hojeahistóriaéoutra. Existemcentenasdeferramentasquemedema
velocidadedosite,quetestamseucódigo,testamolayoutemdiversosbrow-
sersesistemasoperacionais,aresponsividadedolayoutetc. Elasfacilitam
oseutrabalhoeeconomizamumtempopreciosoparadescobrireresolver
problemas,masprincipalmenteparamelhoraroworkflowdotrabalho.
Aminhaopiniãoédequevocênãoprecisaaprendertodasasnovasferra-
mentasetecnologiasqueexistemporaí.Vocêpodemuitobemsevirarcom

## Página 124

11.1. Grunt CasadoCódigo
algumaseaprendercoisasnovasdeacordocomasuanecessidade. Asfer-
ramentasquecitareiaquisãoasmaispopulares.Algumasdelasprecisamde
rubyou node.jsinstaladosnasuamáquina.
Alerta
Nãosesintaobrigadoaaprendertodasasferramentasdamoda.Mui-
tosdevsperdemtempopreciosodandoaten çãoparanovasferramentas
quenemserãousadaspelaequipeouquemorrerãonospróximosmeses.
Nãocaianaladainhadeaprendertudoqueapareceporaí.
Segueadicadealgumasferramentasqueestãoalgumtemponomercado
equesãoúteisparamuitosdesenvolvedores.Mas,comodisse,vejasuareal
necessidadedeaprendê-lasenãofiquetristesevocêsentirquealgumadelas
nãolheseráútil.EumesmonãousoBowerouYeoman.
11.1 G runt
Depoisquevocêterminadeescrevercódigo,háumasériedetarefasquepre-
cisamserexecutadasparaqueessecódigosejapublicadoemproduç ão.São
tarefasrepetitivasque,seforemfeitasmanualmente,podemtomarmuitodo
seutempo.ÉaíqueoGruntaparece.
O Grunt é um automatizador de tarefas
ElerodavialinhadecomandonoterminaletemoNode.jscomobase.
Automatizadoresdetarefasnãosãonovos.Sóparavocêsaber,váriasou-
traslinguagensjátinhamsuassoluçõesdeautomatizadoresdetarefas.Para
citaralguns:MakenoShell,oAntnoJavaeoRakenoRuby.
Sevocêébastantenovonaárea,talvezvocênãoestejaacostumadocom
esseworkflowdetrabalho,masgeralmentedesenvolvemososprojetosemum
118

## Página 125

CasadoCódigo Capítulo11. Ferramentário(Tooling)
ambientemontadonanossaprópriamáquinaantesdecolocaressecódigoem
produçãoparaosusuários.Porisso,imagineoprocesso:emproduç ão,ocó-
digoéconcatenado(todososarquivosdeJavaScriptedeCSSsãounificados
emumsóarquivo),ofuscado(resumindo:osnomedevariáveissãotrocados
pornomesmenores,geralmenteparaapenasumaletra)eminificado(código
semcomentários,semespaços,semquebrasdelinha). Essestrêsprocessos
nãopodemserfeitosmanualmente.OGruntentracomoaliado,fazendoes-
saseoutrastarefas.
Instalando o Grunt
OGruntéinstaladoviaNPM,queéogerenciadordepacotesdoNode.js.
SevocêaindanãotemNode.js,descubracomoinstalarnoprópriositedo
Node. É simples, basta baixar e instalar na máquina (http://nodejs.org/
download/).
Feitoisso,vocêvaiinstalarocomandodoGruntemsuamáquinacom
apenasumcomandonoterminal:
npm install -g grunt-cli
Essainstalaçãopermitequevocêrodeocomando gruntdequalquer
diretóriodamáquina.
Rodando Grunt em um projeto que já existe
SevocêjátiveremumprojetoquetemGruntinstalado,podeseguirestes
trêspassossimplesqueadocumentaçãoexplica:
1) VáparaodiretóriodoprojetoqueusaGrunt;
2) Instaleasdependênciasusandoospluginscom npm install;
3) Rodeocomando grunt.
Issovaiexecutartodasastasksconfiguradasparadispararpordefault
quandorodamosocomando grunt.
Agora,sevocêquerfazeralgodozero,vamosparaopróximopasso.
119

## Página 126

11.1. Grunt CasadoCódigo
Rodando Grunt do zero
Primeiro,vocêprecisafazerumsetup,ondevocêvaideclararquaissãoas
dependênciaseasinformaçõesdequeseuprojetovaiprecisarpararodaras
tarefasdoGrunt.Essearquivoéchamadode package.json.
O package.jsonéumarquivousadopeloNPMparaguardarasinfor-
maçõesdoprojeto.Vocêirálistartodosospluginsdentrodessearquivo,na
opção devDependencies.
{
"name": "LocawebStyle",
"description": "A front-end framework of behavior and style.",
"homepage": "http://locaweb.github.io/locawebstyle",
"keywords": [],
"author": "Locaweb Front-end Team <frontend@locaweb.com.br>",
"contributors": [],
"devDependencies": {
"grunt": "^0.4.5",
"grunt-contrib-jasmine": "^0.8.2",
"grunt-contrib-jshint": "^0.11.0",
"grunt-contrib-watch": "^0.6.1",
"grunt-jasmine-runner": "^0.6.0",
"jasmine-jquery": "^2.0.6"
},
"repository": {
"type": "git",
"url": "git://github.com/locaweb/locawebstyle.git"
},
"version": "3.7.0"
}
VocêvaicolocaressearquivodentrodoRootdoseuprojeto.Juntamente
comoutroarquivochamado Gruntfile.js. Rodandoo npm install
nomesmodiretórioqueessearquivo,elevaiinstalartodasasdependências
necessárias.
Existempoucospassosparavocêcriarum package.json:
• Rodando ogrunt-init, será criado automaticamente um
package.jsonespecíficoparaseuprojeto;
120

## Página 127

CasadoCódigo Capítulo11. Ferramentário(Tooling)
• Rodandoumnpm init,serácriadoumarquivobásico;
• Oupode-seiniciarcomocódigodeexemploaseguir,comoaprópria
documentaçãorecomenda:
{
"name": "my-project-name",
"version": "0.1.0",
"devDependencies": {
"grunt": "~0.4.5",
"grunt-contrib-jshint": "~0.10.0" ,
"grunt-contrib-nodeunit": "~0.4.1",
"grunt-contrib-uglify": "~0.5.0"
}
}
Quandovocêquiserinstalarumnovoplugin,bastausarocomando npm
install <nome do plugin> --save-dev.
Aflag --save-devinstalaopluginejávaigravaradependênciacorre-
tamenteno devDependencies.
Feitoisso,éhoradeirparao Gruntfile.js.
Criando o Gruntfile.js
O arquivo Gruntfile.js (que pode ser chamado de
Gruntfile.coffee, se você usar CoffeScript), é composto por algu-
maspartes:
• Umafunçãoqueenvolvetudo,chamadadefun çãode“wrapper”;
• Configuraçãodoprojetoedastarefas;
• Carregamentodospluginsedastarefas;
• Tarefascustomizadas.
Umexemplodadocumentaçãomostracomoseriaum Gruntfile.js
configuradopararodaroUglify,umataskqueminificaeconcatenaseuJa-
vaScript.
121

## Página 128

11.1. Grunt CasadoCódigo
module.exports = function(grunt) {
// Project configuration.
grunt.initConfig({
pkg: grunt.file.readJSON('package.json'),
uglify: {
options: {
banner: '/*! <%= pkg.name %>
<%= grunt.template.today("yyyy-mm-dd") %> */\n'
},
build: {
src: 'src/<%= pkg.name %>.js',
dest: 'build/<%= pkg.name %>.min.js'
}
}
});
// Load the plugin that provides the "uglify" task.
grunt.loadNpmTasks('grunt-contrib-uglify');
// Default task(s).
grunt.registerTask('default', ['uglify']);
};
Afunçãowrapperéessaaqui:
module.exports = function(grunt) {
// Aqui vai o resto do código
};
Parahabilitarastasks,vocêprecisacarregaropluginqueprovêadeter-
minadatask.SuponhaquevocêqueiracarregaressatarefadeUglify,alinha
aseguiréinseridanofinaldoprojeto,comononossoexemploinicial:
grunt.loadNpmTasks('grunt-contrib-uglify');
Feitoisso,vocêjáconseguerodarnoterminalum grunt uglify no
seuprojeto. Elerodarátodaaconfiguraçãodeterminadadentrodatarefa
uglify.
122

## Página 129

CasadoCódigo Capítulo11. Ferramentário(Tooling)
Conformevocêvaiinserindomuitastarefas,écomumquererfazertasks
customizadas. Porexemplo,fazerumatarefaquerodeapenasostestesde
JavaScriptcomocomando grunt test seriaalgoassim:
grunt.registerTask('test', ['uglify, jasmine']);
Nãovoumeaprofundarmuitoaquiporqueseriareescreverumatradu-
çãodadocumentação,porissoaconselhoquevocêleiaadocumentaç ão. É
bastantesimples.
OGruntéumaferramentaquevaleapenausar.Eurecomendodaruma
olhadacuidadosanaapresentaçãodoAlmirFilho(http://bit.ly/gruntocara)
. VocêvaientendertodaafacilidadequeoGruntpodetrazerparaoseu
workflow.Vejaalgunslinksinteressantesparavocêestudar:
• Documentaçãooficial:(http://gruntjs.com/getting-started)
• VejaosslidesdaapresentaçãoqueoAlmirFilhofeznolink(http://bit.
ly/gruntocara)
• ArtigodoTablelessdoVagnerSantana: GRUNT Você deveria estar
usando(http://tableless.com.br/grunt-voce-deveria-estar-usando/)
• Automação de Build de Front-end com Grunt.js (http://bit.ly/
automacaogrunt)
• Siteoficialcomadocumentação(http://gruntjs.com)
11.2 B ower
Nãoéincomumusarscriptseframeworksdeterceirosemnossosprojetos.
Dependendodotrabalho,sevocênãofororganizado,essecódigoficabem
difícildegerenciar. Algunsdelesprecisamseratualizadosouvocêprecisa
baixaroutrasdependências.OBowerfoicriadopelopessoaldoTwitterpara
ajudarodesenvolvedoragerenciartodasassuasdependências.
Vocêsabequequalquerdesenvolvedortempreguiçadeatualizarbibliote-
cas,pormenoresqueelassejam.QuemnuncadeixouojQuerydesatualizado
poranosnapastadoprojetoporpurapreguiç adebaixaranovaversão,entrar
123

## Página 130

11.2. Bower CasadoCódigo
noprojeto,apagaraversãovelhaecopiaranova? Porquenãoautomatizar
esseprocesso?
OBoweréumgerenciadordepacotesclient-side.Ébaseadoemnode.jse
comooGrunt,rodavialinhadecomando.SevocêjátemoNPMnamáquina,
bastairnoterminaledigitar npm install -g bower. Depoisécorrer
paraaalegriainstalandosuasdependências. Coisasimplesassim: bower
install jquery epronto.
Hátambémumarquivochamado bower.jsonqueéoseumanifesto
dedependências,ouseja,quandooBowerforexecutado,elevaiinstalarau-
tomaticamentetudooqueestálistadono bower.json.Segueumexemplo:
{
"name": "app-name",
"version": "0.0.1",
"dependencies": {
"sass-bootstrap": "~3.0.0",
"modernizr": "~2.6.2",
"jquery": "~1.10.2"
}
}
Umaexplicaçãorápidadecadapontoali:
•nameéonomedasuaaplicação.
•versionéaversãodosuaaplicação.
•dependenciessãoospacotesdedependênciasnecessáriasparasuaapli-
caçãorodar.
Acoisatodaébastantesimples,masvaleapenalermaisparaseaprofun-
dar:
• Slides de uma apresentação do Nando Vieira: (http://bit.ly/
usandobower)
• BowernaPrática(http://tableless.com.br/bower-na-pratica/)
124

## Página 131

CasadoCódigo Capítulo11. Ferramentário(Tooling)
• Configurando o Bower e o Polymer (http://tableless.com.br/
configurando-bower-e-polymer-2/)
• SiteoficialdoBowernolink(http://bower.io)
11.3 D ev Inspector
TodososbrowserstêmumaferramentaútileindispensávelchamadaInspec-
tor.OInspectoréaferramentamaisusadaparadebugaroseucódigofinal,
geradopelobrowser. Hoje,amaioriadosbrowserstemsuaprópriaferra-
mentadeinspe ção.OFirefoxincorporouaFirebug(https://addons.mozilla.
org/pt-br/firefox/addon/firebug/),oIEtemaDeveloperTool(http://msdn.
microsoft.com/en-us/library/dd565628(v=vs.85).aspx),oChromeeoSafari
têmowebinspector(http://trac.webkit.org/wiki/WebInspector)dopróprio
Webkit.OOperausaoDragonfly(http://www.opera.com/dragonfly/).
OInspectoréútiletalvezomaisútildetodasasferramentasquevocê
podeencontrar.Comelevocêanalisa,debuga,modifica,testa,emonitoraseu
códigoclient-side.Nãohácomodesenvolverwebsiteshojeemdiasemaajuda
doInspector.Elevailhemostrarcomoocódigoéexatamenterenderizadonos
browserse,seprecisarfazeralgumamodificação,elemostraráoresultadona
hora,diretonobrowser.
VocêvaiconseguirmodificaroCSS,mexernoHTML,debugaroJavaS-
cripteterresultadosinstantâneos,verificandotodososefeitosdasmodifi-
caçõesnolayout. CadabrowsertemumInspectorcomumacaracterística
diferente. OInspectordoChrome,porexemplo,éótimoparaanalisarper-
formance.
125

## Página 132

11.3. DevInspector CasadoCódigo
Fig.11.1:TimelinedoChromeDevTools
JánodoFirefox,háumaanálisedositeondeelerepresentaoselementos
dolayoutemformato3D.Muitoútilemwebsitescomplexos.
126

## Página 133

CasadoCódigo Capítulo11. Ferramentário(Tooling)
Fig.11.2:Representação3DdoFirefoxparafacilitarodebugdolayout.
OInspectoréoresponsávelporfazervocêusarumbrowserparadesen-
volvereoutrobrowserparanavegarnainternetcomoumusuárionormal.Di-
versosdesenvolvedoresusamoChromecomobrowserdedesenvolvimentoe
oFirefoxcomobrowserpadrãoparanavegar.
LeiamaissobreoInspector:
127

## Página 134

11.4. Consoledosbrowsers CasadoCódigo
• Page Inspector no MDN:https://developer.mozilla.org/pt-BR/docs/
Tools/Page_Inspector
• Ferramentasesitesparatornarmaiságiloseudesenvolvimento:http:
//bit.ly/1xxphTM
• Meet your Web Inspector:http://ruby.bastardsbook.com/chapters/
web-inspecting-html/
11.4 C onsole dos browsers
TodososInspectorsdosbrowserstêmumaferramentachamadaConsole.O
ConsoleserveparadebugardeformamaisespecíficaoseucódigoJavaScript
etambémoDOMdoHTML.Existemvárioscomandosetruquesusandoo
console,nãovoufalarsobretodos.Nofinaldestase çãoháumalistadelinks
paraestudos,indicandooutrostruquesecomandos.
console.log()
VoumebasearnoChrome,queéumdosbrowsersmaisusadospelos
devs.ParaabriroconsolenoChromeuseoatalho(nomac) cmd + option
+ J.Oucliquenateladobrowsercomobotãodireito,váaté Inspect Element
ecliquenaaba Console.
O console.log()vairetornarumamensagemnoconsole.Simplese
fácil. VamosfazerumarquivoHTMLsimplescomooseguinte. Depoisde
criado,abra-onoseubrowsereabraoconsoleparavisualizarosresultados.
<!DOCTYPE html>
<html>
<head>
<title>Teste de Console</title>
</head>
<body>
<p>Testando o console. Show!</p>
<script>
128

## Página 135

CasadoCódigo Capítulo11. Ferramentário(Tooling)
(function(){
console.log('Hello Console!');
})();
</script>
</body>
</html>
Eleapenasmostrouamensagemquecolocamoscomoparâmetro:
Fig.11.3:Mensagembásicanoconsole.
Vocêpodemostrarovalordeumavariávelsequiser:
129

## Página 136

11.4. Consoledosbrowsers CasadoCódigo
Fig.11.4:Exibindoumavariávelnoconsole.log()
Vocêpodetambémconcatenarumastringusandováriostiposdevalores
emapenasumachamadade console.log:
var userName = 'Diego Eis';
var userAge = 30;
console.log('O usuário %s tem %d anos.', userName, userAge);
Oresultadoéesteaqui:
130

## Página 137

CasadoCódigo Capítulo11. Ferramentário(Tooling)
Fig.11.5:Console.logexibindoresultadodeconcatenaçãodevariáveis.
Notequeoparâmetro sformataráseuvalorcomoumastring.Oparâ-
metro dformataráovalorcomouminteiro.Claro,nemprecisodizerquesó
vaiservirparanúmeros.
console.info() e console.error()
Estes dois funcionam da mesma maneira que oconsole.log(),
mas eles têm uma função mais descritiva. Geralmente, usamos o
console.log()paramostrarqualquertipodemensagememuitasve-
zes misturamos mensagens de erro e as informativas no console. O
console.error()eo console.info()servemparadiferenciarmosas
mensagensdeerroseinformativasdasmensagensnormais.Vejaadiante:
function isEqualFour(){
var number1 = 2;
var number2 = 1;
console.log('A soma deve ser igual a 4.', 'Variável 1:',
number1, 'Variável 2:',number2);
if(number1 + number2 == 4) {
console.info('CORRETO! O valor é 4!');
} else {
131

## Página 138

11.4. Consoledosbrowsers CasadoCódigo
console.error('ERRADO! A soma dos valores é ' +
(number1 + number2) + '.' );
}
}
isEqualFour();
Vejacomoficariaasaídanoconsoleusandoo info():
Fig.11.6:Oconsoletrataoconsole.info()comoumamensagemdeinforma-
ção.
Agorao console.error():
Fig.11.7:Oconsoletrataoconsole.info()comoumamensagemdeerro.
NoLocawebStyle,oframeworkfront-enddaLocaweb(http://locaweb.
github.io/locawebstyle/),nósusamoso console.info()parainformarao
devcuriosoquaismódulosforaminicializadosnocarregamentodapágina:
132

## Página 139

CasadoCódigo Capítulo11. Ferramentário(Tooling)
Fig.11.8:Exemplodeconsole.info()usadonoLocawebStyle
console.count()
O count()doconsoleémuitoútil.Emalgumasocasiões,vocêprecisa
saberquantasvezesumafun çãofoiexecutadaouquantasvezesoscriptpas-
souporalgumlugarespecíficodasuafun ção.Emvezdeinserirumasériede
console.log()nocódigoeficarcontandodepoisnoconsole,bastausaro
console.count().
Ocódigo(horrível)aseguirteriaoretornovistocomonaimagem:
function teste(){
console.count('Chamando a função teste()');
}
function chamaTeste() {
teste();
}
function init(){
teste();
chamaTeste();
}
init();
133

## Página 140

11.4. Consoledosbrowsers CasadoCódigo
Fig.11.9:Comooconsole.count()éexibido.
console.dir()
O console.dir() vai retornar uma representação de um objeto
DOM como se fosse um objeto JavaScript. Basta digitar no console ou
usardentrodesuafun çãodamesmaformaqueo console.log(), só
que,comoparâmetro,vocêpassaráumobjetodoDOM.Vejaumexemplo,
ondemostreioretornodarepresentaç ãodo BODYdigitandoocomando
console.dir(document.body):
Fig.11.10:Outputdecomooconsoletrataafun çãoconsole.dir()
134

## Página 141

CasadoCódigo Capítulo11. Ferramentário(Tooling)
Monitorando eventos via console
Há também uma função do console muito interessante chamada
monitorEvents. Essa função ajuda a monitorar eventos, dando infor-
mações específicas sobre os elementos e sobre os eventos quando eles
são disparados. Abra seu browser console e experimente o comando
monitorEvents(window, "resize”);. Vocêvaimonitoraroevento
resizedoelemento window. Todavezqueajanelaéredimensionada,o
eventoédisparadoeasinformaçõessobreelesãomostradasnoconsole.Veja
aimagemaseguircomoseriaoresultadonoChrome:
Fig.11.11:Consolelistandooeventoresizetodasasvezesemqueeleacontece.
Vocêtambémpodepassarumarraydeeventosparaummesmoelemento.
Porexemplo,monitoraroseventos mouseupeo mousedownno body:
135

## Página 142

11.4. Consoledosbrowsers CasadoCódigo
Fig.11.12:Agoramostrandotodasasvezesemqueoseventosmouseupemou-
sedownacontecemnoBody.
Sãocomandosmuitosimplesequenostrazemumagrandeajudadurante
otrabalhododiaadia.
Existemváriosoutrasfunçõesdoconsoletãoúteiscomoessas.Vejaalista
completaaqui: https://developer.chrome.com/devtools/docs/console-api
Muitosimpleseprático. Segueumalistacommaislinksparavocêse
esbaldar:
• Chrome Tips and Tricks Console:https://developer.chrome.com/
devtools/docs/tips-and-tricks
• Using the Console:https://developer.chrome.com/devtools/docs/
console
• Firebug Console Tips: http://www.sitepoint.com/
firebug-console-tips/
• HowtodebugyourjQuerycode: http://msdn.microsoft.com/en-us/
magazine/ee819093.aspx
• BreakpointactionsinJavaScript:http://www.randomthink.net/blog/
2012/11/breakpoint-actions-in-JavaScript/
136

## Página 143

CasadoCódigo Capítulo11. Ferramentário(Tooling)
• Commando Line Inspect Object:https://developer.chrome.com/
devtools/docs/commandline-api#inspectobject
11.5 S obre o uso do terminal
Escreveremalgumterminalésempreumdesesperoparaosiniciantes.Mas
saibaquesemelevocênãovaimuitolonge.Vocêatéconseguesevirardurante
umtempo,massevocêrealmentequerexperimentarnovastecnologiasna
áreadefront-end,vaiprecisarseaventurarnoterminal.
Sevocêquiserusaralgumpré-processador,rodartestes,terpráticacom
GIT,instalargeradoresdearquivosestáticoscomooMiddlemanouusarcoi-
sascomoYeoman,Grunt,Gulp,Jasmineetc.,vocêvaiprecisarmeteramão
noterminal.Esabedeumacoisa?Depoisquevocêseacostuma,vocêsesente
naMatrix.
Outromotivoéquedependendodoprojetoquevocêseenvolver,princi-
palmenteseforemRuby,Pythonecoisasdessetipo,oterminalseráindispen-
sável.Desdeiniciaroprojeto,debugaralgunserros,atualizardependênciase
váriasoutrastarefasserãorecorrentes.Namaioriadasvezes,vocêvaiprecisar
acessaroterminalparaconfiguraremanterseuambientefuncionando.
Elenãoédifícildeusar.Nocome ço,vocêpodeatéseassustarquandovê
alguémmaisexperientefuçandoaquelemontedeletrasnatela,masnãose
amedronte,namaioriadasvezesocarasóestáescaneandoatelaprocurando
porpalavras-chavesoualgumamensagemdeerro.
Maseutenhoumacoisatristeparadizer: existempoucostutoriaisem
português que ensine o básico para iniciantes. Neste link (http://bit.ly/
1u3EyKN)vocêencontraoscomandosbásicos.
Eu realmente sugiro que você tente perder o medo de abrir o ter-
minal e tente estudá-lo. Por enquanto, fica registrada aqui a im-
portância do terminal para sua carreira. Este link vai ajudar muito
noinício:https://linux.ime.usp.br/\char126lucasmmg/livecd/documentacao/
documentos/terminal/Terminal_basico.html.
Diferença entre Shell e Bash
Vocêjápodeterseconfundido,maslávai:Shelléuminterpretadorde
137

## Página 144

11.5. Sobreousodoterminal CasadoCódigo
comandosentreocomputadoreousuário.Vocêtemváriostiposdeinterfaces
parainteragircomoShell,comooBash,escritopeloBrianFoxparaoprojeto
GNU.
Emumaanalogiabembásica:écomoseoShellfosseosistemaoperaci-
onaleoBashfosseasuainterfacegráfica.
VocêpodeusarváriostiposdeinterpretadoresShell,sendoqueo tcsh
éoquevemporpadrãonosMacs.Paravocê,agora,nesseinício,nãoseape-
gueaisso. Oscomandosbásicosserãoosmesmosentreasinterfacesepor
enquantovocênãovaisentirdiferen ça.
• Apresentação de introdução aos comandos do Linuxhttp://bit.ly/
1BPstNw
• DiferençaentreTerminal,Shell,TTYeConsole http://bit.ly/1wSSvye
138

## Página 145

Capítulo12
Produzindositescomcódigo
estático
Oprimeiroproblemaquetemosquandoiniciamosaproduç ãodeumsiteé
comoresolveraspartesdelayoutquesãorepetidasemtodasaspáginasdo
projeto,porexemplo:header,footer,sidebareessascoisas. Jáviváriosdos
meusalunosmantendositescomdezenasdearquivosHTML,semnemao
menosusarumsimples includedePHP.
Usar includesdoPHP(ouqualqueroutrocomandodequalquerou-
tralinguagemquefaçaamesmacoisa),mesmoquesejaalgoamador,resolve
apenasumdosproblemas.Osegundoproblemaera:comoentregarissopara
ocliente?Eunãopoderiasimplesmenteenviarumpacotecomváriosarqui-
vos .phpparaumclientequetrabalhavacomASPouPython. Seeleme
contratouparapassarumPSDparaHTML,precisoentregarparaeleastelas

## Página 146

12.1. Paraosnovatos:UsandoIncludesPHP CasadoCódigo
doprojetoemHTML/CSS/JavaScriptestático.
Logocomeçamosausaro wgetparapercorreroprojetoetransformaras
páginasPHPemHTMLestático.Nãodemoroumuitoparadesistirmosdisso.
Emborao wget(ouatéo httrack)façaquasetudoautomaticamente,esse
workflownãoeraoideal.Precisávamosteralgomaisinteligenteparaexecutar
esseprocesso.Foiaíqueconhecialgumasferramentasparaageraç ãodesites
estáticos,comooJekyll,Middlemanealgunsoutros.
Sevocêébemnovatoainda,vouexplicarcomoseusa,maisomenos,
o includedoPHPlogoaseguir.Massevocêjácome çoufaztemponesse
mundoenãoconheceoMiddlemannemoJekyll,pulealgunsparágrafose
leiamaissobreestesgeradoresdesitesestáticos.
12.1 P ara os nov atos: U sando Includes PHP
OPHPéumalinguagemserver-sideetalvezamaispopularnomundo
todo.Vocênãoprecisaserprogramadorparaentendercomofuncionamos
includes,mas você precisa pelo menos aprender a instalar o Apachepara
rodaroPHPnasuamáquina.
Includesignifica incluiremportuguês.ÉumcomandodoPHP(que
tambémexistecomoutrosnomesemoutraslinguagensserver-side)quein-
cluiumdeterminadoarquivodentrodooutro. Coisasimples:imagineque
vocêtemumcódigoHTMLassim:
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Document</title>
</head>
<body>
<header>
<h1 class="logo">Logo do site</h1>
<ul class="menu">
<li><a href="#">Home</a></li>
<li><a href="#">Contato</a></li>
140

## Página 147

CasadoCódigo Capítulo12. Produzindositescomcódigoestático
</ul>
</header>
<p>Aqui vai o resto do site...</p>
</body>
</html>
Ocódigodo headerérepetidoemtodasaspáginas,comonoexemplo
queciteinoiníciodocapítulo.Aideiaaquiécopiaressecódigodo header
paraumarquivo,quepodeserchamadode header.php,eoincluiremos
emvezdocódigoliteral.Assim:
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Document</title>
</head>
<body>
<?php include "header.php" ?>
<p>Aqui vai o resto do site...</p>
</body>
</html>
Agora,todavezqueprecisarmexernocódigodocabe çalho,vocêsópre-
cisamodificarocódigodoarquivo header.phpetodasaspáginasestarão
atualizadas.
Esteéatécnicamaisbásicadetodaseprovavelmentevocêjáatédeve
trabalhardessaforma.Seesteéoseucaso,vamossubirumnívelagora.
12.2 G erando sites estáticos com Middleman ou
Jekyll
Aqui,vocêjáprecisanomínimoentendercomoinstalarumaGEMdoRuby.
141

## Página 148

12.2. GerandositesestáticoscomMiddlemanouJekyll CasadoCódigo
MiddlemaneJekyllsãoduasGEMSdoRubyquefazemamesmacoisa:
criamsitescomarquivosestáticos.OquevaidecidirsevocêvaiusaroMid-
dlemanouoJekyllépuramentegosto.EucomeceicomoJekyll,masdepois
mudeiparaoMiddleman,quesemostroumaisflexível. Mastantofazqual
vocêvaiusar,oqueinteressasãoasvantagensqueelesproporcionampara
projetosdesitesdepequenoeàsvezesatédemédioporte.
Aideiaéquevocêproduzaumsiteestático,sembancodedadosalgum,
comarquivostotalmentemodularizados,ondealógicanãoestánoserver,
masnosprópriosarquivos. Sevocêprecisafazerumsitepequeno,institu-
cional,semmuitafirula,umsiteestático,comHTML,CSSeJavaScriptéo
suficiente. NãoénecessáriosubirumWordpressouqualqueroutroCMS
complexo,queprecisadeumservidorparrudocombancodedados. Seé
simples,mantenhasimples.
Estrutura de diretórios
Aestruturadediretóriosdosdoisébemparecida.Segueumexemplode
comoseriaodeumprojetoemJekyll.
142

## Página 149

CasadoCódigo Capítulo12. Produzindositescomcódigoestático
Fig.12.1:Comparandoaestrutura,oJekyllparecesermaissimples.
Aestruturadepastaspodeserumpoucodiferenteentreosdois,maseles
têmmuitoemcomum. Percebaqueosdoispossuemumapastachamada
layout.Elaéondeguardamosostemplatesdaspáginas.LayoutsdaHome,
Internaetc.,sãolayoutscompadrõesdiferentes,éaliqueguardaremosesse
código.Vejaumexemplodo default.htmldoJekyll:
{% include header. html %}
{{ content }}
143

## Página 150

12.2. GerandositesestáticoscomMiddlemanouJekyll CasadoCódigo
{% include footer. html %}
AgoraumexemplodoMiddleman:
<%= partial 'partials/header'%>
<%= yield %>
<%= partial 'partials/footer'%>
TodososgeradoresdearquivosestáticossebaseiamemumtipodeTem-
plate. OTemplateécomovocêvaimanipulareusarasinformaçõesdoseu
site.OtemplatepadrãodoMiddlemanéERB,jáoJekyllusaumamarcaç ão
chamadaLiquid(http://liquidmarkup.org),queébaseadaemRuby,masque
separecemaislinguagensdetemplate,comooMustache.OtemplateLiquid
ébastanteusadoemprojetoscomShopifyeSpree.
Ambososgeradoresfuncionamdeformamuitosimilar.Sugiroqueex-
perimenteosdoisparatomarsuadecisãofinal.
Sem banco de dados. Y eah!
Aestruturadecódigodosarquivosémuitosimplesdeseentender,mas
paraalgunspodeserumpoucoestranhapornãoterfamiliaridadecomestru-
turasdedadoscomoYAML.Masissoésimplesevocêaprenderápido,tenho
certeza.Continuelendoparavocêvercomoéfácil.
Paracomeçar,vocênãomantémumbancodedadoseéissoquefaztoda
agraça.Oconteúdodoseusiteficaguardadonosarquivosdecadapágina.
VocênãoprecisalevantarumservidordeMySQL.Todasasinformaçõesdo
siteestarãonosarquivosquevocêcriarparacadapágina. Ouseja,nadade
queries,nadadetemplatestagsdoWordPress.
Um pouco sobre Y AML
OformatoYAMLéconhecidopelafacilidadedeleitura. Elefoicriado
paraestruturarmosinformaçãodemaneiraquesejafácildeentendereescre-
ver.Ouseja,eleéumformatosimplesparaescrevermosmanualmente,mas
quetambémpossamosmanipularviaprogramação.
144

## Página 151

CasadoCódigo Capítulo12. Produzindositescomcódigoestático
QualquerarquivoquecontémumblocoYAML–quegeralmenteécha-
madode front-matter–seráprocessadocomoumarquivoespecial. O
front-matterprecisaseraprimeiracoisadoarquivoedeveestaremumfor-
matoválidodeYAML.Todapáginadoseusite,tantonoJekyllquantono
Middleman,precisacome çarcomumaestruturaassim:
---
title: Home
layout: default
---
Simples?Oblocoédemarcadopelostrêstraçosnocomeçoenofim.T em
quesertrêstraços. Nemmais,nemmenos. OcódigoYAMLsãoasduas
variáveislayoute title.
Ambosossistemasusamessanotaçãoparaorganizarseusarquivosein-
formações.Vocêpodedefinirvariáveisemcadaumdosarquivosparafazer
condiçõesnaspáginas.Seemumapágina,porexemplo,euqueroqueaside-
barapareça,anotaçãoYAMLdelaseráalgoassim:
---
title: Contato
layout: interna
sidebar: true
---
Avariávelsidebarcomovalor falsefoicriadapormim.Notemplate,
usareialgoparecidocomisso,noMiddleman:
<% if current_page.data.sidebar? %>
_A chamada do arquivo da sidebar vai aqui._
<% end %>
Lindoesimples.Quandobuildaroprojeto,osistemajávaicompilaros
arquivosdamaneiracorreta,comocódigosidebar,nolugarquevocêpediu.
Aliás,parafazerobuildémuitosimples. NoMiddlemanbastausaro
comando middleman build.Elevaicompilartodooprojetoecolocaros
arquivosprontosparaodeploydentrodapasta build. JánoJekyll,basta
rodarocomando jekyll.Elevaijogarosarquivosprontosnapasta _site.
145

## Página 152

12.2. GerandositesestáticoscomMiddlemanouJekyll CasadoCódigo
Agora,seoclientequiserumpaineladministrativoparacontrolarocon-
teúdodosite,aínãotemjeito,aconselhoausaroWordpress. Euutilizoo
Middleman/Jekyllparaprojetosemqueoclientepedeparaentregarosar-
quivosHTMLestáticos.ComogeralmenteusoGIT,douparaeleocontrole
dorepositóriodoprojeto,contendoosarquivosdedesenvolvimento,istoé,o
códigodoMiddleman/Jekyll,etambémosarquivosdoúltimobuildfeito.
Estafoisóumapequenaintroduçãosobreosgeradoresdesitesestáticos.
Eusugiroquevocêleiaadocumentaçãodecadaum.Nãoémuitodifícilde
entenderevocêconseguefazerumtesterapidamenteparaaprendercomo
funcionam.
• DocumentaçãodoJekyll(http://jekyllrb.com)
• MarcaçãoLiquidpeloJekyll(http://liquidmarkup.org)
• DocumentaçãodoMiddleman(http://middlemanapp.com)
• Listagem indicando vários outros geradores (https://www.staticgen.
com)
146

## Página 153

Capítulo13
Compartilhandooquesabe
Vocêjáseperguntouporquetemalgunsdesenvolvedoresmaispopulares
queoutros? PorqueexistemváriosZenos,NandoseShiotasporaí? Todos
elestêmumacaracterísticamuitoevidente:elescompartilhamconhecimento.
Elesensinamalgoparaalguémtodososdiasefazemissonãoapenasporque
elessãosolidáriosbonzinhos,masprincipalmenteporqueissoaumentaoco-
nhecimentodeles.Éumprocessonatural.
Um tweet do @fnando
“Achoqueprecisoescreverumartigosobreflexbox... temmuita
coisa que ainda fico viajando. :/”https://twitter.com/fnando/status/
566233046102597633

## Página 154

CasadoCódigo
Pareceóbvio,masnãoé:quandovocêcompartilhaconhecimento,você
aprendemais.Nãoseicomoissofuncionaedevehaverummontedeartigos
científicosabordandooassunto,masofatoéque,cadavezquevocêensina
alguém,inevitavelmenteabsorvemaisconhecimento.Esseéummecanismo
naturaleincrívelquetodomundopossui.Oprocessodeensinofazvocêpen-
sarmaisemelhor.Eleoobrigaapesquisarprofundamentesobreoassunto.
Cadavezquevocêescreveumartigoouplanejaumapalestra,vocêpre-
cisaresumirgrandesassuntosempequenasideias.Vocêcriaanalogiaspara
facilitaroentendimentodagalera.Játentouexplicaroqueéeparaqueserve
apropriedade float?Tenteexplicarcomdetalhesparavocêmesmo,nafrente
doespelho,comofuncionaequaladiferen çadosvalores relativee absolute
dapropriedade position;emborasejaalgosimples,vocêvaiprecisarpensar
emumaexplicaçãofácildeentender.Éumexercíciointeressanteequeabre
horizontesqueamaioriadosdevsnemimagina.
Vocênãoprecisasearriscarlogodecaraafazerpalestras.Mascomecees-
crevendoumartigo.ComecepublicandoumpedaçodecódigonoGistouem
umJSFiddlequalquer.Nãotenhamedodoseucódigooudasuaescrita.Tudo
issovaimelhorarcomopassardotempoevocêprecisacome çardealgumlu-
gar.Vocêaprendemaislevandobordoadadoscríticos—etambémdosTrolls
—doqueguardandoseustextosecódigosapenasparavocê. Nadamelhor
doqueteralguémparaapontarseuserros.Claro,sevocêtiverumamigoou
tiveramizadecomoutrodesenvolvedor,muitomelhorpediraopiniãodele
antesdesejogarparaosleões.
Masmeuapelonestecapítuloésimples: compartilheoquevocêsabe.
Simplesassim.OTablelessnasceuexatamentedessaforma,assimcomová-
riosoutrosblogs.Diversosdesenvolvedoressãopopulareshojeporqueme-
teramascarasempalestrasnoseventospelopaís. Querfalarparapoucas
pessoasantesdeenfrentar100,200,300ouvintes?Compare çaemumencon-
trodedesenvolvedores.VáriascidadestêmMeetupsondevocêpodetratara
timidezfalandopoucaspalavrasparapoucaspessoas.Apenascomece.
148

## Página 155

Capítulo14
Textosextras
EstessãoalgunstextospublicadosnoTableless,quetalvezvocênãotenha
lidoequesãoimportantesparavocêqueestácome çando.Tratammaissobre
comportamentoemercadodoquedeassuntostécnicos.
14.1 Ú ltimo conselho: não queira ser o próximo
Zeno
Quandomonteiestetítuloeusabiaqueiaserpolêmicoequehaveriaum
burburinhonoscorredoresdasinterwebs. Esabedeumacoisa? Estoume
lixandoparaqueosoutrosfalamporaí.
Sobre admitir que você é popular
QuandoconverseicomoZenohorasdepoisdetertidoaideia,expliquei

## Página 156

14.1. Últimoconselho:nãoqueiraseropróximoZeno CasadoCódigo
osmotivosparaeleecomentamossobrecoisasqueacontecemconoscopor
causadessa“popularidade”naárea.Eurealmentenãoqueroquevocêsejao
próximoZenoRocha.Nãomesmo.OZenoéoZeno.Elepercorreuocami-
nhodele.Chegoulongeeseiquevaichegarmaislongeainda.Masumacoisa
écerta:talvezvocêcheguemaislongesendovocêmesmodoquequerendo
seroZeno.
Issoédifícil.Bastante.Comovocêdizquevocêépopularnaáreaemque
atuasemparecerarrogante,prepotente,malaouummetidodenarizempi-
nado?Nãodá.Agaleravaiinterpretarmal.Eununcasoubefazerissoenão
seifazeratéhoje. Époressemotivoquemuitasvezes,noiníciodaminha
carreira,eumeescondianoseventos,nãousavaoscracháscommeunome
eessascoisas. Levatempoparaassimilar. Masadmitirquevocêépopular
(http://bit.ly/1stoXjx)temmaisavercomasatitudesquevocêvaitomardali
parafrentedoqueseimportarcomoqueosoutrosvãofalar. Émuitoso-
brecomovocêvailidarcomasituaç ãodeserpopularecomovocêvaiusar
essavantagem(euseriaimbecildedizerqueissonãoéumavantagem)para
melhorarsuacarreirae,claro,ajudaroutrosdevs.
Esabedeumacoisa?Temquetercoragemparabaternopeitoeadmitir
paravocêeparaosoutrosquevocêéumaestrelinhanaárea.Nãoéquestão
deserhumilde.Équestãodeentenderqualoseupapelnavidadosoutros,
nasuacarreiraeprincipalmentenasuaprópriavida.
Canseiderecebere-mailsdedevsiniciantesdizendoquequeriamser
igualamim.Percebilogoqueissonãoerasaudávelparaocaradooutrolado
emuitomenosparamim.Sim,vocêprecisaseguirospassosdealguém.Isso
éalgointeligentedesefazer.Éassimqueahumanidadeevolui.Masentenda:
seguirospassosdealguémnãoquerdizerquevocêtenhaqueseraoutrapes-
soa.OZenofoielemesmodurantetodoocaminho.Eufuieumesmodurante
todoomeucaminhoevocêprecisaservocêmesmo,seguindooseucaminho.
Senão,vocêvaifalhar.
Quandoeutinhaminhaempresa,contrateiumconsultordenegócios
paranosguiar.Noinícioelequisentenderqualopapeldaempresaedossó-
ciosnomercado,comoatuávamosequalanossainfluêncianaárea.Quando
elesoubequeeueraumcarapopularnomeio,eledisseassim:“Oquevocê
vaifazerquandonãoformaisogarotodomomento?”.Euadmitoquenunca
150

## Página 157

CasadoCódigo Capítulo14. Textosextras
haviapensadonaquiloeissoficoumartelandodurantealgunsdiasnacabe ça.
Issomefezpensarbastantesobreváriascoisas,principalmenteemcomoeu
estavausandoousubutilizandoaminhaimagemnomercado.
Quandoeu(ele)meconvencidequeumdiaessediachegaria,fiqueimais
tranquiloeentendiqueesseéofluxonaturalesaudável.Apopularidadevem
evai.Sevocênãoestápreparadopraisso,seuegoexplodeeolevajunto.Um
diavãoparardefalaroseunomeparafalaronomedeoutrapessoa.Foioque
aconteceucomigo,váriasvezes.NãosóoZeno,masoutroscarasapareceram
evãocontinuaraparecendo.Éimportantequeissoaconte ça.Vocêéforçado
areavaliarosseuserroseprincipalmenteaavaliaroqueosoutrosfizerame
oquevocênãofezparachegarlá.Masosegredoéfazeressaavaliaç ão agora,
sendoounãopopular.
Sobre mudar o Mundo
Outracoisadifícildeentenderéquenemtodomundonasceupramudar
omundo(bit.ly/sobre-mudar-mundo).Talvezvocênãofiquepopular.Talvez
vocênãosejareconhecidopelaspessoasquevocêajudou.Talvezvocêfique
chateadoedescubraquewebnãoéasuapraia,emboravocêqueiramuitoque
seja.Seissoacontecer,esseprocessopodeserfeitoemoutromercado,emou-
traárea,comoutraspessoas.Vocêsóprecisadestestrêscomponentesbásicos
eestaráasalvo:vontade,tempoecuriosidade.Estesseriamoscomponentes
importantesparaqualquertarefaquepreciseserexecutada.
Quandoresolvifazerumartigocomotítulo Não seja o próximo Zeno
Rocha,ummontedegenteinterpretouerrado.Masvocêqueéinteligenteo
bastantevaiperceberqueoqueeuqueromostrarnesseartigoéquequalquer
umpodechegarlásemseroZeno,oMaujor,oEduardoShiota,oNandoVi-
eira,oDiegoEis,LeoBalter,LucasMazza,JeanCarloEmer,JaydsonGomes,
BernarddeLuna,DanielFilho,AlmirFilho,CaioGondimouqualquerou-
trodesenvolvedorconhecidonaárea,massendovocêmesmo.Comassuas
característicasehabilidades.
Seeutivessequeadiantarapenasumadica,elaseriaessa:ajudeeensine
outrosdevs.
Muitoprovavelmenteeunãodeveriaterpublicadoesteartigo.Masjáque
foi,esperoquenãoointerpreteerrado.Adificuldadedefalardesseassuntoé
151

## Página 158

14.2. SobreosPavõesdoFront-end CasadoCódigo
inversamenteproporcionalàfacilidadedostrollsdeseremimbecis.
14.2 S obre os Pavões do Front-end
Eugostavaquandoomercadodefront-enderamaissimples. Quandonão
haviatantoseventos. Quandonãohaviatantagentequerendoseraestrela
davez.Eugostavaquandoomercadoerapequeno,ondeamaioriadascon-
versasrolavaemlistasdediscussões. Quandoquasenãohaviablogssobre
oassuntoeosblogueirosquemaisfalavamtecnologiaetambémfront-end
eramprofissionaisdeoutrasáreas.Eugostavadessetempo.
Nãoqueroparecerumvelhochatoranzinzafalando.Maséqueháuma
linhamuitosutilentrequerersepromoverequererqueomercadocres çade
formasaudável. Hojeemdiatemtantagentequerendoserareferênciada
áreaqueseriatrágicosenãofossetãoengraçado.Todoselesdizemqueestão
mudandoomercado.Quevocêprecisaselevantarefazeralgumacoisa.Que
vocêprecisaserousadoetodoobláblábládequevocêjádeveterouvidofa-
larmilhõesdevezesporaí.Muitosdelesatéestãoseesfor çandoparaqueesse
discursosejareal.Emalguns,vocêatéconsegueverqueestãorealmentepre-
ocupadoscomorumodomercado.Emoutros,ficanacaraqueelesquerem
terseusminutos(ouanos)defama.
EureceboartigosdevoluntáriostodososdiaspeloTableless.Sãopessoas
queatéentãoestavamanônimas. Todaselasexpressamumdesejodecom-
partilharconhecimento.Muitosdelesnuncapalestraram,muitosdelesnunca
nemsequerescreveramumartigo.Maselesqueremajudardealgumaforma
acomunidadeacrescer.Elesqueremtervoztambém.Queremfalarparaos
outros,quecomoeles,sabemquenãoprecisamserumshowmanparaajudar,
bastatervontade.
Não sou contra quem faz self-promotion. Pelocontrário,vocêprecisade
umapitadadeself-promotionparaalavancarsuacarreira,seublog,seunome
etc.Seautopromoveréalgoquevocêprecisausar,masusarbem.Umacoisa
éseautopromoverparaseajudar,outraéseautopromoverparaajudarum
grupo,umpropósito. Tambémnãosoucontraalguémquererterseusmi-
nutosdefama.Issoénormaleàsvezeséopagamentoparaaqueletrabalho
gratuitoqueocaratemfeitoparaacomunidade.Oproblemaéquandoafama
152

## Página 159

CasadoCódigo Capítulo14. Textosextras
setornaarecompensafinal.
Éporissoquegostodostemposantigos.Omercadochegouatéaquipor
causadepessoasquededicavamseutempo,degraç a,paramanterfóruns,lis-
tasdediscussão,encontrossemanais,tutoriaisetc.porpuroamoràprofissão.
14.3 S obre o design oco
Quandoconstruímosumpadrãodeinterfaceparaqualquertipodeproduto
digital,énecessárioqueessepadrãoseperpetue,casocontrário,seutrabalho
nãovalerádenada. Essepadrãoprecisaserprotegidodurantetodoapro-
duçãodoprojeto,offlineouonline,nãoimporta.Paraqueessaperpetuidade
sejareal,vocêesuaequipeprecisarãodefenderessepadrãoe,paradefendê-lo,
vocêprecisadeargumentos.Éaíqueoproblemaaparece.
Nãoseisevocêjátentouconvenceralguémdequeodesigneotrabalho
de user experiencesãoimportantes. Eujátenteialgumasvezesenenhuma
foiagradável. Otrabalhodedesignedaexperiênciadousuáriosãocoisas
intangíveis. Eunãoconsigomostraroquantoamudan çadedesigndeum
siteaumentarãoasvendas,antesdeessedesignserpublicado.
Manterumdesignantigosóporquevendepodeseradecisãomaisra-
cional,masestálongedeseraideal. EraassimcomoGoogleatéelesde-
cidiremmudartodasuainterfaceeaexperiênciadeusodosseusprodutos.
UmconcorrentediretodoGoogleéaApple,umaempresaquerespirade-
sign. OGoogleeraumaempresaessencialmentedominadaporprograma-
dores.OGooglesoubeemalgummomentoqueafaltadedesign—ouode-
signruim—atrapalhariaseusplanosemlongoprazo.Sim,odesignéumfator
decisivoparadiversosusuários.Masécomumasempresasnãopriorizarem
decisõesdemudan çasnosite/produtobaseadasnasnecessidadesdedesign
ouUX.
Éengra çadopoistodomundogostadeveralgobonito. Vocêcompra
coisasfísicasjulgandoprincipalmentedoisaspectos: designefacilidadede
uso.Vocênãocompraalgoporqueéfeioedifícildeusar.Oucompra?
Comsoftwareissonãodeveriaserdiferente.Enaverdadenãoé.Ousuá-
riogeralmentepreferealgoatraente,quefuncionabemequenãoofaç aperder
tempousando.
153

## Página 160

14.3. Sobreodesignoco CasadoCódigo
Arranjando argumentos
Mascomonósarranjamosargumentosparadefenderumpadrãovisual?
Comoarranjamosargumentosparadefenderumnovodesignparaprodutos
ousitesquejáestãodandocerto?
Simples:nãofaçaaqueledesignqueébonitomasordinário.Manjaaquele
designbonito,masoco?Éessequevocênãopodefazer.
Você encontra esse tipo de design em toda parte. Dê um pulo
no Theme Forest ou até no Dribbble (https://dribbble.com/) . Já rola-
ram algumas discussões sobre a superficialidade (http://blog.intercom.io/
the-dribbblisation-of-design/)dosdesignsquerondamoDribbbleeoutros
serviçosparecidos.
Nenhum elemento vem do além
EuquerodarumexemploclarousandoaindaoMaterialDesigndoGo-
ogle. Sevocêaindanãoviuadocumentaçãodeles,vamosveragoraaparte
ondeelesexplicamsobrebotões,nestelink(http://www.google.com/design/
spec/components/buttons.html).
NoMaterialDesignexistemtrêstiposdebotões:o floating button, raised
buttoneo flat button.Noinício,parecequenãoénecessáriotertantostipos
debotões,massevocêpensardireito,hádiversoscenáriosdiferentesnoam-
bientemobileetambémnodesktop.Cadacenáriotemumcontextodiferente
equeexigeumaaten çãomaioroumenorparaasações.
154

## Página 161

CasadoCódigo Capítulo14. Textosextras
Fig.14.1:ExemplosdeelementosqueoGoogleusanoMaterialDesign.
Elestambémtomaramcuidadoparaindicarafrequênciadeusodecada
tipodebotão,alémdoslugaresespecíficosondecadatipodebotãoéusado.
Entendaqueháciêncianissoaí!Seháumpadrão,háorganização.Seháor-
ganização,océrebrodousuárioentendemelhorasregrasdeuso,asrestrições
etc.
Aquantidadedeelementosdeummesmotipotambémnãoserápro-
blema,jáquehárestriçõesdeuso.Claro,vocênãovaiadotarumacole çãode
10botões.Nessecaso,inteligênciaebomsensoprecisamserumaqualidade
nasuaequipe.
155

## Página 162

14.3. Sobreodesignoco CasadoCódigo
Fig.14.2:Essarestriçãodeprioridadepermitequeousuáriosaibaquaistipos
debotõessãomaisimportantesqueoutros.
Quandoháummotivoparacadaelementonatela,vocêganhaargumen-
tos.Sevocêsimplesmentecolocaumelementonatelaporqueachouqueera
tendênciadomercado,vocêperde.Sevocêcolocaporqueachoubonitinho,
vocêperde.Esseéodesignoco,vazio,ordinário.
Vocêtambémganhaargumentosdescobrindoasfalhaseasvantagensdo
site/produtoatual.Tendoinformaçõessobreoprojetoatual,vocênãoprecisa
sairdaestacazero. Vocêsaberáexatamentecomoasvendasacontecemou
comoelassãoperdidas.Issopodeserlevadoparaapróximaversão,podeser
testadoeaprimorado.
Esseéopontoondeépreferívelrealinharseuvisualeoscomportamentos
deinteraçõesdoquefazerumredesigntotal(http://alistapart.com/article/
redesignrealign).Quandovocêrealinha,vocêevoluiodesign.Vocêfiltraas
coisasruins.Quandoháumredesenhototaldosite,ummundodeincertezas
vemàtonanovamentee,claro,seusargumentosterãoqueserbemfortes
paradefenderumredesigncompleto.Quandovocêrealinha,vocêrefazuma
pequenapartedowebsite/produto.Sevocêfazumrealinhamentodevários
componentesduranteoano,aofinalvocêteráumprodutonovo,testadode
formamodularesabendoquecadacomponentetemumsentidoparaestar
156

## Página 163

CasadoCódigo Capítulo14. Textosextras
ali.
Obviamentevocêsópodefazerumrealinhamentosetiverumaboabase
estrutural.Hácoisasquesóseresolvemrefazendotudo.Outrasnão.Ore-
designnessecasopodeserbenéficoporagircomoumreboot,possibilitando
querealinhamentossejampossamserfeitosnaspróximasvezes.
Enfim
Naverdade,esseéumpensamentoaindapoucoexploradoemummonte
deempresas. NaLocawebestivemosduranteumbomtemponoprocesso
dereboot.Infelizmente,éumprocessodoloroso.Masháacertezadequeos
próximospassosserãomaisfáceis.Osargumentosserãomaisforteseteremos
númerosimportantesfalandoaonossofavor. Aquiéumpoucomaisfácil
porquetemosumframeworkquenosajudanoprocessodepadronizaç ãode
(quase)todasasinterfacesdaempresa.Masesseéoutropapo.
157

## Página 165

Capítulo15
Atémaiseobrigadopelospeixes
Eusempregosteideestarpertodosnovatosdaárea.Eufuinovatoumdiaesei
adificuldadequeéarranjarinformaçõesduranteoprocessodeaprendizagem.
Ointuitodestelivrofoisimplesmenteapresentarparavocêastecnologiase
metodologiasquesãoouestãopopularesnomercadonomomento.Espero
quevocêtenhagostadobastanteequeasinformaçõessirvamdereferência
durantemuitotempo.
Omercadodefront-endbrasileirotemcrescidobastante. Issoébom.
Issoémaravilhoso.Issoépicadasgaláxias.Mastambéméalgoruim.Como
émuitofácilaprenderHTMLeCSS,serdevfront-endacabasendoumaporta
bastanteacessívelparamuitaspessoas.Nemsempreessaspessoassetornam
profissionaisengajados. Elesqueremsimplesmenteganharumagrana,so-
breviverepronto.Paraeles,essaprofissãoécomoqualqueroutra.Nãoestou
dizendoqueelesestãoerrados.Issoaconteceemqualquerprofissão,emqual-
querpaís.Paraesses,tantofazoquefalamosdurantetodolivro.Tantofazos

## Página 166

15.1. Devsquevocêdeveseguir CasadoCódigo
eventos,osmeetups,asreuniõesqueagaleradacomunidadefazduranteo
ano.Elesdevemserdeixadosdelado...Estelivrofoicriadoparaoutroperfil
deprofissional.
Ficareimuitogratosevocêcompartilharcomigoseupontodevistaso-
breestelivro.Tenteifazeralgobomaquietenhocertezaquefalheiemvárias
partes. Talvezemalgunsmomentoseupoderiatermeaprofundadomais,
emoutraseupoderiaterfaladodemenos.Porisso,faleparamimasuaopi-
nião,ospontosqueeupoderiatermelhoradoouseháalgoqueeuesquecide
incluir.Falecomigopeloe-maillivro@tableless.com.br.
15.1 D evs que você deve seguir
Essacoisadecriarlistasdos melhoresfront-endsnãoélegalegeralmentenão
ébemrecebidaporváriaspessoas.Poressemotivoeufiqueicomumpéatrás,
mascrieiumalistadeprofissionaisquesãoreferênciasparamim.
Entendaquevocêprecisaterreferênciaseopiniõesdeváriaspessoasdo
mercado. Hojeeuficofelizporterváriosnomesnacabe çaparaindicar.
Quandocomeceinessaárea,nãohaviamuitosdesenvolvedorescomdispo-
siçãoparaajudarouquepublicavamartigostécnicos.Tivequeaprenderna
marra,encontrandoconteúdoquasequeexclusivamentegringos.Hojeomer-
cadonacionalémuito,masmuitopróspero.Porisso,aquivãoalgunsnomes
paravocêseguir:
Almir FilhotrabalhanaGlobo.comdesdesempre.Éumcaradescolado,
alegreebastanteabertoparaconversasdequalquertipo.Vocêjádeveterou-
vidofalarsobreeleporcausadoblogLoopInfinito,queelemantémjuntocom
oCaioGondim(http://loopinfinito.com.br/)etambémagoraelefazpartedo
Zofe,umpodcastexclusivamenteparaassuntossobredesenvolvimentofront-
end.
• Twitter:@almirfilho
• Blog:http://loopinfinito.com.br/
• Palestras:https://speakerdeck.com/almirfilho
160

## Página 167

CasadoCódigo Capítulo15. Atémaiseobrigadopelospeixes
Davi Ferreiraéumdesenvolvedorbemtímidonacomunidade,masum
dosmaiscompetentesqueconhe ço. PublicaalgunsartigosnoTablelesse
principalmentenoMedium.SuasdicasnoTwittereseusartigostécnicossão
minhasreferências.
• Twitter:@davitferreira
• Blog/Site:http://www.daviferreira.com/posts
• Palestras:http://www.daviferreira.com/page/decks
• PerfilnoTableless:http://tableless.com.br/author/davitferreira/
Eduardo Shiotaéojapamaislegaldacomunidade.Superatenciosoesem-
predispostoemajudarqualquerumsobreJS,CSS,HTMLetc.Amagatose
nãovaihesitaremdarumaopiniãosincerasobrequalquerassunto,princi-
palmentesobrequaisdecisõestomaremsuacarreira.
• Twitter:@shiota
• Blog:http://eshiota.com/
• Palestras:https://speakerdeck.com/eshiota
Jean Carlo Emersurgiudonada. Seujeitotranquiloecautelosoqueele
expressasuasopiniõeséumamarcaregistrada.Mesmoassimsuasopiniões
sãosemprefortesediretas.Alémdefazerumapancadadepalestrasdeótima
qualidadepeloBrasil,eleajudaamovimentaracomunidadedefront-endem
PortoAlegre.
• Twitter:@jcemer
• Blog/Sitepessoal:http://jcemer.com/
• Palestras:http://jcemer.com/talks.html
• PerfilnoTableless:http://tableless.com.br/author/jeancarloemer/
161

## Página 168

15.1. Devsquevocêdeveseguir CasadoCódigo
Leo Balteréacaradahumildade.Elenãohesitouemmencionardetalhes
pessoaisemsuatrajetóriaparaaBocoup,queficaemBoston,afimdematar
acuriosidadedeoutrosdevssobrecomoéoprocessodeirtrabalharfora
doBrasil. Éamigodetodosesupersolícitocomqualquerumqueprecise
deajudasobreJS.Paravocêterideia,eleécommiterdotimedoQUnitdo
jQuery.ElerespiraJavaScript.
• Twitter:@leobalter
• Blog:http://leobalter.github.io/
• Palestras:http://pt.slideshare.net/leobalter
Nando Vieiraéback-end,masocaratemapegadanofront-end.Como
umbomfullstack,eleconhecebemosdoisladosdamoeda.Eletemopiniões
bemácidassobretudoqueenvolvedesenvolvimentoweb.Atéporissoeleé
odiadoporunseamadoporoutros. Talvezsejainvejadaoposiç ão. Eusou
dotimequeamaocara.<3
• Twitter:@fnando
• Blog:http://simplesideias.com.br/
• Palestras:https://speakerdeck.com/fnando
Rafael Rinaldi,paramim,éumsinaldeesperan ça!Omercadoprecisade
novascaraspalestrando,escrevendo,gravandovídeosecomideiaseopiniões
diferentesdosdevsmaisantigos.ORinaldiéosinaldequeissoestáaconte-
cendo.Eleapareceudonadaetemfeitoalgumaspalestrasbeminteressantes
peloseventosBrasilafora.
• Twitter:@rafaelrinaldi
• Palestras:https://speakerdeck.com/rafaelrinaldi
• Site:http://rinaldi.io/
162

## Página 169

CasadoCódigo Capítulo15. Atémaiseobrigadopelospeixes
Sérgio Lopestomamuitoredbull,certeza!Ninguémficatristeassistindo
suaspalestras.Emseusartigoselesempreabordaassuntosnovos,queestarão
nabocadopovomuitotempodepois. Éocaraqueajudouapopularizaro
ResponsiveWebDesignaquinoBrasil.Gentemuitofina,agoramaisdoque
nunca!;-)
• Twitter:@sergio_caelum
• Blog/Site:http://sergiolopes.org/
• Palestras:http://sergiolopes.org/palestras/
Existeumasériedeoutrosdevsqueeudeixeiforadalista,masseeufosse
listartodosdariaoutrolivro(uia,boaideia). Massócitandoalguns:Clau-
berStipkovic,ReinaldoFerraz,RaphaelFabeni,BernarddeLuna,Giovanni
Keppelen,DanielFilho,CaioGondim,ClécioBachini,ZenoRocha,Jaydson
Gomes,PauloRagonha,GabrielZigolis,MauricioSoareseváriosoutros!
E os gringos?
Nãovoufazerumadescriç ãobonitadetodososgringos,porissovou
colocarapenasoTwitterdelesaqui.
• @timberners_lee(nemprecisofalar,né?)
• @zeldman(paramim,essecaraéoDeusdaweb)
• @meyerweb(ajudouapopularizaroCSS)
• @chriscoyier(criadordoCSSTricks)
• @glazou(essecarafazpartedoCSSWorkingGroupdoW3C)
• @davidwalshblog(devseniornaMozilla)
• @addyosmani(devnoGoogle)
• @mdo(cocriadordoBootstrap)
• @fat(cocriadordoBootstrap)
163

## Página 170

15.2. 50palavras CasadoCódigo
• @beep(donodotermoResponsiveWebDesign)
• @lukew(sobremobileweb)
• @bradfrost(sobremobileweb)
• @daveshea(Mezzoblue)
• @maxvoltar(designernoDropbox)
• @jasonsantamaria(designertopdelinha)
• @simplebits(cofundadordoDribbble)
• @paul_irish(jsman)
15.2 50 palavras
ComaajudadagaleradoTwitter(Valeu,pessoal!),conseguijuntar50pala-
vras(umpoucomais,naverdade)quevocêpodeouvirmuitoporaí.Sãopa-
lavrasrelacionadasatecnologias,metodologias,editores,linguagensdepro-
gramação,frameworkseoutrascoisasqueenvolvemomundododesenvol-
vimentowebdealgumaforma.Voucomentaralgumasdelas,masvocêpode
veralistacompletaaofinal.
Web Components
Mesmoquetenhadadoumacaídanofinalde2014,WebComponents
temsidoumassuntomuitorecorrenteempalestraseemváriosblogstécni-
cos.Muitosdefendemaideia,outrosaindaachamqueprecisasermelhorado,
mastodomundoentendequeéumpassoparaumcaminhoemdire çãoao
desenvolvimentocomponentizado,deverdade.Euaindanãofiznenhumpro-
jetoutilizandoWebComponentsenãovouusarenquantoeunãoprecisare
enquantonãotiveralgumtipodesuportenativonosbrowsers.
164

## Página 171

CasadoCódigo Capítulo15. Atémaiseobrigadopelospeixes
ES6
EssanovaversãodoJavaScripttemsidobastantecomentadaporqueela
trazumasériedemudan çasrelevantesparaalinguagem.OJavaScriptéuma
linguagemquesepopularizoumuitoduranteosúltimos5ou6anos.Várias
novastecnologiastêmsidobaseadasnoJavaScript,porexemplo,umagrande
partedoferramentárioquetemoshoje,semfalarnoNodeJS.Aversão6do
EcmaScriptvempararesolveralgunsgapsquealinguagemtinhaetambém
trouxeumasériedeoutrascoisasinteressantes,herdadasdeframeworkspo-
pularescomoCoffeeScript,alémdeajudarosframeworksebibliotecasexis-
tentesasetornaremmaisinteligenteseperformáticas.
SP A, Data binding, Angular, React e companhia
MaisdoqueES6,WebComponentsouqualqueroutracoisa,euouvifalar
maisfoisobreSPA,Angular,Reactecompanhia.Todaessatecnologiacriada
emvoltadosSPAsfoimuitoboaparacomunidadeenosensinouumbocado
sobreperformanceeotimização. Eunãoviaumbalan çotãograndesobre
oassuntodesdeautilizaç ãodeAjaxpelopessoaldoGmail. Aparteruim
sãoosmanésquerendofazerqualquersitezinhosimplesdeconteúdousando
algocomoAngularemvezdeusariniciativascomooSennaJS,criadopelo
EduardoLundgreenjuntocomoutrosdevs. OSennaJSéumengineparaa
criaçãodeSPAsdeformainteligente,quepodeserusadoemprojetosdetodos
ostamanhos.
As 50 palavras
Seguealista. Aproveite. EssalistafoimontadapelagaleranesteGist
(bit.ly/frontendwords2014).
1) WebComponents
2) Tooling
3) ES6
4) LeanUX
165

## Página 172

15.2. 50palavras CasadoCódigo
5) DataBinding
6) MobileFirst
7) Performance
8) MaterialDesign
9) SASS
10) SublimeText
11) Polymer
12) Grunt
13) GulpJS
14) ArquiteturaCSS
15) NodeJS
16) AtomicDesign
17) Bower
18) Yeoman
19) SVG
20) ResponsiveWebDesign
21) Flexbox
22) CSSGrid
23) Firebase
24) ContinousIntegration
25) Wearables
26) DesignThinking
166

## Página 173

CasadoCódigo Capítulo15. Atémaiseobrigadopelospeixes
27) TestesA/B
28) io.js
29) IE11
30) Jekyll
31) Middleman
32) FirefoxOS
33) Brakets
34) WebAPIS
35) Docker
36) React
37) ShadowDom
38) Build-first
39) Vagrant
40) Acessibilidade
41) ReactiveJavaScript
42) FunctionalJavaScript
43) Ansible
44) VIM
45) Shell
46) MV*
47) Inspector/DeveloperTools
48) WebKit
167

## Página 174

15.2. 50palavras CasadoCódigo
49) W3CDRM
50) WebRTC
51) Mobiledebugging
52) FaultTolerant
168