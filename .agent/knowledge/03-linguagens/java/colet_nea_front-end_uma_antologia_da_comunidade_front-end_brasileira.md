---json
{
  "id": "colet_nea_front-end_uma_antologia_da_comunidade_front-end_brasileira",
  "title": "Coletânea Front-end Uma antologia da comunidade front-end brasileira",
  "categoria": "03-linguagens",
  "subcategoria": "java",
  "resumo": "**Arquivo Original:** `Coletânea Front-end Uma antologia da comunidade front-end brasileira.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "antologia",
    "brasileira",
    "colet",
    "comunidade",
    "end",
    "front",
    "front-end",
    "java"
  ],
  "perguntas_tipo": [
    "Como utilizar Coletânea Front-end Uma antologia da comunidade front-end brasileira?",
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

# Coletânea Front-end Uma antologia da comunidade front-end brasileira

> **Arquivo Original:** `Coletânea Front-end Uma antologia da comunidade front-end brasileira.pdf`
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

CasadoCódigo Sumário
Sumário
1 Umacoletâneacomomelhordacomunidadefront-endbrasileira 1
1.1 Oscapítuloseosautores .......................... 2
2 ProgressiveEnhancement:construindoumsitemelhorparatodos? 5
2.1 Porondecome çar?.............................. 9
2.2 ProgressiveEnhancementeHTML .................... 1 1
2.3 ProgressiveEnhancementeCSS ...................... 1 3
2.4 ProgressiveEnhancementeJavaScript .................. 1 7
2.5 QuandooProgressiveEnhancementnãoéumaalternativa ...... 2 2
3 Responsive,AdaptiveeFaultTolerance 25
3.1 Responsiveéquebrado ........................... 2 5
3.2 AdaptiveDeliveryéquebrado .......................2 6
3.3 Oquerealmenteimporta:ProgressiveEnhancementeoFaultTole-
rance......................................3 0
3.4 Esque çaosnomesResponsiveeAdaptive ................ 3 2
4 Tudoquevocêprecisasaberparacriarumframeworkdesucesso 35
4.1 Guerracontraosframeworksprontos .................. 3 8
4.2 Organiza çãoepadroniza ção ........................ 3 9
4.3 Nomenclatura ................................ 4 1
4.4 Regrasdeestado ............................... 4 3
4.5 Modulariza ção:Pensandoemseuprojetocomoumsanduíche . . . . 47
4.6 Agrupandoseuscomponentesemumúnicolocal ........... 5 2
4.7 Tornando-seoreidospadrões ....................... 5 5
i

## Página 6

Sumário CasadoCódigo
5 TornandoawebmaisdinâmicacomAngularJS 57
5.1 PorqueAngularJS .............................. 5 7
5.2 AngularJS ................................... 5 8
5.3 Móduloseinje çãodedependências .................... 6 5
5.4 ServiceAngularJS ..............................6 9
5.5 Comunicandocomservidorback-end .................. 7 1
5.6 $routeAngularJs ............................... 7 3
5.7 Conclusão ................................... 7 7
6 AsdiretrizesdeacessibilidadeparaconteúdonaWeb–WCAG 81
6.1 AcessibilidadenaWeb ............................ 8 1
6.2 PortrásdoWCAG2.0 ........................... 8 2
6.3 Princípio1:perceptível ...........................8 4
6.4 Princípio2:operável............................. 9 2
6.5 Princípio3:compreensível .........................9 6
6.6 Princípio4:robusto .............................9 8
6.7 Conclusão ...................................9 9
7 AplicaçõeswebsuperacessíveiscomWAI-ARIA 101
7.1 Leitoresdetela ................................1 0 2
7.2 Roles ......................................1 0 3
7.3 Formuláriosacessíveis............................1 0 6
7.4 RoleDocumentStructure ..........................1 1 0
7.5 Landmarks ..................................1 1 0
7.6 Conclusão ...................................1 1 2
8 APIsgeniaisdaWebmoderna 115
8.1 WebStorage(localStorageesessionStorage) ...............1 1 5
8.2 postMessage .................................1 2 1
8.3 WebNotifications ..............................1 2 6
8.4 HistoryAPI ..................................1 2 8
8.5 Conclusão ...................................1 3 2
ii

## Página 7

CasadoCódigo Sumário
9 AsAPIsdeacessoadispositivosdoHTML5 135
9.1 DispositivosesuasAPIs . . . . . . . . . . . . . . . . . . . . . . . . . . 136
9.2 Comoonavegadoracessaosdispositivos. . . . . . . . . . . . . . . . . 138
9.3 Câmeraemicrofone. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
9.4 Geolocalização . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
9.5 Acelerômetroegiroscópio . . . . . . . . . . . . . . . . . . . . . . . . . 155
9.6 Bateria. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .160
9.7 Vibração . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163
9.8 Iluminaçãoambiente . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164
9.9 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167
10 DebugandosuaWebApp—ou,Comoseestressarmenos 169
10.1 Console . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171
10.2 Utilizandobreakpoints . . . . . . . . . . . . . . . . . . . . . . . . . . . 175
10.3 Emulandodispositivosmóveis. . . . . . . . . . . . . . . . . . . . . . . 186
10.4 Debugremoto . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 192
10.5 Dicasetruques. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 197
10.6 Extensões . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .202
10.7 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .207
11 TestandocódigosJavaScript 211
11.1 Introdução . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 211
11.2 Osbenefíciosdetestarumaaplicação . . . . . . . . . . . . . . . . . . . 212
11.3 Escrevendoostestesunitários. . . . . . . . . . . . . . . . . . . . . . . 214
11.4 Nomundoreal. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227
11.5 Concluindo. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232
iii

## Página 9

Capítulo1
Umacoletâneacomomelhorda
comunidadefront-endbrasileira
Acomunidadebrasileiradeprogramadoresfront-endeWebDesignerséfantástica.
Possuiumafor çaimensadeelevaraqualidadedaWebbrasileira. Osmilharesde
representantesdessacomunidadeproduzemconteúdosótimosemseusblogs,listas
dediscussão,Facebookeconversasdeboteco. Nósnosencontramosemeventos
memoráveisemtodooBrasil.Fazemosadiferen ça.
Esselivroquerserumapequenacelebra çãodessesucesso.
Inspiradosemprojetosinternacionaissemelhantes–comoorecomendadíssimo
SmashingBook –trazemosessaColetâneadeFront-end . Umgrupode11autores
derenomenacionalnacomunidadesejuntouparaescreverartigosquejulgamos
relevantesparaaWeb.
Emaisimportanteatéqueopequenogrupodedesbravadoresdesseprojeto,que-
remosabrirocaminhoparamaisumcanaldacomunidadefront-end.Queremosfe-
edback,queremosquebriguemconoscopraquelancemosnovasedi ções,commais

## Página 10

1.1. Oscapítuloseosautores CasadoCódigo
autoresemaistemas.
1.1 Os capítulos e os autores
Olivroestáorganizadoemcapítulosindependentes,cadaumcomseuautor.Con-
versamosentrenós,mascadatópicoéexpressãodoprópriocriador.
Aúnicaregraera:escreveralgomemorável,quefizesseadiferen çanaWebbra-
sileira.Nessenossomeioquemudarápido,nãoqueríamosfalardamodadomês.
Focamosemtemasatuaismasduradouros.
ComeçamostentandorediscutiropapeldaWebredescobrindoo Progressive
EnhancementcomLuiz Real. Éimpressionantecomoumatécnicacomanosde
idadeécadavezmaisatual. Ecomohámuitagenteaindaignorandoessaprática
essencial.
Nasequência,DiegoEis abordaResponsive,AdaptiveeFaultTolerance com
muitasbuzzwordsepolêmicas.OautormostracomoaWebégenialmenteimprevi-
sível,adaptativaeflexívelediscuteo mindsetcorretopralidarcomisso.
Entraentão BernardDeLuna falandosobreComocriarframeworksCSS .Mais
queumaabordagempuramentetécnica,éumtratadosobreanecessidadedepadrões
nosprojetoseumadiscussãointeressantesobreopapeldosframeworksnasequipes
W e b .
Emseguidatemos GiovanniKeppelen,queapresentaumaintrodu çãodetalhada
aoAngularJS,umdosprincipaisexpoentesatuaisdogrupodeframeworksJavaS-
criptMVC.EledemonstracódigospráticosdosprincipaismódulosdoAngulareos
motivospelosquaisvocêdeveconsideraressaferramentaemsuasaplica ções.
Adiscussãosobreacessibilidadeébastanteprofundacomdoisnomesdepeso.
Primeiro,ReinaldoFerrazdiscuteocora çãodaacessibilidadevistapeloW3C,mos-
trandoaspráticasfundamentaisdas WCAGquemuitasvezesaindasãoignoradas
nomercado.
Depois,DeividMarquesexpandeotemaabordando WAI-ARIAeasnovasmar-
caçõesdeacessibilidadepensandoemintera çõesricasnaWeb.Comexemplosexce-
lentes,elemostracomoosnovosatributospodemserincorporadossemesfor çonas
suasaplica ções.
ComaWebevoluindoapassoslargosebrowserscadavezmaisespertos,oque
nãofaltamsãonovasAPIsparaexplorartodoessepotencial. JaydsonGomesmostra
váriasAPIsmodernas quevocêjápodeusarhoje,comoWebStorage,PostMessage,
WebNotificationseHistory.
2

## Página 11

CasadoCódigo Capítulo1. Umacoletâneacomomelhordacomunidadefront-endbrasileira
Comootemaélongo, AlmirFilhomostraaindamaisAPIs,agoracomfocoem
acessoa recursosdedispositivosmodernos . Abordaaspectossobrecâmera,ace-
lerômetro,aúdio,GPS,vibra çãoemais. Éoquevocêprecisasaberpradominara
Webemsuasnovasfronteiras.
Nasequência,CaioGondim mostracomodominartodoessemundodofront-
endefacilitarodesenvolvimentocom DebugnobrowsereDevTools .Éumcapí-
tulobastanteaprofundadoemcomoincorporarousodasferramentasdedesenvol-
vimentonoseudiaadiacombastanteprodutividadeerecursosúteis.
Noúltimocapítulo,EduardoShiotafalade testescomJavaScript.Umassunto
devitalimportânciaparagarantiraqualidadedequalquerprojetoqueenvolvafront-
end.
E,porfim,eu, SérgioLopes,idealizadordacoletânea,escreviesseprefácioefizo
papeldeeditor,revisortécnico,cobradordeprazosedistribuidordepitacosnotexto
alheio.
Emnomedetodososautores,esperoquegostedostemasqueescolhemose
aproveiteolivro.VamosmudaraWebjuntos!
Sobre o editor
SérgioLopeséinstrutoredesenvolvedornaCaelum,ondedáaulasde
front-endeoutrascoisas.Escrevebastanteconteúdosobrefrontemseu
blog(sergiolopes.org),twitter(@sergio_caelum)eoutroslugares.Parti-
cipademuitoseventosnoBrasiltodoepublicouolivro "AWebMobile”
tambémpelaeditoraCasadoCódigo.
3

## Página 13

Capítulo2
ProgressiveEnhancement:
construindoumsitemelhorpara
todos?
Comnavegadorescadavezmaismodernos,cheiosderecursos,atendênciaéque
nossossitestambémfiquemcadavezmaissofisticados. Porém,nãopodemoses-
quecer:nemtodomundoqueacessanossossitesestáusandoumnavegadorcomos
últimosrecursos.
Oprimeiropensamentoqueaparecenacabe çademuitosquandoouvemalgo
parecidoé:maseupossoobrigarmeususuáriosaatualizaremseusnavegadores.Ou
então:usuáriocomnavegadordesatualizadonãomereceacessarmeusite!Masserá
quesemprepodemosexigirnavegadoresatualizadosdosnossosusuários?Eseráque
navegadoresdesatualizadossãooúnicoproblema?
Quandofazemosumsite,normalmenteofazemosparaumpúblicoimensode
pessoas.Nãopodemosesquecerque,nessepúblicoimenso,temospessoasquenão

## Página 14

CasadoCódigo
gostamdeJavaScriptsendoexecutadoemsuasmáquinas,pessoasque nãopodem
atualizarseusnavegadores,pessoasacessandoainternetapartirdedispositivosli-
mitadosepessoascomdificuldadesmotoras,visuaiseauditivasquenemsempre
conseguemutilizaromouseparanavegaroudependemdeleitoresdetelaparate-
remacessoaonossoconteúdo.Maisainda:temosumtipodeusuáriomuitoimpor-
tanteparaconsiderar,quenãotemJavaScriptnemCSShabilitados:asferramentas
debusca.
Issosignifica,então,quenãopodemosfazerumsitemodernoeacessívelao
mesmotempo?Seriaabsurdoseatecnologiaevoluíssedessaforma.Éporissoqueos
gruposquecontrolamodesenvolvimentodastecnologiasqueusamosnainternet,
comooW3C,têmsempreemmenteapreocupa çãocomessescasoscitados. Mas
comopodemosdesenvolversiteslevandoemcontaessescenários?
Gracefuldegradation
Umaprimeiraformadepensarédesenvolverseusiteprimeiroparaopúblico
geral,quetemacessoaosnavegadoresmaismodernosenãotemrestri çõesdeaces-
sibilidadepara,emumsegundomomento,procuraratenderaosusuárioscommais
limitações.Essaformadepensarestápresentehámuitosanosnodesenvolvimento
desistemaseaideiadecriarsistemastolerantesafalhas;nomundodedesenvolvi-
mentofront-end,essapráticaficoumaisconhecidacomo gracefuldegradation.
Noentanto,pensardessaformapodenoslevaraalgunsproblemas.Vamospe-
garumexemploparaanalisar: umbotãodecompraremumalojavirtual. Você
implementouacomprausandoAJAX,paradarmaisdinamicidadeànavega çãodo
usuário.Assim,noseuHTML,vocêprovavelmentetem:
<input type="hidden" name="produto" value="123456">
<input type="number" name="quantidade">
<a href="#" id="comprar"><img src="icone-comprar.png"></a>
E,noseuJavaScript(usandojQuery,paraencurtarumpouco):
$("#comprar").click(function() {
var dadosCompra = {
produto: $("[name=produto]").val(),
quantidade: $("[name=quantidade]").val()
};
// enviamos os dados no formato JSON para o
6

## Página 15

CasadoCódigo Capítulo2. ProgressiveEnhancement:construindoumsitemelhorparatodos?
// servidor.
// atualizaPagina é uma função que vai ser
// executada depois que o servidor confirmar
// a compra.
$.post("/compra", dadosCompra, atualizaPagina, "json");
});
Issoresolvenossoproblemaparaamaiorpartedosusuários. Agoraparamos
parapensar: aquaiscasosnãoatendemos? Umaprimeirapossibilidadeépensar
naacessibilidadedapágina: seráqueusuárioscomdeficiênciavisualconseguirão
comprarnanossaloja?Dificilmente.Afinal,nossobotãodecompraréumaimagem!
Oleitordetelanãovaiconseguirlerotexto“comprar”apartirdela.Alémdisso,esse
botão,porserumlink,podegerarconfusãonessesusuários.Podemosmelhoraresta
situaçãocomumHTMLmaissemântico:
<form>
<input type="hidden" name="produto" value="123456">
<input type="number" name="quantidade">
<button type="submit" id="comprar">
<img src="icone-comprar.png" alt="Comprar">
</button>
</form>
Reparenousodatag formparaindicarqueestescontroles,juntos,representam
informaçõesqueserãoenviadasparaumservidor. Temostambématag button
comotipo submitdeclarado,paraindicarqueessaimageméumbotãoeque,ao
serclicado,enviaráoformulário.
Agora,ficamaisfácildeumleitordeteladescreveroqueessepeda çodatelafaz,
enemprecisamosalterarnossoJavaScript! Masseráqueháalgumoutrocasoque
precisamostratar?Sim,usuáriossemJavaScript:comoestáaexperiênciaatualpara
eles?Elesconseguemcomprarnonossosite?Oqueacontecequandoelesclicamno
botãodecompra?Absolutamentenada!
Repareque,tendoapreocupa çãocom gracefuldegradation,precisamoslembrar
detodososcenáriosquedeixamosdeladoaodesenvolvernossositecomasúltimas
tecnologias.E,seprecisamoslembrardessescenários,qualachancedeesquecermos
algum? Maisainda: agoraprecisamosimplementarumasolu çãosemJavaScript.
Seráqueépossível?NossoservidornosdevolveumJSONcomoresultado,nãouma
página.Paramostraralgoútilparaousuário, precisamosdeJavaScript,agora.Ou
seja,portermosdesenvolvidoumasolu çãosempensarnoscasosmaislimitados,
7

## Página 16

CasadoCódigo
acabamoscaindoemumbecosemsaída.Precisaremos refazerboapartedanossa
solução,inclusivedoladodoservidor.
Comofazer,então,paranãocorrermosoriscodeesquecermosessescenários
maislimitados? Começandoporeles ;essaéaideiado progressive enhancement.
ProgressiveEnhancement
Paraentenderadiferen çaentreosdois,vamosusaromesmocenário:precisa-
mosimplementarobotãoparacomprarumprodutoemumalojavirtual. Porém,
vamoscome çarporumcenáriobemlimitado:umnavegadorbaseadoemtexto(o
navegadorLynx,porexemplo, http://lynx.browser.org/).Nessetipodenavegador,
aúnicaferramentaquetemosdisponíveléoHTML.Comoimplementarumbotão
decomprausandoapenasHTML?Comalgopróximodoquejátínhamos:
<form action="/comprar" id="comprar">
<input type="hidden" name="produto" value="123456">
<input type="number" name="quantidade">
<button type="submit">Comprar</button>
</form>
Repareemumadiferen çaimportante:oatributo actionnoformulário.Com
ele,onavegadorsabeparaqualendere çonoservidorosdadosdesteformuláriode-
vemserenviados;nãoprecisamosdeJavaScriptnenhumparaensinarissoparao
navegador. Repare,também,emumaoutradiferen ça: colocamosotexto“Com-
prar”dentrodobotãoemvezdaimagem. Atépoderíamosdeixaraimagemmas,
porserumaquestãoestética,podemosdeixarparaumsegundomomento,quando
estivermospensandonoCSSdessapágina.Porfim,valeobservarqueessadecisão
decome çarpelocenáriomaislimitadoinfluenciatambémoladoservidordaaplica-
ção:aocomprar,vamosenviarnossosdadosnoformatopadrãodonavegadorenão
noformatoJSON.
Agorapodemospassarparaumcenárioumpoucomaiscomplexo:usuárioscom
deficiênciavisual.Comeles,jápodemosusarJavaScript.Paraimplementaracompra
comAJAX,comoqueríamosinicialmente,nãoteremosquasenenhumcódigoagora:
$("#comprar").submit(function() {
$.post(this.action, $( this).serialize());
});
Vejaque,agora,nãoprecisamosmaisnospreocuparcomosdadosdoformulário
individualmentenemcomaURIdacompra.Porestarmosusandoumformulário
8

## Página 17

CasadoCódigo Capítulo2. ProgressiveEnhancement:construindoumsitemelhorparatodos?
semântico,podemossimplesmentepedirparaojQuerypegarosdadosdesseformu-
lárioeenviá-locomoonavegadorfaria,porémdeformaassíncrona.
Nessemesmocenário,tambémpoderíamoscome çarapensarnodesigndapá-
gina,usandoelementosgrandese/oucombomcontraste.E,aotestaressecenário
comumleitordetela,provavelmentelembraremosdecolocarmarca çõesdaespeci-
ficaçãoWAI-ARIA,paramelhorarausabilidadedapágina.
Quando começamos por um cenário mais limitado, é natural querermos
solucioná-loadequadamente. Issonosforçaapensaredesenvolverdeumaforma
quefavoreceumHTMLmaissemânticoedesacopladodeCSSeJavaScript.Ganha-
mosnãoapenasumsitequefuncionabemparatodos;ganhamostambémumcódigo
maislimpoefácildemanter .
Noentanto,aplicaro progressiveenhancementnãoétãofácilcomopodeparecerà
primeiravista.Diversasquestõesaparecem:qualvaisermeucenáriomaislimitado?
Por onde começar?Comoacrescentarfuncionalidadesemquebraroqueeujátinha?
Naspróximasse ções,vamosanalisaressasquestõesecomoelasseaplicamacada
umadastecnologiasqueusamosparadesenvolvernossaspáginas.
2.1 Por onde começar?
Quandocome çamosapensarseguindoalinhado progressiveenhancement,vemos
queeleinfluenciaosmaisdiversosaspectosdonossoprojeto.
Porexemplo,seformosdesenvolverumsiteparadivulgarumproduto,podemos
pensar,antesdemaisnada: qualonossopúblico-alvo? Seráqueprecisamosnos
preocuparcomnavegadoresantigos?Qualparceladevisitantesdomeusiteviráde
dispositivosmóveis?Quãoimportanteéaintegra çãocomredessociais?Oqueposso
oferecerparameusvisitantescomconfigura çõesmaislimitadas?
Reparequeessasquestõessãomuitomaisrelacionadasaoseunegóciodoquea
questõestécnicas.Saberrespondê-lasémuitoimportanteparaaplicarmososcon-
ceitosde progressiveenhancementcorretamente,desdeocome çodoprojeto.
Umavezquesetenhaclaroopúblico-alvo,normalmentecome çamduasfrentes
detrabalho:odesenvolvimentodalógicadosite( back-end)eoprojetodainterface.
Nodesenvolvimentodo back-end,saberqualopúblico-alvovaiinfluenciaremquais
funcionalidadesserãoimplementadasecomo.Nodesenvolvimentodainterface,o
paradigmado progressiveenhancementinfluenciaráofluxodessedesenvolvimento,
comoveremosmaisadiante.
Ouseja,o progressiveenhancement nãoéapenasumaformadedesenvolvero
9

## Página 18

2.1. Porondecomeçar? CasadoCódigo
códigodo front-end:éumaformadiferentedepensarodesenvolvimentodopro-
dutocomoumtodo .Sendoassim,umapossívelrespostaparaapergunta“poronde
começar?”é:peloplanejamentodoseuproduto.Umavezquesetenhambemcla-
rososobjetivosdoproduto,asdecisõestécnicas(quaisnavegadoressuportar,quais
tecnologiasusaretc.)tornam-sesimples.
Infelizmente,issodificilmenteaconteceemumcenárioreal. Normalmentete-
mosquelidarcomumpúblico-alvopoucoconhecido,dificuldadesnahoradetomar
decisõesdeprodutomaistécnicasjuntoaoclienteelimita çõesnoor çamentoeno
prazodeentrega.Aindaassim,épossívelaplicaro progressiveenhancement.Senão
sabemosqualocenáriomaislimitadoaquevamosatender,podemoscome çarpelo
maislimitado.Senãotemosor çamentoe/ouprazosuficientesparadesenvolverto-
dasasfuncionalidadesdesejadas,podemosentregarasqueatendemaoscenários
maislimitadosprimeiro.Seoclientenãosabequaistecnologiasosvisitantesdosite
vãousarparaacessaroconteúdo,come çamoscomomínimopossíveldetecnologias.
Entregando com qualidade
Emtodoprojeto,temostrêsvariáveispossíveisdeseremcontrola-
das:or çamento,prazoequalidade.Noentanto,éimpossívelcontrolaras
trêsaomesmotempo:sefixamosprazoequalidade,oprodutosaimais
caro;sefixamosprazoeor çamento,aqualidadediminui;sefixamosor-
çamentoequalidade,odesenvolvimentodemorarámais.
Contudo,sacrificaraqualidadenormalmentenãoéumaboaalter-
nativa. Sendoassim,seoprazonãoésuficienteparaentregartodasas
funcionalidades,nãoentreguenadamalfeito;entregueoqueforpossí-
vel.E,sevocêestiverseguindoo progressiveenhancement,asfunciona-
lidadesquevocêentregarsãoaquelasqueinfluenciamoscenáriosmais
limitados,ouseja,omaiornúmerodeusuáriospossível.
Reparequeatenderaocenáriomaislimitadoprimeironãosignificanecessari-
amente começaradesenvolverpelosnavegadoresmaisantigos(InternetExplorer
6,estouolhandoparavocê)ouparanavegadoresbaseadosemtexto. Novamente,
éumadecisãoquecabeaoclientedoprojeto . Opapelquecabeanós,desenvol-
vedores,éinformaroclientedasconsequênciasdeincluirouexcluirdeterminadas
tecnologiasdoprojeto.
Valelembrar,também,que,cadavezmais,podemosfazermaiscommenos.
10

## Página 19

CasadoCódigo Capítulo2. ProgressiveEnhancement:construindoumsitemelhorparatodos?
Osnavegadoresvêmoferecendoferramentascadavezmaisavan çadasparanós,de
formaquenãodependemosmaisdetecnologiascomoFlashouJavapararesolvera
maiorpartedosproblemas.Alémdisso,oCSSeoHTMLvêmganhandorecursos
quenoslivramdanecessidadedeusarJavaScriptemdiversoscasos. Umexemplo
clássicoéaimplementaçãodenavega çãoemabas:antigamente,essetipodesolu ção
precisavadeJavaScriptparaserimplementada;hojeemdia,épossívelimplementá-la
apenascomCSSeHTML,tornando-adisponívelparaumpúblicoaindamaior.
2.2 Progressive Enhancement e HTML
Sequeremoscome çardocenáriomaisrestrito,precisamospensaremquaistecno-
logiaspodemosusarnessecenário.Háváriaspossibilidadesmas,semdúvida,todas
elastêmsuporteaoHTML.
OHTMLéabasedetodapáginaInternete,portanto,todousuáriodonossosite,
sejahumanooumáquina,temqueentenderpelomenosHTML;semprepodemos
contarcomele.
Noentanto,precisamoslembrarqueoHTMLpassoupordiversasmodifica ções
desdequefoicriado,ouseja,temosváriasversõesdeHTML.Qualdelasvamossu-
portar?Éaíqueahistóriacome çaacomplicar.
Atualmente,todososnavegadores,emsuaúltimaversão,trabalhamcomaver-
são5doHTML.Porém,oqueissosignifica? Quandodizemos HTML5,naver-
dade,estamosfalandodeumasériedenovasfuncionalidadesagregadasàlinguagem
HTML:novastags,novosatributos,novoscontrolesdeformulário,novasAPIs,além
demodifica çõesdesintaxeesemântica.Sãomuitosnovosrecursos,demodoqueos
navegadores,emsuamaiorparte, aindanãoimplementamtodaaespecifica çãodo
HTML5.
Ora,entãonãopodemosusaroHTML5? Felizmente,aespecifica çãodalin-
guagemHTMLjáfoifeitapensandoem progressiveenhancement. Paraentender
oporquê,vamosanalisaroqueacontecequandoumnavegadoranalisaoseguinte
HTML:
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Teste de HTML5 </title>
</head>
11

## Página 20

2.2. ProgressiveEnhancementeHTML CasadoCódigo
<body>
<header>
<h1>Página com HTML5 </h1>
<span>Bacana, né? </span>
</header>
<section>
<h1>Hora atual </h1>
<time>22:39</time>
<p>Um controle de form novo: </p>
<input type="range" min="1" max="10">
</section>
</body>
</html>
Seonavegadorjáimplementasuporteatodoessecódigo,nãohámuitosegredo:
logonocome çodocódigo,estamosusandoadeclara ção DOCTYPEparaindicar
queestamosusandoa últimaversãodoHTML ,ouseja,onavegadordevemostrar
todooseupotencial!Assim,temoscomoresultadoumapáginaexatamentecomo
esperávamos:umcabeçalhocomotítulodapáginaeumase çãodetextocomotítulo
dela,umahora,umparágrafoeumcontroledotipo slider.
Eseonavegadornãoimplementasuporteatodosessesrecursos,oqueacontece?
Jánaversão4,aespecifica çãodoHTMLrecomendaque[1]:
• Seumagentedeusuárioencontrarumelementoquenãoreconhece,eledeve
tentarrenderizarseuconteúdo;
• Seumagentedeusuárioencontrarumatributoquenãoreconhece,eledeve
ignoraradeclara çãocompletadesteatributo,istoé,oatributoeseuvalor;
• Seumagentedeusuárioencontrarumvalordeatributoquenãoreconhece,
eledeveusarovalorpadrãoparaaqueleatributo.
Reparequearecomenda çãoébemfavorávelàaplica çãodo progressiveenhan-
cement:mesmoqueonavegadornãoentendaexatamenteoqueestamosquerendo
dizer,elevaimostraroconteúdoparaousuário; podemosincrementarasemântica
eainteratividadedonossoHTMLsemquebrarosnavegadoresmaislimitados!
Noexemplodadoanteriormente,seonavegadornãosuportaatag <time>eo
inputdotipo range,aindaassimousuárioveráahoraeumcontroledeformulário
(umacaixadetexto,queéocontroledeformuláriopadrão).
12

## Página 21

CasadoCódigo Capítulo2. ProgressiveEnhancement:construindoumsitemelhorparatodos?
Porém,porserapenas umarecomenda ção,nemtodososnavegadoresseguem
essasdiretrizese/ouseguem-nasdemodos bemdiferentes.Emparticular,ousode
tagsdoHTML5noInternetExplorernasversõesanterioresà9trazproblemasde
estilizaçãoeinterpreta çãodaestruturadapágina[2]. Aversão5daespecifica ção
ébemmaisclaraquantoaotratamentodeerros,oquedevemelhoraravidado
desenvolvedorfront-endemumfuturonãomuitodistante.
Suportando HTML5 em versões mais antigas do Inter -
net Explorer
ParacontornarosproblemasdecorrentesdousodetagsdoHTML
5 nas versões mais antigas do Internet Explorer, foi criada uma pe-
quenabibliotecaescritaemJavaScriptcapazdehabilitarumsuportemí-
nimoàsnovastags:ohtml5shiv( https://code.google.com/p/html5shiv/)
. Elaresolveosproblemasdeestiliza çãoeinterpreta çãodaestrutura
da página mas não adiciona funcionalidade ao navegador. Ou seja,
se você quer fazer com que o Internet Explorer suporte o<input
type="datetime">,porexemplo,essabiblioteca nãoresolveopro-
blema.Veremosmaisadianteumapossívelresolu çãoparaessecaso.
Alémdisso,valenotarque,porserumasolu çãobaseadaemJavaS-
cript,elanãoatende100%dosusuáriosdosite:aquelesquedesabilitaram
aexecu çãodeJavaScriptverãoapáginacomosproblemasdeestiliza ção
originais.
2.3 Progressive Enhancement e CSS
Umavezquetenhamosabase–oHTML–deumapáginabemdefinida,podemos
começaraimplementarodesigncomCSS.Valeobservarqueoprocessodedesign,
porsisó,tambémpodeseguiro progressiveenhancement,masnossofocoaquivai
sernasimplica çõesdo progressiveenhancementnousodoCSS.
AssimcomooHTML,oCSSéumatecnologiajáantigaequepassouporuma
grandeevolu ção,culminandonoquechamamosagorade CSS3. E,assimcomo
nocasodoHTML,osnavegadoresnãoimplementamsuporteatodasasnovidades,
mesmoporqueelascontinuamvindo(grids,formas,regiõesparacitaralgunsexem-
plos),masosnavegadoresignoramaspropriedadesdesconhecidas,demodoque
13

## Página 22

2.3. ProgressiveEnhancementeCSS CasadoCódigo
tambémémuitofácilirincrementandonossovisualdeacordocomasfuncionali-
dadesdisponíveis!
Alémdisso,oCSStemumaoutracaracterísticapeculiarquefacilitao progressive
enhancement:quandoumapropriedadeapareceduplicada,apenasaúltimadeclara-
çãoéconsiderada.Paraentenderporqueissonosajuda,vamosconsideraroseguinte
exemplo:umafotocomalegendasobrepostaaela.
UmaformadedescreveressecenáriosemanticamentecomHTMLé:
<figure>
<img src="..." alt="Ancoradouro em Belize" >
<figcaption>Passe as férias no Caribe! </figcaption>
</figure>
Paraposicionaralegendaemcimadafoto,podemosdarà <figure>umpo-
sicionamentorelativoe,àlegenda,umposicionamentoabsoluto:
figure {
position: relative;
}
figcaption {
position: absolute;
bottom: 0 ;
}
Comisso,bastadefiniracordefundo.Notequeacoréumpretotranslúcido.
Atérecentemente,nãohaviaumaformadefazeressacordefundoapenascomCSS,
eranecessáriocriarumaimagemcomessacoreusá-ladefundo,oquenãoémuito
14

## Página 23

CasadoCódigo Capítulo2. ProgressiveEnhancement:construindoumsitemelhorparatodos?
flexívelnemperformático.Então,paraosnavegadoresmaislimitados,vamosusar
umacoropacamesmo:
figcaption {
background-color: black;
color: white;
}
Umavezimplementadoolayoutparacenáriosmaislimitados,podemosirem-
belezandonossapáginacomasnovidadesdoCSS3.Nonossocaso,agorapodemos
colocaracortranslúcidadefundo.Porém,sesubstituirmosanossadeclara çãoatual,
quebraremosnossotrabalhoanterioredeixaremosumtextobrancodiretamenteem
cimadeumafoto,oquenãoénadausável.Entãovamosaproveitarocomportamento
doCSSdesobrescreverdeclara çõesanterioresparasuportartantonavegadoresmais
antigoscomomaisnovos:
figcaption {
background-color: black;
background-color: rgba(0, 0, 0, 0.8 );
color: white;
}
Os navegadores mais antigos só entenderão a primeira declaração de
background-color;osmaisnovosentenderãoasduaseusarãoapenasaúltima.
Vejacomoessecomportamentonospermitefazer progressiveenhancement deum
jeitofácil:bastairacrescentandoasfuncionalidadesmaisrecentes abaixodasmais
antigas!
IndoalémcomCSS
Quandopensamosem progressiveenhancement,devemospensaremdarame-
lhorexperiênciapossívelparaoscenárioslimitados.Issoimplicaemtiraromaior
proveitopossíveldasferramentasquetemosnessescenários.
Amaiorpartedossitesquevamosdesenvolvernonossodiaadiaprecisaráde
CSSparaservisualmenteagradáveleatrairmaisusuários.Ouseja,mesmonoscená-
riosmaislimitados,jáestaremosdependentesdeCSS.Jáqueéassim,entãopodemos
explorá-loomáximopossível!
Muitosrequisitosde front-endquenormalmenteimplementamoscomJavaS-
criptpodemserfeitosapenascomCSS,ouseja,semdependerde mais umatec-
nologia.
15

## Página 24

2.3. ProgressiveEnhancementeCSS CasadoCódigo
Umexemploclássicoderequisitodestetipoéanavega çãoemabas.Umapossível
representaçãoparaabasnoHTMLé:
<ul class="abas">
<li class="aba" id="aba-1">
<a href="#aba-1">Sobre</a>
<section class="conteudo">
...
</section>
</li>
<li class="aba" id="aba-2">
<a href="#aba-2">Descrição</a>
<section class="conteudo">
...
</section>
</li>
<li class="aba" id="aba-3">
<a href="#aba-3">Fotos</a>
<section class="conteudo">
...
</section>
</li>
</ul>
CombasenesseHTML,podemoscriarabasusandoapseudoclasse :targete
algunstruquesdeposicionamento:
.abas {
position: relative;
}
.aba {
display: inline;
}
.aba > a {
float: left;
padding: 0.5em 1em ;
background: linear-gradient(#FFF, #EEE );
border-width: 1px ;
border-style: solid;
border-color: #CCC #CCC #FFF ;
}
.aba:not(:target) a {
16

## Página 25

CasadoCódigo Capítulo2. ProgressiveEnhancement:construindoumsitemelhorparatodos?
border-bottom: 0 none;
}
.aba:target a {
background: white;
}
.conteudo {
position: absolute;
left: 0 ;
top: calc(2em + 4px ); /* altura do link + bordas */
z-index: -2 ;
border: 1px solid #CCC;
background-color: white;
}
.aba:target .conteudo {
z-index: -1 ;
}
Essaeoutrasimplementa çõesvocêpodeconferircommaisdetalhesem http:
//css-tricks.com/examples/CSSTabs.
Valenotarque,àsvezes,passamosadependerdefuncionalidadesdoCSSque
excluemmaisusuáriosdoqueadependênciadeJavaScript.Nestaimplementa ção,
porexemplo,estamosexcluindotodasasversõesdoInternetExploreranterioresà
9. Énecessário,portanto,analisarqualimplementa çãoatendemaisusuárioscom
menosrecursos.
2.4 Progressive Enhancement e Ja v aScript
Desenvolverpensandoprimeironoscenáriosmaislimitadosjáevitaquecaiamosno
tipodearmadilhamostradanaintrodu çãodestecapítulo,comoformulárioAJAX.
Noentanto,quandoadicionamosJavaScriptàpágina,precisamostomarcertoscui-
dadosparanãoquebrarotrabalhojáfeito,assimcomonoCSS.
DamesmaformaquedevemospensarnoCSScomoalgo amaisemumapágina,
devemostambémpensarnoJavaScriptdessaforma. Issosignificaque,namedida
dopossível,ocódigoJavaScript nãodeveinterferir noseuHTML.Porexemplo,em
vezdefazerumlinkvirarumaa çãoemJavaScriptcom
<a href="#" onclick="maisProdutos()">Mais produtos </a>
devemospreservaroHTMLoriginal
17

## Página 26

2.4. ProgressiveEnhancementeJavaScript CasadoCódigo
<a href="mais-produtos.html">Mais produtos </a>
eadicionarafuncionalidadeJavaScriptusandoopróprioJavaScript,emalgo
como
document.querySelector(’[href="mais-produtos.html"]’)
.addEventListener(’click’, maisProdutos);
Dessaforma,nossositecontinuafuncionandoperfeitamente,mesmoqueoJa-
vaScriptapresentealgumproblema,e essaéumadasprincipaisvantagensdo pro-
gressive enhancementparaoseudesenvolvimento .Essetipodepensamentoéco-
nhecidoentreosdesenvolvedoresJavaScriptcomo JavaScriptnão-obstrutivo.
Éfatoque,emmuitoscasos,algumasfuncionalidadessóestarãopresentespara
usuárioscomJavaScripthabilitado.Porexemplo:imaginequequeremosfazeruma
caixadebuscaparafiltrarumalistaderesultados,comonafiguraaseguir. Como
podemosdesenvolveralgodestetipopensandoem progressiveenhancement?
Arespostaparaessaperguntasempreé começandopelocenáriomaislimitado.
EoquepodemosoferecerparanossosusuáriossócomHTML,porexemplo?Uma
simpleslista:
18

## Página 27

CasadoCódigo Capítulo2. ProgressiveEnhancement:construindoumsitemelhorparatodos?
<h1>Sobremesas</h1>
<ul class="resultados">
<li><a href="receita?id=123">Bolo de nozes </a></li>
<li><a href="receita?id=234">Estrogonofe de nozes </a></li>
<li><a href="receita?id=345">Bolo de chocolate </a></li>
<li><a href="receita?id=456">Torta de chocolate </a></li>
<li><a href="receita?id=567">Torta de maçã </a></li>
</ul>
Depoisde incrementarapáginacomoestilo,passamosàfuncionalidadeda
busca.E,paraimplementá-la,podemosfacilmentepensarem mudarnossoHTML
paraalgodotipo:
<h1>Sobremesas</h1>
<input type="search" onkeyup="filtra()">
<ul class="resultados">
<li><a href="receita?id=123">Bolo de nozes </a></li>
<li><a href="receita?id=234">Estrogonofe de nozes </a></li>
<li><a href="receita?id=345">Bolo de chocolate </a></li>
<li><a href="receita?id=456">Torta de chocolate </a></li>
<li><a href="receita?id=567">Torta de maçã </a></li>
</ul>
Porém,aofazermosisso,sempercebermos,estamosoferecendoumapágina
“quebrada”paraosusuáriossemJavaScript. Afinal,paraqueserveestacaixade
buscaparaeles? Nada;portanto,elasimplesmente nãodeveriaestarlá.Mascomo
fazemosparaelaaparecersóparaosusuáriosquetêmJavaScriptfuncionando?
Inserindo-aviaJavaScript!
var busca = document.createElement(’input’);
busca.type = ’search’;
var resultados = document.querySelector(’.resultados’);
resultados.parentNode.insertBefore(busca, resultados);
SevocêestiverusandojQuery,dáparafazerissoem umalinha:
$(’<input type="search">’ ).insertBefore(’.resultados’);
Simples,não?E,dequebra,ganhamosumaorganiza çãodecódigomelhor:oque
érelacionadoaJavaScript ficanoJavaScript.AssimnãopoluímosnossoHTML.
19

## Página 28

2.4. ProgressiveEnhancementeJavaScript CasadoCódigo
Ouseja,quandotemosapreocupa çãodo progressiveenhancementnaimplemen-
taçãodasfuncionalidadesquedependemdeJavaScript,umaboapráticaéusar ape-
nasJavaScriptparaacrescentá-lasaosite.Comisso,asseguramosquenãoquebrare-
mosotrabalhoanteriore,dequebra,deixamosnossocódigomaisorganizado.
LidandocomJavaScriptlimitado
Umpontoquenãogeradoresdecabe çanoHTMLenoCSSmasque,noJa-
vaScript,ébastantecomplicadoélidarcomfuncionalidadesfaltantes. Vimosque,
comrela çãoaoHTML,onavegadormostrainforma çõesdetagsdesconhecidase,
comrela çãoaoCSS,onavegadorignorapropriedadesevaloresnãosuportados;o
mesmonãoacontececomoJavaScript:qualquercomandoquenãosejasuportado
pelonavegadorgeraráum errodeJavaScript ,consequentementeparandotodaa
execuçãodocódigo.
Lidar com as limitações e diferenças entre os navegadores pode ser bas-
tante trabalhoso. Por exemplo, para selecionar elementos da página, podemos
usar a função document.querySelector, como fizemos no exemplo ante-
rior. Noentanto,essafun çãonãoestápresenteemtodososnavegadores. Para
que nosso código funcione em todos os navegadores, podemos usar a função
document.getElementsByClassName:
var resultados = document.getElementsByClassName(’resultados’)[0];
Nestecaso,ocódigoficouapenasumpoucomaiscomplicadodoqueantes.Mas
seráqueparaopróximoexemploseriasimplesoferecerumaalternativa?
var linksExternos = document.querySelectorAll(’a[href^=http]’);
Felizmente,temosatualmentenomercadodiversasbibliotecasquecuidamdes-
sasdiferen çaselimita çõesparanós,taiscomojQuery,Prototype,MooToolseDojo.
Deummodogeral,essasbibliotecasnospermitemescrevercódigoJavaScriptsem
precisarmosnospreocupartantocomoscenáriosmaislimitados.Valeapenausá-
las,principalmentesevocêprecisadarsuporteanavegadoresmaisantigos.
Apesardeabstrairemproblemasdecompatibilidadeentreosnavegadores,essas
bibliotecasnãonoslivramdelidarcomumoutroproblema:presen çaouausência
defuncionalidadesentrenavegadores.
Imagine,porexemplo,quevocêestáconstruindoumsitedeumaredederes-
taurantesequermostrarparaumusuáriosospratosexclusivosdesuaregiãoem
20

## Página 29

CasadoCódigo Capítulo2. ProgressiveEnhancement:construindoumsitemelhorparatodos?
destaque. Paraisso,vocêpodeperguntaremqualcidadeousuárioestáou,mais
interessante,tentardetectarondeeleestá.IssoépossívelpormeiodaAPIdegeolo-
calizaçãodosnavegadores:
navigator.geolocation.getCurrentPosition(function(position) {
// descobre a cidade baseado nas coordenadas
});
Porém,nemtodonavegadortemsuporteaessaAPIe,quandonãohásuporte,o
objeto geolocationnãoestádefinidoe,portanto,ocódigoanteriorgeraumerro.
Umaprimeirasolu çãoseriaverificaronavegadordousuárioparahabilitarou
nãoestetrechodecódigo.Porém,comaquantidadedenavegadoresquetemosatu-
almente,ésimplesdizerquaissuportamgeolocaliza ção?
Umaoutraabordagem,maissimpleserobusta,éverificarseonavegadordo
usuáriotemafuncionalidadedesejada ,independentedequalseja. Nestenosso
caso,ésimplesfazerisso: bastaverificarseoobjeto geolocationestádefinido
antesdeusá-lo.
if (navigator.geolocation) {
navigator.geolocation.getCurrentPosition(function(position) {
// descobre a cidade baseado nas coordenadas
});
}
Noscasosemqueadetec çãodafuncionalidadeémaiscomplicada,podemos
usarabiblioteca Modernizr(http://modernizr.com/),cujopropósitoéjustamente
detectarasfuncionalidadesdisponíveisnonavegador.
Programandodestaforma,podemosgarantirquefuncionalidadesmaisavan ça-
dasnãoquebrarãonossocódigo,permitindoo progressiveenhancementdoladodo
JavaScript.
Emalgunscasos,aindaépossívelestenderafuncionalidadepadrãodonavega-
dorcomousodebibliotecasescritasemJavaScriptqueemulamalgunsrecursos.
Podemos,porexemplo,proverumaimplementa çãodoobjeto geolocationpara
osnavegadoresquenãoopossuem(abiblioteca WebshimsLibfazisso,porexemplo
–https://github.com/aFarkas/webshim).Bibliotecascomessepropósito–acrescen-
tarumafuncionalidadeanavegadoresqueaindanãoasuportam–sãoconhecidas
como polyfills.
Valeobservarqueos polyfillsnãosópermitemousoderecursosavan çadosdo
JavaScriptemnavegadoresmaissimples,comotambémderecursosmaismodernos
21

## Página 30

2.5. QuandooProgressiveEnhancementnãoéumaalternativa CasadoCódigo
deHTMLeCSS.Existem polyfillsparaoscontrolesdeformuláriodotipo datee
paraapropriedade box-sizing,porexemplo.
Assim,dependendodeseupúblicoalvo, polyfillspodemserumaalternativain-
teressanteparamelhoraraexperiênciadosusuárioscommaislimita ções.Maséim-
portantelembrarque polyfillsapenasemulamafuncionalidadeoriginale,portanto,
têmlimitaçõese,pordependeremdeJavaScript(e,emalgunscasos,deoutrastec-
nologias,comoFlash),nãoagregamafuncionalidadedesejadaatodososusuários.
Novamente,desenvolverseusitepensandoem progressiveenhancementéessencial
paraquetodososusuáriostenhamacessoàsinforma çõescontidasnele.
2.5 Quando o Progressive Enhancement não é uma
alternativ a
Aabordagemdo progressiveenhancementresolvemuitosproblemasdodesenvolve-
dorfront-endaofor çarofocoprimeironapartemaisimportantedeumsite,queé
proveroconteúdo. Noentanto,progressiveenhancementtemsuasdesvantagense
nemsempreéaplicável.
Quandodesenvolvemospensandoprimeironoscenáriosmaislimitados,conse-
guimosplanejarnossodesenvolvimentodemodoatornarnossositeminimamente
acessívelnessescenários.Noentanto,issopodeserrestritivoparaoprocessocriativo
dedesenvolvimentodeumsite.Imagine,porexemplo,quevocêprecisafazeruma
páginamostrandoasfuncionalidadesdeumaparelhocelularnovo.Ojeitomaissim-
plesequeatendeatodososusuáriosésimplesmentemontarumalistadessasfunci-
onalidades,possivelmentecomimagensilustrativas.Porém,pensandodessaforma,
vocêpodeacabardeixandodeapresentá-lasdeumaformamaiscriativa,comoum
menuinterativo.Paranãocorreresserisco,valeapenapensarprimeiroemcomo
queremosquenossositefiquenofinalpara,daí,come çaraimplementarpeloce-
náriomaislimitado.Essaideiadeprojetofinal,inclusive,podeservirdeguiapara
soluçõesmaiscriativasmesmonessesprimeiroscenários.
Agora,emprojetosemqueháumadependênciamuitograndederecursosmo-
dernosdosnavegadores,comonumjogoouumsitequetrabalhacomawebcam
dousuário,o progressiveenhancement acabanãotrazendovantagense,poroutro
lado,podedificultarodesenvolvimento. Nessassitua ções,épossíveldesenvolver
umaversãomaissimples,semasfuncionalidadesprincipais,paraoscenáriosmais
limitados,usando progressiveenhancement. Essaabordageméseguida,porexem-
plo,peloGmail,oservi çodee-maildaGoogle. Aversãoprincipaldoclienteweb
22

## Página 31

CasadoCódigo Capítulo2. ProgressiveEnhancement:construindoumsitemelhorparatodos?
édesenvolvidausandorecursosavan çadosdeJavaScript.Parasimplificarodesen-
volvimentodessaversãoeaindapermitiroacessoaose-mailsnosnavegadoresmais
limitados,foidesenvolvidaumaversãobaseadaapenasemHTML.
Há,ainda,casosemqueo progressiveenhancementnãotrazmuitasvantagens.
Emumsitefeitoparaumaintranet,porexemplo,temoscontroletotaldequalseráo
navegadordousuárioequaisfuncionalidadeseletem.Quandotemosessecontrole,
acabanãosendointeressantefazer progressiveenhancement. Porém,aindaassim,
preocupar-secomaacessibilidadedapáginaedesenvolveroCSSeoJavaScriptde
formaincremental,usandooHTMLcomobase,trazvantagensenãodeixadeser
importante.
Mesmonoscenáriosemque progressiveenhancementnãoéaplicável,éinteres-
santeteremmenteaspreocupa çõesdessaformadedesenvolvimento.Desenvolver
paraawebédesenvolverparatodos,independentedeplataforma,navegador,língua
ecapacidades,eessaéaprincipalpreocupa çãodo progressiveenhancement:fazerda
webumasó,paratodos,comoidealizouocriadordaweb,TimBernes-Lee[3].
[1] http://www.w3.org/TR/html401/appendix/notes.html#notes-invalid-docs
[2] http://diveintohtml5.info/semantics.html#unknown-elements [3] http:
//news.bbc.co.uk/2/hi/technology/6983375.stm
Sobre o autor
LuizébacharelemestreemCiênciadaComputa çãoetrabalhacomo
desenvolvedoreinstrutornaCaelumatualmente.Adoraprogramarpara
fazersistemasnãosóúteis,comobonitospordentroeporfora,depre-
ferênciausandoaWebcomoplataforma.Porissomesmo,amaHTML,
CSSeJavaScript.ColaboracomprojetosdecódigoabertocomoVRap-
tor,MedSquareeTubaina,etambémescreveparaoblogVidaGeek.net.
23

## Página 33

Capítulo3
Responsive,AdaptiveeFault
Tolerance
3.1 Responsive é quebrado
Eunãoqueroferirosentimentodeninguém. Euseiqueo ResponsiveWebDesign
(RWD)écoisalinda,contudo,porfavor,nãootratecomoo SantoGraal.ORWD
nãoéasolu çãoparatodososproblemas.OResponsiveéumaboasolu çãoparcial
deumproblemamuitomaiordoqueapenasadequarwebsitesparadiversastelas.
Suposições
Tudooquevocêsabesobreousuárionãopassadesuposi ções.Trabalharcom
Webédifícilporcausadisso.Vocênuncatemcertezasobrecomoseuusuáriopode
acessarseusite.Vocêtemumasuposi ção,umaligeiraideiadequeelepodeacessar
seusitecomumdeterminadobrowser,emumdeterminadosistema,emumdeter-
minadodispositivo.Vocênuncasabenadacomcertezaabsoluta.

## Página 34

3.2. AdaptiveDeliveryéquebrado CasadoCódigo
Vocêpodefalarqueumagrandemaioriadosseususuáriosacessaositeusando
umadeterminadaresolu ção.Masquandovasculhamososdados,essesnúmerossão
fragmentadoseédifícildescobrirpelaquantidadededispositivosebrowsersque
elesusam.VocêpodedescobrirqueamaioriadosseususuáriosusamIE,mastam-
bémqueháumagrandeparcelaqueusaSafariparaMobile.Étudomuitosensível,
entende?
Estruturassim,módulosdepois
OResponsivepodeadequarwebsitesparaváriostiposdetamanhodetela,mas
essaadequa çãosóchegaatéaestruturadosite.Vocêpodefalarqueositeterá3,2ou1
colunaemaisnada.AsMediaQueriesajudamaresolvernossoproblemaestrutural.
Essaparteésuperimportante,masnãoésuficiente.Háaindaoutrograndeproblema
queenvolvecadamódulodosite. Umelementousadonodesktoppodenãosero
idealnoscelulares.
EntendaquenãosoucontraoRWD,peloamordeDeus...Euoamodepaixão.
Masqueroquevocêpensefriamentequeele,sozinho,nãoresolvetodososseuspro-
blemas. Éaíqueumconceitobemmaiorentraemcena,chamado Adaptive Web
Design,queabrangeumasériedesolu çõesparaadaptarseuwebsite/produtoadi-
versoscenáriosecontexto,ondeoRWDéapenasumape çadoquebracabe ças.Você
precisaconsiderarmuitascoisasalémdelayoutsflexíveisparaqueseuwebsiteseja
defatoacessadoporqualquerum.
Existemcenáriosquenãoforambemexploradosequeaindavãonosatormentar
pormuitotempo,comoéocasodosnavegadoresemconsoles. Podeserquevocê
descubraqueseususuários,poralgummotivoqualquer,estejamacessandoseuweb-
siteviaXbox,Playstationetc.Aideiadeadaptarwebsitesparaconsoleséalgopouco
explorado.Paracome çar,vocênãotemmouse,nemteclado.Vocêtemumjoystick
quenãofoipreparadoparaessatarefa.
Muitosformatosestãosurgindodetodososcantoseissoéalgorealmenteper-
turbador. Smartwatchsserãoapróximaondaemuitoprovavelmenteosusuários
sentirãoanecessidadedeacessarinforma çõesemwebsitesusandoumdispositivo
assim.Eaí?
3.2 AdaptiveDelivery é quebrado
Jávouavisandoqueessecampotambémébemdesconhecido.Ninguémtemasres-
postascorretaseninguémsabeexatamenteoquefazeratéagora.Asolu çãocorreta
26

## Página 35

CasadoCódigo Capítulo3. Responsive,AdaptiveeFaultTolerance
éaquelaquefuncionounoseuprojeto.
OAdaptiveDeliverytambéméumapeçadoquebra-cabe ça,comooRWD.Elese
resumeem:enviarpartesdowebsiteouowebsiteinteiroadaptadoparaocontexto
queousuárioseencontra.Sevocêestáusandomobile,vouservirpartesdocódigo
queseadegueaomobile.SeforTV,vouservirpartesdositequefacilitamousoem
umatelagrandeeassimpordiante.
Comovocêfazisso? Depende. Temgentequeusasolu ções back-end,identifi-
candoviaosheadersqualplataforma/contextoousuárioestáeaípedeparaoser-
vidorparaenviardeterminadopeda çodecódigo. Temgentequeresolvetudono
front-end,comJavaScript.Qualdosdoisestáerrado?Depende.
Àsvezes,umasimplestrocadeclassedeumelementojáofazmudartotalmente,
resolvendosuaestruturaparadiversosdispositivos.Àsvezes,vocêprecisadescons-
truirtodooelemento,guardandoseconteúdo,paraconstruiroHTMLdealgodife-
rente.
Oexemplodastabs
Costumousarumexemplobembásicoparavocêentenderabrincadeira.Astabs
(ouguias,comovocêpreferir)sãobemusadasemsistemasewebsites.Oproblema
comastabséqueelassãobemusadasemDesktopsenãonosmobiles.Quandouma
tabquebradelinha,perde-setotalmenteaanalogiainicial.
Emumatelamenor,comoficaria:
27

## Página 36

3.2. AdaptiveDeliveryéquebrado CasadoCódigo
Muito,muito,muitoruim.
Omaislegalseriaquenomobileesseelementovirasseumdropdown. Ouso
seriamaisintuitivo,economizaríamosespa çoemanteríamosdecenteaexperiência
dousuário:
Essaéumasolu çãobásicaevocêpodenemgostardela.Nãoháproblemanisso.
Opontoéquevocêentendeuoconceito:formasdiferentesdeentregaroconteúdo
28

## Página 37

CasadoCódigo Capítulo3. Responsive,AdaptiveeFaultTolerance
dependendododispositivo.
Existemoutrosexemplosextremosde AdaptiveDelivery,nosquaisnãomuda-
mosapenasumapartedocódigo,masositeinteiro,comoéocasodaLufthansa.
Aliás,essesitedaLufthansaéumcaseclássicode AdaptiveDelivery,emqueentre-
gamosocódigoexatodeacordocomocontextodousuário.Existemvárioswebsites
queexplicamessecase.DêumapesquisadanoGooglesobreositedeles.
Existemdoisconceitosquevocêjádevetercansadodeouvireestudar: Fault
ToleranceeProgressiveEnhancement,assuntoinclusivedoprimeirocapítulodolivro.
Osdoisservemcomobaseparaproduzirwebsitesqueseadequamdeverdadea
qualquertipodedispositivo,nãoimportaqualatelaouqualplataforma.
Sevocêlevarasérioessesdoisconceitos,vocêconseguiráfazerwebsitescompa-
tíveiscomqualquerbrowsereprincipalmentecomqualquercontextoqueousuários
seencontrar.
29

## Página 38

3.3. Oquerealmenteimporta:ProgressiveEnhancementeoFaultTolerance CasadoCódigo
3.3 O que realmente importa :P rogressive Enhance-
ment e o Fa u l tTolerance
FaultToleranceécomoasmáquinastratamumerroquandoeleacontece.Éahabi-
lidadedosistemadecontinuaremopera çãoquandoumafalhainesperadaocorre.
Issoaconteceatodomomentocomseucérebro.Osistemanãopodepararatéque
esseerrosejaresolvido,logo,eledáumjeitoparaqueesseerronãoafetetodooresto.
Anaturezainteiratrabalhadessaforma.Osbrowserstrabalhamdessaforma.Épor
issoquevocêconseguetestarascoisasmaravilhosasdoCSS3edoHTML5semse
preocuparcombrowsersantigos.
JátemosasvantagensdoFaultTolerancedesdeoinício
Porexemplo,quandoescrevemosumapropriedadedeCSSqueobrowsernão
reconhece,elesimplesmenteignoraaquelalinhaepassaparaapróxima.Issoacon-
teceotempointeiroquandoaplicamosasnovidadesdoHTML.Lembra-sequando
osbrowsersnãoreconheciamosnovostiposdecamposdeformuláriosdoHTML5?
Obrowsersimplesmentesubstituíaocampodesconhecidopelocampocomumde
texto.
Issoéimportanteporqueoquesefazhojenodesenvolvimentodeumwebsite,
continuaráfuncionandodealgumaformadaqui10anos. Comoosbrowserstêm
essatolerânciaafalhas,linguagenscomoHTMLeCSSganhampoderparaevoluir
otempointeiro,semosbloqueiosdaslimita çõesdopassado.
Entenderaimportânciado FaultToleranceéachaveparaentendero Progres-
siveEnhancement.Naverdade,o ProgressiveEnhancementnãoseriapossívelseessa
tolerânciadefalhasnãoexistisseembrowserseoutrosmeiosdeacesso.
Tudosobreacessibilidade
Fundamentalmente,ProgressiveEnhancement étudosobreacessibilidade. Na
verdade,otermoacessibilidadeénormalmenteusadoparaindicarqueoconteúdo
deveseracessívelparapessoascomnecessidadesespeciais.OProgressiveEnhance-
menttrataissomasnaóticadequetodomundotemnecessidadesespeciaise,por
isso,oacessoaoconteúdodeveriaserfacilitadoparaqualquerpessoaemqualquer
tipodecontexto.Issoincluifacilmentepessoasqueacessamwebsitesviasmartpho-
nes,porexemplo,cujatelaépequenaealgumasdasfacilidadesqueexistemnodesk-
topsestãoausentes.
30

## Página 39

CasadoCódigo Capítulo3. Responsive,AdaptiveeFaultTolerance
NíveisdeTolerância
Nóspassamosporalgunsníveisaodesenvolveralgotendocomométodoo Pro-
gressiveEnhacement.Essesníveistêmcomoobjetivosempreservir,primeiro,ocon-
teúdoe,depois,todasasfuncionalidadesecomportamentosquepossammelhorar
oconsumodesteconteúdoetambémdetodaapágina.
Oobjetivoportrásdatolerânciadeerroséadesempremanterumfallback
quandoalgoruimacontecer. Aprimeiracamadageralmenteéumsimplesfeed-
backbásico,queserácompatívelcomamaioriadosdispositivos.Essefeedbackge-
ralmenteéservirumconteúdoemformadetexto. Issoéóbviopoisotextoéum
conteúdoacessívelparapraticamentequalquermeiodeacessoexistentehoje.Mui-
tosdoselementosdoHTMLtêmumfallbackdetextoparacasosemqueelemento
nãosejacarregadoounãosejareconhecido.Lembradoatributo alt?Atémesmo
nastagsdevídeoeaudio,comoaseguir:
1 <video src="video.ogg" controls>
2 Texto de fallback.
3 </video>
AsegundacamadaéasemânticadoHTML.CadaelementodoHTMLtemsua
funçãoe,principalmente,seusignificado.Elesacrescentamsignificadosaqualquer
informaçãoexibidapeloHTMLe,muitasvezes,estendemosignificadoqueotexto
sozinhonãoconseguiria.
Aterceiracamadadeexperiênciaéacamadavisual,ondevêmoCSSetambém
asimagens,audiosevídeos.Éondeacoisaficabonitaeinterativa.Aqui,vocêsente
maisatolerânciadosbrowsersafalhas.Usamosotempointeiropropriedadesque
nosajudarãoamelhoraraimplementa çãodelayouts,masque,embrowsersantigos,
podemnãoserrenderizados.Experimentamosissoatodomomento.
Aquartacamadaéacamadadeinteratividadeoucomportamento.OJavaScript
tomacontadessapartecontrolandooselementosdoHTML,muitasvezescontro-
landopropriedadesdoCSSpararealizara çõesdeacordocomasintera çõesdousuá-
rio.
AcamadafinaléumaextensãodasemânticadoselementosdoHTML.Aíéonde
inserimosasiniciativasdeWAI-ARIA.Éondevamosguiarleitoresdetelaseoutros
meiosdeacessoparaelementosepontosimportantesnaestruturaqueolayoutse
baseia.Indicandoquaisregiõeseelementossãoreferênciadenavega ção.Parasaber
maissobreWAI-ARIA,vejaocapítulo6.
Nóspodemosresumirascamadasem3:
31

## Página 40

3.4. EsqueçaosnomesResponsiveeAdaptive CasadoCódigo
• Camadadeconteúdo:HTMLsemânticoericocomWAI-ARIAetagscorretas;
• Camadadeformatação:CSSeestilos;
• Camadadecomportamento:JavaScript.
Estassãoastrêscamadasclássicassobreasquaisvocêjáouviudurantesuavida
profissionalinteira.Nãohásegredo.Nãohánadanovo.
Costumodizerparameusalunosquesemprequealgonodesenvolvimentoweb
—principalmentequandosetratacomHTML/CSS—estáficandocomplicado,é
porqueháalgoestáerrado.OHTMLfoifeitosimplesevaicontinuarsimples.Não
hámotivoparacomplicarmosalgoquejáésimples(estouolhandoparavocê,dev
back-end,queinsisteemusarhaml).
FaultTolerancedeveserlevadoemcontaemtodososseusprojetosWeb.Pensar
assimdáflexibilidadeparaoprojetoavan çarparaqualquercaminho,semmedode
problemas,poisessesproblemaspodemsergerenciadoseprincipalmentesolucio-
nadosdeformaeficaz.
Fazerwebsitescompatíveiscomtodososdispositivosdouniverso,comtodosos
sistemasdebusca,leitoresdetelaequalqueroutracoisaqueumdiautilizaremosé
tudosobrevoltaràsraízesdodesenvolvimentoWeb.Ésersimplesdesdeoinício.É
tratardepoucascoisasporvez.
3.4 Esqueça os nomes Responsive eAdaptive
Agoraesque çatudooquefaleiaquiefoqueemapenasumacoisa: vocênãofaz
websitesparadispositivos,vocêfazwebsitesparaosusuários.Seuobjetivoéqueos
usuáriosconsigamacessarainforma çãosemnenhumarestri çãotécnica.Issoquer
dizerqueelepodequereracessarseusitedeumrelógiooudeumaTV,nãoimporta,
elevaiacessar,depreferênciasemtantasmudan çasestruturaisparaevitarnovos
aprendizados.
Sinceramentenãoimportaqualtecnologiaoumetodologiautilizadapelaequipe.
Oqueimportaéumusuáriofalandobemdoseuprodutopoiseleconseguiuencon-
traroquequeria. Porqueelechegou,fezocheckoutsemproblemasenãosentiu
faltadeinforma çõesentreasversões.Oimportanteéaubiquidadedainforma çãoe
asatisfa çãofinaldousuário.
Isso é Web.
32

## Página 41

CasadoCódigo Capítulo3. Responsive,AdaptiveeFaultTolerance
Sobre o autor
DiegoEisfundouoTableless.com.br,websitebrasileiroqueproduz
conteúdosobreboaspráticasenovastecnologiasdedesenvolvimento
webfront-end. TreinouequipesdeempresascomoWhirpool,Oi,Ac-
centure,Itaú,Nokiaeoutros.Agoraestápartindoparasuasegundaem-
presa.
33

## Página 43

Capítulo4
Tudoquevocêprecisasaberpara
criarumframeworkdesucesso
“Nãoépossívelobterumacriaçãocoletivaapartirdasomadecria çõesindividuais.
Um a c r i açãoésempreresultadodeumprocessoconjuntodecria ção.”
–HorácioSoaresNeto
Todoprojetotemumaorigem,umanecessidadeeumproblemapararesolver.
Quandocriamosumproduto/servi ço,queremosresolverumproblemaparaalguém,
ousomosousadosapontodecriarumnovoproblemaparaalguém.Comodesen-
volvedores,nóspodemoscriaruma checklistdeproblemaspredefinidosquetemos
aoiniciarumprojeto,afinaltodoprojetoqueseprezedeveriaserpreparadopara
seracessível,semântico,performático,testávelesustentável. Háalgunsanos,um
grandeproblemacome çouaganharumpoucomaisdepopularidade: areutiliza-
çãodetrechosdecódigo.SejaHTML,CSSouJavaScript,essestrechos,conhecidos
comomódulos,funcionamcomope çasde LEGOque,somadasestrategicamente,
criamprojetosflexíveis,padronizadoseorganizados.

## Página 44

CasadoCódigo
Porqueétãodifícilcriarumpadrão?
Oserhumanotemumaenormefacilidadenoreconhecimentodepadrões,pois
éoqueusamosparavivereéassimquefuncionamos.
Nossocérebroéformadodeduasáreasresponsáveispeloarmazenamentoda
memória.Aprimeiradelaséresponsávelpelamemóriadecurtadura çãooumemó-
riadetrabalho;easegundaéamemóriadelongadura ção.Comoamemóriacurta
possuiumacapacidadelimitada,existeumacamadaanteriorconhecidacomo ar-
mazenamentosensorial,responsávelpelatriagemdoqueseráarmazenadoounão.
Paraisso,elaprecisadefiniremsegundosoquevaiarmazenarnamemóriadecurta
duraçãoeoqueelavaiesquecer.Oquenãoforarmazenadopelosistemadegeren-
ciamentodememóriaéignorado,gerandoumreaprendizadootempotodosobre
aquiloquenãofoiguardado.
Écomoseessaprimeiracamadadaentradadeinforma çãofosseumcachedo
browser,poisacadavezquevocêfecharobrowseroureiniciaroseucomputador,ela
éautomaticamentelimpa.Claroqueseasuaidaaomesmositeforconstante,você
automaticamenteteráositenapáginainicialdoseubrowser,emumaespéciede
memóriadecurtadura ção,ouocolocaráemseusfavoritos,umaespéciedememória
delongadura ção.
Amaiordificuldadeparaosmanipuladoresdamente,comodesigners,éconse-
guirtornaroreconhecimentodasa ções,objetivoseintera çõesnainterfacetãosim-
pleseintuitivosapontodeousuáriorelacionartalcomportamentocomalgoque
estáguardadonamemóriadelongadura ção,tambémconhecidacomomemóriase-
mântica. Porexemplo,oslidedeumafotocomumdedodeslizando,umlogono
cantosuperioresquerdoqueolevaparaapáginainicial,oureconhecerqueoícone
deumlápissignificaeditar. Quantomaisintuitivo,menosamemóriadetrabalho
precisaficartrabalhando,dandoumasensa çãodemaisseguran ça,menosesfor çoe
maisconfortoparaousuário.
Sabendo,então,queoreconhecimentodospadrõeséfeitobaseadonaexperiên-
ciadearmazenamentodecadaserhumano,comoumapessoapodeseacharsufici-
enteparacriarospadrõesqueserãoutilizadosportodaumaequipe,local,remotae
àsvezesatéinternacional?Criarpadrõeséalgoextremamentedifícil.
Criaçãocoletiva,umprojetodemuitos
LembrodequandotrabalhavanaPetrobras,emquetodasemanatínhamosuma
reuniãodeaproximadamente3horasparareverecriarospadrõesdaequipe.Nossa
36

## Página 45

CasadoCódigo Capítulo4. Tudoquevocêprecisasaberparacriarumframeworkdesucesso
metaeradocumentartodososcomponentesutilizados,deformaqueconseguísse-
mosmapeá-losemsuasvaria çõesedarinícioaumplanejamentodecorteportoda
aequipe,oquegeralmenteaconteciaemumquadrobranco.Nofim,umdosdesen-
volvedoresdaequipeeraresponsávelporcriaressecomponenteseguindoopadrão
criadoedocumentado.
Oprojeto,carinhosamentechamadode“zord”,eraumgrandeframeworkque
uniatodososcomponentesutilizadosnossistemasinternosdanossagerência(mais
de20sistemas). Nele,tínhamoscomponentespredefinidoscomoAbas,Sanfonas,
Navegações,Tabelas,Botões,GridseFormulários.Oprojetojápassoupormuitas
atualizaçõeseestásendoutilizadopelaequipeatéhojenosprojetosdaPetrobras.
Desde2003,nocome çodaminhacarreiradentrodeempresas,aideiadepadro-
nizarcomponentessempreestevepresenteemmim.Semprefuiummetódicocom-
pulsivo,queguardavareferênciasempastasseparadasporcomponentes,enãoeram
sóreferências:eucriavacódigosdessesartefatosseparadosparaquetodootimeti-
vesseacessoeperpetuasseessegranderepositório. NocasodaPetrobras,quando
comeceiafazerpartedotimedeproduto,identifiqueiqueexistiaumgranderetra-
balhoparacadaprojetocriado.Acreditoquequalquerretrabalhoéumsintoma,pois
dávisibilidadeaumproblemadeprocesso,sejacausadoporgargalos,inseguran ça,
ego,pregui çaoufaltadeexperiência.Assimsendo,comeceiamapeartodososcom-
ponentesqueeramutilizadosemmaisde2projetos,paracome çaraintermediar
peranteaequipeumaformadepadronizarmosoartefato.
Valelembrarqueapadroniza çãotambémenvolveoprocessodecria ção,entãoa
reuniãoenvolviapadrõesdedesignquetambémnãoeramcontempladospelotime,
atuandonaépocabasicamentecomoumafábricadesoftware.
Depoisdealgumassemanasestudandooprocesso,eu,DanielAraujoeMar-
celloMansocome çamosacriarumframeworkinternoqueprometiarevolucionara
formacomocriávamosformuláriosparaossistemasinternosdaPetrobras.Oponto
altodoprojetofoioGridcriado,pois,paraajustarmosnossoformulárioparaqual-
quercontainerdequalquersistema,teríamosquecriarumasolu çãoadaptativaem
porcentagem.Issomelevouaumaimersãodentrodogrid960criadopor Nathan
Smith,atéentãooGRIDmaisimportantedomundoquantoàdiagrama çãoWeb.
AdaptandoosistemadegridcriadoporNathan,criamosumframeworkfluidoba-
seadoem12colunas,proporcionando-nosmuitaagilidadeeflexibilidadenacria ção
deformuláriosWeb.Acreditoqueissosófoipossívelporcausadacria çãodapropri-
edade box-sizing,quepermitiufazeruminputcom paddinge borderocupar
100%daáreadeumcontainer.
37

## Página 46

4.1. Guerracontraosframeworksprontos CasadoCódigo
OframeworkdeixouumlegadotãograndeparaaPetrobrasqueganhamos3
prêmiosdecriaçãonoano.Talreconhecimentonosfezperceberqueoutraspessoas
eempresaspodiameestariampassandopelosmesmosproblemas.Logo,criamoso
Formee,umframeworkquefoimuitofamosoem2009/2011ebateuametademais
de70mildownloadsem2012.Infelizmente,comoboomdenovosframeworks,o
Formeeficouumtantoquantodesatualizado,masquemsabenãovolteembreve
comfor çatotal,nãoéverdade?
4.1 Guerra contra os frameworks prontos
ComumentesouperguntadosobresercontraoTwitterBootstrapeZurbFounda-
tion.Comoeusemprefalo,umframeworkpodeseroresponsávelpelosucessodo
seusiteedasuaaplica çãoelhepouparmilharesdedólares.Porém,malutilizado,
poderepresentarogargalododesenvolvimentodoseuprodutoelevaroseuprojeto
aofracasso.
Muitasvezes,aspessoasassociamaescolhadautiliza çãodeumframeworkao
ganhodetempo.Euentendoquetempoéacoisamaiscríticadentrodeumprojeto,
principalmentestartups,porém,eusempregostodeutilizaro "reductioadabsurdum”
paralembrarquefatiarumlayoututilizandooPhotoshopouFireworkstambémé
otimizaçãodetempo,assimcomoutilizarsitesprontos.
Namaioriadoscasos,odesenvolvedornãoinspecionaocódigodoframework,
passandoacriarumoutroarquivoCSSparacustomizaroseuprojeto.Emmuitos
outroscasos,odesigndoprojetoéinfluenciadopeloframework,passandoaterli-
mitaçõesquantoàescolhadeespa çamentos,grideoutrasvaria çõesquejáestãopre-
definidasnoframework.Tudoissoéumainversãodevaloresquantoaumprojeto,
poisagoraqueumtimedeprodutoestámaisintegradodoquenunca,trabalhando
commetodologiaságeis,documenta çõesepadrõesdefinidosemequipe,comopo-
demosaceitarqueumcódigodeumprojeto–queéo coredasuaaplica ção–está
sendodefinidoporumframeworkterceirosóporagilidade?
Porcontadessespensamentos, defendoacria çãodoseupróprioframework ,
emqueotimeanalisaráosartefatospresentesnaaplica ção,padrõesdeespa çamen-
tos,grids,fontes,palhetadecoreseintera çõesserãoosguiasparaacria çãodemó-
duloseumprojetoreutilizávelesustentável. Masparaissovocêprecisarádefinir
sevocêquerrealmentecontroletotalsobreoseucódigo. Vocênãoconseguecriar
umcódigomaissimples,commenosobjetosedependênciasdoqueosframeworks
prontos? Vocênãoacreditaque,empoucotempo,umframeworkpróprio,focado
38

## Página 47

CasadoCódigo Capítulo4. Tudoquevocêprecisasaberparacriarumframeworkdesucesso
noproblemaqueositeprecisaresolver,serámaiseficaz?Seasrespostasforemsim,
vocêestáaumpassodeaprenderacriaroseupróprioframework.
4.2 Organização e padronização
Pensaremaplica çõesémuitocomumparaprogramadoresback-endeatémesmo
programadoresJavaScript,mastenhoobservadoumgrupomuitograndededesen-
volvedoresfront-endqueatuammaisnessacamadaestruturaldeHTMLeCSS,por
issonãopodemosenemvamosignorá-los.Vamoscome çarpensandosobreaorga-
nizaçãodoprojeto.
Paradiscutirmossobreorganiza ção,énecessárioreverseusatuaispadrõesem
projeto.Respondaessasperguntassobreoseuprojeto:
1) Qualopadrãodecomentáriosporse çãoeinline?
2) Asclassesdoseuprojetosãofeitascomhífen(-),underscore(_),oucamelCase
(aA)?
3) Quetipodeformatodecoresvocêusanoseuprojeto?Hexadecimal?HSL?RGB?
RGBA?Nomedacor?
4) Comentários,classesedocumentaçõesestãoemqueidioma?Português?Inglês?
Misto?
Paracomponentizarsuapáginademaneirasustentável,vocêprecisaexplorarao
máximoaorganizaçãoepadroniza çãodoprojeto.Oproblemanaverdadeestáem
nossohistóricocomodesenvolvedores,poissemprefomosacostumadosadesenvol-
verdaseguinteforma:
• reset(zerarosestilosparainiciarumnovoprojeto);
• estrutura(criaraestruturabasedoprojeto,geralmentecompostoporheader,
main,footerecolunasmacro);
• página(definircustomizaçõesparacadapáginadoprojeto).
Essemodelotemsuautilidade,masdesenvolveratravésdefluxodepáginasé
muitocruelcomoCSS,poispassamossempreaincrementarocódigo,semobservar
oquejáfoicriadoeoquepodeserreutilizado.Assim,umbotãofeitonapágina1
39

## Página 48

4.2. Organizaçãoepadroniza ção CasadoCódigo
necessitadealtera çõesparaapágina2,eporcontadissonãopoderáserreutilizado
napágina3.Depoisdeumtempo,ninguémentenderáoseuCSS,nemvocêmesmo,
passandoavivertristeesozinho,abandonadonomundodasfolhasdeestilosem
organização.
Paraquemestácomeçando,recomendosempreutilizaromodelomaisbásicode
umprojetoorganizado:
• reset(zerarosestilosparainiciarumnovoprojeto);
• base(criarabasedoprojeto,geralmentecompostoporheader,main,footere
demaisestruturasbase);
• modules(defineoestiloparacadacomponentedeformaisolada,assimcomo
seusestadosdeintera ção);
• layout(fazasmudançasqueumcomponenteouqueabasepodeterparase
ajustaraumapáginaoucontextoespecífico).
Nessecaso,teoricamenteacabamoscomoconceitodedesenvolvimentodepá-
ginasepassamosatratarqualquerprojetocomoumaaplica ção.Infelizmente,ainda
énecessárioutilizarumarquivocomoo“layout”parafuncionarcomoumcoringa,a
fimdepermitircustomiza çõesporquestõesdelayoutdepágina.Mas,quantomenos
utilizá-lo,maismodularizadoesustentávelseráoseuprojeto.
Existeaindaumaoutraformadecriaroseumodelodeprojeto,focadoemte-
matização:
• reset(zerarosestilosparainiciarumnovoprojeto);
• base(criarabasedoprojeto,geralmentecompostoporheader,main,footere
demaisestruturasbase);
• theme(estilizaroprojetoquantoaovisualtemático,comocores,fundosefon-
tes).
Essaestratégiatemáticajáfoiutilizadaemdiversosprojetos,inclusivepormim
mesmo,tantonacria çãoinicialdoFormeequantonaprimeiraversãodoConfboi-
lerplate(https://github.com/braziljs/conf-boilerplate). Porém,euaindasintoque
colocartodososcomponentesna“base”ébastanteconfusoecontraproducente.
Sendoassim,passeiaadotarummodelomaiscompletoparaorganiza çãodepro-
jeto:
40

## Página 49

CasadoCódigo Capítulo4. Tudoquevocêprecisasaberparacriarumframeworkdesucesso
• reset(zerarosestilosparainiciarumnovoprojeto);
• base(criarabasedoprojeto,geralmentecompostoporheader,main,footere
demaisestruturasbase);
• components(defineoestiloparacadacomponentedeformaisolada,assim
comoseusestadosdeintera ção);
• form(defineoestilopratodososobjetosdeformulário,assimcomoseuses-
tadosdeintera ção);
• typography(defineoestiloparatodosososobjetostextuais,assimcomofon-
tesexternase iconfonts).
Ointeressantedessemodeloéaaten çãoquevocêpodedaraumcomponentees-
pecífico.Porexemplo,casoumprojetotenhaumagamadevaria çõesmuitogrande
deumcomponentebotão,vocêpodedarindependênciaaele,isolando-odoitem
“components”.Algunsexemplosdecomponentesque,dependendodesuascomple-
xidadesetamanhos,podemvirarumprojetopróprio:
• buttons
• table
• tabs
• news
• post
• grid
4.3 Nomenclatura
Umadascoisasemqueeumaisprestoaten çãoaoolharumcódigoéanomenclatura
utilizadaparadefinirasclassesdeumprojeto. Vejabem,digoapenasclasses,pois
nãovejosentidoemutilizarIDparaestiliza ção,vistoqueumaclassepodeseralta-
mentereutilizadaeoIDsópodehaverumporHTML.Sabendoquecadaumpode
teroseupróprioestilodenomearobjetos,mostrareiomeupadrãodenomenclatura
paraumbotão.
41

## Página 50

4.3. Nomenclatura CasadoCódigo
<!-- botão -->
<a class="btn"></a>
Percebaqueobotãorecebeonomede btn,umprefixoquefuncionabempara
portuguêsouinglês.Semprequepossível,euutilizotrêsletrasnoprefixo,seguido
dehífenparasepararaspalavrasdonome.Vejaaseguir:
<!-- botão primário -->
<a class="btn btn-primary" ></a>
Esseéopontoemquealgumaspessoasdivergem.Muitosdizemque,apartirdo
momentoemqueutilizamosCSS3,podemosutilizarosnovosseletorespararesgatar
oprefixo“btn-”,nãoprecisandorepetiraescritanoHTML.Casovocênãoconheça,
eisosdoisseletoresCSS3citadoscomosolu ções:
/* todos os itens que COMECEM na classe com o prefixo "btn-" */
[class^=btn-] {}
/* todos os itens que POSSUEM na classe o prefixo "btn-" */
[class*=btn-] {}
Eucreioqueessasolu çãosejamuitocustosaparaoCSS,nãosódeescrita,aceita-
ção,comotambémdeperformance.Assim,prefiroorientarasclassesaoobjetoque
euqueroestilizar,garantindomelhorperformance,intuitividadeedocumenta ção
doscomponentes.Sobreperformance,segueumalistacriadapor SteveSouders,que
mostracomoos regexselectorsbaseadosematributossãoruinsparaperformanceno
browser:
1) ID,e.g.#header
2) Class,e.g. .promo
3) Type,e.g.div
4) Adjacentsibling,e.g. h2 + p
5) Child,e.g. li > ul
6) Descendant,e.g. ul a
7) Universal,i.e.*
42

## Página 51

CasadoCódigo Capítulo4. Tudoquevocêprecisasaberparacriarumframeworkdesucesso
8) Attribute,e.g. [type="text"]
9) Pseudo-classes/-elements,e.g. a:hover
EmboraoIDsejaoseletormaisperformático,ofatodenãoserreu-
tilizável(explicadoanteriormente)éobastanteparaadotarclassescomo
seletoresprincipaisdoseuprojeto.
Vejamaisalgumasvaria çõesdeclassesparaoelementobotão.
btn-primary, btn-secondary, btn-delete, btn-edit,
btn-disabled
Oponto-chavenahoradecriarumaclasseéfocarsempreemsuafun ção.Porém,
existempequenasexce çõesquesãoadotadaspelomercado,porexemplotamanhos
predefinidosdebotãocomo btn-small, btn-large, btn-full.
Namaioriadosprojetos,algumasclassessetornamtãogenéricase
reutilizáveis,quedeixamdenecessitardeprefixo,como clear, omega,
alpha, small, large, fulletc.
4.4 Regras de estado
Cadavezmaisaplica çõestêmtidomaisintera çõescomousuárionoclient. Essas
interaçõescriamumaexperiênciacadavezmaisricaefantásticaparaousuário.O
problemaéquemuitasdessasintera çõessãofeitascomumamanipula çãoinlinedo
elemento,comoumJavaScriptdesabilitarumbotão,atribuindoCSSinlineparao
elemento. Ouaindaumbotãoquepossuiumíconedentro,sóquesemnenhuma
marcaçãoquemepermitacontrolarpeloCSStodososoutrosbotõesquetambém
possuamícones.
Ocontroledosestadosdoselementoséconhecidocomo staterules epodeaju-
darbastanteadocumentarecontrolarumprojeto.
1) Ousuárioestávendoumagaleriadeimagens.Aoclicarnobotão“vermaisfotos”,
ositecarregaráviaajaxmaisitens,deixandoum loadingnobotãoatéofinalda
operação.Qualaclasserecomendadaparaumbotãonomomentodo loading?
43

## Página 52

4.4. Regrasdeestado CasadoCódigo
Tudoindicaqueaescolhamaisóbviaseria btn-loading.Oproblemaéque
oprefixoindicaqueéumtipodebotãoenãoumestadodomesmo,assimsendo,
recomenda-seautiliza çãodedoisdosmaisconhecidos staterules,o is-e has-.
O is-indicaoestadodoelemento,geralmenteparaumestadoprovisório,ou
quepodeseralteradoaqualquermomentopelousuário:
is-loading, is-disabled, is-active, is-checkedetc.
O has-indicaoestadodepertencimentodoelemento,geralmenteparacon-
trolardiagrama çõesouespa çamentos:
has-photo, has-icon, has-comments, has-reviews, has-no-photo,
has-no-commentsetc.
Vamosconsiderarumsistemadenotícias,noqualtemosvaria çõesdanotícia
com/semimagemecom/sembotão.Nossaestruturaprincipaléassim:
<div class="news-item">
<div class="news-content">
<h1>Biscoito Globo </h1>
<p>Muitas vezes amigos de outras cidades me perguntam qual o
principal prato do Rio de Janeiro, eu sempre respondi feijoada,
mas creio estar enganado. A principal iguaria carioca é o famoso
biscoito Globo. Embora o biscoito de polvilho tenha sido
inventado em Minas Gerais e os irmãos criadores do biscoito
terem criado o mesmo em São Paulo. Então, se tem algo que você
não pode deixar de experimentar ao visitar a cidade maravilhosa
é tanto o biscoito salgado quanto o biscoito doce Globo,
acompanhado de um mate de galão, você não vai querer voltar para
sua cidade. </p>
</div>
</div>
Aoincluirumaimagem,nossocódigoviraria:
<div class="news-item">
<div class="news-media">
<img src="biscoito-globo.jpg" alt="Biscoito Globo" >
</div>
<div class="news-content">
<h1>Biscoito Globo </h1>
<p>Muitas vezes amigos de outras cidades me perguntam qual o
principal prato do Rio de Janeiro, eu sempre respondi feijoada,
mas creio estar enganado. A principal iguaria carioca é o famoso
44

## Página 53

CasadoCódigo Capítulo4. Tudoquevocêprecisasaberparacriarumframeworkdesucesso
biscoito Globo. Embora o biscoito de polvilho tenha sido
inventado em Minas Gerais e os irmãos criadores do biscoito
terem criado o mesmo em São Paulo. Então, se tem algo que você
não pode deixar de experimentar ao visitar a cidade maravilhosa
é tanto o biscoito salgado quanto o biscoito doce Globo,
acompanhado de um mate de galão, você não vai querer voltar para
sua cidade. </p>
</div>
</div>
Oproblemanesseexemploéqueoitem news-mediapassouaocuparparteda
diagramação,assimo news-contentvaideixardeocupar100%delargurapara
dividirespa çocomo news-media.Eupossotervários news-itememumalista.
Comoestamosreutilizandoasclasses,oqueeuprecisariafazerparamanterum
news-itemsemimagemeoutrocomimagem? Simples! Utilizandoas Regrasde
estado,vejaaseguir:
<div class="news-item has-img" >
<div class="news-media">
<img src="biscoito-globo.jpg" alt="Biscoito Globo" >
</div>
<div class="news-content">
<h1>Biscoito Globo </h1>
<p>Muitas vezes amigos de outras cidades me perguntam qual o
principal prato do Rio de Janeiro, eu sempre respondi feijoada,
mas creio estar enganado. A principal iguaria carioca é o famoso
biscoito Globo. Embora o biscoito de polvilho tenha sido
inventado em Minas Gerais e os irmãos criadores do biscoito
terem criado o mesmo em São Paulo. Então, se tem algo que você
não pode deixar de experimentar ao visitar a cidade maravilhosa
é tanto o biscoito salgado quanto o biscoito doce Globo,
acompanhado de um mate de galão, você não vai querer voltar para
sua cidade. </p>
</div>
</div>
Assim,eupoderiafazeraseguinteconfigura ção:
.news-media {
width: 28% ;
margin-right: 2% ;
45

## Página 54

4.4. Regrasdeestado CasadoCódigo
}
.has-img .news-content {
width: 100% ;
}
Adicionandoumbotãoparaacessarosite,usaríamosomesmoartifício:
<div class="news-item has-img has-btn" >
<div class="news-media">
<img src="biscoito-globo.jpg" alt="Biscoito Globo" >
</div>
<div class="news-content">
<h1>Biscoito Globo </h1>
<p>Muitas vezes amigos de outras cidades me perguntam qual o
principal prato do Rio de Janeiro, eu sempre respondi feijoada,
mas creio estar enganado. A principal iguaria carioca é o famoso
biscoito Globo. Embora o biscoito de polvilho tenha sido
inventado em Minas Gerais e os irmãos criadores do biscoito
terem criado o mesmo em São Paulo. Então, se tem algo que você
não pode deixar de experimentar ao visitar a cidade maravilhosa
é tanto o biscoito salgado quanto o biscoito doce Globo,
acompanhado de um mate de galão, você não vai querer voltar para
sua cidade. </p>
</div>
<div class="news-btn">
<a class="btn" href="http://www.biscoitoglobo.com.br">Ver site </a>
</div>
</div>
Adicionandoapossibilidadedo has-btnaoprojeto,aumentaríamosacomple-
xidadedaconfigura ção:
.news-media {
width: 28% ;
margin-right: 2% ;
}
.news-btn {
width: 28% ;
margin-left: 2% ;
}
.has-img .news-content,
.has-btn .news-content {
46

## Página 55

CasadoCódigo Capítulo4. Tudoquevocêprecisasaberparacriarumframeworkdesucesso
width: 70% ;
}
.has-img.has-btn .news-content {
width: 40% ;
}
Percebaqueanotíciaestápreparadaparareceberapenaso has-img,mudando
ocontentpara70%.Casoelarecebaapenaso has-btn,ocontenttambémmudará
para70%.Porém,sereceberosdois, has-imge has-btnaomesmotempo,ele
configuraocontentpara40%.Incrívelefácilné?
Trabalharcomprefixosfocadosnafun çãoepensarnosestadosdoselementos
nosfazdiminuirbastanteoriscodeumprojeto,alémdegarantirmaisqualidade
paracriarmosospróximosartefatos.
4.5 Modularização :P ensando em seu projeto como
um sanduíche
“Aosepararumsanduícheempedaçosmenores,vocêpoderapidamentee
eficientementecriarumainfinidadedevariedades.Assimqueasclassesdeveriamser
baseadas.Emvezde“#sanduiche”agoratemos
“.pao.alface.queijo.salame.tomate.maionese”eissoéincrível!Nãogostadetomate?É
fácildeixá-lofora...ClassesbaseadasemestruturasécomocomernoSubway(sóque
melhor).
–HarryRoberts
Lembrodeumaépocaemquedesignersprojetavampáginase,depoisdese-
manas,elaseramentreguesparaodesenvolverfront-end“cortá-las”.Sevocêainda
segueessemétododetrabalho,estámaisdoquenahoradeseatualizareseadequar
aomercadoágil.Hojeemdia,criamos features,componentespadronizadosquesão
ajustadoseminterfaces,deacordocomofluxodousuário.
Odesignerpassaaprojetarfluxoseseusartefatos,passandodeformaiterativa
paraodesenvolvedorquesempre“corta”oscomponentesisoladamente,podendoser
utilizadosereutilizadosemqualquerlugardaaplica ção,nãoimportaqualapágina
ouse ção.
Essenovomodelode“corte”éoquedeuorigemaopolêmico"CSSOrientado
aoobjeto”. Comovimosanteriormente,osprefixossãovinculadosexclusivamente
àfun çãodecadaobjeto,acompanhadosdesuasextensões. Vimosaaplica çãodo
botão,vejamosalgunsoutrosobjetosesuaspossíveisclasses:
47

## Página 56

4.5. Modularização:Pensandoemseuprojetocomoumsanduíche CasadoCódigo
tooltip: tooltip, tooltip-pin-down, tooltip-pin-up,
tooltip-small, tooltip-header, tooltip-content.
tabs: tabs-nav, tabs-item, tabs-link, tabs-content.
Vamoscriarumartefatodenavega çãocomasclassesaseguir:
nav: nav-list, nav-item, nav-link.
<nav class="nav">
<ul class="nav-list">
<li class="nav-item">
<a href="#" class="nav-link"></a>
</li>
<li class="nav-item">
<a href="#" class="nav-link"></a>
</li>
<li class="nav-item">
<a href="#" class="nav-link"></a>
</li>
</ul>
</nav>
1) Precisamosdesenvolverumcomponentedemensagens,comovocêfaria?
Eucometiaumerroemmeuscódigosaoutilizarocomponentede
mensagemvinculadoaocomponentedeformulário.Felizmente,fuiper-
cebendoquemensageméumcomponenteisolado,poisapareceaolongo
dosistemaeemdiferentesmomentos. Sendoassim,passeiautilizaro
nome alertparaoelementodemensagem.
U m a o u t r a m u d a nçaquefiznessecomponentefoiaretiradadosprefi-
xosdascustomiza ções.Porexemplo,antigamenteutilizava msg-error
paraocomponente msg,maspercebiquepalavrascomo success,error,
informationewarning,sãobastantereutilizáveisemoutroscomponentes.
Assimsendo,passeiausarapenas errornacomponentedemensagem
–vocêpodeutilizar“alerta”,sepreferir.
48

## Página 57

CasadoCódigo Capítulo4. Tudoquevocêprecisasaberparacriarumframeworkdesucesso
Tipografia
“TextisaUI”
–JakobNielsen
Muitasvezesesquecemosdaimportânciadatipografiaemumainterface,sóque
ela,possivelmente,éocomponentemaiscrucialdoseuprojeto.Precisamosdefinir
oselementostextuaisdaaplica ção.Elesgeralmentesãotítulos,subtítulos,listas,pa-
rágrafoselinks.Ébastanteimportantevocêsimulartodasascombina çõespossíveis
naetapadetestes,poissemprepodeocorreralgumincômodoparaousuário.Veja
ocódigoaseguir:
<h2>Lorem ipsum dolor sit. </h2>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Modi,
fugit voluptatem vero rem nesciunt corrupti accusamus fuga enim ut
autem. Molestias, ipsam dolores inventore officia quod cupiditate
repellendus labore ipsa. </p>
<h2>Lorem ipsum dolor sit. </h2>
Elenãoéamesmacoisaqueeste:
<h2>Lorem ipsum dolor sit. </h2>
<h3>Lorem ipsum dolor sit. </h3>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Modi,
fugit voluptatem vero rem nesciunt corrupti accusamus fuga enim ut
autem. Molestias, ipsam dolores inventore officia quod cupiditate
repellendus labore ipsa. </p>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Modi,
fugit voluptatem vero rem nesciunt corrupti accusamus fuga enim ut
autem. Molestias, ipsam dolores inventore officia quod cupiditate
repellendus labore ipsa. </p>
<h3>Lorem ipsum dolor sit. </h3>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Modi,
fugit voluptatem vero rem nesciunt corrupti accusamus fuga enim ut
autem. Molestias, ipsam dolores inventore officia quod cupiditate
repellendus labore ipsa. </p>
Umsubtítulopodefuncionarmuitobemaoserelacionarcomumparágrafo,
maspodeficarterrívelaoserelacionardiretamentecomoutrosubtítulo,ouaose
utilizaromesmoparaparágrafosúnicoseparágrafosconsecutivos.Oidealévocê
testartodasessascombina çõesafimdeidentificarummeiotermodeespa çamentos
emargens.
49

## Página 58

4.5. Modularização:Pensandoemseuprojetocomoumsanduíche CasadoCódigo
Acreditoquetodateladeumaaplica çãotenhaoseutítulodapágina
específica. Essetítulotendeaterumtratamentoeespa çamentoparao
restantedoconteúdodiferenciado. Paranãoimpactartodososoutros
subtítulos,eucrioumaclasse page-titleparaesseelemento,fazendo
asdiferencia çõesparaessafun çãodestacada,deixandodeinfluenciaras
demaisaplica çõesdamesmatag.
Testaratipografiadeumprojetoéanalisarsuasvaria çõesecombina çõescom
outroselementos.Paravocêconhecerumpoucomaissobretipografianapartede
front-end,recomendoawikido Normalize.css,criadopeloNicolasGallagher( https:
//github.com/necolas/normalize.css/wiki),queretrataafaltadepadroniza çãona
mostragemdoselementostextuaisentreosbrowsers.ONormalizeéumframework
bastantefamoso,responsávelpelareinicializa çãodoCSSparatodososnavegadores,
preservaçãodospadrõesdeestiloeresolu çãodeinconsistênciasentreoselementos
tipográficos.
GRID
CriarumGRIDétalvezumadastarefasmaisdifíceisnahoradesecriarum
projeto,nãoéàtoaqueeleéresponsávelpelofatodeamaioriadaspessoasutilizar
frameworksprontos.EusemprelembrodequandocrieioFormeeecomofoidifícil
criarcálculosemaiscálculosparachegaraoGridflexívelperfeito,poisoGridé
umaparteperigosadoprojeto,principalmenteporexigiralgumasescolhasdesdeo
começo,como:
• Usareifloatparadiagrama ção?
• Usareialgumpré-processadorcomoLess,SassouStylus?
• Usareicolunasempixelsoucolunasflexíveis?
• Minhascolunasserãoresponsivas?
EmFevereirode2014,fizumprojetodeexperiêncianaempresaeoganha-
dorpassou3diascomigo,ajudando-meacriaronovoframeworkdeumproduto.
Quandocome çamosadefiniroGRID,deiatarefadeanalisar3dosframeworksde
GRIDmaisfamososdomercadoparasaberqualutilizaríamos.Vejaasop ções:
TwitterBootstrapv2
50

## Página 59

CasadoCódigo Capítulo4. Tudoquevocêprecisasaberparacriarumframeworkdesucesso
<div class="row">
<div class="span4">...</div>
<div class="span3 offset2" >...</div>
</div>
Bootstrapv3
<div class="row">
<div class="col-md-8">...</div>
<div class="col-md-4">...</div>
</div>
ZurbFoundation
<div class="row">
<div class="small-6 large-2 columns" >...</div>
<div class="small-6 large-8 columns" >...</div>
<div class="small-12 large-2 columns" >...</div>
</div>
Semanticgs
@column-width: 60;
@gutter-width: 20;
@columns: 12;
header { .column(12); }
article { .column(9); }
aside { .column(3); }
BootstrapLESSvariables
@grid-columns: 12;
@grid-gutter-width: 30px;
@grid-float-breakpoint: 768px;
header {.make-lg-column(12);}
article {.make-lg-column(9);}
aside {.make-lg-column(3);}
NãogostodonomedasclassesdoBootstrapv2,nemdanãosepara çãoentre
onomeeonúmero. OFoundationeanovaversãodoBootstrapjápossuemum
51

## Página 60

4.6. Agrupandoseuscomponentesemumúnicolocal CasadoCódigo
nomemaiseleganteemaisorganizado. Oquemaismeincomodanessessistemas
deGRIDéautiliza çãode“row”paraincluirascolunas. Vocêéobrigadoapena-
lizaroseuHTML,incluindotagssemvaloralgum,simplesmenteparaconseguir
fazerlinhasdecolunas. Definitivamente,criarumframeworkdeGRIDéanalisar
bastanteocustoxbenefíciodepoluiralgoemfun çãodeumsistemareutilizável.
Dentrodessasop ções,escolhemosoSemantic.gs( http://semantic.gs)que,diferente
dosdemais,nãoengessaquantidadedecolunasnamarca ção,nãopoluioHTMLeé
extremamenteconfigurávelatravésdepré-processadores.
Comovocêspodemver,oBootstrap3agoratambémpossuiapossibi-
lidadedosistemadeGRIDvinculadoavariáveisemLESS,porém,pela
elegânciaeporserfocadoapenasemGRID,achamososemanticmais
interessanteparaoprojeto.
AescolhadoGRIDtemqueserfeitaporprojetoe,novamente,recomenda-se
queenvolvaaequipeemtestesparaatomadadedecisão,atémesmoseadecisãofor
acria çãodoseuprópriosistemasdeGRID,comofiznoFormee.
UmadicaparaquemestáestudandoodesenvolvimentodeGRIDsé
pesquisarsobreoatributoCSS box-sizingqueéresponsávelpormu-
darodisplaydo boxmodel,passandoaconsideraro paddinge border
nahoradeaparecernalargura/alturafinal. O box-modelconvencional
nãoosconsideranalarguraealtura,somandonoresultadoosvalores,
ouseja,300pxdelarguraacabasetornando300px+2pxdeborda+10px
depadding=312pxtotal.
4.6 Agrupando seus componentes em um único local
Amelhormaneiradedesenvolveroscomponentesisoladosdeumprojetoénão
desenvolvê-lonapáginaemquestãoe,sim,emumlocalseparado.Esselocalreúne
todososcomponentesreutilizáveisdoprojeto,funcionandocomoumespa çode
documentação,guiaerepositóriodecomponentes. Vejaporexemplo,o "UIkit”
doTwitterBootstrap( http://getbootstrap.com/components/)edoZurbFoundation
(http://foundation.zurb.com/docs/).
52

## Página 61

CasadoCódigo Capítulo4. Tudoquevocêprecisasaberparacriarumframeworkdesucesso
Vocêprecisacriaressapáginadeapresenta çãoondelistaráoscomponentespa-
dronizados.Emumprimeiromomento,vocêpodeinseriroscomponentesnapá-
gina,agrupandodamaneiraqueacharmaisorganizada(vejaoslinksanteriorespara
inspirar-se).Essaetapalhedarámaisseguran ça,poisacadacomponentefinalizado,
vocêesuaequipecomemorarãoopadrãocriado.Lembre-seque,maisdoquecriar
oscomponentes,éprecisosemprevoltarparamelhorarseusartefatos,identificando
pontosdemelhoriaoubugs,tratandoeatualizando-osnessamesmapáginadepa-
drões.
Element.css
Foi lançadoumprojetochamadoElementCSS( http://elementcss.
com)focadoemajudareotimizaracria çãodeumguiaemcimados
componentesdoseuprojeto.Oprojetoorganizaseuscomponenteson-
line,assimseutimepodeselogarevisualizarospadrõesemqualquer
lugarconectadoainternet,alémdecriarnovoscomponentesouvaria-
çõessemprequequiser. Umoutrorecursointeressanteépoderbaixar
aqualquermomentooCSScompiladodetodososcomponentes. Para
projetosgrandes,creioserumpoucolimitado,masparaquemestáco-
meçando,podeserumabelamãonaroda.
Odesignermodernojáprojetaositeouaplica çãoatravésdeum "UIkit”,fi-
candomaisfácilparaodesenvolvedorrecriá-loedocumentá-lo. Paraquealguns
componentesseencaixemdentrodadiagrama çãodesseguia,recomendocriarum
CSSinternodentrodessedocumentocomvaria çõesapenasparacompormelhoro
kit(puramenteestético).Costumosepararcadacomponentedentrodese ções,então
vejaumexemplodeumCSSdentrodo "UIkit”:
.ui-kit {
padding: 50px ;
}
/* SECTIONS */
.section {
position: absolute;
top: 50px ;
margin-right: 50px ;
}
53

## Página 62

4.6. Agrupandoseuscomponentesemumúnicolocal CasadoCódigo
.section-header {
position: absolute;
top: 50px ;
left: 50px ;
}
.section-btn {left: 330px ;}
.section-texts {
left: 330px ;
top: 200px ;
}
.section-progress {
left: 330px ;
top: 550px ;
width: 400px ;
}
.section-form {
left: 630px ;
top: 700px ;
right: 0 ;
}
.section-alerts {
left: 50px ;
top: 700px ;
}
Juntarseusprincipaiscomponentesemumúnicoarquivomudaráasuaformade
pensareescreverHTMLeCSS.Osprincipaisbenefíciosdesecriarumdocumento
separadosão:
• VerseseuocomponentefuncionasemherançaCSS;
• Terseusmódulosdocumentados;
• Proporreutilizações,aoinvésdedesenvolverpáginas;
• Proporanálises360noscomponentes,sugerindomelhoriasisoladas;
• AtingiroDRYCSS(don’trepeatyourself).
54

## Página 63

CasadoCódigo Capítulo4. Tudoquevocêprecisasaberparacriarumframeworkdesucesso
4.7 Tornando -se o rei dos padrões
Obenefíciodamodulariza çãoéincrívelejátiveafelicidadedeverganhosemdi-
versosprojetosemqueeuatuei.Algunscomponentesmeusemmuitosprojetossão
realmenteidênticos. Assimsendo,eupossocopiartantooHTMLquantooCSS,
fazendopequenasaltera ções. Maisdoqueisso,eupossoatémesmocriar snippets
emmeueditor,para,comumsimplesatalho,gerarocomponentedesejado.Issosó
épossívelfazercomumamadurecimentodepadrõeseescrita.
Certavez,estavadandoumtreinamentoparaumainstitui çãodeensinoeumdos
exercíciospráticoseradividiraturmaem2grupos,sendoqueelesteriam5minutos
paracriaroplanejamentodecortedapáginadoFacebook,determinandooscom-
ponentesecriandoopadrãodeclasses.Oresultadofoisurpreendente!Oprimeiro
grupocriouasclassesfocadasnoscomponentes,utilizando btn-e comment-,en-
quantoooutrogrupocriouclassesfocandonasa ções edit-e link-. Nofim,
pegueiocapitãodecadagrupoecoloqueiparaexplicaroplanejamentoproduzido
pelooutrotime. Reconhe çoquefoiengra çadoverastentativasdelereentender
padrõescomo b-e f-,aindamaissabendoquealguémdeforanuncapodejulgar
queopadrãodeumtimenãoestácerto.
Nãoexistepadrãoerrado,assimcomonãoexistem2padrões.Existeamáxima:
sevocêtemmaisdeumpadrão,elenãoéumpadrão.Então,parasetornaroreidos
padrões,vocêprecisapensarquevocênãoestácriandoumprojetoparavocêmesmo
e,sim,paraooutro.
Em2009,eujábradavaemalgumaspalestrasquevocênãotemquecriarum
códigoquesóvocêentende,achandoqueissoofaránecessárioparaaempresaou
projetoqueestáatuando. Casoumpróximodesenvolvedorassumaoprojetoouo
seucargo,eleeaempresatêmqueselembrardevocêpelasuaqualidadedeescrita
edeorganiza ção,enãopeloseuegoísmodeumcódigonãopreparado.Agoraque
vocêjáiniciouseutreinamentoparasetornaroreidospadrões,voudeixá-lopraticar
comseueditorequalquerdúvidaésómeprocurar.Boasorte!
55

## Página 64

4.7. Tornando-seoreidospadrões CasadoCódigo
Sobre o autor
BernardDeLunaatuaemprojetosdigitaisdesde1999, jápartici-
poudediversosprojetosdoBrasil,EUA,Inglaterra,Fran çaeAustrá-
lia. NosúltimosanoslideroutimedeprodutosnaPetrobras,foidire-
torcriativodaMeltDSP,coordenadordeprodutodaEstanteVirtual
eatualmenteéHeaddeprodutonoVideologeco-founderdoFretei-
ros.com.EspecializadoemFront-end,DesignfuncionaleMarketingDi-
gital,BernardjádeumentorianaLeanStartupMachine,émentorda
PapayaVenturesedaCodemy,jápalestrouemmaisde70eventospelo
Brasil,alémdoeventointernacionaldoW3C,StartupCampLATAMe
HTML5DevConf,entreoutros.Notempovago,adoratirarfotodoseu
cachorrocomahashtag #jupidog,temumamaniafeiadefalaremter-
ceirapessoaeseautointitula“sexywebprojectsspecialist”.
56

## Página 65

Capítulo5
Tornandoawebmaisdinâmicacom
AngularJS
5.1 Por queAngular JS
O JavaScript evolui de forma significativa com a criação de novos frameworks,
tornando-se,acadadia,maispoderosoeutilizadoentreosdesenvolvedores. Um
deleséojQuery,amplamenteconhecidoepraticamenteobrigatóriosevocêdeseja
controlaroselementosdeumapáginaHTML,tambémchamadodeDOM.
Seguindoessalinha,diversosframeworksdequalidadecontinuamsurgindo,e
dentreelestemosoAngularJS,queseráonossoprincipalobjetodeestudo.
ConhecendoAngularJS
AngularJSéconstruídosobreaideologiadequeaprograma çãodeclarativadeve
serusadaparaconstru çãodeinterfacesecomponentes,enquantoqueaprograma ção
imperativaéexcelenteparaescreverasregrasdenegócio.

## Página 66

5.2. AngularJS CasadoCódigo
OframeworkseadaptaeestendeoHTMLtradicionalparaumamelhorexpe-
riênciacomconteúdodinâmico,comaliga çãodiretaebidirecionaldosdados(os
famososdata-binding). Issopermitesincroniza çãoautomáticademodelseviews,
abstraindoamanipula çãodoDOMemelhorandoostestes.
AngularJSconseguiuatrairmuitaaten çãonessesúltimostempos, principal-
mentedevidoaoseusistemainovadordemodelagem,facilidadededesenvolvimento
epráticasdeengenhariamuitosólidas.AlgunsdosobjetivosdoAngularJSsão:
1) AbstrairamanipulaçãodoDOMdalógicadoapp.Istomelhoraostestes;
2) Consideraostestesdoapptãoimportantesquantoseudesenvolvimento.Adifi-
culdadedotesteédiretamenteafetadapelamaneiracomoocódigoéestruturado;
3) Abstraioacoplamentoentreoladoclienteeoladoservidordaaplica ção.Permi-
tindoqueodesenvolvimentodoappevoluaemambososlados,deformaparalela,
epermiteoreúsodecódigo.
Aversão1.0foilan çadaapenasemjunhode2012.Narealidade,otrabalhocome-
çouem2009comoumprojetopessoaldeMi škoHevery,umfuncionáriodoGoogle.
Aideiainicialacabousendotãoboaque,nomomentodaescrita,oprojetofoiofi-
cialmenteapoiadopeloGoogle,ehátodaumaequipedoGoogletrabalhandoem
tempointegralnoAngularJS.OprojetoéopensourceeestáhospedadonoGitHub
(https://github.com/angular/angular.js).ÉlicenciadopelaGooglesobreostermos
delicen çaMIT.
5.2 Angular JS
ParausaraestruturaAngularJSsãonecessáriasduasaltera çõesemnossodocumento
HTML,PHP,Railsetc.
Aprimeiracoisaasefazeréincluirabibliotecaemnossodocumento.Asegunda,
éincluirapropriedade ng-appnoelemento htmlemquequeremos“ativar”o
aAgularJS.Nestecaso,come çamosinserindonatag <html>donossodocumento.
Vejaoexemploaseguir:
HelloWorldAngularJS
<html ng-app>
<head>
58

## Página 67

CasadoCódigo Capítulo5. TornandoawebmaisdinâmicacomAngularJS
<title>Titulo Página </title>
<script
src="//ajax.googleapis.com/ajax/libs/angularjs/1.2.11/angular.min.js">
</script>
</head>
<body>
<input ng-model="nome">
<h1>Olá {{ nome }} </h1>
</body>
</html>
Códigoonline: http://plnkr.co/edit/FemetcT1h1HraRQLnT4x
Mesmoesteexemplosimplestrazàtonaalgumascaracterísticasimportantesdo
sistemadetemplatesAngularJS:
• TagsHTMLpersonalizadoseatributos:sãousadosparaadicionarcomporta-
mentodinâmicodeumdocumentoHTMLdeoutraformaestática;
• Chavesduplas({{expressão}}):sãoutilizadascomoumdelimitadorpara
expressõesqueexibemvaloresdomodelo.
No AngularJS, todas as tags HTML e atributos especiais que o framework
podecompreendereinterpretarreferem-secomo diretrizes. Noexemplo,vimos
a ng-appea ng-model.
ModeloMVCnoAngularJS
Quasetodasasaplica çõeswebexistenteshojesãobaseadasdealgumaformano
padrãomodel-view-controller(MVC).Entretanto,oMVCtemumproblema:ele
nãoéumpadrãomuitopreciso,mesmopossuindoumaboaarquitetura.Parapiorar,
existemmuitasvaria çõesederivadosdopadrãooriginal–entreosquaisMVP( http:
//pt.wikipedia.org/wiki/Model-view-presenter)eMVVM( http://en.wikipedia.org/
wiki/Model_View_ViewModel)parecemserosmaispopulares.
Paraaumentaraconfusão,hádiversasestruturas,eosdesenvolvedorestendem
ainterpretarospadrõesmencionadosdeformadiferente. Issoresultaemsitua-
çõesemqueomesmonomeMVCéutilizadoparadescreverváriasarquiteturase
abordagensdecodifica çãodiferentes. MartinFowlerresumeissomuitobemem
http://martinfowler.com/eaaDev/.
59

## Página 68

5.2. AngularJS CasadoCódigo
OtimedoAngularJStemumaabordagemmuitopragmáticaparatodaafamília
depadrõesMVC.Eledeclaraqueoframeworkébaseadonopadrão MVW(model-
view-whatever).Basicamenteéprecisovê-loema çãoparaobterasensa çãodesua
utilidade:
Visãodetalhada
Oexemploquevimosatéagora, "OláMundo”,nãoempregouqualquerestratégia
deestratifica çãoexplícita:inicializa çãodedadoselógica.
Emqualqueraplica çãonomundoreal,noentanto,éprecisoprestarmaisaten-
çãoaumconjuntoderesponsabilidadesatribuídasacadacamada. Felizmente,o
AngularJSoferecediferentesconstru çõesarquitetônicasquenospermitemconstruir
adequadamenteaplica çõesmaiscomplexas.
<!DOCTYPE html>
<html ng-app="nome_meu_app">
<head>
<meta charset="utf-8">
<title>Título Página </title>
<script
src="//ajax.googleapis.com/ajax/libs/angularjs/1.0.8/angular.min.js">
</script>
<script src="app.js"></script>
</head>
<body>
<div ng-controller="OlaCtrl">
Como você está <input type="text" ng-model="nome"><br>
<h1>Eu estou muito bem, {{nome}}! e você? </h1>
</div>
</body>
</html>
Vejaqueagorausamosumanovadiretiva, ng-controller,comumafun ção
JavaScriptcorrespondente.O OlaCtrlaceitaumargumento $scope.
var app = angular.module(’nome_meu_app’, []);
app.controller(’OlaCtrl’, function($scope) {
60

## Página 69

CasadoCódigo Capítulo5. TornandoawebmaisdinâmicacomAngularJS
$scope.nome = ’Giovanni’;
});
Códigoonline: http://embed.plnkr.co/82gR2y7Z4mOPwz7gEgSG/preview
Scope
U m$scope,objetonoAngularJS,estáaquiparaexporomodelodedomínio
paraumavisão.Aoatribuirpropriedadesparaumainstânciadeescopo,podemos
fazernovosvaloresàdisposi çãodeummodelopararenderiza ção.
$scopepodeserampliadocomdadosefuncionalidadesespecíficasparaum
determinadopontodevista.PodemosexporlógicaespecíficadeUIparaosmodelos
dedefini çãodefun çõesemumainstânciadeescopo.
Pode-secriarumafun ção lerNomeparanossavariável nome.
Exemplo:
var OlaCtrl = function ($scope) {
$scope.lerNome = function() {
return $scope.nome;
};
};
Podemosusá-lodaseguintemaneira:
<h1>Olá, {{ lerNome() }}! </h1>
Oobjeto $scopenospermitecontrolarcomprecisãoemqualpartedomodelo
asopera çõesestãodisponíveisparaacamadadevisão. Conceitualmente,escopos
AngularJSestãomuitopertodo ViewModel,opadrão MVVM.
Hierarquiasdeescopo
Vamosolhardeoutraformaparaoexemplosimples OlaCtrlquejáfizemos:
var OlaCtrl = function ($scope) {
$scope.nome = ’World’;
};
O OlaCtrlésemelhanteaumafun çãoregulardoconstrutorJavaScript,não
háabsolutamentenadaemespecialsobreelealémdoargumento $scope.
61

## Página 70

5.2. AngularJS CasadoCódigo
U m n o v o$scopefoicriadopeladiretiva ng-controllerusandoométodo
Scope.$New(). Espereummomento,parecequetemosdeterpelomenosuma
instânciadeumescopoparacriarumnovoescopo. Defato! AngularJStemuma
notaçãodo $rootScope(umescopoqueépaidetodososoutrosescopos). A
instância $rootScopeécriadaquandoumanovaaplica çãoébootstrapped(inicia-
lizada).
Adiretiva ng-controlleréumexemplodeumadiretivadecria çãodeescopo.
AngularJSirácriarumanovainstânciadaclasse Scopesemprequeencontraruma
diretivadecria çãodeescoponaárvoreDOM.Umescoporecém-criadoiráapontar
paraoseupai,usandoapropriedade $parent.
Vamosdarumaolhadanoexemploquefazusodeumadiretiva ng-repeat:
var MundoCtrl = function ($scope) {
$scope.populacao = 70000000 ;
$scope.paises = [
{nome: ’Brasil’, populacao : 63.1 },
{nome: ’Alemanhã’, populacao : 60.1 }
];
};
NossoHTMLficaassim:
<ul ng-controller="MundoCtrl">
<li ng-repeat="pais in paises" >
{{pais.nome}} tem uma população de {{pais.populacao}}
</li>
<hr>
População do mundo: {{populacao}} Milhões de pessoas
</ul>
Adiretiva ng-repeatnospermiteiterarsobreumacole çãodeobjetos(países)
ecriarnovoselementosDOMparacadaitememumacole ção.Asintaxedadiretiva
deveserfácildeseguir.Umnovavariável paisécriadaparacadaitemeexposta
emum $scope.
Háumproblemaaqui,ouseja,umanovavariávelprecisaserexpostaemum
$scopedecadaobjeto( pais)enãopodemossimplesmentesubstituirvaloresan-
teriormenteexpostos. AngularJSresolveesteproblemaatravésdacria çãodeum
novoescopoparacadaelementodeumacole ção.
62

## Página 71

CasadoCódigo Capítulo5. TornandoawebmaisdinâmicacomAngularJS
Views
NósjávimosexemplossuficientesdemodelosAngularJSparaperceberquenão
émaisumalinguagemdemodelagem,mascompletamenteummonstro.Nãosópela
suasintaxedemodeloepornospermitirampliarovocabulárioHTML,mastambém
temacapacidadeúnicadeatualizarpartesdatela,semqualquerinterven çãomanual.
Narealidade,oAngularJStematémesmoconexõesmaisíntimascomoHTML
eoDOM,poisdependedeumnavegadorparaanalisarotextodomodelo.Depois
queonavegadortansformaotextodamarca çãonaárvoreDOM,oAngularJSretro-
cedeepercorreaestruturaDOManalisada.Cadavezqueencontrarumadiretiva,
oAngularJSexecutasualógicaparatransformardiretivasempartesdinâmicasda
tela.
Declarandoumaviewtemplate
Vamosimaginarqueprecisamoscriaruma ListadeTarefas,cujopropósitoéadi-
cionaritensaumalista,comaop çãodemarcarcomo“feito”,equemostrequantas
tarefasestãoprontas.Paraisso,precisamosdoseguintetemplate:
<div ng-controller="TarefasCtrl" class="todo">
<span>{{restante()}} de {{todos.length}} restante </span>
<ul class="unstyled">
<li ng-repeat="todo in todos" >
<input type="checkbox" ng-model="todo.feito">
<span class="feito-{{todo.feito}}">{{todo.text}}</span>
63

## Página 72

5.2. AngularJS CasadoCódigo
</li>
</ul>
<form ng-submit="addTodo()">
<input type="text" ng-model="todoText" size="30"
placeholder="Adicionar novas tarefas" >
<input class="btn" type="submit" value="adicionar">
</form>
</div>
Vamostrabalharemcimadocódigoanterior.Emprimeirolugar,éprecisomos-
trarquantastarefasprontaseutenhoemminhalista.
$scope.restante = function() {
var count = 0 ;
angular.forEach($scope.todos, function(todo) {
count += todo.feito ?0:1 ;
});
return count;
};
Afun ção restanteédefinidapelocontroller TarefasCtrl.Vejaoexemplo
aseguir:
’use strict’ ;
var ColetaneaFrontEnd = angular.module(’meu_app’);
ColetaneaFrontEnd.controller(’TarefasCtrl’, function( $scope ) {
$scope.restante = function() {
var count = 0 ;
angular.forEach($scope.todos, function(todo) {
count += todo.feito ?0:1 ;
});
return count;
};
});
Agora, é preciso adicionar elementos em nossa lista paraque nossa função
restante()funcione.Paraisso,voucriarumalistaedepoisireimanipulá-lacom
afun ção addTodo()quepermiteadicionarnovositens.
64

## Página 73

CasadoCódigo Capítulo5. TornandoawebmaisdinâmicacomAngularJS
var app = angular.module(’meu_app’, []);
app.controller(’TarefasCtrl’, function($scope) {
//Lista com as tarefas
$scope.todos = [
{
tarefa:’Tarefa 01’ ,
feito:true
},
{
tarefa:’Tarefa 02’ ,
feito:false
},
{
tarefa:’Tarefa 03’ ,
feito:false
}
];
//Adicionar novos elementos a lista
$scope.addTodo = function() {
$scope.todos.push({ tarefa :$scope.todoText, feito :false });
$scope.todoText = ’’;
};
//Calcular quantas tarefas estão prontas
$scope.restante = function() {
var count = 0 ;
angular.forEach($scope.todos, function(todo) {
count += todo.done ?0:1 ;
});
return count;
};
});
Códigoonline: http://embed.plnkr.co/fzc1hHQ08prTgOxKPapD/preview
5.3 Módulos e injeção de dependências
Osleitoresatentosprovavelmentenotaramquealgunsdosexemplosapresentados
atéagoraestavamusandofun çõesconstrutorasglobaisparadefinircontrollers.Mas
65

## Página 74

5.3. Móduloseinjeçãodedependências CasadoCódigo
oestadoglobaléomaldaaplica ção,jáquetornaocódigodifícildemanter,testar
eler.DemodoalgumAngularJSvaisugerirestadoglobal.Pelocontrário,elevem
comumconjuntodeAPIsquesetornafácildedefinirequesimplificaoregistrode
objetosnomódulo.
Vejamosumcontrollerdefinidoglobalmentedeformaincorreta.
var OlaCtrl = function ($scope) {
$scope.nome = ’World’;
}
Eagoradaformacorreta,comoAngularJSindicaafazer.
angular
.module(’hello’, [])
.controller(’OlaCtrl’, function($scope) {
$scope.nome = ’World’;
});
AngularJSdefineonamespace angularglobal.Existemváriasfun çõesdeuti-
lidadeeconveniênciaexpostasnestenamespace,omóduloéumadessasfun ções.
Ummóduloatuacomoumcontêinerparaoutrosobjetosgerenciados(controllers,
serviçoseassimpordiante). Hámuitomaisaaprendersobreosmódulosdoque
namespacingsimpleseorganiza çãodecódigo.
Paradefinirumnovomódulo,precisamosforneceroseunomecomooprimeiro
argumentoparaachamadadefun çãomódulo.Osegundoargumentotornapossível
expressarumadependênciadeoutrosmódulos.
Achamadaparaafun ção angular.moduleretornaumainstânciadeummó-
dulorecém-criado.Assim,comonóstemosacessoaesteexemplo,podemoscome çar
adefinirnovoscontrollers.
Injeçãodedependências
O termo injeção de dependência foi cunhado por Martin Fowler (http://
martinfowler.com/articles/injection.html);emlinhasgerais,éumatécnicaparapro-
verdependênciasexternasaumdeterminadocomponentedesoftware.Temosalgu-
masvantagens:
1) Simplificaçãonocódigodaaplica ção: comainje çãodedependência,osobje-
tosdaaplica çãosãoliberadosdatarefadetrazersuasprópriasdependências–
66

## Página 75

CasadoCódigo Capítulo5. TornandoawebmaisdinâmicacomAngularJS
reduçãodecódigoparainicializa çãoeconfigura çãodedependências–,elesfi-
camlivresparaexecutarapenassuasregrasdenegócio,poissabemqueassuas
dependênciasestarãoláquandonecessárias.
2) Testabilidade: se as dependências podem ser injetadas em um componente,
torna-sepossível(etalvezatémaisfácil)injetarimplementa ções mocksdessas
dependências.
3) Baixoacoplamentoentreosobjetos:oobjetoconhecesuasdependênciasapenas
porsuainterfacepública–nãoporsuaimplementa ção,nemporcomoforam
instanciadas. Assim,adependênciapodesertrocadaporumaimplementa ção
diferente,semqueoobjetodependenteconhe çaadiferen ça.
4) Flexibilidadenogerenciamentodociclodevidadosobjetos:objetospodemser
cacheados,serum singletonouterumavidacurta–tudocontroladopormeiode
configuraçõese/oupelocontêiner.
Vejamosumexemplo:
function Filmes(sobreFilme) {
this.sobreFilme = sobreFilme;
}
Filmes.prototype.mudaNome = function(nome) {
this.sobreFilme.exibir(nome);
}
Repareque Filmesnãoestápreocupadocomalocaliza çãode sobreFilme:
elesimplesmenteéentreguea sobreFilmeemtempodeexecu ção.Issoédesejável,
mascolocaaresponsabilidadedeseapoderardadependênciasobreocódigoque
constrói Filmes.
Paragerenciararesponsabilidadedecria çãodedependência,cadaaplicativoAn-
gularJStemum injector.Oinjectoréumlocalizadordeservi çoqueéresponsávelpela
construçãoepesquisadedependências.
Umexemplodousodoservi çodo injector:
angular
.module(’MeusFilmes’, [])
.factory(’sobreFilme’, function($window) {
return {
67

## Página 76

5.3. Móduloseinjeçãodedependências CasadoCódigo
exibir: function(text) {
$window.alert(text);
}
};
});
var injector = angular.injector([’MeusFilmes’, ’ng’]);
var sobreFilme = injector.get(’sobreFilme’);
Requisitarasdependênciasresolveaquestãodacodifica çãodifícil,massigni-
ficatambémqueo injectorprecisaserpassadoemtodooaplicativo. Passaro
injectorquebraaLeideDemeter.Paracorrigirisso,transformamosaresponsa-
bilidadedepesquisadedependênciaparao injector,declarandoasdependências:
ALeideDemeterfoidescritapelaprimeiraveznaUniversidadeNortheastern,em
Boston,Massachusettsem1987.Naverdadeessa“Lei”forneceumconjuntode
orientaçõesúteisparaoprojetodesoftware.Quandoestasregrassãoseguidas,
reduzimosoacoplamento,descrevendocomoosmétodosepropriedadesdasclasses
devemsecomunicarentresi.AleiéporvezesconhecidacomooPrincípiodoMínimo
Conhecimento.
–JoséCarlosMacoratti
Porexemplo:
<div ng-controller="FilmesController">
<button ng-click="falaFilme()">Nome do Filme </button>
</div>
function FilmesController($scope, sobreFilme) {
$scope.falaFilme = function() {
sobreFilme.exibir(’Nome do filme é ...’ );
};
}
injector.instantiate(FilmesController);
Observequeofatodetero ng-controllerinstanciandoaclassefazcom
queelepossasatisfazertodasasdependênciasde FilmesController,semque
ocontrollerconhe çaoinjector. Esteéomelhorresultado. Ocódigodoaplicativo
simplesmentedeclaraasdependênciasqueprecisa,semterquelidarcomoinjector.
Estaconfigura çãonãoinfringeaLeideDemeter.
68

## Página 77

CasadoCódigo Capítulo5. TornandoawebmaisdinâmicacomAngularJS
5.4 ServiceAngular JS
Angularnosoferecediversosservi çosúteisparaqualqueraplica çãonãotrivialque
vocêvaiacharútilparaprópriosservi çospersonalizados.Parafazerisso,vocêdeve
começarporregistrarum servicefactorycomummódulodeservi ço,atravésdoMó-
dulo #factoryAPI oudiretamenteatravésda $provideAPI dentrodafun çãodecon-
figuraçãodomódulo.
Detodososservi çosangular,participardeinje çãodedependência(DI)por
sisóéregistrarcomosistemadeAngularDI(injector)sobumnome(id),bem
comodeclarandodependênciasqueprecisamserfornecidosparaafun çãodefá-
brica do serviçoregistrado. Acapacidadedetrocarasdependênciasdeobjetos
mocks/stubs/dummiesemtestespermitequeosservi çossejamaltamentetestáveis.
Serviçoscriadospelo $injectorsãosingletons.Haveráapenasumainstân-
ciadeumdeterminadoservi çoporinstânciadeumaplicativoemexecu ção.
RegistrandoService
Pararegistrarum service,vocêdeveterummódulodoqualesteservi çoiráfazer
parte.Depois,vocêpoderegistraroservi çocomomóduloatravésda APIModule
ouusandooservi ço $providenafun çãodeconfigura çãodomódulo.Oseguinte
pseudocódigomostraasduasabordagens:
U s a n d o a A P Iangular.Module:
var showMensagemModulo = angular.module(’showMensagemModulo’, []);
showMensagemModulo.factory(’serviceId’, function() {
var sumarioNovaInstancia;
return sumarioNovaInstancia;
});
Usandooservice $provide:
angular.module(’showMensagemModulo’, [], function($provide) {
$provide.factory(’serviceId’, function() {
var sumarioNovaInstancia;
return sumarioNovaInstancia;
});
});
69

## Página 78

5.4. ServiceAngularJS CasadoCódigo
Notequevocênãoestáregistrandoumainstânciadeservi ço,massimumafun-
ção factoryquevaicriaressainstânciaquandochamada.
Dependências
Serviçosnãosópodemserdependentes,mastambémpodetersuasprópriasde-
pendências.Estespodemserespecificadoscomoargumentosdafun ção factory.
Aseguir,vejaumexemplodeumservi çomuitosimples.Eledependedoservi ço
$window(queépassadocomoumparâmetroparaafun ção factory)eéapenas
umafun ção.Oservi çosimplesmentearmazenatodasasnotifica ções;apósaterceira,
eleexibetodasasnotifica çõesporalerta:
angular.module(’showMensagemModulo’, [], function($provide) {
$provide.factory(’notifica’, [ ’$window’, function(win) {
var msgs = [];
return function (msg) {
msgs.push(msg);
if (msgs.length == 3 ) {
win.alert(msgs.join("\n"));
msgs = [];
}
};
}]);
});
UmnovorecursodoAngularpermitedeterminaradependênciaapartirdo
nomedoparâmetro.Vamosreescreveroexemploanteriorparamostrarousodesta
injeçãoimplícitano $window, $scope,enossoservi çodenotifica ções.
angular.
module(’showMensagemModulo’, []).
factory(’notifica’, function($window) {
var msgs = [];
return function (msg) {
msgs.push(msg);
if (msgs.length == 3 ) {
$window.alert(msgs.join("\n"));
msgs = [];
}
};
});
70

## Página 79

CasadoCódigo Capítulo5. TornandoawebmaisdinâmicacomAngularJS
function showController($scope, notifica) {
$scope.notificarChamada = function(msg) {
notifica(msg);
};
}
<div id="implicit" ng-controller="showController">
<p>(Clique 3 vezes para ver um alerta) </p>
<input ng-init="mensagem=’test’" ng-model="mensagem">
<button ng-click="notificarChamada(mensagem);">
exibir notificação
</button>
</div>
Códigoonline: http://plnkr.co/edit/HG1iZBLIvnQnB0TtDEk9
Todososservi çosemAngularsãoinstanciados lazily.Issosignificaqueumser-
viçoserácriadosomentequandoeleénecessárioparaainstancia çãodeumservi ço
ouumcomponentedaaplica çãoquedependedele.Emoutraspalavras,Angularnão
vaiinstanciarservi ços,amenosquesejamsolicitadosdiretamenteouindiretamente
pelaaplica ção. Porúltimo,éimportanteperceberquetodososservi çosAngular
sãoaplica çõesúnicas,ouseja,háapenasumobjetodeumdeterminadoservi çopor
injector.
ComponentesdoMóduloAngular: http://docs.angularjs.org/api/ng
5.5 Comunicando com servidor back -end
Oservi ço $httpéumservi çocentralAngularquefacilitaacomunica çãocomos
servidoresHTTPremotosviaobjeto XMLHttpRequestdonavegadorouatravés
de JSONP.
O $httpAPI baseia-senasAPIs deferred/promiseexpostaspeloservice $q.En-
quantoqueparaospadrõesdeusosimplesissonãoimportamuito,parausoavan-
çadoéimportanteparasefamiliarizarcomessasAPIseasgarantiasqueoferecem.
U s o g e r a l
Oservi ço $httpéumafun çãoquerecebeumúnicoargumento–umobjeto
deconfigura ção–queéusadoparagerarumasolicita çãoHTTPeretornaumapro-
messacomdoismétodos $httpespecíficos.Sãoeles: successe error.
71

## Página 80

5.5. Comunicandocomservidorback-end CasadoCódigo
$http({method: ’GET’,
url: ’//api.twitter.com/1.1/search/tweets.json?q=angularjs’}).
success(function(data, status, headers, config) {
// Sucesso get
data // Retorno do objeto feita pela requisição
}).
error(function(data, status, headers, config) {
// Sucesso get
});
Umavezqueovalorretornadodafun ção $httpéumapromise,vocêtambém
podeusarométododepoisderegistrarretornosdechamada. Eessesretornosde
chamadareceberãoumúnicoargumento–umobjetoquerepresentaaresposta.
Umcódigodestatusderespostaentre200e299éconsideradoumstatusde
sucessoeresultaránoretornosucessosendochamado. Note-seque,searesposta
forumredirecionamento, XMLHttpRequestvaisegui-lodeformatransparente,o
quesignificaqueoretornodeerronãoseráchamadoparataisrespostas.
Métodoscurtos
T o d a s a s i n v o c açõesaoservi ço $httpexigemummétodoHTTPeaURLaser
chamada.Parasimplificar,foramcriadosmétodosdeatalhodiretocomonomedo
métodoHTTP,como gete post:
$http.get(’//api.twitter.com/1.1/search/tweets.json?q=angularjs’)
.success(successCallback);
$http.post(’//api.twitter.com/1.1/search/tweets.json?q=angularjs’, data)
.success(successCallback);
Vejaumexemplorealderequest $http:
<body ng-controller="PessoasCtrl">
<p ng-repeat="dados in pessoas" >
Oi, meu nome é <strong>{{ dados.nome }} </strong>
tenho <strong>{{ dados.idade }} </strong> anos de idade,
moro em <strong>{{ dados.cidade }} </strong>!
</p>
</body>
var app = angular.module(’plunker’, []);
72

## Página 81

CasadoCódigo Capítulo5. TornandoawebmaisdinâmicacomAngularJS
app.controller(’PessoasCtrl’, function($scope, $http) {
$http.get(’dados.json’).success(function(data) {
$scope.pessoas = data;
});
});
[
{
"idade": 23,
"cidade": "Belo Horizonte" ,
"nome": "Giovanni Keppelen"
},
{
"idade": 25,
"cidade": "Rio de Janeiro" ,
"nome": "Keppelen"
}
]
Códigoonline: http://plnkr.co/edit/aHxoFbhGoATluQNrqfRJ?p=preview
Paraestudos,osoutrosmétodosdoAngularparaAjax:
1) $http.get=>http://docs.angularjs.org/api/ng/service/ $http#get
2) $http.head=>http://docs.angularjs.org/api/ng/service/ $http#head
3) $http.post=>http://docs.angularjs.org/api/ng/service/ $http#post
4) $http.put=>http://docs.angularjs.org/api/ng/service/ $http#put
5) $http.delete=>http://docs.angularjs.org/api/ng/service/ $http#delete
6) $http.jsonp=>http://docs.angularjs.org/api/ng/service/ $http#jsonp
5.6 $r o u t eAngular Js
AngularJStemum $route service,quepodeserconfiguradoparalidarcom
transiçõesderotasemaplica çõeswebdeumaúnicapágina.Abrangetodasascarac-
terísticasdo $locatione,adicionalmente,ofereceoutrasfacilidadesmuitoúteis.
O serviço $location analisa a URL do navegador (com base no
window.location)efazaURLdisponívelparasuaaplica ção. Mudançasna
73

## Página 82

5.6. $routeAngularJs CasadoCódigo
URLsãorefletidasnoservi ço $locationeasaltera çõesem $locationsão
refletidasnabarradeendere ços.
Apartirdaversão1.2,oAngularJSteveseusistemaderoteamentoentregue
emumarquivoseparado( angular-route.js) com o seu próprio módulo (
ngRoute). Lembre-sedeincluiroarquivo -angular route.jsedeclararuma
dependêncianomódulo ngRoute.
Rotasbásicas
Em AngularJS, rotas podem ser definidas durante a configuração do apli-
cativo usando o serviço $routeProvider. A sintaxe usada pelo serviço
$routeProviderésemelhanteausadacom $locationpersonalizado.Vejaum
exemplo:
angular.module(’ExemploNgRoute’, [ ’ngRoute’])
.config(function($routeProvider, $locationProvider) {
$routeProvider.when(’/livro/:livroId’, {
templateUrl: ’livro.html’,
controller: LivroCtrl,
resolve: {
delay: function($q, $timeout) {
var delay = $q.defer();
$timeout(delay.resolve, 1000);
return delay.promise;
}
}
});
$routeProvider.when(’/livro/:livroId/ch/:capituloId’, {
templateUrl: ’capitulo.html’,
controller: CapituloCtrl
});
$locationProvider.html5Mode(true);
});
Oservi ço $routeProviderexpõeumaAPIdeestilofluente,naqualpassamos
ométodoqueencadeiachamadasparaadefini çãodenovasrotasedacria çãodeuma
rotadefault.
7 4

## Página 83

CasadoCódigo Capítulo5. TornandoawebmaisdinâmicacomAngularJS
Umaveziniciado,opedidonãopodeserreconfiguradoparasuportarrotasadi-
cionais(ouremoverasjáexistentes). Issoestáligadoaofatodequeosproviders
Angularpodemserinjetadosemanipuladossomenteemblocosdeconfigura ção
executadosduranteinicializa çãodoaplicativo.
Noexemploanterior,vocêpodeverque TemplateUrleraaúnicapropriedade
paracadarota,masasintaxeoferecidapeloservi ço $routeProviderémuitomais
rica.
Oconteúdodeumarotapodetambémserespecificadaemlinhausandoapro-
priedademodelodeumobjetodedefini çãoderota.Emboraestasejaumasintaxe
suportada,codificarmarca çãodarotaemsuadefini çãonãoémuitoflexível(nem
sustentável),porissoraramenteéutilizadanaprática.
Exemplomaiscompletode $route:
Index.html
<div ng-app="ExemploNgRoute">
<div ng-controller="MeusLivrosCtrl" class="tabs">
<a href="Livro/Angular">Angular</a>
<a href="Livro/Angular/ch/1">Angular: Ch1 </a>
<a href="Livro/jQuery">jQuery</a>
<a href="Livro/jQuery/ch/4?key=value">jQuery: Ch4 </a>
<a href="Livro/VanilhaJS">VanilhaJS</a><br/>
<div ng-view></div>
<hr />
<pre>$location.path() = {{$location.path()}} </pre>
<pre>$route.current.templateUrl = {{$route.current.templateUrl}} </pre>
<pre>$route.current.params = {{$route.current.params}} </pre>
<pre>$route.current.scope.name = {{$route.current.scope.name}} </pre>
<pre>$routeParams = {{$routeParams}} </pre>
</div>
</div>
livro.html
controller: {{nome}} <br />
Livro Id: {{params.livroId}} <br />
capitulo.html
75

## Página 84

5.6. $routeAngularJs CasadoCódigo
controller: {{name}} <br />
Livro Id: {{params.bookId}} <br />
Capitulo Id: {{params.chapterId}}
script.js
angular.module(’ExemploNgRoute’, [ ’ngRoute’])
.config(function($routeProvider, $locationProvider) {
$routeProvider.when(’/Livro/:livroId’, {
templateUrl: ’livro.html’,
controller: livroCtrl,
resolve: {
// Com 1 segundo de atraso
delay: function($q, $timeout) {
var delay = $q.defer();
$timeout(delay.resolve, 1000);
return delay.promise;
}
}
});
$routeProvider.when(’/Livro/:livroId/ch/:capituloId’, {
templateUrl: ’capitulo.html’,
controller: capituloCtrl
});
// Para configurar os inks dentro do plunker
$locationProvider.html5Mode(true);
});
function MeusLivrosCtrl($scope, $route, $routeParams, $location) {
$scope.$route = $route;
$scope.$location = $location;
$scope.$routeParams = $routeParams;
}
function livroCtrl($scope, $routeParams) {
$scope.nome = "livroCtrl";
$scope.params = $routeParams;
}
function capituloCtrl($scope, $routeParams) {
$scope.nome = "capituloCtrl";
76

## Página 85

CasadoCódigo Capítulo5. TornandoawebmaisdinâmicacomAngularJS
$scope.params = $routeParams;
}
Códigoonline: http://embed.plnkr.co/8zNXCmheCPCsnxqr78YH/preview
5.7 Conclusão
Comunidade
Todossabemqueprojetonenhumvaiparafrentesenãotempessoasportrás. E
AngularJSéopensource,apesardetertodoumtimedoGoogletrabalhandodiari-
amentenele.Hátambémumacomunidademuitograndeecommuitasop çõesde
aprendizado:
1) angular@googlegroups.com(ListaemailnoGoogle)
2) https://plus.google.com/u/0/communities/115368820700870330756 (Comuni-
dadenoGoogle+)
3)http://stackoverflow.com(starckoverflow)
4) https://www.facebook.com/groups/angularjsbrasil/(ComunidadeFacebook)
5)http://ng-learn.org/
6) #angularjsIRCchannel
Recursoonline
AngularJStemseuprópriowebsite( http://www.angularjs.org),ondepodemos
encontrartudo,absolutamentetudooqueprecisar:visãogeralconceitual,tutoriais,
guiadodesenvolvedor,referênciadaAPI,eassimpordiante.Ocódigo-fontepara
todasasversõesAngularJSliberadospodeserbaixadoem http://code.angularjs.org.
Aspessoasqueprocuramexemplosdecódigonãoirãosedecepcionar,poiso
AngularJStemsuaprópriadocumenta çãoetembastantetrechosdecódigo.Alémde
tudoisso,pode-senavegaremumagaleriadeaplica çõesconstruídascomAngularJS
(http://builtwith.angularjs.org).UmcanaldoYouTubededicadoaissoé http://www.
youtube.com/user/angularjs.
77

## Página 86

5.7. Conclusão CasadoCódigo
Depoimentos
“Nóstínhamosacabadodelançarume-commerce,quepoucosmesesdepoissetornou
osegundomaiordoramoesportivodaAméricaLatina.UsamosjQueryeuma
centenadeplugins.Ocódigo?EraumasopadeseletoresjQuery,eventhandlerse
callbacks.Darmanuten ção,ouseja,mudarocódigoerarealmenteumsofrimento.
Decidimosreescreveraaplica çãousandooAngularJS,bemantesdohype,pela
testabilidadedoJavaScript.Alémderefazeraaplica çãointeiraemapenas2semanas
(contandocomareescritadetodooCSS),oresultadofoiumcódigofácildemudar,
fácildesetrabalharemequipeefácildeentender.Eomelhordetudo,aprendemos
boaspráticasdeDesenvolvimentodeSoftware,gra çasaoDesigndoframework”
–CiroNunes(Front-endEngineerAvenueCode)
Obrigado
AnglarJStemmuitomaispotencialdoquemostreiavocês. Oqueescrevifoi
apenasoverviewdoqueAngularJSécapaz. Poderiaescreverpáginasemaispági-
nassobrecoisaslegaisefuncionalidadessobreele. Acreditoquepudetirarmuitas
dúvidasdequemnãooconheciaoutinhaumbreveconhecimentosobreAngularJS.
Obrigadopelacompanhiadetodoseesperoquetenhamgostado.
78

## Página 87

CasadoCódigo Capítulo5. TornandoawebmaisdinâmicacomAngularJS
Sobre o autor
GiovanniKeppelenéCTOnaPlanedia,plataformaonlineparaplane-
jareplanificarsuaviagem.CofundadordaBrazilJSFoundation,ideali-
zadoreorganizadordoFrontinBHeRio.JS.UmdosautoresdoBrowser
Diet,comZenoRocha,SérgioLopes,MarcelDuram(Twitter),Renato
Mangini(Google)entreoutrosgrandesnomes.TrabalhoucomoFront-
endEngineernoPeixeUrbanoecoordenadorFront-endnaMobicareà
frentedegrandesprojetos.CursandoProdu çãoMultimídianoUNI-BH.
79

## Página 89

Capítulo6
Asdiretrizesdeacessibilidadepara
conteúdonaWeb–WCAG
6.1 Acessibilidade naWeb
AcessibilidadenaWebsignificagarantirquepessoascomdeficiênciadevempoder
usar,acessarecompreenderoqueépublicadonaWeb.Considerarousodediretrizes
internacionaisdeacessibilidadebeneficiaumgrandegrupodepessoas:
• pessoascegas,queutilizamumsoftwareleitordetelaparaacessaroconteúdo
deumapágina;
• pessoascombaixavisão,quenecessitamdecontrasteefontesmaiores;
• pessoasdaltônicasquenãoenxergamumdeterminadotipodecor;
• pessoassurdasquenãoconseguemescutarumáudionaWeb;

## Página 90

6.2. PortrásdoWCAG2.0 CasadoCódigo
• pessoascommobilidadereduzidaqueutilizamumdedo(ounemisso)para
acessaroconteúdodeumapáginaWeb.
Porém,acessibilidadenaWebvaimuitoalémdebeneficiarsomentepessoascom
deficiências.Usuáriosdedispositivosmóveis,pessoascomdeficiênciatemporáriae
usuáriosidosossãoapenasalgunsdosdiversosexemplosdeusuáriosquepodemter
seuacessoaWebprejudicadoseaspáginasnãoforemacessíveis.
SegundooCensodoIBGEde2010,oBrasilcontacomaproximadamente24%
dapopula çãocomalgumtipodedeficiência.Sãomaisde45milhõesdepessoasque
podemteralgumabarreiradeacessocasoaspáginasnãosejamprojetadasdeforma
aatendertodasaspessoas.Oprincípiododesenhouniversaléfundamentalparaque
todostenhamacessoplenoaoconteúdodisponívelnaWeb.Paraissoforamcriadas
asDiretrizesInternacionaisdeAcessibilidadenaWeb.
Dados do censo do IBGE
Ocensode2010trazdadosinteressantíssimossobreacessibilidadee
deficiência:
http://censo2010.ibge.gov.br/noticias-censo?busca=1&id=
3&idnoticia=2170&view=noticia
6.2 Por trás do WCAG2.0
AWebnasceuparaseracessível.Em1997,TimBerners-Leeanunciavaolan çamento
doInternationalProgramOffice (IPO)paraaIniciativadeAcessibilidadenaWeb–
W A I (http://www.w3.org/WAI/)comoobjetivodepromoveregarantirofunciona-
mentodaWebparapessoascomdeficiências.Duranteseulan çamento,ocriadorda
Webdeclarou:
“OpoderdaWebestáemsuauniversalidade.Acessoportodos,independentemente
dadeficiência,éumaspectoessencial”
–TimBerners-Leeem http://www.w3.org/Press/IPO-announce
Esseprogramaalavancoudiversasiniciativaseprojetosrelacionadosàacessibi-
lidadenaWeb. Umdosmaisimportantesfoiacria çãodasDiretrizesdeAcessibi-
lidadeparaConteúdonaWeb–asWCAG1.0( http://www.w3.org/TR/WCAG10/)
82

## Página 91

CasadoCódigo Capítulo6. AsdiretrizesdeacessibilidadeparaconteúdonaWeb–WCAG
,publicadascomorecomenda çãodoW3Cnodia5demaioem1999,comoobje-
tivodeorientarcomotornaroconteúdoacessívelparapessoascomdeficiências.O
documentotemumaótimaintrodu ção,queexplicaque,alémdepromoveraacessi-
bilidadeparapessoascomdeficiências,seguirasdiretrizesbeneficiatodasaspessoas
emdiferentessitua ções,comoacessarumapáginacomilumina çãofraca,ouemum
ambientecommuitobarulhooucomasmãosocupadas.
Noveanosdepois,comaWebemamplaevolu ção,aWAIlan çaasegundaversão
dasDiretrizesdeAcessibilidade,asWCAG2.0( http://www.w3.org/TR/WCAG/).
Baseadasnaprimeiraversãodarecomenda ção,odocumentomudasuaestruturae
ampliaasformasetécnicasparatornaroconteúdoacessível.
Anovaversãodarecomenda çãoestáorganizadadaseguinteforma:
•Princípios–sãoquatroprincípiosquefornecemabaseparaaacessibilidade
daWeb:perceptível,operável,compreensívelerobusto.
•Diretrizes–as12diretrizessobosprincípiosfornecemosobjetivosbásicos
quedevemsertrabalhadosparaqueoconteúdonaWebsejaacessívelàspes-
soascomdeficiências.
•Critériosdesucesso –paracadadiretriz,existemcritériosdesucessopara
atingiroobjetivodecumprirasdiretrizesegarantirqueasWCAG2.0se-
jamefetivamenteusadasemespecifica çõesdeprojetosemgeral,comotestes
deconformidadeetc.Oscritériosdesucessosãodivididosemtrêsníveisde
conformidade:A(maisbaixo),AA,AAAe(maisalto).
•Técnicasdetiposuficienteeaconselhadas –paracadaumadasdiretrizese
critériosdesucessonodocumentoWCAG2.0,existeumagrandevariedade
detécnicas.Astécnicassãodivididasemduascategorias:suficienteeaconse-
lhadas.
Técnicassuficientesgarantemocumprimentodoscritériosdesucesso,apon-
tandodocumenta çãotécnicanecessáriaparaatingirosobjetivos.Jáastécni-
casaconselhadasvãoalémdoqueéexigidonastécnicassuficienteeabrangem
umaamplagamadebarreirasdeacessibilidadequepodemnãoserabordadas
pelastécnicassuficientes.
OobjetivodesteartigoéapresentarosquatroprincípiosdasWCAG2.0,boa
partedasdiretrizesequaisastécnicasparamelhoraraacessibilidadedoseuprojeto
Web.Nãovoupassardetalhadamenteporcadaumadelas,masgostariadeexplicar,
83

## Página 92

6.3. Princípio1:perceptível CasadoCódigo
pelomenosboapartedosprincipaiscritériosdesucessorelacionadosnonívelAde
formasimplesedescomplicada.Boapartedosexemplosdecódigoforambaseados
emexemplosdaprópriadocumenta çãodoW3C.
Éimportanteressaltarqueapenasseguiroqueesteartigoorientanãogaranteque
suapáginasejatotalmenteacessível.Aprincipalrazãodedescreveradocumenta ção
doW3Cdestaformaétornarmaisfácilacompreensãoequebradebarreirasmais
comunsparamelhoraraacessibilidadedaspáginasWeb.Vocêvainotarquealgumas
técnicasnãoestãorelacionadasadesenvolvimentodecódigo,masemboaspráticas
ealternativasparatornaroconteúdodaWebacessívelatodos.
6.3 Princípio1: perceptível
Ainforma çãoeoscomponentesdainterfacedousuáriotêmdeserapresentadosaos
usuáriosemformasqueelespossamperceber.
Oqueissosignifica? Queosusuáriosdevemsercapazesdeperceberainfor-
maçãoqueestásendoapresentada,nãopodendoserinvisívelparatodososseus
sentidos.
Diretriz1.1–alternativasemtexto
Todooconteúdonãotextualdeveforneceralternativasemtexto. Assim,ele
podesertransformadoconformeanecessidadedousuário,comoemfontesmaiores,
braile,sonsetc.Essadiretrizabrangeumaamplagamadesitua ções:
1.1.1Conteúdonãotextual
Quandooconteúdonãotextualéapresentadoaousuário,eledeveterumaalter-
nativaemtextoqueserveparaafinalidadeequivalente.Essecritériodesucessonão
seaplicaàsseguintessitua ções:controlesdeformulário,mídiabaseadaemtempo,
testes,experiênciassensoriais,captchaeimagensdecorativas.
Sãodefinidasalgumassitua çõesdeuso:
SituaçãoA –adescriçãocurtaserveaomesmopropósitoeapresentaamesma
informaçãodoconteúdonãotextual.
Exemplo:umdocumentoHTMLcomumafotodaestátuadoCristoRedentor.
Considerandoqueesseelementonãotextualéumafoto,aformaparasolucionar
essasitua çãoésimples.Bastautilizarumelementodeimagemcomoatributo alt
preenchidodeformaadequada:
84

## Página 93

CasadoCódigo Capítulo6. AsdiretrizesdeacessibilidadeparaconteúdonaWeb–WCAG
<img src="foto.png" alt="Foto do Cristo Redentor" >
Comisso,vocêgarantequetecnologiasassistivasconsigamlerosignificadoda
imagempeloseutextoalternativo.
Apartedifícilnãoécolocaroatributo altnasimagensesim,comodescrevê-la.
Adocumenta çãosugerefazerasseguintesperguntasparaentenderanecessidadee
oquedescrevernoatributo alt.
• Porqueesteconteúdonãotextualestáaqui?
• Quaisasinformaçõessãoapresentadas?
• Qualoobjetivoeledevecumprir?
• Seeunãopuderusaroconteúdonãotextual,quepalavraseuiriausarpara
transmitiramesmafun çãoe/ouinforma ção?
Éimportanteressaltarque,alémdetecnologiasassistivas,ferramentasdebusca
indexamainforma çãodentrodoatributo alt.
SituaçãoB –adescriçãocurtanãoserveaomesmopropósitoeapresentaa
mesmainforma çãodoconteúdonãotextual.
Exemplo:umgráficooudiagramadetalhado.
Nessecaso,asWCAGrecomendam,alémdeumtextoalternativocurtoexpli-
candobrevementeográficooudiagrama,duaspossibilidades:colocarumlinkpró-
ximoàimagemqueváparaumapáginaouarquivocomadescri çãocompletaou
colocarumtextonaprópriapágina,próximoaográficooudiagrama,queexplica
detalhadamenteimagem.
Essatécnicagarantequeumaimagemoudiagramatenhaseuconteúdoconver-
tidoemmodotexto.Assim,ferramentasdebusca,navegadoresetecnologiasassis-
tivaspodemacessarasinforma çõesdeformaplena.
SituaçãoC –oelementonãotextualéumcampodeformulário.
Umcampodeformulárionãotemumaalternativaemtexto,mastemrótulos
quedefinemseupropósitoeotipodedadoquedeveserinserido. Nessecaso,a
recomendaçãoéfazerarela çãoadequadadosatributosIDsdosformulárioscom
seusrespectivosrótulos,utilizandooelemento <label>.
<label for="email">E-mail</label>
<input type="text" name="email" id="email">
85

## Página 94

6.3. Princípio1:perceptível CasadoCódigo
Senãoforpossívelutilizaroelemento label,utilizeoatributo titlepara
identificaroscamposdeformulário.
<input id="area" name="area" title="Código de área" type="text">
<input id="primeiros" name="primeiros" type="text"
title="Primeiros quarto dígitos do número do telefone" >
<input id="ultimos" name="ultimos" type="text"
title="Últimos quarto dígitos do número de telefone" >
Utilizeestatécnicasomentesenãoforpossívelusaroelemento labelnoscam-
posdoformulário.
Nocasodebotõescom <input type="img">,utilizeoatributo altpara
indicaraa çãoaserfeita;porexemplo, alt="enviar formulário".
Essa técnica garante que tecnologias assistivas possam relacionar adequada-
menteosrespectivostextoscomseucampodeformulário. Alémdamelhoriana
acessibilidade,oformuláriotemumganhoenormeemusabilidade,jáquecampos
radioboxecheckboxquerelacionam labelcomIDstornamotextodorótuloum
objetoselecionável,nãosendomaisnecessárioclicarsomentenoquadrado/bolinha
docampo.Otextotambémacionaocampo.
SituaçãoD –oelementonãotextualéumamídiabaseadaemtempo.
Adescri çãodetalhadaseráfeitanadiretriz1.2.
SituaçãoE –oelementonãotextualéumCAPTCHA.
CAPTCHAéaabrevia çãode CompletelyAutomatedPublicTuringtesttotell
ComputersandHumansApart querepresentaumdesafio,normalmenteemimagem,
paraevitarquerobôspreenchamautomaticamenteumformulário. Oproblemaé
queessasimagenssãoinacessíveisparausuárioscegos,quenavegamcomsoftwares
leitoresdetela.CasosejainevitávelousodoCAPTCHA,arecomenda çãoéutilizar
umtextocurtoparadescrevê-loeutilizaroutramodalidadedeCAPTCHAquenão
sejainvisívelparaousuário.Porexemplo,usarumCAPTCHAcomalternativaem
áudio,ouutilizarperguntassimples,emmodotextonapágina.
SituaçãoF –oelementonãotextualdeveserignoradopelastecnologiasassis-
tivas. Casooelementonãotextualdevaserignoradopelastecnologiasassistivas,
comoumaimagemdecorativa,eladeveserinseridadentrodasCSS.
<style>
body {
background: #ffe url(’/images/home-bg.jpg’) repeat;
}
</style>
86

## Página 95

CasadoCódigo Capítulo6. AsdiretrizesdeacessibilidadeparaconteúdonaWeb–WCAG
Diretriz1.2–mídiascombaseemtempo
Garantirquepessoascomdeficiênciatenhamacessoaelementosdemídia,como
áudioevídeoéoobjetivodestadiretriz.Paraáudioevídeopré-gravado,oscritérios
desucessoparaatenderaessadiretrizsãoosseguintes:
1.2.1Apenasáudioeapenasvídeo
Paraáudioevídeopré-gravadosnaWeb,ofere çaumaalternativaparaessetipo
demídia,comoatranscri çãodoáudio/vídeoemumdocumentotextoououtrapá-
ginaWeb.Essatécnicabeneficiapessoasquenãoconseguemouvirumáudionaweb
etambémoferecemaisconteúdoaserindexadoporferramentasdebusca.
1.2.2Legendas(pré-gravadas)
Adocumenta çãodoWCAGorientaafornecerlegendasparaconteúdogravado,
noformato opencaption(sempredisponível)ou closedcaption(queousuáriopode
habilitarounão).AsWCAGnãoorientamsobreumformatoespecíficodelegendas,
masmostramdiversasop çõesdetecnologiasquepossibilitamessaa ção.
1.2.3Audiodescriçãooumídiaalternativa(pré-gravada)
Audiodescriçãoéumatrilhadeáudioqueforneceinforma çõesquecompreen-
demosvisualmenteequenãoestãocontidasemdiálogosdeumvídeo.Aaudiodes-
criçãotemumimpactoenormeemquemassisteaumvídeo,masnãoconseguevero
queéexibido.NoBrasil,oscanaisdeTVabertasãoobrigadosaexibirduashorasde
programaçãosemanalcomaudiodescri ção.Fa çaumtesteeassistaaumfilmecom
esserecursoepercebaoquantoeleéimportanteparaquemnãoenxergaoqueestá
sendoexibido.
Diretriz1.3–adaptável
Estadiretrizorientaodesenvolvedoracriarconteúdosquepossamseradaptados
ouapresentadosemdiferentesformas(comoemumlayoutmaissimples)semque
elepercasuaestruturaouinforma çãocontidanele.
1.3.1Informaçõeserela ções
Éprecisogarantirqueasinforma ções,aestruturaeasrela çõesquesãotransmi-
tidasatravésdapáginaoudaaplica çãoWebestejamdisponíveisdeformaprogra-
87

## Página 96

6.3. Princípio1:perceptível CasadoCódigo
máticaouestejamdisponíveisnotexto.Algunsexemplosparailustraressecritério
são:
• Umformuláriocomcamposobrigatóriosmarcadosadequadamente;
• Umformulárioqueusacoretextoparamarcarcamposobrigatórios;
• Umatabeladehoráriodeônibusquetemseuscabe çalhosdefinidosprogra-
maticamente.
Existemdiversastécnicasquevãodeencontroaessaorienta ção.Algumasdelas
sãoasseguintes:
Utilizeelementossemânticosparamarcaraestrutura.
Aregraaquiégarantirqueoselementostenhamsuasemânticacorretaapresen-
tada.Asemânticafacilitaousodetecnologiasassistivas,poisagrandemaioriados
usuáriosutilizaatalhosdetecladoparanavegar.Dessaforma,ficamaisfácilnavegar
porcabe çalhos,tabelas,formuláriosetc.
Utilizartabelasparamarcarconteúdotabular.
Historicamente,tabelasforamutilizadasparaacria çãodelayoutdepáginas.Essa
técnicaédesencorajada,poiscausaproblemasausuáriosdetecnologiasassistivas.
Paraaexibi çãodedadostabulares,queérealmentesuafun ção,existemalgumas
orientações:
UtilizaroelementoCAPTIONparaotítulodatabela.
Émaissemânticoutilizaroelemento captionqueestádentrodatabela,pois
assimousuárionãoprecisasaireprocurarotítuloreferenteaela.Utilizeoelemento
daseguinteforma:
<table>
<caption>Agenda da semana </caption>
...
</table>
Oelemento captionpodeterseuposicionamentoeformata çãomodificados
porCSS.
Utilizeoatributo scopeparaclassificarlinhasecolunasdetabelascomplexas.
Utilizeosvalores row, col, rowgroupe colgroup.Issofacilitaaorienta çãode
tecnologiasassistivasdentrodeumatabela.
88

## Página 97

CasadoCódigo Capítulo6. AsdiretrizesdeacessibilidadeparaconteúdonaWeb–WCAG
<table border="1">
<caption>Dados de contato </caption>
<tr>
<td></td>
<th scope="col">Nome</th>
<th scope="col">Telefone</th>
<th scope="col">Fax</th>
<th scope="col">Cidade</th>
</tr><tr>
<td>1.</td>
<th scope="row">João dos Santos </th>
<td>999-999-9999</td>
<td>999-999-9999</td>
<td>Belo Horizonte </td>
</tr><tr>
<td>2.</td>
<th scope="row">Carla Pereira </th>
<td>999-999-9999</td>
<td>999-999-9999</td>
<td>São Paulo </td>
</tr><tr>
<td>3.</td>
<th scope="row">Maria Souza </th>
<td>999-999-9999</td>
<td>999-999-9999</td>
<td>Rio de Janeiro </td>
</tr>
</table>
Paratabelasmaiscomplexas,épossívelutilizarIdseHeadersparaumarela ção
melhorentresuascélulas,masarecomenda çãomaisimportanteédeixarastabelas
simples. Émuitomaisfácilcompreenderosdadosquandoastabelassãodefácil
leitura.
Tabelas comIds eHeaders
Casotenhainteressenessatécnica,leia "Usingidandheadersattribu-
testoassociatedatacellswithheadercellsindatatables” ,disponívelem
http://www.w3.org/TR/2013/NOTE-WCAG20-TECHS-20130905/H43
89

## Página 98

6.3. Princípio1:perceptível CasadoCódigo
UtilizeaH1-H6paraestruturarcabe çalhos.
Essatécnicagarantequeasemânticadoscabe çalhossejapreservadaequeusuá-
riosdetecnologiasassistivasconsigamnavegarporeles. AsWCAGsugeremdois
exemplosdeabordagem:
Organizaçãohierárquicadecabe çalhos:
<h1>Produtos em destaque <h1>
...
<h2>Eletrônicos</h2>
...
<h3>Televisores</h3>
...
<h2>Alimentação</h3>
...
<h3>Frutas</h3>
Cabeçahosemlayout:
<head>
<title>Mercado de ações hoje </title>
</head>
<body>
<!-- left nav -->
<div class="left-nav">
<h2>Navegação</h2>
<!-- content here -->
</div>
<!-- main contents -->
<div class="main">
<h1>Mercado de ações hoje </h1>
<!-- article text here -->
</div>
<!-- right panel -->
<div class="left-nav">
<h2>Links relacionados </h2>
<!-- content here -->
</div>
</body>
90

## Página 99

CasadoCódigo Capítulo6. AsdiretrizesdeacessibilidadeparaconteúdonaWeb–WCAG
Éimportanteressaltarqueesseexemplodecódigonãoéumaregradecomoes-
truturarcabe çalhosdentrodeumlayoutdepágina.Cadadesenvolvedorpodeestru-
turardaformaqueacharmelhor,desdequesigaalógicaeocritériodeimportância
decadaníveldecabe çalho.
Forneçadescri çãoadequadaparagruposdeformuláriosutilizandoosele-
mentosLEGENDeFIELDSET.
Érecomendávelagruparblocosdeformulárioconformeotipodedadosolici-
tado. Muitasvezes,aspáginascomformuláriospedemdadospessoais,dadosco-
merciaisetc.Paraevitarqueumcampo nomeoutelefoneapareçaduasvezessemsua
devidamarca çãodegrupo,utilizeoelemento fieldsetparaagruparosblocose
oelemento legendparadeclararotítuloadequadodaquelegrupo.
<fieldset>
<legend>Dados pessoais </legend>
<label for="nome">Nome</label>
<input type="text" name="nome" id="nome">
<label for="end">Endereço</label>
<input type="text" name="end" id="end">
...
</fieldset>
<fieldset>
<legend>Dados Comerciais </legend>
<label for="nome-com">Nome da empresa </label>
<input type="text" name="nome-com" id="nome-com">
<label for="end-com">Endereço</label>
<input type="text" name="end-com" id="end-com">
...
</fieldset>
1.3.2Sequênciacomsignificado
Ofereceraousuárioumasequênciadeleituracorretacasoasequênciadocon-
teúdoafeteseusignificado. Issoémuitocomumquandotemosumapáginacom
múltiplascolunasouquandoacessamoswebsitesdeoutrosidiomas,cujasequência
deleituraédadireitaparaaesquerda.Nessecaso,alémdeordenaroconteúdode
formaestruturada,utilizaratributosqueprogramaticamenteorientealeituraade-
quadadoconteúdoérecomendável,comooRLM(right-to-leftmark)eLMR(left-
to-rightmark).
91

## Página 100

6.4. Princípio2:operável CasadoCódigo
1.3.3Característicassensoriais
Nãofazerumconteúdoquedependaexclusivamentedecaracterísticassensoriais
dosseuscomponentes,comoforma,tamanho,localiza çãovisual,orienta çãoousom.
Oexemplodousodacor(critériodesucesso1.4.1)servecomoorienta çãobásicapara
estecritériodesucesso.
Diretriz1.4–discernível
Facilitaraaudi çãoevisualiza çãodeconteúdosaosusuários.Tornaraexperiência
dousuáriomaissimplesedefácilcompreensãoéamelhorformadegarantirquea
informaçãodapáginasejatransmitidadeformaadequada.
1.4.1UtilizaçãodaCor
Adocumenta çãodoWCAGéenfáticanessesentido:Nuncautilizesomenteacor
paratransmitirinforma çãoaoseuusuário.Pessoascomalgumtipodedaltonismo
eusuáriosquenãoenxergampodemterdificuldadesemutilizarumwebsiteque
orientesuasa çõessomenteporcores. Porexemplo,emumatabelaqueinforma
queostatusverdesignifica“emandamento”evermelho“parado”. Seutilizarmos
somenteacorparainformarostatus,pessoascomalgumtipodedaltonismopodem
nãocompreenderatabela.
Comrela çãoaocontrasteadequadoentreoconteúdoeofundo,oW3Corienta
queelesejadenomínimo4,5:1excetoparatextosampliados(quedevemterum
contrastemínimode3:1),textosdecorativoselogotiposquenãotêmrequisitode
contraste.
1.4.2Controledeáudio
SeumsomemumapáginaWebcome çaratocarautomaticamente(áudioou
vídeo)durantemaisde3segundos,deveestardisponívelummecanismoparafazer
umapausaoupararosomevídeo,oudevedisponibilizarummecanismoparacon-
trolarovolumedosom,independentementedetodooníveldevolumedosistema.
6.4 P rincípio2: operável
Oscomponentesdeinterfacedeusuárioeanavega çãotêmdeseroperáveis.
Oqueissosignifica?Queosusuáriosdevemsercapazesdeoperarainterface;a
interfacedeintera çãonãopodeexigirintera çãoqueousuárionãopossaexecutar.
92

## Página 101

CasadoCódigo Capítulo6. AsdiretrizesdeacessibilidadeparaconteúdonaWeb–WCAG
Diretriz2.1–acessívelviateclado
Todaafuncionalidadedasuapáginadeveseracessívelporteclado,garantindo
quenãoexistambarreirasdeacessoausuáriosquenãopossamutilizarummouse,
porexemplo.
2.1.1Teclado
Estecritériodesucessodefinequetodaafuncionalidadedeveestaracessívelvia
teclado.Paraqueessecritériosejacumprido,existemalgumastécnicasqueauxiliam
odesenvolvimento.
Alémdeutilizaroslinks(âncoras)doHTML,que,porpadrão,jágarantemofoco
viateclado,utilizarfun çõesdefocoemconjuntocomfun çõesdepassaromouse
ajudaagarantirqueofocoviatecladosejafeito. NocasodeusodeJavaScript,o
exemploaseguiréválido:
<a href="menu.php"
onmouseover="swapImageOn(’menu’)"
onfocus="swapImageOn(’menu’)"
onmouseout="swapImageOff(’menu’)"
onblur="swapImageOff(’menu’)">
<img id="menu" src="menu_off.gif" alt="Menu">
</a>
Utilizeoevento onfocusemconjuntocom onmouseover.Omesmoseaplica
parafun çõesde“tiraromouse”.
E,emCSS,aregraéamesma.
a:hover,
a:focus {
background-color:#FFF;
}
2.1.2Sembloqueiodoteclado
Damesmaformaqueteroconteúdoacessívelviatecladoéimportante,ode-
senvolvedordeveevitarbarreirasdetecladoparaousuário. Duranteanavega ção
viateclado,ousuárionãodeveficarpresoemumdeterminadopontodapágina.
Façatestesenavegueutilizandosomenteotecladoparaidentificarpossíveisbarrei-
93

## Página 102

6.4. Princípio2:operável CasadoCódigo
ras(comoscripts)quenãopermitamanavega çãoeopera çãocorretadapáginaou
aplicação.
Diretriz2.2–temposuficiente
Deixartemposuficienteparaqueousuáriopossacumprirastarefasdapágina,
comolereutilizaroconteúdo.Atualiza çõesautomáticaseatividadesquenãopermi-
temqueousuáriopossapararoupausarumaa çãodificultamoacessoaoconteúdo.
2.2.1Ajustávelportemporização
Proporcioneapossibilidadededesligar,ajustaroupausarotempoparaqueo
usuáriopossaexecutarsuaa çãoemtemposuficiente.Asexce çõessãoparaa çõesem
temporealequandoolimitedetempoéessencial,comoumleilãoonline.
2.2.2Colocarempausa,parar,ocultar
Ousuáriodevesercapazdepausar,pararouocultarquaisquerinforma çõesem
movimento,emmodointermitenteouemdeslocamento,quesejaminiciadasauto-
maticamente,duremmaisdecincosegundosesejamapresentadasemparalelocom
outroconteúdo.
Diretriz2.3–convulsões
Nãocrieconteúdosquepossamcausarconvulsõesparaosusuários.
2.3.1Trêsflashesouabaixodolimite
Evitarpublicarconteúdoqueexibatrêsflashesnoperíododeumsegundo.Pes-
soascomfotosensibilidadepodemterconvulsões,dependendodaformacomoo
conteúdopisqueemumatela.Adocumenta çãodoW3Cfornecemaisdetalhesso-
breotamanhodeumaáreaseguraparaopiscardeflashesdeluzquenãosejamem
todaatela.
Diretriz2.4–navegável
Fornecerformasdeajudarosusuáriosanavegar,localizarconteúdosedetermi-
narolocalemqueelesestãoemumapáginaweb.Ousuáriodevetercontrolesobre
oconteúdoesobresualocaliza çãonapáginaWeb,oquedevefacilitaranavega ção
ebuscaporinforma ção.
94

## Página 103

CasadoCódigo Capítulo6. AsdiretrizesdeacessibilidadeparaconteúdonaWeb–WCAG
2.4.1Ignorarblocos
Possibilitequeousuáriopossasaltarouignoraráreasespecíficasdapágina.As
técnicasparacumpriressecritériosãoasseguintes:
Adicioneumlinknotopodapáginaparaoconteúdoprincipal. Essatécnica
beneficianãosópessoasqueutilizamsoftwaresleitoresdetelacomotambémpes-
soascommobilidadereduzida,jáquepossibilitaoacessoviatecladoaoconteúdo
principalsemanecessidadedenavegarportodososlinksdapágina.
<a href="#skip">Saltar conteúdo </a>
.....
<h2 id="skip">Conteúdo principal </h2>
Essatécnicapodeserutilizadaparasaltarnãosóparaoconteúdoprincipalcomo
tambémsaltarapenasblocosespecíficosdeconteúdo.
Utilizeoscabe çalhosparasepararasse çõesdodocumento.
Aestruturadecabe çalhoséimportantíssima,poisalémdegarantirasemântica
decadabloco,definindoseugraucomrela çãoaocabe çalhoanterior,possibilitaque
usuáriosdetecnologiasassistivasutilizemesserecursoparanavegarapenaspelos
cabeçalhos. Porexemplo,usuáriosdesoftwaresleitoresdetelanavegampelosca-
beçalhospressionandoatecla“H”doteclado,mastambémpodemnavegarpelos
númerosde1a6dotecladonuméricoparanavegarpeloníveldecabe çalhodesejado
(H1-H6).
2.4.2Páginacomtítulo
Otítulodevedescreverclaramenteotópicoouafinalidadedapágina.Deveficar
claroaousuáriooqueelevaiencontraraoacessaraquelapáginaweb.Oelemento
<title>éumdosprimeiroselementosaserlidoporumsoftwareleitordetela.
<title>The World Wide Web Consortium </title>
2.4.3Ordemdofoco
Aordemdenavega çãodapáginadevesersequencialnaturalmente. Casoisso
nãosejapossível,devem-seproporcionarformasparagarantiressanavega çãose-
quencialsemqueosignificadoeaoperabilidadesejamperdidos. Astécnicaspara
garantiressecritériosãosimples.
Crieumasequêncialógicadetabula çãoutilizandoosrecursosdoHTML.
95

## Página 104

6.5. Princípio3:compreensível CasadoCódigo
Elementosdelinkeformuláriosjáproporcionamporpadrãoofocoporteclado.
Poressemotivo,utilizarrecursosdeformalinearesequencialéorecomendado.
Casonãosejapossível,pode-sefazerusodoatributo tabindexparaobteroresul-
tadoadequadonanavega ção.
<a href="index.html" tabindex="1">Link para a página principal </a>
<input type="text" name="nome" tabindex="2">
2.4.4Finalidadedolink(emcontexto)
Garantirqueafinalidadedecadalinkpossaserdeterminadapelotextodentro
doprópriolink.Evitarousode“cliqueaqui”ou“vejamais”sãoalgunsdosexemplos.
Ousuáriodevesercapazdecompreenderaquelelinkforadecontexto.Porexemplo:
<a href="rotas.html">
Rotas para chegar ao consultório
</a>
<a href="rotas.html">
<img src="rota.gif" alt=" Rotas para chegar ao consultório " >
</a>
6.5 Princípio3: compreensível
Ainforma çãoeaopera çãodainterfacedeusuáriotêmdesercompreensíveis.
Oqueissosignifica? Queosusuáriosdevemsercapazesdecompreenderas
informações,bemcomoofuncionamentodainterfacedousuário;oconteúdoou
operaçãonãopodeiralémdesuacompreensão.
Diretriz3.1–legível
Tornaroconteúdowebcompreensívelelegívelparaoseuusuário.Issoestárela-
cionadoainterferênciasalémdocódigo,comoumtextobemescritoedefinido,mas
algunsrecursosquemelhoramaacessibilidadepodemserimplementadosdeforma
queauxiliemaleituraecompreensãodotexto.
3.1.1Linguagemdapágina
Definiroidiomadapáginaéfundamentalparaqueferramentasdebusca,na-
vegadoresetecnologiasassistivasconsigaminterpretaroconteúdoemseuidioma
96

## Página 105

CasadoCódigo Capítulo6. AsdiretrizesdeacessibilidadeparaconteúdonaWeb–WCAG
correto. Utilizeoatributo langnoelemento <html>paradeclararoidiomada
páginanoiníciodoseucódigo.
<html lang="pt-br">
Vocêpodemudaroidiomaaqualquermomentonapágina,utilizandoosele-
mentosadequados.
Este texto está em português <span lang="en"> and in english </span>
Diretriz3.2–previsível
FaçacomqueaspáginasWebsurjamefuncionemdeformaprevisível.Surpre-
enderousuárioemtarefasrotineirasounabuscaporinforma çãopodeatrapalhara
efetividadedasuapáginaWeb.
3.2.1Emfoco
Umcomponentedapáginaouaplica çãonãoiniciaumaaltera çãodecontexto
quandorecebeofoco. Ummenudropdownqueiniciaumaa çãoapenasaofazer
focoouumlinkqueexecutaumafun çãoautomaticamenteaoreceberfocopode
dificultaroacessodepessoasquenavegamporteclado,comousuáriosdesoftwares
leitoresdetela.
3.2.2EmEntrada
Alteraradefini çãodeumcomponentedeinterfacedeusuárionãoprovoca,au-
tomaticamente,umaaltera çãodecontexto,amenosqueousuáriotenhasidoavisado
sobreessasitua çãoantesdeutilizarocomponente.Semprequealgoinesperadoem
umapáginaWebestiverprogramadoparaacontecer,ousuáriodeveserinformado
dessetipodealtera ção.
Diretriz3.3–assistênciadeentrada
Estadiretrizorientaosdesenvolvedoresaajudaremseususuáriosaevitarecor-
rigirerros. Informaçõessobrecomopreencherumcampodeformulárioousobre
comoousuáriodeveutilizarosistema/aplica çãosãomuitoúteisnãosóparapes-
soascomdeficiência,mastambémparapessoasquenãoestãofamiliarizadascomo
sistema.
97

## Página 106

6.6. Princípio4:robusto CasadoCódigo
3.3.1Identificaçãodoerro
Sempredescreveraousuárioostiposdeerrosencontradosaoexecutarumaa ção.
Quandoumusuáriopreencheumcampodeformuláriodeformainadequada,o
sistemadeveinformá-loondeestãoesseserrosecomosolucioná-los.
3.3.2Etiquetasouinstru ções
Alémdeidentificaradequadamenteoscamposdeformulárioutilizandooele-
mento label(verdiretriz1.1,critériodesucesso1.1.1,situa çãoC),osformulários
devemconterinforma çõesrelevantessobrecomoousuáriodevepreenchê-lo.Para
evitaroserrosmaiscomuns,comoformasdepreencherdeterminadoscamposou
quaissãoobrigatórios,éimportanteorientarousuáriosobrecomopreenchercorre-
tamenteoformulário.
6.6 P rincípio4: robusto
Oconteúdotemdeserrobustoosuficienteparapoderserinterpretadodeforma
concisapordiversosagentesdousuário,incluindotecnologiasassistivas.
Oqueissosignifica?Queosusuáriosdevemsercapazesdeacessaroconteúdo,
especialmenteconformeastecnologiasevoluem;comoatecnologiaeosagentesde
usuárioevoluem,oconteúdodevepermaneceracessível.
Diretriz4.1–compatível
Essadiretrizorientaamaximizaracompatibilidadecomatuaisefuturosagentes
deusuário,incluindotecnologiasassistivas.
4.1.1Análise
Avalieseoconteúdoestáestruturadodeformaadequada:seoselementosdis-
põemdemarcasdeinícioefimcompletas,seestãoencaixadosconformeaespecifi-
cação,senãotêmatributosduplicadosesetodososIdssãoúnicoseexclusivos.
Uma boa forma de verificar esse critério de sucesso é fazer a validação do
MarkUppelasferramentasdoW3C.Ferramentasdevalida çãodeHTML( http:
//validator.w3.org/)eCSSsãomuitoúteisparaidentificarpossíveisproblemasna
marcaçãodocódigo,quepodemcomprometeraacessibilidadedasuapágina.Fer-
ramentasquefazemverifica çãoautomáticadecontrasteedeacessibilidadetambém
sãoúteisparaauxiliaraencontrarerrosquepoderiamsercomprometedores.
98

## Página 107

CasadoCódigo Capítulo6. AsdiretrizesdeacessibilidadeparaconteúdonaWeb–WCAG
AWAIdisponibilizaumalistacomdiversasferramentasqueajudamafazeruma
verificaçãoautomáticadeacessibilidade.AWAInãoseresponsabilizanemverifica
ouendossanenhumadessesvalidadores. Seu disclaimeréclaro: nenhumaferra-
mentaautomáticapodedeterminaraacessibilidadedeumwebsite. Alistacomas
ferramentasestádisponívelemhttp://www.w3.org/WAI/ER/tools/.
6.7 Conclusão
AsdiretrizesdeacessibilidadeparaconteúdoWebauxiliamodesenvolvedoratornar
seucódigoacessívelparapessoascomdeficiência.Seguirasorienta çõesdeacessibi-
lidadedoW3Cgarantenãosóumcódigoacessível,mastambémumapáginamais
leveequevaiterperformancemelhoremnavegadoresesistemasdebusca.
Esteartigomostradeformamuitosimplesqueboapartedasprincipaisquestões
relacionadasàacessibilidadenaWebestãodiretamenteligadascomousocorreto
dospadrõesdoW3C.Utilizarospadrõesdeformaadequadaevalidarseucódigoé
umótimoprimeiropassoparacolocaraacessibilidadenaWebnarotinadodesen-
volvimento.
AcessibilidadenaWebéumaquestãoimportantenãosomenteparabeneficiar
pessoascomdeficiências. Nós,emalgummomentodanossavidavamosprecisar
daacessibilidade,ouporqueestamosenvelhecendoeperdendoaacuidadevisual,
auditivaedestrezamotoraouporquepodemosestarcomumadasmãosocupadas
aoacessaraWebdeumtelefonecelular.AcessibilidadenaWebéumdospilaresdo
W3Cevaideencontrocomseumaiorprincípio.UmaWebparatodos.
99

## Página 108

6.7. Conclusão CasadoCódigo
Sobre o autor
ReinaldoFerrazéespecialistaemdesenvolvimentoWebdoW3CBra-
sil.Formadoemdesenhoecomputa çãográficaepós-graduadoemde-
signdehipermídiapelaUniversidadeAnhembiMorumbiemSãoPaulo.
Trabalhahámaisde12anoscomdesenvolvimentoWeb. Coordenador
doPrêmioNacionaldeAcessibilidadenaWebedoGrupodeTrabalho
emAcessibilidadenaWeberepresentantedoW3CBrasilemplenárias
técnicasdoW3C.
100

## Página 109

Capítulo7
Aplicaçõeswebsuperacessíveiscom
WAI-ARIA
Acessibilidadeéumtemaimportantíssimo.Ocapítuloanterior,doReinaldoFerraz,
tratoudabasedeacessibilidadenaWebeasdiretrizesdoWCAG.Mashámuito
maisaservisto.Emespecial,o WAI-ARIA,focodestecapítulo,quenosvaipermitir
refinaraindamaisosaspectosdeacessibilidadecomnovassemânticasefocoem
aplicaçõesmaiscomplexas.
WAI-ARIAdefineumaformadetornaroconteúdoeaplicativosWebmaisaces-
síveisapessoascomdeficiência. Elecontribuiespecialmentecomconteúdodinâ-
micoeinterfacedecontrolesdeusuárioavan çadasdesenvolvidoscomAjax,HTML,
JavaScriptetecnologiasrelacionadas.Alémdisso,WAI-ARIAéumpadrãoereco-
mendaçãodoW3C.
Entendaosignificado—WAI(WebAccessibilityInitiative),ARIA(AccessibleRich
InternetApplications).
Emresumo,ARIAsservempradar semânticaparaosleitoresdetela,queinter-

## Página 110

7.1. Leitoresdetela CasadoCódigo
pretarãocommaissignificadoaqueleelementodoseuHTML,alémdeestenderesse
significadodasintera çõescomoprojetoWeb.Vamosverexemplospráticosadiante.
ImportanteressaltarqueasARIAsseaplicamemqualquerversãodoHTML,ou
seja,nãodependemdoHTML5paraseterumprojetoWebacessível.
Dápraseafirmarqueaacessibilidadeestápresenteemtodosospassosdede-
senvolvimentodeumprojetoWeb,eelaémuitoimportante,jáqueestáligadadire-
tamenteaousuário,queprecisaentender,compreendereinteragircomseuprojeto.
Existem ferramentas automatizadas (http://www.w3.org/WAI/ER/tools/) que
ajudamnaavalia çãodeacessibilidade. Contudo,nenhumaferramentasozinhaé
capazdedeterminarseumsitecumpretodosessesitens. Umaavalia çãofeitapor
humanoséessencialparadeterminarseumprojetoWebestáacessível.
7 . 1 Leitores de tela
Existemváriosleitoresdetelanomercado,noentanto,osmaisutilizadossão: J AW S
(Windows/pago), NVDA(Windows/gratuito)e V o i c e O v e r(nativonoMac).São
elesosresponsáveisporajudardeficientesvisuaisanavegaremnainterneteacon-
sumiremtodoseuconteúdo. Porisso,éfundamentalpensarmosnaacessibilidade
deumamaneiracompleta.
QuandofalamosdeimplementaracessibilidadeemprojetosWeb,éimportante
citarqueessestestescome çamutilizandoapenasotecladoe,setodasasprincipais
funcionalidadesocorreremnormalmente,passa-separaopróximopassoqueétestar
comleitoresdetelae,consequentemente,asimplementa çõesdasARIAs.
WAI-ARIApodeter2tiposdeimplementa ção.Utilizandoas rolesouestadose
propriedades.Elessão atributossimplesadicionadosemelementosdoHTMLque
auxiliamnessaintera çãocomosleitoresdetela.
BarradeProgresso
Vamosverumexemplosimples,queimplementaumabarradeprogresso,um
controlebastantecomumdeaparecereminterfacesricas.OHTML5atépossuium
componenteprontohojecom <progress>,maselenãotemsuporteemnavegado-
resantigosepodeserumpoucocomplicadodeestilizar.Porisso,muitasbibliotecas
decomponentesrecriamessafuncionalidadecomelementoscomunscomo dive
usandoJavaScript.
Oproblemadeusar divsimplesparaissoéqueoconteúdonãoéacessível.O
leitordetelanãosabequeaquiloéumabarradeprogresso. UsandoWAI-ARIA,
102

## Página 111

CasadoCódigo Capítulo7. AplicaçõeswebsuperacessíveiscomWAI-ARIA
podemosadicionaressasemântica:
<div class="my-progress-bar" role="progressbar"
aria-valuenow="75" aria-valuemin="0"
aria-valuemax="100" style="width: 75%;" >
75%
</div>
Reparenousodoatributo role="progressbar".Eleindicasemanticamente
queo divrepresentaumabarradeprogressos.Alémdisso,usamosoutraspropri-
edadesaria-paraindicarvaloressemânticosqueantesestavamapenasperdidosno
textoounodesign.Emespecial, aria-valuemaxrepresentaovalormáximoda
barradeprogresso,assimcomo aria-valueminrepresentaomínimo.Eapropri-
edade aria-valuenowrepresentaovaloratual.
Todasessasinforma çõessãoessenciaisparaboaacessibilidade,além,claro,dos
aspectosbásicosquevimosnocapítuloanterior,comosempreproveracessoviate-
clado.
7 . 2 Roles
Oatributo rolenoHTMLredefineosignificadosemânticodeumelemento,me-
lhorandosuainterpreta çãopelosleitoresdetela. Asrolessãoclassificadasdase-
guintemaneira:
1)A b s t r a c t R o l e s—definemconceitosgerais,masnãoservemparamarcarcon-
teúdo;
2) W i d g e t R o l e s—comoopróprionomediz,servemparadefinirwidgetsdeinter-
facedousuário;
3) DocumentStructureRoles —usadosemestruturasqueorganizamoconteúdoem
umapágina,quegeralmentenãoéinterativo;
4) LandmarkRoles—regiõesimportantesdenavega ção.
Veja outro exemplo de implementação de um controle de Abas usando
role="tab"pararepresentaraabaemsie role="tabpanelquerepresentao
conteúdomostradonaquelaaba:
103

## Página 112

7.2. Roles CasadoCódigo
<ul class="tab-panel">
<li>
<a href="#panel1" id="tab1" role="tab"
class="active" aria-selected="true">
Aba 1
</a>
</li>
<li>
<a href="#panel2" id="tab2" role="tab">Aba 2 </a>
</li>
<li>
<a href="#panel3" id="tab3" role="tab">Aba 3 </a>
</li>
</ul>
<div id="panel1" role="tabpanel" aria-labelledby="tab1">
Primeira aba
</div>
<div id="panel2" role="tabpanel" aria-labelledby="tab2">
Segunda aba
</div>
<div id="panel3" role="tabpanel" aria-labelledby="tab3">
Terceira aba
</div>
Repareaindaqueusamosmaisduaspropriedades aria-.A aria-labelledby
amarraoelementodoconteúdodasabascomoelementoqueodescreve.Naprática,
apontaparao iddoelementoquerepresentaaaba.
Jáapropriedade aria-selectedpermiteindicarmosqualabaestáselecio-
nadaatualmente. SeimplementássemosumcontroleviaJavaScriptparatrocade
abas,porexemplo,bastaalterarovalordesseatributo:
$(’[role=tab]’).click(function(){
$(’[role=tab][aria-selected=true]’).attr(’aria-selected’, ’false’);
$(this).attr(’aria-selected’, ’true’);
});
ImplementaçãoemumMenu
MenussãolinkscomunsquemontamosnoHTML.Paraos“videntes”,ébem
óbvio saber que ali existe um menu, mas e para um deficiente visual? Pode-
104

## Página 113

CasadoCódigo Capítulo7. AplicaçõeswebsuperacessíveiscomWAI-ARIA
mosmelhorarisso, darmaissignificadoimplementandoasariascomoatributo
role="menuitem".Alémdisso,a role="navigation"serveparaqueosland-
marksdosleitorespossamentenderquealiéumanavega ção.
No caso de existir submenus, implementearia-expanded="false"
e aria-hidden="true" e altere os valores (via JavaScript) para
aria-expanded="true" aria-hidden="false" conforme o usuário
expandeossubmenus. Comisso,oleitorentenderáqueessalistadelinksestáem
outronível.Importante:submenusdevemseracessíveisviatecladoenãosomente
comomouse.
<ul role="navigation">
<li><a href="#" role="menuitem">menu 1 </a></li>
<li>
<a href="#" role="menuitem">menu 2 </a>
<ul aria-expanded="false" aria-hidden="true">
<li><a href="#" role="menuitem">Submenu 1 </a></li>
<li><a href="#" role="menuitem">Submenu 2 </a></li>
</ul>
</li>
</ul>
ImplementaçãoemumModal
Modaléaquelafamosacaixa,conhecidacomo lightbox(devidoaoplugin),que
trazeminforma çõescomumtipodejanelanaprópriapágina.UtilizandoasArias
podemosdeixá-lasmaissensíveisaosleitoresdetela.
Oatributo role="dialog"informaráaoleitorqueeleestádentrodeumcaixa
dediálogo.
Alémdisso,o aria-labelledbypossuivalordoIDdoelementoquedescreve
acaixadediálogo,quepodeserotítulo,assimoleitorinformaousuárioonome
dessemodal.
<div class="modal" role="dialog" aria-labelledby="titulo">
<div class="modal-header">
<button type="button" aria-label="Fechar Modal" class="close">
×
</button>
<h3 id="titulo">Título da Modal </h3>
</div>
105

## Página 114

7.3. Formuláriosacessíveis CasadoCódigo
<div class="modal-body">
<p>Conteúdo do modal de exemplo </p>
</div>
<div class="modal-footer">
<a href="#" class="btn">Salvar</a>
<a href="#" class="btn">Fechar</a>
</div>
</div>
Outroatributomuitoutilizadoé aria-labelaplicadonobotãode fechar.O
botãofoiconstruídocomapenasum "x”,queéadequadoparausuáriosvisuaissabe-
remqueserveparafechar.Mas,paraleitoresdetela,usamosumafrasemelhor,com
aria-label="Fechar". Oleitorvaiinterpretaressevalornahoradelerparao
usuário.
7 . 3 Formulários acessíveis
Osformuláriossãoasformasmaiscomunsparaapresta çãodeservi çosinterativos,
tendoafinalidadedecoletardadoseinforma çõesaseremprocessados.Comrela ção
àacessibilidade,elespodemviraserumobstáculo,casoseusdesenvolvedoresnão
possuamconhecimentossobreoassunto. Éprecisogarantirqueoformulárioseja
fácildenavegaredeentender,ouseja,ousuáriodeveráteracessoecontrolesobre
todososelementosdoformulárioedeveráconseguircompreenderasinforma ções
contidasnele.
Nocapítuloanteriordolivro,oReinaldomostrouváriastécnicasparasetraba-
lharcomformuláriosdeformaacessível.Oprincipaléusode <label>edoatributo
titlecorretamente. Masépossívelaindacontrolaraordemlógicadenavega ção
com tabindex.
U s a m o s orole="form"noformulárioealgunsatributos aria-paramelhorar
aacessibilidade.Emespecial,utilizando aria-required="true",informaremos
aoleitordetelaqueocampoéobrigatório:
<form action="" method="post" role="form">
<fieldset>
<legend>Título do Formulário </legend>
<p>(*) campos obrigatórios </p>
<div class="form-group">
<label for="name">Nome</label>*
<input class="form-control" name="name"
106

## Página 115

CasadoCódigo Capítulo7. AplicaçõeswebsuperacessíveiscomWAI-ARIA
aria-required="true" type="text" id="name">
</div>
<div class="form-group">
<label for="email">E-mail</label>*
<input class="form-control email" name="email"
aria-required="true" type="text" id="email">
</div>
<div class="form-group">
<label for="msg">Mensagem</label>*
<textarea class="form-control" cols="30" rows="10"
name="msg" aria-required="true" id="msg">
</textarea>
</div>
<input class="btn btn-primary" type="submit"
aria-label="Enviar dados do formulário simples"
value="Enviar dados" >
</fieldset>
</form>
Muitaspáginastêmproblemascomacessibilidadeporsepreocuparemapenas
emexpressarvisualmenteasrestri ções.Porexemplo,umformulárioqueindicaos
camposobrigatóriosapenasatravésdamudan çadecordoinput. Umusuárioque
nãopodever,nãosaberáquaiscampossãodepreenchimentoobrigatório.Asolu ção
éjustamenteusaro aria-required.
Reparequeusamosnovamentenobotãoum aria-labelparasobrescrevera
descriçãoutilizadapeloleitordetelaparaocomponente.
Mensagemdeerrosemformulários
Quandoumerrodeentradadedadosforautomaticamentedetectado,sejapelo
nãopreenchimentodecamposobrigatóriosoupelopreenchimentoincorretodeal-
gumcampo,oitemqueapresentaerrodeveseridentificadoeousuáriodeveser
informadopormeiodetexto.
Apósoenviodasinforma ções,casoexistaalgumcampoincorreto,omesmo
devereceberofoco,eneledeveráconterumamensageminformandoclaramenteao
usuárioorealmotivodoproblema,paraquepossaserresolvido,permitindooenvio
dosdados.
Paramelhorarissoaosusuárioscomdeficiênciavisual,podemosutilizarWAI-
ARIA,implementando aria-invalid="true",queinformaaoleitorqueexiste
107

## Página 116

7.3. Formuláriosacessíveis CasadoCódigo
erronocampo.Eusar aria-labelparadescreverexatamenteoerroocorrido.
<form action="" method="post" role="form">
<fieldset>
<legend class="no-border">Formulário Simples </legend>
<p>(*) campos obrigatórios </p>
<div class="form-group has-error" >
<label for="name">Nome</label>*
<input class="form-control required" name="name"
aria-required="true" type="text" id="name"
aria-invalid="true"
aria-label="Não pode ficar em branco" >
<p for="name" class="help-block">Não pode ficar em branco </p>
</div>
<div class="form-group has-error" >
<label for="email">E-mail</label>*
<input class="form-control email required" name="email"
aria-required="true" type="text" id="email"
aria-invalid="true"
aria-label="Preencha com um e-mail válido" >
<p for="email" class="help-block">
Preencha com um e-mail válido
</p>
</div>
<div class="form-group has-error" >
<label for="msg">Mensagem</label>*
<textarea class="form-control required" cols="30"
rows="10" name="msg" aria-required="true"
id="msg" aria-invalid="true"
aria-label="Não pode ficar em branco" >
</textarea>
<p for="msg" class="help-block">Não pode ficar em branco </p>
</div>
<input class="btn btn-primary" type="submit"
aria-label="Enviar dados do formulário simples"
value="Enviar dados" >
108

## Página 117

CasadoCódigo Capítulo7. AplicaçõeswebsuperacessíveiscomWAI-ARIA
</fieldset>
</form>
Noexemplo,simulamosoenviodoformulárioeoservidorgerandooerrocom
osatributos::aria**corretos. OmesmopoderiatersidofeitocomJavaScriptpara
umavalida çãodinâmica.
Alertas
Seguindoofluxoapóssubmeterseuformulárioaoservidor,podemosainfor-
maçãodesucessooudeerro,conformeaimagemaseguir:
Oatributo role="alert"facilitaparaoleitordetelaqueesseelementoéum
alerta,jáqueelereceberáofocologoemseguida.
<div class="alerta" role="alert">
<p>Mensagem enviada com sucesso </p>
</div>
Aocriarocódigodafiguraanterior,seránecessárioaimplementa çãoviaJavaS-
criptqueoelementotenhafocoerecebaoatributo tabindex="-1",assimoleitor
detelaconseguedarprioridadeemostraraousuárioainforma çãoquealiconsta.
109

## Página 118

7.4. RoleDocumentStructure CasadoCódigo
7 . 4 RoleDocument Structure
Algunsrolesrepresentamapenasestruturasqueorganizamoconteúdonapágina.
Porexemplo,um articleparaindicarumpeda çodapáginaquetemumconteúdo
independente.
OHTML5inclusivepossuiumatag <article>paraessepropósito.Maspo-
demosadicionaramesmasemânticasemHTML5usandoWAI-ARIA:
<article role="article">
<p>Conteúdo</p>
</article>
<div role="article">
<p>Conteúdo</p>
</div>
Háoutrosrolessimplescomessepropósito,como list, img, note, region
e outros. Consulte a lista: http://www.w3.org/TR/wai-aria/roles#document_
structure_roles.
7 . 5 Landmarks
Aslandmarkssãorolesespeciaiscomobjetivodemelhoraranavega çãodousuário
napágina.Aideiaéqueousuáriopossasaltarentre landmarkscomrapidez.
Osleitoresdetelaemsuamaioriajáinterpretamcorretamente,masalgunsainda
não.
1) JawsV.11emaiortemsuportecompleto
2) ChromeVoxV.1emaiortemsuportecompleto
3) VoiceOverV.3emaioresapoiostodosospontosdereferência,exceto“form”
4) NVDA2suportatodosaslandmarks,comexce çãodo“application”
5) WindowEyesV.7nãosuportalandmarks
Nósjáusamosumalandmarkantes,como role="form".Existemváriasou-
tras.
ConheçaagoraparaquecadaLANDMARKsserveeimplementecorretamente,
lembrandoqueelassãoregiõesimportantesdenavega çãodentrodoseuprojeto.
110

## Página 119

CasadoCódigo Capítulo7. AplicaçõeswebsuperacessíveiscomWAI-ARIA
main
Conteúdoprincipalemumdocumento.Istomarcaoconteúdoqueestádireta-
menterelacionadocomotemacentraldapágina.
<main role="main">
Ointeressanteéque,porseruma landmarknavegável,ousuáriopodesaltar
diretoparaoconteúdoprincipal,facilitandomuitoausabilidadeparaleitoresde
tela.Emleitorescompatíveis,fazopapeldolinkde“saltar”quevimosnocapítulo
anterior.
banner
Aregiãoquecontémotítuloprincipalouotítulodosite.Amaiorpartedocon-
teúdodeum banneréorientadaparaolocal,aoinvésdeserespecíficodapágina.
Conteúdoorientadoparaositegeralmenteincluicoisascomoologotipodopatro-
cinadorlocal,oprincipaltítulodapágina,eumaferramentadebuscaespecíficado
site.Tipicamenteesteaparecenotopodapáginaabrangendotodaalargura.
<div role="banner">
complementary
Qualquerse çãododocumentoquesuporta,maséseparáveldoconteúdoprin-
cipal,masésignificativoporsisó,mesmoquandoseparadodele.
<aside role="complementary">
contentinfo
Nocontextodapágina,éondeseaplicaminforma ções.Porexemplo,asnotasde
rodapé,direitosdeautor,oslinksparadeclara çõesdeprivacidadeetc.
<footer role="contentinfo">
form
Aregiãoquecontémumconjuntodeitenseobjetosque,comoumtodo,se
combinamparacriarumformulário.
<form action="" method="post" role="form">
111

## Página 120

7.6. Conclusão CasadoCódigo
navigation
Umacole çãodelinksapropriadosparaousoaonavegarnodocumentooudo-
cumentosrelacionados.
<nav role="navigation">
<a href="">Link 1 </a>
<a href="">Link 2 </a>
<a href="">Link 3 </a>
</nav>
search
AferramentadepesquisadeumdocumentoWeb.Istoétipicamenteumformu-
láriousadoparaenviarsolicita çõesdepesquisasobreositeouaumservi çodebusca
maisgeral.
<div role="search">
application
Umaregiãodeclaradacomoumaaplica çãoWeb,aocontráriodeumdocumento
W e b .
<div role="application">
Paraconheceroutras roles,bastaacessar:
http://www.w3.org/TR/wai-aria/roles#roles_categorization
7 . 6 Conclusão
CriarprojetosWebacessíveisnãoédifícil,nemcustosoemuitomenosimpactano
tempodedesenvolvimento,desdequesejaimplementadonoseuinício.
NoBrasil,nenhumdosgrandese-commerceséacessível,impossibilitandomui-
tosdecompraremetornarem-seindependentenaweb,ouseja,háumagrandefatia
domercadoaindaasersuprida.Sãoclientesfiéisqueestãodeixandodeseratendi-
dos.
ImplementarWAI-ARIAéfácil,simplese,aotestarmos,funcionamagicamente,
bastalereentenderadocumenta ção.
Implementaracessibilidadenãoécaridade,esim,teraconsciênciadequeno
paíshámilhõesdepessoascomalgumtipodedeficiência,sendoelapermanente
112

## Página 121

CasadoCódigo Capítulo7. AplicaçõeswebsuperacessíveiscomWAI-ARIA
outemporária,edessamaneiraestaremospossibilitandoatodoselesoacessoaseu
conteúdo.
OW3CBrasilincentivaessaspráticas.ElecriouoPrêmioNacionaldeAcesssibi-
lidadenaWeb—bastaacessarolinkparasabermaisdetalhes: http://premio.w3c.br/
Sobre o autor
DeividMarqueséumsimplescaradointeriorqueacaboutransfor-
mandoumhobbyemprofissão,jáqueadoraessemundodainternet.É
desenvolvedorFront-endcomfocoemusabilidadeehá5anosmoraem
SãoPaulo.Alémdisso,éumdosorganizadoresdoeventoFrontinSampa
efazpartedoGrupodeTrabalhodeAcessibilidadedoW3CBrasil.
113

## Página 123

Capítulo8
APIsgeniaisdaWebmoderna
Éincríveloqueosbrowsersmodernosconseguemfazer.Paraquemacompanhoua
Webalgunsanosatrás,équasedifícilacreditaraondechegamos.Arevolu çãopós-
HTML5trouxecapacidadesfantásticasparaosnavegadores.Nestecapítulo,vamos
falardealgumasdessasnovidades.
8.1 WebStorage (localStorage e sessionStorage)
Aplicaçõesbaseadasembancodedados,fizeram,eaindafazempartedocotidiano
detododesenvolvedorWeb,Desktop,Mobile(plataformasnativas)etc.Armazenar
informaçõeséalgoimprescindívelnagrandemaioriadossoftwares.
AplataformaWebporsisó,atépoucotempoatrás,semauxíliodeservi çosde
backend,nãoeracapazdepersistirinforma çõesdemaneiraestruturadaebemor-
ganizadanobrowser.Sim,algumassolu çõesalternativassempreexistiram,masaté
hoje,nãopassamdesolu çõesalternativas,quenagrandemaioriadasvezes,nãosa-
tisfazemarealnecessidadedeumaaplica çãoWeb.

## Página 124

8.1. WebStorage(localStorageesessionStorage) CasadoCódigo
Oquetínhamosdisponívelatéagoraquandoqueríamosguardarumainforma-
çãononavegadordocliente?
NomedajaneladoBrowser
Os browsers possuem uma propriedade no escopo principal, a propriedade
name,doobjeto window.
/* Acessando o valor da propriedade */
var data = window.name;
/* Atribuindo valor */
window.name = ’foo’;
Estapropriedadeapenasatribuiumnomeàjanela.Oporéméqueastringque
podeserarmazenadanestapropriedadepodeter,emalgunscasos,até2MB.
Outroporéméqueestapropriedadeguardaoseuestado,ouseja,mesmoquea
páginasejaatualizada,ovalorcontinuadisponível.
Pormuitosanos,algunsdesenvolvedoresutilizaramestatécnicadegostoduvi-
dosocomoumasolu çãoparaarmazenamentodedados.
Atenção:sóestoumencionandoestatécnicaaquiparafinsdecuriosidade,não
autilizeemsuasaplica ções.Comoveremosemseguida,hámelhoresmaneirasde
searmazenardadosnobrowser.
Cookies
Ah,osCookies.
Aprimeiraespecifica çãofoifeitapeloLouMontulli,umfuncionáriodaNetscape
naépoca(meadosde1997).Louestavatentandoresolverumproblemarelacionado
aoprimeirocarrinhodecomprasdaWeb.Asuaespecifica çãooriginalcontinhaas
informaçõesbásicasdecomoos“Cookies”deveriamfuncionarefoiformalizadana
RFC2109,queéareferênciaparaagrandemaioriadosbrowsers.
116

## Página 125

CasadoCódigo Capítulo8. APIsgeniaisdaWebmoderna
Mais da história dosCookies
Recomendamosalgunslinksparavocêconhecerosurgimentodos
cookies:
http://www.nczonline.net/blog/2009/05/05/http-cookies-explained/
http://curl.haxx.se/rfc/cookie_spec.html
http://tools.ietf.org/html/rfc2109
MasoqueéumCookie,afinal?
UmCookieébasicamenteumpequenoarquivotextoqueéarmazenadonamá-
quinadousuáriopelobrowser. Estearquivodetextoéenviadoparaoservidora
cadarequest,paraqueelepossaprocessaralgumtipodeinforma çãorelevante.Co-
okiespodemsercriadostantopeloservidor(aplica çãobackend),quantopelocliente
(aplicaçãofrontend).
MasporquefalartantosobreCookies?
Bom,Cookiesaindasãoextremamenteúteisatualmenteparadiversassitua ções,
inclusive,armazenardados.MasoobjetivodoCookienãoéapenaseste,eporisso,
eleacabasendoineficazemtarefasbásicas.
Éaíquesurgea APIWebStorage,umadasnovidadesdosbrowsersmodernos.
Oquetemosdenovo?
localStorage
localStorageéumobjetoJavaScriptglobal,quenosfornecealgunsmétodos
paraarmazenamentodedadosnobrowser.
SuaAPIébemsimplesebaseadaemchave-valor.Vamosaumexemplo,noqual
queremosgravaro nomeea idadedeumusuário:
window.localStorage.setItem(’nome’, ’John Smith da Silva’ );
window.localStorage.setItem(’idade’, 29);
Notequeutilizamosométdodo setItemparaarmazenarumvalor,passando
umachavecomoreferência.Pararesgatarovalorpreviamentearmazenado,utiliza-
mosométodo getItem,exemplificadoaseguir:
var nome = window.localStorage.getItem(’nome’);
var idade = window.localStorage.getItem(’idade’);
117

## Página 126

8.1. WebStorage(localStorageesessionStorage) CasadoCódigo
console.log(nome); // John Smith da Silva
console.log(idade); // 29
Umdetalheimportante:aAPILocalStoragefuncionaapenascomString.Para
passarumobjeto,éprecisotransformá-loemumaStringantes. Vejaoexemploa
seguir:
window.localStorage.setItem(’usuario’,
{ nome : "John Smith da Silva" , idade : 29 });
Nesteexemplo,temosumfalso-positivo,poisachamadaaométodo getItem
aparentementefunciona.Defato,algumvalorfoiatribuídoparaachave usuario,
porém,nãoovalordesejado. Achave usuarioarmazenouovalor "[object
Object]",queéomesmoqueoresultadodousodométodo toStringnoobjeto.
Ouseja,eletransformouoobjetoemString,masnãodojeitoquegostaríamos.
Amaneiramaisrecomendadaparatrabalharcomobjetosem localStorage,
éutilizarJSON.Exemplo:
var usuario = { nome : "John Smith da Silva" , idade : 29 };
window.localStorage.setItem(’usuario’, JSON.stringify(usuario));
Pararecuperarovalorcomoobjeto,utilizamosométodo parse,comono
exemploaseguir:
var usuario = JSON.parse(window.localStorage.getItem(’usuario’));
console.log(usuario.nome); // John Smith da Silva
console.log(usuario.idade); // 29
Todasasinforma çõessalvasno localStorageficampersistidasnonavegador
dousuárioparasempre.Seelefechareabrironavegador,asinforma çõescontinua-
rãolá.Asúnicasmaneirasderemoverasinforma çõeséseousuáriolimparosdados
donavegadorouse,emnossocódigo,chamarmosométodo removeItem.
sessionStorage
sessionStorage possui implementa ção praticamente igual ao
localStorage,comumasimples,masimportantediferen ça:asessão.
Odadosarmazenadosem sessionStoragesópersistemparaasessãodo
usuário.Istonapráticaquerdizerqueodadonãomaisexistiráapósoencerramento
118

## Página 127

CasadoCódigo Capítulo8. APIsgeniaisdaWebmoderna
dasessão,queéquandoousuáriofecharobrowser. Poresteseucomportamento,
sessionStorageécomumenteutilizadaparaarmazenardadostemporários.
window.sessionStorage.setItem(’temp_user_data’, ’efe2f3f201010101’);
var temp_user_data = window.sessionStorage.getItem(’temp_user_data’);
console.log(temp_user_data); // efe2f3f201010101
Pontosimportantes
TenhaemmentequeasAPIsde localStoragee sessionStoragesão
síncronas. Istoquerdizerqueopera çõesderesgateouarmazenamentodevalores
podemdemorarebloquearaexecu çãodetarefasquedeveriamserexecutadasna
sequência.
Paraousomoderado,ambaspodemserutilizadassemproblema,masparauma
grandequantidadededados,penseemoutrasalternativascomoo IndexedDBou
WebSQL.
Outro ponto que deve ser analisado com cuidado é a regra desame-origin
policy (https://developer.mozilla.org/docs/Web/JavaScript/Same_origin_policy_
for_JavaScript).
AmbasAPIspossuemrestri çãocross-domain.Istoquerdizerque:
• Dadosarmazenadosemhttp://www.dominio.comnãopodemseracessadosde
http://www.foobar.com;
• Dadosarmazenadosemhttps://www.dominio.comnãopodemseracessados
dehttp://www.dominio.com;
• Dadosarmazenadosemhttp://www.dominio.com:8081nãopodemseracessa-
dosde http://www.dominio.com:8080;
• Dadosarmazenadosemhttp://foo.bar.comnãopodemseracessadosde http:
//bazinga.bar.com.
Casosdeuso
WebStoragepodeserutilizadoemdiversassitua ções,dependendodaaplica ção
edoseujulgamentodanecessidade.
Umcasocomumdeusoéparamelhoraraexperiênciaemformulários.
Imagineumgrandeformulário,emqueousuárioprecisapreencherumasérie
decampos. Se,poralgummotivoantesdasubmissãodoformulárioaoservidor,
119

## Página 128

8.1. WebStorage(localStorageesessionStorage) CasadoCódigo
aconteceralgumproblema,comocrashnobrowser,quedadeluz,falhaderedeetc.,
osdadospreenchidospelousuárioserãoperdidos.SecolocarmosaAPIWebStorage
parafuncionaraqui,precisamentefalandodoobjeto localStorage,podemosser
proativos,eguardarosdadosjápreenchidosnobrowser.Bastaumaimplementa ção
simplescomoaseguir:
var input = document.querySelector(’#nome’);
input.addEventListener(’keyup’, function (event) {
var nome = document.querySelector(’#nome’).value;
window.localStorage.set(’campoNome’, nome);
});
Noexemploanterior,noevento keyup,ouseja,apósumateclaserpressionada,
ovalorpreenchidoésalvoem localStorage. Destamaneira,mesmocomal-
gumimprevistonomeiodocaminho,odadoestarásalvo.Aíbastarestaurarovalor
quandoousuáriovoltaraoformulário.
Esteéumexemplosimples,usesuacriatividadeeopoderdaAPIWebStorage
paracriarsolu çõesincríveisemsuasaplica ções.
Consideraçõesfinais
AsAPIsde localStoragee sessionStoragesãosimples,eporestefato
foramfacilmenteadotadaspelosdesenvolvedores.
Aoutilizar,entendabemosseusbenefíciosepontosnegativos,paraquesua
aplicaçãofuncionedamaneiraesperada. Parasabermais,consulteaespecifica ção
oficialeoutrasreferências:
http://www.w3.org/TR/webstorage/
https://developer.mozilla.org/docs/Web/Guide/API/DOM/Storage
http://www.nczonline.net/blog/2012/03/07/in-defense-of-localstorage/
Atualmente,todososbrowserssuportamWebStorage.
120

## Página 129

CasadoCódigo Capítulo8. APIsgeniaisdaWebmoderna
Figura8.1:CompatibilidadedosbrowserscomWebStoragenoiníciode2014.
8.2 p o s tMessage
Problemasdecross-domain
TododesenvolvedorWeb,especialmentenaáreadefront-end,emalgumamomento
jásedeparoucomanecessidadededesenvolveralgumtipodecomunica çãoCross-
Domain.
Cross-Domainéonomepopularpararegrade same-originpolicy,citadaante-
riormentenase çãosobreCookies. Recaptulando:porcomunica çãocross-domain,
entendaocenárioondeumdeterminadodadoprecisasertransferidoparaoutro
contextoemqueodomínio,subdomínio,portaouprotocolosejamdiferentes.
Masporquegostaríamosdefazercomunica çãoCross-Domainnaprática?Mui-
tossiteshojeincluemwidgets,scriptserecursosdeoutrosdomínios.Éobotãode
likedoFacebook,umGoogleMapsembutido,umapropagandadeumservidorex-
ternoentremuitosoutroscasos.Ouainda,emaplica çõescomplexas,podemosoptar
porquebrarnossocódigoemváriaspequenasaplica çõesquesãochamadastodasna
mesmapágina,geralmentecomiframes.
Emtodosessescasos,temosrequisi çõesdedomíniosdiferentesnamesmapá-
gina.E,alémdeincluirrecursosdedomíniosdiferentes,podemosquererconversar
comeles.ComotrocaropontoemummapadoGoogleMapsquefoiincluídovia
iframe;ouseravisadopelobotãodelikedoFacebookdequandoousuáriogostou
ounãodapágina.
Porrazõesdeseguran ça,essetipodecomunica çãoentredomíniosnãoépermi-
121

## Página 130

8.2. postMessage CasadoCódigo
tida. Éasame-originpolicy quecomentamos. Sópossointeragircomrecursosda
mesmaorigem.
Parapassarporcimadessarestri ção,ousode iframesemaplica çõesWebémuito
comum.Eemalgumassitua çãoes,éaúnicaemelhorsolu ção.
Imagine um cenário onde uma página hospedada no domíniohttp://www.
casadocodigo.com.br(páginapai)possuium iframecom srcapontandopara
http://pagamentocdc.com.br(páginafilho).Nestecaso,nemapáginapai,nemapá-
ginafilhopossuempermissãodeusodasAPIsdisponíveisparaacessodiretoaoutros
documentos.
As APIs de acesso a outros documentos são:iframe.contentWindow,
window.parent, window.opene window.opener.
Na figura a seguir, um exemplo em que a página tenta usar a API
iframe.contentWindowemumdocumentoqueestáemoutrodomínio,ouseja,
ferearegrade same-originpolicy.
Figura8.2:Crossoriginiframe
ApostMessageAPI
AAPI postMessagepermitequedadossejamtrafegadosdemaneirasegura
econtroladamesmoemcontextosondearegrade same-originpolicy estariasendo
violada.Naprática, postMessagenospermitecomunica çãocross-originnaWeb
(diferentesdomínios,subdomínios,portaeprotocolo).
AsintaxedaAPIsedivideemenviarerecebermensagens:
/* Enviando mensagens via postMessage */
target.postMessage(mensagem, origem, [transfer]);
122

## Página 131

CasadoCódigo Capítulo8. APIsgeniaisdaWebmoderna
Onde targetéareferênciaparaajanelaondeamensagemdeveserenviada,
comoporexemplooobjetoretornadopelométodo window.open,ouaproprie-
dade contentWindowdeum iframe.
Oparâmetro mensageméamensagempropriamentedita,osdadosaserem
enviadosparaaoutrajanela.ÉpossívelenviarumaString,ouumobjetoliteral.
origemespecificaaURLdajanelaqueamensagemestásendoenviada.Épre-
cisomuitaaten çãoaoespecificaraorigem,poisesteparâmetroéquedefineonível
depermissãodeenviodemensagens. Éessencialparaseguran ça,paranãoexpor
dadosaorigenserradas.
Ousodovalor *épermitido,masédefinitivamentedesencorajado,poiscriaum
túnelaberto,semrestri çõesderecebimentodemensagensdequalqueraplica ção.
Postadaamensagem,aoutrajanela/iframepoderecebê-la.
/* Recebendo mensagens via postMessage */
window.addEventListener("message", function(event) {
if (event.origin !== ’http://casadocodigo.com.br’) {
/*
Só permitimos mensagens do
domínio http://casadocodigo.com.br
*/
return;
}
}, false);
NotequeaAPInosofereceapenasoevento message.Dadosoriundosdequal-
queraplica ção,enviadosvia postMessage,serãoentreguespeloevento message.
Assegure-sedeapenasouviroevento messagequandonecessário,esemprefaçaa
verificaçãodaorigemparaevitarqualquerfalhadeseguran ça.
Pararecuperarmensagens,utilizamospropriedade datadoobjeto event,
exemplificadoaseguir:
/* Recebendo mensagens via postMessage */
window.addEventListener("message", function(event) {
if (event.origin !== ’http://casadocodigo.com.br’) {
/*
Só permitimos mensagens do
domínio http://casadocodigo.com.br
*/
return;
123

## Página 132

8.2. postMessage CasadoCódigo
}
// exibe a mensagem num alerta
alert(event.data);
}, false);
Vamosaumexemploprático. AeditoraCasadoCódigousaumservi çoex-
ternodepagamento.Umaaplica ção,quechamaremosde EditoraApp,rodandono
domíniohttp://www.casadocodigo.com.brquerrecebereenviardadosparaoutra
aplicação, PagamentoApp,queestánodomínio http://pagamentocdc.com.br.
Istovaiserfeitoatravésdeum iframequeapontapara PagamentoAppincor-
poradona EditoraApp.
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Editora Casa do Código </title>
</head>
<body>
<iframe id="PagamentoApp" src="http://pagamentocdc.com.br"></iframe>
</body>
</html>
Acomunica çãoentreasaplica çõesénecessáriaparaqueaeditoraaviseosistema
depagamentossemprequeousuárioescolherumprodutoparacomprar.Eparaque
osistemadepagamentoaviseaeditoraquandoopagamentoforbem-sucedido.
Paraessacomunica çãoserpossível, aaplica ção EditoraAppprecisa ouvir
mensagensenviadasvia postMessageefazerofiltrodaorigemparareceberape-
nasdadosdaaplica ção PagamentoApp.
/* Recebendo mensagens na editora */
window.addEventListener("message", function(event) {
if (event.origin !== ’http://pagamentocdc.com.br’) {
/*
Só permitimos mensagens do sistema de pagamentos!
*/
console.log("Acesso não permitido" );
return;
124

## Página 133

CasadoCódigo Capítulo8. APIsgeniaisdaWebmoderna
}
}, false);
Feitoisso,aaplica ção EditoraAppestaráaptaarecebermensagensapenasdo
domíniohttp://pagamentocdc.com.br.
Agora,vamosenviarmensagensparaaaplica ção PagamentoApppassandoos
dadosdoprodutoqueousuárioquercomprar.
var pgto = document.querySelector(’#PagamentoApp’).contentWindow;
pgto.postMessage(’Coletânea Front-end’ , ’http://pagamentocdc.com.br’);
Pronto.Aaplica ção EditoraAppagorajáestáouvindomensagenseenviando
mensagensparaaaplica ção PagamentoAppdequallivroousuárioquercomprar.
Masofluxoaindanãoestácompleto. Aaplica ção PagamentodApptambém
precisaouvirmensagensda EditoraAppe,claro,filtraraorigemparareceberda-
dosapenasdodomínio http://www.casadocodigo.com.br.
window.addEventListener("message", function(event) {
if (event.origin !== ’http://www.casadocodigo.com.br’) {
/*
Só permitimos mensagens do
domínio http://www.casadocodigo.com.br
*/
console.log("Acesso não permitido." );
return;
}
// processa a cobrança com base no produto desejado
cobranca.comprar(event.data);
}, false);
Paraenviarmensagensdevoltacomaconfirma çãodopagamento,aaplica ção
PagamentoAppprecisaacessaro parent,queéajanelaprincipal:
parent.postMessage(’Pagamento enviado’ ,’http://www.casadocodigo.com.br’);
Agoraofluxoestácompleto,ambasaplica çõespodemenviarerecebermensa-
gensumaparaaoutra.
Atualmente,todososprincipaisbrowserssuportamaAPIde postMessage.
125

## Página 134

8.3. WebNotifications CasadoCódigo
Figura8.3:SuporteaopostMessagenosbrowsersnoiníciode2014
VocêpodeconsultarmaissobreaAPInaMDN:
https://developer.mozilla.org/en-US/docs/Web/API/Window.postMessage
8.3 WebNotifications
WebNotificationémaisumaentreasprincipaisfeaturesdoHTML5.ÉumaAPIpara
enviarnotifica çõesaousuárioquesãoexibidaspelobrowsernosistemadousuário.
Asnotifica çõessãomostradasmesmoqueousuárioestejaemoutraabaouusando
outraaplica ção.Sãousadas,portanto,parachamaraaten çãodousuárioparaalgo
importante. Note,porém,quenossapáginaprecisaestarabertanonavegadorem
algumaaba,senãonãotemoscomoenviaranotifica ção.
AAPIjáestáemworkingdraftdesde2012eosbrowsersmaismodernos,como
FirefoxeChromejádãosuporte.
AAPIébemsimplese,comováriasoutras(Geolocation,WebRTC),énecessário
pedirpermissãoaousuárioparapoderutilizá-la.AAPInosdisponibilizaoobjeto
Notificatione,parapedirpermissãodeusoaousuário,utilizamosométodo
requestPermission:
Notification.requestPermission(function(perm) {
// trata permissão
});
Ométodo requestPermissionrecebe uma funçãodecallbackcomoparâ-
metroedevolveoSTATUSdarequisi çãodepermissão. EsteSTATUSpodeteros
seguintesvalores: default, deniede granted.
126

## Página 135

CasadoCódigo Capítulo8. APIsgeniaisdaWebmoderna
Osvalores defaulte deniedsignificampraticamenteamesmacoisa,que
vocênãoteráacessoaorecurso.Adiferen çaestánostatus denied,queindicaque
ousuárioexplicitamenteclicounaop ção“negar”.Podemosverificarsetemosacesso:
Notification.requestPermission(function(perm) {
if (permission === "granted") {
// temos autorização para mostrar notificações
}
});
Apóspedirpermissão,bastainstanciarumobjeto Notification:
var notification = new Notification("Casa do Código" , {
icon: "icon.png",
body: "Novo livro na casa do cógigo disponível"
});
Figura8.4:Exemplodenotifica çãomostradaemumFirefoxnoLinux
Oprimeiroparâmetro,eúnicoobrigatório,éotítulodanotifica ção.Osegundo
parâmetroéumobjetoliteralcomalgumasop ções,dentreelas icon—paradefinir
umíconeparaanotifica ção—ebody—quedefineotextodanotifica ção.
Anotifica çãoaindapossui4eventos: click, show, errore close. Es-
tescallbacksnosdãomaispodersobrecadanotifica ção. Podemostomardecisões
específicasparacadaumdoseventos.
Porexemplo,mostrarumanotifica çãodenovoe-mailque,quandoclicada,exibe
oe-mailparaousuário(oGmailfazexatamenteisso):
var notification = new Notification("Novo Email!" , {
icon: "icon.png",
body: "Por favor entre em contato."
});
127

## Página 136

8.4. HistoryAPI CasadoCódigo
notification.addEventListener(’click’,function () {
exibeEmailNaJanela();
});
Ointeressantedestescallbackséque,mesmoqueousuárionãoestejanapá-
gina,aoclicarnanotifica ção,algumaa çãopodeserexecutadaembackgroundna
aplicação.
Umdetalheimportanteéque,pormotivosdeseguran ça,somenteumaa çãoex-
plícitadousuáriopoderequisitarpermissãoparanotifica ção.Pora çãoexplícita,en-
tendaalgumaintera çãocommouseouteclado,comocliquenumbotão,porexem-
plo.Depoisdeaprovadas,asnotifica çõespodemserdisparadassema çãodireta.
Atualmente,apenasasversõesmaisnovasdosbrowsersFirefox,SafarieGoo-
gleChromesuportamWebNotifications.Mascomaespecifica çãosetornandoum
padrãooficial,devemosversuportenosoutrosnavegadoresembreve.
Figura8.5:CompatibilidadedasNotifica çõesnoiníciode2014.
8.4 HistoryAPI
Hábastantetempoosbrowserstêmacapacidadedemanipularohistóricodenavega-
çãodousuário.Masapenasintera çõesbásicas,comovoltareavan çarerampossíveis.
AboanovaéqueaAPIagoranosdáopoderde adicionarentradasaohistórico ,
semcausarorecarregamentodapágina. Alémdisso,aAPIpossuiumeventoque
édisparadoacadanovaentradaouremo ção.MarkPilgrim,emseuexcelente Dive
IntoHTML5,falousobreaHTML5historyAPI:
128

## Página 137

CasadoCódigo Capítulo8. APIsgeniaisdaWebmoderna
"Porquevocêiriamanipularmanualmenteabarradeendere çosdonavegador?
Afinal,umsimpleslinkpodenavegaratéumanovaURL;essaéaformaqueaWeb
temfuncionadonosúltimos20anos. Eissovaicontinuarfuncionandodestaforma.
EstaAPInãotentarevolucionaraWeb. Muitopelocontrário. Nosúltimosanos,os
desenvolvedoresWebtêmencontradonovaseexcitantesformasderevolucionaraWeb
semaajudadepadrõesemergentes. AAPIdehistóricodaHTML5foinaverdade
criadaparagarantirqueasURLscontinuemsendoúteisemaplica çõesWebcomscripts
pesados.
VamosentendermelhoropoderdessaAPI.
ConhecendoahistoryAPI
Comomencionadoanteriormente,aAPIjáexisteháumbomtempo.Voltare
avançarparaumdeterminadopontonohistóricodonavegadoréumatarefasimples:
/* Voltar */
window.history.back();
/* Avançar */
window.history.foward();
Alémdevoltareavan çarexplicitamenteparaopontoanterioreposterior,épos-
sívelnavegardemaneiradinâmicaparaumpontodohistórico:
/* Volta 2 passos no histórico */
window.history.go(-2);
/* Avança 3 passos no histórico */
window.history.go(3);
Aindaépossívelsaberonúmerodeentradasnohistórico,atravésdapropriedade
length:
/* Tamanho do histórico */
console.log(window.history.length);
Essesrecursosfuncionamnosbrowsershámuitosanos.MasoHTML5trouxe
novidadesimportantes,quesãoofocodanossadiscussão.
129

## Página 138

8.4. HistoryAPI CasadoCódigo
Porquemanipularohistórico?
OscasosdeusoparaasnovidadesnaAPIdehistóricovieramcomaevolu ção
dasaplica çõesWebeousodeAjax. Nessescenários,écomumqueintera çõesna
páginacausemrequisiçõesAjaxaoinvésdenavegarparaoutrapáginanova.Essas
interaçõesmodificamoestadodapáginamas,paradeixaraeperiênciadousuário
maissuave,optamosporevitaro refresheusarAjax.
Umexemplopráticoéumaaplica çãoWebcomooGmail.Nacaixadeentrada,
vemosalistadee-mails. Aoclicaremumdeles,éexibidootextodaquelee-mail.
Todaessaintera çãoéfeitaviaAjax(paraobterosdadosdoe-mail)enãocausana-
vegaçãoerefreshdatela.
MasqualoproblemaqueaHistoryAPItentouresolvernessecaso?Quandonão
navegamosparaumanovapáginamasapenasrequisitamosalgoviaAjax,a URL
nabarradeendere çosnãomuda .AURLsómudaquandohánavega ção,eoAjax
quebraisso.OruimdenãomudaraURLéqueousuárionãopodelinkar,favoritar
oucompartilharumatelaintermediáriadaaplica ção.NoexemplodoGmail,seria
interessantepoderguardarnosfavoritosumlinkparaume-mailespecífico.
AHistoryAPItrouxe,portanto,umamaneiradecriarnovasentradasnohis-
tóricodousuárioviacódigoJavaScript.Efetivamente,permitindoquealteremosa
URLnabarradeendere çosesuportemosobotãodeVoltarmesmoemaplica ções
queusamAjaxemvezdenavega çõescomuns.
Novosmétodoseoeventopopstate
Os novos métodos da history API são: history.pushState() e
history.replaceState(). Ambosmétodospermitemadicionaremanipular
entradasnohistórico.
pushState
OmétodopushStateadicionaumaentradanohistóricosemcausarnavega ção
depáginas.Recebecomoparâmetros:
•stateobject:objetoqueseráassociadoanovaentrada;
•title: algunsbrowsersignoramesteparâmetro,masseuobjetivoédefiniro
títulodoestado;
•URL:anovaURL.
130

## Página 139

CasadoCódigo Capítulo8. APIsgeniaisdaWebmoderna
Vamosaumexemploprático:SuponhaqueestamosnositedaCasadoCódigo
http://www.casadocodigo.com.br. Aoclicaremumlivro,digamosquesejaolivro
"ColetâneaFrontEnd”,vamoscarregaroconteúdoviaAjaxeexibi-lonapágina.Gos-
taríamosqueaURLmudasseeohistóricosuportasseessaintera ção.Vamosusaro
pushState:
// carrega dados via Ajax
ajax(’dados-coletanea.json’);
// muda historico e URL
var stateObj = { livro : "Coletânea FrontEnd" };
history.pushState(stateObj, "Coletânea FrontEnd" ,
"products/livro-coletanea-frontend");
Oresultadodoclickseráaadi çãodeumanovaentradanohistórico. Abarra
da URL mudará seu conteúdo parahttp://www.casadocodigo.com.br/products/
livro-coletanea-frontendsemcausararequis çãoaobackenddaaplica ção.Emoutras
palavras,apáginanãoirárecarregar.
replaceStateOmétodo replaceStatefuncionaexatamentedamesmama-
neiraqueométodo pushState,excetopelofatodequeestealteraovaloratualdo
histórico,emvezdecriarumnovo.
popstateAgrandevantagemdeseinserirnovasentradasnohistóricoépermitir
queousuárionaveguecomVoltareAvan çar.Comisso,podemossimularanavega-
çãoentrepáginasusando,porexemplo,nossosconteúdoscomAjax.
Oevento popstateédisparadotodavezqueohistóricomudaconformeo
usuárionaveganele.Notequesomentecomalgumaa çãocomooclicknobotãovol-
tar,ouachamadaaalgunsdosmétodosdenavega çãopelohistórico,faráodisparo
doevento.Chamadasaosmétodos pushStatee replaceStatenãodisparamo
evento popstate.
Podemosescutaroeventoerecuperaroestadodohistórico:
window.addEventListener(’popstate’, function(event) {
console.log(JSON.stringify(event.state));
});
Supondoqueestecódigoestárodandojuntamentecomoexemploanterior,o
resultadoseria:
"{"livro":"Coletânea FrontEnd"}"
131

## Página 140

8.5. Conclusão CasadoCódigo
Nocasodaaplica çãoAjax,podemosimplementarum popstatequerefa çaa
requisiçãoAjaxparaapáginaemqueousuárionavegou.Algoassim:
window.addEventListener(’popstate’, function(event) {
var dados = JSON.stringify(event.state);
carregaDadosLivroAjax(dados.livro);
});
Atualmente,agrandemaioriadosbrowserssuportamosnovosmétodoseevento
dahistoryAPI.
Figura8.6:SuporteaHistoryAPInosbrowsersnoiníciode2014
Algumasreferênciasadicionais:
http://www.whatwg.org/specs/web-apps/current-work/multipage/history.html
http://diveintohtml5.info/history.html
https://developer.mozilla.org/docs/Web/Guide/API/DOM/Manipulating_the_
browser_history
8.5 Conclusão
AsnovasAPIsHTML5nosproporcionamumagamadepossibilidadesqueantes
eramdifíceisouatémesmoimpossíveisdeseimplementaremnossasaplica ções
W e b .
132

## Página 141

CasadoCódigo Capítulo8. APIsgeniaisdaWebmoderna
WebStoragenospermitearmazenardadosdeformapadronizadaesimplesnos
browserssemadependênciadeumsistemabackendouusodecookies.Estasimples
APIpodenostrazerdesdeganhosdeperformanceemaplica çõescríticasatéecono-
miaderecursocomputacionalnoservidor,ousimplesmentearmazenarpequenas
informaçõesrelevantessobreosusuários.
AAPIdepostMessagenospossibilitatrafegardados cross-domaindeformase-
guraecontrolada,eliminandoanecessidadedeumacamadadeproxy,outecnologias
intermediáriasparafazeroservi ço.
Com WebNotificationspodemos tornar nossas aplicações mais interativas,
mesmoqueousuárionãoestejapresente(nomomento)emnossaaplica ção. Esta
featurepermitequeaaplica çãoenviemensagensemformadenotifica çãoparao
usuário,atémesmoseeleestivercomfocoemoutraaplica ção,ouemoutrosoft-
ware,quenãoobrowser. WebNotificationsexibenotifica çõesnoníveldosistema
operacional,possibilitandoqueousuárioobtenhainforma çõesrelevantesmesmo
executandooutrastarefas.
OsnovosmétodosdaHTML5historyAPI pushState()e replaceState(),
juntamentecomoeventopopstate,nosproporcionamumamaneirapadronizadade
manipularohistóricodobrowser,fazendocomquenossasaplica çõessejammuito
maisdinâmicasparaousuáriofinal.OusoadequadodaHTML5historyAPIpode
gerareconomiaderecursosnoservidor,assimcomomelhoraraexperiênciado
usuário.
Juntas,estaseoutrasnovasAPIsdoHTML5fazemdaWebamaispoderosa
plataformadedesenvolvimentodesoftware.Sejacriativoeestudeosprósecontras,
queosucessodasuaaplica çãoestarágarantido.
133

## Página 142

8.5. Conclusão CasadoCódigo
Sobre o autor
JaydsonGomeséumentusiastadetecnologiasfront-end,principal-
mentenalinguagemqueéumdospilaresdaWeb,oJavaScript.Elepossui
10anosdeexperiêncianaárea,tendotrabalhadoemdiversasempresas,
semprecomodesenvolvedorWeb.Atualmente,trabalhaemumdosmai-
oressitesdenotíciasdaAméricaLatina,naequipedearquititetura,cri-
andoplataformasesolu çõesescaláveis,comfocoemfront-end.Jaydson
tambéméorganizadordeumdosmaioreseventosdeJavaScriptdopla-
neta,aBrazilJSConf,alémdeorganizareventosregionais,comooRSJS
eoFrontInPoa.
134

## Página 143

Capítulo9
AsAPIsdeacessoadispositivosdo
HTML5
Desdeseunascimento,a webvemsetornandoumaplataformacadavezmaisubíqua
epresentenavidadaspessoas.Cadavezmaisaplicativos,sistemasemercadosin-
teirosestãomigrandoparaawebeéinegávelque,apesardeelaserumaplataforma
emconstanteevolu ção,prometeseraindamelhor—oqueprovocaemnós,desen-
volvedores,umsentimentootimistaconstanteenosdáacertezadequeestamosno
lugaremomentocertos.
EstecapítuloapresentaumdosgrandesgruposdoHTML5, denominadode
acessoadispositivos .Essegrupodefineváriasespecifica çõesquepermitemqueas
aplicaçõeswebpossamfornecerfuncionalidadeseexperiênciasmaisricasecientes
dascapacidadesdeseusdispositivos.

## Página 144

9.1. DispositivosesuasAPIs CasadoCódigo
Seu navegador não é mais o mesmo
ComachegadadoHTML5,onavegadorwebtranscendeusuasori-
gens,etornou-sealgomuitoalémdaquele IE6dasuatia .Podemosdizer
queeleestácadavezmais“sensível”aosseusarredores.
“Seasportasdapercepçãoestivessemabertas,tudoapareceriaparao
homemdojeitoquerealmenteé:infinito.”
–WilliamBlake
ParafraseandoWilliamBlake,seasportasdapercep çãorepresentam
umfiltroqueimpedeossereshumanosdeenxergararealidadeemtoda
suaplenitude,entãopodemosdizerqueoHTML5representaaabertura
dasportasdapercep çãoparaosnavegadores.AntesdoHTML5,osna-
vegadoresnão“tinhamideia”daexistênciadeváriosdispositivos,mas
aospoucos,àmedidaquenovasAPIssurgem,onavegadorestácadavez
mais“ciente”dessasinformações—oqueabreumenormelequedepos-
sibilidadesarespeitodoquepodeounãoserfeitonaweb.
9.1 Dispositivos e suasAPIs
Umdispositivoé(quasesempre)representadoporumequipamentodehardware
especial,doqualocomputadordeveestarmunido.Porexemplo,acâmerarepresenta
umsensor(hardware)dotadodemecanismosquecapturamimagensemtemporeal,
ouseja,oequipamentofísicocompostoporsualenteecomponentesrestantes.
Inovaçõesincríveisdeacessoadispositivosaindaestãosendodesenvolvidase
implementadas,masjápodemosusufruirdealgumasdelas.Maisespecificamente,
nestecapítulo,émostradocomoobterosseguintesdadosatravésdosseusrespectivos
dispositivos:
•Vídeoviacâmera;
•Áudio viamicrofone;
•LocalizaçãogeográficaviaGPS;0
•Aceleraçãoemrela çãoaoseixosortogonaisviaacelerômetro;
136

## Página 145

CasadoCódigo Capítulo9. AsAPIsdeacessoadispositivosdoHTML5
•Orientaçãoemrela çãoaoseixosortogonaisviagiroscópio;
• Informaçõessobre cargaestatus dabateria;
• Controledevibrações doaparelho;
•Quantidadedeluz doambienteviasensordeilumina ção.
Paracadadispositivo,háumaAPIquedefinetudooquepodeserfeitocomele.
EvoluçãodasAPIs
ÉimportanteressaltarqueessasAPIsnãopararamdeevoluireque,assimcomo
qualquercoisanomundomaravilhosodaweb,futuramenteelaspoderãoternovos
recursos—quenãosãoabordadosnestelivro.
Sobreprefixosetestesdesuportenosnavegadores
Durantetodoestecapítulo,nãoserãoconsideradososprefixosdenavegadores
específicos,como moz, webkit, mse o. Porexemplo,aAPI getUserMediaserá
referenciadacomoapenas getUserMediaenãocomo mozGetUserMediaou
webkitGetUserMedia.OmesmoserveparatodasasoutrasAPIs.
Emboraosprefixostendamadesaparecer,éimportantequeodesenvolvedor
fiqueatentoetestepelassuasexistênciasantesdetentarutilizarasAPIsdescritas.
Durantetodoocapítulo,tambémseráconsideradoqueonavegadorsuporta
completamenteasAPIsapresentadas,masantesdeutilizá-lasnomundoreal,éacon-
selhávelquesejafeitoumtestepelasuaexistênciaantesdequalquercoisa.Ummé-
todoquepodeserutilizadoparatestarosuporteaumaAPI,inclusiveconsiderando
osprefixosémostradoaseguir.
var apiPinkFloyd = window.apiPinkFloyd || window.webkitApiPinkFloyd ||
window.mozApiPinkFloyd || window.msApiPinkFloyd ||
window.oApiPinkFloyd;
if(apiPinkFloyd !== undefined){
// tem suporte
}
Nessetrecho,procuramospelaexistênciade apiPinkFloydcomousemqual-
querumdosprefixoscitados. apiPinkFloydpertenceaoobjetoglobal window,
maspoderiapertenceraoutroobjetoqualquer,comoporexemplo,aoobjetoglobal
navigator.
137

## Página 146

9.2. Comoonavegadoracessaosdispositivos CasadoCódigo
9.2 Como o navegador acessa os dispositivos
Poracessoadispositivo,entende-secontrolarouacessarasinforma çõesqueumdado
dispositivopodefornecer.Ascapacidadesdecontroleouacessoainforma çõesva-
riamdeacordocomodispositivoemquestão.Porexemplo,nocasodeumacâmera
(geralmenteumawebcam),podemosacessarseuvídeocapturado,noentanto ainda
nãotemosopoderdecontrolarfoco, zoomouaberturadodiafragmadacâmera—
osistemaoperacionalseencarregatotalmentedessastarefasdebaixonível.
QuemdefineoquepodeounãoserrealizadocomcadadispositivoésuaAPI.
EssaAPIédefinidacomoumpadrão,dessamaneiradiferentesnavegadorespodem
implementaramesmaAPIdemaneiraquesuautiliza çãosejaexatamentedaigual
emtodososnavegadoresqueaimplementam.
Mascomo,defato,umnavegadoracessaumdispositivofísico? Arespostaé
muitosimples: elenãoacessa . Pelomenosnãodeumamaneiradireta. Quemfaz
esseacessodebaixoníveléoSO(sistemaoperacional),quepossuios driversneces-
sáriosparasecomunicarcomodispositivo.
Figura9.1:Camadasdesoftwareenvolvidasnoacessoaumdispositivo.
Afiguraanteriorilustraascamadasdesoftwarequeintermedeiamacomunica-
çãodesdeumaaplica çãowebatéosoftwarecontroladordodispositivofísico( mid-
dleware)dohardware.Masoquenosinteressaéapenasacomunica çãoentreonave-
gadoreoSO,queéintermediadapelasAPIsdeacessoaosdispositivos.Ouseja,note
quenãoimportacomocadaSOsecomunicacomseusdispositivos,odesenvolvedor
apenasprecisalidarcomasAPIsdonavegador.
138

## Página 147

CasadoCódigo Capítulo9. AsAPIsdeacessoadispositivosdoHTML5
9.3 Câmera e microfone
ComeçaremosnossaturnêpelasAPIsdeacessoaosdispositivosmaisóbviosdeste
capítulo:acâmeraeomicrofone.Apossibilidadedecapturaráudioevídeonaweb,
pormuitotempo,permaneceuapenascomomaisumobjetodedesejoparaosde-
senvolvedores. Devidoaumanecessidadecadavezmaiscrescente,issotornou-se
possívelatravésdoantigo MacromediaFlash,queproviaessascapacidades.Coma
chegadadoHTML5,finalmentetornou-sepossívelteracessoessestiposdemídia,
consideradostãotriviaishojeemdia.
APIdemídiasdousuário
AAPIparaacessaracâmeraéamesmaparaacessaromicrofone,tornandosua
utilizaçãorealmentemuitosimples—trata-sedométodo getUserMedia(),do
objetoglobal navigator.
Porquestõesdeprivacidade,quandoométodo getUserMedia()forinvocado,
onavegadorirápedirpermissão aousuárioparaacessarsuacâmeraoumicrofone
—dependendodoqueforrequisitado.
Figura9.2: PromptdonavegadorGoogleChromepedindopermissãoparaacessara
câmeradousuário.
Ométodo navigator.getUserMedia()possui3parâmetros:
1)Opções:umobjetoquecontémasop çõesdemídiaquesedesejacapturar.Cada
opçãoéumachavedoobjeto.Existemduasop çõespossíveis: videoe audio,
quepodemseratribuídascomumvalorbooleano.
2) Callbackdesucesso :fun çãoqueseráexecutadacasoousuáriolibereoacesso
aodispositivorequisitado.Éaquiquefaremosalgocomamídiafornecidapela
câmerae/oumicrofone. Essafun çãotemapenas1parâmetro,querepresentaa
streamdemídiafornecida.
139

## Página 148

9.3. Câmeraemicrofone CasadoCódigo
3)Callbackdefalha :fun çãoqueseráexecutadacasoousuário nãolibereoacesso
aodispositivorequisitadoouseamídiarequisitadanãoforsuportada.Essafun-
çãotemapenas1parâmetro,cujoargumentoéumobjetoquerepresentaoerro,
quepodeserdostipos:
•PermissionDeniedError:ousuárionãopermitiuoacessoaodisposi-
tivo.
•NotSupportedError:algumamídiaespecificadanasop çõesnãoésupor-
tada.
•MandatoryUnsatisfiedError:nenhumafontedentreasmídiasespe-
cificadasencontrada.
Algunsexemplosvariandoasop çõesdeáudioevídeo:
// requisita acesso ao microfone apenas (áudio)
navigator.getUserMedia({audio: true}, liberado, recusado);
// requisita acesso à câmera apenas (vídeo mudo)
navigator.getUserMedia({video: true}, liberado, recusado);
// requisita acesso à câmera e microfone (vídeo com áudio)
navigator.getUserMedia({video: true, audio : true}, liberado, recusado);
Seousuárioliberaroacesso,entãoafun ção liberadoserádisparada.
var liberado = function(stream){
// uhull a stream é nossa
};
Apartirdaqui,aspossibilidadessãoimensas,fa çaoquedesejara streamdemídia
obtida.
Exibindoovídeodacâmera
Parasimplesmentecapturarumvídeoeexibi-lonatela,pode-seutilizaroele-
mento <video>doHTML5:
navigator.getUserMedia({video: true}, function(stream){
// passando a stream como source do elemento video
var video = document.querySelector(’video’);
140

## Página 149

CasadoCódigo Capítulo9. AsAPIsdeacessoadispositivosdoHTML5
video.src = window.URL.createObjectURL(stream);
video.play();
}, function(error){
console.log(’Ocorreu um erro: ’ + error.message);
});
Noteque,paraessetrechofuncionarcorretamente,devehaverumelemento
<video>inclusonocódigoHTML.
Brincandocomvídeodacâmeranocanvas
Comoelemento <canvas>,podemosmanipularourealizarqualquertipode
processamentográficoaumvídeocapturado,jáqueaAPIdo canvaspermitemani-
pulaçãodosseusdadosanívelde pixel.Aideiaéjogarcadaquadro( frame)dovídeo
paraocanvasporveze,assim,realizaramanipula çãográficadesejada.
navigator.getUserMedia({video: true}, function(stream){
// passando a stream como source do elemento video
var video = document.querySelector(’video’);
video.src = window.URL.createObjectURL(stream);
video.play();
// configurando os canvas
var canvas = document.querySelector(’canvas#canvas’);
var canvas2 = document.querySelector(’canvas#canvas2’);
canvas.width = canvas2.width = 640 ;
canvas.height = canvas2.width = 480 ;
var ctx = canvas.getContext(’2d’);
var ctx2 = canvas2.getContext(’2d’);
var desenhaFrame = function(){
window.requestAnimationFrame(desenhaFrame);
ctx2.drawImage(video, 0, 0);
var frame = manipulaFrame(canvas2, ctx2);
ctx.putImageData(frame, 0, 0);
};
desenhaFrame();
}, function(error){
console.log(’Ocorreu um erro: ’ + error.message);
});
141

## Página 150

9.3. Câmeraemicrofone CasadoCódigo
Notrechoanterior,estamosdesenhandoquadroaquadrodovídeonocanvas
comafrequênciaestabelecidapelachamada requestAnimationFrame.Acada
execução,manipulamosoquadroatualdovídeocomafun ção manipulaFrame().
Noteque,paraotrechofuncionarcorretamente,devehaverumelemento <video>
edoiselementos <canvas>(#canvase #canvas2)inclusosnocódigoHTML.
Nesseexemploestamosutilizandomaisumcanvasapeanasparamanipularosqua-
dros,eporissodevepermanecerinvisível.
Afun ção manipulaFramepoderealizarqualquertipodeprocessamentona
imagem,comoporexemplo,converterumaimagemcoloridaparapretoebranco.
Seupseudocódigodeveseparecercomooseguinte:
// função que realiza o processamento gráfico deseja na imagem
var manipulaFrame = function(canvas, ctx){
// captura frame
// manipula frame
// retorna frame
};
Comoexemplo,vejacomoficariaocálculodaimagemempretoebranco:
// função que realiza o processamento gráfico deseja na imagem
var manipulaFrame = function(canvas, ctx){
// captura frame
var imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
var pxs = imageData.data;
// manipula frame
for (i = 0 ; i < pxs.length; i +=4) {
// converte as cores RGB do pixel em escala cinza
var grayscale = pxs[i] * .3 + pxs[i+1] * .59 + pxs[i+2] * .11;
pxs[i] = pxs[i+1] = pxs[i+2] = grayscale;
}
// retorna frame
imageData.data = pxs;
return imageData;
};
Vejaessecódigorodandoonline: http://jsfiddle.net/Q78yM/2/
Porserumprocessamentoqueprecisaserfeitoemtemporealeacadaquadro
obtidodovídeocapturado,podeconsumirbastanteosrecursosdeprocessamentode
142

## Página 151

CasadoCódigo Capítulo9. AsAPIsdeacessoadispositivosdoHTML5
umcomputadoreimpactarnodesempenhodaaplicação,entãoénecessáriobastante
cuidadocomessetipodeexperimento.
T o c a n d ooáudiodomicrofone
Parasimplesmentecapturarumáudioetocá-lo,pode-seutilizaroelemento
<audio>doHTML5,eexatamentedamesmamaneiracomonoexemplodovídeo,
usamosastreamdeáudiodeformasimplificada:
navigator.getUserMedia({audio: true}, function(stream){
// passando a stream como source do elemento audio
var audio = document.querySelector(’audio’);
audio.src = window.URL.createObjectURL(stream);
audio.play();
}, function(error){
console.log(’Ocorreu um erro: ’ + error.message);
});
Noteque,paraotrechoacimafuncionarcorretamente,devehaverumelemento
<audio>inclusonocódigoHTML.
Manipulandoáudiodomicrofone
Demaneirasemelhanteaocanvasparaovídeo,podemosutilizaraAPIWebAu-
diopararealizarumamanipulação noáudiocapturadopelomicrofone. Pode-se,
porexemplo,transformarafaladealguémnumavozrobótica.Aspossibilidadessão
infindáveis,poisaAPIWebAudioébastanteextensaecheiaderecursos.Noentanto,
nãoabordaremossuautilizaçãoaqui.
9.4 Geolocalização
U m adasprimeirasAPIsdeacessoadispositivosasurgirnoHTML5foiaAPIde
geolocalização.Comela,passouaserpossívelobteraposiçãodousuárioemrelação
àsuperfícieterrestre,ouseja,umpontoespecíficoemnossoplaneta.Geolocalização
éumainformaçãoquetemsetornadocadavezmaisimportantenosdiasatuais.
Aimpotânciadageolocalização
Hojeemdia,existematéredessociaisquetêmcomofocoalocalizaçãodosseus
usuáriosedelugaresqueessespodemvisitar—issoparanãomencionaraplicações
143

## Página 152

9.4. Geolocalização CasadoCódigo
denavegaçãoemmapaseatémesmojogos.
Alémdasutilidadesmaiscomunsqueacabaramdesermencionadas,ageoloca-
lizaçãopodeservirparamuitasoutrascoisasimportantes.Considerandoanatureza
contextualdessainformação,elapodeserusadaparamelhorar,porexemplo,abusca
easegurançaemvariadasaplicações.
Pedindoumapizzacomsualocalização
Sistemasdebuscanawebpodemutilizargeolocalizaçãoparaotimizarosresul-
tadosdebuscaparaseusutilizadores.IssojáaconteceháumbomtemponoGoogle.
Porexemplo,aorealizarumabuscapor“pizzaria”,oGoogleretornaráprimeira-
menteaspizzariasqueconsideraserasmaisrelevantesparavocê—eháumagrande
chancedequeasmaisrelevantessejamasqueestãomaispertodevocê,ouseja,de
sualocalização.SeousuárioestiverlocalizadonoRiodeJaneiroaorealizarabusca,
entãooresultadodabuscatraráprimeiramenteaspizzariasdoRiodeJaneiro,elogo
depoiscomeçaráatrazeroutrasmenosrelevantes,muitoprovavelmentenoâmbito
doestado(RJ)edepoisporpaís(BR)—oquevemmuitoacalhar,pois,sevocêes-
tiverprocurandoporumapizzaria,desejasabersobreaspizzariaspróximasdevocê
ousobreasdomundointeiro?
OGoogletambémexibeumaminiaturademapa(snippet)nalateral,mostrando
ummapalocalcomaspizzariasmarcadasemsuasdevidasposições. Aimagema
seguirmostraateladeumresultadodebuscaparaotermo“pizzaria”feitanoRiode
Janeiro.
144

## Página 153

CasadoCódigo Capítulo9. AsAPIsdeacessoadispositivosdoHTML5
Figura9.3:ResultadodebuscanoGooglecomaspizzariasmaisbadaladasdoRiode
Janeiro.
Nessecaso,oGooglenãoestáutilizandoaAPIdeGeolocalizaçãoesimfazendo
umaidentificaçãoautomáticaatravésdoIPdousuário(detalhessobreissomaisà
frente).Masessecasoserveparailustrarmuitobemosganhosquepodemserobti-
doscomousodessainformação.
OGoogletambémnosdáapossibilidadedemodificarmanualmenteocontexto
dalocalizaçãoutilizadaemsuasbuscas(videfigura9.4).Notequeaoclicarnaopção
Ferramentasdepesquisa,éexibidaalocalizaçãoatual—nocaso,RiodeJaneiro–RJ,
quefoiidentificadaautomaticamente—,eaoclicarnalocalização, éexibidauma
caixacomumcampotextualondesepodeespecificaroutralocalidade—edessa
maneiraosresultadosdabuscasofrerãoalterações.
145

## Página 154

9.4. Geolocalização CasadoCódigo
Figura9.4:OpçãodemodificaralocalidadeparaabuscanoGoogle.
Localização podesignificarmais segurança
Aplicações críticasqueprecisamterumbomníveldesegurançatam-
bémutilizam-sedalocalizaçãoparamelhorarnessequesito.Bonsexem-
plossãoaplicaçõesdee-mailebankline,poisasegurançadessesdoistipos
deserviçoséconstantementeameaçada.Paraambos,podeserextrema-
menteimportante,porexemplo,manterumhistóricodeondeseususuá-
riosacessaramsuascontase,comisso,tentaridentificarquandoaconta
deumusuárioéacessada(invadida)porumterceiro,quemuitoprova-
velmenteestejalocalizadonumlocalmuitodiferente—comonoexte-
rior.Comisso,aaplicaçãopoderequisitarumaidentificaçãomaisres-
tritaaousuárioquetentaracessarumacontadeumalocalizaçãomuito
diferentesdasanteriores.
Coordenadasgeográficas
Ogloboédivididolatitudeelongitudinalmente. Imaginecomosefosseum
planocartesianoconvencional,ondeoespaçoédivididoentremedidasaologodos
eixosxey(eopcionalmentez,casosejaumsistematridimensional).Pararepresen-
tarumpontonessesistema,utilizamosumadupla([x, y])ouumatripla([x,
y, z]sefortridimensional).
Ageolocalizaçãoéumainformaçãoexpressaemcoordenadasgeográficas,que
similarmenteaumpontodoplanocartesiano,sãocompostasdede2partesobriga-
toriamente:latitudeelongitude.Hátambémumaterceirainformação(opcional)
146

## Página 155

CasadoCódigo Capítulo9. AsAPIsdeacessoadispositivosdoHTML5
quepodecomporumacoordenadageográfica:aaltitude(similaraozdoplanocar-
tesiano).
Figura9.5:LatitudeelongitudenaTerra.Fonte:Wikipedia.
•Latitude:coordenadadoeixonorte-suldaTerra.Expressaemgraus.
•Longitude:coordenadadoeixoleste-oestedaTerra.Expressaemgraus.
•Altitude:altitudedoponto(compostopelalatitudeelongitude)emrelação
aoníveldomar.Expressaemmetros.Opcional.
Comoonavegadorobtémascoordenadasdousuário
Hádiversasmaneirasdeseobterascoordenadasdelocalizaçãodousuário.O
navegador—atravésdosistemaoperacional—tentaobteressainformação de4
maneirasprincipais.
•GPS:seocomputador(oudispositivomóvel)forequipadocomGPS,tenta
obteralocalizaçãoatravésdosistemadeGPS(satélites).Esseéométodode
melhorresultado,ouseja,alocalizaçãoobtidatemumamelhorprecisãoem
relaçãoaosoutrosmétodos.Écomumentepresenteemdispositivosmóveis.
147

## Página 156

9.4. Geolocalização CasadoCódigo
•InformaçãoWi-Fi:seestiverconectadoaumaredeWi-Fi,tentaobteralocali-
zaçãoapartirdeserviçosonlinequeinformamalocalização(previamenteca-
dastrada)doroteadoremqueseestáconectado.Exemplodeserviço:Skyhook
(skyhookwireless.com)—utilizadopeloiOSdaA p p l e .Essemétodoconsegue
serbempreciso,masnãotantoquantooGPS.
•Antenasdecelular:seestiverconectadoaumserviçodecelular,realiza-sea
triangulaçãodasantenasdecelularmaispróximasparatentardefinirumaárea
comum.Essemétodoémenosprecisoqueoanterior,geralmenteconseguindo
apenasdelimitarumaáreacomumamargemdeerrobemmaiorqueoGPSe
Wi-Fi.
•IP lookup:seestiverconectadoàinternet,tentaobteralocalizaçãoapartirde
serviçosdepesquisadeendereçosIP.Exemplo:ip-adress.com.Essemétodoé
maiscomumenteutilizadopeloscomputadoresdesktop(delocalizaçãofixa)
conectadospormeiodeconexãoacabo.
Hátambémumaquestãoimportanteaseconsiderar:otipodedispositivo(no
sentidodecomputador)sendoutilizado. Basicamenteexistemduasclassificações:
osdeposiçãofixaeosdeposiçãovariável.
•Dispositivosdeposiçãofixa:geralmentesãocomputadoresdesktopoulaptop
(dependedolaptop).NãopossuemGPSnemserviçodecelular—anãoser
quesejautilizadoummodem3G,porexemplo. Ocenáriomaiscomumé
utilizar-sedeinformações deWi-FiouapenasoIPlookup.
•Dispositivosdeposição variável: geralmentesão osdispositivosmóveis,
comosmartphonesetablets.ÉmuitocomumquesejamequipadoscomGPS
eaindautilizemumserviçodecelular. Wi-Fitambémépresente,fazendo
comqueessetipodedispositivotenhaàsuadisposiçãotodosos4métodosde
obtençãodelocalização.
OnavegadorapenasrequisitaparaoSOalocalizaçãoeoSO,porsuavez,équem
decidequalométodoqueforneceráamelhorsolução paraodadomomento,de
acordocomadisponibilidadedecadaumdos4métodos.Algunssistemasutilizam
umasoluçãomista,quemesclaminformações demaisdeummétodoparaproduzir
umalocalizaçãomaisprecisa.
148

## Página 157

CasadoCódigo Capítulo9. AsAPIsdeacessoadispositivosdoHTML5
APIdegeolocalização
A API de geolocalização encontra-se no objeto geolocation dentro de
navigator.Então,paratestarosuporteemumnavegador,pode-sefazersimples-
mente:
if(’geolocation’ in navigator){
// tem suporte a geolocalização
}
AAPIébemsimplesepossuiapenas3métodos:
•getCurrentPosition():obtémasinformaçõesreferentesàgeolocalização
dousuárionodadomomento;
•watchPosition():observaeatualizaasinformações degeolocalizaçãodo
usuário,conformeomesmomudadelocalização;
•clearWatch(): cancelaalgum watchPosition()queestejaemanda-
mento.
Porquestõesdeprivacidade,aochamarosmétodosgetCurrentPosition()
ou watchPosition(),onavegadorprimeiramenterequisitaapermissãodousuá-
rioparaacessarsuageolocalização.NonavegadorGoogleChrome,apareceajáco-
nhecidabarradepermissões, comomostradonafiguraaseguir:
Figura9.6:PromptdonavegadorGoogleChromepedindopermissãoparaacessara
geolocalizaçãodousuário.
Obtendoageolocalização
Para obter a geolocalização pontual do usuário,utiliza-se o método
getCurrentPosition():
149

## Página 158

9.4. Geolocalização CasadoCódigo
// obtem geolocalização
navigator.geolocation.getCurrentPosition(function(position){
posicionarMapa(position.coords.latitude, position.coords.longitude);
});
// maneira mais elaborada
navigator.geolocation.getCurrentPosition(function(position){
posicionarMapa(position.coords.latitude, position.coords.longitude);
}, function(error){
console.log(’Ocorreu um erro: ’ + error.message);
}, {
enableHighAccuracy: true,
timeout: 10000,
maximumAge: 0
});
Notrechodecódigoanterior,asduaschamadassãobemsimilares,porémase-
gundasãodefinidosmais2argumentosdeusoopcional.Os3parâmetrosdométodo
getCurrentPosition()são:
•Callbackdesucesso:funçãodecallbackexecutadaaoreceberarepostacom
asinformações degeolocalização. Possuiapenas1parâmetro,queéoobjeto
contendoasinformações.
•Callbackdefalha(opcional):funçãodecallbackexecutadasehouveralgum
erro.Possuiapenas1parâmetro,queéumobjetocontendootipo(code)ea
mensagem(message)doerro.Ostiposdeerropodemser:
–PERMISSION_DENIED(code = 1):usuárionegoupermissãodeuso.
–POSITION_UNAVAILABLE( code = 2): serviçosnão foramcapazes
deforneceralocalizaçãonodadomomento.
–TIMEOUT(code = 3):estourouotempomáximotolerado.
•Opções (opcional):objetocomopções adicionais,quepodemser:
–enableHighAccuracy:booleanoquepermiteindicarquealocaliza-
ção requisitadadeveteramaiorprecisão possível.Issopodedeixaro
processodeobtençãodalocalizaçãomaislento.
150

## Página 159

CasadoCódigo Capítulo9. AsAPIsdeacessoadispositivosdoHTML5
–timeout: tempomáximodetolerânciaparaobtenção delocalização.
Expressoemmilisegundos.
–maximumAge:indicaapossibilidadedeobter-seposições previamente
obtidasecacheadascomumaidademáximaemmilisegundos.Sefor0,
entãosemprerequisitaránovasposições (semcache).
Informaçõesobtidas
Oobjeto positionqueérecebidocomoargumentonocallbackdesucesso
possuiasseguintespropriedadesevalores:
{
timestamp: 1395810885193,
coords: {
latitude: -23.0068436, // graus (-90 até 90)
longitude: -43.3223877, // graus (-180 até 180)
altitude: 88.43, // metros [opcional]
accuracy: 10, // metros [opcional]
altitudeAccuracy: 15, // metros [opcional]
heading: 271.32, // graus (0 até 360) [opcional]
speed: 7.64 // metros por segundo [opcional]
}
}
Notequeháalgumasinformações alémdascoordenadasgeográficasmenciona-
dasanteriormente.T o d a sessasinformações amaissãoopcionaiseserãofornecidas
dependendoseodispositivoutilizadotemacapacidadeparaisso.Nodesktop,geral-
menteserãoobtidasapenasasinformações delatitudeelongitude.JánumiPhone
sãoobtidastodaselas,comexceçãoàvelocidade(coords.speed).
•timestamp:momentoemquealocalizaçãofoiobtida.
•coords.accuracy:precisão(margemdeerro)dascoordenadasobtidas.
•coords.altitudeAccuracy: precisão (margemdeerro)daaltitudeob-
tida.
•coords.heading:direçãoparaondeodispositivoestáapontando.Ovalor
érepresentadoentreointervadode0até360graus(0representaonorte,90
oleste,180osule270ooeste).Podeservirporexemplo,paraimplementar
umabússola.
151

## Página 160

9.4. Geolocalização CasadoCódigo
•coords.speed:velocidadededeslocamentododispositivoexpressaemme-
trosporsegundo.
Observandoageolocalização
Émuitocomumqueumaaplicaçãoquemostrealocalizaçãodousuárioutilize
ummapaparaissoe,geralmente,tambémédesejávelqueaposiçãodousuárionão
sejaestática.Ouseja,seousuáriosedeslocarcomodispositivoparaoutrolugar,sua
posiçãonomapadeveseratualizadaconcomitantemente.
Paraalcançartalobjetivo,éprecisomanteraaplicaçãoconsultandoeverificando
aposiçãoconstantemente.Issopoderiafacilmenteserobtidofazendo-sepollingcom
ométodogetCurrentPosition(),porém,sabemosqueousodepollingnãoé
nadaelegantedopontodevistadeengenhariadesoftware,mandandooparadigma
dedesenvolvimentoorientadoaeventosdiretamenteproespaço,alémdesercons-
tantementeassociadoagambiarras(porqueserá?).Felizmente,não énecessário
utilizarmospolling,poisaAPIprovêummétodoespecíficoparaconstantemente
observaraposiçãodousuário:watchPosition().
// observa geolocalização
navigator.geolocation.watchPosition(function(position){
posicionarMapa(position.coords.latitude, position.coords.longitude);
});
// maneira mais elaborada
navigator.geolocation.watchPosition(function(position){
posicionarMapa(position.coords.latitude, position.coords.longitude);
}, function(error){
console.log(’Ocorreu um erro: ’ + error.message);
}, {
enableHighAccuracy: true,
timeout: 10000,
maximumAge: 0
});
Aparteboadessemétodoéqueseusparâmetrossãoexatamenteosmesmosque
osde getCurrentPosition().Notequeaúnicadiferençaentreessetrechode
códigoeoanterioréonomedosmétodos.Oscallbacksdesucessoedeerrotambém
recebemosmesmosobjetoscomasmesmasinformações —positione error,
respectivamente.
152

## Página 161

CasadoCódigo Capítulo9. AsAPIsdeacessoadispositivosdoHTML5
A p ó swatchPosition()serchamado,elesemanteránumestadodeespera
—nãobloqueante,poisasrespostassãoassíncronas—edisparandooscallbacksde
erroousucessosemprequeasrespostaschegarem.
OutrodetalheéqueométodowatchPosition()retornaumnúmeroiden-
tificadorúnico(ID),queserveparaquesepossarealizarseucancelamentoposte-
riormente. Paracancelaruma“observação”,porassimdizer,utiliza-seométodo
clearWatch(),querecebeapenas1argumento:oIDdeuma“observação”pre-
viamentecriada.
// obtendo id da observação
var watchId = navigator.geolocation.watchPosition(function(position){
posicionarMapa(position.coords.latitude, position.coords.longitude);
});
// cancelando a observação quando clicar no botão
botaoFechar.addEventListener(’click’, function(){
navigator.geolocation.clearWatch(watchId);
});
Mostrandoalocalizaçãoemummapa
ComointuitodeexemplificarasimplicidadedeusodaAPIdegeolocalização,
serádemonstradocomomostrarummapacomsualocalizaçãoatual.Paradesenhar
omapadesseexemplo,foiescolhidaaAPIdoGoogleMaps,cujautilizaçãoébem
simples.
ComeçandocomoHTML,temosumamarcaçãobemsimplesaseguir.Oele-
mento <div id="mapa">éutilizadopelaAPIdoGoogleMapsmonteomapa
dentrodomesmo.Depoissãoinclusososscriptsnecessários:aAPIdoGoogleMaps
eanossaaplicação.
<!doctype html>
<html>
<head>
<title>Mapa</title>
</head>
<body>
<div id="mapa"></div>
<script type="text/javascript"
src="https://maps.google.com/maps/api/js?sensor=true"></script>
<script type="text/javascript" src="meu_mapa.js"></script>
153

## Página 162

9.4. Geolocalização CasadoCódigo
</body>
</html>
Oconteúdode meu_mapa.js(nossaaplicação)deveseparecercomoseguinte:
var montarMapa = function(position){
// objeto de localizacao do google maps
var localizacao = new google.maps.LatLng(
position.coords.latitude,
position.coords.longitude
);
// elemento DOM onde será montado o mapa
var elementoMapa = document.getElementById(’mapa’);
// objeto de mapa do google maps
var mapa = new google.maps.Map(elementoMapa, {
zoom: 10,
center: localizacao,
mapTypeId: google.maps.MapTypeId.ROADMAP
});
// adiciona um marcador para a localização no mapa
new google.maps.Marker({
map: mapa,
position: localizacao,
title: ’Você está aqui’
});
};
navigator.geolocation.getCurrentPosition(montarMapa, function(error){
console.log(’Ocorreu um erro: ’ + error.message);
});
Quando getCurrentPosition() obtém a localização, a função
montarMapa() échamada —que por sua vez, recebe o objeto position
comascoordenadasusadasparaconstruiroobjetodeposiçãogeográficadoGoogle
Maps( google.maps.LatLng). O restantedo script se encarregaapenasde
montarummapacentralizadonalocalização recebidaedecolocarummarcador
nomapaqueindiquevisualmenteessalocalização.
154

## Página 163

CasadoCódigo Capítulo9. AsAPIsdeacessoadispositivosdoHTML5
Figura9.7:MapadaAPIdoGoogleMapsmostrandoalocalizaçãoatualdodisposi-
tivo.
V e j aesseexemploexecutandoonline:http://jsfiddle.net/LmbXN/
Observação: o elementoutilizado para o mapa —nesse exemplo, <div
id="mapa">—devepossuirsuasdimensões definidas(alturaelargura),casocon-
trárioomapanãoaparecerá.AsdimensõespodemserdefinidasatravésdeCSS(pro-
priedades widthe height).
9.5 Acelerômetro e giroscópio
OHTML5defineumanovaAPIparateracessoàsinformações fornecidaspordis-
positivosdeaceleraçãoeorientação(nosdispositivosquepossuemacelerômetroe
giroscópio).
Praticamentetodososdispositivosmóveis(smartphonesetablets)domercado
hojeemdiavêmequipadoscomestessensoreseoquenãofaltatambémsãoaplicati-
155

## Página 164

9.5.Acelerômetroegiroscópio CasadoCódigo
vosejogosqueseutilizamdessashabilidades.Jánodesktopacoisamudaumpouco
eseuusonãoémuitocomum,comexceçãoaosMacBooks,quejávêmequipados
comessetipodehardware.
Para que serve u m acelerômetro noMa cBo o k ?
Oacelerômetro desempenhaumpapelimportantenosMacBooks.
Elessãousadosparadetectaralgummovimentobruscoe,apartirdisso,
osistemapodesetomarumaatitudeparaseprotegerdealgo.Porexem-
plo,seoMacBookforsoltodeumacertaaltura,osistemadetectauma
aceleraçãoelevadaetentadesligarodiscorígido(HDD)docomputadoa
tempo,antesqueestesejaaltamentedanificadoporcausadaqueda.Não
testemissoemcasa.
ParatestarosuporteaAPI:
if(’DeviceOrientationEvent’ in window){
// seu navegador suporta DeviceOrientationEvent
}
if(’DeviceMotionEvent’ in window){
// seu navegador suporta DeviceMotionEvent
}
if(’CompassNeedsCalibrationEvent’ in window){
// seu navegador suporta CompassNeedsCalibrationEvent
}
AntesdeprosseguirmoscomaAPIeseuseventos,algodeveficarbemclaro:os
eixosdosistemadecoordenadasusados.Oseventosretornamdadosreferentesa
cadaumdoseixosX,YeZ:
156

## Página 165

CasadoCódigo Capítulo9. AsAPIsdeacessoadispositivosdoHTML5
Figura9.8:EixosdosistemadecoordenadasdaAPI.
Onde:
•Xéoeixoque“percorre”ateladodispositivodeladoalado(perpendiculara
YeZ);
•Yéoeixoque“percorre”ateladodispositivodebaixoparacima(perpendi-
cularaXeZ);
•Zéoeixoquecompletaosistema,érepresentadocomoestivesse“saindo”da
tela(perpendicularaXeY).
Detalhe:estandoemumlaptop,esteseixosserãorelativosaoplanodoteclado,
enãoaoplanodatela.
AAPIconsistebasicamentedaimplementaçãodetrêseventos:
•deviceorientation:acontecequandohávariaçãonaorientaçãododispo-
sitivo;
•devicemotion:ocorrequandohávariaçãonaaceleraçãodedeslocamento
dodispositivo;
•compassneedscalibration:disparadoquandoédetectadaanecessidade
decalibarabússoladogiroscópio.
157

## Página 166

9.5.Acelerômetroegiroscópio CasadoCódigo
Obtendoaorientaçãododispositivo
Parateracessoàsinformações sobreaorientação dodispositivo,éutilizado
evento deviceorientation.Esseeventoédisparadoquandohánovosdadosdis-
poníveisfornecidospelosensordeorientação(giroscópio),ouseja,quandoaorien-
taçãoatualmuda.Paratermosacessoaessesdados,precisamosapenasdefiniruma
funçãomanipuladoraparaoevento:
window.addEventListener(’deviceorientation’, function(orientData){
// move bola do jogo de acordo com a orientação do dispositivo
moverBola(orientData.alpha, orientData.beta, orientData.gamma);
});
Todososdadosdisponíveisnaocorrênciadoeventoestarãoem orientData.
Aspropriedadescontidasem orientData—alémdosdadosreferentesàinterface
Event—são: alpha, beta, gammae absolute.
Aspropriedades alpha, betae gammarepresentamarotaçãoemgrausem
tornodecadaumdoseixosZ,XeYrespectivamente,comoilustradonafigurase-
guinte.Apropriedade absoluteéumbooleanoqueindicaseosdadosderotação
sãoabsolutos(referentesaosolo)ounão(referentesaelemesmoououtraposição
arbitráriainicial).
Figura9.9:Rotações alpha,betaegammanos3eixosX,YeZ.
Porexemplo,sedeixarmososmartphonedodesenhoempé,ouseja,como
eixoYapontandoparacimaeoeixoZapontandoparanós,betaseráiguala90,
poisapenasrealizamosumarotaçãode90°emtornodoeixoX.Jásedeixarmoso
mesmosmartphonedecabeçaparabaixo,betaseráiguala-90,poisrealizamosa
mesmarotaçãonosentidocontrário.
158

## Página 167

CasadoCódigo Capítulo9. AsAPIsdeacessoadispositivosdoHTML5
Obtendoaaceleraçãododispositivo
Oevento devicemotionédisparadoperiodicamenteefornecedadossobre
movimentosfísicosrealizadosduranteumcertointervalodetempo(ointervaloen-
treaschamadasdopróprioevento). Fornecedadossobretaxaderotação, assim
comoaaceleraçãoreferenteacadaumdostrêseixos.Paratermosacessoaessesda-
dos,apenasdefinimosumafunçãoparamanipulaçãodoevento devicemotion:
window.addEventListener(’devicemotion’, function(eventData){
// faça algo de legal aqui
});
Osdadosfornecidospor eventData—alémdosdadosreferentesàinter-
face Event—são: acceleration, accelerationIncludingGravitye
rotationRate.
•acceleration:forneceaaceleração dodispositivoemrelação acadaum
dostrêseixos.
–x:aceleraçãoemrelaçãoaoeixoX(expressaemm/s2);
–y:aceleraçãoemrelaçãoaoeixoY(expressaemm/s2);
–z:aceleraçãoemrelaçãoaoeixoZ(expressaemm/s2).
•accelerationIncludingGravity: igualmentea acceleration,for-
neceaaceleraçãododispositivoemcadaumdostrêseixos(X,YeZ).Adife-
rençaestánofatodeohardwareterounãoacapacidadedeexcluiroefeitoda
gravidade.Porexemplo,nocasodeodispositivoestar“deitado”eemrepouso,
aaceleraçãonoeixoZsempreteráumvaloraproximadoa9.8(gravidadeter-
restre).
–x:aceleração(comgravidade)emrelaçãoaoeixoX(expressaemm/s2);
–y:aceleração(comgravidade)emrelaçãoaoeixoY(expressaemm/s2);
–z:aceleração(comgravidade)emrelaçãoaoeixoZ(expressaemm/s2).
•rotationRate:provêastaxasderotaçãoreferentesacadaeixo,proprieda-
des alpha, betae gamma(exatamenteosmesmosdadosfornecidospelo
evento deviceorientation).
159

## Página 168

9.6. Bateria CasadoCódigo
Oeventocompassneedscalibration
Comoopróprionomediz,esteeventodeveráseracionadoquandoonavegador
determinarqueumacelerômetroprecisaser(re)calibrado.Issodeveocorrerape-
nasseforprecisoaumentaraprecisãooucorrigiralgumairregularidadenosdados.
Esteeventopossuiumaaçãopadrãoqueficaacargodecadanavegador.Onavega-
dorpode,porexemplo,mostrardetalhesaousuáriodecomorealizaracalibração.
T a m b é mdeveserpossívelmodificarestecomportamentopadrão demodoqueas
aplicações possamapresentarsuaprópriainterfaceparaessatarefa.
9.6 Bateria
ABatteryAPIpermitequetenhamosacessoainformações sobreabateriadonosso
dispositivo—sejaeleumdispositivomóvel(smartphoneoutablet)ouumlaptop
Nocasodecomputadoresdesktop,nãoteremosestainformaçãodisponível,anão
serqueexistaalgumequipadocombateria.
AprincipalutilidadedessaAPIsedánaplataformamóvel,ondegeralmentete-
mosrecursosbemmaisescassosemrelaçãoaosoutrostiposdedispositivoscomos
quaisestamosacostumados(desktopselaptops).U mdestesrecursoséjustamentea
quantidadedeenergiadisponível.
Semsaberqualasituaçãodabateria,umdesenvolvedorteráqueprojetaruma
aplicaçãoassumindooriscodequesemprehaveráquantidadedeenergiasuficiente
pararealizarsejaqualforatarefapretendida.Istosignificaqueumaaplicaçãomal
implementada—nosentidodeserineficiente—poderáexaurirabateriadousuário
facilmente,piorandoassimaexperiênciadousuário.
Porexemplo,imaginequedesenvolvemosumawebappparaoFirefoxOS.Nossa
appdeverárealizarpolling,issoé,deverá,detemposemtempos,acessarumadeter-
minadafontededadosparachecarseháinformaçãonovadisponível—digamos,
porexemplo,quenossaappperguntaaoFacebookde10em10segundosseháalgo
denovonofeed.Emumintervalode1hora,nossaaplicaçãofará360requisições
sóparasaberseháalgodenovo. 360requisições porhorapodefacilmentecom-
prometerabateriadeumdispositivomóvel.Oidealseria,porexemplo,fazeressas
requisições de30em30segundos(baixandoaquantidadederequisições porhora
para120)quandoodispositivonão estivercarregandoemanterafrequênciade5
segundosparaquandoestiverconectadoaumafontedeenergia.
ComaBatteryAPIserápossívelaosdesenvolvedoresterumfeedbackmaisapu-
radoemrelaçãoaestetipodeproblema,oqueauxiliaránatomadadedecisãoem
160

## Página 169

CasadoCódigo Capítulo9. AsAPIsdeacessoadispositivosdoHTML5
situações importanteseconsequentementemelhoraráaqualidadedosoftwarefinal.
AAPIdabateria
T o d a sasfuncionalidadesrelacionadasabateriaestão definidasnainterface
BatteryManager,queéacessívelatravésdoobjeto navigator.battery.Para
testarosuporte:
if(’battery’ in navigator){
// seu navegador suporta a Battery API
}
AAPIpossuiapenas4propriedadesbemsimples: charging, chargingTime,
dischargingTimee level.Justamentepelasimplicidade,cadaumadelasjáse
autoexplicaapenaspeloseunome.
if(navigator.battery.charging){
// a bateria está sendo carregada
console.log(navigator.battery.chargingTime); // 3226s
// faltam 53.7min para terminar de carregar
} else {
// a bateria NÃO está sendo carregada
console.log(navigator.battery.dischargingTime); // 5564s
// faltam 1h32min para descarregar totalmente
}
// nível de carga
console.log(navigator.battery.level); // 0.34 = 34% de carga
•level: indicaoníveldecargaatualdabateria—númeropontoflutuante
(float)de0a1.
•charging:booleanoqueindicaseabateriadodispositivoestáounãosendo
carregada.Notequeistonãoéomesmoquedizerseabateriaestá(ounão)
conectadaaumafontedeenergia,poistemosocasodeestarligadanafontee
100%carregada,oqueimplicaemdizerqueodispositivotalvezpasseautilizar
aenergiaprovenientedafonte—istoacontecenoMacBookenosdispositivos
iOS.
•chargingTime:forneceotempoestimadoparaqueabateriacarreguetotal-
mente.Seabateriaestivercarregando—ouseja,se chargingfor true—,
161

## Página 170

9.6. Bateria CasadoCódigo
seuvalorseráumnúmerointeiroquerepresentaotempoemsegundos.Caso
contrário,será'Infinity'—oquefazsentido,poisseabaterianãoestá
carregando,podemosdizerqueotemporestanteestimadoéinfinito.
•dischargingTime:aocontráriode chargingTime,forneceotempoesti-
madoparaqueabateriadescarreguetotalmente.Seabaterianãoestivercarre-
gando—quando chargingfor false—,seuvalorseráumnúmerointeiro
querepresentaotempoemsegundos.Casocontrário,será'Infinity'.
EventosdaAPI
Paracadaumadas4propriedadesdescritasantes,háumeventoassociado.
•onchargingchange:serádisparadotodavezquehouverumamudançanos
statuscarregando/descarregando,ouseja,quandoovalorde chargingfor
modificado.
•onchargingtimechange:seabateriaestivercarregando,esseeventoserá
disparadotodavezqueovalorde chargingTimemudar.
•ondischargingtimechange: de maneira análoga a
onchargingtimechange, se a bateria não estiver carregando, esse
eventoserádisparadotodavezqueovalorde dischargingTimemudar.
•onlevelchange:serádisparadotodavezqueoníveldecargadabateriava-
riar,ouseja,quandoovalorde levelformodificado.
navigator.battery.addEventListener(’chargingchange’, function(){
if(navigator.battery.charging){
console.log(’Bateria carregando’);
} else {
console.log(’Bateria DEScarregando’);
}
}, false);
navigator.battery.addEventListener(’chargingtimechange’, function(){
var tempoRestante = navigator.battery.chargingTime / 60;
console.log(’Faltam ’ + tempoRestante + ’ minutos para carregar’);
}, false);
navigator.battery.addEventListener(’dischargingtimechange’, function(){
162

## Página 171

CasadoCódigo Capítulo9. AsAPIsdeacessoadispositivosdoHTML5
var tempoRestante = navigator.battery.dischargingTime / 60;
console.log(’Faltam ’ + tempoRestante + ’ minutos para descarregar’);
}, false);
navigator.battery.addEventListener(’levelchange’, function(){
var nivel = navigator.battery.level * 100;
console.log(’O nível da bateria mudou para ’ + nivel + ’%’);
}, false);
9.7 Vibração
Emboraaindanãosejapossívelprovocarterremotosdeescalageográfica,jápode-
mosfazerdispositivosvibrarcomHTML5.Entendapordispositivoqualquermeio
deacessoquepossuaumhardwareespecíficoquepossibiliteisso—comoosdis-
positivosmóveis,poisnão fariaomínimosentidoseucomputadordesktoptera
habilidadedevibrar.
MuitasdessasnovasAPIsdeacessoadispositivossãofocadasemutilidadesmo-
bile(assimcomoaBatteryAPIdaseçãoanterior),aMozillaéaentidadequemais
investenessasespecificações, pelosimplesfatodequeelamantémoFirefoxOS,cuja
propostaéfuncionartotalmenteemcimadospadrões abertosdaweb.
Considerandoqueomecanismodevibração causaumsimplesfeedbacktátil,
existemalgumasutilidadesquepodemserdeinteresseparaumaaplicaçãomóvel.
Asmaiscomunssão, porexemplo,alertarousuárioaodispararumanotificação,
mensagemouligação evibraremmomentosespecíficosaodecorrerdeumjogo
(umabombaexplodindo,talvez)—causandoumamaiorsensaçãodeimersãopara
ojogador.
Outrasutilidades—não tão óbvias—poderiamser,porexemplo,guiarum
usuárioportadordedeficiênciavisualemumambiente,ondecadatipodevibração
poderiacorresponderadirecionamentoscomo‘esquerda’,‘direita’,‘trás’,‘frente’etc.
Apartirdaívaideacordocomacriatividadedecadaum.
Curiosidade
Originalmente,onomedessaAPIseriaVibrator(vibrador),mas,por
questões óbvias,preferirammudarparaVibration.
163

## Página 172

9.8. Iluminaçãoambiente CasadoCódigo
APIparavibração
EssaéaAPImaissimplesdestecapítulo,poisécompostadeapenas1método
supersimples—vibrate,queresidenoobjeto navigator.Paratestarosuporte:
if(’vibrate’ in navigator){
// tann namm!
}
Deacordocomaespecificação,essemétodorecebeapenasumparâmetroque
representaumaduraçãodetempoqueodispositivodevepermanecervibrando.
navigator.vibrate(1000); // vibra por 1000ms (1s)
Esseparâmetrotambémpodeserumalistarepresentandoumpadrãodetoques,
ondecadaitemdalistaalternaentretempodeduraçãodeumavibraçãoeotempo
deduraçãodeumaintervalo.Comumexemploficamaisfácildeentender:
navigator.vibrate([500, 1000, 800, 500, 1000]);
Notrechoanterior,odispositivocomeçarávibrandopor500ms,depoispausa
por1000ms,vibranovamentepor800ms,pausapor500mseterminavibrandopor
mais1000ms.
Casoumachamadadevibração játenhasidodisparada,tambémépossível
cancelá-lapassandoumzero(0)ouumalista(array)vaziacomoparâmetro.
navigator.vibrate(0); // cancela qualquer vibração em execução
navigator.vibrate([]); // mesma coisa
9.8 Iluminação ambiente
Essecomcertezaéumdosrecursosmaisinteressantesquetêmsurgidodentroda
áreadeacessoadispositivos.Elepermitequetenhamosacessoàquantidadedelumi-
nosidadedoambiente,ouseja,podemossaberseousuárioestásituadonumlugar
escuro,porexemplo. Logicamente,odispositivodousuárioemquestão deveser
equipadocomumsensordeluz—qualquerMacBookeamaioriadosdispositivos
móveisjáopossuem.
U m autilidadequepodeserinteressantepodesertornarautomáticaumafunci-
onalidadebastantecomumentreasaplicações deleitoresdefeeds(comooPocket,
164

## Página 173

CasadoCódigo Capítulo9. AsAPIsdeacessoadispositivosdoHTML5
DiggeReadability),queémodificarocontrastedotexto.Assimousuáriopodeal-
ternarentreníveisdecontrastedemaneiraatornarotextomaisconfortávelpara
leitura:
Figura9.10:ContrastesdisponíveisnoleitordefeedsPocket.
Sevocêestivesseànoitenacamaecomasluzesapagadas,qualcontrasteseria
omaisconfortávelparaler?Amaioriadaspessoascomcertezaescolheriaodadi-
reita(comfundoescuro).Graçasaessa A m b i e n tL i g h tE v e n t sAPItorna-sepossível
tomardecisões combasenaquantidadedeluzatualdoambiente.
APIdeiluminação
Esta nova especificação da W3Cdefinedois novoseventos capazes de de-
tectarmudançasnailuminação doambiente: onlightlevel(DeviceLight)e
ondevicelight(DeviceLevel).Paratestarosuporte:
if(’ondevicelight’ in window){
// seu navegador dá suporte ao evento *Device Light*
}
if(’onlightlevel’ in window){
// seu navegador dá suporte ao evento *Light Level*
}
165

## Página 174

9.8. Iluminaçãoambiente CasadoCódigo
A unidade l u x
Luxéumaunidadequeservepararepresentarvaloresdequantidade
deluzambiente.
•onlightlevel:disparadotodavezquandohouverumamudançadeestado
emrelaçãoailuminação.Existem3estadosdiferentes:
–dim:odispositivoseencontranumambienteescurooucompoucailu-
minação.Exemplo:noiteouquartoescuro.
–normal:oambientetemumnívelidealdeluminosidade.Exemplo:sala
iluminadaadequadamente.
–bright:oambientetemumnívelmuitoclaroouatéexcessivoemquan-
tidadedelux(maissobreissoadiante),fazendocomqueatelaadquira
umaspectomeio“apagado”.Exemplo:luzdodia.
•ondevicelight:esteeventoébemsimilarao onlightlevel,adiferença
estánasuagranularidade.Emvezdeapenastrêspossíveisestados(dim,nor-
malebright),temosacessodiretoaovalordeiluminaçãodoambienteexpresso
emlux.
window.addEventListener(’lightlevel’, function(event) {
console.log(event.value); // dim, normal ou bright
});
window.addEventListener(’devicelight’, function(event) {
console.log(event.value); // 5, 10, 78, ...
});
Cabeaosnavegadoresimplementaremointervaloemluxquedefinecadaum
dostrêsestadosdim,normalebright.Entretanto,aespecificaçãodaW3Crecomenda
queodimcorrespondaaambientescomiluminaçãomenoresque50lux—escuro
osuficienteparaqueumaluzproduzidaporumfundobrancosejaumadistração
—,normalcorrespondaaumvalorentre50e10.000lux—umasaladeescritório,
onasceroupôr dosolemumadiaclaro—eobrightaumailuminaçãoacimade
10.000lux—algocomoluzsolardireta.
166

## Página 175

CasadoCódigo Capítulo9. AsAPIsdeacessoadispositivosdoHTML5
U mexemplopráticopodeseroquemudaascoresdapáginadeacordocomo
níveldeluz.Ocódigoébemsimples:podemospegar,porexemplo,onomedonível
deluzeaplicá-locomoumaclassenoHTML.
window.addEventListener(’lightlevel’, function(event) {
document.body.className += event.value;
});
E,viaCSS,estilizarapáginademaneiradiferente:
.dim {
background: black;
color: white;
}
.normal {
background: #eee;
color: #222;
}
.bright {
background: white;
color: black;
}
9.9 Conclusão
Osaparelhosestãoequipadoscomcadavezmaissensoreserecursosdehardware.
OaparelhoSamsungGalaxyS4,porexemplo,jávinhacom9sensores,incluindo
barômetro,sensordetemperaturaeumidade. Aweb,emsuaconstanteevolução,
suportacadavezmaisessestiposderecursos.
Aqui,discutimosalgunsrecursosdehardwarecomunsecasospráticosparausá-
los.Hámuitasoutraspossibilidadeseaverdadeéqueosdesenvolvedoresestãoape-
nascomeçandoaexplorartodoessepotencial.Inspire-se!
167

## Página 176

9.9. Conclusão CasadoCódigo
Sobre o autor
AlmirFilhoéespecialistaemdesenvolvimentoW e bnaGlobo.come
cofundadordoblogLoopInfinito(loopinfinito.com.br),ondecomparti-
lhaseuconhecimentoeexperiênciassobrefront-endepensamentosso-
breopapelmalucoqueadquirimosnomercadocomodesenvolvedores.
PossuigraduaçãoemestradoemCiênciadaComputaçãopelaUniver-
sidadeFederaldoMaranhão,éentusiastaeextremamenteinteressado
pelospadrões W e beprodutividade.Amantedomundoeartistadesan-
duíches.(Twitter:@almirfilho)
168

## Página 177

Capítulo10
DebugandosuaW e bA p p—ou,
Comoseestressarmenos
“Assimquecomeçamosaprogramar,descobrimos—paranossasurpresa—quenão
eratãofácildeobterprogramassemerros,comotínhamospensado.Adepuraçãoteve
deserdescoberta.Lembro-medomomentoexatoemqueeupercebiqueumagrande
partedaminhavidaapartirdeentãoiriasergastaemencontrarerrosemmeus
própriosprogramas.”
–MauriceWilkes,1949
Pordebugar—oudepurar—códigoentende-seoatoderemoverbugs.Bugs,
porsuavez,sãocomportamentosinesperadosemumdadosoftware.Nenhumpro-
gramadoriráescapardeumdia—outodososdias—debugarumcódigopara
identificarecorrigirumproblema—oubug—emumsoftware.Eterámuitasorte
seocódigoquefordebugarfoiescritoporelemesmo.
Debugarcostumaserumatarefamaiscustosaqueescrevercódigo. Edebugar
códigoJavaScriptclient-sideéespecialmentedificilpelafaltadecontrolequetemos

## Página 178

CasadoCódigo
sobreoambienteondeocódigoseráexecutado.Sãováriossistemasoperacionais,
váriasversões desistemasoperacionais,váriosbrowsers,váriasversões debrowsers,
váriasextensões, váriasresoluções detelaediferentesvelocidadesdeconexão. Em
umadessaspermutações seescondeumbugquevocêteráquecaçar.
Logo,dominarasferramentasdedebugsetornaimperativoparaquesejagasto
menostempoprocurandoecorrigindobugsdeseusoftware.
AorigemdotermoDebug
A p e s a rdecontrovérsiasarespeitodaorigemdotermo“debug”,elaécomumente
atribuidaaGraceHopper,umatalentosadesenvolvedoradaMarinhadosE.U.A.
EnquantotrabalhavanocomputadorMarkIIdaUniversidadedeHarvard,por
voltade1945,umaequipedetécnicosobservouumcomportamentoestranhono
painelFdamáquina.Quandoforaminvestigaroporquêdocomportamentoestra-
nho,viramquehaviaumamariposamorta—uminseto,oubugeminglês—em
umdosrelés,queestavacausandotalfuncionamentoanômalo. Aequipepronta-
menteretirouamariposaeGraceHoppercomentouqueelesestavam“debugando”
osistema.
Figura10.1:OcorrênciadomaufuncionamentodamáquinaMarkIIcomamariposa
colada
Ostécnicoscolaramamariposanolivrodeocorrências,informandoqueelaera
acausadomaufuncionamentodamáquina.GraceHopperentãoadicionouafrase,
embaixodamariposa:“Primeirocasodeumbugrealmenteencontrado” .
ChromeDevT o o l s
NestecapítulovamosusaraferramentadedebugdoChrome,conhecidacomo
170

## Página 179

CasadoCódigo Capítulo10.DebugandosuaW e bApp—ou,Comoseestressarmenos
DeveloperT o o l s—ecarinhosamentechamadadeDevT o o l s.Nãoiremosentrarno
detalhedecadafeaturedoDevT o o l s ,massimapresentaralgumassituações edicas
que—provavelmente—irãomelhorarsuarotinadedesenvolvedorweb.
10.1 Console
“Jáédifícilosuficienteencontrarumerroemseucódigoquandovocêestáprocurando
porele;eéaindamaisdifícilquandovocêassumequenãoexistemerrosemseu
código.”
–SteveMcConnell
NoConsole,temosduasdiferentes—ecomplementares—APIsparadebugare
melhorsaberoqueestáacontecendoemnossaaplicação.Sãoelas:
•ConsoleAPI:usadaprincipalmentepara“logar”informações sobreaaplica-
ção.
•CommandLineAPI:umshellondepodemosinteragircomnossaaplicação,
paradepurardeformamelhorumbug.
PodemosusaraConsoleAPIdiretamenteemnossocódigoparaimprimir—
“logar”—oqueestáacontecendoemnossaaplicaçãoemtempodeexecução. Jáa
CommandLineAPIestádisponívelapenasnocontextodoConsoledoDeveloper
T o o l s .
Nestecapítulo,vamostentarfugirdobásico,como console.logefalarsobre
algunsmétodosetécnicasmenosconhecidasporémmuitoúteisnonossodiaadia
decaçadoresdebugs.
Medindotempo—console.time
Ométodoconsole.timepermite—deformafácil—saberquandotempo
determinadaoperaçãodemorou.Chameométodoconsole.timepassandouma
stringcomoargumentoparainicializaracontagemdotempo.Parafinalizar,chame
ométodoconsole.timeEndpassandoamesmastringquefoipassadaanterior-
mente.
Aseguir,umexemplodemediçãodetempoemumarequisiçãoXHR(Ajax)à
APIdoGitHub.
171

## Página 180

10.1.Console CasadoCódigo
// medindo tempo de uma requisição XHR (Ajax)
console.time(’GitHub API demorou’);
$.get(’https://api.github.com/search/repositories?q=tetris’)
.done(function() {
console.timeEnd(’GitHub API demorou’);
});
Figura10.2:Saídadoconsole.time
Logandodadostabulares—console.table
Como console.table,podemosimprimirnoConsoledadoscomoumata-
bela.Ótimo paralogarumarespostadeumaAPI,comonoexemploanterior.Pode-
ríamosimprimirdeumaformamaisfácildevisualizararespostadaAPIdaseguinte
forma:
$.get("https://api.github.com/search/repositories?q=tetris")
.done(function(response) {
console.table(response.items);
});
Épossívelescolherquaiscamposserãomostrados.Passeum arraycomose-
gundoargumentoinformandoquaischavesdosobjetosserãomostradas,comono
exemploaseguir.
$.get("https://api.github.com/search/repositories?q=tetris")
.done(function(response) {
console.table(response.items, ["full_name", "description"]);
});
172

## Página 181

CasadoCódigo Capítulo10.DebugandosuaW e bApp—ou,Comoseestressarmenos
Figura10.3:Saídanoconsoledométodoconsole.table
Imprimindoastacktrace—console.trace
Issoémuitoútilseusadonolugarcorreto.Eleimprimeastacktracedoponto
ondefoichamado,incluindolinksparaaslinhasdosdevidosarquivosJavaScript.
console.trace();
Listandotodosos e v e n tlisteners—getEventListeners
Estafunçãoretornatodosos event listenersdoobjetopassadocomopa-
râmetro.Éumamãonarodanahoradedebugarcódigo.
// Retorna uma lista com todos os event listeners do elemento document
getEventListeners(document);
ListandotodasasregrasCSSdeumelmento—getMatchedCssRules
RetornaumalistadetodasasregrasCSSqueestão sendoaplicadasnoobjeto
passadocomoparâmetro.
// Retorna uma lista com todas as regras CSS aplicadas ao elemento <body>
getMatchedCSSRules(document.querySelector("body"));
Monitorarchamadasaumafunção—monitor
Monitoratodasaschamadasàfunçãopassadacomoparâmetro.T o d avezquea
função monitor(fn)forchamada,estachamadaélogadanoConsolemostrando
onomedafunção,parâmetroseseusvalores.
173

## Página 182

10.1.Console CasadoCódigo
Figura10.4:Monitorandochamadasaumafunção
Afunção unmonitordesligaomonitoramentonafunçãopassadacomoparâ-
metro.
Monitorandoeventos—monitorEvents
Quandoalgumdoseventosespecificadosacontecenoobjetopassadocomopa-
râmetro,oobjeto Eventélogado.Casonãosejaespecificadonenhumparâmetro,
todososeventosserãoescutados.
Figura10.5:Monitorandotodososeventosnoobjeto window
Parafiltrarquaiseventosserãomonitorados,passecomosegundoparâmetroum
arraycomumalistadosmesmos.
// Monitorando apenas os eventos click, resize e scroll
monitorEvents(window, ["click", "resize", "scroll"]);
T a m b é mépossívelespecificartiposdeeventos,quefuncionamcomogrupos
predefinidosdeeventos.Ostiposdisponíveissão:
174

## Página 183

CasadoCódigo Capítulo10.DebugandosuaW e bApp—ou,Comoseestressarmenos
•mouse: mousedown, mouseup, click, dblclick, mousemove,
mouseover, mouseout, mousewheel;
•key: keydown, keyup, keypress, textInput;
•touch: touchstart, touchmove, touchend, touchcancel;
•control: resize, scroll, zoom, focus, blur, select, change,
submit, reset.
Afunção unmonitorEvents desligaomonitoramentonafunção passada
comoparâmetro.
Breakpointemumafunção—debug
Adicionaum breakpointnaprimeiralinhadafunçãopassadacomoparâme-
tro.Comessemétodo,ficamaisfácildebugarumafunçãosobreaqualnãosabemos
emquearquivoelaestáimplementada.
Figura10.6:Adicionandobreakpointemumafunçãopelométododebug
10.2 Utilizando breakpoints
“Sedebugaréoprocessoderemoçãodebugsdosoftware,entãoprogramaréo
processodeintroduzi-los.”
–EdsgerDijkstra
U mbreakpointéumapausaintencionalnaexecução docódigodesuaaplica-
çãoparamelhorajudarnoprocessodedebug.Deumaformamaisabrangente,um
175

## Página 184

10.2.Utilizandobreakpoints CasadoCódigo
breakpointéumaformadeadquirirconhecimentosobreseuprogramaemtempo
deexecução. Nestecapítulo,vamosaprendercomousarestesbreakpoints,como
funcionameporqueelessãonossosmelhoresriflesnatemporadadecaçaaosbugs.
Ocódigoqueservirádeexemplo
V a m o susaroseguintetrechodecódigo(problemático)parailustrarousode
breakpoints.U m afunçãoqueadicionaumvaloraumarrayapenasseestevalorjá
nãoexistirpreviamente.
// Adiciona o primeiro argumento ao array passado como segundo argumento
// apenas se o primeiro não existir no segundo.
function pushIfNotExists(val, array) {
var i;
for (i = 0; i < array.length; i++) {
if (cmp(array[i], val)) {
return false;
}
}
array.push(val);
return true;
}
Essafunçãorecebedoisargumentos.Oprimeiroargumentoéovaloraserin-
seridonoarrayeosegundoargumentoéoarrayemqueiremosinseriroprimeiro
argumento,apenasseestenãoexistirpreviamentenoarray.
Estamesmafunçãodeclaradaaquiutilizaumaoutrafunçãoparafazercompa-
raçãoentrevalores,afunção cmp.Elatemaseguinteimplementação:
// Retorna ` true` caso o primeiro argumento seja igual ao segundo.
// ` false` caso contrário.
function cmp(a, b) {
if (a == b) {
return true;
} else {
return false;
}
}
176

## Página 185

CasadoCódigo Capítulo10.DebugandosuaW e bApp—ou,Comoseestressarmenos
Ocódigoqueiráusarafunção pushIfNotExistséoseguinte:
// Definimos o valor inicial do array
var arr = [1, "", 3];
// Tentamos inserir os números de 0 a 4 na variável ` arr` .
// Como 1 e 3 já existem, 0, 2 e 4 deveriam ser inseridos
for (var i = 0; i < 5; i++) {
pushIfNotExists(i, arr);
}
console.log(arr.sort());
Ovaloresperadodafunçãoseria ["", 0, 1, 2, 3, 4],porémsevocêexe-
cutarocódigoacima,veráque,naverdade,avariávelarrficoucomovalorfinal
de ["", 1, 2, 3, 4],comonúmero0faltando.Tinhamosumaexpectativaem
relaçãoaocomportamentodestealgoritmo,porémestaexpectativanãofoisatisfeita.
Temosumbug.
Keyworddebugger
V a m o sconfigurarumbreakpointparaentenderoqueestáacontecendoemnossa
aplicaçãoemtempodeexecução. Dentrodo forquetentainserirnovosvaloresà
variávelarr,vamosinserirakeyword debugger,comoaseguir.
for (var i = arr.length; i >= 0; i--) {
debugger; // adicione esta linha ao código
pushIfNotExists(i, arr);
}
RodenovamenteseucódigonoChromeevocêveráqueeleirápararaexecução
exatamenteondedeclaramosakeyword debugger. Declararum debuggerno
códigoéumdosmeiosdeinserirumbreakpoint.
Agoracomeçaoprocessodedebug. V a m o snosaprofundarnestecódigo(em
tempodeexecução)eentenderoqueestáacontecendo.
Controlandoofluxodeexecução
Nesteexatomomento,casovocêestejarodandoseucódigonoChrome,suatela
devedestaforma:
177

## Página 186

10.2.Utilizandobreakpoints CasadoCódigo
Figura10.7:Execuçãodocódigoparadadevidoaobreakpoint
Aexecução doJavaScriptestáparadaenóspodemosveroestadodetodasas
variáveis.Ponhaseumousesobreasvariáveisparaverseuvaloratual.
Oquequeremossaberéporqueovalor 0nãoestásendoinseridonavariável
arr.Entãoestamosprocurandopelomomentoemqueavariávelidoloop for
possuiovalor 0.Continueaexecuçãodocódigoapertandonobotãodestacadona
imagemaseguir.
Figura10.8:Pressioneestebotãoparacontinuaraexecuçãodoscript
Comoakeyword debuggerestádentrodeumloop,ocódigoirápararnova-
mente.Verifiqueovalordavariávelipondoomouseemcimadela.Eladeveestar
comovalor 4agora,jáqueelacomeçoucom 5.
178

## Página 187

CasadoCódigo Capítulo10.DebugandosuaW e bApp—ou,Comoseestressarmenos
Figura10.9:Ponhaomouseemcimadequalquervariávelparasaberseuvalor
Continuecomaexecuçãodoscriptatéqueovalordavariávelicheguea 0,pois
sabemosqueénestaiteraçãodoloopqueobugocorre.U m avezcomavariáveli
comovalor 0,vamosdebugarpassoapassooqueestáacontecendo.
Oscriptestáagoraparadonalinhaondeinserimosakeyword debugger.Para
executaroscriptlinhaalinha,cliquenobotãoqueficaaoladodireitodobotãode
continuaraexecução,comodestacadonaimagemaseguir.
Figura10.10:Cliqueaquiparaexecutarocódigopassoapasso
Agoraocódigoestáparadonachamadadafunção pushIfNotExists.Como
estamosnaúltimalinhaeiteraçãodoloop,oproblemasópodeestardentrodafun-
ção pushIfNotExists.Nóspodemos“entrar”nachamadadeumafunçãopara
entendercomoestafunção irásecomportar. Eéexatamenteissoquequeremos.
Cliquenobotãodestacadonaimagemaseguirpara“entrar”nafunção.
179

## Página 188

10.2.Utilizandobreakpoints CasadoCódigo
Figura10.11:Cliqueaquipara“entrar”nafunção
Vendoocódigodafunção pushIfNotExists,vemosqueantesdeinseriro
valornoarray,verificamosseestevalorprestesaserinseridonãoéigualanenhum
dosvaloresjáexistente.Nósverificamosissocomparandotodososvaloresdoarray
comovaloraserinserido.
A p e r t eobotão parairmosàpróximachamadadefunção, obotão quetemo
desenhodeumasetapassandoporcimadeumponto. V áatéoloop forenele
vamosdebugarcadaiteração.
Continueapertandoomesmobotãoparaqueocódigosejaexecutadopassoa
passo,atéquecheguenalinha return null,queéquandoafunção cmpdiz
quejáexisteumvalordestesnonossocódigo.Quandochegarnestalinha,verifique
quaisvaloresestão sendopassadosparaafunção cmp. Issopodeserfeitopondo
omouseemcimadasvariáveis,ouescrevendonoConsoleasvariáveis.Comojá
sabemoscomoverificarovalordasvariáveisatravésdomouseover,vamosagora
usaroConsole.V o c êpodeirparaaabaConsoleouapertarnobotãomostradona
figuraabaixoparachamarodrawereficarcomaabaSourcesecomoConsolevisíveis
aomesmotempo.
180

## Página 189

CasadoCódigo Capítulo10.DebugandosuaW e bApp—ou,Comoseestressarmenos
Figura10.12:ChameodrawerparaterumConsoleabertoaomesmoqueoSources
Agoraverifiqueovalordasvariáveispassadasparaafunção cmp.U m avezcom
aexecuçãodocódigoparadanonossobreakpoint,ocontextonaabaConsolereflete
ocontextodopontoemquenossocódigoestáparado.Então,podemosverificaro
valordasvariáveisnoConsolee,até,modificá-las.
Paraverificarovalordasvariáveis,apenasdigiteseusnomesnoConsoleeaperte
enter,comonaimagemabaixo.
Figura10.13:Verificandovaloresdasvariáveispassadasparaafunçãocmp
Comopodemosver,afunção cmpretorna truequandocompara 0comuma
stringvazia.Porqueisso?V a m o saveriguarnovamenteasuaimplementação.
Parairdiretonaimplementaçãodeumafunção,digite command+ shift+ O
noOSXou Ctrl+ Shift+ OnoWindowseLinux.Iráaparecerumdialog,digite
cmpedepois Enter.Estamoscadavezmaispróximosdoproblema.
181

## Página 190

10.2.Utilizandobreakpoints CasadoCódigo
Comopodemosver,afunção cmputilizaooperador ==paracompararsedois
valoressão iguais. MasoJavaScriptéumalinguagemfracamentetipada,ouseja,
quandovamoscompararvaloresdetiposdiferentes(aquiestamoscomparandouma
stringcomumnúmero),éfeito,deformaimplícita,umacoerção. A p e s a rdeuma
variávelserumastringeaoutraumnúmero,paraoJavaScript,onúmero0euma
stringvaziasãoequivalentes(nãoidênticas,masequivalentes).
Comparador == e=== noJa v aScript
Ooperador ==,chamadodecomparadorabstrato,primeirotrans-
formaosdoisoperandosparaumtipocomum(todosparanúmeros,
stringetc.) esóentão relizaacomparação. Ooperador ===,cha-
madodecomparador strict,sóretorna truecasoosdoisoperandos
sejamdomesmotipoetenhamvaloresiguais.
Comoboaprática,utilizesempreooperador ===evocênão terá
surpresasdesagradáveis.
Agorasabemosondeestáonossobug.Estávamoscomparandoapenasaequi-
valênciaentredoisvaloresenãoseeramdefatoiguais.Paraquenossocódigoagora
funcionesembugs,bastatrocarooperador ==pelo ===. Destaforma,estamos
comparandovaloretipoentreasvariáveis.
Breakpointvisual
Podemosrepetirtodooprocessoanteriorinserindobreakpointsdeformavisual
semanecessidadedeescreverakeyword debuggerdentrodocódigo.NaabaSour-
ces,bastaclicarsobreonúmerodalinhaquequeremosadicionarumbreakpoint.
182

## Página 191

CasadoCódigo Capítulo10.DebugandosuaW e bApp—ou,Comoseestressarmenos
Figura10.14:Setandobreakpointsdeformavisual
Comoexercício,tenterefazertodosospassosquerealizamosanteriormentese-
tandoobreakpointdeformavisualpelopróprioDevT o o l s .
Breakpointcondicional
Breakpointscondicionais,comoopróprionomesugere,sãobreakpointsquesó
irãoserdisparadoscasoumadeterminadacondiçãosejasatisfeita.Nóspoderíamos
tersimplificadooprocessodedebugdoexemploanteriorcasotivessemosusadoum
breakpointcondicional.
Nósjásabíamosqueoerroestavaaotentarinserironúmero0.Então,podemos
pedirqueaexecução doscriptsejainterrompidaapenasnessacondição. Dentro
dafunção pushIfNotExists,vamossetarumbreakpointcondicionalquandoo
argumento valforiguala 0.Cliquecomobotãosecundáriononúmerodalinha
nocomeçodoloop foreescolhaaopçãoAddconditionalbreakpoint...Dentro
dacondiçãoescreva val === 0.
Quandoestaexpressãoretornartrue,oscriptirápararsuaexecuçãoepodemos
debugarnossaaplicaçãodamesmaformacomofizemosantes,sóque,dessavez,com
menospassos.
183

## Página 192

10.2.Utilizandobreakpoints CasadoCódigo
Figura10.15:Breakpointcondicional
Breakpointsem e v e n tlisteners
Épossíveltambéminserirumbreakpointemeventlisteners.AindanaabaSour-
ces,nacolunadadireita,expandaaseçãoEventListenerBreakpointseescolhao
eventoquedesejadebugar.
Figura10.16:Breakpointemeventlisteners
Seráadicionadoumbreakpointemtodososlistenersdoseventosescolhidosà
direitae,umavezqueoeventofordisparado,oscriptiráparardeserexecutadona
primeiralinhadafunçãodecallbackdolistener.
DebugandoeventosdemutaçãodoDOM
T a m b é mépossívelinserirbreakpointscasoumadadasubárvoredoDOMseja
184

## Página 193

CasadoCódigo Capítulo10.DebugandosuaW e bApp—ou,Comoseestressarmenos
modificada.Emoutraspalavras,casouma divsejainserida,um premovido,uma
classeadicionadaaalgumelementoetc.
Parainserirumbreakpoint,váparaaabaElements,cliquecomobotãodireito
emcimadonó(subárvore)quedesejadebugareescolhaotipodeeventoquequer
queocorraumapausanaexecuçãodoscriptcasosejadisparado.
Figura10.17:BreakpointemMutationeventsdoDOM
Existem3tiposdeeventosdemutaçãodoDOMquepodemserescutadospara
adicionarbreakpoints.Sãoeles:
•Modificaçãonasubárvore:quandoalgumnóéadicionadoabaixodonóque
estásendoinspecionado.
•Modificaçãodeatributos:quandoalgumatributodonóinspecionadoémo-
dificadocomo,porexemplo,quandoumaclasseéadicionadaouremovida.
•Remoçãodenó:quandoalgumnódasubárvoreéremovido.
U m avezquesejaminseridosváriosbreakpointsemdiferentesnós,ficadifícil
saberondeestãotodospara,quandonãoformaisnecessário,removê-los.Naaba
Sources,nacolunaàdireita,existeumlistacomtodososbreakpointsdoDOM.
185

## Página 194

10.3.Emulandodispositivosmóveis CasadoCódigo
Figura10.18:ListadetodososDOMbreakpoints
BreakpointsemchamadasXHR(Ajax)
ParadebugarcódigoquefazchamadasXHR(Ajax)aumadeterminadaURL,
vánaabaSources,nacolunadadireita,noagrupadorcomonomedeXHRBreak-
pointseapertenobotãode“+”.
Figura10.19:BreakpointemchamadasXHR(Ajax)
ElevaiperguntaraURL(oupartedela)quedevecausarobreakpoint.Ésóinserir
eteremosumbreakpointdisparandoquandoaquelaURLforchamadaviaAjax.
10.3 Emulando dispositivosmóveis
“ Aferramentadedepuraçãomaiseficazaindaéopensamentocuidadoso,juntamente
cominstruções deimpressãocriteriosamentecolocadas.”
–BrianKernighan
Debugarumaaplicação webemumdispositivomóvelpodeserumatortura,
186

## Página 195

CasadoCódigo Capítulo10.DebugandosuaW e bApp—ou,Comoseestressarmenos
tanto pela falta de ferramentascomo pelas peculiaridades de cada dispositivo.
Quandofalamosdedesenvolverparamobile,nadasubstituiotestenodispositivo
real.Mas,nestecapítulo,vamosaprenderalgumasferramentasquepodemacelerar
odesenvolvimentoparaestaplataforma.
Habilitandoopaineldeemulaçãodedispositivos
Oprimeiropassoparabrincarcomestasnovasferramentaséhabilitaropainel
deEmulação.Paraisso,cliquenoíconedeSettings,nocantodireitosuperiordoDev
T o o l s .
Figura10.20:AbrindoaspreferênciasdoDevT o o l s
AgorahabiliteocheckboxShow‘Emulation’viewinconsoledrawer.
Figura10.21:HabilitandoaabaEmulationnodrawer
Depois,bastachamaroprópriodrawereclicarnanovaabaEmulation.
187

## Página 196

10.3.Emulandodispositivosmóveis CasadoCódigo
Figura10.22:Opções daabaEmulation
Odrawertambémpodeserchamadopressionandoatecla Esc.
Emulandodispositivos
Normalmente,começamosadesenvolverpáginasouaplicações paraawebtes-
tandoemumbrowserdesktope,sódepois,vamostestaremumdispositivomóvel
para,então,corrigirtodososbugsqueencontramosnodispositivoreal.
NoDevT o o l sépossívelmelhoraressefluxoemulandoalgumascaracterísticas
dedispositivosmóveisetestaralgunscasosquesóaconteceriamnodispositivoreal,
comoumbreakpointdeumamediaquerynoCSS.Ascaracterísticasquepodemser
emuladassão:
•Us e ragent—umastringdisponívelem navigator.userAgentquetam-
bémépassadanocabeçalhodeumarequisição HTTP.Algumasaplicações
verificamseodispositivoéumdispositivomóvelounãoporessastring.
•Screenresolution—emulaasdimensões reais(larguraealtura)deumdis-
positivo.
•DevicePixelRatio—permitequesejaemuladoumdispositivocomtela“re-
tina”apartirdeumdispositivo“não-retina”.Oquequerdizerquealgumas
mediaqueries,taiscomo @media (min-resolution: 2dppx)podemser
testadas.
•Emulateviewport—aplicaumzoomoutaoviewportfísicopadrãododispo-
sitivo.
•T e x tautosizing—emulaalgumasmudançasnarenderizaçãodafonteefetu-
adasporalgunsdispositivosmóveis,afimdemelhoraralegibilidade.
188

## Página 197

CasadoCódigo Capítulo10.DebugandosuaW e bApp—ou,Comoseestressarmenos
•Androidfontmetrics—oAndroidaumentadeformaartificialotamanhoda
fontedeacordocomalgumasconfiguraçõesdesistemaetamanhodetela.Esta
opçãoéhabilitadaporpadrãoapenasquandoseestáemulandodispositivos
Android.
Porpadrão, oDevT o o l sjávempré-carregadocomconfigurações dosdispo-
sitivosmóveismaispopularesatualmente.Escolhendoumdispositivodalista,ele
irápopularasoutrasabas(Us e rAgent,Screen,entreoutras)comasconfigurações
específicasdodispositivoescolhido.
Figura10.23:Selecionandodispositivoaseremulado
Casodesejeemularumdispotivonãolistado,épossíveleditaroscamposindi-
vidualmentecomasespecificações doaparelhodesejado.
Emulandoeventostouch
T e rquesubirumamodificaçãoparaumservidoredarrefreshnapáginadoseu
dispositivomóvelpodeserumsaconahoradedesenvolveralgorelacionadocom
touchevents,umasvezqueamaioriadosdesktopsnãopossuemessetipodeinput.
Paraeventosdotiposingle-touch(feitosapenascomumdedo),épossívelsimulá-
lospeloDevT o o l s .NopainelEmulation,váparaaabaSensorsehabiliteocheckbox
Emulatetouchscreen,comonafiguraaseguir.
189

## Página 198

10.3.Emulandodispositivosmóveis CasadoCódigo
Figura10.24:Emulandotouchevents
Seumouseirávirarumacírculo,simulandoapontadeumdedo.U mcliquedo
mouseirádispararoseventostouch.Parasimularumpinch,aperte Shifte,com
obotãodomousepressionado,movaoponteiro.
SpoofingdeU s e rAgent
OUser-agentéumastringqueidentificaobrowser—agente.Estastringépas-
sadanocabeçalhodetodarequisição aoservidorealgumasaplicações fazemuso
dessaformadeidentificaronavegadorparaservirumconteúdootimizado.
NoDevT o o l s ,épossívelalterarestastringfazendocomqueonavegadorse“dis-
farce”deumoutro. Comodraweraberto,vánopainelEmulation,naabaUs e r
AgenteescolhaoUs e rAgentdeumdispositivoouentrecomumespecífico,como
nafiguraaseguir.
Figura10.25:SpoofingdeUseragent
U mdoswebsitesquefaztaltipodedetecçãoéogoogle.com.Façaumspoofingde
Us e rAgentdoiPhoneetentevisitarogoogle.com.U mnovapáginaserárenderizada.
190

## Página 199

CasadoCódigo Capítulo10.DebugandosuaW e bApp—ou,Comoseestressarmenos
Sobreescrevendogeolocalização
Imaginequeumusuáriodesuaaplicaçãoreporteumbugaotentarprocurarpor
restaurantesnacidadedoRiodeJaneiro.V o c êmoraemSãoPauloesuaaplicação
recebeessesdadospelaAPIdeGeolocalizaçãododispositivo.Comosimularoce-
náriodousuárioquereportouobugeverificarquaisasrepostasdaaplicação no
contextodacidadedoRio?
Essainformaçãotambémpodesersobreescritaparafinsdedebugarcódigo.No
drawer,váparaopainelEmulation,naabaSensorsehabiliteocheckboxEmulate
geolocationcoordinatesinformandoalatitudeelongitudequevocêdesejapassar
emular,comonafiguraaseguir.
Figura10.26:Sobreescrevendogeolocalização
Emulandoacelerômetro
Computadoresdesktopeamaiorpartedosnotebooksnãopossuemacelerôme-
tro.Aausênciadessesensorpodetornarimpossívelotestedeumcódigoqueacesse
osdadosdeaceleraçãododispositivo.MascomoDevT o o l sépossívelemulá-los(ou
sobrescreverseuvalor).Paraisso,váaodrawer,depoisnaabaEmulationecliqueno
checkboxAccelerometer.V o c êpodemexerarepresentação3Ddodispositivopara
emularumadeterminadaposiçãoouporvaloresdiretamenteemcadaeixo.
191

## Página 200

10.4.Debugremoto CasadoCódigo
Figura10.27:Emulandoacelerômetro
10.4 Debug r e m o t o
Emulardispositivosemnossoambientededesenvolvimentoéumsalvadordevi-
das.Masjáimaginousepudéssemosdebugarnodesktopumwebsiterodandoem
nossocelular?Seriaomelhordosdoismundos.Avelocidadedodesenvolvimento
nodesktopcomafidelidadedarenderizaçãodeumdispositivoreal,enãoemulado.
Poisnossossonhosviraramrealidade.Hoje,comumdispositivorodandooAn-
droid4.0+eChrome,épossívelconectarumDevT o o l srodandoemseudesktopao
browserrodandonocelular.
Habilitandoomodo developeremseuAndroid
Parausarodebugremoto,primeirosedevehabilitaraopçãoUSBdebuggingno
seuAndroid.
NoAndroid4.2+omenuDeveloperoptionsestádesabilitadoporpadrão.Para
habilitá-lováemSettings,depoisemAboutphoneeclique7vezesemBuildnum-
ber(ésério...).V o l t eparaatelaanterior,cliqueemDeveloperoptionsehabiliteo
USBDebugging.NoAndroid4.0e4.1,aopçãoUSBDebuggingestáemSettings
>Developeroptions.
192

## Página 201

CasadoCódigo Capítulo10.DebugandosuaW e bApp—ou,Comoseestressarmenos
Figura10.28:ConfiguraçãodadepuraçãoUSBnoAndroid
Debugandonodesktop
HojeoChromedesktopsuportadeformanativaodebugemdispositivosconec-
tadosporUSB,semmaisoantigoestressedeterquebaixar,instalareconfiguraro
ADB(AndroidDebugBridge).
OpróximopassoagoraéhabilitarodebugremotonoChromedesktop.V i s i t ea
páginachrome://inspect/#devicesehabiliteocheckboxDiscoverUSBdevices,como
nafiguraaseguir.
193

## Página 202

10.4.Debugremoto CasadoCódigo
Figura10.29:DescobertadedispositivosconectadosporUSB
AgoraconecteseudispositivoAndroidaocomputadorpelocaboUSB.U m a
mensagememseuAndroiddeveaparecerperguntandosedesejahabilitarodebug-
gingpelaUSB.Digaquesim.
Figura10.30:ConfiguraçãodadepuraçãoUSBnoAndroid
A p ó sisso,seuaparelhoserálistadonoendereçochrome://inspect/#devices.
Nesteendereço,sãolistadostodososaparelhosconectadosesuasrespectivastabs.
194

## Página 203

CasadoCódigo Capítulo10.DebugandosuaW e bApp—ou,Comoseestressarmenos
Podemosterváriosaparelhosconectadosaummesmocomputador,assimcomová-
riasWebViews.EscolhaqualtabquerdebugarecliqueemInspect.
U m anovajanelairáaparecercomoqueridoDevT o o l seum“espelho”datela
doaparelhoqueestamosdebugando. Esteespelhodoaparelhotambéméintera-
tivo.Podemos,porexemplo,rolarapágina,clicareusarnossotecladodesktoppara
entrarmoscomdadosdeumaformamaisrápida.
Figura10.31:Páginawebrodandoemumdispositivomóvelesendodebugadano
DevT o o l snodesktop
Agorajápodemoscomeçaradebugarnossaaplicação.ComomomentoWTF?!,
vánaabaInspectdoDevT o o l seinspecioneumelemento.Repareque,deacordo
comqueomousepassasobreoHTMLdoselementosnoDevT o o l s ,elesficammar-
cadoscomumoverlayazulemseuAndroid.Assimcomoacontecequandoinspe-
cionamosumelementoemumapáginasendorenderizadalocalmente.
Apartirdessemomento,vocêtemumDevT o o l scompleto,acessandoumapá-
ginasendorenderizadaemumdispositivoreal,enãoemulado.
195

## Página 204

10.4.Debugremoto CasadoCódigo
Redirecionamentodeporta
Normalmente,temosumservidorlocalrodandoemnossamáquinaduranteo
desenvolvimento.Parafazercomqueoseucelularfaçaumarequisiçãoaoservidor
queestárodandonamáquinadedesenvolvimentobastadigitaroIPdamáquinade
desenvolvimentoeaportaondeoservidorestáescutando.
Issocasoambosaparelhosestejamnamesmarede,oquenemsempreéverdade.
Como,porexemplo,emredescorporativasquegeralmentesãocheiasderestrições.
Parafacilitaresseworkflow,oDevT o o l ssuportaoredirecionamentodeportas.
Comisso,podemosfazercomqueodispositivoconectadoporUSBacesseumaporta
nocomputadoraoqualestáconectado,mesmoestandoemredesdiferentes.
Figura10.32:SitedaCaelumrodandonoservidordedesenvolvimentosendoaces-
sadoporumdispositivomóvelatravésderedirecionamentodeporta
Parahabilitaroredirecionamento,sigaospassos:
1)Abraoendereçochrome://inspect/#devices;
196

## Página 205

CasadoCódigo Capítulo10.DebugandosuaW e bApp—ou,Comoseestressarmenos
2) CliquenobotãoPortforwarding;
3)NocampoPort,digiteaportaemqueodispositivodeveráescutar;
4) NocampoIPaddressandportdigiteoIPmaisportaemqueseuservidorestá
rodando;
5)HabiliteocheckboxEnableportforwardingantesdeapertarDone.
10.5 Dicase truques
“ A n t e sdeumsoftwareserreutilizável,eleprecisaprimeiroserusável.”
–RalphJohnson
ODevT o o l sérepletodefunções eferramentas.Masalgumasdelasnãosãotão
óbviasdeseremachadas. Nestecapítulovamosfocarjustamentenessasfunciona-
lidades: nasmenoscomuns. MesmovocêjásendoumratodoDevT o o l s ,muito
provavelmenteiráaprenderalgunsnovotruquesdepoisdeleressecapítulo.
Procurandotextoentretodososarquivoscarregados
U mdosatalhosquemaisuso. Eleprocuraporumtextoouexpressãoregular
entretodososarquivoscarregadospelosite.Inclusive—eporissoeleétãoútil—
entrearquivosqueforamcarregadosemtempodeexecução.
CasoestejanoOSX,utilizeasteclas command+ option+ Fparadispararo
paineldebusca.NoWindowseLinux,omesmoédisparadocomasteclas Ctrl+
Shift+ F.
Figura10.33:Procurandotextoentretodososarquivoscarregados
197

## Página 206

10.5.Dicasetruques CasadoCódigo
Forçandoumestadoemumelemento
Játentouinspecionarumelementonoseuestadode hovere,quandovocêmove
seumouseparaoDevT o o l s ,oelementoperdeoestadode hoverevocênãosabe
maisoquefazerouquemxingar?
NoChrome,épossívelforçarumestadoemumelemento,sejaele active,
focus, hoverou visited.NaabaElements,inspecionenormalmenteoelemento
e,comeleselecioanado,cliquenoíconequeficaàdireitanapartedecimadoDev
T o o l seescolhaoestadoquedesejaforçarnoelementoselecionado.
Figura10.34:Forçandoumestadoemumelemento
ContadordeFPS
Útilparavisualizar,emtemporeal,oframeratedesuaaplicação.Quandoativo,
iráaparecerumacaixapretanotopoàdireitacomdetalhessobreaquantidadede
framesqueestãosendorenderizadosporsegundo.Paraumaexperiênciaótima,tente
sempreficaracimade60FPS.
198

## Página 207

CasadoCódigo Capítulo10.DebugandosuaW e bApp—ou,Comoseestressarmenos
Figura10.35:ContadordeFPS
Ainformaçãoéútilparavocêmonitoraraperformancederenderizaçãodosite.
SitescombaixoFPSparecemteranimações menossuaveseperformancepior.
ReplaydechamadasXHR
Jápensouterquerefazersempreaquelefluxoenormenasuaaplicaçãosópara
dispararnovamenteumacertarequisiçãoA j a x(XHR)?Comesseatalho,vocêpode
darumreplayemqualquerchamadaAjax.
199

## Página 208

10.5.Dicasetruques CasadoCódigo
Figura10.36:ReplaydechamadasXHR
CopiandorequisiçõescomocomandocURL
PraticamenteumaderivaçãodoreplaydechamadasAjax.Comadiferençade
que,aqui,égeradoumcomandocURLdarequisiçãofeitacomtodososparâmetros
ecabeçalhos. Colenoseuterminaleaperte enterparadispararumarequisição
idênticaàquefoidisparadapeloseunavegador.
Figura10.37:Copiandorequisições comocomandocURL
T r o q u erapidamenteentreabas
ParanavegardeformarápidaentreasabasdoDevT o o l s ,utilize Cmd+ [e Cmd
+ ](ou Ctrl+ [e Ctrl+ ]noWindowseLinux).
200

## Página 209

CasadoCódigo Capítulo10.DebugandosuaW e bApp—ou,Comoseestressarmenos
Preservaro logdoconsoledurantenavegação
Sabequandovocêquerdebugaralgoqueaconteceumpoucoantesdeumredirect
masestemesmoredirectapagaologdoconsole?Pararesolveresseproblema,clique
comobotão direitonoconsoleeescolhaaopçãoPreserveloguponnavigation.
SeuslogsnãoserãomaiszeradosaovisitarumaoutraURL.
Figura10.38:Preservarologdoconsoledurantenavegação
Limpandoohistóricodoconsole
BastanteútilquandosecomeçaausarcommaisfrequênciaaabaConsole. Cmd
+ KnoOSXe Ctrl+ LnoWindowseLinuxparalimparoconsole. T a m b é m
funcionacomométodoconsole.clear().
CompartilhareanalisarumaTimelinegravadaporoutro
Imaginequevocêestácomumbugnarenderizaçãodasuaaplicaçãoqueaestá
deixandocomumaexperiênciaruim,comoseoscrollestivessepesado.Entãovocê
gravaumasessãocomaferramenteTimelinee,mesmoassim,nãoconsegueiden-
tificaroerroegostariamuitodeenviarestamesmasessãorecém-gravadaparaum
amigodesenvolvedorlheajudarnoprocessodedebug.
Hojeissoépossível.T a n t oexportarcomocarregarumasessão exportadapor
umterceiro.U m aveznaabaTimeline,cliquecomobotãosecundáriodomouse
dentrodaabaeescolhaaopçãoSaveTimelineData...parasalvarasessãoatuale
LoadTimelinedata...paracarregarumasessão.
201

## Página 210

10.6.Extensões CasadoCódigo
Figura10.39:CompartilhareanalisarumaTimelinegravadaporoutro
10.6 Extensões
“Computadoressãobonsemseguirordens,masnãoemlermentes.”
–DonaldKnuth
Existemváriasextensões paraoDevT o o l squepodemmelhoraraindamaiso
processodedebugdealgunsworkflowsespecíficos.Aseguir,apresentoalgumasóti-
masextensões paraosmaispopularesframeworks,paraotimização deummodo
geraleparamelhordebugararquivosnoambientedeprodução.
AngularJSBatarang
ExtendeoDevT o o l scomferramentasespecíficasparaoframeworkAngularJS.
202

## Página 211

CasadoCódigo Capítulo10.DebugandosuaW e bApp—ou,Comoseestressarmenos
Figura10.40:AngularJSBatarang
EmberInspector
U m aótimaextensãoparaquemtrabalhacomoframeworkEmber.Comeleé
possívelvertodasasrotassendousadas,assimcomoumoverlaycomquaistemplates,
controllersemodelsestãosendousadosemtempodeexecução.
203

## Página 212

10.6.Extensões CasadoCódigo
Figura10.41:EmberInspector
BackboneDebugger
Mostra,emtemporeal,todasasviews,models,collectionseroutersusadaspor
suaaplicaçãoqueutilizaoframeworkBackbone.
204

## Página 213

CasadoCódigo Capítulo10.DebugandosuaW e bApp—ou,Comoseestressarmenos
Figura10.42:BackboneDebugger
GruntDevtools
RodetodassuastarefasdoGruntsemsairdobrowser.
205

## Página 214

10.6.Extensões CasadoCódigo
Figura10.43:GruntDevtools
RailsPanel
ÉparaquemtrabalhacomRubyonRails.Mostrainformações desuaapptais
comotempogastoemcadarequisiçãoetempototaldecadaqueryaobancodedados.
206

## Página 215

CasadoCódigo Capítulo10.DebugandosuaW e bApp—ou,Comoseestressarmenos
Figura10.44:RailsPanel
DevtoolsRedirect
ODevtoolsRedirectpermitequeumarequisiçãofeitapelobrowsersejaredireci-
onadaparaumarquivolocalemsuamáquina.Baixeoarquivoqueestáemprodução,
façasuasalterações localmente,eredirecionearequisiçãoparaestearquivoemsua
máquina.Agoratodavezqueoarquivoforcarregado,asuacópialocalqueserácar-
regada.Ótimo parafazertestesnoambientedeproduçãoquenãoiráimpactarnos
usuáriosfinais.
PageSpeedInsights
EstaextensãofeitapeloGooglenosdádicas—maisaprofundadasqueasdaaba
AuditsdoDevT o o l s—sobrecomoeondemelhoraravelocidadedecarregamento
denossaaplicação.
10.7 Conclusão
“Suponhoquesejatentador,seaúnicaferramentaquevocêteméummartelo,tratar
tudocomosefosseumprego.”
207

## Página 216

10.7.Conclusão CasadoCódigo
–AbrahamMaslow,1966
ODevT o o l séaferramentadedebugdoChromee,emminhahumildeopinião,
hojeamelhorferramentaparadebugdeumaaplicaçãoweb.Porém,ocódigodesua
aplicação deverodarnão apenasemumbrowser,masemquantosforpossível.E
bugsirãoeventualmenteaparecernomomentoemquevocêfortestarsuaaplicação
emdiferentesnavegadores.Logo,étambémnecessário—pelomenos—conheceras
ferramentasdedebugdestesoutrosbrowsers.OW e bInspectordoSafari,oFirebug
eDeveloperT o o l sdoFirefoxsãotambémótimasferramentasenãotãodiferentes
assimdasquevimosnestecapítulo.
Paraseaprofundarmaisnoassunto,aconselhoaleituradosseguintesmateriais:
•ChromeDevT o o l s:https://developers.google.com/chrome-developer-tools/
•SafariW e bInspector:http://bit.ly/1d7Livt
•FirefoxDeveloperT o o l s:https://developer.mozilla.org/en/docs/Tools
Porémdebugarumaaplicaçãonãosetrataapenasdeferramentas.Énecessário
experiênciaparasaberporondecomeçar.Apenasencherseucódigodebreakpoints
semnenhumpropósitonãovaiajudararesolverumbug.Éprecisodesconfiarda
coisacerta.Eesteknow-howsóotempoirátedar.
208

## Página 217

CasadoCódigo Capítulo10.DebugandosuaW e bApp—ou,Comoseestressarmenos
Sobre o autor
CaioGondiméumdesenvolvedorfull-stackex-Globo.com,atual-
mentetrabalhandonaBooking.com, recém-chegadoemAmsterdam.
Interessadoemviagens,minimalismo,interfacehomem-máquinaees-
tilodevidaemgeral.T a m b é mépalestranteecofundadordoblogloo-
pinfinito.com.br,ondeescrevesobreasmaisnovastecnologiasdomundo
front-end.V o c êpodesegui-lonoT w i t t e rem@caio_gondim.
209

## Página 219

Capítulo11
TestandocódigosJavaScript
11.1 Introdução
OJavaScripté,semsombradedúvida,alinguagemdeprogramaçãomaisutilizada
nodesenvolvimentodesiteseaplicações web.Emfevereirode2014,noGithub,dos
50repositórioscommaiornúmerodestars,25eramfocadosemJavaScript.Apossi-
bilidadedeusá-loparamanipularoDOM,fazerrequisições assíncronaseescrever
códigosexecutáveisnoladodoclientefezcomqueosprogramadoresmudassema
mentalidadeemrelaçãoaodesenvolvimentoparaaweb.
ComoavançodasAPIsdisponibilizadaspelosnavegadoreseoaumentodacom-
patibilidadeentreeles,alinguagemcriadapeloBrendanEichem10diaspossibilitou
aosdesenvolvedoresacriação deinterfacesricas,complexas,ealtamenteinterati-
vas.Em2004,oGooglelançouoGmail—ummarconousodetecnologiasweb—,
egraçasaosurgimentodeframeworkscomoojQuery,smartphonescombrowsers
modernoseaousocadavezmaioremservidores,oJavaScriptconquistouaposição
delinguagemdeusomaisubíquo.

## Página 220

11.2.Osbenefíciosdetestarumaaplicação CasadoCódigo
Mascomocrescimentodeseuuso,veioocrescimentodacomplexidadedocó-
digoescritoedoriscodequebrarofuncionamentodeumaaplicaçãoacadalinha
alterada.Comoimplementarumasoluçãocomumbomdesignegarantirquealte-
rações emumtrechonãoinfluenciem(ouquebrem)outraspartes?
Nomundododesenvolvimentodesoftware,essesemprefoiopapeldostestes.
Nesteartigo,vamosvercomoaplicá-losaoJavaScript,garantindoumaaplicação
resiliente,defácilmanutenção,efácildesermodificadaeadaptada.
11.2 Os benefíciosde testar u m a aplicação
Imagineaseguintesituação: vocêprecisaimplementarumformuláriodedadosde
cartãodecréditoparaume-commerce.Aosubmetê-lo,umavalidaçãonoladodo
clientedeveverificarse:
•onomefoipreenchido;
•onúmerofoipreenchido;
•onúmeroéválidoparaocartãodabandeiraA;
•adatadevalidadeéválida;
•ocódigodesegurançafoipreenchido;
•ocódigodesegurançaéválido.
Asespecificações parecemsersimplesosuficienteparaavalidação serimple-
mentadasemqualquerpreocupação comtestes. Semperdertempo,vocêescreve
umafunçãoquerealizatodasasverificações. A p ó stestarextensivamentenonave-
gador,vocêconsideraqueestátudobememandaocódigoparaprodução.
Imagineque,semanasdepois,osistemadepagamentopasseasuportaroscar-
tões dabandeiraB.ComoavalidaçãosuportaapenasabandeiraA,vocêdevealterar
ocódigoparasuportarambas.Porém,dependendodamaneiracomoaimplemen-
taçãofoifeita,aadiçãodabandeiraBpodepotencialmenteafetarofuncionamento
deoutraspartesdoformulário.
Comogarantirquetudocontinuafuncionandocorretamente?Ese,nofuturo,
foremadicionadasmaisbandeirasdecartãodecrédito?Eseelasinfluenciaremcomo
ocódigodesegurançaéverificado?EseabandeiraApassarasuportarumnovo
formatodenúmeros?
212

## Página 221

CasadoCódigo Capítulo11.TestandocódigosJavaScript
Emume-commerce,apartedafinalizaçãodacompraéumadasmaiscruciais
paraonegócio.U mpequenoerropodequebrarofuncionamentodapáginaecausar
umaperdasubstancialdedinheiro—tantoemvendas,quantonafidelizaçãodocli-
ente.Infelizmente,independentedotipodaaplicação,bugsfazempartedoprocesso
dedesenvolvimento.Eéamaneiracomotestamosasfuncionalidadesquedefinea
quantidadeeagravidadedelesnahoradeousuáriofinalinteragircomosite.
Asdiferentescamadasdeteste
Existemdiferentesformasdesetestarumaaplicaçãoecadaumacobrediferen-
tespartesecamadas.Nãoexisteumaformaúnicaouidealdeaplicá-lasecadapro-
jeto/timepodenecessitardiferentesmétodosecombinações.
Figura11.1:Asdiferentescamadasdeteste
•Testesunitários:testamasmenorespartesdaaplicação—módulos,fragmen-
tosdecódigo,funções —isoladamente.
•Testesdeintegração:testamaintegraçãoentrediferentesmódulosepartesdo
sistema.Emaplicações web,podemtestaracomunicaçãoentrecomponentes
emumamesmapágina,ouumafeatureespalhadaentrediferentesseções.
213

## Página 222

11.3.Escrevendoostestesunitários CasadoCódigo
•Testesdeaceitação:usadosprincipalmenteemambienteságeis,testamoscri-
tériosdeaceitedeumaestória/featureporcompleto. Atravésdeferramen-
tascomooCucumber(http://cukes.info/),osstakeholdersprimários(comoo
ProductOwner)podemserenvolvidosnoprocessodecriaçãodoteste.
•Testesdesistema:testamasfeaturesmaiscruciaisparaofuncionamentodo
site,depontaaponta.U mexemploseria,emume-commerce,ofluxodebus-
carporumproduto,adicioná-loaocarrinho,preencherosdadosdeentregae
pagamento,efinalizarumacompra.
ComoestamosfocadosnoJavaScript,falareiapenassobreostestesunitários.
11.3 Escrevendo os testes unitários
ParaescrevertestesparaocódigoJavaScript,precisaremos:
•escolherumframeworkdetestes;
•saberoqueéecomoescreverumaspec;
•organizarasspecsemgrupos;
•executarostesteseanalisarosresultados.
Existemdiferentesopções deframeworkediferentesformasdeusá-los.Aqui,
usaremosoJasmine,daPivotalLabs(http://jasmine.github.io/).Porém,apósapren-
derosprincipaisconceitossobrecomoescrevertestes,vocêveráqueésimplesaplicá-
losemdiferentesferramentas.
Montandooambiente
V a m o sutilizaraversão"Standalone”doJasmine:amaissimples,indicadapara
pequenosprojetosoubibliotecas. Maisparafrente,dareialgumasdicasdecomo
utilizá-loemaplicações maiores.
Entre na páginado projeto (https://github.com/pivotal/jasmine/tree/master/
dist),baixeedescompacteozipdaversãomaisrecente.Naversão2.0.0,essaéa
estruturadodiretório:
214

## Página 223

CasadoCódigo Capítulo11.TestandocódigosJavaScript
/jasmine-standalone-2.0.0
/lib
MIT.LICENSE
/spec
PlayerSpec.js
SpecHelper.js
SpecRunner.html
/src
Player.js
Song.js
Nomomento,oquenosinteressaéoarquivo SpecRunner.htmleoconteúdo
dosdiretórios spece src.
Abraoarquivo SpecRunner.html.V o c êveráalgoassim:
Figura11.2:SpecRunner.html
V o c êacabaderodartestesJavaScriptnoseunavegador!Claro,sãoapenasexem-
plosprontos,masver"5specs,0failures”jánãodáumânimo?
Agoraabrao SpecRunner.htmlnoseueditordecódigofavorito.V o c êverá
umapáginaHTMLincluindoumarquivoCSSealgunsarquivosJavaScript.Nofinal
dobloco <head>,háestetrechodecódigo:
<!-- include source files here... -->
<script src="src/Player.js"></script>
<script src="src/Song.js"></script>
215

## Página 224

11.3.Escrevendoostestesunitários CasadoCódigo
<!-- include spec files here... -->
<script src="spec/SpecHelper.js"></script>
<script src="spec/PlayerSpec.js"></script>
Ocomentáriojádáadica:vocêdeveráincluirseusmódulos/bibliotecasaserem
testadose,emseguida,osarquivoscontendoostestes.
Apagueoconteúdodoarquivo spec/SpecHelper.js,apagueosarquivos
src/Player.js, src/Song.jse spec/PlayerSpec.jse,noHTML,deixe
apenasachamadaao SpecHelper.js:
<!-- include source files here... -->
<!-- include spec files here... -->
<script src="spec/SpecHelper.js"></script>
O SpecHelper.jsdeveráconterquaisquerhelpersemétodosquevocêqueira
criarparaauxiliá-lonofuturo.Casonãoprecise,eletambémpodeserremovido.
Agoraestamosprontosparaescrevernossostestes.Comoexemploprático,va-
mosimplementaroformuláriodecartão decréditoqueciteianteriormente.Mas,
primeiramente,énecessárioconhecerosconceitosdespecesuite.
Oqueéumaspec?
Desdequedescompactamosoarquivozip,vocêdeveternotadoapalavraspec
emdiversoslugares.Oqueéumaspec,eoqueelatemavercomtestes?
U m aspecécomosefosseamenor“unidade”deumteste.Elapossuiumades-
crição —umafrasecurtaindicandooqueestásendotestado—eumaoumais
asserções —umacomparaçãoentreexpectativaeresultadoqueretorna trueou
false. Quandotodasasasserções são verdadeiras,aspecpassacomsucesso.Se
algumadelaséfalsa,aspecfalha.
Asasserções possuemtrêspartes:aprimeiraéovaloraseranalisado,chamado
de“valorreal”,asegundaéovalorquequeremos,chamadode“valoresperado”,ea
terceiraéacomparaçãoqueseráfeitaentreosdoisvalores.
Spec: Deve ter a cor azul
Asserção: O estilo ’color’ de .meu-paragrafo deve ser igual a ’blue’
Noexemplo,temos:
•V a l o rreal:Oestilo‘color’de.meu-paragrafo
216

## Página 225

CasadoCódigo Capítulo11.TestandocódigosJavaScript
•V a l o resperado:‘blue’
•Comparação:deveseriguala
Éimportantequeadescriçãodaspecnãosejamuitogenérica.Nocasodonosso
formuláriodecartão decrédito,umaspeccomadescrição “ d e v evalidarcorreta-
mente”acabarápossuindomuitasasserções. Casoumadelasfalhe,aspecinteirafa-
lharáeserámaisdifícilidentificaroproblema.Quebrarostestesemspecsgranulares
tambémgarantiráummelhordesigndecódigo:cadapequenapartedocomponente
seráimplementadaetestadaisoladamente.
Oqueéuma suite?
Asspecssãoagrupadasporcontextos,chamadasdesuites.U m asuitepodecon-
terumconjuntodesuites—quepodemconteroutrassuites—eumaoumaisspecs.
Suite: Meu parágrafo
Suite: Estilos
Spec: Deve ter a cor azul
Spec: Deve ter a fonte Helvetica
Suite: Conteúdo
Spec: Deve conter o texto ’Hello world!’
Geralmente,cadacomponenteérepresentadoporumasuitedemesmonome,
queporsuavezécompostaporoutrassuitesrepresentandodiferentespartesdesua
implementação,cadaumacomseuconjuntodespecs.
Criandoseuprimeiroteste
Quandodescrevioexemplodoformulário,listeiváriasespecificações. Cadauma
delaséelegívelparaserumaspecseparada.Algumaspodemserquebradasematé
duasoumaisspecsdistintas.Relembrando,ocomponentedeveráverificarse:
•onomefoipreenchido;
•onúmerofoipreenchido;
•onúmeroéválidoparaocartãodabandeiraA;
•adatadevalidadeéválida;
•ocódigodesegurançafoipreenchido;
217

## Página 226

11.3.Escrevendoostestesunitários CasadoCódigo
•ocódigodesegurançaéválido.
Paracomeçarnomundodostestes,pegareioprimeiroexemplodalista.Crieo
arquivo validadorCartaoDeCreditoSpec.jsnodiretório speceoincluano
SpecRunner.html:
<!-- include source files here... -->
<!-- include spec files here... -->
<script src="spec/SpecHelper.js"></script>
<script src="spec/validadorCartaoDeCreditoSpec.js"></script>
NoJasmine,assuitessãorepresentadaspelafunção describe.Oprimeiroar-
gumentoéadescriçãodasuiteeosegundoéumafunçãoquerepresentaoblocode
implementaçãodasuite.Esseconceitoficarámaisclaroàmedidaqueimplementar-
mosasspecs.
Abraoarquivo validadorCartaoDeCreditoSpec.jseincluaasseguintes
linhas:
describe("validadorCartaoDeCredito", function () {
});
Salveoarquivoeabrao SpecRunner.htmlnonavegador.V o c êacabadecriar
erodarsuaprimeirasuitedetestes!
Figura11.3:Nossaprimeirasuitedetestes
Mas,nomomento,elanãoestátestandonada.V a m o scriarnossaprimeiraspec.
Elassãodefinidasatravésdafunção ite,assimcomoafunção describe,aceitam
comoargumentosumadescriçãoeumafunçãoqueimplementaaspec:
describe("validadorCartaoDeCredito", function () {
it("valida que o nome é mandatório", function () {
218

## Página 227

CasadoCódigo Capítulo11.TestandocódigosJavaScript
});
});
Aosalvaroarquivoerecarregarapágina,vocêveráqueelelistaráaspecein-
dicaráqueelapassoucomsucesso. Comonão escrevemosnenhumaasserção,ele
assumequetudodeucerto.
Figura11.4:Nossaprimeiraspec
Comovimosantes,umaasserçãoécompostapelovalorreal,pelovaloresperado
epelacomparaçãoentreambos.NoJasmine,issoéescritoatravésdafunção expect
edosmatchers.Modifiqueaimplementaçãodaseguinteforma:
describe("validadorCartaoDeCredito", function () {
it("valida que o nome é mandatório", function () {
var nome = "";
expect(validadorCartaoDeCredito.validaNome(nome)).toEqual(false);
});
});
Opa,tembastantecoisaacontecendoaqui!Deondesaiuesse validaNome?E
esse toEqual?V a m o sporpartes:
•Afunção expectéoquedefineaasserçãonoJasmine.Elaaceitacomoparâ-
metroovalorreal,ouseja,aquelequequeremosgarantirqueestáfuncionando
corretamente.
•Afunção toEqualéummatcher—funções queservemparacompararva-
lores.NocasodoJasmineedeoutrosframeworks,elefuncionanaformade
chain,sendochamadoimediatamentedepoisdeoutrafunção.Omatcherirá
219

## Página 228

11.3.Escrevendoostestesunitários CasadoCódigo
compararovalorpassadoparaafunção expectcomovalorpassadopara
ele. Cadaumpossuiumacomparaçãodiferenteefacilmentededuzívelpelo
nome—o toEqualcomparaseosvaloressãoiguais.
•O validadorCartaoDeCreditoeseumétodovalidaNomeaindanão
existem.Énessepontoqueostestespodemmelhorareatémesmodefiniro
designdasuaimplementação.Tendoasdescrições dasspecsdefinidas,pode-
moscomeçara“prever”comonossocódigoseráutilizado,antesmesmodeele
serimplementado.Onomedissoé"BehaviorDrivenDevelopment”(Desen-
volvimentoMovidoaComportamento)—ouBDD—quedescrevereicom
maisdetalhesposteriormente.
Aorecarregaro SpecRunner.html,vocêveráquefinalmentetemosumerro:
"ReferenceError:validadorCartaoDeCreditoisnotdefined”.
Figura11.5:Erro:ovalidadorCartaoDeCreditoaindanãofoidefinido
Como nem implementamos o validadorCartaoDeCredito,
esse era o resultado esperado. V a m o sfazê-lo: crie o arquivo
validadorCartaoDeCredito.js no diretório src e inclua-o no
SpecRunner.html:
220

## Página 229

CasadoCódigo Capítulo11.TestandocódigosJavaScript
<!-- include source files here... -->
<script src="src/validadorCartaoDeCredito.js"></script>
<!-- include spec files here... -->
<script src="spec/SpecHelper.js"></script>
<script src="spec/validadorCartaoDeCreditoSpec.js"></script>
Abraoarquivoedefinao validadorCartaoDeCredito:
var validadorCartaoDeCredito = {
};
Recarregueo SpecRunner.htmlnonavegador.V o c êveráqueamensagemde
erromudoupara"TypeError:Object #<Object>hasnomethod‘validaNome”’.
Figura11.6:Erro:ovalidadorCartaoDeCreditonãopossueométodovalidaNome
Os erros indicam justamente o nosso próximo passo: criamos o
validadorCartaoDeCredito,agoraprecisamoscriarométodovalidaNome:
var validadorCartaoDeCredito = {
validaNome : function () {
221

## Página 230

11.3.Escrevendoostestesunitários CasadoCódigo
}
};
Agoraamensagemmudarápara"Expectedundefinedtoequalfalse”. Como
validadorCartaoDeCredito.validaNome()não retornanada(ouseja,re-
torna undefined),otestefalha.
Figura11.7:Erro:undefineddeveriaserfalse
Aintençãonãoéfazerotestepassar?Esefizermososeguinte?
var validadorCartaoDeCredito = {
validaNome : function () {
return false;
}
};
222

## Página 231

CasadoCódigo Capítulo11.TestandocódigosJavaScript
Figura11.8:Otestepassou.Masaimplementaçãoestácorreta?
Emboraaimplementação estejacompletamenteerrada, otestepassou, pois
false === falseéverdadeiro.Criamosumtesteinútil?T e s t a réperdadetempo?
Paraevitarisso,bastacomeçarmosasermaiscriteriososecriarmaisspecs.Nossa
suitepodesermelhoradadaseguintemaneira:
describe("validadorCartaoDeCredito", function () {
describe("ao validar o nome", function () {
it("returna true se o nome não estiver em branco", function () {
var nome = "Shiota";
expect(validadorCartaoDeCredito.validaNome(nome)).toEqual(true);
});
it("returna false se o nome estiver em branco", function () {
var nome = "";
expect(validadorCartaoDeCredito.validaNome(nome)).toEqual(false);
});
});
});
223

## Página 232

11.3.Escrevendoostestesunitários CasadoCódigo
Figura11.9:Erro:agoraumadasspecsfalha
Agoraumadasspecsiráfalhareseremosobrigadosacorrigirnossaimplemen-
tação:
var validadorCartaoDeCredito = {
validaNome : function (nome) {
return nome !== "";
}
};
Aorecarregarapáginacomostestes,todospassarão.
224

## Página 233

CasadoCódigo Capítulo11.TestandocódigosJavaScript
Figura11.10:T o d a sasspecsestãoverdes!
Agora,imaginequeocódigoestáfuncionandoefoiparaoar,ealguémconseguiu
burlaravalidaçãodonomecolocandoumespaçoembranconocampodetexto.
Antesdecorrigiroerrodesesperadamente,pormaisurgentequeseja,abraseu
arquivodetesteseadicioneumaspecparatestaressecaso:
it("retorna false se o nome é um espaço em branco", function () {
var nome = " ";
expect(validadorCartaoDeCredito.validaNome(nome)).toEqual(false);
});
225

## Página 234

11.3.Escrevendoostestesunitários CasadoCódigo
Figura11.11:Anovaspecpegouumafalhanaimplementação
E não é que falhou mesmo? V a m o scorrigir no
validadorCartaoDeCredito.js:
var validadorCartaoDeCredito = {
validaNome : function (nome) {
return nome.trim() !== "";
}
};
Pronto.Pazrestauradaeaspecadicionadagarantiráqueessebugnuncamais
passarábatido.
DesenvolvendocomBDD/TDD
Comovimosanteriormente,épossívelescreverostestesantesmesmodeim-
plementarasolução. Avantagemdissoéque,tendoemmãosasespecificações eo
resultadoquequeremos,podemosdeantemãoprojetareprevercomoseráodesign
daimplementação.
Existemduastécnicasparaisso:oBDD,queusamosparaescrevernossaspecdo
validadordecartãodecrédito,eoTDD—T e s tDrivenDevelopment,ouDesenvol-
226

## Página 235

CasadoCódigo Capítulo11.TestandocódigosJavaScript
vimentoMovidoaTestes.Ambossãomuitosimilares,diferindoapenasnamaneira
comodescrevemoseorganizamosassuitesespecs.
NoBDD,ostestesdefinemocomportamentodonossocódigo.Oresultadoé
umaleituradefácilcompreensãoeumpoucomaisdesprendidadeconceitostécni-
cos.OJasminetemfocoemBDD,eonomedosseusmétodosenfatizaasdescrições
dassuitesespecs.Noexemploquedesenvolvemos,aexecuçãodeumaspecformula
umafrase:
[quoteValidadordecartãodecrédito,aovalidaronome,eleretornatrueseo
nomenãoestiverembranco.]
NoTDD,ostestesdefinemaestruturaexatadonossocódigo.Aoinvésdocom-
portamento,descrevemosaimplementação. OQUnit,porexemplo,éfocadoem
TDD,eseusmétodosrefletemisso:
module("validadorCartaoDeCredito");
test("#validaNome", function () {
var validador = validadorCartaoDeCredito;
equal(validador.validaNome("Shiota"), true, "valida nome");
equal(validador.validaNome(""), false, "valida em branco");
equal(validador.validaNome(" "), false, "valida espaço");
});
EntreTDDouBDD,nãoexisteescolhacertaouerrada.Contantoqueostestes
unitáriosestejamsendoescritosequeissosejafeitoantesdaimplementação,ambos
melhorarãoaqualidadedoseucódigoedoseuprojeto.
11.4 No mundo real
“LegalShiota,mascomovouusartudoissonavidareal?”
AmaioriadostutoriaisdetesteseBDDdescrevemsituaçõessimpleseotimizadas
—incluindoosmeusexemplos.Mas,nodiaadia,asaplicações sãomuitomaiores
ecomplexas.Comocontinuarescrevendotestes?
Escrevendospecspequenas
Nãoimportasesuaaplicaçãoécompostaapenasporumvalidadordecartãode
crédito,ouporcentenasdecomponentesemcentenasdearquivos:continueescre-
vendospecssimples,pequenas,esemprequebreosproblemasempartesmenores.
227

## Página 236

11.4.Nomundoreal CasadoCódigo
U m aaplicaçãodemédioporte,comoume-commerce,podefacilmentetermaisde
1000specs.Setodasestiveremdevidamenteseparadasemarquivosesuites,eforem
pequenasedefácilcompreensão,suaaplicaçãoestarádevidamentecoberta,resili-
enteaerrosepoderácrescerousermodificadasemgrandespreocupações.
LidandocomoDOM
U m adasmaioresdesculpascontratestesunitáriosemJavaScripténão poder
testarcódigoquemexecomoDOM—e,emumaaplicaçãoweb,issorepresenta95%
doscasos.Issoébalela:seostestesrodarememumnavegadorquedisponibilizao
DOM,aimplementaçãoserátotalmentetestável.
Noexemplodocartãodecrédito,poderíamoscriarumcomponenteparageren-
ciaronódoDOMcorrespondenteaoformulário,etestá-lo:
describe("formCartaoDeCredito", function () {
describe("ao submeter o formulário", function () {
it("deve validar o nome", function () {
var form = document.createElement("form")
, evento = document.createEvent("HTMLEvents")
, validador = validadorCartaoDeCredito
;
spyOn(validador, "validaNome");
formCartaoDeCredito.init(form);
evento.initEvent("submit", true, true);
form.dispatchEvent(evento);
expect(validador.validaNome).toHaveBeenCalled();
});
});
});
AtravésdaAPIdemanipulaçãodoDOMedetécnicascomoinjeção dedepen-
dência,épossíveltestarcomportamentostípicosdenavegadoressemdependerdeo
formulárioestarpresentedefatonoHTML.Nesteexemplo,umelemento <form>
foicriadodozero,eoevento submitfoisimuladoparatestarocomportamentodo
formCartaoDeCredito.
228

## Página 237

CasadoCódigo Capítulo11.TestandocódigosJavaScript
Rodandoostestesemlinhadecomando
Nãoháproblemasemusaro SpecRunner.htmldoJasmineparatestarpeque-
noscódigosebibliotecas,masparaprojetosgrandes,énecessárioummecanismo
umpoucomaissofisticadodoqueabrirumarquivoHTMLcomchamadaspara
JavaScript. Parafacilitar,automatizar,eintegrarostestescomservidoresdeinte-
graçãocontínua(http://blog.caelum.com.br/integracao-continua/),vamosutilizar
umaCommandLineInterface(CLI)—InterfacedeLinhadeComando—erodaras
specsdiretodoterminal,semprecisardeumnavegador.
Existemdiversassoluções, cadaumaatendendoaumconjuntodiferentedefra-
meworksedisponibilizandodiferentesresultados.Nesteartigo,utilizareioKarma
(http://karma-runner.github.io/),umaferramentaquepossibilitarodartestesdedi-
versosframeworks,emdiferentesnavegadores—inclundooPhantomJS,umnave-
gadorheadless(seminterfacevisual,idealparatestarapenasemlinhadecomando).
Primeiramente,énecessáriopossuiroNode.jsinstaladoemsuamáquina.Caso
nãopossua,visiteosite(http://nodejs.org/)einstaleaúltimaversão. V o c êdeverá
tambéminstalaroPhantomJS(http://phantomjs.org/).
ONode.jspossuiumaferramentadegerenciamentodepacotes,oNPM(Node
PackageManager),eoKarmapodeserinstaladoatravésdela. Abraoterminale
digitenalinhadecomando:
$ npm install -g karma
Instaletambémo karma-cli,quedisponibilizaráocomando karmaemqual-
querdiretório:
$ npm install -g karma-cli
V a m o sutilizar os mesmos arquivos que criamos para rodar com o
SpecRunner.html. Crie um novodiretório ( meuprojeto, por exemplo)e
copieosdiretórios srce specparalá:
/meuprojeto
/spec
/src
Entrenodiretório meuprojeto,edigite:
$ karma init karma.config.js
229

## Página 238

11.4.Nomundoreal CasadoCódigo
O Karma farádiversas perguntas e criaráum arquivo de configuração
karma.config.jsparavocê.Sigaasinstruções erespondademaneirasimilar
aoexemploaseguir.
Which testing framework do you want to use ?
Press tab to list possible options.
Enter to move to the next question.
> jasmine
Do you want to use Require.js ?
This will add Require.js plugin.
Press tab to list possible options.
Enter to move to the next question.
> no
Do you want to capture any browsers automatically ?
Press tab to list possible options.
Enter empty string to move to the next question.
> PhantomJS
>
What is the location of your source and test files ?
You can use glob patterns, eg. "js/*.js" or "test/**/*Spec.js".
Enter empty string to move to the next question.
> src/*.js
> spec/*Spec.js
>
Should any of the files included by the previous patterns be excluded ?
You can use glob patterns, eg. "**/*.swp".
Enter empty string to move to the next question.
>
Do you want Karma to watch all the files and run the tests on change ?
Press tab to list possible options.
> yes
U m abreveexplicaçãosobreasopções:
•Qualframeworkusaremos?AlémdoJasmine,oKarmasuportaMocha,QU-
nit,nodeuniteNUnit.
230

## Página 239

CasadoCódigo Capítulo11.TestandocódigosJavaScript
•EstamosusandoRequire.js?Comonossoexemploésimples,nãoprecisamos
usá-lo.
•OKarmapoderodarostestesemdiversosnavegadores:Chrome,Chrome
Canary,Firefox,Safari,Opera,IE,ePhantomJS.OPhantomJS,comocitei,é
umnavegadorheadless,querodanalinhadecomando,semabrirumajanela.
Casoseuprojetonecessite,épossívelrodarostestesemmúltiplosnavegadores
(contantoqueamáquinaostenhainstalados).
•Devemosindicaralocalização dosarquivosJavaScriptaseremtestadosea
localizaçãodasspecs.
•AconfiguraçãodoKarmapermiteignorarcertosarquivosaorodarostestes.
•Aorodarasuite,oKarmapodemonitorarmodificações nosarquivosaserem
testadosounasspecsereexecutarostestesautomaticamente.
Agoraésórodarasuite:
$ karma start karma.config.js
V o c êdeveráveralgoassim:
INFO [karma]: Karma v0.12.1 server started at http://localhost:9876/
INFO [launcher]: Starting browser PhantomJS
INFO [PhantomJS 1.9.7 (Mac OS X)]:
Connected on socket BXELksjC48w19PUuTdhW with id 98829501
PhantomJS 1.9.7 (Mac OS X): Executed 4 of 4 SUCCESS (0.005 secs /
0.003 secs)
OKarmacontinuarámonitorandoqualqueralteraçãoemarquivosdetesteou
implementação.Seadicionarmosum console.logemumadasspecs,porexem-
plo,eisoqueacontecerá:
INFO [watcher]: Changed file "/Users/eshiota/meuprojeto/spec/
formCartaoDeCreditoSpec.js".
LOG: {returnValue: true, timeStamp: 1395701896098, eventPhase: 0,
target: null, defaultPrevented: false, srcElement: null, type: ’submit’,
clipboardData: undefined, cancelable: true, currentTarget: null,
bubbles: true, cancelBubble: false}
PhantomJS 1.9.7 (Mac OS X): Executed 4 of 4 SUCCESS (0.003 secs /
0.004 secs)
231

## Página 240

11.5.Concluindo CasadoCódigo
AsvantagensdeusaroKarmaeoPhantomJSsão:
•Nãodependerdeumnavegadorcominterfacegráfica.
•Executarostestesautomaticamenteacadaalteraçãonocódigo.
•Integraroresultadodostestescomumservidordeintegração contínua.O
Karmaforneceosresultadosemumformatoquepodeserintegradocomdi-
versassoluções.
11.5 Concluindo
Testesmanuaispodemparecersuficientesnocomeço,masàmedidaqueumprojeto
cresce,ficacadavezmaisdifícilgarantiraintegridadedasfuncionalidades.Como
usocadavezmaiornonossodiaadiaecomoaumentodacomplexidadedoJavaS-
cript,nãopodemosmaisignoraraimportânciadetermossegurançaparaalterarum
códigoeadicionarfeaturessemimpactarofuncionamentodaaplicação.Oproblema
tomadimensões aindamaioresquandodiferentesdesenvolvedoresalteramamesma
basedecódigoepotencialmentequebramfuncionalidades.
Ostestesunitáriosproporcionamessasegurança. Aoescreverspecs,vocêga-
rantequeaimplementação estáfazendoexatamenteoesperado,epodetestarse
alterações, adições ouremoções nocódigoalteraramofuncionamentodaaplicação.
FazendoissoatravésdoBDDouTDD,vocêmelhoraodesigndasuasoluçãoead-
quireumconhecimentomaiorsobreoproblemaaserresolvido.E,aoescreveruma
novaspecacadabugencontrado,vocêdiminuiachancedecausá-lonovamente.
Ferramentasparafazerissonãofaltam,bastaescolheraquemaislheagradar.
Nesteartigo,utilizamosJasmineeKarma,masambassãoapenasduasentreasdiver-
sasopções disponíveis.Ecomovimosnofinal,épossíveldarpassosaindamaiores
eintegrarostestesdeJavaScriptemservidoresdeintegraçãocontínua,testandoa
integridadedocódigoacadaversãogerada,ouemintervalosdetempopredetermi-
nados.
OJavaScriptnãoémaisapenasumartifícioparafazeranimações eenviarfor-
mulários.Alinguagemmaisutilizadanodesenvolvimentoparaawebvaicontinuar
crescendo,eénossopapelcomodesenvolvedoresgarantirquenossocódigoenossas
aplicações semprefuncionarão.
232

## Página 241

CasadoCódigo Capítulo11.TestandocódigosJavaScript
Sobre o autor
EduardoShiotaédesenvolvedorfront-endedesigner. Começoua
produzirsitesem1998,trabalhacomdesenvolvimentoparaaW e bdesde
2002ecomdesigndesde2005.U s a n d oHTML,CSSeJavaScript,busca
projetareimplementarinterfacescomboausabilidade,atravésdeum
códigolimpo,semânticoeescalável.MoraemAmsterdamdesde2013
comaesposaeseusquatrogatos;nashorasvagas,fotografaacidade,e
dáworkshops,palestrasementoriasobrefront-end.V o c êpodesegui-lo
noT w i t t e rcomo@shiota.
233