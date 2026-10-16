---json
{
  "id": "abap_o_guia_de_sobreviv_ncia_do_profissional_moderno",
  "title": "ABAP O guia de sobrevivência do profissional moderno",
  "categoria": "06-devops-infra",
  "subcategoria": "ci-cd",
  "resumo": "**Arquivo Original:** `ABAP O guia de sobrevivência do profissional moderno.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "abap",
    "devops",
    "guia",
    "infra",
    "moderno",
    "ncia",
    "profissional",
    "sobreviv"
  ],
  "perguntas_tipo": [
    "Como utilizar ABAP O guia de sobrevivência do profissional moderno?",
    "Quais as boas praticas de ci-cd?"
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
  "dono": "stack-ci-cd",
  "prioridade": 2
}
---

# ABAP O guia de sobrevivência do profissional moderno

> **Arquivo Original:** `ABAP O guia de sobrevivência do profissional moderno.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 1

ABAP 
O guia de sobrevivência do 
profissional rnoderno 
e Casado 
Código 
--L . 
MAURICIO ROBERTO CRUZ 

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
Introdução
Emdezembrode2010,haviaacabadodesairdeumempregonafábricade
softwaredeumamultinacionaldetecnologia,epartiaparadesbravaráguas
desconhecidas.EstavatrabalhandoemumaconsultorianacionaldeSAP,alo-
cadodiretamenteemclientes,esentia-meconstantementeperdido.
Apósalgunsmesesnanovaempresa,fuitrabalharemumprojetoqueteve
umperíodode“baixa”.Sabecomoé:oclientepedeumcarroimportadoea
consultoriaprojetaaimplementaçãodeumamáquinaquefazoteletransporte
doscarrosdoexterior,diretoparaaportadocliente.Porém,duranteafase
deconstrução,alguémdescobrequetudooqueoclienterealmenteprecisava
eradeumamontanhadecachorros-quentes,daquelesquevocêcompraem
qualquerbarraquinhadeesquina.
Nomeiodessecaos,surgemgerentesdetodososladosecriam-semi-
lharesdereuniõesdealinhamentoparadescobrircomotransformarotele-
transportadordecarrosemumasupermáquinade hot-dogs.Sãonessashoras
quenós,osABAPers,ficamosalgunsdiasparadosesperandoredefinições,
emumaespéciedecalmariaantesdatempestade.Afinal,umasupermáquina
mágicadehot-dogsdessasnãovaisercriadadanoiteparaodia. Ealguém
aindavaiterdepassarmuitamaionesenopãocomumafaquinhaderocam-
boleparaagradarocliente.
Oqueéquevocêfazquandonãotemdemanda?Criaumblog?Éclaro
quenão:vocêvaiconversarnoSkypecomalgumamigo.
Pensandonomeupassadopré-ABAP,averdadeéqueeusempretivevon-
tadedecompartilharconhecimento,dartreinamentos,ensinaralgoaalguém.
Nãoseiexplicardequelugarissosurgiu,seiquesempretiveessavontade.
Sejanaescola,emfórunsdejogosonline,ounaajudadeamigoseparentes
i

## Página 4

CasadoCódigo
comvírusnocomputador(abraços,galeradeTI),sempretenteiexplicaro
queeuestavafazendoparaosoutrosdeformaqueelespudessemreaprovei-
taroprocedimentonofuturo.EjustamenteoMauro,oamigocomquemeu
conversavanoSkype,tambémtinhaesseperfil.
Juntandoduaspessoasquegostamdecompartilharconhecimento,nãoé
deseespantarquenóstenhamostidoaideiadecompartilharaquelemonte
dedicasABAP,queguardávamosemarquivosdetexto,comqualquerumque
quisesseler.MauromantinhaumblogdesatualizadodePHPnoar,queserviu
comobaseparaaidealizaçãodeumblogdeABAP.Ficamosextremamente
empolgadose,emmenosdeumdia,tínhamosumembriãodesitenoar.Só
queaindafaltavaonome.
SetemumacoisaqueeuachoextremamentechatanomundoSAPéque
todomundoéextremamenteformal. Parecequeessavidadetrabalhoem
clientesconsomeaalmadaspessoase,aospoucos,elastornam-seincapazes
deriremdesimesmas,transformando-seemrobozinhosquesepreocupam
maiscomformalidadesdoquecomobjetivoseprazernotrabalho.
Portanto,qualonomequepoderiaquebraressabarreiraquadradalogo
decara,mostrandoqueali,naquelesite,poderíamosfalardeSAPdonosso
jeito,sempreocupações? ABAPZombie – Prevenindo consultores de virarem
zumbis.
Assimnasceuonomedoblog.ABAPerqueéABAPerjávirounoiteapa-
nhandocomcoisassimpleseficouparecendoumzumbidetantotomarcafé.
Essatemáticaserviudebaseparaotomdostextoseparatodaaidentidadevi-
sualdosite.Aospoucos,ganhamosaudiência,tivemosapoiodacomunidade
ABAPbrasileira,eamotivaçãoparacontinuarsemprefoicrescente.
O ABAPZombie (http://www.abapzombie.com) trouxe diversas coisas
boas,discussõesdealtonível(algumasdebaixotambém),umapancadade
novosamigoseumarazãoparafazerdomeupróprioaprimoramentoprofis-
sionalumaconstante.Quatroanosdepois,alguémfinalmentemeconvenceu
dequeeudeveriacompilarpartedosartigosqueescreviemumlivro,resul-
tandonistoquevocêagoratememmãos(ounatela).Reviseitodosostextos
ecrieimuitoconteúdoespecialmenteparaestapublicaç ão,deformaquea
leiturapossaserfeitademaneiracontínua.
Sejavocêjúnior,plenoousênior,esperoqueostextosconsigamarrancar-
ii

## Página 5

CasadoCódigo
lhealgumasrisadas,levantaralgunsquestionamentosefazervocêenxergar,
aomenos,umapequenapartedoseutrabalho,deformadiferente. Prepare
asuaescopeta,tireolan ça-granadasdoguarda-roupaeembarquecomigo
najornadainterminávelcontraoszumbisqueassombramnossasvidasde
ABAPers. Dicadeamigo:ouvocêmiranacabe ça,ouvaigastarmuniçãoà
toa...eanossamunição,comoprogramadores,éonossotempo.
Comoutilizarestelivro
Paraquevocênãofiqueperdidonomundodaspalavrasesejamordido
porumzumbierrante,ostextosforamdivididosem8capítulose2apêndices:
•Capítulo1–Porondecomeçar?: umpanoramageraldalinguagem
ABAPedoseumercado,comalgumasdicasdecomoconseguirinfor-
maçõesparaterumavidaABAPermenostraumática.Iniciamostam-
bémalgumasdiscussõesqueserãoabordadasnospróximoscapítulos.
•Capítulo2–ArelevânciadoABAPparaomercadodeTI:qualauti-
lizaçãodoABAPnomundo?QuantasempresasutilizamoSAPERP?
Qualoseupassadoequalseráoseufuturo?Exploramosasraízesdo
SAPERPparaentenderalgunscomportamentosdomercado,encai-
xandooABAPnoseulugardahistória.
•Capítulo3–CertificaçõesABAP:orealpesodeumacertificaç ão
ABAPéconstantementequestionada. Utilizandoumaanálisedecer-
tificaçõesSAP,criadaporalgunsmembrosdacomunidadeSAPháal-
gunsanos,compartilhominhasexperiênciassobreotema.
•Capítulo4–Osbastidores: háumesforçomonstruosoportrásde
cadadesenvolvimentoABAPquepodemudarcompletamenteosru-
mosdeumprojeto.Entenderesseprocessoécrucialparaterumbom
futurocomoABAPereéexatamenteissoquefaremosnestecapítulo.
•Capítulo5–Carreira,motivação,universoetudomais:todaamo-
vimentaçãocriadanosbastidoresimpactatantoavidaABAPer,que
muitosprogramadoressóenxergamdoiscaminhosparaevoluç ão: a
reclamaçãoouadesmotivaçãoconstante.Seráqueépossívelsairdesse
meioeencontrarumfuturopromissor?
iii

## Página 6

CasadoCódigo
•Capítulo6–OstabusdomundoABAP:asíndromedorobôatinge
diversosABAPersmundoafora,queajudamaproliferartabusquepo-
deriaserresolvidosdeformabemsimples.Nestecapítulo,vamosrefle-
tirsobretodososproblemasclássicosdavidaABAPer:documentaç ão,
nomenclatura,comentários,usodeconstanteseasatisfaç ãodousuá-
rio.
•Capítulo7–Sobreprogramação,semcódigos:sabermilharesdeco-
mandosetécnicasdeprogramaçãoéosuficiente?Hátantacoisaaser
consideradaantesmesmodeumalinhadeprogramaç ãoABAPseres-
critaquecrieiumcapítulosóparaisso.
•Capítulo8–Oquevemporaí:hámuitosnovosprodutosSAPsendo
lançadosemuitosdelesnãoparecemmuito“palpáveis”paraosABA-
Pers.Vamosanalisarquaissãoosprodutosquetêmmaissinergiacom
odesenvolvimentoABAPatualecomoficaráodesenvolvimentoABAP
nofuturo.
•Capítulo9–ApêndiceI:umguiacomdicasemuitomaterialpara
aquelesquequiseremaprenderABAPporcontaprópria,semdepen-
deremdeumcursopago.
•Capítulo10–ApêndiceII:hámuitoslinksecitaçõesdelivrosaolongo
doscapítuloseesseapêndiceservecomoumcompilado.Hátambém
algumasindicaçõesadicionaisdeconteúdoABAPrelevante.
Divirta-se!
Sobreoautor
MauricioRobertoCruzébacharelemCiênciadaComputação,trabalha
comoArquitetodeSoluçõesparaumaconsultoriaSAP,focandodesde2006
nodesenvolvimentoABAPesuasramificações. ÉcocriadordositeABAP-
Zombie,quetentaprevenirqueconsultoressetornemzumbisdetantotraba-
lhar,compartilhandoconhecimentoatravésdeartigostécnicosqueensinam
deformadivertidasobreosmaisdiversostemasdoMundoSAP.Gostamuito
deartesmarciais,músicasestranhas,indiegamesedetestarsistemasopera-
cionais,appselinguagensdeprogramaçãodiferentes.
iv

## Página 7

CasadoCódigo
Lista de discussão
Casovocêqueiraconversarcomigoecomoutrosleitoressobrealguns
dostópicosouassuntosdestelivro,inscreva-senalistadediscussão(via
e-mail),pormeiodolink: http://forum.casadocodigo.com.br/.
v

## Página 9

CasadoCódigo
Agradecimentos
ParatodosaquelesqueacessamoABAPZombie
AcriaçãodestelivronãoexistiriasemaspessoasqueacessamoABAPZombie
diariamente. Agradeçoimensamenteatodospelosfeedbacks,críticas,dis-
cussõeserisadascompartilhadaspormeiodosite.Muitoobrigadoatodosos
consultoresquedeixaramdevirarzumbisporcontanossostextos!
ParaagaleradoSELECTemLOOP
Muitagenteachaquesoumaluco,masmalucoqueémalucoprecisacom-
partilharsuamaluquicecomalguém.Semosuportediáriodaminhaesposa,
Stella,meusprojetosnãotomariamvida.Elaéquemmemantémnocaminho,
comconselhosquepotencializampositivamentetudooquefaço. Palavras
nuncaserãosuficientesparaexpressaraminhagratidão.
Véio,semosuportedomanoMauroesserolênãoteriavistoaluzdodia.
Essemalandroécheiodefitas,quebradas,golsquadrados,ZLs,motocas,ver-
meseumaamizadesemlimites.Valeumaaano!Juntoscontinuaremosnossa
disputadiáriacontraanossaarqui-inimiga,umataldePriscila,aquemtam-
bémagradeçopelasconversas,risadas,aranhasedoideiras.Valeumaaaano
aoquadrado!
Aosoutros3 brothersquetambémmantêmamáquinaABAPZombiefun-
cionando:manodoMetal,manoMentoradoemanadaTattoo–obrigadopor
fazerempartedaequipe!
ODaniloprecisoufalarcomigoumas4vezesatéeuaceitaraideiadolivro.
Obrigadopornãoterdesistidodemeconvencerdessaideiaeporserumdos
meusprincipaiscomparsasnabuscapeloentendimentodestemundo.
Ronildo,RabayeDanilo(denovo),obrigadoporteremmeajudadona
revisãodeconteúdodolivro. Ofeedbackdevocêsfoiextremamenteim-
vii

## Página 10

CasadoCódigo
portante,eeuprecisareipagarcafésavocêsatéoinfinitoparacompensar!
AgradeçotambémàCasadoCódigopelaoportunidade,especialmentepara
aVivianportermeajudadotantoduranteaescrita.Valeu!
Eutrabalheicomtantaspessoasemclientes,projetoseconsultorias,que
seriaimpossíveldecitartodomundo.Saibamquetodoscontêmumaparcela
deresponsabilidadeportudoquecercaestelivro. Meumuitoobrigadoaos
ABAPers,funcionais,BASIS,gerentes,sócios,líderese <insiraumcargo>
comquemtrabalhei.
Porfim,deixoosmeusagradecimentosparatodaagaleradacomunidade
SAPqueconheciporcontadoABAPZombie.Muitoobrigadoporapoiarem
omeutrabalho,ecompartilharemmomentospolêmicosecômicosdodiaa
dia!
Paraaquelesquepensamqueeuseiarrumarimpressoras
Dionisio,LuizaeMarcos.Trêspessoasquenãocontêmamesmapaixão
queeutenhoportecnologia,massempremeapoiamcegamenteemminhas
escolhas.Dedicareiomeumelhorparasempretrazerfelicidadeavocêsatra-
vésdessemontedenomes,siglaseaparelhos“estranhos”. Muitoobrigado,
família.
Emdiversosmomentosdaminhavida,deparo-mecommomentosnos-
tálgicosporcontadasaventuras undergroundsquetivecommeusamigosOtit,
RedArsenaleCarzombie.Nossaamizadeehistóriasãomuitoimportantes.
Obrigado!
Oenvolvimentocomartesmarciaismudou(econtinuamudando)ami-
nhavida. AgradecereieternamenteaomeumestreeamigoCelsoRodri-
gues,portudoqueaprendinosanosemquetreineiHapkido. Muitoobri-
gado!Agrade çotambémmeusSenseisdeKendo,YoshiakiKishikawaeMi-
tikoKishikawa,quedesenvolvemumtrabalhofantástico,econtribuempara
queeumantenhaminhamenteserenaemeuespíritoforte.
Abraçosatodosaquelesqueestãolendo,leramoulerãoestelivro!:)
viii

## Página 11

CasadoCódigo Sumário
Sumário
1 Porondecome çar? 1
1.1 QueméSAPeoqueéoABAP? . . . . . . . . . . . . . . . . . 2
1.2 ConsultoriasSAP . . . . . . . . . . . . . . . . . . . . . . . . . 6
1.3 Academiasseletivas . . . . . . . . . . . . . . . . . . . . . . . . 7
1.4 CursosdeABAP . . . . . . . . . . . . . . . . . . . . . . . . . . 8
1.5 TrabalhocomXYZequeromigrarparaSAP . . . . . . . . . 9
1.6 Abuscaporvagas . . . . . . . . . . . . . . . . . . . . . . . . . 12
1.7 Eujáfizocursoetal...Possoparardeestudar? . . . . . . . . 14
2 ArelevânciadoABAPparaomercadodeTI 17
2.1 OsprimórdiosdoABAP . . . . . . . . . . . . . . . . . . . . . 18
2.2 SemSAP,semABAP . . . . . . . . . . . . . . . . . . . . . . . 21
2.3 Problemasouoportunidades? . . . . . . . . . . . . . . . . . . 23
2.4 SAPéomundoperfeito . . . . . . . . . . . . . . . . . . . . . . 24
3 CertificaçõesABAP 27
3.1 Certificaçãoeasconsultorias . . . . . . . . . . . . . . . . . . . 28
3.2 Oscavaleirosdacertificação:Certification5 . . . . . . . . . . 29
3.3 CertificaçãoeclientesSAP . . . . . . . . . . . . . . . . . . . . 31
4 Osbastidores 33
4.1 Comosurgemasalocações? . . . . . . . . . . . . . . . . . . . 34
4.2 Adan çadascadeiras . . . . . . . . . . . . . . . . . . . . . . . 36
4.3 Mecânicadetrabalho . . . . . . . . . . . . . . . . . . . . . . . 38
4.4 Eentãovemapróximaalocaç ão . . . . . . . . . . . . . . . . . 41
ix

## Página 12

Sumário CasadoCódigo
5 Carreira,motivação,universoetudomais 43
5.1 SeráquetodoABAPerémesmoumconsultor? . . . . . . . . 44
5.2 Nãosejaatingidopelodespreparoalheio . . . . . . . . . . . . 49
5.3 Desvalorizaçãodomercado . . . . . . . . . . . . . . . . . . . 51
5.4 Ovalordarevisão . . . . . . . . . . . . . . . . . . . . . . . . . 52
5.5 Estudosecomunidade . . . . . . . . . . . . . . . . . . . . . . 56
5.6 ABAPéumlixo,vamosvendercoconapraia . . . . . . . . . 59
6 OstabusdomundoABAP 63
6.1 Fantasmasdopassado . . . . . . . . . . . . . . . . . . . . . . . 64
6.2 Impactosnosprocessodedesenvolvimento . . . . . . . . . . 66
6.3 NomeclaturasemABAP . . . . . . . . . . . . . . . . . . . . . 70
6.4 Vidaeobradasconstantesinúteis . . . . . . . . . . . . . . . . 74
6.5 Paredeescreverdocumentaçõesquenãoserãolidas . . . . . 80
6.6 AartemilenardecomentarcódigosABAP . . . . . . . . . . . 87
6.7 UsabilidadeemprogramasABAP . . . . . . . . . . . . . . . . 94
7 Sobreprogramaçãosemcódigos 99
7.1 Odilemadospoucosusuários . . . . . . . . . . . . . . . . . . 100
7.2 Duvidedocaminhomais“fácil”. . . . . . . . . . . . . . . . . 102
7.3 Mesclandoovelhocomonovo . . . . . . . . . . . . . . . . . 104
7.4 Reutilizaçãolocalaoemvezdecópiaexterna . . . . . . . . . 109
7.5 Acavernadefones . . . . . . . . . . . . . . . . . . . . . . . . . 115
8 Oquevemporaí? 117
8.1 SAPNetweaverGateway . . . . . . . . . . . . . . . . . . . . . 118
8.2 SAPUI5eOpenUI5 . . . . . . . . . . . . . . . . . . . . . . . . 124
8.3 SAPFiori . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
8.4 HANA,HANA,HAHA...emaisHANA . . . . . . . . . . . . 128
8.5 AposiçãodoABAPno“novomundo”. . . . . . . . . . . . . 133
x

## Página 13

CasadoCódigo Sumário
9 ApêndiceI–AprendendoABAPporcontaprópria 139
9.1 Aprendainglês. . . . . . . . . . . . . . . . . . . . . . . . . . . 140
9.2 EntendabemoqueSAPERPeABAPqueremdizer . . . . . 141
9.3 SAPemcasa:criandosuaestaç ãodetrabalho . . . . . . . . . 142
9.4 Aprendaaprogramarobásico . . . . . . . . . . . . . . . . . . 143
9.5 Omaravilhosomundodoslivrosqueensinamtudoemais
umpouco . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
10 ApêndiceII–Linkseindicações 147
10.1 Publicações,sites,guias,artigoselivroscitados . . . . . . . . 147
10.2 Recomendaçõesadicionais. . . . . . . . . . . . . . . . . . . . 151
xi

## Página 15

Capítulo1
Porondecome çar?
Équasesempreamesmahistória:algumprofissionalSAPdáaoseuamigoa
famosadicadequeomercadoSAPéaúltimamaravilhadomilênio,comuma
demandaaltíssimadeprofissionaisesaláriosbemacimadamédiabrasileira.
Nãoédifícilencontrarhistóriasdeprofissionaissemformaç ãoemTIque
largaramtudoparatentarumavaganomundoSAP,masérealmentecustoso
encontrarpessoasquefizeramissoetiveramsucessonaempreitada.
Comalgumasdicassimples,épossívelprevenir-sedeuminíciotraumá-
tico. Aanálisepréviadecomoomercadocomporta-seequaissãoassuas
opçõespoderásalvarumagrandequantidadedoseutempoedinheiro.Neste
capítulo,vamoscome çaraentenderumpoucosobreoqueéABAP,comoo
mercadofuncionaequaisasop çõesparaquevocêpossaingressarnessaárea.

## Página 16

1.1. QueméSAPeoqueéoABAP? CasadoCódigo
1.1 Quem é SAP e o que é oABAP?
SAPéumaempresaalemãespecializadaem enterprise software(softwarecor-
porativo).Elapossuiumportfólioenormedeprodutosparaajudarempresas
amaximizaremosseusnegócios.SeumaiorprodutoaindaéoSAPERP,um
grandepacotedeferramentasquepermiteacriaç ãodeprogramasparaprati-
camentequalqueráreadaempresa.Comele,épossívelintegrardiversasáreas
eprocessosemumsólugar.
Oprodutoéumgigantedomundoempresarialeéamplamenteusado
porempresasdegrandeporte,comoveremosnocapítulo 2. Entretanto,é
importantedestacarque,nosúltimosanos,aempresavembuscandoadi-
versificaçãodeprodutos,eáreasdeatuaçãocomnovidadesqueenvolvamo
trabalhodeváriostiposdedesenvolvedoreseprofissionaisdeTI,conforme
apresentaremosnocapítulo 8.
TodaaprogramaçãodoSAPERPéfeitautilizandooABAP(Advanced
Business Application Platform),linguagemdeprogramaçãode4ªgeração,cri-
adanosanos80juntoaoSAPERP.OABAPémoldadoespecialmentepara
lidarcomasdiferentespartesdoERP.
Elecontémumasériedefuncionalidadesparafacilitaraimplantaç ãode
regrasdenegóciocomplexaseamanipulaç ãodeumaenormequantidadede
dados. Eletambémécapazdefazerintegraçãodesistemasexternoscomo
SAPecriarinterfaces(telas)paraosusuários,acessíveispormeiodetransa-
çõesdoERP(umaespéciedelinkparaumprograma).
2

## Página 17

CasadoCódigo Capítulo1. Porondecomeçar?
Fig.1.1:TelainicialdoSAPERPfeitaemABAP
QuandoumclienteimplementaoSAPERPemsuaempresa,eleganha,
porpadrão,umasériedeprogramasABAPcriadospelaprópriaSAP.Esses
programascontêmlógicasprontaspararesolverdiversosproblemascomuns
nasempresas,alémdeintegraremofuncionamentodeáreasdistintas.Sãopo-
pularmenteconhecidoscomo programasstandard,criadosemantidospela
própriaSAP.Aolongodotempo,écomumquenovosprogramasstandards
sejamfeitosequeosantigossejamatualizados.
OsdesenvolvedoresABAP(ouABAPers)quenãoestãoligadoscoma
SAPvãoatéasempresasparaimplantarregrasdenegócioespecíficas.Cada
empresatemalgumaparticularidadeemseuprocesso,quenãotemrelaç ão
comoutrasempresasdoseusegmento. Essaslógicassãocriadasdentrodo
ERP,emprogramascustomizados.Quemcriaeespecificaessesprogramas
sãoosfuncionais,profissionaiscapacitadosementenderoprocessodocli-
enteeestruturarofluxodainformaç ãodentrodoSAP.OABAPercriaráos
3

## Página 18

1.1. QueméSAPeoqueéoABAP? CasadoCódigo
programascombasenasregrasdescritasnessasespecificações.
Fig.1.2:ExemplosimplesdeumatelacriadacomoABAPclássico
OfocodestelivroéoABAP,maséimportantesaberqueotrabalhodo
ABAPerrequerumasériedeinteraçõescomdiferentestiposdeprofissionais
quetrabalhamnaárea.Usaraexpressão mundo SAPnãoénenhumexagero,
dadaaquantidadedepessoascomasmaisdiferentesformaçõesehabilidades
(RH,financeiro,administração,vendas,materiaisemais20áreascorpora-
tivasàsuaescolha).Mesmodentrodaáreadeprogramaç ãoABAP,existem
diversasramificaçõeseespecializaçõesemferramentas,como: Webdynpro
ABAP,Workflow,CRM,SRM,HReAPO,todosprodutoseextensõesdaSAP
querequeremprogramaçãoABAPemsuaimplantação.
4

## Página 19

CasadoCódigo Capítulo1. Porondecomeçar?
Fig.1.3:EditorABAPacessadopormeiodaSAPGui:umclienteparaexibiç ão
dastelasdoSAPERP
Háumfatoquepodeparecerestranhoparaquemnãoéiniciadonaarte
SAP:asempresasquepossuemoSAPERPnormalmentenãocontamcom
grandestimesinternosparafazerasnovascustomizações.Geralmente,elas
contamcomtimesqueajudamamanterosistemafuncionando(umaequipe
desuporte),epreferemcontratarprofissionaisexternos,detemposemtem-
pos,paraimplantarnovasfuncionalidades(ouautomatizações)noformato
deprogramasABAP,organizandoessasatividadesemumprojeto.
SeelasprecisaremdessesprofissionaisSAP“externos”,aquemelaspodem
recorrer?
5

## Página 20

1.2. ConsultoriasSAP CasadoCódigo
1.2 Consultorias SAP
AsempresasquecontêmamãodeobraespecializadadomundoSAPsãoas
consultorias.Elasservemcomoumintermediárioentreanecessidadedocli-
enteeosprofissionaisSAP.Emresumo,elassãoespecializadasemterceirizar
otrabalho,montandoequipese/ouencontrandoprofissionaisparasupriras
demandasdosclientes.
Trilhandoestecaminho,hágrandeschancesdevocêingressarnomundo
SAP,trabalhandoparaumaconsultoria,poisonúmerodeABAPerstraba-
lhandodiretamenteemclientesnãocostumasermuitogrande.Tambémnão
écomumqueempresasterceirizemotrabalhoABAPsemointermédiodas
consultorias,fazendoumcontratodiretocomosprofissionais–hálendasur-
banasdeissoteracontecidomuitonopassado,mas,hojeemdia,háumasérie
dequestõespolíticas/trabalhistasnasempresasquetornamcontratosdesse
tipoextremamenteraros.
Existemconsultoriasdosmaisdiversostipos,dasgigantesemultinacio-
naisatéaspequenasquenãopossuemnemumescritório,atuandosomente
comointermediáriasvirtuais.Elassãomotivosdeamoreódio,frutodeum
mercadoquecontémumaconcorrênciaacirrada.Écomumescutarhistórias
deconsultorias“mercenárias”,pornãotratarembemseusprofissionais,como
tambémencontrarABAPersquetrabalhamhámuitosanosparaamesma
consultoria,pormanteremumarelaçãointernasaudávelelivredecomplica-
ções.
A grande questão para os iniciantes é como conseguir um emprego
nessasconsultorias. Osclientesdificilmentepagarãoporprofissionaisque
estão aprendendo, os juniores. As demandas geralmente exigem níveis
pleno/sênior,eissocriaumabarreiraimensadeentrada. Mesmocomessa
escassezdetrabalhoparaosiniciantes,asconsultoriassabemqueépreciso
formarnovosprofissionaisparaomercado;casocontrário,elasficarãoeter-
namentedegladiando-sepelasmesmaspessoas.
Nasequência,vamosanalisaralgumasformasdeingressarnaárea.
6

## Página 21

CasadoCódigo Capítulo1. Porondecomeçar?
1.3 Academias seletiv as
Émuitopopularousodotermo“academia”paradesignartreinamentosdo
mundoSAP.Elascostumamsercursosextensos,atingindoumnívelconside-
ráveldedetalhes.NemtodasasáreasdomundoSAPdispõemdeambientes
gratuitosparatesteeestudo(comoasáreas“funcionais”),oquereforçaofor-
matolongodocurso.
Hámuitasacademiaspagasofertadasnomercadobrasileiroemundial–
presenciaisouonline–,cobrindopraticamentequalquerassuntorelacionado
aosprodutosSAP.Aacademiaseletivaéomodoqueconsideromaiscômodo
parainiciantes.AcabeientrandonessemundomalucodosERPsporela.
Éimportantequeeulheaviseque“academiaseletiva”éumnomein-
ventadopormim,paraexplicaressaprática. Nãovábaternaportade
empresasfalandodisso(mas,sefizer,mande-meume-mailcontando
comofoi).
Elafuncionaassim:aempresausaaacademiadeensinodalinguagemeo
ecossistemaABAPcomopartedoseuprocessoseletivo.Vocêtemachancede
aprenderatrabalharcomABAPsemcusto,masaempresareservaodireito
denãolhecontratar,casovocênãocorrespondaàsexpectativas.
Essasvagasnormalmentesãoabertasparaestágios,tendocomoalvoprin-
cipalestudantesqueestãocursandoafaculdade,ouquesãorecém-formados.
Existemcasosdeestamodalidadetertidocomoalvopessoasqueestãomi-
grandoparaoSAP,vindodeoutrastecnologias,massãocasosbemmenos
frequentes.
Geralmente,empresasconsideradasgrandesnomundodasconsultorias
deTItêmessapostura,comoaprimeiraempresaparaqualtrabalheicomo
ABAPer. Nomeucaso,possodizerquenãofuieuqueescolhioABAP,na
verdadefoialgumprofissionaldaáreadeR&S(RecrutamentoeSele ção).
Quandoeuestavafazendooprocessoseletivo,existiamduasacademias-
seletivas:umaparaJava,outraparaABAP.Sejapeloalinhamentodosplane-
tas,pelohumordorecrutador,oupelaminhacaradeSAP(o?),fuipararna
academiaABAP.EéporissoquehojenãoexisteumsitechamadoJavazombie.
7

## Página 22

1.4. CursosdeABAP CasadoCódigo
Sevocêestivernafaculdade–maiorpúblicoalvodeempresascomessa
modalidadederecrutamento–,esseé,delonge,omelhorcaminho.Prepare-
separaumprocessoseletivocomplexo(comumnessetipodevaga),masque
seráextremamentegratificanteseconcluídocomsucesso.Obviamente,acon-
sultoriaesperaráquevocêmantenhaumarelaçãodelongoprazocomela,de
formaqueelapossaformarumprofissionalaseusmoldes.
1.4 Cursos de ABAP
VáriasempresasministramcursospagosdeABAP,edeváriasoutrasáreasde
SAP,emdiversascidadesdoBrasil.VocêpodefazerocursonaprópriaSAP,
emumaescolaautorizadaqueutilizaomaterialdaSAP,ouemumaescola
queministraocursousandomaterialpróprio.
Entretanto,arealidadedodiaadianosmostraqueterfeitoumdesses
cursosdeABAPnãogarantiráquevocêconsigaumaposiçãonomercadoem
curtoprazo(àsvezes,nemmesmoalongoprazo). Muitagenteachaqueé
fácilconseguirempregonomundoSAP,porcontadaquantidadeenormede
vagasnãopreenchidas.Entretanto,vocêjáseperguntouquantasdessasvagas
sãoparaconsultoresjuniores?
Muitasconsultoriasdepequenoemédioporte(maioresofertadorasde
vagas)têmdificuldadeemmanterprofissionaisnovos,jáqueasempresasque
têmoSAPERPinstaladosempredãopreferênciaaosprofissionaisexperien-
tesparadesenvolverseusprojetos.Comoaconsultoriavivedaprestaç ãode
serviços,oseufocoprincipalémanterumaequipecomumníveltécnicoalto,
paraproverserviçosdequalidade,oquegeraumabrigapelosmesmospro-
fissionais.
Nessahistóriatoda,quemsofresãoosiniciantesnaárea.Émuitocomum
encontrarrelatosdepessoasquefizeramocurso,gastandoumaquantidade
consideráveldetempoedinheiro,parafalharnahoradeconseguirumapo-
siçãodejúnior.
Éclaroqueocursoéumpontodepartida,masvocêprecisaserrealista
quandoavaliarasop ções. Nãováachandoquevocêvaiconcluirocursoe
conseguiráumempregonapróximasemana.Issosóacontecerásevocêen-
contrarconsultoriascomdemandaparajuniores–oqueéraro–,ousetiver
8

## Página 23

CasadoCódigo Capítulo1. Porondecomeçar?
umQI(quem-indica)dealtonível.
Háquemdigaqueumcertificadopodeserumgrandediferencial,mas
quemédaáreasabequeotemacertificaç ãoestárelacionadoaumasériede
polêmicas,comovamosexplorarnocapítulo 3.
Masacalme-se,nãoestoudizendoqueéimpossívelvirarprogramador
ABAP.Pelocontrário!Éimportantevocêsaberquenãovaisertãofácilcomo
aqueleseuamigoquejáestánaáreadiz,equevocêterádesededicarmuito
paraconquistaroseuespaço.Ocursoésóoprimeiropassodeumagrande
caminhada.
E se você fizesse tudo por conta própria?
Ospassosdescritosnestecapítulodãoumaideiageraldecomoo
mundoABAPfunciona.Muitagentesegueocaminhonatural:fazeruma
academia,pagandoporumcurso,paraaprenderatrabalharnalingua-
gem.Masháumaoutraforma:aprendertudosozinho!Sevocêédotipo
quegostadeestudarporcontaprópriaenãodesistefrenteàprimeira
dificuldade,aproveiteasdicasdoapêndice,nocapítulo 9,paraingressar
diretonomundoABAP,enquantolêorestodolivro.:)
Importante:sevocêquervirarumprogramadorABAP,experiênciaspré-
viascomprogramaçãovãoajudá-loasedestacar.Nomundododesenvolvi-
mentodesoftware,nãoéalinguagemdeprogramaç ãoquevaidizerseum
programadorérealmentebomounão.Umbomprogramadordeveriacon-
seguirtransitartranquilamenteentremaisdeumalinguagem.
Eporfalardeprofissionaisdeoutrasáreas...
1.5 Trabalho com XYZ e quero migrar para SAP
OmundoSAPatraitodotipodegente(jáviadvogadoseatédentistas),nor-
malmenteporcontadossalários:apessoaencontraalgumapesquisasalarial
deSAPnainternet(entendeuadica,certo?) evêqueumempregosimilar
aoseu,nomundoSAP,temumsaláriomaisalto. Aprincipaldúvidaése
asuabagagemeexperiênciadeoutrossistemas/linguagenslhedaráalguma
vantagemnahoradaprocuradonovoemprego.
9

## Página 24

1.5. TrabalhocomXYZequeromigrarparaSAP CasadoCódigo
Eu,sinceramente(ouseráinfelizmente?),achoquedependemuito.
Muitasconsultoriastrabalhamcomalocaçõesporprojetos,eelassãoas
quemaisofertamvagasnomercado. Essetipodeconsultoriadificilmente
levaráemcontaalgumabagagemprévianomomentodacontratação:sevocê
acaboudefazeraacademiaABAPeéumjúnior,nãovaiimportarmuitose
vocêtrabalhou10anoscomCOBOL(COmmon Business Oriented Language).
“Você é um júnior. Não tem experiência e não terá espaço em um projeto
onde tudo precisa ser feito em prazos apertados”,diriaaconsultoria.Podepa-
recerumapráticamercenária,maséummeioquealgumasconsultoriasen-
contramparasobrevivernomercado,jáqueenviarumprofissionalquenão
resolvaoproblemadoclientepoderesultarnodeméritodotrabalhodacon-
sultoriacomoumtodo.Seissoécertoouerradoéumadiscussãoàparte.
Porém, existem algumas consultorias que mantêm profissionais SAP
comopartedesuaequipe–emvezdealocarporprojetos–,fazendocom
queelestransitememseusclientes. Essetipodeconsultoriadeveseroseu
focoprincipal,poiséinteressanteparaelamanterumaequipediversificadae
quepossaatenderclientesemmomentos-chave.
Nessecaso,asuaexperiênciade5anostrabalhandocombancodedados
podeviracalhar,quandosurgirumaintegraç ãocomalgumbancodedados
externo.ASAPtambéméconhecidaporlan çarumasériedeprodutosnovos
acadaano,emuitosdelestransitamemoutrasáreas,comoAndroid,iOS,
HTML5,CSS3,Javaetc.
SevocêpretendemesmomudarparaSAP,invistafortementeedemons-
trequeasuaexperiênciafaráadiferen çaparaseuaprendizado,encurtando
otempoatéatingirumnívelemquevocêconsiga“andarcomaspróprias
pernas”.Sónãoseassustecasoalguémignoresuaexperiênciaprévia,mesmo
sendoalgorelacionadoàTI.Sinceramente(ouinfelizmente?),achancede
issoacontecerébemalta.
MasoABAPémuitoantiquado...
Émuitocomumescutaressetipodefrase. OABAPérealmenteuma
linguagemdeprogramaçãoantiga,masestáemconstanteevolução.
Novas featuressãocriadastodososanos,emuitasdelassãoequivalentes
afeaturesdelinguagensdeprogramaçãomodernas.Oquegeramuitodesses
10

## Página 25

CasadoCódigo Capítulo1. Porondecomeçar?
comentárioséofatodeaSAPmanteraretrocompatibilidadeemseusistema,
ouseja,umadeterminadafuncionalidadeABAP,criadanosanos80,pode
continuarfuncionandoatéosdiasdehoje.
UmABAPerqueteveumaformaçãonosanos90enãoseatualizou ainda
consegueentregarprogramasABAPquefuncionamparaosusuários. Esse
fenômenogeraumasériedeproblemasnaáreaeserábastanteabordadono
decorrerdolivro.
Oprincipalésaberqueexisteinovaç ãoeevoluçãonomundoSAP,po-
rémaimplantaçãodessasinovaçõesdependerásempredosclientes.Jáqueos
ABAPersprestamserviçosparaasempresas,elessempredependerãodelas
implantaremnovosprodutosdaSAP,parautilizarasnovasfun çõesdalin-
guagemABAP–épossíveltestaremambientesTrial,masaimplantaçãoreal
dependedasempresas.
AdinâmicaémuitodiferentedeoutrosmercadosdeTI,comoodede-
senvolvimentoWeb,ondeachancedevocêusaralgonovoéumaconstantee
dependemaisdasdiretrizesdefinidaspelaequipedoseuprojeto,doquede
algumcontratomultimilionário.
11

## Página 26

1.6. Abuscaporvagas CasadoCódigo
Fig.1.4:Umdosexemplosdessaevoluçãoéque,háalgunsanos,jáépossível
programaremABAPpeloEclipse
Dequalquerforma,adisposiçãoparaenfrentaressemercado,trazendo
ideiasinovadoras,podeserumgrandediferencial. Talvezvocêpreciseas-
similaralgumascoisasdopassadoprimeiro,masexistemmuitosABAPers
interessadosemaprender,implantaredesenvolveressasnovastecnologias.
1.6 A busca por v agas
Comtodoesseentendimentodasop ções,éimportantesaberondeanalisar
asvagasquesãoofertadasdiariamentenomercado.Apesardapopularizaç ão
doLinkedIn,boapartedasvagasdomundoSAPdoBrasilaindaéanunciada
porlistasdee-mail,quenasceraminicialmentecomolistasdediscussão,e
acabaramvirandolistasdevagas.
Vezououtravocêencontraráalgumasdiscussõessobrecoisastécnicas,
12

## Página 27

CasadoCódigo Capítulo1. Porondecomeçar?
masapostoquevocêvairecebermuitomaise-mailscomvagas. Sãotantos
pordiaqueachoválidovocêcriarumacontaseparada,sóparaassinaressas
listas,anãoserquevocênãotenhaproblemasemlidarcomumacaixade
entradacaótica.
ListasquevocêpodeseguirparavagasABAP:
• abap-sap@grupos.com.br
• abap-4@yahoogrupos.com.br
Sevocênãosabecomoentraremumgrupodee-mail,pesquise!
QuasetodomundodeSAPABAPnoBrasilsegueessaslistas,portanto,
precisoressaltarumacoisaquevejotodasemana: sevocêformandarseu
CVparaalgumavaga,cuidadoparanãoenviá-loparaogrupotodo.Parece
umacoisabásica,mastodasemanaalguémcometeesseerro.Vejanoe-mail
davagaparaqualendere çodee-mailvocêtemdemandarseuCV,emande
somenteparaele.Obrigado.:)
OFacebooktambémestápopularizando-senocompartilhamentodeva-
gas. ProcurepelosgruposdeSAPeABAP,efiqueligadonasvagasqueas
recrutadorascompartilham.
TaxaHoraeaArtedeserum“Sombra"
Vocêfezocurso,entrounaslistas,viumilhõesdevagas... Esemprea
pessoaqueestárecrutandopedea“pretensãosalarial”.
Sevocêéuminiciante,éóbvioquevocênãovaisaberquantopedir.Como
jácomentei,existempesquisassalariaispúblicasdeSAPnainternet,para
quevocêtenhaumabasedosvalores. Seforasuaprimeiraoportunidade,
nãoexijavaloresaltos,principalmenteporquevocêestaráconcorrendocom
outrosiniciantes. Nestemomento,dêprioridadeaadquirirconhecimento.
Preocupe-secomsaláriosapóstercondiçõestécnicasdeexigirumvalorade-
quado.
Dizalendaquealgumasconsultoriascontratamjunioresparatrabalha-
rememprojetoscomo Sombras.UmSombraéumapessoaquenãotemcusto
paraoprojetoeestáaliunicamenteparaficaraoladodealguémmaisexpe-
riente,afimdeaprenderotrabalhoe,posteriormente,sercontratadocomo
júnior.
13

## Página 28

1.7. Eujáfizocursoetal...Possoparardeestudar? CasadoCódigo
Apesardeeuterdito“lenda”,jáouvirelatosdequeessetipodecontra-
taçãoexiste,porémébemrara. Sevocêencontraralgodotipoenãotiver
umanecessidademonetáriaurgente,agarreessaoportunidade.Aprenderna
práticaésempremelhor.
1.7 Eu já fiz o curso e tal...P osso parar de estu-
dar?
Claroquenão! Otrabalhonaáreadetecnologiamuitasvezesrequerque
vocêencontrerespostasparaquestõesdodiaadiaporcontaprópria. Você
vaiutilizarmuitooGoogle,podeapostar.
Hátambémenormeschancesdevocêencontrarrespostasnositequea
própriaSAPmantémparasuacomunidadedeprofissionais,chamado SAP
Community Network(SCN).Vocêencontrarátoneladasdeinformaçõessobre
(quase)qualquercoisadequevocêprecise,como:apostilas, e-learning,fóruns
dediscussão,blogs,apresentações,wikisetc.
OSCNéoprincipalportalparatécnicosdomundoSAP.Aleiturare-
correntedosartigosediscussõessãoessenciaisparaevoluirnacarreiracomo
ABAPer.
UmaoutraótimafonteparaestudossemcustoséositeOpenSAP(http:
//open.sap.com/),quecontémcursoscompletos,feitospormeiodevídeos,
comomaterialpreparadopelaprópriaSAP.Eomelhor: étudocompleta-
mentegratuito.Masadivinhesó:étudoeminglês.
Ficaaquia principaldicadestelivro:sevocênãosabeinglêsequertraba-
lharcomSAP(ouTI),saibaquevocênãovaipoderaproveitarquasenadado
quetemnainternetevaiperdermuitasinformaçõesvaliosasquecertamente
iriamajudá-lonodiaadia.ExistemblogsnacionaiscomooABAPZombieeo
ABAP101,masaquantidadedeinformaçãoémuitopequenaemcomparação
aovolumemonstruosogeradopelacomunidadeinternacional.
Comunidadesdeoutraslinguagenstêmfórunsnacionaiscommuitasin-
formações,comooGUJ(Java),masaindanãotemosnadasimilarquefunci-
onetãobemparaABAP,eachopoucoprovávelqueissoaconte çanofuturo.
14

## Página 29

CasadoCódigo Capítulo1. Porondecomeçar?
VirandooABAP-Master-Blaster
Seguindoessasdicas,épossívelviraroSAP-Mega-Master-Blaster? De-
pende!
Dependedoquê?Desuadedicaçãoedesuavontadedetersucessonessa
área.
Eudefendoquetodomundoécapazdefazerqualquercoisa,desdeque
tenhavontadeededicação.Ocaminhopodeserárduo,mas,compaciência
epersistência,vocêchegalá. Maisumavez: conseguirumempregocomo
júniorésóoprimeiropasso.Umcomplicadopassoparaalguns,éverdade,
massomenteoprimeirodeumajornadarecheadadedesafios.
Leia relatos de iniciantes
Escrevi pela primeira vez sobre iniciantes em um post do ABAPZom-
bie, chamado de Guia do ABAP Noob (http://bit.ly/2biqp6f) . A versão 
deste livro é mais completa e atualizada, mas esse post contém diversos 
comentários, com muitos relatos interessantes sobre os passos iniciais do 
mundo SAP.
Recomendoaleituradostextosparatodosdaárea!
15

## Página 31

Capítulo2
ArelevânciadoABAPparao
mercadodeTI
OABAPnãoéumalinguagemdeprogramaçãopopular.Hágrandeschances
deprogramadoresmaisnovosnãofazeremamenorideiadequeelesequer
existe.Eumesmo,quandocomeceinomundoSAPeaindaestavacursando
afaculdade,tivedeexplicarparamaisdeumdosmeusprofessoresdoque
setratavaotalABAPcomqueeutrabalhava.Éclaroque,commeussólidos
conhecimentosdeestagiáriode2meses,devoterdadoumaexplicaç ãocom-
pletamentesuperficialecontribuídocomaimpopularidadedacoisatoda.
Nocomeço,euprocuravaexplicaroABAPrelacionando-ocomautili-
dadedeumERPparaumaempresa.Easpessoasmeolhavamestranho.Mas
depoisdeumtempo,enfim,chegueiaumaexplicaç ãobemmaiscompreensí-
velparahumanosqueentendem(ounão)códigosbinários:sevocêconsome

## Página 32

2.1. OsprimórdiosdoABAP CasadoCódigo
produtosouserviçosdegrandescorporações,hágrandeschancesdeoABAP
fazerpartedasuavida,semquevocêsequerfaçaideia.Éparacriarprogramas
paraotimizarprocessosdessasgrandesorganizaçõesqueoABAPerexiste.
Paraquevocêtenhaumadimensãodotamanhodoecossistema,dados
oficiaisdivulgadospelaSAP(emjaneirode2015)indicamque98%das100
empresasmaisvaliosasdomundocontêmalgumtipodeprodutoSAPem
suasoperações.Das2.000empresaslistadascomoasmaioresempresaspú-
blicaspelaForbes,87%delasãoclientesSAP.
Osvaloresmovimentadosanualmentenessemercadoultrapassamfacil-
menteacasadosbilhões(deeuros).Dariaparacomprartodaamáquinaque
movimentaaMegaSenaeaindasobraria(muito)dinheiro.
Seessemercadoétãogigantescoeimpactaavidadetantaspessoas
(mesmoqueportabela),porqueeleétãodesconhecido,mesmoentreosen-
volvidoscomomercadodeTI?Arespostadessaperguntaestádiretamente
relacionadacomasraízesdaSAPcomoempresa.Nestecapítulo,vamosava-
liarbrevementeahistóriadaSAPparaentenderporqueesteéummundotão
“fechado”.
2.1 Os primórdios do ABAP
ASAPéumaempresaanciã,seconsiderarmosadinâmicadacriaç ãodasem-
presasdostemposatuais.Foicriadanoiníciodosanos70,porumgrupode
cincoex-funcionáriosdaIBM,comofocodeautomatizareintegrarprocessos
corporativosatravésdesoftwares.
Jánaquelaépoca,anecessidadedeterdadosrelevantesemtemporealera
algomuitoimportanteparaempresas.EosistemadaSAPfocavaexatamente
nisso,gerandoinformaçõesquandoelaseramrequeridasemvezdefazê-lo
duranteprocessamentosnoturnos(eramuitocomumrodarprocessamentos
complexosdeinformaçõesànoite,quandoninguémestavatrabalhando).
Essesistemaintegradoecomprocessamentoemtemporealevoluiuaté
chegarnochamadosistemaR/2,quetevesuaprimeiraversãolan çadanofinal
dosanos70. FoioprodutoprincipaldaSAPdurantetodoadécadade80.
Nessaépoca,ABAPjádavaascaras,engatinhandocomoumalinguagempara
gerarrelatórios.
18

## Página 33

CasadoCódigo Capítulo2. ArelevânciadoABAPparaomercadodeTI
Masfoisomenteem1992,comacriaç ãodochamadoSAPR/3(ERPcom
arquiteturaem3camadas–apresentação,aplicaçãoebancodedados),que
oABAPganhoufor ça,comobasedeprogramaç ãodetodosistema. Prati-
camentetodasasaplicaçõeseprocessosinternosdoR/3foramcriadasem
ABAP,sendotambémalinguagemutilizadaparacriarextensõesnosistema,
combasenosrequerimentosdecadaempresa.
Osistemaéseparadoemmódulos(vendasedistribuiç ão,gerenciamento
demateriais,RHetc.)eémuitoflexível,podendoserimplantadoemempre-
sasdesegmentoscompletamentedistintos(porexemplo,empresasaeronáu-
ticasedebensdeconsumo).
OABAPnasceucomoumalinguagemcomcomandoextensos.Parafazer
umasimplesleituradeumdadoemumatabelainterna(umaespéciedearray
dasoutraslinguagens),eranecessáriaumasériedepalavras: READ TABLE
tabela INTO linha WITH KEY <igualdade> INDEX 1.. Extrema-
mentetrabalhoso(ouchato).
Porestemotivo,énaturalmentecomparadaaoCOBOL,quepossuisin-
taxesemelhante. Alinguagemrecebeumuitasatualizaçõesdesdeasuacri-
ação,aopontoqueomesmocomandopodeserescritodeformasimilara
linguagensmodernas–tabela[ 1 ] –,desdequeosistemadoclientees-
tejaatualizadocomosúltimos patches.
Apesardasatualizaçõesconstantes,aindaépossívelutilizaromesmobom
e“velho”ABAPdosanos90nosdiasatuais,porcontadaretrocompatibili-
dademantidapelosistema.Vamosexplorarmuitocomoessaretrocompati-
bilidadeafetamosABAPersepráticasdehojeemdia,nocapítulo 6.
OR/3foiosistemaERPquefezcomaSAPiniciasseumapenetraç ãode
mercadotremenda,quesesustentaatéosdiasatuais. OABAPéresponsá-
velporgrandepartedessapopularidade,porserumalinguagemfácildeser
aprendidaemuitoprodutiva.
Um relatório de materiais com diversas funcionalidades (ordenação,
layoutsdiferentes,filtros,sele çãodelinhas/colunas,entreoutras)podeser
criadoporqualquerABAPermedianoemminutos,sejahojeounoiníciodos
anos90. Tambémnãoénecessárioentenderdeparticularidadesdobanco,
poisoABAPabstraicompletamenteosacessospormeiodoOpenSQL,um
conjuntodecomandosABAPqueabstraiasoperações,funcionandoemqual-
19

## Página 34

2.1. OsprimórdiosdoABAP CasadoCódigo
querbancodedadossuportadopelaSAP(praticamentetodososbancosusa-
dosporgrandesempresassãosuportados).
Fig.2.1: Comosdadosmontados,umrelatóriocomoesseficaprontoem
poucosminutos
AlémdoABAP,umasériedecomplementoseoutrosprodutostambém
foramgeradospelaSAP,desdeacriaç ãodoR/3,quecompõeoecossistema
SAP.Sãoosmaisdiversosaplicativos:algunsfocadosnaintegraç ãodesiste-
mas(PI),outroscomfoconomundomobile(SMP)eatémesmoERPsme-
noresparapequenasemédiasempresas(SAPBusinessOne).
HátambémumpacotedeprodutoscriadosemcimadochamadoSAP
WebApplicationServer(WebAS)eumaplataformacriadaprimariamente
emABAP,queservedeber çoparadiversosprodutosdaSAP(CRM,SCM,o
próprioERPetc.).
Muitassiglasenomesconfusos,nãoémesmo?Onúmerodeprodutose
soluçõesgeradosdesdeaascensãodoR/3culminamemumcenárioextrema-
20

## Página 35

CasadoCódigo Capítulo2. ArelevânciadoABAPparaomercadodeTI
mentecomplexo,tantoque,àsvezes,nemmesmooclientesabeaquiloque
contratou.
Jávialgunspagaremhorasdeconsultoriaparaentenderoquefazempro-
dutosadicionaisembutidosemlicen çasqueelesmesmospossuem.Omundo
corporativopodesertãoconfusoqueoclientepodeacabarpagandoumali-
cençaparaalgoqueelenãofazamínimaideiaseéútilparaseunegócio.
Pareceloucura,jáqueoscontratosenvolvemmontantesaltos,maséumasi-
tuaçãocomum. Portanto,sevocêficouumpoucoperdido,fiquetranquilo
quevocênãoestásozinho(epelomenosvocênãoperdeumilhõescomisso).
AvaliandooimpériocriadopelaSAPaolongodosanos,ficaclaroque
oABAP–comolinguagem–eaSAP–comoprovedoradesoftwares–são
extremamenterelevantesparaomercadodeTI.Maséimportantenotarque
éummercadofocado somenteemempresas,enãoaousuáriofinal.
Issoimplicaemdiversasdiferen çascommercadosmaisabertos,comoo
mercadoweb,degamesoumobile,sendoaprincipaldelasessacaracterística
deserummercadopoucoacessível,anãoserquevocêtenhaenvolvimento
diretocomasempresasqueutilizamosprodutosSAP.
2.2 SemSAP,sem ABAP
AgrandequestãoéquesemumsistemaSAP,simplesmentenãoexistepro-
gramaçãoABAP.Issonãoéalgoruimouumdeméritodalinguagem,jáque
elafoicriadaexatamenteparaisso.Entretanto,teraconsciênciadequetodo
oportfólioSAPéorientadoparaempresaséalgocrucialparaentenderos
motivosquefazemomercadosercomoeleé.
Porumlado,empresasegrandescorporaçõesestãodispostasainvestiral-
tasquantidadesdedinheiroparaotimizarseusprocessos.Obviamenteestou
sendobemsimplistanessafrase,jáqueempresas semprevãofazeropossível
paraenxugarseusgastos,masomercadoSAPgerabastantedinheiroeuma
parterazoávelchegaatéosprofissionaisdomeio.
Outrospontospositivosenvolvemotrabalhoemmuitasempresasgigan-
tescas,gerandoumaexperiênciavaliosaparaacarreiradoprofissional,além
deoportunidadedeviagensnacionaiseinternacionaisparatrabalharempro-
jetosdosclientes.
21

## Página 36

2.2. SemSAP,semABAP CasadoCódigo
ABAPerscostumamtransitarporváriosprojetosemdiversasempresas,
gerandoumdinamismoenormenosesquemasdetrabalho,práticasadotadas
epadrõesdedesenvolvimento.Éprecisoumacapacidadedeadaptaç ãorápida
paramanter-seprodutivo.OclienteXpodeterum guidelinecompletamente
engessadodetrabalho,inibindoemmuitoacapacidadedoABAPeragir.Jáo
clienteYpodenãoseimportaremcontrolarabsolutamentenada,deixando
cadadesenvolvedorimplantarosprogramasdojeitoquequiser.
OsrelacionamentosnomundoSAPcostumamserextremamenteimpor-
tantesesãoabaseparacontratosdetrabalhoeoportunidades.Dadasasdifi-
culdadesdeentradaquejáabordamos,énaturalqueonúmerodeprofissio-
naissejarelativamentepequeno.Nessecenário,ficafácilconhecerumaquan-
tidadeconsideráveldepessoasquepodemlheajudarquandopreciso,nãosó
comABAP,mastambémoutrasáreasrelacionadasaoSAPERP(negóciose
infraestrutura).
Sóqueessasempresasquegastamriosdedinheironacustomizaç ãode
seussistemascontêmumaurgênciarecorrenteemseusrequerimentos,ge-
randoumacargadetrabalhomuitograndeeumaenormeofertadeempregos
(quenemsempresãopreenchidas).Essaurgênciatambémfazcomqueacon-
corrênciaentreconsultoriasparaganharumdeterminadocontratosejabem
acirrada,emprocessosextremamentelentoseburocráticos,comoveremos
nocapítulo4.
Essaformadefazerascoisascorrendotambémprejudicacompletamente
aformaçãodosprofissionais:setudoéparaontem,nãohátempoparaapren-
derdireto,somentetempoparaentregar.ComooABAPabstraiesimplifica
diversosproblemas(acessoaoBD,telasparasele ção,relatórios),amaiorparte
dotempocostumasergastatentandoimplantarregrasdenegóciosmuito
complexasefazendosistemaedadostrabalharemdaformaqueoclientepe-
diu.Éprecisomuitocuidadoparaessecomplexidadefuncionalnãofazercom
queas skillsdeprogramaçãofiquemdelado,gerando“tradutoresderegrasde
negócio”,enãoprogramadores.
Encontrarprogramascommaisde10anosemambientesprodutivosque
sãocruciaisparaofuncionamentodaempresaéalgocompletamentenormal
paraumABAPer.AlgumasáreasexternasaoSAPacabamdeparando-secom
códigosmal-estruturadosecomplexosdeseremassimilados,sementender
22

## Página 37

CasadoCódigo Capítulo2. ArelevânciadoABAPparaomercadodeTI
completamenteessecontextodosoftwarecorporativocriadoemcimadeum
sistemacommaisde30anosnascostas.Issocriaumadistânciaaindamaior
porpartedealgunsprogramadores,poracharemque todoequalquerdesen-
volvimentoABAPétratadodessaforma,oquenãoéreal.
2.3 Problemas ou oportunidades?
Softwarecorporativodificilmenteserátratadodamesmamaneiraquesoft-
wareparaasgrandesmassas. Sãomundoscompletamentediferentes,cada
umcomassuasparticularidades.Todosospontosqueciteipodemserinter-
pretadoscomoproblemaspelaspessoas,jáqueéumcenárioquepodenão
parecermuitoatrativo.
Masoquevocêachariadecriarumsistemaanalíticoquecalculaeotimiza
asrotaslogísticasdeumamultinacional? Oucriaraautomatizaç ãodepro-
cessosentresistemasdistintosparamovimentarmaisde5miltransaçõespor
minuto?Oumesmocriarrelatóriosextremamentecomplexosdetomadade
decisão,quepodemmovimentardezenasdemilhõesderegistros(edinhei-
ros)?Criarmonitoresunificadosparaautomatizaracriaç ãodosdocumentos
envolvidos,empraticamentequalquernegóciodaempresa?
Todosessescenáriosenvolvemdesenvolvimentoscomplexosqueneces-
sitamdeum expertisetécnicoalto.NãoésóconhecimentoABAP,envolveco-
nhecero landscapedocliente,comointegrarosdados,comounirossistemas,
comopadronizarcomunicaçõesoucomootimizartecnicamenteprogramas
queprocessamquantidadesgigantescasdedados.
OmundoSAPcontémmuitasoportunidadesdeprojetosinteressantee
complexosparaaquelesquepossuemosconhecimentosadequados,umnú-
merodepessoasquevocêjádeveterdeduzidonãosertãoenorme,dadoo
cenárioqueexpliqueiatéagora.Sãooportunidadesreaisderesoluçãodepro-
blemascomplexos,quetrazemumagrandesatisfaç ãoquandoconcluídos.
Naminhavisão,apesardeserummundofechadoeexistiremdiversas
barreirasdeentrada,umavezdentrodomundoSAP,todoproblemasetrans-
formaemumagrandeoportunidade.Muitasconsultoriaseatémesmoclien-
tessubestimamdiariamenteacapacidadequeelestêmemmãos,comtodas
asferramentasdisponibilizadaspelaSAP.Seusadascommaestria,épossível
23

## Página 38

2.4. SAPéomundoperfeito CasadoCódigo
transitarentreasmaisdiversastecnologias(incluindoprodutos/linguagens
não-SAP)ecriaraplicaçõesmuitorobustas.
Éumasituaçãomuitoparecidacomadasempresasmaisnovas(aquelas
startupscomescritóriosdefrenteparaomar),ondequasetudoépossível,
bastaalguémtomarainiciativaedecidirimplantarmudan ças. Nãoqueo
caminhosejafácil,afinal,empresasgrandespodemsetornarburacosnegros
burocráticos.Mas,sefossefácil,tambémnãoteriamuitagraça.
Essasoportunidadesficamaindamaisevidentesseconsiderarmostoda
amovimentaçãodaSAPnosúltimosanospararepensarodesenvolvimento
desoftwarenaempresa,adotandopráticascomoUIsutilizandobibliotecas
Javascript(SAPUI5),eserviçosparapadronizarefacilitaroconsumodasin-
formações(ODATAviaGatewayouHANA).TantoqueexisteatéumGitHub
oficialdaempresa,disponívelem https://github.com/sap.Falaremosdetudo
issoemaisumpouconocapítulo 8.
2.4 SAP é o mundo perfeito
Masnemdelonge. Paracome çar,pensenaquantidadedefuncionáriosda
empresaenvolvidosnautilizaçãodeumsoftware,comooSAPERP.Umaárea
deTIdeumamultinacionalpodetertimesmuitograndes,normalmentees-
palhadosporváriaspartesdoglobo.Essaéamaiordificuldadedeencontrar
inovadoreseentusiastasnessemeio:atingirumconsensoentreprofissionais
efinançasnaempresa,paraconseguirtrabalharcompráticasatuais,sistemas
atualizadoseequipescapacitadas.
UmABAPerverádetudo,desdeaquelaempresaquenãotemdinheiro
parainvestirematualizaçõesetrabalhacomprocessosjurássicosatéaquela
outraqueusaeabusadetodasasatualizações patches,correçõeseferramentas
queumalicen çaSAPdisponibiliza.
Pormaistentadorquesejatrabalharsomentenasempresasinovadoras,é
deextremaimportânciaterconhecimentodesistemasouprocessosantigos,
paraquevocêpossaentenderoporquêelesnãoeramamelhorsolução.Con-
tantoquevocênãoassumaqueessesformatosemecânicasfalhasdetrabalho
sejamaregra,épossívelfazerbomproveitodasexperiências.
OABAPérelevante?Sim,eaindavaisemanternomercadoTIpormuitos
24

## Página 39

CasadoCódigo Capítulo2. ArelevânciadoABAPparaomercadodeTI
anos. Afinal,amesmaburocraciaexistenteparatrabalharcomumsistema
SAPERPtambémestápresenteemumadecisãodetroca,ouinutilizaç ãode
umsistematãogigantesco.
Seelesetornaráumalinguagemesquecidaemumsistema“encostado”,
oucontinuarásendorelevanteparaoecossistemaalongoprazo,éimpossível
prever,poisdependediretamentedaaceitaçãodosclientesparaasnovastec-
nologiaslançadaspelaSAP.Porsetratardeumaempresadesseporteecom
essapenetraçãodemercado,éimprovávelqueelesumatãocedo.
Claroquenadaduraparasempre,mas,mesmoqueoABAPváparaovi-
nagre,aindaexistirãodiversasoportunidadesnomundoSAP,tantoparade-
senvolvedorescomoparaorestodosprofissionaisenvolvidos.Bastamanter-
seatualizado,enãosubestimarasinergiaecapacidadedeintegraç ãodoABAP
eferramentasSAPcomtodoequalqueroutrotipodetecnologia. Ser“so-
mente”umABAPernãoéosuficiente.
25

## Página 41

Capítulo3
CertificaçõesABAP
Seasuainten çãoéadecome çarcomoABAPerevocênãotemnenhumtipo
deenvolvimentoinicialemempresas(estágio,traineeetc.),hágrandeschan-
cesdevocêterchegadoaalgumainformaçãorelacionadaàscertificaçõesSAP.
Mesmoaquelesquejáestãonaáreadevemterseperguntado,emalgummo-
mento,seacertificaçãopodeserummeiointeressantedealavancarocurrí-
culo.
Osvaloresnãosãobaratos,principalmenteporvocêserobrigadoafazer
ocursooficialparapoderprestaraprova(issoéumabarreiraexistenteno
Brasil,masnãoéassimemoutrospaíses).Certamente,antesdeinvestirrios
dedinheiro,vocêdevetersequestionado:qualorealvalordacertificaç ãona
práticadomercado?Essarespostanãoétãosimplesassimdeserrespondida,
apesardeosmilharesde bannersemsitesdevendasdecursostentaremprovar
ocontrário.

## Página 42

3.1. Certificaçãoeasconsultorias CasadoCódigo
Esqueçaomercado:quantovaleumacertificaç ãoparavocê?
Antesdediscutircomoomercadoenxergaascertificações,destacoque
existempessoasqueenxergamacertificaç ãocomoumaformadeobjetivar
seusestudosemdeterminadatecnologia.Nemtodomundoconsegueestudar
porcontaprópriaesemmetas.Algumaspessoasprecisamdeumamotivaç ão
parafocaremseudesenvolvimento.
Paraessaspessoas,nãoimportatantoassimovalorqueomercadodápara
acertificação,importamaisaexperiênciaadquiridaduranteoprocessode
estudosparaaprovafinal.Normalmente,elasnãovãoestudarsomenteoque
énecessárioparapassarnaprova–naverdade,seraprovadoéconsequência
doseuinteressearespeitodotema.
Sevocêtemessaformadepensar,nãoparepararefletirsobreovalorque
issoteráparaomercado.Váemfrenteecoloqueseufoconascertificações.
Tenhocertezadequeoprocessotodoserábenéficoparavocê.
Paratodososoutroscasos...
3.1 Certificação e as consultorias
DesdeoiníciodomeutrabalhocomSAPatéapublicaç ãodestelivro(9
anos+),nenhumlíder,gerente,sócioouclientenuncamediuomeuconhe-
cimentocombaseemumacertificaç ão. Mudeialgumasvezesdeempresa,
easavaliaçõessempresebasearamnaminhaexperiênciaeconhecimentos
técnicosquedemonstreiduranteosprocessosseletivos.
Umleitoratentopodepensar:“Ué,mascomovocêvaisaberseacerti-
ficaçãorealmentepesou,sevocênãotemcertezaabsolutadosmotivosque
fizeramvocênãosercontratadoemalgumprocessoseletivo?”.
Defato,nãotenhocomosaberosmotivosquefizeramcomqueeunão
passasseemalgumasentrevistas.Entretanto,épossívelterumaideiaaocon-
versarcomrecrutadores,alémdebalizarpelasminhasprópriasexperiências
comoavaliadorduranteorecrutamento.
Acertificaçãodemonstraqueoprofissionaldedicoupartedoseutempo
aosestudoseconseguiupassaremumaprova.Oproblemaéqueaprovaestá
longederefletirasnecessidadesdodiaadia,portanto,nãodáparautilizaro
28

## Página 44

3.2. Oscavaleirosdacertificação:Certification5 CasadoCódigo
eles dão diversas sugestões sobre como a reestruturação do exame de certifica-
ção SAP pode trazer benefícios a todos da comunidade: clientes, profissionais 
e até a própria SAP. O grupo também fez uma pesquisa extensa que listou as 
percepções de diversos consultores do mundo todo a respeito de certificações. 
Dennis Howlett, um dos SAP Mentors que criou o artigo original, cita em 
um de seus artigos sobre o tema (http://bit.ly/2bC7Ydi) que um dos motivos 
que levou à criação foi a vontade de que uma certificação SAP tenha
omesmopesoqueumcertificadodeummédico,dentistaouadvogado.Ou
seja,quesejaumamarcagarantidadequalidadeprofissional.
Eleponderaqueopesodacertificaçãoénecessário,porcontadoesquema
dacarreiradosconsultoresenvolvidoscomSAP.Normalmente,esseéum
trabalhoparaavidatoda,nãosendoummercadocomumamassagrandede
profissionaisquetrabalhamalgunsanosnaárea,paradepoismudarempara
outrastecnologias.
Éinteressanteanalisartambémqueaequipedo Certification 5sabia,desde
oinício,queseriamuitodifícilparaaSAPmudartodooseuesquemade
certificaçãoparaalgomelhor,dadaotamanhodaempresaeacomplexidade
dereestruturartodoosistema.
NoPDFdoartigo,vocêpodeaindaverasrespostasqueaprópriadi-
visãodecertificaçõesdaSAPdeuparaascríticaslevantadaspelogrupo. É
interessanteveroposicionamentodaSAPEducationparaalgumasquestões.
Issoajudaaentenderamecânicadoprocesso,enaltecendoadificuldadeem
adequá-loparaoqueentendemoscomosendosatisfatório.
Analisandotodoomaterial,ficaevidentequenãoexisteaverdadeabso-
lutasobreorealpesodeumacertificaçãodomercadoSAP.Hámuitasdúvidas,
partindodetodasasáreas:clientes,consultores,consultoriaseatédedentro
daprópriaSAP(comovistonoscomentáriosdoartigo).
O Certification 5levantouquestõesqueestavam“nagarganta”demuitos
profissionaisdomundoSAP,porém,aomenosnaáreaABAP,poucomudou
desdeamovimentação. Osquestionamentos,dúvidaseconfusõessobreo
valordessepapelaindapersistemesãoconstantementeabordadosnanossa
área,principalmenteentreaquelesqueaindanãotêmumavagadentrodesse
mercado.
30

## Página 45

CasadoCódigo Capítulo3. CertificaçõesABAP
3.3 Certificação e clientesSAP
Apesardaminhaperspectivanadaotimista,acreditoquenemtudoestá“per-
dido”paraascertificaçõesnoformatoatual. Dentrodessecenáriocheiode
incertezas,existeumasituaçãoondeacertificaçãorevela-senecessária:exi-
gênciadocliente.
Algunsprojetosemempresasgigantescasexigemqueaconsultoriaapre-
senteumnúmeroXdeprofissionaiscertificados,paraqueaconsultoriapossa
entraremumprocessodeconcorrência.
Quandotrabalheiemconsultoriasmultinacionais,eracomumchegarem
e-mailsdaáreadoRHdetemposemtempos,tentandocaç arprofissionais
certificados,provavelmenteparasubmeterseuscurrículosparaalgumades-
sasconcorrências. Notequeissonãoqueriadizerqueoprofissionalcertifi-
cadoseriaalocadonoprojeto,casoaconsultoriaganhasse.Oimportanteera
cumprirasexigênciasdocliente,parapoderentrarnoprocessodeconcor-
rênciaesubmeterumapropostadetrabalho.Aimpressãoqueissopassaéda
certificaçãoserumameraformalidadeenadamais.
Eaí,vouounãovou?
Comodisseanteriormente,tudodependedasuamotivaç ão.Nãofaçaa
certificaçãosimplesmente porque sim,ouporquealguémestásugerindoque
issoseráumdiferencialmatador. Vocêcorreoriscodegastarumagrande
quantidadededinheiro,enãoobteroretornoesperado.
Tenhocertezaabsolutadequeprofissionalnenhumgostadegastardi-
nheiroàtoa.Afinal,osvaloresnãosãobaixos.Portanto,avaliebemoquea
certificaçãosignificaparavocê,antesdeentrarnessajogada.Vá,masvácom
cautela!
31

## Página 47

Capítulo4
Osbastidores
Nesteponto,jáficouclaroqueosgrandesempregadoresdomundoSAPsão
asconsultorias. Sãoelasquenegociamosprojetoscomclientes,edecidem
quandoeondeodesenvolvedorvaipôrempráticaaquiloquesabe.
Essadinâmicageraasmaisdiversaspolêmicasediscussões,jáquemuitas
vezesaspráticasdasconsultoriaspodemparecerumtantoquantoabusivas,
levandooprofissionalasentir-seexploradoedescontentecomoseutrabalho.
OqueeunoteiaolongodosanoséquemuitosdosABAPersquere-
clamamdeasconsultoriasseremexploradorassequerentendemobásicode
comoumaconsultoriafunciona.Podeparecersimples,masháumasériede
profissionaisqueprecisaminteragiratéqueoABAPersejaalocadonoprojeto
XouY.
Nestecapítulo,explicareiapartirdasminhasexperiênciasumpoucoda

## Página 48

4.1. Comosurgemasalocações? CasadoCódigo
mecânicadecomoascoisasfuncionam,paralheajudaradecidirseacon-
sultoriaparaaqualvocêtrabalhaestá mesmosendoabusiva.Éclaroquehá
gerentesodiosos,líderescarrascosecomerciaistapados.Mas,àsvezes,tudoo
queprecisamoséentenderocontextoquenoslevouàquelaalocaç ãobizarra.
Afinal,essepovobizarroequetrabalhamalpodeseridentificadofacilmente,
nãoémesmo?
Importante:asexplicaçõesdestecapítuloforamcriadasdopontodevista
dasconsultorias,enãoenvolvemamecânicadetrabalhodosABAPerscon-
tratadoscomofuncionáriosdeumaempresaquecontémprodutosSAP.Nor-
malmente,essesdesenvolvedoressãoescaladosparacargosrelacionadosao
suportediárioeaosproblemasdeprodução,queenvolvemacorre çãodeerros
emelhoriasespecíficasemalgunsprocessos.
Porcontadofatodeasdinâmicasdessestrabalhosseremcompletamente
distintas(dependemuitodaculturaepráticadecadaempresa),elasnãoserão
consideradasnestemomento.Mas,sevocêforumdessesABAPers,nãopule
ocapítulo:hágrandeschancesdevocêconsiderarumempregoemumacon-
sultoria,emumperíodode“dúvidas”dasuacarreira.Sabercomoascoisas
funcionamfacilitaráasuapossíveltransição.
4.1 Como surgem as alocações?
TodomundogostadefalarqueoSAPERPéumprodutoextremamentecaro,
masovalorpagopelalicen çacostumasermuitoinferioràquantidadededi-
nheirogastacomconsultorias.ÉaquelavelhahistóriadequeimplantaroSAP
ERPporsisónãoéobastante.Éprecisotambémcustomizarosistema:ade-
quandoregrasdenegócio,criandorelatórioscomplementares,aumentando
aprodutividadedaequipe,ouatémesmotrocandoacordeumatelapor-
quealgum bam-bam-bamquisassim.Etudoisso,obviamente,custa(muito)
dinheiro.
AnecessidadedeumABAPernascemuitoantesdorecebimentodeuma
especificaçãofuncional,elateminícionamentedocliente.Apartirdomo-
mentoemqueumclientedecidequeeleprecisaajustar/melhorar/criaruma
determinadafuncionalidade,opapeldoABAPerpodetornar-senecessário.
Todotrâmiteenvolvidonesseprocessodaideiaàrealizaç ãoéquedetermi-
34

## Página 49

CasadoCódigo Capítulo4. Osbastidores
narácomoequandoseráaalocaçãododesenvolvedoreoutrosprofissionais
domundoSAP.
Funcionaassim:quandooclienteenfimdecidequeele realmenteprecisa
alterarosistemadealgumaforma(issopodedemoraranos,acredite),elevai
contatardiversasconsultoriasparaqueelasfaç amumor çamentodequanto
ficaráotrabalho.Elasprecisarãoavaliarorequerimentodoclienteedefinir
umasoluçãotécnica.Issogeraráumaestimativadeesfor çoparapoderquan-
tificarovalordasalterações/criações,estassumarizadasemumdocumento
queasconsultoriaschamamde propostas.Sãonelasqueestãolistadosoes-
copodotrabalho,onúmerodeprofissionaisenvolvidos,aestimativadehora
paraosdesenvolvimentoseovalorcobradopelosserviçosprestados.
Muitaspalavras“corporativas”noúltimoparágrafo?Voureescreverpara
ficarmaisclaroparaanossarealidade:oclientequeradicionaralgumadoi-
deiraaosistema.Então,aconsultoriaverificaseelenãoestáviajandoedefine
umasoluçãotécnica,tentandodarumchutecerteirodotempoqueserágasto
nostrabalhos,contandocomfolgasnostemposeprevendoalteraçõesdoes-
copo(ocliente semprepedealgomais, sempre).Issotudoésumarizadoem
umarquivoWord/Excel–quemuitasvezeségrandedemaisparaserenten-
didoporumhumano–,eéentregueaoclienteparaqueeleavalieseasolução,
aestimativadetempoeosvaloresdaconsultoriafazemounãosentido.
Munidodaspropostasdediversasconsultorias,oclientevaidecidircom
qualseguiráemfrente. Apesardeessadecisãopareceralgodeterminístico
(deveganharamelhorproposta,certo?),essafasepodesercompletamente
subjetiva.
Asituaçãoébemparecidacomadequandovocêdecidequecomprarna
padaria do Zé da esquinaémelhordoqueirà padaria de superqualidadeque
ficaa200metrosdesuacasa,sóparaevitarafadiga.Essadecisãocostuma
ficaraindamaisfácilseoZéforseuparente:certamentevocêsóvaicomprar
comele...atéquevocêcomprealgoestragado,oquefarácomquevocêpossa
voltaraconsiderara padaria de superqualidade(ounão,vaisaber).
Éimportantenotarquealgumasconsultoriaspodemfazerosmaisdiver-
sosmalabarismosparaganharumprojetodeumclienteondeháumadisputa
acirrada.Dependendodomalabarismo,osprofissionaisalocadosnoprojeto
podemsofrermuito.Desdedespesasnãopagasatémilharesdehorasextras
35

## Página 50

4.2. Adançadascadeiras CasadoCódigo
paracobrirumerronavenda.
Aliás,essesproblemasnavendageramareclamaçãonúmeroumdospro-
jetosatrasadosoucorridos.Issoénatural,poisseoprojetonascererrado,as
chancesdetodososenvolvidossofreremmuitocomsuaimplantaç ãosãoal-
tíssimas.
Poisbem,essetrâmitetodoqueenvolvegerentes,líderes,sócios,comerci-
aiseespecialistaspodedemorarumtempãoparaterminar.Tudodependedo
escopodotrabalho:quantomaioroprojeto,maisdemoradoficaráoprocesso
dacriaçãodaspropostas.
Aquelasreuniõesintermináveiscomosespecialistasdasconsultoriassão
muitocomunsnestafase,jáqueoclientepodenãoterno çãodaquantidade
dehorasquepodemsergastasparaajustaralgoqueelepensaqueésimples.
Muitasalivacostumasergastaatéalguémconseguirexplicar,deformacon-
sistente,quealgoquedeveriacustar10,naverdadecusta1.000. Háainda
diversasrodadasdeperguntaserepostas,tudoparaqueaconsultoriapossa
chegaràmelhorrelaçãodesoluçãoepre ço.
Apesardademoraedacomplexidadedotrabalho,horaououtraopro-
jetopodeserfechadocomaconsultoriaemquevocêtrabalha(sejamláquais
foremascondiçõesacordadas).Eénessahoraqueéprecisodecidiralgoex-
tremamentecrucial:quemdaequipevaitrabalharnoprojeto?
4.2 A dança das cadeiras
“ Ah, essa é outra decisão fácil, não é mesmo? Basta escolher quem estiver dis-
ponível e mandar para o projeto!
Quemderaessadecisãofosseassimtãosimples.
Odinheirodaconsultoriavemdaalocaç ãodosseusprofissionais,por-
tanto,consultorianenhumateminteresseemdeixarpessoasdesalocadas.A
vendaconstantedosseusserviçoséessencialparamanterseusprofissionais
faturandoemclientes.Semisso,consultorianenhumasobrevive.
Omaiorproblemanahoradedecidirquemvaiparaoprojetoéquenem
sempreasdatascoincidem.Nãodáparachegarparaoclienteefalar:“sabe
aqueleprojetoquevairesolvertodososseusproblemasequevocêquerfechar
conosco?Então,vamosdeixarparaoanoquevem,poisnãotenhoninguém
36

## Página 51

CasadoCódigo Capítulo4. Osbastidores
disponívelparaatendê-lo”.
Dizeralgoassimébasicamentedarumatestadoparaoclientedizendo
“fechecomoutraempresa”.Emsituaçõesespecíficas(projetosruinsoupara
evitarasuperalocaçãodosconsultores),recusarumprojetopodeserasaída.
Porém,todaconsultoriateminteresseemfecharprojetosinteressantesde
grandesempresas,tendoounãoosprofissionaispararealizarosprojetos.
Ué,masperaí!Comoassimasconsultoriasfechamprojetossemterpes-
soasparatrabalharneles?
Éissomesmo:comoasdatasentreosprojetosqueestãorolandonacon-
sultoriapodemnãocoincidircomasdatasdosnovos,aconsultoriapodefe-
charprojetosmesmosemsaberquemvaitrabalharneles. Nomelhordos
mundos,elaconsegueremanejarseusprofissionaisparaatenderàsnovasde-
mandas,masmuitasvezeselaprecisarecorreraomercadoecontratarnovos
funcionários.
Essasituação,aliás,éaquemaisgeraaquelaavalanchediáriadeofertas
devagasquevemostodososdiasemgruposdee-mail,Facebook,LinkedIne
afins.Aconsultoriapode,inclusive,come çaraabrirasvagassemnemmesmo
saberseoacordocomoclienteserárealmentefechado,comoummecanismo
deprecauçãocasoganheoprojeto.Issonãoéumapráticaexclusivadomundo
SAP;qualqueráreadeTIrelacionadaaserviçosacabacaindoemsituações
similares.
Supondoqueaconsultoriatenhaaspessoasnecessáriasparaatendera
demanda,ficaamesmadúvidaanterior: quemdaequipevaitrabalharno
projeto?Emtodasasconsultoriasemquetrabalhei,osmelhoresprofissionais
tinhampreferênciaparaosmelhoresprojetos.
Seforumclienteestratégico–ouseja,quetemmuitodinheiroparagastar
–,podeatéserqueumótimoABAPersejasubstituídonoprojetoondeestá,
paraquepossatrabalharnonovoprojetoimportante.Éexatamenteporisso
queéextremamenteessencialmanter-seatualizado,estudardeformacontí-
nuaeprocurarrealizarsempreumótimotrabalho. Bonsgestoresprecisam
depessoascompetentesemquempossamconfiar,eessapessoasterãoprio-
ridadeemescolhascomoesta.
Particularmente,demoreiumpoucoparaentenderessadinâmica,pois
umABAPernoiníciodacarreiratempouquíssimocontatocomessemundo
37

## Página 52

4.3. Mecânicadetrabalho CasadoCódigo
daspropostasecontratosfechadosdeprojetos. Masdepoisdeentendê-la,
percebiquemuitasdaspessoasquepegamospioresprojetosealocaçõesaca-
bamsendopessoasquenãosãoescolhidascomprioridadepelaconsultoria.
Umaanalogiaboaéofutebol:emumjogodedecisão,quemjoganotime
titular? Equementraemumjogoquetempouquíssimaimportância,mas
precisasercumprido?Seojogador mega master blasterestálesionado,quem
vaiparaoseulugar? Seráqueémaisvantajosocontratarumnovojogador
emvezdepegaralguémdobancodereservas?
Pareepense:emumasituaçãosimilar,sevocêfosseogestor,quemvocê
escolheria?
4.3 Mecânica de trabalho
ApósquiloselitrosdearquivosdoWordeExcel,inúmerose-mailscom384
pessoasemcópiaeumainfinidadede“reuniõesdealinhamento”,suacon-
sultoriaenfimganhouoprojetoedecidiuquevocêseráoalocadodavez.E
agora?
Noiníciodosprojetos,vocêprovavelmentevaireceberumasériededocu-
mentosquedizemquaispadrõesvocêdeveseguiraoprogramarparaaquele
cliente. Sãopadrõesdenomenclatura,diretrizesdeperformance,templates
deespecificaçõestécnicaseroteirosparatestesunitários.Éclaroqueissosó
aconteceráemprojetosorganizados.Namaioriadeles,évocêqueprecisará
perguntarporestesdocumentos. Dicadeamigo:faç aissologoquechegar,
paranãocorreroriscodefazerascoisas“doseujeito”,eterquealterartudo
depoisdepronto(comojáaconteceucomigo,maisdeumavez).
Agoraquevocêjáestáapardetodasasnormasediretrizes,restauma
corridaconstantecontraotempo.Duranteaproposta,algumasestimativas
foramestipuladas,eelasdiziamqueoprogramaABAPXiriademorar,mais
oumenos,otempoYparaserrealizado.
“Masissoéumabsurdo!”,dizoABAPerrevoltado.Namaioriadasvezes,
aspessoasqueseenvolvemcompropostassãoespecialistasABAPers,por-
tanto,ostemposnãodevemestartotalmenteforadarealidade. Se,mesmo
assim,alguémchegarcomprazoscompletamenteapertados,lembre-seda-
quelesmalabarismosdequefaleiháalgunsparágrafosatrás. Nemsempre
38

## Página 53

CasadoCódigo Capítulo4. Osbastidores
osespecialistasABAPersestãopresentesnahoradedefinirqualdesenvolvi-
mentoserápenalizado“emproldavendadoprojeto”.
Consultoriasgrandesdispõemdeumafaseemqueaestimativafeita,em
tempodeproposta,deveserconfirmada,jáqueénahoradoprojetoquea
empresacontratantevailiberartodososdetalhesnecessáriosdeumadeter-
minadademanda.Nemsempreissoexisteemconsultoriasmenores;todosos
prazosjáforampredeterminadosepronto.OABAPerpodeatétentardiscu-
tircomogerenteparaverseumademandaqueprecisariadodobrodetempo
paraserconcluídapodeserremanejada,masissonemsempreépossível.
Oclientepode,inclusive,inventarnovasfuncionalidades“donada”e,de-
pendendodocaso,aconsultoriaprecisaarcarcomoprejuízo.Arealidadeé
bemmaiscrueldoqueaquiloqueéensinadopelosprofessoresdeengenharia
desoftware.
Durantesuacarreiracomodesenvolvedor, vocêverádiversosartigos,
podcastselivros(esteinclusive)dizendoparanãoirpelocaminhomaisfácil
nahoradeprogramar.Emumasituaç ãodeprazosapertados,comofazero
melhordesenvolvimento?Acreditequandoeulhedigoqueé sempremelhor
fazerascoisasdireito,pormaiscurtoquesejaotempo.
Vocêpodeatégastarumtempomaiordesenvolvendo,masonúmerode
problemasquevocêvaievitarnofuturovaleráapena. Bastavocêconven-
ceroseugerentedequeissofazsentido. Seelenãoacreditar,usoobome
velho“euavisei”quandodeterminadoprogramaruim,geradopeloprojeto,
atrapalharcompletamenteotesteintegrado.Um“euavisei”bemempregado
semprefunciona.Sótomecuidadocomasreações!
Masacalme-se,nemtudoétãocaótico. Muitosprojetoscontêmprazos
muitomaioresdoqueonecessário. Issoéfrutodafamosa“gordura”,um
tempoadicionalqueaconsultoriaadicionaàspropostas,prevendoatrasos
oualteraçõesdeescopopelapartedocliente.Sevocêjápensouem“porque
determinadoABAPerficaodiainteirosemfazernada”,essetipodedemanda
éumaprovávelresposta.
Oprazoestipuladoparaasdemandasnãodeveserutilizadosomentepara
acriaçãodocódigo,vocêtambémprecisatestarcorretamenteasuaaplicação
eentregarquaisquerquesejamosdocumentosqueoprojetopedir.Aespe-
cificaçãotécnicacostumaserodocumentomaisignoradopelosABAPers–e
39

## Página 54

4.3. Mecânicadetrabalho CasadoCódigo
falaremosmaisdelanospróximoscapítulos.
Ostestesdependemmuitodoscenáriosgeradospelotimefuncionale
pelocliente,maselesprecisamserfeitos. Nãohesiteemencherosacode
ambosafimdequeelescriemoscenáriosnecessáriosparaquevocêpossa
validar,seasuaaplicaçãorealmentefazaquiloquedeveriafazer.
Nofim,quasetudogiraemtornodotemponosprojetos.Prepare-separa
lidarcomaperguntaqueeumaisodeionestacarreira:“eaí,quantotempo
faltaparavocêterminaressademanda?”.ApostoqueoSAPERPfaráopos-
síveleimaginávelparaqueasuaresposta(“sómaisumdia”)sejacompleta-
mentefalha. Seenvolver BAPIs,alteraçõesemprogramasantigos,amplia-
çõesdeprocessosnativosdosistemaou CALL TRANSANCTIONs,achance
desuarespostaserfuradaéaindamaior.
Assimcomoacontecenavenda,pormaiorquesejamosproblemasque
umprojetopossagerar,horaououtraeleentraráemproduç ão,pormeioda
faseconhecidacomo Go Live. Eugostodedizerqueénessemomentoque
aquelesquenãotrabalharamdireitopagamosseuspecados.
Osdesenvolvimentosvãotodosparaaprodução,eaquelesquenãoforam
feitos(outestados)corretamentecorremgrandesriscosdegeraremperdas
monetáriasreaisparaaempresacontratante. Nãosãorarasaslendasurba-
nasdeprogramasABAPqueatrapalhavamdeterminadoprocessoegeraram
perdasimensasparalinhasdeproduçãodosclientes.
Afamosafrase“oscaminhõesestãoparados”surgiudeprogramasrela-
cionadosàliberaçãodocaminhão(NotaFiscaletc.),quesimplesmentenão
funcionavamemprodução.Tenhoamigosquejáficaramcomaorelhaver-
melhaporcontadecaminhoneirosqueesperavamumdiainteironaportada
empresa,atéquealguémarrumasse“osistema”.
É,amigoABAPer,nãosubestimeanossacapacidadedeatrapalharavida
dosoutrosatravésdecódigosfalhos.Preocupe-seementregarumtrabalho
corretoevocênãosofrerádoresdecabe ça.Assim,mesmoquealgoquevocê
fezdêerrado,seusparessaberãoquenãofoiporfaltadeempenhoefarãoo
possívelparaajudá-loacorrigirasfalhas.
40

## Página 55

CasadoCódigo Capítulo4. Osbastidores
4.4 E então vem a próxima alocação
O Go Livefoiumsucesso,todososprogramasestãoemproduç ão,osistema
aparentementenãotemmaisfalhaseasuaalocaç ãoestápertodofim.Énesse
momentoqueocicloserepete.
Devoltaàconsultoria,gestoresvãoavaliarquaisosprojetosdisponíveis,
parapoderremanejarsuaequipe.Háalgumprojetonovoprecisandodepes-
soas?Háalgumprojetocorrentequeprecisadeajuda?Sendovocêparteda
equipe,seufuturodependerádiretamentedasdecisõesdogestoressobreonde
seriaomelhorlugarparaoalocar.
Issopodeacontecerdiretamente,porexemplo: vocêsainasexta-feira
deumprojetoparacome çarnasegunda-feiraemoutrocompletamentedi-
ferente,oupodedemoraralgumtempoparaacontecer,emummomentoem
quevocêseencontrará“desalocado”.
Adesalocaçãoévistadeformaruimpelamaioriadaspessoasdomundo
SAP.Mascomojáexpliquei,nemsempreasdatasdosprojetoscoincidem,o
quelevaaconsultoriaaprecisardeixarumprofissionalparadoporumtempo,
atéqueumnovoprojetoinicie.Procuresaberclaramenteseasuadesaloca-
çãoédecorrentedeumaproblemadedatas,ouporqueoseugestorpreferiu
mandarumaoutrapessoasemseulugar.Ésemprebomsaberomotivoreal
dascoisas,porpiorqueeleseja.
Independentedomotivo,sevocêencontra-sedesalocado,terádeachar
umarespostaparaaderradeirapergunta:oquefazer?Redessociais,jogose
assuntospessoaisvãofazerdetudoparatomaroseutempo.Resista!
Conversecomseugestorevejaseeleprecisadeajuda.Seelenãoprecisar,
aproveiteessetempolivreparaestudarourevisar“aquela”coisaquegerou
problemasnoúltimoprojeto. Useotempocomalgoútiledemonstreinte-
resse.Ficarparadoesperandoalguémdecidiroseufuturoéprovavelmentea
piorformadeaproveitaressetempo.
“Ah,masumdescansofazbem...”.Certavez,reclameidecansaçoeférias
paraafaxineiradoescritórioondetrabalho,dizendoqueeuestavahámais
de2anossemférias.Elarespondeuparamimcomenormesimplicidade:“Eu
seicomoé,meufilho,estouhá8anossemférias”.Elaacordatododia04:30,
chegaemcasaàs22:00eéumadaspessoasmaisalegresquejáconheci.
41

## Página 56

4.4. Eentãovemapróximaalocação CasadoCódigo
Éclaroqueeuacreditoquetirarfériasanuaiséalgomuitobom(eeu
recomendofortementequevocêfaçaisso),masoserhumanorealmentegosta
dereclamardebarrigacheia.Temumtempolivrenoprojeto?Tenteutilizar
paraalgoútiledemonstreissoparaseuspares.Apostoquevocêcolherábons
frutos.
Voltandoaoperíododetransiçãoentreprojetos,émuitoimportanteque
vocêconstantementeentendaasuaposiçãodentrodaconsultoria.Umacoisa
queéfrequentementeignoradaéomomentodofeedback.
Duranteumprojeto,vocêcertamentetrabalhoucommuitaspessoasdos
maisdiferentescargosefun ções,tudoparaquevocêconseguisseentregarseus
programasABAPcomqualidade. Seráqueelesgostaramdoseutrabalho?
Seráqueelesteriamalgumaobservaçãoparafazer? Pedirfeedbackparaos
outroséumaformaótimadetercertezasevocêestáounãonolugaronde
gostariadeestar.
Osfeedbacksmaisimportantessãoosdosseusgestoresedosseusamigos
ABAPersmaisexperientesquejátrabalharamcomvocê.Elespodemrevelar
problemasqueestejamfazendocomqueoutrosavaliemmaloseutrabalho,
oupontosfortesquevocêpodeusarparaalavancarsuacarreira.
Comoadinâmicadasalocaçõespodefazercomquevocêsaiadeumpro-
jetoevádiretamenteparaooutro,semtempopararespirar,éimportante
pedirumfeedback antesdofimdoprojeto.Nãodeixeparadepois.
Quandovocêéalocadonopróximoprojeto,ocicloserepete.Elevaise
repetirmuitasemuitasvezes,atéquevocêvireumgestor,umlíderdentro
dosprojetos,umespecialista(quefatalmenteprecisaráajudarempropostas),
ouvirealgumaoutracoisaqueeunãopossoimaginar,decidaqueessavida
malucanãoéparavocêoucontinuesendojogadodeprojetoemprojetocomo
umtapa-buracodealocaçõesruinsdeconsultorias.Aescolhaésempresua.
42

## Página 57

Capítulo5
Carreira,motivação,universoe
tudomais
MudançasnacarreiraABAPerpodemdemorarparaacontecer.Vocêcodifica,
codificaecodifica,muitasvezessemumaperspectivaclaradeondechegará,
alémdatríadejúnior-pleno-sênior. Parapiorar,processosburocráticosdo
diaadiadasempresas,quecostumamseraindamaiscomplexosdoqueos
exploradosnocapítulo 4,contribuemmuitoparadesmotivarosdesenvolve-
dores.
Nessecenáriopseudoapocalíptico,minhamaiorrecomendaçãoé: não en-
tre em pânico.AscarreirasmeteóricasdomundoSAPcostumamatropelara
noçãodemuitosconceitos,envolvimentocomoutrosdesenvolvedoreseaté
mesmoumano çãodequetudosempreestáruim.Éprecisotercautela.
Ostextosaseguirsãoreflexõessobretemasqueimpactamasuacarreira

## Página 58

5.1. SeráquetodoABAPerémesmoumconsultor? CasadoCódigo
easuamotivação,paratrilharocaminhodoABAPer.Deconceitosbásicosà
vendadecocosnapraia,vamosrefletirseéaindústriaquerealmentenãodá
brechasparaodesenvolvimentodosABAPers,ouseétudoumaquestãode
pontosdevista.
5.1 Será que todo ABAPer é mesmo um consul-
tor?
QuandoingresseinomundoSAP,semprecontavaaosmeusfamiliaresqueeu
trabalhavacomoprogramadorABAP.Porém,comopassardotempo,percebi
quepraticamenteninguémdomercado(clientes,recrutadores,usuáriosetc.)
utilizaotermoprogramador:oprofissionalABAPéchamadode consultor
ABAP.
Algumavezvocêjáparouparapensarnoqueháportrásdessadiferen ça?
Primeiramente,vamosanalisarasdefiniçõesdeambosostermos,direta-
mentedoDicionárioAuréliodaLínguaPortuguesa(versãoonline):
•Consultor:
Consultor é o profissional que, por seu saber, sua experiência, é procu-
rado para dar ou fornecer consultas técnicas ou pareceres, a respeito de
assuntos ou matéria dentro de sua especialidade.
•Programador:
Programador é o profissional especialista encarregado da preparação de
um programa imposto a um computador.
Ouseja, consultoréaquelecaraqueconsegueanalisarasoluç ãointeira
paradaramelhoralternativapossível,pararesolverumdeterminadopro-
blema;programadorépartedaquelaparcelamínimadapopulaçãomundial
quesabeescreverprogramascominstruçõescapazesdeseremexecutadaspor
computadores,devidamentedocumentadosetestados.
Sevocêpensarumpouco,éfácilchegaràconclusãodequetodopro-
gramadorexperienteétambémumótimoconsultor,mesmonãousandotal
título.
44

## Página 59

CasadoCódigo Capítulo5. Carreira,motivação,universoetudomais
A definição de que ABAPers são consultores e que profissionais
Java/Ruby/PHPsãoprogramadoreséumamerapráticademercado,definida
parajustificarasaltastaxascobradasemmeadosdosanos90,quandooSAP
ERPcomeçouasepopularizar.Porserumsistemaexclusivoparaomundo
corporativo,um meroprogramadornãoerasuficienteparaimplantá-lo,era
precisoumconsultor.
NomundoSAP,nãoexisteumsóprofissionalqueentendeasnecessidades
dosusuários,desenhaosprocessos,programa,testaeimplantaemproduç ão.
Essepapelécompartilhadoentreosfuncionais,quefocamemimplantarre-
grasdenegócioespecíficasdaempresanasregrasjáexistentesnoERP;eos
ABAPers,quesupostamentedeveriamterbonsconhecimentossobreasne-
cessidadesdosusuáriosedoprocesso,parapodertransformá-losemprogra-
mas.
AfiguraaseguirdemonstraaestruturadeumprojetoSAPclássico,di-
fundidaepraticadaportodoomercado:
Fig.5.1:EstruturaclássicadeumprojetoSAP
45

## Página 60

5.1. SeráquetodoABAPerémesmoumconsultor? CasadoCódigo
Nessaestruturadeprojetos,quantasvezesoconsultorABAPerajudoua
definirasoluçãodoprojetocomoumtodo(enãosomenteadosseuspro-
gramas)?Quantasvezesfoienvolvidoemum business blueprint(fasedame-
todologiaASAP–AcceleratedSAP–emqueécriadoodetalhamentodos
processos,paraqueelesviremespecificaçõesfuncionais)? Conseguiriaele
responder,empoucaspalavras,qualopropósitodoseuprojetoequaisim-
pactoseleteránodiaadiadaempresa?
Emmaisde9anostrabalhandocomABAPers,poucasvezeseuposso
dizerqueosvirealmenteenvolvidosnadefiniç ãodassoluçõesdosprojetos.
Essasituaçãoéumpoucoirônica:osconsultoresdizemquetrabalharcom
ABAPémaisdoquefazersóapartetécnica,porémapostoqueforampoucas
asvezesemqueelesrealmentetiveramvozativanasdefiniçõesdecomoum
projetofoiimplantado.
Todosacabamcriandoseusprogramasdeacordocomoquefoipedido
pelofuncional,semsaberexatamentedoquesetrataequalaimportância
daqueledesenvolvimentonoprojetocomoumtodo.
Aimpressãoquetenhoéadequeadefiniç ãodeconsultornãoreflete
emnadaarealidade.Noformatoatual,osABAPersficampresos,enjaulados
emumcírculoviciosodetrabalhoquedestróisuacriatividadeeasuareal
capacidadedeprestarconsultoria.
46

## Página 61

CasadoCódigo Capítulo5. Carreira,motivação,universoetudomais
Fig.5.2:LOOPeternodeumABAPersemlembraç as
Pense:seosprocessosnosprojetosfossemdiferentes,etodos(funcionais,
abapers,keyusers)pudessemdesenharjuntosassoluções,oprojetoseriaim-
plantadodeformadiferente?
Umadasprincipaisarmasdeumprogramadoréasuacapacidadedeabs-
trairosproblemasemontaraarquiteturadosistemanasuamente,prevendo,
assim,futurosproblemasnapartetécnica.Essainformaç ãoéextremamente
valiosaemmomentosiniciaisdeumprojeto,epodedefinirosrumosqueele
vaitomar(paraobemouparaomal).
EssefluxodetrabalhonãoéditadopelosABAPers,éalgopresenteno
mundoSAPhámuitotempo.Éumparadigmaenraizadonasempresas.
OABAPerquetrabalhaporintermédiodeumaconsultoria, alocado
emclientes,normalmenteprecisaentregarseusdesenvolvimentosnomenor
47

## Página 62

5.1. SeráquetodoABAPerémesmoumconsultor? CasadoCódigo
tempopossível,sendoqueotempoparaentenderocontextodoprojetose-
queréconsiderado. Essafaltadeenvolvimentocomapartededefiniç ãoe
arquiteturaéfrutodosmaisdiversosproblemas,desdesistemascomusabi-
lidadeterríveisatéfalhasestruturaisquepodemgeraratrasosou,emcasos
graves,projetosperdidos(quandooclientedesistedeterminarumprojeto).
Existealgumaformademelhoraressecenário?
Nossomundogiraemtornodasestimativas: quandooclienteprecisa
fazeralgumaalteração/extensãodoseusistema,elepediráparaa(s)consul-
toria(s)fazer(em)umaestimativadetempodotrabalho,paraavaliarqualserá
ocustodatarefa.
Existemdiversastécnicasparadescobriro“númeromágico”dehorasque
serãogastascomumdesenvolvimento:abordagenscientíficascomoaanálise
depontosdefun ção,queusamtécnicasparaestimarotempoapartirdas
funcionalidadespercebidaspeloousuário;abordagenspráticascriadaspela
experiênciadeprogramadores,comoascompartilhadasporSteveMcCon-
nellnolivro Software Estimation: Desmystifying the Black Art;guidelinesde
estimativas(muitocomunsemconsultorias),quedirãoqueafuncionalidade
ABAPXvailevarYtempoparaserimplantada;ouatémesmoobomevelho
“2semanas”,semembasamentoalgum.
Independentedaabordagem,esseéomomentoperfeitoparaoABAPer
exercer,enfim,opapeldeconsultor:paraestimar,éprecisoimaginar como
osistemaseráimplantado.Paraarquitetarumasoluçãotécnica,énecessário
entenderosrequerimentosdocliente/funcionais,analisarasinterfacescom
outrosprogramas,verificarosimpactosemoutrosprocessosatuais,antecipar
barreirastécnicaselimitaçõesdosistema,avaliarseépossívelsimplificaro
processo...
Àsvezes,oparecerdoABAPerpodeinvalidarcompletamenteacriaç ão
deumprograma(porsercomplexodemais),oumesclardesenvolvimentos
emproldasimplicidade(qualanecessidadedetrêsinterfacesnovas,sejá
existemtrêsinterfacesnosistemaquefazempraticamenteamesmacoisa?).
Naminhavisão,amelhormaneiradedemonstraraimportânciadotraba-
lhoABAPer,nosmomentosdedefinição,énãomenosprezarasestimativas.
Entendermuitodalinguagemparaotimizar SELECTsémuitoimportante,
48

## Página 63

CasadoCódigo Capítulo5. Carreira,motivação,universoetudomais
mastãoimportantequantoéotimizaraarquiteturadoprogramaduranteas
definições,removendotodaequalquersele çãodesnecessária.
Étentador“chutar”valoresextremamentealtospararequerimentosque
serãotrabalhosos,masissosócontribuiparaqueoABAPercontinuepreso
emseu LOOPcomotimefuncional,semvozativaesemparticipaç ãonos
rumosdosprojetos.
Emnossapráticadiária, umtítulodeconsultorouprogramadorterá
poucaimportância.Maisimportanteétentarenvolver-secadavezmaiscom
asdefiniçõesdosprojetospormeiodasestimativas,oureuniõesde blueprint.
Issofarácomqueonossoconhecimentotécnicopossaterimpactosbenéficos
nosprojetos,agregandovaloresgrandesàsoluç ãoentregueaocliente.
5.2 Não seja atingido pelo despreparo alheio
Umaconversarecorrenteemescritóriosdeconsultoriaseempresasquetra-
balhamcomSAPésobreodespreparodepartedosprofissionaisqueofere-
cemseusserviçosnomercadobrasileiro. Mesmocompoucotemponessa
área,vocêcertamenteescutarádiversashistóriassobreprofissionais picaretas
epessoasquenãotêmcondiçõesdetrabalharemprojetose/ousuporte.
ÉmuitocomumprofissionaisquetrabalhamcomSAPconheceremal-
gumapessoaqueépopularmenteintituladade“mauprofissionalquesabe
sevender”. Casovocê(ainda)nãoconheça,penseemumprofissionalque
afirmaterconhecimentossólidossobrealgumatecnologia,masacabademo-
randohorasinfinitasparaconcluirtarefasbásicas,alémdenãomostraros
taisconhecimentossobrepraticamentenadadoqueenvolveseutrabalho.
Notequenãoestouconsiderandoodespreparodeprofissionaisjuniores
recém-formados:oproblemasãooscasosdeplenosesenioresdespreparados
quecoexistemcomomundodeconsultorias,projetoseclienteshámuito
tempo.
Essaspessoasbeneficiam-sedasaltasdemandaseabaixanonúmerode
profissionais. Asconsultoriassempretêmmuitapressanacontratação(por
pressãodoclienteparacome çarosprojetos),eváriosdesses vendedoresen-
tramdeformadespercebidanosprojetos.Atéalguémdescobrirqueelenão
sabenada,ocaosjáfoiinstaurado,trazendomuitadordecabe çaenoitesmal
49

## Página 64

5.2. Nãosejaatingidopelodespreparoalheio CasadoCódigo
dormidas.
Essetiposituaçãoestálongedeacabare,provavelmente,nuncaseráex-
tinta. Filtrarnaentrevistaalguémdespreparadoparaalgumacoisarequer
umníveldeconhecimentoquemuitosrecrutadoresnãopossuem–emesmo
aquelesqueotêmpodemterdificuldadesnoprocesso.
Contratarapessoacertanãoéumatarefafácil:todasastécnicasderecru-
tamentoesele ção–comotestes,avaliaçãocomportamental,avaliaçãoprática
edinâmicas–sãomeiosdetentarconseguiroprofissionalcorreto–ene-
nhumadelaséinfalível.
Pioraofatodequeapressanacontrataç ãofazcomqueoprocessoseletivo
pulealgumasetapase,muitasvezes,aprovatécnicaABAPeréfeitasomente
pelaconversa(ousóportelefone). Sevocêjátrabalhouparamaisdeuma
consultoriadeveterseacostumadocomofatodenãosernecessáriofazer
nenhumtipodeprovapráticanoprocessoseletivoparaumavagadeABAPer.
Orecrutadornãoavalianenhumdosseuscódigos,nãovêvocêinterpre-
tandoumrequerimentodocliente,nãovêvocêcriandoalgumasoluçãopara
umproblema...Oquecontasãoexperiências,respostasparaperguntastéc-
nicas“padrão”eumaeventualindicação. Trêsitensquedeixamasportas
abertasparaqualquerumquesaibasevender.
EssecenáriojogacontraapráticaABAPer,eonivelamentodoconheci-
mentonecessárioparaalguémganharotítulodebomprofissionalnomundo
SAP,nogeral,tendeasermuitobaixo.Exemplo:sevocêtrabalhaemumpro-
jetopequenocom2ABAPers,sendoque1deleséumABAPerdespreparado,
vocêtemgrandeschancesdedestacar-sesemfazermuitacoisa,ganhandodi-
versoselogiosporpartedocliente,edepessoasquenãoconseguemavaliar
osdetalhestécnicosporpartedaconsultoria(seelesnãoconseguemavaliar
corretamentenacontratação,porqueavaliarãocorretamentenosprojetos?).
Aospoucosvocêcriaailusãodequeéumprofissional fora da curva,e
deixadetervontadedeestudarebuscarconhecimento,porpensarquejá
sabeosuficienteparamanter-serelevanteparaomercadopormuitotempo.
Essasituaçãopodeacontecerdeumaformanãoexplícitaaolongodesua
carreira,epodeprejudicarmuitooseudesenvolvimentoprofissional.Elafará
comquevocêentreaindamaisnoseu“mundinho”,ondetudoquevocêfaz
éperfeitoenãoénecessárioaprendernadanovoenemseatualizar.Sevocê
50

## Página 65

CasadoCódigo Capítulo5. Carreira,motivação,universoetudomais
consegueresolverosproblemasdaqueleprojetoeaindaéelogiado,paraque
mudar,nãoémesmo? Éassimqueaondadodespreparopodeatingir-lhe,
semquevocêperceba.
5.3 Desv alorização do mercado
“OsABAPersestãosendodesvalorizados!Astaxasestãoabaixando!Somos
vítimasdeconsultoriasmercenárias!”. Escutoreclamaçõesdessetipodesde
2006,quandocomeceiatrabalharcomABAP.
Veteranosdizemqueelasjáexistiamnofinaldosanos90,quandooSAP
ERPaindaestavasepopularizando.Equeméquemaisadorareclamarsobre
injustiçassalariais? Osmesmosdespreparadosquesobrevivemnoecossis-
tema.
Por trás dessas reclamações, há um raciocínio bem simples: “Por
que aprender algo novo, se existem tantos profissionais ruins e, com o
pouco que eu sei, consigo ser bem remunerado? Por qual motivo pre-
cisogastartempoaprendendotécnicasetecnologiasatuais,secomomeu
START-OF-SELECTION, FORM BUSCA_DADOS, FORM FORMATA_DADOS e
FORM MOSTRA_RELATÓRIO (separaçãoextremamentebásica–equasesem-
prefalha–dalógicadeumprogramaABAP)consigoganharumbomsalá-
rio?”.
Éessetipodegentequeodeiacompartilharsuaspreciosas“manhas”
(comosenãoexistisseainternet), odeiaensinarinicianteseficairritada
quandovêjunioresdiscutindoconceitosquenãosãofamiliaresentreosmais
velhos.Écomoseareclamaçãofosseummecanismodeautodefesa,paranão
vazaromedoconstantedeserempassadosparatrás.
Oquemuitagentenãopercebeéqueonossoconhecimentocomopro-
gramadoréoquetráslucroparatodososenvolvidosnoprocesso:clientes,
consultoriaseopróprioprogramador. Potencializandooconhecimento,é
possívelreverterocenárioefazercomqueomercadotenhadepagaroseu
valoremvezdevocêterdereclamardeumasupostadesvalorizaç ãogenera-
lizada.
CertavezrecebiumareclamaçãodequeosartigosdoABAPZombiecon-
tribuíamparaabaixarataxadomercado.Ficopensando,então,seesselivro
51

## Página 66

5.4. Ovalordarevisão CasadoCódigo
farávocêperderseuemprego(atualoufuturo)...
Mantendoamotivação
Émuitoimportantequevocêfiqueatentoenãosedeixelevarporre-
clamaçõesirreaiseumsupostosensodesuperioridadetécnica,baseadana
comparaçãocomumpossíveltrabalhomedíocredosseuspares.
Particularmente,gostodeusaroensinocomomecanismoparaalavancar
meuprogressoefugirdessecenário.Compartilharconhecimentoémaisdo
queumaformadefazer“umnome”–essaéapartemenosimportante. A
responsabilidadedeensinaralgocorretamentegeraumanecessidadecons-
tantedepesquisarafundosobreosdiversosconceitos,paracomporartigos
queentregueminformaçõesdequalidade.
Issofuncionaparamimeparamuitosoutros,maspodenãofuncionar
paravocê. Éprecisoquevocêencontreoseuprópriomecanismo. Gosta
debuscarsoluçõesparadúvidas?Gastealgunsminutosdiárioslendoo feed
dacomunidadeABAPdoSCN,queagregaperguntastécnicasdepessoasdo
mundotodo.Preferealgomaisprático?Envolva-secomacriaç ãodealguma
ferramentaABAPopensourceatravésdoGitHub. Vocênãoédotipoque
gostadedesenvolveremcomunidade? Entãomelhoresuashabilidadesde
programação,utilizandositescomproblemasmatemáticosfeitosparaserem
resolvidosporprogramadores,comoo Project Euler.
OmundoSAPestá,infelizmente,recheadodeABAPersquenãofazema
mínimaideiadoqueestãofazendo.Nãodeixequeodespreparodosoutros
sejaarazãoprincipaldoseutriunfo.
5.4 O v alor da revisão
Aprimeiravezquepasseiporumprocessode Peer Review(revisãodepares),
emqueumapessoarevisavaabsolutamentetudoqueeutinhageradodurante
odesenvolvimentodeumprogramaABAP(incluindodocumentaç ãoetes-
tes),foiquandoeuaindaeraumestagiário.
Esseprocessoderevisãocontinuadamanteve-seduranteos4anosemque
trabalheinaquelaempresa. Sempre,antesdeentregarumdesenvolvimento
paraumcliente,algumprogramadormaisexperienteparavaalgumashoras
52

## Página 67

CasadoCódigo Capítulo5. Carreira,motivação,universoetudomais
(jáprevistasnocronogramadoprojeto)erevisavatudoqueeuhaviafeito.
Todasaquelasdiscussõesqueeutivecomprogramadoresexperientesso-
breastécnicasdeprogramaçãoearquiteturadesoftwareforamextremamente
benéficasparaaminhaformaçãocomoABAPer.Lembro-medeficarcons-
tantementefrustradoquandoalguémachavaalgumproblemaemumdesen-
volvimentomeu,aopontodecome çarafazerumPeerReview antesdoPeer
Review.Ouseja,eumesmorevisavaacoisatodanosmínimosdetalhesantes
deentregar.Mesmoassim,oserroscontinuavamaparecendo.Errosmenores,
éverdade,masaindaassimerrosquepoderiamatrapalharousodaquiloque
euhaviacriado.
Umfatoimportanteadestacaréqueessamecânicafuncionavamuito
bem,poiseutrabalhavaemuma“FábricadeSoftware”noiníciodaminha
carreira.EmvezdemandarosABAPersatéocliente,todostrabalhavamre-
motamenteemumsóescritório,atendendomúltiplosprojetos.
ExistiamdivisõesdeABAPersparacadaprojeto,masafábricadispunha
deprocessosparaaumentarsuaprodutividade,eumdesenvolvedorpoderia
atendermaisdeumclienteseassimfossenecessário. Umdosindicadores
chavesdafábricaeraaqualidadedosoftwareentregue,portanto,eracrucial
queotrabalhofosserevisadonoprocessodePeerReviewantesdaliberaç ão
paraocliente(aindamaisporboapartedaequipeeracompostadejuniores
eplenos,umdospilaresquegeramdinheironesseesquema).
Poisimaginevocêqualfoiomeuespantoquandoeusaídessaconsultoria
edasuafábricadesoftwareparatrabalhardiretamentealocadoemprojetos
declientes.QuasenenhumaconsultoriaABAPaplicaalgumprocessodePeer
ReviewparaABAPersemalocaçõesdessetipo,tudodependedocliente:seele
nãotivernenhumprocessoparamanteraqualidadedoscódigos,ninguémse
importa.
Eraextremamenteestranhoeassustadorsaberqueumprogramameu
iriasubirparaumambientedeprodução,semtersidorevisado.Tantoqueeu
faziamaisumPeerReviewemcimadoqueeumesmodesenvolvia,ouseja,
oPeerReviewantesdoPeerReview(queeraparaserantesdoPeerReview,
que,nessecaso,nãoexistia).
Aospoucosfuinotandoque,alémdeninguémseimportarcomrevisões,
muitostinhamummistodemedoevergonhadequealguémolhasseosseus
53

## Página 68

5.4. Ovalordarevisão CasadoCódigo
códigos.Dependendodapessoa,sugeriralgumamelhoriatécnicaeraassinar
umatestadodediscórdiaeterna,poiselairiatemarcarcomoocara chatoque
fica fuçandonoprogramadosoutros. Nãoexistiaargumentaçãooudiscus-
sãoemproldamelhoriamútua(afinal,asugestãodemelhoriapoderiaestar
errada!),erasomenteumabirraboba,nomaiorestilo4ªsérie.Surreal.
Ah,masacoisaficavaaindapior.
Acontecequeeusempretivemuito coachingnoiníciodeminhacarreira.
Acadafinaldeprojeto,fazíamosumareuniãodefeedback,eolíderepro-
gramadoresmaisexperientesdestacavampontosemqueeutinhaidobeme
ondeeutinhacometidoalgumdeslize.
Haviaatéumapessoadedicadaacoletarfeedbacksdoslíderesdoprojeto
ondeeuhaviapassado,paraentãopoderdiscutircomigoodirecionamento
daminhacarreira(emumprogramade mentoring).
Voltandoaoprojetodiretonocliente,meuprogramasemrevisãoquejá
estavaemumambienteprodutivo,sejaporcontadasminhasautorrevisõesou
porpurasorte,nãohaviacausadonenhumtipodeproblema.Apósotempo
desuporte,oprojetochegavaaofim.Eoqueaconteceu?Exatamente nada,
alémdaalocaçãonopróximocliente.
Feedbacks,processosderevisãodecódigo,programaç ãoemparesedis-
cussõestécnicasdeveriamseralgo normal,enãoaexce ção.Comoépossível
que,apósmaisde30anosdeindústriaSAP,asconsultoriasaindanãoenxer-
guemosproblemasqueafaltadessetipodepráticacausaparaseusclientes?
Paracomeçar,oABAPerquenuncapassoupornadadissocriaumbaita
deumegodotamanhodomundo.Seninguémnuncareclamoudoseutraba-
lho,eseusprogramassempreforamparaoambienteprodutivoefuncionaram
(mesmoquedepoisde1zilhãodecorre çõesdeerro),issoquerdizerqueele
sabeprogramarmuitobem,certo?
Nãoimportasefuturamenteaquelesquedarãomanuten çãoemseuspro-
gramaspassaremnoitesdebugandoumerroporcontadapéssimaestrutura
docódigo.OABAPertambémquasenuncavêousuário(maissobreissono
capítulo7),entãotambémnãoimportaseastelascominformaç ãosãotão
confusasque,paraextrairalgumainformaç ãodeumrelatório,sejapreciso
exportá-loparaoExcel(!!!)etratarosdados,jáqueoprogramanãoostrata
porcompleto.
54

## Página 69

CasadoCódigo Capítulo5. Carreira,motivação,universoetudomais
Como é possível elevar a qualidade dos seus profissionais, sem dizer quais 
são seus pontos fortes e fracos? As empresas que provêm serviços ABAP ado-
ram achar que a solução para melhorar a qualidade da equipe é dar treina-
mentos, quando o que falta é uma boa dose de verdade. Ou seja, ser aberto 
aos seus funcionários quanto aos seus pontos fortes, fracos e sobre o que pode 
ser melhorado.
Onde você entra nessa história? É simples: peça para alguém mais experi-
ente revisar seus códigos. Crie pequenas unidades de códigos automatizadas 
– uma classe, um conjunto de funções etc. – para serem utilizadas por mais 
de uma pessoa, e peça para que elas avaliem se a solução técnica atende às 
necessidades.
Dois programadores poderão resolver um mesmo problema de formas 
completamente distintas. Discutir as soluções e caminhos diferentes é um 
exercício riquíssimo. A cada final de projeto, pe ça para seu líder (ou até 
mesmo o c
liente) uma análise do seu trabalho técnico. Veja se aquele modelo 
mental do “você profissional”, criado pela sua cabeça, condiz com a realidade.
Mesmo sozinho em um projeto, existem inúmeras formas de conseguir 
feedback técnico. Uma maneira interessante de ganhar outras perspectivas 
em cima do seu trabalho é compartilhando-o pela internet.
Você pode fazer isso por meio de qualquer rede de compartilhamento de 
código, como o GitHub (que reconhece a sintaxe ABAP nos arquivos texto de 
final .abap), ou mesmo por meio de tópicos no fórum principal da comu-
nidade, o SCN.
A prática de compartilhar código ABAP ainda não é popular no mundo 
SAP, mas está crescendo aos poucos. Dê uma olhada no filtro do GitHub para 
a palavra ABAP, disponível em http://bit.ly/2biqpmR, para ter uma ideia.
Se voc considerar que a SAP liberou somente em 2014 o compartilha-
mento de códigos ABAP em qualquer plataforma, até que 300+ repositórios 
envolvidos com ABAP, de alguma forma é um volume razoável (razões legais 
impediam o compartilhamento de código fora do site da SAP até meados de 
2014. Sabe como é, empresas antigas são cheias desses rolos).
Independente do canal, é importante saber que receber feedbacks, técni-
cos ou não, é fundamental para a sua formação. Mesmo para um sênior que 
tenha crescido nesse cenário completamente estranho, sempre há tempo.
55

## Página 70

5.5. Estudosecomunidade CasadoCódigo
Paraterminar,éessencialquevocêescolhabemquaisconselhosdados
durantealgumtipoderevisãodeverãoserincorporadosnoseutrabalho.Um
bomrevisordecódigonãovaiimporoseujeitodetrabalhar. Exemplode
imposição: pedirparaquevocêaltereosímbolodetodasasexpressõesde
igualdadede =para EQ.Issonãoénenhumamelhoriadecódigo,éuma
convençãoqueorevisoracreditaser“melhor”.
Arevisãoquetrarábenefíciosparaasuaevoluç ãocomoprogramadoré
aquelaquequestionaosmotivosquelevaramvocêatomarasdecisõestécni-
casquetomou,paraimplantarosrequerimentos.Revisõesdeperformance,
melhoriasdeestrutura,dicasdecomandos/técnicasquepoderiamtersido
utilizadaséotipoderevisãoquetrarávalor.
Manias de código
Confesso que demorei algum tempo até entender que o meu jeito de 
programar não é a única forma de fazê-lo. Todo  programação tem as suas 
manias, que não tem relação nenhuma com a estruturação do código, 
mas sim com a forma como ele é escrito.
Se levarmos em consideração a quantidade de palavras reservadas 
do ABAP, é fácil imaginar que cada  programador (ou time) acaba cri-
ando o seu jeito de indentar e escrever os comandos. Acessando este site 
http://bit.ly/2byVRka, você poderá ver diversos ABAPers com-
partilhando suas manias.
Aproveiteecompartilheassuastambém!
5.5 Estudos e comunidade
JáescuteiinúmerashistóriasdeABAPersmaisantigossobrecomoeradifícil
conseguirinformaçãoquandoosistemasepopularizounoBrasil,nomeio
dosanos90.Eracomumabriremumaapostilacomotítulo“ABAPBásico”
nafrentedeclientes,antesdecome çaradesenvolverumnovoprograma.Não
haviamfóruns,aofertadecursoseraescassa(emuitocara!)enãoexistiam
muitosconsultores.Olemaeraaprender-fazendo,esejaoqueosdeusesqui-
serem.
56

## Página 71

CasadoCódigo Capítulo5. Carreira,motivação,universoetudomais
Hojeemdia,todoprogramadoraprendelogodecaraqueoGoogleé
oseumaioraliadonabuscadeinformações. Umarápidapesquisaporal-
gumcomandoABAPretornaráinúmeraspáginas,comdefinições,explica-
ções,exemplosetc.Ainformaçãoéabundante,tantoqueéprecisotomarum
certocuidadoaocopiartodoequalquerexemplo,jáquemuitospodemestar
completamenteerrados.
Omaisinteressanteéquenemtodoesseconteúdofoigeradopelaprópria
SAP.Aliás,amaiorpartefoigeradoporoutrosABAPers,quedispuseramdo
seutempopararesponderalgumadúvida,porvezesmontandoexemplosou
protótiposparaexemplificarsuasteorias.
OsitedaSAPCommunityNetwork(http://scn.sap.com)éomaiorrepo-
sitórioderespostasadúvidas,eabrigaumnúmerograndedeprofissionais
dispostosaajudarnasoluçãodedúvidas,paraosmaisdiversosproblemas.
Quemdedicatemporespondendoàsdúvidasdeoutraspessoasnãosão
gêniosdaprogramação. Sãoprogramadorescomoeuouvocê,quepassam
pelosmesmosproblemas,dúvidasequestionamentos. Jáouviuaquelahis-
tóriadequeaspessoasquemaisaprendemsãoaquelasquemaisensinam?
“Gastar”temporespondendodúvidasdeoutrosdesenvolvedoreséestudar.
Aresponsabilidadederesponderalgumacoisarelevantecriaanecessi-
dadedepesquisarsobreotemae/oucriarprotótipos,paranãofalarboba-
gem. Enãoénecessáriomuitotempoparaessetipodeatividade:umape-
quenarotinadiáriade20minutos,lendodúvidasdeoutrosdesenvolvedores
etentandoajudá-los,jáéosuficiente.
Essapartededúvidaserespostaséapartemaisóbviadainteraç ãodaco-
munidade. Porém,háumaoutrafonteótimadeleitura,quesãoosartigos
criadosporABAPerssobreosmaisdiversostemas.Artigosinteressantesge-
ramdiscussõesdealtíssimonível,quecontribuemmuitoparaocrescimento
detodososenvolvidos.
UmbomexemplosãoosartigoscriadospeloHorstKeller,umdosrespon-
sáveispeladocumentaçãodoABAP.Elecostumacriardiversospostscon-
tendoasnovidadesdasnovasversõesdoABAP,antesmesmodelasserem
liberadas,comexemplosclarosdo“antes”e“depois”decadaumdoscódi-
gos.Comoosclientescostumamdemorarparaatualizarseussistemas,mui-
tosdessestextostêmumarelevânciagarantidapormuitosmeses,comoo
57

## Página 72

5.5. Estudosecomunidade CasadoCódigo
artigo ABAP Language News for Release 7.40 – Inline Declarations
(http://bit.ly/2bqbUip) , criado em 2013, porém relevante até os dias 
atuais. Como o ciclo de atualização do ABAP nas empresas é enorme, esse 
artigo continuará relevante por um bom tempo.
A visão de que estudar é somente ler um livro ou fazer um curso está 
completamente equivocada. Envolver-se com a comunidade é estudar.
Um dos posts mais clássicos do SCN é uma discussão gigantesca sobre 
um dos temas mais polêmicos da performance em programas ABAP: o uso 
do FOR ALL ENTRIES versus o uso do INNER JOIN para “unir” tabelas 
na hora de realizar seleções (http://bit.ly/2bkOfxG) . Esse tópico tenta en-
cerrar a discussão dizendo que os JOINs serão melhores que os FOR ALL 
ENTRIES, na maioria dos casos. Lá há diversos comentários, links supor-
tando as teorias e mais de 50 mil visualizações. Mesmo assim, aposto que 
você encontrará algum ABAPer que acredita que FOR ALL ENTRIES são 
sempre melhores “porque sim”, facilmente. Experimente perguntando para 
alguns.
Estudar pelo envolvimento com comunidade é tão ou mais importante 
do que pagar cursos oficiais (ou secundários) sobre alguma técnica específica. 
As discussões e níveis de detalhes de uma comunidade engajada pode atingir 
níveis dificilmente cobertos por um curso de poucas horas.
Minha última recomendação de estudos é a de que você gaste tempo 
aprendendo absolutamente qualquer tecnologia que não tenha nada a ver 
com SAP. Os benefícios dessa prática são infinitos. Por mais que existam di-
versos guias do mundo SAP que explicam Orientação a Objetos no ABAP, 
passei a entender mais a fundo as decisões do time que desenhou o ABAP 
Objects, quando decidi aprender C++ (que tem uma, adivinhe, comunidade 
que disponibiliza vários guias gratuitos muito bons).
Todas as linguagens e técnicas de programação evoluem em conjunto, e 
muita coisa que foi criada para uma determinada tecnologia pode ser repli-
cada em outra. Aprofundar seus conhecimentos em ABAP é mandatório, mas 
ficar só nisso acaba limitando a sua capacidade.
58

## Página 73

CasadoCódigo Capítulo5. Carreira,motivação,universoetudomais
5.6 ABAP é um lixo, v amos vender coco na praia
Queatireaprimeira BADIquemnuncaescutouafrase: “Trabalharcom
ABAPémuitoruim,vamoslargartudoevendercoconapraia”.Éumacons-
tantenomeioSAPescutarpessoasbradandoqueestãoinfelizesemsuaspo-
siçõesatuaisepreferiamestarfazendoalgodiferente(eumesmojáreclamei
compessoasmaispróximassobreisso).
Entretanto,tenhoumpensamentoquevaiumpoucocontradessalenda
urbanadequeabrircocosémelhorquedebugaraVA01(nomepopularda
transaçãodoprogramadeordensdevenda). Paraquevocêentendaminha
linhaderaciocínio,vamosexplorarumpoucocomonasceessesentimento
deque“estátudozoado”.
Comosurgeadesmotivaç ãogeneralizada
• Projetoscomprazosapertados;
• Gerentes/líderestapados;
• Timecomercialquevendeerrado;
• Equipetécnicaruim;
• Tecnologiadatadaeantiga;
• Mãosatadasàsdecisõesdosclientes;
• Precariedadedaspráticas;
• Padrõeseconvençõesarcaicas;
• Umainfinidadedehorasextras;
• Usuáriosmalditosefuncionaisodiosos;
• ABAPerspilantras;
• BASISquetrabalhamsemvontade;
• Incapacidadedeusartecnologiasnovas;
59

## Página 74

5.6. ABAPéumlixo,vamosvendercoconapraia CasadoCódigo
• Recrutadorespicaretas;
• SAPéumaempresaquesóatrapalha;
• Ostandardéhorrível;
• <insirasuareclamaçãoaqui>.
QualquerpessoacomalgunsanosnaáreaABAPficadesmotivadoquanto
pensanofuturo,emgrandeparteporumaouváriasdasrazõesanteriores.
Normalmente,vocêficaextremamenteempolgadocomummardepossibili-
dadesiniciais(júnior),paraentãotomaralgumas“porradas”davidaABAPer
emprojetoscomplicadosquecome çamalhedeixarirritado(pleno),final-
menteterminandoemumaposiçãodeconformidadecomosproblemaspor
contadesaláriosbonsparaarealidadebrasileira(sênior).Boapartedadis-
cussãosobresalárioetaxasvemdesseconformismo.
NomundoSAP,somosafogadosanualmenteemummardenovosnomes,
siglaseprodutospelacomunidadeSAPmundial:HANA,Fiori,Gateway,UI5,
blá-blá-blá.Asmesmasindagaçõesquejádiscutimosserepetem:oqueestu-
dar?Oquefazer?Paraondeeuvou?ABAPéumlixoentão,éisso?
Essemedoaumentaaindamaisumadesmotivaç ãogeneralizadapeloen-
tendimentodequeaquilocomquevocêtrabalhanãoéosuprassumotecno-
lógicodaempresaqueprovêaferramentaparaseutrabalho(aSAP).Écomo
sealguémfalasse:“Olhequelegalesseteletransportadorquefazvocêirdo
BrasilatéaChinaem5segundos!Agoracaleabocaeváapé”.
SaindodomundoSAPeolhandoparaoslados,encontramosummundo
queé,aparentemente,maravilhoso.Startupsdivertidas,trabalhoremoto,tec-
nologiadeponta,pessoasfelizes,capacidaderealdeaprendizado,eventos
descolados,equipesqualificadas,<insiraalgoquevocênãotemegostaria
hojeaqui>.Todomundosabedoditadopopular:“Agramadovizinhoémais
verde”. Emummundoondevocêtrabalhaemumasalaescura,semágua,
redeeemcondiçõesprecárias,nãodáparapiorar,nãoémesmo?
Problemas,problemas,problemas...
60

## Página 75

CasadoCódigo Capítulo5. Carreira,motivação,universoetudomais
Ofuturonãoépromissor?
Penseemtudoquevocêacaboudeler.Elessãoproblemasespecíficosdo
mundoSAP,ouestãorelacionadoscomváriasáreas? Essemontedecoisas
estápresenteemtudoquantoqueélugar,eamaiorpartedelasfogedonosso
controle.
Nemmesmoumaprofissãoperfeitaestálivredeproblemas.Vamospegar
oexemplodealguémquevendecocosnapraia.Apessoaacordademanhã,
passaumprotetorsolar,arranjaoscocos,empurraseucarrinhoatéapraia,
sentaolhandoparaomar,puxaumacâmeraprofissional,tirasdiversasfo-
tosepostanaInstagram/Facebookparamassagearseuegoemostrarparao
mundocomoasuavidaéótima.Entreanálisesvisuaisde834ondasporhora
nabeiradomar,agranaaltaaparecedeformamágicaemsuacontapermi-
tindoqueapessoavolteparaacasaapósumdiasuperprodutivo,guardeseus
cocosemumlugarseguroevájogarumvideogame,bebercervejaou<insira
algoquevocêgosteaqui>.
Após1anonessavida,sealguémperguntasseparaapessoa“comoanda
omercadodoscocos”,oquevocêachaqueelaresponderia?Eu apostoque
boapartedaspessoasemsituaçõessimilaresresponderia“nãoestáfácil”.Re-
clamariampelopuroprazermórbidodereclamar.
Ograndevilãodoseufuturoévocêmesmo. Osproblemasdomundo
terãoimpactosinferioresaosproblemastrazidosporfazermalasimesmo.
Reclamarporreclamaréummecanismodedefesaparademonstraraos
outrosquenóstemosumacapacidadesuperioràquelaqueutilizamos,para
fazeroquefazemosnonossodiaadia.Eucanseidereclamarporreclamarna
minhavida,para10minutosdepoiscontinuarfazendoexatamenteamesma
coisadequereclamei(enãomeorgulhodissonemumpouco).
Euaindafaçoisso,nãoéfácilmudar.Issoéumcostume,umvício,uma
cultura.AlgoqueéextremamentecomumnomundoSAPeemoutrasáreas,
algoqueéfeitomilharesdevezesdiariamenteemtodososprojetos,clientes
econsultorias.
Serefletirmosemvoltadessemontedereclamaçõeseproblemas,veremos
quetodosrealmenteexistem,sempreexistiramesempreexistirão.Évocêque
decidecomolidarcomeleseoquantoissotudooafetará.
61

## Página 76

5.6. ABAPéumlixo,vamosvendercoconapraia CasadoCódigo
Vátreinar
Reclamarconstantementedequetudoestáumlixonãolevaaabsoluta-
mentenada.NósgostamosdecriticaraSAPporabsolutamentetudooque
acontece,comoseelafosseresponsávelporfazerascoisasdireito,paraque
nóspossamostriunfardaformacerta.ASAPfazoqueelaentendaoqueé
melhorparaela,assimcomovocêdeveriafazeroqueachamelhorparavocê
emvezdereclamar,reclamar,reclamarenãofazernada.
MeumestredeHapkidocostumavadizerumacoisaqueficoumuitomar-
cadaemminhavida: vátreinar.Emvezdeficardiscutindoseaartemarcial
XémelhorqueaY,vátreinar.Nãopercatemporeclamandodasfederações,
vátreinar. Nãoalimenteoegoquerendoprovarquevocêéomaisforte,vá
treinar.Nãosejavencidopelapreguiça,vátreinar.
Nãofiquesonhandocomavendadecocosnapraia,vádebugar.
QueraprendercoisasnovasnoSAP?Váemfrente,esforce-se!Quersair
domundoSAP,entãomexa-se! Estudealgodiferente,crieprojetosnovos,
corraatrásdoseusonhomaluco.Nãoquerestudarnada,nãoqueraprender
nadanovo,quercontinuarcomoseuABAPepronto? Ótimo,melhoreseu
nívelABAPenãosesintamalcomaescolha.
Nãosejacontagiadoporvisõespessimistas. Issonãovailevaranada.
Vocênãoprecisaconcordarcomtudoqueaconteceemsuavolta,masdeixar
defazeralgosobreaquiloquelheincomodaéondemoraoperigo.Enquanto
vocêficarparado,nadaacontece.Omundomuda,masvocêficanamesma.
Eaí,oquevaiser?
62

## Página 77

Capítulo6
OstabusdomundoABAP
Conformevocêfor(digi)evoluindocomoABAPer,vocêentenderáqueboa
partedotrabalhoépegarummontedecódigoantigoetentarfazeralgocom
aquilo. Porseremcódigosmonstruosos,ficamuitodifícilentendertodaa
lógicaparapodercriarumanovaalteraç ãoquecondigacomaestruturaori-
ginalmentepreparadaparaoprograma.
Naprática,cadanovodesenvolvedorvaiincorporarasnovasalterações
doseujeito,torcendoparaquesuasinclusõesnãoquebremnadaquejáfun-
ciona.Eaquelesqueajustaramocódigopodemserpessoasdeníveistécnicos
diferentes,comseuspróprioscostumeseformasdetrabalho.
Essesprogramastornam-segrandescolchasderetalhos.Diversaslógicas
espalhadas,cadaumaàsuamaneira,gerandotitãsde30millinhas.Sóque,
apesardessemontedecódigosmalucosecomplicados,oobjetivofinaldo
programaprovavelmente continuaomesmo. Elepodefazerumaouduas

## Página 78

6.1. Fantasmasdopassado CasadoCódigo
coisasamais,entretantodevecontinuarentregandooresultadofinalpara
quefoioriginalmentecriado.
Apartemaislegaldessahistóriaéquepouquíssimaspessoasserãocapazes
dedizeroqueoprogramafazpordentro(talvezninguémsaiba). Funciona
eissoéosuficiente.
Umprogramadorconsegueaprenderbastantecriando,mastambémcon-
segueaprendermuitolendocódigosalheios.Oprogramamonstrofunciona,
entãotemoseuvalor.UmABAPerjúniorpodeleras67millinhasdecódigoe
evoluirmuitocomodesenvolvedor,nãoémesmo?ABAPersexperientesres-
ponderiamque“elepodeaprender,masprecisatomarmuitocuidado”.Sendo
umprogramaantigo,deveestarinundadodetécnicasultrapassadaseestru-
turaçõesineficientes,servindocomohistóricodalinguagem,masnãocomo
basedoquedeveserusadonacriaç ãodeumnovoprograma.
Essabrevefábuladeumprogramajurássicorepete-seaoanalisarmosa
práticaABAPcomoumtodo. Pensebem: nopassado,alguémcriouuma
formadetrabalho,visandoconsistênciaequalidadenoprocessodedesen-
volvimento.Aolongodosanos,muitaspessoasforamcontribuindoparaque
issoevoluísse. Seráquetodaselasavaliaramoprocessocompletodeforma
objetivaparaimplantar“melhorias"?Ouseráquecadaumatambémestava
munidadeseuspróprioscostumeseformasdetrabalho,implantandodeter-
minadanovapráticacomosefosseamaiscorreta?
OprocessodedesenvolvimentoABAPtambémpodeterviradoumacol-
chaderetalhos?Existempráticassemsentidoquesãoseguidasporequipes
deprojeto,semquestionamentos?
VamosveralgunsaspectoscruciaisdapráticaABAPparavalidarseal-
guémrealmenteavaliouoprocessocomoumtodo,ousesimplesmenteadi-
cionouoseu PERFORM resolve_somente_o_meu_problema paraen-
tregarademanda.
6.1 Fantasmas do passado
SendooABAPumalinguagemdeprogramaçãodecertaidade,énaturalima-
ginarmosqueomercadojádeveterpassadopordiversasfasesdiferentes.
Tudooquegiraemtornodomercadodesoftwaresofreudiversasmudan-
64

## Página 79

CasadoCódigo Capítulo6. OstabusdomundoABAP
çasnosúltimos30anos(épocaemqueoABAPfoicriado),eessasalterações
certamenteatingiramapráticaABAPnasempresas.
Eugostodedizerque“nomundocorporativoarodagiramuitomaisde-
vagardoquegostaríamos”. Somosdiariamenteinundadosemredessociais
esitesdenotíciapormaneirasinovadorasdetrabalho,timesespalhadosem
várioslugaresdoglobo,equipesaltamenteprodutivasimplantandometodo-
logiasmalucaseprogramadorescapazesdecriarsistemaspararesolveros
maisdiversosproblemas.
Essedinamismonãoestápresenteemambientescorporativos,porum
motivoóbvio:qualqueralteraçãobruscanostimesinternosdeumaempresa
temapossibilidadedegerarimpactosnegativosemseusnegócios.Mudan ças
costumamsermeticulosamenteanalisadasantesdeseremincorporadaspelos
timesdedesenvolvimentodegrandesempresas.
Naprática,profissionaisSAPestãoacostumadosaenfrentarpráticasan-
tiquadasdetrabalho. Asformasantigasvãodesdemetodologiasdeprojeto
atéaprogramaçãonossadecadadia. Muitosfantasmasdopassadoassom-
bramavidadosABAPers,quemuitasvezesincorporamessesfantasmassem
perceberem.
Paraexemplificaresseprocesso,noquedizrespeitoaoscódigos,umdos
fatoresquemaiscontribuemparaessefenômenoéoqualveremosnasequên-
cia.
Aretrocompatibilidade
OSAPERPmantémaretrocompatibilidadecomversõesmaisantigasdo
ABAP.Issoquerdizerquealgumafuncionalidadeantigacontinuaválidaem
programascriadoshoje,mesmoquejáexistaumformamaisnovaerobusta
deimplementá-la.Conformeexplicadonocapítulo 1,oSAPcontémseuspró-
prioprogramasescritosemABAP,eaquantidadedelinhasdecódigo stan-
dardnosistemaérealmentegrande.Sãomilharesemilharesdeprogramas
criadosparaasmaisdiversasfuncionalidadesequecontinuamsendousados
emambientesprodutivosnosdiasatuais.
Normalmente,areaçãoaonosdepararmoscomalgumcódigo standard
éadejogartudoforaereescrevercompletamenteaaplicaç ão. Porém,se-
riaumaloucuratotaltentarrefazeroSAPERPdozero–issopoderiamatar
65

## Página 80

6.2. Impactosnosprocessodedesenvolvimento CasadoCódigo
completamente o produto.
Joel Spolsky nos conta um pouco do que aconteceu com o Netscape 
quando o seu time de desenvolvimento tentou recriar o produto, no clássico 
post Things You Should Never Do, Part I (http://bit.ly/2bkOfxG) . A situ-
ação aqui é semelhante: por mais que os códigos não sejam perfeitos e usem 
técnicas datadas, eles já passaram por diversos níveis de aprovações de uti-
lização em ambientes produtivos. Para a estratégia da SAP como empresa, 
manter a retrocompatibilidade do ERP é algo crucial para seu negócio dar 
certo.
6.2 Impactos nos processo de desenvolvimento
Voltando à questão da inovação, se as empresas demoram para incorporá-las, 
imagine seus profissionais. A programação ABAP é inundada por mitos, teo-
rias e manias que já caíram por terra há muito tempo. A retrocompatibilidade 
contribui para que cada ABAPer crie seu próprio mundinho da programa-
ção, recheado das coisas que ele sabe que funcionam. O que é novo, diferente 
ou estranho deve ser ignorado, até que algum cliente exija. Essa abordagem 
tem reflexo em desenvolvedores, funcionais, líderes, gerentes... É tentador 
acomodar-se em meio àquilo que você já conhece (o seu mundinho), mas sair 
constantemente da sua zona de conforto é essencial para manter uma carreira 
de sucesso.
Muitos zumbis nascem ao incorporarem práticas sem questionar se elas 
fazem ou não sentido. Todos eles compartilham uma mesma condição, que 
eu gosto de chamar de “síndrome do robô”.
Fuja da síndrome do robô
UmaconstruçãocomumnomundodoABAP:
LOOP AT table INTO line .
CALL FUNCTION 'BUSCA_INFORMACOES_ADICIONAIS'
EXPORTING
material = line -material
TABLES
details = material_details[] .
66

## Página 81

CasadoCódigo Capítulo6. OstabusdomundoABAP
(...)
ENDLOOP
Simples, não é? Considere que a fun ção
BUSCA_INFORMACOES_ADICIONAIS é uma função standard que re-
tornará todas as informações adicionais dos materiais para a tabela
MATERIAL_DETAILS.Éótimodescobriraexistênciadealgomágicoque
retornatodososdadosformatadosexatamentedojeitoqueprecisamos.Eé
nessesentimentodefelicidadeondemoraoperigo.
ComopraticamentetodoocódigoABAPcriadopelaSAPéabertopara
visualizaçãoedebug(émuitoraroencontraralgumcódigoquenãosejapos-
sívelvisualizar),constantementetentamosresolvernossosproblemasusando
asmesmasfun çõesqueosprogramasstandardutilizam. Aliás,essaéuma
boaprática:emvezdereescreveraroda,devemossempreprocurarporfun-
çõesouclassesstandardqueresolvamnossosproblemas,principalmentepor
contadacomplexidadeenvolvidanamanipulaçãodedadoseregrasdenegó-
ciodentrodoSAP.
SóquenemsempreoABAPerdaSAPcrioudeterminadafun çãopen-
sandonoreúso. Muitasvezeselafoicriadapensandonocontextodaquele
programastandard,ouemumgrupodefun çõesespecífico.Elacertamente
resolveosproblemasgeradosporaqueleprograma,maspodenãotersido
criadanemotimizadapensandonareutilizaçãoemoutroscódigos.
Afunçãodoexemploinicialfoicriadaparabuscarosdadosdeummate-
riale,aparentemente,resolvetodososproblemas.Sóqueessetipodefaz-tudo
podefazermilhões(oumelhor,bilhõesoutrilhões)desele çõeseacessosao
bancodedados,destruindoaperformancedoprograma(ouatédosistema).
AolongodessesanostrabalhandocomABAP,tenhonotadoquepoucas
pessoaspreocupam-seemanalisarocódigodentrodafun çãoantesdeutilizá-
ladentrodelaçosparamilhõesderegistros.Ludibriadopelafacilidadecom
queosdadoschegam mastigadosaoprograma,éfácildarumtironoseupé
ounodealguémquealgumdiavaiterdefazerumaanálisedeperformance
notalprograma,quedeverodarmaislentoqueotrânsitodeSãoPauloem
umdiadechuva.
67

## Página 82

6.2. Impactosnosprocessodedesenvolvimento CasadoCódigo
Comoresolver?
Infelizmente,nãoháumaregraquepodeseraplicadasempre:cadacasoé
umcaso.Oidealéquevocêverifiqueoqueafun çãofazantesdesairenfiando-
aemtudoquantoé LOOPdoseucódigo.Ostandardpodetercódigosreal-
mentecomplexos,masutilizandotransaçõescomoaST05ouSE30,épossível
terumarápidaideiasealgumasdasfun çõespodemserprejudiciais.
Voucontarumapequenahistóriadeexemplo.Certavez,ajudeiemuma
análisedeperformanceemumprogramagigantesco,eomaiorproblemaera
umachamadadefun çãoparabuscaralistatécnicadosmateriais,executada
diversasvezessemmotivo:
LOOP AT purchase_orders INTO purchase_order .
CALL FUNCTION 'CS_BOM_EXPLOSION'
EXPORTING
matnr = purchase_order -matnr
TABLES
(tabelas de retorno c/ a lista técnica ).
ENDLOOP .
Essafunçãoexecutamuitos SELECTsemseuprocessamento,enãoera
necessáriochamá-latantasvezes.Atabela PURCHASE_ORDERScontémitens
dedocumentosdeMM(material management,umdosmódulosdoSAP),e
itensdediferentesdocumentospodemtero mesmomaterial.Alistatécnica
deummaterialnãoéumdadoquesofrealteraçõescomfrequência,portanto,
nãoexistenenhumanecessidadedeexecutaressafun çãoduasvezesparao
mesmomaterialdentrodeum LOOP.Umasoluçãomelhorémontarumca-
cheinternoparaaschamadasdessafun ção.
Nocasoqueajudeiaresolver,fizemosumcontrolemuitosimplespara
queafunçãonãofosseexecutadaduasvezesparaomesmocódigodematerial,
melhorandoaperformancedoprogramaemcercade70%.Asoluç ãoutópica
seriarefazerassele çõesdentrodoprograma,recriandoacessosúnicosacada
umadastabelasnobanco.
Naspoucashorasquetínhamospararefatoraroprograma,essasoluç ão
seriacompletamenteinviável,poislistastécnicascontêmregrasdenegócio
muitocomplexas,emuitasvariaçõesaseremconsideradas. Afun çãoreal-
mentefacilitaporconteralógicastandardqueconsideraconfigurações,mas
68

## Página 83

CasadoCódigo Capítulo6. OstabusdomundoABAP
éprecisoumaanáliseparaentenderumpoucomelhorcomoelafunciona
antesdesairutilizando-adequalquerjeito.
Esseexemplodeanáliseantesdousoéaplicávelemdiversassituaçõesdo
mundoABAP.Eletambémnosrevelaqueexisteumproblemamuitomaior
porbaixodeumasingelafun çãousadadeformaerrada.
Asíndromedorobô
Normalmente,umrobônãoécriadoparapensar:eledeveexecutaruma
tarefapré-programadadeformaeficiente,nomenortempopossível. ABA-
Pernenhumgostadeserenxergadocomoum robozinhoquebebecaféeo
converteemlinhasdecódigo.Todostambémrevelamumcertodesconforto
quandoalguémbrincaqueadivisãoABAPdeumprojetotendeaviraruma
pastelariaconformeosprazosficamapertados(“agoramevêum REPORTde
queijo,agoraumafun çãodeescarola”).
Ofatoirônicoéquemuitossecomportamcomorobôsquandocriam
soluçõesapartirdecópiasdetrechosdecódigo,semfazeremamenorquestão
deentenderoqueestáportrásdaquela classe mágicaou função faz-tudo.
Vocêpodeestarpensando: “Ah,maséimpossívelentendertudooque
umafunção/classestandardfaz”,eeudigoquecódigosstandardsãorealmente
complexosdeseremcompreendidos.Entretanto,entenderaomenosabase
dofuncionamentodotrechoquevocêestiverreutilizandotorna-seessencial
paracriarumaaplicaçãorobusta.Saberqueafun ção CS_BOM_EXPLOSION
fazseleçõesrecursivassalvadrasticamenteaperformancedoprogramaque
ausa,eomesmoéválidoparaoutrasfun ções,classes,oupraticamentequal-
quercódigocopiadodostandard(efórunsdeinternet).
Maisumexemplodasíndromesãoaspessoasquetêmumprazermór-
bidopelautilizaçãode CLEAR, REFRESHe FREEl.Sãorelatórios, formse
métodosZquecome çamcomalimpezadevariáveisque acabaramdeser
declaradas. Osujeitoteveumproblemadevariáveis sujasumaveznavida,
epreferelimpartudoporprecauç ãoemvezdeentenderoqueocasionouo
errodaprimeiravez.Nessassituações,nascemosrobôs.
AdinâmicadoSAPedaevoluç ãodalinguagemfazcomquesejaneces-
sárioreavaliarmosaquiloquesepopularizoucomo a forma correta,diaria-
mente.HáalgonoseudiaadiaABAPerqueseencaixanasíndromedorobô?
69

## Página 84

6.3. NomeclaturasemABAP CasadoCódigo
Quantotempovocêgastariaparaentenderumpoucodofuncionamento da-
quelacoisaquevocêutilizaesempresalvaasuavida?
Tenteacharrespostasparaessasquestões.Arealidadedosprojetoscerta-
menteobrigarávocêausarcoisassemsabercompletamentecomoelasfunci-
onam,mastenhasempreemmenteque,mesmocopiandoumasoluç ãodeal-
gumoutrolugar,aresponsabilidadedacópiarecém-criadaserásempre100%
sua.
Asíndromedorobôvaimuitoalémdacodificaç ão.Pensenasdocumen-
tações,nocontroledeversões,napadronizaç ãoenosprocessosderevisão.
Nãosecontentesimplesmentecomalgoque sófunciona.Tenteentenderaos
poucosoquerealmenteaconteceportrásdecadaumdoscódigoseprocessos
quevocêutiliza.
Nãoentrenomodoautomático.Fujadasíndromedorobôaproveitando
asdicasaseguir!
6.3 Nomeclaturas em ABAP
Seexisteumapessoaquecertamentenãofugiudasíndromedorobô,foi
aquelaquedissequeopadrãodenomenclatura <fs_>serviaparaalguma
coisa.Respondarapidamente:qualoutrotipodevaríavelnomundoABAP
queusa <>,semseros FIELD-SYMBOLS?Nenhuma?Certo!Então,porque
utilizarodesnecessário fs_?Oidentificador <>nãoéosuficiente?
Omotivodissoésimples:“tudovemdapadronização”. Nãobastatera
palavra PERFORMou FORMparaidentificarqueaquiloéumachamadadeum
blocodecódigo,éprecisocolocaruminútil F_.Nãobastaqueummétodo
possuaformasbemespecíficasdeserdisparado,éprecisocolocar M_emseu
nome.Issotudoérealmentenecessário?
Seimuitobemqueasgrandesempresaspossuemosseusprópriospadrões
denomenclaturaefor çamautilização. ParaopobreABAPeralocado,não
sobremuitaescolha: vocêprecisaseguirospadrõesqueoclientedecidiu;
casocontrário,alguémfarácomquevocê“ajuste”seuprogramainteiropara
queelepossaseguirparaaproduç ão.
Essahistóriadecolocarumidentificadordotipo V_antesdevariáveis
nãonasceunomundoSAP.Issoéumapráticamuitoconhecidanomundo
70

## Página 85

CasadoCódigo Capítulo6. OstabusdomundoABAP
do desenvolvimento de software, chamada notação húngara. A ideia básica 
é colocar um identificador antes do nome da variável, para que você possa 
saber de que tipo é a variável sem precisar navegar até a sua definição.
É assim que você poderia saber, por exemplo, que sNome é uma String, 
só de olhar para a variável. O seu uso é fruto de muita controvérsia e discus-
sões constantes. No artigo em inglês da notação húngara do Wikipédia, pode-
mos ver citações de desenvolvedores famosos, alguns a favor e outros contra 
(http://bit.ly/2biqMOh) . Sua adoção/aversão não é unânime.
De volta ao ABAP, a notação húngara certamente ajudou diversos desen-
volvedores da época do HEADER LINE (forma de construir tabelas que está 
obsoleta). Vamos declarar uma tabela interna com HEADER LINE:
DATA : mara  TYPE  TABLE  OF mar
a WITH HEADER  LINE .
mara -matnr  = '1234'
Se precisássemos de uma estrutura com dados da mara, poderíamos de-
clarar da seguinte forma:
DATA : mara  TYPE  mara .
mara -matnr  = '1234'
E se o nosso programa tivesse de ter, ao mesmo tempo, um mesmo bloco 
de código, a mara tabela interna e a mara como estrutura, como identificar 
qual é qual? A solução mais prática adotada na époc a foi a notação húngara, 
usando um identificador antes do nome de cada uma das variáveis:
DATA : t_mara  TYPE  TABLE  OF mara  WITH HEADER  LINE ,
wa_mara TYPE mara .
t_mara = '1234' .
wa_mara = '1234'
Dessaforma,ficamaisfácilsaberqualvariáveléqual.Assimfoinaquela
épocaeaindaénosdiasatuais.Anotaç ãohúngaraaindaéopadrãodomi-
nanteparadiversosprojetosABAP.
Bom,setemosumaótimaformadeidentificarotipodavariável,paraque
perdertempoexplicandosuautilidade,nãoémesmo?
71

## Página 86

6.3. NomeclaturasemABAP CasadoCódigo
DATA : v_tabix TYPE sy-tabix ,
v_tabix2 TYPE sy- tabix .
Ah,sãotodasvariáveissimples,etemo V_ali,oqueémaisdoqueo
suficiente!Serámesmo?Emalgummomento,odesenvolvedorpreocupou-se
emexplicarparaqueserveaquelavariável?Vamostentarreescreveromesmo
códigodeoutraforma:
DATA : indice_tabela_materiais TYPE sy-tabix ,
indice_tabela_clientes TYPE sy-tabix .
Emqualdosdoisexemplosficoumaisclaroomotivodeexistênciade
cadaumadasvariáveis?
Naminhavisão,omaiorproblemadosidentificadoresdasvariáveiséque
elasfazemcomqueoABAPervápelocaminhomaisfácil:seonomejátem
oidentificadordotipo( T_, V_etc.),nãoéprecisosepreocuparemdarum
nomequeexplicaautilidadedaquelaáreadememória.
Existeaindaumsentimentogeneralizadodequeasvariáveisdevemter
umnomepequeno.Nopassado,mantervariáveisdenomescurtosfaziasen-
tido,tantopelalimitaçãode80colunasdoeditorABAPquantopeladificul-
dadedevisualizarcódigosgrandesnodebugantigo:
72

## Página 87

CasadoCódigo Capítulo6. OstabusdomundoABAP
Fig.6.1:Issoaconteciadiretocomprogramascomplexoseeraextremamente
irritante
Desde2006,oeditoredebugdoABAPevoluíramenãopossuemessas
limitações. Outracoisaquecontribuiumuitoparaapopularizaçãodasva-
riáveiscomnomespequenoseininteligíveisfoiodicionárioABAP. MATNRé
material, BUKRSéempresae GJAHRéoanofiscal.Masasuavariávelnão
precisachamar V_MAT_GJ.
73

## Página 88

6.4. Vidaeobradasconstantesinúteis CasadoCódigo
Nomenclaturascomo <fs_>e f_nãoservemparaabsolutamentenada,
masmaisimportantequeissoédescrevercorretamenteoquevirá depois
dosidentificadores.Nãohánecessidadedemanterumavariávelcomonome
pequenosemmotivo. Quantomaisdescritivaelafor,melhor. Mesmoque
vocêsejaobrigadoausarumdessespadrões,nãoexisterazãoparafazerdisso
umamuletaedeixardedescreverorealpropósitodesuasvariáveis.
Dapróximavezquevocêforcriarumavariávelchamada V_AUX,pense
bemnomotivoquelevouàsuacriaç ão.Eutenhocertezaabsolutadeque,ao
responderapergunta“paraqueserveestavariável?”,vocêautomaticamente
vaidescobrirumbomnomeparaela.
6.4 Vida e obra das constantes inúteis
Porfalaremvariáveis,vocêjáviualgumcódigocomaseguintedeclaraç ão?
CONSTANTS : c_x TYPE c value 'X'.
Euapostoquesim. Aliás,euapostariaquevocêjáfez,fazouvaifazer
issoemalgummomentodasuacarreira,poisasíndromedorobôtemuma
penetraçãonospadrõesdeempresasmuitomaiordoquepodemosimagi-
nar.Masnãocolocaremoso LOOP FROM sy-tabix antesdo READ TABLE
BINARY SEARCH,vamosentenderumpoucoporqueessetipodeconstante
écompletamenteinútil.
Oqueéumaconstante?
Ocomando CONSTANTSéusadonadeclaraçãodeconstantes(sério?),ou
seja,variáveiscomumvalorquenuncamudaráemtempodeexecuç ão:
CONSTANTS tipo_documento TYPE char4 VALUE 'WXYZ' .
Vocêpodeusaravariável TIPO_DOCUMENTO,tendoacertezadequeseu
valornuncaseráalteradoapósoiníciodoprograma.Vocêpodeatécriaruma
estruturaconstante,veja:
CONSTANTS :
BEGIN OF estrutura ,
74

## Página 89

CasadoCódigo Capítulo6. OstabusdomundoABAP
inteiro TYPE i VALUE '123' ,
char TYPE c VALUE 'A' ,
numchar TYPE n VALUE '2' ,
END OF estrutura .
WRITE estrutura -inteiro .
Essamecânicadefuncionamentoébemsimplesdeserassimilada.Sóque
apartemaisimportanteestánarespostaparaaseguintepergunta:quando
devoutilizarumaconstante?
Imaginequevocêprecisafazerumprogramaquemostrarádadosso-
mentedeumadeterminadaempresaeocódigodaempresaseráutilizado
emdiversassele çõesevalidaçõesdentrodocódigo.Sevocêusardiretamente
nocódigoovalordaempresaealgumdiaelemudar,todoocódigo-fonte
precisaráseralteradoporcontadeumasimplestrocadevalores.
Esseéofamoso hardcode,umvalorescritoexplicitamentesemnenhum
tipodeinteraçãocomousuáriooufontesexternas(tabelasdeparâmetro,
arquivosetc.),tambémchamadode marretaemalgunscasos.
material -werks = 'ZMB1' .
IF material -werks = 'ZMB1' .
* Faça algo
ENDIF .
CASE material - werks .
WHEN 'ZMB1' .
* Faça outro algo
ENDCASE .
Seovalordaempresa( WERKS)precisassemudar,vocêteriaquealterar
trêsdiferentespontosdoprograma.Emvezdeespalharovalor ZMB1porto-
dososlados,émelhorcriarumaconstante.Assim,vocêgarantequesomente
umlugarprecisaráserajustado.
CONSTANTS : empresa TYPE marc -werks VALUE 'ZMB1' .
material -werks = empresa .
75

## Página 90

6.4. Vidaeobradasconstantesinúteis CasadoCódigo
IF material -werks = empresa .
ENDIF .
CASE material -werks .
WHEN empresa .
ENDCASE .
Tudobonito,tudolindo,tudoperfeito. “Issotudoémuitoóbvio”,você
podepensar.Então,respondarápido:porqualmotivoexistemquilos,litros
etoneladasdeconstantescom C_Xespalhadaspeloscódigos?
Hardcodeeabanalizaç ãodasconstantes
Quemfalouqueprogramadoresdeveriamevitarhardcodesfoisábio.Po-
rém,emmomentoalgumeledisseque todovalorescritodeformaliteralno
códigoéumaconstante.
Canseideverconstantes C_X = ‘X’ espalhadasporprogramasABAP.
Issoétotalmentedesnecessário,ocódigoficahorríveldeselereovalordava-
riávelnuncapoderáseralterado,jáquetemsignificados diferentesemcada
umdoslugaresondeestásendousado.Exemplodessacoisahorrível:
PARAMETERS :
p_docto AS CHECKBOX ,
p_users AS CHECKBOX ,
p_soma AS CHECKBOX .
CONSTANTS : c_x TYPE c VALUE 'X'.
IF p_docto = c_x .
* Algo com o documento
ENDIF .
IF p_users = c_x .
* Algo com o usuário
ENDIF .
IF p_soma <> c_x .
76

## Página 91

CasadoCódigo Capítulo6. OstabusdomundoABAP
* Some alguma coisa
ENDIF .
Sevocêmudarovalorde C_Xpara SPACE,issonãoquerdizerqueto-
dososlugaresonde C_Xestásendousadotêmdeseralterados.Essaéuma
variávelquenãoprecisariatersidocriada,pois nuncaseráalterada,servindo
somenteparadeixarocódigoirritantementemaischatodeserlido.
AlinguagemABAPnãopossuivaloresbooleanos(true ou false),portanto,
o ‘X’éutilizadoemvárioslugaresparadescobrirseumcampoestá“ligado”
(true, ‘X’)oudesligado(false, SPACE).
Reescrevendoocódigoanterior,imaginandoqueexistaosuporteavalo-
resbooleanos,ficaaindamaisclaroquenãofazomenorsentidoexistiressa
constante:
* Imaginando que ABAP tenha booleanos:
IF p_docto IS true .
* Algo com o documento
ENDIF .
IF p_users IS true .
* Algo com o usuário
ENDIF .
IF p_soma IS false .
* Some alguma coisa
ENDIF .
77

## Página 92

6.4. Vidaeobradasconstantesinúteis CasadoCódigo
Simulando B ooleanos no ABAP
O ABAP não contém suporte a booleanos, mas a SAP disponibi-
liza uma forma de “simular” seu uso em seu código. Por meio do 
TYPE-POOLS: abap, você consegue ter acesso ao tipo abap_bool, 
além de constantes abap_true e abap_false. Nenhuma dessas cons-
tantes e tipos são reais booleanos, são constantes do tipo C, que po-
dem ter os valores ‘X’ ou SPACE. A documentação do ABAP contém 
guidelines de como aplicar corretamente essas constantes no seu código: 
http://bit.ly/2biqMOh.
Podeparecermuitosimplescolocarsomenteumaconstanteburrade
exemplo,masémuitofácilencontrar REPORTscommaisde 20constantes
quenãoprecisavamestarali,deixandoocódigoaparentementemaisconfuso
doquedeveria.
Passeiporprojetosqueobrigavamosdesenvolvedoresacriaremcons-
tantesparatodososvaloresliteraisexistentesnoscódigos.Nessassituações
surgemsoluçõesaindamaiscontraprodutivasparaconstantes,comoo“ma-
ravilindo”C_SPACE:
CONSTANTS :
c_x TYPE c VALUE 'X' ,
c_space TYPE c VALUE ' '.
IF p_docto = c_x .
* Algo com o documento
ENDIF .
IF p_users = c_space .
* Algo com o usuário
ENDIF .
Estranho,nãoé?Eomartírionãoparaporaí.Colocaronomedacons-
tanteigualaoseuvaloréassinarumcontratode“problemaalongoprazo”
dentrodocódigo.
78

## Página 93

CasadoCódigo Capítulo6. OstabusdomundoABAP
CONSTANTS c_zmb1 TYPE CHAR4 VALUE 'ZMB1' .
Seumdiaovalor ‘ZMB1’mudarpara ‘ZMB2’,ficarámuitomaisfácil
entenderqueocódigousaa C_ZMB1emum IF,quando,naverdade,seu
valoré ‘ZMB2’(éclaroquenão).
Éexatamenteporissoqueeununcaconfioemconstantesquecontêmno-
mesparecidoscomvalores.DepoisdeumtempotrabalhandocomSAP,dá
parasacarqueuma C_2200éonúmerodeumcentroouplanta,sónãodá
paratercertezadequeoseuvalorérealmente ‘2200’.Podemosapelidar
cadaumadessasconstantesde abomináveis constantes das neves:“abominá-
veis”,porqueelasrealmentesãoabomináveis;“dasneves”,porquesoadiver-
tido.
Masenfim,quandoeuprecisousarumaconstante?
Valeobomsensoeacorretaanálisedaregradenegócio. Seexisteum
valorqueseráusadoemdiversospontosdoprograma,daquelesqueocli-
ente/funcionalnãodeveránuncamudarsemrequisitarumaalteraç ãonaes-
pecificaçãoequeimportamparaoprocessododesenvolvimento(tipodedo-
cumento,umaempresa,umnúmerodecontacontábiletc.),vocêpodecon-
siderarutilizarumaconstante.
Omelhormesmoénuncadeixarovalorcravadonoprograma,tentando
sugerirousodeumatabeladeparâmetros,comoa TVARV(acessandoatran-
sação STVARVparamanipular).Issogarantequeoclientenãoprecisarácon-
tratarumABAPersomenteparaalterarumpequenovalor,deixandoseupro-
gramaconfigurável.
Deixoregistradoque,emtodosessesanosnessaindustrialvital,esteé
otópicoquemaisrevelaasamarrasimpostaspelosprocessosjurássicosde
qualidadedecódigo,aplicadosemalgumasempresas. Essastravas,aliadas
adesenvolvedoresquepreferemexecutartrabalhoscomorobôsemvezde
ponderaremsobreoquefazem,atrapalhamconstantementeaqualidadedos
programasgeradosemprojetos.
Abaixaracabe çaparaumametodologiae/ouprocessoquandoeleclara-
mentenãofazsentidoondeestásendoaplicadoénegligenciarapossibilidade
demelhoriasnociclodedesenvolvimentodesoftwareseprojetos.Tomecui-
79

## Página 94

6.5. Paredeescreverdocumentaçõesquenãoserãolidas CasadoCódigo
dadoparanãoentrarnomodoautomático,enãodeixequeprocessosdere-
visõesarcaicose guidelinesdedesenvolvimentodatadasoneremaqualidade
doseutrabalho.
Paraterminar,éclaroqueeuconsigoimaginarumcenárionoqualalgum
processodeQAS(quality assurance,ougarantiadaqualidade)semno çãovai
obrigá-loaemburreceroseucódigo. Minhadicaé: apresenteargumentos
válidoscontraapráticaquenãofazsentido.Sevocêconseguirmostrarque
aquelacorreçãoqueestásendoimpostavaipiorarocódigo,hágrandeschan-
cesdeaprópriaequipedeQASreconsideraro guidelineburrico.
6.5 Pare de escrever documentações que não se-
rão lidas
NaáreadeTI,quasetudoseresumeaotempoquevocê,desenvolvedor,vai
gastarparafazerXatividades. Existemmilharesdetécnicasemaneirasde
mensurarquantotempovocêgastaráparafazerumadeterminadatarefa,e
todaselassãodeextremaimportânciaparaofuncionamentodomercado.
ComojádiziaograndeSuperSam,interpretadopeloatorRamónValdés(o
SeuMadruga): time is money, oh yeah.
Porém,umadascoisasqueachomaisengraçadanomundoSAPéotempo
desperdiçadocomdocumentaçõesfalhasequenuncaserãousadas,servindo
somenteparafazervolumeno“pacotãodahomologação”.Asmetodologias
dizemqueessastaisdocumentaçõessãoimportantes,masapráticanosmos-
traque,seelasforemfeitasdojeitoqueamaioriadosprojetosascrias,elas
nãosãoúteisparaabsolutamentenada.Oquediabosacontececomasdocu-
mentaçõestécnicasemprojetosSAP?
AsdocumentaçõestêmmuitaimportânciaemqualquerprojetodeTI.O
problemaéqueoconceitodedocumentaçãoemváriosprojetoseempresas
queusamoSAPestácompletamenteequivocado.Horasehorassãogastasem
documentosquenãodizemabsolutamentenadasobreosprogramascriados.
Milharesdepalavrasgastasparadescreverumcódigo-fontelinhaalinha,
enemummíseroparágrafoparaexplicarosmotivosquelevaramodesen-
volvedoraescolherasoluçãotecnicamentemaiscomplexaparaaquele FORM
crucialdoprocesso.Sãodesenvolvedoresbrincandodedocumentareapro-
80

## Página 95

CasadoCódigo Capítulo6. OstabusdomundoABAP
vadoresfelizescomaexistênciademaisumitemparaajudarnahomologaç ão
doprograma.
De volta ao básico
ParaqueserveumaEF(EspecificaçãoFuncional)eumaET(Especi-
ficaçãoTécnica)?Seiqueboapartedosqueleemestelivrojádeveestar
carecadesaber,mascomooABAPZombiesempreabrigoumuitosini-
ciantesnaárea,nãocustanadaconceituarnovamenteosdoisitens:
• AEspecificaçãoFuncional (EF)éumdocumento,criadoporfun-
cionais,queexplicacomoumdeterminadoprogramaterádese
comportarnosistemaparaatenderaumanecessidadedeumusuá-
rioouumaempresa. Elecontémprincipalmenteexplicaçõesdo
pontodevistadosprocessosdenegócio. Podeounãoterexpli-
caçõesumpoucomaistécnicas(nomedetabelas,campos,nome
defunçõesetc.)–issodependedofuncionalqueasescreve.Em
outraspalavras,eladevedescreveroqueousuárioquerdeuma
formaqueoprogramadorconsigaentender(ou,pelomenos,de-
veria).
• AEspecificaçãoTécnica(ET)éumdocumento,criadopelospro-
gramadores,queprecisaexplicartecnicamentecomoosoftware
funcionadentrodosistema.ÉsuportadopelaEFecontémdescri-
çõesdecomooprogramadorcriouosoftwareparaatenderoque
aEFpediu.Normalmente,contémalistadosobjetoscriados,uma
explicaçãodecomocadaobjetofoiusadonodesenvolvimento,a
arquiteturaportrásdosoftwareedetalhesdecomocadapartedo
programafoitecnicamenteimplementada(ou,pelomenos,deve-
ria!).
AcriaçãodeETsruinssedáemcenáriosquejásetornarampadrõesna
práticaABAP.Seráquevocêjásedeparoucomalgumdeles?
81

## Página 96

6.5. Paredeescreverdocumentaçõesquenãoserãolidas CasadoCódigo
ETsde800páginasparaprogramasde500linhas
Muitasempresastêmtemplatesfechadosparaacriaçãodeespecificações
técnicas,eagrandemaioriadelaspedemdetalhesdemaissobreoprograma.
Descriçõesdetabelascampoacampo(colocandootipo,tamanho,descriç ão,
eoutrasXbilhõesdeinformações),listagemdetodosos TEXTscriadosno
programacomassuasrespectivastraduções,atributostécnicosdecadaum
dosobjetosdodesenvolvimentoemaisoutrasinformaçõesquesimplesmente
nãoprecisariamestarali.
EsseéotipodeETquetemomenortempodevida: ésóvocêmudar
adescriçãodeumcampoemqualquertabelaquevocêcriou,eelajáestará
desatualizada. Étambémaquelaquenãoexplicaquasenadasobrecomoo
programafunciona.Ouseja,seoprogramadorquecriouoprogramasairda
empresa,ooutroqueseviredebugandoatéoinfinitoealémparadescobrir
comoelefunciona.
CriaraETantesdecodificar
SeummesmoprogramadorvaicriarocódigoeaET,émuitocomum
eleprimeirocodificaresódepoisdocumentar–mesmoqueasmetodologias
adotadaspelasempresasdigamqueissoéerrado.Porém,existemcasosem
queumprogramadormaisexperientecriaaET,eumoutromenosexperi-
entequecodificacombasenodocumento.EssetipodeETtendeaficarcom
umaqualidadeumpoucomaior,porqueelaexplicatecnicamentecomoopro-
gramadevefuncionarsemchegaraumníveldedetalheabsurdoeirrelevante
paraodocumento.
Oproblemaéque,nagrandemaioriadasvezes,oABAPerJúnioracaba
fazendoalgumacoisacompletamentediferentedoqueestavanaET,simples-
menteporquenomundodaprogramaçãovocêsóvaisaberquecertascoisas
nãovãofuncionarcomoespecificadasquandovocê,defato,vailáetentaco-
dificar.
Esseéumcenáriomuitocomumnodiaadia.Oproblemaéqueanossa
classeépreguiçosaeninguématualizaaETapósodesenvolvimentotersido
concluído.Elajánascedesatualizada,enãodescrevetotalmentecomoopro-
gramacriadofunciona.
82

## Página 97

CasadoCódigo Capítulo6. OstabusdomundoABAP
FazerdaETumacópia“semvergonha”daSE38
Nomeiodacorreriadoprojeto,muitosABAPersabremumdocumento
novonoeditordetextos,dão CTRL + C nocódigo-fonteeum CTRL + V
naET,salvameaentregamjuntoaoprograma. Issoémaiscomumdoque
parece,acredite.EessasETspassamportodososníveisdeaprovaç ão,acredite
denovo.
CriaraDOMM–DocumentaçãoOrientadaaMimMesmo
MuitapessoasesquecemqueomontedecoisasdescritasemumaETsser-
virãocomoreferêncianofuturo.Emummundoperfeito,sevocêchegasseem
umprojetoparafazerummodificaçãofuncionalemumprogramade829.382
linhas,vocênãoteriadedebugartudoparaentendê-lo.Primeiramente,iria
leraEFparasaberqualprocessoodesenvolvimentocobre,paradepoislera
ETeentendercomoaqueleprocessofuncionalfoiimplementadopelopro-
grama.
OproblemaéquandooABAPerutilizaaETcomoumrascunho,um
documentoondeeleescrevetodasaquelascoisasmaravilhosasqueprecisa
lembrarsobreodesenvolvimento.Omaislegaléqueelecostumadeixartudo
descritodamaneiramaisdesorganizadapossível,oqueajudamuitoavidade
quemforleraquilonofuturo(sóquenão).
Existesolu ção?
Otempodestinadoàcriaçãodedocumentaçõesprecisapassaraserusado
comsabedoria(nomaiorestiloJedimesmo). NãoéporacasoqueoMani-
festoÁgil(http://www.manifestoagil.com.br/)valorizasoftwareemfuncio-
namentomaisdoquedocumentaçãoabrangente.Otristeéqueboapartedas
ETsemprojetosSAPnãoserveparanadaesóexisteporqueametodologia
obrigaodesenvolvedoracriarodocumentoparaqueoprodutopossaentrar
emprocessodehomologação.
Ninguémquestionaoobjetivorealdeadotarumametodologia,todosfa-
zemoqueeladescreveliteralmente,eseguemoudefendemaquilocomuma
fécega,semavaliarosreaisbenefíciosdetodooprocesso.Nomeiocorpora-
tivo,issoestámuitolongedemudaremlargaescala.
83

## Página 98

6.5. Paredeescreverdocumentaçõesquenãoserãolidas CasadoCódigo
Particularmente,gostodaideiadeterumdocumentoqueexpliqueopro-
grama,masodeioamaneiracomoelesnormalmentesãogerados.“Ué,então
comovocêachaquepodemosgerardocumentaçõesquesejammaisúteis?”,
vocêmepergunta,jovem(ouvelho)Padawan.Eeuexplico:temosdeserre-
alistasquandotratamosdemelhoriasemdocumentações.Nãodáparajogar
tudoparaoaltoedizerqueETsnãoprestam,quedesenvolvimentoágilélegal
equevamoscriarnossasprópriasdocumentaçõesdojeitoqueagentequiser.
IssosimplesmentenãovaiaconteceremprojetosSAP,nemacurto,nema
médioprazo.
Independentedeseumdiaamaioriadosprojetosutilizarámetodologias
modernasounão,precisamosmelhorarasdocumentaçõesdentrodocenário
atual.Portanto,segueaquiaminhalistadedicasdecomocriarumaETque
tragavalorparaoseudesenvolvimento,equefarãooseutemposergastocom
algumacoisaquepoderáajudaroutrosABAPersnofuturo.
1)PensenoquevocêgostariadeleremumaETalheia.
Aprimeiracoisaquecostumofazeraodocumentarépensarnascoisas
queumoutroprogramadorpodeacharinteressanteseeleleraminhaET.
Quaispontosprecisamdeumaexplicaçãomaisdetalhada?Porqueeutive
defazerumalógicamuitomaisenroladaemumpontoque,aosebasear
naEF,pareciabemmaissimples?Porqueoptamospeloparalelismoem
umprogramacomperformancecrítica? Existealgumpontoqueémais
fácildeserentendidoolhandodiretamenteocódigo?Porqueaestrutura
declassesfoicriadadaquelamaneira?Sevocêresponderalgumasdessas
perguntasemsuadocumentação,elajávalerámuitomaisdoqueamaioria
dasETscriadasporaí.
2) Semencherlingui ça:guardeparticularidadesdocódigoparaocódigo.
DiversasETscontêmdescriçõesdemaissobrepartesquesófazemsentido
parapontosespecíficosdocódigo-fonte.Aquientramcriaçõesdevariáveis
auxiliares, LOOPsbinários,usoderotinasdeconversão,métodosefun ções
paraconversõesdevalores,declaraçõesdetabelasinternasetc.Anãoser
queessespequenostrechosdecódigofaç amsentidoparaoentendimento
“geral”dasoluçãoimplementada,nãovaleapenadescrevê-losnaET.
84

## Página 99

CasadoCódigo Capítulo6. OstabusdomundoABAP
3)Lembre-se:nadadeinibiracriatividadedoprogramador.
Essefrasefoiditaporumgrandeparceiromeudeprojetoseéalgoex-
tremamenteválidoparaETscriadasantesdocódigo.Sevocêestáescre-
vendoumaETparaumcolegamenosexperiente,cuidadoparanãocair
nomesmoproblemaanterior:descreverdemaisoquedevesercriado.Se
fosseparavocêterqueresolvertudonaET,seriamaisfácilirláeescrever
ocódigodeumavez,nãoémesmo?
Pessoasmaisnovasprecisamdeestímulosparadesenvolversuacapaci-
dadedeprogramar,portanto,nadadeinibiracriatividadedosseuspupi-
los.Ah,epe çaparaeleatualizarodocumentoposteriormente,deixando
aETfácildeserentendidaporalgumoutroprogramadornofuturo.
4) CopiarecolarcódigosinteirosnaET:NÃOFAÇANUNCA!
Essaatividadeéfeitalevandoemcontaa“perdadetempoemcriardo-
cumentações”. Sinceramente,nestecaso,atéesses10minutosqueserão
gastosdando CTRL + C e CTRL + V nocódigoserãoperdidos. Não
façaissoemhipótesenenhuma.
QuandoleioumaETassim,pensoqueseucriadornãofazamínimaques-
tãodeexplicarcomooseudesenvolvimentofuncionaparaninguém(tal-
vezporquenemelemesmosaibaoqueestáfazendo).Criardocumenta-
çõesfazpartedonossopapeldentrodomundoSAP,eprecisamosfazer
essetrabalhocomresponsabilidade.
5)Façasugestõesdemudanç anostemplates.
Sevocênãotrabalhaparaumprojetoquetenhaumtemplate100%fe-
chado,podeserdegrandevaliasugerirmudan çasparadeixaraETmais
enxutaedefácilentendimentoparaoutrosprogramadores(ouatémesmo
o“você-do-futuro”).
Emprojetosqueutilizammetodologiaságeis,adocumentaç ãocostuma
serumpoucomaislivreecadaequipeadotasomentedocumentaçõesque
elesjulguemextremamentenecessárias.Sevocêconhecealguémquetra-
balhaemumaempresaqueadotaessetipodemetodologia(mesmoem
outraslinguagens),pergunteaelecomoelestrabalhameoquefazsentido
paraaquelaempresa.Vocêpodetrazeralgumasideiasparasuaequipee
85

## Página 100

6.5. Paredeescreverdocumentaçõesquenãoserãolidas CasadoCódigo
fazeraET,enfim,servirparaalgumacoisa. Ébemraroencontrarem-
presasqueimplantamprojetosSAPbaseadosemmetodologiaságeis,mas
issonãoquerdizerquevocênãopossaagregaralgunsconceitosemseus
trabalhos.
6) TentecomeçaralerETsdevezemquando.
Nós,programadores,temosohábitodesairolhandoparaocódigoan-
tesdelerqualquertipodedocumentaç ão.Écomoquandovocêcompra
umaTVnovaenemdábolaparaomanual:jásaifuç andoeaprendendo
tudosozinho.Parapequenascorre ções/modificações,fazsentidoirdireto
nocódigoealterar;porém,paramodificaçõesmaioreserestruturaçãode
programasmalucos,podeserqueoseucolegaprogramadortenhasido
solidárioetenhaescritoumaETbacana,daquelasquevãolheajudaraen-
tendercomooprogramafoiimplementado.LeressaETpodefazercom
quevocêgastemuitomenostemponasuaatividade.
AgrandemaioriadasETsporaísãodescartáveis.Faloissocomcertapro-
priedade,afinal,comovocêachaqueeuconseguimapearessemontede
padrões?FoilendoETspelosprojetosafora!Leressasdocumentaçõesé
legal,porquevocêvêcadacoisabizarraetambémencontraboassurpresas.
ÉaquiquevocêqueescreveETszoadasficacomvergonhaaosaberque
alguémumdiadeveterlidoexingadoseunomenocabe çalhododocumento!
Nemtudoestáperdido,dependedevocê!
Sevocêtiverquegastartempocomalgumaatividade,procuredartudo
desi.Nãoenxergueaatividadededocumentaçõescomoummerotrabalho
braçaleinútil,poiselapodesermuitomaisdoqueisso.Dizalendaqueeste
quevosescrevedescobriuumacertavontade“obscura”deescreverartigos
técnicosapartirdascriaçãodedocumentações.
Algumasfontesdeinspiraçãoparaentenderoquantodocumentaçõessão
projetosopensource.ExperimenteanalisarprojetospopularesdoGitHub,ou
mesmoframeworkspopularescomooRails. Asdocumentaçõescostumam
terestruturaintuitivas,sãobemcompletasefazemdetudoparaajudaros
programadoresnautilizaçãodasferramentas.Denadaadiantacriaralguma
86

## Página 101

CasadoCódigo Capítulo6. OstabusdomundoABAP
plataformaabertasupermega-animalebonitaseninguémconseguirusar,não
émesmo?
Porfim,falandodomundoSAP,minharecomendaçãoéapertaro F1em
comandosABAPsaleatóriose ler.AdocumentaçãodecomandosdoSAPé
muitodetalhadaeajudabastantesevocêestiverdispostoadedicarumtempo
noentendimentodostermosque,àprimeiravista,talveznãofaç ammuito
sentido(jáqueaescritaébemtécnica).
Avalie outros pontos de vis ta
O tema “documentações” é muito polêmico no mundo SAP. Pu-
bliquei uma versão do artigo original do ABAPZombie sobre docu-
mentações no SAP Community Network, disponível em http://
bit.ly/2bPEyt1. O post gerou uma extensa discussão nos comentários, 
com outros desenvolvedores expondo os seus pontos de vista (de forma 
um pouco mais “acalorada” em alguns momentos).
A mensagem do texto é praticamente a mesma, mas vale a pena a 
leitura de
 outros pontos de vista nos comentários. Certas pessoas acre-
ditam que um template é essencial para o documentações em projetos de 
larga escala, outras pensam que a automatização por meio de programas 
geradores de documentação é mais do que o suficiente. Porém, o senti-
mento principal daqueles que comentaram é o de que as documentações 
no mundo SAP são mesmo, em sua grande maioria, completamente des-
cartáveis.
6.6 A arte milenar de comentar códigos ABAP
Naseçãoanterior,discutimossobredocumentaçõese,emcertaspartes,sugeri
quecertasexplicaçõesdeveriamficarnoscódigoscomocomentáriosemvez
deinundaremdocumentosdetextocomexplicaçõestécnicasdetalhadas.
Sóquenaminhasandan çasporcódigosalheiosecódigosantigosDMM
(“demimmesmo”),sempreachocuriosoaquantidadedecomentáriossem
sentidoqueencontro.Comentar:seráqueémesmo semprenecessário?Vou
contarumabrevefábulasobrecomentários,paradepoisapresentaralgumas
87

## Página 102

6.6. AartemilenardecomentarcódigosABAP CasadoCódigo
ideiasparavocêaprimorarsuatécnicanestaartemilenar.Prepareseukimono
evamosàluta!
Gerandoredundânciasinúteis
Quandoeucomeceinomundodaprogramaç ão,disseram-meque“co-
mentarcódigoséumaformadeconversarcomalguémquedarámanuten ção
noseuprograma,ouatémesmocomoseueudofuturo”.Fiqueimaravilhado
comessapossibilidadedequebrarabarreiradotempoatravésdoABAPe
comeceiacomentarfreneticamentemeuscódigos,imaginandoqueaquele
montedepalavrasazuis(ousabe-seláacordoscomentáriosnoseueditor)
ajudariamalguémalgumdia.
Oproblemaéquemefalaramqueeudeveria“comentar”,masninguém
medissequaisinformaçõesexatamentedeveriatransmitirpeloscomentários.
Efoiassimquecome çaramanascercomentáriosinfames,daqueletipore-
dundanteequenãoajudaemnada:
START -OF-SELECT
*-- Validações iniciais
PERFORM valida_dados_tela_sele ção.
*-- Atualiza dados
PERFORM atualiza_tabela_casdatro .
*-- Exibe ALV na Tela
PERFORM exibe_alv_final .
*-- Análise de todas as ordens de vendas
LOOP AT ordens ASSIGNING <ordem> .
*--Verifica se o Material existe no cadastro de materiais
READ TABLE materiais WITH KEY
mantr = <ordem> -matnr
BINARY SEARCH .
ENDLOOP .
88

## Página 103

CasadoCódigo Capítulo6. OstabusdomundoABAP
Essetipodecomentáriomelembradeprovasdissertativasdaépocado
colégio,ondeutilizávamosaquelagrandetécnicaderepetiraperguntaqueo
professorfez,paraarespostaparecermaioreaparentarpossuirmaisconteúdo
(quemnunca?).
Comcomentáriosinúteiscomoesses,acreditavaqueomeucódigoestava
muitobemcomentadoequeissoajudariamuitoquemfossedarmanuten ção
nofuturo. Obviamente,comentarocódigoeraumpré-requisitodarevisão
depares,logo,quemfosserevisarmeucódigonãopoderiareclamarqueele
nãoestava“bem”comentado.
Useiessatécnicafalhapormaisde1anoemeio,atéquetivedealterar
umcódigoDMMantigo,daquelesqueeuhaviafeitonosprimeirosmesesda
minhacarreiracomoABAPer.Ocódigoeragrande,continhadiversospro-
blemasestruturaisealógicaeracomplicadaosuficienteparaeutermeesque-
cidooquediabosaquelepedaçodecódigofazia.Foialiqueeupercebique
oscomentáriosqueeuhaviafeitonãoprestavamparaabsolutamentenada!
Umpequenoexemploparamostrarotipodecomentáriosqueencontrei:
*-- Análise das Ordens
LOOP AT ordens ASSIGNING <ordem> .
*-- Busca o cliente
READ TABLE clientes WITH KEY
kunnr = <ordem> -kunnr
BINARY SEARCH .
IF sy-subrc <> 0.
*-- Continua para o próximo registro - não soma
CONTINUE .
ENDIF .
soma -vbeln = <ordem> -vbeln .
*-- Busca o Material
READ TABLE materiais WITH KEY matnr = <ordem> -matnr .
BINARY SEARCH .
*-- Efetua o cálculo
89

## Página 104

6.6. AartemilenardecomentarcódigosABAP CasadoCódigo
...
(contas e mais contas )
...
*-- Sumariza os valores
COLLECT soma INTO calculos .
...
ENDLOOP .
Essecódigoestácomentado,masnemdelongeestá bemcomentado.Para
queservemexatamenteaquelescálculos?Eporqueaquelavalidaç ãodecli-
enteexiste?Aliás,comoépossívelumaordemterumclientequenãoexiste
na“tabeladeclientes"?
Pessoas mais experientes poderiam encontrar facilmente as respostas
paraessasperguntas,sefizessemumaanálisedepurandoocódigo,ouaté
mesmolendoaEspecificaçãoTécnica/Funcional(contantoquesejambons
documentos). MaseueraumABAPerjúnior,nomeiodeumcódigode5
millinhas,comumaETquenãoexplicavaabsolutamentenada.Evoulhefa-
lar:sofrimuitoparaentenderporqueaquelasomaestavaerradanocódigo.
Seráquedavaparaeutersofridomenos,seoscomentáriosfossemumpouco
diferentes?
Comoo“eu”dopassadopoderiaterajudadoo“eudofuturo"
Todomundojáfezcomentáriosidiotasnocódigoalgumdia.Issoénor-
mal.Oquenãodevesernormalévocêcairnasíndromedorobôecontinuar
fazendocomentáriosidiotasparasempre.
Muitasvezessomosorientadosdesdeoinícioaerrar,poisaprendemos
algumascoisasdemaneiraerrada.Masasituaç ãoqueciteimefezpensarem
comomelhoraroscomentáriosdomeucódigo. Desdeentão,passeiapes-
quisarcomfrequênciaartigosqueanalisamapráticadecomentarcódigos,
oqueajudoumuitoamudarminhaformadepensar.Hámuitainformaç ão
disponívelacercadecomentários,eextraíasdicasmaissimplesdeseremim-
plementadasnoABAPnossodecadadia.
Começamosnossajornadadereflexões,jogandonolixotodasasredun-
90

## Página 105

CasadoCódigo Capítulo6. OstabusdomundoABAP
dâncias:
1)Seoseucomentárioexplicaexatamenteamesmacoisaquealguémen-
tendeaolerocomando,elenãoserveparaabsolutamenteNADA.
Essafrasejámatapraticamentetodososcomentáriosdocódigodopri-
meiroexemplodestecapítulo.Paraqueexplicaremumcomentárioque
euvouentrarnoblocoquefazvalidações,seonomedo FORMjámeindica
isso?
2) Comentáriosnãodevemexplicaroqueocódigoestáfazendo,elesde-
vemmostraromotivodeaquelalógicaexistir.
Esteconceitoéumaextensãodoprimeiro. Usandonovamenteoexem-
ploinicial,podemosdizerqueaquelecomentário“Efetuaocálculo”éum
comentáriobeminútil.Aliás,emmomentoalgumoscomentáriosexpli-
camporqueeupreciseifazeraquelasváriasoperações:somarvaloresem
funçãodabuscadomaterial,ouignorarasomadalinhacasoocliente
nãoexista.Elessódizemoóbvio,aquiloqueépossívelentenderlendoo
códigopuro,sãocomentáriosdescartáveis.
Masentãoquerdizerqueeupossodar CTRL + C, CTRL + V doreque-
rimentodaEFnocódigo?Dizumvelhoprovérbiochinêsque...
3)...osmelhorestiposdecomentáriossãoaquelesdosquaisvocênãopre-
cisa.
Umbomindicadorparaanalisarseoseucódigoestá“limpo”ebemes-
truturado,éverificarquantoscomentáriosestãoespalhadospelofonte.
Normalmente,quandovocêtevedeusarmuitoscomentáriosparacon-
seguirexplicaroqueoseucódigoestáfazendo,podeserahoracertapara
refatorar(oureescrever)aquelalógica.
Aartedecomentarestádiretamenteligadaaoutraartemuitoignorada
porprogramadores:aartemilenardenomearvariáveiseblocosdoprograma.
Comnomesmelhoresdevariáveisede FORMs/métodos/funções,oseucó-
digoficamuitomaisclaroedireto,comrelaç ãoàssuas“maléficas”intenções.
NomundoABAP,todostêmocostumedeencurtaronomedasvariáveis,
91

## Página 106

6.6. AartemilenardecomentarcódigosABAP CasadoCódigo
gerandoenormesconfusõescomoasfamosas T_AUX1, T_AUX2, T_AUX3
etc.
Nos PARAMETERSe SELECT-OPTIONS,hádesculpaparaosnomescur-
tos,poisosistemalimitaonomeem8caracteres.Norestodasdeclaraçõesé
possívelsermuitomaisflexível.Seexisteanecessidadededuplicarumava-
riável,issoquerdizerquecadaumadelasserveparaumacoisadiferente–e
issopodeserexplicadocomseusnomesdasvariáveis.
Paravocêterideiadoquantoessaquestãodemanterocódigolimpoé
importante,hálivrosinteirosdedicadosaessastécnicas,comoolivro Clean
Code: A Handbook of Agile Software Craftsmanship,deRobertC.Martin,Mi-
chaelC.FeatherseTimothyR.Ottinger.
Nele, osautoresdefendematesedequecomentáriossãonecessários
somentequandoháumafalhadoprogramadoremexpressar-seatravésdo
código-fonte.ÉumaideiabemextremadopontodevistaABAP,masperfei-
tamenteviávelemdiversassituaçõesnomundodaprogramação.
No nosso caso, quase sempre trabalhamos com desenvolvimen-
tos cheios de regras de negócios complicadas que envolvem tabe-
las/campos/funções/classes/métodos com nomes em alemão abreviados
(sefossefácil,nãoteriagraça).Basear-seemnomesdecamposdodicionário
dedadoséumaboaprática(como MATNR),masmuitodelesrequeremum
poucomaisdeexplicação(comooelementodedados BOSTA–eleexiste,é
sério!VejanatransaçãoSE11).Porcontadisso,acreditoquenósprecisamos
muitodebonscomentários.
Dequalquerforma,umadicalegalparavocêcome çaraescrevercódigos
maisautoexplicativoséaseguinte:programecomoseorecursodecomentar
códigossimplesmentenãoexistisse.
Imagineummundoondeocompiladornãoreconhecesseo *(asterisco)
ea "(aspa)comocaracteresdeiníciodecomentários. Ummundoonde
vocêprecisasecomunicarcomoutrosprogramadoreseoseueudofuturo
pormeiodocódigo.Nestemundo,atarefadecriarumprogramaficamuito
maisinteressante! Anãoserquevocêsejaumtroglodita,obrigatoriamente
vocêteráquesepreocuparfortementecomaestruturadocódigo,comos
nomesdevariáveisedetodososoutrosobjetos.
Entrarneste“mundinho”dapróximavezquevocêcomeçaraprogramar
92

## Página 107

CasadoCódigo Capítulo6. OstabusdomundoABAP
deveajudaroseucódigoaficarmuitomaisautoexplicativo. Atarefaficará
bemmaisdifícil,masaevoluçãocomoprogramadorextraídadaexperiência
serápermanente.Tentoentrarnotal“mundinho”ondecomentáriosnãoexis-
temerecorroaoscomentáriosparaexplicarpartescomplicadasdaregrade
negócio,oualgumalógicamirabolantequepreciseifazer.Oideal,paramim,
équeapessoaconsigadarmanuten çõessimplesnocódigo,semprecisarolhar
umdocumentoexterno.
Acorreriadosprojetosobriga-nosacriarlógicasmonstruosas,cheiasde
regrasmalucasecálculoscomplicados. Seenvolveremregrasdeimpostos
enormasdogoverno,acoisapodeficaraindamaisconfusa.Éporissoque
gostomuitodeexplicardeformageraloquedeterminadoblococomplexode
códigofaz,comoseeuestivessepreparandoo“debugador”antesdechegar
nalógicapesada.
Costumofazerissocomduasoutrêslinhasdecomentários,comono
exemploaseguir:
* A norma XYZ da Receita obriga que este cálculo seja
* feito com base na lista técnica completa dos materiais.
* Aqui todas as listas são explodidas e as porcentagens
* são contabilizadas no cálculo final.
Issojámeajudoumuitoquandopreciseidarmanuten çãoemprogramas
antigosqueeumesmohaviacriado.Agorafaç aumteste:experimenteabrir
ocódigodeumprogramaquevocêacaboudecriar.Quaismelhoriaspodem
serimplementadassemgrandesesfor ços?
Apalavramaisimportantequevocêprecisalevaremconsideraç ãona
horadecomentarseuscódigosé didática.Seosseuscomentáriosforemdi-
dáticosaoexplicaremostrechosmaiscomplicadosdoseucódigoABAP,você
evitaráconfusões,eajudarátodoequalquerleitorfuturo.Quevocêpossain-
corporaressasdicasparadesenvolveradidáticadecomentáriosnasuaprática
ABAPerdiária,fazendocomqueoníveldasuaarteatinjaníveisabsurdos,da-
quelesemqueBruceLeenenhumpoderiabotardefeito.
93

## Página 108

6.7. UsabilidadeemprogramasABAP CasadoCódigo
6.7 Usabilidade em programas ABAP
Existemdiversasdefiniçõesparausabilidade,dasmaissimplesatéasmais
complexas.Gostodedefini-lacomoaquelacoisainvisívelquefazcomqueo
usodosoftwaresejaprazeroso,poralgummotivoquevocênãosabeexplicar.
Aliás,vocênemvaipensarsobreoquefazvocêquerervoltareutilizaraquele
software,elesimplesmente funciona.
Visualmente,oSAPERPéumsistemaumtantoquantoantiquado.Suas
telasestãolongedeserosuprassumododesenvolvimentodeinterfaces.Issoé
natural,poistrata-sedeumsistemacomcertaidade.ASAPlan çou,aolongo
dosanos,diversasferramentascomplementaresqueseconectamaoSAPpor
meiodoABAPparabuscarasinformaçõesemostraremtelasfantásticas,
bonitasefáceisdeusar.Entretanto,oseuusoaindanãoestácompletamente
difundido(falaremosumpoucomaisdessasnovastecnologiasecomoelas
conectam-seaoABAPnocapítulo 8).
Mas,supondoquevocêéABAPerequeestádesenvolvendoprogramas
utilizandoABAPpuro,existealgumnecessidadedepensarsobreusabilidade?
Pararesponderessapergunta,vamoscome çaranalisandoumasituação
clássicadavidaABAPer:
1) OABAPerrecebeumaEspecificaçãoFuncionalparatransformaremum
programaABAP maravilindo.Muitosdedossãogastosdigitandológicas
malucasecálculoscomplexos.Depoisdeterterminado,eleexplicapara
osfuncionaiscomoutilizaronovoprograma.Ofuncionalvalidaasoluç ão
eaprovaodesenvolvimento.
2) Otimefuncionalexplicaoprogramaparaousuáriochave,quetambém
validaeaprovaodesenvolvimento.Tudosegueatéafasefinaldoprojeto.
3) Apósaentradaemprodução,quandocome çaosuporte,aparecemerros
dizendoqueosdadosdesaídanãoestãocorretos,jáqueosvaloresentra-
dosnateladesele çãonãoestãosendousadoscorretamentecomofiltros.
4) Apósumcaosmomentâneo,opessoaldoprojeto descobre em um passe
de mágicaqueamaioriadesseserrosexistemporqueosusuários nãoen-
tenderamcompletamentecomoosprogramasfuncionavam.Otimeex-
plicaparamaisusuários(alémdousuáriochave)comoelesdevemusar
94

## Página 109

CasadoCódigo Capítulo6. OstabusdomundoABAP
osprogramas,eostaisdefeitos,paraalegriadosgerenteseafins,nãosão
consideradoscomoproblemasdoprojeto.
5) Apósalgunsdiasemproduçãosemproblemas,todaaequipevaicome-
morarfelizecontenteosucessodemaisumprojetoentregue.
Nessecenário,todosenvolvidoscomoprojetovãoconsiderarqueosis-
temafoiimplantadocomsucesso.Mesmoqueotalusuárioqueestavausando
osistemadeformaerradareclamecomseuscolegassobreamáqualidade
dosnovosprogramas. Elepassasemanasreclamandoque“asequênciade
telasnãofazomenorsentido”eque“essesfiltrosparecemfiltros,masnão
filtros...quemfoiomalucoquefezdessaforma?”.Depoisdeumtempo,ele
fatalmenteparadereclamar,afinal,disseramparaelequeoproblemaeraele,
enãoosistema.
OobjetivofinaldeumprojetoSAPéprovertransações/programasquere-
solvamumproblemadonegócio,sejaparaaumentaraprodutividade,oupara
tornarpossíveisasanálisescomplexasdedadosdoambiente.Todaequipede
projetoprocuraentregarprogramasqueresolvamessesproblemasdeforma
robustaeconsistente,comperformanceadequadaesemerrosdecálculosou
regrasdenegócio.
Agoraresponda:emqualmomentoaequipedoprojetoprocurouima-
ginarcomoousuárioutilizariaessesprogramas? Qualamelhorformade
disporosdadosnatela?Quantastelassãorealmentenecessárias?Essesmi-
lharesdebotõesprecisammesmoestaragrupadosnessateladesele ção?Os
termosusadosnostextosfazemsentidoparaousuário?Asmensagensdeerro
sãoboasobastanteparaqueousuárioconsigatomarumaaç ãocorretiva?
Aqueleusuário(“ochato”,deacordocomoSr.Projeto),umdosquere-
clamaramqueoprogramaestavaerrado,certamentetinhaanseiosevontades
emrelaçãoausabilidadedosistemaquenãoforamcumpridospeloprojeto.
Sevocêsecolocassenolugardele,apostoquevocêtambémdiriaquemui-
tascoisasestãoerradas,simplesmenteporqueelasparecemerradas.Usuários
normalmentenãotêmconhecimentostécnicosdosistema,eassuaspercep-
çõespodemsercompletamentediferentesdaquelasdaequipetécnica.
Àsvezes,parecequealgumasempresasestãocriandosoftwaredetráspara
afrente,pensandoprimeironaestruturadoprogramaemodelagemdeda-
95

## Página 110

6.7. UsabilidadeemprogramasABAP CasadoCódigo
dosemvezdepensaremprimeironousuário.Doqueelerealmenteprecisa?
Comoelevaiusaraaplicação?Quemtipodedesignpodeajudá-loaganhar
tempoemsuastarefasdiárias? Comoodesigndesoftwarepodeajudara
prevenirseuserros?Essassãoquestõesque,infelizmente,(quase)nuncasão
feitasemprojetosSAP.
Oimportantenãoésóbuscaremostrarosdados.Éimportantetambém
pensarem comoosdadosserãoapresentadosparaousuário.Eleéomotivo
peloqualestamosaqui,eelesdevemreceberalgoquesejafácilesimplesde
usar.
Umdosgrandeserrosdeváriosprojetoséignorarcompletamenteaopi-
niãodousuárioquandooassuntoéusabilidade.Émuitocomumverespecifi-
caçõesdeprogramasOnline(module-pools)comcincotelas,comummonte
deinformaçõesjogadas,sóporqueorequerimentofuncionaldizqueaquelas
informaçõesprecisamestarali.Comodesenharumatelasemsabercomoo
usuáriofinalvaiusarosistemaemseudiaadia?
OABAPnãoprovêmuitasmaneirasdecriarcontrolesdetela;étudomeio
padronizado,exatamenteporcontadausabilidade. Masnãoadiantanada
existirtodaumaestruturavisualedeatalhosnosistema,seosprogramas
customizadosnãoseguiremessespadrõesdeformaqueelesfaç amsentido
paraosusuários.Umcasosimplesécolocaroatalhoparaaaç ão“voltar”de
umatelaemumatecladeatalhodiferentedo F3.Sevocêjáfezisso,euaposto
queasuaorelhajáficouvermelhaquandoumusuáriotentouapertaro F3
paravoltardurantealgumanavegaçãoenadaaconteceu.Seuprogramapode
trazertodososdadoscorretamente,masosusuáriosvãoodiá-locasoelenão
tenhasidoestruturadodeformaconsistentecomorestodosistema.
Osproblemasvãoalémdeumusuárioaborrecidoporumatalho.Pense
nasmensagensdeerro.Projetonenhumpreocupa-seemmapeareentender
oscasosondeoserrosestarãopresentes,achandoqueumsimples“Dados
inválidos”éosuficienteparaqueaaplicaçãoprevinaumproblema.
Essetipodemensagemcriaumcaosaindamaior,jáqueousuáriopreci-
sarádescobrir(sabe-selácomo)qualéo“bendito”dadoqueéinválido.Esse
tipodesituaçãopodegerarumenormeestresseparaosusuáriosdosistema:
seelenãoentendeamensagem,precisafalarcomalguémquesaiba,quepre-
cisaolharcomeleoutrosdados,queprecisaacessar76.234transações.Atéeles
96

## Página 111

CasadoCódigo Capítulo6. OstabusdomundoABAP
perceberemqueoproblemaeraumdígitoerradonaContaContábil,quanto
tempolevariaparaumABAPerfazerumaconsistênciamelhornateladese-
leçãoedizerquesomenteumdosparâmetrosestavaerrado?
Canseideverusuárioschaveindagando,duranteotesteintegrado(!),se
amensagemdeerropoderiaincluironúmerododadoinválidopara“ajudar
agente”.Imaginoquantaspessoasdeixaramdeser“ajudadas”.
Simplesaçõespodemresolverumaboapartedessesproblemas.Umade-
lasénãotera usuariofobia.Tenteseaproximardosusuários,nãopenseque
ofuncionaléoúnicoqueprecisainteragircomele. Vocêquevaidesenhar
astelas,criaroscontroles,implantaros matchcodes,agruparosparâmetros
natela,colocartextosemcolunas,traduziraaplicaç ão,mapearosatalhos,
acrescentar tooltips,escreverotextodasmensagensdeerro.
User eXperience
Afacilidadedeusodeumsoftwareeasimplicidadedoseudesign
sãofatoresconstantementelevantadoscomodeterminísticosparaque
elesejabemsucedido.Ocampoda User eXperience(UX)analisacomo
odesigndeumprodutopodeafetaraspercep ções,comportamentose
emoçõesdeumusuário,levando-oaamarouodiaraquiloqueestiver
usando. NocampodeUX,vocêconseguiráencontrarosmaisdiversos
estudossobrecomoestruturarseuproduto(ousoftware)comousuário
emmente,podendoseradiferen çaentreosucessoeafalha.
UmdosautoresmaisimportantesdaáreaéDonaldNorman,escritor
doclássicolivroThe Design of EverydayThings.Nesse,eleanalisacomoo
designpodeserusadocomoumamaneiradecomunicaç ãoentreobjeto
eusuário,provendomeiosdeaplicartécnicaseformasdepensamento
paramelhorarassuasprópriascriações.Recomendomuitosualeitura,
poisosconceitospodemserutilizadosnãosónacriaç ãodeprogramas
ABAPs,masparapraticamentequalquertipodesoftware.
Naprática,aestruturadeumprojetoSAPcostumaimpedir,pordefini-
ção,aproximidadedoABAPeredosusuários–todaaintermediaçãocostuma
serfeitasomentepelotimefuncional.Masexperimentefazeroseguinteteste
97

## Página 112

6.7. UsabilidadeemprogramasABAP CasadoCódigo
(quandonenhumgerentedeprojetoestiverolhando):pergunteparaalgum
usuárioseeletemalgumcomentáriosobreumprogramaABAPquevocêde-
senvolveu,sóque nãofaleemmomentonenhumquefoivocêquemdesen-
volveuaqueleprograma.Umfeedbackhonestocertamentevaisurpreendê-lo,
pelobemoupelomal(quetambémé“bem”sevocêaprendercomoerro).
98

## Página 113

Capítulo7
Sobreprogramaçãosemcódigos
Qualquertipodeprogramaçãoenvolveumasériedeconsideraçõesqueextra-
polamacriaçãodocódigoemsi.Denadaadiantaterdecoradotodasasvari-
açõesdoscomandosdalinguagemABAPsevocênãosoubercomoempregá-
las.
Descobrireste“como”requerumaavaliaçãodocontextodoclientepara
qualoprogramaserácriado,quaisaspessoasenvolvidasemtodoprocesso(da
concepçãoaouso)edaspossibilidadesdeexpansãodoprogramanofuturo.
Todasasatividadesquepodemserexecutadasantesmesmodeaprimeira
linhadecódigoserescrita.
Compartilhonestecapítuloumaanálisedealgumasdessasatividadespré-
código,paraquevocêpossaexercerasuafun çãodeABAPeratémesmoantes
deefetuarumloginnosistema.

## Página 114

7.1. Odilemadospoucosusuários CasadoCódigo
7.1 Odilema dos poucos usuários
Certavez,euprecisavapendurarumquadronaparededaminhacasa.Eu,que
tinhaacabadodesairdacasadosmeuspaisparamorarcomminhaesposa,
nãofaziaamínimaideiadecomoosquadrosiampararnaparede.Sim,eu
sabiaquehaviaumprego(ouparafuso)portrás,masnuncahaviaprecisado
furarependurarumporcontaprópria(ouvaidizerquevocêsequerpensava
nissoquandomoravacomseuspais?).
Enfim,pegueiafuradeiraefureiaparededecasa,emumprocessoque
descascouumpoucodesuatinta,emvoltadonovoburaco.Nãotinhapro-
blema,afinal,oquadroiriatampar. Opteiporutilizarumabuchasimples
paraprenderoparafuso,maséclaroqueabrocaquehaviausadonãotinhao
tamanhoexatodabuchaqueeuprecisavaparaprenderoparafuso.Portanto,
preciseiaumentarofurousandoa mesmabroca(nãotinhaoutra),aumen-
tandoconsideravelmenteasujeiraemminhasala.
Depoisdeumasériedetentativas,finalmenteencaixeiabuchaeconsegui
fixaroparafuso. Pendureioquadro–quenãoeramuitopesado–enunca
maispreciseialterá-lo. Elecontinuaalinaminhaparede,enuncamaisme
deutrabalho.
Supondoque,nofuturo,euqueiracolocarumquadromuitomaispesado
naparede,essagambiarraqueeufizvaifuncionar? Háalgumachancede
euterabertoofurodemaiseoquadrodespencar? Precisareifazertudode
novo,aumentandoofuroaindamaisparacolocarumabuchaeparafusos
maisadequadosparaumpesomaior?
Ah,nadadissoimporta.Euaindagostomuitodoquadroenãopretendo
tirá-lodelátãocedo.
Nessepequenoexemplo–quedemonstraquenãonascideformaalguma
paratrabalhosmanuais–,preferinãomeestressartantoaoavaliarquala
formaperfeitadecriarummecanismoresistenteparasegurarqualquertipo
dequadroqueeuvenhaacolocarnofuturo.Tudooqueeuqueriaerapen-
duraroquadroepronto.
Otempoqueeugastariagerandoasoluçãoperfeitaparaqualquerquadro
domundonãosejustificava,poiso aumentodobenefício queeuteriapor
terfeitoamegasoluçãodequadrosseriabempequenaemrelaç ãoaomeu
“furoaumentadonamarra”.
100

## Página 115

CasadoCódigo Capítulo7. Sobreprogramaçãosemcódigos
Eseeudecidissequenãoquerotrocardequadro,nãovouprecisarme
preocuparmaiscomessaparedepelorestodavida?
Diversasvezes,viprojetosentregandoprogramasABAPcomamesma
mentalidadequeeutiveaopendurarmeuquadro.Afinal,pouquíssimospro-
gramasABAPsãousadosemlargaescalanasempresas.Ouseja,nãoépreciso
sepreocuparcomtelasdesele çõesrobustas,mensagensclaraseobjetivas,e
umaarquiteturadecódigoquepermitaextensõespoucotraumáticas.
Otempoquelevariaparagerarumprogramabomnãosejustificava,já
queo aumentodobenefício queseriaadquiridonãopoderiaserresgatado
diretamentenaqueleprojeto.Entregaralgoquefunciona,paraalgumtipode
usopontual,torna-seosuficiente.
Acontecequeprogramasemempresasnãosãoiguaisaosquadrosquete-
mosnasparedesdasnossascasas.Asregrasdenegóciopodemmudaracada
novasemana,áreascorporativaspodemcrescerdanoiteparaodia,eaquele
programaqueerausadoporalguémemumasalaescurapode,subitamente,
transformar-senabaseparaumasériedeatividadesqueenvolvemmuitas
pessoas.
OdilemadepoucosusuárioséconstantementeusadonomundoSAP
comodesculpapararealizarummautrabalho. Oimediatismodaentrega
criaumsistemanoqualumtrabalhomedianoémaisdoqueosuficiente.
Infelizmente,osimpactospodemsercatastróficos.
QualquerABAPercompoucotempodeexperiênciajáprecisoudebugar
algumprogramamonstrodemilharesdelinhas(Zouumstandard)quefaz
partedeumprocessocrucialparaaempresa. Seráque,noprocessodecri-
açãodaquelecódigo,elefoifeitoparaserusadoparaumagrandeparcelade
usuários,ousomenteparaumaminoriabemespecífica?Dadaafaltadedo-
cumentação,cadanovoprogramadorprecisavacriarofamoso“puxadinho”
nocódigo,criandoumainfinitacolchaderetalhoslógicosininteligível?
Pormaisbizarroquesejaorequerimento,implantá-loemumprograma
monstruosoésempremaisdifícil.Aocontráriodasabedoriapopular,gerar
umasoluçãomelhornemsemprelevarámaistempo.
Ocaminhomaisfácilcostumaserocaminhobraçal,ouseja,vocêresolve
muitosproblemasescrevendomuitocódigo,semponderarqualamelhores-
tratégiadeimplementação. Ocaminhomaisinteligente costumaprecisar
101

## Página 116

7.2. Duvidedocaminhomais“fácil” CasadoCódigo
demenoscódigo,vocêpassarámaistempopensandoemvezdeescrevendo
ABAP.
Bom,apostoquevocênãoquercorreroriscodeplantarumasementede
monstrengonoseucódigo,direcionando-osomenteapoucosusuários.Para
reduziraschances,éprecisopensaremalgumascoisasantesmesmodeabrir
oeditorABAPeescreverosprimeiroscomandos.
7.2 Duvide do caminho mais “fácil”
Quandoumanovaespecificaçãofuncionalapareceemseue-mail,oquevocê
faz? Portrásdessesdocumentosexistemprazos,expectativas,estimativas,
dinheiroepressão.Énaturalqueaprimeirareaç ãosejaabri-laeiniciarime-
diatamenteacriaçãodoprograma,parapoderselivrarrapidamentedoge-
rentequenãoparadeperguntar“qualéostatus?”.Aschancesdeumcomeço
precocesãoaindamaioresseexistiralgum“direcionamento”técniconaEs-
pecificaçãoFuncional,definidosabe-seláporquem.
Algumaspáginasatrás,nocapítulo5,refletimossetodoABAPeréreal-
menteumconsultor. Oproblemaaquiébemparecido:aestruturaclássica
dosprojetosSAPcontribuiparaquevocênãosejaenvolvidonoprocessode
arquiteturadosistema,portanto,seuúnicoinputsobreoprogramaasercri-
adoéenviadopelofuncionalatravésdaEF.
EssaEFmuitasvezescontémasfamosas“sugestõesdeimplementaç ão
técnica”,umapseudoarquiteturadocódigoquenãofoicriadapornenhum
programador. QuemcriaaEFéumfuncional,alguémque“deve”possuir
bonsconhecimentosdasáreasdenegóciodaempresaesabecomotraduzi-
losparaprocessosdentrodoSAPERP.Processos,não códigos.
AEFpodeconterinúmerosdetalhesdonegócioaserautomatizado,maso
funcionalnãotemaobrigaçãodepossuirgrandesconhecimentossobrecomo
umdeterminadoprogramadevesercriado.Elenãosabequalamelhorestra-
tégiadeimplantação,qualomelhortipodeobjetoasercriado,qualamelhor
tecnologiapararesolveroproblema,ouqualtécnicadeprogramaç ãoserá
empregada.
DecidirissotudoéresponsabilidadedoABAPer. Claroque,naprática,
algunsfuncionaispodematéfacilitarotrabalhotécnicoporteremalgumtipo
102

## Página 117

CasadoCódigo Capítulo7. Sobreprogramaçãosemcódigos
deconhecimentorelacionado(sejaporcontadaexperiência,ouporcargos
anteriores),mas,mesmoassim,qualquerdiretriztécnicacomoEFserveso-
mentecomoumasugestão,enãocomoverdadeabsoluta.
Ocaminhofácildeusarumasugestãodessascomobasepodeterresulta-
doscatastróficos.Omaiorproblemadessecenáriorevela-sequandooABA-
Perdecidequetomaressecaminholhedaráumpasselivreparaabster-sede
problemasfuturos.“OproblemaXnométodoYsóacontece,poisocódigo
estáigualaopedidonaEF": essetipodeempurra-empurraderesponsabi-
lidadesnuncavairesultaremalgobenéficoparaoprojeto,oprogramaeas
pessoasenvolvidas,alémderevelarumtotaldescasododesenvolvedorcom
oprogramasendocriado.
Seterenvolvimentocomasfasesdedefiniç ãodeumprojetonãoéta-
refafácilparaABAPersalocadosoutrabalhandodiretamenteparaclientes,
imagineentãoparaosquetrabalhamemumaáreamuitocomumnasconsul-
torias:afábricadesoftware.
Aideiadeumafábricaéotimizaramãodeobradodesenvolvimento,fa-
zendocomqueosABAPersquealitrabalhampossamatenderdemandasde
maisdeumcliente,semficarematreladosàduraç ãocompletadeumdeter-
minadoprojeto. Essaotimizaçãodificultaaindamaisoacessoaocontexto
doprojeto,eodesenvolveracabacriandoprogramaspararesolverproblemas
queelenãosabequaissão.
Járecebimuitasdessas“sugestõestécnicas”emEFsquandotrabalheiem
fábricas,econfessoqueeratentadorapoiar-mecompletamentenasoluç ão
desenhadapelofuncionalnaEF,quandoeuestavainiciandocomABAPe
programação,emvezderefletirjuntoaalguémmaissêniorsobreumame-
lhorestratégiadeimplementação.Semumavisãocompletadoprojeto,sema
experiênciaparaprevererrosfuturosecompressãodeentregaportodosos
lados,éfácilcairnessaarmadilha.
Umaoutraarmadilhamuitocomumésaircriandocópiasemaiscópias
deprogramasZ,standardsoudeinternet,semomenorcritériodeavaliaç ão.
SejapelaEFouatravésdocliente,aparecemordenscomo“façaumcópiado
programa Z_MOSTRO_BIZARROealtere sóum FORM”.
Verificarsealgofazsentidoantesdecopiaréalgobásico;entretanto,não
forampoucasasvezesemqueencontreiconjuntosde4ou5programasdi-
103

## Página 118

7.3. Mesclandoovelhocomonovo CasadoCódigo
ferentesquenãopassamdecópiasumdosoutros,comalgumaspequenas
modificações. Emtempodedesenvolvimento,issopodeparecerbenéfico,
masnomomentoemquealgumafuncionalidadecomumparardefuncionar,
oABAPerteráquealterartodosos5programas.
Todoprogramadoré(oudeveriaser)ensinadoacriarsoluçõesreutilizá-
veis(dasquaisfalaremosaseguir). Porém,éimpressionantecomoasboas
práticassãojogadasnolixoemambientescorporativos,emproldosprazos
deentregadosprojetos.
IndependentedoníveltécnicodeumaEF,aresponsabilidadedaimple-
mentaçãoserásempredodesenvolvedor.Pularafaseessencial,queéplanejar
earquitetaraimplementaçãodosoftware,certamenteresultaráemfalhas.
Umaboaalternativaéquestionarofuncional,entendendocomeleosmo-
tivosqueolevaramaadicionartantosdetalhestécnicosnaEF–ainten ção
normalmenteédeajudaremvezdeatrapalhar.Seainten çãofoipositiva,um
brainstormconjuntotorna-seumaótimaalternativaparamaximizaraquali-
dadedaarquitetura.
Desconsiderouocaminhofácilechegouemumasoluç ãointeressante,
levandoemconsideraçãooprocessodescritonaEF?Entãovamoscontinuar
asanálises,poisaindanãoestamosprontosparaescrevernenhumalinhade
código.
7.3 Mesclando o velho com o novo
Jáfalamosbastantesobrearetrocompatibilidadeeseusimpactosnocapítulo
6.ÉpossívelcriarumdesenvolvimentoABAPhojeaousarmosfeaturesbem
velhasaténovidadesimplantadasnosúltimosSupportPackages,desdequeo
sistemaestejadevidamenteatualizado.Então,oqueutilizar:ovelhoABAPão
desempre,ouoABAP-hipsterdostemposmodernos?
Vamossuporquevocêprograme(outenhaaprendidoaprogramar)do
mesmojeitoqueseprogramavaABAPnosanos90,enãopretendemudar
suaformadetrabalho. Seusprogramasestãoregadosdecomandosmarca-
doscomoobsoletosnadocumentaçãooficial,aestruturaçãointernaécom-
pletamentebaseadaem FORMse CALL FUNCTIONs,eclassessãoutilizadas
somentequandoéfeitoum ALV(usandoum copy-pastedainternet,éclaro).
104

## Página 119

CasadoCódigo Capítulo7. Sobreprogramaçãosemcódigos
Apesardotrabalhoàmodaantiga,suaexperiênciacompensaafaltade
atualizaçãotécnica,jáquevocêconhecemilharesdemanhasparadriblaro
sistemaeconseguirfazeraquiloqueprecisa,dentrodeumtempocontrolado.
Apósentregue,manuten çõespontuaistendemasersimples,afinal,você
programoumaisdomesmo.Jáasmanuten çõesgrandespodemserbemcom-
plicadasseaestruturaçãodoparadigmaproceduralnãofoibemaplicada(o
quegeralmenteacontece).Entretanto,dopontodevistadecomandos,todos
terãobaseparaentenderoquefoicriado.Areutilizaç ãodecomponentesge-
ralmenteénula,oprogramafuncionaparaaquelerequerimentoespecíficoe
pronto.
Agora,imaginequevocêabsorveutodooturbilhãodeinformaçõesnovas
sobreasúltimasversõesdoABAPeestáprontoparaaplicarabsolutamente
tudo.Obviamente,seusprogramassãocriadosutilizandoABAPObjects,ge-
randoclassesapartirdediagramaselaboradosquecontemplamclaramente
osprocessosrequeridosnaEF.
Diversasnovasfeaturesdalinguagemsãoimplantadasnosseuscódigos–
daquelasquenem10%dosseusamigosABAPersconhecem–,elesprocuram
seguirdiretrizesmodernasdeprogramaç ãoeabominamo jeito procedural
de ser. Nahoradeajustá-los,aprimeirareaçãodosoutrosdesenvolvedores
seráummistodeespantoemedo.Espantoporqueseucódigopodeparecer
tersidoescritoemélficoparaalguémquenãoacompanhacomtantoafinco
atualizaçõesdalinguagememaneirasextra-SAPdetrabalhar;emedopornão
saberseumamíseraalteraçãodeumIFnaqueleprogramamegaelaborado
podedestruircompletamenteosistema.
Apesardapossibilidadedexingamentosporpartedealgunspares,oefeito
colateraldetersepreocupadoemcriarumcódigorobustoéqueareutilizaç ão
dasoluçãoparaoutrosproblemasserábemgrande.Issopossivelmentegerará
grandesotimizaçõesdetempoemfuturosprojetos.
Usartudoquehádebomemelhornomundodaprogramaç ãoedoABAP
resultaráemumprogramasuperioràabordagemdeprogramar“maisdo
mesmo”.Aconteceque,seamaioriadosABAPersqueforemdarmanuten ção
nessecódigonãoentenderemabsolutamentenadasobreosnovoscomandos,
ouestiveremdesatualizadosquantoàspráticasdeprogramaç ão,essaabor-
dagempodegerarummontedetranstornos,poistudovailevarmuitomais
105

## Página 120

7.3. Mesclandoovelhocomonovo CasadoCódigo
tempodoqueoprevistoparaserajustado/corrigido.
“Aquelequevaialterarquecorraatráseaprenda!”.Umaabordagemcomo
essaébenéficaquandotodosquefarãomanuten çãonoscódigosestiverem
dispostosaaprenderetiveremtempoparatal. Infelizmente,umasériede
fatorespodefazercomquedeterminadaequipedeumaempresadecidaer-
radicarcompletamentetudooqueénovodoseusistema,dopontodevista
deprogramação.Explicocomumasituaçãoquejáenfrenteiemmaisdeuma
empresa.
Nivelandoumsistemapelopassado
Certavez,umentusiastadamodernizaç ãodoABAPdecidiucriaruma
sériedeprogramasgeradosemumprojetoutilizandotodasasatualizações
dalinguagem. Lembre-seaquidequeABAPestánaversão7.4(quandoda
escritadestelivro),permitindoousodecomandosbemantigoscomare-
trocompatibilidade.NãoéexageroalgumdizerqueumABAP“dasantigas”
nãoconseguiriaentenderpraticamentenadadosprogramasqueoentusiasta
criou.Efoiexatamenteoqueaconteceu,deumamaneiraumpoucotrágica.
Oentusiastacriouseusprogramasmodernosdurantesuaalocaç ãoem
umprojeto,quedurouatéosuportepós-implantaçãoemprodução.Acontece
que,algunsmesesapósesseprojeto,umaalteraç ãoemoutrosprogramasque
subiuparaproduçãogerouumerroemcadeia(afinal,noSAPpraticamente
tudoéconectadodealgumaforma),exigindoqueosprogramascriadospelo
entusiastafossemalteradosparaevitarumafalhacríticaemproduç ão.
Atarefadeajustarosprogramasprecisavaserfeitacomextremarapidez,
poisoproblemaimpactavadiretamenteaentradadematéria-primanaem-
presa.Senãofossecorrigidoemquestãodehoras,haviaumriscodealinha
deproduçãoparar,resultandoemperdassignificativasdedinheiro.
Aalteraçãonãoeranadadeoutromundoeoprogramaestavaestruturado
parasuportarumajustedessetipo.TendosidocriadousandoABAPObjects,
umaalteraçãonascondiçõesparagerarumainstânciadeumadeterminada
classequeimplantavao design pattern Factory(umaconstruçãoclássica
daOrientaçãoaObjetos)seriaosuficiente.Porém,oABAPerdoclientenão
faziaamenorideiadoqueeraOO,quantomaisumdesignpattern.
Oresultadonãopoderiaseroutro:oABAPerculpoua“modernidadedo
106

## Página 121

CasadoCódigo Capítulo7. Sobreprogramaçãosemcódigos
código”pelademoradaalteração. Apósmilharesdeligaçõesdegerentese
diretoresdescabelados,encontraramalguémqueentendiadeABAPObjects
paraajustaroprograma. Entretanto,issonãofoiobastanteparaapagara
percepçãodequeocódigo“ABAPdesempre”eraocódigoquerealmenteera
bom,equeteraplicadocoisas“novasdemais”tinhasidoacausaraizdetoda
aconfusão.
Oresultado? OABAPerdoclientegerouumarestriç ãoparatodosos
futurosABAPersqueprestassemserviçonaquelaempresa: “Nãoinventem
nada,façamtodososcódigosdomesmojeitoquesempreforamfeitosdesde
1990”.Essadiretrizperduraatéhoje.
OABAPerdocliente,porserumdesenvolvedordecódigo,deveriater
empenhado-separaentenderoqueestavaescritoali,paraentãofazeraal-
teraçãonecessária.Éumtremendoabsurdoqueeletenhajogadoaculpana
modernidadedocódigo,nãoémesmo?Fazerumaafirmaç ãoaessapergunta
deformapragmáticaébemfácil,masacoisatodacomplicaseconsiderarmos
apressãodepositadaemcimadaqueleABAPernaquelecenário.
Algunsambientescorporativospodemsetornarextremamentenocivos
emsituaçõesdecaos,comoessa. Eurealmenteacreditoqueaculpafoido
ABAPerquenãosabiacompreenderocódigo,masissonãoquerdizerqueeu
nãoentendaosmotivosqueolevaramatomarumadecisãoerrada,jogando
oerroparaapráticamoderna.
Setodaessahistóriaparecemalucademais,pe çoparaquevocêfaçaum
testeepergunteaosseusamigoseconhecidosABAPersquantosdelessabem
quaisasgrandesadiçõesfeitasàlinguagemABAPemsuasúltimasversões.
OumesmoquantostiveramumaformaçãoABAPqueensinavaalgoalémda
programaçãoprocedural,oucitavaaexistênciadomundoalémdasferra-
mentasbásicasdoABAP,comooALV(SAP ListViewer–omotivodeterem
usadooAemvezdoSparaaprimeiraletradasiglaéumeternomistério).
Ograndedilemaéque,mesmoquealguémtenhacontatocomoABAP
modernodurantesuaformação,arealidadedosprojetoseclientescomseus
sistemasdesatualizadosesemferramentasdevidamenteinstaladasfor çaqueo
níveldoABAPsejasempreniveladopelopassado.Situaçõesextremas,como
clientesqueproíbemousodepráticasmodernas,sãosómaisumdossinto-
mas,enãoacausaraiz.
107

## Página 122

7.3. Mesclandoovelhocomonovo CasadoCódigo
Ostandardnãofoiconstruídoemumdia
Felizmente,muitacoisatemmudadonomundoSAPnosúltimosanos.A
empresavemfazendocampanhasenormesparaqueseusnovosprodutos(dos
quaisfalaremosnocapítulo 8)sejamcomprados,implementadoseusados
portodasuabaseinstalada.Nolongoprazo,novasfeaturesdoABAPserão
obrigatóriasparaqueumdeterminadoprojetosejasequerimplantado.
Mascomofazerparainovarhoje,aplicandooquehádenovosemmedo
decriarumcaoscorporativogeneralizado?
Minhasugestãoécriarumaescaladeinovaç ão,nomomentodedecisão
sobrequalcaminhotomaraocriarodesignearquiteturado(s)seu(s)pro-
grama(s):
•Inovaçãototalesemfrescuras: seaequipedocliente(ouempresana
qualvocêtrabalha)mantémumaculturainternadeatualizaçãocons-
tantedosseussistemasinternos,useeabusedetodasasnovidadesque
osistemapermitir,sempreocupações.
•Índicesdatendênciadefazermaisdomesmo: seaequipenãocon-
témnenhumarestrição,mascontémmembrosquedemonstramcerto
receioquantoaousodenovasferramentasecomandosdalinguagem,
aindaassimimplanteoquevocêjulgarnecessário.Porém,deixetudo
muitobemdocumentoeexpliquepessoalmenteatodosqueforemdar
manutençãosobreoquevocêfez.Dessaforma,vocêfomentadiscus-
sõessobreatualizaçõesdoABAP,futurodalinguagemedesafiosna
adequaçãodecoisasnovasemsistemasantigos.
•Restriçõesretroabsurdas: mesmoemcenáriosondeexistaumasitu-
açãoderestriçãocominovações,aindaassimapliquealgumconceito
novo–masvácomcalma. Tentarprovarqueousodeumanovabi-
bliotecadeexibiçãodetelascomoo SAPUI5atravésdoGateway(fala-
remosdeambosnocapítulo 8)éfalhaquasecerta. Algumapequena
modificaçãonocódigo–comodeclaraçãodevariáveis inline–prova-
seeficiente,eéfácildeserentendidaporqualquerABAPer.Ainser ção
depequenasatualizaçõeséumadasúnicasformasdereverterumasi-
tuaçãotãoproibitiva,eéumaatividadequeprecisaserfeitadeforma
constanteparasurtiralgumefeito.
108

## Página 123

CasadoCódigo Capítulo7. Sobreprogramaçãosemcódigos
Aliadaaessalista,crieumametapessoaldetentarimplantarumape-
quenanovafeatureacadaumdosprogramasquevocêfizer.Apostoqueapós
algumaspequenasatualizaçõesseprovaremúteis,vocêpassaráparaalgumas
maiores.
Pormaiscômodoquesejaassumirquetodosdeveriamestaratualizados
edeveriamutilizaroquehádemaismodernonalinguagem,nãodápara
ignorarofatorhumanodemovimentaçõescomoessaemumacomunidade
que,emparte,nãovêmotivoalgumparadeixardetrabalhardojeitocomo
sempretrabalhou.
Apoiar-senocomodismoquearetrocompatibilidadetrazfazcomque
ABAPersseafundemcadavezmaisnoabismodaincertezaseassuashabili-
dadescontinuarãoválidasdiantetodoonovoecossistemadeprodutosquea
SAPvemcriandonosúltimosanos.Amelhorformadecombateressetipode
incertezaéinovardeformacontínua,comumpassodecadavezedeacordo
comasdiretrizesdoclienteondeotrabalhoseráfeito.
7.4 Reutilização local ao em vez de cópia ex-
terna
QuandofalamosdesoluçõesquepodemserreutilizadasnomundoSAP,logo
sepensaemprogramasquepodemserportadosdeumclienteparaooutro,
como“aceleradores”dodesenvolvimento.OclienteXpedeumrelatóriode
vendasgenérico,quepossivelmentepoderáserutilizadonoclienteY(desde
queoprojetosejavendido).OABAP,então,copiaocódigogeradonocliente
X,afimdeusá-lonofuturocomoumacelerador,casooclienteY,WouZ
venhamatertalnecessidadenofuturo.
Essaéumapráticacorriqueira,aindamaisquandopensamosqueoSAP
ERPconsistedeinstalaçõesseparadasporclientesque,muitasvezes,perten-
cemaummesmosegmentoecertamenteprecisarãosuprirdeficiênciasse-
melhantesaoprocessostandards,comcódigosABAPcustomizados.Eventu-
almente,algunsdessesaceleradoressãomelhoradoscomotempoeacabam
virandoprodutos.Háatéempresasquesobrevivemprimariamentedacomer-
cializaçãodeprodutoscriadosusandooABAP.
Entretanto,criarumprogramaemumclienteecopiá-loparavenderem
109

## Página 124

7.4. Reutilizaçãolocalaoemvezdecópiaexterna CasadoCódigo
outroémeramenteumavisãocomercialdoprocesso.Elanãoé errada,mas
tendeaatropelarabuscapelaqualidadedecódigoemproldaqualidadedo
dinheiro.Vamosignoraressepensamentoporhora,efocarnareutilizaç ãode
códigoemumamesmainstalação/cliente.
Recapitulandooquejáexploramosanteriormente, umainstalaç ãodo
SAPERPcontémumnúmeroimensodeprogramasABAPentreguesaocli-
entepelotimedaprópriaSAP.Juntoaessesprogramasstandardestáuma
sériedefunções,classeseoutroscomponentesABAPquepodemserincor-
poradosemprogramasZ,geradospelosABAPerquecustomizamosistema.
ÉcomumqueABAPersapoiem-se somentenoscomponentesstandardsgera-
dospelaprópriaSAPpararealizartarefascomuns,como:download/upload
dearquivos,geraçãodecomponentesdetelaoumanipulaç ãodeprocessos
funcionaisdosistema.
O exemplo mais clássico é a ferramenta que gera os famosos relató-
riosALV.Hátrêsformasdeusá-laemprogramasABAP:atravésdefun-
ções,comoa REUSE_ALV_GRID_DISPLAY;atravésdaclassemaispopu-
larmenteutilizada,a CL_GUI_ALV_GRID;ouatravésdaclassemaisatual,
a CL_SALV_TABLE.
SeumABAPerprecisarcriarumALVemumcliente,normalmenteele
irádiretamenteaumadessasclasses,mesmoquealgumoutroABAPertenha
criadoalgomágicoemaisviávelparaaquelecaso,naquelamesmainstalaç ão.
Explico.
ImaginequeumABAPerfoiatéumclienteeprecisoufazerumprojeto
paraimplantarcincorelatóriosALV,cadaumcomumavisãodiferentedein-
formaçõesdasvendasdosprodutos.Elesabiaqueosrelatóriosseriamprati-
camenteiguais,mudandosomentealgunscálculoscomplexoseaformatação
dosdadosparaexibiçãoefiltros.Emvezdecriar5vezesamesmalógicaque
implantariaamesmasele çãoealógicadecriaç ãodoALV,preferiucriaruma
classeparatratartudoqueeracomum,abstraindoalógicafuncionalparaser
embutidaseparadamenteemcadaumdosrelatórios.
Elecrioumétodosparareceberosfiltros,usandotécnicasdeassociaç ão
dinâmica(comoo ASSIGNeasclassesdo Runtime Type Services)pararesol-
verostiposdecadavariável,emétodosparareceberparâmetrosdeexibiç ão.
Tambémimplantouumahierarquiadeclasses,deformaqueerapossívelde-
110

## Página 125

CasadoCódigo Capítulo7. Sobreprogramaçãosemcódigos
rivaraclasseprincipalquegerariaoALVparauma“classeespecíficadorela-
tórioX”.Assim,oscálculospoderiamserimplantadosreaproveitandotodoo
mecanismoprincipal.
Osusuáriosprecisavamde5programasdiferentes,porcontadepermis-
sõesdeacessoetelasdefiltrodiferentes.Logo,oABAPerfinalizoucriando
5programas,todosutilizandosuaclassegeradoradeALVspararelatóriosde
vendas.
Semesesapósacriaçãodesses5relatóriossurgissemmais2que,poral-
gummotivo,precisassemserfeitosporoutraconsultoria,comoutroABAPer,
seráqueeleusariaamesmaclasseparaotimizaroprocesso,ourecorreriaàs
implementaçõesstandardsdaSAP?
Émuitodifícilcontrolarumabasedecódigosnodetalhe,emumERPde
umaempresagigantesca.Nãoestamosfalandode100ou200códigos,masde
centenasdemilharesdecódigos-fonteemalgunscasos.Porsertantacoisa,
éimpossívelqueoABAPerquefosseimplantaros2novosrelatóriossequer
soubessedaexistênciadoscincoprimeiros.
Oclientepoderiaatécontarparaeledos5relatóriosanteriores,porémele
quasenuncasabedetalhadamentequalfoiaabordagemtécnicaqueotime
dedesenvolvimentoadotounacriaçãodosprogramas.Issoporqueastarefas
sãodelegadasparaasconsultoriasouequipesinternas,naesperan çadeque
adocumentaçãosejaoportoseguroparaentenderoquefoifeito.Conforme
vimosnocapítulo 6,amaiorpartedasdocumentaçõesABAPdegrandesem-
presasnãoexplicamabsolutamentenadasobreoscódigos.
OABAPerdanovaconsultoriaprovavelmenterecriariatudodozeropara
os2novosrelatórios. Comumprazonascostasgeralmenteapertado,nin-
guémvaificarfuçandomilharesdefontesparaconseguirencontraruma
classequefoifeitapensandona“reutilizaçãodecódigopararelatóriosdopro-
cessodevendas”.
Percebemoquãoespecíficoissosoa? Seriacomoprocurarumaagulha
emumpalheirogigante,comumprazodefinidoemhoras.Vocêpodedara
sortedeacharempoucosminutos,ougastartodootempodisponívelprocu-
randoeacabarsemnada.Aliás,semnadanão,provavelmentecomalguém
crucificandosualerdezaementregaroprogramapronto.
Quemsaimaisprejudicadodetodoesseroloéoclienteque,pornãocon-
111

## Página 126

7.4. Reutilizaçãolocalaoemvezdecópiaexterna CasadoCódigo
seguircontrolarexatamentecomoosprogramassãocriados,acabacomvá-
riasversõesdiferentesparaamesmasoluç ãoimplantadasemseusprogramas
ABAP.
Jávidesenvolvedoresdeoutrastecnologias,acostumadoscomogerenci-
amentodeaplicaçõesespecíficas,assustarem-secomessevolumedeprogra-
masABAPcriados,queaparentaserumcaosquenãofazomenorsentido.
Essesentidoexiste,masestáextremamentefragmentadocomáreasdistintas
daempresa,responsáveisporpequenaspartesdoprocesso,todosembolados
nesserepositórioimensodoqualoABAPpodetervisãodotodo.Qualquer
umseassustaria.
Comesseexemplo,ficaclaroomotivodeoABAPersemprerecorrerao
standardquandofalamosdereutilização.Mas,seporumladoissodámais
segurançadoqueocódigostandardreutilizado–queemteoriaémaisrobusto
–,poroutrocriaummodelomentaldenãocriarpensandonareutilizaç ão
localdoscomponentesdoseuprograma.
Tudoésemprerefeitodozeroe,talvez,copiadoparaumoutrocliente.É
essetipodeabordagemquefazcomqueamaioriadosprogramascriadosem
instalaçõesdoERPsejafeitapensandoemsuportarsomenteumquadropela
vidatodanaparede.
Umdosconceitosmaisbásicosdomundododesenvolvimentodesoft-
wareéoDRY–Don’t Repeat Y ourself–,cunhadoporAndyHunteDave
Thomas,nolivro The Pragmatic Programmer. Todoprogramadoraprende
desdecedoqueéprecisoorganizaroseucódigodeformaotimizada,pen-
sandoemumaestruturaquepotencializeoreúsoeeliminandoanecessidade
deescreverummesmoblocodecódigorepetidasvezes.
Masporqueesseconceitoéaplicadosomentenaescala“local”decada
umdosprogramasABAP,enãonainstalaç ãodoambientecomoumtodo?
Talvezessesejaumdosprincipaismotivosdaenormeresistênciaqueo
paradigmadaOrientaçãoaObjetosenfrentanomundoABAP:pensarque
cadapequenoprogramatrabalhadeformaseparada,semsernecessáriocriar
pensandonoreúsoporpartedosistemacomoumtodo.Algumtipodereuti-
lizaçãodecódigoprecisaexistirsomenteparaaquelepequenoprogramafeito
noprojeto,queresolveumpequenoproblemaeponto.
Omaisirônicoéque,sevocêcriaumprogramaABAPpensandonoreúso
112

## Página 127

CasadoCódigo Capítulo7. Sobreprogramaçãosemcódigos
–dopontodevistadetodoosistema–,suasoluçãoseráautomaticamente
portávelparaqualqueroutrainstalaçãoSAP,desdequeissosejafeitodeforma
legal(vejaoboxaseguirparamaisinformações).
Naquelahistóriadoscincorelatórios,elespoderiamfacilmentevirar50.
Talveznãonomesmocliente,maspensenaspossibilidadessealógicaprinci-
paldosrelatóriosfosseportadaparaoutroslugares.Comalgunsajusteseme-
lhorias,umapequenaideiacomoessaderelatóriospoderiaviraralgomaior
e,quemsabe,atémesmocriarumcaminhoparaumaempresadeprodutos.
Masmesmoquevocênãoqueiradominaromundocomprogramas
ABAP,tentepensarnautilidadedepartesdoseuprogramadopontodevista
detodoosistema.Quaispartespoderiamserreutilizadasemmaisdeumpro-
grama?Qualamelhorformadecriarcomponentestécnicosqueabstraema
lógicafuncional?Comodocumentar/nomearoscomponentesdeformaque
elessejammaisbementendidosporoutrosABAPers(eatéporvocêmesmo
nofuturo)?
Vocênãoprecisainiciarumaabordagemdestetipo,tentandoabstrairum
processofuncionaldescritoem374páginas. Comeceidentificandopadrões
empequenaslógicasecriemecanismosparaquevocênãoprecisenuncamais
fazeraquilonovamente.
113

## Página 128

7.4. Reutilizaçãolocalaoemvezdecópiaexterna CasadoCódigo
Qual a legalidade da cópia de códigos entre clientes?
Na prática, sempre existiu a cópia deliberada de programas ABAP de 
um cliente para o outro no mercado e, normalmente, ninguém se preo-
cupa com os detalhes que indicam se isso é uma prática legal ou não.
Se você é contratado por um cliente para criar um determinado có-
digo, isso indica que o código gerado é de propriedade do cliente, e não 
sua ou da empresa para a qual você trabalha. Entretanto, há algumas for-
mas de tornar esse tipo de compartilhamento legal: através dos namespa-
ces (espécie de “pacotes” criados pela SAP para parceiros e clientes, que 
dá a “benção” para que os códigos sejam portados pontualmente/como 
produtos); ou baseando-se nos termos descritos no documento SAP De-
veloper License Agreement (http://bit.ly/2byZw17) . Este último, feliz-
mente, permite que códigos e ferramentas ABAP feitos em ambientes 
Trial ABAP sejam livremente compartilhados por seus autores, por meio 
de licenças open source.
FerramentasclássicasdoABAPopensource
Algumaspessoasextrapolamopensamentodoreúsoemprojetoseele-
vamsuasideiasaoníveldereúsoportodaacomunidade.Háduasferramen-
tasABAP open sourcequeconsideroessenciaisparaodiaadia:o SAPLinke
oABAP2XLSX,amboscriadosemantidosporumafor çatarefaqueenvolve
ABAPersdosmaisdiversoscantosdomundo.
OSAPLink(http://www.saplink.org)facilitaamovimentaçãodeobjetos
ABAP(telas,fun ções,classes,programas,onlinesetudomais)entredoissis-
temasdiferentes,semanecessidadedeenvolveraequipedeBASISeotrans-
portederequests.
JáoABAP2XLSX(http://www.abap2xlsx.org/)permiteacriaçãodepla-
nilhasdoExcelextremamentecomplexasapartirdeumconjuntodeclas-
ses,simpleseintuitivo. Alémdeseremferramentasmuitoúteis,servemde
inspiraçãoparaquevocêpossaelevaraaplicaç ãodoreúsoemseuspróprios
projetos.
114

## Página 129

CasadoCódigo Capítulo7. Sobreprogramaçãosemcódigos
7.5 Acaverna de fones
Detudooquediscutimosnestecapítulo,apartequeconsideromaisdifícilnão
éaprenderamelhorformadereutilizarsoluções,testarnovastecnologiasou
fazerexperimentoscomprojetosopensource.Paramim,apartemaisdifícil
é,delonge,sairdacavernadefones.
Sevocêjáteveaoportunidadedetrabalharemprojetoemumcliente,
sabequealgunsdessesambientesnãosãolámuitosprópriosparaaartede
programar.Hámuitobarulho,muitaconversaemuitasdistrações.
OúltimoredutodosABAPersacabasendoosfonesdeouvido,quenos
levamparadentrodonosso“mundinho”.Lá,umamúsica,rádiooupodcast
ajudamasimularumadesconexãocomarealidade,aumentandonossacapa-
cidadedefocaremmontaralógicadenossascriações.Somos,enfim,capazes
defocarnossasmentesnaprogramação.
Entretanto,notequeexisteumasinergiaimensaentretodosostópicos
discutidosanteriormente:vocêsempreprecisaráfalarcomalguém,sejaofun-
cional,ousuário,ocliente,acomunidadeouoseuamigoABAPer.
Parecemaluquice,jáquetodosnósclaramentenoscomunicamos.Entre-
tanto,lembre-sedequediscutimosláatrás,nocapítulo 5,queadesconexão
entreoABAPereousuáriosimpostapelosprojetosimpedequeosABAPers
realmenteprestemconsultorianosprojetosporondepassam,ficandoreféns
dainterfacecomosfuncionais.Oquantodissoéculpaestritamentedaestru-
turaimpostapelosprojetos? EoquantoéculpadosprópriosABAPersque
ficamfechadosemseusmundinhos,esperandoquealguémmandequeele
façaalgumacoisa?
Oproblemanãoéofoneemsi,maséaideiadequeépossívelserum
programadorABAPsemseenvolverativamenteemdiscussõesedefinições.
SeoSAPERP,pordefinição,éumsistemacompletamenteintegrado,pensar
queaquelesquetrabalhamnestemundopodemsempretrabalhardeforma
fragmentadaéumerro.
Tudooquevocêfazparamelhorarcomoprogramadorprecisaserefe-
tivamentetestado. Quantomaisrápidovocêpuderconversarcomalguém
paratestarseassuasabordagensestãocertasounão,maisrápidovocêvai
melhorar.
115

## Página 130

7.5. Acavernadefones CasadoCódigo
EmvezdesomentecrucificarumfuncionalporcolocarcódigonaEF,
conversecomelesobreissoomaisrápidopossível.Discutasobreinovações
diretamentecomocliente,gerente,líderousejaláquempuderajudá-loa
implantaralgumaideianovaquevocêtiver.Consulteoutrosdesenvolvedores
parasaberseasuaabordagemtécnicafavorecealgumtipodereúso,ousevocê
esqueceualgumacoisaquepoderiasermelhorada.
Sejaporpoucosminutos,ouporalgumashoras,saiadasuacavernade
foneseexploreessasabordagens. Nemsemprevocêconseguiráimplantar
tudodeumasóvez,masnãotemproblema.Oimportanteédaroprimeiro
passo,enãocairemummarasmoeternoqueodeixaráapagadoecompoucas
possibilidadesdeevoluiraplicandotodasassuascapacidadescomoABAPer.
Consideretudoissoparadepois,finalmente,abriroeditoreprogramar.
116

## Página 131

Capítulo8
Oquevemporaí?
QuandocomeceiatrabalharcomABAP,eracomumescutarnoscorredores
deconsultoriasqueoABAPmorreriaedarialugaraoJava.Atéhojedevem
existirpessoasdesinformadasqueacreditamemtaisrumores.Podeserque
oABAPpare çadefasado,afinal,existemtantosprodutosetecnologiasnovas
queoABAPficaumpoucodistantedosholofotes.
Apesardetodososnovosportfóliosdeprodutos,éfatodequeoSAP
ERPaindaéocarro-chefedaempresaalemã.Ofocodevendasestávoltado
paranovidades,mastudorelacionadoaoABAPéoquemantevee(também)
mantémaempresafuncionandoaplenovapor.
Portanto,nãoésurpresanenhumadescobrirque,porbaixodemilhares
desiglaseconceitosnovos,oABAPquasesempreestápresentedealguma
forma. Poressemotivo,diversasevoluçõesestãosendoimplantadasnalin-
guagem,muitasdelasvisandoasimplificaç ãodaescrita,integraçãonativa

## Página 132

8.1. SAPNetweaverGateway CasadoCódigo
comprodutosnovosdaSAPesuporteatécnicasdisponíveisemlinguagens
deprogramaçãomodernas.
ParademonstrarumpoucodasoportunidadesrelacionadasaoABAPno
futuro,destaqueioenvolvimentodalinguagemcomtrêsnovosprodutosSAP
quetêmgrandeschancesdeapareceremnoseudiaadianospróximosanos.
TodosservemdebaseparaoutrassoluçõesSAPcomplementares,queinclu-
sivejápossuemumabaseconsideráveldecasosdeimplantaçãopelomundo.
IssopodeservistopelositeoficialdoHANA(http://hana.sap.com/),
carro-chefedessanovageração,noqualépossívelacessarumalistacomdi-
versoscasosdeusoemempresas“gigantes”dosmaisdiversossegmentos:
Ebay,Mercedes,Vodafone,Sandisk,Cisco,entreoutros.Sabecomoé:assim
comoainternet,essatalSAPrealmentechegouparaficar.
8.1 SAPN etweaver Gatew ay
SeexisteumacoisafrustrantenodesenvolvimentoABAPpuroéasuainca-
pacidade,comoprogramador,degerarumaexperiênciadeusuáriosatisfa-
tória. Oscontrolesdeteladisponíveisnativamenteparao SAP Gui(cliente
localparaconexãoeexibiçãodetelasdoSAPERP)sãoextremamentelimita-
dos,incapazesdecompetircomtecnologiasavan çadas,comoiOS,Android,
HTML5ederivados.
OmaiorméritodastelasdaSAPGuiatuaiséavelocidade,tantodedesen-
volvimentoquantodeuso–emrelaçãoaofluxodeusoparapreenchimento
decampos,nãoàperformancedoprogramacomoumtodo.Gerarumatela
básica(conhecidascomo Dynproou Dynamic Programs)noABAPpormeio
deumReport,com15camposdefiltrocontendoajudasdepesquisacomple-
xas,étarefadepoucosminutos.
OABAPabusadeumdicionáriodedadoscompletamenteintegradoque
facilitamuitoessatarefa,porautomaticamentedisponibilizarumasériede
funcionalidadesaocriarumlinkentreocampodatelaeumcampodeuma
tabeladobancodedados.Todaessapraticidadetemumpre ço,queéapa-
dronizaçãodastelasdosistema.
118

## Página 133

CasadoCódigo Capítulo8. Oquevemporaí?
Fig.8.1:Teladesele çãosimples,muitocomumdentrodosistema
AlémdasDynpros,algunsobjetoscomplementaressurgiramparatentar
enfrentarosproblemasdeusabilidadeelimitação,comooWebdynproeBSPs
(Business Server Pages).AmbospermitemacriaçãodetelasapartirdoABAP,
paraexibiçãoembrowsers.
NoWebdynpro,aferramentadecriaç ãodetelaswebdoABAPgerao
códigoautomaticamenteparaserexibidonobrowser;jánocasodosBSPs,
éprecisocodificartodasasinterfacesnamão. Ointeressanteéquemesmo
sendoobjetosdisponíveisdeformanativaemqualquerambienteSAPERP,
ambosnãosetornaramop çõespopulares,provavelmenteporcontadapra-
ticidadedecriaçãopresentenousodasDynpros.Ousuário,porsuavez,já
estáacostumadoscomDynpros(porcontadastransaçõesstandard),enor-
malmentenãoquestionatalescolha.
Entretanto,nãoémaisumasimplescomodidadeterdeacessarsistemas
empresariaisatravésdeinterfacessimpleseobjetivas,issoéuma necessidade.
Odesigndeaplicativosparabrowsersousistemasoperacionaistendeain-
terfacesqueajudamusuáriosacompletartarefascomsucesso,normalmente
comvisualsimples,einteligênciarobustaecomplexaporbaixodospanos.
Penseemcomovocêfaziaantigamenteparacomprarumingressodeci-
nema:vocêprecisavaarranjarumjornalcomoshoráriosedias,iratéoci-
nema,enfrentarumafilaenormeedescobrirnahoraseexistiaounãosessão
paraofilmequevocêquerver.Hoje,comumsmartphone,épossívelrealizar
todoesseprocessodequalquerlugar:desdeaavaliaç ãodadisponibilidadede
lugaresnasessãoatéacompraefetivadosingressos.Enemprecisaimprimi-
119

## Página 134

8.1. SAPNetweaverGateway CasadoCódigo
los,bastaapresentaroticketdacompranateladocelularevocêentrano
cinema.Comofazerparacriarexperiênciassemelhantesnomundodasem-
presaseseusERPs?
Umdoscaminhosseriaaconversãototaldastelasatuaisparatelasmais
modernas. Masimagineoesfor çonecessárioparaadaptartodaselas(stan-
dardsecustomizadas). Oesfor çoparaalgoassimseriacompletamentein-
sano,jáqueagrandemaioriadastransaçõesqueosusuáriosutilizamestá
criadanasvelhasDynpros.Provavelmente,quandootrabalhoestivessecon-
cluído(seéqueépossívelterminá-lo),as“novas”telasjáestariamdefasadas,
dadaaquantidademonstruosadetemponecessárioparafazertaladaptaç ão.
Nãoseriamaisfácilproveralgummeiodeaplicaçõesexternasacessarem
osdadosdoERP,deumaformaconsistenteegerenciável,desenvolvendoa
User Interface(UI)emoutrastecnologias? ASAPpermitequeumcliente
possaconsumirdadosdoERPapartirdequalquertipodeaplicaç ão,criando
umaUIespecíficanatecnologiaquebementender. Algoassimentregaria
aresponsabilidadedacriaçãodosfluxosdastelasparasistemasexternosao
SAP,removendoanecessidadedousodeDynpros,Webdynpros,BSPsetoda
essavelharia.Éexatamenteparatrataressetipodecenárioquefoicriadoo
SAPNetweaverGateway,um Add-on(espéciedeplugin)paraoSAPERP.
Consuma-me,dizoOData
AtravésdoGateway,desenvolvedoresABAPpodemmodelarumserviço
OData(Open Data Protocol)paraserconsumidoporalgumafonteexterna.
Essafonteexternapodeserabsolutamente qualquersistemaoutecnologia
queconsigaconsumirumserviçoOData,sejaeleumaplicativoweb,mobile,
desktopouumamáquinadecafé. Nãoéumaferramentaexatamentenova,
masvemganhandocadavezmaisnotoriedadenostemposatuais,pormotivos
queexplicareinase ção8.3,juntoaoSAPFiori.
120

## Página 135

CasadoCódigo Capítulo8. Oquevemporaí?
ProtocoloOData
OODataéumprotocoloaberto,criadopelaMicrosofteutilizado
comopadrãopeloGatewayparaqualquertipodecomunicaç ão,supor-
tandooperaçõesdecriação,leitura,dele ção,atualizaçãoeconsultas(que-
ries).Talvezissopare çaalgodeoutromundoparaoABAPeracostumado
comoALV(SAP List Viewer )desempre,masébasicamenteaformade
comunicaçãoentrefront-endeback-end.
Exemplo:umaaplicaçãowebfazumarequisiçãodeleituradeordens
devendaparaumserviçoOData,criadopeloGateway,queacabaresul-
tandonachamadadeummétodoABAPnoqualéfeitoo SELECTna
tabela VBAK.Osdadossãoretornadosporumparâmetrodométodo
quecainalógicadoserviçoOData,que,porsuavez,entregaosdadosde
voltaaoaplicativowebparaseremexibidos.
CasovocêqueiraaprendercommaisdetalhessobreserviçosOData,
oprópriositedoprotocoloéumbominício: http://www.odata.org/.
Não é preciso estar na última versão do ERP para poder usufruir do 
Gateway, a instalação é suportada desde a versão 7.0  do SAP Netweaver. 
Para saber quais componentes estão liberados para cada versão (a lista é 
muito extensa), recomendo o site de pré-requisitos do Gateway (http://
bit.ly/2bRpVGu) , que é constantemente atualizado quanto ao suporte do 
Add-on, nas diversas versões do SAP ERP. Após sua instalação, os ABAPers 
terão acesso a um dashboard (transação SEGW), em que é possível modelar 
e monitorar os serviços OData.
121

## Página 136

8.1. SAPNetweaverGateway CasadoCódigo
Fig.8.2:DashboarddoGatewayondeosserviçossãocriados
ParaentenderofuncionamentocompletodoGatewayecomoeleseco-
municacomasaplicaçõesexternas,éprecisoestudarumpoucomaissobreo
protocoloODataearquiteturaREST,quesãoasbasesparatodatrocadeda-
dos.Porhora,comoABAPer,éimportantesaberqueexisteumaferramenta
daSAPquepermitequeumsistemaexternoconsulte,atualize,crieouapague
dadosdoERP,fazendochamadasparaessesserviçosODataqueresultaram
emchamadasdemétodos,dentrodeclassesABAP.
Nessecenário,oABAPerteráafun çãodedesenvolvedorback-end,tra-
tandoosdadosecriandológicasconsistentes,paraqueoaplicativoexterno
possaconsumirainformaçãojátrabalhada. Sevocêodeiadesenhartelase
nãoentendenadadedesenvolvimentofront-end,opapeldedesenvolvedor
back-endpodeserumcaminhoatrilharnofuturo.
122

## Página 137

CasadoCódigo Capítulo8. Oquevemporaí?
Arquitetura REST
O OData é um protocolo que se baseia na arquitetura REST (Repre-
sentational State Transfer), que provê restrições, guidelines e melhores 
práticas para a criação de um serviço web. O REST não é o protocolo em 
si, é um modelo de arquitetura que pode ou não ser usado como base.
Como a arquitetura do OData tem raízes fortes na arquitetura REST, 
é essencial entender melhor como o REST guia a implementação e a co-
municação entre as partes, para compreender completamente o funcio-
namento de um serviço OData. Já para a utilização básica do Gateway 
via ABAP, não é necessário ter conhecimentos profundos nesse tópico, já 
que há uma série de wizards e UIs que simplificam todo o processo.
Entretanto, se você quiser se aprofundar mais nos conceitos, reco-
mendo esta série de posts: http://bit.ly/1Gk4GqQ. Nela o autor guia
oABAPernacriaçãodeumaAPIbaseadaemREST,usandosomenteo
ABAPpuro,semoGatewayeserviçosOdata.Éumaboaformadeab-
sorverosconceitos,paradepoisseaprofundarnoprotocoloODataem
si.
Muitassiglas?Muitosnomesnovos?Muitaanimaçãoeconfusão?Vamos
serumpoucomaispráticoscomumpequenoexemplo.
ChegandonoABAPapatirdeumachamadaOData
Suponhaquequeremosfazerumatelamuitoloucaparabuscardadosde
ummaterialdaempresa,masnecessitamosdeinformaçõesqueestãodisponí-
veissomentedentrodoERP.Precisamosquenossaaplicaç ãowebseconecte
aoSAP,dealgumaforma,eencontreessesdados,parapodermosexibi-los
dandopiruetasvirtuais.
SupondoqueexistaumserviçoODatacomoGatewaydisponívelnoSAP
ERPparabuscademateriais,oaplicativopoderáconsumiroserviçoOData
porumaURL(geradapeloGateway),comoessa: http://www.zombie.com:
50000/sap/opu/odata/sap/zflights_srv/FlightsCollection.
Essachamadavaidispararumachamadaaométododeumaclassedo
123

## Página 138

8.2. SAPUI5eOpenUI5 CasadoCódigo
ladoABAP(tambémgeradapeloGateway).Nessemétodo,oABAPerpode
fazer SELECTs,chamar BAPIsou“marretar”tabelaspararetornarosdados
domaterial. OGatewaypegaoretornodométodo,geraum XMLcomos
dados(ouum JSON,sepreferir)–seguindoospadrõesOData–,eenvia
paraaaplicaçãoquerequisitouasinformações.
Daíparaafrente,aaplicaçãoqueconsumiuoserviçoODatapodefazer
oqueforprecisocomosdados.Essetipodeconexãonãoprecisaserneces-
sariamenteumabusca:podeserumaaç ãodedele ção,criaçãooualteração.
TodaessaestruturadeURLs,métodosedisponibilizaçãodoODataége-
radaautomaticamenteapartirdodashboarddoGateway,ondeépossívelmo-
delarosserviços,egerartodososobjetosABAPedeconfiguraç ãonecessá-
rios.
Podemosafirmar,portanto,queoGatewayfazaconexãoentredoisapli-
cativosousistemasdiferentes.Esseconceitobásicoacabaconfundindoouso
doAdd-oncomoutroprodutodaSAP:oPI(Process Integration), middleware
paragerenciamentodeinterfaces.
Porém,todasasfeaturesdoGatewayfocamemproverosdadosdoERPde
formaquepossamserconsumidose/oumanipuladosporaplicaç ãoexternas
queenvolvam ações dousuário.JáoPItemumaabrangênciamuitomaior,
atuandocomoumpontoúnicoparaintegraçõesdequalquernatureza,entre
oSAPesistemasexternos.Apesardepareceremsimilares,oposicionamento
decadaferramentaébemdiferentedentrodoecossistema.
EssaideiadetransformaroERPcomoumplataformacapazdeexpor
dadosdeforma“consistenteparaoconsumo”estádiretamenteamarradacom
umnovoprodutodoSAP,focadoemtelas.Vamosaele.
8.2 SAPUI5 eOpenUI5
ComoGatewayprovendoumaforma“padronizada”e“aberta”paraocon-
sumodedadosdoERP,énaturalqueaSAPtenhacriadoasuaprópriabibli-
otecaparacriaçãodetelas,chamada SAPUI5.Elapossuiumasériedecom-
ponentesquefacilitamodesenvolvimentodeaplicaçõesweb,abusandode
HTML5,CSS3eJavaScript.
124

## Página 139

CasadoCódigo Capítulo8. Oquevemporaí?
Fig.8.3:ExemplodeumaplicativofeitocomUI5
Asvantagensdousodeumabibliotecacomoessaéquediversosproble-
masqueumdesenvolvedorfront-endenfrentajáforamsanados,sendoum
dosmaiscomplexososuporteadiferentestamanhosdetelae devices(por
exemplo,browsersdecomputador,tabletoucelulares). Umadasprincipais
featuresdoSAPUI5sãoseuscontrolesqueforamcriadospensandonodesign
responsivo.
Usandocorretamenteoscontrolesdisponíveis,éfácilcriartelascomsu-
porteadiferentestamanhosdetela,semprecisarpreocupar-secomasmi-
lharesadaptaçõesdeCSSouJavaScriptqueseriamnecessárias.Abiblioteca
resolvetudosozinha.
ÉimportantedestacaraquiqueaSAPnãoé,nemdelonge,aprimeiraa
criarumabibliotecadessetipo. Háalternativasmuitomaispopularesentre
desenvolvedoresweb,comooJQuery,Zepto.jseKendoUI,quejásãoapli-
125

## Página 140

8.3. SAPFiori CasadoCódigo
cadasnomercadoháanos. Agrandediferen çaéqueoSAPUI5éaescolha
nativadaSAPparausaremseusprópriosprodutos,oquenaturalmentevai
escalarparatodooecossistema.
OusodoSAPUI5estárestritoaosclientesquecontêmalgumtipodeli-
cençadeprodutoSAP,masissonãoquerdizerqueoseuusoprecisarestar
obrigatoriamenterelacionadocomumcomponenteSAP.OSAPUI5éreal-
menteumabibliotecavoltadaaodesenvolvimentoweb,comcapacidadede
gerartelasemqualquertipodeaplicaçãoweb.Adiferen çaéqueoseucódigo
edesenvolvimentosãoproprietários.
Vocêjádeveestarpensando: “Puxa,maisumavezosdesenvolvedores
domundoSAPestãototalmenteamarradosàslicen çasdosclientes...certo?”
Nãoexatamente. ExisteumaalternativaaoSAPUI5,chamada OpenUI5. A
bibliotecaépraticamenteamesma, porémoOpenUI5étotalmenteopen
source.
Suacriaçãoocorreudevidoaumapequenapressãodacomunidade,que
nãoviasentidoemmanterumabibliotecacomtantaempregabilidadeatre-
ladaaosclientesquepossuemlicen çasSAP.Felizmente,aSAPresolveuabrir
ocódigo,criandouma branchespecíficaparaomundoopensource.Nami-
nhaopinião,essemovimentofoialgomuitopositivoparaquebraressaideia
deumaempresaextremamentefechada.Entretanto,seoOpenUI5teráreal-
mentealgumarelevâncianomundoweb,sóotempodirá.
Bem,muitobonitasessastelaseessacoisatodadedesenvolvimentoweb,
opensourceedesignresponsivo. MasoqueseráqueaSAPfarácomtudo
isso?Fiquetranquilo,elajáfez.
8.3 SAPFiori
SendooGatewayumaplataformarobustacriadapelaSAPparaproverda-
dos,paraseremconsumidosexternamente,eoSAPUI5umabibliotecaque
permiteacriaçãodetelaswebresponsivas,oqueaimpediriadecriarseus
própriosaplicativosexternosparaexibirinformaçõesdoERP,deumaforma
maisatrativa?Afórmulanãopoderiasermaissimples:Gateway+SAPUI5=
SAPFiori.
ASAPmapeouquaistransaçõesstandarderammaisusadaspelosusuá-
126

## Página 141

CasadoCódigo Capítulo8. Oquevemporaí?
rios do ERP, reescreveu todas utilizando o combo SAPUI5 e Gateway, e 
disponibilizou-as dentro de um novo produto, o SAP Fiori. Essas transações 
são separadas em aplicativos dentro do pacote Fiori, podendo ser instaladas 
uma a uma como Add-ons no sistema, de acordo com a necessidade do cli-
ente. Não existe nenhum custo adicional para um cliente do ERP utilizar o 
Fiori, basta ter o Gateway instalado no sistema para que “as novas transações” 
possam ser instaladas.
As telas são visualmente agradáveis, funcionam em diferentes resolu-
ções, são otimizadas para dispositivos móveis e conseguem, finalmente, en-
tregar aos usuários do ERP a flexibilidade e  simplicidade que todos sem-
pre sonhavam. Ok, sonhar talvez seja uma palavra muito forte, mas você 
pode ter uma ideia muito boa de como o Fiori funciona no site oficial: 
http://bit.ly/29sraxv.
Ei, há um capítulo atrás, este era um livro de ABAP, não era? O que Fiori, 
UI5 e Gateway têm a ver com ABAP?
Note que eu disse que a SAP reescreveu aplicações standard, não falei 
nada sobre transações customizadas com o ABAP. Se o cliente usar uma tran-
sação standard na versão Fiori, não vai demorar muito para ele perguntar se 
é possível converter uma de suas transações Z para esse novo formato. É ai 
que entra um desenvolvedor web, para criar as telas com o SAPUI5, e você, 
ABAPer, para criar a lógica de acesso aos dados com o Gateway.
As aplicações Fiori standard também podem ser ampliadas, permitindo 
alterações e ajustes (algo que lembra de longe um user-exit, ou brecha con-
trolada para alterações). Qualquer aplicativo Fiori depende diretamente dos 
dados armazenados no ERP para funcionar, e o processamento desses dados 
irá fatalmente envolver o bom e velho ABAP. Entretanto, gradualmente 
mais e mais desenvolvedores ABAP vão passar a considerar o SAPUI5 
como uma alternativa de exibição para seus aplicativos (seja por escolha 
própria ou por requisição do cliente).
Uma coisa engraçada que já ocorre é que as empresas/consultorias come-
çaram a criar vagas para desenvolvedores “Fiori” quando, na verdade, tudo
oqueelasqueremsãodesenvolvedorescomconhecimentosemcriaç ãode
programascomoSAPUI5.Aúnicaformadeconseguirum“desenvolvedor
Fiori”éarrancandoalguémquetenhacriadoumaplicativoFiorinaSAPe
127

## Página 142

8.4. HANA,HANA,HAHA...emaisHANA CasadoCódigo
contratando-o.
Partedessaconfusãosedáporcontadotermo“Fiori-like”,usadoparades-
creveraplicativosSAPUI5queseparecemcomosaplicativosdopacoteFiori.
Enfim,sepreciseidetudoissoparaexplicartodaessamovimentaç ãodirecio-
nadaaodesenvolvimentoweb,imaginetentarconvenceralguémsemno ção
nenhumadetecnologia(comomuitosgerentes,diretoresepessoascompo-
derdedecisão)sobreessadiferen çaentreumaaplicaçãoFioriqueéfeitacom
SAPUI5eumaplicativocriadocomoSAPUI5emsi.
Masamaioremaiscomplexaestratégiadeexpansãoeconsolidaç ãoda
SAPnãoseresumeareescrevertelaseinvadiromundoweb.Elatemaver
comumnovobancodedados.
8.4 HANA,HANA,HAHA... e maisHANA
OHANAéumbancodedadosin-memory,criadopelaSAP.Umproduto
completamentenovoquevisaaumentardrasticamenteaperformancedo
acessoemanipulaçãodosdados. Eletemtotaladerênciaaosprodutosatu-
aisdaSAPeéabaseparapraticamentetudoqueaSAPestálan çandonos
últimosanos.
AntesdeexplorarmosumpoucooecossistemacriadoapartirdoHANA,
vamosentenderdoquesetrataessebancodedadoseporqueeleétãoim-
portante.
Opoderdeumbancodedadosin-memory
Otermoin-memoryindicaqueobancodadosvaiutilizaroarmazena-
mentoemmemóriadeformaprimária,diferentedasversõesdebancodeda-
dosmaisusadoshojeemdianomercadoSAP,quesebaseiamprimariamente
noarmazenamentoemdisco.AmaiorpartedasinstalaçõesdoSAPERPem
clientesestáacopladaabancosdedadosdeempresasexternas,sendomais
comunsinstalaçõescomOracleouMicrosoftSQLServer(ambospossuem
suasprópriasversõesin-memory,masasusadasembases,instaladasdoSAP
ECC,costumamserasversõesconvencionais).
Oprincipalmotivodessamudan çaéaperformance,queédrasticamente
melhoradaemaplicaçõesquelidamcombilharesderegistrostodososdias.
128

## Página 143

CasadoCódigo Capítulo8. Oquevemporaí?
SendooHANAumacriaçãodaSAP,naevoluçãodosoutrosprodutossempre
existiráalgumtipodeintegraçãonativacomessenovobancodedados.
Antesdefalarmosdeintegraç ão, háumamudançadearquiteturado
HANAqueésimplesdeserexplicadaeajudabastanteaentendercomoalgu-
masmudanças“porbaixodospanos”beneficiamasaplicações.Essamudança
éoarmazenamentodosdadosdetabelasemcolunaemvezdoarmazena-
mentoemlinhas.
Paraentendermelhoresteconceito,vamosanalisarinicialmenteumata-
belaquearmazenaseusdadosemlinhas:
Fig.8.4:Exemplodearmazenamentoemlinhas
SepegássemososmesmodadosemigrássemosparaoHANA,asinforma-
çõesseriamorganizadasemcolunasnasnovastabelas,deformaquenenhum
dadofossearmazenadodeformaduplicada:
Fig.8.5:Exemplodearmazenamentoemcolunas
Essapequenamudan çadearquiteturaescalaumasériedevantagenspara
oHANA:
• Oespaçousadoéotimizado,poisnãoexisteinformaçãoduplicadaem
umamesmacoluna.Emprodução,umatabeladeinformaçõescontá-
beis–comoa BSEG–podeterfacilmentemaisde300(!) colunase
129

## Página 144

8.4. HANA,HANA,HAHA...emaisHANA CasadoCódigo
dezenasdemilhõesderegistros. Imagineacompressãoparaumata-
beladessetamanho?
• Nãoexisteanecessidadedeíndicessecundários. Cadacolunajáfica
organizadacomumaespéciede SORTnosvaloresarmazenados.Isso
querdizerqueacessosaquaisquercolunasserãoperformáticos.
• Operaçõesanalíticasserãoextremamentemaisrápidas.UmSELECT
SUM,porexemplo,teráumaperformancemuitomelhoremcompa-
raçãoaosbancosdedadosconvencionais,principalmenteemtabelas
gigantescas.
Essaideiadearmazenamentoemcolunaspodeparecerestranhaetalvez
vocêestejaseperguntando:“SeoHANAvaiarmazenarasinformaçõespor
colunas,comoelefazparamontarumalinha?”Internamente,cadaumadas
tabelascontémumatabelaauxiliarcomosíndicesdecadacolunaqueformam
aslinhas.Paraoexemploanterior,atabeladeíndicesficariaassim:
Fig.8.6:Tabeladeíndicesquepermitemontaraslinhasdoexemploanterior
Éclaroqueexisteumcustopara“recriar”umalinhaapartirdessatabela
deíndices,masesseformatodetabelasemcolunasbeneficiaoperaçõescom
grandesquantidadesdedados. QualquerguidelinedeperformanceABAP
pré-HANAdiráqueémuitomelhorbuscartudooquevocêforprecisardo
bancodedadoscomumoumais
SELECTs,etrabalharoscálculosnamemó-
riainternadoprograma.
ComoHANA,ocenáriomuda,poisémaisperformáticodelegaroscál-
culoseagregaçõescomplexasparaobancoetrazerainformaç ãojátraba-
lhadaparaoprograma,sobrandosomenteotrabalhodeexibiç ão. ASAP
130

## Página 145

CasadoCódigo Capítulo8. Oquevemporaí?
usamuitootermo code-to-dataparaexemplificaressaideiaquevemcomo
HANA:cálculoscomplexospodemserfeitosdiretamentenasqueriesexecu-
tadasnobancoemvezdeseremfeitosnosprogramas.
Essaarquiteturaimpactaaindaadistribuiç ãodainformaçãodentrodo
SAPERP.Considereasfamosas“tabelasespelho”,quenadamaissãodoquea
duplicaçãodeumatabelacomumachaveprimáriadiferente.Anecessidade
deduplicardadossedáporcontadotamanhoenormedatabelaprincipal,
queinviabilizaoperaçõescomplexasporcontadamáperformancedeacesso.
Comastabelasespelho,osistemareduzasinformaçõeseasdeixaorganizadas
por“visões”diferentesdenegócio(naprática,astabelasprincipaiscostumam
tertantosregistrosqueasespelhostambémacabamvirandotabelas“mons-
trinhas”).
UmdoscasosmaisconhecidosentreABAPerséocombodetabelas
BSEG, BSIK, BSAK, BSIDe BSAD,quearmazenambasicamenteamesma
informaçãocontábilemestadosdiferentesparaonegócio(documentoscom-
pensadosenãocompensados,porclienteoufornecedores).NoHANA,essa
complexidadetodaacaba,poisjuntandoacompressãocomaperformance
deacessoagrandesmassasdedados,ascincotabelastornam-seuma. Isso
permitearealizaçãodequalqueranálisenecessária,comaltaperformance.
LevandoemconsideraçãosomenteapráticaABAPer,oHANAexigeque
aformadepensarnotratamentodedadosemumprogramasejacompleta-
mentediferente.SeumambientemigrarparaoHANA,masmanterosseus
códigospriorizandoaaplicaçãodecálculoseagregaçõesemprogramas–em
vezdedelegaressaatividadeparaobanco–,oganhodeperformanceserá
irrisórioeoHANAserásubutilizado.
ASAPprovêumasériedefacilidadesparamitigaressasdificuldadesem
umamigração,entretanto,essaéumamudan çadepensamentoquedemorará
paraserincorporadaemlargaescalapelosABAPers.Acoisatodaficaainda
maisdemoradaquandoconsiderarmosquefazeramigraç ãodebancodeda-
doséumatarefaextremamentecomplexaemgrandesempresas,envolvendo
diversasáreaseprofissionais.
Tudoissoqueacabeideescrevervaidemorarmuitoparaveraluzdodia,
certo?Errado,pelosimplesfatodeoHANA nãoprecisardoSAPERPpara
existircomoproduto.
131

## Página 146

8.4. HANA,HANA,HAHA...emaisHANA CasadoCódigo
Ecossistema
OHANApodeternascidocomoumbancodedados,mashojeapalavra
HANArepresentamuitomaisdoqueisso. EmvezdesertratadopelaSAP
“somente”comoumbancodedadosin-memory,eleétratadocomoumapla-
taformain-memory.
AtravésdoSAP HANA Extended Application Services(XS),umdesenvol-
vedorconseguecriareexecutarapartedoservidordeumaaplicaç ão(com
JavaScript),delegandoaatividadedeexibiçãoparaoutrastecnologias.
AssimcomooGateway,oXSconsegueproverumserviçoODataapartir
doHANA,paraserconsumidoportecnologiasfront-end.Issoquerdizerque
épossívelfazerumaplicativousandooSAPUI5,econectá-lodiretamenteao
HANA,semanecessidadede“passar”peloABAP.IssonãoserestringeaoSA-
PUI5ouOpenUI5,masaqualquertipodebiblioteca,frameworkoulingua-
gemqueconsigausaroprotocoloODataparacomunicaç ãocomoback-end.
ÉpossíveltambémusaroHANAnanuvem,pormeioda HANA Cloud
Platform(HCP).Umdesenvolvedorpodecriarumambiente trial freeusando
umsistemacomoo Amazon Web Services (AWS)ecriarseuaplicativona
plataforma,paraposteriormenteservendidoatravésdo HANA App Center
(http://www.sapappcenter.com/).
ÉinteressanteverqueháalgumasstartupsofertandoaplicativosHANA
noAppCenter.ExisteumainiciativadaSAPparaexpandirousodoHANA
por startups, por meio do programaStartup Focus (http://startupfocus.
saphana.com/).
TodaaexpansãodoHANAéalgocompletamentediferentedoqueaSAP
feznosúltimos30anos,sendoatéumpoucodifícildeserentendidapelos
maisexperientesdaárea,dadaaavalanchedeinformaçõesexistentessobre
otema. NoBrasil,aindanãoháumapenetraç ãoimensadoHANAcomo
bancodedadosouplataformanasempresas,masaospoucosissoestámu-
dando,principalmenteporcontadeumprodutochamado T ax Development
Framework(TDF).
OTDFéumaplataformaparadesenvolverprogramasquegeramrelató-
riosdeobrigaçõesfiscais(comoosSPEDs)feitaemHANA.Emvezdegerar
osrelatóriossomenteporprogramasABAP,aempresainstalaoTDF,migra
osdadosparaoHANAegeraosrelatóriosdiretamentedelá,comdashboards
132

## Página 147

CasadoCódigo Capítulo8. Oquevemporaí?
criadosporparceirasdaSAP(quepodemserfeitosemABAP,ouemoutras
tecnologias).
NessahistóriadeusaroHANAcomoplataformaeexpandirparadiver-
sosoutrosprodutos,comoficaoSAPERP?Láatrás,nocapítulo 2,expliquei
rapidamentequeoSAPERP,noqualamaioriadasABAPerstrabalhamhoje
emdia,éumaevoluçãodoSAPR/3,comsuaarquiteturaem3camadas.
ClaramenteaSAPestápautandoofuturonoHANA,portanto,énatural
queoERPtambémmigrasseaospoucosparaaplataforma.Emfevereirode
2015,aSAPanunciouopróximopassodoseumaiorproduto,oSAPERP,com
ochamadoS/4HANA(algocomo“SimpleforHANA”.Não,nãoéSAP,enão,
eunãoseiporquedeixaramaquelabarranonome).
Nofuturoqueaempresaalemãimagina,todososERPsdaSAPvãorodar
emcimadaplataformaHANA.Seelajátemumaaplicaç ãodesucessocom
maisde30anosdeestradaeagoratambémtemumbancodedadospromissor,
nadamaisjustoqueunirosdoisemumacoisasó.Qualquerumdenósfaria
omesmo.
8.5 A posição do ABAP no“novo mundo”
Em2007,umlivrochamado Next Generation ABAP Developmentfoilançado
peladuplaRichHeilmane ThomasJung.Aideiaportrásdesselivroeraade
demonstrarumpanoramageraldasfeaturesdoABAPque,naquelaépoca,
eramsubutilizadasemempresasepoderiamtrazerbenefíciosavidadosABA-
Pers.
Olivrotratadeassuntospertinentesparaadataemquefoilan çado,
comoBSPs,WebDynpro,Portal,Webservices,classesdepersistências,ob-
jetoscompartilhados(Shared Objects)eatémesmoABAPUnit(ferramenta
paraaplicaroTestDrivenDevelopmentnoABAP).Ouseja,todasfeatures
quecontinuamsendosubutilizadasporABAPersmundoafora.
Escrevinocapítulo 7umabrevehistóriaquedemonstracomooposicio-
namentodealgunsABAPersacabamimpedindoqueinovaçõesdalinguagem
sejam,defato,aplicadasnodiaadia.Essaposturaestáfadadaaumcaminho
detrevas,jáquecadavezmaisoABAPtendeaserumalinguagemquevai co-
existircomoutrastecnologiasdaSAP,nãosendosomenteelaaprotagonista.
133

## Página 148

8.5. AposiçãodoABAPno“novomundo” CasadoCódigo
VejamosoexemplodaintegraçãodoSAPUI5comoABAPatravésdo
Gateway. Nãoémaisumquestãodedecidirsevocêvaiusarumaclasseou
umafunçãopararesolverumproblema,ousecriarámaisumbotão,emuma
barrade STATUS-GUI,paracriarumanovaaç ão. Parasequercriaruma
tela,éprecisoteralgumconhecimentodeJavaScript,sabercomoumOData
(criadoviaGateway)funcionaeterno çõesboasdeABAPObjects,parapoder
utilizarcorretamenteasclassesgeradasparaimplementaralógicafuncional
noback-end.
Supondoqueoclientenãoliguemuitoparaaimplementaç ãodenovas
tecnologiasfront-endacurtoprazo,oumesmoqueessetipodedesenvol-
vimentofiquedividido(ABAPernoback-end,desenvolvedorwebnofront-
end),háfeaturescriadasnamaisnovaversãodoABAP(7.40)queintegram
aindamaisalinguagemaosbancosdedadomodernos,comgrandefocona
integraçãoABAPeHANA:
•ABAPManagedDatabaseProcedures: comanovaversão, épos-
sívelcriar proceduresdiretamentededentrodoABAP,pormeiode
ummétododeumaclasse. Basicamente,ésóadicionarumaexten-
sãonachamadadométodoeproporcionarmaisalgumasconfigu-
rações,porexemplo, METHOD xxxxx BY DATABASE PROCEDURE
FOR HDB LANGUAGE SQLSCRIPT. Neste caso, HDB indica que o
bancodedadoséoHANA,e SQLSCRIPTéalinguagemusadanele
paracriarprocedures.Dentrodessemétodo,aprogramaçãonãoéfeita
emABAP,massimnalinguagemenviadapeloparâmetro LANGUAGE.
•ABAPCoreDataServices: aideiaportrásdoCDSépermitiracriação
descriptsquevãogerar viewsmuitomaiscomplexasdoqueaquelas
quepoderiamsercriadaspelaSE11,paraseremconsumidospormeio
deum SELECT.Essesscriptspodemserreutilizadospordiferentes
bancosdedados.
•EvoluçãodoOpenSQL: oconjuntodeinstruções,usadospelosABA-
Persparafazersele ções,chamadodeOpenSQL,evoluiparapermitir
quemaislógicassejamresolvidaspelobancodedados.Hámuitaspos-
sibilidadesnovas,comoautilizaçãodeinstruçõescomoo CASE,para
134

## Página 149

CasadoCódigo Capítulo8. Oquevemporaí?
decidirosvaloresdascolunasnatabeladeretorno,cálculosentrecolu-
nasdentrodopróprio SELECT,oumesmoaconcatenaçãodevalores
entrecolunas.
Todasessasfeaturesestãoalinhadascomoparadigma code-to-data,em
queaideiaéfazercomquemaiscódigosejaresolvidonacamadadobanco
dedadosemvezdesimplesmentebuscartodososdadoscommilharesde
SELECTsetratarajun çãodedadosdediversastabelasviaABAP.
A lista completa das novidades pode ser acessada em 
http://bit.ly/2bPEqJX
Alémdasinovaçõesquefocamnamaiorintegraçãocombancosdeda-
dos,hámuitasoutrascriadascomoobjetivodemodernizaraformacomo
alinguageméescrita,comoporexemploooperador NEWparainstanciar
umobjeto,ouasdeclarações in-linequepermitemqueum FIELD-SYMBOL
sejacriadodiretamentedentrodeum LOOP,como LOOP AT <tabela>
ASSIGNING FIELD-SYMBOL(<linha>). São melhorias que reduzirão
drasticamenteaquantidadedecódigonecessáriapararealizardeterminada
tarefa.
Umparteinteressantedessasnovidadeséquemuitasdelassóestarãodis-
poníveisparaosABAPersqueprogramaremutilizandoo ABAP Development
T ools(ADT),um plugindoEclipse(softwareparadesenvolvimento)queha-
bilitaaprogramaçãoABAPforadaSAPGui. CDSviewsouproceduresvia
ABAPsópoderãosercriadascomoEclipse,enãoestarãodisponíveispara
criaçãopelaboaevelhatransaç ãoSE80. ComoEclipsetambémdeixade
existiradependênciadeutilizaroWindowscomoplataformadedesenvolvi-
mento,jáqueelefuncionaperfeitamentenoLinuxounoMacOS.
135

## Página 150

8.5. AposiçãodoABAPno“novomundo” CasadoCódigo
Fig.8.7:OutravantagemdoEclipseéque,alémdoABAP,eletambémsuporta
desenvolvimentosemUI5enaplataformaHANA
Quebrandobarreiras
Háumnovolivroqueexploracommuitomaisdetalhestodasessasnovas
ferramentasefeatureschamado ABAP to the Future,escritoporPaulHardy.
Aideiaéparecidacomado The Next Generation ABAP:explorartudooque
jáestádisponíveleésubutilizadopelacomunidadeABAP,comcasosdeuso
eexemplosdeimplantação.
Entretanto,oquegarantequeacomunidadenãová,emsuamaioria,no-
vamenteignoraressasnovasferramentas,fazendocomquemuitasdessas
boasideiascaiamnoesquecimento?
Éimpossívelpreverofuturo,masoposicionamentodaSAPemusaro
HANAcomobasedoseunovoERPtendeaexigirqueodesenvolvedorABAP
dominemuitomaistecnologias,alémdovelho SELECTno LOOP.Odesen-
volvedorABAPprecisaráentenderquealinguagempassaacoexistircomou-
trosprodutos,edeveráabusardetodasasnovasfeaturesparapotencializar
melhoressoluçõesparaosusuários.
Amaiorbarreiraaserquebradaporprofissionaisdestaáreaéadenãose
apegaraosproblemasdiscutidosaolongodestelivro.Sãovícioseformasde
pensarcriadasaolongodotempo,queprejudicamcompletamenteumamu-
136

## Página 151

CasadoCódigo Capítulo8. Oquevemporaí?
dançadeparadigmaedaformacomooABAPerpodeencararseutrabalho.
Atrásdessabarreira,háummundocommuitasferramentasnovas,for-
masdiferentesdetrabalhoaseremexploradas,tecnologiasquepodemgerar
experiênciasfantásticaseoportunidadesdecarreira(quase)infinitas.
OABAP sempreesteveemconstanteevolução.Nãoseapegueaopassado,
masevoluacomele!
137

## Página 153

Capítulo9
ApêndiceI–AprendendoABAP
porcontaprópria
Sevocêchegouatéaquilendotodoorestodolivro,hágrandeschancesde
vocêjátrabalharcomABAP,fazendo,assim,todooconteúdodesteapêndice
desnecessário. Mas,paravocêqueleuestelivropretendendoingressarna
área,saibaqueexisteumaformadeaprenderABAPsemprecisardesembolsar
litrosdedinheiro.
Aprendersemdependerdeumcursopagooudeempresasépossível,mas
estálongedeserumaalternativafácil.
AmaiordiferençaentreaprenderRuby,Java,C# ouABAP,estánadificul-
dadedeconseguirumsistemaERPpararealizaroseuaprendizado.Semum
sistemaTrialdisponibilizadopelaSAP,ousemoacessoaumERPdealguma
empresa,vocênãoterácomocriarnemmesmoofamoso“HelloWorld”(mais

## Página 154

9.1. Aprendainglês CasadoCódigo
sobreissoaolongodoapêndice).
Essadependênciageraumasériededificuldadesquecertamentepodem
sersuperadas,masprecisamdeumacertadosedepersistênciaporpartede
quemqueraprender.
OutracoisaquecomplicaavidadosinicianteséentenderqueoABAP
écriadoemfun çãodasnecessidadesdoERP.NodiaadiaABAPer,émuito
comumpassarmoshorastentandoarquitetarlógicascomregrasdenegócio
complexasqueintegrameenvolvemmuitastabelaspreexistentesnosistema.
Porcontadisso,éprecisosecontextualizarumpoucoparaentenderonde
vocêestá“pisando”.
ABAPersespecialistascontêmumconhecimentobomdecomoosdados
transitamfuncionalmenteentreastabelasdoERP,oquefacilitamuitootra-
balho.NaprogramaçãoABAP,conhecerdiversastécnicasdeprogramaçãoe
comandosmirabolantesrealmenteajuda,masentendercomoainformaç ão
transitadentrodosistemaétãoimportantequanto.Éumdesafioconstante
paraodesenvolvedorteressetipodeconhecimento,masfazpartedadiver-
são.
Enfim,chegadehistória!Vamoscome çar?
9.1 Aprenda inglês
Esperavaalgotécnico?Seiquejáciteiissonocapítulo 1,massaibaqueestaé
realmenteadicamaisimportantedestelivroealgoquefazumafaltatremenda
nocotidiano.
AprenderinglêséprimordialparatrabalharcomABAP,SAPouqualquer
outracoisarelacionadaaomundodeTI.Parademonstrarissonaprática,adi-
antoquevocênãoconseguiráabsorvernemmetadedascoisasqueestiverem
listadasnestecapítulosenãosouberinglês. Voudeixarumpequenoaviso
nessaspartes,paravocêsaberoqueestaráperdendo.
Terdecriarumasessãosóparaissopodeparecerloucuraparaalgumas
pessoas,maspraticamentetodosquecruzaramomeucaminhoprofissionale
nãoentendeminglêsconcordamqueissojáfez muitafaltaemdiversasoca-
siões.
Eupoderiadedicarmilhõesdepalavrassobreoquantooinglêséimpor-
140

## Página 155

CasadoCódigo Capítulo9. ApêndiceI–AprendendoABAPporcontaprópria
tanteparaaprenderqualquercoisadetecnologia,masdecidiresumir:sevocê
nãoquiseraprenderinglêsdeverdade–enãosópseudoleitura–,aescolhaé
sua.Entretanto,tenha certezadequevocêseráumprofissionaldeTIlimitado.
Talvezalgumdiaexistainformaçãosuficienteemportuguês(jálançaramaté
umaversãoemPT-BRdo StackOverflow),masissonãoacontecerátãocedo.
Diariamenteencontropessoasincapazesdeacompanharosnovoslan çamen-
toseatualizarseusconhecimentosporcontadisso.
It’s up to you!
9.2 Entenda bem o que SAPERP eABAP querem
dizer
Eunãoestavabrincandoquandodissequeocontextoéextremamenteim-
portantenoaprendizadoABAP.Masacalme-se!SabeaWikipédia?Acesse-a
eminglêseprocurepelasseguintesinformações:
• SAP?Queempresaéessa?–http://en.wikipedia.org/wiki/SAP_SE
• ComofuncionaoERPdaSAP–http://en.wikipedia.org/wiki/SAP_
ERP
• OverviewdoABAP–http://en.wikipedia.org/wiki/ABAP
Hámuitoslivroseguiasnawebquetentamexplicarofuncionamentobá-
sicodoSAPERPquepodemcompletaroseuentendimento,masosartigos
daWikipédiaeminglêsmantêm-seatualizadoseservemparadarumaboa
baseaosiniciantes.Sótentenãoseperdernomardelinks,poisexistemmui-
tosprodutosSAP,eissopodegerarumacertaconfusão. Empoucotempo,
vocêentenderáque“mundoSAP”ésinônimode“mundodassiglas”.
ABAPéumalinguagemdeprogramaçãoproprietáriadaSAP,etudoque
vocêdesenvolveremABAPseráparaprodutosdaprópriaSAP.Édiferentede
linguagensabertascomoJavaouC++,quepodemserusadasparadesenvol-
verpraticamentequalquertipodesoftwarequelhedernatelha.
Écostumededesenvolvedordesoftwarequereraprenderalinguagem
semseimportarcomahistóriadacoisatoda. Noentanto,émuitofácilse
141

## Página 157

CasadoCódigo Capítulo9. ApêndiceI–AprendendoABAPporcontaprópria
está escrito).
Note também que não existe custo por parte da SAP pelo servidor ABAP 
Trial, mas existem custos relacionados ao servidor na nuvem. Ter uma instân-
cia ABAP Trial na AWS envolve espaço de armazenamento nos servidores da 
Amazon, custos relacionados ao tráfego de informações e tempo de utilização 
da máquina.
Os valores estão longe de serem abusivos (normalmente frações de dóla-
res por hora de utilização), mas é extremamente importante que você controle 
a instância manualmente. Como os valores são cobrados por hora, lembre-se 
sempre de manter a instância desligada quando não estiver usando o servidor 
para minimizar os custos.
Existem guias no portal de desenvolvedores para que você crie um alerta 
na AWS quando o valor exceder uma determinada quantia, por exemplo: 
“alerte-me quando a conta passar de 10USD/mês”. Recomendo que você ative 
esses alertas para não ter surpresas quando chegar a conta.
Além do AS Trial para o ABAP, a SAP oferta uma série de ambientes dife-
rentes que podem ser utilizados por desenvolvedores para listar as tecnologias 
SAP. Este link lista todos os ambientes disponíveis: http://bit.ly/1uHOjzF.
Se você tiver curiosidade sobre do que se tratam algum deles, há uma pa-
lestra em português feita pelo Tobias Hoffman, em um evento SAP brasileiro, 
que ajuda a entender um pouco mais sobre algumas delas: bit.ly/opcoes-trial-
para-devs.
9.4 Aprenda a programar o básico
O maior problema da galera que vai começar no mundo SAP é achar que apa-
recerá “do nada” um PDF mágico com centenas de páginas, códigos explica-
dos, respostas para todas as dúvidas e explicações com o máximo de detalhes. 
Vamos aos fatos: ABAP é uma linguagem usada para um software de uma em-
presa alemã, que é utilizado por empresas do mundo todo, em um mercado 
muito fechado. Você acha mesmo que as pessoas iriam sair explicando todos 
os detalhes, assim, de graça?
Apesar de muitas pessoas da área acreditarem que essas informações não 
são compartilhadas sem custo, a própria SAP disponibiliza um guia detalhado
143

## Página 159

CasadoCódigo Capítulo9. ApêndiceI–AprendendoABAPporcontaprópria
Casovocêqueiraaprofundarseusconhecimentosemoutrastecnologias
queenvolvemdesenvolvimentoABAP–comoUI5eHANA–,hátambémo
sitedaOpenSAP(http://open.sap.com/),queoferececursosgratuitosonline.
Ah,eestátudoeminglês.Denovo.
9.5 O maravilhoso mundo dos livros que ensi-
nam tudo e mais um pouco
Comoemqualqueroutralinguagemdeprogramaç ão, existeumagrande
quantidadedelivrosqueexplicamalinguagememABAP,algunsdelesnos
mínimosdetalhes.Temcoisasexplicadasemalgunslivrosqueatéquemcriou
oABAPnãodevesaber(sério).
ASAPtemumaeditoraprópria,aSAPPress,quepublicalivrossobre
diversostemas.Minharecomendaçãoprincipaléolivro ABAP Objects.Você
vaiaprenderaprogramardesdeobásico,utilizandoOrientaç ãoaObjetos,e
oníveldedetalhesdasexplicaçõeséextremamentealto,semserchato(para
umlivrotécnico).
Paraseaprofundarumpoucomaisemoutrasferramentasdalinguagem,
recomendooslivros Next Generation ABAP –deRichHeilmane Thomas
Jung–eABAP to the Future–dePaulHardy–,duasfontesenormesdeco-
nhecimento.
HáumamovimentaçãorecenteemtornodonovobancodedadosdaSAP
(oHANA),eexisteumlivrochamado ABAP Development for SAP HANA
–escritoporThorstenSchneider,EricWestenbergereHermannGahm–,
queexplicacomooABAPintegra-seaoHANA.Nãorecomendoestelivrode
início,mas,pelosmotivosexplicadosnocapítulo 8,éimportantesaberque
eleexiste.
Pesquisou,viuospre çoseachouumabsurdo? Essaéumareclamação
constante,jáquenãoexistepublicaçõeslocaisnoBrasileéprecisoimportar
ostítulos(dáparacomprarume-booktambém,diretonositedaSAPPress.
Pelomenosvocêeconomizanofrete).Livrosassimsãouminvestimentoani-
mal;afinal,vocêestácomprandoconhecimento,algoquemuitagentedaárea
aindatemmedodecompartilhar.ApostoqueumcursooficialnaSAP,ouex-
traoficialbrasileirosobrequalquerumdessestemas,sairiamuitomaiscaro.
145

## Página 160

9.5. Omaravilhosomundodoslivrosqueensinamtudoemaisumpouco CasadoCódigo
Ah,evocêjádeveterentendidoomantradoinglêsatéaqui,certo?
Mãosàobra!
Comoeudisseinicialmente,esteéumcaminhobemárduo.Longedeser
impossível,mascheiodenuancesquepodemfazervocêdesistirnomeiodo
processo.
Sevocêforumdosbrasileirosquenãodesistemnunca,todoconheci-
mentoadquiridopoderásermuitobemempregadonestevastomundoSAP.
Paraterminar,deixoaseguirguiaumpoucomaisdetalhadodecomo
criarainstânciaABAPTrial,utilizandoaAWS.Subaasuainstância,abrao
ambienteemãosàobra!
146

## Página 161

Capítulo10
ApêndiceII–Linkseindicações
10.1 Publicações, sites, guias, artigos e livros
citados
Paraquevocênãopreciseprocuraraolongodolivroquandoquiservisitarum
linkqueciteisobreumdeterminarassunto,crieiestecompiladoorganizado
portópicos.
Paraosiniciantes
•http://bit.ly/2biqp6f – Guia original do “ABAP Noob”, com comen-
tários relatando experiências de ingresso na área;
•http://bit.ly/abap-trial-guide-paul-hardy – Guia para instalação do 
ABAP AS Trial, por Paul Hardy;

## Página 162

CasadoCódigo Capítulo10. ApêndiceII–Linkseindicações
Livros
•Next Generation ABAP,porRichHeilmane ThomasJung:explicadi-
versasferramentasinteressantesdalinguagemABAP,daépocaemque
foilançado;
•ABAP to the Future, porPaulHardy: evoluçãodo Next Generation
ABAP,porémcomexplicaçõesparafeaturesmaisatuais;
•ABAP Developmento for SAP HANA, por Thorsten Schneider, Eric
WestenbergereHermannGahm:tudoquemudanodesenvolvimento
ABAPjuntoaoHANA;
•ABAP Objects,porHorstKellereSaschaKr üger: aprendendoABAP
dozeroatravésdoparadigmadeOrientaçãoaObjetos;
•Software Estimation: Desmystifying the Black Art,porSteveMcConnel:
umlivrointeirocriadocomointuitodeajudarumdesenvolvedora
estimarotempogastonacriaçãodeumcódigo;
•Clean Code: A Handbook of Agile Software Craftsmanship,porRobert
C.Martin:princípios,padrõesepráticasparacriarumcódigo“limpo”,
comocasosdeusosreaisdeaplicaç ão;
•The Design of EverydayThings,porDonaldNorman:exploraosconcei-
tosbásicosdodesigndeinteração,quevisamelhoraracomunicaç ão
entreobjetoeusuário.
10.2 Recomendações adicionais
OutrossitesquerecomendoforadoSCN,comconteúdorelacionadoaSAP
eABAP:
•http://zevolving.com/–Umsitecommuitainformaçãorelevante,prin-
cipalmenteparaquemgostadeusarABAPObject.Oautordosite,Nai-
meshPatel,fezumsériemuitointeressanteondeimplementouvários
DesignPatternsusandoABAP,comexemplosdeutilizaç ão.
151

## Página 163

10.2. Recomendaçõesadicionais CasadoCódigo
•http://abapinho.com/ – Blog de Nuno Godinho, de Portugal. Ele man-
tém uma frequência ótima de publicação desde o início do blog, em 
2009. O maior foco são pequenas curiosidades e dicas para ajudar no 
dia a dia. E o site ganha, de muito longe, como melhor layout já feito 
em site de ABAP. :)
•http://www.hanabrasil.com.br/ – Um projeto de Fábio Pagoti (abap101) 
e Fábio Ferri. É um site novo com foco principal em desenvolvimento 
HANA, UI5 e derivados do novo mundo.
•https://github.com/fabiopagoti/NYT-Launchpad-UI5 – Por favor no 
Fábio, o aplicativo UI5 do New York Times, exibido no capítulo 8, 
que foi feito por ele e está disponível neste repositório.
•http://bit.ly/2bIMvSc – Canal do YouTube que agrega diversas 
palestras feitas em eventos brasileiros da comunidade SAP. Note que 
não são específicos de ABAP, são relacionados a diversos assunto do 
mundo SAP.
No capítulo8, apresentei algumas ferramentas da “nova guarda” do
mundoSAP.Maisalgunslivrospublicadossobreoassuntoquevalemser
mencionados:
•UI5 para desenvolvedores ABAP,porFábioPagotidoABAP101eHA-
NABRASIL:focaemensinarsobreUI5eomundododesenvolvimento
webparaoABAPer,comexemplosqueaproximemosdoismundos.
•OData and SAP Netweaver Gateway, por Carsten Bönnen, Volker
Drees,AndréFischer,LudwigHeinzeKarstenStrothmann: particu-
larmenteachooGatewayumaferramentafantástica,eesselivrofaz
umótimotrabalhoemexplicartodaaavalanchedeconceitosesiglas
quefazempartedoprodutoedoprotocoloOData.
•Getting started with SAPUI5,porMiroslavAntolovic:umlivroquefoca
somentenabibliotecadaSAPparaUIs,oSAPUI5,combastantedeta-
lhes.
152

## Página 164

CasadoCódigo Capítulo10. ApêndiceII–Linkseindicações
Para terminar, muitos ABAPers ainda não sabem direito como 
fazer para trabalhar com o ABAP no Eclipse. O guia, disponível em 
http://bit.ly/2bkzbFe, é um bom ponto de partida. Mas tenha em mente 
que cer-tas features só vão funcionar em ambientes que estejam com 
versões atua-lizadas (como sempre). Para saber o que funciona em qual 
versão, acesse: http://bit.ly/2bCbbJO.
153

## Página 165

ÍndiceRemissivo CasadoCódigo
ÍndiceRemissivo
ABAP7.40,134
ABAPConceitos, 2,3,10,17,19,139,
141,143
ABAPHistória, 18
ABAPLicença,113
ABAPObjects, 58,105,106,110,133
ABAPTrial,142
abap_bool,77
Academia,7
Alocação,37,41,106
Armazenamentoemcolunas, 129
Arquitetura,48,100,104,122
Back-end,122
Bibliotecas,125
Caosdoatalho, 96
Certificações,8
Certification5,29
Coaching,54
Code-to-data,130,135
Comunidade,14,29,57,58
Concorrência,31,35
Conformismo,60,115
Constantes,74
Consultor,44,102
Consultoria,6,10,28,31,33,49
Contratação,37
Contratos,20
Cursosgratuitos,14,144
Definição,47
Desalocação,41
Designdeinteração,97
Didática,93
Documentação,39
Don’tRepeatYourself(DRY),112
Eclipse,11,135
Ecossistema,20,23
EspecificaçãoFuncional, 81,102
EspecificaçãoTécnica,81
Estimativas,38,48
Estudos,28,52,55,64,106,144
Fábricadesoftware,53,103
FAEversusINNERJOIN, 58
Feedback,42,54
Formação,22
Front-end,125
Funçãofaz-tudo, 69
FuturodoABAP, 24
GoLive, 40
Gordura,39
Guidelines,38,79
154

## Página 166

CasadoCódigo ÍndiceRemissivo
HANACloudPlatform(HCP), 132
Hardcode,75,76
In-memory,128
Informação,56
Inglês,14,140
Inovação,11,23,105,108,119
Interfaces,94
Livros,145
Mercado,18,21
Metodologiaságeis,83,92
Middleware,124
Mudanças,65
Mundinho,92
Networking,22
Nomenclatura,73
Notaçãohúngara,70
OData,120
Opensource, 114,126
OpenSQL, 19
Padronização,70,79
Performance,68
Picaretas,49
Prazos,40
Programador,44
Projeto,5,41,46
Propostas,35,38
Reclamões, 51,61
Recrutamento,50
ReescreveroSAP, 65
Retrocompatibilidade,19,65,106
Reutilização,67,104,109,115
Revisãodepares, 52
Robô,69,76,82,83,90,101
S/4HANA,133
SAPERP,2
SAPHANA,118
SAP HANA Extended Application
Services(XS), 132
Sombras,13
Tabelasespelho,131
Telas,94
UsereXperience(UX), 97,118
Usuário,95,96,101
Vagas,8,13
Variávelsuja,69
Versão740, 57
155