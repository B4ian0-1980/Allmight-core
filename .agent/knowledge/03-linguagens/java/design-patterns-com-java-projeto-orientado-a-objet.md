---json
{
  "id": "design-patterns-com-java-projeto-orientado-a-objet",
  "title": "Design Patterns com Java Projeto orientado a objetos guiado por padrões",
  "categoria": "03-linguagens",
  "subcategoria": "java",
  "resumo": "**Arquivo Original:** `Design Patterns com Java Projeto orientado a objetos guiado por padrões.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "com",
    "design",
    "guiado",
    "java",
    "linguagens",
    "objet",
    "objetos",
    "orientado"
  ],
  "perguntas_tipo": [
    "Como utilizar Design Patterns com Java Projeto orientado a objetos guiado por padrões?",
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

# Design Patterns com Java Projeto orientado a objetos guiado por padrões

> **Arquivo Original:** `Design Patterns com Java Projeto orientado a objetos guiado por padrões.pdf`
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
AgradecimentosPessoais
MeuprimeiroagradecimentoéaDeus,porEletermeproporcionadotudoparaque
trilhasseocaminhoquetrilheiatéchegarondeestouagora.Portercolocadoaspes-
soascertasparameajudaremminhasdificuldades,portermecolocadoobstáculos
nashorasadequadasquemepermitiramamadurecerparasuperarobstáculosmai-
oresnofuturoeportermeiluminadonomomentodasdecisõesmaiscríticasque
acabaramdirecionandominhavidanofuturo.
Emseguidaenviomeu“muitoobrigado”parameuspais,JoséMariaeMariada
Graça,quesempremeincentivaramemeapoiaramemminhasescolhas. Mesmo
estandodistantesfisicamentehoje,seiquetodososdiaselesrezametorcempor
mim.Imaginodireitinhoelesmostrandoesselivroparatodomundocomomaior
orgulho!Aproveitoessaoportunidadeparaestenderesseagradecimentoparatoda
minhafamilia,emespecialparaminhaTiaDorinhaquesempreestevedomeulado
quandoprecisei.
AgradeçotambémaMariaEduarda,aDuda,minhafilhamaisvelha,portrazer
sóalegriadesdequechegounessemundo.Seujeitoamigoecarinhosomeconforta
semprequeporalgummotivoestouparabaixo.Nãoseicomotantabondadeepaci-
ênciapodecaberemapenasumapessoa.Soumuitogratopeloseucompanheirismo,
comoquandoelasentadomeuladobemagarradinhaparaassistirumfilmeoujogar
umvideo-game.
Seguindoparaamaisnovadafamilia,agrade çoaAnaBeatriz,aBia,porcon-
teramaiorconcentra çãodeenergiaealegriadetodomundo. Apesardeserbem
bagunceiraegostardeumalvoro ço,elasemprefazalgumacoisaqueconseguetirar
umagargalhadadenossabocanashorasmaisinesperadas.Éatédifícildedescrever
aalegriaquesintoquandoeuchegoeessabaixinhavemgritandoomeunomeedá
umabraçonaminhaperna.
Deixeiparaofimosagradecimentosparaminhacompanheiradetodavida,mi-
nhaesposaRoberta,ou,comoeuchamoela,Lindinha.Achoqueelanãotemno ção
i

## Página 6

CasadoCódigo
doamorquesintoporelaecomosuapresen çaécentralemminhavida.Euagra-
deçoaelaporatravésdesuasa çõestersetornadoapessoamaisimportantedaminha
vida.Semelaeuseriaincompletoenãoteriaestruturaparatertrilhadoocaminho
queseguiemminhavidaatéessemomento.Muitoobrigadoportodoseuapoio,por
todoseuamoreportodoseucarinho!
ii

## Página 7

CasadoCódigo
AgradecimentosProfissionais
Antesdemencionaralguémdeformaespecífica,gostariadeagradeceratodosmeus
professores,colegasdetrabalho,amigosecompanheirosquedealgumaformacon-
tribuiramparameuconhecimentoemeincentivaramaseguiremfrente.Nossavida
éfeitadepessoasedeexperiências,eéapartirdissoqueseguimosnossoscaminhos
erealizamosnossasescolhas.
PrimeiramentedeixoumagradecimentoinstitucionalaoITA,uminstitutoque
éreferêncianacionaleinternacionalemengenharia,emondemeformeiemEnge-
nhariadaComputa çãoefizmeumestradoedoutorado.Alémdisso,tambémfoium
localondetiveaoportunidadedeatuarcomoprofessorpormaisde5anos.Foram
experiênciasquememarcaramesãoumaimportantepartedaminhahistória.Eusaí
doITA,mascomcertezaoITAnãosaiudemim!Agrade çoemespecialaoprofes-
sorClovisFernandes,meuorientadornagradua ção,nomestradoenodoutorado.
Umgrandeamigo,quesempremeincentivouequefoigrandementor,cujosensina-
mentosforammuitoalémdequestõestécnicas.Esperoaindafazermosmuitascoisas
juntos!
AgradeçoarevistaMundoJ,principalmenteaoMarcoGuapo,inicialmentepor
terabertoespa çoparaqueescrevessesobreminhasideiasemeusconhecimentose
emseguidaporterconfiadoamimoconteúdodarevistacomoeditor-chefe.Atra-
vésdaminhaatua çãonarevistaeupudeaprendermuitacoisaememantersempre
atualizadoduranteosúltimosanos.Atravésdosartigosqueescreviganheiexperiên-
ciaetomeigostopelaescritadeconteúdotécnico.Possoafirmarcomcertezaquea
sementedesselivrofoiplantadaemalgunsdemeusartigosduranteosúltimosanos.
Esperoqueessaparceriaaindadurebastantetempo!
Agradeçotambémacomunidadedepadrões,tantonacionalquantointernaci-
onal,portermeinfluenciadocomtodasuaculturaeideias. Sougratoporterem
merecebidodebra çosabertoseporteremfornecidoumforumondefoipossível
debaterasminhasideiaseobterfeedbackdostrabalhosqueestourealizando.Agra-
iii

## Página 8

CasadoCódigo
deçoemespecialpeloapoioeincentivodeFabioKon,FábioSilveira,JerffesonSouza,
UiráKulezsa,AdemarAguiareFilipeCorreia.Tambémagrade çopelosmeusgurus
JosephYodereRebeccaWirfs-Brock,comquemaprendidemaisetivediscussões
muitointeressantessobremodelagemearquiteturadesoftware.
AgradeçoaoINPE,institui çãoondeacabeideingressar,portermerecebidode
braçosabertosepelaconfian çaquetemdepositadoemmeutrabalho.Esperopoder
darmuitascontribui çõesedesenvolverdiversostrabalhosinteressantesduranteos
anosqueestãoporvir!
FinalmenteagradeçoaCasadoCódigopeloconviteparaescritadesselivro.Ape-
sardavontadesempreterexistido,oconvitedevocêsfoioestopimparaqueesse
projetosetornassealgoconcreto. Deixoumagradecimentoemespecialaoeditor
desselivro,PauloSilveira,pelosquestionamentosesugestõesquecontribuiramde
formadefinitivaparaoconteúdodesselivro.
iv

## Página 9

CasadoCódigo
MinibiografiadoAutor
EduardoMartinsGuerranasceuemJuizdeForaem1980ecursouoensinobásico
emédioemescolapública,oColégiodeAplica çãoJoãoXXIII.Desdeessaépocaele
jádespertouseuinteressepelaprograma ção,come çandocomadigita çãodecódigo
BasicquevinhaemrevistasnoseudefasadocomputadorExatoPro. Adiversão
eramaisveroefeitodepequenasmodifica çõesnocódigodoqueojogoquesaia
comoresultado.Nessaépoca,poucodepois,tambémfezumcursodeClipper,onde
desenvolveuseuprimeirosoftware:umgerenciadordecanil!
Incentivadoporseusprofessores,pelafacilidadecomdisciplinasnaáreadeexa-
tas,prestouovestibularparaoITAem1998,logoapósotérminodeseusestudos,e
foiaprovado.Duranteocurso,eleoptoupelacarreiramilitarepelocursodecompu-
tação,alémdeparticipardeatividadesextracurricularescomoprojetosparaaem-
presajúnioreaulasnocursopré-vestibularparapessoascarentes,CASDVestibu-
lares. Nessescincoanos,Eduardoseapaixonoupelaáreadedesenvolvimentode
softwareepelapossibilidadedeusarconstantementesuacriatividadeparapropor
sempresoluçõesinteligenteseinovadoras.Doisdiasdepoisdeseformar,casou-se
comsuamaisfortepaixão,suaesposaatual,Roberta.
Apósformado,em2003,foialocadonoCentrodeComputa çãodaAeronáutica
deSãoJosédosCampos(CCA-SJ),ondeficariapelospróximos4anos.Duranteesse
período,trabalhoucomodesenvolvimentodesoftwareoperacionalparaatenderas
necessidadesdaFor çaAéreaBrasileira,adquirindoumavaliosaexperiêncianaárea.
Nofinalde2005,comdedica çãoemtempoparcial,Eduardoconseguiuseutítulo
demestreemEngenhariadaComputa çãoeEletrônicaapresentandoadisserta ção
“UmEstudosobreRefatoraçãodeCódigodeTeste”.Nessetrabalho,Eduardodesen-
volvesuapaixãopelodesigndesoftware,realizandoumestudoinovadorsobreboas
práticasaosecodificartestesautomatizados.Essadisserta çãotalveztenhasidoum
dosprimeirostrabalhosacadêmicosnoBrasilnocontextodedesenvolvimentoágil.
Noanodeconclusãodeseumestrado,veiosuaprimeirafilha,MariaEduarda.
v

## Página 10

CasadoCódigo
Devidosuasededeconhecimento,aindanesseperíodo,estudouporcontapró-
priaetirousetecertifica çõesreferentesatecnologiaJava,sendonaépocaumdos
profissionaisbrasileiroscommaiornúmerodecertifica çõesnaárea. Alémdisso,
ocupaocargodeeditor-chefedarevistaMundoJdesde2006,naqualjápublicou
dezenasdeartigostécnicosdereconhecidaqualidade. Essesfatoslhederamuma
visãodaindústriadedesenvolvimentodesoftwarequefoimuitoimportanteemsua
trajetória,direcionandosuapesquisaeseustrabalhosparaproblemasreaiserele-
vantes.
No CCA-SJ, Eduardo atuou de forma decisiva no desenvolvimento de fra-
meworks. Seusframeworkssimplificaramacria çãodasaplica çõesederammaior
produtividadeparaaequipedeimplementa ção.Umdeles,oSwingBean,foitrans-
formadoemumprojetoopen-sourceejápossuimaisde5000downloads.Agrande
inovaçãoediferencialdeseusframeworksestavanofatodeserembaseadosemme-
tadados.Apartirdessecasodesucesso,eledecidiuestudarmaissobrecomoautili-
zaçãodemetadadospoderiaserfeitaemoutroscontextos.Foiumasurpresadesco-
brirque,apesardeoutrosframeworkslíderesdemercadoutilizaremessastécnicas,
aindanãohavianenhumestudosobreoassunto.Foi,então,queEduardocome çou
suajornadaparaestudaretornaracessívelousodessatécnicaporoutrosdesenvol-
vedores,poiselesabiadopotencialqueosframeworksbaseadosemmetadadostem
paraagilizarodesenvolvimentodesoftwareeotornarmaisflexível.
Então,em2007,eleingressounocursodedoutoradodoITApeloPrograma
dePós-Gradua çãoemAplica çõesOperacionais–PPGAO.Apesquisasobrefra-
meworksbaseadosemmetadadosseencaixavaperfeitamentenoobjetivodopro-
grama.Acria çãodearquiteturasflexíveis,nasquaissepodeacrescentarfuncionali-
dadedeformamaisfácil,éalgocríticoparaaplica çõesdecomandoecontrole,foco
deumadasáreasdoprograma.OrientadopeloprofessorClovisTorresFernandes,
começouumapesquisaqueenvolveuaanálisedeframeworksexistentes,aabstra ção
detécnicasepráticas,acria çãodenovosframeworksdecódigoabertoeaexecu ção
deexperimentosparaavaliarosconceitospropostos.
FoinessaépocaqueEduardocome çouaparticipareseenvolveunacomunidade
depadrões. Em2008submeteuparaoSugarLoafPLoPemFortalezaosprimeiros
padrõesqueidentificouemframeworksqueutilizavammetadados.Nessemomento
eleseemplogoucomoespíritodecolabora çãodacomunidadedepadrões,onde
recebeuumimensofeedbackdotrabalhoqueestavarealizando.Desdeentãosetor-
nouummembroativodacomunidade,publicandoartigoscomnovospadrõesem
eventosnoBrasilenoexterior. Alémdisso,em2011participoudaorganiza çãodo
vi

## Página 11

CasadoCódigo
MiniPLoPBrasil,em2012foioprimeirobrasileiroaserchairdaprincipalconferên-
ciainternacionaldepadrões,oPLoP,eem2013estátambémparticipandotambém
daorganizaçãodopróximoMiniPLoP.
Enquantorealizavaseudoutorado,Eduardofoiincorporado,aindacomomili-
tar,nocorpodocentedoDepartamentodeCiênciadaComputa çãodoITA,onde
pôdedesenvolverumanovapaixão:ensinar! Duranteesseperíodo,ministrouau-
lasnagradua çãoeemcursosdeespecializa ção,eorientouumasériedetrabalhos
que,decertaforma,complementavameexploravamoutrosaspectosdoqueestava
desenvolvendoemsuatese.Emconsequênciadobomtrabalhorealizado,foicon-
vidadoportrêsvezesconsecutivasparaseroprofessorhomenageadodaturmade
graduaçãoEngenhariadaComputa çãoeduasvezesparaaturmadeespecializa ção
emEngenhariadeSoftware.
Em 2010, apresentou seu doutorado chamado “A Conceptual Model for
Metadata-basedFrameworkseconcluiucomsucessoessajornadaquedeixoudi-
versascontribuições.Devidoarelevânciadotema,foiincentivadopelosmembros
dabancaacontinuarosestudosquevemrealizandonessaárea.Apesardateseter
trazidograndesavan ços,eletemconsciênciaqueaindahámuitoaserfeito.Umade
suasiniciativasnessaáreafoioprojetoEsfinge( http://esfinge.sf.net),queéumpro-
jetoguarda-chuvaparaacria çãodediversosframeworkscomessaabordagembase-
adaemmetadados.Atéomomentojáexistemtrêsframeworksdisponíveisevários
artigoscientíficosemcimadeinova çõesrealizadasnessesprojetos.Nomesmoano
queterminouseudoutorado,veiosuasegundafilhinha,aAnaBeatriz.
Em2012,EduardoprestouconcursoparaoInstitutoNacionaldePesquisasEs-
paciais,ondeassumiuocargodepesquisadornoinício2013.Hojeeleseguecomsua
pesquisanaáreadearquitetura,testesedesigndesoftware,buscandoaplicarastéc-
nicasquedesenvolveparaprojetosnaáreaespecial.Adicionalmente,atuacomodo-
centenapós-gradua çãodeComputa çãoAplicadadesseinstituto,ondebuscapassar
oconhecimentoqueadquiriueorientaralunosparacontribuiremcomessasáreas.
vii

## Página 12

CasadoCódigo
Porquemaisumlivrodepadrões?
O primeiro livro de padrões “Design Patterns: Elements of Reusable Object-
OrientedSoftware”,conhecidocomoGangofFour(GoF),jáfoilan çadoamaisde
15anosedeformaalgumaseuconteúdoestáultrapassado.Emminhaopinião,esse
livrofoialgomuitoafrentedeseutempo,sendoquemuitasdesuaspráticassóforam
serutilizadasdeformaefetivapelaindústriaalgunsanosdepois.Duranteessesanos,
diversoslivrossobreessespadrõesforamescritos,apresentandosuaimplementa ção
emoutraslinguagensouensinando-osdeformamaisdidática.Dessecontextopo-
demsurgirasseguintesperguntas:seráqueéprecisomaisumlivrosobrepadrões?
Oqueesselivrotrásdediferente?
Duranteessesúltimosanostivediversostiposdeexperiênciaquemefizeremter
diferentesvisõessobreospadrões.Dentreessasexperiênciaseupossocitaroensino
demodelagemdesoftwareepadrões,autiliza çãodepadrõesparaodesenvolvimento
deframeworkseaplica ções,aidentifica çãodenovospadrõesapartirdoestudode
implementaçõesexistentesediscussõesnacomunidadesobrepadrõesesuaaplicabi-
lidade.Apartirdissoacreditoquetiveaoportunidadedeterumavisãodiferenciada
sobreessespadrões,eéessavisãoqueprocuropassarnesselivro.Asse çõesaseguir
descrevemalgunsdiferenciaisdesselivroemrela çãoaoutrosexistentes.
UmaSequênciaDidáticaparaAprendizado
Percebiquemuitoscursossobrepadrões,sendoelesdadosporuniversidadesou
empresasdetreinamento,vãoensinandoospadrõesumporum.Masqualéamelhor
ordemparaoensinoeaassimila çãodospadrões? Issoeraalgoqueeradecidido
porcadaprofessor.Umaordeminadequadanesseaprendizadopodeimpedirqueo
alunonãocompreendaosprincípiosportrásdasolu çãodopadrão,oquedificulta
suacompreençãoarespeitodesuaaplicabilidadeesuasconsequências.Issotambém
podecausarumavisãolimitadadasolu çãodopadrão,oqueimpedesuaadapta ção
paraoutroscontextossimilares.
ix

## Página 13

CasadoCódigo
Esselivroprocuraorganizarospadrõesemumasequênciadidáticaparaoapren-
dizado. Cadacapítuloagrupaospadrõespelotipodetécnicaqueutilizamemsua
soluçãooupelotipodeproblemaqueresolvem. Dessaforma,aoverumamesma
técnicaserutilizadaempadrõesdiferentesépossívelcompreendermelhorasuadi-
nâmicaedequeformasdiferenteselapodeserutilizada. Emcapítulosquefocam
emtiposdeproblema,avisãodasdiferentesalternativasdesolu çãoedassuasdi-
ferenças,criaumsensocríticoarespeitodaspossíveisalternativasdemodelageme
quaisoscritériosquedevemserconsideradosparasuaescolha.
Issofazcomqueesselivrováalémdaapresenta çãodospadrõesesejanaverdade
arespeitodetécnicasparamodelagemorientadaaobjetos.Ospadrõessãoutiliza-
doscomoumareferênciaparaadiscussãodecadaumadessastécnicas.Dessaforma,
esselivroérecomendadoparautiliza çãocomomaterialbaseemcursosdegradua-
çãooupós-gradua çãoarespeitodetécnicasdeprograma çãoorientadaaobjetosou
programaçãoorientadaaobjetosavan çada.
RelaçãoentrePadrões
Outroproblemaqueperceboéqueospadrõestendemaserolhadosdeforma
individual.Issoéumaconsequênciadoformatoqueospadrõespossuemedofato
deseremauto-contidos,ouseja,todainforma çãosobreopadrãoestarcontidaem
suadescrição. Issoporumladoébompoispermitequealguémobtenhatodasas
informaçõessobreumdeterminadopadrãoemapenasumlocal.Porém,poroutro
lado,perde-seumpoucoaideiaarespeitodorelacionamentoentreospadrões.Ape-
sardehaverumase çãoquedescreveospadrõesrelacionados,aindaéumadescri ção
pequenaparaumaquestãodetamanhaimportância.
Apresentarorelacionamentoentreospadrõesfoiumdosobjetivosdesselivro.
Apesardecadapadrãoapresentarumasolu çãoindependente,édacombina çãoen-
treelesqueépossívelcriarumasinergiaparacria çãodesolu çõesaindamelhores.
Dessaforma,amedidaqueolivrovaiseguindo,enovospadrõesvãosendoapresen-
tados,existeumapreocupa çãoemmostrarcomoelespodemsercombinadoscom
ospadrõesanterioresoucomoelespodemserutilizadoscomoumaalternativaaum
outropadrão.Essetipodediscussãoéimportante,poisalémdesaberasolu çãodo
padrão,tambéméessencialsaberquandoaplica-la.
RefatoraçãoparaPadrões
Amodelagemdeumaaplica çãoéumaquestãodinâmicaqueevoluiamedida
x

## Página 14

CasadoCódigo
queodesenvolvimentodosoftwarevaiseguindoseucurso. Apesardeaindaser
comumamodelagemdasclassesdaaplica çãoapartirdediagramasantesdoinicioda
implementações,muitasvezesosproblemasaparecemsomentedepois.Sendoassim,
tãoimportantequantosabercomoutilizarospadrõesnamodelageminicial,ésaber
comorefatorarumcódigoexistenteparaumasolu çãoqueutilizeumdeterminado
padrão.Arefatora çãoconstantedocódigoéhojeumadasbasesparaamanuten ção
desuaqualidadeaolongodoprojeto.
Dessaforma,alémdeapresentarospadrões,esselivrotambémsepreocupaem
mostrarquaisospassosqueprecisariamserfeitospararefatorarumcódigoexistente
emdireçãoaumdeterminadopadrão.Esteassunto,quejáfoitemadeumlivrodedi-
cadosomenteaele,aquiéapresentadodeformafluidajuntamentecomospadrões.
Issoéimportanteparaqueoleitorpossaterumavisão,nãoapenasestáticaemrela-
çãoautiza çãodeumpadrão,masdecomoumcódigoexistentepodeevoluireser
melhoradoapartirdesuaintrodu çãoapartirdepequenospassos.
ExemplosRealistasedoDia-a-dia
Pormaisquediagramassejamúteisparaquesetenhaumavisãogeraldeumaso-
lução,osdesenvolvedoresaindatemmuitoaculturado“ show me the code”,querendo
vernapráticacomoumpadrãopodeserimplementado.PormaisqueoGoFtenha
sidoumlivroafrentedeseutempo,eleutilizaexemplosquehojeestãodistantesde
umdessenvolvercomum,comoacria çãodeumasuitedecomponentesgráficosou
umeditordetexto.Algunsoutroslivrosacabamtrazendo“ toy examples”,queseriam
exemplossimplesedidáticos,masquesãoforadocontextodeaplica çõesreais.
Achomuitoimportantequeoleitorseidentifiquecomosexemplosefa çauma
ligaçãocomotipodesoftwarequedesenvolve. Aoseverpróximoaosexemplose
possuirumaexperiênciaanteriorcomaqueletipodeproblema,émuitomaisfácil
compreenderasquestõesqueestãoenvolvidaseasalternativasdesolu çãocomsuas
respectivasconsequências.Nesselivro,busqueitrabalharcomexemplosrecorrentes
emaplicaçõesdesenvolvidasporgrandepartedosprogramadores,comogera çãode
relatórios,carrinhodecomprasemaplica çõesdee-commerceegera çãodearquivos
paraintegraçãoentreaplica ções. Acreditoqueassimficarábemmaisclarocomo
cadaumpoderáutilizaressespadrõesemseudia-a-dia.
DicaseReferênciasparaImplementa çõesemJava
Muitospadrõesapresentadosporesselivrosãoamplamenteutilizadosemfra-
xi

## Página 15

CasadoCódigo
meworkseAPIsJava. Muitasvezes,apenasporseguirasregrasdeumadetermi-
nadaAPI,semsabervocêjáutilizandoumdeterminadopadrão.Aflexibilidadeque
aqueleframeworkconsegueparaserinstanciadonasuaaplica ção,muitasvezesé
conseguidojustamentepelousodopadrão! Oconhecimentodeumasitua çãoem
queaquelepadrãofoiutilizadae,muitasvezessemsaber,vocêacabououtilizando,
tambémajudamuitoemsuacompreen ção.
Dessaforma,esselivrotambémcitadiversasclassesdeAPIspadrãodalingua-
gemJavaedeframeworksamplamenteutilizadospelacomunidadededesenvolvi-
mento. Issovaipermitirqueodesenvolvedorpossacompreendermelhoraquela
soluçãointeligenteutilizadanaquelecontexto,etrazeramesmaideiaparaquestões
doseuprópriocódigo.
Alémdisso,comoopróprionomedolivrodiz,ospadrõesdeprojetosãoapre-
sentadosnalinguagemJavae,dessaforma,acabamtrazendoalgumasdicasmaises-
pecíficasdalinguagemjparasuaimplementa ção.Essasdicasvãodesdeautiliza ção
dosprópriosrecursosdalinguagem,comoautiliza çãodesuabibliotecadeclassese,
atémesmo,deframeworksexternos.
xii

## Página 16

CasadoCódigo
ListadeDiscussão
Odesigndesoftwareéumtemapeloqualmeapaixoneijustamenteporseralgoem
queousodacriatividadeéessancial,ecadaaplica çãotemsuasparticularidades,o
quesempretraznovasquestõesaseremdiscutidas.Omesmoocorrecompadrões!
Elesjáestãoaíamuitosanoseatéhojeaindaexistemuitadiscussãosobreeles!Sendo
assim,eugostariaqueesselivronãofosseapenasumacomunica çãodemãoúnica
ondeeuescrevoevocêsleem,masoiníciodeumcanaldecomunica çãoparafo-
mentardiscussõeseconversassobrepadrõesedesigndesoftwareemgeral.
Sendo assim, criei uma lista de discussão com o nome"Design Patterns
em Java: Projeto orientado a objetos guiado por padrões”no endereço
projeto-oo-guiado-por-padroes@googlegroups.com.
Sevocêquerdiscutir,colocarsuasdúvidasesabereventosenovidadesnomundo
dospadrões,deixoaquiomeuconviteparaaparticipa çãonogrupo!
xiii

## Página 17

CasadoCódigo
Prefácio
Por Joseph Y oder
Jáfazemcercade20anosqueo GangofFour escreveuolivroinicialdepa-
drõeschamado "DesignPatterns: ElementsofReusableObject-OrientedSoft-
ware”.Desdeaquelaépoca,ospadrõesdeprojetosetornarammuitoconhecidose
umaparteessencialdeumaboamodelagememsistemasorientadosaobjetos.Adi-
cionalmente,ospadrõesganharamumagrandeaceita çãonacomunidadededesen-
volvimentodesoftware,oquepodeserobservadopelaexistênciadediversaspubli-
caçõesecasosdesucesso.Existemtambémdiversasconferênciasaoredordomundo
criadasaosmoldesdaprimeiraconferênciasobrepadrões,a PatternLanguagesof
Programs(PLoP).
MesmonosanosiniciaisdoJava,épossívelobservarcomoospadrõesinfluenci-
aramalinguagem.Algumasdessasinfluênciaspodemservistasclaramentenaspri-
meirasAPIsdoJava,comoasinterfaces Iteratore Observer,enquantooutras
foramimplementadascomopartedaevolu çãodessasAPIs,comoaimplementa ção
doslisteners,quesãoumaimplementa çãomaisatualdopadrão Observer.
Porém,éimportantenotarqueumbomdesignnãoaconteceporacidente,pois
eleexigetrabalhoduroeevolu ção.Deformacomplementar,tambémnãoquerdi-
zerqueusandoumpadrãonecessariamentesetemumbomdesign. Porexemplo,
alinguagemJavafoilan çadaapenasalgunsanosdepoisdapublica çãodoprimeiro
livrodedesignpatterns.Porcausadisso,muitasdasprimeirasbibliotecasdalingua-
gemforaminfluenciadaspelolivroemuitospadrõesforamincorporadosnodesign
desuasprincipaisbibliotecaseframeworks.Noentanto,issonemsempreguiouas
soluçõesparaomelhordesigneforamnecessáriasváriasevolu çõesemsuasclasses
depoisquediversosproblemasforamencontradosnasprimeirasversões.
Um bom exemplo pode ser visto no tratamento de eventos do Java
AWT. No AWT 1.0, o tratamento de eventos utilizava o padrãoChain of
Responsibility.Aprincípioessapareciaumasolu çãoadequadaaoolharparaos
xv

## Página 18

CasadoCódigo
requisitos.Oproblemacomessaimplementa çãoeraqueprecisava-sedautiliza ção
deum Mediatoroudacria çãodediversassubclasses. Issopoderiacausarpro-
blemasdedesempenho,vistoqueparaoeventosertratadoeranecessáriopercorrer
todaacadeiaparadescobrirqualeraaclassequedeveriaprocessa-lo. Issomuitas
vezesdirecionavaodesenvolvedoracria çãodeumasolu çãomuitocomplexadevido
aograndenúmerodesubclassesqueprecisavacriar.
Apartirdisso,oAWT1.1passouatrataroseventosdeformamaiseficenteuti-
lizandoospadrões Observere Adapter. Essamodelagemevoluiudepoispara
autilizaçãodelisteners.Essaacabousendoumasolu çãomuitomaislimpaeefici-
ente,vistoqueapenasasclassesinteressadasnoeventoeramnotificadasquandoele
acontecia.Essahistóriaclaramentemostraqueodesigndeumsoftwaredevelevar
emconsideraçãoasconsequênciaspositivasenegativasdecadadecisão,esóporque
eleutilizapadrõesnãoquerdizerqueaquelaéamelhoralternativadedesign.Veja
queissonãoquerdizerqueutilizarpadrõeslevaadecisõeserradasdedesign,mas
que,pelocontrário,autilizaçãodeumoutropadrãomaisadequadosemostrouuma
soluçãomelhor.
Apenassaber comoaplicarospadrõesnãoéosuficienteparaumbomdesign.
Entenderquandoeondeaplica-losétãoimportantequanto,senãomaisimportante.
Defato,nodecorrerdotempo,mesmoumbomdesigninicialpodesercompro-
metidoporsucessivasrevisõesarquiteturais. Em1998,foifeitaaafirma çãoquea
arquiteturaquerealmentepredominavanapráticaeraa Big Ball of Mud (tra-
duzindoGrandeBoladeLama). Emesmocommuitotrabalhoededica çãoainda
épossívelacabarcomum Big Ball of Mud sevocênãoestácomprometidoa
manterocódigosemprelimpo.
Existemmuitasfor çasebonsmotivosquepodemlevaraumaarquiteturaex-
tremamentecomplexa.Defato,arquitetosetimesdedesenvolvimentoexperientes
estãoconstantementefazendoexatamenteoquedeveriaserfeitoquandosedeparam
com“lama”ecomplexidadedesnecessáriaemseusistema.
Quandosetentamanterumaarquitetura,éimportantetentarprotegercertas
partesdodesign. Grandessistemaspossuempartesmudamemdiferentesveloci-
dades. Existemcertasaçõesepadrõesquevocêpodeutilizarparaisolaredefinir
divisõesemvoltadessasdiferentespartes,tantoparatornaraarquiteturaestável,
quantoparapossibilitarasmudan çasondeelassãonecessárias.Defato,essaéuma
premissaimportantedospadrõesdeprojeto.Issosetornaumaconsidera çãoainda
maisimportantequandoevoluimosaestruturadasaplica çõesparaummundoonde
partedelasestálocalizadananuvem.
xvi

## Página 19

CasadoCódigo
Euconheçooautordesselivro(Eduardo)amuitosanos.Eduardotemgrande
experiênciaempadrões,designorientadoaobjetoseJava.Eujácolaboreietrabalhei
comeleemprojetosorientadosaobjetosepublica ções,incluindoaimplementa ção
dediversospadrõesdeprojetoeaconstru çãodeframeworks.Eduardotemmuita
experiêncianaconstruçãodeframeworks,atividadequeexigeumconhecimento
profundodepadrões,alémdequandoeondeutiliza-los.Eletemmaisdoqueuma
compreençãode“como”implementarumpadrãoemJava.Eduardoclaramentecom-
preendeoqueestáemjogoemumbomdesignorientadoaobjetosecomoutilizar
ospadrõesparaumdesignmaislimpo,maisreutilizávelemaisfácildemudar.
Qualquerdesenvolvedorparasetornarproficienteemumdesignorientadoaob-
jetosprecisarácompreendernãoapenasobásicosobrepadrões,mastambémprin-
cipiosmaisavan çadosarespeitodesuasconsequênciaseocontextoemquedevem
serutilizados.Estelivroémaisdoqueumlivrodereceitassobrecomoaplicarospa-
drões,pois,pelocontrário,eletraztambémimportantesprincípioseseaprofunda
nessastécnicasavançadasdedesign.Oleitorirádescobrirnesselivroumguiaefici-
entearespeitodecomoaplicarospadrões,comoescolheropadrãomaisadequado
ecomosaberquandoumdesigndeveserrefatoradoparaaintrodu çãodeumnovo
padrão.
Apósleresselivro,épossívelcontinuaressajornadasobreoconhecimentode
padrõesatravésdeconferênciassobreoassunto,comooSugarLoafPLoPnoBrasil.
Esteassuntotemsetornadodeextremaimportânciaparatodasasfacetasdossis-
temasdesoftware,principalmenteaquelesqueestãoemconstanteevolu çãoparase
manterematualizadosfrenteanovosrequisitos.
xvii

## Página 20

CasadoCódigo Sumário
Sumário
1 EntendendoPadrõesdeProjeto 1
1.1 ConceitosdaOrienta çãoaObjetos . . . . . . . . . . . . . . . . . . . . 2
1.2 Masessesconceitosnãosãosuficientes? . . . . . . . . . . . . . . . . . 7
1.3 OPrimeiroProblema:CálculodoValordoEstacionamento . . . . . 8
1.4 Strategy:oPrimeiroPadrão! . . . . . . . . . . . . . . . . . . . . . . . . 14
1.5 Oquesãopadrões? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
1.6 ComooLivroEstáOrganizado . . . . . . . . . . . . . . . . . . . . . . 18
2 ReusoAtravésdeHeran ça 21
2.1 ExemplodePadrãoqueUtilizaHeran ça-NullObject . . . . . . . . . 22
2.2 HookMethods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
2.3 Revisandomodificadoresdemétodos . . . . . . . . . . . . . . . . . . . 28
2.4 PassosdiferentesnaMesmaOrdem-TemplateMethod . . . . . . . . 29
2.5 RefatorandonaDire çãodaHeran ça. . . . . . . . . . . . . . . . . . . . 35
2.6 CriandoObjetosnaSubclasse-FactoryMethod . . . . . . . . . . . . 39
2.7 ConsideraçõesFinaisdoCapítulo . . . . . . . . . . . . . . . . . . . . . 43
3 DelegandoComportamentocomComposi ção 45
3.1 TentandoCombinarOp çõesdoGeradordeArquivos . . . . . . . . . 46
3.2 Bridge-UmaPonteentreDuasVariabilidades . . . . . . . . . . . . . 48
3.3 HookClasses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
3.4 State-VariandooComportamentocomoEstadodaClasse . . . . . . 56
3.5 SubstituindoCondicionaisporPolimorfismo . . . . . . . . . . . . . . 63
3.6 CompondocomMúltiplosObjetos-Observer . . . . . . . . . . . . . 66
3.7 ConsideraçõesFinaisdoCapítulo . . . . . . . . . . . . . . . . . . . . . 74
xix

## Página 21

Sumário CasadoCódigo
4 ComposiçãoRecursiva 77
4.1 CompondoumObjetocomsuaAbstra ção. . . . . . . . . . . . . . . . 78
4.2 Composite-QuandoumConjuntoéumIndivíduo . . . . . . . . . . 81
4.3 EncadeandoExecu çõescomChainofResponsibility . . . . . . . . . . 87
4.4 RefatorandoparaPermitiraExecu çãodeMúltiplasClasses . . . . . . 93
4.5 ConsideraçõesFinaisdoCapítulo . . . . . . . . . . . . . . . . . . . . . 96
5 EnvolvendoObjetos 99
5.1 ProxieseDecorators . . . . . . . . . . . . . . . . . . . . . . . . . . . . .100
5.2 ExemplosdeProxies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
5.3 ExtraindoumProxy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
5.4 AdaptandoInterfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
5.5 ConsideraçõesFinaisdoCapítulo . . . . . . . . . . . . . . . . . . . . . 120
6 EstratégiasdeCria çãodeObjetos 121
6.1 LimitaçõesdosConstrutores . . . . . . . . . . . . . . . . . . . . . . . . 122
6.2 CriandoObjetoscomMétodosEstáticos . . . . . . . . . . . . . . . . . 124
6.3 UmÚnicoObjetodaClassecomSingleton . . . . . . . . . . . . . . . 127
6.4 EncapsulandoLógicaComplexadeCria çãocomBuilder . . . . . . . 130
6.5 RelacionandoFamíliasdeObjetoscomAbstractFactory . . . . . . . 136
6.6 ConsideraçõesFinaisdoCapítulo . . . . . . . . . . . . . . . . . . . . . 140
7 Modularidade 141
7.1 FábricaDinâmicadeObjetos. . . . . . . . . . . . . . . . . . . . . . . . 142
7.2 InjeçãodeDependências . . . . . . . . . . . . . . . . . . . . . . . . . . 148
7.3 ServiceLocator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156
7.4 ServiceLocatorversusDependencyInjection . . . . . . . . . . . . . . 161
7.5 ConsideraçõesFinaisdoCapítulo . . . . . . . . . . . . . . . . . . . . . 163
8 AdicionandoOpera ções 165
8.1 ClassesqueRepresentamComandos . . . . . . . . . . . . . . . . . . . 166
8.2 CenáriosdeAplicaçãodoCommand . . . . . . . . . . . . . . . . . . . 173
8.3 DoubleDispatch-Mechama,queeutechamo! . . . . . . . . . . . . . 179
8.4 PadrãoVisitor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 184
8.5 ConsideraçõesFinaisdoCapítulo . . . . . . . . . . . . . . . . . . . . . 196
xx

## Página 22

CasadoCódigo Sumário
9 GerenciandoMuitosObjetos 199
9.1 CriandoumaFachadaparasuasClasses . . . . . . . . . . . . . . . . .200
9.2 SeparandoCódigoNovodeCódigoLegado . . . . . . . . . . . . . . .207
9.3 MediandoaIntera çãoentreObjetos . . . . . . . . . . . . . . . . . . .208
9.4 ReaproveitandoInstânciascomFlyweight . . . . . . . . . . . . . . . . 215
9.5 ConsideraçõesFinaisdoCapítulo . . . . . . . . . . . . . . . . . . . . . 225
10 IndoAlémdoBásico 227
10.1 Frameworks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 228
10.2 UtilizandoTiposGenéricoscomosPadrões . . . . . . . . . . . . . . . 233
10.3 PadrõescomTest-drivenDevelopment . . . . . . . . . . . . . . . . . . 236
10.4 PossoAplicaressesPadrõesnaArquitetura? . . . . . . . . . . . . . . . 241
10.5 ComunidadedePadrões . . . . . . . . . . . . . . . . . . . . . . . . . . 243
10.6 Eagora? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245
ÍndiceRemissivo 248
Bibliografia 251
Versão:16.1.7
xxi

## Página 23

Capítulo1
EntendendoPadrõesdeProjeto
“Eu diria algo como ‘Software está gerenciando o mundo’. Nosso trabalho é apenas
polinizá-lo ... ”
–BrianFoote
Imaginequeumapessoatenhaaprendidodiversastécnicasdepintura. Apar-
tirdesseconhecimentoelasaberácomopegarumpincel,comomisturarascorese
comotrabalharcomdiferentestiposdetinta.Seráquesomentecomesseconheci-
mentoelaconseguirápintarumquadro?Notequeelasabetudoqueseprecisapara
realizarapintura,porémtodoesseconhecimentonãoéválidoseapessoanãosou-
bercomoutilizá-lo.Pararealizaressatarefa,énecessário,alémdeconhecimento,ter
habilidade,queéalgoquesóseaprendecommuitapráticaetreino.Saberastécnicas
éapenasoprimeiropasso...
Comprogramaçãoaconteceumfenômenosimilar.Quandoseaprendeumalin-
guagemorientadaaobjetoseseusrecursos,issoéequivalenteaseaprenderapegar
emumpincel. Saber,porexemplo,comoutilizarheran çaepolimorfismonãoéo
suficienteparadistinguiremquaissitua çõeselesdevemserempregadosdeforma

## Página 24

1.1. ConceitosdaOrientaçãoaObjetos CasadoCódigo
apropriada.Éprecisoconhecerosproblemasquepodemaparecerduranteamode-
lagemdeumsistemaesaberquaisassolu çõesquepodemserimplementadaspara
equilibrarrequisitos,muitasvezescontraditórios,comosquaisseestálidando.
Felizmenteexisteumaformadeconseguiresseconhecimentosemprecisarpas-
sarpelocaminhotortuosodeerrarváriasvezesantesdeaprenderaformacorreta.É
umprazerpoderapresentarnesselivroos Design Patterns,padrõesdeprojetonatra-
duçãomaisutilizada,umaformadesedocumentarumasolu çãoparaumproblema
demodelagem.Maisdoqueisso,padrõesnãosãonovassolu ções,massolu çõesque
foramimplementadascomsucessodeformarecorrenteemdiferentescontextos.A
partirdeles,épossívelaprendercomaexperiênciadeoutrosdesenvolvedoreseab-
sorveresseconhecimentoqueeleslevaramdiversosanosparaconsolidar.
Oobjetivodessecapítuloéfazerumarevisãodosprincipaisconceitosdaorien-
taçãoaobjetoseapresentarcomoospadrõesdeprojetopodemserutilizadospara
adquirirhabilidadeemmodelagemdesoftware.Aoseufinal,seráapresentadauma
visãogeraldecomoessespadrõesserãoapresentadosnodecorrerdolivro.
1.1 Conceitos daOrientação a Objetos
Emlinguagensmaisantigas,nãohavianenhumasepara çãodoselementosdecódigo.
Eleeracriadoemúnicobloco,noqualparaseexecutardesviosnofluxodeexecu ção,
comoparaacria çãodeloopsecondicionais,eraprecisorealizarsaltosatravésdo
temidocomando goto. Issotornavaocódigomuitodifícildesergerenciadoe
reutilizado,complicandoseudesenvolvimentoemanuten ção.Foidessaépocaque
surgiuotermo "código macarrônico”,quesereferiaàdificuldadedecompreensãodo
fluxodeexecu çãodessesprogramas.
Emseguida,pararesolveresseproblema,foicriadaa programaçãoestruturada.
Nessenovoparadigmasurgiramestruturasdecontrolequepermitiamacria çãode
comandocondicionais,comoo ifeo switch,ecomandositerativos,comoo
foreo while.Umaoutraadi çãoimportanteforamasfun ções.Apartirdelasera
possíveldividiralógicadoprograma,permitindosuamodulariza ção. Issofacilita
queessasfun çõespossamserreutilizadasemoutrasaplica ções. Amaiordificul-
dadenesseparadigmaeracomolidarcomosdadoseocomportamentoassociadoa
eles.Eracomumacria çãodevariáveisglobais,quefacilmentepoderiamacabarcau-
sandoproblemasporestaremcomvaloresinconsistentes.Outroproblemaocorria
comdadosrelacionadosquepodiamserlivrementemodificadosefacilmentefica-
reminconsistentes.
2

## Página 25

CasadoCódigo Capítulo1. EntendendoPadrõesdeProjeto
Comoumaevolu çãodaprograma çãoestruturadasurgiua programaçãoorien-
tadaaobjetos .Alémdaestrutura çãodalógica,comesseparadigmaerapossívela
estruturaçãodosdadoseconceitosdosoftware.Sendoassim,pode-secolocartoda
lógicarelacionadaaumconjuntodedadosjuntocomele. Alémdisso,apartirda
possibilidadedeabstra çãodeconceitosconsegue-sedesacoplarcomponentes,ob-
tendoummaiorreúsoeumamaiorflexibilidade.
Ostópicosaseguirexploramcommaiordetalheosprincipaisconceitosdapro-
gramaçãoorientadaaobjetos.
ClasseseObjetos
Naprogramaçãoorientadaaobjetossãodefinidosnovostiposatravésdacri-
açãode classes,eessestipospodemserinstanciadoscriando objetos. Aideiaé
queumobjetorepresenteumaentidadeconcretaenquantosuaclasserepresenta
umaabstra çãodosseusconceitos. Se,porexemplo,tivermosumaclasse Gato,
oGarfieldeoFrajolaseriamobjetosdessaclasse. Adicionalmente, umaclasse
CarteiraDeIdentidade,querepresentaumaabstra ção,teriacomoinstânciasa
minhaeasuacarteiradeidentidade.
Euvejomuitaspessoasutilizaremametáfora "a classe seria a forma e o objeto
seria o pão”paraexplicararela çãoentreclasseseobjetos.Pessoalmente,nãogosto
dessaanalogiapoiselalevaaentenderqueaclasseéoqueproduzoobjeto,oque
seriamaispróximodoconceitodefábrica(queserávistonoCapítulo 6desselivro).É
importanteperceberqueosobjetosrepresentamentidadesconcretasdoseusistema,
enquantoasclassesabstraemsuascaracterísticas.
Aclassepossuiestadoecomportamento,quesãorepresentadosrespectivamente
pelosatributosemétodosdefinidos.Enquantoumaclassepossuiumacaracterística,
umobjetopossuiumvalorparaaquelacaracterística.Porexemplo,um Gatopos-
suiacordopelo,enquantooGarfieldpossuiseupelolaranjado.Aclassepossuium
comportamentoeoobjetopoderealizaraquelecomportamento.Seguindoomesmo
exemplo,enquantoum Gatopodecorrer,oFrajolarealmentecorreparatentarpe-
garoPiu-piu.
Projetarumsistemaorientadoaobjetosconsisteemdefinirsuasclassesecomo
elascolaboramparaconseguirimplementarosrequisitosdeumaaplica ção. Éim-
portanteressaltarquenãoésóporqueumalinguagemorientadaaobjetosestásendo
utilizadaqueseestarámodelandodeformaorientadaaobjetos.Sesuasclassesnão
representamabstraçõesdosistemaesãoapenasrepositóriosdefun ções,vocêna
verdadeestáprogramandosegundooparadigmaestruturado.
3

## Página 26

1.1. ConceitosdaOrientaçãoaObjetos CasadoCódigo
Herança
Seumaaplica çãoprecisadeumconjuntodeobjetos,devemhaverclassesque
abstraiamessesconceitos.Porém,essesmesmosobjetospodemprecisarsertratados
empartesdiferentesdosoftwareapartirdediferentesníveisdeabstra ção.OGarfield
eoFrajolapodemsertratadoscomogatosemumapartedosistema,porémoutra,
queprecisartambémlidarcomosobjetosPica-paueMickeyMouse,podeprecisar
deumconceitomaisabstrato,comoanimaloupersonagem.
Aherançaéumacaracterísticadoparadigmaorientadoaobjetosquepermite
queabstraçõespossamserdefinidasemdiversosníveis.Considerandoquevocêtem
umaclasse,elapodeserespecializadaporumaoutraqueirádefinirumconceito
maisconcreto. Poroutrolado,umconjuntodeclassespodesergeneralizadopor
umaclassequerepresentaumconceitomaisabstrato.Quandoumaclasseestende
outra,elanãosóherdaaestruturadedadoseocomportamentodasuperclasse,mas
tambémocontratoqueelamantémcomosseusclientes.
Umdosgrandesdesafiosdamodelagemorientadaobjetoséidentificarospontos
emqueessaabstra çãodeveserutilizadaequeseráaproveitadadeformaadequada
pelosistema.Pelofatodeumsistemadesoftwareserumarepresenta çãodealgum
processoqueacontecenomundoreal,issonãosignificaquetodasasabstra çõesexis-
tentesprecisamserrepresentadasnosoftware.Umavião,porexemplo,seriarepre-
sentadodeformacompletamentediferenteemumsimuladordevoo,emumsistema
decontroledetráfegoaéreoenosistemadevendasdeumacompanhiaaérea.Saber
qualarepresenta çãoeasabstra çõesmaisadequadaséumgrandedesafio.
Encapsulamento
Semprequefalosobreencapsulamento,iniciocomafrase "A ignorância é uma
benção!”. Nãomeentendammal,mascomacomplexidadedascoisascomqueli-
damosnosdiasdehoje,érealmentemuitobomnãoprecisarsabercomoelasfunci-
onamparautilizá-las.Ficofelizempoderassistirminhatelevisão,mudardecanal,
aumentarovolumeenãoteramenorideiadecomoessascoisasestãofuncionando.
Imaginecomoseriacomplicadopoderutilizarnovastecnologiasseelasexigissem
umacompreensãoprofundadeseufuncionamentointerno.
Essamesmaquestãoacontececomsoftware.Antesdaprograma çãoestruturada,
odesenvolvedorprecisavaconhecerosdetalhesdeimplementa çãodecadapartedo
código. Comacria çãodasfun ções,houveumcertoavan çoemrela çãoàdivisão
docódigo,porémautiliza çãodealgumasfun çõesaindademandavaumconheci-
4

## Página 27

CasadoCódigo Capítulo1. EntendendoPadrõesdeProjeto
mentosobreseufuncionamentointerno,comoquevariáveiselasestãoacessandoe
atualizando.
Oencapsulamentoéumconceitoimportantedaorienta çãoaobjetosquediz
quedevehaverumasepara çãoentreocomportamentointernodeumaclassecoma
interfacequeeladisponibilizaparaosseusclientes.Issopermitequeodesenvolvedor
queutilizarumaclasseprecisesabersomentecomointeragircomela,abstraindo
seucomportamentointerno. Esteéumconceitomuitopoderosoquepossibilitao
desacoplamentoentreasclasses,podendoserutilizadoparaumamelhordivisãodo
softwareemmódulos.
Osmétodos getterse setters,quesãoutilizadosrespectivamenteparaacessare
modificarpropriedadesemumobjeto,sãoumexemplodousodoencapsulamento.
Paraosclientesdaclasse,apenasumainforma çãoestásendorecuperadaoumo-
dificada,porémaimplementaçãoportráspoderealizaroutrascoisas.Aorecuperar
umainformação,elapodesercalculadaapartirdeoutrosdados,eaomodificaruma
informação,podehaverumavalida çãodosdados.Éimportantelembrarqueouso
dessesmétodosdeacessoéapenasumcome çoparaoencapsulamentodeumaclasse.
Aestruturadedadospodeserutilizadaemanipuladatambémporoutrosmétodos
deformatotalmentetransparenteàclassecliente.
AlinguagemJavaprovêasinterfacescomoumrecursodelinguagem,queper-
mitequeadefini çãodocontratoexternodaclassepossaserfeitadeformaseparada
daimplementação. Quandoumaclasseimplementaumainterfaceécomosees-
tivesseassinandoumdocumento,noqualelasecomprometeaimplementarseus
métodos.Dessaforma,osclientesdelanãoprecisamconheceraclasseondeestáa
implementação,masapenasainterface.Adicionalmente,diferentesimplementa ções
podemserutilizadaspeloclientesemamodifica çãodeseucódigo.
5

## Página 28

1.1. ConceitosdaOrientaçãoaObjetos CasadoCódigo
Interface ou classe abstrata?
Váriasvezesjámefizeramapergunta: "quando devo utilizar uma
classe abstrata e quando devo utilizar uma interface?”. Tantoasclasses
abstratasquantoasinterfacespodemdefinirmétodosabstratosquepre-
cisamserimplementadospelasclassesquerespectivamenteaestendeou
implementa.Porémapenasasclassesabstrataspodempossuirmétodos
concretoseatributos.Apesardessadiferen ça,arespostaparaperguntaé
maisconceitualdoquerelacionadacomquestõesdelinguagem.
Quandoaabstra çãoqueprecisarsercriadaforumconceito,ouseja,
algoquepossaserrefinadoeespacializado,deve-seutilizarumaclasse
abstrata. Quandoaabstraçãoéumcomportamento,ouseja,algoque
umaclassedevesaberfazer,entãoamelhorsolu çãoéacria çãodeuma
interface. Imagineumjogonoqualexistemnavesquesemovem. Se
suaabstraçãorepresentaumanave,entãovocêestárepresentandoum
conceitoedeveutilizarumaclasseabstrata.Poroutrolado,sesuaabs-
traçãorepresentaalgoquesemove,entãooqueestásendoabstraídoé
umcomportamentoeamelhorsolu çãoéusarumainterface.
Polimorfismo
Opolimorfismoénaverdadeumaconsequênciadautiliza çãodeheran çaeda
utilizaçãodeinterfaces.Nãofariasentidoutilizarheran çaparacriarnovasabstra-
çõesseoobjetonãopudesseservistocomoumadessasabstra ções. Equivalente-
mente,nãofariasentidohaverumainterfaceseaclassenãopudessesertratadacomo
algoquepossuiaquelecomportamento.Éatravésdopolimorfismoqueumobjeto
podeservistocomoqualquerumadesuasabstra ções.
Apalavrapolimorfismosignifica "múltiplas formas”,oqueindicaqueumobjeto
podeassumiraformadeumadesuasabstra ções.Emoutraspalavras,qualquerob-
jetopodeseratribuídoparaumavariáveldotipodeumadesuassuperclassesoupara
otipodesuasinterfaces.Issoéumrecursoextremamentepoderoso,poisumcódigo
podeutilizarumaclassequenãoconhece,sesoubertrabalharcomumadesuasabs-
trações.Issopodeterumimpactotremendonareutiliza çãoedesacoplamentodas
classes.
Umbomexemploparaentenderpolimorfismoéainterface Comparablequeé
6

## Página 29

CasadoCódigo Capítulo1. EntendendoPadrõesdeProjeto
providapelaAPIpadrãodalinguagemJava.Osalgoritmosdeordena çãopresentes
naclasse Collectionssabemordenarlistasdequalquerobjetoqueimplementa
essainterface,oqueincluiclassescomo Number, Stringe Date.Dessaforma,se
umaclassedasuaaplica çãoimplementaressainterface,entãoosalgoritmossaberão
ordenarumalistadesuasinstâncias.Omaisinteressanteéqueessealgoritmoutiliza
suaclasse,mesmotendosidodesenvolvidomuitoantesdelaexistir.
1.2 Mas esses conceitos não são suficientes?
Semmaisdelongas,jáireiresponderquenãosãosuficientes.Naverdade,compre-
enderbemessesconceitoséapenasoprimeiropassoparaarealiza çãodeumprojeto
orientadoaobjetos.Entenderosignificadodaheran çaesabercomoimplementá-la
nalinguagemdeprograma çãonãoésuficienteparasaberemquesitua çõesoseu
empregoéadequado.Sabercomoumaclasseimplementaumainterfacenãobasta
parasaberquandoseuusoiráajudararesolverumproblema.
Realizaramodelagemdeumsoftwareéumimensojogoderaciocínio,comoem
umtabuleirodexadrez.Damesmaformaquemuitasvezeséprecisoentregaruma
peçaparaseatingirumobjetivo,noprojetodeumsoftwareécomumabrirmãode
certascaracterísticasparaseobteroutras.Porexemplo,aoseadicionarumaverifi-
caçãodeseguran ça,odesempenhopodeserdegradado.Oumesmo,aoseadicionar
flexibilidade,acomplexidadedeusodasolu çãopodeaumentar.
Sãorarososbenefíciosquevêmsemnenhumaconsequêncianegativa.Durante
oprojetodeumsoftwareodesenvolvedorestásentadoemumamesadenegocia ção,
edooutroladoestãosentadososrequisitosqueprecisamseratendidos.Aocolocar
namesaumasolu ção,devemseravaliadosasperdaseosganhosobtidosparatentar
equilibrarosatributosdequalidadedosistema. Muitasvezeséprecisocombinar
maisdeumasolu çãoparaqueobenefíciodeumacompenseadesvantagemdaoutra.
Nessejogo,assolu çõesquepodemserempregadassãoasprincipaisarmasdo
desenvolvedor.Odesenvolvedorcommenorexperiênciaconheceumaquantidade
menordesolu ções,oquemuitasvezesolevaaadotarumprojetoinadequadoàs
necessidadesdosoftware. Aelabora çãodeumasolu çãopartindodozerotrazde
formaintrínsecaoriscodainova ção,emuitasvezesacaba-sedeixandodeconsiderar
outrasalternativas.
Mascomoconhecerdiversassolu çõessemprecisarpassarporváriosanosalter-
nandoentreescolhascertaseerradas?Comosaberocontextoemqueessassolu ções
sãoadequadasequaissãoascontrapartidasdosbenefíciosdasolu ção?Felizmente
7

## Página 30

1.3. OPrimeiroProblema:CálculodoValordoEstacionamento CasadoCódigo
existeumaformanaqualdesenvolvedoresmaisexperientesexpressamseuconheci-
mentoemumdeterminadodomínio.Eentãoeuapresentoospadrõesdeprojeto,os
Design Patterns!
1.3 OP rimeiroProblema:C álculo do Valor do Es-
tacionamento
Parailustrarcomoolivrovaiproceder,essase çãovaiapresentarumprimeiropro-
blemadeprojeto,apartirdoqualserãoexploradasasalternativasdesolu ção.Apesar
degrandepartedosproblemasserdesistemasfictíciosecriadosparailustraraapli-
caçãodospadrões,assitua çõesapresentadasporelessãorealistaseaplicáveisem
softwaresreais.
Considereosistemadeumestacionamentoqueprecisautilizardiversoscrité-
riosparacalcularovalorquedevesercobradodeseusclientes. Paraumveículo
depasseio,ovalordevesercalculadocomoR $2,00porhora,porém,casootempo
sejamaiordoque12horas,serácobradaumataxadiária,ecasoonúmerodedias
formaiorque15dias,serácobradaumamensalidade. Existemtambémregrasdi-
ferentesparacaminhões,quedependemdonúmerodeeixosedovalordacarga
carregada,eparaveículosparamuitospassageiros,comoônibusevans.Ocódigoa
seguirapresentaumexemplodecomoistoestavadesenvolvido.
public class ContaEstacionamento {
private Veiculo veiculo ;
private long inicio , fim ;
public double valorConta() {
long atual = ( fim==0) ? System .currentTimeMillis() : fim ;
long periodo = inicio - atual ;
if ( veiculo instanceof Passeio ) {
if ( periodo < 12 * HORA ) {
return 2.0 * Math .ceil(periodo / HORA );
} else if ( periodo > 12 * HORA && periodo < 15 * DIA ) {
return 26.0 * Math .ceil(periodo / DIA );
} else {
return 300.0 * Math .ceil(periodo / MES );
}
} else if ( veiculo instanceof Carga ) {
// outras regras para veículos de carga
8

## Página 31

CasadoCódigo Capítulo1. EntendendoPadrõesdeProjeto
}
// outras regras para outros tipos de veículo
}
}
Comoépossívelobservar, ocódigoutilizadoparacalcularosdiversoscon-
dicionaisécomplicadodeseentender. Apesardeapenaspartedaimplementa-
çãodométodotersidoapresentada,pode-seperceberqueasolu çãoutilizadafaz
com que o métodovalorConta()seja bem grande. As instâncias da classe
ContaEstacionamentorelacionadascomosveículosqueestãonomomentoesta-
cionadossãoexibidasparaooperadoretêmseutempoatualizadoperiodicamente.
Atéentão,oprópriodesenvolvedorsabiaqueocódigoestavaruim,mascomoo
códigoestavafuncionando,preferiudeixardaformaqueestá.Porém,osoftwareco-
meçouaservendidoparaoutrasempresaseoutrasregrasprecisariamserincluídas.
Algunsmunicípiospossuemleisespecíficasarespeitodointervalodetempoparao
qualumestacionamentodefinirsuatarifa.Alémdisso,diferentesempresaspodem
possuirdiferentescritériosparacobraroservi çodeseusclientes.
Asoluçãodaformacomoestánãoiráescalarparaumnúmerograndederegras!
Ocódigoquejánãoestavabompoderiacrescerdeumaformadescontroladaese
tornarnãogerenciável.Odesenvolvedorsabiaqueprecisariarefatoraressecódigo
paraumasolu çãodiferente.Oqueelepoderiafazer?
UsandoHeran ça
Aprimeiraideiaqueodesenvolvedorpensoufoinautiliza çãodeheran çapara
tentardividiralógica.Suaideiaeracriarumasuperclasseemqueocálculodovalor
dacontaseriarepresentadoporummétodoabstrato,oqualseriaimplementado
pelassubclassescomcadaumadasregras. AFigura 1.1apresentacomoseriaessa
solução.
9

## Página 32

1.3. OPrimeiroProblema:CálculodoValordoEstacionamento CasadoCódigo
Figura1.1:Utilizaçãodeheran çaparadividiralógica
Umdosproblemasdessasolu çãoéaexplosãodesubclassesquevaiacontecer,
devidoàsváriaspossibilidadesdeimplementa ção. Outraquestãoéqueutilizando
herança,depoisnãoépossívelalterarocomportamentoumavezqueclassefoiins-
tanciada. Porexemplo,depoisde12horasqueumveículoestiverestacionado,o
comportamentodocálculodatarifadeveseralteradodaabordagemporhoraparaa
abordagempordia.Quandosecriaoobjetocomosendodeumaclasse,paramudar
ocomportamentoqueelaimplementa,éprecisocriarumanovainstânciadeoutra
classe.Issoéalgoindesejável,poisamudan çadeveriaacontecerdentrodaprópria
classe!
Asegundasolu çãoqueodesenvolvedorpensoufoiutilizaraheran çamascom
umagranularidadediferente. Suaideiaeraquecadasubclassepossuísseocódigo
relacionadoaumaabordagemdecobran çaparaumtipodeveículo. Porexemplo,
nocasoacima,seriaapenasumasubclasseparaveículosdepasseioeelaconteriaos
condicionaisdetemponecessários.Dessaforma,amesmainstânciaseriacapazde
fazerocálculo.
Aocomeçaraseguiressaideia,odesenvolvedorpercebeuquenassubclassescri-
adasocorriabastanteduplica çãodecódigo.Umdosmotivoséqueacadapequena
diferençanaabordagem,umanovasubclasseprecisariasercriada. Seamudan ça
fossepequena,orestodocódigocomumprecisariaserduplicado.AFigura 1.2ilus-
traessaquestão.Umadasclassesconsideraatarifadeveículodepasseiocomoapre-
sentadoanteriormenteeaoutraconsideraqueaprimeirahoraprecisaserdividida
emperíodosde15minutos(umaleiqueexistenomunicípiodeJuizdeFora)eem
seguidafazacobran çaporhoracomomostradaanteriormente.Observequesehou-
vesseumaclassecomosperíodosde15minutosmaisacobran çapordiaepormês,
10

## Página 33

CasadoCódigo Capítulo1. EntendendoPadrõesdeProjeto
maiscódigoaindaseriaduplicado.
Figura1.2:Duplica çãodecódigocomaimplementa çãomenosgranular
Mas será que é possível ter uma forma de manter a mesma instância de
ContaEstacionamentosemprecisarduplicarcódigo?
PensandoemComposi ção
Aopensarmelhor,odesenvolvedordecidequeaheran çanãoéamelhoraborda-
gempararesolveroproblema.Eleprecisadeumasolu çãoquepermitaquediferentes
algoritmosdecálculodetarifapossamserutilizadospelaclasse.Adicionalmente,é
desejávelquenãohajaduplica çãodecódigoequeomesmoalgoritmodecálculo
possaserutilizadoparadiferentesempresas.Alémdisso,umaclassedevepoderini-
ciaraexecu çãocomumalgoritmoeomesmosertrocadoposteriormente.
Uma solução que se encaixa nos requisitos descritos é a classe
11

## Página 34

1.3. OPrimeiroProblema:CálculodoValordoEstacionamento CasadoCódigo
ContaEstacionamento delegar a lógica de cálculo para a instância de uma
classe que a compõe. Dessa forma, para trocar o comportamento do cálculo
do valor do estacionamento, basta trocar a classe que está o compondo. Essa
classetambémpoderiaserparametrizadaeserreutilizadanocontextodediversas
empresas.Afigura1.3mostraodiagramaquerepresentaessasolu ção.
Figura1.3:Utilizandoacomposi çãoparapermitiratrocadoalgoritmo
Agoraapresentamosaclasse ContaEstacionamentodelegandoparauma
classe que a compõe o calculo do valor do estacionamento. A interface
CalculoValorabstraioalgoritmodecálculodatarifa. Observequeexisteum
métodoquepermitequeoatributo calculosejaalterado,permitindoamudan ça
dessealgoritmodepoisqueoobjetofoicriado.
public class ContaEstacionamento {
private CalculoValor calculo ;
private Veiculo veiculo ;
private long inicio ;
private long fim ;
public double valorConta() {
return calculo .calcular(fim-inicio, veiculo );
}
public void setCalculo( CalculoValor calculo ){
this.calculo = calculo ;
12

## Página 35

CasadoCódigo Capítulo1. EntendendoPadrõesdeProjeto
}
}
Aseguir,aclasse CalculoDiariamostraumexemplodeumaclassequefaz
ocálculodatarifapordia.Observequeessaclassepossuiumatributoquepodeser
utilizadoparaparametrizarpartesdoalgoritmo.Dessaforma,quandoaestratégia
foralteradaparaocalculodovalorpordia,bastainserirainstânciadessaclasseem
ContaEstacionamento. Valetambémressaltarqueessamesmaclassepodeser
reaproveitadaparadiferentesempresasemdiferentesmomentos,evitandoassima
duplicaçãodecódigo.
Listagem 1.1-Exemplodeclassequefazocálculodatarifa:
public class CalculoDiaria implements CalculoValor {
private double valorDiaria ;
public CalculoDiaria( double valorDiaria ){
this.valorDiaria = valorDiaria ;
}
public double calcular() {
return valorDiaria * Math .ceil(periodo / HORA );
}
}
ReconhecendoaRecorrênciadaSolu ção
Apósimplementarasolu ção,odesenvolvedor,orgulhosodesuacapacidadede
modelagem,começaapensarqueessamesmasolu çãopodeserutilizadaemoutras
situações.Quandohouverumalgoritmoquepodevariar,essaéumaformadeper-
mitirquenovasimplementa çõesdoalgoritmopossamserplugadasnosoftware.Por
exemploocálculodeimpostos,comopodevariardeacordocomacidade,poderia
utilizarumasolu çãoparecida.
Naverdade,eleselembrouquejátinhavistoumasolu çãoparecidaemumsis-
temacomquehaviatrabalhado.Comooalgoritmodecriptografiaqueerautilizado
paraenviarumarquivopelaredepoderiasertrocado,existiaumaabstra çãocomum
atodoselesqueerautilizadapararepresentá-los.Dessaforma,aclassequeenviava
oarquivo,eracompostapelaclassecomoalgoritmo. Sendoassim,odesenvolve-
dordecidiuconversarcomocolegaarespeitodacoincidênciadasolu çãoutilizada.
13

## Página 36

1.4. Strategy:oPrimeiroPadrão! CasadoCódigo
Suasurpresafoiquandoeledissequenãoeraumacoincidência,poisamboshaviam
utilizadoopadrãodeprojeto Strategy.
Eu já usei isso e nem sabia que era um padrão!
Umareaçãocomumquandocertaspessoastêmseuprimeirocontato
compadrõeséverquejáutilizouaquelasolu çãoanteriormente. Issoé
normal,poisopróprionome "padrão”significaqueaquelaéumasolu ção
quejáfoiutilizadacomsucessoemdiversoscontextos.Nessemomento,
algumaspessoaspensam: Para que eu preciso saber os padrões se eu posso
chegar a essas soluções sozinho?.
Observequeparaodesenvolvedorchegaraessasolu çãoeledemorou
umcertotempo.Mesmoassim,podemhaveroutrassolu çõesqueeledei-
xoudeexplorareconsiderar,epodemhaverconsequênciasquemuitas
vezesnãosãolevadasemconta.Aoaprenderpadrões,odesenvolvedor
adquireoconhecimentonãoapenasdaestruturaempregada,massobre
ocontextoemqueeleéutilizadoeastrocasfeitasparaseequilibraros
requisitos.Dessaforma,nãoseenganeachandoqueospadrõesnãoirão
teacrescentarconhecimento,poismesmoosdesenvolvedoresmaisex-
perientesaprendemmuitocomeles.
1.4 Strategy : oPrimeiroPadrão!
“Por mais bonita que seja a estratégia, ocasionalmente deve-se olhar os resultados. ”
–-SirWinstonChurchill
O Strategyéumpadrãoquedeveserutilizadoquandoumaclassepossuir
diversosalgoritmosquepossamserutilizadosdeformaintercambiável. Asolu ção
propostapelopadrãoconsisteemdelegaraexecu çãodoalgoritmoparaumains-
tânciaquecompõeaclasseprincipal. Dessaforma,quandoafuncionalidadefor
invocada,nomomentodeexecu çãodoalgoritmo,seráinvocadoummétododains-
tânciaqueacompõe. AFigura 1.4apresentaumdiagramaquemostraaestrutura
básicadopadrão.
14

## Página 37

CasadoCódigo Capítulo1. EntendendoPadrõesdeProjeto
Figura1.4:EstruturadopadrãoStrategy
Umadaspartesprincipaisdeumpadrãodizrespeitoàssuasconsequências,pois
éapartirdelasqueodesenvolvedorvaiavaliarseessaéumaboaescolhaounão
paraseusrequisitos. Nocasodo Strategy,aprincipalconsequênciapositivaé
justamenteofatodeoalgoritmopoderseralteradosemamodifica çãodaclasse.A
partirdessaestrutura,novasimplementa çõesdelepodemsercriadaseintroduzidas
posteriormente.
Outropontopositivodopadrãoestánofatodalógicacondicionalnaclasseprin-
cipalserreduzida.Comoaescolhadoalgoritmoestánaimplementa çãodoobjeto
queestácompondoaclasse,issoeliminaanecessidadedetercondicionaisparasele-
cionaralógicaaserexecutada.Outraconsequênciapositivaestánofatodeaimple-
mentaçãopodersertrocadaemtempodeexecu ção,fazendoqueocomportamento
daclassepossasertrocadodinamicamente.
Nomundodospadrões,valeaexpressão "nem tudo são flores”,eéimportante
conhecerasconsequênciasnegativasdopadrãoqueestásendoutilizado. Nocaso
do Strategy,issoacontecenoaumentodacomplexidadenacria çãodoobjeto,
poisainstânciadadependênciaprecisasercriadaeconfigurada. Casooatributo
sejanulo,aclassepodeapresentarumcomportamentoinesperado.Outroproblema
dessasoluçãoestánoaumentodonúmerodeclasses:háumaparacadaalgoritmo,
criandoumamaiordificuldadeemseugerenciamento.
1.5 Oque são padrões?
Umpadrãodescreveumconjuntocompostoporumcontexto,umproblemaeuma
solução.Emoutraspalavras,pode-sedescreverumpadrãocomoumasolu çãopara
15

## Página 38

1.5. Oquesãopadrões? CasadoCódigo
umdeterminadoproblemaemumcontexto.Porémumpadrãonãodescrevequal-
quersolução,masumasolu çãoquejátenhasidoutilizadacomsucessoemmaisde
umcontexto.Exatamenteporessemotivoqueadescri çãodospadrõesnormalmente
sempreindicaalgunsdeseususosconhecidos. Umpadrãonãodescrevesolu ções
novas,massolu çõesconsolidadas!
AideiadospadrõesvemdotrabalhodeChristopherAlexandernaáreadear-
quiteturadecidadeseconstru ções[ 5].Nestelivro,cadapadrãotraziaumasolu ção
adequadaaumproblema,quepoderiaserreutilizadaeadaptadaparadiversassi-
tuações.Adissemina çãodospadrõesnacomunidadededesenvolvimentodesoft-
wareiniciou-secomoconhecidolivro "Design Patterns: Elements of Reusable Object-
Oriented Software”[10]. Eledescreviasoluçõesdeprojetoorientadoaobjetosque
sãoutilizadasatéhojepordesenvolvedoresdetodomundo.Esselivrotambéméco-
nhecidocomo GoF,umacrônimode Gang of Four,umareferênciaaosseusquatro
autores.
Paraserumpadrão,umasolu çãonãobastaserrecorrente,masprecisaseruma
boasolução(casocontrárioéumanti-padrão!).Alémdisso,écomumqueelatraga
outraspartes,comoaestruturadasolu ção,comofuncionasuadinâmicaeascon-
sequênciaspositivasenegativasdesuaaplica ção. Outraparteimportanteéore-
lacionamentocomosoutrospadrões,poismostraoutrosqueoferecemumaoutra
alternativa,oupadrõesquepodemcomplementaressasolu çãoparacompensarsuas
desvantagens.
Muitosdesenvolvedoresachamqueopadrãoseresumeàsuaestrutura,normal-
menterepresentadaatravésdeumdiagramadeclasses,eesquecemdetodoorestode
suadescrição.Issoéumusoinadequadodospadrões,poisseasolu çãoforutilizada
nocontextoerrado,elapodeatrapalharmaisqueajudar.Seobservarmostodosos
padrões,épossívelobservarqueaestruturadealgunssãobastantesimilares.Porém
osproblemasqueessasestruturasvãoresolverpodemsercompletamentediferentes.
Poroutrolado,aestruturaapresentadanopadrãoéapenasumareferência,poisé
possívelaplicá-locomdiversasadaptaçõesestruturaisdeacordocomasnecessidades
daaplicação. Époressemotivoqueexistemfortescríticasaferramentaspossuem
umaabordagemdegeraraestruturadepadrõesdeformaautomática.
Padrõesnãoserefletemempeda çosdecódigooucomponentesquesãoreutiliza-
dosdeformaigualemdiversasaplica ções,elessãoumconhecimentoquedeveestar
nacabe çadosdesenvolvedores. Apartirdesseconhecimento,osdesenvolvedores
devemavaliarocontextoeoproblemaquequeremresolvereadaptar,ecombinar
padrõesdeformaaequilibrarasfor çasenvolvidas. Éapartirdesseconhecimento
16

## Página 39

CasadoCódigo Capítulo1. EntendendoPadrõesdeProjeto
queospadrõesajudamosdesenvolvedoresamelhoraremsuahabilidadeemmode-
lagemorientadaaobjetos.
Quanto mais padrões eu utilizar , melhor v ai ficar o
meu código?
Claroquenão! Comoopadrãoéumasolu çãoparaumproblema,
aplicá-loondeoproblemanãoexisteiráapenascomplicarascoisas.Isso
seriacomoparaumapessoaqueacabouaaprenderausarummartelo,
vertodososproblemascomosefossemumprego. Pormaisqueum
parafusopossaparecercomumprego,asolu çãoébemdiferente.
Omesmovaleparaospadrões.Nãoésóporquevocêaprendeuum
novopadrão,queprecisairutilizando-oemtodasassolu ções.Lembre-se
queelestambémpossuemconsequênciasnegativasquepodemsesobre-
poràsvantagensemalgunscasos.Procurepossuirdiversospadrõesem
suacaixadeferramentaseutilizaromaisadequadoparaacadasitua-
ção.Suautiliza çãodesnecessáriapodeserdesastrosaegerarumasobre-
engenhariadosistema,oque,nomínimo,dificultaamanuten çãodocó-
digo.
Ospadrõestambémadicionamàequipeumaterminologiaparasereferirasolu-
çõesdemodelagem,criandoumvocabuláriocompartilhado.Dessaforma,quando
alguémmencionaronomedeumpadrão,todossaberãodoquesetrata.Essenome
nãoserefereapenasàestrutura,masatodasinforma çõesagregadasaele,comosua
dinâmicaesuasconsequências.
Estelivronãoirádescrevê-losemumformatotradicional,masiráutilizá-los
paraexemplificartécnicasquepodemserutilizadasparaprojetarumsoftware.Cada
capítuloiráfocaremumatécnicaouemumtipodeproblema,eentãoserãoapresen-
tadosospadrõesrelacionadoscomexemplosqueirãoilustrarsuaimplementa ção.
Tambémserãodiscutidasasdiferentesalternativasdesolu çãoeasconsequênciaspo-
sitivasenegativastrazidasporcadaumadelas.Oobjetivoéapresentarimportantes
técnicasdeprojetoorientadoaobjetosapartirdaaplica çãodepadrões.
Todosospadrõesapresentadosnolivroutilizarão este estilo,entãotoda
vezquevirumnomenesseestilo,saibaqueestáfazendoreferênciaaumpadrão.Seus
nomesserãomantidoseminglêsdevidoaofatodeseremreferenciadosdessaforma
pelacomunidadededesenvolvimentodesoftwarenoBrasil,sendoqueparamuitos
17

## Página 40

1.6. ComooLivroEstáOrganizado CasadoCódigo
delesnãoexisteumatradu çãoadequada.Oscapítulosdolivropodemserlidosde
formaindependente,porémelespodemfazerreferênciaapadrõesexplicadosem
capítulosanteriores.Paradesenvolvedoresinexperientes,recomenda-sealeiturados
capítulosnaordemdeapresenta ção.
Grandepartedospadrõesutilizadosnesselivrosãooscontidosno[ 10],porém
outrosimportantesdeoutrasfontestambémestãoincluídos.Quandonenhumarefe-
rênciaforprovidacomaprimeiracita çãoaopadrão,issosignificaráqueéumpadrão
desselivro.
ChegandoaosPadrõespelaRefatora ção
Existembasicamenteduasformasparaseimplementarospadrõesnoseucódigo.
Aprimeiradelas,éasuaintrodu çãonamodelagemantesdocódigoserdesenvol-
vido.Nessecaso,éfeitaumaanálisepreliminardoproblema,emqueéidentificado
ocontextonoqualéadequadaaaplica çãodopadrão.Aoutraabordageméatravés
darefatoração[12],umatécnicanoqualocódigoéreestruturadodeformaanãoha-
vermodificaçãodeseucomportamento.Nessecontexto,ocódigojáfoidesenvolvido
porémapresentaalgumtipodedeficiênciaemtermosdeprojeto,situa çãoconhecida
comomaucheiro. Sendoassim,ocódigovaisendoalteradoempequenospassos
atéquesechegueaopadrãoalvo.
Sabercomoutilizarrefatora çãoparasechegarapadrõeséumatécnicaimpor-
tante[16],poisnemsempreasolu çãomaisadequadaéaqueéempregadanapri-
meiravez.Esselivroiráapresentar,juntamentecomospadrões,comopodesurgir
anecessidadedesuaaplica çãoemumcódigoexistenteequaisospassosderefato-
raçãoquepodemserfeitosparasuaimplementa ção.Noexemploapresentadonesse
capítulo,foimostradoumcódigoproblemáticojáexistentequefoirefatoradopara
implementaropadrão Strategy.Ospassosdarefatora çãoparaeleserãomostra-
dosnoCapítulo3.
1.6 Como o LivroEstá Organizado
Estaseçãoiráfecharessecapítuloinicial,falandoumpoucosobreaorganiza çãodo
livro.Aquiospadrõessãoapresentadosdeumaformadistintadeoutroslivros.Os
capítulossãoorganizadosdeacordocomoprincípiodedesignutilizadopelopa-
drão.Dessaforma,elesservirãoparaexemplificartiposdeproblemaquepodemser
resolvidoscomaquelatécnica.Serãoapresentadosexemplos,quealémdemostrar
aaplicaçãodopadrãodeformapráticatambémirãoilustrarcomoelespodemser
18

## Página 41

CasadoCódigo Capítulo1. EntendendoPadrõesdeProjeto
combinados.
OCapítulo2come çaexplorandodeformamaisprofundaautiliza çãodehe-
rançaequaissãoospadrõesquefazemusodesseprincípioparapermitiraexten-
sãodecomportamento. Deformacomplementar,oCapítulo 3contrastaousoda
herançacomousodacomposi ção,ressaltandoasprincipaisdiferen çasentreelas.
Nesseponto,diversospadrõesquefazemusodacomposi çãoserãoapresentados,
inclusivedeformacombinadacomaheran ça.
Seguindoalinhaderaciocínio,oCapítulo 4apresentaacomposi çãorecursiva,
ecomoelapodeserutilizadaparafacilitaroreaproveitamentodecódigo.Apartir
dospadrõesqueutilizamesseprincípioépossívelcombinarocomportamentode
diversasclassesdeformasdiferentes,obtendoumagrandequantidadedepossibili-
dadesdecomportamentofinal.Emseguida,oCapítulo 5mostracomoacomposi ção
recursivatambémpodeserutilizadaparaoencapsulamentodeobjetos,deformaa
permitirquefuncionalidadessejamadicionadasnaclassedeformatransparenteaos
seusclientes.
OCapítulo6tratadacria çãodeobjetosedosdiferentespadrõesquepodem
serutilizadospararesolverproblemas,comoumalógicadecria çãocomplexaoua
criaçãodeobjetosdeclassesrelacionadas.Aindatratandodessetema,oCapítulo 7
abordaquestõesdemodularidadedentrodaaplica ção,apresentandodiferentestéc-
nicasparapermitirqueumaclasseobtenhaainstânciadeoutrasemdependerdi-
retamentedela.Issopermitequenovasimplementa çõespossamserplugadassema
necessidadederecompilaraaplica ção.
Emseguida,enquantooscapítulosiniciaisapresentaramtécnicasparaalterara
implementaçãoe,consequentemente,ocomportamentodefuncionalidadesexisten-
tes,oCapítulo8mostratécnicasparaquenovasfuncionalidadeseopera çõespossam
seradicionadasemclassesexistentes.E,deformacomplementar,oCapítulo 9mos-
tracomoacomplexidadedeumagrandeaplica çãopodesergerenciadaatravésda
criaçãodesubsistemasedoencapsulamentodagerênciadacomunica çãoentreos
objetos.
Finalizandoolivro,oCapítulo 10nãoapresentanenhumnovopadrão,masal-
gunstópicosavan çadosecomplementaresaoquefoiapresentadoaolongodetodo
livro.Essestópicosincluemquestõessobreodesenvolvimentodeframeworks,uti-
lizaçãodetiposgenéricosempadrõesedautiliza çãodepadrõesemumprocesso
TDD.Porfim,eleterminafalandoumpoucodaculturadacomunidadequeexiste
noBrasilenomundoparaoestudoeidentifica çãodenovospadrões.
19

## Página 42

Capítulo2
ReusoAtravésdeHerança
“Entidades de software devem ser abertas a extensão, mas fechadas a modificação. ”
–BertrandMeyer
Aherançaéumadasprincipaisfuncionalidadesdelinguagensorientadasaob-
jetos.Éapartirdelaqueépossívelgrandepartedopotencialdereúso.Oproblema
équemuitagentequedizissoparaporaíaindabuscaoreúsoatravésdaheran çade
formaerrada.
Oprimeiropensamentoquenormalmentetemosaoseestenderumaclasseé
reutilizaralógicadasuperclassenasubclasse. Seráqueissoémesmoverdade? O
queumasubclassepodereutilizardasuperclasse?Aestruturadedados?Seusméto-
dos?Areutiliza çãodaestruturadedadosnaheran çanãoémuitoimportante,pois
simplesmenteinstanciandoeutilizandoumaclasseissoépossíveldeserfeito.Auti-
lizaçãodosmétodosdasuperclassepelasubclasseéequivalenteaoreúsodefun ções
naprogramaçãoestruturada,nãosendotambémgrandenovidade.
Opotencialdereúsopossívelcomheran çaestáemoutrolocal!Elepodeestar
simnoreúsodecódigodasuperclasse,porémnãoécomasubclassechamandomé-

## Página 43

2.1. ExemplodePadrãoqueUtilizaHeran ça-NullObject CasadoCódigo
todosdasuperclasse,mascomasuperclassechamandocódigodasubclasse.Quando
ummétododasuperclassechamaummétodoquepodeoudeveserimplementado
nasubclasse,issopermitequeummesmoalgoritmopossaserreutilizadocompas-
sosalterados.Essaflexibilidadeaumentaopotencialdereutiliza çãopoispermitea
suaadaptaçãoparanecessidadesmaisespecíficas.
Outrolocalondeocódigopodeserreusadoénasclassesqueutilizamumavariá-
velcomotipodasuperclasse.Nessecaso,comoasinstânciasdassubclassespodem
seratribuídasaessavariável,épossíveladaptarocomportamentosegundoains-
tânciautilizada.Resumindoemapenasumapalavra:polimorfismo!Porexemplo,
oalgoritmodeordena çãodelistaspodeserreutilizadoemdiversasaplica çõespara
ordenaçãodelistasdediversasclasses.Issosóépossívelpoistodasasclassescom-
partilhamamesmaabstra çãodotipoComparable.
Oobjetivodessecapítuloémostrarcomoaheran çapodeserutilizadaemum
designorientadoaobjetosparapermitiradapta çãodecomportamentoeconsequen-
tementeummaiorreúso.Issoseráfeitoapresentandopadrõesqueutilizamosprincí-
piosdaheran çadescritosecomoelespodemserutilizadosparacria çãodesolu ções.
2.1 Exemplo de Padrão que UtilizaHerança -N ull
Object
“O que é invisível para nós é também crucial para nosso bem estar. ”
–JeanetteWinterson
Paracomeçarafalardeheran ça,essase çãoapresentaumpadrãobemsimples,
porémbastanteútil. ApesardenãotersidoincluídonoGoF,emumaentrevista
recente,umdosautoresconfessouqueocolocariaemumahipotéticasegundaedi ção
dolivro[ 20]. Eleiráilustrarcomocomousodaheran çaépossível "enganar”o
códigoqueutilizaaclasse,introduzindoumnovocomportamentoqueiráeliminar
anecessidadedousodecondicionais.Comoparaocódigoclienteocomportamento
daclasseéinvisível,odinamismodessecomportamentopodeserachaveparase
lidarcomsitua çõesdiferentes.
Voucomeçarcitandoumasitua çãoquecertamentemuitosjáviramemalgum
código que trabalharam. A classeApresentacaoCarrinho apresentada na
listagemaseguirchamaométodo criarCarrinho()daclasse CookieFactory
pararecuperarumcarrinhopreviamentecriadopelousuárioapartirdoscookies
armazenados em seu navegador. Uma vez tendo os valores recuperados, são
22

## Página 44

CasadoCódigo Capítulo2. ReusoAtravésdeHerança
definidosatributosparaaexibi çãodasinforma çõesdocarrinhonapartesuperior
da página do usuário. O grande problema desse código é que, caso nenhum
carrinhotenhasidocriado, eleretornaumvalornulo. Daíéprecisoadicionar
condicionaisparaconfigurarosvaloresadequadosparaquandoocarrinhofornulo.
Listagem 2.1-CondicionaisparaProte çãodeValoresNulos:
public class ApresentacaoCarrinho{
public void colocarInformacoesCarrinho( HTTPServletRequest request ) {
Carrinho c = CookieFactory .criarCarrinho(request);
if(c != null ) {
request.setAttribute("valor", c .getValor());
request.setAttribute("qtd", c .getTamanho());
} else {
request.setAttribute("valor", 0.0);
request.setAttribute("qtd", 0);
}
if(request.getAttribute("username") == null ) {
if ( c != null ) {
request.setAttribute("userCarrinho",
c.getNomeUsuario());
} else {
request.setAttribute("userCarrinho",
"<a href=login.jsp>Login</a>" );
}
} else {
request.setAttribute("userCarrinho",
request.getAttribute("username"));
}
}
}
Seesseproblemasetornarrecorrente,elepodeserumaverdadeiracatástrofena
legibilidadedocódigodeumaaplica ção.Écomumvercondicionaisrepetidospara
trataremváriospontosapossibilidadedeumadeterminadavariávelsernula.Esses
condicionaisgarantemaseguran çadocódigoapenasnaqueleponto,poisnadaga-
rantequeessevalorserátratadoadequadamenteemoutroslocais.Mascomoentão
fazerparaprotegerminhaaplica çãodeum NullPointerExceptionsemprecisar
recorreraessetipodecondicional?
23

## Página 45

2.1. ExemplodePadrãoqueUtilizaHeran ça-NullObject CasadoCódigo
CriandoumaClasseparaRepresentarValoresNulos
Opadrão Null Object [27]propõeacria çãodeumaclassepararepresentar
objetosnulosemumaaplica ção.Essaclassedeveestenderaclasseoriginaleimple-
mentarseusmétodosdeformaaexecutarocomportamentoesperadodaaplica ção
quandoumvalornuloforrecebido. Dessaforma,emvezdeseretornarumvalor
nulo,retorna-seumainstânciadessanovaclasse.
Aclasse CarrinhoNuloapresentadanalistagemaseguirexemplificaacria ção
deum Null Object paraessecontextoo. Observequeosmétodosretornam
exatamenteosvaloresqueeramconfiguradosparaocasodocarrinhosernulo.
Nesseexemplo,apenasvaloressãoretornados,porémemoutroscasoséprecisoter
umalógicaaserexecutadadentrodosmétodos.
Listagem 2.2-DefiniçãodaClasseparaRepresentaroCarrinhoNulo:
public class CarrinhoNulo extends Carrinho {
public double getValor(){
return 0.0;
}
public int getTamanho(){
return 0;
}
public String getNomeUsuario(){
return "<a href=login.jsp>Login</a>" ;
}
}
Nalistagemaseguir,épossívelobservarcomoocódigoficamaissimplescom
aeliminaçãodaparteresponsávelpelotratamentodosvaloresnulos. Outracoisa
queprecisariaseralteradaéaprópriaclasse CookieFactoryquedeveretornar
umainstânciade CarrinhoNuloemvezde nullquandonenhumcarrinhodo
usuárioforencontrado.
Listagem 2.3-Códigoapósaintrodu çãodoNullObject:
public class ApresentacaoCarrinho{
public void colocarInformacoesCarrinho( HTTPServletRequest request ) {
Carrinho c = CookieFactory .criarCarrinho(request);
24

## Página 46

CasadoCódigo Capítulo2. ReusoAtravésdeHerança
request.setAttribute("valor", c .getValor());
request.setAttribute("qtd", c .getTamanho());
if(request.getAttribute("username") == null ) {
request.setAttribute("userCarrinho", c .getNomeUsuario());
} else {
request.setAttribute("userCarrinho",
request.getAttribute("username"));
}
}
}
Umaconsequênciainteressantedaaplica çãodessepadrãoéqueeleresolveo
problemadotratamentodevaloresnulosemqualquerpontodaaplica çãoqueutilize
essaclasse.Pormaisqueométodoapresentadonoexemplotratasseessesvalores,a
mesmasituaçãopoderiaacontecerempartesdocódigoquenãoofazem,gerandoa
possibilidadedeerro.Apesardasvantagens,otratamentodosvaloresnulosnãofi-
camexplícitoseissopodegerarumacertaconfusãonahoradeleredarmanuten ção
nessecódigo.
OUsodaHeran çanoNullObject
Umadascoisasinteressantesdesseexemploécomoocódigoqueutilizavao
Null Object desconheciacompletamentequeeleestavaali.Eleconheciaapenas
ainterfacedasuperclasse,masutilizouasfuncionalidadesdasubclasse.Naverdade,
esseéoprincipalmotivoparaautiliza çãodaheran çanoprojetodeumsoftware:
ousodopolimorfismo.Comeleépossívelreutilizarocódigoclienteparadiversas
implementações.Inclusive,umbomtesteparaverificarseousodeheran çaéade-
quadoemumadeterminadasitua çãoéversefazsentidosubstituiraimplementa ção
porumadesuassubclassesemtodososcontextos.
25

## Página 47

2.2. HookMethods CasadoCódigo
Herdar ou não herdar de JPanel?Eis a questão!
Euvejoessaquestãodautiliza çãoounãodaheran çaénodesen-
volvimentodeaplica çõesdesktopemSwing.Aosecriarumanovatela
paraaplicação,umadúvidacomuméseessaclassedeveestenderaclasse
JPanelousimplesmenteutilizá-la.Aextensãode JPanelpodefazer
sentidoaprincípio,vistoqueanovaclasseseráumpainel(obedecendoa
famosaregra "é um”)equepodeseradicionadaemumainterfacegráfica.
Poroutrolado,sepensarmosnosprincípiosdaheran ça,umasub-
classedevepoderserutilizadanolugardesuasuperclasse.Raciocinando
dessaforma,émuitofácilpensaremdiversassitua çõesemqueaclasse
comateladeumaaplica çãonãofariasentidodeserutilizadanolugar
deumpainelgenérico.Issotambémquebrariaocontratodasuperclasse,
vistoquediversosmétodos,comoparaadi çãodecomponenteseconfi-
guraçãodelayoutdeixariamdefazersentido.
Somenteverificarseasubclasse é umasuperclassepodenãosersufici-
ente.Antesdeutilizarheran çaverifiqueseopolimorfismofazsentido,ou
seja,sequalquersubclassepodeserutilizadanolugardasuperclasse.Em
casonegativo,issoéumindíciodequeaheran çaestásendoutilizadade
formainadequada.Esseéconhecidocomoo PrincípiodeSubstitui ção
deLiskov,quedefendequeseumaclasseéumsubtipodeoutra,então
osobjetosdessaclassepodemsersubstituídospelosobjetosdosubtipo
semquesejanecessárioalteraraspropriedadesdoprograma.
O NullObjectéumpadrãoquedemonstrabemessacaracterísticasdahe-
rança,poiselepermitequeocódigoclientepossaserutilizado,mesmoparaocaso
deumobjetonulo.Observequeoutrasimplementa çõesde Carrinho,comoum
quetalvezacessainforma çõesremotamente,tambémpoderiamserretornadaspela
fábricaeutilizadaslivremente.
2.2 HookMethods
Umimportanteusoquepodeserfeitodaheran çaéparapermitiraespecializa ção
decomportamento. Dessaforma,asuperclassepodefornecerumabaseparauma
determinadafuncionalidade,aqualinvocaummétodoquesomenteédefinidopela
26

## Página 48

CasadoCódigo Capítulo2. ReusoAtravésdeHerança
superclasse. Essemétodofuncionacomoumpontodeextensãodosistemaécha-
madodemétodo-gancho,oueminglês,hookmethod.
AFigura2.1representaoconceitode hook method.Asuperclassepossuiummé-
todoprincipalpúblicoqueéinvocadopelosseusclientes.Essemétododelegaparte
desuaexecu çãoparao hook method,queéummétodoabstratoquedeveserimple-
mentadopelasubclasse.Elefuncionacomoum“gancho”noqualumanovalógica
deexecuçãoparaaclassepodeser“pendurada”.Cadasubclasseoimplementapro-
vendoumalógicadiferente.Comoessalógicapodeserinvocadaapartirdomesmo
métodopúblico,definidonasuperclasse,os hook methodspermitemqueoobjeto
possuaumcomportamentodiferentedeacordocomasubclasseinstanciada.
Figura2.1:RepresentaçãodeHookMethods
Essapráticaémuitoutilizadaemframeworksparapermitirqueasaplica ções
possamespecializarseucomportamentoparaseusrequisitos. Nessecaso,ofra-
meworkprovêalgumasclassescom hook methodsqueprecisamserespecializadas
pelaaplicação.Sendoassim,aaplica çãodeveestenderessaclasseeimplementaro
hook methoddeformaainserirocomportamentoespecíficodeseudomínio.Ima-
gine,porexemplo,umframeworkquerealizaoagendamentodetarefas. Usando
27

## Página 49

2.3. Revisandomodificadoresdemétodos CasadoCódigo
essaestratégiaelepoderiaproverumaclasseparaserestendida,naqualprecisaria
serimplementadoum hook methodparaadefiniçãodatarefadaaplica ção.Enquanto
isso,naclassedoframeworkestariaalógicadeagendamentoquechamariaométodo
definidopelaaplica çãonomomentoadequado.
UmexemplodeusodessatécnicaestánaServletsAPI[ 21],naqualumservlet
precisaestenderaclasse HTTPServlet.Essaclassepossuiométodo service()
queéinvocadotodavezqueeleprecisatratarumarequisi çãoHTTP.Essemétodo
chamaoutrosmétodos,como doPost()ou doGet(),queprecisamserimple-
mentadospelasubclasse.Neleseladeveinseriralógicaaserexecutadaparatratara
requisiçãorecebida.Nessecaso,essesmétodospossuemumaimplementa ção default
vaziaeprecisamserimplementadossomentesenecessário.
2.3 Revisando modificadores de métodos
Quandoaprendemosobásicodalinguagem,aprendemosmodificadoresdeacessoe
outrostiposdemodificadoresdemétodosequaloseuefeitonasclasses.Oquenem
todoscompreendeméquandocadaumdelesprecisaserutilizadoequalotipode
mensagemquesepassacomcadaumemtermosdedesign.Aseguirestãorelacio-
nadosalgunsmodificadoresdeacessoequalorecadoqueumaclassemandapara
duassubclassesquandoutilizacadaumdeles:
•abstract:Ummétodoabstratoprecisaobrigatoriamenteserimplementado
emumasubclasseconcreta.Issosignificaqueesseéum hook methodquefoi
definidonasuperclasseeobrigatoriamenteprecisaserdefinido.
•final:Deformacontrária,ummétododotipofinalnãopodesersobrescrito
pelassubclasseseporissonuncairárepresentarum hook method.Essesmé-
todosrepresentamfuncionalidadesdaclassequeprecisamserimutáveispara
seubomfuncionamento. Costumamserosmétodosqueinvocamos hook
methods.
•private:Osmétodosprivadossópodemserinvocadosdentrodaclasseque
sãodefinidos. Dessaforma,elesrepresentammétodosdeapoiointernosda
classeenuncapoderãosersubstituídospelasubclassecomoum hook method.
•protectede public:Todososmétodospúblicoseprotegidos,desdeque
nãosejam final,sãocandidatosa hook method. Éissomesmo! Qualquer
28

## Página 50

CasadoCódigo Capítulo2. ReusoAtravésdeHerança
métodoquepodesersobrescritonasubclassepodeserutilizadoparaain-
serçãodecomportamento.Algumasclassespossuemimplementa çõesvazias
paraessesmétodos,oquefazcomquesejam hook methodscomimplementa-
çãoopcionalpelassubclasses.
Aocriarumaestruturadeclasses,éimportantecolocarosmodificadorescor-
retosnosmétodosdeformaapassaramensagemcertaparaasclassesqueforem
estendê-la.Porexemplo,seummétodoquecoordenaachamadade hook methods
forsobrescrito,elespodemnãoserchamadosealgumaspremissasassumidasna
superclassepodemnãosermaisverdadeiras. Porissoéprecisomuitocuidadoao
proverumaclasseparaserestendidacomopartedaAPIdeumcomponenteoufra-
mework.
2.4 Passos diferentes na Mesma Ordem -T emplate
Method
“No meio do caminho tinha uma pedra / tinha uma pedra no meio do caminho /
tinha uma pedra / no meio do caminho tinha uma pedra. ”
–CarlosDrummonddeAndrade
O principal padrão que utilizahook methods como técnica é oTemplate
Method. Estepadrãoéaplicávelquandosedesejadefinirumalgoritmogeral,que
estabeleceumasériedepassosparacumprirumrequisitodaaplica ção.Porém,seus
passospodemvariareédesejávelqueaestruturadaimplementa çãoforne çauma
formaparaqueelessejamfacilmentesubstituídos.
Imagine,porexemplo,comoseriasefôssemosdefinirumalgoritmoparaaspes-
soasacordaremeiremaotrabalho.Essealgoritmoenvolveriaa çõescomoacordar,ir
aobanheiro,comeralgumacoisa,trocarderoupaeselocomoveratéotrabalho.De-
pendendodapessoacadaumdospassospodeserdiferente,comootipoderoupa
quecolocamparairaotrabalhoouoquecomempelamanhã. Nalocomo çãoao
trabalho,algunspodemirdetransportepúblico,outrospodemiremseucarroe
atémesmoapéoudebicicleta.Pormaisquecadaumdospassossejadiferente,o
algoritmoqueosutilizaacabasendoomesmo.
EstruturadoTemplateMethod
Paraentenderaestruturado Template Method vamosutilizarcomometá-
foraalgofamiliaramuitaspessoas:modelosdedocumento.Conformeilustradona
29

## Página 51

2.4. PassosdiferentesnaMesmaOrdem-TemplateMethod CasadoCódigo
Figura2.2,ummodelodedocumentodefinealgumaspartesquesãofixaseoutras
partesquedevemserintroduzidasquandoodocumentopropriamenteditoforcri-
ado.Sãolacunasqueprecisamsercompletadasequeirãovariardedocumentopara
documento.Omodeloprovêumaestruturaquepodeserfacilmentereaproveitada,
simplificandosuacria ção.
Figura2.2:UsodeTemplatesparaDocumentos
Deformasimilar,um Template Method éummodelodealgoritmoquepos-
suialgumaspartesfixasealgumaspartesvariáveis.Aspartesvariáveissãolacunas
queprecisamsercompletadasparaqueoalgoritmofa çarealmentesentido.Aslacu-
nassãorepresentadascomo hook methodsquepodemserimplementadosnassub-
classes.Casosejaumalacunaobrigatória,ométododeveserdefinidocomoabstrato
ecasoaimplementa çãosejaopcional,ométodopodeserconcretoenormalmente
possuiumaimplementaçãovazia.Oalgoritmoérepresentadoatravésdeummétodo
nasuperclassequecoordenaaexecu çãodos hook methods.
A Figura 2.3 apresenta a estrutura do padrãoTemplate Method. A
ClasseAbstratarepresentaasuperclassequeimplementao TemplateMethod
equedefinequaissãoos hook methods. A ClasseConcretarepresentaaclasse
queherdao Template Method da ClasseAbstrataedefineumaimplemen-
taçãoconcretados hook methods. Aclasserepresentadacomo Clienteinvocao
metodoTemplate().Observequeapesardotipodavariávelserdotipodaclasse
abstrata,otipoinstanciadoéodasubclassequeimplementaospassosconcretosdo
algoritmo.
30

## Página 52

CasadoCódigo Capítulo2. ReusoAtravésdeHerança
Figura2.3:EstruturadoPadrãoTemplateMethod
Qual a diferença entre HookMethods e o Template
Method?
Muitaspessoasnessepontopodemestarachandoque Hook Methods
eopadrão Template Method sãoamesmacoisa.Agrandediferen ça
équeos Hook Methodssãoumatécnicaparapermitiraextensãodecom-
portamentoeo Template Method,comoumpadrão,éumasolu ção
paraumproblemamaisespecífico.Seriacorretodizerqueo Template
Methodutiliza Hook Methodsemsuasolu ção.Oqueéimportanteper-
ceberéqueoconceitode Hook Methodémaisgeraleinclusiveéutilizado
poroutrospadrõesqueserãovistosmaisàfrentenesselivro.
SerializandoPropriedadesemArquivos
Imaginequeemumaaplica çãoprecisamospegarmapasdepropriedadesese-
rializaremarquivos. Aquestãoéqueoformatoemqueaspropriedadesprecisam
31

## Página 53

2.4. PassosdiferentesnaMesmaOrdem-TemplateMethod CasadoCódigo
serestruturadassãodiferentes.Porexemplo,podeserpossívelestruturarasinfor-
maçõesemarquivosXMLeemarquivosdepropriedades. Alémdisso,osarqui-
vospodemprecisarreceberumpós-processamento,comoumacriptografiaouuma
compactação.Paraoexemploqueseráapresentadoiremosconsiderarqueexistem
duaspossibilidades:acria çãodoarquivoXMLcompactadoeacria çãodoarquivo
depropriedadescriptografado.
Comonessecasotemosumalgoritmobaseemqueospassospodemsermodifi-
cadosdeacordocomaimplementa ção,esseéumcenárioadequadoparaimplemen-
taçãodopadrão Template Method. Aclasse GeradorArquivo,apresentada
nalistagemaseguir,possuiométodo gerarArquivo()quedefineumalgoritmo
baseparaacria çãodoarquivo,invocandoosdoismétodosabstratos processar()
e gerarConteudo().Essemétodopossuiomodificador finalparaqueelenão
possasersobrescritonassubclasses. Notequeométodo processar()fornece
umaimplementação defaultqueretornaopróprioarraydebytes,representandoo
casoemquenãoexisteprocessamentoadicionalapósoarquivosergerado.Diferen-
temente,ométodo gerarConteudo()éabstratoeobrigatoriamenteprecisaráser
implementado.
Listagem 2.4-ClassequedefineoTemplateMethod:
public abstract class GeradorArquivo {
public final void gerarArquivo( String nome ,
Map<String, Object > propriedades )
throws IOException {
String conteudo = gerarConteudo (propriedades);
byte[] bytes = conteudo .getBytes();
bytes = processar (bytes);
FileOutputStream fileout = new FileOutputStream (nome);
fileout.write(bytes);
fileout.close();
}
protected byte [] processar( byte[] bytes ) throws IOException {
return bytes ;
}
protected abstract String
gerarConteudo(Map<String, Object > propriedades );
}
32

## Página 54

CasadoCódigo Capítulo2. ReusoAtravésdeHerança
Asduaspróximaslistagensapresentamasclasses GeradorXMLCompactado
e GeradorPropriedadesCriptografado que implementam a classe
GeradorArquivo, fornecendo uma implementação para os passos do al-
goritmos definidos na superclasse. A primeira implementação, no método
gerarConteudo() cria um arquivo XML no qual existe uma tag chamada
<properties>ecadapropriedadeéumelementodentrodessatag. Ométodo
processar()usaaclasse ZipOutputStreamparagerarumarquivocompac-
tado.Jánasegundalistagem,ométodo gerarConteudo()criaaestruturadeum
arquivodepropriedadesemquecadalinhapossuioformato propriedade=valor.O
métododeprocessamentocriptografaosbytesdoarquivoutilizandoumalgoritmo
simpleschamadocifradeCésar,emqueovalordecadabyteédeslocadodeacordo
comoparâmetro delay.
Listagem 2.5-ClassequegeraoarquivocomXMLcompactado:
public class GeradorXMLCompactado extends GeradorArquivo {
protected byte [] processar( byte[] bytes ) throws IOException {
ByteArrayOutputStream byteOut = new ByteArrayOutputStream ();
ZipOutputStream out = new ZipOutputStream (byteOut);
out.putNextEntry(new ZipEntry ("internal"));
out.write(bytes);
out.closeEntry();
out.close();
return byteOut .toByteArray();
}
protected String gerarConteudo( Map<String, Object > props ) {
StringBuilder propFileBuilder = new StringBuilder ();
propFileBuilder.append("<properties>");
for(String prop : props .keySet()){
propFileBuilder.
append("<"+prop+">"+props.get(prop)+"</"+prop+">");
}
propFileBuilder.append("</properties>");
return propFileBuilder .toString();
}
}
Listagem 2.6-Classequegeraarquivodepropriedadescriptografado:
33

## Página 55

2.4. PassosdiferentesnaMesmaOrdem-TemplateMethod CasadoCódigo
public class GeradorPropriedadesCriptografado extends GeradorArquivo {
private int delay ;
public GeradorPropriedadesCriptografado( int delay ) {
this.delay = delay ;
}
protected byte [] processar( byte[] bytes ) throws IOException {
byte[] newBytes = new byte [bytes.length];
for(int i =0;i<bytes.length;i++){
newBytes[i]= ( byte) (( bytes[i]+delay) % Byte .MAX_VALUE);
}
return newBytes ;
}
protected String gerarConteudo( Map<String, Object > props ) {
StringBuilder propFileBuilder = new StringBuilder ();
for(String prop : props .keySet()){
propFileBuilder.append(prop+"="+props.get(prop)+"\n");
}
return propFileBuilder .toString();
}
}
ConsequênciasdoUsodoTemplateMethod
Peloexemploapresentadoepeladescri çãodopadrão,épossívelperceberque
como Template Method podemosreaproveitarocódigorelativoàpartecomum
deumalgoritmo,permitindoquecadapassovariávelpossaserdefinidonasubclasse.
Issotambéméumaformadepermitirqueafuncionalidadedaclassequedefineo
algoritmobásicosejaestendida.Assimépossíveldefinirumafuncionalidademais
geralnaqualpodeserfacilmenteincorporadaaparteespecíficadodomíniodaapli-
cação.Éimportantelembrarqueosmodificadoresadequadosdosmétodosdevem
serutilizadosparaimpedirqueocontratodasuperclassecomosseusclientesseja
quebrado.
Porém,comofoiditonoprimeirocapítulo,ousodaheran çanessepadrãotam-
bémtrazalgumaslimita ções.Aprimeiraéqueaheran ça "é uma carta que só pode
ser jogada uma vez”,issosignificaqueumaclassequeprecisedecomportamentosde
duasoutrasclassessópoderáfazerousodaheran çaparaumadelas.Essaquestão
34

## Página 56

CasadoCódigo Capítulo2. ReusoAtravésdeHerança
serámelhordiscutidanoCapítulo 3. Outraquestãoéquedepoisqueumaimple-
mentaçãoforinstanciadanãoserámaispossívelalterarospassosdoalgoritmo.
Aoutilizarumpadrão,éprecisoavaliarparaosrequisitosdesuaaplica çãoquais
consequênciaspesammaisoumenos.Apartirdessasinforma çõesépossíveldecidir
seseuusoseráounãoadequado. Ressaltoqueomaiorproblemadeumasolu ção
quepossuilimita çõeséquandoelassãodesconhecidaspelodesenvolvedores,pois
quandosetemconsciênciadesuaexistênciaépossívelgerenciaroriscooutratá-las,
muitasvezesapartirdeoutrospadrões.
2.5 Refatorando na Direção da Herança
Muitasvezes,osrequisitosquedirecionamodesenvolvimentoparaousodaheran ça
nãosurgemtodosaomesmotempo.Outrasvezes,simplesmentenãosevisualizano
momentoqueseestáprogramandoqueaquelepadrãopodeajudarnasolu ção.Nes-
sescasos,opadrãopodeseralcan çadoapartirderefatora ções.Aideiaéconseguir,
apartirdepequenospassos,irmodificandoaospoucosaestruturadasolu ção,sem
modificaroseucomportamento. Valeressaltarqueéextremamenterecomendado
quearefatora çãosejaapoiadaporumasuítedetestesautomatizados,quedevem
serexecutadosacadapassodarefatora çãoparaverificarseocomportamentofoi
mantido.
Demolindo tudo que foi criado e reconstruindo do
zero
Umgrandeerroaoserefatorarumcódigoédestruirtodaasolu ção
existenteereconstruirdozeroumanovasolu ção. Issoéruimpoisdu-
ranteumlongoperiododetempoperde-seareferênciadostestesauto-
matizados,quedãoofeedbackseocomportamentoestásendomantido
inalterado.Nodecorrerdesselivro,serãoapresentadosospassosquede-
vemserseguidosparaserefatorarasolu çãonadire çãodospadrõesapre-
sentados.Comisso,pretende-semostrarcomoquecomumasequência
depequenasmudan çaspode-sealcan çarumgrandeimpactonaquali-
dadedocódigoenamodelagemdaaplica ção.
Nocasodenecessidadedeserefatorarparaousodaheran ça,existemdoiscená-
riosdiferentes.Noprimeiro,todaafuncionalidadefoiacumuladaemapenasuma
35

## Página 57

2.5. RefatorandonaDireçãodaHeran ça CasadoCódigo
classe,quepossuiumgrandenúmerodecondicionaiseumcódigodedifícilmanu-
tenção. Osegundocenárioocorrequandofuncionalidadescomsimilaridadesnos
algoritmossãoimplementadasemdiferentesclasses,gerandoduplica çãodecódigo.
AFigura2.4apresentaospassosparaarefatora çãoquandoumaúnicaclasse
concentraemummétodotodasaspossibilidadesdoalgoritmoutilizandocondici-
onais. Aprimeiraetapaéextrairosmétodosdeacordocomospassosquedevem
serrealizadospeloalgoritmo.Apósaextra ção,cadamétodoaindapossuiráalógica
condicionalnecessáriaparatodosospossíveiscaminhos.Naetapaseguinteécriada
umasubclassepararepresentarumaalternativadeexecu çãodoalgoritmoeospassos
seguintesconsistememmoverafuncionalidadeparaessasubclasse.Esseprocesso
vaisendorepetidoatéquecadapossívelcaminhosejamovidoparaumasubclassee
somentealógicamaisgeralestejaconcentradanasuperclasse.
Paraqueissosejafeito,oprimeiropassoésobrescreverosmétodosextraídos
nanovasubclassecriada.Aprincípio,essesmétodosaindairãodelegaraexecu ção
dasuafuncionalidadeparaasuperclasse,fazendoumachamadaaométodooriginal
naforma super.orginal().Casoexistaalgumparâmetrosetadonasuperclasse
paraaescolhadospassosdoalgoritmo,elepodeserconfiguradodeformafixana
subclasse,deacordocomoqueseráimplementadonela.Aetapaseguinteconsiste
emmoverparaasubclassealógicarelativaaosmétodoscomospassosdoalgoritmo.
Deveserretiradoocondicionalnasuperclasse,juntamentecomocódigoaserexe-
cutado,einseridonométododasubclasse,quenãodevemaisdelegarsuaexecu ção
parasuperclasse.Esseprocedimentodeveserfeitométodopormétodo.Emseguida,
osmesmospassosdevemserrepetidosparaacria çãodenovassubclasses,atéque
nãoexistamaislógicanessesmétodosdasuperclasse. Nocasodenãohaveruma
implementação default,elesdevemsetornarabstratos.
36

## Página 58

CasadoCódigo Capítulo2. ReusoAtravésdeHerança
Figura2.4:Quebrandoclasseúnicacommétodograndeecomplexo
Aoutrapossibilidadederefatora çãodeveserrealizadaquandoexistiremduas
classesqueimplementamalgoritmossimilaresepossuamcódigoduplicado. Con-
formeestáapresentadonaFigura2.5,arefatora çãoirálevararefatora çãonadire ção
dadefiniçãodeumasuperclassecomumqueimplementaum Template Method.
Aprimeiracoisaqueprecisaserfeitaéaextra çãodemétodoscomaspartesquedife-
37

## Página 59

2.5. RefatorandonaDireçãodaHeran ça CasadoCódigo
renciamumalgoritmodooutro.Depoisdessaetapa,ocódigointernodosmétodos
principaisdeveserigualetodasasdiferen çasdevemestarnosmétodosextraídos.
Emseguida,parauniformizarasclasses,éprecisorenomearosmétodosparaque
fiquemcommesmonomeemesmaassinaturaemambasasclasses(incluindotipos
deparâmetroseexce ções).Deve-sebuscarnomesquerepresentembemapartedo
algoritmoabstraídaporeles.
Figura2.5:Criandosuperclasseparaduasclassescomcódigoduplicado
Paraseguiremdire çãoaimplementa çãodo TemplateMethod,opassoseguinte
écriarumasuperclassequesejaespecializadaporambasasclasses.Aprincípioessa
classeestarávaziaparaquenãoconflitecomaimplementa çãodecadauma. Em
38

## Página 60

CasadoCódigo Capítulo2. ReusoAtravésdeHerança
seguida,deve-sesubirparasuperclasseosmétodosextraídos,porémcomométodos
abstratos.Issopermitiráquenaetapaseguinteométodoprincipalsejatotalmente
movidoparasuperclasseeretiradodetodasassubclasses.
Maucheirodecódigo:MissingTemplateMethod
Naterminologiadedesigndesoftware,um maucheiro,ou bad smell,sereferea
algumindíciodeproblemasnocódigoquepodemsignificardeficiênciasemsuamo-
delagem.Ummaucheiroédiferentedeumbug,poisnãonecessariamenteelecausa
umerronaaplica ção,mastrazoutrasconsequênciasnegativascomodificuldadede
manutençãoefaltadeflexibilidade.Existemferramentasquefazemadetec çãoau-
tomáticademauscheiros,usandocomobasesuasmétricasecaracterísticas.Olivro
“Refatoração:aperfei çoandooprojetodecódigoexistente”[12]trazumalistacom
algunsdeles.
Umdosmaucheirosquesãofrequentementedetectadosporessasferramentasse
chama "Missing T emplate Method”.Eleserefereadoiscomponentesquepossuemum
númerosignificantedesimilaridades,masnãocompartilhamdeumamesmaabstra-
ção,comoumainterface,oudeumamesmaimplementa ção,comoum Template
Method. Aosedepararcomessasitua ção,sejadetectadaporumaferramentaou
não,éindicadaarefatora çãodescrita.
2.6 CriandoObjetos naSubclasse-FactoryMethod
“Pequenas surpresas após cada esquina, mas nada perigoso. ”
–WillyWonka,AFantásticaFábricadeChocolates
Oconceitode hook methodnãoseaplicasomenteaopadrão TemplateMethod.
Existemoutrospadrõesquefazemusodomesmoprincípioparasolucionarproble-
masdiferentes.Elesaindapodemcombinarissocomoutrastécnicasparacompor
soluçõesmaiselaboradas. Essase çãoapresentaopadrão FactoryMethod,queé
utilizadopararesolverumproblemarelacionadoacria çãodeobjetos.
Quandoestamosdesenvolvendoumaaplica ção,écomumtermosclassesdedi-
ferenteshierarquiasserelacionando. Porexemplo,umaclassequerepresentauma
entidadedosistemapodeserelacionarcomaclassequefazasuavalida ção,ouuma
classequerepresentaumdocumentopodeserelacionarcomaclassequegerasua
representaçãoemPDF.Quandoissoocorre,acabamostendoquecriarumaclasse
emfunçãodaoutraqueestásendoutilizada.Noexemplocitado,sabemosquetodo
39

## Página 61

2.6. CriandoObjetosnaSubclasse-FactoryMethod CasadoCódigo
documentopossuiseugeradordePDF,mascomorelacionarasduasclasses?Paraa
classequeestarátrabalhandocomalógicadegera çãodearquivos,nãointeressade
qualclasseéainstânciaqueeleestárecuperando,masapenasqueessainstânciaseja
relacionadacomaclassequeestátrabalhando.
RelacionandoDAOseClassesdeServi ço
Parairmaisfundonesseproblemadacria çãodeobjetos,vamosconsiderarum
exemplobastantecomumemtodotipodeaplica ção.Quandotemosumaarquitetura
decamadasdefinida,écomumqueobjetosdeumacamadaprecisemcriarosobjetos
respectivosdacamadaseguinte. Nesseexemplo,consideraremosduascamadasda
aplicação:acamadaDAO(nomequevemdopadrão Data Access Object )que
realizaoacessoaobancodedadoseacamadadeservi ço,ondeestãoimplementadas
asregrasdenegócio.Nessecaso,acamadadeservi çorelacionadacomumaentidade
devecriaroDAOparaamesmaentidade.
Ainterface DAOdefineosmétodosgeraisdeacessoadadosqueserãodisponi-
bilizados,comopararecupera ção,grava çãoeexclusãodeentidades.Essainterface
precisaráserimplementadaparacadaentidadedosistema,paraacria çãodessas
operaçõesdecadauma.Notequeainterfacepossuiumparâmetrogenéricoqueé
utilizadoparadeterminaraentidadeassociadaaoDAOeparaqueessaentidade
sejautilizadanosparâmetroseretornosdosmétodos,variandodeacordocomque
queforsetadonaimplementa ção.
Listagem 2.7-InterfacedeDefini çãodeumDAO:
public interface DAO< E> {
public E recuperarPorId( Object id );
public void salvar( E entidade );
public void excluir( Object id );
public List <E> listarTodos ();
}
Aclasse ServicoAbstratorepresentaumaclassedacamadadenegóciosque
contémserviçosrelacionadosaumaentidade. Paraproversuafuncionalidade,ela
precisadacolabora çãodoDAOrelacionadoamesmaentidade. Essaclassepossui
métodoscomserviçosgeraisquesãoprovidosatodasasentidades.Umexemploé
ométodo gravarEntidadeEmArquivo(),querecuperaumaentidadeapartir
deseuidentificadorechamaainstânciadeGeradorArquivo(aquelaclassecriada
40

## Página 62

CasadoCódigo Capítulo2. ReusoAtravésdeHerança
anteriormentenessecapítulo)paracria çãodeumarquivocomaspropriedadesda
classe.Essaspropriedadessãoobtidasatravésdométodo getMapa()definidopara
otipoEntidade.ValeressaltarquequalquersubclassedeGeradorArquivopodeser
utilizada,poiselaépassadanoconstrutordaclasse.
Agrandequestãoéqueosmétodosgeraisdessaclasseabstrataprecisamacessar
oDAOparaexecutarsuafuncionalidade,porémqualseráainstânciaéalgoquesó
serádefinidonasubclasse,quandoaentidadecomaqualsetrabalhajáterásido
definida. Dessaforma,aclassedefiniuummétodoabstratochamado getDAO(),
queretornaainstânciadoDAOparaserutilizada. Assim,assubclassesdevem
implementaressemétododeformaaretornarainstânciacorreta. Esseéum hook
methodcomoobjetivodecriarumobjeto.
Listagem 2.8 - Serviço abstrato que define um método para recuperação do
DAO:
public abstract class ServicoAbstrato< E>{
public GeradorArquivo gerador ;
public ServicoAbstrato( GeradorArquivo gerador ){
this.gerador = gerador ;
}
public abstract DAO <E> getDAO ();
//Serviço geral
public void gravarEntidadeEmArquivo( Object id , String nomeArquivo ){
E entidade = getDAO ().recuperarPorId(id);
gerador.gerarArquivo(nomeArquivo,
((Entidade)entidade).getMapa());
}
}
A classe ServicoProduto, apresentada na próxima listagem, representa
um exemplo de uma subclasse da classeServicoAbstrato para a entidade
Produto.Observequeelaimplementao hook methoddefinidoecriaainstânciado
DAOrelacionadocomaclasse Produto.Noexemplo,ainstânciaécriadaquando
oprimeiroacessoéfeitoaométodo. Essaclassepodepossuirmétodosespecíficos
deproduto, porémosmétodosherdadosdasuperclassequeutilizamométodo
getDAO()tambémpoderãoserutilizados.
41

## Página 63

2.6. CriandoObjetosnaSubclasse-FactoryMethod CasadoCódigo
Listagem 2.9-Serviçoconcretoquedefineaimplementa çãoFactoryMethod:
public class ServicoProduto extends ServicoAbstrato <Produto>{
private DAO <Produto> dao ;
public DAO <Produto> getDAO (){
if(dao == null ){
dao = new ProdutoDAO ();
}
return dao ;
}
//Funcionalidade específica
public double getPrecoProduto( Object produtoId ){
Produto p = getDAO ().recuperarPorId(id);
return p .getPreco();
}
}
Valeobservarautiliza çãodostiposgenéricosnesseexemplo. Comoaclasse
ServicoProdutoespecificoudeformaexplícitaotipogenéricodesuasuperclasse,
todososelementosdaclassequeusavamoparâmetrodotipogenéricoserãofixados.
Comoométodo getDAO()precisaráagoraretornarum DAO<Produto>,haverá
umerrodecompila çãocasoumDAOcomoutrotipogenéricoforretornado.
EntendendooFactoryMethod
Oexemplodecria çãodoDAOnasclassesdeservi ço,ilustrambemocená-
rioondeaclassedainstânciautilizadadependedasubclasse.Opadrão Factory
Methodutilizaum hook methodparadelegaracria çãodainstânciaparaasubclasse.
Issopermitequemétodosmaisgeraisnasuperclassepossamutilizaressainstância
mesmosemconheceraclasseconcreta.Issopodeserfeitoinvocandoométodoabs-
tratodecria çãoqueéimplementadonasubclasse.
AFigura2.6apresentaumdiagramacomaestruturadopadrão Factory
Method. Nessepadrão,aclasseprincipalpossuiumadependênciacomumaabs-
traçãodeumahierarquiadeclasses. Nodiagrama, Dependenciaestárepresen-
tadacomoumainterface,porémnãohánadaqueimpededeserumaclasse. O
método metodoFabrica()possuiaresponsabilidadedecriarumainstânciade
Dependencia,porémnaclasseprincipaleleéummétodoabstrato.Dessaforma,
42

## Página 64

CasadoCódigo Capítulo2. ReusoAtravésdeHerança
nassubclassesessemétodoprecisaserimplementadoededevesercriadoumobjeto
deumaclasseconcretaquepossuaaabstra çãodadependência.
Figura2.6:EstruturadopadrãoFactoryMethod
Apartirdessepadrão,épossíveldesacoplarasuperclassedacria çãodeumade-
pendência.Comacriaçãodasinstânciasnasubclasse,apenaselasficamacopladasas
classesconcretasdahierarquia.Dessaforma,casoumanovainstânciadadependên-
ciapreciseserutilizadapelasuperclasse,bastacriarumanovasubclassequeretorne
aquelainstância.
2.7 Considerações Finais doCapítulo
Essecapítuloabordouautiliza çãodaheran çaparaareutiliza çãodecódigo.Opri-
meiropadrãoapresentadofoi Null Object,quemostracomoopolimorfismo
podeserutilizadoparaqueocódigodosclientesdeumaclassepossaseradaptados
comsuasextensões.Nessepadrãofoivistocomoaextensãodeumaclassepodeser
suarepresentaçãonula,fazendocomqueocódigoclienteconsigalidarcomelade
formatransparente.
Emseguidafoimostradocomoousodaheran çapodeserfeitoparapermitira
especializaçãodocódigodasuperclasse.Apartirde hook methodsépossívelqueas
subclassesinsiramcomportamentoemmétodosqueestãoimplementadosnasuper-
classe.Foramapresentadosospadrões Template Method e Factory Method
quefazemusodesseprincípio.
Apesardessespadrõespossuíremousodaheran çacomoparteprincipaldesua
solução,ousodosprincípiosapresentadosnãosãosuaexclusividade.Emqualquer
43

## Página 65

2.7. ConsideraçõesFinaisdoCapítulo CasadoCódigo
outrocontextoemqueosrequisitospuderemsersolucionadosapartirdaespecia-
lizaçãodafuncionalidadedasuperclasse,osmesmoprincípiosapresentadospodem
serutilizados.Opróximocapítuloiráexplorarousodacomposi çãoemostrarcomo
elapodeserutilizadaemconjuntocomaheran çaequandoseuusoémaisadequado.
44

## Página 66

Capítulo3
DelegandoComportamentocom
Composição
“ A primeira regra do gerenciamento é a delegação. Não tente fazer tudo sozinho
porque você não consegue. ”
–AntheaTurner
Aopensaremobjetos,umacoisamuitonaturaléimaginaremcomosãocombi-
nados.Naverdade,nãoexistemgrandesconstru çõesdohomemquenãosãofeitas
apartirdacombina çãodediversosobjetos.Umacasa,porexemplo,éfeitaapartir
dacombinaçãodediversosblocos.Olhandooutrosexemplos,umcarroécomposto
depe çaseumcomputadoréfeitodecomponenteseletrônicos. Oqueémaisin-
teressanteéqueamedidaquevamosdescendo,muitasvezesopadrãovaiserepe-
tindo:umape çapodesercompostaporoutras. Umaplacadecomputadoréfeita
comcapacitores,resistênciasechips.Éaquantidadeinfinitadecombina çõesdesses
elementosquetornapossívelaconstru çãodediversascoisasdiferentesapartirdo
mesmomaterial.

## Página 67

3.1. TentandoCombinarOpçõesdoGeradordeArquivos CasadoCódigo
Quandoaprograma çãoorientadaaobjetosfoicriada,umdosobjetivoserasim-
plificaraabstra çãodosconceitosdomundorealparaosoftware.Dessaforma,um
elementoexistentenodomíniodaaplica çãopoderiaserrepresentadoutilizandoum
objetonosoftware. Damesmaformaqueascoisasinteragemnomundorealpara
arealizaçãodeumobjetivo,dentrodeumsoftwarenãopoderiaserdiferente. Do
mesmojeitoquediversaspe çassãocombinadasemváriosníveisparacomporum
componentefísico,oscomponentesdesoftwaretambémpodemserresultadoda
combinaçãodeoutroscomponentesmaisgranulares.
Apesardenãoestarentreosquatroelementosprincipaisdeumalinguagemori-
entadaaobjetos,acomposi çãoéumconceitoquevemimplícitoquandosefala
emobjetos. OCapítulo 1jáapresentouousodacomposi çãoatravésdopadrão
Strategy,eestecapítuloiráexploraroconceitomaisafundoemostrarcomoele
podeserutilizadoparaaextensãodecomportamento.Serámostradocomoacom-
posiçãocombinadacomousodeabstra çõespodesereficaznasolu çãodediferentes
problemas.Aprimeirase çãocome çarevisitandooexemplodogeradordearquivos
docapítuloanteriorparailustrarcenáriosondeaslimita çõesdaheran çasãoeviden-
tes.
3.1 Tentando Combinar Op ç õ e s d oGerador de Ar-
quivos
No exemplo do capítulo anterior, a classeGeradorArquivo implementava
o padrão Template Method para permitir que as subclasses pudessem
especializar parte do comportamento, como o formato da geração do con-
teúdo e um pós-processamento a ser feito nos bytes do arquivo. O método
principal gerarArquivo() invocava os hook methods processar()
e gerarConteudo(), que eram implementados somente na subclasse.
As duas subclasses de GeradorArquivo, GeradorXMLCompactado e
GeradorPropriedadesCriptografado, respectivamente implementam os
métodosparageraremXMLcompactadosedepropriedadecriptografados.
Oproblemacome çaaotentarmosterumaimplementa çãoquecombinaocom-
portamentodessassubclasses,comoparaagera çãodearquivosXML ecriptografa-
dos.Setentarmosutilizaraheran ça,acabamoscomaduplica çãodealgumapartedo
código.AFigura 3.1mostraoqueacontecequandocriamosumanovaclassequede-
fineogeradordeXMLcomoumasuperclassecomduassubclassesqueespecializam
apenasapartedopós-processamento.Apesardetersidocriadaumaabstra çãorefe-
46

## Página 68

CasadoCódigo Capítulo3. DelegandoComportamentocomComposição
renteaoformatodoarquivo,aausênciadeumaabstra çãoparaopós-processamento
fazcomquehajaduplica çãodecódigo.
Figura3.1:Duplicaçãodecódigoaosetentarcriarumnovonívelnahierarquia
AFigura3.2mostraquesetentarmosestruturarahierarquiadeumaoutraforma
paraeliminaraduplica çãoanterior,continuaremoscomduplica çãoemumaoutra
partedocódigo.
Alimitaçãodousodaheran ça,queficaevidentenesseproblema,éofatodeela
poderserutilizadaapenasumavez.Sefossepossívelterheran çamúltiplaemJava,
umaclassepoderiaobteraimplementa çãodoformatodoarquivodeumasuper-
classeeadopós-processamentodeoutra. Comoissonãoépossível,quandopre-
cisamosdeumaimplementa çãodeoutroramodahierarquia,acabahavendouma
duplicaçãodecódigo.
47

## Página 69

3.2. Bridge-UmaPonteentreDuasVariabilidades CasadoCódigo
Figura3.2:Manutençãodaduplica çãoaosetentarcriarahierarquiapelooutrolado
Quandomaisdeum hook methodsãodefinidosemumasuperclasseeimplemen-
tadosporumasubclasse,essasimplementa çõesficamligadasumaaoutradevidoao
fatodeteremsidoimplementadasnamesmaclasse.Pormaisquesejapossívelirim-
plementandocada hook methodemumníveldiferentedahierarquia,aduplica ção
aindapodeacontecer,principalmenteseessesfatoresquepodemvariar-chama-
dosdevariabilidade-sãoindependentesumdooutro.Oproblemavaisetornando
aindamaiscríticoquandoseaumentaonúmerodevariabilidadeseonúmerode
possíveisimplementaçõesdecadaumadelas. Aquantidadedeclassesnecessárias
paraimplementartodasaspossibilidadestendeaaumentardeformaexponencial!
3.2 Bridge-U ma Ponte entre Du a sVariabilidades
“ A ponte não é de concreto, não é de ferro / Não é de cimento / A ponte é até onde vai
o meu pensamento / A ponte não é para ir nem pra voltar / A ponte é somente pra
atravessar / Caminhar sobre as águas desse momento”
–Lenini
Comotodosjádevemdesconfiarpelofocodocapítulo,acomposi çãoseráutili-
zadacomoformaderesolveroproblemadescrito.Comocomapurautiliza çãode
48

## Página 70

CasadoCódigo Capítulo3. DelegandoComportamentocomComposição
herança,aimplementa çãodeumavariabilidadeficaligadaaoutra,aideiadanova
soluçãoseriasepararaimplementa çãodeumadelasemumaoutraclasse.Damesma
formamostradanopadrão StrategynoCapítulo1,essaclasseirácomporaclasse
principal,nocaso GeradorArquivo.Dessaforma,ométodoimplementadonessa
hierarquiadeclassesàparteseráinvocadocomopartedaimplementa çãodoalgo-
ritmo. AFigura3.3mostracomoficariaaestruturadeclassescomautiliza çãoda
composiçãoparaosalgoritmosdepós-processamentodosarquivos.
Figura3.3:Utiliza çãodeComposi çãonoGeradorArquivo
Alistagemaseguirapresentaocódigodo GeradorArquivoapósaaplica ção
dessasolu ção. Ométodo processar()nãoestámaisnamesmaclasseesim
na instância de PosProcessador que compõe GeradorArquivo. Dessa
forma, qualquer implementação dessa interface pode ser utilizada para realizar
opós-processamentodoarquivo. Agrandemotiva çãodessasolu çãonocenário
apresentadoéqueoprocessadorpodeserconfiguradoindependentedasubclasse
queestásendoutilizada,permitindoàsduasvariardeformaindependente.
Listagem 3.1-ClasseGeradorArquivoutilizandocomposi ção:
public abstract class GeradorArquivo {
private PosProcessador processador ;
public void setProcessador(PosProcessador processador ){
this.processador = processador;
}
public final void gerarArquivo(String nome ,
49

## Página 71

3.2. Bridge-UmaPonteentreDuasVariabilidades CasadoCódigo
Map<String, Object> propriedades)
throws IOException {
String conteudo = gerarConteudo(propriedades);
byte[] bytes = conteudo.getBytes();
bytes = processador.processar(bytes);
FileOutputStream fileout = new FileOutputStream(nome);
fileout.write(bytes);
fileout.close();
}
protected abstract String
gerarConteudo(Map<String, Object> propriedades);
}
Mas e o caso em que não há pós -processamento?
Naimplementaçãooriginalapresentadanocapítuloanterior,omé-
todo processar()possuíaumaimplementação defaultparaocasode
nãohavernenhumpós-processamento.Essecasodevesertratadoaqui
nessasoluçãotambém!Oquedeveserfeito?Deve-secolocarumcondi-
cionalparaverificarseoprocessadorfoiconfiguradocorretamente?Essa
éumasoluçãopossível,porémpodemosutilizaro Null Object para
solucionaresseproblema.
Para fazer isso, uma implementação de PosProcessador cha-
mada NullProcessador poderia ser criada com uma que retor-
nasseopróprioarraydebytesrecebidocomoparâmetrosemnenhum
pós-processamento. Sendo assim, para garantir que não ocorra um
NullPointerExceptioncasooconteúdodavariável processador
sejanulo,umainstânciadessaclassepoderiaseratribuídaaelaemalgum
momentodainicializa çãodoobjeto.
Esseexemplomostracomoéimportantecombinarassolu çõesdos
padrõesparachegaraumaestruturafinal. Enxergueumpadrãocomo
umelementoquepodeserincluídoparacomporasuasolu çãoenãoa
soluçãocompleta!
EntendendoopadrãoBridge
Essasoluçãocaracterizaopadrão Bridge,quecriaumaponteentreduashi-
50

## Página 72

CasadoCódigo Capítulo3. DelegandoComportamentocomComposição
erarquiasligadasporumarela çãodecomposi çãopermitindoqueambasvariemde
formaindependente.Nessecaso,aponteécaracterizadapelarela çãodecomposi ção
entreaclasse GeradorArquivoeainterface PosProcessador.Umcenárioem
queessetipodesolu çãoécomuméquandotemosumahierarquiadeabstra çõese
outracomimplementa ções,permitindoquecadaumapossavariarindependente-
mente. Nestecaso,o GeradorArquivoesuassubclassessãoumaabstra çãoque
caracterizaalgoritmosdegera çãodearquivosemdeterminadosformatos,porém
aindasemdefiniraimplementa çãodopós-processamento.
AFigura 3.4apresentaumaestruturamaisgeralparaopadrão Bridge. A
classe Abstracaorepresentaumconceitoqueprecisaserrepresentadoemum
sistemaepossuiduasvariabilidadesindependentes,ouseja,comportamentosnão
dependentesquepodemserestendidose/oumodificados. Aclasserepresentada
como AbstracaoRefinadaespecializaocomportamentodaabstra çãoatravés
daimplementaçãodeseus hook methods.Jáaabstra çãorepresentadapelainterface
Componentecompõeaclasse Abstracaoerepresentaumadesuasvariabilida-
des. Dessaforma,quandoessaopera çãoprecisarserinvocadaem Abstracao,o
métodonaclassequeacompõeseráchamado.
Figura3.4:EstruturaGeraldoPadrãoBridge
No exemplo apresentado, a classeAbstracao é representada pela classe
GeradorArquivo,querepresentaumaabstra çãodecomogerararquivosapar-
tirdemapasdepropriedades.Seusrefinamentossãoclassesqueaespecializampara
queagera çãodosarquivossejafeitaemumformatoespecífico,comoXMLear-
quivosdepropriedades. Ainterface Componenteérepresentadapelainterface
51

## Página 73

3.2. Bridge-UmaPonteentreDuasVariabilidades CasadoCódigo
PosProcessadoreficaclaroapartirdesuasimplementa çõesqueelarepresenta
umaoperaçãodepós-processamentodoarquivo.
OsEfeitosdoBridge
A principal motivação na implementação do padrão Bridge é tornar in-
dependentes os fatores que podem variar na solução. Qualquer subclasse de
Abstracaopodeserfacilmentecompostacomqualquerimplementa çãodainter-
face Componente,permitindoacombina çãodeambaslivrementesemduplica ção
decódigo.Caso,porexemplo,umanovaimplementa çãodequalquerumadasduas
hierarquiasforcriada,elaseráfacilmentecombinadacomoquejáexiste.
Umefeitocolateralmuitointeressanteéqueasclassesqueforamseparadas,
tambémpodemserutilizadasemoutrocontexto. Noexemplo,osalgoritmosde
pós-processamentopoderiamserutilizadosnagera çãodeoutrostiposdearqui-
vosoumesmoparaoenviodeinforma çõespelarede. Essetipodequestãonos
fazrefletirseaprincípio,pensandoapenasnasresponsabilidades,essafuncionali-
dadejánãodeveriatersidoatribuídaaoutraclasse. Imagineacessarumaclasse
chamada GeradorArquivoparacriptografardadosparaseremenviadosemuma
rede.Dessaforma,umaconsequênciadessepadrãotambéméodesacoplamentode
responsabilidades,permitindomaisfacilmenteoseureusoemoutroscontextos.
Umpontoqueachointeressanteno Bridgeéofatodesuasolu çãoutilizarao
mesmotempoheran çaecomposi ção.Escutomuitaspessoasdizeremparautilizar
sempreacomposiçãonolugardaheran ça,porémachoqueapalavra "sempre”é
muitocomplicadanocontextodedesigndesoftware,poisnãoexistebaladeprata
nemumasolu çãomágicaqueiráresolvertodososseusproblemas.Acomposi ção
temsimsuasvantagensqueserãoapresentadasnopresentecapítulo,poréméim-
portantesempreavaliarcomcuidadooproblemaeosrequisitosdasolu çãoparaque
sebusqueamaisapropriada.
52

## Página 74

CasadoCódigo Capítulo3. DelegandoComportamentocomComposição
O padrão não é o diagrama!
Umerrocomumaoseaprenderosprimeirospadrõeséacharque
aimplementaçãodevesersempreexatamentecomoémostradanodi-
agramageraldopadrão. Odiagramaéapenasumareferência,poisa
mesmasoluçãopodeserimplementadadediversasoutrasformas. Por
exemplo,dependendodocontexto, Implementacaopoderiaserim-
plementadacomoumaclasseabstrataouaclasse Abstracaopoderia
possuirmaisdeum hook methodaserimplementadoporsuassubclas-
ses. Époressemotivo,queferramentasquegeramcódigoouprovêem
umaestruturadeclassesparaaimplementa çãodepadrõessãobastante
criticadasporespecialistasdaárea.Émaisimportantesepreocuparem
terumsolu çãoadequadaaoseuproblema,doqueseguircegamentea
estruturadopadrão.
3.3 Ho o kClasses
Nocapítuloanteriorfoiintroduzidooconceitode Hook Methods,quesãométodos
quepodemsersobrescritospelassubclassescomoformadeestendereespecializaro
comportamentodaclasse.Nessecapítuloestamosvendoumaoutraformadealterar
ocomportamentodasclassesapartirdacomposi ção.Emvezdeospontosemqueo
comportamentopodevariarseremdefinidosnamesmaclasse,elessãodefinidosem
umaoutraclassequecompõeaclasseprincipal.Aessaclassequepodeseralterada
damosonomede Hook Class.AFigura 3.5ilustraoconceitoapresentado.
53

## Página 75

3.3. HookClasses CasadoCódigo
Figura3.5:Representa çãodoConceitodeHookClasses
Damesmaformaqueos hook methods,as hook classessãoumatécnicautilizada
pelospadrõesparachegaraumasolu çãoparaumproblemamaisespecífico.Opa-
drão Bridge,porexemplo,utilizaaomesmotempoum hook methodeuma hook
c l a s scomoformadeseparardoispontosdeextensãocujocomportamentopodeva-
riardemodoindependente. Dessamaneira,éimportantenãoapenasconheceros
padrões,mascompreenderosprincípiosportrásdesuaestruturaparaentenderme-
lhorasconsequênciastrazidasporumadecisãodedesign.
DiferençasEntreosTiposdeHooks
Quandoentendemosaideiaportrásdos hook methodsedas hook classes,elesaté
quesãobemparecidos.Emambososcasos,aclasseprincipalchamaummétodocuja
implementaçãopodevariar.Nocasodos hook methodsessemétodoestánamesma
classe,podendoaimplementa çãovariarcomasubclasse,enocasodas hook classeso
métodoestáemumobjetoquecompõeaclasse,fazendocomqueaimplementa ção
variecomainstância.Apesardealgumasemelhan ça,autiliza çãodeumatécnicaou
outrapossuiconsequênciasbemdiferentes.
Aprimeiradelasestánomomentoemqueaimplementa çãoqueseráutilizada
54

## Página 76

CasadoCódigo Capítulo3. DelegandoComportamentocomComposição
éescolhida.Quandoum hook methodéutilizado,aescolhaéfeitanomomentoem
queoobjetoéinstanciado. Issoocorrepoisaocriarmosumnovoobjetodevemos
escolherqualaclasseconcretaqueseráutilizada,efazendoissoestamosescolhendo
asuaimplementa çãodos hook methods. Jánocasodautilizaçãode hook classes,a
implementaçãopodesertrocadaaqualquermomento,bastandoparaissotrocara
instânciaquefoiconfigurada.Observequeissonãoéobrigatório,comonoexemplo
daclasse GeradorArquivoapresentadanessecapítulo,quepermitiaaconfigura-
çãodaclassequeacompunhaapenasnoconstrutor.
Nesseponto, valeapenaretomaroexemplodoprimeirocapítulo, noqual
eranecessáriopodertrocaralógicaquecalculavaovalordoestacionamentode
acordocomotempoecomotipodeveículo. Nocenárioapresentadoeraextre-
mamenteimportantepodertrocaraimplementa çãodocálculoapósacria çãodo
objeto ContaEstacionamento. Essefoiumdosmotivosquefizeramaescolha
dopadrão Strategy,queutilizauma hook class,seradequadoparaaresolu çãodo
problema.
Outraquestãoquedeveserlevadaemconsidera çãoéograudedependência
dediferentespontosdeextensão.Casoos hook methodssejamdefinidosnamesma
classe,sendoelesnaprópriaclasseouemuma hook class,asimplementaçõesficamli-
gadas.Foiesseoproblemaapresentadonoexemplodo GeradorArquivo,noqual
pontosdeextensãoeramindependentesmasficavamdefinidosnamesmaclasse.
Quandousamosapenas hook methods,pelofatodenãohaverheran çamúltiplaem
Java,elessempreficaminterligados.Aoutilizarmos hook classes,secolocarmosos
métodosnamesmaclasse,omesmoproblemairáacontecer,porémsepusermos
emclassesdiferentes,cadaimplementa çãopoderáserconfiguradadeformainde-
pendente.Opadrão Bridgeabordajustamenteessaquestão,utilizandodiferentes
estratégiasdeextensãoparaqueasimplementa çõespossamvariardeformainde-
pendente.
EvoluindooModelodeClasses
Emumartigoclássicosobrepadrõesparaevolu çãodeframeworks[ 8],émos-
tradoquenormalmenteospontosdeextensãosãoprimeiramentedefinidosutili-
zandoherança,oqueéconhecidocomo whitebox framework,parasóemseguida
evoluirparaousodecomposi ção,chamadode blackbox framework.Pormaisquea
composiçãopare çasermaisvantajosaqueaheran çaporsuascaracterísticasestru-
turais,émuitomaisfácildeixarsuaclasseabertaàextensãoatravésdeheran ça.
Otermo whitebox frameworkserefereaframeworkscujasclassespermitemsua
55

## Página 77

3.4. State-VariandooComportamentocomoEstadodaClasse CasadoCódigo
extensãoapartirdaheran ça. Devidoaofatodassubclassesteremacessoadeta-
lhesinternosdaclassequeestásendoestendida,suaestruturaficaexposta.Otermo
whitebox,oucaixabranca,éumametáforaaessavisibilidadequeodesenvolvedor
precisaterdecomoascoisassãonaclasseinternamente.Comautiliza çãodessepa-
radigma,qualquermétodopúblicoouprotegidoquenãosejafinal,éumpotencial
hook methodaserespecializadopelassubclasses.Dessaforma,quandonãosesabe
exatamenteoqueseránecessárioserestendido,aheran çaéumaboaalternativapor
possibilitarqueváriospontosfiquememaberto. Umadesvantagemdessaaborda-
geméquequemdesenvolveraclassequefazaextensãodeveconheceraestrutura
internadasuperclasse,tornandoatarefamaiscomplexa.
Poroutrolado,otermo blackbox frameworkserefereaframeworkscujomeca-
nismodeextensãosebaseiaemcomposi ção.Nessecaso,odesenvolvedordevecriar
implementaçõesqueobedecemaumainterfacefornecidaeutilizá-lasparacompor
aclasseprincipal.Otermo blackbox,oucaixapreta,éutilizadoporqueodesenvolve-
dornãoprecisaconheceraparteinternadasclassesdoframeworkparaestendê-las.
Apesardepossuirasvantagensdacomposi ção,essetipodepontodeextensãoémais
difícildeseridentificado,poiséprecisosaberapor çãoexatadafuncionalidadeque
serádelegada.Emcompensação,depoisqueessespontosforemidentificados,émais
fácilparaoutrosdesenvolvedoresalteraremocomportamento,poiselessóprecisam
entenderasinterfacesqueestãoimplementando.
Naverdade,nadaprecisasercompletamentepretooubranco.Ocaminhonatu-
ralé,aocriaraprimeiraclasse,deixaralgunspossíveis hook methodsemabertopara
quesejapossívelrealizaraextensãodocomportamento.Àmedidaqueasextensões
foremsendocriadaseosprincipaispontosondeocomportamentoéespecializado
comfrequênciaforemidentificados,aestruturapodeserrefatoradaparaousode
hook classes.
3.4 St a t e-Variando oComportamento com o Estad o
d aCl a s s e
“Eu costumava partir por semanas em um estado de confusão. ”
–AlbertEinstein
Umcenáriobastantecomumaodesenvolvermosumsoftwareéumadetermi-
nadaentidademudardeestadoduranteodecorrerdesuaexecu ção,alterandoseu
comportamentodeacordocomesseestado.Umacontacorrenteemumbanco,por
56

## Página 78

CasadoCódigo Capítulo3. DelegandoComportamentocomComposição
exemplo,comporta-sediferentecasoosaldoestejanegativo.Emumjogo,asmesmas
açõespodemgerardiferentesefeitosemumpersonagemquandoeleestáemestados
diferentes,comoquandopegaalgumitemouestádentrod’água.
Aimplementaçãocomumnessescasosécriarumasériedecondicionaisemque,
emdiversospontosdaclasse,verifica-seoestadodoobjetoeexecuta-sealógicamais
adequada.Seguindoessaideia,algunsestadossãosuficientesparadeixarocódigo
bastanteconfuso.Écomumqueamesmasequênciadecondicionaissejaencontrada
emdiversospontosdocódigoondeoestadodoobjetopossuiinfluência.Alémdisso,
essaestruturatornacomplicadaaadi çãodemaisestados,poisissodemandaráalte-
raçõesnocódigodaprópriaclasseeiráaumentaraindamaisaquantidadedecon-
dicionais.Comoresolverisso?Conhe çaopadrão State!
AEstruturadoState
Essaseçãoiráapresentaropadrão State,oqualutilizacomposi çãoparaper-
mitiressavaria çãodecomportamentodeacordocomooestadodeumaentidadedo
sistema.Nessepadrão,osestadossãorepresentadosapartirdeclassesqueobede-
cemaumaabstra çãocomum,podendoserumainterfaceouumasuperclasse.Dessa
forma,aentidadeécompostaporumobjetodotipodessaabstra çãoe,nosmétodos
denegócio,delegaparaeleocomportamentodetodapartequedependedoseues-
tado.AFigura 3.6representaaestruturadessepadrão.
57

## Página 79

3.4. State-VariandooComportamentocomoEstadodaClasse CasadoCódigo
Figura3.6:EstruturadopadrãoState
Sendoassim,apenasalógicacomumserámantidanaentidadeeocompor-
tamentodoobjetoespecíficodecadaestadoestarádefinidoemcadasubclasse.
Quandooestadoforalterado,bastatrocarainstânciautilizadaparacaracterizaro
estado,queconsequentementeocomportamentodaentidadeseráalterado. Nesse
caso,oestadoéuma hook classparaaqualestásendodelegado.Umaconsequência
dessepadrãoéasimplicidadeemalterarestadosexistentes,oumesmoinserirnovos
estadosnociclodevidadaentidade.Adesvantageméque,devidoàdivisãodaló-
gicadosestados,ficamaisdifícilterumavisãoglobaldosestadosetransi çõesque
podemserrealizadas.
BuscaemProfundidade
Calma! Vocênãoestáemumlivrodealgoritmos! Achomuitointeressante
quandoépossívelresolverumproblemaclássiconaáreadeprojetodealgoritmos
eestruturadedadosutilizandoalgumpadrão. Issonosmostraqueelessãoúteis
paraqualquertipodesoftware. Oalgoritmoabordadonessase çãoéabuscaem
profundidadeemgrafos.Nessealgoritmo,àmedidaqueosnósdografovãosendo
percorridos,elesmudamdecoreocomportamentodoalgoritmodependedacordo
nóqueestásendopercorrido.Dessaforma,o Stateseráutilizadoparaconfigurar
ocomportamentodecadanódeacordocomseuestado.
58

## Página 80

CasadoCódigo Capítulo3. DelegandoComportamentocomComposição
Abuscaemprofundidadeéumalgoritmodebuscadegrafos,queseiniciacom
umnóraizevaiseexplorandocadaumdeseusramos,semprenamaiorprofun-
didadepossível,antesderetrocedereprocessarosoutrosramos.Paraquemnãose
lembradoalgoritmodebuscaemlarguraemgrafos,segueumabreveexplica çãode
comoelefunciona.Aexecu çãoinicia-seapartirdeumnóetodosiniciam-secom
acorbranca.Quandoumnócome çaaserprocessado,eleadquireacorcinzaque
significaqueeleestásendoprocessado.Aoadquiriracorcinza,sãoprocessadosto-
dososseusnósadjacentesquetenhamacorbranca. Aofinalizaraexecu çãoonó
passadacorcinzaparacorpreta,queindicaqueseuprocessamentofoiconcluído.
Oalgoritmoterminaquandoonóraizondeoalgoritmoiniciouadquireacorpreta.
AFigura 3.7apresentaumexemplodeexecu çãodoalgoritmopassoapassoem
umgrafo.Nesseexemplo,conformeosnósvãomudandodeestado,elesadquirem
umacordiferenteeasarestasquejátiveremsidopercorridassãocolocadasemne-
grito.Apartirdoexemploépossívelentenderdeumaformamaisconcretacomoos
nóssãopercorridoseasitua çãoemquemudamdeestado.
Figura3.7:BuscaemProfundidadePassoaPasso
59

## Página 81

3.4. State-VariandooComportamentocomoEstadodaClasse CasadoCódigo
ImplementaçãodaBuscaemProfundidadeUtilizandoState
O primeiro passo da implementação é definir um nó e quais os pontos da
execuçãoquediferemcomoestado. Nocontextodoalgoritmo,asinforma ções
relevantesdeumnósãooseunome,seusnósadjacentesesuacor. Essaclasse
possuiummétodochamadobuscaProfundidade()queiráefetivamenteexecutar
oalgoritmo. Ospontosidentificadosquepodemvariarcomoestadosão: (a)a
própriaexecuçãodabuscaemprofundidade,poisnocasodonóserpretooucinza
elanãodeveserexecutada;e(b)quandoonóassumeumacor. Aimplementa ção
realizadaparaclasse Noestárepresentadanalistagemaseguir.
Listagem 3.2-Definiçãodaclassequerepresentaumnó:
public class No {
private Set<No> adjacentes = new HashSet<>();
private Cor cor ;
private String name ;
public No(String name ){
this.name = name;
cor = new Branco();
}
public void buscaProfundidade(List<No> list){
cor.busca(this, list);
}
public Set<No> getAdjacentes() {
return adjacentes;
}
public void addAdjacentes(No adj ) {
adjacentes.add(adj);
}
public void setCor(Cor cor , List<No> list) {
this.cor = cor;
cor.assumiu(this ,list);
}
public String toString() {
return name;
}
}
Oatributo correpresentaoestadodonónaexecu çãodoalgoritmo. Ob-
60

## Página 82

CasadoCódigo Capítulo3. DelegandoComportamentocomComposição
serve que métodos são invocados no objeto desse atributo quando o método
buscaProfundidade()éinvocadoequandoumanovacoréconfiguradaapar-
tirdométodo setCor().O buscaProfundidade()recebeumalistaquedeve
serpopuladacomosnósdografonaordemqueterminaramdeserexecutadospelo
algoritmo.
A listagem a seguir apresenta a classe abstrataCor e suas três subclasses.
Observe que cada cor implementa oshook methods da definição do estado, de
acordocomadescri çãodoalgoritmo. Quandoonónoestado Brancorecebe a
chamadadabusca,omesmodevepassarparaacor Cinza.Essa,porsuavez,aoser
assumidapelonóiniciaoprocessamentodetodososnósadjacentes,assumindoa
cor Pretoaoseufinal.Finalmente,aosetornar Preto,onódeveseradicionado
nalistarecebidacomoparâmetropeloalgoritmo.
Listagem 3.3-Implementaçãodosestadosdeumnó:
//Classe que abstrai o estado de um nó
public abstract class Cor {
void busca(No no , List<No> list){}
void assumiu(No no , List<No> list){}
}
//Implementações dos três estados possíveis
public class Branco extends Cor {
public void busca(No no , List<No> list) {
no.setCor(new Cinza(), list);
}
}
public class Cinza extends Cor {
void assumiu(No no , List<No> list) {
for(No adj : no.getAdjacentes())
adj.buscaProfundidade(list);
no.setCor(new Preto(), list);
}
}
public class Preto extends Cor {
void assumiu(No no , List<No> list) {
list.add(no);
}
}
61

## Página 83

3.4. State-VariandooComportamentocomoEstadodaClasse CasadoCódigo
Alistagemaseguirmostraacria çãodografoapresentadonaFigura 3.7ea
execuçãodoalgoritmo. Aoseufinal,osnóssãoimpressosnaordememqueseu
processamentofoifinalizado.
Listagem 3.4-Execuçãodoalgoritmoparaografodoexemplo:
public static void main(String[] args) {
No a = new No("A"); No b = new No("B");
No c = new No("C"); No d = new No("D");
No e = new No("E"); No f = new No("F");
No g = new No("G"); No h = new No("H");
a.addAdjacentes(b); b.addAdjacentes(c);
c.addAdjacentes(d); d.addAdjacentes(b);
a.addAdjacentes(e); e.addAdjacentes(f);
f.addAdjacentes(c); f.addAdjacentes(g);
f.addAdjacentes(h); a.addAdjacentes(h);
List<No> l = new ArrayList<>();
a.buscaProfundidade(l);
for(No n : l)
System.out.println(n);
}
Nessealgoritmo,diversasa çõesdependemdoestadodonó,comoseeledeve
seradicionadonalistaouseosnósadjacentesdevemserprocessados.Apesardisso,
observequenenhumcomandocondicionalfoiutilizadonaimplementa ção!
UtilizandoumEnumparaImplementaroState
Quandotemosquerepresentarestadosdeumobjetoemumsoftware,frequen-
tementeutilizamosenumera ções. Oproblemaéquemuitasvezesasenumera ções
possuemapenasadefini çãodosestados,ficandoalógicaespecíficadecadaestado
presadentrodoscondicionaisnaclasse.Constru çõesdotipo enumpodemdefinir
métodos, inclusive abstratos, que podem ser sobrescritos na definição de cada
estado. Seguenalistagemaseguircomoascoresdosnósdografopoderiamser
definidasutilizandoumaenumera ção. Emrelaçãoaorestodocódigo,somentea
inicializaçãodoatributo cordaclasse Noprecisariasermodificada.
Listagem 3.5-Execuçãodoalgoritmoparaografodoexemplo:
62

## Página 84

CasadoCódigo Capítulo3. DelegandoComportamentocomComposição
public enum Cor {
BRANCO{
public void busca(No no , List<No> list) {
no.setCor(CINZA, list);
}
},CINZA{
void assumiu(No no , List<No> list) {
for(No adj : no.getAdjacentes())
adj.buscaProfundidade(list);
no.setCor(PRETO, list);
}
},
PRETO{
void assumiu(No no , List<No> list) {
list.add(no);
}
};
void busca(No no , List<No> list){}
void assumiu(No no , List<No> list){}
}
Porémexistemalgumassitua çõesemqueautiliza çãodeenumera çõesédesa-
conselhadanarepresenta çãodeumestado.Aprimeiraéquandoédesejávelqueo
estadosejaumpontodeextensãoequenovosestadospossamserdefinidos.Nesse
caso,comoospossíveisestadossãodefinidosdentrodeumaenumera çãofixa,não
sepodeadicionarumnovosemamodifica çãodocódigodopróprioenum.Outra
situaçãoéquandoalgumestadoprecisaarmazenarumainforma çãoespecíficado
objetoqueestásendocompostoporele.Nessecaso,comocadainstânciadoenum
écompartilhadaportodosqueapossuem,ainforma çãonãopoderiaserdiferente
paracadauma.
3.5 Substituindo Condicionais porPolimorfismo
Noexemploapresentado,osnósjápossuíamumestadoexplícitosegundoadescri-
çãodoalgoritmo,porémumcenárioparautiliza çãodopadrão Statemuitasvezes
édifícildeseridentificadoinicialmente.Oconceitodoquesignificaumestadopara
umadeterminadaentidadedosoftwarepodecome çaraficarexplícitosomenteno
63

## Página 85

3.5. SubstituindoCondicionaisporPolimorfismo CasadoCódigo
momentodacodifica ção.Arepeti çãodecondicionaissimilaresemdiversospontos
damesmaclassepodeserumsinaldequeseriaadequadaarefatora çãodocódigo
emdireçãoaopadrão State.
Omesmovaleparaoutrospadrõesqueutilizamcomposi ção. Umexemploé
quandoumaclassepossuirummétodograndequeutilizacondicionaisparaseleci-
onardentrealternativasdeimplementa çãoparaummesmoalgoritmo.Nessecaso,
arefatoraçãopoderiasernadire çãodopadrão Strategy.Oexemploapresentado
naintroduçãodolivroilustrabemumarefatora çãoemdire çãoàcomposi ção.
Figura3.8:RefatorandoemDire çãoaComposi ção
64

## Página 86

CasadoCódigo Capítulo3. DelegandoComportamentocomComposição
AFigura 3.8apresentaoprocessoquepodeserutilizadoparaextrairaclasse
queseráutilizadaparaacomposi çãoeparaacria çãodasimplementa çõesdecada
alternativa.Oprimeiropassoconsistenaidentifica çãodoslocaiscomalógicacon-
dicionalcomodescritoacimaenasuaextra çãoparamétodosqueaprincípioficarão
naprópriaclasse. Emseguida,umanovaclassedevesercriadaeumatributodo
tipodeladeveserintroduzidonaclasseprincipalquesedesejarefatorar.Notequea
princípioelaestarávaziaenenhumusodelaéfeitoapartirdaprincipal.
Comanovaclassecriada,opróximopassoémoverosmétodosextraídosna
primeiraetapadarefatora çãoparaela.Cadamétododeveserpassadoparaanova
classecomométodopúblicoeoslocaisondeerainvocadodevemagorachamá-lo
apartirdoatributocriado. Éaconselhávelquecadamétodosejamigradosepara-
damente,executandotestesemcadapasso.Umaquestãoquedeveserconsiderada
nessepontoérelacionadaaosdadosquesãoutilizadospelapor çãodalógicaqueestá
indoparaoutraclasse.Quandoainforma çãoforumparâmetrorelacionadocomo
algoritmoemsi,normalmenteeleéincluídocomoumatributodaclassequeestá
sendoextraída. Quandoéumainformaçãodaclasseprincipal,normalmenteeleé
passadocomoparâmetro,ouaprópriainstânciadaclasseépassadacomoparâmetro.
Depoisquealógicacondicionalformigradaparaoutraclasse,épossívelco-
meçaraextrairsubclassescomcadaumadasimplementa ções.Oconteudodeum
condicionalnasuperclassedevesermovidoparaumasubclasse. Adicionalmente,
éprecisoatribuirumainstânciadessaclassenaprincipalquandoelaprecisarser
invocada. Essatrocadeinstânciaérealizadanormalmentenomomentoemquea
variávelutilizadanoscondicionaiséalterada.Porexemplo,searefatora çãoforpara
opadrão State,entãoamudan çadainstânciadeveocorrernomomentodamu-
dançadeestado.Comisso,alógicaqueanteseraselecionadacomcondicionalagora
seráinvocadaatravésdepolimorfismo. Asduaslistagensaseguirapresentamres-
pectivamenteoanteseodepoisdacria çãodeumanovasubclasse.
Listagem 3.6-Códigodocomponenteantesdarefatora ção:
public class Componente {
public void metodoExtraido() {
if (possibilidadeA) {
//lógica referente ao cenário A
} else if (possibilidadeB) {
//lógica referente ao cenário B
} else if (possibilidadeC) {
//lógica referente ao cenário C
}
65

## Página 87

3.6. CompondocomMúltiplosObjetos-Observer CasadoCódigo
}
}
Listagem 3.7-Códigodocomponenteesuasubclassedepoisdarefatora ção:
public class Componente {
public void metodoExtraido() {
if (possibilidadeB) {
//lógica referente ao cenário B
} else if (possibilidadeC) {
//lógica referente ao cenário C
}
}
}
public class ComponenteA extends Componente {
@Override
public void metodoExtraido() {
//lógica referente ao cenário A
}
}
Depoisqueumasubclasseforextraída,arefatora çãodeveserconcluídacoma
extraçãodasoutrassubclasses.Éimportantenãotentarcriartodasassubclassesde
umasóvez.Acadasubclasseextraída,deve-seexecutarostestesparaverificarser
elafoirealizadacorretamente.Aofinalizaraextra ção,asuperclassepodeficarcom
algumcomportamento default,casoexista,ouosmétodospodemsertransformados
emabstratoscasotodalógicatenhasidomovida.
3.6 Compondo com MúltiplosObjetos-O bserver
“ A visão de um observador imparcial é uma janela para o mundo. ”
–KennethL.Pike
Nosexemplosvistosatéomomento,acomposi çãoocorreapenascomumains-
tância.Nessase çãoseráapresentadoumpadrãoqueutilizaacomposi çãocommúl-
tiplosobjetos:o Observer.Esseéumpadrãomuitoimportanteequefrequente-
menteénecessárioemaplicações.Éaplicávelquandoexisteumobjetocujoseven-
tosprecisamserobservadosporoutrosobjetos.Umexemploseriaumcomponente
66

## Página 88

CasadoCódigo Capítulo3. DelegandoComportamentocomComposição
gráficocujoseventosprecisamsertratadospelaaplica ção.Umoutroexemplo,tal-
vezmenosóbvio,éumobjetodedadoscujasmudan çasdemandammudan çasem
outraspartesdosistema.
Apróximase çãoapresentaumexemplodopadrão Observer,emquemudan-
çasemumobjetosãonotificadasaoutrosobjetosinteressados. Emseguidaesse
padrãoseráanalisadodeformamaisprofunda,avaliandosuaestruturabásicaesuas
consequências. Porfim,serãomostradasalgumasAPIsexistentesquefazemuso
dele.
Notificandomudan çasemumaCarteiradeA ções
Oexemploqueseráabordadoenvolveumobjetoquerepresentaumacarteirade
ações.Essacarteirapossuiummapacomoscódigosdasa çõesesuarespectivaquan-
tidade.Deacordocomasa çõesdousuáriooucomgatilhosconfiguradosnaaplica-
ção,a çõespodemsercompradasouvendidasalterandosuaquantidade.Aquestão
équeexistemdiversasclassesinteressadasemsaberquandoumainforma çãoéal-
teradanessaclasseparapoderexecutarasualógica.Porexemplo,umcomponente
queexibeumgráficocomaquantidadedecadaa çãodacarteiraprecisasaberquando
houveumamudan çaparaseratualizado.Outroexemploseriaumcomponenteque
fizesseumlogdasaltera çõesrealizadas. Poderiatambémexistirumcomponente
parafazeraauditoriadosdados.
Casoasnotifica çõessejamfeitasindividualmenteparacadanecessidade,aclasse
querepresentaacarteiradea çõesficariaacopladaàsclassesqueprecisarianotificar.
Issonãoédesejável. Alémdedificultarmudançasnasclassesenvolvidas,tornaria
complicadoaadi çãodenovasclassesinteressadasemmudan çasnessasinforma ções.
Pararesolveresseproblema,opadrão Observerseráimplementadonasolu-
ção. Serácriadaumainterface Observador,apresentadanalistagemaseguir,a
qualdeveserimplementadapelasclassesquedesejamreceberoseventosdemu-
dançanaquantidadedasa ções.Implementa çõesdessainterfacepoderãoserregis-
tradasnaclasse CarteiraAcoes,cujalistagemtambémestáapresentada,atra-
vésdométodo addObservador().Dessaforma,todososobservadoresregistra-
dosreceberãoumanotifica çãoquandoumamudan çaforrealizada. Observeque
ométodo notificar()chamaométodo mudancaQuantidade()dainterface
Observadoremtodasasinstânciasregistradas.
Listagem 3.8-Interfacepararecebernotifica çõesdacarteiradaa ções:
public interface Observador {
67

## Página 89

3.6. CompondocomMúltiplosObjetos-Observer CasadoCódigo
void mudancaQuantidade(String acao , Integer qtd );
}
Listagem 3.9-Classecujosdadospodemserobservadosporoutrasclasses:
public class CarteiraAcoes {
private Map<String,Integer> acoes = new HashMap<>();
private List<Observador> obs = new ArrayList<>();
public void adicionaAcoes(String acao , Integer qtd ) {
if(acoes.containsKey(acao)){
qtd += acoes.get(acao);
}
acoes.put(acao, qtd);
notificar(acao, qtd);
}
private void notificar(String acao , Integer qtd ) {
for(Observador o: obs)
o.mudancaQuantidade(acao, qtd);
}
public void addObservador(Observador o ) {
obs.add(o);
}
}
Aseguir,sãoapresentadasduaslistagensdeclassesqueimplementamainterface
Observador: AcoesLoggere GraficoBarras.Aclasse AcoesLoggerpossui
umaimplementaçãobemsimpleseapenasregistraanovaquantidaderecebidano
console.Jáaclasse GraficoBarrasutilizaocomponentedegera çãodegráficos
JFreeChartparaacria çãodeumajanelacomumgráficodebarrasqueéatualizado
todavezqueumamudan çaénotificada.
Listagem 3.10 - Classe que observa mudanças nas quantidades e registra no
console:
public class AcoesLogger implements Observador {
public void mudancaQuantidade(String acao , Integer qtd ) {
System.out.println("Alterada a quantidade da ação "
+ acao + " para " + qtd);
68

## Página 90

CasadoCódigo Capítulo3. DelegandoComportamentocomComposição
}
}
Listagem 3.11-Classequecolocaasquantidadesemumgráficodebarras:
public class GraficoBarras implements Observador {
private DefaultCategoryDataset dataset ;
private JFrame frame = new JFrame();
public GraficoBarras() {
dataset = new DefaultCategoryDataset();
JFreeChart chart = ChartFactory.createBarChart(
"Carteira de Ações" ,"Siglas",
"Quantidade", dataset, PlotOrientation.VERTICAL,
false, true, false);
ChartPanel chartPanel = new ChartPanel(chart);
frame.setContentPane(chartPanel);
frame.setSize(500, 270);
frame.setVisible(true);
frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
}
public void mudancaQuantidade(String acao , Integer qtd ) {
dataset.setValue(qtd, "Quantidade", acao);
}
}
Utilizando oJFr e eCh a r t
Sevocêdesejaexecutaroexemploapresentado,precisabaixaroJFre-
eChartnoendere ço http://www.jfree.org/jfreechart/eadicionarosar-
quivosjfreechart-1.x.x.jarejcommon-1.x.x.jarnoclasspath.Osgráficos
desseframeworksempresãodivididosemduaspartes: oconjuntode
dadoseasuarepresenta çãovisual.Noexemploapresentado,oatributo
datasetdaclasse DefaultCategoryDatasetrepresentaoconjunto
dedadoseavariávellocal chartrepresentaapartevisual.Nocaso,com
aalteraçãodoconjuntodedadosassociadoaográfico,arepresenta ção
tambéméatualizada.
69

## Página 91

3.6. CompondocomMúltiplosObjetos-Observer CasadoCódigo
Parafinalizaroexemplo,alistagemaseguirapresentaummétodo main()que
associaosobservadoresnacarteiradea çõeseadicionaa çõesacarteira.Noiníciodo
código,asinstânciasde GraficoBarrase AcoesLoggersãocriadaseassociadas
aoobjetodaclasse CarteiraAcoes.Emseguida,ométodo Thread.sleep()é
utilizadoparagerarumintervaloentrecadaquantidadeinseridanacarteiradea ções,
paraserpossívelverdeformaprogressivaasaltera çõesnográficoeasmodifica ções
registradasnoconsole.AFigura 3.9apresentaográficogeradonofinaldaexecu ção.
Listagem 3.12-Exemplodeexecu çãodacarteiradea çõescomobservadores:
public static void main(String[] args) throws Exception {
GraficoBarras gb = new GraficoBarras();
AcoesLogger al = new AcoesLogger();
CarteiraAcoes c = new CarteiraAcoes();
c.addObservador(gb);
c.addObservador(al);
Thread.sleep(2000);
c.adicionaAcoes("COMP02", 200);
Thread.sleep(2000);
c.adicionaAcoes("EMP34", 400);
Thread.sleep(2000);
c.adicionaAcoes("ACDF89", 300);
Thread.sleep(2000);
c.adicionaAcoes("EMP34", -200);
Thread.sleep(2000);
c.adicionaAcoes("COMP02", 150);
}
70

## Página 92

CasadoCódigo Capítulo3. DelegandoComportamentocomComposição
Figura3.9:ExemplodoGráficoGeradopelaAplica ção
IndoafundonoPadrãoObserver
Aestruturadopadrão Observerébemsimples:aclassequeestásendoobser-
vadaécompostaporumalistadeobservadores.Alémdisso,aclassenormalmente
oferecemétodosquepermitemaadi çãoeremo çãodessesobservadoresemtempo
deexecução.Dessaforma,quandooestadodaclasseobservadaéalterado,todosos
observadoressãonotificados.AFigura 3.10apresentaumdiagramacomaestrutura
dopadrão.
71

## Página 93

3.6. CompondocomMúltiplosObjetos-Observer CasadoCódigo
Figura3.10:EstruturadoPadrãoObserver
Observequenodiagramaexisteumahierarquiadeclassescompostapelasclas-
ses Observavele ObservavelConcretoquenãohaviasidorepresentadano
exemplo,noqualessesdoispapéissãodesempenhadospelamesmaclasse.Essaabs-
traçãodeobjetosobserváveispodeserextremamenteútilquandohouvermaisde
umaclassequepuderemitirnotifica ções. Imagine,porexemplo,diversoscompo-
nentesgráficosquepodemnotificaraocorrênciadeeventosgeradospora çõesdo
usuário.Nessecontextopodeserimportanteacapacidadedeabstrairessecompor-
tamentoeatribuirobservadoresaomesmotipodeclasse.
Umaimportanteconsequênciadessepadrãoéodesacoplamentoentreaclasse
queestásendoobservadaeaobservadora. Ainterfacequedeveserimplemen-
tadapelosobservadoreséocontratoqueuneasimplementa ções.Dessaforma,um
mesmoobservadorpodeseradicionadoemdiferentesobjetos,recebendonotifica-
çõesdetodoseles,eváriosobservadoresdiferentespodemrecebernotifica çõesdo
mesmoobjeto. No Observeraoinvésdepossuiruma hook class,aclasseobser-
vadapodepossuirumconjunto,sendoqueo hook methoddetodaséchamadono
momentoemquedeveocorreranotifica ção.
Éimportanteressaltar,especialmenteaosefalardo Observer,quediversasva-
riaçõessãopossíveis.Porexemplo,podemexistirváriosmétodosdenotifica çãopara
diferentestiposdeevento,queprecisamserimplementadospelaclasseobservadora.
Nessecaso,cadamétodoseriachamadoemumasitua çãodiferente. Noexemplo
72

## Página 94

CasadoCódigo Capítulo3. DelegandoComportamentocomComposição
apresentado,poderiahaverummétodoparanotificarquandoumaa çãoéremovida
dacarteira.Outropontoemquepodehavervaria çãoéemcomoosobservadoressão
gerenciados.Elespoderiam,porexemplo,serpassadosnoconstrutore,outrasve-
zes,nãofazsentidohaverummétododeexclusão.Lembre-sequeopadrãoéapenas
umareferênciaecabeaodesenvolvedoradaptá-loaoseucontexto!
Aolidarcomacomposi çãodediversas hook classes,éimportantelevaremconsi-
deraçãocomooqueocorreemumainfluenciaasoutras.Porexemplo,oqueacontece
seumadasclasseslan çaumaexce ção?Asoutrasdevemcontinuarsendoexecutadas?
Emcasopositivo,devehaverumtratamentodeerroseparadoparacadainvoca ção.
Outraquestãoseriaemrela çãoàpossibilidadededemoranaexecu çãodeumobser-
vadorinfluenciaravelocidadedenotifica çãodosoutros.Dependendodosrequisitos
daaplicação,podesernecessárioachamadado hook methoddecadaclasseemum
threaddiferente.
PadrãoObservernasAPIsJava
Opadrão ObserverpodeservistocomfrequênciaemváriasAPIsdalingua-
gemJava. Umdosmotivosdelepodersernotadodeformatãoexplícitaéporque
diversasclassespermitemquesuasmudan çassejamrecebidaspelaaplica çãoatravés
deobservadores.Comofoidito,essaéumaboaformadepermitirodesacoplamento
entreaclassequegeraeaquerecebeoevento.
Ainterface ActionListener,porexemplo,éutilizadanoSwingnasclasses
quedesejamtratareventosdeinterface.Nocaso,osobjetosobservadossãocompo-
nentesdeinterface,comoaclasse JButton.Oobservador,quetambéméchamado
listener,éadicionadonocomponenteatravésdométodo addActionListener()
eprecisaimplementarométodo actionPerformed()paratrataroseventos.
Outroexemplodeimplementa çãodo Observer,agoranasAPIsdoJavaEE,é
o MessageListenerparaorecebimentodemensagensJMS.Essainterfacepre-
cisaserimplementadaporclassesquedesejamrecebermensagensdeumservi çode
mensageria,asquaisdevemimplementarométodo onMessage()paratratarcada
mensagemrecebida.Umainstânciade MessageConsumercomafilaouotópico
deorigeméondeo listenerdeveserconfigurado.OsMessageDrivenBeans,quesão
EJBsresponsáveisportratarmensagensJMS,tambémimplementamessainterface.
HádezenasdeoutrosexemplosdentrodasclássicasAPIsdoJava.Todososlis-
tenersdesessãodasservlets,oslistenersdefasedaJSFeoslistenersdemudan çasde
valoresementidadesnaJPAsãobonsexemplosdeimplementa çãodo Observer,
quedesacoplamseucódigoefacilitamaextensão. Todososobservadorespodem
73

## Página 95

3.7. ConsideraçõesFinaisdoCapítulo CasadoCódigo
trabalhardeformatotalmenteindependente,semterconhecimentodaexistência
dosoutros.
Umacoisainteressanteemaprenderpadrõeséqueapartirdelesficamaisfácil
compreenderofuncionamentodeAPIseframeworksqueutilizamos. Écomose
passássemosaolharparaelescomoutrosolhos.Imaginoquesejaalgocomparável
aquandoestudamosfísica,químicaoubiologiaepassamosacompreendermelhor
omundoaonossoredor. Aoperceberqueumpadrãofoiimplementadoemuma
solução,émaisfácilentendercomutilizaraquelaAPIequaisasconsequênciasdo
usodaquelasolu çãonaquelecontexto.
AI nterfaceObserver e aCl a s s eObserv able
UmacuriosidadequepoucossabeméqueexistedesdeaJDK1.0ain-
terface java.util.Observereaclasse java.util.Observable.
Ainterface Observerpossuiométodo update()querecebecomo
parâmetroainstânciade Observablequegerouoeventoemaisumob-
jetoqueéoparâmetropassadoparaométodo notifyObservers().
Aideiadaclasse Observableéqueelasejaestendidaporclassesque
queiramemitirnotifica çõessobremudan çasemseuestado. Elapos-
suimétodosimplementadosparagerenciarenotificarasinstânciasde
Observer.
Oqueémaisinteressanteéqueessaclassenãoéutilizadaemnenhum
lugardaAPIdaJDK,mesmoopadrão Observersendoutilizadoem
diversoscontextos.Aquestãoprincipaléqueessasclassesconsideramo
Observercomoumaimplementa çãoprontaenãocomoumasolu ção
quepodeseradaptadaparadiversoscontextos.Pormaisqueasolu ção
apresentadaporessasclassessejareutilizável,dificilmenteelaserámais
adequadadoqueumaimplementa çãodopadrãoparaumcontextoes-
pecífico.
3.7 Considerações Finais doCapítulo
Essacapítuloapresentoucomoacomposi çãopodeserutilizadaparainserirpontos
deextensãoquepermitemqueumapor çãodelógicapossaserinseridadurantea
execuçãodeumaclasse.Essespontospodemserusadosparainserirumalógicaes-
pecíficadaaplicaçãooudeumdomínioemumaclassemaisgenérica,tornado-amais
7 4

## Página 96

CasadoCódigo Capítulo3. DelegandoComportamentocomComposição
reutilizável.Pormeiode hook classes,aadapta çãodecomportamentoéfeitaatravés
dacombinaçãodeobjetos,podendoodesenvolvedorcriarnovoscomponentespara
aconfiguraçãodeclassesfinal.
Aextensãodecomportamentopodeocorrerpordiferentesmotivoseemvaria-
doscontextos.Podeserdelegadaparaoutraclasseaexecu çãodeumalgoritmoque
podesertrocado,comoéocasodopadrão Strategy.Outrocenárioéadelegação
dalógicarelativaàsdiferen çasdeestadodeumobjeto,sendoesseofocodopadrão
State.Finalmente,opadrão Observerassociaaexecu çãodemétodosdediversas
outrasclassesàmudan çadeestadoouaeventosocorridosemumobjeto.
Alémdecompreenderospadrõeseessescenáriosquefavorecemousodacom-
posição,éimportantetambémconhecerosprincípioseconsequênciasportrásdes-
sasdecisões.Acomposi çãopodeinclusivesercombinadacomoutrostiposdeso-
lução,comonopadrão Bridgenoqualelaécombinadacomousodeheran çaem
umahierarquiadiferente.
75

## Página 98

Capítulo4
ComposiçãoRecursiva
“Recursão: ver recursividade. Recursividade: se ainda não entendeu, ver recursão”
–PiadaNerd
Nocapítuloanteriorfoivistocomoacomposi çãopodeserutilizadaparacom-
binarclassesdediferentestiposparapermitirqueafuncionalidadesejaestendida.
Atravésdopolimorfismo,aclassecompostapodeabstrairaimplementa çãodaclasse
queaestácompondo,permitindoquediversasclassesdiferentespossamsercoloca-
dasnaquelaposi ção.Agoraimagineseumaclassepudersercompostapelasuapró-
priaabstração,ou,emoutraspalavras,seelapossuirumatributodesuasuperclasse
oudeumadesuasinterfaces. Issopermitiriaqueumainstânciadamesmaclasse
pudesseserutilizadaparacompô-la,tornandopossívelacria çãodeumagrandees-
truturadessaforma.
Euseiqueissoparecesermuitoabstrato,masvamostentarpensaremumexem-
plodomundofísicoparailustraresseconceito.Imagineumape çadeLegoqueprovê
napartedecimaumaformaparaqueoutraspe çaspossamserencaixadase,naparte
debaixo,aformadoencaixeparaqueelasejaligadanapartedecima. Comoa

## Página 99

4.1. CompondoumObjetocomsuaAbstra ção CasadoCódigo
mesmapeçapossuiasduasformasdeencaixe,possívelligarecombinarváriaspe-
çasdomesmotipoemdiferentesconfigura ções.Quandoconsideramosquepodem
existirpeçasdiferentescomomesmoformatodeencaixe,aspossibilidadessãoainda
maiores.
Voltandoaomundodosoftware,écomoseaformaqueumape çaprovêemsua
partesuperiorfosseainterfacedaclasse.Analogamente,otipodeumatributoseria
oencaixedisponibilizadoparaqueumaoutrape çapossaseencaixar.Dessaforma,
umaclassequeimplementaumainterfaceseencaixaemumatributodaqueletipo.
Nacomposiçãosimples,utilizandoessaideiaépossívelconectarapenasdoisobjetos.
Masquandoumaclasseprovêumainterfaceeumatributodomesmotipo,épossível
criarumaestruturacomdiversosobjetos.Nessecaso,asprópriaspossibilidadesde
configuraçõesdessaestruturajátornamosoftwaremaisflexível.
4.1 Compondo um Objeto com sua Abstração
Arecursividadeéumconceitoamplamenteutilizadoemprograma ção.Umafun ção
recursiva,porexemplo,éaquelaquechamaasimesmacomopartedasualógica.Em
umalgoritmorecursivo,afun çãoéchamadanovamenteparadiminuiroproblema
queprecisaserresolvido.Dessaforma,elevaisendoreduzidoatéopontoemque
suaresoluçãoétrivial.Esseéchamadodepontodeparada.
Umexemploclássicoesimplesdefun çãorecursivaéofatorialdeumnúmero,
queconsistenamultiplica çãodetodososnúmerosinteirosepositivosmenoresou
iguaisàquelenúmero. Alistagemaseguirapresentaaimplementa çãodofatorial
utilizandorecursão.Observeque,peladefini çãodefatorial,ofatorialdeumnúmero
né nvezesofatorialde n-1. Ofatodequeofatorialde1é1éutilizadocomo
critériodeparada.
Listagem 4.1-Cálculodofatorialcomalgoritmorecursivo:
public static int fatorial(int n){
if(n == 1)
return 1;
return n * fatorial(n-1);
}
Quandocriamosumaestruturacomobjetos,épossívelutilizartambémocon-
ceitoderecursividadeparaqueelasejadefinidautilizandosuaprópriadefini ção.
Issoéfeitoquandoumaclassecontémumatributodoprópriotipodaclasse.Esse
78

## Página 100

CasadoCódigo Capítulo4. ComposiçãoRecursiva
tipodeestruturaémuitoutilizadoparadefinirmuitasestruturasdedados,como
listasligadas,árvoresegrafos.Porexemplo,noCapítulo 3foiapresentadabuscaem
profundidadedegrafos,ondeaclasseNopossuíaumalistadeinstânciasdeNo.
Paraexemplificarvamosconsiderarocódigodoelementodeumalistaligada
definidoaseguir. Aclasse Elementopossuiumatributo proximoquepossui
omesmotipo. Dessaforma,épossívelencadeardiversasinstânciasdessaclasse
formandoumalista. Ométodo contar() éummétodorecursivonoqualo
própriométodoéchamadonovamente,porémnainstânciaqueestivernoatributo
proximo. A condição de parada é quando um elemento não possui próximo,
significandoqueeleéoúltimoelementodalistaedeveretornarum. Sehouver
umpróximoelemento,entãoacontagemdeveretornarummaisacontagemdo
próximo.
Listagem 4.2-Exemplodeelementodelistaligada:
public class Elemento{
private Object valor ;
private Elemento proximo ;
public Elemento(Object valor ){
this.valor = valor;
}
public Object getValor(){
return valor;
}
public Elemento getProximo(){
return proximo;
}
public void setProximo(Elemento proximo ){
this.proximo = proximo;
}
public int contar(){
if(proximo == null)
return 1;
return 1 + proximo.contar();
}
}
Atéentãonãotemmuitadiferen çaentreasestruturasquepodemserconstruídas
emumalinguagemestruturada,comoC,emquepodem-secriarestruturasdeda-
79

## Página 101

4.1. CompondoumObjetocomsuaAbstra ção CasadoCódigo
dosutilizandoaconstru ção struct.Ograndediferencialdessadefini çãorecursiva
deestruturaséautiliza çãodopolimorfismo.Dessaforma,otipobaseutilizadona
estruturapodeserumainterfaceouumasuperclassequepossuemdiversasimple-
mentações.Sendoassim,diversostipospodemserutilizadosnacria çãodaestrutura
eaimplementa çãodeumpodeserabstraídapelosoutros.Adicionalmente,essaes-
truturatambémpodeserfacilmenteestendidaatravésdacria çãodenovostiposque
possuamamesmaimplementa ção.
AFigura 4.1apresentadiferentespossibilidadesparaaimplementa çãodacom-
posiçãorecursiva.Umadelaséelaserdefinidanasuperclasse.Dessaforma,todas
assubclassespoderãosercompostasporumaclassedahierarquia.Outrapossibili-
dadeéquandoacomposi çãorecursivaédefinidaemumaoumaissubclasses.Nessa
opção,apenasalgunstipospodemserutilizadosparaaimplementa çãodarecursi-
vidadeeoutrosserãopontosfinaisnaestrutura.Nessecapítuloserãoapresentados
padrõesqueutilizamessasdiferentesalternativasdeimplementa ção.
Figura4.1:PossibilidadesparaComposi çãoRecursiva
Éimportanteressaltarqueexistemvaria çõesdaspossibilidadesapresentadas.A
composição,porexemplo,podeserdeumaoumúltiplasinstâncias,oquegeraria
soluçõesdiferentes.Dependendododomínio,podetambémhavermaisdeumatri-
butoquepossuaumadefini çãorecursiva,masquepossuadiferentessignificados
paraaclasse. Emumaárvore,porexemplo,umalistadenóspoderepresentaros
nósfilhoseumatributosimplespoderepresentaropai.
80

## Página 102

CasadoCódigo Capítulo4. ComposiçãoRecursiva
4.2 Composite-Q uando um Conjunto é um Indivíduo
“Para sempre é composto de agoras. ”
–EmilyDickinson
Umdoserrosdepessoasqueestãoiniciandonaorienta çãoaobjetosémodelar
ocoletivoestendendooindivíduo.Umacestadema çãsnãoéumamaçãparaqueo
usodeheran çasejajustificado.Similarmente,umconjuntodeprocessos nãoéum
processo,logotambémnãoécorretoutilizarheran çapararepresentá-lo. Normal-
menteissoéfeitoparaasubclasseinvocardiretamenteosmétodosdasuperclassee,
dessaforma,asubclassedefineumnovoconjuntodemétodos,ignorandoainterface
públicadasuperclasse.
Apesardoquefoidito,existemsitua çõesemqueoconjuntotambémrepresenta
umúnicoindivíduo.Umconjuntodeprodutospodeserumproduto?Arespostaé
simdependendodocontexto.Umalojaouumsupermercadofrequentementemon-
tamkitscomdiversosprodutosquesãovendidoscomoumprodutoúnico.Como
representarissoemumsistema? Aquestãoéqueesseconjuntodeprodutosterá
umalógicadiferenteparadiversosfatores,comoparaocálculodopre ço,porexem-
plo.Porém,emoutroscenários,eledeveserconsideradocomoumprodutocomum.
Essase çãoapresentaopadrão Compositecujoobjetivoéproverumasolu-
çãoparaobjetosquerepresentamumconjuntodeobjetos,masquecompartilham
amesmaabstra çãodeles.Eletemopotencialdeencapsularumalógicacomplexa,
dividindo-aemumahierarquiadeclassesesimplificandoasolu çãofinal.Todosque
jáutilizaramum Compositeemumprojetorealsabemqueéumpadrãorealmente
muitopoderoso.
ApresentandooPadrãoComposite
Opadrão Compositepossuioobjetivodepermitirqueamesmaabstra ção
possaserutilizadaparaumainstânciasimpleseparaseuconjunto. AFigura 4.2
apresentaaestruturabásicausadanopadrão.Umaabstra çãoapresentaumainter-
facebásicacomasopera çõesquedevemserexecutadastantonosobjetossimples
quantonoscompostos.Aclasse Simplesrepresentaumúnicoindivíduoeaclasse
Compostorepresentaoconjunto. Observequeexisteumarela çãodecomposi ção
entre Compostoe Abstracao,quemostraqueumobjetodaclasse Composto
podesercompostoporoutrotambémdaclasse Composto.
81

## Página 103

4.2. Composite-QuandoumConjuntoéumIndivíduo CasadoCódigo
Figura4.2:EstruturaBásicadoComposite
Asoperaçõesdefinidasnaabstra çãodevemserimplementadasemtodasassub-
classes.Paraassubclassessimples,quenãoforemcompostasporoutrasdotipoda
abstração,podeserumaimplementa çãodireta.Porexemplo,umaclasse Produto
podedisponibilizarummétodopararetornaropre çoepossuirapenasoacessoa
umatributo.Osegredodopadrão Compositeestánaimplementaçãodosmétodos
compostos,quedeveminvocarosmétodosdasinstânciasqueocompõeeexecutar
umalógicaparacriarumresultadoúnico.Noexemplodoproduto,oprodutocom-
posto,umaclasse KitProdutos,pararetornaropre çoelepoderiasomaropre ço
dosprodutosqueocompõeedarumdescontoemcima.
Osobjetosorganizadoscomopadrão Compositeacabamseguindoumaestru-
turadeárvore.Asfolhasseriamasclassessimples,quenãopossuemacomposi ção.
ApesardenodiagramadaFigura 4.2apenasumtipodeclassesimplesserrepre-
sentado,éimportanteressaltarquepodemhaverdiversasclassesdessetipocomdi-
ferentesimplementações. Osramosseriamrepresentadospelasclassescompostas,
queseriamcompostaspelosseusfilhos.Onúmerodefilhosdeumaclassecomposta
variacomanecessidadedaaplica ção,podendoserduasinstânciasouumconjunto.
Ograndebenefíciodo Compositeétornartotalmentetransparenteparaos
clientesofatodeestaremtrabalhandocomumobjetosimplesoucomposto. Isso
tornamuitosimplesadicionarumaimplementa çãodeumobjetocompostoemuma
hierarquiajáexistentenaaplica ção.
82

## Página 104

CasadoCódigo Capítulo4. ComposiçãoRecursiva
Composite em Componentes Gráficos
Umcontextoemqueopadrão Compositeémuitoutilizadoéparaa
criaçãodecomponentesgráficos.Muitossãoformadosapartirdacom-
posiçãodeoutroscomponentesexistentes,porémsãotratadoscomoum
só.Porexemplo,umcomponentedesele çãodearquivosnormalmente
possuibotõeseumacaixadetexto. Dessaforma,quandoummétodo
setEnable()forchamado,eledeverácoordenarainvoca çãodessemé-
todoemtodososseuscomponentesinternos.
EmJava,esseconceitoéutilizadoemsuítesgráficasparaaplica ções
desktop,comonoSwingenoSWT,eemframeworkscomcomponentes
parapáginasweb,comooJSF.OframeworkSwingBean,porexemplo,
possuiumquerepresentaumformulárioeécompostopordiversosou-
troscomponentes.
ModelandoaRepresenta çãodeTrechosAéreos
Paraexemplificaraaplica çãodopadrão Composite,vamosmodelarasclasses
querepresentamtrechosaéreosemumaaplica çãodeturismo. Paraesseexercício
vamosconsiderarqueasinforma çõesprincipaisdeumtrechoaéreosãosuaorigem,
seudestinoeoseupre ço. Muitasvezes,quandoumclientesolicitaumvooapar-
tirdeumaorigemeumdestino,nãoexisteumvoodiretoqueconectaaquelesdois
aeroportos.Nessecaso,normalmentebusca-seentãoumvooquepousaemumae-
roportointermediário,deondeoclientepodepegarumoutrovooatéoseudestino.
Nessecaso,alémdopre çodosdoistrechos,deve-seadicionarataxadeconexãoco-
bradapeloaeroportointermediário.Aquestãoéindependentedotrechoaéreoser
compostopormaisdeumtrechoounão,emcertospontososistemadevetratá-los
deformasimilar.
Oprimeiropassoéadefini çãodeumainterfacequeirádefinirquaisservi ços
serãodisponibilizadospelaclassequerepresentarotrechosimpleseocomposto.
Peladescriçãodoproblema,otrechodevesercapazderetornaraorigem,odestino
eopre ço.Sendoassim,alistagemaseguirapresentaainterface TrechoAereoque
definemétodospararecupera çãodessasinforma ções.Emseguida,éapresentadoo
códigodaclasse TrechoSimples,quepossuiumaimplementa çãocujalógicaé
apenasoacessoaatributos.
83

## Página 105

4.2. Composite-QuandoumConjuntoéumIndivíduo CasadoCódigo
Listagem 4.3-Interfacequedefineosservi çosdeumtrechoaéreo:
public interface TrechoAereo {
public String getOrigem();
public String getDestino();
public double getPreco();
}
Listagem 4.4-Representaçãodeumtrechoaéreosimples:
public class TrechoSimples implements TrechoAereo{
private String origem ;
private String destino ;
private double preco;
public TrechoSimples(String origem , String destino , double preco) {
this.origem = origem;
this.destino = destino;
this.preco = preco;
}
public String getOrigem() {
return origem;
}
public String getDestino() {
return destino;
}
public double getPreco() {
return preco;
}
}
Paraaimplementaçãodotrechocomposto,seráaplicadoopadrão Composite.
Nessecaso,otrechocompostopossuidoisatributos,respectivamentepararepresen-
taroprimeiroeosegundotrechoqueocompõe. Tambémexisteumatributoque
representaataxadeconexãoaserpagadeformaadicionalaopre çodecadatrecho
individualmente.Notequenoconstrutoréfeitaumaverifica çãoseosegundotre-
chocomeçanomesmolocalemqueoprimeirotermina. Podeserobservadoque
asoperaçõesqueprecisavamserimplementadasdelegampartedaexecu çãoparaos
trechosquecompõemoobjeto.
Listagem 4.5-Representaçãodotrechoaéreocomposto:
84

## Página 106

CasadoCódigo Capítulo4. ComposiçãoRecursiva
public class TrechoComposto implements TrechoAereo {
private TrechoAereo primeiro ;
private TrechoAereo segundo ;
private double taxaconexao;
public TrechoComposto(TrechoAereo primeiro , TrechoAereo segundo ,
double taxaconexao) {
this.primeiro = primeiro;
this.segundo = segundo;
this.taxaconexao = taxaconexao;
if(primeiro.getDestino() != segundo.getOrigem())
throw new RuntimeException("O destino do primeiro" +
"não é igual a origem do segundo" );
}
public String getOrigem() {
return primeiro.getOrigem();
}
public String getDestino() {
return segundo.getDestino();
}
public double getPreco() {
return primeiro.getPreco() + segundo.getPreco() +
taxaconexao;
}
}
AFigura 4.3apresentaumexemplodecomoumvoocomtrêstrechosseriare-
presentadoutilizandoaestruturadeclassesapresentada.Aseguirtambémémos-
tradaumalistagemcomocódigoparaacria çãodostrechossimplesecompostos.
Observepeloexemplo,que TrechoCompostopodesercompostotantoporins-
tânciasde TrechoSimplesquantoporinstânciasdopróprio TrechoComposto
deformatransparente,criandoumaestruturadeárvore.
85

## Página 107

4.2. Composite-QuandoumConjuntoéumIndivíduo CasadoCódigo
Figura4.3:Representa çãodetrechosaéreos
Listagem 4.6-Criaçãodetrechoscompostos:
TrechoSimples ts1 = new TrechoSimples("São Paulo" , "Brasília", 500);
TrechoSimples ts2 = new TrechoSimples("Brasília", "Recife", 300);
TrechoSimples ts3 = new TrechoSimples("Recife","Natal", 350);
TrechoComposto tc1 = new TrechoComposto(ts2, ts3, 30);
TrechoComposto tc2 = new TrechoComposto(ts1, tc1, 50);
Por que TrechoComposto não pode estender Trecho-
Simples?
Podeparecertentadoraprincípiofazercomque TrechoComposto
estenda TrechoSimplesemvezdecriarumainterfacecomumentre
asduas.Seissoocorresse,aclasse TrechoCompostoiriasimplesmente
ignoraraestruturadedadosdaclasse TrechoSimpleseaindateria
quelidarcomseuconstrutor.Issogerariaummalcheirodecódigocha-
madode Refused Bequest,queocorrequandoumasubclassenãoutiliza
aestruturaeosmétodosherdadosdasuasuperclasse. Paraqueaquela
herançaédadaparaaclasseseelanãoautiliza?
86

## Página 108

CasadoCódigo Capítulo4. ComposiçãoRecursiva
4.3 Encadeando Execuções com Chain ofResponsi-
bility
“Nenhuma corrente pode ser mais forte que seu elo mais fraco. ”
–ProvérbioPopular
Quandoemumsoftwareumafuncionalidadeéexecutada,normalmenteexistem
diversospassosqueprecisamserexecutadosemsequência. Adificuldadeocorre
quandoprecisa-sedeflexibilidadenaconfigura çãodessespassos.Porexemplo,pode
sernecessáriaamodifica çãodaordemdospassoseatémesmoparaainser çãode
novospassos.Umoutroobjetivoseriaapossibilidadedereutiliza çãodessespassos
emoutrosprocessamentosouparaoutrasaplica ções.
Chain of Responsibility éumpadrãodeprojetoquecriaumacadeia
deexecuçãonaqualcadaelementoprocessaasinforma çõeseemseguidadelegaa
execuçãoaopróximodasequência.Emsuaimplementa çãotradicional,oselemen-
tossãopercorridosatéqueumdelesfa çaotratamentodarequisi ção,encerrando
aexecuçãodepoisdisso.Comoalternativa,tambémépossívelcriarumacadeiade
execuçãoondecadaumexecutasuafuncionalidadeatéqueacadeiatermineouela
sejaexplicitamentefinalizadaporumdoselementos.
RecuperaçãodeumArquivoRemoto
Paraficarmaisconcretooentendimentodopadrão,imaginequeumarquivo,
comoumalistadecertificadosdigitaisrevogados,éatualizadodeformaperiódica
emumservidorremoto,contendoadataemquesuavalidadeéexpirada.Paratornar
recuperaçõesfrequentesmaiseficientesaaplica çãocrioudoistiposdecache,sendo
umemmemóriaeoutronabasededados.Dessaforma,primeiroverifica-seseexiste
umarquivoválidoemmemória,emseguidanobancodedadosesomenteentão,se
nãoforencontrado,oarquivoérecuperadodoservidorremoto.
Emumaimplementa çãotradicional,todaessalógicaseriaimplementadana
mesmaclasse,comdiversoscondicionaisemsequênciaparaverificarseumadeter-
minadaestratégiaseriaadequadapararecupera çãodoarquivo.Utilizandoopadrão
Chain of Responsibility ,cadapossibilidadeéimplementadaemumaclasse
diferente,asquaissãoencadeadasemumfluxodeexecu ção.Cadaumadelasverifica
seoarquivoexisteeéválido,retornandoomesmoemcasopositivoedelegandoa
execuçãoparaapróximainstânciadacadeiaemcasonegativo.AFigura 4.4repre-
sentaessacadeiadeexecu ção.
87

## Página 109

4.3. EncadeandoExecuçõescomChainofResponsibility CasadoCódigo
Figura4.4:CadeiadeExecu çãoparaRecupera çãodeArquivo
Para implementarmos essa sequência de execução, o primeiro passo é
definirmos uma superclasse que define um elemento da cadeia. A classe
RecuperadorArquivo, apresentada na próxima listagem, possui um atri-
butodoseumesmotipochamado proximoquerepresentaopróximoelemento.
Essaclassetambémdefineummétodoabstratochamado recuperarArquivo()
que é umhook method quedeveserimplementadopelassubclassesparaarecu-
peraçãodoarquivodeacordocomaestratégiadesejada. Alémdisso,ométodo
chamarProximo()éresponsávelporverificarseexisteumpróximoelementoe
invocá-lo. Adicionalmente,ométodo recuperar()tentarecuperaroarquivo,
retornando-oseeleforválidoechamandoopróximoelementodacadeiaemcaso
negativo.
Listagem 4.7-ClasseabstrataquedefinealógicadoChainofResponsibility:
public abstract class RecuperadorArquivo {
private RecuperadorArquivo proximo ;
public RecuperadorArquivo(RecuperadorArquivo proximo ) {
this.proximo = proximo;
}
public Arquivo recuperar(String nome ){
Arquivo a = recuperaArquivo(nome);
if(a==null || ! a.isValido())
return chamarProximo(nome);
else
return a;
}
88

## Página 110

CasadoCódigo Capítulo4. ComposiçãoRecursiva
protected Arquivo chamarProximo(String nome ) {
if(proximo == null)
throw new RuntimeException("Não foi possível " +
" recuperar o arquivo" );
return proximo.recuperar(nome);
}
protected abstract Arquivo recuperaArquivo(String nome );
}
Cada subclasse de RecuperadorArquivo deve implementar o método
recuperaArquivo()buscandooarquivoemumafontediferente.Peladescri ção
doproblema,asimplementa çõesirãobuscaroarquivonobancodedados,deum
cacheemmemóriaedeemumservidorremoto. Alistagemaseguirapresenta
aclassequefazabuscaemumcacheemmemóriaparaexemplificarcomoseria
umadessasimplementa ções.Ométodo recuperaArquivo()verificaseexisteo
arquivonomapaeretornanulocasonãoexista.Paraarmazenarnovosarquivosno
mapa,ométodo chamarProximo()tambéméimplementadoparapermitirque
setenhaacessoaoarquivoretornadopelopróximo.
Listagem 4.8 - Classe que define o recuperador que define o cache em memó-
ria:
public class RecuperadorCacheMemoria extends RecuperadorArquivo {
private Map<String, Arquivo> cache = new HashMap<>();
public RecuperadorCacheMemoria(RecuperadorArquivo proximo ) {
super(proximo);
}
protected Arquivo recuperaArquivo(String nome ) {
if(cache.containsKey(nome))
return cache.get(nome);
return null ;
}
protected Arquivo chamarProximo(String nome ) {
Arquivo a = super.chamarProximo(nome);
cache.put(nome, a);
return a;
}
}
89

## Página 111

4.3. EncadeandoExecuçõescomChainofResponsibility CasadoCódigo
Alguém viu um TemplateMethod?
Desafiooleitoraobservarmelhoroexemplodecódigodessase-
çãoeacharumaimplementa çãodopadrão Template Method! O
método recuperar()daclasse RecuperadorArquivoimplementa
umalógicacomumaoselementosdacadeiadeexecu çãoedelegaos
pontosvariáveisa hook methods queserãoimplementadospelassub-
classes. Observe que o métodochamarProximo(), também cha-
mado pelo Template Method, apesar de nao ser abstrato, tam-
bémpodeserconsideradoum hook method. Peloexemplodaclasse
RecuperaCacheMemoriapode-sepercebercomoelepodesersobres-
critopelasubclasseparaaadi çãodafuncionalidade.
Comojáressaltamos,écomumhaverumaliga çãoforteentrediferen-
tespadrõesdeprojeto.Muitasvezeselesaparecememconjuntoeatéé
difícildiferenciá-los.
EstruturaeAlternativasdeImplementa ção
Opadrão Chain of Responsibility colocacadaelementoqueirápartici-
pardoprocessamentodalógicacomooelementodeumalistaligada,ondecadaum
temacessoaopróximonacadeiadeexecu ção.AFigura 4.5mostracomoacomposi-
çãorecursivaéutilizadanaimplementa çãodaestruturadeclasses.Nessecaso,uma
hook classdomesmotipoédefinidanasuperclasse,significandoquetodotipode
elementodacadeiapodesercompostoporumpróximo.Casoelesejanulo,oupos-
suaumelementoquerepresenteum Null Object,serámarcadoofinaldacadeia
deexecução.
90

## Página 112

CasadoCódigo Capítulo4. ComposiçãoRecursiva
Figura4.5:EstruturadoChainofResponsibility
Nessarepresentação,ométodo executar()disponibilizacomoAPIpública
aexecuçãodetodoselementosdacadeiaeométodo executarElemento()re-
presentaaexecu çãodalógicasomentedaqueleelemento. Dessaforma,ométodo
executar()invocaprimeiroalógicaimplementadanaprópriaclasseeemseguida
invocadeformarecursivaoprópriométodo executar()nopróximoelemento.
Comoalternativadeimplementa ção,ométodo executarElemento()pode
recebercomoparâmetroopróximoelemento,sendotambémresponsávelpelasua
invocação.Dessaforma,cabeàimplementa çãodecadaclassedecidiremquesitu-
açõesopróximodeveserinvocadoeemquemomentoissodeveacontecer. Utili-
zandoessaalternativa,cadaimplementa çãopodeincluirlógicaqueseráexecutada
tantoantesquantodepoisdaexecu çãodele.
Apartirdaimplementa çãodo Chain of Responsibility adquire-seuma
grandeflexibilidadeparaaconfigura çãodalógicaqueseráexecutada. Porexem-
plo, facilmenteumnovoelementodacadeiapodeserintroduzido, ouumexis-
tente pode ser excluído. A própria ordem em que os elementos são organiza-
dospodegerarumagrandediferen çanofinal. Porexemplo,paraautiliza çãodo
RecuperadorArquivoemdispositivoscommemóriaRAMlimitada,oelemento
quefazocacheemmemóriapoderiafacilmenteserexcluídodacadeia.Emumoutro
cenárioemqueoarquivopudesseestardisponívelemmaisdeumservidor,maisins-
tânciasdoelementoqueobuscaremotamentecomendere çosdiferentespoderiam
serincluídas.
91

## Página 113

4.3. EncadeandoExecuçõescomChainofResponsibility CasadoCódigo
FiltrosemAplica çõesWeb
Umexemplodousodo Chain of Responsibility emAPIsdoJavaEEsão
osfiltrosdeaplica çõesweb[ 21].Umexemplodaestruturabásicadeumfiltroestá
representadanapróximalistagem.Aclassequerepresentaofiltrodeveimplementar
ainterface Filtere,alémdeimplementarosmétodos init()e destroy()
queservemrespectivamenteparaainicializa çãoefinaliza ção,aindaéprecisoincluir
ométodo doFilter()queéondealógicaseráefetivamenteimplementada.
Listagem 4.9-ExemplodeFiltroparaAplica çõesWeb:
public class FiltroExemplo implements Filter{
public void doFilter(ServletRequest req ,
ServletResponse resp ,
FilterChain chain ){
//antes do próximo filtro
chain.doFilter(req,resp);
//depois do próximo filtro
}
public void destroy{}
public void init(FilterConfig config ){}
}
Ométodo doFilter()recebecomoumdosparâmetrosumainstânciada
classe FilterChain,querepresentajustamenteacadeiadefiltrosqueestásendo
executada.Aoserchamadoométodo doFilter()nessainstância,ocontroleda
execuçãoépassadoparaopróximofiltroou,senãohouverpróximo,paraoservlet
queirátratararequisi ção. Observequecomoopróximofiltroéinvocadodentro
dométodo doFilter(),podeseradicionadafuncionalidadetantoantesquanto
depoisdasuaexecu ção.Inclusiveopróximofiltronemprecisaserinvocado,como
nocasodarequisi çãoserdirecionadaaumapáginadeerro.Outracoisaquepode
serfeitaéamodifica çãodosparâmetrosqueserãopassadosparaospróximosfiltros,
inclusiveencapsulando-oscomautiliza çãode Proxies(umpadrãoqueserávisto
nopróximocapítulo).
Umdosusosmaisclássicosparafiltrosemaplica çõeswebéparaverificarseo
usuárioestálogado.Nessecaso,eleverificaseexisteumusuárioválidonasessãoe
92

## Página 114

CasadoCódigo Capítulo4. ComposiçãoRecursiva
redirecionaparaapáginadeloginemcasonegativo. Porémexistemváriosoutros
usosparafiltros,como:realiza çãodecontroledeacesso;fazerumabuscaporparâ-
metrosmaliciosos;iniciarefinalizarumatransa çãocomabasededados;emodificar
asaídageradapeloservlet.Emgeralosfiltrossãoutilizadosparafuncionalidadesque
precisamserexecutadasemdiversasrequisi çõesdiferentes.Autiliza çãodo Chain
of Responsibility emsuaimplementa çãopermitequeaordemdosfiltrosseja
modificadaequefiltrospossamserfacilmenteintroduzidosouremovidos.
Essamodelagemutilizadaparaosfiltrosémesmados interceptorsdoframework
Struts2[ 7].Um interceptortemumafun çãobemparecida,queéderealizaralgum
processamentoantese/oudepoisdotratamentodeumarequisi çãoweb. Grande
partedasfuncionalidadesdoframework,comoainje çãodosparâmetrosdo r e q u e s t
ouaintrodu çãodeobjetosdasessãodousuário,éimplementadaatravésdos i n t e r -
ceptors.Osinterceptorsqueatuamparacadarequisi çãosãoconfiguradosatravésde
umarquivoXML.Nessecaso,autiliza çãodopadrão ChainofResponsibility per-
mitequeessescomponentesdoframeworkpossamserfacilmenteremovidosouque
novoscomponentesespecíficosdaaplica çãopossamseradicionados.
4.4 Refatorando para Permitir a Execução de Múl-
tiplasClasses
U m a e v o l uçãocomumqueocorreemaplica çõeséanecessidadedequemaisuma
açãosejarealizadacomorespostaaumevento.Porexemplo,imaginequeaorece-
berumainforma çãoaaplica çãoprecisepersisti-laemumabasededados. Como
tempo,novosrequisitosvãosurgindoeexigemquenovasa çõessejamtomadasna-
quelecenário,comoachamadadeumservi çoremotoouoregistroemumatrilhade
auditoria.Oobjetivodessarefatora çãoépermitirque,nachamadadeummétodo,
diversasclassespossamserexecutadas.Issodeveserrealizadodeformaquenãohaja
umacoplamentoentreessasclassesequeissosejatransparenteaosqueinvocam.
Paraqueessarefatora çãopossaserrealizada,éimportantequeaexecu çãodessa
funcionalidadejáestejaisoladautilizandoacomposi çãosimples.Ouseja,queapar-
tirdeuma hook classconfiguradasejapossíveltrocaralógicaqueseráexecutada,mas
nãoincluirmúltiplasclassesparaaexecu ção.Diferentementedopadrão Observer,
noqualaclasseobservadaprecisagerenciaraexistênciademúltiplosobservadores,
nessecasoédesejávelqueaexistênciademúltiplasexecuçõessejatransparentepara
aclasse.
Paramostrararefatora çãoparaosdoispadrõesapresentadosnessecapítulo,
93

## Página 115

4.4. RefatorandoparaPermitiraExecu çãodeMúltiplasClasses CasadoCódigo
seráretomadooexemplodaclasse GeradorArquivo. Oobjetivoserápermitir
quediversospós-processadorespossamatuaremcimadoarquivogeradodeforma
transparenteparaaclasseprincipal. Apósopadrão Bridge,existeumainter-
facechamada PosProcessadorquedeveserimplementadaporqualquerimple-
mentaçãoqueirácomporaclasse GeradorArquivos.Noexemplo,osdoispós-
processadoresexistentesrespectivamentecriptografamecompactamoarquivoapós
asuagera ção.Observequeseambosforemutilizados,aordemdeprocessamento
iráalteraroresultadofinal,poisumarquivocriptografadoecompactadoédiferente
deumarquivocompactadoecriptografado.
As seçõesaseguirdescrevemcomocadaumdospadrõesapresentadosnessa
seçãopoderiamserimplementadospararesolveroproblemacomosrequisitosdes-
critos.
IntroduzindoumComposite
Paraimplementaropadrão Composite,oqueprecisaserfeitoéaimplementa-
çãodeumaclassequepossuaamesmainterfacedeumpós-processadoresejacapaz
decoordenaraexecu çãodediversospós-processadores. Alistagemaseguirmos-
traaclasse PosProcessadorCompostoquedesempenhaessepapel.Observeque
elaécompostaporumarraydepós-processadoresquesãorecebidosnoconstru-
tor.Adicionalmente,ométodo processar()executaomesmométododeforma
recursivanasinstânciasde PosProcessadorquecompõemaclasse.
Listagem 4.10-Criaçãodeumpós-processadorcomposto:
public class PosProcessadorComposto implements PosProcessador{
private PosProcessador[] processadores;
public PosProcessadorComposto(PosProcessador... p){
processadores = p;
}
public byte [] processar( byte[] bytes){
for(PosProcessador p : processadores){
bytes = p.processar();
}
return bytes;
}
}
Agrandevantagemdousodo Composite nessecasoéqueelenãoexige
94

## Página 116

CasadoCódigo Capítulo4. ComposiçãoRecursiva
nenhumamudançanasclassesexistentes. Aclasse PosProcessadorComposto
podeseradicionadafacilmentenaclasse GeradorArquivo etodososoutros
pós-processadorespodemfacilmenteserincluídosnela. Adificuldadedeusaro
Compositeiráapareceremcenáriosondeaintegra çãoentreasclassesenvolvidas
nãoacontecesempredamesmaforma.Issopodeexigiracria çãodediversasclasses
quedesempenhamessepapel,maspossuemumalógicadeintegra çãodiferente.
RefatorandoparaChainofResponsibility
Umaoutraabordagemparaarefatora çãoseriaimplementaropadrão Chain
of Responsibility parapermitirqueospós-processadorespossamserorgani-
zadosemumacadeiadeprocessamento.Issovaiexigirumamudan çanaabstra ção
querepresentaumpós-processadorparaincluiracomposi çãorecursiva,ouseja,
paraaadi çãodeuma hook classquerepresenteopróximoprocessadordacadeia.A
interface PosProcessadorprecisariaserrepresentadacomoumaclasseabstrata,
cujalistagemestáapresentadaaseguir.
Listagem 4.11-ClassePosProcessadorparaacria çãodeumacadeiadeprocessa-
mento:
public abstract class PosProcessador{
private PosProcessador proximo ;
public PosProcessador(PosProcessador prox ){
proximo = prox;
}
public PosProcessador(){
proximo = nem PosProcessadorNulo ();
}
public byte [] processarCadeia( byte[] bytes){
bytes = processar(bytes);
return proximo.processarCadeia(bytes);
}
protected abstract byte [] processar( byte[] bytes);
}
Aclasse PosProcessadorpossuioatributo proximodeseuprópriotipo,
quedeveserpassadonoconstrutor. Casosejaofinaldacadeia,umconstrutor
vazio pode ser invocado, o qual irá configurar umNull Object no atributo
95

## Página 117

4.5. ConsideraçõesFinaisdoCapítulo CasadoCódigo
proximo. Ométodoabstrato processar() representaalógicadeprocessa-
mentoespecíficadaquelaimplementa çãoqueseráinvocadaduranteaexecu çãoda
cadeia-e,porelenãopoderserinvocadodefora,suavisibilidadeé protected.
Ométodo processarCadeia()éoresponsávelpelaexecu çãodacadeiaein-
vocanãosomenteométodo processar()daprópriaclasse,quantoométodo
processarCadeia()doatributo proximo.
Diferentementedaimplementa çãodo Composite,essarefatora çãotemum
pequenoimpactonasoutrasclassesenvolvidas. Porexemplo,asclassesquein-
vocampós-processadoresprecisarãoalterarométodoqueestásendochamadode
processar()para processarCadeia(). Elepoderiasermantido,porémàs
custasdeumamudan çanonomedo hook methodqueprecisasercriadonospós-
processadores. Ouseja,comoométododisponívelpublicamentenãoseriamaiso
pontodeextensão,onomedealgumdelesprecisasermodificado.Outrasmudan-
çasdevemserfeitasnassubclasses,queprecisamdisponibilizaronovoconstrutor
querecebeum PosProcessadorcomoparâmetroealterarde implementspara
extendsarelaçãocom PosProcessador,quenãoémaisumainterface.
4.5 Considerações Finais doCapítulo
Essecapítuloapresentouconceitosarespeitodacomposi çãorecursiva,naqualob-
jetossãocompostosporoutrosquepossuemumadesuasabstra ções.Comautiliza-
çãodopolimorfismo,épossívelcombinardiversasimplementa çõesdeumamesma
abstraçãoformandoumaestruturaflexívelecomplexa.Apartirdacria çãodenovas
classesesuainclusãoemumdeseuspontospode-seestenderoseucomportamento.
Aprópriaorganiza çãodasclassesnãodeixadeserumpontoquepodeseradaptado
econfigurado.
Opadrão Compositeutilizaesseconceitoparapermitirarepresenta çãode
objetoscompostos,emoutraspalavras,objetosquecombinamafuncionalidadede
outrosdomesmotipo.Comessepadrão,umadassubclasseséquempossuiacom-
posiçãorecursiva.Nessepadrãoasclassesseorganizamemformadeárvore,sendo
ascompostasosnósinternoseasoutras,asfolhas.
Já oChain of Responsibility criaumaestruturaparecidacomumalista
ligada,naqualcadaelementopossuiumareferênciaparaopróximo.Acomposi ção
recursivanormalmenteéimplementadanasuperclasse,poistodotipodeelemento
devepoderterumpróximo.Apartirdesseencadeamentodeclasses,épossívelcon-
figurarquaiselementosdevemserincluídosnoprocessamento.
96

## Página 118

CasadoCódigo Capítulo4. ComposiçãoRecursiva
Autilizaçãodessetipodeestruturanormalmenteéligadaànecessidadedefle-
xibilidadeeconfigurabilidadedalógicadaaplica ção. Arecursividadedasolu ção
permiteodesacoplamentoentreoselementoseacria çãodediversaspossibilidades
deconfiguração.
97

## Página 120

Capítulo5
EnvolvendoObjetos
“Não existe colher. Você verá que não é a colher que se dobra, apenas você mesmo. "
–Garotocomacolher,Matrix
Oencapsulamentoéumacaracterísticaquefazcomqueosclientesdasclasses
precisemconhecerapenasasuainterface,abstraindosuaimplementa çãointerna.O
polimorfismopermitequeainstânciadeumaclassepossaseratribuídaaumava-
riável,desdequeobedeçaàabstra çãoutilizadacomotipo.Essasduascaracterísticas
fazemcomqueexistaumaignorância,nosentidocorretodapalavra,daclassecliente
emrelaçãoàclassecomqueelarealmenteestálidando.
Apartirdessesconceitos,épossívelqueumaclasseenvolvaumainstânciasem
queaclientesaibaqueestálidandocomoutroobjeto.Dessaforma,elaservirácomo
intermediáriaentreaclasseclienteeaclassealvo.Comisso,elaobtémocontroleda
execuçãoantesedepoisdecadainvoca çãodemétodo.Issopermiteque,porexem-
plo,funcionalidadessejamadicionadasequevalida çõessejamrealizadas. Pode-se
inclusiveinterceptaraexecu çãodeummétodo,retornandoumvaloroulan çando
umerromesmoseminvocarométodooriginal.

## Página 121

5.1. ProxieseDecorators CasadoCódigo
Essecapítuloapresentaospadrõeseconceitosrelacionadosaesseencapsula-
mentodeobjetos.Estemesmoconceitopodeserutilizadoparaprotegerumobjeto,
adicionarfuncionalidadeseatémesmoadaptarinterfaces. Serámostradoqueum
dosgrandespoderesdessatécnicaéfazerocódigoclientepensarqueaindaestá
lidandocomoobjetooriginalefazerqueesseobjetonãosaibaqueestásendoen-
volvido.
5.1 Proxies eDecorators
“O olhar é, antes de mais nada, um intermediário que remete de mim a mim mesmo. ”
–Sartre
Diferentementedoscapítulosanteriores,voucome çarjáapresentandodoispa-
drõesaomesmotempo. Omotivoparaissoéqueopadrão Proxypossuiuma
estruturamuitoparecidacomopadrão Decorator,sendoqueadiferen çaébasi-
camenteamotiva çãoeocontextonoqualospadrõessãoaplicados.
Aideiabásicadessespadrõesécriarumaclassequeenvolveumaoutradomesmo
tipo.Dessaforma,elapodeserpassadadeformatransparentecomosefosseaclasse
originalparaquemairáutilizar. AFigura 5.1representaofuncionamentodesses
padrões.
Figura5.1:Envolvendoumobjeto
Autilizaçãodessetipodetécnicatrazumanovaperspectivaparaamodelagem
declasses,poisaoinvésdeconcentrartodososaspectosdeummétodoemapenas
uma,épossíveltratardiferentesquestõesemdiferentescamadas.Assimafuncionali-
dadedaclassequeestáencapsulandopodeserutilizadaparaváriasimplementa ções.
100

## Página 122

CasadoCódigo Capítulo5. EnvolvendoObjetos
Paraficarmaisconcreto,umavalida çãodeparâmetrosquenormalmenteéfeitaden-
trodosmétodospoderiasercolocadaemumaclassequeenvolveaclasseprincipal.
Dessaforma,essavalida çãopoderiaserreutilizadaparadiversasimplementa ções.
AEstruturadosPadrões
Aestruturado Proxyedo Decoratorutilizaacomposi çãorecursiva. Isso
significaqueambossãocompostosporumaclassequepossuiamesmaabstra ção
queeles. AestruturadessespadrõesestáapresentadanaFigura 5.2. Observeque
sãomuitosimilaresepermitemqueainstânciadeumaclasseencapsuleumobjetoe
possaassumiroseulugar.Dessaforma,osclientesdelanãoterãoconhecimentode
seestãolidandocomaoriginaloucomumaqueaestáencapsulando.
Figura5.2:EstruturadospadrõesProxyeDecorator
Opadrão Decoratorrecebeuessenomerelacionadoaofatode“decorar”uma
classeexistenteadicionandoumanovafuncionalidade. Imaginecomoseaclasse
principalfosseumquadroeo Decoratorfosseamoldura,queestáacrescentando
elementosnovisualdoquadro.Oprincipalobjetivodessepadrãoéacrescentarfun-
cionalidadesaclassesexistentesdeumaformatransparenteaquemasutiliza.Isso
tambémpodeserutilizadoparaumamelhordistribui çãoderesponsabilidades,per-
mitindoqueaprincipalsefoquenaregradenegóciocentralequeoutrasclassesque
aencapsulamcuidemdeoutrasfuncionalidades.
Opadrão Proxyestámaisligadoaproverumobjetoparaservircomointerme-
diárionacomunicaçãocomumoutroprincipal.Umexemplocomumdeutiliza ção
101

## Página 123

5.1. ProxieseDecorators CasadoCódigo
dessepadrãoépararepresentarlocalmenteobjetosqueestãoemservidoresremotos.
Dessaforma,oproxyencapsulaalógicadeacessoremotofazendoparecerqueoob-
jetoestásendoacessadolocalmente.Umoutroexemploéparaacria çãodeobjetos
“caros”,ouseja,quepossuemumaltocustocomputacionaldeconsumoderecur-
sosparacria ção.O Proxypodeservircomoumarepresenta çãoparaesseobjeto,
permitindoqueomesmosejacriadosomentequandofornecessário.
Umacoisainteressantedaestruturadeambosospadrõesésuacomposi çãore-
cursivaquepermitequesejafeitoumencadeamentodeclasses,deformasimilar
ao Chain of Responsability .Sendoassim,um Proxyou Decoratorpode
nãosomenteencapsularaclasseoriginal,mastambémencapsularumaclasseque
jáestejaencapsuladacomumoutro Proxyou Decorator.Dessaforma,aclasse
ficacomdiversascamadas,cadaumacomumaresponsabilidadediferente,encap-
sulandoaregradenegócioprincipal.
Aprincipaldiferen çaentreosdoispadrõesestánoobjetivodecadaum. En-
quantoo Decoratorvisaadicionarnovasfuncionalidades,o Proxyservemais
comoumaprote çãoaoobjetoprincipal. Emtermosdeestrutura,o Decorator
costumapermitirqueoobjetoencapsuladosejapassadonoconstrutor,ouconfigu-
radodealgumaoutraforma.Dessemodo,acomposi çãoéfeitautilizandoaabstra-
ção,permitindoquequalquerimplementa çãosejaencapsulada.Jáo Proxy,muitas
vezes,protegeumobjetoespecíficoeacria çãodoobjetoencapsuladoocorreden-
trodele. Nocasodeum Proxyquefaçaacessoremoto,elenemcompõeaclasse
propriamentedita,masutilizaasclassesdeacessoàredeparadelegaraschamadas.
Porémessadiferençaestruturalémuitosutilepodeatémesmoserconsiderada
comoumdetalhedeimplementa ção.Emrela çãoaosobjetivos,aprote çãoaoacesso
feitapelo Proxynãodeixadeserumafuncionalidadecomono Decorator.Por
essemotivo,daquiparafrentenesselivroopadrão Proxyserácitadoreferenciando
ambosospadrões.
102

## Página 124

CasadoCódigo Capítulo5. EnvolvendoObjetos
Para que eu preciso de uma interface se nunca vou mu -
dar essa implementação?
Muitasvezesvejodesenvolvedorespensandoduasvezesantesdecriar
umaabstração,noformatodeumainterface,dealgumcomponenteim-
portantedosistema. Porexemplo,vamosimaginarumaclassequere-
tornepropriedadesdeumarquivodeconfigura çãodosistema.Pormais
quenãoexistaapossibilidadedesecriarumanovaimplementa çãopara
essaclasse,podeserinteressantequeelapossuaumaabstra ção.
Umdosmotivosparaissoéapossibilidadedesecriarum Proxyque
iráenvolveressaimplementa ção. Nesseexemplodaleituradoarquivo,
poderiahaver Proxiesparafuncionalidadescomooarmazenamento
dosvaloresemmemóriaeparaaverifica çãodaconsistênciadessesva-
lores. Sendoassim,antesdepensarquesóvaihaverumaclasse,pense
queaabstra çãotambémpodeserutilizadanacria çãode Proxiesque
podemencapsularaclasseprincipal.
Sevocêporacasonãocriouumainterfaceparaumaclassequeprecisa
deum Proxy,lembre-sequenãoédifícilrefatorá-lacomasrefatora ções
automatizadasdisponíveisnosIDEs.NoEclipse,porexemplo,aoextrair
ainterface,existeaop çãoparautilizá-laaoinvésdotipodaclasseonde
forpossível.Sendoassim,maisimportantequecriarainterfaceéobede-
ceraoencapsulamento,evitandodependerdedetalhesinternosdaclasse.
CenáriosparaAplicaçãodeProxies
Autilizaçãode Proxieséumrecursotãopoderosoquemearriscariaadizer
queéopadrãoquemaisutilizo.Antesdeentraremexemplosmaisdetalhados,acho
importantemostraralgunscenáriosondeautiliza çãodessatécnicapodeserfeita.
Acreditoqueissoajudaaenxergaropotencialdessespadrões.
Muitasvezesénecessáriaacria çãodecódigodeprote çãoparaevitarqueseja
feitaumainvoca çãodemétodocomparâmetrosinadequadosouemumcontexto
errado. Exemplosdessassituaçõesseriamparâmetrosqueprecisamestaremum
formatoespecificooumétodosquesópodemserinvocadosemdeterminadosesta-
dosdaclasse. Outrocenárioondeéimportanteprotegeraclasseépararequisitos
103

## Página 125

5.1. ProxieseDecorators CasadoCódigo
desegurança,evitandoqueumafuncionalidadesejaacessadaporumusuárionão-
autorizadooubloqueandoparâmetrosmaliciososquetentamexecutarataquesde
injeção(verquadro).Paratodosessescasos,paraevitarqueessecódigodeprote ção
fiquemisturadocomocódigodonegócio,muitasvezeséinteressantecriarumproxy
exclusivamenteparabloquearessesacessosindevidos.
Ataques deInjeção
Umataquedeinje çãoéaquelequeseaproveitadeaplica çõesquese
utilizamdaconcatena çãodestringsparaaforma çãodeumcomando
queseráexecutado. Dessaforma,oatacanteprocuraenviarumparâ-
metromaliciosoparaaaplica çãovisandoaforma çãodeumcomando
diferenteduranteaconcatena ção. Umdosexemplosmaisfamososéo
SQLInjection,noqualprocura-seinjetarpartesdecomandosSQLem
umastringqueformaráumaconsultaqueseráexecutadanobancode
dados.Outroexemplodeataqueéo Cross-site Scripting,quefazousode
injeçãodejavascriptemparâmetrosquesãoutilizadosparaaconstru ção
depáginasweb.
Umoutrocenárioondeousode Proxiesébastantecomuméparafazercache
daexecu çãodemétodos. Quandoumafuncionalidadedemoradaprecisaserexe-
cutadadeformarepetidaemumaaplica ção,éinteressantearmazenaroresultado
obtidonaprimeiraexecu çãoereutilizá-loemnovasinvoca ções.Colocarissojunto
comaprópriafuncionalidadepodetornarocódigoconfuso,misturandoduasres-
ponsabilidadesnomesmolocal. Dessaforma,um Proxypodeserutilizadopara
encapsularaclasse,armazenandooresultadodaprimeiraexecu çãoeretornando-o
semexecutaraclassenovamentenaspróximasinvoca ções.
Outrautilizaçãoclássicadessetipodetécnicaéparatornartransparenteoacesso
aumsistemaremoto.Aumcertotempoatrás,acomunica çãoentreaplica çõesre-
motasprecisavaserimplementadaatravésdoacessoabibliotecasderede,sendouma
atividadedifíciletrabalhosa.Hoje,grandepartedastecnologiasparacomunica ção
remota,comoRMI,EJBoumesmoclassesclientesdewebservices,encapsulatodo
esseprocessodentrodeum Proxy,oqualéresponsávelporacessarremotamente
umcomponentedisponibilizadopeloservidor. Esse Proxyimplementaamesma
interfacedoobjetooriginal,permitindoumatransparênciadesseprocessoparaa
aplicação,quepodeacessardeformaindiferenteoobjetolocalouoremoto.
104

## Página 126

CasadoCódigo Capítulo5. EnvolvendoObjetos
Emgeral,essespadrõessãoutilizadosparafuncionalidadesquesãoortogonaisa
estruturadosoftware.Issosignificaqueelascortamaestruturadosoftwareestando
presentesemdiversasclasses,nãoestandoligadasdiretamenteàsuafuncionalidade.
Porexemplo,umafuncionalidadederegistrodeauditoriaoudecontroledeacesso
costumasernecessáriaemdiversasclassesdeummesmotipo.Autiliza çãodeum
Proxypermitiria,nãosomenteareutiliza çãodissoemdiversasimplementa çõesde
umaabstração,comotambémpermitiriaqueessacaracterísticafossemodularizada,
evitandoseuespalhamentoemdiversasclasses.
ProxiesnaAPIdoJava
AsAPIsdalinguagemJavaestãorepletasdeexemplosdeimplementa çãodos
padrões Proxye Decorator.Comotodobomencapsulamento,sevocêjáutilizou
algumdeles,provavelmentenãopercebeuasuapresen ça. Essaseçãotrazalguns
exemplosdeusodessespadrões,quepodemservircomoumareferênciaparaoseu
uso.
O primeiro exemplo está na API de coleções. Essa API possui algu-
mas classes que servem para “decorar” as coleções existentes adicionando fun-
cionalidades a elas. A classeCollections possui métodos estáticos como
synchronizedList(List<T> list) queretornaalistarecebidacomsincroni-
zaçãoe unmodifiableList(List<? extends T> list) paracriarumalista
não-modificável.Oquenaverdadeessesmétodosfazeméencapsularalistapassada
emum Proxyqueadicionaessacaracterísticaaoobjetoretornado.
Outrousoimportantedopadrão ProxyacontecenoRMI(RemoteMethodIn-
vocation),queéatecnologiautilizadaemJavaparaainvoca çãoremotademétodos.
Nessemodelo,apósacria çãodaclassequedisponibilizaráseusmétodosremota-
mente,sãogeradososchamados s t u b se skeletons.Os skeletonssãoclassesquerece-
bemnoservidorasrequisi çõeseinvocamaclasseremota.Jáos s t u b ssão Proxies
queficamnoclienteerepresentamaclasseremota,possuindoamesmainterfaceque
ela.
AAPIpadrãoparaomapeamentoobjeto-relacionalnoJavaEE,oJPA(JavaPer-
sitenceAPI),possuiumafuncionalidademuitointeressantequepermiteumcarre-
gamentopreguiçosodelistasassociadasàclasseprincipal. Issosignificaqueseeu
tenhoumaclasse Pessoaquepossuiumalistadeinstânciasde Telefonequesão
persistentesemumabaserelacional,épossívelqueaocarregaruma Pessoa,sua
listade Telefonesejacarregadasomentenaprimeiravezemqueelaéacessada.
Issoéfeitoapartirdeum Proxyqueacessaabasededadosepopulaalistasomente
105

## Página 127

5.2. ExemplosdeProxies CasadoCódigo
emseuprimeiroacesso.
ProxiesDinâmicos
Quandocriamosumaclasseparaserum Proxy,elaprecisaimple-
mentaramesmaabstra çãodaclassequeestáencapsulandoparaque
possaserpassadanolugardela. EmJavaépossívelcriaroschamados
ProxiesDinâmicos. Elestêmacapacidadedeassumirdinamicamente
umainterface, permitindoquesejautilizadoparadiversasinterfaces.
Esseéumrecursoavan çadodaAPIdereflexãoquefogeaoescopodesse
livro,poréméimportantecitarparaqueoleitorsaibadaexistênciadesse
tipoderecurso.
5.2 Exemplos deProxies
“Falar é fácil. Mostre-me o código. ”
–LinusTorvalds
Nessecapítulo,umlongocaminhofoipercorridosemnemumexemplodecó-
digo. Paranãodecepcionarosleitores,introduzoestase çãodedicadaaapresentar
algunsexemplosde Proxy. Aideiaémostrarexemplosrealistasquepossamser
adaptadosparaoutrasaplica ções.Cadasubse çãoiráapresentarumcontexto,ain-
terfaceutilizadapelasclasseseemseguidaocódigodo Proxy.
InvocaçõesAssíncronas
Muitasvezesemalgunssistemastemosfuncionalidadesquedemoramaserexe-
cutadas.Nessescasos,éruimdeixarousuárioesperando,sendoqueemalgunscasos
elepodeinclusiveacharqueosistematravou.Oquecostumaaconteceréessasfun-
cionalidadesseremexecutadasemumathreaddiferente. Abaixoseguealistagem
dainterfacequeabstraiostiposdetransa çãodosistema.Paraasimplementa ções,
asinformaçõesdatransa çãosãoarmazenadasematributosenormalmentepassadas
noconstrutor. Paramaisdetalhessobreessaconstru ção,veroCapítulo 8sobreo
padrão Command.
Listagem 5.1-Interfacequedefineosservi çosdeumtrechoaéreo:
public interface Transacao {
106

## Página 128

CasadoCódigo Capítulo5. EnvolvendoObjetos
public void executar();
}
Talvezoprimeiroimpulsofosseadicionaracria çãodenovasthreadsnaspró-
priasimplementaçõesde Transacao. Porémissoiriagerarumaduplica çãode
códigoentreasclassesqueprecisariamdisso. Issotambémcausariaproblemasse
umamesmatransa çãoprecisasseserexecutadanamesmathreadouemumathread
diferentedependendodocontexto.Nessecaso,acria çãodathreadnachamadada
transaçãopoderiaresolveresseproblema,masnãoresolveriaoproblemadadupli-
cação.
Umaformadeabordarissoseriaacria çãodeum Proxyqueencapsulasseuma
transaçãoeainvocassedeformaassíncrona.Aclasse ProxyAssincronoapresen-
tadaaseguirimplementaessafuncionalidade. Elepodeserutilizadoemqualquer
implementaçãode Transacao,evitandoaduplica ção,einclusiveamesmaclasse
podeserutilizadacomousemo Proxy.
Listagem 5.2-Interfacequedefineosservi çosdeumtrechoaéreo:
public class ProxyAssincrono implements Transacao{
private Transacao t ;
public ProxyAssincrono(Transacao t ) {
this.t = t;
}
public void executar() {
Runnable r = new Runnable(){
public void run() {
t.executar();
}
};
Thread t = new Thread(r);
t.start();
}
}
RealizandooCachedeumDAO
Data Access Object ,tambémconhecidocomo DAO,éumpadrãocomo
objetivodeisolaroacessoadadosdeumaaplica ção[ 6]. Apartirdele,define-se
umainterfaceparaoacessoadadoseumaimplementa çãoparaencapsulartodas
107

## Página 129

5.2. ExemplosdeProxies CasadoCódigo
asresponsabilidadesreferentesàinterfacecomumbancodedados. Apesardeser
umpadrãoforadoescopodesselivro,eledescreveumapráticabastantepopularem
aplicaçõesquelidamcomdados.
Esseexemplosecontextualizaemumsoftwarequepossuium DAOquerealiza
o acesso a um banco relacional. Imagine que a interface dessa camada seja a
apresentadanalistagemaseguir. Normalmenteum DAOcostumapossuirmais
métodos,porémnesseexemplovamosconsiderarapenastrês,respectivamentepara
recuperação,exclusãoegrava çãonabasededados.Imaginequeaaplica çãoesteja
tendo problemas de desempenho e tentando diminuir a quantidade de acessos
a banco. Uma forma de fazer isso é guardando alguns objetos em memória e
reaproveitá-losemleiturassubsequentes. Comofazerissocomomenorimpacto
possível?
Listagem 5.3-Interfacequedefineosservi çosdeumtrechoaéreo:
public interface DAO {
public Identificavel recuperar(int id);
public void excluir(int id);
public void salvar(Identificavel obj );
}
Paranãoafetarnemosclientesnemospróprios DAOs,asolu çãoseriacolocar
um Proxyencapsulandoo DAOoriginalparaadicionarafuncionalidadedecache.
Aseguiréapresentadaaimplementa çãodaclasse CacheDAO.Elepossuiummapa
queéutilizadoparaarmazenarosobjetospersistidosapartirdoseuidentificador.
Osmétodos salvar()e excluir()respectivamenteadicionameremovemos
objetosdomapa,masapenasapósdelegarachamadaàclassequeestáencapsulando.
Listagem 5.4-Interfacequedefineosservi çosdeumtrechoaéreo:
public class CacheDAO implements DAO {
private DAO dao ;
private Map<Integer,Identificavel> cache;
public CacheDAO(DAO dao ) {
this.dao = dao;
this.cache = new HashMap<>();
}
public Identificavel recuperar(int id) {
108

## Página 130

CasadoCódigo Capítulo5. EnvolvendoObjetos
if(cache.containsKey(id))
return cache.get(id);
Identificavel obj = dao.recuperar(id);
cache.put(id, obj);
return obj;
}
public void excluir(int id) {
dao.excluir(id);
cache.remove(id);
}
public void salvar(Identificavel obj ) {
dao.salvar(obj);
cache.put(obj.getId(), obj);
}
}
Dessaforma,ométodo recuperar()primeiroverificaseoobjetoestánoca-
cheeemcasopositivooretornaseminvocaro DAOencapsulado.Casooobjetonão
estejanocache,o DAOéentãoinvocadoeoobjetoencapsuladoéarmazenadono
cacheantesdeserretornado.Observequenesseexemploo Proxypode,emalguns
casos,retornarparaoclientesemneminvocarométododoobjetoencapsulado.
Valeressaltarqueoexemplodecacheapresentandoébemsimplesenãoestá
preparadoparalidarcomumasériedequestõesimportantes.Paraexemplificarpo-
demsercitadasasincroniza çãoparadiversosacessosparalelos,aexpira çãodevido
àpossibilidadedeatualiza çãodosdadosporoutrasorigenseadistribui çãonocaso
deaplicaçõesemqueosdadossãoacessadosdeváriasmáquinas.Casoemsuaapli-
caçãosejanecessárioumcachemaiselaborado,sugere-seautiliza çãodepadrões
destinadosàcria çãodecacheparaacessoadados[ 19]. Porém,quantomaiscom-
plexoeleprecisarser,maisadequadoéautiliza çãodeum Proxyparaisolaressa
complexidadedorestodaaplica ção. FrameworkscomooHibernatejátrabalham
dessaformaeatépossibilitamaescolhadasuabibliotecadecache,comooEhCache
eoInfinispan.
TentativasRepetidasdeAcesso
Outrasituaçãoquenãoéincomumdeacontecerésernecessárioadicionaruma
funcionalidadeemumaclasseaqualnãopodemosmodificar. Issonormalmente
acontecequandoessaclassefazpartedeumframeworkoubibliotecadeclasses
que está sendo utilizada. Considere a interface representada a seguir como a
109

## Página 131

5.2. ExemplosdeProxies CasadoCódigo
implementadaporumaclassedisponibilizadaporumaempresaparabuscarum
arquivoemseusservidoresremotos.Porém,devidoainstabilidadedarede,existem
muitasfalhasaotentarrecuperaroarquivo.
Listagem 5.5-Interfacequedefineosservi çosdeumtrechoaéreo:
public interface AcessoRemoto {
public byte [] buscarArquivo( String url ) throws IOException;
}
Paradiminuironúmerodefalhas,umaalternativaérealizartentativasrepetidas
deacessoaoarquivo.Comoaclassenãopodesermodificadaenãoédesejávelmo-
dificarasclassesquebuscamoarquivo,umaalternativaéacria çãodeum Proxy
quetentebuscaroarquivonovamentenocasodeumafalha. Nalistagemaseguir
éapresentadaaclasse TentativasRepetidasqueencapsulaumainstânciado
tipo AcessoRemoto.Ométodo buscarArquivo()invocaomesmométodono
objetoqueestásendoencapsulado,porémdentrodeumbloco try/catchonde
umpossívelerroécapturadoincrementandoonúmerodetentativas.Sendoassim,o
métodoéinvocadonovamenteatéquenenhumerrosejaretornadoouqueonúmero
limitedetentativassejaatingido.
Listagem 5.6-Interfacequedefineosservi çosdeumtrechoaéreo:
public class TentativasRepetidas implements AcessoRemoto{
private AcessoRemoto ar ;
private int maximoTentativas;
public TentativasRepetidas(AcessoRemoto ar , int maximoTentativas) {
this.ar = ar;
this.maximoTentativas = maximoTentativas;
}
public byte [] buscarArquivo( String url ) throws IOException{
int tentativas = 0;
IOException ultimoErro = null;
while(tentativas < maximoTentativas){
try{
return ar.buscarArquivo(url);
}catch(IOException ex ){
tentativas++;
ultimoErro = ex;
110

## Página 132

CasadoCódigo Capítulo5. EnvolvendoObjetos
}
}
throw ultimoErro;
}
}
5.3 Extraindo um Pr o x y
Normalmenteospadrões Proxye Decoratorsãoaplicadosquandoumafunci-
onalidadeprecisaseradicionadaedeseja-secausarumimpactomínimonocódigo
quejáfoiimplementado. Nessecasonãoénecessáriorefatoraraaplica çãoparaa
implementaçãodopadrão.Anecessidadederefatora çãonadire çãodeum Proxy
podeocorrerquandoumaclasseestáinchadacommuitasfuncionalidadesedeseja-
sedividiressasresponsabilidades.Arefatora çãoparaessecenárioseriaextrairum
Proxycomumafuncionalidadenãoligadadiretamenteaoobjetivoprincipalda
classe.Esseprocedimentopoderiaserrealizadodiversasvezesparadiferentesfun-
cionalidades.
Umoutrocasonoqualessarefatora çãoserianecessáriaéquandoexisteduplica-
çãoemumapartedocódigoentreimplementa çõesdeumamesmaabstra ção.Isso
tambémpodesermotivadoquandoseperceberqueemumanovaimplementa ção
seránecessáriapartedafuncionalidadejápresenteemumaoutraclasse. Como
exemplo,outrodiacrieiumaclasseemquehaviaumcódigointernoquevalidava
seaordemdeinvoca çãodosmétodosestavacorreta,porémquandofuicriaruma
novaimplementaçãopercebiqueamesmavalida çãoserianecessária.Dessaforma,
extraíum Proxycomapartedevalida çãodaprimeiraclasseepasseiautilizá-lo
comtodasasimplementa ções.
AFigura 5.3apresentaospassosdarefatora çãodeextra çãodeum Proxyde
umaclasseexistente. Oprimeiropassoécriaraclassequerepresentaráo Proxy,
delegandotodasaschamadasdosmétodosparaainstânciaqueestásendoencap-
sulada.Nessepontoéimportantefazercomqueostestesnãoatuemisoladamente
naclasse,masnelaencapsuladapelo Proxyrecém-criado. Inicialmenteostestes
deverãopassarsemproblemas,poisnenhumcódigofoiadicionadonaclasseinter-
mediária.
111

## Página 133

5.3. ExtraindoumProxy CasadoCódigo
Figura5.3:Refatora çãodeExtra çãodeProxy
Depoisdepossuirasuítedetestesatuandoemcimadaclasseemconjuntocom
o Proxy,éhoradecome çaramigrarfuncionalidadedaclasseencapsulada.Aprin-
cipalregraéqueocomportamentoconjuntodevepermanecerinalterado. Dessa
forma,aparterelativaacadaumdosmétodospodeirsendomovidaparaoin-
termediário,atéquetodafuncionalidadedesejadaestejano Proxy.Depoisdisso,
seodesenvolvedoracharnecessário,elepodesepararostestesdaclassedostestes
relativosàfuncionalidadedo Proxy,quedevemfuncionarcomqualqueroutraim-
plementaçãoencapsulada.
112

## Página 134

CasadoCódigo Capítulo5. EnvolvendoObjetos
Criando um Pr o x y n oEclipse
Acria çãodaversãoinicialdo Proxy,quesimplesmentedelegaos
métodosparaclasseencapsulada,podeserbemtrabalhosaebra çalse
ainterfacealvopossuirumnúmerograndedemétodos. Felizmente,o
Eclipsepossuiumafuncionalidadedegera çãodecódigoquecriaauto-
maticamenteosmétodosquedelegamachamadaparaosmétodosde
umatributo.
Parautilizá-la,primeiramentedeve-secriarumaclasseeincluirum
atributodotipoqueseráencapsulado.Nãocaianatenta çãodeadicionar
ainterfacejuntamentecomseusmétodos.Emseguida,cliquecomobo-
tãodireitosobreocódigoeescolha Source > Generate Delegate Methods.
Nessemomentoiráabrirumajanelaapresentandoquaismétodosdos
atributosvocêdesejacriaredelegarparaeleachamada. Ésóescolher
todososmétodoseemseguidadeclararqueaclasseimplementaain-
terfacealvo.AFigura 5.4mostraacaixadediálogoabertaduranteesse
processo.
113

## Página 135

5.4. AdaptandoInterfaces CasadoCódigo
Figura5.4:AutomatizandoaDelega çãodeMétodosnoEclipse
5.4 Adaptando Interfaces
“ A incapacidade de se adaptar traz a destruição.”
–BruceLee
Umoutrocenárioondeexisteanecessidadedecriarumaclassequeenvolvaou-
traéquandopossuímosumaclassequeimplementaumainterface,masprecisamos
queelaimplementeoutra.Umexemplodomundofísicoocorrequandocompramos
umnotebooknosEstadosUnidoseprecisamosligá-loaquinastomadasdoBrasil.
Nocaso,onotebookamericanopossuiumafontequepossuiainterfacedastomadas
americanas,porémprecisamosqueelepossuaaquepermitaqueelesejaligadoaqui
noBrasil. Todossabemqueesseproblemanãoédifícilderesolver,bastandoum
adaptadorqueencaixeemumaentradanoparãobrasileiroepossuaumaentradano
padrãoamericano.AFigura 5.5mostradeformavisualaquestãodoadaptador.
114

## Página 136

CasadoCódigo Capítulo5. EnvolvendoObjetos
Figura5.5:Representa çãodoadaptadordetomadas
Aideiadopadrão Adapternãoémuitodiferentedeumadaptadordetomadas.
Criamosumaclassequeimplementaainterfacenecessária,aqualprecisamosnos
adaptar,a“tomadanova”.Internamenteessaclasseécompostaporumareferência
aumobjetoqueimplementaaoutrainterface,a“tomadaantiga”. Dessaforma,o
Adaptertraduzaschamadasdainterfacequeeleimplementaparaaclassequeele
encapsula.Issonemsempreétrivial,poisnormalmentenãoésomenteonomedo
métodoquemuda,masoutrasquestõesmuitasvezesinesperadas.
EstruturadopadrãoAdapter
Aestruturadopadrão Adapterésimilaràdospadrões Proxye Decorator,
sendoqueaprincipaldiferen çaéqueaclassequeestásendoencapsuladanãopossui
amesmainterfacedaqueaestáenvolvendo. Éjustamenteessefatoquepermitea
adaptaçãoentreasinterfaces. AFigura 5.6mostraemumdiagramaosprincipais
participantesdessepadrão.
115

## Página 137

5.4. AdaptandoInterfaces CasadoCódigo
Figura5.6:EstruturadopadrãoAdapter
Nessediagramatemosumaclasse Clientequedependedealgumaforma
de uma InterfaceAlvo. Sendo assim, paratornarpossível ela acessar uma
classe Adaptadaquenãoimplementaessaabstra ção,elaprecisautilizaraclasse
Adaptador,queiráreceberchamadasdemétodoconformea InterfaceAlvoe
iráchamarosmétodoscorrespondentesnaclasse Adaptada.
Éimportanteficarclaroquenemsempreaadapta çãoésimplesdeserfeita.Ques-
tõescomunsqueprecisamsertraduzidasincluemanomenclaturadeclasseseméto-
dos,alémdaconversãodeparâmetroseretornos.Questõesmaiscomplexaspodem
envolverdiferentesformasdeinteragircomasclasses.Porexemplo,oqueéumpa-
râmetrodemétodoemumapodeserumatributopassadonoconstrutornaoutra,
ouainda,oqueéoretornoemumapodeserumatributopopuladoemumparâme-
tropassadoparaométodonaoutra.Porém,amaiordificuldadeéquandoexistem
diferençassemânticasentreasdiferentesAPIs.Nessecaso,normalmenteénecessá-
riaaajudadeespecialistasdodomínioparacompreenderasdiferen çasepossibilitar
atradução.
ExemplodeAdaptador
Imagineumaaplica çãoqueinterajacomoservi çodeSMSdeoperadorasde
celular. Considere que a versão inicial da aplicação possua uma interfacepara
interagircomoservi çodeapenasumaoperadora.Alistagemaseguirapresentaa
116

## Página 138

CasadoCódigo Capítulo5. EnvolvendoObjetos
interface SMSSenderqueéutilizadapelaaplica ção´paraoenviodemensagens.
Essaclassepossuiométodo sendSMS()querecebecomoparâmetroumainstân-
ciadaclasse SMS,tambémapresentadanalistagem,eretornaumvalorbooleano
dizendoseamensagemfoienviadacomsucessoounão.
Listagem 5.7-InterfaceUsadapeloSistemaparaEnviodeSMS:
public interface SMSSender {
public boolean sendSMS(SMS sms );
}
public class SMS {
private String destino ;
private String origem ;
private String texto ;
//getters e setters omitidos
}
Aoevoluiraaplica ção,foinecessárioincorporaroservi çodeenviodeSMSde
umaoutraoperadora. Nãofoiumasurpresamuitograndequandofoiconstatado
queaAPIparaoacessoafuncionalidadeeracompletamentediferente.Alistagem
comainterfacedessanovaAPI, EnviadorSMS,estárepresentadaaseguir. A
primeiradiferençaestánosparâmetros,queemvezdeseremencapsuladosemuma
classe,nocasoa SMS,sãopassadodiretamenteparaométodo. Outradiferen ça
équeotextodamensagemnãoémaisumastring,masumarraydestrings. A
primeiraAPIrecebiaumtextolongoedividiaemváriasmensagenssenecessário,
porémnessaoutraAPIamensagemprecisaserdividaemtrechosde160caracteres
antesdachamadadométodo. Finalmente,anovaAPIlan çaumaexce çãopara
indicarumafalha,enãoretornaumvalorbooleanoparaindicarosucessoounão.
Listagem 5.8-InterfaceUsadapeloSistemaparaEnviodeSMS:
public interface EnviadorSMS {
public void enviarSMS(String destino , String origem , String[] msgs)
throws SMSException;
}
Paraevitarqueasclassesclienteprecisemseralteradaseseacoplaremauma
novaAPI,decidiu-secriarum Adapterparatraduziraschamadasdeumainterface
paraoutra.Paracriaresseadaptadoréprecisolidarcomtodasasquestõesrelativas
117

## Página 139

5.4. AdaptandoInterfaces CasadoCódigo
àsdiferençasentreasinterfaces.Aimplementa çãodoadaptadorestárepresentada
nalistagemaseguir.
Listagem 5.9-InterfaceUsadapeloSistemaparaEnviodeSMS:
public class SMSAdapter implements SMSSender {
private EnviadorSMS env ;
public SMSAdapter(EnviadorSMS env ) {
this.env = env;
}
public boolean sendSMS(SMS sms ) {
String dest = sms.getDestino();
String orig = sms.getOrigem();
String[] txts = quebrarMsgs(sms.getTexto());
try {
env.enviarSMS(dest, orig, txts);
} catch (SMSException e ) {
return false ;
}
return true ;
}
private String[] quebrarMsgs( String text ){
int size = text.length();
int qtd = ( size%160==0)? size/160: size/160+1;
String[] msgs = new String[qtd];
for(int i=0; i<qtd; i++){
int min = i*160;
int max = ( i==qtd-1)? size: (i+1)*160;
msgs[i] = text.substring(min,max);
}
return msgs;
}
}
Ométodo sendSMS()inicialmenterecuperaasinforma çõesdoobjeto SMSe
asatribuiavariáveislocais.Ométodo quebrarMsgs()échamadoparaquebrar
otextodamensagemqueestáemapenasumastringemumarraystringscomta-
manhomáximode160caracteres.Paralidarcomadiferen çadoretorno,achamada
aométodo enviarSMS()daclasse EnviadorSMSéencapsuladaemumbloco
118

## Página 140

CasadoCódigo Capítulo5. EnvolvendoObjetos
try/catch.Dessaforma,casoaexce çãoforcapturadaométodoretorna false,
ecasoométodosigaseufluxonormal,éretornado true.
Atravésdesseexemplo,épossívelobservarcomoexistemváriosfatoresquede-
vemserlevadosemconsidera çãonahoradaadapta ção.Muitasvezespode-seperder
funcionalidadeeinforma ções.Emumcasooposto,podemserfornecidasinforma-
çõesincompletasouhaverfuncionalidadesdainterfacequenãopodemserexecuta-
das.Naclasse SMSAdapter,porexemplo,paratransformaraexce çãorecebidaem
umretornobooleano,perdeu-seamensagemcomacausadoerroeoutrasinforma-
çõesassociadasaela.
Adaptando Exceções
Quandoaexce çãolan çadaporummétodoprecisasertransformada
naexceçãolan çadapelainterfacedaclasseadaptadora,asolu çãomais
comumérealizarachamadadométodoencapsuladaemumbloco try,
elançaranovaexce çãodentrodobloco catch. Casoelasejacriada
semrelaçãocomaanterior,oerrolan çadopossuiráemseu stacktraceo
métododo Adaptercomoorigem,omitindoarealcausadoerro.Ose-
gredonessecasoénãoesquecerdepassaraexce çãooriginalnoconstru-
tordanova,dessaformao stacktraceanteriorseráincluídocomocausa
doerro.
AdaptadoresparaMigra çãodeAPIs
Umoutrocenárioondeopadrão Adaptercostumaserbastanteutilizadoépara
darsuporteaclassesqueutilizaramumaversãoantigadeumaAPIemumaversão
novadosoftware.Imagine,porexemplo,queemumaaplica çãofossemcriadasclas-
sesqueimplementassemainterfacedeumframeworkparaseremutilizadasporele.
Casooframeworkmodifiqueessainterfaceemsuapróximaversão,aaplica çãonão
poderáutilizarasclassesjácriadas.Issoéumgrandeproblema,vistoqueaaplica ção
podenemcompilarcomanovaversãodoframework.
Comoumaformadecontornaresseproblema,oframeworkpodeproverum
adaptadorqueadapteasclassesdesenvolvidasnaversãoanteriordainterfaceparaa
versãonova.Dessaforma,asclassesdaaplica çãopodemusaresseadaptadorpara
continuarutilizandoasclassesjádesenvolvidas.
119

## Página 141

5.5. ConsideraçõesFinaisdoCapítulo CasadoCódigo
Comoumexemplodisso,aJDK1.0possuíaainterface Enumeration,com
osmétodos hasMoreElements()e nextElement(),eeraimplementadapor
classesquedesejavampermitiraitera çãodeseuselementos.NaJDK1.2foiintrodu-
zidaainterface Iterator,comomesmoobjetivo,porémcomnomesdemétodos
menores, hasNext()e next(),ecomummétodoopcional remove().
Parapermitirquecódigosquetrabalhemcomumainterfacepossamlidarcom
classes que sabem trabalhar com a outra, a biblioteca de classesApache Com-
mons Collections provê a classeIteratorUtils. Elapossuiosmétodosestá-
ticos asIterator(), queadaptaum Enumeration paraum Iterator, e
asEnumeration(),quefazaadapta çãoinversa. Dessaforma,seumcódigoque
utiliza Enumerationprecisautilizarumaclassequeimplementa Iterator,ele
podeutilizaro IteratorUtilsparafazeressaadapta ção.
5.5 Considerações Finais doCapítulo
Estecapítuloabordoupadrõesquedefinemclassesqueenvolvemobjetos,servindo
comointermediáriasentreaqueforneceafuncionalidadeeacliente. Comouso
doencapsulamentoedopolimorfismo,épossíveltornaressaintermediáriatranspa-
rente,permitindofacilmenteaadi çãodeumanovacamadaentreelas.Esserecurso
poderosopermiteautiliza çãodediversosartifíciosescondidossobamáscaradain-
terfacedaqualaclasseclientedepende.
Na primeira parte do capítulo, foram abordados os padrõesProxy e
Decorator,nosquaisessaclasseintermediáriapossuiamesmaabstra çãodaquea
estáenvolvendo.Dessaforma,elapodeadicionarnovasfuncionalidadesesepassar
pelaprópriaclasse.Jánasegundaparte,foiabordadoopadrão Adapternoquala
intermediáriaéutilizadaparaencapsularumaclassecomumainterfacediferenteda
sua.Nessecaso,aideiaéjustamentepermitirqueumaclassecomumadeterminada
interfacepossaserutilizadaporoutraquesabeinteragircomclassescominterface
diferente.
120

## Página 142

Capítulo6
EstratégiasdeCriaçãodeObjetos
“ A verdadeira felicidade vem da alegria de atos bem feitos, o entusiasmo de criar
coisas novas. ”
–AntoinedeSaint-Exupery
Noscapítulosanteriores,foramapresentadosdiversospadrõesquemontames-
truturasutilizadasparafornecerflexibilidadeeextensibilidadenasclassesdaaplica-
ção.Quandoutilizamosheran ça,devemosescolherentrediferentesimplementa ções
deumaabstra çãoparaqueelatenhaocomportamentoadequado. Comcomposi-
ção,outrosobjetosdevemserinstanciadoseinseridosnaclasseprincipal. Coma
composiçãorecursiva,diversasinstânciasdeimplementa çõesdeumaabstra çãosão
combinadasemumaestruturaqueforneceocomportamentodesejado.Finalmente,
paraautiliza çãode Proxies,éprecisoenvolveroobjetoecolocá-lonolugardo
encapsulado.
Paraospadrõesfuncionareméprecisoqueessasestruturasestejammontadas,
porémsabercomocriá-lasdeformaadequadanãoétãosimples.Porexemplo,de
nadaadiantaaclasseutilizarasabstra çõesparasedesacoplardasimplementa ções,

## Página 143

6.1. LimitaçõesdosConstrutores CasadoCódigo
senahoradecriarosobjetoselareferenciadiretamenteasclasses.Osobjetosdevem
estardesacopladostambémnomomentodacria ção! Nãosomenteautiliza çãode
umaestruturadeheran çaoucomposi çãodevesertransparenteàclassecliente,mas
tambémacriaçãodessaestrutura.Paraquerealmenteexistaflexibilidade,deveser
possívelcriarasdiferentesimplementa çõesoucombina çõesdeclasseparaqueo
comportamentopossaseralterado.
Essecapítuloiráabordarospadrõesparaacria çãodeobjetos.Elesmostramtéc-
nicasparaodesacoplamentodalógicadecria çãodeobjetos,principalmentequando
precisa-seutilizarumdospadrõesapresentadosnoscapítulosanteriores.Também
serãoapresentadassolu çõesparaencapsularumalógicacomplexadecria çãoepara
vincularacria çãodeobjetosrelacionados.Apróximase çãoiniciaocapítulomos-
trandoporqueosconstrutores,aformatradicionaldecriarobjetos,podemnãoser
suficientesparaencapsularessalógicadecria ção.
6.1 Limitações dos Construtores
SevocêperguntarparaqualquerdesenvolvedorJavacomosecriaumobjeto,eleirá
prontamenteresponderqueéatravésdeconstrutores.Apesarderealmentenãoser
possívelcriarumanovainstânciadeumaclassesemainvoca çãodeumconstrutor,
suaaplica çãonãoprecisainteragirdiretamentecomelesparacriarosobjetosde
queprecisa.Principalmentequandosedesejadesacoplaraclasseclientedaqueestá
sendocriada. Seoconstrutorfordiretamenteinvocado,ocódigodaclassecliente
precisarásermudadoparasubstituí-laporumanovaimplementa ção.
Estaseçãomostraalgumaslimita çõesdosconstrutoresquedificultamsuautili-
zaçãoparaacria çãodeobjetos.Algumasdessasquestõessãoabordadasnofamoso
livro E ff e c t i v e J a v adeJoshuaBloch[ 3].
DoisConstrutoresNãoPodemTerParâmetrosdeMesmoTipo
Umacaracterísticadosconstrutoreséqueelespossuemomesmonomedaclasse
quecriam.Issonãoéumproblemaseelapossuiumprocessodecria çãosimples,for-
necendoumoudoisconstrutoresparasuacria ção.Porém,quandoexistemdiversas
formasdecriarobjetosdeumamesmaclasse,issopodeserumproblema.Paraco-
meçar,todaaexpressividadequeépossívelatravésdautiliza çãodenomesdescritivos
paramétodosnãopodeserutilizadanosconstrutores,vistoqueelesprecisamtero
mesmonomedaclasse. Issodificultabastantequandoumaclassepossuidiversos
construtoresenãosesabeexatamentequalocomportamentoqueseráfornecido
122

## Página 144

CasadoCódigo Capítulo6. EstratégiasdeCriaçãodeObjetos
porcadaumdeles.
Essaquestãoficaaindamaiscríticaquandoénecessáriaacria çãodeconstruto-
resquepossuemparâmetrosdemesmotipo.Comoissonãoépossívelnalinguagem
Java,éprecisoutilizarartifíciosparadiferenciarosconstrutores.Porexemplo,adi-
cionarumparâmetrodiferenteamaisparadiferenciá-los,ouaindacriarapenasum
construtorcomumparâmetrodizendoqualotipodecria çãoquesedeseja.
Para ficar mais concreta essa situação, imagine que uma classe chamada
CoordenadaGeograficapossareceberstringscomrepresenta çõestextuaisdas
coordenadasemseuconstrutor.Comoexistemdiversosformatosparacoordenada,
comoo Geodésico(Lat 021°30.4423’ S ; Long 055°09.6734’ W)eo GeodésicoDe-
cimal(Lat -21.5070334899 ; Long -55.4119080998),ainten çãoseriaterconstrutores
separadosparacadatipodeformato. Infelizmente,comoambosconstrutoreste-
riamomesmonomeereceberiamumastringcomoparâmetro,essasolu çãonão
seriapossíveldeserimplementada.
UmConstrutorSempreCriaumNovoObjeto
Umaoutracaracterísticadeumconstrutoréquetodavezqueeleéchamado
eleretornaumnovoobjetodaclasse.Certamenteéissomesmoqueumconstrutor
deveriafazer,porémmuitasvezesdeseja-seutilizarumobjetoquejáexisteenão
gerarumnovo.Seesseforocaso,ficainviabilizadaacria çãodessesobjetosatravés
deconstrutores.
Objetosquenãocontenhamestado,ouseja,contenhambasicamentemétodos
comlógicadenegócio,sãobonscandidatosparateremumnúmerolimitadodeins-
tâncias. Outrasvezes,deseja-semanterumaúnicaentidadepararepresentaruma
determinadaentidadeemtodosistema.Imaginequeemumsistemadelocadorade
carrosdeseja-seterumaúnicainstânciapararepresentarainstânciade TipoCarro
querepresentaum Corsa.Dessaforma,quandofornecessáriorepresentarum Corsa
emvezdesecriarumanovainstância,ajáexistentedeveserretornada.Nadadisso
podeserfeitoutilizandoconstrutoresdiretamente.
UmConstrutorSóPodeRetornarObjetosdaMesmaClasse
Talvezoprincipalproblemadosconstrutoressejaretornarobjetosapenasda
classequedefiniuaqueleconstrutor. Nãoépossível,porexemplo,retornaruma
instânciadeumasubclasseouenvolveroobjetoemum Proxy. Dessaforma,a
classequeinvocaoconstrutordeumaoutraseacoplaaelafortemente.Pormaisque
123

## Página 145

6.2. CriandoObjetoscomMétodosEstáticos CasadoCódigo
elautilizeaabstra çãoemoutraspartesdocódigo,seránecessárioumaaltera çãono
códigodecria çãocasoumaoutraclassepreciseserutilizada.
Paraentendercomoissopodeserumproblema,imagineumaclassequeéuti-
lizadaemváriospontosdosistema. Suponhaagoraqueelapossuísseumgrande
métodoquefosserefatoradoparaautiliza çãodopadrão Template Method,no
qualsubclassesimplementariampartesdoalgoritmo. Umasitua çãosimilarseria
sefossecriadoum Decoratorparaadicionaralgumanovafuncionalidadeaessa
classe.Seelafosseutilizadaemváriospontosdiferentesdosistema,ocódigodecri-
açãodeveriasermodificadoemtodosessespontosparaqueasubclasseadequada
fossecriadaouqueo Decoratorfossecriadoparaencapsularainstância.
Sendoassim,épossívelperceberqueautiliza çãodiretadeconstrutorespodedi-
ficultarbastanteousodospadrõesqueforamvistosatéomomentonesselivro.Aló-
gicadecria çãopodesecomplicarprincipalmentequandoalgunspadrõessãocombi-
nadosesurgemquestõescomo:escolherasubclassecorretaparainstanciar;escolher
asimplementaçõesparacomporainstância;eadicionarfuncionalidadesenvolvendo
oobjetoem Proxies.Aspróximasse çõesapresentamalgunspadrõesquepodem
serutilizadosparaeliminaressaslimita çõeseencapsularumalógicacomplexade
criaçãodeobjetos.
6.2 CriandoObjetos com MétodosEstáticos
“Se permaneces estático na derrota, mova-se rumo à vitória. ”
–EdilsonSanchesPontes
Asoluçãomaissimplesparaeliminaranecessidadedautiliza çãodeconstrutores
diretamenteéacria çãodemétodosestáticosparacriaremosobjetos.Essapráticaé
conhecidacomo Static Factory Method . Apesardeserconsideradoumpa-
drão,essapráticanãofoidevidamentedocumentadacomoumpadrãoeéabordada
commaisdetalhesno E ff e c t i v e J a v a[3].
Nessepadrão,asclassesclientesdelegamparaosmétodosestáticosalógicade
criaçãodasinstâncias. Essesmétodosrecebemosparâmetrosnecessárioseestes
retornamainstânciaadequada. Comoessesmétodosdecria çãonãopossuemas
restriçõesdosconstrutores,elespodemresolveraslimita çõesdescritasnase çãoan-
terior.
Um dos primeiros benefícios da utilização do Static Factory Method
está na expressividade, pois é possível nomear o método de acordo com a ló-
gica de criação envolvida. Isso acaba resolvendo o problema dos construtores
124

## Página 146

CasadoCódigo Capítulo6. EstratégiasdeCriaçãodeObjetos
comtiposdeparâmetrorepetidos,poisésócriarnomediferentesparaeles. No
exemplodaclasse CoordenadaGeograficacitadoanteriormente,seriapossí-
velpossuirmétodosdecria çãochamados criarCoordenadaGeodesico()e
criarCoordenadaGeodesicoDecimal().Dessaforma,ocódigoclienteficaria
inclusivemaisclaroemrela çãoàestratégiadecria çãoqueestásendoutilizada.
Outrapossibilidadeinteressanteéaderetornarumobjetojáexistente.Esseob-
jetonormalmenteéguardadonaprimeiravezqueeleécriadoedepoiséaprovei-
tadoparaaschamadasseguintes. Eleéarmazenadoemumavariávelestática,ou
emalgumacole çãotambémemumavariávelestática.Umexemploclássicodissoé
aobtençãodeconexõesparaumbancodedados.Aclasse DriverManager,por
exemplo,disponibilizaométodoestático getConnection()emqueumaconexão
éretornada.Algumasimplementaçõescriamum pooldeconexões,ondeasconexões
sãoreaproveitadadepoisdeseremutilizadas.
Umoutropontointeressantedo Static Factory Method équeelepodere-
tornarqualquerimplementação.Dessaforma,épossívelintroduzirnovassubclasses
eretorná-lasnessemétododeformatransparenteàclassecliente.Assim,aclassecli-
entedependenterealmenteapenasdotiporetornadopelapelométodofábricaenão
dasimplementaçõesretornadas.Issosimplificamuitorefatora çõesquecriamnovas
classesdeumaabstra ção,comoacria çãode Template Method edeum Proxy,
poisaoalteraro Static Factory Method ,todasasqueoutilizamparaacria ção
poderãoreceberumanovaimplementa çãodeformatransparente.
StaticFactory MethodXF actory Method
Antesdeirfundonascaracterísticasdo Static Factory Method
éimportantedeixarbemclaroqueeleédiferentedopadrão Factory
MethodapresentadonoCapítulo 2. Opadrãoqueestásendodescrito
nessase çãoconsisteemummétodoestáticoutilizadoparaencapsular
acria çãoe/ouobten çãodeinstânciasporpartedaclassecliente. Jáo
Factory Method éum hook methoddefinidoporumaclasseparade-
legaracria çãodeumainstânciaparasuassubclasses.
ExemplosdeStaticFactoryMethod
Paraexemplificarautiliza çãodemétodosfábrica,vamosretomaroexemplodo
geradordearquivoapresentadonoscapítulosanteriores(aversãoqueutilizaopa-
125

## Página 147

6.2. CriandoObjetoscomMétodosEstáticos CasadoCódigo
drão Composite).Alistagemaseguirapresentaocódigodeumaclassequedis-
ponibiliza Static Factory Methods paraacria çãodegeradoresdearquivo.
Nessaimplementaçãooptou-sepordisponibilizarmétodosdiferentesparaacria-
çãodosgeradoresdearquivosemXMLedepropriedades.Outraalternativaseriaa
passagemdeumparâmetroqueidentificariaoformatodoarquivo.
Listagem 6.1-FábricadeGeradorArquivoutilizandoStaticFactoryMethod:
public abstract class FabricaGerador {
public static final String ZIP = "ZIP";
public static final String CRYPTO = "CRYPTO";
public static GeradorArquivo criarGeradorXML
(String... processadores) {
GeradorArquivo g = new GeradorXML();
g.setProcessador(criarProcessador(processadores));
return g;
}
public static GeradorArquivo criarGeradorPropriedades
(String... processadores) {
GeradorArquivo g = new GeradorPropriedades();
g.setProcessador(criarProcessador(processadores));
return g;
}
private static PosProcessador criarProcessador
(String... processadores) {
if(processadores.length > 1) {
PosProcessadorComposto pp = new PosProcessadorComposto();
for(String proc : processadores){
pp.add(criarProcessador(proc));
}
return pp;
} else if (processadores[0].equals(ZIP)){
return new Compactador();
} else if (processadores[0].equals(CRYPTO)){
return new Criptografador();
}
}
}
Paraosprocessadores,épassadoumarraydestringsqueidentificamospós-
126

## Página 148

CasadoCódigo Capítulo6. EstratégiasdeCriaçãodeObjetos
processadoresemsuarespectivaordem.Ambososmétodosfábricadelegamacria-
çãodelesparaométodo criarProcessador().Observequecasoexistamaisde
um,aclasse PosProcessadorCompostoqueimplementaopadrão Composite
éutilizada.
O código a seguir mostra como a classeFabricaGerador seria utili-
zada na criação de umGeradorArquivo. Um dos métodos estáticos, como
criarGeradorXML()ou criarGeradorPropriedades(),deveserinvocado
passandocomoparâmetrodeformaopcionalasstringsquerepresentamospós-
processadores. Notequeaclassetemcontatoapenascoma FabricaGerador
eaabstra ção GeradorArquivo,sendoqueousodetodasassubclassesepós-
processadoresficamencapsuladosdentrodafábrica.
Listagem 6.2-ExemplodeCria çãodoGeradorArquivo:
GeradorArquivo ga = FabricaGerador.criarGeradorXML(
FabricaGerador.ZIP,FabricaGerador.CRYPTO);
AprópriaAPIdoJavautilizaessepadrãoemdiversospontosparaencapsu-
laracria çãodeobjetos. Umexemplocomumsãoosmétodos parseInt()e
valueOf()daclasse Integer. Alémdeseremmétodosestáticosqueretornam
instânciasde Integer,elesfazemcacheparaqueamesmainstânciasejaretornada
casoomesmonúmerosejapassado.Issoocorreigualmentecommétodossimilares
emoutrasclassesqueencapsulamtiposprimitivos.
ImpedindodeInvocaroConstrutor
Disponibilizarum Static Factory Method nãoimpedeasclassesclientes
deinvocaremoconstrutoreignorartodaalógicadecria çãoencapsulada.Parare-
solveressaquestão,osegredoéfazercomqueoconstrutortenhaumavisibilidade
quedêacessoaométodofábricaenãodêacessoàsclassesclientes.Seométodoes-
tivernamesmaclassequeestásendocriada,oconstrutorpodeserdeclaradocomo
privado.Seométodofábricaestiveremumaclassediferente,entãoumasolu çãoé
declará-locomoprotegidoecolocaressaclassefábricanomesmopacotequeasque
sãocriadasporele.
6.3 Um Ú nicoObjeto daCl a s s e c o mSingleton
“Só pode haver um!”
127

## Página 149

6.3. UmÚnicoObjetodaClassecomSingleton CasadoCódigo
–ConnorMacLeod,Highlander
Umcasoespecialdautiliza çãodo Static Factory Method équandosede-
sejaqueaaplica çãopossuaapenasumainstânciadeumadeterminadaclasse.Isso
normalmenteémotivadoporquestõesdenegócio,emquefazsentidoapenasum
objetodaqueletipo. Porexemplo,imagineumsoftwarequerepresenteumjogo
dexadrezentreduaspessoas. Nessecontextoprovavelmentefarásentidoapenas
umtabuleirodejogo.Aestruturaparapermitiressetipodeconstru çãoéopadrão
Singleton.
A listagem a seguir apresenta um exemplo de implementação do padrão
Singleton.Noexemplo,o Singletonéutilizadoemumaclassequerepresenta
earmazenaconfigura çõesdosistema. Esseéumexemploemqueousodesse
padrãoéadequado,poissóexisteumaúnicaconfigura çãoparatodoosistema,e
dessaformaelapodeserfacilmenteobtidaapartirdequalquerclasse.
Listagem 6.3-ExemplodeSingleton:
public class Configuracao {
private static Configuracao instancia ;
public static Configuracao getInstancia() {
if(instancia == null)
instancia = new Configuracao();
return instancia;
}
// Construtor privado!
private Configuracao() {
//lê as configurações
}
// ...
}
Nessecaso,ométodofábricaénormalmentedefinidonaprópriaclasse. Oar-
tifíciodedefinirumconstrutorprivadoéfrequentementeutilizadoparaimpedira
criaçãodeoutrasinstânciasdaclasse. Umatributoestáticoédefinidoparaarma-
zenaressainstânciaeummétodoestáticoédisponibilizadodeformapúblicapara
128

## Página 150

CasadoCódigo Capítulo6. EstratégiasdeCriaçãodeObjetos
suarecuperação.Observequenalistagemdeexemplooobjetoécriadonoprimeiro
acessoaométodo. Umaimplementaçãoalternativa,seriaincluiressacria çãoem
umblocoestáticoparaqueelafosserealizadaquandoaclassefossecarregadapela
máquinavirtual.
Alistagemaseguirmostraoexemplodecomoumaclassepodeobterainstância
daqueimplementaopadrão Singleton. Observequeoprocessonãoémuito
diferentedainvoca çãodeum Static Factory method .Emqualquerlocalda
aplicaçãoemqueométodo getInstancia()forinvocado,omesmoobjetoserá
retornado.
Listagem 6.4-ObtençãodeumSingleton:
Configuracao c = Configuracao.getInstancia();
Umadasvantagensdo Singletonéafacilidadedeacessodessainstância
porqualquerobjetonaaplica ção. Dequalquerclasseépossívelchamarométodo
getInstancia()eobtê-la.Issoevita,porexemplo,queessainstânciaúnicapre-
ciseserpassadacomoparâmetroparadiversoslugares.Noexemplodotabuleirode
xadrez,essaprovavelmenteseriaumaclassequeprecisariaestaracessíveldediversos
locaisdeacordocomalógicadojogo.
U m a s o l uçãoutilizandoum Singletonofereceumaflexibilidademuitomaior
doqueumasolu çãoqueutilizamétodosestáticosparaaexecu çãodasregrasdene-
gócio.Porserumobjeto,ainstânciaúnicapodeserespecializadaeencapsuladapor
um Proxy,oquenãoépossívelfazercommétodosestáticos.Essaquestãoprejudica
bastanteatestabilidadedeclassesqueacessammétodosestáticos,poisnãoépossí-
velsubstituí-losporumobjetofalsocompropósitosdeteste,conhecidocomoMock
Object[25]. Umasoluçãoqueconciliaapraticidadedosmétodosestáticoscoma
flexibilidadedo Singletonseriaosmétodosestáticosdelegaremalógicadesua
execuçãoparaosmétodosdo Singleton.
OLadoNegrodoSingleton
Opadrão Singletondeveserutilizadocommuitocuidadoenassitua çõesem
querealmentefizersentidoterapenasumainstânciadeumaclasse.Muitosacham
que,porserumpadrão,elepodeserutilizadoemqualquerpartedosistema. O
resultadoéqueo Singletonacabasendousadocomoumavariávelglobalda
orientaçãoaobjetos,oquepodereduziraflexibilidadedaaplica çãodeixandosua
modelagemdeficiente.Poreleserutilizadomaisemsitua çõesinadequadas,muitos
acabamconsiderandoo Singletoncomoumamáprática.Sendoassim,todavez
129

## Página 151

6.4. EncapsulandoLógicaComplexadeCriaçãocomBuilder CasadoCódigo
queforutilizarum Singletonreflitabastantesesuautilizaçãoémesmonecessá-
ria.T a m b é mveremos,emumcapítuloposterior,queinversãodecontroleeinjeção
dedependênciaspodemajudarbastantenessecaso.
6.4 Encapsulando LógicaComplexa deCriação co m
Builder
“Podemosconstruir? Sim! Podemos s i m ! ”
–Bob,oConstrutor
Peloquejáfoiditosobreacriação deobjetosatéomomentonessecapítulo,
acreditoquetenhasidopossívelpercebercomoacriaçãodedeterminadostipospode
sercomplexa. Nessescasos,alógicadacriação, quemuitasvezesprecisavalidar
parâmetrosoubuscarinformações emarquivos,acabasemisturandocomalógica
daprópriaclasse.Sendoassim,mantê-lasnamesmaclassepodedeixá-lagrandee
confusa,tantocomautilizaçãodeconstrutoresquantocomautilizaçãodemétodos
estáticosdecriação.
Opadrão Builderforneceumasoluçãoparaessaquestãodacriaçãodeobjetos
complexos,comadefiniçãodeumaclasseresponsávelpeloprocessodecriação. A
partirdeum Builderépossívelseguiromesmoprocessodecriaçãoparadiferentes
estruturasediferentesrepresentações. Dessaforma,aclassequeinvocaosmétodos
deum Builderparaacriaçãodoobjetoqueprecisaficadesacopladadessalógica
decriaçãocomplexaedaclasseconcretaqueestásendocriada.
Alémdisso,podesercriadaumaabstraçãoparaum Builderdeformaquedi-
ferentesimplementações possamsercriadas.Dessemodo,osclientespodemguiar
acriaçãodediferentesobjetosatravésdo Builder,porémsemsaberaimplemen-
taçãoqueestásendoutilizadae,consequentemente,qualaclassedoobjetoqueestá
sendocriado.EssetipodepráticaémuitocomumemAPIsquedisponibilizamin-
terfacesquesãoimplementadaspordiferentesfornecedores.Porexemplo,imagine
umaAPIquelidacomcertificadosdigitais.Opadrão Builderpodeserutilizado
paracriaroobjetoqueassinaumarquivodigitalmente,porémcadafornecedorpos-
suiráumaimplementaçãodiferentedo Builderdeacordocomsuasclasses.
AFigura6.2apresentaaestruturadopadrão Builder.Nodiagrama,aclasse
Clienteprecisacriarumainstânciadaabstração Produtoeutilizaum Builder
paraessatarefa.Observequepelaestruturaépossívelterváriasimplementações do
Builder,possibilitandoquediferentesestratégiasdeimplementaçãosejamutiliza-
130

## Página 152

CasadoCódigo Capítulo6. EstratégiasdeCriaçãodeObjetos
das.Poréméimportanteressaltarqueessaabstraçãodo Buildersódeveserusada
quandorealmentefornecessária.
Figura6.1:RepresentaçãodopadrãoBuilder
Nafiguraalgunsoutrospadrões estão representadosparailustraracomplexi-
dadequeoprocessodecriaçãopodepossuir.V e j aqueaclasserepresentadacomo
Produtopodepossuirsubclasses,podesercompostaporoutras,podeserenvolvida
porum Proxyepodetersuasimplementações combinadasporum Composite,
issoentreoutrospadrões quepodemserutilizados.Nenhumdessesoutrospadrões
citadossãoobrigatóriosparaautilizaçãodeum Builder,porémsuapresençaau-
mentaacomplexidadedoprocessodecriaçãofavorecendoautilizaçãodeumpadrão
decriaçãodeobjetos.
CriandooSessionFactorydoHibernatecomumBuilder
Paramelhoraracompreensãodopadrão Builderessaseção apresentaum
exemplodoseuusonoframeworkHibernateparaacriação doobjetodaclasse
SessionFactory.OHibernateéumframeworkcujaprincipalfuncionalidadeé
realizaromapeamentoobjeto-relacional,ouseja,entreclassesetabelasdobancode
dados.Paraqueissopossaserfeito,éprecisoquediversasconfigurações sejamlidas
131

## Página 153

6.4. EncapsulandoLógicaComplexadeCriaçãocomBuilder CasadoCódigo
dearquivosedeanotaçõesemclasses,tornandoacriaçãodeum SessionFactory,
aclassequegeraassessões paraoacessoabasededados,umprocessobemcom-
plexo.
Alistagemaseguirmostraautilizaçãodaclasse AnnotationConfiguration
para a criação de um SessionFactory. Nesse contexto,
AnnotationConfiguration é a implementação do padrão Builder.
Observe como diversos método são chamados para adicionar configura-
ções em relação a como essa classe deve ser criada. O encadeamento na
chamada dos métodose deve ao fato de cada um deles retornar a pró-
pria instância de AnnotationConfiguration, com exceção do método
buildSessionFactory()queretornaainstânciade SessionFactory.
Listagem 6.5-CriaçãodeumSessionFactorydoHibernate:
SessionFactory sessionFactory = new AnnotationConfiguration()
.addPackage("com.lojavirtual")
.addAnnotatedClass(CarrinhoCompras.class)
.addAnnotatedClass(Cliente.class)
.addAnnotatedClass(Produtos.class)
.addResource("orm.xml")
.configure()
.buildSessionFactory();
Esseéumbomexemplodeusodopadrão Builderpoisenvolverealmente
umprocessocomplexodecriação. ApartirdaleituradearquivosXMLedas
anotações dasclassesmapeadassão extraídasasinformações necessáriasparao
SessionFactory. Éimportanteressaltarqueessalógicaextrapolaasresponsa-
bilidadesdaclasse SessionFactory,fazendotodosentidoaseparação dares-
ponsabilidadedasuacriaçãoemumaclasseseparada.
BuildercomInterfaceFluente
OtermointerfacefluentefoicunhadoporMartinFowlereErickEvans[14],
comoumaformadedescreverumestilodeconstruçãodeinterfaces.Aideiaédaro
nomedosmétodosdaclassedeformaqueocódigopareçaumafraseemlinguagem
natural. A listagem a seguir mostra o exemplo de uma interface tradicional,
utilizandométodoscomeçadoscom gete set,eamesmaclasseutilizandouma
interfacefluente. Comumainterfacefluenteécomosevocêestivessedefinindo
umanovalinguagemdentrodalinguagemdeprogramação apartirdosnomes
132

## Página 154

CasadoCódigo Capítulo6. EstratégiasdeCriaçãodeObjetos
dosmétodos,práticaquetambéméchamadadeDSL(LinguagemEspecíficade
Domínio)interna[15].
Listagem 6.6-Exemplodeusodeinterfacefluente:
//Estilo comum
Pessoa p = new Pessoa();
p.setNome("João");
p.setDataNascimento("30/03/1985");
p.setCargo("gerente");
//Interface fluente
Pessoa p = new Pessoa()
.chamada("João")
.nascidaEm("30/03/1985")
.comCargo("gerente");
Apartemaisimportantedeumainterfacefluenteestánanomenclaturautilizada
paraosmétodos.Elesdevemsoarcomosefossempartedeumafrase,deforma
que“u m anova pessoa chamada J o ã o”vira new Pessoa().chamada("João").
Outraquestão équeosmétodosdevemretornarainstânciadaprópriaclasse,ou
seja, this,paraaschamadasdemétodopossamserencadeadas.Noexemploapre-
sentado,aschamadasdosmétodos chamada(), nascidaEm()e comCargo()
retornamaprópriainstânciade Pessoa.
Muitasvezes,asaplicações precisamdeutilizarasinterfacesnopadrãoJavaBe-
ans(utilizandométodoscom gete set),porrequisitodosframeworksutilizados.
Issoacabainviabilizandoautilização dainterfacefluentenasclassesdedomínio.
Porém,issonãoimpedequeelassejamutilizadasnos Builders,quecriamessas
classes.Éimportantemaisumavezressaltarque,paraqueautilizaçãodo Builder
sejaadequada,éprecisoqueoprocessodecriaçãodoobjetoemquestãosejacom-
plexoeexijaaconfiguraçãodediversosparâmetros.
U mdosframeworkspioneirosnautilizaçãodeinterfacesfluentesparaacriação
deobjetosfoioframeworkJMock[24]. Eleéutilizadoparaacriação demock
objects,quesão objetosfalsosutilizadosparasubstituirasdependênciasdeuma
classe em testes de unidade. A listagem a seguir apresentaalguns trechos de
códigodoJMockparadefinirocomportamentodoobjetofalsoesuasexpectati-
vasemrelação àschamadasdaclassetestada. Observequeapesardaslimitações
relativasàsintaxedalinguagemJava,épossívellerocódigocomosefosseumafrase.
133

## Página 155

6.4. EncapsulandoLógicaComplexadeCriaçãocomBuilder CasadoCódigo
Listagem 6.7-InterfaceFluentenoJMock:
//uma chamada ao método log() com uma string contendo 'erro'
one (logger).log(with(stringContaining("error")));
//exatamente 3 chamadas de count()
//retornando consecutivamente 10, 20 e 30
exactly(3).of(counter).count();
will(onConsecutiveCalls(returnValue(10),
returnValue(20),returnValue(30)));
//permitir chamada ao método sqrt com valor menor que zero
//irá lançar a exceção IllegalArgumentException
allowing (calculator).sqrt(with(lessThan(0)));
will(throwException(new IllegalArgumentException());
ExemplosdeUtilizaçãodoBuilder
Para exemplificar os conceitos do padrão Builder e de interface flu-
ente, seráutilizado comocontextoo mesmo exemplopara a criação da classe
GeradorArquivomostradocomo Static Factory Method.Alistagemase-
guirapresentaaimplementaçãodaclasse BuilderGerador.Essaclassepossuium
atributo instanciaquearmazenaoobjetoqueestásendoconstruído.Aocha-
marumdosdoismétodos gerandoEmXML()ou gerandoEmPropriedades()
a subclasse correta érecuperada e atribuída ao atributo. Jáos métodos
comCriptografia()e comCompactacao()adicionamosprocessadoresnains-
tânciasendoconstruída,utilizandoo Compositequandohouvermaisdeum.No
finaldetodoprocesso,ométodo construir()deveserchamadopararetornaro
objetocriado.
Listagem 6.8-BuilderparaaclasseGeradorArquivo:
public class BuilderGerador {
private GeradorArquivo instancia;
public BuilderGerador gerandoEmXML() {
instancia = new GeradorXML();
return this;
}
134

## Página 156

CasadoCódigo Capítulo6. EstratégiasdeCriaçãodeObjetos
public BuilderGerador gerandoEmPropriedades() {
instancia = new GeradorPropriedades();
return this;
}
public BuilderGerador comCriptografia() {
adicionaProcessador(new Criptografador());
return this;
}
public BuilderGerador comCompactacao() {
adicionaProcessador(new Compactador());
return this;
}
private void adicionaProcessador(PosProcessador p) {
PosProcessador atual = instancia.getProcessador();
if(atual instanceof NullProcessador) {
instanciasetProcessador(p);
}else{
PosProcessadorComposto pc = new PosProcessadorComposto();
pc.add(atual);
pc.add(p);
instancia.setProcessador(pc);
}
}
public GeradorArquivo construir() {
return instancia;
}
}
Paradeixaroexemplomaisinteressante,vamosimaginarqueexistamainda
Proxysquepossamserutilizadosparaencapsularaclasse GeradorArquivo.
Dentrodesseexemplo,imaginequeaclasse ProxyAssincronoinvoqueomé-
tododegeraçãodearquivosemumathreaddiferenteequeaclasse LoggerProxy
graveaschamadasrealizadasemumarquivodelogparafinsdeauditoria.Alista-
gemaseguirmostracomoessasclassespoderiamfacilmenteserincorporadasno
Builder.Aoserchamadoométodo,oproxyencapsulaainstânciaarmazenadae
oresultadoéatribuídoaelamesma.
Listagem 6.9-AdicionandométodosnoBuilderparaadiçãodeProxies:
public class BuilderGerador {
//...
public BuilderGerador assincrono() {
135

## Página 157

6.5. RelacionandoFamíliasdeObjetoscomAbstractFactory CasadoCódigo
instancia = new ProxyAssincrono(instancia);
return this;
}
public BuilderGerador registrandoAuditoria() {
instancia = new LoggerProxy(instancia);
return this;
}
}
Paravercomoficaaconstruçãodoobjetoutilizandointerfacefluente,alistagem
aseguirmostraumexemplodecódigo.Observecomoaconstruçãodoobjetoflui
deformafácilentreaschamadasdemétodoparasuaconfiguração.
Listagem 6.10-ExemplodeutilizaçãodoBuildercominterfacefluente:
GeradorArquivo ga = new BuilderGerador().gerandoEmXML()
.comCriptografia().comCompactacao().assincrono()
.registrandoAuditoria().construir();
6.5 Relacionando Famílias de Objetos co m Abs-
tract Factory
“ F a m í l i aq u e${algumVerbo}unida, permanece unida. ”
–Ditopopular
Nospadrões anteriores,foramabordadosproblemasreferentesàcomplexidade
decriação dosobjetos,alémdeseudesacoplamentodaclasseclienteedaprópria
classequeestásendocriada.U moutroproblemasurgequandomaisdeumobjeto
relacionadoprecisasercriado. Muitasvezesexistemfamíliasdeobjetosnosquais
existemclassesrelacionadasemhierarquiasparalelas.U mexemploéquandouma
mesmaAPIéimplementadapordiversosfornecedores.Nessacaso,cadaumdeles
forneceimplementações diferentesparaasmesmasabstrações. Nãofazsentidouti-
lizarumaclassedeumfornecedorjuntocomoutraclassedeoutro,poisapesarde
obedeceremàsmesmasabstrações elasnãopodemsermisturadas.
U mpadrão queexistequefocanasolução desseproblemaéo Abstract
Factory. Nessepadrão,emvezdetermosumafábricaparaacriaçãodeumob-
jeto,elaédestinadaàcriaçãodeumafamíliadeobjetosrelacionados.Dessaforma,
setodososobjetosrelacionadosforemobtidosapartirdamesmafábrica,nãohaverá
inconsistênciaentreeles.
136

## Página 158

CasadoCódigo Capítulo6. EstratégiasdeCriaçãodeObjetos
U mexemploquetemosnaplataformaJavaéaAPIJDBC.Aclasse Connection
representaumaconexãocomobancodedadosetambéméutilizadaparacriarou-
trosobjetosutilizadosparainteragircomobancodedados.Semisturarmososobje-
tosobtidosdeconexõesdiferentes(o ResultSetdoMySQLcomo Statementdo
PostGreSQL,porexemplo)obteremosumerro,porémofatodeexistirumainstância
comoumpontocentraldeondetodospodemserobtidosevitaqueessetipodeerro
aconteça.Nessecaso,aclasse Connectionfazopapelde Abstract Factory,
poissóvaifabricarobjetosrelativosaobancodedadoscomoqualelasabesecomu-
nicar.
EstruturadoAbstractFactory
Aestruturabásicadopadrão Abstract Factoryestáapresentadanodia-
gramaaseguir.Asclasses ProdutoAe ProdutoBrepresentamasclassesperten-
centesaumafamília.Dessaforma,afamília“X”érepresentadapelasimplementa-
ções ProdutoAXe ProdutoBXeosimilarocorrecomafamília“Y”.Oexemplo
apresentaapenasdoistiposdeprodutoeduasfamílias,porémemumaimplemen-
taçãodessepadrãopodehavermaisdecadaumdeles.
Aclasse FabricaAbstrataéaqueabstraiacriação deumafamíliadeob-
jetos. Cadaimplementação éresponsávelpelacriação deumadasfamíliasdeob-
jetoepossuimétodosparaacriação decadaumdostiposdeobjetodafamília.
Comopodeservistonodiagrama, cadafamíliapossuiumaimplementação da
Abstract Factory.Porexemplo,a FabricaFamiliaXcriainstânciasdasclas-
ses ProdutoAXe ProdutoBX.
Existe uma troca importante que se faz quando se utiliza o Abstract
Factory.Utilizandoessepadrão,émuitofácilcriareintroduzirnaaplicaçãouma
novafamíliadeobjetos. Paraisso,bastacriarasimplementações paraasabstra-
ções dosobjetosqueserãofeitoseumanova Abstract Factoryqueosretorne.
Poroutrolado,essepadrão dificultaacriação deumnovotipodeobjetoperten-
centeaessafamília.Issoexigiriaaadiçãodeummétododecriaçãona Abstract
Factory,exigindomodificações emtodasassuasimplementações. Emresumo,é
fáciladicionarumanovafamíliadeobjetos,porémédifíciladicionarumnovotipo
deobjetonafamília.
137

## Página 159

6.5. RelacionandoFamíliasdeObjetoscomAbstractFactory CasadoCódigo
Figura6.2:EstruturaBásicadoAbstractFactory
CriandoObjetosparaoEnviodeSMS
V a m o simaginarqueumaaplicaçãopreciseinteragircomosistemadeSMSde
diversasoperadorasdetelefoniamóvel.T a m b é mvamossuporqueexistamdiversos
objetosqueprecisemsercriadosparainteragircomesseserviço.Elessão:
•ObservadorSMS:Recebeeventosrelativosàchegadademensagensdestina-
dasàaplicação.
•FiltroSMS:Configuraumfiltroquerestringeasmensagensquedevemser
recebidasoutratadasporumdeterminadoobjeto.
•EnviadorSMS:ResponsávelporenviarSMSparadispositivosmóveis.
•RespondedorAutomatico:Configurarespostasautomáticasparadetermi-
nadostiposdemensagem.
138

## Página 160

CasadoCódigo Capítulo6. EstratégiasdeCriaçãodeObjetos
Dependendodaoperadora,algunsserviços,comoarespostaautomáticaouo
filtroparaorecebimentodemensagens,podeserimplementadosdiretamenteno
servidoroupelaAPIcliente.Poressemotivo,nãoépossível,porexemplo,utilizar
umfiltrodeumaoperadoraparafiltrarasmensagensrecebidasporumobservador
deoutraoperadora.Omesmovaleparaaclasse RespondendorAutomaticoque
tambémpodesercriadaapartirdeumfiltro.
Dessaforma,opadrão Abstract Factorypodeserutilizadoparaconcentrar
acriaçãodessesobjetosemumaúnicaclasse.Esseobjetonãoprecisasernecessa-
riamenteapenasdestinadoaisso,podendorepresentaralgumconceitodosistema.
Nessecaso,aclassequeirácriarosobjetospodeserarepresentaçãodeumaconexão
dosistemacomosservidoresdaoperadora.Aseguirestárepresentadaalistagem
querepresentaaabstraçãodessaclasse.
Listagem 6.11-ExemplodeutilizaçãodoBuildercominterfacefluente:
public interface ConexaoOperadora{
public FiltroSMS criarFiltro(String expressao);
public EnviadorSMS criarEnviador();
public ObservadorSMS criarObservador();
public ObservadorSMS criarObservadorComFiltro(FiltroSMS f);
public RespondendorAutomatico criarRespostaAutomatica(FiltroSMS f);
//outros métodos referentes a conexão
}
Pode-seobservarpelalistagemqueexistemmétodosdecriação querecebem
umainstânciade FiltroSMScomoparâmetro. Casoumobjetocriadoapartir
deumaoperadoradiferentefossepassadocomoparâmetro,umerroserialançado,
pormaisqueaabstraçãofosseaceitapelotipodoparâmetro.Aconcentraçãodesses
métodosdecriaçãonamesmaclasseajudaaevitarqueessetipodemisturadeobjetos
ocorra.
Ofatoda Abstract Factoryserdefinidaapartirdeumaabstraçãopermite
queosclientespossaminteragirdeformatransparentecomdiferentesoperadoras.
Essaabstraçãotambémpermitequecadaclassetenhasuasparticularidades,como
porexemplo,osparâmetrosquesãonecessáriosparaqueaconexãopossaseresta-
belecida.
139

## Página 161

6.6. Considerações FinaisdoCapítulo CasadoCódigo
6.6 Considerações Finaisd oCapítulo
Essecapítulofocouempadrões paraacriação deobjetos. Opadrão Static
Factory Methodencapsulaacriaçãodeobjetospermitindoquesejamretornadas
instânciasdesubclasses,instânciasjáexistentes,equesetenhaumaexpressividade
maiorapartirdenomesmaissignificativos.Foivistotambémopadrão Singleton
comoumcasoespecialdo Static Factory Methodparaocenárioemquedeve
haverapenasumainstânciadeumadeterminadaclasse.
Paracasosmaiscomplexos,emquediversosparâmetrospodemserutilizados
paraconstruçãodoobjeto,o Builderéumpadrãoadequado.T a m b é mfoimos-
tradocomoelepodeserútilquandooutrospadrõesquedeixamaestruturadosobje-
tosmaiscomplicada,como Proxy, Template Methode Composite,sãoempre-
gadosnasclassesqueprecisamsercriadas.Finalmente,foiabordadoo Abstract
Factory,quefocaemcenáriosondefamíliasdeobjetosrelacionadosprecisamser
criadas.
140

## Página 162

Capítulo7
Modularidade
“ N o s s oo b j e t i v odefinitivo éa programação extensível. P o risso queremos dizer a
construção de u m ahierarquia de módulos, cada u madicionando nova
funcionalidade ao sistema. ”
–NiklausWirth
Nocapítuloanteriorforamapresentadosdiversospadrões paraacriaçãodeob-
jetos.Essespadrões, deumaformageral,desacoplamaclasseclientedasuacriação.
Issopermitequeessaclassedependaapenasdasuaabstração,possibilitandoqueno-
vasimplementações sejamcriadaseincorporadasàclasseresponsávelpelacriação.
A p e s a rdisso,aclienteacabadependendoindiretamentedaqueestásendocriada.
Porexemplo,elapodedependerdeum Builder,queporsuavezdependedas
implementações. Omesmovaleparaosoutrospadrões!
Essadependência,mesmoqueindireta,impedequeaclasseclienteeasim-
plementações sejamdivididasemmódulosindependentes. Noexemplocitadodo
Builder,aclasseclienteprecisateracessoaele,oqualprecisateracessoàsimple-
mentações. Comessaestruturanãoépossível,porexemplo,inserirdinamicamente

## Página 163

7.1.FábricaDinâmicadeObjetos CasadoCódigo
novasimplementações, permitindoqueelassejamutilizadaspelacliente,poispara
issoaclasseresponsávelpelacriação,comoo Builder,tambémprecisariadeser
modificada.
Amodularidadeécadavezmaisumrequisitonão-funcional importantenas
aplicações. Porémmodularidadenãoéapenasdividirosoftwareemmódulosque
formamumúnicobloco,maspermitirquenovosmódulospossamsercriadose
incorporadosnosoftwaresemanecessidadedesuamodificação. U mexemplode
modularidadeéoIDEEclipse,aoqualnovospluginspodemserfacilmenteedina-
micamenteincorporados.
Paraqueessetipodemodularidadepossaseratingida,énecessárionãosomente
autilizaçãodeinterfaceseabstrações paraainteraçãoentreosobjetos,mastambém
umdesacoplamentonomomentodesuacriação.Dessaforma,seumaclassecliente
utilizarum Builderouqualqueroutrointermediárioparainstanciarseusobjetos,
elanãopodedependerdiretamentedasimplementações. Issoirápermitirquenovas
implementações sejamincorporadassemmodificaraaplicação.
7 . 1Fábrica Dinâmica deObjetos
“Vidasfortes são motivadas por fi n sdinâmicos; as menores por desejos e inclinações. ”
–KennethHildebrand
Aprimeiraperguntaaserrespondidaé:comoobterumobjetosemdepender
diretaouindiretamentedesuaclasse?EmJava,aAPIdereflexãopermitequeuma
classesejainstanciadaapartirdeumastringcomoseunome.Issopermitequeas
classesqueserão instanciadaspossamserdefinidas,porexemplo,emumarquivo
deconfiguração.Dessaforma,aoleressearquivo,épossívelinstanciaraclassesem
dependerdiretamentedela.Issopermitequenovasclassespossamsersimplesmente
adicionadasao classpathdaaplicaçãoeconfiguradasnoarquivo.
Opadrão Dynamic Factory[17]propõeessaestruturaparaacriaçãodeobje-
tos.Elaéaplicávelquandosedesejacriarumobjetodeumaabstraçãoconhecida,ou
seja,quepossuiumadeterminadainterfaceousuperclasse,porémcujaimplementa-
çãonãopodeserdeterminadaemtempodecompilação. Issonormalmenteocorre
quandodeseja-sepermitirquenovasimplementações possamserincorporadasao
softwaresemasuamodificação,tornando-omaisextensíveleflexível.U mexemplo
seriaumsoftwarequeprecisaserimplantadoemdiversosclienteseemalgunsdeles
énecessáriodesenvolverclassesespecíficasparaaquelecontexto.
142

## Página 164

CasadoCódigo Capítulo7 .Modularidade
EstruturadoPadrão
Aestruturadopadrão Dynamic factorynãoémuitodiferentedaestrutura
deoutrospadrões decriação. Dessaforma,aclasseclienteirádependerapenasda
abstraçãocompartilhadapelasimplementações eiráacessarumaclassequeimple-
mentaumafábricadinâmica,responsávelpelacriaçãodosobjetos.Essafábricapor
suavezacessaumaoutraclasseresponsávelporlerasinformações arespeitodeque
implementaçãodeveserinstanciadaparaumadeterminadainterfaceousuperclasse.
Apartirdessainformação,aAPIdereflexãoéutilizadaparainstanciaressaclasse.
A Figura 7 . 1mostra a estrutura do padrão. A classe representada como
LeitorMetadadoséresponsávelporlerasinformações arespeitodequaisim-
plementações devemserinstanciadas.Essasinformações podemestararmazenadas
emumarquivodeconfiguração,emumbancodedadosouatémesmonasanotações
dealgumaclasse.Independentedaformacomoessasconfigurações sãodefinidas,é
importantequeelascontenhamqualaimplementaçãoquedeveserinstanciadapara
umadeterminadaabstração.
Figura7.1:EstruturadoDynamicFactory
Apartirdessaestruturaémuitofácilintroduzirnosistemanovasclasses.Para
issobastaconfiguraronomedessaclassenolocalondeo LeitorMetadadosobtém
asinformações eadicionaraclasseemumarquivo.jarnoclasspathdaaplicação.
Sendoassim,não apenasaclasse Clienteirádependerapenasdaabstração de
Produto,masoprocessodecriaçãodentrodaclasse FabricaDinamicatambém.
143

## Página 165

7.1.FábricaDinâmicadeObjetos CasadoCódigo
O que são metadados?
Apalavra“metadado”ésobrecarregadadesignificadodependendo
daáreadacomputaçãoemqueestamos.Deumaformageral,metadado
significa“dadosobreodado”,quenocontextodeumalinguagemorien-
tadaaobjetosseriamasinformaçõesarespeitodasclassesdeumsistema.
Nessecaso,osdadossãoasinformações daaplicaçãoeasclassescontêm
informações sobreosseustipos,suavisibilidadeecomosãomanipula-
dos.Dessaforma,nocontextodeumaclasse,osmetadadosseriamseus
atributos,seusmétodos,suasinterfaces,suasuperclasse,entreoutros.
Na estrutura do padrão Dynamic Factory, a classe
LeitorMetadados éresponsávelpor ler uma informação a res-
peitodeumaabstração,queéaclassequedeveserinstanciadanaquele
contexto. Dessaforma,comoessaéumainformação referenteauma
classedosoftware,pode-sedizerqueeleestálendoumnovometadado
paraela.
Opadrão Dynamic Factorypodeserimplementadoemconjuntocomum
Builderoucomum Static Factory Methoddeacordocomasnecessida-
desdaaplicação. Senecessário,maisdeumaclassepodeserconfiguradapara
umamesmaabstração, assimcomoclassesqueserão utilizadasparacomposição,
oumesmoparaenvolveraclasseprincipal,comoum Proxy.Oquediferenciaesse
padrãodosvistosnocapítuloanterioréodesacoplamentoentreafábricaeasimple-
mentações queestãosendocriadas.
DynamicFactorynaPrática
Paraexemplificaracriação deumafábricadinâmicacomousodereflexão,a
listagemaseguirmostraoexemplodeumaclassequecriaosobjetosdeacordo
comonomedaclasseconfiguradoemumarquivodepropriedades. Aclasse
FabricaDinamica possuiumconstrutorquerecebeonomedoarquivocom
asconfigurações decriação. AclassePropertiesdaprópriaAPIpadrão doJavaé
utilizadaparafazeressaleitura,fazendoopapeldeleitorademetadados.
Listagem 7.1- Fabrica dinâmicaque lêa classe da implementação de um ar-
quivodepropriedades:
144

## Página 166

CasadoCódigo Capítulo7 .Modularidade
public class FabricaDinamica {
private Properties props;
public FabricaDinamica(String arquivo)
throws FileNotFoundException, IOException{
props = new Properties();
props.load(new FileInputStream(arquivo));
}
public <E> E criaImplementacao(Class<E> interface) {
String nomeClasse = props.getProperty(interface.getName());
if(nomeClasse == null) {
throw new IllegalArgumentException(
"Interface não configurada");
}
try {
Class clazz = Class.forName(nomeClasse);
if (interface.isAssignableFrom(clazz)) {
return (E) clazz.newInstance();
} else {
throw new IllegalArgumentException(
"Classe configurada não implementa a interface");
}
} catch (ClassNotFoundException e) {
throw new IllegalArgumentException(
"Classe configurada não existe",e);
} catch (Exception e) {
throw new IllegalArgumentException(
"Não foi possível criar a implementação",e);
}
}
}
Muitasvezes,classesjáexistentesnosistemaouemalgumframeworkutilizado
pelaaplicação podemserutilizadosparaserumparticipantedeumpadrão. No
exemploapresentadoda Dynamic factory,foiutilizadaaclasse Properties
pararealizaçãodaleituradoarquivocomosmetadados.Emoutrospadrões, como
145

## Página 167

7.1.FábricaDinâmicadeObjetos CasadoCódigo
o Observer,porexemplos,opapeldeobservadorouobservadopodeserdesem-
penhadoporalgumaclassejáexistente.Casosejarequeridaumainterfacediferente
paraaclasseexistente,opadrão Adapterpodeserutilizadaparafazeraadaptação.
Aclassedoexemploesperaquenoarquivosejamdefinidaspropriedadescomo
nomedainterfaceevalorescomonomedaclassequedeveserinstanciada.Dessa
forma,quandoométodo criaImplementacao()éinvocado,onomedainter-
faceéutilizadopararecuperararespectivaimplementação quedeveserinstanci-
ada.Essainstanciaçãoéfeita,primeiramenteobtendo-seainstânciade Classre-
ferenteàquelaimplementação atravésdométodoestático Class.forName(),e
emseguidainvocandoométodo newInstance().Observequeantesdeefetiva-
mentecriaroobjetoéverificadoseaclasserealmenteimplementaainterface.Nesse
caso,comachamadadométodo newInstance(),oconstrutorsemparâmetros
daclasseseráinvocado.Sendoassim,paraqueessafábricasejautilizada,épreciso
queasimplementações possuamesseconstrutor.
Reflexão emJa v a
Reflexão éacapacidadedeumsistemadeexecutarcomputações a
respeitodesimesmo.Deumaformamaisprática,issoenvolveosistema
poderobterinformações, acessareatémesmomodificarsuaspróprias
classes.AAPIReflectiondalinguagemJavaprovêfuncionalidadesape-
nasparaobterinformações eacessarasclassesdosistema.Funcionalida-
desdemodificaçãodeclassessãomaiscomunsemlinguagensdinâmicas.
AclassebásicadaAPIReflectionéa Classquerepresentauma
classedosistema. Apartirdelaépossívelobterinformações, como
seunome,seusmétodos,seusatributos,suasuperclasseesuasinter-
faces. Alémdisso,tambémépossívelinstanciá-laatravésdométodo
newInstance(),comovistonoexemplo. OutrasclassesdessaAPI
representamoutroselementosdecódigo, como Method, Field e
Constructor. Estáforadoescopodesselivroaexplicação dofunci-
onamentodessaAPI,poréméimportantesaberessesfundamentospara
acompreensãodecomoopadrão Dynamic Factoryfunciona.
Paraexemplificarautilização daclasse FabricaDinamica,seráretomado
o exemplodo gerador de arquivos. Parasimplificaro exemplo, vamos supor
que as implementações possuem um construtorsem parâmetrose que o pós-
146

## Página 168

CasadoCódigo Capítulo7 .Modularidade
processadoréconfiguradoatravésdeummétodosetter. Aversão apresentadada
classe FabricaDinamicanãosuportaocarregamentodemaisdeumaimplemen-
tação damesmainterface,porémissopoderiasercontornadocomumapequena
modificação. Paramanteroexemplosimples,seráconfiguradaapenasumainstân-
ciadainterface PosProcessadorparaserinseridano GeradorArquivo.
A seguir são apresentadaslistagens que mostram um exemplo de como o
arquivodepropriedadesseriadefinidoecomoacriaçãodasclassesseriarealizada.
Observequeocódigoqueinstanciao GeradorArquivocomsuadependência
não referenciaemnenhummomentoaimplementação. Adicionalmente,aim-
plementação tambémnão éreferenciadapelaclasse FabricaDinamica,quelê
onomedaclassedeumarquivoexterno. Essetipodepráticapermitequenovas
classessejamcriadaseplugadasnosistema,semanecessidadedarecompilaçãodas
classesjáexistentes.
Listagem 7.2-Arquivodepropriedadescomadefiniçãodasclasses:
br.com.casadocodigo.GeradorArquivo=br.com.casadocodigo.GeradorXML
br.com.casadocodigo.PosProcessador=br.com.casadocodigo.Compactador
Listagem 7.3-UtilizandoaFabricaDinamicaparaacriaçãodoGeradorArquivo:
FabricaDinamica f = new FabricaDinamica("configuracoes.prop");
GeradorArquivo gerador = f.criaImplementacao(GeradorArquivo.class);
gerador.setPosProcessador(f.criaImplementacao(PosProcessador.class);)
UmaBaseParaOutrosPadrões
Mesmosendoumpadrãoimportante,a Dynamic Factoryémuitasvezesuti-
lizadaporbaixodospanos.A p e s a rdeserválidasuautilizaçãodiretaparaacriação
dealgunsobjetosdosistema,podesercomplicadoutilizaressepadrãocomoestra-
tégiadecriação geraldentrodeumaarquitetura. Aspróximasseções apresentam
padrões paraacriaçãodesacopladadeobjetosquepodemserutilizadosnolugarda
Dynamic Factory.Observemque,paraqueelessejampossíveisdeserimplemen-
tadosparaseobtermodularidade,aindaénecessárioqueuma Dynamic Factory
atuenocarregamentodinâmicodessasclassesemalgummomento.
147

## Página 169

7.2.InjeçãodeDependências CasadoCódigo
7 . 2Injeção deDependências
“ Averdadeira felicidade é...aproveitar o presente, sem a ansiedade da dependênciado
fu t u r o . ”
–LuciusAnnaeusSeneca
Quandoumobjetoprecisadacolaboraçãodeoutroparacumprirsuasresponsa-
bilidades,éumprocessonaturalqueopróprioobjetocrieoubusqueessasinstâncias.
Essaresponsabilidadepelacriação dasdependências,quandoestánopróprioob-
jeto,podeacabarcriandoumacoplamentoeprejudicandoamodularidade,mesmo
quandointerfacessãoutilizadasparainteraçãoentreasclasses.
U m aformadeevitarqueaprópriaclassesejaresponsávelporcriarsuasdepen-
dênciasécriá-lasdeformaexternaeinseri-lasnoobjetonomomentooudepois
desuacriação. Essaéaideiaprincipaldopadrão Dependency Injection[13]!
A p e s a rdeseutilizarmuitoonomeemportuguês,Injeção de Dependências,
parapadronizarautilizaçãodosnomesdospadrões eminglêsnesselivro,eleserá
referenciadocomo Dependency Injection.
Inversão deControle?
Devidoaofatodessepadrão inverteraresponsabilidadedecriação
dasdependênciasdeumaclasse,eletambéméconhecidocomoInver-
sãodeControle.Porémonome“inversãodecontrole”tambéméutili-
zadoparadenominarpráticasparaodesenvolvimentodeframeworks,
nasquaisasclassesdoframeworkinvocamclassesdaaplicação,inver-
tendoassimocontroledofluxodeexecução. Dessaforma,onome
Dependency Injectionacabouprevalecendo.
A p e s a rdesuasimplicidade,o Dependency Injectionéumpadrãomuito
poderoso,poisdesacoplaaclassedesuasdependências,permitindoqueelassejam
reutilizadasemdiferentescontextos.Consequentemente,atestabilidadedessaclasse
acabatambémsendoaumentada,poisobjetosvoltadosparaotestepodemserinje-
tadosnolugardasdependências.
148

## Página 170

CasadoCódigo Capítulo7 .Modularidade
FuncionamentodaInjeção
Ofocodopadrão Dependency Injectionénacriação econfiguração de
umaclassequepossuiumaoutracomodependência.Essadependência,porsua
vez,édotipodeumaabstração, normalmenterepresentadaporumainterface,a
qualgeralmentepossuimaisdeumaimplementação. Oproblemanocasoécomo
criareconectaressasinstânciassemqueexistaumadependênciadeumaparaoutra.
Essepadrãopropõecomosoluçãoaexistênciadeumaoutraclassequeirá“montar”a
aplicação,criandoasimplementações corretasdecadacomponenteeconectando-as
deformaaseobterocomportamentodesejado.
A Figura 7 . 2apresenta uma representação do padrão Dependency
Injection. A classe Montador équem na verdade coordena todo o pro-
cesso,tantodecriarasinstânciascorretas,quantodeinjetá-lasnaclasse Produto.
Essa,porsuavez,deveapenasproverumaformadeasdependênciaspoderemser
injetadas.Apróximaseçãoexploramaisdetalhesarespeitodesseprocesso.
Figura7.2:InjeçãodeDependências
Oprocessodecriaçãoereutilizaçãodeinstânciasécontroladopelo Montador,
quepodedefinirdiferentesestratégiasparaisso.Porexemplo,casoadependência
sejaumobjetoquepossasercompartilhado,amesmainstânciapodeserinjetada
diversasvezes.U m aoutraestratégia,muitocomumparaconexõesaserviçosouser-
vidoresremotos,éacriaçãodeumpooldeobjetos,deondeelessãoretiradosparaa
injeçãoemumaclasseeretornadosaofinaldesuautilização.Ofatodesseprocesso
nãosercontroladopelaclassepermitequeelapossaserreutilizadaemdiversoscon-
149

## Página 171

7.2.InjeçãodeDependências CasadoCódigo
textos.
Imagineumaclassequerealizeacessoaumabasededadoserecebaatravésde
uma Dependency Injectionaconexãoquedeveserutilizadaporela.Elapode-
riaserutilizadaporumaaplicaçãodesktopondeapenasumaconexãoécriadapara
todaaplicação,mastambémpoderiaserreusadaemumaaplicaçãoJavaEEqueexe-
cutaemumservidordeaplicaçãonoqualaconexãoéobtidadeumpool.Osimples
fatodessaconexãosercriadadeformaexternaàclasseeinjetadaemsuaestruturaé
queatornareutilizávelnasdiferentesarquiteturascitadas.
Comopode-seperceber,grandepartedotrabalhoacabaficandocomaclasse
Montador,responsávelpelacriaçãoeconexãoentreasclassesenvolvidas.Elapode
sersimplesecriadaespecificamenteparaumaaplicação,ousergenéricaecarregar
dinamicamenteasclassesqueprecisamserinstanciadasatravésdeuma Dynamic
Factory.Felizmente,existemframeworkseAPIs,comooSpringeoCDIdoJava
EE,queimplementammontadoresquecriamasinstânciasapartirdeconfigurações
emarquivosXMLeanotações. Sendoassim,raramenteénecessáriocriarumaclasse
parafazeropapeldemontador. Maisàfrenteserámostradocomoainjeção de
dependênciasfuncionanoSpring.
FormasdeInjetarDependências
Ainjeçãodedependênciaspodeserhabilitadadediversasformasemumaclasse.
Essaseçãoiráexplorarasalternativasexistentes,assimcomoamotivaçãonautili-
zação decadaumadelas. Dealgumaforma,deveserpossívelqueumaentidade
externareconheçaadependênciaepossainseri-lanaclasse,mesmoqueemapenas
certosmomentosdeseuciclodevida.
Otipomaiscomumdeinjeção dedependênciaséatravésdométodosetter.
Atravésdessemétodo,aclassepermitequeadependênciasejaconfiguradacomum
métodosetter,quearecebecomoparâmetro.Alistagemaseguirmostracomoa
classe AcessoDadosdisponibilizaummétodosetterparaqueaconexão coma
basededadospossaserconfigurada.Utilizandoessaestratégia,adependênciapode
seratribuídaealteradaaqualquermomento.
Listagem 7.4-Injeçãodedependênciapormétodosetter:
public class AcessoDados {
private Connection connection;
public void setConnection(Connection c) {
connection = c;
150

## Página 172

CasadoCódigo Capítulo7 .Modularidade
}
//...
}
U m aoutraabordagemparaainjeção dedependênciaséoconstrutor. Nessa
estratégia,adependênciadeveserinjetadanoobjetonomomentodesuacriação.
Essecasoacabasendomaisindicadoparacenáriosondeelaéobrigatóriaeessencial
paraofuncionamentodaclasse.Alistagemaseguirmostraomesmoexemploda
classe AcessoDados,porémutilizandoa Dependency Injectionatravésdo
construtor.
Listagem 7.5-Injeçãodedependênciapeloconstrutor:
public class AcessoDados {
private Connection connection;
public AcessoDados(Connection c) {
connection = c;
}
//...
}
Comofoiapresentadonocapítuloanterior,autilizaçãodeconstrutorestrazdi-
versasrestrições eaclassequeutilizainjeção porconstrutoresacabasofrendoos
mesmosproblemas.Poroutrolado,oconstrutoréumaformadegarantirqueuma
instânciadaclassenãoserácriadasemreceberaqueleparâmetro.U m adependência
bidirecional,porexemplo,seriaimpossíveldeserinjetadaporconstrutoresnasduas
classes...Naprática,ainjeçãopormétodossetteracabasendomaiscomum,sendo
feitaumaconfiguraçãocuidadosaparaqueomontadornãodeixedeconfiguraras
dependênciasimportantes.
U m aoutraabordagemexistenteparaa Dependency Injectionéautilização
deinterfaces.Nessecaso,édefinidaumainterfacequedeclaramétodosquedevem
serutilizadosparaainjeçãodadependência.Dessaforma,aclassequeprecisadela
deveimplementaressainterfaceparapoderrecebê-la.A p e s a rdeserumaabordagem
mais“burocrática”queasoutrasduas,elapermitequeaclassequeinjetaadepen-
dênciareconheçafacilmenteoobjetoqueprecisadelaparapoderprocedercoma
injeção.
Aestratégiadeutilizaçãodeinterfacesparainjetardependênciasémuitoutili-
zadaquandoomontadorprecisagerenciardiversasinstânciasepassarcertosobjetos
apenasparaasclassesqueprecisamdeles.Ainterfaceacabafuncionandocomoum
marcadorqueindicaquandooobjetoprecisadadependência.
151

## Página 173

7.2.InjeçãodeDependências CasadoCódigo
Paraexemplificaressasituação,considereumsistemaquepossuiumaabstração
chamada Processoquerepresentamprocessosdenegócioquepodemserexecu-
tados.Dasclassesqueimplementamessesprocessos,algumasdelasprecisamsaber
qualéousuárioqueasestáexecutando. Paranão tornaressasclasseacopladasa
comoasinstânciasdaclasse Usuariosãoarmazenadaseacessadas,tomou-seade-
cisãodeutilizar Dependency Injectionparaqueousuáriosejainseridonessas
instâncias. Alistagemaseguirmostraadefinição dainterfacequeasclassesque
desejamreceberainstânciadeUs u a r i odevemimplementar.
Listagem 7.6-Definiçãodeuminterfaceparainjeçãodousuário:
public interface CienteUsuario{
public void recebeUsuario(Usuario u);
}
Comoformadeinjetaradependência,foicriadoum Proxyqueencapsula
classesdainterface Executor,queéresponsávelporexecutarasclassesdotipo
Processopassadasaelas. Aclasse ProxyInjecaoUsuario,apresentadana
próximalistagem,verificacomooperador instanceofseoobjetoimplementaa
interfaceeinjetaadependênciadaclasse Usuarioemcasopositivo.
Listagem 7.7-Proxyparaainjeçãodousuário:
public class ProxyInjecaoUsuario implements Executor {
private Executor executor;
private Usuario usuario;
public ProxyInjecaoUsuario(Executor e, Usuario u) {
executor = e;
usuario = u;
}
public void executar(Processo p) {
if(p instanceof CienteUsuario) {
((CienteUsuario)p).recebeUsuario(usuario);
}
executor.executar(p);
}
}
Pelastécnicasanterioresdeinjeção dedependências,podeserobservadoque
aclassedevesinalizardealgumaformaondeequalelaqueprecisaserinjetada.
U m aoutraformadesesinalizarisso,bastanteutilizadaemframeworkseAPIs
152

## Página 174

CasadoCódigo Capítulo7 .Modularidade
maisrecentes,éatravésdeanotações. Aanotação énormalmenteincluídaem
umatributoounoseurespectivométodosetternoqualeladeveserinjetada. A
listagemaseguirmostraumexemplodeumServletquedevereceberumainjeção
dedependênciadeumEJBdoservidordeaplicações ondeestáimplantado.Note
quenesse caso éfeitautilização de reflexão paraquea dependênciapossa ser
inseridadiretamenteemumatributo,mesmoelesendoprivado.
Listagem 7.8-Injeçãodedependênciapeloconstrutor:
public class ServletLogin extends HttpServlet {
@EJB
private ServicoAutenticacao servico;
//lógica do servlet omitida
}
OsEfeitosColateraisdaInjeção
Seporumladoa Dependency Injectiontemopotencialdetornaraclasse
maisreutilizável,apassagemderesponsabilidadedamontagemdorelacionamento
dasclassesparaumterceirotambémpodegerarerrosemtempodeexecução.Como
aclassenãotemmaiscontrolesobresuasdependências,elaficasujeitaaerrosrefe-
rentesaumafalhanesseprocessoqueocorredeformaexterna.
U merrobastantecomumquandoessepadrão éutilizadoocorrequandouma
dependênciadeixadeserconfigurada.Nessecaso,élançadaaconhecidaeindese-
jávelNullPointerExceptionquandoaclassetentainvocaralgummétodonela.
Porumaquestãodesegurançadecódigo,issopodelevarmuitosdesenvolvedoresa
incluíremdiversoscondicionaisparaverificarseainstâncianãoénula,oquegera
umacertapoluiçãoeverbosidade.
A p e s a rdainjeção dedependênciassimplificarostestesdeunidade,devidoà
chancedeerrocomasmontagens,quandoessepadrãoéutilizado,émuitoimpor-
tantequesefaçaostestesdeintegraçãodaaplicação. Essestestesservemparaga-
rantirnãosomentequeasclassesestãofuncionandodeformaadequadajuntas,mas
queaaplicaçãoestácriandoeinjetandoasinstânciasdeformacorreta.Seriacomo
seestivéssemostestandoseomontadorestáfazendoainjeçãoadequadamente.
Amontagemdinâmicadaaplicaçãotambémpodedificultaracompreensãodo
contextoglobaldecomoosobjetosinteragemparaformarafuncionalidadedaapli-
cação. Aflexibilidadedeumaclasseempoderinteragircomdiversasimplementa-
ções tambémdificultasabercomqueclasseselaestáinteragindoemumcontexto
153

## Página 175

7.2.InjeçãodeDependências CasadoCódigo
concreto.Porexemplo,aosedepararcomumerro,odesenvolvedornãotemcomo
saberqualfoiaclasseinvocadaporela. Paraissoeledeveprocurarnomontador
ounasconfigurações daaplicaçãoparasaberqualeraaestruturanaquelecaso.Essa
indireçãoacabasendoumefeitocolateralaodesacoplamentoconquistado.
InjeçãodeDependênciasnoSpring
Normalmente,quandoainjeçãodedependênciaséutilizadaemumaaplicação,
éutilizadoalgumframeworkpararealizaramontagemdasclasses. U mdosfra-
meworksqueprimeirosedestacouporessetipodefuncionalidadeemuitoutilizado
atéhojeéoSpring.Utilizando-o,asinstânciascomsuasrespectivasdependências
sãodefinidasemumarquivoXMLeoframeworkseencarregadecriá-las.
A listagem a seguir exemplificacomo o Springseria utilizado no exemplo
dogeradordearquivo. Cadainstânciaédefinidacomoumbeannoarquivode
configuração, recebendoumnomequeseráutilizadoparareferênciasinternase
pararecuperá-lodeformaexterna. Utilizandoonomedosbeans,asinstâncias
podem ser injetadas utilizando diferentesestratégias,como pelo construtorou
atravésdepropriedades.
Listagem 7.9-ConfiguraçãodainjeçãodedependênciapeloSpring:
<?xml version="1.0" encoding="UTF-8"?>
<beans...>
<bean id="compactador" class="br.com.casadocodigo.Compactador" />
<bean id="criptografador" class="br.com.casadocodigo.Criptografador">
<constructor-arg type="int" value="3"/>
</bean>
<bean id="composite"
class="br.com.casadocodigo.PosProcessadorComposto">
<constructor-arg>
<ref bean="compactador"/>
<ref bean="criptografador"/>
</constructor-arg>
</bean>
<bean id="geradorArquivo" class="br.com.casadocodigo.GeradorXML">
<property name="processador" ref="composite" />
</bean>
</beans>
Noexemplo,obean criptografador recebeumparâmetronoconstru-
154

## Página 176

CasadoCódigo Capítulo7 .Modularidade
torreferenteaotamanhododeslocamentodecaracteresutilizadonoalgoritmo.
Asreferênciasdosbeans criptografadore compactadorsão tambémpas-
sadascomoparâmetroparaoconstrutordobean composite. Finalmente,o
bean geradorArquivorecebeumainjeçãodobean compositenapropriedade
processador.AtravésdoarquivoXMLapresentado,épossíveldefinirqualclasse
seráinstanciadaparacadabeanecomoumadeveserutilizadanaconstrução da
outra.
OsusuáriosdoframeworkSpring, pararecuperaremumbeandevemfazer
usodaclasse ApplicationContext. Elaéresponsávelporcarregaroarquivo
XMLcomadefinição dacomposição dosobjetoseretorná-losàaplicação. A
listagema seguir mostra comoela seria utilizada na criação de uma instância
do GeradorArquivo comodefinidonoarquivoXML.Emaplicações web, o
Spring normalmenteéintegrado diretamentecom o containerweb jácriando
osobjetoseinjetando-osnasclassesquetratamasrequisições. Nessecaso,não
háanecessidadedeacessodiretoàclasse ApplicationContextpelaaplica-
ção,poisissoéfeitopelocontainerweboupeloframeworkqueestásendoutilizado.
Listagem 7.10-RecuperaçãodeumbeanconfiguradonoSpring:
String xml = "applicationContext.xml";
ApplicationContext ac = new ClassPathXmlApplicationContext(xml);
GeradorArquivo ga = (GeradorArquivo) ac.getBean("geradorArquivo");
Apartirdoquefoimostrado,épossívelpercebercomoseriasimplesamudança
dasimplementações envolvidasedaconfiguraçãodaestruturamontada.Porserem
definidosemumarquivoXML,osbeanspodemseralterados,consequentemente
mudandoocomportamentodaaplicação,semanecessidadedesuarecompilação.
Paraexemplificaressefato,imaginequesejanecessáriointroduzirum Proxyna
classe GeradorArquivoparaainvocaçãoassíncronadeseusmétodos.Issopoderia
serfacilmenterealizadocolocandoaclassedo Proxynobean geradorArquivo,
fazendo-oencapsularoqueestavadefinidoanteriormente,conformemostradona
listagemaseguir.
Listagem 7.11-InserçãodeumProxydeformatransparente:
<?xml version="1.0" encoding="UTF-8"?>
<beans...>
...
<bean id="geradorArquivo"
155

## Página 177

7.3.ServiceLocator CasadoCódigo
class="br.com.casadocodigo.GeradorProxyAssincrono">
<constructor-arg>
<ref bean="geradorEncapsulado"/>
</constructor-arg>
</bean>
<bean id="geradorEncapsulado" class="br.com.casadocodigo.GeradorXML">
<property name="processador" ref="composite" />
</bean>
</beans>
7 . 3ServiceLocator
“Quandotentar localizar a l g o,procure primeiro em s u amente. ”
–CraigBruce
Opadrão Service Locator[13]éumaalternativaaopadrão Dependency
Injectionparapermitiramodularidadenasaplicações. Diferentementedainje-
ção,asprópriasclassessão responsáveisporbuscarassuasdependências.Porém,
elasfazemissoatravésdeumaoutraclasseresponsávelporlocalizaraimplementa-
çãoquedeveserutilizadaparaumadeterminadainterface.
Nocontextodessepadrão,apalavra“ s e r v iço ”éutilizadaparadenotarumacola-
boraçãodeumaoutraclasse.Seriacomoseaclasseexternaestivesseprestandoum
serviçoparaaqueautiliza.Nessecaso,aclasseprincipaldeclaraotipodeserviço
queelaprecisautilizandoumaabstração,comoumaclasseabstrataouumainter-
face,eentãoutilizaum Service Locatorparaencontraraqueiráprestaraquele
serviçoparaela.
156

## Página 178

CasadoCódigo Capítulo7 .Modularidade
ServiceLocator como u mJ2EEPattern
O Service LocatorfoidocumentadocomoumCoreJ2EEPat-
ternefoimuitoutilizadoparaalocalizaçãodeserviçosremotos,prin-
cipalmenteenterprisebeans,emaplicações J2EE[6].Nessecontexto,o
Service LocatorseconectavaaumrepositórioJNDIparaadquirir
umareferênciaaessesserviçosremotosefaziaumcachedessareferên-
ciaparaevitaracessosdesnecessáriosaoregistrodenomes.Nasnovas
versões daplataformaenterpriseJava,queperdeuo“2”eagorasechama
simplesmenteJavaEE,autilizaçãodessepadrãoficouobsoletaaprópria
plataformajáprestaesseserviço,realizandoinclusiveainjeção dessas
dependênciasnasclasses.
Poressemotivo,quandosefalaem Service Locatormuitagente
achaqueéumpadrãoobsoletopelaexperiênciaquetevecomelenapla-
taformaJ2EE.Nessecontexto,essepadrãotinhaoobjetivoprincipalde
centralizaromecanismodebuscadeserviços,encapsulandoaspeculi-
aridadesdecadaregistroeevitandobuscasdesnecessárias.Porém,fora
dessecontexto,essepadrão aindaémuitoimportante,principalmente
parapermitiramodularidadedasaplicações. Sendoassim,sevocêainda
guardaalgumtraumadautilizaçãodessepadrãoparabuscarEJBs,deixe
issodeladoporqueelepodesermuitoútilemoutrassituações.
EstruturaparaLocalizaçãodeServiços
No Service Locator,nãoexisteafiguradeumaclassequecentralizaares-
ponsabilidadedecriação eligação dasclassesqueirão comporaaplicação. Nesse
padrãocadaumabuscasuasprópriasdependênciasatravésdeumaclasseresponsá-
velporbuscarainstânciaquedeveseradicionadacomodependência.
AFigura7 . 3apresentaaestruturadopadrão Service Locator. Nodia-
grama,aclasse Clienterepresentaaclassequeprecisacriarumainstânciada
abstração Servico. A p e s a rdehaverumarelação deagregação entreessasclas-
ses,nessepadrão arelação poderiasermaisfraca,comoacriação eutilização do
serviçodeformaencapsuladadentrodeummétodo.Segundoopadrão,umaclasse
responsávelporencontrareretornaraimplementaçãodesseserviço,representada
por LocalizadorServicos,éutilizadapelaclasse Clienteparafazerisso.
157

## Página 179

7.3.ServiceLocator CasadoCódigo
Figura7.3:EstruturadoServiceLocator
U m aclassequeimplementeumlocalizadordeserviçospodepossuirumaim-
plementação fixa,retornandoasinstânciasdesejadasdeacordocomoparâmetro
passado.Eraessetipode Service Locatorquecostumavaserutilizadonasapli-
cações J2EE.Porém,paraconseguirmodularizaraaplicação,éprecisoqueelefaça
usodeuma Dynamic Factoryparaqueosserviçosretornadospossamsermais
facilmentealterados.
Quandoopadrão Dependency Injectionéutilizado,essaquestão ainda
precisaserimplementada,porémqueméoresponsávelporbuscarosserviçosnão
éalguémqueéinvocadopelasclasses,esimomontador.Porisso,muitasvezes,o
montadorprecisadeum Service Locatorparapoderlocalizarasimplementa-
ções einjetá-lasnasclasses.
U mdosproblemasdessepadrão estánofatodasclassesficaremacopladasà
classeresponsávelpelabuscadeserviços.Issoasimpededeseremreutilizadasfora
deumcontextoemqueo Service Locatorestejapresente.Dequalquerforma,
o Service Locatorcostumaserutilizadoencapsuladonaclasse,nãosendouma
dependênciaexpostanaAPIexterna.Issoébompoisnãocriaessadependêncianas
classescliente.
UtilizandoaclasseServiceLoader
AJDKpossuiumaclassechamada ServiceLoaderquepodeserutilizada
comoum Service Locatorquecarregadinamicamenteasimplementações de
umainterface.Essasimplementações podemestarempacotadaseconfiguradasden-
trodediferentesarquivosJAR.Sendoassim,aimplementação serácarregadade
158

## Página 180

CasadoCódigo Capítulo7 .Modularidade
acordocomosarquivosJARqueestiverempresentesnoclasspathdaaplicação.Basta
incluireremoverarquivosdoJARparaalteraraimplementaçãoutilizada.
Paraqueaclasse ServiceLoaderpossaserutilizada,oprimeiropassoseriater
umainterfacequeserviriadeabstraçãoparaoserviçoasercriado.Asimplemen-
tações dessainterfacepoderiamentão sercolocadasemarquivosJARparaserem
localizadas.Alémdaimplementação,aindaénecessárioincluirnoJARumarquivo
queregistraaclassecriadacomoumaimplementaçãodaqueleserviço.Essearquivo
devesercolocadodentrododiretório META_INF/servicesedeveteronome
completodainterface,incluindoopacote. Comoconteúdo,devehaversimples-
menteumalinhacomonomedaclasseparacadaimplementaçãodaquelaabstração
contidanaqueleJAR.
AFigura7 . 4ilustracomodeveseressaestrutura.Considere Abstracaocomo
ainterfaceparaqualsedesejedefinirosserviços.Noexemplo,o arquivo1.jar
possui as implementações ImplementacaoA e ImplementacaoB e o
arquivo2.jar possui a ImplementacaoC. Cada arquivo JAR possui um
arquivochamado Abstracao, onomedainterface,comosnomedasclasses.
Dessaforma,deacordocomoarquivoJARcolocadonoclasspathdaaplicação,
classesdiferentesseriamretornadaspelo ServiceLoader.
Figura7.4:ArquivosJARparautilizaçãodoServiceLoader
159

## Página 181

7.3.ServiceLocator CasadoCódigo
Alistagemaseguirilustra,dentrodoexemplodaFigura7 . 4,comofuncionaa
classe ServiceLoader. Essetrechodecódigoimprimenoconsoletodasasim-
plementações queestãoregistradasparaumainterface.Ométodoestáticoload()
da classe ServiceLoader éutilizado para carregartodas as implementações
registradasdainterface Abstracao.Emseguida,éutilizadoum Iteratorpara
percorrerasimplementações recuperadaseimprimi-lasnoconsole.
Listagem 7.12- Imprimindo as implementações encontradas pelo ServiceLoa-
der:
ServiceLoader<Abstracao> sl = ServiceLoader.load(Abstracao.class);
Iterator<Abstracao> i = sl.iterator();
while(i.hasNext()) {
System.out.println(i.next().getClass().getName());
}
Para mostrar um exemplo mais concreto do uso do ServiceLoader, a
listagemaseguirmostracomoelepoderiaserutilizadoparaarecuperaçãodospós-
processadoresparaaclasse GeradorArquivo.Nessecaso,o Service Locator
estásendoutilizadonoconstrutorparapopularoatributo processadordaclasse.
Observequecasoexistaapenasumaimplementação,elaseráatribuídadiretamente
aoatributo,mascasoexistamaisdeuma,aclasse PosProcessadorComposto
éutilizada. Dessaforma,casoumarquivoJARconfiguradocomumanovaim-
plementação foradicionadoaoclasspathdaaplicação, elaserárecuperadapelo
ServiceLoader. Nocasodaclasse PosProcessadorComposto,queéuma
implementaçãoquenãodeveserretornada,bastanãoincluí-lanoarquivo.
Listagem 7.13- Buscando os pós-processadores do GeradorArquivo com um
ServiceLocator:
public abstract class GeradorArquivo {
private PosProcessador processador = new NullProcessador();
public GeradorArquivo()) {
ServiceLoader<PosProcessador> sl =
ServiceLoader.load(PosProcessador.class);
Iterator<PosProcessador> i = sl.iterator();
List<PosProcessador> lista = new ArrayList<>();
160

## Página 182

CasadoCódigo Capítulo7 .Modularidade
while(i.hasNext()) {
lista.add(i);
}
if(lista.size() == 1) {
processador = lista.get(0);
} else if (lista.size > 1) {
processador = new PosProcessadorComposto(lista);
}
}
//demais métodos
}
Combinando diversos padrões em u m a solução
Nodecorrerdesselivro,vimosdiversospadrões queaospoucosfo-
ramsendoincorporadosàssoluções apresentadas.Aideiaéquepaula-
tinamenteelescomecemafazerpartedanossaformadepensareque
acabamosutilizando-osmesmosemperceber.Desafiovocêadarmais
umaolhadanocódigo daúltimalistagemetentaridentificarospa-
drões queestão alipresentes. Utilizamoso Bridgenaabstração do
GeradorArquivoenousodecomposiçãoparaospós-processadores,
o Null Objectéutilizadoparaoscasosondenãohápós-processador,
o Compositeéutilizadoparaquandohámaisdeumpós-processador,
e,finalmente,o Service Locatoréutilizadoparaocarregamento
dinâmicodospós-processadores.
Notequenãoestoudizendoparaaplicartodosospadrões possíveis
emumamesmasolução,poisissoéumamáprática.Porém,oqueacaba
acontecendo,équenasoluçãosucessivadosproblemasdedesigndeuma
classe,énaturalqueoresultadosejafrutodacombinação dediversos
padrões.
7 . 4ServiceLocator versus DependencyInjection
Depois de aprendersobreos padrões Dependency Injection e Service
Locator,surgeadúvidadequaldelesutilizar.Antesdecomeçaraexplorarasvan-
tagensedesvantagensdecadaum,éimportanteressaltarquecomautilização de
161

## Página 183

7.4.ServiceLocatorversusDependencyInjection CasadoCódigo
qualquerumdosdoisépossívelseobtermodularidade,particionandoaaplicação
empartesefetivamenteindependentes.Dessaforma,ficamaissimplesaintrodução
denovasimplementações semanecessidadederecompilaçãodocódigodasclasses
queasutilizam.Comisso,cadaumdosmódulosdosistemapodeevoluirdeforma
independente,facilitandoamanutençãoeevoluçãodosoftware.
U m adasgrandesdiferençasentreosdoispadrões estáemquempossuiares-
ponsabilidadedemontaraconfiguraçãodeobjetosdaaplicação.Quandoopadrão
Dependency Injectionéutilizado,elaficacentralizadanaclasseresponsável
pelamontagem. Nessecaso,elaprecisaconhecertodasasdependênciasdetodas
asclassesenvolvidas,estaticamenteoudinamicamenteapartirdealgumaconfigu-
ração. Diferentemente,quandoseutilizao Service Locator,cadaclasseéres-
ponsávelporbuscarsuasdependênciasapartirdeumaclasseresponsávelpelalo-
calizaçãodosserviços.Issopermitequenovasclassesdefinamnovospontosonde
outrasabstraçõespossamserinseridas,semanecessidadedehaverumpontocentral
quesaibadessanovadependência.
Emresumo,quandoseinjetadependências,aresponsabilidadedemontartodaa
aplicaçãoficacentralizadae,quandocadaclassebuscaseusserviços,essaresponsa-
bilidadeficadistribuída.Sendoassim,seocontextoéumaaplicaçãoondesedeseja
termodularidadeparaquestõesdemanutençãoeevolução,masnãoexisteanecessi-
dadedaadiçãodenovasclassesdinamicamente,entãoo Dependency Injection
éumaboasolução.Porém,emcenáriosemqueaarquiteturaébaseadaemplugins
enão existeumpontonaaplicação noqualsetemconsciênciadetodaspossíveis
dependências,entãoo Service Locatorsemostramaisadequado.
U m aconsequênciadissoestáemquão explícitassão asdependênciasdeuma
classe. Quandoseusao Dependency Injection,éfácilvisualizaratravésdos
construtores,interfacesemétodosdeacessoquaissãoasdependênciasquepodem
serinjetadas. Poroutrolado,ainvocação deum Service Locatorpodeestar
encapsuladadentrodosmétodosdaclasse,nãoasexpondoexternamente.Issopode
terumefeitonegativo,poisnão deixaclaroquaisprecisamserconfiguradaspara
umadeterminadaclasse.
A p e s a rdenãoserobrigatório,o Dependency Injectionacabasendomuito
utilizadoemambientesondeosobjetosdaaplicaçãosãogerenciadosporumcontai-
ner.U mexemplodissoseriamaplicações webouaplicações EJB,emqueociclode
vidadosobjetosécontroladopeloservidor.Dessaforma,comoacriaçãodosobje-
tosquetratarãoasrequisições ficaacargodocontainer,eletemaoportunidadede
injetarasdependênciasnomomentocerto.FrameworkscomoSpringsãochamados
162

## Página 184

CasadoCódigo Capítulo7 .Modularidade
de lightweight container,oucontainerleve,devidoaofatodecontrolaremociclode
vidadosobjetosgerenciadosporeles.
U mpontoondeo Dependency Injectioncertamentelevavantageména
testabilidade. Comoadependênciaéinjetadanaclasse,essemesmomecanismo
podeserutilizadoparaainjeçãodeumobjetofalso,ou mock o b j e c t[25],paraisolar
aclasseduranteoteste.Jácomo Service Locator,issopodeserumpoucomais
complicado,poiso mock o b j e c tprecisariaserconfiguradoparaserretornadopor
ele.Dependendodecomoessaconfiguraçãoéfeita,issopodesermaissimplesou
maiscomplicado,porémdequalquerformapodeserumproblemaparacasosem
queaclassedo mockégeradadinamicamenteporalgumframework.Nessescasos,
umasoluçãoseriajápensaremumaimplementaçãoquesimplifiqueasubstituição
daimplementaçãoretornadaparaumserviçoemcódigodeteste.
Alternativ as dePr o j e t o
Ospadrões deprojetodocumentamsoluções recorrentesquesãouti-
lizadasemumdeterminadocontexto. Pormaisqueelesdocumentem
boassoluções, nemsempreumdeterminadopadrãoéamelhorsolução
paraumaaplicação.Porisso,podemexistirmaisdeumpadrãoquepo-
demseraplicadosnaresoluçãodeummesmoproblema,comomostrado
nessecapítulo.Sevocêquerflexibilizarospassosdeumalgoritmo,você
podeutilizaro Template Methodparafazerissocomherança,ouo
Strategyparausarcomposição. Sevocêquercombinarsoluções de
classesexistentesdeformatransparente,pode-seutilizaro Composite
ouo Chain of Responsibility. Pormaisqueambosospadrões
nessescasosresolvamoproblema,elespossuemcaracterísticasecon-
sequênciasdiferentes.Dessaforma,éimportantenãoutilizarospadrões
cegamenteeavaliardentreasalternativasexistentesquaisasquepossuem
consequênciasmaisadequadasparaocontextodasuaaplicação.
7 . 5Considerações Finaisd oCapítulo
Nessecapítuloabordamospadrões quefocamemsoluções paraqueseconsigaobter
modularidadeparaaplicações. Essassoluções atuamemummomentocrucialna
163

## Página 185

7.5.Considerações FinaisdoCapítulo CasadoCódigo
vidadosobjetos:asuacriação.Desdeoprimeirocapítulodesselivro,jáforamapre-
sentadassoluções queutilizamencapsulamentoepolimorfismoparadesacoplaros
objetos,porémnomomentodacriação,emqueaimplementaçãoefetivamentepre-
cisaserinstanciada,areferênciadiretaàclassecostumainterferirnamodularidade.
Opadrão Dynamic Factoryfoiapresentadocomoumabasequepodeser
utilizadapelosoutrospadrões paraocarregamentodinâmicodasimplementações
quedevemserutilizadasparacomporaclasseprincipal.Emseguida,forammsotra-
dosospadrões Dependency Injectione Service Locator,queapresentam
alternativasarespeitodecomoumaclassepodedelegaracriação desuasdepen-
dências.Secombinadoscomumasoluçãoqueutilizaum Dynamic Factoryna
criaçãodasinstâncias,épossívelrealmentemodularizaraaplicação.
164

## Página 186

Capítulo8
AdicionandoOperações
“ N ó snão podemos r e s o l v e rproblemas usando o mesmo tipo de pensamento q u e
usamos quando nós os criamos. ”
–AlbertEinstein
Noscapítulosanterioresdesselivroforamapresentadosalgunspadrões queau-
xiliamnaadiçãodefuncionalidadeemclassesjáexistentes.Porexemplo,ospadrões
Proxye Decoratorpermitemaadiçãodefuncionalidadesatravésdoencapsula-
mentodoobjetooriginal.Dessaforma,um Proxypodeadicionarumalógicaantes
oudepoisdainvocação deummétodo.Porémessalógicaadicionadaéconside-
radatransversalàdaclassequeestásendoencapsulada,ouseja,elaéindependente
ecomplementaraelas.
Poroutrolado, padrões queutilizamcomposição, comoo Strategy eo
Bridge,podemtrocarainstânciaqueacompõe paraalterarafuncionalidadeque
estásendoexecutada.Deformacomplementar,padrõesquepermitemacomposição
recursiva,comoo Compositeeo Chain of Responsibility,possibilitama
combinaçãodocomportamentodasimplementações. A p e s a rdesserecursopermitir

## Página 187

8.1.ClassesqueRepresentamComandos CasadoCódigo
quesejapossívelvariar,oumesmocomplementar,afuncionalidadedecertospontos
deumobjeto,elanãopermitequesejamadicionadasnovasoperações.
Essecapítuloiráexplorarpadrões quepodemserutilizadosparaaadiçãodeno-
vasfuncionalidadesenovasoperações paraclasses.Seguindoosprincípiosdaori-
entaçãoaobjetos,nessescasos,aprópriaoperaçãoseráconsideradaumaentidade
nosoftware.Apartirdisso,serãodefinidasabstrações paraquediversasoperações
possamserimplementadaseincorporadasàsclassessemanecessidadedesuamo-
dificação.
8.1 Classes queRepresentam Comandos
“ Umcomando com sabedoria, éobedecido com alegria. ”
–ThomasFuller
Muitasvezes,precisamosdefiniroperações aseremexecutadassemquequem
acionaessaoperaçãotenhaciênciadoqueestásendoexecutado.U mexemploco-
mumdissoocorreeminterfacesgráficas,quandoalgoprecisaseradicionadopara
serexecutadonoacionamentodeumbotão oudeumitemdemenu. Emoutras
palavras,éprecisoqueaexecuçãodeumalógica,quenormalmenteérepresentada
atravésdeummétodo,sejarepresentadaporumaclasse.
V a m o stomarcomocontextodoexemploumaaplicaçãodee-commercequepre-
cisaserimplantadaemdiversosclientesquepossuemdiferentesnecessidades. O
carrinhodecompras,porexemplo,queéumaimportanteclasseparaosistema,pre-
cisadediferentesoperações dependendodaimplantação. Emumalojaquevende
produtosdeinformática,ocarrinhodevesaberinformarovalordofreteeaprevi-
sãodeentrega,porémessasinformações nãofazemsentidoparaumalojaquevende
músicadigitaleprecisainformarotamanhodosarquivosparadownloadeotempo
estimadodeacordocomavelocidadedaconexãodocliente.
Comofoiditonaintrodução,algunsdospadrõesjáapresentadosnesselivroper-
mitemalteraraimplementaçãodeumaoperaçãoimplementadaporumaclasse.Po-
rémesseseriaumcasodiferente,noqualdiferentesoperações seriamdisponibiliza-
daspelaclasse,dependendodasituação.Comolidarcomisso?Comopermitirque
asoperações disponibilizadaspelaclassepossamserincorporadasdeformadinâ-
mica?
ConhecendoopadrãoCommand
166

## Página 188

CasadoCódigo Capítulo8. AdicionandoOperações
O Commandéumpadrãoqueconsistenarepresentaçãodeumaoperaçãocomo
umaclasse.Aabstraçãoquerepresentaocomando,noformatodeumasuperclasse
ouinterface,defineummétodoquedeveserutilizadoparaexecutaraoperação.
Oscomandosconcretos,queimplementamouestendemaabstração,devemdefinir
comoatributoaestruturadedadosnecessáriaparaasuaexecução. Dessaforma,o
comandoacabasendoumaclassequepoderepresentarumaoperaçãodosistemain-
dependentedetodoocontexto.Éessacaracterísticaquepermitediversasaplicações
dessepadrão!
AFigura8.1apresentaautilização do Commandnocontextodeumcompo-
nente.U mcomponentepodepossuircomouma H o o kClassumcomando,oqual
eleiráexecutarcomorespostaaalgumeventodosistema.Aclassequecriaocom-
ponente,nafigurarepresentadapelaclasse Fabrica,deveinjetaraimplementação
de Comandoadequada.Nessecaso,ousodeumainterfacemaisgeralpermiteque
umamesmaimplementaçãopossaserusadaemvárioscomponentesequequalquer
implementaçãopossaserassociadaaumcomponenteespecífico.
Figura8.1:UtilizaçãodoCommandcomopartedeumcomponente
A p e s a rdaclasse Componenterepresentadanodiagramapoderserumcom-
ponentegráficoounão,ousodessepadrãoémuitocomumparaaconfiguraçãode
respostasparaações deusuárioparacomponentesdeinterfacegráfica.Imagine,por
exemplo,queummesmocomandopodeserexecutadoaoseclicaremumbotão,
aoselecionarumitemdemenuouaoacessarumatalhonoteclado.Poroutrolado,
váriosbotões quesãorepresentadospelamesmaclasseprecisamexecutardiferen-
tescomandosaoseremacionados.Essaliberdadenaassociaçãodoscomandosaos
167

## Página 189

8.1.ClassesqueRepresentamComandos CasadoCódigo
componenteséumadasvantagensdessepadrão.
Muitasvezes,aclassequepossui Commandnãooexecutadiretamente,maso
passaparaoutraclasseparasuaexecução.AFigura8.2apresentaessecenário.Nesse
caso,aclasse Clientepegaocomandoconfiguradoemalgumcomponenteoucria
ainstânciade ComandoConcretocomocomportamentodesejado,e
enviaaclasse ExecutorComandosparaexecução. Essaestruturafazsentido
quandoexisteanecessidadedeumcontrolecentraldoscomandosqueestãosendo
executados.U mexemplodessasituaçãoseriaquandoénecessárioinjetarrecursos
nessocomando,comoumaconexão comobancodedados. Outrocenárioseria
quandoseprecisaguardarumhistóricodoscomandosexecutados,comoparaques-
tões detransaçãoouparapossibilitarqueousuáriovolteatrásemumaação.
Figura8.2:PassandooCommandcomoparâmetroparaexecução
U m adasprincipaisconsequênciaspositivasdopadrão Commandestánafacili-
dadedeadiçãodenovasoperações aosoftware.Poreleabstrairoconceitodeope-
ração,issopermitequenovasimplementações possamserfacilmenteincorporadas.
Outroaspectopositivodo Commandestánofatodeeleserumarepresentaçãode
umaoperaçãoindependentedocontextoemqueelaestáinserida.Issopermiteque
essaoperaçãosejaarmazenadaemumhistóricoouenviadapelarede,deformaque
suasinformações possamseracessadaseafuncionalidadeexecutadaemqualquer
momento.Issoémuitoútilparaaimplementaçãodetransações, registrodeaudito-
riaeatémesmoafuncionalidadededesfazerações dousuário.
Poroutrolado,ofatodecadaoperaçãoserrepresentadaporumaclassediferente
fazcomqueonúmerodeclassescresçabastante.U mCommandtambémacabapre-
judicandooencapsulamentodaclasserelacionadacomsuaexecução,poiseleprecisa
168

## Página 190

CasadoCódigo Capítulo8. AdicionandoOperações
teracessoàsinformaçõesdela,quemuitasvezesfariamsentidoapenasinternamente.
U m aformadecontornaressaquestãoéutilizar Dependency Injectionparain-
jetarasinformaçõesnasclassesquerepresentamumcomando.U m aalternativapara
identificarqualparâmetrodeveserinjetadopoderiaserautilizaçãodainjeçãopor
interfaces,emqueapresençadeumainterfaceindicariaanecessidadedeumain-
formaçãonocomando.
ImplementandooCarrinhodeCompras
Paraexemplificarautilizaçãodopadrão Command,vamospegaroexemplodo
carrinhodecomprasutilizadonaintroduçãodessaseção.Oobjetivoépermitirque
ocarrinhodecompraspossaterdiferentesoperações deacordocomocontextoem
queaaplicaçãotiversidoimplantada.Issoirápermitirnãosomentequeelepossa
possuirdiferentesoperações emdiferentescontextos,mastambémquenovasope-
rações possamserfacilmenteincorporadas.
Paraimplementaropadrão Commandnessecontexto,asoperações docarrinho
decomprasdevemserrepresentadaspeloscomandos.Alistagemaseguirapresenta
ainterfacequedeveserimplementadapelasclassesquerepresentamoscomandos.
Observe que o método executar() não recebe nenhumparâmetro,pois os
parâmetrosqueessaexecuçãotiverdeverãoserinseridosnaclasseearmazenados
comoatributos. Oretornodotipo Objectfoiutilizadoparapossibilitarqueo
comandoretornassequalquerobjetocomoresultadodesuaexecução,oqualdeve
sertratadoporqueminvocá-lo.
Listagem 8.1-Interfacequeabstraiumaoperaçãodocarrinhodecompras:
public interface ComandoCarrinho{
public Object executar();
}
Aclasse CarrinhoCompras,apresentadanalistagemaseguir,éaclasseque
representaocarrinhodecompraspropriamentedito. Emsuaestruturadedados,
alémdousuárioedalistadeprodutos,tambémestãooscomandosdisponíveispara
aquelainstância.Oscomandossãoarmazenadosemummapaesãoidentificados
porumaString. Dentrodessecontexto,ométodo executaComando() seria
responsávelporexecutá-loepassarparaeleasinformações necessáriasparasua
execução. Casoocomandonão sejaencontradono Map,umaexceção dotipo
ComandoNaoEncontradoExceptionélançadapelométodo.
169

## Página 191

8.1.ClassesqueRepresentamComandos CasadoCódigo
Listagem 8.2-ImplementaçãodoCarrinhodeCompras:
public class CarrinhoCompras{
private Map<String, ComandoCarrinho> comandos;
private List<Produto> produtos;
private Usuario usuario;
//outros métodos de carrinho de compras
public Object executaComando(String nomeComando)
throws ComandoNaoEncontradoException{
ComandoCarrinho c = comandos.get(nomeComando);
if(c == null)
throw new ComandoNaoEncontradoException();
if(c instanceof CienteDosProdutos){
(CienteDosProdutos(c)).setlistaProdutos(produtos);
}
if(c instanceof CienteDoUsuario){
(CienteDoUsuario(c)).setUsuario(usuario);
}
return c.executar();
}
public Set<String> getComandosDisponiveis(){
return comandos.keySet();
}
}
U m acaracterística interessante dessa solução éa utilização de interfaces
paraqueocarrinhopossainjetarasinformações noscomandos. Asinterfaces
CienteDosProdutos e CienteDoUsuario são implementadaspelas classes
que desejam respectivamente receber a lista de produtose as informações do
usuário.Issopermiteàsclassessinalizaremdequalinformaçãoprecisamparaseu
processamentoeàclasse CarrinhoComprassaberqualinformação elaprecisa
passar.
Listagem 8.3 - Exemplo de operação que calcula o tamanho para download
dosprodutosdocarrinho:
170

## Página 192

CasadoCódigo Capítulo8. AdicionandoOperações
public class TamanhoParaDownload
implements ComandoCarrinho, CienteDosProdutos{
private List<Produto> produtos;
public void setListaProdutos(List<Produto> produtos){
this.produtos =produtos;
}
public Object executar(){
double tamanho = 0;
for(Produto p : produtos){
if(p.isDigital()){
tamanho += p.getTamanhoDownlaod();
}
}
return double;
}
}
CombinandooCommandcomOutrosPadrões
Opadrão Commandpossuiestruturasimples,atéumpoucoparecidacomoutros
padrõesbaseadosemcomposição,comoo Observereo Strategy.Devidoaessa
simplicidade,muitasvezesacabasendofácilsuacombinaçãocomoutrospadrões.
Porexemplo,quandodiversoscomandospossuírempassossimilares,autilização
deum Template Methodcomobasedodométododeexecução podeevitara
repetiçãodecódigo. Devidoàinterfacecomumcompartilhadapeloscomandos,a
criação deum Proxyqueencapsuleumcomandopodeserútilparaaadição de
funcionalidadesemqualquerimplementação.
Paraquequenovoscomandospossamserfacilmenteadicionadosaosistema,
umacombinação comuméautilização deum Dynamic Factory oudeum
Service Locator paraocarregamentodasimplementações. Muitasvezes, a
configuração doscomandoséacompanhadadeinformações arespeitodassitua-
ções emquedevemserinvocados.Alistagemaseguirretomaoexemplodaclasse
CarrinhoComprasemostracomooscomandospoderiamsercarregadosdinami-
camentenoconstrutordaclasse.Nocaso,opadrão Service Locatoréutilizado
apartirdaclasse ServiceLoader.
Listagem 8.4-UtilizaçãodeumServiceLocatorparalocalizaroscomandos:
171

## Página 193

8.1.ClassesqueRepresentamComandos CasadoCódigo
public class CarrinhoCompras{
private Map<String, ComandoCarrinho> comandos;
public CarrinhoCompras(){
comandos = new HashMap<>();
carregarComandos();
}
public void carregarComandos(){
}
}
U m aoutrasituaçãoquepodeocorreréquandoutilizamoso Commandehápas-
sossimilaresaseremexecutadosemdiversoscenários.Porexemplo,asolicitação
deumaconfirmaçãodousuárioouaatualizaçãodeumatabelapodemserpassos
necessáriosparadiferentesoperações. Nessecaso,pode-seconsideraraimplemen-
taçãodesequênciasdecomandos,emqueoacionamentodeumcomandoresultará
naexecuçãodeumacadeiadeoutroscomandosligadosaele.Somentepelapalavra
“encadeamento”jáépossívelpensarno Chain of Responsibility!
Para exemplificarmos uma cadeia de comandos, considere a abstração
ComandoCarrinho apresentadana seção anterior. Paraimplementaro enca-
deamentodecomandos,iremostransformarainterfaceemumaclasseabstrata,
cujo código estáapresentado na listagem a seguir. Essa classe abstrata pos-
sui o atributo proximo que representa o próximo comando da sequência.
O método executar(), que estava presente na interface, agora se tornou
uma métodoconcreto. Esse métodoinvocaprimeiramenteo métodoabstrato
executarComando(), no qual a funcionalidade daquele comando deve ser
inserida,eemseguidaexecutaopróximocomandocasoessenãosejanulo.
Listagem 8.5-Interfacequeabstraiumaoperaçãodocarrinhodecompras:
public abstract class ComandoCarrinho{
private ComandoCarrinho proximo;
public ComandoCarrinho(ComandoCarrinho proximo){
this.proximo = proximo;
}
172

## Página 194

CasadoCódigo Capítulo8. AdicionandoOperações
public void executar(){
executarComando();
if(proximo != null)
proximo.executar();
}
protected abstract void executarComando();
public abstract Object getResultado();
}
Outraquestãoqueprecisouseralteradaparaaimplementaçãodasequênciade
comandosfoiaformaqueoresultadodocomandoédisponibilizado.Naimplemen-
taçãoanterior,oretornoeradadopeloprópriométodo executar().Nessecaso,
anãoserquehajaumaformapadrãodecombinarosresultadosdasequência,não
épossívelretornaroresultadonoprópriométodo.Asoluçãodadanessecasofoia
definiçãodeummétodoabstratoparaoretornodoresultado.Dessaforma,aclasse
docomandopodeescolhercomooresultadoseráobtidoe,casosejaaplicável,como
eleserácombinadocomoresultadodocomandoexecutadonasequência.
Combine padrões, mas para diferentes problemas
Acombinação depadrões éumrecursomuitopoderoso,quepode
gerarumasinergiaquetrazbenefíciosmuitomaioresdoqueautiliza-
çãoisoladadecadapadrão. Porémessacombinaçãodeveserfeitacom
cuidado,poisautilizaçãodeváriospadrões emumamesmasoluçãosem
necessidadeéumamáprática.Issoporqueelespodemtornarasolu-
ção complexasemtrazernenhumbenefício. T o d avezquepensarem
umasoluçãocommúltiplospadrões, minhasugestãoéquevocêfaçaum
exercícioseperguntandoqualoproblemaquecadaumestáresolvendo.
Secasonãoconseguirresponderessaperguntaparaalgumdeles,consi-
dereremoveraquelepadrãodasolução. Mesmoquevocêestejaerrado
eopadrãoacabevoltando,pelomenosvocêaprendeumaissobreoseu
problemaepodeinclusiveconsideraroutrasalternativas.
8.2 Cenários deAplicação d oCommand
Aseçãoanteriordescreveuopadrão Commandeapresentouoexemplodocarrinho
decompras,noqualeleerautilizadopararepresentarnovasoperações aseremin-
173

## Página 195

8.2. CenáriosdeAplicaçãodoCommand CasadoCódigo
seridasnocarrinho.Existemoutroscenáriosimportantesondeessepadrãopossui
umagrandeaplicabilidade.Éinteressantecomoemcadaumessepadrãoéimple-
mentadoporummotivodiferente,porémemtodoselesasoluçãocomo Command
érelacionadacomousodeumaclassepararepresentarumaoperação. Aspróxi-
massubseções irãoapresentardiferentesocasiões paraouso,mostrandoexemplos
decódigodecomoimplementá-los.
ExecuçãoRemota
U m adasvantagensdeseterumarepresentaçãodeumaoperaçãodosistemaé
poderpassaressaoperaçãocomoparâmetro.Esseéocasomostradonaseçãoante-
riorquandohaviaumexecutordecomandos.U m avantagemdessaestruturaéque
esseexecutorpodeestarlocalizadoemumamáquinaremota,oferecendoserviços
paraaexecuçãodessescomandos.Essaestruturapermiteterumainterfacedeser-
viçosmaisenxuta,provendoparaclientesremotosafuncionalidadedeexecuçãode
comandos.
Paraexemplificarcomoumexecutorremotodecomandospoderiaserimple-
mentado,essaseçãomostraoexemplodeumSessionBeanqueexecutacomandos
remotamente.Primeiro,éprecisodefinirumainterfaceremotaparaessaexecução,
comomostradonalistagemaseguir.U m aquestãonotávelnessecasoéainterface
Comandoestender Serializableparapoderserenviadaatravésdarede.Nesse
caso,éimportantequeasimplementações tragamconsigotodasasinformações
necessáriasparaaexecução.
Listagem 8.6-Interfaceremotapraexecuçãodecomandos:
@Remote
public interface ExecutorComandos{
public Object executarComando(Comando c);
}
Em seguida, precisamos implementar o Session Bean que implementa a
interfaceremotadefinida. Issoéapresentadonalistagemaseguir. Ométodo
executarComando()executaocomandoeemseguidaretornaoresultadoda
execuçãoqueérecuperadodeumapropriedadedesseobjeto.Essemétodotambém
podeinjetarnocomandorecursosqueestãopresentesapenasnoservidor,comoo
EntityManagermostradonoexemplo,queserveparaacessarobancodedados.
Paraisso,bastaocomandoimplementarainterface PrecisaEntityManager.
174

## Página 196

CasadoCódigo Capítulo8. AdicionandoOperações
Listagem 8.7-SessionBeanparaexecuçãoremotadecomandos:
@Stateless
public class ExecutorRemoto implements ExecutorComandos{
@PersistenceContext
private EntityManager em;
public Object executarComando(Comando c){
if(c instanceof PrecisaEntityManager){
((PrecisaEntityManager)c).setEntityManager(em);
}
c.executar()
return c.getResultado();
}
}
Aimplementação deumclienteparaesseserviçoacabasendomuitosimples.
Alistagemaseguirmostraummétodoutilitárioquepoderia serusadoparaa
execuçãodecomandosemumservidorremoto.Aspropriedadespassadasparao
métodoservem,agrossomodo,paraalocalização doservidoreoparâmetrode
nome jndiNameparaalocalizaçãodoserviçodeexecuçãodecomandos.Como
essasinformações dependemdoservidoredasuaversão,decidiu-seporpassá-las
comoparâmetro.Apartirdachamadadessemétodoocomandoseráenviadoao
servidoreexecutado,eoresultadodesuaexecuçãoenviadodevoltaeretornado.
Listagem 8.8-ClientequeacessaoSessionBeanparaexecuçãodeumcomandono
servidor:
public static Object executaComandoRemoto(Comando c,
String jndiName, Properties props) throws NamingException{
InitialContext ic = new InitialContext(props);
ExecutorComandos ec = ic.lookup(jndiName);
return ec.executarComando(c);
}
Aprincipalvantagemdessasolução équeficamuitosimplesadicionarnovas
funcionalidadesparaseremexecutadasnoservidor.Normalmente,cadanovaope-
raçãonoservidorprecisadadefiniçãodeummétodonainterfaceremotaenaim-
plementação paraquesejaconsumidoporseusclientes. Nasolução apresentada,
175

## Página 197

8.2. CenáriosdeAplicaçãodoCommand CasadoCódigo
apenasométododeexecuçãodecomandosprecisaserexpostoremotamente,bas-
tandoacriaçãodeumnovocomandoparaaintroduçãodeumaoperação.
U m aconsequêncianegativadessainterfacemaisgeraléqueissofacilitaaintro-
duçãodecomandosmaliciosos,abrindoumabrechaparaexecuçãodefuncionali-
dadesdiversasnoservidor.A p e s a rdaclassedocomandoprecisarestarpresenteno
classpathdoservidorparapoderserexecutada,éaconselhávelimplementarnoser-
vidorfuncionalidadesdesegurançavisandoautorizaroacessoapenasacomandos
conhecidos.
T r a n s açõeseLogging
Ofatodeasoperações seremrepresentadasporobjetosepoderemserarmaze-
nadaspermitequesejafeitoumhistóricodoscomandosexecutadospelosistema.
Elepodeserpersistido,servindocomoumlogdoquefoiexecutadopelaaplicação.
Issotambémpossibilitaqueessasoperações sejamrefeitasnocasodeumaquedado
sistema,oquefazcomqueoscomandossirvampararepresentartransaçõesduráveis
emsistemasdeinformação.
Parailustrarousodo Commandparaimplementaçãodetransações, seráutili-
zadocomoexemplooframeworkPrevayler(http://prevayler.org).Esseframeworké
umaimplementaçãodecódigoabertoquefazapersistênciadeobjetosemJava.Com
aimplementaçãodopadrão Prevalent System[26],elemantémosobjetosper-
sistentesemmemóriaearmazenaastransações paraumapossívelrecuperaçãodo
sistema.Detemposemtempos,étiradoumsnapshotdoobjetopersistido,queégra-
vadoserializadoemdisco.Nosintervalosentreentreessasgravações, astransações
sãoarmazenadasparaguardarasalterações realizadas.
Considere,porexemplo,queoobjetoqueestásendopersistidopeloPrevayler
sejaumalistaequeumadasoperações quepodemserfeitasnessalistasejaa
inserçãodeumnovoelemento.Alistagemaseguirapresentacomoessatransação
seria implementada. Observe que ela possui como parte de sua estrutura de
dadosoitemqueseráinserido,alémdométododeexecuçãodefinidonainterface
Transaction,nocaso executeOn().
Listagem 8.9 - Exemplo de uma transação do Prevayler para adicionar um
itememumalista:
public class InserirItem implements Transaction<List<Serializable>>{
private Serializable item;
176

## Página 198

CasadoCódigo Capítulo8. AdicionandoOperações
public InserirItem(Serializable item){
this.item = item;
}
public void executeOn(List<Serializable> lista, Date date){
lista.add(item);
}
}
Autilização do Commandparaadefinição detransações, nessecaso,permite
queelasejaarmazenadaerecuperadasenecessário.Casoalistafossemodificada
diretamente,seriaprecisoarmazenaressalistaacadaalteração paraqueelasnão
fossemperdidas. Comoépossívelpersistiraalteração,épossívelarmazenaruma
versãodalistaetodososcomandosexecutadosnelaapartirdaqueleponto.Dessa
forma,casosejanecessáriorecuperarsuaúltimaversão, bastarecuperaraversão
serializadacomtodasastransações apartirdaquelepontoeexecutarastransações
novamente.
FazereDesfazer
U m aoutraaplicaçãodo Commandéparadarsuportenaaplicaçãoàfuncionali-
dadededesfazerações realizadaspelousuário.Nessecaso,asoperações realizadas
poreledevemserarmazenadasparapoderemseracessadasedesfeitas.Paraqueisso
sejapossível,alémdeummétodoparaexecutarocomando,tambéménecessário
umquerevertaosseusefeitos. Alistagemaseguirmostraoexemplodeumain-
terfaceparaadefiniçãodeumcomandocomosmétodosfazer()e desfazer().
Listagem 8.10-Interfaceparacomandoquepodeserdesfeito:
public interface Comando{
public void fazer();
public void desfazer();
}
Estecenárioéumexemplonoqualumaclasseparaaexecuçãodecomandosse
faznecessária.Seupapeléproverumlocalcentralizadoparaexecuçãoearmazena-
mentodoscomandos,paraviabilizarqueelespossamserrecuperadoserevertidos
senecessário.Alistagemaseguirapresentaumexecutordecomandosquepermite
queoscomandosexecutadospossamserdesfeitosequeoscomandosdesfeitos
177

## Página 199

8.2. CenáriosdeAplicaçãodoCommand CasadoCódigo
possamserrefeitos.
Listagem 8.11- Executor de comandos que possibilita que comandos sejam
desfeitoserefeitos:
public class ExecutorComandos {
private Queue<Comando> feitas;
private Queue<Comando> desfeitas;
public ExecutorComandos() {
feitas = new LinkedList<>();
desfeitas = new LinkedList<>();
}
public void executarComando(Comando c) {
c.fazer();
feitas.offer(c);
desfeitas.clear();
}
public void desfazer() {
if(!feitas.isEmpty()) {
Comando c = feitas.pool();
c.desfazer();
desfeitas.offer(c);
}
}
public void refazer() {
if(!desfeitas.isEmpty()) {
Comando c = desfeitas.pool();
c.fazer();
feitas.offer(c);
}
}
}
Essaclassepossuiduaspilhasquesão chamadasde feitase desfeitas.
Quandoumcomandoéexecutado,eleéempilhadonapilha feitas. Quandoo
métododesfazer()éinvocado,ocomandodecimadapilha feitasédesempi-
lhado,invoca-seneleométododesfazer()eeleécolocadonapilha desfeitas.
Nessemomento,ousuárioaindatemaoportunidadedevoltaratráscomachamada
dométodo refazer(),oqualdesempilhaumcomandodapilha desfeitas,
178

## Página 200

CasadoCódigo Capítulo8. AdicionandoOperações
executaocomandoeoadicionanapilha feitas.Porém,comosófazsentidorefa-
zerumcomandologoquefoidesfeito,semprequeumnovocomandoéexecutado,
apilha desfeitaséesvaziada.
Emumexecutordecomandosmaissofisticados,poderiahavercomandosque
nãopodemserdefeitosoucomandosinertes,ouseja,quenãodeveriamserincluídos
napilhadecomandosrealizados. Compequenasmodificações, aimplementação
apresentadapoderiaseradaptadaparaessetipoderequisito.Nessecasodehaver
diversostiposdecomando,diferentesinterfacesqueexpressamaspossíveisopera-
ções decadaumdelespoderiamserutilizadasparadiferenciação.Outraalternativa
seriaautilizaçãodeumainterfaceúnicaedeanotações paramarcaroscomandos
queprecisamsertratadosdeformadistinta.
8.3 DoubleDispatch-Me chama, que eu te chamo!
“ N ã ol i g u epara nós, nós l i g a m o spara você!”
–PrincípiodeHollywood
U m asituaçãoquemuitasvezesocorrenocotidianoéumaperguntaserrespon-
didacomoutrapergunta.Imaginequeumagarotaquestioneoseunamorado:“E uv i
vocêdentro da boate na sexta a noite! O q u evocêestava fazendo lá?”eeleresponda:
“Se vocême v i uvocêt amb é mestava lá!O q u evocêestáfazendo lá?” .Brincadeiras
àparte,umatécnicaimportantequepodeserutilizadaemumprojetoorientadoa
objetoséfazercomqueumachamadademétodosejarespondidacomachamada
deoutrométodonoobjetopassadocomoparâmetro.
Parailustraroproblema,vamosretomaroexemplodocarrinhodecompras,po-
rémconsiderandoquediversostiposprodutospossamseradicionadosnocarrinho
emumamesmaloja.Dependendodotipodeproduto,diferentespropriedadespre-
cisamsermodificadas. U m amúsica,porexemplo,adicionariaseupreçonovalor
totaleseutamanhonototalparadownload.Jáumprodutofísico,alémdopreço,
adicionariaseupesoevolume,queseriamutilizadosposteriormenteparaocálculo
dofrete.Alémdissooutrostiposdeprodutopodemsurgir,comoavendadepassa-
gensaéreasouentradasparaeventos.V a m o svernessaseçãocomoseriaasolução
semautilizaçãodepadrões edepoiscomousodo Double Dispatch[28].
ResolvendooProblemadoCarrinhosemPadrões
Oprimeiroinstintoparaaimplementaçãodaadiçãodediferentestiposdepro-
dutosseriacriarcondicionaisparaselecionarentreosváriostiposdeproduto.Nesse
179

## Página 201

8.3.DoubleDispatch-Mechama,queeutechamo! CasadoCódigo
caso,otipodoproduto,atravésdasuaclasse,seriautilizadoparadiferenciá-los.A
listagemaseguirmostraoexemplodecomoficariaocódigodessasolução.Apartir
dela,acadanovotipodeproduto,umnovocondicionalprecisariaseradicionado
nessemétodo.
Listagem 8.12-U s a n d ocondicionaisparaidentificarotipodoproduto:
public class CarrinhoCompras {
//outros métodos e atributos
public void adicionarProduto(Produto p) {
produtos.add(p);
if(Produto instanceof ProdutoDigital) {
ProdutoDigital pd = (ProdutoDigital) p;
adicionaPropriedade("PRECO", pd.getPreco());
adicionaPropriedade("DOWNLOAD", pd.getTamanho());
} else if(Produto instanceof ProdutoFisico) {
ProdutoFisico pf = (ProdutoFisico) p;
adicionaPropriedade("PRECO", pf.getPreco());
adicionaPropriedade("VOLUME", pf.getVolume());
adicionaPropriedade("PESO", pf.getPeso());
} else {
//mais condicionais para cada tipo de produto
}
}
}
U m aformadeeliminaroscondicionaisseriaacriação deummétodopara
aadição decadatipodeproduto,comomostradonapróximalistagem. Como
emJavapode-sefazerasobrecargademétodos,épossívelquetodospossuamo
mesmonome. Dessaforma,ométodoseriaselecionadodeacordocomotipode
produtopassadoparaele. A p e s a rdessasolução eliminaroscondicionais,ainda
serianecessáriaaadição denovosmétodosnaclasse CarrinhoComprasparaa
adiçãodenovostiposprodutos.
Listagem 8.13-U s a n d oummétododiferenteparacadatipodeproduto:
public class CarrinhoCompras {
//outros métodos e atributos
180

## Página 202

CasadoCódigo Capítulo8. AdicionandoOperações
public void adicionarProduto(ProdutoDigital pd) {
produtos.add(pd);
adicionaPropriedade("PRECO", pd.getPreco());
adicionaPropriedade("DOWNLOAD", pd.getTamanho());
}
public void adicionaProduto(ProdutoFisico pf) {
produtos.add(pf);
adicionaPropriedade("PRECO", pf.getPreco());
adicionaPropriedade("VOLUME", pf.getVolume());
adicionaPropriedade("PESO", pf.getPeso());
}
//outros métodos para cada tipo de produto
}
Oproblemaaquiéqueaadiçãodeumnovotipodeprodutonaverdadeéuma
novaoperaçãoparaaclasse CarrinhoCompras,poiscadaumpossuiumalógica
diferente.Ambasasimplementações apresentadasexigemquemaiscódigosejaadi-
cionadonaclasseparaaadiçãoaosuportedeumnovotipodeproduto.Comoper-
mitirissosemalteraraclasse?
AplicandooDoubleDispatchnoCarrinhodeCompras
Comotalvezvocêdesconfiepelaintrodução, amelhorformaderesponder
essaperguntaédevolverapergunta! Nessecaso,aperguntaqueestásendofeita
paraocarrinhoéoqueeleprecisafazerquandoumdeterminadotipodeproduto
foradicionado. Então, umaformadedevolveressaperguntaseriaelequestionar
oprodutoqualpropriedadeeledeveadicionarnocarrinho. Alistagemaseguir
mostra como ficaria a classe CarrinhoCompra com a implementação dessa
solução.
Listagem 8.14-UtilizandooDoubleDispatchnocarrinhodecompras:
public class CarrinhoCompras {
//outros métodos e atributos
public void adicionarProduto(Produto p) {
produtos.add(p);
p.adicionaPropriedades(this);
}
}
181

## Página 203

8.3.DoubleDispatch-Mechama,queeutechamo! CasadoCódigo
Observequeométodo adicionarProduto()recebeumainstânciadaclasse
Produtocomoparâmetroedevolveparaessainstânciaainvocação dométodo
adicionaPropriedades(), passando-se como parâmetro. Abaixo segue o
exemplodecomoseriaaimplementação daclasse ProdutoDigital,queagora
temaresponsabilidadedeadicionarsuasresponsabilidadesnocarrinho. Observe
queométodorecebeoprópriocarrinhodecomprascomoparâmetroeadicionaas
propriedadesadequadas.Casoalgumaoutramodificaçãono CarrinhoCompras
fossenecessária,elatambémpoderiaserfeitanessemétodo.
Listagem 8.15-ExemplodetipodeprodutocomousodoDoubleDispatch:
public class ProdutoDigital extends Produto {
//atributos de um produto digital
@Override
public void adicionaPropriedades(CarrinhoCompras c) {
c.adicionaPropriedade("PRECO", getPreco());
c.adicionaPropriedade("DOWNLOAD", getTamanho());
}
}
Essaéjustamenteaideiadaestruturadopadrão Double Dispatch:aclasse
devolveachamadademétodoparaoparâmetroquerecebe. Assim,dependendo
dotipopassadocomoparâmetro,ométodoinvocadoteráumaimplementaçãodife-
rente.Observequeantesdaimplementaçãodopadrão,eranecessáriaamodificação
daclasse CarrinhoCompras,pormeiodaadiçãodeummétodooudacriaçãode
umcondicional,paradarsuporteaumnovotipodeproduto.Sendoassim,acada
novotipodeproduto,écomosetivéssemosadicionandoumnovotipodeoperação
naclasse.
EstruturadoDoubleDispatch
Se formostraduzirdeformaliteraldoinglês,onomedopadrão Double
Dispatchsignifica“despachoduplo”.Nessecontexto,apalavra“despacho”significa
adelegaçãodepartedafuncionalidadedaclasseparaoutra.Aadiçãodapalavra“ d u -
plo”,significaqueessadelegaçãoocorreduasvezes.Sendoassim,onomedopadrão
acabaressaltandosuaprincipalcaracterística,queéadaclassequerecebeachamada
dométododevolvê-laparaumobjetorecebidocomoparâmetro,oqualiráexecutar
umaoperaçãonaclassequechamouométodo.
182

## Página 204

CasadoCódigo Capítulo8. AdicionandoOperações
AFigura8.3representaaestruturadopadrão.U m acaracterísticaqueprecisaser
ressaltadaéadependênciacíclicaentreasclasses Despachantee Elemento,em
quecadaclassepossuiummétodoquerecebeaoutracomoparâmetro.A p e s a rdisso,
éimportantenotarquemesmoque Despachantedependade Elemento,elanão
dependedenenhumadesuasimplementações. Dessaforma,qualquerumadelas
podeserpassadacomoparâmetroenovasimplementações podemserfacilmente
incorporadas.
Figura8.3:EstruturabásicadoDoubleDispatch
U m avisãodinâmicadesseprocessodo Double DispatchestánaFigura8.4.
Noprimeirocaso,quandooelementoépassadocomoparâmetro,elerecebeuma
chamadadaclasse Despachanteeexecutaumaoperação nessaclasse. Nose-
gundocaso,quandoumelementodiferenteépassadocomoparâmetro,operações
diferentessãoexecutadasnaclasse Despachante.Issofazcomquesejapossível
determinaraoperaçãoaserexecutadaapartirdoparâmetropassado.
183

## Página 205

8.4. PadrãoVisitor CasadoCódigo
Figura8.4:V i s ã odinâmicadofuncionamentodoDoubleDispatch
Cadaclassediferentepassadacomoparâmetroécomosefosseummétodo
diferentesendoexecutadonaclasse Despachante. Sendoassim, o Double
Dispatchéumpadrão quepodeserutilizadoquandosedesejaacrescentarno-
vasoperações emumaclassedeformadinâmica. Paraisso,bastaimplementara
interfaceecriaranovaoperaçãonométodoqueéchamadodevoltapelaclasse.
8.4 Padrão Visitor
“ OVisitor éu mpadrão de q u evocêdificilmente precisa, mas, quando precisa,
nenhuma o u t rasolução r e s o l v eo problema. ”
–JosephYoder
184

## Página 206

CasadoCódigo Capítulo8. AdicionandoOperações
Opadrão Visitornaminhaopiniãoéumdosmaisdifíceisdesercompreen-
didoseaplicadosdoGoF[10].Emcursossobremodelagemorientadaaobjetosque
ministro,algumasvezesfizumworkshopdepadrões, emquecadaalunoapresen-
tavaumpadrão. Commuitafrequência,quemapresentavao Visitoracabavase
confundindoeentendendoerradosuaidea.Muitosdosexemplosqueencontravam
naInterneteramtão artificiaisqueacabavamilustrandosomenteaestrutura,mas
nãoamotivaçãoparaousodopadrão.
O Visitorutilizaemsuaestruturao Double Dispatch,vistonaseçãoan-
terior. Acompreensãodessepadrão certamentejáéumpassoimportanteparaa
compreensãodo Visitor.Apróximaseçãoiráapresentaroexemplodeumpro-
blemaquedificilmenteteriaumasoluçãoeficientesemautilizaçãodessepadrão.Em
seguidaserámostradocomoelefuncionaecomopoderiaserutilizadopararesolver
oproblema.
DiferentesRelações entre Padrões
A t éomomentojávimosdiversasformasderelacionamentoentrepa-
drões. Oexemplomaissimplesseriaquandodoispadrões podemser
utilizadosemconjuntoparaasoluçãodeumproblema.Outroexemplo,
seriaquandodoisoumaisfornecemsoluções alternativasparaomesmo
problema.Nocasodo Visitoredo Double Dispatchtemosum
novotipoderelação: quandoasoluçãodeumpadrãoéutilizadacomo
partedasoluçãodeoutro.
Pormaisqueissopossaparecerestranho,essetipoderelação no
mundodospadrões énatural. Existempadrões maisfundamentaise
maisgeraisquesãoutilizadosporoutrosqueresolvemproblemasmais
específicos. Nolivro“ImplementationPatterns”[2],porexemplo,são
apresentadasdiversaspráticasmaisgranularesqueacabamsendoutili-
zadasdentrodospadrões apresentadosnesselivro.Éimportanteressal-
tarqueaindaexistemváriasoutrasformasderelacionamentoentreeles
[18],alémdasapresentadasnesselivro.
VáriosRelatóriosemDiversosFormatos
Oexemplodessaseçãoiráutilizarcomocontextoumsoftwarequeprecisagerar
diversostiposderelatórioemdiversosformatos.Emrelaçãoaostiposderelatório,
185

## Página 207

8.4. PadrãoVisitor CasadoCódigo
cadaumpossuiinformações eumalógicademontagemdiferente.Podemosterum
quesumarizaascomprasdeumclienteeoutroquemostraasvendasmensaisde
umdeterminadoproduto.Outrasvezes,amesmainformaçãopodeserexibidade
formasdiferentes,comocomgráficosoucomtabelas.Sendoassim,apesardosele-
mentosdeumrelatórioseremosmesmos,comotexto,tabelas,títulosegráficos,suas
informações esuaestruturasãodiferentes.
Emrelaçãoaoformatoemqueorelatórioserágerado,tambémexistemvárias
possibilidades. Exemplosdeformatosquepodemsernecessáriossão emHTML
paravisualizaçãoembrowsers,emPDFparapermitirumamelhorleituraeimpres-
são,planilhaparapermitirumamanipulaçãoposteriordosdadoseatémesmoem
XMLparaqueorelatóriopossaserinterpretadoeexibidoporoutrasaplicações.
Paraageração emcadaumdosformatos,umaAPIdiferenteprecisaserutilizada
pelaaplicação,comooiTextparaPDFeoJakartaPOIparaplanilhas.Sendoassim,
mesmoqueoselementosdosrelatóriossejamosmesmos,ageraçãodecadaumdeles
emcadaplataformaécompletamentediferente.
AFigura8.5ilustraarelação demuitosparamuitosentrerelatórioseosfor-
matos.Comocadaumpossuiinformações diferentes,ficadifícilreutilizarocódigo
degeraçãodeumparaoutro.Adicionalmente,comocadaAPIcriaoselementosde
formadiferente,tambémnãoépossívelreutilizarocódigodegeraçãoparadiferentes
formatosdentrodomesmorelatório.
186

## Página 208

CasadoCódigo Capítulo8. AdicionandoOperações
Figura8.5:Relacionamentoentreostiposderelatórioeostiposdesaída
Comoessareutilizaçãodecódigonãoédireta,asoluçãocomumnessecasoseria
cadaumdosrelatóriospossuirummétodoparaageraçãoemcadaformato,como
mostradonaFigura8.6. Dessaforma,acadanovorelatório,precisariasercriado
ummétodoparaasuageraçãoemcadaumdosformatos.Seumnovoformatofosse
introduzido,issotambémdemandariaacriaçãodeumnovométodoemcadaclasse
derelatório.
187

## Página 209

8.4. PadrãoVisitor CasadoCódigo
Figura8.6:Estruturadasoluçãodoproblemadorelatóriosemousodepadrões
Oproblemanãopáranaintroduçãodenovoselementos,mastambémaparece
namanutençãodosformatoserelatóriosjáexistentes.Imagine,porexemplo,que
comoumnovorequisitodousuáriosejanecessárioaadiçãodologodaempresano
iníciodosrelatóriosemPDF.Issovaidemandarumaatualizaçãoemtodasasclasses
derelatório.Poroutrolado,sefossenecessáriaaintroduçãodeumanovainformação
norelatório,todososmétodosprecisariamseratualizados.
IntroduzindooVisitor
Paracomeçaraexplicaro Visitor,vouutilizarumametáforaqueilustrabem
comoopadrãofunciona.Imaginequeexistamduaspintoras,MariaEduardaeAna
Beatriz,sendoqueaprimeirapossuiumestilodepinturamaisclássicoeasegunda
umestilomaiscubista.Consideretambémqueelasvãovisitardoislocaisdiferentes,
sendoumdelesumafavelaeooutroumacasanocampo.Quandoforemnafavela,
serápedidoaelas "pinte essa favela”equandoforemacasadecamposerápedido
"pinte essa casa de campo”.
188

## Página 210

CasadoCódigo Capítulo8. AdicionandoOperações
AFigura8.7apresentacomofoioresultadodasvisitasdaspintorasaoslocais.
A p e s a rdopedidofeitoaelasaovisitaremumlocalseromesmo,oresultadodo
pedido,nocasooquadro,serátotalmentediferente.Comocadapintorapossuium
estilodiferente,aexecuçãodomesmopedidoserádistinta.Sendoassim,oresultado
finaldependetantodolocalqueestásendovisitado,quantodapintoraqueoestá
visitando.
Figura8.7:V i s i t adepintorasdiferentesemlocaisdiferentes
O Visitorfuncionadeformaanálogaaoexemplodaspintoras.Quandoesse
189

## Página 211

8.4. PadrãoVisitor CasadoCódigo
padrão éutilizado,existeumahierarquiadeclassesquerepresentaosvisitantese
umaoutraquerepresentaelementosqueaceitamvisitantes.Quandoumelemento
recebeumvisitante,solicitaumatarefaaele,passando-secomoparâmetrooupas-
sandoalgumainformaçãoquepossuiinternamente.Assim,cadaclassequeimple-
mentaaabstraçãodevisitanteirárealizaressatarefadeummododiferenteecada
implementaçãodeumelementoirásolicitaralgodiferenteaosvisitantes.
A estrutura do Visitor estáapresentada na Figura 8.8. A interface
Visitantedefinequaismétodosdevemserimplementadospelosvisitantes. De
formacomplementar,ainterface Elementodefineummétodoparaaceitaruma
visita.Dessemodo,duranteela,cadaimplementaçãode Elementoiráchamarum
métodode Visitantediferente.Demaneiraanálogaaoexemplodaspintoras,o
resultadodependetantodoelementovisitadoquantodovisitante.Écomosecada
implementaçãode Visitantefosseumanovaoperaçãosendoadicionadaparao
conjuntodeclassesqueimplementam Elemento.
Figura8.8:EstruturadopadrãoVisitor
Arepresentaçãoclássicado VisitorécomoaapresentadanaFigura8.8,na
qualainterface Visitantepossuiummétodoparacadaimplementaçãodainter-
190

## Página 212

CasadoCódigo Capítulo8. AdicionandoOperações
face Elemento.Assimficabemclaroqualmétodoumadeterminadaimplemen-
taçãoiráchamar;porém,paracadanovaimplementaçãode Elemento,umnovo
métodoprecisariaseradicionadoemcadaumdosvisitantes.Dessaforma,ficaria
fáciladicionarumnovovisitantemasnãoumnovoelemento.
A p e s a rdo Visitorserfrequentementeretratadocomessaestrutura,nemsem-
preosmétodosdefinidosnainterface Visitanteprecisamrefletirasimplemen-
tações de Elemento. Essesmétodospodemdefinirasoperações quepodemser
feitasporumvisitanteeoquevaidiferenciarcadaelementoseráasequênciaque
irãochamareosparâmetrosqueirãopassarparacadamétodo.Napróximaseção,o
exemplodageraçãoderelatóriosemdiferentesformatosiráutilizaressaabordagem.
OdiagramadesequênciadaFigura8.9mostracomoumclienteinvocariauma
operaçãoapartirdo Visitor.Inicialmenteoclientecriariaainstânciadaimple-
mentaçãodesejadadainterface Visitanteeapassariacomoparâmetroparaomé-
todo aceitar()deum Elemento.Dentrodessemétodo,ométodovisitar()
do Visitanteseriainvocadopassandoaprópriaclasseouinformações comopa-
râmetro.Essemétodoporsuavez,invocariamétodosnaclassepassadacomopa-
râmetro. Poressediagramadesequênciaficabemclaroautilização do Double
Dispatchcomopartedasoluçãodo Visitor.
Figura8.9:SequênciadeinvocaçãoemumVisitor
191

## Página 213

8.4. PadrãoVisitor CasadoCódigo
Aprincipaldiferençaentreo Visitoreo Double Dispatchestánahie-
rarquiadoselementos.No Double Dispatch,operações podemseradicionadas
atravésdapassagemdeumaimplementaçãodiferentecomoparâmetro.Aflexibili-
dadeestánométododotipodoparâmetroparaoqualédelegadaaexecução.Jáno
Visitor,existetambémdiversaspossibilidadesdeimplementaçãoparaaclasseque
aceitaoparâmetro.Dessaforma,cadaimplementaçãopodeinvocarmétodosdife-
rentesnoobjetorecebidocomoargumento.
FazendoosFormatosdeSaídaVisitaremosRelatórios
Depoisdevercomofuncionao Visitor,estaseçãoapresentacomoelepode
serutilizadonoproblemadageraçãoderelatóriosemdiversosformatos.Dentrodo
contextodopadrão,orelatóriorepresentaráoelemento,eoformatodorelatórioserá
ovisitante.Quandoométododegeraçãodorelatórioforchamadopassandoovisi-
tantecomoparâmetro,osseusmétodosserãochamadoscomosdadosdorelatório,
deformaacriarasuaestrutura.
Alistagemaseguirapresentaainterfacequedefineosmétodosqueumvisitante
deveimplementar. Observequecadamétodorepresentaumaseção dorelatório,
comaexceção de getResultado() queéutilizadonofinalpararetornaro
resultadodageração. Dessaforma,cadaimplementaçãodevecriarumalógicaque
crieaseçãodorelatórioadequada.Porexemplo,enquantoumrelatórioirágerarum
títulodentrodeumdocumentoPDF,ooutroirácriarastagsparaarepresentação
dotítuloemumapáginaHTML.
Listagem 8.16- Interfaceimplementadapelas classes que representamum for-
matodearquivo:
public interface FormatoVisitante{
public void visitarTitulo(String t);
public void visitarSubtitulo(String t);
public void visitarParagrafo(String p);
public void visitarTabela();
public void visitarTabelaCabecalho(String... ct);
public void visitarTabelaLinha(Object... o);
public void visitarTabelaFim();
public void visitarImagem(String path);
public Object getResultado();
}
192

## Página 214

CasadoCódigo Capítulo8. AdicionandoOperações
Conformealistagemaseguir,ainterface Relatorio, aoinvésdepossuir
diversosmétodoscomonasoluçãorepresentadanaFigura8.6,agorapossuiapenas
ummétodochamado gerarRelatorio(). Essemétodorecebeumaclassedo
tipo FormatoVisitantecomoparâmetro,queéquemirádeterminaroformato
degeraçãodorelatório.Enquantoasoluçãoanteriorpossuíaummétodoparacada
formato,nessecaso,cadatipode FormatoVisitantepassadocomoparâmetro
podeserutilizadocomoadefiniçãodeumanovaoperaçãonessaclasse.
Listagem 8.17-Interfaceimplementadapelosrelatórios:
public interface Relatorio{
public Object gerarRelatorio(FormatoVisitante fv);
}
Parailustrarageração deumrelatório,alistagemaseguirmostracomoseria
criadoumrelatórioquelistasseascomprasdeumcliente.Observequeacriaçãodas
seções dorelatório,comotítulo,parágrafoetabela,sedáapartirdachamadados
métodosdoobjetodotipo FormatoVisitantepassadocomoparâmetro.Dessa
forma, cadarelatóriodiferenteiriachamaressesmétodosnaordemnecessária,
passandoseusdadoscomoparâmetro.Nessecaso,nãoexisteummétodoespecífico
paracadatipoderelatório.
Listagem 8.18-Implementaçãodageraçãodeumrelatório:
public class ComprasCliente implements Relatorio {
private Cliente c;
private List<Item> items;
//outros métodos
public Object gerarRelatorio(FormatoVisitante fv) {
fv.visitarTitulo("Compras de "+c.getNome());
fv.visitarParagrafo("CPF "+ c.getCPF());
fv.visitarParagrafo("Cliente desde "+ c.getDataCadastro());
fv.visitarTabela();
fv.visitarTabelaCabecalho("Produto", "Data", "Valor");
for(Item i : items) {
fv.visitarTabelaLinha(i.getProduto(),
i.getDataCompra(), i.getValor());
}
193

## Página 215

8.4. PadrãoVisitor CasadoCódigo
fv.visitarTabelaFim();
return fv.getResultado();
}
}
Ainda exemplificandoa implementação das interfaces, a listagem a seguir
mostracomoseriaumaimplementação de FormatoVisitanteparaageração
derelatóriosemHTML.Avariávelsb,dotipo StringBuilder,éutilizadapara
guardarorelatórioentreaschamadasdemétodo.Dessaforma,acadachamadade
método,umanovapartedorelatórioéadicionadaao StringBuilder.Deforma
similar,outrasimplementações armazenariamorelatórioqueestariasendogerado
emumavariável,eiriamagregandoasseções aeleamedidaqueosmétodosfossem
chamados.
Listagem 8.19-ImplementaçãodoformatoHTMLpararelatórios:
public class VisitanteHTML implements FormatoVisitante {
private StringBuilder sb = new StringBuilder();
public void visitarTitulo(String t){
sb.append("<h1>"+t+"</h1>");
}
public void visitarSubtitulo(String t){
sb.append("<h2>"+t+"</h2>");
}
public void visitarParagrafo(String p){
sb.append("<p>"+t+"</p>");
}
public void visitarTabela(){
sb.append("<table>");
}
public void visitarTabelaCabecalho(String... ct){
sb.append("<tr>");
for(String s : ct)
sb.append("<th>"+s+"</th>");
sb.append("</tr>");
}
public void visitarTabelaLinha(Object... obs){
sb.append("<tr>");
for(Object o : obs)
sb.append("<td>"+o.toString()+"</td>");
194

## Página 216

CasadoCódigo Capítulo8. AdicionandoOperações
sb.append("</tr>");
}
public void visitarTabelaFim(){
sb.append("</table>");
}
public void visitarImagem(String path){
sb.append("<img src='"+path+"'>");
}
public Object getResultado(){
return sb.toString();
}
}
Parafinalizaroexemplo,alistagemaseguirapresentaocódigoqueseriausado
paraageração deumrelatório. Inicialmenteaclassedorelatórioedoformato
precisariamsercriadas. Dealgumaformaasinformações seriamrecuperadas,
estandoissoforadoescopodoexemplo. Eentão paraasuageração, bastariaa
chamadadométodo gerarRelatorio()passandoaimplementaçãodovisitante
comoparâmetro.
Listagem 8.20-Códigoclienteparaageraçãoderelatórios:
Relatorio r = new ComprasCliente();
//carrega dados no relatório
FormatoVisitante fv = new VisitanteHTML();
String resultado = (String) r.gerarRelatorio(fv);
Essasoluçãopermitequenovosrelatóriossejamfacilmenteadicionados,nãoim-
portandooformatodegeração,equenovosformatossejamadicionados,jáfuncio-
nandoparatodososrelatórios.Agrandedificuldadedemanutençãodo Visitor
ocorrequandoénecessáriaainserçãodeumnovométodonainterfacedaclassevi-
sitante.Nessecaso,issoaconteceriasefossenecessáriaageraçãodeumnovotipo
deseçãoparaosrelatórios.Adificuldadeocorreriadevidoaofatodesernecessária
acriaçãodeumnovométodoqueprecisariaseradicionadoemtodasasimplemen-
tações.
195

## Página 217

8.5.Considerações FinaisdoCapítulo CasadoCódigo
Elementos Compostos noVisitor
U mpadrão que se encaixa muito bem com o Visitor éo
Composite. Nessecaso,oelementoquerecebeovisitanteseriacom-
postoporoutroselementosquetambémpodem receberovisitante.
Nessecaso,oelementocompostopoderiarealizarchamadasprópriasno
visitanteedelegarpartedaexecuçãoparaoselementosqueocompõe,
passandoovisitanteparaqueelesrealizemasprópriaschamadas.
Dentrodoexemplodosrelatórios,umdelespoderiasercomposto
poroutros. Dessaforma,umapartequefosserecorrente,poderiaser
modeladacomoumrelatórioàparteeutilizadaparacomporoutrosre-
latórios.Sendoassim,ométodoqueaceitaumvisitante,alémdeserim-
plementadopeloelementoprincipal,tambémpodeserimplementado
pelasclassesqueocompõem.
8.5 Considerações Finaisd oCapítulo
Essecapítuloabordouumproblemaimportanteparaodesenvolvimentodeaplica-
ções, queéaadição deoperações deformadinâmica. Emalgunscasos,aadição
deoperações emobjetosfazpartedopróprionegócioeaestruturadosistemapre-
cisapermitirasuaevolução nessesentido,semquesejanecessáriaamodificação
frequentedasclassesenvolvidas.
Oprimeiropadrãoapresentadonessecapítulofoio Command.Eleconsisteno
encapsulamentodeumaoperação comoumaclasse,emvezdesuarepresentação
atravésdeummétodo.Apartirdessaestrutura,épossívelcomporasclassesdina-
micamentecomcomandos,tornandopossívelaadiçãodenovasoperações. Outra
possibilidadetrazidaporessepadrão édearmazenaroscomandosjáexecutados,
dessaformapode-seutilizá-losparaaimplementação detransações eauditoria,e
atémesmoguardá-losparaquepossamserdesfeitos.
Outrospadrõesparaaadiçãodeoperaçõesvistosnessecapítuloforamo Double
Dispatcheo Visitor.Essesdoisutilizamorecursodedelegaraexecução,ou
partedela,paraoobjetopassadocomoparâmetro.Dessaforma,ocomportamento
édeterminadopeloparâmetropassado,possibilitandoaadiçãodenovasoperações
apartirdacriação denovasabstrações dotipodoparâmetro. Particularmenteo
Visitoréumpadrãocomplicadoedifícildeserimplementado,porémnassitua-
196

## Página 218

CasadoCódigo Capítulo8. AdicionandoOperações
ções emqueeleéaplicável,osganhosnasuautilizaçãoemtermosdereúsoemanu-
tençãopodemserimensos.
197

## Página 220

Capítulo9
GerenciandoMuitosObjetos
“Ninguémédono da multidão, a i n d aq u ecreia tê-ladominada. ”
–EugeneIonesco
Existemhojesoftwaresimensos,commilhões delinhasdecódigo! Algumas
vezesperguntoàspessoasseelassabemcomoalguémconseguetrabalharemuma
basedecódigocommilharesdeclassesemilhões delinhasdecódigo.Quandoeu
façoisso,algunscoçamacabeçaetentamimaginarquetipodementeconsegue
visualizar,abstrairetrabalharcomtamanhaquantidadedeinformações. Averdade
éque,seosoftwareforbemmodelado,ninguémprecisaconhecertudo,somentea
parteemqueestátrabalhandoeassuasinterfacescomoresto.
Porém,mesmoutilizandoospadrões quevimosatéagora,aquantidadedeim-
plementações podeaumentarmuito. Issopodeacontecerprincipalmentequando
temos classes granulares, ou quando padrões como Command, Strategy e
Observersãoutilizados.Nessespadrões,sãodefinidasinterfacesquenormalmente
definemapenasummétodo,quepodeacabarpossuindomuitasimplementações pe-
quenas.Paraosclientesdessasclasses,anecessidadedeconhecimentodetodasas

## Página 221

9.1.CriandoumaFachadaparasuasClasses CasadoCódigo
classescomqueelepodeinteragirpodesetornarumverdadeiropesadelo.
Ospadrões queserãoapresentadosnessecapítulofocamemsimplificaretornar
escalávelorelacionamentoentreumagrandequantidadedeclasseseobjetosdosis-
tema.Aideiaprincipalésimplificarainterfaceentreasclasses,tornandomaisfácil
ainteraçãoentreelas.Outrasvezesoproblemanãoestáexatamentenaquantidade
declasses,masnaquantidadedeobjetosqueéinstanciada.Oúltimopadrãodesse
capítulomostracomoépossíveldiminuirecontrolaressaquantidadedeobjetos,
otimizandoamemóriadispendidacomeles.
9.1 Criando u m aFachada para suasClasses
“ Aignorância éu m aespéciede bênção.”
–JohnLennon
Émuitocomumqueumadeterminadafuncionalidadedeumsistemaresulte
dacolaboração dediversoscomponentes. Porexemplo,aoseconcluirumacom-
praemumsistemadee-commerce,podesernecessáriointeragircomcomponentes
responsáveispeloestoque,pelocontrolefinanceiroepeloempacotamentoeenvio
demercadorias. Responsabilizaroclientedessesserviçosporinteragircomessas
classesdeformacorretapodecausarproblemas.Seexistiremdoistiposdecliente,
porexemplomobileeweb,essamesmalógicaprecisaráserreplicadanosdois.Isso
dificultamudançanessalógicaeacoplaoclienteadiversoscomponentes.
Quandoospadrõessãoutilizadosnacriaçãodeumasolução,muitasvezesdiver-
sasclassesauxiliaresvãocolaborar.Porexemplo,asclassespodemserencapsuladas
comum Proxy,podemsercompostasporoutrasclasses,oumesmoreceberum
Visitorcomoparâmetro.T e roconhecimentodequaisclassesdevemsercriadas
einseridasnacomposiçãomuitasvezesécomplicadoparaosclientes.Issonãoape-
nasosacoplaaimplementações específicas,comotambémàestruturadasolução
adotada,dificultandopossíveisrefatorações futuras.
Emoutraspalavras,ograndeproblemaaquiécomplexidadeeacoplamento!Não
édesejávelqueosclientesdasclassesprecisemconhecertodosseusdetalhesestru-
turaisouseacoplaradiversasimplementações. Opadrão Facade(pronuncia-se
"façade”porserumapalavradeorigemfrancesa)propõe acriação deumaclasse
intermediáriaqueservecomoumafachadaparaqueoclientepossaacessarasfun-
cionalidadesdesejadas.Essaclasseencapsulaacomplexidadedainteraçãoentreos
diversoscomponentesedesacoplaoclientedasimplementações.
200

## Página 222

CasadoCódigo Capítulo9. GerenciandoMuitosObjetos
EstruturadoFacade
Aestruturado FacadeébemsimpleseestárepresentadanaFigura9.1.Deve
sercriadaumaclasse,apresentadanafiguracomo Fachada,querecebeaschama-
dasdosclientesedelegaparaasclassesapropriadasdeumsubsistema. Pormais
quepareçaqueo Facadeéumsimplesredirecionadordechamadas,elepodeter
importantesresponsabilidadesrelativasàcoordenação eorquestração dessascha-
madas.Dessaforma,asclassesclientesirãointeragirapenascomafachada,queos
isoladacomplexidadedasclassesdosubsistema.
Figura9.1:EstruturadoFacade
Diversospadrões vistosnesselivrodeixamaestruturadeclassesmaisbemorga-
nizada,maisflexíveleprontaparaevoluir.Porémissotemumcustodecomplexidade
comqueosclientesprecisamlidaraocriaremetrabalharemcomessaestruturade
classes. Pormaisqueospadrões decriação vistosnoscapítulos6e7sejamutili-
zados,osclientesaindaprecisamconfigurarasdependênciasouasfábricas.Nesse
contexto,o Facadeencapsulaessacomplexidadeeforneceummétodosimplesque
provêaosclientesafuncionalidadedesejada.
Apartirdessepadrãoépossívelisolarumconjuntodeclassesdorestodaaplica-
ção,deixandoafachadacomooúnicopontodecontato.Comessaestruturadefine-
seumsubsistemaquepodeevoluirdeformaindependenteeinclusiveserreutilizado
emoutroscontextos.Comessaestruturamodularizadaépossívelparticionaraar-
201

## Página 223

9.1.CriandoumaFachadaparasuasClasses CasadoCódigo
quiteturadeumaaplicação,organizandooscomponentesetornandoamanutenção
maissimples.
IsolandoAPIsExternas eFrameworks
QuandoutilizamosumaAPIexternaouumframework,elesprecisam
seradaptadosàsnecessidadesdaaplicação.Porseremmaisgeraisecom
objetivodeatenderumgrandenúmerodeaplicações, aquantidadede
configurações queprecisamserfeitasedeclassescomasquaisprecisa-se
interagirpodesermaiordoqueonecessárioparaasnecessidadesdasua
aplicação.Dessaforma,um Facadepodesercriadoparaisolarautiliza-
çãodessaAPIouframework,provendoparaaaplicaçãoapenasmétodos
namedidadassuasnecessidades.IssodesacoplaaaplicaçãodaAPIutili-
zadaetornamaissimplesainteraçãocomaquelasfuncionalidadespara
orestosistema.
Imagine,porexemplo,umaaplicaçãoquepreciseacessarumcartão
comcertificadodigitalparaexecutarsuasfuncionalidades.AAPIquein-
teragecomasfuncionalidadesdecriptografiaépreparadaparalidarcom
diferentestiposdecartãoealgoritmoscriptográficos.Porém,aaplicação
geralmentenãoprecisadetodaessaflexibilidade,poisotipodecartão
queelairáutilizarjáestápré-estabelecido,assimcomooalgoritmocrip-
tográfico.Dessaforma,utilizandoum Facadeparaproverosserviços
necessáriosparaorestodaaplicação,alémdepermitirquedesenvolve-
dorespossamutilizarafuncionalidadesemconheceraAPI,facilita-sea
manutençãocasoalgumamudançasejanecessárianessaparte.
Deumacertaforma,aestruturado Facadesepareceumpoucocomado
Adapter. U m adasdiferençaséqueo Facadeinteragecomdiversasclassesen-
quantoo Adapternormalmenteencapsulaapenasumaclasse,apesardeissonão
serumaregraobrigatória.Outradiferençaéqueo Adapternormalmenteadapta
paraumainterfaceconhecida,queoclientejáutilizaporserimplementadaporou-
trasclasses,eo Facadedefineumnovoconjuntodemétodoscomoobjetivode
simplificarainteração.
RefatorandoparaoFacade
Anecessidadedo Facademuitasvezesnãoépercebidanoiníciodoprojeto.
202

## Página 224

CasadoCódigo Capítulo9. GerenciandoMuitosObjetos
Issoocorreporqueasinterações entreasclassescomeçamdeformasimpleseobje-
tiva,mascomaevoluçãodoprojetoacabamseespalhandoparadiversasclassese
utilizandodiversasclassesemétodos.Dessaforma,quandoocódigodaaplicação
começaaseentrelaçardemaiscomodeumsubsistemaeissopassaadificultara
manutenção,éhoradecriarum Facadeparaisolarumapartedaoutra.
OpassobásicodessarefatoraçãoésimpleseestáilustradonaFigura9.2.Opri-
meiropassodarefatoraçãoéidentificaropontonaclasseclientequefazacessoaos
subsistemaseextrairummétodocomessalógica. Aprincípioessemétodofica
naprópriaclasse,masosegundopassodarefatoração éjustamentemovê-lopara
o Facade. Dessaforma,oacessoaosubsistemaficaráconcentradonafachada,
isolando-osdasclassesclientes.Pormaisquepossaparecersimples,esseprocedi-
mentoprecisaserrepetidoparatodosospontosemqueosubsistemaéacessado.
203

## Página 225

9.1.CriandoumaFachadaparasuasClasses CasadoCódigo
Figura9.2:RefatorandoparaaCriaçãodeumFacade
À medidaqueocódigoforsendomovidoparaafachada,podesernecessário
refatoraressecódigo,queaprincípioestavadistribuídoentreasclasses,eagoraestá
204

## Página 226

CasadoCódigo Capítulo9. GerenciandoMuitosObjetos
concentradoemapenasuma. Porexemplo,podeserquedoismétodosmovidos
paraessaclassepossuamumcódigomuitoparecido.Nessecaso,podeserquevalha
apenaintroduzirumparâmetroeunirosmétodos,ouextrairummétodoauxi-
liarcomumutilizadopelosdois.Adificuldadedarefatoraçãoparaacriaçãodeum
Facadevaidependerdequantoocódigodeacessoaosubsistemaestáespalhado.
Paraessatarefa,valeapenautilizaralgumaferramentaquedetecteasdependên-
ciasentreasclasses,paraquepossamserlocalizadosospontosquedependemdo
subsistemaqueestásendoisolado.
CriandoumaFachadaparaoGeradordeArquivos
Oexemplodocomponentegeradordearquivoséumcasonoqualforamcri-
adasdiversasclassesparasolucionaroproblemadegerarumarquivoapartirde
ummapadepropriedades. Parautilizarasolução éprecisosaberasubclassede
GeradorArquivocorretaparadefinirotipodearquivoecompô-lacorretamente
comospós-processadores. Éclaroquecomapenasdoistiposdecada,não étão
difícilassimdeconhecerasimplementações, porémconformeonúmerodeimple-
mentações aumentasse,essecomponentepoderiaficardifícildeutilizar.
U mexemplodecomopoderiasercriadauma Facadeparaogeradordearqui-
vosestáapresentadonalistagemaseguir.Cadamétodotemumobjetivobemespe-
cíficodescritopeloseunomee,apartirdafachada,asfuncionalidadesdogerador
dearquivopodemserinvocadasdiretamente,semanecessidadedeconfigurações
edacriaçãodeclassesadicionais.Noexemplo,foramcriadosmétodosparaagera-
çãodascombinações entreosformatosdearquivoeostiposdepós-processamento,
sendoqueocasodopós-processadorcompostonãofoiincluído.Dentrodocontexto
deumaaplicação,seriamincluídosno Facadesomenteosmétodosquerealmente
fossemserutilizadosporela.
Listagem 9.1-Exemplodefachadaparageradordearquivos:
public class GeradorArquivoFacade{
public void gerarXMLCompactado(
String nome, Map<String,Object> propriedades){
GeradorArquivo g = new GeradorXML();
g.setProcessador(new Compactador());
g.gerarArquivo(nome, propriedades);
}
public void gerarPropriedadesCompactado(
205

## Página 227

9.1.CriandoumaFachadaparasuasClasses CasadoCódigo
String nome, Map<String,Object> propriedades){
GeradorArquivo g = new GeradorPropriedades();
g.setProcessador(new Compactador());
g.gerarArquivo(nome, propriedades);
}
public void gerarXMLCriptografado(
String nome, Map<String,Object> propriedades){
GeradorArquivo g = new GeradorXML();
g.setProcessador(new Criptografador());
g.gerarArquivo(nome, propriedades);
}
public void gerarPropriedadesCriptografado(
String nome, Map<String,Object> propriedades){
GeradorArquivo g = new GeradorPropriedades();
g.setProcessador(new Criptografador());
g.gerarArquivo(nome, propriedades);
}
//outros métodos
}
Aideiadesecriarumafachadaparaencapsularoacessoaumconjuntodeclasses
nãoésubstituiraAPIoriginal,mastornarmaissimplesoacessoàsfuncionalidades.
Nocasodogeradordearquivos,asclassesoriginaiscontinuamexistindoepermi-
tindotodotipodeextensãoqueerapossívelanteriormente.Dessaforma,apenaso
acessoàsfuncionalidadesfoisimplificado,nãoprejudicandodeformaalgumaaes-
truturaeaflexibilidadejáexistente.Aideiadafachadanãoéfornecermétodospara
cadapossibilidadedasclasses,masforneceraquelasnecessáriaspelaaplicação.
206

## Página 228

CasadoCódigo Capítulo9. GerenciandoMuitosObjetos
DefinindoComponentes Plugáveis
O Facadeéumpadrãoimportanteparaadefiniçãodecomponen-
tes.Afachadadefinidaéainterfaceexternadocomponente,queprovê
serviçosparaaaplicação atravésdacoordenação dainvocação desuas
classesencapsuladas. Adefinição deumainterfacecomoabstração da
fachadapermitequeexistamdiversasimplementações paraaquelecom-
ponente. Seessapráticaforcombinadacompadrões como Dynamic
Factory, Dependency Injectionou Service Locator,épos-
sívelqueocomponentepossaserinstanciadodinamicamente.Essaéa
baseparaadefiniçãodeumaarquiteturaconstruídacomcomponentes
plugáveis,naqualcadaumdelespodesersubstituídoenovoscompo-
nentespodemserfacilmenteadicionados.
9.2 SeparandoCódigoNo v odeCódigoLegado
“Deixai-os crescer j u n t o sa t éa colheita, e, no t e mp oda colheita, direi aos ceifeiros:
ajuntai primeiro o joio, atai-o em feixes para ser queimado; mas o tr ig o,recolhei-o no
meu celeiro.”
–Mateus13:30
EmseulivrosobreDomain-drivenDesign[11],EricEvansapresentaumpadrão
chamado Anti-Corruption Layer.Essepadrãoéaplicávelemcenáriosondeé
necessárioacessarcódigolegado,ondenãonecessariamenteomodelodeobjetosé
bemconstruídoecompatívelcomodanovaaplicação.Essecódigolegadopodeser
umsistemacompleto,umcomponenteouatémesmoumconjuntodeclasses.U m
dosriscosnessecasoédeomodeloantigo“contaminar”anovaaplicação, aqual
tentaseadaptaraoparadigmaeàmodelagemdocódigoantigo.Poroutrolado,essa
integraçãomuitasvezeséimportante,poispodeproporcionarreaproveitamentode
códigoegerarumgrandevalorparaocliente.
O Anti-Corruption Layerpropõe acriaçãodeumacamadaentreanova
aplicaçãoeocódigolegado.Elaéresponsávelportraduziraschamadasfeitaspela
aplicaçãoeminvocações paraclassesdosistemalegado.Apartirdessanovacamada,
épossívelabstrairaexistênciadocódigolegadodorestodaaplicação,oferecendoos
serviçosdeformaconsistentecomomodeloeamodelagemdanovaaplicação.
207

## Página 229

9.3.MediandoaInteraçãoentreObjetos CasadoCódigo
Naimplementaçãodessepadrão,o Facadeénormalmenteutilizadoparaforne-
cerosserviçosnecessáriosdocódigolegado,encapsulandotodoacessoaele.Dentro
dessafachadapodesernecessáriautilizaçãodeclassesresponsáveisportraduziras
entidadesdomodelodeumdossistemaparaooutro.Issopodeocorrertantocomas
classesdanovaaplicaçãoqueserãorecebidascomoparâmetroquantocomasclasses
retornadaspelosistemalegado.
Atradução entreduasclassesépossívelquandooimportanteforemosdados
queelacarrega. Porém,quandoaclasseretornadapossuirmétodosqueprecisam
serinvocados,não fazsentidoduplicá-losnaclassedonovosistema. Nessecaso,
podeserutilizadoum Adapterqueencapsulaumaclasselegadaparauminterface
utilizadapelonovosistema.Dessaforma,existiráummétodonoadaptadorqueirá
fazerosajustesnecessáriosparadelegarafuncionalidadeparaométododaclasse
legada.
9.3 Mediando aInteração entre Objetos
“ C a d au mde nós escolheráo mediador q u eseleciona a informação segundo os
critériosq u epreferimos. ”
–F .SarsfieldCabral
O Facadeéumpadrãoquepodeserutilizadoparaoencapsulamentodasfun-
cionalidadesfornecidasporumsubsistema.Essasfuncionalidadessãodisponibili-
zadasatravésdeumaclasseeconsumidasporobjetosecomponentesdaaplicação.
Porém,nemsempreainteraçãoentreosobjetosdeumsoftwareaconteceemape-
nasumadireção.Osobjetospodemserelacionarcomoutrosdeformascomplexas,
inclusivedeformaahaverumacomunicaçãobidirecionalentreeles.Pormaisque
essainteraçãopossaacontecerdeformabemdefinida,podemsercriadasinterde-
pendênciasdesestruturadasedifíceisdecompreender.
U mcontextoemquealógicadeinteraçãoentrecomponentescostumasertornar
complexaéeminterfacesgráficas.Porexemplo,aescolhadeumvaloremumcombo
boxpodeserogatilhoparaorecarregamentodeumalistaeaomesmotempofazer
comquecertoscampossejamdesabilitados. Emdoiscamposondeprecisamser
entradasasenhaesuaverificação, amudançadovaloremumdoscampospode
dispararumalógicadevalidaçãoquefazacomparaçãocomooutro.Quandoum
componenteéligadodiretamentecomoutroseasinterações são complexas,fica
muitodifícilentenderedarmanutençãonessesrelacionamentos,queprecisamser
criadosumaum,emumarelaçãomuitos-para-muitos.
208

## Página 230

CasadoCódigo Capítulo9. GerenciandoMuitosObjetos
Éjustamenteparaessetipodecenárioqueo Mediatordeveserutilizado.Esse
padrãopropõe acriaçãodeumaclassequeservecomomediadoraentreosobjetos.
Dessaforma,aoinvésdosobjetosenviaremrequisições ereceberemrequisições de
váriosoutros,elairáinteragirapenascomomediador.Essaclasseseráresponsá-
velporreceberasrequisições dosobjetoseenviá-lasparaosobjetosqueasdevem
receber.
AumentandooNúmerodeObservadoreseObservados
Paraexemplificarautilização dessepadrão, vamosretomaroexemploapre-
sentado no Capítulo3 para o padrão Observer. Nesse exemplo, a classe
CarteiraAcoesrepresentaumacarteiradeações quepodepossuirobservadores,
sendoqueométodo addObservador()éutilizadoparaaadição deumobser-
vador. Cadaobservadoréumaclassequeimplementaainterface Observador,
querecebeumachamadanométodo mudancaQuantidade()quandoações são
adicionadasouremovidasdacarteira.
Dentrodessecenário,ascoisaspodemsecomplicarquandoonúmerodecartei-
rasedeobservadorespudersergrande.Porexemplo,sehouverdezcarteirasdeações
aseremobservadaspordezdiferentesobservadoresemumdeterminadocontexto,
serãonecessáriasceminvocaçõesdemétodoparaadicionarcadaumdosobservado-
resemcadaumadascarteiras.Essaligaçãodiretaentreosobjetospodetornardifícil
ogerenciamentodequaisobservadoresestãorecebendoeventosdequaiscarteiras.
A utilização de um Mediator éuma alternativapara gerenciara relação
entreosobservadoreseascarteirasdeação. Aclasse GrupoObservacao,cuja
listagemestáapresentadaaseguir,éumamediadoraquerepresentaumgrupode
carteirasquepodemserobservadasporumgrupodeobservadores.Paracumprir
esseobjetivo,essaclasseimplementaainterface Observadoreseadicionacomo
observadora em todas as carteirasadicionadasa ela. Alémdisso, ela também
recebeobservadores,osquaissãoadicionadosemumalistamantidainternamente.
Assim,quandoalgumadascarteirasnotificaromediadordealgumevento,esseserá
repassadoatodososobservadores.
Listagem 9.2-Mediadorparainteração entreacarteiradeações eseusobser-
vadores:
public class GrupoObservacao implements Observador {
private List<Observador> obs = new ArrayList<>();
209

## Página 231

9.3.MediandoaInteraçãoentreObjetos CasadoCódigo
public void mudancaQuantidade(String acao, Integer qtd) {
for(Observador o: obs)
o.mudancaQuantidade(acao, qtd);
}
public void addObservador(Observador o) {
obs.add(o);
}
public void addCarteira(CarteiraAcoes ca) {
ca.addObservador(this);
}
}
Cadaobservadorseráadicionadoapenasnaclasse GrupoObservacao,quese
encarregaráderepassaroseventosgeradosportodasascarteiras.Deformasimilar,
cadacarteiratambémteráapenasumobservador,queseráomediador.Portanto,
essaclasseagecomointermediáriaparaacomunicaçãoentreessesobjetos.
Oexemploapresentadomostraumcasosimplesde Mediator,porémimagine
queessecenáriosecompliqueumpoucomais.Considere,porexemplo,quedeter-
minadosobservadoresestejaminteressadosapenasemeventosapartirdeumacerta
quantidadeousomentedeumgrupodeações. Essepadrãocriaumcontextodeinte-
raçãoentreosobjetosondeessetipoderegrapodeserintroduzidaemaisfacilmente
gerenciada.
EstruturadoMediator
Aestruturadopadrão Mediatorébemilustradapelametáforautilizadaem
seunome. Existeumaclassemediadoraqueservecomointermediáriaparainte-
ração entreosobjetosdaaplicação, comomostraaFigura9.3. Nessaestrutura,a
classerepresentadacomo Mediadorrecebechamadasde RealizadorChamadas
e,deacordocomalógicadeinteraçãoentreosobjetos,invocamétodosnasclasses
dotipo RecebedorChamadas.Aclasse RealizarRecebedor,representadano
diagrama,ilustraocasoemqueumamesmaclasserecebeerealizainvocações no
mediador.
210

## Página 232

CasadoCódigo Capítulo9. GerenciandoMuitosObjetos
Figura9.3:EstruturadopadrãoMediator
Osobjetosquesãoinvocadospelomediador,porprecisaremseracessíveisaele,
normalmentesão armazenadosematributosinternos. Jáasclassesqueinvocam
funcionalidadesneleprecisam,dealgumaforma,obtersuareferência.Paraisso,
podemseraplicadasasestratégiasdecriação deobjetosapresentadasemcapítu-
losanteriores.Porexemplo,sehouverapenasummediadorparatodaaaplicação,
um Singletonpodeserutilizadoparaqueasclassestenhamumaformacentrali-
zadadeacessarasuainstância.U m aoutraalternativa,seriaousode Dependency
Injection,deformaqueomediadorseriainjetadonasclassesqueprecisassemse
comunicarcomele.
U mdosprincipaisbenefíciosdessepadrãoéodesacoplamentoentreasclasses
queprecisamrealizarumachamadaeasquedevemtratá-las.Comoomediadoré
colocadoentreasclasses,emnenhummomentoexisteumacessodiretoentreelas.
O Mediatorcentralizaogerenciamentodorelacionamentoentreobjetos,oque
simplificaatrocadasinstânciaseaadiçãodenovasnocontextodeinteração. Em
outraspalavras,casoumnovoobjetopreciseinteragircomoutros,emvezdeleser
ligadoacadaobjeto,elesóprecisaestarligadoaomediador.
O Mediatoréindicadoquandoasrelações entreosobjetosforemcomplexas
211

## Página 233

9.3.MediandoaInteraçãoentreObjetos CasadoCódigo
osuficiente,deformaavalerapenaqueessaresponsabilidadesejaconcentradaem
umaclasse.U mdosmotivosparaessacomplexidadeseriaumagrandequantidade
deobjetos,osquaisprecisariamestarligadosunsaosoutros.Outromotivoseriam
regrasparaessainteraçãoentreosobjetos,comocondições paraqueumdetermi-
nadoobjetorecebaumachamada.Comousodessepadrão,essasregrasmigrariam
dasclassesparaomediador.Porexemplo,aoinvésdeumaclassefiltrarcomquais
objetoseladeveinteragirouquaischamadaseladevetratar,essaresponsabilidade
seriamovidaparaomediador.Éimportanteressaltarqueapesardeasrelações tra-
tadaspelomediadorseremcomplexas,elasprecisamseguirregrasbemdefinidas.
Opassobásicoparaarefatoraçãodeadiçãodeummediadoremumconjunto
declassesnãoémuitodiferentedoapresentadonaFigura9.2,paraaadiçãodeum
Facade.Alógicadeinteraçãoentreosobjetosprecisariairsendoextraídaemmé-
todos,osquaisseriammovidosparaomediadoremseguida.Porém,àmedidaque
novasinterações fossemsendoadicionadas,omediadorprecisariairincorporando
asnovasregras,semeliminarasantigas.U m apráticaquefacilitaessatransiçãosão
osmediadoresimplementaremasabstrações dasclassesquerecebemaschamadas,
poisassimelepoderáserinvocadodeformatransparentepelasclassesjáexistentes.
Issofoifeitonoexemplodaclasse GrupoObservacao,queimplementouainter-
face Observadorparapoderserfacilmenteadicionadanaclasse CarteiraAcoes
jáexistente.
LançandoEventosnoSpring
U m aformainteressantedeseutilizarum Mediatoréatravésdeeventos.T o d a s
asrequisições sãopassadasparaomediadornaformadeumevento,oqualétratado
pelasclassesinteressadasnaqueletipodeevento.OframeworkSpring,apresentado
noCapítulo7paraousodeinjeção dedependências,possuiumafuncionalidade
quepermiteolançamentoeotratamentodeeventospelasclassesdeclaradasnoseu
contexto.
Essaseçãoiráapresentarcomooexemplodacarteiradeações seriaimplemen-
tadoutilizandooSpringcomomediador.Aprimeiraclassequeprecisaserdefinidaé
aquerepresentaoeventoqueserálançado.Essaclasseprecisaconterasinformações
queaclassequecriaoeventodesejacomunicarparaaqueoreceberá.Alistagema
seguirapresentaaclasse MovAcao,querepresentaumeventodemovimentaçãode
umaação.Essaclasseprecisaestenderaclasse ApplicationEvent,definidapelo
próprioSpring.
212

## Página 234

CasadoCódigo Capítulo9. GerenciandoMuitosObjetos
Listagem 9.3-Definiçãodeumnovotipodeevento:
public class MovAcao extends ApplicationEvent {
private String acao;
private Integer qtd
public MovAcao(String acao, Integer qtd) {
this.acao = acao;
this.qtd = qtd;
}
public String getAcao() {
return acao;
}
public Integer getQtd() {
return qtd;
}
}
EmseguidaéprecisodefiniraclassequeirágeraroseventosenotificaroSpring.
Noexemploapresentado,esseseriaocasodaclasse CarteiraAcoes,apresentada
nalistagemaseguir,quedevegerarum MovAcaotodavezqueaquantidadede
umaaçãoforalteradaatravésdométodo adicionaAcoes().Paraqueelapossa
gerarumevento,elaprecisareceberdoSpringumainjeçãodedependênciasdeuma
instânciade ApplicationEventPublisher,cujométodo publish()deveser
chamadoacadageraçãodeevento.Nessecaso,oframeworkutilizaaestratégiade
Dependency Injectionpormeiodeinterfaces,naqualaclasseprecisaimple-
mentarainterface ApplicationEventPublisherAwareparareceberadepen-
dêncianométodosetterdefinidoporela.
Listagem 9.4-ClassequepublicaoseventosnoSpring:
public class CarteiraAcoes implements ApplicationEventPublisherAware {
private Map<String,Integer> acoes = new HashMap<>();
private ApplicationEventPublisher publicador;
public void
setApplicationEventPublisher(ApplicationEventPublisher p) {
this.publicador = p;
}
213

## Página 235

9.3.MediandoaInteraçãoentreObjetos CasadoCódigo
public void adicionaAcoes(String acao, Integer qtd) {
if(acoes.containsKey(acao)){
qtd += acoes.get(acao);
}
acoes.put(acao, qtd);
MovAcao evento = new MovAcao(acao,qtd)
publicador.publishEvent(evento)
}
}
Aclassequeestiverinteressadaemumeventodeveimplementarainterface
ApplicationListener, comotipogenéricoigualàclassedoeventoquese
desejareceber. Dessaforma,todavezqueumeventodaqueletipoforlançado,o
Springiráinvocarométodo onApplicationEvent()naquelaclasse.Alistagem
aseguirmostraoexemplodaclasse AcoesLogger queescrevenoconsoleas
informações dasinstânciasde MovAcaorecebidas.
Listagem 9.5-ClassequerecebeoseventosdotipoMovAcaodoSpring:
public class AcoesLogger implements ApplicationListener<MovAcao>{
public void onApplicationEvent(MovAcao evento) {
System.out.println("Alterada a quantidade da ação "
+ evento.getAcao() + " para " + evento.getQtd());
}
}
ParajuntarospedaçosecolocaroSpringcomomediadordasclasses,épreciso
criarumarquivodeconfiguraçãocomadefiniçãodessasclasses.Noexemplo,esse
arquivosechama beans.xmleseuconteúdoestáapresentadonalistagemaseguir.
Listagem 9.6-Arquivobeans.xmlparaconfiguraçãodosbeansdoSpring:
<?xml version="1.0" encoding="UTF-8"?>
<beans ...>
<bean id="carteira" class="br.com.casadocodigo.CarteiraAcoes"/>
<bean id="logger" class="br.com.casadocodigo.AcoesLogger"/>
</beans>
Finalmente,parailustrarcomoessecódigoseriautilizado,apróximalistagem
mostraumtrechodecódigoqueutilizaasclassescriadas.Nessecódigoécriadoum
214

## Página 236

CasadoCódigo Capítulo9. GerenciandoMuitosObjetos
contextodoSpringatravésdoarquivoXMLapresentadoeemseguidaainstância
daclasse CarteiraAcoesérecuperada.Quandoométodo adicionaAcoes()
éinvocado,oeventoserágeradoerecebidopelaclasse AcoesLogger.
Listagem 9.7- Código que cria o contextoda aplicação e provocageração de
eventos:
ConfigurableApplicationContext contexto =
new ClassPathXmlApplicationContext("beans.xml");
CarteiraAcoes c = (CarteiraAcoes) contexto.getBean("carteira");
c.adicionaAcoes("ABC", 300);
c.adicionaAcoes("XYPLZ", 700);
Essaabordagembaseadaemeventoséumaformainteressantedeimplementa-
çãodemediadores.OseventossãolançadospelasclassesparaoSpringsemqueelas
saibamqueoutrasclassesseinteressamporeles.Damesmaforma,oseventossão
tratadosporclassesquenãotêmconhecimentodeondeforamoriginados. Essaé
umaformadedesacoplaroscomponentesdeumsistema,semimpedirqueelesse
comuniquemcomosoutros.
9.4 ReaproveitandoInstâncias co mFlyweight
“ Um ac l a s s edeve ser i m u t á v e la não ser q u et e n h au m aboa r a z ã opara fazê-la
m u t á v e l .”
–JoshuaBloch
Asseções anterioresabordarampadrões que visam simplificaro relaciona-
mentoeacomunicação entreasclassesdeumsistema. T a n t oo Facadequanto
o Mediatorsimplificamasinterfaces,tornandoaestruturadosoftwaremaismo-
dular.Diferentemente,o Flyweightatacacenáriosondeexisteacriaçãodemui-
tosobjetosdeumamesmaclasse,quemuitasvezesacabamsendosemelhantes.A
soluçãodessepadrãoconsistenoreaproveitamentodamesmainstânciapararepre-
sentaçãodeobjetossemelhantes,sendoqueoqueirádiferenciá-laéocontextono
qualelaseráinserida.
OclássicoexemplodessepadrãoutilizadonoGoF[10]éodeumeditordetexto
queprecisarepresentarasletrasdeumdocumento.Secadaletradodocumentofosse
representadaporumobjetodiferente,aquantidadedeobjetosseriamuitogrande.
Imagine,porexemplo,quantasvezesaletra“ a ”apareceemumtexto. Utilizando
215

## Página 237

9.4. ReaproveitandoInstânciascomFlyweight CasadoCódigo
o Flyweight,cadaletraseriarepresentadaporapenasumainstância,queseria
utilizadasemprequeelafossenecessária.Oquediferenciaria,porexemplo,asdi-
ferentesletras“ a ”dotexto,seriamolocaleocontextoemqueestariaminseridas.
Dessaforma,propriedadesquepossamvariar,comootamanhoetipodafonte,não
seriampropriedadesdaletraesimdotrechodetextoemqueestariainserida.
Pormaisqueesseexemplodoeditordetextosejabemilustrativoparaoenten-
dimentodopadrão, acreditoquemuitopoucosdesenvolvedoresnosdiasdehoje
trabalhemcomeditoresdetexto.Adicionalmente,arepresentaçãodecaracteresem
Stringsetextoéumproblemajábemresolvidopelasbibliotecasnativasdelingua-
gensdeprogramaçãomaismodernas,comooJava.Entãoseráqueessepadrãoainda
éaplicávelemsistemasatuais?Emqueoutroscenárioselepoderiaserutilizado?É
justamentesobreissoquesetrataessaseção!
StatusdeIten sdeumPedidoemumSistemadeE-commerce
Imaginequeemumsistemadee-commercesejanecessáriocontrolarostatus
decadaitemdeumpedido.Cadaitemdacompraécompostocomumainstância
daclasse StatusItemapresentadanalistagemaseguir.Alémdonomedostatus,
essaclassetambémpossuialgumaspropriedadesbooleanasquesão utilizadasna
lógicadosistemaparaverificarsealgumasações podemsertomadaspelousuário.
Quandoostatusdeumiteméalterado,umanovainstânciade StatusItem
referenteaonovostatusécriadaeinseridanainstância.
Listagem 9.8-Classequerepresentaostatusdeumitemdeumacompra:
public class StatusItem {
private String nome;
private boolean podeCancelar;
private boolean compraConcluida;
public StatusItem(String nome, boolean podeCancelar,
boolean compraConcluida){
this.nome = nome;
this.podeCancelar = podeCancelar;
this.compraConcluida = compraConcluida;
}
public String getNome(){
return nome;
}
216

## Página 238

CasadoCódigo Capítulo9. GerenciandoMuitosObjetos
public boolean isCompraConcluida(){
return compraConcluida;
}
public boolean podeCancelar(){
return podeCancelar;
}
}
Aperceberqueaaplicação estavaocupandoumgrandeespaçoemmemória,
foiutilizadaumaferramentade profilingparainvestigarquaisinstânciasestavam
ocupandoamemóriadamáquinavirtual. Nessaanálise,umadassurpresasfoia
presençadeumnúmeromuitograndedeobjetosdaclasse StatusItem.Mesmo
sendoumaclassepequena,aimensaquantidadedeinstânciasocupavaumaparte
significativadamemória.Porserumaaplicaçãoemquediversosusuáriosacessam
deformasimultânea,epelofatodecadaordemdecomprapoderpossuirdiver-
sositens,onúmerode StatusItemnamemóriaemumdeterminadomomentoé
semprealto.Porém,pordiversasinstânciaspossuíremasmesmasinformações, esse
pontofoiumdosescolhidosparaotimização.
O que é u m a ferramenta de profiling?
U m aferramentade profilingéumsoftwareutilizadopordesenvolve-
doresparafazeranálisededesempenhodeaplicações. Ferramentasde
profilingparaJavanormalmenteseconectamàmáquinavirtualqueestá
executandoaaplicação ecolhemdiversasinformações, comootempo
deexecuçãodosmétodoseaquantidadedeobjetosemmemória,entre
outrascoisas.Sendoassim,épossívelsaberquemétodoestádemorando
maistempoparaexecutarouqualéaclassecujasinstânciasestãoocu-
pandomaismemória.Seemumaanálisedessasforconstatadoqueexis-
temmuitasinstânciassemelhantesdeumamesmaclassenamemória,o
Flyweightécertamenteumpadrãocandidatoparadiminuirsignifica-
tivamenteessenúmero.
ApresentandooFlyweight
O Flyweight,cujatraduçãoseriaalgocomopeso-moscaoupeso-pena,éum
padrão cujoobjetivoépermitirarepresentação deumnúmerograndedeobjetos
217

## Página 239

9.4. ReaproveitandoInstânciascomFlyweight CasadoCódigo
deformaeficiente.Eleéaplicávelemcenáriosondeexistemdiversasinstânciasda
mesmaclasseemmemóriaquesãosimilares.Dessaforma,asoluçãopropostapelo
padrãoéreutilizaramesmainstânciaemtodososlocaisondeobjetossemelhantes
precisaremserutilizados.
AFigura9.4apresentaaestruturadopadrão.Aclasseapresentadacomonome
FabricaFlyweightéresponsávelporretornarasinstânciasde Flyweightpara
asclassesclientes.Normalmenteafábricautilizaumachaveparaidentificarainstân-
ciaquedeveserretornada,quenormalmenteéumastringouumnúmeroqueiden-
tificalogicamentedentrodaaplicaçãooobjetodesejado.Afábricapodeinicializar
osobjetosdeforma“preguiçosa”,criando-osnaprimeiravezqueforemsolicitados,
armazenando-osinternamenteeretornandoamesmainstânciaemsolicitações pos-
teriores.Ou,comoalternativa,asinstânciaspodemsercriadaslogonainicialização
daprópriafábrica,oqueéindicadoquandohouverpoucasinstâncias.
Figura9.4:FuncionamentodoFlyweight
U m acaracterísticamuitoimportantedo Flyweightéqueosobjetosrepresen-
tadosporeleprecisamserimutáveis.Emoutraspalavras,depoisdecriados,oestado
internodessesobjetosnãopodesermaisalterado.Oprincipalmotivoparaissoéque
amesmainstânciaestarásendoutilizadaemdiversoscontextosdaaplicação,eseela
fordealgumaformamodificada,todososoutroscontextosserãoafetados.Maisà
frentenessemesmocapítuloserão apresentadoscuidadosquesedeveteremJava
paraacriaçãodeclassesimutáveis.
U moutracaracterísticadasclasses Flyweight,justamenteporsuaimutabi-
218

## Página 240

CasadoCódigo Capítulo9. GerenciandoMuitosObjetos
lidade,estánofatodeseusmétodosalgumasvezesdependeremdoestadoexterno
parasuaexecução.T o d ainformaçãoqueprecisarseralteradaouquefordependente
doestadodaexecuçãonãopodeserarmazenadadentrodo Flyweight.Porisso
mesmo,seessaclasseprecisarexecutaralgumalógicaquedependedocontextoonde
está,asinformações precisamserpassadascomoparâmetro.NaFigura9.4,essetipo
demétodoestárepresentadopelométodo executar()naclasse Flyweight.
Aprincipalconsequênciadessepadrãoéaeconomiadememóriaquesepodeter
comareutilizaçãodeinstânciasemdiversospontosdaaplicação.Emaplicações que
tratamrequisições dediversosusuáriosdeformasimultânea,comoemaplicações
W e b ,essepadrãopodeterumgrandeimpactoparaarepresentaçãodeobjetosmuito
utilizados.Amelhoradedesempenhotambémpodeterimpactoemprocessamento,
vistoquediversasinstânciasnãoprecisarãomaissercriadas,eposteriormenteco-
letadaspeloGarbageCollector.Alémdisso,seaaplicação realmentegarantirque
existeapenasumainstânciaparacadatipodeobjetodaquelaclasse,ascomparações
entreelespodemserfeitasutilizandoooperador“==” ,queémuitomaiseficiente
queométodo equals().
CompartilhandoasInstânciasqueRepresentamoStatus
V o l t a n d oao problema apresentado anteriormente, as instâncias da classe
StatusItemsão boascandidatasàimplementação dopadrão Flyweight. Isso
porquesãoobjetosimutáveisnocontextodaaplicação,ouseja,umitemirámudar
destatus,masnãoirámodificarasinformações deumdeterminadostatus.Issoper-
mitequeasinstânciasdessaclassepossamsercompartilhadaspordiversosobjetos.
Ofatodehaverumnúmeromuitograndedeinstânciassimilaresdessaclassena
aplicaçãotambémmotivaaimplementaçãodopadrão.
Oprimeiropassoparaimplementá-loéacriaçãodeumafábricaresponsávelpela
criaçãoeretornodosobjetos.Nocasofoicriadaaclasse FabricaStatusItem,
representadanalistagemaseguir.Nessecontexto,devehaverapenasumainstância
dessafábricaparaqueosobjetosde StatusItemsejamarmazenadosemapenas
umlocal. Paraisso,essaclasseimplementaopadrão Singleton,armazenando
a instânciano atributoestático instance e retornando-oatravésdo método
getInstance().
Listagem 9.9-FábricaparaobtençãodasinstânciasdeStatusItem:
public class FabricaStatusItem {
private static FabricaStatusItem instance =
219

## Página 241

9.4. ReaproveitandoInstânciascomFlyweight CasadoCódigo
new FabricaStatusItem();
public static FabricaStatusItem getInstance() {
return instance;
}
private Map<String,StatusItem> mapa;
private FabricaStatusItem(){
mapa = new HashMap<>();
mapa.put("CARRINHO", new StatusItem(
"CARRINHO", true, false));
mapa.put("FECHADO", new StatusItem(
"FECHADO", true, false));
mapa.put("PAGO", new StatusItem(
"PAGO", true, true));
mapa.put("ENVIADO", new StatusItem(
"ENVIADO", false, true));
mapa.put("ENTREGUE", new StatusItem(
"ENTREGUE", false, true));
}
public StatusItem get(String nome){
if(!mapa.containsKey(nome))
throw new RuntimeException("Status inexistente:"+nome);
return mapa.get(nome);
}
}
Aclasse FabricaStatusItemcriatodosos StatusItemnoconstrutoreos
armazenaemumamapa.Essaéumaestratégiaválidapoisonúmerodeobjetosé
pequeno.Outrapossibilidadeseriaircriandoosobjetosàmedidaqueforemsoli-
citados.Essecasoéinteressante,porexemplo,quandoosobjetossãoarmazenados
emumabasededados. Assimsomenteosobjetosquerealmenteforemutilizados
serãomantidosemmemória.
Alémda criação da fábrica,épreciso substituir os locais onde a classe
StatusIteméinstanciadapelainvocaçãodafábrica.U m aformadeajudaradetec-
taressespontosédeclararoconstrutordaclassecomomodificardeacesso default,
ecolocarsomenteafábricanomesmopacotequeele.Issogeraráumerrodecom-
pilaçãoemtodasasclassesforadessepacotequetentaremutilizá-lo.
220

## Página 242

CasadoCódigo Capítulo9. GerenciandoMuitosObjetos
CuidadosparaCriarObjetosImutáveiseÚnicos
Criarclassesquegeramobjetosimutáveispodenãoseralgotãotrivialquanto
seimagina. Principalmenteemlinguagensorientadasaobjetosemqueasclasses
podemserestendidasecomportamentospodemsersobrepostos.Naimplementa-
ção do Flyweightéimportantetercertezadequeasinstânciascompartilhadas
realmentenãopermitemmodificação,poisissopoderiaresultaremumproblema
críticoedifícildedetectar.Abaixoestãoalgumasdiretivasaseremseguidasparaa
implementaçãodeclassesimutáveis:
•Nãoadicionemétodossetterououtrosmétodosquemodifiquemosatributos
daclasse.Issoiráimpedirqueexternamenteosclientesdoobjetoomodifi-
quem.
•Crietodososatributoscomo privatee final.Issoiráimpedirqueelesse-
jaminacessíveisasubclassesequepossamsermodificadosapósasuaprimeira
atribuiçãodevalor.
•Impeçaacriaçãodesubclasses.Issopodeserfeitodeformadiretadeclarandoa
classecomo final.Outraalternativaédeclararoconstrutorcomo private
eutilizarum Static Factory Methodparaacriaçãodasinstâncias.Issoé
importanteparaimpedirquesubclassesadicionemnovascaracterísticasmu-
táveis.
•Nãoretornediretamenteatributoscomobjetosmutáveis.Emoutraspalavras,
sevocêretornarumobjetomutávelarmazenadoemumatributo,elepoderá
sermodificadopelosclientes,mesmoestandodefinidocomo final. Caso
sejamesmonecessárioretorná-lo,crieumacópiaeoretorne.
•Cuidadoaoreceberobjetosmutáveisnaconstruçãodoobjeto,poiselespodem
sermodificadospelosclientesposteriormente,mesmonãosendoretornados
pelaclasse.Oquerecomenda-senessecasoéacriaçãodeumacópiadoobjeto
mutávelrecebidoparaoarmazenamentoemumatributodoobjetoimutável.
Analisandoaclasse StatusItemapresentadaanteriormente,épossívelobser-
varqueelanãoseguetodasasrecomendações paraacriaçãodeobjetosimutáveis.
A p e s a rdenãopossuirmétodossetterparamodificações noobjeto,osatributosnão
possuemomodificador finaleaclassepodeserestendida. Alistagemaseguir
mostraaclasse StatusItemmodificadasegundoasrecomendações paraobjetos
221

## Página 243

9.4. ReaproveitandoInstânciascomFlyweight CasadoCódigo
imutáveis.Observequeoconstrutorfoidefinidocomoprivadoefoidefinidoum
Static Factory Methodparaimpedirquesejamdefinidassubclasses. Como
nenhumdosatributosdessaclasseémutável,não foiprecisosepreocuparcomo
retornoecomorecebimentodelescomoparâmetro.
Listagem 9.10-T o r n a n d oaclasseStatusItemimutável:
public class StatusItem {
private final String nome;
private final boolean podeCancelar;
private final boolean compraConcluida;
static void StatusItem criar(String nome,
boolean podeCancelar, boolean compraConcluida) {
return new StatusItem(nome, podeCancelar, compraConcluida);
}
private StatusItem(String nome, boolean podeCancelar,
boolean compraConcluida) {
this.nome = nome;
this.podeCancelar = podeCancelar;
this.compraConcluida = compraConcluida;
}
//métodos de acesso as propriedades
}
U moutrocuidadoqueéprecisoterseriaemrelaçãoàunicidadedosobjetosdo
Flyweight.Alémdaexistênciadafábrica,éprecisotercertezadequeelaestásendo
invocadaemtodososlocaisondeoobjetoécriado.Naclasse StatusItemdessa
seção,o Static Factory Methodchamado criar()édefinidocomomodifi-
cadordeacesso defaultparaquesomenteafábrica,localizadanomesmopacoteque
ele,possautilizá-lo.
Porém,somente isso pode não ser suficientepara garantir essa unicidade.
U mcasoqueprecisadeumtratamentoespecialéquandoaclassequecontémo
Flyweightprecisaserserializada.Normalmenteissoocorrequandoelaéenviada
remotamentecomoparâmetroouquandoépersistidaemumarquivo.Nessecaso,
nomomentodadesserialização umanovainstânciado Flyweightserácriada.
Nessescasos,éprecisosobreporomecanismodeserializaçãodaclassequecontém
ainstânciado Flyweightparaqueelasejarecuperadadafábricaquandofordes-
222

## Página 244

CasadoCódigo Capítulo9. GerenciandoMuitosObjetos
serializada.
Paraexemplificaressecaso,seráconsideradaaclasse Itemqueécomposta
pelaclasse StatusItem,enoexemploprecisaserserializávelpoiséenviadare-
motamentecomoparâmetroparaumEJB.Paraevitarqueumatributodotipo
StatusItemsejaincluídodeformainadequadaemumaclasseserializável,eladeve
sermantidasemaimplementaçãodainterface Serializable.Dessaforma,caso
hajaatentativadeserializá-la,mesmoquedentrodeumaoutra,ocorreráumerro.
Paraquesejapossívelserializarumaclassecompostaporum StatusItem,
énecessáriodeclararoatributocomo transientparaqueelenão sejaincluído
no algoritmo de serialização. Em seguida épreciso customizar o algoritmo
de serialização para que ele de alguma forma guarde o status do objeto e o
recupere da fábricadepois. Isso pode ser feito criando os métodosprivados
writeObject()e readObject()naclasse. Nométodo writeObject(),o
método defaultWriteObject()échamadoparaqueoalgoritmodeseriali-
zação padrão sejaexecutadoeemseguidaonomedostatus,queéutilizadopara
arecuperação dafábrica,tambéméarmazenado. Deformasimilar,nométodo
readObject(), o método defaultReadObject() échamado inicialmente
eemseguidaélidaastringcomonomedostatus. Essastringéutilizadapara
recuperaro StatusItemdafábricaeoatribuiraoatributodaclasse.
Listagem 9.11-SobrepondoomecanismodeserializaçãodaclasseItem:
public class Item implements Serializable {
private transient StatusItem status;
//outras propriedades
//métodos getters e setters omitidos
private void writeObject(ObjectOutputStream oos)
throws IOException {
oos.defaultWriteObject();
oos.writeObject(status.getNome());
}
private void readObject(ObjectInputStream ois)
throws ClassNotFoundException, IOException {
ois.defaultReadObject();
String status = ois.readObject().toString();
this.status = FabricaStatusItem.getInstance().get(status);
}
223

## Página 245

9.4. ReaproveitandoInstânciascomFlyweight CasadoCódigo
}
O código da listagem a seguir pode ser utilizado para testar se o me-
canismo de serialização estáfuncionando corretamente. O métodochamado
copiarPorSerializacao()criaumacópiadoobjetoapartirdesuaserializa-
çãoedesserialização.Dessaforma,épossívelcriarumobjetodaclasse Item,criar
umacópiaeemseguidaverificarseainstânciaconfiguradanavariáveltransiente,
quenocasorepresentao Flyweight,éamesma.
Listagem 9.12-SobrepondoomecanismodeserializaçãodaclasseItem:
public class TesteSerialização {
public static void main(String[] args) throws Exception {
Item i1 = new Item();
i1.setProduto("Livro Design Patterns");
i1.setStatus(FabricaStatusItem.getInstance().get("PAGO"));
//seta outras propriedades
Item i2 = (Item) copiarPorSerializacao(i1);
if(i1.getStatus()==i2.getStatus()){
System.out.println("Mesma instância!");
}
}
public static Serializable copiarPorSerializacao(Serializable obj)
throws Exception {
ObjectOutputStream output = null;
ObjectInputStream input = null;
try {
ByteArrayOutputStream byteOutput =
new ByteArrayOutputStream();
output = new ObjectOutputStream(byteOutput);
output.writeObject(obj);
output.flush();
byte[] byteArray = byteOutput.toByteArray();
ByteArrayInputStream byteInput =
new ByteArrayInputStream(byteArray);
input = new ObjectInputStream(byteInput);
return (Serializable) input.readObject();
} finally {
output.close();
input.close();
}
224

## Página 246

CasadoCódigo Capítulo9. GerenciandoMuitosObjetos
}
}
Omesmocuidadoquesetemcomaserializaçãodoobjeto,tambémépreciso
tercomqualquertipodepersistência.Seasuaaplicação utilizaJPA,porexem-
plo,seaclasse Itemforpersistente,deve-setomarcuidadoparaqueinstâncias
de StatusItemnão sejamcriadasdeformaautomáticapeloframeworkdeper-
sistência.Asoluçãoparaesseproblemaésimilaràapresentadaparaaserialização.
Oatributodevesermarcadocomaanotação @Transientemétodoscomanota-
ções dotipo @PrePersiste @PostLoaddevemsercriadospararespectivamente
persistirachaveemumoutroatributoerecuperaroobjetodafábricadepoisdo
carregamentodosdadosnoobjeto.
Co m o oFlyweight éUsadoParaStrings emJa v a
Aclasse StringemJavaéumobjetoimutável.Todososméto-
dosquemodificamumastring,comoparaconcatenaçãoouextraçãode
substring,retornamumanovainstânciade Stringenãomodificama
original.Dessaforma,acadeiadecaracteresutilizadainternamentepela
Stringpodesercompartilhadapordiversasinstânciasdessaclasse.Isso
ficabemclaroemmétodoscomo substring(),emqueamesmaca-
deiaéutilizadananovainstânciade Stringretornada.Issoseriaum
exemplodousodo Flyweightparaaeconomiadememórianamá-
quinavirtual.
9.5 Considerações Finaisd oCapítulo
Essecapítulotratoudequestões relacionadasaogerenciamentodorelacionamento
entreosobjetosdeumaaplicação.Paraentenderumaclasse,éprecisoentendernão
apenasseuselementos,mastambémasinterfacescomasclassescomqueserelaci-
ona.Quandoonúmerodeclassesaumenta,éessencialqueelassejamorganizadas
equesebusquesimplificarainterfaceentreelas. Quandoonúmerodeinstâncias
émuitogrande,éimportantegerenciarorelacionamentoentreelasparaqueseja
possívelentenderoestadodosistemaemumdeterminadomomento.
Opadrão Facadefoiapresentadocomoumaformadedividiraaplicaçãoem
subsistemas.Elecriaumainterfaceúnicaquecoordenaainvocaçãodediversasclas-
225

## Página 247

9.5.Considerações FinaisdoCapítulo CasadoCódigo
sesparafornecerserviçosaorestodaaplicação.Comoconsequênciasprincipais,as
classesencapsuladasficamdesacopladasdorestodaaplicação,eainterfaceparaob-
tersuafuncionalidadeésimplificada.Deformasimilar,o Mediatorservecomo
umintermediáriopararelaçãoentreobjetosdosistema.Porcentralizaregerenciar
osrelacionamentos,omediadorretiradasclassesessaresponsabilidadequeficaes-
palhadaentreelasedesacoplaaclassequegeraumachamadademétododaclasse
quearecebe.
Emseguida,focandonadiminuiçãodonúmerodeinstânciassimilaresdeuma
mesmaclasse,o Flyweightpropõe queessasinstânciassejamreaproveitadasem
diversospontosdaaplicação.Paraisso,éprecisocriarumafábricadessesobjetos,a
qualretorneamesmainstânciaquandoforemnecessáriosobjetossimilares.T a m -
béméprecisoqueessaclassecompartilhadasejaimutável,paraquealterações rea-
lizadasemumcontextonãoafetemoutrosemqueainstânciaestiversendoreuti-
lizada. Alémdopadrão,tambémforamapresentadasquestões maisespecíficasda
linguagemJavaparaaimplementaçãodessepadrãonaprática.
226

## Página 248

Capítulo10
IndoAlémdoBásico
“ A oinfinito... E além!”
–BuzzLightyear,T o yStory
Durantetodoesselivrotrilhamosumcaminhoquenosapresentoudiversospa-
drões quepodemserutilizadosparaprojetarumsoftwareorientadoaobjetos.Cada
capítulofocouemumatécnicaouemtipodeproblema,paraosquaisalgunspadrões
foramapresentados.Nemtodosospadrões doGoF[10]forammostrados,porém,
comoconhecimentodospadrões etécnicasnesselivro,acreditoqueoleitortenha
umaboabaseparaarealizaçãoeevoluçãodoprojetodeumaaplicação.Alémdisso,
comessavisãoadquirida,ficamaissimplesacompreensãodeoutrospadrões.
Esseúltimocapítulonãoapresentanenhumpadrãonovo,porémexploradiver-
sostópicosmaisavançadoserecentesarespeitodautilizaçãodepadrões. Eleaborda,
porexemplo,suautilizaçãoparaodesenvolvimentodeframeworksecomoostipos
genéricospodemserusadosdeformaefetivanasuaimplementação. T a m b é msão
discutidasquestões arespeitodautilizaçãodepadrões comatécnicadedesenvol-
vimentoTest-DrivenDevelopmentecomoospadrões apresentadosseaplicampara

## Página 249

10.1.Frameworks CasadoCódigo
problemasmaisamplosrelacionadosàarquitetura.Finalmente,olivroeocapítulo
finalizamfalandoumpoucosobreacomunidadenacionaleinternacionaldepa-
drões.
10.1 Frameworks
“ Umfr a mewo r knão ébom pelo q u ee l efaz, mas quando pode ser u t i l i z a d opara o
q u ee l enão faz. ”
–EduardoGuerra
Nosdiasdehoje,émuitodifícilalguémdesenvolverumaaplicaçãosemautili-
zaçãodeumframework,principalmentenalinguagemJava.Elenãoapenasprovê
umreusodeseucódigo,comotambémoreúsodesuaestrutura,deseudesign.
Dessaforma,alémdepossibilitaroreaproveitamentodefuncionalidadesacelerando
oritmodedesenvolvimento,eletambémdirecionaaarquiteturadaaplicaçãoàuti-
lizaçãodeboaspráticasdecódigo.
U mframeworkpodeservistocomoumsoftwareincompletoqueprecisaser
preenchidocompartesespecíficasdeumaaplicaçãoparapoderserexecutado[22].
Imagine,porexemplo,umframeworkquefaçaoagendamentodeexecuções. So-
zinho,elenãofaznada,poisnãotemoqueseragendadosemaexistênciadeuma
aplicação. Aoserinstanciado,eleécompletadocomclassesdaaplicaçãoqueserão
invocadasporele,eentãofazsentidoasuaexecução.
U m aestruturaabstratareferenteaumdeterminadodomínioéapresentadapelo
framework.Essedomíniopodeserhorizontal,referenteaumacamadadeaplicação,
comoapresentaçãooupersistência,ouvertical,referenteaodomíniodaaplicação,
comosegurosoucomércioeletrônico. Dequalquerforma,oframeworkcapturao
conhecimentodessedomínio,identificandoosprincipaispapeisqueasclassesde-
sempenhamecomoelasserelacionam.Apartirdisso,eleprovêumestruturareuti-
lizávelquepodeserusadaparaacriaçãodeaplicações dentrodaqueledomínio.
U mframeworkpossuipontoscomfuncionalidadefixa,chamadosde fr o zen
spot s,epontoscomfuncionalidadevariável,chamadosde hotspots. Os hotspots
são pontosdeextensão disponibilizados,ondeaaplicação podeinserirpartedo
seucódigo. Os fr o zenspot ssão osqueefetivamenteprovêemafuncionalidadedo
frameworkequecoordenamaexecuçãodos hotspots. Igualmenteimportantes,os
hotspotseos fr o zenspot sformamsuaarquiteturaemconjunto.
Elepropõeumaformadereúsomuitodiferentedeumabibliotecadefunções ou
declasses.Quandoumabibliotecaéutilizada,aaplicaçãoéresponsávelporinvocar
228

## Página 250

CasadoCódigo Capítulo10.IndoAlémdoBásico
afuncionalidadedasclasses,coordenandosuaexecuçãoeusando-acomoumpasso
deseuprocessamento.Quandoumframeworkéutilizado,normalmenteéelequem
temocontrolesobreaexecuçãoeinvocaafuncionalidadedasclassesdaaplicação
empontosespecíficos.Issopermitequeaaplicaçãoreutilizeocódigoeaestrutura
doframework,especializando-oparasuasnecessidades.
U mframeworktambémédiferentedepadrões deprojeto,poisrepresentaefe-
tivamenteumaimplementação,umsoftware.Ospadrões, comojáfoiditodurante
olivro,jáexistemcomoconhecimento,comoumaideia. Porém,muitospadrões
sãoutilizadosparaviabilizaracriaçãode hot spot snaestruturadosframeworks.Os
hook methodseas hook c l a s s e s,apresentadosrespectivamentenoscapítulos2e3,
sãoexemplosdetécnicasquepodemserutilizadas.Atravésdaherança,aaplicação
podeestenderumaclassedoframeworkeinserirfuncionalidadeemummétodo.
Comcomposição,aaplicaçãopodeimplementarumainterfacedoframeworkein-
serirumaclasseparaserinvocadaemumdeterminadopontodaexecução.
Ostiposde hot spot sapresentadosnessaseçãonãosãoosúnicosquepodemser
utilizadosemframeworks.Autilizaçãodereflexãoemetadados,especialmentede-
finidoscomanotações, temsidoumapráticacadavezmaisutilizadaemframeworks
maisrecentes[9].Porémessasquestões jáestãoalémdoescopodesselivro.
Aindaexistembibliotecas?
Bibliotecadefunções éumconceitoqueveiodaprogramaçãoestruturada,onde
oreúsopermitidopeloparadigmadeprogramaçãoeramaisrestrito.Porém,ainda
existemalgumasbibliotecasdefunções emJava,porexemplo,comoasclasses Math
e Collections. Emaplicações, essabibliotecadefunções éfrequentementeco-
locadaemalgumaclasseterminadacom“Utils” .Nessaclasse,usualmentesão
incluídosmétodos,normalmenteestáticos,quesãodeusogeraldaaplicação.
U mconceitodebibliotecainseridonaprogramaçãoorientadaaobjetossãoas
bibliotecasdeclasse.Agora,emvezdetermosapenasmétodosreutilizáveis,temos
classes!U mexemplodebibliotecadeclassesmuitopopularemJavaéaCollection
API.Diferentementedosframeworks,asbibliotecassãosimplesmenteclassesreu-
tilizáveis,quenão permitemnenhumtipodeextensão. Oconceitodebiblioteca
tambéméaplicáveldentrodaestruturadeumframeworkcomoumconjuntode
classesquecompartilhadeumamesmaabstraçãoepodemserinseridasemumde
seushotspots.Porexemplo,emumframeworkdevalidaçãodeinstânciasemque
oalgoritmodevalidação deumapropriedadeéum hotspot,fariasentidoumabi-
bliotecadeclassescomostiposmaiscomumdevalidação,comoformatodestring,
229

## Página 251

10.1.Frameworks CasadoCódigo
limitesnuméricos,entreoutros.
Muitasvezes,emaplicações, utilizamosclassescomosefossempartedeuma
biblioteca, porémse olharmoscomcalma suadocumentação, veremosqueela
possui diversos hotspotspelos quais épossívelestender o seu comportamento,
caracterizando-semaiscomoumframework.Issotemavercomumpadrãocha-
madode Low Surface-to-volume Ratio[4],cujatradução donomeseria
“baixaproporção dasuperfícieparaovolume”.Essepadrão temavercomvocê
tentarproverumasériedeserviçosapartirdeumainterfaceexternacompacta.Isso
tornaoframeworkmaissimplesdeserutilizado,muitasvezesfazendoparecerque
quemestáprovendoaqueleserviçoéumasimplesclasse.O Facadeémuitasvezes
utilizadoparaseatingiresseobjetivo.
Outrofatorquefazcomquemuitasvezesosframeworkssepareçamcomsim-
plesclassesvemdofatodos hotspotsseremconfiguradospordefaultcomclasses
maiscomunsdeseremusadas.Outraalternativasãoos hotspotsseremconfigurados
atravésde Buildersquecriaeinjetaasclassesdeacordocomparâmetrosecon-
figurações. Essetipodepráticapropiciauma Gentle Learning Curve[4],ou
curvadeaprendizadosuave,poisodesenvolvedorusuáriodoframeworknãoprecisa
conhecereconfigurartodosos hotspotsparainstanciaroframework.Porém,caso
sejanecessário,elepodeiraospoucosaprendendomaissobreasuaestruturapara
alterarocomportamentoquandofornecessário.
OutrosExemplosdeFrameworks
SevocêjádesenvolveualgumaaplicaçãoemJava,muitoprovavelmentejáusou
algumframework.Muitasvezesosdesenvolvedoresacabamnãopercebendoquea
classequeestãodesenvolvendofazpartedeumcontextomaisamploeéinvocada
porumframeworkemum hotspot. Essaseção iráapresentaralgunsexemplosde
frameworkparaqueosconceitosapresentadospossamservistosapartirdeuma
perspectivamaisconcreta.
V o ucomeçarcomoexemplodeframeworksparaaplicações web,poisalémde
serumdomíniofamiliarparamuitosleitores,elespossuemum hotspotbemóbvio.O
quemudadeumarequisiçãoparaoutra?Afuncionalidadequeéexecutadaquando
arequisiçãocheganoservidor!Dessaforma,aclasseresponsávelportratarumare-
quisição,chamadade controlleremummodeloarquiteturalMVC[23],acabasendo
um hotspotnesseframework.ExemplosdeclassesdessetiposeriamServletsnaAPI
padrãoJavaEE,ActionsnoframeworkStrutseManagedBeansnoJSF.Observeque
antesdaclassedaaplicaçãoreceberocontroledarequisição,diversasoutrasfuncio-
230

## Página 252

CasadoCódigo Capítulo10.IndoAlémdoBásico
nalidadessãoexecutadaspeloframework,indodesdeatraduçãodosparâmetrosaté
controledeacesso.
U moutro exemplo interessante de framework é o Quartz (http:
//quartz-scheduler.org/) , cujo principal objetivo érealizar o agendamento de
tarefas.Épossívelperceberquepelodomíniodesseframework,suaexecuçãonão
fazsentidoforadocontextodeumaaplicação. Pormaisqueelepossuaclasses
implementadasparaasmaisvariadasopções deagendamento,semaaplicação
elenãotemoqueagendar.Dessaforma,oprincipal hotspotdoframeworksãoas
tarefascomlógicadaaplicaçãoaseremexecutadasdeacordocomoagendamento
realizado.Alistagemaseguirmostraumexemplodeumaclasseparaserexecutada.
Listagem 10.1-ExemplodeclasseusadacomohotspotdoframeworkQuartz:
public class ExcluiUsuariosInvalidos implements Job {
public void execute(JobExecutionContext context)
throws JobExecutionException{
// lógica específica da aplicação
}
}
U mexemplode frameworkum pouco diferenteéo Log4J,cujo objetivoé
fazerologdeumaaplicação. Dentrodessedomínio,oLog4Jébastanteflexível,
permitindoagravação dediversostiposdeinformações, emdiferentesformatos
eemdiferenteslocais,comonoconsole,emarquivos,embancosdedadoseaté
remotamente. Diferentementedosoutrosframeworkscitados,oLog4Jjápossui
umabibliotecadeclassesquepodemserutilizadasemseus hotspots.Dessaforma,
umaaplicação poderia utilizaroframeworksemimplementarnenhumdeseus
hotspots,porémsefornecessárioelapode,porexemplo,criarclassesparaadição
depropriedadesespecíficasnologouparaquesejarealizadoologemumlocal
diferente. Apartirdasconfigurações doLog4J,apresentadasnalistagemaseguir,
épossívelperceberqueexistemváriaspropriedadesquerecebemnomesdeclasse,
quenaverdadeestãoconfigurandoimplementaçõesparaseremusadasnos hotspots.
Listagem 10.2-ExemplodearquivodeconfiguraçãodoLog4J:
# Configura o nível de log para o logger principal como INFO.
log4j.rootLogger=INFO, Console, LogFile
# Configuração do log do console
231

## Página 253

10.1.Frameworks CasadoCódigo
log4j.appender.Console=org.apache.log4j.ConsoleAppender
log4j.appender.Console.layout=org.apache.log4j.PatternLayout
log4j.appender.Console.layout.ConversionPattern=%d{ISO8601}
[%t] %-5p %C - %m%n
# Configuração do log em arquivo
log4j.appender.LogFile=org.apache.log4j.DailyRollingFileAppender
log4j.appender.LogFile.DatePattern='.'yyyy-MM
log4j.appender.LogFile.file=/path/to/logfile.log
log4j.appender.LogFile.layout=org.apache.log4j.PatternLayout
log4j.appender.LogFile.layout.ConversionPattern=%d{ISO8601}
[%t] %-5p %C - %m%
EnxergandooGeradorArquivocomoumFramework
Oexemplodogeradordearquivoutilizadoaolongodesselivropodesercon-
sideradoumframework.Issoporqueaclasse GeradorArquivonãoapenaspode
serinvocadapelaaplicação,comotambémprovêpontosemqueessafuncionalidade
podeserestendidaeespecializadaporaplicações. AFigura10.1apresentaquaisse-
riamos hotspotseos fr o zenspot sdogeradordearquivos.Exemplosde fr o zenspot s
estãonoalgoritmodegeraçãodearquivosenacombinaçãodospós-processadores
no Composite.Jáos hot spot sseriamoformatodegeraçãodosarquivos,asformas
depós-processamentoeaprópriaordemdeexecuçãodospós-processadores.
232

## Página 254

CasadoCódigo Capítulo10.IndoAlémdoBásico
Figura10.1:Hotspotsefrozenspotsdogeradordearquivo
U m acoisaimportantedeseressaltaréquenemsempreprecisaserumaclasse
daaplicaçãoaserutilizadanolugardeum hot spot. U mframeworkpodepossuir
umabibliotecadeclassesquerepresentamimplementações maisgeraisquepodem
serutilizadaspelaaplicaçãoemumpontodeextensão.Porexemplo,nogeradorde
arquivos,o Compactadoreo Criptografadorseriamclassesmaisgeraisque
poderiamfazerpartedabibliotecadeclassesdoframework. Porém,nadaimpede
queumaaplicaçãocrieumimplementaçãoprópriaeutilizenaqueleponto.
10.2 UtilizandoTiposGenéricos co m osPadrões
“ E uapenas q u e r ocrescer criativamente e ser inspirado. E unão q u e r ofazer a l g o
genéricoo ub u r ro.”
–SiennsMiller
OstiposgenéricossãoumafuncionalidadedelinguagemintroduzidanoJava1.5.
Apartirdela,épossívelparametrizartiposparaquesejapossívelsubstituirpartesda
assinaturadeseusmétodos,comoretornoseargumentos,peloparâmetropassado
paraotipo.U mcenárioondeissoémuitoaplicáveléparacoleções. U m alista,por
exemplo,aoserinstanciadapoderecebercomoparâmetrootipoquedevearma-
zenar,deformaquemétodosderecuperação retornemaqueletipoemétodosde
inserçãoaceitemcomoparâmetroapenasaqueletipo.
233

## Página 255

10.2.UtilizandoTiposGenéricoscomosPadrões CasadoCódigo
Osuportedelinguagematiposgenéricoséumafuncionalidadequevisaprimei-
ramenteàsegurançadecódigo. Antesdeexistiremtiposgenéricos,ascoleções no
Javapodiamreceberqualquerobjeto.Oproblemaaconteciaquandoumainstância
erarecuperadaeprecisavaserconvertidaparaumdeterminadotipo.Casooobjeto
nãofossedotipoesperado,uma ClassCastExceptioneralançada.Comtipos
genéricos,alémdocódigoficarmaislimposemanecessidadedefazero cast,erros
comoessesãopegosjáemtempodecompilação.
Ostiposgenéricostambémpodemserutilizadosnadefinição deinterfaces.
Dessaforma,aclassequeimplementaressainterfacepodemanterotipogenérico
paraserdefinidonasinstânciasoujádefinirotipoutilizadonomomentodaim-
plementação. Apartirdisso,umamesmainterfacepodeserutilizadaparaimple-
mentaçãodediversasinterfacesnaqualapenasotipoemretornoseparâmetrossão
alterados.Baseadonessemodelo,outrasclassespodemutilizarotipodainterface
parametrizadoparaaceitaremapenasimplementações que,porexemplo,retorna-
remaqueletipo.
A p e s a rdospadrõesseremideiasmaisgerais,ostiposgenéricospodemsermuito
úteisparaacriação deimplementações maisflexíveiseseguras. Porexemplo,em
padrões ondeexisteacolaboração deduasclasses,pode-segarantiremtempode
compilação,apartirdocontratoentreasclasses,queapenasinstânciascomomesmo
tipogenéricopodemserelacionar.
Paraexemplificar,vamosutilizaropadrão Observer. Nessepadrão, um
observadoréaquelaclassequepossuiopapelderecebernotificações dosobjetos
queestáobservando. Comonessadefinição, oobjetopassadocomoparâmetro
nanotificação podevariar,esteacabasendoumexcelentecandidatoparaserum
parâmetrogenéricoda interfacequedefineesse contrato. A listagema seguir
apresentaainterface Observadorquedefineumparâmetrogenéricorelativoà
classedoeventoutilizadaparanotificação.
Listagem 10.3-Definiçãodeumobservadorcomtipogenérico:
public interface Observador<E>{
public void notificar(E evento);
}
Paraqueosoftwarefaçasentido,umaclassedevepoderapenasserobservada
porumaqueconsigaentenderoseventosgeradosporela.Ouseja,alguémquegera
eventosdeumaclassesópoderiaserobservadoporalguémquerecebeeventodessa
234

## Página 256

CasadoCódigo Capítulo10.IndoAlémdoBásico
classe,oudealgumadesuasabstrações. Alistagemaseguirapresentaainterface
Observavelquetambémdefineumtipogenérico.Nocaso,elaaceitanométodo
adicionaObservador(),umaclassequeimplementeainterface Observador
comotipogenéricoigualousendoumaabstraçãoaoseu.
Listagem 10.4-Restringindoosobservadorescomumtipogenérico:
public interface Observavel<E>{
public void adicionaObservador(Observador<? super E> o);
}
Alistagemaseguirmostracomoasinterfacespoderiamserimplementadase
conectadas. Suponhaumaaplicação quetrabalhecomcomprasevendasdeação,
naqualexistemeventosquerepresentamasoperações realizadas. Dentrodessa
aplicação, existeumeventomaisabstratochamado OperacaoAcao,quepossui
duasespecializações, sendoessas CompraAcaoe VendaAcao.
Listagem 10.5-Criandoeconectandoasinterfacescomtiposgenéricos:
public class ObservadorOperacao implements Observador<OperacaoAcao>{
public void notificar(OperacaoAcao evento){ ... }
}
public class ProcessadorCompra implements Observavel<CompraAcao>{
public void adicionaObservador(Observador<? super CompraAcao> o){
...
}
}
ObservadorCompra oc = new ObservadorCompra();
ProcessadorCompra pc = new ProcessadorCompra();
pc.adicionaObservador(oc);
Nessecontexto,considereumaclassechamada ObservadorCompraqueim-
plementeainterface Observercomotipogenérico CompraAcaoeumaclasse
chamada ProcessadorCompraqueimplementeainterface Observavelcom
otipogenérico CompraAcao. Nessecaso,oobservadorpoderiaserinseridona
classeobservável,poisumaclassequerecebeeventosdotipo OperacaoAcaovai
saberlidarcomumeventodotipo CompraAcao,porsersuasuperclasse.Porém,
235

## Página 257

10.3.Padrões comTest-drivenDevelopment CasadoCódigo
umaclasseque,porexemplo,implementasse Observavel<VendaAcao>nãopo-
deriaserpassadaparaaclasse ProcessadorCompra,portratarumtipodeevento
diferentedogeradoporessaclasse.
Autilizaçãodetiposgenéricosparaimplementaçãodepadrões ajudanacriação
desoluçõesquepermitemumamaiorsegurançadecódigo.Noexemploapresentado
dopadrão Observer,aprópriaestruturamontadaimpedequeumaclassenão
compatívelsejapassadacomoparâmetro.Essetipoderestriçãonãoseriaimposta
seométododainterface Observadoraceitasseum Objectcomoparâmetro.Por
outrolado,sefosseprecisorestringirotipoobservadosemusartiposgenéricos,seria
necessáriaacriaçãodeumainterfaceparacadacaso.
Ousodo Observerfoiapenasumexemploparamostrarcomoautilizaçãode
tiposgenéricospodeajudaraamarrarostiposdeumasoluçãocompadrõesparaevi-
tarinconsistências.Outrospadrões tambémpodemserutilizadosparasebeneficiar
desserecursodelinguagem[1].O Abstract Factory,porexemplo,podeutili-
zartiposgenéricosparaasseguraralgumrelacionamentoentreostiposretornadose
o Commandpodeseutilizardesserecursoparapermitirqueasclassesdeclaremno
tipooretornoresultantedesuaexecução.
10.3 Padrões co mTest-drivenDevelopment
“ T D Déu m aideia louca q u efunciona. ”
–KentBeck
OTest-drivenDevelopment,TDD,éumatécnicadedesenvolvimentoeprojeto
desoftwarenaqualostestessãocriadosantesdocódigodeprodução.Éumatécnica
quevemsetornandocadavezmaispopularnomercadoemaisatençãodaacade-
mia. Comessatécnica,asclassesvão sendodesenvolvidasincrementalmenteem
pequenosciclos,osquaisalternamentreacriaçãodeumteste,odesenvolvimento
decódigodeproduçãoparasatisfazerotesteadicionadoearefatoraçãodocódigo
criado.
Duranteacriaçãodostestes,otrabalhododesenvolvedoréfocadonadefinição
daAPIexternadaclasseedoseucomportamentoesperadodentrodecadacenário
definido.Apartirdecadatesteadicionado,atarefaaseguiréimplementarasolução
maissimplespossívelnaclassequeestásendodesenvolvida,deformaaonovotestee
osanterioresseremtodossatisfeitos.Comonessemomentooobjetivoéfazeroteste
passar,logoqueissoéatingido,segueummomentoparaserefletirsobreodesign
236

## Página 258

CasadoCódigo Capítulo10.IndoAlémdoBásico
eaclarezadocódigo.Dessaforma,antesdeseguirodesenvolvimentocomaintro-
duçãodemaisumteste,ocódigoérefatoradoeamanutençãodocomportamento
verificadacomaexecuçãodostestes.
ExistemhojemuitosdesenvolvedoresqueutilizamoTDDmaiscomoumatéc-
nicadedesenvolvimentodoqueumatécnicadeprojeto.Emoutraspalavras,eles
projetamcomoserãoasclassesecomoelasirãoserelacionar,edepoisimplemen-
tamafuncionalidadeutilizandoTDD.Quandoeleéutilizadotambémcomouma
técnicadeprojeto,amodelagemdaaplicaçãovaiacontecendodeformaevolutiva,
incluindoadefinição dascolaborações edoscontratosentreasclasses. Aseção a
seguirfalasobrecomooprojetoocorrecomTDDeopapeldospadrões nessepro-
cesso.
ProjetandocomTDDePadrões
OprojetodeumaclassecomTDDaconteceemgrandepartenadefinição do
teste.ÉnelequevocêvaiexpressaraAPIexternadaclasseecomoelaéutilizadape-
losseusclientes.Ofatodostestesseremcriadosantesfavorececertascaracterísticas
naclassequeestásendodesenvolvida,oquefavoreceasuatestabilidade.U m ades-
sascaracterísticaséacoesão,pelofatodequeémaissimplestestarumaclassecom
umaresponsabilidadebemdefinidadoqueclassesqueacumulamdiversasrespon-
sabilidades.Issoajudaemummelhorparticionamentodasclassesparaumamelhor
divisãoderesponsabilidades.
Outraquestãoqueétrabalhadaduranteostesteséodesacoplamentodaclasse
queestásendodesenvolvidadassuasdependências.A p e s a rdenão serobrigató-
rionoTDD,normalmenteutilizam-setestesdeunidadenodesenvolvimento.Isso
éfeitoparaqueotestepossafocarexclusivamentenasresponsabilidadesdaquela
classe.Paraisso,énecessárioinserirobjetosfalsos(mockobjects)naclassetestada,
esimulardiferentescomportamentosdasdependênciasparaacriaçãodoscenários
deteste.
Parapossibilitarainserçãodosmockobjects,éprecisoqueaclassepossuaum
mecanismonoqualasdependênciaspossamsersubstituídas.Alémdisso,éneces-
sárioquesejadefinidoumcontrato,normalmenteatravésdeumainterface,quefor-
malizeainteraçãoentreaclassedesenvolvidaeasdependências.Essasnecessidades
detesteresultamnautilizaçãodeumconjuntodeboaspráticasqueacabamfavore-
cendoodesigndaaplicação.
MasseráqueapenasessesprincípiosdeTDDsãosuficientesparamodelarum
software?Naverdade,ostestesservemcomoummecanismoparaexpressarodesign
237

## Página 259

10.3.Padrões comTest-drivenDevelopment CasadoCódigo
desejadoparaumaclasse,masseodesenvolvedornãosouberqualdeveserasolução
paraoproblema,autilizaçãodessatécnicaficarárestrita.Omesmoseaplicapara
amodelagemcomousodeUML,poiselaéapenasumaferramentaparaexpressar
omodelodaaplicação atravésdediagrama,edenadaadiantaseodesenvolvedor
nãosouberquaisclassesvairepresentar.Sendoassim,nãoimportaqualaformaou
técnicanaqualodesigndaaplicaçãoestásendodefinido,ospadrõessãoimportantes
paraqueodesenvolvedorpossadirecionarsuasolução.
NocasodoTDD,jánoprimeiroteste,odesenvolvedorprecisadefinircomoa
classeserácriada. Nessemomento,jápodeentraremaçãooconhecimentoares-
peitodepadrõesdecriação.Seráutilizadoumconstrutorouum Static Factory
Method?Éprecisoutilizarum Singletonparaaaplicaçãoterapenasumainstân-
ciadessaclasse?Emumsegundomomento,casooprocessodecriaçãodasclasses
forcomplexoosuficiente,pode-separtirparaacriação deum Builder,oqual
poderiaserdesenvolvidoemsuaprópriaclassedeteste.
O Dependency InjectionéumpadrãomuitoutilizadoquandoseusaTDD,
principalmentequandorealmenteprocura-seisolaraclassetestadadesuasdepen-
dências.Issoéfeitoparafacilitarasubstituiçãodadependênciapormockobjects
peloteste.Porém,comofoivistonoCapítulo7,opadrão Service Locatorpo-
deriatambémserutilizadonessassituações semprejuízoàmodularidade.
Quandoumpadrão éutilizado,normalmenteexistemmaisdeumaclasseen-
volvida,sendocadaumacomumaresponsabilidadebemdefinida.Aoseoptarpor
desenvolverumasoluçãobaseadaemumpadrãoapartirdeTDD,deve-seapartir
dostestesdirecionarainterfacedaclasseedesuasdependênciasparaousodesse
padrão.Imagineumexemploemqueopadrão Visitorestivessesendoutilizado.
Nostestesdeclassesqueimplementamainterfacevisitante,queépassadacomopa-
râmetro,seriaverificadoseaschamadasaosmétodosgerariamoefeitoesperado.
Nostestesdasclassesvisitadas,ostestesverificariamseosmétodosdoobjetovisi-
tantepassadocomoparametroseriaminvocadoscorretamente.Esseéumexemplo
noqualopadrãoescolhidointerferenaformacomoostestesseriamcriados.Mesmo
assim,ainterfacequeservecomocontratoentreessasduasclassespoderiairsendo
modeladadeformaincrementalatravésdoTDD.
ArefatoraçãotambéméumafasedociclodeTDDqueémuitoimportantepara
oprojetodosoftwarequeestásendodesenvolvido.ComonoTDDoprojetoocorre
deformaevolutivaedeacordocomasnecessidadescorrentes,areestruturaçãoda
soluçãoqueestásendoadotadaéalgofeitocomumacertafrequência.Nessecon-
texto,comonemsempreanecessidadedousodeumpadrãoacontecenaprimeira
238

## Página 260

CasadoCódigo Capítulo10.IndoAlémdoBásico
versão daclasse,énaturalqueelessejamimplementadosapartirderefatorações.
Principalmentequandoumaclassecomeçaaacumularresponsabilidadesouapa-
receumaduplicação decódigo. T e rospadrões comoumdirecionamentoparaas
refatorações, comofoimostradonodecorrerdoscapítulos,éumaexcelenteforma
dedirigirodesigndaaplicaçãoparaboassoluções deformaevolutiva.
Concluindo,pormaisqueoTDDfavoreçaacriação declassesmaiscoesase
desacopladas,issonãoéosuficienteparaoprojetodeumaaplicaçãocomoumtodo.
Nessecontexto,autilizaçãodepadrões, tantoparadirecionarostestes,quantopara
oalvoderefatorações, podeterumimpactopositivonassoluções desenvolvidas.
ExemplodeTDDusandooPadrãoObserver
Parailustrarautilizaçãodepadrões comTDD,vamosimaginaroexemplode
umaaplicação dee-commerce. Nela,aoseadicionarumprodutonocarrinhode
compras,existemdiversasfuncionalidadesquedevemseracionadas.Porexemplo,
deve-seregistraressainformaçãoparaasestatísticasdoproduto,deve-seadicionar
acategoriadoprodutonosinteressesdoclienteedeve-secriarumareservapara
umaunidadedoprodutonoestoque.Ainclusãodetodasessasfuncionalidadesno
carrinhodecompraspoderiasobrecarregaressaclasseetorná-laacopladaadiversos
subsistemas.
U mpadrãoadequadoparaessetipodeproblemaéo Observer,poisocarri-
nhodecompraspoderianotificarasclassesinteressadasemseuseventossemestar
acopladoaelas. Nessecaso,aresponsabilidadedaclassequerepresentaocarri-
nhodecomprasseriasimplesmentenotificarosobservadoresdoseventosocorridos.
Baseando-senisso,ostestesdessaclassedeveriamapenasfocarseasnotificações es-
tãosendofeitasnahoraecomasinformações corretas.
O primeiro passo seria a criação de um teste que definisse como seria a
funcionalidadedenotificação docarrinhodecompras,conformeocódigomos-
tradonapróximalistagem. Observequeéinstanciadaumaclasse,chamadade
MockObservadorparasimularaexistênciadeumobservadorduranteoteste.Esse
mockobjectéadicionadocomoumobservadornaclassetestadaeotesteverifica
se,aoadicionarumprodutonocarrinhodecompras,oobservadorénotificado
comoprodutoadicionado.
Listagem 10.6- T e s t eque define padrão Observer e verifica recebimento de
notificação:
@Test
239

## Página 261

10.3.Padrões comTest-drivenDevelopment CasadoCódigo
public void testeNotificacao(){
MockObservador mock = new MockObservador();
CarrinhoCompras cc = new CarrinhoCompras();
cc.addObservador(mock);
Produto p = new Produto("Cabo HDMI", 30.0);
cc.adicionar(p);
assertTrue(mock.recebeuNotificacao());
assertEquals(p, mock.produtoRecebido());
}
Em seguida, épreciso definir a classe MockObservador que estásendo
utilizadanoteste. Essaclassedeveimplementarainterfaceesperadapelométodo
addObservador()daclassetestada,nocaso ObservadorCarrinho. Observe
queessaclassetambémdevepossuirosmétodosutilizadosnotesteparaverifi-
cação, nocaso recebeuNotificacao()e produtoRecebido(). V e j aque
aimplementação dessaclassedevefazersentidoparaoteste,ouseja,ométodo
notificaProduto() exigido pela interface implementada deve armazenar o
resultadoparapoderserverificadonoteste.
Listagem 10.7-Mockobjectquesimulaumobservador:
public class MockObservador implements ObservadorCarrinho {
private Produto p;
@Override
public void notificaProduto(Produto p){
this.p = p;
}
public boolean recebeuNotificacao(){
return p != null;
}
public Produto produtoRecebido(){
return p;
}
}
Oqueéinteressantenotarnessecaso,équeainterfaceeosseusmétodossão
definidosnomomentoemqueestásendocriadooteste.Otesteéummecanismo
240

## Página 262

CasadoCódigo Capítulo10.IndoAlémdoBásico
queestásendoutilizadoparaadefiniçãodessecontrato,poréméapartirdopadrão
Observerqueasoluçãofoiconstruída.
Nessecaso,apósadefinição dostestesdaclasseobservada,seriamcriadasas
classesobservadoras,queimplementariamainterface ObservadorCarrinho.Se
oTDDcontinuasseaserutilizadonessedesenvolvimento,seriacriadaumanova
bateriadetestesparacadaclasse.Nessestestes,ométodo notificaProduto()
seriainvocadosimulandoumanotificaçãodeumaclassequeestásendoobservadae
verificandoocomportamentoesperadodaclasseemquestão.Quandoasclasseses-
tivessemdesenvolvidas,umtestedeintegração,envolvendoocarrinhodecompras
easclassesobservadoras,tambémpoderiasercriadoparaverificarseasfuncionali-
dadesseintegramdeformacorreta.
10.4 PossoAplicaressesPadrões n aArquitetura?
“ N ã oexistem regras na arquiteturapara u mcastelo nas nuvens. ”
–G.K.Chesterton
Muitosdospadrões apresentadosnesselivrotambémpodemseaplicaremum
contextomaisamplodeumaarquitetura.Nessecaso,emvezdeclasses,ospartici-
pantesdospadrões seriamcomponenteseatémesmosubsistemasdeumsoftware.
Comoospadrões são ideiasenão estão ligadosaimplementações específicas,os
problemaseassoluções dospadrões podemseraplicadosemumaescaladiferente.
Pegandonovamentecomoexemploopadrão Observer,damesmaformaque
umaclassepodeprecisarrecebernotificações deoutra,umsubsistemapodeprecisar
receberatualizações deoutrossubsistemasremotos.Enquantodentrodeumsoft-
wareorientadoaobjetososcontratossão firmadosapartirdeinterfaceseclasses
abstratas,entresistemasremotossãoutilizadosprotocolosdecomunicação.Asolu-
çãocertamenteprecisadeumaadaptação,mascertamenteamesmaideiapodeser
usada.
Porém,autilizaçãodessespadrões deveserfeitacommuitocuidado,poisapesar
dassoluções seremsimilares,asconsequênciasdeseuusopodemserbemdiferen-
tes.Porexemplo,emumaarquitetura,quandolidamoscomsubsistemasqueestão
distribuídosemumarede,sempredevemosconsiderarapossibilidadedeumdos
nósenvolvidosfalhar.Issoéalgoquenãoprecisamosconsiderarquandoestamosli-
dandocomclassesimplantadasemumamesmamáquinavirtual.Essaéapenasuma
dasquestões quedevemserconsideradas;existemoutras,comoatolerânciaaesse
241

## Página 263

10.4.PossoAplicaressesPadrões naArquitetura? CasadoCódigo
tipodefalha,questões dedesempenhoemrelaçãoàformacomoéfeitaacomunica-
ção,entreoutras.
Paraexemplificaressaquestão,considereopadrão Proxy.Comofoivisto,ele
podeserutilizadoparaprotegeroacessoaumdeterminadoobjeto.Normalmente,
quandoissoéfeito,éadicionadaumafuncionalidadenesseacesso,como,porexem-
plo,algumaverificaçãodesegurançaouvalidaçãodosdados.Dessaforma,o Proxy
ficaentreoclienteeaclassequeestásendoacessada.
Deformasimilar,o Proxytambémpodeseraplicadodeformamaisabstrata
aarquiteturas.Nessacaso,eleiráficarcomointermediárioentredoissubsistemas.
Eleirádisponibilizarosmesmosserviçoseutilizaromesmoprotocoloqueosubsis-
temaoriginal,paraquesejatransparenteparaoclienteasuaexistência.Emoutras
palavras,oclientedeveacessaro Proxycomoseestivesseacessandoosubsistema
original.AFigura10.2mostraarepresentaçãodessepadrãoimplementadonocon-
textodeumaarquitetura. Nessecaso, Proxytambémpoderiaadicionaralguma
funcionalidadenesseacesso,comodesegurançaouregistrodeauditoria,damesma
formaqueopadrãooriginal.
Figura10.2:EstruturadeumProxyparaCriaçãodeArquitetura
Porém,comofoidito,ousodo Proxyemumaarquiteturapodeterconsequên-
ciasdiferentesdeseuusocomobjetos.Porexemplo,sehouveralgumproblemacom
amáquinaondeestivero Proxy,oclienteperderáacessoaoserviço,mesmoeste
estandoemfuncionamento.Issoadicionaumnovopossívelpontodefalhanaarqui-
tetura,oqueéumaconsequêncianegativaemrelaçãoàimplementaçãocomobjetos.
242

## Página 264

CasadoCódigo Capítulo10.IndoAlémdoBásico
Poroutrolado,o Proxytambémpodeserresponsávelpeloroteamentodasmen-
sagensentreoclienteeoservidor,permitindoqueoservidormudesualocalização
semafetarosclientes,oqueseriaumanovaconsequênciapositiva.
Muitasvezes,écomplicadosepararoqueéumasoluçãodedesigndoqueéuma
soluçãoarquitetural.Oimportanteénãoutilizarassoluções dospadrões cegamente
esempreconsiderarasconsequênciasantesdasuautilização. Lembre-sequeexis-
temsoluções alternativasquepodemresolveroproblemadeumaformadiferente,
gerandoumoutroconjuntodeconsequências.Trabalharcomarquiteturaésaber
fazertrocas,porexemplo,sacrificandodesempenhoparaaumentarasegurança,e
escolherassoluções deformaaatenderosrequisitosnão-funcionaisdosistema.
10.5 Comunidade dePadrões
“Fundamentala qualquer disciplina relacionada a ciênciao uengenharia éu m a
vocabuláriopara expressar seus conceitos, e u m alinguagem para os relacionar
j u n t o s .”
–BradAppleton
A p ó sleresselivro,vocêpodeseperguntar:Comosurgemnovospadrões? Onde
euencontronovospadrões? Comoeufaçoparatrabalharcomisso? OHillside
Groupéumaorganizaçãointernacionalsemfinslucrativoscujoobjetivoéfomentar
adocumentação depadrões paraasmaisdiferentesáreas,principalmenteasrela-
cionadasaodesenvolvimentodesoftware.Dessaforma,elaauxilianaorganização
dediversasconferênciasfocadasempadrões aoredordomundoeajudaautoresa
amadureceremseuspadrões parasuapublicação,sejaemformatodeartigosoude
livros.
Asconferênciasdepadrões, conhecidascomoPLoP(PatternLanguagesofPro-
gram),acontecemaoredordomundoerecebemsubmissõesdeartigoscompadrões,
linguagensdepadrões, ourelativosautilizaçãodepadrões. Aconferênciaprincipal
acontecetodoanonosEUAeem2013irácompletar20edições. Pessoalmentejá
tiveoprazerdeparticipardealgumasedições, einclusivedeseroorganizadordo
PLoP2012,queaconteceuemTucson,noArizona.Sãoconferênciasnormalmente
paraumnúmeropequenodepessoas(normalmenteentre40e60pessoas)equesão
muitodiferentesdeumaconferênciacientíficatradicional.
ExistemoutrasconferênciasPLoPaoredordomundocomooEuroPLoP(Ale-
manha),AsianPLoP(Japão),KoalaPLoP(Austrália),VikingPLoP(paísesdaEscan-
dinávia),e,oestreantede2013,GuruPLoP(Índia).Existemtambémconferências
243

## Página 265

10.5.ComunidadedePadrões CasadoCódigo
temáticas,ondepessoasinteressadassereúnemparadiscutirpadrões deumdomí-
nioespecífico,comooMetaPLoP(metaprogramação),oScrumPLoP(padrõespara
documentarpráticasdoScrum)eoParaPLoP(programaçãoparalela).NoBrasil,a
cadadoisanos,ocorreoSugarLoafPLoP,oeventolatino-americanodepadrões, e
nosanosintermediáriosumMiniPLoP,umaversãoreduzidadoevento.
O que são linguagens de padrões?
U m alinguagemdepadrões éumconjuntodepadrões quedocu-
mentamsoluções eboaspráticasparaumdeterminadodomínio. Por
exemplo,euescreviumalinguagemdepadrões paraaconstrução de
frameworksqueutilizamanotações emetadados.Maisdoquesimples-
menteumasoluçãopontual,alinguagemdepadrõespossuisoluções que
sinergicamentepodemsercombinadasesecomplementam,sendouma
formadedocumentaroconhecimentodemodelagemsobreaqueledo-
mínio.
AsubmissãodeumpadrãoparaumPLoPpossuiumprocessodiferentedoque
asubmissãodeartigosparaoutrasconferências.Aosubmeterumpadrão,apósuma
filtrageminicial,eleéatribuídoaum shepherd(pastor).O shepherdéumaespecia-
listanaáreadepadrões cujopapeléorientareajudaroautoraevoluireamadurecer
otrabalhosubmetido.Sendoassim,durantecercadeummêsemeio,oautorem
conjuntocomo shepherdirãointeragirecooperarparaqueotrabalhoevoluadu-
ranteesseperíodo.Sódepoisdissoqueoartigorealmenteseráavaliadopelocomitê
edecididoseeleseráaceitoounãonaconferência.
Naconferência,oautorprecisaparticipardeumaseção chamadade W r i t e r s
W o r k s h o p,queébemdiferentedeumaseçãotradicionalondeoautorsimplesmente
apresentaoseutrabalho.Nessaseção,umgrupoirádiscutirotrabalhodoautorle-
vandoemconsideraçãooentendimentoqueobtiveramsobreotrabalho,apontando
pontosdemelhoriaedandosugestões. Oautorparticipadadiscussãoapenasnoini-
cio,quandoselêumapequenapartedoartigo,enofim,quandopodetirardúvidas
sobrealgumcomentário.Pormaisangustiantequesejaveraspessoasdiscutindo
sobreseutrabalhoenãopoderopinarouexplicaralgumacoisa,esseéumprocesso
comoqualsetemumgrandefeedbackarespeitodecomooutraspessoasenxergam
oseutrabalho.
Pessoalmentegostomuitodoestilodacomunidadedepadrões, quetemumes-
244

## Página 266

CasadoCódigo Capítulo10.IndoAlémdoBásico
píritomuitocolaborativo,focadoemajudaraquelesqueparticipamdelaadocumen-
taremseuspadrõesdamelhorformapossível.Nasconferências,alémdoestilopecu-
liardasapresentações, aindaexistetodaumaculturaquevalorizamuitoainteração
entreaspessoas.Existem,porexemplo,tradições comoadejogosparaaproximaros
participantesetrocadelembrançasemquecadaumtraznormalmentealgotípico
desuaregiãooupaís.
10.6 E agora?
“Todavez q u evocêt e mmedo de fazer a l g u m acoisa e vocêfaz, e l at edeixa mais forte.
M e s m oq u evocêf a l h e .”
–FredBartlit
Duranteesselivrofoitrilhadoumcaminhoquepassoupordiversospadrõesque
mostrameexemplificamtécnicasparaacriaçãodoprojetodeumsoftwareorientado
aobjetos.Diferentementedequandoseaprendeausarumnovoframeworkouuma
novaAPI,quandoseestáadquirindoconhecimento,saberprojetarumsoftwareé
umahabilidade.Eumahabilidadesóseaprendedeverdadecomprática,sendoque
oconhecimentoénecessário,porémnãosuficiente.
Sendoassim,opróximopassoagoraétentarcolocarempráticaospadrões e
técnicasapresentadosnestelivro.Quandodesenvolverumsoftwareprocureolhar
paraelecomolharmaiscrítico,tentandoidentificarquaispadrõeselejáimplementa,
muitasvezesdeformainduzidapelosframeworksutilizados.U m adicapodeestar
nosprópriosnomesdasclasses,quecomfrequência“entregam”opadrãoutilizado.
Procureraciocinaremcimadaquelasolução eidentificarquaisforamosmotivos
paraautilizaçãodaquelepadrãoequaisbenefícioseleestátrazendoparaodesign.
Aprendemosmuitoobservandosoluções prontaseabstraindooquefoiutilizadona
suaconcepção.
Emseguida,vejaquaisproblemasvocêconsegueidentificarecomopoderiaser
feitoparamelhorar.Muitasvezes,umpadrãodeixoudeseraplicadoemumasitua-
çãoemqueeleeraadequado,porémtambémnãoéraroencontrarimplementações
depadrõesincorretas,emqueelesforamutilizadosnocontextoerrado.Aduplicação
decódigo,porexemplo,éumindíciodequealgonãoestácheirandobemnaquela
partedosoftware. V e j aentãocomoalgumpadrão poderiateajudarnaresolução
daqueleproblema,considerandoasconsequênciasequalopesodecadaumaparao
cenárioemquestão.
245

## Página 267

10.6.Eagora? CasadoCódigo
Adicionalmente,aocriarumanovasolução,penseemcomoalgumpadrãopo-
deriateajudarnaresoluçãodosproblemasenvolvidos.Procureconteraansiedade
deaplicardiversospadrões emsequênciasemteralgumamotivaçãonosrequisitos.
T a m b é mnãodeixedecombinarospadrões nassituações emqueissoforadequado.
Projetarumsoftwareconsisteemsaberequilibrarosrequisitosatravésdacombina-
çãodesoluções paraospequenosproblemas,deformaaseobterumresultadofinal
adequado.T e s t esuassoluções! Criecenáriosbaseadosemhistóriasdoclienteeveja
seseudesignseencaixa.U s eboaspráticasemantenhaocódigolimpoparaqueseja
fácilderefatorá-lofrenteanovasnecessidades.
Finalmente,desenvolvimentodesoftwareéalgoqueseestudadurantetodasua
carreira! Conheçanovospadrões, estudecomoospadrões seencaixamnasnovas
tecnologias,ebusqueospadrões específicosparaosdomíniosrelacionadosasua
arquitetura.Alémdisso,lembre-sequedesigndesoftwareéumaatividadecriativa,
então eviteformulasprontas,tenhasempreumavisão críticaeutilizeospadrões
comoumaferramentadasuacriatividade.
Boasorte!
246

## Página 268

CasadoCódigo ÍndiceRemissivo
ÍndiceRemissivo
AbstractFactory,136,137,139,140,236
Adapter,115,118,119,146,202,208
Anti-CorruptionLayer,207
Bridge,51,52,54,55,75,93,161,165
Builder,130–135,140–142,144,230,238
ChainofResponsibility,87,90,91,93,95,
96,102,163,165,172
Command, 106, 166–169, 171–173, 176,
177,196,199,236
Composite,81–84,94,96,126,127,131,
134,140,161,163,165,195,232
DataAccessObject,40,108,109
Decorator,100–102,105,111,115,120,124,
165
DependencyInjection,148–153,156,158,
161–164,169,206,211,213,238
DoubleDispatch,179,182–185,191,192,
196
DynamicFactory,142–144,146,147,150,
164,171,206
Facade,200–203,205–208,212,215,225,
230
FactoryMethod,42,43
Flyweight,215–219,221–226
GentleLearningCurve,230
LowSurface-to-volumeRatio,230
Mediator,208–212,215,226
NullObject,24–26,43,50,90,96,161
Observer,67,71–75,93,146,171,199,209,
234,236,239,241
PrevalentSystem,176
Proxy,92,100–112,115,120,121,124,125,
129,131,135,140,144,152,155,
165,200,242,243
Service Locator, 156–158, 160–164, 171,
206,238
Singleton,128,129,140,211,238
State,57,58,64,65,75
StaticFactory,238
StaticFactoryMethod,124–129,134,140,
144,221,222
Strategy,14,15,18,36,46,49,55,64,75,
163,165,171,199
TemplateMethod,29–32,34,38,39,43,
46,90,124,125,140,163,171
Visitor,184,185,188–192,195,196,200
247

## Página 270

CasadoCódigo ReferênciasBibliográficas
ReferênciasBibliográficas
[1]AlexMarquesCamposAlexandreGazola. Padrões deprojetocomgenerics-
revistamundoj,edição35.
[2] KentBeck. ImplementationPatterns.Addison-WesleyProfessional,2007.
[3] JoshuaBloch. E ff e c t i v eJ a v a ,Segunda edição.Addison-Wesley,2008.
[4] JosephW .YoderBrianFoote. Theselfishclass-patternlanguagesofprogram
design3.1997.
[5]MurraySilversteinChristopherAlexander,SaraIshikawa. A Pattern Language:
T owns,Buildings, Construction.OxfordUniversityPress,1977.
[6] JohnCrupiDeepakAlur,DanMalks. Core J2EE Patterns: Best Practices a n d
Design Strategies.PrenticeHall,2003.
[7] ScottStanlickDonBrown,ChadMichaelDavis. S t r u t s2 i nA c t i o n.2008.
[8] RalphJohnsonDonRoberts. Evolvingframeworks: Apatternlanguagefor
developingobject-orientedframeworks-proceedingsofthethirdconference
onpatternlanguagesandprogramming.1996.
[9] UiráKuleszaClovisFernandesEduardoGuerra,FelipeAlves. Areferencear-
chitectureforimprovingtheinternalstructureofmetadata-basedframeworks
-journalofsystemsandsoftware,volume86,issue5.2013.
[10]RalphJohnsonJohnVlissidesErichGamma,RichardHelm. Design Patterns:
Elements o fReusable Object-Oriented Software. Addison-WesleyProfessional,
1994.
[11]EricEvans. Domain-Driven Design: Tackling Complexity i nthe H e a r to fSoft-
ware.Addison-WesleyProfessional,2003.
249

## Página 271

ReferênciasBibliográficas CasadoCódigo
[12]MartinFowler. Refactoring: Improving the Design o fExisting Code. Addison-
WesleyProfessional,1999.
[13]MartinFowler.Inversionofcontrolcontainersandthedependencyinjection
pattern.http://martinfowler.com/articles/injection.html,2004.
[14]Martin Fowler. Fluent interface. http://martinfowler.com/bliki/
FluentInterface.html,2005.
[15]MartinFowler. Domain-Specific Languages. Addison-WesleyProfessional,
2010.
[16]JoshuaKerievsky. Refactoring t oPatterns.Addison-WesleyProfessional,2004.
[17]JosephW .YoderLeonWelicki,RebeccaWirfs-Brock.Thedynamicfactorypat-
tern-proceedingsofthe15thconferenceonpatternlanguagesandprogram-
ming.2008.
[18]JamesNoble.Classifyingrelationshipsbetweenobject-orienteddesignpatterns
-australiansoftwareengineeringconference.1998.
[19]CliftonNock. Da taAccess Patterns: Database Interactions i nObject-Oriented
Applications.Addison-WesleyProfessional,2003.
[20] LarryO’Brien.Designpatterns15yearslater:Aninterviewwitherichgamma,
richardhelm,andralphjohnson. http://www.informit.com/articles/article.
aspx?p=1404056,2009.
[21]JavaCommunityProcess. Jsr-315javatmservlet3.0. http://jcp.org/aboutJava/
communityprocess/final/jsr315/index.html,2009.
[22] BrianFooteRalphJohnson. Designingreusableclasses-journalofobject-
orientedprogramming.1988.
[23]T r y g v eReenskaug. Themodel-view-controller(mvc)-itspastandpresent.
http://heim.ifi.uio.no/~trygver/2003/javazone-jaoo/MVC_pattern.pdf,2003.
[24] NatPryceSteveFreeman.Evolvinganembeddeddomain-specificlanguagein
java-proc.oopsla2006.2006.
[25]TimMackinnonJoeWalnesSteveFreeman,NatPryce.Mockroles,notobjects
-proc.oopsla2004.2004.
250

## Página 272

CasadoCódigo ReferênciasBibliográficas
[26] OvidiuTudosa. Prevalentsystem. https://wiki.engr.illinois.edu/download/
attachments/121733136/prevsystem_otudosa2.pdf,2009.
[27]BobbyW o o l f .Thenullobjectpattern-patternlanguagesofprogramdesign3.
1997.
[28] MicheldeChamplainY u nMai.Apatternlanguagetovisitors-proceedingsof
the8thconferenceonpatternlanguagesandprogramming.2001.
251