---json
{
  "id": "devops_na_pr_tica_-_entrega_de_software_confi_vel_e_automatizada",
  "title": "DevOps Na prática - entrega de software confiável e automatizada",
  "categoria": "06-devops-infra",
  "subcategoria": "linux",
  "resumo": "**Arquivo Original:** `DevOps Na prática - entrega de software confiável e automatizada.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "automatizada",
    "confi",
    "devops",
    "entrega",
    "infra",
    "linux",
    "software",
    "tica"
  ],
  "perguntas_tipo": [
    "Como utilizar DevOps Na prática - entrega de software confiável e automatizada?",
    "Quais as boas praticas de linux?"
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
  "dono": "stack-linux",
  "prioridade": 2
}
---

# DevOps Na prática - entrega de software confiável e automatizada

> **Arquivo Original:** `DevOps Na prática - entrega de software confiável e automatizada.pdf`
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

## Página 5

CasadoCódigo
"Parameupai,quemeintroduziuaomundodacomputa çãoeémeuexemplo
devida.”
i

## Página 7

CasadoCódigo
Prefácio
JezHumble
Poucodepoisquemeformeinauniversidadeem1999,eufuicontratadopor
umastart-upemLondres. Meuchefe,JonnyLeRoy,ensinou-meaprática
deimplantaçãocontínua:quandoterminávamosumanovafuncionalidade,
fazíamosalgunstestesmanuaisrápidosnanossaestaç ãodetrabalhoe,em
seguida,copiávamosos scriptsASPrelevantesporFTPparaoservidorde
produção–umapráticaqueeunãorecomendariahoje,masqueteveavan-
tagemdenospermitirmostrarnovasideiasparanossosusuáriosmuitorapi-
damente.
Em2004,quandoentreina ThoughtWorks,meutrabalhoeraajudarem-
presasaentregarsoftwareeeufiqueichocadoaodescobrirqueprazosdeme-
sesoumesmoanoseramcomuns.Felizmente,tiveasortedetrabalharcom
váriaspessoasinteligentesemnossaindústriaqueestavamexplorandofor-
masdemelhorarestesresultados,aomesmotempoaumentandoaqualidade
emelhorandoanossacapacidadedeservirnossosusuários.Aspráticasque
desenvolvemostambémtornaramavidamelhorparaaspessoascomquem
estávamostrabalhando(porexemplo,nãoprecisávamosmaisfazer deploys
foradohoráriocomercial)–umaindicaçãoimportantedequevocêestáfa-
zendoalgocerto. Em2010,DaveFarleyeeupublicamos EntregaContínua,
ondedescrevemososprincípiosepráticasquetornampossívelentregarpe-
quenasalteraçõesincrementais,deformarápida,barataecombaixorisco.
Noentanto, onossolivroomiteosdetalhespráticosdoquevocêre-
almenteprecisaparacome çaracriarumapipelinedeentrega, comopôr
empráticasistemasdemonitoramentoeinfraestruturacomocódigo,além
dosoutrospassospráticosimportantesnecessáriosparaimplementarentrega
contínua.PorissoestoumuitocontentequeoDaniloescreveuolivroqueestá
iii

## Página 8

CasadoCódigo
emsuasmãos,queeuachoserumacontribui çãoimportanteevaliosaparaa
nossaárea.ODaniloestáprofundamenteenvolvidoemajudarorganizações
aimplementaraspráticasdeentregacontínuaháváriosanosetemampla
experiência,eeutenhocertezadequevocêvaiacharoseulivropráticoe
informativo.Desejo-lhetudodemelhornasuajornada.
iv

## Página 9

CasadoCódigo
Sobreolivro
Entregarsoftwareemproduçãoéumprocessoquetemsetornadocadavez
maisdifícilnodepartamentodeTIdediversasempresas. Cicloslongosde
testeedivisõesentreasequipesdedesenvolvimentoedeopera çõessãoalguns
dosfatoresquecontribuemparaesteproblema. Mesmoequipeságeisque
produzemsoftwareentregávelaofinaldecadaiteraç ãosofremparachegar
emproduçãoquandoencontramestasbarreiras.
DevOpséummovimentoculturaleprofissionalqueestátentandoque-
braressasbarreiras. Comofocoemautoma ção,colaboração,compartilha-
mentodeferramentasedeconhecimento,DevOpsestámostrandoquede-
senvolvedoreseengenheirosdesistematêmmuitooqueaprenderunscom
osoutros.
Nestelivro,mostramoscomoimplementarpráticasdeDevOpseEntrega
Contínuaparaaumentarafrequênciadedeploysnasuaempresa,aomesmo
tempoaumentandoaestabilidadeerobustezdosistemaemproduç ão.Você
vaiaprendercomoautomatizarobuildedeploydeumaaplicaç ãoweb,como
automatizarogerenciamentodainfraestrutura,comomonitorarosistema
emprodução,comoevoluiraarquiteturaemigrá-laparaanuvem,alémde
conhecerdiversasferramentasquevocêpodeaplicarnoseutrabalho.
v

## Página 11

CasadoCódigo
Agradecimentos
Aomeupai, Marcos, porsersempreumexemploaseguireporiralém
tentandoacompanharosexemplosdecódigomesmosemnenhumconhe-
cimentonoassunto. Àminhamãe,Solange,eminhairmã,Carolina,pelo
incentivoeporcorrigiremdiversoserrosdedigitaç ãoeportuguêsnasver-
sõespreliminaresdolivro.
Àminhaparceiraemelhoramiga,Jenny,pelocarinhoeapoioduranteas
diversashorasquepasseitrabalhandonolivro.
Aomeueditor,PauloSilveira,pelaoportunidade,pelaconfian çaepor
sabercomodarumpuxãodeorelhaouumincentivonahoracertaparaque
olivrosetornasseumarealidade.Àminharevisoraeamiga,VivianMatsui,
porcorrigirtodososmeuserrosdeportuguês.
Aosmeusrevisorestécnicos:HugoCorbucci,DanielCordeiroeCarlos
Vilella.Obrigadopormeajudaremaencontrarformasmelhoresdeexplicar
conceitosdifíceis,pelaopiniãosobreostermosdifíceisdetraduzir,porques-
tionaremminhasdecisõestécnicasepormeajudaremamelhoraroconteúdo
dolivro.
AoscolegasPrasannaPendse,EmilyRosengren,EldonAlmeidaeoutros
membrosdogrupo“Blogger’sBloc”naThoughtWorks,pormeincentivarem
aescrevermaisepelo feedbacknoscapítulosiniciais,mesmonãoentendendo
alínguaportuguesa.
Aosmeusinúmerosoutroscolegasdetrabalhoda ThoughtWorks,emes-
pecialRolfRussell,BrandonByarseJezHumble,queouviramminhasideias
sobreolivroemeajudaramaescolheramelhorformadeabordarcadaas-
sunto,capítuloporcapítulo.
vii

## Página 12

CasadoCódigo
Porfim,atodosquecontribuíramdeformadiretaouindiretanaescrita
destelivro.
Muitoobrigado!
viii

## Página 13

CasadoCódigo
Sobreoautor
DaniloSatocome çouaprogramaraindacrian ça, quandomuitaspessoas
aindanãotinhamcomputadoremcasa.Em2000entrounocursodebacha-
reladoemCiênciadaComputaçãodaUniversidadedeSãoPaulo,come çando
suacarreiracomoadministradordaRedeLinuxdoIME-USPdurante2anos.
AindanagraduaçãocomeçouaestagiarcomodesenvolvedorJava/J2EEeteve
seuprimeirocontatocomMétodosÁgeisnadisciplinadeProgramaç ãoEx-
trema(XP).
IniciouomestradonaUSPlogoapósagraduaç ãoe,orientadopeloPro-
fessorAlfredoGoldman,defendeuemAgostode2007adissertaç ão“UsoEfi-
cazdeMétricasemMétodosÁgeisdeDesenvolvimentodeSoftware”[16].
Durantesuacarreira,Daniloatuoucomoconsultor,desenvolvedor,admi-
nistradordesistemas,analista,engenheirodesistemas,professor,arquitetoe
coach,tornando-seconsultorlíderda ThoughtWorksem2008,ondetraba-
lhouemprojetosRuby,PythoneJavanoBrasil,EUAenoReinoUnido.Atu-
almentetemajudadoclientesaadotarpráticasdeDevOpseEntregaContínua
parareduzirotempoentreaconcep çãodeumaideiaesuaimplementaç ão
comcódigorodandoemprodução.
Alémdacarreiraprofissional,Danilotambémtemexperiênciacomopa-
lestranteemconferênciasnacionaiseinternacionais,apresentandopalestras
eworkshopsna: XP2007/2009/2010,Agile2008/2009,Ágiles2008,Cone-
xãoJava2007, FalandoemAgile2008, RioOnRails2007, PyConBrasil
2007,RejectConfSP2007,RailsSummitLatinAmerica2008,AgileBrazil
2011/2012/2013,QConSP2011/2013,RubyConfBrasil2012/2013,alémdeser
ofundadordoCodingDojo@SãoPauloeorganizadordaAgileBrazil2010,
2011e2012.
ix

## Página 15

CasadoCódigo Sumário
Sumário
1 Introdução 1
1.1 Abordagemtradicional . . . . . . . . . . . . . . . . . . . . . . 2
1.2 Umaabordagemalternativa:DevOpseentregacontínua . . 4
1.3 Sobreolivro . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2 Tudocome çaemprodu ção 11
2.1 Nossaaplicaçãodeexemplo:alojavirtual . . . . . . . . . . . 12
2.2 Instalandooambientedeprodução . . . . . . . . . . . . . . . 15
2.3 Configurandodependênciasnosservidoresdeprodução . . 20
2.4 Buildedeploydaaplicação . . . . . . . . . . . . . . . . . . . . 28
3 Monitoramento 35
3.1 Instalandooservidordemonitoramento . . . . . . . . . . . . 36
3.2 Monitorandooutrosservidores . . . . . . . . . . . . . . . . . 42
3.3 ExplorandooscomandosdeverificaçãodoNagios . . . . . . 44
3.4 Adicionandoverificaçõesmaisespecíficas . . . . . . . . . . . 48
3.5 Recebendoalertas . . . . . . . . . . . . . . . . . . . . . . . . . 55
3.6 Umproblemaatingeprodução,eagora? . . . . . . . . . . . . 59
4 Infraestruturacomocódigo 61
4.1 Provisionamento,configuraçãooudeploy? . . . . . . . . . . . 62
4.2 Ferramentasdegerenciamentodeconfiguração . . . . . . . . 65
4.3 IntroduçãoaoPuppet:recursos,provedores,manifestosede-
pendências. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
xi

## Página 16

Sumário CasadoCódigo
4.4 Reinstalandooservidordebancodedados . . . . . . . . . . 74
4.5 Reinstalandooservidorweb . . . . . . . . . . . . . . . . . . . 82
4.6 Fazendodeploydaaplicação . . . . . . . . . . . . . . . . . . . 87
5 Puppetalémdobásico 97
5.1 Classesetiposdefinidos . . . . . . . . . . . . . . . . . . . . . 97
5.2 Empacotamentoedistribuiçãousandomódulos . . . . . . . 101
5.3 RefatorandoocódigoPuppetdoservidorweb . . . . . . . . . 105
5.4 Separaçãoderesponsabilidades:infraestruturavs.aplica ção 115
5.5 Puppetforge:reutilizandomódulosdacomunidade . . . . . 119
5.6 Conclusão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
6 Integraçãocontínua 127
6.1 Práticasdeengenhariaágil . . . . . . . . . . . . . . . . . . . . 128
6.2 Começandopelobásico:controledeversões . . . . . . . . . . 128
6.3 Automatizandoobuilddoprojeto . . . . . . . . . . . . . . . . 131
6.4 Testesautomatizados:diminuindoriscoeaumentandoacon-
fiança . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
6.5 Oqueéintegraçãocontínua? . . . . . . . . . . . . . . . . . . . 139
6.6 Provisionandoumservidordeintegraçãocontínua . . . . . . 142
6.7 Configurandoobuilddalojavirtual . . . . . . . . . . . . . . 147
6.8 Infraestruturacomocódigoparaoservidordeintegraç ão
contínua. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158
7 Pipelinedeentrega 165
7.1 Afinidadecomainfraestrutura:usandopacotesnativos . . . 166
7.2 Integraçãocontínuadocódigodeinfraestrutura . . . . . . . 184
7.3 Pipelinedeentrega . . . . . . . . . . . . . . . . . . . . . . . . . 198
7.4 PróximosPassos . . . . . . . . . . . . . . . . . . . . . . . . . . 205
8 Tópicosavançados 207
8.1 Fazendodeploynanuvem . . . . . . . . . . . . . . . . . . . . 209
8.2 DevOpsalémdasferramentas . . . . . . . . . . . . . . . . . . 230
xii

## Página 17

CasadoCódigo Sumário
8.3 Sistemasavan çadosdemonitoramento . . . . . . . . . . . . . 231
8.4 Pipelinesdeentregacomplexas . . . . . . . . . . . . . . . . . 234
8.5 Gerenciandomudan çasnobancodedados . . . . . . . . . . 234
8.6 Orquestraçãodedeploy . . . . . . . . . . . . . . . . . . . . . . 235
8.7 Gerenciandoconfiguraçõesporambiente . . . . . . . . . . . 236
8.8 Evoluçãoarquitetural . . . . . . . . . . . . . . . . . . . . . . . 238
8.9 Segurança. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241
8.10 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 242
Bibliografia 246
Versão:17.2.28
xiii

## Página 19

Capítulo1
Introdução
Comoavan çodatecnologia,softwaretemsetornadopartefundamentaldo
diaadiademuitasempresas.Aoplanejarsuasfériasemfamília–agendando
quartoemhotéis,comprandopassagensdeavião,realizandotransaçõesfi-
nanceiras,enviandoSMSoucompartilhandoasfotosdaviagem–vocêin-
teragecomdiversossistemasdesoftware. Quandoumdessessistemasestá
foradoar,oproblemanãoéapenasdaempresaqueestáperdendonegócios,
mastambémdosusuáriosquenãoconseguemrealizarsuastarefas.Poresse
motivoéimportanteinvestirnaqualidadeeestabilidadedosoftwaredesdeo
momentoemqueaprimeiralinhadecódigoéescritaatéomomentoemque
eleestárodandoemprodução.

## Página 20

1.1. Abordagemtradicional CasadoCódigo
1.1 Abordagem tradicional
Metodologiasdedesenvolvimentodesoftwareevoluíram,porémoprocesso
detransformarideiasemcódigoaindaenvolvediversasatividadescomo:le-
vantamentoderequisitos, design,arquitetura,implementaçãoeteste.OsMé-
todosÁgeisdedesenvolvimentodesoftwaresurgiramnofinaldadécadade
90propondoumanovaabordagemparaorganizartaisatividades.Aoinvés
derealizá-lasemfasesdistintas–modeloconhecidocomoprocessoemcas-
cata–elasacontecememparalelootempotodo,emiteraçõescurtas.Aofinal
decadaiteração,osoftwaresetornamaisemaisútil,comnovasfuncionali-
dadesemenos bugs,eotimedecidejuntocomoclientequalapróximafatia
aserdesenvolvida.
Assimqueoclientedecidequeosoftwareestáprontoparairaoareo
códigoécolocadoemprodução,osverdadeirosusuárioscome çamausaro
sistema.Nessemomento,diversasoutraspreocupaçõessetornamrelevantes:
suporte,monitoramento,seguran ça,disponibilidade,desempenho,usabili-
dade,dentreoutras. Quandoosoftwareestáemproduç ão,aprioridadeé
mantê-lorodandodeformaestável. Emcasosdefalhaoudesastres,otime
precisaestarpreparadoparareagirdeformaproativaeresolveroproblema
rapidamente.
Devidoànaturezadessasatividades,muitosdepartamentosdeTIpos-
suemumadivisãoclaraderesponsabilidadesentreo timededesenvolvi-
mentoeo timedeoperaç ões. Enquantootimededesenvolvimentoéres-
ponsávelporcriarnovosprodutoseaplicações,adicionarfuncionalidadesou
corrigirbugs,otimedeoperaçõeséresponsávelporcuidardessesprodutos
eaplicaçõesemprodução.Otimededesenvolvimentoéincentivadoaintro-
duzirmudanças,enquantootimedeoperaçõesprezapelaestabilidade.
Àprimeiravista,estadivisãoderesponsabilidadesparecefazersentido.
Cadaequipepossuiobjetivoseformasdetrabalhodiferentes. Enquantoo
timededesenvolvimentotrabalhaemiterações,otimedeoperaçõesprecisa
reagirinstantaneamentequandoalgodáerrado.Alémdisso,asferramentas
eoconhecimentonecessárioparatrabalharnessasequipessãodiferentes.O
timededesenvolvimentoevoluiosistemaintroduzindomudan ças.Poroutro
lado,otimedeoperaçõesevitamudan ças,poiselastrazemumcertoriscoà
estabilidadedosistema. Cria-seentãoumconflitodeinteresseentreessas
2

## Página 21

CasadoCódigo Capítulo1. Introdução
duasequipes.
Umavezqueoconflitoexiste,aformamaiscomumdegerenciaressa
relaçãoéatravésdacriaçãodeprocessosquedefinemomododetrabalho
easresponsabilidadesdecadaequipe. Detemposemtempos,aequipede
desenvolvimentoempacotaosoftwarequeprecisairparaproduç ão,escreve
documentaçãoexplicandocomoconfigurarosistema,comorealizarainsta-
laçãoemproduçãoerepassaaresponsabilidadeparaotimedeoperações.É
comumousodesistemasdecontrolede ticketsparagerenciaracomunica-
çãoentreasequipesassimcomoadefiniç ãodeacordosdeníveldeserviço
(service-levelagreements ouSLAs)paragarantirqueos ticketssejamproces-
sadoserespondidosemumtempoadequado.
Essapassagemdebastão–tambémconhecidaeminglêspelotermohand-
off–criaumgargalonoprocessodelevarcódigododesenvolvimentoeteste
paraprodução. Écomumchamaresseprocessode deployemambientede
produção.Emportuguêséatépossívelouvironeologismo deploiar,ouentão
otermocorretoemportuguês,queseria“implantar”.
Comopassardotempo,oprocessotendeasetornarmaisemaisburocrá-
tico,fazendocomqueafrequênciade deploysdiminua.Comisso,onúmero
demudan çasintroduzidasemcada deploytendeaacumular,aumentando
tambémoriscodecada deployecriandoocicloviciosomostradonafigura
1.1.
Figura1.1:Cicloviciosoentredesenvolvimentoeoperações
Essecicloviciosonãosódiminuiahabilidadedaempresaderesponder
rapidamenteamudan çasnonegócio,comotambémimpactaetapasanterio-
3

## Página 22

1.2. Umaabordagemalternativa:DevOpseentregacontínua CasadoCódigo
resdoprocessodedesenvolvimento.Aseparaçãoentreostimesdedesenvol-
vimentoedeoperações,o hand-offdecódigoexistenteentreeleseacerimô-
niaenvolvidanoprocessode deployacabamcriandooproblemaconhecido
como“aÚltimaMilha”[17].
Aúltimamilhaserefereàfasefinaldoprocessodedesenvolvimentoque
aconteceapósosoftwareatendertodososrequisitosfuncionaismasantesde
serimplantadoemprodução.Elaenvolveváriasatividadesparaverificarseo
quevaiserentregueéestávelounão,como:testesdeintegra ção,testesdesis-
tema,testesdedesempenho,testesdeseguran ça,homologaçãocomusuários
(tambémconhecidocomo UserAcceptanceTests ouUAT),testesdeusabili-
dade,ensaiosde deploy,migraçãodedadosetc.
Éfácilignoraraúltimamilhaquandoaequipeestáproduzindoedemons-
trandofuncionalidadesnovasacadaumaouduassemanas.Porém,sãopou-
casasequipesquedefatofazem deployemproduçãoaofinaldecadaitera-
ção.Dopontodevistadonegócio,aempresasóteráretornonoinvestimento
quandoosoftwareestiverrealmenterodandoemproduç ão.Oproblemada
últimamilhasóévisívelquandosetomaumavisãoholísticadoprocesso.
Pararesolvê–loéprecisoolharalémdasbarreirasimpostasentreasdiferentes
equipesenvolvidas:sejaaequipedenegócios,aequipededesenvolvimento
ouaequipedeoperações.
1.2 Uma abordagem alternativ a: D evOps e en-
trega contínua
Muitasempresasdesucessonainternet–comoGoogle,Amazon,Netflix,
Flickr,GitHubeFacebook–perceberamqueatecnologiapodeserusadaaseu
favorequeoatrasono deployparaproduçãosignificaatrasarsuahabilidade
decompetireseadaptaramudan çasnomercado.Écomumqueelasrealizem
dezenasouatécentenasde deployspordia!
Essalinhadepensamentoquetentadiminuirotempoentreacriaç ão
deumaideiaesuaimplementaçãoemproduçãoétambémconhecidacomo
“EntregaContínua”[6]eestárevolucionandooprocessodedesenvolvi-
mentoeentregadesoftware. Algunsautorespreferemutilizarotermoem
inglês,continuousdelivery.
4

## Página 23

CasadoCódigo Capítulo1. Introdução
Quandooprocessode deploydeixadeserumacerimôniaepassaase
tornaralgocorriqueiro,ocicloviciosodafigura1.1seinvertecompletamente.
Oaumentodafrequênciade deploysfazcomqueaquantidadedemudan ças
emcada deploydiminua,reduzindotambémoriscoassociadocomaquele
deploy. Essebenefícionãoéalgointuitivo,porémquandoalgodáerradoé
muitomaisfácildescobriroqueaconteceu,poisaquantidadedefatoresque
podemtercausadooproblemaémenor.
Noentanto,adiminuiçãodorisconãoimplicanaremo çãocompletados
processoscriadosentreasequipesdedesenvolvimentoedeoperações. O
segredoquepermiteainversãodocicloéaautomatizaç ãodesseprocesso,
conformemostraafigura 1.2.Automatizaroprocessode deploypermiteque
elesejaexecutadoaqualquermomentodeformaconfiável,removendoorisco
deumerrohumanocausarproblemas.
Figura1.2: PráticasdeDevOpsajudamaquebrarocicloviciosoatravésda
automaçãodeprocessos
Investiremautomatizaçãonãoéumaideianova,muitasequipesjáes-
crevemtestesautomatizadoscomopartedoprocessodedesenvolvimentode
software.Práticascomoodesenvolvimentodirigidoatestes(Test-DrivenDe-
velopmentouTDD)[3]ouaintegraçãocontínua[12]–queserádiscutidaem
maisdetalhesnocapítulo 6–sãocomunseamplamenteaceitasnacomuni-
dadededesenvolvimento.Essefocoemautomaçãodetestes,juntamentecom
acriaçãodeequipesmultidisciplinares,ajudouaquebrarabarreiraexistente
entredesenvolvedores,testadoreseanalistasdenegócio,criandoumacultura
decolaboraçãoentrepessoascomhabilidadescomplementarestrabalhando
5

## Página 24

1.3. Sobreolivro CasadoCódigo
comopartedamesmaequipe.
Inspiradonosucessodosmétodoságeis,umnovomovimentosurgiupara
levaramesmalinhaderaciocínioparaopróximonível:omovimento De-
vOps. Seuobjetivoécriarumaculturadecolaboraç ãoentreasequipesde
desenvolvimentoedeoperaçõesquepermiteaumentarofluxodetrabalho
completado–maiorfrequênciadedeploys–aomesmotempoaumentandoa
estabilidadeerobustezdoambientedeproduç ão.
Alémdeumamudan çacultural,omovimentoDevOpsenfocabastante
naspráticasdeautomaçãodasdiversasatividadesnecessáriasparaatacaraúl-
timamilhaeentregarcódigodequalidadeemproduç ão,como:compilação
docódigo,testesautomatizados,empacotamento,criaçãodeambientespara
testeouprodução,configuraçãodainfraestrutura,migraçãodedados,mo-
nitoramento,agregamentode logsemétricas,auditoria,segurança,desempe-
nho,deploy,entreoutros.
EmpresasqueaplicaramessaspráticasdeDevOpscomsucessonãoenxer-
gammaisodepartamentodeTIcomoumgargalomassimcomoumagente
decapacitaçãodonegócio.Elasconseguemseadaptaramudan çasnomer-
cadorapidamenteerealizardiversos deployspordiadeformasegura.Algu-
masdelasinclusivefazemcomqueumnovodesenvolvedorrealizeum deploy
paraproduçãonoseuprimeirodiadetrabalho!
Estelivroiráapresentar,atravésdeexemplosreais,asprincipaispráti-
casdeDevOpseEntregaContínuaparapermitirquevocêrepliqueomesmo
sucessonasuaempresa.Oobjetivoprincipaldolivroéaproximarascomuni-
dadesdedesenvolvimentoedeoperações.Desenvolvedoresconhecerãoum
poucomaissobreaspreocupaçõesepráticasenvolvidasparaoperaremanter
sistemasestáveisemprodução,enquantoengenheiroseadministradoresde
sistemairãoaprendercomointroduzirmudan çasdeformaseguraeincre-
mentalatravésdeautomação.
1.3 Sobre o livro
Oprincipalobjetivodolivroémostrarnapráticacomoaplicarosconcei-
tosetécnicasdeDevOpseEntregaContínua.Poressemotivo,tivemosque
escolherquaistecnologiaseferramentasutilizar. Nossapreferênciafoiusar
6

## Página 25

CasadoCódigo Capítulo1. Introdução
linguagenseferramentasdecódigolivreepriorizamosaquelasquesãobas-
tanteusadasnaindústria.
Vocêvaiprecisarusarasferramentasescolhidasparaacompanharos
exemplosdecódigo. Porém, semprequeapresentarmosumanovaferra-
menta,vamosdiscutirumpoucosobreasoutrasalternativas,paraquevocê
possapesquisarqualop çãofazmaissentidonoseucontexto.
Vocênãoprecisadenenhumconhecimentoprévioespecíficoparaacom-
panharosexemplos.SevocêtiverexperiêncianoecossistemaJavaouRuby,
seráumbônus.NossoambientedeproduçãovairodaremUNIX(Linux,para
sermaisespecífico),portantoumpoucodeconhecimentonousodalinhade
comandopodeajudarmasnãoéobrigatório[13].Detodaforma,vocêvaiser
capazderodartodososexemplosnasuaprópriamáquina,independentese
estárodandoLinux,MacouWindows.
Públicoalvo
Estelivroévoltadoparadesenvolvedores,engenheirosdesistema,admi-
nistradoresdesistema,arquitetos,gerentesequalquerpessoacomconheci-
mentostécnicosquetenhainteresseemaprendermaissobreaspráticasde
DevOpseEntregaContínua.
Estruturadoscapítulos
Olivrofoiescritoparaserlidodoinícioaofimdeformasequencial.De-
pendendodasuaexperiênciacomoassuntoabordadoemcadacapítulo,você
podepreferiravan çarouseguiremumaordemdiferente.
Nocapítulo2 apresentamosaaplicaçãodeexemploqueseráusadano
restantedolivroeastecnologiasusadasparaconstruí-la.Comoofocodoli-
vronãoénodesenvolvimentodaaplicaçãoemsi,usamosumaaplicaçãonão
trivialescritaemJavaeusandodiversasbibliotecasbemcomunsnoecossis-
temaJava.Aofinaldocapítulo,aaplicaç ãovaiestarrodandoemproduç ão.
Comumambientedeproduçãonoar,no capítulo3vamosvestirocha-
péudotimedeoperaçõeseconfigurarumservidordemonitoramentopara
detectarfalhaseenviarnotificaçõessemprequealgumproblemaforencon-
trado. Aofinaldocapítulo,seremosnotificadosdequeumdosservidores
caiu.
7

## Página 26

1.3. Sobreolivro CasadoCódigo
Nocapítulo4 vamosreconstruiroservidorproblemático,dessavezde
formaautomatizada,tratandoainfraestruturacomocódigo. O capítulo5
éumacontinuaçãodoassunto,abordandotópicosmaisavan çadoserefato-
randoocódigoparatorná-lomaismodular,legíveleextensível.
Apósvestirochapéudotimedeoperações,iremosvoltarnossaaten ção
paraodesenvolvimentodesoftware.O capítulo6discutepráticasdeenge-
nhariaágilqueajudamaescrevercódigodequalidade.Vamosaprendersobre
osdiversostiposdetestesautomatizadosesubirumnovoservidordedicado
parafazerintegraçãocontínuadocódigodanossaaplicaç ão.
Apresentamosoconceitodapipelinedeentregano capítulo7.Coloca-
mosocódigodeinfraestruturanaintegraç ãocontínuaeimplementamosum
processoautomatizadoparainstalaraversãomaisnovadaaplicaç ãoempro-
duçãocomosimplescliquedeumbotão.
Nocapítulo8migramosoambientedeproduçãoparaanuvem.Porfim,
discutimostópicosmaisavan çados,componteirospararecursosondevocê
podepesquisareaprendermaissobreosassuntosqueficaramdeforadoes-
copodestelivro.
Convençõesdecódigo
Nosexemplosdecódigo,vamosusarreticências ...paraomitiraspar-
tesnãoimportantes. Quandoocódigojáexiste,vamosrepetiraslinhasao
redordaáreaqueprecisaseralteradaparadarumpoucodecontextosobrea
modificação.
Quandoalinhaémuitocompridaenãocoubernapágina,vamosusar
umabarrainvertida \paraindicarqueapróximalinhanolivroéacontinu-
açãodalinhaanterior. Vocêpodesimplesmenteignorarabarrainvertidae
continuardigitandonamesmalinha.
Nosexemplosnalinhadecomando,alémdabarrainvertida,usaremos
umsinaldemaior >napróximalinhaparaindicarqueelaaindaépartedo
mesmocomando.Istoéparadistinguirocomandoqueprecisaserdigitado
dasaídaqueocomandoproduzquandoforexecutado. Aoexecutarosco-
mandos,vocêpodesimplesmentedigitartudonamesmalinha,ignorandoa
\eo >.
8

## Página 27

CasadoCódigo Capítulo1. Introdução
Maisrecursos
CriamosumfórumdediscussãonoGoogleGroupsondevocêpodeen-
viarperguntas,sugestõesou feedbackdiretoparaoautor. Paraseinscrever,
acesseaURL:
https://groups.google.com/d/forum/livro-devops-na-pratica
Todos os exemplos de código do livro também estão disponíveis no
GitHubdoautor,nasURLs:
https://github.com/dtsato/loja-virtual-devops
https://github.com/dtsato/loja-virtual-devops-puppet
9

## Página 29

Capítulo2
Tudocomeçaemprodução
Aocontráriodoquemuitosprocessosdedesenvolvimentosugerem,ociclo
devidadosoftwaresódeveriacome çarquandousuárioscomeçamausá-lo.
Oproblemadaúltimamilhaapresentadonocapítulo1deveriaseraprimeira
milha,poisnenhumsoftwareentregavalorantesdeentraremproduç ão.Por
isso,oobjetivodestecapítuloésubirumambientedeproduç ãocompleto,
começandodozero,einstalarumaaplicaçãoJavarelativamentecomplexaque
seráusadacomopontodepartidaparaosconceitosepráticasdeDevOps
apresentadosnolivro.
Aofinaldestecapítulo,teremosumalojavirtualwebcompletarodando
–suportadaporumbancodedados–quepermitiráqueusuáriossecadas-
trem,efetuemcompras,alémdefornecerferramentasdeadministraç ãopara
gerenciamentodocatálogodeprodutos,daspromo çõesedoconteúdodis-
ponibilizadonalojavirtual.
Dequeadiantaadicionarnovasfuncionalidades,melhorarodesempe-

## Página 30

2.1. Nossaaplicaçãodeexemplo:alojavirtual CasadoCódigo
nho,corrigirdefeitos,deixarastelasdalojavirtualmaisbonitasseissotudo
nãoforparaprodução?Vamoscome çarfazendoexatamenteessapartedifícil,
essataldeúltimamilha:colocarosoftwareemproduç ão.
2.1 Nossa aplicação de exemplo: a loja virtual
Comoofocodolivronãoénoprocessodedesenvolvimentoemsi,massim
naspráticasdeDevOpsqueauxiliamo build,deployeoperaçãodeumaapli-
caçãoemprodução,usaremosumaaplicaçãofictíciabaseadaemumprojeto
decódigoaberto. Alojavirtualéumaaplicaç ãowebescritaemJavasobre
aplataformaBroadleafCommerce(http://www.broadleafcommerce.org/).O
códigoutilizadonestecapítuloenorestantedolivrofoiescritocombaseno
sitededemonstraçãooferecidopelaBroadleafepodeseracessadonoseguinte
repositóriodoGitHub:
https://github.com/dtsato/loja-virtual-devops/
OBroadleafCommerce éumaplataformaflexívelqueexpõepontosde
configuraçãoedeextensãoquepodemsercustomizadosparaimplementar
funcionalidadesespecíficas. Noentanto,boapartedasfuncionalidadespa-
drãodeumsitedecomprasonlinecomooSubmarinoouaAmazonjáestão
disponíveis,incluindo:
• Navegaçãoebuscanocatálogodeprodutos;
• Páginasdeprodutocomnome,descrição,pre ço,fotoseprodutosrela-
cionados;
• Carrinhodecompras;
• Processodecheckoutcustomizávelincluindocódigospromocionais,
dadosdecobran çaedeentrega;
• Cadastrodeusuário;
• Históricodecompras;
• Ferramentasdeadministraçãopara:catálogodeprodutos,promo ções,
preços,taxasdefreteepáginascomconteúdocustomizado.
12

## Página 31

CasadoCódigo Capítulo2. Tudocomeçaemprodução
Figura2.1:Umapréviadapáginainicialdalojavirtual
Alémdisso,o BroadleafCommerce utilizadiversosframeworksbemes-
tabelecidosnacomunidadeJava,tornandooexemplomaisinteressantedo
pontodevistadeDevOps,poisrepresentabemacomplexidadeenvolvidano
processode buildedeploydeumaaplicaçãoJavanomundoreal. Osdeta-
lhesdeimplementaçãovãoalémdoescopodestelivro,poréméimportante
conhecerumpoucodasprincipaistecnologiaseframeworksutilizadosnesta
aplicação:
•Java:aaplicaçãoéescritaemJava(http://java.oracle.com/),compatível
comaversãoJavaSE6esuperiores.
•Spring:oSpring(http://www.springframework.org/)éumframework
dedesenvolvimentodeaplicaçõescorporativaspopularnacomunidade
Javaqueoferecediversoscomponentescomo:inje çãodedependências,
gerenciamentodetransações,segurança,umframeworkdeMVC,den-
treoutros.
•JPAeHibernate: oJPAéaAPIdepersistênciadoJavaeoHiber-
nate(http://www.hibernate.org/)éaimplementaçãomaisfamosada
JPAnacomunidadeJava,oferecendorecursospararealizaromapea-
mentoobjeto-relacional(object-relationalmapping ouORM)entreob-
jetosJavaeastabelasnobancodedados.
13

## Página 32

2.1. Nossaaplicaçãodeexemplo:alojavirtual CasadoCódigo
•Google Web Toolkit: o GWT (http://developers.google.com/
web-toolkit/)éumframeworkdesenvolvidopeloGoogleparafacilitar
acriaçãodeinterfacesricasquerodamnobrowser. OGWTpermite
queodesenvolvedorescrevacódigoJavaqueéentãocompiladopara
Javascript. AlojavirtualutilizaoGWTparaimplementarainterface
gráficadasferramentasdeadministração.
•ApacheSolr:oSolr(http://lucene.apache.org/solr/)éumservidorde
pesquisaquepermiteaindexaçãodocatálogodeprodutosdalojavir-
tualeofereceumaAPIeficienteeflexívelparaefetuarconsultasdetexto
emtodoocatálogo.
•Tomcat:oTomcat(http://tomcat.apache.org/)éumservidorqueim-
plementaastecnologiasweb–JavaServleteJavaServerPages–doJava
EE.Apesardo BroadleafCommerce rodaremservidoresdeaplicação
alternativos–comoJetty,GlassFishouJBoss–utilizaremosoTomcat
porserumaescolhacomumemdiversasempresasrodandoaplicações
webJava.
•MySQL:oMySQL(http://www.mysql.com/)éumservidordebanco
dedadosrelacional. OJPAeoHibernatepermitemqueaaplicaç ão
rodeemdiversosoutrosservidoresdebancodedados–comoOracle,
PostgreSQLouSQLServer–porémtambémutilizaremosoMySQL
porserumaescolhapopularepordisponibilizarumaversãodecódigo
aberto.
Nãoéumaaplicaçãopequena. Melhorainda:elautilizabibliotecasque
sãofrequentementeencontradasnagrandemaioriadasaplicaçõesJavano
mercado. Comofalamos,vamosutilizá-lacomonossoexemplo,masvocê
tambémpodeseguiroprocessocomasuaprópriaaplicaç ão,ouaindaesco-
lheroutrosoftware,independentedelinguagem,paraaprenderastécnicasde
DevOpsqueserãoapresentadasediscutidasduranteolivro.
Opróximoobjetivoécolocaralojavirtualnoar,porém,antesdefazero
primeirodeploy,éprecisoterumambientedeproduç ãopronto,comservi-
doresondeocódigopossarodar.Oambientedeproduç ãoemnossoexemplo
seráinicialmentecompostode2servidores,conformemostraafigura 2.2.
14

## Página 33

CasadoCódigo Capítulo2. Tudocomeçaemprodução
Figura2.2:Ambientedeproduçãodalojavirtual
Usuáriosacessarãoalojavirtual,querodaráemumainstânciadoTom-
catnoservidorweb.Oservidorwebrodarátodasasbibliotecaseframeworks
Javautilizadospelalojavirtual,inclusiveumainstânciaembutidadoSolr.Por
fim,aaplicaçãowebutilizaráoMySQL,rodandoemumservidordebanco
dedadosseparado.Estaéumaarquiteturawebdeduascamadascomumente
utilizadapordiversasaplicaçõesnomundoreal.Nocapítulo 8discutiremos
commaisdetalhesosfatoresqueinfluenciamaescolhadaarquiteturafísica
parasuaaplicação,porémporenquantovamosusaralgocomumparasim-
plificaroexemploecolocaralojavirtualnoaroquantoantes.
2.2 Instalando o ambiente de produção
Comprarservidoresehardwareparaalojavirtualcustariamuitodinheiro,
entãoinicialmenteiremosusarmáquinasvirtuais.Issopermitirácriartodoo
ambientedeproduçãonanossamáquina.Existemdiversasferramentaspara
rodarmáquinasvirtuais–comoVMwareouParallels–porémalgumassão
pagaseamaioriausaumainterfacegráficaparaconfiguraç ão,oquetornaria
estecapítuloumacole çãode screenshotsdifíceisdeacompanhar.
Pararesolveressesproblemas,usaremosduasferramentasquefacilitamo
usoeconfiguraçãodemáquinasvirtuais:o Vagrant(http://www.vagrantup.
com)eo VirtualBox(http://www.virtualbox.org).OVirtualBoxéumaferra-
mentadaOraclequepermiteconfigurarerodarmáquinasvirtuaisnasprinci-
paisplataformas:Windows,Linux,MacOSXeSolaris.OVirtualBoxpossui
umaferramentadelinhadecomandoparaexecutareconfigurarasmáquinas
virtuais,porémparafacilitaraindamaisotrabalho,usaremosoVagrantque
forneceumaDSLemRubyparadefinir,gerenciareconfigurarambientesvir-
tuais.OVagrantpossuitambémumainterfacedelinhadecomandosimples
15

## Página 34

2.2. Instalandooambientedeprodução CasadoCódigo
parasubireinteragircomessesambientesvirtuais.
CasovocêjápossuaoVagranteoVirtualBoxinstaladosefuncionando,
vocêpodepularparaasubse ção"DeclarandoeSubindoosServidores”.Caso
contrário,oprocessodeinstalaçãodessasferramentasésimples.
InstalandooVirtualBox
Para instalar o VirtualBox, acesse a página dedownloadhttp://www.
virtualbox.org/wiki/Downloadseescolhaaversãomaisatual.Nomomento
daescritadolivro,aversãomaisnovaéoVirtualBox4.3.8eseráaversãouti-
lizadanodecorrerdolivro.Escolhaopacotedeinstalaç ãodeacordocoma
suaplataforma:noWindowsoinstaladoréumarquivoexecutável .exe;no
MacOSXoinstaladoréumpacote .dmg;noLinuxoVirtualBoxdisponibi-
lizapacotes .debou .rpm,dependendodasuadistribuição.
Umavezquevocêtenhafeitoo download,instaleopacote. NoWin-
dows e no Mac OS X, basta dar um duplo clique no arquivo de ins-
talação (.exe no Windows e.dmg no Mac OS X) e seguir as ins-
truções do instalador. No Linux, caso tenha escolhido o pacote.deb,
instale-o executando o comando dpkg -i {arquivo.deb}, substi-
tuindo {arquivo.deb} pelo nome do arquivo baixado, por exemplo
virtualbox-4.3_4.3.8-92456~Ubuntu~raring_i386.deb. Caso
tenhaescolhidoopacote .rpm,instale-oexecutandoocomando rpm -i
{arquivo.rpm},substituindo {arquivo.rpm}pelonomedoarquivobai-
xado,porexemplo VirtualBox-4.3-4.3.8_92456_el6-1.i686.rpm.
Observação:noLinux,casoseuusuárionãoseja root,vocêprecisarárodar
oscomandosanteriorescomocomando sudonafrente,porexemplo: sudo
dpkg -i {arquivo.deb}ou sudo rpm -i {arquivo.rpm}.
ParatestarqueoVirtualBoxestáinstaladocorretamente,acesseotermi-
naleexecuteocomando VBoxManage -v.ParaabriroterminalnoWin-
dows,vocêpodeusar Win+Redigitar cmd.Casotudoestejacorreto,oco-
mandoretornaráalgocomo“4.3.8r92456”,dependendodaversãoinstalada.
InstalandooVagrant
UmavezqueoVirtualBoxestiverinstalado,prossigacomoprocessode
instalaçãodoVagrant,queébemparecido.Acesseapáginade downloaddo
16

## Página 35

CasadoCódigo Capítulo2. Tudocomeçaemprodução
Vagranthttp://www.vagrantup.com/downloads.htmleescolhaaversãomais
atual. Nomomentodaescritadolivro,aversãomaisnovaéoVagrant1.5.1
eseráaversãoutilizadanodecorrerdolivro.Faç ao downloaddopacotede
instalaçãodeacordocomasuaplataforma:noWindowsoinstaladoréum
arquivo .msi;noMacOSXoinstaladoréumpacote .dmg;noLinuxoVa-
grantdisponibilizapacotes .debou .rpm,dependendodasuadistribuição.
Assimquetenhafeitoo downloaddopacote,instale-o: noWindowse
noMacOSX,bastadarumduplocliquenoarquivodeinstalaç ão( .msi
no Windows e.dmg no Mac OS X) e seguir as instruções do instala-
dor. NoLinux, bastaseguirosmesmospassosdainstalaç ãodoVirtual-
BoxnoLinuxusandoopacoteescolhido( vagrant_1.5.1_i686.debou
vagrant_1.5.1_i686.rpm). NoMacOSXenoWindows,ocomando
vagrantjáécolocadono PATHapósainstalação.NoLinux,vocêvaipreci-
saradicionar /opt/vagrant/binnoseu PATH.
ParatestarqueoVagrantestáinstaladocorretamente,acesseoterminal
eexecuteocomando vagrant -v. Casotudoestejacorreto,ocomando
retornaráalgocomo“Vagrant1.5.1”,dependendodaversãoinstalada.
Oúltimopassonecessárioéconfigurarumaimageminicialqueservede
templateparainicializarcadamáquinavirtual. Estasimagens,tambémco-
nhecidascomo box,servemcomopontodepartida,contendoosistemaope-
racionalbásico.Nonossocaso,utilizaremosuma boxoferecidapelopróprio
Vagrant,quecontémaimagemdeumLinuxUbuntu12.04LTSde32bits.
Parabaixareconfiguraresta box,éprecisoexecutarocomando:
$ vagrant box add hashicorp/precise32
==> box: Loading metadata for box ’hashicorp/precise32’
box: URL: https://vagrantcloud.com/hashicorp/precise32
...
Essecomandoiráfazero downloaddoarquivodeimagemdamáquina
virtual, queégrande(299MB),portantoelevaidemorarparaexecutare
umaboaconexãocomainternetseránecessária. Umalistadeoutrasima-
gens disponibilizadas pela comunidade Vagrant pode ser encontrada em
http://www.vagrantbox.es/eoprocessodeinicializaçãoéparecidocomoco-
mandoanterior. AempresaportrásdoVagrant,aHashiCorp,introduziu
17

## Página 36

2.2. Instalandooambientedeprodução CasadoCódigo
recentementeoVagrantCloud (https://vagrantcloud.com/),umaformade
encontrarecompartilhar boxescomacomunidade.
Declarandoesubindoosservidores
UmavezqueoVagranteoVirtualBoxestãofuncionando,declararege-
renciarumambientevirtualésimples.Adeclaraçãodeconfiguraçãodasmá-
quinasvirtuaiséfeitaemumarquivochamado Vagrantfile.Ocomando
vagrant initcriaumarquivo Vagrantfileinicial,comcomentários
queexplicamtodasasop çõesdeconfiguraçãodisponíveis.
Nonossocaso,iremoscome çardeformasimpleseconfigurarapenas
onecessárioparasubirosdoisservidoresdeproduç ão. Oconteúdodo
Vagrantfilequeprecisamosé:
VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
config.vm.box = "hashicorp/precise32"
config.vm.define :db do |db_config|
db_config.vm.network :private_network, :ip => "192.168.33.10"
end
config.vm.define :web do |web_config|
web_config.vm.network :private_network, :ip => "192.168.33.12"
end
end
Essearquivoconfiguraduasmáquinasvirtuais,comapelidosde“ db”
e“web”. Ambasutilizarãoabox hashicorp/precise32queinstala-
mosanteriormente. Cadaumapossuiumblocodeconfiguraç ãoquede-
fineumendere çoIPparaconfiguraraconexãocomarede.Osendere çosIP
192.168.33.10e 192.168.33.12foramescolhidosdeformaarbitrária
paraevitarconflitoscomasconfiguraçõesderededasuamáquina.
Parasubirosservidores,bastaexecutarocomando vagrant upno
mesmodiretórioondeoarquivo VagrantfilefoicriadoeoVagrantto-
marácontadesubireconfigurarasmáquinasvirtuaisparavocê. Setudo
correrbem,asaídadocomandoseráalgoparecidocom:
18

## Página 37

CasadoCódigo Capítulo2. Tudocomeçaemprodução
$ vagrant up
Bringing machine ’db’ up with ’virtualbox’ provider...
Bringing machine ’web’ up with ’virtualbox’ provider...
==> db: Importing base box ’hashicorp/precise32’...
==> db: Matching MAC address for NAT networking...
==> db: Checking if box ’hashicorp/precise32’ is up to date...
==> db: Setting the name of the VM: blank_db_1394680068450_7763
==> db: Clearing any previously set network interfaces...
==> db: Preparing network interfaces based on configuration...
db: Adapter 1: nat
db: Adapter 2: hostonly
==> db: Forwarding ports...
db: 22 => 2222 (adapter 1)
==> db: Booting VM...
==> db: Waiting for machine to boot. This may take a few
minutes...
db: SSH address: 127.0.0.1:2222
db: SSH username: vagrant
db: SSH auth method: private key
==> db: Machine booted and ready!
==> db: Configuring and enabling network interfaces...
==> db: Mounting shared folders...
db: /vagrant => /private/tmp/blank
==> web: Importing base box ’hashicorp/precise32’...
==> web: Matching MAC address for NAT networking...
==> web: Checking if box ’hashicorp/precise32’ is up to date...
==> web: Setting the name of the VM:
blank_web_1394680087001_3842
==> web: Fixed port collision for 22 => 2222. Now on port 2200.
==> web: Clearing any previously set network interfaces...
==> web: Preparing network interfaces based on configuration...
web: Adapter 1: nat
web: Adapter 2: hostonly
==> web: Forwarding ports...
web: 22 => 2200 (adapter 1)
==> web: Booting VM...
==> web: Waiting for machine to boot. This may take a few
minutes...
web: SSH address: 127.0.0.1:2200
19

## Página 38

2.3. Configurandodependênciasnosservidoresdeprodução CasadoCódigo
web: SSH username: vagrant
web: SSH auth method: private key
==> web: Machine booted and ready!
==> web: Configuring and enabling network interfaces...
==> web: Mounting shared folders...
web: /vagrant => /private/tmp/blank
Issosignificaqueasmáquinasvirtuaisestãofuncionandoeprontaspara
seremusadas.Sevocêlerasaídacomcuidado,veráqueospassosforamos
mesmosparaambasasmáquinas dbe web. Alémdisso,oVagranttam-
bémmapeouportasdeSSHemontouumapartiç ãoparaacessarosarquivos
existentesnodiretóriodamáquinahospedeira.Issopodesoarumpoucocon-
fuso,masdemonstraalgumasdasfuncionalidadespoderosasqueoVagrant
disponibiliza.
2.3 Configurando dependências nos servidores
de produção
Agoraqueosservidoresestãorodando,éprecisoinstalarospacotesedepen-
dênciasparaquealojavirtualfuncione.Administradoresdesistemaprova-
velmentejáestãoacostumadosatrabalharemdiversasmáquinasaomesmo
tempo,porémdesenvolvedoresgeralmentetrabalhamsempreemumamá-
quinasó.
Naspróximasse çõescomeçaremosainteragircommaisdeumamáquina
aomesmotempoeamaiorpartedoscomandosprecisarãoserexecutadosno
servidorcorreto. Usaremosumanotaçãoespecialparaguiarasinstruções
norestantedolivro,representandoousuárioeoservidorno promptdali-
nhadecomandoparaservirdelembreteparavocêverificarseestárodando
ocomandonoservidorcerto. Opadrãoserá {usuário}@{servidor}$,
noqualousuáriogeralmenteserá vagranteoservidorpodevariarentre
dbou web. Destaforma,comandosprecedidosde vagrant@db$devem
serexecutadosnoservidor dbecomandosprecedidosde vagrant@web$
devemserexecutadosnoservidor web.
Aoinvésdepulardeumservidorparaooutro,iremosfocarinicialmente
emumservidorporvez,come çandopeloservidordebancodedados.
20

## Página 39

CasadoCódigo Capítulo2. Tudocomeçaemprodução
Servidordebancodedados
Primeiramente,precisamoslogarnoservidordebancodedadosparains-
talaroMySQL.Issoéfeitoatravésdocomando vagrant ssh db,queabre
umasessãoSSHcomoservidor db.Umavezlogado,ainstalaçãodoservidor
MySQLéfeitaatravésdopacote mysql-server:
vagrant@db$ sudo apt-get update
Ign http://us.archive.ubuntu.com precise InRelease
Ign http://us.archive.ubuntu.com precise-updates InRelease
...
Reading package lists... Done
vagrant@db$ sudo apt-get install mysql-server
Reading package lists... Done
Building dependency tree
...
ldconfig deferred processing now taking place
Paraentenderoqueestáacontecendo,vamosanalisarcadapartedesse
comando. Ocomando apt-getéusadoparagerenciarquaispacoteses-
tãoinstaladosnosistema. Ainstrução updateatualizaoíndicedepaco-
tesparaasúltimasversões. Ainstruç ão installserveparainstalarum
novopacotenosistema. Nessecasoopacotequequeremosinstalaréopa-
cote mysql-serverquecontémoservidorMySQL.Ocomandointeiroé
precedidopelocomando sudo.EmsistemasUNIX,existeumusuárioespe-
cialcom“superpoderes”conhecidocomousuáriorooteocomando sudo
permiteexecutaralgocomoseousuárioatualfosse root.
OprocessodeinstalaçãodoservidorMySQLexigeaescolhadeumase-
nhadeacessoparaousuário root.Vocêprecisaráforneceressasenhaduas
vezesnoprocessodeinstalação.Aescolhadeumasenhaseguraéimportante
paragarantiraseguran çadosistema,porémétambémumtópicodediscus-
sãoàparte,queabordaremosnocapítulo 8. Sealguémdescobrirasenha
mestre,elepoderáexecutarqualquercomandonobancodedados,inclusive
apagartodasastabelas!Navidarealvocênãoquerqueissoaconte ça,porém,
noexemplodolivro,usaremosumasenhasimplesparafacilitar:“secret”.Se
preferir,vocêpodeescolheroutrasenha,masdaquiparafrentetomecuidado
21

## Página 40

2.3. Configurandodependênciasnosservidoresdeprodução CasadoCódigo
parasubstituirqualquermen çãodasenha“secret”pelasenhaquevocêesco-
lheu.
Ao terminar a instalação do pacote, o servidor MySQL já vai estar
rodando, porém apenas para acesso local. Como precisamos acessar o
bancodedadosdoservidorweb,éprecisoconfiguraroMySQLparaper-
mitirconexõesexternas. Paraisto, bastacriaroarquivodeconfiguraç ão
/etc/mysql/conf.d/allow_external.cnf. Vocêpodeusaroeditor
detextoquepreferir–emacse vimsãoduasop çõescomuns–porémaqui
usaremoso nanoporserumeditormaissimplesdeaprenderparaquemnão
estáacostumadoaeditararquivosnalinhadecomando.Ocomandoseguinte
criaoarquivo(como rootnovamente)desejado:
vagrant@db$ sudo nano /etc/mysql/conf.d/allow_external.cnf
Bastaentãodigitaroconteúdodoarquivoabaixoeusar Ctrl+Opara
salvare Ctrl+Xparasalvaresairdoeditor:
[mysqld]
bind-address = 0.0.0.0
Umavezqueoarquivofoicriado,éprecisoreiniciaroservidorMySQL
paraqueelepercebaanovaconfiguraç ão.Issoéfeitocomocomando:
vagrant@db$ sudo service mysql restart
mysql stop/waiting
mysql start/running, process 6460
Nestemomento,oservidorMySQLjáestáprontoerodando,porémainda
nãocriamosnenhumbancodedados.Écomumquecadaaplicaç ãocrieseu
própriobancodedados,ou schema,parapersistirsuastabelas,índiceseda-
dos.Precisamosentãocriarumbancodedadosparaalojavirtual,quecha-
maremosde loja_schema,atravésdocomando:
vagrant@db$ mysqladmin -u root -p create loja_schema
Enter password:
Aoexecutarestecomando,aop ção -u rootinstruiqueaconexãocom
oMySQLdeveserfeitacomousuáriorooteaop ção -piráperguntarase-
nha,quenessecasoserá“secret”.Orestodocomandoéautoexplicativo.Para
22

## Página 41

CasadoCódigo Capítulo2. Tudocomeçaemprodução
verificarqueobancodedadosfoicriadocomsucesso,vocêpodeexecutaro
seguintecomandoquelistatodososbancodedadosexistentes:
vagrant@db$ mysql -u root -p -e "SHOW DATABASES"
Enter password:
+--------------------+
| Database |
+--------------------+
| information_schema |
| loja_schema |
| mysql |
| performance_schema |
| test |
+--------------------+
Assimcomonãoérecomendávelexecutarcomandosnosistemaopera-
cionalcomousuário root,nãoérecomendávelexecutarqueriesnoMySQL
comousuário root.Umaboapráticaécriarusuáriosespecíficosparacada
aplicação,liberandoapenasoacessonecessárioparaaaplicaç ãorodar.Além
disso,ainstalaçãopadrãodoservidorMySQLincluiumacontaanônimapara
acessoaobancodedados.Antesdecriaracontaparaalojavirtual,precisa-
mosremoveracontaanônima:
vagrant@db$ mysql -uroot -p -e "DELETE FROM mysql.user WHERE
user=’’; \
> FLUSH PRIVILEGES"
Enter password:
Umavezqueacontaanônimafoiremovida,criaremosumusuáriocha-
mado loja,comumasenha“lojasecret”,comacessoexclusivoaoschema
loja_schema:
vagrant@db$ mysql -uroot -p -e "GRANT ALL PRIVILEGES ON
loja_schema.* \
> TO ’loja’@’%’ IDENTIFIED BY ’lojasecret’;"
Enter password:
Paratestarqueonovousuáriofoicriadocorretamente,podemosexecutar
umaquerysimplesparaverificarquetudoestáOK(asenhadeveser“lojase-
23

## Página 42

2.3. Configurandodependênciasnosservidoresdeprodução CasadoCódigo
cret”poisestamosexecutandoocomandocomousuário lojaaoinvésde
root):
vagrant@db$ mysql -u loja -p loja_schema -e
"select database(), user()"
Enter password:
+--------------+----------------+
| database() | user() |
+--------------+----------------+
| loja_schema | loja@localhost |
+--------------+----------------+
Nesteponto,oservidordebancodedadosjáestáconfiguradoerodando
corretamente.Paradeslogardamáquinavirtual db,vocêpodedigitaroco-
mando logoutoupressionar Ctrl+D.Obancodedadosaindaestávazio–
nenhumatabelaoudadosforamcriados–porémiremoscuidardistonase ção
2.4.Antesdisso,precisamosterminardeconfigurarorestodainfraestrutura:
oservidorweb.
Servidorweb
IremosinstalaroTomcateconfigurarumafontededadosparausaro
bancodedadoscriadoanteriormente.Paraisto,precisamoslogarnoservidor
rodandoocomando vagrant ssh web,queabreumasessãoSSHcomo
servidor web. Umavezlogado,ainstalaçãodoTomcatéfeitaatravésdo
pacote tomcat7.Tambémprecisamosinstalaroclienteparaconectarcom
obancodedadosMySQL,disponívelnopacote mysql-client:
vagrant@web$ sudo apt-get update
Ign http://us.archive.ubuntu.com precise InRelease
Ign http://us.archive.ubuntu.com precise-updates InRelease
...
Reading package lists... Done
vagrant@web$ sudo apt-get install tomcat7 mysql-client
Reading package lists... Done
Building dependency tree
...
ldconfig deferred processing now taking place
24

## Página 43

CasadoCódigo Capítulo2. Tudocomeçaemprodução
IstoiráinstalaroTomcat7,oclienteMySQLetodasassuasdependências,
incluindooJava6. ParaverificarqueoTomcatestárodandocorretamente,
vocêpodeabrirseunavegadoredigitaraURL http://192.168.33.12:8080/do
servidorweb–192.168.33.12foioendere çoIPconfiguradonoVagrant
e 8080éaportaondeoTomcatrodaporpadrão. Setudoestiverok,você
deveverumapáginacomumamensagem "Itworks!”.
Alojavirtualprecisadeumaconexãoseguracomoservidorparatransfe-
rirdadospessoais–comosenhasounúmerosdecartãodecrédito–deforma
criptografada.Paraisso,precisamosconfigurarumconectorSSLparaqueo
TomcatconsigarodartantoemHTTPquantoHTTPS.ConexõesSSLusam
umcertificadoassinadoporumaautoridadeconfiávelparaidentificaroser-
vidoreparacriptografarosdadosquetrafegamentreoseunavegadoreoser-
vidor.Usaremosaferramenta keytool,queépartedadistribuiçãopadrão
doJava,paragerarumcertificadoparaonossoservidorweb. Duranteeste
processo,vocêprecisaráfornecerdiversasinformaçõessobreoservidoralém
deumasenhaparaprotegero keystore,quenonossocasoseránovamente
“secret”parasimplificar. Ocomandocompleto,juntamentecomexemplos
dosdadosqueprecisamserfornecidos,fica:
vagrant@web$ cd /var/lib/tomcat7/conf
vagrant@web$ sudo keytool -genkey -alias tomcat -keyalg RSA \
> -keystore .keystore
Enter keystore password:
Re-enter new password:
What is your first and last name?
[Unknown]: Loja Virtual
What is the name of your organizational unit?
[Unknown]: Devops na Prática
What is the name of your organization?
[Unknown]: Casa do Código
What is the name of your City or Locality?
[Unknown]: São Paulo
What is the name of your State or Province?
[Unknown]: SP
What is the two-letter country code for this unit?
[Unknown]: BR
Is CN=Loja Virtual, OU=Devops na Prática, ..., C=BR correct?
25

## Página 44

2.3. Configurandodependênciasnosservidoresdeprodução CasadoCódigo
[no]: yes
Enter key password for <tomcat>
(RETURN if same as keystore password):
Explicandoocomandopassoapasso:aop ção -genkeygeraumanova
chave;aop ção -alias tomcatdefineumapelidoparaocertificado;aop-
ção -keyalg RSAespecificaoalgoritmousadoparagerarachave,nesse
casoRSA;porfim,aop ção -keystore .keystoredefineoarquivoque
armazenaráo keystore. Esteformatodearquivopermitearmazenardi-
versaschaves/certificadosnomesmo keystore,porissoébomescolher
umapelidoparaocertificadogeradoparaoTomcat. Alémdisso,tantoo
keystorequantoocertificadodoTomcatsãoprotegidosporsenha.Nesse
caso,usamos“secret”paraambos.
Umavezqueocertificadofoicriadoearmazenado,precisamosconfigurar
oservidordoTomcatparahabilitaroconectorSSL.Issoéfeitoeditandoo
arquivo /var/lib/tomcat7/conf/server.xml:
vagrant@web$ sudo nano /var/lib/tomcat7/conf/server.xml
Dentrodestearquivo,adefiniçãodoconectorSSLparaaporta8443já
estápredefinida,porémcomentada. Vocêprecisadescomentaradefinição
desteconectoreadicionarmaisdoisatributosquerepresentamoarquivodo
keystoreeasenhadeprote ção. AparterelevantedoarquivoXMLque
precisamosalteraré:
<?xml version=’1.0’ encoding=’utf-8’?>
<Server port="8005" shutdown="SHUTDOWN">
...
<Service name="Catalina">
...
<!-- Define a SSL HTTP/1.1 Connector on port 8443
This connector uses the JSSE configuration, when using
APR, the connector should be using the OpenSSL style
configuration described in the APR documentation -->
<Connector port="8443" protocol="HTTP/1.1"
SSLEnabled="true"
26

## Página 45

CasadoCódigo Capítulo2. Tudocomeçaemprodução
maxThreads="150" scheme="https" secure="true"
keystoreFile="conf/.keystore"
keystorePass="secret"
clientAuth="false" sslProtocol="SSLv3" />
...
</Service>
</Server>
Aconfiguraçãodoservidorwebestáquaseprontaaqui. Aúltimaal-
teraçãoqueprecisamosfazeréaumentaraquantidadedememóriaqueo
Tomcatpodeusar. Alojavirtualexigemaismemóriadoqueainstalaç ão
padrãodoTomcatdefine,porissoprecisamosalterarumalinhanoarquivo
/etc/default/tomcat7:
vagrant@web$ sudo nano /etc/default/tomcat7
Alinhaquedefineaop ção JAVA_OPTSprecisaseralteradaparaper-
mitirqueamáquinavirtualdoJavauseaté512Mbdememória,aoinvésda
configuraçãopadrãode128Mb.Apósaalteraç ão,aop ção JAVA_OPTSdeve
ficar:
JAVA_OPTS="-Djava.awt.headless=true -Xmx512M
-XX:+UseConcMarkSweepGC"
Porfim,paraquetodasasconfiguraçõessejamaplicadas,precisamosrei-
niciaroservidorTomcat:
vagrant@web$ sudo service tomcat7 restart
Paraverificarquetudoestáfuncionando,vocêpodevoltarnonavega-
doretentaracessarapáginapadrãoatravésdoconectorSSL,acessandoa
URL https://192.168.33.12:8443/.Dependendodequalnavegadorvocêestáuti-
lizando,umavisoirásurgirparaalertarqueocertificadodoservidorfoiau-
toassinado.Emumcenárioreal,vocêgeralmentecompraumcertificadoSSL
assinadoporumaautoridadeconfiável,masnessecasoiremosprosseguire
aceitaroalertapoissabemosqueocertificadofoiautoassinadointencional-
mente.Setudodercerto,vocêveránovamenteapágina "Itworks!”,dessavez
usandoumaconexãoseguraemHTTPS.
Nestemomento,ambososservidoresestãoconfiguradoseprontospara
aúltimaetapa:fazero buildedeployparacolocaralojavirtualemproduç ão!
27

## Página 46

2.4. Buildedeploydaaplicação CasadoCódigo
2.4 Build e deploy da aplicação
Atéagora,aconfiguraçãodosservidoresdebancodedadosewebforamre-
lativamentegenéricas.Instalamosospacotesdesoftwarebásicospararodar
oMySQLeoTomcat,configuramosconectoresparaHTTP/HTTPS,criamos
umusuárioeumbancodedadosvazio,queporenquantonãoestãodireta-
menteassociadosàlojavirtualanãoserpelonomedo schemaedousuário
queescolhemos.
Chegouomomentodebaixarecompilarocódigo,rodarostestes,empa-
cotaraaplicaçãoecolocaralojavirtualnoar!Esseprocessodecompilaç ão,
testeeempacotamentoéconhecidocomo build. Asetapasdoprocessode
buildtambémpodemincluirgerenciamentodedependências,rodarferra-
mentasdeanáliseestáticadocódigo,coberturadecódigo,geraç ãodedocu-
mentação,dentreoutros.Aprincipalfun çãodoprocessode buildégerarum
oumaisartefatos,comversõesespecíficas,quesetornampotenciaiscandida-
tos,ou releasecandidates,parao deployemprodução.
Geralmenterecomenda-serodaroprocessode buildemumambientepa-
recidocomoambientedeproduçãoparaevitarincompatibilidadesdesistema
operacionalouversõesdebibliotecas.PoderíamosatéconfiguraroVagrant
paracriarumanovamáquinavirtualparautilizarmoscomoservidorde build.
Porém,parafacilitaradiscussãonestecapítulo,faremoso buildnoservidor
web,queéondeo deployvaiacontecer. Issoeconomizarádiversospassos
agora,porémvamosrevisitaresteprocessonocapítulo 6.
Para realizar obuild, é preciso instalar mais algumas ferramentas: o
Git(http://git-scm.com/)paracontroledeversão,o Maven(http://maven.
apache.org/)paraexecutaro buildemsieo JDK(JavaDevelopmentKit)para
conseguirmoscompilarocódigoJava:
vagrant@web$ sudo apt-get install git maven2 openjdk-6-jdk
Reading package lists... Done
Building dependency tree
...
ldconfig deferred processing now taking place
Umavezqueessasferramentasforaminstaladas,precisamosbaixarocó-
digoqueestáhospedadonoGithubatravésdocomando git clone,eexe-
cutaro buildrodandoocomando mvn install:
28

## Página 47

CasadoCódigo Capítulo2. Tudocomeçaemprodução
vagrant@web$ cd
vagrant@web$ git clone https://github.com/dtsato/
loja-virtual-devops.git
Cloning into ’loja-virtual-devops’...
remote: Counting objects: 11358, done.
remote: Compressing objects: 100% (3543/3543), done.
remote: Total 11358 (delta 6053), reused 11358 (delta 6053)
Receiving objects: 100% (11358/11358), 55.47 MiB | 1.14 MiB/s,
done.
Resolving deltas: 100% (6053/6053), done.
vagrant@web$ cd loja-virtual-devops
vagrant@web$ export MAVEN_OPTS=-Xmx256m
vagrant@web$ mvn install
[INFO] Scanning for projects...
[INFO] Reactor build order:
[INFO] loja-virtual-devops
[INFO] core
[INFO] admin
[INFO] site
[INFO] combined
[INFO] ----------------------------------------------------
[INFO] Building loja-virtual-devops
[INFO] task-segment: [install]
[INFO] ----------------------------------------------------
...
AprimeiraexecuçãodoMavenvaidemorarde20a25minutospoisdi-
versascoisasacontecem:
•Sub-projetos:oprojetoestáorganizadoem4módulos: corepossui
asconfiguraçõesprincipais,extensõesecustomizaçõesdalojavirtual;
siteéaaplicaçãowebdalojavirtual; adminéumaaplicaçãoweb
restritaparaadministraçãoegerenciamentodalojavirtual;porfim,
combinedéummóduloqueagregaasduasaplicaçõeswebeo core
emumúnicoartefato.Cadamóduloatuacomoumsubprojetoqueo
Mavenprecisarealizaro buildseparadamente.
•Resoluçãodedependências:oMaveniráresolvertodasasdependên-
ciasdoprojetoebaixarasbibliotecaseframeworksnecessáriospara
29

## Página 48

2.4. Buildedeploydaaplicação CasadoCódigo
compilarerodarcadamódulodalojavirtual.
•Compilação:ocódigoJavaeGWTprecisasercompiladoparaexecu-
ção. Issotomaumbomtemponaprimeiravez. OcompiladorJavaé
inteligenteosuficientepararecompilarapenasonecessárioem builds
subsequentes.
•Testesautomatizados:emmódulosquedefinemtestesautomatizados,
oMaveniráexecutá-losegerarrelatóriosdequaistestespassarame
quaisfalharam.
•Empacotamentodeartefatos:porfim,omódulo coreseráempaco-
tadocomoumarquivo .jarenquantoosmódulosweb( site, admin
e combined)serãoempacotadoscomoumarquivo .war.Ambosos
arquivos jare warsãoequivalentesaarquivos zipquevocêbaixa
regularmentedainternet,noentantoaestruturainternadospacotesé
bemdefinidaepadronizadapeloJava:o jarcontémclassescompi-
ladaseservecomobibliotecaenquantoo warcontémclasses,biblio-
tecas,arquivosestáticosedeconfiguraçãonecessáriospararodaruma
aplicaçãowebemum containerJavacomooTomcat.
Aofinaldaexecuçãodoprocessode build,setudocorrerbem,vocêdeve
verumrelatóriodoMavenparecidocom:
...
[INFO] ----------------------------------------------------
[INFO] Reactor Summary:
[INFO] ----------------------------------------------------
[INFO] loja-virtual-devops ............... SUCCESS [1:35.191s]
[INFO] core .............................. SUCCESS [6:51.591s]
[INFO] admin ............................. SUCCESS [6:54.377s]
[INFO] site .............................. SUCCESS [4:44.313s]
[INFO] combined .......................... SUCCESS [25.425s]
[INFO] ----------------------------------------------------
[INFO] ----------------------------------------------------
[INFO] BUILD SUCCESSFUL
[INFO] ----------------------------------------------------
[INFO] Total time: 20 minutes 31 seconds
30

## Página 49

CasadoCódigo Capítulo2. Tudocomeçaemprodução
[INFO] Finished at: Sat Mar 15 02:34:24 UTC 2014
[INFO] Final Memory: 179M/452M
[INFO] ----------------------------------------------------
Issosignificaqueo buildrodoucomsucessoeoartefatoquenosinteressa
paradeployéoarquivo devopsnapratica.wardomódulo combined,
queseencontranodiretório combined/target.
Antesdefazero deploydoarquivo war,aúltimaconfiguraçãonecessária
noTomcatéadefiniçãodasfontesdedado,ou DataSource,queaaplicação
iráacessarparaconectarcomobancodedados.Setaisdefiniçõesestivessem
dentrodoartefatoemsi,nósprecisaríamosrealizarumnovo buildtodavez
queosparâmetrosdeconexãocomobancodedadosmudassemoucasoqui-
séssemosrodaramesmaaplicaçãoemambientesdiferentes.Emvezdisso,a
aplicaçãodependederecursosabstratosatravésdaespecificaç ãoJNDI(Java
NamingandDirectoryInterface). Estesrecursosprecisamserconfigurados
eexpostospelo container,possibilitandoaalteraçãosemnecessidadedeum
novobuild.
A loja virtual precisa de três fontes de dados no JNDI chamadas
jdbc/web, jdbc/secure e jdbc/storage. No nosso caso, usare-
mosomesmobancodedadosparaostrêsrecursos,definidosnoarquivo
context.xml:
vagrant@web$ sudo nano /var/lib/tomcat7/conf/context.xml
Asconfiguraçõesrelevantessãoostrêselementos <Resource>eadife-
rençaentreeleséapenasoatributo name:
<?xml version=’1.0’ encoding=’utf-8’?>
<Context>
<WatchedResource>WEB-INF/web.xml</WatchedResource>
<Resource name="jdbc/web" auth="Container"
type="javax.sql.DataSource" maxActive="100" maxIdle="30"
maxWait="10000" username="loja" password="lojasecret"
driverClassName="com.mysql.jdbc.Driver"
url="jdbc:mysql://192.168.33.10:3306/loja_schema"/>
31

## Página 50

2.4. Buildedeploydaaplicação CasadoCódigo
<Resource name="jdbc/secure" auth="Container"
type="javax.sql.DataSource" maxActive="100" maxIdle="30"
maxWait="10000" username="loja" password="lojasecret"
driverClassName="com.mysql.jdbc.Driver"
url="jdbc:mysql://192.168.33.10:3306/loja_schema"/>
<Resource name="jdbc/storage" auth="Container"
type="javax.sql.DataSource" maxActive="100" maxIdle="30"
maxWait="10000" username="loja" password="lojasecret"
driverClassName="com.mysql.jdbc.Driver"
url="jdbc:mysql://192.168.33.10:3306/loja_schema"/>
</Context>
Parafazero deploydalojavirtualemsi,simplesmenteprecisamoscopiar
oartefato warparaolugarcertoeoTomcatfaráonecessárioparacolocara
lojavirtualnoar:
vagrant@web$ cd ~/loja-virtual-devops
vagrant@web$ sudo cp combined/target/devopsnapratica.war \
> /var/lib/tomcat7/webapps
Assimcomoo builddemorouumpouco,oprocessode deploytambém
vailevaralgunsminutosnaprimeiravez,poisaaplicaç ãoirácriarastabelas
epopularosdadosusandooHibernate.Vocêpodeacompanharoprocesso
dedeployolhandoparaoslogsdoTomcat.Ocomando tail -féútilnesse
casopoiselemostraemtemporealtudoqueestáacontecendonolog:
vagrant@web$ tail -f /var/lib/tomcat7/logs/catalina.out
Mar 15, 2014 2:08:51 AM org.apache.coyote.AbstractProtocol start
INFO: Starting ProtocolHandler ["http-bio-8080"]
Mar 15, 2014 2:08:51 AM org.apache.coyote.AbstractProtocol start
INFO: Starting ProtocolHandler ["http-bio-8443"]
Mar 15, 2014 2:08:51 AM org.apache.catalina.startup.Catalina
start
INFO: Server startup in 408 ms
...
Odeployterminaassimquevocêperceberqueasatividadesnologpara-
ram. Paraterminarocomando tailvocêpodeusar Ctrl+C.Agoraésó
32

## Página 51

CasadoCódigo Capítulo2. Tudocomeçaemprodução
testarquetudoestáfuncionando:abraumanovajanelanonavegadoredigite
aURL http://192.168.33.12:8080/devopsnapratica/. Parabéns,alojavirtualestá
emprodução!
Figura2.3:Páginadeadministraçãodalojavirtual
Vocêtambémpodeacessarapáginadeadministraçãoqueseencontrana
URL http://192.168.33.12:8080/devopsnapratica/admin/(abarranofinaldaURL
éimportante).Entrandocomousuário“admin”esenha“admin”vocêpode
navegarpelaspáginasdeadministraçãoegerenciarocatálogodeprodutos,
categorias,oconteúdodaspáginasdalojavirtual,gerenciarpedidos,assim
comousuáriosepermissões.
Agoraqueestamosemproduçãoeconquistamosaúltimamilha,pode-
mosfocarnosprincípiosepráticasdeDevOpsnecessáriosparaoperarnossa
aplicaçãoemprodução,aomesmotempopermitindoquenovasmudan ças
sejamintroduzidasdeformaconfiável.
33

## Página 53

Capítulo3
Monitoramento
Agoraquealojavirtualestáemproduç ão,conquistamosapartemaisim-
portantedociclodevidadequalquer software. Noentanto,estefoiapenas
oprimeiropasso!Daquiparafrente,precisamosvestirochapéudotimede
operaçõesenosresponsabilizarpelaestabilidadedosistemaemproduç ão:
precisamosgarantirquealojavirtualcontinuefuncionandosemproblemas.
Comosaberseosistemaestáfuncionandonormalmenteouseestáfora
doar?Vocêpodeacessaralojavirtualmanualmenteeverificarseestátudo
ok,porémissolevatempoedependedevocêlembrardefazê-lo.Vocêtam-
bémpodeesperarporreclamaçõesdeseususuários,masessatambémnãoé
umaboaop ção.Sistemasdemonitoramentoexistempararesolveressepro-
blema.Vocêdefinequaisverificaçõessãonecessáriasparasaberseosistema
estáfuncionandoeosistemademonitoramentoenvianotificaçõesassimque
algumaverificaçãofalhar.
Umbomsistemademonitoramentoiráalertá-loquandoalgoestiverer-

## Página 54

3.1. Instalandooservidordemonitoramento CasadoCódigo
rado,permitindoquevocêinvestigueearrumeoqueestivercausandoproble-
masomaisrápidopossível.Destaforma,vocênãoprecisadependerdeseus
usuáriosavisaremquandoalgoestáforadoar,possibilitandoumaabordagem
maisproativapararesoluçãodeproblemas.
Nestecapítuloiremosinstalarumsistemademonitoramentoeconfigurá-
locomváriasverificaçõesparagarantirquealojavirtualestejafuncionando
emprodução.Utilizaremosumadasferramentasdemonitoraç ãomaisutili-
zadasporequipesdeoperações:o Nagios(http://www.nagios.org/).Apesar
deserumaferramentaantigaepossuirumainterfacegráficanãomuitoami-
gável,eleaindaéumadasop çõesmaispopularesporterumaimplementação
robustaeumecossistemaenormedepluginsescritosemantidospelacomu-
nidade.Aofinaldocapítulo,nossoambientedeproduç ãoincluiráumnovo
servidor,conformemostraafigura 3.1.
Figura3.1:Ambientedeproduçãodalojavirtual
3.1 Instalando o servidor de monitoramento
Emumsistemademonitoramento,osservidoresgeralmenteatuamemdois
papéisprincipais:supervisorousupervisionado.O supervisoréresponsável
porcoletarinformaçõessobreorestodainfraestrutura,avaliarseelaestásau-
dáveleenviaralertascasoencontrealgumproblema.Os supervisionadossão
osservidoresquefazemotrabalhorealquevocêestáinteressadoemmoni-
torar. Nanossalojavirtual,oservidorwebeoservidordebancodedados
36

## Página 55

CasadoCódigo Capítulo3. Monitoramento
serãosupervisionadosporumnovoservidorqueiremosinstalareconfigurar
paraatuarcomosupervisor.
Rodarosupervisorexternamenteaosservidoressupervisionadoséuma
boaprática. Seosupervisorestiverrodandonamesmamáquinaealgum
problemaacontecer,ambosficarãoindisponíveisevocênãoconseguiráser
alertadodoproblema.Poressemotivo,iremosdeclararumanovamáquina
virtualnoarquivo Vagrantfile,comoapelido monitoreendereçoIP
192.168.33.14:
Vagrant.configure("2") do |config|
config.vm.box = "precise32"
config.vm.define :db do |db_config|
db_config.vm.network :private_network,
:ip => "192.168.33.10"
end
config.vm.define :web do |web_config|
web_config.vm.network :private_network,
:ip => "192.168.33.12"
end
config.vm.define :monitor do |monitor_config|
monitor_config.vm.network :private_network,
:ip => "192.168.33.14"
end
end
Apóssalvaroarquivo,bastaexecutar vagrant upnomesmodiretó-
rioparasubironovoservidor. Setudodercerto,asaídadocomandoserá
parecidacom:
$ vagrant up
Bringing machine ’db’ up with ’virtualbox’ provider...
Bringing machine ’web’ up with ’virtualbox’ provider...
Bringing machine ’monitor’ up with ’virtualbox’ provider...
==> db: Checking if box ’hashicorp/precise32’ is up to date...
==> db: VirtualBox VM is already running.
37

## Página 56

3.1. Instalandooservidordemonitoramento CasadoCódigo
==> web: Checking if box ’hashicorp/precise32’ is up to date...
==> web: VirtualBox VM is already running.
==> monitor: Importing base box ’hashicorp/precise32’...
==> monitor: Matching MAC address for NAT networking...
==> monitor: Checking if box ’hashicorp/precise32’ is
up to date...
==> monitor: Setting the name of the VM:
blank_monitor_1394851889588_2267
==> monitor: Fixed port collision for 22 => 2222.
Now on port 2201.
==> monitor: Clearing any previously set network interfaces...
==> monitor: Preparing network interfaces based on
configuration...
monitor: Adapter 1: nat
monitor: Adapter 2: hostonly
==> monitor: Forwarding ports...
monitor: 22 => 2201 (adapter 1)
==> monitor: Running ’pre-boot’ VM customizations...
==> monitor: Booting VM...
==> monitor: Waiting for machine to boot. This may take a few
minutes...
monitor: SSH address: 127.0.0.1:2201
monitor: SSH username: vagrant
monitor: SSH auth method: private key
monitor: Error: Connection timout. Retrying...
==> monitor: Machine booted and ready!
==> monitor: Configuring and enabling network interfaces...
==> monitor: Mounting shared folders...
monitor: /vagrant => /private/tmp/blank
Paracompletarainstalaçãobásica,precisamoslogarnoservidorusando
ocomando vagrant ssh monitor.Umavezlogado,ainstalaçãodoNa-
gioséfeitaatravésdopacote nagios3. Porém,antesdeinstalaroNagios,
precisamosconfigurarosistemaparausaraúltimaversão.Paraisto,precisa-
mosexecutarosseguintescomandos:
vagrant@monitor$ echo "Package: nagios*
> Pin: release n=raring
> Pin-Priority: 990" | sudo tee /etc/apt/preferences.d/nagios
38

## Página 57

CasadoCódigo Capítulo3. Monitoramento
Package: nagios*
Pin: release n=raring
Pin-Priority: 990
vagrant@monitor$ echo "deb http://archive.ubuntu.com/ubuntu \
> raring main" | sudo tee /etc/apt/sources.list.d/raring.list
deb http://archive.ubuntu.com/ubuntu raring main
vagrant@monitor$ sudo apt-get update
Ign http://archive.ubuntu.com raring InRelease
Ign http://security.ubuntu.com precise-security InRelease
...
Issoadicionaumanovaentradanalistadepacotescomo releasemais
novodoUbuntu–chamado“raring”–econfiguraaspreferênciasdoinsta-
ladordepacotesparadarprioridadeaonovo releasenospacotesdoNagios.
Ocomando apt-get updatefazcomqueoinstaladordepacotesatua-
lizeseu cacheparasaberdasnovasversõesdisponíveis. Umavezfeitoisso,
podemosinstalaronagiosatravésdocomando:
vagrant@monitor$ sudo apt-get install nagios3
Reading package lists... Done
Building dependency tree
...
ONagiospossuiumadependênciacomoPostfix,umprogramaUNIX
responsável por envio de e-mails. Por esse motivo, durante a instalação
irá aparecer uma tela rosa pedindo configurações para o Postfix. Esco-
lha Internet Sitepara seguir o processo de instalação e na próxima tela,
onde ele pede o nome do sistema para envio de e-mails, digite “moni-
tor.lojavirtualdevops.com.br”.
ApróximateladeconfiguraçãoédoNagios,evocêprecisaescolheruma
senhaparaousuárioadministrador“nagiosadmin”conseguiracessarain-
terfaceweb. Usaremosasenha“secret”. Apósestasconfigurações,opro-
cessodeinstalaçãodeveterminarevocêpodetestarseainstalaç ãofuncio-
nouabrindooseunavegadorwebevisitandooendere çohttp://nagiosadmin:
secret@192.168.33.14/nagios3.Casovocêtenhaescolhidooutrousuárioouse-
nha,modifiqueaURLcomosdadosdeacessocorretos. Setudodercerto,
vocêveráainterfacewebdeadministraçãodoNagios.Clicandonolink Ser-
vices,vocêveráumatelaparecidacomafigura 3.2.
39

## Página 58

3.1. Instalandooservidordemonitoramento CasadoCódigo
Figura3.2:InterfacedeadministraçãodoNagios
Comovocêpodeperceber,algumasverificaçõespadrão–ouserviços,na
terminologiadoNagios–jáestãopré-configuradas. Porenquanto,oservi-
dorestáapenasseautomonitorando,atuandotantocomosupervisorquanto
supervisionado.Nestatela,cadaservidormonitorado–ou host–possuium
conjuntodeserviços.OservidordoNagiosestárepresentadopelonome lo-
calhostecadalinhanatabelarepresentaumaverificaç ãoindependente. O
statusverde“OK”significaqueaverificaçãopassou,enquantoostatus“PEN-
DING”significaqueaverificaçãoaindanãorodou. Asverificaçõespadrão
são:
•Cargaatual:acargadeumsistemaUNIXmedeoquãoocupadaaCPU
está.Parasermaisexato,acargaéumamédiamóveldotamanhoda
filadeprocessosesperandoparaexecutar. QuandoaCPUcome çaa
sesobrecarregar,osprocessosprecisamesperarmaistempopararo-
dar,aumentandoafilaefazendoosistemarodarmaisdevagar. Esta
verificaçãoenviaumalertaquandoacargaatualultrapassaumcerto
limite.
•Usuáriosatuais: verificaquantosusuáriosestãologadosnosistema.
40

## Página 59

CasadoCódigo Capítulo3. Monitoramento
Essaéumamaneirasimplificadadedetectarintrusãonoservidoreen-
viaralertasquandoonúmerodeusuárioslogadosvaialémdoesperado.
•Espaçodedisco: quandoumservidorficasemespaçoemdisco,di-
versosproblemascome çamaaparecer.Umdosmotivosmaiscomuns
paraissoéageraçãodelogsemsistemasdeproduç ão.Paraevitareste
problemaéimportantemonitorarquantoespaçolivreaindaresta.Esta
verificaçãoenviaalertasquandooespaçolivreatingeumcertolimite.
•HTTP:verificaqueoservidorestáaceitandoconexõesHTTP.Neste
caso,oNagiosinstalouumservidorwebparaquepossamosacessara
interfacedeadministraçãodafigura 3.2. Porpadrão,estaverificação
enviaráalertascasonãoconsigaabrirumaconexãoHTTPnaporta80.
•SSH:verificaqueoservidorestáaceitandoconexõesSSHnaporta22e
enviaalertasquandoencontraalgumproblema.
•Númerototaldeprocessos:outraformadeavaliarseoservidorestá
sobrecarregadoéatravésdonúmerototaldeprocessos.Semuitospro-
cessosestiveremexecutandoaomesmotempo,osistemaoperacional
vaigastarmaistempogerenciandoqualpoderodarnaCPU,nãoso-
brandotemposuficienteparaquenenhumdelesrodeefetivamente.
Estaverificaçãoenviaalertasquandoonúmerototaldeprocessosul-
trapassaumcertolimite.
Aprimeiravista,podeparecerquesãomuitasverificaçõesparamonito-
rarumúnicoservidor. Noentanto,seguindoomesmoprincípiodeescre-
verpoucasasser çõesportestequandodesenvolvemoscódigousandoTDD,
verificaçõesmaisgranularesajudamaidentificaropontodefalhamaisra-
pidamentequandoalgumproblemaacontece. Emvezdereceberumalerta
genéricodizendoqueoservidorestácomproblemas,vocêvaiterinforma-
çõesespecíficasparaidentificaracausadoproblemamaisrapidamente.
Naspróximasse çõesdiscutiremosumpoucomaissobreosconceitoseas
configuraçõesdoNagioseaprenderemoscomosupervisionaroutrosservi-
dores,comoadicionarmaisverificaçõesecomoreceberalertasquandoalgo
dáerrado.
41

## Página 60

3.2. Monitorandooutrosservidores CasadoCódigo
3.2 Monitorando outros servidores
ComoNagiosinstaladoeefetuandoverificações,precisamosconfigurá-lo
paramonitorarnossosoutrosservidoresdeproduç ão.Paraistoprecisamos
declararondeestãoosoutrosservidoresequaisverificaçõesexecutar.Cria-
remosumnovoarquivoparadefinirtodasasconfiguraçõespertinentesàloja
virtual:
vagrant@monitor$ sudo nano /etc/nagios3/conf.d/loja_virtual.cfg
Nestearquivoiremosdeclararosservidoresdalojavirtual,definindono-
voshostscomosrespectivosendere çosIP:
define host {
use generic-host
host_name 192.168.33.10
hostgroups ssh-servers, debian-servers
}
define host {
use generic-host
host_name 192.168.33.12
hostgroups ssh-servers, debian-servers
}
Sempre que alteramos um arquivo de configuração, precisamos
recarregá-losparaqueoNagiosdetecteasmudan ças. Paraisto,usamoso
comando reload:
vagrant@monitor$ sudo service nagios3 reload
NoNagios,um hostrepresentaumdispositivoasermonitorado,como
porexemploumservidor,umroteadorouumaimpressora. Podemostam-
bémagruparhostssemelhantesem hostgroups edefinirconfiguraçõespara
diversosservidoresdeumavez,evitandoduplicação.Omesmo hostpodeser
membrodemaisdeum hostgroup.
Noarquivodeconfiguração /etc/nagios3/conf.d/loja_virtual.cfg,
definimos que os nossos servidores são membros de dois grupos:
42

## Página 61

CasadoCódigo Capítulo3. Monitoramento
ssh-servers e debian-servers. O grupo ssh-servers cria
umaverificaçãoparaoserviçoSSH.Ogrupo debian-serversnãodefine
nenhumaverificaçãoextra,masadicionainformaçõescomoologotipoda
DebianqueaparecenoíconedoservidornainterfacewebdoNagios.
Paraverificarqueasconfiguraçõesforamaplicadascomsucesso,você
poderecarregarapáginadeadministraçãoeesperaratéqueasnovasveri-
ficaçõesSSHestejamOK,conformemostraafigura 3.3.
Figura3.3:MonitorandoserviçoSSHemmaisservidores
Parafacilitaraconfiguração,iremosadicionarnossosservidoresadois
novoshostgroups:umgrupochamado web-serversparaosservidoresweb
eumgrupochamado db-serversparaosservidoresdebancodedados.
Faremosissoeditandoomesmoarquivodeconfiguraç ão:
vagrant@monitor$ sudo nano /etc/nagios3/conf.d/loja_virtual.cfg
Seráprecisoadicionarosnovos hostgroups emodificaraconfiguração
doshostsexistentesparaadicioná-losaosgruposcorretos:
define hostgroup {
hostgroup_name db-servers
alias Database Servers
43

## Página 62

3.3. ExplorandooscomandosdeverificaçãodoNagios CasadoCódigo
}
define hostgroup {
hostgroup_name web-servers
alias Web Servers
}
define host {
use generic-host
host_name 192.168.33.10
hostgroups ssh-servers, debian-servers, db-servers
}
define host {
use generic-host
host_name 192.168.33.12
hostgroups ssh-servers, debian-servers, web-servers
}
Apósrecarregaroarquivodeconfiguração–usandoomesmocomando
sudo service nagios3 reload–vocêpodeverificarqueosnovosgru-
posexistemclicandonolink HostGroupsnateladeadministraçãodoNagios.
Executardiversasverificaçõeseenviaralertasquandoalgoestáerradosão
asfuncionalidadesmaisimportantesdeumsistemademonitoramentocomo
oNagios.Napróximase ção,vamosconhecerosdiversostiposdechecagens
queestãodisponíveisparaverificarquealojavirtualestáfuncionandocorre-
tamente.
3.3 Explorando os comandos de verificação do
Nagios
CadaserviçodoNagiosestáassociadoaumcomandoqueéexecutadoem
cadaverificação.Ocomandonadamaisédoqueumscriptquepodeserexe-
cutadodiretamentedalinhadecomando.Diversoscomandosjávêminstala-
doscomoNagiosporpadrão,porémvocêpodecriarseusprópriosscriptsou
instalarpluginsdacomunidadeparaestendersuabibliotecadeverificações.
44

## Página 63

CasadoCódigo Capítulo3. Monitoramento
Vamosexploraralgunsdoscomandospré-instalados,queestãodisponí-
veisnodiretório /usr/lib/nagios/plugins.Porexemplo,ocomando
check_ssh,queéexecutadonaverificaçãodoserviçoSSH:
vagrant@monitor$ cd /usr/lib/nagios/plugins
vagrant@monitor$ ./check_ssh 192.168.33.12
SSH OK - OpenSSH_5.9p1 Debian-5ubuntu1 (protocol 2.0)
vagrant@monitor$ echo $?
0
vagrant@monitor$ ./check_ssh 192.168.33.11
No route to host
vagrant@monitor$ echo $?
2
Percebaqueaorodarocomando check_sshpassandooendere çoIPdo
servidorweb,eleimprimeumamensagemcomumresumodeumalinhado
queaconteceu. Essamensagemgeralmenteédaforma <VERIFICAÇÃO>
<STATUS>-<MENSAGEMCOMDETALHES>,porémoquedefineore-
sultadodaverificaçãonãoéoformatodamensagem,massim,ocódigode
saídadoprocesso–ouexitcode,representadopelavariável $?nobash:
•0–OK:indicaqueaverificaçãopassoucomsucesso. Representado
pelostatusverdenainterfaceweb.
•1–WARNING:indicaqueaverificaçãopassouoprimeirolimitede
alerta.Representadopelostatusamarelonainterfaceweb.
•2–CRITICAL:indicaqueaverificaçãofalhouealgoestáerrado.Re-
presentadopelostatusvermelhonainterfaceweb.
•3–UNKNOWN:indicaqueaverificaçãonãoconseguiudecidirseo
serviçoestábemounão.Representadopelostatuslaranjanainterface
web.
Outraverificaçãoquepodemosfazeréqueconseguimosacessaroservi-
dorwebporHTTP:
vagrant@monitor$ ./check_http -H 192.168.33.12
Connection refused
45

## Página 64

3.3. ExplorandooscomandosdeverificaçãodoNagios CasadoCódigo
HTTP CRITICAL - Unable to open TCP socket
vagrant@monitor$ echo $?
2
vagrant@monitor$ ./check_http -H 192.168.33.12 -p 8080
HTTP OK: HTTP/1.1 200 OK - 2134 bytes in 0.007 second response
time ...
vagrant@monitor$ echo $?
0
Percebaqueprecisamospassaraop ção -Hparaindicarqual hostdeve
serverificado.Alémdisso,comonãoespecificamosaportaaserverificada,
ocomando check_httpusaaporta80porpadrão.Aopassarmosaop ção
-pcomovalor8080–aportaondeoservidorTomcatestáescutando–a
verificaçãopassacomsucesso.
Umúltimocomandoparaexplorarmoséaverificaçãodequantoespaço
emdiscoaindaestádisponível:
vagrant@monitor$ ./check_disk -H 192.168.33.12 -w 10% -c 5%
/usr/lib/nagios/plugins/check_disk: invalid option -- ’H’
Unknown argument
Usage:
check_disk -w limit -c limit [-W limit] [-K limit] ...
vagrant@monitor$ ./check_disk -w 10% -c 5%
DISK OK - free space: / 74473 MB (97% inode=99%); ...
Perceba que, ao contrário do comandocheck_http, o comando
check_disknãoaceitaaop ção -Heconsegueapenasverificarquantoes-
paçoemdiscoestádisponívelnoservidorlocal.Issoacontecepoisoserviço
HTTPéumserviçoderedeacessívelremotamente. Poroutrolado,oco-
mando check_diskprecisadeinformaçõeslocaisdoservidorparadeci-
dirquantoespaçodediscoestádisponívelenãopodeserexecutadoremota-
mente.
ONagiospossuitrêsopçõesquandovocêprecisarealizarumaverificação
remotadeumserviçoquenãoestádisponívelnarede:
•ChecagemporSSH:atravésdocomando check_by_ssh,oNagios
consegueabrirumaconexãoSSHcomoservidorremotoeexecutaro
46

## Página 65

CasadoCódigo Capítulo3. Monitoramento
comandolá.Estaéumaop çãosimplespoisnãoexigeainstalaç ãode
nenhumagentenoservidorsupervisionado. Noentanto,conformeo
númerodeverificaçõesremotasaumenta,issopodeaumentaracarga
noservidorsupervisor,poiseleprecisarácriaredestruirdiversasco-
nexõesSSH.
•ChecagemativacomNRPE:o Nagios Remote Plugin Executor, ou
NRPE,éumpluginquepermiteaexecuç ãodeverificaçõesquede-
pendemderecursoslocaisnoservidorsupervisionado. Umprocesso
agentedoNRPErodanoservidorsupervisionadoeficaesperandope-
didosdeverificaçãodosupervisor.QuandooNagiosprecisaexecutar
umaverificação,elepedeparaoagenteNRPErodá-laecoletaosresul-
tadosquandoaverificaçãotermina.Estetipodeverificaçãoéativapois
queminiciaopedidodeexecuçãodocomandoéoservidorsupervisor.
•ChecagempassivacomNSCA:o NagiosServiceCheckAcceptor,ou
NSCA,éumpluginquepermiteaexecuç ãodeverificaçõesremotas
deformapassivanoservidorsupervisionado.Umprocessoclientedo
NSCArodanoservidorsupervisionadoeexecutaasverificaçõesperi-
odicamente,enviandoosresultadosparaumservidorNSCAqueroda
nosupervisor.Estetipodeverificaçãoépassivapoisqueminiciaaexe-
cuçãodocomandoéopróprioservidorsupervisionado.
Afigura 3.4mostraasdiferentesformasderealizarverificaçõescomo
Nagios.Verificaçõesdeserviçosderede,como check_httprodamdireto
doservidorsupervisor. Verificaçõesqueprecisamrodarnoservidorsuper-
visionado,podemserchamadasativamentecom check_by_sshouatravés
dopluginNRPE.Porfim,verificaçõespassivaspodemrodardeformainde-
pendentenoservidorsupervisionadoeosresultadosenviadosparaoNagios
atravésdopluginNSCA.
47

## Página 66

3.4. Adicionandoverificaçõesmaisespecíficas CasadoCódigo
Figura3.4:VerificaçõesremotascomNagios
AgoraquejáconhecemososdiferentestiposdeverificaçõesdoNagiose
sabemoscomoexecutarseusdiferentescomandos,vamostornaromonito-
ramentodainfraestruturadalojavirtualmaisrobusto.
3.4 Adicionando verificações mais específicas
Alémdasverificaçõespadrão,vocêpodedeclararseusprópriosserviçose
associá-losaumúnico hostouaumgrupode hosts. Nainfraestruturada
lojavirtual,oservidordebancodedadosestárodandooMySQLcomoum
serviçoderede.Podemosverificarqueoserviçoestádisponíveladicionando
umaverificaçãoassociadaaogrupo db-serversnofinaldoarquivodecon-
figuração /etc/nagios3/conf.d/loja_virtual.cfg:
define hostgroup ...
define host ...
define service {
service_description MySQL
use generic-service
hostgroup_name db-servers
check_command check_tcp!3306
}
ApósrecarregaroNagioseesperarpelapróximaexecuç ãodaverificação,
umnovoserviço“MySQL”aparecerácomostatusOK.Estaverificaçãousao
comando check_tcpquetentaabrirumaconexãoTCPnaportaespecifi-
cada–nessecasoaportaondeoMySQLrodaé3306. AsintaxedoNagios
parapassarargumentosparaumcomandoésepará-loscomumpontode
exclamação( !).
48

## Página 67

CasadoCódigo Capítulo3. Monitoramento
Estaverificaçãogarantequeexistealgumprocessoaceitandoconexões
TCP na porta 3306, porém não garante que tal processo seja o MySQL.
Para verificar que o banco de dados realmente está lá, é preciso usar
umoutrocomando check_mysql, jáinstaladonodiretóriodeplugins
/usr/lib/nagios/plugins. Executandodiretamentedalinhadeco-
mando,podemosverquaisargumentoseleaceita:
vagrant@monitor$ /usr/lib/nagios/plugins/check_mysql --help
...
Usage:
check_mysql [-d database] [-H host] [-P port] [-s socket]
[-u user] [-p password] [-S]
...
Vamosentãoadicionarumanovaverificaçãonoarquivodeconfiguração
dalojavirtual:
define hostgroup ...
define host ...
define service ...
define service {
service_description MySQL-lojavirtual
use generic-service
hostgroup_name db-servers
check_command check_mysql_database!loja!lojasecret
!loja_schema
}
Você deve ter percebido que o comando executado na linha de co-
mandosechama check_mysql,porémocomandoqueusamosparade-
clararoserviçosechama check_mysql_database. Issoacontecepois
os comandos precisam ser declarados dentro do Nagios antes de serem
usadosporumserviço. Nessecaso, opluginjádefiniuoscomandosdo
Nagios e podemos ver suas declarações olhando o conteúdo do arquivo
/etc/nagios-plugins/config/mysql.cfg:
vagrant@monitor$ cat /etc/nagios-plugins/config/mysql.cfg
define command{
49

## Página 68

3.4. Adicionandoverificaçõesmaisespecíficas CasadoCódigo
command_name check_mysql
command_line /usr/lib/nagios/plugins/check_mysql -H
’$HOSTADDRESS$’
}
...
define command{
command_name check_mysql_database
command_line /usr/lib/nagios/plugins/check_mysql -d ’$ARG3$’
-H ...
}
...
Oúltimocomandopermitepassarargumentosparaonomedeusuário,
senhaequalbancodedadosqueremosverificar.Podemosvertambémaor-
dememqueosargumentosdevemserpassadosquandodeclaramosnosso
serviço:oNagiossubstituiostokens $ARG1$, $ARG2$, $ARG3$pelosva-
loresseparadospelopontodeexclamaçãonarespectivaordem.
Agoraquetemosnossobancodedadosmonitorado,éhoradeadicio-
naralgumasverificaçõesparaosservidoresweb.Seguindoomesmoraciocí-
niodeantes,osserviçosderedeexpostospeloservidorwebsãoasconexões
HTTPeHTTPSdoTomcat. Ocomandoquepodemosusarpararealizar
taisverificaçõeséo check_http,tambéminstaladonodiretóriodeplu-
gins /usr/lib/nagios/plugins. Executandodiretamentedalinhade
comando,podemosverquaisargumentoseleaceita:
vagrant@monitor$ /usr/lib/nagios/plugins/check_http --help
...
Usage:
check_http -H <vhost> | -I <IP-address> [-u <uri>] [-p <port>]
[-w <warn time>] [-c <critical time>] [-t <timeout>] [-L]
[-a auth] [-b proxy_auth]
[-f <ok|warning|critcal|follow|sticky|stickyport>]
[-e <expect>] [-s string] [-l]
[-r <regex> | -R <ignorecase regex>]
[-P string] [-m <min_pg_size>:<max_pg_size>] [-4|-6] [-N]
50

## Página 69

CasadoCódigo Capítulo3. Monitoramento
[-M <age>] [-A string] [-k string] [-S <version>] [--sni]
[-C <warn_age>[,<crit_age>]] [-T <content-type>] [-j method]
NOTE: One or both of -H and -I must be specified
...
Nessecaso, apesardopluginjádeclararalgunscomandosdoNagios
noarquivo /etc/nagios-plugins/config/http.cfg,nenhumdeles
aceitaoargumento -pparapassaraporta. Comootomcatnãoestáro-
dandonaportaHTTPpadrão(80),antesdeassociarmosumnovoserviçoao
grupodeservidores web-serversprecisamosdeclararnossosprópriosco-
mandos.Faremosissonoarquivodeconfiguraçãodalojavirtual(lembrando
queabarrainvertidaindicaapenasqueocomandodeveserdefinidotodona
mesmalinha):
define hostgroup ...
define host ...
define service ...
define service ...
define command {
command_name check_tomcat_http
command_line /usr/lib/nagios/plugins/check_http -H
’$HOSTADDRESS$’ \ -p ’$ARG1$’ -u ’$ARG2$’ -e ’HTTP/1.1 200 OK’
}
define service {
service_description Tomcat
use generic-service
hostgroup_name web-servers
check_command check_tomcat_http!8080!’/devopsnapratica/’
}
Oargumento -Hrepresentaoendere çodohostmonitorado,oprimeiro
argumentorepresentaaportadaverificaçãoHTTPeosegundoargumentoé
aURI.Nossocomandotambémpassaaop ção -eparagarantirquearesposta
doservidoréumstatusdesucesso: HTTP/1.1 200 OK.
Porfim,vamosadicionarumaúltimaverificaçãoparagarantirqueaco-
nexãoSSLtambémfuncionanaporta8443doTomcat:
51

## Página 70

3.4. Adicionandoverificaçõesmaisespecíficas CasadoCódigo
define hostgroup ...
define host ...
define service ...
define service ...
define command ...
define service ...
define command {
command_name check_tomcat_https
command_line /usr/lib/nagios/plugins/check_http -H
’$HOSTADDRESS$’ \ --ssl=3 -p ’$ARG1$’ -u ’$ARG2$’ -e
’HTTP/1.1 200 OK’
}
define service {
service_description Tomcat SSL
use generic-service
hostgroup_name web-servers
check_command check_tomcat_https!8443!’/devopsnapratica/
admin/’
}
ApósrecarregaraconfiguraçãodoNagioseesperarpelaexecuç ãodas
novasverificações,ateladeserviçosnainterfacedeadministraçãodeveestar
parecidacomafigura 3.5.
52

## Página 71

CasadoCódigo Capítulo3. Monitoramento
Figura3.5:Todasasverificaçõesdalojavirtual
Oarquivodeconfiguração /etc/nagios3/conf.d/loja_virtual.cfg
completo,aofinaldestase çãoficaráassim:
define hostgroup {
hostgroup_name db-servers
alias Database Servers
}
define hostgroup {
hostgroup_name web-servers
alias Web Servers
}
define host {
use generic-host
host_name 192.168.33.10
hostgroups ssh-servers, debian-servers, db-servers
}
define host {
use generic-host
host_name 192.168.33.12
53

## Página 72

3.4. Adicionandoverificaçõesmaisespecíficas CasadoCódigo
hostgroups ssh-servers, debian-servers, web-servers
}
define service {
service_description MySQL
use generic-service
hostgroup_name db-servers
check_command check_tcp!3306
}
define service {
service_description MySQL-lojavirtual
use generic-service
hostgroup_name db-servers
check_command check_mysql_database!loja!lojasecret
!loja_schema
}
define command {
command_name check_tomcat_http
command_line /usr/lib/nagios/plugins/check_http -H
’$HOSTADDRESS$’ \ -p ’$ARG1$’ -u ’$ARG2$’ -e ’HTTP/1.1 200 OK’
}
define service {
service_description Tomcat
use generic-service
hostgroup_name web-servers
check_command check_tomcat_http!8080!’/devopsnapratica/’
}
define command {
command_name check_tomcat_https
command_line /usr/lib/nagios/plugins/check_http -H
’$HOSTADDRESS$’ \ --ssl=3 -p ’$ARG1$’ -u ’$ARG2$’ -e
’HTTP/1.1 200 OK’
}
define service {
54

## Página 73

CasadoCódigo Capítulo3. Monitoramento
service_description Tomcat SSL
use generic-service
hostgroup_name web-servers
check_command check_tomcat_https!8443!’/devopsnapratica/
admin/’
}
Agoraquetemosverificaçõesmaisdetalhadassobreofuncionamentoda
lojavirtual,aúltimacoisaqueprecisamosconfigurarparaterumsistemade
monitoramentorobustoéorecebimentodealertas.
3.5 Recebendo alertas
Terverificaçõesdetalhadasdoseusistemaéapenasoprimeiropassopara
construirumsistemademonitoramentorobusto.Nãoadiantanadaseusis-
temademonitoramentodetectarumproblemasevocênãopuderseravisado.
Porisso,éimportanteconfigurarmosalertasparareceberinformaçõessobre
problemasoquantoantespossível.
ExistemváriospluginsdoNagiosparaenviaralertasdediversasmanei-
ras:e-mail,pager,mensagemSMS,sistemasdechatcomoMSN,ICQ,Yahoo,
ouqualquercoisaquevocêpuderfazerdalinhadecomando. Vocêpode
inclusivedefinirseuprópriocomandoparaescolhercomooNagiosenviará
alertas. Porpadrão,oNagiosjávemconfiguradocomdoiscomandospara
enviaralertaspore-mail:umdelesnotificaqueo hostestácomproblemase
ooutronotificaquealgumserviçoestácomproblemas.Podemosveradefi-
niçãodessescomandosnoarquivo /etc/nagios3/commands.cfg:
vagrant@monitor$ cat /etc/nagios3/commands.cfg
...
define command {
command_name notify-host-by-email
command_line /usr/bin/printf "%b" ... | /usr/bin/mail -s ...
}
define command {
command_name notify-service-by-email
command_line /usr/bin/printf "%b" ... | /usr/bin/mail -s ...
55

## Página 74

3.5. Recebendoalertas CasadoCódigo
}
...
Alémdessescomandos,existemmaisdoisobjetosdoNagiosquepo-
demserconfiguradosparadecidirquemrecebeosalertasequando: con-
tatoseperíodosdetempo – outime periods. Períodos de tempo de-
finem quando alertas podem ser enviados e estão definidos no arquivo
/etc/nagios3/conf.d/timeperiods_nagios2.cfg.Olhandoocon-
teúdodoarquivopodemosverasdiferentesop ções,inclusiveofamosope-
ríododesuporte24x7–24horaspordia,7diasporsemana:
vagrant@monitor$ cat /etc/nagios3/conf.d/timeperiods_nagios2.cfg
...
define timeperiod {
timeperiod_name 24x7
alias 24 Hours A Day, 7 Days A Week
sunday 00:00-24:00
monday 00:00-24:00
tuesday 00:00-24:00
wednesday 00:00-24:00
thursday 00:00-24:00
friday 00:00-24:00
saturday 00:00-24:00
}
...
Contatossãoaspessoasquerecebemalertas. Nonossocaso, usare-
mosoúnicocontatodefinidonoNagiosparaousuário root,noarquivo
/etc/nagios3/conf.d/contacts_nagios2.cfg:
vagrant@monitor$ cat /etc/nagios3/conf.d/contacts_nagios2.cfg
...
define contact {
contact_name root
alias Root
service_notification_period 24x7
host_notification_period 24x7
service_notification_options w,u,c,r
host_notification_options d,r
56

## Página 75

CasadoCódigo Capítulo3. Monitoramento
service_notification_commands notify-service-by-email
host_notification_commands notify-host-by-email
email root@localhost
}
...
Nadefiniçãodocontatovocêescolheoperíodoemqueocontatoestará
emalerta,seuendere çodee-mail,oscomandosexecutadosparaenviaraler-
taseasop çõesdenotificação.Nestecaso,seremosnotificadosquandoo host
estiverindisponível( dparadown)ourecuperado( rpararecovery)equando
serviçosentrarememstatusdealerta( wparawarning),desconhecido( u
paraunkown),crítico( cparacritical)ourecuperado( rpararecovery). O
Nagiostambémsuportaconfiguraçõesparagruposdecontatosquandovocê
queralertarumtimeinteiroaoinvésdeumaúnicapessoa.Noentanto,não
precisaremosusarestafuncionalidadenestecapítulo.
Paragarantirquenossainfraestruturaconsigaenviaralertasdeverdade,
precisamosescolherqualserviçodemensagensseráusadopeloNagios.Ape-
sardeninguémgostardeseracordadodemadrugada,timesdeoperações
precisamdarsuporte24x7paraseussistemaseportantopreferemsernotifi-
cadosporpagerouSMS.Noentanto,édifícilencontraralgumserviçográtis
paraenviodeSMS,especialmenteparaoperadorasbrasileiras.Algumasop-
çõesdeserviçosonlinepagoscomcoberturaSMSinternacionalsãoo Twilio
(http://www.twilio.com/)eo Nexmo(http://www.nexmo.com/).
Outroserviçoonlinepagobastanteusadoéo PagerDuty(http://www.
pagerduty.com/)porpermitirgerenciargrupos,contatos,agendadequem
estáon-calleformasdeenviodealertasnumúnicolugar,independentedo
Nagios.OPagerDutysuportaenviodeSMS,e-mail,ouaténotificaçõespara
iPhoneouAndroid.Antesdecome çarapagarpeloplanomensal,épossível
criarumacontadetesteválidapor30diaseoPagerDutypossuiumapágina
bemdetalhadaexplicandocomointegrá-locomoNagios.
Nonossocaso,paraevitarumadependênciaemumsistemaexternopago,
vamosusaraconfiguraçãopadrãodoNagiosdeenviodealertaspore-mail.
AúnicaconfiguraçãonecessáriaécriarumcontatonoNagiosparareceber
osalertasdalojavirtual.Faremosissoeditandooarquivodeconfiguraç ãode
contatos /etc/nagios3/conf.d/contacts_nagios2.cfg,trocandoo
57

## Página 76

3.5. Recebendoalertas CasadoCódigo
endereçodee-mailroot@localhostpeloseuendere çodee-maildever-
dade:
...
define contact {
contact_name root
...
email <seu_email>@gmail.com
}
...
Paraqueestaconfiguraçãotenhaefeito,precisamosrecarregaroserviço
doNagiospelaúltimavez:
vagrant@monitor$ sudo service nagios3 reload
* Reloading nagios3 monitoring daemon configuration files
nagios3 ...done.
Apartirdeagora,qualqueralertaseráenviadodiretamenteparaoseue-
mail.Paratestarqueoenviodealertasestáfuncionandocorretamente,você
podepararoserviçoSSHeesperaraexecuç ãodaspróximasverificaçõesdo
Nagios:
vagrant@monitor$ sudo service ssh stop
ssh stop/waiting
ONagiosirátentarexecutaraverificaçãoquatrovezesantesdedeclarar
oserviçoindisponível.Assimqueoserviçoaparecercomstatusvermelhona
teladeadministraçãodoNagioseonúmerodetentativasalcan çar“4/4”,você
deveráreceberumalertapore-mail.Paraquetudovolteaonormal,reinicie
oserviçoSSH:
vagrant@monitor$ sudo service ssh start
ssh start/running, process 3424
AssimqueoNagiosdetectarqueoservi çovoltouaonormal,vocêrece-
beráume-mailavisandoqueoserviçoestárecuperado.
58

## Página 77

CasadoCódigo Capítulo3. Monitoramento
3.6 Um problema atinge produção , e agora?
Agoraquetemosumsistemademonitoramentoconfiguradoparaexecutar
verificaçõeseenviaralertassobreeventuaisproblemasnainfraestruturada
lojavirtual,podemossimularumcenáriodefalhadeumdosservidores.Essa
tambéméumaboamaneiradetestarseosistemademonitoramentoestá
funcionandocorretamente.
Vamosimaginarquenossoservidordebancodedadostenhasofridoum
problemadehardwareeparoudefuncionar.Paraisto,bastasairdamáquina
virtualdemonitoramentoexecutandoocomando logoutousimplesmente
digitando CTRL-DepedirparaoVagrantdestruiramáquinavirtualdobanco
dedados:
vagrant@monitor$ logout
Connection to 127.0.0.1 closed.
$ vagrant destroy db
db: Are you sure you want to destroy the ’db’ VM? [y/N] y
==> db: Forcing shutdown of VM...
==> db: Destroying VM and associated drives...
Dentrodealgunsminutos,osistemademonitoramentoirádetectarqueo
servidorestáindisponíveleenviaráumalerta.Apartirdestemomento,usuá-
riosnãoconseguemmaisacessaralojavirtualparaefetuarcompras.Sendoo
engenheiroresponsávelpelaoperaçãoemprodução,vocêrecebeanotificação
erespondeprontamenteparaconfirmarafalhaeagoravocêprecisarestituir
oserviço.
OlhandooconsoledoNagios,vocêveráalgoparecidocomafigura 3.6.
Ohostdobancodedadosetodososseusserviçosestãovermelhos,poréma
verificaçãodoserviçoHTTPnoservidorwebtambémfalha,indicandoque
oproblemadobancodedadosestáafetandoalojavirtual.
59

## Página 78

3.6. Umproblemaatingeprodução,eagora? CasadoCódigo
Figura3.6:Verificaçõesfalhandoquandoumproblemaatingeprodução
Paraquetudovolteaonormal,vocêprecisaráreinstalaroservidorde
bancodedados.Noentanto,fizemosistodeformamanualnocapítulo 2.Re-
petirtodosaquelespassosmanualmentelevarámuitotempoe,emmomentos
decrisecomoeste,tempoéumrecursoescasso.Seráquenãoexisteumama-
neiramelhordeinstalareconfiguraressesservidores?
60

## Página 79

Capítulo4
Infraestruturacomocódigo
Administradoresdesistemaaprendemopoderdalinhadecomandodesde
cedoepassamboapartedodianoterminalcontrolandoainfraestruturada
suaempresa.Écomumdizerqueelesestãoalterandoa configuraçãodosis-
tema. Sejainstalandonovosservidores,instalandonovosoftware,fazendo
upgradedesoftwareexistente,editandoarquivosdeconfiguração,reiniciando
processos,lendoarquivosdelog,efetuandoerestaurando backups,criando
novascontasdeusuário,gerenciandopermissões,ajudandodesenvolvedores
ainvestigaralgumproblemaouescrevendo scriptsparaautomatizartarefas
repetíveis.
Cadaumadessastarefasalteraligeiramenteoestadodoservidorepode
potencialmentecausarproblemasseamudan çanãoforexecutadacorreta-
mente.Éporissoquemuitosadministradoresdesistemanãodãoacessoaos
servidoresdeproduçãoparadesenvolvedores:paraevitarmudan çasindese-
jáveisepelafaltadeconfian ça.Noentanto,emmuitasempresas,essastarefas

## Página 80

4.1. Provisionamento,configuraçãooudeploy? CasadoCódigo
sãoexecutadasmanualmentenosservidoresdeproduç ãopelosprópriosad-
ministradoresdesistemaeelestambémpodemcometererros.
UmdosprincipaisprincípiosdeDevOpséinvestiremautomaç ão.Auto-
maçãopermiteexecutartarefasmaisrapidamenteediminuiapossibilidade
deerroshumanos. Umprocessoautomatizadoémaisconfiávelepodeser
auditoradocommaisfacilidade.Conformeonúmerodeservidoresquepre-
cisamseradministradosaumenta,processosautomatizadossetornamessen-
ciais.Algunsadministradoresdesistemaescrevemseuspróprios scriptspara
automatizarastarefasmaiscomuns.Oproblemaéquecadaumescrevesua
própriaversãodos scriptseficadifícilreutilizá-losemoutrassituações.Por
outrolado,desenvolvedoressãobonsemescrevercódigomodularizadoereu-
tilizável.
Comoavan çodaculturaDevOpseoaumentodacolaboraçãoentread-
ministradoresdesistemaedesenvolvedores,diversasferramentastêmevo-
luídoparatentarpadronizarogerenciamentoautomatizadodeinfraestru-
tura. Taisferramentaspermitemtratarinfraestruturadamesmaformaque
tratamoscódigo:usandocontroledeversões,realizandotestes,empacotando
edistribuindomóduloscomunse,obviamente,executandoasmudan çasde
configuraçãonoservidor.
Essapráticaéconhecidacomoinfraestruturacomocódigo enospermi-
tiráresolveroproblemaqueencontramosnofinaldocapítulo 3.Emvezde
reinstalartudomanualmente,vamosusarumaferramentadegerenciamento
deconfiguraçõesparaautomatizaroprocessodeprovisionamento,configu-
raçãoe deploydalojavirtual.
4.1 Provisionamento , configuração ou deploy?
Aocomprarumlaptopouumcelularnovo,vocêsóprecisaligá-loeelejá
estáprontoparauso.Emvezdemandaraspe çasindividuaiseummanualde
comomontarsuamáquina,ofabricantejáfeztodootrabalhonecessáriopara
quevocêusufruaseunovoaparelhosemmaioresproblemas.Comousuário,
vocêsóprecisainstalarprogramaserestaurarseusarquivosparaconsiderar
amáquinasua.Esseprocessodepreparaçãoparaousuáriofinaléconhecido
comoprovisionamento.
62

## Página 81

CasadoCódigo Capítulo4. Infraestruturacomocódigo
Otermo provisionamentoécomumenteusadoporempresasdeteleco-
municaçõeseporequipesdeoperaçõesparasereferiràsetapasdepreparação
iniciaisdeconfigura çãodeumnovorecurso:provisionarumaparelhocelu-
lar,provisionaracessoàinternet,provisionarumservidor,provisionaruma
novacontadeusuário,eassimpordiante. Provisionarumaparelhocelular
envolve,entreoutrascoisas: alocarumanovalinha,configurarosequipa-
mentosderedequepermitemcompletarligações,configurarserviçosextra
comoSMSoue-maile,porfim,associartudoissocomochipqueestánoseu
celular.
Nocasodeservidores,oprocessodeprovisionamentovariadeempresa
paraempresadependendodainfraestruturaedadivisãoderesponsabilida-
desentreasequipes.Seaempresapossuiinfraestruturaprópria,oprocesso
deprovisionamentoenvolveacompraeinstalaçãofísicadonovoservidorno
seudatacenter.Seaempresapossuiumainfraestruturavirtualizada,opro-
cessodeprovisionamentosóprecisaalocarumanovamáquinavirtualparao
servidor.Damesmaforma,seaequipedeoperaçõesconsideraraequipede
desenvolvimentocomo“usuáriofinal”,oprocessodeprovisionamentoacaba
quandooservidorestáacessívelnarede,mesmoseaaplicaç ãoemsiainda
nãoestiverrodando.Seconsiderarmososverdadeirosusuárioscomo“usuá-
riosfinais”,entãooprocessodeprovisionamentosóacabaquandooservidor
eaaplicaçãoestiveremrodandoeacessíveisnarede.
Paraevitarmaiorconfusãoemanterintegridadenodecorrerdolivro,
valeapenaolharparaoprocessodepontaapontaedefinirumaterminolo-
giaadequada.Imaginandoocenáriomaislongodeumaempresaquepossui
infraestruturaprópriaporémnãotemservidoressobrandoparauso,asetapas
necessáriasparacolocarumanovaaplicaçãonoarseriam:
1)Compradehardware:emempresasgrandesessaetapainiciaumprocesso
deaquisição,queenvolvediversasjustificaçõeseaprovaçõespoisinvestir
dinheiroemhardwareinfluinacontabilidadeenoplanejamentofinan-
ceirodaempresa.
2) Instalaçãofísicadohardware:essaetapaenvolvemontaronovoservidor
numracknodatacenter,assimcomoinstalaçãodecabosdefor ça,derede
etc.
63

## Página 82

4.1. Provisionamento,configuraçãooudeploy? CasadoCódigo
3)Instalaçãoeconfiguraç ãodosistemaoperacional: umavezqueoser-
vidoréligado, éprecisoinstalarumsistemaoperacionaleconfigurar
ositemsbásicosdehardwarecomo: interfacesderede,armazenamento
(disco,partições,volumesemrede),autenticaçãoeautorizaçãodeusuá-
rios,senhade root,repositóriodepacotesetc.
4) Instalaçãoeconfiguraç ãodeservi çoscomuns:alémdasconfigurações
basedosistemaoperacional,muitosservidoresprecisamconfigurarser-
viçosdeinfraestruturabásicoscomo:DNS,NTP,SSH,coletaerotaçãode
logs,backups,firewall,impressãoetc.
5)Instalaçãoeconfiguraçãodaaplicação:porfim,éprecisoinstalareconfi-
gurartudoquefaráesteservidorserdiferentedosoutros:componentesde
middleware,aaplicaçãoemsi,assimcomoconfiguraçõesdomiddleware
edaaplicação.
Nodecorrerdolivro,usaremosotermo provisionamentoparasereferir
aoprocessoqueenvolveasetapas1-4,ouseja,todasasatividadesnecessárias
paraqueoservidorpossaserusadoeindependentedarazãopelaqualele
foirequisitado. Usaremosotermo deploy,ouoequivalenteemportuguês
implantação,quandonosreferirmosàetapa5.Apesardo deployprecisarde
umservidorprovisionado,ociclodevidadoservidorédiferentedaaplica ção.
Omesmoservidorpodeserusadoporváriasaplicaçõesecadaaplicaçãopode
efetuardeploydezenasouatécentenasdevezes,enquantooprovisionamento
denovosservidoresacontececommenosfrequência.
Nopiorcaso,oprocessodeprovisionamentopodedemorarsemanasou
atémesesdependendodaempresa.Poressemotivo,écomumverequipesde
desenvolvimentodefinindocombastanteantecedênciaosrequisitosdehard-
wareparaseusambientesdeproduçãoeiniciandoesseprocessocomaequipe
deoperaçõesnasetapasiniciaisdoprojeto,paraevitaratrasosquandoaapli-
caçãoestiverprontaparairaoar. Algumacolaboraç ãopodeacontecerno
começodoprocesso,porémamaiorpartedotempoasduasequipestraba-
lhamemparalelosemsaberoqueaoutraestáfazendo.
Piorainda,muitasdessasdecisõesarquiteturaiscruciaissobreaquanti-
dadedeservidores,configuraçõesdehardwareouescolhadosistemaope-
racionalsãotomadasnocome çodoprojeto,nomomentoemquesetema
64

## Página 83

CasadoCódigo Capítulo4. Infraestruturacomocódigo
menorquantidadedeinforma çãoeconhecimentosobreasreaisnecessida-
desdosistema.
UmdosaspectosmaisimportantesdaculturaDevOpséreconheceresse
conflitodeobjetivosecriarumambientedecolaboraç ãoentreasequipesde
desenvolvimentoedeoperações. Ocompartilhamentodepráticaseferra-
mentaspermitequeaarquiteturaseadapteeevoluaconformeasequipes
aprendemmaissobreosistemarodandonomundoreal:emproduç ão.Esta
visãoholísticatambémajudaaencontrarsoluçõesquesimplifiquemopro-
cessodecompraeprovisionamento,removendoetapasouutilizandoauto-
maçãoparafazercomqueelasaconte çammaisrápido.
Umbomexemplodessasimplificaçãodoprocessoéousodetecnologias
comovirtualizaçãodehardwareecomputaçãoemnuvem–tambémconhe-
cidapelotermoeminglês cloudcomputingousimplesmentecloud.Provedo-
resdeserviçoclouddepontapermitemquevocêtenhaumnovoservidorno
aremquestãodeminutosatravésdeumsimplescliquedebotãoouchamada
deAPI!
4.2 Ferramentas de gerenciamento de configu-
ração
Nase çãoanterior,explicamosadiferen çaentreprovisionamentoe deploy.
Comexceçãodositems1e2queenvolvemcompraeinstalaç ãofísicadehard-
ware,asoutrastrêsetapasenvolvemalgumtipodeconfiguraç ãodosistema:
sejadosistemaoperacionalemsi,dosoftwarebaseinstaladonamáquinaou
daaplicaçãoquerodaemcimadele.Afigura 4.1mostraasdiferentesetapas
dociclodevidadeumservidoreogerenciamentodeconfiguraç ãoatual.
Figura4.1:Escopodogerenciamentodeconfiguração
65

## Página 84

4.2. Ferramentasdegerenciamentodeconfiguração CasadoCódigo
Existemdiversasferramentasparagerenciamentodeconfiguraç ão: shell
scripts(alinhadecomandotambéméconhecidacomo shell),Puppet(http:
//www.puppetlabs.com/puppet/), Chef (http://www.opscode.com/chef/),
Ansible (http://www.ansibleworks.com/tech/) ,Salt (http://saltstack.com/
community) ,Pallet (http://palletops.com/) eCFEngine (http://cfengine.
com/)sãoalgumasdasmaispopulares.
Amaioriadessasferramentaspossuiumaempresaresponsávelpeloseu
desenvolvimentoepelocrescimentodacomunidadeeecossistemaaoseure-
dor.Todaselasestãocontribuindoparaaevoluç ãodacomunidadeDevOpse,
apesardecompetirementresi,seumaioradversárioaindaéafaltadeusode
ferramentas.Porincrívelquepare ça,amaioriadasempresasaindagerenciam
seusservidoresdeformamanualoupossuem scriptsproprietáriosescritoshá
tantotempoqueninguémconseguedarmanuten ção.
Agrandediferen çaentre shellscripts proprietárioseasoutrasferramen-
taséquegeralmenteo scriptsófuncionaparainstalareconfiguraroservidor
pelaprimeiravez.Eleservecomodocumentaç ãoexecutáveldospassosexe-
cutadosnaprimeirainstalação,porémseo scriptforexecutadonovamente,
eleprovavelmentenãovaifuncionar.Oadministradordesistemasprecisaser
bemdisciplinadoeprecisaescrevercódigoextraparalidarcomassituações
ondealgumpacotejáestáinstaladoouprecisaserremovidoouatualizado.
Asoutrasferramentasespecializadastêmumacaracterísticaimportante,
conhecidacomo idempotência:vocêpodeexecutá-lasdiversasvezessegui-
dascomomesmocódigoeelasmudarãoapenasoquefornecessário. Se
umpacotejáestáinstalado,elenãoseráreinstalado. Seumserviçojáestá
rodando,elenãoseráreiniciado. Seoarquivodeconfiguraç ãojápossuio
conteúdocorreto,elenãoseráalterado.
Idempotênciapermiteescrevercódigodeinfraestruturadeformadecla-
rativa. Aoinvésdainstruçãoser "instaleopacoteX”ou"crieousuárioY”,
vocêdiz"euqueroqueopacoteXestejainstalado”ou"euqueroqueousuário
Yexista”.Vocêdeclaraoestadofinaldesejadoequandoaferramentaexecuta,
casoopacoteouousuáriojáexistam,nadairáacontecer.
Apróximacoisaquevocêpodeestarseperguntandoé "Qualdessasferra-
mentasdevousar?”.Nestecapítulo,usaremosoPuppetporpermitirexempli-
ficarbemessapropriedadedeclarativadalinguagem,porserumaferramenta
66

## Página 85

CasadoCódigo Capítulo4. Infraestruturacomocódigo
madura,aceitanacomunidadedeadministradoresdesistemaeporserbem
adotadanacomunidade.Porém,averdadeéqueusarqualquerumadessas
ferramentasémelhorquenada.Asferramentasnesseespaçoestãoevoluindo
constantementeeéimportantevocêsefamiliarizarcomalgumasdelasantes
detomaradecisãodequaldelasémelhorparasuasituaç ão.
4.3 Introdução ao Puppet: recursos, provedo-
res, manifestos e dependências
Cadaumadasferramentasdegerenciamentodeconfiguraçãopossuiumater-
minologiaprópriaparasereferiraoselementosdalinguagemeaoscompo-
nentesdoseuecossistema. Emumnívelfundamental,cadacomandoque
vocêdeclaranalinguageméuma diretivaevocêpodedefinirumconjunto
delasemum arquivodediretivas, queéoequivalenteaumarquivode
código-fontedeumalinguagemdeprogramaçãocomoJavaouRuby.
NoPuppet,essasdiretivassãochamadasde recursos.Algunsexemplos
derecursosquevocêpodedeclararnoPuppetsão:pacotes,arquivos,usuá-
rios,grupos,serviços,trechosde scriptexecutável,dentreoutros.Oarquivo
noqualvocêdeclaraumconjuntodediretivaséchamadode manifesto.Ao
escrevercódigoPuppetvocêpassaráamaiorpartedotempocriandoeedi-
tandoessesmanifestos.
ParasefamiliarizarcomasintaxedalinguagemPuppeteseumodelode
execução,vamosreconstruiramáquinavirtualdoservidordebancodedados
elogarporSSHnamáquinaqueestázerada:
$ vagrant up db
Bringing machine ’db’ up with ’virtualbox’ provider...
==> db: Importing base box ’hashicorp/precise32’...
==> db: Matching MAC address for NAT networking...
==> db: Checking if box ’hashicorp/precise32’ is up to date...
==> db: Setting the name of the VM: blank_db_1394854529922_29194
==> db: Clearing any previously set network interfaces...
==> db: Preparing network interfaces based on configuration...
db: Adapter 1: nat
db: Adapter 2: hostonly
==> db: Forwarding ports...
67

## Página 86

4.3. IntroduçãoaoPuppet:recursos,provedores,manifestosedependências CasadoCódigo
db: 22 => 2222 (adapter 1)
==> db: Running ’pre-boot’ VM customizations...
==> db: Booting VM...
==> db: Waiting for machine to boot. This may take a few
minutes...
db: SSH address: 127.0.0.1:2222
db: SSH username: vagrant
db: SSH auth method: private key
==> db: Machine booted and ready!
==> db: Configuring and enabling network interfaces...
==> db: Mounting shared folders...
db: /vagrant => /private/tmp/blank
$ vagrant ssh db
Welcome to Ubuntu 12.04 LTS (GNU/Linux ...
vagrant@db$
AproveitandoqueaboxdoVagrantjápossuioPuppetinstalado,podemos
começarausá-lodiretamentecriandoumnovoarquivodemanifestovazio
chamado db.pp.Porpadrão,manifestospossuemextensão .pp:
vagrant@db$ nano db.pp
Como conteúdo inicial iremos declarar um recurso para o pacote
mysql-serveredizerqueoqueremosinstaladonosistema.Issoéfeitopas-
sandoovalor installedparaoparâmetro ensuredorecurso package:
package { "mysql-server":
ensure => installed,
}
Sevocêcompararessadeclaraçãoderecursocomocomandoqueexecu-
tamosnocapítulo 2–sudo apt-get install mysql-server–verá
queelessãoparecidos.Aprincipaldiferen çaéanatureza declarativadalin-
guagemdoPuppet.Nocomandomanual,instruímosogerenciadordepaco-
tesainstalaropacote mysql-serverenquantoquenoPuppetdeclaramos
oestadofinaldesejadodosistema.
Manifestosnãosãoumalistadecomandosaserexecutados.Quandoo
Puppetexecuta,elecomparaoestadoatualdosistemacomoestadodeclarado
68

## Página 87

CasadoCódigo Capítulo4. Infraestruturacomocódigo
nomanifesto,calculaadiferen çaeexecutaapenasasmudan çasnecessárias.
Apóssalvaroarquivo,executeoPuppetcomoseguintecomando:
vagrant@db$ sudo puppet apply db.pp
err: /Stage[main]//Package[mysql-server]/ensure: change from
purged to present failed: Execution of ...
...
E: Unable to fetch some archives, maybe run apt-get update or ...
notice: Finished catalog run in 6.62 seconds
Você pode ver que o Puppet tentou alterar o estado do pacote
mysql-server de removido (purged) para presente (present), no en-
tantoencontrouerrospoisesquecemosdeexecutarocomando apt-get
update,comofizemosnocapítulo 2.Paraisso,vamosdeclararumnovore-
curso execedefinirumadependênciadizendoqueeledeverodarantesdo
pacote mysql-server.Mudaremosoconteúdodoarquivo db.pppara:
exec { "apt-update":
command => "/usr/bin/apt-get update"
}
package { "mysql-server":
ensure => installed,
require => Exec["apt-update"],
}
Paraentenderoconteúdodomanifesto,precisamosconhecermaisalgu-
mascaracterísticasdalinguagemdoPuppet.Todorecursopossuiumnome
–astringentreaspasduplaslogoapósadeclaraçãoeantesdo“:”–queserve
comoumidentificadorúnico.Quandoumrecursoprecisasereferiraoutro
recurso,usamosasintaxecomaprimeiraletramaiúsculaeonomedorecurso
entrecolchetes.
OPuppetnãogarantequeaordemdeexecuç ãorespeiteaordememque
osrecursossãodeclaradosnomanifesto. Quandoexisteumadependência,
vocêprecisadeclará-laexplicitamente. Nestecaso,adicionamosoparâme-
tro requirenorecurso packageparagarantirqueocomando apt-get
69

## Página 88

4.3. IntroduçãoaoPuppet:recursos,provedores,manifestosedependências CasadoCódigo
updateexecuteantesdainstalaçãodoMySQL.AgoraoPuppetinstalaráo
pacote mysql-serverquandoexecutadonovamente:
vagrant@db$ sudo puppet apply db.pp
notice: /Stage[main]//Exec[apt-update]/returns: executed
successfully
notice: /Stage[main]//Package[mysql-server]/ensure: ensure
changed \
’purged’ to ’present’
notice: Finished catalog run in 59.98 seconds
VocêpodeverqueoPuppetalterouoestadodopacote mysql-server
deremovido(purged )parapresente(present ). Paraconfirmarqueopacote
foirealmenteinstalado,vocêpodeexecutarocomando:
vagrant@db$ aptitude show mysql-server
Package: mysql-server
State: installed
...
Percebaqueogerenciadordepacotesdizqueoestadoatualdopacote
mysql-serveré“instalado”(installed). Paraentenderanaturezadeclara-
tivadomanifesto,tenterodaroPuppetnovamente:
vagrant@db$ sudo puppet apply db.pp
notice: /Stage[main]//Exec[apt-update]/returns: executed
successfully
notice: Finished catalog run in 6.41 seconds
Dessavez,orecurso apt-updateexecutou,porémnadaaconteceucom
opacote mysql-server,quejáestavainstalado,satisfazendooestadode-
claradoemnossomanifestodoPuppet.
OutradiferençaquevocêpodeterpercebidoentreomanifestoPuppete
ocomandomanualdocapítulo 2équenãoprecisamosdizerparaoPuppet
qualgerenciadordepacotesusar.IssoacontecepoisrecursosdoPuppetsão
abstratos. Existemváriasimplementaçõesdiferentes–chamadasdeprove-
dores–paraosdiversossistemasoperacionais.Paraorecurso package,o
Puppetpossuidiversosprovedores: apt, rpm, yum, gem,dentreoutros.Na
70

## Página 89

CasadoCódigo Capítulo4. Infraestruturacomocódigo
horadaexecução,combaseeminformaçõesdosistemaoPuppetiráescolher
oprovedormaisadequado.Paraverumalistacomtodososprovedoresdis-
poníveisparaumdeterminadorecursoassimcomodocumentaçãodetalhada
dosparâmetrosqueorecursoaceita,vocêpodeexecutarocomando:
vagrant@db$ puppet describe package
package
=======
Manage packages. ...
...
Providers
---------
aix, appdmg, apple, apt, aptitude, aptrpm, blastwave, dpkg,
fink, freebsd, gem, hpux, macports, msi, nim, openbsd,
pacman, pip, pkg, pkgdmg, pkgutil, portage, ports,
portupgrade, rpm, rug, sun, sunfreeware, up2date, urpmi,
yum, zypper
AgoraqueentendemosofuncionamentobásicodoPuppet,vamosparar
deexecutarcomandosmanuaisdentrodoservidorecome çaraescrevercó-
digodeinfraestruturaforadamáquinavirtual.UsaremosoVagrantparanos
ajudaraprovisionaroservidor.
RecomeçarusandoPuppetcomVagrant
Primeiramentevamossairdamáquinavirtual dbedestruí-lanovamente,
comofizemosnofimdocapítulo 3:
vagrant@db$ logout
Connection to 127.0.0.1 closed.
$ vagrant destroy db
db: Are you sure you want to destroy the ’db’ VM? [y/N] y
==> db: Forcing shutdown of VM...
==> db: Destroying VM and associated drives...
Nomesmodiretórioemquevocêcriouoarquivo Vagrantfile,crieum
novodiretóriochamado manifestse,dentrodele,umnovoarquivo db.pp
71

## Página 90

4.3. IntroduçãoaoPuppet:recursos,provedores,manifestosedependências CasadoCódigo
comomesmoconteúdodase çãoanterior.Anovaestruturadediretóriosdeve
estarassim:
.
Vagrantfile
manifests
db.pp
AgoraéprecisoalteraroarquivodeconfiguraçãodoVagrant–oarquivo
Vagrantfile–parausaroPuppetcomoferramentadeprovisionamento
damáquinavirtual db:
VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
config.vm.box = "hashicorp/precise32"
config.vm.define :db do |db_config|
db_config.vm.network :private_network,
:ip => "192.168.33.10"
db_config.vm.provision "puppet" do |puppet|
puppet.manifest_file = "db.pp"
end
end
config.vm.define :web do |web_config|
web_config.vm.network :private_network,
:ip => "192.168.33.12"
end
config.vm.define :monitor do |monitor_config|
monitor_config.vm.network :private_network,
:ip => "192.168.33.14"
end
end
Feitoisso,assimquesubirmosumanovamáquinavirtualparaoservi-
dordebancodedados,oVagrantirárodaroPuppetautomaticamente,sem
precisarmoslogarnoservidorporSSHeexecutarcomandosmanualmente.
72

## Página 91

CasadoCódigo Capítulo4. Infraestruturacomocódigo
AsaídadaexecuçãodoPuppetserámostradalogoapósasaídanormaldo
Vagrantevocêperceberásealgumerroacontecer.Porexemplo,aexecuç ão
inicialmostraráopacote mysql-serversendoinstalado:
$ vagrant up db
Bringing machine ’db’ up with ’virtualbox’ provider...
==> db: Importing base box ’hashicorp/precise32’...
==> db: Matching MAC address for NAT networking...
==> db: Checking if box ’hashicorp/precise32’ is up to date...
==> db: Setting the name of the VM: blank_db_1394854957677_21160
==> db: Clearing any previously set network interfaces...
==> db: Preparing network interfaces based on configuration...
db: Adapter 1: nat
db: Adapter 2: hostonly
==> db: Forwarding ports...
db: 22 => 2222 (adapter 1)
==> db: Running ’pre-boot’ VM customizations...
==> db: Booting VM...
==> db: Waiting for machine to boot. This may take a few
minutes...
db: SSH address: 127.0.0.1:2222
db: SSH username: vagrant
db: SSH auth method: private key
==> db: Machine booted and ready!
==> db: Configuring and enabling network interfaces...
==> db: Mounting shared folders...
db: /vagrant => /private/tmp/blank
db: /tmp/vagrant-puppet-2/manifests => /private/tmp/blank/
manifests
==> db: Running provisioner: puppet...
Running Puppet with db.pp...
stdin: is not a tty
notice: /Stage[main]//Exec[apt-update]/returns: executed
successfully
notice: /Stage[main]//Package[mysql-server]/ensure: ensure
changed \’purged’ to ’present’
notice: Finished catalog run in 71.68 seconds
AgoraquesabemoscomousaroVagranteoPuppetparaprovisionar
73

## Página 92

4.4. Reinstalandooservidordebancodedados CasadoCódigo
nossoservidor,éhoraderestauraroambientedeproduç ãodalojavirtual.
4.4 Reinstalando o servidor de banco de dados
Temosummanifestosimplesqueexecutaoprimeiropassodainstalaç ãodo
servidordebancodedados. Sevocêlembradopróximopassoquetoma-
mosnocapítulo 2,precisamosnessemomentocriaroarquivodeconfigura-
ção /etc/mysql/conf.d/allow_external.cnfparapermitiracesso
remotoaoservidorMySQL.Faremosissousandoorecurso file,quere-
presentaaexistênciadeumarquivonosistema. Alteramosoconteúdodo
arquivo db.pppara:
exec { "apt-update":
command => "/usr/bin/apt-get update"
}
package { "mysql-server":
ensure => installed,
require => Exec["apt-update"],
}
file { "/etc/mysql/conf.d/allow_external.cnf":
owner => mysql,
group => mysql,
mode => 0644,
content => "[mysqld]\n bind-address = 0.0.0.0",
require => Package["mysql-server"],
}
Porpadrão,onomedorecursorepresentaocaminhocompletoondeo
arquivoserácriadonosistemaeoparâmetro contentpossuioconteúdodo
arquivo.Paraespecificarumcaminhodiferente,vocêpodeusaroparâmetro
path.Osparâmetros owner, groupe moderepresentamousuárioegrupo
associadosaoarquivoesuaspermissões.
Paraaplicaranovaconfiguração,aoinvésdedestruiresubirumanova
máquinavirtual,vocêpodeusarocomando provisiondoVagrantpara
simplesmenteexecutaroPuppetnamáquinavirtualjáexistente:
74

## Página 93

CasadoCódigo Capítulo4. Infraestruturacomocódigo
$ vagrant provision db
==> db: Running provisioner: puppet...
Running Puppet with db.pp...
stdin: is not a tty
notice: /Stage[main]//Exec[apt-update]/returns: executed
successfully
notice: /Stage[main]//File[ /etc/mysql/conf.d/
allow_external.cnf]/ \
ensure: defined content as
’{md5}4149205484cca052a3bfddc8ae60a71e’
notice: Finished catalog run in 4.36 seconds
Dessa vez, o Puppet criou o arquivo
/etc/mysql/conf.d/allow_external.cnf. Para saber quando
umarquivodeconfiguraçãoprecisaseralterado,elecalculaum checksum
MD5doseuconteúdo.OMD5éumalgoritmode hashbastanteusadopara
verificaraintegridadedeumarquivo.Umapequenaalteraç ãonoconteúdo
doarquivofazcomqueoseu checksumMD5sejatotalmentediferente.
Nonossocaso,oconteúdodoarquivodeconfiguraç ãoépequenoecon-
seguimosdeclará-loporcompletonomanifesto. Noentanto,écomumter
arquivosdeconfiguraçãocomdezenasoucentenasdelinhas.Gerenciarar-
quivoslongoscomoumaúnicastringemcódigoPuppetnãoéumaboaideia.
Podemostrocaroconteúdodoarquivoporum template.OPuppetentende
templatesERB(embeddedruby),umsistemade templatequepermiteembutir
códigoRubydentrodeumarquivotexto.
Parausarum template, primeiramenteprecisamosextrairoconteúdo
paraumnovoarquivo allow_ext.cnf,quedeveficarjuntodomanifesto:
.
Vagrantfile
manifests
allow_ext.cnf
db.pp
Mudeoconteúdodoarquivo allow_ext.cnfligeiramente,paraqueo
Puppetaltereoarquivonapróximaexecuç ão:
[mysqld]
bind-address = 9.9.9.9
75

## Página 94

4.4. Reinstalandooservidordebancodedados CasadoCódigo
Porfim,trocamosoparâmetro contentdorecurso fileparausaro
template:
exec ...
package ...
file { "/etc/mysql/conf.d/allow_external.cnf":
owner => mysql,
group => mysql,
mode => 0644,
content => template("/vagrant/manifests/allow_ext.cnf"),
require => Package["mysql-server"],
}
AoexecutaroPuppetnovamente,vocêveráqueo checksumMD5irámu-
dareoconteúdodoarquivoseráalterado:
$ vagrant provision db
==> db: Running provisioner: puppet...
Running Puppet with db.pp...
stdin: is not a tty
notice: /Stage[main]//Exec[apt-update]/returns: executed
successfully
notice: /Stage[main]//File[ /etc/mysql/conf.d/
allow_external.cnf]/ \
content: content changed
’{md5}4149205484cca052a3bfddc8ae60a71e’
\ to
’{md5}8e2381895fcf40fa7692e38ab86c7192’
notice: Finished catalog run in 4.60 seconds
AgoraprecisamosreiniciaroserviçoparaqueoMySQLpercebaaaltera-
çãonoarquivodeconfiguração.Fazemosissodeclarandoumnovorecurso
dotipo service:
exec ...
package ...
file ...
service { "mysql":
76

## Página 95

CasadoCódigo Capítulo4. Infraestruturacomocódigo
ensure => running,
enable => true,
hasstatus => true,
hasrestart => true,
require => Package["mysql-server"],
}
Oserviçopossuinovosparâmetros: ensure => running,quega-
rantequeoserviçoestejarodando; enable, quegarantequeoserviço
rodesemprequeoservidorreiniciar; hasstatuse hasrestart, que
declaramqueoserviçoentendeoscomandos statuse restart; por
fim,oparâmetro require,quedeclaraumadependênciacomorecurso
Package["mysql-server"].
Se você tentar executar o Puppet, verá que nada acontece
pois o serviço já foi iniciado quando o pacote foi instalado.
Para reiniciar o serviço toda vez que o arquivo de configuração
mudar, precisamos declarar uma nova dependência no recurso
File["/etc/mysql/conf.d/allow_external.cnf"]:
exec ...
package ...
file { "/etc/mysql/conf.d/allow_external.cnf":
owner => mysql,
group => mysql,
mode => 0644,
content => template("/vagrant/manifests/allow_ext.cnf"),
require => Package["mysql-server"],
notify => Service["mysql"],
}
service ...
Oparâmetro notifydefineumadependênciadeexecução:sempreque
orecurso fileforalterado,elefarácomqueorecurso serviceexecute.
Dessavez,sealterarmosoconteúdodo template allow_ext.cnfdevolta
para 0.0.0.0eexecutarmosoPuppet,oserviçoseráreiniciado:
77

## Página 96

4.4. Reinstalandooservidordebancodedados CasadoCódigo
$ vagrant provision db
==> db: Running provisioner: puppet...
Running Puppet with db.pp...
stdin: is not a tty
notice: /Stage[main]//Exec[apt-update]/returns: executed
successfully
notice: /Stage[main]//File[ /etc/mysql/conf.d/
allow_external.cnf]/ \
content: content changed
’{md5}8e2381895fcf40fa7692e38ab86c7192’ \
to
’{md5}907c91cba5e1c7770fd430182e42c437’
notice: /Stage[main]//Service[mysql]: Triggered ’refresh’ \
from 1 events
notice: Finished catalog run in 6.88 seconds
Comessaalteração,obancodedadosestárodandonovamenteeumadas
verificaçõesdoNagiosdeveficarverde. Paracorrigirapróximaverificaç ão
precisamoscompletaraconfiguraçãodobancodedadoscriandoo schemae
ousuáriodalojavirtual.
Criaremoso schemadeclarandomaisumrecurso execcomomesmo
comandousadonocapítulo2:
exec ...
package ...
file ...
service ...
exec { "loja-schema":
unless => "mysql -uroot loja_schema",
command => "mysqladmin -uroot create loja_schema",
path => "/usr/bin/",
require => Service["mysql"],
}
Alémdadependênciacomorecurso Service["mysql"],usamosum
novoparâmetro unlessqueespecificaumcomandodeteste:casoseucó-
digodesaídasejazero,ocomandoprincipalnãoiráexecutar.Essaéaforma
detornarumrecursodotipo execidempotente. Aocontráriodo exec
78

## Página 97

CasadoCódigo Capítulo4. Infraestruturacomocódigo
queusamospararodaro apt-get update,nestecasoéimportantequeo
Puppetnãotentecriarumnovo schematodavezqueforexecutado.
Conformefizemosnocapítulo2,precisamosremoveracontaanônima
deacessoaoMySQLantesdecriarousuárioparaacessarnossonovo schema.
Faremosissodeclarandoumnovorecurso exec:
exec ...
package ...
file ...
service ...
exec ...
exec { "remove-anonymous-user":
command => "mysql -uroot -e \"DELETE FROM mysql.user \
WHERE user=’’; \
FLUSH PRIVILEGES\ "",
onlyif => "mysql -u’ ’",
path => "/usr/bin",
require => Service["mysql"],
}
Nestecomando,aoinvésdeusaroparâmetro unlessusamosoparâme-
trooposto onlyifqueiráexecutarocomandoprincipalapenasseocódigo
desaídadocomandodetesteforzero. Estecomandodetestetentaacessar
oMySQLusandoumusuáriovazio.Casoconsigaconectar,oPuppetprecisa
executarocomandoSQL DELETE ...pararemoveracontaanônima.Por
fim,criaremosumúltimorecurso execparacriarousuáriocompermissão
deacessoao schemadalojavirtual:
exec ...
package ...
file ...
service ...
exec ...
exec ...
exec { "loja-user":
unless => "mysql -uloja -plojasecret loja_schema",
79

## Página 98

4.4. Reinstalandooservidordebancodedados CasadoCódigo
command => "mysql -uroot -e \"GRANT ALL PRIVILEGES ON \
loja_schema.* TO ’loja’@’%’ \
IDENTIFIED BY ’lojasecret’;\"",
path => "/usr/bin/",
require => Exec["loja-schema"],
}
AoexecutaroPuppetpelaúltimaveznoservidordebancodedados,
veremosumasaídaparecidacom:
$ vagrant provision db
==> db: Running provisioner: puppet...
Running Puppet with db.pp...
stdin: is not a tty
notice: /Stage[main]//Exec[apt-update]/returns: executed
successfully
notice: /Stage[main]//Exec[loja-schema]/returns: executed
successfully
notice: /Stage[main]//Exec[loja-user]/returns: executed
successfully
notice: /Stage[main]//Exec[remove-anonymous-user]/returns:
executed \ successfully
notice: Finished catalog run in 15.56 seconds
Comissoconseguimosrestaurarporcompletooservidordebancodeda-
dosetodasasverificaçõesdoNagiosreferentesao host dbdeverãoficarver-
des.AúnicaverificaçãoquepermanecerávermelhaéaverificaçãodoTom-
cat,poisaaplicaçãoaindanãoestáacessível. Naspróximasse çõesiremos
automatizaroprocessodeprovisionamentodoservidor webedo deployda
aplicação.Porenquanto,oconteúdocompletodomanifesto db.ppficou:
exec { "apt-update":
command => "/usr/bin/apt-get update"
}
package { "mysql-server":
ensure => installed,
require => Exec["apt-update"],
}
80

## Página 99

CasadoCódigo Capítulo4. Infraestruturacomocódigo
file { "/etc/mysql/conf.d/allow_external.cnf":
owner => mysql,
group => mysql,
mode => 0644,
content => template("/vagrant/manifests/allow_ext.cnf"),
require => Package["mysql-server"],
notify => Service["mysql"],
}
service { "mysql":
ensure => running,
enable => true,
hasstatus => true,
hasrestart => true,
require => Package["mysql-server"],
}
exec { "loja-schema":
unless => "mysql -uroot loja_schema",
command => "mysqladmin -uroot create loja_schema",
path => "/usr/bin/",
require => Service["mysql"],
}
exec { "remove-anonymous-user":
command => "mysql -uroot -e \"DELETE FROM mysql.user \
WHERE user=’’; \
FLUSH PRIVILEGES\ "",
onlyif => "mysql -u’ ’",
path => "/usr/bin",
require => Service["mysql"],
}
exec { "loja-user":
unless => "mysql -uloja -plojasecret loja_schema",
command => "mysql -uroot -e \"GRANT ALL PRIVILEGES ON \
loja_schema.* TO ’loja’@’%’ \
IDENTIFIED BY ’lojasecret’;\"",
81

## Página 100

4.5. Reinstalandooservidorweb CasadoCódigo
path => "/usr/bin/",
require => Exec["loja-schema"],
}
4.5 Reinstalando o servidor web
Agoraqueoservidor dbestárestaurado,vamosautomatizaroprocessode
provisionamentoe deploynoservidor web. Paraisto,criaremosumnovo
arquivonodiretório manifestschamado web.pp:
.
Vagrantfile
manifests
allow_ext.cnf
db.pp
web.pp
Emvezdeassociaronovomanifestocomoservidor webjáexistente,
vamoscriarumanovamáquinavirtualtemporáriachamada web2parapo-
dermostestarnossocódigoPuppetisoladamenteantesdeaplicá-lonoambi-
entedeprodução.Aofinaldocapítulo,iremosnoslivrardamáquinavirtual
web2eaplicaremosamesmaconfiguraçãonoservidor webdeverdade.O
conteúdodo Vagrantfilecomanovamáquinavirtualdeveficar:
VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
config.vm.box = "hashicorp/precise32"
config.vm.define :db do |db_config|
db_config.vm.network :private_network,
:ip => "192.168.33.10"
db_config.vm.provision "puppet" do |puppet|
puppet.manifest_file = "db.pp"
end
end
config.vm.define :web do |web_config|
82

## Página 101

CasadoCódigo Capítulo4. Infraestruturacomocódigo
web_config.vm.network :private_network,
:ip => "192.168.33.12"
end
config.vm.define :web2 do |web_config|
web_config.vm.network :private_network,
:ip => "192.168.33.13"
web_config.vm.provision "puppet" do |puppet|
puppet.manifest_file = "web.pp"
end
end
config.vm.define :monitor do |monitor_config|
monitor_config.vm.network :private_network,
:ip => "192.168.33.14"
end
end
Inicialmentevamosdeclararapenasosrecursosparaexecutaro apt-get
updateeinstalarospacotesbasedoservidor web2,deformasimilaraos
comandosexecutadosnocapítulo 2:
exec { "apt-update":
command => "/usr/bin/apt-get update"
}
package { ["mysql-client", "tomcat7"]:
ensure => installed,
require => Exec["apt-update"],
}
Aosubiranovamáquinavirtual,oPuppetiráaplicaressaconfigura çãoe
instalarospacotes:
$ vagrant up web2
Bringing machine ’web2’ up with ’virtualbox’ provider...
==> web2: Importing base box ’hashicorp/precise32’...
...
==> web2: Running provisioner: puppet...
83

## Página 102

4.5. Reinstalandooservidorweb CasadoCódigo
Running Puppet with web.pp...
stdin: is not a tty
notice: /Stage[main]//Exec[apt-update]/returns: executed
successfully
notice: /Stage[main]//Package[mysql-client]/ensure: ensure
changed \ ’purged’ to ’present’
notice: /Stage[main]//Package[tomcat7]/ensure: ensure changed \
’purged’ to ’present’
notice: Finished catalog run in 105.89 seconds
Feitoisso,vocêpodeabrirseunavegadoredigitaraURL http://192.168.33.
13:8080/evocêdeveráverumapáginaquediz"ItWorks!”.Issosignificaqueo
Tomcatestáinstaladoerodandocorretamente.
Ospróximospassosrealizadosnocapítulo 2foramaconfiguraçãodaco-
nexãoseguracomHTTPS,acriaçãodo keystoreparaarmazenarocertifi-
cadoSSLeoaumentodaquantidadedememóriadisponívelparaamáquina
virtualJavaquandooTomcatinicia.
Todasessasoperaçõesenvolvemeditaroucriarumnovoarquivonosis-
tema. JásabemoscomoentregararquivoscomoPuppet,entãofaremosos
trêspassosdeumasóvez.Primeiramente,vamosreaproveitarosarquivosde
configuraçãoquejáestãofuncionandonoservidor webcomotemplatespara
omanifestodoPuppet. Osseguintescomandosirãocopiarosarquivosda
máquinavirtualwebparaodiretóriocompartilhadopeloVagrant:
$ vagrant ssh web -- ’sudo cp /var/lib/tomcat7/conf/.keystore \
> /vagrant/manifests/’
$ vagrant ssh web -- ’sudo cp /var/lib/tomcat7/conf/server.xml \
> /vagrant/manifests/’
$ vagrant ssh web -- ’sudo cp /etc/default/tomcat7 \
> /vagrant/manifests/’
Emvezdeusarocomando vagrant sshparalogarnamáquinavirtual,
passamosumcomandoentreaspasapósostraços --.Essecomandoexecu-
tarádentrodamáquinavirtual. Ocaminho /vagrantéondeoVagrant
mapeiaodiretórioondevocêdefiniuo Vagrantfiledentrodamáquina
virtual.Setudodercerto,osarquivosforadoVagrantdevemser:
84

## Página 103

CasadoCódigo Capítulo4. Infraestruturacomocódigo
.
Vagrantfile
manifests
.keystore
allow_ext.cnf
db.pp
server.xml
tomcat7
web.pp
Comonãoprecisamosalterarnadanoconteúdodessesarquivos,basta
declararmosnovosrecursosdotipo fileparaqueoPuppetentregue-osno
lugarcerto,ajustandoseusdonosepermissões:
exec ...
package ...
file { "/var/lib/tomcat7/conf/.keystore":
owner => root,
group => tomcat7,
mode => 0640,
source => "/vagrant/manifests/.keystore",
require => Package["tomcat7"],
}
file { "/var/lib/tomcat7/conf/server.xml":
owner => root,
group => tomcat7,
mode => 0644,
source => "/vagrant/manifests/server.xml",
require => Package["tomcat7"],
}
file { "/etc/default/tomcat7":
owner => root,
group => root,
mode => 0644,
source => "/vagrant/manifests/tomcat7",
require => Package["tomcat7"],
85

## Página 104

4.5. Reinstalandooservidorweb CasadoCódigo
}
Porúltimo,precisamosdeclararoserviço tomcat7,queprecisaserrei-
niciadoquandoosarquivosdeconfiguraç ãosãoalterados. Osparâmetros
dorecurso servicesãoosmesmosqueusamosnoserviço mysqlquando
configuramososervidordebancodedados:
exec ...
package ...
file { "/var/lib/tomcat7/conf/.keystore":
...
notify => Service["tomcat7"],
}
file { "/var/lib/tomcat7/conf/server.xml":
...
notify => Service["tomcat7"],
}
file { "/etc/default/tomcat7":
...
notify => Service["tomcat7"],
}
service { "tomcat7":
ensure => running,
enable => true,
hasstatus => true,
hasrestart => true,
require => Package["tomcat7"],
}
Podemosentãorodaromanifestotodoparaaplicarasúltimasconfigura-
çõesnoservidor web2:
$ vagrant provision web2
==> web2: Running provisioner: puppet...
Running Puppet with web.pp...
86

## Página 105

CasadoCódigo Capítulo4. Infraestruturacomocódigo
stdin: is not a tty
notice: /Stage[main]//Exec[apt-update]/returns: executed
successfully
notice: /Stage[main]//File[ /var/lib/tomcat7/conf/server.xml]/
content: \ content changed
’{md5}523967040584a921450af2265902568d’ \
to ’{md5}e4f0d5610575a720ad19fae4875e9f2f’
notice: /Stage[main]//File[ /var/lib/tomcat7/conf/.keystore]/
ensure: \ defined content as
’{md5}80792b4dc1164d67e1eb859c170b73d6’
notice: /Stage[main]//File[ /etc/default/tomcat7]/content:
content \
changed ’{md5}49f3fe5de425aca649e2b69f4495abd2’ to \
’{md5}1f429f1c7bdccd3461aa86330b133f51’
notice: /Stage[main]//Service[tomcat7]: Triggered ’refresh’ from
3 events
notice: Finished catalog run in 14.58 seconds
Feitoisso,temosoTomcatconfiguradoparaaceitarconexõesHTTPe
HTTPS.Podemostestarabrindoumanovajanelanonavegadorwebeaces-
sandoaURL https://192.168.33.13:8443/. Apósaceitarocertificadoautoassi-
nado,vocêveráumapáginaquediz"Itworks!”.
4.6 Fazendo deploy da aplicação
Paratermosumservidor webcompleto,precisamosfazero deploydaloja
virtual. EmvezdeusaroPuppetparareconstruiroprocessode buildden-
trodamáquinavirtual–comofizemosnocapítulo2–vamosreaproveitaro
artefato .wargerado.Nocapítulo 6iremosrevisitaressadecisãoeencontra-
remosumaformamelhordegeraroartefato .wardaaplicação.
Vamostambémreaproveitaro templatedoarquivo context.xml,no
qualdefinimososrecursosJNDIparaacessoaobancodedados. Usando
omesmotruquedase çãoanterior,vamoscopiarosarquivosdedentroda
máquinavirtualweb:
$ vagrant ssh web -- ’sudo cp /var/lib/tomcat7/conf/
context.xml \
87

## Página 106

4.6. Fazendodeploydaaplicação CasadoCódigo
> /vagrant/manifests/’
$ vagrant ssh web -- \
> ’sudo cp /var/lib/tomcat7/webapps/devopsnapratica.war \
> /vagrant/manifests/’
AgoraoconteúdodosarquivosediretóriosforadoVagrantdevemser:
.
Vagrantfile
manifests
.keystore
allow_ext.cnf
context.xml
db.pp
devopsnapratica.war
server.xml
tomcat7
web.pp
Oartefatocontentoaaplicaçãoweb devopsnapratica.warnãopre-
cisaseralterado,porémvamosdefinirvariáveisdentrodomanifestopara
conterosdadosdeacessoaobancodedados. Essasvariáveisserãosubsti-
tuídasquandooPuppetprocessaro templateERBquecriaremosnoarquivo
context.xml:
exec ...
package ...
file ...
file ...
file ...
service ...
$db_host = "192.168.33.10"
$db_schema = "loja_schema"
$db_user = "loja"
$db_password = "lojasecret"
file { "/var/lib/tomcat7/conf/context.xml":
owner => root,
88

## Página 107

CasadoCódigo Capítulo4. Infraestruturacomocódigo
group => tomcat7,
mode => 0644,
content => template("/vagrant/manifests/context.xml"),
require => Package["tomcat7"],
notify => Service["tomcat7"],
}
file { "/var/lib/tomcat7/webapps/devopsnapratica.war":
owner => tomcat7,
group => tomcat7,
mode => 0644,
source => "/vagrant/manifests/devopsnapratica.war",
require => Package["tomcat7"],
notify => Service["tomcat7"],
}
A sintaxe do Puppet para declarar variáveis é um cifrão$ seguido
donomedavariável. Usamososímbolodeigual =paraatribuirvalo-
res às nossas variáveis. Para usar essas variáveis dentro dotemplatedo
arquivo context.xml, precisamos alterar o seu conteúdo substituindo
os valores existentes pelo marcador<%= var %>, onde var deve ser
o nome da variável sem o cifrão$. O novotemplateERB do arquivo
manifests/context.xmldeveser:
<?xml version=’1.0’ encoding=’utf-8’?>
<Context>
<!-- Default set of monitored resources -->
<WatchedResource>WEB-INF/web.xml</WatchedResource>
<Resource name="jdbc/web" auth="Container"
type="javax.sql.DataSource" maxActive="100"
maxIdle="30"
maxWait="10000"
username="<%= db_user %> "
password="<%= db_password %> "
driverClassName="com.mysql.jdbc.Driver"
url="jdbc:mysql://<%= db_host %> :3306/<%= db_schema %> "/>
<Resource name="jdbc/secure" auth="Container"
89

## Página 108

4.6. Fazendodeploydaaplicação CasadoCódigo
type="javax.sql.DataSource" maxActive="100" maxIdle="30"
maxWait="10000"
username="<%= db_user %> "
password="<%= db_password %> "
driverClassName="com.mysql.jdbc.Driver"
url="jdbc:mysql://<%= db_host %> :3306/<%= db_schema %> "/>
<Resource name="jdbc/storage" auth="Container"
type="javax.sql.DataSource" maxActive="100" maxIdle="30"
maxWait="10000"
username="<%= db_user %> "
password="<%= db_password %> "
driverClassName="com.mysql.jdbc.Driver"
url="jdbc:mysql://<%= db_host %> :3306/<%= db_schema %> "/>
</Context>
Comisso,finalizamosomanifestoPuppetparaprovisionarefazer deploy
daaplicaçãonoservidor web2.Podemosexecutá-lorodandoocomando:
$ vagrant provision web2
==> web2: Running provisioner: puppet...
Running Puppet with web.pp...
stdin: is not a tty
notice: /Stage[main]//Exec[apt-update]/returns: executed
successfully
notice: /Stage[main]//File[ /var/lib/tomcat7/conf/context.xml]/
content: \ content changed
’{md5}4861cda2bbf3a56fbfdb78622c550019’ \
to ’{md5}8365f14d15ddf99b1d20f9672f0b98c7’
notice: /Stage[main]//File[ /var/lib/tomcat7/webapps/ \
devopsnapratica.war]/ensure: defined content as \
’{md5}cba179ec04e75ce87140274b0aaa2263’
notice: /Stage[main]//Service[tomcat7]: Triggered ’refresh’ from
2 events
notice: Finished catalog run in 21.78 seconds
TenteagoraacessaraURL http://192.168.33.13:8080/devopsnapratica/noseu
navegadorparaverquealojaestáfuncionandocorretamente.Sucesso!
Agoraquesabemosrecriaroservidor webporcompleto,podemosnos
90

## Página 109

CasadoCódigo Capítulo4. Infraestruturacomocódigo
livrardamáquinavirtual web2.Parademonstraropoderdousodeautoma-
çãoparaprovisionamentoe deploy,vamostambémdestruiramáquinavirtual
weberecriá-ladozero:
$ vagrant destroy web web2
web2: Are you sure you want to destroy the ’web2’ VM?[y/N] y
==> web2: Forcing shutdown of VM...
==> web2: Destroying VM and associated drives...
==> web2: Running cleanup tasks for ’puppet’ provisioner...
web: Are you sure you want to destroy the ’web’ VM? [y/N] y
==> web: Forcing shutdown of VM...
==> web: Destroying VM and associated drives...
Antesdereiniciaramáquinavirtualnovamente,precisamosatualizaro
arquivodeconfiguraçãodoVagrant–oVagrantfile–paraconterapenas
umservidor web:
VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
config.vm.box = "hashicorp/precise32"
config.vm.define :db do |db_config|
db_config.vm.network :private_network,
:ip => "192.168.33.10"
db_config.vm.provision "puppet" do |puppet|
puppet.manifest_file = "db.pp"
end
end
config.vm.define :web do |web_config|
web_config.vm.network :private_network,
:ip => "192.168.33.12"
web_config.vm.provision "puppet" do |puppet|
puppet.manifest_file = "web.pp"
end
end
config.vm.define :monitor do |monitor_config|
91

## Página 110

4.6. Fazendodeploydaaplicação CasadoCódigo
monitor_config.vm.network :private_network,
:ip => "192.168.33.14"
end
end
Oúltimopassoéreconstruiramáquinavirtual webdozero:
$ vagrant up web
Bringing machine ’web’ up with ’virtualbox’ provider...
==> web: Importing base box ’hashicorp/precise32’...
==> web: Matching MAC address for NAT networking...
==> web: Checking if box ’hashicorp/precise32’ is up to date...
==> web: Setting the name of the VM:
blank_web_1394856878524_4521
==> web: Fixed port collision for 22 => 2222. Now on port 2200.
==> web: Clearing any previously set network interfaces...
==> web: Preparing network interfaces based on configuration...
web: Adapter 1: nat
web: Adapter 2: hostonly
==> web: Forwarding ports...
web: 22 => 2200 (adapter 1)
==> web: Running ’pre-boot’ VM customizations...
==> web: Booting VM...
==> web: Waiting for machine to boot. This may take a few
minutes...
web: SSH address: 127.0.0.1:2200
web: SSH username: vagrant
web: SSH auth method: private key
==> web: Machine booted and ready!
==> web: Configuring and enabling network interfaces...
==> web: Mounting shared folders...
web: /vagrant => /private/tmp/blank
web: /tmp/vagrant-puppet-2/manifests =>
/private/tmp/blank/manifests
==> web: Running provisioner: puppet...
Running Puppet with web.pp...
stdin: is not a tty
notice: /Stage[main]//Exec[apt-update]/returns: executed
successfully
notice: /Stage[main]//Package[mysql-client]/ensure: ensure
92

## Página 111

CasadoCódigo Capítulo4. Infraestruturacomocódigo
changed \ ’purged’ to ’present’
notice: /Stage[main]//Package[tomcat7]/ensure: ensure changed
’purged’ \ to ’present’
notice: /Stage[main]//File[ /var/lib/tomcat7/conf/context.xml]/
content: \ content changed
’{md5}4861cda2bbf3a56fbfdb78622c550019’ \
to ’{md5}8365f14d15ddf99b1d20f9672f0b98c7’
notice: /Stage[main]//File[ /var/lib/tomcat7/conf/server.xml]/
content: \ content changed
’{md5}523967040584a921450af2265902568d’ \
to ’{md5}e4f0d5610575a720ad19fae4875e9f2f’
notice: /Stage[main]//File[ /var/lib/tomcat7/conf/.keystore]/
ensure: \ defined content as
’{md5}80792b4dc1164d67e1eb859c170b73d6’
notice: /Stage[main]//File[ /var/lib/tomcat7/webapps/ \
devopsnapratica.war]/ensure: defined content as \
’{md5}cba179ec04e75ce87140274b0aaa2263’
notice: /Stage[main]//File[ /etc/default/tomcat7]/content:
content \ changed
’{md5}49f3fe5de425aca649e2b69f4495abd2’ to \
’{md5}1f429f1c7bdccd3461aa86330b133f51’
notice: /Stage[main]//Service[tomcat7]: Triggered ’refresh’ from
5 events
notice: Finished catalog run in 106.31 seconds
Pronto!Conseguimosreconstruiroservidor webefazer deploydaloja
virtualem1minuto!
AverificaçãodoNagiosdeveficarverdeealojavirtualestánovamente
acessívelparanossosusuários.Aversãofinaldomanifesto web.pp,aofinal
destecapítulo,ficou:
exec { "apt-update":
command => "/usr/bin/apt-get update"
}
package { ["mysql-client", "tomcat7"]:
ensure => installed,
require => Exec["apt-update"],
}
93

## Página 112

4.6. Fazendodeploydaaplicação CasadoCódigo
file { "/var/lib/tomcat7/conf/.keystore":
owner => root,
group => tomcat7,
mode => 0640,
source => "/vagrant/manifests/.keystore",
require => Package["tomcat7"],
notify => Service["tomcat7"],
}
file { "/var/lib/tomcat7/conf/server.xml":
owner => root,
group => tomcat7,
mode => 0644,
source => "/vagrant/manifests/server.xml",
require => Package["tomcat7"],
notify => Service["tomcat7"],
}
file { "/etc/default/tomcat7":
owner => root,
group => root,
mode => 0644,
source => "/vagrant/manifests/tomcat7",
require => Package["tomcat7"],
notify => Service["tomcat7"],
}
service { "tomcat7":
ensure => running,
enable => true,
hasstatus => true,
hasrestart => true,
require => Package["tomcat7"],
}
$db_host = "192.168.33.10"
$db_schema = "loja_schema"
$db_user = "loja"
94

## Página 113

CasadoCódigo Capítulo4. Infraestruturacomocódigo
$db_password = "lojasecret"
file { "/var/lib/tomcat7/conf/context.xml":
owner => root,
group => tomcat7,
mode => 0644,
content => template("/vagrant/manifests/context.xml"),
require => Package["tomcat7"],
notify => Service["tomcat7"],
}
file { "/var/lib/tomcat7/webapps/devopsnapratica.war":
owner => tomcat7,
group => tomcat7,
mode => 0644,
source => "/vagrant/manifests/devopsnapratica.war",
require => Package["tomcat7"],
notify => Service["tomcat7"],
}
Investiremautomaçãonospermitiudestruirereconstruirservidoresem
questãodeminutos. Vocêtambémdeveterpercebidoquepassamosmuito
poucotempoexecutandocomandosmanuaisdentrodosservidores.Trans-
ferimosaresponsabilidadedeexecuçãodecomandosparaoPuppetedecla-
ramosoestadofinaldesejadoemarquivosdemanifesto.
OcódigodoPuppetestácome çandoacrescerenãotemosumaestrutura
claraparaorganizarosarquivosdemanifestoeos templates.Tambémestamos
tratandooartefato .warcomoumarquivoestático,algoquesabemosnão
serideal. Nospróximoscapítulosiremosrevisitaressasdecisõesecriarum
ecossistemamaisrobustoparaentregacontínuadalojavirtual.
95

## Página 115

Capítulo5
Puppetalémdobásico
Nofinaldocapítulo 4,ocódigoPuppetparaconfigurarainfraestruturada
lojavirtualnãoestámuitobemorganizado.Aúnicaseparaç ãoquefizemos
foicriardoisarquivosdemanifesto,umparacadaservidor: webe db.No
entanto,dentrodecadaarquivo,ocódigoésimplesmenteumalistadere-
cursos.Alémdisso,osarquivosdeconfiguraçãoede templatesestãojogados
semnenhumaestrutura. Nestecapítulovamosaprendernovosconceitose
funcionalidadesdoPuppetaomesmotempoquerefatoramosocódigopara
torná-lomaisidiomáticoebemorganizado.
5.1 Classes e tipos definidos
OPuppetgerenciaumaúnicainstânciadecadarecursodefinidoemumma-
nifesto,tornando-osumaespéciede singleton.Damesmaforma,uma classe
éumacoleçãoderecursosúnicosemseusistema. Sevocêconhecelingua-

## Página 116

5.1. Classesetiposdefinidos CasadoCódigo
gensorientadasaobjetos,nãoseconfundacomaterminologia.Umaclasse
noPuppetnãopodeserinstanciadadiversasvezes.Classessãoapenasuma
formadedarnomeaumacole çãoderecursosqueserãoaplicadoscomouma
unidade.
UmbomusodeclassesnoPuppetéparaconfiguraç ãodeserviçosque
vocêprecisainstalarapenasumaveznosistema. Porexemplo,noarquivo
db.ppinstalamoseconfiguramososervidorMySQLecriamoso schemaeo
usuárioespecíficosdalojavirtual.Navidareal,podemostervários schemase
usuáriosusandoomesmobancodedados,porémnãoinstalamosmaisdeum
MySQLporsistema.OservidorMySQLéumbomcandidatoparadefinirmos
emumaclassegenérica,quechamaremosde mysql-server.Refatorando
nossoarquivo db.ppparadeclarareusaranovaclasse,teremos:
class mysql-server {
exec { "apt-update": ... }
package { "mysql-server": ... }
file { "/etc/mysql/conf.d/allow_external.cnf": ... }
service { "mysql": ... }
exec { "remove-anonymous-user": ... }
}
include mysql-server
exec { "loja-schema": ...,
require => Class["mysql-server"],
}
exec { "loja-user": ... }
Percebaquemovemosorecurso Exec["remove-anonymous-user"]
– que remove a conta de acesso anônima – para dentro da classe
mysql-serverpoisissoéalgoquedeveacontecersomentequandooser-
vidorMySQLéinstaladopelaprimeiravez.Outramudan çaquevocêpode
perceberéqueorecurso Exec["loja-schema"]agoratemumadepen-
dênciacom Class["mysql-server"]emvezdeumrecursoespecífico
Service["mysql"]comoanteriormente.Essaéumaformadeencapsular
detalhesdeimplementaçãodentrodaclasse,isolandoesseconhecimentodo
restodocódigo,quepodedeclarardependênciasemcoisasmaisabstratase
98

## Página 117

CasadoCódigo Capítulo5. Puppetalémdobásico
estáveis.
Paradefinirumanovaclassebastaescolherseunomeecolocartodosos
recursosdentrodeumadeclaraçãodotipo class <nome da classe> {
... }.Parausarumaclassevocêpodeutilizarasintaxe include <nome
da classe>ouaversãomaisparecidacomadefiniç ãodeumrecursocom
quejáestamosacostumados: class { "<nome da classe>": ... }.
Poroutrolado,osrecursosquecriamo schemaeousuáriodalojavirtual
podemserreaproveitadosparacriar schemaseusuáriosparaoutrasaplica-
çõesrodandonestemesmoservidor.Colocá-losemumaclasseseriaaforma
erradadeencapsulamentopoisoPuppetexigiriaqueelafosseúnica. Para
situaçõescomoesta,oPuppetpossuiumaoutraformadeencapsulamento
chamadade“tiposdefinidos”.
Umtipodefinido–oudefinedtype–éumacoleçãoderecursosquepode
serusadaváriasvezesemummesmomanifesto.Elespermitemquevocêeli-
mineduplicaçãodecódigoagrupandorecursosrelacionadosquepodemser
reutilizadosemconjunto.Vocêpodeinterpretá-loscomoequivalentesama-
crosemumalinguagemdeprogramaç ão.Alémdisso,elespodemserpara-
metrizadosedefinirvalorespadrãoparaparâmetrosopcionais.Agrupando
osdoisrecursos execparacriaro schemaeousuáriodeacessoaobancode
dadosemumtipodefinidochamado mysql-db,teremos:
class mysql-server { ... }
define mysql-db($schema, $user = $title, $password) {
Class[’mysql-server’] -> Mysql-db[$title]
exec { "$title-schema":
unless => "mysql -uroot $schema",
command => "mysqladmin -uroot create $schema",
path => "/usr/bin/",
}
exec { "$title-user":
unless => "mysql -u$user -p$password $schema",
command => "mysql -uroot -e \"GRANT ALL PRIVILEGES ON \
$schema.* TO ’$user’@’%’ \
IDENTIFIED BY ’$password’;\"",
99

## Página 118

5.1. Classesetiposdefinidos CasadoCódigo
path => "/usr/bin/",
require => Exec["$title-schema"],
}
}
include mysql-server
mysql-db { "loja":
schema => "loja_schema",
password => "lojasecret",
}
A sintaxe para declarar um tipo definido édefine <nome do
tipo>(<parâmetros>) { ... }. Nesse exemplo, o tipo definido
mysql-dbaceitatrêsparâmetros: $schema, $usere $password.Opa-
râmetro $user,quandonãoespecificado,teráomesmovalordoparâmetro
especial $title. Paraentenderovalordoparâmetro $title–quenão
precisaserdeclaradoexplicitamente–bastaolharasintaxedachamadana
qualdeclaramosumainstânciadotipodefinido: mysql-db { "loja":
schema => "loja_schema", ... }. Onomedorecursoqueinstan-
ciaotipodefinido,nestecaso loja,serápassadocomovalordoparâmetro
$title.Osoutrosparâmetrossãopassadosseguindoamesmasintaxeque
usamosemoutrosrecursosnativosdoPuppet:onomedoparâmetroeseu
valorseparadorporumaflecha =>.
Movemososdoisrecursos execquecriamo schemaeousuáriopara
dentrodotipodefinido.Substituímostambémtodasasreferências hardco-
dedpelorespectivosparâmetros,tomandocuidadoparausaraspasduplas
nasstringsparaqueoPuppetsaibaexpandirosvalorescorretamente. Para
poderusarotipodefinidomaisdeumavez,precisamosparametrizaronome
dosrecursos execetorná-losúnicosusandooparâmetro $title. Aúl-
timamodificaçãofoipromoveradeclaraç ãodadependênciacomaclasse
mysql-serverparaotopodotipodefinido. Comisso,oscomandosin-
dividuaisdentrodotipodefinidonãoprecisamdeclarardependênciascom
recursosexternos,facilitandoamanuten çãodessecódigonofuturo.
Usandoclassesetiposdefinidos,conseguimosrefatorarocódigoPuppet
paratorná-loumpoucomaisreutilizável. Noentanto,nãomudamosaor-
100

## Página 119

CasadoCódigo Capítulo5. Puppetalémdobásico
ganizaçãodosarquivosemsi.Tudocontinuadeclaradodentrodeumúnico
arquivo.Precisamosaprenderumaformamelhordeorganizarnossosarqui-
vos.
5.2 Empacotamento e distribuição usando mó-
dulos
OPuppetdefineumpadrãoparaempacotareestruturarseucódigo: módu-
los. Módulospossuemumaestruturapredefinidadediretóriosondevocê
devecolocarseusarquivos,assimcomoalgunspadrõesdenomenclatura.
MódulostambémsãoumaformadecompartilharcódigoPuppetcomaco-
munidade.OPuppetForge(http://forge.puppetlabs.com/)éumsitemantido
pelaPuppetLabsondevocêpodeencontrardiversosmódulosescritospela
comunidadeouregistrarummóduloquevocêescreveuequercompartilhar.
Dependendodasuaexperiênciacomdiferenteslinguagens,osequivalen-
tesaummóduloPuppetnascomunidadesRuby,Java,Pythone.NETseriam
umagem,um jar,um eggeuma DLL,respectivamente.Aestruturadedire-
tóriossimplificadaparaummóduloPuppeté:
<nome do módulo>/
files
...
manifests
init.pp
templates
...
tests
init.pp
Em primeiro lugar, o nome do diretório raiz define o nome do mó-
dulo. Odiretório manifestséomaisimportantepoislávocêcolocaseus
arquivosdemanifesto(comextensão .pp). Dentrodeledeveexistirpelo
menosumarquivochamado init.pp,queservecomopontodeentrada
paraomódulo. Odiretório filescontémarquivosdeconfiguraçãoestáti-
cosquepodemseracessadosdentrodeummanifestousandoumaURLes-
pecial: puppet:///modules/<nome do módulo>/<arquivo>. Odi-
101

## Página 120

5.2. Empacotamentoedistribuiçãousandomódulos CasadoCódigo
retóriotemplatescontémarquivosERBquepodemserreferenciadosden-
trodeummanifestousandoonomedomódulo: template('<nome do
módulo>/<arquivo ERB>').
Porfim,odiretório testscontémexemplosmostrandocomousarasclas-
sesetiposdefinidospelomódulo. Essestestesnãofazemnenhumtipode
verificaçãoautomatizada. Vocêpoderodá-losusandoocomando puppet
apply --noop.EssecomandosimulaumaexecuçãodoPuppetsemrealizar
nenhumaalteraçãonosistema.Casohajaalgumerrodesintaxeoudecompi-
lação,vocêirádetectá-losnasaídadocomando puppet apply --noop.
Nossapróximarefatoraçãoéumapreparaçãoantesdecriarmosomó-
dulo.Vamosquebraradefiniçãodaclasse mysql-serveredotipodefinido
mysql-dbemdoisarquivosseparadoschamados server.ppe db.pp,res-
pectivamente. Nomesmonívelemquecriamosoarquivo Vagrantfile,
vamoscriarumnovodiretório modulesondecolocaremosnossosmódu-
los.Dentrodele,criamosumnovomóduloparainstalaç ãoeconfiguraçãodo
MySQL,chamado mysql,criandoaseguinteestruturadediretóriosemo-
vendoosrespectivosarquivosparalá:
.
Vagrantfile
manifests
.keystore
context.xml
db.pp
devopsnapratica.war
server.xml
tomcat7
web.pp
modules
mysql
manifests
init.pp
db.pp
server.pp
templates
allow_ext.cnf
Percebaquecriamosumnovoarquivochamado init.ppnodiretório
102

## Página 121

CasadoCódigo Capítulo5. Puppetalémdobásico
modules/mysql/manifests.Essearquivoseráopontodeentradaparao
móduloeeledevedeclararumaclasse mysqlvaziaqueservecomo names-
paceparaorestodomódulo:
class mysql { }
Movemos também o arquivo allow_ext.cnf para o dire-
tório modules/mysql/templates. Por estar dentro da estru-
tura padrão do módulo, não precisamos mais referenciar otemplate
usando um caminho absoluto. O Puppet aceita o caminho no for-
mato <nome do módulo>/<arquivo> e sabe procurar otemplate
<arquivo> dentro do módulo escolhido. Podemos então mudar o re-
curso file no arquivo modules/mysql/manifests/server.pp
de template("/vagrant/manifests/allow_ext.cnf") para
template("mysql/allow_ext.cnf"):
class mysql::server {
exec { "apt-update": ... }
package { "mysql-server": ... }
file { "/etc/mysql/conf.d/allow_external.cnf":
...
content => template("mysql/allow_ext.cnf"),
...
}
service { "mysql": ... }
exec { "remove-anonymous-user": ... }
}
Perceba que renomeamos a classe mysql-server para
mysql::server. Esta é a nomenclatura padrão que o Puppet entende
paraimportarclassesetiposdentrodomesmomódulo. Damesmaforma,
devemostambémrenomearotipodefinido mysql-dbpara mysql::db
dentro do arquivomodules/mysql/manifests/db.pp, e alterar sua
dependênciacomaclasse mysql::server:
define mysql::db($schema, $user = $title, $password) {
Class[’mysql::server’] -> Mysql::Db[$title]
103

## Página 122

5.2. Empacotamentoedistribuiçãousandomódulos CasadoCódigo
...
}
Porfimpodemossimplificarbastanteoarquivo manifests/db.pp
parausaraclasse mysql::servereotipodefinido mysql::dbnonovo
módulo:
include mysql::server
mysql::db { "loja":
schema => "loja_schema",
password => "lojasecret",
}
Comisso,criamosummódulogenéricoquedisponibilizaumaclassepara
instalaroservidorMySQLeumtipodefinidoparacriarum schemaeum
usuárioparaacessá-lo.Podeparecerconfusoofatodeestarmosmudandoas
coisasdelugarsemnenhumamudan çanocomportamento,poréméexata-
menteporissoquerefatorarmoscódigo!Melhoramossuaestruturasemmo-
dificarocomportamentoexterno. Obenefícioéfacilitarotrabalhodema-
nutençãonofuturo,isolandocomponentesindividuaiseagrupandoaquilo
queérelacionado.Princípiosde designdesoftware–comoencapsulamento,
acoplamentoecoesão–tambémajudamamelhorarcódigodeinfraestrutura.
Paratestarquetudocontinuafuncionando,vocêpodedestruiresubir
amáquinavirtual dbnovamente,porémantesdissoéprecisofazeruma
pequenaalteraçãoparadizeraoVagrantquetemosumnovomóduloque
precisaestardisponívelquandooPuppetexecutar. Mudamosoarquivo
Vagrantfileparaadicionaraconfiguração module_pathnasVMs web
e db:
VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
...
config.vm.define :db do |db_config|
...
db_config.vm.provision "puppet" do |puppet|
puppet.module_path = "modules"
104

## Página 123

CasadoCódigo Capítulo5. Puppetalémdobásico
puppet.manifest_file = "db.pp"
end
end
config.vm.define :web do |web_config|
...
web_config.vm.provision "puppet" do |puppet|
puppet.module_path = "modules"
puppet.manifest_file = "web.pp"
end
end
...
end
AgoraqueocódigoPuppetparagerenciarainfraestruturadobancode
dadosestárefatorado,éhorademelhorarocódigoqueinstala,configurae
fazdeploydaaplicaçãonoservidorweb.
5.3 Refatorando o código Puppet do servidor
web
AgoraquesabemoscomorefatorarnossocódigoPuppet,vamoscriarum
novomódulochamado tomcatqueseráusadopeloservidorweb.Empri-
meirolugar,vamossimplesmentecriaraestruturadediretóriosdonovomó-
duloemoverosarquivosdodiretório manifestsparaosseguintesdiretó-
riosdentrode modules/tomcat:
.
Vagrantfile
manifests
.keystore
db.pp
devopsnapratica.war
web.pp
modules
mysql
...
105

## Página 124

5.3. RefatorandoocódigoPuppetdoservidorweb CasadoCódigo
tomcat
files
server.xml
tomcat7
manifests
templates
context.xml
Osúnicosarquivosrestantesnodiretório manifestssãoasdefinições
dosservidores( db.ppe web.pp),oarquivoWARcontentoaaplicaç ãoda
lojavirtualeoarquivo .keystorecontendoocertificadoSSL.Fizemosisso
paraseguirumprincípioimportantenodesenvolvimentodesoftware: sepa-
raçãoderesponsabilidades.Seolharmosoconteúdodoarquivo web.pp,
estamosmisturandorecursosmaisgenéricos–queinstalameconfiguramo
Tomcat–comrecursosespecíficosdalojavirtual. Sesimplesmentemover-
mostudoparaomesmomódulo,elenãoseráreutilizável.Pensesoboponto
devistaexternodeumaoutraequipenasuaempresaouacomunidadeem
geral:ummóduloqueinstalaeconfiguraoTomcatémuitomaisútildoque
ummóduloqueconfiguraoTomcatcomtodaalojavirtualinstalada.
Tendoissoemmente,oobjetivodorestodarefatoraç ãoseráextrairum
módulodoTomcatquenãopossuanenhumareferênciaacoisasespecíficas
dalojavirtual.Conformeformosmovendodefiniçõesderecursodoarquivo
web.ppparaomódulo tomcat,vamosmantercoisasespecíficasdaloja
virtualnomanifestodoservidoretornarosrecursosdomódulo tomcat
maisgenéricos.
Antesdecome çarmosaatacarosrecursosdoTomcat,vamoscome çar
comalgoumpoucomaissimples: extrairapartequeinstalaoclientedo
MySQLparaumanovaclassenomódulo mysql.Criamosumnovoarquivo
client.ppdentrode modules/mysql/manifests,comoconteúdo:
class mysql::client {
exec { "apt-update":
command => "/usr/bin/apt-get update"
}
package { "mysql-client":
ensure => installed,
106

## Página 125

CasadoCódigo Capítulo5. Puppetalémdobásico
require => Exec["apt-update"],
}
}
Novamente, a motivação é separação de responsabilidades: a classe
mysql::clientpodeserútilemoutroscontextos,mesmoquandovocê
nãoestádesenvolvendoumaaplicaçãoweb,portantocolocá-lanomódulo
mysqlfazmaissentidodoquenomódulo tomcat. Aospoucosestamos
começandoadesembaraçarocódigo.
Comissopodemoscome çaramudaroarquivo web.pp:vamosincluir
anovaclasse mysql::client,removerorecurso Exec[apt-update]
–quemigrouparaanovaclasse–eprecisamostambématualizartodasas
referênciasaosarquivosestáticosede templateparaonovocaminhodentro
domódulo:
include mysql::client
package { "tomcat7": ... }
file { "/var/lib/tomcat7/conf/.keystore": ... }
file { "/var/lib/tomcat7/conf/server.xml": ...
source => "puppet:///modules/tomcat/server.xml", ...
}
file { "/etc/default/tomcat7": ...
source => "puppet:///modules/tomcat/tomcat7", ...
}
service { "tomcat7": ... }
$db_host = "192.168.33.10"
$db_schema = "loja_schema"
$db_user = "loja"
$db_password = "lojasecret"
file { "/var/lib/tomcat7/conf/context.xml": ...
content => template("tomcat/context.xml"), ...
107

## Página 126

5.3. RefatorandoocódigoPuppetdoservidorweb CasadoCódigo
}
file { "/var/lib/tomcat7/webapps/devopsnapratica.war": ... }
Asúnicasreferênciasquedevemcontinuarapontandoparaocaminho
absolutosãoosrecursos File[/var/lib/tomcat7/conf/.keystore]
e File[/var/lib/tomcat7/webapps/devopsnapratica.war], já
quenãoosmovemosparadentrodomódulo.
Agora vamos começar a mover partes do código do arquivo
web.pp para novas classes e tipos definidos dentro do módulo
tomcat. Criaremos um novo arquivo server.pp dentro do dire-
tório modules/tomcat/manifests e iremos mover os seguintes
recursosdoarquivo web.ppparaumanovaclassequechamaremosde
tomcat::sever:
class tomcat::server {
package { "tomcat7": ... }
file { "/etc/default/tomcat7": ... }
service { "tomcat7": ... }
}
Paraexporestanovaclassenomódulonovo,precisamoscriartambém
umarquivo init.ppdentrodomesmodiretório,contendoinicialmente
umaúnicaclassevazia: class tomcat { }.Comisso,podemosalteraro
arquivo web.pp,removendoosrecursosqueforammovidosesubstituindo-
osporum includedanovaclasse tomcat::server:
include mysql::client
include tomcat::server
file { "/var/lib/tomcat7/conf/.keystore": ... }
file { "/var/lib/tomcat7/conf/server.xml": ... }
$db_host = "192.168.33.10"
$db_schema = "loja_schema"
$db_user = "loja"
$db_password = "lojasecret"
108

## Página 127

CasadoCódigo Capítulo5. Puppetalémdobásico
file { "/var/lib/tomcat7/conf/context.xml": ... }
file { "/var/lib/tomcat7/webapps/devopsnapratica.war": ... }
Percebaqueaindanãomovemostodososrecursosdotipo fileparaa
novaclasse,poiselespossuemreferênciaseconfiguraçõesquesãobastante
específicasdanossaaplicação:
• Oarquivo.keystorepossuiocertificadoSSLdalojavirtual.Nãoé
umaboaideiadistribuirnossocertificadoemummódulogenéricodo
Tomcatqueoutraspessoasouequipespodemreutilizar.
• Oarquivoserver.xmlpossuiconfiguraçõesparahabilitarHTTPS
contendoinformaçõessecretasquetambémsãoespecíficasdalojavir-
tual.
• Oarquivocontext.xmlconfiguraosrecursosJNDIdeacessoao
schemadobancodedadosdalojavirtual.
• Porfim,oarquivodevopsnapratica.warcontémnossaaplicação.
ParatornaromódulodoTomcatmaisgenérico,vamosprimeiroresol-
veroproblemadaconfiguraçãoSSLedoarquivo .keystore. Dentrodo
arquivodeconfiguração server.xml,emvezdeassumirqueonomedo
keystoreeasenhadeacessoserãosempreosmesmos,vamostransformá-lo
emumtemplateepassaressasinformaçõesparaaclasse tomcat::server.
Paraentenderoresultadodesejado,come çaremosmostrandoasalterações
noarquivo web.pp:
include mysql::client
$keystore_file = "/etc/ssl/.keystore"
$ssl_connector = {
"port" => 8443,
"protocol" => "HTTP/1.1",
"SSLEnabled" => true,
"maxThreads" => 150,
"scheme" => "https",
"secure" => "true",
109

## Página 128

5.3. RefatorandoocódigoPuppetdoservidorweb CasadoCódigo
"keystoreFile" => $keystore_file,
"keystorePass" => "secret",
"clientAuth" => false,
"sslProtocol" => "SSLv3",
}
$db_host = "192.168.33.10"
$db_schema = "loja_schema"
$db_user = "loja"
$db_password = "lojasecret"
file { $keystore_file:
mode => 0644,
source => "/vagrant/manifests/.keystore",
}
class { "tomcat::server":
connectors => [$ssl_connector],
require => File[$keystore_file],
}
file { "/var/lib/tomcat7/conf/context.xml": ... }
file { "/var/lib/tomcat7/webapps/devopsnapratica.war": ... }
Vamosdiscutircadaumadasmudan ças:emprimeirolugar,mudamoso
diretóriodoarquivo .keystoreparaumlugarmaisgenérico,foradoTom-
cat,esalvamossualocalizaç ãoemumanovavariável $keystore_file.
Comisso,removemosasreferênciasedependênciascomoTomcatdore-
curso File[/etc/ssl/.keystore]. Asegundamudançaimportanteé
quetornamosaclasse tomcat::serverparametrizada,passandoumnovo
parâmetro connectorsquerepresentaum arraydeconectoresquepreci-
samserconfigurados.
Esseexemplotambémserveparamostrarduasnovasestruturasdedados
reconhecidaspeloPuppet: arraysehashes.Umarrayéumalistaindexadade
itens,enquantoum hashéumaespéciededicionárioqueassociaumachave
aumvalor. Aopassaralistadeconectorescomoumparâmetro,podemos
mover o recurso File[/var/lib/tomcat7/conf/server.xml]
para dentro da classe tomcat::server, no arquivo
110

## Página 129

CasadoCódigo Capítulo5. Puppetalémdobásico
modules/tomcat/manifests/server.pp:
class tomcat::server($connectors = []) {
package { "tomcat7": ... }
file { "/etc/default/tomcat7": ... }
file { "/var/lib/tomcat7/conf/server.xml":
owner => root,
group => tomcat7,
mode => 0644,
content => template("tomcat/server.xml"),
require => Package["tomcat7"],
notify => Service["tomcat7"],
}
service { "tomcat7": ... }
}
Percebaqueasintaxededeclaraçãodaclassemudouparaaceitaronovo
parâmetro $connectors,quepossuiumvalorpadrãocorrespondentea
umalistavazia. Comoagoraoconteúdodoarquivo server.xmlprecisa
serdinâmico,precisamosmovê-lododiretório modules/tomcat/files
paraodiretório modules/tomcat/templates,substituindotambéma
definiçãodorecursoparausaro templatenageraçãodoarquivo. Porfim,
precisamosmudaroconteúdodoarquivo server.xmlparaconfiguraros
conectoresdinamicamente:
<?xml version=’1.0’ encoding=’utf-8’?>
<Server port="8005" shutdown="SHUTDOWN">
...
<Service name="Catalina">
...
<Connector port="8080" protocol="HTTP/1.1"
connectionTimeout="20000"
URIEncoding="UTF-8"
redirectPort="8443" />
<%- connectors.each do |c| -%>
<Connector
111

## Página 130

5.3. RefatorandoocódigoPuppetdoservidorweb CasadoCódigo
<%= c.sort.map{|k,v| "#{k}=’#{v}’"}.join(" ") %> />
<%- end -%>
...
</Service>
</Server>
Perceba que agora nenhum conector referencia qualquer caracterís-
tica específica da nossa aplicação. Usando um pouco de Ruby notem-
plate server.xmlconseguimos transformar em dados o que antes es-
tava hard-coded. A parte interessante é a linha:c.sort.map{|k,v|
"#{k}=’#{v}’"}.join(” “).Aoperação sortgarantequesempreire-
mositerarno hashnamesmaordem.Aoperação maptransformacadapar
dechave/valordo hashemumastringformatadacomoumatributoXML.Por
exemplo:umhash {"port"=> "80", "scheme"=> "http"}setrans-
formaránalista["port='80'", "scheme='http'"].Aoperação join
juntatodasas stringsdessalistaemumaúnica string,separando-ascomum
espaço.Oresultadofinaléastring: "port='80'scheme='http'".
Agora que resolvemos o problema da configuraç ão
SSL, podemos usar o mesmo truque para mover o recurso
File[/var/lib/tomcat7/conf/context.xml] para dentro da
classe tomcat::server. Novamentecomeçamospelamudan çadesejada
noarquivo web.pp:
include mysql::client
$keystore_file = "/etc/ssl/.keystore"
$ssl_conector = ...
$db = {
"user" => "loja",
"password" => "lojasecret",
"driver" => "com.mysql.jdbc.Driver",
"url" => "jdbc:mysql://192.168.33.10:3306/loja_schema",
}
file { $keystore_file: ... }
class { "tomcat::server":
112

## Página 131

CasadoCódigo Capítulo5. Puppetalémdobásico
connectors => [$ssl_conector],
data_sources => {
"jdbc/web" => $db,
"jdbc/secure" => $db,
"jdbc/storage" => $db,
},
require => File[$keystore_file],
}
file { "/var/lib/tomcat7/webapps/devopsnapratica.war": ... }
Seguindo o mesmo padrão, adicionamos um novo parâmetro
data_sources na classe tomcat::server e passamos umhash
contendoosdadosdeconfiguraç ãodecada datasource. Movemostam-
bém o recurso File[/var/lib/tomcat7/conf/context.xml]
para a classe tomcat::server no arquivo
modules/tomcat/manifests/server.pp:
class tomcat::server($connectors = [], $data_sources = []) {
package { "tomcat7": ... }
file { "/etc/default/tomcat7": ... }
file { "/var/lib/tomcat7/conf/server.xml": ... }
file { "/var/lib/tomcat7/conf/context.xml":
owner => root,
group => tomcat7,
mode => 0644,
content => template("tomcat/context.xml"),
require => Package["tomcat7"],
notify => Service["tomcat7"],
}
service { "tomcat7": ... }
}
Precisamostambémalteraroarquivode template context.xmlpara
gerarosrecursosJNDIdinamicamente:
<?xml version=’1.0’ encoding=’utf-8’?>
<Context>
113

## Página 132

5.3. RefatorandoocódigoPuppetdoservidorweb CasadoCódigo
<!-- Default set of monitored resources -->
<WatchedResource>WEB-INF/web.xml</WatchedResource>
<%- data_sources.sort.each do |data_source, db| -%>
<Resource name="<%= data_source %> " auth="Container"
type="javax.sql.DataSource" maxActive="100"
maxIdle="30"
maxWait="10000"
username="<%= db[’user’] %> "
password="<%= db[’password’] %> "
driverClassName="<%= db[’driver’] %> "
url="<%= db[’url’] %> "/>
<%- end -%>
</Context>
Comissoconseguimosrefatorarbastantenossocódigo,tornado-osmais
organizadoemaisfácildeserreaproveitado.Nessemomento,aestruturade
diretórioscomosnovosmódulosdeveser:
.
Vagrantfile
manifests
.keystore
db.pp
devopsnapratica.war
web.pp
modules
mysql
manifests
client.pp
db.pp
init.pp
server.pp
templates
allow_ext.cnf
tomcat
files
tomcat7
manifests
114

## Página 133

CasadoCódigo Capítulo5. Puppetalémdobásico
init.pp
server.pp
templates
context.xml
server.xml
5.4 Separação de responsabilidades: infraes-
trutura vs. aplicação
Atéagora,estamosnosfor çandoaescrevermódulosquesejamgenéricose
reaproveitáveis. Noentanto,ocódigoquerestounosmanifestos web.pp,
db.ppeosarquivossoltos .keytoree devopsnapratica.warainda
parecemummaucheiro.Umapráticacomumpararesolveresseproblemaé
criarmódulosespecíficosparaaaplicaç ão. Masissonãocontradizosargu-
mentosqueviemosfazendoatéagora?
Separarmódulosdeinfraestruturadosmódulosdeaplicaçãoéumaforma
deaplicaroprincípiodaseparaçãoderesponsabilidadesemoutronível.Essa
éumaformadecomposição:osmódulosdeaplicaçãoaindautilizamosmó-
dulosdeinfraestrutura,quecontinuamreaproveitáveiseindependentes. A
figura5.1mostraaestruturaedependênciasdesejadasentrenossosmódulos.
Figura5.1:Módulosdeaplicaçãovs.módulosdeinfraestrutura
Oúltimomóduloqueiremoscriarnestecapítuloseráresponsávelpela
instalaçãoeconfiguraçãodalojavirtual.Paraisso,precisamosexpandirnossa
estruturadediretóriosearquivosdamesmaformaquefizemosanterior-
mente,masdessavezparaonovomódulo loja_virtual:
115

## Página 134

5.4. Separaçãoderesponsabilidades:infraestruturavs.aplicaç ão CasadoCódigo
.
Vagrantfile
manifests
db.pp
web.pp
modules
loja_virtual
files
.keystore
devopsnapratica.war
manifests
db.pp
init.pp
params.pp
web.pp
mysql
...
tomcat
...
Movemososarquivos .keystoree devopsnapratica.warparao
diretório modules/loja_virtual/filesecriamosquatroarquivosde
manifestoparacolocarmosasnovasclassesdomódulo loja_virtual:
db.pp, init.pp, params.ppe web.pp. Oarquivo init.ppsimples-
mentedeclaraumaclassevaziaparaservirde namespaceraizparaorestodo
módulo:
class loja_virtual { }
Oarquivo db.ppirádefinirumanovaclasse loja_virtual::db,com
oconteúdomovidoquasesemalteraçõesdoarquivo manifest/db.pp:
class loja_virtual::db {
include mysql::server
include loja_virtual::params
mysql::db { $loja_virtual::params::db[’user’]:
schema => $loja_virtual::params::db[’schema’],
password => $loja_virtual::params::db[’password’],
116

## Página 135

CasadoCódigo Capítulo5. Puppetalémdobásico
}
}
Aúnicadiferençaéquemovemososvaloresdousuário,senhae schema
dobancodedadosparaumaoutraclasse loja_virtual::paramsdentro
domesmomódulo.EsteéumpadrãocomumemmódulosPuppet,emque
vocêcentralizaosparâmetrosemumaúnicaclasseparanãoprecisarduplicá-
losdentrodomódulo.
Osparâmetrosdefinidosnaclasse loja_virtual::paramstambém
respeitamseu namespace,porissoprecisamosreferenciá-losusandoocami-
nhocompleto $loja_virtual::params::db['user']emvezdesim-
plesmente $db['user'].Paraentendermelhorcomoessesparâmetrosfo-
ramdefinidos,bastaolharoconteúdodoarquivo params.ppquedefinea
novaclasse loja_virtual::params:
class loja_virtual::params {
$keystore_file = "/etc/ssl/.keystore"
$ssl_connector = {
"port" => 8443,
"protocol" => "HTTP/1.1",
"SSLEnabled" => true,
"maxThreads" => 150,
"scheme" => "https",
"secure" => "true",
"keystoreFile" => $keystore_file,
"keystorePass" => "secret",
"clientAuth" => false,
"sslProtocol" => "SSLv3",
}
$db = {
"user" => "loja",
"password" => "lojasecret",
"schema" => "loja_schema",
"driver" => "com.mysql.jdbc.Driver",
"url" => "jdbc:mysql://192.168.33.10:3306/",
}
117

## Página 136

5.4. Separaçãoderesponsabilidades:infraestruturavs.aplicaç ão CasadoCódigo
}
Esse é praticamente o mesmo conteúdo que tínhamos no arquivo
manifests/web.pp. Aúnicadiferen çafoiaadiçãodachave schema
aohash $db, cujovalorestavaanteriormenteembutidonofinaldopa-
râmetro $db['url']. Fizemos isto para poder reaproveitar a mesma
estrutura nas classes loja_virtual::db e loja_virtual::web.
Com esta alteração, você precisa também mudar o arquivo de template
modules/tomcat/templates/context.xml para usar a nova chave
schema:
...
<Context>
...
<Resource ... url="<%= db[’url’] + db[’schema’] %> "/>
...
</Context>
Como a definição dos parâmetros já está disponível em uma única
classe, fica fácil de entender o código movido e alterado na nova classe
loja_virtual::web:
class loja_virtual::web {
include mysql::client
include loja_virtual::params
file { $loja_virtual::params::keystore_file:
mode => 0644,
source => "puppet:///modules/loja_virtual/.keystore",
}
class { "tomcat::server":
connectors => [$loja_virtual::params::ssl_connector],
data_sources => {
"jdbc/web" => $loja_virtual::params::db,
"jdbc/secure" => $loja_virtual::params::db,
"jdbc/storage" => $loja_virtual::params::db,
},
require => File[$loja_virtual::params::keystore_file],
118

## Página 137

CasadoCódigo Capítulo5. Puppetalémdobásico
}
file { "/var/lib/tomcat7/webapps/devopsnapratica.war":
owner => tomcat7,
group => tomcat7,
mode => 0644,
source => "puppet:///modules/loja_virtual/
devopsnapratica.war",
require => Package["tomcat7"],
notify => Service["tomcat7"],
}
}
Damesmaformaquefizemosnaclasse loja_virtual::db,incluímos
aclasse loja_virtual::paramseusamosocaminhocompletoparaos
parâmetros.Tambémmudamososrecursosdotipo fileparareferenciaros
arquivosusandoocaminhorelativoaomóduloaoinvésdocaminhoabsoluto
nosistemadearquivos.
Comisso,nossonovomóduloestácompletoeoconteúdodosarquivos
demanifestodecadaservidorficabastantesimplificado:
# Conteúdo do arquivo manifests/web.pp:
include loja_virtual::web
# Conteúdo do arquivo manifests/db.pp:
include loja_virtual::db
5.5 Puppet forge: reutilizando módulos da co-
munidade
Conformeodesenvolvimentodeumaaplicaçãovaiprogredindoeosistema
cresce,écomumtambémaumentaronúmerodeclasses,pacotesebibliote-
casusadasnoprojeto. Comissoganhamosumanovapreocupaç ão: geren-
ciamentodedependências. Esseéumproblematãocomumquediversas
comunidadesdedesenvolvimentocriaramferramentasespecíficasparalidar
comele:nacomunidadeRuby,oBundlergerenciadependênciasentre gems;
nacomunidadeJava,oMaveneoIvygerenciam jarsesuasdependências;até
119

## Página 138

5.5. Puppetforge:reutilizandomódulosdacomunidade CasadoCódigo
mesmoadministradoresdesistemausamgerenciadoresdepacotescomoo
dpkgouo rpmparacuidardasdependênciasnainstalaçãodesoftware.
Ocódigodeautomaçãodeinfraestruturadalojavirtualtambémestáco-
meçandoamostrarproblemasnogerenciamentodesuasdependências. Já
temostrêsmódulosPuppetecriamosumadependênciaindesejadaentrere-
cursosnosmódulos mysqle tomcat. Sevocêprestaratenção,orecurso
Exec[apt-update]édeclaradoduasvezesnasclasses mysql::servere
mysql::clienteéusadoemtrêslugaresdiferentes:nasprópriasclassese
naclasse tomcat::server.
Demodogeral,dependênciassãomaissimplesdegerenciarquandoa
declaraçãoeousoestãomaispróximos. Umadependênciaentrerecursos
declaradosnomesmoarquivoémelhorqueumadependênciaentrerecur-
sosdeclaradosemarquivosdiferentes;umadependênciaentrearquivosdi-
ferentesdomesmomóduloémelhorqueumadependênciacomrecursosde
módulosdiferentes.
Dojeitoqueocódigoestá,omódulo tomcattemumadependência
diretacomumrecursoespecíficodomódulo mysql.Sealojavirtualdeixar
deusaromódulo mysql,nãoserápossívelinstalareconfiguraroTomcat.
Essetipodedependênciacriaumacoplamentoforteentreosmódulos mysql
e tomcat,tornandomaisdifícilutilizá-losindependentemente.
Idealmente,nãoprecisaríamosdeclararnenhumrecursoespecíficodo
APT.Oúnicomotivodetermosdeclaradoesserecursonocapítulo 4foi
porqueprecisávamosatualizaroíndicedoAPT–executandoum apt-get
update–antesdeinstalarqualquerpacote.Issonãoéumanecessidadedo
MySQLoudoTomcat,massimumproblemaqueapareceassimqueoPuppet
tentainstalaroprimeiropacotenosistema.
Paramelhorarnossocódigoeremoveressadependênciaindesejada,va-
mosaproveitarparaaprendercomousarmódulosdacomunidade. Vamos
usarummódulodaPuppetLabsquefoiescritoparalidarcomoAPTdeforma
maisgeral.
Ao ler a documentação do módulo (https://github.com/puppetlabs/
puppetlabs-apt)vemosqueeleexpõeaclasse aptequeelapossuiumparâ-
metro always_apt_updatequefazoqueprecisamos:
class { ’apt’:
120

## Página 139

CasadoCódigo Capítulo5. Puppetalémdobásico
always_apt_update => true,
}
Comisso, garantimosqueoPuppetirárodarocomando apt-get
updatetodavezqueforexecutado. Noentanto,precisamosgarantirque
ocomandorodeantesdainstalaçãodequalquerpacotenosistema.Parade-
clararessadependência,vamosaprenderumanovasintaxedoPuppet:
Class[’apt’] -> Package <| |>
Aflecha ->impõeumarestriçãonaordemdeexecuç ãodosrecursos.
Damesmaformaqueoparâmetro requireindicaumadependênciaentre
doisrecursos,aflecha ->garantequeorecursodoladoesquerdo–nesse
casoaclasse apt–sejaexecutadoantesdorecursodoladodireito.Asintaxe
<| |>–tambémconhecidacomooperadorespaçonave–éumcoletorde
recursos. Ocoletorrepresentaumgrupoderecursoseécompostode:um
tipoderecurso,ooperador <|,umaexpressãodebuscaopcionaleooperador
|>.Comodeixamosaexpressãodebuscaembranco,selecionamostodosos
recursosdotipo package.
Juntando essas duas informações temos um código mais genérico
que garante que o Puppet irá executar umapt-get update an-
tes de tentar instalar qualquer pacote no sistema. Com isso, po-
demos alterar a nossa classeloja_virtual, declarada no arquivo
modules/loja_virtual/manifests/init.pp:
class loja_virtual {
class { ’apt’:
always_apt_update => true,
}
Class[’apt’] -> Package <| |>
}
Podemosagoraremoverasreferênciasaorecurso Exec[apt-update]
dosmódulos mysqle tomcat,assimcomoorecursoemsi. Oarquivo
modules/mysql/manifests/client.ppficabemmaissimplificado:
121

## Página 140

5.5. Puppetforge:reutilizandomódulosdacomunidade CasadoCódigo
class mysql::client {
package { "mysql-client":
ensure => installed,
}
}
Damesmaforma,oarquivo modules/mysql/manifests/server.pp
tambémficamaisenxuto:
class mysql::server {
package { "mysql-server":
ensure => installed,
}
file { "/etc/mysql/conf.d/allow_external.cnf": ... }
service { "mysql": ... }
exec { "remove-anonymous-user": ... }
}
Por fim, removemos a dependência indesejada
na classe tomcat::server alterando o arquivo
modules/tomcat/manifests/server.pp:
class tomcat::server($connectors = [], $data_sources = []) {
package { "tomcat7":
ensure => installed,
}
file { "/etc/default/tomcat7": ... }
file { "/var/lib/tomcat7/conf/server.xml": ... }
file { "/var/lib/tomcat7/conf/context.xml": ... }
service { "tomcat7": ... }
}
Paracompletaressarefatoração,precisamosgarantirqueocódigoque
adicionamosàclasse loja_virtualsejaexecutadonosservidores web
e db. Para isso basta incluí-la no começo da declaração das classes
loja_virtual::webe loja_virtual::db:
122

## Página 141

CasadoCódigo Capítulo5. Puppetalémdobásico
# Conteúdo do arquivo modules/loja_virtual/manifests/web.pp:
class loja_virtual::web {
include loja_virtual
...
}
# Conteúdo do arquivo modules/loja_virtual/manifests/db.pp:
class loja_virtual::db {
include loja_virtual
...
}
Pronto,nossarefatoraçãoestácompleta.Refatoraçõesalteramaestrutura
internadocódigosemalterarseucomportamentoexterno[10].Paragarantir
quenossosservidoresaindasãoconfiguradoscorretamentedepoisdetodas
asalteraçõesfeitasnestecapítulo,vamosreprovisioná-losdozero,primeiro
destruindooservidor db:
$ vagrant destroy db
db: Are you sure you want to destroy the ’db’ VM? [y/N] y
==> db: Forcing shutdown of VM...
==> db: Destroying VM and associated drives...
==> db: Running cleanup tasks for ’puppet’ provisioner...
Porém,aotentarsubiroservidor dbnovamente,encontramosumpro-
blemainesperado:
$ vagrant up db
Bringing machine ’db’ up with ’virtualbox’ provider...
...
Puppet::Parser::AST::Resource failed with error ArgumentError:
Could not find declared class apt at /tmp/vagrant-puppet-2/
modules-0/loja_virtual/manifests/init.pp:4 on node precise32
EsseerroindicaqueoPuppetnãoconseguiuencontraraclasse apt,
poisnãoinstalamosomódulodaPuppetLabs. Aformamaissimplesde
instalarummódulodacomunidadeéusandoaprópriaferramentadeli-
nha de comando do Puppet, executando:puppet module install
<nome-do-módulo>.Issoiráinstalaronovomóduloesuasdependências
123

## Página 142

5.5. Puppetforge:reutilizandomódulosdacomunidade CasadoCódigo
no modulepathpadrão,tornando-osdisponíveisnapróximaexecuç ãode
um puppet apply.
Naatualconfiguração,nãorodamos puppet applydiretamente.Esta-
mosusamosoVagrantparagerenciaraexecuç ãodoPuppet.Alémdisso,o
móduloprecisaserinstaladodentrodamáquinavirtual,oquetornaopro-
cessodeprovisionamentoumpoucomaiscomplicadosequisermosexecutar
umcomandoantesdoVagrantiniciaraexecuç ãodoPuppet.
Conformeonúmerodemódulosesuasdependênciasaumentam,fica
maisdifícilinstalá-losumporumusandoalinhadecomando.Abiblioteca
LibrarianPuppet (http://librarian-puppet.com/)foicriadajustamentepara
resolveresseproblema.Vocêdeclaratodasasdependênciasemumúnicoar-
quivo PuppetfileeoLibrarianPuppetresolveeinstalaosmódulosnas
versõesespecificadasemumdiretórioisolado.Elefuncionadeformasimilar
aoBundler,paraquemconheceoecossistemaRuby.
Nomesmonívelemqueestáoarquivo Vagrantfile,vamoscriarum
novodiretório librariancontendooarquivo Puppetfilecomose-
guinteconteúdo:
forge "http://forge.puppetlabs.com"
mod "puppetlabs/apt", "1.4.0"
AprimeiralinhadeclaraqueusaremosoPuppetLabsForgecomofonte
oficialpararesolverebaixarosmódulos. Asegundalinhadeclaraumade-
pendênciacomomódulo pupppetlabs/aptnaversão 1.4.0.
ParaexecutaroLibrarianPuppetantesdeusaroPuppet,vamosinstalar
umnovo plugindoVagrant. Pluginssãoumaformadeestenderocompor-
tamentobásicodoVagrant,permitindoqueacomunidadeescrevaecom-
partilhediversasmelhorias.Outrosexemplosde pluginsdoVagrantsão:su-
porteaoutrasferramentasdevirtualizaç ão, máquinasvirtuaisnanuvem,
etc. ParainstalaroplugindoLibrarianPuppet(https://github.com/mhahn/
vagrant-librarian-puppet/),bastaexecutar:
$ vagrant plugin install vagrant-librarian-puppet
Installing the ’vagrant-librarian-puppet’ plugin. This can
take a few minutes...
Installed the plugin ’vagrant-librarian-puppet (0.6.0)’!
124

## Página 143

CasadoCódigo Capítulo5. Puppetalémdobásico
ComoestamosgerenciandoosmódulosdoLibrarianPuppetemumdire-
tórioisolado,precisamosconfigurá-lonoarquivo Vagrantfileeadicioná-
lono modulepath:
VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
...
config.librarian_puppet.puppetfile_dir = "librarian"
config.vm.define :db do |db_config|
...
db_config.vm.provision "puppet" do |puppet|
puppet.module_path = ["modules", "librarian/modules"]
...
end
end
config.vm.define :web do |web_config|
...
web_config.vm.provision "puppet" do |puppet|
puppet.module_path = ["modules", "librarian/modules"]
...
end
end
...
end
Comisso,podemostentarprovisionaramáquinavirtual dbnovamentee,
dessavez,setudodercerto,veremosqueapósnossocódigodeautomaç ãode
infraestruturacontinuafuncionandomesmoapóstodasasrefatora çõesfeitas
atéaqui:
$ vagrant reload db
==> db: Checking if box ’hashicorp/precise32’ is up to date...
...
$ vagrant provision db
==> db: Installing Puppet modules with Librarian-Puppet...
==> db: Running provisioner: puppet...
125

## Página 144

5.6. Conclusão CasadoCódigo
Running Puppet with db.pp...
...
notice: Finished catalog run in 56.78 seconds
5.6 Conclusão
Missãocumprida! Comparadocomocome çodocapítulo,nãoapenasme-
lhoramosaestruturaeaorganizaçãodonossocódigocomotambémapren-
demosnovasfuncionalidadesecaracterísticasdoPuppet. Osarquivosque
estavamgrandeseconfusosterminaramocapítulocomapenasumalinhade
códigocada.Agoraosarquivosdemanifestorepresentamoqueseráinstalado
emcadaservidor.Aprendemostambémcomoreutilizarmódulosdacomu-
nidadeecomogerenciardependênciasutilizandoferramentasdecódigolivre
comooLibrarianPuppeteorespectivo plugindoVagrant.
Comoumexercíciopararefor çarseuentendimento,imaginesequisésse-
mosinstalaralojavirtualcompletanumúnicoservidor:quãodifícilseriaesta
tarefaagoraquetemosmódulosbemdefinidos?Umoutroexercíciointeres-
santeéusaroqueaprendemossobreoPuppetparaautomatizarainstalaç ão
econfiguraçãodoservidordemonitoramentodocapítulo 3.
Maséclaroqueaindaháespaçoparamelhoria. Escrevercódigolimpo
edefácilmanuten çãoémaisdifícilquesimplesmenteescrevercódigoque
funciona.Precisamosrefletiredecidirquandoocódigoestábomosuficiente
paraseguiremfrente.
Porenquanto,seguindooespíritodemelhoriacontínua,decidimosparar
derefatorarmesmosabendoqueaindaexistemmauscheirosnonossocódigo.
Emparticular,entregarumarquivoWARestáticocomopartedeummódulo
Puppetsófuncionasevocênuncaprecisaralterá-lo. Sabemosqueissonão
éverdadenamaioriadassituações,entãoiremosrevisitaressadecisãonos
próximoscapítulos.Masantesdissoprecisamosaprenderumaformasegurae
confiáveldegerarumnovoarquivoWARtodavezquefizermosumaalteração
nocódigodalojavirtual.
126

## Página 145

Capítulo6
Integraçãocontínua
Sevocêéumdesenvolvedordesoftware,atéagoradeveteraprendidoum
poucosobreomundodeoperações:subimosoambientedeproduç ão,fize-
mosbuildedeploydaaplicação,configuramosumsistemademonitoramento
eescrevemoscódigoPuppetparaautomatizarainfraestrutura.Deixamosde
ladooqueaconteceantesdaaplicaçãoestarempacotadaemumarquivoWAR
parafocarnoladooperacionalquandotentamoscolocarumsistemaempro-
dução.
AessênciadeDevOpsémelhoraracolaboraçãoentreequipesdedesen-
volvimentoeoperaçõesentãoéhoradeolharumpoucomaisparaoladodo
desenvolvimento.Escrevercódigoéumadasprincipaisatividadesdeumde-
senvolvedordesoftwareeDevOpspodeajudaratornaroprocessodeentrega
maisconfiável.Vamosdiscutircomolidarcommudan çasnocódigo-fontede
formasegura,levando-asdesdeum commitatéumpacotequepodeserim-
plantadoemprodução.

## Página 146

6.1. Práticasdeengenhariaágil CasadoCódigo
6.1 Práticas de engenharia ágil
Muitasempresascome çamsuaado çãodemétodoságeisusandoScrum[14]
ouKanban[2],processosquefocamnaspráticasdegestãocomo:reuniões
empé,quadrodetarefas,divisãodotrabalhoemhistórias,planejamentoem
iterações,ouretrospectivas.Noentanto,praticantesdemétodoságeisexperi-
entessabemqueumaado çãodesucessonãopodedeixardeladoaspráticas
deengenhariaágilqueafetamdiretamenteaqualidadedosoftwaredesenvol-
vido.
Aprogramaçãoextrema–ExtremeProgramming ouXP–foiumadas
primeirasmetodologiaságeisquerevolucionouaformacomosoftwareera
desenvolvidonofinaldadécadade90. Nolivroseminal ExtremeProgram-
mingExplained[4],KentBeckdefiniuosvalores,princípiosepráticasdame-
todologia,cujoprincipalobjetivoépermitirodesenvolvimentodesoftware
dealtaqualidadequeseadaptaarequisitosvagosouemconstantemudan ça.
DentreaspráticasdeengenhariaintroduzidasporXPestão:refatoraç ão,
TDD,propriedadecoletivadecódigo, designincremental,programaçãoem
pares,padrõesdecódigoeintegraç ãocontínua.Enquantoalgumaspráticas
aindageramcontrovérsia,muitasdelasjápodemserconsideradasnormais
hojeemdia,sendoadotadasporumgrandenúmerodeempresaseequipes.
Emparticular,apráticadaintegra çãocontínuafoiumadasmaisbemsuce-
didasporajudararesolverumgrandeproblemadosprocessosdedesenvol-
vimentodesoftwareexistentesatéentão:afasedeintegraç ãotardia.
Nósjádiscutimosnocapítulo 1oqueacontecequandodeixamospara
integraretestarsomentena“últimamilha”. Porissoéimportantededicar
umcapítulodeumlivrodeDevOpsàpráticadaintegraç ãocontínua.Porém,
antesdedefinirmosoqueelaéecomoimplementá-la,precisamosfalarsobre
algunsdeseuselementosbásicosparaentenderporqueelafunciona.
6.2 Começando pelo básico : controle de ver-
sões
Independentedevocêtrabalharisoladamenteouemequipe,oprimeirosinal
deumprogramadorbemdisciplinadoéaformacomoelegerenciamudan ças
nocódigo-fontedoseusistema.Quandoeuestavaaprendendoaprogramar,
128

## Página 147

CasadoCódigo Capítulo6. Integraçãocontínua
escreviacódigodescartávelesimplesmentemantinhaumacópiadetodosos
arquivosnomeucomputador.Issofuncionouatéaprimeiravezqueprecisei
reverterocódigoparaaúltimaversãoestável.Eutinhafeitotantasmudan ças
deumasóvezqueocódigoficounumaversãoinconsistente,quenãocom-
pilavaenãofuncionava.Tudoqueeuqueriaeraterumamáquinadotempo
quemelevasseparaaúltimaversãoquefuncionava.
Quandocomeceiatrabalharemequipe,oproblemapiorou. Euemeus
colegasqueríamosfazermudan çasempartesdiferentesdosistema,mascomo
cadaumtinhaumacópiacompletadocódigo,precisávamoscompartilhar
diretórios,mandare-mailcomarquivosanexados,ouusardisquetes(sim,
naquelaépocaissoeracomum)paratransferirarquivosparaláeparacá.Não
precisodizerqueessaeraumatarefaárduaecometíamoserrosesporádicos
quetomavamumbomtempoparadescobriroquefaltououcomoresolver
conflitos.
Minhavidamudouquandodescobriqueesseproblemajátinhasidore-
solvidoporpessoasmaisinteligenteseexperientesqueeu. Elascriaramos
sistemasdecontroledeversões ,ferramentasqueatuamcomoumrepositó-
riocentraldecódigoemantêmumhistóricodetodasasmudan çasfeitasno
seusistema.Cadamudan çaéchamadadeum commit,queagrupaosarquivos
alteradoscomoautordamudan çaeumamensagemexplicativa.Issopermite
quevocênaveguenohistóricodoprojetoesaibaquemmudouoque,quando,
eporquê.Quandoduaspessoastentamalteraromesmoarquivo,essasfer-
ramentastentamresolveroconflitoautomaticamente,porémlheavisamse
precisaremdeajudahumana.
Hojeemdianãoexistemotivoparanãousarumsistemadecontrolede
versões.Umadasferramentasmaispopulareséo Git(http://git-scm.com/),
umsistemadistribuídoquenãoimpõeanecessidadedeexistirumúnicore-
positóriocentralparatodosos commitsdoprojeto.Porserdistribuído,cada
desenvolvedorpoderodarumservidorlocalemsuaprópriamáquina.Oque
otornapoderosoéquecadaservidorsabeenviarseuhistóricolocalparaou-
trosservidores,permitindoquevocêcompartilhecódigodeformaeficiente.
Aescolhadeumservidorcentraléapenasumaconven ção,masninguémpre-
cisaestarconectadonaredeparafazerseus commits.
Éincrívelcomoaindaencontroequipesquenãotêmdisciplinaalgumano
129

## Página 148

6.2. Começandopelobásico:controledeversões CasadoCódigo
seuprocessodeentrega. Desenvolvedoressimplesmentelogamnoservidor
deproduçãoealteramocódigo“aovivo”,semnenhumaformadeauditoria
oucontroledequalidade.Qualquerdesenvolvedorpodecriarumdefeitoem
produçãoeninguémconseguirásaberaorigemdoproblema.
EntregacontínuaeDevOpsexigemdisciplinaecolaboraç ão. Opro-
cessodeentregadeumaequipedisciplinada semprecomeçacomum commit.
Qualquermudançaqueprecisairparaprodução–sejacódigo-fonte,código
deinfraestruturaouconfiguração–seiniciacomum commitnosistemade
controledeversões.Issopermiterastrearpossíveisproblemasemproduç ão
comsuaorigem,seuautor,alémdeservircomoumaferramentacentralde
colaboraçãoentreasequipesdedesenvolvimentoedeoperações.
AlojavirtualestáusandooGitcomosistemadecontroledeversões.Seu
repositórioprincipalestáhospedadonoGithub.Alémdeoferecerrepositó-
riosGitgratuitosparaprojetosdecódigoaberto,oGithubéumaferramenta
decolaboraçãoquepermiteoutrosusuáriosrelataremdefeitos,pedidosde
novasfuncionalidades,ouatémesmoclonaremrepositóriosparacontribuir
códigoquecorrigeouimplementataisfuncionalidades.
EmqualquerrepositórioGit,vocêpodeusarocomando git logpara
mostrarohistóricode commitsdoprojeto,porexemplo:
$ git log
commit 337865fa21a30fb8b36337cac98021647e03ddc2
Author: Danilo Sato <dtsato@gmail.com>
Date: Tue Mar 11 14:31:22 2014 -0300
Adicionando LICENSE
commit 64cff6b54816fe08f14fb3721c04fe7ee47d43c0
Author: Danilo Sato <dtsato@gmail.com>
...
CadacommitnoGitérepresentadoporum hash–ouSHA–queéum
conjuntodeletrasenúmerosqueservemcomoidentidadeúnica.Noexemplo
anterior,ocommitmaisrecentepossuioSHAquecome çacom 337865da.O
SHAécalculadocombasenoconteúdodosarquivosmodificadospelo com-
miteelefuncionacomoumaespéciedechaveprimáriaquepodeserusada
parareferenciaro commit.
130

## Página 149

CasadoCódigo Capítulo6. Integraçãocontínua
Emoutrossistemasdecontroledeversão,comonoSVN, commitssão
representadospornúmerosqueautoincrementamacadamudan ça,noen-
tanto,comooGitéumsistemadistribuído,cadarepositórioprecisacalcular
umhashqueéglobalmenteúnico,independentedaexistênciadeoutrosre-
positórios.
Maisparafrenteveremoscomocriarnovos commitsnorepositóriolocale
comocompartilhá-loscomorepositóriocentral.Porenquantovamosapren-
deroutrasferramentasepráticasdeengenhariaágilquefacilitamaado çãode
DevOpseentregacontínua.
6.3 Automatizando o build do projeto
Jávimosopoderdaautomaçãonoscapítulosanterioresquandosubstituímos
umprocessodeprovisionamentoe deploymanualcomcódigoPuppet. A
automaçãodetarefasrepetitivasajudaadiminuiroriscodeerroshumanos,
alémdeencurtarotempode feedbackentreaintroduçãodeumproblemae
suadetecção.AutomaçãoéumdosprincipaispilaresdeDevOpsesemostra
presenteemdiversaspráticasdeengenhariaágil.
Umapartedoprocessodeentregaquesebeneficiabastantedaautomaç ão
éoprocessode build.O builddeumsistemaenvolvetodasastarefasneces-
sáriasparaconseguirexecutá-lo,comoporexemplo:compilação,downloade
resoluçãodedependências,vinculaçãocombibliotecas,empacotamento,cál-
culodemétricasdequalidadeetc.Essastarefaspodemvariardependendoda
linguagemdeprogramaçãoquevocêusa. EmRuby,porexemplo,vocênão
precisacompilararquivosantesdeexecutá-los.
Oresultadodo buildégeralmenteumoumaisarquivosbinários,tam-
bémchamadosdeartefatos.EmumsistemaJava,algunsexemplosdearte-
fatossão:arquivos .jar, .warouatémesmodocumenta çãoJavadocem
HTMLgeradaapartirdocódigo-fonteourelatóriosgeradospelaferramenta
quecalculamétricasdequalidadedocódigo.
Umexemplodeprocessode buildnãorelacionadoaodesenvolvimento
desoftwareestásendousadonaescritadestelivro. Olivroéescritoemar-
quivostextousandoumalinguagemdemarcaç ãodesenvolvidapelaCaelum
–oTubaína(https://github.com/caelum/tubaina).Nossoprocessode build
131

## Página 150

6.3. Automatizandoobuilddoprojeto CasadoCódigo
transformaosarquivostextoeimagensemartefatosquepodemserimpressos
oulidoscomoe-booksemformatoPDF, .mobiou .epub.
Conformeumsistemacresce,seuprocessode buildficamaiscomplicado
eédifícillembrartodosospassosnecessárioscasovocêestejaexecutando-
osmanualmente.Porissoéimportanteinvestiremautomaç ão.Atualmente,
todasasprincipaislinguagenspossuemumaoumaisferramentasdecódigo
livredisponíveisparaajudarnoprocessode build: emJavatemosoAnt,o
Maven,oBuildr,oGradle;emRubytemosoRake;emJavascripttemoso
Grunt;em.NETtemosoNAnt;alémdediversasoutrasalternativas.
AlojavirtualfoiescritausandooMavencomoferramentade build.Con-
formediscutimosnofinaldocapítulo 2,nossoprocessode buildiráresol-
verebaixartodasasdependências,compilar,executartestesautomatizados
eempacotarosartefatosde4módulosdistintos: core, admin, sitee
combined.Paratestarqueo builddoMavenaindafuncionanoseuclonedo
repositório,vocêpodeexecutarocomando:
$ mvn install
[INFO] Scanning for projects...
[INFO] ----------------------------------------------------
...
[INFO] ----------------------------------------------------
[INFO] Reactor Summary:
[INFO] ----------------------------------------------------
[INFO] loja-virtual-devops ............... SUCCESS [1.156s]
[INFO] core .............................. SUCCESS [2.079s]
[INFO] admin ............................. SUCCESS [10:16.469s]
[INFO] site .............................. SUCCESS [7.928s]
[INFO] combined .......................... SUCCESS [25.543s]
[INFO] ----------------------------------------------------
[INFO] ----------------------------------------------------
[INFO] BUILD SUCCESSFUL
[INFO] ----------------------------------------------------
[INFO] Total time: 10 minutes 53 seconds
[INFO] Finished at: Thu Mar 14 07:15:24 UTC 2013
[INFO] Final Memory: 80M/179M
[INFO] ----------------------------------------------------
Porenquanto,nãovamosfazernenhumaalteraç ãonoprocessode build,
132

## Página 151

CasadoCódigo Capítulo6. Integraçãocontínua
porémumaspectoimportantedasuaexecuç ãomereceumpoucomaisde
atenção:ostestesautomatizados.
6.4 Testes automatizados: diminuindo risco e
aumentando a confiança
Compilarosistemaéumpassoimportanteparasuaexecução,principalmente
emlinguagensdetipagemestática.Noentanto,nãoégarantiaqueosistema
iráfuncionarcorretamente.Elepodeconterdefeitosouatémesmoterfun-
cionalidadesimplementadasdeformaerrada.Porissoéimportantetambém
incluirnoprocessode buildaexecuçãode testesautomatizados.
Existemdiversostiposdetestesquepodemserautomatizados,cadaum
comcaracterísticasdistintas. Nãoexisteumaclassificaçãoouterminologia
amplamenteaceitanaindústria,porémvejamosalgunsdostiposdetestemais
comuns:
•Testesdeunidade:práticascomoTDD[3]erefatoração[10]dãobas-
tanteênfasenessetipodeteste,queexercitaunidadesdecódigoiso-
ladamentesemanecessidadedesubireaplicaç ãointeira.Essestestes
geralmenterodambemrápido–naordemdemilissegundos–podendo
serexecutadoscombastantefrequênciaefornecendoomelhortipode
feedbackparaosdesenvolvedores.
•Testesdeintegraçãooutestesdecomponente:exercitamumaparte
daaplicaçãooucomoelaseintegracomsuasdependências,porexem-
plo: umbancodedados,umserviçoREST,umafilademensagens,
ouatémesmoos frameworksebibliotecasutilizados.Dependendodo
componentequeestásendotestado,aexecuç ãodessestestespodem
exigirquepartesdosistemaestejamrodando.
•Testesfuncionaisoutestesdeaceitação:exercitamasfuncionalidades
dosistemacomoumtodo,dopontodevistaexterno.Geralmenteeste
tipodetesteexercitaainterfacegráficaousimulaainteraç ãocomo
sistemadopontodevistadeumusuário. Essestestesgeralmentesão
maislentospoisexigemqueamaiorpartedosistemaestejarodando.
133

## Página 152

6.4. Testesautomatizados:diminuindoriscoeaumentandoaconfian ça CasadoCódigo
Eessesnãosãoosúnicostiposdetestes,existemmuitomais:testesde
desempenho,testesexploratórios,testesdeusabilidadeetc.Elescontribuem
paraavaliaraqualidadedoseusistema,porémnemsempreéfácilautomatizá-
los.Testesexploratórios,porexemplo,sãomanuaispornaturezaeexigema
criatividadedeumserhumanoparadescobrircenáriosondeosistemanão
secomportadaformaesperada.
Acomunidadeágilgeralmenteserefereaosquatroquadrantesdafigura
6.1descritosporBrianMarick[7]comoummodeloparadescreverostipos
detestenecessáriosparaentregarsoftwaredequalidade.
Figura6.1:Quadrantesdeteste
Noladoesquerdoestãotestesquedãosuporteàprograma ção,outestes
queosdesenvolvedoresexecutamcombastantefrequênciaparaobter feed-
backsobreasmudan çasintroduzidasemcada commit.Essestestessepreo-
cupamemavaliaraqualidadeinternadosoftware.Noladodireitoestãotes-
tesquecriticamoprodutocomoumtodo,avaliandosuaqualidadeexternae
tentandoencontrarproblemasperceptíveisaumusuáriodosistema.
Noladosuperiorestãotestesvoltadosaonegócio.Essestestessãodescri-
tosdopontodevistadonegócio,usandoumalinguagemquefazsentidopara
umespecialistadedomínio.Noladoinferiorestãotestesvoltadosàtecnolo-
gia.Essestestessãodescritosdopontodevistatécnico,usandotermosque
farãomaissentidoparaosprogramadoresmasnãotantoparaumespecialista
dedomínio.
Odiagramamostraexemplosdetiposdetesteparacadaquadranteetam-
bémmostraondeémaiscomuminvestiremautomação.Testesnoquadrante
134

## Página 153

CasadoCódigo Capítulo6. Integraçãocontínua
superiordireitosãogeralmentemanuais,poisexigemcriatividadeouexplora-
ção,tarefasquehumanossãobonsemexecutar.Testesnoquadranteinferior
esquerdosãogeralmenteautomatizadosparapoderserexecutadosdiversas
vezeseevitardefeitosderegressão. Nessadiagonal,nãoexistemuitacon-
trovérsianaindústriaemuitasempresasadotamessaestratégiadetestes.A
outradiagonaléumpoucomaiscontroversa.
Umdosgrandesproblemasnaindústriadesoftwareéaformacomoem-
presasencaramtestesdoquadrantesuperioresquerdo.Émuitocomumver
empresasabordaremessestestesdeformamanualeinvestirumaenorme
quantidadedetempoepessoasescrevendo scriptsdetesteemumaplanilha
ouumsistemadegerenciamentodecasosdeteste.
Humanossãopéssimosparaexecutaresses scriptspassapassopoisnão
somosbonsemtarefasrepetitivas: écomumpularmosumaetapaouaté
executá-lanaordemerrada. Poressemotivoaindaexistemempresasalo-
candoumaquantidadeconsideráveldetempona“últimamilha”parauma
fasedetestesabrangente.Umaabordagemágilparaostestesdoquadrantesu-
perioresquerdoéinvestiremautomaçãoparaqueoshumanostenhammais
tempoparaexecutartestesnoquadrantesuperiordireitoondepodemadici-
onarmuitomaisvalor.
Noquadranteinferiordireitooproblemaéumpoucodiferente.Existem
formasdeautomatizaralgunstiposdetestedestequadrante,enquantooutros
aindaprecisamsermanuais.Noentanto,oproblemamaiscomuméqueesse
quadranteégeralmenteignorado. Problemasdedesempenhoouescalabili-
dadesósãoencontradosemproduç ão,quandojáétardedemais.Estaéuma
áreaondeacolaboraçãotrazidaporDevOpspodetrazergrandesbenefícios
paraaentregadesoftwaredequalidade.
Nocasodalojavirtual,comograndepartedosistemaéimplementada
peloBroadleafCommerce,temospoucocódigoJavacustomizadoe,conse-
quentemente,poucostestesautomatizados.Alojadedemonstraç ãooriginal
nãotinhanenhumteste,apesardeocódigodabibliotecaemsiserbemtes-
tado. Poderíamosescreverumoutrolivroapenasabordandoesseassunto,
porémdecidimosautomatizarapenasalgunstestesdeunidadeefuncionais
parausarmoscomoexemplos.
Nossoprincipalinteresseéusaressestestesparafornecer feedbackquando
135

## Página 154

6.4. Testesautomatizados:diminuindoriscoeaumentandoaconfian ça CasadoCódigo
introduzimosmudanças.Quantomaistemposepassaentreomomentoem
queumdefeitoéintroduzidoatésuadetecç ão,maisdifícilserácorrigi-lo.
Poressemotivoéimportanteincluiramaiorquantidadepossíveldetestes
automatizadosnoprocessode build.
OMavenesperaquevocêescrevatestesdeunidadee,inclusive,jásabe
comorodá-losnoprocessode buildpadrão. Sevocêexaminarasaídado
comando mvn installqueexecutamosnase çãoanterior,veráoresultado
dostestesdeunidadeno builddocomponente admin:
...
-------------------------------------------------------
T E S T S
-------------------------------------------------------
Running br.com.devopsnapratica.....AdminLoginControllerTest
Tests run: 2, Failures: 0, Errors: 0, Skipped: 0, Time ...
Results :
Tests run: 2, Failures: 0, Errors: 0, Skipped: 0
...
Onosso builddoMaventambémestáconfiguradoparaexecutartestes
funcionaisqueescrevemosusandoo Selenium(https://code.google.com/p/
selenium/),tambémconhecidoatualmentecomo WebDriver. OSelenium
éumabibliotecaparaautomaçãodonavegadorweb,quenospermitesimu-
larocomportamentodeumusuárionavegandopelalojavirtualeescrever
testesautomatizadosnoestiloJUnitparaverificarquetudofuncionacomoo
esperado.
Nomódulo sitecriamosapenasumexemplodetestefuncionaldefi-
nidonaclasse br.com.devopsnapratica.acceptance.SearchTest.
InicialmenteprecisamosescolherqualnavegadoriremosutilizarequalURL
eledeveacessar:
@Before
public void openBrowser() throws InterruptedException {
driver = new HtmlUnitDriver();
driver.get("http://localhost:8080/");
136

## Página 155

CasadoCódigo Capítulo6. Integraçãocontínua
Thread.sleep(5000); // Waiting for Solr index
}
Aanotação @Beforeépartedo JUnitesignificaqueométodoserá
executadoantesdequalquerteste. Nessecaso,criamosumainstânciade
um HtmlUnitDriverqueéaimplementaçãomaisrápidaelevedeum
WebDriverpois,aoinvésdeabrirumnovoprocessoeumanovajanelapara
onavegadorweb,eleemulatudoemJava. Outrasimplementaçõesexistem
paraosnavegadoresmaiscomuns,comoporexemplo: ChromeDriver,
FirefoxDriverouseestivernoWindows, InternetExplorerDriver.
Ométodo get(String url)carregaumapáginawebnaURLespeci-
ficada,bloqueandoatéqueaoperaçãotermine.Porfim,fazemosnossoteste
esperar5segundosparagarantirqueoíndicedebuscadoSolrtenhasido
carregado. Nossométododetesteédefinidousandoaanotação @Testdo
JUnit:
@Test
public void searchScenario() throws IOException {
...
}
Primeiramente,verificamosqueapáginafoicarregadacorretamente,ve-
rificandootítulodajaneladonavegadorusandoométodo getTitle()do
driver:
assertThat(driver.getTitle(),
is("Broadleaf Demo - Heat Clinic"));
Sabendo que estamos na página correta, procuramos pelo elemento
correspondente ao campo de busca com nomeq, usando o método
findElement(By by).Preenchemosentãoocampocomotermodebusca
"hotsauce”esubmetemosoformuláriousandoométodo submit():
WebElement searchField = driver.findElement(By.name("q"));
searchField.sendKeys("hot sauce");
searchField.submit();
137

## Página 156

6.4. Testesautomatizados:diminuindoriscoeaumentandoaconfian ça CasadoCódigo
Ométodo submit()tambémirábloquearatéqueanovapáginaseja
carregada.Feitoisso,bastaverificarqueabuscaretornou18produtos,vali-
dandootextodedescriçãoatravésdométodo getText():
WebElement searchResults = driver.findElement(
By.cssSelector("#left_column > header > h1" ));
assertThat(searchResults.getText(),
is("Search Results hot sauce (1 - 15 of 18)"));
Repare que dessa vez estamos usando um seletor CSS para encon-
traroelementodesejadonapágina. Porfim, podemostambémverificar
que a página atual mostra apenas 15 resultados, agora usando o método
findElements(By by)que,emvezderetornarumúnicoelemento,re-
tornaumalistadeelementos:
List<WebElement> results = driver.findElements(
By.cssSelector("ul#products > li"));
assertThat(results.size(), is(15));
ObuilddoMavenestáconfiguradoparaexecutarnossotestefuncio-
nalcomopartedafase integration-test,poisprecisamossubirtantoo
bancodedadosquantoaaplicaçãoantesdeexecutaressetipodeteste.Ana-
lisandoasaídadocomando mvn installexecutadoanteriormente,você
tambémiráencontraroresultadodostestesfuncionaisno builddocompo-
nente site:
...
[INFO] --- maven-surefire-plugin:2.10:test (integration-test)
@ site ---
[INFO] Surefire report directory: ...
-------------------------------------------------------
T E S T S
-------------------------------------------------------
Running br.com.devopsnapratica.acceptance.SearchTest
...
Tests run: 1, Failures: 0, Errors: 0, Skipped: 0, Time ...
Results :
138

## Página 157

CasadoCódigo Capítulo6. Integraçãocontínua
Tests run: 1, Failures: 0, Errors: 0, Skipped: 0
...
Comisso,demonstramoscomointegrardiferentestiposdetesteauto-
matizadosnoprocessode builddoseuprojeto.Agoratemososingredientes
básicosparadiscutirumapráticadedesenvolvimentoessencialparatrabalhar
emequipedeformaseguraeeficiente: integraçãocontínua.
6.5 O que é integração contínua?
Quandováriosdesenvolvedoresestãotrabalhandonomesmosistema,apa-
recemnovosdesafiosnoprocessodedesenvolvimentodesoftware. Traba-
lharemparaleloexigemaiscomunicaç ãoecoordenaçãoentreosmembros
daequipepoisquantomaistempoelesficaremsemintegrarsuasmudan ças,
maiororiscodecriaremconflitos.
Integraçãocontínua éumadaspráticasoriginaisdeXPqueencorajade-
senvolvedoresaintegrarseutrabalhofrequentementeparaquepossíveispro-
blemassejamdetectadosecorrigidosrapidamente.Assimqueumdesenvol-
vedorterminaumatarefacujocódigopodesercompartilhadocomaequipe,
eleprecisaseguirumprocessodisciplinadoparagarantirquesuasmudan ças
nãovãointroduzirproblemasequeelasvãofuncionarcorretamentecomo
restodocódigo.
Aoterminarsuatarefa,vocêrodaum buildlocalexecutandotodosos
testesautomatizados. Issogarantequeassuasmudan çasfuncionamisola-
damenteepodemserintegradascomorestodocódigo.Opróximopassoé
atualizarsuacópialocaldoprojeto,puxandoasalteraçõesmaisrecentesdo
repositóriocentral. Éprecisoentãoexecutarostestesnovamenteparaga-
rantirqueassuasmudan çasfuncionamjuntocomasalteraçõesrecentesque
foramintroduzidasporoutrosdesenvolvedores. Sóentãoéquevocêpode
compartilharseu commitcomorepositóriocentral.
Idealmente,cadadesenvolvedorprecisafazerpelomenosum commitpor
diaparaevitaroacúmulodealteraçõeslocaisquenãoestãovisíveisparao
restodaequipe. Equipesmadurastêmohábitodecomitaraindamaisfre-
quentemente,geralmentediversasvezesaodia. Nopiorcaso,sevocêestá
139

## Página 158

6.5. Oqueéintegraçãocontínua? CasadoCódigo
trabalhandoemumamudan çaquevaidemorarmaistempoenãotemcomo
quebrá-laempedaçosmenores,vocêdeveatualizarsuacópialocaldoprojeto
omáximopossívelparaevitaradivergênciacomoqueestáacontecendono
repositóriocentral.
Esseritualdiminuiachancedevocêintroduzirumamudan çaquequebra
ostestesdoprojeto.Noentanto,exigetambémquetododesenvolvedortenha
adisciplinadefazerissoacada commit. Poressemotivo,apesardenãoser
estritamentenecessário,émuitocomumaequipeprovisionarumservidor
dedicadoàintegraçãocontínua,responsávelporgarantirqueoprocessoestá
sendoseguidocorretamente.
Oservidordeintegraçãocontínuaéresponsávelpormonitorarorepo-
sitóriocentraldecódigoeiniciarum builddoprojetotodavezquedetectar
umnovocommit.Aofinaldaexecuçãodeum build,elepodepassaroufalhar.
Quandoobuildfalha,écomumdizerqueelequebrououque“estávermelho”.
Quandoo buildterminacomsucesso,écomumdizerqueo buildpassouou
que“estáverde”.
Oservidordeintegraçãocontínuafuncionatambémcomoumradiador
deinformaçõesdaequipe,mantendotodososdesenvolvedoresinformados
doestadoatualdo builddoprojeto.Ferramentasnessaáreapossuemdiver-
sasmaneirasdedisseminaressainformação:atravésdepainéisdecontrolee
interfacesweb,enviandoe-mailsounotificaçõesparaaequipetodavezqueo
buildfalhar,ouexpondoumaAPIquepodeserusadaparamostraroestado
atualdoprojetoemoutrosdispositivos.
Quandoumproblemadeintegraçãoédetectadoeo buildquebra,uma
boapráticaéquenenhumoutrodesenvolvedorcompartilheseus commitsen-
quantoo buildnãoforconsertado.Geralmenteosresponsáveispeloúltimo
commitcomeçamainvestigaroproblemaedecidementreconsertaropro-
blemaourevertero commitproblemático. Essapolíticaéboaparareforçar
aimportânciademantero buildfuncionandojáqueaequipeficabloqueada
paracompartilharnovasmudan çasenquantooproblemanãoéresolvido.
Existemdiversasferramentascomerciaisedecódigolivrequepodem
serusadasparaconfigurarumservidordeintegraç ãocontínua. Algumas
dasmaispopularessãoo Jenkins(http://jenkins-ci.org/),o CruiseControl
(http://cruisecontrol.sourceforge.net/),o Go(http://go.thoughtworks.com/)
140

## Página 159

CasadoCódigo Capítulo6. Integraçãocontínua
,o TeamCity(http://www.jetbrains.com/teamcity/),eo Bamboo(http://
www.atlassian.com/software/bamboo). Existemtambémserviçosdeinte-
graçãocontínuananuvemnoestiloSaaS(Software as a Service ouSoft-
warecomoServiço)como,porexemplo,o TravisCI(http://travis-ci.org/)
,o SnapCI(http://snap-ci.com/)ouo Cloudbees(http://cloudbees.com/).
Paraumalistamaiscompletadasdiferentesferramentasdeintegraç ãocontí-
nua,valeapenavisitarapáginadaWikipedia http://en.wikipedia.org/wiki/
Comparison_of_continuous_integration_software.
Nossoobjetivonãoéentrarnoméritoounasvantagensedesvantagens
decadaferramenta,massimmostrarumexemplodoprocessodeintegraç ão
contínuafuncionandonaprática. PorissoescolhemosusaroJenkins,que
éumaferramentadecódigolivrebempopularnomundoJava,possuium
amploecossistemadepluginseumacomunidadebemativa.
Antesdeentrarmosnosdetalhesdecomoinstalareconfiguraroservidor
Jenkins,érecomendadoquevocêtenhaseuprópriorepositórioGitdaloja
virtual,ondevocêteráliberdadedefazerseuspróprios commitsparaexer-
citarmosnossoprocessodeintegraçãocontínua. Paraisso,vocêpodesim-
plesmentecriarseupróprio forkdorepositórioprincipalnoGitHub.Um fork
nadamaiséqueoseupróprioclonedequalquerrepositóriodoGitHub.Esta
funcionalidadeexisteparaquemembrosdacomunidadedesoftwarelivre
possamfazermodificaçõesecontribuí-lasdevoltaparaorepositórioprin-
cipal.
Para criar o seuforkvocê vai precisar de um usuário cadastrado no
GitHub. Feitoisso,acesseaURLdorepositóriodalojavirtualem https:
//github.com/dtsato/loja-virtual-devopsecliquenobotão Fork, conforme
mostraafigura 6.2.Apósalgunssegundos,vocêteráumacópiacompletado
repositórioemumanovaURLqueseráparecidacomaURLanterior,porém
substituindoousuário dtsatopeloseuusuáriodoGitHub.
141

## Página 160

6.6. Provisionandoumservidordeintegraçãocontínua CasadoCódigo
Figura6.2:FazendoforkdorepositórionoGitHub
Umavezqueoseu forkdorepositóriotiversidocriado,vocêpodeexe-
cutaroseguintecomandoparaobterumacópialocalnasuamáquina,subs-
tituindo <usuário>peloseuusuáriodoGitHub:
$ git clone https://github.com/<usuário>/loja-virtual-devops.git
Cloning into ’loja-virtual-devops’...
remote: Counting objects: 11358, done.
remote: Compressing objects: 100% (3543/3543), done.
remote: Total 11358 (delta 6053), reused 11358 (delta 6053)
Receiving objects: 100% (11358/11358), 55.47 MiB | 857.00 KiB/s,
done.
Resolving deltas: 100% (6053/6053), done.
$ cd loja-virtual-devops
6.6 P rovisionando um servidor de integração
contínua
ComojáestamosfamiliarizadoscomoprovisionamentousandoVagrante
Puppet,vamosadicionarumanovamáquinavirtualchamada cinoarquivo
Vagrantfile:
142

## Página 161

CasadoCódigo Capítulo6. Integraçãocontínua
VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
...
config.vm.define :db ...
config.vm.define :web ...
config.vm.define :monitor ...
config.vm.define :ci do |build_config|
build_config.vm.network :private_network,
:ip => "192.168.33.16"
build_config.vm.provision "puppet" do |puppet|
puppet.module_path = ["modules", "librarian/modules"]
puppet.manifest_file = "ci.pp"
end
end
end
AnovamáquinavirtualseráprovisionadapeloPuppetusandoumnovo
arquivodemanifestochamado ci.pp. Vocêpodecriaressenovoarquivo
dentrododiretório manifestseseuconteúdoébemsimples:
include loja_virtual::ci
Seguindo o mesmo padrão que criamos no capítulo5, vamos
definir os recursos do servidor de integração contínua em uma
nova classe chamada loja_virtual::ci dentro do módulo
loja_virtual. Para isto, precisamos criar um novo arquivo no ca-
minho modules/loja_virtual/manifests/ci.ppnoqualessanova
classeédefinida:
class loja_virtual::ci {
include loja_virtual
...
}
Éaquiquevemaparteinteressantedainstalaç ãoeconfiguraçãodoJen-
kins.Primeiramenteprecisamosinstalaralgunspacotesbásicosparaasferra-
mentasdedesenvolvimentoe buildcomooGit,MaveneocompiladorJava:
143

## Página 162

6.6. Provisionandoumservidordeintegraçãocontínua CasadoCódigo
package { [ ’git’, ’maven2’, ’openjdk-6-jdk’]:
ensure => "installed",
}
ParainstalareconfiguraroJenkinsvamosusarummóduloescritopela
comunidade, cuja documentação pode ser encontrada emhttps://github.
com/jenkinsci/puppet-jenkins. Este módulo define uma classe chamada
jenkinsqueinstalaumservidorJenkinscomconfiguraçõespadrão. Para
usá-la,bastaadicionarorecurso:
class { ’jenkins’:
config_hash => {
’JAVA_ARGS’ => { ’value’ => ’-Xmx256m’ }
},
}
Estamospassandoum hashqueirásobrescreveraconfiguraçãopadrãode
umadasop çõespassadasnainicializaçãodoJenkins.Definindoaconfigura-
ção JAVA_ARGScomovalor "-Xmx256m"estamosdizendoqueoprocesso
JavadoJenkinspodealocareusaraté256Mbdememória.
UmdosprincipaisatrativosdoJenkinséseuecossistemadeplugins.Para
umalistacompletadetodosospluginssuportadospeloJenkinsvocêpode
acessarsuadocumentaçãoem https://wiki.jenkins-ci.org/display/JENKINS/
Plugins.OmóduloPuppetpossuiumtipodefinidoquepermiteinstalardi-
versosplugins:
$plugins = [
’ssh-credentials’,
’credentials’,
’scm-api’,
’git-client’,
’git’,
’javadoc’,
’mailer’,
’maven-plugin’,
’greenballs’,
’ws-cleanup’
]
144

## Página 163

CasadoCódigo Capítulo6. Integraçãocontínua
jenkins::plugin { $plugins: }
Nonossocaso,osprincipaispluginsqueestamosinteressadossão:
•Plugin git(http://wiki.jenkins-ci.org/display/JENKINS/Git+Plugin)
:permitequeoJenkinsmonitoreeinicie buildsapartirdeumreposi-
tórioGitaoinvésdopadrãoSVN.Osplugins ssh-credentials,
credentials, scm-apie git-clientsãodependênciasdesse
plugin,porissoprecisamosincluí-los.
•Plugin maven-plugin(http://wiki.jenkins-ci.org/display/JENKINS/
Maven+Project+Plugin):permitequeoJenkinsexecuteum builddo
Maven.Osplugins javadoce mailersãodependênciasdesseplu-
gin,porissoprecisamosincluí-los.
•Plugin greenballs (http://wiki.jenkins-ci.org/display/JENKINS/
Green+Balls): alteraçãocosméticanainterfacewebdoJenkinspara
mostrarbuildsbemsucedidosnacorverdeemvezdopadrãoazul.
•Plugin ws-cleanup(https://wiki.jenkins-ci.org/display/JENKINS/
Workspace+Cleanup+Plugin):permitequeoJenkinslimpeosarqui-
vosentreaexecuçãodeum buildeoutro.
Comisso,aclasse loja_virtual::cicompletaficaassim:
class loja_virtual::ci {
include loja_virtual
package { [’git’, ’maven2’, ’openjdk-6-jdk’]:
ensure => "installed",
}
class { ’jenkins’:
config_hash => {
’JAVA_ARGS’ => { ’value’ => ’-Xmx256m’ }
},
}
145

## Página 164

6.6. Provisionandoumservidordeintegraçãocontínua CasadoCódigo
$plugins = [
’ssh-credentials’,
’credentials’,
’scm-api’,
’git-client’,
’git’,
’maven-plugin’,
’javadoc’,
’mailer’,
’greenballs’,
’ws-cleanup’
]
jenkins::plugin { $plugins: }
}
Podemosagoratentarsubiroservidor ciusandooVagrant,porémen-
contramosumproblema:
$ vagrant up ci
Bringing machine ’ci’ up with ’virtualbox’ provider...
==> ci: Importing base box ’hashicorp/precise32’...
==> ci: Matching MAC address for NAT networking...
...
Puppet::Parser::AST::Resource failed with error ArgumentError:
Could not find declared class jenkins at
/tmp/vagrant-puppet-2/modules-0/loja_virtual/manifests/ci.pp:12
on node precise32
Aclasse jenkinsnãofoiencontradapoisesquecemosdeadicioná-lano
arquivo PuppetfilequeoLibrarianPuppetusaparainstalarosmódulos
doPuppetForge.Paraisto,alteramosoarquivo librarian/Puppetfile
adicionandoomódulo rtyler/jenkinsnaversão 1.0.0:
forge "http://forge.puppetlabs.com"
mod "puppetlabs/apt", "1.4.0"
mod "rtyler/jenkins", "1.0.0"
146

## Página 165

CasadoCódigo Capítulo6. Integraçãocontínua
Agorapodemosreprovisionaroservidor cieoJenkinsseráinstalado
comsucesso:
$ vagrant provision ci
==> ci: Installing Puppet modules with Librarian-Puppet...
==> ci: Running provisioner: puppet...
Running Puppet with ci.pp...
...
notice: Finished catalog run in 84.19 seconds
ParaverificarqueoJenkinsfoiinstaladoeconfiguradocorretamente,
vocêpodeabrirumanovajanelanoseunavegadorwebeacessaraURL
http://192.168.33.16:8080/.Setudoestivercertovocêveráateladeboas-vindas
doJenkinsmostradanafigura 6.3.
Figura6.3:Teladeboas-vindasdoJenkins
6.7 Configurando o build da loja virtual
AgoraqueoJenkinsestáinstaladoerodando,precisamosconfigurá-lopara
rodaro builddalojavirtualtodavezquehouverum commitnorepositório
Git.Noentanto,antesdefazerisso,precisamosfazerumaconfiguraç ãoma-
nualparaqueoJenkinsreconhe çaondeoMavenestáinstaladonosistema.
147

## Página 166

6.7. Configurandoobuilddalojavirtual CasadoCódigo
Paraisto,vocêdeveclicarnolink "ManageJenkins”natelaprincipal,ena
telaseguintecliquenoprimeirolink "ConfigureSystem”,quenoslevarápara
ateladeadministraçãodoJenkinsmostradanafigura 6.4.
Figura6.4:TeladeadministraçãodoJenkins
Nestatela,umpoucomaisparabaixo,vocêveráumase çãochamada "Ma-
ven”comumaop ção"Maveninstallations”.Cliquenobotão"AddMaven”e
eleiráexpandirnovasop ções. Iremosentãodesmarcaraopção "Installau-
tomatically”poisoMavenjáestáinstaladonosistema. Precisamosapenas
dizerparaoJenkinsocaminhoondeoMavenpodeserencontrado,preen-
chendoocampo "Name”comovalor "Default”eocampo "MAVEN_HOME”
comovalor "/usr/share/maven2”.Afigura6.5mostracomodeveficarasua
configuraçãoapósseguirestasinstruções,destacandoemvermelhoasáreas
importantes.
148

## Página 167

CasadoCódigo Capítulo6. Integraçãocontínua
Figura6.5:ConfigurandooMavennoJenkins
Éprecisoentãoclicarnobotão "Save”naparteinferiordapáginaparaque
asalteraçõestenhamefeito.Issoiránoslevardevoltaàteladeboas-vindasdo
Jenkins.Podemosentãocriaro builddalojavirtualclicandonolink "create
newjobs”.NaterminologiadoJenkinsum job–outrabalho–representaa
tarefaquevocêquerexecutarrepetidamente. Nele,vocêconfiguraosparâ-
metrosdeexecuçãoeastarefasdoseu build.O jobarmazenaohistóricode
execuçõesassimcomooestadoatualdoseu build.
Umanovatelaseráexibidaparavocêdefinironomedo jobeseutipo.Ire-
mosdefinironomecomo "loja-virtual-devops”eescolheremosaop ção"Build
amaven2/3project”conformemostraafigura6.6.
149

## Página 168

6.7. Configurandoobuilddalojavirtual CasadoCódigo
Figura6.6:CriandoumnovojobnoJenkins
Aoclicarnobotão "OK”,chegamosnatelaprincipaldeconfiguraçãodo
novojob. Vamosdescreverpassoapassooqueprecisamosfazeremcada
seção:
•Seção "Source Code Management”: nestaseçãodefinimosqualsis-
temadecontroledeversõesoJenkinsdeveusarparaobterocódigo
doprojeto.Aoescolheraop ção"Git”,novasopçõesserãoexpandidas.
Aúnicaop çãoimportanteé "RepositoryURL”ondevocêdevepreen-
chercomaURLdoseurepositórionoGitHubcriadonofinaldase ção
6.5,conformemostraafigura 6.7.
150

## Página 169

CasadoCódigo Capítulo6. Integraçãocontínua
Figura6.7:Configurandoosistemadecontroledeversões
•Seção "Build Triggers”:nestase çãodefinimosquaiseventosirãodar
inícioaumanovaexecuçãodo builddoprojeto. Iremosdesmarcara
opção "BuildwheneveraSNAPSHOTdependencyisbuilt” eescolher
aopção "PollSCM”quesignificamonitorarosistemadecontrolede
versões. Umanovacaixadetexto "Schedule”seráexpandida,naqual
vocêprecisadefinirafrequênciacomqueoJenkinsiráverificarseexiste
algumnovo commitnorepositório.Iremospreenchê-lacomovalor "*
****”,quesignifica“monitoremudançasacadaminuto”,conforme
mostraafigura 6.8
151

## Página 170

6.7. Configurandoobuilddalojavirtual CasadoCódigo
Figura6.8:Configurandogatilhoelimpezadaáreadetrabalho
•Seção "Build Environment”:nestase çãovamosescolheraop ção"De-
leteworkspacebeforebuildstarts”paraqueoJenkinssemprelimpea
áreadetrabalhoantesdecome çarumnovo build,conformemostraa
figura6.8.Issogarantequeo buildsempreexecutedeformadetermi-
nística,poisnenhumarquivovaificarsobrandoentreumaexecuç ãoe
outra.
•Seção "Build”: nestaseçãodefinimosqualcomandodeveserexecu-
tadopararodaro build.ComoestamosusandooplugindoMaven,só
precisamospreencherocampo "Goalsandoptions”comovalor "ins-
tall”,conformemostraafigura6.9.
152

## Página 171

CasadoCódigo Capítulo6. Integraçãocontínua
Figura6.9:TarefadoMavenearquivandoartefatosnofinaldobuild
•Seção "Post-build Actions”:nestase çãodefinimosoquedeveaconte-
cerapósaexecuçãodo build.Aoclicarnobotão "Addpost-buildaction”,
iremosescolheraop ção"Archivetheartifacts”,quedizaoMavenpara
arquivarosartefatosgeradospeloprocessode build.Novasop çõesse-
rãoexpandidasebastapreencherocampo "Filestoarchive”comovalor
"combined/target/*.war”,conformemostraafigura6.9. Issofarácom
queoJenkinsarquiveoartefato .wargeradonofinaldo buildpara
quepossamosobtê-lomaisparafrente,nahoradefazerum deploy.
Aofinaldetodasessasconfigurações,vocêpodeclicarnobotão "Save”no
finaldapáginaeo jobserácriadoeirácomeçaramonitorarorepositórioGit
imediatamente.EmmenosdeumminutovocêveráqueoJenkinsvaiagen-
daraexecuçãodoprimeiro builddoseuprojetoe,quandoo buildnúmero1
começararodar,vocêveráumabarradeprogressonocantoinferiordireito,
conformemostraafigura 6.10.
153

## Página 172

6.7. Configurandoobuilddalojavirtual CasadoCódigo
Figura6.10:Primeirobuildagendadoparaexecuç ão
Oprimeiro buildgeralmentedemoraumpoucomaispoisoMavenpre-
cisaresolverebaixartodasasdependênciasdoprojeto.Paraacompanharo
progressoeverasaídacomoseestivesserodandoo buildemumterminal,
vocêpodeclicarnabarradeprogresso. Estapáginaseatualizaautomatica-
mentee,aofinaldaexecuçãodo build,vocêveráamensagem"Finished:SUC-
CESS”quenosinformaqueo buildpassou!Afigura 6.11mostraumexemplo
deum buildqueterminoucomsucesso.
154

## Página 173

CasadoCódigo Capítulo6. Integraçãocontínua
Figura6.11:Buildfinalizadocomsucesso
Paraumresumodaexecução,acesseaURLdo jobemhttp://192.168.33.16:
8080/job/loja-virtual-devops/evocêveráumapáginaparecidacomafigura
6.12.Nocantoinferioresquerdo,vocêveráohistóricodos buildsdoprojetoe
abolinhaverderepresentasucesso–quandoo buildfalha,elaficavermelha
–enocentrodapáginavocêveráumlinkparaoartefato .wargeradono
últimobuildbemsucedido.
155

## Página 174

6.7. Configurandoobuilddalojavirtual CasadoCódigo
Figura6.12:Resumodaexecuçãoeartefatoarquivado
Agoratemosumservidordeintegraçãocontínuaquerodaum buildtoda
vezquedetectarum commitnorepositórioGit.Paratestarainstalaç ãoum
poucomais,vamoscriarumnovo commitcomumapequenaalteraçãoeva-
lidarqueoJenkinsrodaumnovo builddoprojeto. Paraisto,vamosusaro
repositórioquevocêclonoudoGitHubnase çãoanterior.Dentrododiretório
doprojetoclonado,executeocomando:
$ echo -e "\n" >> README.md
Ocomando echoadicionaumaquebradelinhanofinaldoarquivo
README.md. CasovocêestejarodandoesteexemplonoWindowseoco-
mandonãofuncione,vocêpodesimplesmentealteraroarquivonoseueditor
detextopreferidoesalvá-lo.
Aseguir,ocomando git commitcriaumnovo commitcomumamen-
sagemexplicandooquemudoueocomando git pushenviaocommitlocal
paraorepositóriocentralnoGitHub.Nesteúltimocomando,vocêpodepre-
cisarfornecerseuusuárioesenhadoGitHub,dependendodecomosuaconta
estáconfigurada.
$ git commit -am"Adicionando quebra de linha ao final do README"
[master 4d191bd] Adicionando quebra de linha ao final do README
156

## Página 175

CasadoCódigo Capítulo6. Integraçãocontínua
1 file changed, 2 insertions(+), 1 deletion(-)
$ git push origin master
Counting objects: 15, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 310 bytes | 0 bytes/s, done.
Total 3 (delta 2), reused 0 (delta 0)
To git@github.com:dtsato/loja-virtual-devops.git
9ae96a8..4d191bd master -> master
AssimqueoJenkinsdetectaronovo commit,umnovo buildseráagen-
dado,conformemostraafigura 6.13.
Figura6.13:Novobuildagendadoapósumnovocommit
Dessavez,aexecuçãodo builddevesermaisrápida.Nonossoexemplo,
enquantooprimeiro builddemorouaproximadamente12minutos,osegundo
durouapenas4minutos,poistodasasdependênciasjáestavamno cachelocal
doMaven. Aofinaldaexecução,vocêpodenovamenteirparaapáginado
jobemhttp://192.168.33.16:8080/job/loja-virtual-devops/evernãosóomais
novoartefatodisponívelcomotambémumgráficomostrandoohistóricode
execuçãodostestesdoprojeto,conformemostraafigura 6.14.
157

## Página 176

6.8. Infraestruturacomocódigoparaoservidordeintegraç ãocontínua CasadoCódigo
Figura6.14:Maisumbuildbem-sucedido
6.8 Infraestrutura como código para o servi-
dor de integração contínua
ComoJenkinsinstaladoefuncionandocorretamente,poderíamosacabaro
capítuloporaqui.Noentanto,vocêsdevemterpercebidoquefizemosdiver-
sasconfiguraçõesmanuaisatravésdainterfacewebdoJenkinseissopodeser
perigososehouverproblemascomnossoservidordeintegraç ãocontínua.
Quandoumaequipepassaapraticarintegraç ãocontínua,esseservidor
passaaserparteessencialdainfraestruturadoprojeto.Damesmaformaque
nenhumdesenvolvedorpodefazerum commitquandoobuildestáquebrado,
aequipeinteiraficabloqueadaquandooservidordeintegra çãocontínuaestá
foradoar.
Poressemotivoprecisamossercapazesdetrazeraoarumnovoservidor
deintegraçãocontínuacompletamenteconfiguradoomaisrápidopossível.
Iremosumpoucomaisalémparacodificartodasasetapasmanuaisemcó-
digoPuppetparaquepossamosprovisionarumnovoservidordeintegraç ão
contínuacompletoemcasodeemergência.
OJenkinsarmazenaamaioriadesuasconfiguraçõesinternasemar-
158

## Página 177

CasadoCódigo Capítulo6. Integraçãocontínua
quivosXMLdentrododiretório /var/lib/jenkins. Aprimeiracon-
figuraçãomanualquefizemosnaúltimase çãofoidizeraoJenkinsonde
oMavenestáinstaladonosistema. Essaconfiguraç ãoésalvanoarquivo
/var/lib/jenkins/hudson.tasks.Maven.xml.Vamosusaromesmo
truquedocapítulo 4paracopiaroarquivodedentrodamáquinavirtual ci
paranossamáquinalocal:
$ vagrant ssh ci -- ’sudo cp /var/lib/jenkins/
hudson.tasks.Maven.xml \
> /vagrant/modules/loja_virtual/files’
Esse comando irá salvar o arquivo dentro do módulo Puppet da
loja_virtualem modules/loja_virtual/files.Precisamosadici-
onarumnovorecursonaclasse loja_virtual::ci,alterandooarquivo
modules/loja_virtual/manifests/ci.pp:
class loja_virtual::ci inherits loja_virtual {
package { ... }
class { ’jenkins’: ... }
$plugins = ...
jenkins::plugin { ... }
file { ’/var/lib/jenkins/hudson.tasks.Maven.xml’:
mode => 0644,
owner => ’jenkins’,
group => ’jenkins’,
source => ’puppet:///modules/loja_virtual/
hudson.tasks.Maven.xml’,
require => Class[’jenkins::package’],
notify => Service[’jenkins’],
}
}
A próxima configuração manual que fizemos foi criar
o job. Sua configuraç ão fica armazenada no arquivo
/var/lib/jenkins/jobs/loja-virtual-devops/config.xml.
Vamosusaromesmotruqueparacopiaressearquivodedentrodamá-
quinavirtualparaumnovodiretóriode templatesnomóduloPuppetda
loja_virtual:
159

## Página 178

6.8. Infraestruturacomocódigoparaoservidordeintegraç ãocontínua CasadoCódigo
$ mkdir modules/loja_virtual/templates
$ vagrant ssh ci -- ’sudo cp \
> /var/lib/jenkins/jobs/loja-virtual-devops/config.xml \
> /vagrant/modules/loja_virtual/templates’
ParainstruiroPuppetcomocriaro jobapósainstalaçãodoJenkins,va-
mosprecisardefiniralgumasvariáveiscomasconfiguraçõesnecessáriasden-
trodoarquivo ci.pp.Nãoseesque çadesubstituirousuário dtsatopelo
seuusuáriodoGitHubnaURLdavariável $git_repository:
class loja_virtual::ci inherits loja_virtual {
package { ... }
class { ’jenkins’: ... }
$plugins = ...
jenkins::plugin { ... }
file { ’/var/lib/jenkins/hudson.tasks.Maven.xml’: ... }
$job_structure = [
’/var/lib/jenkins/jobs/’,
’/var/lib/jenkins/jobs/loja-virtual-devops’
]
$git_repository = ’https://github.com/dtsato/
loja-virtual-devops.git’
$git_poll_interval = ’* * * * *’
$maven_goal = ’install’
$archive_artifacts = ’combined/target/*.war’
}
Precisamosentãosubstituirosvaloresqueestão hardcodeddentrodo
arquivo XML por expressões ERB que usam as variáveis que acabamos
de criar. Os elementos do XML que precisam ser alterados no arquivo
modules/loja_virtual/templates/config.xmlestãoemdestaquea
seguir,enquantoaspartesnãoalteradasmostramapenasreticências(...):
<?xml version=’1.0’ encoding=’UTF-8’?>
<maven2-moduleset plugin="maven-plugin@2.1">
...
<scm class="hudson.plugins.git.GitSCM" plugin="git@2.0.3">
...
160

## Página 179

CasadoCódigo Capítulo6. Integraçãocontínua
<userRemoteConfigs>
<hudson.plugins.git.UserRemoteConfig>
<url><%= git_repository %> </url>
</hudson.plugins.git.UserRemoteConfig>
</userRemoteConfigs>
...
</scm>
...
<triggers>
<hudson.triggers.SCMTrigger>
<spec><%= git_poll_interval %> </spec>
...
</hudson.triggers.SCMTrigger>
</triggers>
...
<goals><%= maven_goal %> </goals>
...
<publishers>
<hudson.tasks.ArtifactArchiver>
<artifacts><%= archive_artifacts %> </artifacts>
...
</hudson.tasks.ArtifactArchiver>
</publishers>
...
</maven2-moduleset>
Comotemplatecriado,precisamosalteraraclasse loja_virtual::ci
paracriarumnovodiretórioparaonosso jobeusaro templateparacriaro
arquivo config.xml. Faremosistoadicionandodoisnovosrecursosem
modules/loja_virtual/manifests/ci.pp:
class loja_virtual::ci inherits loja_virtual {
package { ... }
class { ’jenkins’: ... }
$plugins = ...
jenkins::plugin { ... }
file { ’/var/lib/jenkins/hudson.tasks.Maven.xml’: ... }
$job_structure = ...
$git_repository = ...
161

## Página 180

6.8. Infraestruturacomocódigoparaoservidordeintegraç ãocontínua CasadoCódigo
$git_poll_interval = ...
$maven_goal = ...
$archive_artifacts = ...
file { $job_structure:
ensure => ’directory’,
owner => ’jenkins’,
group => ’jenkins’,
require => Class[’jenkins::package’],
}
file { "${job_structure[1]}/config.xml":
mode => 0644,
owner => ’jenkins’,
group => ’jenkins’,
content => template(’loja_virtual/config.xml’),
require => File[$job_structure],
notify => Service[’jenkins’],
}
}
O recurso File[$job_structure] garante que a es-
trutura de diretórios do job seja criada enquanto o recurso
File["${job_structure[1]}/config.xml"] usa o template ERB
paracriaroarquivodeconfiguraç ãodo jobenotificaroserviçodoJenkins
paraqueelesejareiniciado.
Comessasalterações,podemostestarseoPuppetrealmenteconsegue
recriaroservidordeintegraçãocontínuadozero.Faremosistousandooco-
mando vagrant destroy ciparaderrubaroservidor ci,seguidode
umcomando vagrant up ciqueiráreprovisioná-lo:
$ vagrant destroy ci
ci: Are you sure you want to destroy the ’ci’ VM? [y/N] y
==> ci: Forcing shutdown of VM...
==> ci: Destroying VM and associated drives...
==> ci: Running cleanup tasks for ’puppet’ provisioner...
$ vagrant up ci
Bringing machine ’ci’ up with ’virtualbox’ provider...
162

## Página 181

CasadoCódigo Capítulo6. Integraçãocontínua
==> ci: Importing base box ’hashicorp/precise32’...
==> ci: Matching MAC address for NAT networking...
...
notice: Finished catalog run in 76.70 seconds
Setudodercerto,aofinaldaexecuç ãodoPuppet,vocêpodeacessarain-
terfacewebdoJenkinsem http://192.168.33.16:8080/e,emvezdeverapágina
deboas-vindas,vocêveráqueo jobdalojavirtualjáexisteeprovavelmente
estarárodando,conformemostraafigura 6.15.
Figura6.15:Jenkinsrecriadodozeroerodandoumnovobuild
Nestecapítuloaprendemosumpoucomaissobrealgumaspráticasdeen-
genhariaágilquepermitemdesenvolversoftwaredequalidade:sistemasde
controledeversão,processosde buildautomatizados,algunsdosprincipais
tiposdetestesautomatizadose,porfim,comoprovisionarumservidordein-
tegraçãocontínuaparadetectarproblemasomaisrápidopossívelegarantir
queaqualidadedosoftwareestásendoavaliadaacada commit.
Alémdisso,encontramosumaformamelhordegeraroartefato .war
aofinaldecada buildforadosservidoresdeprodu ção. Noentanto,oarte-
fatoestápublicadoapenasdentrodoJenkins.Precisamosdeumamaneirade
unirnosso buildcomoprocessode deployparadarmosopróximopassoa
163

## Página 182

6.8. Infraestruturacomocódigoparaoservidordeintegraç ãocontínua CasadoCódigo
caminhodaentregacontínua.
164

## Página 183

Capítulo7
Pipelinedeentrega
Agoraqueadotamosapráticadeintegraçãocontínua,temosumaformacon-
fiáveldegerarevalidarnovasversõesdalojavirtualacada commit.Aofinal
deum buildbemsucedidotemosumartefato .warqueviracandidatoair
paraprodução. Esseéumpassoimportantenajornadaparaimplementar
entregacontínuaeaumentarafrequênciade deploys.Temososcomponentes
necessáriosparacriarumprocessode deployqueaconteceaocliquedeum
botão,sóprecisamosligarospontos.
Atualmente,omóduloPuppetda loja_virtualpossuiumarquivo
.warcomumaversãofixacriadaquandofizemosoprimeiro buildmanual
nocapítulo2. Parausarumarquivo .warmaisrecente,poderíamosbai-
xarumacópialocalacessandoapáginado jobnoJenkins,colocá-lodentro
domóduloPuppetereprovisionaroservidor web.Emvezdefazerissode
formamanualvamosaprendercomocompartilharartefatosusandoumre-
positóriodepacotesquepodeserdiretamenteacessadopelonossocódigo

## Página 184

7.1. Afinidadecomainfraestrutura:usandopacotesnativos CasadoCódigo
Puppetduranteum deploy.
Alémdisso,vamosdiscutircomointegrarocódigodeinfraestruturano
nossoprocessoautomatizadodeentregaecomomodelarasdiferentesetapas
necessáriasparalevarcódigodeum commitatéproduçãocomqualidadee
confiança.
7.1 Afinidade com a infraestrutura: usando pa-
cotes nativos
Copiararquivosparaláeparacánãoéaformamaiseficientedefazer de-
ploy.ÉporissoquenomundoJavaécomumusararquivos .warou .jar
paraagrupardiversosarquivosemumúnicopacote.Elesnadamaissãoque
arquivos ZIP–umformatodecompactaçãobemconhecido–comalguns
metadadosextrasqueindicamoconteúdodopacote. Ecossistemasdeou-
traslinguagenstambémpossuemseusprópriosformatosdeempacotamento
edistribuição: .gememRuby, .dllem.NETetc.
Administradoresdesistemaestãoacostumadosausarosistemadepaco-
tesnativodosistemaoperacionalparaempacotar,distribuireinstalarsoft-
ware. Nósinclusivejáosestamosusandoextensivamentenonossocódigo
Puppet,todavezquecriamosumrecursodotipo Packageouocomando
apt-getparainstalaroMySQL,oTomcat,oNagiosetc.
Esseéumexemploemquedesenvolvedoreseadministradoresdesistema
possuemopiniõeseferramentasdiferentes.DevOpspodemelhoraressacola-
boraçãosimplesmentealinhandoasferramentasusadasduranteoprocesso.
Existemdiversosmotivospelosquaisadministradoresdesistemapreferem
usarpacotesnativosparainstalarsoftware:
•Versionamentoembutidoegerenciamentodedependências : esse
ponto é discutível pois alguns formatos – como Rubygems – pos-
suem esse tipo de suporte. Arquivos.jar e .war também
dão suporte a declarar a versão do pacote dentro do arquivo
META-INF/MANIFEST.MF,porémissonãoéobrigatórioenãopos-
suinenhumasemânticaespecialqueasferramentaspossamaproveitar.
Pacotesnativos,poroutrolado,tratamversõesedependênciascomo
parteintegrantedopacoteesabemresolvê-lasnahoradainstalaç ão.
166

## Página 185

CasadoCódigo Capítulo7. Pipelinedeentrega
•Sistemadedistribui ção: repositóriossãoaformanaturaldearma-
zenarecompartilharpacotesnativosesuasferramentasdegerencia-
mentoeinstalaçãosabemrealizarbuscasebaixarospacotesnecessá-
riosnahoradainstalação.
•Instalaçãoétransacionaleidempotente:gerenciadoresdepacotedão
suporteàinstalação,desinstalaçãoeatualização(ou upgrade)depaco-
teseessasoperaçõessãotransacionaiseidempotentes.Vocênãocorre
oriscodeinstalarapenasmetadedopacoteedeixararquivossoltosno
sistema.
•Suporteaarquivosdeconfiguraç ão:pacotesnativossabemidentificar
arquivosdeconfigura çãoquepodemseralteradosapósainstalaç ão.O
gerenciadordepacotesirámanteroarquivoalteradoouiráguardar
umacópiadoarquivoparaquevocênãopercasuasalteraçõesquando
fizerum upgradeouquandoremoveropacote,respectivamente.
•Verificaçãodeintegridade:quandopacotessãocriados,um checksum
écalculadocombasenoconteúdodoarquivo.Apósopacoteserbai-
xadoparainstalação,ogerenciadordepacotesirárecalcularesse check-
sumecompará-locomoquefoipublicadonorepositórioparagarantir
queopacotenãotenhasidoalteradooucorrompidonoprocessode
download.
•Verificaçãodeassinatura:damesmaforma,pacotessãocriptografi-
camenteassinadosquandopublicadosnorepositório.Noprocessode
instalação,ogerenciadordepacotespodeverificaressaassinaturapara
garantirqueopacoteestárealmentevindodorepositóriodesejado.
•Auditoriaerastreabilidade:gerenciadoresdepacotespermitemdes-
cobrirqualpacoteinstalouqualarquivonosistema.Alémdissovocê
podesaberdeondeumcertopacoteveioequemfoioresponsávelpor
criá-lo.
•Afinidadecomferramentasdeinfraestrutura:porfim,amaioriadas
ferramentasdeautomaçãodeinfraestrutura–comooPuppet,Chef,
167

## Página 186

7.1. Afinidadecomainfraestrutura:usandopacotesnativos CasadoCódigo
Ansible,Saltetc.–sabemlidarcompacotesnativos,gerenciadoresde
pacoteeseusrepositórios.
Poressemotivovamosaprendercomocriarumpacotenativoparaanossa
aplicação.Alémdissovamoscriareconfigurarumrepositóriodepacotespara
publicaredistribuiressesnovospacotesgeradosaofinaldecada buildbem
sucedido.
Provisionandoorepositóriodepacotes
NossosservidoressãomáquinasvirtuaisrodandoLinuxcomosistema
operacional.Emparticular,estamosusandooUbuntu,umadistribuiç ãoLi-
nuxbaseadanoDebian. Nessaplataforma,pacotesnativossãoconhecidos
comopacotes .debeo APTéaferramentapadrãoparagerenciamentode
pacotes.
Umrepositóriodepacotesnadamaiséqueumaestruturadediretóriose
arquivosbemdefinida.Orepositóriopodeserexpostodediversasmaneiras,
comoporexemplo:HTTP,FTP,umsistemadearquivoslocalouatémesmo
umCD-ROMquecostumavaseraformamaiscomumdedistribuiç ãodo
Linux.
Vamosusaro Reprepro(http://mirrorer.alioth.debian.org/)paracriar
e gerenciar nosso repositório de pacotes. Utilizaremos o servidor
ci para distribuir os pacotes pois podemos usar a mesma ferramenta
para gerenciar o repositório e para publicar novos pacotes ao final de
cada build. Para isso criaremos uma nova classe no nosso módulo
loja_virtualchamada loja_virtual::repodentrodeumnovoar-
quivo modules/loja_virtual/manifests/repo.ppcomoseguinte
conteúdoinicial:
class loja_virtual::repo($basedir, $name) {
package { ’reprepro’:
ensure => ’installed’,
}
}
Isso irá instalar o pacote do Reprepro. Essa classe recebe dois
parâmetros: $basedir será o caminho completo para o diretório
168

## Página 187

CasadoCódigo Capítulo7. Pipelinedeentrega
onde o repositório local será criado e$name será o nome do re-
positório. Precisamos também incluir essa classe no servidor ci
e faremos isso alterando a classeloja_virtual::ci no arquivo
modules/loja_virtual/manifests/ci.pp:
class loja_virtual::ci {
...
$archive_artifacts = ’combined/target/*.war’
$repo_dir = ’/var/lib/apt/repo’
$repo_name = ’devopspkgs’
file { $job_structure: ... }
file { "${job_structure[1]}/config.xml": ... }
class { ’loja_virtual::repo’:
basedir => $repo_dir,
name => $repo_name,
}
}
Adicionamos duas novas variáveis para representar o dire-
tório raiz e o nome do repositório e criamos um novo recurso
Class['loja_virtual::repo'] passando essas variáveis como
parâmetrosdaclasse.
NocasodoUbuntu,cadaversãodosistemaoperacionalpossuiumcodi-
nomediferente,tambémconhecidocomo distribuição.Nonossocaso,esta-
mosusandooUbuntu12.04,tambémconhecidocomo precise.Repositó-
riosDebianeUbuntutambémsãodivididosem componentes,queservem
paracomunicarosdiferentesníveisdesuporte: maincontémsoftwarequeé
oficialmentesuportadoelivre; restrictedpossuisoftwarequeésuportado
porémcomumalicençamaisrestritiva; universecontémpacotesmantidos
pelacomunidadeemgeral; multiversecontémsoftwarequenãoélivre.
Nonossocaso,comovamosdistribuirumúnicopacote,todasessasclassifi-
caçõesnãoimportamtanto,entãovamosdistribuirnossopacotecomoum
componente main.
Para que o Reprepro crie a estrutura inicial de diretórios e arqui-
vosdorepositório,precisamoscriarumarquivodeconfiguraç ãochamado
169

## Página 188

7.1. Afinidadecomainfraestrutura:usandopacotesnativos CasadoCódigo
distributionsdentrodeumdiretório confnodiretórioraizdore-
positório. Para isso, vamos criar um novo arquivo detemplateERB em
modules/loja_virtual/templates/distributions.erbcomose-
guinteconteúdo:
Codename: <%= name %>
Architectures: i386
Components: main
SignWith: default
Nessearquivo, Codenameéaformacomoaferramentadalinhadeco-
mandodoRepreproserefereaorepositóriopornome.Usamosasintaxede
substituiçãodoERB <%= name %>queserefereaoparâmetro $nameda
definiçãodaclasse loja_virtual::repo.
Aconfiguração Architectureslistaquaisarquiteturasdeprocessa-
dorospacotesdesserepositóriosuporta.Quandoumpacotepossuiarquivos
compiladosparalinguagemdemáquina,oprocessodecompilaç ãousaum
conjuntodeinstruçõesdiferentesdependendodeondeoprogramaseráexe-
cutado,porissoéimportantedefinirqualarquiteturafoiusadanacompilaç ão
paraqueopacoteexecutecorretamenteapósainstala ção.Nonossocaso,as
máquinasvirtuaisestãorodandoUbuntuemumprocessadordotipo i386.
Aconfiguração SignWithdizaoRepreprocomoeledeveassinarospa-
cotespublicadosnesserepositório.Usaremosovalor defaultqueéacon-
figuraçãopadrãoediscutiremosmaissobreassinaturadepacotesumpouco
maisadiante.
O próximo passo é criar o diretório raiz do repositório e definir
um novo recurso do tipoFile para criar o arquivo de configuração
distributionsusandoo templaterecém-criado.Faremosissonoarquivo
modules/loja_virtual/manifests/repo.pp:
class loja_virtual::repo($basedir, $name) {
package { ’reprepro’:
ensure => ’installed’,
}
$repo_structure = [
"$basedir",
170

## Página 189

CasadoCódigo Capítulo7. Pipelinedeentrega
"$basedir/conf",
]
file { $repo_structure:
ensure => ’directory’,
owner => ’jenkins’,
group => ’jenkins’,
require => Class[’jenkins’],
}
file { "$basedir/conf/distributions":
owner => ’jenkins’,
group => ’jenkins’,
content => template(’loja_virtual/distributions.erb’),
require => File["$basedir/conf"],
}
}
A variável $repo_structure contém a lista de diretórios
que precisa ser criada. Inicialmente você só precisa do diretório
raiz e do diretório conf. Com isso podemos definir o recurso
File["$basedir/conf/distributions"] que usará o template
ERBparacriaroarquivodeconfiguraç ãodoReprepro.
Comorepositóriocriado,precisamosexporseusarquivosparaqueele
possaseracessadodeoutrosservidores. Usaremososervidorweb Apa-
che(http://httpd.apache.org/)paraquenossorepositóriosejaacessadopor
HTTP.InstalareconfiguraroApacheébemsimplesseusarmosomódulo
apachedoPuppetForgeemantidopelaprópriaPuppetLabs.Antesdemais
nada,vamosadicionaradependênciaaonovomódulonaversão 1.0.1no
arquivo librarian/Puppetfile:
forge "http://forge.puppetlabs.com"
mod "puppetlabs/apt", "1.4.0"
mod "rtyler/jenkins", "1.0.0"
mod "puppetlabs/apache", "1.0.1"
Com isso, basta modificar o arquivo
modules/loja_virtual/manifests/repo.pp para adicionar a
171

## Página 190

7.1. Afinidadecomainfraestrutura:usandopacotesnativos CasadoCódigo
classe apacheeusarotipodefinido apache::vhostparaconfigurarum
hostvirtual:
class loja_virtual::repo($basedir, $name) {
package { ’reprepro’: ... }
$repo_structure = [...]
file { $repo_structure: ... }
file { "$basedir/conf/distributions": ... }
class { ’apache’: }
apache::vhost { $name:
port => 80,
docroot => $basedir,
servername => $ipaddress_eth1,
}
}
NoApache,um hostvirtualéaformaderodarmaisdeumwebsiteno
mesmoservidor.Osparâmetros servernamee portdefinemoendere ço
eaportaondeumclientepodeacessaro hostvirtual.Oparâmetro docroot
definequaldiretórioseráexpostonesseendere ço.Nonossocaso,vamosex-
porodiretório $basedirnaporta80eusaremosoendere çoIPdoservidor
paraacessarorepositório.
Avariável $ipaddress_eth1nãoestádefinidanessaclasseenãoé
passadacomoparâmetro. EssavariáveléfornecidapeloFacter,umaferra-
mentautilitáriadoPuppetqueexpõeinformaçõessobreoservidorparauso
emqualquerarquivodemanifesto. Paravertodasasvariáveisdisponíveis
vocêpoderodarocomando facterdentrodequalquerumadasmáquinas
virtuais:
$ vagrant ssh ci
vagrant@ci$ facter
architecture => i386
...
ipaddress => 10.0.2.15
ipaddress_eth0 => 10.0.2.15
ipaddress_eth1 => 192.168.33.16
172

## Página 191

CasadoCódigo Capítulo7. Pipelinedeentrega
...
uptime_seconds => 11365
virtual => virtualbox
vagrant@ci$ logout
Nessecaso,temosduasinterfacesderedeconfiguradas: 10.0.2.15na
interface eth0correspondeaoendere çoIPpadrãoalocadopeloVagrant;
192.168.33.16nainterface eth1correspondeaoendere çoIPquedefini-
mosnoarquivo Vagrantfileparaqueosnossosservidoresconsigamse
comunicar.
Podemos então reprovisionar o servidorci rodando o comando
vagrant provision cie,setudodercerto,vocêpodeacessaraURL
http://192.168.33.16/noseunavegadoreverorepositóriovaziomostradona
figura7.1.
Figura7.1:Repositóriodepacotesvaziocriado
Criandoepublicandoumpacotenativo
Comorepositóriopronto,precisamosmudarnossoprocessode build
paracriarumpacotenativoepublicá-lo.Usaremosaferramenta FPM(https:
//github.com/jordansissel/fpm/) , uma Rubygem escrita por Jordan Sissel
173

## Página 192

7.1. Afinidadecomainfraestrutura:usandopacotesnativos CasadoCódigo
parasimplificaroprocessodecriarpacotesnativosparaasdiferentespla-
taformas–.debnoDebian/Ubuntu, .rpmnoRedHat/CentOSetc.
Para instalar o FPM vamos adicionar um novo recurso do tipo
Package no início da classe loja_virtual::ci, no arquivo
modules/loja_virtual/manifests/ci.pp:
class loja_virtual::ci {
include loja_virtual
package { [’git’, ’maven2’, ’openjdk-6-jdk’, ’rubygems’]:
ensure => "installed",
}
package { ’fpm’:
ensure => ’installed’,
provider => ’gem’,
require => Package[’rubygems’],
}
...
}
Orecurso PackagedoPuppetiráusarogerenciadordepacotespadrão
doservidoremqueestárodando,porémvocêpodesobrescrevê-lo. Nesse
caso,estamosdefinindooprovedor gemexplicitamente,paraqueoPuppet
instaleumaRubygemenãoumpacotenativo.Tambémprecisamosinstalar
opacotenativo rubygems,queéumadependênciadoFPM.
Agora podemos alterar o arquivo de configuração do build da
loja virtual para rodar um comando ao final de todobuild bem
sucedido. Eis as alterações necessárias no final do arquivo XML
modules/loja_virtual/templates/config.xml:
<?xml version=’1.0’ encoding=’UTF-8’?>
<maven2-moduleset plugin="maven-plugin@2.1">
...
<prebuilders/>
<postbuilders>
<hudson.tasks.Shell>
<command>
174

## Página 193

CasadoCódigo Capítulo7. Pipelinedeentrega
fpm -s dir -t deb -C combined/target --prefix \
/var/lib/tomcat7/webapps/ -d tomcat7 -n devopsnapratica
\ -v $BUILD_NUMBER.master -a noarch devopsnapratica.war
\ &amp;&amp; reprepro -V -b <%= repo_dir %> includedeb
\ <%= repo_name %> *.deb
</command>
</hudson.tasks.Shell>
</postbuilders>
<runPostStepsIfResult>
<name>SUCCESS</name>
<ordinal>0</ordinal>
<color>BLUE</color>
<completeBuild>true</completeBuild>
</runPostStepsIfResult>
</maven2-moduleset>
Vamosquebrarasalteraçõesporpartes,come çandodetrásparafrente:
oelemento <runPostStepsIfResult>foialteradoparadizeraoJen-
kins que ele deve rodar um novo comando sempre que umbuilddesse
job completar e seu resultado for bem sucedido. O novo elemento
<hudson.tasks.Shell>–dentrodoelemento<postbuilders>–foi
criadoparadizeraoJenkinsqueeledeverodarumcomandodoterminal,ou
shell.
Ocomandoemsipodeserquebradoemduaspartes:aprimeiracriaopa-
cote .debusandooFPMeasegundapublicaopacotenorepositóriousando
o reprepro.Vamosexplicarcadaop çãopassadaaocomando fpm:
•-s:especificaqueaorigeméumconjuntodearquivose/oudiretórios;
•-t:dizqueoformatodesejadoéumpacote .deb;
•-C:dizaoFPMqueeleprecisaentrarnodiretório combined/target
paraencontrarosarquivosqueserãoempacotados;
•--prefix:defineodiretórioalvoondeosarquivosdevemsercoloca-
dosquandoopacoteforinstalado;
175

## Página 194

7.1. Afinidadecomainfraestrutura:usandopacotesnativos CasadoCódigo
•-d: especifica uma dependência entre nosso pacote e o pacote
tomcat7,umavezqueprecisamosqueodiretóriodasaplicaçõesweb
existaantesdonossopacoteserinstalado;
•-n:onomedonossopacote .deb;
•-v:aversãodopacote. Nessecaso,estamosusandoumavariávelde
ambientedefinidapeloJenkins $BUILD_NUMBERquecorrespondeao
númerodobuildatual. Dessamaneiraconseguimosquecadanovo
buildproduzaumanovaversãodopacote;
•-a:especificaaarquiteturadopacote. Nonossocasonãotemosne-
nhumarquivocompiladoparalinguagemdemáquina,entãousamoso
valor noarch;
•devopsnapratica.war:oúltimoargumentopassadoéonomedo
arquivoquequeremosempacotar.
Após todas essas opções do comando fpm, usamos a sintaxe
&amp;&amp;queéaformadedizer &&dentrodeumarquivoXML.O
caractere &é especial dentro de um arquivo XML, por isso precisamos
escapá-lo,usandooequivalente &amp;.Depoisdissoinvocamosocomando
repreprocomasseguintesop ções:
•-V:especificaqueocomandodevesermaisverboso.Issofarácomque
elemostremaismensagensexplicativasacadapassodasuaexecuç ão;
•-b: especificaodiretóriobaseondeorepositórioestáconfigurado.
Nessecasoestamosusandoovalordavariável $repo_dirquede-
finimosnomanifestodaclasse loja_virtual::ci;
•includedeb:esteéocomandodoRepreproparapublicarumnovo
pacotenorepositório. Estecomandoprecisadedoisparâmetros: o
nomedorepositório,representadopelavariável $repo_name,eoar-
quivo .debdesejado.
Com essa alteração no arquivo de configuração dojob, precisamos
reprovisionar o servidorci novamente, usando o comandovagrant
provision ci.
176

## Página 195

CasadoCódigo Capítulo7. Pipelinedeentrega
Ao final da execução do Puppet, você precisará iniciar um novo
build manualmente para testar a geração do pacote. Você pode fazer
issoclicandonolink "BuildNow”napáginahttp://192.168.33.16:8080/job/
loja-virtual-devops/.
Paranossasurpresa,onovo buildfalhacomoerromostradonafigura
7.2.Umadasmensagensdeerrodiz "Error:gpgmecreatednosignature!”,que
nosinformaqueoprocessodepublicaçãofalhouquandoorepositóriotentou
assinaropacoteusandoaferramentaGPG.
Figura7.2:Buildfalhouaotentarpublicaropacote
OGPG(http://www.gnupg.org/)–ouGnuPG–éumaferramentapara
comunicaçãosegura. Originalmenteescritoparapossibilitaratrocadee-
mailsdeformasegura,elesebaseiaemumesquemadecriptografiacom
chaves. Explicaressetópicoafundoestáalémdoescopodolivro,porém
bastasaberqueoGPGpermitegerarparesdechave,trocareverificarchaves,
criptografaredescriptografardocumentoseautenticardocumentosusando
assinaturasdigitais.
RepositóriosdepacoteusamoGPGparaassinaturadigitaldepacotes,por
issovamosprecisarconfigurarumpardechaves.Aogerarumpardechaves,
criamosuma chavepública–quepodeserdistribuídaparaverificaçãode
177

## Página 196

7.1. Afinidadecomainfraestrutura:usandopacotesnativos CasadoCódigo
assinaturas–eumachaveprivada–quedeveserprotegidaeseráusadapelo
repositórioparaassinarospacotesquandoelesforempublicados.
Oprocessodecriaçãodechavesusaogeradordenúmerosaleatóriosdo
sistemaoperacional,porémexigeumcertoníveldeentropianosistemapara
garantirarobustezdoprocessodecriptografia. Entropiaégeradaquando
vocêusadispositivosdeentradaaodigitarnoteclado,movero mouse,ler
arquivosdodiscoetc. Comoestamosusandoumamáquinavirtualémais
difícilgerarentropia,porissovamosinstalarumaferramentachamada ha-
veged(http://www.issihosts.com/haveged/)quenosajudaránoprocessode
geraçãodechaves:
$ vagrant ssh ci
vagrant@ci$ sudo apt-get install haveged
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following NEW packages will be installed:
haveged
0 upgraded, 1 newly installed, 0 to remove and 157 not upgraded.
...
Setting up haveged (1.1-2) ...
Comoodonodorepositórioéousuário jenkins,precisamosgeraras
chavesGPGcomoesteusuário. Paraisso,vamosusarocomando supara
trocardeusuário:
vagrant@ci$ sudo su - jenkins
jenkins@ci$ whoami
jenkins
Agorabastaexecutarocomando gpg --gen-keyparageraroparde
chaves.Noprocessodegeraçãodechavesvocêprecisaráresponderaalgumas
perguntas. Aprimeiradelaséotipodechave,queusaremosaop ção (1)
RSA and RSA:
jenkins@ci$ gpg --gen-key
gpg (GnuPG) 1.4.11; Copyright (C) 2010 ...
178

## Página 197

CasadoCódigo Capítulo7. Pipelinedeentrega
Please select what kind of key you want:
(1) RSA and RSA (default)
(2) DSA and Elgamal
(3) DSA (sign only)
(4) RSA (sign only)
Your selection?
Apróximaop çãoéotamanhodachave,queusaremosopadrãode2048
bits:
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (2048)
Requested keysize is 2048 bits
Aoperguntaravalidadedachave,usaremosaop çãozeroquedizquea
chavenãoexpira.Logoapósessaop ção,vocêprecisadigitar yparaconfirmar
quenãoquerqueachaveexpire:
Please specify how long the key should be valid.
0 = key does not expire
<n> = key expires in n days
<n>w = key expires in n weeks
<n>m = key expires in n months
<n>y = key expires in n years
Key is valid for? (0)
Key does not expire at all
Is this correct? (y/N) y
Agora você precisa especificar o nome e e-mail associados com
esse par de chaves. Usaremos o nomeLoja Virtuale o e-mailad-
min@devopsnapratica.com.br:
You need a user ID to identify your key; ...
Real name: Loja Virtual
Email address: admin@devopsnapratica.com.br
Comment:
You selected this USER-ID:
"Loja Virtual <admin@devopsnapratica.com.br>"
179

## Página 198

7.1. Afinidadecomainfraestrutura:usandopacotesnativos CasadoCódigo
Aofinaldetodasasop ções,vocêprecisadigitaraopção Oparaconfirmar
todososdados.OGPGiráentãopedirporum passphrase,umtipodesenha
paraprotegerachave.Nessecasovamosdeixaro passphraseembranco,po-
rémissonãoérecomendadoemumambientedeproduç ão. Oprocessode
assinaturaseráexecutadopelo jobdoJenkins,entãovamosconfirmaro pas-
sphraseembranco:
Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? O
You need a Passphrase to protect your secret key.
...
pub 2048R/4F3FD614 2014-03-06
Key fingerprint =
C3E1 45E1 367D CC8B 5863 FECE 2F1A B596 ...
uid Loja Virtual <admin@devopsnapratica.com.br>
sub 2048R/30CA4FA3 2014-03-06
Nofinaldaexecuçãodocomandovocêveráumresumodopardecha-
vesrecém-criado.Emespecial,vocêprecisaráanotaroIDdachavepública
gerada,nessecasoovaloré 4F3FD614.Aúltimacoisaqueprecisamosfazer
éexportarachavepúblicaparaumarquivoqueficarádisponívelnaraizdo
repositório:
jenkins@ci$ gpg --export --armor
admin@devopsnapratica.com.br > \
> /var/lib/apt/repo/devopspkgs.gpg
O comando gpg --export exporta o conteúdo da chave pú-
blica. Aop ção --armorindicaqualpardechavesqueremosexportar,
nesse caso usando o e-mail admin@devopsnapratica.com.br.
A saída deste comando é redirecionada para um novo arquivo
/var/lib/apt/repo/devopspkgs.gpgqueseráexpostojuntocomo
repositório. Feitoisso,podemosdeslogardamáquinavirtualexecutando
ocomando logoutduasvezes,umaparadeslogarousuário jenkinse
outraparasaircompletamentedamáquinavirtual:
jenkins@ci$ logout
vagrant@ci$ logout
$
180

## Página 199

CasadoCódigo Capítulo7. Pipelinedeentrega
Agorapodemosrodarumnovo buildclicandonolink "BuildNow”nova-
mente.Dessavezo builddevepassarconformemostraafigura 7.3.
Figura7.3:Buildpassouepacotefoipublicado
Vocêpodeverificarqueopacotefoipublicadonorepositórioacessando
aURLhttp://192.168.33.16/quedeveráteralgoparecidocomafigura 7.4.
181

## Página 200

7.1. Afinidadecomainfraestrutura:usandopacotesnativos CasadoCódigo
Figura7.4:Repositóriocomopacotepublicado
Fazendodeploydopacotenativo
Agoraquetemosumrepositóriodepacotesdisponívelcomaúltima
versãodalojavirtual,podemosfinalmentenoslivraroarquivo .warque
estáfixodentrodomóduloPuppet. Paraisto,vamossubstituirorecurso
File['/var/lib/tomcat7/webapps/devopsnapratica.war'] por
doisnovosrecursosnaclasse loja_virtual::webnofinaldoarquivo
modules/loja_virtual/manifests/web.pp:
class loja_virtual::web {
...
file { $loja_virtual::params::keystore_file: ... }
class { "tomcat::server": ... }
apt::source { ’devopsnapratica’:
location => ’http://192.168.33.16/’,
release => ’devopspkgs’,
repos => ’main’,
key => ’4F3FD614’,
key_source => ’http://192.168.33.16/devopspkgs.gpg’,
include_src => false,
182

## Página 201

CasadoCódigo Capítulo7. Pipelinedeentrega
}
package { "devopsnapratica":
ensure => "latest",
notify => Service["tomcat7"],
}
}
Orecurso Apt::Source['devopsnapratica']declaraumnovore-
positóriodepacotesqueoAPTpodeusar.Oparâmetro locationpossuio
endereçodoservidorciondeorepositórioestáacessívelporHTTP.Opa-
râmetro releaseéonomedorepositóriodesejado,enquantooparâmetro
reposlistaoscomponentesdesejados.Osparâmetros keye key_source
sãoconfiguraçõesparaverificaçãodeassinaturaentãousamosoIDdachave
públicaqueanotamosnase çãoanterioreaURLparaacessarachavepública
norepositório.Porfim,oparâmetro include_srcprecisaserconfigurado
comovalor falsepoisnossorepositórionãopossuipacotescomocódigo-
fontedosoftwaredistribuído.
Comorepositórioconfigurado,criamosumnovorecurso packagepara
instalaraversãomaisrecentedopacote devopsnapraticaenotificamoso
serviçodoTomcatparaquesejareiniciadoapósopacoteserinstalado.Feito
isso,podemosreprovisionaroservidor webdozero,destruindoerecons-
truindosuamáquinavirtual:
$ vagrant destroy web
web: Are you sure you want to destroy the ’web’ VM? [y/N] y
==> web: Forcing shutdown of VM...
==> web: Destroying VM and associated drives...
==> web: Running cleanup tasks for ’puppet’ provisioner...
$ vagrant up web
Bringing machine ’web’ up with ’virtualbox’ provider...
==> web: Importing base box ’hashicorp/precise32’...
==> web: Matching MAC address for NAT networking...
...
notice: Finished catalog run in 51.74 seconds
Setudodercerto, vocêdeveconseguiracessaralojavirtualnaURL
http://192.168.33.12:8080/devopsnapratica/ e pode então apagar o arquivo
183

## Página 202

7.2. Integraçãocontínuadocódigodeinfraestrutura CasadoCódigo
devopsnapratica.wardodiretório modules/loja_virtual/files.
7.2 Integração contínua do código de infraes-
trutura
Játemosumaformadepublicareconsumirpacotescomnovasversõesda
lojavirtualaofinaldecada build.Noentanto,todocódigodeinfraestrutura
queescrevemosatéagoraexisteapenasnanossamáquinalocaljuntocomo
arquivodeconfiguraçãodoVagrant.Nãoestamosaproveitandoosbenefícios
daintegraçãocontínuanocódigoPuppet.
Nestaseçãovamosconsertarisso,criandoumnovorepositórioparacon-
troledeversões,umnovoprocessode build,adicionandotestesautomati-
zadosecriandoumnovo jobnoJenkinsparaexecutaressenovoprocesso
deintegraçãoepublicarumnovopacotedocódigodeinfraestruturaacada
commit.
Criandoorepositórioparacontroledeversões
Aprimeiradecisãoéondecomitarocódigodeinfraestrutura. Temos
duaspossibilidades: colocarjuntocomorepositóriodaaplica çãooucriar
umnovorepositórioparaocódigoPuppet.Avantagemdecolocartudono
mesmorepositórioéquevocêsimplificaoprocessode setupparaumnovo
membrodasuaequipe,poistudoestánomesmolugar. Noentanto,você
acoplamudançasnaaplicaçãocommudan çasnainfraestrutura:um commit
emqualquerdosdoiscomponentesiráiniciarumprocessode buildquegera
ambososartefatos.Comoociclodemudan çasdaaplicaçãoérelativamente
independentedainfraestrutura,vamosoptarporusarrepositóriosseparados.
VocêpodeoptarporinicializarumnovorepositórioGitnaraizdodi-
retórioondeestãoosmódulosemanifestosdoPuppet,usandoocomando
git init,alterandooarquivo .gitignoreparaindicarquaisarquivos
vocênãoquernorepositórioefazendoo commitinicial:
$ git init
Initialized empty Git repository in /tmp/devops-puppet/.git/
$ echo ".vagrant" >> .gitignore
$ echo "librarian/.tmp" >> .gitignore
184

## Página 203

CasadoCódigo Capítulo7. Pipelinedeentrega
$ echo "librarian/.librarian" >> .gitignore
$ echo "librarian/modules" >> .gitignore
$ echo "librarian/Puppetfile.lock" >> .gitignore
$ echo "*.tgz" >> .gitignore
$ git add -A
$ git commit -m"Commit inicial"
[master (root-commit) 64686a5] Commit inicial
27 files changed, 664 insertions(+)
create mode 100644 .gitignore
...
create mode 100644 modules/tomcat/templates/server.xml
DepoisvocêpodecriarumnovorepositórionoGitHubmanualmente
escolhendoumnome,porexemplo loja-virtual-puppet. Feitoisso,
vocêpodeexecutarocomandoaseguirsubstituindoousuário dtsatopelo
seuusuáriodoGitHube loja-virtual-puppetpelonomedorepositório
quevocêescolheu:
$ git remote add origin
git@github.com:dtsato/loja-virtual-puppet.git
$ git push -u origin master
Counting objects: 42, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (33/33), done.
Writing objects: 100% (42/42), 12.11 KiB | 0 bytes/s, done.
Total 42 (delta 1), reused 0 (delta 0)
To git@github.com:dtsato/loja-virtual-puppet.git
* [new branch] master -> master
Branch master set up to track remote branch master from origin.
Aoutraop ção,quevaieconomizaralgunspassosnaspróximasse ções,
éclonarorepositóriojáexistentenorepositório https://github.com/dtsato/
loja-virtual-devops-puppet.Damesmaformaquefizemosnocapítulo 6,você
podeclonaresserepositórioclicandonobotão "Fork”.
Independentedasuaescolha,temosagoranossocódigoPuppetemum
sistemadecontroledeversõesepodemosseguiradianteparacriarum build
automatizado.
185

## Página 204

7.2. Integraçãocontínuadocódigodeinfraestrutura CasadoCódigo
Umbuildautomatizadosimples
OPuppetéescritoemRubyediversasdasferramentasusadaspelaco-
munidadesãoinspiradasouintegradascomoecossistemaRuby.Rubypos-
suiumaferramentade buildbastantepoderosaeaomesmotemposimples:
oRake(http://rake.rubyforge.org/).InspiradopeloMake,vocêpodedefinir
tarefas(outasks)compré-requisitosquedefinemcomandosarbitrários.
ParaentendercomooRakefunciona,vamoscriarumarquivo Rakefile
ondepodemosdefinirnossasprimeirastarefas:
desc "Cria o pacote puppet.tgz"
task :package do
sh "tar czvf puppet.tgz manifests modules librarian/modules"
end
desc "Limpa o pacote puppet.tgz"
task :clean do
sh "rm puppet.tgz"
end
Atarefa packagecriaumpacoteusandoocomando tarcontendotodo
ocódigoPuppetquetemosatéagora.Atarefa cleanapagaopacotegerado
usandoocomando rm.Paraexecutaressastarefas,vocêpodesimplesmente
passá-lasparaocomando rakenoterminal:
$ rake -T
rake clean # Limpa o pacote puppet.tgz
rake package # Cria o pacote puppet.tgz
$ rake package
tar czvf puppet.tgz manifests modules librarian/modules
a manifests
...
a librarian/modules/apache/files/httpd
$ rake clean
rm puppet.tgz
Tambémvejaqueocomando rake -Tlistatodasastarefasdocumenta-
das.SabemosqueosmódulosdoLibrarianPuppetjáforambaixados,porisso
elesentraramnopacote.PorémelesnãoestariamdisponíveisseoLibrarian
186

## Página 205

CasadoCódigo Capítulo7. Pipelinedeentrega
Puppetnãotivesseexecutado.Podemoscriarumaoutratarefaparaexecutar
ocomando librarian-puppet installeaomesmotempoaprendera
sintaxedoRakeparaespecificarpré-requisitosentretarefas:
# encoding: utf-8
namespace :librarian do
desc "Instala os módulos usando o Librarian Puppet"
task :install do
Dir.chdir(’librarian’) do
sh "librarian-puppet install"
end
end
end
desc "Cria o pacote puppet.tgz"
task :package => ’librarian:install’ do
sh "tar czvf puppet.tgz manifests modules librarian/modules"
end
...
ORaketambémsuporta namespaces,paraagrupartarefassimilaresden-
tro de um mesmo nome. Nesse caso, criamos umnamespacechamado
librarian e uma tarefainstall dentro dele que simplesmente en-
tranodiretório librarianeexecutaocomando librarian-puppet
install.Adefiniçãodatarefa packagetambémmudouparadeclararsua
dependênciacomanovatarefa librarian:install.Aoexecutaratarefa
packagenovamente,vemosumerro:
$ rake package
librarian-puppet install
rake aborted!
Command failed with status (127): [librarian-puppet install...]
...
Tasks: TOP => package => librarian:install
(See full trace by running task with --trace)
IssoacontecepoisoLibrarianPuppetnãoestáinstaladonoseusistema.
NósapenasousamoscomoumplugindoVagrant.NomundoRuby,amelhor
formadegerenciaressetipodedependênciadeambienteéusaro Bundler
187

## Página 206

7.2. Integraçãocontínuadocódigodeinfraestrutura CasadoCódigo
(http://bundler.io/).ComoBundlervocêdeclarasuasdependênciasemum
arquivo GemfileeoBundlertomacontaderesolverasdependências,baixar
einstalarasRubygemsnasversõesquevocêdesejar.Vamoscriaroarquivo
Gemfilecomoseguinteconteúdo:
source ’https://rubygems.org’
gem ’rake’, ’10.1.1’
gem ’puppet-lint’, ’0.3.2’
gem ’rspec’, ’2.14.1’
gem ’rspec-puppet’, ’1.0.1’
gem ’puppet’, ’2.7.19’
gem ’librarian-puppet’, ’0.9.14’
AlémdoRakeedoLibrarianPuppet,jáadicionamosalgumasoutrasde-
pendênciasquevamosprecisarnapróximase ção.Percebatambémqueesta-
mosusandoversõesespecíficasdessasRubygemsparatornarnossoambiente
localomaispróximopossíveldoambientedeproduç ão.Porexemplo,nos-
sasmáquinasvirtuaisrodamoPuppetnaversão 2.7.19,porissousamosa
mesmaversãonoprocessode build.
ParainstalarasdependênciasvocêprecisaprimeiramenteinstalaroBun-
dleremsi,casonuncaotenhausadonasuamáquina.Feitoisso,vocêpode
rodarocomando bundle installparainstalartodasasRubygemsneces-
sárias:
$ gem install bundler
Successfully installed bundler-1.5.3
1 gem installed
$ bundle install
Fetching gem metadata from https://rubygems.org/...........
Fetching additional metadata from https://rubygems.org/..
Resolving dependencies...
Using rake (10.1.1)
...
Your bundle is complete!
Use `bundle show [gemname]` to see where a bundled gem is
installed.
188

## Página 207

CasadoCódigo Capítulo7. Pipelinedeentrega
Agoraatarefa packagedeverodarcomsucesso.Sóprecisamosprefixar
ocomandocom bundle execparagarantirqueoRakevairodarusando
asgemsnasversõesespecificadasnonosso Gemfile:
$ bundle exec rake package
librarian-puppet install
tar czvf puppet.tgz manifests modules librarian/modules
a manifests
a manifests/ci.pp
...
Temosumprocessoautomatizadoparaempacotarnossocódigo,porém
nãoestamosfazendonenhumtipodeverificaç ão. Umaformabemsim-
pleserápidadevalidarocódigoPuppetéusaraferramenta PuppetLint
(http://puppet-lint.com/),queverificaqueseucódigoestáseguindoumpa-
drãodecódigoegeraavisosquandoencontrarproblemas. Comonósjáo
incluímosnonosso Gemfile,podemossimplesmenteadicionarumanova
tarefaedependêncianoarquivo Rakefile:
# encoding: utf-8
require ’puppet-lint/tasks/puppet-lint’
PuppetLint.configuration.ignore_paths = ["librarian/**/*.pp"]
namespace :librarian do ... end
desc "Cria o pacote puppet.tgz"
task :package => [’librarian:install’, :lint] do
sh "tar czvf puppet.tgz manifests modules librarian/modules"
end
task :clean do ... end
O Puppet Lint já define a tarefa Rake para gente, por
isso nós precisamos apenas fazer um require do arquivo
'puppet-lint/tasks/puppet-lint'. Também configuramos a
tarefaparaignorarosarquivos .ppdentrododiretório librarianpois
nãoqueremosvalidarocódigoPuppetdosmódulosexternosqueestamos
189

## Página 208

7.2. Integraçãocontínuadocódigodeinfraestrutura CasadoCódigo
usando. Nossobuilddevefocarnosmódulosqueestamosescrevendo. Por
fim,alteramosospré-requisitosdatarefa packageparalistarduastarefas
usandoum Array.
Aoexecutaratarefa package,veremosdiversosavisosdoPuppetLint,
representadoscomomensagensdotipo WARNING:
$ bundle exec rake package
librarian-puppet install
modules/loja_virtual/manifests/ci.pp - \
WARNING: class not documented on line 1
modules/loja_virtual/manifests/ci.pp - \
WARNING: double quoted string containing no variables on line 5
...
TestandocódigoPuppet
OPuppetLintvaiencontrarproblemasdesintaxeeestilonocódigoPup-
pet,porémnãoconsegueverificarsevocêdigitouonomedeumavariável
erradoouseumdeterminadovalorestáerrado. Paraisso,podemosescre-
vertestesautomatizadosparanossosmódulosusandoferramentascomoo
RSpec-Puppet(http://rspec-puppet.com/),umaextensãodopopular fra-
meworkdetestesRSpecquenosdádiversasextensõesparatestarcódigoPup-
petcommaisfacilidade.
ARubygemdoRSpec-Puppettambémjáestáinstalada,porémprecisa-
mosinicializarumaestruturadediretóriosondecolocaremosnossocódigo
detestedentrodecadamódulo. Primeiramente,iremosfocarnomódulo
mysql:
$ cd modules/mysql
$ bundle exec rspec-puppet-init
+ spec/
...
+ Rakefile
$ rm Rakefile
$ cd ../..
Nosso primeiro teste será para a classemysql::client, por isso
vamos criar um novo arquivoclient_spec.rb dentro do diretório
190

## Página 209

CasadoCódigo Capítulo7. Pipelinedeentrega
modules/mysql/spec/classescomoseguinteconteúdo:
require File.join(File.dirname(__FILE__), ’..’, ’spec_helper’)
describe ’mysql::client’ do
it {
should contain_package(’mysql-client’).
with_ensure(’installed’)
}
end
Obloco describedefineonomedaclasse,tipodefinidooufun ção
donossomóduloquequeremostestar.Cadabloco itrepresentaumcasode
teste.Nestecaso,aclasse mysql::clientinstalaopacote mysql-client
porissonossotesteverificaqueopacotefoiinstalado.Paraexecutaroteste,
podemosusarocomando rspec:
$ bundle exec rspec modules/mysql/spec/classes/client_spec.rb
.
Finished in 0.34306 seconds
1 example, 0 failures
Sucesso!TemosnossoprimeirotestedoPuppetpassando.Assimcomo
nocapítulo 6,nossoobjetivoaquinãoéobterumaaltacoberturadetestes,
massimentendercomointegraroprocessodetestecomoprocessodeentrega
contínua. ParamaisdetalhesdecomoescrevertestesparacódigoPuppet,
vocêpodeexplorarorepositóriooriginalouleradocumentaç ãodoRSpec-
Puppetem http://rspec-puppet.com/tutorial/.
Oqueprecisamosfazerérodarostestesnoprocessode build.Paraisso,
vamosalteraroarquivo Rakefileparacriarnovastarefas:
...
require ’rspec/core/rake_task’
TESTED_MODULES = %w(mysql)
namespace :spec do
TESTED_MODULES.each do |module_name|
desc "Roda os testes do módulo #{module_name}"
191

## Página 210

7.2. Integraçãocontínuadocódigodeinfraestrutura CasadoCódigo
RSpec::Core::RakeTask.new(module_name) do |t|
t.pattern = "modules/#{module_name}/spec/**/*_spec.rb"
end
end
end
desc "Roda todos os testes"
task :spec => TESTED_MODULES.map {|m| "spec:#{m}" }
namespace :librarian do ... end
desc "Cria o pacote puppet.tgz"
task :package => [’librarian:install’, :lint, :spec] do
sh "tar czvf puppet.tgz manifests modules librarian/modules"
end
task :clean do ... end
task :default => [:lint, :spec]
VamosusaratarefaRakefornecidapelopróprioRSpecparadefiniruma
tarefaparacadamódulo. Porenquanto,temostestesdefinidosapenaspara
omódulo mysql.Pararodartodosostestes,criamosumatarefa specque
dependedastarefasdecadamódulo. Tambémadicionamosumnovopré-
requisitonatarefa packageedefinimosumatarefapadrão defaultque
executasemprequevocêrodarocomando rakesemespecificarnenhuma
tarefa.Porexemplo:
$ bundle exec rake
modules/loja_virtual/manifests/ci.pp - \
WARNING: class not documented on line 1
...
/Users/dtsato/.rvm/rubies/ruby-1.9.3-p385/bin/ruby \
-S rspec modules/mysql/spec/classes/client_spec.rb
.
Finished in 0.33303 seconds
1 example, 0 failures
192

## Página 211

CasadoCódigo Capítulo7. Pipelinedeentrega
Comissotemosumprocessode buildetestesautomatizadoquepode-
mosusarparaimplementarintegraçãocontínuadocódigodeinfraestrutura.
Podemosentãofazerum commiteenviarnossocódigoparaorepositórioGit:
$ git add -A
$ git commit -m"Adicionando build e testes automatizados"
[master 3cf891c] Adicionando build e testes automatizados
8 files changed, 100 insertions(+)
create mode 100644 Gemfile
...
create mode 100644 modules/mysql/spec/spec_helper.rb
$ git push
Counting objects: 21, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (12/12), done.
Writing objects: 100% (18/18), 2.34 KiB | 0 bytes/s, done.
Total 18 (delta 0), reused 0 (delta 0)
To git@github.com:dtsato/loja-virtual-puppet.git
fe7a78b..3cf891c master -> master
ConfigurandoumjobnoJenkinsparaocódigoPuppet
Agorapodemosfinalmentecriarumnovo jobnoJenkinsparanossocó-
digoPuppet.AcessandoapáginaprincipaldoJenkinsem http://192.168.33.16:
8080/vocêpodeclicarnolink NewItem.Napróximapágina,especificamos
onomedo jobcomoloja-virtual-puppeteotipodeprojetoé Buildafree-style
softwareprojectconformemostraafigura 7.5.
193

## Página 212

7.2. Integraçãocontínuadocódigodeinfraestrutura CasadoCódigo
Figura7.5:Novojobparacódigodeinfraestrutura
Aoclicarnobotão OK,chegamosnatelaprincipaldeconfiguraç ãodo
novojob. Vamosdescreverpassoapassooqueprecisamosfazeremcada
seção:
•Seção "Source Code Management”:vamosescolheraop çãoGitepre-
encherocampo RepositoryURL comaURLdoseurepositóriono
GitHubcriadonase çãoanterior,conformemostraafigura 7.6.
194

## Página 213

CasadoCódigo Capítulo7. Pipelinedeentrega
Figura7.6:Configurandoosistemadecontroledeversões
•Seção "Build Triggers”:vamosescolheraop çãoPollSCM epreencher
acaixadetexto Schedulecomovalor *****,conformemostraafigura
7.7
Figura7.7:Configurandogatilhoelimpezadaáreadetrabalho
195

## Página 214

7.2. Integraçãocontínuadocódigodeinfraestrutura CasadoCódigo
•Seção "Build Environment”:nestase çãovamosescolheraop çãoDe-
leteworkspacebeforebuildstarts paralimparaáreadetrabalhoantes
decomeçarumnovo build,conformemostraafigura 7.7.
•Seção "Build”:nestase çãoescolheremosaop çãoExecuteshell dentro
dacaixadesele çãoAddbuildstep.Ocampo Commanddeveráserpre-
enchidocomovalor bundle install --path ~/.bundle &&
bundle exec rake package,conformemostraafigura 7.8.
Figura7.8:Comandodobuildearquivandoartefatosnofinaldobuild
•Seção "Post-build Actions”:aoclicarnobotão Addpost-buildaction
vamosescolheraop çãoArchivetheartifacts epreencherocampo Files
toarchivecomovalor *.tgz,conformemostraafigura 7.8.
Comissopodemosclicarnobotão Saveeumnovo builddeveráser
agendado e executar nos próximos minutos. No entanto, obuild falha
comumamensagem bundle: not found. VamosprecisarinstalaroBun-
dler para que o Jenkins consiga rodar nossobuild. Faremos isso adi-
cionando um novo recurso do tipoPackage no começo do arquivo
modules/loja_virtual/manifests/ci.pp,juntocomainstalaçãodo
FPM:
196

## Página 215

CasadoCódigo Capítulo7. Pipelinedeentrega
class loja_virtual::ci {
...
package { [’fpm’, ’bundler’]:
ensure => ’installed’,
provider => ’gem’,
require => Package[’rubygems’],
}
...
}
Após reprovisionarmos o servidorci com o comandovagrant
provision ci,vocêpodeiniciarumnovo buildclicandonolink "Build
Now”. Dessavezeledeveterminarcomsucesso,conformemostraafigura
7.9.
Figura7.9:Buildbem-sucedido
Seguindoosmesmospassosdocapítulo 6podemosautomatizaropro-
cessodecriaçãodesse jobcomcódigoPuppet. Encorajamosquevocêtente
fazê-loparaexercitarseuconhecimentodoPuppetedosconceitosapresenta-
dosatéagora.UmapossívelsoluçãoestádisponívelnorepositóriodoGitHub
quevocêclonounoiníciodestase ção.Iremosomitiressaexplicaçãodolivro
197

## Página 216

7.3. Pipelinedeentrega CasadoCódigo
porquestãodeespaçoeparapodermosdiscutirumdosconceitosmaisim-
portantesdaentregacontínua:a pipelinedeentrega.
7.3 Pipeline de entrega
Paraterminarestecapítulo,éhoradeintegrarnossosdois buildseconfigurar
umprocessode deployparaproduçãoemumclique.Atualmentetemosdois
processosdeintegraçãocontínuaindependentes,nosquaisoprodutofinalde
cadabuildéumpacotequepodeirparaproduç ão.
Geralmenteocaminhodeum commitatéaproduçãoprecisapassarpor
diversasetapas,algumasdelassãoautomatizadasenquantooutrasexigem
aprovaçõesmanuais. Porexemplo,écomumempresasteremetapasdeva-
lidaçãocomousuárioondevocêpodedemonstrarosoftwarefuncionando
emumambientedetestesesóapósumconsensomútuoéqueocódigovai
paraprodução. Existemtambémdiversasempresaswebquecolocamqual-
quercommitbemsucedidoemproduçãosemnenhumaetapadevalidaç ão
manual.
Éaquiquefazemosadistin çãoentreduaspráticasquegeralmentesão
confundidas:implantaçãocontínua(deploycontínuoouContinuousDeploy-
ment)éapráticadecolocaremproduçãotodo commitbemsucedidoegeral-
mentesignificafazerdiversos deploysemproduçãopordia; entregacontínua
éapráticaondequalquercommitpodeirparaproduçãoaqualquermomento,
porémadecisãodequandoistoaconteceéumaop çãodenegócio.
Paraexemplificaradiferen çavamospensaremduassituações: napri-
meiravocêestádesenvolvendoumprodutoqueprecisaserdistribuídoeins-
talado–porexemplo,umaplicativomóvel–efazerumdeployemprodução
acada commitnãoéalgofáciloudesejável.Emoutrasituaçãovocêtemuma
aplicaçãowebusadaconstantementeporváriosusuáriosecolocarcorre ções
ounovasfuncionalidadesnoarrapidamentepodemtedarumavantagem
competitivanomercado.
Independentedequalpráticafizermaissentidoparavocê,existeumpa-
drãoessencialparaimplementarentregaouimplantaçãocontínua:a pipeline
deentrega.Emumnívelabstrato,apipelinedeentregaéumamanifestaç ão
automatizadadoseuprocessodeentregadesoftware,desdeumamudan çaaté
198

## Página 217

CasadoCódigo Capítulo7. Pipelinedeentrega
suaimplantaçãoemprodução.Elamodelaasetapasautomatizadasemanu-
aisdoprocessodeentregaeéumaextensãonaturaldapráticadeintegraç ão
contínuaquediscutimosatéaqui.
Afigura7.10mostraumexemplodeumapipelinedeentregacomum,
ondeumamudan çapassapelosestágiosde buildetestesdeunidade,testes
deaceitação,valida çãocomusuáriofinaleentregaemprodução.Odiagrama
mostratambémcomoapipelinefornecefeedbackrápidoquandoproblemas
sãoencontrados.Cadaestágioestáláparavetaramudan çaantesqueelache-
gueemprodução.Somenteos commitsque“sobreviverem”todososestágios
dapipelinesãodisponíveispara deployemprodução.
Figura7.10:Mudançassepropagandopelapipelinedeentrega
Modelarasuapipelinedeentregaexigeentenderseuprocessodeentrega
ebalancearoníveldefeedbackquevocêquerreceber.Geralmente,osestá-
giosiniciaisfornecemfeedbackmaisrápido,porémpodemnãoestarexecu-
tandotestesexaustivosemumambienteparecidocomproduç ão.Conforme
osestágiosavançam,asuaconfian çaaumenta,assimcomoasimilaridadedos
ambientesquevãoficandocadavezmaisparecidoscomproduç ão.
Nonossocaso,vamosmodelarumapipelinedeentregabemsimplificada,
umavezquenossoobjetivoémostrarumaimplementaçãoprática.Porexem-
plo,nossostestesdeaceitaçãoatualmenterodamno buildinicialdaaplicação,
199

## Página 218

7.3. Pipelinedeentrega CasadoCódigo
juntocomostestesdeunidade,poisérápidoosuficienterodá-losemcon-
junto.Conformeacoberturadostestesfuncionaisaumenta,geralmenteau-
mentatambémseutempodeexecuçãoevocêvaiprecisarconsiderarsepará-
losemestágiosdiferentesdapipeline.
Afigura7.11mostraanossapipelinedeentrega.Temosdoisestágiosinici-
aiseparalelospara build,testeeempacotamentodocódigodaaplicaç ãoedo
códigodeinfraestrutura.Ambososestágiosestãoconectadoscomumnovo
estágiodedeployparaproduçãoqueiremosconfiguraraseguir.Porenquanto,
todasastransiçõesserãoautomáticasportantoessapipelineimplementaum
processodeimplantaçãocontínua.
Figura7.11:Pipelinedeentregadalojavirtual
Criandoumnovoestágiodedeployparaprodu ção
Antes de criar o novojobno Jenkins, precisamos instalar mais dois
plugins que permitem ligar nossosjobs entre si: o plugin"Paramete-
rizedTrigger”(https://wiki.jenkins-ci.org/display/JENKINS/Parameterized+
Trigger+Plugin)permitequeum buildsejaengatilhadoquandoo buildde
outroprojetotermina,assimcomopermitepassarparâmetrosentreeles;o
plugin"CopyArtifact”(https://wiki.jenkins-ci.org/display/JENKINS/Copy+
Artifact+Plugin)permitecopiarartefatosdeum buildparaoutro.
Vamosadicionaressespluginsnaclasse loja_virtual::ci,alterando
oarquivo modules/loja_virtual/manifests/ci.pp:
200

## Página 219

CasadoCódigo Capítulo7. Pipelinedeentrega
class loja_virtual::ci {
...
$plugins = [
...
’ws-cleanup’,
’parameterized-trigger’,
’copyartifact’
]
...
}
Comissopodemosreprovisionaroservidor ciexecutandoocomando
vagrant provision cieestaremosprontoparacriaronovo jobnoJen-
kins.NapáginaprincipaldoJenkinscriaremosumnovo jobclicandonolink
NewItemepreenchendoonomedoprojetocomo DeployemProdu çãoees-
colhendootipodeprojeto Buildafree-stylesoftwareproject.
Aoclicar "OK”seremoslevadosparaapáginadeconfiguraçãodonosso
novojob.Dessavezdeixaremosase ção"SourceCodeManagement”intocada
poisqueremosquenosso buildrodequandoosoutrosprojetosterminarem.
Paraisso,nase ção BuildTriggers vamosescolheraop ção Buildafterother
projectsarebuilt epreencherocampo Projectnamescomovalor loja-virtual-
devops,loja-virtual-puppet.
Nase ção BuildEnvironment vamosnovamentemarcaraop ção Delete
workspacebeforebuildstarts.Nase çãoBuildiremosadicionardoiscomandos:
•CopiandoartefatodoPuppet:selecionandootipo Copyartifactsfrom
anotherproject,vamospreencherocampo Projectname comovalor
loja-virtual-puppeteescolheremosaop çãoUpstreambuildthattrigge-
redthisjob.IssofarácomqueoJenkinscopieoartefatodo buildque
engatilhouessaexecução.Alémdisso,vamosmarcaraop çãoUseLast
successulbuildasfallback paraquepossamosengatilharum deploypara
produçãomanualmentesemprecisarrodaro builddoprojetoanterior.
Porfim,preenchemosocampo Artifactstocopy comovalor puppet.tgz,
conformemostraafigura 7.12.
•Fazendoo deploynoservidorweb:adicionamosoutrocomandodo
tipoExecuteshell, vamospreencherocampo "Command”comum
201

## Página 220

7.3. Pipelinedeentrega CasadoCódigo
comando de três partes, separadas por&&. A primeira parte co-
piaoartefatoparaoservidor webusandoo scp. Asegundaparte
executaumcomandoremotonoservidor webparadescompactaro
artefatocopiado. Aterceiraparteiráiniciaraexecuç ãodoPuppet
usandoocomando puppet applyecolocandonossosmódulosno
modulepath.Ocomandocompleto,quepodeservistonafigura 7.12,
fica:
scp puppet.tgz vagrant@192.168.33.12: && \
ssh vagrant@192.168.33.12 ’tar zxvf puppet.tgz’ && \
ssh vagrant@192.168.33.12 ’sudo /opt/vagrant_ruby/bin/puppet
apply \ --modulepath=modules:librarian/modules manifests/web.pp’
Figura7.12:Comandosparadeploydalojavirtual
Aoclicarem Savetemosonossonovo jobparafazer deployemprodu-
ção. Vamosiniciaro deployclicandonobotão BuildNow nonovoprojeto.
Paranossasurpresa,o deployfalhacomumerro Permissiondenied,pleasetry
again.conformemostraafigura7.13.
202

## Página 221

CasadoCódigo Capítulo7. Pipelinedeentrega
Figura7.13:Erronatentativadedeployautomatizado
Istoacontecepoisousuário jenkinsqueexecutatodosos buildsnão
tempermissãoparacopiarouexecutarcomandosnoservidor web.Paracon-
sertarisso,precisamoslogarnamáquinavirtualeexecutaralgunscomandos
paratrocadechavesSSHentreosservidores:
$ vagrant ssh ci
vagrant@ci$ sudo su - jenkins
Ocomando sumudaasessãoparaousuário jenkins.Feitoisso,po-
demosrodarocomando ssh-keygenqueirágerarumpardechavesSSH
efaráalgumasperguntas:
jenkins@ci$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/var/lib/jenkins/.ssh/
id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /var/lib/jenkins/.ssh/
id_rsa.
Your public key has been saved in /var/lib/jenkins/.ssh/
203

## Página 222

7.3. Pipelinedeentrega CasadoCódigo
id_rsa.pub.
The key fingerprint is:
67:ae:7d:37:ec:de:1f:e7:c3:a8:15:50:49:02:9d:49
jenkins@precise32
The key’s randomart image is:
+--[ RSA 2048]----+
| .+E+o. |
| +o. |
| . |
| . |
| S o . |
| + . |
| . oo..|
| o o.+=o|
| . .o.+o.*|
+-----------------+
Usamosarespostapadrãoparatodasasperguntas,inclusivedeixando
o passphraseem branco. Com o par de chaves SSH criado, precisamos
copiarnossachavepúblicaparaoservidor web. Usaremosocomando
ssh-copy-idparaissoeasenhadousuário vagrantétambémvagrant:
jenkins@ci$ ssh-copy-id vagrant@192.168.33.12
vagrant@192.168.33.12’s password:
Now try logging into the machine, with ...
ComissoterminamosaconfiguraçãoSSHepodemossairdeambasas
máquinasvirtuais,novamenteexecutandoocomando logoutduasvezes:
jenkins@ci$ logout
vagrant@ci$ logout
$
Feitoisso,podemosiniciarumnovo deployparaproduçãoedessavez
tudofunciona! Afigura 7.14mostraasaídabemsucedidadoprocessode
deploy.
204

## Página 223

CasadoCódigo Capítulo7. Pipelinedeentrega
Figura7.14:Deployaocliquedeumbotãobemsucedido
7.4 Próximos Passos
Agoratemosumapipelinedeentregaautomatizadaquenospermitefazer de-
ployautomatizadoacada commitbemsucedido. Conformediscutimosdu-
ranteocapítulo,existemmaisalgumascoisasquevocêpodeexplorarpara
fortaleceroseuentendimentodosconceitosapresentados. Vocêpodeme-
lhoraracoberturadostestesdoPuppet.
OutroexercíciointeressanteéautomatizarasconfiguraçõesdoJenkins
quefizemosmanualmentenestecapítulo. Astécnicasqueusamosnocapí-
tulo6podemajudá-loaqui.Aindanotópicodeinfraestruturacomocódigo,
aclasse loja_virtual::ciestácomeçandoaficarcomplexaeapósaauto-
maçãodaconfiguraçãodosnovos jobs,ébemcapazquevocêpreciserefatorá-
la.
Quandocopiamosoarquivo .tarparaoservidor web,deixamososar-
quivosdescompactadossoltosporlá.Oidealseriafazerumalimpezaassim
queoprocessode deployterminarparagarantirquenãodeixamosnadapara
trás.Casoalgummódulosejaremovidoemum buildsubsequente,nãoque-
remosterproblemasnoprocessode deployporterdeixadoarquivossoltos
emum deployanterior.
205

## Página 224

7.4. PróximosPassos CasadoCódigo
NossadecisãodeempacotarocódigoPuppetcomoumarquivo .tar
ecopiá-lodeum buildparaooutrousandoumplugindoJenkinséapenas
umadaspossíveissolu ções.Existemoutrasopçõesdedistribuiçãodecódigo
Puppetquenãodiscutimosnolivro,masnadaimpedevocêdeexplorá-las.O
PuppetpossuiumcomponentechamadodePuppetMasterqueéumservidor
centralondeosnósdasuainfraestruturapodemseregistrarparasemanter
atualizados.Comoissorequermaisinfraestrutura,nósdecidimosseguiruma
abordagemsemoPuppetMastereusarumpoucomaisdeorquestraç ãoex-
terna.
Porfim,nossoprocessode deployapenasatualizaoservidor web.Gos-
taríamosdefazerum deploycompletodetodanossainfraestrutura,oupelo
menosdosservidoresqueafetamdiretamenteoambientedeexecuç ãodaapli-
cação.Umoutroexercíciointeressanteépensaremcomoimplementaresse
deploydoservidordebancodedadosjuntamentecomoservidor web.
206

## Página 225

Capítulo8
Tópicosavançados
JádiscutimosdiversosconceitosimportantesparaadotaçãodeDevOpseim-
plementamospráticasquepossibilitamaentregacontínua. Alémdacola-
boraçãoentredesenvolvedoreseoperações,umdosaspectosculturaismais
importantesdeDevOpséamelhoriacontínua.Assimcomoasreuniõesdere-
trospectivaajudamequipeságeisaadaptarseuprocessodedesenvolvimento,
precisamosusartécnicassemelhantesparaavaliareevoluiroprocessodeen-
tregadesoftware.
Melhoriacontínuaéumaformadeaplicarométodocientíficononosso
trabalho.Vocêcomeçacomumahipótesedemelhoria,combasenoseuins-
tintoouemobservaçõesefatossobreoseuprocessoatual.Vocêentãopropõe
umexperimentoparatestarsuahipótese.Issoimplicanacoletadenovosda-
dos,fatoseobservaçõesquepodemsuportarourefutarsuahipóteseinicial.
Esseciclodeaprendizadopossibilitaimplementarpequenasalteraçõesnoseu
processoparatorná-lomaisemaiseficiente.

## Página 226

CasadoCódigo
Nestecapítuloiremosabordaralgunstópicosmaisavan çados.Nossoob-
jetivonãoécriarumalistacompreensivadetodasastécnicas,ferramentas,
plataformasemetodologiasquevocêprecisaconhecer.Queremosabordaral-
gunstópicosimportantesparaquevocêtenhaconhecimentosuficientepara
decidirquaissãoospróximospassosapartirdaquinasuajornadademelho-
riacontínua.
Evoluindoumprocessodedeploymanualparaautomatizado
Nofinalde2012,euestavatrabalhandocomumclientequefazia deploy
emproduçãoumaouduasvezesporsemana. Elestinhamumprocessode
deploymanualqueprecisavaserexecutadoeacompanhadodepertoporum
dosengenheirosqueficavanoserviçoatémaistarde.Ostestadorestambém
ficavamtrabalhandoatétardepararealizaralgunstestesmanuaisbásicoslogo
apóscada deploy.
Certodia,esseengenheirocometeuumerroeesqueceudemudarum
arquivodeconfiguraçãoparausaraURLdeconexãocomobancodedados
corretas.Comisso,umdosprocessosdeindexaç ãoestavausandoobancode
dadoserrado.Oprocessonãofalhoueostestadoresnãoperceberamoerro
poisabuscaaindaestavafuncionando,porémcomresultadosincorretos.Por
isso,oproblemasófoidetectadonodiaseguintequandoumrepresentante
donegócioestavaapresentandooprodutoparaumpotencialcliente.
Comoestafalhateveumcustoaltoparaonegócio,eufaciliteiumareu-
niãode post-mortemcomosenvolvidosefizemosuma análisedecausaraiz
discutindoomotivodeoproblemateracontecidoassimcomopotenciaisme-
didasparaevitarqueeleserepetisse.Umdosresultadosdareuniãofoique
eupareassecomoengenheironopróximo deployparalevantardadossobre
osprocessosmanuaisquepoderiamserautomatizados.
Nasemanaseguinte,fiqueinotrabalhoatémaistardeparaacompanhar
oprocessode deployecomeceiapreencher post-itsparacadapassomanual
queeleexecutava.Eutambémtomavanotaquandoelenãotinhacertezado
quefazeraseguir:quaiscomandoseleexecutavaparadecidirsepodiaseguir
adianteounão.Aofinaldaquelanoite,tínhamosumaparedeinteiracoberta
depost-its.
Nodiaseguinte,fizemosumareuniãocomorestodaequipee,usandoos
208

## Página 227

CasadoCódigo Capítulo8. Tópicosavançados
post-itscomodados,criamosváriasideiasparaautomatizarastarefaseveri-
ficaçõesmaisproblemáticas.Nãoimplementamostodasassugestõesimedi-
atamente,masusamosessenovoconhecimentoparaconvencerosrepresen-
tantesdonegócioparaalocarumacertacapacidadedaequipeparatrabalhar
nessasmelhoriasduranteaspróximasiterações.
Apósalgunsmeses,oprocessode deployestavaquasetotalmenteautoma-
tizadoedescobrimosdiversastarefasmanuaisquepoderiamserexecutadas
etestadasemoutrosambientesantesdeexecutá-lasemproduç ão.Apesardo
processoautomatizado,meuclienteaindanãoestavaconfortávelemexecu-
tardeploysduranteodia,porissoaindaficávamosnotrabalhoatétarde.No
entantoagoratínhamosbemmenossurpresaspoiserasóapertarumbotãoe
esperaroprocessoterminar.
8.1 Fazendo deploy na nuvem
Ocustodemanterum datacenter comhardwarefísicoéaltoparaempresas
depequenoemédioporte. Alémdisso,fazerplanejamentodecapacidade
nessasituaçãoédifícilpoisvocêprecisapreversuataxadecrescimentoantes
mesmodeterseuprimeirousuário.
Nosúltimosanos,empresascome çaramainvestiremtecnologiasdevir-
tualizaçãoparatentaraproveitarmelhoracapacidadedosservidoresfísicos
quejápossuíam.Commáquinasvirtuais,vocêpoderodarmaisdeumservi-
dornamesmamáquinafísica,ajudandoacontrolaroscustoscomcomprae
manutençãodohardwareedo datacenter.
Enquantoisso,empresasdainternetcomoaAmazoninvestirammuito
dinheiroparamontarumainfraestruturarobustaqueaguentasseopicode
acessosecomprasdofinaldoano.Norestantedoano,osservidoressãosubu-
tilizados,deixandorecursoscomputacionaisdisponíveis.Foidaíquetiveram
aideiadealugaresseexcessoderecursosparapotenciaisclientes,criando
umadasinovaçõesmaisimportantesnomundodatecnologiadosúltimos
tempos:acomputaçãoemnuvem.
Omodelode computaçãoemnuvem possibilitanovasmaneirasdecon-
tratarepagarpelainfraestrutura,apresentandocincocaracterísticasessenci-
ais[8]:
209

## Página 228

8.1. Fazendodeploynanuvem CasadoCódigo
•Serviçosobdemanda: umconsumidorpodeprovisionarinfraestru-
turadecomputaçãosobdemandaedeformaautomatizada,semane-
cessidadedeinteraçãohumanacomalguémdoseuprovedordeservi-
ços.
•Amploacessoàrede:osrecursosdanuvemestãodisponíveisnarede
epodemseracessadosporclientesdequalquertipodeplataforma–
dispositivosmóveis, tablets,laptopsououtrosservidores.
•Poolderecursos:osrecursosdecomputaçãodoprovedorfazemparte
deum poolcompartilhadoquepodeserusadoporváriosconsumido-
res.Geralmente,recursosnanuvemabstraemsuareallocalizaç ãodos
consumidores. Emalgunscasos,consumidorespodemespecificara
localizaçãodesejada,masissoaconteceemumníveldeabstraç ãomais
alto–comoumcertopaís,estadoou datacenter.
•Elasticidade: recursospodemserprovisionadoseliberadosrapida-
mente–atédeformaautomatizadaemalgunscasos–paraqueainfra-
estruturapossaescalardeacordocomademanda.Dopontodevista
doconsumidor,osrecursosnanuvemsãopraticamenteinfinitos.
•Serviçomensurado:serviçosnanuvemcontrolamemensuramauto-
maticamenteousodecadarecurso.Damesmaformaqueumhidrô-
metromedeoquantodeáguavocêgastounomês,seuprovedoriráusar
essesdadosparacobrarpelouso.Ousodessesrecursospodesermo-
nitorado,controladoegerarrelatóriosquetrazemtransparênciatanto
paraoprovedorquantoparaoconsumidor.
Existemtambémtrêsmodelosdeserviçonacomputaçãoemnuvem,com
diferentesníveisdeabstração:
•IaaS(InfrastructureasaService ouInfraestruturacomoServiço):dis-
ponibilizarecursosdeinfraestruturafundamentaiscomocomputação,
armazenagemouserviçosderede. Oconsumidortembastantecon-
troledasconfiguraçõesdessescomponentes,inclusivepodendoesco-
lhereacessarosistemaoperacional. ExemplosdeofertasIaaSsão:
AWS,OpenStack,DigitalOcean,AzureeGoogleCompute.
210

## Página 229

CasadoCódigo Capítulo8. Tópicosavançados
•PaaS(PlatformasaService ouPlataformacomoServiço):disponibi-
lizaumaplataformagerenciadaondeoconsumidorpodefazer deploy
dasuaaplicação.Oconsumidorgeralmentenãoconseguecontrolara
infraestruturadiretamente,apenasassuasaplicaçõesepossivelmente
configuraçõesdoambientedeexecução.ExemplosdeofertasPaaSsão:
Heroku,GoogleAppEngine,ElasticBeanstalk,OpenShifteEngine
Yard.
•SaaS(SoftwareasaService ouSoftwarecomoServiço):disponibiliza
umprodutoouserviçocujainfraestruturaestárodandonanuvem.O
consumidornãocontrolaougerenciaainfraestruturanemmesmoa
aplicaçãoemsi,apenasassuasconfiguraçõesdentrodoproduto.Di-
versosserviçosonlinepodemserconsideradosSaaS:GMail,Dropbox,
Evernote,Basecamp,SnapCIeoTravisCI.
Existemdiversosprovedorespúblicoseprivadosdecomputaç ãoemnu-
vem.AAmazonfoiapioneiranaáreacomoAmazonWebServicesouAWS
(http://aws.amazon.com/),oferecendoinfraestruturacomoserviço(IaaS)e
umagrandeofertadeprodutosesoluções. Apesardeserumserviçopago,
elaofereceumafaixadeusográtisnoprimeiroanoapósvocêcriarumanova
conta. Devidoàsuaflexibilidadeematuridade,vamosexplorarcomosubir
nossoambientedeproduçãonoAWS.
ConfigurandooambientenoAWS
CriarumanovacontanoAWSérelativamentesimpleseexigequevocê
tenhaemmãosumcelulareumcartãodecrédito.Comoeleslan çamnovos
produtoseofertasmuitofrequentemente,esseprocessoinicialdecria çãode
contaestásempremudandoeficandomaissimples.Poressemotivonãova-
mosdescrevê-lopassoapasso,masvousuporquevocêjátenhaumaconta
configuradaeativada.
OprincipalserviçodoAWSéoEC2,ou ElasticComputeCloud,quenos
provêunidadesdecomputaçãonanuvem. Comelevocêdecidequantaca-
pacidadedecomputaçãovocêprecisaeprovisionaosservidoresdesejados
comumachamadadeAPIouocliquedeumbotão.Éumaformarápidade
conseguirumnovoservidornanuvem.
211

## Página 230

8.1. Fazendodeploynanuvem CasadoCódigo
ComacontaAWScriada,vocêpodeacessaroconsoledegerenciamento
naURLhttps://console.aws.amazon.com/ everáatelaprincipalmostradana
figura8.1.Nessatelavocêpodeterumaideiadaquantidadedeserviçosofe-
recidospelaAmazon.OEC2éumdoslinksnase çãoCompute&Networking.
Figura8.1:ConsoledecontroleAWS
ClicandonolinkdoEC2vocêélevadoparaopaineldecontroledesse
serviço.AprimeiracoisaqueprecisamosfazerécriarumpardechavesSSH
paraconseguiracessarnossosservidoresumavezqueforemcriados. Para
isso,acesseolink "KeyPairs”nomenulateralecliquenobotão CreateNew
Pairconformemostradonafigura 8.2.
212

## Página 231

CasadoCódigo Capítulo8. Tópicosavançados
Figura8.2:CriandoumnovopardechavesdeacessoSSH
Preenchaocampo Keypairname comonomedachave devopseclique
emYes. Oarquivodachaveprivada devops.pemserábaixadoconforme
mostraafigura 8.3.Vocêprecisasalvá-laemumlugarseguropoisaAmazon
nãoguardaumacópiadessearquivoparavocê,poisseriaumaviolaç ãode
segurança.Anoteocaminhoondevocêsalvarachaveprimária,poisiremos
usá-lonapróximase ção. Porenquanto,vamospresumirqueoarquivote-
nhasidosalvonoseudiretório HOMEem ~/devops.pem.Comissovamos
conseguiracessarnossosservidoresporSSH.
213

## Página 232

8.1. Fazendodeploynanuvem CasadoCódigo
Figura8.3:Pardechavescriadoedownloaddachaveprimária
OpróximoserviçoquevamosutilizaréoVPC,ou VirtualPrivateCloud.
OVPCnospermitecriarumase çãoisoladadoAWSondepodemosprovisi-
onarrecursoseterumpoucomaiscontrolesobreaconfiguraç ãoetopologia
darede.AosubirumservidorEC2dentrodeumaVPC,podemosescolher
seuIPinterno.Comesseserviçovamosconseguirmanteramesmatopologia
deredequeusamosparaosnossosservidoreslocaisnoVirtualBox.
ParacriarumanuvemprivadanoVPC,cliquenolink VPCdentrodo
menuServicesdoconsole.NopaineldecontroledoVPC,cliqueem Getstar-
tedcreatingaVPC conformemostraafigura 8.4.
214

## Página 233

CasadoCódigo Capítulo8. Tópicosavançados
Figura8.4:PaineldecontroledoVPC
Escolhaaop çãoVPCwithaSinglePublicSubnetOnly conformemostra
afigura8.5.Issovaicriarumatopologiaderedecomumúnicosegmentode
redepúblico,comacessodiretoàinternet.
Figura8.5:CriandoumanovaVPC
215

## Página 234

8.1. Fazendodeploynanuvem CasadoCódigo
Aoclicarem Continuevocêserálevadoparaapróximateladeconfigura-
çãoondeiremosdefinirnossosegmentoderede.Primeiramentevamosclicar
nolink EditVPCIPCIDRBlock epreencherocampo IPCIDRblock como
valor 192.168.0.0/16. Iremoscolocaromesmovalornocampo Public
Subnetapósclicarnolink EditPublicSubnet,conformemostraafigura 8.6.
Figura8.6:ConfiguraçõesdesegmentosderedenoVPC
Porfim,bastaclicarem CreateVPC paracriarnossanuvemprivadae
veremosumamensagemdesucessoconformemostraafigura 8.7.
216

## Página 235

CasadoCódigo Capítulo8. Tópicosavançados
Figura8.7:NuvemprivadanoVPCcriadacomsucesso
PrecisamosagoraanotaroIDdonossosegmentoderedeparausona
próximase ção. Paraistocliquenolink Subnetsnomenulateraleescolhaa
subnetcriada.Nestatelavocêveráosdetalhesdosegmentoderedeconforme
mostraafigura 8.8. AnoteoIDnasuatelaqueserádiferentedoqueestá
destacadonafiguraumavezqueoAWSalocaumnovoIDúnicosempreque
umnovorecursoforcriado.
217

## Página 236

8.1. Fazendodeploynanuvem CasadoCódigo
Figura8.8:AnotandooIDdasubnetcriada
AúltimaconfiguraçãoqueprecisamosfazernoconsoledoAWSécon-
figurarum securitygroup,ougrupodeseguran ça. Umgrupodeseguran ça
defineasregrasdeacessoainstânciasEC2.Eleéumaespéciede firewallque
bloqueiaoupermiteacessoparadentroouforadainstância,dependendode
suasconfigurações.
Vamosclicarnolink SecurityGroupsnomenulateraleselecionarogrupo
deseguran çadefault. Nosdetalhes,cliquenaaba Inboundparaadicionar
4novasregrasparapermitiracessoSSH,HTTPeHTTPSnasportas22,
80/8080e443respectivamente,conformemostraafigura 8.9.Cliqueem Ap-
plyRuleChanges paraqueasmudan çastenhamefeito.
218

## Página 237

CasadoCódigo Capítulo8. Tópicosavançados
Figura8.9:CriandoumanovaVPC
Provisionandoosservidoresdeprodu çãonoAWS
Para provisionar os servidores de produção no AWS vamos usar um
plugin do Vagrant chamadovagrant-aws (https://github.com/mitchellh/
vagrant-aws).AsversõesmaisnovasdoVagrantfuncionamcomprovedores
alémdoVirtualBoxeessepluginconfiguraumprovedorquesabeprovisionar
noAWS.Instalaropluginésimples:
$ vagrant plugin install vagrant-aws
Installing the ’vagrant-aws’ plugin. This can take a few
minutes...
Installed the plugin ’vagrant-aws (0.4.1)’!
Alémdisso,precisamostambémimportaruma boxdiferentequeserá
usadapeloplugin. Conformeadocumentaçãodopluginrecomenda,cha-
maremosessa boxde dummyeparaadicioná-labastaexecutarocomando:
$ vagrant box add dummy \
> https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box
Downloading box from URL: https://github.com/mitchellh/...
Extracting box...e: 0/s, Estimated time remaining: --:--:--)
Successfully added box ’dummy’ with provider ’aws’!
219

## Página 238

8.1. Fazendodeploynanuvem CasadoCódigo
Comoplugininstaladoeonovo boxdisponível,podemosalterarnosso
arquivodeconfiguraçãodoVagrantparaadicionarasconfiguraçõesdeacesso
aoAWS.Faremosissoalterandooarquivo Vagrantfile:
VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
config.vm.box = "hashicorp/precise32"
...
config.vm.provider :aws do |aws, override|
aws.access_key_id = "<ACCESS KEY ID>"
aws.secret_access_key = "<SECRET ACCESS KEY>"
aws.keypair_name = "devops"
aws.ami = "ami-a18c8fc8"
aws.user_data = File.read("bootstrap.sh")
aws.subnet_id = "<SUBNET ID>"
aws.elastic_ip = true
override.vm.box = "dummy"
override.ssh.username = "ubuntu"
override.ssh.private_key_path = "<PATH DA CHAVE PRIVADA>"
end
config.vm.define :db do |db_config|
...
db_config.vm.provider :aws do |aws|
aws.private_ip_address = "192.168.33.10"
aws.tags = { ’Name’ => ’DB’ }
end
end
config.vm.define :web do |web_config|
...
web_config.vm.provider :aws do |aws|
aws.private_ip_address = "192.168.33.12"
aws.tags = { ’Name’ => ’Web’ }
end
end
220

## Página 239

CasadoCódigo Capítulo8. Tópicosavançados
config.vm.define :monitor do |monitor_config| ... end
config.vm.define :ci do |build_config|
...
build_config.vm.provider :aws do |aws|
aws.private_ip_address = "192.168.33.16"
aws.tags = { ’Name’ => ’CI’ }
end
end
end
Vocêvaiprecisarfazeralgumassubstituiçõesusandoassuaspróprias
configuraçõesdoAWSqueobtivemosnase çãoanterior. Osvalorespara
subnet_ide private_key_pathnósjátemosanotadosdase çãoanterior.
Paraconseguirosvaloresdo access_key_idedo secret_access_key,
vocêpodeacessarolink SecurityCredentials nomenudeusuáriomostrado
nafigura8.10.
Figura8.10:Menuparaacessarcredenciaisdeseguran ça
Napróximatela,aoexpandirase çãoAccessKeysvocêveráumbotãoCre-
ateNewAccessKey conformemostraafigura8.11.
221

## Página 240

8.1. Fazendodeploynanuvem CasadoCódigo
Figura8.11:Menuparaacessarcredenciaisdeseguran ça
Após criar oaccess keycom sucesso você verá uma nova tela que
lhe dará os valores para preencher nos camposaccess_key_id e
secret_access_keyconformemostraafigura 8.12.Essassãosuascreden-
ciaispessoais,porissonãoascompartilhecomninguém.Sealguémobtiver
suascredenciais,eleconseguirásubirmáquinasevocêteráquepagaraconta!
222

## Página 241

CasadoCódigo Capítulo8. Tópicosavançados
Figura8.12:Menuparaacessarcredenciaisdeseguran ça
No Vagrantfiledefinimosalgumasoutrasconfiguraçõesdoprovedor
AWS.O keypair_nameéonomedopardechavesquecriamosnase ção
anterior.O amiéoIDdaimagembasequeoAWSusaráparacriarumnovo
servidor. Nessecaso,oID "ami-a18c8fc8"correspondeaumaimagem
basedoUbuntu12.04LTSde32bits,amesmaversãodosistemaoperacional
earquiteturausadosnasmáquinasvirtuaisdoVirtualBox.
Porfim,oparâmetro user_dataapontaparaumnovoarquivoquepre-
cisamoscriar. AosubirumanovainstâncianoEC2,vocêpodepassarum
pequenoscriptqueseráexecutadoassimqueamáquinasubirpelaprimeira
vez.Nessecaso,precisamosdeum scriptparainstalaroPuppetemsi,quenão
vempré-instaladonaAMIqueescolhemos.Oconteúdodessenovoarquivo
bootstrap.shdeveser:
#!/bin/sh
set -e -x
export DEBIAN_FRONTEND=noninteractive
wget https://apt.puppetlabs.com/puppetlabs-release-precise.deb
dpkg -i puppetlabs-release-precise.deb
223

## Página 242

8.1. Fazendodeploynanuvem CasadoCódigo
apt-get -y update
apt-get -y install puppet-common=2.7.19* facter=1.7.5*
Essescriptérelativamentesimples. Oscomandos wgete dpkg -i
configuramumnovorepositóriodepacotescomtodosos releasesdoPup-
petmantidospelaprópriaPuppetLabs. Comisso,simplesmenteusamoso
comando apt-getparaatualizarseuíndicedebuscaeinstalarospacotes
doPuppetnaversão2.7.19edoFacternaversão1.7.5,asmesmasqueestamos
usandonasmáquinasvirtuaislocaisdoVirtualBox.
Pronto,agorapodemosprovisionarnossosservidoresdeproduç ãono
AWScomoVagrantusandoumanovaop ção --provider=aws,come-
çandopeloservidor db:
$ vagrant up db --provider=aws
Bringing machine ’db’ up with ’aws’ provider...
==> db: Installing Puppet modules with Librarian-Puppet...
==> db: Warning! The AWS provider doesn’t support any of the
==> db: Vagrant high-level network configurations
==> db: ( `config.vm.network`). They will be silently ignored.
==> db: Launching an instance with the following settings...
==> db: -- Type: m1.small
==> db: -- AMI: ami-a18c8fc8
...
notice: Finished catalog run in 39.74 seconds
Casovejaumamensagemdeerrodizendoqueoservidorjáestápro-
visionado com um provedor diferente, simplesmente faça um vagrant
destroy db ci webparadestruirassuasmáquinasvirtuaislocais. Em
futurasversõesdoVagrantvocêvaipodersubiromesmoservidorusando
diferentesprovedoresaomesmotempo.Apósdestruí-las,vocêpodeexecu-
tarocomando vagrant up db --provider=awsnovamenteeeleirá
funcionarconformemostradoanteriormente.
Temosnossoprimeiroservidorrodandonanuvem! Opróximoseráo
servidor ci,poisprecisamospublicaropacote .debqueseráusadopelo
servidor webposteriormente.Masantesdefazerisso,vamosfazerumape-
quenaalteraçãonaclasse loja_virtual::repopoisnoEC2teremosape-
nasumainterfacederede eth0enossomóduloassumequeorepositório
224

## Página 243

CasadoCódigo Capítulo8. Tópicosavançados
seráacessívelnoendereçoIPdainterface eth1.Fazemosestaalteraçãono
finaldoarquivo modules/loja_virtual/manifest/repo.pp:
class loja_virtual::repo($basedir, $name) {
package { ’reprepro’: ... }
$repo_structure = [...]
file { $repo_structure: ... }
file { "$basedir/conf/distributions": ... }
class { ’apache’: }
if $ipaddress_eth1 {
$servername = $ipaddress_eth1
} else {
$servername = $ipaddress_eth0
}
apache::vhost { $name:
port => 80,
docroot => $basedir,
servername => $servername,
}
}
AquiestamosusandoumanovasintaxedoPuppetparaexpressõescon-
dicionais.Seavariável $ipaddress_eth1estiverdefinida,elaseráusada,
casocontráriousaremos $ipaddress_eth0. Issopermitequenossocó-
digoPuppetcontinuefuncionandolocalmentecomasmáquinasvirtuaisdo
VirtualBox.Podemosagorasubiroservidor cinanuvem:
$ vagrant up ci --provider=aws
Bringing machine ’ci’ up with ’aws’ provider...
==> ci: Installing Puppet modules with Librarian-Puppet...
==> ci: Warning! The AWS provider doesn’t support any of the
==> ci: Vagrant high-level network configurations
==> ci: ( `config.vm.network`). They will be silently ignored.
==> ci: Launching an instance with the following settings...
==> ci: -- Type: m1.small
==> ci: -- AMI: ami-a18c8fc8
...
notice: Finished catalog run in 423.40 seconds
225

## Página 244

8.1. Fazendodeploynanuvem CasadoCódigo
Comoservidorprovisionado,oJenkinsiráiniciarumnovo builddaloja
virtualetentarápublicarumnovopacote .deb. Selembrarmosoquefoi
precisofazernocapítulo 7paraconfigurarorepositório,vamosprecisarlogar
namáquinaparageraropardechavesGPGeexportarachavepública.Caso
nãolembredetodosospassos,releiaocapítuloanterior,selembrar,sigaas
mesmasinstruçõesmostradasadiante:
$ vagrant ssh ci
ubuntu@ip-192-168-33-16$ sudo apt-get install haveged
Reading package lists... Done
...
Setting up haveged (1.1-2) ...
ubuntu@ip-192-168-33-16$ sudo su - jenkins
jenkins@ip-192-168-33-16$ gpg --gen-key
gpg (GnuPG) 1.4.11; Copyright (C) 2010 ...
...
pub 2048R/3E969140 2014-03-11
Key fingerprint =
2C95 5FF8 9789 14F9 D6B3 ECD4 4725 6390 ...
uid Loja Virtual <admin@devopsnapratica.com.br>
sub 2048R/67432481 2014-03-11
jenkins@ip-192-168-33-16$ gpg --export --armor \
> admin@devopsnapratica.com.br > /var/lib/apt/repo/
devopspkgs.gpg
jenkins@ip-192-168-33-16$ logout
ubuntu@ip-192-168-33-16$ logout
Connection to 54.84.207.166 closed.
$
Não se esqueça de anotar o ID da chave pública gerada, nesse
casso 3E969140, e substituir o parâmetro key do recurso
Apt::Source[devopsnapratica] na classe loja_virtual::web.
Agorabastaesperarqueonosso buildtermineepubliqueopacote .deb.
Paraacompanharoprogressodo build,vocêprecisadescobrironomedo
hostpúblicodoservidorJenkinsnoAWS.Paraisto,acesseolink Instances
nomenulateraldopaineldecontroledoEC2,selecioneoservidor“CI”e
copieovalordocampo PublicDNSconformemostraafigura 8.13.
226

## Página 245

CasadoCódigo Capítulo8. Tópicosavançados
Figura8.13:NomedohostpúblicodoservidordeCI
Com o endereço em mãos, acesse o Jenkins em uma nova janela
do navegador, usando a porta 8080. Nesse caso, nossa URL éhttp://
ec2-54-84-207-166.compute-1.amazonaws.com:8080/evocêveráoJenkins
rodandonanuvemconformemostraafigura 8.14.
Figura8.14:Jenkinsrodandonanuvem
227

## Página 246

8.1. Fazendodeploynanuvem CasadoCódigo
Assimqueo buildcompletarcomsucesso,vocêpodeprovisionaroservi-
dor web:
$ vagrant up web --provider=aws
Bringing machine ’web’ up with ’aws’ provider...
==> web: Installing Puppet modules with Librarian-Puppet...
==> web: Warning! The AWS provider doesn’t support any of the
==> web: Vagrant high-level network configurations
==> web: ( `config.vm.network`). They will be silently ignored.
==> web: Launching an instance with the following settings...
==> web: -- Type: m1.small
==> web: -- AMI: ami-a18c8fc8
...
notice: Finished catalog run in 88.32 seconds
Vocêpodeusaromesmoprocedimentoparadescobrironomedohost
públicodoservidor webnoAWS,conformemostraafigura 8.15.
Figura8.15:Nomedohostpúblicodoservidorweb
Nonossocaso,aoacessar http://ec2-54-85-98-13.compute-1.amazonaws.
com:8080/devopsnapratica/veremosnossalojavirtualrodandonanuvem,
conformemostraafigura 8.16.Sucesso!Conseguimosmigrarnossaaplicação
228

## Página 247

CasadoCódigo Capítulo8. Tópicosavançados
paraanuvemsemmuitadordecabe ça. Oinvestimentoemautomaçãodo
processovaleuapena.
Figura8.16:Lojavirtualrodandonanuvem
ComoosrecursosnoAWSsãopagos,precisamosdestruirosservidores
paraeconomizardinheiro. Cuidado!Sevocêesquecerestepasso,vocêre-
ceberáumacontainesperadanofinaldomês!
$ vagrant destroy ci web db
db: Are you sure you want to destroy the ’db’ VM? [y/N] y
==> db: Terminating the instance...
==> db: Running cleanup tasks for ’puppet’ provisioner...
web: Are you sure you want to destroy the ’web’ VM? [y/N] y
==> web: Terminating the instance...
==> web: Running cleanup tasks for ’puppet’ provisioner...
ci: Are you sure you want to destroy the ’ci’ VM? [y/N] y
==> ci: Terminating the instance...
==> ci: Running cleanup tasks for ’puppet’ provisioner...
Paragarantirqueasinstânciasforamrealmenteterminadas,acesseolink
"Instances”nomenulateraldopaineldecontroledoEC2evocêdeveveralgo
parecidocomafigura 8.17.
229

## Página 248

8.2. DevOpsalémdasferramentas CasadoCódigo
Figura8.17:InstânciasEC2terminadas
8.2 DevOps além das ferramentas
Seriaimpossívelcobrirtodasasferramentasetécnicasqueestãoevoluindono
mundoDevOpsnestelivro.Paratodosostópicosabordados,existemdiversas
ferramentasalternativassendousadaspelacomunidade.Alémdisso,existem
ostópicosquenãoforamabordadosesuasrespectivasop çõesdeferramentas.
Omotivodetermosusadoasferramentasqueusamosfoiparamostrar
umexemplopráticodeentregacontínuaeDevOps.DevOpsémaisdoque
suasescolhasdeferramentas.JohnWilliseDamonEdwardsdefiniramoacrô-
nimoCAMSparadefiniroqueéDevOps[19]eJezHumblemaistardeintro-
duziuLeanparacompletaroacrônimo CALMS:
•(C)ultura:pessoaseprocessossãomaisimportantes.Seaculturanão
estiverpresente,qualquertentativadeautomaç ãoestádestinadaafa-
lhar.
•(A)utomação:libereoshumanospararealizartarefasqueexigemcri-
atividadeeintuiçãoedeixeastarefasrepetitivasparaoscomputadores,
quesabemexecutá-lasrapidamenteedeformabemmaisconfiável.
230

## Página 249

CasadoCódigo Capítulo8. Tópicosavançados
•(L)ean(pensamentoenxuto):diversosprincípios leaninfluenciama
culturaDevOps,comoamelhoriacontínua,ofocoemqualidade,aeli-
minaçãodedesperdícios,aotimizaçãodotodoeorespeitoàspessoas.
•(M)edição:sevocênãosoubermedir,nãosaberáavaliarseestámelho-
randooupiorando.Umaado çãodeDevOpsdesucessoirámedirtudo
oqueforpossível,porexemplo:métricasdedesempenho,métricasde
processo,métricasdenegócioetc.
•(S)haring(compartilhamento):acolaboraçãoeocompartilhamento
deideiaseconhecimentoajudamacriaraculturanecessáriaparao
sucessocomDevOps.
Comessascaracterísticasemmente,vamosdiscutiralgunsdostópicos
quenãoforamabordadosnolivroparaquevocêprossigacomseusestudos
sobreDevOps.Nãoseesque çadoúltimoprincípio:compartilheoquevocê
aprenderecontribuacomacomunidade!Compartilharhistóriaséumadas
melhoresmaneirasdecriarconhecimento.
8.3 Sistemas av ançados de monitoramento
Osistemademonitoramentoqueconfiguramosnocapítulo 3focanadetecção
enotificaçãodefalhasnoambientedeproduç ão.ONagioséumaferramenta
bastantecomumnaindústria,porémtemsuaslimitações:ainterfacegráfica
éantiquadaedifícildeusar,suasarquivosdeconfiguraç ãosãocomplicados
enão-intuitivoseemumambientemaisdinâmicoondeservidorespodemir
eviraqualquermomento,oNagiosnãoéumaferramentamuitoflexível.
Existemoutrosaspectosimportantesquedevemserconsideradosemum
sistemademonitoramentomaiscompleto.Emparticular,algumasáreasestão
recebendobastanteatençãodacomunidadeediversasferramentaseprodutos
estãosurgindoparaatacá-las:
•Agregaçãode logs:quantomaisservidoresvocêpossuir,maisdifícilé
investigaredepurarproblemas.Aabordagemtradicionaldelogarno
servidorefazerum grepnosarquivosnãofuncionapoisvocêpre-
cisaficarconectandoemdiversosservidoresparadepurarumúnico
231

## Página 250

8.3. Sistemasavançadosdemonitoramento CasadoCódigo
problema. Poressemotivo,diversasferramentasdeagregaç ãoein-
dexaçãodelogsestãosurgindo. Umconjuntodeferramentasdecó-
digolivretemganhadopopularidadenessaárea: o Logstash(http:
//logstash.net/)coleta, filtra, analisaearmazenaentradasde log de
diversasfontesdiferentesno Elasticsearch(http://elasticsearch.org/),
umaferramentadebusca.Outrasop çõesnesseespaçosãooGraylog2
(http://graylog2.org/),o Splunk(http://www.splunk.com/),o Loggly
(https://www.loggly.com/),o PaperTrail(https://papertrailapp.com/)
eoLogentries(https://logentries.com/).
•Métricas:eumelembroquealguémmedisseumavezque“vocênão
temumproblemadedesempenho, vocêtemumproblemadevisi-
bilidade”. Sevocêenxergarondeequandooproblemaacontecevai
sermuitomaisfácilresolvê-lo. PorissoDevOpsencorajavocêame-
diromáximopossível. Métricaspodemserdesistema,daaplicaç ão,
doprocesso, denegócioouatédaspessoas. Existemalgumasfer-
ramentasevoluindonesteespaçoquepermitemacapturaearmaze-
namentodemétricas. Abiblioteca Metrics(http://metrics.codahale.
com/)escritaemJavapeloCodaHaleecomalgumasvariaçõesem
outraslinguagensprovêumaboaAPIparaquedesenvolvedorespas-
semapublicardiversostiposdemétricaapartirdocódigo. Nolado
daagregaçãoearmazenamentoexistemferramentascomoo StatsD
(https://github.com/etsy/statsd/), oCollectD (http://collectd.org/),
oCarbon(http://graphite.wikidot.com/carbon) , oRiemann(http:
//riemann.io/),o Ganglia(http://ganglia.sourceforge.net/),o Tem-
poDB(https://tempo-db.com/),o OpenTSDB(http://opentsdb.net/)
eoLibrato(https://metrics.librato.com/).
•Visualizações: quantomaisdadosemétricasvocêcoletar,maioréo
riscodevocêsofrerumasobrecargadeinformações. Porissoéim-
portanteinvestiremferramentasetécnicasdevisualizaç ãodeinfor-
maçãoparasintetizargrandesvolumesdedadosemumformatomais
digestívelparahumanos. Algumasferramentasnesseespaçosãoo
Graphite(http://graphite.wikidot.com/),o Cubism.js(http://square.
github.io/cubism/),o Tasseo(https://github.com/obfuscurity/tasseo)
232

## Página 251

CasadoCódigo Capítulo8. Tópicosavançados
eoGraphene(http://jondot.github.io/graphene/).
•Informaçõesemtempodeexecu ção:paraentenderondeestãoosgar-
galosdasuaaplicaçãoemprodução,vocêprecisacoletarinformações
emtempodeexecução.Comissovocêpodedescobrirquantotempo
seucódigoestágastandoemchamadasexternas,renderizandopági-
nasHTMLouquaisconsultasestãolevandomuitotemponobancode
dados. Outraáreaquetemganhadoimportânciaéacapturadeda-
dosdopontodevistadeusuário,porexemplo: quantotempoasua
páginademoraparacarregarnonavegadordousuário. Ferramentas
nesseespaçosãooNewRelic(http://newrelic.com/),o GoogleAnaly-
tics(http://www.google.com/analytics/)eo Piwik(http://piwik.org/).
Alémdisso,éimportantetambémcapturarerroscomferramentacomo
oNewRelicouoAirbrake(https://airbrake.io/).
•Monitoramentodedisponibilidade:outrotipodemonitoramentoé
saberquandoasuaaplicaç ãoestánoarounão. Sevocêtiverusuá-
riosdistribuídosaoredordomundo,essetipodemonitoramentoé
aindamaisimportante,poisvocêpodeestarindisponívelemapenas
algunslugaresenãooutros. Ferramentasnesseespaçosãoo Ping-
dom(https://www.pingdom.com/),o NewRelic,o Monitor.us(http:
//www.monitor.us/)eo UptimeRobot(http://uptimerobot.com/).
•Sistemasanalíticos:todosessesdadospodemserconsumidosporum
sistemaanalíticoparatentarencontrarcorrelações,tendências,ou in-
sightsavançadossobreseusistema. Aindanãoexistemmuitasferra-
mentasnesseespaço,porémoNewVem(http://www.newvem.com/)
possuialgunsrelatóriosanalíticosinteressantessobreusoderecursos
nanuvemparaotimizarseuscustos.
Soluçõesdemonitoramentomaisholísticastentamatacartodasessas
áreas,permitindoquevocêmonitoreemdiversosníveiseagregueinforma-
çõesemumúnicolugar.Comissovocêpodedetectarcorrelaçõesentredados
independentes.O NewRelic(http://newrelic.com/)éumprodutoSaaSpago
queestátentandoirnessadire ção.
233

## Página 252

8.4. Pipelinesdeentregacomplexas CasadoCódigo
Quantomaisavan çadoecompletoforoseusistemademonitoramento,
maiorvaisersuaconfian çaparafazermais deploysemprodução.Adetecção
deproblemasoperacionaissetornaumaextensão–eemalgunscasosaté
umasubstituição–doseuprocessodetestes.AIMVU,porexemplo,realiza
maisde50 deployspordiaecriouumsistemadeimunidadequemonitora
diversasmétricasduranteum deploy.Quandoalgumproblemaderegressão
édetectado,essesistemareverteoúltimo commitautomaticamenteeenvia
alertasparaprotegerosistemaemproduç ão[5].
8.4 Pipelines de entrega complexas
Nonossoexemplodocapítulo 7configuramosumapipelinedeentregabem
simplificada.Nomundoreal,écomumqueexistammaisestágioseambientes
pelosquaisumaaplicaçãoprecisapassarantesdechegaremproduç ão. Em
casosmaiscomplexos,vocêterádiversasaplicações,componenteseserviços
queseintegramentresi.Nessassituações,vocêvaiprecisardemaisníveisde
testedeintegraçãoparagarantirqueoscomponenteseserviçosseintegram
corretamente.
CriaregerenciarpipelinesmaiscomplexascomoJenkinscome çaafi-
carmaiscomplicadoconformeonúmerode jobscresce. Apipelinenãoé
umconceitoprimáriodoJenkins,maspodesermodeladausandodependên-
ciasegatilhosentre jobs,comofizemosnocapítuloanterior.Nesseespaço,a
ferramentaGo(http://www.go.cd/)escritapela ThoughtWorksteveseucó-
digorecentementeabertoefoiescritacomapipelinedeentregaemprimeiro
plano.Comummodelodeexecuçãode jobsdistribuídoeumaformademo-
delardiferentesambientes,oGoéumaop çãoatraenteparagerenciarpipeli-
nescomplexas.
8.5 Gerenciando mudanças no banco de dados
Umdosassuntosquenãoabordamosmasémuitoimportanteécomogeren-
ciarmudançasnobancodedados. Nanossaaplicação,oHibernatecriao
schemainicialdetabelasepreenchecomosdadosdereferênciadalojavir-
tual.Nomundoreal,o schemadobancodedadosiráevoluirevocênãopode
simplesmenteapagarereconstruirosdadosacada deploy.
234

## Página 253

CasadoCódigo Capítulo8. Tópicosavançados
Paralidarcomaevoluçãodobancodedados,geralmentetentamosde-
sacoplaroprocessode deploydaaplicaçãodoprocessode deploydobanco
dedados.Porexigirmaiscuidado,algumasempresasoptamporatualizaro
bancodedadosumavezporsemanaenquantoaaplicaç ãovaiparaprodução
diversasvezespordia.Práticasparaevoluiro schemadeumbancodedados
deformaseguraestãodescritasnoslivrosdePramosSadalage“Refatorando
bancodedados”[9]e“Receitasparaintegraçãocontínuadebancodedados”
[15]. Olivro“Entregacontínua”[6]tambémtemumcapítulodedicadoao
gerenciamentodedados.
8.6 O rquestração de deploy
Nossoprocessode deployébemsimples. Elesimplesmentereprovisionao
servidor webautomaticamentesemprequeumnovo commitpassarpelapi-
peline.Quantomaiscomponentesvocêpossuirnasuaarquitetura,maiorvai
seranecessidadedeorquestraraordemdo deploy.Nonossocaso,porexem-
plo,precisaríamosprovisionarobancodedadosantesdoservidorweb. Se
vocêtiverumclusterreplicadodobancodedados,vocêvaiquererfazero
deployemumadeterminadaordemparaevitaraperdadedadosediminuir
otempoemqueobancoficaindisponível.
Paraessassituações,érecomendadocriarum script(ouumconjunto
descripts)responsávelpordecidiraordememqueo deploydeveaconte-
cer. Ferramentascomoo Capistrano(http://capistranorb.com/),o Fabric
(http://fabfile.org/)ouatémesmoscriptsshellpodemserusadasparaessetipo
deorquestração. OutraalternativanomundoPuppetéusaro MCollective
(http://puppetlabs.com/mcollective),umprodutopagooferecidopelaPup-
petLabs.
Umatécnicaimportanteparareduziroriscodosseus deployséconhecida
como blue-green deployments–ouimplantaçõesazul-verde.Sechamarmos
oambientedeproduçãoatualde“azul”,atécnicaconsisteemintroduzirum
ambienteparalelo“verde”comanovaversãodosoftwaree,umavezquetudo
étestadoeestáprontoparacome çaraoperar,vocêsimplesmenteredireci-
onatodootráfegodeusuáriosdoambiente“azul”paraoambiente“verde”.
Emumambientedecomputaçãoemnuvem,assimqueforconfirmadoque
235

## Página 254

8.7. Gerenciandoconfiguraçõesporambiente CasadoCódigo
oambienteociosonãoémaisnecessário,écomumdescartá-lo,umaprática
conhecidacomoservidoresimutáveis.
8.7 Gerenciando configurações por ambiente
Écomumquesuapipelinedeentregapassepordiversosambientes,porexem-
plo:umambientedetestes,umambientedehomologa ção,umambientepré-
produçãoeoambientedeproduç ão. Umprincípioimportanteéquevocê
deveconstruirseusartefatosumavezeusá-losemtodolugar.Issosigni-
ficaquevocênãodevecolocarconfiguraçõesespecíficasdeumambienteno
artefatoprincipaldaaplicação.
UmexemplodessetipodeconfiguraçãoéaURLdaconexãocomobanco
dedados.Emcadaambientevocêteráumainstânciadiferentedobancode
dadosrodando,portantovocêprecisaconfiguraraaplicaç ãoparaapontar
paraobancodedadoscorreto.Existemalgumasabordagensdiferentespara
resolverestetipodeproblema:
•Sistemadecontroledeversões: estaéumaabordagemcomaqual
vocêcomitaumarquivodeconfiguraçãodiferenteparacadaambiente
nosistemadecontroledeversões.NomundoJava,écomumvocêcriar
arquivos .propertiesparacadaambiente.Suaaplicaçãoprecisaen-
tãosabercarregaroarquivocertoquandoestiverrodando.Adesvanta-
geméquetodasasconfiguraçõesficamdentrodoartefatodaaplica ção,
tornandodifícilalterá-lassemfazerumnovo deploy.
•Pacotesdeconfiguraç ãoporambiente: estaabordageméparecida
comaanterior,porém,emvezdeempacotarosarquivosdeconfigura-
çãonoartefatodaaplicação,vocêgerapacotesdeconfiguraçãodiferen-
tescomasconfiguraçõesespecíficasparacadaambiente.Issopermite
reconfigurarsemfazerumnovo deploydaaplicação.
•ConfiguraçãocomDNS:aoinvésdemudaraURLemcadaambiente,
vocêpodeusaramesmaURLemtodososambientes–porexemplo,
bd.app.com–eusarosistemaderesoluçãodeIPsdoDNSparare-
solveromesmonomede hostparaoIPcorretonaqueleambiente.Essa
236

## Página 255

CasadoCódigo Capítulo8. Tópicosavançados
abordagemsófuncionaparaconfiguraçõesdotipoURLenãofuncio-
nariaparaoutrostiposdeconfigurações.
•Provedorexternodeconfiguraç ões:emalgunscasos,vocêpodeque-
rercontrolaressetipodeconfiguraçãoemumlugarcentralizado.Um
conceitocomumnomundodeoperaçõeséumCMDB(Configuration
ManagementDataBaseoubancodedadosparagerenciamentodecon-
figurações),umrepositóriodetodososativosdeTIdasuaorganizaç ão
esuasrespectivasconfigurações. Existemalgumasformasdiferentes
deimplementaressaprática:noPuppet,o hiera(https://github.com/
puppetlabs/hiera)armazenaconfiguraçõesdeformahierárquica,per-
mitindosobrescrevervaloresporambienteedistribuí-loparacada host
emconjuntocomoPuppetmaster;noChefvocêpodecriar databags
paraarmazenarconfiguraçõesouimplementarumLWRP(LightWeight
ResourceProviderouprovedorderecursosleves)paraobterconfigura-
çõesdeumservidorcentralexterno.Outraformadeimplementaressa
práticaéutilizaroprópriosistemadecontroledeversõesesuashabi-
lidadesde branchingemerging,conformedescritoporPaulHammant
[11];algumasempresasacabamimplementandoumasoluçãocustomi-
zadapararesolveresseproblema.
•Variáveisdeambiente:umaabordagemusadanoHerokuquesetor-
noupopularquandoumdeseusengenheiros,AdamWiggins,publicou
oartigosobrea "twelve-factorapp”[18].Nessaabordagemtodaconfi-
guraçãoquevariaentreumambienteeoutroédefinidaemvariáveis
deambiente.Issogarantequenenhumaconfiguraçãoacabeacidental-
mentenorepositóriodecódigoeéumpadrãoagnósticodalinguagem
edosistemaoperacionalemqueaaplicaç ãovairodar.
Existemvantagensedesvantagensdecadaabordagementãovocêvaipre-
cisarconsiderarqualdelasfazmaissentidonoseuambiente.Porexemplo,o
Herokuexigequeconfiguraçõessejamfornecidasemvariáveisdeambiente,
entãovocênãotemoutraop ção. Casovocêestejacontrolandotodaasua
infraestruturacomoPuppet,aabordagemdeusarohierasetornamaisinte-
ressante.
237

## Página 256

8.8. Evoluçãoarquitetural CasadoCódigo
8.8 Evolução arquitetural
Aofinaldolivro,terminamoscomumambientecompostodequatroservi-
dores:osservidores webe dbsãopartedoambientedeproduçãoessenciais
paraqueusuáriosconsigamacessaralojavirtual.Osservidores monitore
cisãopartedanossainfraestruturadeentregaemonitoramento.Damesma
formaqueaprendemosemelhoramosnosso designdecódigodepoisqueo
códigoestáescritoeemuso,vamosaprendereterfeedbacksobrenossain-
fraestruturaumavezqueaaplicaçãoestáemprodução.
Conformevocêinvestenoseusistemademonitoramentoeobtémmétri-
cas,dadoseinformaçõessobrecomosuaaplicaç ãosecomportaemprodu-
ção,vocêteráfeedbackparamelhoraraarquiteturadasuainfraestrutura.Por
exemplo,afuncionalidadedebuscadanossalojavirtualéfornecidapeloSolr
enomomentoestamosrodandoumainstânciaembutidadoSolr,namesma
JVM.Conformeaquantidadedeprodutosindexadosaumenta,oSolrirácon-
sumirmaismemóriaeirácompetirporrecursoscomopróprioTomcat.No
piorcaso,umproblemanoSolrpodeafetaraaplicaç ãotoda.
UmaevoluçãodaarquiteturaseriamigraroSolrparaumservidorde-
dicado. Nessecaso,quandoalgumproblemaacontecer,aaplicaç ãoconti-
nuarodando. Vocêapenasforneceumadegrada çãodafuncionalidadede
busca. Dependendodaimportânciadessafuncionalidade,vocêpodeesco-
lhersimplesmentedesabilitá-laouusarumaimplementaçãoalternativaque
usaobancodedados.Todasessassãodecisõesválidasetornamasuaaplica-
çãomaisresilientedopontodevistadousuário.
Quandoestiverplanejandosuaarquiteturafísicaeacapacidadeesperada
parasuaaplicação,vocêdevelevaremcontadiversosfatores,geralmenteas-
sociadoscomrequisitosnão-funcionais:
•Frequênciademudanças: mantenhajuntooquemudanamesma
frequência.Esteprincípioseaplicatantono designdesoftwarequanto
naarquiteturadoseusistema.Sealgumcomponentetemmaisdeum
motivoparamudar,éumaindicaçãodequeeledeveserdividido.No
nossocaso,essafoiumadasmotivaçõesparasepararmososestágios
debuild,ospacoteseosrepositóriosdecódigodaaplicaç ãoedainfra-
estrutura.
238

## Página 257

CasadoCódigo Capítulo8. Tópicosavançados
•Pontosdefalha:éimportanteconhecerospontosdefalhadasuaar-
quitetura. Sevocênãoescolhê-losdeformapropositada,elesainda
existirão.Vocêsónãovaisaberondeequandoumafalhapodeaconte-
cer.NoexemplodoSolrembutido,sabemosqueumafalhanessecom-
ponentepodederrubaraaplicaçãointeira,portantoalgumasdecisões
arquiteturaisdevemserdefinidascomcenáriosdefalhaemmente.
•Unidadesde deployedependências:existeumprincípiodearquite-
turaquedizqueémelhorter“pequenaspeças,fracamenteacopladas”
doqueterumúnicomonólitoondetodasaspe çasestãoaltamenteaco-
pladas.Aopensarnasuaarquitetura,considerequaiscomponentesde-
vemserisoladosdorestoequaispodemirparaproduç ãodeforma
independentedoresto. Nonossocaso,estafoioutramotivaç ãopara
separaroservidor dbdoservidor web.
•Acordosdeníveldeservi ço(service-levelagreements ouSLAs): um
SLAéumamétricaquedefinecomoumserviçodeveoperardentro
delimitespredefinidos. Emalgunscasos,provedorescolocampena-
lizaçõesfinanceirasparadarmaispesoaoSLA.SLAsgeralmenteco-
bremcaracterísticascomodesempenhoedisponibilidade. Quandoa
suaaplicaçãoprovêumSLA,vocêvaiprecisartomardecisõesarquite-
turaisparatentargarantirquevocêconsegueatendê-lo.Porexemplo,
sevocêforneceumaAPIpúblicaqueprecisaestardisponível99.99%
porano–issosignificaqueelasópodeestarindisponívelnomáximo
52minutose33segundosporano–vocêpodeprecisaradicionarca-
madasparalimitaronúmeroderequisiçõesqueumclientepodefazer,
paraquenenhumclienteconsigamonopolizarseusrecursosouderru-
bemsuaAPI.JohnAllspawcobreesseassuntoembemmaisdetalhes
nolivro“TheArtofCapacityPlanning”[1].
•Escalabilidade: dependendodassuasexpectativassobreescalabili-
dade,vocêvaiprecisardecidirospontosdeextensãonasuaarquitetura.
Existemduasabordagenscomunsparalidarcomisso: escalabilidade
horizontalpermitequevocêadicionecapacidadecolocandomaisser-
vidoresalémdosquevocêjápossui; escalabilidadevertical permite
quevocêadicionecapacidadecolocandomaisrecursos–comoCPU,
239

## Página 258

8.8. Evoluçãoarquitetural CasadoCódigo
memória,disco,redeetc.–nosservidoresquevocêjápossui.Quando
vocêtemcomponentesseparados,vocêganhaapossibilidadedecon-
sideraressesrequisitosdeescalabilidadeemcadacomponente. Por
exemplo,vocêpodeescolherescalarseusservidoreswebhorizontal-
mente,enquantoseubancodedadosiráescalarverticalmente.
•Custos:ooutroladodamoedaaosepararmaisemaiscomponenteséa
questãodocusto.Emambientesdecomputaç ãoemnuvem,vocêpode
otimizarseuscustosconformevocêaprendemaissobrecomosuaapli-
caçãosecomportaemprodução.Noentanto,sevocêestáplanejando
comprarseuprópriohardware,nãoesque çadeconsideraroscustosde
cadaopçãoarquiteturalantesdetomarqualquerdecisão.
•Padrõesdeuso:sevocêsabequesuaaplicaç ãotempicosdeusoprevi-
síveis,oucaracterísticassazonaisbemconhecidas,épossívelotimizar
suainfraestruturaparareduzircustos.Istoéimportanteprincalmente
emumambientedecomputaçãoemnuvem,ondeéfácilaumentarou
diminuironúmerodeservidores. Nonossocaso,oservidordeinte-
graçãocontínuaprovavelmentenãoprecisaestardisponível24horas
pordia,7diasporsemana. Senossosdesenvolvedorestrabalhamno
mesmoescritório,ébemcapazqueoservidornãosejautilizadofora
dohoráriocomercialounosfinsdesemana.Estaéumavantagemde
migrarsuainfraestruturaparaanuvem,poisvocêpodesimplesmente
desligaroservidoreparardepagarduranteoperíodoocioso.
•Usoderecursos:porfim,outracaracterísticaquedeveserconsiderada
quandovocêdecidirasuaarquiteturaéopadrãodeusoderecursosde
cadacomponente.ServidoreswebgeralmenteprecisamusarmaisCPU
econcorrênciaparaatenderdiversasrequisiçõessimultâneas.Porou-
trolado,servidoresdebancodedadosgeralmenteusammaismemória
ediscoparaindexaçãoepersistência.Conheceressascaracterísticasde
cadacomponentedoseusistemaéimportanteparaaescolhadamelhor
arquitetura.
Nãoexisteumarespostacorretaparatodasassituações.Conformevocê
ganhamaisexperiência,vocêaprendeaidentificarquaiscaracterísticassão
240

## Página 259

CasadoCódigo Capítulo8. Tópicosavançados
maisimportantesparasuaaplicação. Oprincípiodamelhoriacontínuase
aplicaaqui,poiséumamaneiradeavaliarseassuasmudan çasarquiteturais
estãotrazendoosbenefíciosdesejados.
8.9 Segurança
Umassuntobastanteimportanteemváriosaspectosdasuaaplicaç ãoein-
fraestruturaéaseguran ça. Duranteolivro,nósescolhemossenhasfracase
àsvezesatéasdeixamosembrancoparasimplificaroexemplo.Noentanto,
essanuncaéamelhorop çãoemumambientedeproduç ão. Outroaspecto
importanteéquevocênãodevecompartilharsegredos–senhas,passphrases,
certificadosouchavesprimárias–entreosdiferentesambientes.Emalguns
casoséimportanteinclusivequevocênãocompartilheessessegredoscom
todososmembrosdaequipe.
Nuncacoloquesegredosemtextopuronorepositóriodecódigo.Como
regrageral,sempretentecriptografarinformaçõessensíveisparaque,mesmo
quandoalguémtenhaacessoàinforma ção,elenãosejacapazdeobterose-
gredo. Nessamesmalinhaderaciocínio,éimportantequevocênãoarma-
zeneinformaçõespessoaisdosseususuáriosemtextopuro. Nãodeixeque
segredosapareçamemtextopuronosseus logs.Nãocompartilhesenhaspor
e-mailouanoteemum post-itqueficadoladodoservidor.Seusistemaétão
seguroquantoseupontomaisfracoe,porincrívelquepare ça,opontofraco
égeralmentehumano.
Semprequeprecisamosgeraralgumtipodechave,percebaquefizemos
issodeformamanualparanãocolocarossegredosnocódigodeconfiguraç ão
dainfraestrutura.Existemalgumasalternativasparagerenciaressetipodein-
formaçãonasferramentasmaispopularesdeinfraestruturacomocódigo.No
Puppet,vocêpodeusarohiera-gpg(https://github.com/crayfishx/hiera-gpg)
ouopuppet-decrypt(https://github.com/maxlinc/puppet-decrypt).OChef
possuioconceitodeum databag criptografadoquepodearmazenarse-
gredosdeformaconfiável. EmJava,abiblioteca Jasypt(http://www.jasypt.
org/)provêumaformadecolocarconfiguraçõescriptografadasemarquivos
.propertiesparaqueelesnãosejamarmazenadosemtextopuro.
Outroprincípiointeressantequevaiajudá-loaencontrarproblemasno
241

## Página 260

8.10. Conclusão CasadoCódigo
seuprocessoautomatizadoétentarevitarlogaremumservidordeproduç ão
pararealizarqualquertipodeoperaç ão.BloquearoacessoSSHaoservidor
removeumimportantevetordeataque,umavezqueninguém(nemmesmo
você)serácapazdeexecutarcomandoslogandodiretamentenoservidor.
Éclaroqueoacessodiretoéapenasumdosvetoresdeataque. Ame-
lhorformadeabordarseguran çaésempreusarumesquemaemcamadas.
Coloqueproteçãoemcadaníveldoseusistema:noscomponentesderede,
nasuaaplicação,nospacotesdesoftwarequevocêescolher,noseusistema
operacionaletc.Tambéméimportantequevocêsemantenhainformadoso-
brevulnerabilidadesrecenteseestejapreparadoparaatualizarasversõesdo
seuscomponentessemprequeumproblemadeseguran çaforencontradoe
consertado.
Segurançaéumassuntocomplexoecheiodedetalhes,porissoéimpor-
tantevocêprocurarmaisrecursosespecializados. Paraaplicaçõesweb,um
bompontodereferênciaparaostiposdevulnerabilidadesmaiscomunse
formasdeprotegê-loséo OWASP(https://www.owasp.org). Todoano,o
OWASPpublicaumalistadosdezmaioresriscosdeseguran çaaosquaisa
suaaplicaçãopodeestarexposta. Elesmantêmatéumalistadeferramen-
tasdetestequeconseguemautomatizaraverificaç ãodealgunsproblemasde
segurançaquevocêpodeincorporarnasuapipelinedeentrega.
8.10 Conclusão
Umdosprincipaisobjetivosdesselivrofoiintroduzirtécnicaseconceitosde
DevOpseEntregaContínuanaprática. Poressemotivocome çamoscom
umaaplicaçãonãotrivialemproduç ãologonosegundocapítulo.Aprende-
moscomomonitorarerecebernotificaçõesquandoalgumproblemaéde-
tectadoemprodução.Tambémvimoscomotratarainfraestruturacomocó-
digo,oquenospossibilitourecriaroambientedeprodu çãodeformarápida
econfiável. Conseguimos,inclusive,migrarnossoambienteparaanuvem
semmuitadordecabe ça,reaproveitandoocódigoqueconstruímosaolongo
doscapítulos. Aprendemoscomomodelarnossoprocessodeentregaeim-
plementarumprocessoautomatizadode buildedeploycomdiferentestipos
detesteautomatizadosquenosdãoconfian çadeirparaproduçãomaisfre-
242

## Página 261

CasadoCódigo Capítulo8. Tópicosavançados
quentemente. Porfim,comumapipelinedeentrega,implementamosum
processodedeploycontínuoemquequalquer commitnocódigodaaplicação
oudeinfraestruturapodeirparaproduç ãoquandopassaportodosostestes.
Issoservecomoumabasesólidaquevocêpodeaplicarimediatamente
quandovoltaraotrabalhoamanhã. Comoexistemmuitomaiscoisaspara
aprendereacomunidadeDevOpscontinuaevoluindoecriandonovasferra-
mentas,nãodariaparaabordartudoemumlivrosó.Porisso,nestecapítulo
discutimosbrevementeoutrostópicosimportantesquevocêvaisedeparar
quandoembarcarnajornadadeentregacontínua.
Nossacomunidadeestácrescendoeointeressenoassuntoaumentaacada
dia.Nãoseassusteseasferramentasqueapresentamosaquievoluamouno-
vaspráticasapareçam,poiséassimquecriamosconhecimento.Oimportante
équevocêsaibaondeecomoprocurarporrecursosequevocêcompartilhe
seusaprendizadoscomacomunidade:escreva postsnoseublog,apresente
umestudodecasoemumaconferênciaouemseugrupodeusuários,com-
partilhesuasexperiênciasboaseruins,ajudeamelhorarnossasferramentas
contribuindocomcódigo,corrigindodefeitosoumelhorandosuadocumen-
tação,enviandoperguntasesugestõesnogrupodediscussãodolivroe,além
detudo,mantenha-seconectado!
243

## Página 263

CasadoCódigo ReferênciasBibliográficas
ReferênciasBibliográficas
[1] JohnAllspaw. TheArtofCapacityPlanning: ScallingWebResources.
O’ReillyMedia,2008.
[2] DavidJ.Anderson.Kanban:MudançaEvolucionáriadeSucessoparaseu
NegóciodeTecnologia.BlueHolePress,2011.
[3] MauricioAniche. Test-DrivenDevelopment: TesteeDesignnoMundo
Real.CasadoCódigo,2012.
[4] KentBeck.ProgramaçãoExtrema(XP)Explicada:AcolhaasMudan ças.
Bookman,2004.
[5] JamesBirchler. Imvu’sapproachtointegratingqualityassurancewith
continuousdeployment.2010.
[6] JezHumbleeDavidFarley. EntregaContínua:ComoEntregarSoftware
deFormaRápidaeConfiável.Bookman,2014.
[7] LisaCrispineJanetGregory. AgileTesting:APracticalGuideforTesters
andAgileTeams.Addison-WesleyProfessional,2008.
[8] TimothyGranceePeterM.Mell. Thenistdefinitionofcloudcomputing.
Technicalreport,2011.
[9] ScottAmblerePramodSadalage. RefactoringDatabases:Evolutionary
DatabaseDesign.Addison-WesleyProfessional,2006.
[10] MartinFowler.Refatoração:Aperfei çoandooProjetodeCódigoExistente.
Addison-WesleyProfessional,1999.
245

## Página 264

ReferênciasBibliográficas CasadoCódigo
[11] PaulHammant.Appconfigworkflowusingscm.2013.
[12] SteveMatyaseAndrewGloverPaulDuvall. ContinuousIntegration:Im-
provingSoftwareQualityandReducingRisk.Addison-WesleyProfessio-
nal,2007.
[13] DanielRomero.ComeçandocomoLinux:Comandos,Servi çoseAdmi-
nistração.CasadoCódigo,2013.
[14] RafaelSabbagh.Scrum:GestãoÁgilparaProjetosdeSucesso. Casado
Código,2013.
[15] PramodSadalage.RecipesforContinuousDatabaseIntegration:Evoluti-
onaryDatabaseDevelopment.Addison-WesleyProfessional,2007.
[16] DaniloSato. UsoeficazdemétricasemmétodosÁgeisdedesenvolvi-
mentodesoftware.Master’sthesis,2007.
[17] ThoughtWorks. ThoughtWorksAnthology: EssaysonSoftwareTechno-
logyandInnovation.PragmaticBookshelf,2008.
[18] AdamWiggins.Thetwelve-factorapp.2012.
[19] JohnWillis.Whatdevopsmeanstome.2010.
246