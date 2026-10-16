---json
{
  "id": "cdi_integre_as_dependencias_e_contextos",
  "title": "CDI_Integre_as_Dependencias_E_Contextos",
  "categoria": "06-devops-infra",
  "subcategoria": "ci-cd",
  "resumo": "**Arquivo Original:** `CDI_Integre_as_Dependencias_E_Contextos.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "cdi",
    "cdi_integre_as_dependencias_e_contextos",
    "contextos",
    "dependencias",
    "devops",
    "infra",
    "integre"
  ],
  "perguntas_tipo": [
    "Como utilizar CDI_Integre_as_Dependencias_E_Contextos?",
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

# CDI_Integre_as_Dependencias_E_Contextos

> **Arquivo Original:** `CDI_Integre_as_Dependencias_E_Contextos.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 2

CasadoCódigo Sumário
Sumário
1 AntesdefalardeCDI... 1
1.1 Boaspráticasdeorientaç ãoaobjetos ................... 2
1.2 Lidandocomoacoplamento ........................ 7
1.3 Evoluçãodasferramentasdegestãodedependência .......... 1 1
1.4 Obomevelhoarquivoproperties ..................... 1 1
1.5 BuscandoasdependênciascomSpringeXML ............. 1 4
1.6 BuscandoasdependênciascomSeameanota ções ........... 1 7
1.7 Deondevimos? ............................... 1 9
2 OqueéeparaqueserveaCDI 21
2.1 Paraondevamos? .............................. 2 1
2.2 Evitandoqueacomplexidadedocódigosempreaumente ....... 2 1
2.3 Introdu çãoàinje çãodedependências .................. 3 1
2.4 Amotivaç ãodaCDI ............................. 3 6
2.5 Oqueéeparaqueserveumaespecificaç ão? ............... 3 6
2.6 ACDIésóparaJavaEEmesmo? ..................... 3 8
3 IniciandoumprojetocomCDI 39
3.1 OláCDI .................................... 3 9
3.2 OqueéumpacoteCDI? ..........................4 7
3.3 Usandoinje çãoempropriedades,construtoresemétodosinicializa-
dores......................................4 8
3.4 Asformasdeseinjetardependências ...................4 9
3.5 Recapitulando ................................ 5 2
i

## Página 3

Sumário CasadoCódigo
4 Resolvendodependênciascomtipagemforte 53
4.1 Lidandocomaambiguidadenasdependências ............. 5 4
4.2 Osqualificadores ............................... 5 8
4.3 Alternatives:eliminandoambiguidadeetornandoumbeanopcional 65
4.4 Prioridade:novidadedaCDI1.1,partedoJavaEE7 ..........6 8
4.5 Beansnomeados ...............................7 0
4.6 Trabalhandocomheran çaentrebeans .................. 7 2
4.7 Restringindootipodosbeans ....................... 7 4
4.8 Resoluçãodedependênciasobdemandaelookupprogramático ...7 6
4.9 Resumodofuncionamentodaresoluç ãodedependências.......8 0
5 OciclodevidadosobjetosgerenciadospelaCDI 83
5.1 Métodosprodutores .............................8 4
5.2 EscoposdaCDI ...............................8 9
5.3 Escopoderequisiç ãocom@RequestScoped ...............9 4
5.4 Escopodesessãocomo@SessionScoped ................. 9 7
5.5 @ApplicationScoped:Omaiorescopopossível .............9 9
5.6 @ConversationScoped:Vocêcriandoseupróprioescopo .......1 0 1
5.7 @Dependent:OescopopadrãodoCDI .................1 0 8
5.8 Métodosfinalizadores ............................1 1 1
6 InterceptorseDecorators 113
6.1 Implementandorequisitostransversaiscominterceptors ........1 1 3
6.2 Interceptadoresdeciclodevida ......................1 2 1
6.3 EstendendoumbeanexistentecomDecorators .............1 2 4
6.4 Vinculaçãodinâmicaentreoobjetodecoradoeseudecorador ....1 2 6
7 DefinindoEstereótiposediminuindooacoplamentoutilizandoEventos 133
7.1 Definindoestereótipos ...........................1 3 4
7.2 UtilizandoEventosparaobterumbaixíssimoacoplamento ......1 3 7
7.3 Observadoressíncronosdeeventos ....................1 4 1
7.4 Eventosequalificadores ...........................1 4 1
7.5 Observadoresassíncronosdeeventos ...................1 4 6
7.6 Injetandodependênciasnosobservadores ................1 4 8
ii

## Página 4

CasadoCódigo Sumário
8 ArelaçãodaCDIcomasdemaisespecificaç õesJavaEE 151
8.1 RelaçãoentreCDIeEJB/JPA ........................1 5 2
8.2 RelaçãoentreCDIeJSF ...........................1 5 6
8.3 RelaçãoentreCDIeJMS ..........................1 6 3
8.4 Empacotandoasmelhorias .........................1 6 9
9 ExtensõesCDI 171
9.1 DoSeamàCDI ................................1 7 2
9.2 Extensõesportáveisdisponíveis ......................1 7 4
9.3 Criandonossasextensões ..........................1 7 5
9.4 Extensãoportável:usandoconven çãoemvezdeconfiguraç ão ....1 7 7
9.5 Extensãonãoportável:eventosassíncronosforadoJavaEE ......1 8 0
10 ExecutandoCDIemdiferentesambientes 189
10.1 ExecutandoCDIemservletcontainers ..................1 9 0
10.2 ExecutandoCDIapartirdeumaclassemain ..............1 9 3
10.3 Ecomotestarumaaplicaç ãoCDI? ....................1 9 5
10.4 Desenvolvendotestesdeintegraçãocompersistência..........2 0 1
ÍndiceRemissivo 208
iii

## Página 6

Capítulo1
AntesdefalardeCDI...
OassuntoprincipaldestelivroéaCDI,masnãoiremoscome çarnossosestudos
diretamentenela.Teremmãosumaboaferramentaémuitobom,porém,antesde
utilizá-la,precisamosversobredesenvolvimentodesoftwarecomoumtodo.Mesmo
quevocêsejaumprogramadorexperiente,valeapenarevisitartópicosimportantes
comoesses.Atéporqueserexperientenãoésinônimodesabertudo.
Obomdesenvolvimentodesoftwarenãoéumatarefatrivial. Equilibraraba-
lançaquetem,deumlado,aaltacoesão,edeoutro,obaixoacoplamentoéalgoque
setornamaissimplescomaexperiênciaeobservandobonscódigos.
Nãoépossíveljustificaramáqualidadedeumsoftwarepelaquantidadedemu-
dançasqueomesmoprecisousofrerporaltera çõesnonegócio,ousimplesmente
pormudan çadeopiniãodocliente.Issovaiacontecer,ecabeanós,desenvolvedo-
res,projetarmosnossasaplicaçõesdeformaaacomodardamelhorformapossível
essasmudan ças.
Amenosqueosoftwarequeestivermosdesenvolvendosejaalgoparaumane-
cessidadetemporária,enãotenhaumusopermanente,certamenteelemudará,e

## Página 7

1.1. Boaspráticasdeorientaçãoaobjetos CasadoCódigo
nãoapenasumavez,ecomissoalgumaspartesdeleirãosofrercomessamudan ça.
Podeseratéque,dependendodaurgência,aparteafetadapelamudan çapreciseser
melhoradadepois,masnãopodemosdeixarqueesseefeitosejapropagadoparatoda
aaplicação.
Tomemoscomoexemploumaaplicaç ãoquecontroletudorelacionadoaosre-
cursoshumanosdeumaempresa,desdeocadastrodetalhadodosdadosdosfuncio-
náriosatéafolhadepagamento.Agoravamosconsiderarumamudan çadelegislação
quenosobrigueamudaraformacomoafolhadepagamentoécalculada,eessaseja
simplesmenteapartemaiscomplexadetodoosistema,umavezquealémdosalário
decadafuncionário,éprecisotambémcalculartodososimpostosedescontosde
planodesaúde,empréstimoscomdescontoemfolhaetudomais.
Nessecenário,épossívelargumentarqueamudan çaéinviávelpormexerno
cernedosistema? Obviamente,não. Entãonossosistemaprecisaser resiliente,ou
seja,suportarbemasmudan ças.
Nocenárioapresentado,amudan çadetodoocálculodafolhadepagamento
provavelmentenãoseráapiorpartedotrabalho.Geralmenteaequipesabeprogra-
mar,escrevercódigo,econsequentementevaisaberpassarparaaIDEasalterações
nalegislação.Apiorpartecostumaseroreflexodessamudan çanorestantedosoft-
ware.Apesardenãoserofocodolivro,veremosumpoucosobretestesnocapítulo
10,eentãoentenderemosoquantoessaéumaferramentaimportanteparaminimi-
zarosriscosdessescomportamentosnãoprevistosapósumaalterações.Masantes
mesmodeescrevertestesparaosistema,temosqueprojetaressesistemadeformaa
nãopropagarmosasmudan çasdeumadeterminadaparteparaosistematodo.Esse
efeitocascataéquecostumaserapiorpartedeumamudan çagrande.
1.1 Boas práticas de orientação a objetos
Abaixacoesãoeoaltoacoplamentosãoasprincipaiscausasdeumamudan ça,que
deveriaficarretidaemumaparte,sairdestruindoosistematodo.Masoquereal-
menteéisso?Ouvimostantofalaremcoesãoeacoplamentomasasvezesnãotemos
certezadoqueissosignifica.
Coesão
Acoesãoéacapacidadedeumobjetoestarfocadonasuatarefaespecífica.Seseu
papelécalcularosaláriodofuncionário,entãoquefaç aisso.Elenãodevecalcular
osalárioecalcularodescontodoimpostoderenda, ecalcularodescontodoplano
2

## Página 8

CasadoCódigo Capítulo1. AntesdefalardeCDI...
desaúde,ecalcularasfériasproporcionaisdaquelemês,emaisummontedecoisas.
Issoporqueseumadessascoisasmudar,nossocódigomuda.
Nãoexisteporémumaregraquedeterminaatéquepontoalgodeveestarjunto,
eapartirdessepontoascoisasdevemserseparadas.Noexemploanterior,podemos
tertudoissonummesmoobjetosejulgarmosomelhorlocal,masseriainteressante
termosmétodosespecíficosseparandocadatarefa,aindaquesejamprivados,ede-
poisterummétodoquecombinetodosessessubcálculos.
Podemosperceberque,dessamaneira,criamosníveisdereten çãodamudan ça.
Seocálculodeimpostoderendamudar,mudamosapenasométodoespecíficoe
osdemaisnãosãoafetados.Setodoocálculodafolhadepagamentomudar,talvez
tenhamosquealteraraclassetoda,masessamudan çaaindaficariarestritaaessa
classe,nãoafetandoasdemaisdosistema.
Granularidade
Equantoaofatodedeixarmosossubcálculosemmétodosespecíficosdentro
deumamesmaclasse,nãoseriamaisadequadocolocarmoscadaumdelesemuma
classediferente?Semfazerissonãoestaríamoscriandoumaclassepoucocoesa,que
fazcoisasdemais?
Novamente,nãoexisteumarespostaparaqualquercenário.Essamedidadeta-
manhodecadaunidade,comométodo,classe,subsistema,chamamosdegranu-
laridade. Setivermosclassesmenores,cadaumacontendoumsubcálculodesses,
podemosdizerqueestamostrabalhandocomumagranularidademaisfina. Ésó
imaginarcadaclassecomoumgrãodeareia. Nessecasoteríamosumaareiabem
fina.
Agorasefizermoscadapartedocálculomaioremummétododiferente,mas
namesmaclasse,eformosaplicandoamesmaideiaemtodonossosistema,nossas
classesserãocomogrãosmaioresdeareia—logoteremosumagranularidademais
grossa.
Equalotamanhoideal?Apartirdequalmomentoprecisamostransformarpar-
tesdonossométodoemmétodosseparados,edepoissepararessesmétodosemclas-
sesespecíficas?Comonãohárespostamágica,costumamosdeixarnossométodono
tamanhomáximodeumateladeummonitormédio.Então,seformosanalisarocó-
digodeummétodo,podemosfazê-losemrolaraimagemnomonitor.Masnoteque
consideramosummonitormédio,poisdenadaadiantavocêterummonitorde30”
comumaresoluç ãoabsurdaenquantoosoutrosmembrosdaequipetêmmonito-
resde17”ou19”comumaresoluçãobemmenor.Epense,aindaquetodostenham
3

## Página 9

1.1. Boaspráticasdeorientaçãoaobjetos CasadoCódigo
essatelaenorme,seráqueparaenchê-latodacomcódigo,nãoteremosinformaç ão
demaisparaanalisar?Aanalogiadométododotamanhodeumatelaéparaajudar
queelesejapequeno,defácilcompreensão.Vocêtemqueolharelogoentender.Se
atelaformuitograndeeafontemuitopequenavocêpodeconseguircolocaruma
bíbliainteiranelasemprecisarutilizararolagem,masissonãovaiajudarmuito.
Deformasemelhante,devemoscuidardotamanhodasnossasclasses. Nãohá
umaregrabaseadanaquantidadedemétodos,poisotamanhodelespodevariar
bastante.Podemostermétodoscommeiadúziadelinhaseoutrosdotamanhoda
nossatela.Maséinteressantedefinirumametacomumparaatodaaequipe,oupara
você,casotrabalhesozinho.Definaporexemplo150ou200linhasevejasefunciona
bem. UtilizeferramentasnaIDEounoservidordeintegraç ãocontínuaquefaç a
relatóriosautomáticosdequaisclassesoumétodosestãomuitograndes,issovaite
ajudar no começo,maslembre-sequeomaisimportanteégerenciarmososignifica
dosmétodosedasclasses.Vocênãovaiquebrarummétodoouclasseporqueuma
ferramentaestámandando,vocêvaiusaresseindicadorcomoumalertateavisando
queométodoouclasseestágrandedemais,eentãovocêvaireadequá-losparaque
semantenhamsempresimplesdeentenderefáceisdealterar,poismudan çassempre
existirão.
4

## Página 10

CasadoCódigo Capítulo1. AntesdefalardeCDI...
Outros cenários onde av aliamos a granularidade
Esseconceitodegranularidadeéimportantetambémemoutrosce-
nários,comonaprogramaçãodistribuída. Naprogramaçãolocal(não
envolvendopassagemdevalorespelarede)podemoschamardiversos
métodos,cadaumarealizandoumapequenapartedotrabalhoejun-
tandooresultadoemmilissegundos.Quandofazemosumaprograma-
çãodistribuída,chamandoummétodoqueestárodandoemoutramá-
quina,precisamosqueessemétodofaç amaiscoisas,paraprecisarmos
chamarmenosmétodosdiferentesparaobteromesmoresultado,pois
cadainvoca çãodemétododiferentepassapelaredeparachegaraoou-
trocomputador,entãoémelhorumnúmeromenordeinvocaç ões.
Nessecasodaprograma çãolocalversusaprogramaç ãodistribuída,
quandoosmétodonosdãorespostasmenores,temosumagranularidade
maisfina,equandoasrespostassãomaiscompletas,temosumagranu-
laridademaisgrossa.Qualamelhor?Geralmentequandoprogramamos
local,umagranularidademaisfinanosdarámétodosmenores,econse-
quentementemaisfáceisdeentender.Jáquandotemosumachamadade
métodoremota,émelhorumagranularidademaisgrossa,poistemosa
latênciaderedenomeiodocaminho.Mesmonessetipodeprograma-
ção,devemosteraseparaç ãodecadapartedotrabalhofeitadamesma
maneiraquefaríamosnaprogramaç ãolocal,facilitandooentendimento
docódigo.Adiferen çaéquenãochamaremoscadaumdessesmétodos,
esimummétodoquecombinetodoseles.
Acoplamento
Enquantoacoesãoéamedidadoquantoumobjetoéfocadoemsuatarefa,o
acoplamentoéamedidadasociabilidadedesseobjeto,ouoquantoeleserelaciona
comosoutrosobjetoseafor çadessesrelacionamentos. Porexemplo,receberum
objetodotipo
Funcionariocomoparâmetrodeummétodoéumacoplamento
menorqueterdentrodanossaclasseumapropriedadedessetipo,queporsuavezé
menortambémdoquenossaclasseserumsubtipode
Funcionario.
5

## Página 11

1.1. Boaspráticasdeorientaçãoaobjetos CasadoCódigo
Figura1.1:Ilustraçãoreferenteaoacoplamento,quandomenor,melhor
Coesãoeacoplamentosãoladosopostosdeumabalan ça. Àmedidaquepro-
curamosmanterumaaltacoesão,deixaremosdeterclasses“sabe-tudo”eteremos
maisrelacionamentosentreclassescompapéisespecíficos.Massetentarmosdimi-
nuirdemaisoacoplamento,voltaremosaterclassesqueagregammuitasfun ções,
visandodiminuirasdependênciasentreelas,masacabandocomsuacoesão.
Paranossasorte,essaequa çãojávemsendoresolvidahábastantetempo,ea
formacomoissotemsidofeitoéfocarnacoesão,edelimitarbemasfronteirasen-
treasclassesparaquesuasinter-relaçõesnãocausemumacoplamentonegativo.
Umacoplamentonegativoéaqueleemqueasclassesqueserelacionamconhecem
demaisotrabalhodaoutra.Assim,pormaisqueasresponsabilidadesestejam(par-
cialmente)separadas,aclasse
Asabecomoaclasse Bestáimplementadaetoma
diversasdecisõeslevandoissoemconsideraç ão. Naprática,aimplementaçãode
umaécontinuaçãodaoutra.
Aodefinirfronteirasentreasclasses,devemoscuidarparaqueumafuncionede
formatotalmenteindependentedaoutra. Pormaisqueamesmapessoacodifique
ambas,éimportantequeasdecisõesinternasdeumanãosepropagemparaaoutra.
Assim,seumamudar,aoutrapodecontinuarigual.
Porexemplo,vamosconsiderarumaclassequecalculatodaafolhadepagamento
deumaempresa,eoutraclassequeexibeosdezmaioressaláriosparaopresidenteda
empresa.Imagineque,aocalcularafolhadepagamento,aprimeiraclassearmazena
umalistadosfuncionáriosquetiveramseussalárioscalculadosemordemdecres-
centedesalário.Easegundaclassesimplesmenteexibeosprimeirosdezelementos
dessalista,poissabequeapósocálculoalistaestaráordenada.
Ocorreporémque,porquestõesdeperformance,aprimeiraclasseéalterada,de
6

## Página 12

CasadoCódigo Capítulo1. AntesdefalardeCDI...
modoarealizarocálculodossaláriosdeformaparalela,eapósajun çãodotrabalho
decada Threadoresultadonãoestámaisordenado.Nessecaso,aclassequeexibeos
dezmaioressaláriossofreráumimpactoporestaracopladademaiscomaprimeira.
Essetipodeacoplamentoéumquedevemosevitar.
Definainterfacesclarasentreasclasses,deixandonítidooquecadaumarecebee
devolvedeinformaçõesparaaoutra,eimplementecadaclassedeformaquesomente
ainterfacedaoutrasejaconhecida,esuaimplementaç ãointernasejatotalmente
ignorada.
1.2 Lidando com o acoplamento
Comoditoanteriormente,lidardeformaeficientecomacoplamentoéumamatéria
quevemsendoaprimoradahámuitosanos. Existemdiversospadrõesdeprojeto
quenosajudamagerenciá-lodeformaeficiente,etambémferramentas—oufra-
meworks—quenosajudamaimplementaressespadrõesdeumamaneirasimples.
Essenãoéumlivrodepadrõesdeprojetos,masveremosalgunsparanosajudar
aentendernapráticaessesconceitos.Umpadrãofácildeentenderequeservirápara
nossoexemploinicialéo Strategy.Imagine,porexemplo,queprecisamoscompactar
umarquivo,queserárepresentadoporumarraydebytes.Precisamosdeumaclasse
querecebaessearrayedevolvaumnovoarrayquerepresenteoarquivojácompac-
tado,porémtemosdiferentesformas,ouestratégiasdecompactaç ão,comoozip,o
rareobzip2. Ointeressantedessepadrãoéquepodemosfacilmentetrocaraes-
tratégia,oualgoritmoutilizadopararesolveromesmoproblema,semalterarnosso
códigoparaisso.
Trazendoparaumexemplomaispróximodanossarealidade,vamosconsiderar
onossocálculodesalários.Podemosterdiferentesimplementaçõesdeumacalcula-
doradesaláriononossosistema,umaparacadaversãodoplanodecargosesalários
daempresa.Provavelmentenessecasonãoteremosessasdiferentesversõesexecu-
tandoemummesmomomento,jáapenasumplanodecargosficaemvigorporvez.
Mesmoassimaplicaremosomesmoconceitopoisainterfacecontinuaráamesma,e
apenasaimplementaçãoseráalterada.
Paraexemplificarvamosconsiderarainterfaceaseguir.
public interface CalculadoraDeSalarios {
double calculaSalario(Funcionario funcionario);
}
7

## Página 13

1.2. Lidandocomoacoplamento CasadoCódigo
Evamosconsiderarquenoano2000,aempresapossuíaumsalárioúnicopara
osfuncionários,todosrecebiamR$ 2.000,00.
public class CalculadoraDeSalariosPadrao
implements CalculadoraDeSalarios {
public double calculaSalario(Funcionario funcionario) {
return 2000.0;
}
}
Jáiniciamosbem,utilizandoumainterfacequedefineoqueseesperadeumacal-
culadoradesalários,masmesmoassimprecisaremosinstanciarumobjetodanossa
classequandoformosutilizaracalculadora. Logo,teríamosumtrechodecódigo
parecidocomoseguinte.
...
Funcionario funcionario = buscaAlgumFuncionarioDeAlgumLugar();
CalculadoraDeSalarios calculadora = new CalculadoraDeSalariosPadrao();
double salario = calculadora.calculaSalario(funcionario);
...
Todavezqueprecisássemosdeumainstânciada CalculadoraDeSalarios
serianecessáriousarooperador newecriarumanovainstânciadaimplementaç ão
quetemos. Mas,pormaisqueainterfacefacilitebastantenaevolu çãodosistema,
permitindo-nostrocaraimplementaç ãosemquebrarosclientes,quandomudarmos
essaimplementação,precisaremosalterartodonossosistema,buscandoondeaim-
plementaçãoantigaestavasendousadaetrocarpelanova.Essanovaimplementaç ão
podeser,porexemplo,combaseemumnovoplanodecargosesaláriosetenhasaído
em2002.
public class CalculadoraDeSalariosPlano2002
implements CalculadoraDeSalarios{
public double calculaSalario(Funcionario funcionario) {
if(funcionario.getEscolaridade() == Escolaridade.SUPERIOR){
return 3000.0;
}
else{
return 2000.0;
}
8

## Página 14

CasadoCódigo Capítulo1. AntesdefalardeCDI...
}
}
Combasenonovoplano,funcionárioscomnívelsuperiorpassamaganharR$
3.000,00,enquantoosdemaiscontinuamganhandoR$ 2.000,00.Nãosepreocupe
comaimplementaç ão,elaestápropositalmentesimples,aideiaépercebermoso
problemaqueteremos,poisprecisaremosfazerum find replacenanossaaplicaç ão
trocandotodososlugaresondeaimplementaç ãoantigaerausada.
Por esse problema, geralmente aliado ao padrãoStrategy, costumamos uti-
lizar o padrãoFactory Method. Assim temos um método que sabe criar ob-
jetos da forma correta. No nosso caso, esse objeto é a implementação de
CalculadoraDeSalarios.Anossaimplementaç ãodessemétodoconstrutorde
objetospodeseralgobemsimplescomooquesegue.
public class CalculadoraDeSalariosFactory {
public CalculadoraDeSalarios criaCalculadora(){
return new CalculadoraDeSalariosPlano2002();
}
}
Eseuusoficariadaseguinteforma.
...
Funcionario funcionario = buscaAlgumFuncionarioDeAlgumLugar();
CalculadoraDeSalariosFactory factory =
new CalculadoraDeSalariosFactory();
CalculadoraDeSalarios calculadora = factory.criaCalculadora();
double salario = calculadora.calculaSalario(funcionario);
...
A vantagem de termos um meio “terceirizado” de criar nossos objetos,
é que qualquer mudança na forma de criá-los fica escondida dentro dele.
Até agora, a mudança que tivemos foi apenas trocar a implementação da
CalculadoraDeSalarios,masaaltera çãopoderiasermaior.
Apenasparaevoluirnessalinhaderaciocínio,consideremosque,mesmoapósa
reestruturaçãodoplanodecargosdaempresa,em2002,osfuncionáriosreivindica-
ramquefosseseguidoopisosalarialdacategoria,equeessasolicitaç ãofoiatendida.
Logo,comodesenvolvedoresdosistemaquecalculaafolhadepagamento,precisa-
remosutilizaressareferênciasalarialparacalcularossalários,eparatal,definimos
aseguinteinterface.
9

## Página 15

1.2. Lidandocomoacoplamento CasadoCódigo
public interface TabelaDeReferenciaSalarial {
double buscaPisoSalarial(Cargo cargo );
}
Assim,teremosquegarantirqueosaláriodofuncionárionuncasejamenorqueo
pisodocargoqueeleocupa.Comoesseéumexemploapenasdidático,quenemfará
partedoprojetoquedesenvolveremos,vamosignorarsuaimplementaç ão,conside-
randoapenasqueelasechama TabelaDeReferenciaSalarialPadrao.Agora
precisamos apenas passar essa tabela para nossaCalculadoraDeSalarios.
Para que essa dependência fique mais explícita podemos definir um método
setTabelaDeReferenciaSalarialnainterface CalculadoraDeSalarios.
Dessaforma,quemimplementaressainterfacesaberáqueobrigatoriamenteprecisa
receberessatabela.
public interface CalculadoraDeSalarios {
double calculaSalario(Funcionario funcionario);
void setTabelaDeReferenciaSalarial(
TabelaDeReferenciaSalarial tabela );
}
public class CalculadoraDeSalariosFactory {
public CalculadoraDeSalarios criaCalculadora(){
TabelaDeReferenciaSalarial pisosSalariais =
new TabelaDeReferenciaSalarialPadrao();
CalculadoraDeSalarios calculadora =
new CalculadoraDeSalariosPlano2002();
calculadora.setTabelaDeReferenciaSalarial(pisosSalariais);
return calculadora;
}
}
Veja que interessante, dessa vez não trocamos a implementação da
CalculadoraDeSalarios, mas mudamos a forma como ela é construída.
Aindaassimnãoprecisamossairalterandonossocódigoemtodolugar,eissoé
muitobom.Contudo,quasesempreháespaçoparamelhorias.
10

## Página 16

CasadoCódigo Capítulo1. AntesdefalardeCDI...
1.3 Evolução das ferramentas de gestão de depen-
dência
Apesardemuitosimples,oquefizemoscomnossafactoryfoiumaformadege-
renciarasdependênciasdanossaaplicaç ão,especificamenteasimplementaçõesde
CalculadoraDeSalariose TabelaDeReferenciaSalarial,estaúltimaé
umadependênciaindiretadanossaaplicaç ão,poisquemdependedelaéacalcu-
ladora.
Otrabalhoestáindobem,masnossoobjetivoéconseguirtrocaressasdependên-
ciassemprecisaralterarnossaaplicaç ão,nemqueessaalteraç ãoestejarestritaauma
únicaclasse.Emoutraspalavras,veremosoqueseráprecisofazerparatrocarmosos
componentes(dependências)danossaaplicaçãosemanecessidadederecompilaç ão
alguma.
Paraexemplificar,imaginequedepoisdemuitosanosdosistemaemexecuç ão,
osindicatodisponibilizaumwebservicecomasreferênciassalariais,evocêcrieuma
novaimplementaçãoda
TabelaDeReferenciaSalarialcombasenesseservi ço
web.Comasalteraçõesquefaremosapartirdeagora,serápossívelcolocarumnovo
jarcomaimplementaç ãonovanoclasspathdaaplicaç ão,alterarumarquivodecon-
figuração(ouasvezesnemisso),eaoreiniciaraaplicaç ãoanovaimplementaç ãojá
estáemuso.
Jáfoifaladoqueexistemframeworksquenosajudamnessetrabalho,everemos
osprincipaisprecursoresdaCDInasse çõesaseguir;masantesdissoveremoscomo
fazeressagestãomanualmente.
1.4 O bom e velho arquivo properties
Aformamaissimplesdetirarmosainstanciaç ãodasdependênciasdedentrodocó-
digo,éusandoarquivodepropriedades,noformatochave=valor.Paratrabalharcom
essesarquivos,usaremosaclasse
java.util.ResourceBundle.Suautilizaç ãoé
bemsimples,everemosmelhoratravésdeumexemplo.
Primeiroprecisaremoscriarumarquivonaraizdoclasspathdanossaaplicaç ão.
Paraisso,coloqueoarquivonapasta srcdoseuprojetodoeclipse,ou src/java
seestiverutilizandoonetbeans. Essessãoosdiretóriospadrões,masvocêpode
especificaroutrodiretóriodentrodaIDE.Oimportanteéqueoarquivocomnome
dependencias.propertiesfiquenopacote default.
Apóscriaressearquivo,queéumarquivotextosimples,vamosdeixá-locomo
seguinteconteúdo.
11

## Página 17

1.4. Obomevelhoarquivoproperties CasadoCódigo
CalculadoraDeSalarios br.com...CalculadoraDeSalariosPlano2002
TabelaDeReferenciaSalarial br.com...TabelaDeReferenciaSalarialPadrao
Odivisorentreachaveeovalorpodeserum =ousimplesmenteumespa çoem
branco,quefoioutilizado.Ecomovamosinstanciaressasclassesdeformadinâmica,
éimportantecolocarmosonomecompletodaclasse,queincluiopacote.Notrecho
deexemploosnomesforamencurtadosparasermaisfacilmentevisualizado.
Aseguirotrechoquecriaainstânciadaclasseapartirdaleituradeseunome
nessearquivoproperties.
public class CalculadoraDeSalariosFactory {
private ResourceBundle bundle =
ResourceBundle.getBundle("dependencias");
public CalculadoraDeSalarios criaCalculadora(){
String nomeDaClasse =
bundle.getString("calculadora_de_salarios");
try {
Class<?> classe = Class.forName(nomeDaClasse);
return classe.asSubclass(CalculadoraDeSalarios.class)
.newInstance();
} catch (Exception e ) {
return null;
}
}
}
Comopodemosver,obtemosumainstânciade ResourceBundleatravésdo
métodogetBundle,querecebecomoparâmetroonomedoarquivopropertiesque
criamos,semaextensão .properties.Comesseobjetoemmãos,conseguimos
recuperarqualquervalordedentrodoarquivopassandosuarespectivachavepara
ométodo getString.Porfim,dentrodeum try/catch,fizemosainstanciaç ão
daclasseapartirdeseunome,edepoisainstanciaç ãodoobjetoapartirdainstância
daclasse.Ométodo asSubclassestásendousadoapenaspararetornarmosotipo
corretodaclasse,casocontrárioométodo newInstancedevolveriaum Object
emvezdotipoqueesperamos,eentãoteríamosquefazerumcast.
Ousodo try/catchéobrigatóriopoisestamoslidandocomnomedeclasses
quepodemestardigitadosincorretamenteporexemplo,ouaclassepodenãoterser
visívelounãoterumconstrutorpadrãovisível.
12

## Página 18

CasadoCódigo Capítulo1. AntesdefalardeCDI...
Esse trecho serviu para entendermos como instanciar um objeto a par-
tir de um arquivo properties, mas agora precisamos terminar de criar nossa
CalculadoraDeSalarios de forma correta, pois ainda falta instanciarmos a
TabelaDeReferenciaSalarial.Paraqueocódigonãofiquemuitorepetitivo,
vamoscriarummétodoprivadochamado criaInstancia.Esseseráummétodo
genériconosdoissentidosdapalavra,poisusa genericseserveparaqualquertipode
classe.
private <T> T criaInstancia (Class<T> classe){
String nomeDaClasse = bundle.getString(classe.getSimpleName());
try {
Class<?> clazz = Class.forName(nomeDaClasse);
return clazz.asSubclass(classe).newInstance();
} catch (Exception e) {
return null;
}
}
Tantonessecódigo,quantonoanterior,oidealéqueusemosumaAPIdeLogger
pararegistrarumpossívelerronesseprocesso,enãoapenasdevolver nullsem
sabermosorealmotivodeissoterocorrido.
Analisandoessecódigo,percebemosqueutilizamosonomesimplesdaclasse
comochaveaserbuscadano dependencias.properties.Issodeucertoporque
utilizamosomesmonomedainterfacequedesejamosinstanciarcomochavedentro
doarquivo,oquefacilitounossotrabalhoagora.Orestantedocódigoépraticamente
omesmoquevimosanteriormente.
Agoraquejátemosumaestruturaparainstanciarnossosobjetos,podemosvoltar
aométodo
criaCalculadoradanossafactory,queéoquerealmentedevolvea
dependênciaqueprecisamos.
public CalculadoraDeSalarios criaCalculadora(){
TabelaDeReferenciaSalarial pisosSalariais =
criaInstancia(TabelaDeReferenciaSalarial.class);
CalculadoraDeSalarios calculadora =
criaInstancia(CalculadoraDeSalarios.class);
calculadora.setTabelaDeReferenciaSalarial(pisosSalariais);
13

## Página 19

1.5. BuscandoasdependênciascomSpringeXML CasadoCódigo
return calculadora;
}
Umavezquecriamosométodogenérico criaInstancia,ficoubemsim-
plescriarinstânciasdequalquerclasse. Emumsistemareal,essemétodoprova-
velmenteficariaemumaclasseutilitáriaqueseriautilizadaporqualquerfactory,
ouaindaevoluiríamosmaisessemétodoparaquepudéssemosterumfactorycom-
pletamentegenérica,queutilizasse reflectionparabuscarsubdependênciascomoa
TabelaDeReferenciaSalarialdentrodanossa CalculadoraDeSalarios.
Outraop çãoseriatambémtrocarosarquivosdepropriedadesporregistroem
bancodedados.Nessecaso,seasclassesjáestivessemnoclasspathdaaplicaç ão,não
serianecessárionemmesmoreiniciá-laparatrocarmosaimplementaç ãodeuma
interface.Porém,independentementedecomocontinuaríamosodesenvolvimento
danossaaplicação,jávimosoqueserianecessárioparagerenciarmosmanualmente
aimplementaçãodasdependênciasdasnossasclasses.Agorapassaremosavercomo
podemosfazeressagestãoatravésdeframeworks.
1.5 Buscando as dependências com Spring eXML
OSpringéumframeworkmuitoimportanteparaahistóriadoJava,poisenquanto
oJEEdopassado,chamadoàépocadeJ2EE,eramuitoverbosonoseuuso,oSpring
facilitoubastanteascoisas,dandoumaalternativaporforada“linhaoficial”doJava.
Seriacomocomprarumcarromasiraumaboaoficinanãooficial,poisaoficial
erademasiadamenteburocráticaelevávamosmuitotempoparaconseguiragendar
umarevisão. SeanalisarmososcódigosfeitosatéalgunsanosusandoSpringve-
remosmuitosaquivosXML,oqueacabouinclusivenaépocacaracterizandopejo-
rativamenteoframework,eatécertopontoaprópriaplataformaJavacomosendo
orientadaaarquivosXML.
Nessa seção,estaremosvendooSpringdopontodevistahistórico,então,por
maisquehojesejapossívelutilizaranota çõesemsuaconfiguraç ão,nomomento
históricoemqueelefoimaisimportanteaconfiguraç ãoerabasicamenteporXML.
PorémseformosiniciarumprojetoutilizandoSpringhojeemdia,certamentenão
faríamoscomoveremosaseguir.
Outropontoimportantedeconsiderarmoséqueestaremosinteragindocoma
APIdoSpringdeumaformadesanexadadeseucontexto.Estaremosbasicamente
utilizandooSpringcomofactory. Faremosissoapenasparasimplificaroentendi-
mento,enãovisandocomparaçõescomSeamouCDI.Quandodigoforadocontexto
14

## Página 20

CasadoCódigo Capítulo1. AntesdefalardeCDI...
significaquepartiremosdeumaclassesimples,ouatémesmoummétodo main,e
entãochamaremosoprimeirobeanatravésdocontextodoSpring.
Paracontinuarnamesmalinhadoexemploanterior,vamosconsideraramesma
factoryquecria CalculadoraDeSalarios.Porémagorairemosimplementá-la
usandoSpring.
import org.springframework.context.ApplicationContext;
import
org.springframework.context.support.ClassPathXmlApplicationContext;
public class CalculadoraDeSalariosFactory {
private ApplicationContext context =
new ClassPathXmlApplicationContext("dependencias.xml");
public CalculadoraDeSalarios criaCalculadora(){
CalculadoraDeSalarios calculadora =
(CalculadoraDeSalarios) context.getBean("calculadora");
return calculadora;
}
}
NãoveremosaquicomoconfigurarumambienteparaexecutaroSpring,masna
documentaçãodoframeworképossívelverosjarsnecessáriosparasuautilizaç ão.
Oquenosimportaéainstancia çãodoseucontextoeaobten çãodeumobjetode
dentrodeleatravésdométodo getBean.Essecontextofoicriadotendocomobase
oarquivo dependencias.xml,quegeralmenteédeixadonaraizdoclasspathda
aplicação,assimcomofizemoscomoarquivoproperties.
Podenãoparecer,masnossafactoryestápronta. Nãoprecisamosinstanciara
TabelaDeReferenciaSalarialecolocá-ladentrodacalculadora,poisoSpring
fazissopornós.Paratal,precisamosdeixaroarquivo dependencias.xmlcomo
otrechoaseguir.
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans-3.0.xsd">
15

## Página 21

1.5. BuscandoasdependênciascomSpringeXML CasadoCódigo
<bean id="calculadora"
class="br.com.casadocodigo...CalculadoraDeSalariosPlano2002">
<property name="tabelaDeReferenciaSalarial" >
<ref bean="tabela"/>
</property>
</bean>
<bean id="tabela"
class="br.com.casadocodigo...TabelaDeReferenciaSalarialPadrao">
</bean>
</beans>
PodemosperceberquedentrodoXMLfazemosareferênciadobeancomid
"tabela" dentro da propriedadetabelaDeReferenciaSalarial do bean
"calculadora". Comisso,aopedirmosacalculadora,oSpringinstanciatam-
bématabelaeatravésdométodo setTabelaDeReferenciaSalarialvincula
osdoisobjetos.
Umframeworkcomoessefacilitaemuitoquandotemosumaestruturamais
complexa,naqualobjetosdependemdeváriosoutrosobjetos,esuasdependências
possuemdependências. Fazerumafactorynamão,comovimosantesatravésde
arquivosproperties,ficariaextremamentecomplexoesuscetívelaerros. Paraau-
tomatizarumpoucomaisotrabalhoteríamosqueusarreflexão,eaindaassimnão
chegaríamosaonívelderefinamentoqueumframeworkespecíficoparaessefim
podenosproporcionar.
Obviamentenesseexemplomostramosalgomuitosimples.AssimcomoSeam
eCDI,oSpringtemmuitomaisqueisso. Osbeanspossuemescopos,podemter
interceptadoresemétododinâmicosderesoluç ãodedependência.Issotupoporque
apartirdomomentoemquechamamosométodo
getBean,entramosnocontexto
doSpring,edentrodessecontextoépossívelfazermuitacoisa,comointegraç ãocom
módulosJavaEEououtrosframeworks.Masobviamentenãoiremosentrarnesses
detalhes,poisseriaassuntoparaumlivroespecífico.
Oqueprecisamosteremmenteéqueframeworksmodernosquasesemprenos
oferecem,cadaumàsuamaneira,asmesmasfuncionalidades. Apropostadessa
seçãoéapenasperceber,dopontodevistahistórico,comoerao“jeitão”Springde
resolverdependências.
16

## Página 22

CasadoCódigo Capítulo1. AntesdefalardeCDI...
1.6 Buscando as dependências com Seam e anotações
ComoJava5eainclusãodeanotações,ascoisasficarammaisfáceisparaodesenvol-
vedor.Novosframeworkssurgiramcomumafilosofiadiferente,adaconfiguraç ão
simplificada.Enquantoantesaquantidadeexcessivadeconfiguraç ãopermitiauma
extremaflexibilidadeàcustadasimplicidade,anovagera çãodeframeworkspermi-
tiafazermuitomaisconfigurandoapenasoessencialouaexce ção. OJBossSeam
foiumframeworkquenasceucomessafilosofia.Apesardepossuiralgunspassosde
configuração,porjáternascidonaeradasanota ções,elejáerabemmaissimplesde
seutilizar.
OutrodiferencialdoJBossSeamfoiseufocoinicialnaintegraç ão,possívelgra-
çasaoperíodoemqueelesurgiu,poisnessemomentooJavaEEcomoumtodojá
tinhaevoluídomuito,principalmenteatravésdoEJB3eJPA.Issopermitiuumde-
senvolvimentopuroemJavaEEtão,oumaissimplesdoquefazerutilizandoSpring.
DessaformaoSeamnãonasceufocadoemofereceruma stackalternativaaoJava
EEcomofezoSpring,massimemintegrartodasastecnologiasjáexistentesdeuma
formasimpleseelegante,coisaqueaindanãoexistianoJavaEnterprise.
AssimcomonoexemploutilizandoSpring,nãoentraremosnasintegraçõesdo
SeamcomoJavaEE,nemcomoeleauxiliaatratartransa çãoouqualqueroutro
assuntocomumaoSeam,SpringouCDI.OfocoéapenasanalisarmoscomoSeam
trataaquestãodaresolu çãodedependências.
Apesar de ser possível configurar utilizando XML, o Seam já nasceu com
as anotações, então utilizá-las é o mais comum quando usamos esse fra-
mework. Dessa forma, assim como fizemos no XML do Spring (ou faría-
mos no XML do Seam), vamos dar nomes aos beans usando a anotação
@org.jboss.seam.annotations.Name. Além disso, vamos usar também a
anotação @org.jboss.seam.annotations.AutoCreateparaqueobeanseja
automaticamentecriadoquandofordemandado.Semisso,oSeamusaobeandispo-
nívelnoescopooudevolve
null.Porémcomonãoestamosusandoescopos,para
simplificaroexemplo,precisamosdemaisessaanotaç ão.
@Name("calculadoraDeSalarios") @AutoCreate
public class CalculadoraDeSalariosPlano2002
implements CalculadoraDeSalarios{
...
}
@Name("tabelaDeReferenciaSalarial") @AutoCreate
17

## Página 23

1.6. BuscandoasdependênciascomSeameanotações CasadoCódigo
public class TabelaDeReferenciaSalarialPadrao
implements TabelaDeReferenciaSalarial{
...
}
Agora que os beans já possuem nomes, precisamos referenciar a
TabelaDeReferenciaSalarial dentro da CalculadoraDeSalarios.
Paraisso,podemosanotartantoumapropriedadequantoseumétodo settercom
@org.jboss.seam.annotations In. Então, alterando mais uma vez nossa
calculadorateremososeguintecódigo.
@Name("calculadoraDeSalarios") @AutoCreate
public class CalculadoraDeSalariosPlano2002
implements CalculadoraDeSalarios{
@In
public void setTabelaDeReferenciaSalarial(
TabelaDeReferenciaSalarial t){
...
}
...
}
ApesardeficarbastanteparecidocomocódigoCDIqueveremosnodecorrer
destelivro,oSeamtemumasérialimitaç ão. Aresoluçãodadependênciaéfeita
atravésdonomedocomponente,enãopelotipo.Apesardenãotermosespecificado
nenhumnomenaanota ção @In,oSeamconsideraonomedocomponenteaser
injetadocomoigualaonomedapropriedadeanotada.Comoanotamosum setter,
oprefixo“set”éremovidoeaprimeiraletraépassadaparaminúsculoparaobter
onomedapropriedadecorrespondente. Então,naprática,écomosetivéssemos
colocadooseguintecódigo
@In("tabelaDeReferenciaSalarial").
Agoraqueaconfiguraç ãodosbeansestáfeita,precisamosvoltarànossafactory
epedira CalculadoraDeSalariosaocontextodoSeam.
import org.jboss.seam.Component;
public class CalculadoraDeSalariosFactory {
public CalculadoraDeSalarios criaCalculadora(){
CalculadoraDeSalarios calculadora = (CalculadoraDeSalarios )
18

## Página 24

CasadoCódigo Capítulo1. AntesdefalardeCDI...
Component.getInstance("calculadoraDeSalarios");
return calculadora;
}
}
Apesardeusarmosmenosclasses,nãoétãosimplesrodaroSeamdentrodeuma
maincomoconseguimoscomSpring.Noentanto,queroquevocêsefoquenaqua-
lidadedocódigoesimplicidadequeteveonossoprograma,analisandocomosedeu
aevoluçãodesdeoarquivoproperties,passandoporXML,echegandoàanota ção.
Contudo,éimportantesemprelembrarmosqueoSeamusaasanota çõesparacon-
figurarseucontexto,masaligaç ãoentreosbeanséfeitapornomes,enãoportipos
comoénaCDI.
1.7 De onde vimos?
OobjetivodestecapítulofoiintroduzirquestõesbásicasdeOO,quesãoindepen-
dentesdousodeframeworks,masqueaoseremdesprezadaspodenãofazersentido
autilizaçãodeum. Depoispassamosporumbrevehistóricocomaevolu çãoda
resoluçãodedependências,noqualemmomentoalgumtivemosobjetivodecom-
pararosframeworks,jáquecadaumpodeserutilizadodediversasmaneirasenão
necessariamentepararamnopontoemqueforamapresentadosaqui.
Assimcomopodemostirarproveitodeumcarromodernosemnoslembrarmos
daevolu çãodoscarroscarburados,paraainje çãoeletrônica,edepoisosaceleradores
eletrônicos,tambémpodemostirarproveitodaCDIsemessacontextualizaç ãohis-
tórica.Masquandotemosesseconhecimento,entendemosmelhorporquealgumas
coisassãocomosão,etemosumpoucomaisdepoderargumentativo.
19

## Página 26

Capítulo2
OqueéeparaqueserveaCDI
2.1 Para onde v amos?
Nestecapítuloveremosodesafioqueédeixarsimplesdemanterumsistemacom
umaregracomplexa.Taldesafioéodiaadiademuitosdesenvolvedores,eprovavel-
menteemalgummomentopassaremosporele,afinal,pormaisquemuitossistemas
tenhamváriaseváriastelasdecadastro,semprequetemosquelidarcomapartecen-
traldosistema,ondeficasuainteligênciadenegócio,passaremospelosproblemas
aquiapresentados.
2.2 Evitando que a complexidade do código sempre
aumente
Parainiciarnossosestudos,vamostomarcomoexemploumsistemaquecalculao
impostoderendadosfuncionáriosdeumaempresaparainformaràReceitaFederal.
Porém,comonadaésimples,antesprecisamoscalcularosaláriodecadafun-

## Página 27

2.2. Evitandoqueacomplexidadedocódigosempreaumente CasadoCódigo
cionário,eparaissoseráprecisoanalisarcritérioscomo:cargooufun çãoexercida
dentrodaempresa,escolaridade,qualificações,eporfim,umcritérionãomuitouti-
lizadomasqueserveparaenriquecernossoexemplo,otempodeempresa.
Facilmentepercebemosqueesseéumcenáriodecomplexidaderazoável,en-
tãoiremosporpartes.Paracome çarmos,precisaremoscoletarinformaçõesbásicas,
comoosaláriobasedocargooufun ção,aescolaridadedofuncionário,eaescolari-
dadeesperadaparaocargo.
public double calculaImpostoDeRenda(Funcionario funcionario){
double salario = funcionario.getCargo().getSalarioBase();
Escolaridade escolaridadeFuncionario =
funcionario.getEscolaridade();
Escolaridade escolaridadeCargo =
funcionario.getCargo().getEscolaridadeDesejada();
...
}
Aescolaridadedofuncionárioeaescolaridadedocargoservemparaverificar-
mosseeletemosrequisitosesperadosparaafun ção. Issoocorremaisfrequente-
mentequandotemposreformula çõesnoplanodecarreiradeumaempresa.Se,por
exemplo,umcargoexigianívelsuperioredepoispassaaexigirpós-graduaç ão,as
pessoascomnívelsuperiornãoperderãoafun ção,mastambémnãoreceberãoo
mesmosaláriodosnovosfuncionáriosquedeverãosercontratadosseguindoasno-
vasexigênciasecomsaláriosumpoucomaisaltos.
Nonossoexemplo,estamosconsiderandoumavariaç ãode20%(vinteporcento)
tantoparaquemestáabaixodomínimoesperadoparaocargo,quantoparaquem
temescolaridadeacimadoesperado,comoummestradoporexemplo. Ocálculo
dessadiferen çapoderiaserfeitoassim:
//se o funcionário tem escolaridade inferior à esperada para o cargo
if(escolaridadeFuncionario.compareTo(escolaridadeCargo) < 0){
salario = salario * 0.8;
}
//se o funcionário tem escolaridade superior à esperada para o cargo
else if(escolaridadeFuncionario.compareTo(escolaridadeCargo) > 0){
salario = salario * 1.2;
}
Agorairemoscalcularumagratificaç ãoportempodeservi çonaempresa.Usa-
mosumafórmulasimples,naqual,paracadaanotrabalhadodaremosumaumento
22

## Página 28

CasadoCódigo Capítulo2. OqueéeparaqueserveaCDI
de1%(umporcento),eemcasodepermanênciadepelomenos5anosnaempresa,
haveráumaumentoextrade10%(dezporcento).
int anoAtual = getAnoAtual();
int anoAdmissao = funcionario.getAnoAdmissao();
//dá 1% de aumento para cada ano trabalhado na empresa
double anosTrabalhados = anoAtual - anoAdmissao;
double aumentoAntiguidade = anosTrabalhados / 100;
salario = salario * (1 + aumentoAntiguidade);
//se tem mais de 5 anos na empresa tem aumento de 10%
if(anosTrabalhados > 5){
salario = salario * 1.1;
}
Namaioriadasvezesvalemuitomaisumcódigolegíveldoqueumnúmerome-
nordelinhas.Então,nãosepreocupedemaisemfazercontasemumaúnicalinha
comprometendoalegibilidadeeamantenabilidadedoseucódigo.Crievariáveisque
expliquemoqueestásendofeito,esealgoficarmuitogrande,separeemmétodos.
Agoraquejátemososaláriobrutocalculado,precisamosdescontaroimpostode
renda.Nomundorealteríamosmaisdescontos,mascomoestamoscriandonosso
própriouniversodeexemplo,vamosdeixaro
funcionariosermaisfelizeter
menosdescontosnoseusuadosalário.
Noexemploaseguir,utilizaremosatabeladeIRde2013,masosdadosnãoin-
fluenciammuito—omaisimportanteépercebermosoquantonossocódigovai
ficandocomplexo,edepoisveremoscomoresolverisso.
...
//tabela de IR de 2013
double aliquota = 0.0;
double parcelaDeduzir = 0.0;
//ifs estão de forma mais didática, na prática poderiam ser reduzidos
if(salario <= 1710.78){
aliquota = 0.0;
parcelaDeduzir = 0.0;
}
else if(salario > 1710.78 && salario <= 2563.91){
aliquota = 7.5/100;
23

## Página 29

2.2. Evitandoqueacomplexidadedocódigosempreaumente CasadoCódigo
parcelaDeduzir = 128.31;
}
else if(salario > 2563.91 && salario <= 3418.59){
aliquota = 15.0/100;
parcelaDeduzir = 320.60;
}
else if(salario > 3418.59 && salario <= 4271.59){
aliquota = 22.5/100;
parcelaDeduzir = 577.0;
}
else if(salario > 4271.59){
aliquota = 27.5/100;
parcelaDeduzir = 790.58;
}
double impostoSemDesconto = salario * aliquota;
return impostoSemDesconto - parcelaDeduzir;
} //final do método calculaImpostoDeRenda
Ocálculodeimpostoderendanãoéomaissimplesdomundo,mastambémnão
étãocomplicado.Se,porexemplo,tivermosumsaláriodeatéR$ 1.710,78,estamos
isentosdoimposto,massetivermosumsalárioacimadeR$ 4.271,59estaremosna
faixade27,5%doimposto.
MasalguémqueganhaR$ 10.000,00nãovaipagarR$ 2.750,00deIR,quese-
riaovalorguardadonavariável impostoSemDesconto;poisodescontode27,5%
sóincidenaparceladosalárioacimadosR$ 4.271,59. Poressemotivotemosa
parcelaDeduzir,queéovalorquetemosquedescontardessesR$ 2.750,00para
chegarnoimpostocorreto.
Outraformadechegarnoimpostoseriadividirosalárioemcadafaixaecalcular
oimpostoproporcionaldecadaumadelasedepoissomartudo.Masnapráticaépara
issoquea“parcelaadeduzir”faz,jáéocálculoprontodessadiferença.
Juntandotudo,aofinalteríamososeguintecódigo:
public double calculaImpostoDeRenda(Funcionario funcionario){
double salario = funcionario.getCargo().getSalarioBase();
Escolaridade escolaridadeFuncionario =
funcionario.getEscolaridade();
Escolaridade escolaridadeCargo =
funcionario.getCargo().getEscolaridadeDesejada();
24

## Página 30

CasadoCódigo Capítulo2. OqueéeparaqueserveaCDI
// se o funcionário tem escolaridade inferior
// à esperada para o cargo
if(escolaridadeFuncionario.compareTo(escolaridadeCargo) < 0){
salario = salario * 0.8;
}
// se o funcionário tem escolaridade superior
// à esperada para o cargo
else if(escolaridadeFuncionario.compareTo(escolaridadeCargo) > 0) {
salario = salario * 1.2;
}
int anoAtual = getAnoAtual();
int anoAdmissao = funcionario.getAnoAdmissao();
//dá 1% de aumento para cada ano trabalhado na empresa
double anosTrabalhados = anoAtual - anoAdmissao;
double aumentoAntiguidade = anosTrabalhados / 100;
salario = salario * (1 + aumentoAntiguidade);
//se tem mais de 5 anos na empresa tem aumento de 10%
if(anosTrabalhados > 5){
salario = salario * 1.1;
}
//tabela de IR de 2013
double aliquota = 0.0;
double parcelaDeduzir = 0.0;
// ifs estão de forma mais didática,
// na prática poderiam ser reduzidos
if(salario <= 1710.78){
aliquota = 0.0;
parcelaDeduzir = 0.0;
}
else if(salario > 1710.78 && salario <= 2563.91){
aliquota = 7.5/100;
parcelaDeduzir = 128.31;
}
else if(salario > 2563.91 && salario <= 3418.59){
25

## Página 31

2.2. Evitandoqueacomplexidadedocódigosempreaumente CasadoCódigo
aliquota = 15.0/100;
parcelaDeduzir = 320.60;
}
else if(salario > 3418.59 && salario <= 4271.59){
aliquota = 22.5/100;
parcelaDeduzir = 577.0;
}
else if(salario > 4271.59){
aliquota = 27.5/100;
parcelaDeduzir = 790.58;
}
double impostoSemDesconto = salario * aliquota;
return impostoSemDesconto - parcelaDeduzir;
}
Emumcenárioreal,aocalcularosalárioaindapoderíamostermaisvariáveis,
comogratificações,incentivosouumdiferencialporumconhecimentoespecífico,
masnoslimitaraoexemploapresentado.Vocêdevetersesentidodesanimadoem
leressecódigo,pelasuaextensão,diversoscasospossíveisecomplexidade.Imagine
sefosseumaaplicaç ãoreal.
Podemosperceberqueométodo
calculaImpostoDeRendasabemuitacoisa,
equantomaisresponsabilidadesasclassespossuem,maisdifícilémantê-las.
Agoraconsideremosqueparaummétododessetipoestaremproduç ão,elepre-
cisaestartestado.Emaisdoqueisso,eleprecisadetestesautomatizados,poistestes
manuaisalémdetrabalhosostendemanãosertãometódicosereproduzíveis.Mas
comotestarummétodo sabichão? Acreditoqueessesejaumbomcandidatopara
uma“queimadearquivo”,poiselesabedemais.
Mesmoantesdepensarmosemtestar,precisamosorganizaressecálculo.Uma
ótimaideiaseriasepararacalculadoradesaláriosdacalculadoradeIR.Olhandoo
métodocompleto,queéenorme,percebemosduaspartesbemdistintasdentrodele,
claramenteduasoperaçõesdiferentesmasqueestavamjuntasnomesmométodo:o
cálculodosaláriobruto,eocálculodoIR.
Vamosentãocriarumaclassequetemcomoresponsabilidadecalcularsóosa-
láriobruto,assimcasoessaregramude,alteramosessaclasseenãocorremosorisco
dedanificarocálculodoIR,poiselesficarãoindependentesapartirdeagora.
Ocódigoaseguirnósjáconhecemos,sóvamossepará-loemumaclasse:
26

## Página 32

CasadoCódigo Capítulo2. OqueéeparaqueserveaCDI
public class CalculadoraDeSalarios {
public double calculaSalario(Funcionario funcionario){
double salario = funcionario.getCargo().getSalarioBase();
Escolaridade escolaridadeFuncionario =
funcionario.getEscolaridade();
Escolaridade escolaridadeCargo =
funcionario.getCargo().getEscolaridadeDesejada();
// se o funcionário tem escolaridade inferior
// à esperada para o cargo
if(escolaridadeFuncionario.compareTo(escolaridadeCargo) < 0){
salario = salario * 0.8;
}
// se o funcionário tem escolaridade superior
// à esperada para o cargo
else if(
escolaridadeFuncionario.compareTo(escolaridadeCargo) > 0) {
salario = salario * 1.2;
}
int anoAtual = getAnoAtual();
int anoAdmissao = funcionario.getAnoAdmissao();
//dá 1% de aumento para cada ano trabalhado na empresa
double anosTrabalhados = anoAtual - anoAdmissao;
double aumentoAntiguidade = anosTrabalhados / 100;
salario = salario * (1 + aumentoAntiguidade);
//se tem mais de 5 anos na empresa tem aumento de 10%
if(anosTrabalhados > 5){
salario = salario * 1.1;
}
return salario;
}
}
Agoratemosumaclassequesósabecalcularsalários,equeaindapoderiaser
melhorada,separandocadacritériocomoescolaridadeouqualificaç ão,fun çõesou
cargos,eantiguidadesemsubcalculadoras.Estasencapsulariamcadalógicadecál-
culoespecíficaenofinalacalculadorageralcombinariaosresultados.Masfaremos
27

## Página 33

2.2. Evitandoqueacomplexidadedocódigosempreaumente CasadoCódigo
issoemmomentooportuno,oprincipalagoraévermosondeaCDIvainosajudar.
Comaseparaç ão,nossacalculadoradeIRficoubemmaissimples:
public class CalculadoraDeImpostos {
public double calculaImpostoDeRenda(Funcionario funcionario){
CalculadoraDeSalarios calculadora = new CalculadoraDeSalarios();
double salario = calculadora.calculaSalario(funcionario);
//tabela de IR de 2013
double aliquota = 0.0;
double parcelaDeduzir = 0.0;
// ifs estão de forma mais didática,
// na prática poderiam ser reduzidos
if(salario <= 1710.78){
aliquota = 0.0;
parcelaDeduzir = 0.0;
}
else if(salario > 1710.78 && salario <= 2563.91){
aliquota = 7.5/100;
parcelaDeduzir = 128.31;
}
else if(salario > 2563.91 && salario <= 3418.59){
aliquota = 15.0/100;
parcelaDeduzir = 320.60;
}
else if(salario > 3418.59 && salario <= 4271.59){
aliquota = 22.5/100;
parcelaDeduzir = 577.0;
}
else if(salario > 4271.59){
aliquota = 27.5/100;
parcelaDeduzir = 790.58;
}
double impostoSemDesconto = salario * aliquota;
return impostoSemDesconto - parcelaDeduzir;
}
}
28

## Página 34

CasadoCódigo Capítulo2. OqueéeparaqueserveaCDI
Refatoração e testabilidade
Nasaplicaçõesquejátemos,separaressasresponsabilidadesemclas-
sesdistintasnemsempreétãosimples.Podeocorrerdeemumaaplica-
çãosimilarocálculodosalárioedosdescontosiremocorrendodeforma
entrelaçada,umavezpartedeum,outrapartedeoutro.
Nessecasopodeserinteressanteinverteraordemqueusamosaqui,e
casonãoexistam,primeirocriarostestesquegarantamofuncionamento
dométodoquequeremosrefatorar. Depoisdetestado,aísimfaríamos
umarefatoraçãocompleta,separandoasresponsabilidades,eentãousa-
ríamososmesmostestesparagarantirquearefatora çãonãodanificouo
funcionamento.
Somentedepoisqueostestesestivessemtodosverdes(executados
comsucesso)équeaproveitaríamososmétodosdenegóciomaisbem
escritosparamelhorartambémocódigodosnossostestes.
Entendendo mais de testes automatizados
Testedecódigoéumamatériaampla,tatoéquetemosexcelentesli-
vrossobreoassunto[ ?].Assimsendo,oobjetivoaquinãoécobrirtotal-
menteesseassunto,esimfalarumpoucosobrecomoissoéimportante
nodesenvolvimentodesoftware.
ACDInãoamarranossoprojetodeclasses,nosdandoliberdadepara
umprojetobemtestável.Noentanto,emalgunsmomentosprecisamos
maisdoquetestesdeunidade,comotestesdeintegraç ãoedesistema.
Quandopassamosparaostestesdeintegraç ão,ferramentascomoCDI
costumamdartrabalho,masnocapítulo 9veremoscomoissopodeser
feitosemmuitotrabalho.
Agorasimpodemospartirparaostestes.Vamosconsiderarumfuncionáriocom
saláriodeR$3.000,00.TeremosqueverificarseoimpostodelefoideR$ 129,40,pois
elecaiunaalíquotade15%esuaparcelaadeduzirédeR$ 320,60.Nãoparecemuito
complicado,nãoéverdade?Seriaalgoparecidocomoseguintecódigo.
@Test
29

## Página 35

2.2. Evitandoqueacomplexidadedocódigosempreaumente CasadoCódigo
public void testaCalculoIRNaSegundaFaixaDeContribuicao(){
Funcionario funcionario = new Funcionario();
funcionario.setSalario(3000.0); // esse método não existe
CalculadoraDeImpostos calculadora =
new CalculadoraDeImpostos();
//a calculadora de IR usa outra classe para calcular o salário
double impostoDeRenda =
calculadora.calculaImpostoDeRenda(funcionario);
Assert.assertEquals(129.4, impostoDeRenda, 0.0001);
}
OdetalheéqueessesaláriodeR$ 3.000,00nãopodeseratribuídoassim,ele
écalculadopela CalculadoraDeSalariosdentrodocálculodoIR.Issoquer
dizerquetemosdoiscálculosacontecendodentrodomesmoteste,eissopodecausar
confusão.
Nonossocaso,teríamosqueconfiguraro funcionariocomdadosquesa-
beríamos que ao final do cálculo do salário bruto, teríamos R$3.000,00 como
resultado. Maspodeocorrerdeconfigurarmosofuncionáriocorretamenteea
CalculadoraDeSalariosdefalhar,devolvendoumvalorerrado. Então,esta-
ríamostestandooimpostoachandoqueosaláriobrutoera 3000.0masnaprática
ovalorseriaoutro,eotestefalharia.
O pior nesse exemplo é que o teste que estamos escrevendo chama-se
testaCalculoIRNaSegundaFaixaDeContribuicao,entãoseelefalhar,apri-
meiracoisaqueviráàsnossasmenteséqueocálculodoIRestácomproblemas,e
nãoqueoerrofoinocálculodosalário.Mascomolidarcomessescasos?
Poderíamos nesse ponto ser um pouco impulsivos e sair alterando a assi-
natura do método que calcula o imposto de renda para este receber o salário
jácalculado, apenasum
double, eentãoeliminaríamosadependênciacoma
CalculadoraDeSalariosnosnossostestes.
Essapodeser,sim,umadassolu ções,masveremosquetemosoutrasmaisapli-
cáveisaqualquermodelo.Alémdomais,seformostentarmudarasassinaturasdos
nossosmétodosparareceberdadosmaisindependentes,jáprocessados,empouco
tempoestaremostrabalhandosomentecomtipossimplesdedados(primitivose
wrappers),eacabaremoscomaOO,quetemcomobaseacolabora çãoentreobjetos.
Asoluçãomaisadequadaparapromoveratestabilidadedonossocódigosem
30

## Página 36

CasadoCódigo Capítulo2. OqueéeparaqueserveaCDI
feriraOOéousoda InjeçãodeDependências,ou Dependency Injection (DI)em
inglês.
2.3 Introdução à injeção de dependências
Ainje çãodedependênciasémuitoimportanteparatermosumsistemamaissimples
demanter.Apesardeparecerquesuaprincipalvantageméajudarnostestes,issona
verdadeésóumaformadepercebermossuarealvantagem,queéafacilidadeem
trocarpe çasdonossosistemadiminuindomuitoapossibilidadedequebra.Vamos
voltaraonossoexemploparaentendermosmelhorcomoissofunciona.
public class CalculadoraDeImpostos {
private CalculadoraDeSalarios calculadoraSalarios;
public CalculadoraDeImpostos(CalculadoraDeSalarios calculadora){
calculadoraSalarios = calculadora;
}
public double calculaImpostoDeRenda(Funcionario funcionario){
double salario = calculadoraSalarios.calculaSalario(funcionario);
//resto do método continua igual
}
}
A principal mudança no desenho das classes é o que fizemos na
CalculadoraDeImpostos. Na versão anterior de seu código, essa classe
instanciavadiretamenteaclasse CalculadoraDeSalarios,eassimnãoconse-
guíamosdeumaformasimplesinterferirnarela çãoentreumaclasseeoutra.Agora,
apesardesutil,amudan çaépoderosa;poisaclassequeantesativamenteresolviaa
dependênciaagoraesperapacientementequealguémlhesupraessadependência.E
quandoessealguém(nósmesmosouum fr a mewo r k)passaessadependênciaparaa
classequenecessita,dizemosqueeleestáinjetandoadependênciaemquemprecisa.
Nesse primeiro momento nós mesmos estaremos passando para a
CalculadoraDeImpostos a instância de CalculadoraDeSalarios que
elanecessita,ouseja,ainje çãodedependênciaserámanual,maséaquiqueaCDI
atuará, suprindo“automaticamente”essasdependências. Veremosmaisàfrente
31

## Página 37

2.3. Introduçãoàinje çãodedependências CasadoCódigo
que,apesardasaspas,esseprocessoétãosimplesquepoderemos,sim,nagrande
maioriadoscasos,considerá-loautomático.
Jáfizemosasalteraçõesnaclassequepossuiadependência,agorafaltaalterar
nossotesteparainjetaressadependênciadaformacorreta.
@Test
public void testaCalculoIRNaSegundaFaixaDeContribuicao(){
Funcionario funcionario = new Funcionario();
funcionario.setSalario(3000.0); //esse método não existe
CalculadoraDeSalarios calculadoraSalarios =
new CalculadoraDeSalarios();
CalculadoraDeImpostos calculadoraImpostos =
new CalculadoraDeImpostos(calculadoraSalarios);
//a calculadora de IR usa outra classe para calcular o salário
double imposto =
calculadoraImpostos.calculaImpostoDeRenda(funcionario);
Assert.assertEquals(129.4, imposto, 0.0001);
}
Essepassofoiapenasdidático,poisnãoeliminanossoproblema,apenasmostra
comodevemosmontarainstânciade CalculadoraDeImpostos.Paraobtermos
umavantagemdeverdade,precisaremostrocaracalculadoradesalários.Criaremos
umanovaclasseparasubstituira CalculadoraDeSalarios,eessanovaclassevai
servirsomenteparanossostestes. Emvezdecalculardeverdade,elavaidevolver
ovalorqueespecificarmos,assimnãoteremosmaisadependênciaentreasduas
calculadorasdentrodomesmoteste.
public class CalculadoraDeSalariosMock extends CalculadoraDeSalarios {
private double salarioFixo;
public CalculadoraDeSalariosMock(double salarioFixo){
this.salarioFixo = salarioFixo;
}
public double calculaSalario(Funcionario funcionario){
return salarioFixo;
}
}
32

## Página 38

CasadoCódigo Capítulo2. OqueéeparaqueserveaCDI
Na classe CalculadoraDeSalariosMock nós estendemos a classe
CalculadoraDeSalarios e sobrescrevemos o método calculaSalario
paraqueelefuncionedaformaquedesejamos. Éumservi çograndeparaum
resultadosimples,masnãosepreocupe,existemframeworksquefazemissosema
necessidadedecriarmosumanovaclasse,um M o c k.
Criação simplificada de Mocks com frameworks
Mockssãoobjetos“burros”,programadospararesponderexatamente
comoprecisarmosemcadasituaç ão.Nonossoexemplomandamosele
simplesmenteretornarumvalor,independentementedoqueométodo
calculaSalariosemanticamenterepresenta.
ExistemframeworksquefacilitambastanteotrabalhocomooMoc-
kito,queseráusadonoscódigosdeexemploapartirdocapítulo 10.
Apesardotrabalhoamais,fazeressaclassenosmostraquesetivéssemosdefi-
nidoa CalculadoraDeSalarioscomoumainterface,enãocomoumaclasse,
nosso M o c kficariasemanticamentemelhor.Omockemsinãoéumproblemapois
nofuturovamosusarumframeworkparacriá-losobdemanda,mascasoprecisemos
emumdeterminadomomentoalteraraformadecalcularossalários,porexemplo
depoisdeumnovoplanodecargosesalários,poderemoscairnomesmoproblema
quevemosnoexemplo.
Princípiodasubstitui çãodeLiskoveousodeinterfaces
Quandoprecisamostrocarumobjetoporoutro,comonocasotrocamosnossa
calculadorarealpelomock,enocasodeumnovoplanosdecargos,aplicamoso
PrincípiodasubstituiçãodeLiskov,segundooqualoobjetomockconsegueperfei-
tamentesepassarpeloobjetoreal.
Percebaporémqueparafazermosissofuncionarfoiprecisoqueomockseja
subclasseda
CalculadoraDeSalarios,oquedopontodevistasemânticonão
temsentidoalgum.Novamenteimaginemosissoaplicadonocasodacriaç ãodeum
novoplanodecargos,emqueaimplementaç ãooriginalserádesprezada,maspara
queconseguíssemosfazeranovacalculadorasubstituiraprimeira,precisaríamos
queestafossesubclassedaprimeira. Casousássemosumainterfacenãoteríamos
esseproblema.
33

## Página 39

2.3. Introduçãoàinje çãodedependências CasadoCódigo
Apósentendermosumpoucomaissobrecomoumobjetosubstituioutro,vamos
aplicarissononossoteste.
@Test
public void testaCalculoIRNaSegundaFaixaDeContribuicao(){
Funcionario funcionario = new Funcionario();
CalculadoraDeSalarios calculadoraSalarios =
new CalculadoraDeSalariosMock(3000.0);
CalculadoraDeImpostos calculadoraImpostos =
new CalculadoraDeImpostos(calculadoraSalarios);
//a calculadora de IR usa outra classe para calcular o salário
double imposto =
calculadoraImpostos.calculaImpostoDeRenda(funcionario);
Assert.assertEquals(129.4, imposto, 0.0001);
}
Agorasimtemosumcódigofuncionando.Criamosmanualmenteummockuti-
lizandooprincípiodasubstituiç ãoeinjetamosessemockcomodependênciada
CalculadoraDeImpostos. Nadamalparauminício. Acreditoquefoipossível
perceberoquantoalgosimples,comoainje çãodedependências,podefazeruma
diferençanamodularidadedonossosistema,trocandoumaclasseporoutrasem
queasclassesclientespercebam.
34

## Página 40

CasadoCódigo Capítulo2. OqueéeparaqueserveaCDI
Princípio deLiskov
Esseprincípiodescreveoqueénecessárioparafazerumobjetoser
aceitonolugardeoutro.Basicamenteonovoobjetotemqueserumsub-
tipo,ouemJavaimplementaramesmainterfacequeoprimeiro.Além
disso,osmétodosdasubclassetêmqueaceitar nomínimo tudoqueo
métododasuperclasseaceita,edevolver nomáximooqueoprimeiro
devolvia.
Comoexemplo,podemosconsiderarummétodoquerecebaede-
volvanúmeros. Seaclasseoriginalaceitaapenasnúmerospositivos,a
novaclassetemquenomínimoaceitartodososnúmerosqueaprimeira
aceitava,masseelaaceitartambémosnúmerosnegativosnãotempro-
blema. Nessecaso,provavelmentenumprimeiromomentoaop çãode
enviarnúmerosnegativosnãoseráusadapelosistema,vistoqueelejá
estácondicionadoàprimeiraclassequesóaceitanúmerospositivos.Já
seanovaclasseaceitarmenosqueaoriginal,porexemplosomentenú-
merosmaioresquemil,osistemapodepassarparaessanovaclasseo
número50,poiscomaclasseoriginalerapossível,masnanovaissoge-
rariaumerroemtempodeexecuç ão.
Arespeitodoretorno,oprincípioéoinverso:seaclasseoriginalre-
tornasomentenúmerospositivos,podemosnomáximodevolverosnú-
merospositivosnanovaclasse.Issoporqueosistemajávaiestarcondici-
onadoaesperarapenasnúmerospositivos,entãoaoretornarumnúmero
negativopoderíamosterumerroemtempodeexecu ção.Agoraseretor-
narmosumaquantidadeaindamaisrestritaderesultadosnãoteremos
problema,comoretornarapenasvaloresmaioresquemil.
Épossívelpercebermosquequantoàtipagem,aslinguagensdepro-
gramaçãodãocontadorecado,jáasrestri çõesdeentradaesaídados
métodosnamaioriadasvezesprecisamsertratadaspelodesenvolvedor,
eporissopodemosconsiderarqueainterfacedeumaclassenãoésóa
assinaturadeseusmétodos,mastambémasrestri çõesque,quandoexis-
tirem,devemestarespecificadasviaJavaDocououtraformaefetivade
documentação.
35

## Página 41

2.4. AmotivaçãodaCDI CasadoCódigo
2.4 A motiv ação da CDI
Nossoexemploatéaquifoisimples,masconformeeleforaumentandosentiremos
cadavezmaisanecessidadedealgumgerenciadordessasdependências.
Omaisimportantenessecapítulo,épercebermosqueconformeosistemacresce,
evamosnospreocupandoemantê-loorganizadoetestado,vaisurgindoanecessi-
dadedeumauxílio.
Precisamosdeumaferramentaquenosdêapossibilidadedemontarnossosob-
jetosapartirdeoutros,comoum“lego”.Porémessaferramentapreferencialmente
precisanoslivrardeconfiguraç õesmorosas,cheiasdeXML;etambémdeconfigura-
çõessimples,comanotaç ões,masquenãoconseguemanalisarostiposdosobjetos,
comovimosnase ção1.3.EéaquiqueentraaCDI.
ACDIéumaespecificaç ãoJava,cujonomecompletoé“ContextandDepen-
dencyInjectionforJavaEE”[?],mascomopodemospercebero“forJavaEE”não
entranasigla.Defato,conformeformosnosaprofundandonoassunto,vamosper-
ceberqueaCDInãoéapenasparaoJavaEE,mastambémparaoJavaSE.
SevocêestáiniciandonouniversoJava,podeserquenãoestejahabituadocom
otermo“especificação”,masfiquetranquilo,trataremosdissologoaseguir.Epara
nosajudaralembrarsemprequeestamosfalandodeumaespecifica ção,procurarei
sempremereferiràCDInogênerofeminino.Poisnãofalamosdeumframework,e
simdeumaespecificaç ão.
2.5 O que é e para que serve uma especificação?
Apesardoconvencimentodarealnecessidadedealgosóvirquandonosdepara-
moscomcasosmaiscomplexos,comosexemplosapresentadospercebemosquehá
vantagemnousodainje çãodedependência,enodecorrerdolivroteremoscerteza
disso. Tantoqueumindicadordaimportânciadeumamatériaéaquantidadede
pessoastentandoresolverseusproblemas.
Quandooassuntoéinje çãodedependência,temosnoecossistemaJavaalgumas
opçõesdeframeworks,sendoosmaisconhecidosemodernosoSpringFramework
eoJBossSeam,jáapresentadosnase ção1.3.
Apesardeseremduasboasferramentas,SpringeSeamsãoframeworksdiferen-
tes,eadotandoqualquerumdosdoisamudan çaparaoutroframeworkquefa çaa
mesmatarefaémuitocustosa,nãovalendoapena.Dessaformacasooframework
queestivermosutilizandocomeceaapresentarumnívelelevadodebugsoutenha
36

## Página 42

CasadoCódigo Capítulo2. OqueéeparaqueserveaCDI
seudesenvolvimentodescontinuado,nossaaplicaç ãocorresériosriscosdeficarde-
satualizadaouterfalhasgraves.
Poressemotivosurgemasespecificaç ões.Elasdefinemcomoumadeterminada
funcionalidadedevesecomportareosimplementadores(empresas,funda ções,gru-
posdeusuários,indivíduosetc)têmliberdadedeimplementardamaneiraquede-
sejarem,desdequeaespecificaç ãosejaseguida.
Naprática,elaéumdocumentotextoqueespecificacadafuncionamentoes-
peradodosoftwarequeaimplemente. Comissotemosafacilidadedeescolhera
implementaçãoquemaisnosagradar,ecasoamesmasejadescontinuadaousua
qualidadenãonossatisfaç amais,podemostrocardeimplementaç ãocompoucoes-
forço,vistoqueviaderegraocomportamentodetodaselasdeveserigualoubem
parecido.Eparagarantirqueessefuncionamentosejapadrão,existeumabateriade
testesquesãoaplicadosaumaimplementaç ãoquequeirasecertificarcomoaderente
àespecificação.
ACDI—ContextandDependencyInjectionforJavaEE—éaespecificaç ão
queregecomodevefuncionarosframeworksdeinje çãodedependênciasparaa
plataformaJava.Dessaforma,agoratemosumamaiorliberdadedeescolhanaim-
plementação,emesmoframeworksquenãoaimplementamacabamtendoumcom-
portamentoparecidocomodaespecificaç ão,paraquesejapossívelreutilizaroco-
nhecimentoeatémesmocódigovindodeaplicaçõesfeitascomimplementaç õesde
CDI.
QuandoestivermosestudandoespecificamenteaCDI,veremosqueelatrouxe
umainovaçãoemrelaç ãoàsoutrasespecificações.Émuitocomumumaimplemen-
taçãotrazerfuncionalidadesamaisdoqueaespecificaç ãodetermina,poisaveloci-
dadedademandadacomunidadeésuperioràdocomitêqueevoluiasespecificações.
Issoémuitobompoistemosnovidadesemumavelocidademaior,masquandouti-
lizamosessasfuncionalidadesnãoespecificadas,acabamosnosprendendoauma
implementaçãoespecífica,poisumaoutraimplementaç ãopodenãotertalfuncio-
nalidadeoutê-ladeformadiferente.
Porserissocomum,aCDIjáespecificoucomocriarextensõesportáveisentre
implementações,comissoseestivermosutilizandooWeld(daJBoss),implementa-
çãodereferência,equisermosmudarparaaOpenWebBean(daApache),poderemos
levarparaessasegunda,asextensõesdesenvolvidaspelaprimeira,desdequetaisex-
tensõessejamimplementadasseguindoasregrasdeportabilidade.Érealmentealgo
muitointeressanteequefazfaltaemoutrasespecificaç ões. Nocapítulo9veremos
especificamentesobreessasextensões.
37

## Página 43

2.6. ACDIésóparaJavaEEmesmo? CasadoCódigo
2.6 ACDI é só paraJa v aEE mesmo?
Apesardeseunome, Context and Dependency Injection for Java EE,aCDIéumaes-
pecificaçãoquepodeserutilizadaemambiente Enterpriseouemambiente Standard,
comodentrodeumTomcat,Jetty,ouatémesmoemumaaplicaç ãoDesktop.Esse
nomenãoquerdizerondeaCDIroda,massimondeelavemprontaparauso,que
nocasoénoambienteJavaEE,tantonoprofileFullquantonoWeb.
Atéaversão5,oJavaEEeraumacole çãoenormedeespecificaçõesque,juntas,
nospermitemdesenvolverosmaisvariadostiposdeaplicaç ão,mastinhamuitomais
funcionalidadesdoqueagrandemaioriadasaplicaç õescostumausar. Porisso,a
partirdaversão6,oJavaEEpassouaterdiferentesperfis:oFulleoWeb. OFull,
oucompleto,éoequivalenteàcole çãodoJavaEE5emaisalgumasespecificações
novas,dentreelasaCDI.JáoperfilWebéumsubconjuntodessasespecificações,
contendoapenasasespecificaçõesmaisúteisparaasaplica çõesmaiscomuns.
Acontecenoentantodehaveraplicaçõesqueusamaindamenosrecursosdoque
osdisponibilizadosnoperfilWebdoJavaEE,comoumaaplicaç ãoqueutilizeJSFe
JPA[?].Essetipodeaplicaç ãoprecisaapenasdeum Servlet Container,eapesarde
serumaaplica çãoweb,nessecasoconsideramosqueelaestásobreaplataformaJava
SE.Logo,nãopodemosconfundiraplicaçõesJavaSEcomaplica çõesDesktop,mas
aCDIpodeserutilizadaemambos.
38

## Página 44

Capítulo3
IniciandoumprojetocomCDI
NoscapítulosanterioresapenasiniciamosaconversasobreCDI,queobviamente
vaidurartodoesselivro. Masagora,nessesprimeiroexemplos,jáconseguiremos
entenderumpoucomaisdosmotivosquefazemdaCDIumaótimaalternativapara
utilizarmosnosnossosprojetos.
OsexemplosdesselivroserãobaseadosnaIDENetbeans,enoservidordeapli-
caçãoGlassFish4,mastodososconceitossãoindependentesdeIDEedeServidor.
Utilizaremostambémaimplementaçãodereferência,Weld,mastodaimplementa-
çãocertificadadevefuncionardeformasemelhante.
Parafacilitaropassoapasso,vocêpodeclonaresserepositórionoGithub: https:
//github.com/gscordeiro/livro-cdi.
3.1 Ol á CDI
Vamosaproveitaroexemploda CalculadoraDeImpostosvistoanteriormentee
agoravamoscolocá-laparafuncionarcomaCDI.Iniciaremoscomuma Servlet,que

## Página 45

3.1. OláCDI CasadoCódigo
éumaclasseJavaquerodanoservidoreéalcan çável por umaURL.Esseprimeiro
códigoteráobjetivoapenasdidático,nãovaifazerpartedaversãofinaldosistema.
Parainiciar,faç aodownload(https://netbeans.org/downloads)daversãoJava
EEoudaversãoFull(Tudo)donetbeans,poisassimjávirácomoservidorGlassFish
4.ComaIDEaberta,crieumaaplicaç ãoWebelheatribuaumnome.Quandofor
perguntado,informequeseráumaaplicaç ãoJavaEE7.
CasoestejausandoEclipse,vocêpodeadicionaroservidoraocriarumnovo
projeto,indoem“New>DynamicWebProject”edêaoprojetoonomequepreferir.
Logoapósespecificaronomedoprojeto,vocêpoderáescolheroservidor(Target
runtime).
IremosiniciarnossoexemplocomumaServlet.AsIDEspossuemformasespe-
cíficasparaacriaç ãodeServlets,masnadaquefujamuitodeumcliquecomobotão
direito,escolheracriaç ãodeumanovaServleteatravésdewizardespecificarqual
padrãodeurlequaismétodospretendemosutilizar.Nonossoexemploespecifica-
mosrespectivamente
/hello-cdieométodo doGet.
@WebServlet("/hello-cdi")
public class IniciandoComCDI extends HttpServlet {
@Inject
private CalculadoraDeImpostos calculadoraImpostos ;
public IniciandoComCDI() {
System.out.println("Instanciando a Servlet..." );
}
@PostConstruct
public void ok(){
System.out.println("Servlet pronta.");
}
protected void doGet(HttpServletRequest req,
HttpServletResponse res)
throws ServletException, IOException {
double salarioBase =
Double.parseDouble(req.getParameter("salario"));
Funcionario funcionario = new FuncionarioBuilder()
40

## Página 46

CasadoCódigo Capítulo3. IniciandoumprojetocomCDI
.comSalarioBaseDe(salarioBase)
.build();
System.out.println("Efetuando o cálculo.");
//a calculadora de IR usa outra classe para calcular o salário
double imposto =
calculadoraImpostos.calculaImpostoDeRenda(funcionario);
res.getOutputStream().print(
String.format("Salario base: R$ %.2f\n" +
"Imposto devido: R$ %.2f", salarioBase, imposto));
System.out.println("Fim.");
}
}
Nãomeimporteiemescreverdiretamentenoconsole(saídapadrão)daaplica-
ção.Aléméclarodeescrevernatelaoresultadodocálculo.
OpteiporumaservletporestaseraAPImaisbásicadoJavaparaaWeb,dessa
formanãoprecisamosdemuitoconhecimentoacumuladoparaentenderoexemplo.
Perceba que esse código faz uso das mesmas classes utilizadas no
testaCalculoIRNaSegundaFaixaDeContribuicao, então não se pre-
ocupe em entender o sentido do cálculo, e sim a dinâmica de resolução das
dependências.
Como já estamos utilizando aCalculadoraDeImpostos junto com a
CalculadoraDeSalarios,sem mocks,precisamoscriarumfuncionáriodever-
dade,eporissoutilizamosaclasse FuncionarioBuilder,quefacilitaoprocesso
decriaçãodesseobjeto.
public class FuncionarioBuilder {
private int anoAdmissao;
private Escolaridade escolaridadeFuncionario;
private Escolaridade escolaridadeCargo;
private double salarioBase;
public FuncionarioBuilder() {
escolaridadeCargo = Escolaridade.SUPERIOR;
escolaridadeFuncionario = Escolaridade.SUPERIOR;
41

## Página 47

3.1. OláCDI CasadoCódigo
anoAdmissao = Calendar.getInstance().get(Calendar.YEAR);
}
public FuncionarioBuilder comSalarioBaseDe(double salarioBase){
this.salarioBase = salarioBase;
return this;
}
public Funcionario build(){
Cargo cargo = new Cargo(salarioBase, escolaridadeCargo);
return new Funcionario(cargo,
escolaridadeFuncionario,
anoAdmissao);
}
}
Essecódigoénecessáriopoisacriaç ãodoFuncionárioenvolveacriaç ãode
Cargo,ecomoprecisaremoscriarumfuncionáriodiversasvezes,comonostes-
tes,amaneiradefacilitaracriaç ãodosobjetoscomoqueremoséviaessaclasse,que
implementaopadrão builder.
Na CalculadoraDeImpostos,apenasadicionamosaanotaç ão @Injectno
construtorparaqueaCDIsaibaqueprecisainjetaressadependênciaparanós.Fora
isso,assimcomojávimosnocódigodaservlet,utilizamosummétodopúblicoesem
argumentosanotadocomaanotaç ão
@PostConstruct,queéchamadopelaCDI
semprequeoobjetoestápronto,ouseja,játevetodassuasdependênciassatisfeitas.
import javax.annotation.PostConstruct;
import javax.inject.Inject;
public class CalculadoraDeImpostos {
private CalculadoraDeSalarios calculadoraSalarios ;
@Inject
public CalculadoraDeImpostos(CalculadoraDeSalarios calculadora){
System.out.println("Iniciando Calculadora de impostos..." );
calculadoraSalarios = calculadora;
}
42

## Página 48

CasadoCódigo Capítulo3. IniciandoumprojetocomCDI
@PostConstruct
public void init(){
System.out.println("Calculadora de impostos pronta!" );
}
//resto do código permanece igual...
}
Tambémparafacilitaraanálisedasequênciadaresoluç ãodasdependênciasé
quealteramosumpoucoa CalculadoraDeSalariosparaescrevernoconsole
quandoelacome çaaserinstanciadaequandoelaestiverpronta.
import javax.annotation.PostConstruct;
public class CalculadoraDeSalarios {
public CalculadoraDeSalarios() {
System.out.println("Iniciando Calculadora de salários..." );
}
@PostConstruct
public void init(){
System.out.println("Calculadora de salários pronta!" );
}
//resto do código permanece igual...
}
Ainda existe um detalhe antes de executarmos nosso exemplo. Como
criamos uma classe CalculadoraDeSalariosMock que estende a
CalculadoraDeSalarios, quando a CalculadoraDeImpostos solicitar
adependênciaviaseuconstrutor,aCDIficaráemdúvidadequalimplementaç ão
utilizarparasatisfazeradependência,seacalculadorarealouamock,poisambas
têm tipos compatíveis com a dependência. Por isso colocaremos a anotação
@Vetoednaclassemock,indicandoàCDIqueessaclassenãodeveserconsiderada
umacandidataàresoluç ãodedependências.
import javax.enterprise.inject.Vetoed;
43

## Página 49

3.1. OláCDI CasadoCódigo
@Vetoed
public class CalculadoraDeSalariosMock extends CalculadoraDeSalarios {
//conteúdo permanece igual
}
Casoestejautilizandoaversão1.0daCDI,emqueestaanota çãonãoestádispo-
nível,vocêpodeusaraanotaç ão @javax.enterprise.inject.Alternative
nolugarda @Vetoed.Essaanota çãotambémmarcaobeancomonãoelegívelem
umprimeiromomento,masnospermitereativá-loposteriormenteviaconfiguraç ão.
Masnãosepreocupecomessaanota çãoporenquanto,veremosmaisdetalhesdela
nase ção4.3.
Agora, analisando as classes CalculadoraDeImpostos e
CalculadoraDeSalarios podemos perceber algo interessante, elas não
precisamdenenhumaanota çãoparaqueaCDIasdetecteeconsigautilizá-las.
Tantoéquetivemosquecolocarumaanota çãonomockparaqueelatambémnão
fosseconsideradaautomaticamente. Foraessa,aoutraanota çãoquetemoséada
Servlet,queestáaliporqueprecisamosmapearumpadrãodeurlparaela,enãopor
causadaCDI.
Seexecutarmosoexemploatravésdaseguinteurl: http://localhost:8080/livro-cdi/
hello-cdi?salario=3000,teremosesseresultado.
Figura3.1:HelloworldcomCDI
Podemosverqueoresultadofoiomesmodostestesvistosantes,masoresultado
nãoéomaisimportante,oprincipalobjetivoéentendermoscomooprocessotodo
funciona.Seanalisarmosasaídanoconsoledaaplicaç ão,teremosalgocomoisso:
Instanciando a Servlet...
Iniciando Calculadora de salários...
44

## Página 50

CasadoCódigo Capítulo3. IniciandoumprojetocomCDI
Calculadora de salários pronta!
Iniciando Calculadora de impostos...
Calculadora de impostos pronta!
Servlet pronta.
Efetuando o cálculo.
Fim.
Comesseexemplobemsimplesjáconseguimosperceberadinâmicabásica
daresolu ção de dependências. Ao instanciar a ServletIniciandoComCDI, a
CDIpercebeuqueelaprecisavadeumainstânciade CalculadoraDeImpostos,
eporissologodepoisdeinstanciaroprimeiroobjeto, jácome çouaproviden-
ciarsuadependência. Porém,pormaisqueaServletnãotenhaumadependên-
ciadiretada CalculadoraDeSalarios, semestanãoépossívelinstanciara
CalculadoraDeImpostos.
Comoutilizamosainje çãoda CalculadoraDeSalariosnoconstrutorda
CalculadoraDeImpostos,nãotemcomoaCDIiniciarainstanciaç ãodestaen-
quantoaquelanãoestiverpronta. Apenasdidaticamente,sefizéssemosaseguinte
alteraçãoteríamosumasaídadiferente:
import javax.annotation.PostConstruct;
import javax.inject.Inject;
public class CalculadoraDeImpostos {
@Inject
private CalculadoraDeSalarios calculadoraSalarios;
public CalculadoraDeImpostos(){
System.out.println("Iniciando Calculadora de impostos..." );
}
@PostConstruct
public void init(){
System.out.println("Calculadora de impostos pronta!" );
}
//resto do código permanece igual...
}
45

## Página 51

3.1. OláCDI CasadoCódigo
Apósessaalteraç ão,asaídanoconsoleseriaaseguinte:
Instanciando a Servlet...
Iniciando Calculadora de impostos...
Iniciando Calculadora de salários...
Calculadora de salários pronta!
Calculadora de impostos pronta!
Servlet pronta.
Efetuando o cálculo.
Fim.
Podemos perceber que a CDI resolve a ordem em que os objetos precisam
serinstanciados. Depoisdeinstanciara CalculadoraDeSalarios,elaéinje-
tadana CalculadoraDeImpostos,ecomoessaerasuaúnicadependência,a
CalculadoraDeImpostoséavisadaqueestápronta,atravésdeseumétodoano-
tadocom @PostConstruct. Agoraqueestácompleta,elaéinjetadanaServlet,
quetambéméavisadaqueestápronta.Somentedepoisdoambienteprontoéquea
requisiçãoéatendidaeocálculoéefetuado.
Comoobservamosnoexemplo,parasolicitarainje çãodeumadependência
bastautilizarmosaanota ção @javax.inject.Inject.DessaformaaCDIpro-
curaemseucontextoumaclassecandidataasupriressadependência,ecomopor
padrãotodaclassedentrodeumpacoteCDIécandidataaserinjetada,nãopre-
cisamosfazernenhumaconfiguraç ãonasclasses. Veremosqueemalgunscasosé
interessanteespecificarmosalgumascaracterísticasadicionais,masissoéaexce ção,
poiso defaultjánosserveparaamaioriadoscasos. Defaultsinteligentessãouma
dasmarcasdaCDI.
46

## Página 52

CasadoCódigo Capítulo3. IniciandoumprojetocomCDI
O uso do@PostC onstruct
QuandousamosCDI,oumesmooutroframeworkquegerenciaas
dependênciasdasnossasclasses,precisamosficaratentossobreofatode
queométodoquerepresentaainstanciaç ãoemsinãoéachamadado
construtor,esim,ométodoanotadocom @PostConstruct,poisna
invocaçãodessemétodosimtemoscertezaqueoobjetoestápronto.
Então, sepretendíamosfazeralgumaprogramaç ão no construtor,
podeserinteressantefazerno @PostConstruct,poisnele,indepen-
dentementeseainje çãodedependênciafoiviaconstrutor,métodoini-
cializadoroudiretamentenaspropriedades,saberemosqueoobjetoestá
pronto.Éumaespéciedeconstrutorlógicodoobjeto.
Umexemplodissoéquandotemosserializaç ãodeumobjeto,como
napassivaçãodeumEJB.Podeserqueocontainerserializeoobjeto
quandoelesetornainativoedepoisoretorneparaamemóriaquando
eleforusadonovamente.Quandoissoocorre,umanovainstânciaécri-
ada,econsequentementeseuconstrutorprecisaráserinvocado,poisé
o construtor físico,jáométodoanotadocom
@PostConstruct, cons-
trutor lógico,nãoseráinvocado,poistrata-sedomesmobean. Elenão
estásendoconstruído,criadonaquelemomento,sóestáretornandoao
estadooriginal.
3.2 O que é um pacoteCDI?
Acabamosdeverque,porpadrão,todaclassedentrodeumpacoteCDIéelegível
parasuprirumadependência.MasoqueéumpacoteCDI?Eaquelasclassesutili-
táriasquenósjátemosprontasdentrodeumjar,comopodemosinjetarinstância
delasdentrodanossaaplicaç ão?
Comoestamostrabalhandocomumaaplicaç ãoWeb(war),bastacolocarmos
umarquivochamado
beans.xmldentrodapasta WEB-INFdanossaaplicaç ão.
Agorasetiverumjarsimplesouejb-jar,colocamosessearquivodentrodapasta
META-INFepronto,aconfiguraç ãodaCDIestápronta.
Nessepontopodemosnosperguntar:maseasconfigura çãodaCDI,ondecolo-
camos?
Arespostaestánovamenteem defaultsinteligentes.Comoatéaquinãoprecisa-
47

## Página 53

3.3. Usandoinjeçãoempropriedades,construtoresemétodosinicializadores CasadoCódigo
mosfazerconfiguraç ãoalguma,nãoprecisamossequerdefinirumaestruturaxml
mínimadentrodessearquivo.Bastaqueeleexistacomessenome,mesmoestando
vazio,queaCDIjácome çaafuncionar.
Somentequandoprecisarmosconfiguraralgoespecífico,équenospreocupare-
mosemporalgodentrodoarquivo.
Atéagoraaestruturadanossaaplicaç ãoestáparecidacomadaimagemaseguir.
Figura3.2:Estruturadaaplicaç ãoearquivobeans.xmlvazio
3.3 Usando injeção em propriedades, construtores
e métodos inicializadores
Jásabemosqueparainjetarumrecursodentrodanossaclasseéextramentesimples,
bastafazermoscomonoexemplo:
public class CalculadoraDeImpostos {
48

## Página 54

CasadoCódigo Capítulo3. IniciandoumprojetocomCDI
@Inject
private CalculadoraDeSalarios calculadoraSalarios ;
//...
}
Apesar de ser bastante simples, se lembrarmos que uma das vantagens da
injeçãodedependênciaéatestabilidade, perceberemosqueinjetarrecursosem
uma propriedadeprivadanão énada testável. É sónos lembrar doteste visto
nase ção 2.3,emquenosdeparamoscomoproblemadeprecisarmossubstituira
CalculadoraDeSalariosdentroda CalculadoraDeImpostosparaqueapri-
meiradevolvesseumvalorfixoparaasegunda.Masissosófoipossívelquandodei-
xamosdeinjetaradependênciadentrodeumatributoprivado,epassamosausaro
construtor.
@Test
public void testaCalculoIRNaSegundaFaixaDeContribuicao(){
Funcionario funcionario = new Funcionario();
funcionario.setSalario(3000.0); // esse método não existe
CalculadoraDeSalarios calcSalarios = new CalculadoraDeSalarios();
CalculadoraDeImpostos calcImpostos = new CalculadoraDeImpostos();
calcImpostos.calculadoraSalarios = calcSalarios; //não é possível!
double impostoDeRenda =
calcImpostos.calculaImpostoDeRenda(funcionario);
Assert.assertEquals(129.4, impostoDeRenda, 0.0001);
}
Comonessetrechoutilizamosainjeç ãoviapropriedadeprivada,aCDIconse-
gueinjetar,masnósnão.Naverdadeépossível,masteríamosqueutilizarrecursos
deprogramaçãoquesaemdoquecostumamosutilizarnodiaadia. Alémdisso,
étotalmentedesnecessáriofazeressas“maracutaias”umavezqueaCDIconsegue
injetaradependênciadediversasmaneiras.
3.4 As formas de se injetar dependências
Sãotrêsasformasbásicasdeinjetarumadependência,outiposdepontosdeinje ção,
eosdoisprimeirosnósjávimos:viapropriedadeouatributo,viaconstrutor,ouvia
49

## Página 55

3.4. Asformasdeseinjetardependências CasadoCódigo
métodoinicializador. Asemânticadessasduasúltimasop çõeséexatamenteigual,
comopodemospercebernosexemplosaseguir.
public class CalculadoraDeImpostos {
private CalculadoraDeSalarios calculadoraSalarios;
@Inject
public void recebe(CalculadoraDeSalarios calcSalarios,
OutraClasse dependencia2 , ...){
this.calculadoraSalarios = calcSalarios;
//obtém outras dependências e pode fazer alguma inicialização
}
//...
}
Ouentãopodemosusaroconstrutordeformasemelhanteàdométodoinicia-
lizador(nessesexemplosa dependencia2dotipo OutraClassetemointuito
apenasdemostrarasintaxe,nãofazendopartedocódigoreal).
public class CalculadoraDeImpostos {
private CalculadoraDeSalarios calculadoraSalarios;
@Inject
public Calculadora(CalculadoraDeSalarios calcSalarios,
OutraClasse dependencia2 , ...){
this.calculadoraSalarios = calcSalarios;
//obtém outras dependências e pode fazer alguma inicialização
}
//...
}
Avantagemdessasduasabordagenséquepodemosutilizarnosnossostesteso
mesmométodoqueaCDIusaparainjetarasdependências. Adiferen çadasduas
estáapenasnousoounãodeumconstrutorparainjetarasdependências. Se,por
exemplo,utilizarmosalgumframeworkqueutilizaoconstrutorpadrão(públicoe
semargumentos),eoptarmosporinjetarasdependênciasusandoumconstrutor,
50

## Página 56

CasadoCódigo Capítulo3. IniciandoumprojetocomCDI
teremosquelembrardecriarmanualmenteoconstrutorpadrão.Aindaassim,acre-
ditoqueessaop çãosejamaiselegante,comopodemosvernonovocódigodeteste
aseguir.
@Test
public void testaCalculoIRNaSegundaFaixaDeContribuicao(){
Funcionario funcionario = new Funcionario();
CalculadoraDeSalarios calcSalariosMock =
new CalculadoraDeSalariosMock(3000.0);
//cria a CalculadoraDeImpostos passando dependência no construtor
CalculadoraDeImpostos calcImpostos =
new CalculadoraDeImpostos(calcSalariosMock);
double impostoDeRenda =
calcImpostos.calculaImpostoDeRenda(funcionario);
Assert.assertEquals(129.4, impostoDeRenda, 0.0001);
}
Comoseobserva,voltamosautilizaro mockcriadonase ção2.3paraqueocó-
digosejaexecutável.Agoravamosvercomoficaocódigoseoptarmospelométodo
inicializador.Nessecaso,nãoprecisaremoscriarmanualmenteoconstrutorpadrão,
masautilizaç ãonãoficatãolimpa:
//cria a CalculadoraDeImpostos
CalculadoraDeImpostos calcImpostos = new CalculadoraDeImpostos();
//cria o mock
CalculadoraDeSalarios calcSalariosMock =
new CalculadoraDeSalariosMock(3000.0);
//atribui o mock à calculadora de impostos =/
calcImpostos.recebe(mock);
Essaabordagemtambémnospermitepassarasdependênciasdentrodeumteste,
masautilizaç ãoémenosintuitiva.
51

## Página 57

3.5. Recapitulando CasadoCódigo
3.5 Recapitulando
Vimosastrêsformasdepassarumadependência:viaatributoprivado,métodoini-
cializadoreviaconstrutor. Vimostambémquequalquerclassedentrodeumpa-
coteCDIécandidataparasatisfazerumadependência,ouseja,éinjetávelemoutras
semprecisardenenhumaconfiguraç ãoouanotaç ão.Aocontrário,anotamosapenas
quandoqueremosqueaclassenãosejainjetável,porpadrãotodassão.
Comovimosatéaqui,usaraCDInãoénadadifícil,épraticamenteJavapuro.
Paraumprojetinhosimples,oquevimosatéagorajábastaria,poisjásabemosin-
jetarasdependências,queéumadasprincipaisfuncionalidadesdaCDI.Nosfalta
agoraaprendercomorefinarumpoucomaisessemecanismo,aléméclarodasoutras
funcionalidadesqueaespecificaç ãonostraz.
Nopróximocapítuloveremoscomoespecificarqualificadoresàsnossasclasses,
evitandocasosdeambiguidade.
52

## Página 58

Capítulo4
Resolvendodependênciascom
tipagemforte
TalvezaprincipalfuncionalidadedaCDIsejaaresolu çãodedependênciasdeforma
tipada.Enquantoasprimeirasferramentasdeinje çãodedependênciaserambasea-
dasemXMLouemanota çõesqueusavam Strings,aCDIusaamesmatipagem
fortequeestamoshabituadosausarnoJava.
Nãoinjetamosumadependênciabaseadononomedeumbean,esimnoseu
tipo. Autilizaçãodenomeséfeitaemcasosexcepcionais,porexemplo,quando
queremosinjetarumobjetodeumtipomuitosimples,comouma String.
Comotemosmuitoscasosparaanalisar,emvezdeescreverateoriadaresolu ção
dedependênciasagora,vamospassarpelosexemplosqueirãofundamentaroenten-
dimentodessateoria.Aofinaldocapítuloteremosumarevisãodoquefoivistoea
definiçãodofuncionamentodessemecanismotãoimportante.

## Página 59

4.1. Lidandocomaambiguidadenasdependências CasadoCódigo
4.1 Lidando com a ambiguidade nas dependências
Emprojetosmédiosougrandes,costumamosterumadiversidadedetiposdecom-
ponentes,diferentesconfiguraçõesdeobjetos.Écomumtermosdiversospadrõesde
projetoscoexistindo,aindaquenãopercebidos,algoquegeralmentenãoocorreem
projetospequenos.Essesdiferentesarranjosdeobjetosacabammuitasvezesdeman-
dandoumaconfiguraçãodiferenteaousarmosCDI,masnadaquesejacomplicado.
Vamosadotarcomoexemploafuncionalidadedecálculodafolhadepagamento
danossaempresa.Jávimosnase ção2.3sobreoprincípiodasubstitui çãodeLiskov,
equeéumaboapráticaousodeinterfaces;logoiniciaremosessafuncionalidade
peladefiniçãodasuainterface.
public interface CalculadoraFolhaPagamento {
Folha calculaFolha(List<Funcionario> funcionarios);
}
Definimos uma interface bem simples para focarmos na CDI. Para nossa
CalculadoraFolhaPagamentoteremosduasimplementa çõestambémsimples,
umaqueefetuaocálculoefetivodafolhadepagamentos,salvandonobancodeda-
dosainformaç ãodafolhadomêscorrente;eoutraquefazapenasumasimulaç ão,
nãoproduzindoefeitospermanentes,apenasapurandoosvalores.
Partiremosdeimplementaç õesfalsas,queapenasescrevemnoconsoleoque
estariamfazendo:
public class CalculadoraFolhaPagamentoReal
implements CalculadoraFolhaPagamento {
public Folha calculaFolha(List<Funcionarios> funcionarios){
System.out.println("Efetua o cálculo "
+ "real da folha de pagamentos" );
}
}
Apesardaimplementaç ãoqueacabamosdever,conceitualmenteessaimple-
mentaçãoda CalculadoraFolhaPagamentoalémdecalcularosvalores,deixa
54

## Página 60

CasadoCódigo Capítulo4. Resolvendodependênciascomtipagemforte
semprenobancodedadosoresultadodocálculodafolhadomêsatual. Épossí-
velquenomundorealtivéssemosmaismétodosnessainterface,possibilitandoo
cálculoretroativo,porexemplo,masessemétodojábastaporenquanto.
Seforaprimeiravezqueexecutamosocálculodentrodomês,serácriadoum
novoregistrocomosdadosdafolhadessemês,massejátiverumresultadocalculado
nobanco,estedeveráseratualizado. Assimsendo,cadamêsdeveterapenasum
registrodecálculodanossafolha.
Vamosagoraàsegundaimplementaç ão.
public class SimuladoraCalculoFolhaPagamento
implements CalculadoraFolhaPagamento {
public Folha calculaFolha(List<Funcionarios> funcionarios){
System.out.println("Efetua o simulacao da folha de pagamentos" );
}
}
Já aSimuladoraCalculoFolhaPagamentofazoscálculosdosvaloresda
folhasemconsiderarseháalgumregistroparaomês,eaofinalnãosalvaqualquer
informaçãonobancodedados.Serveapenasparaosetorfinanceiroprojetarvalo-
res.Seriaoequivalenteaumsimuladordefinanciamentodeumbanco.Osvalores
mostradosalinãoficamregistradosnosistemadobanco,servemapenascomouma
pré-visualização.
Agorapodemoscriaroutraservletparatestarmosnossasimplementações.Va-
mosiniciarpelaimplementaç ão“real”.
@WebServlet("/calcular-folha")
public class CalcularFolhaPagamento extends HttpServlet {
@Inject
private CalculadoraFolhaPagamento calculadoraFolha ;
public CalcularFolhaPagamento() {
System.out.println("Instanciando a Servlet "
+ " CalcularFolhaPagamento...");
}
55

## Página 61

4.1. Lidandocomaambiguidadenasdependências CasadoCódigo
@PostConstruct
public void ok(){
System.out.println("CalcularFolhaPagamento pronta.");
}
protected void doGet(HttpServletRequest req,
HttpServletResponse res)
throws ServletException, IOException {
FuncionarioBuilder builder = new FuncionarioBuilder();
Funcionario f1 = builder.comSalarioBaseDe(1000.0).build();
Funcionario f2 = builder.comSalarioBaseDe(2000.0).build();
Funcionario f3 = builder.comSalarioBaseDe(3000.0).build();
List<Funcionario> funcionarios = Arrays.asList(f1, f2, f3);
System.out.println("Efetuando o cálculo..." );
Folha folha = calculadoraFolha.calculaFolha(funcionarios);
//mensagem para o usuário
res.getOutputStream().print("Calculo da folha "
+ "executado com sucesso");
//saída no console
System.out.println("Fim.");
}
}
Odetalheimportanteaquiéquenãoinjetamosaimplementaç ão,senãonãofaria
sentidodefinirmosainterface. Devemossempredesenvolverpensandonaabstra-
ção,enãonocasoconcreto.Sendoassim,solicitamosainje çãodeumaimplemen-
taçãodainterface CalcularFolhaPagamento.Comisso,aocriarmosumanova
implementação,nãoprecisamosmudarnossaservlet.
Anãoobservânciadessasboaspráticasdeprojetodeclasseséqueaumentao
efeitocascataquandotemosumamudan çanonossosoftware.Usandoainterface,
seaformadecalcularafolhamudar,nãoprecisamosficarcolandodúziasde i fspara
56

## Página 62

CasadoCódigo Capítulo4. Resolvendodependênciascomtipagemforte
alteraraclasseatual,podemossimplesmentecriarumanovaimplementaç ãoque
substituiaantiga.
Podemosaindarodarasduasimplementaç õesemparalelo,algoquenãoseria
possívelsealterássemosdiretamenteaimplementaç ãooriginal. Amenoséclaro,
quefossefeitoumimenso i fseparandoocálculonovodovelho,oquecertamente
transformarianossocódigoemalgoenormeecheiodeduplicações;difícildeenten-
deremanter.
Parecequeestátudocerto,masseexecutarmosnossoexemploteremosumasur-
presa(onometotalmentequalificadodaclassefoiencurtadoeaidentaç ãoalterada
apenasparasimplificaraanálisedolog):
org.jboss.weld.exceptions.DeploymentException:
WELD-001409 Ambiguous dependencies for type [CalculadoraFolhaPagamento]
with qualifiers [@Default] at injection point
[[field] @Inject private br...CalcularFolhaPagamento.calculadoraFolha].
Possible dependencies
[[Managed Bean
[class br...CalculadoraFolhaPagamentoReal]
with qualifiers [@Any @Default],
Managed Bean
[class br...SimuladoraCalculoFolhaPagamento]
with qualifiers [@Any @Default]]]
Aoiniciaraaplica çãotemosessamaravilhademensagemdeerro!Elanosex-
plicacertinhooqueocorreu,eonde.UmadaspremissasdaCDIétentaradiantaro
máximodeerrospossíveisaoinciarmosseucontexto.Emvezdesubirmosaaplica-
çãocomsucessoeencontrarmosdiferenteserrosacadatelaqueacessamos,epior,
commensagensnadaexplicativas,aCDIdefinequeasvalidaçõesdevemserfeitas
aosubirocontextoeasmensagensdevemdizeroporquêdoproblema.
Lendo a mensagem percebemos que a CDI (no caso estamos
usando a implementação de referência, o Weld) nos mostra exata-
mente qual o problema. Temos dois candidatos elegíveis para sa-
tisfazer a dependência no ponto de injeção [[field] @Inject private
br.com.casadocodigo.livrocdi.servlets.CalcularFolhaPagamento.calculadoraFolha].
Se voltarmos à seção 3.4, vamos relembrar os três tipos de ponto de inje-
ção: atributo (aqui chamado defield), método inicializador e construtor. Na
mensagem, aparece que a tentativa foi de injetar uma dependência em um
atributo e ainda mostra qual foi: o atributo
calculadoraFolha da classe
57

## Página 63

4.2. Osqualificadores CasadoCódigo
br.com.casadocodigo.livrocdi.servlets.CalcularFolhaPagamento.
Assim, mesmo em uma aplicação grande, não teremos dúvida de onde está o
problemarelatado.
Continuandoaanálisedamensagem,veremosqueoproblemaocorreuporque
encontramosdoiscandidatoselegíveisparaamesmadependência,ecomonãoes-
pecificamosmaisnenhumdetalheparaajudaraCDIaescolher,simplesmentefoi
lançadaumaexce ção.
Ainda na mensagem de erro vemos que além do tipo,
CalcularFolhaPagamento, a CDI analisou também osqualifiers, ou quali-
ficadoresdasdependências, mascomoambososcandidatostinhamosmesmos
qualificadores,aambiguidadepermaneceu.
Nas seçõesseguintesveremosformasdeeliminaressaambiguidade.
4.2 Os qualificadores
Aformamaiscomumdeeliminaraambiguidadeéatravésdousodequalificadores.
Essenome,porsinal,épraticamenteautoexplicativo.Comqualificadoresconsegui-
mosdistinguirumcandidatoasuprirumadependênciadeoutro.
Adefiniçãodeumqualificadorésimples,criamosumaanotaç ãoqueseráoqua-
lificador,eaanotamosparadizerqueelanãoéumaanota çãoqualquer.
import static java.lang.annotation.ElementType.*;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;
import javax.inject.Qualifier;
@Target({TYPE, FIELD, METHOD, PARAMETER})
@Retention(RetentionPolicy.RUNTIME)
@Qualifier
public @interface Simulador {
}
Apesardasdiversasanotaç õesnanossaanota ção,apenasa @Qualifieréda
CDI,asoutrasduassãoanota çõesnormaisdoJava.Porissonocódigodeixeiapare-
cendoosimports.
Asduasprimeirasanota ções, @Targete Retention,servemrespectivamente
paradizerondepoderemosutilizarnossoqualificador,eparaquenossaanotaç ão
58

## Página 64

CasadoCódigo Capítulo4. Resolvendodependênciascomtipagemforte
sejalegívelemtempodeexecuç ão,poissemissoaCDInãoconseguirialê-la. Por
fim,aanotaçãoqueinteressadizquenossaanota çãoéumqualificador.Agorabasta
qualificarmosnossasclassesquenãohaverámaisdúvidas.
@Simulador
public class SimuladoraCalculoFolhaPagamento implements
CalculadoraFolhaPagamento {
//o resto do código permanece igual
}
Comonossoqualificadordizqueoobjetomarcadoporeleéumsimulador,dei-
xamosocódigorealcomoestá,emarcamosapenasosimulador.
Agoraaosubirnossaaplicaç ãonãoocorrenenhumerro,eaoexecutarnossaser-
vlet(http://localhost:8080/livro-cdi/calcular-folha),asaídanoconsoleéaseguinte.
Instanciando a Servlet CalcularFolhaPagamento...
CalcularFolhaPagamento pronta.
Efetuando o cálculo...
Efetua o cálculo real da folha de pagamentos
Fim.
Ou seja, a dependência injetada foi a implementaç ão real da
CalculadoraFolhaPagamento.
Umacoisaquedevemosperceber: nanossaservletpedimosparainjetaruma
CalculadoraFolhaPagamentosemespecificarumqualificador,entãonaprática
pedimosparaquesejainjetadaumainstânciacomoqualificador @Default.
Seolharmosnovamenteologdoerroapresentadoantesderesolvermosaam-
biguidade,apareciaamensagemdequeforamencontradosdoiscandidatoscomos
tiposcompatíveis,ecomosmesmosqualificadores, @Anye @Default.
Logo,podemosconcluirqueassimcomoquandonãoespecificamosnenhum
construtornanossaclasseoJavaautomaticamentecriaumconstrutordefault,assim
tambémaCDIqualificanossosobjetoscomoqualificadordefaultsenãoespecifi-
carmosoutro.
Podemos concluir também que se anotarmos a classe
CalculadoraFolhaPagamentoReal com o qualificador @Simulador,
voltaremos a ter o mesmo problema de ambiguidade, mas dessa vez com os
qualificadores
@Anye @Simulador.
59

## Página 65

4.2. Osqualificadores CasadoCódigo
Qualificadorescomatributos
Comosempre,agoraqueentendemosasoluç ão,vamosevoluirumpouquinho
oproblema.Vamossuporqueestásendofeitoumestudodeviabilidadefinanceira
deumnovoplanodecargosparaaempresa,ejáquetemosafuncionalidadede
simularafolhadepagamento,osetorfinanceironospediuparaimplementarmos
umsimuladorqueconsiderasseosparâmetrospretendidosnonovoplano.
Dessaforma,aimplementaç ãorealesuaservletpermaneceminalteradas,mas
precisaremosdemaisumainstânciade
CalculadoraFolhaPagamentoparaexe-
cutaressanovatarefa.Odetalheéqueessanovaimplementaç ãotambémseráum
simulador,masemvezdesimularnoplanodecargosatual,queédoanode2005,
vaifazeroscálculosbaseadosnapropostade2013.
Comoresolvemos?Alteramosnossoqualificadorpara
@Simulador2005ecri-
amosum @Simulador2013?Jáconsiderandoessassituações—osqualificadores
—assimcomoqualqueranotaçãoJavapodeteratributos,nonossovamoscriarum
queserviráparaidentificaroplanoqueestásendoconsiderado.
@Target({TYPE, FIELD, METHOD, PARAMETER})
@Retention(RetentionPolicy.RUNTIME)
@Qualifier
public @interface Simulador {
PlanoDeCargos planoDeCargos() default PlanoDeCargos.VERSAO_2005;
}
Alteramosnossoqualificadorparaqueeleaceiteaindicaç ãodoplanodecar-
gosqueestásendoconsiderado. Paramanteracompatibilidade, especificamos
que caso não seja especificado um valor para essa propriedade, será conside-
radooplanode2005, maspoderíamosdeixarsemvalorpadrãoealterarnossa
SimuladoraCalculoFolhaPagamentoparaespecificarláqualplanousar.Mas
comoemumcasorealpodeserquetenhamosmuitomaiscasosparamudar,dessa
maneiraminimizamososimpactos.
Outracoisaquepodemosperceberéqueestamosusandoumaenumquerepre-
sentaosplanosdecargos.
public enum PlanoDeCargos {
VERSAO_2005, VERSAO_2013
}
Éumcódigobemsimples,queestamosusandoapenasparanãousarmosum
inteiropuro,poisissopodeacarretarerrodedigitaç ão.Eo enumtemaindaavanta-
60

## Página 66

CasadoCódigo Capítulo4. Resolvendodependênciascomtipagemforte
gemdetrazerosvalorespossíveisprontos,enquantoseestivéssemosusandointeiro,
alémdapossibilidadedoerrodedigitaç ão,teríamosquesaberdecabe çaquaisos
valoresválidos.
Agorasim,podemoscriaronovosimuladorespecificandoaversãodoplanoque
estamosconsiderando.
import static
br.com.casadocodigo.livrocdi.qualificadores.PlanoDeCargos.*;
@Simulador(planoDeCargos = VERSAO_2013)
public class SimuladoraCalculoFolhaPagamentoPlano2013 implements
CalculadoraFolhaPagamento {
@Override
public Folha calculaFolha(List<Funcionario> funcionarios) {
System.out.println("Simulação com plano de 2013" );
return null;
}
}
A diferença está apenas no fato de especificarmos um valor diferente do
padrão dentro do nosso qualificador. Agora quando formos injetar uma
CalculadoraFolhaPagamentodentrodeumbean,temosasseguintesop ções:
@Inject
private CalculadoraFolhaPagamento calculadoraFolha;
Issoinjetaaimplementaç ãorealdainterfacepedida,queseráumobjetodaclasse
CalculadoraFolhaPagamentoReal.Napráticaécomoseestivéssemosespeci-
ficandoquequeremosoqualificador @Default.
@Inject @Simulador
private CalculadoraFolhaPagamento calculadoraFolha;
//ou
@Inject @Simulador(planoDeCargos = VERSAO_2005)
private CalculadoraFolhaPagamento calculadoraFolha;
61

## Página 67

4.2. Osqualificadores CasadoCódigo
Como especificamos a VERSAO_2005 como valor padrão do qualifica-
dor, essas duas opções são equivalentes, e a implementação injetada será a
SimuladoraCalculoFolhaPagamento.
Porfim,temosaseguinteop ção.
@Inject @Simulador(planoDeCargos = VERSAO_2013)
private CalculadoraFolhaPagamento calculadoraFolha ;
Isso fará com que o bean injetado seja da classe
SimuladoraCalculoFolhaPagamentoPlano2013.
A utilização de propriedades nos qualificadores é uma ferramenta interes-
sante pois evita a criação de qualificadores esquisitos, que seriam na verdade
umaespecializaçãodeoutroqualificador. Emvezdetermosdoisqualificadores:
@Simulador2005e @Simulador2013,temosapenasumqualificadornoqual
podemosespecificarumatributo.
Podemosterinclusiveváriosatributosdentrodonossoqualificador:
import javax.enterprise.util.Nonbinding;
@Target({TYPE, FIELD, METHOD, PARAMETER})
@Retention(RetentionPolicy.RUNTIME)
@Qualifier
public @interface Simulador {
PlanoDeCargos planoDeCargos() default PlanoDeCargos.VERSAO_2005;
boolean planoAprovado() default true;
@Nonbinding boolean enviarNotificacao() default false;
}
Paramostrarcomopodemosutilizarmaisdeumapropriedade,alteramosnosso
qualificadorparaqueelerecebamaisdeumapropriedade.Nesseexemplo,adiciona-
mosduasnovaspropriedades.Aprimeiraparadefinirseosimuladorédeumplano
jáaprovadoounão,easegundaéapenasumainformaç ãoextra,quenãoinfluencia
naqualificaçãopropriamentedita.
Isso porque anotamos a propriedade
enviarNotificacao com
@Nonbinding, e dessa maneira informamos à CDI que a mesma não deve
serconsideradaquandoumbeancandidatoestiversendoescolhido. Ovaloraí
presente serve apenas como uma propriedade informativa para o nosso código
Java. Ouseja,emalgummomentopodemosterumcódigoanalisandoseovalor
62

## Página 68

CasadoCódigo Capítulo4. Resolvendodependênciascomtipagemforte
dapropriedadeéverdadeiroparaenviar,porexemplo,ume-mailavisandoqueo
cálculofoirealizadoequaloresultado.
Apesardaspropriedadenosqualificadoresevitaracriaç ãodenovosqualifica-
doresdemaneiradesnecessária,existirãocasosemqueteremosmaisdeumquali-
ficadoraomesmotempo.Cadaqualificadordessespodeteratributosqueespecifi-
camaindamaisoquequeremos,quesãoosatributosque nãoestãoanotadoscom
@Nonbinding,etambématributosquepossuamessaanota çãoeservemapenas
comoinformaçãoadicional.
Ésólembrarque Nonbindingsignifica“nãovinculante”,aquelequenãocriavín-
culo. Foraessaspropriedadesnãovinculantes,todasasoutrasrefinammaisainda
aqualificaçãodobean—assimtambémcomoacontecequandotemosmaisdeum
qualificador.
Aofinaldocapítulo,nase ção4.9,teremosumarecapitulaç ãodetodooprocesso
deresoluçãodedependênciasenvolvendoqualificadoreseoutrasferramentasque
veremosatélá.Tenteimaginaraspossibilidadescomasferramentasquevocêjáviu,
esepermaneceralgumadúvida,comoresumoacreditoqueelaserásanada.
Oqualificador@Any
Jáentendemoscomoacabarcomumaambiguidadeatravésdeumqualificador,
masnosdeparamosalgumasvezescomessequalificador @Any.Comoonomedele
diz,essequalificadorestápresenteem qualquerobjeto.
Paraexemplificar,vamosmudarnossaservlet,queestáfuncionandosemqual-
querambiguidade,paraqueelafiquedessaforma:
@WebServlet("/calcular-folha")
public class CalcularFolhaPagamento extends HttpServlet {
@Inject @Any
private CalculadoraFolhaPagamento calculadoraFolha ;
//o restante permanece igual
}
Sabemos que temos três candidatos a satisfazer de-
pendências do tipo CalculadoraFolhaPagamento, que
são: CalculadoraFolhaPagamentoReal, que está com
o qualificador @Default, já que não especificamos outro,
63

## Página 69

4.2. Osqualificadores CasadoCódigo
SimuladoraCalculoFolhaPagamento, o qual recebeu o qualificador
@Simulador, e SimuladoraCalculoFolhaPagamentoPlano2013, que
recebeuoqualificador @Simulador(planoDeCargos = VERSAO_2013) .
Senopontodeinje çãonãocolocarmosnenhumqualificador,estaremosimpli-
citamentepedindoodefault,esecolocarmos @Simuladorsabemosqualinstância
seráinjetadatambém. Masfazendoaaltera çãoqueacabamosdever,estamospe-
dindoparaquenessecasosejaconsiderado qualquercandidatodisponívelnocon-
texto.
Nonossoexemplo,issofarácomquevoltemosaterproblemasdeambiguidade:
org.jboss.weld.exceptions.DeploymentException: WELD-001409
Ambiguous dependencies for type [CalculadoraFolhaPagamento]
with qualifiers [@Any] at injection point [[BackedAnnotatedField]
@Inject @Any private br...CalcularFolhaPagamento.calculadoraFolha].
Possible dependencies
[[Managed Bean [class br...SimuladoraCalculoFolhaPagamentoPlano2013]
with qualifiers [@Simulador @Any],
Managed Bean [class br...SimuladoraCalculoFolhaPagamento]
with qualifiers [@Simulador @Any],
Managed Bean [class br...CalculadoraFolhaPagamentoReal]
with qualifiers [@Any @Default]]].
Please see server.log for more details.
Paraqueserviriaentãoessequalificador?Ele,naverdade,seriaoequivalenteà
classe java.lang.Object,queémãedequalquerobjetoJava,masparaosobjetos
queestãonocontextoCDI.Assim,seprecisarmos,poralgummotivo,buscartodos
oscandidatosdeumdeterminadotipo,independentedequalificadores,usamoso
qualificadorespecial
@Any.
Ousoficarámaisclaroquandoestivermosestudandoabuscaprogramáticade
dependências,naseção4.8.Nessecenárioseráinteressantepodermosbuscartodos
oscandidatosasatisfazerumadependênciadeumdeterminadotipo,eentãotomar
algumadecisãoemtempodeexecuç ão,ouaindausartodosessesobjetosdeuma
vez.
Apenasparanãoficarmuitoabstrato,vamossuporquetenhamosumainterface
quedefineummecanismodenotificaç ão.Essasnotificaçõesseriamenviadasaores-
ponsávelpelosetorfinanceirodaempresasemprequeumanovafolhafossegerada,
podendoserpore-mail,SMSouqualquermeioquepossamosimaginar.
Comonãosabemosquaisqualificadoresasimplementaçõesdessainterfacepo-
demter,podemosutilizaroqualificador
@Anyparabuscartodasasimplementações
64

## Página 70

CasadoCódigo Capítulo4. Resolvendodependênciascomtipagemforte
disponíveis,colocá-lasemuma Collection,eentãopassarportodasasinstân-
ciasinvocandoumaaumaparagarantirqueporalgummeioanotificaç ãochegaria
aqueminteressar.
4.3 Alternatives: eliminando ambiguidade e tor-
nando um bean opcional
Aanotação @Alternativeserveparatransformarmosumbeanemumaalterna-
tivaasuprirumadependência,ouseja,elenãoseráumcandidatoautomaticamente
disponível.
Todobeanalternativosóéinjetávelsefordeclaradono beans.xml,enesse
casoeleficacomumaprioridademaiordoqueobeannãoalternativo.
Nocasodaaplicaç ãoqueestamosdesenvolvendo,vamosconsiderarquetivemos
acriaçãodeumnovoplanodecargosesalários,quealteroutotalmenteaformacomo
nossocálculodesalárioéfeitohoje.Aprimeiraalternativaquepodemospensaré
emalteraraclasse
CalculadoraDeSalariosparaacomodarasnovasregras,mas
vamosanalisarmelhoressecaso.
U m a m u d a nçagrandeassimpodenãoentraremvigorimediatamente,então
vamosconsiderarqueamudan çaentreemproduç ãodaquitrêsmeses.Alémdisso,
apósentraremprodu çãopodeserquepordescontentamentodealguns,aempresa
volteatrás,paraaregraqueestavafuncionandoantesepartaparaaelabora çãode
umnovoplano.
Alterandodiretamenteocódigoda CalculadoraDeSalarios,nãopodería-
moscolocaremproduç ãoimediatamentepoisaregranovasópassariaavalerno
futuro.Edepoissetivermosquevoltararegraantigateríamosquereverterasalte-
rações.Apesardessescenáriosserembemcobertosporumbomusodecontrolede
versãodecódigo,casoissonãosejafeitocorretamente,enãotenhamosumservidor
debuild,podemostersituaçõesemquenãoseriapossíveldeterminadodesenvolve-
dorfazerumnovodeploypoisaversãoqueestánasuamáquinajáestácomocálculo
alterado.Claroqueesseéumexemplopraticamentelúdico,masnãoquerdizerque
nãoocorra.
Umdosusosde
@Alternativepodeserjustamenteodesenvolvimentodessa
novaversãoda CalculadoraDeSalarios. Emvezdemudaraimplementaç ão
daclasse,extraímosumainterfacedessaclasse(geralmenteasIDEstematalhospara
fazerisso).Dessaformateremosainterface
CalculadoraDeSalarioseaimple-
mentaçãocomocódigoatual,etodosospontosdeinje çãodevemcontinuarapon-
65

## Página 71

4.3. Alternatives:eliminandoambiguidadeetornandoumbeanopcional CasadoCódigo
tandoparaotipo CalculadoraDeSalarios,queanteseraumaclasse,eagora
passaaserumainterface.
public interface CalculadoraDeSalarios {
double calculaSalario(Funcionario funcionario);
}
public class CalculadoraDeSalariosPlano2005
implements CalculadoraDeSalarios {
/*
Código igual ao que tínhamos em
CalculadoraDeSalarios quando era classe
*/
}
Agoracomoestamoscriandoumnovocálculocombasenonovoplanodesa-
lários, bastacriarmosumanovaimplementaç ão, quepodeporexemplosecha-
mar CalculadoraDeSalariosPlano2013,paraindicarqueéocálculodoplano
criadonesseano. Porémsecolocarmosasduasimplementaçõesemprodu çãoao
mesmotempo,teremosojáconhecidoproblemadaambiguidade.Porisso,nanova
implementaçãoutilizaremosaanotaç ão @Alternative.
import javax.enterprise.inject.Alternative;
@Alternative
public class CalculadoraDeSalariosPlano2013
implements CalculadoraDeSalarios {
//o novo código, que nesse exemplo não influencia no entendimento
@Override
public double calculaSalario(Funcionario funcionario){
return 0.0;
}
}
Agorapodemosdeixaraimplementaç ãopronta,einclusivefazerumdeploycom
elasemomenorproblema,poisosbeansalternativosnãosãoinjetáveisemlugarne-
nhumatésegundaordem.Essasegundaordemseráaexpressahabilitaç ãodessebean
noarquivo beans.xml,ouviaanota ção,momentoemqueelepassaaserelegívele
66

## Página 72

CasadoCódigo Capítulo4. Resolvendodependênciascomtipagemforte
inclusive“sobrescreve”obeannãoalternativo.Emoutraspalavras,quandoligarmos
a CalculadoraDeSalariosPlano2013,elaentraautomaticamentenolugarda
CalculadoraDeSalariosPlano2005.Ecasosejanecessáriovoltaratrás,basta
comentaralinhadoarquivo beans.xmlondehabilitamosobean.
Pelaprimeiravezestamosmexendocomumarquivoxml,eaindaassimseucó-
digoémínimo. Agrandemaioriadeleéocabe çalhodoarquivo,eeuencurteio
nomedaclasseparaficarbememumalinha,massemprequeusarmosoarquivo
xml,deveusaronometotalmentequalificadodasclasses.
<beans xmlns="http://xmlns.jcp.org/xml/ns/javaee"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
http://xmlns.jcp.org/xml/ns/javaee/beans_1_1.xsd">
<alternatives>
<class>
br.com.casadocodigo...CalculadoraDeSalariosPlano2013
</class>
</alternatives>
</beans>
Agora, ao executarmos nosso sistema, a classe
CalculadoraDeSalariosPlano2013 é que será a injetável nos pontos que
pedempelainterface CalculadoraDeSalarios.
Podemosperceberqueousode @Alternativetemumpropósitodiferentedo
usodosqualificadoresvistosantes,éumaformadedesabilitartemporariamenteum
bean,ehabilitá-loemmomentooportunodeumaformaqueelevoltenolugardo
beanequivalente.
Emumcenáriomaiscomplexo,podemosteratémaisdeumbeanmarcadocomo
alternativo. Porexemplo,quandoutilizamosopadrão Strategy. Épossívelmarcar
todasasimplementaçõescomoalternativasehabilitarsomenteaquelaquequeremos
usarnomomento. Porém,sehabilitarmosmaisdeuma,voltaremosaoproblema
daambiguidade,amenosqueespecifiquemos,viaanotaç ão,qualalternativatem
prioridademaior.
67

## Página 73

4.4. Prioridade:novidadedaCDI1.1,partedoJavaEE7 CasadoCódigo
4.4 Prioridade:novidade daCDI1.1,parte doJa v aEE
7
ApartirdoJavaEE7,comaatualizaç ãodaespecificaç ãodeinterceptorparaaversão
1.2(JSR318releasedemanuten ção2),foiadicionadaapossibilidadedeestipularmos
ordenaçãodosinterceptors;paraqueissofossepossível,foiadicionadaaanota ção
@Prioritynasanota çõescomunsdoJava(JSR250).Quandoestivermosestudando
osinterceptadores,veremosmaissobreisso.Porenquantovamosanalisaressaano-
taçãodopontodevistados @Alternatives.
Comojávimos,usaralternativaséumaboaformadecriarmosdiferentesop ções
paraumadependência,masatéoJavaEE6,nãoconseguíamoshabilitarmaisdeuma
alternativaaomesmotempo,poisteríamosoproblemadeambiguidade.Umbean
alternativotemprioridadesobreumbeannãoalternativo,masentreosalternativos
nãohaviamaneiradeestipularprioridade.
Agora,alémdenãoprecisarmosmaisutilizaroarquivo
beans.xmlparaati-
varumaalternativa,podemosestipulardiferentesprioridadesparacadauma,assim,
seráinjetadaadeprioridademaior.
Aanotação
@Priorityrequeruminteiroqueespecificaqualaprioridade,e
seráinjetadoobeandeprioridademaior.Nãoéobrigatório,maséinteressanteuti-
lizarmosointervalodevaloresqueconstamnaespecificaç ãodeinterceptors:
• Interceptor.Priority.PLATFORM_BEFORE=0
• Interceptor.Priority.LIBRARY_BEFORE=1000
• Interceptor.Priority.APPLICATION=2000
• Interceptor.Priority.LIBRARY_AFTER=3000
• Interceptor.Priority.PLATFORM_AFTER=4000
Osvaloresparaplataformaebibliotecaservemparaespecificarrespectivamente
osintervalosquesãousadospelaplataformaJava,ouseja,aspartesdopróprioJava
EE;eparaseremusadospelasbibliotecas,frameworks,eoutrascoisasqueexecutam
emmomentodiferentedaplataforma,etambémdanossaaplicaç ão.
Comoestamosaquitratandododesenvolvimentodeaplicações,vamostrabalhar
apartirdovalor
Interceptor.Priority.APPLICATION.Vamosentãoalterar
nossasimplementaçõesde CalculadoraDeSalariosapenasparavermosessa
possibilidade.
68

## Página 74

CasadoCódigo Capítulo4. Resolvendodependênciascomtipagemforte
import javax.annotation.Priority;
import javax.enterprise.inject.Alternative;
import javax.interceptor.Interceptor;
@Alternative @Priority (Interceptor.Priority.APPLICATION + 1)
public class CalculadoraDeSalariosPlano2013
implements CalculadoraDeSalarios {
// código permanece igual
}
Vamosanotarnossaclasse CalculadoraDeSalariosPlano2013comaano-
tação @Priorityeinformaraprioridadequequeremos.Agorapodemoscomentar
no beans.xmlondeativávamosessebeanalternativo,poisaanota çãosupreessa
demanda.
<beans xmlns="http://xmlns.jcp.org/xml/ns/javaee"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
http://xmlns.jcp.org/xml/ns/javaee/beans_1_1.xsd">
<alternatives>
<!--
<class>
br.com.casadocodigo...CalculadoraDeSalariosPlano2013
</class>
-->
</alternatives>
</beans>
Vamosagoradeixarnossaimplementaç ãoatualtambémcomoalternativapara
podermostestarapriorizaç ão.
import javax.annotation.Priority;
import javax.enterprise.inject.Alternative;
import javax.interceptor.Interceptor;
@Alternative @Priority (Interceptor.Priority.APPLICATION)
public class CalculadoraDeSalariosPlano2005
implements CalculadoraDeSalarios {
69

## Página 75

4.5. Beansnomeados CasadoCódigo
// código permanece igual
}
Notem que aCalculadoraDeSalariosPlano2013ficoucomumapriori-
dademaiorparaqueelasejaaescolhida.
Paraconseguirmostestar,podemoscriarumaoutraservletqueinjetaessade-
pendênciaesimplesmenteescreveraclasseselecionadanarespostaparaousuário.
Embreve,estaremosmelhorandoessaformadetestareaapresenta çãoparaousuá-
rio,masparadarmosumpassodecadavez,aindaestámaissimplesfazerissousando
servletsauxiliares.
@WebServlet("/calcular-salario")
public class CalculadoraSalario extends HttpServlet {
@Inject
private CalculadoraDeSalarios calculadoraDeSalarios;
@Override
protected void doGet(HttpServletRequest req, HttpServletResponse res)
throws ServletException, IOException {
res.getOutputStream()
.print("Calculadora: " + calculadoraDeSalarios.getClass());
}
}
Aí basta alternarmos a prioridade de uma ou outra instância de
CalculadoraDeSalarios e executar novamente para percebermos a mu-
dançanasele çãodobeanaserinjetado.
4.5 Beans nomeados
ApesardaCDItrabalharmuitobemcomaresolu çãodedependênciasatravésde
tipos,hácasosemqueprecisamosqueumbeansejadescobertoapartirdeumnome.
Issopodesernecessárioquandopedimosainje çãodeumtipomuitosimples,como
uma Stringouum Integerquesignifique,porexemplo,ocaminhopadrãoonde
anexosserãosalvosouonúmeromáximodeelementosaserexibidosnaspáginas
delistagemdosistema,ouseja,naspaginações.
70

## Página 76

CasadoCódigo Capítulo4. Resolvendodependênciascomtipagemforte
@Inject @Named("caminhoSalvarAnexos" )
private String caminhoAnexos;
@Inject @Named("tamanhoPaginacao")
private Integer tamanhoPaginacao;
Nessecaso,comootipoémuitocomum,usamosonomecomoumqualifica-
dor.Masdeondevirãoessesobjetos?EssestipossãodopróprioJava,logo,nãosão
injetáveisdiretamente,aindamaiscomessesnomes.Parasupriressanecessidade,a
CDIdefineosmétodosprodutores,queserãoapresentadosnase ção5.1,entãonão
sepreocupecomessedetalheainda.
Umaoutraformaderecuperarmosessasinformaçõesqueestamospedindovia
nome,seriaatravésdadefiniç ãodeumtipoquerepresenteasconfiguraçõesdosis-
tema.Nessetipoperderíamoscolocaressasedemaisinformaçõesnecessárias,como
caminhosde wsdlparaintegraçãoentresistemaseoquemaisfornecessário. Po-
deríamosemummétodoprodutorbuscaressasinformaçõesnobancodedadose
colocaroobjetocomtodasasinformaçõesnocontextoCDI.Assim,emvezdebus-
carumainformaç ãonobancocadavezqueprecisássemos,bastariainjetaroobjeto
querepresentaaconfiguraç ãodosistema.
Mas se a funcionalidade de nomearmos um bean servisse somente para
isso, acabaríamos de descobrir que ela na verdade não é muito útil. Po-
rém temos um caso em que os nomes são necessários, e dessa vez não te-
moscomofazerdeoutraforma. Essecasoéautilizaç ãodosbeansem expres-
sion languages, ouELs. Por exemplo, em uma página JSP ou JSF onde temos
#{calculadoraFolhaBean.ultimoCalculo.valorFolha}.
QuandotrabalhamoscomEL,temosapenasuma Stringquerepresentao
nomedobean, nocasoo calculadoraFolhaBean. Logo, aresoluçãodesse
objeto precisará ser feita via nome. Para que um bean seja alcançável por EL,
precisamos “batizá-lo”, dar um nome a ele. Para isso utilizamos a anotação
javax.inject.@Named.
import javax.inject.Named;
@Named
public class CalculadoraFolhaBean {
//precisa ter um método getter
private FolhaPagamento ultimoCalculo;
71

## Página 77

4.6. Trabalhandocomherançaentrebeans CasadoCódigo
...
}
Nessa anota ção podemos especificar um nome, como
@Named("nomeDoBean"),oupodemosdeixaronomepadrãocomonoexem-
plo. Esse nome padrão nada mais é do que o nome simples da classe com a
primeira letra passada para minúsculo. Por isso, na EL vista antes usávamos
calculadoraFolhaBean.
UmavezresolvidooobjetoraizdaEL,queprecisaterumnome,osdemaissão
alcançadosvia reflection,atravésdosrespectivos gettersemcasodeleitura,e setters
emcasodeescrita.Essefuncionamento,porém,serávistoemoutromomento,poiso
importantenessase çãoéentendermosquealémdaresoluçãoportipo,aCDIsuporta
resoluçãopornome.
OmaiscomuméutilizarmososbeansnomeadoscomoobjetoraizemumaEL,
masnadaimpedequeoinjetemosemoutrobean;enessecasopodesertantopor
nome,comopelotipo,comojáestamoshabituados.
4.6 Trabalhando com herança entre beans
Jávimossobreprincípiodasubstituiç ãonase ção2.3;nopontodevistadoJava,se
estivermosusandointerfaces,conseguimostrocarsuasimplementaçõesouconse-
guimostrocarumtipoporseussubtipos.UsandoCDI,noentanto,nãobastausar
implementsou extends.
Vamostomarcomoexemploaclasse CalculadoraDeSalariosPlano2013,
quejávimosnosexemplosanteriores, eumanovaclassequeveremosagora, a
CalculadoraAssincronaDeSalariosPlano2013.Ocódigodessasclassesnão
importamparanossoexemplo,oimportanteéentendermoscomoaplicarasubsti-
tuiçãoentreacalculadoraeacalculadoraassíncrona,seusubtipo.
@Calculadora
public class CalculadoraDeSalariosPlano2013
implements CalculadoraDeSalarios {}
Paraenriquecernossaanálise,adicionamosumqualificadornovo,queusaremos
apenasnesseexemplo: @Calculadora.Agoravejamosacalculadoraassíncrona.
@Alternative @Priority (Interceptor.Priority.APPLICATION)
public class CalculadoraAssincronaDeSalariosPlano2013
extends CalculadoraDeSalariosPlano2013 {}
72

## Página 78

CasadoCódigo Capítulo4. Resolvendodependênciascomtipagemforte
Para que não tenhamos problemas de ambiguidade, vamos considerar,
para o estudo de herança, que a CalculadoraDeSalariosPlano2013 é
uma classe simples (e não um@Alternative como vimos antes) e que a
CalculadoraAssincronaDeSalariosPlano2013éumbeanalternativoativo,
poisestáanotadocom @Priority. Esseajusteéapenasparatermosumcenário
maissimplesdeanalisar,porémcomtodososingredientesparaumaboaanálise
dessetema.
Combasenoquejásabemos,conseguimospredizercomoaCDIiráresolvera
seguintedependência.
@Inject
private CalculadoraDeSalarios calculadora;
Comoambasasclassesqueacabamosdeversãodetipocompatívelcomainter-
facesolicitada,mascomoa CalculadoraAssincronaDeSalariosPlano2013
éalternativa,ouseja,temprioridade,sabemosqueelaseráaimplementaç ãoseleci-
onada.Masqualseriaoresultadoseotrechoquesolicitaainje çãodadependência
fossecomooseguinte:
@Inject @Calculadora
private CalculadoraDeSalarios calculadora;
Nesse caso, seria injetada uma instância da classe
CalculadoraDeSalariosPlano2013, pois sua subclasse não possui o quali-
ficador @Calculadora. Noentanto, pormaisquenãotenhamosanalisadoo
código da classe CalculadoraAssincronaDeSalariosPlano2013, vamos
considerarqueelaéumaevolu çãodesuaclassemãe,eque,aocriá-la,esperávamos
queelaentrassenolugardaclassemãe. Atéporque,jáestudamosoprincípioda
substituiçãoesabemosqueépossível,mascomonosassegurarqueanovaclasse
sempreseráselecionadanolugardaantiga?
Umaformadefazerissoseria,alémdeestenderaclasseoriginal,colocarnasub-
classetodososqualificadoresdaprimeira.Comisso,noexemploqueacabamosde
ver,emquealémdotipoerampedidosqualificadores(nocasoum,maspoderiam
serdiversos),obeanselecionadoseriaacalculadoraassíncrona.Mesmoassimainda
teríamosdoiscasosemqueaclassemãecontinuariasendoutilizada:métodospro-
dutoreseobservadoresdeeventos.Essesdoisassuntosaindanãoforamvistos,mas
oqueimportaporenquantoéqueambosnãosãoherdadospelasubclasse.
73

## Página 79

4.7. Restringindootipodosbeans CasadoCódigo
Aanotação@Specializes
Pararesolveressaquestão,aCDIdisponibilizaaanotaç ão @Specializes,que
marcaasubclassecomoumasubstitutadaclassemãe. Assim,mesmoqueanova
implementaçãosejaadicionadaemumnovojar,muitotempodepoisqueosistema
estáemprodução,elacertamenteentraráemtodososlugaresondeaclassemãeera
utilizada.Paratal,bastacolocaressaanota çãonaclassefilha.
@Specializes @Assincrono
public class CalculadoraAssincronaDeSalariosPlano2013
extends CalculadoraDeSalariosPlano2013 {}
Agorasabemosqueonovobeansubstituirátotalmenteoantigo,poisaousar
@Specializesaclassefilhaherdatambémtodososqualificadoresdamãe. Isso
não impede no entanto que a nova classe defina novos qualificadores, como o
@Assincronodoexemplo.
Outracoisaherdadaéonomedobeanoriginal. Casoaclassemãepossuio
qualificador @Named,aclassefilhanecessariamenteherdaráomesmonome. Sea
classemãenãopossuirumnome,afilhaficalivreparadefinirounãoum. Masse
amãefornomeadaeafilhatentardefinirumnovonome,serálan çadoumerro
quandoaconfiguraçãoforlidaenquantoaaplicaç ãoinicializa.
Porém,nemtudoétãoautomático,comoomecanismodeespecializaç ãoprecisa
garantirquerealmenteaclassemãenãoseráinstanciadaemmomentoalgumpela
CDI,ecomoosmétodosprodutoreseobservadoresdeeventosnãosãoherdados,
osmesmosficarãoinativosamenosquesejamreimplementados(sobrescritos)na
subclasse.
4.7 Restringindo o tipo dos beans
Jávimosdiversasformasdelidarcomambiguidadeentrebeans:qualificadores,al-
ternatives,eatéespecializarumbean. Mastemosaindaoutraformadegerenciar
nossasdependências,queéforçandootipodobean.Obviamentenãopodemosco-
locarqualquertipoquequeiramos,masapenaslimitaratéqueníveldahierarquia
nossobeanestaráaptoaresponder.
Vamosrecapitularalgunsdosexemplosquevimosatéaqui,everificarumanova
formadelidarcomaambiguidade.
public interface CalculadoraDeSalarios { ... }
7 4

## Página 80

CasadoCódigo Capítulo4. Resolvendodependênciascomtipagemforte
public class CalculadoraDeSalariosPlano2013
implements CalculadoraDeSalarios { ... }
public class CalculadoraAssincronaDeSalariosPlano2013
extends CalculadoraDeSalariosPlano2013 { ... }
Comojávimosatéagora,aresolu çãodedependênciasdaCDIéfortementebase-
adaemtipos,entãoesseéofatordeterminantenaescolhadeumdessescandidatos.
Vamosverospróximosexemplos.
//problema de ambiguidade
@Inject private CalculadoraDeSalarios calculadora;
//problema de ambiguidade
@Inject private CalculadoraDeSalariosPlano2013 calculadora;
//sem problema de ambiguidade
@Inject private CalculadoraAssincronaDeSalariosPlano2013 calculadora ;
Os problemas de ambiguidade que acabamos de
ver envolvem CalculadoraDeSalariosPlano2013 e
CalculadoraAssincronaDeSalariosPlano2013. Isso porque natural-
mente cada bean é candidato a suprir dependências de qualquer um dos tipos
do bean. No caso, CalculadoraAssincronaDeSalariosPlano2013 res-
ponde pelo próprio tipo, por CalculadoraDeSalariosPlano2013, por
CalculadoraDeSalariosepor java.lang.Object.Maspodemosrestringir
porquaistiposnossobeanestádispostoaresponder,paraissobastausarmosa
anotação
@javax.enterprise.inject.Typed.
//responde apenas por CalculadoraDeSalarios e Object
@Typed(CalculadoraDeSalarios.class)
public class CalculadoraAssincronaDeSalariosPlano2013
extends CalculadoraDeSalariosPlano2013 { ... }
/*
responde por CalculadoraDeSalarios,
CalculadoraDeSalariosPlano2013 e Object
*/
75

## Página 81

4.8. Resoluçãodedependênciasobdemandaelookupprogramático CasadoCódigo
@Typed({CalculadoraDeSalarios.class,
CalculadoraDeSalariosPlano2013.class})
public class CalculadoraAssincronaDeSalariosPlano2013
extends CalculadoraDeSalariosPlano2013 { ... }
Restringir o tipo de um bean pode, em determinada situação, re-
solver um problema de ambiguidade. Por exemplo, se injetarmos o
tipo CalculadoraDeSalariosPlano2013 e restringirmos o tipo
de CalculadoraAssincronaDeSalariosPlano2013 para o tipo
CalculadoraDeSalarios. Nesse caso apenas o próprio bean do tipo
CalculadoraDeSalariosPlano2013poderásecandidatar.
Essatalveznãosejaaformamaishabitualdelidarcomambiguidade,masémais
umaferramentaqueaCDInosoferece.
4.8 Resolução de dependência sob demanda e loo-
kup programático
Há situaçõesemqueainje çãodedependênciacomumnãoéobastante.Podemoster
problemasdedependênciacíclica,ouproblemasdelentidãoquandoumbeantem
muitasdependências,queporsuavezpodetertambémváriasoutrasdependências.
Parasolucionaresseproblemapodemoslan çarmãodainje çãodedependência lazy,
ousobdemanda.
Paraexemplificar,vamostomarcomoexemploainje çãodeumainstânciade
CalculadoraFolhaPagamento,
//forma tradicional
@Inject
private CalculadoraFolhaPagamento calculadoraFolhaPagamentoPadrao;
//injeção sob demanda
@Inject
private Instance<CalculadoraFolhaPagamento>
calculadoraFolhaPagamentoLazy;
Nesses exemplos, conforme já vimos, teremos a inje ção de uma
instância da implementaç ão CalculadoraFolhaPagamentoReal.
Isso porque usamos o qualificador @Default, e as demais
implementações, SimuladoraCalculoFolhaPagamento e
76

## Página 82

CasadoCódigo Capítulo4. Resolvendodependênciascomtipagemforte
SimuladoraCalculoFolhaPagamentoPlano2013, possuem o qualifica-
dor @Simulador.
Adiferen çaéqueaoinjetarmosdaformatradicional,ainstânciaéimediata-
mentecriada-ourecuperada,dependendodoescopo-,enquantoaforma lazyé
apenasumlinkparaotipopretendido.Ainstânciarealédisponibilizadaatravésdo
método get(),comovemosaseguir.
@Inject
private Instance<CalculadoraFolhaPagamento>
calculadoraFolhaPagamentoLazy;
...
CalculadoraFolhaPagamento calculadora =
calculadoraFolhaPagamentoLazy.get();
Somentenessemomentoainstancia çãoacontece.Essaabordagemajudaemca-
sosdeinje çãolenta.Casotenhamosmuitasdependênciasquesãoutilizadassomente
emdeterminadoscasos,porexemplodependendodealgumainformaç ãoexterna,
pedirparatodasasdependênciasseremresolvidasdesdeoiníciopoderáprovocar
umacertalentidãonosistema.
Emcenáriosassim,ébempossívelqueessebeanestejapoucocoeso,fazendo
coisasdiferentes,coisasdemais.Porémquandotrabalhamoscominstanciaç ãoma-
nualdasdependências,acabamosinstanciandocadadependênciasóquandoelassão
demandadas,oqueacabamaquiandooquetalvezsejaumproblemadeprojetodas
classes.
Porémsabemosquenemsempreésimplesfazeralgunsajustesnaaplicaç ão,
comoporexemplosepararbeansmuitograndesemoutrosmaiscoesos,seessefor
ocaso,aindaserápossívelusarainstanciaç ãosobdemandaparamelhoraraper-
formance.Usandoainterface
javax.enterprise.inject.Instance,criamos
umponteiroquenãocriaainstânciaimediatamente,masnopermitefazernomo-
mentoapropriado,assimcomofaríamossetivéssemosinstanciandotodasasclasses
manualmente.Omesmopodeserusadoparaevitarosproblemasdedependência
cíclica,quetambémpodesignificarumproblemadeprojetoquesóaparecequando
passamosautilizarumagestãodedependênciaautomática.
Lookupprogramático
Comofalamosquandovimosoqualificador @Any,eleserámuitoútilagora
quandovamos, programaticamente, buscarasdependênciasdanossaaplicaç ão.
77

## Página 83

4.8. Resoluçãodedependênciasobdemandaelookupprogramático CasadoCódigo
Atravésdessequalificadorconseguiremosrecuperartodasasinstânciascandidatas,
comopodemosveraseguir.
//forma tradicional lança exceção
@Inject @Any
private CalculadoraFolhaPagamento todasCalculadorasFolhaPagamento;
//injeção sob demanda
@Inject @Any
private Instance<CalculadoraFolhaPagamento> todasCalculadorasFolhaLazy;
Enquanto na forma tradicional nós teríamos uma exceção ao tentar injetar
CalculadoraFolhaPagamentousandooqualificador @Any,nainje çãosobde-
mandasóteríamosaexce çãosechamássemosométodo get().Masaquivaientrar
odinamismodedescobrirmosainstânciacorretaparaomomento.
@Inject @Any
private Instance<CalculadoraFolhaPagamento> todasCalculadoras;
...
if(simulacao){
Instance<CalculadoraFolhaPagamento> simuladoras =
todasCalculadoras.select(new SimuladorQualifier(){});
}
Ométodo selectdainterface Instancefiltraaspossibilidades,agoraemvez
detrês,temosapenasumcandidato: SimuladoraCalculoFolhaPagamento.
Masvamosanalisarmelhoralgunspontos.
Há uma sobrecarga do métodoselect, nos permitindo filtrar as possi-
bilidade através de qualificadores ou pelo tipo. Utilizamos aqui o filtro pelo
qualificador @Simulador, mas para fazer isso criamos uma classe chamada
SimuladorQualifier,comopodemosveraseguir.
public class SimuladorQualifier
extends AnnotationLiteral<Simulador> implements Simulador {
private PlanoDeCargos planoDeCargos;
private boolean planoAprovado;
private boolean enviarNotificacao;
public SimuladorQualifier(){
78

## Página 84

CasadoCódigo Capítulo4. Resolvendodependênciascomtipagemforte
this(PlanoDeCargos.VERSAO_2005, true, true);
}
public SimuladorQualifier(PlanoDeCargos planoDeCargos ,
boolean planoAprovado, boolean enviarNotificacao){
...
}
//os métodos da anotação simplesmente devolvem as propriedades
}
Como é possível ver, essa classe por padrão especificará o
PlanoDeCargos.VERSAO_2005 no processo de seleção, ou seja, é como se
estivéssemosdefinindoumpontodeinje çãocomoeste:
@Inject @Simulador(planoDeCargos = VERSAO_2013)
private CalculadoraFolhaPagamento calculadoraFolhaPagamento;
Porémcomoestamosusandoumqualificadorcompropriedades,temosesse
grande trabalho para reproduzir essa anotação programaticamente. Se fosse
umqualificadorsimples, sempropriedades, bastariautilizarmosaclasseutilitá-
ria javax.enterprise.util.AnnotationLiteral.Nãoprecisaríamosdessa
classe SimuladorQualifier,poderíamosreescreveroexemploanteriordase-
guintemaneira.
@Inject @Any
private Instance<CalculadoraFolhaPagamento> todasCalculadoras;
...
if(simulacao){
Instance<CalculadoraFolhaPagamento> simuladoras =
todasCalculadoras.select(new AnnotationLiteral<Simulador>(){});
}
Ainterface Instancenosofereceuma interface fluente,permitindoinvocações
seguidasdométodo select,ondepodemosiracadainvocaç ãorefinandomaiso
filtrodoscandidatosasupriradependência.Essemesmotipodelookupnósvoltare-
mosavernase ção7 . 4,porémemvezdeinjetardependências,estaremosutilizando
olookupparaespecificardinamicamenteoeventoqueserádisparado.
79

## Página 85

4.9. Resumodofuncionamentodaresoluç ãodedependências CasadoCódigo
4.9 R esumo do funcionamento da resolução de de -
pendências
Comoditonoiníciodocapítulo,essadefiniç ãoficouparaofinalpoisparachegar
aquipassamospordiversosexemplos,esemelesesseresumopoderiaficarmuito
abstrato. Essaseráumase çãoquetalvezvalhaapenavoltarpararelembrar,seja
durantealeituradestelivro,ouquandotiverdúvidasnosseusprojetos.
Jávimoscomofuncionamosqualificadoreseosbeansalternativos.Agorapo-
demosformalizarcomoaCDIresolveasdependênciasdeumaformaresumida.
Avaliandootipo
Oprimeiroelementoaserconsideradoéotipodoobjeto. Otipoqueestáno
pontodeinje ção,ouseja,aquelequeestápedindoadependência,éoquechama-
mosdetiporequerido.Serãoconsideradosbeanscandidatosaquelesquetêmtipos
compatíveiscomotiporequerido.Seestaforumainterfaceserãoaceitosbeansde
classesqueaimplementaesubclassesdessas. Seotiporequeridoforumaclasse,
serãoaceitosbeansdomesmotipooudesubtiposdorequerido.Ésóimaginarque
otesteseráfeitousando
instanceof,searespostaforverdadeira,obeanserá
elegível.
Quandosetratardeumtipoprimitivo,seráconsideradooseutipo w r a p p e r,ou
seja,otipodeum intserájava.lang.Integerevice-versa.
Seotiporequeridoforumtipogenérico,como Dao<X>,serãoaceitossomente
beanssemtipagemetipobaseexatamenteigual( Dao),oucomtipoparametrizado
compatível. Porexemplo, Dao<Y>,onde Yforcompatívelcom(nãoéomesmo
quesubtipode) X.Nosexemplosafrenteveremoscommaisdetalhes.Casootipo
requeridosejagenéricoenãoestejatipado,como Dao,obeaninjetadodeveráestar
semtipagemoutipadocom Object.
Porexemplo,setivermosadependênciaaseguir:
@Inject Dao<Pessoa> dao;
Nesse caso serão aceitos beans dos tiposDao, sem tipagem alguma, ou
Dao<Pessoa>.
Agoravamosconsiderarquetemostambémasseguintesclasses:
public class PessoaFisica extends Pessoa { ... }
public class PessoaDao extends Dao<Pessoa> { ... }
80

## Página 86

CasadoCódigo Capítulo4. Resolvendodependênciascomtipagemforte
Com esse cenário, só seria possível injetarDao<PessoaFisica> se
o ponto de injeção definisse @Inject Dao<? extends Pessoa> , pois
Dao<PessoaFisica>nãoéumtipocompatívelcom Dao<Pessoa>.Agora,no
casoemqueocoringafoiusado,temosumpontodeinje çãocompatívelpoisnão
limitamosotipoparametrizadoa Pessoa,emvezdissoincluímosseussubtipos.
Voltandoaopontodeinje ção @Inject Dao<Pessoa> dao ,conseguiríamos
tambéminjetarneleumainstânciade PessoaDao,poiséumtipocompatível.
Jáanalisandoosaarrays, sóserãoconsideradosseoscandidatosforemdo
mesmotipodorequerido;nãosãoconsideradosarraysdesubtiposdoesperado.Por
exemplo,vamosolharopontodeinje çãoaseguir:
@Inject Pessoa[] pessoas;
Aquiépossívelinjetarumarraydotipo Pessoa[],masnãoépossívelinjetar
umarraydotipo PessoaFisica[],pois,apesarde PessoaFisicaserumtipo
compatívelcom Pessoa,osrespectivosarraysnãosão.
Avaliandoosqualificadores
Alémdatipagem,temososqualificadoresealternativoscomojávimos.Casoo
pontodeinje çãoespecifiqueumqualificador,serãoconsideradosapenasosbeans
quetenhamtodososqualificadoressolicitados. Casonãoexistaumbeancomto-
dososqualificadoressolicitados,aCDIlan çaráumexceção,poisadependêncianão
podeserresolvida.
Paratodososefeitosdaresoluç ãodedependências,quandoumadependência
requeralgunsqualificadores,nãoadiantaterquasetodosdessesqualificadores,se
obeannãopossuiraomenosumdosrequeridos,elenãoseráescolhido. Jáseele
possuirosqualificadoresrequeridoseaindamais,nãohaveráproblema,oquenão
podeéfaltarumqualificador.
Aindasobequalificadores,precisamoslembrardeseusatributos,comojávi-
mos. Assimsendo,quandoumqualificadoréespecificado,sóserãoconsiderados
aceitáveisbeanscomosmesmosqualificadores,ecadaqualificadordeveter todos
osatributoscomosmesmosvaloresdoqualificadorrequerido.Aexce çãoéquanto
aosatributosanotadoscom
@Nonbinding,poisessesnãosãovinculantes.
Avaliandoosalternativos
Semprequetivermosváriosbeanscompatíveiscomadependênciarequerida,
ouseja,tipoequalificadoresaceitáveis,aCDIverificasedentreelesháalgumbean
81

## Página 87

4.9. Resumodofuncionamentodaresoluç ãodedependências CasadoCódigo
alternativo. Casoexista,osbeansnãoalternativossãodescartados,esomenteos
alternativos,quenaturalmentetemprioridade,serãoavaliados.
Dentreosbeansalternativosrestantes,seráescolhidoaqueledemaiorpriori-
dade,comovistonase ção 4.4. Casonãohajaumbeancomprioridadesuperior,
sejamalternativoscommesmaprioridadeouquandotivermosapenasbeansnãoal-
ternativos,aCDIlan çaráumaexceção,poisnãoterácritériosparaescolherentreos
elegíveis;éocasodaambiguidadequejávimosnessecapítulo.
82

## Página 88

Capítulo5
Ociclodevidadosobjetos
gerenciadospelaCDI
Assimcomotodaferramentadealtonível,comoJSFeJPA,quandotrabalhamoscom
CDItemosquelidarcomociclodevidadosobjetos.Apartirdomomentoemque
nãosomosnósqueinstanciamososobjetos,temosqueterumaformadeinteragir
comesseprocesso,ounomínimoentendercomoelefunciona.
Desdeocapítulo 3temosvistoqueparatermosumobjetoinjetável,umbean
CDI,bastaqueeleestejadentrodeumpacoteCDI.Nãoprecisamossequeranotara
classecomalgodaCDI.Issonãoquerdizer,porém,quenãotenhamosumaformade
construirobjetosquenãoestãoautomaticamentedisponíveisnoseucontexto.Para
issousaremososmétodosprodutores.
Temostambémumaformadeliberaralgunsrecursosquandoobjetossãodes-
truídos,sãocomométodosdestrutores. Eentreacria çãoeadestruiç ãodoobjeto
temosseutempodevida,queédefinidopeloescopo,maisumelementoqueveremos
nessecapítulo.

## Página 89

5.1. Métodosprodutores CasadoCódigo
5.1 Métodos produtores
Emalgumassituações,precisaremosinjetarumaclassequenãoéumbeanCDI,
comoainstânciadeumaclassedealgumabibliotecapré-existente. Umexemplo
dissoéousodeumabibliotecadelog,comoaSLF4J(www.slf4j.org).Paratal,vamos
voltaraoexemplodanossaprimeiraservlet,
IniciandoComCDI,etrocarnossas
escritasnoconsolepelousodoSLF4J.
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
@WebServlet("/hello-cdi")
public class IniciandoComCDI extends HttpServlet {
private Logger logger =
LoggerFactory.getLogger(IniciandoComCDI.class);
public IniciandoComCDI() {
//System.out.println("Instanciando a Servlet...");
logger.info("Instanciando a Servlet..." );
}
...
}
OusodaAPIdelogébemsimples,comoacabamosdever,masnãoseriamais
interessantesepudéssemosinjetaro Logger?
@Inject private Logger logger ;
Nessescasoséquevamosusarosmétodosprodutores.Novamentetemossorte,
poisaimplementaçãodoprodutoréalgoextramentesimples.
import javax.enterprise.inject.Produces;
public class Produtor {
@Produces
public Logger criaLogger(){
return LoggerFactory.getLogger(IniciandoComCDI.class);
}
}
84

## Página 90

CasadoCódigo Capítulo5. OciclodevidadosobjetosgerenciadospelaCDI
Bemsimples.Bastacriarmosummétodoanotadocom @Producesqueretorne
otipoquequeremosproduzir.Dessamaneira,quandoopontodeinje çãosolicitara
dependência,aCDIiráchamarométodoprodutorparageraroobjetoesperado.
QuandoocontextoCDIsobe,asdependênciassãotodaschecadasparaverse
tembeansqueassatisfaç am.ÉnessemomentoqueaCDIlan çaexce çõescasoa
dependêncianãopossasersatisfeitaouemcasodeambiguidade,queéquandoen-
contramaisdeumcandidatocompatível.Nocasodo Logger,comoestamosdiante
deumtipoquenãoépartedeumbeanCDI,onormalseriaserlan çadaumaexce-
çãodizendoqueadependêncianãopoderiasersatisfeita,mascomotemosométodo
produtor,aCDIsabequeconseguiráproduzirobeanquandofordemandada.
Comoométodoprodutorensinaumanovaformadeinstanciarumbean,caso
criemosumprodutordeumaclassequejáestádentrodonossoprojetooudeoutro
pacoteCDI,estaremoscriandoumaambiguidade,masnonossoexemploessenão
seráumproblema.
Porém,serepararmosbem,temosumproblemanonossoprodutor:elesópro-
duz
Loggersdaclasse IniciandoComCDI.Serviuparamostraromecanismo
básicodosprodutores,masobviamentenãovainosservirmais. Paraqueconse-
guíssemosresolveresseproblemaprecisaríamosterumaformadesaberemque
pontoestarásendoinjetadoobeanqueestamosproduzindo.Paraissotemosain-
terface
javax.enterprise.inject.spi.InjectionPoint,quenosdáexa-
tamenteessainformação.
Entreosmétodosdessainterfacetemosumquedevolveondeoobjetoestásendo
injetado.
public interface InjectionPoint {
java.lang.reflect.Member getMember();
...
}
Otipo java.lang.reflect.Memberéumainterface,abstraçãodeumcons-
trutor,deumapropriedadeoudeummétododeumaclasse. Comojávimosna
seção3.3,essessãoostiposdepontodeinje çãopossíveis.
No nosso exemplo, estamos injetando a dependência em uma propriedade,
que na API de reflection é do tipo
java.lang.reflect.Field, uma im-
plementação de Member. A partir desse tipo acessamos a classe onde a pro-
priedade está declarada através do métodogetDeclaringClass(), que nos
devolve o java.lang.Class que possui nossa propriedade, ou seja, o tipo
IniciandoComCDI.
85

## Página 91

5.1. Métodosprodutores CasadoCódigo
import javax.enterprise.inject.Produces;
public class Produtor {
@Produces
public Logger criaLogger(InjectionPoint ip ) {
return Logger.getLogger(ip.getMember()
.getDeclaringClass().getName());
}
}
Agoratemosnossoprodutorgenéricoparapoderproduzir Loggeremqualquer
lugardonossosistema.Porém,podeserqueprecisemosdemaisinformaç õespara
criarobean,porexemploousuáriologado,paraissobastainjetarmosesseobjeto
nonossoprodutor,afinaleleéumaclassenormal.
public class Produtor {
private Logger logger = LoggerFactory.getLogger(Produtor.class);
@Inject
private UsuarioLogado usuario ;
@Produces
public Logger criaLogger(InjectionPoint ip ) {
Class classe = ip.getMember().getDeclaringClass();
logger.info("Criando log para a classe " + classe +
" e para o usuário " + usuario);
return Logger.getLogger(classe.getName());
}
}
Nessecasousamosadependênciaextraapenasparagerarumlog,masvimos
comoinjetá-la.Entretanto,temosumaformaaindamaissimplesdefazerisso.Ape-
sardepodermostermétodosprodutoresemqualquerclasse,nãoéincomumtermos
umaclassenonossosistemacomaresponsabilidadedeproduzirdiversasdependên-
ciascomoo
Loggerqueacabamosdever.Senessaclassetivermosváriosmétodos
produtores,ealgunsdelesprecisaremdeumaoudiasinformaç õesextrasparagerar
obean,podeserqueaclassenofinaltenhaváriasdependências.Eissonãoéomaior
86

## Página 92

CasadoCódigo Capítulo5. OciclodevidadosobjetosgerenciadospelaCDI
problema,oqueocorreéquenãoficaclaroqualdependênciaestásendousadapara
produzirqualbean.
Pararesolveresseproblema,podemosinjetarasdependênciasnoprópriomé-
todoprodutor. Seolharmosdenovo,veremosqueopróprio InjectionPoint
foipassadoparanossométodocomoumadependência.Bastaseguirmosamesma
lógicaparaasdemaisdependências.
public class Produtor {
@Produces
public Logger criaLogger(InjectionPoint ip , UsuarioLogado usuario) {
...
}
}
Agora,sabemosexatamentequaisdependênciassãonecessáriasparaproduzir
nossobean.Alémdisso,aclasseficamaislimpa,eocódigomaiselegante.Esimpli-
cidadeeelegâncianuncafezmalacódigoalgum.
Comooprodutoréumaformadecolocarumaclassecomum(porexemplode
bibliotecanãoCDI)dentrodocontextoCDI,podemosespecificarnoprodutoras
mesmascoisasquepodemosanotarnaprópriaclasse,comoqualificadoreseescopos.
Oprimeirojáénossoconhecido,masosegundoserávistoaindanessecapítulo.
public class Produtor {
@Produces @QualificadorX @QualificadorY (VALOR_Z)
public Logger criaLogger(InjectionPoint ip , UsuarioLogado usuario) {
...
}
}
Propriedadeprodutora
Jávimosqueosmétodosprodutorespodemestarpresentesemqualquerbean,
masalémdeummétodo,podemosterumapropriedadeanotadacom @Produces.
Asregrassãobasicamenteasmesmasdosmétodos,adiferen çaéquecasoapropri-
edadeprodutoraestejadefinidadentrodeumEJBdotipoSessionBean,estadeverá
obrigatoriamenteserestática.
UmexemplodousodessafuncionalidadeécolocarmosnocontextoCDIobjetos
doJavaEE.
87

## Página 93

5.1. Métodosprodutores CasadoCódigo
public class ProdutorJava EE {
@PersistenceContext(unitName="organizacionalDatabase")
@Produces @OrganizacionalDatabase EntityManager organizacionalEM;
...
}
Nesseexemplo,nósusamosaformaJavaEEdeinjetaro EntityManagerdo
bancodedadosquechamamosde“organizacional”.Aomesmotempoproduzimos
essemesmoobjetocomoqualificador @OrganizacionalDatabase.Comisso,
asdemaisclassesdosistemapodemsimplesmenteinjetardessaforma:
@Inject @OrganizacionalDatabase
EntityManager organizacionalEntityManager ;
Avantagemdessatraduç ão—daformaJavaEEparaaCDI—équepodemos
usarapenasaformaCDIdeinjetardependências,ecomissorodarnossaaplicaç ão
tambémemambientesnãoJavaEE,comooTomcat.Nesseúltimoambientepode-
ríamosterummétodoprodutorcomooquesegue.
public class ProdutorJavaSE {
@Produces @OrganizacionalDatabase
public EntityManager criaEntityManager(){
EntityManagerFactory emf = Persistence
.createEntityManagerFactory("organizacionalDatabase");
return emf.createEntityManager();
}
...
}
Agora, com base no que já aprendemos sobre alternatives, poderíamos
marcar ambos produtores: ProdutorJava EE e ProdutorJavaSE como
@Alternativesehabilitarno beans.xmlapenasocorrespondenteaoambiente
queestivermosinstalandonossaaplicaç ão.
Restringindootipodobeanproduzido
Tantonosmétodosquantonaspropriedadesprodutoras, podemosutilizara
mesmaanotação @Typedvistanase ção4.7.Dessamaneiraobeanproduzidonão
serácandidatoasuprirdependênciasdetodosostipospossíveis,massomentedos
especificadosnaanotaçãoe java.lang.Object.
88

## Página 94

CasadoCódigo Capítulo5. OciclodevidadosobjetosgerenciadospelaCDI
@Produces @Typed( CalculadoraDeSalarios.class)
public CalculadoraDeSalariosPlano2013 criaCalculadora(){
return new CalculadoraAssincronaDeSalariosPlano2013();
}
5.2 Escopos daCDI
Comoestamosfalandodociclodevida,chegouahoradefalarmosdosescopos,meio
peloqualdefinimosotempodevidadeumbean.Atéagora,nossosexemplostêm
sidobaseadoemservlets,queserviramatéaquiporseremextremamentesimples,
masparafalarmosdeescopos,precisaremosdealgomaisflexível,poisasservlets
sãoobjetoscriadosumaúnicavezevivemenquantoaaplicaç ãoestiverrodando.
Comoacompanhamociclodevidadaaplicaç ão,écomosesemprefossemdoescopo
application.Digocomosefossempoisnãoespecificamosescoposemservlets.
Praexplorartodososescopospossíveis,pararemosdeusarasservletseusare-
mosJSF.NãoéobjetivodestelivroensinarJSF,masousaremosparaexemplificaros
escopos.VocêpodefazerusodeCDIcomoutrosframeworks,masaescolhadoJSF
éporserpartedoJavaEE,assimcomooCDI.ParasabermaissobreJSF,etambém
sobreJPA,recomendoolivro“AplicaçõesJavaparaawebcomJSFeJPA”daeditora
CasadoCódigo[?].
Antes de entrar em um escopo específico, vamos fazer uma tradução bá-
sica de uma de nossas servlets para um bean JSF. Iniciaremos pela servlet
IniciandoComCDI,eagoraquejápassamospelo hello world,poderemosdarum
significadomelhorparaessaclasse.
Ocódigoatualdelaéoseguinte:
@WebServlet("/hello-cdi")
public class IniciandoComCDI extends HttpServlet {
@Inject
private CalculadoraDeImpostos calculadoraImpostos;
public IniciandoComCDI() {
System.out.println("Instanciando a Servlet..." );
}
@PostConstruct
public void ok(){
89

## Página 95

5.2. EscoposdaCDI CasadoCódigo
System.out.println("Servlet pronta.");
}
protected void doGet(HttpServletRequest req,
HttpServletResponse res)
throws ServletException, IOException {
double salarioBase =
Double.parseDouble(req.getParameter("salario"));
Funcionario funcionario = new FuncionarioBuilder()
.comSalarioBaseDe(salarioBase)
.build();
System.out.println("Efetuando o cálculo.");
//a calculadora de IR usa outra classe para calcular o salário
double imposto = calculadoraImpostos
.calculaImpostoDeRenda(funcionario);
res.getOutputStream().print(
String.format("Salario base: R$ %.2f\n" +
"Imposto devido: R$ %.2f", salarioBase, imposto));
System.out.println("Fim.");
}
}
Oprimeiropassoparamudarmosnossaservlet,étransformá-laemumaclasse
Javasimples,tambémconhecidacomoPOJO(PlainOldJavaObject),ouseja,a
boaevelhaclasseJava,quenãoprecisaimplementarinterfacesouestenderclas-
sesdealgumframework.Agora,comonossaclassenãoémaisumaservlet,omé-
todo
doGetvaivirarummétodosimples,querenomearemosparaalgosignificativo,
como calculaImposto.Eaproveitandoamudan çadenome,vamosdartambém
umnomesignificativoparaaclasse:
public class CalculadoraImpostosBean {
@Inject
private CalculadoraDeImpostos calculadoraImpostos;
90

## Página 96

CasadoCódigo Capítulo5. OciclodevidadosobjetosgerenciadospelaCDI
public CalculadoraImpostosBean() {
System.out.println("Instanciando a CalculadoraImpostosBean..." );
}
@PostConstruct
public void ok(){
System.out.println("CalculadoraImpostosBean pronta.");
}
public void calculaImposto(HttpServletRequest req,
HttpServletResponse res)
throws ServletException, IOException {
double salarioBase =
Double.parseDouble(req.getParameter("salario"));
Funcionario funcionario = new FuncionarioBuilder()
.comSalarioBaseDe(salarioBase)
.build();
System.out.println("Efetuando o cálculo.");
//a calculadora de IR usa outra classe para calcular o salário
double imposto = calculadoraImpostos
.calculaImpostoDeRenda(funcionario);
res.getOutputStream().print(
String.format("Salario base: R$ %.2f\n" +
"Imposto devido: R$ %.2f", salarioBase, imposto));
System.out.println("Fim.");
}
}
Estamosmudandoaclasseaospoucos: porenquantomudamosbasicamente
onomedaclasse,inclusivenasmensagensquesaiamnoconsole. Agoravamos
arrumaraassinaturadométodo calculaImposto,queaindaestácomcarade
servlet. Colocaremosumapropriedadenanossa CalculadoraImpostosBean
que armazenará a informações que antes vinha do objetoreq, do tipo
HttpServletRequest.
91

## Página 97

5.2. EscoposdaCDI CasadoCódigo
public class CalculadoraImpostosBean {
//o resto permanece igual ...
private double salarioBase; //getters e setters
private double imposto; //getters e setters
public void calculaImposto() {
Funcionario funcionario = new FuncionarioBuilder()
.comSalarioBaseDe(salarioBase)
.build();
System.out.println("Efetuando o cálculo.");
imposto = calculadoraImpostos.calculaImpostoDeRenda(funcionario);
System.out.println("Fim.");
}
}
Nonossonovocódigooimpostoécalculadoearmazenadoemumaproprie-
dadedobean,poisnomundorealnossasclassesdenegócioapenasefetuamalógica
daaplicação,elasnãosãoresponsáveispelaapresentaç ãodosresultadosaousuá-
rio.ParaissocriaremosumapáginaJSFsimples,queapenasteráumcampoparaa
entradadosalárioenofinalapresentaráovalordoimposto.
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:h="http://xmlns.jcp.org/jsf/html">
<h:form>
<h:panelGrid columns="2">
Salário base:
<h:inputText value="#{calculadoraImpostosBean.salarioBase}"/>
Imposto Calculado:
<h:outputText value="#{calculadoraImpostosBean.imposto}"/>
<h:commandButton value="Calcular Imposto"
action="#{calculadoraImpostosBean.calculaImposto()}"/>
</h:panelGrid>
92

## Página 98

CasadoCódigo Capítulo5. OciclodevidadosobjetosgerenciadospelaCDI
</h:form>
</html>
Masantesdeexecutaressapágina,precisamosdarumnomeaonossobean,
comovimosnase ção4.5.Paraissotemosquefazerumaúltimaalteraç ãononosso
bean:
@Named
public class CalculadoraImpostosBean { ... }
Napáginaquecriamostemosocomponente h:panelGridqueserveapenas
parafazeraformataç ãodapágina.Comele,especificamosaquantidadedecolunas
quedesejamoster.Comoespecificamosduascolunas,significaqueacadadoiscom-
ponentes—noexemploalabeleocomponenteJSF—serácriadaumanovalinha.
Assimnãonospreocupamoscomoalinhamento,easaídajáficaráigualàseguinte:
Figura5.1:FormuláriodacalculadoradeimpostosfeitacomJSF
Osdemaiscomponestessãodeinputeoutputsimples,alémdobotãoqueexecuta
aação,chamandoométodoligadoàpropriedade action.
Seexecutarmosnossaaplicaç ãocomoestá,veremosqueovalorapresentadono
impostoestarázerado,masissoporquenãoespecificamosnenhumescopo.Emvá-
riosdosnossosbeansrealmentenãoespecificaremosnenhumescopoeissonãoserá
umproblema,porémsempassarpelosoutrosserámaisdifícilentenderesseescopo
default.Porisso,voltaremosafalardelenase ção5.7.
93

## Página 99

5.3. Escopoderequisiçãocom@RequestScoped CasadoCódigo
5.3 Escopo de requisição com @RequestS cop ed
Oescopo r e q u e s téomaiscomumemumaaplicaç ãoweb,poistodainteraç ãoentre
obrowsereoservidoréumrequest. Esseescopodefineumciclodevidaquese
inicianomomentoemquearequisiç ãodousuáriocheganoservidor,eduratodo
oprocessamentoetambémtodooprocessodegeraç ãodarespostaparaousuário.
Somentequandoarespostaparaousuárioéterminadaqueorequesttermina.
Parecesimples, maséprecisoficarmosatentosprincipalmenteaessaúltima
parte: ageraçãodarespostaparaousuário. Nãoadiantaacompanharmosaexe-
cuçãopassoaapassodetodaalógicadaaplicaç ãoeacharqueestátudocerto,pois
sealgoocorrerdepoisdoprocessamento,masantesdageraç ãodarespostaterminar,
aindapodemosterproblema,poisociclocomoumtodoéqueimporta.
Umaformadetentarmosilustrarofuncionamentodesseescopoéatravésda
figuraaseguir:
Figura5.2:Ilustraçãodoescoporequest
NafiguraexemplificamosachamadadaURL /editar.jsf.Comojáfoidito,
obeanécriadonomomentoemquearequisiç ãocheganoservidor,eterminano
94

## Página 100

CasadoCódigo Capítulo5. OciclodevidadosobjetosgerenciadospelaCDI
momentoemquesaidele. Novamenteprecisamosnosatentar,poisarespostaé
geradatodanoservidor. Àsvezes,emumaolhadarápida,podemospensarqueo
requestterminarianachegadadarespostaaobrowser,masessavoltanadamaisédo
queumatransferênciapelarededeumHTMLpronto.
Retornandoaonossoexemplo,bastacolocarmosaanotaç ãodoescoporequest
queascoisasfuncionarão:
import javax.enterprise.context.RequestScoped;
import javax.inject.Named;
@Named @RequestScoped
public class CalculadoraImpostosBean { ... }
A cada clique no botão "Calcular Imposto" estaremos disparando
uma nova requisição. A cada requisição, será criada uma nova instância de
CalculadoraImpostosBean,quereceberásuasdependênciasecalcularáoim-
posto. DepoisoJSF,assimcomofariaumapáginaJSP,acessaobeanparabuscar
osvaloresqueprecisaparamontarateladeresposta. Apósterminaragera çãoda
resposta,orequesttermina,ecomotodosessesbeansestãonesseescopo,nessemo-
mentoelessãoretiradosdamemória.
Comoesteéoprimeiroescopoqueestamosvendo,vamosvermaisumailustra-
çãoquenosauxiliaacompreenderesseciclo:
95

## Página 101

5.3. Escopoderequisiçãocom@RequestScoped CasadoCódigo
Figura5.3:Ciclodarequisiç ãodocálculodeimposto
Podemos dividir essa imagem em duas partes, a primeira mostra o pro-
cesso de criação do bean, parecido com o que fizemos na seção 3.1, mas na-
quelemomentousamosaanálisedeconsole,agoraestamosvendograficamente.
Nonossocasotemostrêsbeansenvolvidos CalculadoraImpostosBean ->
CalculadoraDeImpostos -> CalculadoraDeSalarios ,enossafigurailus-
traessadependência.
Na segunda metade, temos a chamada do método
calculadoraImpostosBean.calculaImposto() pelo botão da nossa
tela. E depois da resposta entregue ao navegador, os beans são removidos da
96

## Página 102

CasadoCódigo Capítulo5. OciclodevidadosobjetosgerenciadospelaCDI
memóriapoisoescopo—request—termina.
Sedesconsiderarmosachamadadométodoeanalisarmosapenasoprocesso
decriaçãodosbeans,eaofinalaseudescarte,estaremosanalisandoexatamente
omesmofuncionamentoindependentementedoescopo. Conformeformosanali-
sandoosdemaisescoposissoficarámaisclaro.
5.4 Escopo de sessão com o @SessionScop ed
Oprocessodecriaç ãoedescartedeumbeannãomudaseoescopoérequestou
session,oquemudaéquandooprocessoocorre.Enquantoorequestcompreende
cadainvoca çãoaoservidorfeitapelocliente,asessãoenglobatodasasrequisições
deummesmocliente. Parafacilitar,ésóimaginaroprocessodeautenticaç ãoem
umaaplicaçãoweb.Enquantotivermoscomobrowseraberto,estaremoslogadosna
aplicação,issoporqueasinformaçõesdeautenticaç ãocostumamficarnoescopode
sessão.
Cadavezqueacessamosumaaplicaç ãopelaprimeiravez,comumdeterminado
navegador,écriadaumanovasessão.Masissonãocriaautomaticamenteosbeans
deescoposessão,estesgeralmentesãocriadosquandoutilizadospelaprimeiravez,e
duramenquantoasessãoexistir.Enquantoconseguimosperceberpeloconsoleque,
noescoporequest,osobjetossãorecriadosacadasolicitaç ão;comoescoposessão,
sóperceberemosessacriaç ãoumavezparacadabrowserutilizado.
Geralmenteasessãoémantidaatravésdeumcookieouentãoalgumparâmetro
naurlqueégeradopeloservidor,assimconseguimosabrirmaisdeumasessãose
usarmosbrowsersdiferentesouachamadasessãoanônimasuportadapelosnavega-
doresmaismodernos.
Paratestaracriaç ãosessões,épossívelfecharobrowsereabrirnovamentepra
criarumanovasessão,masissonãosignificaqueaantigaseráfechada.Geralmente
oqueocorrequandoumusuáriofechaobrowsersemusaralgumaop ção“sair”da
aplicação,équeasessãoficaráinativanoservidor,ocupandorecursosdesnecessari-
amente,atéqueo timeoutsejaalcan çado.Issogeralmenteocorreapóstrintaminutos
deinatividade.
Aseguirumaimagemparailustraressefuncionamento.
97

## Página 103

5.4. Escopodesessãocomo@SessionScoped CasadoCódigo
Figura5.4:Ilustraçãodoescopodesessão
98

## Página 104

CasadoCódigo Capítulo5. OciclodevidadosobjetosgerenciadospelaCDI
Nodesenvolvimentodeaplicaçõesreais,muitasvezessurgemfuncionalidades
cujosestadossãomaisdifíceisdegerenciardoqueumasimplesrequisiç ão,eopri-
meiroimpulsopodesermudaroescopodobeanparasessão. Esseprocedimento
resolveoproblemaemtempodedesenvolvimento,mascriaumnovoproblemaem
tempodeexecuç ão.
Simplesmentepassarumbeanparaescopodesessãofazcomqueaaplicaç ão
passeaconsumirrecursosdeformaexagerada.Recursosquedeveriamsermanti-
dosporpoucasrequisi çõesacabamficandonamemóriaenquantoousuárioestiver
logado,umdesperdício.Amelhorpráticanaprogramaç ãocomoumtodo,ésem-
preusaromenorescopoqueresolvaoproblema,equandofalamosdeescopoissoé
aindamaisimportante.Antesdemudaroescopodeumbeanderequestparasession
poresteprimeiroparecerpequenodemaisparaafuncionalidade,olheoescopode
conversaçãonase ção5.6.
Comooexemplodasinformaçõesdeautenticaç ãodousuário,oescopodeses-
sãoserveparaarmazenarinformaç õesquedevemestaremmemóriadurantetoda
anavegaçãodousuárionaaplicaç ão. Outrosexemplospodemseraspermissões
dousuário,informaçõesdeperfildeacesso,nome,horadologin,entreoutrasque
possamserinteressantesdependendodaaplicaç ão.
5.5 @ApplicationScop ed:O maior escopo possível
Oescopodeaplicaç ãonãofogedofuncionamentopadrão,adinâmicaéamesma,a
diferençaestáemsuaamplitude.Enquantooescoporequestduraumaúnicarequi-
siçãodeumdeterminadousuário,esessãoenglobatodaautilizaç ãodosistemapor
umusuário,aaplicaçãoenvolvetodosusuáriodaaplicaç ão. Assim,secolocarmos
algonesseescopo,estarádisponívelparaqualquerusuárioqueacessaraaplicaç ão.
Umexemploseriaafuncionalidadedelistartodososusuáriosqueestãoonline,
equemsabeatéumchatentreeles.Éumescopoquecruzatodasassessões,então
setemosquetomarcuidadoaoporalgonoescoposessão,temosqueredobrarisso
noescopoaplicaç ão.
Aindacomoexemplodeaplicaçõesparaesseescopo,poderíamospensaremlis-
tagensfixas,comoestadosemunicípios. Essepodeserumusolegítimo,poisre-
almenteéalgocomumaqualquerusuário,masexistemoutrasop ções.Nessecaso,
podemosutilizarumcachedesegundonívelnacamadadepersistência,algodaJPA,
enãodaCDI.Umaboamaneiradedesenvolveraplica çõeséprocurarsempreusara
soluçãocorretaparacadaproblema.Muitasvezescolocaralgonoescopoaplicaç ão
99

## Página 105

5.5. @ApplicationScoped:Omaiorescopopossível CasadoCódigo
poderesolver,massepuderutilizarumasoluç ãodecache,teránasmãosumaop ção
maisrobusta.
Parailustrarofuncionamentodesseescopotemosaseguinteimagem:
Figura5.5:Ilustraçãodoescopodeaplicaç ão
Comovimos,oescoposóterminaquandobaixamosaaplicaç ão,entãocolo-
100

## Página 106

CasadoCódigo Capítulo5. OciclodevidadosobjetosgerenciadospelaCDI
candoalgoaqui,estaremosadicionandoalgonamemóriaqueficarálápormuito
tempo.
5.6 @ConversationS cop ed: Você criando seu pró -
prio escopo
Oescopodeconversaç ão,éumpoucodiferentedosanterioresporqueelepossui
doiscomportamentosdistintos. Nãobastaanotarobeancomesseescopo,temos
queescolherquandopassaraconversaç ãodeumestadoparaooutro.
Umaconversaçãoéumescopointeligente,queporpadrãosecomportacomo
oescoporequest,perdendoseuestadoacadarequisiç ão.Ointeressanteéquepo-
demosescolherumdadomomentoparaqueoescoposetornepersistente,comose
fosseoescopodesessão.Porém,enquantoestepermanecenamemóriapormuito
tempo,podemosdizeràconversaç ãoqueelavolteasecomportarcomooescopo
request,entãoosdadosnelaarmazenadossãodescartadosaofinaldapróximare-
quisição,eelavoltaasecomportarcomoorequest.
Oestadopadrão,parecidocomrequestéchamadode transient,queéquando
osestadosnãosãomantidos. Jáinvocandoométodo
Conversation.begin()
nossaconversaçãopassaparaoestado long-running,eestemantémosdadosatéque
ométodo Conversation.end()sejachamado,quandovoltaaser transienteos
dadosdeixamdeserarmazenados.Aimagemaseguirilustraessefuncionamento.
101

## Página 107

5.6. @ConversationScoped:Vocêcriandoseupróprioescopo CasadoCódigo
Figura5.6:Ilustraçãodoescopodeconversaç ão
102

## Página 108

CasadoCódigo Capítulo5. OciclodevidadosobjetosgerenciadospelaCDI
Vamosanalisarcomoimplementamosissononossocódigo. Comojáfoidito,
nocasodaconversaç ãonãobastaanotarobean,temosquedefinirquandoelapas-
sardeumestadoparaoutro.Criaremosnonossosistemaafuncionalidadedecal-
cularumafolhadepagamentobaseadoemumalistadefuncionáriosquevamos
adicionandoumaum. Nossoexemploserámaissimplesdoqueseriaumexem-
ploreal,eparasimplificar,emvezdeusarmosbancodedados,usaremosaclasse
FuncionarioBuilder.
import javax.enterprise.context.Conversation;
import javax.enterprise.context.ConversationScoped;
@ConversationScoped @Named
public classe CalculadoraFolhaBean implements Serializable {
@Inject
private Conversation conversation ;
@Inject
private CalculadoraFolhaPagamento calculadoraFolha ;
public void iniciaConversacao(){
if(conversation.isTransient()){
conversation.begin();
}
}
public void terminaConversacao(){
if(!conversation.isTransient()){
conversation.end();
}
}
...
}
O primeiro passo é criarmos um bean nomeado para que seja aces-
sível da nossa página JSF. Como acabamos de ver, não basta anotar
o bean com o escopo, precisamos injetar uma instância da interface
javax.enterprise.context.Conversation e utilizá-la para gerenciar
osestadosdaconversaç ão.Alémdeiniciarefinalizaraconversaç ão(alternarentre
103

## Página 109

5.6. @ConversationScoped:Vocêcriandoseupróprioescopo CasadoCódigo
transiente long-running),temosométodo setTimeout(long milliseconds),
queusamosparamudarotimeoutdessaconversaç ãoespecífica.Injetamostambém
uma instância de CalculadoraFolhaPagamento que é quem sabe fazer o
cálculoqueprecisamos.
É importante também que nosso bean, e todos os beans injetados, como
CalculadoraFolhaPagamento,implementemainterface Serializable.Sem
issoserálançadaumaexce çãoduranteainicializaç ãodaaplicaç ão.
Criaremosumatelasimples,ondepodemosinformarosaláriodeumfuncioná-
rioeadicioná-lonalistaatravésdeumbotão.Teremosumoutrobotãoparaefetuaro
cálculoeoutrosdoisparainiciareterminaraconversaç ão.Alémdessescomponen-
tes,escreveremosaquantidadedefuncionárioquejáestãonalista,e,assim,vamos
percebendoaalteraç ãodeestadodonossobeanantesdecálculo.Ocódigodatela
podeservistoaseguir.
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:h="http://xmlns.jcp.org/jsf/html">
<h:form>
<h:panelGrid columns="2">
Salário base: <h:inputText
value="#{calculadoraFolhaBean.salarioFuncionario}"/>
Funcionário adicionados: <h:outputText
value="#{calculadoraFolhaBean.funcionarios.size()}"/>
Valor da Folha: <h:outputText
value="#{calculadoraFolhaBean.folha != null ?
calculadoraFolhaBean.folha.valor : 'Não calculado '}"/>
<h:commandButton value="Inicia Conversação"
action="#{calculadoraFolhaBean.iniciaConversacao()}"/>
<h:commandButton value="Termina Conversação"
action="#{calculadoraFolhaBean.terminaConversacao()}"/>
<h:commandButton value="Adicionar Funcionário"
action="#{calculadoraFolhaBean.adicionaFuncionario()}"/>
<h:commandButton value="Calcular Folha!"
action="#{calculadoraFolhaBean.calcularFolha()}"/>
</h:panelGrid>
</h:form>
</html>
Nossatela,quandoexecutando,separecerácomessa:
104

## Página 110

CasadoCódigo Capítulo5. OciclodevidadosobjetosgerenciadospelaCDI
Figura5.7:Teladecálculodefolha
Porém ainda precisamos do restante da implementação da classe
CalculadoraFolhaBean:
@Named @ConversationScoped
public class CalculadoraFolhaBean implements Serializable{
...
private FuncionarioBuilder builder;
private Folha folha ; //getter
private List<Funcionario> funcionarios; //getter
private double salarioFuncionario; //getter e setter
@PostConstruct
public void init(){
builder = new FuncionarioBuilder();
funcionarios = new ArrayList<>();
}
public void adicionaFuncionario(){
Funcionario funcionario = builder
.comSalarioBaseDe(salarioFuncionario).build();
getFuncionarios().add(funcionario);
105

## Página 111

5.6. @ConversationScoped:Vocêcriandoseupróprioescopo CasadoCódigo
}
public void calcularFolha(){
folha = calculadoraFolha.calculaFolha(getFuncionarios());
}
}
E como até agora não tínhamos visto a implementaç ão da
CalculadoraFolhaPagamentoReal,veremosagora:
public class CalculadoraFolhaPagamentoReal implements
CalculadoraFolhaPagamento, Serializable {
@Inject
private CalculadoraDeSalarios calculadoraDeSalarios;
@Override
public Folha calculaFolha(List<Funcionario> funcionarios) {
double valor = 0.0;
for (Funcionario funcionario : funcionarios) {
valor += calculadoraDeSalarios.calculaSalario(funcionario);
}
return new Folha(new Date(), valor, funcionarios);
}
}
Nossa calculadora está pronta para ser testada. Experimente digitar o sa-
láriodofuncionárionocampocorrespondenteeacioneobotão "Adicionar
Funcionário".Altereovalordosalárioeacioneobotãonovamente.Vocêperce-
beráqueseminiciaraconversaç ão,nuncaconseguirásairdeumúnicofuncionário
adicionado.
Seobservaraimagem 5.6,perceberáqueantesdeiniciaraconversaç ão,obean
morrelogoapósotérminodarequisiç ão. Assim,pormaisqueatelaapresente
ainformaçãodequealistajácontémum Funcionario, noservidorobean
CalculadoraFolhaBeanjáfoidestruído,equandoacionarobotão "Adicionar
Funcionário"maisumavez,estaremosnaverdaderecriandotodososobjetos,e
adicionandonelesoprimeiro Funcionarionovamente.
Apartirdomomentoemqueclicamosnobotão "Inicia Conversação",
transformamos a conversação em long-running conversation, e com isso a
106

## Página 112

CasadoCódigo Capítulo5. OciclodevidadosobjetosgerenciadospelaCDI
CalculadoraFolhaBeannãomorremaisapósotérminodarequisiç ão.Nospró-
ximosacionamentosdessebotãoperceberemosqueacontagemdefuncionáriosvai
aumentando,epodemosfinalmenteusarobotão "Calcular Folha!".
Experimentetambémutilizarobotão "Termina Conversação",eperceba
quenapróximaaç ãonossaaplicaç ãosecomportaránovamentecomosefosseapri-
meiraexecução.Issoporque,aotransformarmosumaconversa ção long-runningem
transient,fazemoscomqueobean CalculadoraFolhaBeanvolteaserdescar-
tadoaofinaldecadarequisiç ão.
Nesseexemploutilizamosumúnicobeaneumaúnicatelaparafacilitaroenten-
dimento,masumaconversaç ãopodedurarporváriastelasediferentesbeandentro
danossaaplicaç ão.Realmenteesseéumescopobastanteversátil.
Alémdesseescopoteromodo“liga-desliga”dearmazenamentodedados,ainda
queesque çamosdefinalizaraconversaç ão,elanãoserácomoasessãoqueguardaos
valoresporumlongotempo,porexemplo,trintaminutossenadaforfeito.Nocaso
daconversação,mesmoqueestejanoestado long-running,osdadossãodescartados
quandoaconversaçãoatingeseu timeout.Avantageméqueessetimeoutnãocoin-
cidecomodasessão,porpadrãoédeapenasdoisminutos,economizandorecursos
maisdoqueasessão,aindaqueesque çamosdefinalizaraconversaç ão.
Podeparecerumaboaop çãodiminuirotempodasessãoparaeconomizarrecur-
sos,masissonoslevaaefeitosindesejados.Sedeixarmosumtempomuitopequeno,
podemosderrubarasessãodeusuáriosqueestãolendoalgumtextonateladosis-
tema,eissopodecausarcertodesconforto. Mesmoquevocêtenhaoutrosmeios,
comocookies,paramanteraautenticaç ãodousuário,certamenteperderáoutrasin-
formaçõesqueousuáriopossarterpreenchidopoucoantesiniciaraleituradotexto.
Novamentedevemosbuscaraferramentacertaparacadaproblema,enamaio-
riadassitua çõesveremosqueaconversaç ãoéumescopomaisapropriadoparaas
funçõesdanossaaplicaç ãodoqueasessão.
QuandoestivermosvendoumpoucosobreCDIjuntamentecomEJBs,vere-
mosqueesseescopotrazoutrasvantagens,comoacapacidadedemanterabertoo
contextodepersistência,
EntityManager,durantetodaaconversaç ão.Comisso
temosavantagemdocachedeprimeironívelsempreàmão,mantendoosobjetos
persistentessempregerenciados.MesmoEJBsnãosendoobjetodestelivro,veremos
umpoucomaissobreissoquandoestivermosapreciandoaintegraç ãodaCDIcom
osdemaiselementosdoJavaEE.
107

## Página 113

5.7. @Dependent:OescopopadrãodoCDI CasadoCódigo
5.7 @Dependent:O escopo padrão do CDI
Oescopodependentefoioprimeiroqueutilizamosnosnossosexemplos,econ-
tinuamosautilizá-lootempotodo. Esseéopadrão, aqueleatribuídoaobean
quandonãoespecificamosoutro.Paranossaanálise,vamosutilizaromesmoexem-
plodoescopodeconversaç ão,ondetemosobean
CalculadoraFolhaBeanea
CalculadoraFolhaPagamento. Enquantooprimeirotemodeconversaç ão,o
segundo,quenãoespecificanenhumexplicitamente,temescopodependente.
Agoraquetemosumexemplo,oentendimentodesseescopoésimples.Vimos
quea CalculadoraFolhaPagamentotemescopodependente,masdependente
dequem?Do CalculadoraFolhaBean,quefoiquemsolicitouainje çãodobean
dependente.Assim,senossobeannãoespecificarumescopo,eleseguiráodequem
osolicitar.
Antesdeiniciarmosaconversaç ãolonga,tantoo
CalculadoraFolhaBean
quantoo CalculadoraFolhaPagamentoestavamfuncionandocomescopode
conversaçãoemmodotransiente.Apósiniciarmosaconversaç ão,ambospassaram
para long-running conversation.Quandoumécriado,ooutrotambém,eomesmo
ocorrenocasodadestruiç ãodobean.Naimagemaseguir,temosumailustraç ãode
comooescopodependentesecomportaquandoestiverdependendodeumescopo
request.
108

## Página 114

CasadoCódigo Capítulo5. OciclodevidadosobjetosgerenciadospelaCDI
Figura5.8:Ilustraçãodoescopodependentejuntoaoescoporequest
Eagoraumaimagemquemostraoescopodependentesendoutilizadoporum
beancomescopodesessão. Adinâmicaéamesmadequandoéutilizadoporum
beancomescoporequest.Odependentesempresegueociclodevidadobeanprin-
cipal.
109

## Página 115

5.7. @Dependent:OescopopadrãodoCDI CasadoCódigo
Figura5.9:Ilustraçãodoescopodependentejuntoaoescopodesessão
Ondedefinirosescoposequaisasrestri ções?
Nãoexisteumaregrasobreondedefinirumescopo,masomaiscomumédefi-
nirmosnosbeansnomeados,queserãoacessadospelasnossaspáginasJSFouJSP,e
estesusamosbeanscomescopodependente,esãobuscadosviatipoenãopornome.
110

## Página 116

CasadoCódigo Capítulo5. OciclodevidadosobjetosgerenciadospelaCDI
Nadaimpedenoentantoquebeansnãonomeadostenhamescoposdefinidos.
U m a r e s t r içãoquetemosquantoaescopos, équebeanssóacessamoutros
com escopo igual ou maior que o seu. Por exemplo, não tem como um bean
@ApplicationScopedinjetarumbean @RequestScoped,porémocontrário
épossível.
Também não há restrição que impeça deixarmos um bean nomeado
com escopo dependente, mas se olharmos a primeira versão do nosso bean
CalculadoraImpostosBean definido na seção 5.2veremos que ela não fun-
cionava. IssoporqueobeanestavasendoacessadodiretamentepelapáginaJSF
masnãotinhaumescopopróprio,eradependente. Assim,cadavezqueapágina
tentavaacessarobean,ouacadaELquechamavaseunome,eracriadoumnovo
bean.Então,éobvioquequenãofuncionaria,poisovalorinformadopelousuário
acabariadescartadologoemseguida.
5.8 Métodos finalizadores
Quandoumobjetoécriadopeloprópriocontainer,porexemplooservidordeaplica-
çõesJBossouGlassfish,estetemaresponsabilidadedegerenciartambémodescarte
desseobjeto.PorémquandonósmesmosocriamoseoinserimosnocontextoCDI
atravésdeummétodooupropriedadeprodutora,nóstemosquecuidarparaqueo
objetosejaretiradodamemóriadeformacorreta.
Umexemploéaproduç ãodeum
EntityManagercomovimosnase ção5.1.
Quandoinjetamosumainstânciausandoaanota ção @PersistenceContext,
é porque o servidor de aplicações gerencia esse objeto para nós. Assim
sendo, não precisamos chamar o método
EntityManager.close()
pois o servidor faz isso. Agora se o criamos manualmente usando
Persistence.createEntityManagerFactory.criaEntityManager,
nóséquetemosaresponsabilidadedefechá-lo.
Parafazerisso,bastadefinirmosummétodoeanotarapropriedadequequere-
mosfecharcom @Disposes:
import javax.enterprise.inject.Disposes;
public class ProdutorJavaSE {
@Produces @OrganizacionalDatabase
public EntityManager criaEntityManager(){
111

## Página 117

5.8. Métodosfinalizadores CasadoCódigo
EntityManagerFactory emf = Persistence
.createEntityManagerFactory("organizacionalDatabase");
return emf.createEntityManager();
}
public void fechaEntityManager(
@Disposes @OrganizacionalDatabase EntityManager em ){
em.close();
}
}
Oprocessodevinculaç ãodométodo d i s p o s e raoobjetoqueserádescartado
segueamesmapolíticadaresoluç ãodedependênciaparaospontosdeinje ção.
Percebaqueométodofinalizadorpareceummétodoinicializador,queéanotado
com @Injecteemcadaparâmetrodeclaraumadependência.Adiferen çaéque,
emvezdeanotarométodo,anotamosapropriedadequequeremosdestruircom
@Disposes,easdemaisanota çõeseotipodeclaradoservemparaespecificaros
objetosquepodemserfinalizadosatravésdonossométodo.
Assimcomonométodoinicializador,podemosdeclararmaisparâmetrosnomé-
todofinalizador,adiferen çaéquesomenteumdelesseráreferenteaoobjetoqueserá
destruído,osdemaisserãopontosdeinje ção.
...
public void fechaEntityManager(
@Disposes @OrganizacionalDatabase EntityManager em ,
Logger logger ){
logger.info("Fechando EntityManager");
em.close();
}
...
Nesseexemplooparâmetro Logger logger éumpontodeinje çãoassim
comopodemosternométodoprodutor,eserveparaauxiliarnoprocessodefinaliza-
çãodoobjeto.Poderiainclusiveterqualificadorescomoqualquerpontodeinje ção.
Noentantosemaisdeumparâmetroestiveranotadocom @Disposes,ouseaCDI
encontrarmaisdeummétodofinalizadorparaomesmobean,serálan çadoumerro
duranteasvalidaçõesfeitasquandoaaplicaç ãoéiniciada.
112

## Página 118

Capítulo6
InterceptorseDecorators
Nestecapítuloveremosduasfuncionalidadesmuitointeressantes: interceptorse de-
corators.Sãomecanismostecnicamenteparecidos,massemanticamentebemdife-
rentes.Ambosnospermitem,cadaumcomsuaaplicabilidade,estendernossaapli-
caçãodeformaelegante,semmexer,oumexendomuitopoucononossocódigo.
6.1 Implementando requisitos transversais com in-
terceptors
Uminterceptor,ouinterceptador,éumaespéciede web filterdaAPIdeservlets,mas
emvezdeagirnasrequisiç õesweb,funcionanasinvocaçõesdemétodosdoscompo-
nentesCDI.Osinterceptadorestêmessenomeporqueelesinterceptamachamada
demétodoepodemexecutaraçõesespecíficasantes,depoisounolugardarequisi-
çãooriginal.
Secompararmosofuncionamentodofiltroedointerceptador,veremosmuitas
semelhanças.

## Página 119

6.1. Implementandorequisitostransversaiscominterceptors CasadoCódigo
Figura6.1:Funcionamentodosfiltrosweb
Basicamenteosfiltroswebsãoobjetosqueinterceptamachamadaparauma
servletbaseadosemumpadrãodeurl,quenoexemploforam /* e /priv/* .
Jáointerceptor,comoveremosnaimagemaseguir,temomesmofunciona-
mentomas,emvezdepadrãodeurl,baseia-seemanota çõesespecíficasparainter-
ceptaraschamadasdemétodos.Alémdisso,emvezdeservlets,comosintercepta-
dorestrabalhamosnoníveldebeansCDIeseusmétodos.
Figura6.2:Funcionamentodosinterceptadores
Equalavantagemdisso?Talvezsevocênuncacriouum filter,nãoimaginapor
queusariaum interceptor.Essetipodefuncionalidadeémuitoimportanteparaim-
114

## Página 120

CasadoCódigo Capítulo6. InterceptorseDecorators
plementarmosrequisitostransversaisdosistema.Porexemplo,requisitosdesegu-
rança.
Enquantonumfiltrowebpoderíamosespecificarquetodasasrequisi çõesdosis-
temasópodemserrealizadasseousuáriojátiverfeitologin,podemosespecificar
queummétodoespecífico,outodososmétodosdeumadeterminadaclasse,sópode
serexecutadoporumapessoacomdeterminadoperfil.Ouainda,queapósaexecu-
çãodequalquermétododeumaclassedevesergeradoumlog,assimcomofaríamos
aogerarumlogdequalquerrequisiç ãoweb.
Ofuncionamentoésimples,masumexemplofacilitaaindamais:
@WebFilter("/*")
public class FiltroAutenticacao implements Filter {
@Inject
private Logger logger ;
@Override
public void doFilter(ServletRequest request,
ServletResponse response, FilterChain chain )
throws IOException, ServletException {
//faz um processamento prévio
HttpServletRequest req = (HttpServletRequest) request;
HttpSession session = req.getSession();
Object usuario = session.getAttribute("usuarioLogado");
String paginaDeLogin = "login.jsf";
String paginaAtual = req.getRequestURI();
if(usuario == null && !paginaAtual.endsWith(paginaDeLogin )){
//envia para tela de autenticação
logger.info("usuário não autenticado");
((HttpServletResponse)response).sendRedirect(paginaDeLogin);
}
else {
//chama a ação original
chain.doFilter(request, response);
//faz processamento posterior
115

## Página 121

6.1. Implementandorequisitostransversaiscominterceptors CasadoCódigo
logger.info("terminando requisição para " + paginaAtual);
}
}
...
}
Comoacabamosdever,criamosumfiltrowebquefor çaousuárioaseau-
tenticar. Poderíamos fazer qualquer tipo de lógica antes e depois da execução
doqueousuáriopretendiafazer, queérepresentadapelachamadadométodo
%chain.doFilter(request, response).Eomaisinteressante:comoacha-
madadessemétodoéoquedisparaaexecuç ãoalvodousuário,épossível,baseado
emalgumcritério,optarmossimplesmentepornãofazeressachamada,oufazer
umaoutracoisaemseulugar.Éoqueocorrequandoousuárionãoseautenticouno
sistema.Nolugardeprocessarmosarequisiç ãoparaapáginaqueeletentavaacessar,
enviamo-loparaateladelogin.Trocamosaa çãooriginaldousuárioporoutramais
apropriadanomomento.
Deformabastantesemelhantepodemosdefiniruminterceptor:
@Interceptor @Priority (Interceptor.Priority.APPLICATION)
public class Auditor {
@Inject
private Logger logger ;
@AroundInvoke
public Object auditar(InvocationContext context) throws Exception {
//faz processamento antes
logger.info("faz processamento anterior" );
Method method = context.getMethod();
Object target = context.getTarget();
Object[] params = context.getParameters();
logger.info(String.format("auditando o método: '%s' "
+ "do objeto: '%s' "
+ "com os parâmetros: '%s'", method, target, params));
116

## Página 122

CasadoCódigo Capítulo6. InterceptorseDecorators
//chama o método original
logger.info("chama método original" );
Object retorno = context.proceed();
//faz processamento posterior
logger.info("faz processamento posterior" );
return retorno;
}
}
Adiferen çaéqueointerceptorestátrabalhandodentrodocontextoCDI,mas
assimcomonofiltro,podemosfazeroperaçõesantes,depois,oumesmosubstituir
aexecuçãooriginalporoutracoisa,quepodeinclusivenãofazernada. Paraisso,
bastariacolocarainvoca çãodométodo context.proceed()dentrodeum if
quechecassenossoscritérios.Éumaformamaissimples,masqueatendeàmaioria
doscasosdoqueanteriormentefazíamoscomprograma çãoorientadaaaspectos,ou
AOP.
Emcomumtambématodasessasformasdeimplementarrequisitostransversais
estáoforteapelosemânticodenãoutilizá-lasparaimplementarrequisitosfuncio-
nais. Issoquerdizerquenãodevemoscodificarrequisitosdenegócioalidentro,
comoalgumtipodecálculo.Paraessaaplicaç ãotemosos decorators,penseemin-
terceptadoresapenasparavalidaçõesdeacesso,auditoriaeoutrasregrasgerais.
Pormaisqueusandoainterface
InvocationContextsejapossível,concei-
tualmenteuminterceptadornãodevesaberqualclasseestáinterceptando. Obvia-
mente,saberquemestásendointerceptadonãoéoproblema,podemosusaressa
informaçãoparagerarumlog,porexemplo,masnãoparatomarumadecisãode
negócio.Sevocêachaquetemessanecessidade,talvezomelhorsejacriarumoutro
interceptadorcomumafun çãoespecífica,emvezdefazer i f sdentrodeumsó,ou
entãocriarum decorator.
Masseointerceptadornãosabequemestáinterceptando,comofazemosali-
gaçãoentreambos? Fazemosatravésdos interceptor bindings. Issonadamaisédo
que uma anotaçãoqueécolocadanointerceptadorenasclassesoumétodosque
desejamosinterceptar.
import javax.interceptor.InterceptorBinding;
117

## Página 123

6.1. Implementandorequisitostransversaiscominterceptors CasadoCódigo
@Retention(RetentionPolicy.RUNTIME)
@Target({ElementType.TYPE, ElementType.METHOD})
@InterceptorBinding
public @interface Auditavel {}
Assimcomoumqualificador,quevimosnase ção 4.2,podemosteratributos
dentrodos interceptor bindings, eamenosqueapropriedadesejaanotadacom
@javax.enterprise.util.Nonbinding,sóserãoligadosbeanseinterceptors
queespecificaremosmesmosvaloresparacadapropriedadenaanota çãoquefaza
relação.
Criadaaanotaçãovinculadora,anotamosaclasseoumétodoquedesejamosau-
ditar.
@Auditavel
public class GestoraDePermissoes { ... }
public class GestoraDePermissoes {
@Auditavel
public void mudaPermissoes(Funcionario f, Permissao[] permissoes) {
...
}
}
Podemos também adicionar a meta-anotaç ão
@java.lang.annotation.Inherited no interceptor binding, dessa forma
nossa anotaçãoseráherdável. Nonossoexemplo, significaqueclassesfilhasda
GestoraDePermissoestambémserãoauditáveis.
@Retention(RetentionPolicy.RUNTIME)
@Target({ElementType.TYPE, ElementType.METHOD})
@Inherited
@InterceptorBinding
public @interface Auditavel {}
@Auditavel
public class GestoraDePermissoes { ... }
public class GestoraAssincronaDePermissoes
extends GestoraDePermissoes { ... }
118

## Página 124

CasadoCódigo Capítulo6. InterceptorseDecorators
Alémdisso,comoveremosnase ção7 . 1,podemoscolocarumoumais interceptor
bindingsdentrodeestereótipos. Assim,umbeancomesseestereótipopassaaser
interceptadoautomaticamente.Arestriç ãonessecasoéquesópodemoscolocarem
estereótipos interceptor bindingscom @Target(ElementType.TYPE).
Herdando anotações
Apesardenãotermoscomentadodessapossibilidade,podemosutili-
zaraanotaç ão @java.lang.annotation.Inheritedtambémnos
qualificadores,masessapossibilidadeédesestimuladapelaespecificaç ão.
Enquantoaclassefilhadeumtipointerceptadoprovavelmentemere ça
serinterceptadotambém,osqualificadorespreferencialmentedevemser
usadocommoderaç ão.
No exemplo que vimos, faz sentido a
GestoraAssincronaDePermissoes ser auditável, afinal, ela
tambéméuma GestoraDePermissoes,eéauditada.
Jáquandotrabalhamoscomqualificadores,temosointuitodeindivi-
dualizaraomáximocadabean,eseseussubtiposherdaremseusqualifi-
cadoresteremosmaischancesdeaconteceremproblemasdeambigui-
dade. Sequisermosqueumsubtipotenhaosmesmosqualificadores,
podeserocasodeusarmos
@Specializes,comovimosnase ção4.6.
Aindafaltaalgoparaquenossointerceptorfuncionecomopretendido:adicio-
narneleaanota çãovinculante. Podemosinclusivecolocarmaisdeumaanotaç ão
de bindingnomesmointerceptor,masnonossoexemplousaremosapenasarecém
criada @Auditavel.
@Interceptor @Auditavel @Priority(Interceptor.Priority.APPLICATION)
public class Auditor {
...
}
Agorasimtemosnossointerceptadorfuncionandocomoesperávamos, pois
alémdeespecificarqual interceptor bindingeleusará,jáoativamoscomaanota-
ção @Priority. Assimcomofizemoscomosbeans a l t e r n a t i v e s,utilizamosessa
anotaçãonãosóparaativar,mastambémparadefiniraprioridade,ouordemde
119

## Página 125

6.1. Implementandorequisitostransversaiscominterceptors CasadoCódigo
execuçãodonossointerceptor. Isso,porém,sóépossívelseestivermosutilizando
CDI1.1.
Seestivermosutilizandoaversão1.0,precisaremosregistrarnossosintercepta-
doresviaarquivo beans.xml,enãoconseguimosdefiniraordemdeexecuç ãodos
mesmos;pelomenosnãosemutilizaralgumaconfiguraç ãoespecíficadealguma
implementaçãooubibliotecaauxiliar.Paraativarnossointerceptadorsemutilizara
anotação @Priority,precisaremosconfigurardaseguintemaneira.
<beans xmlns="http://xmlns.jcp.org/xml/ns/javaee"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
http://xmlns.jcp.org/xml/ns/javaee/beans_1_1.xsd">
<interceptors>
<class>
br.com.casadocodigo.livrocdi.interceptador.Auditor
</class>
<class>...</class> <!-- um interceptador em cada tag class -->
</interceptors>
</beans>
Assimcomonãoconseguimosdefiniraordemdeexecuç ãoapenascomoar-
quivo beans.xml,nãotemoscomodefiniraordemdeexecuç ãodosintercepta-
doresseestespossuíremamesmaprioridade( @Priority). Porém,setivermos
interceptadorescomprioridadesdiferentes,seráexecutadoprimeiroaquelequeti-
verumnúmerodeprioridademenor.Ouseja,interceptadorcomprioridade1(um)
executaantesdoquetiverprioridade10(dez).
Apesardetermosvistoumfuncionamentoparecidocomodofiltroweb,uti-
lizandoaanotaç ão
@AroundInvoke,épossíveldefinirmosmaisalgunsmodosde
interceptaçãocomCDI.Todosostiposqueveremosaseguirutilizamamesmaforma
defazer bindingentreobeaninterceptadoeointerceptador,adiferen çaficaapenas
nomomentoemqueométododointerceptadorseráchamado.
Interceptador@AroundTimeout
Estetipodeinterceptadoréutilizadoquandodesejamosinterceptaraexecuç ão
demétodosinvocadospeloserviçode time rdoJavaEE.Sãoaquelesmétodosgeral-
menteanotadoscom @Timeoutou @Schedule:
...
@Schedule(hour = "*", minute = "*/10")
120

## Página 126

CasadoCódigo Capítulo6. InterceptorseDecorators
public void importaDadosDoFTP(){
...
}
...
Nesse exemplo, consideramos que nosso sistema a cada 10 (dez) minutos
buscaalgumtipodedadonoFTP.Porém, esseservi çodetimersófuncionase
nossobeanfoiumEJB,enossosexemplosnãosãoEJBs. Comoestamosfalando
deinterceptadores, éimportantecitarmosessetipo. Parainterceptarmosasin-
vocações dos métodos disparados pelo serviço de timer, utilizamos a anotação
@javax.interceptor.AroundTimeout,comopodemosveraseguir.
...
@AroundTimeout
public Object timer(InvocationContext context) throws Exception {
//faz algo antes
Object target = context.getTarget();
Object retorno = context.proceed();
//faz algo depois
return retorno;
}
...
Éinteressantenotar,ainda,queométodo importaDadosDoFTP()podeserin-
vocadotantopeloservi çode time rquantodiretamenteporumclientedoEJBnoqual
eleestádefinido.Porémcomotemosduasformasdechamaromesmométodo,po-
demostertantouminterceptador @AroundTimeoutquantoum @AroundInvoke
aptosainterceptaressemétodo.Comosabemosqualseráchamado?ACDIcuida
dissocorretamente. SeométodoforchamadodiretamentepeloclientedoEJB,o
interceptadorutilizadoseráo
@AroundInvoke,masseforchamadovia time r,será
utilizadoo AroundTimeout.
6.2 Interceptadores de ciclo de vida
Alémdostiposdeinterceptadoresquevimos, existemosinterceptadoresdeci-
clo de vida. Dois deles utilizam anotações que já usamos há muito tempo:
121

## Página 127

6.2. Interceptadoresdeciclodevida CasadoCódigo
@PostConstructe @PreDestroy,eservemparainterceptaromesmomomento
queativaosmétodosanotadosporelas.Jáoterceiro,nospermiteinterceptarocons-
trutordosbeans,eseráporelequeiniciaremos.
Interceptador@AroundConstruct
Aoutilizaraanotação @javax.interceptor.AroundConstructdefinimos
uminterceptadorque,emvezdeinterceptarachamadadeummétodoqualquerdo
nossobean,interceptaachamadadoseuconstrutor.
...
@AroundConstruct
public void interceptaConstrutor(InvocationContext context)
throws Exception {
context.proceed(); //chama o construtor interceptado
Object objetoRecemCriado = context.getTarget();
}
...
Comonessecasoestamosinterceptandooconstrutordobean,achamadade
context.proceed()fazcomqueoobjetocujoconstrutorfoiinterrompidoseja
criado. Senãochamarmosessemétodo,oobjetonãoserácriado. Apenasapósa
chamadadométodo proceed()conseguimosrecuperaroobjetorecémcriado
atravésdométodo getTarget()do InvocationContext.Esseobjeto,porém,
nãoestácomsuasdependênciaspovoadas, entãopodemosterproblemascomo
NullPointerExceptionsetentarmosexecutaralgumdeseusmétodos.
Obviamente,senossoobjetoalvodefinirquesuasdependênciasdeverãoserto-
dassatisfeitasviaseuconstrutor,teremosoobjetorecémcriadojácomessasde-
pendências,mascomoalgunsobjetospodemreceberdependênciasdeoutraforma,
fazerusodoobjetonovoéarriscado.Atéporque,voltandoàpremissadequeointer-
ceptadornãodeveconhecerqualobjetoestásendointerceptado,éimprecisofazer
muitassuposiçõessobrecomoesteobjetorecebesuasdependências.
Sóteremoscertezaqueoobjetoestátotalmentemontadoquandoométodoano-
tadocom
@PostConstructforinvocado.Porématéagorasóutilizamosessaano-
taçãoparadefinirmétodosdentrodoprópriobeanquefoicriado.Mastemostam-
bémaop çãodeinteragircomessemomentoviainterceptadores.
122

## Página 128

CasadoCódigo Capítulo6. InterceptorseDecorators
Interceptadores@PostConstructe@PreDestroy
Desdeoiníciodosnossosexemplostemosutilizado @PostConstructpara
quenossosbeanssaibamquandoestãoprontos,comtodasasdependênciassatisfei-
tas,eassimpossamfazeralgo.Deformaparecida,podemosutilizar @PreDestroy
paraexecutaralgumaoperaç ãoantesdonossobeanserremovidodamemória.
Atéaqui,nossautilizaçãotemseparecidocomaseguinte.
@Named @RequestScoped @Auditavel
public class CalculadoraImpostosBean {
@Inject private CalculadoraDeImpostos calculadoraImpostos;
@PostConstruct
public void init(){
System.out.println("CalculadoraImpostosBean pronta.");
}
@PreDestroy
public void destroy(){
System.out.println("CalculadoraImpostosBean indo embora.");
}
}
Essaéaformadeutilizaressasanota çõesdentrodoprópriobean,maspodemos
utilizá-lastambémemuminterceptor.Comoemtodososdemaistipos,avinculaç ão
entreointerceptoreobeanéfeitavia interceptor bindings.Nonossoexemplo,esse
bindingéfeitopelaanotaç ão @Auditavel,enossointerceptadoréo Auditor.
@Interceptor @Auditavel @Priority(Interceptor.Priority.APPLICATION)
public class Auditor {
@PostConstruct
public void postConstruct(InvocationContext context)
throws Exception{
Object target = context.getTarget();
//chama método anotado com @PostConstruct, se houver
context.proceed();
}
123

## Página 129

6.3. EstendendoumbeanexistentecomDecorators CasadoCódigo
@PreDestroy
public void preDestroy(InvocationContext context ) throws Exception{
Object target = context.getTarget();
//chama método anotado com @PreDestroy, se houver
context.proceed();
}
}
Basicamente,adiferen çaéqueaoremoverosmétodosde callbackdedentro
doprópriobean,conseguimosdarumcomportamentomaisuniformedentrodo
nossosistema. Nãoprecisamosrepetirváriasvezesomesmocódigoquecriaum
logmostrandoociclodevidadecadaumdosbeansdosistema.Bastafazerissono
interceptorevinculá-loaobeanatravésdaanota çãodevinculaç ão—noexemplo,a
@Auditavel.
Notetambémqueporestarmosinterceptandoométodooriginal,sempretemos
aop çãodechamá-loounãoviamétodo proceed().Nesseexemploacima,obean
podeaténãoterummétodode callbackdentrodele,mesmoassimointerceptador
conseguecapturaromomentoapropriado. Agora,seobeantiveressesmétodos
dentrodele,osmesmosserãoexecutadosnomomentoemquechamamosométodo
proceed().
6.3 Estendendo um bean existente com Decorators
DecoratorsemCDInadamaissãodoqueumaformadeimplementarmosopadrão
deprojetodemesmonome.Logo,adefiniç ãodeumseaplicaaooutro.
Umdecorator,oudecorador,éumobjetoqueestendeasfuncionalidadesdeum
objetojáexistente,paraissoeleprecisateramesmatipagemdoobjetodecorado.A
grandesacadadessepadrãoéqueemvezdeestenderoobjetooriginalesobrescrever
osmétodosquedesejamosalteraroucriarnovosmétodos,fazemosissodeforma
dinâmica,emtempodeexecuç ão. Vamosverissodeformagráficaparafacilitaro
entendimento.
124

## Página 130

CasadoCódigo Capítulo6. InterceptorseDecorators
Figura6.3:Implementaçãosimplesdeumainterface
Iniciamosvendoumaclasseclienteutilizandoumasimplesimplementaç ãode
umainterface,quenocasofoia CalculadoraDeSalarios. Atéaquinadade
novo,masvainosajudaraperceberaevolu çãodoexemplo.Aseguirveremosuma
formadeestenderaimplementaç ãoqueacabamosdever.
Figura6.4:Estendendoaimplementaç ãooriginal
Quando estendemos uma implementaç ão existente, como no
exemplo que acabamos de ver, podemos sobrescrever os métodos
existentes e chamar a implementaç ão original através do super.
Como a classe CalculadoraDeSalariosPlano2013 estende a
CalculadoraDeSalariosPlano2005, e esta, por sua vez, implementa a
interface CalculadoraDeSalarios, logo, aimplementaçãodoplanode2013
tambémimplementaessainterface, eporissopodeserusadapelanossaclasse
cliente.
Essaéumaformalegítimadeestenderumcomportamento,tantoéqueaprópria
linguagemnosdámeiosdefazê-lo,masnovamentetemosquetomarcuidadocom
asemântica. Seráqueaimplementaç ãodoplanode2013 éaimplementaçãodo
125

## Página 131

6.4. Vinculaçãodinâmicaentreoobjetodecoradoeseudecorador CasadoCódigo
planode2005,ousimplesmenteausa? Quandousamosextensãoouimplemen-
tação, lemosqueumaclasse édotipoestendidoouimplementado. Ouseja, a
CalculadoraDeSalariosPlano2005 éuma CalculadoraDeSalarios.
Até aí tudo bem. Mas será que aCalculadoraDeSalariosPlano2013
é uma CalculadoraDeSalariosPlano2005? Ou seria apenas uma
CalculadoraDeSalarios?
Essaquestãosemânticaéumdosaspectosquepodemostratarmelhorcomum
decorador,masnãoficamoslimitadosaisso.Porém,comoveremosaindabastante
sobredecoradores,nessemomentooaspectosemânticojánosvaleaanálise. Por
isso,vamosolharcomoresolvê-lousandocomposiç ãoemvezdeheran ça.
Figura6.5:Usandocomposiç ãoemvezdeheran ça
Agora com esse arranjo, temos uma leitura correta das classes envolvidas:
a CalculadoraDeSalariosPlano2013éuma CalculadoraDeSalariose
paraexecutarasuatarefa usaa CalculadoraDeSalariosPlano2005.Ótimo,
problemasemânticoresolvido,masseráqueumdecoratorésóumnomebonitinho
paraamáxima“quandopossível,usecomposiçãoemvezdeheran ça"?Obviamente
quenão,eagoraqueentendemosaestruturadodecorador,veremosemquesitua-
çõeselenosserámuitoútil.
6.4 Vinculação dinâmica entre o objeto decorado e
seu decorador
Enquantonoexemploqueacabamosdeveraligaç ãoentreosobjetosfoidefinida
emtempodedesenvolvimento,utilizandoalinguagemdeprograma ção,afuncio-
nalidadequeveremosapartirdaCDIvinculaosobjetosemtempodeexecuç ão.
126

## Página 132

CasadoCódigo Capítulo6. InterceptorseDecorators
Naverdade,essaéumacaracterísticadoprópriopadrãodeprojeto decorator,nãoé
apenasusarcomposição,éfazerissocomaaplicaç ãorodando.
Ofuncionamentododecoradorlembramuitoodointerceptador. Adiferen ça
éque,nesteúltimo,ainterceptaç ãoéfeitadeformagenérica,paraadicionaràre-
quisiçãorequisitosnãofuncionais,comoseguran ça;jánodecoradoradicionamos
funcionalidadesdenegócio,tantoéqueodecoradorprecisateromesmotipodo
objetodecorado.
QuandoaCDIvaiinjetarumdeterminadoobjetonaclassecliente,elaverificase
nãoexisteumdecoradorcomtipocompatível,setiver,essedecoradorépassadono
lugardoobjetooriginal,eooriginaléinjetadodentrododecorador,edentrodeste
passaaserchamadode delegate.Vejamosumexemploprático.
@Inject
private CalculadoraDeSalarios calculadoraDeSalarios ;
Aquitemosumcódigojáconhecido,quenadamaisédoqueumclientedain-
terface CalculadoraDeSalariosrecebendo-adocontextoCDI.Agoravamos
analisaraimplementaç ãoda CalculadoraDeSalariosPlano2013,queéum
decorator.
@Decorator
public class CalculadoraDeSalariosPlano2013
implements CalculadoraDeSalarios {
@Inject @Delegate
private CalculadoraDeSalarios delegate ;
@Inject
private Logger logger ;
@Override
public double calculaSalario(Funcionario funcionario){
logger.info("Delegate plano 2013" );
double salario = delegate.calculaSalario(funcionario);
return salario * 1.1;
}
}
127

## Página 133

6.4. Vinculaçãodinâmicaentreoobjetodecoradoeseudecorador CasadoCódigo
Nesseexemplo,vamosconsiderarquedepoisdemuitanegociaç ãocomosfunci-
onários,aempresaondetrabalhamosdecidiuqueoplanodesaláriosde2013apenas
iráconcederumaumentode10%(dezporcento)sobreoplanoanterior.Emvezde
criarmosumanovaimplementaç ãodainterface
CalculadoraDeSalarios,uti-
lizamosaexistente,quejáestátestada,eadicionamosaoretornodoseucálculoo
percentualdeaumentoestipulado.
Ointeressantedeanalisarmosemumdecoradoréopontodeinje çãoanotado
com
@Delegate.Percebaque,foraessaanota ção,esteéumpontodeinje çãoco-
mum,ondedefinimosotipoquedesejamoseanotamoscom @Inject.Podemos
adicionaraítambémqualquerqualificadorquedesejarmos,eaofazerissoestaremos
especificandomaisemquaiscasosdesejamosqueodecoradorsejautilizado.
Ofuncionamentoésimples,odecoradorseráutilizadoparasubstituiroob-
jeto original toda vez que seudelegate combinar com o que a classe cliente
espera que seja injetado. Em outras palavras, se a classe cliente espera uma
CalculadoraDeSalarioscomqualificador @Defaultenossodecoradorsabe
decorarumobjetocomomesmotipo,entãoeleserápassadoàclassecliente,eo
objetooriginalseráseudelegate.
Se quisermos que nosso decorador atue sobre qualquer
CalculadoraDeSalarios, e não apenas o @Default, podemos fazer a
seguintealteração.
@Decorator
public class CalculadoraDeSalariosPlano2013
implements CalculadoraDeSalarios {
@Inject @Delegate @Any
private CalculadoraDeSalarios delegate;
...
}
Agora qualquer CalculadoraDeSalarios passará a ser decorada pelo
CalculadoraDeSalariosPlano2013. Comovimosnase ção 4.2,oqualifica-
dor @Anyépraticamenteumdesqualificador,fazendocomqueopontodeinje-
çãomarcadocomeleaceiteobjetoscomquaisquerqualificadores,enãosomenteo
@Default,quesempreestáimplícitoquandonãoespecificamosoutro.
Umavezqueentendemosomecanismode“interceptação”quenossodecorador
acabausandoparaentrarnolugardosobjetosoriginais,podemosvoltaraanalisaro
exemploanterior,emquetínhamosainje çãodeum Loggeralémdo delegate.Isso
128

## Página 134

CasadoCódigo Capítulo6. InterceptorseDecorators
porquenossodecoradoréumbeancomoqualqueroutro,eassimpodetertambém
suasprópriasdependências.Essasdependênciasserãoresolvidascomoqualquerou-
tra,podendoterosmesmosproblemasdeambiguidadeounãotendoquemasupra;
podemserinterceptadas,epodeminclusiveseremdecoradasporumoutrodecora-
dor.Sónãopodemosterumadependênciacíclica,naqualpedimosparainjetar,em
umapropriedadequenãoo delegate,umobjetoqueestásendodecoradopelanossa
classe.Cadadecoradorpodeterumúnicodelegate,maspodeterdiversospontosde
injeçãonormais.Tambémcomoumbeannormal,nossodecoradorpodereceberas
dependênciasviapropriedade,comonoexemplo,oucomasoutrasviaspossíveis:
construtoremétodoinicializador.
Ótimo,agoratemosumdecoradorfuncionando,masesequisermosmaisin-
formações sobre o bean que estamos decorando em tempo de execução? Por
exemplo, se quisermos saber exatamente qual o seu tipo, seus pontos de inje-
ção etc; fazemos isso via reflection em cima do delegate? Existe uma forma
maissimples,adicionadanaversão1.1daCDI,queéadicionarumainstânciade
javax.enterprise.inject.spi.Bean,representandoobeandecorado.
Ainterface Beannospermiteacessaressasmetainformaçõesquequeremossa-
ber,eparatermosacessoaelabastaadicioná-lacomodependênciaanotando-acom
@Decorated.
@Decorator
public class CalculadoraDeSalariosPlano2013
implements CalculadoraDeSalarios {
@Inject @Delegate @Any
private CalculadoraDeSalarios delegate ;
@Inject @Decorated
private Bean<CalculadoraDeSalarios> bean;
...
}
Comoaprópriaanota çãosugere,esseéo Beanqueestásendodecorado,e
atravésdessainterfacerespondemosasperguntasanteriores,epodemosinclusive
utilizá-lasparaadicionarmaisinformaçõesaonossolog.
...
@Inject @Decorated
private Bean<CalculadoraDeSalarios> bean;
129

## Página 135

6.4. Vinculaçãodinâmicaentreoobjetodecoradoeseudecorador CasadoCódigo
@Override
public double calculaSalario(Funcionario funcionario){
logger.info("Delegate plano 2013" );
Class beanClass = bean.getBeanClass();
Set<InjectionPoint> injectionPoints = bean.getInjectionPoints();
logger.info(String.format("Bean original: '%s' "
+ "com injection points: '%s'", beanClass,
injectionPoints));
double salario = delegate.calculaSalario(funcionario);
return salario * 1.1;
}
...
Comonossodecoradorcompleto,faltaapenashabilitá-lo,poisassimcomoos
interceptadoreseosbeansalternativos,umdecoradorprecisaserativado,sejavia
beans.xmlouviaanota ção.
Oarquivo beans.xmlquehabilitanossodecoradorficadaseguintemaneira.
<beans xmlns="http://xmlns.jcp.org/xml/ns/javaee"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
http://xmlns.jcp.org/xml/ns/javaee/beans_1_1.xsd">
<interceptors>
<class>
br.com.casadocodigo...CalculadoraDeSalariosPlano2013
</class>
<class>...</class> <!-- um interceptador em cada tag class -->
</interceptors>
</beans>
Encurteionomedaclasseapenasparafacilitaraleitura,massetratadonome
completodaclasse,assimcomoemtodososoutrosexemplosapresentados.Também
comonosoutrosexemplosondeusamosoarquivoXML,apartirdaversão1.1daCDI
podemosutilizaraanotaç ão
@Priorityparaativaresserecurso.Comaalteraç ão
aseguirnãoprecisamosalteraro beans.xml.
@Decorator @Priority(Interceptor.Priority.APPLICATION)
public class CalculadoraDeSalariosPlano2013
130

## Página 136

CasadoCódigo Capítulo6. InterceptorseDecorators
implements CalculadoraDeSalarios {
...
}
Assimcomoosinterceptors, podemostambémordenarnossosdecoradores.
Damesmaformaquepodemostermaisdeuminterceptadorexecutandoemuma
mesmarequisição,podemostermaisdeumdecorador.Comdecoradoresnãopa-
recetãoóbvio,massetivermosumahierarquiadebeansumpoucomaiscomplexa,
podemosterumdecoradoremumnívelmaisabstratoeoutroemumnívelmais
específicodessahierarquia.Prioridadesmenoresexecutamprimeiro,ebeansativa-
doscom
@PriorityexecutamantesdosativadosviaarquivoXML.Alémdisso,os
decoradoressãochamadossempredepoisdosinterceptadores.
131

## Página 138

Capítulo7
DefinindoEstereótipose
diminuindooacoplamento
utilizandoEventos
Agoraquejásabemossobrequalificadores,maisespecificamentebeansnomeados,
escoposeinterceptadores,podemosverumaferramentamuitoútildaCDIqueéa
criaçãodeestereótipos.
Alémdisso,veremostambémnestecapítulocomoutilizarEventos,umafunci-
onalidadequenosdaráapossibilidadedeestendernossaaplicaç ãocombaixíssimo
acoplamento.Provavelmentedurantealeituravocêlembrarádesitua çõesnossiste-
masemquetrabalhaemqueautilizaç ãodeeventosdiminuiriaoacoplamentona
comunicaçãoentreclasses,módulos,eatémesmosistemasdiferentes.

## Página 139

7.1. Definindoestereótipos CasadoCódigo
7 . 1 Definindo estereótipos
Quandoalguémfalaqueumadeterminadapessoaéumnerd,queimagemvemà
suacabe ça?Talvezumapessoapequena,deóculos,quieta,inteligente,eprovavel-
mentecomumnotebookporperto. Sevocêpensouemalgoparecido,sabeoque
éumestereótipo.Podemospensaremdiversosexemplosdiferentes,masosignifi-
cadoésempreomesmo:umageneralizaç ãodecaracterísticascomuns,umaimagem
preconcebidadealgo.
Atéaquivimosdiversasconfigura çõesquepodemosfazeremnossosbeans,tais
comodefinirumnome,umescopo,qualificadoreseinterceptadores. Àprimeira
vistanãopareceumtrabalhomuitocomplicado,edefatonãoé,maspodemossim-
plificaressasconfiguraçõescriandoumestereótipoparaosbeans. Paraservirde
base,vamosrelembraroexemplodaclasse
CalculadoraImpostosBeanquevi-
mosnase ção5.2.
@Named @RequestScoped
public class CalculadoraImpostosBean { ... }
Agoravamospensarnonossosistemadeumaformamaisabstrata.Temosum
sistemaquetrataoRHefolhadepagamentosdanossaempresa,ecomojávimos
pelosdiversosexemplosneleexistemdiversascalculadorasdiferentes,umadeim-
postos,outradesalárioeumaoutradefolhadepagamento.Alémdisso,podemos
teraindacalculadorassimuladaspara,porexemplo,seremutilizadasemumestudos
deimpactofinanceiroquandoumnovoplanodecargosesaláriosforproposto.
Podemosperceberqueotermo“calculadora”érecorrentenonossosistema,as-
simcomoCRUDs,oucadastrosdetabelasbásicaspodesercomumnoprojetoque
vocêtrabalhahoje. Quandopensamosemumtermosignificativo,umaespéciede
abstraçãocomumavárioslocaisdosistema,geralmentepensamoseminterfaces.É
possívelatédefinirmosumainterfaceparaascalculadorastambém,masessenão
seráofocoaqui.Nossoobjetivoéverdeformaparecidaosbeansquemanipulamas
calculadoras,oscontroladoresqueinjetamascalculadoraspropriamenteditas.Isso,
noentanto,nãosignificaquenãopossamosaplicaromesmoraciocínioàsimple-
mentaçõesdascalculadoras,mastrabalhandocomoscontroladoresteremosmais
mecanismosaanalisar.
Olhandoespecificamenteparanosso
CalculadoraImpostosBean,masen-
xergandoaabstraç ãodetodosos CalculadoraXYZBean,percebemosqueto-
doselespossuemnomeeescopo. Éumcome ço,maspodemosiralém. Podería-
mos,porexemplo,definirqueessesbeansdevemserauditados,usandoaanota ção
134

## Página 140

CasadoCódigo Capítulo7. DefinindoEstereótiposediminuindooacoplamentoutilizando...
@Auditavelquevimosnase ção6.1,eassimficariaregistradonologdaaplicaç ão
quemandaexecutandooquê.Oresultadoseriaalgocomoocódigoaseguir.
@Named @RequestScoped @Auditavel
public class CalculadoraImpostosBean { ... }
Agorapensandoumpoucomaisemquestõesdeinfraestrutura,poderíamoster
uminterceptadorgeralque,diferentedoligadoàanotaç ão @Auditavel,quetrata
maisdeauditoriadequecoisasmaisrestritas,lidassecomquestõesgeraisgenéricas
daaplicação,comoqualmétodoestásendochamado,qualaURLatual,eoutras
informaçõesnãorelacionadasaonegócio. Esseinterceptadorestariavinculadoa
umaanotaçãoquedefinimosagora:
@Rastreavel.Tantoseucódigoquantoodo
interceptadornãoimportam,poisestamosinteressadosnasemânticaapenas.Feito
isso,seolharmosnossobeannovamente,veremosqueaquantidadedeanota çõesjá
incomoda.
@Named @RequestScoped
@Auditavel @Rastreavel
public class CalculadoraImpostosBean { ... }
Opiordessecenárionãoénemotantodeanota çõesemcimadaclasse,esim
apossibilidadedeesquecermosdedefiniromesmolequedeanotaç õesquandoes-
tivermosdefinindoo CalculadoraXYZBean.Aindamaisagoraqueestamosde-
finindointerceptadoresgenéricosqueservemaquestõesdeinfraestrutura,comoo
@Rastreavel. Essasgeralmentesãoasprimeirascoisasquesãoesquecidascon-
formeosistemacresce. Umdesenvolvedorlembradecolocaressasanota ções,o
outronão,eoquandotemosumproblemaparaanalisarologestáinconsistente.
Paraevitaressesproblemas,podemosdefinirumaanota çãoqueresumetudo
isso.Podemos,porexemplo,chamá-lade @CalculadoraBean,eelateráoseguinte
código.
import javax.enterprise.inject.Stereotype;
@Stereotype
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
public @interface CalculadoraBean {
}
Aqui,ainda,temosadefiniç ãomínimadonossoestereótipo. Estamosusando
@Target(TYPE), mas também podemos combinar com ostargets METHOD e
135

## Página 141

7.1. Definindoestereótipos CasadoCódigo
FIELD.Paraqueoestereótipo CalculadoraBeansejaumresumodetodasaquelas
anotações,temosquecolocá-lasnele.
import javax.enterprise.inject.Stereotype;
@Stereotype
@Named @RequestScoped
@Auditavel @Rastreavel
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
public @interface CalculadoraBean {
}
Émuitacoisajunta,masagoratemosumcondensadodetodasasconfigurações
quedesejamoscolocarnosbeansdessetipo.Agoraésóanotarnossoalvocomesse
estereótipo.
@CalculadoraBean
public class CalculadoraImpostosBean { ... }
Deagoraemdiante,sequisermosadicionarumnovointerceptadoremtodosos
beansdessa“família”,bastaadicionarnoestereótipo.Ok,muitointeressante,mase
seobean CalculadoraFolhaDePagamentoBeanestiveremumatelamaiscom-
plexaquearesponsávelporcalcularimpostos,eporissoprecisarmosdeumescopo
maisapropriadocomo
@ConversationScoped?Nãotemproblema,poisoeste-
reótipodefineoescopopadrão,podendosersobrescritopelobeanqueoutilizar.
@CalculadoraBean
@ConversationScoped
@Named("calculadoraFolhaBean")
@UmNovoQualificadorQualquer
@MaisUmInterceptorBinding
public class CalculadoraFolhaDePagamentoBean { ... }
Comopodemosver,asconfiguraç õesdoestereótiponãosãolimitadoras,sãopa-
dronizadoras,podendoserestendidaspelobeancliente.Semprequepossível,tente
padronizarsuasconfiguraç õesparaevitarinconsistências.Apesardetermosanali-
sadoumestereótipoparaacamada“controladora”doMVC,comoestamosfalando
deCDI,podemosdefinirumestereótipoparaqualquerlugardanossaaplicaç ão,
comonaimplementaçãodascalculadoras.
136

## Página 142

CasadoCódigo Capítulo7. DefinindoEstereótiposediminuindooacoplamentoutilizando...
Podemos,porexemplo,definirumestereótipocomo @Alternativeparaque
sejausadonassimuladorasdecálculo.
@Stereotype
@Alternative
@Rastreavel
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
public @interface Mock {
}
Epodemosaindacombinarestereótipossimplesmenteanotandoumestereótipo
comoutro.
@Stereotype
@CalculadoraBean @Mock
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
public @interface CalculadoraMockBean {
}
Assimqualquerbeananotadocom @CalculadoraMockBeanteráumnome
padrão, será @RequestScoped, @Auditavel e @Rastreavel, e também
@Alternative.Certamenteéumaformamuitoflexíveldeorganizarosbeanscom
característicassemelhantes.
@Model:estereótipodesérie
Aprendemosacriarnossosprópriosestereótipos,mascasoqueiramosapenas
umquedefinaoescoporequestcomopadrãoequeobeanqueoutilizarseránome-
ado,podemosutilizaroestereótipo @javax.enterprise.inject.Model.Seu
objetivoédisponibilizar,semanecessidadedecodificaç ãoalguma,umestereótipo
quesirvaparaosbeansdacamada“model”doMVC.
7 . 2 UtilizandoEventos para obter um baixíssimo
acoplamento
QuandopensamosemCDI,aprimeirafuncionalidadequenosvemàcabe çaéa
resoluçãodedependências. Esteéoassuntomaisbuscadosobreaespecificaç ão,
137

## Página 143

7.2. UtilizandoEventosparaobterumbaixíssimoacoplamento CasadoCódigo
masnestase çãoveremoscomoomecanismodeeventospodeserdegrandevalia
paranossasaplicações.
Autilizaçãoéextremamentesimples,masprecisamospensarnasfuncionalida-
desdosnossossistemasdeumaformadiferente.Paranossoestudo,vamosconside-
raragestãodefuncionáriosdanossaempresa.Imaginequenaempresatemosdi-
versossistemas,equeparaacessaressessistemasosfuncionáriosprecisam,alémde
seuloginesenha,estaremcomsuasituaç ãofuncionalativadentrodaempresa.Ou
seja,quandoofuncionáriofordesligado,seuacessodevesercortadonossistemas.
Semelhantemente,podemoscriaroacessoaossistemasquandoumnovofuncioná-
rioforcontratado,entãologoqueelesairdoRHdaempresa,jápoderácome çara
trabalhar.
Quaisserãoossistemasqueosfuncionáriosdaempresautilizamvaidepender
decadaramodeatuaç ão. Porexemplo,emumaempresadedesenvolvimentode
software,osfuncionáriosterãoacessoaorepositóriodecódigoeàferramentade
controledeissues.EmoutrasempresastalveztenhamosquedaracessoaoERP,ou
qualquersistemaquevocêpossaimaginar. Agorapensecomocriaressesacessos
logodepoisdocadastrodofuncionário,ecomoremovê-losnodesligamento.Será
quealgoparecidocomopseudocódigoabaixoéumaboaalternativa?
public void cadastrarFuncionario(Funcionario funcionario){
//lógica de ativação do funcionário
funcionario.setStatus(ATIVO);
entityManager.persist(funcionario);
criaUsuarioGit(funcionario);
criaUsuarioIssueTracker(funcionario);
criaUsuarioERP(funcionario);
}
Comopodemosperceber,acabamoscriandoumacoplamentoentreagestãode
funcionáriososdiversossistemasqueelesutilizarãonoseudiaadia.Podenãopa-
receralgotãoabsurdo,masnãoéodesejado,vistoqueessessistemaspodemmudar.
Podemostrocaro issue trackerutilizado,podemospassarausaralgumnovosistema
oudeixardecriarusuáriosnoERPparatodososfuncionário,deixandoapenaspara
aquelesquedefatoprecisarãooperaressesistema.Acadamudan çadessetipo,tere-
mosquealterarométododecadastrodofuncionário,mesmosemqualqueralteraç ão
nalógicadeativaç ãodefuncionáriodopontodevistadoRH.Issonosdáumforte
indíciodequedevemosmudaralgo.
138

## Página 144

CasadoCódigo Capítulo7. DefinindoEstereótiposediminuindooacoplamentoutilizando...
U m a e v o l uçãonessecenárioseriadefinirmosalgumtipodeinterfacequeabs-
traiaessacriaç ãodeusuários.
public interface GerenciadorDeAcesso {
void criaUsuario(Funcionario funcionario)
}
public class GerenciadorDeAcessoGit implements GerenciadorDeAcesso {...}
public class GerenciadorDeAcessoERP implements GerenciadorDeAcesso {...}
//outras implementações
Eagorapodemosalterarnossagerenciadoradefuncionáriosparautilizaressa
abstração
public class GerenciadorFuncionarioBean {
private List<GerenciadorDeAcesso> gerenciadoresAcesso =
Arrays.asList(
new GerenciadorDeAcessoGit(),
new GerenciadorDeAcessoERP(),
new GerenciadorDeAcessoIssueTracker());
public void cadastrarFuncionario(Funcionario funcionario){
//lógica de ativação do funcionário
funcionario.setStatus(ATIVO);
entityManager.persist(funcionario);
for(GerenciadorDeAcesso gerenciador : gerenciadoresAcesso){
gerenciador.criaUsuario(funcionario);
}
}
}
Dessamaneiraépossívelalterarmuitacoisaapenascriandonovasimplementa-
çõesde GerenciadorDeAcessoeadicionandoouremovendoinstânciasdalista
gerenciadoresAcesso.Aindapodíamosevoluirnossasolu çãocriandoumaes-
péciedefederaçãodegestoresdeusuários,tratandoessacole çãocomosefosseum
únicoobjeto,edeixandoqueesseobjetodelegassecadachamadaaoselementosda
lista.Issocomcertezamelhorariaaindamaisasolu ção,masaindapodemosterno-
vassituaçõesfugindodonossocontrole.
Vamossuporque,porquestõeslegais,nossaempresatenhaqueinformarao
INSSquandorealizarumanovacontrataç ão.Seriaumasituaç ãomuitoparecidacom
139

## Página 145

7.2. UtilizandoEventosparaobterumbaixíssimoacoplamento CasadoCódigo
acriaçãodeusuáriosfeitaatravésdasimplementaçõesde GerenciadorDeAcesso,
mascriarumanovaimplementaç ãodessainterfaceparainformaraoINSSseriauma
quebranasemânticadainterface.Atéporqueteremosoutrosmétodosdeconcessão
depermissõesqueaimplementaç ãodoINSSnãonecessitaria.Eagora?Comore-
solveresseproblema?
Poderíamoscriarumainterfaceancestralda GerenciadorDeAcesso,com
apenasmétodoscomo criarUsuarioe removerUsuarioeentãocriaraimple-
mentaçãodoINSSbaseadonela.Masseráqueprecisamosmesmofazeressascoisas
dentrodométododenegócio?Arespostaénão,eusaremoseventospararesolver
essesproblemas. Avantageméqueprovavelmentetambémestaremospreparados
paraqualqueroutranovaoperaç ãoquetenhamosdefazeraocontratarumfuncio-
nário,semcorreroriscodequebrarasemânticadasinterfacesquetemos,esemter
quealterá-lasparaisso.
import javax.enterprise.event.Event;
public class GerenciadorFuncionarioBean {
@Inject
private Event<Funcionario> eventoFuncionarioCadastrado;
public void cadastrarFuncionario(Funcionario funcionario){
//lógica de ativação do funcionário
funcionario.setStatus(ATIVO);
entityManager.persist(funcionario);
eventoFuncionarioCadastrado.fire(funcionario);
}
}
Criamosumobjetoquelan çaeventosrelacionadosaotipo Funcionario,
e o chamamos de eventoFuncionarioCadastrado, que é do tipo
javax.enterprise.event.Event. Com isso, agora nosso método de ne-
gócionãodependedequalquer GerenciadorXYZ,elesimplesmentelan çaum
eventoescutávelporqualquerobjetodocontextoCDI.Assim, sealgumobjeto
quiser fizer alguma operação no cadastramento de um novo funcionário, basta
escutaresseevento. Oacoplamentoentrequemlan çaoeventoequemoescutaé
praticamentezero.
140

## Página 146

CasadoCódigo Capítulo7. DefinindoEstereótiposediminuindooacoplamentoutilizando...
7 . 3 Observ adores síncronos de eventos
Paraumobjetoreceberanotificaç ãodequeumnovo Funcionariofoiadmitido,
bastaescutaroeventolan çadopelo GerenciadorFuncionarioBean.
import javax.enterprise.event.Observes;
public class GerenciadorDeAcessoGit {
public void criaUsuarioGit(@Observes Funcionario funcionario){
...
}
}
Aimplementação,comoacabamosdever,ébemsimples.Omelhoréquenem
precisamosdefinirqualquerinterface,umavezquenãoexistequalquervínculoen-
tre GerenciadorFuncionarioBeane GerenciadorDeAcessoGit.Seexiste
algumvínculo,étotalmenteindireto,poisporpadrãoosobservadoressãosíncro-
nos.Assim,casoumobservadordemoredemaisparaprocessaralgo,oulanceuma
exceção,quemlan çouoeventoseráimpactado,eoacoplamentoentreosdoisse
restringeaisso.
Nãopodemosnoentantodiminuirdemaisessacaracterística,vistoqueemum
cenárioJavaEE,ondeatransa çãoégerenciadapelocontainer,ométodoquelan ça
oeventoeoqueoobservaexecutamnamesmatransa ção.Assim,aexce çãolan çada
porumobservadorpodecausar r o l l b a c kemtodaatransa ção,queenvolveomé-
tododenegócioetodososobservadores.Essapodeserumacaracterísticadesejável,
nospermitindovalidaralgoviaobservador,maspodenãoser.Nessecasoamelhor
opçãoseriautilizarumeventoassíncrono.
7 . 4 Eventos e qualificadores
Oexemplodenotificadoreobservadorquevimosfoiextramentesimples:envolve
apenasumeventodotipo
Funcionario.Masparaqueessemecanismosejaefi-
caz,precisamosconseguirdiferenciar,porexemplo,umeventodecontrataç ãode
funcionáriodeumeventodedesligamento,eparafazerisso,utilizamosqualificado-
res,damesmaformaquefazíamosparaacabarcomaambiguidadenaresolu çãode
dependências.
Parademonstrar,vamosalterarnossoexemploparadistinguirmoseventosde
contrataçãoeeventosdedemissãodefuncionários.Osqualificadoresutilizadossão
141

## Página 147

7.4. Eventosequalificadores CasadoCódigo
criadosexatamentedamesmaformaqueosqualificadoresvistosnase ção4.2,usados
naresolu çãodedependências,poressemotivonãoénecessáriovermosocódigo
aqui.
public class GerenciadorFuncionarioBean {
@Inject @Contratacao
private Event<Funcionario> eventoContratacao;
@Inject @Demissao
private Event<Funcionario> eventoDemissao;
public void cadastrarFuncionario(Funcionario funcionario){
...
eventoContratacao.fire(funcionario);
}
public void demitirFuncionario(Funcionario funcionario){
...
eventoDemissao.fire(funcionario);
}
}
Váriasclassespodemobservaromesmoevento,masparafacilitarvamoscolocar
algunsobservadores,umabaixodooutro.
public void escutaContratacao(@Observes @Contratacao Funcionario f){
...
}
public void escutaDemissao(@Observes @Demissao Funcionario f){
...
}
public void escutaQualquerEventoDeFuncionario(@Observes Funcionario f){
...
}
Enquanto os dois primeiros observadores são específicos para cada tipo
de evento de Funcionario, o terceiro observará qualquer evento do tipo
Funcionario,seja @Contratacao, @Demissaoououtraqualidadedeeventode
funcionárioquevenhaasercriado.Masnossoexemploaindapodeserincremen-
tado.Iremosadicionarumoutrotipodedesligamentodefuncionário,aaposentado-
ria.Agoraaodesligarumfuncionárioprecisaremosdefinirotipodedesligamento.
142

## Página 148

CasadoCódigo Capítulo7 .DefinindoEstereótiposediminuindooacoplamentoutilizando...
public class GerenciadorFuncionarioBean {
private TipoDesligamento tipoDesligamento;
@Inject @Aposentadoria
private Event<Funcionario> eventoAposentadoria;
@Inject @Demissao
private Event<Funcionario> eventoDemissao;
...
public void desligarFuncionario(Funcionario funcionario){
...
if(tipoDesligamento == TipoDesligamento.APOSENTADORIA){
eventoAposentadoria.fire(funcionario);
}
else if(tipoDesligamento == TipoDesligamento.DEMISSAO){
eventoDemissao.fire(funcionario);
}
}
}
Esseexemplofunciona, maspoderíamostrocarosdois pontosdeinje çãode
eventosporapenasum,equalificá-lodinamicamente,parecidocomo quefizemos
naseção4.8quandovimosolookupprogramático.Podeparecerqueficamaisdifícil,
masissonosdámuitapossibilidadede tomaradedecisãoem tempodeexecução.
public class GerenciadorFuncionarioBean {
private TipoDesligamento tipoDesligamento;
@Inject
private Event<Funcionario> eventoDesligamento;
...
public void desligarFuncionario(Funcionario funcionario){
...
Annotation qualificador = null;
143

## Página 149

7.4. Eventosequalificadores CasadoCódigo
if(tipoDesligamento == TipoDesligamento.APOSENTADORIA){
qualificador = new AnnotationLiteral<Aposentadoria>(){};
}
else if(tipoDesligamento == TipoDesligamento.DEMISSAO){
qualificador = new AnnotationLiteral<Demissao>(){};
}
Event<Funcionario> eventoQualificado = eventoDesligamento
.select(qualificador);
eventoQualificado.fire(funcionario);
}
}
Fizemosusodaclasseutilitáriajavax.enterprise.util.AnnotationLiteral,
que deve ser tipada com a anotação que desejamos represen-
tar. Logo depois, de posse do objeto qualificador, que é do
tipo java.lang.annotation.Annotation, usamos o método
select(Annotation) do objeto Event. É como se estivéssemos saindo
deum selectsem whereparaumcom where qualificador = q. Obviamentenesse
exemplo q representaoqualificadordefinidodinamicamente, dentrodo nosso
método.Feitaessaalteração,osobservadores nãomudamabsolutamentenada,pois
oseventoscontinuarãosendoqualificados.
Qualificadoresdeeventoscomatributos
Novamenteigualvimos naseção 4.2,podemosdefinir atributosnosqualifica-
doresutilizados. Essesatributostambémservempararelacionaronotificadoreo
observadordo evento,amenosqueapropriedadedoqualificadoresteja anotada
com @Nonbinding;exatamentecomoacontece quandousamosumqualificador
parainjetardependências.Porexemplo,apartirdeagorapassaremosa usaroqua-
lificador @Desligamento.
@Target({TYPE, FIELD, METHOD, PARAMETER})
@Retention(RetentionPolicy.RUNTIME)
@Qualifier
public @interface Desligamento {
TipoDesligamento value() default TipoDesligamento.APOSENTADORIA;
}
V a m o salterarmaisumaveznossoexemploparausarmosapenasumqualifica-
dor,efazeradistin çãoviaatributo.Utilizaremosamesmaenum queusamosnos
144

## Página 150

CasadoCódigo Capítulo7 .DefinindoEstereótiposediminuindooacoplamentoutilizando...
ifsanteriores. Paranãotermoscódigos muitoextensosvamos olharapenascomo
injetaros produtoresdeeventos nanossaclasse.
@Inject @Desligamento(TipoDesligamento.APOSENTADORIA)
private Event<Funcionario> eventoAposentadoria;
@Inject @Desligamento(TipoDesligamento.DEMISSAO)
private Event<Funcionario> eventoDemissao;
//e os observadores ficam como abaixo
public void observaAposentadoriaFuncionario(@Observes
@Desligamento(APOSENTADORIA) Funcionario funcionario){
...
}
public void observaDemissaoFuncionario(@Observes
@Desligamento(DEMISSAO) Funcionario funcionario){
...
}
Feitoisso,poderíamosusarcadainstânciadessacomo jávimosnosexemplos
anteriores.Porémomaisinteressanteseriavermoscomoqualificardinamicamente
nossoprodutordeeventos,assimcomoacabamosdefazer quandotínhamosdois
qualificadores.Oproblemaé quenãoconseguimosfazer issodeumamaneirasim-
ples,poisagoratemosquedevolveraanotaçãonométodovalue()donossoobjeto
qualificador.Partedissopodeserfeitacomclassesaninhadas,masusaremosuma
classeserviráparasubstituira AnnotationLiteralpoisdessamaneiraocódigo
ficamaisorganizado.
public abstract class DesligamentoQualifier
extends AnnotationLiteral<Desligamento>
implements Desligamento {
private TipoDesligamento tipoDesligamento;
public DesligamentoQualifier(TipoDesligamento tipoDesligamento ){
this.tipoDesligamento = tipoDesligamento;
}
public TipoDesligamento value() {
return tipoDesligamento;
145

## Página 151

7.5. Observadoresassíncronosdeeventos CasadoCódigo
}
}
Eagoravoltamosmaisumavezàversãoem quetemosapenasumainstânciade
Event,equalificaremos issodeformadinâmica,masagorausandoqualificadores
compropriedades.
public class GerenciadorFuncionarioBean {
private TipoDesligamento tipoDesligamento;
@Inject
private Event<Funcionario> eventoDesligamento;
...
public void desligarFuncionario(Funcionario funcionario){
...
Annotation qualificador = null;
if(tipoDesligamento == TipoDesligamento.APOSENTADORIA){
qualificador = new DesligamentoQualifier(APOSENTADORIA){};
}
else if(tipoDesligamento == TipoDesligamento.DEMISSAO){
qualificador = new DesligamentoQualifier(DEMISSAO){};
}
Event<Funcionario> eventoQualificado = eventoDesligamento
.select(qualificador);
eventoQualificado.fire(funcionario);
}
}
7 . 5Observ adores assíncronos de eventos
Jávimoscomofuncionao mecanismodeeventos,evimos tambémque,porpadrão,
osobservadores são síncronos. Porém,comofoidito,aexecuç ãolentadeum ob-
servadorpodeimpactarnaexecuçãodométododenegócio,eemalguns casosnão
háoqueserfeito,precisamosrealizarumatarefa queélenta,mascertamentenão
queremosdegradarofuncionamentodométodonotificador. A saídaparaissoéa
utilizaçãodeobservadoresassíncronos.
146

## Página 152

CasadoCódigo Capítulo7 .DefinindoEstereótiposediminuindooacoplamentoutilizando...
Comoaindavamosanalisarnocapítulo8,aCDI nãosobrepõe funcionalidades
deoutrasespecificações doJavaEE.Eo suporteamétodosassíncronosjáétratado
pelaespecificaçãodeEJBs,assimsendo,utilizaremosesse suporteparacriarmosob-
servadoresassíncronos.
Logo,somentecomCDI, nãoconseguimosexecutarobservadoresassíncronos
emum servlet containercomoT o m c a touJetty.Isso,éclaro,semalgumaextensão
queadicioneessafuncionalidade foradeumservidordeaplicaç ãocomoJBossAS
(Wildfly)ouGlassfish. Sobreextensões, nosaprofundaremosnocapítulo9. Por
enquantoapenasutilizaremosafuncionalidadedisponível noJavaEE.
Agoraquesabemosqueessafuncionalidadeé naverdadeumempréstimo da
especificaçãodeEJBs,vamos vercomoimplementamosumobservadorassíncrono.
@Stateless
public class ObservadorDeFuncionarios {
@Asynchronous
public void observaDemissaoFuncionario(@Observes
@Desligamento(DEMISSAO) Funcionario funcionario){
...
}
}
Basta que nosso beans seja um EJB eanotar nosso observador com
@javax.ejb.Asynchronouseométodo passaaexecutaremumcontextodi-
ferentedométodonotificador. Considerandoocontextotransacionaldométodo
de negócio, o observador assíncrono funciona comose estivesse anotado com
@javax.ejb.TransactionAttribute(REQUIRES_NEW).Em outraspalavras,
oobservador nãoprovoca r o l l b a c knométodonotificador.
Sabendo dessa funcionalidade,pode parecerqueencontramos umabala de
prata,umavezqueoobservador podedemorarsemimpactaronotificador. Jásabe-
mostambémqueumaexce çãonoobservadortambémnãovaiatrapalharométodo
denegócio ouosdemaisobservadores. Mastemosquenoslembrarqueemalguns
casos,oobservadorestar namesmatransaçãoqueonotificadoréodesejável.
V a m o simaginarocenáriodeumsistemadevendas, ondeaovenderum item
élançadoum evento,queécapturadopelomódulodeestoque paraqueestedecre-
menteaquantidadedo produto.Agora,imaginemos queocorraumproblema no
módulodeestoque. Podeserinteressantequeaexce çãochegueàoperaç ãode venda
147

## Página 153

7.6. Injetandodependênciasnosobservadores CasadoCódigo
paraqueoestoque nãofiqueinconsistente.Entãoaoperaç ãodavendapodeserre-
petida,e senãohouverumanovaexceção,a transaçãoocorredeformaconsistente.
Emumcenáriocomoodescrito, casoestejamosusandoumobservadorassín-
crono,ocorrendoumaexce çãonomódulo deestoque,teríamos quevoltaraomó-
dulodecompraparadesfazeravenda. Nessecaso,seoclientejáfoiembora,nãoserá
possívelrefazeraoperação.Teríamosquenotificaroproblemadealguma formapara
podertratá-lodeformamanual.Emresumo,emalgumassituações desejamosqueo
observadorsejasíncronoeem outrasassíncrono,nãoexisteumúnicoremédiopara
todososmales.
7 . 6Injetando dependências nos observ adores
U mobservadordeeventoéumbeancomum,dessamaneira,épossívelinjetar qual-
querdependêncianele.Porém,temosaopçãodefazer algobemparecidocomo que
vimosnosmétodosprodutores,queéreceberumadependênciacomoparâmetrodo
método.
Podemos criar obean ObservadorDeFuncionarios e injetarnele um
Loggercomopoderíamosfazeremqualquer outrapartedosistema.
public class ObservadorDeFuncionarios {
@Inject
private Logger logger;
public void observaFuncionario(@Observes Funcionario funcionario){
logger.info("Recebendo evento do funcionario {}", funcionario);
}
}
Maspodemostambémrecebero Loggercomodependêncianoprópriomé-
todoobservador.Asvantagensde sefazerissosãoasmesmascomentadas naseção
5.1quandovimososmétodos produtores. Basicamentequandocolocamosasde-
pendênciasnométodo,ficaclarooqueénecessárioparaoobservadorfuncionar.É
comoumadocumentaç ãoaníveldeassinaturademétodo.
public class ObservadorDeFuncionarios {
public void observaFuncionario(@Observes Funcionario funcionario,
Logger logger){
logger.info("Recebendo evento do funcionario {}", funcionario);
148

## Página 154

CasadoCódigo Capítulo7 .DefinindoEstereótiposediminuindooacoplamentoutilizando...
}
}
Cadamétodoobservadorsópodeterumparâmetroanotadocom @Observes,
osdemaisparâmetrosserão pontosdeinje ção.
U s a n d oainterfaceEventMetadata
Utilizandoainje çãodedependências nosparâmetrosdosmétodosobserva-
dores, podemosutilizarmaisumafuncionalidade daCDI1.1, queéainterface
javax.enterprise.inject.spi.EventMetadata.Essainterfacepossui ape-
nastrêsmétodos,comopodemosveraseguir.
public interface EventMetadata {
javax.enterprise.inject.spi.InjectionPoint getInjectionPoint();
java.util.Set<Annotation> getQualifiers();
java.lang.reflect.Type getType();
}
O primeiro métododevolve o InjectionPoint referente ao objeto
Event<T>quelançouoevento,oupoderetornar nullseoeventofoidispa-
radodiretamente via BeanManager.fireEvent(Object objetoDoEvento,
Annotation... qualificadores).
Osoutrosdoismétodosretornamrespectivamenteosqualificadoreseo tipodo
eventodisparado.Issoporquenãonecessariamenteessesvaloresserãoexatamente
iguaisaosqueestãoconfigurados nométodoobservador.Comojávimos,nossoob-
servadorpodetermenosqualificadoresqueoeventooriginal;assim tambémcomo
otipopodesercompatível,semser omesmo.
Diferentede quandoinjetamoso Loggertantonobeanquantonométodo,o
EventMetadatasópodeserinjetadonométodoobservador.
public void observaFuncionario(@Observes Funcionario funcionario,
Logger logger, EventMetadata eventMetadata){
logger.info("Recebendo evento do funcionario {}", funcionario);
InjectionPoint injectionPoint = eventMetadata.getInjectionPoint();
if(injectionPoint != null){
logger.info("Evento disparado por {}",
injectionPoint.getMember());
}
149

## Página 155

7.6. Injetandodependênciasnosobservadores CasadoCódigo
}
A p e s a rdeestarmosfinalizandoo capítulo,aindaveremosumpouco maissobre
eventos,eumexemplo realdousode BeanManager.fireEventnaseção 8.2,
ondeaprenderemossobreCDIeJSF.
150

## Página 156

Capítulo8
ArelaçãodaCDIcom asdemais
especificações J a v aEE
OJavaEEéumacole çãodediversasespecificações,comoEJB,JPA,JSF, BeansV a l i-
dation,JMS,JTA,e maisumadúziadesiglas queàsvezesassustaquemestácome-
çandoatrabalharcomJavaEE.Masaboanotíciaéquesãoespecificações simplesde
usar,ea cadaversãodo JavaEEelasficammaissimplesainda. Nomeiode todases-
sasespecificações,temosaCDI, queacabafuncionandocomoumsistemanervoso,
oumaisprecisamenteocérebrodoJavaEE,poisestápresenteempraticamentequal-
queroutraespecificaçãomoderna.
Algumasespecificações sãopraticamentepartedaCDI,sendodifícilutilizaresta
semusarosrecursos dasdemais.U mexemploéaJSR318, Interceptors1.2,doqual
atéjávimospartedeseusfuncionamentonaseção6.1.
Existetambémaespecificação“DependencyInjectionforJava”(JSR330),que
temonomebemparecidocoma própriaCDI(“ContextsandDependencyInjection
fortheJavaEEplatform”).Masessa,porém,não passadeumespecificaç ão-anã,

## Página 157

8.1.RelaçãoentreCDIeEJB/JPA CasadoCódigo
queapenaspadronizaasanotações dopacote javax.injectcomo @Injecte
@Qualifier. Elaserveparaoutrosprovedoresdeinje çãodedependência,como
Spring,utilizemasmesmasanotações queasutilizadaspelasimplementações de
CDI,comoo W e l d ,mesmonãoimplementandoamesmaespecificaç ão.
ACDI foiintroduzidanoJavaEE6,ecomoestavasendodesenvolvidaem pa-
ralelocomdiversas outrasespecificações,algumasdelas,comooJSF2.0, nãoeram
totalmentecompatívelcomanovaespecificação.Porém,agoranoJavaEE7 ,essasin-
tegrações foramamadurecidas,fechandopequenaslacunasqueexistiamnasversões
anteriores.
Emtodos asintegrações,aCDIfuncionabasicamentecomouminjetorde re-
cursosdaoutraoutraespecificação,porissovamosnosaternestecapítuloaalgumas
integrações quesãomaisperceptíveisnodiaadia.
8.1 Relação entre CDI eEJB/JPA
QuandoutilizamosCDIeJPAdentrodeumservidordeaplicações, quetambémtem
disponívelaimplementaçãodeEJB, nemnos damoscontadeestar usandoessaúl-
timaquandovamossalvarumobjetonobancodedados. A p e s a rdetermospassado
porJPAapenasdepassagememalgunsmomentos, porestenãoserofocodestelivro,
sabemosquesóconseguimosescrever nobancodedadosutilizandoJPA seexistir
umatransaçãoativa. Semtransações épossívelapenaslerdados.
Acontecequequando temosEJBsdisponíveis,podemosfazer algotãosimples
quantooseguinte parasalvarumobjeto.
@Stateless
public class FuncionarioBean {
@Inject
private EntityManager em;
public void salvarFuncionario(Funcionario funcionario){
em.persist(funcionario);
}
}
Bastaanotarnossobeancom @Statelessou @Statefulparaquetodosos
métodosdentrodobeansejamautomaticamentetransacionais.Ouseja,noexemplo
queacabamosdever,ométodo salvarFuncionarionãoprecisalidarcomtran-
sações, poisissoéfeitoautomaticamentepeloservidor.Ótimo, maseseestivermos
152

## Página 158

CasadoCódigo Capítulo8. ArelaçãodaCDIcom asdemaisespecificações JavaEE
utilizandoCDIeJPAemumservletcontainercomoo T o m c a touJetty?Nessecaso
teremosquelidarcom astransações manualmente,comonoexemploaseguir.
public class FuncionarioBean {
@Inject
private EntityManager em;
public void salvarFuncionario(Funcionario funcionario){
EntityTransaction tx = em.getTransaction();
tx.begin();
em.persist(funcionario);
tx.commit();
}
}
Nosdoisexemplos,consideramos queexisteumprodutorCDIquedisponibiliza
o EntityManagerparanossobean,assimcomovistonaseção5.1.Principalmente
paraquemestáacostumadoàpraticidade dagestãoautomáticadetransações,e viu
comoésimplesfazeruminterceptadorcomCDI(como naseção6.1),ficaa dúvida:
porqueaCDI nãouminterceptador prontoparagerenciartransações?Aresposta
éque,pormaisquesejasimplesfazerisso,ACDI nãooferecenadaquesobreponha
algojádisponívelnoJavaEE.Sejátemosessafuncionalidade nosEJBs,aCDI não
ofereceumaalternativa.
Isso,noentanto,não significaquenão pudéssemoscriaresseinterceptador
quandoformosrodarCDIeJPA foradeumservidordeaplicaç ão,ouquenãotenha-
mosextensões prontasquenosoferecemessafuncionalidade. Aindaveremossobre
extensões nocapítulo9,maselassãobasicamentejarsqueadicionamosànossaapli-
caçãoeassimganhamosfuncionalidades quevãoalémdaCDIpadrão.
Paranossasorte,essafuncionalidadeé tãosimplesdeimplementar quesequer
precisamoslançarmãodafuncionalidadedeextensão, bastapraissoimplementar
uminterceptadorconforme jávimos.U mexemplodeimplementaçãoquenosdaria
essafuncionalidadeéocódigoaseguir.
@Interceptor @Transacional
public class InterceptadorGerenciadorDeTransacoes {
@Inject
private EntityManager entityManager;
153

## Página 159

8.1.RelaçãoentreCDIeEJB/JPA CasadoCódigo
@AroundInvoke
public Object gerenciaTransacao(InvocationContext context)
throws Exception {
EntityTransaction tx = null;
try {
//em ambiente JTA apenas o getTransaction já lança exceção
tx = entityManager.getTransaction();
tx.begin();
Object retorno = context.proceed();
tx.commit();
return retorno;
} catch (RuntimeException e) {
if(tx != null) tx.rollback();
throw e;
}
}
}
No nosso exemplo, apenas injetamos no interceptador o mesmo
EntityManager que está disponívelno bean, e então fizemos a gestãoma-
nualdatransação. Conformeocomentárionocódigo,temos quetomarcuidado
paranãocolocarparaexecutaresseinterceptadordentrodoservidordeaplicaç ão,
poisládentro,quemcuida dastransações éo container. Porisso,éinteressante
ativaresseinterceptadorapenasem servlet containers.
Paranossoexemplofuncionar,precisamos quenosso EntityManagertenha
oescopoderequisiç ão,queéoquemaisseassemelhaaoescopode transaçãodos
EJBs.
public class ProdutorEntityManager {
@Produces @ApplicationScoped
private EntityManagerFactory factory = Persistence
.createEntityManagerFactory("default");
@Produces @RequestScoped
public EntityManager criaEntityManager(
EntityManagerFactory factory){
return factory.createEntityManager();
}
154

## Página 160

CasadoCódigo Capítulo8. ArelaçãodaCDIcom asdemaisespecificações JavaEE
public void fechaEntityManager(
@Disposes EntityManager entityManager){
entityManager.close();
}
}
Esseescopoémuitoimportante,poissenãooespecificarmos,aCDI atribuio
escopo dependent,euma novainstânciaserácriadatodavezqueforsolicitado.No
nossocaso,oprolemaseriaaexistênciadeumainstânciade EntityManagerden-
trodaclasse FuncionarioBean,eoutrainstânciadentrodointerceptador,fazendo
nossomecanismonãofuncionarcomooesperado. Depoisdetudo,precisamos ape-
nasusarointerceptador.
@Transacional
public class FuncionarioBean {
@Inject private EntityManager em;
public void salvarFuncionario(Funcionario funcionario){
em.persist(funcionario);
}
}
OU
public class FuncionarioBean {
@Inject private EntityManager em;
@Transacional
public void salvarFuncionario(Funcionario funcionario){
em.persist(funcionario);
}
}
Ocódigodo interceptor binding @Transacionalnãoestánesseexemplo,mas
jávimoscomocriá-losquandoestudamosinterceptadores.
Agorasenossaaplicação trabalharcommaisdeum bancodedados,teremos
maisdeum EntityManagerdisponível.Nessecaso,precisaremosfazerumainje-
çãomaiselaboradanonosso interceptadorparaconseguirmosutilizaro objetocor-
reto.Comoaindanãovimoscomofazer isso,vamosretomaresseassuntonaseção
4.8,ondeveremoscomofazerinje ções programáticas.
155

## Página 161

8.2. RelaçãoentreCDIeJSF CasadoCódigo
Sequisermosdisponibilizar nossointerceptadorparaqualqueraplicação,basta
colocaro arquivo beans.xmldentrodapasta META-INFdojarqueiráconter
nossointerceptador.Comisso,quandoocontextoCDIiniciar naaplicaçãoqueusa
nossosjar,portermosesse arquivonesselugar,o jarseráconsideradoumpacote
CDI,eointerceptorequalquer outrobeanqueestiverdentrodo jarficarádisponível
naaplicação.
Porémcomojávimosnaseção6.1,nãobastadefinirointerceptador,precisamos
ativá-lo.Issopodeserfeitonoarquivo beans.xmlousimplesmenteadicionando
aanotação @Priorityaointerceptador.Massetivermostantoaplicações quero-
damem servlet containerquandoemservidoresdeaplicaç ão,o maisindicadoseria
ativarmosviaXMLsomentenoambientecorreto;uma vezqueaanotaçãojáativao
interceptadorporpadrão.
8.2 Relação entre CDI eJSF
OJSF2.0eoCDI1.0tiveramalgunsproblemasdeintegraç ão,poisforamdesen-
volvidosparalelamente naépocadolançamentodoJavaEE6. AgoranoJavaEE7 ,
comJSF2.2eCDI1.1,essesproblemas foramsuperados.Oúnico pontoqueainda
temosalgum atritoécomasanotações deescopodoJSF, queseencontramnopa-
cote javax.faces.bean,poiselastêmamesmafunçãodosescoposdefinidos no
pacote javax.enterprise.context.T a n t oéqueadocumentaçãodoJSF2.2 já
informaqueasanotações dessepacotedevem serdepreciadasem novasversões da
especificação,e nossugereusarasanotações dopacoteCDI semprequepossível.A t é
porque,porcontadessasobreposição,aCDI nãoreconheceasanotações deescopo
dopacotedoJSF.
Utilizandoasúltimasverõesdisponíveis atéomomento—JSF2.2eCDI1.1—
nãoteremososproblemasdeincompatibilidade, quesãoprincipalmenteaincapaci-
dadedeinjetarmosrecursosatravés daCDIdentrodeconversoresevalidadoresJSF.
Dequalquerforma,mesmoutilizandoasversõesanterioresconseguimos contornar
essadeficiênciautilizandoextensões daCDIcomo DeltaSpikedafundaçãoapache
(http://deltaspike.apache.org/jsf.html). Porém,veremosmaisdeextensões noca-
pítulo9,porenquantobastasabermosqueessaslimitações nãoprecisamimpactar
nossasaplicações.
Agoraquejáfalamosdohistórico, dasantigaslimitações equeasnovasver-
sões asresolveram,vamosexploraro quepodemosfazercomaintegraç ãoentre
essasduasespecificações. Parainiciarmosdeuma formaleve,podemoscriar mé-
156

## Página 162

CasadoCódigo Capítulo8. ArelaçãodaCDIcom asdemaisespecificações JavaEE
todoprodutoresparaobjetosdocontextoJSF quemuitasvezesprecisamos buscar
viaAPI,como porexemplo FacesContext, ExternalContext,ambosdopa-
cote javax.faces.context,e javax.faces.application.Application.
Esses,éclaro,sãoapenasalgunsexemplos,podemosfazer issoparaqualqueroutro
bean.
public class ProdutorFaces {
@Produces
private FacesContext context = FacesContext.getCurrentInstance();
@Produces
private ExternalContext externalContext = FacesContext
.getCurrentInstance().getExternalContext();
@Produces
private Application application = FacesContext
.getCurrentInstance().getApplication();
}
Podemosaindacriar qualificadores representando os escoposquepodemos
acessarvia ExternalContexteinjetardiretamente mapasdentrodosnossos be-
ans.
@Inject @ApplicationMap
private Map<String, Object> applicationMap;
@Inject @SessionMap
private Map<String, Object> sessionMap;
@Inject @RequestMap
private Map<String, Object> requestMap;
@Inject @RequestParameterMap
private Map<String, String> requestParameterMap;
E para disponibilizarmos esses objetos,basta incrementarmos mais nosso
ProdutorFacescomosseguintesmétodos.
@Produces @ApplicationMap
public Map<String, Object>
157

## Página 163

8.2. RelaçãoentreCDIeJSF CasadoCódigo
disponibilizaApplicationMap(ExternalContext ec){
return ec.getApplicationMap();
}
@Produces @SessionMap
public Map<String, Object> disponibilizaSessionMap(ExternalContext ec){
return ec.getSessionMap();
}
@Produces @RequestMap
public Map<String, Object> disponibilizaRequestMap(ExternalContext ec){
return ec.getRequestMap();
}
@Produces @RequestParameterMap
public Map<String, String>
disponibilizaParameterMap(ExternalContext ec){
return ec.getRequestParameterMap();
}
Comoacabamosde ver,ébemsimplese útilfazeresse tipodeintegração,ea
únicacoisaqueusamosfoiafuncionalidadedaCDIdecriar produtores.Essesexem-
plosdeixam bemclarocomoaCDIéao mesmotempoabrangente—poisusamos
comqualquercoisadentrodo JavaEE—,poderosa,eomaisimportante,simples.
ObservadoresparaeventosdoJSF
Criarproduresparaosobjetos maisacessadosdoJSFé bastantesimples,mas
agoravamosdarumpassoalémnessaintegração.TrabalhandocomJSF,emalguns
momentosprecisamosinteragircomociclode vidadeumarequisiç ão,fazendo al-
gumaoperaçãodepois dafase Restore V i e wouantesda Render Response,apenaspara
exemplificar. Porém,parafazerissonão podemosusar,pelomenosnãodeforma
natural,nossos beans“ d enegócio”,quesão POJOs;esimimplementarainterface
PhaseListener.
public class SegurancaPhaseListener implements PhaseListener {
@Override
public void afterPhase(PhaseEvent event ) {
//verifica se o usuário está logado
//se não estiver, envia para tela de login
158

## Página 164

CasadoCódigo Capítulo8. ArelaçãodaCDIcom asdemaisespecificações JavaEE
}
@Override
public void beforePhase(PhaseEvent event ) {
}
@Override
public PhaseId getPhaseId() {
return PhaseId.RESTORE_VIEW;
}
}
Nesseexemplo,criamosumlistener quevaiverificarseousuárioestálogadoou
nãoe,casonãoesteja,enviá-loàteladelogin.Ocódigo quefazissonão importa,
poisvariaem cadaorganização.Ointeressanteaquié analisarmoscomotemos que
fazer,ecomo seriainteressantefazermos,como noexemploabaixo.
public class SegurancaListener {
public void verificaLogin(
@Observes @After @RestoreView PhaseEvent e){
//executa a lógica de checagem do login
}
}
Avantagemdosegundoexemplo,é quepodemoslidarcomoseventosdociclo
devidadoJSF damesmaformaquefazemoscomqualquer outroevento,ouseja,
dentrodosnossos beans.U m aoutralimitaçãoquecontornamoscomessa mudança,
équeantesdaversão2.2doJSF, nãoerapossíveltermos pontosdeinje çãodentro
dos PhaseListeners,oquenoslimitavabastante.JáusandoeventosCDI,mesmo
usandoJSFanterior,nãotínhamosesseproblemapoisquemescutao eventojáéum
beanCDI.Essalimitaçãonoentandoéfacilmentecontornadautilizandoo módulo
JSFdajácitadaextensão DeltaSpike.
Mascomo podemos,sem a necessidade de qualquer extensão disparar um
eventoCDIequivalenteaum PhaseEventdoJSF?Aimplementaç ãonãoédifícil,
eusaremososmesmosmecanismosdeeventos quejávimosatéaqui.Paraavançar-
mosaospoucos,vamosiniciar apenascomaimplementaçãoqueresolveexatamente
ocenárioquequeremosobservar,queéomomentologoapósotérminodafase Res-
tore V i e w.
159

## Página 165

8.2. RelaçãoentreCDIeJSF CasadoCódigo
public class EventPhaseListener implements PhaseListener {
@Inject
@After @RestoreView
private Event<PhaseEvent> afterRestoreView;
@Override
public void afterPhase(PhaseEvent event ) {
afterRestoreView.fire(event);
}
@Override
public void beforePhase(PhaseEvent event ) {
}
@Override
public PhaseId getPhaseId() {
return PhaseId.RESTORE_VIEW;
}
}
Somenteissoésuficientepararesolvernossoproblema. Contudo,olhandoo
exemplo,vemosqueusamosinjeçãodedependênciasdentrodo PhaseListener,
ecasovocêprecisefazerissodentrodeumaaplicaç ãoquenãoutilizeaversão2.2do
JSF,vocêteráquelançaresseseventosde outramaneira.
Paraisso precisaremos doobjeto BeanManager, quepode ser obtidovia
injeção (quenão está disponívelno nossocenário),ou via lookup combase
em seu nome JNDI. Aobtenção dessa instância seráfeita através do método
CdiUtils.getBeanManager(),queporenquantoiráabstrairasdiferençasdesse
processoquandoestamosemambiente JavaEEounão.Nãosepreocupe,poisvere-
mosessesdetalhesquandoabordarmoscomousarCDIemdiferentesambientes, no
capítulo10.
public class EventPhaseListener implements PhaseListener {
@Override
public void afterPhase(PhaseEvent event ) {
BeanManager beanManager = new CdiUtils().getBeanManager();
beanManager.fireEvent(event, new AnnotationLiteral<After>(){},
160

## Página 166

CasadoCódigo Capítulo8. ArelaçãodaCDIcom asdemaisespecificações JavaEE
new AnnotationLiteral<RestoreView>(){});
}
...
}
Agoranossocódigofuncionaemambientes préJSF2.2,e apesardemaistraba-
lhoso,oprocessoparaenviaroeventosebaseiaemalgoquejávimosnaseção7 . 4,que
sãoosliteraisdequalificadores. Parausarométodo BeanManager.fireEvent
bastapassarmosoobjetoquerepresentao evento,eseusqualificadores,quein-
dependentedetermos ounão usadoinje çãodedependência, são o Aftereo
RestoreView.
Comojásabemoslançareventosdentrodo PhaseListeneremqualquerver-
sãodoJSF,voltaremosaincrementara EventPhaseListenerparaqueagoraela
dispareparaocontextoCDI eventoreferentesatodasasfasesdoJSF.Comoesselivro
ébaseadoemJavaEE7 ,usaremosoexemplodoJSF2.2 ousuperior,quesuportain-
jeçãodedependênciasno PhaseListener,mascomoquevimosseremoscapazes
deadaptaroexemplo paraoutroscenários.
Quandoestudamossobreeventos,e tambémagoraquandovimoscomo usar
umaversão maisantigadeJSF, usamos AnnotationLiteralsparadiminuira
quantidadedeinje ções queprecisamosusarparaimplementarnossasolução. Em
vezdeusarmosalgoparecidocomoprimeiroexemploaseguir,faremos algomais
parecidocomosegundo.
@Inject
@Before @RestoreView
private Event<PhaseEvent> beforeRestoreView;
@Inject
@After @RestoreView
private Event<PhaseEvent> afterRestoreView;
@Inject
@Before @ApplyRequestValues
private Event<PhaseEvent> beforeApplyRequestValues;
...
Seguindoessalinha,teríamos pelomenos12(doze)pontosdeinje çãonanossa
classe,poisteríamoso beforeeo a ft e rparacadaumadas6(seis)fasesdoJSF. Nolugar
dessaabordagem,utilizaremosa formaprogramáticacomopodemosveraseguir.
161

## Página 167

8.2. RelaçãoentreCDIeJSF CasadoCódigo
public class EventPhaseListener implements PhaseListener {
@Inject
private Event<PhaseEvent> event;
@Override
public PhaseId getPhaseId() {
return PhaseId.ANY_PHASE;
}
@Override
public void afterPhase(PhaseEvent event ) {
disparaEvento(event, new AnnotationLiteral<After>(){});
}
@Override
public void beforePhase(PhaseEvent event ) {
disparaEvento(event, new AnnotationLiteral<Before>(){});
}
public void disparaEvento(PhaseEvent phaseEvent,
Annotation qualificadorAntesOuDepois ){
Annotation qualificadorFase = null;
if(RESTORE_VIEW.equals(phaseEvent.getPhaseId())){
qualificadorFase = new AnnotationLiteral<RestoreView>(){};
}
else if(APPLY_REQUEST_VALUES.equals(phaseEvent.getPhaseId())){
qualificadorFase =
new AnnotationLiteral<ApplyRequestValues>(){};
}
else if(PROCESS_VALIDATIONS.equals(phaseEvent.getPhaseId())){
qualificadorFase =
new AnnotationLiteral<ProcessValidations>(){};
}
else if(UPDATE_MODEL_VALUES.equals(phaseEvent.getPhaseId())){
qualificadorFase =
new AnnotationLiteral<UpdateModelValues>(){};
}
else if(INVOKE_APPLICATION.equals(phaseEvent.getPhaseId())){
162

## Página 168

CasadoCódigo Capítulo8. ArelaçãodaCDIcom asdemaisespecificações JavaEE
qualificadorFase =
new AnnotationLiteral<InvokeApplication>(){};
}
else if(RENDER_RESPONSE.equals(phaseEvent.getPhaseId())){
qualificadorFase =
new AnnotationLiteral<RenderResponse>(){};
}
event.select(qualificadorAntesOuDepois)
.select(qualificadorFase)
.fire(phaseEvent);
}
}
Ficouum trechodecódigoumpouco longo,masapesardenãosermuitoes-
tético,commuitos if else,ésimplesdeentender. Primeiramentealteramoso
retornodométodo getPhaseId()parainformarquenosso listenerescutatodas
asfasesdoJSF. Depoisapenasrepetimosalgoquejávimosquandoestudamoseven-
tos: injetamosumeventogenérico,semqualificadores,edepoisutilizamoso mé-
todo select(Annotation qualificador) paraadicionarosqualificadores no
nossoeventoantesdedispará-lo.Percebacomoainterfacefluentefacilita nossotra-
balho—bastachamarduasvezesométodo,semprecisarcriarum a r r a youlistapara
passarosqualificadoresdeuma vez.
Épossívelexplorar aindamuitomaispossibilidadesdeintegraçãoentreCDI,JSF
eJPA,masointuitodessas sessões foimostrarocaminho,edeixar queque seusco-
nhecimentosdeCDIadquiridos atéaquisugiramoutroscenários.Alémdomais,se
entrarmosemmuitosdetalhesdeJSFeJPA,desviaremoso focodolivro,queéCDI.
Mascasotambémqueiraaprofundarseusconhecimentosnessasduasferramentas,
dêumaolhadanomeu livrodaCasadoCódigo sobreesseassunto[?].
8.3 Relação entre CDI eJMS
NoJavaEE7 ,aespecificaçãodeJMS—serviçodemensageria Java—ganhouuma
novaAPI,bemmaisfácildeusar,ebemintegradacomCDI. Nessaseçãoiremos ver
comoutilizaressapoderosaferramenta juntocomafuncionalidadedeeventos da
CDI.
AnovaAPIdeJMS, queveionaversão2.0 daespecificação,trouxepara elaa
163

## Página 169

8.3.RelaçãoentreCDIeJMS CasadoCódigo
facilidadequeos Session Beanspassaramaterapartirdasuaversão3.0. Issopor
sijápodeserumfator queajudea aumentarautilizaçãodemensageriadentro das
aplicações Javacorporativas.Éverdade quesomenteousodemétodosdenegócio
assíncronosjáfacilitabastantenossotrabalhoemexecuções maiscustosas,mas JMS
vaialém.
Oserviçodemensageria Javadáanossaaplicaçãoumacapacidadedeprocessa-
mentoassíncronomuitogrande.Paraexemplificar,vamosimaginarumaaplicaç ão
deprocessamentodepagamentosdeuma outraaplicaçãodecomércioeletrônico.
A p e s a rdasinterfacesdaatualidadenosdaraimpressãode sertudosíncrono,vamos
pensarmaisespecificamenteemboletos, quenaturalmentesãoassíncronos,geral-
mentesendoprocessadoscomumdiade atraso.
Imaginequesuaaplicaçãotemumaltopoderdeprocessamento,porémdevidoa
umasuperpromoçãodeumgrandesitedevendas, asrequisições começaramache-
garemum volumemuitomaiordoquesuaaplicaçãoconsegueprocessar.Ocenário
poderiasercatastrófico,suaaplicaçãopoderiaparardereceberrequisiçõesenquanto
tentaprocessarademanda,eositede vendaspoderiaperderinúmerosnegóciospois
nãoconseguiriaterminaravenda, quedependedosistemadepagamentos.Depen-
dendodo caso,caberiaatéprocesso.
OJMS,assimcomoqualquer outroserviço,nãoéaPanaceiaquedeixarátudoem
ordememum piscardeolhos, masajudaráemuito.Nonossoexemplohipotético,
aaplicaçãodevendas, nãosolicitariaparanossaaplicaçãoprocessaropagamentoe
ficariaesperando.Elaregistrariaavendanafiladeprocessamentoeresponderia que
eminstanteso usuárioreceberiaanotificaç ãoouentãofariauma teladeprogresso
quefazo usuárioaguardaralgunsinstantes paradaraimpressão queoprocessoé
“online”.
Essafilageralmenteépersistente,ouseja,setivermosmilvendasparaserempro-
cessadaseoservidor cair,quandoestevoltaraindateremososmil itensnafila.Além
disso,afilaégerenciadaautomaticamentepeloservidordeaplicação.Enquantoexis-
tiremelementos nafila,obeanresponsávelporprocessarasvendasseráchamado.
Eo quedápoderaessaferramentaé quehá,naverdade,um pooldebeansdeum
mesmotipo,paralelizandooprocessamentoomáximopossível parasuaaplicação
darcontadademanda.Essesbeansqueprocessamelementosdeuma fila,outópico,
sãoosMDBs, ou Message-Driven Beans.
Aprincipaldiferençadeum Message-Driven Beanparaum Session Beanéquea
aplicaçãode vendasnãoacessadiretamenteoMDBcomofariacomoEJB. Elaco-
locaasolicitaçãonafila,eocontaineréquechamaoMDBparaprocessaropróximo
164

## Página 170

CasadoCódigo Capítulo8. ArelaçãodaCDIcom asdemaisespecificações JavaEE
elementodafila.AssimcomoosEJBs StatelessosMDBs tambémnãomantémes-
tado,e porissoemambostemoso usodo pool,queéumdosresponsáveispelaboa
responsividade.
Esselivro,porém,nãotemcomofinalidademostrarcomoutilizarJMS paraau-
mentaraescalabilidade dasnossasaplicações, porhoraveremoscomocriaruma
ponteentreoseventosCDIe asmensagensJMS.
UmasdasprincipaisdiferençasentreoseventosCDIe asmensagensJMSéque
oseventossóexistemdentrodocontextodeumaaplicaç ão,enquanto asmensagens
podemserconsumidaspordiversasaplicações. Issoporqueaotópico ouafilanão
sãoprivativosdeumaaplicaç ão,sãorecursosqueficamdisponíveisparaqualquer
aplicaçãoqueconseguirsecomunicarcomoservidor ondeelasestão.Emcenários
maioresteremosinclusiveservidoresdedicadosexclusivamenteaprocessar filase
tópicos.
Nessaseção,usaremosafacilidadedoseventoseadisponibilidade dasmensa-
gensparafazercomqueoeventolançadoporumaaplicaçãosejaescutadoporoutra.
ComunicandoduasaplicaçõescomumaponteCDI-JMS
Dentrodeum mesmosistemapodemosutilizareventos paraintegrarmódulos
diferentescomum baixoacoplamento,masquandopensamosemaplicações dife-
rentestemosaindamaisopções. Porexemplo,épossível,aocadastrarumnovofun-
cionário,dispararemoutrossistemasatarefadecriaç ãodeconta nocontroladorde
domínioeliberar seuacessonacanceladoestacionamento.E nomomentododesli-
gamentodofuncionáriocancelartodososacessosanteriormenteconcedidos. Pode
atéserpossíveltertodosessescontroles nomesmosistema,masomaiscomumnão
éesse.
Noexemploquevamosanalisaragora,vamosconsideraraintegraç ãocomuma
agênciadeempregos. Quandoumfuncionáriosedesligardaempresa,e não for
poraposentadoria,nósnotificaremosaagênciaparaqueelajáiniciea buscapela
recolocaçãodo profissionalnomercadode trabalho.Comonossaaplicaçãosóestá
tratandoaposentadoriaedemissão,vamosfazeremcimadoexemplodedemissão,
masseriapossívelolharqualquereventodedesligamentoe usaro EventMetadata
paraignorarmososdesligamentos quetivessemqualificadordeaposentadoria.
Conceitualmente,oquedesejamoséalgoassim.
165

## Página 171

8.3.RelaçãoentreCDIeJMS CasadoCódigo
Figura8.1:EventodaaplicaçãoAsendoconsumido pelaaplicaçãoB viaJMS
Pelaimagemvemosum eventoproduzidonaaplicaçãoA,sendoconsumido por
4(quatro)observadores,doisdeles daaplicaçãoB.V i acódigooesperado seriaum
códigosemelhanteaoseguinte.
public class GerenciadorFuncionarioBean {
@Inject @Desligamento(DEMISSAO)
private Event<Funcionario> eventoDemissao;
public void demitirFuncionario(Funcionario funcionario){
eventoDemissao.fire(funcionario);
}
}
Eoseguintecódigo jánosistemadaagênciadeempregos:
public class AgenciaDeEmpregos {
public void ajudarFuncionarioDemitido(
@Observes @Desligamento (DEMISSAO) Funcionario funcionario,
Logger logger){
logger.info("Ajudando {} a conseguir um novo emprego",
funcionario);
166

## Página 172

CasadoCódigo Capítulo8. ArelaçãodaCDIcom asdemaisespecificações JavaEE
}
}
Paraqueissofuncione,noentanto,vamosprecisarcolocarnanossaaplicaçãoum
observadorqueescuteesse eventoecriaumamensagem nafilaJMS,e naaplicação
daagênciadeempregoscolocarumMDB queleiaamensagemecrie novamenteo
eventonosmesmosmoldesdooriginal. Parasimplificar,criaremosnossaintegração
deformaespecíficaparaessecenário,mascomumpoucodeabstraç ãoereflexãoé
possívelcriarimplementações genéricasqueatendembemamaioriadoscasos.
IniciaremospelocódigoquecriaamensagemJMS. Nossoexemploserábaseado
naAPIsimplificadadoJMS2.0, masépossívelportarocódigoparaaAPItradicional
casoestejaexecutandoemambiente préJavaEE7 .
@Stateless
public class ObservadorDeFuncionarios {
@Inject
private JMSContext jmsContext;
@Resource(mappedName = "jms/demissaoTopic")
private Topic topicoDemissao;
@Asynchronous
public void notificaAgenciaDeEmprego(
@Observes @Desligamento (DEMISSAO) Funcionario funcionario,
Logger logger) throws Exception{
logger.info("Enviando o(a) {} para agencia de empregos",
funcionario);
jmsContext.createProducer().send(topicoDemissao, funcionario);
}
}
Estamos usando um tópico JMSque estáno mesmo servidor que nossa
aplicação, e recuperamos esse tópico via @Resource(mappedName =
"jms/demissaoTopic"). Tópicos efilas devem ser criados no servidor de
aplicação queestivermos utilizando,não éalgo da aplicação. Noglassfish, só
precisamostomarocuidadode não daromesmonome JNDIe nomefísicopara
otópico oufila,senãoo nomenãoseráencontrado. Ovalorquepassamospara o
atributo mappedNamedaanotação @ResourceéonomeJNDI,e nãoofísico.
167

## Página 173

8.3.RelaçãoentreCDIeJMS CasadoCódigo
Percebaquefizemosnossoobservadorserassíncrono,poisassim,casopassemos
autilizarumservidorJMS remoto,umapossíveldegradaçãonotempoderesposta
aocolocaramensagem nafilanãoimpactaránométododenegócio.
Aimplementaçãocomoum todoficoubemsimples.U s a m o so JMSContext
paracriarum producerdemensagenseemseguidaenviamoso objetofuncionário,
quedeveserserializável,paraotópicodedemissões. Agoranoladodaagênciade
empregosteremosumMDB queescutaessetópicoe recriaamensagemnocontexto
daquelaaplicação.
@MessageDriven(mappedName = "jms/demissaoTopic")
public class AgenciaDeEmpregosMessageBean implements MessageListener {
@Inject @Demissao
private Event<Funcionario> eventoDemissao;
@Inject
private Logger logger;
@Override
public void onMessage(Message message) {
try {
Funcionario funcionario =
message.getBody(Funcionario.class);
logger.info("Recebida a demissão do funcionario {} via JMS" ,
funcionario);
eventoDemissao.fire(funcionario);
} catch (JMSException ex) {
logger.error("Erro ao ler a mensagem via JMS", ex);
}
}
}
U mMDB, como acabamos de ver, é simplesmente umbean ano-
tado com @javax.ejb.MessageDriven e que implementa a in-
terface javax.jms.MessageListener. No corpo do método
onMessage(javax.jms.Message) precisamos apenas recuperar o con-
168

## Página 174

CasadoCódigo Capítulo8. ArelaçãodaCDIcom asdemaisespecificações JavaEE
teúdodamensagem,quenessecasoéumobjetodotipo Funcionario.Paraisso,
utilizamosométodo getBodyquefoiadicionadoàversão2.0deJMS parafacilitar
otrabalho.Comofuncionárioemmãos,esabendo queessamensageméreferente
aumademissão, bastalançarumnovoeventoCDI.
Paraabstrairmosessafuncionalidade,poderíamoscriarumobservador global
doladodanossaaplicação,e via EventMetadatacriarumobjetoquerepresenteo
evento.Emvezdetermoso objetofuncionário,teríamostambémosqualificadores
utilizados.Naoutraaplicação,noexemploaagênciadeempregos,leríamosesse ob-
jetoquerepresentao eventoe,antesdelançá-lonocontextoCDI,especificaríamos
osqualificadoresde formaprogramáticacomojáfizemosalgumasvezes.Alémdes-
sasalterações,criaríamos tambémumtópicocom títulomaisgenérico,comopor
exemplo "jms/cdiEventsTopic"oualgoparecido.
Percebatambémqueparadiferenciarmaisumaaplicaçãodaoutra,utilizamoso
qualificador @Desligamento(DEMISSAO),e naagênciadeempregosutilizamos
@Demissao.Parafacilitaracriaç ãode algogenérico,quepossasercompartilhado
pelasdiversasaplicações danossaorganização,o melhorécriarmosum jarcomo
conjuntodequalificadorese classesqueserão compartilhadasentreasaplicações.
Geralmenteesses jarsnão possuemqualquer classeinteligente,apenastiposcom-
partilhados,esãochamadosde <nomeDaAplicacaoDeOrigem>-client.jar.
Obviamente essa éapenas uma sugestão,mas fica simples perceberque to-
das as aplicações que precisarão se comunicar com anossaApp precisão do
nossaApp-client.jar.
8.4 Empacotando a smelhorias
Todososexemplos quevimosnessecapítulosão passíveisdeempacotamento, ou
seja,podemoscolocaressaspequenas melhoriasemum projetoseparado,gerarum
jar,ecolocarnasnossasaplicações.Qualqueraplicaç ãoqueutilizaressejarteráauto-
maticamentesuporteàinje çãoderecursos daJPAeJSF,efazendo asgeneralizações
comentadasnaúltimaseção,poderíamos tereventosCDI passandodeumaaplica-
çãoparaaoutraviaJMS.
Implementar isso não énada complicado —basta colocar os arquivos
de configuração no local correto. Enquantonas aplicações web os arquivos
faces-config.xmle beans.xmlficamgeralmentenapasta WEB-INF,aocriar
umabibliotecaprecisamoscolocaressesarquivosdentro dapasta META-INFque
ficanaraizdo jar.
169

## Página 175

8.4. Empacotandoasmelhorias CasadoCódigo
Assim,mesmoaindasemtermosvistoomecanismodeextensões propriamente
dito,jáconseguiremoscriarbibliotecasde apoiocommuitafuncionalidadeinteres-
sante.
170

## Página 176

Capítulo9
ExtensõesCDI
U m aespecificaçãonadamaisédoqueumapadronizaçãodecomofazerdetermi-
nadatarefa.AJPApadronizao mapeamentoobjeto-relacional,JSFpadronizacomo
desenvolverclientes webcomumsofisticadogerenciamentodeestadoecomCDI
temosapadronizaç ãodecomoinjetardependênciasegerenciarescoposdentrodo
JavaEE.Porém,semprequealgoépadronizado,atendênciaélimitarainovaç ão.
Como,porexemplo,inovarnomapeamentoobjeto-relacionalseaJPAdefineasfun-
cionalidades?
Aformaencontradaparaqueainovaçãocontinue apesardasespecificações é
atravésdaadiçãodefuncionalidades nãoespecificadas.Estasadicionamfuncionali-
dadesimportantesàsimplementaçõesdasespecificações.Oexemplo maisnotórioé
odaJPA,ondetemosoEclipseLink(http://www.eclipse.org/eclipselink )comoim-
plementaçãodereferência,eo Hibernate(http://hibernate.org)comoaimplemen-
taçãomaisutilizada.
ProsseguindonaanálisedaJPA,temosfuncionalidadesnãoespecificadasnessas,
eem outrasimplementações, queadicionamcaracterísticas muitoimportantesem

## Página 177

9.1.DoSeamàCDI CasadoCódigo
cadaimplementação.NoHibernatetemosocachedeconsulta,quenospermiteevi-
tardiversasconsultasdesnecessáriasnobancodedados,alémdo cachedesegundo
níveldeentidades quefoiadicionadoàespecificaç ãodepois quejáestavadisponí-
velnoHibernate.JánoEclipseLinktemoso suportea multitenant,quenospermite
escolherdiferentesestratégias parafazernossaaplicaçãofuncionarcomdiferentes
clientes. Issopermitequeumamesmainstânciadeaplicaç ãode vendassejautili-
zadapordiferentessitesde e-commerce,porexemplo.
Qualoproblemadeumaimplementaç ãoadicionarfuncionalidades não espe-
cificadas?Praticamentenenhum,desde quevocênãotroquedeimplementação.O
“detalhe”équeapossibilidadede trocardeimplementaçãoéuma dasvantagensda
especificação,eacabamosperdendo isso.Seporexemploutilizarmoso suporteaca-
chedeconsultadoHibernate,casomudemosparaoEclipseLinkteremos quefazer
algumaalteraçãonanossaaplicaçãoparausarosuporteequivalentedoEclipseLink.
Hácasostambémemqueumaimplementação não temumequivalenteàfuncio-
nalidadedaoutra.Porexemplo,atéomomentooHibernatenãotemumsuportea
multitenanttãoelaboradoquantoodoEclipseLink.
Qualadiferençadosuporteaextensões daCDI?
ComoaCDIéumaespecificaç ão maisrecente,inteligentementeadicionouo
suporteaextensõesportáveis,de formaqueimplementadoresdaespecificação,ou
mesmoqualquerumdenós,pudessemdesenvolverfuncionalidadesalém dasespe-
cificadasquenãodependamdeumaimplementaç ão,esim daprópriaespecificação.
V o l t a n d oaoparalelocomaJPA, seriacomosepudéssemosadicionarafuncio-
nalidadede multitenantdoEclipseLinkenquanto usamosoHibernatecomoimple-
mentaçãodaJPA.Issonospermiteaomesmotempodesfrutardainovaçãoconstante
queasimplementações dasespecificações nosoferece,sem, noentanto,ficarmos
presosaessasimplementações. U s a m o saimplementaçãoe asfuncionalidadesadi-
cionais,masnahoradetrocardeimplementa ção,continuamoscomosadicionais.
Essasofisticaçãofoiresultadodaevoluçãodo frameworkSeam,desenvolvidopela
JBoss,e queacabouservindode basepara aCDI.
9.1 DoSeam à CDI
OJBoss Seamfoiumframeworkcriadocomo objetivodeapararasarestasexisten-
tesentreasdiversasespecificações doJavaEE5.Essaversãodo JavaEEfoifocadana
facilidadedeimplementaç ão,e foiumdivisorde águasdoJavaparaaplicações cor-
172

## Página 178

CasadoCódigo Capítulo9. ExtensõesCDI
porativas,poissaiudealgoextremamenteverboso,cheiodeXML, paraalgosimples
deimplementarutilizando asanotações, quehaviamsidointroduzidaspouco antes
noJava5.
Autilizaçãodo JavaEEficou bemmaissimples,comJPA1.0,JSF1.2eEJB3.0.
Porém,essasespecificações nãotinhamumtrabalhodeintegraçãomuitoelaborado,
eaíentravaoSeam,quepodemostraduzir parajunção,integração.
OSeamfezbastantesucesso,ealémdesimplesmenteintegrar asdiversases-
pecificações doJavaEE,passouaoferecerumacole çãodeutilidades,comogera-
çãofacilitadadePDFs,seguran ça,integraçãocom BPM(workflow)eenginede re-
gras(Drools),dentreoutras. Enquantoalgumasdessasutilidades são integrações
comoutrosframeworks,quepodemserutilizadosseparadamente,comoo Drools
(http://www.jboss.org/drools)eo jBMP(http://www.jboss.org/jbpm),outrascoisas
comoosuporteaescritade PDFsatravésdetags,como sefosseumHTML,era algo
totalmenteintegradoao Seam.
Ocorreque,conceitualmente,muitasdessasutilidadeseramacessórias,e seria
interessantepoderutilizá-lascomqualquerframework.Enquanto isso,oSeampos-
suíaumnúcleo queerao responsávelpelainjeçãodedependências; núcleoeste
que“concorria”comonúcleodeoutrosframeworkscomoo Spring(http://www.
springsource.org/spring-framework).
ComooJavaEEnão possuíaumaespecificaç ão quepadronizasseesse meca-
nismo,em vezdedesenvolveruma novaversãodo Seamevoluindotantoo core
quantoosutilitários,aJBossliderouaespecificaç ãodaCDIcomo substitutadonú-
cleodoSeam. Ecomoeradesejável queosutilitáriosdo Seamnão seperdessem,
mastambémadicionartudoaquilo naespecificaçãodesviaria seufoco,asoluçãofoi
tratá-loscomoextensões. Dessaforma,aCDI jánasceucomaideiade serextensí-
vel.Aseguirépossível verumaimagem, queficavadisponívelnositedo Seam,que
ilustraessaevoluçãodo Seam2,paraoSeam3,quepassouaserapenasumacole ção
deextensões.
173

## Página 179

9.2. Extensõesportáveisdisponíveis CasadoCódigo
Figura9.1:Evoluçãodo Seam2atéaCDIeo Seam3
AJBoss noentantodescontinuouoSeam3,epassouoprojetoparaaFundação
Apache,queochamoudeDeltaSpike(http://deltaspike.apache.org). Algunsmó-
dulos,entretanto,tornaram-sebibliotecasindependentes,como podeservistona
páginadoSeam(http://www.seamframework.org).
9.2 Extensões portáveis disponíveis
OprojetoDeltaSpikeaindaestábemrecente,e apesardetersebaseadoemversões
completasdosmódulosdo Seam3,aindanão temumaversãoestáveldisponível.
Aindaépossívelacessarosmódulosdo Seam3,maselesnãosãomaisatualizados,
entãobugs nãoserãocorrigidos nemnovas funcionalidadesintroduzidas. Mesmo
assimpodeserumaopçãocasooDeltaSpikenãoofereçaafuncionalidade quepro-
curamos.
HáaindaoMyFaces CODI(https://bitly.com/myfaces-codi), tambémdaapa-
che,quetemdiversasfuncionalidades maisvoltadasparaJSF,comopodemos ver
nawikidoprojeto(https://bitly.com/codi-wiki).Umasdasprincipaisvantagensdo
CODI,sãoosdiferentesescoposoferecidos,comoumaconversaç ãodiferente dapa-
drãodoCDI,com suportea restart,subconversações, grupodeconversações dentre
outraspeculiaridades.Temos tambémescopos windowe v i e waccess.Adocumen-
174

## Página 180

CasadoCódigo Capítulo9. ExtensõesCDI
taçãodessasfuncionalidadesestádisponível nawikidoprojetoCODI,nomódulo
JSF.Certamenteestaéuma páginaquevalea penaservisitada.
HátambémestalistacomdiversasextensõesCDI: https://groups.diigo.com/
group/cdi-extensions.Aquiépossívelencontrarlink paraasextensõesdo Seam3,
quejánão estão maislistadasnapáginadoprojeto,alémdeoutrosqueapontam
parapostsdeblogserepositórios(github ououtros)quepossuemasmaisdiversas
implementações deextensõesCDI.
Masoquepodemosesperardessasextensões? Alémdealgumasinovações,o
maiscomumétrazerparaoambientenãoJavaEE,funcionalidades quegeralmente
jáestãodisponíveis nesseambiente.Nessecasonãotemosalgonovo,apenasconse-
guimos,porexemplo,desfrutardegerenciamento automáticodetransações dentro
deumservletcontainercomo T o m c a touJetty.
Temostambém,noexemplodoJSF,umadiantamentodefuncionalidades que
viriamsomenteemversõesseguintes dasespecificações. Porexemplo,amaioriadas
extensõesintegradascomJSFpermitemainje çãodedependênciasdentrodecon-
versores,validadorese PhaseListenersemversõesanterioresaoJSF2.2, quando
issoaindanãoerapossívelnativamente.
9.3 Criando nossas extensões
CriarumaextensãoCDIésimples,efaremosdoisexemplos queprovarãoisso.An-
tesvamosentendero queéprecisoparacriarumaextensão.ACDIfaz usodeuma
funcionalidadeadicionada noJava6,queéumaformasimplificada,epadronizada,
decarregaraimplementaçãodeum serviçoqualquer.É bemparecidocomo quevi-
moslánoinício,naseção1.3,ondecarregávamosaimplementaçãodeumainterface
deum arquivoproperties.
Essa funcionalidade é oferecida através da classe
java.util.ServiceLoader,e seufuncionamentoésimples,bastacriarmosum
arquivotextocomo nomedainterface(ou classeabstrata)queestamosimplemen-
tando,ecolocá-lodentrodapasta META-INF/services.Nonossocaso,estaremos
implementando a interface javax.enterprise.inject.spi.Extension,
então todas as extensões CDI estarão no arquivo
META-INF/services/javax.enterprise.inject.spi.Extension.
Dentrodessearquivocriaremosumalinhacomo nomecompletode cadaclasse
queimplementaainterfaceemquestão.
Ainterface ExtensiondaCDInãopossuiqualquermétodo paraimplemen-
175

## Página 181

9.3. Criandonossasextensões CasadoCódigo
tarmos,éapenasoquechamamosdeinterfacede marcação. Emvezdeusarmos
métodofixos,aCDIdefiniudiversoseventos quepodemosobservardurantea su-
bidadaaplicação,eentãofazer asmodificações quedesejarmos. Existemdiversos
eventosquepodemosobservar, taiscomo:
• BeforeBeanDiscovery
• AfterBeanDiscovery
• ProcessAnnotatedType
• ProcessBeanAttributes
• ProcessProducer
• ProcessObserverMethod
• ProcessInjectionPoint
Além desses, temos muitosoutros que podem ser encontrados no pacote
javax.enterprise.inject.spi.Aliás,agoraqueestaremosdesenvolvendoex-
tensões,passaremosa olharbastanteparaospacotes spiqueexistemdentrodaCDI.
SPIsignifica Service Provider Interface,ecomoa partirdeagoraestaremosdesenvol-
vendoextensões queproveemserviçosdentrodaCDI,éessainterfacequeusaremos.
Interfaceaquinosentidomaisamplo,comoum pontodevistada APIdeCDI.
Ofuncionamentobásicodasextensõeséobservardeterminado evento,emodi-
ficaroobjetodetectadopelaCDI.Comoomecanismodeextensãoéprojetado para
nospermitiralterarocontextooriginal, nossasextensõesexecutamlogo nasubida
daaplicação,antesdainjeçãodedependênciaestardisponível,etemosacessoa obje-
tosmodificáveisquerepresentamocontento atéentão.Ouseja,podemosmodificar
asanotações deum beanqueacaboude serlido,oumesmoacessaralistagemdos
beanseremover,ouadicionar,umelemento ládentrodocontexto.
Pormaisqueestemecanismodeextensão sejamuitobemprojetado,esimples
deusar,aindaexistemdetalhes quenãoestãodisponíveis na SPI,nosobrigandoa
utilizarclassesespecíficasdaimplementação,quenonosso casoéaimplementação
dereferência,oW e l d. Quandoprecisamosutilizardessesmecanismos,temos as
chamadasextensões nãoportáveis,poisestamosnosprendendoàimplementaç ão.
Issomuitasvezesnãoéumproblema,atéporquejáécomumnosprenderaumaim-
plementaçãoquandousamosJPA,porexemplo.Mascomoextensões portáveissão
176

## Página 182

CasadoCódigo Capítulo9. ExtensõesCDI
umaevolução,atendênciaéessemecanismoscontinuarevoluindo paraprecisarmos
cadavezmenosdesenvolverextensões nãoportáveis.
Nosexemplosqueiremosdesenvolver,veremosumaextensão portável,quepode
serintegradaemum projetoqueusaporexemplo OpenWebBeans(implementação
deCDI daApache);e outranãoportável,quefazusodeclassesdo W e l d.Porsorte,
osdois principaisservidoresdeaplicaç ãoopen-source,JBoss/Wildflye Glassfish,
utilizamo W e l dcomoimplementação.
9.4 Extensão portável: usando convenção em vez de
configuração
Provavelmentevocêconheceumconceito muitoutilizadohojeemdia queéauti-
lizaçãodeconven çãoem vezdeconfiguração. Sabemosqueconfiguraralgocom
anotaçãoébemsimples,aindamaisquandotemosestereótipos quepodemcombi-
nardiversasconfigurações emumaúnica anotação.
Mesmotendomeios bemsimplesdeconfigurar,vamoscriarumaconven ção:
qualquerclassedentrodeumpacote controllersouquetenhanometerminado
em Controllerdevereceberoestereótipo @Controller.Esseestereótipoape-
nasdefineoescopo r e q u e s teadicionaum nomeaobean.Napráticaéigualaoes-
tereótipo @ModelquejávemnaCDI,mascomojávimosnaseção 7 . 1,podemos
usarnossoestereótipopróprioparaadicionarinterceptadorese atémesmooutros
estereótipos. Poressemotivovamosusaressaanotação,em vezdeseparadamente
adicionar @Namede @RequestScopedaonossobean.Entãovamosaoexemplo.
public class ControllerPorConvensaoExtension implements Extension {
private Logger logger = LoggerFactory
.getLogger(ControllerPorConvensaoExtension.class);
void configuraControllers(@Observes ProcessAnnotatedType pat) {
AnnotatedType at = pat.getAnnotatedType();
logger.info("Passando pelo AnnotatedType {}", at)
}
}
A estruturada extensão ésomenteessa, bem simples. Estamosutilizando
o evento ProcessAnnotatedType, que observa cada AnnotatedType,
177

## Página 183

9.4. Extensãoportável:usandoconvençãoem vezdeconfiguração CasadoCódigo
que representa cada objeto dentro do contexto CDI. Temostambém o
evento ProcessBeanAttributes, que observa cada BeanAttributes,
que é umaoutra visão, ainda mais simples, de cada AnnotatedType.
Agora para que nossa extensão possa ser carregada, precisamos doarquivo
META-INF/services/javax.enterprise.inject.spi.Extension como
jáfoidito.Dentrodessearquivotemosapenasonomedaclassedanossaextensão.
br.com.casadocodigo.livrocdi.extension.ControllerPorConvensaoExtension
V i s t aa estrutura, vamos implementar o conteúdo do método
configuraControllers.
void configuraControllers(@Observes ProcessAnnotatedType pat) {
AnnotatedType at = pat.getAnnotatedType();
Class classe = at.getJavaClass();
if (classe.getPackage().getName().endsWith("controllers")
|| classe.getSimpleName().endsWith("Controller")) {
pat.setAnnotatedType(new AnnotatedTypeControllerWrapper(at));
logger.info("Controlador encontrado: {}", classe);
}
}
Acabamos de implementar a lógica da nossa convenção: pacote
controllers ou classe com nome terminado em Controller. O traba-
lho de adicionar o estereótipo@Controller vai ser feito dentro da classe
AnnotatedTypeControllerWrapper,masantesdisso,vamos analisarondeela
estásendousada.
Agrandefacilidadedo mecanismodeextensão daCDIéquecadaeventoobser-
vado,comoo ProcessAnnotatedTypenosdevolveumobjetorelacionado.Nesse
casoestamosexecutandoumcódigo nossoacada AnnotatedTypedescobertopelo
contexto.EsseobjetopodeserrecuperadopelométodogetAnnotatedType,mas
podeseralteradopelométodo setAnnotatedType. Paratodosos outroseven-
tosquepodemosobservarparaconstruirnossasextensõesofuncionamentoé muito
parecido.Recuperamoso objetorecémanalisadoatravésdométodo get,e pode-
mosusarométodo setparatrocaresseobjetoporoutrocomascaracterísticasque
178

## Página 184

CasadoCódigo Capítulo9. ExtensõesCDI
desejamos.Outrométodoquegeralmenteestádisponívelnosobjetos ProcessXYZ
éo veto(),quepodeserutilizadopararemoveresse objetodocontexto,como se
eleestivesseanotadocom @Vetoed.
Ocódigo daclasse AnnotatedTypeControllerWrappertemumfunciona-
mentomuitosimples,comopodemos veraseguir.
class AnnotatedTypeControllerWrapper implements AnnotatedType {
private AnnotatedType wrapped;
AnnotatedTypeControllerWrapper(AnnotatedType original ) {
this.wrapped = original;
}
@Override
public Set<Annotation> getAnnotations() {
Set<Annotation> annotations =
new HashSet<>(wrapped.getAnnotations());
annotations.add(new AnnotationLiteral<Controller>(){});
return annotations;
}
@Override
public Class getJavaClass() {
return wrapped.getJavaClass();
}
...
}
Existemváriosoutrosmétodosqueprecisamserimplementados,mastodos
seguemamesmafilosofiado getJavaClass(), apenasrepassandoainvoca-
ção para o objeto wrapped. Agoraanalisemos o métodoque nos interessa:
getAnnotations(). Vejamoscomoeleésimples,consistindo apenasemadici-
onaraanotação Controllernalistade anotações danossaclasse. Assim,não
fazemosasdemaisanotações pararemdefuncionar, apenasadicionamosumeste-
reótipo.Seaclassejátiverumescopo ouumnome,osdadosdo nossoestereótipo
serásobrescritoporessasanotações específicas.Bemsimplesefuncional.
179

## Página 185

9.5. Extensãonãoportável:eventosassíncronosforadoJavaEE CasadoCódigo
9.5 Extensão n ã o portável: eventos assíncronos
fora d oJa v aEE
A p e s a rdemuitosimplesde usar,omecanismodeextensão nãonosdeixamanipu-
lartodososobjetos quegostaríamos.Nesseexemplovamos manipularosmétodos
observadores,queremos trocaroobservador normalporumqueexecuteemuma
Threadseparadaparapermitiraexecuç ãoassíncrona.
NaCDIpodemosacompanharosmétodosobservadorespresentes naaplicação
daseguinteforma.
public class EventoAssincronoExtension implements Extension {
private Logger logger = LoggerFactory
.getLogger(EventoAssincronoExtension.class);
public void analisaObservers(@Observes ProcessObserverMethod pom) {
ObserverMethod observerMethod = pom.getObserverMethod();
jogger.info("Método {} é um observer" + observerMethod);
}
}
Comovimosaoconstruiraextensão ControllerPorConvensaoExtension,
ocomumétermosummétodo geteum setemcada ProcessXYZdentro
daSPIdaCDI.Porémainterface ProcessObserverMethod não possuium
método setObserverMethod, nosobrigando a utilizarclassesespecíficas do
W e l d ,deixandode terumaextensão portável.Emversõesfuturaspodemos teressa
limitaçãoremovida; porhoraveremoscomo sairdessasituação,edesituações que
podemocorrernonosso diaadiae queaSPInãonosofereçaumasaída.
Aprimeiracoisa quefaremoséobservar seaclassequeimplementaainter -
face ProcessObserverMethodnosofereceessemétodo. Aclasseemquestão
éa org.jboss.weld.bootstrap.events.ProcessObserverMethodImpl,
maselatambémnãoofereceum setObserverMethod.A saídaseráutilizarum
eventodiferente,o AfterBeanDiscovery.
Esseeventoélançadodepois quetodosos beans,etambémosobservadores
foramdescobertose nãoháproblemaem suasdefinições. Entãodepoisdetudo
pronto,vamostentarmudaralgoquenãotivemosaberturaparamudarnomomento
apropriado.Aestrutura danossaextensãoficaráentão daseguinteforma.
180

## Página 186

CasadoCódigo Capítulo9. ExtensõesCDI
public class EventoAssincronoExtension implements Extension {
private Logger logger = LoggerFactory
.getLogger(EventoAssincronoExtension.class);
void afterBeanDiscovery(@Observes AfterBeanDiscovery abd,
BeanManager bm) {
logger.info("Todos os beans já foram lidos");
}
}
Apenastrocamosoeventoqueiremosobservar. Nessetrecho,adicionamos
tambémo javax.enterprise.inject.spi.BeanManager.Enquantoemum
observadordeeventoscomumpodemosreceberqualquer objetocomodependên-
ciadométodo, bastandopara issocolocarmaisparâmetrosalémnoanotadopelo
@Observes;quandoimplementamosumaextensão,oúnico objetoinjetáveléo
BeanManager.Issoporqueométodoseráchamadoantesdocontextoestartermi-
nado,assim não seriapossívelencontrar asdependências.Jáo BeanManageré
umobjetoúnicoecentral naCDI,logo eleexistedesdeoinício dainicializaçãoda
aplicação.
Nessemomento,podemosutilizarosmétododo BeanManagerparaacessar
suasestruturasinternasemodificá-las.Podemosfazer issocomos beansediversos
outroselementosdocontexto, masinfelizmentenãotemosumamaneiradealterar
adefiniçãodeobservadoresdeeventosatravésdessainterface.
Asaídaseráutilizaraimplementaç ãode BeanManager,eentãorecuperara
listadeobservadores.Faremos issodaseguintemaneira.
void afterBeanDiscovery(@Observes AfterBeanDiscovery abd,
BeanManager bm) {
BeanManagerImpl manager = ((BeanManagerProxy) bm).delegate();
List<ObserverMethod<?>> observers = manager.getObservers();
}
Atravésdaclasse org.jboss.weld.manager.BeanManagerImplconse-
guimosacessarométodo getObservers(),e aísimpoderemosprosseguir na
implementaçãodanossaextensão.Porémantesdeavançar,vamosentendermelhor
comoessaextensãoiráfuncionar.
181

## Página 187

9.5. Extensãonãoportável:eventosassíncronosforadoJavaEE CasadoCódigo
Novamenteosobservadoresassíncronos
Jávimossobreobservadoresassíncronosdeeventos naseção7 . 5.Naquela oca-
sião,vimos queparausarafuncionalidadeprecisávamosqueobeanfosseumEJB,
equeométodoestivesseanotadocom @Asynchronous. T a m b é mjávimosque
aCDI não ofereceuma formanativadetermosobservadoresassíncronos, poiso
intuitonãoécompetircomoutrasespecificações. Logo,sequisermosexecutarCDI
foradoservidordeaplicações, semEJBs,precisaremosdeumaextensão quenosofe-
reçaisso.Podemosbuscarumaprontanasreferênciasapresentadasnestecapítulo,
ouentãodesenvolveranossa.
Ointuito danossaimplementaçãonãoécompetircomqualquerextensãode-
senvolvidapororganizações comoA p a c h eouJBoss,esimmostrarcomopodemos
implementarcoisasmuitoúteisquandonãoencontrarmosumaalternativapronta.
Nonossoexemplo,teremosapenasumaanotaçãoJavasimples, @Assincrono,
queserácolocadasobreosmétodosobservadores quedesejamosquesejamexecu-
tadosde formaassíncrona.Adiferen çaparaaanotação @Asynchronous,équea
nossapodesercolocadaemum beancomum,enãoapenasemEJBs.
ComoaSPIdaCDInãoprevêessetipodemanipulaçãodeobservadores, nãohá
umaformasimplesdemanipularmosessesmétodos.Precisaremosdeumatarefaum
poucomaistrabalhosa-masnemtanto-e queenvolvemaisalgumasclassesespe-
cíficasdoW e l d .Comoestamosusandoalgoespecíficodaimplementação,podemos
teralterações dessasclassesnofuturo,poressemotivoomelhoréseriausarmossó
classesdaespecificação.Masjávimosquenonosso exemplonãoserápossível.
Vejamosentãocomo trocaro ObserverMethodpadrão,porum w r a p p e rque
faça-oexecutaremuma Threadseparada.
void afterBeanDiscovery(@Observes AfterBeanDiscovery abd,
BeanManager bm) {
BeanManagerImpl manager = ((BeanManagerProxy) bm).delegate();
List<ObserverMethod<?>> observers = manager.getObservers();
for (ObserverMethod<?> observerMethod : observers) {
ObserverMethodImpl observerMethodImpl =
(ObserverMethodImpl) observerMethod;
MethodInjectionPoint methodInjectionPoint =
observerMethodImpl.getMethod();
182

## Página 188

CasadoCódigo Capítulo9. ExtensõesCDI
AnnotatedMethod annotatedMethod =
methodInjectionPoint.getAnnotated();
Method method = annotatedMethod.getJavaMember();
if (method.isAnnotationPresent(Assincrono.class)) {
//aqui chegamos ao ponto que desejávamos!
}
}
}
Precisamos usar diversas classes para poder chegar até o
java.lang.reflect.Method que representa o método observador,
para então verificar se ele está anotado com @Assincrono, através de
if(method.isAnnotationPresent(Assincrono.class)).
Depoisdetudo isso,conseguimosidentificaro ObserverMethodquedeseja-
mostrocardentrodocontextoCDI. Paraissocriaremosuma classe w r a p p e rassim
comofizemosnaextensão ControllerPorConvensaoExtension.Eentão rea-
lizaremos,dentrodo ifanterior,atrocadeum objetopelooutro.
if (method.isAnnotationPresent(Assincrono.class)) {
ObserverMethod original = observerMethodImpl;
ObserverMethod observerMethodWrapper =
new ObserverMethodWrapper(original);
observers.remove(original);
abd.addObserverMethod(observerMethodWrapper);
}
A p ó sinstanciarmos nossa classe ObserverMethodWrapper, re-
movemos a original da lista de observers e adicionamos o obser-
vador novo em seu lugar. Adicionamos o novo usando o método
AfterBeanDiscovery.addObserverMethod(ObserverMethod). Pode-
mosperceberqueométododeadicionaroobservadorexiste,o quenão existeé
umaformapadrãode trocaroobjetoantigopelonovo. Optamospelométodo
porqueelefazpartedaSPI,entãopreferimosutilizá-lo,senãoadicionaríamos ele
diretonalista observers,queéumareferênciadedentrodocontextoCDI.
183

## Página 189

9.5. Extensãonãoportável:eventosassíncronosforadoJavaEE CasadoCódigo
Faltaagoraocódigo daclasse ObserverMethodWrapper,quetrocaráacha-
madaoriginalporumaquelançauma nova Thread.
import java.util.concurrent.ExecutorService;
...
public class ObserverMethodWrapper<T> implements ObserverMethod<T> {
private Logger logger = LoggerFactory
.getLogger(ObserverMethodWrapper.class);
private ObserverMethod delegate;
private ExecutorService executor;
public ObserverMethodWrapper(ObserverMethod delegate) {
this.delegate = delegate;
}
...
}
Aindanão vimostodososmétodos danossaclasse,masaestruturabásicajános
fornecealgumainformação. Percebaautilizaç ão daclasse ExecutorService,
queserveparadispararmosexecuções de Runnablesem novas Threads.V a m o s
assumirqueconseguiremosumainstânciadessainterfaceeprosseguir. Depoisvol-
taremoseanalisaremosumpouco sobrecomoconseguimosessainstância.
Agrande maioriadosmétodossãoapenasdelegações dechamadasdemétodo
paraoobjeto delegate.
@Override
public Class getBeanClass() {
return delegate.getBeanClass();
}
@Override
public Type getObservedType() {
return delegate.getObservedType();
}
//delegação dos demais métodos para o delegate
@Override
184

## Página 190

CasadoCódigo Capítulo9. ExtensõesCDI
public void notify(Object event) {
getExecutor().execute(new ExecuteEventRunnable(delegate, event));
}
Ométodomaisinteressantenesseexemploéo notify(Object).Esseéomé-
todoqueéresponsávelpordispararanotificaçãoparaoobservador.O quefazemos
aquié,emvezdesomentedelegara chamadaparaoobjeto delegate,o queaca-
barianão surtindonenhumaalteraç ão nocomportamentopadrãodoobservador,
chamaro delegate.notify(event)dentrodeuma nova Thread.
O método getExecutor() nos devolve uma instância de
ExecutorService, e sabendoque esse objeto consegue disparar a execução
deum Runnableemuma nova Thread,agoraprecisamosveraimplementação
daclasse ExecuteEventRunnable.
class ExecuteEventRunnable implements Runnable {
private ObserverMethod delegate;
private Object event;
public ExecuteEventRunnable(ObserverMethod delegate, Object event) {
this.delegate = delegate;
this.event = event;
}
@Override
public void run() {
delegate.notify(event);
}
}
Simplesmente chamamos o observador original, representadopelo objeto
delegate, dentro de um Runnable. Sabendo um pouco do funciona-
mentode Threads dentro do Java, sabemosquebasta fazeralgocomo new
Thread(Runnable).start() para executar o Runnable em umanova
Thread,realmenteébemsimples,mascomoestamosrodandonossocódigodentro
deumservidor,essa nãoéumaabordagemrecomendada.
Tradicionalmente,autilizaçãode múltiplasthreadsdentrodoJavaEEébemdi-
ferentedo seuusonoJavaSE.Enquantoemumaaplicaç ãodesktoppodemos usar
new Thread comocitado,noJavaEEa formadefazer issoeradispararumamen-
sagemJMSparaqueum Message-Driven Beanaprocessassede formaassíncrona.
185

## Página 191

9.5. Extensãonãoportável:eventosassíncronosforadoJavaEE CasadoCódigo
NoJavaEE6 issofoisimplificadocomaadiç ãodaanotação @Asynchronousque
jávimos.Issofacilitoumuitoouso,mascomoestamosconstruindouma alternativa
justamenteaesse mecanismo,precisamosdeoutraalternativa.
Felizmente, oJava EE 7 adicionou o umanova especificação, a "Con-
currency Utilities for J a v aEE” (JSR-236) [?]. Essa especificação simples-
mente nosoferece uma APIJava EE compatívelcom a API JavaSE disponí-
vel desde oJava 5. Enquanto no SE essas funcionalidades estãono pacote
java.util.concurrent, no EE 7 ,essa nova especificação definiu o pacote
javax.enterprise.concurrent. Deformaparecida,noJSEtemosprincipal-
menteasinterfaces ExecutorServicee ThreadFactory,jánoJEEtemos as
respectivasinterfaces ManagedExecutorServicee ManagedThreadFactory.
A p ó sessebreveentendimentodosignificadodessasinterfaces,vejamosaim-
plementaçãodométodo getExecutor(),queéondebuscaremosasinstâncias
corretas.
private ExecutorService getExecutor() {
if (executor != null) {
return executor;
}
try {
Context ctx = new InitialContext();
executor = (ManagedExecutorService )
ctx.lookup("java:comp/env/concurrent/ManagedExecutorService");
} catch (Exception e) {
logger.error("Erro ao buscar o "
+ " ManagedExecutorService (JSR 236)" , e);
logger.warn("Usando implementação simples " +
" de newCachedThreadPool()" );
executor = Executors.newCachedThreadPool();
}
return executor;
}
Semprebuscaremosno contextoda aplicação uma instância gerenciada de
ExecutorService,poiselacertamenteestaráintegradaao poolde Threadsque
186

## Página 192

CasadoCódigo Capítulo9. ExtensõesCDI
oservidorjápossui,enãocorreremosoriscodeinterferirnegativamente nociclode
vidadaaplicaçãoedoservidor, evitandoqualquervazamentode memóriaoucoisas
dogênero.Paraconseguirmosrecuperaresse objeto,adicionamosno web.xmlda
aplicaçãooseguinteconteúdo.
<resource-env-ref>
<resource-env-ref-name>
concurrent/ManagedExecutorService
</resource-env-ref-name>
<resource-env-ref-type>
javax.enterprise.concurrent.ManagedExecutorService
</resource-env-ref-type>
</resource-env-ref>
Precisamosdessaconfiguração porquenão existeumcaminhopadrãodefi-
nidopararecuperarmoso ManagedExecutorService. Omesmovaleparao
ManagedThreadFactory.
Para terminar nossa análise,precisamos ter bastante atenção no con-
teúdo do catch no método getExecutor(). Caso não consiga-
mos recuperar o ManagedExecutorService, utilizaremos o método
Executors.newCachedThreadPool(), porémregistraremos um aviso no
logparaqueissosejaaveriguado. Podeserqueaconfiguraçãodo nomeJNDI
nãoestejacorreta, maspodeserquenãoestejadisponívelumaimplementaç ãode
ExecutorService. A p e s a rdessaimplementação serpartedoJavaEE,é bem
possívelqueembreveconseguiremosutilizá-ladentrodeservletcontainers.
Esperoquenestecapítulotenhaficadoclaroavantagemdetermosextensões
portáveis,masquetambémtenhaservidorparaindicarumcaminho quandoessa
nãoforumapossibilidade,nocasodasextensões nãoportáveis.Comoacabamosde
falardeservletcontainers,passaremos agoraparaoúltimocapítulo,ondeveremos
autilizaçãodeCDIemambientes nãoJavaEE,dentreelesoservletcontainer.
187

## Página 194

Capítulo10
ExecutandoCDIemdiferentes
ambientes
ACDIéumaespecificaç ãopensada paraoJavaEE,mascomojáadiantamosemdi-
versosmomentos,épossívelexecutá-loforadesseambiente.Nessecapítuloveremos
comoexecutarCDIem servlet containers,a partirdeuma classe mainetambémem
testesdeintegração.
Nossofoconessesexemplosvaideixarde serafuncionalidade daCDI,poisjá
vimosbastantesobreissodurantetodoolivro. Agorairemosfocarnaconfiguração
necessáriaparaexecutarnesseambientes.Essassãoconfigurações específicaspara
oW e l d ,implementaçãodereferênciadaCDI,poisaespecificaçãonãoabordaesses
ambientes.

## Página 195

10.1.ExecutandoCDIemservletcontainers CasadoCódigo
10.1 Executando CDI em servlet containers
Aoexecutarumaaplicaç ãodentrodeumservletcontainer,temos quelembrardas
diversasfuncionalidades quenãoestarãodisponíveis,comocontrole automáticode
transações,eventosassíncronos,mensageria,dentreoutras. Porémissomuitasvezes
nãoéumproblema,umavezquejásabemoscomoimplementar,compoucoesfor ço,
essasfuncionalidades, sejaviaextensãoousimplesmenteadicionandoum jarcom
asfuncionalidadesimplementadas.
Nessaseçãoiremosutilizarcomoreferênciao tomcat,masnadocumentaçãodo
W e l dencontramoscomoprocederaconfiguraç ão paraexecutarnojettytambém.
Comoessesservidores nãotemaobrigaçãode proverosserviçosdaCDI,teremos
que,pelaprimeiravez,fazerodownloaddo W e l d .Obviamenteépossívelutilizar
gerenciadoresdedependênciacomo mavenouivy,masportermosqueadicionar
basicamentedoisjars,procederemosdaformatradicionalmesmo.
O download doW e l dpode ser feito no seguinte endereço: http://www.
seamframework.org/Weld/Downloads. A p ó sdescompactar oarquivo baixado,
precisamos deapenas dois jars que podem ser encontrados dentroda pasta
artifacts, são eles cdi-api.jar e weld-servlet.jar. Bastacriarmos
umprojetowebnaIDEdanossapreferênciaecolocaresses jarsdentrodapasta
WEB-INF/lib. Precisamoslembrartambém,assimcomo jáfazíamosnosproje-
tosJavaEE,édecolocaro arquivo beans.xml,mesmovazio,dentro dapasta
WEB-INF.
Apartirdessemomentojáestamoscomo setupbásicofeito,temosentão que
partirparaasconfigurações propriamenteditas. Nãosepreocupecomapossibi-
lidadedeesqueceralgumdetalhe, poisvocêpodeverificarseseu projetopossui
todasasconfigurações comparando-ocomo projetodisponívelnogithub: https:
//github.com/gscordeiro/cdi-tomcat.
U mobjetomuitoimportanteparaaCDIéo BeanManager.Esseobjetoésem-
prenecessárioealcançávelviaJNDIemambiente JavaEE.Porémcomoestamos
usandoumservletcontainer,vamos precisarfazerumaconfiguraçãoparaadicionar
esseobjetodentrodocontextoJNDI daaplicação. Notomcat,essaconfiguraçãoé
feitadentrodo arquivo META-INF/context.xml,cujoconteúdovemosaseguir.
<Context>
<Resource name="BeanManager" auth="Container"
type="javax.enterprise.inject.spi.BeanManager"
factory="org.jboss.weld.resources.ManagerObjectFactory" />
</Context>
190

## Página 196

CasadoCódigo Capítulo10.ExecutandoCDIemdiferentesambientes
Paracompletaraconfiguraç ãodo BeanManager, precisamosadicionarno
web.xmlumaentradaquecriaumareferênciacomonome "BeanManager"para
otipo javax.enterprise.inject.spi.BeanManager.
<resource-env-ref>
<resource-env-ref-name>BeanManager</resource-env-ref-name>
<resource-env-ref-type>
javax.enterprise.inject.spi.BeanManager
</resource-env-ref-type>
</resource-env-ref>
Aoatribuirmosesse nomeao BeanManager,eleficadisponível nocontexto
JNDIcomo nome "java:comp/env/BeanManager".Nósnãoprecisamosusar
diretamenteessenome,masomódulo servletdoW e l dvaiprecisar.
AgoraqueoJNDIestá pronto,precisamoscolocar maisumaconfiguração no
web.xml,queéoListenerdoW e l dqueirásubirocontextoCDIe tambéminteragir
comasrequisições.
<listener>
<listener-class>
org.jboss.weld.environment.servlet.Listener
</listener-class>
</listener>
Agorasimterminamos, nossaaplicaçãoestáprontaparautilizarasfuncionali-
dadesdaCDI.Apenasparatestarmos,vamoscriarumaservlet quefazainje çãode
uma CalculadoraSalarios. A p e s a rdecontinuarmos nomesmoexemploda
aplicaçãoJavaEE,aquiiremos terimplementaçõesbem maissimples,poisointuito
éapenastestaro setupdoambiente.
@WebServlet("/calculadoraSalario")
public class CalculadoraSalarioServlet extends HttpServlet {
@Inject
private CalculadoraSalarios calculadoraSalarios;
@Override
protected void doPost(HttpServletRequest req,
HttpServletResponse resp)
throws ServletException, IOException {
191

## Página 197

10.1.ExecutandoCDIemservletcontainers CasadoCódigo
Funcionario funcionario = new Funcionario(
req.getParameter("funcionario"),
Double.parseDouble(req.getParameter("salario")));
double salario =
calculadoraSalarios.calculaSalario(funcionario);
System.out.printf("Salário do(a) %s é %.2f" ,
funcionario.getNome(),
salario);
}
}
Ousodo System.outéapenasparasimplificaroexemplo, noprojetodo
githubtemosumsimples formuláriodeentradadedadoseuma páginaqueexibeo
resultado.
Aimplementaçãoda CalculadoraSalariosaquinesseprojetoébemmais
simples,apenasadiciona10%(dezporcento)ao saláriobasedofuncionário.
public class CalculadoraSalarios {
@Inject
private Event<Funcionario> calculoSalarioEvent;
public double calculaSalario(Funcionario funcionario){
calculoSalarioEvent.fire(funcionario);
return funcionario.getSalarioBase() * 1.1;
}
}
Temostambémolançamentodeumeventosimples,queserveparaindicarqueo
saláriodofuncionáriofoicalculado.Comojávimosesseconteúdo,aqui nãoutiliza-
mosqualquerqualificador;queremos apenasverqueoseventostambémfuncionam
noservletcontainercomo noapplicationserver.
Porfimtemosoobservadordo evento,nosmesmosmoldes quejávimosantes.
public class ObservadorCalculadora {
public void escutaCalculoSalario(@Observes Funcionario funcionario){
System.out.printf("O salário do(a) %s "
+ " acabou de ser calculado\n" , funcionario.getNome());
192

## Página 198

CasadoCódigo Capítulo10.ExecutandoCDIemdiferentesambientes
}
}
Essaseçãofoirelativamentecurtapoisjávimostodooconteúdo,etambémpor-
queaconfiguraçãoemsi tambémnão éextensa. Entãoseemnossaorganização
utilizamosservletcontainersem vezdeservidoresdeaplicaç ãoJavaEE,nãoprecisa-
mosabrirmãodasgrandesvantagensdaCDI.T o m c a teJettydiferembempoucoem
suaconfiguração.Comooarquivo web.xmlfazpartedaespecificaçãodeservlets,a
únicamudançaseránoarquivo META-INF/context.xmldotomcat,quenojetty
sechama WEB-INF/jetty-env.xmletemoseguinteconteúdo.
<!DOCTYPE Configure PUBLIC "-//Mort Bay Consulting//DTD Configure//EN"
"http://www.eclipse.org/jetty/configure.dtd">
<Configure id="webAppCtx"
class="org.eclipse.jetty.webapp.WebAppContext">
<New id="BeanManager" class="org.eclipse.jetty.plus.jndi.Resource">
<Arg> <Ref id="webAppCtx"/> </Arg>
<Arg>BeanManager</Arg>
<Arg>
<New class="javax.naming.Reference">
<Arg>javax.enterprise.inject.spi.BeanManager</Arg>
<Arg>org.jboss.weld.resources.ManagerObjectFactory</Arg>
<Arg/>
</New>
</Arg>
</New>
</Configure>
10.2 Executando CDI a partir de u m a classe main
Assimcomoprecisamosfazer naseçãoanterior,precisamos baixaroW e l dnapá-
ginadoprojeto: http://www.seamframework.org/Weld/Downloads. Játendoos
jarsbaixados,precisamoscriarum novoprojetoJavasimpleseadicionaros jars
cdi-api.jare weld-se.jarnoseuclasspath. V o c êtambémpodeverificar
seuprojetocomparandocomodisponível nogithub:https://github.com/gscordeiro/
cdi-desktop.
Nãoseránecessáriocriarconfigurações parausarW e l ddentrodanossa main,
bastafazermosainicializaç ãodocontexto manualmente.
193

## Página 199

10.2.ExecutandoCDIa partirdeuma classemain CasadoCódigo
public class CalculadoraMain {
public static void main(String[] args) {
Weld weld = new Weld();
WeldContainer container = weld.initialize();
CalculadoraSalarios calculadoraSalarios = container.instance()
.select(CalculadoraSalarios.class).get();
Funcionario funcionario = new Funcionario("Fulano", 5000.0);
double salario =
calculadoraSalarios.calculaSalario(funcionario);
System.out.printf("Salário calculado do %s é %.2f\n",
funcionario.getNome(), salario);
weld.shutdown();
}
}
U m alimitaçãodo W e l demaplicaçãoJSEestánosescoposdisponíveis:aplicação,
dependenteesingleton, jáquenãoexisterequisiçãoesessão foradeumservidor.
A p e s a rdena mainnãotermosusado @Inject,utilizamosuma formadeloo-
kupprogramático.Masainje çãocontinuafuncionando, bastavermosocódigo da
CalculadoraSalarios.
public class CalculadoraSalarios {
@Inject
private Event<Funcionario> calculoSalarioEvent;
public double calculaSalario(Funcionario funcionario){
calculoSalarioEvent.fire(funcionario);
return funcionario.getSalarioBase() * 1.1;
}
}
Éexatamenteo mesmocódigoqueutilizamosnaaplicação cdi-tomcat.
194

## Página 200

CasadoCódigo Capítulo10.ExecutandoCDIemdiferentesambientes
Podemos tambémfugir da subida manual do contexto doW e l d ,bas-
tando para isso usaruma classe main disponível dentro do weld-se.jar:
org.jboss.weld.environment.se.StartMain.Aosubirocontexto,o W e l d
lançaoevento ContainerInitialized,enossa“falsamain”observaesseevento.
import org.jboss.weld.environment.se.bindings.Parameters;
import org.jboss.weld.environment.se.events.ContainerInitialized;
@Singleton
public class CalculadoraFalsaMain {
@Inject
private CalculadoraSalarios calculadoraSalarios;
public void printHello(@Observes ContainerInitialized event ,
@Parameters List<String> parameters) {
Funcionario funcionario = new Funcionario("Fulano", 6000.0);
double salario =
calculadoraSalarios.calculaSalario(funcionario);
System.out.printf("Salário calculado do %s é %.2f\n",
funcionario.getNome(), salario);
}
}
Agora sim, nossa “falsamain”consegue trabalhar com injeção da
CalculadoraSalarios. Além disso,usamos o qualificador @Parameters
parasolicitaraocontainerainje çãodosparâmetros da mainoriginal; ofamoso
String[] args.
Assimcomo noprojeto cdi-tomcat,oseventoscontinuamfuncionando, as-
simcomointerceptadores,decoradorese asoutrasfuncionalidadesdaCDI.
10.3 E co mo testar u m a aplicação CDI?
JánoiníciodolivromostramoscomoaCDI nosdeixalivresparaconstruirprojetos
declassestestáveis.Issoparatestesdeunidade resolveaquestão, masprecismos
tambémlidarcom testesdeintegraçãoedesistema. Nossofoconessaseçãoestará
195

## Página 201

10.3. EcomotestarumaaplicaçãoCDI? CasadoCódigo
nostestesdeintegração,poiséondeaCDIatua,fazendoainje çãodasdependências,
decorandoeinterceptando asinvocações,alémé clarodeeventose outrostópicos
quejávimos.
Atualmente,aferramentade automaçãode testesdeintegraçãomaisutilizadano
JavaEEéoArquillian(http://arquillian.org/). Elenospermite,dedentrodo nosso
casodeteste,subirumcontextodeCDI paraqueconsigamosexecutar nossoteste
juntocominje çãodedependência,controlede transações,etudo maisquesefizer
necessárioparanossostestesreproduziremsituações reaisdaaplicação.
UmpoucodeArquillian
Paraconstruirnossos testesdeintegraçãocomArquillian,precisamosentender
comoelesfuncionarãocomaferramenta. Paraissovamosfazerumparalelocomo
processomanualdeconstruçãodaaplicação,deployetestes.
Quandoestamosdesenvolvendo nossaaplicação,colocamos todasclasses ear-
quivosdeconfiguraç ãonecessáriosnoslocaiscorretos,emseguidafazemosoem-
pacotamentodaaplicação. Esseempacotamentopodeserumarquivojar,warou
ear.MuitasvezesaIDEescondeesseprocessodenós,fazendooempacotamento
eodeployeainicializaç ãodoservidorde formaautomáticaquandoexecutamosa
ação “Executar”.Porémtemosqueteremmentequetodosesses passosprecisam
acontecerparanossaaplicaçãopossasertestada.
Parafazemoempacotamento daaplicaçãoa sertestada,utilizamosoShrink-
W r a p(http://www.jboss.org/shrinkwrap),queéumaferramentadecriaç ãoprogra-
máticadepacotesjava.Veremos napráticacomoutilizaressaferramenta, quenos
ofereceumaAPIfluente muitosimplesde usar.
A p ó soempacotamento,precisamosfazerodeploydessepacote. Aquientraum
outroaspectomuitointeressantedoArquillian, quesãoos container adapters. T e -
mosbasicamentetrêstiposde adapters:Embedded, ManagedeRemote.Alémdisso
temosadaptersparadiferentescontainersde cadaumdessestipos.
Porexemplo,analisandoGlassFisheJBoss,vemos quetemosos trêstiposde
adaptadordeGlassFish3.1(masqueexecutatambémoGlassFish4);jáparaoJBoss
7 . 1temosapenasostiposManagedeRemote.
Adiferenciaçãoentreesses tiposésimples:
•Embedded:Nessetipodeadaptador,oArquillian sobeumainstânciadocon-
tainer,sejaeleGlassFish,JBoss,outroservidorouatémesmoumcontainer
sócomo W e l demexecução,tudo issodedentrodo próprioteste.Aquinão
196

## Página 202

CasadoCódigo Capítulo10.ExecutandoCDIemdiferentesambientes
énecessáriobaixaroservidoreinstalar(descompactar) nanossamáquina,
podemosdeixaroArquillianfazer todootrabalho.Porissoessetipodeadap-
tadoréchamado“embarcado”,poiselesobededentrodo próprioteste.
•Managed:Nessetipodeadaptador,oArquillianumaumainstalaç ãodocon-
tainerexistenteexternamente, maséelequemgerenciaa subidaeadescida
docontainer.
•Remote:Jánesteúltimotipodeadaptador,oArquillianfaz usodeumains-
tânciajáexistenteeemexecuç ãodecontainer. Ouseja,oservidor jádeveestar
rodandoparaqueodeploydo nossopacotesejarealizado.
Emtodosesses tiposdeadaptadores,oArquillianfazodeploy,executaostestes,
edepoisfazoundeploydopacote. Nosdoisprimeirostipos, no before class dos
nossostestesoArquillian tambémsobeocontainere no after class baixaesse
containerde formaautomática.JáotipoRemoteéomaiscomumquandotempos
umservidorvoltado paraostestes,ouquandotemosmuitostestesegostaríamosde
subiroservidorumaúnica vez.Nessecasopodemosfazerum scriptquesubaedes ça
oservidor antesedepoisdostestes. Nonossoexemplofaremos usodoadaptador
GlassFishEmbedded.
Configurandoasdependências
AmontagemdoambienteArquilliannãoémuitosimples,envolvemuitasdepen-
dências,assim,édifícilconfigurá-losemoauxíliodeferramentascomoo mavenouo
ivy.Porseraformamaiscomum,econsequentemente maisfácildeencontrarexem-
plos,utilizaremosomaven. Comooarquivo pom.xmlcostumaverextenso,vere-
mosapenaspartesdeleaqui, masseuconteúdocompletoestádisponívelnogithub:
https://github.com/gscordeiro/cdi-arquillian.
Criamosumnovoprojetocomsuporteaomavenparacolocarnossostestes. Essa
separaçãotemsomenteointuitodedeixaro projetoinicialmaisleve,senãoenquanto
estivéssemosadicionandopequenasfuncionalidadeseexecutandoo projetonoser-
vidor,teríamoso mavenrodandotodaabateriadetestes,subindoedescendoocon-
textodoglassfishtodahora,deixandooprocesso todomaislento.Obviamenteissoé
configurável,masalémdesimplificaroprocessocomoum todo,oprojetoapartado
servecomoumareferênciarápidaparavocêquejátemseusprojetosCDIedeseja
adicionarsomenteostestes. Ouseja,aseparaç ãoéapenasdidática,emumprojeto
realostestesficamjuntocomseuprojeto.
197

## Página 203

10.3. EcomotestarumaaplicaçãoCDI? CasadoCódigo
Paramantermosofoco,vamosignorar,porhora,configurações comunsdopro-
jetonomaven,comodependênciasdeJavaEEeJUnit.
<dependencyManagement>
<dependencies>
<dependency>
<groupId>org.jboss.arquillian</groupId>
<artifactId>arquillian-bom</artifactId>
<version>1.1.1.Final</version>
<scope>import</scope>
<type>pom</type>
</dependency>
</dependencies>
</dependencyManagement>
<dependencies>
<dependency>
<groupId>org.glassfish.main.extras</groupId>
<artifactId>glassfish-embedded-all</artifactId>
<version>4.0</version>
<scope>provided</scope>
</dependency>
<dependency>
<groupId>org.jboss.arquillian.container</groupId>
<artifactId>arquillian-glassfish-embedded-3.1</artifactId>
<version>1.0.0.CR4</version>
<scope>test</scope>
</dependency>
<dependency>
<groupId>org.jboss.arquillian.junit</groupId>
<artifactId>arquillian-junit-container</artifactId>
<version>1.1.0.Final</version>
<scope>test</scope>
</dependency>
</dependencies>
Alémdasdependênciasbásicas,comoJavaEEeJUnit, tambémdeixaremospara
logomaisaconfiguraçãodepersistênciadoarquillian. Agoravamosvercomorea-
lizarum testesimplesusandooarquillian.
@RunWith(Arquillian.class)
public class CalculadoraSalariosTest {
198

## Página 204

CasadoCódigo Capítulo10.ExecutandoCDIemdiferentesambientes
@Deployment
public static JavaArchive createDeployment() {
return ShrinkWrap.create(JavaArchive.class)
.addClass(Funcionario.class)
.addClass(CalculadoraSalarios.class)
.addClass(CalculadoraSalariosDezPorcento.class)
.addAsManifestResource(EmptyAsset.INSTANCE, "beans.xml");
}
...
}
Aquipodemosveraestruturabásica daclassedetestes. U s a m o saanotação
@org.junit.runner.RunWithdoJUnite passamosaoArquillianogerencia-
mentodociclode vidadoteste,permitindoàferramenta subiredescerocontainer
quandonecessário.
O empacotamento doqueserá testado éfeitoatravés de um método está-
ticoquedevolveopacotemontadoprogramaticamente. Nonossoexemploéum
org.jboss.shrinkwrap.api.spec.JavaArchive. Pormaisquenossaapli-
caçãosejaweb,comovamostestarapenasacalculadora,nãohavendoqualquertela,
podemosfazer nessemomentoumjaremvezdeumwar.
Paramontarnosso pacotevamosadicionando asclasses,e tambémosrecursos
quenecessitarmos. Percebacomocriamosum arquivochamado "beans.xml",
em branco ( EmptyAsset.INSTANCE), e dentro do “manifest resource” (
addAsManifestResource). Esseúltimométodoémuitointeressantepoissabe
exatamenteolocal ondeoarquivodevesercolocado.Seestivéssemoscriandoum
WarArchiveteríamosaindaummétodo addAsWebInfResourceparacolocaro
recursotambémnolocalcorreto. Muitomaissimplesdo queficarmosnospreocu-
pandocomaspastasearquivos "build.xml"doAnt.
Maisumfator importanteanotarmoséquecriamossemprepacotessomente
comonecessário paraexecutaro testeatual. Então senossaaplicaçãoégrande,
cheiadeEJBs,páginasweb,ediversasbibliotecas,aaplicaç ãodemoramaisparasubir.
Mascriandoumpacotecomoessedo testequetemapenastrêsclasses,certamente
otempodesubiredesceropacoteseráincomparavelmente menor.
V a m o sagoraretornaràclasse CalculadoraSalariosTest,ondevamostes-
tarnossacalculadora.
199

## Página 205

10.3. EcomotestarumaaplicaçãoCDI? CasadoCódigo
@Deployment
public static JavaArchive createDeployment() { ... }
@Inject
private CalculadoraSalarios calculadoraSalarios;
@Test
public void deveAumentarSalarioBaseEmDezPorcento(){
Funcionario funcionario =
new Funcionario("Fulano", 4000.0, Escolaridade.MEDIO);
double salario = calculadoraSalarios.calculaSalario(funcionario);
assertEquals(4400.0, salario, 0.001);
}
Essa classe Funcionario e a classe CalculadoraSalarios são
versões simplificadas das classes que jávimos. Isso novamente apenas
para deixar oprojeto cdi-arquillian mais simples. A implementação
CalculadoraSalariosDezPorcento,porexemplo,apenasadiciona10%(dez
porcento)aovalordo saláriobasedo Funcionario.
Testandoambiguidade
Podemosfazer maisumtesteinteressanteparaverificarmosaambiguidadede
dependências.
@RunWith(Arquillian.class)
public class AmbiguidadeTest {
@Deployment
public static JavaArchive createDeployment() {
return ShrinkWrap.create(JavaArchive.class)
.addClass(CalculadoraSalarios.class)
.addClass(CalculadoraSalariosDezPorcento.class)
.addClass(CalculadoraSalariosVintePorcento.class)
.addAsManifestResource(EmptyAsset.INSTANCE, "beans.xml");
}
}
Nesseexemplo,montamosumpacotecomainterface CalculadoraSalarios
200

## Página 206

CasadoCódigo Capítulo10.ExecutandoCDIemdiferentesambientes
esuasduasimplementações. Agoravamosinjetarumainstânciadessainterface uti-
lizando javax.enterprise.inject.Instance,eemseguidavamosverificar
aambiguidadeedepoisresolvê-la.
@Deployment
public static JavaArchive createDeployment() { ... }
@Inject
private Instance<CalculadoraSalarios> calculadoraSalarios;
@Test
public void deveApresentarAmbiguidade(){
assertTrue(calculadoraSalarios.isAmbiguous());
}
@Test
public void naoDeveApresentarAmbiguidade(){
Instance<? extends CalculadoraSalarios> calculadoraEspecifica =
calculadoraSalarios.select(
CalculadoraSalariosVintePorcento.class);
assertFalse(calculadoraEspecifica.isAmbiguous());
}
A t éaqui,poderíamosterutilizadoapenasoadaptadordo próprioW e l dnolugar
determosutilizadoodo GlassFish.Porémagorairemosexplorarexemplosenvol-
vendopersistência,enessecasoprecisamosdeuma soluçãomaiscompleta.
10.4 Desenvolvendo testes de integração co m p e r-
sistência
Comoresultadodaseçãoanterior, játemosoambientede testesfuncionandocom
oarquillian. Agoravamosexpandirnossoambienteparatermossuporteàextensão
depersistência.Precisamosparaissoadicionaroseguinte trechodecódigo naseção
<dependencies>do pom.xml.
<dependencies>
<dependency>
<groupId>org.jboss.arquillian.extension</groupId>
<artifactId>arquillian-persistence-impl</artifactId>
201

## Página 207

10.4. Desenvolvendotestesdeintegraçãocompersistência CasadoCódigo
<version>1.0.0.Alpha5</version>
<scope>test</scope>
</dependency>
</dependencies>
Agoraconseguimosfacilmentecontrolar transaçãodentrodostestes,econse-
guimostambémutilizaroDBUnit(http://dbunit.sourceforge.net).É muitapossibi-
lidadejunta,masvejamoscomoautilizaç ãoésimples.Parainiciar,faremosum teste
bemsimplesdeinser çãodefuncionáriosnobancodedados.Novamenteveremoso
códigoem partespara irmosanalisandocadaparte.
@RunWith(Arquillian.class)
public class FuncionarioPersistenceTest {
@Deployment
public static JavaArchive createDeployment() {
return ShrinkWrap.create(JavaArchive.class)
.addClass(Funcionario.class)
.addAsManifestResource(
new File("src/test/resources/META-INF/persistence-teste.xml"),
"persistence.xml")
.addAsManifestResource(EmptyAsset.INSTANCE, "beans.xml");
}
...
}
Agora nosso pacote tem somente uma classe, a entidade Funcionario,
e temosmais dois recursos: o primeiro é oarquivo persistence.xml e
o outro é o beans.xml. Jávimos que este últimoserá umarquivo vazio,
mas o persistence ébastante interessante, pois criamos umarquivo chamado
persistence-teste.xml,comumaconfiguraç ãode bancodedadosespecífica
paraoambientedetestes, eaoadicioná-lo nopacotemudamos seunomepara
persistence.xml,queéoesperadopelocontainer.
Nessearquivo,configuramos omecanismode persistênciaparaconstruir o
bancoquandoocontexto subireparaapagarobancoquandoostestestermina-
rem.Dessaforma,acadatesteobancoseráreconstruído,entãonãoprecisamosnos
preocuparemapagarosdados manualmenteentreumaexecuç ãoe outradoteste.
NessemomentotemosumpacoteCDI quepossuiafuncionalidadedepersis-
tênciaativada. Eagorapodemosnovamenteencararo própriotestecomosefosse
202

## Página 208

CasadoCódigo Capítulo10.ExecutandoCDIemdiferentesambientes
umbeangerenciadopelaCDI,injetandoinclusiveo EntityManager.
@Deployment
public static JavaArchive createDeployment() { ... }
@PersistenceContext(unitName = "livroCdiPU")
EntityManager em;
@Test
@Transactional
public void deveInserir2Funcionarios() {
TypedQuery<Funcionario> query =
em.createQuery("select f from Funcionario f", Funcionario.class);
assertEquals(0, query.getResultList().size());
Funcionario funcionario1 =
new Funcionario("Xico", 2000.0, Escolaridade.FUNDAMENTAL);
Funcionario funcionario2 =
new Funcionario("Maria", 4000.0, Escolaridade.MEDIO);
assertEquals(null, funcionario1.getId());
assertEquals(null, funcionario2.getId());
em.persist(funcionario1);
em.persist(funcionario2);
assertEquals(Integer.valueOf(1), funcionario1.getId());
assertEquals(Integer.valueOf(2), funcionario2.getId());
assertEquals(2, query.getResultList().size());
}
Esse teste nos mostra como proceder no teste de persistência.
Com a extensão de persistência do arquillian, temos acesso àanotação
@org.jboss.arquillian.persistence.Transactional. Anotando o
testecomela,esteficatransacional, nospermitindosalvarobjetosnobancocomo
seestivéssemosdentrodeumEJB. U m aoutrapráticaéanotarométododetestes,
outodaaclasse,com @Transactional(TransactionMode.ROLLBACK),para
queosdadosnãosejampersistidos,gerandosempreum r o l l b a c knatransaçãoatual.
203

## Página 209

10.4. Desenvolvendotestesdeintegraçãocompersistência CasadoCódigo
Assimosdiversosmétodos nãoinfluenciamumnooutro.
OusodoDBUnitdeformamuitosimples
Outraferramentaquenosauxiliaacriar testesenvolvendoa camadadepersis-
tência,éoDBUnit.Comojáadicionamosaextensãodepersistênciadoarquillian,o
DBUnitjáestádisponível.
ODBUnittrabalhabasicamentemontandoumamassadedados antesdecada
teste,eaofinalverifica seosdadosficaramcomooesperado. Eletrabalhanonível
debancodedados,e nãonosobjetos,o quenospermiteinclusive testarpossíveis
proceduresexistentesnoprojeto.
@RunWith(Arquillian.class)
public class FuncionarioDBUnitTest {
@Deployment
public static JavaArchive createDeployment() {...}
@PersistenceContext(unitName = "livroCdiPU")
EntityManager em;
@Test
@UsingDataSet("funcionarios.xls")
@ShouldMatchDataSet("funcionarios-expected.xls")
public void deveDar10PorcentoAumentoAosFuncionariosNivelSuperior() {
List<Funcionario> funcionarios =
em.createQuery("select f from Funcionario f "
+ "where f.escolaridade = :escolaridade", Funcionario.class)
.setParameter("escolaridade", Escolaridade.SUPERIOR)
.getResultList();
for(Funcionario funcionario : funcionarios){
double salarioAtual = funcionario.getSalarioBase();
funcionario.setSalarioBase(salarioAtual * 1.1);
}
}
}
204

## Página 210

CasadoCódigo Capítulo10.ExecutandoCDIemdiferentesambientes
Nesseoutroteste,ométodo createDeployment()éexatamenteigualaodo
exemploanterior.O quepodemosnotardediferen çaéapresen çadasduasanotações
quefazusoreferênciaaoDBUnit: @UsingDataSete @ShouldMatchDataSet.
NoDBUnit,os datasetspodemserváriostiposdearquivos,comoXML,YML,
enonosso exemploutilizamos planilhasXLS,poiselasseparecembemcomasta-
belasquedesejamosrepresentar.Parautilizarumaplanilha, bastaquecadaplanilha
dentrodo arquivotenhaomesmonome decadatabela,ecadacolunadaplanilha
temqueteromesmonome dascolunasdo banco.
Comoessaferramenta trabalhanonívelde tabelas,não temosqueanalisaro
modeloOO,esimorelacional. Precisamosreproduzirnasplanilhasomodelorela-
cional,nãooOO,issoéimportante.Paraficarbemclaro,vamosanalisaraestrutura
dessaclasse Funcionario,queémaissimplesdoqueatínhamosvistoatéantesde
inciarmosessestestes.
public enum Escolaridade {
FUNDAMENTAL, MEDIO, SUPERIOR
}
@Entity
public class Funcionario implements Serializable {
@Id @GeneratedValue
private Integer id;
private String nome;
private double salarioBase;
private Escolaridade escolaridade;
//getters e setters
}
Agoravejamosasduasplanilhas,a quepossuiosdadosiniciais,ea quepossui
osdadosesperados.
205

## Página 211

10.4. Desenvolvendotestesdeintegraçãocompersistência CasadoCódigo
Figura10.1:Dadosiniciaisdo teste
OpróprioDBUnitapagatodososdados databelaedeixaexatamentecomos
dadosesperados.
206

## Página 212

CasadoCódigo Capítulo10.ExecutandoCDIemdiferentesambientes
Figura10.2:Dadosesperadosaofinaldo teste
A p ó sotesteéfeitaaverificaçãoseosdadosficaramdeacordocomoesperado.
Senãoestivero testefalha,nãoénecessárioassert.
Comonossotesteéfeitocombasenaescolaridadedofuncionário,eessedado
éumEnum,natabela,porpadrão,essedadovirauminteiro. Comopodemosvera,
temosdoisfuncionárioscomnívelsuperior:Ana,comsaláriobasedeR$4.000,00;e
Antôniocom saláriodeR$5.000,00. Naplanilhacomosdadosesperadosalteramos
apenasosvaloresdos saláriosdessesfuncionários,acrescentando10%(dezporcento)
comopedeoteste.
Apartirdesseponto,bastaimplementarosdemais testesdenegócio danossa
aplicação,poisosmecanismosjáestãofuncionando. Esperoqueesseúltimocapítulo
tenhaservidotambémcomoumpequeno tutorialdeArquillian,poisalémdetestar
asfuncionalidadesdaCDI,essaferramentaauxilia muitonostestescomJavaEEde
modogeral.
Assimcomoeste últimocapítulo,esperoqueestelivro tenhaservidoparaauxi-
liarnoseudesenvolvimentoprofissionalcomoumtodo.ACDIéumaespecificaç ão
muitointeressante,eespero queseusestudostantoemCDIcomoem JavaEEconti-
nuemevoluindo.O JavaEEtemmudadobastantenasúltimasversões, setornando
207

## Página 213

10.4. Desenvolvendotestesdeintegraçãocompersistência CasadoCódigo
cadavezmaissimplesdeutilizar, mesmoassimacreditoqueestelivrotenhacontri-
buídoparadeixarseuentendimentoaindamaissimples.
208