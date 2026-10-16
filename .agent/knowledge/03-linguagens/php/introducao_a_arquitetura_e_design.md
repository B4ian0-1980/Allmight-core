---json
{
  "id": "introducao_a_arquitetura_e_design",
  "title": "Introducao_a_Arquitetura_e_Design",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Arquivo Original:** `Introducao_a_Arquitetura_e_Design.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "arquitetura",
    "design",
    "introducao",
    "introducao_a_arquitetura_e_design",
    "linguagens",
    "php"
  ],
  "perguntas_tipo": [
    "Como utilizar Introducao_a_Arquitetura_e_Design?",
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

# Introducao_a_Arquitetura_e_Design

> **Arquivo Original:** `Introducao_a_Arquitetura_e_Design.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 2

© 2012, Casa do Código
Todos os direitos reservados e protegidos pela Lei nº9.610, de 10/02/1998.
Nenhuma parte deste livro poderá ser reproduzida, nem transmitida, sem auto-
rização prévia por escrito da editora, sejam quais forem os meios: fotográficos,
eletrônicos, mecânicos, gravação ou quaisquer outros.
Casa do Código
Livros para o programador
Rua Vergueiro, 3185 - 8º andar
04101-300 – Vila Mariana – São Paulo – SP – Brasil

## Página 3

CasadoCódigo
“AnossaavóCéres”
–PauloSilveiraeGuilhermeSilveira
“Aminhaesposa,meuspaisemeuirmão”
–SérgioLopes
“Ameuspaiseesposa”
–GuilhermeMoreira
“Ameusamadospais”
–NicoSteppat
“Aminhaamadaesposaefamília”
–FabioKung
i

## Página 5

CasadoCódigo
Agradecimentos
DepoisdedoisanosministrandoocursodeArquiteturaeDesignnaCaelum,além
decincoanoscomumblogdemaisdeduzentosartigostécnicos,pareciafácilescre-
versobreumassuntoquefazpartedonossodiaadia.
Terrívelengano.
Emvezdosseismesesprevistos,passaram-sedoisanos.Doisanostrabalhando
deformaatornaracessívelpráticasetrade-offsqueaparecemcomfrequênciana
plataforma.Sãoproblemasqueosdesenvolvedorespassamaenfrentarrapidamente
aoganharmaisexperiênciaefamiliaridadecomJava.
JuntaresseconhecimentonãoseriapossívelsemaexistênciadoGUJ.com.br,
criadoem2002,noqualosusuáriosjátrocarammaisdeummilhãodemensagens.
Nós,autores,participamosativamentedofórum,oqualnãoatingiriaessamagnitude
semaajudadoRafaelSteil.
Tambémnãoseriapossívelorganizaressasideiassemacolaboraç ãodediversos
amigosqueasrevisaramediscutiramostemasconosco: LucasCavalcanti,David
Paniz,CeciliaFernandes,AlbertoSouza,BrunodeOliveira,FábioPimentel,Vinicius
RobertoeAdalbertoZanata.
Agradecemosaosqueparticiparameparticipamdaelaboraç ãodocursoFJ-91
naCaelum:AdrianodeAlmeida,AndersonLeite,JoséDonizettieDouglasCampos.
Umaespecialmen çãoaoMaurícioAniche,que,alémderealizarumaminuciosa
revisão,nosincentivouatodomomentoamelhorarotextoeacortaroquenãofosse
essencialparaolivro.
iii

## Página 7

CasadoCódigo
Sobre os autores
Paulo SilveiraébacharelemestreemciênciadacomputaçãopelaUSPecofundador
daCaelum.PossuiexperiênciacomdesenvolvimentowebnaAlemanha,passando
peloIBOPEepordoisanoscomoinstrutordaSunMicrosystems.Éumdosfunda-
doresdoGUJ.com.br,editortécnicodarevistaMundoJecriadordoVRaptor.
Guilherme SilveiraélídertécnicoecofundadordaCaelum.TrabalhoucomJava
eTibconaAlemanha,comitterdoXStreamecriadordoRestfulie.Concentraseus
estudosemserviçosREST.Programadorexperiente,participoudasfinaismundiais
deprogramaçãonoJapãoenoCanadádoICPCpelotimedaUSPeéarquitetoJava
certificado(SCEA5).
Sérgio LopesécoordenadornaunidadeSãoPaulodaCaelum.Programadesde
2000edesenvolveemJavadesde2003. ÉarquitetoJavacertificado(SCEA5),mo-
deradordoGUJeparticipanteativodacomunidadeatravésdepalestras,projetos,
cursoseartigos.
Guilherme MoreiraéinstrutoreconsultorpelaCaelum,ondefocaseutrabalho
principalmentecomJavadesde2005,comprojetosinternosetambémdiretamente
nosclientes.FormadoemProcessamentodeDadospelaFATEC-SPearquitetoJava
certificado(SCEA5),escreveartigosparaarevistaMundoJ,alémdeserresponsável
pelaunidadedeBrasíliadaCaelum.
Nico SteppatéengenheirodecomputaçãoaplicadapelaFachhochschuleBran-
denburg.Éinstrutor,consultoredesenvolvedorháseteanoscomJavanoBrasilena
Alemanha.AtuanaunidadeRiodeJaneirodaCaelumeéarquitetoJavacertificado
(SCEA5).
Fabio KungéengenheirodacomputaçãopelaEscolaPolitécnicadaUSP.Passou
porweb,Java,Ruby,experiêncianaAlemanha,instrutornaCaelum,responsávelna
LocawebporCloudComputingenoHerokuemSãoFrancisco. ÉarquitetoJava
certificado(SCEA5).
v

## Página 9

CasadoCódigo
Prefácio
PorJimWebber.
O Arquiteto
Quandopensosobreotermo“arquiteto”,ésemprecomsentimentosconfusos,
comosuspeitoquesejaocasoparamuitosdenósquetrabalhamcomdesenvolvi-
mentodesoftwareatualmente.Duranteminhacarreira,ouvidiversasopiniõesdife-
rentesparaessetermo,mas,paramim,oqueéprincipalparaserumbomarquiteto
possobuscardosmeusprimeirosdiascomodesenvolvedorprofissional(outentando
serumprofissional).
Meuprimeiroempregopareciaserintimidador-apósdiversosanosdepesquisa
acadêmicadentrodeumdepartamentodeciênciadecomputaçãoemumauniver-
sidade,entreiemumaempresaquehaviacompradorecentementeumastartupde
middlewareJavagerenciadaporumgrupodeamigos. Essesamigostrabalhavam
noramodemiddlewarepordécadase“hackeavam”emJavaatémesmoantesdeele
teressenome. Sairdazonadeconfortodacomputaç ãodealtodesempenho,com
tecnologiasasquaiseuestavaacostumado,epularparaumdomínionovodepro-
cessamentodetransaçõesdistribuídascomfocoemCORBAeJ2EEerarealmente
intimidador.Apesardeterumsensorazoáveldeteoriadesistemasdistribuídos,eu
jamaishaviaescritoCORBAouJ2EEcomousuário,muitomenoscomodesenvol-
vedordemiddleware.Foramtemposcomplicados.
Nolaboratórioondecomeceiatrabalhar,meuscolegasostentavamnomesde
cargosbaseadosemsuascapacidades(e,suspeito,longevidade!).Possuíamosenge-
nheiros,engenheirossenioresearquitetos,todososquaistrabalhavamarduamente
emdesenvolverumexcelentemiddlewaredetransaç ão, workflowemensageria.
Comoumengenheirosênior,eueraumpoucomenosverdedoqueosapenasen-
genheiros,masambosrecebíamosordensdosarquitetos-umportime-queeram
oráculos.Osarquitetosquelideravamnossotimeconheciamocódigodetrásparaa
vii

## Página 10

CasadoCódigo
frente,mastambémconheciamseuscampos.Erasemprepossívelconfiarqueseriam
capazesdeexplicarmodelosdetransaçãodistribuídacomplexosemostrarcomodi-
versospadrõeseabstraçõesdocódigoossuportavam. Elestambémconheciamas
armadilhaseconseguiamdetectarcedoescolhasdedesigneimplementaç ãoruins,
umavezqueeramcapazesdeveràfrente,oupelomenosvermaislongedoqueeu
conseguia.
Nãoachoquedissealgumdiaparaessesarquitetos-talvezporcausadomeu
orgulhojuvenil-oquãoimportanteelesforamemdelinearmeupensamentoecom-
portamento.Entretanto,sempreaspirei(ealgumasvezessucedi)sercomoeles,co-
nheceratecnologiaprofundamente,entenderocontextonoqualelaestásendoem-
pregada,guiareserguiadopeloscolegasdemeutime.Essafoiumaaspiraç ãoque
leveiparameupróximoempregoemumaempresaglobalmuitoconhecidaeadmi-
radanoramodeconsultoriadeTI.
Aoentraremminhanovaempresa,decidiquejáhaviavistobastantesoftwaree
erabomosuficienteemescrevercódigo,eentãomedeclareiumarquiteto.Aoen-
contraralgunsdemeusnovoscolegaspelaprimeiravez,fuicalorosamenterecebido
eperguntadosobrequalseriameupapel.Respondiqueeueraumarquiteto;algoque
penseiquedariaumsentidodecompetêncianonívelmicrodapilhadetecnologias,
enonívelmacroaoredordaconstruçãodesistemas.Fiqueiatônitoaodescobrirque
fuirepreendidoporessarespostaefiqueimeperguntandooqueacabaradeaconte-
cer,afinal,eunãohaviaentradoparatrabalharcomessaspessoasdevidoareputaç ão
queelespossuíamnodesenvolvimentodesoftwareeAgile?
Nãodemoroumuitoparaqueeuentendesseocontexto.Meuscolegastrabalha-
vamcomconsultoriaháalgunsanoseconhecerammuitos“arquitetosexperientes”.
Masessesnãoeramomesmotipodepessoaqueeuadmiravaemmeuprimeiro
trabalho;eramarquitetosperigosamenteultrapassados,compoucahabilidadeem
entregarsoftware,eumtalentosemfimparacausarconfusãoecriarpolíticascor-
porativas. Eeu,aparentemente,tinhameapresentadocomoumdesses. Nãoeraa
melhormaneiradecausarumaboaimpressãoaosmeusnovoscolegas.
Aindaassim,duranteos6anosenos10paísesemquetrabalhei,medescrevi
comoarquiteto.Euestavaemumamissãoderecuperarovalordessetítulo,ecomo
passardotempoobtivealgumsucesso.Come çamosapensaremumarquitetonão
sócomoo“melhorprogramador”ouum“pesomorto”,massimcomoumpapelque
consideraosdetalhesdenívelmacroemumtimequeentregasoftware-comoa
integraçãocomoutrossistemasfuncionará,comofalhaserecuperaçõesserãotraba-
lhadas,comoavazãoserámedidaegarantida.
viii

## Página 11

CasadoCódigo
Nosmelhoresprojetosemquetrabalhei,opapeldoarquitetoeracomplementar
aodosstakeholders.Enquantoopessoaldenegóciospriorizaaentregadefuncio-
nalidades,arquitetospriorizamosrequisitosnãofuncionaiseajudamaordenara
entregaderequerimentosfuncionaisqueminimizamemantêmcaracterísticasnão
funcionais.Nosmelhoresprojetosquetrabalhei,eunãoeraomelhorprogramador
daequipe,nemnamaiorpartedasvezestinhaomaiorconhecimentodaslingua-
gens,ferramentaseframeworkscomparadocomoutrosdedicadosprogramadores.
Apósumtempoengolindooorgulho,comeceiaverasvantagensinerentesdisso.
Comoarquiteto,aindasoualguémquetambémentendebastantedecódigo,em
umnívelnoqualconsigoescrevercódigocomoutrosprogramadores(possivelmente
melhoresdoqueeu)elerseucódigoetestes. Acreditoqueissosejafundamental
paraaarquitetura. Semahabilidadedeseenvolvercomocódigo,arquitetosnão
têmcomodeterminarcomosuaarquiteturafoiadotadaporumasolução,nemcomo
elestêmumamaneiradiretadepegarfeedbackdesuaarquiteturaparamelhorá-la.
Semhabilidadesdesoftware,umarquitetoficarefémdostimesdedesenvolvimento,
oqueéumoverhead,nãoumbenefício.
Sentadoaquiemminhamesa,emLondres,escrevendoesseprefácio,éclaroque
ano çãodoconceitodearquitetocontinuacinzenta. Atémesmohoje,arquitetos
estãofrequentementenotopodatorredemarfim,descrevendovisõesgrandiosase
impraticáveisatravésdeslidesediagramasUMLquenãoajudamparatropasnas
trincheirasobedeceremcomoescravos(comoseelesfossem!).Masnãoprecisaser
assim. Aquelesdenósquesepreocupamcomamelhoriacontínuadoramoese
preocupamemescrevercódigocadavezmelhorcomosefeitoscolateraispositivos
queissopoderesultaremnossasociedadeecomunidadetêmodeverdetomaro
termo“arquiteto”ereapropriar-sedele.
Estelivroéumpassonessadire ção. Eletrataarquitetoscomoprofissionaisdo
desenvolvimentodesoftwareeéfundamentalqueelesentendamasferramentasco-
munsdoramodedesenvolvimentodesoftware. Estelivroprovêinsightsnasfer-
ramentascomuns,padrõesdedesenvolvimentoepráticasdedesignquearquitetos
contemporâneostrabalhandoemaplicaçõescorporativaspossuem.Eletratadeuma
gamadedisciplinasdedesenvolvimentodesdecódigorobusto,designdeaplicaç ão,
dadoseintegração,quesãoosprincipaiselementosdamaiorpartedossistemascor-
porativos.Elenãoapenasfocaemimportantesdetalhesdalinguagemedosprinci-
paisframeworks,mastambémnonívelmacro,dandoumapercep çãomaiscompleta
-percepçãoestaqueumarquitetopraticanteprecisaquandoajudaaguiarumtime
paraosucesso.
ix

## Página 12

CasadoCódigo
Àmedidaquedesenvolvedoresprocuramsetornararquitetos,olivromostraque
ofocoestreitonaúltimalinguagemouframeworkdamodaénecessário,masnãosu-
ficiente.Àmedidaquearquitetosbuscamreabilitaç ão,estelivrodeixaóbvioquenão
hásucessosemreaprenderas(habilmentedemonstradas)ferramentasdeconstru-
çãodesoftware.Enquantonenhumlivropodetorná-loumarquitetodanoitepara
odia,esteprovêaomenosummodelodotipodearquitetoqueeutantoadmirava,
eesperoquesualeituraoinspireasetornaressetipodearquitetotambém.
JimWebberéformadoemcomputa çãoepossuidoutoradopelaUniversityofNew-
castle.Trabalhouporbastantetempona ThoughtWorks,ondeficouconhecidopeloseu
manifestoGuerrillaSOA.Hoje,éChiefScientistnaNeoTechnology,empresaportrás
dobancodedadosorientadoagrafosNeo4j
x

## Página 13

CasadoCódigo
Introdução
Implementação, design ou arquitetura?
Desenharsistemaséumatarefadifícil. E,aindafazercomquesejamescaláveise
performáticos,mantendoumaaltaqualidadeinternaeexterna,éumdesafio.
Noartigo“Aimportânciadeserfechado”,CraigLarmandizque“vocêdeveen-
frentarsuasbatalhasdedesign,sejamelasnonívelmacroarquiteturalounohumilde
campodasinstâncias”[109]. Essasbatalhasdevemsercontradecisõesqueatrapa-
lhamocrescimentoeafuturamodificaç ãodasuaaplicação,diminuindoocustode
manutençãoalongoprazo.
Masédifícildefinircomprecisãooquesãoinstânciasounívelmacroarquite-
tural,aslinhasqueseparamarquitetura,designeimplementaç ãosãomuitotênues.
MartinFowlerfalaomesmonoâmbitodepatternslogonasegundapáginadeseu
livro"PatternsofEnterpriseApplicationArchitecture:“Algunsdospadrõesnestelivro
podemserchamadosarquiteturais,jáquerepresentamdecisõesimportantessobrees-
saspartes;outrossãomaissobredesigneoajudamaimplementaressaarquitetura.
Nãofa çonenhumaforte tentativa de separar esses dois, uma vez que aquilo que é
arquitetural ou não é subjetivo”. [68]Fowlerquestionainclusiveousodotermo
arquitetocomopapel.[70]AuniversidadedeCarnegieMellonpossuidiversasde-
finiçõesetambémabordaagrandedificuldadequeédefiniradiferen çaexataentre
implementação,designearquitetura.[51],[1]
Nestelivro, em vez de encontrar respostas e solu ções encaixotadas, apresen-
taremos perguntas e discussões relacionadasaalgunsdosprincipaistópicosrecor-
rentesemaplicaçõesescritasparaaplataformaJava,afimdealimentaroespírito
críticododesenvolvedor. Eledevesercapazdeenxergarambas,asvantagenseas
desvantagens;todoo trade-offpresenteemsuasdecisões.
Dominarumaplataforma,seusprincipaisframeworkseseufuncionamentoin-
ternoéessencialparaqueosresponsáveispelodesenvolvimentodeumaaplicaç ão
conheçamnãosóasvantagens,mastambémasdesvantagensdesuasdecisões. O
desenvolvedorqueacreditanãoexistiroudesconheceoladonegativoparadetermi-
xi

## Página 14

CasadoCódigo
nadaabordagemsofreráasconsequênciasdemanutençãoquandoasmesmassurgi-
remdentrodaaplicação.
Comopassardotempo,aimplementaçãoouodesignouaarquiteturadeixaráde
atenderàsnecessidadesdosclientes.Nesseinstante,énecessárioevoluiresseaspecto
defasado,paraquevolteasersuficientementeadequadoparaaquelarealidadedo
sistema.
ComoJoelSpolskyafirma,“pessoasdetodoomundoestãoconstantementecri-
andoaplicaçõesWebusando.NET,JavaePHP.Nenhumadelasestáfalhandoporcausa
daescolhadatecnologia”.[191]Maselevaialém,aodizerque“todosessesambientes
sãograndesecomplexos,e você realmente precisa de, no mínimo, uma pessoa com
enorme experiência de desenvolvimento na plataforma escolhida,porque,casocon-
trário,vocêtomarádecisõeserradaseacabarácomumcódigomuitoconfusoquepre-
cisaserreestruturado”.Joeldeixaexplícitaanecessidadedeprofundoconhecimento
técnicodaplataformaescolhida.
Fowleraindacomplementaque,diferentementedaengenhariacivil,ondehá
umadivisãoclaradehabilidadesentrequemfazodesignequemfazaconstruç ão,
comsoftwareédiferente.[71]Qualquerdesenvolvedorquevenhaalidarcomdeci-
sõesdealtonívelnecessitadeumforteconhecimentotécnico.Estelivrofoielabo-
radocomessavisão:osucessodaarquiteturadeumsistemaestáfortementeligado
comodesigneaimplementação.
Levandoemconsideraçãoessavisão,estelivrodestina-seàquelequeaspirapor
umpapeldearquiteto? Quemseriaoarquiteto? Opapeldoarquitetoéampla-
mentediscutidoe,nanossavisão,oarquitetoprecisaconhecerprofundamentea
plataforma,alémdeserumexcelenteeexperientedesenvolvedor.
NaspalavrasdeMartinFowler,“otermoarquiteturaenvolveano çãodosprin-
cipaiselementosdosistema, as peças que são difíceis de mudar.Umafunda çãona
qualorestoprecisaserconstruído”.
[71]Podemosiralémedizerqueessafundaç ãoqueconstituiaarquitetura,que
envolveosprincipaiselementosdosistema,podesimserevolutivaesofrermodifi-
caçõescomotempo,desdequeseudesigneimplementaç ãopermitam,quebrando
umpoucoaideiadequeotrioarquitetura-design-implementaç ãoformeummodelo
estritamentepiramidal.Estelivroabordarámuitasquestõesdedesigneimplemen-
taçãocomointuitodedemonstraressapossibilidadeevolutiva.
Aimagemdeumarquitetodistantedodiaadiadodesenvolvimentodaequipe,
semprofundoconhecimentotécnicoedeimplementaç ãosobreaferramenta,que
apenastomaasgrandesdecisõesedespachaordensediagramas,hámuitotempo
xii

## Página 15

CasadoCódigo
estádefasada.Maisdoquequererseroisoladoarquitetoqueapenasdespachaor-
dens,cadavezmaisenxergamosqueocaminhoéserolíderincentivadordatomada
dedecisão,alémdeumexímiodesenvolvedor. [190]Parafraseandomaisumavez
MartinFowler,“(...)oarquitetodevesercomoumguia(...)queéumexperienteeca-
pacitadomembrodaequipequeensinaaosoutrossevirarmelhor,eaindaassimestá
sempreláparaaspartesmaiscomplicadas”. [70]ELarmantambémnãoperdoao
arquitetoquenãovêcódigo:“umarquitetoquenãoestáapardaevolu çãodocódigo
doproduto,nãoestáconectadocomarealidade”,chegandoaconsiderarqueocódigo
éoverdadeirodesignouarquiteturadosoftware.[111]
Éimpossível“mudar”umaarquiteturaouumdesigndiretamente,umavezque
ambossãointerpretaçõesdoúnicobemexistente:aimplementação.Atravésdamu-
dançanaimplementação,adquire-seascaracterísticasarquiteturaisoudedesignde-
sejadas. Arquitetura e design são interpretaç ões, visões, leituras críticas de uma
implementação(Figura1).
Figura1:Arquiteturaedesignsãointerpretações,leiturascríticasdeumaimplemen-
tação.
Designéumaformadeinterpretaraimplementaç ão,analisandoecompreen-
dendoasinteraçõesentredeterminadaspartesdosistema,comopossíveisimpactos
queumamudan çaemumpontocausaemoutrocomponentequeoacessadiretaou
indiretamente. Existemdiversasinterfacesdecomunicaçãoentrediversoscompo-
nentes:oApachesecomunicacomoJettyatravésdo mod_jk;umaaplicaçãoWeb
xiii

## Página 16

CasadoCódigo
secomunicacomoJettyatravésdaServletAPI;jádentrododomíniodaaplica-
ção,outrasinterfacesconectampartesdeumaimplementaç ão,comouma List,um
Calendar,um DAOouuma Connection. Todaselassãoanalisadasnoaspectode
design(Figura2).
Figura2: Nopontodevistadodesign,importamcaracterísticasdasinterfacesde
comunicaçãoentrepartesdosistema,seuscomponentes,emtodososníveisdeabs-
tração:desdeentreclassesatédoissoftwaresdistintos.
Implementaçãonãosignificasomenteocódigoescritopelosdesenvolvedoresda
equipeatual,mastambémoconjuntodeescolhasdeferramentas,versõesquefa-
zempartedosambientesdedesenvolvimento,homologaçãoeprodução,linguagem
utilizada,legibilidadedocódigo,entreoutras.Todasessasescolhasmodelamaim-
plementaçãodeumsistema,assimcomosuaqualidade(Figura3).
Arquiteturaéaindaumaoutramaneiradeveraimplementaç ão,analisandoe
compreendendocomoumamudan çaemdeterminadopontodosistemaafetaosis-
temainteiro,edetodasasmaneiraspossíveis.Porexemplo,casoumpontoqualquer
daaplicaçãopasseateracessoremotoaoinvésdeapenaslocal,issopodeafetaruma
outrapontadaaplicação,deixando-amaislenta.Essetipodeanálisenãocostuma
serfeitaquandosepensanodesign,jáqueodesigntemumapreocupaç ãomaislocal.
Aessavisãomaisglobaldosistema,édadoonomedearquitetura(Figura4).
xiv

## Página 17

CasadoCódigo
Figura3:Nopontodevistadaimplementaç ão,analisa-seocódigo,asescolhasde
versão,linguagemutilizada,legibilidadedocódigoetc.
Figura4:Nopontodevistaarquitetural,analisa-secomoescolhasdeimplementa-
çãoinfluenciamosistemainteiro-nãocomoumtodo,nãocomoumsó,maspor
completo.
Comopassardotempo,comodesignearquiteturasãodiferentesmaneirasdein-
terpretaraimplementação,éatravésdeumamudançanaimplementaçãoqueobtém-
seasmudan çasdesejadasnavisãodedesignounavisãodearquitetura(Figura5).
xv

## Página 18

CasadoCódigo
Figura5: Umavezquesomenteimplementaçõessãoconcretas,todotipodemu-
dançaimplicaemconheceraimplementaç ãoe,alterá-lacausapossíveismudan ças
nosaspectosarquiteturaisededesign.
Umaboaimplementação,designouarquiteturaéaquelaquepermitemodifica-
çõescausandosomenteumimpactoconsideradojustoaoutraspartesdosistema,e,
aomesmotempo,diminuindoasocorrênciasdetaissituações,minimizandoocusto
dedesenvolvimentoemanuten ção.
Éessavisãodearquiteturaedesignquetentamosobternestelivro.Aplataforma
Javaévistacomprofundidadeesuaspeculiaridades,desdeocampodasinstâncias,
interfacesedaJVM,atéonívelmacroarquiteturaldelayers,tierseframeworks.A
implementaçãoterápapelfundamentalaqui,esuaimportânciaérealç adamesmo
emdiscussõesarquiteturaisdealtonível.
Colhemosnossaexperiênciaaolongodenoveanosdediscussõesnosfóruns
doGUJ.com.br,cincoministrandoocursodeArquiteturaeDesignJavanaCaelum,
alémdediversosprojetos,consultoriaseexperiênciastrocadascomosclientesepar-
ceiros. Conhecer profundamente as ferramentas é o primeiro passo para poder
fazer as perguntas corretas ao enfrentar o cenário de uma nova aplicação.
xvi

## Página 19

CasadoCódigo Sumário
Sumário
1 A plataforma Java 1
1.1 Javacomoplataforma,alémdalinguagem . . . . . . . . . . . . . . . . 1
1.2 Especificaçõesajudamouatrapalham? . . . . . . . . . . . . . . . . . . 7
1.3 Usealinguagemcertaparacadaproblema. . . . . . . . . . . . . . . . 11
2 Java Virtual Machine 15
2.1 Princípiosdegarbagecollection . . . . . . . . . . . . . . . . . . . . . . 15
2.2 Nãodependadogerenciamentodememória . . . . . . . . . . . . . . 23
2.3 JITCompiler:compilaçãoemtempodeexecução . . . . . . . . . . . 27
2.4 Carregamentodeclasseseclassloaderhell . . . . . . . . . . . . . . . . 31
3 T ópicos de Orientaç ão a Objetos 41
3.1 Programevoltadoàinterface,nãoàimplementaç ão . . . . . . . . . . 41
3.2 Componhacomportamentos. . . . . . . . . . . . . . . . . . . . . . . . 47
3.3 Eviteheran ça,favoreçacomposição . . . . . . . . . . . . . . . . . . . . 50
3.4 Favoreçaimutabilidadeesimplicidade . . . . . . . . . . . . . . . . . . 55
3.5 Cuidadocomomodeloanêmico . . . . . . . . . . . . . . . . . . . . . 62
3.6 ConsidereDomain-DrivenDesign . . . . . . . . . . . . . . . . . . . . 66
4 Separaç ão de responsabilidades 75
4.1 Obtenhabaixoacoplamentoealtacoesão . . . . . . . . . . . . . . . . 75
4.2 Gerenciesuasdependênciasatravésdeinje ção . . . . . . . . . . . . . 78
4.3 ConsidereusarumframeworkdeInje çãodeDependências. . . . . . 87
4.4 Fábricaseomitodobaixoacoplamento . . . . . . . . . . . . . . . . . 94
4.5 Proxiesdinâmicasegeraçãodebytecodes . . . . . . . . . . . . . . . . 104
xvii

## Página 20

Sumário CasadoCódigo
5 T estes e automaç ão 111
5.1 Testesdesistemaeaceitação . . . . . . . . . . . . . . . . . . . . . . . . 112
5.2 Testedeunidade,TDDedesigndecódigo . . . . . . . . . . . . . . . . 115
5.3 Testandoaintegraçãoentresistemas . . . . . . . . . . . . . . . . . . . 126
5.4 Feedbackatravésdeintegraçãocontínua . . . . . . . . . . . . . . . . . 130
6 Decisões arquiteturais 139
6.1 Dividindoemcamadas:tierselayers . . . . . . . . . . . . . . . . . . . 140
6.2 DesenvolvimentoWebMVC:ActionsouComponentes? . . . . . . . 147
6.3 Dominesuaferramentademapeamentoobjetorelacional. . . . . . . 155
6.4 Distribuiçãodeobjetos . . . . . . . . . . . . . . . . . . . . . . . . . . . 168
6.5 Comunicaçãoassíncrona . . . . . . . . . . . . . . . . . . . . . . . . . . 178
6.6 ArquiteturacontemporâneaeoCloud . . . . . . . . . . . . . . . . . . 182
7 Integraç ão de sistemas na Web e REST 193
7.1 PrincípiosdeintegraçãodesistemasnaWeb. . . . . . . . . . . . . . . 194
7.2 Padronizações,contratosrígidoseSOAP. . . . . . . . . . . . . . . . . 198
7.3 Evitequebrarcompatibilidadeemseusserviços. . . . . . . . . . . . . 203
7.4 PrincípiosdoSOA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .206
7.5 REST:arquiteturadistribuídabaseadaemhipermídia . . . . . . . . . 212
Bibliografia 246
xviii

## Página 21

Capítulo1
AplataformaJava
Diversas plataformas de desenvolvimento possuem grande penetração no mer-
cado.AplataformaJavaatingiualideran çadevidoaalgumascaracterísticasrelacio-
nadasaoseuprocessodeevoluçãoeespecificação,juntocomaparticipaçãofortee
ativadacomunidade.ConhecerbemoecossistemaJavarevelaseuspontosfortese
tambémasdesvantagenselimitaçõesquepodemosenfrentaraoadotá-la.
1.1 J av a como plataforma, além da linguagem
ÉfundamentalconhecercomqueobjetivosaplataformaJavafoiprojetada,afim
deentendercomprofundidadeosmotivosquealevaramaserfortementeadotada
noladodoservidor. JavaéumaplataformadedesenvolvimentocriadapelaSun,
queteveseulan çamentopúblicoem1995.Elavinhasendodesenvolvidadesde1991
comonome Oak,lideradaporJamesGosling. OmercadoinicialdoprojetoOak
compunha-sededispositivoseletrônicos,comoos set-topbox.[39]
Desdeasuaconcep ção,aideiadeumaplataformadedesenvolvimentoeexe-
cuçãosempreestevepresente. OJavaidealizadoeraumasoluç ãoquefacilitavao

## Página 22

1.1. Javacomoplataforma,alémdalinguagem CasadoCódigo

## Página 23

CasadoCódigo Capítulo1. AplataformaJava
Java é uma completa plataforma de desenvolvimento e execução.Estaplataforma
écompostadetrêspilares:amáquinavirtualJava(JVM),umgrandeconjuntode
APIsealinguagemJava.
OconceitodemáquinavirtualnãoéexclusividadedoJava.As HardwareVirtual
Machines,comoVMWare,ParallelsouVirtualBox,tambémmuitofamosas,sãousa-
daspararodarváriossistemasoperacionaisaomesmotempo,utilizandoorecurso
devirtualizaçãoqueabstraiohardwaredamáquina. JáaJVM, Java Virtual Ma-
chine(MáquinaVirtualJava),éumaApplicationVirtualMachine,queabstrainãosó
acamadadehardwarecomoacomunicaç ãocomoSistemaOperacional.
UmaaplicaçãotradicionalemC,porexemplo,éescritaemumalinguagemque
abstraiasoperaçõesdehardwareeécompiladaparalinguagemdemáquina.Nesse
processodecompilação,égeradoumexecutávelcominstruçõesdemáquinaespe-
cíficasparaosistemaoperacionaleohardwareemquestão.
UmexecutávelCnãoéportável;nãopodemosexecutá-lonoWindowsenoLi-
nuxsemrecompilação.Masoproblemadeportabilidadenãoserestringeaoexecu-
tável,jáquemuitasdasAPIssãotambémespecíficasdosistemaoperacional.Assim,
nãobastarecompilarparaoutraplataforma,éprecisoreescreverboapartedocódigo
(Figura1.1).
Figura1.1:ProgramaemCsendoexecutadoemdoissistemasoperacionaisdiferen-
tes.
Aousaroconceitodemáquinavirtual,oJavaeliminaoproblemadaportabili-
dadedocódigoexecutável.Emvezdegerarumexecutávelespecífico,como“Linux
PPC”ou“Windowsi386”,ocompiladorJavageraumexecutávelparaumamáquina
genérica,virtual,nãofísica,aJVM.
3

## Página 24

1.1. Javacomoplataforma,alémdalinguagem CasadoCódigo
JVMéumamáquinacompletaquerodaemcimadareal.Elapossuisuaspróprias
instruçõesdemáquina(assembly)esuasAPIs. Seupapeléexecutarasinstruções
demáquinagenéricasnoSistemaOperacionalenohardwareespecíficosoboqual
estiverrodando(Figura1.2).
Figura1.2:ProgramaemJavasendoexecutadoemdoissistemasoperacionaisdife-
rentes.
Nofimdascontas,oproblemadaportabilidadecontinuaexistindo,masoJava
puxaessaresponsabilidadeparaaprópriaJVM,emvezdedeixá-laacargodode-
senvolvedor.ÉprecisoinstalarumaJVMespecíficaparaosistemaoperacionaleo
hardwarequesevaiusar. Mas,feitoisso,odesenvolvimentodoaplicativoétotal-
menteportável.
Éimportanteperceberque,porcausadesteconceitodaJVM,ousuáriofinal,
quedesejaapenasrodaroprograma(nãodesenvolvê-lo),nãopodesimplesmente
executá-lo.TantoosdesenvolvedoresquantoosusuáriosprecisamdaJVM.Masos
primeiros,alémdaJVM,precisamdocompiladoredeoutrasferramentas.
Porestarazão,oJavapossuiduasdistribuiçõesdiferentes:o JDK(Java Develop-
ment Kit),queéfocadonodesenvolvedoretraz,alémdaVM,compiladoreoutras
ferramentasúteis;eo JRE(Java Runtime Environment),quetrazapenasoneces-
sárioparaseexecutarumaplicativoJava(aVMeasAPIs),voltadoaousuáriofinal.
UmpontofundamentalarespeitodaJVMéqueelaéumaespecificaç ão,dife-
4

## Página 25

CasadoCódigo Capítulo1. AplataformaJava
rentedemuitosoutrosprodutoselinguagens.QuandovocêcompravaoMicrosoft
VisualBasic6.0,sóhaviaumaop ção:odaMicrosoft.
AJVM,assimcomoalinguagem,possuiespecificaçõesmuitobemdefinidase
abertas: aJavaVirtualMachineSpecification [113]ea JavaLanguageSpecification.
[85]Emoutraspalavras,pode-setomaraliberdadedeescreverumcompiladore
umamáquinavirtualparaoJava.Eéistooqueacontece:nãoexisteapenasaJVM
HotSpotdaSun/Oracle,mastambémaJ9daIBM,aJRockitdaOracle/BEA,aApple
JVM,entreoutras.Ficamosindependentesatédefabricante,oqueémuitoimpor-
tanteparagrandesempresasquejásofrerammuitocomafaltadealternativaspara
tecnologiasadotadasantigamente.
EssavariedadedeJVMstambémdácompetitividadeaomercado.Cadaumadas
empresasfabricantestentamelhorarsuaimplementaç ão,sejaaperfeiçoandooJIT
compiler,fazendo tweaksoumudandoogerenciamentodememória.Istotambém
traztranquilidadeparaasempresasqueusamatecnologia.Sealgumdiaopre çoda
suafornecedoraestivermuitoalto,ouelanãoatingirmaisseusrequisitosmínimos
deperformance,épossíveltrocardeimplementação.Temosagarantiadequeisso
funcionará,poisumaJVM,paraganharestenome,temdepassarporumabateria
detestesdaSun,garantindocompatibilidadecomasespecificações.
AplataformaMicrosoft.NETtambéméumaespecificaçãoe,porestemotivo,o
grupoMonopodeimplementarumaversãoparaoLinux.
Os bytecodes Java
AJVMé,então,oponto-chaveparaaportabilidadeeaperformancedaplata-
formaJava. Comovimos,elaexecutainstruçõesgenéricascompiladasapartirdo
nossocódigo,traduzindo&#173;-asparaasinstru çõesespecíficasdosistemaopera-
cionaledohardwareutilizados.
Essasinstruçõesdemáquinavirtualsãoos bytecodes. Sãoequivalentesaos
mnemônicos(comandos)doassembly,comadiferen çadequeseualvoéumamá-
quinavirtual. Onome bytecodevemdofatodequecada opcode(instrução)tem
otamanhodeumbytee,portanto,aJVMtemcapacidadederodaraté256byte-
codesdiferentes(emboraoJava7possuaapenas205). Istofazdelaumamáquina
teoricamentesimplesdeseimplementarederodaratéemdispositivoscompouca
capacidade.
Podemos,inclusive,visualizaressesbytecodes. OdownloaddoJDKtrazuma
ferramenta,o javap,capazdemostrardemaneiramaislegívelobytecodecontido
5

## Página 26

1.1. Javacomoplataforma,alémdalinguagem CasadoCódigo
emumarquivo.class compilado.Obytecodeserámostradoatravésdosnomesdas
instruções,enãodebytespuros.
OcódigoaseguirilustraumexemplodeclasseJava:
public class Ano {
private final int valor;
public Ano(int valor) {
this.valor = valor;
}
public int getValor() {
return valor;
}
}
Eaexecuçãodalinhadocomando javap -c Anoexibeoconjuntodeinstruções
queformamaclasse Ano:
public class Ano extends java.lang.Object{
public Ano(int);
Code:
0: aload_0
1: invokespecial #10; //Method java/lang/Object.”<init>”:()V
4: aload_0
5: iload_1
6: putfield #13; //Field valor:I
9: return
public int getValor();
Code:
0: aload_0
1: getfield #13; //Field valor:I
4: ireturn
}
EmboraalinguagemJavatenhaumpapelessencialnaplataforma,tê-lacomo
umaexecutoradebytecodes,enãoexatamentedecódigoJava,abrepossibilidades
interessantes.AplataformaJavatemidocadavezmaisnadire çãodeserumambiente
deexecuçãomultilinguagem,tantoatravésda ScriptingAPI quantoporlinguagens
quecompilamdiretoparaobytecode.Éumaideiapresente,porexemplo,no.NET
desdeoinício,comsua CommonLanguageRuntime(CLR)executandodiversaslin-
guagensdiferentes.
6

## Página 27

CasadoCódigo Capítulo1. AplataformaJava
AlinguagemScalamostraestafor çadobytecodeparaaplataformaJava.Paraa
JVM,oqueinteressasãoosbytecodes,enãoapartirdequallinguagemelesforam
gerados.EmScala,teríamososeguintecódigofonte,quepossuiamesmafunciona-
lidadequeocódigoJavamostradoanteriormente:
class Ano(val valor:Int)
AocompilarmosaclasseScalaanteriorcomocompilador scalac,osbytecodes
geradosserãomuitopróximosdosvistosnaclasseJava.Épossívelobservarissoro-
dandoocomando javapnovamente. Aúnicagrandemudançaéqueogetterem
Scalachama-seapenas valor()enão getValor()comoemJava. Veremosmais
sobreoutraslinguagensrodandoemcimadaJVMnestecapítulo.Alémdisso,mui-
tosframeworkseservidoresdeaplicaçãogerambytecodedinamicamentedurantea
execuçãodaaplicação.
AJVMé,portanto,umpoderosoexecutordebytecodes,enãointeressadeonde
elesvêm,independentementedeondeestiverrodando.Éporestemotivoquemuitos
afirmamquealinguagemJavanãoéocomponentemaisimportantedaplataforma,
mas,sim,aJVMeobytecode.
1.2 E specificações ajudam ou atrapalham?
APlataformaJavaébastantelembradaporsuascaracterísticasdeabertura,porta-
bilidadeeatéliberdade.Háoaspectotécnico,comindependênciadeplataformae
portabilidadedesistemaoperacionaldesdeoiníciodaplataforma. Hátambéma
comunidadecomseusgruposdeusuáriosportodoomundo,sempreapoiadosein-
centivadospelaSun/Oracle.Háaindaomundoopensource,queabraçouoJavacom
diversosprojetoscruciaisparaoecossistemadaplataforma,muitosdelespresentes
nodiaadiadamaioriadosdesenvolvedores.EháoJCPesuasespecificações.
Em1998,trêsanosapósonascimentodoJavadentrodaSun,foicriadoo Java
CommunityProcess(JCP),comoumórgãoindependentedaprópriaSun,cujoob-
jetivoeraguiarospassosdoJavademaneiramaisabertaeindependente. Hoje,a
OracledetémosdireitosdamarcaJava,masasdecisõessobreosrumosdaplata-
formanãoestãoapenasemsuasmãos.QuemguiaosrumosdoJavaéoJCP,com
suascentenasdeempresasedesenvolvedoresparticipantes,queajudamaespecifi-
carasnovastecnologiaseadecidirnovoscaminhos.Háum ComitêExecutivoeleito
acadatrêsanosquecomandaoórgão.Grandesempresas,comoGoogle,IBM,HP,
RedHat,Nokia,alémdaOracle,fazempartedele,inclusiveorganizaçõeslivres,como
aSouJava.
7

## Página 28

1.2. Especificaçõesajudamouatrapalham? CasadoCódigo
Cadanovafuncionalidadeoumudan çaquesequeirarealizarnaplataformaé
propostaaoJCPnoformato JSR,uma JavaSpecificationRequest.Sãodocumentos
querelatamessaspropostas,paraquepossamservotadaspelosmembrosdoJCP.De-
poisdeaceitaumaJSR,éformadoum Expert Groupparaespecificá-laemdetalhes
edepoisimplementá-la.TodosospassosficamsobachanceladoComitêExecutivo,
enãounicamentedaOracle.AsJSRsrecebemnúmerosdeidentificaç ãoeacabam
ficandoreconhecidasporestes.AJSR318,porexemplo,especificouoEJB3.1;aJSR
316paraoJavaEE6;eaJSR336paraoJavaSE7.
MasasJSRdefinemapenas especificações deprodutosrelacionadosaoJava,e
nãoimplementações.AtéháumaimplementaçãodereferênciafeitapeloJCP,mas,
nofundo,opapeldoórgãoécriargrandesdocumentosquedefinemcomotudo
devefuncionar.Oqueusamosnapráticaéumaimplementaç ãocompatívelcoma
especificaçãooficial.QuandobaixamosoJDKdaSun/Oracle,oquevemnãoéoJava
SE,mas,sim,umaimplementaçãofeitapelaempresaseguindoaespecificaç ão.Mas
nãosomosobrigadosausaraHotSpot,implementaç ãodaSun/Oracle. Podemos
usaroutras,comoaJ9daIBM,aJRockitdaBEA/Oracle,ouoHarmonydaApache,
e,ainda,JVMsmaisespecíficasparacertossaboresdoUnix,dispositivosmóveise
hardwaresmaisparticulares.
Porestemodelodeaberturadeespecificações,oJavagaranteatodosumgrau
deindependênciadofabricante. Épossívelusarprodutosdediversosediferentes
fabricantes(IBM,Oracle,JBoss)etrocá-loscomcertafacilidadenahoraqueforne-
cessário.Asdiferençasentreosprodutosdediferentesfabricantesestãonosuporte
oferecido,documentação,facilidadesextrasdegerenciamento,otimizações,eatéex-
tensõesproprietárias.Sobreesteúltimopontovaleumaressalva:praticamentetodo
fabricanteestendeaespecificaçãooficialcomAPIsproprietárias,sejacomoobjetivo
detaparlacunasnaespecificação,sejaparateralgumdestaqueamaisemrelaç ãoa
seusconcorrentes.Nãoháproblemaalgumnisso,maséprecisoterconsciênciade
que,aousarumrecursoproprietário,épossívelperderportabilidadeeindependên-
ciadofabricante.
Hámuitascríticas,contudo,aoJCPeaoprocessodeespecificaç ãodoJavano
geral.Fala-sedademoradasnovasespecificaçõesequeoJCPadotaapenasaspectos
maisbásicosdastecnologias,paraagradaratodos,travandoassimainovaç ão.Mas,
afinal,especificaçõesajudamouatrapalham?
Quandoumatecnologiaseestabelececomoumadasprincipaisemsuaárea,sua
evoluçãotorna-seinvariavelmentemaislenta.Novasideiasquesurgemnomercado
tentamatacarospontosnegativosqueatecnologiapadrãopossui,eoprocessonatu-
8

## Página 29

CasadoCódigo Capítulo1. AplataformaJava
raléqueumadessassetorneonovopadrãodentrodealgumtempo.Ummotivopara
atecnologiapadrãonãoadotaressasinovaçõeséseusucessosedeveraosresulta-
dosjáobtidosanteriormentenomercado.Masproblemasesoluçõessãotemporais,
dependemdarealidadenomomentoemquesãoestudados.
AlinguagemJavaviveumasituaçãosimilar.Desenvolvidapararesolverdetermi-
nadosproblemas,asbarreirasqueapresentasãomuitasvezessuperadaspelamistura
comoutraslinguagensdentrodaplataformaJava.Umdosgrandesconflitosdalin-
guagemégarantircompatibilidadecomversõesanteriores.Éumfatorimportante
paradarseguran çaaosusuáriosegarantirlargaado ção,e,aomesmotempo,um
freionaquantidadeaceitadeinovaçãoeevolução.
Naplataforma.NETháumhistóricodemenorrigidezemrelaç ãoàcompatibi-
lidade. AlinguagemC#evoluiumaisrapidamente,removendodecisõeshojecon-
sideradasruinseincorporandooutrasconsideradasinteressantes,comolambdase
ExtensionMethods.[36]Aomesmotempo,aquebradecompatibilidadecausades-
contentamentodediversosclientes.Desenvolvedoresprecisamdenovostreinamen-
tos,oVisualStudioéalteradoediversasbibliotecasdeixamdefuncionar.Porisso,a
partirdo.NET2.0nãohouvemaisquebrasdecompatibilidade,apenasnovasbibli-
otecasefuncionalidades.
NocasodaplataformaJava,oJCPutilizaseucomitêparadefinirosrumosdas
especificações.Éumaabordagemconhecidacomo DesignbyCommittee,visandoco-
locarasespecificaçõesnasmãosdemaisdeumaempresa.Aomesmotempo,diver-
sasinovaçõesaconteceramecontinuamasurgir,emprodutosproprietárioseopen
sourceque,comopassardotempoeaado çãopelomercado,acabamsendopadro-
nizadosatravésdoJCP.Sendoassim,especificaçõessãocomumentecriadas,oupara
gerarinovações,ouparapadronizaraquiloqueomercadoinovoueadotoucomo
boastecnologias.
Porém,oprocessointroduzidopelocomitêimplicamaiorlentidãonainovaç ão.
Seháquebradecompatibilidade,dificilmenteamudan çaseráadotada.Umafunci-
onalidadepodesertecnicamenteexcelenteparadeterminadosusuários,mas,sefor
contraosinteressesdeumdosmembrosdocomitê,poderáserdeixadadefora.Se
nãoháconsenso,nãoentra,ou,pior,estende-seadiscussãopormuitotempo.
Eventualmente,extensõesàespecificaçãoficampopulares,comoa CriteriaAPI
doHibernate,quenãofezpartedaprimeiraversãodaJPA(JSR-220).Casoasoutras
implementaçõesdaespecificaçãoprecisemdemuitoesfor çoparasuportarumanova
funcionalidade,osmembrosdaespecificaçãopodemcriarbarreiraseafuncionali-
dadepodeatémesmonãoentrarparaaJSR,ouentrarcomdiversasmudan çasque
9

## Página 30

1.2. Especificaçõesajudamouatrapalham? CasadoCódigo
nãonecessariamentefazemsentidodopontodevistatecnológico.Oprocessoburo-
cráticoeotempogastopelosdesenvolvedoresadaptandoaimplementaç ãopodem
defasarasespecificações(Figura1.3).
Figura1.3:Comoainovaçãonomundoopensourceestárelacionadaàsespecifica-
ções.
Masexistemdiversosmotivosquetornamasespecificaçõesatraentes. Amais
frequentementecitadaéaop çãodemudaraimplementação,minimizandooefeito
devendorlock-in. Porém,naprática,érarotrocarmosaimplementaçãodeuma
especificação,anãosertalvezconsiderandodiferentesambientes,comoirdodesen-
volvimentoparaaprodução.
Apesardetalvantagem,muitasvezesumaimplementaç ãoespecíficaacabapor
dominaromercado,comonocasodoHibernate. Éraroencontrarsituaçõesem
queequipestrocaramoHibernateporoutraimplementaç ãodeJPA,masécomum
outrasimplementaçõesseremtrocadaspeloHibernate.Nessesentido,seoprojeto
jáusaHibernate,aespecificaçãopodemaislimitarqueengradeceroprojeto.Além
disso,otimizaçõescostumamserfeitasparaimplementaçõesespecíficas.
Aoadotarumaespecificação,oprogramadoreoarquitetodevemlevaremcon-
sideraçãoasperdas,devidoàabstraç ão,eosganhosdeumpadrão,quefacilitea
entradadenovosdesenvolvedoresedesacoplaosucessodeumprojetodeumúnico
vendor.
Umagrandevantagemdasespecificaçõeséacertezadequeconhecê-lapermi-
tiráaodesenvolvedortrabalharemprojetosquetenhamdiferentesimplementações.
Claroquehaverádiferençasaseremaprendidas,masteraespecificaçãodiminuibas-
tanteesseaprendizado.
Outropontomuitasvezescitadoéqueasespecificaçõestrazemcertasgarantias
defuturoecontinuidadeparaaquelatecnologia,deixandooprojetolivreatédede-
10

## Página 31

CasadoCódigo Capítulo1. AplataformaJava
terminadofabricantecasoeleparedesuportarseuprodutooumudesuapolítica
comercial. Istonãosignificaqueprojetosopensourceetecnologiasproprietárias
nãotenhamessasgarantias,masadotarumaespecificaç ãopodetrazeraindamais
garantiasdefuturoquandoissoformuitonecessário.Porém,hácasostambémde
especificaçõespraticamenteabandonadas,comoaJDO,queémuitopoucousadae
jásuperadapelaJPA.
Comoqualquerescolha,desenvolvervoltadoàespecificaç ãoouusartecnolo-
giasproprietáriaséumadecisãoasertomadaapartirdasvantagensedesvantagens
decadaabordagem.AplataformaJava,diferentedemuitasoutras,temessapossi-
bilidadedeescolhadisponívelemsuasdiversasramificações. Quandoforpreciso
umaespecificaçãodealgumatecnologia,provavelmenteaplataformaJavateráalgo
disponível. E,quandoforconvenientealiberdadeeinovaç ãodastecnologiaspro-
prietárias,certamentetambémencontraremosalgo.
1.3 U se a linguagem certa para cada problema
ComopassardotempoeoamadurecimentodaplataformaJava,percebeu-seque
alinguagemajudavaemmuitospontos,mastambémimpediaumdesenvolvimento
maisaceleradoempartesespecíficas.
Osprimeirosindíciosdanecessidadedeoutrasfuncionalidadesnalinguagem
Javasãoantigos. Algumasdelasforamsupridascomadisseminaç ãodetécnicas,
comoproxiesdinâmicos,emvezdosstubspré-compiladosencontradosemRMIe
EJB1.xe2.x.Ou,ainda,asanotaçõesJavaparadiminuirasconfiguraçõesXML,antes
comunsemframeworkscomooXDocleteoSpring.
Outras necessidades foram resolvidas com a manipulação de bytecodes em
tempodeexecuçãocomaexplosãonaado çãodebibliotecascomessefim,como
ASMouJavassist.HáaindalinguagenscomoGroovyeoutrasforamdesenvolvidas
parafacilitaracriaçãodecódigomaisadequadoàtipagemdinâmica.
Comisso,outraslinguagens,atéentãoconsideradassecundáriaspelomercado,
começaramatomarfor çaporpossuíremmaneirasdiferenciadasderesolverosmes-
mosproblemas,mostrando-semaisprodutivasemdeterminadassituações.
ParaaplicaçõesWebemJava,porexemplo,écomumaado çãodeoutraslingua-
gens.Grandepartedotempo,utiliza-seCSSparadefinirestilos,HTMLparapáginas,
JavaScriptparacódigoqueserárodadonocliente,SQLparabancosdedados,XMLs
deconfiguraçãoe expressionlanguage(EL)nosJSPs.Mas,sejáusamosalinguagem
certaparaatarefacerta,porquenãoaproveitarestapráticaemtodaaaplicaç ão?
11

## Página 32

1.3. Usealinguagemcertaparacadaproblema CasadoCódigo
Porquenãoacrescentarmaisumalinguagemseestaresolveromesmoproblemade
maneiramaissimpleseelegante?
Aplataforma.NETjáfoicriadatendocomoumdeseusobjetivosuportardi-
versaslinguagens.ASunpercebeuposteriormentequenãoapenasalinguagemJava
poderiaseaproveitardasvantagensdaplataforma:oexcelentecompiladorJIT,algu-
masdasmelhoresimplementaçõesdeGarbageCollectorexistentes,aportabilidade
eaquantidadedebibliotecasjáconsolidadasnomercadoeprontasparaserusadas.
Hoje,aJVMécapazdeinterpretarecompilarcódigoescritoemdiversaslingua-
gens. ComoRhino,códigoJavaScriptpodeserexecutadodentrodaJVM.Assim
comocódigoRubypodeserexecutadocomJRuby,PythoncomJythonePHPcom
Quercus.ExistemlinguagenscriadasespecificamentepararodarsobreaJVM,como
Groovy,Beanshell,ScalaeClojure. OalemãoRobertTolksdorfmantémumalista
damaioriadaslinguagenssuportadaspelaJVMemseusite,[204]ondeépossível
encontraratémesmoimplementaçõesdalinguagemBasic.
Muitosperguntamqualseriaautilidadedeexecutar,porexemplo,códigoJa-
vaScriptnaJVM.Arespostaestánascaracterísticasdalinguagem,afinal,aplata-
formaseráamesma.Apesardetodoopreconceitoqueexistesobreela,JavaScript
vemsetornandoumalinguagemdeprimeiralinha,queéadotadaemoutrospon-
tosdenossaaplicação,enãoapenasnocontatofinalcomocliente. Oartigo“A
re-introductiontoJavaScript”mostracomoalinguagemvaialémdostutoriaissim-
plesqueencontramosnaInternet.[215]Eaado çãodeplataformasservidoras,como
oNode.js,mostramcomoJavaScripttambémpodeserumalinguagemdeusogeral.
UmexemplosimplesdeusodeJavaScriptéparaevitaraduplicaç ãodecódigo;
sejáexisteumavalidaçãodeCPFdoclientefeitaviaJavaScript,podemosreutilizar
essepedaçodecódigonoservidor,garantindoofuncionamentodosistemamesmo
nocasodeJavaScriptestardesabilitadonocliente.Ocódigocontinuasendoexecu-
tadodentrodaJVMcomtodasasotimizaçõesligadasàcompilaç ãosobdemandado
mesmo.NãoéàtoaqueasnovasversõesdoHibernateValidatorpermitemquesua
validaçãoserverside sejaemJavaScript.
ÉcomumencontraraplicaçõesJavarodandoRubyduranteoprocessodebuild,
atravésdeferramentascomoRakeeCucumber,para,porexemplo,efetuarostestes
end-to-endatravésdeumbrowser. ORailsrodandosobaJRubyécadavezmais
adotado.
OGrails,umframeworkbaseadonosconceitosdoRails,maslevadoàplata-
formaJavaatravésdalinguagemGroovy,tambéméadotadoparaacriaç ãodepro-
jetosWebemgeral. Essalinguagemtambémpodeserutilizadajuntamentecom
12

## Página 33

CasadoCódigo Capítulo1. AplataformaJava
BeanshellouRubyparaconfigurarframeworkscomooSpring,quejánãoestámais
sólimitadoaXML.
Emarquiteturasmodernas,écomumencontraraplicaçõesWebdesenvolvidas
sobaplataformaJava,porexemplo,noclouddoGoogleAppEngine,escritasemJava
eemRuby,interagindoatravésdeJRubyetestadaviaRubyeJSpec.Odesenvolvedor
precisadominarcadavezmaislinguagensparatirarproveitodetodaselas. Háo
contrapontonamanutenibilidadedocódigo:maislinguagensexigemmaistrabalho,
eénecessáriomedirmuitobemesse trade-off.
AtendêncianamescladelinguagensétãofortequeaSuncriouoprojeto MLVM
(MultiLanguageVirtualMachine),tambémconhecidocomo DaVinciMachine. O
projetobuscaviabilizarumconjuntodeespecificaçõesparamelhoraraexecuç ãode
códigoescritoemoutraslinguagens,especialmenteaslinguagensdinâmicas.Existe
umainiciativaparecidanaplataforma.NET,o Dynamic Language Runtime–DLR.
Umdosprincipaisavan çostrazidospeloprojetoDaVinciMachine éumnovo
bytecodechamado invokedynamic,umadasprincipaismudan çasnoJavaSE7. O
invokedynamicpermitequemétodosnãodefinidosemtempodecompilaç ãopos-
samseracessadosatravésdecódigoJavapuro,facilitandoamisturacomoutraslin-
guagensquetrouxeramobjetoscomcaracterísticasdinâmicasparadentroda Vir-
tualMachine,comooJRuby.Éummomentoimportantenadire çãodoJavacomo
plataformamultilinguagem.Éaprimeiravezqueumnovobytecodeéadicionadoà
plataformaparanãoserusadopelalinguagemJavaemsi,masporoutraslinguagens.
Aindaseguindoessecaminhodalinguagemcorretanoinstanteadequado,sur-
giuumfortemovimentoquebuscaobomusodelinguagensapropriadasaodomínio
aseratacado,as DomainSpecificLanguages.Existemdiversostipos,característicase
maneirasdecriá-las,semprecomointuitodetrazerparaocódigoumalegibilidade
quesejamaisnatural.
Linguagens funcionais
Em2009,SteveVinoskichamouaaten çãoparaaretomadadapopularidadedo
usodelinguagensfuncionaisnaWeb,[207]causadaprincipalmentepelafacilidade
desetrabalharcomconcorrênciaeexpressividade.
Operaçõescomuns,comotirarumamédiadepreçodeumaList<Produto>,vão
consumiralgumaslinhasdecódigoemJava,mesmocomoauxíliodebibliotecas
externasquepossuam Predicates.Comofuncional,comoemScala,umsimples
media(produtos)(_.preco)fazessetrabalho,epodeserreaproveitadoparacalcu-
laramédiadetempogastodeuma List<Processos>,dadoquetemosinúmeras
13

## Página 34

1.3. Usealinguagemcertaparacadaproblema CasadoCódigo
primitivasfuncionais,comoo foldLeft(conhecidocomo accumulateou reduce
emoutraslinguagens):
def media[T](itens:List[T])(valorador: T => Double) =
itens.foldLeft(0.0)(_ + valorador(_)) / itens.size
QuandoJavaquebrouabarreiradequemáquinasvirtuaisseriamnecessaria-
mentelentas,ajudouadesconstruirtambémomitosimilaralinguagensfuncionais,
queexistememversõesinterpretadasquantocompiladas.
Poroutrolado,comadesaceleraçãodoaumentodapotênciadeumprocessador,
omercadovoltou-separaoladodoscomputadoresmulti-coreelinguagensfuncio-
naismaispuras,fortementeembasadasnaimutabilidade,quepodemsebeneficiar
detaisprocessadoresdemaneiramaissimpleseeficiente,semusomanualdelocks
edelimitaçõesderegiõescríticas.Afacilidadetrazidapelasclosures,apartirdoJava
SE8,[186]étambémumdiferencialaserconsiderado,diminuindodrasticamenteo
númerodeclassesanônimas,tornandoocódigomaislegívelemenosverboso.
Comisso,padrõesquesãomaissimplesdeimplementaremlinguagensfuncio-
naispodemsermaiscomplicadosemoutrosparadigmas,evice-versa.
Podemosescolheramelhorlinguagemparacadatarefa,reaproveitandotodaa
bibliotecajáexistenteemJava,ecomunicandoentreelasdemaneiratransparente.
14

## Página 35

Capítulo2
JavaVirtualMachine
ComaJVMnocentrodaPlataformaJava,conhecerseufuncionamentointernoé
essencialparaqualqueraplicaçãoJava.Muitasvezes,deixamosdeladoajustesim-
portantesdeGarbageCollector,nãoentendemosasimplicaçõesdoJITnonosso
designouenfrentamosproblemaspráticoscomClassLoaders.
DentreosdiversostópicosassociadosàJVM,destacamosalgunsquejulgamos
vitaisparatododesenvolvedorJava.
2.1 P rincípios de garbage collection
Durantemuitotempo,umadasmaioresdificuldadesnahoradeprogramarerao
gerenciamentodememória.Osdesenvolvedoreseramresponsáveispelasuaaloca-
çãoeliberaçãomanualmente,oquelevavaamuitoserrose memoryleaks.Hoje,em
todasasplataformasmodernas,Javainclusive,temosgerenciamentodememória
automáticoatravésdealgoritmosdecoletadelixo.
O Garbage Collector (GC)éumdosprincipaiscomponentesdaJVMeres-
ponsávelpelaliberaçãodamemóriaquenãoestejamaissendoutilizada.Quandoa

## Página 36

2.1. Princípiosdegarbagecollection CasadoCódigo
aplicaçãoliberatodasasreferênciasparaalgumobjeto,estepassaaserconsiderado
lixoepodesercoletadopeloGCaqualquermomento. Masnãoconseguimosde-
terminaromomentoexatoemqueessacoletaocorrerá;istodependetotalmentedo
algoritmodogarbagecollector.Emgeral,oGCnãofarácoletasparacadaobjetoli-
berado;eledeixaráolixoacumularumpoucoparafazercoletasmaiores,demaneira
aotimizarotempogasto.Essaabordagem,muitasvezes,ébemmaiseficiente,além
deevitarafragmentaçãodamemória,quepoderiaaparecernocasodeumprograma
quealoqueelibereamemóriademaneiraingênua.[39]
Mas,comoérealizadaessacoletaexatamente?Vimosqueelanãoéfeitalogoque
umobjetoficadisponível,mas,sim,detemposemtempos,tentandomaximizaraefi-
ciência.Emgeral,aprimeiraideiaqueapareceaosepensaremGCéqueeleficavar-
rendoamemóriaperiodicamenteeliberaaquelesobjetosqueestãosemreferência.
EstaéabasedeumconhecidoalgoritmodeGCchamado Marck-And-Sweep,[159]
constituídodeduasfases:naprimeira,oGCpercorreamemóriaemarca(mark)to-
dososobjetosacessíveispelasthreadsatuais;nasegunda,varre(sweep)novamente
amemória,coletandoosobjetosquenãoforammarcadosnafaseanterior.
Essealgoritmoenvelheceu,damesmaformaqueoingênuo referencecounting.
Estudosextensivoscomváriasaplicaçõeseseuscomportamentosemtempodeexe-
cuçãoajudaramaformarpremissasessenciaisparaalgoritmosmodernosdeGC.A
maisimportantedelaséa hipótese das gerações.[206]
Segundoestahipótese,geralmente95%dosobjetoscriadosduranteaexecuç ão
doprogramatêmvidaextremamentecurta,istoé,sãorapidamentedescartados.É
oqueartigosacadêmicoschamamdealtoíndicede mortalidadeinfantil entreos
objetos.Ahipótesedasgeraçõesaindadizqueosobjetossobreviventescostumam
tervidalonga. Combasenessasobservações,chegou-seaoquehojeéconhecido
comooalgoritmo generational copying,usadocomobasenamaioriadasmáquinas
virtuais.[137][160]
Ésimplesobservaressepadrãogeracionalemmuitosprogramasescritosem
Java,quandoobjetossãocriadosdentrodeummétodo. Assimqueométodoter-
mina,algunsobjetosqueforamcriadosláficamsemreferênciasesetornamelegí-
veisàcoletadelixo,istoé,elessobreviveramapenasduranteaexecuç ãodométodo
etiveramvidacurta.
Mesmométodoscurtosesimples,como toString,acabamgerandoobjetosin-
termediáriosquerapidamentenãoserãomaisreferenciados:
public String toString() {
return “[contatos: “+ listaDeContatos + “]”;
16

## Página 37

CasadoCódigo Capítulo2. JavaVirtualMachine
}
Aqui,duranteaconcatenaçãodastrêspartesda String,um StringBuilderserá
utilizado,eomesmovaiocorrerparaainvocaç ãoimplícitado toStringdacoleção
listaDeContatos,quegerauma Stringapartirdeoutro StringBuilder. Todos
essesobjetospodemserrapidamentedescartados,etalvezopróprioretornodomé-
todoseráreferenciadoapenasporumbreveinstante.
Nogenerationalcopying,amemóriaédivididaemgerações,quegeralmentesão
duasyounggeneration eoldgeneration (Figura2.1). Ageraçãonovaétipicamente
menorqueavelha;aJVMHotSpot,porexemplo,estáprogramadaparaocupar,
porpadrão,atéumter çodoespaçototal. Todonovoobjetoéalocadonestaparte
e,quandoelaseencher,oGCrealizaráseutrabalhoembuscadesobreviventes.O
truqueestájustamentenofatodequeoGC,nestecaso,varreapenasageraç ãojovem,
queébempequena,semterdeparalisaraJVM(stop-the-world )pormuitotempo.
Osobjetosquesobrevivemàcoletasão,então,copiadosparaageraç ãoseguinte,
etodooespaçodageraçãonovaéconsideradodisponívelnovamente.Esseprocesso
decópiadeobjetossobreviventeséquedánomeaoalgoritmo.
Figura2.1:Divisãodasgeraçõesnoheap.
Pode-sepensarqueo generationalcopying nãoétãobom,pois,alémdeliberar
objetosdamemória,gastatempocopiandoossobreviventes.Masseugrandetrunfo
équeeleagenosobjetossobreviventes,enãonosdescartados,comofariaumal-
goritmotradicional.Nodescarte,osobjetosnãosãoverdadeiramenteapagadosda
memória;oGCapenasmarcaamemóriacomodisponível.Segundoahipótesedas
gerações,portanto,ogenerationalcopyingrealizarácópiaemapenas5%dosobjetos,
osquetêmvidamaislonga.E,emboraumacópiasejarelativamentecustosa,copiar
apenasospoucossobreviventesémaisrápidoqueliberar,umporum,osdiversos
objetosmortos.
Novosobjetossãoalocadosnayounge,assimqueelaestiverlotada,éefetuado
ochamado minor collect.Énestepassoqueosobjetossobreviventessãocopiados
paraaold,etodooespaçodayoungtorna-sedisponívelnovamenteparaaloca-
17

## Página 38

2.1. Princípiosdegarbagecollection CasadoCódigo
ção. Commenorfrequência,sãoexecutadosos major collects,quetambémcole-
tamnageraçãooldusandoo mark-and-sweep.Majorcollectssãotambémchamados
FullGC,ecostumamdemorarbemmais,jáquevarremtodaamemória,chegando
atravaraaplicaçãonosalgoritmosmaistradicionais(nãoparalelos).
ÉpossívelfazerumaobservaçãosucintadocomportamentodoGCmesmosem
umprofiler,bastandousaraop ção -verbose:gcaoiniciaraJVM.Ologdeexecuç ão
doGCmostraafrequênciadaschamadasaos minoremajorcollects,bemcomoa
eficiênciadecadachamada(quantodememóriafoiliberado)eotempogasto. É
importanteobservaressesvaloresparaperceberseoprogramanãoestágastando
muitotemponosGCs,ouseascoletasestãosendoineficientes.Umgargalopossível
deserencontradoéageraçãoyoungmuitopequena,fazendocomquemuitosobjetos
sejamcopiadosparaaoldpara,logoemseguida,seremcoletadosemuma major
collect,prejudicandobastanteaperformancegeraldoGCeaeficiênciados minor
collects.
UmmitomuitocomuméodequeestressamosoGCsecriarmosmuitosobjetos.
Naverdade,comoosalgoritmosestãoadaptadossegundoahipótesedasgerações,
omelhorsãomuitospequenosobjetosquelogosetornamdesnecessários,doque
poucosquedemoramparasairdamemória.Emalgunscasos,atéotamanhodoob-
jetopodeinfluenciar;naJRockit,porexemplo,objetosgrandessãoalocadosdireto
na::oldgeneration:;,logonãoparticipamdacópiageracional.
Amelhortécnicaqueumdesenvolvedorpodeutilizaréencaixarademandade
memóriadasuaaplicaçãonahipótesedasgeraçõesenasboaspráticasdeorientação
aobjetos,criandoobjetospequenoseencapsuladosdeacordocomsuanecessidade.
Seocustodecriaç ãodoobjetonãoforgrande,segurarsuasreferênciasoufazer
cachesacabasendopior.Obviamente,issoexcluicasosemqueocustodecriaç ãoé
grande,comoumlaçodeconcatenaçãode Stringatravésdooperador+;nessecaso,
émelhorusar StringBuildersouStringBuffers.
Umefeitocolateralinteressantedoalgoritmodecópiadeobjetoséa compacta-
çãodamemória.AlgoritmosingênuosdeGCcostumamcausargrandefragmenta-
cão,porqueapenasremovemosobjetosnãomaisusados,eossobreviventesacabam
espalhadosecercadosdeáreasvazias. O generationalcopying copiaosobjetosso-
breviventesparaoutrageraçãodeformaagrupada,eamemóriadageraç ãoanterior
éliberadaemumgrandeeúnicobloco,semfragmentaç ão.Foraisso,outrasestra-
tégiasdecompactaçãodememóriaaindapodemserusadaspelaJVM,inclusivena
oldgeneration. Éimportantenotarqueissosóépossívelporcausadomodelode
memóriadoJava,queabstraitotalmentedoprogramaaformacomoosponteiros
18

## Página 39

CasadoCódigo Capítulo2. JavaVirtualMachine
eendereçosdememóriasãousados.Épossívelmudarobjetosdelugaraqualquer
momento,eaVMprecisaapenasatualizarseusponteirosinternos,oqueseriamuito
difícilderealizaremumambientecomacessodiretoaponteirosdememória.
Explorando o gerenciamento de memória nas JVMs
AáreatotalusadaparaarmazenarosobjetosnaJVMéchamadaheap.Otama-
nhodoheapdememóriadamáquinavirtualécontroladopelasop ções-Xmse-Xmx.
Aprimeiraespecificaotamanhoinicialdoheap,easegunda,otamanhomáximo.
Inicialmente,aJVMalocanosistemaoperacionalaquantidadeXmsdememóriade
umavez,eessamemórianuncaédevolvidaparaosistema.Aalocaç ãodememória
paraosobjetosJavaéresolvidadentrodaprópriaJVM,enãonosistemaoperaci-
onal. Conformemaismemóriaénecessária,aJVMalocaemgrandesblocosatéo
máximodoXmx(seprecisardemaisqueisso,um OutOfMemoryErrorélançado).É
muitocomumrodaramáquinavirtualcomvaloresiguaisdeXmseXmx,fazendo
comqueaVMaloquememórianosistemaoperacionalapenasnoinício,deixando
dedependerdocomportamentoespecíficodoSO.
Conheceressaseoutrasop çõesdogarbagecollectordasuaJVMpodeimpactar
bastantenaperformancedeumaaplicação.Considereocódigoaseguir:
for (int i = 0; i < 100; i++) {
List<Object> lista = new ArrayList<Object>();
for (int j = 0; j < 300000; j++) {
lista.add(new Object());
}
}
RodandoumprogramacomessecódigonomainnaJVM6HotSpot,usandoo
-clientpadrãocom64mdeXmseXmx,aohabilitaro -verbose:gcobtemosuma
saídacomoesta:
[GC 25066K->24710K(62848K), 0.0850880 secs]
[GC 28201K(62848K), 0.0079745 secs]
[GC 39883K->31344K(62848K), 0.0949824 secs]
[GC 46580K->37787K(62848K), 0.0950039 secs]
[Full GC 53044K->9816K(62848K), 0.1182727 secs]
....
Osvaloresmostradosemcadalinhacorrespondema:memóriaemusoantesda
coleta,memóriadepois,totaldememóriadaJVMeotempogastonacoleta.Asaída
19

## Página 40

2.1. Princípiosdegarbagecollection CasadoCódigo
realébemmaior,maspraticamenterepeteosmesmospadrões.Épossívelperceber
queos minorGCsãomuitopoucoeficientes,liberampoucamemória,aocontrário
dosFullGC queparecemliberarmuita. Issoindicafortementequeestamosindo
contraahipótesedasgerações.Osobjetosnãoestãosendoliberadosenquantoainda
jovens,nemsendocopiadosparaageraç ãovelha,deonde,depoisdeumtempo,
serãoliberados.Nestenossocaso,oalgoritmodeGCbaseadoemcópiadeobjetosé
umimensogargalodeperformance.
Propositadamente,ocódigodetestesegurareferênciasporumtempoquees-
tressaoGC.Emumaaplicaçãoreal,oidealseriaalterarocódigoparaqueseadapte
melhoràhipótesedasgerações.Mas,quandoocomportamentodasuaaplicaç ãoé
diferentedohabitual,bastaalteraralgumasconfiguraçõesdogarbagecollectorpara
obteralgumganho.
Emnossamáquinadetestes,semalterarotamanhototaldoheap,aoaumentar
odayounggenerationusandoaop ção -XX:NewRatio=1(opadrãoé2naHotSpot),
temosumganhodemaisde50%naperformancegeraldaaplicaç ão. Essaopção
mudaapropor çãoentreostamanhosda younggenerationeda old.Porpadrão,2/3
serãoolde1/3seráyoung;aomudarovalorpara1,teremos1/2paracadaárea.Claro
queesseganhodependemuitodoprogramaedaversãodaJVM,mas,aoolharagora
paraasaídadoprograma,épossívelobservarcomoumapequenamudan çaimpacta
bastantenaeficiênciadoGC:
[GC 49587K->25594K(61440K), 0.0199301 secs]
[GC 43663K->26292K(61440K), 0.0685206 secs]
[GC 47193K->23213K(61440K), 0.0212459 secs]
[GC 39296K->21963K(61440K), 0.0606901 secs]
[GC 45913K->21963K(61440K), 0.0215563 secs]
...
Nosnovostestes,o FullGC nemchegaaserexecutado,porqueospróprios mi-
norgc sãosuficientesparadarcontadosobjetos.E,comooalgoritmodeGCéba-
seadoemcópias,poucosobjetossãocopiadosparaa oldgeneration,influenciando
bastantenaperformancedoprograma. Saiba adequar sua aplicação à hipótese das
gerações, seja adequando seu código, seja conhecendo as melhores configurações
de execução da sua JVM.
PensandoemcomousufruirdessascaracterísticasdoGC,oqueémelhorpara
umaaplicação: usarobjetosgrandes,cachesgigantesdeobjetoseabusardeatri-
butosestáticos;ouescreverdiversospequenosobjetoscriadoseliberadosatodo
momento? SegurarobjetosnamemóriaestressademaisoGCbaseadoemcópias
20

## Página 41

CasadoCódigo Capítulo2. JavaVirtualMachine
deobjetos.AboapráticadeOrientaçãoaObjetosjádizquedevemoscriarpeque-
nosobjetosencapsulados,semmuitosdadosestáticos,originandoinstânciassem
nospreocuparmoscomcacheseoutrasalegadasotimizações. Seseguirmosaboa
prática,oGCtambémfuncionarámelhor.AJVM,deummodogeral,foiescritae
adaptadaaolongodesuavidaparasuportarodesenvolvedornasboaspráticas.
OutropontoparticulardaJVMHotSpotdaOracle/Sun(esuasderivadas)éa
chamadapermanentgeneration,ou PermGen(Figura2.2).Éumespaçodememó-
riacontadoforadoheap(alémdoXms/Xmxportanto),ondesãoalocadosobjetos
internosdaVMeobjetosClass,Method,alémdo pool de strings. Aocontrário
doqueonomepareceindicar,esseespaçodememóriatambémécoletado(du-
ranteos FullGC),mascostumatrazergrandesdoresdecabe ça,comoosconheci-
dos OutOfMemoryError,acusandoofimdo PermGenspace.Aprimeiradificuldade
aquiéque,pornãofazerpartedoXms/Xmx,o PermGenconfundeodesenvolve-
dor,quenãoentendecomooprogramapodeconsumirmaismemóriadoquea
definidano -Xmx. ParaespecificarotamanhodoPermGen,usa-seoutraop ção,a
-XX:MaxPermSize.
Figura2.2:DivisãodamemórianaJVMdaSun.
Masosproblemascomestourodo PermGensãodifíceisdediagnosticar,justa-
menteporquenãosetratadeobjetosdaaplicaç ão.Namaioriadoscasos,estáligadoa
umaquantidadeexageradadeclassesquesãocarregadasnamemória,estourandoo
tamanhodoPermGen.Umexemploconhecido,queaconteciaantigamente,erausar
oEclipsecommuitosplugins(sabidamenteoWTP)nasconfiguraçõespadrõesda
JVM.PorcausadaarquiteturadepluginsbemorganizadaeencapsuladadoEclipse,
muitasclasseseramcarregadaseamemóriaacabava.
Umoutroproblemabemmaiscorriqueirosãoosestourosdo PermGenaose
fazermuitos hotdeploys nosservidoresdeaplicação. Porváriosmotivospossíveis
(comoveremosduranteotópicodeClassLoaders),oservidornãoconsegueliberar
21

## Página 42

2.1. Princípiosdegarbagecollection CasadoCódigo
asclassesdocontextoaodestruí-lo.Umanovaversãodaaplicaç ãoéentãocarregada,
masasclassesantigascontinuamnamemória.Éapenasumaquestãodetempopara
essevazamentodememóriaestouraroespaçodo PermGen.
Algoritmos de coleta de lixo
AplicaçõesdegrandeportepodemsofrercomoGC.Éfundamentalconhecer
algumasdasprincipaisop çõesquesuaJVMpossibilita.NocasodaHotSpot,aJVM
maisutilizada,diversosalgoritmosdiferentesestãodisponíveisparauso.[135][129]
Porpadrão,éusadoo Serial Collector,queébastanterápido,masusaapenasuma
thread.Emmáquinascomumoudoisprocessadores,elecostumaserumaboaes-
colha.Masemservidoresmaiscomplexos,comváriosprocessadores,podedesper-
diçarrecursos. Istoporqueeleéumalgoritmo stop-the-world,oquesignificaque
todoprocessamentodaaplicaçãodeveserinterrompidoenquantooGCtrabalha,
paraevitarmodificaçõesnamemóriaduranteacoleta.Mas,porserserial,implica
que,seumamáquinativermuitosprocessadores,apenasumpoderáserusadopelo
GC,enquantotodososdemaisficamociosos,poisnãopodemexecutarnenhuma
outratarefaenquantooGCroda.Istoéumdesperdícioderecursos,eumgargalo
emmáquinascomváriosprocessadores.
É possível então, na HotSpot, habilitar diversos outros algoritmos de
GC e até usar combinações deles. OParallel Collector (habilitado com
-XX:+UseParallelGC)conseguerodar minorcollects emparalelo. Eletambémé
stop-the-world,masaproveitaosváriosprocessadores,podendoexecutaroGC.Note
que,porcausadisso,oalgoritmoparaleloacabademorandoumtempototalmaior
queoserial,emrazãodocustodesincronizaroacessoàmemóriasendocoletada
(synchronized,semáforos,mutexes,....).Mas,comoestamosfalandodemáquinas
commuitosprocessadores,oqueacabaacontecendoéqueessetempoédivididoen-
treosváriosprocessadores,eoefeitoéqueseusamelhorohardwareesediminuio
tempodeparadaparacoleta.[135]Épossívelaindahabilitarumcoletorparalelopara
ageraçãooldeosmajorcollects,usando -XX:+UseParallelOldGC.
Quandoorequisitoprincipalédiminuirotempoderesposta,ouseja,diminuir
otempoqueaaplicaçãoficaparadaesperandooGC,omelhorpodeserusaro Con-
current Mark-and-sweep(CMS),tambémchamadode lowpausecollector (ativado
com-XX:+UseConcMarkSweepGC).Essealgoritmoagenageraçãooldeconseguefa-
zeramaiorpartedaanálisedamemóriasempararomundo. Eletemapenasum
pequenopedaçostop-the-world,oqueacabatornandootempoderespostabemme-
nor. Masopreçoquesepagaéqueoalgoritmogastamaisprocessamentototal,e
22

## Página 43

CasadoCódigo Capítulo2. JavaVirtualMachine
temcustosmaioresdecontroledeconcorrência.Podeserumaboaideiaemmáqui-
nascommuitosprocessadoresecombastantememóriaasercoletada.[135]Aousar
oCMS,ageraçãoyoungécoletadacomumalgoritmoparalelochamadoParNewe
épossívelatédesabilitá-loeusaroSerial.
A última novidade em relação a algoritmos GC é oG1, desenvolvido pela
Sun.[134]Éumalgoritmoconcorrentequetentatrazerumpoucomaisdeprevisibi-
lidadeparaoGC,umadasgrandescríticasdequempreferegerenciamentomanual
dememória.Apesardeserconsideradoumalgoritmogeracional,elenãoseparao
heapemduasgerações,esimemmuitaspequenasregiões. Dinamicamente,oG1
escolhealgumasregiõesparasercoletadas(oqueacabadandoosentidológicoda-
quelasregiõesserema younggen). Ointeressanteéqueépossívelespecificarpara
oG1tempomáximoasergastoemGCemumdeterminadointervalodetempo.O
G1,então,tentaescolherumnúmeroderegiõesparacadacoletaque,baseadoem
execuçõesanteriores,eleachaqueatingirãoametasolicitada.Comisso,espera-se
terumalgoritmodeGCmaiseficienteemaisprevisível,comparadasmaiscurtase
constantes.
EssesalgoritmosmudammuitodeumaJVMparaoutra.Osquatrojácitadossão
dasúltimasversõesdaJVM6edaJVM7daOracle/Sun.Outrasmáquinasvirtuais
possuemoutrosalgoritmos.AJRockit,porexemplo,permitedesabilitaroalgoritmo
geracionaleusarumbaseadono mark-and-sweepcomaop ção -Xgc:singlecon(há
outrostambémparecidoscomosalgoritmosparalleleconcurrentdoHotSpot).[43]
AAzulSystems,conhecidaporsuaJVMfocadaemaltaperformance,possuiemseus
produtos,desdeofimde2010,umGCsempausas.[196]
Amemóriapodeserumgargaloparasuaaplicaç ão;portanto,conhecerbemseu
funcionamentoeseusalgoritmospodeserpe ça-chaveparaosucessodeumprojeto.
2.2 N ão dependa do gerenciamento de memória
Comovimos,o GarbageCollectoréumdosserviçosmaisimportantesdaJVMeexige
poucoesforçoparausá-lo.Conhece-lo,alémdeseusalgoritmos,ajudanomomento
deescrevercódigosmelhoresenãotersurpresas.Masháaindaoutrasquestõesre-
lacionadasaocomportamentodoGC.
Umdosprincipaispontosésuanaturezaimprevisível. Porserumserviçoda
JVMquerodasimultaneamenteàsuaaplicaç ão,nãoconseguimoscontrolarexpli-
citamenteseucomportamento.Diferentedogerenciamentomanual,noqualtanto
aalocaçãoquantoaliberaçãodememóriasãochamadasexplicitamentepelode-
23

## Página 44

2.2. Nãodependadogerenciamentodememória CasadoCódigo
senvolvedor,emJavaeemoutraslinguagensbaseadasnaexistênciadeumGC,não
definimosospontosdecoleta.Apenasliberamosasreferênciasparaosobjetose,em
algummomento,acoletaseráefetuada.
Anãoexigênciadanecessidadedeexplicitaressacoletaéopontopositivodo
GC,poistiraessapreocupaçãododesenvolvedor,masétambémsuamaiorcrítica,
pelasuaimprevisibilidade.Elepodeficarmuitotemposemrodarnocasodeexistir
muitamemóriadisponívele,derepente,gastarmuitotempoemumaúnicaexecu-
ção,potencialmenteparalisandoorestantedaaplicaç ão.Sãoessasparalisaçõesque
osalgoritmos ConcurrenteG1tentamminimizar.
Algunsdesenvolvedorestentamescrevercódigoparaqueopróprioprograma
controlealgunsaspectosrelacionadosaoGCe,deummodogeral,issonãoéuma
boaideia.
Umaprimeiramápráticabastantecomuméainvocaç ãoao System.gc()na
esperançademinimizaraimprevisibilidadedoGCeaumentarsuafrequênciade
execuções. Essaabordagemapresentadiversosproblemas. Emprimeirolugar,o
métodonãogaranteaexecuçãodoGC,comodefinidoemseuJavaDoc:
InvocarométodoGCsugerequeaMáquinaVirtualJavafa çaumesfor çoparare-
ciclarobjetosnãoutilizadosafimdeliberaramemóriaqueelesocupamatualmente
pararápidareutilização.Quandoocontrolevoltadachamadadométodo,aMáquina
VirtualJavafezomáximoesfor çopararecuperarespa çodetodososobjetosdescarta-
dos.[42]
Ouseja,ainvocaçãodométodoéumasugestãoparaaexecuç ãodoGC,que
podeseratendidaounão. Emoutraspalavras,ainvocaç ãoao System.gc()não
garanteresultadoalgum. Porexemplo,aJVMdaOracle/Sun,porpadrão,sempre
segueasugestão,etodainvocaç ãoaestemétodoexecutaum FullGC.Namaioria
dasvezes,essaobediênciaéaindapior,umavezqueo FullGC,quenãodeveria
serexecutadocommuitafrequência,varretodooheap,demorandoparacompletar.
Alémdisso,aquantidadedememórialiberadaserápequenanocasodeinvocações
muitopróximas.
Umcasoencontradocomfrequênciaaparecequandoumprocessodentrodeum
laçoconsomemuitamemória,eosdesenvolvedoresdecideminvocar System.gc()
dentrodoloop,acarretandoumaenormeperdadeperformance:
public void processa(List<Cliente> clientes, List<Evento> eventos) {
for(Cliente cliente : clientes) {
for(Evento evento : eventos) {
cliente.analisa(evento);
24

## Página 45

CasadoCódigo Capítulo2. JavaVirtualMachine
System.gc();
}
}
}
PodemostentarfixarumintervalodeinvocaçõesdoGC,comoacadacincomi-
nutosouaotérminodaexecuçãodecadamétodo.MaséquasecertoqueaVMseria
capazdeescolhermomentosmaisapropriadosparaexecuçãodoGCdoquenós.Isso
porque,aocontráriodaVM,oprogramanãotemavisãogeraldamemóriadurante
todootempodeexecuçãoe,porisso,éincapazdecalcularexatamenteoimpactoda
coleta.
Porfim,mesmoqueinsistamosemfazeratalinvocaç ãoexplícita,éimportante
saberque,emruntime,épossíveldesabilitaraexecuç ãoarbitráriadoGC,oque
seráumproblemasenãocontrolamostudodoambientedeproduç ão.NaHotSpot,
porexemplo,aop ção XX:+DisableExplicitGC,passadaparaaJVMnalinhadeco-
mando,desabilitaaschamadasaSystem.gc(),ignorando-asporcompleto.Aliás,este
éocomportamentopadrãodemuitasoutrasJVMs.
O método finalize de Object
Nãopodemoscontrolaromomentodacoletadosobjetos,masépossívelserdele
notificadonessemomento.Uminstanteantesderemovercadaobjetodamemória,o
GarbageCollectorinvocaseumétodofinalize,notificando-odacoleta.Estemétodo
édefinidonaclasse Object,epodemosreescrevê-loemnossasclassescomcódigo
próprioaserexecutadoantesdeosobjetosseremcoletados.
public class DAO {
private Conexao conexao;
// métodos do DAO
@Override
public void finalize() {
super.finalize();
this.conexao.fecha();
}
}
Namaioriadasvezes,porém,usarestemétodocausamaisdoresdecabe çado
queresolveproblemas. Ométodopodeserexecutadomuitotempodepoisqueo
25

## Página 46

2.2. Nãodependadogerenciamentodememória CasadoCódigo
objetosetornouinacessível,ouatémesmonãoserchamadonunca. Imagineum
programaquerodacommuitamemória,quasenãoausaeexecutarapidamente;o
GCpodenãoterjamaisaoportunidadedeserexecutado.
Mesmoquandoforexecutado,seucomportamentoécomplicado.Ese,durante
afinalização,recuperarmosumareferênciadoobjetoemoutrolugar? OGCnão
ocoletae,napróximavezqueoobjetoestiverdisponível,ofinalizenãoseráexe-
cutadonovamente. Ouaindasenossaimplementaçãodestemétododeixarvazar
umaexceção,elaseráengolidaeafinalizaç ãodoobjetointerrompida. Seestiver-
mostrabalhandocomheran ça,precisamosgarantirainvocaçãodofinalizedamãe.
Alémdisso,asfinalizaçõessãoexecutadassequencialmenteporumathreadespecí-
fica,quepossuiumafiladeobjetosfinalizáveisemordemnãodeterminada,oque
fazcomqueumapossíveldemoranafinalizaç ãodeumobjetoatraseadealgumou-
troimportante. Todosessesproblemasseacumulamedificultamaescritadeum
métodofinalizeadequado.
Demodogeral,evitedependerdefinalizações,aindamaisseforumcódigoim-
portanteequenecessitadagarantiadeexecuç ão.Nãouseofinalizecomoúnicome-
canismodeliberaçãoderecursosimportantes,como,porexemplo,fecharconexões
ouarquivos.Semprequeseuobjetoexigiralgumprocessodefinalizaç ão,exponha
ummétodocloseoudisposeparaosdesenvolvedoreschamarem-noexplicitamente,
garantindoaexecuçãodessecódigoimportante.Comorecursode try-with-resources
doJava7,então,éaindamaisfácilgarantirqueodesenvolvedorchameocloseno
momentocerto.[45]
Umusopossívelparaofinalizeécomosegundomecanismodefinalizaç ão,in-
vocandoométodoprincipalcasoousuárioseesque çadefazê-lo.Éumaseguran ça
amais,masnãoumagarantiadeexecuç ão-nessecaso,ousuárioestavaerrado,pois
ocorretoseriaterchamadoocloseexplicitamente.
public class Leitor {
private final InputStream input;
public Leitor(InputStream input) {
this.input = input;
}
// métodos
public void finalize() {
close();
}
public void close() {
try {
26

## Página 47

CasadoCódigo Capítulo2. JavaVirtualMachine
input.close();
} catch(IOException ex) {
// logar ou algo diferente
}
}
}
Nosraroscasosemqueprecisarmostrabalharcomfinalizações, oJavadis-
ponibiliza um outro mecanismo mais robusto que ofinalize.[161] No pa-
cote java.lang.ref,[40] estão as classes de referências fracas (WeakReference,
SoftReferencee PhantomReference)e RefereceQueue. Comelas,odesenvolve-
dorconseguecontrolarsuaprópriafiladecoletaeprocessardojeitoquedesejaras
finalizaçõesdeseusobjetos.Outrousodereferênciasfracasépermitiraimplementa-
çãodecachesdeobjetosquenuncaestouramamemória.Pornãoseremreferências
normaisJava(fortes),elasnãoimpedemacoletadoobjeto,simplificandoaimple-
mentaçãodestetipodecache.Osdetalhesdereferênciasfracasestãoforadoescopo
desselivro,masrecomendamosseuusoquandofornecessáriodetectarfinalizações
deobjetos.
De um modo geral, não interferir no GC ou depender de seu comportamento
é uma boa prática.Programadoresmaisacostumadosaumcontrolefinodogerenci-
amentodememóriapodemsesentirdesconfortáveisemdeixartudonamãodaVM.
Masagrandevantagemdogerenciamentoautomáticodememóriaéjustamentenão
maisnospreocuparmoscomdetalhesdoGCeterumaimplementaç ãoeficienteà
nossadisposição.
2.3 JIT C ompiler: compilação em tempo de execução
QuandooJavafoilan çado,aJVMeraordensdemagnitudemaislentaquehoje,
interpretandoseucódigoquequalquerprogramanativoemC.Hoje,oJavaébastante
rápido,masaindacarregaesteestigmaoriginadonopassado.
AsprimeirasJVMseramsimplesmenteinterpretadoresdebytecodes.Liamar-
quivos.classetraduziamcadabytecodenasequênciadeexecuçãoparaasinstruções
demáquinaequivalentes.ApartirdoJava1.1,aSunincluiuseuprimeiro JIT Com-
piler,adquiridodaSymantec,e,noJava1.2,incluiuoHotSpot.Aevoluç ãodessas
duastecnologiasaolongodasversõesdoJavaéoquefazaJVMserequiparávela
aplicaçõesnativasemCeC++.
OsgrandesganhosdeperformancedoJavadevem-seàotimizaç ãoadaptativa,
istoé,acapacidadedefazerotimizaçõesdeacordocomousodoprogramaeas
27

## Página 48

2.3. JITCompiler:compilaçãoemtempodeexecução CasadoCódigo
condiçõesdomomento. TantoJavaquantoCpossuemumaetapadecompilaç ão
estática,quegeraumarquivobinárioaserexecutado,e,duranteessacompilaç ão,
váriasotimizaçõessãorealizadas.AdiferençaéqueobinárionativoCgeradoéexe-
cutadodiretamentenamáquina,eobinárioJavaéaindaexecutadoatravésdaJVM,
ondeoutrasotimizaçõesacontecem.NocasodoC,todaotimizaç ãopossíveléfeita
estaticamentepelocompilador,enquantoqueoJavaconsegueexecutarumasegunda
etapadeotimizaçõesdentrodaVMnomomentodacompilaç ãodosbytecodespara
códigonativo,nachamadacompilaçãodinâmica.ÉistooquefazoJavaexecutartão
rapidamente.
Duranteaexecuçãodoprograma,aJVMaanalisaedetectaospontosmaisim-
portanteseexecutadosdaaplicação.Essesmétodossãoentãocompiladosdinami-
camentepeloJITparacódigonativootimizado,etodaexecuç ãosubsequenteéfeita
comele,atingindoperformancecomparávelaC.AsVMsmaismodernasconseguem
atérecompilardeterminadométodocomotimizaçãomaisagressivacasopercebam
queaperformancemelhorará. Elastambémpercebemquedeterminadocódigojá
nãoémaisimportante,edescartamsuascompilações,ouquedeterminadaheurís-
ticaaplicadanãofoiboa,eaplicamumnovotipodeotimizaç ão.
AevoluçãoconstantedaJVMedoJITfazcomqueoJavasejacadavezmais
rápido. Mesmoumprogramaantigomelhorasignificativamentesuaperformance
seousuáriosimplesmenteatualizaraversãodaJVM.Emumprogramanativotra-
dicional,paraousuárioterumganhodeperformance,porexemplo,porcausade
umaversãonovadocompiladorC,eleteráqueesperardofabricanteumaversão
novarecompilada. Maisdoqueisso,muitosprogramascomerciaisemCexigem
ummínimodeportabilidade,como,porexemplo,rodardesdeoWindowsXPaté
oWindows7,ousuportarqualquerprocessadorInteleAMD.Paratanto,frequen-
tementeacompilaçãodoprogramaCéfeitausandorecursoscomunsatodasas
plataformasvisadas. Ouseja,umdenominadorcomumemrelaç ãoaotimizações,
instruçõesdemáquinaechamadasdosistema.JáoJava,pornãofazeracompilaç ão
paracódigonativoapenasestaticamente,consegueusarestratégiasfocadasnosis-
temaoperacionalenohardwareusadosnomomentodesuaexecuç ão,chegandoa
invocarinstruçõesespecíficasdoprocessadoremuso.
Otimizações para clientes e servidores
Diferentesaplicaçõestêmdiferentesnecessidadesdeperformanceeresponsivi-
dade.Pensandonisso,aJVMofereceperfisdiferentesqueadaptamofuncionamento
doJITeoutrascaracterísticasdaJVM.
28

## Página 49

CasadoCódigo Capítulo2. JavaVirtualMachine
Aplicações voltadas ao usuário final, geralmente clientes Desktop, têm uma
grandedemandaporinicializaçãorápida,emboranãoprecisemtantodeperfor-
mance;emgeral,ogargalonessasaplicaçõeséoinputdousuário.Sehabilitarmos
aopção -clientnaJVM,elaperdemenostemponostartupparaousuáriovero
resultadomaisrapidamente,masaocustodeterumJITfazendootimizaçõesme-
nosagressivasalongoprazo.Umdosfocosdestaconfiguraç ãoé,porexemplo,não
consumirmuitamemória,atédeixandodefazercertasotimizaçõesnoJITqueaca-
bariamaumentandoousodememória,como inlinedemétodos.
Jáaopção -serverprevêcenáriosnosquaisotempoinicialnãoéumgrande
problema,masexisteumapreocupaç ãomaiorcomaperformancealongoprazo.
Ostartupdemoramaisalgumtempo,eoJITrodaemumadesuasversõesmais
agressivasparaodesempenhodaaplicaç ão.[38]Ousodememóriaémaisintenso,
masaperformancedeexecuç ãoémaioralongoprazo. AVMserverabusa,por
exemplo,derecursoscomo inlinedemétodos,emqueocódigocompiladopeloJIT
jájuntanamemóriaocódigodosmétodosenvolvidosparaevitar jumpsaomáximo.
NasversõesmaisrecentesdaHotSpot,casonãopassemosaop çãoexplicita-
mente,aprópriamáquinavirtualescolheentreclienteserver,tamanhodoheap,
algoritmodeGCeoutrospontoscombasenotipodehardwarenoqualosoftware
estásendoexecutado–esterecursoéchamadodeVM ergonomics.[37]Háainda
opçõesexperimentais,comoa -XX:+AgressiveOptsquehabilitamaisotimizações.
Se desenhássemos um gráfico que mostrasse a relação entre performance e
tempoparaasVMsservereclient,eaindaumprogramaC,teríamosalgocomo
aFigura2.3,aseguir:
Figura2.3:Ilustraçãodaperformancedeumaaplicaç ãoaolongodotempo.
FácildesernotadoàprimeiravistaéoprocessodostartupdemoradoemJava.A
29

## Página 50

2.3. JITCompiler:compilaçãoemtempodeexecução CasadoCódigo
inicializaçãodaJVMtemmelhoradobastanteacadaversão,masaindaéumgargalo
importanteemaplicaçõescurtasouquetenhamumanecessidadedeiníciorápido.
EssademorasedeveàquantidadedeclassesqueaJVMprecisacarregarnocome ço,
etambémaotempoparaesquentaroJIT.NaHotSpot,porexemplo,oprograma
começaexecutandotudoemmodointerpretadoe,sódepoisdeidentificarospontos
quentes,équeoJITéacionadoparadeterminadométodo.Enquantoisso,naJVM
server,porpadrão,oJITfazaotimizaç ãoapósdezmilinvocações.JánaJRockit,há
umprimeiroJITcompilerquerodadesdeoiníciorealizandopoucasotimizaçõese,
conformeospontosquentessurgem,umsegundoJITmaisagressivorecompilaos
métodosescolhidos.
DadoestemonitoramentoqueaJVMfazparadecidiromomentocertodeoti-
mizarseucódigopeloJIT,ficaapergunta:oqueémelhor,escreverpequenosmé-
todosreaproveitáveisentresicommuitasinvocações,oumétodosgigantesquesão
invocadosumaspoucasvezes? Quebrarnossocódigoempequenosmétodos,que
concentramumaúnicaresponsabilidade,éamelhorprática.E,porquestõesdeper-
formance,paraoJIT,quantomaisreaproveitáveisforemseusmétodos,maisinvoca-
çõesserãofeitasemaisfocadasserãoasotimizações. *Programe baseado em boas
práticas, e deixe o JIT cuidar da execução otimizada.
Outropontoasenotaréaperformanceconstantenaaplicaç ãoC.Noinício,ela
éextremamentemaisrápida,mastodaotimizaçãopossívelemumprogramaCfoi
realizadaemcompilação.UmaaplicaçãoemJavapodetersuaperformancevariável
aolongodaexecução,deacordocomaatividadedoJIT.Emumaaplicaç ãoquenão
exijatantoI/Oethreads,aJVMémaduraosuficienteparaserequiparávelcomC
namaioriadassituações.
ÉpossívelvisualizarocomportamentodoJITusandoalgumasop çõesavançadas
daJVM.NaHotSpot,aop ção -XX:+PrintCompilationhabilitaummodoondetodo
métodocompiladopeloJITéimpressonoconsole. Aotestaremaplicaçõesbem
simples,compoucasinvocações,épossívelnotarqueoJITraramenteéacionado.
Emoutrascommaisinvocaçõesdemétodos(umbomtesteéusaralgumalgoritmo
recursivo),nota-sequeosmétodosmaisquentessãocompiladospeloJIT.
Mascomosaberosmétodosaseremcompilados? NaHotSpot,aousaraVM
client,opadrãoéaguardar1.500invocaçõesdeummétodoatécompilá-lo.JánaVM
server,sãoaguardadas10.000invocaçõesantesdacompilação.É,aliás,oquenosso
gráficoanteriorindicava,queaVMserverdemoraumpoucomaisparaesquentar,
mastemumaperformancemelhoralongoprazo.
NaHotSpot,épossívelcontrolaronúmerodeinvocaçõesaseremaguardadas
30

## Página 51

CasadoCódigo Capítulo2. JavaVirtualMachine
antesdascompilaçõesusandoaop ção -XX:CompileThreshold=<NUM>passandoo
númerodesejado. Muitaspessoasperguntam-seporqueoJITnãocompilatodos
osmétodos,rodandotudodeformanativaeotimizada.Éfáciltestarestecaso,pas-
sando1naop çãoanterior,elogovocênotaráumaperdadeperformanceemmuitas
aplicaçõespequenasoucompoucalógicarepetida.Nestecaso,ocustodecompila-
çãoeotimizaçãoémuitoalto.Emoutros,principalmenteemaplicaçõesmaislongas,
épossívelatéteralgumganho,maslogopercebe-sequeosnúmeroscalculadospor
padrãopelaJVMacabamsendovaloresbemrazoáveisparaamaioriadasaplicações.
Outrotesteinteressanteéusaraop ção -Xint,quedesabilitacompletamenteoJITe
fazaVMrodarapenasemmodointerpretado.Emaplicaçõesumpoucomaislongas,
logosepercebeumaimensaperdadeperformance.
Demodogeral,oquesepercebeéquenãoterumJITéumapéssimaideia,
quasetãoruimquantocompilartodososmétodosexistentes.Naprática,omelhor
acabasendoocomportamentopadrãodoJITdecompilarapenasospontosquentes.
Nossaaplicação,porém,deve,sim,estarpreparadaparausufruiromelhordoJIT.
Emgeral,issosignificaasboaspráticasdedesigncomváriospequenosmétodos
sendoreaproveitadosportodoocódigo.
Podesernecessáriomonitoraraexecuçãodeumaaplicação,comoquandoháa
necessidadedeencontrargargalosespecíficosdeperformanceevazamentosdeme-
mória. AOracledisponibilizadiversasferramentasparafacilitaro profiling,como
jmap,jstatejconsole.[34]PluginsparaIDEstambémexistememabundância,como
oTPTPdoEclipse.Dentreasferramentaspagas,destacam-seoTestKiteoJProfi-
ler.Todoselespermitemaumdesenvolvedorextrairinformaçõesdeumaaplicaç ão
rodandonaplataformaJavaparaentendermelhorcomoelaestáfuncionandoem
produção,atémesmoaquelasescritasemoutraslinguagens,masinterpretadasna
VM.
2.4 C arregamento de classes e classloader hell
ÉfrequentediversasaplicaçõesWebseremimplantadasemummesmoServletCon-
tainer,emumamesmamáquinavirtual,etambémquemuitasdelasutilizembibli-
otecaseframeworksemcomum. Imagineduasaplicaçõesqueutilizamamesma
versãodoHibernate:ondedevemoscolocarosJARs?
Muitossugeriramcolocá-losemalgumdiretóriocommon/libdoServletCon-
tainer;outrosdisseramparajogardiretamentenavariáveldeambiente CLASSPATH.
Esseseramconselhosfrequentes,emespecialquandoerararotermaisdeumaapli-
31

## Página 52

2.4. Carregamentodeclasseseclassloaderhell CasadoCódigo
caçãoJavaimplantadaemummesmoservidor.Paraentenderosgravesproblemas
quepodemsurgirnestasituação,éprecisoprimeirocompreendercomoéofuncio-
namentodocarregadordeclassesdaJVM.
ClassloaderéoobjetoresponsávelpelocarregamentodeclassesJavaparaame-
móriaapartirdeumarraydebytesquecontémseusbytecodes.[114]Érepresen-
tadopelaclasseabstrata java.lang.ClassLoader,eexistemdiversasimplementa-
çõesconcretas,comoajava.net.URLClassLoader,responsávelporcarregarclasses
buscandoemdeterminadasURLs.
Classloaderssãoumponto-chavedaplataformaJava.Comeles,podemoscarre-
gardiferentesclassescomexatamenteomesmonomeemantê-lasdeformadistinta,
emdiferentesespaçosdenomes(namespaces).Bastaqueusemosclassloadersdife-
rentes.UmaclasseéunicamenteidentificadadentrodaJVMporseunomecompleto
(incluindoonomedopacote,ochamado fullyqualifiedname)maisoclassloaderque
acarregou.
Édestaformaqueservidoresdeaplicaç ãoconseguemmanterseparadasversões
diferentesdeumamesmabiblioteca;podemosteroHibernate3.6emumaaplicaç ão
WebeoHibernate3.3emoutra.Paraisso,doisclassloadersdiferentessãonecessários
paracarregarasclassesdasduasdiferentesaplicações.Comoumclassloadercarrega
umaclasseumaúnicavez,senestecasofosseutilizadoomesmoclassloader,haveria
conflitodeclassescomomesmonome(porexemplo,a org.hibernate.Session
dasduasversõesdeHibernatediferentes),prevalecendoapenasaprimeiraquefosse
encontrada.
Porém,omecanismodecarregamentodeclassesnãoétãosimples.Porumame-
didadeseguran ça,osclassloaderssãocriadoseconsultadosdemaneirahierárquica
(Figura[ref-labelclassloaders2-4).
32

## Página 53

CasadoCódigo Capítulo2. JavaVirtualMachine
Figura2.4:Hierarquiadeclassloaders.
AfiguramostraostrêsclassloadersqueaJVMsempreutilizaráporpadrão.An-
tesdeumclassloaderiniciarumcarregamento,eleperguntaaoseupai(parentclas-
sloader)senãoconseguecarregar(oujácarregou)aclasseemquestão.Seo parent
classloaderconseguir,eleseráresponsávelporessecarregamento. Essefunciona-
mentohierárquicoéoquegaranteseguran çaàplataformaJava.Éassimqueclasses
importantes,comoasdo java.lang,serãosemprelidaspelo bootstrapclassloader,
casocontrário,poderíamos,porexemplo,adicionarumaclasse java.net.Socket
ànossaaplicaçãoe,quandoestafosseimplantadanoservidor,todasasoutrasclas-
sesdessaaplicaçãoquefizessemusodaSocketestariamusandoagoraumprovável
cavalodetroia.
Logo,évitalumcertoconhecimentodessesclassloadersfundamentais.
•Bootstrap classloader:Carregaclassesdort.jar,eéoúnicoque
• realmentenãotemparentalgum;éopaidetodososoutros,evitandoque
qualquerclassloader,tentemodificarasclassesdort.jar(pacote java.lang,
porexemplo).
•Extension classloaderCarregaclassesdeJARsdentrododiretóriona
• propriedadejava.ext.dirs, que, por padrão, tem o valor
$JAVA_HOME/lib/ext. Na JVM da Sun, é representado pela classe in-
terna sun.misc.Launcher$ExtClassLoader. Tem como pai oBootstrap
classloader.
•Application classloader ou System classloader:Carregatudodefinidono
33

## Página 54

2.4. Carregamentodeclasseseclassloaderhell CasadoCódigo
•CLASSPATH, tanto da variável de ambiente, quanto da linha de comando
(passado como argumento por-cp). Representado pela classe interna
sun.misc.Launcher$AppClassLoader,temcomopaio Extensionclassloader.
OBootstrapclassloaderéoquecarregatodasasclassesdabibliotecapadrão
(rt.jarinclusive). Depoisdele,aaplicaçãopodeusaroutrosclassloaders,jáquea
maioriadasclassesestáforadesseJAR.
Asaplicaçõespodemcriarnovosclassloaderseincrementaressahierarquia(Fi-
gura2.5).Oscontainerscostumamcriarmuitosoutrosclassloadersalémdospadrões
damáquinavirtual.Emgeral,criamum Container classloader,responsávelpelos
JARsdocontaineredeumacertapasta,comouma common/lib.Alémdeste,ocon-
tainerprecisadeumclassloaderespecíficoparacadaaplicaç ão(contexto)implan-
tada.Esse WebApplicationclassloaderéresponsávelpelocarregamentodasclasses
doWEB-INF/classesedo WEB-INF/libemaplicaçõesWeb,porexemplo.
Conhecendoessahierarquia,podemosperceberoproblemaquandodesenvol-
vedoresdesavisadosjogamJARsemdiretórioscompartilhadosportodasasaplica-
çõesdeumdeterminadoservidor,comoocasododiretório common/libdoApache
Tomcatemversõesmuitoantigas,ouutilizandoavariáveldeambiente CLASSPATH.
Considerandoquetemosduasaplicações,APP-novaeAPP-antiga,queusam
amesmaversãodoHibernate3.3,elasfuncionarãonormalmentemesmocomos
jarsdoHibernatereferenciadosnavariável CLASSPATH.NomomentoqueaAPP-
novaprecisarutilizaraversão3.6,comoproceder? Jogaraversãomaisnovano
WEB-INF/libdaAPP-novanãoresolveoproblema,poisahierarquiadeclassloa-
dersfariacomquea org.hibernate.SessionetodasasoutrasclassesdoHibernate
sejamcarregadasdosjarsdefinidosna CLASSPATH,possivelmentegerandoerrosines-
peradosemtempodeexecução(Figura2.5).
34

## Página 55

CasadoCódigo Capítulo2. JavaVirtualMachine
Figura2.5:Hierarquiausualdeclassloadersnocontainer.
Esseproblemaémuitomaisgravedoqueaparenta;otipodeerroquepodesur-
girédedifícilinterpretação. Omenordosproblemasseriaterocomportamento
daversãoantigadoHibernate.MaisgraveéquandohámétodosnovosnoJARmais
recente;ainterfaceSessiondoHibernateantigoseriacarregada,equandosuaaplica-
çãoAPP-novainvocarummétodoquesóexistenaversãonova, NoSuchMethodError
serálançado!Issocausaumaenormedordecabe ça,poisodesenvolvedorficacon-
fusoaoverqueocódigocompilouperfeitamente,masduranteaexecuç ãoaJVM
indicaqueaquelemétodonãoexiste.
NoSuchMethodErroréum forte indicador de que o código foi compilado es-
perando uma versão diferente de uma biblioteca que a encontrada em tempo de
execução,provavelmenteporcausadeosjarsestaremespalhadosecompartilhados.
Ocomportamentodaaplicaçãopodesermaiserrático;imaginequeaaplicaç ão
APP-novautilizadiretamenteumaclassedoHibernatequesóexistenaversãomais
nova,comoa TypeResolver.Oclassloaderqueverificaavariável CLASSPATHnãoa
encontrará,eentãoelaserácorretamentecarregadado WEB-INF/libpeloclassloader
específicodocontexto.Porém,a TypeResolverdoHibernate3.6referenciaoutras
classesbásicasdoHibernate,eestasserãocarregadasdaversãoantiga,oHibernate
encontradona CLASSPATH,fazendocomqueoHibernatesejacarregadopartedeuma
versão,partedeoutra,resultandoemefeitoscolateraisinesperadosedesastrosos.
35

## Página 56

2.4. Carregamentodeclasseseclassloaderhell CasadoCódigo
EssaconfusãoésimilaraoDLLHell,frequentementechamadode Classloader hell
naplataformaJava.
Emalgumasconfiguraçõesdeclassloadersdiferentes,quecarregamclassesde
diretóriosemcomum,podeaparecerum ClassCastExceptioncuriosoededifícil
discernimento.SeumareferênciaaumobjetodotipoProdutoforpassadacomoar-
gumentoparaummétodoquerecebeumobjetotambémdestetipo,masestaclasse
tiversidocarregadaporumclassloaderdiferente,aexce çãoserálan çada. Ode-
senvolvedorficaráconfusoaoveruma ClassCastExceptionemumainvocaçãode
métodoemquenemmesmoháumcasting.Issoaconteceporque,comovimos,em
tempodeexecuçãoaidentidadedeumaclassenãoéapenasseu fullyqualifiedname,
mastambémoclassloaderqueacarregou. Assim,umaclassecommesmonome,
mascarregadaporclassloadersdiferentes,éoutra.Istoéchamadode runtime iden-
tityemuitoimportanteparapermitirquecontainerstenhammaisdeumaversãoda
mesmaclassenamemória(comooexemplodas Sessionsdediferentesversõesdo
Hibernate).[48]
Muitoscontainers,incentivadospelaprópriaespecificaçãodeServlets,aplicam
ummodelodeclassloadersinvertidosparaminimizarosproblemas. Aoinvésde
deixaroWebAppclassloaderfilhodoContainerclassloader,eleéfeitofilhodireto
doBootstrapclassloadermascomumareferênciasimplesparaoContainerclasslo-
ader.Aarquiteturatradicionaldificultaqueumaaplicaç ãosobrescrevaalgumcom-
ponentedoContainerclassloader,masessemodeloinvertido(padrãonoTomcat,
porexemplo)permiteessecenário. Aordemderesoluçãodasclassespassaaser:
primeirooBootstrap,depoisasclassesdaaplicaç ãoedepoisascompartilhadasdo
Container.
Criando seu ClassLoader
Podemosinstanciara URLClassLoaderparacarregarclassesapartirdeumcon-
juntodadodeURLs.Considerequeaclasse DAOestádentrododiretóriobin:
URL[] bin = {new URL("file:bin/")};
ClassLoader loader = new URLClassLoader(bin, null);
Class<?> clazz = loader.loadClass("br.com.arquiteturajava.DAO");
Repare que passamos null como segundo argumento do construtor de
URLClassLoader. Istoindicaqueseuparentclassloaderseráobootstrapdireta-
mente.
36

## Página 57

CasadoCódigo Capítulo2. JavaVirtualMachine
Setambémcarregarmosaclasseatravésdo Class.forNameecompararmosa
referênciadasduasclasses:
URL[] bin = {new URL("file:bin/")};
ClassLoader loader = new URLClassLoader(bin, null);
Class<?> clazz = loader.loadClass("br.com.arquiteturajava.DAO");
Class<?> outraClazz = Class.forName("br.com.arquiteturajava.DAO");
System.out.println(clazz.getClassLoader());
System.out.println(outraClazz.getClassLoader());
System.out.println(clazz == outraClazz);
O Class.forName()carregaaclasseusandooclassloaderquefoiresponsável
pelaclassedocódigoexecutado;nocaso,oApplicationclassloaderseestivermosno
métodomain.EoresultadocomaJVMdaOracle/Suné:
java.net.URLClassLoader@19821f
sun.misc.Launcher$AppClassLoader@11b86e7
false
Executandoestemesmocódigoparaumaclassedabibliotecapadrão,digamos,
java.net.Socketou java.lang.String,teremosumresultadodiferente.Elasse-
rãocarregadasemambososcasospelo bootstrapclassloader(representadopelo
null),poisnãohácomoevitarqueesseclassloadersejaconsultadoemrazãoda
questãodeseguran çajádiscutida.
Aoremovero nulldoconstrutor,o URLClassLoaderterácomoparentoclass-
loaderquecarregouocódigosendoexecutado(o Applicationclassloader),fazendo
comqueocarregamentodaclassesejadelegadoparaeste,antesdesertentadopelo
nossoURLClassLoader.Casoodiretóriobinestejanoclasspath,o Applicationclass-
loaderconseguecarregaraclasseDAOeonossorecém-criadoclassloadernãoserá
oresponsávelpelocarregamento:
URL[] bin = {new URL("file:bin/")};
ClassLoader loader = new URLClassLoader(bin);
Destavez,oresultadoé:
sun.misc.Launcher$AppClassLoader@11b86e7
sun.misc.Launcher$AppClassLoader@11b86e7
true
37

## Página 58

2.4. Carregamentodeclasseseclassloaderhell CasadoCódigo
Oparentclassloaderserásempreconsultadoantesdeoclassloaderdehierar-
quia“maisbaixa”tentarcarregarumadeterminadaclasse.Lembre-sedequeesteéo
motivopeloqualjogarosJARsnavariáveldeambiente CLASSPATHpodeacabares-
condendoversõesdiferentesdamesmaclassequeestejamaoalcancedeclassloaders
mais“baixos”nahierarquia.
Endorsed JARs
Essefuncionamentohierárquicocausaproblemastambémcomabibliotecapa-
drão;acadaversãonovadoJava,algumasAPIs,antesexternaseopcionais,sãoin-
corporadas. Estefoiocaso,porexemplo,dasAPISdeparseamentodeXMLdo
Apache(XerceseXalan). Casoelasfossemincluídasdentrodabibliotecapadrão,
qualqueroutroprojetoquenecessitassedelasemumaversãodiferente(tantomais
atualquantomaisantiga)teriasempreaversãodort.jar
Para contornar o problema, a Sun colocou as classes que seriam do pacote
org.apacheparadentrode com.sun.org.apache.[136]Semdúvidaumamaneirade-
selegante,masqueevitouoproblemadeversionamento.
Esteproblematornou-seaindamaisfrequente.NoJava6,aAPIdemapeamento
deXML,aJAXB2.0,entrouparaabibliotecapadrão. Quemnecessitausaraver-
são1.0,ouaindaumafuturaversão3.0,teráproblemas;aversão2.0sempreterá
prioridadenocarregamento.OJBoss4.2necessitadaAPIdoJAXB1.0parasuaim-
plementaçãodeWebServices,esofreentãocomessainclusãodoJava6.[180]Aliás,
oJBosspossuiumalongaeinteressantehistóriademanipulaç ãodosclassloaders,
sendooprimeiroEJBcontaineraoferecer hotdeployment,eparaistotevedecon-
tornarumasériederestriçõeseatémesmobugsdaJVM.[24]
QuandoointerpretadordeJavascriptRhinoentroujuntocomaScriptingAPI
noJava6naJVMdaSun,passamosateromesmoproblemaquandoénecessário
utilizarsuasversõesdiferentes.[112]
Nessesdoiscasos,paracontornaroproblema,utilizamosorecursodeendor-
sedJARs.Atravésdalinhadecomando(-Djava.endorsed.dirs=),vocêespecifica
diretóriosquedevemterprioridadenaprocuradeclassesantesqueodiretórioext
doJavaSEsejaconsultado.Éumaformadeoadministradordosistemadizerque
confiaem(endossa)determinadosJARs. Algunsservidoresdeaplicaç ãopossuem
umdiretórioespecialondevocêpodejogarosJARsaseremendossados.Valeno-
tarocuidadoquedevesertomadoaoconfiaremumJAR,colocando-onotopoda
hierarquiadosclassloaders.
38

## Página 59

CasadoCódigo Capítulo2. JavaVirtualMachine
OutOfMemoryError no redeploy de aplicações
VimosquealgumasJVMsarmazenamasclassescarregadasnamemórianoes-
paçochamadoPermGen.Écomumapareceremproblemascom OutOfMemoryError,
acusandoqueesteespaçoseesgotou,dadoumnúmeromuitograndedeclassescar-
regadas.Emparticular,issoocorrefacilmentedepoisdealgunshotdeploysemum
container.
Todaclassecarregadatemumareferênciaparaoseuclassloader,assimcomo
todoclassloaderreferenciatodasasclassescarregadasporele.Issoparaquepossa
devolversempreamesmaclassenocasodeoutrainvocaç ãosubsequenteparao
mesmofullqualifiedname,agindocomoumafactoryquecacheiasuasinstancia-
ções.Esserelacionamentobidirecionalentre Classe ClassLoaderfazcomqueos
objetosClasssósejamcoletadospelogarbagecollectorjuntocomoclassloaderin-
teiroetodasasoutrasclassesassociadas.Logo,aúnicamaneiradeumobjeto Class
sercoletadoésetodasasreferênciasparatodasasclassesdoseuclassloaderforem
liberadastambém.
Aorealizarohotdeploydeumaaplicaç ão,oprópriocontainerliberaasrefe-
rênciasdasclassesantigas,possibilitandoacoletadoclassloaderdocontexto. Isso
deveriasersuficienteparaqueocontextofosseinteiramenteliberadodamemória,
mas,naprática,outroclassloaderacimadaqueledaWebApplicationsegurareferên-
ciasparaclassesdaaplicação.Eháváriasbibliotecasqueassimsecomportam,como
opróprioDriverManagerdoJDBC(JavaDatabaseConnectivity ).Esteguardarefe-
rênciasparaasclassesdosdriversregistrados,maselassãocarregadaspelobootstrap,
eodriver,emgeral,estádentrodaaplicaç ão,no WEB-INF/lib.Ocarregamentode
umúnicodriverJDBCécapazdesegurarnamemóriaocontextointeirodeuma
aplicaçãoquenãoémaisnecessária.
Existemváriosoutrosexemplosdebibliotecaseclassesquecausammemoryle-
aksparecidos[5][194].NocasodoJDBC,asoluç ãoéfazerum contextlistener que
invocaométodo deregisterDriverno DriverManager,mashásituaçõesnãotão
simplesdesecontornar,queenvolvemversõesespecíficasdebibliotecascomseus
própriostiposdeleaksdereferênciasaclassesquejánãosãomaisutilizadas. Na
prática,équaseimpossívelumaaplicaçãoJavaconseguirevitaressesleaksdeclass-
loaders,porissoemalgummomentosurgemos OutOfMemoryErrorfrequentesnos
hotdeploys,sendomaisummotivoparaevitá-losemproduç ão.
39

## Página 61

Capítulo3
TópicosdeOrientaçãoaObjetos
Umbomdesigndesoftwarevisaaumaarquiteturaflexívelquepermitafuturasal-
terações,faciliteaproduçãodecódigoorganizadoelegível,maximizandoseurea-
proveitamento. Todooparadigmadaorientaçãoaobjetos,seusprincípioseboas
práticasprocuramtrazeressesbenefíciosparaodesign.
Aopensarnosistemacomoumtodo,outrasquestõesdemaisaltonívelsurgem,
emespecialaquelasquetratamdaformacomoosobjetosserelacionamesuaorga-
nizaçãodentroeentresistemas.Aorelacionardoisobjetosdistintos,deve-selevar
emcontaasboaspráticasqueserãodiscutidasnessecapítulo,comoadiminuiç ãodo
acoplamentoentreobjetos.
3.1 P rograme voltado à interface, não à implemen-
tação
Aotrabalharcomcole ções,escolheraimplementaçãocertaparacadacasoéuma
tarefadifícil.Cadaumadelas,como ArrayList, LinkedListouHashSet,émelhor

## Página 62

3.1. Programevoltadoàinterface,nãoàimplementação CasadoCódigo
pararesolverdeterminascategoriasdeproblemas.Podesermuitoarriscadoescrever
todoocódigodaaplicaç ãodependentedeumadecisãoantecipada. Apesardisso,
grandepartedosdesenvolvedoresoptaporsempreutilizar ArrayListdesdeoinício
semcritérioalgum.
Considereum DAOdefuncionáriosquepodelistaronomedetodosquetraba-
lhamemdeterminadoturno,devolvendoum ArrayListcomosnomes:
public class FuncionarioDao {
public ArrayList<String> buscaPorTurno(Turno turno) { ... }
}
Eumcódigoqueprecisasabersedeterminadofuncionárioestevepresente,efe-
tuandoumabuscasimplesnalistadevolvida:
FuncionarioDao dao = new FuncionarioDao();
ArrayList<String> nomes = dao.buscaPorTurno(Turno.NOITE);
boolean presente = nomes.contains("Anton Tcheckov");
Masabuscacom containsemum ArrayListé,emtermoscomputacionais,
bastantecustosa.Poderíamosutilizaroutrasalternativasdecole ção,trocandoore-
tornode ArrayListparaHashSet,porexemplo,poissuaoperação containsémuito
maiseficientecomputacionalmente,usandointernamenteumatabeladeespalha-
mento(hashtable).Parapoucosfuncionários,adiferen çaéimperceptível,porém,à
medidaquealistaaumenta,adiferen çadedesempenhoentreum ArrayListeum
HashSetsetornamaisclara,eatémesmoumgargalodeperformance.
Oproblemaemrealizarumamudan çacomoesta,deimplementação,équetodo
códigoqueusavaoretornodométodocomo ArrayListquebra,mesmoquesóusás-
semosmétodosquetambémexistemdefinidosem HashSet.Seriaprecisoalterarto-
dososlugaresquedependemdealgumaformadessemétodo.Alémdetrabalhoso,
tarefasdotipo search/replacesãoumfortesinaldecódigoruim.
Háesseacoplamentosintáticocomaassinaturadométodo,queconseguimos
resolverolhandooserrosdocompilador.Massemprehátambéminformaçõesse-
mânticasimplícitasnautilizaçãodessemétodo,equenãosãoexpostosatravésda
assinatura.Umexemplodeacoplamentosemânticoestáemdependerdainforma-
çãodequeuma Listpermitedadosduplicados,enquantoum Setgaranteunici-
dadedoselementos. Comoproblemasnoacoplamentosintáticosãoencontrados
emtempodecompilação,ossemânticossomenteosãoemexecuç ão,daíummotivo
daimportânciadetestesquegarantamocomportamentoesperado.
42

## Página 63

CasadoCódigo Capítulo3. TópicosdeOrientaçãoaObjetos
Ograndeerrodométodo buscaPorTurnodaclasse FuncionarioDaofoiatrelar
todososusuáriosdométodoaumaimplementaçãoespecíficade Collection.Desta
forma,alteraraimplementaçãotorna-sesempremuitomaiscustoso,caracterizando
o alto acoplamentoquetantoseprocuraevitar.
Paraminimizaresseproblema,épossívelusarumtipoderetornodemétodo
maisgenérico,quecontemplediversasimplementaçõespossíveis,fazendocomque
osusuáriosdométodonãodependamemnadadeumaimplementaç ãoespecífica.
Ainterface Collectionéumaboacandidata:
public class FuncionarioDao {
public Collection<String> buscaPorTurno(Turno turno) { ... }
}
Comométododestaforma,podemostrocaraimplementaç ãoretornadasem
receiodequebrarnenhumcódigoqueestejainvocando buscaPorTurno,jáquenin-
guémdependedeumaimplementaçãoespecífica.Usar interfacesJavaéumgrande
benefícionestescasos,poisajudaagarantirquenenhumcódigodependadeuma
implementaçãoespecífica,poisinterfacesnãocarregamnenhumdetalhedeimple-
mentação.
Reparequeépossíveloptaraindaporoutrasinterfaces,como List(maisespe-
cífica)e Iterable(menosespecífica).Aescolhadainterfaceidealvaidependerdo
quevocêquerpermitirqueocódigoinvocadorpossautilizarerealizarnareferência
retornada. Quantomenosespecífica,menoroacoplamentoemaispossibilidades
dediferentesimplementações. Emcontrapartida,ocódigoclientetemumagama
menordemétodosquepodemserinvocados.
Algosimilartambémocorreparareceberargumentos. Considereummétodo
quegravadiversosfuncionáriosemlotenonosso DAO:
public class FuncionarioDao {
public void gravaEmLote(ArrayList<Funcionario> funcionarios) { ... }
}
Receberprecisamente ArrayListcomoargumentotempoucautilidade;rara-
mentenecessitamosqueumacole çãosejatãoespecíficaassim. Receberaquium
Listprovavelmentebasteparaonossométodo,epermitequeocódigoinvocador
passeoutrascole çõescomoargumento.Podemosiralémereceber Collectionou,
ainda,Iterable,casonossanecessidadesejaapenaspercorreroselementos.Aesco-
lhade Iterable,nestecaso,permitiriaomaiordesacoplamentopossível,maslimi-
tariaousodentrodométodo;nãoseriapossível,porexemplo,acessaraquantidade
43

## Página 64

3.1. Programevoltadoàinterface,nãoàimplementação CasadoCódigo
deelementosqueessacole çãopossui,nemoselementosdemaneiraaleatóriaatravés
deumíndice.Devemosprocurarumbalan çoentreodesacoplamentoeanecessi-
dadedonossocódigo.Estaéaideiado PrincípiodeSegregaçãodeInterfaces : clientes
não devem ser for çados a depender de interfaces que não usam.[122]
Odesenvolvedordeveteremmentequeacoplarumaclasse,quepossuimenos
chancesdealteraçõesemsuaestrutura,comoutramenos estávelpodeserperigoso.
[125]Considereainterface List,quepossuimuitasrazõesparanãomudar,afinal,
elaéimplementadaporváriasoutrasclasses;sesofressealterações,todasasclasses
queaimplementamteriamqueseralteradastambém.Consideramos,então,queela
éaltamenteestável,oquesignificaqueelararamenteobrigaráumamudan çanas
classesqueautilizam(Figura3.1).
Figura3.1:Interfacessãomaisestáveisporgarantiremmenoresmudan çascomque-
bradecompatibilidade.
Umaimplementaçãodelista, MeuProprioArrayList,feitapelodesenvolvedoré
provavelmentemais instávelqueainterface List,jáqueasfor çasqueaimpedem
demudarsãofracas(nãoháoutrasclassesutilizandoessaimplementaç ão).Ouseja,
44

## Página 65

CasadoCódigo Capítulo3. TópicosdeOrientaçãoaObjetos
umaclasseacopladaaessaimplementaçãodelistaeventualmentepodeserobrigada
amudarporcausadealgumaalteraç ãoem MeuProprioArrayList.
Osframeworksebibliotecasconsagradossempretiramproveitodousodeinter-
faces,desacoplando-seomáximopossíveldeimplementações.Tantoa Sessiondo
Hibernatequantoa EntityManagerdaJPAdevolvem Listnosmétodosqueenvol-
vemlistasderesultados.Aoanalisarafundoasimplementaçõesatuaisde Sessione
EntityManagerdoHibernate,elasnãoretornamnem ArrayList,nem LinkedList,
nemnenhumacole çãodo java.util,e,sim,implementaçõesdelistaspersistentes
depacotesdopróprioHibernate.
Istoépossível,novamente,pelodesacoplamentoprovidopelousodasinterfaces.
Alémdisso,oretornodasconsultascomJPAeHibernatesão List,paradeixarclaro
aousuárioqueaordeméimportante.Manteraordemdeinser çãoepermitiracesso
aleatóriosãocaracterísticasdocontratode Listesãoimportantesparaoresultado
deconsultas,poispodemdefinirumaordenação(order by),umaótimajustificativa
paraoptarporumainterfacemaisespecífica,enãousar IterableouCollection.
Nas principais APIs do Java, é fundamental programar voltado à inter-
face. Aousar java.io,evitamosaomáximonosreferenciara FileInputStream,
SocketInputStream,entreoutras. Ocódigoaseguiraceitaapenasarquivoscomo
streams:
public class ImportadoraDeDados {
public void carrega(FileInputStream stream) { ... }
}
Desta forma, não é possível passar qualquer tipo deInputStream para a
ImportadoraDeDados.Adotarestalimitaçãodependedocódigodentrodométodo
carrega.Aoutilizaralgummétodoespecíficode FileInputStreamquenãoesteja
definidoem InputStream,nãoháoquefazerparadesacoplarocódigo.Casocon-
trário,essemétodopoderia,edeveria,receberumareferênciaa InputStream,fi-
candomaisflexívelepodendoreceberosmaisdiferentestiposdestreams,como
argumento,queprovavelmentenãoforampreviamenteimaginados. Utilize sempre
o tipo menos específico possível.
Repareque,muitasvezes,classesabstratastrabalhamcomointerfaces,nosen-
tidoconceitualdeorientaçãoaobjetos.[206]Classesabstrataspossuemavantagem
desepoderadicionar-lhesumnovométodonãoabstrato,semquebrarocódigojá
existente.Jácomousode interfaces(aqui,pensandonapalavra-chavedoJava),aadi-
çãodequalquermétodoacarretaráaquebradasclassesqueaimplementam.Como
45

## Página 66

3.1. Programevoltadoàinterface,nãoàimplementação CasadoCódigo
interfacesnuncadefinemnenhumaimplementação,avantageméqueocódigoestá
sempredesacopladodequalqueroutroqueasutilize.Issomudacomospolêmicos
extensionmethods doJava8,permitindoescreverumaimplementaç ãopadrãonas
interfaces,possibilitandosuasevoluções,aomesmotempoqueminimizaaquebra
decompatibilidade.
Os métodos load(InputStream), da classe Properties, e
fromXML(InputStream), do XStream, são ótimos exemplos de código que não
dependemdeimplementação. Podemreceberarquivosdosmaisdiferentesstre-
ams: rede(SocketInputStream),uploadHTTP( ServletInputStream),arquivos
(FileInputStream),dedentrodeJARs(JarInputStream )earraysdebytegenéricos
(ByteArrayInputStream).
AJavaDatabaseConnectivity (JDBC)éoutraAPIfirmementefundadanouso
deinterfaces. Opacote java.sqlpossuipouquíssimasclassesconcretas. Sempre
queencontramosumcódigotrabalhandocomconexõesdebancodedados,ve-
mosreferênciasàinterface Connection,enuncadiretamentea MySQLConnection,
OracleConnection, PostGreSQLConnection,ouqualqueroutraimplementaçãode
umdriverespecífico,apesardeestapossibilidadeexistir.
Referindo-sesemprea Connection,deixamosaescolhadaimplementaçãocen-
tralizadaemumoupoucoslocais.Destaforma,ficamuitofáciltrocaraimplementa-
çãosemmodificartodoorestantedocódigo.Issoocorregraç asaodesacoplamento
providopelousodeinterfaces.
NocasodoJDBC,essaescolhaporumaimplementaç ãoestácentralizadana
classeconcreta DriverManager,queaquiagecomoumafactory.Eladecideporins-
tanciarumaimplementaçãoespecíficade Connectiondeacordocomosparâmetros
passadoscomoargumentosaométodo getConnectioneconformeospossíveisdri-
verspreviamentecarregados.
Connection connection =
DriverManager.getConnection("jdbc:mysql://192.168.0.33/banco");
Podeserfácilenxergarasvantagensdousodasinterfaces,masébemmaisdifícil
começarautilizá-lasextensivamentenoseuprópriodomínio.Ousoexageradode
reflectionparainvocarmétodosdependendodealgumascondiçõespodesermuitas
vezessubstituídoporinterfaces.Assim,adecisãodequalmétodoinvocarédeixada
paraainvocaçãovirtualdemétodoqueopolimorfismopromove,diminuindobas-
tanteacomplexidadeeaumentandoamanutenibilidade,alémdealgumganhode
performance.[17]
46

## Página 67

CasadoCódigo Capítulo3. TópicosdeOrientaçãoaObjetos
Istoéaindamaisgritantecomousodainstruç ão switch,oumesmoemum
excessivonúmerode ifsencadeados;essaabordagempodeacoplartotalmenteseu
modelo,tornandonecessáriasmudançasfrequentesneletodavezqueumanovaen-
tidadeforadicionadaaodomínio.[66]
Programe voltado à interface, não à implementaçãoéoutrodospríncipiosde
orientaçãoaobjetosdolivro DesignPatterns ([206][79]),abordadopormeiode
outrosexemplosnoseminal DependencyInversionPrinciple,deBobMartin.[121]
3.2 C omponha comportamentos
Umcódigocompoucaspossibilidadesdefluxoslógicos(branches deexecução),ou
seja,poucoscaminhosdeexecução,émaisfácildeentenderemanter.Oexemploa
seguirmostraumprocessodepagamento:
public void processa(Pagamento aPagar) {
if (aPagar.isServico() && aPagar.getValor() > 300) {
impostos.retem(aPagar.getValor() * TAXA_A_RETER);
} else if(aPagar.isProduto()) {
estoque.diminui(aPagar.getItem());
}
conta.executa(aPagar);
if (aPagar.desejaReceberConfirmacao()) {
emails.enviaConfirmacao(aPagar);
}
}
Apesardesimples,existemseispossibilidadesdiferentesdeexecuç ãodométodo,
alémdeelemisturardiversoscomportamentosquenãopossuemrelaç ão,istoé,res-
ponsabilidadesdiferentesparaumaúnicaclasse:impostos,estoques,transferências
ee-mails.
Talcomportamentopodesercompostopordiversaspartesmenorese, para
tanto,refatoraçõespequenaspodemserexecutadas.Amaissimplesseriaaextraç ão
dequatrométodos,umasoluçãoquesimplificaocódigoatual,masnãoaumentasua
coesão.
Épossívelaumentaracoesãodaclasseextraindotaismétodosemquatroclasses
distintas,como RetemImposto, ProcessaEstoque, Transferenciae Confirmacao.
Porfim,ascondiçõespodemsertratadasatravésdeumacadeiaderesponsabilidade
47

## Página 68

3.2. Componhacomportamentos CasadoCódigo
(chainofresponsibility)ounotificações(observers),usandoumainterfacecomuma
todosessesprocessosquedevemserexecutados.Estedesign,quefavoreceacom-
posiçãoemvezdeumgrandemétodo,isolapreocupaçõesdistintasparapartesse-
paradasdocódigo.
Umainterface Processosimplesécapazdemodelarosdiferentestiposdepro-
cessosquepodemseraplicadosaum Pagamento,comoa RetemImposto:
public interface Processo {
void lidaCom(Pagamento pagamento);
}
public class RetemImposto implements Processo {
private static final double TAXA_A_RETER = 0.10;
public void lidaCom(Pagamento aPagar) {
if (aPagar.isServico() && aPagar.getValor() > 300) {
impostos.retem(aPagar.getValor() * TAXA_A_RETER);
}
}
}
Outras implementações possíveis de passos do processo seriam as classes
ProcessaEstoque, Transferenciae Confirmacao. Acadeiaderesponsabilidade
podeserrepresentadaporumaoutraclasse Processos,queaplicadiferentespro-
cessosaummesmopagamentodemaneiraencadeada:
public class Processos {
private final List<Processo> processos;
public Processo(List<Processo> processos) {
this.processos = processos;
}
public void processa(Pagamento aPagar) {
for (Processo passo : processos) {
passo.lidaCom(aPagar);
}
}
}
48

## Página 69

CasadoCódigo Capítulo3. TópicosdeOrientaçãoaObjetos
Pode-seevoluiraindamaisoexemploacima;quandoaexecuç ãodecadapasso
deumcomportamentoécondicionaledeacordocomasmaisvariadasregras,é
comumadicionarummétodoextradeverificaç ão,queindicaseoprocessamento
deveounãoserfeitonaquelecaso:
public interface Processo {
void lidaCom(Pagamento pagamento);
boolean deveProcessar(Pagamento pagamento);
}
public class RetemImposto implements Processo {
private static final double TAXA_A_RETER = 0.10;
public void lidaCom(Pagamento aPagar) {
impostos.retem(aPagar.getValor() * TAXA_A_RETER);
}
public boolean deveProcessar(Pagamento aPagar) {
return aPagar.isServico() && aPagar.getValor() > 300;
}
}
Padrõesdedesignparecidoscomoanteriorsãoencontradosnosconversoresde
diversosframeworks,renderizaçãodetelas,execuçãodeprocessoscomplexos,filtros
daservletAPIetc.(Figura3.2).
49

## Página 70

3.3. Eviteherança,favoreçacomposição CasadoCódigo
Figura3.2:Compondocomportamentoatravésdediferentescomponentesdeuma
aplicação.Àmedidaquefoinecessário,ocódigoerarefatorado.
Apósaquebradeumcomportamentoemdiversaspartes,énecessáriojuntar
essescomportamentosnovamente.Composição(composition)éestauniãoatravés
dautilizaçãodealgumapráticadedesign,comonocasovistoanteriormente,noqual
opolimorfismopermitetrabalhardemaneirauniformecompartesqueexecutam
tarefasdistintas.
Ummétodoqueapresenteumcorpocomumnúmerorazoávelde branches
(como ifse switches),ouquenãopermitaacompreensãoimediatadeseucom-
portamento,podeserrefatoradoparafacilitarsuamanuten ção.
3.3 E vite herança, favoreça composição
Ousoounãodeheran çaéumantigodebatequeapareceinúmerasvezesnaliteratura,
antesmesmodaexistênciadoJava,([79],[205])eemrecentesartigoscomlinguagens
maismodernas. [206],[17],[91]Algunscríticoschegamaafirmarqueelanunca
deveriaserutilizada.[192]
Omaiorproblemacomaheran çaéqueacoplamosaimplementaçãodaclasse
mãemuitoprecocemente,criandoanecessidadedeaclassefilhaconhecermuito
50

## Página 71

CasadoCódigo Capítulo3. TópicosdeOrientaçãoaObjetos
bemocódigointernodaclassemãe,oqueévistocomoumaquebradeencapsula-
mento.
Podemos enxergar este problema em um exemplo encontrado no pacote
java.util,com PropertieseHashtable.Aclasse Propertiesherdade Hashtable
e,portanto,instânciasde Propertiespossuemdisponíveismétodosde Hashtable.
Mas,muitasvezes,essesmétodosnãofazemsentido,comonocasoda Properties
que lida apenas comStrings. A quebra aparece quando temos uma instân-
cia deProperties e invocamos o métodoput(Object, Object), em vez de
setProperty(String, String),podendopassarum Objectqualquercomoargu-
mento. Nessecaso,aoinvocarposteriormenteométodo getProperty(String),
recebemosuminesperado null. Nãohácomoevitarquealguéminvoqueomé-
todoquetrabalhacom Object,anãoserdocumentandoarespeito,comoocorre
nojavadocdessaclasse.Terdegarantircondiçõesapenasatravésdo javadocéum
contratomuitofraco,emespecialdizendoquetalmétodonãodeveserinvocado
comdeterminadostiposdeobjetos,algoque,emJava,poderiaserfeitoatravésda
tipagemestática.
public class TesteProperties {
public static void main(String[] args) {
Properties properties = new Properties();
// não deveria ser possível invocar:
properties.put("data_de_inicio" , Calendar.getInstance());
Processador p = new Processador();
p.processa(properties);
}
}
public class Processador {
public void processa(Properties properties) {
String valor = properties.getProperty("data_de_inicio");
// o Calendar estará na String?
}
}
Arelaçãoé-umdaherançanemsempreétãofácildeseraplicadaaobjetos.Ape-
sardeumquadradoserumretângulo,umcarroserumveículoeumdicionáriode
propriedadesserumatabeladeespalhamento,nãonecessariamenteumobjetodo
tipodicionáriodeveserencaradocomoumobjetodetabeladeespalhamentocaso
51

## Página 72

3.3. Eviteherança,favoreçacomposição CasadoCódigo
istonãorespeiteo princípiodesubstitui çãodeLiskov. [123][91]Poresteprincípio,
deveriaserpossívelreceberum Propertiescomoum Mapsemnenhumproblema,
masvimosqueissonãoocorrenocódigodescritoantes.Aindanopacote java.util,
temosaclasse Stackqueestende Vector,expondométodosdestaquenãosãoca-
racterísticasdeumapilha.
Masamotivaçãoinicialdoscriadoresde Propertieséextremamenteválida:o
reaproveitamentodecódigojáescritonaclasse Hashtable.Heran çaécomumente
citadaemcenáriosdereúsodecódigo,masnãoéaúnicasoluç ão. Usarcomposi-
çãopermitereaproveitamentodecódigosemoefeitoindesejadodaquebradeen-
capsulamento. Paraqueaclasse Propertiesreaproveitasseosrecursosjáexisten-
tesem Hashtablecomcomposiçãobastariaumatributo Hashtableprivado,eo
métodosetPropertydelegariaainvocaçãoparao hashtable.put.Dessamaneira,
expomosapenasosmétodosquedesejamos,sempossibilitarquefosseinvocadoo
hashtable.putdiretamente,nemque Propertiespudesseserpassadacomoargu-
mentoparaalguémqueesperauma Hashtable. Melhorainda,comosurgimento
daAPIdeCollections,comonoJava1.2,aimplementaç ãopoderiaserfacilmente
trocadaporalgum Mapsemcausarproblemasaosusuáriosdaclasse.
Ousoabusivodeheran çaocorreemdiversosframeworkseAPIs.OStruts1é
umexemplodesteusoedeseusdiversosproblemasrelacionados;somosinstruídos
aestender Actione,aomesmotempo,atomarmuitocuidadocomseuciclodevida,
principalmenteaosobrescreveralgunsmétodos-chavedessaclasse.Emlinguagens
comsuportea mixin,comoRuby,oacoplamentocomasclassespodegerarcompli-
caçõesaindamaiores,quesóserãopercebidasemtempodeexecuç ão.[176]
Oproblemadaheran çaaparece,mesmoquemaissutilmente,nousodeclas-
sesabstratasparaaplicarpatterns,comoo templatemethod. Podemosrepararem
algunstropeçosdaimplementaçãobasede Servlet, GenericServlet,começando
pelométodoinit(ServletConfig):
public abstract class GenericServlet
implements Servlet, ServletConfig, Serializable {
// ...
public void init(ServletConfig config) throws ServletException {
this.config = config;
this.init();
}
}
52

## Página 73

CasadoCódigo Capítulo3. TópicosdeOrientaçãoaObjetos
Ao criar nossa própria servlet na Web, somos obrigados a herdar de
HttpServlet,que,porsuavez,herdade GenericServlet.Sequisermosreescrever
ométodoinit(ServletConfig)emnossaclasse,devemossemprenoslembrarde
invocaro super.init(ServletConfig),casocontrárioa ServletConfignãoserá
guardadacomoatributona HttpServlet,fazendoorespectivogetterretornar null,
quebrandomuitoscódigos,comoaseguir:
public class LogServlet extends HttpServlet {
public void init(ServletConfig cfg) throws ServletException {
log("Inicializando a servlet");
}
public void doGet(HttpServletRequest req, HttpServletResponse res) {
// vai lançar NullPointerException
getServletConfig().getInitParameter("...");
}
}
Ousodeheran çaparacriarumafilhade HttpServletgeranecessidadedesa-
bercomoométodo init(ServletConfig)foiimplementadonaclassemãe,oque
consisteemumaquebradeencapsulamento.
NamudançadeAPIdaServlet2.0paraa2.1,houveainser çãodeummétodo
paratentarevitaresteproblema,quesetornararecorrenteentreosdesenvolvedo-
res.Onovométodo init(),semparâmetros,deveserreescrito;eleéinvocadopelo
próprioinit(ServletConfig)apóso ServletConfigserguardadoemumatributo.
Dentrodeum init()reescritopodemosobteracessoao ServletConfigatravésdo
getterdaclassemãe,queagoraestarácorretamenteatribuído.Mesmoassim,emra-
zãodatomadadedecisãooriginalnaAPIdeservlet,odesenvolvedoraindadeve
conhecercomoessesmétodosfuncionamnaclassemãe,poissóassimsaberádeto-
dososcuidadosquesãonecessários.
Masnemtudoénegativo.Todoessedesigndeservletstemcomoobjetivoprin-
cipaltrazeropolimorfismoeumainterfacedeusouniformeparaasservletsserem
chamadaspelocontainer. Contudo,emJava,épossívelusar interfaceparapoli-
morfismo,semospontosnegativosdaheran çacomoquebradeencapsulamentoe
altoacoplamento.AAPIdeservletspoderiaterusadoumdesignbaseadoeminter-
facescomum strategypatternporexemplo,evitandoaheran ça.Umasugestãoseria
umainterface InvocationProcessorcommétodoscomo init(ServletConfig)e
process:
53

## Página 74

3.3. Eviteherança,favoreçacomposição CasadoCódigo
public interface InvocationProcessor {
void init(ServletConfig config);
void process(HttpServletRequest req, HttpServletResponse res);
boolean shouldProcess(HttpServletRequest request);
void destroy();
}
Poderíamoscriarváriasimplementações,cadaumacapazdelidarcomasrequi-
siçõesqueacharconveniente,como,porexemplo,paraométodo GET:
public class GetProcessor implements InvocationProcessor {
public void init(ServletConfig config) { }
public boolean shouldProcess(HttpServletRequest request) {
return "GET".equals(request.getMethod());
}
public void process(HttpServletRequest req, HttpServletResponse res) {
// código de processamento aqui
}
public void destroy(ServletConfig config) { }
}
Aosubstituiraheran çaporinterface,continuamoscomobenefíciodopolimor-
fismo.Masheran çaaindatrazoutrograndebenefício,oreaproveitamentodecódigo,
algoqueinterfacespurasnãofazem. Podemos então usar interfaces com composi-
ção, obtendo substitutos para todos os benefícios de herança sem correr o risco de
cair na armadilha da quebra de encapsulamento e alto acoplamento.Repareque,
destaforma,oacoplamentoébemmenor,nenhumadasclassesprecisaconhecero
funcionamentointernodasoutras.
Porém,sefornecessárioousodeheran ça,algunscuidadossãoimportantespara
minimizarapossívelquebradeencapsulamento.JoshuaBloch,no EffectiveJava,fala
deDesignforInheritance,([17])comdiversaspráticascomoevitarinvocaçõesentre
métodospúblicos,paraqueasobrescritadeumnãomudeocomportamentode
outro.
Aomesmotempoquedesejamosevitarheran ça,temosinteresseempermitir
mudançanonossocomportamentosemanecessidadedealteraroucopiarocódigo
original.Mantendopontosdeextensão,permitimosqueclassesqueimplementam
umadeterminadainterfacesejamcapazesdemodificarocomportamentodeoutras
54

## Página 75

CasadoCódigo Capítulo3. TópicosdeOrientaçãoaObjetos
classes. Atravésdeinterfacesecomposição,podemoscriardesdeumnovodriver
JDBCparaumdeterminadobancodedados,ouflexibilizartrabalhossimples,como
ordernarlistascom Comparatorsimplementandodiferentescritériosdecompara-
ção.Esteprincípio,demantersuasclassesabertasparaextensãosemanecessidade
dealteraçãonocódigooriginal,échamado OpenClosedPrinciple.[124]
Evite herança, favoreça composiçãoéumdedoisprincípiosfundamentaisde
designdolivro DesignPatterns,comfrequênciareferenciadonaliteratura. [79],
[206]
3.4 F avoreça imutabilidade e simplicidade
Doisclientescomamesmadatadepagamentonãopodemcompartilharinstâncias
de Calendar,pois,seumdelesalterarovencimento,essamudan çaresultariaem
umefeitocolateralprovavelmenteindesejado:ooutrotambémsofreaalteraç ão.A
classe Calendarpermitemudançanoestadodesuasinstânciase,portanto,diz-se
queaclasseémutável,comooexemploaseguirdemonstra:
Calendar data = new GregorianCalendar(2004, 2, 13);
cliente.setVencimento(data);
Calendar doisDiasDepois = cliente.getVencimento();
doisDiasDepois.add(Calendar.DAY_OF_MONTH, 2);
outroCliente.setVencimento(doisDiasDepois);
// efeito colateral:
System.out.println(cliente.getVencimento());
Aclasse Stringtemcomportamentodiferente.Quandocome çamosaprogra-
marcomJava,passamosporumcódigosemelhanteaoquesegue:
String s = "java";
s.toUpperCase();
System.out.println(s);
Estecódigo,queaparececomfrequêncianasprovasdecertificaç ão,imprimirá
javaemletrasminúsculas.Issoporqueaclasse Stringéditaimutável.Todomé-
todoinvocadoemuma String,queparecemodificá-la,sempredevolveumanova
55

## Página 76

3.4. Favoreçaimutabilidadeesimplicidade CasadoCódigo
instânciacomaalteraçãorequisitada,masnuncaalteraainstânciaoriginal.Aotor-
narumaclasseimutável,umaamplagamadeproblemascomunsdesaparece.[82],
[17]
Simplicidade e previsibilidade
Objetosimutáveissãomuitomaissimplesdemanipularqueosmutáveis,tendo
umcomportamentobemprevisível:
String s = "arquitetura";
removeCaracteres(s);
System.out.println(s);
Nãoimportaoqueométodo removeCaracteres(s)faça,asaídaapresentaráar-
quitetura.Objetosimutáveisnãosofremefeitoscolaterais,poistêmcomportamento
previsívelemrelaçãoaoseuestado.Comparecomumcódigosemelhante,maspas-
sandoumareferênciaaumobjetomutável;nocaso,um Calendar:
Calendar c = Calendar.getInstance();
verificaFeriado(c);
System.out.println(c.get(Calendar.YEAR));
Pormaisexplícitoquesejaonomedométodo,nãoépossívelafirmar,apenascom
estetrechodecódigo,qualéasaídanoconsole,poisométodo verificaFeriado
pode alterar algum dado desta instância deCalendar. Os próprios engenhei-
ros da Sun admitiram alguns erros de design das APIs antigas, como a classe
java.util.Calendarsermutável. [16]Porisso,muitasvezesrecorremosàsAPIs
deterceiros,comoa Joda Time,nasquaisencontramosentidadesdedatas,horários
eintervalosimutáveis.
Quandooobjetoémutável,paraevitarquealguémomodifique,temosqueto-
maralgumaprecaução. Umasolução,frequentementeusadacomcole çõesatravés
do Collections.unmodifiableList(List)eseussimilares,éinterfacearoobjeto
eembrulhá-lodetalformaqueosmétodosexpostosnãopossibilitemmodificaç ão.
Emvezdepassarareferênciaoriginaladiante,passamosessanovareferência,cuja
instâncialançaexceçõesemqualquertentativademodificação.
Outrasoluçãoparaobjetosmutáveisécriar cópias defensivas doobjeto. Em
vezdedevolveroobjetooriginalquesedesejapreservar,criamosumacópia,por
exemplo,atravésdométodoclone,edevolvemosestacópia.Ousuário,destaforma,
56

## Página 77

CasadoCódigo Capítulo3. TópicosdeOrientaçãoaObjetos
nãotemcomoalteraroobjetooriginal,masrecebeumacópiaparausopróprio,que,
sealterar,afetaráapenasasimesmo.
Objetosimutáveissãomaissimplesdeselidar. Depoisdesuacriaç ão,sempre
saberemosseuvalorenãoprecisamostomarcuidadosadicionaisparapreservá-lo.
Objetosmutáveis,emcontrapartida,comfrequêncianecessitamdeumcuidadoadi-
cional,cujoobjetivoéevitaralteraçõesinesperadas.
Otimizações de memória
Podemostirarproveitodaimutabilidadedeoutrasformas.[82]Comocadaob-
jetorepresentaapenasumestado,vocênãoprecisamaisdoqueumainstânciapara
cadaestado.AprópriaAPIdalinguagemJavausaaimutabilidadecomoumavan-
tagemparafazercacheereaproveitamentodeinstâncias.
Éocasodo pooldeStringsdaJVM,quefazcomque Stringsdemesmocon-
teúdopossamserrepresentadasporumaúnicainstânciacompartilhada.Omesmo
aconteceemboapartedasimplementaçõesdasclasseswrappercomo Integer.Ao
invocarInteger.valueOf(int),areferênciaa Integerdevolvidapodeserfrutode
umcacheinternodeobjetoscomnúmerosmaisfrequentementesolicitados.[41]
Essetipodeotimizaçãosóépossívelcomobjetosimutáveis.Ésegurocomparti-
lharinstânciasde Stringsou Integerscomdiferentespartesdoprograma,semo
riscodequeumaalteraçãonoobjetotragaefeitoscolateraisindesejadosemoutras
partesdosistema.
Ehámaispossibilidadesaindaparaotimizaçõesgraçasàimutabilidade.Aclasse
Stringaindaseaproveitadessacaracterísticaparacompartilharseuarrayde char
internoentre Stringsdiferentes. Seolharmosseucódigofonte,veremosqueela
possuitrêsatributosprincipais:um char[] valueedoisinteiros, counte offset;
[133]estesinteirosservemparaindicaroinícioeofimda Stringdentrodoarrayde
char
Seumétodosubstring(int,int)levaemcontaaimutabilidadedas Stringse
osdoisinteirosquecontrolaminícioefimparareaproveitaroarrayde char.Quando
pedimosumadeterminada substring,emvezdeoJavacriarumnovoarrayde char
comopedaçoemquestão,eledevolveumnovoobjeto String,queinternamente
compartilhaareferênciaparaomesmoarrayde charquea Stringoriginal,etem
apenasosseusdoisíndicesajustados.Ouseja,criarumasubstringemJavaémuito
leve,sendoapenasumaquestãodeajustardoisnúmerosinteiros(Figura3.3).
57

## Página 78

3.4. Favoreçaimutabilidadeesimplicidade CasadoCódigo
Figura3.3:CompartilhandoomesmoarrayentreduasStringsdistintas.
Essaotimizaçãoéumaimplementaçãoumpoucomaissimplesdodesignpattern
flyweight,emquesepropõereaproveitarobjetoscomobjetivodediminuirousoda
memória. [17]Oprópriopoolde Stringspodeserconsideradoum flyweight. E
poderíamosirmaislongecomo flyweight,implementandoaconcatenaçãodeStrings
apontandoparadiversasoutrasStringsinternamenteaoinvésdecopiarosdados
paraseupróprioarraydechar.Nestecaso,aAPIdoJavapreferenãochegaraeste
ponto,pois,apesardeumganhodememória,haveriao trade-offdoaumentode
processamento.
Éválidotambémressaltaroperigodecertasotimizaçõesemalgunscasos. Na
otimizaçãodosubstring,porexemplo,uma Stringpequenapodeacabarsegurando
referênciaparaumarrayde charsmuitograndeseelafoioriginadaapartirdeuma
Stringlonga.Issoimpediriaqueoarraymaiorfossecoletado,mesmosenãopos-
suirmosreferênciasparaa Stringoriginal.
Hátambémumexcessodememóriaconsumidatemporariamente. Comimu-
tabilidade,cadainvocaçãodemétodocriaumanovacópiadoobjetoapenascom
algumaalteraçãoe,seistoestiverdentrodeumlaço,diversascópiastemporárias
serãoutilizadas,masapenasoresultadofinaléguardado. Aqui,ousodopattern
builderpodeajudar,comoéocasodaclassemutável StringBuilder(ousuaversão
threadsafe StringBuffer)comseumétodo appendemvezde String.concat(ou
ooperadorsobrecarregado +)emumlaço.
58

## Página 79

CasadoCódigo Capítulo3. TópicosdeOrientaçãoaObjetos
Acesso por várias threads
Definirregiõescríticascom synchronizedéaindaumasoluçãorepetidamente
encontradaaomanipularmemóriacompartilhada.Destaforma,evitamosqueduas
escritasconcorrentesseentrelacemequeleiturassejamcapazesdeacessardados
inconsistentesouintermediários.
Atarefadifícilédefinirtodasasregiõescríticasequaissãomutuamenteexclu-
sivas;definirumaregiãomuitograndegeraperdadevazão(throughtput ),enquanto
umadetamanhoinsuficienteimplicaráosmesmosproblemasdenãotê-las.
Emvezderecorreraosrecursosdaslinguagens,pensemosnessesobjetosde
formadiferente,evitandoesseestadointermediário,nãopermitindoamudan çade
valores.Avantageméa thread-safety,pois,comonãoexistemestadosintermediá-
rios,nãohácomoacessarnemmodificardadosemmomentosdeinconsistência.
Oestadoinconsistenteficaescondidonalógicadeconstruç ão,eonovoestadosó
estarádisponívelquandoterminardeserconstruído,paraentãotersuareferência
compartilhadapormaisdeumathread.
Aslinguagensfuncionaismaispuras,como ErlangeHaskell,estãosendoutiliza-
dasemambientesdegrandeconcorrência,dadasuacaracterísticadetrabalharquase
queapenascomvaloresimutáveis.Perde-seoconceitode variávelcomooconhece-
mos,jáqueosvaloresnãomudam;nascememorremcomomesmoestado.Você
éobrigadoaprogramarapenasdemaneiraimutável,oqueéumaenormemudan ça
deparadigma. MuitasdessaslinguagenspodemrodarsobreaJVM,comoScala,
que,apesardesuportarmutabilidade,temfortesraízesemprogramaç ãofuncionale
recomendaousodeimutabilidade.
Imutabilidade e encadeamento de invocações de métodos
Umavezqueasclassessãoimutáveis,osmétodosnãopossuemefeitoscolaterais
e,portanto,devemdevolverumareferênciaaumnovoobjeto(Figura3.4).Logo,é
naturalencadearinvocaçõesdemétodos(methodchaining ),viabilizandoacriação
decódigomaislegível:
Data vencimento = new Data();
Calendar proximaParcela = vencimento.adicionaMes(1)
.proximoDiaUtil()
.toCalendar();
59

## Página 80

3.4. Favoreçaimutabilidadeesimplicidade CasadoCódigo
Figura3.4:Cadainvocaçãodemétodoquecriaumasituaç ãonova,criaumestado
novo,devolveareferênciaparaumobjetonovo.
OmesmoacontececomoutrasclassesimutáveisdoJava,como BigDecimal,
BigIntegereString:
String valor = "arquiteturajava.com.br";
String resultado = valor.toUpperCase().trim().substring(6);
Methodchaining éumapráticasimplesquepermiteacriaçãodeinterfacesflu-
entes(fluentinterfaces)([72])que,juntocomoutrospadrõeseaplicadaadomínios
específicos,permiteacriaçãode DSLs.
Criando uma classe imutável
Para que uma classe seja imutável, ela precisa atender a algumas
características:[17]
• Nenhummétodopodemodificarseuestado.
• Eladeveserfinal,paraevitarquefilhaspermitammutabilidade.
• Osatributosdevemserprivados.
• Osatributosdevemserfinal.
• Casosuaclassetenhacomposiçõescomobjetosmutáveis, elesdevemter
acessoexclusivopelasuaclasse,devolvendocópiasdefensivasquandoneces-
sário.
60

## Página 81

CasadoCódigo Capítulo3. TópicosdeOrientaçãoaObjetos
Umaclasseimutávelficariacomo:
public final class Ano {
private final int ano;
public Ano(int ano) {
this.ano = ano;
}
public int getAno() {
return this.ano;
}
}
Estecódigoseriamaiscomplicadosenossaclasseimutávelfossecompostadeob-
jetosmutáveis.Umaclasse Periodoimutável,implementadacomCalendars,preci-
sarátrabalharcomcópiasdefensivasemdoismomentos.Primeiro,quandoreceber
algum Calendarcomoparâmetroe,depois,quandodevolveralgum Calendarque
façapartedacomposiçãodoobjeto. Senãocopiarmososobjetos,épossívelque
algumcódigoexternoàclasse Periodoaltereos Calendarsemquestão,gerando
inconsistência.
Noteascópiasdefensivasnoconstrutorenosgettersnoseguintecódigo:
public final class Periodo {
private final Calendar inicio;
private final Calendar fim;
public Periodo(Calendar inicio, Calendar fim) {
this.inicio = (Calendar) inicio.clone();
this.fim = (Calendar) fim.clone();
}
public Calendar getInicio() {
return (Calendar) inicio.clone();
}
public Calendar getFim() {
return (Calendar) fim.clone();
}
}
61

## Página 82

3.5. Cuidadocomomodeloanêmico CasadoCódigo
Aproveitamosaquiofatode Calendar implementarCloneable,casocontrário
precisaríamosfazeracópiamanualmente,criandoumnovoobjetoealterandoos
atributospertinentesumaum.
Comonossaclasseéimutável,seprecisarmoscalcularalgumainformaç ãoque
exijaqualquermodificação,clonamosoobjeto.Éocasodeummétodoqueadieo
períodoemumasemana,ouseja,somesetediasaofimdoperíodo:
public Periodo adiaUmaSemana() {
Calendar novoFim = (Calendar) this.fim.clone();
novoFim.add(Calendar.DAY_OF_MONTH, 7);
return new Periodo(inicio, novoFim);
}
E, com uma pequena modificação, podemos implementar o design pattern
flyweightemnossaclasse,compartilhandoainstânciado Calendardeiníciodo,pe-
ríodoentreoobjetooriginaleonovo,comumasemanaadiada.Paratanto,preci-
saríamosdeumoutroconstrutorprivadoparaserchamadono adiaUmaSemanaque
nãofizesseo clone.
Utilizarclassesimutáveistrazumtrabalhoamaisjuntocomosdiversosbenefí-
ciosdescritos. Você deve considerar fortemente criar sua classe como imutável.
3.5 C uidado com o modelo anêmico
Umdosconceitosfundamentaisdaorientaç ãoaobjetoséodequevocênãodeve
exporseusdetalhesdeimplementação. Encapsulandoaimplementação,podemos
trocá-lacomfacilidade,jáquenãoexisteoutrocódigodependendodessesdetalhes,
eousuáriosópodeacessarseuobjetoatravésdocontratodefinidopelasuainterface
pública.[21]
Costumeiramente,aprendemosqueoprimeiropassonessadire çãoédeclarar
todosseusatributoscomo private:
public class Conta {
private double limite;
private double saldo;
}
Paraacessaressesatributos,umdesenvolvedorqueaindaestejaaprendendovai
rapidamentecairemalgumtutorial,quesugereacriaç ãode gettersesetterspara
podertrabalharcomessesatributos:
62

## Página 83

CasadoCódigo Capítulo3. TópicosdeOrientaçãoaObjetos
public class Conta {
private double limite;
private double saldo;
public double getSaldo() {
return saldo;
}
public void setSaldo(double saldo) {
this.saldo = saldo;
}
public double getLimite() {
return limite;
}
public void setLimite(double limite) {
this.limite = limite;
}
}
Essaclassecontémalgunsmétodosqueacabamporferirasideiasdoencapsula-
mento.OmétodosetSaldoéumbomexemplodisso,jáquedificilmenteosaldoem
umaentidade Contaserásimplesmente“substituído”poroutro.Paraalterarosaldo
deumaconta,énecessárioalgumaoperaçãoquefaçamaissentidoparaodomínio,
comosaquesoudepósitos.
Nunca crie um getter ou setter sem uma necessidade real;lembre-sedeque
precisamosqueessanecessidadesejaclaraparacriarqualquermétodoquecoloca-
mosemumaclasse. Particularmente,os gettersesetterssãocampeõesquandofa-
lamosemmétodosqueacabamnuncasendoinvocadose,alémdisso,grandeparte
dosutilizadospoderiasersubstituídapormétodosdenegócio.[100]
EssapráticafoiincentivadanosprimórdiosdoAWT,paraoqualerarecomen-
dadocriar gettersesettersparasereminvocadosnopreenchimentodecadacampo
visualdasuainterfacegráficacomousuário,cunhandootermo JavaBean.OsEJBs
tambémcontribuíramparaestaprática,comoserávistoadiante.
Criandoclassesdestaforma,istoé,adicionando gettersesetterssemsercriteri-
oso,códigoscomo conta.setSaldo(conta.getSaldo() + 100)estarãoespalhados
portodaaaplicação.Seforpreciso,porexemplo,queumataxasejadebitadatoda
vezqueumdepósitoérealizado,seránecessáriopercorrertodoocódigoemodificar
63

## Página 84

3.5. Cuidadocomomodeloanêmico CasadoCódigo
essasdiversasinvocações.Umsearch/replaceocorreriaaqui;péssimosinal.Podemos
tentarcontornarissoepensaremcriarumaclasseresponsávelporestalógica:
public class Banco {
public void deposita(Conta conta, double valor) {
conta.setSaldo(conta.getSaldo() + valor);
}
public void saca(Conta conta, double valor) {
if (conta.getSaldo() >= valor) {
conta.setSaldo(conta.getSaldo() - valor);
} else {
throw new SaldoInsuficienteException();
}
}
}
Essetipodeclassetemumacaracterísticabemprocedural,fortementesinalizada
pelaausênciadeatributoseexcessodousodemétodoscomofun ções(depositae
sacapoderiamserestáticos).Alémdisso,pode-sedizerqueestaclassetemuma in-
timidadeinapropriadacomaclasse Conta,poisconhecedemaissuaimplementação
interna.Reparequeométodo sacaverificaprimeiroseosaldoémaiorqueovalor
asersacado,para,então,retirarodinheiro.Essetipodelógicadeveriaestardentro
daprópriaclasse Conta.
Oprincípiodo Tell,Don’tAskpregaexatamenteisso:vocêdevedizeraosobjetos
oquefazer(comosacardinheiro),evitandoperguntaremexcessooestadoaoobjeto,
comogetSaldo,e,apartirdesseestado,tomarumadecisão.[172]
Essetipodeclasseécomumenteencontradaeéclassificadacomoopattern Bu-
sinessObject porconcentraralógicadenegócios.Jáaclasse Conta,porterapenas
osdados,recebiaonome ValueObject(hoje,estepatterntemoutrosignificado).Da
formacomoestá,temosseparadosnossosdadosnaclasse Contaealógicadenegócio
naclasse Banco,rompendooprincípiobásicodemantercomportamentoeestado
relacionadosemumaúnicaclasse.
Éoquechamamosde modelo anêmico(anemicdomainmodel ),[77],noqual
nossaclasse Contaparecenãoterresponsabilidadealgumanosistema,nenhuma
açãorelacionada. Énecessárioumaclasseexterna, Banco,paradaralgumaaç ão
paranossa Conta,tratando-aquasecomoumfantoche.[29]Comisso,aclasse Banco
conhecedetalhesdaimplementaçãodaclasse Contae,seestamudar, Bancomuito
provavelmentemudarájunto.
64

## Página 85

CasadoCódigo Capítulo3. TópicosdeOrientaçãoaObjetos
Podemosuniralógicadenegócioaosdadosdeumamaneirasimples,inserindo
métodosnaclasse Contaeremovendoosqueapenasacessamemodificamdireta-
menteseusatributos:
public class Conta {
private double saldo;
private double limite;
public Conta(double limite) {
this.limite = limite;
}
public void deposita(double valor) {
this.saldo += valor;
}
public void saca(double valor) {
if (this.saldo + this.limite >= valor) {
this.saldo -= valor;
} else {
throw new SaldoInsuficienteException();
}
}
public double getSaldo() {
return this.saldo;
}
}
Aquimantivemoso getSaldo,poisfazpartedodomínio.Tambémadicionamos
algumasmanipulaçõesaométodo saca,epoderíamosdebitaralgumimpostoem
cimadequalquermovimentaçãofinanceiranométodo deposita. Enriqueça suas
classes com métodos de negócio, para que não se tornem apenas estruturas de
dados.Paraisso,cuidadoaocolocar gettersesettersindiscriminadamente.Devemos
encapsularosdadosematributosdeobjetose,ainda,lembrarqueaorientaç ãoa
objetospregaatrocademensagens(invocaçãodemétodos)demaneiraaconcentrar
asresponsabilidadesaquempertenceosdados.OpróprioAlanKay,quecunhouo
termo“programaçãoorientadaaobjetos”,ressaltaque“otermofoiumamáescolha,
poisdiminuiaênfasedaideiamaisimportante,atrocademensagens”.[35]
ÉpossívelseguiramesmalinhaparaentidadesdoJPA/Hibernate,verificando
65

## Página 86

3.6. ConsidereDomain-DrivenDesign CasadoCódigo
arealnecessidadedosgettersesetters.Porexemplo,anecessidadedeummétodo
setIdparaachaveprimáriatorna-sediscutívelnomomentoemqueumframework
utilizareflectionoumanipulaçãodebytecodeparaleratributosprivados.
Algumasvezes,os gettersesetterssão,sim,necessários,ealgunspatternsaté
mesmoprecisamdeumaseparaç ãodelógicadenegóciosdosrespectivosdados.
[73]Práticascomoo TestDrivenDevelopment podemajudaranãocriarmétodos
semnecessidade.
Porém,frequentemente,entidadessemlógicadenegócio,comcomportamentos
codificadosisoladamentenos businessobjects,caracterizamummodelodedomínio
anêmico.Émuitofácilterminarcolocandoalógicadenegócio,quepoderiaestarem
emnossasentidades,diretamenteemActionsdoStruts, ActionListenersdoSwing
emanagedbeansdoJSF,transformando-osem transactionscripts.Estemodeloacaba
ficandocomumforteapeloproceduralevaidiretamentenacontramãodasboas
práticasdeorientaçãoaobjetosedo Domain-DrivenDesign.[21],[57]
3.6 C onsidere Domain-D riven Design
Todosoftwareédesenvolvidocomumpropósitoconcreto,pararesolverproblemas
reaisqueacontecemcompessoasreais. Todososconceitosaoredordo problema
aserresolvidosãooquedenominamosdomínio. Oobjetivodetodaaplicaç ãoé
resolverasquestõesdeumdeterminadodomínio.
Domain-DrivenDesign(DDD)significaguiaroprocessodedesigndasuaaplica-
çãopelodomínio.Pareceóbvio,masmuitossoftwaresnãosãoprojetadosdeacordo
comodomínioemqueatuam.Podemosperceberessarealidadeanalisandoocódigo
dediversossistemasatuais,nosquaisasentidadesnãocondizemcomarealidadedos
usuáriosesãodedifícilentendimento.[57],[77]
SegundooDDD,éimpossívelresolveroproblemanodomíniodoclientesem
entendê-loprofundamente.Éclaroqueodesenvolvedornãoquersetornarumcom-
pletoespecialistanaáreadocliente,masdevecompreendê-laosuficienteparade-
senvolverguiadopelodomínio.
Paraistoacontecer,oponto-chaveéa conversa.Conversaconstanteeprofunda
entreosespecialistasdedomínioeosdesenvolvedores. Aquelesqueconhecemo
domínioemdetalhesdevemtransmitirconhecimentoaosdesenvolvedores.Juntos,
chegarãoatermosevocábulosemcomum,uma línguacomum,quetodosutilizem.
Éachamada Língua Ubíqua(UbiquitousLanguage).
Estalínguaébaseadanostermosdodomínio,nãototalmenteaprofundadaneste,
66

## Página 87

CasadoCódigo Capítulo3. TópicosdeOrientaçãoaObjetos
masosuficienteparadescreverosproblemasdemaneirasucintaecompleta.
Duranteaconversaconstante,cria-seum modelo do domínio(ouDomainMo-
del). Éumaabstraçãodoproblemareal,queenvolveosaspectosdodomínioque
devemserexpressadosnosistema,desenvolvidaemparceriapelosespecialistasdo
domínioedesenvolvedores. Éestemodeloqueosdesenvolvedoresimplementam
emcódigo,quedeveocorrerliteralmente,itemporitem,comofoiacordadoporto-
dos.Istopossibilitaodesenvolvimentodeumcódigomaisclaro,e,principalmente,
queutilizametáforasprópriasdodomínioemquestão.
Seuprogramadeveexpressarariquezado domainmodel. Qualquermudança
nomodelodeveserrefletidanocódigo. Casoomodelosetorneinviávelparase
implementartecnicamente,eledevesermudadoparasetornarimplementável.
Esseprocessonãoocorreantesdoiníciodoprojeto,maséumtrabalhocons-
tante,quedeveserrevisitadoatodoinstante.PraticandoDDD,écomumencontrar
situaçõesemqueoespecialistaeosdesenvolvedoresaprendemmaissobreodomí-
nioerefatoramocódigoesuasentidadesàmedidaqueoprojetoédesenvolvidoe,
porisso,práticasde TestDrivenDesign erefatoraçãosãocomplementaresaDDD.
NoDDD,seucódigosempreseráaexpressãodomodelo,que,porsuavez,é
guiadopelodomínio.
AprincipalliteraturasobreDomain-DrivenDesignéolivrohomônimode
EricEvans.<spanclass="char-style-override-4”>26Nele,oautorapresentaoqueé
oDDD,alínguaubíquaeparteparaum catálogodedesignpatterns.Esses patterns
citadosporEvanssãoferramentasquefacilitamaimplementaç ãodo DomainModel
nosoftware.Elessãoexcessivamentereferenciadosemartigos,masnãosãooponto
principaldoDDD.
Emmuitasdiscussõesemtornodoassunto,comfrequênciaencontram-sere-
ceitasmágicasque,aparentemente,podemseraplicadasemqualquerprojeto.Este
éumdosmaioreserrosquesepodecometer.Nãoexistereceitapronta,etampouco
apenasumaúnicamaneiradeescreversuasclasses.SedesejausarDDD,lembre-se
doprincipal: odomínio. VocêpodecriarumModelriquíssimoeumdesignele-
gante;mas,seelenãoforumaexpressãofieldo Domain,senãoforapartirdalíngua
comum,vocênãoestáusandoDDDeomodelosofrerácomasuadiferen çacomo
domínio.
As quatro camadas do DDD
Evanspropõeemseulivroadivisãodaaplicaç ãoemquatrocamadas(layers),
parafavoreceroisolamentododomínio,oencapsulamento,aflexibilidadeefacilitar
67

## Página 88

3.6. ConsidereDomain-DrivenDesign CasadoCódigo
oDDD(Figura3.5).
Ainterfaceeainteraçãocomousuário(Swing,HTML,etc.)sãoa UI Layer.A
Application Layeréqueauxiliaodomínioaserexecutado,entregandoetraduzindo
asinformaçõesdequeodomínioprecisa.OprincipalpontodoDDDéomodelodo
domínioesuaslógicasdenegócio,queformamo Domain Layer.Porfim,a Infras-
tructure Layercontémserviçosdeinfraestruturanecessáriosaofuncionamentodas
outraslayers,persistência,segurança,enviodee-mail,entreoutros(Figura3.5).
Naimplementaçãoda DomainLayer,surgemnecessidadesmaisortogonaisou
serviçosmaiscomplicadosquefogemdodomínioemquestão,comopersistênciae
comunicaçãoSMTPparaenviodee-mails.Épapelda InfrastructureLayerservira
DomainLayereàsoutrascamadascomessasfacilidades.
Figura3.5:AsquatrocamadasdoDDD.
AUILayer,comumentechamada view,éresponsávelpelainterfaceentreousuá-
rioeseusistema.Éelaqueinteragecomousuário,recebendosuasaçõeseexibindo
umarepresentaçãodomodelo. ApplicationLayeréumacamadafinaquefazaponte
68

## Página 89

CasadoCódigo Capítulo3. TópicosdeOrientaçãoaObjetos
entreainterfaceeomodelododomínio. Éelaquecoordenaeestimulaomodelo
deformaaatenderàrequisiçãodaUI.Namaioriadossistemas,éumacamadabem
simples,emuitasvezesinexistente;sevocêusaumbomframeworkcontrolador,é
bemcapazqueelejáconsigafazeressaponteentreUIemodeloautomaticamente.
ODDDétodosobrea DomainLayer.ÉnelequeestáaquestãodaUbiquitous
Languageedodomainmodel.EnessamesmacamadaentramospatternsqueEvans
cita,osquaissãofrequentementediscutidosnacomunidade.
HámuitospatternsapresentadosporEvans: algunsnovos,outrosde model-
drivendesigneatéalgunsdoGoFrevisitados.Umdosmaissimpleséo V alue Object,
quemodelaumobjetogeralmenteimutávelondeoquerealmenteinteressaéseuva-
lor. Sãoobjetoscomo java.util.Calendarou java.awt.Color,emquenãohá
identidade,edoisobjetoscommesmovalorsãoiguaisperanteosistema(umlugar
quetenhaumobjeto Calendarcomadatadehoje,podesertrocadoporumoutro
objetoCalendarcomamesmadata).
HáaindaopatternEntity(Entidade),quetratadeobjetoscomidentidadeúnica,
eciclodevidaquequeremoscontrolar. Emumalojavirtual,porexemplo,um
Produtopodeseruma entity.Doisprodutoscommesmonomesãocoisasdiferentes,
enãopodemsertrocados(háidentidadeemcadaobjeto,nãoéapenasovalorque
conta).Ociclodevidatambémébemdefinido.Oobjetoécriadoemumcertomo-
mentodecadastro,suarepresentaçãopodeserpersistidaerestauradadeumbanco
dedados,eeleéjogadoforaquandoforremovido.
Sobreociclodevidadas entities,Evanspropõeaindaumasériedepatterns.
DesdeaversãoDDDpara Factory,aplicadaàcamadadedomínio,atéofamosoe
mal-entendidoRepository.Esteéumpadrãointeressanteparadiscutirvárioscon-
ceitosdoDDDeenxergarseusprincipaispontosemrelaç ãoàmodelagemdodomí-
nio.
Repositórios
Muitosdomíniosprecisampersistirdados.O Domainexpert (oespecialistado
domínio)podenãosaberoqueéumbancodedadosnemosignificadode persis-
tência,massabequequer cadastrarosclientesdesuaempresaparadepois procurar
nessecadastro.Oclientedizparaodesenvolvedor(aconversa)queprecisa contro-
larseuestoquedeprodutosparadepois buscarquaisprodutosestãoembaixa. O
usuáriotem,intuitivamente,oconceitodepersistênciaeacessodasinformações.
Jáodesenvolvedor,conhecetudodebancosdedados,integridaderelacional,
Hibernate,relacionamentos,SQL,normalizaçãoequalqueroutrodetalhetécnico
69

## Página 90

3.6. ConsidereDomain-DrivenDesign CasadoCódigo
envolvido.Nadadissoépertinenteaodomíniodocliente,emborasejamtodoscon-
ceitosfundamentaisparaseimplementarano çãodepersistênciaqueousuáriotem
nacabeça.Éaíqueentrao Repository.
SegundoEvans,repositórioéumnomequeaparecenalínguaubíquapararepre-
sentaraqueleconceitorudimentardepersistênciaqueexistenacabe çadocliente.É
norepositórioquecadastramosasinformações.Énelequevamos,depois,procurar
objetosjácadastrados.Pormeiodele,controlamososobjetosebuscamosinforma-
çõessobreeles.
AimplementaçãoemsidorepositórionãoéfocodoDDD.Odesenvolvedor
provavelmentecriaráumDAOcomJPAouJDBC,ouumaimplementaç ãodiretade
umainterface,masissofogedoescopododomainmodel. EscreverSQLecódigo
demanipulaçãodebancodedadosnãofazparteda DomainLayer,amenosque
seudomíniosejabancosdedados.Tudoissofazpartedacamadadeinfraestrutura,
lugarondeseuDAOdeveestar. Acamadadedomaindeveapenaspensaremum
repositóriodeobjetosnoqualasoperaçõesdepersistênciaacontecem.
OsdesenvolvedoresconhecemopadrãoDAOcomoumaformadeencapsular
asparticularidadesdoacessoabancodedados(ouaalgumabasededados)eisolar
essacomplexidadedorestantedoprograma. Agora,oDDDpropõeorepositório,
querepresentaolugarondenossosobjetossãocolocadosparaquedepoispossa-
mosrecuperá-los.E,infelizmente,muitosconcluemqueRepositórioeDAOsãoo
mesmo.Nãosão,emborasejafatoqueissotudogeramuitaconfusão.
Repositórioéumconceitodo DomainLayer,quetemdefazerpartedo Modelo.
Noteadiferen ça:DAOsurgedoproblemadeencapsularfuncionalidadesespecíficas
deinfraestrutura;oRepositório,danecessidadedoclientedeguardareobterobjetos
dodomínio.
Onomedorepositórionãodeveseralgointernoaocódigo,masdevefazerparte
dalínguaubíqua;deveaparecernasconversasenoDomainModel. Deveserum
conceitoqueoespecialistadedomíniotambémentendae,porqueestáno Model,é
queelevaiparaocódigo.Nãoháproblemaemtrazerpalavreadotécnicoparaa Ubi-
quitousLanguage,desdequetodosentendamosignificado,mantendooprincípio
dalínguaubíqua.
OpadrãoDAOnãofazpartedalínguaubíqua,masdacamadadeinfraestrutura.
ExisteumarelaçãoentreRepositórioseDAOs,poisgeralmenteasbuscassãofeitas
nobancodedados,ecostumaserboapráticaterumDAOparatanto,masoDDD
mesmonãodiznadasobreoassunto,jáqueistoestáforadodomínio.
SegundooDDD,háváriasimplementaçõespossíveis,todasboas,desdequevocê
70

## Página 91

CasadoCódigo Capítulo3. TópicosdeOrientaçãoaObjetos
sigaosconceitosdiscutidos.UmaencontradacomfrequênciaérepresentaroRepo-
sitórionacamadadodomínioatravésdeumainterfaceJavaimplementadadireto
nacamadadeinfraestrutura.Emcasosmaiscomplexos,orepositóriopodeseruma
classeconcretaquedelegachamadasparamaisdeumDAOnainfraestrutura.Mas
istonãoéregra.Desenvolvapensandonodomínio,etemosDDD.Poderíamoster:
public interface ClientesRepository {
List<Cliente> getPorNome(String nome);
List<Boleto> getPorCliente(Cliente cliente);
}
Seriamuitomaisconvenienteterainterfaceeseusmétodoscomnomesmais
orientadosadomínio,[31]como Clientesparaainterface,ouainda:
public interface TodosClientes {
List<Cliente> comNome(String nome);
}
public interface TodosBoletos {
List<Boleto> doCliente(Cliente cliente);
}
Onome TodosClientesajudanoentendimentodoqueéumrepositório;tecni-
camente,eletentasimularumacole çãoemmemória,masnaverdadeépersistente.
Estacaracterísticaajudaoclienteaentenderoqueorepositóriofazduranteuma
conversacomosdesenvolvedores.Algunsdetalhesdequedevemosnoslembrarao
usarosrepositóriossãoevitartermétodoscomnomestécnicoseagruparasfunci-
onalidadesportipo;seummétodoretornaumalistadeboletos,eleprovavelmente
pertenceaorepositóriodeboletos.
Domain-Specific Language
Aproveitandoadiscussãosobremodeloedomínio,percebemosque,aocriarum
códigobaseadonomodelo,eleficadelimitadopeloselementosqueforemabordados
noescopododomínio,e,consequentemente,nalínguaubíqua.
Essasclasseseosmétodosdaaplicaçãoserãoespecíficosparaumdeterminado
problema; nestecaso, então, acabamoscriandoumabibliotecaespecíficaparao
domíniodaaplicação,epodemosconsiderarqueestabibliotecaéuma DSL,ou
Domain-SpecificLanguage.
71

## Página 92

3.6. ConsidereDomain-DrivenDesign CasadoCódigo
Seconsiderarmosquetudooquefoicriadousaumalinguagemhospedeira,por
exemploJavaouRuby,estamosfalandode DSLsinternas.
OcódigoaseguirmostraumexemploemJavadeDSLinterna:
cliente.fazReserva(paraQuarto(numeroDoQuarto)).
de(dataDeInicio).ate(dataDeSaida);
Podemosencararessetrechodecódigocomoumanovalinguagem.Masperceba
queeleaindarespeitaasregrasdesintaxedoJava,sualinguagemhospedeira. É
códigoJavaválido. Ousodeumalinguagemhospedeiraéoquecaracterizauma
DSLinterna.
EssasDSLsbeneficiam-sedefuncionalidadesquesualinguagempossui. Para
projetarecriaruma DSLinterna,podemosusartécnicasdeprogramaçãoquealin-
guagemhospedeirapermite,comooencadeamentodemétodos(MethodChaining )
donossoexemplo.
Issotornaaconstruçãode DSLsinternasmuitomaissimples.Diversasvezes,es-
sasDSLssurgemnaturalmenteaorefatorarocódigoparaqueexpressecadavezmais
odomínioealínguaubíqua.Encadeamentodemétodos, varargs,staticimports,ge-
nerics,polimorfismo,classesanônimaseproxiesdinâmicossãoalgumasdasfunci-
onalidadesaplicadasnaconstruçãode DSLsinternasemJava.As DSLssãocriadas
emcimadeummodeloquerepresentaodomínio,ummodelosemântico (semantic
model).[62]
ReparenosexemplosaseguirumaDSLdeumrepositório,quepermiteacom-
posiçãodeumatarefaapartirdepartesmenores:
List<Quarto> vagas = quartos.vagosNoPeriodo(proximaSemanaUtil())
.dosTipos(Tipos.PADRAO, Tipos.LUXO)
.lista();
List<Cliente> hospedes = clientes.queSeHospedaram(data)
.nos(quartos.doTipo(Tipos.PADRAO))
.lista();
Alémdisso,nadanosimpedede,emvezdeusarumaDSLhospedadaemuma
GPL(GeneralPurposeLanguage,ouLinguagemdePropósitoGeral),criarumanova
sintaxeelinguagempararesolveroproblema.ChamamosessaslinguagensdeDSL
externa.Exemplo:
cliente faz reserva do quarto 215 de 12/02/1990 ate 20/02/1990
72

## Página 93

CasadoCódigo Capítulo3. TópicosdeOrientaçãoaObjetos
Agrandevantagemdecriaruma DSLexternaéapossibilidadederestringirseu
vocabulário,dexando-abempróximadalínguaubíqua. ExemplosdeDSLsexter-
nassãoSQL,CSSeexpressãoregular. [62]Outroaspectoimportanteéquea DSL
externatambémnãoprecisarespeitarasregrasdesintaxedenenhumalinguagem
hospedeira,oquedáumaenormeflexibilidadeaoprojetá-la.
Poroutrolado,adesvantagemde DSLsexternaséaimplementaçãodeinter-
pretadores,parserse/oucompiladores. Jáquecriamosumanovasintaxe,émuito
trabalhosoconceberuminterpretador,parseroucompiladordozero. Parsergenera-
tors,tambémconhecidoscomocompiladoresdecompiladores(compilercompilers),
ajudambastante.Mesmoassim,aindanãoéumatarefafácil.
Háalgunsanos,tinha-seaideiadequeacriaç ãodeDSLsserviriaparaque,atra-
vésdelas,pessoasquenãosãoprogramadoresconseguissemescreversuaspróprias
rotinas. Mas,apósalgumtempodediscussãosobreoassunto,essaideiaperdeu
forçae,atualmente,pensa-sequeasDSLsdevamserescritasporprogramadores,
mascontinuemfáceisdelerporpessoasquenãoprogramam,comoéocasodos
businessexperts.[74]
Aotrabalharcom DSLs,considereousodeframeworksqueauxiliemnasuacri-
ação. UmdosframeworksJavamaisusadosparacriar DSLsexternaséoANTLR,
umparsergeneratorusadoemimportantesprojetos,comonainterpretaçãode HQL
(HibernateQueryLanguage).EmRuby,háoGherkin,usadopeloCucumbernain-
terpretaçãodesuasespecificaçõesexecutáveis.OHamcrest,usadonoJMock,ajuda
bastantenacriaçãode DSLsinternasemJava,alémdepermitiracriaçãodecompo-
nentesreutilizáveisentreDSLsdistintas.
DSLspodemserescritascomênfaseemqualquerdomínio,trazendoparaode-
senvolvimentodosoftwareacapacidadedeexprimirumcomportamento,através
dalinguagemmaispróximadarealidadedoproblemaaserresolvido,etentandore-
moveraomáximooruídosintáticodabiblioteca,linguagemoupadrõesutilizados
parasuportá-la.Amaiorpartedocódigopassaaserescritacomovocabuláriodo
domínio,enãomaiscomodaferramenta.
73

## Página 95

Capítulo4
Separaçãoderesponsabilidades
Aopensarnodesigndeumaaplicaç ão,ofoconãodeveserapenasnarelaç ãoentre
doisobjetos,mastambémentregruposdeobjetosquetrabalhamemconjuntopara
umadeterminadafinalidade. Aodesenharpequenasclassesque,juntas,realizam
umatarefamaior,oprogramadorganhaemsimplicidadeemodularidade.
Émaissimplesmanterumsistemacompostoporclassesquecontêmapenasuma
responsabilidadebemdefinida,jáqueaalteraçãodeumcomportamentoéfeitoem
umaúnicaclassedosistema. Poresseeoutrosmotivos,oprogramadordevebus-
carclassescombaixoacoplamentoealtacoesão,evitandopadrõesconhecidosque
levamadesignsrígidosedealtocustodemanuten ção.
4.1 O btenha baixo acoplamento e alta coesão
Pararealizaralteraçõescomfacilidadeemumsistema,queremosquemudan çasem
umapartedelenãoimpliquemmaismudan çasemoutras.Anecessidadedeatuali-
zaçõesemdiversospontosdocódigonomomentoderealizaralgumaalteraç ãode

## Página 96

4.1. Obtenhabaixoacoplamentoealtacoesão CasadoCódigo
funcionalidadepodeindicarqueessespontosestãoligados(ouacoplados)dema-
neiraindesejada. Acoplamentoéoquantodoiselementosestãoamarradosentresi
equantoasalteraçõesnocomportamentodeumafetamodeoutro.
Pode-sefalardoacoplamentoentreduasclasses,oudoquantodoismódulos
daaplicaçãoestãoamarrados,ou,ainda,avaliaroquantodoisframeworksdistintos
sãoafetadosumpelooutro.Nãosequer,porexemplo,alterarumaclasse Usuario
porquehouvemudan çasnaregrada ControleDeAcesso,outerdealterarDAOspor
causademudan çasnaView,ouaindaserimpedidodeusaralgumframeworkWeb
porqueadotamosHibernateparapersistência.
Partesdosistemapodemserchamadasdecomponentes. Classesindividuais,
conjuntodeclasses,umpacoteouatémesmoumabibliotecacontidaemumarquivo
JARsãoexemplosdecomponentes. Emtodososcasos,minimizaroacoplamento
implicatambémfacilitaratrocadosmesmos,alémdeserpe çafundamentalparaa
manutençãodocódigo,formandoumaarquiteturademaiorqualidade.
Masbaixoacoplamentoédiferentedenenhumacoplamento.Paraquedoiscom-
ponentessecomuniquem,semprehaveráumaligação.Aobuscarfacilidadedema-
nutençãoalongoprazo,devemoslutarparaqueessaligaç ãosejaamenoremais
simplespossível.Descobrir,entenderegerenciaressasdependênciaséumadaspar-
tesmaiscomplicadasdoprocessodedesenvolvimentodesoftware.BobMartindiz
queosdesignsdeterioramàmedidaquenovosrequisitosfor çammudançasquenão
foramprevistas,eissofazcomquesejamintroduzidasdependênciasnovasenão
planejadasentreclassesemódulosdosistema.[126]Fowlertemumaopiniãopare-
cidaedizque,àmedidaqueossistemascrescem,énecessáriaumamaioraten çãoao
gerenciamentodessasdependências,pois,casocontrário,simplesalteraçõespodem
serpropagadasparaoutrasclassesoumódulos,prejudicandoassimaevoluç ãodo
software.[69]
Encapsulamentoebomusodeinterfacessãoessenciaisparadiminuiroacopla-
mentoentrecomponentes,masháaindaumpontoimportantequandosepensaem
umnívelmaisalto,olhando-separaosistemacomoumtodo:as responsabilidades
decadacomponente.Arazãodaexistênciadetodocomponenteéexerceralgumtipo
defun çãonosistema,assumircertorequisitocomosuaresponsabilidade. Euma
importanteeboapráticaégarantirqueeletenhatenha alta coesão,oquesignifica
garantirquesuasresponsabilidadessejamrelacionadasefaç amsentidojuntas,ou
seja,quenãohajaresponsabilidadesdesconexasdentrodeummesmocomponente.
Issofacilitaoentendimentoefuturamodificaçãodocomponente,alémdeaumentar
suaschancesdereutilizaçãojáque,emgeral,poucaspartesdosistemaprecisariam
76

## Página 97

CasadoCódigo Capítulo4. Separaçãoderesponsabilidades
deumcomponentecomresponsabilidadesmuitodiversas.
BobMartindefiniuresponsabilidadecomo“umarazãoparamudan ça”,emseu
artigo“SingleResponsibilityPrinciple”.[120]Nele,Martindefendeque,alémdeter
altacoesão,ocomponentedeveterapenasumaúnicaresponsabilidade,“emmo-
mentoalgumdeveexistirmaisdeummotivoparaalterarumaclasse”.Issodiminui
oacoplamentoentreresponsabilidadesdiferentes,evitandoquemudan çasemuma
afetemaoutra.Nessemesmoartigo,eleaindacita:“sevocêconseguepensaremmais
deummotivodemudan çaparasuaclasse,entãoelatemmaisdeumaresponsabili-
dade”.
Umconceitoaindamaisamploedifundidocomoexcelentepráticaarquitetu-
raléoda Separação de Responsabilidades,ou SoC,doinglêsSeparationofCon-
cerns.Paradiminuiroacoplamento,aumentaracoesão,promoveraflexibilidadee
garantirresponsabilidadesúnicas,éprecisosabersepararessasresponsabilidades.
Háquemdigaqueotermoapareceupelaprimeiravezem1974,naspalavrasdeEds-
gerDijkstra,quandoargumentavaque,aodesenvolverumsoftware,muitosaspectos
diferentesdevemsertratados.[47]E,comoelediz:“Nadaseganha–aocontrário!–
abordandoessesdiversosaspectossimultaneamente.Éoqueeualgumasvezeschamei
de‘separaçãoderesponsabilidades”’.E,maisàfrente,explica:“Issonãosignificaigno-
rarosoutrosaspectos,masestarapenasfazendojusti çaaofatodeque,sobopontode
vistadeumaspecto,ooutroéirrelevante”.
Emumnívelmaispróximoaocódigo,ummétodoqueverificapermissõesdo
usuáriologadoemontaumrelatório,possuimaisdeumaresponsabilidadediferente
erequerrefatoração. Aqui,separarsignificacriardoismétodosdistintos,umpara
aautorizaçãoeoutroparaaexecuç ãodatarefa.Levandoopensamentoaumnível
superior,casoosmétodosfiquemnamesmaclasse,elacontinuacomdoispapéis
distintos: autenticaçãoeexecução. Oresultadoseriasepararocódigoentreduas
classes.Ou,maisainda,empacotesousubmódulosdiferentesdaaplicaç ão.Eaté,se
forocaso,emframeworksespecializadosemcadatarefa.
Comosepodever,essetrabalhopodeserfeitoemdiversosníveis,enãosóem
linguagensorientadasaobjeto.NomundoWeb,arquivosHTMLpreocupam-seem
descreverconteúdo,arquivosCSSdescrevemaapresentaçãoe,porfim,arquivosJa-
vaScript,alógicadasuapágina. Épossívelmisturartodoocódigo,mastambém
podemossepará-loemdiversaspartes,cadaumacomsuaprópriaresponsabilidade.
Aolongodosanos,SoCfoiganhandodefiniçõesmaisrobustasesetornouam-
plamentedifundido.Emorientaçãoaobjetos,muitosefaladoassuntoparadefinir
opapeldecadaclassedosistema.Fala-sedeSoCquandoseorganizaascamadasda
77

## Página 98

4.2. Gerenciesuasdependênciasatravésdeinjeção CasadoCódigo
aplicação,naseparaçãodo MVC,narelaçãocominversãodecontrole,orientaç ãoa
aspectoseemváriasoutrassituações.
Háváriaspráticaseabordagensquefacilitamaseparaçãoderesponsabilidades,
comoveremosnospróximostópicos.
4.2 G erencie suas dependências através de injeção
Mesmocomobaixoacoplamentohaverásempreumaligaçãoentreduasclassesque
precisamtrabalharemconjunto. Normalmente,háumaclassequenecessitados
serviçosoferecidosporoutra.Qualquermudan çanestaclassequeestásendoaces-
sadapodeafetarocomportamentodaprimeira. Háaquiumarelaç ãonaturalde
dependência.[110]Relaçõescomoessaindicamaindaqueasemânticadoclienteé
incompletasemofornecedor.[69]
Suponhaumaclassechamada CalculadoraDeSalario,responsávelporcalcu-
lar o salário de um determinado funcionário. Para estimar quais impostos se-
rãodescontadosdoempregado,estaclasseprecisada TabelaDeImpostos. Existe
umarelaçãodedependênciaentreessasduasclassese, porisso, dizemosquea
CalculadoraDeSalario dependeda TabelaDeImpostos. Quandooassuntoéor-
ganizaçãodeclasseseobjetos,asdependênciasentreasdiversaspartesdosistema
sãoumassuntodelicado.Devemosnosesfor çaraomáximoparadiminuiroacopla-
mento.
Umcasorecorrenteemdiversosprojetoséatentativadeencapsulartodooacesso
adados(persistência)deumaaplicação,centralizando-oemobjetosespecíficos,apli-
candoopattern DataAccessObject (DAO).
public class ProjetoDao {
public void salva(Projeto projeto) {
// ...
}
public void remove(Projeto projeto) {
// ...
}
public Projeto carrega(Long id) {
// ...
}
}
78

## Página 99

CasadoCódigo Capítulo4. Separaçãoderesponsabilidades
PartindodoprincípiodequeessaclasseutilizadiretamenteJDBCparaoacesso
aobanco,elaprecisadeumaconexão,umareferênciaa java.sql.Connection,em
todososseusmétodos.Ousodealgumframeworkparaacessoadadosoudema-
peamentoobjeto-relacionalnãoresolveriaoproblema,jáqueelaprecisariadealgo
análogoaumaSessionouEntityManager.
OproblemaéqueoDAOfoicriadoparaencapsularosdetalhesdeacessoaos
dados,porém,precisadealgunsrecursos(nestecaso,umaconexão)pararealizar
seutrabalho.Seriaomesmocasocomum EnviadorDeEmails,quenecessitadeuma
conexãocomoSMTP,porexemplo.
Umaprimeirapossibilidadeparaobterumareferênciapara Connectionseria
abrirconexõesdiretamentenosmétodosquenecessitamdelas,deixandoosdetalhes
porcontadopróprioDAO:
public class ProjetoDao {
public void salva(Projeto projeto) throws SQLException {
String url = "jdbc:mysql://localhost/db";
String usuario = "root";
String senha = "password";
Connection connection =
DriverManager.getConnection(url, usuario, senha);
// ::uso da conexão ...::
connection.close();
}
// ::outros métodos do DAO::
}
OcódigoanteriorserveparaconectaremumabasedoMySQL.Éinviávelrepeti-
loemtodososoutroslugaresqueprecisemdeconexão.Alémdisso,aindaexistem
diversosoutrosdetalhesimportantesaseremconsiderados,comoaexternalizaç ão
dasconfiguraçõeseousodeum pool de conexões paragerenciamentomaisinteli-
gentedosrecursos.
Reparequeaclasse ProjetoDao temresponsabilidadesdemais;alémdesaber
comosalvar,buscarealterarprojetos,aindaéresponsávelporcriarumaconexão
comabasededados. Elaéumtípicoexemplodeumaclassecombaixacoesão,
devidoatantasresponsabilidades.
79

## Página 100

4.2. Gerenciesuasdependênciasatravésdeinjeção CasadoCódigo
Oprimeiropassoparaamenizaroproblemaécentralizaroprocessodecriar
conexões. Dessaforma,aclassepodedependerapenasdeumainterfaceeignorar
completamenteosdetalhesdecriaçãodeconexões(seaconexãoénova,seveiode
umpool,qualdriverestamosusando,etc.).Ousodeuma factorypermiteesconder
ecentralizartaisdetalhesetrocaressaestratégiamaisadiante,casonecessário.
public void salva(Projeto projeto) throws SQLException {
Connection connection = new ConnectionFactory().getConnection();
// ::uso da conexão:: ...
connection.close();
}
Aobtençãodasconexõesficamaissimples,masaindanãoresolveoproblema.
Comessecódigo,nãoépossívelsalvardois Projetosutilizandoamesmaconexão,
nemexecutardoismétodosdoDAOdentrodeumamesmatransaç ão;acadanova
invocaçãodemétodoumanovaconexãoéadquirida. Essaéumamáprática,co-
nhecidacomo SessãoporOpera ção,TransaçãoporOpera ção,ouainda Conexãopor
Operação(Session/ConnectionperOperation).
Seriapossívelagruparasoperaçõesqueprecisamdamesmaconexão/transaç ão
dentrodeummesmométododoDAO:
public void salva(Projeto projeto, Gerente gerente) {
Connection connection = new ConnectionFactory().getConnection();
// ...
connection.close();
}
Mas,nestecaso,oDAOacabariacomumagrandequantidadedemétodos,a
maioriaformadapraticamentepelacombinaçãodeoutros. Esteéumclaroexem-
plodepéssimadivisãoderesponsabilidades,jáqueoDAOtrabalhademais,abre
conexão,cuidadetransação,fechaconexão,alémdatarefaquerealmentelhecabe:
acessardados.Qualquernovotipodetransaçãodaaplicaçãoexigeumnovométodo
noDAO.
Dealgumaformaéprecisopermitirqueamesmaconexãosejautilizadaemdi-
versosmétodosdoDAO,guardando-aemumatributo.Precisamostambémdeum
localparaabriraconexão:
80

## Página 101

CasadoCódigo Capítulo4. Separaçãoderesponsabilidades
public class ProjetoDao {
private Connection connection;
public void inicia() {
this.connection = new ConnectionFactory().getConnection();
}
}
CriarummétodoparainiciaroDAOeabriraconexãoresolveumproblema,
masgeraoutro.Podemosnosesquecerdeinvocarométodo inicia,fazendocom
que Connectionseja null. OobjetoDAOnãoéum Bom Cidadão (GoodCitizen
Pattern),[145]jáquepodeserinstanciadosemquetodasassuasdependênciaseste-
jamresolvidas.
Paraqueumobjetosejaumbomcidadão,eledevesempreestaremumestado
consistente.Paratanto,ousodoconstrutoréessencial,noqualsãopreenchidasto-
dasasdependênciasnecessáriasparaqueoobjetopossatrabalharadequadamente,
semasubsequentenecessidadedeinvocar settersououtrosmétodosdeinicializa-
çãoeconfiguração.Oprincípioaindavaialém,definindoalgumasboaspráticasna
manipulaçãodeexce ções,loggingeprogramaçãodefensiva,tornandoessesobjetos
maissegurosemrelaçãoacódigodeterceiros.
AseguinteversãodoDAOusaoconstrutorpararesolveroproblemaefor çaa
aquisiçãodaconexãonomomentodesuainstanciaç ão:
public class ProjetoDao {
private final Connection connection;
public ProjetoDao() {
this.connection = new ConnectionFactory().getConnection();
// ::poderia também abrir uma transação::
}
public void fecha() {
// ::poderíamos consolidar a transação::
this.connection.close();
}
}
Aconexãoéabertanoconstrutor,porém,Javanãotemdestrutores.Mesmoque
tivesse,ouoprogramadorusasseométodo finalize,nãoseriaumasoluç ãoade-
quada,jáquenãoháagarantiadequandoumobjetoserácoletadopelo Garbage
81

## Página 102

4.2. Gerenciesuasdependênciasatravésdeinjeção CasadoCódigo
Collector.Éfundamentaltercontrolesobreondeequandoasconexõessãoabertas
efechadas,tendoemvistaqueesteéumrecursocaro,talcomodescritoresdear-
quivos,threads,socketseoutrosqueusamdeI/Oououtraschamadasaosistema
operacional.
ComoonossoDAOjádetémaresponsabilidadedecriaraconexão,éseupapel
fechá-la.Ométodofechapareceserasolução,jáqueagoraépossívelinstanciaro
DAOeinvocarváriasoperaçõesdentrodamesmaconexão/transação.Aindaassim,
estasoluçãopossuialgunsproblemas:
• Ométodofechaquebraoencapsulamento,jáqueexpõeumdetalheespecí-
ficodestaimplementaçãodeDAOqueestamosusando;existeumaconexão
quedeveserfechada.Seaimplementaç ãodoDAOfortrocadaporumaque
persistaemarquivosXML,porexemplo,nãohaveriamaisnecessidadedeter
ométodofecha,poisnãoexistiriamaisnenhumaconexãoaserfechada.Ao
mesmotempo,nãosepodesimplesmenteremoverométodo fecha,jáqueele
estánainterfacepúblicadosDAOs;issoquebrariatodososseusclientes. É
nessemomentoquecome çamasurgirasimplementaçõesvaziasdemétodos.
• Aboapráticadiz:“seabrir,feche”!Destaforma,evita-seespalhararesponsa-
bilidadedegerenciarorecursoqueestamosmanipulando.Oproblemaéque
oDAOabreaconexão,masnãosabequandofechá-la,edelegaestatarefaa
quemoutiliza.Osusuáriosdaclasseficamresponsáveisporinvocarométodo
fechaesaberondefecharalgoquenemforamelesqueabriram.Aresponsa-
bilidadedegerenciarconexõesficaassimmuitoespalhadapelosistema;todos
sãoresponsáveisporsaberqueumaconexãoexiste,quandoéabertaequando
deveserfechada.
• Nãoháerrosdecompilaçãopornãoinvocarométodo fecha,portanto,nin-
guéméobrigadoainvocá-lo.Comoaresponsabilidadeseespalhaportodoo
sistema,achancedeseesquecerdefecharaconexãoaumentamuito,paranão
dizerqueéinevitável.Issogeraproblemasdevazamentodeconexões,quenão
sãofechadasepodemresultarnodesastrosoefeitodobancorejeitandonovas
conexõesquandojáexistiremmuitasabertas.
• Fecharaconexãocostumasermaiscomplexoqueumasimplesinvocaçãoao
métodoclose.Podehavernecessidadedecontrolarasexce çõesouexecutar
rollbacknocasodeumapossíveltransaçãodeixadaaberta.Sehouverumpool,
fecharpodesignificardevolveraconexãoparalá.Paranãorepetiressecódigo
82

## Página 103

CasadoCódigo Capítulo4. Separaçãoderesponsabilidades
emtodososDAOs,poderíamosencapsulá-lo,talcomofizemoscomacriaç ão
na ConnectionFactory. Masaindaprecisamosnoslembrardechamaresse
novométodoemtodososlugares,espalhandonovamentearesponsabilidade.
• Parapiorar,nestaabordagemaindanãoépossívelsalvarumProjeto,atualizar
um Usuarioeremoveruma Historiausandoamesmaconexão,oudentro
damesmatransação. ComocadaDAOpossuisuaprópriaconexão,nãohá
comocompartilharamesmaentreváriosdeles;oescopodeexistênciadeuma
conexãoéinternoaodeumDAO.
AsoluçãoparatodosessesproblemasétirardoDAOaresponsabilidadedege-
renciaraberturaefechamentodeconexões.Suaúnicaresponsabilidade(SingleRes-
ponsibilityPrinciple)[120]serátratardasoperaçõesdemanipulaçãodobanco,mas
semapreocupaçãodegerenciarconexões.Aumentamossuacoesãoediminuímos
seuacoplamentocomoutraspartesdosistema.
Mas não podemos simplesmente remover todo o código relacionado a
Connection.ParaexecutarseuscomandosSQL,eleaindaprecisadeumaconexão.
Emvez,então,decriarumanovaconexãonoDAO,elepassaareceberumaconexão
jácriadaporalguém. E,comestaconexão,poderáexecutarsuaresponsabilidade
demanipularobancodedadossemoutraspreocupações. Receberaconexãoem
vezdecriá-laéumexemplodoprincípioda Injeção de dependências(Dependency
Injection–DI).Umaformafácildecodificarseriarecebendonoconstrutordaclasse:
public class ProjetoDao {
private final Connection connection;
public ProjetoDao(Connection connection) {
this.connection = connection;
}
public void adiciona(Projeto p) {
// ::usa a connection::
}
// ::não precisamos de um método fecha()::
}
Aodizerqueosobjetosnãovãomaisatrásdesuasdependências,masqueagora
devemapenasrecebê-lasdealguém,invertemosquemestánocontroledegerenciar
83

## Página 104

4.2. Gerenciesuasdependênciasatravésdeinjeção CasadoCódigo
adependência.Emvezdefazerosobjetosirematrásdaquiloqueprecisam,opro-
gramadorfazcomqueelesrecebamosobjetosjáinicializadosepreparadosparauso.
Éoquesechamade Inversão de Controle (InversionofControl–IoC).Injeçãode
dependênciaséumadasformasmaiscomunsdeIoC.[119],[89]
Esteconceitoteveorigemháumbomtempo,nopaperdeRichardSweetem
1988,[193]queintroduziuo Hollywood Principle:“Don’tcall,uswewillcallyou!”
(nãonoschame,nósochamaremos!).Oobjetivoé,aoinvésdedecidiromomento
certodeinvocarcadacomponente,deixar-seserinvocadoquandoadequado. Ao
invésdedecidiromelhormomentoparainvocarcertocomponente,deixa-seser
invocadoporalguémquevaijulgaromomentocorreto.EmDI,vemosestaprática
aodeixardeinvocarocódigodegerenciamentodaconexãoepassaraserinvocado,
porexemplo,noconstrutor,comtudojáprontoparausoFigura4.1.
Figura4.1:Nãonoschame,nósochamaremos:HollywoodPrinciple
Masainversãopodeaconteceremoutroscenários,quenãonogerenciamento
dedependências. Umaaplicaçãovisualpodeprecisarsaberquandocertobotãoé
pressionado.Emvezdeverificaroestadodobotãodetemposemtempos,pode-se
apenasregistrarumlistenerqueseránotificadoquandooeventoocorrer.Ocódigo
84

## Página 105

CasadoCódigo Capítulo4. Separaçãoderesponsabilidades
detratamentodoeventopassaaserinvocadopelobotão,emvezdeinvocarmétodos
paradescobrirseuestado.Ocontrolefoiinvertido.Outroexemplosãooscontainers
WebeEJBdoJavaEE,queinvocamnomomentocertoosmétodosdeumaServlet
ouoscallbacksdeumEJB. DI é uma das formas de implementar IoC, mas não a
única.
VoltandoaoexemplodeDI,restaaquestãodequemgerenciaráaconexão.
AquelequedesejausaroDAO,precisarásepreocuparcomisso. Imagineumsis-
temaWebcomcentenasdeActionsdiferentes,todasenvolvendoousodealgum
DAO.Antes,podia-sesimplesmentecriá-losemsepreocuparcomconexão;agora
passa-seasepreocuparcomaconexão:
public class AdicionaProjetoAction {
public void execute() {
Connection connection;
connection = new ConnectionFactory().getConnection();
ProjetoDao dao = new ProjetoDao(connection);
dao.adiciona(...);
}
}
Usar aConnectionFactory alivia um pouco do problema, mas não é uma
boa solução. A action, além de ter responsabilidades normais ligadas a Web,
comomanipular requesteresponse, agoratambémestáacopladaa Connection,
ConnectionFactoryeDAO.Comodiminuiresseacoplamento?
Injeçãodedependênciasnovamente.Aúnicaresponsabilidadedaactionéadi-
cionarumprojetonoDAO,e,paraisso,sónecessitadeumDAO,nãoprecisase
preocuparcomosdetalhesdesuacriaç ãooudeaberturadeconexão:
public class AdicionaProjetoAction {
private final ProjetoDao dao;
public AdicionaProjetoAction(ProjetoDao dao) {
this.dao = dao;
}
public void execute() {
this.dao.adiciona(...);
}
}
85

## Página 106

4.2. Gerenciesuasdependênciasatravésdeinjeção CasadoCódigo
Podeparecerqueestamosapenasempurrandooproblema,jáquealguémterá
quecriaressaAction.E,agora,instanciá-laexigeaexistênciadeumDAO,que,por
suavez,exigiráumaconexão.Oproblemapareceaumentar.MasosegredodeDI
épensaremcadacomponenteisoladamente,deumamaneiraquaseegoístacom
relaçãoaorestantedosistema. ÉjustamenteoprincípiodeHollywoodnaprática,
pensandoemcadaclassecomoopontomaisimportantedaaplicaç ãoeempurrando
responsabilidadessecundáriasparaoutraclasselidar.
Mas,claro,alguémteráqueresolveresseemaranhadodedependênciasemal-
gumahora. Seráalgumcomponentedosistemacujaúnicaresponsabilidadeseja
exatamentealigação(wiring,ouamarrar,injetar)dasdependências. Éocompo-
nentequeestaránocontroledaaplicação,paraquetodoorestopossausarDIeIoC.
Nainjeçãodedependências,existeumdependente(oDAO)eumadependência(a
conexão);equemamarratudoissoéumprovedor(provider ).Porseralgotãoimpor-
tanteebastantecomumemdiversasaplicações,normalmenteusa-seumframework
prontocomoprovider.Spring,PicoContainer,GoogleGuiceeoCDIdoJavaEE6
sãoexemplosdecontainerdeDI,comoveremosnotópicoseguinte.
Éimportanteressaltar,porém,adiferen çaentreapráticadeInje çãodeDepen-
dênciaseousodealgumframeworkespecífico.Inverterocontroleedeclararsuas
dependênciasparaserinjetadasporalguéméconsideradoumaboapráticadede-
sign,eéatémesmoumdesignpatternbemaceito.[151]Devemosprogramarnossas
classescomDIsemprequepossível.
Masissonãoimplicaquesejamosobrigadosausaralgumframeworkcomoos
citadosanteriormente.HáquemdefendaevitarousodeframeworksdeDIequeo
própriocódigodegerenciamentodasdependênciassejaimplementado,jáqueéalgo
quecostumaserfácildeserescritopeloprogramador,alémdeficarmaisexplícito
comoosobjetosserelacionam.[118],[163]Éumaopiniãoquegerabastantepolêmica,
jáqueosframeworksmodernossãosimplesdeusarelivramoprogramadordemais
umadordecabe ça,pormenorqueelapossaser. Háaindaumadiscussão:se,em
linguagensmaisflexíveisqueJava,comoScalaouRuby,apróprialinguagemjánão
trazrecursosequivalentesaosframeworksdeDI.[20],[107]
Independentementedaformadeseimplementar,épraticamenteconsensoqueo
usodeInje çãodeDependênciaséumapráticadedesignquaseobrigatória.Comas
vantagensdediminuiroacoplamentoentreoscomponentes,aumentaracoesãodas
partesdosistemaepromoverumamelhorseparaç ãoderesponsabilidades,ousode
DIéaltamenterecomendado.
86

## Página 107

CasadoCódigo Capítulo4. Separaçãoderesponsabilidades
4.3 C onsidere usar um framework de Injeção de De-
pendências
Discutimosnotópicoanterioraimportânciadousodainversãodecontroleedain-
jeçãodedependências.Mesmosendoconsideradaumaboapráticadedesign,ainda
trazalgunsdesafios,poisgerenciarasdependênciasdetodasasclassesdoprojeto
nãoétarefafácil. Hámuitascomplicaçõesenvolvidas,comotratardasdependên-
ciasdedependências,cuidardacriaçãoeliberaçãodoscomponentesegerenciaro
momentoemquetudoissodeveserfeito.
Visandofacilitaressetrabalho,surgiramdiversosframeworksdeinje çãodede-
pendências.Umdosprincipais,emimportânciaeemuso,éo Spring Framework,
idealizadoporRodJohnson.PioneiroemDI,oSpringnasceucomsuporteapenas
àchamadainje çãoviasetter:
public class AdicionaProjetoAction {
private ProjetoDao dao;
public setDao(ProjetoDao dao) {
this.dao = dao;
}
// ...
}
Suaconfiguração,durantemuitotempo,suportavaapenasXML,comonotrecho
aseguir:
<beans ...>
<bean id="adicionaAction” class=”br.com.arquiteturajava.AdicionaProjetoAction
<property name="dao”>
<ref local="projetoDao”/>
</property>
</bean>
</beans>
Essaantigaabordagemdeusarsettersparainje ção,porém,ébastanteproblemá-
tica.Seadependência,poralgummotivo,nãoestiverdisponível,aclasseserácriada
emumestadoinconsistente,nãoseráum GoodCitizen.Invocarosmétodosdene-
góciopodecausar NullPointerExceptionsindesejadas,jáqueareferêncianãoterá
87

## Página 108

4.3. ConsidereusarumframeworkdeInje çãodeDependências CasadoCódigo
sidopreenchida.Alémdisso,semautilizaçãodeumaferramentadeinje çãodede-
pendências,odesenvolvedoréobrigadoalembrardeinvocarossettersapropriados
antesdeefetivamenteusaroobjeto,comoaoescrevertestesdeunidades.
Comotempo,oSpringpassouasuportarinje çãoviaconstrutores,alémdecon-
figuraçõescomanotações,diversasconvençõesesimplificações.
Oframeworkcresceuapontodeintegrartambémdiversosoutrosserviçosefun-
cionalidades,comoAOP,persistência,controletransacional,MVCe,maisrecente-
mente,atéusocomoutraslinguagensedentrodaplataformadeclouddaVMWare.
Ocomponentecentralemtudoissosemprefoiocontainerdeinje çãodedependên-
cias,queconsagrouoSpring.
Masfoio PicoContainer,outrodosprincipaisframeworksdeDI,oprimeiroa
implementarinjeçãoviaconstrutores.Essetipodeinje çãosolucionaoproblemado
métodosetteraoexigirqueasdependênciasnecessáriasparaofuncionamentodo
objetosejampassadasaoinstanciá-lo. Porestemotivoe,porrespeitaroprincípio
dobomcidadão,ousodeinje çãoporconstrutoréomaisutilizadoatualmente.
IdealizadoporPaulHammanteAslakHellesoy,oPicoéumframeworkquecar-
regaaténonomeaideiademinimalismoesimplicidade.SeuúnicofocoéDI,sem
possuirtodososdesdobramentosqueoSpringeoutrosframeworkspossuem. Ele
surgiuquestionandooexcessodeconfiguraçõesemXMLdoSpringeoutrosfra-
meworks,etrouxeumaabordagemdeconfiguraç ãoprogramáticaatravésdapró-
prialinguagemJava,comasvantagensdeevitarerrosemtempodecompilaç ãoe
autocompletardeIDEs.
// ::exemplo de classe com dependência no construtor::
public class AdicionaProjetoAction {
private final ProjetoDao dao;
public AdicionaProjetoAction(ProjetoDao dao) {
this.dao = dao;
}
public void execute() {
this.dao.adiciona(...);
}
}
// ::configuração programática em algum outro lugar::
MutablePicoContainer pico = new DefaultPicoContainer();
88

## Página 109

CasadoCódigo Capítulo4. Separaçãoderesponsabilidades
pico.addComponent(ProjetoDao.class);
pico.addComponent(AdicionaProjetoAction.class);
Mesmomudandoaforma,aconfiguraçãodoPicoaindaseriaexterna,easclas-
sesdodesenvolvedornãoteriamligaç ãofortecomoframework.Éatépossívelmi-
grardeumcontainerparaooutroapenasportandoaconfiguraç ão,semmexernas
classesdaaplicação.Hoje,oPicoContainersuportatambémconfiguraçãoporano-
tações,injeçãoporsetterseoutrosrecursosmaiscomplexosparagerenciamentodas
dependências.[157]
Outraformadeinje ção,alémdossetterseconstrutores,queaparecebastanteno
EJB3.xmastambémemoutrosframeworks,éainje çãodiretamenteematributos.O
apelodestaabordageméasimplicidadedocódigodaclasse,quenãoprecisanemde
setternemdeconstrutor,masnãocostumaseraabordagempreferidaparausodeDI.
Escreverumtestedeunidadeparaumaclassequerecebeasdependênciasvaiexigiro
usodereflectionparaconseguirinjetá-la.Paraevitaristo,osframeworksqueoptam
porestetipodeinje çãocriaramoutrosframeworks,queservemsimplesmentepara
facilitaraescritadessestestes. Issomostraoquantoodesignficaacopladocoma
ferramentaespecífica,masestetipodeacoplamentodeveserevitadoaomáximo.
ComocrescimentodousodeanotaçõesemJava,osframeworksdeDIpassa-
ramaoferecerseuusocomoalternativaparaaconfiguraç ão.O Google Guicefoium
dosprimeirosaoferecerconfiguraçãodoscomponentesedasinje çõesusandoano-
tações.Comaanotação com.google.inject.Injectfazemosaúnicaconfiguração
necessária:
public class AdicionaProjetoAction {
private final ProjetoDao dao;
@Inject
public AdicionaProjetoAction(ProjetoDao dao) {
this.dao = dao;
}
public void execute() {
this.dao.adiciona(...);
}
}
Ousodeanotaçõessimplificouasconfigurações,mastrouxeàtonaadiscussão
sobreacoplamentocomoframework.NoSpring,porexemplo,énecessárioanotar
89

## Página 110

4.3. ConsidereusarumframeworkdeInje çãodeDependências CasadoCódigo
ospontosdeinje çãocom @AutoWired,ounoGuice,com @Inject–ambasespecí-
ficasdecadaumdeles.Trocardeframeworknessecenárioébastantetrabalhoso;o
Pico,porexemplo,atétentaminimizaroproblemasuportandoanotaçõesdeoutros
frameworks,comooGuice,masessenãoéomelhorcenário.
ApossívelsoluçãosurgiucomumapropostadoGuiceedoSpringparapadro-
nizaçãodeumconjuntosimplesdeanotações.AJSR-330especificouumnovopa-
cote javax.injectcompoucasanotaçõescomunsaseremusadasparaconfigurar
asclassesdousuário,comoa @javax.inject.Injectparausonospontosdeinje-
çãoespalhadospelocódigo.EssaJSRnãoespecifica,porém,comofuncionaofra-
mework,suasconfiguraçõeseoprocessodeDIemsi,masapenasainterfaceentreo
códigodaaplicaçãoeoframework.Foiumpassoimportantíssimoparadiminuiro
acoplamentocomframeworksespecíficos.Emboraaindahajaousodeconfiguraç ão
nocódigo,sãoanotaçõesgenéricas,portáveiseespecificadas.
MasograndepassoparaaplataformaJava,alémdaJSR-330,foiolan çamentodo
CDI – Context and Dependency Injection,aJSR-299,juntocomoJavaEE6.En-
treasváriasfuncionalidadesdessaespecificação,muitasinspiradaspeloJBossSeam,
estáumaferramentacompletadeinje çãodedependênciasparaaplataformaJavaEE.
Anteriormente,noEJB3,algumaspoucasfuncionalidadesdeinje çãoforamadicio-
nadas,demaneiramuitolimitada:apenasalgunstiposeramdisponíveiselimitadosà
injeçãoporsetterouatributo.OCDItrazumaespecificaç ãoàalturadosframeworks
maisconsagrados,integradaàJSR-330edisponívelemtodastackdoJavaEE6.
OmesmocódigodoexemplodeGoogleGuicefuncionarácomCDI,apenastro-
candoopacotedaanotaçãopara javax.inject. NenhumcódigoJavaénecessá-
rio,eumasimplesanotaç ãotrazDIparabeansdoJSF,EJBseatéServletseou-
trosframeworks. OutroexemploquemostraasimplicidadedoCDIéinjetarum
PersistenceContextdaJPAdentrodoDAO,usandofactoriesprodutorasdebeans
comasimplesanotação @Produces:
// o DAO com a configuração do ponto de injeção
public class ProjetoDao {
private final EntityManager manager;
@Inject
public ProjetoDao(EntityManager manager) {
this.manager = manager;
}
// ... restante do DAO ...
90

## Página 111

CasadoCódigo Capítulo4. Separaçãoderesponsabilidades
}
// a classe que produz o bean
public class JPAUtil {
public @Produces EntityManager criaEntityManager() {
// implementação que devolve um novo EntityManager customizado
}
}
Masépossívelatenderacenáriosaindamaiscomplexoscompoucoesfor ço.Ou-
troexemploseriacriardiferentesEntityManagersparadiferentesDAOs,suportando
umcasodeusoemquelógicadadiretoriatemacessoaumbancodedadosrestrito.
Podemosescreverdoismétodosprodutoresediferenciarobeangeradocomum
Qualifier:
// uma anotação de negócio para diferenciar os beans
@Qualifier
@Retention(RetentionPolicy.RUNTIME)
public @interface Diretoria { }
// ::2 produtores, um implicitamente @Default e outro para diretoria::
public class JPAUtil {
public @Produces EntityManager criaEntityManager() {
// ::implementação que devolve um novo EntityManager customizado::
}
public @Produces @Diretoria EntityManager criaEMDiretoria() {
// ::implementação que devolve novo EntityManager com superpoderes::
}
}
// ::DAOs normais continuam recebendo EntityManager normal::
public class ProjetoDao {
private final EntityManager manager;
@Inject
public ProjetoDao(EntityManager manager) {
this.manager = manager;
}
}
91

## Página 112

4.3. ConsidereusarumframeworkdeInje çãodeDependências CasadoCódigo
// a Diretoria recebe o DAO especial
public class RelatoriosSigilososDao {
private final EntityManager manager;
@Inject
public RelatoriosSigilososDao(@Diretoria EntityManager manager) {
this.manager = manager;
}
}
Háaindamuitosoutrosrecursosinteressantes,comosuportea decorators,in-
terceptadoresdemétodos,listenersdeeventos,eatéapossibilidadedeusarversões
alternativasdosbeans,dependendoseoambienteédedesenvolvimento,testesou
produção. Váriosdessesrecursosestãopresentestambémemoutrosframeworks
DI,masoCDItemganhadomuitosadeptosporserumasoluç ãooficialeportá-
vel.E,alémdeserumaespecificação,éextremamentefácil,produtivoecomcódigo
bastantelimpo,muitasvezesmaissimplesatéqueoutrosframeworks.
Outros recursos de containers DI
QuandosepensaemDI,imediatamenteselembradecriaç ãoeinje çãodeob-
jetos.Realmenteéesteofocoprincipal,masretirardedentrodasclassesarespon-
sabilidadedecriaçãodasdependênciasabrecaminhoparadiversosoutrosrecursos
interessantes.
Aprimeiraquestãoasepensarésobrequemseráresponsávelporfinalizaros
objetos. Muitosdelesnãoprecisamsersomentecriados,mastambémfinalizados,
comoaochamarométodo closedeuma Connection.Masdequeméestaresponsa-
bilidadeagora?Quemcriouoobjetocostumaseroresponsávelporsuafinalizaç ão.
Antes,nossoDAOabriaa Connectionetinhaquefechá-la.Agora,eleapenasrecebe
umacriadapelocontainer.Passaaserresponsabilidadedeste,portanto,lidarcoma
finalizaçãoeliberaçãodasdependências.
Todososframeworkscitadosvêmcomrecursosimportantesparaadministraro
ciclo de vidacompletodosobjetosgerenciados.Nãoapenascriareinjetarasdepen-
dências,comotambémsabercomofinalizá-las. NoCDI,porexemplo,aanotação
@Disposespermiteindicarblocosdecódigoparafinalizaçãodoscomponentes.Mas
surgeumaoutraquestão:qualéomomentocertodefinalizardeterminadoobjeto?
E,mesmocomrelaçãoàcriação,quandoinstanciarasdependências? Equantos
92

## Página 113

CasadoCódigo Capítulo4. Separaçãoderesponsabilidades
objetoscriar? Devehaverumaúnica Connectionnaaplicaçãotodaaserinjetada
emtodososDAOs?Oudeveserabertauma Connectioncadavezquealguémpe-
diruma? Ouuma Connectionparacadausuário,independentementedequantos
DAOseleuse?
Quandosefaladeciclodevida,éimportantesaberdeterminaraformadege-
renciamentodecadaobjeto,quandoecomodevesercriado,equandodeveserdes-
truído. Estamosfalandoemdefinirum escopoparaaexistênciadecadaobjeto.
TodososcontainersDImodernossãocontextuaisepermitemaconfiguraç ãodos
escopos. EmumaaplicaçãoWeb,emgeral,usamosescoposassociadosacadare-
quest,àsessãodousuário,ouescopoglobaldaaplicaç ão.NoXMLdoSpring,por
exemplo,usamos scope="request"paraconfigurarqueumcertobeandevesercri-
adoacadarequestedestruídonofinaldarequisiç ão.Ou,noCDI,podemosusara
anotação @SessionScopedparaindicarquecertocomponenteestáassociadoàses-
sãodousuário,eserádestruídoquandoasessãoforinvalidada.
Háoutrosescopos,comoo prototype,doSpring,quecriamumainstâncianova
acadapontodeinje ção,ouoescopoconversacionaldoJBossSeamedoCDI,que
permiteaumobjetoserusadoduranteumasequênciaderequisiçõescomoumwi-
zard,umaconversa.Ou,ainda,noJSFqueencontramoso ViewScope,alémdacapa-
cidadeextremamenteflexíveldoCDIparasedefinirnovosescoposparaaaplicaç ão.
Masosrecursosnãoparamporaí. Comogerenciamentocompletodoci-
clodevidadosobjetosporpartedoscontainers,estesdisponibilizamaindamais
eventosquesomentecriaçãoedestruição.Épossívelconfigurarcallbacks,comoo
@PostConstructeo @PreDestroy,ou,ainda,interceptarexecuçõesdosmétodosde
negóciodosbeans.
Alémdisso,porserumobjetocriadopelocontainereinjetadonasclassessem
elassaberemexatamentecomofoifeitaainstância,muitosframeworksadicionam
recursosespeciaisaosobjetos. Éfácilcriar decoratorsaoredordoobjetoinjetado.
Ou,ainda,injetarum proxyparaoobjetoreal,quepodeadicionarrecursoscomo
aAOPdoSpringedoGuice,ouapoderosainje çãodeobjetosdemenorescopo
encontradanoCDI.Tudoissosemqueaclassequerecebeadependênciaprecise
conhecernadaamaissobreoobjetoinjetado,comacoplamentomínimoeexcelente
extensibilidade.
Eissoparaficarapenasaoredordoserviçodegerenciamentodedependências.
Naprática,muitosoutrosserviçossãooferecidosemconjuntocomoframework,
comonoSpring. Embora,comovimos,DIsejaumaimportantepráticadedesign
epodemosusá-laatécomgerenciamentomanualdedependências,ousodeum
93

## Página 114

4.4. Fábricaseomitodobaixoacoplamento CasadoCódigo
frameworkricoparafazerestegerenciamentoautomáticoémuitorecomendado.
Comrecursosavan çadosjáprontosedeusocadavezmaissimplificado,usarum
containerDIéalgoaserfortementeconsiderado.
4.4 F ábricas e o mito do baixo acoplamento
Umadastécnicasdeorientaçãoaobjetosquemaisfavorecemobaixoacoplamento
éopolimorfismo.Podercriarumainterfacecomumparadiversasimplementações
possíveiseescolheraimplementaçãomaisapropriadaparacadasituaçãosãorecur-
sosbastantepoderosos. Écomoterumsistemagenéricodepagamentosindepen-
dentedaempresadepagamentos:
ServicoPagamentos pgto = new PagamentoViaCielo();
// ::ou:::
ServicoPagamentos pgto = new PagamentoViaRedecard();
Aousarumainterfacecomumparaambososserviços,podemosnosacoplar
somenteàinterfaceetrocaraimplementaç ãosemmaioresesfor ços.Independente
dequalimplementaçãosejausada,teremosomesmocódigodeuso:
pgto.setValor(99.90);
pgto.setCartao("4111 1234 5678 0987");
pgto.efetuaCobranca();
Éexcelentepodermostrocardeimplementaç ãoapenasmudandoumpequeno
pedaçodoprograma,ondedamoso new.Maseseesteserviçoforusadoemvários
lugares?Ou,mesmoquesejaemapenasumlugar,seráresponsabilidadedestesaber
qualempresadepagamentosdeveserusada? Emumexemplodelojavirtual,po-
deríamosterumcomponentedosistemaresponsávelporfinalizarascomprasdos
usuários. Eledevereceberopedido,dispararumaordem,destinadaaoserviçode
estoqueeentregas,eefetuaropagamento:
public class FinalizaCompra {
public void finaliza(Pedido pedido) {
ServicoPagamentos pgto = new PagamentoViaCielo();
pgto.setValor(pedido.getTotal());
pgto.setCartao(pedido.getCliente().getCartao();
pgto.efetuaCobranca();
94

## Página 115

CasadoCódigo Capítulo4. Separaçãoderesponsabilidades
// ... ::outras lógicas::
}
}
Pareceumcódigobastantesimples,masmostraumdosmaiorespontosfracosdo
new:instanciardiretamenteumobjetogeraumacoplamentocomaimplementaç ão
usada.Pormaisóbvioqueissopossaparecer,hágravesconsequências:
• AclasseFinalizaComprapassaaestaracopladacomaimplementaçãoespecí-
ficaPagamentoViaCielo.Seestaclassemudar,porexemplo,parareceberum
argumentoespecialcomumcódigodaCielo,elaquebra.
• Aclasseficacomaresponsabilidadededecidirqualimplementaçãodeveser
usadaparaoserviçodepagamentos. Éumagranderesponsabilidade,algo
quetiraofocodaresponsabilidadeprimáriaqueseriaasimplesfinalizaç ãoda
compra.
• Sehouvermaisdeumaclassenosistemaquepreciseusarumsistemadepa-
gamentos,todasterãoquetomaradecisãodequalimplementaç ãousar.Pode
haverinconsistênciase,mesmoquenãohaja,aresponsabilidadeestariaespa-
lhadapordiversoslugares.
• Acriaçãodoobjetopodeserpotencialmentecomplexa.Talvezsejanecessário
passarargumentoscomplicados,eatéconstruirobjetosauxiliaresparapassar
paranossoserviçodepagamentoescolhido.Deixartodaessaresponsabilidade
namãoda FinalizaCompranãoéumaboaideia.
Asoluçãoparaencapsulararesponsabilidadedecriaç ãodoobjetoespecíficoé
darorigemauma factory.Esseimportanteefamosodesignpattern,aocontráriodo
simplesconstrutor,permitequesejaencapsuladootiporealdoobjetoinstanciadoe,
mais,centralizaadecisãodecriaçãoparaquemudan çasfuturassejammuitosimples.
Alémdisso,seacriaçãodoobjetoexigirparâmetrosouumainicializaç ãocomplexa,
afactorytornatudomaisfácilencapsulandoacomplexidadedousuário.
Usarumafactoryémuitofácil:
public class FinalizaCompra {
public void finaliza(Pedido pedido) {
ServicoPagamentos pgto = Pagamentos.criaServicoPagamentos();
// ... ::restante da lógica::
95

## Página 116

4.4. Fábricaseomitodobaixoacoplamento CasadoCódigo
}
}
Adiminuiçãodoacoplamentoeoencapsulamentosãovisíveis.Hádiversasop-
çõesparacriarumafactory:amaissimpleséummétodoestático,comonoexemplo,
mashávariações,comoumobjetodefábricaoua AbstractFactorycompleta.Mas,
emtodososcasos,asfábricas,emboramelhoresqueosimples new,aindatrazem
diversospontosnegativos:
• Opontomaisdiretoéqueagoraháumacoplamentocomafábricaemsi.Em-
borasejamenospiorqueacoplaràimplementaç ãodocomponente,estamos
acopladosàfábrica,equalquermudan çanelapodequebrarnossocódigo.O
métododefábrica,usualmenteestático,éumpontodeacessoglobalaoobjeto,
eestamosamarrandooprojetotodoaesteponto.
• Seexistiremvárioslugaresnaaplicaçãoqueprecisamdeumserviçodepa-
gamentos,todosnecessitarãochamaressafábrica.Estamosespalhandoares-
ponsabilidadedecriaçãodesteobjetoporvárioslugaresdiferentes.
• Nãoépossívelusarimplementaçõesdiferentesemdiferentespontosdopro-
grama. Secadamódulodosistemaprecisardeumdiferenteserviçodepa-
gamento,precisaríamos,dealgumaforma,indicarparaafábricaqualobjeto
devesercriado.Passarumargumentoàfábrica,indicandoseéCieloouRe-
decard,costumaserasolução,masvoltaoproblemadedeixarparaaclasse
FinalizaCompraadifícilresponsabilidadedeescolheraimplementaç ão.
• Seráqueométodofinalizaéomelhorlugarparasecriaroserviçodepaga-
mentos?Eseprecisarmoscompartilharamesmainstânciacommaisdeuma
classe? Esearegradenegócioexigirquesópodemoscriarumserviçode
pagamentosporusuário? Comodecidiromomentocertodecriaroobjeto
chamandoafábrica? Eseoobjetoexigirumafinalizaç ão,comofecharuma
conexão;dequeméestaresponsabilidade?Éoproblemadedefiniroescopo
dosobjetos.
• A classeFinalizaCompra pode precisar de mais componentes além do
ServicoPagamentos,como ServicoEstoquee ServicoEntrega. Asolução
seriausarfábricasespecíficasparacadacomponente,masissoaumentaainda
maisasresponsabilidadesdanossaclasse,alémde,agora,geraracoplamento
comváriasoutrasclassesdefábrica.
96

## Página 117

CasadoCódigo Capítulo4. Separaçãoderesponsabilidades
Algunsdospontosnegativosdafactorysãosanadospelousodeum ServiceLoca-
torouRegistry.Aideiaédiminuiroproblemadoacoplamentocomdiversasfábricas
diferentes,edeseconhecerpontosdeacessoglobaldistintosparacadadependência.
Teríamosumúnicocomponenteglobalnosistema,cujaresponsabilidadeécentra-
lizaralocalizaçãodetodasasdependênciaspossíveiseproverumpontodeacesso
únicoesimplesparaquaisquercomponentesqueforemnecessáriosemqualquer
partedosistema.
Umadasformasmaiscomunsdesecriarumservicelocatoréproverumúnico
métodoquerecebecomoargumentoqualcomponentesedesejaobter. Istopode
serfeitoatravésdeumnomeemString(comoemJNDI,porexemplo),ouatécom
soluçõesmaiscomplexas,passandoainterfacedesejada:
public class FinalizaCompra {
public void finaliza(Pedido pedido) {
// usando nomes para os componentes
ServicoPagamentos pgto = Locator.get("servico-pagamentos");
// usando a interface
ServicoPagamentos pgto = Locator.get(ServicoPagamentos.class);
}
}
Comoservicelocatorglobal,nãoimportaquantasdependênciasaclassepre-
cisa,épossívelobtertodasapartirdele. Aindatemosumacoplamentoaoservice
locator,maséalgobemmaislevequenasfábricas,jáqueseráumúnicopontode
acessoglobalparatodoosistema.Usandoaversãocomnomesparaoscomponen-
tes,conseguimosaindaresolveroproblemadeusardiferentesimplementaçõesem
diferentespartesdosistema,bastandodarnomesdiferen-tesparaasdependências.
Comalgumesfor çorazoável,épossívelaindaqueoservicelocatorresolvao
problemadoescopodecriaçãodasdependências.Seriapossívelqueeletivesseum
cacheinternoparaguardardependências,quedevemserinstanciadasumaúnica
vezemtodaaaplicaçãoecompartilhadascomtodos.Comumpoucodemágicae
possivelmenteThreadLocal,seriapossívelatéquehouvesseumpequenocachepara
permitircompartilharomesmoobjetodentroapenasdomesmorequest.
Masessasolu çãoaindadeixaalgunspontosemaberto.Pormaisquetenhamos
diminuídooacoplamentocomcoisasexternas,aindatemosoacoplamentocomo
servicelocator.Piorainda, todasasclassesdosistemaestarãoacopladasaele,equal-
quermudançasimplespassaaserextremamentetraumáticaparatodoosistema.Há
aindaoproblemadopontodeacessoglobal.Asclassesprecisamconheceresseponto
97

## Página 118

4.4. Fábricaseomitodobaixoacoplamento CasadoCódigo
deacessoeaindasaberalocalizaç ãoexatadesuasdependências,pormaisencapsu-
ladoqueissoestejadentrodoservicelocator.
Porém,oproblemamaisgraveéque Service Locator não é Inversão de Con-
trole.ComoaaplicaçãoprecisainvocardiretamenteoServiceLocatorparaobtersua
dependência,aaplicaçãotemocontrole.Inje çãodedependênciasresolveosúltimos
problemasaoinverterocontroledocódigoderesoluç ãodedependência,tirandodas
classesdaaplicaçãoaresponsabilidadederesolversuasprópriasdependências.
MartinFowlerdiz[65]queagrandedecisãoésequeremosestaracopladosao
ServiceLocatoremtodaaaplicaç ãoounão. AInversãodeControleremoveesse
acoplamento,maspodetornarmaisdifícilenxergaroqueaaplicaç ãofazexatamente,
eatéseufluxodeexecução.Pordefinição,ficadifícilenxergarquemestánocontrole,
eistopodeeventualmenteserumproblema.
Nogeral,asvantagensdainversãodecontrolesuperamseuspontosnegativos,
porissoseuusoétãorecomendado.ComInje çãodeDependências,nãoháoaco-
plamentoaumpontodeacessoglobal.Nãohánecessidadedeasclassesconhecerem
alocalizaçãodesuasdependências.
UsandoDI,asclassespossuemmenosresponsabilidadesepreocupações,jáque
alguémestaránocontroledogerenciamentodasdependências. Comoainje çãoé
feitaporalguémexterno,suaconfiguraçãoéexternaàclasse,edecidirqualimple-
mentaçãodeveserinjetadaemquallugarnãoémaissuaresponsabilidade. Além
disso,comovimos,asferramentasmodernasdeinje çãodedependênciasconseguem
aindatrazeroutrasvantagens,comocontrolecompletodeciclodevidadasdepen-
dências,incluindosuasfinalizações,escoposbemdefinidos,entreoutras.
Singletons, Factories e os containers de DI
Singletonéumdosdesignpatternscompiorfama. Chegaaserchamadopor
muitosde antipattern. Em2009,duranteumaentrevistaemcomemoraç ãoaos15
anosdolivro DesignPatterns,aoserperguntadosobrequaismudan çasfarianolivro
emumahipotéticarevisão,ErichGammaafirmouquetirariaSingletondele.Mais,
oautoraindaafirmouquesingletonsseriamum designsmell.[151]
Osingleton,àprimeiravista,parecebastantesimpleseinofensivo.Comfrequên-
cia,háanecessidadedesemodelarnaaplicaç ãoarestriçãodeinstânciaúnicapara
certasclasses.Osingletonaparececomoumasoluç ãoeleganteparaimpediracria-
çãoindiscriminadadeinstâncias,controlandooacessoàinstânciaúnicacriadain-
ternamente.Umnomebastantecomumparaométodoqueexpõeainstânciaúnica
égetInstance:
98

## Página 119

CasadoCódigo Capítulo4. Separaçãoderesponsabilidades
public class Configuracoes {
private static final Configuracoes INSTANCE = new Configuracoes();
private Configuracoes(){}
public static Configuracoes getInstance() {
return INSTANCE;
}
public String get(String chave) {
// ... ::implementação::
}
}
Esteexemplorepresentaumaclassequeguardaconfiguraçõesglobaisparaosis-
tema. Éimplementadocomumcódigosimples,quecriaainstâncianoatributoe
disponibilizaumpontodeacessoatravésdométodo getInstance.Háoutraspos-
síveisformasdeimplementar,como,porexemplo,acriaç ão lazydainstância,ou
aindausandouma enumdoJava5,comoolivro EffectiveJavapropõe.
Sejaqualforaformaescolhida,aprimeiraperguntaasecolocarédecunho
bempráticoetécnico: singletonsrealmenteexistem? Averdadeéquearestrição
dainstânciaúnicapodeserfacilmenteburladausandoclassloadersdiferentes.Ou,
ainda,forçandoacriaçãodenovasinstânciascomreflection.Emumambienteclus-
ter,então,aquestãoéquasefilosófica.Comoencararossingletonssehádiferentes
instânciasdaaplicaçãorodandoemdiferentesmáquinas?
Mas,deixandodeladoasquestõestécnicasdecomoburlarumsingleton,o
grandeproblemadessepatternédedesign.Asclassesqueforemdependerdosin-
gletonprecisarãoobterainstânciaúnicaapartirdoseumétodo getInstance,um
pontodeacessoglobalquegeraumacoplamentodetodososusuárioscomalocali-
zaçãodoobjeto:
public class AdicionaAction {
public void execute() {
Configuracoes config = Configuracoes.getInstance();
String dado = config.get("informacoes");
// ...
}
}
99

## Página 120

4.4. Fábricaseomitodobaixoacoplamento CasadoCódigo
Decertaforma,ométodo getInstancepodeserencaradocomoumafábrica
quesempreproduzamesmacoisa,ouumRegistrydeumúnicoobjeto.Háosmes-
mosproblemasdiscutidosanteriormentedeFactoryedeServiceLocator. Hátal-
vezatéumacoplamentomaior,poisemgeralousuáriodosingletonacabasabendo
queaquiloéumsingleton,aindamaispelasemânticaassociadaa getInstance.O
usuárioacabacarregandooconhecimentodequesetratadeumsingleton,ouseja,
acopla-secomumdetalheinternodacriaç ãodeinstânciasdeumaoutraclasse.No
diaemqueaclasse Configuracoesprecisardeixardeserumsingletonepassarater
váriasinstâncias,todoorestantedosistemaseráafetado.
NamesmaentrevistaemquecriticaoSingleton,ErichGammapropõeumnovo
designpattern quepoderiaserincluídonolivro:aInje çãodeDependências,justa-
menteasoluçãoparaosproblemascitados.
public class AdicionaAction {
private final Configuracoes config;
public AdicionaAction(Configuracoes config) {
this.config = config;
}
public void execute() {
String dado = this.config.get("informacoes");
// ...
}
}
Aactionpassaanãomaissaberquesetratadeumsingleton.Seumdiaestefato
mudareváriasinstânciaspassaremasernecessárias,aactionnãosofreráqualquer
alteração. Emais: comoteremosalguémnocontroledasdependênciasecriaç ão
dosobjetos,seriapossívelatéqueaclasse Configuracoesnãofossemaiscodificada
comoumsingleton.Nãoqueanecessidadedeterumainstânciaúnicanãosejavá-
lida,masestapodeseraresponsabilidadedocontainerquegerenciaasdependên-
cias,eaprópriaclasse Configuracoespoderiaterumaresponsabilidadeamenos
aonãoprecisarsepreocuparemcriarecuidardesuainstânciaúnica. Seumdia
foremnecessáriasváriasinstâncias,nemaclasse Configuracoessofreriamodifica-
ções,masapenasocomponentequecontrolaasdependênciassaberiadestefato.
Naverdade,todososcontainersdeDIsuportamqueseconfigurecertocompo-
nente,umasimplesclasse,comoumsingleton,ouseja,umainstânciaúnica.Masé
100

## Página 121

CasadoCódigo Capítulo4. Separaçãoderesponsabilidades
umaconfiguraçãointernaaoframework. NoSpring,porexemplo,épossívelcon-
figurarquequalquerclassedosistemasejaumbeancominstânciaúnicacomparti-
lhada.Bastausaroatributo scopenoXML,indicandojustamenteovalor singleton:
<bean id="configuracoes”class=”br.com.arquiteturajava.di.Configuracoes”scope=”singleton”/>
Ou,n
oPicoContainer,aoadicionarprogramaticamenteumcomponente,pode-
mosindicarqueainstânciacriadadeveserúnicaecompartilhadaportodos:
MutablePicoContainer pico = new DefaultPicoContainer();
pico.as(CACHE).addComponent(Configuracoes.class);
NoJa
vaEE6,umadasmaioresadiçõesaoEJBemsuaversão3.1foio Singleton
Bean. Umasimplesanotação @SingletoninstruiocontainerqueaqueleEJBdeve
terumainstânciaúnicacompartilhadaemtodaaaplicaç ão:
@Singleton
public class Configuracoes {
public String get(String chave) {
// .. implementação
}
}
G
oogleGuice,CDIequalqueroutroframeworkdeDIpossuemrecursospare-
cidos.Naprática,oqueobservamoséqueo Singleton deixa de ser um design pat-
tern implementado em código e evolui para apenas uma configuraç ão dos fra-
mewo
rks de DI parainstruí-losemcomoseráapolíticadecriaç ãodeobjetosde
certa
classe.
EnãoésóosingletonqueencontrouseuespaçodentrodoscontainersdeDI.
Factories,decertaforma,tambémevoluíramparafazerpartedocontainer.Assim
comoamotivaçãodainstânciaúnicadossingletonsaindapodeserválidamesmo
aousarDI,asmotivaçõesdasfábricastambémcontinuamválidas.Estastêmavan-
tagemdeencapsularmuitobemacriaç ãodeobjetoscomplexos,quedemandem
diver
sospassos,algoquepoderiacomplicarotrabalhodeumframeworkautomati-
zado.
No tópico anterior foi possível observar isso no CDI com sua anotação
@Produces.Esserecursonadamaiséqueumaformadeindicaraoframeworkque
determinadocódigoéummétododefábricaparacertotipodedependência,eque
ocontainerdeveinvocá-loparaobternovosobjetossemprequenecessário:
101

## Página 122

4.4. Fábricaseomitodobaixoacoplamento CasadoCódigo
public class JPAUtil {
public @Produces EntityManager criaEntityManager() {
// implementação que devolve um novo EntityManager customizado
}
}
Mas repare que uma aplicaç ão jamais invocaria esse método
criaEntityManagerdiretamente.Fazê-lotrariadevoltaosproblemasdepontode
acessoglobaldasfábricaseoaltoacoplamento.Essemétodoéumafábricaqueserá
invocadasomentepelocontainer. NoSpring,temosomesmoefeitousandoseus
FactoryBeanse,noPico,seus ComponentAdapter.
Noslugaresdaaplicaçãoondefornecessárioum EntityManager,bastadeclarar
adependênciaeocontainercuidarádainvocaçãodafábricainternamente.Éaevo-
luçãodasfábricascomtodasassuasvantagens,masemumcontextodeInje çãode
Dependênciasdebaixoacoplamentoesemacessoglobal.
O Service Locator que há dentro de cada container DI
TodocontainerdeDI,internamente,éumgrandeServiceLocator,umimenso
Registryparanossosobjetos. Épossívelatéencararoframeworkdestaforma. No
Spring,porexemplo,depoisdeconfiguradososbeansnoXML,épossívelobterre-
ferênciasparaobjetosdesejadospelonomeconfigurado:
ApplicationContext container;
container = new FileSystemXmlApplicationContext("spring.xml");
AdicionaProjetoAction action;
action = (AdicionaProjetoAction) container.getBean("adicionaAction");
action.execute();
OcódigoanteriormostracomooSpringfacilitaaobten çãodoobjetodaAction
semsepreocuparseelavaireceberumDAOcomoargumento,ouatéseoDAOtem
umaconexãocomodependência,que,porsuavez,precisadosdadosdeconexão,
usuárioesenha. Todasasdependênciassãoresolvidas,bastaindicaronomedo
beannoXML(adicionaAction )etemosumainstânciaprontaparauso.
ComoPicoContainernãoseriadiferente.Apósconfigurartodasasdependên-
ciasprogramaticamente,comovimosnotópicoanterior,seriapossívelobterasre-
ferênciasdesejadasdiretamentenocontainer.Adiferen çaéquepassamosotipodo
objetonahoradeobtê-lo:
102

## Página 123

CasadoCódigo Capítulo4. Separaçãoderesponsabilidades
PicoContainer container = ....
AdicionaProjetoAction action;
action = container.getComponent(AdicionaProjetoAction.class);
action.execute();
Guice,CDIeoutrosframeworkstêmcódigosemelhante. Sóháumproblema:
estamosusandoumgrandeServiceLocator,enãoInje çãodeDependências. Invocar
diretamente o container de DI na aplicaç ão não é Inversão de Controle, e é uma
má prática.
Pensenaclassequeeventualmenteteriaessecódigodeinvocaç ãodiretaaocon-
tainerparaobteruma AdicionaProjetoAction. Seuobjetivonãoémanipularo
container,mas,sim,obterumobjetodeactionparainvocarseumétodo execute.Se
suaresponsabilidadeéapenasutilizaraaction,poderíamostambémusarInje çãode
Dependênciasnessaclasseefazê-lareceberuma AdicionaProjetoActionnocons-
trutor,semprecisardereferênciaparaocontainerneminvocá-loexplicitamentepara
obtersuadependência.
Masháumaquestãonãoresolvida.InversãodeControlenãosignificafaltade
controle. Alguémprecisaestarnocontrole. MesmousandoumframeworkdeDI,
alguémprecisainiciá-lo,daropassodeinicializaçãoechamarexplicitamenteopri-
meirobean. Éprecisoumcódigoinicial,quenãoseráInversãodeControle,para
queorestantedaaplicaçãoestejacomocontroleinvertido.
EmumaaplicaçãogerenciadaporumcontainerWebouEJB,opróprioservidor
podefazeressepassoinicialdecriarocontainerdeDI,jáqueeleestánocontrole.
UmaaplicaçãoCDIquerodeemumcontainerJavaEE6,porexemplo,nuncapre-
cisaráinvocarqualquercódigodoCDIparainicializarocontainerouinvocaras
dependênciasexplicitamente.ComCDInoservidor,bastajogarasclassesanotadas
corretamentequeoCDIfarátodoocontroledaaplicaç ãoautomaticamente.
Porém,nemsempreaaplicaçãorodaemumambientegerenciadopelocontainer
doservidor.UmaaplicaçãoDesktopnométodo main,porexemplo,teriaqueinici-
alizaroframeworkdeDImanualmente. Estemétodoéocontroleinicialdetoda
aplicaçãoDesktop,e,sequeremosusarInversãodeControlenorestantedaaplica-
ção,seráseupapeldispararocódigomínimonecessárioparacontrolaraaplicaç ão.
Podemosdizerqueserianecessárioescreverumcódigode bootstrapdaaplicação
queiniciaoframeworkecontrolatodoorestantedosistema.Essecódigo,embora
importanteenecessário,nãoéInversãodeControlee,portanto,deveseromenor
103

## Página 124

4.5. Proxiesdinâmicasegeraçãodebytecodes CasadoCódigo
possível,semlógicadenegóciosecomaúnicaresponsabilidadedecontrolaraapli-
cação.
Referenciarocontainernomeiodaaplicaç ãoeinvocarseusbeansdiretamente
éumapéssimaprática,contráriaatudoqueseviudeInversãodeControleeInje ção
deDependências.Aúnicasituaçãojustificávelénosraroscasosemqueprecisamos
escreverumcódigocurtode bootstrapdaaplicação.
4.5 P roxies dinâmicas e geração de bytecodes
OsrecursosdeorientaçãoaobjetoseaAPIbásicadereflectionpodemnãosersu-
ficientesparasepararcódigosdeinfraestruturaededomíniodemaneiracompleta-
mentetransparente.
Considereainvocaçãodeummétododeumobjetoqueestejaemoutramáquina
virtual.Écomumexistirumrepositóriocentraldedados,querealizapesquisaem
umestoquedelivros,parasaberadisponibilidadedestes.Comoacessaressainfor-
maçãosemexporobancodedados?
SenossoservidorestárodandoJava,podehaverumobjetoquerepresentaa
Livrariaepossuimétodosqueprecisamseracessadosapartirdeumaoutramá-
quinavirtual. Umaideiapoderiasercriarumaclasse,quecontrolaoacessoaos
objetosdessaJVMremota,eexecutarosmétodosquedesejarmos:
ClasseControladoraDoServidor.executa("livraria", “buscaAutor”);
Nessaabordagem, ficadifícilpassarparâmetros, receberretornosdiferentes,
alémdenãochecarocorretofuncionamentodachamadaemtempodecompila-
ção,podendosurgirerrosemtempodeexecuç ão.Tambémémuitotrabalhososer
obrigadoacuidardetantainfraestrutura,desdetrabalharcom Socketspurasaté
definirprotocolosegerenciarsituaçõesdefalha.
Seria mais interessante se a aplicação cliente simplesmente tivesse uma re-
ferência a um objeto local, que pudesse ser utilizado para invocar métodos
em um objeto que está na aplicação servidora em outra JVM. Algo como
livraria.buscaAutor("turgueniev").
Parachegaraumasoluçãoelegantecomoesta,inicialmentehánecessidadede
umaclasseparapodertrabalharcomoidentificadordoobjetoremoto,onomedo
métodoaserinvocadoeseusparâmetros. Esse Controladorficaresponsávelpor
repassaressasinformaçõesàmáquinavirtualremota:
104

## Página 125

CasadoCódigo Capítulo4. Separaçãoderesponsabilidades
public class Controlador {
public <T> T invoca(Long id, String metodo, Object... parametros)
throws IOException, ClassNotFoundException {
Socket socket = new Socket("192.168.87.17", 3040);
try {
OutputStream saida = socket.getOutputStream();
InputStream entrada = socket.getInputStream();
ObjectOutputStream writer = new ObjectOutputStream(saida);
writer.writeObject(id);
writer.writeObject(metodo);
writer.writeObject(parametros);
ObjectInputStream reader = new ObjectInputStream(entrada);
return (T) reader.readObject();
} finally {
socket.close();
}
}
}
Dadoqueoclienteconheceoobjetoreferenciadonoservidor,elepodeagora
executarmétodosatravésdessaclassecontroladora:
Object resultado = Controlador.invoca(7, "processaNotasAte", hoje);
Apesardefuncionar,essaabordagemapresentadiversasdesvantagens,alémde
claramentenãoterumtratamentoadequadoaosrecursoscaros,nemumbomtra-
tamentodesuasexce ções. Alémdisso,odesenvolvedorsetornaresponsávelpor
códigodeinfraestruturaquetrabalhacom Sockets,protocolos,exceptionsemuito
mais.Apesarde,nessecaso,nãosertãocomplicadomanterumprotocolobemdefi-
nido,tratarcorretamenteasexceptionsnocasodeoservidorcair,timeoutseoutros
detalhessãoproblemasdeinfraestruturaquelevambastantetempoparaseresolver
corretamente.Ocódigoingênuovairapidamentesemostrarinsuficiente.
Seriamaisinteressanteseaaplicaçãoobtivesseacessoaumasimplesreferência,
quepudesseserutilizadaparainvocarmétodosemumobjetoqueestánaaplicaç ão
servidoraemoutraJVM.Deseja-seinvocarummétodoremotamente:
Double valor = empresa.processaNotasAte(new Date());
Paraisto,épossívelisolarumanovacamadaquedelegaasinvocações,extraindo
umainterfaceeimplementandoaclasse Controlador.Mesmoassim,todososmé-
105

## Página 126

4.5. Proxiesdinâmicasegeraçãodebytecodes CasadoCódigo
todosdaimplementaçãode Empresapassamafazerumsimplespapelde proxy,de-
legandoarequisiçãoparaoservidorremoto.
public interface Empresa {
Double processaNotasAte(Date data);
}
public class EmpresaProxy implements Empresa {
private final Long id;
public EmpresaProxy(Long id) {
this.id = id;
}
public Double processaNotasFiscaisAte(Date data) {
try {
Controlador ctrl = new Controlador();
return (Double) ctrl.invoca(id, "processaNotasAte", data);
} catch(IOException ex) {
throw new RuntimeException("Erro na invocacao remota", ex);
} catch(ClassNotFoundException ex) {
throw new RuntimeException("Erro na invocacao remota", ex);
}
}
}
UmobjetoquepodeserinvocadodeoutraJVMédotiporemoto.Nestecaso,
aAPIpermiteacessá-lodemaneiratransparente,semqueodesenvolvedorquefaz
taisinvocaçõestenhadecodificarmuitodiferentedecomofazcominvocaçõeslo-
cais.Àsvezes,taltransparênciapodetrazerconsequênciasnegativas,comoquando
odesenvolvedorexecutamuitaschamadasremotassemperceberFigura4.2.
Remotabilidadeéumdosaspectosquepodemaparecernumaaplicaçãoedeseja-
segastaromenortempopossívelcomisso.Essesobjetosquefazemopapeldedele-
gadoresderequisiçõesparaumobjetoremotosãoconhecidos,nestecontexto,como
stubsouproxies,atéaquigeradosprogramaticamentepelodesenvolvedor.
Parafacilitarotrabalhoepermitirqueessascaracterísticassejamaplicadasa
diversasclassesdistintas,épossívelutilizarproxiesdinâmicasdoJava.Esteéumre-
cursoquepermitecriar,emtempodeexecuç ão,o bytecodedeumaclasseapenasem
memória,queimplementadeterminadasinterfaces,porém,todainvocaç ãoaesses
objetospassaráporum InvocationHandler.
106

## Página 127

CasadoCódigo Capítulo4. Separaçãoderesponsabilidades
Figura4.2:Aplicaçãousandoumproxyparaacessaroobjetoremoto
public class RemoteProxy implements InvocationHandler {
private final Long id;
private RemoteProxy(Long id) {
this.id = id;
}
public Object invoke(Object proxy, Method m, Object[] args) {
try {
return new Controlador().invoca(id, m.getName(), args);
} catch(IOException ex) {
throw new RuntimeException("Erro na invocação remota", ex);
} catch(ClassNotFoundException ex) {
throw new RuntimeException("Erro na invocação remota", ex);
}
}
}
public class Proxies {
public static <T> T getRemoto(Long id, Class<T> type) {
return (T) Proxy.newProxyInstance(
this.getClass().getClassLoader(),
new Class[] {type},
new RemoteProxy(id));
}
}
107

## Página 128

4.5. Proxiesdinâmicasegeraçãodebytecodes CasadoCódigo
Ficasimplesacessarremotamentequalquerumdosnossosobjetos:
Empresa remoto = Proxies.getRemoto(15L, Empresa.class);
Double valor = remoto.processaNotasAte(new Date());
Comooobjetoreferenciadopelavariável remotofoigeradodinamicamente,o
nomedasuaclasseemtempodeexecuç ãoserá Proxy$N.Estaclasseimplementa
asinterfacespassadascomoargumento, nestecaso, Empresa. Osseusmétodos,
queestãonumbytecodeapenasemmemória,delegamtodasasinvocaçõesparao
InvocationHandlerdado.AFigura4.3ilustraoprocessodeinvocaç ãoaométodo
remotamenteatravésdeumaproxydinâmica.
Ainvocação remoto.processaNotasAte(new Date())sómostraqueéremota
pelonomequefoidadoparaareferênciaàproxy,deixandoaremotabilidadetrans-
parente.Ocódigodo Controladoréinvocadointernamentepelaproxy.Écomum
encontrardiversosframeworks,comooRMIeoHibernate,quevãotirarproveito
dessasproxiesdinâmicas,escondendotodoocódigodifícileexplícitoqueseriane-
cessáriopararealizartaistarefas.Umpontonegativoéexatamenteessatransparên-
cia,quepodefazercomqueodesenvolvedornãoseatenhaaoexcessodeusode
recursoscaros,comoconexõesaobancoeinvocaçõesremotas.
ProxiescriadasatravésdessaAPInãopodemestenderclasses,massomenteim-
plementarinterfaces.Existemalternativasparacontornaresselimite,quevãogerar
bytecodeemtempodeexecução,estendendodeterminadaclasseeatémesmoalte-
randomodificadoresdeacesso,comoo Javassist,cglibouASMFigura4.3.
Figura4.3:Aplicaçãoutilizandooproxydinâmicoparaacessarumobjetoremoto
Apesardeserumrecursopoderoso,amanipulaç ãodebytecodedeveserpon-
108

## Página 129

CasadoCódigo Capítulo4. Separaçãoderesponsabilidades
derada,assimcomoumdesignatravésdeinterfacesépreferívelaousopesadode
reflection. Elavaiserfrequentementeaplicadapordiversosframeworks,quetra-
balhamparaajudarsuainfraestrutura,econheceressacapacidadeajudaaentender
melhoraferramenta,otimizá-laeenfrentarcommaisfacilidadeasestranhasstack
tracesquepodemsurgir.OHibernate,porexemplo,vaiutilizarasproxiesdinâmicas
emanipulaçãodebytecodeparafazerseumecanismodelazyness.
Aprogramaçãoorientadaaaspectos(AOP),queganhouevidêncianocome ço
dosanos2000atravésdoAspectJedoAspectWerkz,costumaserimplementada
atravésdamanipulaçãodebytecode.Hoje,apesardetodaexpectativa,encontra-se
maisnumnichobemespecífico,utilizadointernamenteaoscontainers.OJBoss,por
exemplo,temseumicrokernelbaseadoemseupróprioprojetoJBossAOP.OSpring
tambémofereceumabiblioteca,aSpringAOP,parapoderdefinirseusaspectos.[108]
109

## Página 131

Capítulo5
Testeseautomação
Equipesdedesenvolvimentodesoftwarecomumenteevitamaatividadedetestes,
sejapelajustificativadeumatrasonaentregaoupeloaltocustoderealizá-losde
formamanual. Anãoexecuçãodestaatividadediminuiaqualidadefinaldosoft-
ware,que,namaiorpartedasvezes,apresentaráproblemasdurantesuaoperaç ão,
queserãodedifícildetecçãoecorre ção.
Éimpossívelgarantirqueumsoftwarenãopossuafalhas.Odesenvolvedordeve
asseguraraqualidadedosoftwaree,paraqueissoaconte çademaneirasustentável,
énecessáriocriareautomatizartestes.
Existemmuitosníveisdetestes,ecadaumdelesentregaumtipodefeedback
diferenteparaodesenvolvedor.Otestedesistema,porexemplo,garanteaqualidade
externa,verificandoseafuncionalidadeestádeacordocomorequisitadopelocli-
ente.Jáotestedeunidadeajudaodesenvolvedoragarantiraqualidadeinternado
código,dandofeedbacksobreodesigndosmódulosepermitindoumamanuten ção
commenorcusto.
Estecapítulodiscutetécnicas,vantagensedificuldadesdetestesemdiferentes

## Página 132

5.1. Testesdesistemaeaceitação CasadoCódigo
níveis,bemcomoalternativasparaautomatizá-los.
5.1 T estes de sistema e aceitação
Umsoftwarequefuncioneapenasnamáquinadedesenvolvimentonãoagregavalor
paraocliente.Énecessárioalgumrecursoquegarantaboapartedocorretofunci-
onamentodocódigoequedêaodesenvolvedorofeedbacksobreasversõesdeseu
sistemaemumajaneladetempoaceitável.
Nomercadotradicionaldedesenvolvimento,sãodescritas,emlongosdocumen-
tos,chamadosmanuaisdeteste,bateriasaseremexecutadasmanualmente.Ostestes
queindicamseocomportamentodosistemanãomudouecontinuafuncionando
conformeoesperadosãoostestesqueadicionamvalorparaocliente.
Oprimeiropassonaquebradessaabordagemtradicionaléaautomaç ãodeste
procedimento,pararemovererroshumanos,diminuindootempodefeedbackde
cadamudançaefetuadapelosdesenvolvedores.
Testesqueatravessamosistemainteiro,desdeainterfacecomousuárioatéo
backenddesuaaplicação,sãochamados end-to-end.EmaplicaçõesWeb,sãoaqueles
queutilizamferramentascomoo Seleniumparaacessardiretamente,atravésdeum
navegador,oconteúdodaspáginasdosistema.Comesteresultado,sãoconferidasas
expectativasatravésdasasserções(atravésdeasserteverify).Oexemploaseguir
mostraousodiretodaAPIdo Selenium2:
@Test
public void oProdutoFoiAdicionadoAoCarrinho() throws Exception {
browser.get("http://localhost/produtos/livro_sobre_arquitetura");
// quando o usuário preenche a quantidade
WebElement form = browser.findElement(By.id("produto"));
form.findElement(By.name("produto.quantidade")).sendKeys("2");
// e clica em adicionar();
form.submit();
// então a listagem mostra que o produto foi adicionado
List<WebElement> linhas = browser.findElements(By.tagName(“tr”));
WebElement ultima = linhas.get(linhas.size() - 1);
WebElement produto = ultima.findElements(By.tagName("td")).get(2);
assertThat(produto.getText(), is("Livro sobre arquitetura"));
112

## Página 133

CasadoCódigo Capítulo5. Testeseautomação
WebElement qtd = ultima.findElements(By.tagName("td")).get(3);
assertThat(qtd.getText(), is("2"));
}
Avantagemdestetipodetesteégarantirquenãohaveráumaregressãonasfun-
cionalidadesjáexistentesdosistema,conferindoaapariçãodebugsnocódigo,que
jáfuncionavaconformeoesperado.Bastaumanovaexecuçãodessabateriadetestes
parasabersealgumafuncionalidadepreviamentetestadadeixoudefuncionar.
Apesardessavantagem,essestestessãolentosepassampelopontomaisfrágil
deumaaplicaçãoWeb,ainterfacecomousuário.Qualquermudan çanelacostuma
acarretaraquebradediversostestes end-to-enddeumasóvez,mesmoquandoasre-
grasdenegóciopermanecemcorretas.Aatualizaçãoconstantedessecódigodetestes
écustosaepodeocorreracadamudan çanainterface.Porestemotivo,éimportante
encontraronúmeroidealdetestes end-to-endquegarantaocomportamento,enão
atrapalheamanuten çãoeevoluçãodosistema.
T este de serviços Web
AotestarserviçosWeb,cujainterfaceéumarepresentaç ãoem,porexemplo,
XMLouJSON,emvezdeutilizaro Seleniumparacarregarumnavegador,utiliza-se
umaAPI,comoo Restfulieouo HttpApacheCommons:
public void deveRetornarAsUltimas3Cotacoes() {
adiciona(new Cotacao("PETR4", 30.3));
adiciona(new Cotacao("PETR4", 32.1));
adiciona(new Cotacao("PETR4", 31.3));
String xmlEsperado =
"<cotacoes><cotacao>31.3</cotacao><cotacao>32.1</cotacao>" +
"<cotacao>30.3</cotacao></cotacoes>";
assertThat(
Restfulie.at("http://localhost/cotacoes/PETR4").get().getBody(),
is(equalTo(xmlEsperado)));
}
Apesardenãoexistirumnavegadorouinterfacegráficaenvolvido,essestestes
tambémsãoend-to-end,poisatravessamosistemainteiro.Elesgarantemaqualidade
externaaocódigo,trabalhandocomserviçosWeb,sejaatravésdeSOAP,POXou
REST.
113

## Página 134

5.1. Testesdesistemaeaceitação CasadoCódigo
T estes de aceitação
Quandoostestessãoescritosdemaneiraadescreverocomportamentodosis-
tema,tambémsãoutilizadosparagarantirqueesteúltimoestejadeacordocomos
requisitoslevantadosjuntoaocliente.[143]Essetipodeteste,principalmenteemXP,
échamadodetestesdeaceitação(acceptancetests,outestesdeaceite).
Portanto,nemsempreessestestesdeaceitaç ãoprecisampassarportodoosis-
tema,enemtodosprecisamser end-to-end. Comonocasodeadotaro Selenium
somenteparagarantiraintegraçãoentreainterfacedousuárioeo frontcontroller,
semvalidaralógicadenegóciosportrás.Porexemplo,emumsistemadecompra
on-line,umtestevalidaqueainterfacerespondecomooesperado,semgarantirque
acomprasejarealmenteefetuada.Istoé,asasser çõesnãoverificamoresultadodessa
operaçãocomológicadenegócio(suasconsequênciasdentrodosistema).Essere-
sultadodenegóciosjáestácobertoporoutrabateriadetestes,deaceitaç ão.
FerramentascomoCucumbereoJBehavesãoótimasparacriartestesdeacei-
tação,mas,segundoalgunsautores,nãodeveriamserusadasparatestarlógicade
negóciosatravésdaUI.[128]Umtestedeaceitaçãoqueutilizataisferramentas,mas
semacessarainterface,consisteemgarantirtodososfluxosdecompra,diminuindo
seucustodemanuten ção.
Deacordocomalegibilidadedocódigoescrito,otestedeaceitaç ãopodeatéser
encaradocomoumaformadedocumentaç ão.Oexemploaseguirutilizamétodos
auxiliares,aumentandoaexpressividadeefacilitandosualeitura:
@Test
public void mostraQueOProdutoFoiAdicionadoAUmCarrinhoDeCompras() {
Carrinho carrinho = aoAcessarOProduto("livro_sobre_java")
.escolher(2).eAdicionarNoCarrinho();
Item adicionado = carrinho.getUltimaLinha();
assertThat(adicionado.getProduto(), is(equalTo("Livro de Java"));
assertThat(adicionado.getQuantidade(), is(equalTo(2));
}
Ostestesdeaceitaçãogarantemqueocomportamentoseráomesmoqueoes-
peradopelocliente,dandoseguran çaparaumapossívelentregadosoftware.
T estando os limites do sistema
Requisitosnãofuncionaistambémpodemsergarantidosatravésdetestesauto-
matizados,comoquandoemumsistemaénecessárioqueotempoderespostapara
114

## Página 135

CasadoCódigo Capítulo5. Testeseautomação
determinadasrequisiçõeslevenomáximo4segundos,comumamédiade2segun-
dos.Testesdeperformancepodemserescritosatravésdeferramentassimples,como
clientesHTTP,abouJMeter.Aotestarosservidoresdeproduç ãoousimilarescom
umacargaequivalenteacenáriosconsideradosextremos(testedecarga),épossível
validaroutrorequisitonãofuncional: aescalabilidade. Levandoemconsideraç ão
asduasvariáveis,temosdadosquepermitemanalisaraperformanceemfun çãodo
númerodeacessossimultâneos.Aautomatizaçãodessestestesgarantiráofeedback
rápidosobreaqualidadenessesrequisitosnãofuncionais.
Testesexecutadospeloserhumano,queadicionamsurpresasnoroteiro,explo-
randocasosparticulares(cornercases)quenãoforamvislumbradospelosdesenvol-
vedoressãochamadosdetestesdeexploraç ãoeelescontinuamimportantes.Uma
falhapercebidaporumtestedeexploraçãopodeserrapidamenteautomatizadaatra-
vésdacriaçãodeumnovotestedeaceitaç ão.
5.2 T este de unidade, TDD e design de código
Todosostestesservemcomogarantiaderegressão,umavezque,qualquermudan ça
quequebreoscomportamentosesperados,serádescobertaaoexecutá-los.Masnem
todosostestessãofeitoscomestefim.Testesmenorespodemverificarocompor-
tamentodepequenaspartesdocódigo,tipicamenteumaclasseouummétodo,cha-
mados,nestecontexto,deunidade.
Umtestedeunidade devegarantirqueaexecuç ãodaqueletrechomínimode
códigoestejacorreta.Paraisso,verifica-seoretornodeumainvocaç ão,ainteração
dotrechocomoutraspartesdosistemaouoestadodoobjeto.Noexemploaseguir,a
classeVendaéutilizadaparacalcularoimpostoaserpagoemumavenda,enquanto
seutesteverificademaneiraisoladaseométodo getImpostofuncionaconformeo
esperado.
public class Venda {
private final Produto[] produtos;
public Venda(Produto... produtos) {
this.produtos = produtos;
}
public double getImposto() {
double imposto = 0;
for (Produto produto : produtos) {
115

## Página 136

5.2. Testedeunidade,TDDedesigndecódigo CasadoCódigo
imposto += produto.getPreco() * 0.1;
}
return imposto;
}
}
public class VendaTest {
@Test
public void deveCalcularDezPorcentoSobreOPrecoDosProdutos() {
Produto livro = new Produto("Arquitetura e Design", 100);
Produto computador = new Produto("Notebook", 2000);
double imposto = new Venda(livro, computador).getImposto();
assertEquals(210.0, imposto, 0.001);
}
}
Verificaroretornodeumainvocaçãopodeserfeitocomumasimplesasser ção,
masconferirainteraçãoentrecomponentespodeserdifícil,dependendododesign
dassuasclasses.
OexemploaseguirmostraumcontroladorWebqueacessaabasededadospara
agendarumareunião,utilizandoaabordagemtradicionaldecriarprimeiroocódigo
edepoisoteste:
public class ClienteController {
public String agenda(long id, Calendar horario) {
Cliente cliente = ClienteDao.getInstance().busca(id);
Reuniao reuniao = new Reuniao(cliente, horario);
ReuniaoDao.getInstance().cria(reuniao);
return "sucesso";
}
}
Apesardefuncionalecorreto,ocódigoanteriorapresentaumaltoacoplamento
comasclasses ReuniaoDaoe ClienteDao. Eletambémpossuibaixacoesãoaose
preocupartantocomaregradenegóciosquantocomdetalhesdaconversãode long
para Cliente. Aocriarumtesteisoladoparaeste controller,encontra-sealgumas
barreiras:
public class ClienteControllerTest {
@Test
public void deveSalvarReuniaoComOsDadosDoCliente() {
116

## Página 137

CasadoCódigo Capítulo5. Testeseautomação
Calendar horario = Calendar.getInstance();
ClienteController cliente = new ClienteController();
assertEquals("sucesso", cliente.agenda(15, horario));
}
}
Otesteanteriorpodefuncionar,masnãodemaneiraisolada. Ainvocaç ãoao
métodoagendaimplicaachamadaabuscaecria,métodospertencentesaoutras
classes.Alémdisso,faltaaverificaçãodecomotaismétodosforamexecutadoscor-
retamente,umavezqueotestesógarantiuoretorno.
Paratestaressecódigoporcompleto,énecessáriofazerasser çõesemoutraspar-
tesdocódigo. Issoindicaqueháumpossívelexcessodeacoplamentocomsuas
dependências.Nãoépossíveltestá-locomoumaunidade.Parasistemaslegadose
semtestes,ocódigoaseguiréumprimeiropassodeumprocessoaceitável,maso
próximoseriaodarefatoração,visandoadiminuiçãodoacoplamento.
public class ClienteControllerTest {
@Test
public void deveSalvarReuniaoComOsDadosDoCliente() {
Calendar horario = Calendar.getInstance();
ClienteController cliente = new ClienteController();
assertEquals("sucesso", cliente.agenda(15, horario));
Cliente cliente = ClienteDao.getInstance().busca(15);
Reuniao reuniao = ReuniaoDao.getInstance().buscaUltima();
assertEquals(cliente, reuniao.getCliente());
}
}
Parapossibilitaraescritadotestedemaneiraisolada,oprimeiropassoétornar
explícitasasdependênciasdeumaclasse,recebendo-asdealgumamaneira,con-
formeosprincípiosdeinje çãodedependênciasedo GoodCitizen[146]Paraisso,é
necessárioremoverainvocaçãodiretaaométodo getInstance.
public class ClienteController {
private final ClienteDao clientes;
private final ReuniaoDao reunioes;
public ClienteController(ClienteDao clientes, ReuniaoDao reunioes){
this.clientes = clientes;
117

## Página 138

5.2. Testedeunidade,TDDedesigndecódigo CasadoCódigo
this.reunioes = reunioes;
}
public String agenda(long id, Calendar horario) {
Reuniao reuniao = new Reuniao(clientes.busca(id), horario);
reunioes.cria(reuniao);
return "sucesso";
}
}
Recebendotaisdependências,elaspodemserfacilmentetrocadasduranteaexe-
cuçãodoteste:
public class ClienteControllerTest {
@Test
public void deveSalvarReuniaoComOsDadosDoCliente() {
ClienteDao clientes = mock(ClienteDao.class);
ReuniaoDao reunioes = mock(ReuniaoDao.class);
Cliente cliente = new Cliente();
when(clientes.busca(15)).thenReturn(cliente);
Calendar horario = Calendar.getInstance();
ClienteController controller =
new ClienteController(clientes, reunioes);
assertEquals("sucesso", controller.agenda(15, horario));
verify(reunioes.cria(new Reuniao(cliente, horario)));
}
}
Otesteanteriorcriaum ClienteControllerepassainstânciasde ClienteDaoe
deReuniaoDao.Mas,destavez,osobjetossãooutros;nãosãoimplementaçõescon-
cretasdaquelasclasses,esimobjetosquesimulamocomportamentodasmesmas.
Estesobjetossãochamados mocks.Assim,éfinalmentepossíveltestarocontrolador
semainterferênciadorestodosistema.
Essarefatoraçãodiminuiuoacoplamentodaclasse ClienteControllercomos
DAOs,tirandoaresponsabilidadedegerenciarociclodevidadasdependências.
Ocontroladoragoranãodependedeumaimplementaç ãoconcretadosDAOs,mas
118

## Página 139

CasadoCódigo Capítulo5. Testeseautomação
apenasdainterfacepúblicadosmesmos.Oacoplamentoébemmenoremaisexplí-
cito.
TantoClienteDaoquantoReuniaoDaopoderiamsertransformadoseminterfa-
ces(extractinterface),maisestáveisqueclassesconcretas,conformevistonocapítulo
sobreorientaçãoaobjetos;assim,todocódigoetestesquedependemdelassofreriam
menosmudanças,tornando-osmaisgerenciáveis.Comasinterfaces,ocontrolador
permitiriaquequalquerimplementaçãofosseutilizada,removendooacoplamento
diretoàsimplementaçõesdosDAOs.
Seo design possui alto acoplamento, será praticamente impossível testar seu
código através de testes de unidade[78].Porestemesmomotivo,métodosestáticos
eestadoglobaldificultamostestesdeunidade,assimcomotodotipodebuscaexplí-
citaporumadependênciaaumentaoacoplamento(singletonsoufactoriesatravés
demétodosestáticosenewindiscriminados).
Umavantagemdostestesdeunidadesobreoutrostiposéque,alémdegarantir
queantigosbugsnãoserepitamnofuturo,elesdãofeedbacksobreoacoplamentoe
acoesãodocódigo.Masrecebertalfeedbackapenasapósescrevermuitaslinhasde
códigodosistemapodesertarde,pois,nessemomento,arefatoraç ãoeamelhoria
dodesignpodemserdifíceiseapresentarumcustomaiscaro.
Oriscoemtestardepois,istoé,criarprimeiroafuncionalidadeesóentãooteste,
éserinfluenciadopelovíciodamentedodesenvolvedorapósaescritadocódigo.
Nestasituação,otesteéescritoparacomprovarqueaquiloquefoidesenvolvidoestá
deacordocomoqueoprogramadorentendeu.Seafuncionalidadefoiimplemen-
tadademaneiraerrada,écomumqueotestetambémesteja. Aoinvésdegarantir
queocódigofuncionaadequadamente,elegarantequeumbugcontinuasendoum
bug,enquantodáasensaçãodequeestáfuncionando. Éfáciltambémdeixarsem
testesalgunsdospossíveiscaminhosqueocódigopodeseguir,comonãotestaruma
condição elseouuma exception.
Atéesteinstante,acriaçãodostestesfoifeitaapósaimplementaç ãodeumafun-
cionalidade.Invertendoaordem,ouseja,escrevendoprimeiroocódigodetestee
depoisaimplementação(test-first),recebe-sefeedbackconstantesobreodesigndo
sistema,alémdetornarobrigatóriaaexistênciadepelomenosumtesteparacada
funcionalidade.Destaforma,umdesenvolvedoratentosepoliciaparaimplementar
somenteaquiloqueseutesteprecisaparapassar.
Emumalógicadenegóciossimples,queenvolvedoispossíveiscaminhos(if e
else),essaabordagemobrigaodesenvolvedoraescreverumtesteparacadauma
dasduassituações.
119

## Página 140

5.2. Testedeunidade,TDDedesigndecódigo CasadoCódigo
Umaconsequênciadaexistênciadetestesparatodasasfuncionalidadeséaalta
coberturadocódigo(codecoverage). Elaservecomométricaparaindicarqueas
partescombaixacoberturaprecisamseranalisadascomcautelaquantoaoseufun-
cionamento.Masaexistênciadeumtestenãogarantequeelefuncionecorretamente,
comovistonocasodostestesescritosapósaimplementaç ão,ou,ainda,quandoo
desenvolvedortestaerroneamenteumafuncionalidade. AFigura5.1mostraparte
dorelatóriodecoberturadeumprojeto.
Umtestedescrevecomoocódigoseráutilizado.Quantomaiscomplicadoocó-
digodeumteste,maisproblemáticoestáodesignadotado.Porexemplo,umteste
querequerdiversasinicializaçõesdedependênciasindicaumaltoacoplamento,en-
quantoseeleenvolvemuitasverificaçõesdistintas,hápossíveisproblemasdecoesão.
Figura5.1:Exemploderelatóriodecoberturadelinhasebranches.
Éfundamentalqueodesenvolvedordomineboaspráticasdedesignparaque
sejacapazdeinterpretarofeedbackdeumteste.Antesdeescreveraimplementaç ão
deumafuncionalidade,acriaçãodeumtestedáliberdadeparaqueodesenvolvedor
escrevaoqueacreditaserumbomdesign,semsepreocuparcomosdetalhesde
implementação.
SuponhaqueumaaplicaçãoWebtenhaanecessidadedefinalizarumavenda
apartirdeumpedidojáfeitopelousuário,atravésdagravaç ãonobancodeum
pedido,formadoporprodutoepre ço.Alémdisso,énecessáriotambémenviaruma
mensagemparaoutrosistemaqueseráresponsávelpeloenviodoprodutoparao
clienteediminuiraquantidadedoprodutonoestoque.
Criandootesteprimeiroéobtidoumcódigodesejadodeexecuç ão:
public class VendasTest {
120

## Página 141

CasadoCódigo Capítulo5. Testeseautomação
@Test
public void deveFinalizarVendaSalvandoEnviandoEDiminuindoEstoque(){
VendaDao dao = mock(VendaDao.class);
Estoque estoque = mock(Estoque.class);
ClienteHttp httpClient = mock(ClienteHttp.class);
Endereco destino = new Endereco("Rua Vergueiro 3185, SP");
Produto livro = new Produto("Arquitetura e Design", 100);
Produto computador = new Produto("Notebook", 2000);
Pedido pedido = new Pedido(destino, livro, computador);
Vendas vendas = new Vendas(dao, estoque, httpClient);
Venda venda = vendas.vende(pedido);
// salvar a venda
verify(dao.salva(venda));
// diminuir do estoque os produtos da venda
verify(estoque.diminui(venda.getProdutos()));
// enviar a venda para outro sistema
String xml = new XStream().toXml(venda);
verify(httpClient.post(xml)));
}
}
Nãoháproblemasnaexistênciademaisdeumassertpormétododeteste,desde
quetodosestejamgarantindoumúnicocomportamento.Entretanto,otesteacima
indicaqueaabordagemlevariaaumaclasseVendasquepossuidiversasresponsa-
bilidades;alémdecriaresalvarumaVenda,elatambéméresponsávelpordiminuir
oestoque,serializá-laeenviá-laparaooutrosistema.
Ocustoderefatoraraclasse Vendasaindaébaixo,jáqueaclassenãoexiste.Um
desenvolvedoratentoperceberiaafalhadedesignaoescreveressenomedométodo
deteste.Tantaspalavrasnonomedeummétodo,aindamaisconcatenadascom“es”,
indicamquehámuitasresponsabilidades. Refatorá-loatémesmoantesdaimple-
mentaçãoseriaumpassofundamentalparaaumentaracoesãodessaclasse.
Ocódigodetestecome çaaindicarquehámuitospassosenvolvidosemumpro-
cessodevenda,equedeveserinteressantequebrarasresponsabilidadesdessaclasse
Vendasempequenasclassese,depois,juntá-lasnovamente.Aprincipalresponsabi-
lidadedestaclasseégerarumaVendapropriamentedita.Orestopodesercomposto
nela,atravésdeobservers[80],analogamenteàdiscussãosobrecomposiçãonocapí-
tulosobreOO.
121

## Página 142

5.2. Testedeunidade,TDDedesigndecódigo CasadoCódigo
Ométodovendepassaráaterumaúnicaresponsabilidade,adegeraravenda
baseadanopedido.Apósessarefatoração,oseguinteconjuntodetesteséobtido:
public class VendasTest {
// método auxiliar para gerar um pedido
private Pedido umPedido() {
Endereco destino = new Endereco("Rua Vergueiro 3185, SP");
Produto livro = new Produto("Arquitetura e Design" , 100);
Produto computador = new Produto("Notebook" , 2000);
return new Pedido(destino, livro, computador);
}
@Test
public void deveGerarUmaVenda() {
Vendas vendas = new Vendas();
Venda venda = vendas.vende(umPedido());
assertEquals(2100.0, venda.getTotal(), 0.00001);
}
}
Aimplementaçãodométodo vendeparaotesteanteriorébemsimples:
public class Vendas {
public Venda vende(Pedido pedido) {
return geraVendaAPartirDe(pedido);
}
private Venda geraVendaAPartirDe(Pedido pedido) {
// gera uma venda baseada nas regras de negócio
}
}
Agoraqueavendajáfoigerada,énecessárioadicionaralgunspassosdeum
processo.Casotaiscomportamentosfossemimplementadosdentrodestaclasse,o
resultadoseriaabaixacoesão. Portanto,quandoaplicável,quebra-seocomporta-
mentoemdiversospassos.Aclasse Processofuncionacomoumalistade Passos:
122

## Página 143

CasadoCódigo Capítulo5. Testeseautomação
public interface Passo {
void processa(Venda venda);
}
public class Processo implements Iterable<Passo> {
private final List<Passo> passos;
public Processo(Passo... passos) {
this.passos = Arrays.asList(passos);
}
public Iterator<Passo> iterator() {
return passos.iterator();
}
}
Aclasse Vendasnotificaráalistadospróximospassosaseremexecutadoscom
a Vendarecém-criada. Énecessárioadicionarumtestequegarantatalcomporta-
mento:
@Test
public void devePassarAVendaGeradaPorTodoOProcessoDeVenda() {
Passo passo1 = mock(Passo.class);
Passo passo2 = mock(Passo.class);
Processo processo = new Processo(passo1, passo2);
Vendas vendas = new Vendas(processo);
Venda venda = vendas.vende(umPedido());
verify(passo1.processa(venda));
verify(passo2.processa(venda));
}
Reparenovamentenobaixoacoplamento: aimplementaçãodaclasse Vendas
nãosabequaisserãoospassosexecutados.
public class Vendas {
private final Processo processo;
public Vendas(Processo processo) {
123

## Página 144

5.2. Testedeunidade,TDDedesigndecódigo CasadoCódigo
this.processo = processo;
}
public Venda vende(Pedido pedido) {
Venda venda = geraVendaAPartirDe(pedido);
for (Passo passo : this.processo) {
passo.processa(venda);
}
return venda;
}
private Venda geraVendaAPartirDe(Pedido pedido) {
// gera uma venda baseada nas regras de negócio
}
}
Acriaçãodospassossegueosdetalhesnecessáriosparacadatrechodelógica,
sendoquecadaresponsabilidadequeodesenvolvedorjulgarsuficientementedesco-
nexadasoutrasterásuaprópriaclasse:
public class SalvaVenda implements Passo {
private final VendaDao dao;
public SalvaVenda(VendaDao dao) {
this.dao = dao;
}
public void processa(Venda venda) {
this.dao.salva(venda);
}
}
public class ReduzEstoque implements Passo { ... }
public class EnviaVendaParaOutroSistema implements Passo { ... }
Odesignfinaloferecemaiorcoesãoemenoracoplamento,atravésdaado çãode
conceitosdeinje çãodedependênciasecomposiçãodecomportamentosatravésde
124

## Página 145

CasadoCódigo Capítulo5. Testeseautomação
umacadeiadepassosaseremseguidos. Asoluç ãoapresentadaacimaéumadas
possíveismaneirasderesolveroproblemadebaixacoesão,ecabeaodesenvolvedor
encontraramaisadequadaaoseuproblema.
Abordagenscomoestautilizamtambémapráticadepassostãopequenosquanto
façamsentido,masnãonecessariamenteomenordetodos(omenordetodosécha-
madobabystep),paraajudarodesenvolvedoranãopularpassos.
Percebaqueostestesdeunidadeeofeedbackconstantequeelesdãosobreo
designguiaramoprogramadornodesenhodasclassesacima,diferentedofeedback
fornecidopelostestes end-to-end.Oprocessodeescrevertestesantesdaimplemen-
taçãoeusarofeedbackdelesparaguiaroprocessoéconhecidopor Test-DrivenDe-
velopment(TDD)[15]. Esseimpactonodesignétãograndequemuitosutilizama
siglaTDDpara Test-DrivenDesign[7](Figura5.2).
Odesigndaclasseemergedecomoodesenvolvedordesejautilizá-la.Dependerá
doconhecimentododesenvolvedoraescolhadospadrõeseboaspráticasaserem
aplicados. Noexemploanterior,odesignfugiudemodelosanêmico[61],adotouo
usodeumrepositório[30]einje çãodedependênciasatravésdoconstrutor.
TDDéumaferramenta,esozinhanãogaranteresultado,maspermitealcan çá-lo
quandoemconjuntocomoutraspráticas.Testesajudamnodesignmostrandoba-
sicamenteosproblemasaoprogramador;umtestecomplicadodemaiséumindício
depossíveisfalhasdessedesign[78][127].Umcódigofácildetestartendeaapresen-
tarumbomdesign.MichaelFeatherspossuiumaexcelentefrasequeresumeaideia:
“Existeumagrandesinergiaentretestabilidadeeumbomdesign"[58].
125

## Página 146

5.3. Testandoaintegraçãoentresistemas CasadoCódigo
Figura5.2:Oprocessodetest-first,implementaçãoerefatoração
Testarocomportamentoéachavedostestes,quedevemsomentevalidaroes-
perado,enãocomooresultadoesperadoéatingido. Aocriarostestes,executa-se
umaaçãoegarante-sequeocomportamentodaquelaunidadeoufuncionalidadeem
questãoéoesperado.
Aideiadeescreverostestesdeunidadeantesdaimplementaç ãoétãointeres-
santequepodeserestendidaparaostestesdesistema.Atécnica,conhecidacomo
AcceptanceTest-DrivenDevelopment(ouATDD),sugerequeoprogramadorcriepri-
meiroumtestedesistemaantesdecome çaraimplementação.Elagarantequetoda
equipetenhaomesmoentendimentosobreoquedeveserfeito,jáqueostestesde
aceitaçãosãodefinidosantesmesmodeiniciaraimplementaç ão.
5.3 T estando a integração entre sistemas
Énecessáriogarantirtambémqueacomunicaçãoentrecomponentesinternosda
aplicaçãoeoutrossistemasfuncione,como,porexemplo,umacamadadeDAOque
acessaumbancodedados. Enquantoostestes end-to-endtestamumaaplicação
inteiraetestesdeunidade,ocomportamentoisolado,osdeintegraç ão(integration
tests)verificamumapartedapilhadeexecuç ão.
DAOscomumenterecebemum EntityManagerousimilaremseuconstrutor,e
outilizamparaenviarstatementsparaumbanco.Aocome çarpeloteste,épossível
utilizarmocksparaverificarseaqueryesperadaépassadaparaomanager,comono
126

## Página 147

CasadoCódigo Capítulo5. Testeseautomação
exemploaseguir;umDAOchamado ClienteDao,quepossuiráummétodorespon-
sávelporretornaroscincoclientesincluídosmaisrecentementeequeestãomarca-
doscomoimportantes:
@Test
public void deveBuscarOsCincoMaisRecentesEImportantes() {
EntityManager manager = mock(EntityManager.class);
Query query = mock(Query.class);
List<Cliente> resultados = new ArrayList<Cliente>();
String jpql = "select from Cliente where importante=true " +
"order by dataDeCriacao";
when(manager.createQuery(jpql)).thenReturn(query);
when(query.setMaxResults(5)).thenReturn(query);
when(query.list()).thenReturn(resultados);
ClienteDao dao = new ClienteDao(manager);
List<Cliente> clientes = dao.cincoMaisRecentesEImportantes();
assertThat(clientes, is(equalTo(resultados)));
}
Apóscriadooteste,adiciona-seométodonoDAO,masotesteverificaseos
métodosdeEntityManagereQuerysãoinvocados;portanto,aimplementaçãoserá
baseadanestainformação,comosexatosparâmetrosesperados.
public class ClienteDao {
private final EntityManager manager;
public ClienteDao(EntityManager manager) {
this.manager = manager;
}
public void adiciona(Cliente cliente) {
manager.persist(cliente);
}
public List<Cliente> cincoMaisRecentesEImportantes() {
String jpql = "select from Cliente where importante=true "
+ "order by dataDeCriacao asc";
return manager
.createQuery(jpql)
.setMaxResults(5).list();
127

## Página 148

5.3. Testandoaintegraçãoentresistemas CasadoCódigo
}
public List<Cliente> todos() {
return manager.createQuery("from Cliente").list();
}
}
Aodizerqueométododevebuscarcincoclientesetestarsomenteseuma String
épassadaparaumoutrométodo,opróprionomedotesteindicaaodesenvolvedor
queexistealgodeerrado.Nãoestásendotestadoseocódigobuscaosclientes,mas
simseelepassaumparâmetro.
Quantomaisotesteseassemelhaaocódigocriado,maisasasser çõesvalidama
implementação,emvezdoresultadoesperadodocomportamento.Casoodesenvol-
vedortenhaescritoa Stringdeumamaneirasintaxicamenteválida,masretornando
resultadosincorretos,aimplementaçãocostumaserfeitacomamesma String,eo
testepassaaserummerovalidadordequeoqueodesenvolvedorescreveunaim-
plementaçãoéomesmoqueesperavadigitar,nãoadicionandovaloràbateria.
Noexemploanterior,odesenvolvedorpensouemcomoseráimplementadoo
comportamentoenquantoescreviaoteste,antesdaimplementaç ão,cometendoum
erroaoutilizara Stringasc,emvezdedesc.Nestecenário,odesenvolvedoréindu-
zidoausarnaimplementaçãoamesma Stringdoteste.Comoelenãosepreocupou
emverificaraordem,massomentea String,esteerrofoipropagadoparaaimple-
mentação.Aotestarprimeiro,éimportantepensarnocomportamentoesperado,e
nãonaimplementação,paraevitarsituaçõescomoesta,emquea Stringutilizada
notestenãogaranteocomportamentocorretodafuncionalidade.
Paraevitartestesinúteisquesomenterefletemaquiloquefoidigitadoemcom-
ponentesqueenvolvemainteraçãocomoutrossistemas,énecessárioverificarque
ocomportamentodaunidadesejaoesperado.Ocódigoaseguirdemonstracomo
verificaressaintegração:
public class ClienteDaoTest {
private EntityManagerFactory factory;
private EntityManager manager;
private ClienteDao clienteDao;
@Before
public void setUp() {
factory = Persistence.createEntityManagerFactory("teste");
128

## Página 149

CasadoCódigo Capítulo5. Testeseautomação
manager = factory.createEntityManager();
clienteDao = new ClienteDao(manager);
manager.getTransaction().begin();
}
@After
public void tearDown() {
manager.getTransaction().close();
manager.close();
factory.close();
}
private cliente clienteImportante() {
Cliente cliente = new Cliente();
cliente.setImportante(true);
return manager.persist(cliente);
}
return cliente;
@Test
public void deveBuscarOsCincoMaisRecentesEImportantes() {
List<Cliente> esperados = new ArrayList<Cliente>();
for (int i = 0; i < 5; i++) {
esperados.add(clienteImportante());
}
// esperamos o mais recente primeiro
Collections.reverse(esperados);
List<Cliente> importantes =
clienteDao.cincoMaisRecentesEImportantes();
assertThat(importantes, is(equalTo(esperados)));
}
}
Aimplementaçãoda JPAjáfoitestadapeloseufornecedor,masotestefeitoaqui
nãoéparagarantirofuncionamento,porexemplo,da:;JPA como MySQL,massim
queaquerycriadadentroda Stringfoifeitadetalmaneiraquecorrespondeàlógica
denegóciosquedesejamosalcan çar.Umdospontosfundamentaisdaimportânciade
taltesteestánofatodequea Stringdaquerypossui branches::,fluxosdistintos,de
lógica.Ferramentasdecoberturadecódigonãodetectamessesdetalhes,eentendem
queaqueryéuma Stringcomooutraqualquer.Porém,elapossuidiversasregras
129

## Página 150

5.4. Feedbackatravésdeintegraçãocontínua CasadoCódigo
embutidasquepodemtersidoescritasdemaneiraerrada;portanto,otestepara
verificarqueaquerynãodevolvenadaalémdoesperadoéfundamental.
Umtestedeintegraçãobastantediscutidodizrespeitoaométodoadicionades-
critoanteriormente.Eledelegaumarequisiç ãoparaomanagere,àprimeiravista,
pareceserdesnecessáriotestá-la.Casonãohajaumtestequepassepelaintegraç ão
comoutrosistemaeodesenvolvedoranotaraclasse Clientedemaneirainválida,
usandoumtipodecampoquenãoésuportadonobancoescolhido,ostestesretor-
narãoumafalsasensaçãodequeaconfiguraçãoestáválidaedequeosistemaestá
consistente,quandonarealidadenãoestá.
OstestesdeintegraçãodevemtocaraAPIqueacessaossistemasexternos.Estes
podemserumacópiadosistemadeproduçãoouumaversãomaissimples,comoum
grandemockouambientedeteste,maséimportantequeelesecomporteexatamente
comoosistemarealaoqualseráfeitaaintegraç ãoquandoemprodução.
5.4 Feedback através de integração contínua
Éarriscadorecolher,somentenodiadaentrega,informaçõessobreumnovobug,
devidoàmudan çaempartedocódigo. Énecessárioqueestainformaç ãoapare ça
rapidamenteparaodesenvolvedorresponsável.Entregarfuncionalidadesfrequen-
tementepermitereceberumfeedbackrápidosobreosucessooufalhadecadamu-
dançanoprojeto.
Étambémimportantedescobrirrapidamentequeumafuncionalidadenovanão
atendeàsnecessidadesdoclientecomoeleimaginavanomomentodesuaconcep ção,
seénecessárioumaalteraçãoouatémesmosuaremo ção.
Acriaçãodeumsoftwareébaseadanaexploraç ãodaspossibilidadesdeimple-
mentaçãoqueeleforneceparaocliente,eoúnicomomentoemqueelepodeter
certezasobreumcaminhoescolhidoéduranteseuuso.Tudoissorequerfeedback
rápidoecontínuodenossasmudan çasnabasedecódigo.
Quantomaistardioofeedbackrecebidopelosdesenvolvedoresarespeitodeum
bugoufuncionalidadequenãoatingeoobjetivo,maisdifícillembraroque,comoe
osmotivospelosquaisfoitomadaumadecisãonodesenvolvimentoqueresultouno
mesmo.Quantomaistempoosdesenvolvedoresmantiveremsuasalteraçõesnabase
decódigoemsuaprópriamáquina,semenviá-lasaoservidordecontroledeversão
(versioncontrolsystem)paraintegrá-lasaocódigodeseuscolegas,maisdevagarserá
ofeedbackdesuasdecisões.Integrarfrequentementeminimizaotamanhodos mer-
gesquedevemserfeitos,alémdepermitirreceberfeedbackomaisrápidopossível.
130

## Página 151

CasadoCódigo Capítulo5. Testeseautomação
Paraisto,devemosintegrarasalterações,feitassemprequejulgarrazoável–oqueé
umconceitosubjetivo–,mas,quantomaiscedo,melhor.
Omercadotemadotadocommitslocaisminimais,queenvolvempassospeque-
nosdedecisão,comoumarefatoraçãosimpleseintegraçãodocódigocomocontrole
deversãoassimqueumafuncionalidadeécompletada,ouumbugcorrigido.Pode-
selevarmaisaoextremo,efetuandoaintegraç ãosemprequealgoéalteradoenão
quebranenhumafuncionalidadepreexistente. Integrarnessafrequência,sempree
omaisrápidopossível,tentandominimizarainfluênciadejanelaslongasseminte-
gração,échamadointegraçãocontínua(continuousintegration).
Éimportantequeamaiorpartepossíveldostestessejaexecutadaacadacommit,
paraqueainformaçãodoimpactodasalteraçõesnabasedecódigovenharapida-
mente,permitindoaodesenvolvedoragirdemaneiraadequadaparacorrigirfalhase
bugsquepossamterseintroduzido.JamesShore,emseulivrosobrediversaspráticas
deXP[173],cita10minutoscomoumtempobomparatalretornodeinformaç ão.
Nossaexperiênciaindicaqueessetempovariaentrecadaprojeto,equipeemo-
mentodoseudesenvolvimento. Quantomaisbaixomelhor,masénecessário,ao
mesmotempo,escolherumconjuntodetestesquegarantamumfeedbackdequali-
dadeenãodemoremaisdoqueodesejado.
Oprocessointeiro,desdeacompilaçãoatéodeploy,podeserquebradoemdi-
versasfases,descritoemum buildpipeline (Figura5.3). Umexemplode pipeline
envolveafaseinicialdecompilaçãoeverificaçãodemétricasdequalidade;depois,a
execuçãodetestesdeunidade;terminandocomumaterceirafaseautomáticadetes-
tesend-to-end.Apartirdesteinstante,essepipelinepoderiacontinuarsuaexecuç ão
atravésdeumcliquequeindicaodeploypara homologaçãoouprodução.
Figura5.3:Possívelrepresentaçãodeumbuildpipelinecom5etapas.
131

## Página 152

5.4. Feedbackatravésdeintegraçãocontínua CasadoCódigo
Integração contínua e branches
Umaalternativaàintegraçãocontínuaéacriaçãodeumbranchparacadafunci-
onalidadequeestásendodesenvolvida(featurebranches).Durantetodootempoem
quecadabranchviveseparado,aintegraç ãodeixadesercontínua,eofeedbackque
osdesenvolvedoresrecebemsobresuasalteraçõesnabasedecódigosetornacada
vezmaislento,alémdosproblemasde mergeinerentesalongosbranches.
Emoutrasituação,quandoextremamentenecessárioexecutarocommitdeuma
funcionalidadeparcial,asfuncionalidadespodemsermantidastodasdentrodeum
únicobranchatravésdetécnicas,comoadeconfiguraçõesqueasativamoudesa-
tivam(featuretoggle),ou,ainda,op çõesemtempodecompilaçãoqueremovemou
adicionampartesaosistema[178][179].EvanBottchercitaqueacriaç ãodediversos
branchesparalelosvaicontraapropriedadecoletivadocódigo,umavezqueequipes,
trabalhandoemisolamento,nãocompartilhamoconhecimentodotrabalhoexecu-
tado.Umavezqueoprocessodemergeseriamaispenoso,osdesenvolvedorespo-
demacabarporevitarrealizarrefatorações,resultandoemumdébitotécnicomaior
emrelaçãoaodesigndaaplicação.[22]
Aadoçãodeumsistemadecontroledeversão,aintegraç ãocontínua,commits
minimalistas,mergespequenoseIDEscomfuncionalidadesinteligentesderefato-
raçãosãoferramentasquepermitemaodesenvolvedorefetuarmudan çasnabasede
códigosemmedodepossíveisconsequênciasnegativas,pois,comofeedbackrápido,
evita-seenviaralgumcódigoquenãofuncioneparaumsistemaemproduç ão.
Build automatizado
Existemdiversasferramentasde buildautomatizado,quefacilitamoprocessode
execuçãodeseustestes,umavezquesigamosoconceitodeintegraç ãocontínua.
oDentreelas,destacam-seoCruise.rb(esuasvariações,comooCruiseControl)
eJenkins,antigoHudson,comcódigoopensource,enquantooCruiseeoTeamCity
sãoexemplosdeprodutospagos. JamesShorecitaque,paraconfiguraroprojeto
pararodarnamáquinadebuild,devemosautomatizaroprocessodeconfiguraç ão
atravésdescripts[173]. Aprópriamáquinadebuildtambémpodeserconfigurada
atravésdescripts,facilitandoacriaçãodediversasmáquinasdebuildepossibilitando
distribuí-lo.
Quandooprojetocresce,gargalosnotempodeexecuç ãodobuildsurgem,po-
dendopassardeumlimiteaceitável.Épossívelparalelizaraexecuç ãodobuild,dis-
tribuindooprocessoentrediversasmáquinas.Poucosservidoresdebuildsuportam
132

## Página 153

CasadoCódigo Capítulo5. Testeseautomação
nativamentedistribuiregerenciarastarefas.Oobjetivodeparalelizarpartesdopro-
cessoentrediversasmáquinaséfazercomqueofeedbackparaosdesenvolvedores
sejarecebidomaisrapidamente,mesmoemprojetosgrandes.
OdesafioaoadotaraspráticasdetestesautomatizadoseoprocessodeTDD
éencontrarumaescolhadeumconjuntodetiposdetestesdistintosqueajudeno
processodedesigndoseucódigo,maximizeasgarantiasderegressãoeocorreto
funcionamento,alémdeminimizarotempodefeedback.
Entrega contínua
Paraentregarfuncionalidadesaoclienteénecessáriocolocaroprodutoemum
sistemadeprodução,umprocessochamado::deploy:;.Épossívelencontraraplica-
çõesondeeleétotalmentemanual,suscetíveladiversostiposdefalhahumana.As
abordagensfrequentementeencontradasenvolvemaexistênciadeumúnicorespon-
sávelpelodeploy,queutilizaumarquivodetextoondeestãodescritosospassosa
seremexecutados.
Emcasosmaisgraves,oroteiroéseguidoporalguémquenãotemvínculoal-
gumcomoprojeto,somenteatarefadesegui-lo,sementenderofuncionamentoda
aplicação. Issopodeacarretarumgraveaumentodecusto,jáquepossíveisfalhas
parciaisnoprocessodedeploypodemdeixarosdadosouaaplicaç ãoemumestado
inconsistente.Nessecaso,somenteosdesenvolvedoresseriamcapazesdeentender
omotivoeasconsequênciasdeseprolongaressasituaç ãopormuitotempo,impli-
candomaioresfor çohumanoparacorrigi-los.Essetipodedeploycostumaserfeito
àssextas-feirasànoite,comumafrequênciabaixíssima,tentandoevitarospicosde
acessoaossistemaseminimizarpossíveisproblemas,mas,mesmoassim,pordiver-
sasvezesosdesenvolvedoressãoacionadosparapassarofimdesemanacorrigindo
umdeployfalho.
Diminuirointervaloentreentregas,criandoumprocessodeentregacontínua
(continuousdelivery,ou,ainda,entregafrequente)[101][177]éfundamentalparame-
lhoraraqualidadedoprodutodesenvolvido.Paraentregarfrequentemente,éneces-
sárioqueoprocessodedeploynãoimpliquecustosaltos,como,porexemplo,ode
sereshumanosinterpretaremarquivosquedescrevemoprocessodedeploy.Porse-
remexecutadoscommaiorfrequência,énecessárioquetomempoucotempode
execuçãoeexijampoucaounenhumainteraç ãohumana,permitindoquequalquer
umosexecuteeefetuecorre çõesmaiscedonoprocessodedesenvolvimentodosoft-
ware.
Paraminimizaroserrosdoprocessodedeploy,astarefas,cujaresponsabilidade
133

## Página 154

5.4. Feedbackatravésdeintegraçãocontínua CasadoCódigo
eradeumserhumano,devemseragoraautomatizadas.Todaexecuç ãodelinhade
código,cópiadearquivo,back-updosdadosemudan çasdeschemadobancode
dados,entreoutros,devemserexecutadosatravésdescripts.
Sãoinúmerososprojetoscujoprocessoenvolvesomenteacópiadeartefatose
arquivosdeconfiguraçãodistintosparaoambientedeproduç ão. E,emtaiscasos,
automatiza-secomacriaçãodescripts,invocandocomandosdetransferênciade
arquivoscomoscpousftp,queserãorecebidospeloservidorecolocados“noar”.
Opçõesemoutraslinguages,comoRuby,sãoautilizaç ãodeferramentas,comoo
capistrano,quepossuemfocoemautomatizaçãodetarefasemsi.Oexemploaseguir
mostraumscriptque,antesdeexecutarodeploydeumarquivo war,extraiumback-
updobancodedadosedaversãoatualemproduç ãodaaplicação.
#!/bin/sh
if [ -f version ]; then
DUMPVERSION=`cat version`
else
DUMPVERSION=0
fi
DUMPVERSION=$((DUMPVERSION + 1))
echo “$DUMPVERSION” > version
mysqldump -u usuario -p senha sistema > snapshots/dump_$DUMPVERSION
cp webapps/application.war snapshots/application_$DUMPVERSION
cp latest_application.war webapps/application.war
bin/restart.sh
Processosdedeploymaiscomplexosenvolvem,porexemplo,amigraç ãodees-
truturasdeumbancodedadosrelacional,acriaç ãodenovosíndicesdebusca,a
atualizaçãodedadosagrupadoresparciais,utilizadospararelatóriosde businessinte-
ligence:;,epodemserautomatizadoscomferramentasespecíficasquepermitemacon-
figuraçãodeumprocessodedeploy( deploypipeline::),comocomscriptsantjunto
comsuastasksparadeployemservidoresdeaplicaç ão[214],oubuildscompleta-
mentecontroladospelomaven.
Ferramentasespecializadaspermitemqueequipesdedesenvolvimentoeopera-
çõestrabalhemmaispróximas,gerenciandoaconfiguraçãodesistemasoperacionais
esoftwares(configurationmanagement )[101]. Essegerenciamentopodeseralcan-
çadocomferramentascomoPuppet,ChefeCFEngine,criandoscriptsquedeclaram
comodeveserfeitaaconfiguraçãodeumconjuntodemáquinas,desdeseusistema
134

## Página 155

CasadoCódigo Capítulo5. Testeseautomação
operacional,passandopelosservidoresdeaplicaç ão,loadbalancers,etc.,tentando
aproximaroprocessodedesenvolvimento,aentregaeaoperaç ãodesoftware.[152]
UmaaplicaçãoWebtípicapodedeclararemsuaconfiguraç ãoalgumsoftware
paraloadbalancing.Este,porsuavez,éconfiguradoparaapontarparaasmáquinas
comservidoresWeb,comoApachehttps,JettyouGlassfish.EoservidorWeb,por
suavez,apontaparamáquinascombancosdedadosquerodamMySQLououtros.
Todaessaconfiguraçãofoifeitapelomesmoscript.
Todasessasreceitasdevemserguardadascomcontroledeversão.Dessaforma,
aqualquerinstante,umdesenvolvedorpodereplicarqualquerversãohistóricado
sistemaemumconjuntoseparadodemáquinas. Eainda,restaurandoumbackup
dobancodedados,podesimularbugsqueaconteceramemversõesespecíficasdo
sistema.
Adotandotalprática,épossívelreplicaroambientedeproduçãocomumcusto
muitobaixo;bastaexecutaroscriptparaquesejacriadoumnovoambientedeho-
mologaçãomaispróximoaodeproduç ão,ajudandoaencontrarbugsmaiscedo.
Ambientesdedesenvolvimentotambémpodemserautomatizadosdamesmama-
neira,umprocessoqueajudaquandoasequipespossuemaltarotatividadedede-
senvolvedores.
Parapermitiraexecucãodeumdeployempoucosminutosatravésdeumúnico
clique,automatiza-setudooqueforpossível,facilitandoaentregarápidadecor-
reçõesefuncionalidadesaceitas.Alcan çaramaturidadedeentregacontínuanãoé
trivial,principalmenteemprojetosqueenvolvemmigraç ãodedadosouintegração
edependênciasentresistemas.Aabordagemdeimplementaçãodetaispráticasdeve
seramesmadequalqueroutratecnologia;umpassoporvez,adiciona-seumanova
fasenoprocessodebuildedeployeaguarda-seatéaequipeseadaptaràmudan ça
noritmodetrabalhoparaadicionarumnovo.
Voltaratrásemumaentrega,oprocessode rollbackdeumdeploy,tambémé
automatizado,utilizandopráticassimples,comoback-uperestauraç ão,ou,ainda,
técnicasdebluegreendeployment [76]parapermitiracoexistênciatemporáriaem
produçãodediversasversõesdeumsoftware.OambientedoGoogleAppEngine,
porexemplo,permiteatrocadaversãoemproduç ãocomapenasumclique,dado
queambasasversõesjáestãoimplantadas.Essesrollbackssãoaindamaiscompli-
cadosdeseimplementar,enovamenteaequipedevepesarobenefíciodaprática
contraanecessidade. Aexperiênciaindicaque,aomaturarastécnicasdeentrega
contínua,opróximopassoéinvestirtempodedesenvolvimentotécniconorollback,
massóconfiarnelenoinstanteemquefortestadoemoutrasmáquinaseoefeitoal-
135

## Página 156

5.4. Feedbackatravésdeintegraçãocontínua CasadoCódigo
cançadoforoesperado.Oscriptaseguiréumexemplosimplesdesuportearollback
deaplicaçõesWeb,baseadonoscriptdedeploymostradoanteriormente.
#!/bin/sh
ROLLBACK=$1
if [ -f version ]; then
DUMPVERSION=`cat version`
else
DUMPVERSION=0
fi
DUMPVERSION=$((DUMPVERSION + 1))
echo “$DUMPVERSION” > version
mysqldump -u usuario -p senha sistema \
> snapshots/dump_for_rollback_$DUMPVERSION
cp snapshots/application_$ROLLBACK latest_application.war
mysql -u usuario -p senha -e “drop database sistema;”
mysql -u usuario -p senha < snapshots/dump_$DUMPVERSION
deploy.sh
Todaessafacilidadededeploytrazumcustoparaaequipedeinfraestrutura
eoperações,queprecisaestarpreparadaparaenfrentarproblemasmenores,mas
possivelmentecommaisfrequência,nocasodaexistênciadeumaquantidadegrande
dedeploys.Deve-seencontrarumbalan çoentreosdois.Comopassardotempo,o
processodedeployautomatizadocontornamuitosdospossíveiserros,minimizando
anecessidadedeatuaçãohumanaaoaconteceralgumafalha.
Emaplicaçõeslegadas,écomumverumdébitotécnicomuitograndenopro-
cessodedeploy,comumentelembradoporsuabaixaqualidadeefinsdesemanas
perdidos.Aado çãodessaspráticaséumcaminholongo,queenvolvecustos,e,por-
tanto,umprocessoquedeveseradotadoaospoucos.
Porfim,adotarlongosintervalosentrecadaumadasentregasdesoftwareleva
aoacúmulodefalhasaseremdetectadasposteriormente,alémdeasinterpretações
erradasdosrequisitosrefor çaremumasituaçãocadavezmaisdifícildesercontor-
nada.
136

## Página 157

CasadoCódigo Capítulo5. Testeseautomação
Nãoentregarsoftwaredemaneiracontínuaéumagrandedesvantagemcom-
petitiva. Todootempoemqueumafuncionalidadenãoestánoaréumganhoàs
empresasconcorrentesemrelaçãoaoprodutodesenvolvido. AFigura5.4ilustraa
diferençadecustosentreempresasqueentregamounãosoftwaredemaneiracontí-
nua:
Figura5.4:Entregarcedofacilitaoprocessodecorre çãodasfuncionalidadesquenão
atendemaocliente.
Diversasboaspráticasabordamoprocessodecriaç ãoemanuten çãonoambi-
entedosdesenvolvedores,deixandodeladooúltimotrechoasercaminhadopelo
softwareafimdeserutilizadopelosclientes:odeployeaconfiguraç ãodeoutrosam-
bientes. Aspráticasenvolvidascomoprocessodeintegraçãocontínua,testescom
intençãodecapturarerrosprecocemente,feedbackfrequenteeentregacontínuafo-
camaresoluçãodosproblemasenvolvidosnestaúltimaetapadepré-utilizaç ãodo
software.
Todasessaspráticaspermitemacriaçãodetestesnosquaisduasversõesdeuma
partedosistemasãoapresentadasaocliente(chamadasde testesa/b).Otesteveri-
ficaoretornodecadavariaçãodosistemaparadoisgruposdistintosdeusuáriose,
apósdeterminadoperíododetempo,toma-seadecisãodequaldasduasficaráem
produção,emgeralaqueproduzmaiorretornofinanceiro.
137

## Página 159

Capítulo6
Decisõesarquiteturais
Comovimos,arquiteturapodeserdefinidacomoumapossívelinterpretaç ãodaim-
plementaçãodosistema. Équandoolhamosparaaaplicaç ãoparaobservarcomo
diferentespartesdosistemaafetam-seentresi.Essavisãomaisglobaltraz,porém,
diversosdesafioseindagaçõesquedemandamdecisõesdifíceisquepodemsignificar
osucessoouofracassodoprojeto.
Quandousarremotabilidadeeaplicaçõesdistribuídas?Comoescolheramelhor
abordagemWebentreframeworks component-basedeaction-based? Ondeusar–
eondenãousar–umatecnologiademapeamentoobjetorelacional?Emquemo-
mentoadotarumarquiteturadecomunicaçãoassíncrona?Equaisassituaçõesonde
usarcloudcomputingpodeseramelhorideia?
Esseseoutrosquestionamentossãoimportantes decisões arquiteturaisqueen-
frentamosdiariamentenosmaisdiversosprojetos.

## Página 160

6.1. Dividindoemcamadas:tierselayers CasadoCódigo
6.1 D ividindo em camadas: tiers e layers
Eminglês,duaspalavrassãocomumenteusadasaosefalardedivisãodecamadas:
tierelayer.Emportuguês,porém,acabamostraduzindoambascomo camada,per-
dendoaimportantediferen çaentreessestermosedificultandoacomunicaç ão.
Aofalarem layers,normalmentepensa-seemseparaçõeslógicas,emcomoor-
ganizarocódigodaaplicaçãodemaneiraadiminuiroacoplamentoefacilitarmu-
danças. MVC,porexemplo,éumpadrãodedivisãode layersbastanteusado. O
Domain-DrivenDesignpropõeoutradivisãoemquatro layers,comdestaquees-
pecialparaa DomainLayer. Mashámaisdivisõesde layerspropostasporoutros
autores.[67]Oimportanteépromoveradiminuiçãodoacoplamentoentrediferen-
tespartesdocódigoeevitarquemudan çasemumlugarafetemoutros.
Jáadivisãoem tiersvisaaseparaçõesfísicasentrepartesdosistema. Embora
nocenárioatualdevirtualizaçãoecloudcomputingsejacadavezmaiscomplicado
definircomexatidãobarreirasfísicas,deummodogeralcaracterizamos tiersdife-
rentescomocomponentesdosistemaquerodamoupoderiamfacilmenterodarem
máquinasseparadas.OservidorWebéconsideradoum tier,eobancodedados,ou-
tro,assimcomooclienteremoto,umservidordeaplicaç ão,umcachedistribuídoe
outrosexemplos.Emgeral,caracterizam-secomo tiersdiferentesdoiscomponentes
daarquiteturaquesecomuniquemremotamenteviarede.
Usarlayersemexcessopodegerarcódigodedifícilmanuten ção. E,emre-
lação atiersdemais, quando não há uma real necessidade, pode trazer efeitos
catastróficos.[90],[158]Otradeofféclaro: adicionar tierspodeajudaremdiversos
aspectos,masaumentaraquantidadedeinvocaçõesremotas,quesãocarasecom-
plicadas,podeimpactarsignificativamenteaperformanceeaescalabilidade.Fowler
dizparareduzirmosaomáximoadistribuiçãodeobjetos,[63]eestaéamesmaopi-
niãodeoutrosautores.[13]
Arquiteturasdeapenasum tiereramcomunsantigamentenosmainframesque
centralizavamtodooprocessamento,persistênciaeinterfacedoprograma. Outro
exemplo,cadavezmaisextintoemaplicaçõescorporativas,sãoosprogramasDesk-
toppuramentelocais.Certamente,usarapenasum tiertemavantagemdediminuir
alatênciaemelhoraraperformance,jáquenãoháanecessidadedeefetuarrequisi-
çõesnaredeparabuscarinformações.
Poroutrolado,aescalabilidadeécomprometida,umavezquenãoépossívelque
umnúmeroarbitráriodeusuárioscompartilheaaplicação.Arquiteturascentraliza-
dastêmtambémsériosproblemasdedisponibilidade,jáqueháumúnicoponto
140

## Página 161

CasadoCódigo Capítulo6. Decisõesarquiteturais
simplesdefalha.Poressesmotivos,arquiteturasdedois tierstornaram-semaisco-
muns.
OexemploclássicodestasarquiteturassãoasaplicaçõesDesktopconectadasa
umbancodedadoscentral,quesetornarambastantecomunsemaplicaçõesDelphi
eVisualBasic(Figura6.1).
Figura6.1:Clienteseumservidor.
Émuitocomum,ainda,o tierdeinterfacepossuirbastantecódigorelacionado
aodomínio.Sãoos fatclients,aliviandooservidordedeterminadastarefasquepo-
demserexecutadasnocliente. Asdesvantagensprincipaisnessaabordagemsãoo
processamentomaisintensonoclienteeadificuldadedemanterintegridade,con-
fiabilidadeeseguran ça.Pensandonisso,umavariaçãobastantecomumémantera
lógicadenegócioem storedproceduresnobancodedados,comoobjetivodedei-
xaralógicaseguraeencapsulada,alémdeminimizaraperdadeperformancepela
adiçãodemaisum tier. Usarstoredprocedure talvezsejaessencialemumaarqui-
teturadedois tiersporcausadeseguran çaeperformance,mastrazosproblemas
dedependênciadobancodedados,dificuldadedeintegraç ãoepoucaseparaçãode
responsabilidades(Figura6.2).
Háaindaoproblemadopontosimplesdefalhanobancodedadoscentral.Mas,
emborasuaquedapossacausarindisponibilidadeemtodososclientes,porserum
141

## Página 162

6.1. Dividindoemcamadas:tierselayers CasadoCódigo
fatclient,aindaépossívelofereceralgumafuncionalidadeoff-line. Jáaescalabili-
dadenessetipodearquiteturaestácondicionadaàcapacidadedobancocentral,
aindamaisporquemuitasvezesoclientepodemanterumaconexãoconstantemente
aberta.Emborasejaumasoluçãobarata,essetipodearquiteturatemforteslimita-
çõesdeescalabilidadeedisponibilidade.
Figura6.2:Fatclientacessandoprocedimentosmantidosnobanco.
Umoutroproblemaenfrentadopelasarquiteturasdois tierséadificuldadeem
mantertodososclientesatualizados,prejudicandoaextensibilidade,amanutenibi-
lidadeeatéaseguran ça.Hátecnologiasqueminimizamesseproblema,comoo Java
WebStart,queforneceumaplataformasimplesparaainstalaç ãoemanuten çãodas
versõesdeumamesmaaplicaç ãoJavadesktop.Masasoluç ãodefinitivapareceter
vindocomalargaado çãodaWebcomoplataformaparaasaplicações.
NaarquiteturaWebtradicional,temostrêstiers:oclienteremoto,oservidorWeb
eobancodedados.Oclienteé,emgeral,umnavegadorWebqueapenasrenderiza
ainterface;nãocostumaterprocessamentoelógicadodomínioquenãosejamre-
lacionadosàvisualizaçãodosdados. Esses thinclients trazemaimensavantagem
desempreacessaremaúltimaversãodisponíveldaaplicaç ão,centralizandoaevo-
luçãodosistemanoservidorWebebancodedados,trazendomaiorfacilidadede
142

## Página 163

CasadoCódigo Capítulo6. Decisõesarquiteturais
atualização(Figura6.3).
Outravantagemdestetipodearquiteturaéaseguran çaeconfiabilidade,jáque
osistemaacabacentralizadono tierWeb,minimizandoapossibilidadedeclientes
maliciososprejudicaremseufuncionamento. Masaperformancecostumaserum
grandeproblema. Adicionarumnovo tier,aindamaisWeb,acabaaumentandoo
response-time,umareclamaçãoconstantedosusuáriosquevivenciamumamigração
doDesktopparaWeb.
Figura6.3:Clientesmagrosatravésdeumnavegadoreumservidor.
Comoobjetivodemelhoraraperformanceparaousuário,observamosavolta
dosfatclientsnaformadeinterfacesricasnonavegador,as RichInternetApplications
(RIA).AprópriaplataformaJavainvestenessetipodeabordagemdesdeoiníciocom
osAppletse,maisrecentemente,comJavaFX,maspodemoscitartambémFlash,
Flex,Silverlighteoutroscomcaracterísticassemelhantes.Masessasabordagenssão
dependentesdetecnologiasexternasaonavegadoreoquemaissevêatualmenteé
ousodopróprionavegador,paraasinterfacesricas,baseadasfortementeemJavaS-
cript,AjaxeatéHTML5.Algumastecnologiasvãoalém,comooSocket.IO,utilizam
WebSocketscomfallbackparaFlash,casooprimeironãoestejadisponívelnaquele
browser.OfuturodasaplicaçõesWebéaevoluçãodonavegadorparasuportarin-
terfacescadavezmaisricas,masmantendoasvantagensdeumaarquiteturadefácil
143

## Página 164

6.1. Dividindoemcamadas:tierselayers CasadoCódigo
gerenciamento.
Aotrabalharcomtrêstiers,deixadefazersentidomantertodooprocessamento
notierquearmazenaosdados,poisointermediárioseriaapenascomoumaponte.
Nessaabordagem,asantigas storedproceduresperdemimportânciaepassamaser
substituídasporlógicadenegócioexecutadano tierintermediário,obusinesstier.
Nestecenário,oclientefazasrequisiçõesaoservidorqueexecutaalógicaedelegaa
manipulaçãodosdadosparaobancodedados(Figura6.4).
Figura6.4:Clientemagroacessandoprocessosarmazenadosnoservidor.
Aindaháproblemascomdisponibilidadeeescalabilidadeseapenasumservidor
Webeumbancodedadosestãoativos.Usandoliteralmenteapenastrês tiersédi-
fícilcontornarestetipodeproblema,porissoécomumadicionaroutroselementos
comoreplicaçãoem clusters,loadbalancers eoutros tiers. Écostumechamareste
tipodesoluçãocomo N-tiers,umavariaçãodostrês tierscommaiscomponentes
pararesolverproblemasdeescalabilidade,disponibilidadeeoutros.
Hádiversosexemplosdenovos tiersadicionadosàsaplicações,comoservidores
deaplicaçãoseparadosdoservidorWeb,cachesdistribuídos,servidoresdemensa-
geriaetc.Emgeral,háumimpactonaperformancepelaadiç ãodenovos tiers,mas
commelhorasignificativaemescalabilidade,porhaverapossibilidadedeseadicio-
nartantasmáquinasquantasforemnecessárias,edisponibilidade,pornãohaverum
pontosimplesdefalha(Figura6.5).
144

## Página 165

CasadoCódigo Capítulo6. Decisõesarquiteturais
Estetipodearquiteturatemtambémseuspontosnegativos,comoacomplexi-
dadecriadaeadificuldadedegerenciamentoemanuten çãodetodaainfraestrutura.
Háquestõesaseremresolvidasnomododereplicaç ãodosservidoresseaaplicaç ão
tiverestado,alémdecuidadosparticularescomobancodedados.Poressesmoti-
vos,muitosprojetosfogemdacomplexidadedo N-tierssenãoháumrequisitomuito
fortedeescalabilidadeedisponibilidade.
Figura6.5:Trêstierscomdiversasmáquinasatendendoàsrequisições.
Otimização na comunicaç ão entre tiers
AMicrosoftdizparaevitaraumentaronúmerode tiers,[13]assimcomoapri-
meiraleideMartinFowler.[64],[63]Independentementedeemquantos tierssua
aplicaçãoestádividida,énecessáriotomarprecauções. Sãotrêsospontosprinci-
145

## Página 166

6.1. Dividindoemcamadas:tierselayers CasadoCódigo
pais.
Oprimeiroéaquantidadedeinvocaçõesparaooutro tier(númeroderound-
trips). Seoclientefezumaúnicarequisiç ão,épéssimogerardiversasrequisições
internasentreos tiersdaaplicação.Oidealéqueessenúmerode roundtripsseja1,
ounomáximoumaconstantepequena.Algunsframeworkspodemfacilmentegerar
umaquantidadeproporcionalaonúmerodeentidadesqueestãosendomanipula-
das,tornando-seumgargaloenormeparaaescalabilidadedeaplicaç ão.
Osegundoéotamanhodainformaç ãotransmitida(payload ). Quantomaior
oJSON,aentidadeserializadaemXML,maisrecursosserãoconsumidos. Nesse
instante,sugemos DataTransferObjects(DTO) paraadequaragranularidadedo
serviço,almejandoumúnicoroundtrip.Oexcessodeheadersemmensagenscurtas
tambémpodeserumasobrecarga.
Oterceiroéocache,essencialparapoderatémesmoevitarumarequisiç ãopara
ooutro tier,desonerandomuitoaaplicação(Figura6.6).
Figura6.6: Evitarcomunicaçãoremota,diminuirosdadostransferidoseefetuar
cachedasinformações.
Reparequeessassãopraticamenteasmesmasrecomendaçõesdadasporumad-
ministradordebancodedados:minimizaraschamadas,tentandopegartodainfor-
maçãonecessáriaemumaúnicaquery,eaomesmotempobuscarapenasosdados
necessários.Sepossível,cachearoresultado.Acomunicaç ãodo tierdeapresenta-
çãodeveterosmesmoscuidados;entreosprincípiosdoGooglePageSpeedpara
performanceWebclient-side,estãoocache,minimizaraquantidadedeinvocações
AJAXecompactarosarquivostrafegadosparaminimizaraquantidadededados
carregados.[189]
146

## Página 167

CasadoCódigo Capítulo6. Decisõesarquiteturais
Nospróximostópicos,semprequeumframeworkenvolvertrabalhoemmaisde
umtier,haverámençãodecomotomaressescuidadosnaprática.
6.2 D esenvolvimento Web MVC: Actions ou Compo-
nentes?
OJava1.0surgiunamesmaépocadoestourodaWeb.Mas,comovimos,aprimeira
abordagemdaplataformaeraousodeApplets client-side,emboraJamesGosling
jápensasseemalgo server-sidedesde1995. Oprimeiromovimentoemdire çãoà
geraçãodepáginas server-sidefoiolan çamentodeServletsem1997,seguidopelo
JSPem1998.[49]
OgrandepassodeServletfoicriarummodelobastanteperformáticoparatra-
balharcomHTTPemJavasemodesenvolvedorprecisarsepreocuparcomdetalhes
deinfraestruturaoudoprotocolo. Comseuprocessamentoderequisiçõessimul-
tâneasem Threadsparalelaslevesdocontainer,emvezdeprocessosconcorrentes,
asServletssemostrarammaisrápidas,escaláveiserobustasqueomodeloCGIda
época.IstofezoJavaganharconsiderávelimportâncianomercadoWeb.Masoobje-
tivodeServletsnuncafoicriarpáginasdemaneiradesacopladadopensamentodos
designers;seufocoerapermitirprogramausandooprotocoloHTTPemJava,com
grandeperformanceeescalabilidade.JavaServerPagesnasceuentãocomoobjetivo
detrazerprodutividadeefacilidadesnacriaçãodaspáginas,usandoasprópriasSer-
vletsporbaixo,paraaproveitarsuasvantagens.Noinício,ousodeJSPeramisturar
HTMLcomchamadasacomponentesJavaviapequenospedaçosdecódigoJava,os
hojetemidos scriptlets,desencorajadosagoraporpossibilitarumapéssimamistura
deresponsabilidades.
Alémdesertodabasedequalquerframeworkeinfraestruturasimportantesem
projetosWeb,Servletssãoideaisemmomentosnosquaisprecisamosmanipular
muitosdetalhesdoprotocoloHTTPexplicitamente.Páginasdinâmicasgeralmente
nãoprecisamdisto,porissoousomaisfrequentedeJSPsemconjuntocomfra-
meworks.
NolayerdeView,váriosenginesdetemplating,como VelocityeFreemarker,sur-
girampararemoverocódigoJavadosJSP.Maistarde,muitosdosnovosrecursos
dessesframeworksforamincorporadosaoJSP2.0comusoda expressionlanguagee
taglibs,aposentandoos scriptlets.
AViewnãoprecisasernecessariamenteconstituídaporumtemplateengine
comoJSPouVelocity. Seoclientedanossaaplicaç ãoforoutrosistema,aView
147

## Página 168

6.2. DesenvolvimentoWebMVC:ActionsouComponentes? CasadoCódigo
podeserimplementadaatravésdeumprocessodeserializaç ãodeobjetosparaal-
gumformato,comoado VRaptoraorenderizarumobjetoemJSON.Nessescasos,
umaconfiguraçãoprogramáticadaViewsubstituiumtemplateengine.Emvezde
somentepáginasHTML,estetipodesoluçãoécomumaodisponibilizarserviçosou
recursosviaWebparaconsumoporoutrossistemas.
AgrandeevoluçãonodesenvolvimentoWebveiocomarecomendaç ãodouso
dopadrãoarquitetural ModelViewController,oMVC.Osmodelosoriginais,tanto
deServletsquantodeJSPs,nãofocavamafacilitaç ãodaintegraçãocomdesigners,
aseparaçãoentrelógicadenegóciosecódigo client-sideouasboaspráticasdeOO
eencapsulamento.Criava-seumabarreiramuitoforteàmanuten çãoeextensão.O
padrãoMVC,origináriodacomunidadeSmalltalk,[27]passouaseraplicadonode-
senvolvimentoWebemJavacomaajudadeváriosoutrospadrões,depoisdocumen-
tadosnoconhecidolivro CoreJ2EEPatterns.[4]Aseparaçãoentre Model, Viewe C
ontrollerseriafeita,porexemplo,criandoumacaServletquefinafrentedetodasas
requisições,analisandoachamadaedelegandoparaoutraclassequerealmentesaiba
realizaralógicadenegócioemquestão,fazendoopapelde FrontController.[132]
Logopercebeu-sequeasimplementaçõesdoMVCerammuitopróximas, e
muitocódigoeraindependentedaaplicaç ão. Surgiramentãoosprimeirosfra-
meworkscomimplementaçõesreaproveitáveisdopadrãoMVC,entreeleso Apache
Struts,umdoscontroladorespioneirosnaplataformaJava.
AlémdaseparaçãoMVC,oStrutsaindatrouxeinternacionalizaç ão,validação
eintegraçãocomoutrastecnologiasdemercado.Foirealmenteumimensoavan ço
paraacomunidadeJava. Comotempo,porém,omercadopassouaverdeficiên-
ciasnoStrutseabuscaralternativas. Entreosproblemasestavamousoexaustivo
deherançadeclassesdoStruts(comoanecessidadedeestender ActionForm),asex-
cessivasconfiguraçõesemXMLeaspoucasconven çõesdecódigo,quegeravamum
forteacoplamentocomoframework.[60]UmdosprimeirosconcorrentesdoStruts
foioWebWorke,depois,vieramoutros,comoSpringMVC,Tapestry,VRaptore
Stripes. Cientesdosprópriosproblemas,osdesenvolvedoresdoStrutspassarama
investirno Struts 2jáem2005,propondoumajun çãocomoprojetoWebWork2,
quepossuíaumcódigomuitomaisflexível.[25]
Nomeiodetodaessarevoluç ãodoStruts,nasceu,em2004,pelomesmocria-
dordoStruts1,o JavaServer Faces.FoiaprimeiraespecificaçãoJavaEEparaMVC,
fortementebaseadaemideiasanterioresdeframeworksbaseadosemcomponen-
tes,comooASP.NET,plataformaparadesenvolvimentoWebcriadapelaMicrosoft.
Nessemesmoano,surgiuo RubyonRails,trazendomuitasideiasrevolucionáriasque
148

## Página 169

CasadoCódigo Capítulo6. Decisõesarquiteturais
seriamdepoisabsorvidasporváriosframeworks.Oatrasodolan çamentodoStruts
2gerouumadivisãograndenomercado,semhaverapresen çadeumlíderabsoluto,
comofoicomsuaprimeiraversão.Dezenasdeframeworksnovosapareciamatodo
momento,easnovidadesdoentãorecenteJava5estavamaindacome çandoaser
adotadas.Nessascondiçõesadversas,omercadoviuumportoseguronanovaespe-
cificaçãoJSFlan çadapeloJCP.Seumodelodecomponenteserabastantediferente
doqueseutilizavaemJavaatéentãoe,mesmocomsuaprimeiraversãoapresen-
tandodeficiênciasesemosprometidoseditoresvisuais,oJSFatingiuosucessocom
aajudadachanceladoJCP.
MVC
Mas,independentementedoframeworkoudaabordagempreferida,oMVC,
usualmentetidocomoumpadrãoarquitetural,acabouconsolidando-secomuna-
nimidade.HáaindaoutrospadrõesemesmovariaçõesdoMVC,massemprecom
oobjetivodefacilitaramanuten çãoefavoreceraseparaçãodas layers.AFigura6.7
apresentaumapossívelimplementaçãodopadrãoMVCparaumaaplicaç ãoWeb,
conformesugeridono JavaBluePrints,[19]eservecomobaseparaagrandeparte
dassoluçõesqueadotamessepadrão.
149

## Página 170

6.2. DesenvolvimentoWebMVC:ActionsouComponentes? CasadoCódigo
Figura6.7:UmapossívelimplementaçãodeModelViewControllerparaaplicações
Web.
OmodeloMVCvemjustamenteparafacilitaraseparaç ãodolayervisualda
aplicaçãododomínioedonegócio.Nadefiniç ãoformaldeMVC,[27]aatualização
daviewéfeitaatravésde observersquesãonotificadosdoseventosocorridosnos
modelos,umavisãomuitoligadaàsaplicaçõesdesenvolvidasnaépocaparaDesktop.
Mas,apesardadefiniçãoformaldessepadrãooudasinterpretaçõesqueomercado
adotoudoMVC,acaracterísticademaiorvaloréadesepararoscomponentesde
apresentaçãodorestodaaplicação(conhecidocomo SeparatedPresentation).[67]
Umadasformasdegarantirqueissoaconte çaénãopermitirqueumlayeracesse
outroquenãosejaseuvizinhodireto.Umexemploqueviolaestaregraéoacesso
diretoaosDAOspelas Views,sempassarporalgumaAction.Ou,ainda,oacessoa
umrepositóriopelamesma viewsempassarpelomodelo.CódigoHTMLmisturado
comSQLelógicadenegóciosemJavaéespecialmentedifícildemanter,alémdeo
reúsoserbaixo;mas,infelizmente,esteaindaéumdosgrandesresponsáveispelo
altocustodemanuten çãodecódigolegado.
UmagrandediscussãoemtornodomodeloéseasActions(ouequivalenteem
outrosframeworks)pertencemaosmodelosouaoscontroladores;algunsdesenvol-
vedoresacreditamqueessasclassessãocontroladoresjáque,dealgumaforma,co-
150

## Página 171

CasadoCódigo Capítulo6. Decisõesarquiteturais
nhecemarequisiçãoeas Views.Osmaispuristas,seguindoadefiniç ãodopadrão,
consideramqueelasfazempartedomodelo.
Action-based versus Component-based
AmaiorpartedosframeworksWebexistentessegue,naturalmente,omodelode
requisiçõeserespostasdopróprioHTTPetambémdasServlets.Encaixam-seaqui,
entreoutros,Struts(1e2),SpringMVC,Stripes,VRaptoreframeworksemoutras
linguagens,comoRubyonRails,Grails,DjangoeASP.NETMVC.Emboratodos
apresentemdiversasfacilidades,nenhumtemcomoobjetivoesconderomodelode
requisiçõeserespostasinerentedoprotocoloHTTP,nemsuacaracterística stateless,
seumodelodeURIsetantosoutrospontos.Essacategoriadeframeworksécomu-
mentereferenciadapor Action-basedouRequest-based.Oexemploaseguirmostra
umaaçãoquecadastraclientes,escritaatravésdoStruts2.
public class AdicionaClienteAction {
private Cliente cliente;
@Action(value=”adiciona” ,results = {
@Result(name = “ok”, location = “/cliente/adicionado.jsp”)
})
public String execute() {
new Clientes().adiciona(cliente);
return “ok”;
}
}
Emcontrapartida,háoutralinhadeframeworks,lideradapeloJSFeASP.NET,
quetrazumaabstraçãomaiornodesenvolvimentoWeb,noqualoobjetivoénão
observarmaistãodepertoosdetalheseofluxodoHTTP,mas,sim,trabalharcom
componentesvisuaisdealtoníveleummodelodedesenvolvimentomaispróximo
deaplicaçõesDesktop. Sãoosframeworks Component-based,nosquaistambém
podemosencaixarWicket,JBossSeam,GWTealgunsoutros(Figura6.8).
151

## Página 172

6.2. DesenvolvimentoWebMVC:ActionsouComponentes? CasadoCódigo
Figura6.8:Representandoumatelaatravésdecomponentesricos.
ComasincontáveispossibilidadesdeframeworksWeb,maisimportanteque
discutirfuncionalidadespontuaisdecadaumésaberescolherentre action-basede
component-based.Osframeworksbaseadosemcomponentes,comooJSF,têmcomo
objetivotrazercaracterísticasdodesenvolvimentoDesktopparaodesenvolvimento
Web. Programa-seorientadoacomponentesricosereaproveitáveis,comummo-
delodetratamentodeeventosrobustoemanuten çãodoestadodastelas(stateful ).
OHTTP,porém,nãoéfeitodecomponentes,masorientadoarequisições(nãoeven-
tos),eéstateless.Ouseja,umframework component-basedcomooJSFprecisacriar
abstraçõescomplexasemcimadomodelotradicionaldaWeb.
Algunsdesenvolvedoresnãoestãoacostumadoscomomodeloderequisiç ãoe
respostadaWeb,mas,sim,apensarnaintegraç ãoentreelementosdetela,como
comobotõesoucamposdetexto,controlandooquefazerquandoumdelesdispara
umevento,comooclique,mudan çadeumvalor,eoutros.AorigemdoMVCestá
ligadaaesseambienteDesktopouconsole,enãoaaplicaçõesWebbaseadasemre-
quisiçõeserespostas.[27],[67]HáaindaaplicaçõesWebcominterfacesmuitocom-
plexas,nasquaisainteraçãoentreosdiversoscomponenteseseusestadoséoponto
principal–nãohánecessidadedecontrolefinodoHTMLgerado,porexemplo.Nes-
sescasos,usarumframework component-basedcomoJSFpodefacilitarbastante.
MashásituaçõesemqueprecisamoscontrolaroHTMLfinal,como,porexem-
plo,porcausadeacessibilidade,ouparasuportarnavegadoreseplataformasdife-
rentes,ou,ainda,comootimizaçõesparabuscas(SEO),eatémesmocontrolefino
dasrequisiçõesAJAX,códigoJavaScripteHTML.Podehaveraindaanecessidadede
umamanipulaçãodasURIsutilizadas,tantoparasuportar bookmarkscorretamente
quantoparaatenderaosmecanismosdebuscas,e,ainda,permitirredirecionamen-
toseoutroscontroles.Podemospreferirtrabalharorientadosarequisiçõeserespos-
152

## Página 173

CasadoCódigo Capítulo6. Decisõesarquiteturais
tascomcaracterísticas statelessparamelhoraproveitaraWebeoutrasferramentas
quegiramemtornodoHTTP,alémdegarantirescalabilidadeedisponibilidademais
facilmente.Nessetipodesituação,usarumframework action-basedcostumaseen-
caixarmelhorcomosolução.[96]
Porém,éimportanteressaltarqueépossívelusarosdoismodelospararesolver
praticamentequalquerproblema.Nãoéporqueoptamosusar action-basedquenão
podemosusarcomponentesvisuaisricos,como,porexemplo,comJQueryUI,YUI
ouExtJS.Enãoéporqueoptamospor component-basedquenãopodemosdesen-
volverstatelessoucontrolarmelhorasURIseterumbomSEO.
Todososframeworkscostumamsuportar,aseumodo,recursoscomovalida-
ção,internacionalização,facilidadesparapopularos beansemuitosoutros.Emge-
ral,costuma-sedizerqueaplicaçõesWebcomplexasericasemformulários,quede
algumaformasejamumagrandeaplicação,sãomaisbemservidasporframeworks
component-based,enquantositesWebqueexijamumcontrolemaisfinodoqueestá
sendoenviadoparaoclientesãoocasoidealdos action-based.Ambososmodelos
sãocapazesdeatenderapraticamentetodososcenários,eaescolha,emgeral,sedá
peloestilodeprogramaçãodaequipe,quepodesermaisorientadoacomponentes
eeventosouapáginaserequisições. Aliás,umimportantemovimentoafavorda
ideiadacoexistênciaentreambososmodelosfoiolan çamentodoASP.NETMVC
pelaMicrosoft.Duranteanos,oASP.NETclássicofoisímbolodaeradosframeworks
component-based,eaprópriaplataforma.NEThojesuportatambémaabordagem
action-basedcomoASP.NETMVC.
JavaServer Faces
Porserumaespecificação,oJSFteveumaaceitaçãonomercadomuitomaisfácil
erápidaquemuitosframeworksescritosporterceiros.Aideiadetrabalharcomuma
especificaçãoémuitotentadoraparadiversasempresas,queprecisamdeumpouco
maisdegarantiadacontinuidadedatecnologia.Masestenãodeveseroúnicoponto
avaliadoaoescolherumatecnologiaparadeterminadoproblema,muitomenospara
resolvertodososproblemasdeumaempresa.
UmadasprimeiraspropagandasdoJSFdiziaqueseriapossívelescreverainter-
facedousuáriosemapreocupaçãocomondeelaseriadesenhada.Poderiaseremum
navegadorcomum(HTML),emumdecelular(WML),ouatémesmorenderizá-la
emFlash,semprecomomesmocódigoeosmesmoscomponentes.Bastariatrocar
oelementoquerenderizaaresposta–chamado Render-kit–eteríamosrenderiza-
çõesbemdiferentes. Estacaracterísticafoipoucoutilizada,poisanecessidadedas
153

## Página 174

6.2. DesenvolvimentoWebMVC:ActionsouComponentes? CasadoCódigo
empresaseraapenasdegerartelasHTMLparanavegadorescomuns;naprática,é
raroverumaaplicaçãoquetroqueorender-kitpadrãodoJSF.
MasessacaracterísticadenãoescreverapáginaemHTMLpuro,e,sim,usando
oscomponentesdoJSF,permitequeoframeworkcuidedeaspectosquegeralmente
causamproblemasparaosdesenvolvedoresWeb,escondendodiversospontostra-
balhosos. EstecontroledámuitopoderparaoJSFfazer,porexemplo,o binding
noscomponentes,permitindoaçõesquerealmentefacilitemodesenvolvimentode
sistemasWeb,comoovalordeumcamposerautomaticamenteguardadoemum
atributodeumbeanjáconvertidoparaoformatocorreto.Ouqueocliquedeum
botãonateladispareummétodoescolhidopelodesenvolvedordiretonobean.Ou,
ainda,que,aoocorrerumamudan çadeumvalor,sejadisparadaumavalidaç ão,
entreoutrosrecursos.
OcontrolequeoJSFfazsobreoqueacontecenoscomponentessóépossível
porqueoframeworkguardaemanipulaumarepresentaç ãodecadaelementocomo
umobjeto,organizandotodoselesnoformatodeuma árvoredecomponentes.Cada
elementodaárvoreguardaoestadoatualdoscomponentesdatelae,acadaevento
disparado,éfeitaumarequisiçãoparaoJSF,queseencarregade,logonoinícioda
requisição,atualizarasinformaçõesnestaárvore.
Aárvoredecomponentestambémserviuparaamenizaroutroproblemacomum
paraosnovosdesenvolvedoresWeb:ofatodeoprotocoloHTTPserstateless.Como
entreumarequisiçãoeoutranãoháarmazenamentodeinformaçõesautomatica-
mente,anãoserqueseusesessõesexplicitamente,oJSFajudoumuitoaoguardar
informaçõesnaárvore,tirandomaisumpesodascostasdodesenvolvedor.Há,por
exemplo,umpoderosoecomplexociclodevidadoscomponenteserequisiçõesJSF,
oquedáaodesenvolvedorapossibilidadedeacompanharasdiversasfasesdofluxo
internodeexecuçãodoJSF,comomanipulaçãodoestadodatela,validação,conver-
são,binding,invocaçãodalógicadenegócios,etc.
Alémdetudo,omodelo ComponentBasedqueoJSFusapermiteumagrandeex-
tensibilidade;épossívelcriarnovoscomponentesdeacordocomasuanecessidade.
Algumasempresasatémesmocriaramcomponentesextremamenteúteisepráticos,
como,porexemplo,o RichFaces,queadicionaàgamaoficialdecomponentesdoJSF
funcionalidadescomocomponentesmaisricos,ferramentasdelayout,temas,entre
outros.
OJSF2foiumagrandeevoluç ãonoframework,amenizandodiversosantigos
problemaseacrescentandoimportantesnovasfuncionalidades.Hásuportenativoa
Ajax,Faceletsintegrado,novosescopos,melhorsuporteaGETebookmarks.Além
154

## Página 175

CasadoCódigo Capítulo6. Decisõesarquiteturais
disso,hádiversasconvençõesquediminuemasconfiguraçõesque,porsuavez,agora
sãofeitascomanotaçõessimples.Outropontobastanteforteéaintegraç ãocomo
restantedoJavaEE6,emparticularasvalidaçõessimplificadascomBeanValidation,
injeçãodedependênciascomCDIeatétransformarosmanagedbeansemEJBspara
ganharosserviçosdocontainer.
Mesmocomdiversasvantagens,oJSFnãoéunanimidadeentreosdesenvol-
vedores. Pelofatodeser ComponentBased,aindaexistemalgunsempecilhospara
sistemasWeb.Entreeles,afaltadecontroledoHTMLéumdosmaissérios.Como
oHTMLégeradopelopróprioJSF,qualquerotimizaçãooumodificaçãoquequeira-
mosfazersetornaextremamentecustosaecomplexa;emcasosmaisextremos,pode
serqueoJSFnãodêsuporteadeterminadafuncionalidade.Odesigneaexperiência
dousuáriosão,emgeral,adaptadospelaslimitaçõesqueoJSFapresenta,emvezde
umaabordagemmaislivrenodesign,emqueocódigoseráadaptadoparaatingiro
resultadodesejado.
JSFsegueummodelomenosfocadonaWebemaisvoltadoparaaárvorede
componentes.AWebéapenasoambientedoJSF,masseuobjetivofinalsãooscom-
ponentes.JSFacabasetornandoumaferramentapoderosaparacriaraplicaçõescom
interfacesmuitocomplexas,comdiversasfuncionalidades,masquenãonecessitem
deumcontrolefinodoHTML,JavaScripteCSS,ouumaproximidademaiordas
característicasdoHTTP.Nessescasos,favore çaumframework ActionBased.
6.3 D omine sua ferramenta de mapeamento objeto
relacional
ConsultasSQL,gerenciamentodetransações,cacheseadecisãodequandopersistir
ebuscardadosdobancosãopreocupaçõesfrequentesemgrandepartedosprojetos
edemandammuitotempoetrabalho.Todocódigoutilizadopararesolveressespro-
blemasraramenteéescritodeformaafacilitarseureúso,eoprogramadoréobrigado
areescrevergrandepartedeleparaacessarosdadosaoiniciarumnovoprojeto.
Poresteeoutrosmotivos,soluçõesquevisamfacilitarotrabalhodoprograma-
dor,diminuindoanecessidadedousodoJDBCeaescritadecomplicadasconsultas
SQL,apareceramhábastantetempoeganhamcadavezmaisfor ça.
O que há de errado com o JDBC?
JDBCéumadasAPIsmaisantigasdoJava,existentedesdeoJDK1.1ecomcons-
tantesatualizações.Aversão4.0,disponívelnoJava6,trouxemelhoriassignificativas
155

## Página 176

6.3. Dominesuaferramentademapeamentoobjetorelacional CasadoCódigo
eoferecemuitopoderatémesmoabancosdedadosespecíficos.[156]Ocódigopara
executarumasimplestransaçãocomJDBCpuropodeserescritodemaneirabem
sucinta.
public void insere(String email) throws SQLException {
Connection con = abreConexao();
con.setAutoCommit(false);
con.createStatement().execute(
“INSERT INTO Destinatario(email) VALUES (‘”+ email + “’)”;
);
con.commit();
con.close();
}
Podenãoestaróbvio,masestetipodecódigoingênuoéacausadosprincipais
problemasaoacessarbancosdedadoscomJava: vazamentodememória,transa-
çõesnãofinalizadascorretamente,excessodeconexõesabertascomoservidorpela
ausênciadepool,baixaescalabilidade,vazamentodeconexõeseatémesmo SQL
injection.
Podemostentarresolveressesproblemascomumcódigomaiscompleto.
public class DestinatarioDao {
private final DataSource dataSource = new ComboPooledDataSource();
public void insere (String email) throws DAOException {
String sql = “INSERT INTO Destinatario(email) VALUES (?)”;
Connection con = null;
PreparedStatement stmt = null;
try {
con = this.dataSource.getConnection();
con.setAutoCommit(false);
stmt = con.prepareStatement(sql);
stmt.setString(1, email);
stmt.execute();
con.commit();
} catch (SQLException e) {
try {
if (con != null)
con.rollback();
throw new DAOException(“Erro no insert”,e);
156

## Página 177

CasadoCódigo Capítulo6. Decisõesarquiteturais
} catch (SQLException e) {
throw new DAOException(“Erro no insert e rollback”,e);
}
} finally {
try {
if (stmt != null)
stmt.close();
} catch (SQLException e) {
throw new DAOException(“Erro ao fechar statement”,e);
} finally {
try {
if (con != null)
con.close();
} catch (SQLException e) {
throw new DAOException(“Erro ao fechar con”,e);
}
}
}
}
}
Ocódigomaisrobustoutiliza PreparedStatementparaevitarSQLinjectione
tirarproveitodealgunsbancosquepré-compilamasqueries;tomacuidadocom
try, catch, finallyparanãodeixartransaçõespendenteseconexõesabertas;usa
umpooldeconexõesatravésdeum DataSourceparaevitarovazamentodestasenão
utilizarconexõesquepossivelmentepossamtersidofechadaspeloservidor.[183]
Eestecódigoaindapodetermelhorias.Oesfor çoemlançarexceptionscomboas
mensagensenãodeixarvazar SQLExceptionpoderiasermaiorcommaisblocos
try/catchparatrataroserrosseparadamente,comonocasodefalharaaberturada
conexão.Éválidorepararqueautilizaçãodeinversãodecontroleajudariabastante
otrabalhodeevitaressecódigorepetitivo(o boilerplatecode).Mesmotomandotodo
estecuidado,háaquiumtrabalhoaindadedesign,jáqueoprogramadordevedecidir
ondecolocarocódigoSQL,isolando-oemDAOs,arquivosde properties,XMLsou,
ainda,anotaçõesdoJDBC4.0.
ComaevoluçãodaplataformaJava,surgiramdiversassoluçõesparaminimizar
oriscoefacilitaraimplementaçãodospadrõesqueaparecemnocódigoanterior.
Aprimeiraop çãoseriaabstrairoacessodiretoaoJDBCtomandoasdevidaspre-
cauçõeseusandoasmelhorespráticas.Aindaassim,teríamosmuitotrabalhoecó-
digorepetido,e,porisso,ferramentasconhecidascomo datamapperssurgiram.Es-
157

## Página 178

6.3. Dominesuaferramentademapeamentoobjetorelacional CasadoCódigo
sasferramentasliberamoprogramadordaárduatarefadeexecutaraconsultaSQL,
mapearaslinhasdatabelanasentidadesdoseumodelo,gerenciartransações,etc.
Umframeworkbastanteutilizadoéo iBatis,consideradoporalgunscomoum
datamapper menospoderoso,quejáencapsulaasnecessidadescomunsdodesen-
volvedor,quandoutilizaoJDBC,echegaatéaorganizarasqueriesSQLsemarquivos
XML.[14]Apesardenãoserum datamapper,o Spring JDBC templateémaisuma
alternativadeuso.Essestiposde wrappers,porém,sãopoucousados.Umdosre-
flexosdestaperdadepopularidadeéqueoiBatisparousuaevoluç ão. Umforkfoi
criado,o MyBatis,masacomunidadeJavacaminhacadavezmaisparaasferramen-
tasdemapeamentoobjetorelacional.
Mapeamento objeto relacional
Opróximopassoseriautilizarumaferramentaquefacilitasseaindamaisotraba-
lhododesenvolvedor,fazendocomqueeledeixasseatémesmodeescreverconsultas
SQL.Essasferramentassãoconhecidascomo ORM(object-relationalmapping).Elas
sãocapazesdefazeraponteentreoparadigmaentidaderelacionaleoorientadoa
objetosdeformaaminimizaroabismoentreosconceitosdessasduasabordagens,
conhecidocomoaimpedânciaobjeto-relacional(objectrelationalimpedancemis-
match).[6]
Umexemplosãoastabelascompridasqueaparecemcomcertafrequênciano
mundorelacionale,diferentedeclassescommuitosatributosnaorientaç ãoaob-
jetos,nãosãovistascomtantarepulsa.Ferramentasdemapeamentodevempossi-
bilitarquemaisdeumaclassesejautilizadapararepresentarumaúnicatabela. O
contráriotambémpodeacontecer,comoumaclassesermapeadaemmaisdeuma
tabela.
Outrocasosãoastabelasassociativassimples.Elassãoaformadefazerorela-
cionamentomuitosparamuitos entreentidadesnomodelorelacional. Aomapear
isso,suaferramentadevearrumarumaformaelegantedeesconderessesaglomera-
dosdeparesdechaves,provavelmentesemcriarumaclasseparataleusandoapenas
coleçõesearraysdeobjetos.
Jáaherançaéumconceitoquenãobatecommodelagemrelacional.Emalguns
frameworksORM,ousodaheran çapodeformarumsériogargalodeacordocom
aformaderepresentaçãoadotadanobancodedados(asconhecidasestratégiasda
JPAedoHibernate),dadoquediversastabelasprecisamserconsultadasemalgumas
queriespolimórficas,emespecialquandoéimpossívelusaralgunsrecursosdoSQL,
comounions.[181]Muitosvãodesaconselharaheran ça,preferindousarcomposição,
158

## Página 179

CasadoCódigo Capítulo6. Decisõesarquiteturais
conformevistonotópico Eviteherança,favoreçacomposição[81],[181](Figura6.9).
Comafor çaqueasespecificaçõesJavaEEtêm,écomumqueaescolhaporuma
ferramentaORMacabecaindosobreumadasimplementaçõesdaJPA.Dentreelas,
osprincipaisconcorrentessãooOracleTopLink,aOpenJPA,aBEAKodo,oEclip-
seLinkeoHibernate,certamenteaop çãomaiscomum.Sejaqualforsuaescolha,há
algunscuidadosquedevemsertomados.
Figura6.9:Mapeamentoderelacionamentosmuitosparamuitosemuitosparaum.
Umcuidadoimportanteéentendereusarcorretamenteosmodos eagerelazyde
seobterobjetosrelacionados.Semprequetemosrelacionamentoscom @ManyToOne
ou @OneToOne, opadrãoétrazeroobjetorelacionado(eager ); e, quandotemos
@OneToManyou @ManyToMany, acoleçãodeobjetosrelacionadossóérecuperada
quandoforacessada(lazy ).Paraboapartedoscasos,ocomportamentopadrãoésu-
ficiente,maséprecisoidentificarcasosemqueprecisamosconfigurarum FetchType
diferente(porexemplo,quandoumobjetorelacionadoémuitopesadoequeremos
comportamentolazyemvezde eager).Éprecisoestaratentoaousoindiscrimidado
delazy,quepodegeraroproblemados n+1selects,comoveremos,assimcomoo
159

## Página 180

6.3. Dominesuaferramentademapeamentoobjetorelacional CasadoCódigo
usoindiscriminadode eagerpodeocasionarcarregamentodesnecessáriodedados
emexcesso.
Hátambémapossibilidadedeseajustaro fetchtype diretamentenasconsul-
tas;porexemplo,fazendoumabuscaespecíficacomo eageremqueorelaciona-
mentoestáconfiguradocomo lazy–usandojoinfetch nasHQLeo setFetchMode
dasCriterias.[155]AlgumasimplementaçõesdeJPA,comoaOpenJPAeoHiber-
nate,aindapermitemquecamposbásicossejam lazysemanecessidadedeuma
pré-compilação,possibilitandoqueumaentidadesejaparcialmentecarregadaeque
camposchavessejaminicializadossomentequandoesenecessários.
Outrocuidadoasertomadoénaintegraç ãocomorestantedaaplicaç ão. Na
Web,acessamosentidadesdonossomodelona Viewe,seelaspossuemrelaciona-
mentoslazy,precisamosqueo EntityManagerqueascarregouestejaabertoaté
ofimdarenderizaçãodapágina. Casoestejafechado,amaioriadasimplemen-
taçõesdeJPAnãovaisereconectaraobancodedadoselan çaráumaexception
(LazyInitializaionException,nocasodoHibernate).
Paraqueissonãoocorra,devemosmantero EntityManageraberto,sejaatravés
deumfiltro,deuminterceptadoroualgumoutromecanismo. Esteéoconhecido
patternOpenEntityManagerinView (derivadodo OpenSessioninView,termocu-
nhadopeloHibernate)(Figura6.10).
160

## Página 181

CasadoCódigo Capítulo6. Decisõesarquiteturais
Figura6.10:PadrãoOpenEntityManagerinView.
Outraformadeescapardosproblemasdeproxies lazyéutilizarumcontai-
nerdeinje çãodedependências. Frameworks, comoSpringeVRaptor, jápos-
suemfiltroseinterceptadoresparaessescasos, eatémesmousandoaanotaç ão
@PersistenceContextdoJavaEEparainje çãodedependênciaspodemosobtero
mesmoefeito.[184]
ComoadventodoJavaEE5ealgumasformasdeinje çãodedependências,di-
minuiuanecessidadedeumgrandenúmerodepatternsquehaviaparaoJ2EE,mas
algumaspreocupaçõesaindapersistem.Aprincipaldelasenvolvecomoacessarum
EntityManager,umaperguntaparaaqualexistemdiversasop ções:dentrodeum
objetoqueagecomoumDAO,emumDomainModelouemumModelFaç ade.
Aindaépossível,ecadavezmaisfácilcomousodainje çãodevariáveismembro,
acessá-lodiretamenteatravésdalógicadenegócios. Apesardeesteaindaserum
debateemquemuitasopiniõesdivergem,agrandemaioriadosdesenvolvedores
optaporprotegeroacessoao EntityManageratravésdeumDAO,nãopermitindo
quequalquercódigooacesseetambémajudandoareaproveitarmétodosqueen-
capsulamrotinasdeacessoadadosquesãomaisqueapenasaexecuç ãodeuma
161

## Página 182

6.3. Dominesuaferramentademapeamentoobjetorelacional CasadoCódigo
query.[153],[185]
Porumaquestãodeajustedegranularidade,paraquenãosejamexpostosmais
dadosqueonecessário,ouparaagrupardiferentesatributosdeentidadesemum
únicoresultado,épossívelquehajaanecessidadedo DataTransferObject.[154]Ou-
trospatternsdoJavaEE5tambémforamcatalogados,masmuitosdelesnãoforam
largamenteadotadospelacomunidade,oupossuemnomenclaturaeimplementa-
çõesdivergentes.[138],[154]
Connection Pool
Aquaseonipresen çadoHibernate,tantoatravésdousodaJPAquantodireta-
mente,fazcomqueoconhecimentoprofundodasfuncionalidadesoferecidaspor
esteframeworkmere çaatençãoespecial.Apesardoesfor çodaJPA1.0emunificar
umagrandepartedefuncionalidadescomunsatodasasferramentasORMemuma
especificação,muitoficoudefora.AJPA2.0tentadiminuiressasgrandesdiferen-
çasentreosdiversosfabricantesexistentes,criandonovasanotaçõeseestendendoa
interfaceEntityManagercomnovosmétodoserecursos.[46]
EntreosrecursosimportantesqueexistemnoHibernateeoutrosframeworks,
porémnãonaJPA,podemoscitaralgunsquesãovitaisparaaescalabilidadeea
performancedaaplicação. Odesconhecimentodessasfuncionalidadespodelevar
atémesmoumprojetosimplesaofracasso,sejapeloconsumoexcessivodememória,
sejapelodisparoexageradodequeries.[182]
Usarum pooldeconexões,porexemplo,épraticamenteobrigatórioemqual-
queraplicaçãoqueusebancodedados. Umproblemacomumemaplicaçõesque
abremconexõesindiscriminadamenteésobrecarregarobancocomumnúmero
muitograndedeconexões.Ousodopoolpermitecontrolaromáximodeconexões
quepodemserabertas.Alémdisso,abrirefecharconexõessãooperaçõescustosas.
Nãovaleapenaestabelecertodaacomunicaç ãocomobanco,abriraconexão,para
usá-larapidamente,edepoislogofechá-la.Usaropooleconomizabastantetempo
aomanterasconexõesabertasecompartilhá-las.
Hádiversospoolsdeconexãonomercadojáimplementadoseprontosparauso,
desdeospróprios datasourcesdosservidoresatébibliotecasseparadascomooC3P0
eoDBCP.UsarumpooldeconexõescomoHibernateéextremamentefácil,bas-
tandoumaspoucaslinhasdeconfiguraçãoXML,[93]lembrando-seapenasdeevitar
opoolpadrãodoframework,quedeveserutilizadoapenasparatestes.
Um problema tradicional dos pools está ligado à detecção de conexões
quebradas, que ainda estão marcadas como disponíveis, causando a famosa
162

## Página 183

CasadoCódigo Capítulo6. Decisõesarquiteturais
java.net.SocketException: Broken pipe aotentarutilizá-la.Énecessárioche-
cardealgumaformaseaconexãodeumpoolaindaestáválida,aberta,sejaatra-
vésdeumaverificação, aorequisitarumaconexão, sejaexecutandoverificações
periódicas.[183]
Cache e otimizando a performance
Outropontoimportanteparaumaboaperformanceeescalabilidadeéevitar
consultasrepetidasempequenosintervalosdetempo: osistemaresponderápido
eobancodedadosnãoéacionado. Dentrodeumamesma Session,asentidades
gerenciadasporelaficamemumcache,odeprimeironível(firstlevelcache),atéque
essasessãosejafechadaouaentidadeexplicitamenteremovida(atravésdo clearou
evict).Esseprimeironíveldecacheexisteparagarantiraintegridadedosdadosna
memóriaenobanco,evitandoquenocontextodeuma Sessionpossaexistirmais
deumarepresentaçãodomesmoregistroaomesmotempo.ÉoqueFowlerchama
deIdentityMapemseuPOEAA.[67]
PensandoemumcontextoWeb,ocachedeprimeironívelexisteduranteociclo
devidadeumarequisição.Épossíveliralém,jáquemuitasentidadessofrempoucas
alteraçõesepodemterseusdadoscacheadosporumaregiãomaiorqueadelimitada
porumaúnicarequisição.O cache de segundo nível (secondlevelcache)temeste
papel.Atravésdesimplesanotações,épossíveltirarproveitoderobustosmecanis-
mosdecache,como EhcacheouJBossCache. Épossívelaindaconfigurardetalhes
comoapolíticadociclodevidadasentidadesnocache(LRU,LFU,FIFO...),seu
respectivotamanho,ostemposdeexpiração,entreoutros.[212]
Quandoumadeterminadaentidadeforbuscadaatravésdesuachaveprimária
eaindanãoestivernocachedeprimeironível,oHibernatepassarápelocachede
segundonívelparaverificarsuapresen ça.Casoseutempodeexpiraç ãonãotenha
passado,umacópiadesseobjetocacheadoserádevolvidasemnecessidadedeacesso
aobancodedados.Seastabelasemquestãosãoapenasacessadasporsuaaplicaç ão,
épossívelconfigurarocachedetalmaneiraquenuncaexpireenquantonãohouver
umaatualizaçãonaentidade.Ocódigoaseguirmostraautilizaç ãotransparentede
umcachedesegundodenível,umavezqueasegundabuscanãoatingiráobanco
dedados:
EntityManager manager1 = jpa.getEntityManager();
Conta primeiroRetorno = manager1.find(Conta.class, 15);
EntityManager manager2 = jpa.getEntityManager();
163

## Página 184

6.3. Dominesuaferramentademapeamentoobjetorelacional CasadoCódigo
Conta segundoRetorno = manager2.find(Conta.class, 15);
System.out.println(“Titular da primeiraconta: “+
primeiroRetorno.getTitular());
System.out.println(“Titular da segundaconta: “+
segundoRetorno.getTitular());
NaFigura6.11épossívelverificarcomoosdadossãoarmazenadoseencontrados
nocachedeprimeiroesegundoníveis:
Fazerumcacheeficiente,queevitavazamentodememóriaeproblemasdecon-
corrênciasemperderescalabilidade,éumatarefadifícil;aoadotarferramentasde
ORMquesuportamtaisbibliotecas,todaessainfraestruturajáestádisponível.Mas
todaestratégiadecacheéperigosaporque,paraevitarficarcomdadosobsoletos,é
precisoumaboapolíticadeinvalidaç ãoemcasodeatualizações. OHibernatefaz
tudoissodeformatransparenteseasatualizaçõessãofeitasatravésdele. Mas,se
nossosobjetostiveremmuitasatualizaçõesemcomparaçãocomonúmerodecon-
sultas,oefeitopodeseroinversododesejado:oHibernategastarámuitotemponas
invalidaçõesdecacheeaperformanceprovavelmenteseráprejudicada. Use cache
apenas em entidades que não mudam nunca ou nas que mudam muito pouco em
relação às consultas.
164

## Página 185

CasadoCódigo Capítulo6. Decisõesarquiteturais
Figura6.11:Cachedeprimeiroesegundoníveisemaç ão.
Aado çãodecachesfavoreceperformanceeescalabilidadeemtrocademaior
consumodememória.Cachessãoaindamaiseficazesparaaplicaçõesnasquaisda-
dosdesatualizados(stale)podemsermostradospordeterminadoperíododetempo
semprejuízoparaocliente. Porexemplo,umaqueryqueretornaoprodutomais
vendidonodiapodesercacheadaporalgunsminutosouatéhoras.
Oquefoiapresentadoatéagoraéochamadocachedeentidades.Masfrequente-
mentesãoexecutadaspesquisasqueretornamomesmoresultadoatéqueastabelas
envolvidassoframalterações.OHibernatepodecachearatémesmooresultadode
queries,atravésdoquerycache.Guardartodooresultadodeumaqueryconsumiria
muitamemóriaedadosrepetidos,eéporissoqueaferramentavaiapenasarmaze-
naraschavesprimáriasdasentidadesdevolvidas.Quandoestaforexecutadamais
umavez,oHibernatepegaráesseconjuntodechavesprimáriaseasbuscará,sem
anecessidadedeexecutaraquerydenovo.Porisso,éimportantetambémcolocar
essasentidadesnocachedesegundonível,enãoapenasaquery,paraqueanovaexe-
cuçãonãoprecisefazernenhumhitnobancodedados,utilizandoapenasosdados
damemóriaparadevolveroresultado.
165

## Página 186

6.3. Dominesuaferramentademapeamentoobjetorelacional CasadoCódigo
Esseresultadodequerycacheadoseráinvalidadoaomenorsinaldemodificaç ão
nastabelasenvolvidas,poisissopodealteraroqueestaqueryretornaria. Queries
queenvolvamtabelasmodificadasconstantementenãosãoboascandidatasao query
cache.
Épossívelqueodesenvolvedornãoqueirainvalidartodoocachedeumaquery
acadamodificaçãonasrespectivastabelas,poisdiversasvezeséaceitávelqueares-
postaparaumaquerynãosejaconsistentecomosdadosmaisatuais,ousejasabido
queaatualizaçãodedeterminadoscamposnãoinfluenciamoresultadodasqueries.
Essecomportamentodeinvalidaçãodocachedequeriespodesermodificadopara
umajustemaisfino,atravésdasubstituiç ãoda StandardQueryCache,implemen-
tandodiretamentea QueryCacheouestendendoopadrão,paraquesejatolerantea
algunsupdates.[95]
Emqueriesmuitopesadasefrequentementeacessadas, umaimplementaç ão
simples,queverificaaexistênciadainformaçãonocacheeentãoexecutaaquery,
podepossuirgargalos.Se,porexemplo,nointervalode10segundos,200usuários
acessaremessainformaçãoeaindanãohaviadadosnocache,aqueryseráexecutada
umavezparacadaumdeles,jáqueoresultadosóécolocadonocacheapósoretorno
daprimeirarequisição.Esseproblema,quandomuitasrequisiçõesseacumulamem
cimadeumdado,quepodeounãoestarcacheado,échamadode dogpileeffect.[97]
Odoublechecklocking eoutrasboaspráticasprevinemsituaçõescomoessas,eéim-
portanteconhecê-las.[171],[18],[83]Aintegraçãodosframeworkscomasbibliotecas
decachejáseprevinemdessassituações,porém,aoutilizarabibliotecadecachedi-
retamente,eemalgunscasosistosefaznecessário,vocêmesmoprecisatomaressas
medidas.
Quandoovolumededadosémuitogrande,umamáquinapodeserpoucopara
guardartodoocache.Épossívelutilizarumclusterparaarmazená-lo,eoHibernate
játrabalhacomInfinispan,CoherenceeMemcachedeformaadiminuiranecessidade
deconfiguração. Comeles,épossívelfazero finetuning paraminimizarotráfego
intracluster,alémdedesabilitarasincronizaçãoimediatadeestadocomobancode
dados,usandoo write-behind,umaabordagemassíncronamuitomaisescalável,po-
rémcommenorconfiabilidade,poispermiteavisualizaçãodedadosdesatualizados
(staledata).[208],[216]
Mais otimizações e recursos
Alémdasestratégiasdecache,oHibernateaindadisponibilizaoutrosmecanis-
mosdeotimização.Aoexecutarumaquery,écomumiterarsobretodasasentidades
166

## Página 187

CasadoCódigo Capítulo6. Decisõesarquiteturais
retornadas.Seoresultadodeumaqueryéum List<Livro>,e Livropossuicomo
atributouma List<Autor>queserácarregadademaneira lazy,existeentãoumpo-
tencialproblema:aofazerolaçoparamostrartodososautoresdesseslivros,para
cadainvocação livro.getAutores()umanovaqueryseráexecutada,porexemplo:
select * from Autor where livro_id = 1
select * from Autor where livro_id = 3
select * from Autor where livro_id = 7
select * from Autor where livro_id = 12
select * from Autor where livro_id = 15
select * from Autor where livro_id = 16
Esteproblemaéconhecidocomo n+1,pois,aoexecutarumaúnicaquery,tem-se
comoefeitocolateralaexecuçãodemais n queries,onde néonúmerodeentidades
resultantedaqueryoriginalequepodeserbemgrande.
ÉpossívelconfiguraroHibernateparaqueeleinicializeacole ção lazydeau-
toresdoslivrosdeumamaneiramaisagressiva,semfazercadacarregamentose-
paramente,massimde5em5,valorquepodeserdefinidoatravésdaanotaç ão
@BatchSize(size=5),quediminuibastanteasqueriesdeinicializaç ão:
select * from Autor where livro_id in {1, 3, 7, 12, 15}
select * from Autor where livro_id in {16}
Assim,onúmerodequeriesexecutadaséminimizado,unindodiversasqueries
emumaúnica,diminuindoonúmerode roundtripsatéobancodedados.
Paradetectarapresen çadoprobleman+1eoutros,nãoéviávelolharotempo
todoologdequeriesemproduç ão,poiséfácildeixarescapardiversosgargalos.O
Hibernatepossuiaclasse Statisticsque,sehabilitada,armazenarádadossobre
entidades,relacionamentos,queriesecache. Épossívelvercomdetalhesquantas
vezescadaqueryestásendoexecutada,ostemposmáximos,mínimosemédios;e,
ainda,quantasvezesocachedesegundoníveléinvalidadoemcomparaç ãoaquantas
vezeseleéusado;ouatéquantastransaçõesforamabertasenãocomitadas,entre
outros.Atravésdestaclasse,émuitomaisfácilidentificargargaloseproblemaspara
sabermosondecolocarumnovocache,ondeusaro @BatchSize,ondeémelhorser
eageroulazy,etc.
Aindafalandoemotimizações,oHibernateémuitasvezescriticadoemsituações
queenvolvemoprocessamentodemuitosdadosdeumavez.Masexistemmecanis-
mosespecíficosparatrabalharnessescasos.[92]Imaginequesejanecessáriofazer
oprocessamentodeumimensoarquivoTXTeinserirmilhõesdelinhasnobanco
167

## Página 188

6.3. Dominesuaferramentademapeamentoobjetorelacional CasadoCódigo
dedadosdeumavez.Ainvocaç ãode session.save(ouentityManager.persist)
váriasvezes,provavelmente,vairesultaremuma OutOfMemoryError.
Anoçãodecontextopersistenteatreladoàsessãofazcomquetodososobjetos
inseridossejamarmazenadosnocachedeprimeironívelatéqueelasejafechada.
Einserirmuitosobjetosnessecachenãoéumaboaideia. Soluçõespossíveisvão
desdechamar session.cleardevezemquandoparalimparessecache,atéusar
diretamentea StatelessSession,outrotipodesessãoquenãoguardaestado(epor
issoperdeváriosbenefíciosdoHibernate,masresolveproblemasdemanipulaç ão
demuitosobjetos).
Jáquandooproblemafortrazermuitosregistrosdobancoparaamemória,me-
lhorqueexecutarumasimples queryepegarumaimensalistadeobjetosqueprova-
velmenteestouraráamemória,éestudarestratégiasdecomopegarpoucosobjetos
porvez.Nessecenário,os ScrollableResultspermitemautilizaçãodocursordi-
retamentenobancodedados,evitandotrazertodososdadosdeumavezparaa
memória.
Deve-seconsideraratésevaleapenatrazeroselementosparaamemória.Mui-
tosprocessamentospodemserfeitosdiretamentenobancodedadosatravésde batch
updates.Porexemplo,reajustarem10%ospre çosdetodososprodutosdeumaloja:
emvezdetrazertodososprodutosparaamemóriaeatualizarchamandoo setPreco,
podemosexecutarumúnico UPDATEdiretamentenobancodedados.OHibernate
suportaessetipodeprocessamentoatravésde UPDATE,DELETEeINSERT...SE-
LECTdiretamentepelaHQL.
ÉtambémpossívelexecutarqueriesnativaspeloHibernate. Emboraumadas
grandesfacilidadesdoframeworksejaageraç ãodasqueries,existemsituaçõesnas
quaisqueremosescreveralgumasdelasdiretamente. Umbommotivoéaprovei-
tarasqueriescomplexas,escritaspeloDBA,comtodososdetalhesdeotimizaç ão
dobanco,emvezdetentartraduzirtudoparaoHQL.Comqueriesnativas,conse-
guimoschamarrecursosbemespecíficosdobancodedadosqueestamosusando,
inclusivestoredprocedures,eobterumgrauamaisdeotimizaç ãonassituaçõesem
queperformanceformaisimportantequeportabilidadedebancodedados.
Háaindadiversasoutrasfuncionalidades,comoaexistênciadomodode fetch
extralazy,fazendocomqueumacole çãonãosejainteiramenteinicializada:queries
diferentesserãodisparadasparachamadas,como lista.size(), lista.get(15)e
atémesmo lista.add (entidade),evitandocarregamentodedadosdesnecessá-
rios.Ou,ainda,asfuncionalidadesdeauditoriadoHibernate,quepermitemmanter
umhistóricocompletodealteraçõesemcadaentidadedosistema.
168

## Página 189

CasadoCódigo Capítulo6. Decisõesarquiteturais
Alémdefuncionalidadespróprias,oHiberantepossuidiversossubprojetosque
auxiliamtarefascomumenterelacionadasaobancodedados.O Hibernate Search,
porexemplo,integrademaneiraeleganteoLucenecomoHibernate,permitindo
queseuíndicedepequisatextualsejaatualizadodemaneiratransparenteatravésde
listeners,epossuimecanismosdealtaescalabilidadeparafazeraatualizaç ãodestes
demaneiraassíncrona. Abuscatextualmuitasvezesédeixadadeladopordesco-
nhecimentodoLuceneedestaintegraç ão,gerandoqueriescomplexasquegeram
resultadospobres,jáqueoSQLnãopermitebuscascomomesmopoder.
Nãousaralgumasdessaspoderosasfuncionalidadespodedificultarodesenvol-
vimentodaaplicação,alémdepossivelmentecriarumenormegargalodeperfor-
mance.Éimportanteconhecerafundoasfuncionalidadesqueafetamaperformance
doHibernate,[94]alémdetodososoutrosrecursosparaaumentaraprodutividade
doprogramador. Novamenteaqui, usar um framework sem um conhecimento
significativo sobre suas funcionalidades pode causar problemas que seriam fa-
cilmente evitados.
6.4 D istribuição de objetos
Distribuirobjetosemdiferentesmáquinaséumapropostacomumparatentarme-
lhoraraescalabilidadedeumaaplicaç ão. Masasdificuldadesedesvantagensque
umaarquiteturadistribuídaapresentapodemsermaisprejudiciaisàperformancee
manutenibilidadedoqueosganhos.
Essasvantagensedesvantagensdadistribuiç ãodosobjetosdependemdode-
signadotadopelaimplementação,quepodeinduzirosdesenvolvedoresacometer
erroscomfacilidade.Historicamente,porescolhasinadequadasnodesigndediver-
sastecnologiasdeobjetosdistribuídos,criaram-sedesignpatternspararesolveros
problemasinerentesàremotabilidade,comoosrelacionadosàperdadeescalabili-
dadeaofazerinvocaçõesremotasemexcessosemnecessidade,ouaotransportarum
volumealtodedadosentreos tiers.
ComcadaversãonovadoEJB,porexemplo,asinvocaçõesremotasficammais
transparenteseseaproximamdemaisaumainvocaç ãolocal,quandoolhamosape-
nasocódigo.Odesenvolvedorsemmuitoconhecimentopodeacabarcodificandoe
gerandoinúmerasrequisiçõesentretiers,causandoperdadeperformanceeescala-
bilidade,problemascomunsaoempregartaissoluçõessemodevidocuidado.
MartinFowler,conhecidoporseustrabalhosemtornodeboaspráticasdeOO
epatternsarquiteturais,formuloua PrimeiraLeideObjetosDistribuídos:“Não dis-
169

## Página 190

6.4. Distribuiçãodeobjetos CasadoCódigo
tribua seus objetos”.[64],[63]
Aocriarinterfacesdegranularidadegrossanos Facades,aocopiarobjetosem
DTOseemmuitasoutrassituaçõesimpostaspelaremotabilidade,sacrificam-seas
boaspráticasdedesignOO,diminuindoaflexibilidadeeaextensibilidade. Eeste
preçoéaltodemaisparasepagarnamaioriadoscasos. Demodogeral,Fowler
pregaquedevemosfavorecerumsistemabemprojetadoeflexívelaumaarquite-
turadistribuída.Étambémpelomotivodacomplexidadeedocustodeinvocações
remotasqueaMicrosoftrecomendaousodearquiteturasnãodistribuídasquando
possível.[13]ProgramarpensandoemFacadescommétodosdegranularidademaior
émuitodiferentedoqueseestáacostumadoafazercomumaúnicaJVM.
OsprincipaisargumentosparausodearquiteturasdistribuídascomEJBssão
escalabilidadeedisponibilidade. Umadivisãomuitocomumparaissoésepararo
WebserverdoApplicationserveremdois tiers(Figura6.12).
Figura6.12:DivisãoentreWebservereApplicationserveremumaarquiteturaN-
tiers.
Masépossívelganharescalabilidadeedisponibilidadesemessaseparaç ão;po-
demoscriartodaaaplicaçãoedepoisrodá-laemumcluster,ondecadamáquina
teráumainstânciacompletadaaplicação. Evitandomanteroestadonamáquina,
ficafácilobterredundâncianumclusterassim,semnecessidadedereplicaç ãoesin-
cronizaçãodeinformaçõesentreseusnós.
170

## Página 191

CasadoCódigo Capítulo6. Decisõesarquiteturais
Hácasos,claro,emqueexisteanecessidadededistribuirobjetos.Estanãodeve
seraregra,masaexce ção. Programadoresdevemsercríticoseparcimoniososna
distribuiçãodeobjetos,eFowlerchegaabrincarque“vocêdevevendersuaavópre-
diletaantesdedistribuirseusobjetos”.[67]Mesmotentandoevitartodasassituações
dedistribuiçãodeobjetos,muitasvezesvocênãoconseguiráeliminartodas.
EJBs
Écomumquediscussõessobreobjetosdistribuídosenvolvendoaplataforma
JavatoquemnoassuntoEJBs.DesdeseunascimentodentrodaIBM,estatecnologia
foifortementedivulgadacomopartefundamentaldaarquiteturaJavaEE,equeteria
papelimportantíssimoemtodotipodeprojetoJava.Muitosprojetospassaramauti-
lizarEJBsporcausadisso,muitasvezessemrefletirosuficientesobreessaescolha.
ElogosurgiuogrupodoscríticosferrenhosaosEJBs,questionandoasvantagense
apontandoasdesvantagensdeadotaratecnologia.
AntesmesmodosEJBs,comoobjetivodeexporainterfacedeumobjetopara
acessoremoto,foicriadaaespecificaçãodoRMI,umatecnologiaquesóprovêore-
cursoderemotabilidade.Os EnterpriseJavaBeansforaminicialmentedesenvolvidos
pelaIBM,em1997,comoumcontainerdeserviçosemcimadoRMI.Incorporados
em1998pelaSunàplataformaJava,oEJBtinhacomoobjetivoproverum container
quedisponibilizasseimplementaçõesdediversosaspectosenecessidadescomunsàs
aplicaçõescorporativas.
Entreessesserviços,temospersistência,controletransacional,segurança,men-
sageria,WebServices,serviçodenomes,poolingdeobjetosemuitosoutros.Como
éumaespecificaçãodoJavaEE,tudoissoestáprontoeimplementadonosdiver-
sosservidoresdeaplicaçãodisponíveisparausoemqualqueraplicaç ãoJava.Com
aevoluçãodaplataforma,essesrecursosficarammaisfáceisdeserutilizadospelas
aplicações,alémdeaumentaraquantidadederecursospadronizados,diminuindo
asfuncionalidadesespecíficasdecontainer. Conhecerbemoquecadaumdesses
serviçostrazéimportanteparatomaradecisãodeadotarounãoomodelodecom-
ponentesdoEJB.
OsStatefulSessionBeans sãoosquemaisseassemelhamàideiadeumobjeto
expostopeloRMI,mascomserviçosadicionais.Éumobjetonoservidorqueguarda
oestadodasessãocomocliente. Cadaclientepossuisuaprópriainstância,onde
podearmazenarseusdadosechamarmétodosremotosdenegócio(Figura6.13).
171

## Página 192

6.4. Distribuiçãodeobjetos CasadoCódigo
Figura6.13:StatefulSessionBeanscominstânciasreservadasparacadacliente.
Paraatingiraltaescalabilidade–umadasvantagensdoEJB–,ocontainerpossui
ummecanismodepassivaçãoeativaçãodeobjetos.Comoonúmerodeinstâncias
podesermuitograndeemaplicaçõescommuitosusuáriossimultâneos,ocontainer
écapazdetemporariamenteserializaralgunsdosobjetosdamemóriaqueestejam
semusonomomento(passiva ção).E,tãologoousuárionecessitenovamentedasua
instância,ocontainervaireativarnamemóriademodotransparente(ativa ção),sem
necessidadedecódigoextranenhumporpartedosdesenvolvedoresdaaplicaç ão.
Essetipodecomportamento,somadoàcapacidadedereplicaç ãoeclusterização
dosservidoresdeaplicação,éoquefazosEJBsseremtãousadosparaatingiralta
escalabilidadeedisponibilidade.
JáosStatelessSessionBeans tentamtratardeoutracategoriadeuso,naqualse
queradistribuiçãodoobjetoeosserviçosdocontainer,masondenãoénecessário
guardarinformaçõesrelativasaumcliente.Éumobjetoqueexpõemétodosdeló-
gicadenegóciosemnecessidadedeserutilizadosemprepelomesmocliente(Figura
6.14).
172

## Página 193

CasadoCódigo Capítulo6. Decisõesarquiteturais
Figura6.14:PooldeinstânciasdoStatelessSessionBeanscompartilhadasportodos
osclientes.
MasonomedessetipodeEJBéextremamenteconfuso. Otermo statelesssu-
gerequeoobjetonãopodeteratributosemanterestado.Maselepodeterestado,
desdequenãosejavinculadoaalgumclienteespecífico.Dizemosqueelenãopodeé
manterestadoconversacional,ouseja,todaconversacomoclientedeveserfeitaem
umaúnicainvocaçãodemétodo;seeleinvocarumsegundométodo,seráumanova
conversa,epossivelmenteatécomumobjetodiferente.
Éporestemotivoqueocontainermantémum poolcomváriasinstânciascom-
partilhadasentreosdiversosclientes.Osclientesnãosabemqualinstânciaacessarão
dopoolacadanovainvocaç ão,porissonãodevemmanterestadorelacionadoao
cliente.ÉmuitocomumusarestetipodeEJBparafazerumpooldeconexões,por
exemplo,ondecadaobjetomantémumaconexãoabertaemumatributoseu.Para
ocliente,todososobjetossãoequivalentes,semestadoqueoatreleàquelainstância
específica.
Portanto,apalavra statelesspodeconfundir,assimcomoapalavra session,que
173

## Página 194

6.4. Distribuiçãodeobjetos CasadoCódigo
poderiaindicarqueoobjetoguardasessão(estadoconversacional),justamenteo
queelenãofaz. Os statelesssessionbean costumamserusadosapenasparaexpor
métodosdenegócioindependentesentresi,queexecutamumafuncionalidadee
devolvemalgumarespostasemesperarnecessariamenteporumapróximainvocaç ão
domesmocliente.Elepodeatémanteroestadodesuainstância,masnãoumestado
conversacionalcomocliente.
OsEntityBeans fechamostiposdeEJBsqueestavamdisponíveisdesdeaspri-
meirasversõesdaplataforma.Mas,aocontráriodos sessionbeans,apartirdaversão
3.0,elesdeixaramdeserobjetosremotos,e,daversão3.1emdiante,suaespecifica-
ção,aJavaPersistenceAPI,éatémesmoumaoutraJSR.Oobjetivodos entitybeans
eraoferecerumserviçodepersistêncianocontainerEJB.Seriamobjetosgerenciados
pelocontainer,representandoentidadesdobancodedadossemqueodesenvolve-
dorprecisassesepreocuparcomtodaapersistência.Éumserviçobastanteútil,mas
eleseramremotos.
Imagineumsistemadeumalojavirtualquefaçaumabuscaeretorneumalistade
Produto.Seprecisarmospercorreressalistade,digamos,100elementos,invocando
getNomeegetPrecoemcadaum,aousarmos entitybeans,teríamos200invocações
remotasdemétodos,queéumgargalogiganteparaaescalabilidadedosistemapelo
excessodecomunicaçãoentretiers.Justamentepararesolveresteproblema,foique
oCoreJ2EEpatterns passouapregarousodo DataTransferObject oDTO(antiga-
mentechamadode ValueObjectporessecatálogo)(Figura6.15).
174

## Página 195

CasadoCódigo Capítulo6. Decisõesarquiteturais
Figura6.15:Clientesinvocandométodosremotosemumafrequênciamuitoalta.
Emvezdedevolverumareferênciaremotado entitybean,opadrãonosmostra
queosdadosdevemsercopiadosparaoutrosobjetossimples,nãoremotoseseriali-
záveis.Destaforma,oclienteconseguiriaosobjetosdesejadosparausolocalmente
dosdados,semopre çodograndenúmerodeinvocaçõesremotas.Opadrãoacabou
virandoumremendodaespecificaçãodeEJB;quandoerausadoentitybean,sem-
preprecisávamosaplicaroDTO.Estapráticaficoutãoforte,queoDTOcome çoua
seraplicadoemoutrassituações,muitasvezessemnecessidade;porexemplo,para
transportardadosentre layersemvezde tiers.[67],[154]Algunsatémesmoaplicavam
DTOsnoMVCparatrafegarobjetosentreoModeleaView,copiandoecolando
atributoseadicionandocomplexidadesemnecessidade.[28]
ComoEJB3.0,oproblemadanecessidadeobrigatóriadoDTOpassouaser
resolvidopelaJavaPersistenceAPI,ondeasentidadesnãosãomaisremotas,esim
serializáveis;opatternfoiabsorvidopeloframework.Paradiminuiraquantidadede
requisiçõesaobancodedados,pode-seutilizaraconstrução select new Classeda
JPA-QL,quepermitesermaisespecíficocomosdadosaseremcarregados,atravésdo
usodeValueObjectsdegranularidademaisajustada,que,paraalgunsautores,vão
175

## Página 196

6.4. Distribuiçãodeobjetos CasadoCódigo
agircomoumDTOnestecaso.[154]Hátambémsituaçõesnovasparaselidar,como
potenciaisproblemascomrelacionamentos lazynãoinicializadosantesdaseriali-
zação.Eaindaoutrosantigospatterns,alémdoDTO,quetambémperdemespaço,
comoservicelocator parabuscardependências,substituídoporinje çãodedepen-
dênciaseCDI.
OutrotipodeEJB,queentrounaversão2.0,sãoos Message-drivenBeans,que
permitemoprocessamentodemensagensassíncronascomJMS.Édiferentedosde-
maisEJBspornãopossuirinterfaceremota,poiséapenasumcomponentedentro
doservidor,usufruindodainfraestruturadeserviçosdocontainerepossibilitando
maiorescalabilidade. VamostratardemensageriaeJMSnopróximotópicodeste
capítulo.
OúltimotipodeEJBacrescentadoàplataformafoio Singleton Bean,novona
versão3.1.Éumobjetoglobalcomestadocompartilhadoportodaaaplicaç ão,ga-
rantindoaunicidademesmoemambienteclusterizado. Éútilparaexpordadose
comportamentosquesejamnecessáriosemváriospontosdaaplicaç ãodemaneira
seguraemrelaçãoàconcorrênciaecomtodoosuportedocontainer.
Remoto ou local?
QuandoosEJBssurgiram,comovimos,foramapresentadoscomoumaevoluç ão
doRMI.Eraumatecnologiaparafacilitarousodeobjetosdistribuídoseiralém,
manipulandotambémseuciclodevida,seguran ça,persistênciaeoutrosserviçosde
infraestrutura.
Umaimportanteevoluçãonaversão2.0foiosuporteainterfaceslocais.Apartir
destaversão,umEJBpoderiater,alémdainterfaceremota,umalocalquepermiti-
riaqueoobjetofosseusadoeficientementeporoutrosobjetosnamesmaJVMenão
fosseexpostoremotamente.Asinterfaceslocaisforamessenciaisparaseimplemen-
taralgunsdosconhecidospatternsdoJavaEEemrelaç ãoàremotabilidade,comoo
DTO.Nessecenário,porexemplo,o entitybeanéacessadopelasuainterfacelocalno
servidor,enuncaédiretamenteexpostoremotamente,evitandoinvocaçõesremotas
emexcesso(Figura6.16).
176

## Página 197

CasadoCódigo Capítulo6. Decisõesarquiteturais
Figura6.16:PadrãoDataTransferObject.
Outropadrãomuitoutilizadoerao SessionFacade,[139]tambémdoCoreJ2EE
Patterns. EmumsistemabemconstruídodeacordocomasboaspráticasdeOO,
encapsulamentoeseparaçãoderesponsabilidades,criamosumasériedepequenos
objetos,cadaumcomsuaresponsabilidadedistinta,etodoscolaborandoparaexecu-
taraslógicasdosistema.Masoproblemaéque,emumsistemadistribuídocomoos
EJBs,exporaoclientemuitosobjetoscompequenosmétodosacabaimplicandouma
granularidademuitofina.Istoé,paraexecutaralgumaoperaç ão,oclienteacabaria
efetuandomuitasinvocaçõesremotasparaacessarváriosmétodoseobjetos,cau-
sandoproblemassériosdeescalabilidade.O SessionFacadepropõeacriaçãodeno-
vosobjetosremotoscominterfacedegranularidademaisgrossaparaseremexpostos
remotamenteaocliente,paraqueeleinvoqueapenasesseFacaderemotamente,eo
Facade,porsuavez,fazainvocaç ãoaosdiversosobjetosdenegócioenvolvidosna-
quelaoperaçãousandosuasinterfaceslocais.Essepatternaindaémuitousadono
EJB3,apesardeseunomenãosermaiscitadocomamesmafrequência.Éessencial
emqualquerarquiteturadistribuídapreocupar-secomagranularidadedosserviços
disponibilizados(Figura6.17).
177

## Página 198

6.4. Distribuiçãodeobjetos CasadoCódigo
Figura6.17:UsandoFacadesparadiminuiragranularidadeemchamadasremotas.
ÉbastanteinteressanteacompanharahistóriadosEJBscomrelaç ãoàdistribui-
çãodeobjetos.Lembrandoque,originalmente,eraumatecnologiaestritamentedis-
tribuída,mesmoqueainvocaçãoocorresseemumamesmamáquinavirtual. Na
versão2,asinterfaceslocaisforamincluídasparaajudaraimplementarospatterns
queresolvemosproblemasdeescalabilidade,evitandooexcessodeinvocaçõesre-
motas.NessaépocadoEJB2équecríticosdaplataforma,comoopróprioMartin
FowlereRodJohnson,passaramapensaremalternativascomoPOJOs,containers
leveseoSpring,poisemmuitoscasosaremotabilidadeeadistribuiç ãodeobjetos
nãoeramnecessárias.
OsEJBsforammuitoutilizadoscomoumaalternativamaisfácilaoCORBA,em
especialparaocasomaissimplesdepossibilitaroacessodediferentesclientes,na
qualasaplicaçõesWeb,mobileeDesktopacessemafuncionalidadeemcomum.As
novasversõesdoEJBnãofocaramestaabordagem,dandomaisênfaseaosoutros
aspectosdeinfraestrutura.Hoje,umaop çãofrequentementeadotadaéexporessas
funcionalidadescomoserviçosWeb,comoserávistonoCapítulo7.
OJCPcapturoucadavezmaisastendênciasdosmercados,aprimorando-asden-
trodasJSRs;tantoqueoEJB3.0foiumagrandeevoluç ãonaplataforma,trazendo
simplicidadeeprodutividadenuncaantesvistasnoJavaEE,boapartefrutodessas
críticasanteriormenteapresentadas.Aversão3.1trouxeaindaumapequenamodi-
ficaçãodeimensaimportânciaparatodaessadiscussão:parausarEJBslocalmente,
178

## Página 199

CasadoCódigo Capítulo6. Decisõesarquiteturais
nãoprecisamosmaisnemdeinterfaceslocais. Bastaumaanotaç ãoeobeanpode
serusadoemqualquerlugardaaplicação,usufruindodosserviçosdocontainerEJB,
semacomplexidadehistóricadaplataforma.E,comosnovosrecursosdeinversão
decontroleeinje çãodedependênciasdoCDInoJavaEE6,usaressesbeanslocal-
mentecomtodososserviçosémuitosimples.
Oprimeiroaadvogarafavordeumcontainerlevedeserviçosparaobjetoslocais
foioSpring,sempremuitocríticodosEJBs. ComoJavaEE6,finalmenteaplata-
formaganhaumapadronizaçãoparaumcontainerlevedeobjetoslocaiscomEJB
3.1eCDI,resolvendomuitasdasantigascríticas.OSpring,poroutrolado,acabou
acrescentandoremotabilidade,WebServiceseoutrosrecursosàsuaplataforma.Por
caminhosedire çõesdiferentes,JavaEEeSpringseaproximarammuitoemsuasúlti-
masversões.HáquemdigaqueEJBshojesãomaisprodutivoscomsuasanotações,e
háquemprefiraosrecursosamaisdoSpring,comoAOPeintegraç ãocompequenas
outrasbibliotecas.
Masfatoéque,sevocêbuscaumcontainerlevedeobjetoscomserviçosreapro-
veitáveiseumaexcelenteimplementaçãodeIoCeDI,hojeépossívelescolherentre
JavaEE6eSpring.EJBdeixoudesersinônimoderemotabilidade.
6.5 C omunicação assíncrona
Existemoutrasmaneirasdedistribuircomportamentoentrediversaspartesdeum
sistemabuscandoescalabilidadeemaiorperformance.Emumaabordagem assín-
cronadecomunicaçãoentresistemas,atrocademensagenséfeitadetalmaneira
queosistemaqueenviaamensagemnãoprecisaesperaroprocessamentodares-
posta,ficandolivreparacontinuarsuarotina,diferentedetecnologiasdeintegraç ão
comRPC.Éumainvocaçãonãoblocante.
Acaracterísticaassíncrona,aprincipaldos middlewaresorientadosamensagem
(MOM),éumaótimaop çãoparasistemasquenecessitemexecutarrapidamenteal-
gumtipoderotinaaoserdisparadoumevento.Porexemplo,aomudaropre çode
umprodutoquandoumapromo çãoélançada,nãoéprecisoesperartodosospre ços
seremalterados;ousuáriopodecontinuarutilizandoosistemanormalmente.Situa-
çõesemquenãohánecessidadederespostadeumcomportamentoaserexecutado
sãopassíveisdeimplementaçãoviamensageriaassíncrona.
Aideiadetrocarmensagensentresistemasremotosnãoétãorecenteassim.
Desdeosanos1960,aIBMjápossuíao“IBM7740communicationcontrolsystem”,
quetrabalhavacomofluxodemensagensentresistemasremotos.[103]Masafigura
179

## Página 200

6.5. Comunicaçãoassíncrona CasadoCódigo
realdoMOMapenassetornoupopularnasdécadasde1980e1990,porcausados
produtoscomo TIBCORendevous eIBMMQSeries,quejáforneciamimplementa-
çõescompletasdeMOM.
Porém,nãohaviaumapadronizaçãoquecuidassedatrocademensagens. Os
fabricantesdeviamdarsuporteatodotipodemétodoebibliotecasdeenvioere-
cebimentodemensagensexistentes. Foinestecenárioquesurgiuaespecificaç ão
JMS.Comopraticamentetodososservidoresdemensageriapossuíaminterfacesde
comunicaçãoparecidas,assimcomoosbancosdedados,foipossívelcriarumapa-
dronizaçãodabibliotecadecomunicaç ãocomosservidoresdegerenciamentode
mensagem.
JMS–JavaMessageService,emconjuntocomdiversasoutrasespecificaçõese
frameworks,foiumdosresponsáveispelaaceitaçãodoJavacomoplataformadede-
senvolvimentocorporativo.JMScarregaconsigoasgrandesvantagensdeumMid-
dlewareOrientadoaMensagem:garantiadeentrega,controledaentrega,serassín-
cronoeescalável,tudoissonaformadeumaespecificação,comsuporteàintegração
nativacomaplataformaJavaEE.
Apósolan çamentodoJMS,muitosfabricantesdeMOMimplementaramaes-
pecificação,facilitandootrabalhodasempresasnotrabalhocommensageria.Sendo
umaespecificação,nãoimportaaimplementação,omododeenviarerecebermen-
sageméomesmo. ASunfoiapenasalíderdaespecificaç ão;quemmaispartici-
poudacriaçãodoJMSforamosprópriosfabricantes,porquenecessitavamdeuma
padronização.[164]
AestruturaplanejadanoJMSusaofatodeatrocademensagemserassíncrona
paragarantiraentregadamensagem,usandoomodelo store-and-forward.Quando
umamensageméenviadaaoMOM,primeiroelepersisteessamensagem,depoisa
repassaparaseudestino. Mesmoqueodestinonãoestejarespondendo,amensa-
gemjáestáguardada.Então,quandoelevoltararesponder,oMOMrealizaaentrega.
Essemecanismoéótimoparatrabalharcomserviçosquepodemnãoestardisponí-
veis100%dotempo.Essaconfian çatambémpodeserconfigurada;emalgunscasos
podenãosercrucialentregartodasasmensagens,ealgumasfalhasdeentregasão
aceitáveisemtrocadeumaescalabilidademuitomaior.
Comoexisteum broker(intermediário)demensagens,ossistemasacabamnão
secomunicandodiretamente;quemenviaamensagemnãoprecisasabernadasobre
quemarecebe.Estedesacoplamentoémuitousadoparaligarsistemasquenãose
conheciampreviamente;elesapenasprecisampassaraconhecero brokerdemensa-
gem,enãoumaooutro,oferecendomodularizaç ãoeflexibilidadeparaossistemas.
180

## Página 201

CasadoCódigo Capítulo6. Decisõesarquiteturais
Essasduascaracterísticassãoextremamenteimportantesparagarantiroreúsode
componentes.
Ofatodeasmensagensseremassíncronaseosistema store-and-forwardfazem
comqueasmensagenssejamprocessadasapenasnamedidadopossível,eaquelas
queaindanãoforamprocessadasficamguardadasesperandoumaoportunidade.
Mesmoquehajaumaumentodovolumedasmensagens,osenviadoresnãosofrem
nenhumimpedimentoparamandaroutrasmensagens,equemasrecebenãoperde
nenhumadelasgraçasaobroker.Aindaqueocomponentequerecebaasmensagens
nãoasestejaprocessandoemumtempoaceitável,odesacoplamentoentrequem
enviaequemrecebepermiteacrescentarmaisprocessadoresdemensagem,ouaté
mesmotrocaro brokerporummaisperformático.[165]
Modelos de Entrega
JMSdisponibilizadoismodelosdeentregamaiscomuns,o point-to-pointeo
publish-subscriber.O publish-subscriber,representadopelainterface TopicdoJMS,
usaomodeloum-para-muitosparaenviarasmensagens.Cadapublicaç ãodeuma
novamensagemfarácomqueoMOMconfiratodososqueestãoregistradospara
receberestetipodemensagem,ecadaumrecebeumacópia,àmedidaqueo broker
acharconveniente. Essemodeloérecomendadoparamensagensquepossamser
processadasporzero,umouváriosrecebedores.Casonãohajaninguémregistrado
noMOMparareceberamensagem,elaseráperdida.[166]
Pequenasmudançaspodemserfeitasnessemodelo,obtendo-seresultadosbem
diferentes.Elepodetrabalharcomgarantiadeentregaaoconfigurarum subscriber
comoum durablesubscriber;nestecaso,oservidorreteráamensagematéo dura-
blesubscriber voltararesponder. Outraconfiguraçãomuitoutilizadaéofiltrode
mensagens,noqualépossívelconfiguraroassuntodamensagemecada subscriber
aplicarumfiltro.
Jáopoint-to-pointusaomodeloum-para-umparaenviarasmensagens,eére-
presentadopelainterface QueuedoJMS.Nestemodelo,oprodutorenviaeoMOM
entregaparaapenasumconsumidor.Eletambémpodeserusadoparabalanceara
cargadeprocessamento;quandoumamensagemchegaao MOM,eleescolheapenas
umconsumidorparaprocessaramensagem,mesmoquetenhamosmaisconsumi-
doresresgitrados.[167]
AespecificaçãoJMSapenasdefineainterfacedecomunicaç ãoentreosclientes
eoservidorJMS,porém,oformatointernodamensagempodeserescolhidolivre-
mentepelasaplicações.Utilizarumformatotextotemprevalecido,mesmoquetodos
181

## Página 202

6.5. Comunicaçãoassíncrona CasadoCódigo
osparticipantessejamJava,poisevita-seutilizarobjetosserializadoscomoconteúdo
dasmensagens.MensagensXMLtambémsãoencontradas,apesardeformatosori-
entadosacolunaseremmaisabundantese,deacordocomalgumasrestriçõesno
volumededados,atémesmopreferíveis.
Aideiadetrocaassíncronanãoexcluianecessidadederesposta,hácasoemque
elaapenasnãoprecisaserimediata. Porisso,aespecificaç ãoJMSpossuirecursos
paraconfigurarparaondearespostadamensagemdeveserenviada.Essaop çãoé
muitoutilizada:emvezdeoconsumidorresponderdiretamenteparaoprodutorda
mensagem,eleencaminhaarepostaparaoutrafila,criandoumfluxodeoperações.
Umexemploseriaosistemadedisparosdee-mailsemmassa,noqual,emum
casocomum,alistacontémmilharesdedestinatários.Searequisiç ãoforesperaro
fimdoenvioparaprosseguir,elaficarábloqueadapormuitotempo. Realizaresta
tarefademaneiraassíncrona,encaixa-seperfeitamente,emespecialsenãohouvera
necessidadedesaberquandoasmensagensforamconsumidaseseose-mailsforam
devidamenteenviados.
Asvantagensestãodiretamenteligadasàrestriç ão;oprodutorestálivrepara
operardamaneiraqueacharconvenienteapósoenvio,nãoprecisandoaguardar
umarespostaparaprosseguir.Porumlado,temosoacoplamentomenorentrequem
sãoosconsumidoresequemsãoosprodutores,umavezqueasmensagensnãosão
endereçadasparamáquinasespecíficas,masaclasseeoconteúdodamensagemsão
fatoresdeumacoplamentoentreasduaspartes.
Casoosconsumidoresassumamumpadrãofixodemensagemdadaumaclasse
específica,qualquermudançanoformatodessamensagemporumprodutor(mesmo
aadiçãodeumainformaçãonova)quebraráosconsumidores.Issomostraoaltoaco-
plamentodevidoaoformatodamensagem.Seaimplementaç ãodosconsumidores
ignorainformaçõesdesconhecidas,adiçõesnamensagemnãoquebramconsumido-
resdesatualizados;éaabordagem Must-Ignore.
Asmensagensassíncronasnãoaparecemapenasno businesstier. OAjaxtira
proveitodoassincronismoparadarumausabilidademelhoràinterfaceWeb,eaté
mesmoabordagensassíncronasexistempararealizarqueriesnobancodedados,
comointerfacesanálogasaoJDBC,tendocallbacksparareceberoresultadoquando
necessário.
182

## Página 203

CasadoCódigo Capítulo6. Decisõesarquiteturais
6.6 A rquitetura contemporânea e o Cloud
Boapartedossistemasatuaisusaalgumavariaç ãodaarquitetura N-tiers,quevi-
mosnotópico6.1.Aclássicaarquiteturacliente-servidor 2-tiersapresentavadiver-
sosproblemas,entreelesadificuldadenaescalabilidadeeumadisponibilidaderuim
porcausadadependênciaaoservidorcentral.AevoluçãoparaarquiteturasWebem
3-tierssolucionoudiversasquestões,comogerenciabilidade,extensibilidadeema-
nutenibilidade.Massistemasem 3-tiersaindatêmbastantedificuldadecomescala-
bilidadeedisponibilidade.
Aevoluçãoparaarquiteturasde N-tierspermite,assim,clusterização,loadbalan-
cers,modularizaçãoemsistemas,etc.Oprincipalobjetivodestetipodearquitetura
éatacarosproblemasdeescalabilidadeedisponibilidadecomsuasdiversaspráti-
casetecnologias.EJBs,porexemplo,podemtercaracterísticasnegativasemcertos
cenários,comoumimpactoemperformance,maséinegávelquemelhoramescala-
bilidadeedisponibilidadequandobemutilizados.Ou,ainda,ousodemensageria
eJMS,umatécnicacomobjetivosfortesemmelhoraraescalabilidadeedisponibili-
dadedesistemasintegrados.Muitasvezes,preferimosescalabilidadehorizontal,em
vezdevertical,apenaspelamelhoradedisponibilidadeeescalabilidadepraticamente
infinita.
Disponibilidadecostumaserumrequisitoimportanteparaamaioriadossis-
temas,atéospequenos. Escalabilidadeéalgomaisexigidoporsistemasmaiores,
masmesmopequenasaplicaçõesestãosujeitasapicosmomentâneosdeacessooua
umcrescimentoimprevisíveldeusuários.Porém,emboraimportantesevastamente
discutidos,escalabilidadeedisponibilidadecostumamsergrandesdificuldadespara
osarquitetos.Mesmocomasdiversasferramentasdisponíveiseservidorescadavez
melhores,éprecisosepreocuparemcomomontaroclusterWebdeJettys.Ou,ainda,
dequeformaativarareplicaçãodobancodedados.Ecomoescolherospontosda
aplicaçãoquenecessitamdecachesdistribuídos? Qualdevesersuainfraestrutura
físicaparaqueelaescaleosuficienteequaisascaracterísticasdohardwareescolhido
(dimensioning)?
Sãomuitasdecisõeseumaarquiteturabastantecomplexa.Eapiorparte,talvez,
éficarnadúvidaseaaplicaçãovairealmenteaguentar. Seoconcorrentequebrar
ehouverumamigraçãoemmassadeclientesparaaempresa,osistemaescalana
velocidadenecessária? Sehouverumproblemacomodatacenter,aaplicaç ãoes-
tarádisponívelemoutrainstalação? Sefornecessárioumgrandevolumedeaces-
sosmomentâneos,consigoatenderànecessidadepontualsemdesperdíciodepois?
Seacontecerumgrandedesastrenatural,tenhoreplicaç ãoemoutracidade?Outro
183

## Página 204

6.6. ArquiteturacontemporâneaeoCloud CasadoCódigo
continente?
Resolveressasquestõesépossíveleexistemdiversastécnicasparaplanejaraca-
pacidadenecessária,mastodasbastantetrabalhosas,carasecomumapossibilidade
deerroemcasosnãoprevistos.Oarquitetoacaba,então,deixandodeladoproble-
masquejulgademenorriscoparaosistemaemquestão.Esefossepossível,porém,
teraltadisponibilidadeeescalabilidadecombaixocusto,semcomplexidadeecom
menosplanejamento?
Em 2007, o jornal americanoThe New York Timesenfrentou um desses
problemas.[86]Onovosistema TimeMachinepermitiriaaosleitoresoacessoao
acervohistóricodojornal,umtotaldemaisde11milhõesdeartigosemedições
publicadasaolongode150anos.Todoessematerialéarmazenadoemterabytesde
imagensTIFFdealtadefinição,comcadaimagemrepresentandopequenospedaços
deumapáginaimpressa.
OtrabalhoconsistiaemgerarPDFsamigáveisdessaspáginasemumaresolu-
çãorazoávelparaconsumoviaWeb.Masquantasmáquinasequantotemposeriam
necessáriosparagerarPDFspara150anosdehistóriadojornal? E,mesmoquese
chegasseaumnúmero“x”necessário,qualseriaamelhorestratégia:comprardi-
versasmáquinasparaesseusopontualedesperdiç á-lasaofimdatarefa? Ouusar
otempoociosodemáquinasjáexistentesparaevitardesperdício,masprolongando
bastanteotempodeconclusãodatarefa? Asoluç ãono NewYorkTimes foiusar
Cloud Computing.Maisespecificamente,resolveramoproblemaem24hcom100
instânciasrodandonaAmazonEC2aocustoirrisóriodealgumaspoucascentenas
dedólares.
CloudcomputingéumarevoluçãonomundodeTI,tantoqueéofocodoJavaEE
7.Seugrandeatrativoéafacilidadeparaescalartodotipodetarefacombaixocusto
esempreocupaçãocommanuten çãodaprópriainfraestrutura.Háatémesmoquem
compareessasmudançascomarevoluçãoelétricadocomeçodoséculoXX.[32]Ain-
vençãodaenergiaelétricatransformouomundonoséculoXIX,masdurantemuito
tempoesteverestritaaempresaseinstituiçõesquepodiamadquirirseuspróprios
geradores.ArevoluçãonoséculoXXfoiosurgimentodegrandesusinasgeradoras
edeumaextensaredededistribuição.Aproduçãoemaltaescaladerrubouospre ços
daenergiaeoserviçodedistribuiçãosimplificouseuuso.Aeletricidadelogosepo-
pularizouatéparafamíliasdemaisbaixarenda,jáqueoserviçoerabarato,simples
esemcomplexasinfraestruturaspróprias.E,sendoumserviço,paga-seapenaspelo
queseusa,tornandofácilocontroledeor çamentoedispensandoaltosinvestimentos
eminfraestrutura.
184

## Página 205

CasadoCódigo Capítulo6. Decisõesarquiteturais
Cloud computing é a computação como servi ço. Comoosserviçosdeener-
giaelétrica,águaencanadaoutelefonia,ocloudencaraosrecursoscomputacionais
comoserviços.Processamento,armazenamento,tráfegodedadoseoutrospassama
seroferecidospelosprovedoresdecloudparausosimplesebarato.Emvezdeman-
teraprópriainfraestruturadeservidores,temosàdisposiç ãoserviçosqueoferecem
recursoscomputacionaisdeacordocomcadanecessidade.Nãoéprecisoumgrande
investimentoinicial,easpreocupaçõescommanuten çãoegerenciamentodain-
fraestruturapraticamentedesaparecem.Épossívelescalarquasequeinfinitamente,
demaneiraelástica,usandorecursossomentequandofornecessárioeliberando-os
quandonãoforem.Evita-sedesperdícioaosepagarapenaspeloquerealmentefor
usado.Nofim,éumagrandeeconomiadecustosedoresdecabe ça.
Diversasgrandesempresasproveemserviçosdecloudcomputing,comoGoo-
gle,Microsoft,Amazon,SalesForce,RackspaceeLocaweb.Mashádiferen çasentre
osserviçosoferecidos. Algunsprovedores,maisnotadamenteaAmazon,comseu
EC2,oferecemavirtualizaçãodehardwareondeépossívelrodarmáquinasvirtuais
completas.Chamadosde IaaS(InfrastructureasaService),essesserviçosoferecem
grandeflexibilidadeparatodotipodeaplicação,masaindaexigemagerênciadetoda
acamadadesoftware,assimcomoacomunicaç ãoentretodososnós.Istopodeser
facilitadoeautomatizadoatravésdeferramentas,masestásempresobresponsabili-
dadedodesenvolvedor.
Pensandoemmaisfacilidade,diversosprovedoresdisponibilizamplataformas
completasdedesenvolvimento,abstraindonãosóohardware,comotodoogerencia-
mentodesistemaoperacional,servidorWebesoftwaresbásicos.Essesserviços,cha-
mados PaaS(PlatformasaService),sãooferecidos,porexemplo,peloGoogleApp
Engine,oVMForce,AmazonBeanStalk,HerokueMicrosoftAzure.Desenvolve-sea
aplicação,usandoasferramentasdisponibilizadaspeloprovedor,eoúnicotrabalho
éodeploynanuvem.Nãohápreocupaçãocomogerenciamentodehardwarenem
dosoftwaredeinfraestrutura,permitindoquesefoqueapenasnaaplicaç ão. Com
isso,hábastantefacilidadeparadesenvolveresubiraplicações,comescalabilidade
elástica,altadisponibilidadeepagandoapenaspelosrecursosusados.
TeroambientetodoprontoéagrandevantagemdoPaaS,maspodesertambém
suadesvantagem.Muitasvezes,édifícil,ouatéimpossível,terumcontrolefinodas
configuraçõesesoftwaresusadosnaplataforma.NoAppEngine,porexemplo,não
secontrolaonúmerodeinstânciasdaaplicação,éprecisoconfiarnosalgoritmosde
escalabilidadedaplataforma.Hátambémumasériederestriçõesemrelaçãoaquais
APIsJavapodemserutilizadas,alémdelimitaçõesaosistemadearquivos,bancode
185

## Página 206

6.6. ArquiteturacontemporâneaeoCloud CasadoCódigo
dadosecomunicaçãoentrenós,podendotornardifícilamigraç ãodeumaaplicação
quenãofoiinicialmentedesenhadaparaestetipodecloud. Épapeldoarquiteto
decidirquandodeterminadaplataformaéapropriadaparaoprojeto.
EssadesvantagemdoacoplamentocomaplataformaPaaSespecíficatornadifícil
tambémaportabilidadeparaoutrosprovedoresdecloud. Muitosserviçostentam
amenizaroproblemausandoespecificaçõesconsolidadaseportáveis,masisto,às
vezes,nãoésuficiente.NoAppEngine,oDatastore,seubancodedadosnãorelaci-
onalbaseadonoBigTabledoGoogle,ébemdiferentedeseusarcomparadoaoutros
bancosdedados.
Tentandominimizaroacoplamentocomaplataforma,éatéoferecidaumaim-
plementaçãodaJPAemcimadoDatastorecomcertaslimitações.Naprática,porém,
asdiferençaselimitaçõesdoDatastoreacabamvazandoparaaaplicaç ão,tornando
quaseimpossívelrodarumaaplicaçãonormaljáprontacomJPAsemfazermui-
tosajustes.Emboraválida,apreocupaçãocomoacoplamentocomumaplataforma
específicapodeserbastanteminimizadacomumbomdesignorientadoaobjetos.
Usandotécnicasdeseparaçãoderesponsabilidadesebomencapsulamento,épossí-
velisolaressepontonegativoeusufruirdetodasasoutrasvantagensdoPaaS.
Nãoterocontroletotaldainfraestruturatambémpodeserumproblema,mesmo
noIaaS.Detalhesdatopologiadarede,configuraç ãoespecíficadohardwareeaté
mesmoageolocalizaçãodosservidorespodemtrazersurpresasparaumaaplica-
ção.ONetfiixpossuiumdosmaisconhecidoscasosdesucessonamigraç ãoparao
AmazonEC2,[116]porém,diversosproblemascomalatênciadarede,maioremais
variávelqueaquetinhamanteriormente,for çouumacertodagranularidadedos
serviçosedoprotocoloparareduzironúmerode roundtrips.[98]
HátambémquemchameserviçosWebprontoscomoGmail, GoogleDocs,
DropboxouGitHubdecloudcomputing. Essesprodutossãochamadosde SaaS
(SoftwareasaService),esãomaisorientadosaousuáriofinal.Éaofertadeserviços
dispensandoinstalaçõeseconfigurações,facilitandoparaousuárioepermitindo
acessodequalquerlugar. Hátambémofertasdeserviçoscomputacionaisnomo-
delodeSaaS,comooPusher,umaAPIwebparaenviodemensagensdisponibilizada
comoserviçoparatodotipodeaplicações.
Aaplicabilidadedecloudcomputingébastanteextensa,emgeralcomobjetivos
deescalabilidade,disponibilidade,cortedecustosefacilidadedegerenciamento.Na
Caelum,porexemplo,oGoogleAppEngineéusadonositeprincipal,nãopormoti-
vosdeescalabilidade,jáquenãoéumsitecommuitosacessos.Mashápicospontuais
deacessoemqueovolumedeusuáriosaumentamaisde10vezesdurantealgunsmi-
186

## Página 207

CasadoCódigo Capítulo6. Decisõesarquiteturais
nutos,quandosãofeitosgrandesanúnciosoulan çamentos. Cloudcomputingnos
permiteescalarelasticamentenessesmomentosparaatenderaosnovosusuáriosde
maneiratransparenteebarata.Alémdisso,usaroAppEnginenostrouxemaisdis-
ponibilidadeeconfiabilidadesecomparadoaousodeumservidorprópriocomo
antes.Diminuiuoscustoscominfraestruturaesimplificoubastanteoprocessode
desenvolvimentoedeploy.
HáaindaoutrosexemplosnaCaelum.Umimportantesistemadaempresapos-
suiumbuildcomplicadoelongo,dadaacomplexidadedoprojetoeonúmerode
testes.Durantemuitotempo,convivemoscomasdoresdecabe çadegerenciarum
servidordeintegraçãocontínualocalmente.
Umadasquestõesmaisproblemáticaseraolongotempodebuild,queengessava
oprocessodedesenvolvimento.ComoEC2daAmazon,rodamosostestesempa-
raleloemdiversasinstânciasdoHudsoneTeamcity,agilizandobastanteoprocesso
deintegraçãocontínua.NocampodeSaaS,usaroGitHubdiminuiudrasticamente
nossosproblemascominfraestruturaeseuscustosassociados. Hádiversosoutros
cenárioseexemplosdetodotipodeempresas,semprebuscandofacilidadeparade-
senvolver,executareescalarasaplicações,alémdecortarcustoseterambientesmais
robustos,confiáveiseescaláveis.[115]
Existemcríticasequestionamentosaousodecloudcomputing. Amaiorpre-
ocupaçãocertamenteérelacionadaàseguran çaeàprivacidade. Muitasempresas
questionamseseusdadosesuaaplicaç ãoestarãoasalvoapartirdomomentoem
quesuainfraestruturaforterceirizadaedependerdeumprovedordecloud. Há
duasquestõesenvolvidas.Aprimeiraécomrelaç ãoàseguran çacontraataquesex-
ternos. Seriaainfraestruturadoprovedormaisseguraqueumasoluç ãoprópria?
Difícilsaber,maséfatoquetodososbonsprovedoresdecloudpossuemequipes
especializadasnogerenciamentodetodaessasinfraestrutura. Alémdisso,esteéo
coraçãodosnegóciosdoprovedor,eécertosuporqueseuconhecimentonessaárea
temgrandeschancesdesermaiorquedeempresascujainfraestruturaprópriaseja
apenasumsuporteparasuaatividadeprincipal.
Outropontoqueajudaagarantiraseguran çacontraataqueséaconstanteatu-
alizaçãodossoftwaresdainfraestruturausada.Quandotemosmáquinaspróprias,
énossodeveratualizarquasequediariamentenossosistemaoperacional,servidor
Web,debancodedados,etc.Naprática,éfácilverempresasdeixaremdeladooesta-
fantetrabalhodeatualizarossoftwaresconstantemente.Novamente,aousarcloud,
paramosdenospreocuparcomissoedeixamosotrabalhonamãodoprovedor,que
emgeralpossuipolíticasbastanterígidaseeficazesquantoaatualizaçõesdesegu-
187

## Página 208

6.6. ArquiteturacontemporâneaeoCloud CasadoCódigo
rança,alémdebackupseredundância.
Osegundopontodepreocupaçãocomaseguran çaécomrelaçãoaoprovedor
emsi.Podemosestarmaisseguroscontrahackersaousarcloud,masquemgarantirá
aprivacidadedosdadoscontraacessosdopróprioprovedor? Realmentenãohá
solução,anãoserescolherprovedorescomboaspolíticasdeprivacidadeeações
clarasnessadire ção,econfiarnoprovedor.Massempreháapossibilidadetécnica
deacessolocaldosdados,comoemqualqueroutroserviçoqueusamos,taiscomo
telefoniaouprovedordeinternet. Éimportantelembrarquetodonegóciodeum
provedordecloudébaseadonaconfian çadeseususuários,eelescertamentesãoos
primeirosaperseguiragarantiadeprivacidadedeseusclientes.
Umúnicoepisódiodeviolaçãodeprivacidadeinternamentenoprovedorseria
capazdequebraraempresa. Mas,claro,hácenáriosemqueosriscosenvolvendo
certosdadossigilosossãomuitograndes,eocloudcomputingclássiconãoéuma
solução. Pensandonisso,hásoluçõesdecloudsprivadosquetentamtrazeralguns
dosbenefíciosdocloudcomputingparainfraestruturasinternasdasempresas.
Outropontodepreocupaçãoédisponibilidade. Aomigrarparaumprovedor
decloud,fica-secompletamentedependentedesuadisponibilidade.Ehácasosem-
blemáticosdeproblemasnessaárea,comoagrandequedadosserviçosdaAmazon
nodatacenterdacostalesteamericanaemAbrilde2011.Durantehoras(eatédias,
emalgunscasos),diversossitesficaramforadoar,comoFoursquareeReddit.Jáou-
tros,comooNetflix,quehaviamsepreocupadocomredundânciaentredatacenters,
conseguiramsemanternoar.Masesseepisódio,juntocomdiversosoutrosmeno-
resempraticamentetodososprovedores,levantaaquestãosobreadependênciada
disponibilidadedoprovedor.
Ofatoéque100%dedisponibilidadeéutópico,sejaeminfraestruturaprópriaou
paraumprovedor.Aquestãonãoéterumsistemaquenãocainunca,masumque
rapidamenteserecuperedequedas.Eaperguntaquesedevefazeré:qualachance
daminhainfraestruturaprópriacairemcomparaç ãocomachancedealgumdos
provedoresficarindisponível.Dediversasformasdiferentes,parecequeoambiente
dealgunsdosgrandeserespeitadosprovedoresdecloudtemmaiorchancedeficar
noarqueumainfraestruturaprópria,salvotalvezrarasexce çõesdeempresascom
infraestruturasbemavan çadas.
Considerações sobre escalabilidade
Jogarumaaplicaçãoqualqueremcloudnãofuncionacomosoluç ãomágicapara
escalabilidade.Ocloudnostrazpreparadosparaescalarelasticamentetodoohard-
188

## Página 209

CasadoCódigo Capítulo6. Decisõesarquiteturais
ware,e,nocasodePaaS,aplataformadesoftware.Nãohátantapreocupaç ãocom
máquinas,softwarescomplicadosparaescalar,eatémesmoaconfiguraçãodenovos
nósdeumclusterficabastantefacilitada.Masescalabilidadeéumaquestãoarquite-
tural,eassoluçõesparaatacá-lacostumamadicionarcertacomplexidadeaoprojeto.
Nãosedeveadotarumasoluçãoarrojadadeescalabilidade,amenosqueelasetorne
necessárianaprática.[106]
Adificuldadedeseescalarumaaplicaç ãoenvolveprincipalmenteseuestado,
seusdados.Comogarantirqueosistemaaguentaovolumedeleiturasnecessário?
Comoparalelizarescritadedados?Comoreplicarospontosdeacessoadadossem
perderaconsistência?Comogarantiradisponibilidade?
Quandosefaladedados,nãoéapenassobrebancoseapersistência. Hátam-
bémoestadodosservidores,comoseusobjetosinternosouassessõesdousuário.Ao
criarumcluster,éimportantedecidircomomantê-las.Usarreplicaçãototalgarante
quetodasasmáquinasestãopreparadasparatratarrequisiçõesdequalquerusuário,
equeasinformaçõesnãoserãoperdidasquandoumamáquinacair.Mas,aomesmo
tempo,implicamumacargamuitomaiorparaosservidores,oquepodeserinviável
emclustersmuitosgrandes,mesmoqueaatualizaç ãoentreelessejafeitademaneira
assíncrona,onerandoaconsistência.Poroutrolado,existemtambémas stickyses-
sions,nasquaisomesmousuárioésempredirecionadoaummesmonó.Issotiraa
cargadareplicação,masdificultaumbalanceamentouniformedasrequisições,além
denãoevitarperdadedadosnocasodeindisponibilidade.Muitasvezes,asoluç ão
acabasendoumhíbridodessasduasabordagens,oujogarassessõesparaobanco
dedadosseestejáestivercomsuaescalabilidaderesolvida.Ou,ainda,atéchegarà
soluçãomaisextremaeterumaaplicaç ãostatelessemrelaçãoaousuário,altamente
escalável,masnemsempreviável.
Nãoétrivialescolhercomomontarumclusterdemáquinasparaobancodeda-
dosapropriadamenteparaobterleituraseescritasdeformaaganharescalabilidade
edisponibilidade,ponderandoaconsistência.Embancosrelacionaisécomumuti-
lizarumatopologia master-slave,naqualumamáquinaprincipalreplicatodoseu
conteúdoparaumoumais slaves.Enquantotodaescritaéfeitano master,porman-
terdadosidênticosemmaisdeumlugaraomesmotempo,aleiturapodeserdis-
tribuídaentretodasasoutrasmáquinas.Issoresolveoproblemademuitasleituras,
masnãoésoluçãosetivermosumgrandevolumedeescritas,alémdepossuirum
únicopontodefalhaqueafetaadisponibilidade.Háalgoritmosquesuportamescri-
tasemdiferentesnós,mashásériascomplicaçõestécnicas,principalmenteligadas
àconsistência.E,umavezqueédifícilelentoimplementartransaçõesdistribuídas,
189

## Página 210

6.6. ArquiteturacontemporâneaeoCloud CasadoCódigo
evita-sesuautilizaçãoemsistemasdegrandeescalabilidade[174](Figura6.18).
Figura6.18:Topologiamaster-slaveembancosdedados.
Àmedidaqueosdadosatingemvolumesgigantescos,torna-seinviávelmantê-
lostodosemumaúnicabase,comoumaúnicatabelaemumbancorelacional.Atu-
alizaçõesficamcadavezmaislentaseosíndicescadavezmaisineficazes.Torna-se
tambémmuitocaroreplicá-loporcompleto. Asoluçãopassaaserparticionaros
dadosemmaistabelasebancosdedados.Pode-sequebraraslinhasemtabelasdife-
rentes,algoconhecidocomoparticionamentohorizontal,ou sharding.Umadificul-
dadeécomodecidirospontosdedivisão.DevemosdividirosclientesdeA-Mem
umatabela,edeN-Zemoutra?Podenãoserumadivisãobalanceada;paraisto,há
algoritmosparaparticionardemaneiramaisdistribuídacomhashesouids.OTwit-
ter,porexemplo,utilizaoutrachavecomumdeparticionamento,adatadeinser ção
deumainformação;dadosantigossãoretornadoscomfrequênciabaixaepodemser
armazenadosemlistagensdistintas.[106]Achavevaidependerdaaplicaç ão.Outra
abordagemparaparticionamentoseriaavertical,comtabelascommenoscolunas,
quepassamaestarmaisespalhadasparadividirosdados(Figura6.19).
190

## Página 211

CasadoCódigo Capítulo6. Decisõesarquiteturais
Figura6.19:Particionamentohorizontaldedadospeladata.
Abrirmãodeconceitostradicionaisrelacionadosabancosdedadoséoutraso-
lução.Emsituaçõesdealtaescalabilidade,desnormalizarosdadospassaaseruma
opção. Issosignificaduplicardadosemdiferenteslugaresparafacilitarleiturase
sobrecarregarmenosobancodedados,mesmodificultandoaatualizaç ãodosda-
dosparaaaplicação.Ou,ainda,guardarresultadosdeagregaçõeseagrupamentos,
emvezdeusarobancoparacalculá-losdinamicamente.Emtodososcasos,háum
trade-offclaroentreescalabilidadeeumamaiorcomplexidadedomodelodedados
edocódigodaaplicaçãoparamanipulá-los.
Asoluçãomaisusadaerecomendadaparaescalabilidadeéousodecachespara
suportarmaisleituraseevitaroacessoaobancodedados. Usa-seocachedese-
gundoníveldoHibernate,comovimosnotópico6.3,ecachesdistribuídos,como
oMemcache,comestafinalidade.Emboranãoresolvamoproblemadeescalares-
crita,oscachessãoessenciaisparaescalabilidade,tendoemvistaquenamaioriadas
aplicaçõeshámaisleiturasqueescritas.
Masusarcachesoureplicaçãosemprelevantaopontodaconsistênciadosdados,
como,porexemplo,garantirquenãoseleiadadosantigos.Porém,consistênciaéum
termodifícildesedefinir.Podeserbastanteaceitávelque,depoisdeumaescrita,os
191

## Página 212

6.6. ArquiteturacontemporâneaeoCloud CasadoCódigo
dadossóestejamvisíveisparaleiturasdetodosapósalgunssegundos. Emoutras
aplicações,istoéinadmissível.Umportaldenotíciastalveznãoexijaqueasnotícias
nahomepageapare çamnoexatoinstantedesuapublicaç ão,masumsistemade
cotaçõesdabolsadevalorespodenãoterestaflexibilidade.Hásoluçõesdebancosde
dadosqueflexibilizamagarantiadeconsistênciatradicionalembancosrelacionais.
Comisso,ganha-sebastantepossibilidadeparaescalar.
Trêscaracterísticasdosbancosedasaplicaçõessãoimportantesparaescolher
aformadeabordaraescalabilidade: consistência,disponibilidadeoutolerânciaa
falhaseparticionamentos. OTeoremaCAP[26],[197]postulaquesóépossívelter
duasdessasgarantiassimultaneamente.Cabeaoarquitetoavaliarquaisdelastrarão
maisvaloràaplicação. Talconsideraçãoéaindabastantesimplista,afinal,oqueé
consistênciaparasuaaplicação?Seissosignificanãoverdadosdesatualizadosdepois
de10segundosdeumamodificaç ão,podeserpossívelatingirostrêsrequisitos.O
mesmoquestionamentoocorreparaasoutrasduascaracterísticas.
Muitosequestionahojeemdiasobrequalbancodedadosusar.Anteriormente,
bancosrelacionaiserampraticamenteobrigatórios,masocrescimentodaWebeda
necessidadedesoluçõesmaisrobustasdeescalabilidadefizeramcomquenovasop-
çõessurgissem. OmovimentoNoSQLprocuramostraroutrasabordagensaban-
cosdedadoscomsoluçõesnãorelacionais,comokey-valuestores,bancosbaseados
emgrafos,orientadosadocumentos,entreoutros. Soluçõesdecloudcomputing
sãobaseadasembancosnãorelacionais,comooBigtable,doGoogleAppEngine,
eoSimpleDB,daAmazon.Hátambémmuitosdisponíveisparauso,comoApache
HBase,MongoDB,ApacheCassandra,criadopeloFacebook,ouVoldemort,criado
peloLinkedIn.
NoGoogleAppEngine,porexemplo,háduassoluçõesdepersistênciabasea-
dasnoBigTable.[213]Seudatastorepadrãoébaseadoemreplicaçãoassíncronamas-
ter/slaveegaranteconsistência,masnãodisponibilidade. Outraop çãoéo High
ReplicationDatastore,quegarantedisponibilidade,masenfraqueceasgarantiasde
consistência,alémdesermaiscustosodeusar.Odesenvolvedorprecisaoptarpela
soluçãoqueformaisadequadaparaaaplicaç ão.Umadecisãofrequentenahorade
escolherumbancoNoSQLéabrirmãodaconsistênciaeterumsistema eventual-
menteconsistente.Abre-semãodastradicionaisgarantiasdoACIDparaadquiriro
BASE(BasisAvailable,Softstate,Eventualconsistent ).[162]
192

## Página 213

Capítulo7
IntegraçãodesistemasnaWebe
REST
Sistemassemuma APIexternavivemisoladosemsilosdedados,algocadavezmais
raro,jáqueanecessidadedeseintegrarcomoutrossistemasécrescente.Porisso,ao
desenvolverumanovaaplicação,pensa-seemcomoserásuaintegraçãocomoutras
nofuturo.
Existemdiversasop çõesdeintegraçãoparasistemasdistribuídos, cadauma
apresentandoníveisdeacoplamentoecoesãodistintos, centralizandooudistri-
buindoocontrolesobreosprocessosqueocorrem,abordagensfocadasemsistemas
homogêneosounasquaisosclientesserãoaplicaçõesdesconhecidasdeterceiros.
Amaneiraescolhidaparaintegrarossistemashojeimplicaráoscustosdemanu-
tençãodosoftwareduranteospróximosanos,portanto,talescolhadeveserfeita
analisando-seos trade-offsdecadasolução.
Entreasváriaspossibilidades,têmganhadodestaqueasquefacilitamatingirre-
quisitosnãofuncionaissemumtrabalhoextra,alémdepossibilitarumaevoluç ão

## Página 214

7.1. PrincípiosdeintegraçãodesistemasnaWeb CasadoCódigo
dosserviçosevitandoaquebradeclientes.ÉnestalinhadepensamentoqueaWeb
(comHTTPehipermídia)comoplataformaeaabordagemRESTsesobressaem.
Infraestruturajáexistente,comocachesHTTP,proxies,balanceadoreseferramen-
tasdemonitoraçõespassamafuncionarcomoummiddlewaremaistransparentee
simples.
7 .1 P rincípios de integração de sistemas na Web
Sistemasquenãoapresentampontosdeintegraçãoestãofadadosaumesfor çomuito
grandedemanutenção[175],umavezqueosmercadoscorporativoeWebcaminham
paraadivisãoderesponsabilidadesentrepequenossistemas,nacontramãodaan-
tigaabordagemcentralizadora.Doissistemasquaisquerintegradospodemservistos
comopartedeumúnicomaior,cadaumescritocomlinguagensepilhasdetecno-
logiaspossivelmentediferentes[12].Omeiodecomunicaçãoentreeleséumaspecto
fundamentalnaarquitetura.
Nopassado,apluralidadenospadrõeseprotocolosimplicavaanecessidade
de implementar diversos requisitos, como segurança, autenticação, autorização,
cache, etc., quedeviamsersuportadosemgrandepartedeles. Tanenbaumiro-
nizaqueavantagemdospadrõesconsistenaexistênciadediversospadrõespara
escolhermos[195],enquantoJohnSowadiz,emsua LawofStandards (LeidosPa-
drões),que“todavezqueumaorganiza çãodesenvolveumnovosistemacomoum
padrãoparaX,oresultadoprincipaléaamplaado çãodeumsistemamaissimples
comoorealpadrãoparaX "[188].Comotempo,surgiuanecessidadedeusodeum
protocoloparatransferênciadedadosquejásuportassenaturalmenteessesrequisi-
tosmencionados.
Hoje,oprotocolopadrãoparatrocadeinformaçõeséoHTTP.Aporta80ébem-
vindapelosfirewalls,e,aomesmotempo,existemdiversasferramentas,clientes,
servidoreseintermediáriosquesuportamoprotocolo. Muitasdessasferramentas
trazemsoluções,porexemplo,paraproblemasdeperformanceeescalabilidadeno
usodoHTTP.Alémdisso,épossíveldesenvolversistemasWebnasmaisdiversas
linguagensdeprogramação.
UtilizaroHTTPcomobaseparaacomunicaç ãofoiocaminhoencontradopelas
organizaçõesparaumanovageraçãodepadrõesdecomunicaç ão. Aevoluçãodo
usodehipermídiaedaHTTPpermitiuqueestesuperassemuitosoutrosprotocolos
inventadosparaindústriasespecíficas[168].
194

## Página 215

CasadoCódigo Capítulo7. IntegraçãodesistemasnaWebeREST
Representando os dados e as operações
DesdequeaideiadeintegrarsistemasnaWebsurgiu,parafacilitaroprocessode
desenvolvimentoeconsumodosserviços,ofocovoltou-separaautilizaçãodeXML
puro,conhecidocomo POX(plainoldXML),paraaexecuçãodechamadasremotas.
Emmuitoscasos,essesXMLssãotrocadosentreconsumidor(cliente,ou consu-
mer)eserviçoatravésderequisiçõesdotipoPOST,utilizandoumaúnicaURIpara
acesso.Noexemploaseguir,umsistemautilizaaURI /servicosparabuscarasin-
formaçõesdeumcliente,adicionandonocorpodarequisiçãoqualaopera çãoexata
queoclientedesejaexecutar:
POST /servicos HTTP/1.1
Host: arquiteturajava.com.br
Content-Type: application/xml
Content-Length: 91
<acao>
<codigo>busca_cliente</codigo>
<parametros>
<id>15</id>
</parametros>
</acao>
OexemploaseguirmostraumXMLderetorno,descrevendoumcliente:
<cliente>
<nome>Guilherme Silveira</nome>
<empresa>Loja Caelum</empresa>
</cliente>
Paraaçõescomresultados,comoacriaç ãodeumcliente,oservidorcostuma
devolveroresultadodaoperaçãodentrodocorpodaresposta,nãoutilizandoo res-
ponsecode doprotocoloHTTP,masumamensagemprópria:
HTTP/1.1 200 OK
Date: Sun, 18 Sep 2011 18:09:00 GMT
Content-type: application/XML
<resultado>OK</resultado>
Umprotocolofoiatémesmocriado,chamado XML-RPC,padronizandoestaco-
municação. Naprática,amaiorpartedossistemason-linequeutilizamXMLou
JSONnãoadotaessaespecificação,utilizandoseupróprioformatoepadrões.
195

## Página 216

7.1. PrincípiosdeintegraçãodesistemasnaWeb CasadoCódigo
Essaabordagemenvolveomínimodeutilizaç ãodoprotocoloHTTP,somente
paratunneling[168],masganhamuitonafacilidadedeimplementaç ão.Emalgumas
variações,utiliza-sequeryparameters paradecidirqualaçãoseráexecutadaouaté
mesmoparapassartambémosparâmetrosdeumarequisiç ão.
UmserviçoassimpodeserimplementadocomqualquerframeworkWebeuma
APIdeserializaçãodeXML,como XStream,noexemploaseguir,oubinding,como
oJAX-B.
@XStreamAlias(“cliente")
public class Cliente {
private String nome, empresa;
public Cliente(String nome, String empresa) {
this.nome = nome;
this.empresa = empresa;
}
public String getNome() {
return nome;
}
public String getEmpresa() {
return empresa;
}
}
XStream xstream = new XStream();
xstream.processAnnotations(Cliente.class);
Cliente cliente = new Cliente(“Guilherme Silveira",“Loja Caelum");
System.out.println(xstream.toXML(cliente));
OresultadodoexemploacimaéoXML:
<cliente>
<nome>Guilherme Silveira</nome>
<empresa>Loja Caelum</empresa>
</cliente>
Osclientesacessamosservidoresatravésde APIsHTTP,comoApacheHttpCli-
ent,enovamenteumaferramentadeserializaç ãooubinding:
196

## Página 217

CasadoCódigo Capítulo7. IntegraçãodesistemasnaWebeREST
String uri = "http://arquiteturajava.com.br/loja/cliente/7465";
HttpClient client = new DefaultHttpClient();
HttpGet get = new HttpGet(uri);
HttpResponse response = client.execute(get);
System.out.println(response.getStatusLine().getStatusCode());
HttpEntity entity = response.getEntity();
InputStream input = entity.getContent();
Cliente cliente = (Cliente) xstream.fromXML(input);
System.out.println(cliente.getNome());
HTTP
AdotandoacaracterísticadoprotocoloHTTPdequetoda URIidentificaalgo,
algunssistemasutilizamdiversas URIseumúnicométodo,emgeral POST.Emum
próximopassodeado çãodoprotocolo,diversosmétodossãoutilizadosparafaci-
litaraidentificaçãodatarefasendoexecutada,como GET,paraobterinformações,
POST,paracriar, PUT,paraalterar, DELETE,pararemover,etc. Issopermiteque
osistemacomoumtodosebeneficiedasvantagensdecadamétodoondeomesmo
foradequado,comoaocachearresultadosdeumaqueryexecutadaatravésdeuma
requisiçãoGET.
Comapopularizaçãodeoutrosformatosquefazemounãousodeschemas,
comoo JSON,diversosserviçosexpostosnaWebpassaramavisaràsimplicidade,
expressividade,ou,ainda,aumentaracompatibilidadeentreversõesdiferentesdos
serviços.
AmescladediversossistemasWebparaacriaç ãodeumnovo(mashups)foifa-
cilitadaporumanovageraçãodeferramentaseserviçosWeb. Grandepartedelas
foicriadaemcimade JSON,distribuindooconteúdodossistemaoriginais. Éco-
mumencontrarfotosdoFlickr,vídeosdoYouTube,mapasdoGoogleegruposdo
Facebooknasmaisdiversasaplicaçõeson-line,tudoissoresultadodessaintegraç ão
simplesnaWeb,vindasdasideiasde XML-RPC.
Frameworks,comoo VRaptor,apresentamconvençõesquefacilitamacriaçãode
serviçosquegeramresultadosemdiversosformatos,dandoacessoàsinformações
doprotocoloHTTPqueestedesejar.Outrassoluções,comoaespecificaç ãoJAX-RS,
queveremosadiante,suportam,semconven ções,acriaçãodetaisserviços.
197

## Página 218

7.2. Padronizações,contratosrígidoseSOAP CasadoCódigo
7 .2 P adronizações, contratos rígidos e SOAP
BaseadoemRPC,oSOAPéumenvelopequeganhouaceitaç ãoporpoderutilizar
apilhadetecnologiasquejáseencontravaonipresentenasplataformasdeprogra-
mação,comoatransferênciadeconteúdoXMLviaHTTP.Visandoàindependência
doprotocoloutilizado,asmensagenspoderiamsertransferidastambématravésde
SMTP,entreoutros,dandoumagrandeliberdadedeescolhaparaoprotocolode
“baixonível”.Aoabstrairoprotocolo,énecessáriogarantirummínimodepadroni-
zaçãosobreaoperaçãoaserexecutada,comooformatodamensagem,questõesde
segurançaecache.
Apesardageneralizaçãodaabordagem,naprática,amaiorpartedossistemas
utilizao tunnelingviaHTTP(WebServices). Masosprotocolossãoheterogêneos,
cadaumdelespossuirestriçõesefuncionalidadesdistintas,como,porexemplo,o
suportenativoaassincronismonoJMS,ouosuporteaautenticaç ão,cacheecom-
pressãonoHTTP.
Paragarantirquecaracterísticasnãocomunsatodososprotocolossejamsu-
portadasdemaneirahomogênea,foinecessáriaacriaçãodeextensõesquepadro-
nizaramcadaumadessascaracterísticas,normalmenteconfiguradasatravésdosca-
beçalhosdemensagensexistentesnoSOAP[209]. Porexemplo,nocasodeauten-
ticação,criou-seumaextensãochamada WS-Security,permitindoqueautilização
deSOAPfuncionasseindependentementedousodedeterminadoprotocolopara
tunneling.Hoje,existemdiversasextensões,como WS-Addressing,WS-Notification
eoutros[104],frequentementereferenciadasconjuntamentepelasigla WS-*(Figura
7.1).
198

## Página 219

CasadoCódigo Capítulo7. IntegraçãodesistemasnaWebeREST
Figura7.1:ExemplopossíveldestackparatrocademensagemcomSOAP.
SOAP na prática
Paraqueumserviçosejaconsumido,oclienteprecisaconhecerasdiversasestru-
turasutilizadasedisponibilizadaspelosistema,comoos schemasadotados,serviços
disponíveiseseuspontosdeacesso.Essasdefiniçõessãofeitasatravésdainterface
remotadoserviço,descrito,porsuavez,atravésdaespecificaçãodeum WSDL.
Apesardeaversão1.2,de2003,seraprimeirarecomendadapelo W3C,amaior
partedasferramentassuportasomenteaversão1.1,comonocasodoWS-BPEL
2.0[11].Oexemploaseguirmostrapartedeumarquivocompatívelcom WSDL1.1,
umadasmaneirasdedefinirospossíveis schemasoutipos:
<wsdl:types>
<s:schema elementFormDefault="qualified"
targetNamespace="http://arquiteturajava.com.br/bolsa">
<s:element name="PegarValorAtual">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1"
name="simbolo" type="s:string" />
</s:sequence>
</s:complexType>
</s:element>
199

## Página 220

7.2. Padronizações,contratosrígidoseSOAP CasadoCódigo
<s:element name="PegarValorAtualResponse">
<s:complexType>
<s:sequence>
<s:element minOccurs="1" maxOccurs="1"
name="PegarValorAtualResult" type="s:float" />
</s:sequence>
</s:complexType>
</s:element>
</s:schema>
</wsdl:types>
A definição de uma operação é feita separadamente, junto com a descri-
ção dos tipos esperados como entrada e saída. No exemplo a seguir, a ope-
ração PegaValorAtual recebe uma estruturaPegaValorAtualSoapIn e devolve
PegaValorAtualSoapOut:
<wsdl:message name="PegarValorAtualSoapIn">
<wsdl:part name="parameters" element="tns:PegarValorAtual" />
</wsdl:message>
<wsdl:message name="PegarValorAtualSoapOut">
<wsdl:part name="parameters" element="tns:PegarValorAtualResponse" />
</wsdl:message>
<wsdl:portType name="BolsaDeValoresServiceSoap">
<wsdl:operation name="PegarValorAtual">
<wsdl:input message="tns:PegarValorAtualSoapIn" />
<wsdl:output message="tns:PegarValorAtualSoapOut" />
</wsdl:operation>
</wsdl:portType>
Apesardenãosermandatório,o WSDLénormalmenteutilizadocomSOAP,e
éatagbindingda WSDLBindingExtension quedefineesseacoplamento,alémde
indicarqualoprotocoloutilizadopara tunneling:
<soap12:binding transport="http://schemas.xmlsoap.org/soap/http" />
Porfim,sãodefinidasasURIsaseremacessadas:
<wsdl:binding name="BolsaDeValoresServiceSoap12"
type="tns:BolsaDeValoresServiceSoap">
<soap12:binding transport="http://schemas.xmlsoap.org/soap/http" />
<wsdl:operation name="PegarValorAtual">
<soap12:operation style="document"
200

## Página 221

CasadoCódigo Capítulo7. IntegraçãodesistemasnaWebeREST
soapAction="http://arquiteturajava.com.br/bolsa/PegarValorAtual" />
<wsdl:input>
<soap12:body use="literal" />
</wsdl:input>
<wsdl:output>
<soap12:body use="literal" />
</wsdl:output>
</wsdl:operation>
</wsdl:binding>
<wsdl:service nam
e="BolsaDeValoresService">
<wsdl:port name="BolsaDeValoresServiceSoap12"
binding="tns:BolsaDeValoresServiceSoap12">
<soap12:address
location="http://arquiteturajava.com.br/bolsa/BolsaDeValoresService"/>
</wsdl:port>
</wsdl:service>
Odesenvolvedorpodeutilizarferramentas,comoo wsimportdoJAX-WS,para
gerarstubsqueabstraemesimplificamoacessoaosserviçosexpostosatravésde
SOAP.Esses stubscostumamserclassesquedelegaminvocaçõesparabibliotecas
HTTPacessaremoserviço.Oresultadoéacriaçãodedezenasdeclasses,quema-
peiamessasdefiniçõesparaestruturasdedadosdalinguagemescolhida,comovalue
objectseentidades.Mudan çasnoWSDLimplicamanecessidadedereanáliseepro-
vávelnovageraçãode stubs.
@WebService
public class PagamentoService {
@WebMethod
@WebResult(name="pagamentos")
public List<Pagamento> getPagamentosPorCliente(
@WebParam(name="cliente") Cliente cliente) {
List<Pagamento> pagamentos = //lógica
return pagamentos;
}
}
Sobre a adoção do SOAP
Aexistênciadetantasextensõesrefor çaaideiadequeSOAPdeixoudeladopon-
201

## Página 222

7.2. Padronizações,contratosrígidoseSOAP CasadoCódigo
tosqueoprotocoloHTTPjásuportara.Cadaabstraç ãointroduzidaatravésdeuma
extensãoaumentaacomplexidadedosistema,portanto,desenvolvedoresearquite-
tosdevempesarobenefíciodessasdecisõescontraadesvantagemqueelasapresen-
tam.
SegundoJamesSnell,quefoiresponsávelporpartedessastecnologiasquando
naMicrosoft,“SOAPcomeçoucomumcaminhosimplesediretoparafazerRPCcom
tunnelingviaHTTP,comummeroPOST,mascresceuparasuportarnomesdemé-
todosemheaders"[187].SegundoStefanTilkov,oWS-*come çoucomumpequena
pilhadepadronizaçõesecresceuparaumaltonúmerodecomplexasespecificações,
quedificultamautilizaçãodatecnologia[202]. Historicamente,umaevoluçãoso-
breosmodelosdeintegraçãodesistemasanteriores,oSOAP,apósmaisde10anos
deexistência,apresentahojealtoscustosetemsemostradodedifícilmanuten ção
devidoàaltacomplexidadeeàabstraç ãodoprotocoloutilizado.
Omercadotemvistocomcadavezmaiscautelaaado çãodeSOAPcomoso-
luçãotécnica,especialmentecomparando-oàpossibilidadedeutilizaraWebcomo
plataformadeintegração. OGoogle,porexemplo,abandonouabuscaatravésde
SOAPem2009[198].StefanTilkovdizque“nomomentoatual,asvantagenstécnicas
deixaramdevalerapena,somenterecomendamosousodeWebservicestradicionais
viaSOAPquandoquestõespolíticasestãoenvolvidas,como,porexemplo,acessoaum
sistemaSAPquejápossuioservi çodisponibilizado"[200].JamesSnell,enquantotra-
balhavanaMicrosoft,desenvolvendoWS-*,diss:“nuncatrabalheiemumaaplicação
queresolvesseumanecessidaderealdenegócioe,agora,trabalhandojuntoadeze-
nasdemilharesdedesenvolvedoresdaIBM,nuncapasseiporumasituaç ãoonde
WS-*fosseumasoluçãoqueseencaixasse"[105].
Natentativaderesolverpartedosproblemas,aversão1.2doSOAP[210]seapro-
ximamaisdoprotocoloHTTP,deixandodeutilizá-losomentepara tunneling,ou
execuçãodechamadasRPC.Taismudan ças,comoosuporteamétodosquenãoso-
menteoPOST,facilitaramautilizaçãodelayersintermediários,como,porexemplo,
cache,atravésdosheadersHTTP.
Muitasferramentasnãosuportamounãoencorajamosdesenvolvedoresauti-
lizarosdetalhesdasversõesmaisnovasdoSOAP,consequentementeperdendoas
vantagensdautilizaçãodoHTTP.OmercadoqueutilizaWS-*aindanãoadotou
taismudanças,limitandoousodoprotocolo.Omapeamentoaoprotocoloaindaé
muitosuperficial,eaimagemdequeomesmodeveserusadoparaRPCsemantém:
“UmdosobjetivosdodesigndoSOAPéencapsularefazerchamadasRPCusandoa
extensibilidadeeflexibilidadedoXML”[210].
202

## Página 223

CasadoCódigo Capítulo7. IntegraçãodesistemasnaWebeREST
7 .3 E vite quebrar compatibilidade em seus serviços
Partedosegredodobaixocustodemanuten çãoestáemmanteracoesãoediminuir
oacoplamentoentrepartesdeumsistema. Aoaplicaresteconceitonaintegraç ão
entredoissistemas,osmesmosdevemminimizarospontosdeacoplamentopara
maximizaracapacidadedemudan çasemquebradecompatibilidade. Oprocesso
decriarumanovaversãodeumserviçoéchamadoversionamento(versioning ),e
podeounãomantercompatibilidadecomasanteriores. Umaimplementaç ãoque
obrigaaatualizaçãodeclientestodavezqueumanovaversãodoserviçoélan çada
apresentaaltoníveldeacoplamentoealtocustodemanuten ção.
Quantomaisgenéricososclientes,menoroacoplamentocomumserviçoespe-
cíficoe,portanto,menoranecessidadedemanuten çãodosmesmos,dadaumaatu-
alizaçãodoservidoracessado.Diversastécnicaspodemseraplicadasemqualquer
tipodeintegraçãodesistemasevisamminimizaranecessidadedessasatualizações.
V alidação de estrutura e esquemas
Aoreceberosdadosdeumoutrosistema,épossívelvalidarsuaestruturapor
completo,comumcontrolemaisrígidosobreoqueaoutrapontapodefazer.Nessas
situaçõesextremas,validam-seatémesmoosdadosquenãoserãoutilizados,mas
descartados. UmexemplodetalabordagemsurgeaovalidarumXMLcontraum
schemacompleto,mesmoutilizandosomenteumapartedoconteúdorecebido.
Oexemploaseguirmostraumschemaquedefineumaestruturapararepresen-
tarordensdecompra,incluindoodestinoeumalistadeprodutos:
<?xml version="1.0" encoding="iso-8859-1" ?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
<xs:element name="compra">
<xs:complexType>
<xs:sequence>
<xs:element name="cliente" use="required">
<xs:complexType>
<xs:sequence>
<xs:element name="id" type="xs:string"/>
<xs:element name="nome" type="xs:string"/>
<xs:element name="dataDeNascimento" type="xs:string"/>
</xs:sequence>
</xs:complexType>
</xs:element>
203

## Página 224

7.3. Evitequebrarcompatibilidadeemseusserviços CasadoCódigo
<xs:element name="produto" maxOccurs="unbounded">
<xs:complexType>
<xs:sequence>
<xs:element name="id" type="xs:string"/>
<xs:element name="quantidade" type="xs:positiveInteger"/>
<xs:element name="preco" type="xs:decimal"/>
</xs:sequence>
</xs:complexType>
</xs:element>
</xs:sequence>
</xs:complexType>
</xs:element>
</xs:schema>
Alémdavalidaçãocompletacontraoesquema,umaferramentadebindingque
nãoignoracamposdesconhecidosimplicaomesmotipodeacoplamento;qualquer
mudançanoesquemalevaànecessidadedeatualizaç ãodetodaabasedeclientes.
Nessescasos,umcamponovoadicionadoemumarepresentaç ãoXMLquebraa
compatibilidade,poisquemosconsomenãoesperavaessenovovalor.Oproblema
surgequandoosclientessãoacopladosaumcontratofixo,umaestruturacompletae
imutável.Schemassãomaneirasdegarantirumaestrutura,masseusclientesdevem
minimizaroacoplamento,permitindoaomáximosuaevolução.
Oexemploaseguirmostraumapossívelevoluç ãodo schema,adicionandoum
camponovo,contendooCPFdoclienteeremovendoadatadenascimento:
<xs:element name="cliente" use="required">
<xs:complexType>
<xs:sequence>
<xs:element name="id" type="xs:string" />
<xs:element name="nome" type="xs:string" />
<xs:element name="cpf" type="xs:string" />
</xs:sequence>
</xs:complexType>
</xs:element>
UmaaplicaçãotradicionalvalidaráocampodataDeNascimentoindependente-
menteseesteforounãoutilizado.Asclassesgeradastambémpossuirãoumcampo
paraa dataDeNascimento.Porisso,oresultadodaremo çãodessecampoéumerro
devalidação,eaquebradaaplicaç ão.Umavezqueelanãoutilizavaosdados,mas
deixoudefuncionar,esseacoplamentoaumadefiniç ãorígidaédesnecessário.
204

## Página 225

CasadoCódigo Capítulo7. IntegraçãodesistemasnaWebeREST
ÉimportantevalidarsomenteapartedoXMLqueseráutilizada,ignorando
quaisquermudançasdeestruturanaquiloquenãoénecessário. Éprecisoseguir
àriscao schemanomomentodegerarosdadosaseremenviados.Seguindoessas
duasregras,asaplicaçõesclientepossuemasgarantiasnecessárias,mantendoum
acoplamentomaisflexívelaocontrato.
OWSDL,porexemplo,nãoobriga,masincentivaavalidaç ãocompletaatravés
deschemas,reforçandoesseacoplamento.
Paraexecutarvalidaçõesparciaisépossívelutilizarferramentascomoo Re-
laxNG,pelaqualoservidorserácapazdeadicionarouremoverdadossemquebrar
todososclientesexistentes. Emvezdeumaconsequênciatãonegativa,somente
aquelesclientesqueutilizavamcamposremovidosprecisarãoseratualizados.Estaé
abasedopadrão MustIgnore,criadoporDavidOrchardem2003[150],quedescreve
práticasparafacilitaraevoluçãodeum schemaXML,assuntotambémmencionado
porIanRobinson,compráticasvoltadasa backwardeforwardcompatibility[55].Es-
saspráticaspodemserutilizadascomqualquertipodeserviçoqueconsumamen-
sagensvalidáveisatravésdeumschema.
Háaindaformatosmaisamigáveisàevoluçãodoschema,comoo protocolbuffers
(application/x-protobuf),criadopeloGoogle[84].Paranãoquebrarosclientes,
elessãocapazesdefornecervalorespadrãoparacamposqueforamremovidos. O
exemploaseguirmostraadefiniç ãodeumesquemademensagemdeclientecom
umcamponomeepais,ondeopaíspadrãoéBrasil.Casoemumanovaversãodo
sistemaumcamponãosejaenviado,bastaalteraroesquemaparadefinirumvalor
padrão,podendoassimmanteracompatibilidadecomversõesanteriores.
message Cliente {
required string nome = 1;
optional string pais = 2 [default = “brasil"];
}
Mantendo diversas versões incompatíveis no ar
Emalgunsmomentos,énecessárioquebraracompatibilidadecomaversãoan-
terior,eficadifícilminimizarocustodemanuten çãodaquelesquejáconsomem
osserviços. ÉpossívelcriarnovasURIsdeacessoparacadareleasedeversãoin-
compatíveldoserviço.Destamaneira,durante,porexemplo,doisanos,oservidor
secomprometeamantercompatibilidadenoconjuntodeserviçosexpostos,e,após
essetempo,estesjáestarãosubstituídoseserãoremovidos,permitindoqueoscli-
entesfaçamsuasalteraçõesemciclosmaiores.Estaabordagem,apesardealiviaro
205

## Página 226

7.4. PrincípiosdoSOA CasadoCódigo
custonamanutençãonosclientes,nãoremoveanecessidadedesuaadaptaç ãoacada
ciclodeversionamento.
7 .4 P rincípios doSOA
Apósanosdediscussãosobreoqueseriaexatamenteumaarquiteturaorientadaa
serviços(SOA),evindodeumadécadaquandoaado çãodeSOAPeraconsiderada
aúnicasoluçãoparaessaarquitetura,em2009foicriadoo SOAManifesto[56],um
conjuntodecaracterísticasimportantesparaessetipodearquiteturabaseadonavi-
sãodomercadonaquelemomento.SegundooSOAManifesto,épossívelimplemen-
tarumaarquiteturaemcimadeCORBA,SOAP,DCOM,REST,etc.
Nessalinhado SOA,agranularidadedosserviçosdevepermitiroreúsopor
diversos clientes, além da criação de novos serviços através da composição de
outros. Por exemplo, para completar um processo (workflow) de compra, ser-
viços são pensados como funções que atingem pequenos objetivos dentro do
fluxo,como PesquisarProdutos, CriarCompra, AlterarCompra, CancelarCompra,
AlterarDestino, VerificarCompra. OsWebServicesdaAmazon,porexemplo,
apresentamessetipodegranularidade,comonocasoda ProductAdvertisingAPI,
queforneceacessoàbuscadeprodutosnocatálogointerno. Porpossuíremuma
granularidademenor,épossívelreutilizaressesserviçosemdiversostiposdeaplica-
tivos,desdeumsistemaDesktopquemostraorastreamentodesuascompras,pas-
sandoporpluginsparacalendários,quemostramadataesperadadechegadadaen-
trega,atéclientesqueautomatizamcompras,comolivrosparacolecionadoresque
estãocomopre çoabaixodomercado(Figura7.2).
206

## Página 227

CasadoCódigo Capítulo7. IntegraçãodesistemasnaWebeREST
Figura7.2:Umserviçoderastreamentodecomprascompostodautilizaç ãodedi-
versosoutrosserviços,namesmaouemoutrasmáquinas.
Éimportantequesejapossíveldescobrirdetalhessobreoserviço,alémdeutili-
zarcontratosformaisqueosdescrevam,como,porexemplo,SOAPatravésde WSDL
eschemasxml.Osserviçosabstraemdeseusclientesosdetalhesinternosdesuasim-
plementações,funcionandocomoainterfacedecomunicação,encapsulandosiste-
maseprocessospossivelmentepreexistentes.Porfim,serviçosimplementadoscom
asideiasdeSOAapresentammaisbenefíciosparaaaplicaç ãoquandonãomantêm
nenhumainformaçãodoclienteatualnoservidor,apesardenãoserumrequeri-
mentoparaodesenvolvimentodosistema.
Componha serviços
Umavezquecentenasdeserviçosestarãoexpostos,énecessáriocontrolarcomo
seráfeitaainteraçãoentreeles. Acriaçãodenovossistemaseserviçosbaseados
naquelespreexistentespodeserfeitaatravésdeumcódigoqueacessaecontrolatodo
ofluxo(orquestra, orchestration)deumgrandeprocesso(um workflow).
AFigura7.3exemplificaumpedidodecompra,noqualháumprocessodeor-
çamentocomdiversosfornecedoresexternos,abuscadomaisbaratoentreeleseo
207

## Página 228

7.4. PrincípiosdoSOA CasadoCódigo
pedidoparaliberaçãodeverba.
Figura7.3:Exemplodeprocessodepedidodecompra.
Oexemploaseguirmostracomoépossíveldescreverumprocessodepedidode
compraporumusuáriocujoor çamentoseráfeitocomdiversosfornecedores:
Pedido pedido = comprador.pede(produtos);
List<Orcamento> orcamentos = new ArrayList<Orcamento>();
for (Fornecedor fornecedor : fornecedores) {
orcamentos.add(fornecedor.getOrcamento(pedido));
}
Omenoror çamentoéescolhidoeopedidodeaprovaç ão,enviadoparaores-
ponsável. Quandoessepedidoérespondido,um callbackéfeitoassincronamente
parao OrcamentoAnalisado:
Comparator<Orcamento> comparador = new MaisBaratoComparator();
Orcamento orcamento = Collections.min(orcamentos, comparador);
double valor = orcamento.getValor();
Usuario responsavel = comprador.responsavelPorAprovacaoPara(valor);
responsavel.pedeAprovacao(orcamento, new OrcamentoAnalisado());
Esteprimeiropasso,quedescreveofluxodecompra,podeserescritodemaneira
genérica:
208

## Página 229

CasadoCódigo Capítulo7. IntegraçãodesistemasnaWebeREST
public class PedidoDeCompra implements Passo {
private final List<Fornecedor> fornecedores;
public PedidoDeCompra(List<Fornecedor> fornecedores) {
this.fornecedores = fornecedores;
}
public void executa(Map<String, Object> args) {
Usuario comprador = (Usuario) args.get(“comprador");
Produtos produtos = (Produtos) args.get(“produtos");
Pedido pedido = comprador.pede(produtos);
List<Orcamento> orcamentos = new ArrayList<Orcamento>();
for (Fornecedor fornecedor : fornecedores) {
orcamentos.add(fornecedor.getOrcamento(pedido));
}
Comparator<Orcamento> comparador = new MaisBaratoComparator();
Orcamento orcamento = Collections.min(orcamentos, comparador);
double valor = orcamento.getValor();
Usuario usuario = comprador.responsavelPorAprovacaoPara(valor);
usuario.pedeAprovacao(orcamento, new OrcamentoAnalisado());
}
}
Apósoresponsáveltomarumaação,aprovandoourecusandooor çamento,o
processocontinua,finalmenteefetuandoopedidodevendaounotificandoseucan-
celamento.
public class OrcamentoAnalisado implements Passo {
private final Emails emails;
public OrcamentoAnalisado(Emails emails) {
this.emails = emails;
}
public void executa(Map<String, Object> args) {
Confirmacao resposta = (Confirmacao) args.get(“resposta");
209

## Página 230

7.4. PrincípiosdoSOA CasadoCódigo
if (resposta.isPositiva()) {
resposta.getOrcamento().executa();
} else {
emails.notificaRecusa(resposta.getPedido());
}
}
}
Diversascaracterísticasdofluxodescritoanteriormentesãopadrõescomuns
(comoos EnterpriseIntegrationPatterns)[99]queaparecemaodescreverproces-
sosdeintegraçãodesistemas.Ferramentas,comooApacheCamel,implementam
APIsbaseadasem methodchainingouXMLparatrabalharcomessesprocessos.Por
exemplo,oconteúdodolaçoforpoderiaserexecutadoemparalelo(padrãocha-
madodeSplitter),easrespostasdevemseraguardadasparaentãoseremcombinadas
(Agregator).
Comalgumastécnicasdedesign,oexemploanteriorpodeserencapsuladoem
umaDSL,reforçandoovocabuláriododomínioutilizado:
public class PedidoDeCompra {
private final List<Fornecedor> fornecedores;
public PedidoDeCompra(List<Fornecedor> fornecedores) {
this.fornecedores = fornecedores;
}
public void compra(Usuario comprador, List<Produto> produtos) {
Pedido pedido = comprador.pede(produtos);
Orcamento orcamento = fornecedores.quota(pedido, maisBarato());
comprador.confirma(orcamento).em(OrcamentoAnalisado.class);
}
}
public interface CallBack<T> {
void processa(T argumento);
}
public class OrcamentoAnalisado implements CallBack<Confirmacao> {
210

## Página 231

CasadoCódigo Capítulo7. IntegraçãodesistemasnaWebeREST
private final Emails emails;
public OrcamentoAnalisado(Emails emails) {
this.emails = emails;
}
public void processa(Confirmacao resposta) {
resposta.executaOrcamento(emails);
}
}
Organizarecoordenarasequênciadetrocadeinformaçõesentreserviçosatravés
deumpontodecódigoúnicoéopapeldeumorquestrador.Umavezquetodosos
serviçosestãodescritos,aengineresponsávelpelatrocademensagens(enterprise
servicebus,ou ESB)coordenatudooqueseráfeitoduranteaexecuçãode workflows.
Emcasodefalha,éresponsabilidadedosistemacentralmitigaroriscoenvol-
vido,porexemplo,tentandonovamenteapósdeterminadoperíododetempo.Esse
sistemapodeserencarregadodeexecutarrequisiçõesadiversosserviçosemparalelo
eaguardararespostaparaentãocontinuarnofluxo,entreoutrastarefas.Fornece-
doresdeferramentasesoluçõesSOAapresentamprodutosqueorquestramserviços,
visandofacilitaracriaçãoemanuten çãodeaplicaçõesquecentralizamocontroledo
processo.
Paraumsistemaquesejacompostopormaisdeumserviçodistinto,comoa
reservadehoteleadevoo,cadaumhospedadoemempresaseservidoresdiferentes,
éimportanteencontrarumasoluçãoquecoordeneoscasosdefalha. Dispararas
duasrequisiçõesemparaleloaceleraofluxo,masocontroledefalhanareservado
vooapósaconfirmaçãodohoteldeveserimplementadodemaneiraacancelaro
hotel.Transaçõesdistribuídascomoessaspossuemosproblemasdeconsistênciae
integridadenaturaisdessaarquitetura,eferramentascomoasdeorquestraç ão,junto
comosdiversospadrõesWS-*,podemajudaralidarcomeles,adicionandocerta
complexidade.
Serviçospodemsercompostosprogramaticamenteouatravésdeferramentas.
Nãoéaado çãodeumprodutodeorquestraçãooudegeraçãodecódigoquetraráo
sucessoaumaarquiteturaorientadaaserviços,mas,sim,suacompreensãotécnica
esuaado çãonomomentoadequado.
211

## Página 232

7.5. REST:arquiteturadistribuídabaseadaemhipermídia CasadoCódigo
7 .5 REST: arquitetura distribuída baseada em hi-
permídia
Naabordagemorientadaaserviçostradicional,atendênciaéfor çarosdesenvolve-
doresacriaremmúltiplasoperações,alémdediversostiposdedados.Porexemplo,
umsistemasimples,comtiposrepresentandoclientes,compras,produtosepaga-
mentos,possuitambémdiversosserviços,comomostraaFigura7.4.
Cadaumdosserviçospossuisóumendere ço,sóumaURIatravésdaqualpode
seracessado.
Épossívelalteraressaformadeexposiç ãodosistemaaodisponibilizarmaisen-
dereços,emgeralumaURIparacadaentidade(recurso),mascomumnúmeroli-
mitadodeoperações. Cadaoperaçãopassaatrabalharcomumrecursoespecífico
atravésdesuarepresentação,aumentandoacapilaridade.AFigura7.5ébaseadaem
umsimilardeStefanTilkov,quetentadescrevertaisdiferen ças[201].
Figura7.4:Tipos,operaçõeseendere çosemumaabordagemorientadaaServiços.
Figura7.5:Tipos,operaçõeseendere çosemumaarquiteturaREST.
Cadaumdessesdadoséconsideradoumrecurso(resource),algointangíveldire-
tamente,queseráacessadoemanipuladoatravésdesuasrepresentações(representa-
tion).Porexemplo,umpedidodecompraéumrecurso,quepodeserencontradoem
umendereço(address),naURIhttp://arquiteturajava.com.br/loja/compras/1535434,
representadoatravésdeumXML.
212

## Página 233

CasadoCódigo Capítulo7. IntegraçãodesistemasnaWebeREST
Acomunicaçãoestásendofeitaentreclienteseservidoresatravésderepresen-
taçõesdessesrecursos,oqueformaabasedeumaarquiteturaorientadaarecursos
(ResourceOrientedArchitecture–ROA)[199][169].Aadoçãodestaarquiteturajunto
aoutrascaracterísticas,comousodeumainterfaceuniforme,stateless,navegaç ão
entreseusrecursoseestadosatravésdecontrolescomoosdehipermídia(HATE-
OAS)[59],caracterizaumaarquiteturaREST(RepresentationalStateTransfer )[211].
Sendoassim,RESTpodeseralcan çadoatravésde,porexemplo,HTTPerepre-
sentaçõescomsuporteahipermídia,maspoderiaserutilizadaoutrapilhadetecno-
logiascomasmesmascaracterísticas.Avantagemdaado çãodoHTTPjuntamente
comXMLouJSONestánaonipresen çadessastecnologias.Apartirdeagora,assu-
miremosaimplementaçãodeumaarquiteturadistribuídabaseadaemhipermídia
emcimadoprotocoloHTTP.
Ainterfacedecomunicação(uniforminterface)doRESTtambémrequerautili-
zaçãodemensagensautodescritivas,istoé,qualquerintermediário(comoumproxy)
écapazdeentenderainten çãodeumamensagemetomarumaaç ãodeacordo.
AinteraçãoentreumclienteeoservidoratravésdeRESTinicia-seatravésde
umpontodeentrada(entry-point ),umaURIquepermiteacessarorestodosistema.
Essenovoacessoérealizadoatravésdecontroles,comosimpleslinks:
<loja>
<nome>Loja de livros</name>
<horarioDeFuncionamento>10:00-22:00</horarioDeFuncionamento>
<link rel="clientes" href="/clientes" />
<link rel="produtos" href="/produtos/guia_completo" />
</loja>
Elescostumamdescreverorelacionamentoentreorecursoacessadoeoutros
atravésdoatributorel,alémdoendereçopresenteemhref.Resultadosderequisições
podemsercacheadospelocliente,proxieseatémesmopeloservidor,diminuindo
consumoderecursos[3].
Terumagranularidadepequenacomorespostanãodevesermotivadoporeco-
nomiadebanda,jáqueumarepresentaçãomaior,contendomaisinformações,tam-
bémpodesercacheada.Usandodiversosheaders[147],épossíveldiminuirdrastica-
menteonúmeroderequisiçõese/ouabandaconsumida[75].
OJAX-RSéaespecificaçãodoJavaparaserviçosWebREST,epodeserutilizada
juntamentecomoutrastecnologiasdoJavaEE,comofazerintegraç ãocomEJBs.
UsandoJAX-RSépossíveldescreverasoperaçõesdecriaremostrarumplanode
saúde,comonocódigoaseguir:
213

## Página 234

7.5. REST:arquiteturadistribuídabaseadaemhipermídia CasadoCódigo
@Path(“/planos")
public class PlanoDeSaudeResource {
@GET
@Path(“/{planoId}")
@Produces(“application/xml")
public Plano mostrar(@PathParam(“planoId") String planoId) {
// busca o plano
}
@POST
@Consumes(“application/xml")
public void criar(JAXBElement<Plano> plano) {
// armazena o plano
}
}
Comisso,aoexecutarumGETem /planos/15,avariável planoIdpassaater
ovalor15,eométodomostraréresponsávelpordevolverum Planoqueseráse-
rializadoemXMLdeacordocomsuasanotações JAX-B.FazendoumPOSTpara
/planoseenviandoumXMLnocorpodarequisiç ão,esteserádesserializadopara
umJAXBElement<Plano>.
Essa primeira geração de ferramentas focadas em REST, incluindo oJersey,
abordasomenteosaspectosligadosaoprotocoloHTTP[203],comomencionado
porLeonardRichardsonemsuaclassificaç ãodeserviçosWeb.5Aversão2daes-
pecificaçãoJAX-RSatendeaosquesitosdeAPIclienteesuporteahipermídia[33].
Frameworks,como VRaptor,RestfulieeRestlet,suportamnativamenteautilização
decontroleshipermídiacomoomeiodeinteraç ãocomoservidor.
Clientes e hipermídia
Noexemplodeclienteseordens,ocódigoaseguirutilizao Restfulieparaacessar
oentrypointdaloja:
Response response = Restfulie.at(“http://arquiteturajava.com.br/loja")
.accepts(“application/xml").get();
System.out.println(response.getCode());
System.out.println(response.getBody());
Épossíveltambémqueabibliotecaadotadaforne çaumaAPIdealtonívelpara
deserializaçãoeinterpretaçãodoconteúdoexistentedentrodeumarepresentaç ão:
214

## Página 235

CasadoCódigo Capítulo7. IntegraçãodesistemasnaWebeREST
String uri = “http://arquiteturajava.com.br/loja/clientes/15";
Response response = Restfulie.at(uri).accepts(“application/xml").get();
Cliente cliente = response.getResource();
Neste exemplo, o cliente conhece um modelo/padrão de URIs (URI tem-
plate)[53],queidentificaumconjuntodeURIs. AsURIsadotadaspodemserin-
formativasparaqueumserhumanoacompreenda[2],masbasear-seempadrões
comohttp://arquiteturajava.com.br/loja/clientes/$idtornariaosclientesaindamais
acopladosaoserviço.
Sendoassim,oclientedeveconhecersomenteaentradadosistema,oseu entry-
point.Apartirdesteponto,oservidordiráaoclientequaisoutrosrecursospoderá
acessaratravésde,porexemplo,umlink.Umlinkpossuiumvalorsemântico,um
significado,quedescreveorelacionamentoentreorecursoatualeaquelequeserá
atingidoaoacessá-lo.Linkssãoexemplosdecontroleshipermídia[59],umamarca-
çãoqueconectadoisrecursosdentrodeumarededemaneiranãolinear[144].
NasabordagenstradicionaisdeserviçosWeb,requisiçõesretornamXMLou
JSON,cujoconteúdoécompostosomentepelosdadosacessados.Seguindooscon-
ceitosdeSOA,umprimeiroserviçoécriadoparaabuscadeclientes,umsegundo
parapermitirefetuarpagamentos,assimcomoumterceiropararetornaralistade
serviçoscontratadoseativosdedeterminadocliente.
NaimplementaçãotradicionaldeSOAP,serianecessárioqueoclienteconhe-
cessedeantemão(early-binding )todasasURIsqueacessará,escrevendoasmesmas
dentrodocódigo,decisõesem designtime.Tomandocomoexemploapesquisade
umcliente,oXMLaseguirrepresentaumpossívelretorno:
<cliente>
<nome>José Beltrano</nome>
<empresa>Loja Caelum</empresa>
</cliente>
Nestecaso,nãohácomosaberqualURIacessar,nemquaisparâmetrosenviar,
paraobterospagamentosefetuadoseserviçoscontratadosporessecliente.Opro-
blemaficaaindamaiscomplicadoaotentardescobrircomoexecutartarefasdees-
crita,comoefetuarumnovopagamento.
NaWebhumana,édiferente. Cadarequisiçãonãoretornaapenasosdados(o
HTMLemsi)eaestruturautilizada(oesquemadeumHTML),mastambémele-
mentoscomolinkseformuláriosquepermitemaoclientenavegarpelosistema,pas-
sandodeumapáginaaoutraparaatingirseuobjetivo.Essasformasdeinteraç ãocom
215

## Página 236

7.5. REST:arquiteturadistribuídabaseadaemhipermídia CasadoCódigo
oservidorpodemmudaracadarequisiç ão–novoslinks,URIsquemudam,etc.Es-
saspáginasnãopossuemapenasumarepresentaçãodorecurso,mastambémdados
paracontrolarofluxodoclientenaaplicaç ão(dadosdecontrole, controldata).
Arepresentaçãodeumclientequeutilizalinkscomocontrolehipermídiapode
serfeitaemdiversosformatosderepresentaç ão,comoemHTML:
<html>
<body>
<div class="cliente">
<span class="nome">Guilherme Silveira</span>,
<span class="empresa">Loja Caelum</span>
</div>
<div class="navegacao">
<a href="/cliente/7453687/pagamentos">pagamentos</a> |
<a href="/cliente/7453687/servicos">serviços</a> |
</div>
</body>
</html>
Umclientegenérico,comoumnavegador,écapazdeapresentaroresultadopara
ocliente,quetomaráadecisãodequalpassoseguiratravésdoscontrolespresentes.
Quandoaempresadecidirqueémelhorcontrolarospagamentosatravésdeumou-
trofornecedor,serásuficientealteraraURI(href )paraaqualoslinksapontam.Uma
vezqueotipoderelacionamentoentreosdoisrecursoséomesmo,oslinksainda
representamospagamentoseosserviçosdessecliente,quecontinuamfuncionando.
Emcasosextremos,atémesmooformatodamensagemtrocadapoderiamudar,um
problemaresolvidoatravésde mediatypes.
Aintegraçãodesistemasviahipermídiautilizaessescontrolesparabeneficiar
projetosquetambémfazemacomunicaçãomáquina-a-máquina[54].Substituindo
oHTMLporXML,oresultadodabuscaficacomonoexemploaseguir:
<cliente>
<nome>Guilherme Silveira</nome>
<empresa>Loja Caelum</empresa>
<link rel="pagamentos" href="/cliente/745368/pagamentos" />
<link rel="pagamentos-form" href="/cliente/745368/pagamentos-form" />
<link rel="servicos" href="/cliente/745368/servicos" />
</cliente>
Paragerarumrecursocomoeste,épossívelutilizarumatemplateenginequal-
216

## Página 237

CasadoCódigo Capítulo7. IntegraçãodesistemasnaWebeREST
queroumaneirasprogramáticasdeconfiguraroscontroleshipermídia,comoase-
guir,nocasodoRestfulie:
@Get
@Path(“/cliente/{cliente.id}")
public void mostra(Cliente cliente) {
ConfigurableHypermediaResource recurso;
recurso = restfulie.enhance(database.busca(cliente));
recurso.relation(“pagamentos")
.uses(PagamentosController.class).lista(cliente);
recurso.relation(“pagamentos-form")
.uses(PagamentosController.class).form(cliente);
recurso.relation(“servicos")
.uses(ServicosController.class).lista(cliente);
result.use(representation()).from(resource, “cliente").serialize();
}
UmasegundarequisiçãoGETpermiteentãorecuperarosdadosdospagamentos
deumcliente,quetambéméumarepresentaçãodessesrecursos.Notecomoolink
éacessadoenavegado;oclienteestáacopladoàpresen çaeaoseusignificado:
Cliente cliente = response.getResource();
response = resource(cliente).getLink(“pagamentos”).follow().get();
Pagamentos todos = response.getResource();
NaFigura7.6,épossívelvisualizarcomofuncionaoacessoaumarepresentaç ão
atravésdeumlinkhipermídia,querelacionadoisrecursosdistintosnaWeb.
Figura7.6:Oclienteseguindoolinkquepossuiosignificadodeseuspagamentos.
217

## Página 238

7.5. REST:arquiteturadistribuídabaseadaemhipermídia CasadoCódigo
Casooservidordecidaalteraramáquina,ouatémesmoofornecedorquecon-
trolaalistagemdepagamentos,bastaqueelemudeolink. Oservidorpassaráa
indicaraoclienteondeencontrarasinformações,emvezdeirbuscá-la.Ocontrole
éinvertido. Comooclienteestáacopladoaosignificadodeumlink,enãocoma
URI,eleseadaptaautomaticamente,conformeoexemploilustradonaFigura7.7.
Figura7.7:Devidoaoacoplamentosemânticocomolink,enãocomaURI,ocliente
acessaoserviçodecontroledepagamentosqueoservidorutilizar.
Érecomendadoousodenamespacesnosatributos rel,comoem http://loja.
arquiteturajava.com.br/rel/servicos, paradesambiguarpossíveissituaçõesemque
umamesmapalavrapossuadoissignificados. RepositórioscomooIANApermi-
temoregistrodosignificadoderelacionamentos,comoéocasodapalavra payment.
Enquantolinkssãoumaformadecontrolehipermídia,quepermitefácilnave-
gação,osformuláriosproveemumamaneiradeinteragircomoestadodaaplicaç ão
paraqueaaplicaçãodoclientedescubraemtempodeexecuç ãoquaisdadosedeque
maneiraelesdevemserenviados[170].Umapossívelimplementaç ãodeformulário
podeserfeitaatravésdautilizaçãodeumaURIespecíficaparaobterumexemplode
representaçãoaserutilizadonapróximarequisiç ão,comonocódigoaseguir:
<link rel=”pagamentos-form”href=”/cliente/7453687/pagamentos-form”/>
Formulárioremeteàidentificaçãodeummodelo(template),queapresentaquais
dadosedequemaneiraelesdevemserenviadosparaoservidor.NocasodeHTML,
porexemplo,acomposiçãodastagsaseguirindicaaoclientequealgocomase-
mânticadonoDoCartaodeveserenviado,comumaajudadedescriç ãoparaumser
humanocompreendercomo“onomedodonodocartãodecrédito”,alémdeumvalor
deexemplo“GuilhermeSilveira":
218

## Página 239

CasadoCódigo Capítulo7. IntegraçãodesistemasnaWebeREST
<label for=”donoDoCartao”>O nome do dono do cartão</label>
<input type=”text”name=”donoDoCartao”id=”donoDoCartao”value=”GuilhermeSilveira”/>
Umaaplicaçãopodeusarumaformadeespecificaç ãodessasmensagenspara
indicaraoclientecomoumpagamentodeveserenviado.Oexemploaseguirutilizao
XForms,umaespecificaçãodoW3C.Notecomoapalavraformulárionãoaparece,e
oconceitodevalores(oucampos)aseremenviadoséalcan çadoatravésdeexemplos
(instance):
<model xmlns=”http://www.w3.org/2002/xforms”>
<instance>
<!-- exemplo de pagamento para o cliente, um formulário -->
<pagamento>
<nomeNoCartao>
Preencha aqui com o nome do dono do cartão
</nomeNoCartao>
<numeroDoCartao>4444555566667777</numeroDoCartao>
<codigo>262</codigo>
<dataDeExpiracao>10/2080</dataDeExpiracao>
</pagamento>
</instance>
<submission
resource=”/cliente/7453687/pagamentos”
method=”post”
mediatype=”application/xml”/>
</model>
Elementosquepermitemanavegação(links)oufornecemexemplosdedados
aseremenviados(formulários)podemserincluídosoureferenciadosemqualquer
representação,sejaelaatravésdeHTML,XMLouJSON[8][217].Linkspodemser
atémesmoinclusosatravésdecabe çalhosHTTP[149],comoemcasosemqueare-
presentaçãoébinária,comoumaimagem.
O OpenSearch, por exemplo, criado para implementar buscas na Web,
utiliza modelos de URI, por meio de um controle hipermídia, que en-
sinam ao cliente qual URI deve ser acessada para uma busca[52], como
por exemplo o padrão http://arquiteturajava.com.br/loja/produtos/busca?q=
\protect\T1\textbraceleftsearchTerms\protect\T1\textbraceright&p=\protect\T1\
textbraceleftstartPage\protect\T1\textbraceright.
Emvezdecentralizartodoocontroleemumúnicopontodeexecuç ão,usando
hipermídiaémaisfácildistribuirocomportamentoentreváriaspartes.Destama-
219

## Página 240

7.5. REST:arquiteturadistribuídabaseadaemhipermídia CasadoCódigo
neira,realizarumprocessopassaaenvolverdiversosagentesquecoordenamsozi-
nhosseutrabalho.AdotandoSOAP,issopodeseralcan çadocomaespecificaçãodo
WS-Choreographyeumalinguagemcomum,queajudeadefinircomooscompo-
nentesdeumserviçocoreografadodevemsecoordenar.
Operações
AoutilizaroHTTPcomoumaAPI,enãoapenaspara tunneling,odesenvolvedor
limitaaintegraçãoapoucasoperaçõesquepodemserrealizadasemcadarecurso.
Porexemplo,aotrabalharcomprodutos,écomummapearcadamétodoHTTP
comumtipodeoperaçãodiferente. POSTePUTpodemserusadosparacriaç ão;
PATCH[50]ouPUTparaalterar;PUTparasubstituir;GETparaleitura;DELETE
pararemoção;HEADparaobteroscabe çalhos(metadados)deumrecurso;eOPTI-
ONSparaentenderquaisoperaçõessãoaceitasnaqueleinstanteparadeterminado
recurso.
Algunsdessesmétodospedemoenviodeumcorpo,comonocasodoPUTe
POSTparacriaçãodeumnovorecurso,paraondeestedeveserenviadoporcom-
pleto.NocasodePATCH,ocorpodefineumformatodealteraçõesaseremaplicadas
emumrecurso(um diff).Apesardeserespecificadoatravésdeuma RFC,ométodo
PATCHéomaisrecenteeaindanãosuportadoporalgumasAPIs.
Media types
Considerandoarepresentaçãoabaixo,agoraépossíveltrabalharcomoslinksde
umrecurso:
<cliente>
<nome>Guilherme Silveira</nome>
<empresa>Loja Caelum</empresa>
<link rel=”pagamentos”href=”/cliente/745368/pagamentos”/>
<link rel=”pagamentos-form”href=”/cliente/745368/pagamentos-form”/>
<link rel=”servicos”href=”/cliente/745368/servicos”/>
</cliente>
Mascomointerpretaresteconteúdoou,atémesmo,saberseatravésdeumatag
linképossívelexecutarumaoperação?Paraisto,énecessárioindicarosignificado
dele,dar-lhealgumvalorsemântico.Osignificadodeumarepresentaç ãotrocadaen-
treclienteseservidoresécompreendidapeloseu mediatype.Seuobjetivoéexplicar
220

## Página 241

CasadoCódigo Capítulo7. IntegraçãodesistemasnaWebeREST
comoaestruturaeosignificadodosdadosdevemserinterpretadosecompreen-
didos. Duranteumarequisição,oclienteeoservidornegociamparaescolherum
mediatype[102]queamboscompreendam(contentnegotiation)(Figura7.8).
Figura7.8:Negociaçãoocorrendoentreclienteeservidor.
Semconhecerqualomediatypeutilizadonarepresentaç ão,éimpossívelafir-
marcomexatidãoseeleéumXML(application/xml),umavariaç ãodeXML
(application/atom+xml),oualgumoutroformato.Alémdisso,pelasuadefiniç ão,
umXMLnãopossuilinks,somentetags;portanto,ondeumserhumanointerpreta
osignificadodataglinkcomoumcontrolehipermídia,umamáquinadeveriainter-
pretarcomoumaoutratagqualquer.
Paraextrairoformatoeasemânticadamensagem,énecessárioquetodarepre-
sentaçãovenhaacompanhadadonomedo mediatype quefoiutilizado.Oprocesso
deinterpretaçãodetagssópodeserfeitoapósanalisarocabe çalhoHTTP,queindica
qualo mediatype utilizado,porexemplo, text/html.
Comononavegador,asaplicaçõesRESTentendemasintaxeeasemânticadas
tagsencontradasemumarepresentaçãodeacordocomseu mediatype,porexemplo,
221

## Página 242

7.5. REST:arquiteturadistribuídabaseadaemhipermídia CasadoCódigo
text/html.
UtilizandooHTTP,aescolhadequalmediatypeusaréfeitaatravésdope-
didodocliente,presentenocabe çalhoAccept. Éachamadanegociação. Oexem-
plo a seguir mostra uma requisição que aceita tantoapplication/xml quanto
application/json:
GET /cliente/7453687 HTTP/1.1
Host: arquiteturajava.com.br
Accept: application/xml, application/json
Naresposta,ocabe çalhoContent-typeindicao mediatype escolhido:
HTTP/1.1 200 OK
Date: Sun, 18 Sep 2011 18:09:00 GMT
Content-type: application/xml
<cliente>
<nome>Guilherme Silveira</nome>
<empresa>Loja Caelum</empresa>
<link rel=”pagamentos” href=”/cliente/745368/pagamentos” />
<link rel=”pagamentos-form” href=”/cliente/745368/pagamentos-form”/>
<link rel=”servicos” href=”/cliente/745368/servicos”/>
</cliente>
Nemsemprearespostaaoprocessode contentnegotiationéumsucesso.Oservi-
dorpodeserincapazdefornecerumarepresentaç ãoatravésdosmedia-typesaceitos
pelocliente. OHTTPpermiteautilizaç ãodeseus responsecodes paradescrever
diversassituaçõesimportantesnacomunicaçãoentredoissistemas. Porexemplo,
quandooservidornãoencontraum media-typeaceitável,eledevedevolverocódigo
406 Not Acceptablejuntoaumarespostaquecontenhareferênciasparaaqueles
quesãoaceitos.
Naintegraçãodesistemas, osformatosmaiscomunssãooXMLeoJSON.
UmavezqueURIsdentrodocorpodevemsertratadascomotexto,ambosnão
definem semântica de controles hipermídia. Para isto, temos outras opções,
comoacriaçãodeum media-typepróprio. Porexemplo,umalojadelivroscria
application/vnd.livro+xml,enquantoumalojadefilmes vnd/filme+xml. Uma
lojainteirapodecriarseupróprio media-typecomovnd/minha_livraria+xml.
Osufixo */*+xml(como application/vnd.caelum+xml)éprevistopelaRFC
3023[142],permitindoqueodesenvolvedordefinaasregrasdecompreensãodocon-
222

## Página 243

CasadoCódigo Capítulo7. IntegraçãodesistemasnaWebeREST
teúdoatravésdoconteúdobase,masainda,assim,indicandoqueusaasintaxede
XML.
Mascadaumadessasextensõesviveisoladamente,ficandoimpossívelumare-
presentaçãoúnicaqueincluainformaçõesencontradasemdois media-typesdistin-
tos.Porexemplo,selivrossãodefinidosatravésdeum media-type,filmesatravésde
outro,pessoaserecomendaçõesatravésdeumterceiro,ficaimpossívelacriaç ãode
umaúnicarepresentaçãocomtodasessasinformações.Porisso,sãorecomendadas
abordagens,quepermitamqualquercombinaçãodeconteúdoeregrasdeprocessa-
mentodeles.
Emvezdecriarvários media-typesbaseadosemXML[130],épossíveladotarum
únicomedia-typemaisgenérico[23].Asregrasdeprocessamentosãodefinidasnesse
mediatype,permitindoautilizaçãodepequenasdefiniçõesdesemânticaeproces-
samentoreferenciadasdentrodarepresentação,comonocasodosmicroformatos
(micro-formats)[218],comohCalendarehCard. Elespermitemadefiniçãodeum
contratofixo,comgarantiasparavalidaç ãoecompatibilidade,alémdesemanter
parcialmenteflexível,comliberdadeparaevolução,diminuindooacoplamentoem
relaçãoaum schemafixo.
MicroformatostambémauxiliamoSEOdealgunsmecanismosdebuscas,como
peloGoogle[44][131]eYahooSearchMonkey. MikeAmundsensugereaado ção
deXHTMLcomoum media-typequesuportacontroleshipermídia[9].Ocódigoa
seguiréumexemplodelocaldescritoutilizandoummicroformatoatravésdo media-
typeapplication/xhtml+xml:
<div class=”locationvcard”>
<span class=”fnorg”>Caelum</span>
<div class=”adr”>
<div class=”street-address”>Rua Vergueiro, 3185, 8o andar</div>
<div>
<span class=”locality”>São Paulo</span>
<span class=”postal-code”>04101300</span>
</div>
</div>
</div>
TecnologiascomoRDF(ResourceDescriptionFramework)tambémvisamdesa-
coplaroconsumidordeseusserviços[117].
Comoacoplamentodoclienteao media-type[211],enãomaisaumservidorde-
terminado, elimina-se a necessidade de especificações como WSDL e W ADL, per-
223

## Página 244

7.5. REST:arquiteturadistribuídabaseadaemhipermídia CasadoCódigo
mitindo a tomada de decisões em tempo de execu ção, em vez de design time.[87]
[10]
Representando conceitos: ontologias
Écomumencontrarsistemasqueapresentamentidadessimilares,comopessoas,
amigos,músicas,clientes,produtos,seguros,filmes,etc.Porexemplo,osignificado
deumcartãodecréditoéigualemgrandepartedeaplicações. Mas,seamaneira
comotaissistemasapresentamourequeremtaisinformaçõesdiferirentresi,clientes
quedesejamutilizá-losterãoummaiorcustodedesenvolvimentoemanuten ção.
Semutilizarumpadrãoamplamenteaceitoouconhecidoefuncionandoso-
mentecomosdetalhesdedeterminadoserviço,osclientesficamrefénsdasdecisões
tomadaspelosservidores. Umbomexemplodeacoplamentoàestruturaestánas
APIsderedessociaiscomooTwitter,LinkedIneFacebook.Todospossuemestrutu-
rassimplesparaindicar,porexemplo,relacionamentosentreusuários,masumavez
quecadaumutilizaformatosdistintosdeXMLouJSON,osclientessãoobrigadosa
escreverumcódigodiferenteparaacessareinteragircomcadaumdosserviços.O
códigoaseguirmostraumexemploderelacionamentoqueusaaAPIdoTwitter:
{
“previous_cursor”: 0,
“ids”: [
143206500,
143201760,
777920
],
“previous_cursor_str”: “0”,
“next_cursor”: 0,
“next_cursor_str”: “0”
}
EoJSONaseguiréaformaescolhidapararepresentarrecursosquepossuemo
mesmosignificado,masdestavezatravésdoFacebook:
{
“data”: [
{
“name”: “Paulo Silveira”,
“id”: “6012890”
},
224

## Página 245

CasadoCódigo Capítulo7. IntegraçãodesistemasnaWebeREST
{
“name”: “Sérgio Lopes”,
“id”: “6314230”
}
]
}
Apesardomesmosignificado(nestecaso,asemânticaderelacionamentoentre
usuários),anãoutilizaçãodeumconjuntodeconceitospadronizados,oudeuma
ontologia(ontology)pararelacionamentos,resultaemclientesfrágeisecomcusto
maiorparacriação.
MuitosacabamoptandopelacriaçãodeAPIsopensource,comoclientesgené-
ricosquetratamcadaserviçoatravésdeumparserdistinto,facilitandootrabalho
dosdesenvolvedoresfinais.Taisbibliotecasseriamdesnecessáriassearepresentação
utilizasseumformatobemconhecido(well-known),capazdedarsignificadoadi-
versostiposderelacionamentos,generalizandoasduasanteriores,comooexemplo
application/jsonaseguir:
{
“person” : {
“name” : “guilhermecaelum”,
“relations” : [
“follows” : “paulo_caelum”,
“follows” : “sergio_caelum”
]
}
}
Utilizarpadrõesprópriosfacilitaodesenvolvimentoacurtoprazo,masimplica
custosdemanuten çãomaisaltosdevidoaoacoplamentodoclientecomumúnico
servidor.Jáexistemdiversospadrõesnomercadoquepodemserutilizados,comoo
casodofriendofafriend (FOAF)[140],quedescrevepessoaseseusrelacionamentos.
Code on demand
Outrastécnicaspermitemaadaptaçãodoclientedeacordocomasnovasfunci-
onalidadesqueumserviçodisponibiliza,entregandocódigosobdemanda(codeon
demand).Destaforma,osclientespodemaprendernovasmaneirasdeinteragircom
oserviço.AutilizaçãodecódigoJavaScriptnosnavegadores,XMLsdeconfiguraç ão
deUI,códigocompiladocomoFlashouAppletssãoexemplosde codeondemand.
225

## Página 246

7.5. REST:arquiteturadistribuídabaseadaemhipermídia CasadoCódigo
Diversasquestõesdeseguran çasurgemaoadotarestetipodeabordagem,umavez
quecódigoseráexecutadonocliente.AFigura7.9ilustraumaaplicaç ãoparacelular
quepodeconstruirsuainterfacecomousuárioatravésdeumarepresentaç ão:
Figura7.9:Usuárioacessandocelularcominteraçãodefinidadeacordocomasres-
postasdoservidor.
AutilizaçãodeumarepresentaçãocomcódigoJavaScript,acessandoomodelo
daaplicaçãonocliente,permiteacustomizaç ãodocomportamento,comonocaso
comumde codeondemand encontradonaWeb,oJSONP.Noexemploaseguir,a
mesmaaplicaçãoparacelularpermiteagoramostraracontadedestinoantesdeexe-
cutaratransferência:
<exemplo>
<contaDestino></contaDestino>
<valor>0</valor>
<data>13/03/2011</data>
<script>
<![CDATA[
contaDestino.onChange(function() {
buscaNomeDoDestinatario(contaDestino.val());
});
]]>
</script>
</exemplo>
226

## Página 247

CasadoCódigo Capítulo7. IntegraçãodesistemasnaWebeREST
Apesardeoconceitodehipermídiaede codeondemand estaremnabasedeuma
arquiteturaREST,existemdezenasdesistemasutilizandoHTTPpara tunneling,que
obtiveramgrandesucesso,sejacomXMLouJSON,enãopossuemanecessidadede
adotarREST.
Sejaseguindoumcontratorígido,adotandoumavalidaç ãoparcialdos schemas,
acessandopartesdosistemadinamicamenteatravésdehipermídiaouaprendendo
comcódigosobdemanda,odesenvolvedorpossuiumlequedetecnologiasàsua
disposiçãoqueresolvemomesmoproblemadeintegraç ão,masque,alongoprazo,
influenciarãoamanuten çãodeseusclientes.
Estado conversacional
Paraimplementarumcarrinhodecompras,costuma-seutilizarcookies,e,com
isso,amesmaURI(como http://arquiteturajava.com.br/loja/carrinho)identificadois
recursosdiferentes,dependendodoclientequeoacessa. Asmensagenstrocadas
entreclienteeservidornãosãomaisautodescritivas(selfdescribingmessages). A
Figura7.10exemplificatalsituação.
Figura7.10:ServindodoisrecursosdiferentesatravésdeumaúnicaURI.
QuandooservidortrataduasrequisiçõesparaamesmaURIdemaneiradife-
rente,dependendodeinformaçõesarmazenadasnocliente,intermediáriosperdem
acapacidadedeentenderoquearequisiç ãosignifica. Esteestadoconversacional
227

## Página 248

7.5. REST:arquiteturadistribuídabaseadaemhipermídia CasadoCódigo
deveserevitadoparamaximizaropotencialdecachesetambémpossibilitaroacesso
amaisdeumcarrinhodecompras.
Todainformaçãoquedescreveamensagemequenãofazpartedainterfaceuni-
formeoudo media-type,échamadadeconhecimentoforadebanda(outofband
knowledge)[59]. RESTéstatelessnosentidodenãomanterestadodaaplicaç ãono
cliente.Umadasmaneirasdetransformarumaabordagemqueutilizacookiespara
umaRESTéidentificarocarrinhosemquebrarainterfaceuniforme,como,por
exemplo,naURIem http://arquiteturajava.com.br/loja/carrinho/57389386257. Ou
seja,cadarecursopassaatersuaprópriaURI.
ÉparecidocomoqueosservidoresWebpermitemfazercomovalordeJSESSIO-
NIDnaURI,masutilizandosessionecookiesapenasparaguardarinformaçõesque
nãoprecisamserendere çáveisnemafetamoresultadodeumarequisiç ão.Issoim-
possibilitaosequestrodesessãoquandohácompartilhamentodeURIsentreusuá-
rios(quepoderiaacontecernousodeJSESSIONID),jáqueosdadosrelativosaum
únicousuáriopodemcontinuarsendotransmitidosporsessãoecookies.
UmadificuldadeencontradaemWebSiteséadenãopodercomprarduaspassa-
gensaéreasoupagardoisboletosbancáriosemabasdiferentesdeummesmobrow-
ser,dadoopéssimousodecookiesparaexpressaroestadoatualdeumcliente.Utili-
zandoumaabordagemmaisamigávelaoendere çamento,ganha-setambémapossi-
bilidadedeterdoiscarrinhosdecompraparaummesmousuárioou,ainda,compar-
tilharsuascomprasepagamentoscomoutrosusuários,casosejainteressanteparaa
aplicação.
OexemplodaFigura7.11mostraoscarrinhosagoracomURIsdistintas,ondeo
cachepodeserfeitosemproblemaseousuáriopoderealizarduascomprassimulta-
neamente,ou,ainda,compartilharsuascomprasepagamentoscomoutrosusuários.
228

## Página 249

CasadoCódigo Capítulo7. IntegraçãodesistemasnaWebeREST
Figura 7.11: Recursos podem ser compartilhados ou cacheados mais facilmente
quandocadaumpossuisuaprópriaURI.
Utilizandocookiesesessãoparaguardaroidentificadordocarrinho,seriadifícil
cachearoucompartilharorecurso. Problemaspodemapareceratémesmocomo
botãodevoltar,deixandooservidorconfusocommaisdeumaaba.
Quandoaaplicaçãonãoarmazenaestadodoclienteemsessões,épossíveladotar
umbalanceadordecarga(load-balancer ),quenãoprecisajogaroclientesemprepara
omesmonóservidor(stickysession),neménecessáriotransferirsessõesdeumlado
paraoutro(sessionreplication),nemficardependentedeumúnicoservidor. Isso
minimizaoprocessamentoereduzaquantidadedemensagenstrocadas.
Como usar caches em um servi ço Web
CachessãointermediáriosimportantesaoutilizaraWebcomoinfraestruturae
plataforma.Elesdiminuemaquantidadededadostransferidoseotempoesperado
deumaresposta.NoHTTP1.1,amaiorpartedasconfiguraçõesdecacheéfeitaatra-
vésdoheader Cache-Control,comonoexemploaseguir,quepermite10minutos
decacheemclientesouintermediários:
HTTP/1.1 200 OK
Date: Mon, 21 Feb 2011 10:10:00 GMT
Last-Modified: Sun, 20 Feb 2011 10:10:00 GMT
Cache-Control: max-age=600,public
229

## Página 250

7.5. REST:arquiteturadistribuídabaseadaemhipermídia CasadoCódigo
No HTTP, as requisições condicionais, que usam cabeçalhos como
If-Not-Modified, permitem a um proxy ou servidor somente entregar uma
novaresposta casoorecursotenha sidoalterado. Emdiversassituações, esses
caches ajudam a diminuir o número de requisições (round-trips) ou a banda
consumida. Oexemploaseguirmostraarequisiç ãodeumclientequepossuiem
seucacheosdadosdeumrecurso,masdesejaverificarseelenãofoialteradodesde
umadataespecífica:
GET /clientes/743756 HTTP/1.1
Host: arquiteturajava.com.br
If-Modified-Since: Sun, 20 Feb 2011 10:10:00 GMT
Arespostadoservidor,casonãotenhasidoalterado,evitaoconsumodesneces-
sáriodebanda:
HTTP/1.1 304 Not Modified
Date: Mon, 21 Feb 2011 10:10:00 GMT
Last-Modified: Sun, 20 Feb 2011 10:10:00 GMT
Cache-Control: max-age=3600,must-revalida
Umapráticacomumconsisteemcolocarumaaplicação(proxyreverso)funcio-
nandocomocachenamáquinadoservidor.Elepodearmazenartodasasrepresenta-
çõespúblicasecacheáveis,evitandooprocessamentocasoelassejamacessadaspor
diversosclientes. Épossívelbeneficiar-sedecachesdemaneiraseguraemHTTP,
mesmoquandooclienteprecisaestarautorizado.Maisimportante,oscachesdere-
quisiçõesHTTPestãoonipresentes.Diferentedecachesespecíficosaoserverside,
elespodemapareceremnavegadores,APIsclientes,servidores,proxies,etc.(Figura
7.12).
230

## Página 251

CasadoCódigo Capítulo7. IntegraçãodesistemasnaWebeREST
Figura7.12:CachesHTTPpodemaparecertantoemclientesquantoemservidores
eintermediários.
ArespostadeumservidornãovariasomentedeacordocomaURI,mastam-
bémcomoscabe çalhosdarequisiçãoHTTP.Paranãoquebrarcaches,oservidor
deveindicarquaiscabe çalhosdarequisiçãoinfluenciaramemseuresultado. Para
umarequisiçãoqueutilizouocabe çalhoAccept: application/xml,oresultadoa
seguirfariacomqueumaproxyentregasseomesmoXMLparaumarequisiç ãocom
Accept: application/json:
GET /clientes/743756 HTTP/1.1
Host: arquiteturajava.com.br
Accept: application/xml
HTTP/1.1 200 Ok
Date: Mon, 21 Feb 2011 10:10:00 GMT
Last-Modified: Sun, 20 Feb 2011 10:10:00 GMT
Cache-Control: max-age=3600,must-revalidate
Content-Type: application/xml
Omesmoocorrecomoutrosheadersdenegociaç ão,comoo Accept-Encoding,
parasuportarcompressãogzip.Oservidordeveutilizarocabe çalho Varyparare-
231

## Página 252

7.5. REST:arquiteturadistribuídabaseadaemhipermídia CasadoCódigo
solveroproblema,como Vary: Accept .
Damesmamaneiraque,naWebhumana,épossívelquebrarumaúnicarequi-
siçãoemdiversasparaotimizarousodecache[75],sistemasfor çarãomúltiplasre-
quisiçõesnaAPIpararecuperarpequenospedaçosdeinforma ção. Essaspráticas
dequebrarrequisiçõesgrandesemmenoreseutilizarhipermídiaparanavegarno
sistemapermitemotimizaçõesdecacheepodemseradotadasporqualquersistema
integradoatravésdaWeb.Reparequeéumaabordagemdiferentedaquecostuma
seraplicadacomSOAP,ondeumagranularidademaiorérecomendada,evitando
umnúmerograndederequisições.
Tomandocomoexemploumserviçoqueretornaumrelatóriocominformações
financeirasdetalhadas,épossívelquebrararequisiç ão,paraqueelassejamfeitas
baseadasnoparâmetrodoano.Seoclientenecessitardainformaç ãode4anosdife-
rentes,fará4requisições.Avantagemseráquecadaumadessasrequisiçõespoderá
sercacheada,eatémesmotertemposdeexpiraç ãodiferentes.Aproveita-sedofato
dequeorelatóriofinanceirodosanosanterioresprovavelmentenãomudarão,ever
dadosstalenãoéumgrandeproblema.Sefosseapenasumaúnicarequisiç ão,não
seriapossívelseaproveitartantoassimdocache.
Umasoluçãomaiselaboradapodetercomoentrypointorelatóriodoanocor-
rente,queseráentreguejuntocomumlinkparaosresultadosdoanoanterior.Os
headersindicamumpossívelperíodocurtodecache.Aoseguirolink,osheaders
indicamumperíododecachemuitomaiorelinksparanavegaç ão(Figura7.13):
Figura7.13:Relatóriobeneficiando-sedecachedevidoaousodehipermídianaque-
bradeumrecursoportempo.
HTTP/1.1 200 OK
232

## Página 253

CasadoCódigo Capítulo7. IntegraçãodesistemasnaWebeREST
Date: Sun, 18 Sep 2011 18:09:00 GMT
Cache-control: max-age: 63072000
Content-type: application/xml
<pagamentos>
<pagamento>...</pagamento>
<pagamento>...</pagamento>
<pagamento>...</pagamento>
<link rel=”next”
href=”http://arquiteturajava.com.br/loja/pagamentos/2011” />
<link rel=”previous”
href=”http://arquiteturajava.com.br/loja/pagamentos/2009” />
</pagamentos>
Segmentarorecursoportempoéumapráticasimpleseefetivade segmentation
byfreshness[75],eusarhipermídiaéumpassoadiantequepermiteaotimizaç ãodo
cache.
Emalgumassituações,ocachepodeserusadocomoumaformadeprolongar
adisponibilidadedeserviçosquetemporariamenteestãoforadoar. Utilizandoo
headerdecache-controleseustale-if-error[148],épossívelindicarqueumares-
postapodeserentreguedocache,mesmoqueesteestejaexpirado.E,seoservidor
nãoestiverdisponível,éumatrocaconscienteentremostrarumdadopossivelmente
desatualizadoouquebrarumaaplicação:
HTTP/1.1 200 OK
Cache-Control: max-age=6000, stale-if-error=12000
Content-Type: application/json
Atravésdostale-while-revalidate,damesmaRFC,épossívelminimizarosdanos
doefeitodogpileemaplicaçõesservidasnaWebqueutilizamcachesHTTP[88].
CombinarcabeçalhosetécnicasdecacheemHTTPéfundamentalparaobomuso
daWebcomoplataforma.
233

## Página 255

CasadoCódigo ReferênciasBibliográficas
Referências Bibliográficas
[1]DefiningSoftwarearchitecture.2009.
[2] SubbuALLAMANJARU.Restfuluris.2010.
[3] SubbuALLAMANJARU.RESTfulWebServicesCookbook.2010.
[4] DeepakALUR,DanMalks,andJohnCrupi.Corej2eepatterns:Bestpractices
anddesignstrategies.2.ed.2003.
[5] MagnusALVESTAD.Memoryleakswheretheclassloadercannotbegarbage
collected.
[6] ScottAmbler.Theobject-relationalimpedancemismatch.
[7] ScottAmbler.Introductiontotestdrivendesign(tdd).2003.
[8] MikeAMUNDSEN.Designingahypermediaapiwithjson.2010.
[9] MikeAMUNDSEN.Restfulprofiling:Xhtml-basedwebapis.2010.
[10] MikeAMUNDSEN.Whywadlwhenyoucanrun?2010.
[11] DianeJORDANanJohnEVDEMON. Webservicesbusinessprocessexecu-
tionlanguageversion2.0.2007.
[12] GregoryR.ANDREWS.FoundationsofMultithreaded,Parallel,andDistribu-
tedProgramming.2000.
[13] AbelAvram.Practicingagilityinapplicationarchitecture.2008.
[14] RolandBarcia. Tiredofhandcodingjdbc?useibatisasadatamappingfra-
meworkinstead.2005.
235

## Página 256

ReferênciasBibliográficas CasadoCódigo
[15] KentBeck.Test-drivendevelopment:byexample.2002.
[16] JoeBLANDYandJoshuaBLOCH.Whydoesn’tjavahaveanimmutabledate
class?2003.
[17] JoshuaBLOCH.EffectiveJava.2ed. 2008.
[18] JoshuaBLOCH.EffectiveJava.2.ed. 2008.
[19] JAVABLUEPRINTS.Model-view-controller.2000.
[20] JonasBONÉR.Real-worldscala:Dependencyinjection(di).
[21] GradyBOOCH.Object-orientedanalysisanddesignwithapplications.1993.
[22] EvanBOTTCH.Continuousintegration–singlecodeline.2010.
[23] TimBray.Don’tinventxmllanguages.2006.
[24] AdrianBROCK.Jbossclassloaderhistory.
[25] DonBrown.Myhistoryofstruts2.2006.
[26] JulianBROWNE.Brewer’scaptheorem.2009.
[27] SteveBURBECK. Applicationsprogramminginsmalltalk-80™:Howtouse
model-view-controller(mvc).1987.
[28] PhillipCALÇADO.Internaldatatransferobjects.
[29] PhillipCALÇADO.Objetosfantoches.
[30] PhillipCALÇADO.Howtowritearepository.2010.
[31] PhillipCalçado.Howtowritearepository.2010.
[32] NicholasCARR.TheBigSwitch:RewiringtheWorld,fromEdisontoGoogle.
2008.
[33] RobertoCHINNICIandMarekPOTOCIAR.Jax-rs2.0: Thejavaapiforrest-
fulwebservices.2011.
[34] MandyChung. Monitoringandmanagingjavase6platformapplication.
2006.
236

## Página 257

CasadoCódigo ReferênciasBibliográficas
[35] COMPUTERWORLD.Atozofprogramminglanguages:Smalltalk-80.2010.
[36] MicrosoftCorporation.Extensionmethods(cprogrammingguide).
[37] ORACLECORPORATION.Ergonomicsinthe5.0java™virtualmachine.
[38] ORACLECORPORATION.Frequentlyaskedquestionsaboutthejavahots-
potvm.
[39] OracleCorporation.Thehistoryofjavatechnology.
[40] ORACLECORPORATION.Javadocdojava.lang.ref.
[41] ORACLECORPORATION.Javadocdométodovalueof(int)daclasseinteger.
[42] ORACLECORPORATION.Javadocdosystem.gc().
[43] ORACLECORPORATION.Tuningthememorymanagementsystem.
[44] MikeDANYLCHUKandNitinSHETTI. Introducinganewrichsnippets
format:Events.2010.
[45] JosephDARCY.Projectcoin:Updatedarmspec.2010.
[46] LindaDEMICHIEL.Javapersistence2.0proposedfinaldraft.2009.
[47] EdsgerW.DIJKSTRA.Ontheroleofscientificthought.1974.
[48] JBOSSDOCUMENTATION.Classcastexceptions–i’mnotyourtype.
[49] JimDRISCOLL.Servlethistory.2005.
[50] L.DUSSEAULT,LindenLAB,andJ.SNELL.Patchmethodforhttp.2010.
[51] AmmonH.EdenandRickKazman. Architecture,design,implementation.
25thInternationalConferenceonSoftwareEngineering–ICSE,2003.
[52] DeWittetalClinton.Opensearchspecification.2000.
[53] J.etalGREGORIO.Uritemplate.2010.
[54] SavasetalPARASTATIDIS. Theroleofhypermediaindistributedsystem
development.WS-REST‘10ProceedingsoftheFirstInternationalWorkshopon
RESTfulDesign,2010.
237

## Página 258

ReferênciasBibliográficas CasadoCódigo
[55] Royetal.SINGHAM. TheThoughtworksAnthology:essaysonSoftwareTech-
nologyandInnovation.2008.
[56] Stefanetal.TILKOV.Soamanifesto.2009.
[57] EricEvans.Domain-drivendesign:Tacklingcomplexityintheheartofsoftware.
2003.
[58] MichaelFEATHERS.Thedeepsynergybetweentestabilityandgooddesign.
2007.
[59] RoyFIELDING.Architecturalstylesandthedesignofnetworkbasedsoftware
architectures.2000.
[60] NealFORD. Evolutionaryarchitectureandemergentdesign: Evolutionary
architecture.2010.
[61] MartinFowler.Anemicdomainmodel.
[62] MartinFowler.Domain-specificlanguage.
[63] MartinFowler.Errantarchitectures.
[64] MartinFowler.Firstlawofdistributedobjectdesign.
[65] MartinFOWLER.Inversionofcontrolcontainersandthedependencyinjec-
tionpattern.
[66] MartinFOWLER.Refactoring:ImprovingtheDesignofExistingCode.1999.
[67] MartinFOWLER.PatternsofEnterpriseApplicationArchitecture.2002.
[68] MartinFowler.PatternsofEnterpriseApplicationArchitecture.2003.
[69] MartinFowler. UMLDistilled:abriefguidetothestandardobjectmodeling
language.2003.
[70] MartinFowler.Whoneedsanarchitect? IEEESoftware,v.20,2003.
[71] MartinFowler.Isdesigndead?2004.
[72] MartinFowler.Fluentinterface.2005.
[73] MartinFowler.Gettereradication.2006.
238

## Página 259

CasadoCódigo ReferênciasBibliográficas
[74] MartinFOWLER.Businessreadabledsl.2008.
[75] MartinFOWLER.Segmentationbyfreshness.2008.
[76] MartinFOWLER.Bluegreendeployment.2010.
[77] MartinFOWLER.2003.Anemicdomainmodel.
[78] SteveFREEMANandNatPRYCE. Growingobject-orientedsoftware,guided
bytests.2009.
[79] ErichGAMMA,RichardHELM,RalphJOHNSON,andJohnM.VLISSIDES.
DesignPatterns:elementsofreusableobject-orientedsoftware.1994.
[80] ErichGAMMA,RichardHELM,RalphJOHNSON,andJohnM.VLISSIDES.
DesignPatterns:elementsofreusableobject-orientedsoftware.1994.
[81] SimsonGNANAM.Howinheritanceworksinhibernate.2008.
[82] BrianGoetz.Javatheoryandpractice:Tomutateornottomutate?2003.
[83] BrianGOETZ.JavaConcurrencyinPractice.2006.
[84] GOOGLE.Protocolbuffers.
[85] JamesGosling,BillJoy,GuySteele,andGiladBracha. TheJava™Language
Specification.3.ed. 2005.
[86] DerekGOTTFRID.Self-service,proratedsupercomputingfun!2007.
[87] JoeGREGORIO.Doweneedwadl?2007.
[88] IlyaGRIGORIK.Asynchronoushttpcachevalidations.2008.
[89] PaulHAMMANT.Inversionofcontrolhistory.
[90] DavidHAYDEN.Webapplications:N-tiervs.n-laye.2005.
[91] EricHERMAN.Compositionvs.inheritanceinjava.
[92] JBOSSHIBERNATE.Batchprocessing.
[93] JBOSSHIBERNATE.Configuraçãodoc3p0nohibernate.
[94] JBOSSHIBERNATE.Improvingperformance.
239

## Página 260

ReferênciasBibliográficas CasadoCódigo
[95] JBOSSHIBERNATE.Querycache.2009.
[96] EelcoHILLENIUS.Wicketisnotsuitedforwebsites.2011.
[97] ToddHOFF.Strategy:Breakupthememcachedogpile.2009.
[98] ToddHOFF. Netflix: Uselesschattyprotocolsinthecloud-plus26fixes.
2010.
[99] GregorHOHPEandBobbyWOLF. Enterpriseintegrationpatterns:designing,
building,anddeployingmessagingsolutions.2003.
[100] AllenHOLUB.Whygetterandsettermethodsareevil.2003.
[101] JezHUMBLEandDavidFARLEY.Continuousdelivery:reliablesoftwarere-
leasesthroughbuild,test,anddeploymentautomation.2010.
[102] IANA.http://tools.ietf.org/html/rfc5789.2007.
[103] IBM.Dpdchronology.
[104] INNOQ.Webservicesstandardsasofq12007.2007.
[105] Ws-*istoRESTas TheoryistoPractice.2007.
[106] NickKALLEN.Bigdatainreal-timeattwitter.2010.
[107] FabioKung.Rubyanddependencyinjectioninadynamicworld.2010.
[108] RamnivasLADDAD.AspectJinaction:EnterpriseAOPwithSpringApplica-
tions.2.ed. 2009.
[109] CraigLarman. Protectedvariation:Theimportanceofbeingclosed. IEEE
Software,v.18,2001.
[110] CraigLARMAN. Applyingumlandpatterns: anintroductiontoobject-
orientedanalysisanddesignanditerativedevelopment.3.ed.2004.
[111] CraigLarman. Basdesign architecture.PracticesforScalingLeanandAgile
Development,2010.
[112] JulienLECOMTE.Yahoouicompressorandjavaclassloader.
[113] TimLindholm.TheJava™VirtualMachineSpecification.2.ed.1999.
240

## Página 261

CasadoCódigo ReferênciasBibliográficas
[114] TimLINDHOLMandFrankYELLIN. Thejavavirtualmachinespecification:
Loading,linking,andinitializing.
[115] SérgioLopes. Vivendonocloud: ainfraestruturaexternadacaelumem11
soluções.2011.
[116] SubrayaMALLYA.Netflix’smovetoamazonec2–explained.2010.
[117] FrankMANOLAandEricMILLER.Rdfprimer.2004.
[118] RobertC.Martin.Dependencyinjectioninversion.
[119] RobertC.Martin. Oodesignqualitymetrics-ananalysisofdependencies.
1994.
[120] RobertC.Martin. Thesingleresponsibilityprinciple.1995.
[121] RobertC.MARTIN.Thedependencyinversionprinciple.1996.
[122] RobertC.Martin.Theinterfacesegregationprinciple.1996.
[123] RobertC.MARTIN.Theliskovsubstitutionprinciple.1996.
[124] RobertC.Martin.Theopen-closedprinciple.1996.
[125] RobertC.Martin.Stability.1997.
[126] RobertC.Martin.Designprinciplesanddesignpatterns.2000.
[127] RobertC.MARTIN. AgileSoftwareDevelopment: Principles,Patterns,and
Practices.2002.
[128] RobertC.MARTIN. Railsconf2010keynote–cucumberscriptsandtesting
businessrulesthroughtheui.2010.
[129] JonMASAMITSU.Ourcollectors(sun).
[130] MICROFORMATS.Plainoldxmlconsideredharmful.2008.
[131] MICROFORMATS.Googleaddssupportforhcalendarandhreciperichsnip-
pets.2010.
[132] SUNMICROSYSTEMS.Corej2eepatternsfrontcontroller.
241

## Página 262

ReferênciasBibliográficas CasadoCódigo
[133] SUNMICROSYSTEMS.Códigofontedaclassestring.
[134] SUNMICROSYSTEMS.Thegarbage-firstgarbagecollector.
[135] SUNMICROSYSTEMS.Javase6javahotspot™virtualmachinegarbagecol-
lectiontuning.
[136] SUNMICROSYSTEMS.Jaxpcompatibilityguideforthej2se5platform.
[137] SUNMICROSYSTEMS. Memorymanagementinthejavahotspot™virtual
machine.2006.
[138] SUNMICROSYSTEMS.Javapersistenceblueprints.2007.
[139] SUN MICROSYSTEMS. Core j2ee patterns session faç ade.
http://java.sun.com/blueprints/corej2eepatterns/Patterns/SessionFacade.html.
[140] LibbyMILLERandDanBRICKLEY. Thefriendofafriendproject.2000.
[141] HansMuller.Official:Swingisthedominantguitoolkit.2005.
[142] M.Murata,S.ST.LAURENT,andD.Kohn.Xmlmediatypes.2001.
[143] GlenfordMYERS.Theartofsoftwaretesting,2.ed.2004.
[144] T.H.NELSON.Complexinformationprocessing:afilestructureforthecom-
plex,thechangingandtheindeterminate. ACM‘65Proceedingsofthe196520th
nationalconference,1965.
[145] DanNORTHandAslakHELLESOY.Picocontainerdesignpatterns.
[146] DanNORTHandAslakHELLESOY.Picocontainerdesignpatterns.
[147] MarkNOTTINGHAM. Cachingtutorialforwebauthorsandwebmasters.
1998-2010.
[148] MarkNOTTINGHAM.Httpcache-controlextensionsforstalecontent.2010.
[149] MarkNOTTINGHAM.Weblinking.2010.
[150] DavidORCHARD.Versioningxmlvocabularies.2003.
[151] LarryO’BRIEN. Designpatterns15yearslater: Aninterviewwitherich
gamma,richardhelm,andralphjohnson.2009.
242

## Página 263

CasadoCódigo ReferênciasBibliográficas
[152] RajivPANT.Organizingawebtechnologydepartment.
[153] VincentPARTINGTON. Jpaimplementationpatterns:Dataaccessobjects.
2009.
[154] VincentPARTINGTON. Jpaimplementationpatterns: Servicefacadesand
datatransfersobjects.2009.
[155] AnthonyPATRICIO.Ashortprimeronfetchingstrategies.2010.
[156] SriniPENCHIKALA.Jdbc4.0enhancementsinjavase6.2006.
[157] PICOCONTAINER.Picocontainersite.
[158] LainPranshu.LayersandTiers.2006.
[159] BrunoR.Preiss.Mark-and-sweepgarbagecollection.
[160] TonyPRINTEZIS. Garbagecollectioninthejavahotspot™virtualmachine
(generationalalgorithm).2004.
[161] TonyPRINTEZIS.Howtohandlejavafinalization’smemory-retentionissues.
2007.
[162] DanPRITCHETT.Base:Anacidalternative.2008.
[163] NatPRYCE."dependencyinjection"consideredharmful.2011.
[164] MarkRICHARDS,RichardMONSON-HAEFEL,andDavidA.CHAPPELL.
JavaMessageService.2.ed. 2009.
[165] MarkRICHARDS,RichardMONSON-HAEFEL,andDavidA.CHAPPELL.
JavaMessageService.2.ed. 2009.
[166] MarkRICHARDS,RichardMONSON-HAEFEL,andDavidA.CHAPPELL.
JavaMessageService.2.ed. 2009.
[167] MarkRICHARDS,RichardMONSON-HAEFEL,andDavidA.CHAPPELL.
JavaMessageService.2.ed. 2009.
[168] LeonardRICHARDSON.Justicewilltakeusmillionsofintricatemoves.2008.
[169] LeonardRICHARDSONandSamRUBY.Restfulwebservices.2007.
243

## Página 264

ReferênciasBibliográficas CasadoCódigo
[170] IanROBINSON.Usingtypedlinkstoforms.2010.
[171] DouglasC.SCHMIDTandTimHARRISON. Double-checkedlocking:An
optimizationpatternforefficientlyinitializingandaccessingthread-safeob-
jects.1996.
[172] AlecSHARP.Smalltalkbyexample:thedeveloper’sguide.1997.
[173] JamesSHORW.TheArtofAgileDevelopment.2007.
[174] RandySHOUP.ebaysarchitecturalprinciples.2008.
[175] DavidSIEGEL.Pull:thepoweroftheSemanticWebtotransformyourbusiness.
2009.
[176] GuilhermeSilveira. Compondoseucomportamento:herança,chainofres-
ponsabilityeinterceptors.2010.
[177] GuilhermeSilveira. Deploycontínuo: poisintegraçãocontínuanãobasta.
2010.
[178] GuilhermeSILVEIRA.Brancheseintegraçãocontínua:oproblemadefeature
branches.2011.
[179] GuilhermeSILVEIRA.Martinfowlerandjezhumbleoncontinuousdelivery.
2011.
[180] PauloSilveira.Java6,asapisdexml,webserviceseclassloaders.2007.
[181] PauloSilveira.Jpacomhibernate:heran çaemapeamentos.2007.
[182] PauloSilveira. Os7hábitosdosdesenvolvedoreshibernateejpaaltamente
eficazes.2008.
[183] PauloSilveira.2009.2009.
[184] PauloSilveira.Enfrentandoalazyinitializationexceptionnohibernate.2009.
[185] PauloSilveira. Guj:Acessoaoentitymanager:atravésdeumdaooudireta-
mente?2009.
[186] PauloSilveira.Trabalhandocomclosuresnojava8.2011.
244

## Página 265

CasadoCódigo ReferênciasBibliográficas
[187] JamesSNELL.Restfulrpc.2010.
[188] JohnSOWA.Sowa’slawofstandards.1991.
[189] GOOGLEPAGESPEED.Webperformancebestpractices.
[190] JoelSpolsky.Don’tletarchitectureastronautsscareyou.2001.
[191] JoelSpolsky.Languagewars.2006.
[192] BernieSUMPTION.Inheritanceisevil,andmustbedestroyed.2007.
[193] RichardE.Sweet. Themesaprogrammingenvironment. Proceedingsofthe
ACMSIGPLAN85symposiumonLanguageissuesinprogrammingenviron-
ments,1985.
[194] AttilaSZEGEDI.Adayinthelifeofamemoryleakhunter.2005.
[195] AndrewS.TANENBAUM.Computernetworks.2.ed. 1988.
[196] GilTENE.Azul’spauselessgarbagecollector.2010.
[197] RoyansK.THARAKAN.Brewer’scaptheoremondistributedsystems.2010.
[198] EricTHOLOMÉ.Wellearnedretirementforsoapsearch.2009.
[199] StefanTILKOV.RESTundHTTP:Einsatzderarchitekturdeswebf ürintegra-
tionsszenarien.2009.
[200] StefanTILKOV.Einstieginrest.2010.
[201] StefanTILKOV.Einstieginrest.2010.
[202] StefanTILKOV.Enterpriseitvs.www.2010.
[203] StefanTILKOV,MarcHADLEY,andPaulSANDOZ.Jsr311final:Javaapifor
restfulwebservices.2008.
[204] RobertTolksdorf. Programminglanguagesforthejavavirtualmachinejvm
andjavascript.
[205] BillVENNERS.Inheritanceversuscomposition:Whichoneshouldyoucho-
ose?1998.
245

## Página 266

ReferênciasBibliográficas CasadoCódigo
[206] BillVENNERS.Designprinciplesfromdesignpatterns–aconversationwith
erichgamma,partiii.2005.
[207] SteveVinoski.Welcometo"thefunctionalweb".2009.
[208] LanVUONG. Extremetransactionprocessingpatterns: Write-behindca-
ching.2009.
[209] W3C.Simpleobjectaccessprotocol(soap)1.1.2000.
[210] W3C.Soapversion1.2part0:Primer(secondedition).2007.
[211] JimWEBBER,SavasPARASTATIDIS,andIanROBINSON.RESTinpractice:
Hypermediaandsystemsarchitecture.2010.
[212] EHCACHEWEBSITE.Hibernatecaching.
[213] GOOGLEAPPENGINEWEBSITE. Choosingadatastoreforgoogleapp
engine.
[214] TOMCAT WEBSITE. Tomcat manager how to.
http://tomcat.apache.org/tomcat-7.0-doc/manager-howto.html.
[215] SimonWillison.Are-introductiontojavascript.2006.
[216] GalderZAMARREÑO.Usinginfinispanasjpa/hibernatesecondlevelcache
provider.2010.
[217] K.ZYPandG.Court. Ajsonmediatypefordescribingthestructureand
meaningofjsondocuments.2009-2010.
[218] TantekÇELIK.Facebookaddshcalendarandhcardmicroformatstomillions
ofevents.2011.
246