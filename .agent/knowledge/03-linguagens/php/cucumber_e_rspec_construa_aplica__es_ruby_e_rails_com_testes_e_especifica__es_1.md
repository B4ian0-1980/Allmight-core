---json
{
  "id": "cucumber_e_rspec_construa_aplica__es_ruby_e_rails_com_testes_e_especifica__es_1",
  "title": "Cucumber e RSpec Construa aplicações Ruby e Rails com testes e especificações",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Arquivo Original:** `Cucumber e RSpec Construa aplicações Ruby e Rails com testes e especificações.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "aplica",
    "com",
    "construa",
    "cucumber",
    "especifica",
    "linguagens",
    "php",
    "rails"
  ],
  "perguntas_tipo": [
    "Como utilizar Cucumber e RSpec Construa aplicações Ruby e Rails com testes e especificações?",
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

# Cucumber e RSpec Construa aplicações Ruby e Rails com testes e especificações

> **Arquivo Original:** `Cucumber e RSpec Construa aplicações Ruby e Rails com testes e especificações.pdf`
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

## Página 3

CasadoCódigo
Dedicatória
Dedicoaminhamãeeminhanoiva.
i

## Página 5

CasadoCódigo
Agradecimentos
Agradeçoaminhamãe,minhanoiva,amigosePlataformatec.
iii

## Página 7

CasadoCódigo
Sobre o autor
HugoBaraúnaéco-fundadordaPlataformatec,empresadeconsultoriaemdesenvol-
vimentodesoftwareespecializadaemRubyeRails.APlataformatecéreferênciana-
cionaleinternacionalnomundoRuby,devidoprincipalmenteaseusprojetosopen
sourceesuacolaboraçãocomacomunidade.Eleatuatantonadire çãodaempresa
quantocomodesenvolvedor,tendoparticipadodeprojetosdeconsultoria,coaching
etestesdecarga.
HugoseformouemEngenhariadeComputaç ãopelaPolitécnicadaUSPem
2010.Duranteafaculdade,passoupelolaboratórioUSP-Microsofteporempresas
comoProcworkeIBM.
Paraele,sóépossívelfazerprodutoseserviçosdequalidadequandoseamao
quefaz.
v

## Página 9

CasadoCódigo
Prefácio
vii

## Página 11

CasadoCódigo Sumário
Sumário
1 Visão geral sobre TDD 1
1.1 TDDesuahistória . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 EporqualmotivoeudeveriausarTDD? . . . . . . . . . . . . . . . . . 3
2 Primeiros passos com RSpec e Cucumber 5
2.1 OláRSpec. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.2 OláCucumber . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
2.3 OqueéBDD? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3 Introdu ção ao básico do RSpec 23
3.1 AprendendoaestruturabásicadeumtestecomRSpec . . . . . . . . . 23
3.2 PorquêexistemtantosmatchersnoRSpec . . . . . . . . . . . . . . . . 26
3.3 ConhecendoosRSpecbuilt-inmatchers . . . . . . . . . . . . . . . . . 33
3.4 Matchersrelacionadosatruthyefalsy . . . . . . . . . . . . . . . . . . 33
3.5 Osmatchersdeequidade . . . . . . . . . . . . . . . . . . . . . . . . . . 34
3.6 Matchersrelacionadosaarrays . . . . . . . . . . . . . . . . . . . . . . . 35
3.7 Custommatchers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
3.8 EntendendooprotocolointernodematcherdoRSpec . . . . . . . . . 53
3.9 Pontos-chavedestecapítulo . . . . . . . . . . . . . . . . . . . . . . . . 56
4 Organizaç ão, refatoração e reuso de testes com o RSpec 59
4.1 ReduzindoduplicaçãocomhooksdoRSpec . . . . . . . . . . . . . . . 59
4.2 DRYversusclarezanostestes . . . . . . . . . . . . . . . . . . . . . . . 65
4.3 Afterhook . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
4.4 Aroundhook . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
ix

## Página 12

Sumário CasadoCódigo
4.5 Organizandoseustestes . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
4.6 Reusodetestes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
4.7 Pontos-chavedestecapítulo . . . . . . . . . . . . . . . . . . . . . . . . 86
5 TDD na prática, come çando um projeto com TDD 87
5.1 Definindooescopodanossaaplicaç ão:JogodaForca . . . . . . . . . 88
5.2 EspecificandoumafuncionalidadecomCucumber . . . . . . . . . . . 89
5.3 UsandoRSpecnonossoprimeiroteste . . . . . . . . . . . . . . . . . . 94
5.4 UsandoArubaparatestarumaaplicaç ãoCLI . . . . . . . . . . . . . . 99
5.5 Pontos-chavedestecapítulo . . . . . . . . . . . . . . . . . . . . . . . . 104
6 Come çando o segundo cenário 107
6.1 Definindoosegundocenário . . . . . . . . . . . . . . . . . . . . . . . . 107
6.2 Reduzaduplicaçãoatravésdesupportcode . . . . . . . . . . . . . . . 108
6.3 Implementandoofluxodojogonobinário . . . . . . . . . . . . . . . . 110
6.4 Modificandonossocenárioparareceberofeedbackcorreto . . . . . . 113
6.5 UsandosubjecteletdoRSpecparaevitarduplicaç ãonostestes . . . . 116
6.6 Refatorandoocódigoparapoderimplementarosegundocenário . . 119
6.7 Extraindoumaclasseatravésderefatoração . . . . . . . . . . . . . . . 123
6.8 Possibilitandoaojogadorterminarojogonomeio . . . . . . . . . . . 127
6.9 Pontos-chavedestecapítulo . . . . . . . . . . . . . . . . . . . . . . . . 129
7 Finalizando a primeira funcionalidade 131
7.1 Continuandoosegundocenário . . . . . . . . . . . . . . . . . . . . . . 131
7.2 Deixandoosegundocenárionoverde . . . . . . . . . . . . . . . . . . 132
7.3 Finalizandoaprimeirafuncionalidade . . . . . . . . . . . . . . . . . . 139
7.4 Pontos-chavedestecapítulo . . . . . . . . . . . . . . . . . . . . . . . . 142
8 Refatorando nosso código 143
8.1 Identificadoospontosaseremrefatorados . . . . . . . . . . . . . . . . 143
8.2 Extraindoumaclassedeummétodoprivado . . . . . . . . . . . . . . 146
8.3 Distribuindoresponsabilidadesparaoutrasclasses . . . . . . . . . . . 153
8.4 Pontos-chavedestecapítulo . . . . . . . . . . . . . . . . . . . . . . . . 167
x

## Página 13

CasadoCódigo Sumário
9 Especificando a segunda funcionalidade 169
9.1 DocumentandoespecificaçãoecritériodeaceitecomCucumber . . . 169
9.2 Definindootestedeaceitaçãodoprimeirocenário . . . . . . . . . . . 171
9.3 Melhoreatestabilidadedoseusoftware . . . . . . . . . . . . . . . . . . 175
9.4 Pontos-chavedestecapítulo . . . . . . . . . . . . . . . . . . . . . . . . 184
10 Finalizando a segunda funcionalidade 187
10.1 Refatorandonossojogoparaterumamáquinadeestados . . . . . . . 187
10.2 Refatorandoofluxodojogoparausaramáquinadeestados . . . . . 193
10.3 Organizandoseustestesotimizandoparaleitura . . . . . . . . . . . . 198
10.4 Interfacediscoveryutilizandotestdoubles . . . . . . . . . . . . . . . . 201
10.5 FinalizandoafuncionalidadeAdivinharletra . . . . . . . . . . . . . . 219
10.6 Pontos-chavedestecapítulo . . . . . . . . . . . . . . . . . . . . . . . . 229
11 Finalizando nosso jogo 231
11.1 Especificandoofimdojogo . . . . . . . . . . . . . . . . . . . . . . . . 231
11.2 Jogadorvenceojogo . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232
11.3 Jogadorperdeojogo . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241
11.4 Próximospassos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .246
Bibliografia 249
Versão:16.2.23
xi

## Página 15

Capítulo1
VisãogeralsobreTDD
UmadasmelhoresqualidadesdacomunidadeRubyéousoconstantedeTDD(test-
drivendevelopment).Todoprojetoopen-sourcefamosonanossacomunidadetem
umasuítedetestesautomatizados.Éopadrãoeodiaadiadetododesenvolvedor
Ruby.Sevocêaindanãofazisso,vocênãoéumdesenvolvedorRubycompleto.Ao
lerestelivro,vocêestádandomaisalgunspassosemdire çãoaserumdesenvolvedor
melhor.
Durantealeituradestelivro,vocêiráaprenderafazerTDD,o T est-Driven De-
velopment,usandoalgumasdasferramentasmaisfamosasnacomunidadeRuby:o
RSpeceoCucumber.Vocêiráaprendersobreasferramentasemsietambémsobre
comoaplicaratécnicadeTDDparaconstruirumsoftwaredemaisqualidade.
SevocêaindanãoconheceouconhecepoucosobreTDD,prepare-se,porque
essapráticairámudaromodocomovocêescrevesoftware...paramelhor.

## Página 16

1.1. TDDesuahistória CasadoCódigo
1.1 TDD e sua história
AhistóriadeTDDcome çaprincipalmentenocome çodadécadade90,quando
KentBeckescreveemSmalltalksuaprimeirabibliotecadetestes,oSUnit. Aideia
inicialdeleerafacilitaraexecuç ãodetestesdesoftware,automatizandoessatarefa
quemuitasdasvezeserafeitamanualmente.
AlgunsanossepassarameemumaviagemdeaviãoparaoOOPSLA(Object-
OrientedProgramming,Systems,Languages&Applications),tradicionaleventode
orientaçãoaobjetos,KentBeckeErichGammaescreveramumaversãodoSUnit
emJava,oJUnit.
OJUnitfoiganhandomaisemaisespaçonomundodedesenvolvimentodesoft-
ware,tendováriosportsfeitosparaoutraslinguagenscomoRuby,C++,Perl,Python,
PHPeoutras. Aopadrãodafamíliaformadaportodasessasbibliotecassedeuo
nomedexUnit.
AopassoqueousodasbibliotecasxUnitfoiamadurecendo,utilizá-lasnãoera
maisvistocomoapenasumaatividadedeteste,massimcomoumaatividadede
design(projeto)decódigo.Essavisãofazsentidoaosepensarqueantesdeimple-
mentarumdeterminadométodoouclasse,osusuáriosdexUnitprimeiroescrevem
umtesteespecificandoocomportamentoesperado,edepoisfazemocódigoquevai
fazercomessetestepasse.AesseusodasbibliotecasxUnit,sedeuonomedetest-
drivendevelopment(TDD).
Nofinaldadécadade90,KentBeckformalizouoExtremeProgramming(XP),
queviriaaserumadasprincipaismetodologiaságeisdedesenvolvimentodesoft-
waredomundo.OXPéformadoporalgumaspráticasessenciais,entreelasoTDD.
ComaevangelizaçãodeTDDdentrodoXP,apráticaganhouaindamaistraç ão,
sendovistocomoumadasbasesparaodesenvolvimentodesoftwarecomqualidade.
EntrandonomundoRuby, aprimeirabibliotecadetestesautomatizadosna
nossalinguagemfoiescritaporNathanielTalbott,batizadacomonomeLapidary.
TalbottapresentouoLapidarynaprimeiraRubyConfdahistória,em2002.OLapi-
darydeuorigemao Test::Unit,tradicionalbibliotecaxUnitemRuby,queusamos
atéhoje. Desdeocomeçodanossacomunidade,ousodeTDDetestesautomati-
zadossemprefoiaregra,enãoaexce ção.Comoeudisseantes,todoprojetoopen
sourceemRubyqueseprezatemtestesautomatizados.
Em2003,DavidHeinemeierHansson(DHH)escreveuoRubyonRails(oupara
osíntimos,Rails).Railssetornouo killer appdalinguagemRuby,ouseja,Railsétão
bomqueaspessoascome çaramaaprenderRubysóporcausadele.Comoumdos
2

## Página 17

CasadoCódigo Capítulo1. VisãogeralsobreTDD
softwaresmaisfamososescritosemRuby,Railstambémtevegrandeimportânciana
evangelizaçãodeTDDnanossacomunidade.Issoporqueporpadrãotodoprojeto
geradopeloRailsjávemcomumdiretórioespecíficoparavocêcolocarseustestes
automatizados,ouseja,RailsteconvidaafazerTDD.
Daíprafrente,orestoéhistória.HojeTDDéumapráticamuitobemdifundida
nomundodedesenvolvimentodesoftware,sendovistacomoumadasbasespara
desenvolvimentodesoftwarecomqualidadeedefácilmanuten ção.
1.2 E por qual motivo eu deveria usar TDD?
Em1981,nolivro Software Engineering Economics[2],BarryBoehmsugeriuqueo
custodealteraçãoemumprojetodesoftwarecresceexponencialmenteàmedidaque
seavançanasfasesdodesenvolvimento.
Figura1.1:Custodealteraçãoemumprojetodesoftware
Comoocustodealteraçãodosoftwarecrescemuitoaolongodasfasesdedesen-
volvimento,seriamelhorfazeramaioriadasalteraçõesnecessáriaslogonocome ço
deumprojeto,queseriamasfasesdelevantamentoderequisitoseanálise. Uma
metodologiaquesegueessaideiaéaCascata(Waterfall ).
Outraabordagemquepodesertomadaemrelaç ãoaesseaumentoexponencial
nocustodealteraçãoétentarreduzi-loemantê-lomaisconstanteaolongodode-
senvolvimentodoprojetoedociclodevidadosoftware. Essaéumadasideiasde
metodologiaságeis,comooXP,ondeumadaspráticasqueajudaadiminuiresse
custoéoTDD.
3

## Página 18

1.2. EporqualmotivoeudeveriausarTDD? CasadoCódigo
UmadasconsequênciasdefazerTDDéqueoseusistemaficacobertoporuma
suítedetestesautomatizados,demodoquetodavezquevocêforfazerumamu-
dançanocódigo,épossívelrodarasuíteeelaentãodirásevocêquebroualgum
comportamentopreviamenteimplementado.
SegundooXP,odesenvolvedordeveaolongodoprojetorefatorarconstante-
menteocódigoparadeixarodesignomelhorpossível.Comarefatoraç ãoconstante,
odesigndosoftwarepodesemanterbom,demodoqueocustodealteraç ãodosis-
temanãocres çaexponencialmente.Naprática,issoquerdizerquesenocome çodo
projetolevaumasemanaparaadicionarumafuncionalidade,umanodepois,deve
continuarlevandoumasemanaoupoucomaisdoqueisso. Essamanuten çãodo
custodemudan çadocódigoemumnívelbaixoéumadasvantagensqueseganha
aoutilizarTDD.
Outravantageméaperdadomedodemudarocódigo.Apossibilidadedepoder
seapoiarnasuítedetestetodavezquevocêformodificarosoftwaretedaliberdade
ecoragememmudareadaptarosistemadeacordocomanecessidadedoprojeto,
portodasuavida.Essetipodecoisapermite,porexemplo,quevocêpossafazermu-
dançasarquiteturaisnoseucódigo,garantindoqueeleirácontinuarfuncionando.
Permitetambémquenovosintegrantesdaequipepossamconseguircontribuirmais
rapidamentenoprojeto,vistoqueelesnãoprecisamtermedodemudarocódigo.
Porfim,outravantagemnotadapelospraticanteseestudiososdeTDDéame-
lhoranodesigndoseucódigo. Existemváriosexemplosmostrandoumarelaç ão
diretaentretestabilidadeebomdesign.Aideiageraléqueseseucódigofordifícil
detestar,significaqueelepodeestaracopladodemaisoucombaixacoesão.TDDnos
ajudaadetectaressetipodeproblema,nossugerindomelhorarodesigndonosso
código.Essavantagemvaificarmaisclaraquandoformosdesenvolverumprojeto
inteirocomTDD,apartirdocapítulo 5.
AgoraquevocêjáconheceahistóriaportrásdoTDDeasvantagensdeusá-lo,
vamosverumexemplosimplesdecomoéissonapráticaedepoisvamosfalarsobre
acontinuaçãodessahistóriaecomoelaculminounoquehojeconhecemoscomo
BDD(behavior-driven development).
4

## Página 19

Capítulo2
PrimeirospassoscomRSpece
Cucumber
Comodesenvolvedor,conhe çoanossasedeporvercódigo.Todomundojáouviua
tradicionalfrase“show me the code!”.Éporissoqueaoinvésdecomeçarmosvendoos
detalhessobreRSpeceCucumber,vamosprimeiroverumaespéciede“helloworld”
paraambasasferramentas.
Nesteprimeiromomento,omaisimportanteéquevocêpossaterumaideiada
“cara”doRSpecedoCucumber,eéissoquevamosfazernestecapítulo.
2.1 O lá RSpec
ORSpecéumabibliotecadetestesdeunidadeemRubyquesegueafilosofiadoBDD,
queéumaextensãodoTDD.VamosfalarmelhorsobreBDDdepois.Porenquanto
nossoobjetivoévernapráticacomoéescreverumpequenoprogramaseguindo
TDDeusandoRSpec.

## Página 20

2.1. OláRSpec CasadoCódigo
Comovocêviunocapítulo 1,TDDnãoéconsideradoapenasumapráticade
teste,massimumapráticadedesign.Issosefazverdadepois,aoseguiroTDD,você
pensanaAPI(interface)doseusoftwareantesmesmodeconstruí-lo.Vocêdescreve
essepensamento,essaespecificação,emformatodetesteautomatizado. Umavez
otestefeito,vocêdesenvolveopedaçodesoftwarequevocêacaboudeespecificar,
fazendocomqueseutestepasse.Umavezqueotestepassoueestáminimamente
atendido,vocêficalivrepararefatoraroseucódigo,reduzindoduplicação,deixando-
omaisclaroefazendooutrasmelhoriasquevocêjulgarnecessárias.Aessefluxodo
TDDsedáonomedered-green-refactor.Vamosaplicá-loparaficarmaisclaro.
Figura2.1:Ciclored-green-refactor
O primeiro teste com RSpec
NaminhaauladeestruturadedadosdaPoliaprendiaimplementarumapilha.
NaqueletempoeunãoconheciaTDD,entãofiznaraç a,semtestes(eemC).Hoje,
olhandopratrás,ficaacuriosidade:“comoseriaimplementaraquelapilha,sóque
comtestes?”
Horademataressacuriosidade!
Umapilha(Stack)éumaestruturadedados LIFO(last in, first out),ouseja,é
umacoleçãodeelementosnaqualoúltimoquevocêcolocouéoprimeiroasair.
Vamosespecificaressecomportamentoemformatodeteste.
NãoseimporteporenquantocomasintaxedoRSpec,ocódigoserásimpleso
bastanteparaquevocêpossaentendê-lomesmosemnuncatervistoRSpec.
Vamoscomeçarespecificandoométodo push(empilha).Quandovocêempilhar
6

## Página 21

CasadoCódigo Capítulo2. PrimeirospassoscomRSpeceCucumber
umelemento,entãoesseelementodevepoderservisualizadonotopodapilha.
Figura2.2:Pilhacomelementossendoempilhados
Vamoscriarumarquivochamado stack_spec.rbcomoseguintecódigo,que
especificaráessecomportamento:
describe Stack do
describe "#push" do
it "puts an element at the top of the stack" do
stack = Stack.new
stack.push(1)
stack.push(2)
expect(stack.top).to eq(2)
end
end
end
Novamente,nãoseassustecomasintaxe.Atente-seapenasaofatodequeesta-
moschamandoométodo pushparaadicionarprimeirooelemento 1eemseguida
oelemento 2napilhaeporfim,indicamosqueo topodapilhadevecontero
elemento 2,seguindoassimaideiade last in, first out.
EsseéumtesteescritocomRSpecepararodá-lo,precisamosantesinstalá-lo,
atravésdesuagem.Parafazerainstalação,executeoseguintecomandonoseucon-
sole:
$ gem install rspec
Comeleinstalado,pararodarseustestesbastaexecutarnoseuconsole:
7

## Página 22

2.1. OláRSpec CasadoCódigo
$ rspec --color stack_spec.rb
AorodaroRSpec,otestequebra,comoesperado.Esseéopasso red,dociclo
red-green-refactor.Elequebrouporqueatéagorasóimplementamosoteste,não
implementamosnenhumcódigoqueofaçapassar.Nessemomento,oimportanteé
verqueotestequebroueporquêelequebrou.ApósterrodadooRSpec,vocêdeve
tervistoumamensagemdeerrocontendoaseguintesaída:
$ rspec --color stack_spec.rb
(...)
uninitialized constant Stack (NameError)
Amensagemdeerronosdizqueotestequebrouporqueaconstante Stack
aindanãofoidefinida.Ouseja,precisamoscriaraclasse Stack.Parasimplificar,
escrevaadefiniçãodaclassenomesmoarquivo stack_spec.rbdemodoqueele
fiqueassim:
class Stack
end
describe Stack do
describe "#push" do
it "puts an element at the top of the stack" do
stack = Stack.new
stack.push(1)
stack.push(2)
expect(stack.top).to eq(2)
end
end
end
AorodaroRSpecagora,vemososeguinte:
$ rspec --color stack_spec.rb
(...)
Failures:
8

## Página 23

CasadoCódigo Capítulo2. PrimeirospassoscomRSpeceCucumber
1) Stack#push puts an element at the top of the stack
Failure/Error: stack.push(1)
NoMethodError:
undefined method `push' for #<Stack:0x007fa91b919b70>
Figura2.3:Testenovermelho
Evoluímos,masotesteaindaquebroueamensagemdeerroagoranosdizque
foiporqueométodo pushaindanãoestádefinido,precisamosimplementaresse
métodoainda.
Paraimplementarométodo push,precisamospensarnoqueeleiráfazer.Te-
mosquecolocarumelementodentrodapilha,demodoqueoúltimoitemcolocado
éoqueficaránotopodapilha.Comomecanismoparaguardaroselementos,pode-
mosusarum Arrayeircolocandooselementosdentrodele.Faç aissoeditandoa
classe Stackdoseguintemodo:
class Stack
def initialize
@elements = []
end
def push(element)
@elements << element
end
end
9

## Página 24

2.1. OláRSpec CasadoCódigo
# (...)
Comométodo pushimplementado,vamosrodaroRSpecnovamente:
$ rspec --color stack_spec.rb
(...)
Failures:
1) Stack#push puts an element at the top of the stack
Failure/Error: expect(stack.top).to eq(2)
NoMethodError:
undefined method `top' for #<Stack:0x007fce55c55e38 >
Evoluímosmaisumpoucoeotestequebrounovamente.Nãodesanime!Dessa
vezamensagemdeerrofoidiferente,oquerquerdizerqueestamosprogredindo.
Agoraelanosdizqueomotivodafalhaéqueométodo topaindanãofoiimple-
mentado.
Oqueométodo topprecisafazeréapenasretornaroúltimoelementoquefoi
empilhado. Parasabermosqualoúltimoelementoadicionadonanossapilha,va-
moscriarumavariáveldeinstânciachamada @last_element_indexparasalvar
oíndicedoúltimoelemento,noarrayinterno @elements,adicionadoapilha.Mo-
difiqueocódigoparaseguiressaideiaeficarassim:
class Stack
def initialize
@elements = []
@last_element_index = -1
end
def push(element)
@elements << element
@last_element_index += 1
end
def top
@elements[@last_element_index]
end
end
10

## Página 25

CasadoCódigo Capítulo2. PrimeirospassoscomRSpeceCucumber
AorodarmosoRSpec,dessavezvemososeguinte:
$ rspec --color --format documentation stack_spec.rb
Stack
#push
puts an element at the top of the stack
Finished in 0.00549 seconds
1 example, 0 failures
Figura2.4:Testenoverde
Agoraotestepassou!Chegamosaopasso greendociclored-green-refactor.
Agoraqueostestesestãonoverde,podemosrefatorarotestee/ouocódigopara
melhorá-los.Refatorarémelhorarocódigosemmudarseucomportamentoexterno,
nãoadicionandonenhumcomportamentonovo,apenasmelhorandoaqualidade
internadonossosoftware.
Umpontoquepodemosmelhorarnonossocódigoéomodocomoestamos
pegandooúltimoelementosalvonapilha. Aoinvésdecriarumavariáveldeins-
tânciaparapegaroúltimoelementodoarrayinterno,podemossimplesmentefazer
elements[-1]. Passando-1paraíndicedoarray,indicamosqueestamosque-
rendooúltimoelementoadicionado.
Seguindoessaideia,modifiqueocódigoparaficarassim:
class Stack
def initialize
@elements = []
end
11

## Página 26

2.1. OláRSpec CasadoCódigo
def push(element)
@elements << element
end
def top
@elements[-1]
end
end
AgorarodeoRSpecnovamenteparachecarseotesteestápassandoeocompor-
tamentopreviamenteespecificadocontinuafuncionando:
$ rspec --color --format documentation stack_spec.rb
Stack
#push
puts an element at the top of the stack
Finished in 0.00549 seconds
1 example, 0 failures
Sucesso,otestecontinuanoverde!Issoquerdizerqueconseguimosrefatoraro
nossocódigocomsucesso.Melhoramosaqualidadeinternasemquebrarnadaque
jáestavafuncionando.
Opassoseguinteseriaescreveropróximotestedaclasse Stack,talvezparao
métodotop,ouparaumpossívelmétodo pop(desempilha),seguindoociclored
-green-refactornovamente.Esseseudeixareicomoumdesafioparavocê,apenas
repliqueopadrãoquefoimostrado.
Nocapítulo3iremosentraremdetalhesnoRSpec,entenderessasintaxeestra-
nhaeasmuitasnuancesdoframework. Eapartirdocapítulo 5iremosconstruir
umaaplicaçãointeirafazendoTDD,usandoRSpecdocome çoaofim.Lávocêterá
bastantetempoeexemplosparaexercitarociclored-green-refactoreaprender
comoseconstróiumsoftwareinteirousandoTDD.
Dandoumaúltimaolhadanocódigoqueescrevemosparafazerotestecomo
RSpec,dáparaperceberquefizemosadescriç ãodeumcomportamentodonosso
código,atravésdasseguinteslinhas:
describe Stack do
describe "#push" do
it "puts an element at the top of the stack" do
12

## Página 27

CasadoCódigo Capítulo2. PrimeirospassoscomRSpeceCucumber
Dissemosqueestávamos“Descrevendo”(Describe)aclasseStack,emseguida
oseumétodo #pusheporfim,falamosqueelecolocaoelementonotopodapilha.
Masreparequemisturamoscódigocomotexto.Seráquenãoháumaalternativade
descrevernossaaplicaçãocomoumtodo,apenascomoumtexto,umroteiro,efazer
comqueissoexecute?Nãoseriamaisnatural?
Escrevo em português ou em inglês?
Émuitocomumseperguntarseadescriç ãodoqueestátestandodeve
serfeitoeminglêsouemportuguês.PelofatodeoRSpecsebasearno
inglês,ficamaisnaturalmantertudonomesmoidioma,alémdequea
legibilidadeficamaiorquandoseentendeoidioma.Masnadaoimpede
fazerasdescriçõesemportuguês.
Duranteolivro,usaremosasdescriçõeseminglês,masdaremossem-
preasexplicaçõesemportuguês.
2.2 O lá Cucumber
OCucumberéumaferramentadetestesdeaceitação,ouseja,serveparaautomatizar
testesdocomportamentodosoftwarelevandoemcontaopontodevistadousuário
final.
AoescreverumtestecomCucumber,vocêiráespecificarumafuncionalidade
doseusistema,aoinvésdeespecificarumaclasseouummétodo. Demodobem
resumido,entendaoCucumbercomoumaespéciededocumentaç ãoderequisitos
funcionais on steroids.
Eudigoisso,poisapropostadoCucumberéajudaraespecificarosistemacom
documentosescritosemumalinguagemnatural(inglês,portuguêsetc),porémcom
apossibilidadedeexecutaressadocumentaç ãoparaverificarocomportamentoes-
pecificadonosistemareal.Ouseja,umadocumentaç ãoexecutável.
O primeiro teste com Cucumber
Paraficarmaisclaro,vamosverumexemplodeumaespecificaç ãoescritacom
Cucumber.
Vocêfoicontratadoparadesenvolverumpequenojogodaforca,queiráfunci-
onarnoshell.Vocêconversacomocliente,eleteexplicaomotivodequererojogo
ecomoelepensaqueeleiráfuncionar.
13

## Página 28

2.2. OláCucumber CasadoCódigo
Vocêentendeocontextointeiroedecidedocumentaraprimeirafuncionalidade
paraentãopediraoclienteparaconferirseoseuentendimentoestácorreto.Apri-
meirafuncionalidadequevocêimaginaéade“Começarjogo”,evocêadocumenta
doseguintemodo:
# language: pt
Funcionalidade: Começar jogo
Para poder passar o tempo
Como jogador
Quero poder começar um novo jogo
Cenário: Começo de novo jogo com sucesso
Ao começar o jogo, é mostrada a mensagem inicial para o jogador.
Quando começo um novo jogo
Então vejo a seguinte mensagem na tela:
"""
Bem vindo ao jogo da forca!
"""
Esseéumexemplorealdeespecificaç ãodesoftwarecomCucumber. Aspec
temotítulodafuncionalidade,umanarrativaexplicandoocontextoeporfimum
cenáriodeteste,mostrandoumexemplodecomoosoftwareiráfuncionardoponto
devistadousuáriofinal.
Cenários em português
DiferentementedequandoescrevemosasespecificaçõescomoRS-
pec,ondemisturávamoscódigoetexto,comoCucumberescrevemos
apenastextoparadescreveroscenários.Issoremovequalquerruídoque
alinguagemdeprogramaçãopudessecausarnadescriçãoedessaforma,
fazcomqueescreveremlinguagemnaturalsejaalgobemsimplesedi-
reto.
Duranteolivro,paraoscenáriosemcucumber,usaremossempreo
português.
Percebacomoaespecificaçãoébemsimpleseclara.Oclienteentãolêaspece
confirmaqueoentendimentoestácorreto. Vocêpodeagorairemfrenteedesen-
volveressafuncionalidade.UmadasvantagensdeutilizaroCucumberéquevocê
14

## Página 29

CasadoCódigo Capítulo2. PrimeirospassoscomRSpeceCucumber
podeusaressamesmadocumentaç ãoparacriarumcenáriodetestedeaceitaç ão
automatizado.Vamosfazerisso.
Antesdetudo,precisamosinstalaroCucumber.Comoeletambémédistribuído
comoumagem,bastaexecutarnoseuconsole:
$ gem install cucumber
Agoracrieumnovodiretóriochamado hello-cucumberedentrodelecrie
umoutrodiretóriochamado features. Dentrodessediretório features,crie
umarquivochamado features/comecar_jogo.featureesalvedentrodeleo
conteúdodaespecificaçãoquefizemoshápouco. AgoravocêjápoderodaroCu-
cumber.
Parafazerisso, dentrododiretório hello-cucumber, executeocomando
cucumbernoseuconsole:
$ cucumber
Issofarácomqueoscenáriossejamexecutadoseaseguintesaídaapare çacomo
resultado:
# language: pt
Funcionalidade: Começar jogo
Para poder passar o tempo
Como jogador
Quero poder começar um novo jogo
Cenário: Começo de novo jogo com sucesso
Ao começar o jogo, é mostrada a mensagem inicial para o jogador.
Quando começo um novo jogo
Então vejo a seguinte mensagem na tela:
"""
Bem vindo ao jogo da forca!
"""
1 scenario (1 undefined)
2 steps (2 undefined)
0m0.002s
You can implement step definitions for undefined steps with these
snippets:
15

## Página 30

2.2. OláCucumber CasadoCódigo
Quando /^começo um novo jogo$/ do
pending # express the regexp above with the code you wish you had
end
Então /^vejo a seguinte mensagem na tela:$/ do |string|
pending # express the regexp above with the code you wish you had
end
VamosanalisarumpoucoasaídadoCucumber.Logodepoisdotextodaespe-
cificaçãoemsi,vemososeguinte:
1 scenario (1 undefined)
2 steps (2 undefined)
Percebaqueeledizquetemosumcenárioqueestáindefinidoequeexistemdois
stepstambémindefinidos.EmspecsdeCucumber,cadacasodetesteéumcenárioe
cadacenárioécompostoporváriossteps.Nonossocaso,temosocenário "Começo
de novo jogo com sucesso” quecontémossteps "Quando começo um novo jogo” e
"Então vejo a seguinte mensagem na tela: (...)”.
16

## Página 31

CasadoCódigo Capítulo2. PrimeirospassoscomRSpeceCucumber
Figura2.5:EstruturadeumaespecificaçãocomCucumber
Parautilizaressadocumentaçãocomoumtesteautomatizado,temosquedefinir
cadaumdessessteps,implementandooqueoCucumberchamade step definitions.
BasicamenteédizeraoCucumberoqueeleprecisafazernaquelepasso. Olegalé
queseostepaindaestáindefinido,opróprioCucumberjánosdáumsnippetde
stepdefinition,comopudemosvernofinaldasaída:
$ cucumber
(...)
You can implement step definitions for undefined steps with these
snippets:
Quando /^começo um novo jogo$/ do
pending # express the regexp above with the code you wish you had
end
Então /^vejo a seguinte mensagem na tela:$/ do |string|
17

## Página 32

2.2. OláCucumber CasadoCódigo
pending # express the regexp above with the code you wish you had
end
Vamosagoraautomatizarnossaespecificação.Primeirocrieumdiretóriodentro
do featuresevamoschamá-lode step_definitions.Dentrodessediretório
crieumarquivochamado game_steps.rb.Nessearquivovamoscolocarosstep
definitionsdosdoisquetemosnanossaspec. Implementeessesstepsdoseguinte
modonessearquivo:
# encoding: UTF-8
Quando /^começo um novo jogo$/ do
@game = Game.new
@game.start
end
Então /^vejo a seguinte mensagem na tela:$/ do |text|
expect(@game.output).to include(text)
end
Oquefizemosfoiimplementarosstepdefinitions,definindoquaispartesdaAPI
donossosoftwarecadastepdefinitionvaiutilizar.
Paraostepdecome çarumnovojogo, imaginamosquepoderíamosterum
objeto @game e que para começar um novo jogo bastaria chamar o método
game.start.
Nosegundostepdefinition,estamosverificandoseo outputdo @gamecontém
amensageminicialdojogo,queestásalvanavariável text.
Especificaçõesdecucumberdevemtestarosistemautilizandoamesmainterface
queousuárioutilizaria.Onossojogoseráumjogodeconsole,masporenquanto
vamosmanterotestebemsimplesnesse“helloworld”,semumainteraçãorealdo
testecomoconsole.Iremosfazeressetipodetestedemodocompletoedetalhadoa
partirdocapítulo 5.
Comosstepdefinitionsprontos,vamosrodaroCucumbernovamente:
$ cucumber
(...)
uninitialized constant Game (NameError)
18

## Página 33

CasadoCódigo Capítulo2. PrimeirospassoscomRSpeceCucumber
(...)
1 scenario (1 failed)
2 steps (1 failed, 1 skipped)
Percebaqueotestequebrouequenosdeuumamensagemdeerro.Amensagem
deerrodotesteéofeedbackquedevemosusarparaopróximopassodeimplemen-
tação.Nessecasoamensagemestádizendoqueaclasse Gameaindanãofoidefinida.
OcorretonessemomentoagoraseriapararumpoucoostestesdeCucumbere
começarumciclocompletodered-green-refactorcomRSpecparaadefiniç ãoda
classe Game,masnãovamosfazerissoagora,paramanteroexemplosimples. O
ciclointeirodeBDDcomCucumbereRSpecseráfeitoextensivamenteapartirdo
capítulo5.
Por enquanto, vamos apenas definir a classeGame dentro do arquivo
features/step_definitions/game_steps.rbmesmo.Adicioneadefinição
dessaclassenofinaldessearquivo:
# encoding: UTF-8
Quando /^começo um novo jogo$/ do
@game = Game.new
@game.start
end
Então /^vejo a seguinte mensagem na tela:$/ do |text|
expect(@game.output).to include(text)
end
class Game
end
AorodaroCucumbernovamente,vemosumamensagemdeerrodiferente:
$ cucumber
(...)
undefined method `start' for #<Game:0x007fde41b5a938> (NoMethodError)
(...)
19

## Página 34

2.2. OláCucumber CasadoCódigo
Dessavezotestequebrouporqueométodo Game#startnãofoidefinidoainda.
Vamosimplementaressemétodo,quevaisalvardentrodo outputdojogoamen-
sageminicial.Adicioneessemétodoàclasse Gamedoseguintemodo:
# encoding: UTF-8
# (...)
class Game
def initialize
@output = []
end
def start
@output << "Bem vindo ao jogo da forca!"
end
end
AorodarmosoCucumber,podemosverqueamensagemdeerromudou:
$ cucumber
(...)
undefined method `output' for #<Game:0x007fbcdb268410> (NoMethodError)
(...)
Pela mensagem de erro, podemos ver que falta implementar o método
Game#output,responsávelpordevolveroconteúdodavariável @output. Para
implementá-lo,bastaadicionarum attr_reader :outputnaclasse Game:
# encoding: UTF-8
# (...)
class Game
attr_reader :output
# (...)
end
AorodaroCucumberagora,vemosqueagoraeleestánoverde!
20

## Página 35

CasadoCódigo Capítulo2. PrimeirospassoscomRSpeceCucumber
$ cucumber
(...)
1 scenario (1 passed)
2 steps (2 passed)
Figura2.6:SpeccomCucumbernoverde
Pronto,vocêacaboudeescreversuaprimeiraespecificaçãocomCucumber!A
ideiaeramostrardemodorápidocomoéacaradoRSpecedoCucumber,paravocê
terumaideiadoquevempelafrente.
Reparequeduranteostestes,otempointeironósdescrevemosocomportamento
dasaplicações.Essefoconocomportamentoéumgrandediferencial,quequando
bemusado,podedarumanovavidaaosnossostestes.
2.3 O que é BDD?
OtermoBDD(behavior-drivendevelopment)foicunhadoporDanNorthporvolta
de2003[11].DanNorthestavatendodificuldadesemensinarTDDparaseusalunos,
poiselesficavamcomdúvidassobreporondecome çaratestar,oquetestar,como
nomearseustestesetc.
ElepercebeuquepartedoproblemaementenderTDDeraapalavra testeem
si,poiselaconfundiaodesenvolvedorsobrearealmotivaç ãoportrásdeTDD.A
21

## Página 36

2.3. OqueéBDD? CasadoCódigo
principalmotivaçãodoTDDnãoétestaroseusoftware,esimespecificá-locom
exemplosdecomousaroseucódigoedeixarissoguiarodesigndomesmo.
AofazerTDD,odesenvolvedorestáespecificandoocomportamentodoseusoft-
wareedefinindoseudesign.AsuítedetestesautomatizadosgeradaatravésdoTDD
é“apenas”umaboaconsequênciadoprocesso. Baseadonessasideias,DanNorth
sugeriumudarapalavrade testepara comportamento(behavior). Paraconcretizar
suaideia,DanNorthescreveuoJBehave,umabibliotecadeBDDemJava.
NomundodeRuby,aideiadeBDDcome çouaseconcretizarquandoDanNorth
portouoJBehaveparaRubycomonomedeRBehave. Em2005,inspiradopela
ideiadeBDD,StevenBakerescreveuaprimeiraversãodoRSpec.Temposdepoiso
RBehavefoiintegradoaoRSpeccomonomedeStoryRunner.Finalmente,em2008,
AslakHellesøyreescreveuoStoryRunnereochamoudeCucumber.
ApesardoBDDternascidoapenascomoummododereveranomenclaturado
TDDeomodocomoseenxergaessaprática,hojeBDDémaisdoqueisso,eleagora
éumaabordagemdedesenvolvimentodesoftware[3]quepropõequevocêdesen-
volvaseusoftwareespecificandoasváriascamadasdecomportamentocomtestes
automatizados.Comeceprimeiroespecificandoocomportamentodeumafuncio-
nalidade.Depoisdisso,especifiqueasclassesemétodosqueserãonecessáriaspara
implementaressafuncionalidade.
Àpráticadecome çarodesenvolvimentodeumafuncionalidadecomtestesde
aceitaçãoedepoisfazerostestesdeunidade,sedáonomede acceptance test-driven
development(ATDD).EssaéumadaspráticasnasquaisoBDDsebaseia.Umadas
outraspráticaséofamoso domain-driven design[4].
Apartirdocapítulo 5nósiremosdesenvolverumaaplicaçãoseguindoofluxode
BDD.ComeçaremosportestesdeaceitaçãocomCucumbereemseguidafaremos
testesdeunidadecomRSpec. Masantesdecome çarmosadesenvolveroprojeto,
vocêprecisaaprendermaissobreoRSpeceoCucumber,eéissoquefaremosnos
capítulosaseguir.
22

## Página 37

Capítulo3
IntroduçãoaobásicodoRSpec
NestecapítulovocêiráaprendercomousaroRSpecparafazertestesdeunidade.
IremosvercomooRSpecpodenosajudaraescrevertestesquesejamlegíveiseque
possamservirnãosócomotestesderegressãomastambémcomomaisumafonte
dedocumentaçãodonossocódigo.
3.1 A prendendo a estrutura básica de um teste com
RSpec
ParacomeçarmosaentenderaestruturadeumtestecomRSpec,vamosdaruma
olhadanoquefizemosnocapítuloanterior:
describe Stack do
describe "#push" do
it "puts an element at the top of the stack" do
stack = Stack.new

## Página 38

3.1. AprendendoaestruturabásicadeumtestecomRSpec CasadoCódigo
stack.push(1)
stack.push(2)
expect(stack.top).to eq(2)
end
end
end
Aprimeiracoisaqueestamosfazendonessetesteéchamarométodo describe:
describe Stack do
# (...)
end
Ométodo describeserveparaagruparosnossostestes. Noqueacaba-
mos de fazer, usamos umdescribepara agrupar as specs da classeStack
e um describe aninhado para agrupar especificamente as specs do método
Stack#push. Omodocomoestamosusandoo describeaninhadoparaagru-
parostestesrelacionadossomenteaocomportamentodométodo Stack#pushé
apenasumaconven ção,poderíamosterfeitosemusarum describeaninhado:
describe Stack do
it "puts an element at the top of the stack" do
stack = Stack.new
stack.push(1)
stack.push(2)
expect(stack.top).to eq(2)
end
end
Maisparafrentevamosfalarmaisdessaconven ção.Vamosagoraentenderpara
queserveométodo it.
Ométodo itserveparacriarmosumtestedefato.Dentrodoblocoquepas-
samosparao itéondeéescritoumexemplodecomoonossocódigodevese
comportaremumdeterminadocontexto.Noexemploquefizemosacimatemoso
seguinteteste:
it "puts an element at the top of the stack" do
stack = Stack.new
24

## Página 39

CasadoCódigo Capítulo3. IntroduçãoaobásicodoRSpec
stack.push(1)
stack.push(2)
expect(stack.top).to eq(2)
end
Percebacomoocódigoescritoéapenasumachamadadométodo it.Eleestá
sendochamadocomdoisargumentos.Oprimeiroéastringquecontémumades-
criçãodoteste. Osegundoargumentoéumblococomocódigodotesteemsi,
delimitadopelo doe end.
Aterceira,eúltimapartebásicadeumtestecomRSpec,éaasser ção,queéonde
verificamosseonossocódigosecomportoudomodoesperado.NoRSpecasasser-
çõessãofeitascom expectations.Notesteacimaaexpectationqueestamosfazendo
éaparteondechecamosseotopodapilhacontémoelemento2:
expect(stack.top).to eq(2)
Aestruturadeumaexpectationsegueaseguinteforma:
expect(actual).to matcher(expected)
ou:
# usando to_not
expect(actual).to_not matcher(expected)
# usando not_to
expect(actual).not_to matcher(expected)
Onde actualéoobjetodoqualvocêestátestandoalgumcomportamento,
expectéummétododoRSpecparainiciarumaexpectatione matcheréum
objetoquesegueoprotocolodo RSpec::Matcherseserveparatestardefatoo
comportamentoesperadodoseuobjeto.
Nocasodonossotesteanterior,omatcherusadofoio eq,quetestaseoseu
objetoéigualaovaloresperadousandoooperador ==.Ouseja,oquefizemosno
nossotestefoiverificarseovalorretornadopelométodo stack.toperaigualao
valoresperado,2.
25

## Página 40

3.2. PorquêexistemtantosmatchersnoRSpec CasadoCódigo
Diferentes sintaxes de expectation: expect X should
SevocêjáviuouescreveualgumtestecomRSpecantesdelereste
livro,éprovávelquevocêtenhavistoasintaxeantigadoRSpecparacriar
expectations,queerausandoométodo should.
Antigamente, opadrãodeexpectationsdoRSpeceradoseguinte
modo:
stack.top.should eq(2)
aoinvésde:
expect(stack.top).to eq(2)
Naversão2.11doRSpecanovasintaxe expectfoiintroduzida,e
desdeentãoéasintaxerecomendadapeloequipecoredoRSpec.
Se você tiver interesse, você pode ver o porquê dessa mu-
dança em um post (http://myronmars.to/n/dev-blog/2012/06/
rspecs-new-expectation-syntax) no blog do Myron Marston, atual
mantenedordoRSpec.
Vistotudoisso,agoravocêjáconheceaestruturabásicadeumtestecomRSpec.
Useo describeparaagruparosseustestesdemodológico.Useo itparaescrever
umtesteemsi. Eporfim,useos RSpec::Matchersparaverificarocomporta-
mentoesperadodentrodoteste.
AgoravamosdarumaolhadanosmatchersquevemporpadrãocomoRSpec.
3.2 P orquê existem tantos matchers no RSpec
AntesdecomeçarmosaverosdiversosmatchersqueoRSpecnosofereceporpadrão,
valeapenaentendermosumadasvantagensemtertantosmatchersassim.Paraisso,
vamoscriarumpequenoprojetoefazerumtesteparaele.
Vamosdesenvolverumobjetoquesirvacomoumsacodepalavras,ondevocê
pode colocar palavras dentro dele e depois verificar quantas palavras tem den-
tro do saco. Comece criando um diretório para o nosso projeto, chamado de
bag_of_words:
$ mkdir bag_of_words
26

## Página 41

CasadoCódigo Capítulo3. IntroduçãoaobásicodoRSpec
$ cd bag_of_words
CrieumGemfileusandoobundler:
$ bundle init
ColoqueoRSpecnoGemfile:
source "https://rubygems.org"
gem "rspec"
EfinalmenteinstaleoRSpecusandoobundler:
$ bundle install
Sobre o Bundler
Casovocêaindanãoconhe çaoBundler,eleéumprojetomuitofa-
mosonacomunidadeRubyfeitoparagerenciarasdependênciasdoseu
projeto.
Parafazerisso,vocêdevecriaumarquivochamado Gemfileelistar
neleasgemscomsuasversõesdasquaisoseuprojetodepende.Baseado
nessearquivo Gemfile,oBundlerinstalaasgemsnecessárias,resol-
vendoasversõesdelasdeacordocomoquevocêconfigurou.
VistoqueoBundlerédistribuídocomoumagem,instalá-loébem
fácil,bastavocêutilizaroRubyGems,fazendooseguintecomandono
console:
$ gem install bundler
ComoRSpecinstalado,vamoscriaraestruturadediretóriosdonossoprojeto,
começandopelo lib:
$ mkdir lib
EagoracrieaestruturadediretórioearquivospadrãodoRSpecusandoose-
guintecomando:
27

## Página 42

3.2. PorquêexistemtantosmatchersnoRSpec CasadoCódigo
$ rspec --init
create spec/spec_helper.rb
create .rspec
Percebaqueaorodarocomando rspec --init,elecrioudoisarquivose
umdiretório. Odiretório specéondedevemoscolocarnossostestes. Oarquivo
spec/spec_helper.rbéondesãocolocadasasconfiguraçõescomunsentreto-
dosnossostestes.Efinalmentenoarquivo .rspecéondepodemosdeixarsalvasas
flagsqueserãopassadasparaocomando rspecquandoformosrodarnossostestes.
Comaestruturadediretóriospronta,vamoscome çaradesenvolvernossopequeno
projeto.
Comece criando um arquivo de teste chamado
spec/bag_of_words_spec.rb:
$ touch spec/bag_of_words_spec.rb
Vamos fazer um teste para especificar que é possível colocar pala-
vras no nosso saco de palavras. Escreva o seguinte teste no arquivo
spec/bag_of_words_spec.rb:
require "spec_helper"
require "bag_of_words"
describe BagOfWords do
it "is possible to put words on it" do
bag = BagOfWords.new
bag.put("hello", "world")
expect(bag.words.size).to eq(2)
end
end
Vamos entender o que fizemos nesse teste. Primeiro demosrequiredo
spec_helper, aquele arquivo gerado automaticamente pelo comandorspec
--init. Nessearquivoficamasconfiguraçõesgeraisdanossasuítedetestes,en-
tãofizemos requiredeleparagarantirqueessasconfiguraçõessejamaplicadasao
nossoteste.
28

## Página 43

CasadoCódigo Capítulo3. IntroduçãoaobásicodoRSpec
Depoisfizemos requiredoarquivo bag_of_words,queaindanemexiste,
maséondecolocaremosocódigodanossaclasse.
Porfim, notesteemsi, nóssimplesmentecriamosumobjeto bag, coloca-
mos duas palavras dentro dele e testamos se o tamanho da lista retornada por
bag.words.sizeéiguala2.
Rodeotesteeverifiquequeeleestáquebrando:
$ bundle exec rspec --format documentation
(...)
cannot load such file -- bag_of_words (LoadError)
Otestequebracomumamensagemquenosfalaqueoproblemaéquenãofoi
possíveldar requiredoarquivo bag_of_words. Claro,aindanãoocriamos.
Vamosdaroprimeiropassonatentativadefazerotestepassar,criandoessearquivo
comumaclasse BagOfWordsecomométodo BagOfWords#put.Paraisso,crie
oarquivo lib/bag_of_words.rbeescrevaoseguintecódigonele:
class BagOfWords
attr_reader :words
def initialize
@words = []
end
def put(*words)
# TODO
end
end
Comaimplementaçãoacimafeita,combasicamenteum initializeeum
métodoputqueaindavamosimplementar,podemosrodarostestesnovamentee
verofeedbackparaopróximopasso:
$ bundle exec rspec --format documentation
BagOfWords
is possible to put words on it (FAILED - 1)
Failures:
29

## Página 44

3.2. PorquêexistemtantosmatchersnoRSpec CasadoCódigo
1) BagOfWords is possible to put words on it
Failure/Error: expect(bag.words.size).to eq(2)
expected: 2
got: 0
(compared using ==)
Nossotestequebroucomaseguintemensagem:
Failure/Error: expect(bag.words.size).to eq(2)
expected: 2
got: 0
Pelamensagempodemosverqueoesperadoeraqueo sizedo array words
fosse2,masveio0.Amensagemestácorretaeestádeacordocomnossoobjetivo
final,maselapodeficarmelhor. Oquequeremostestaréqueexistem2palavras
na bag,enãoqueoarray wordstem2elementos. Percebaqueosdoismodos
depensardãonomesmoresultado,maspensarem“palavrasdentrodosaco”está
maispertododomíniodonosssoproblemadoque“númerodeelementosdeum
array”.Podemosmelhoraraexpressividadedonossotesteusandoummatchermais
apropriadoparaessecontexto,quenessecasoseriao Have Matcher.
Seguindoessaidéia,reescrevaaexpectationdonossotesteparaficarassim:
require "spec_helper"
require "bag_of_words"
describe BagOfWords do
it "is possible to put words on it" do
bag = BagOfWords.new
bag.put("hello", "world")
expect(bag).to have(2).words
end
end
Erodeotestenovamente:
$ bundle exec rspec --format documentation
30

## Página 45

CasadoCódigo Capítulo3. IntroduçãoaobásicodoRSpec
(...)
Failures:
1) BagOfWords is possible to put words on it
Failure/Error: expect(bag).to have(2).words
expected 2 words, got 0
Percebacomoamensagemdeerromudou.Amensagemagorafala:“expected
2words,got0”.Amensagemagorafazbemmaissentidoemrelaçãoaodomíniodo
nossoproblema!Percebatambémcomoficadiferenteleranovaexpectationcom-
paradaaantiga:
# antiga
expect(bag.words.size).to eq(2)
# nova
expect(bag).to have(2).words
Nãosóamensagemdeerroficoumaisexpressivacomotambémoprópriocó-
digodonossotestetambémficou!Essaéavantagemdeseusaromatchercorreto.É
porissoqueoRSpecvemcommaisde30matchers,paraquenossostestessejamex-
pressivoseparaquepossamosaplicaraidéiadoBDDdeescrevertestesquesirvam
comoespecificaçãoedocumentaçãodonossocódigo.
Bom,agoraquejáestamosusandoomatchercorreto,valeapenafazermoso
testepassar. Bastafazermoscomqueométodo BagOfWords#putconcateneos
seusargumentosnoarrayde @wordsinterno.Modifiqueessemétodonoarquivo
lib/bag_of_words.rbparaficarassim:
class BagOfWords
attr_reader :words
def initialize
@words = []
end
def put(*words)
@words += words
end
end
31

## Página 46

3.2. PorquêexistemtantosmatchersnoRSpec CasadoCódigo
Agoraaorodarostestes,vemosqueelespassam:
$ bundle exec rspec --format documentation
BagOfWords
is possible to put words on it
Finished in 0.00139 seconds
1 example, 0 failures
Agoraestamosprontosparadarumaolhadanosbuilt-inmatchersdoRSpec(que
sãoosmatcherspadrãodoRSpec).
Curiosidade: a manipulação do $LOAD_P ATH feita pelo RSpec
Paraentenderessacuriosidade,vocêdevesaberqueemRubyaofazer require
"file_path",oRubyvaiprocuraroarquivo file_pathdentrodavariávelglobal
$LOAD_PATHevaicarregá-loseachar.
Notestequefizemosacima,vocêdeveselembrarquedemos requiredo
spec_helperedoarquivo bag_of_words:
# spec/bag_of_words_spec.rb
require "spec_helper"
require "bag_of_words"
describe BagOfWords do
# (...)
end
AolerocódigodetestesdeoutrosprojetoscomRSpec,épossívelquevocêveja
queapessoaestáinserindoodiretório lib/explicitamenteno $LOAD_PATHpara
conseguirdar requireemumarquivodessediretório.Umexemplodessetipode
códigopoderiaserassim:
require "spec_helper"
$LOAD_PATH.unshift File.join(File.dirname(__FILE__), "..", "lib")
require "bag_of_words"
Hátemposatráseumepergunteiporquequealgumaspessoasficavamcolo-
candoodiretório lib/explicitamentedentrodo $LOAD_PATHeoutrasnão.Acon-
tecequenoRSpec,édesnecessáriofazerisso,porqueelejáfazissopornós.Issoé
32

## Página 47

CasadoCódigo Capítulo3. IntroduçãoaobásicodoRSpec
feitopelorspec-core(https://github.com/rspec/rspec-core/tree/v2.13.1/),noarquivo
lib/core/load_path.rb:
require 'rspec/core/ruby_project'
RSpec::Core::RubyProject.add_to_load_path('lib', 'spec')
Portanto,nãoesque ça,nãoénecessáriocolocarodiretório lib/e spec/ex-
plicitamenteno $LOAD_PATH,oRSpecjáfazissopornós.
3.3 C onhecendo os RSpec built-in matchers
UmmatchernoRSpecéumobjetoqueserveparaverificarocomportamentoes-
peradononossoteste.EleéusadoparamontarumaexpectationdoRSpecdedois
modosdiferentes:
expect(actual).to matcher(expected)
expect(actual).to_not matcher(expected)
Umexemploparacadaumdosmodosdeexpectationacimapodeser:
expect(1).to eq( 1)
expect(1).to_not eq(2)
Comomencionadonase çãoanterior,oRSpecvemcommuitosbuilt-inmat-
chersparanosajudaraescrevertestesexpressivos. Vamosdarumaolhadaneles,
começandopelosmaisbásicos,os "be matchers”.
3.4 M atchers relacionados a truthy e falsy
Os be matchersservemparavocêtestarseumobjetoéavaliadocomo trueou
false.Vocêpodeusá-losdoseguintemodo:
expect(obj).to be_true # passa se obj é truthy (não nil ou não false)
expect(obj).to be_false # passa se obj é falsy (nil ou false)
expect(obj).to be_nil # passa se obj é nil
expect(obj).to be # passa se obj é truthy (não nil ou não false)
Notequeosbematchersjáseriamosuficienteparafazerqualquertipodeteste
proseusoftware.Porexemplo,poderíamosre-escreveroteste:
33

## Página 48

3.5. Osmatchersdeequidade CasadoCódigo
it "is possible to put words on it" do
bag = BagOfWords.new
bag.put("hello", "world")
expect(bag).to have(2).words
end
para:
it "is possible to put words on it" do
bag = BagOfWords.new
bag.put("hello", "world")
expected = (bag.words.size == 2)
expect(expected).to be_true
end
Masusaros“bematchers”paratudo,comousamosacima,prejudicariaasemân-
ticadosnossostesteseéporissoquetemosoutrosmatchers.
3.5 O s matchers de equidade
Os equality matchersservemparaverificarseumobjetoéigualaoutroobjeto.
Existemaisdeummatcherparaessetipodeverificaç ãoporquenoRubyexistemais
deummododechecaraequidadeentredoisobjetos,quesãoosseguintes:
a.equal?(b) # object identity - a e b se referem ao mesmo objeto
a.eql?(b) # object equivalence - a e b tem o mesmo valor
a == b # object equivalence - a e b tem o mesmo valor com conversão
# de tipo
OsmatchersqueoRSpectemparaverificarequidadesão:
expect(a).to equal(b) # passa se a.equal?(b)
expect(a).to be(b) # passa se a.equal?(b)
expect(a).to eql(b) # passa se a.eql?(b)
expect(a).to eq(b) # passa se a == b
34

## Página 49

CasadoCódigo Capítulo3. IntroduçãoaobásicodoRSpec
3.6 M atchers relacionados a arrays
ORSpecnosoferecealgunsmatchersespecíficosparaverificaç ãodearrays.Opri-
meiroéo MatchArray.Essematcheréusadoparaverificarseumarrayé“igual”
aoutro,independentedaordemdoselementosdoarray.Segueumexemplodeuso
dessematcher:
array = [1, 2, 3, 4]
expect(array).to match_array([1, 2, 3, 4])
expect(array).to match_array([4, 3, 2, 1])
expect(array).not_to match_array([1, 2, 3])
expect(array).not_to match_array([1, 2, 3, 4, 5])
Outromatcherrelacionadoaverificaç ãodearrayséo Include Matcher.
Vocêpodeusá-loparaverificararelaçãodepertinênciaentreumoumaiselementos
eumdeterminadoarray.Segueumexemplodeusodessematcher:
array = [1, 2, 3, 4]
expect(array).to include(1)
expect(array).to include(1, 2, 3)
expect(array).to include(1, 2, 3, 4)
expect(array).not_to include(0)
expect(array).not_to include(5)
expect(array).not_to include(5, 6, 7, 8)
expect(array).not_to include([1, 2, 3, 4])
Porfim,existemtambémosmatchers start_withe end_withqueservem
paraverificarseumarraycome çaouterminacomumasequênciadeelementos.
Segueumexemplodeusodessesmatchers:
array = [1, 2, 3, 4]
expect(array).to start_with(1)
expect(array).to start_with(1, 2)
expect(array).not_to start_with(2)
expect(array).to end_with(4)
35

## Página 50

3.6. Matchersrelacionadosaarrays CasadoCódigo
expect(array).to end_with(3, 4)
expect(array).not_to end_with(3)
Matchers relacionados a hashes
ParaverificarHashes,oRSpecnosofereceo Include Matcher,omesmo
matcherquevimosnaverificaçãodearrays.Segueumexemplodeusodessematcher
comhashes:
hash = { a: 7, b: 5 }
# você pode usar para verificar se um hash tem uma ou mais chaves
expect(hash).to include(:a)
expect(hash).to include(:a, :b)
# você pode usar para verificar se um hash tem um ou mais pares de
# chave - valor
expect(hash).to include(a: 7)
expect(hash).to include(b: 5, a: 7)
expect(hash).not_to include(:c)
expect(hash).not_to include(a: 11)
expect(hash).not_to include(a: 13, c: 11)
expect(hash).not_to include(:c, :d)
Matchers relacionados a strings
ORSpecoferecealgunsmatchersrelacionadosastrings,sendoquealgunsde-
lessãoosmesmosusadosparaverificararrays.Vamoscome çarolhandoo Match
Matcher,queserveparaverificarovalordeumastringdeacordocomumaexpres-
sãoregular:
string = "hugo barauna"
expect(string).to match(/hugo/)
expect(string).to match(/araun/)
expect(string).not_to match(/barao/)
expect(string).not_to match(/hugs/)
Agoraseguemexemplosdosmatchersusadosporstringsearrays,come çando
pelo include:
36

## Página 51

CasadoCódigo Capítulo3. IntroduçãoaobásicodoRSpec
string = "hugo barauna"
expect(string).to include("h")
expect(string).to include("hugo")
expect(string).to include("hugo", "bara")
expect(string).not_to include("barao")
expect(string).not_to include("hugs")
Porfim,vocêtambémpodeusarosmatchers start_withe end_withcom
strings:
string = "hugo barauna"
expect(string).to start_with("hugo")
expect(string).not_to start_with("barauna")
expect(string).to end_with("barauna")
expect(string).not_to end_with("hugo")
Predicate matchers
UmdostiposdematchersmaisfamososdoRSpecsãoos Predicate Matchers.
Paraentenderessesmatchersvamoscome çarestudandooseguinteexemplo.
Imaginequevocêestádesenvolvendoumaaplicaçãodee-commerceetemuma
classechamada Cart.Essaclassetemummétododeinstânciachamado empty?.
Paraespecificaressemétodo,vocêpoderiafazeroseguinteteste:
describe Cart do
describe "#empty?" do
it "returns true when the cart has no products" do
cart = Cart.new
expect(cart.empty?).to be_true
end
end
end
Acontecequetodavezqueumobjetotemumpredicatemethod(métodoque
terminacom?),oRSpecgeraummatcherespecíficoparaessemétododinamica-
mente.Nocasodoexemploacima,aoinvésdefazer:
37

## Página 52

3.6. Matchersrelacionadosaarrays CasadoCódigo
expect(cart.empty?).to be_true
Vocêpodeutilizarumpredicatematcherparare-escreverotestedoseguinte
modo:
expect(cart).to be_empty # chama o método cart.empty?
OqueoRSpecfazégerarparatodopredicatemethodchamado method_name?
ummatcherchamado be_method_name.Foioquefizemosacimaquandousamos
omatcher be_emptyreferenteaopredicatemethod empty?.Essetipodematcher
ébemusadoporqueospredicatemethodssãoumaconven çãobastanteusadana
comunidadeRuby.
Os predicate matchers ainda tem outras três formas. A segunda forma é
quandooRSpecgeraummatcher have_method_nameparamétodosdaforma
has_method_name?. Um exemplo desse caso pode ser visto para o método
has_key?deumhash:
hash = { key: 1 }
expect(hash).to have_key(:key) # chama o método hash.has_key?(:key)
Vocêpodeutilizaressaformadepredicatematcherparaosseusprópriosob-
jetos também. Imagine o exemplo da classeCart, ela poderia ter o método
has_products?evocêpoderiaespefificaressemétododoseguintemodo:
describe Cart do
describe "#has_products?" do
it "returns true if it has products" do
product = Product.new
cart = Cart.new(product)
expect(cart).to have_products # chama o método cart.has_products?
end
end
end
A terceira e quarta formas dos predicate matchers são os matchers
be_a_method_name e be_an_method_name. Para entender essas últimas
formas,imaginequesuaclasse Carttemosmétodos thing?e object?,e
ambosdevemretornar true. Vocêpodeespecificaressesmétodosdoseguinte
modo:
38

## Página 53

CasadoCódigo Capítulo3. IntroduçãoaobásicodoRSpec
expect(cart).to be_a_thing # chama o método cart.thing?
expect(cart).to be_an_object # chama o método cart.object?
Matchers para exceptions
ORSpecofereceummatcherparavocêespecificarqueummétodolevantauma
determinadaexception,éo RaiseError Matcher. Vocêpodeusá-locomométodo
raise_erroreseualias raise_exception:
expect { raise }.to raise_error
expect { raise }.to raise_exception
Percebaquediferentementedomodopadrãodeescreverumaexpectation,o
argumentoqueépassadoparaométodo expectéumbloco:
# correto
expect { raise }.to raise_error
# correto
expect do
raise
end.to raise_error
# errado
expect(raise).to raise_error
Épossívelverificartambémseaexceptionlevantadaédeumaclasseespecífica:
expect { raise RuntimeError }.to raise_error(RuntimeError)
expect { raise StandarError }.to_not raise_error(RuntimeError)
Porfim,vocêpodeverificartambémamensagemdaexceptionlevantada:
expect { raise 'error message ' }.to raise_error('error message ')
expect { raise 'wrong message ' }.to_not raise_error('error message ')
Matchers para comparação de números
Paracompararseumvaloréigualaumcertonúmerovocêdeveusaro eq matcher
: expect(hugo_age).to eq(27).Mas,eparacompararseumnúmeroémenor
oumaiorqueoutro?Paraessescasosvocêtemosseguintesmatchers:
39

## Página 54

3.6. Matchersrelacionadosaarrays CasadoCódigo
expect(7).to be < 10
expect(7).to be > 1
expect(7).to be <= 7
expect(7).to be >= 7
Matchers relacionados a números float
Fazeraverificaçãodenúmerosfloatpodeserproblemático,poisdevidoaparte
fracionáriadonúmero,nãodáparasimplesmenteutilizarummatcherdeequidade.
Imagineporexemploquevocêvoltouparaasaulasdegeometriaplanaequercon-
firmarquevocêsabequeovalordePié3.14:
expect(Math::PI).to eq(3.14) # executa Math::PI == 3.14
Acontecequeotesteacimavaifalhar,porquePinãoéexatamenteiguala3.14,ele
éaproximadamente3.14.UmaaproximaçãodePicommaiscasasdecimaispoderia
serporexemplo3.141592653589793.
Comoproblemaacimaemmente,oRSpecnosofereceo BeWithin matcher,que
serveparafazercomparaçõesentrenúmerosdeformaaproximada.Poderíamosre-
escreverotesteacimadoseguintemodocomessematcher:
expect(Math::PI).to be_within(0.01).of(3.14)
Oqueotesteacimaestáfazendoécompararseovalorde Math::PIémaior
ouiguala 3.14 - 0.01oumenorouigualaovalorde 3.14 + 0.01.Ouseja,
paraumaexpectationgenéricanoseguinteformato:
expect(actual).to be_within(delta).of(expected)
Oqueessematcherfazéverificarseaseguinteexpressãoéverdadeira:
(expected - delta) <= actual <= (expected + delta)
Matchers para ranges
ParaversõesdoRubyapartirda1.9,oRSpecofereceummatcherparaverificar
seumoumaiselementospertecemaumdadorange,éo Cover Matcher.Vocêpode
usá-lodaseguinteforma:
range = (1..10)
40

## Página 55

CasadoCódigo Capítulo3. IntroduçãoaobásicodoRSpec
expect(range).to cover(1)
expect(range).to cover(10)
expect(range).to cover(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
expect(range).to cover(5, 6, 7, 8)
Matchers para verificar a classe de um objeto
Sevocêestiverescrevendoalgumtestequepreciseverificardequalclasseseu
objetoé,vocêpodeusarosmatchers BeAnInstanceOfe BeAKindOf.Elesfun-
cionamdoseguintemodo:
# be_an_instance_of verifica se o objeto é uma instância da classe dada
expect(5).to be_an_instance_of(Fixnum)
expect(5).not_to be_an_instance_of(Numeric)
expect(5).not_to be_an_instance_of(String)
# be_a_kind_of verifica se o objeto é uma instância da classe dada ou
# de uma subclasse da classe dada
expect(5).to be_a_kind_of(Fixnum)
expect(5).to be_a_kind_of(Numeric)
expect(5).to be_a_kind_of(Object)
expect(5).not_to be_a_kind_of(String)
Matchers para verificar tamanho de coleção
Sevocêquerchecarotamanhodeumacole ção,vocêpodeusaro Have Matcher.
Nase ção 3.2nósvimosumexemplodeusodessematcherquandoescrevemoso
seguinteteste:
describe BagOfWords do
it "is possible to put words on it" do
bag = BagOfWords.new
bag.put("hello", "world")
expect(bag).to have(2).words
end
end
41

## Página 56

3.6. Matchersrelacionadosaarrays CasadoCódigo
Vamosentendermelhoroquealinha expect(bag).to have(2).wordsfaz
pordebaixodospanos:
1) aprimeiracoisaqueo Have Matcherfazédeterminarseoobjetosendotes-
tado é uma coleção ou se ele contém uma coleção. Para fazer essa checa-
gemelevêométodoquefoipassadoparao have,nocasoacimafoiomé-
todo words, echecaseoobjetosendotestadorespondeparaessemétodo:
bag.respond_to?(:words);
2) comooobjeto bagrespondeparaométodo words,o Have Matcherinfereque
oobjeto bagcontémumacoleçãoeésobreessacole çãoquesequerverificaro
tamanho;
3) finalmente,o Have Matcherverificaotamanhodessacole çãodeacordocomo
tamanhopassadonaexpectation.Comonocasoacimaotamanhopassadopara
omatcherfoi2( have(2).words),eleexecuta bag.words.size == 2.
O Have Matcherprecisafazertodaalógicaacimaporqueeleserveparatestaro
tamanhodeumacole çãoemdoiscenários:
• quandovocêquerverificarotamanhodeumacoleçãocontidaporumobjeto,
comonocasoacima;
• quandovocêquerverificarotamanhodeumacoleçãodiretamente.
Abaixosegueumexemplodeusodessematcherparaverificarotamanhodeuma
coleçãodiretamente:
collection = [1, 2, 3]
expect(collection).to have(3).itens
Umoutrodetalheinteressantesobreessematcheréquequandovocêestáfa-
zendoumtestedeumacole çãodiretamente,vocêpodepassarqualquermétodopara
ele:
collection = [1, 2, 3]
# todos os modos abaixo funcionam
expect(collection).to have(3).items
expect(collection).to have(3).children
expect(collection).to have(3).things
42

## Página 57

CasadoCódigo Capítulo3. IntroduçãoaobásicodoRSpec
Apesardequalquermétodoquevocêpassarparao Have Matcherfuncionar
quandooobjetosendotestadoéumacole ção,éimportantequevocêescolhaomé-
todoquemelhorrepresenteasemânticadodomíniodoseuproblema.
Porexemplo,sevocêestiverfazendoalgumaaplicaç ãoqueésobreprocessa-
mentodetexto,fazmuitomaissentidovocêescreverumtestecomo:
words = "hugo"
expect(words).to have(4).letters # letters é um termo do domínio
# do problema
doqueumtestecomo:
words = "hugo"
expect(words).to have(4).items # itens não é um termo do domínio
# do problema
Escolherométodocorretocomomostramosacimatemduasvantagens.Apri-
meiraéqueaoescrevercódigodetestequemelhorrepresentaoseudomínio,você
estáseguindoapráticade“linguagemubíqua”doDomainDrivenDesign-DDD,
deixandoseutestemaisparecidocomumadocumentaç ãoetambémfacilitandoa
criaçãodeumdicionáriodetermospadrãoparaoseuprojeto.
Asegundavantagempodeservistapelavariaç ãoentreamensagemdeerrono
teste.Elaésempreumótimoindíciosevocêestánocaminhodeescreverumbom
teste.
Porexemplo,otesteaseguirquebracomaseguintemensagem:
words = "hugo"
expect(words).to have(3).items
# Failure/Error: expect(words).to have(3).items
# expected 3 items, got 4
Jáomesmotesteescritodeummodomelhor,quebracomaseguintemensagem:
words = "hugo"
expect(words).to have(3).letters
43

## Página 58

3.6. Matchersrelacionadosaarrays CasadoCódigo
# Failure/Error: expect(words).to have(3).letters
# expected 3 letters, got 4
Percebacomoamensagemdeerroficoumelhorquandousamosummétodo
maisapropriadoparadescreverainten çãodonossoteste.
Porfim,vocêpodeusarmaisduasformasdessematcher,quesãoasformas
have_at_leaste have_at_most.Segueumexemplousandoessasduasformas:
collection = [1, 2, 3, 4, 5]
expect(collection).to have_at_least(3).elements
expect(collection).to have_at_most(5).elements
Matcher para verificar mudança de estado ou valor
Imaginequevocêestádesenvolvendoumjogoeprecisecriarumobjetoque
temumamáquinadeestados,porexemplo,paratrackearseojogojácome çouou
não.Vocêquerqueoobjetotenhaummétodo Game#startqueaoserdisparado,
oestadointernodojogodevemudarde :initialpara :started. Vocêpode
especificaressecomportamentodoseguintemodo:
describe Game do
describe "#start" do
it 'changes the game state from :initial to :started ' do
game = Game.new
expect {
game.start
}.to change { game.state }.from(:initial). to(:started)
end
end
end
Neexemploacimausamoso Change Matcherem:
expect {
game.start
}.to change { game.state }.from(:initial).to(:started)
paraverificarqueovalordoestadodoobjeto gamemudade :initialpara
:startedquandoaação game.startforexecutada.
44

## Página 59

CasadoCódigo Capítulo3. IntroduçãoaobásicodoRSpec
Comovocêpôdevernoexemploacima, o Change Matcher podeserusado
quandovocêquerverificarqueaexecuçãodeumblocodecódigocausaumamu-
dançadeestadodeumobjeto.
Seguemmaisalgunsexemplosdeusodo Change Matcher:
# verifica que ao rodar Counter.increment o valor de Counter.count
# é modificado em duas unidades
expect {
Counter.increment
}.to change { Counter.count }.by(2)
# verifica que ao tentar salvar um user com um atributo inválido
# o valor de User.count não é modificado
expect {
invalid_attributes = { name: nil }
user = User.new(invalid_attributes)
user.save
}.to_not change(User, :count)
# verifica que ao adicionar alguns jogadores ao objeto team, o valor
# de team.size é modificado por pelo menos uma unidade
expect {
team.add_players(some_players)
}.to change(team, :size).by_at_least(1)
Pensenessetipodematchercomoumverificadorqueanalisaráovalorantese
depoisdealgumaação.
Outros matchers padrão do RSpec
Pronto,jávimosamaioriadosmatcherspadrãoquevemcomoRSpec. Mas,
comosãomuitosemuitasvariações,nãovaleapenavertodososdetalhesdetodos
osmatchersquevemcomoRSpecdeumavezsó.Porissoconvidovocêadepoisdar
umaboanavegadapeladocumentaçãodoRSpecparavermaissobreosmatchers
padrão.
Vocêpodeveressadocumentaçãodeduasformas, noRelish(https://www.
relishapp.com/rspec/rspec-expectations/v/2-14/docs/built-in-matchers),queéuma
documentaçãomaisaltonível. Ou,vocêpodeverdiretonocódigodoRSpec,no
seguintelinkdoGithub: https://github.com/rspec/rspec-expectations/blob/v2.13.0/
lib/rspec/matchers.rb.
45

## Página 60

3.7. Custommatchers CasadoCódigo
Valeapenaguardaresseslinks,poisjuntocomoquevimosnestelivro,elessão
umaótimareferênciasobreosmatcherspadrãodoRSpec.
AgoraquevocêjáleubastantesobreosmatchersquevemcomoRSpec,descanse
umpouquinho,poisaseguirvocêiráaprenderaescreverosseusprópriosmatchers!
3.7 C ustom matchers
NaseçãoanteriornósaprendemossobreosmatcherspadrãodoRSpecevimosque
existemmuitosdeles. MasmesmocomoRSpecnosoferecendotantosmatchers,
asvezespodemosprecisardemais. Asvezestemosqueescrevernossospróprios
matchers.Vamosverquandoissopodesernecessário.
Imaginequevocêestátrabalhandoemumaaplicaçãodee-commerce.Vocêestá
encarregadodetrabalharnafuncionalidadedecategorizaçãodeprodutos.Oescopo
dafuncionalidadedizque:
• umacategoriacontémumaoumaissubcategorias;
• umasubcategoriacontémumoumaisprodutos;
• umacategoriacontémtodososprodutoscontidosporsuassubcategorias.
Vamospensarnumexemploparaoescopoacima.Nanossaaplicaç ãopodeexis-
tirumacategoriachamada“eletrônicos”. Essacategoriapodeconterduassubcate-
gorias,taiscomo“computadores”e“celulares”.Asubcategoriacomputadorespode
conteroprodutoMacBookeasubcategoriacelularespodeconteroprodutoiPhone.
Logo,acategoriaeletrônicosdeveconterosprodutosMacBookeiPhone.
Atéentãovocêjátemocódigodeduasclasses.Ocódigodaclasse Category:
class Category
attr_reader :subcategories
attr_reader :name
def initialize(name)
@name = name
@subcategories = []
end
def add_subcategories(*subcategories)
# TODO
46

## Página 61

CasadoCódigo Capítulo3. IntroduçãoaobásicodoRSpec
end
end
Eocódigodaclasse Subcategory:
class Subcategory
attr_reader :products
def initialize(name)
@name = name
@products = []
end
def add_product(product)
@products << product
end
end
Agoraimaginequevocêpreciseescreverumtesteunitárioparaespecificarque
umacategoriacontémtodososprodutosdesuassubcategorias.Poderíamoscome çar
escrevendoessetestedoseguintemodo:
describe Category do
it "contains all the products of its subcategories"
end
Nosetupdessetestevamoscriarumobjetoparaacategoria "eletronics",
criarobjetosparaassubcategorias "computers"e "cell phones"eadicionar
umprodutoparacadasubcategoria:
describe Category do
it "contains all the products of its subcategories" do
eletronics = Category.new("eletronics")
computers = Subcategory.new("computers")
cell_phones = Subcategory.new("cell phones")
computers.add_product("MacBook")
cell_phones.add_product("iPhone")
end
end
Agorapodemosadicionaressassubcategoriasacategoria "eletronics"eve-
rificarqueosprodutosdelasestãocontidosnacategoria "eletronics":
47

## Página 62

3.7. Custommatchers CasadoCódigo
describe Category do
it "contains all the products of its subcategories" do
eletronics = Category.new("eletronics")
computers = Subcategory.new("computers")
cell_phones = Subcategory.new("cell phones")
computers.add_product("MacBook")
cell_phones.add_product("iPhone")
eletronics.add_subcategories(computers, cell_phones)
eletronics_products = eletronics.subcategories.map { |sub|
sub.products
}
eletronics_products.flatten!
expect(eletronics_products).to include("MacBook", "iPhone")
end
end
Percebacomoainten çãodalógicadeverificaçãodessetestenãoestá100%clara:
eletronics_products = eletronics.subcategories.map { |sub|
sub.products
}
eletronics_products.flatten!
expect(eletronics_products).to include("MacBook", "iPhone")
Sódebateroolhonessecódigonãodaparadizerqueainten çãodeleéverificar
queacategoria "eletronics"contémosprodutos "MacBook"e "iPhone".
Esseéoprimeiropontoamelhorar.
Osegundopontoamelhorarnóspodemosidentificaraorodarotesteelersua
mensagemdeerro:
1) Category contains all the products of its subcategories
Failure/Error:
expect(eletronics_products).to include("MacBook", "iPhone")
expected [] to include "MacBook" and "iPhone"
A mensagem de erro não fala explicitamente que o erro é que a categoria
"eletronics"nãocontémnenhumdosprodutosqueeladeveriaconter.Lembre-
sequeamensagemdeerrodeumtesteémuitoimportante,poisumamensagemde
erroclarapodenosajudararesolvermaisrápidoumtestequeestáquebrado.
48

## Página 63

CasadoCódigo Capítulo3. IntroduçãoaobásicodoRSpec
Entãopelomenosessesdoispontosnóspodemosmelhorarnonossoteste,a
clarezadainten çãodalógicadeverificaç ãoeamensagemdeerrodoteste. Para
fazeressamelhorapodemosescreverum custom matcherdoRSpeceutilizá-lopara
refatoraraverificaçãodonossotesteparaficarassim:
expect(eletronics).to contain_products("MacBook", "iPhone")
VamosaprenderacomofazerumcustommatcherdoRSpec.
Escrevendo um custom matcher do RSpec
ORSpecnosofereceumaDSLparaescreverumcustommatcherdemodobem
simples.ParaentenderessaDSL,vamosescreverumcustommatcherqueservepara
verificarseumnúmeroémúltiplode7.Essematcherpoderáserusadodoseguinte
modo:
expect(21).to be_a_multiple_of(7)
Oprimeiropassoparaescrevermosocustommatcheracimaéutilizarométodo
RSpec::Matchers.definedaDSLdoRSpec:
RSpec::Matchers.define :be_a_multiple_of
Ométodo definecriaummétodonomeadosegundooargumentoquefoi
passadoparaele,nonossocasoométodo be_a_multiple_of. Continuandoa
seguiraDSL,énecessáriopassarumblocoparaessemétodo:
RSpec::Matchers.define :be_a_multiple_of do |expected|
end
Reparenoargumentoqueépassadoparaobloco,o expected.Esseargumento
éomesmoqueépassadoparaonossomatchernahoraqueéutilizado.Logo,quando
utilizarmos be_a_multiple_of(7),ovalorde expectedserá7.
Parafinalizaronossomatcher,énecessáriocolocaralógicadeverificaçãodentro
dele,ouseja,alógicaparachecarseumnúmeroémúltiplodeoutro.Podemosfazer
issochecandoseorestodadivisãoentreonúmerotestadoeoargumentopassado
paraomatcherézero:
RSpec::Matchers.define :be_a_multiple_of do |expected|
match do |actual|
(actual % expected) == 0
end
end
49

## Página 64

3.7. Custommatchers CasadoCódigo
Repare que para implementar a lógica de verificação utilizamos o método
match. Chamamosessemétodopassandoumblocopraelecomumargumento,
o actual,queéoobjetosendotestado.Noexemploqueestamosusando:
expect(21).to be_a_multiple_of(7)
actualéo21(objetosendotestado)eo expectedéo7(argumentopassado
paraomatcher).
Pronto,issoéomínimonecessárioparaescrevermosnossoprópriomatcher.
Comessematcherpronto,poderíamosescreverumtestedoseguintemodo:
RSpec::Matchers.define :be_a_multiple_of do |expected|
match do |actual|
(actual % expected) == 0
end
end
describe "The be_a_multiple_of custom matcher" do
it "can be used to verify if a number is a multiple of another one" do
expect(21).to be_a_multiple_of(7)
expect(15).to be_a_multiple_of(3)
expect(7).not_to be_a_multiple_of(3)
end
end
Agoraquejásabemoscomoconstruirnossoprópriomatcher,vamosvoltarao
nossoobjetivoinicial,escreverummatcherparaverificarqueumacategoriacontém
umoumaisprodutos.
Otestequeescrevemosparaacategorizaç ãodeprodutosestáatéentãodose-
guintemodo:
describe Category do
it "contains all the products of its subcategories" do
eletronics = Category.new("eletronics")
computers = Subcategory.new("computers")
cell_phones = Subcategory.new("cell phones")
computers.add_product("MacBook")
cell_phones.add_product("iPhone")
eletronics.add_subcategories(computers, cell_phones)
50

## Página 65

CasadoCódigo Capítulo3. IntroduçãoaobásicodoRSpec
eletronics_products = eletronics.subcategories.map { |sub|
sub.products
}
eletronics_products.flatten!
expect(eletronics_products).to include("MacBook", "iPhone")
end
end
Queremosmodificá-lousandoumcustommatcherparaficarassim:
describe Category do
it "contains all the products of its subcategories" do
eletronics = Category.new("eletronics")
computers = Subcategory.new("computers")
cell_phones = Subcategory.new("cell phones")
computers.add_product("MacBook")
cell_phones.add_product("iPhone")
eletronics.add_subcategories(computers, cell_phones)
expect(eletronics).to contain_products("MacBook", "iPhone")
end
end
Paraescreveressecustommatcher,iremosmaisumavezutilizaraDSLdoRSpec
eextrairalógicadeverificaçãooriginalparadentrodessematcher:
RSpec::Matchers.define :contain_products do |*products|
match do |category|
subcategories_products = category.subcategories.map { |sub|
sub.products
}
subcategories_products.flatten!
expect(subcategories_products & products).to eq products
end
end
Agoraquetemosocustommatcherpronto,podemosutilizá-lononossoteste
paraficarassim:
describe Category do
it "contains all the products of its subcategories" do
51

## Página 66

3.7. Custommatchers CasadoCódigo
eletronics = Category.new("eletronics")
computers = Subcategory.new("computers")
cell_phones = Subcategory.new("cell phones")
computers.add_product("MacBook")
cell_phones.add_product("iPhone")
eletronics.add_subcategories(computers, cell_phones)
expect(eletronics).to contain_products("MacBook", "iPhone")
end
end
Reparequeapósessarefatoraçãodeextrairumalógicadeverificaç ãocomplexa
paraumcustommatcher,ocomportamentoesperadononossotesteficoubemmais
claro.
Outropontoqueficoumelhoréamensagemdeerrodonossoteste.Paravermos
isso,bastarodarmosessetesteeveraseguintemensagem:
Failures:
1) Category contains all the products of its subcategories
Failure/Error: expect(eletronics).to
contain_products("MacBook", "iPhone")
expected #<Category:0x007fcb1c0fc460 @name="eletronics",
@subcategories=[]>
to contain products "MacBook" and "iPhone"
Namensagemdeerrojáestámaisclaroqueotestefalhouporqueacategoria
eletronicsnãocontémosprodutos "MacBook"e "iPhone",masaindapode-
mosmelhoraressamensagemaindamais.
A mensagem de erro acima foi gerada automaticamente pelo RSpec a par-
tir do nome do nosso custom matcher. Como nem sempre a mensagem pa-
drão fica clara, é possível customizá-la. Podemos fazer isso usando o método
failure_message_for_shoulddaDSLdecustommatcherdoRSpec:
failure_message_for_should do |category|
"expected category #{category.name} to contain products #{products}"
end
Ocódigoacimadeveseradicionadodentrodadefiniç ãodonossocustommat-
cher:
52

## Página 67

CasadoCódigo Capítulo3. IntroduçãoaobásicodoRSpec
RSpec::Matchers.define :contain_products do |*products|
match do |category|
subcategories_products = category.subcategories.map { |sub|
sub.products
}
subcategories_products.flatten!
expect(subcategories_products & products).to eq products
end
failure_message_for_should do |category|
"expected category #{category.name} to contain products #{products}"
end
end
Agora,aorodarmosoteste,elefalhacomaseguintemensagem:
Failures:
1) Category contains all the products of its subcategories
Failure/Error: expect(eletronics).to
contain_products("MacBook", "iPhone")
expected category eletronics to contain products ["MacBook", "iPhone"]
Apósacustomização,amensagemdeerroficoubemmaisclara!
Alémdessaopçãodecustomização,oRSpectemváriasoutras.Comosãomuitas,
convidovocêaolharadocumentaçãodecustommatchersdoRSpec(https://www.
relishapp.com/rspec/rspec-expectations/v/2-14/docs/custom-matchers)paraveras
outrasopçõesdecustomização.
Agoraquevocêjáteveaexperiênciadeconstruirumcustommatchercoma
DSLdoRSpec,vamosvermelhoroquedefatoéummatcherproRSpecedescobrir
oprotocolodematchersportrásdissotudo.
3.8 E ntendendo o protocolo interno de matcher do
RSpec
NaseçãoanteriornósaprendemosaconstruirnossosprópriosmatchersproRSpec
usandoaDSLdecustommatchers.EssaDSLserverparafacilitaracriaç ãodenovos
53

## Página 68

3.8. EntendendooprotocolointernodematcherdoRSpec CasadoCódigo
matchers,maselanãoéoúnicomododecriarummatchernovo.Vocêpodecriarseu
própriomatcherseentenderoprotocoloportrásdarelaç ãoentreumaexpectation
eoseumatcher.
Comovimosnase ção3.1,umaexpectationsegueaseguinteestruturabásica:
expect(actual).to matcher(expected)
Paraficarmaisclarocomoumaexpectationéexecutada,vamoscolocarmais
algunsparêntesesnessaestrutura:
expect(actual).to(matcher(expected))
Vocêpodeverpelalinhadecódigoacimaqueomatcherutilizadonãoénada
maisdoqueumargumentoparaométodo to. Ocontratoentreessemétodoeo
seuargumentonãoébaseadonotipodesseobjetomatcher,massimnoseucompor-
tamento,ouseja,ébaseadonofamoso duck typing.
O protocolo mínimo de um matcher é que ele responda para o método
matches?(actual),onde actualéoobjetosendotestado. Conhecendoesse
protocolo,podemosescreveromatchermaissimplesdomundo,queseriaoseguinte:
class SimplestMatcher
def matches?(actual)
true
end
end
Parautilizaressematcher,poderíamosescreverumtestedoseguintemodo:
class SimplestMatcher
def matches?(actual)
true
end
end
describe 'The matcher procotol' do
context 'a minimal matcher' do
it 'has a #matches?(actual) method' do
expect('anything').to SimplestMatcher.new
end
end
end
54

## Página 69

CasadoCódigo Capítulo3. IntroduçãoaobásicodoRSpec
Talvez você estranhe a linha expect('anything').to
SimplestMatcher.new devido ao argumento sendo passado para o mé-
todo toserumobjetonormal. Poderíamosdeixaressecódigoumpouquinho
mais“bonito”construindoumhelpermethodqueretorneumainstânciadonosso
matcher:
class SimplestMatcher
def matches?(actual)
true
end
end
describe 'The matcher procotol' do
it 'has a #matches?(actual) method ' do
expect('anything').to simple_matcher
end
def simplest_matcher
SimplestMatcher.new
end
end
Essaidéiadeterumhelpermethodqueretornaumainstânciadomatcherque
vocêqueréexatamenteoqueoRSpecfazcompraticamentetodososseusmatchers.
PodemosverissoexaminandoocódigodoRSpecparao eq matcher.Comovimos
antes,essematcheréutilizadodoseguintemodo:
actual = 'got it '
expected = 'got it '
expect(actual).to eq(expected)
OqueoRSpecfazportráséqueeletemdentrodomódulo RSpec::Matchers
umhelpermethodchamado eqcomoseguintecódigo:
def eq(expected)
BuiltIn::Eq.new(expected)
end
Comovocêpodever,essehelpermethodretornaumainstânciadeumbuilt-in
matcherdoRSpec,o Eq Matcher.Essematchertemdentrodeleumaimplementa-
55

## Página 70

3.9. Pontos-chavedestecapítulo CasadoCódigo
çãodométodo matches?(actual),seguindooprotocolodematchers,comum
códigosemelhanteaeste:
def matches?(actual)
actual == expected
end
Pronto,agoravocêjáconheceocontratobásicoentreumaexpectationeum
matcher.Paraumobjetoserummatcher,bastaqueelerespondaparaamensagem
matches?(actual).
Oúltimopontoparaentenderocontextointeirodeumaexpectationésaberpara
queelausaessemétodo matches?(actual).Internamenteométodo tochama
essemétodo,seeleretornar trueéporqueaexpectationpassou,seeleretornar
false,éporqueelaquebrou.Simplesassim.
Arealimportânciadeconheceressecontratoénãoparavocêconstruirseuspró-
priosmatchers,issovocêpodefazerusandoaDSLdoRSpec,poiselaautomatizaum
montedecoisasparavocê.Conheceressecontratoéimportanteparaqueumaex-
pectationdoRSpecparedeparecermágicaefaç asentidoparavocê. Conheceras
entranhasdassuasferramentassempreéútil,eagoravocêjáconheceumpouco
maisdos internalsdoRSpec.Comodizumgrandeamigomeu:“nãoéfeitiç aria,é
tecnologia!”.
3.9 P ontos-chave deste capítulo
NestecapítulonósconhecemosaestruturabásicadeumtestecomRSpec.Conhe-
cemososmétodos describe, iteaconstruçãodeumaexpectation.
AprendemostambémqueoRSpectemmuitosbuilt-inmatchersparanospos-
sibilitaraescrevertestesquepare çamcomdocumentação,queestejampróximosdo
semânticadodomíniodoproblemasendoresolvidoeparagerarmensagensdeerro
claras.
EmseguidavimoscomoésimplesescrevernossoprópriomatcherusandoaDSL
decustommatchersdoRSpec.Dadoqueémuitofácilfazerisso,nãoexiteemfazê-lo
quandoomotivoforclarezadoteste.
Porfim,vimoscomooRSpecemprega duck typingnoseuprotocolodematchers.
Agora,quandoalguémviercomaquelevelhopapode“Rubyémagianegra”,pelo
menosparaosmatchersdoRSpecvocêjápodedizerquenãoé,epodemostrar
comofuncionaportrásdospanos.
56

## Página 71

CasadoCódigo Capítulo3. IntroduçãoaobásicodoRSpec
NestecapítulovimostodoobásiconecessárioparaescrevertestescomRSpec,
entãojápodemosirparaopróximopasso,queécomoorganizar,refatorarereutilizar
ocódigodosnossostestes.Pareumpoucoparatomarumcafé,poisveremostudo
sóissonopróximocapítulo.
57

## Página 73

Capítulo4
Organização,refatoraçãoereusode
testescomoRSpec
Nestecapítulovocêiráaprenderacomoorganizarseustestes.Iráaprenderqueum
testedeunidadetemumanarrativaequalavantagemdesegui-la.Iráaprendertam-
bémacomorefatorarseustestesparaficaremmenosrepetitivos,massemperdera
clarezadosmesmos.
Vamoslá!
4.1 R eduzindo duplicação com hooks do RSpec
ORSpecoferecetrêstiposdehooksparapodermosreduziraduplicaç ãodosnossos
testeserodarmoscódigosarbitrários,antes,depoisouantesedepoisdosnossos
testes,sãoeles: before hook, after hooke around hook.Vamoscome çar
analisandoumexemplodequandopodemosusaro before hookparareduzira
duplicaçãodecódigodosnossostestes.

## Página 74

4.1. ReduzindoduplicaçãocomhooksdoRSpec CasadoCódigo
Usando o before hook para reduzir duplicação
Imaginequevocêestáescrevendoumjogo.Partedaespecificaçãodessejogodiz
que,quandoojogadorestánaúltimafase,seeleacertaroalvo,ojogodevefazeras
seguintesações:
• parabenizarojogador;
• setaropontuaçãopara100.
ComobompraticantedeTDD,antesdecome çaradesenvolveressafuncionali-
dade,vocêespecificaessecomportamentocomaseguinteestruturadetestes:
describe Game, "in the final phase" do
context "when the player hits the target" do
it "congratulates the player"
it "sets the score to 100"
end
end
Antesdecontinuarmosfalandosobreostestesemsi,vamosanalisaralgumas
novidadesnele.
Aprimeiranovidadeéastringsendopassadacomosegundoargumentodomé-
todo describe:
describe Game, "in the final phase"
Comovimosnocapítulo 3,ométodo describeserveparaagruparostestesde
modosemântico. Aformamaissimplesdeagruparosseustesteséporclasse. No
entanto,háoutrosmodos.Nocódigoquevimos,estamosagrupandonossostestes
porclasseeumdeterminadoestadodoobjetodessaclasse,nocaso,oestadoemque
o gameestánaúltimafase.Umadosbenefíciosdeutilizaressastringcomosegundo
argumentoéomodocomoelaficanooutputdeexecuç ãodosnossostestesquando
executamosoRSpeccomoformatodesaída documentation:
$ rspec --format documentation hooks_spec.rb
Game in the final phase
when the player hits the target
congratulates the player
sets the score to 100
60

## Página 75

CasadoCódigo Capítulo4. Organização,refatoraçãoereusodetestescomoRSpec
Asegundanovidadequefizemosnessetesteéousodométodo context.Esse
métodoéapenasumaliasdométodo describeetambémserveparaagruparnos-
sostestesdeformasemântica. Nessecasopreferimosusaro contextporquea
leituradelenessecontextoficamelhordoqueusarométodo describe.Compare
ambososmodosaseguir,primeirousando context:
describe Game, "in the final phase" do
context "when the player hits the target" do
Eagorausandoo describe:
describe Game, "in the final phase" do
describe "when the player hits the target" do
Explicadasasnovidades,vamoscontinuaratrabalharnosnossostestes.Vamos
começarescrevendooprimeiro:
context "when the player hits the target" do
it "congratulates the player"
# (...)
Osetupdessetesteenvolvecriarumobjetogameecolocá-lonafasefinal:
context "when the player hits the target" do
it "congratulates the player" do
game = Game.new
game.phase = :final
end
# (...)
end
Orestodotesteenvolveverificarquedadoessesetup,quandoojogadoracertar
oalvo,ojogodevedarparabénsparaojogador:
context "when the player hits the target" do
it "congratulates the player" do
game = Game.new
game.phase = :final
game.player_hits_target
61

## Página 76

4.1. ReduzindoduplicaçãocomhooksdoRSpec CasadoCódigo
expect(game.output).to eq("Congratuations!")
end
# (...)
end
Beleza,essetestejáestápronto.Vamospularapartedeescreverocódigopara
fazeressetestepassar,porquenãoéofocoagora,vamosescreveropróximoteste.
Opróximotesteéo:
context "when the player hits the target" do
# (...)
it "sets the score to 100"
end
Asfasesdesetupeexercíciodessetestesãoiguaisadotesteanterior,devemos
criarumjogonafasefinaledepoisfazercomqueojogadoracerteoalvo:
context "when the player hits the target" do
# (...)
it "sets the score to 100" do
game = Game.new
game.phase = :final
game.player_hits_target
end
end
Aúnicapartequemudaparaessetesteéaetapadeverificaç ão,ondequeremos
verificarqueapontuaçãodojogoficaem100:
context "when the player hits the target" do
# (...)
it "sets the score to 100" do
game = Game.new
game.phase = :final
game.player_hits_target
62

## Página 77

CasadoCódigo Capítulo4. Organização,refatoraçãoereusodetestescomoRSpec
expect(game.score).to eq(100)
end
end
Agoravamosanalisarcomoficouoarquivodetestesinteirodepoisdetermos
escritoosdoistestes:
describe Game, "in the final phase" do
context "when the player hits the target" do
it "congratulates the player" do
game = Game.new
game.phase = :final
game.player_hits_target
expect(game.output).to eq("Congratuations!")
end
it "sets the score to 100" do
game = Game.new
game.phase = :final
game.player_hits_target
expect(game.score).to eq(100)
end
end
end
Percebaqueexisteduplicaçãoentreostestes. AssimcomovocêsegueoDRY
(don’t repeat yourself)noseucódigodeprodução,vocêtambémpodeusaramesma
idéianocódigodosseustestes.ORSpecfacilitaareduç ãodeduplicaçãoatravésdo
before hook. ObeforeéummétododoRSpecparaoqualvocêpodepassarum
blocodecódigoquevaiserexecutadoantesdecadatesteouantesdetodosostestes:
before(:each) do
# roda esse código uma vez antes de cada teste
end
# ou
63

## Página 78

4.1. ReduzindoduplicaçãocomhooksdoRSpec CasadoCódigo
# não precisa passar o :each, pois ele é a opção default do before
before do
# roda esse código uma vez antes de cada teste
end
before(:all) do
# roda esse código uma vez só antes de todos os testes
end
Vamosutilizarobeforeparaprimeiroextrairosetupcomumentrenossosdois
testes:
describe Game, "in the final phase" do
before do
@game = Game.new
@game.phase = :final
end
context "when the player hits the target" do
it "congratulates the player" do
@game.player_hits_target
expect(@game.output).to eq("Congratuations!")
end
it "sets the score to 100" do
@game.player_hits_target
expect(@game.score).to eq(100)
end
end
end
Repare que extraímos o setup para um before hook dentro do escopo do
describe.Poderíamosterextraídoparaoescopodo context,maspreferimosex-
trairparaoescopodo describeporquesegundoastringdesse describe(Game,
"in the final phase"),todosostestesdeleirãocompartilharomesmoestado
do game,ouseja,o gameestarnaúltimafase.
Reparetambémqueaoextrairmososetupparaobeforehook,foinecessário
salvaroobjeto gamecomoumavariáveldeinstância. Fizemosissoporqueesseé
64

## Página 79

CasadoCódigo Capítulo4. Organização,refatoraçãoereusodetestescomoRSpec
omododecompartilharvariáveisentreumbeforehookeostestesdentrodoseu
escopo.
Agoraquejáextraímospartedocódigoduplicadonosnossostestes,vamosana-
lisarsevaleapenaextrairorestodeduplicaç ão.
4.2 DRY versus clareza nos testes
O que ainda temos duplicado entre ambos os testes é a linha
@game.player_hits_target:
context "when the player hits the target" do
it "congratulates the player" do
@game.player_hits_target
expect(@game.output).to eq("Congratuations!")
end
it "sets the score to 100" do
@game.player_hits_target
expect(@game.score).to eq(100)
end
end
Poderíamostranquilamenteextrairessalinhaparaumbeforenoescopodocon-
texto.Ficariaassim:
context "when the player hits the target" do
before { @game.player_hits_target }
it "congratulates the player" do
expect(@game.output).to eq("Congratuations!")
end
it "sets the score to 100" do
expect(@game.score).to eq(100)
end
end
Noentanto,seráquevaleapenareduziraduplicaç ãoaomáximonosnossos
testes? Arespostaénão. AaplicaçãodoconceitodeDRYnocódigodetestesé
diferentedaaplicaçãodoconceitodeDRYnocódigodeproduç ão.
65

## Página 80

4.2. DRYversusclarezanostestes CasadoCódigo
Nocódigodetestesumadasmaiorespreocupaçõesquevocêdeveteréseoteste
estáclaro,ouseja,seoleitordessecódigoconseguelereentenderoqueoteste
estáquerendotestar. Oumelhorainda,oleitordeveentenderarelaç ãodecausae
consequênciadoseuteste.Podemosvisualizarmelhoressarelaç ãocomaseguinte
máquinadeestados:
Figura4.1:Relaçãodecausaeconsequênciadeumteste
Aolerumteste,deveestarclaroparaoleitorarelaç ãodecausaeconsequência
demostradanodiagramaacima.Casoestejadifícildeentenderessarelaç ão,então
faltaclarezanoteste.
Porisso,todavezquevocêforrefatorarseustestes,sejapelomotivodeDRYou
outrarazão,vocêdevesemprepensarseessarefatoraçãonãoiráimpactarnaclareza
doseuteste.Noexemploquedemosacimaelanãoficoutãoimpactadaporqueos
testessãopequenos:
context "when the player hits the target" do
before { @game.player_hits_target }
it "congratulates the player" do
expect(@game.output).to eq("Congratuations!")
end
it "sets the score to 100" do
expect(@game.score).to eq(100)
end
end
Ummododeavaliarseoseutesteestáperdendoaclarezaélersomenteocódigo
dotesteemsi,ouseja,somenteoblocodecódigopassadoparao it.Vamosfazer
issoparaoseguinteteste:
66

## Página 81

CasadoCódigo Capítulo4. Organização,refatoraçãoereusodetestescomoRSpec
it "sets the score to 100" do
expect(@game.score).to eq(100)
end
Sódeleressetestevocêpoderiaseperguntar:
• emqueestadooobjetogameprecisaestarparaoscoresersetadocomo100?
• oquetemqueserfeitonoobjetogameparaqueeleseteoscorepara100?
Essasperguntassãoválidasparaserpossívelentenderarelaç ãodecausaecon-
sequênciadeumteste.Seotesteestivessesidoescritodoseguintemodo:
it "sets the score to 100" do
game = Game.new
game.phase = :final
game.player_hits_target
expect(@game.score).to eq(100)
end
essasperguntasteriamsidorespondidasapenaslendoocódigodotesteemsi.
Mascomoorefatoramos,énecessáriolerocódigodos before hookstambém.
Nocasodesseteste,comooarquivodetestesémuitopequenoeocódigodos
before hooksestábempertodocódigodotesteemsi,otestenãoperdemuitoem
clareza.Noentanto,seotesteestiveremumarquivomuitograndeevocêtiverque
darmuitoscroll,fazendoidasevoltasentreotesteeosbeforehooks,podeserqueo
seutestetenhaperdidoaclareza.
Resumindo,antesdeextrairtudoqueforrepetidoentreosseustestesparabefore
hooks,penseseaofazerissovocênãoestáafetandoaclarezadoseuteste.Ouseja,
nãoextraiatudoparabeforehookssóparadeixarocódigodoseuteste“DRY”,pense
nasvantagensedesvantagensdefazerisso.Lembre-sequeemcódigodeteste,uma
dascaracterísticasmaisimportanteséaclarezaeapossibilidadedeentenderfácila
relaçãodecausaeconsequência.
4.3 A fter hook
O after hookdoRSpecserveparavocêexecutarcódigoapósosseustestes. Assim
comoo before hook,eletedáaop çãodeexecutarcódigodepoisdecadatesteou
depoisdetodososseustestes:
67

## Página 82

4.3. Afterhook CasadoCódigo
after(:each) do
# roda esse código uma vez depois de cada teste
end
# ou
# não precisa passar o :each, pois ele é a opção default do after
after do
# roda esse código uma vez depois de cada teste
end
after(:all) do
# roda esse código uma vez só depois de todos os testes
end
Umexemplodeondepodeserútilo after hookéquandoénecessáriodeletar
arquivosgeradosduranteostestes.
Imaginequevocêestáescrevendoumtestedeumobjetoquesalvaumcacheem
umarquivonofilesystem:
it "caches the result in a file" do
expect {
my_cool_object.run
}.to change { File.exists?(cache_path) }. from(false).to(true)
end
Aorodaresseteste,umarquivodecacheégerado.Paraqueseutestenãodeixe
sujeiraparatrás,vocêpodeusaro after hookparadeletaressearquivogerado:
after(:all) do
FileUtils.rm(Dir.glob("#{cache_dir}/*"))
end
it "caches the result in a file" do
expect {
my_cool_object.run
}.to change { File.exists?(cache_path) }. from(false).to(true)
end
68

## Página 83

CasadoCódigo Capítulo4. Organização,refatoraçãoereusodetestescomoRSpec
4.4 A round hook
O around hookdoRSpecéútilquandovocêprecisarodarcódigoantesedepoisdo
seuteste:
describe "An around hook example" do
around do |example|
puts "Before the example"
example.run
puts "After the example"
end
it do
puts "Inside the example"
end
end
Podemosrodarotesteacimaparaentenderocaminhodaexecuç ãodoteste
quandousamosum around hook:
Before the example
Inside the example
After the example
Valeapenanotarqueoquefizemosacimapoderiatersidofeitotranquilamente
usandobeforeeafterhooks:
describe "An around hook example" do
before do
puts "Before the example"
end
after do
puts "After the example"
end
it do
puts "Inside the example"
end
end
Olugarondepodevalermaisapenausaroaroundhookaoinvésdetrocá-lopor
umbeforeeumafteréquandovocêtemalgumavantagemderodaroseutestedentro
69

## Página 84

4.5. Organizandoseustestes CasadoCódigo
deumbloco.Umexemplodissoéquandovocêquerrodarosseustestesdentrode
umatransaçãodoseubancodedados,demodoquevocêpossadarumrevertde
todososdadossalvosnobancopeloseutestesimplesmentedandoumrollbackna
transação:
class Database
def self.transaction
puts "open transaction"
yield
puts "rollback transaction"
end
end
describe "around hook" do
around(:each) do |example|
Database.transaction(&example)
end
it "runs the example as a proc" do
puts "saving a lot of data in the database"
end
end
Aoexecutarotesteacima,podemosveraseguintesaída:
open transaction
saving a lot of data in the database
rollback transaction
Repare que o método around passa como argumento para o seu bloco
o example (teste criado pelo método it), o qual você pode passar
como uma proc para um método que receba um bloco, como fizemos em
Database.transaction(&example).
4.5 O rganizando seus testes
Organizarbemosseustesteséimportanteparaafilosofiade“testescomodocumen-
tação”doBDD.Dependendodecomoseustestesestãoorganizados,podeficarmais
difícilparaoleitorentenderosseustestes,prejudicandooentendimentodarelaç ão
decausaeconsequência.Comoprimeiradicaparaorganizarseustestes,vamosdar
umaolhadanasquatrofasesdeumteste.
70

## Página 85

CasadoCódigo Capítulo4. Organização,refatoraçãoereusodetestescomoRSpec
Organizando seus testes segundo as quatro fases do xUnit
UmtestedopadrãoxUnittemquatrofases,sãoelas:
1) setup:ondevocêcolocaoSUT(system under test,porexemplooobjetosendo
testado)noestadonecessárioparaoteste;
2) exercise:ondevocêinteragecomoSUT;
3) verify:ondevocêverificaocomportamentoesperado;
4) teardown:ondevocêcolocaosistemanoestadoqueeleestavaantesdotesteser
executado.
Talvezvocênãotenhapercebido,mastodosostestesqueescrevemosaolongo
desselivroatéagoraestãoseguindoessasfases. Vejaporexemplootestedapilha
quefizemosnocapítulo 2:
describe Stack do
describe "#push" do
it "puts an element at the top of the stack" do
stack = Stack.new
stack.push(1)
stack.push(2)
expect(stack.top).to eq(2)
end
end
end
Leiaotesteacimaetenteidentificaras4fases.Eupessoalmentegostodedeixar
umaquebradelinhaentrecadafasedoteste,demodoquefiquefácilentendera
estruturadomesmosóbatendooolho.
Paraficarexplícito,segueocódigodotesteacimacomumcomentárioparacada
fase:
describe Stack do
describe "#push" do
it "puts an element at the top of the stack" do
# setup
71

## Página 86

4.5. Organizandoseustestes CasadoCódigo
stack = Stack.new
# exercise
stack.push(1)
stack.push(2)
# verify
expect(stack.top).to eq(2)
end
end
end
Nemsempreénecessárioescrevermosafasedeteardown,poisasuanecessidade
dependedotestesendoescrito.Umexemplodetestequetemafasedeteardowné
otestequeescrevemosquandovimosoafterhook:
after(:all) do
# teardown
FileUtils.rm(Dir.glob("#{cache_dir}/*"))
end
it "caches the result in a file" do
expect {
# exercise
my_cool_object.run
}.to change { File.exists?(cache_path) }. from(false).to(true)
# verify com change matcher
end
Sóparaficarclaro,nãoénecessáriovocêescreverumcomentárioexplicando
cadafasedoteste,mascolocarumaquebradelinhaentrecadafaseiráajudarbastante
oleitoraentenderaestruturadoseutestevisualmente.Compareumtestecomesem
essasquebrasdelinhaereflitasobrequalémaisclaroemrelaç ãoàsfasesdoteste:
# sem quebra de linha
it "puts an element at the top of the stack" do
stack = Stack.new
stack.push(1)
stack.push(2)
expect(stack.top).to eq(2)
end
72

## Página 87

CasadoCódigo Capítulo4. Organização,refatoraçãoereusodetestescomoRSpec
# com quebra de linha
it "puts an element at the top of the stack" do
stack = Stack.new
stack.push(1)
stack.push(2)
expect(stack.top).to eq(2)
end
EstruturarseutesteseguindoasquatrofasesdostestesxUnitiráajudaroleitor
aentenderarelaçãodecausaeconsequênciadoseutestedemodomaiseficiente.
Usando um example group por método
Antesdecome çarmosafalarsobrecomoorganizarseus example groups,você
precisaprimeirosaberoqueéum example groupdoRSpec.Entãosentaquelávem
história.
Comovimosnase ção2.3,oBDDpropõeumamudan çananomenclaturaori-
ginaldoTDDparaquesejamaisfácildeentenderarealmotivaç ãodapráticade
test-drivendevelopment.Aoinvésdeteste,umoutrotermomuitousadonomundo
doBDDéapalavraexemplo.
Aoescreverumtesteparaoseucódigo,vocêestánaverdadeescrevendoum
exemplodecomooseucódigopodeserusado.Comoasvezessomenteumexemplo
nãoéobastante,vocêescreveváriosexemplos. SevocêseguirafilosofiadoBDD,
seusexemplospodemserviratécomopartedadocumentaç ãodoseucódigo.
Tertestescomopartedadocumentaçãopodesermuitoútilporexemplonocaso
quevocêestáescrevendoumabiblioteca.SevocêusarBDDparaescreversuabibli-
oteca,odesenvolvedorqueforusá-lapodeusarcomoreferêncianãosóadocumen-
taçãodaAPIdasualib,mastambémexemplosreaisdecódigoolhandoostestes
dela.
Poisbem,oRSpecutilizaessanomenclaturade exemplosnasuaestruturain-
terna.Vocêpodeconfirmarissoentendendooretornodosmétodos ite describe
doRSpec.
O que o método it retorna na verdade é um objeto da classe
RSpec::Core::Example, um objeto que representa um exemplo de uso do
seucódigo, otesteemsi. Quandovocêprecisaorganizaressesvários examples
73

## Página 88

4.5. Organizandoseustestes CasadoCódigo
dentrodeumgrupoquefaç asentido,vocêusaométodo describe,queretorna
umaclassechamada RSpec::Core::ExampleGroup,querepresentaumgrupo
deexamples.
Agoraquejásabemosdeondevemosnomes Examplee ExampleGroupqueo
RSpecutilizanormalmente,vamosolharumaconven çãodecomoorganizarexample
groupsdosseustestes.
Naseção3.1nósescrevemosumtestedepilhadoseguintemodo:
describe Stack do
describe "#push" do
it "puts an element at the top of the stack" do
stack = Stack.new
stack.push(1)
stack.push(2)
expect(stack.top).to eq(2)
end
end
end
Percebacomousamosométodo describeparaagruparostestesrelacionados
aométodo Stack#push:
describe Stack do
describe "#push" do
# testes relacionados ao método Stack#push
end
end
Agruparostestesdeummétododeinstânciautilizandoo describedesse
modoéumaconven çãomuitousadaparaorganizarseustestesemumexample
grouppormétodo.
Amesmaconven çãopodeserusadaparaagruparostestesdeummétodode
classdentrodeumexamplegroupcomonomedessemétodo:
describe Stack do
describe ".limit" do
# testes relacionados ao método Stack.limit
end
end
74

## Página 89

CasadoCódigo Capítulo4. Organização,refatoraçãoereusodetestescomoRSpec
Comoessaorganizaçãoéapenasumaconven ção,vocênãoéobrigadoausá-la.
Mascadavezmaisessaconven çãovemsetornandoumaboapráticanacomuni-
dade,poiselafacilitaaoleitordostestesencontrartodosostestesrelacionadosaum
determinadométodo,algoqueémuitoútilseesseleitorestiverquerendoentender
ocomportamentodeummétodoemespecífico.
Notação Class#instance_method e
Class.class_method
Em Ruby, existe uma notação muito usada para se referen-
ciar a um método de instância ou de classe, que é a notação
Class#instance_methode Class.class_method.
Paramétodosdeinstânciavocêsereferenciautilizandoocaractere
“#”entreonomedaclasseeonomedométodo:
Class#instance_method
No caso da nossa pilha, temos um método de instância cha-
mado push,portantopodemosnosreferenciaraelecomanotaç ão
Stack#push.
Paramétodosdeclassevocêsereferenciautilizandoocaractere“.”
entreonomedaclasseeonomedométodo:
Class.class_method
No caso da nossa pilha, ela tem um método de classe cha-
mado initialize, podemos nos referenciar a ele com a notação
Stack.initialize.
Usando subject e let para organizar SUT e objetos colaboradores
Agoravamosolharcomovocêpodeusarosmétodos subjecte letdoRSpec
paraorganizarseustestes. Masantesdisso,comoaindanãoaindavimosnenhum
dessesdoismétodos,vamosprimeiroolharcadaumisoladamente.
ORSpecofereceummétodochamado subjectparadefiniro SUT( system
under test,oobjetosendotestado). Paraentendermoscomoelepodeserusado,
segueumexemplodecódigocomoseuuso:
describe Array, "with some elements" do
75

## Página 90

4.5. Organizandoseustestes CasadoCódigo
subject(:array) { [1,2,3] }
it "should have the prescribed elements" do
array.should == [1,2,3]
end
end
Notesteacimanósusamoso subjectparadefinirummétodochamado
array,quequandoexecutado,retornaoarray [1, 2, 3],queéSUTdonosso
teste.
Percebaquevocêpoderiare-escreverocódigoacimausandoumbeforehook:
describe Array, "with some elements" do
before do
@array = [1,2,3]
end
it "should have the prescribed elements" do
@array.should == [1,2,3]
end
end
Noentanto,ousodométodo subjectnocasoacimaémaisindicado,jáque
eledeixaexplícitoqueoobjetosendomanipuladoéoSUT.
Adiferençaentreusaro subjecteumbeforehookparaosetupdoSUT,éque
o subjectfoifeitoparamanipularoSUT,jáobeforehookserveparafazerosetup
dotestedotestecomoumtodo,ouseja,obeforehookémaisgenérico.
Agoraquejávimosumaapresentaçãodo subject,vamosfalardo let.
O letserveparadefinirum helper method(métodoauxiliar)paraoseuteste.
Vamoscomeçaraentendero letanalisandooseguinteexemplo:
describe Game do
let(:ui) { TwitterUi.new("sandbox_username", "sandbox_password") }
end
Ocódigoacimacriaummétodochamado uiquequandochamadoiráretornar
umobjetodaclasse TwitterUi.Essemétodopodeserusadodentrodeumteste,
comoaseguir:
describe Game do
before do
76

## Página 91

CasadoCódigo Capítulo4. Organização,refatoraçãoereusodetestescomoRSpec
@game = Game.new
end
let(:ui) { TwitterUi.new( 'sandbox_username', 'sandbox') }
it "congratulates the player when the player hits the target" do
@game.ui = ui # chamando o método definido pelo let
@game.player_hits_target
expect(@game.output).to include("Congratulations!")
end
end
Umaoutracaracterísticainteressantedo letéquesuaexecuçãoélazy.Ouseja,
oblocodecódigopassadoparaelesóvaiserexecutadosevocêchamarométodo
definidopelo let.Essecomportamentoédiferentedocomportamentodobefore
hook,quesempreexecutaseublocodecódigoparatodososexamplesdoseuescopo.
Paraesclareceressecomportamento,segueumexemplo:
describe "The lazy-evaluated behavior of let" do
before { @foo = 'bar' }
let(:broken_operation) { raise "I'm broken" }
it "will call the method defined by let" do
expect {
expect(@foo).to eq('bar')
broken_operation
}.to raise_error("I'm broken")
end
it "won't call the method defined by let" do
expect {
expect(@foo).to eq('bar')
}.not_to raise_error
end
end
Agoraquejáconhecemoso subjecteo let,vamosaprenderummodode
comousá-losparaorganizarnossostestes.
77

## Página 92

4.5. Organizandoseustestes CasadoCódigo
Comovocêdevesaber,emprogramaçãoorientadaaobjetos,paraqueumob-
jetopossarealizarsuaresponsabilidade,eleasvezesdependedeoutrosobjetos.Esses
objetosdosquaiseledependesãochamadosseuscolaboradores.Jáqueumobjeto
dependedeoutrospararealizarsuaresponsabilidade,umapráticamuitocomumé
passarparaoconstrutordeumaclasseosobjetosdasquaiseladependecomopa-
râmetros.Essapráticasechamainje çãodedependência,nósveremosumexemplo
concretodelanocapítulo 5.
Poisbem,seumobjetodependedeoutrosparaserconstruídoeaetapadecons-
truçãodeumobjetoéaetapamaisbásicanoseuciclodevida,entãopodevalera
penaexplicitarnoseutestecomoéfeitaaconstruçãodesseobjetoequemsãoosseus
colaboradores.Afinal,sealguémquiserentendercomousaroseucódigo,aprimeira
coisaqueessapessoadeveentenderécomocriarumainstânciaválidadoseuobjeto.
EmumtestecomRSpec,paradeixarmosexplícitocomocriarumdadoobjetoe
quaissãoseuscolaboradores,podemosusarosmétodos subjecte let.Vamos
usarumtrechodecódigoquejávimosantesparaexemplificarisso.
Imaginequevocêestáconstruindoumjogoevocêquerelesecomuniquecom
ojogadorviaTwitter.Vocêpoderiaterduasclassesparaessesistema,aclasse Game
eumaclassechamada TwitterUi,queseriaresponsávelpelainterfacedeescrita
eleituradoTwitter.Vamoscome çaraescreverumtesteparaaclasse Gameusando
subjectparaexplicitarcomoconstruirumobjeto gameeo letparamostrar
quemsãooscolaboradoresdo system under test(SUT):
describe Game do
subject(:game) { Game.new(ui) }
let(:ui) { TwitterUi.new('sandbox_username', 'sandbox_password') }
end
Agoradigamosquequeiramosescreverumtestequeespecifiquequequandoo
jogadoracertaroalvo,ojogodeveparabenizarojogador.Poderíamoscontinuaro
códigoacimaeescreveressetesteassim:
describe Game do
subject(:game) { Game.new(ui) }
let(:ui) { TwitterUi.new('sandbox_username', 'sandbox_password') }
it "congratulates the player when the player hits the target" do
game.player_hits_target
expect(game.output).to include("Congratuations!")
78

## Página 93

CasadoCódigo Capítulo4. Organização,refatoraçãoereusodetestescomoRSpec
end
end
Percebaqueparaacessaro subjectbastachamarmosométodoquefoidefi-
nidoporele.Nocasoacima,foiométodo game.
Explicitarnotestecomosecriaumainstânciadoseuobjetoequemsãoosco-
laboradoreséumaótimaformadeorganizarseuteste.Issoporquevocêjámostra
paraoleitornaintroduçãodoseutesteumexemplodealgoqueéessencialparausar
oseuobjeto,queécomoconstruirumainstânciadele.
4.6 R euso de testes
AgoraquejávimossobreosRSpechooks,sobrecomorefatorarnossostestesusando
oselesetambémsobrecomoorganizarnossostestes,vamosverumpoucosobre
comoreutilizarnossostestes.
ORSpecofereceumafuncionalidadebeminteressanteparareutilizartestesem
diferentescontextos,onomedessafuncionalidadeé shared examples.Masondeque
serianecessárioreutilizartestes?Vamosverumexemplo.
Imaginequevocêestádesenvolvendoumsistemadepublicaç ãodeconteúdo.
Atéentão,oseusistemasógerenciablogposts.Umrequisitodoseusistemaéque
seumblogpostforpublicado,énecessárioquevocêsalveadatadepublicaç ãodele.
Sabendodisso,vocêcomeçaeescreveraseguintespecparaasuaclasse BlogPost:
describe BlogPost do
describe "#publish" do
it "saves the publication date" do
blog_post = BlogPost.new
blog_post.publish!
today = Time.now.strftime("%Y-%m-%d")
expect(blog_post.published_on).to eq(today)
end
end
end
Parafazeressetestepassar,vocêescreveaclasse BlogPostdoseguintemodo:
class BlogPost
attr_reader :published_on
79

## Página 94

4.6. Reusodetestes CasadoCódigo
def publish!
today = Time.now.strftime("%Y-%m-%d")
@published_on = today
end
end
Depoisdeumtempo,seusistemafoisendocadavezmaisusadoevocêdecide
queagoraelecuidarátambémdepublicaçãodepapersacadêmicos.Umdosrequisi-
tosdepublicaçãodepaperséomesmodapublicaçãodeblogposts,vocêdevesalvar
adataqueopaperfoipublicado.ComoumbompraticantedeTDD,vocêescreveo
seguintetesteparaaclasse Paper:
describe Paper do
describe "#publish" do
it "saves the publication date" do
paper = Paper.new
paper.publish!
today = Time.now.strftime("%Y-%m-%d")
expect(paper.published_on).to eq(today)
end
end
end
Parafazeressetestepassar,vocêescreveoseguintecódigo:
class Paper
attr_reader :published_on
def publish!
today = Time.now.strftime("%Y-%m-%d")
@published_on = today
end
end
Vocêparaumpouco,olhaasduasclasses,osdoistestesepercebequetemtotal
duplicaçãoentreosdois:
class BlogPost
attr_reader :published_on
80

## Página 95

CasadoCódigo Capítulo4. Organização,refatoraçãoereusodetestescomoRSpec
def publish!
today = Time.now.strftime("%Y-%m-%d")
@published_on = today
end
end
class Paper
attr_reader :published_on
def publish!
today = Time.now.strftime("%Y-%m-%d")
@published_on = today
end
end
Paraeliminaressaduplicação,vocêpensaemextrairummóduloqueconte-
nhaasregrasdenegóciodeumobjetopublicável.Essemódulopoderiasechamar
Publishable.Aidéiaébasicamenteextrairocomportamentoduplicadodelógica
depublicaçãonasclasses BlogPoste Paperparaessemódulo.
Nóspoderíamosescreverumtesteparaessemódulodoseguintemodo:
class PublishableObject
include Publishable
end
describe "A published object" do
subject { PublishableObject.new }
describe "#publish" do
it "saves the publication date" do
subject.publish!
today = Time.now.strftime("%Y-%m-%d")
expect(subject.published_on).to eq(today)
end
end
end
Agoravamospararumpoucoparaentenderotesteacima. Primeironósdefi-
nimosumaclassesóparaesseteste,a PublishableObject,queincluiomódulo
81

## Página 96

4.6. Reusodetestes CasadoCódigo
quequeremostestar. Depoisdisso,nóschamamosométodo subjectsempas-
sarparaeleonomedométodoqueelevaidefinir.Quandovocêusaosubjectdesse
modo,vocêestádefinindoosetupdoSUT,massemdarumnomeparaele.Parausar
osubjectdefinidodessemodo,bastavocêchamarométodo subjectdedentrodo
teste,comofizemosacima:
subject.publish!
Depoisdeanalisaressesdetalhes,percebaqueessetestenadamaisédoquea
generalizaçãodostestesquefizemosantesparaasclasses BlogPoste Paper.
Para fazer esse teste passar, basta escrevermos o código do módulo
Publishable:
module Publishable
attr_reader :published_on
def publish!
today = Time.now.strftime("%Y-%m-%d")
@published_on = today
end
end
Agora que já temos esse módulo pronto, podemos inclui-lo nas classes
BlogPoste Paper:
class BlogPost
include Publishable
end
class Paper
include Publishable
end
Comissoconseguimosreduziraduplicaçãonasclassesemsi,maseaduplicaç ão
nostestes?Assimcomoconseguimosextrairocomportamentoduplicadonasnossas
classesparaummódulo,podemosextrairostestesduplicadosparaoqueoRSpec
chamade shared examples.
Parafazerisso,vamoscome çartransformandoostestesquefizemosacimapara
omódulo Publishableem shared examples.Paradefinirumconjuntode shared
examplesvocêdeveusarométodo shared_examples_forepassarparaeleuma
stringnomeandoesseconjuntodeexamples:
82

## Página 97

CasadoCódigo Capítulo4. Organização,refatoraçãoereusodetestescomoRSpec
shared_examples_for "a publishable object" do
end
Agorabastadefinirquaissãoosexamplesquepertencemaesses shared examples
passandoelesdentrodoblocodo shared_examples_for:
shared_examples_for "a publishable object" do
describe "#publish" do
it "saves the date when the object is published" do
subject.publish!
today = Time.now.strftime("%Y-%m-%d")
expect(subject.published_on).to eq(today)
end
end
end
Para usar um conjunto deshared examples, você deve usar o método
it_behaves_like ou o métodoinclude_examples passando como argu-
mentoonomedos shared examples. Ambososmétodossãobemparecidoselogo
logovamosveradiferen çaentreeles.Agoravamosre-escreverostestesdomódulo
Publishableutilizandoossharedexamplesquecriamosacima:
class PublishableObject
include Publishable
end
describe "A published object" do
subject { PublishableObject.new }
include_examples "a publishable object"
end
Pronto,issoétudoqueénecessárioparautilizarmosos shared examplesquede-
finimos.Percebaquealémdeincluiros shared examples,nessecasoaindafoineces-
sáriodefiniro subject.Issoporqueos shared examplesestãousandoo subject
definidopelotestequeosinclui:
shared_examples_for "a publishable object" do
describe "#publish" do
it "saves the date when the object is published" do
83

## Página 98

4.6. Reusodetestes CasadoCódigo
subject.publish! # uso do subject definido pelo teste que incluir
# estes shared examples
# (...)
end
end
end
Naverdade,ossharedexamplestemacessoatudoqueédefinidodentrodoteste
queosinclui,assimcomoummódulotemacessoaosmétodosdaclassequeoinclui.
Parafinalizararefatoraçãodostestesdomódulo Publishable,vamosrodar
otesteevercomoficouooutputdoRSpec.Assumindoqueessestestesestejamem
umarquivochamado shared_examples_spec.rb,podemosrodá-lodoseguinte
modo:
$ rspec --format documentation shared_examples_spec.rb
A publishable object
#publish
saves the publication date
Percebacomoostestesquedefinimosnossharedexamples "a publishable
object"foramincluidosdiretamentenooutputdoexamplegroupquefizemospara
testaromódulo Publishable.
Bom, agorasófaltautilizarmosesses shared examples nostestesdasclasses
BlogPoste Paper. Fazer isso é bem simples, basta você utilizar o método
it_behaves_like:
describe BlogPost do
it_behaves_like "a publishable object"
end
describe Paper do
it_behaves_like "a publishable object"
end
Percebaqueparaostestesdasclassesacimanãofoinecessáriodefinirmosex-
plicitamenteo subject,comofizemosnotestedomódulo Publishable. Isso
porquequandovocênãodefineexplicitamenteo subject,oRSpecfazissopara
84

## Página 99

CasadoCódigo Capítulo4. Organização,refatoraçãoereusodetestescomoRSpec
vocêautomaticamente. Eledefineo subjectautomaticamentequandooargu-
mentopassadoparaométodo describeéumaclasse.Entãoquandoescrevemos
oseguintecódigo:
describe BlogPost do
end
ORSpecnaverdadedefineosubjectdemodoimplícitodoseguintemodo:
describe BlogPost do
subject { BlogPost.new }
end
ApesardoRSpecdefinirosubjectdemodoimplícito,sempredêpreferênciapara
definirosubjectdemodoexplícitoedandoumnomeparaele.Aofazerdessemodo
vocêdeixaráseutestemaisclaro.
Porfim,vamosrodarostestesdasclasses BlogPoste Paperparaverque
ométodo it_behaves_likegeraumoutputumpoucodiferentedométodo
include_examples:
$ rspec --format documentation shared_examples_spec.rb
BlogPost
behaves like a publishable object
#publish
saves the publication date
Paper
behaves like a publishable object
#publish
saves the publication date
Percebaqueaousaro it_behaves_like,elecolocaooutputdossharedexam-
plesaninhadocomafrase behaves like a publishable object,diferentementedequando
usamosométodo include_examples,quecolocouooutputdossharedexamples
diretamente,semmostrarqueelessãosharedexamples.
Bom,agoravocêjásabecomoreutilizartestesutilizandoafuncionalidadede
shared examplesdoRSpec.Essaéumafuncionalidadebempoderosaepodeteajudar
bastanteareduzirtestesrepetitivos.
Oúnicocuidadoquevocêtemqueteraoutilizaressafuncionalidadeénãousá-
lademaisdemodoacomprometeraclarezadosseustestes.Lembre-se,aoescrever
testes,aclarezaémaisimportantequeoDRY.
85

## Página 100

4.7. Pontos-chavedestecapítulo CasadoCódigo
4.7 P ontos-chave deste capítulo
Nestecapítuloaprendemossobrecomorefatorar,organizarereutilizarnossostestes.
ComeçamosaprendendosobreosRSpechooksecomoelespodemnosajudara
reduzirduplicaçãonosnossostestes.Algoquevocêprecisalembrardissoésempre
pesarareduçãodeduplicaçãoversusaperdadeclarezanosseustestes.
Aprendemossobreoquequerdizerclarezanostestes. Umtesteéclaroseele
possibilitaaoseuleitorentenderdemodofácilarelaç ãodecausaeconsequência
entreasfasesde setup, exercisee verifydoteste.
Emseguidaaprendemosqueumtestetemumanarrativa,quesãoasquatrofases
dopadrãoxUnit: setup, exercise, verifye teardown.Seguirumanarrativanoseuteste
facilitaacompreensãodomesmo.
Porexemplo,vocêlembradaestruturaderedaçãodissertativaquevocêaprendeu
naescola?Aestruturaeraintroduç ão,desenvolvimentoeconclusão.Oequivalente
dessaestruturaderedaçãoparaumtestesãoasquatrofasesdoxUnit.Sigaaestrutura
dasquatrofaseseoseutesteficarámaisclaro.
Outrotópicointeressantequevimossobreorganizaç ãodetestesfoiaidéiade
usaro subjecte letdoRSpecparaexplicitarosetupdoseuSUTequemsãoos
colaboradoresdoseuobjeto.Teressetipodeinformaç ãonocome çodoseutesteé
algomaisquepodeajudarnaclarezadomesmo.
Porfim,vimossobrecomoutilizarossharedexamplesdoRSpecparareutili-
zartestes. Adicaaquiémesmadesempre: aopensaremreduzirduplicaç ãonos
testes,façaissocomcautela,clarezaémaisimportantedoqueDRYquandoseestá
escrevendotestes.
NocapítuloseguinteiremosaprendersobreRSpecMocks,sobreoquesão test
doublesequenovidadesousodessetipodeferramentatrásparaomodocomoes-
crevemostestes.
Nãosaiadaí!
86

## Página 101

Capítulo5
TDDnaprática,começandoum
projetocomTDD
Nãoésegredoqueparadesenvolverumahabilidadeomaisimportanteépraticar,
praticarepraticar!ComTDDnãoédiferente,nãobastalersobreRSpec,Cucumber,
suassintaxesesuasfuncionalidades.Énecessáriopraticar,énecessárioescrevertes-
tes!Porisso,nesteenospróximoscapítulosvamosdesenvolverumaaplicaç ãode0
a100fazendoTDDcomCucumbereRSpec.
Nestecapítuloiremoscome çarodesenvolvimentodaaplicaç ão,definiroseu
escopo,fazerseusetup,especificaretestaraprimeirafuncionalidade.
Alémdisso,vocêteráoprimeirocontatocomofluxodefazerTDDcomCu-
cumbereRSpec,ofamoso outside-in development. Ouseja,come çarotestecom
umaespecificaçãodeCucumber,depoisfazertestesdeRSpec,depoisfazeroRSpec
passareporfimfazeroCucumberpassar.
Porfim,duranteodesenvolvimentodessaaplicação,vocêaprenderáasrespostas
paraalgumasdúvidasclássicassobreTDD,taiscomo:

## Página 102

5.1. Definindooescopodanossaaplicação:JogodaForca CasadoCódigo
• Porondedevocomeçaratestar?
• Oquedevotestar?
• Quantostestesdevoescrever?
Aodecorrerdesteedospróximoscapítulosasrespostasparaessaseoutrasper-
guntasficarãomaisclarasparavocê.
5.1 D efinindo o escopo da nossa aplicação: J ogo da
Forca
Aaplicaçãoqueiremosdesenvolveréumjogodaforcacominterfacepelalinhade
comando. Antesdecomeçarmosafazerocódigo,énecessárioprimeirosaberos
requisitosdojogo.Vocêconheceojogodaforca?
Ojogodaforcaéoriginalmenteumjogodepapelecanetaquefuncionadose-
guintemodo:
1) Umapalavrasecretaédefinida
2) Vocêtentaadivinharumaletradapalavra
3) Sevocêacertaraletra,émostradaaposiçãodessaletradentrodapalavrasecreta
4) Sevocêerraraletra,umapartedobonecoaparecenaforca
5) Vocêganhaseacertartodasasletras
6) Vocêperdeseerrarobastanteparaocorpointeirodobonecoaparecernaforca
88

## Página 103

CasadoCódigo Capítulo5. TDDnaprática,começandoumprojetocomTDD
Figura5.1:Jogodaforcacomduasletrasadivinhadasetrêserroscometidos
Agoraquejásabemosofluxoeasregrasdenegóciodojogo,qualopróximo
passoantesdecome çaraprogramar?
Umaboaideiaétransformaresseescopoemumalistadefuncionalidadesqueo
nossojogoterá.Alistadefuncionalidadesdonossojogoseráaseguinte:
•Jogador começa um novo jogo:jogomostraamensageminicialepedepro
jogadorsortearumapalavra;
•Jogador adivinha uma letra da palavra:jogadortentaadivinharumaletrae
ojogomostraseeleacertououerrou;
•Fim do jogo:ojogoterminaquandooujogadoracertatodasasletrasouerra
obastanteparaocorpointeirodobonecoaparecernaforca.
Baseadonessalistadefuncionalidades,jápodemoscome çaradesenvolvernosso
projeto.
5.2 E specificando uma funcionalidade com Cucum-
ber
89

## Página 104

5.2. EspecificandoumafuncionalidadecomCucumber CasadoCódigo
Fazendo o setup do projeto
Antesdetudovamoscriarumdiretórioondeficaráocódigodonossoprojeto.Para
isso,abraoseuterminaledigiteosseguintescomandos:
$ mkdir forca
$ cd forca
Atualmente,todoprojetoemRubyusaoBundlerparagerenciarsuasdependên-
cias. ComoiremosusarCucumbereRSpec,vamoscriarum Gemfileelistaras
dependênciasdonossoprojeto.
InstaleoBundlerecrieumGemfile,fazendoosseguintescomandosnoterminal:
$ gem install bundler
$ bundle init
Depois,adicioneoCucumbereRSpecno Gemfile:
source "https://rubygems.org"
ruby "1.9.3"
group "test" do
gem "cucumber"
gem "rspec"
end
Efinalmente, parainstalarasdependências, bastafazer bundle install.
Apóstudoisso,vocêjádeveteroCucumbereoRSpecinstalados.
ComoCucumberinstalado,podemosrodá-lopelaprimeiravez:
$ bundle exec cucumber
You don 't have a 'features' directory. Please create one to get started.
See http://cukes.info/ for more information.
Após rodar o comando, ele nos avisa que é necessário criar o diretório
features. Comovimosnocapítulo ??,énessediretórioqueficaoconjuntode
especificaçõesdanossaaplicação. Então,vamoscriaraprimeiraespecificaç ãodo
nossojogodaforca!
90

## Página 105

CasadoCódigo Capítulo5. TDDnaprática,começandoumprojetocomTDD
Definindo os steps do primeiro cenário
Baseadonalistadefuncionalidadesquedefinimos, vamoscome çarespecifi-
candoafuncionalidade "Jogador começa um novo jogo”.Paraisso,crieumarquivo
chamado features/comecar_jogo.featureeescrevaoseguintenele:
# language: pt
Funcionalidade: Começar jogo
Para poder passar o tempo
Como jogador
Quero poder começar um novo jogo
Cenário: Começo de novo jogo com sucesso
Ao começar o jogo, é mostrada a mensagem inicial para o jogador.
Quando começo um novo jogo
Então vejo na tela:
"""
Bem vindo ao jogo da forca!
"""
Com essa especificação escrita, ao rodarmos o cucumber fazendobundle
exec cucumber,veremosaseguintesaídanatela:
$ bundle exec cucumber
# language: pt
Funcionalidade: Começar jogo
Para poder passar o tempo
Como jogador
Quero poder começar um novo jogo
Cenário: Começo de novo jogo com sucesso
Ao começar o jogo, é mostrada a mensagem inicial para o jogador.
Quando começo um novo jogo
Então vejo na tela:
"""
Bem vindo ao jogo da forca!
"""
1 scenario (1 undefined)
91

## Página 106

5.2. EspecificandoumafuncionalidadecomCucumber CasadoCódigo
2 steps (2 undefined)
0m0.002s
You can implement step definitions for undefined steps with these
snippets:
Quando /^começo um novo jogo$/ do
pending # express the regexp above with the code you wish you had
end
Então /^vejo na tela:$/ do |string|
pending # express the regexp above with the code you wish you had
end
Perceba que o Cucumber nos mostra que 1 cenário foi executado (1
scenario (1 undefined)),masquetemos2stepsindefinidos( 2 steps (2
undefined)).Alémdisso,elejánosdáumguiainicialdecomodefiniressessteps:
Quando /^começo um novo jogo$/ do
pending # express the regexp above with the code you wish you had
end
Então /^vejo na tela:$/ do |string|
pending # express the regexp above with the code you wish you had
end
Paracomeçaradefiniressessteps,vamosnosbasearnesseguia.Crieumarquivo
chamado features/step_definitions/game_steps.rbeescrevaoseguinte
nele:
# encoding: UTF-8
Quando /^começo um novo jogo$/ do
pending
end
Então /^vejo na tela:$/ do |string|
pending
end
SevocêrodaroCucumberagora,veráquedessavezelefalaquetemos1cenário
pending,1steppendinge1stepskipped:
92

## Página 107

CasadoCódigo Capítulo5. TDDnaprática,começandoumprojetocomTDD
$ bundle exec cucumber
(...)
1 scenario (1 pending)
2 steps (1 skipped, 1 pending)
0m0.013s
Estánahoradecome çarmosaimplementarnossoprimeirostep.
Implementando o primeiro step
Oprimeirostepquevamosimplementaréo "Quando começo um novo jogo”.
Seguindooquedefinimosnadescriçãodessestep,sóprecisamoscolocarnasuaim-
plementaçãoocódigoquevaicome çarumnovojogo.Paraisso,vamosimaginarque
onossosistemateráumaclasse Gamequeseráresponsávelpelojogorodando,eum
métodoGame#startquecomeçaráumnovojogo.
Seguindo essa ideia, escreva o seguinte código no arquivo
features/step_definitions/game_steps.rb:
Quando /^começo um novo jogo$/ do
game = Game.new
game.start
end
Reparequeestamosusandoumaclasse Gameeummétodo Game#startantes
mesmodelesseremimplementados.Issonãoéumproblema,fazpartedofluxodo
TDDusarumcódigoquevocêgostariaqueexistisseedeixarostestesnosguiarsobre
quandodevemosimplementaressecódigo.
SeguindoofluxodeTDD,aorodaroCucumber,otestefalhaerecebemosa
seguintemensagem:
$ bundle exec cucumber
Quando começo um novo jogo
uninitialized constant Game (NameError)
./features/step_definitions/game_steps.rb:4:in
`/^começo um novo jogo$/'
features/comecar_jogo.feature:9:in `Quando começo um novo jogo'
Ofeedbackquerecebemosdotesteéqueaconstante Gameaindanãofoidefi-
nida.Vamosentãodefini-lacriandoaclasse Game.Crieodiretório libedentro
delecrieoarquivo lib/game.rbcomoseguinteconteúdo:
93

## Página 108

5.3. UsandoRSpecnonossoprimeiroteste CasadoCódigo
# encoding: UTF-8
class Game
end
Depoisdisso,aorodaroCucumbernovamente,elecontinuanosfalandoquea
constante Gameaindanãofoidefinida. IssoporquenãoconfiguramosoCucum-
berparacarregarnossanovaclasse. Paraqueelepossacarregá-la,crieoarquivo
features/support/env.rbedentrodeleescreva:
require File.join(File.dirname(__FILE__), "..", "..", "lib", "game")
Agora,rodandooCucumber,recebemosaseguintemensagem:
$ bundle exec cucumber
Quando começo um novo jogo
undefined method `start' for #<Game:0x007f93c911bdb8> (NoMethodError)
./features/step_definitions/game_steps.rb:5:in
`/^começo um novo jogo$/'
features/comecar_jogo.feature:9:in `Quando começo um novo jogo'
Oerromudou,issoébomporqueéumindicadorqueestamosavan çando.Essa
novamensagemdeerronosfalaquenãoexisteummétodochamado startna
classe Game.Nestemomento,temosduasop ções:
1) Implementarmosométodostartnaclasse Game
2) Escrevermosumtesteparaespecificarométodo startantesdecome çara
implementá-lo
ComobonspraticantesdeTDD(etambémporquevocêestálendoumlivro
sobreTDD),vamosescolherasegundaop ção:escreverumtesteantesdecome çara
implementar.VamosusaroRSpecparaescreveresseteste.
5.3 U sando RSpec no nosso primeiro teste
Antesdecome çarausaroRSpec,precisamosinicializá-lononossoprojeto,execu-
tandooseguintecomandonoterminal:
$ bundle exec rspec --init
94

## Página 109

CasadoCódigo Capítulo5. TDDnaprática,começandoumprojetocomTDD
Após inicializar o RSpec, crie o diretóriospec e crie o arquivo de teste
spec/game_spec.rb. Oprimeirotestequevamosescreveréparaométodo
Game#start.Aoexecutaressemétodo,deveserimpressonatelaamensagemini-
cialdojogo.
Paraquepossamostestaressecomportamento,podemosusaroRSpecparave-
rificarseamensageminicialfoiimpressanatela:
# encoding: UTF-8
require 'spec_helper'
require 'game'
describe Game do
describe "#start" do
it "prints the initial message" do
game = Game.new
game.start
initial_message = "Bem vindo ao jogo da forca!"
STDOUT.should include(initial_message)
end
end
end
Oquefizemosnessetestefoi:
• criamosumainstânciadaclasseGame(fasedesetupdoteste);
• depoischamamosométodostart(fasedeexercíciodoteste);
• verificamosseométodostartimprimiunatelaamensageminicialdojogo
(fasedeverificaçãodoteste).
AorodarmosoRSpec,executando bundle exec rspec,veremosaseguinte
mensagem:
$ bundle exec rspec
F
Failures:
95

## Página 110

5.3. UsandoRSpecnonossoprimeiroteste CasadoCódigo
1) Game#start prints the initial message
Failure/Error: game.start
NoMethodError:
undefined method `start' for #<Game:0x007fd44b8f5f08>
# ./spec/game_spec.rb:10:in `block (3 levels) in <top (required)> '
Finished in 0.00036 seconds
1 example, 1 failure
Ouseja,nossotestefalhou,estávermelho. Amensagemdefalhanosdizque
ométodo startnãofoidefinidonaclasse Game. Então,chegouahoradeim-
plementarmosessemétodo.Aúnicacoisaqueeledeveráfazeréimprimirnatelaa
mensageminicialdojogo.Parafazerisso,escrevaoseguintenaclasse Game:
class Game
def start
initial_message = "Bem vindo ao jogo da forca!"
puts initial_message
end
end
AorodarmosoRSpecnovamente,vemosaseguintemensagem:
$ bundle exec rspec
1) Game#start prints the initial message
Failure/Error: STDOUT.should include(initial_message)
IOError:
not opened for reading
Oproblemaagoraestánomodocomoestamostestandoseamensagemini-
cialfoiimpressacomsucesso.Estamosfazendoissotentandolerdo STDOUT,mas
noRubynãoépossívellerdo STDOUT,amensagem "IOError: not opened
for reading"estánosdizendoisso.Então,comopodemostestaressecomporta-
mento?!Nãoparecetãosimples.
Quandoumtestecome çaaficardifícildeescrever,éprovávelqueele“queira”
nosdarumfeedbackquealgumacoisapodesermelhorada.Então,vamospensarno
queonossométodo startestáfazendo,comoestamostentandotestá-loeoque
podemosmelhorar.
96

## Página 111

CasadoCódigo Capítulo5. TDDnaprática,começandoumprojetocomTDD
Paraqueométodo startfuncione,eleprecisafazerumachamadaaométodo
puts. NoRuby,ométodo putsédefinidonomódulo Kernel. Logo,aofazer
puts initial_messagedentrodométodo start,eleestánaverdadedepen-
dendodométodo Kernel#putsparafuncionar.Noentanto,essadependêncianão
estáexplícita,eéporissoqueestádifícildetestaressemétodo.
TDD“nosforça”adeixarexplícitasasdependênciasdenossosobjetos.Nocaso
daclasse Game,podemosdeixarexplícitaadependênciade Kernel#puts,inje-
tandoessadependêncianaclasse Game.
Vamosfazerissoadicionandoumparâmetronoconstrutordaclasse Game.Esse
parâmetrosechamará output,representandoadependênciadeumobjetoque
possaimprimirstringsnatela.Alémdisso,parafacilitarainstanciaç ãodeumobjeto
daclasse Game,vamossetaro STDOUTcomovalordefaultdesseparâmetro.
Abraaclasse Gameeadicioneessenovoparâmetronoconstrutorescrevendoo
seguinte:
class Game
def initialize(output = STDOUT)
@output = output
end
def start
initial_message = "Bem vindo ao jogo da forca!"
@output.puts initial_message
end
end
Reparequecomadependência outputsalvanavariáveldeinstância @output,
mudamostambémaimplementaçãodométodo startparafazer @output.puts
aoinvésdesomente puts.
Agoraabraoarquivo game_spec.rbeomodifiqueparaficarassim:
describe Game do
describe "#start" do
it "prints the initial message" do
output = double("output")
game = Game.new(output)
initial_message = "Bem vindo ao jogo da forca!"
output.should_receive(:puts).with(initial_message)
97

## Página 112

5.3. UsandoRSpecnonossoprimeiroteste CasadoCódigo
game.start
end
end
end
Finalmente,aorodarostestes,vemosqueelespassam!
$ bundle exec rspec
.
Finished in 0.00055 seconds
1 example, 0 failures
Apóscomemorarquenossoprimeirotestepassou(\o/),valeapenaentender
melhoroquefizemosparaelepassar.
Adificuldadeestavaemtestarqueométodo startestavaimprimindoamen-
sageminicialcomsucesso.Naimplementaç ãoanteriordométodo start,elede-
pendiadométodo Kernel#puts,masessadependêncianãoestavaexplícitana
horadeconstruirumobjetodaclasse Game. Pararesolveroproblema,deixamos
explícitoqueoobjeto gamedependedealgumobjetoquesabeimprimirstrings.
Fizemosissoaoinjetaressadependêncianoconstrutordaclasse Game:
class Game
def initialize(output = STDOUT)
@output = output
end
end
Umavantagemdedeixaressadependênciaexplícita,équeissoviraumpontode
extensãodaclasse.Elanãodependemaisdiretamentedo STDOUT,eladependede
umobjetoqualquerquesabeimprimirstrings.Ouseja,estamosusando duck typing
aqui.Noambientedeprodução,esseobjetoéo STDOUT,masnostestespodemos
trocá-loporoutroobjeto,desdequeesseobjeto“separeça”comumobjetoqueim-
primestrings.Efoioquequefizemos,nosvalemosdeducktypingedeinje çãode
dependência.
Paratestarseométodo startestáfuncionando,nãoprecisamosmaisversea
stringfoiimpressanatela,bastaverificarmosseainteraç ãoentreoobjeto gameea
dependênciadelefoifeitacorretamente.Foiissoquefizemosaousarummocknesse
teste,estamostestandoseoobjeto gamechamaométodo putsdasuadependência
quandoométodo game.startéexecutado:
98

## Página 113

CasadoCódigo Capítulo5. TDDnaprática,começandoumprojetocomTDD
it "prints the initial message" do
game = Game.new(output)
output.should_receive(:puts).with(initial_message)
game.start
end
Resumindo,deixamosdetestaroestadofinaldosistema(stringimpressanatela)
paratestarainteraçãoentreoobjetoesuadependência. Fizemosissousando RS-
pec Mocks. EssatécnicadefazerTDDtestandoacomunicaç ãoentreosobjetose
nãooestadodelesébemexplicadanofamosolivro Growing Object-Oriented Soft-
ware, Guided by T ests,escritoporSteveFreemaneNatPryce[7]etambémnolivro
emportuguêsT est-Driven Development: T este e Design no Mundo Real,escritopelo
MauricioAniche[1].
Porfim,vocêpoderodaroCucumbernovamenteeverqueoprimeirostep,que
antesnãopassava,poisfaltavaimplementarométodo start,agorapassa:
$ bundle exec cucumber
(...)
1 scenario (1 pending)
2 steps (1 pending, 1 passed)
0m0.015s
Estamosprontosparairprosegundostep!
5.4 U sando Aruba para testar uma aplicação CLI
Onossoprimeirostep( "Quando começo um novo jogo")jáestápassando,va-
mosagorapensarnosegundo,queé:
Então vejo na tela:
"""
Bem vindo ao jogo da forca!
"""
Ouseja,precisamostestarqueapósojogadoriniciarojogo,essamensagem
inicialéimpressanatela.
99

## Página 114

5.4. UsandoArubaparatestarumaaplicaçãoCLI CasadoCódigo
Noambientedeprodução,ojogoiráimprimirno STDOUT,ouseja,nocon-
sole.Mas,comovimosnotestedeunidadedaclasse Game,nãoépossívelverificar
oquefoiimpressono STDOUT.PararesolveresseproblemanotestecomRSpec,
nósusamosmocks,dessemodoconseguimostestaraclasse Gameisoladamente,in-
dependentedaimplementaçãorealdesuasdependências.NotestecomCucumber
iremosfazerdiferente.
TestescomCucumbersãotestesdeaceitaç ão,nessetipodeteste,idealmente,o
softwaredevesertestadodomesmomodoqueousuáriofinaloutiliza.Porisso,não
queremosusarmocksaqui. Nãoqueremosfazerumtesteisolado,queremosfazer
umtestequerexercitetodasascamadasdonossosoftwaredemodointegrado.
Acontecequeatéagora,onossojogoaindanãotemumainterfacecomousuá-
rio.EntãoantesdecontinuarescrevendotestesdeCucumberquetestemapartirda
interfacecomousuário,precisamosprimeirocriaressainterface. Parafazerisso,
crieoarquivo bin/forcacomoseguinteconteúdo:
#!/usr/bin/env ruby
$:.unshift File.join(File.dirname(__FILE__), "..", "lib")
require 'game'
game = Game.new
game.start
Edefinaessearquivocomoumexecutável:
$ chmod +x bin/forca
Essearquivoseráobináriodonossojogo.Éelequeminiciaráaaplicação.Assim,
bastaráqueojogadorrodeessearquivoparaveraseguintesaída:
$ bin/forca
Bem vindo ao jogo da forca!
100

## Página 115

CasadoCódigo Capítulo5. TDDnaprática,começandoumprojetocomTDD
Como lidar com binários em Ruby no Windows
Nowindowsvocênãopodefazer chmod +xparatornarumarquivo
deRubyexecutável,énecessáriocriarumarquivo .batparaqueoar-
quivooriginalsejatratadocomoexecutável.Parafazerisso,alémdeter
criadooarquivo bin/forca,comovocêfezanteriormente,seráneces-
sáriocriartambémumarquivo bin/forca.batcomoseguintecon-
teúdo:
@"ruby.exe" "%~dpn0" %*
Agoraqueonossojogotemumainterfacecomousuário,precisamosatuali-
zaro step_definition Quando /^começo um novo jogo$/,paraqueele
interajacomojogodomesmomodoqueojogadorinteragiria. Paraimplementar
step definitionsqueinteragemcomumaaplicaçãodelinhadecomando,utilizaremos
umagemchamada Aruba.
OArubanadamaisédoqueumacole çãodestepdefinitionsdeCucumberfei-
tosparafacilitarodesenvolvimentodetestesqueinteragemcomumaaplicaç ão CLI
(Command Line Interface). AoutilizaroAruba,ficaráfácilverificaroquefoiim-
pressonatela.Semeleissoseriadifícil,poisteríamosqueexecutarnossojogoem
outroprocesso,quenãooprocessorodandonossotesteeconversarcomeleatravés
doseu STDINe STDOUT.Issotudo,emaisumpouco,oArubaéquemiráfazerpra
gente.
ParainstalaroAruba,adicioneeleno Gemfile:
group "test" do
gem "cucumber"
gem "rspec"
gem "aruba"
end
Eatualizeoseubundle,comocomando bundle install.
Para fazer seu setup é necessário dar um require dele no
arquivo features/support/env.rb. Então abra o arquivo
features/support/env.rbeoediteparaadicionaresse require:
101

## Página 116

5.4. UsandoArubaparatestarumaaplicaçãoCLI CasadoCódigo
require File.join(File.dirname(__FILE__), "..", "..", "lib", "game")
require "aruba/cucumber"
Para usuários de Windows
AlgunsusuáriosdeWindowspodemterumproblemadeencodingao
rodaroCucumbercomAruba,ereceberãoalgoparecidocomaseguinte
mensagemdeerro:
Incompatible character encodings:
IBM437 and UTF-8 (Encoding::CompatibilityError)
Sevocêtiveresseproblema,bastaalteraro default_encoding
para utf-8noarquivo features/support/env.rb.Façaissoadi-
cionandoaseguintelinhanotopodessearquivo:
Encoding.default_external = "utf-8"
Agoraprecisamosmodificaro step definition“Quando /^começo um novo
jogo$/”parautilizaroAruba. Masantesdisso,vamosvercomoeleestáimple-
mentadoatéentão:
Quando /^começo um novo jogo$/ do
game = Game.new
game.start
end
Omodocomotínhamosimplementadoessesteperaviaumachamadadiretade
umaclassedonossosistemaparacome çarojogo. NaimplementaçãocomAruba
faremosdiferente,queremosusá-loparacome çarojogodomesmomodoqueo
jogadorofaria,ouseja,executandoobinário forca.
Para refatorar esse step definition a fim de usar o Aruba, abra o arquivo
features/step_definitions/game_steps.rbeediteo step definitiondeco-
meçodenovojogoparaficarassim:
Quando /^começo um novo jogo$/ do
steps %{
102

## Página 117

CasadoCódigo Capítulo5. TDDnaprática,começandoumprojetocomTDD
When I run `forca` interactively
}
end
Paracomeçarumjogoexecutandoobinário forca,usamosostepdefinition“
When I run 'command'interactively”doAruba.
Para usuários de Windows
NowindowsvocêdevefazercomqueoCucumberrodeobinário
forca.bat,nãoo forca,portantomudeostepdefinitionacimapara:
Quando /^começo um novo jogo$/ do
steps %{
When I run `forca.bat` interactively
}
end
Lembre-sedesempreusar forca.batquandoforreferenciarobi-
nárioforcanosseusstepdefinitionsqueusamAruba.
Comisso,vocêjápoderodaroCucumbernovamenteeverificarqueostepcon-
tinuapassando:
$ bundle exec cucumber
(...)
1 scenario (1 pending)
2 steps (1 pending, 1 passed)
Finalmente,sóestáfaltandooúltimosteppendente,o "Então vejo na tela:”.
Essestepdeveverificarseumastringfoiimpressanatela. Paraisso,vamosutili-
zarostepdefinition“Then /^the stdout should contain "([^"]*)"$/”
doAruba.
Editeessestepnoarquivo features/step_definitions/game_steps.rb”
paraficarassim:
Então /^vejo na tela:$/ do |text|
steps %{
Then the stdout should contain "#{text }"
103

## Página 118

5.5. Pontos-chavedestecapítulo CasadoCódigo
}
end
Porfim,aorodaroCucumber,veremosquenossoprimeirocenárioestáno
verde:
$ bundle exec cucumber
1 scenario (1 passed)
2 steps (2 passed)
Figura5.2:Primeirocenárionoverde
Finalmente,conseguimosterminaroprimeirocenáriointeiro!
Nocapítuloseguintecontinuaremosodesenvolvimentodessaprimeirafuncio-
nalidade.Masantesdisso,valeapenalembrarmosdospontos-chavequeacabamos
deaprender.
5.5 P ontos-chave deste capítulo
Começamosocapítuloentendendooescopodanossaaplicaç ãoeespecificandoa
primeirafuncionalidadecomCucumber.
ComaprimeiraspecdeCucumbernovermelho,seguimosofluxode outside-in
development,fazendoumtestedeRSpec,implementandocódigoparavê-lopassare
porfimfazeroCucumberpassar.
104

## Página 119

CasadoCódigo Capítulo5. TDDnaprática,começandoumprojetocomTDD
AofazerosprimeirostestesdeunidadecomRSpec,vimosqueTDDnosfor ça
adeixarexplícitoasdependênciasdeumobjeto,quandofoinecessárioinjetarade-
pendênciaoutputnaclasse Game.EsseéumdospontosnosquaisTDDnoslevaa
fazerumcódigomelhor,porqueaodeixarasdependênciasexplícitas,ficamaisfácil
demudarocomportamentodonossosoftwaresimplesmentetrocandoaimplemen-
taçãodealgumadependência.
Porfim,vimosqueaousarmosoCucumbercomoferramentadetestesdeacei-
tação,devemosfazernossostestesenxergandoosoftwaresobtestecomoumacaixa
preta.Parafazertestescomessavisãonocasodeumaaplicaç ãodelinhadecomando,
usamosoAruba,queéumaextensãodoCucumberparatestaraplicaçõesCLI.
105

## Página 121

Capítulo6
Começandoosegundocenário
Nocapítuloanteriordefinimosoescopodonossoprojeto,fizemososetupecome ça-
mosadesenvolveretestaraprimeirafuncionalidadedojogodaforca.Nestecapítulo
nósiremoscontinuarodesenvolvimentodessafuncionalidade,definindoosegundo
cenáriodelaefazendoasmudan çaserefatoraçõesnecessáriasparaimplementaresse
segundocenário.
Vamoslá!
6.1 D efinindo o segundo cenário
Atéagorajáimplementamosoprimeirocenáriodafuncionalidade“Começarjogo”.
Mas,paracome çaronossojogo,nãobastaqueojogadorvejaamensageminicial
dojogo,éprecisotambémsortearapalavraquedeveráseradivinhada,apartirde
umtamanhodepalavradefinidopelojogador.Nessesorteio,teremososseguintes
cenários:

## Página 122

6.2. Reduzaduplicaçãoatravésdesupportcode CasadoCódigo
•Sorteio da palavra com sucesso:quandoojogadorescolheotamanhodapa-
lavraasersorteadaeojogoconseguesortearumapalavracomessetamanho;
•Sorteio da palavra sem sucesso:quandoojogadorescolheotamanhodapa-
lavraasersorteada,masojogonãotemumapalavracomessetamanho.
Vamos começar definindo o cenário de sucesso. Para isso, abra o arquivo
comecar_jogo.featureeadicioneoseguinteconteúdonele:
@wip
Cenário: Sorteio da palavra com sucesso
Após o jogador começar o jogo, ele deve escolher o tamanho da
palavra a ser adivinhada. Ao escolher o tamanho, o jogo sorteia a
palavra e mostra na tela um "_" para cada letra que a palavra
sorteada tem.
Dado que comecei um jogo
Quando escolho que a palavra a ser sorteada deverá ter "4" letras
Então vejo na tela:
"""
_ _ _ _
"""
Percebaquecolocamosatag @wip(workinprogress)nessecenário,paraconse-
guirexecutá-losozinho.Aoexecutarmosessecenárionoterminal,vemososeguinte:
$ bundle exec cucumber --tags @wip
(...)
1 scenario (1 undefined)
3 steps (1 skipped, 2 undefined)
Ouseja,dos3stepsdonossocenário,2aindaestãoindefinidos.Vamoscome çar
atrabalharnisso.
6.2 R eduza duplicação através de support code
Oprimeirostepindefinidoéo“Dado que comecei um jogo”.Essestepémuito
parecidocomostep“Quando começo um novo jogo”queimplementamosno
108

## Página 123

CasadoCódigo Capítulo6. Começandoosegundocenário
capítuloanterior. Naverdade,nósqueremosqueambososstepsfaç amamesma
coisa,ouseja,inicieumjogo.
Poderíamosterreutilizadoomesmostep,masnãoofizemosdepropósito.Fi-
zemosassimporqueescrevemosotextodonovosteppensandoprincipalmentedo
pontodevistadequemoestálendo.
Seusstepsdevemserescritosotimizadosmaisparaleituradoqueparaimple-
mentação. Lembre-se,oCucumbernãoésóumaferramentadeautomatizaç ãode
testesdeaceitação,massimumaferramentadeespecificaç ãodesoftwareeprinci-
palmenteummododecomunicaroqueoseusoftwarefaz.
Paradefinironovostep“ Dado que comecei um jogo”,poderíamossim-
plesmentecopiarecolaradefiniçãodostep“Quando começo um novo jogo”,
masissogerariaduplicaçãononossocódigo.Paraevitarisso,iremosextrairaparte
queficariaduplicadaparao support codedoCucumber.
Crieoarquivo features/support/game_helpers.rb,eimplementeo hel-
per method start_new_game, queseráresponsávelporiniciarumnovojogo
usandooAruba:
module GameHelpers
def start_new_game
steps %{
When I run `forca` interactively
}
end
end
World(GameHelpers)
Reparequealémdetermoscriadoomódulo GameHelpers,tambémincluímos
osmétodosdessemódulonocontextodosstepdefinitions,usandoométodo World
doCucumber,comovimosnocapítulo ??.
Agora edite o step Quando /^começo um novo jogo$/ do arquivo
features/step_definitions/game_steps.rbparaqueelechameonosso
novohelpermethod start_new_game:
Quando /^começo um novo jogo$/ do
start_new_game
end
109

## Página 124

6.3. Implementandoofluxodojogonobinário CasadoCódigo
AorodaroCucumber,vocêveráqueocenário "Começo de novo jogo com su-
cesso”continuanoverde. Comisso,podemosadicionaronovostepnoarquivo
features/step_definitions/game_steps.rb:
Dado /^que comecei um jogo$/ do
start_new_game
end
RodandooCucumberparaonovocenário,vemosqueumstepjáestápassando,
masqueo "Quando escolho que a palavra a ser sorteada deverá ter “4” letras”continua
indefinido:
$ bundle exec cucumber --tags @wip
(...)
3 steps (1 skipped, 1 undefined, 1 passed)
Vamosimplementaresseúltimostep.
6.3 I mplementando o fluxo do jogo no binário
Opróximostepaserimplementadoéo "Quando escolho que a palavra a ser sorteada
deverá ter “4” letras”.Paraimplementá-lo,vamosadicionarumstepdefinitionnoar-
quivo features/step_definitions/game_steps.rbqueusaráoArubapara
simularumjogadordigitandootamanhodapalavraasersorteadanojogo:
Quando /^escolho que a palavra a ser sorteada deverá ter "(.*?)" letras\
$/ do |number_of_letters|
steps %{
When I type "#{number_of_letters}"
}
end
AorodarmosoCucumberdestecenário,vemososeguinte:
$ bundle exec cucumber --tags @wip
Então vejo na tela:
"""
_ _ _ _
110

## Página 125

CasadoCódigo Capítulo6. Começandoosegundocenário
"""
expected "Qual o tamanho da palavra a ser sorteada?\n"
to include "_ _ _ _"
Diff:
@@ -1,2 +1,2 @@
-_ _ _ _
+Qual o tamanho da palavra a ser sorteada?
(RSpec::Expectations::ExpectationNotMetError)
features/comecar_jogo.feature:25:in `Então vejo na tela: '
Failing Scenarios:
cucumber features/comecar_jogo.feature:18
Ocenáriofalhou,masporquê? Omotivoéqueaindaprecisamosconstruiro
restodafuncionalidade.Oqueestáfaltandoé:
1) ojogadorpoderescolherotamanhodapalavraasersorteada;
2) ojogosorteiaessapalavra;
3) ojogoimprimenatelaumcaractere“_”paracadaletradapalavrasorteada.
Precisamosmodificarobináriodonossojogoparaimplementaressespassos.
Atéentãoobináriosóiniciaojogoeimprimeamensageminicial:
#!/usr/bin/env ruby
$:.unshift File.join(File.dirname(__FILE__), "..", "lib")
require 'game'
game = Game.new
game.start
Precisamosmodificá-loparaqueelepe çaparaojogadorotamanhodapalavra
asersorteada,depoisasorteieecontinuerodandoatéqueojogoacabe. Ouseja,
precisamosmodificarobinárioparaqueelerodeofluxodojogocomoumtodo.
Nossaideianãoéimplementarocódigodofluxodojogoemsinobinário,mas
simqueobináriodependademétodosdonossosistemaqueserãoresponsáveispor
controlaressefluxo.
111

## Página 126

6.3. Implementandoofluxodojogonobinário CasadoCódigo
Paracontrolarofluxodojogo,podemosimaginaqueaclasse Gameterádois
novosmétodos, ended?e next_step. Ométodo ended?irádizerseojogo
terminouounão.Eométodo next_stepvaiexecutaropróximopassodojogo,
baseadonoestadoatualdomesmo.
Vamosadicionarousodessesnovosmétodosnobináriodonossojogo.Modifi-
queoarquivo bin/forcaparaqueelefiqueassim:
#!/usr/bin/env ruby
$:.unshift File.join(File.dirname(__FILE__), "..", "lib")
require 'game'
game = Game.new
game.start
while not game.ended?
game.next_step
end
Oquefizemosnessecódigofoioseguinte:apósojogoserinicializadoemostrar
amensageminicial,eleentranumloopeficarodandoopróximopassodojogoatéo
jogoterminar,utilizandoométodo Game#ended?paracontrolaroloopeométodo
Game#next_stepparaexecutaropassoseguintedojogo.
Logoapósojogocome çar,apalavraaindanãofoisorteada,entãoopróximo
passoépedirprojogadorotamanhodapalavraasersorteadaesorteá-la. Emse-
guida,opróximopassoéojogopedirparaojogadoradivinharumaletradapalavra.
Ospassosseguintesconsistemnojogadotentaradivinharasletrasdapalavra,atéque
eleadivinhetodaseganhe,oupercaporqueerroudemais.
Antesdecome çarmosaimplementaropróximopassodofluxodojogo,vamos
rodaronovobinário.
$ bin/forca
Bem vindo ao jogo da forca!
bin/forca:10:in `<main>': undefined method `ended?' for
#<Game:0x007fe84890a208 @output=#<IO:<STDOUT>>> (NoMethodError)
Ouseja,oerrofoiqueométodo Game#ended?aindanãofoiconstruído.
112

## Página 127

CasadoCódigo Capítulo6. Começandoosegundocenário
VamosrodaroCucumbereverseapareceamesmamensagemdeerro:
$ bundle exec cucumber
Então vejo na tela:
"""
_ _ _ _
"""
expected "Bem vindo ao jogo da forca!\n" to include "_ _ _ _"
Diff:
@@ -1,2 +1,2 @@
-_ _ _ _
+Bem vindo ao jogo da forca!
(RSpec::Expectations::ExpectationNotMetError)
features/comecar_jogo.feature:26:in `Então vejo na tela: '
2 scenarios (1 failed, 1 passed)
5 steps (1 failed, 4 passed)
Nãoapareceuamesmamensagemdeerro.Rodandoobinário,ofeedbackque
recebemoséqueométodo Game#ended?aindaprecisaserimplementado. Ao
rodarcomCucumber,nãorecebemosomesmofeedback.
Executandoobinário,nossojogoquebra,rodandocomCucumberoprimeiro
cenáriochegaatéapassareosegundocenárioquebracomumamensagemdeerro
diferentedaqueaparecequandoquebrarodandonamão.Issonãoestálegal,pois
comooCucumberdevetestarosoftwaredomesmopontodevistadousuáriofinal,
sealgoestáquebrandodopontodevistadousuário(rodandodiretamenteobiná-
rio),eledeveriaquebrarnostestesdoCucumbertambém.Precisamosconsertaresse
problema!
6.4 M odificando nosso cenário para receber o fe-
edback correto
Vimosquerodarojogonamãoestáquebrandoerodá-locomCucumbernãoestá
quebrando.IssoéruimpoistestesdoCucumberdevemnosdizerseosoftwareestá
quebrandodopontodevistadousuário.
OusuáriofinaleoCucumberestãoiniciandoojogodomesmomodo,usando
obinárioforca,comadiferen çaqueoCucumberestáfazendoissoviaoAruba.
113

## Página 128

6.4. Modificandonossocenárioparareceberofeedbackcorreto CasadoCódigo
ParaqueotestecomCucumbertenhaumresultadofinalmaisparecidocom
rodarojogonamão,oquepodemosfazeréchecarseobináriorodoucomsucesso,
ousejaverificaro exit statusdoprocessodojogo.OArubatemumstepdefinition
queverificao exit statusdoprocessosobteste,portanto,podemosusá-lo.
Vamosmudarnossoarquivodefeature features/comecar_jogo.feature,
colocandoumstepquevaifazerisso. Iremostrocaroantigostep "Então vejo na
tela:”porumnovostep,o "Então o jogo termina com a seguinte mensagem na tela:”.
Oantigostepsóverificavaseumadadastringfoiimpressanatela.Nessenovostep,
alémdeverificarseastringfoiimpressa,verificaremostambémseoprocessodo
jogoterminoucomsucesso,atravésdachecagemdoseu exit statuscomoAruba.
Modifique os cenários do arquivo arquivo
features/comecar_jogo.feature para utilizar esse novo step e ficar as-
sim:
Cenário: Começo de novo jogo com sucesso
Ao começar o jogo, é mostrada a mensagem inicial para o jogador.
Quando começo um novo jogo
Então o jogo termina com a seguinte mensagem na tela:
"""
Bem vindo ao jogo da forca!
"""
@wip
Cenário: Sorteio da palavra com sucesso
Após o jogador começar o jogo, ele deve escolher o tamanho da
palavra a ser adivinhada. Ao escolher o tamanho, o jogo sorteia a
palavra e mostra na tela um "_" para cada letra que a palavra
sorteada tem.
Dado que comecei um jogo
Quando escolho que a palavra a ser sorteada deverá ter " 4" letras
Então o jogo termina com a seguinte mensagem na tela:
"""
_ _ _ _
"""
Ao rodar o Cucumber, veremos que esse step ainda está indefi-
nido. Vamos defini-lo. Ao adicionar o novo step definition no arquivo
features/step_definitions/game_steps.rbeleficaráassim:
114

## Página 129

CasadoCódigo Capítulo6. Começandoosegundocenário
# encoding: UTF-8
Dado /^que comecei um jogo$/ do
start_new_game
end
Quando /^começo um novo jogo$/ do
start_new_game
end
Quando /^escolho que a palavra a ser sorteada deverá ter "(.*?)" letras\
$/ do |number_of_letters|
steps %{
When I type "#{number_of_letters}"
}
end
Então /^o jogo termina com a seguinte mensagem na tela:$/ do |text|
steps %{
Then it should pass with:
"""
#{text}
"""
}
end
Deletamosoantigostep "Então vejo na tela:”eadicionamosonovostep "Então
o jogo termina com a seguinte mensagem na tela:”.Usamosostepdefinition“Then
it should pass with:”doAruba.Essestepdefinitionverificaseumtextofoi
impressono STDOUTetambémverificaseo exit statusdoprocessosobtestefoide
sucesso.
AorodaroCucumbernovamente,vemososeguinte:
$ bundle exec cucumber
Então o jogo termina com a seguinte mensagem na tela:
(...)
Exit status was 1 but expected it to be 0. Output:
115

## Página 130

6.5. UsandosubjecteletdoRSpecparaevitarduplicaç ãonostestes CasadoCódigo
forca/bin/forca:10:in `<main>':
undefined method `ended?' for #<Game: ...> (NoMethodError)
2 scenarios (2 failed)
Amensagemdeerronosdizqueoprogramaquebroucomamensagemdeex-
ceção "undefined method 'ended?'",omesmofeedbackquerecebemosao
rodarojogonamão.AgorasimostestescomCucumberrefletemarealidade!Com
ofeedbackcorretodoCucumber,podemosseguiremfrente.
6.5 U sando subject e let do RSpec para evitar dupli-
cação nos testes
AorodaroCucumber,vemosqueambososcenáriosquebram,equebramcoma
seguintemensagem:“undefined method 'ended?'for #<Game:>”.Ouseja
precisamosimplementarométodo Game#ended?.
Comovimosnoarquivo bin/forca,ométodo Game#ended?seráusadopara
sinalizarseojogodevecontinuarrodandoounão.Ojogodevecontinuarrodando
ouatéqueojogadorpe çaparaeleterminar,ouatéqueeleganheouatéqueeleperca.
Vamoscomeçarfazendoumtesteparacobrirocenáriodequandoojogoacaboude
começar.
Abraoarquivo spec/game_spec.rbeescrevaessetestedoseguintemodo:
it "returns false when the game just started" do
game = Game.new
game.should_not be_ended
end
AorodarmosoRSpec,essetestequebraporquefaltaimplementarométodo
Game#ended?,vamosimplementá-lo.
Essemétodoteráqueretornar trueou falsedependendoseojogoterminou
ounão.Vamossalvarainformaç ãoseojogoterminouounãoemumavariávelde
instânciachamada @ended,eutilizá-laparaimplementarométodo Game#ended?.
Seguindoessaideia,adicioneométodo ended?noarquivo lib/game.rbe
modifiqueométodo initializeparaficarassim:
def initialize(output = STDOUT)
@output = output
116

## Página 131

CasadoCódigo Capítulo6. Começandoosegundocenário
@ended = false
end
def ended?
@ended
end
Agora,aorodaroRSpec,vemosqueonovotestepassa.Atéentão,nossostestes
daclasse Gameestãoassim:
describe Game do
describe "#start" do
it "prints the initial message" do
output = double("output")
game = Game.new(output)
initial_message = "Bem vindo ao jogo da forca!"
output.should_receive(:puts).with(initial_message)
game.start
end
end
describe "#ended?" do
it "returns false when the game just started" do
game = Game.new
game.should_not be_ended
end
end
end
Percebaqueacriaçãodoobjeto gameestáduplicadaentreosdoistestes.Vamos
extrairainstanciaçãodoobjetogameparaum subject.Alémdisso,vamosaproveitar
paraextrairadefiniçãodocolaborador outputparaum let.
Pessoalmente,eugostodedeixaradefiniçãodetodososcolaboradoresdoobjeto
sobtestenocome çodotesteusando let.Dessemodo,ficabemclaroquaissãoas
dependênciasdoobjetosobteste.
Apósessareduçãodeduplicidade,nossotesteficaráassim:
describe Game do
let(:output) { double("output") }
117

## Página 132

6.5. UsandosubjecteletdoRSpecparaevitarduplicaç ãonostestes CasadoCódigo
subject(:game) { Game.new(output) }
describe "#start" do
it "prints the initial message" do
initial_message = "Bem vindo ao jogo da forca!"
output.should_receive(:puts).with(initial_message)
game.start
end
end
describe "#ended?" do
it "returns false when the game just started" do
game.should_not be_ended
end
end
end
Depoisdessarefatoração,vocêpodeverificarqueostestesdeRSpeccontinuam
passando.Então,podemosrodarostestesdoCucumbernovamente:
$ bundle exec cucumber
Então o jogo termina com a seguinte mensagem na tela:
(...)
Exit status was 1 but expected it to be 0. Output:
forca/bin/forca:11:in `<main>':
undefined method `next_step' for #<Game: ... > (NoMethodError)
2 scenarios (2 failed)
Pela mensagem de erro, podemos ver que falta implementarmos o método
Game#next_step,vamosescreverumtesteparaessemétodoeimplementá-lo.
Oprimeirotestequeiremosescreveréprocenárioondeojogoacaboudecome-
çar.Nessecontexto,ométodo Game#next_stepdevepedirprojogadorotamanho
dapalavraasersorteada.Parafazeraverificaç ãodesseteste,bastachecarmosseo
118

## Página 133

CasadoCódigo Capítulo6. Começandoosegundocenário
objeto gameirápedirproseucolaborador outputparaimprimiraperguntapro
jogadorpedindootamanhodapalavraasersorteada.
Seguindo essa ideia, escreva esse teste no arquivo arquivo
spec/game_spec.rb:
describe "#next_step" do
context "when the game just started" do
it "asks the player for the length of the word to be raffled" do
question = "Qual o tamanho da palavra a ser sorteada?"
output.should_receive(:puts).with(question)
game.next_step
end
end
end
Vamosfazeressetestepassar. Implementeométodo next_stepnoarquivo
lib/game.rb,queimprimiráafrasepedindootamanhodapalavra:
def next_step
@output.puts("Qual o tamanho da palavra a ser sorteada?")
end
AorodaroRSpec,podemosverqueostestesestãopassando.Ouseja,podemos
voltarparaoCucumber.
6.6 R efatorando o código para poder implementar
o segundo cenário
AorodarmosoCucumber,vemososeguinte:
$ bundle exec cucumber
(...)
process still alive after 3 seconds (ChildProcess::TimeoutError)
2 scenarios (2 failed)
Mesmocomosmétodos Game#ended?e Game#next_stepimplementados,
osdoiscenáriosdoCucumbercontinuamquebrando.Oerroaconteceu,poisopro-
cessodonossojogonuncatermina.Paraentendê-lomelhor,rodeonossojogo:
119

## Página 134

6.6. Refatorandoocódigoparapoderimplementarosegundocenário CasadoCódigo
$ bin/forca
Qual o tamanho da palavra a ser sorteada?
Qual o tamanho da palavra a ser sorteada?
(...)
Qual o tamanho da palavra a ser sorteada?
Qual o tamanho da palavra a ser sorteada?
Qual o tamanho da palavra a ser sorteada?
Oproblemaqueestáocorrendoéquenossojogoestáemumloopinfinitoporque
emnenhummomentoométodo Game#ended?estáretornandotrue.
Precisamosqueojogadortenhaummododefinalizarojogonomeio.Omodo
comoelevaipoderfazerissoédigitando "fim”emqualquermomentoqueojogo
pediralgumaentrada.
Paraimplementaressaideia,vamoscome çaradicionandoumnovostepnanossa
feature,o "E termino o jogo”,quevaisimularojogadorterminandoojogonomeio.
Podemosadicionarprimeironocenário "Começo de novo jogo com sucesso”:
Cenário: Começo de novo jogo com sucesso
Ao começar o jogo, é mostrada a mensagem inicial para o jogador.
Quando começo um novo jogo
E termino o jogo
Então o jogo termina com a seguinte mensagem na tela:
"""
Bem vindo ao jogo da forca!
"""
Eemseguida,nocenárioquefarácomsucessoosorteiodapalavra:
@wip
Cenário: Sorteio da palavra com sucesso
Após o jogador começar o jogo, ele deve escolher o tamanho da
palavra a ser adivinhada. Ao escolher o tamanho, o jogo sorteia a
palavra e mostra na tela um "_" para cada letra que a palavra
sorteada tem.
Dado que comecei um jogo
Quando escolho que a palavra a ser sorteada deverá ter "4 " letras
E termino o jogo
Então o jogo termina com a seguinte mensagem na tela:
120

## Página 135

CasadoCódigo Capítulo6. Começandoosegundocenário
"""
_ _ _ _
"""
Agora,estramosprontosparaimplementaressestep. Adicioneoseguintestep
definitionnoarquivo features/step_definitions/game_steps.rb:
Quando /^termino o jogo$/ do
steps %{
When I type "fim"
}
end
Com esse step definido, ao rodar o Cucumber, vemos que o processo do
jogocontinuarodandosemparar. Issoaindaestáacontecendoporqueométodo
Game#next_stepaindanãoestápedindoumaentradadojogador,ondeelepode
digitar“fim”.Vamosespecificaressenovocomportamentoatravésdeumteste.
Atéentão,nósjátemosumtesteparaométodo Game#next_step:
describe "#next_step" do
context "when the game just started" do
it "asks the player for the length of the word to be raffled" do
question = "Qual o tamanho da palavra a ser sorteada?"
output.should_receive(:puts).with(question)
game.next_step
end
end
end
Essetesteverificaseojogoperguntaprojogadorotamanhodapalavraasersor-
teada,quandoométodoGame#next_stepéexecutadoeojogoacaboudecome çar.
Precisamosmodificaressetesteparafazermaisdoqueisso,eleprecisaverificartam-
bémseojogoestálendootamanhodapalavraqueojogadorirádigitar.Paralera
entradadojogador,podemoscriarumnovocolaboradorqueteráessaresponsabili-
dade,vamoschamá-lode input.Vamosentãomudarotesteacimaparaverificar
seoobjeto gamepedeparaoobjeto inputleraentradadojogador:
1 describe Game do
2 let(:output) { double("output") }
3 let(:input) { double("input") }
121

## Página 136

6.6. Refatorandoocódigoparapoderimplementarosegundocenário CasadoCódigo
4
5 subject(:game) { Game.new(output, input) }
6
7 # (...)
8
9 describe "#next_step" do
10 context "when the game just started" do
11 it "asks the player for the length of the word to be raffled" do
12 question = "Qual o tamanho da palavra a ser sorteada?"
13 output.should_receive(:puts).with(question)
14
15 input.should_receive(:gets)
16
17 game.next_step
18 end
19 end
20 end
21 end
Parafazeressetestepassar,podemosinjetaradependência input,aquala
implementaçãodefaultvaisero STDIN,eutilizá-lanométodo next_stepparaler
aentradadojogador.Essaimplementaçãonoarquivo lib/game.rbficaráassim:
class Game
def initialize(output = STDOUT, input = STDIN)
@output = output
@input = input
@ended = false
end
# (...)
def next_step
@output.puts("Qual o tamanho da palavra a ser sorteada?")
word_length = @input.gets
end
end
AorodarostestesdeRSpec,vemosqueagoraelespassam.Vamosaproveitarque
ostestesestãopassandoevamosrefatorar.
122

## Página 137

CasadoCódigo Capítulo6. Começandoosegundocenário
6.7 E xtraindo uma classe através de refatoração
Umproblemadaimplementaçãoatualéqueagoranossaclasse Gametemmaisuma
dependência.Essanovadependênciaémaisummotivoparanossocódigoquebrar
eumnívelamaisdecomplexidade.Agoraparainstanciarmosumobjetodaclasse
Game,precisamosantesinstanciardoisobjetos:
let(:output) { double("output") }
let(:input) { double("input") }
subject(:game) { Game.new(output, input) }
Ospapéisdessesobjetossãomuitorelacionados,umtemcomoresponsabilidade
mostrarcoisasparaousuário,ooutrotemcomoresponsabilidadepegarentradasde
dadosdousuário.
Comoospapéisestãobemrelacionados,podemosjuntaressesdoisobjetosem
umsó,quevaiteraresponsabilidadedepoderinteragircomousuário.Umobjeto
quefaráainterfacecomnossousuário. Vamosrefatorarnossotesteecódigopara
trocarautilizaçãodosobjetos inpute outputporumúnicoobjetoquechama-
remosde ui(user interface).
Aprimeiracoisaquetemosquemudarnotestedaclasse Gameéatrocara
criaçãode inpute outputpor ui.Atéentão,essapartedotesteestáassim:
describe Game do
let(:output) { double("output") }
let(:input) { double("input") }
subject(:game) { Game.new(output, input) }
# (...)
end
Vamosmodificá-laparaficarassim:
describe Game do
let(:ui) { double("ui") }
subject(:game) { Game.new(ui) }
# (...)
end
123

## Página 138

6.7. Extraindoumaclasseatravésderefatoração CasadoCódigo
Asegundamudan çaquetemosquefazernostestesdaclasse Gameémudar
chamadosdemétododo inputedo outputparaonovo ui.Nessestestes,temos
verificaçãodechamadademétododessesobjetosnosseguintestrechos:
it "prints the initial message" do
initial_message = "Bem vindo ao jogo da forca!"
output.should_receive(:puts).with(initial_message)
game.start
end
e
it "asks the player for the length of the word to be raffled" do
question = "Qual o tamanho da palavra a ser sorteada?"
output.should_receive(:puts).with(question)
input.should_receive(:gets)
game.next_step
end
Ou seja, onde antes estava “ output.should_receive(:puts)”
ou “input.should_receive(:gets)”, precisamos mudar para “
ui.should_receive(:puts)” e “ui.should_receive(:gets)”. E, já
queestamosmudandode inpute outputpara ui,valeapenarepensaros
nomesdemétodos putse getsparaonovo ui.
Osnomesdemétodo putse getsestãomuitorelacionadoscomo STDOUTe
STDIN,queeramasimplementaçõesantigasdasdependênciasdo game.Apartir
deagoraestamoscriandoumanovaabstraç ãocomodependência,o ui.Essanova
dependêncianãonecessariamentesemprevaitercomoimplementaçãorealo STDIN
e STDOUTportrás.Logo,fazsentidocriarmosnomesdemétodosmaisabstratos,
queestejammaisrelacionadoscomopapelqueadependênciavaiterparao game
doquecomaimplementaçãorealquevaiserfeita.Vamosmudarentãode getse
putspara reade write.
Seguindo essa ideia, onde antes era “input.should_receive(:gets)”
vai ficar “ ui.should_receive(:read)” e onde an-
tes era “ output.should_receive(:puts)” vai ficar “
ui.should_receive(:write)”.
Logo,ostrechosdecódigoanterioresficarãoassim:
124

## Página 139

CasadoCódigo Capítulo6. Começandoosegundocenário
it "prints the initial message" do
initial_message = "Bem vindo ao jogo da forca!"
ui.should_receive(:write).with(initial_message)
game.start
end
eassim:
it "asks the player for the length of the word to be raffled" do
question = "Qual o tamanho da palavra a ser sorteada?"
ui.should_receive(:write).with(question)
ui.should_receive(:read)
game.next_step
end
Porfim,nossotesteinteiroficaráassim:
describe Game do
let(:ui) { double("ui") }
subject(:game) { Game.new(ui) }
describe "#start" do
it "prints the initial message" do
initial_message = "Bem vindo ao jogo da forca!"
ui.should_receive(:write).with(initial_message)
game.start
end
end
describe "#ended?" do
it "returns false when the game just started" do
game.should_not be_ended
end
end
describe "#next_step" do
context "when the game just started" do
125

## Página 140

6.7. Extraindoumaclasseatravésderefatoração CasadoCódigo
it "asks the player for the length of the word to be raffled" do
question = "Qual o tamanho da palavra a ser sorteada?"
ui.should_receive(:write).with(question)
ui.should_receive(:read)
game.next_step
end
end
end
end
Parafazerotestepassar,precisamosalteraraclasse Gameparadeixardeutilizar
input.getse output.putsparautilizar ui.reade ui.write. Precisamos
tambémmudarainje çãodedependênciaparaanovadependência ui.Aplicando
essasmudançasnoarquivo lib/game.rb,ocódigoficaráassim:
class Game
def initialize(ui = CliUi.new)
@ui = ui
@ended = false
end
def start
initial_message = "Bem vindo ao jogo da forca!"
@ui.write(initial_message)
end
def ended?
@ended
end
def next_step
@ui.write("Qual o tamanho da palavra a ser sorteada?")
word_length = @ui.read
end
end
Comessaimplementação,nossostestespassam.
Notequeaimplementaçãodefaultdadependência uiéumobjetodeumanova
classe,aclasse CliUi(commandlineuserinterface).
126

## Página 141

CasadoCódigo Capítulo6. Começandoosegundocenário
Crieumnovoarquivo lib/cli_ui.rbeescrevaocódigodessaclassenele:
# Classe responsável por representar a interface com o usuário.
#
class CliUi
def write(text)
puts text
end
def read
user_input = gets
user_input
end
end
Paraqueaclasse Gameenxergueaclasse CliUi,adicioneoseguinte require
nocomeçodoarquivolib/game.rb:
# encoding: UTF-8
require_relative 'cli_ui'
class Game
# (...)
end
AorodarostestesdoRSpec,vemosqueelesestãopassando.Comarefatoraç ão
terminadaecomostestesnoverde,podemosirparaopróximopasso.
6.8 P ossibilitando ao jogador terminar o jogo no
meio
Comostestespassando,podemosvoltarparaaideiaoriginal,queeraapossibilidade
dojogadorterminarojogonomeiodigitando "fim”.Paraisso,adicioneoseguinte
testenoarquivo lib/game.rb:
describe "#next_step" do
# (...)
it "finishes the game when the player asks to" do
player_input = "fim"
127

## Página 142

6.8. Possibilitandoaojogadorterminarojogonomeio CasadoCódigo
ui.stub(read: player_input)
game.next_step
game.should be_ended
end
end
Aorodarmosostestes,elesfalhamcomaseguintemensagem:
Failures:
1) Game#next_step finishes the game when the player asks to
Failure/Error: game.next_step
Double "ui" received unexpected message :write with
("Qual o tamanho da palavra a ser sorteada?")
# ./lib/game.rb:21:in `next_step'
# ./spec/game_spec.rb:42
Oproblemafoiqueodouble uirecebeuumamensagem writecomoargu-
mento "Qual o tamanho da palavra a ser sorteada?”demodoinesperado.Ométodo
next_stepdefatochama ui.write,masaúnicacoisaquefizemosnosetupdo
nossotestecomodouble uifoi ui.stub(read: player_input). Fizemos
dessemodo,poisessaéaúnicapartedainteraç ãocomo uiquenosimportanesse
teste.
Oquequeremoséignorarorestodasmensagensenviadasparaodouble ui.Po-
demosfazerissousandoafeaturede as_null_objectdoRSpec.Editeadefinição
dadependênciauinoarquivo spec/game_spec.rbparaficarassim:
describe Game do
let(:ui) { double("ui").as_null_object }
# (...)
end
Agoraaorodarostestes,recebemosamensagemdeerroesperada:
$ bundle exec rspec
1) Game#next_step finishes the game when the player asks to
Failure/Error: game.should be_ended
128

## Página 143

CasadoCódigo Capítulo6. Começandoosegundocenário
expected ended? to return true, got false
# ./spec/game_spec.rb:44
Parafazerotestepassar,precisamosmodificarométodo next_stepparaque
eleseteaflag @endedcomo true,casoojogadortenhadigitadoaentrada "fim".
Comessamodificação,ométodo Game#next_stepficaráassim:
def next_step
@ui.write("Qual o tamanho da palavra a ser sorteada?")
player_input = @ui.read.strip
if player_input == "fim"
@ended = true
end
end
AorodarostestesdoRSpecagora,vemosqueelesestãopassando. Emelhor
ainda,serodarmosostestesdoCucumber,vemosqueoprimeirocenáriovoltoua
passar!
$ bundle exec cucumber
(...)
2 scenarios (1 failed, 1 passed)
Ouseja,agorafinalmentepodemosvoltaratrabalharnocenárioquedefinimos
nocomeçodestecapítulo,ocenário "Sorteio da palavra com sucesso”. Masvamos
fazerissosónopróximocapítulo.
6.9 P ontos-chave deste capítulo
Nessecapítulo,nóscontinuamosaespecificaraprimeirafuncionalidadedopro-
grama, "Começar Jogo”.Aodefinirumnovocenárioparaessafuncionalidade,usa-
mososupportcodedoCucumberparaevitarduplicaç ãonacamadadestepdefini-
tions.
Outropontoimportante,équetivemosqueadaptarnossostestescomCucum-
berparaqueelesrefletissemarealidadedonossoprograma,queestavaquebrando
na“vidareal”,maspassandonostestes. Terofeedbackcorretodostestesémuito
129

## Página 144

6.9. Pontos-chavedestecapítulo CasadoCódigo
importante,poiscasoissonãosejafeito,aspessoaspodemcome çaraperderacon-
fiançanasuítedetestes.
NostestescomRSpec,vimoscomousaro subjecteo letparaevitardupli-
caçãodecódigonostestes.
Porfim,refatoramosaclasse Game,extraindoumanovadependência,aclasse
CliUi.Dessemodoficoumaisfácildefazernossostestes.Alémdisso,aoretirarmos
essaresponsabilidadedaclasse Game,adeixamosmenosacopladacomo inpute
outputcomusuário.
Essarefatoraçãoresultouemumdesigncommenoracoplamento.Essamelho-
rianodesignpodenosajudarcomrequisitosfuturos,porexemplo,seainterface
comusuáriomudassedelinhadecomandoparaTwitter,agorapodemosfazerisso
simplesmentetrocandoaclasse CliUiporumaclasse TwitterUi.
Comtudoissofeito,estamosprontosparanocapítuloseguintefinalizaraespe-
cificaçãoeimplementaçãodaprimeirafuncionalidade.
130

## Página 145

Capítulo7
Finalizandoaprimeira
funcionalidade
Nocapítuloanterior,nósdefinimososegundocenáriodaprimeirafuncionalidade.
Noentanto,nãopudemosimplementá-lo,poisfoinecessáriofazerumasériedemo-
dificaçõeserefatoraçõesparaquepudéssemoscomeçaratrabalharnessenovoce-
nário.
Nestecapítulo,iremosimplementaresseeoterceirocenário,finalizandoassim
essafuncionalidade. Aofinaldocapítuloojogadorjávaipoderiniciarumjogoe
sortearumapalavraparaeleadivinhar.
Sigam-meosbons!
7 .1 C ontinuando o segundo cenário
Antesdeirmosparaopróximopasso,vamosvercomoestãonossostestes.Aoro-
darmosoRSpec,podemosverqueestátudoverde. Porém,aorodaroCucumber,

## Página 146

7.2. Deixandoosegundocenárionoverde CasadoCódigo
vemososeguinte:
$ bundle exec cucumber
Dado que comecei um jogo
Quando escolho que a palavra a ser sorteada deverá ter "4" letras
E termino o jogo
Então o jogo termina com a seguinte mensagem na tela:
"""
_ _ _ _
"""
expected "Bem vindo ao jogo da forca!\n
Qual o tamanho da palavra a ser sorteada?\n
Qual o tamanho da palavra a ser sorteada?\n"
to include "_ _ _ _"
2 scenarios (1 failed, 1 passed)
Ouseja,oprimeirocenárioestápassandoeosegundoestáquebrando.Porquê?
Elequebrou,poisfaltaimprimirnatelaum "_"paracadaletradapalavrasorteada.
Vamosfazerisso!
7 .2 D eixando o segundo cenário no verde
Parafazeressesegundocenáriopassarénecessárioqueonossojogosorteieuma
palavraeimprimanatelaum“_”paracadaletradapalavrasorteada. Issodeve
acontecercomopassoseguinteapósjogadordizerqualotamanhodapalavraaser
sorteada.Logoessecomportamentofarápartedométodo Game#next_step.
Podemosestruturarostestesparaessecomportamentodoseguintemodono
arquivo spec/game_spec.rb:
describe "#next_step" do
# (...)
context "when the player asks to raffle a word" do
it "raffles a word with the given length"
it "prints a '_' for each letter in the raffled word"
132

## Página 147

CasadoCódigo Capítulo7. Finalizandoaprimeirafuncionalidade
end
# (...)
end
Para implementar o primeiro teste (it "raffles a word with the
given length")podemoschecarsedadoqueojogadorinputaotamanhodapa-
lavracomo "3",entãoapalavrasorteadadodeveráter3letras:
describe "#next_step" do
# (...)
context "when the player asks to raffle a word" do
it "raffles a word with the given length" do
word_length = "3"
ui.stub(read: word_length)
game.next_step
game.raffled_word.should have(word_length).letters
end
it "prints a '_' for each letter in the raffled word"
end
# (...)
end
AorodaroRSpec,otestequebraevemososeguinte:
$ bundle exec rspec
Failures:
1) Game#next_step when the player asks to raffle a word raffles a word
with the given length
Failure/Error: game.raffled_word.should have(word_length).letters
NoMethodError:
undefined method `raffled_word' for #<Game:0x007fc3facf85d0>
133

## Página 148

7.2. Deixandoosegundocenárionoverde CasadoCódigo
Ouseja,faltaimplementarmosométodoqueretornaráapalavrasorteada,o
método Game#raffled_word. Façaissoadicionandooseguintenocome çodo
arquivo lib/game.rb:
class Game
attr_accessor :raffled_word
end
AorodarmosoRSpecnovamente,elequebracomaseguintemensagemdeerro:
$ bundle exec rspec
Failures:
1) Game#next_step when the player asks to raffle a word raffles a word
with the given length
Failure/Error: game.raffled_word.should have(word_length).letters
NoMethodError:
undefined method `letters' for nil:NilClass
Ouseja,nãofoipossívelverificarquantasletrasapalavrasorteadatem,poisnão
existeumapalavrasorteadaainda. Paraotestepassar,precisamosqueométodo
next_stepsorteiaumapalavracomotamanhodadopelojogador. Modifiqueo
métodoGame#next_stepparaqueelefaçaisso:
def next_step
@ui.write("Qual o tamanho da palavra a ser sorteada?")
player_input = @ui.read.strip
if player_input == "fim"
@ended = true
else
word_length = player_input.to_i
words = %w(hi mom game fruit)
@raffled_word = words.detect { |word| word.length == word_length }
end
end
Implementamos a seguinte condição no código acima: se o adivi-
nhar_letra.featurenãodigitou "fim",entãoeledigitouotamanhodapalavraa
134

## Página 149

CasadoCódigo Capítulo7. Finalizandoaprimeirafuncionalidade
sersorteada.Apósisso,usamosesseinputparasortearumapalavraesalvarelaem
@raffled_word.
Aorodarostestes,vemosqueagoraelespassam!Masantesdeseguiremfrente,
vamosrefatorarnossocódigoparaficarmaisclaroainten çãodele.
Aolerotrechodecódigoaseguir:
word_length = player_input.to_i
words = %w(hi mom game fruit)
@raffled_word = words.detect { |word| word.length == word_length }
Podemospensarumpoucoeentenderqueoqueeleestáfazendoésorteara
palavra. Masaintençãodessecódigo(o queelefaz,enão comoelefaz)poderia
estarmaisexplícitaparaquemolerá.Paradeixarainten çãodessetrechodecódigo
maisexplícita,vamosrefatorá-lo,extraindoessetrechoparaummétodoprivado
chamado raffle_word:
def next_step
@ui.write("Qual o tamanho da palavra a ser sorteada?")
player_input = @ui.read.strip
if player_input == "fim"
@ended = true
else
raffle_word(player_input.to_i)
end
end
private
def raffle_word(word_length)
words = %w(hi mom game fruit)
@raffled_word = words.detect { |word| word.length == word_length }
end
AorodaroRSpec,vemosqueelecontinuanoverde,ouseja,refatoramossem
quebrarnada.Vamosparaopróximospecpendente,queéo ’it “prints a ‘_’ for each
letter in the raffled word"’.
Essetesteiráverificarseojogoestáimprimindoumcaractere“_”paracadaletra
dapalavrasorteada.Implementeessetestedoseguintemodo:
it "prints a '_' for each letter in the raffled word" do
word_length = "3"
135

## Página 150

7.2. Deixandoosegundocenárionoverde CasadoCódigo
ui.stub(read: word_length)
ui.should_receive(:write).with("_ _ _")
game.next_step
end
AorodaroRSpec,elafalharácomaseguintemensagem:
$ bundle exec rspec
Failures:
1) Game#next_step when the player asks to raffle a word
prints a '_' for
each letter in the raffled word
Failure/Error: ui.should_receive(:write).with("_ _ _")
Double "ui" received :write with unexpected arguments
expected: ("_ _ _")
got: ("Qual o tamanho da palavra a ser sorteada?")
Amensagemnosdizqueoobjeto uideveriaterrecebidoamensagem write
comoargumento '_ _ _',masnãorecebeu.Vamosescreverummétodochamado
print_letters_feedbackquevaiserresponsávelporimprimirofeedbackdas
letrasadivinhadas,queseráinicialmenteum“_”paracadaletradapalavrasorteada.
Essemétododeveserchamadologoapósapalavrasersorteada. Adicionandoa
chamadadessemétodo,nossocódigoficaráassim:
1 def next_step
2 @ui.write("Qual o tamanho da palavra a ser sorteada?")
3 player_input = @ui.read.strip
4
5 if player_input == "fim"
6 @ended = true
7 else
8 raffle_word(player_input.to_i)
9 print_letters_feedback
10 end
11 end
Ométodo print_letters_feedbackseráummétodoprivadoeaimple-
mentaçãodeleficaráassim:
136

## Página 151

CasadoCódigo Capítulo7. Finalizandoaprimeirafuncionalidade
def next_step
# (...)
end
private
# (...)
def print_letters_feedback
letters_feedback = ""
@raffled_word.length.times do
letters_feedback << "_ "
end
letters_feedback.strip!
@ui.write(letters_feedback)
end
Aorodarasuíte,vemosqueoteste ’it “prints a ‘_’ for each letter in the raffled
word"’,masoutroquebrou:
$ bundle exec rspec
Failures:
1) Game#next_step when the game just started asks the player for the
length of the word to be raffled
Failure/Error: game.next_step
NoMethodError:
undefined method `length' for nil:NilClass
# ./lib/game.rb:43:in `print_letters_feedback'
# ./lib/game.rb:30:in `next_step'
# ./spec/game_spec.rb:34:
Comopodemosvernamensagemdeerrodoteste,oproblemaocorreunacha-
madodométodo length,dentrodométodo print_letters_feedback:
def print_letters_feedback
letters_feedback = ""
137

## Página 152

7.2. Deixandoosegundocenárionoverde CasadoCódigo
@raffled_word.length.times do
letters_feedback << "_ "
end
letters_feedback.strip!
@ui.write(letters_feedback)
end
Essetestequebrouporqueneleavariáveldeinstância @raffled_wordestá
nil.Paraentenderporqueissoaconteceu,vamosdarumaolhadanotestequeque-
brou:
describe "#next_step" do
context "when the game just started" do
it "asks the player for the length of the word to be raffled" do
question = "Qual o tamanho da palavra a ser sorteada?"
ui.should_receive(:write).with(question)
ui.should_receive(:read)
game.next_step
end
end
# (...)
end
Lendo o teste, vemos que em nenhum momento é setado o que o método
ui.readiráretornar.Mas,paraqueumapalavrasejasorteadaeavariáveldeins-
tância @raffled_wordsejasetada,énecessárioqueessemétodoretornealgo,que
seráotamanhodapalavraasersorteada.Esseéoproblemaqueprecisamosconser-
tar.
Para que o ui.read retorne o tamanho da palavra, vamos
mudar a linha que estava ui.should_receive(:read) para
ui.should_receive(:read).and_return(word_length):
describe "#next_step" do
context "when the game just started" do
it "asks the player for the length of the word to be raffled" do
138

## Página 153

CasadoCódigo Capítulo7. Finalizandoaprimeirafuncionalidade
question = "Qual o tamanho da palavra a ser sorteada?"
ui.should_receive(:write).with(question)
word_length = "3"
ui.should_receive(:read).and_return(word_length)
game.next_step
end
end
# (...)
end
AorodaroRSpecnovamente,podemosverqueeleestánoverde. E,aorodar
oCucumber,podemosverqueeletambémestánoverde!Terminamososegundo
cenáriodaprimeirafuncionalidadedonossojogo!Comoocenárioestánoverde,já
podemostiraratag @wipdele.
Comtudonoverde,vamosparaopróximocenário.
7 .3 Finalizando a primeira funcionalidade
Aprimeirafuncionalidadedonossojogoéa“Come çarjogo”,queconsistenosse-
guintescenários:
1) Começodenovojogocomsucesso;
2) Sorteiodapalavracomsucesso;
3) Sorteiodapalavrasemsucesso.
Osdoisprimeiroscenáriosjáestãonoverde. Vamoscome çaraespecificare
implementaroúltimocenário.
Adicioneoseguintecenárionoarquivo features/comecar_jogo.feature:
@wip
Cenário: Sorteio da palavra sem sucesso
Se o jogador pedir pro jogo sortear uma palavra com um tamanho
que o jogo não tem disponível, o jogador deve ser avisado disso
e o jogo deve pedir pro jogador sortear outra palavra.
139

## Página 154

7.3. Finalizandoaprimeirafuncionalidade CasadoCódigo
Dado que comecei um jogo
Quando escolho que a palavra a ser sorteada deverá ter "20" letras
E termino o jogo
Então o jogo termina com a seguinte mensagem na tela:
"""
Não temos uma palavra com o tamanho desejado,
é necessário escolher outro tamanho.
Qual o tamanho da palavra a ser sorteada?
"""
AorodaroCucumber,vemosqueelequebraparaessenovocenário:
$ bundle exec cucumber -t @wip
1 scenario (1 failed)
Comodecostume,quandotemosumtestenovodeCucumberquebrando,o
próximopassoéescreverumtestedeRSpecefazê-lopassar.Vamosfazerisso.
Vamosescreverumtestequevaiverificarocenárioquandoojogadorpedepara
sersorteadoumapalavracomumtamanhoqueojogonãotem.Paraimplementar
esseteste,adicioneoseguintenoarquivo spec/game_spec.rb:
describe "#next_step
" do
# (...)
context "when the player asks to raffle a word" do
# (...)
it "tells if it's not possible to raffle with the given length" do
word_length = "20"
ui.stub(read: word_length)
error_message = "Não temos uma palavra com o tamanho " <<
"desejado,\n" <<
"é necessário escolher outro tamanho."
ui.should_receive(:write).with(error_message)
game.next_step
end
140

## Página 155

CasadoCódigo Capítulo7. Finalizandoaprimeirafuncionalidade
end
end
AorodaroRSpec,podemosconfirmarqueonovotesteestávermelho.Vamos
fazê-lopassar.Aimplementaçãoatualdo Game#next_stepestáassim:
def next_step
@ui.write("Qual o tamanho da palavra a ser sorteada?")
player_input = @ui.read.strip
if player_input == "fim"
@ended = true
else
raffle_word(player_input.to_i)
print_letters_feedback
end
end
Precisamosalterá-laparasenãoforpossívelsortearumapalavracomotamanho
pedido,entãoumamensagemdeerrodeveserimpressaparaojogador.Parafazer
isso,bastachecaroretornodométodo raffle_word,sefor false,entãoamen-
sagemdeerrodeveserimpressaprojogador.Altereométodo Game#next_step
doseguintemodoparaimplementaressaideia:
def next_step
@ui.write("Qual o tamanho da palavra a ser sorteada?")
player_input = @ui.read.strip
if player_input == "fim"
@ended = true
else
if raffle_word(player_input.to_i)
print_letters_feedback
else
error_message = "Não temos uma palavra com o tamanho " <<
"desejado,\n" <<
"é necessário escolher outro tamanho."
@ui.write(error_message)
end
end
end
141

## Página 156

7.4. Pontos-chavedestecapítulo CasadoCódigo
Reparequefoinecessáriofazerum if ... elsedentrodo elsejáexistente
parafazerotestepassar. Condicionaisaninhadassãoummalsinal,mostraqueo
códigoestácomplexo. Precisamosrefatorarisso,masporenquantovamosdeixar
assim.
Comaimplementaçãoacima,aorodarmosoRSpec,vemosqueelepassacom
tudonoverde.E,aorodaroCucumber,vemosqueeletambémestá100%verde!
$ bundle exec cucumber
(...)
3 scenarios (3 passed)
Finalmenteafuncionalidadedecome çarojogoestátotalmentepronta! Mas,
antesdecontinuaracomemoração,nãoseesque çadetiraratag @wipdocenário
queacabamosdefinalizar.
Comtodosostestesnoverde,estamosprontospararefatorar.Iremosfazerisso
sónopróximocapítulo.
Enquantovocêdescansaumpoucoesepreparaparaopróximocapítulo,apro-
veitetambémparabrincarcomoquetemosprontoatéagora.Bastarodarobinário
dojogo bin/forcaeexploraraprimeirafuncionalidade.
7 .4 P ontos-chave deste capítulo
Nessecapítulonósconseguimosfinalizaraespecificaç ãoeimplementaçãodapri-
meirafuncionalidade.
Duranteaimplementação,vimoscomorefatorarnossocódigoparadeixarmais
claraasuainten ção,atravésdaextraçãodemétodosprivados.
Porfim,nofinaldaimplementação,foinecessáriofazermaiscondicionaisani-
nhadasdoquegostamos,deixandonossocódigomaiscomplexo. Nocapítulose-
guinte,vamosrefatorarnossocódigoparaeliminaresseeoutrosdébitostécnicos
quenossocódigopossater.
142

## Página 157

Capítulo8
Refatorandonossocódigo
Nocapítuloanteriornósterminamosaespecificaç ãoeimplementaçãodaprimeira
funcionalidade.Noentanto,algumaspartesdocódigoquedesenvolvemosatéagora
podemsermelhoradas.
Nestecapítulonósvamosidentificarquepartespodemsermelhoradas,refatorar
nossocódigoemelhoraraarquiteturadonossoprojeto.Tudoissocomsuporteda
nossasuítedetestes,queirágarantirquenãoiremosquebrarnenhumafuncionali-
dadeenquantomelhoramosaqualidadedenossocódigo.
8.1 I dentificado os pontos a serem refatorados
Nofinaldaimplementaçãodocenárioanterior,notamosqueumapartedonosso
código não ficou tão boa quanto queremos, essa parte está dentro do método
Game#next_step:
def next_step
@ui.write("Qual o tamanho da palavra a ser sorteada?")

## Página 158

8.1. Identificadoospontosaseremrefatorados CasadoCódigo
player_input = @ui.read.strip
if player_input == "fim"
@ended = true
else
if raffle_word(player_input.to_i)
print_letters_feedback
else
error_message = "Não temos uma palavra com o tamanho " <<
"desejado,\n" <<
"é necessário escolher outro tamanho."
@ui.write(error_message)
end
end
end
Essemétodoestácommuitascondicionaisaninhadas,oquedificultaoenten-
dimentodométodoeaumentasuacomplexidade. Esseéumpossívelpontoaser
refatorado.
Outrapontoquevaleapenaseravaliadoéoconjuntodemétodosprivadosda
classe Game:
class Game
# (...)
private
def raffle_word(word_length)
words = %w(hi mom game fruit)
@raffled_word = words.detect { |word| word.length == word_length }
end
def print_letters_feedback
letters_feedback = ""
@raffled_word.length.times do
letters_feedback << "_ "
end
letters_feedback.strip!
144

## Página 159

CasadoCódigo Capítulo8. Refatorandonossocódigo
@ui.write(letters_feedback)
end
end
Métodosprivadosemexcessopodeserumindícioqueaclasseestácommaisde
umaresponsabilidadeequeumadassuasresponsabilidadesestáescondidadesua
APIpúblicaatravésdemétodosprivados. Talvezessesmétodosprivadossãomais
umpontopossívelderefatoração.
Porfim,paratermosmaisfeedbacksobreaqualidadedenossocódigo,pode-
mosolhartambémparaostestes.Testespodemdarumótimofeedback,poisneles
onossocódigoéutilizadoassimcomoseriautilizadoporoutrapartedonossosoft-
ware,entãonotesteficabemclaro,porexemplo,seésimplesounãodeutilizaro
códigoquefizemos.
Vamosdarumaolhadanostestesdaclasse Game:
Game
#start
prints the initial message
#ended?
returns false when the game just started
#next_step
finishes the game when the player asks to
when the game just started
asks the player for the length of the word to be raffled
when the player asks to raffle a word
raffles a word with the given length
prints a '_' for each letter in the raffled word
tells if it 's not possible to raffle with the given length
Aprimeiracoisaquepodemosnotarnostestesdaclasse Gameéqueamaio-
riadelesérelacionadaaocomportamentodométodo next_step. Essemétodo
implementaoseguintecomportamento:
• mostrarumainformaçãoparaojogador
• pediruminputdojogador
• fazeralgumprocessamentointernodojogo
• depoismostraroutrainformaçãoparaojogador
145

## Página 160

8.2. Extraindoumaclassedeummétodoprivado CasadoCódigo
• eassimconsecutivamente
Essecomportamentoébasicamenteofluxodojogo.
Tirandoostestesdo next_step,sósobramdois,umdo starteumdo
ended?. Odo starttestaseéimpressoamensageminicialparaojogador,ou
seja,tambémestárelacionadoainteraçãocomousuárioeaofluxodojogo. Odo
ended?verificaseojogoacabouounão,ouseja,érelacionadocomoestadodo
objeto game.
Amaioriadostestesdaclasse gameésobreofluxodojogoeinteraç ãocom
usuário,sóumésobreoestadodoobjeto game.Ouseja,umobjetodaclasse Game
cuidadofluxodojogo,dainteraç ãocomousuárioetambémdeguardaroestado
dojogo.Issoestáestranho,podeserumindíciodefaltadecoesãoequeaclasseestá
implementandomaisdeumaresponsabilidade.
Vamoscomeçaraatacarcadaumdospontoslevantadoserefatorarondefor
necessário.
8.2 E xtraindo uma classe de um método priv ado
Oprimeiropontoqueiremosanalisarserãoosmétodosprivados,maisespecifica-
mente,ométodo Game#raffle_word.
AolerocódigodaclasseGame,podemosnotarqueelaestáfazendopelomenos
3coisas:
• Interagecomousuárioeexecutaasaçõesnecessáriasbaseadonoinputdo
usuário.Todaapartedo next_stepporexemplo.
• Conheceoestadodojogo:métodoended?evariáveldeinstância @ended
• Sorteiaumapalavra:métodoraffle_word
Secadaumadessaspartestiverumnovorequisito,aclassevaiterquesermodi-
ficada,logooprincípiodaresponsabilidadeúnica(SingleResponsibilityPrinciple-
SRP[9])estásendoquebrado.Porexemplo,imagineseoprocessodesortearuma
palavranãosejamaissorteardeumarray hard-codednocódigo,massimsortear
atravésdacomunicaçãocomumwebservicesorteadordepalavras.Seissoaconte-
cesse,serianecessáriomudaraclasse Game.
Outromotivopararefatorarmosométodo Game#raffle_wordéquepelofato
deleserummétodoprivado,nãopudemosfazertestesdeunidadeparaele.Vistoque
146

## Página 161

CasadoCódigo Capítulo8. Refatorandonossocódigo
essemétodoimplementaumcomportamentoimportante,elemerecetestes.Sevocê
sentiranecessidadedetestarummétodoprivado,podeserumsinaldequevalea
penaextrairessemétodoparasuaprópriaclasse.Eéissoquevamosfazer.
Comecemodificandoumapartedostestesdaclassegameparaficarassim:
1 describe Game do
2 let(:ui) { double("ui").as_null_object }
3 let(:word_raffler) { double("raffler").as_null_object }
4
5 subject(:game) { Game.new(ui, word_raffler) }
6
7 # (...)
8
9 describe "#next_step" do
10 # (...)
11
12 context "when the player asks to raffle a word" do
13 it "raffles a word with the given length" do
14 word_length = "3"
15 ui.stub(read: word_length)
16
17 word_raffler.should_receive(:raffle).with(word_length.to_i)
18
19 game.next_step
20 end
21
22 it "prints a '_' for each letter in the raffled word" do
23 word_length = "3"
24 ui.stub(read: word_length)
25 word_raffler.stub(raffle: "mom")
26
27 ui.should_receive(:write).with("_ _ _")
28
29 game.next_step
30 end
31
32 it "tells if it's not possible to raffle with the given length" do
33 word_length = "20"
34 ui.stub(read: word_length)
35 word_raffler.stub(raffle: nil)
36
147

## Página 162

8.2. Extraindoumaclassedeummétodoprivado CasadoCódigo
37 error_message = "Não temos uma palavra com o tamanho " <<
38 "desejado,\n" <<
39 "é necessário escolher outro tamanho."
40
41 ui.should_receive(:write).with(error_message)
42
43 game.next_step
44 end
45 end
46
47 # (...)
48 end
49 end
Vamos entendero que fizemos nocódigo acima. Primeiro, na linha 3nós
deixamos explícito que o objetogame tem um novo colaborador, o objeto
word_raffler,quevaiteropapeldesorteadordepalavras. Alémdedeixarde-
pendênciaexplícita,tambémainjetamosnoobjeto gamenalinha5.
Apósexplicitaressadependência,foinecessárioidentificarquaisostestesque
seriamafetadosporessarefatoraçãoeadaptá-los. Otestedalinha13testaseuma
palavravaisersorteadacomotamanhodado.Comoeleérelacionadoaosorteioda
palavrativemosqueadaptaresseteste.Paraadaptá-lo,nalinha17usamosmocksdo
RSpecparaverificarseamensagemcertaestavasendoenviadaparaanovadepen-
dênciaword_raffler
Otestedalinha22testasefoiimpressoum“_”paracadaletradapalavrasor-
teada. Comoessetestetambémestáatreladoaoprocessodesortearpalavra,tam-
bémtivemosqueadaptá-lo. Nalinha25,foinecessáriofazerumstubdométodo
word_raffler.rafflepararetornarapalavra "mom”,queseriaapalavrasor-
teada. Nessecasousamos stubenão mockpoisotestenãoésobreverificarquea
mensagem rafflefoienviadaparaoobjeto word_raffler. Usarstubsserve
sóparasetaroretornodealgumadependência,jáusarmocksserveparatestarsea
interaçãocomumadependênciafoifeitacorretamente.
Notestedalinha32étestadoocomportamentodequandonãoépossívelsortear
umapalavracomotamanhopedido.Paraadaptá-lo,bastoufazerumstubdométodo
word_raffler.rafflepararetornar nil.Esseretornode nilquerdizerqueo
word_rafflernãopôdesortearumapalavracomotamanhopedido.Aofazermos
essestubestamosinclusivedefinindooprotocolodecomunicaç ãoentreoobjeto
gameeoobjeto word_raffler.
148

## Página 163

CasadoCódigo Capítulo8. Refatorandonossocódigo
Apóstodasessasmodificaçõesnostestes,vamosrodá-loseveroqueprecisare-
mosmudar:
$ bundle exec rspec
(...)
Failure/Error: subject(:game) { Game.new(ui, word_raffler) }
ArgumentError:
wrong number of arguments (2 for 1)
(...)
7 examples, 7 failures
Todosostestesquebraram.Amensagemdeerronosmostraqueoproblemaé
queoconstrutordaclasse Gamesóaceitaumargumento.Vamosmodificá-lopara
podermosinjetaranovadependência.Editeométodo initializedaclasse Game
afimdeinjetaradependência word_raffler,eledeveficarassim:
class Game
# (...)
def initialize(ui = CliUi.new, word_raffler = WordRaffler.new)
@ui = ui
@word_raffler = word_raffler
@ended = false
end
# (...)
end
Aorodarostestesnovamente,vemososeguinte:
$ bundle exec rspec
Failures:
1) Game#next_step when the player asks to raffle a word raffles a word
with the given length
Failure/Error:
149

## Página 164

8.2. Extraindoumaclassedeummétodoprivado CasadoCódigo
word_raffler.should_receive(:raffle).with(word_length.to_i)
(Double "raffler").raffle(3)
expected: 1 time
received: 0 times
# ./spec/game_spec.rb:45
7 examples, 1 failure
Agorasomenteumtestequebrou. Oproblemafoiqueotesteestáverificando
seamensagem rafflefoienviadaparaoobjeto word_raffler,maselanãofoi
enviada.Vamosmodificaraclasse Gameparaqueelapossausaranovadependência
enãotermaisométodoprivado. Editeométodo Game#next_stepnoarquivo
lib/game.rbparaficarassim:
1 def next_step
2 @ui.write("Qual o tamanho da palavra a ser sorteada?")
3 player_input = @ui.read.strip
4
5 if player_input == "fim"
6 @ended = true
7 else
8 if @raffled_word = @word_raffler.raffle(player_input.to_i)
9 print_letters_feedback
10 else
11 error_message = "Não temos uma palavra com o tamanho " <<
12 "desejado,\n" <<
13 "é necessário escolher outro tamanho."
14
15 @ui.write(error_message)
16 end
17 end
18 end
Nalinha8modificamosocódigoparausaroobjeto @word_raffleraoinvés
dechamarométodoprivado.Aproveiteedeleteoantigométodoprivado.
AorodarmosoRSpec,podemosverqueestátudonoverde! Vamosrodaro
Cucumber:
$ bundle exec cucumber
150

## Página 165

CasadoCódigo Capítulo8. Refatorandonossocódigo
Exit status was 1 but expected it to be 0. Output:
forca/lib/game.rb:8:in `initialize':
uninitialized constant Game::WordRaffler (NameError)
from forca/bin/forca:7:in `new'
from forca/bin/forca:7:in `<main>'
3 scenarios (3 failed)
TodosostestesdoCucumberquebraram.Ostestesdeunidadedaclasse Game
passaramporqueelesestãotestandoessaclasseisoladadassuasdependências,atra-
vésdetestdoubles(mocksestubs).JáosdodoCucumberquebraramporqueeles
testamosoftwarecomoeleé,incluindoaintegraç ãoentreosobjetos.
AmensagemdeerrodoCucumberestánosdizendoquenãoexisteumacons-
tante Game::WordRaffler,ouseja,queaclasse WordRafflernãofoiimple-
mentada.Vamoscontinuarnossarefatoraçãoeimplementá-la.
Crieoarquivo spec/word_raffler_spec.rbcomosseguintestestespara
essanovaclasse:
# encoding: UTF-8
require 'spec_helper'
require 'word_raffler'
describe WordRaffler do
it "raffles a word from a given list of words" do
words = %w(me you nice)
raffler = WordRaffler.new(words)
raffler.raffle(3).should == "you"
raffler.raffle(2).should == "me"
raffler.raffle(4).should == "nice"
end
it "returns nil if it doesn 't have a word with the given length" do
words = %w(me you nice)
raffler = WordRaffler.new(words)
151

## Página 166

8.2. Extraindoumaclassedeummétodoprivado CasadoCódigo
raffler.raffle(20).should be_nil
end
end
Parafazerotestepassar,crieumarquivo lib/word_raffler.rbcomose-
guinteconteúdo:
# encoding: UTF-8
# Classe responsável por sortear uma palavra de uma dada lista de
# palavras.
#
class WordRaffler
def initialize(words = %w(hi mom game fruit))
@words = words
end
def raffle(word_length)
@words.detect { |word| word.length == word_length }
end
end
AorodaroRSpec,podemosverqueestánoverde. Percebaquealógicado
métodoraffledessanovaclasseéexatamenteigualadoantigométodoprivado
Game#raffle_word.Ouseja,sóextraímosoantigométodoparaessanovaclasse.
Outracoisaquefizemosfoideixarcomocomentárionocome çodaclasseasua
responsabilidade.Gostodefazerissoparadeixarbemclaroqualaresponsabilidade
daclasseemquestão. Aoescrevermosessetexto,nosfor çamosapensarsobreas
responsabilidadesdessaclasseepodemosverificarseelaestáacumulandomaisde
uma.
Aúltimacoisaquefaltafazerparaterminaressarefatoraç ãoédarum require
danovaclasseparaaclasse Game.Parafazerisso,adicioneo require_relative
'word_raffler'nocomeçodaclasseGameparaficarassim:
# encoding: UTF-8
require_relative 'cli_ui'
require_relative 'word_raffler'
class Game
152

## Página 167

CasadoCódigo Capítulo8. Refatorandonossocódigo
# (...)
end
AorodaroCucumberagora,podemosverqueestátotalmenteverde!Finaliza-
mosoprimeiropontoderefatoração.Vamosparaopróximo.
8.3 D istribuindo responsabilidades para outras
classes
Naseçãoanterioridentificamosqueaclasse Gametinhapelomenostrêsresponsa-
bilidades:
• Interagircomousuárioeexecutarasaçõesnecessáriasbaseadonoinputdo
usuário.Todaapartedo next_stepporexemplo.
• Conheceroestadodojogo:métodoended?evariáveldeinstância @ended
• Sortearumapalavra:métodoraffle_word
Aresponsabilidadedesortearumapalavranósjáextraímos,deletandoummé-
todoprivadoecriandoumanovaclassesóparaessaresponsabilidade.
Opróximopontoseráextrairalógicadefluxodojogodaclasse Game.Aideia
équeessaclassefiquesomentecomaresponsabilidadedeguardaroestadodojogo
easregrasdenegóciodeledemodogeral.
Paracomeçar,vamosretirardaclasse Gamealógicarelacionadoaofluxodo
jogo e interação com usuário. Comece criando um arquivo de teste chamado
spec/game_flow_spec.rbemovaostestesdométodo starte next_step
doarquivo spec/game_spec.rbparaessenovoarquivo.Alémdemoverostes-
tes,teremosquefazeralgumasadaptaçõesneles.Vamosmoverdepoucoapoucoos
testeseentenderasmodificaçõesnecessárias.
Oprimeirotestequeiremosmoverseráodométodo start,queficaráassim
nonovoarquivo spec/game_flow_spec.rb
1 # encoding: UTF-8
2
3 require 'spec_helper'
4 require 'game_flow'
5
153

## Página 168

8.3. Distribuindoresponsabilidadesparaoutrasclasses CasadoCódigo
6 describe GameFlow do
7 let(:ui) { double("ui").as_null_object }
8 let(:game) { double("game").as_null_object }
9
10 subject(:game_flow) { GameFlow.new(game, ui) }
11
12 describe "#start" do
13 it "prints the initial message" do
14 initial_message = "Bem vindo ao jogo da forca!"
15 ui.should_receive(:write).with(initial_message)
16
17 game_flow.start
18 end
19 end
20
21 # (...)
22 end
Alémdemoveressetestedaclasse Gameparaotestedanovaclasse GameFlow,
nalinha17tivemosquefazerumaadaptaç ão,mudandoondeantesera gamepara
ficar game_flow.
Outropontoquevalenotaréaconstruç ãodoobjeto game_flownalinha10,
percebaqueeledependetantode gamequandode ui.Issoporquearesponsabi-
lidadedessenovoobjetoécuidardainteraç ãocomoousuárionecessáriadurante
ofluxodojogoe,aolongodofluxodojogo,enviarasmensagensnecessáriaparao
objeto game,queéquemvaicuidardasregrasdojogoemsi.
Após movermos os testes do métodostart, vamos mover os do método
next_step,evamosolharcomocadaumaficará.Oprimeirotesteficaráassim:
1 describe GameFlow do
2 # (...)
3
4 describe "#next_step" do
5 context "when the game just started" do
6 it "asks the player for the length of the word to be raffled" do
7 question = "Qual o tamanho da palavra a ser sorteada?"
8 ui.should_receive(:write).with(question)
9
10 word_length = "3"
11 ui.should_receive(:read).and_return(word_length)
154

## Página 169

CasadoCódigo Capítulo8. Refatorandonossocódigo
12
13 game_flow.next_step
14 end
15 end
16
17 # (...)
18 end
19 end
Paraesseteste,aúnicaadaptaç ãoquetivemosquefazerfoinalinha13,onde
mudamosde gamepara game_flow.
Otesteseguintequeiremosmoverficaráassim:
1 describe GameFlow do
2 # (...)
3
4 describe "#next_step" do
5 context "when the player asks to raffle a word" do
6 it "raffles a word with the given length" do
7 word_length = "3"
8 ui.stub(read: word_length)
9
10 game.should_receive(:raffle).with(word_length.to_i)
11
12 game_flow.next_step
13 end
14 end
15
16 #(...)
17 end
18 end
Nalinha10desseteste,tivemosquemudarondeestava word_rafflerpara
game.Issoporquequemusarádiretamenteo word_rafflerésóoobjeto game.
O game_flowpedeparao gamesortearumapalavraeoobjeto gameusao
word_rafflerparaisso.Devidoaessanovacadeiaderesponsabilidades,seráne-
cessárioqueo gameimplementeummétodo raffle,queatéentãonãoexistia.
Opróximotesteasermovidoficaráassim:
1 describe GameFlow do
2 # (...)
155

## Página 170

8.3. Distribuindoresponsabilidadesparaoutrasclasses CasadoCódigo
3
4 describe "#next_step" do
5 context "when the player asks to raffle a word" do
6 it "prints a '_' for each letter in the raffled word" do
7 word_length = "3"
8 ui.stub(read: word_length)
9 game.stub(raffle: "mom", raffled_word: "mom")
10
11 ui.should_receive(:write).with("_ _ _")
12
13 game_flow.next_step
14 end
15 end
16
17 #(...)
18 end
19 end
Nalinha9desseteste,tivemosquefazerumstubnoobjeto game,porémantesde
moveroteste,nósfazíamosessestubnoobjeto word_raffler.Estamosfazendo
ostubnoobjeto gameporqueelequeéadependênciadiretado game_flowenão
o word_raffler.
Oúltimotestequevamosmoveranalisandocomdetalheséoseguinte:
1 describe GameFlow do
2 # (...)
3
4 describe "#next_step" do
5 it "finishes the game when the player asks to" do
6 player_input = "fim"
7 ui.stub(read: player_input)
8
9 game.should_receive(:finish)
10
11 game_flow.next_step
12 end
13
14 #(...)
15 end
16 end
156

## Página 171

CasadoCódigo Capítulo8. Refatorandonossocódigo
Essetesteverificaseojogoéterminadoquandoojogadordigita“fim”.Antesnós
fazíamosessaverificaçãoolhandooestadodoobjeto game,fazendo game.should
be_ended.Apósmoverotesteparaoarquivo spec/game_flow_spec.rb,não
devemosmaistestaroestadodoobjeto game,jáquenãoéeleoobjetosobteste.
Entãoparafazeressetesteestamosverificandoseamensagemcertaestásendoenvi-
adaparaoobjeto game,comovocêpodevernalinha9.Essetesteesperaqueobjeto
gametenhaummétodo Game#finish,queaindaprecisaserimplementado.
O resultado final dos testes que movemos para o arquivo
spec/game_flow_spec.rbficaráassim:
# encoding: UTF-8
require 'spec_helper'
require 'game_flow'
describe GameFlow do
let(:ui) { double("ui").as_null_object }
let(:game) { double("game").as_null_object }
subject(:game_flow) { GameFlow.new(game, ui) }
describe "#start" do
it "prints the initial message" do
initial_message = "Bem vindo ao jogo da forca!"
ui.should_receive(:write).with(initial_message)
game_flow.start
end
end
describe "#next_step" do
context "when the game just started" do
it "asks the player for the length of the word to be raffled" do
question = "Qual o tamanho da palavra a ser sorteada?"
ui.should_receive(:write).with(question)
word_length = "3"
ui.should_receive(:read).and_return(word_length)
game_flow.next_step
157

## Página 172

8.3. Distribuindoresponsabilidadesparaoutrasclasses CasadoCódigo
end
end
context "when the player asks to raffle a word" do
it "raffles a word with the given length" do
word_length = "3"
ui.stub(read: word_length)
game.should_receive(:raffle).with(word_length.to_i)
game_flow.next_step
end
it "prints a '_' for each letter in the raffled word" do
word_length = "3"
ui.stub(read: word_length)
game.stub(raffle: "mom", raffled_word: "mom")
ui.should_receive(:write).with("_ _ _")
game_flow.next_step
end
it "tells if it's not possible to raffle with the given length" do
word_length = "20"
ui.stub(read: word_length)
game.stub(raffle: nil)
error_message = "Não temos uma palavra com o tamanho " <<
"desejado,\n" <<
"é necessário escolher outro tamanho."
ui.should_receive(:write).with(error_message)
game_flow.next_step
end
end
it "finishes the game when the player asks to" do
player_input = "fim"
ui.stub(read: player_input)
158

## Página 173

CasadoCódigo Capítulo8. Refatorandonossocódigo
game.should_receive(:finish)
game_flow.next_step
end
end
end
Antes de rodar esses novos testes, vamos verificar como ficaram os testes
da classe Game após termos movido a maior parte deles. Abra o arquivo
spec/game_spec.rb,eledeveestarassim:
1 # encoding: UTF-8
2
3 require 'spec_helper'
4 require 'game'
5
6 describe Game do
7 let(:ui) { double("ui").as_null_object }
8 let(:word_raffler) { double("raffler").as_null_object }
9
10 subject(:game) { Game.new(ui, word_raffler) }
11
12 describe "#ended?" do
13 it "returns false when the game just started" do
14 game.should_not be_ended
15 end
16 end
17 end
Comoeradeseesperar,todosostestessobreofluxodojogoforamextraídos,
ficandoapenasotestedométodo ended?,queésobreguardaroestadodojogo.
Apósterextraídoamaiorpartedostestes,seránecessáriofazeradaptaçõesnostestes
daclasse Gametambém.Porexemplo,nãoprecisaremosmaisdoobjeto uinesse
teste,jáquetodainteraçãocomousuárioseráresponsabilidadedo game_flow.
Entãodeletealinha7eadapteo subjectnalinha10pararetiraradependênciade
ui.Apósessasadaptações,otesteficaráassim:
# encoding: UTF-8
require 'spec_helper'
159

## Página 174

8.3. Distribuindoresponsabilidadesparaoutrasclasses CasadoCódigo
require 'game'
describe Game do
let(:word_raffler) { double("raffler").as_null_object }
subject(:game) { Game.new(word_raffler) }
describe "#ended?" do
it "returns false when the game just started" do
game.should_not be_ended
end
end
end
Vamoschecarsearefatoraçãodaclasse Gamenãoquebrounada.Aorodaros
testesdaclasse Game,vemosqueelesestãopassando:
$ bundle exec rspec spec/game_spec.rb
1 example, 0 failures
Nãopodemosesquecertambémqueaclasse Gameprecisafazermaisalgumas
coisasdasquaisa GameFlowdepende,quesãoosmétodos rafflee finish.
Adicioneosseguintestestesparaelesnoarquivo spec/game_spec.rb:
describe "#raffle" do
it "raffles a word with the given length" do
word_raffler.should_receive(:raffle).with(3)
game.raffle(3)
end
it "saves the raffled word" do
raffled_word = "mom"
word_raffler.stub(raffle: raffled_word)
game.raffle(3)
game.raffled_word.should == raffled_word
end
end
160

## Página 175

CasadoCódigo Capítulo8. Refatorandonossocódigo
describe "#finish" do
it "sets the game as ended" do
game.finish
game.should be_ended
end
end
Parafazeressestestespassarem,adicioneosseguintesmétodosnaclasse Game:
def raffle(word_length)
@raffled_word = @word_raffler.raffle(word_length)
end
def ended?
@ended
end
Emudeoconstrutordaclasse Gameparaficarassim:
def initialize(word_raffler = WordRaffler.new)
@word_raffler = word_raffler
@ended = false
end
Oquemudamosnoconstrutorfoitirarainje çãodedependência ui,jáque
Gamenãodependemaisde ui.
Aorodarostestesdaclasse Gamepodemosverificarqueelesestãopassando:
$ bundle exec rspec spec/game_spec.rb
4 examples, 0 failures
Comostestesdaclasse Gamenoverde,podemosiremfrente.
Apóstermosmovidoostestesde next_stepe startparaonovoarquivo
spec/game_flow_spec.rb,precisamosmovertambémalógicanecessáriaparaa
novaclasse.Vamoscriaroarquivo lib/game_flow.rbemoveralógicanecessária
daclasse Gameparaessanovaclasse.
Movaométodo startdaclasse Gameparaaclasse GameFlow,demodoa
ficarassim:
161

## Página 176

8.3. Distribuindoresponsabilidadesparaoutrasclasses CasadoCódigo
# encoding: UTF-8
require_relative 'cli_ui'
require_relative 'game'
# Esta classe é responsável pelo fluxo do jogo.
#
class GameFlow
def initialize(game = Game.new, ui = CliUi.new)
@game = game
@ui = ui
end
def start
initial_message = "Bem vindo ao jogo da forca!"
@ui.write(initial_message)
end
# (...)
end
Percebaquealémdemoverométodostart,tambémimplementamosoconstru-
tordaclasse GameFlow,explicitandoadependênciade gameede ui.
Agora mova o método next_step e o método privado
print_letters_feedbackparaanovaclasse,demodoaficarassim:
1 class GameFlow
2 # (...)
3
4 def next_step
5 @ui.write("Qual o tamanho da palavra a ser sorteada?")
6 player_input = @ui.read.strip
7
8 if player_input == "fim"
9 @ended = true
10 else
11 if @raffled_word = @word_raffler.raffle(player_input.to_i)
12 print_letters_feedback
13 else
14 error_message = "Não temos uma palavra com o tamanho " <<
15 "desejado,\n" <<
162

## Página 177

CasadoCódigo Capítulo8. Refatorandonossocódigo
16 "é necessário escolher outro tamanho."
17
18 @ui.write(error_message)
19 end
20 end
21 end
22
23 private
24 def print_letters_feedback
25 letters_feedback = ""
26
27 @raffled_word.length.times do
28 letters_feedback << "_ "
29 end
30
31 letters_feedback.strip!
32
33 @ui.write(letters_feedback)
34 end
35 end
Vamosprecisarfazeralgunsajustesapósmoveressesmétodos. Nalinha11
nãopodemosmaisusar @word_raffler,entãomudeessalinhaparaficarassim:
@game.raffle(player_input.to_i).
Nalinha27,nãotemosmaisacessoavariáveldeinstância @raffled_word,já
queissofazpartedoestadointernodoobjeto game. Entãomudeessalinhapara
ficarassim: @game.raffled_word
Apósessasmodificações,essesmétodosficarãoassim:
1 class GameFlow
2 # (...)
3
4 def next_step
5 @ui.write("Qual o tamanho da palavra a ser sorteada?")
6 player_input = @ui.read.strip
7
8 if player_input == "fim"
9 @ended = true
10 else
11 if @game.raffle(player_input.to_i)
12 print_letters_feedback
163

## Página 178

8.3. Distribuindoresponsabilidadesparaoutrasclasses CasadoCódigo
13 else
14 error_message = "Não temos uma palavra com o tamanho " <<
15 "desejado,\n" <<
16 "é necessário escolher outro tamanho."
17
18 @ui.write(error_message)
19 end
20 end
21 end
22
23 private
24 def print_letters_feedback
25 letters_feedback = ""
26
27 @game.raffled_word.length.times do
28 letters_feedback << "_ "
29 end
30
31 letters_feedback.strip!
32
33 @ui.write(letters_feedback)
34 end
35 end
Apóstodaessarefatoração,aorodarmosoRSpecinteiro,vemososeguinte:
$ bundle exec rspec
Failures:
1) GameFlow#next_step finishes the game when the player asks to
Failure/Error: game.should_receive(:finish)
(Double "game").finish(any args)
expected: 1 time
received: 0 times
# ./spec/game_flow_spec.rb:73
12 examples, 1 failure
Muito bom, só um teste está quebrando! Ele quebrou porque quando
game_flowrecebeuoinput“fim”dojogador,elenãoenviouamensagemfinish
164

## Página 179

CasadoCódigo Capítulo8. Refatorandonossocódigo
para o seu colaboradorgame. Para corrigir esse problema, edite o método
GameFlow#next_stepparaficarassim:
1 def next_step
2 @ui.write("Qual o tamanho da palavra a ser sorteada?")
3 player_input = @ui.read.strip
4
5 if player_input == "fim"
6 @game.finish
7 else
8 if @game.raffle(player_input.to_i)
9 print_letters_feedback
10 else
11 error_message = "Não temos uma palavra com o tamanho " <<
12 "desejado,\n" <<
13 "é necessário escolher outro tamanho."
14
15 @ui.write(error_message)
16 end
17 end
18 end
A única coisa que fizemos foi mudar a linha 6 para chamar o método
game.finish.
Depoisdetudoisso,finalmenteaorodarmosoRSpec,tudoestánoverde!
$ bundle exec rspec
12 examples, 0 failures
RSpecnoverde,vamosveroCucumber. AorodarmosoCucumber,vemoso
seguinte:
$ bundle exec cucumber
(...)
Exit status was 1 but expected it to be 0. Output:
forca/bin/forca:8:in `<main>':
undefined method `start' for #<Game>
(...)
3 scenarios (3 failed)
165

## Página 180

8.3. Distribuindoresponsabilidadesparaoutrasclasses CasadoCódigo
Todosostestesestãoquebrando.Oproblemaapontadopelamensagemdeerro
équenãoexisteométodo startnaclasse Game.Claro!Porqueextraímosessee
outrosmétodosparaaclasse GameFlow.Precisamosatualizarobináriodonosso
jogopararesolveresseproblema.
Editeoarquivo bin/forcaparaficarassim:
#!/usr/bin/env ruby
$:.unshift File.join(File.dirname(__FILE__), "..", "lib")
require 'game_flow'
game_flow = GameFlow.new
game_flow.start
while not game_flow.ended?
game_flow.next_step
end
AorodaroCucumberdenovo,vemososeguinte:
$ bundle exec cucumber
(...)
Exit status was 1 but expected it to be 0. Output:
Exit status was 1 but expected it to be 0. Output:
forca/bin/forca:10:in `<main>':
undefined method `ended?' for #<GameFlow> (NoMethodError)
(...)
3 scenarios (3 failed)
Infelizmente,todosostestesaindaestãoquebrando.Felizmente,amensagemde
erromudou,oquequerdizerqueestamosavan çando.Amensagemdeerroindica
queoproblemaéqueaclasse GameFlownãotemométodo ended?.Defato,ela
nãotem,porquequemguardaoestadodojogoéaclasse Game.Mas,podemosfazê-
ladelegaressemétodoparasuadependência game.Parafazerisso,editeocome ço
doarquivo lib/game_flow.rbparaficarassim:
166

## Página 181

CasadoCódigo Capítulo8. Refatorandonossocódigo
1 # (...)
2
3 require 'forwardable'
4
5 # Esta classe é responsável pelo fluxo do jogo.
6 #
7 class GameFlow
8 extend Forwardable
9 delegate :ended? => :@game
10
11 # (...)
12 end
Vocêpodevernalinha9queoquefizemosfoiapenasusarabibliotecapadrãodo
Ruby, Forwardable,paradelegarométodo ended?paraoobjetodependência
game.
AorodaroCucumberagora,elefinalmenteestánoverde! CucumbereRSpec
noverde,maisumpassodarefatoraç ãofinalizado,missãocumprida.
Nocomeçodocapítuloidentificamostrêspontosderefatoração:
1) extraçãodaresponsabilidadedesortearpalavra
2) extraçãodaresponsabilidadedefluxodojogo
3) reduçãodecondicionaisaninhadasnométodo next_step
Conseguimosrefatorarosdoisprimeirospontos.Oúltimoponto,vamosdeixar
nanossalistadébitostécnicoseatacá-lonospróximoscapítulos,duranteodesen-
volvimentodapróximafuncionalidade.Masantesdeirmosemfrentevamospensar
umpouconospontos-chavedestecapítulo.
8.4 P ontos-chave deste capítulo
Nestecapítulonósrefatoramosonossocódigo,melhorandoaarquiteturaeaqua-
lidade. Começamosidentificandoospontosdemelhoriaatravésdofeedbackdos
nossostestesedadetecçãodealguns code smellscomuns,taiscomométodospriva-
dosfazendocoisasdemaisemuitascondicionaisaninhadas.
Antesdarefatoração,nossoprojetotinhaapenasduasclasses: Gamee CliUi.
Aofinaldoprocessoderefatoração,ficamoscomquatroclassesnototal,adicionando
167

## Página 182

8.4. Pontos-chavedestecapítulo CasadoCódigo
duasnovasclasses: WordRafflere GameFlow.Fizemosissoparareduzironú-
meroderesponsabilidadesqueaclasse Gameestavaabrigando,aumentandoassim
asuacoesão.
Aprimeirarefatoraçãoquefizemosfoiextrairumaclassedeummétodoprivado,
nocaso,extraímosaclasse WordRaffler.Asegundarefatoraçãoquefizemosfoi
baseadanofeedbackdostestesdaclasse Game.Nósnotamosquehaviamuitostes-
tesparaummétodosó,ométodo next_step,oquejustificouextrairumaclasse
novaqueabrigariaaresponsabilidaderelacionadaaessemétodo,nocaso,aclasse
GameFlow.
Nósfizemostodooprocessoderefatoraçãocomsuportedanossasuítedetestes.
Acadapequenopasso,nósrodamosasuíteparasabersehavíamosquebradoalgoeo
queprecisariaseradaptado.Fazerrefatoraçãosemumasuitedetestesautomatizados
émuitoarriscado,vocêpodequebraralgumapartedosistemasemnemmesmo
perceber.
Portanto,umadasvantagensdoTDDéqueasuítedetestesqueconstruímos
duranteodesigndonossocódigoservetambémcomoumasuítedetestesderegres-
são. Eéessasuítequenosdáconfian çaeprodutividadenamelhoriacontínuada
qualidadedonossocódigo.
168

## Página 183

Capítulo9
Especificandoasegunda
funcionalidade
Nocapítuloanteriornósrefatoramosonossocódigoparamelhoraraqualidadedo
mesmo,facilitandoassimaadiçãodasfuncionalidadesqueestariamporvir.Neste
capítulocomeçaremosadesenvolverumadessasnovasfuncionalidades,afunciona-
lidadede "adivinhar letra”.
Para desenvolver essa funcionalidade, continuaremos seguindo o fluxo de
outside-in developmentcomTDD,come çandocomtestesdeaceitaçãocomCucum-
beredepoisindoparaostestesdeunidadecomRSpec.
Horadecolocaramãonamassa!(opa,nocódigo).
9.1 D ocumentando especificação e critério de
aceite com Cucumber
Naseção5.1nósdefinimosqueonossojogoteriatrêsfuncionalidades:

## Página 184

9.1. DocumentandoespecificaçãoecritériodeaceitecomCucumber CasadoCódigo
1) Jogador começa um novo jogo:jogomostraamensageminicialepedeprojo-
gadorsortearumapalavra;
2) Jogador adivinha uma letra da palavra:jogadortentaadivinharumaletraeo
jogomostraseeleacertououerrou;
3) Fim do jogo:ojogoterminaquandooujogadoracertatodasasletrasouerrao
bastanteparaocorpointeirodobonecoaparecernaforca.
Aprimeirafuncionalidadenósjádesenvolvemoserefatoramosnoscapítulos
anteriores.Vamosagoracome çaradesenvolverasegundafuncionalidade.Antesde
começaradesenvolveressafuncionalidade,precisamosprimeiropensarnaespecifi-
caçãodelaenosseuscritériosdeaceite.Comoaprendemosnoscapítulosanteriores,
vamosutilizaroCucumberparadocumentaraespecificaç ãoeoscritériosdeaceite
dessafuncionalidade.
Para come çar a fazer isso, crie o arquivo
features/adivinhar_letra.feature e comece a preenchê-lo com a es-
pecificaçãodessafuncionalidade,queseráassim:
# language: pt
Funcionalidade: Adivinhar letra
Após a palavra do jogo ser sorteada, o jogador pode começar a tentar
adivinhar as letras da palavra.
Cada vez que ele acerta uma letra, o jogo mostra para ele em que
posição dentro da palavra está a letra que ele acertou.
Cada vez que o jogador erra uma letra, uma parte do boneco da
forca aparece na forca. O jogador pode errar no máximo seis vezes, que
correspondem às seis partes do boneco: cabeça, corpo, braço esquerdo,
braço direito, perna esquerda, perna direita.
Atravésdaespecificaçãoacimajápodemosterumentendimentomelhorde
comoseráessafuncionalidade. Massóissonãoéobastanteparacome çarmosa
desenvolvê-la. Alémdessadescriçãomaisgenérica,énecessáriodefinirocritério
deaceitedessafuncionalidade. Paradefini-lo,podemosescreveralgunsexemplos
sobrecomodeveserocomportamentodessafuncionalidadeemcenáriosespecífi-
cos.Osexemplosqueiremosutilizarparanosguiarcomocritériodeaceiteserãoos
seguintes:
170

## Página 185

CasadoCódigo Capítulo9. Especificandoasegundafuncionalidade
Cenário: Sucesso ao adivinhar letra
Se o jogador adivinhar a letra com sucesso, o jogo mostra uma
mensagem de sucesso e mostra em que posição está a letra que o
jogador adivinhou.
Cenário: Erro ao adivinhar letra
Se o jogador errar ao tentar adivinhar a letra, o jogo mostra uma
mensagem de erro e mostra quais as partes o boneco da forca já
perdeu.
Cenário: Jogador advinha com sucesso duas vezes
Quanto mais o jogador for acertando, mais o jogo vai mostrando pra
ele as letras que ele adivinhou.
Cenário: Jogador erra três vezes ao adivinhar letra
Quanto mais o jogador for errando, mais partes do boneco da forca
são perdidas.
Oscenáriosacimajásãoobastanteparacobriroscritériosdeaceitedessafun-
cionalidade.Aodefinirosexemplosparaumafuncionalidade,vocêdeveternomí-
nimoocenáriodesucessoeocenáriodeerro.Foioquefizemosaoescreverosdois
primeiroscenáriosacima.
Alémdoscenáriosbásicosdesucessoeerro,definimostambémmaisdoiscená-
rios,paradeixarclarooqueacontecequandoojogadoracertaouerramaisdeuma
vezaotentaradivinharumaletradapalavrasorteada.
Agoraquejátemosaespecificaçãodafuncionalidade,assimcomoadefiniç ão
doscenáriosquecompõemoseucritériodeaceite,podemoscome çaraimplementar
otestedeaceitaçãodonossoprimeirocenário.
9.2 D efinindo o teste de aceitação do primeiro ce-
nário
Nonossoprimeirocenário, "Sucesso ao adivinhar letra”,iremossimularumjogador
iniciandoojogo,escolhendoqueapalavrasorteadadeverátertrêsletrasedepois
adivinhandoumaletradessapalavracomsucesso.Parafazerissoescrevaosseguin-
tesstepsdessecenárionoarquivo features/adivinhar_letra.feature:
@wip
Cenário: Sucesso ao adivinhar letra
171

## Página 186

9.2. Definindootestedeaceitaçãodoprimeirocenário CasadoCódigo
Se o jogador adivinhar a letra com sucesso, o jogo mostra uma
mensagem de sucesso e mostra em que posição está a letra que o
jogador adivinhou.
Dado que comecei um jogo
E que escolhi que a palavra a ser sorteada deverá ter "3" letras
Quando tento adivinhar que a palavra tem a letra "a"
E termino o jogo
Então o jogo mostra que eu adivinhei uma letra com sucesso
E o jogo termina com a seguinte mensagem na tela:
"""
a _ _
"""
AntesderodarmosoCucumber,vamosanalisarumpoucomaisessessteps.
Dentrodessessteps,temosaseguintesequência:
1) jogadorcomeçaumjogo;
2) eleescolhequeotamanhodapalavraasersorteadaseráde3letras;
3) eletentaadivinharqueapalavratemaletra“a";
4) eleacertaaletraeojogomostraqueeleacertou.
Aoleressesstepsepensaremcomovamosimplementá-los,podemosnosfazer
aseguintepergunta:“comoquesabemosquenesseteste,aojogadortentaradivinhar
queapalavratemaletra‘a’,elevaiacertar?”.Notesteestádefinidoqueeleiráacertar,
masoporquêeleacertaeoporquêdapalavracom3letrasteraletra“a”dentrodela
nãoestáexplícito!Deixarcoisasimplícitasemumtesteéumproblema.Issoéum
problemapordoismotivos:
1) Parapodermosimplementarumtestedemodoqueelesejadeterminístico,éne-
cessárioexplicitaroqueotesteprecisaparaelefuncionar(setupdoteste);
2) Quandoalguémforlerseuteste,deveserpossívelqueeleentendaarelaç ãode
causaeconsequênciadoseuteste. Ouseja,deveserpossívelqueeleentendao
seguintefluxodoseuteste:dadoqueosistemaestáemumdeterminadoestado,
quandorealizoumadeterminadaaç ãonessesistema,entãoobservoumadata
consequência.Quandonãoépossívelentenderessefluxodoseuteste,éprovável
queeleestejasofrendodo smell Obscure test(testeobscuro).Vocêpodelersobre
esseeoutros test smellsnolivro xUnit T est Patterns[10].
172

## Página 187

CasadoCódigo Capítulo9. Especificandoasegundafuncionalidade
Domodocomodefinimosnossoteste,eleestápecandonosdoispontosacima.
Paraqueojogadoradivinhecomsucessoaletra“a”dapalavrasorteada,devemos
garantirnosetupdonossotestequeapalavradetrêsletrasasersorteadateráaletra
“a”.
Ooutroproblemaéqueparaoleitordonossotestenãoestáclaroporqueo
jogadorconsegueadivinharcomsucessoaletra“a”,jáqueotestenãofalaqualéa
palavrasorteada.
Vamosresolveressesproblemasadicionandomaisumstepnonossotestepara
deixarexplícitoqueseumapalavradetrêsletraforsorteada,elateráaletra“a”.Va-
mosadicionaressestepusandoafuncionalidadede background(contexto)doCu-
cumber. Adicioneoseguintestepantesdocenário "Sucesso ao adivinhar letra”no
arquivo features/adivinhar_letra.feature:
Contexto:
* o jogo tem as possíveis palavras para sortear:
| número de letras | palavra sorteada |
| 3 | avo |
Após adicionar esse contexto na nossa funcionalidade, o seu arquivo
features/adivinhar_letra.featuredeveestarassim:
# language: pt
Funcionalidade: Adivinhar letra
Após a palavra do jogo ser sorteada, o jogador pode começar a tentar
adivinhar as letras da palavra.
Cada vez que ele acerta uma letra, o jogo mostra para ele em que
posição dentro da palavra está a letra que ele acertou.
Cada vez que o jogador erra uma letra, mais uma parte do boneco da
forca aparece na forca. O jogador pode errar no máximo seis vezes, que
correspondem às seis partes do boneco: cabeça, corpo, braço esquerdo,
braço direito, perna esquerda, perna direita.
Contexto:
* o jogo tem as possíveis palavras para sortear:
| número de letras | palavra sorteada |
| 3 | avo |
173

## Página 188

9.2. Definindootestedeaceitaçãodoprimeirocenário CasadoCódigo
@wip
Cenário: Sucesso ao adivinhar letra
Se o jogador adivinhar a letra com sucesso, o jogo mostra uma
mensagem de sucesso e mostra em que posição está a letra que o
jogador adivinhou.
Dado que comecei um jogo
E que escolhi que a palavra a ser sorteada deverá ter "3" letras
Quando tento adivinhar que a palavra tem a letra "a"
E termino o jogo
Então o jogo mostra que eu adivinhei uma letra com sucesso
E o jogo termina com a seguinte mensagem na tela:
"""
a _ _
"""
Reparequenocenário "Sucesso ao adivinhar letra”,quandoojogadorescolhe
queapalavrasorteadadeveráter3letras,eadivinhacomsucessoqueelatemaletra
“a”,oleitordotestejápoderáentenderarelaçãodecausaeconsequênciadesseteste.
Aoleroteste,elepodeverificarqueojogadorconseguiuadivinharcomsucessoa
letra“a”,porquenocontextodessetestedefinimosqueseapalavrasorteadativertrês
letras,entãoelaseráapalavra“avo”,quepossuialetra“a”.
Agoraquenossocenárioestáclaro,vamosrodaroCucumberedescobrirqualo
próximopasso:
$ bundle exec cucumber -t @wip
(...)
1 scenario (1 undefined)
7 steps (3 skipped, 4 undefined)
0m0.008s
You can implement step definitions for undefined steps with these
snippets:
Dado /^o jogo tem as possíveis palavras para sortear:$/ do |table|
# table is a Cucumber::Ast::Table
pending # express the regexp above with the code you wish you had
end
Dado /^que escolhi que a palavra a ser sorteada deverá ter "(.*?)"
174

## Página 189

CasadoCódigo Capítulo9. Especificandoasegundafuncionalidade
letras$/ do |arg1|
pending # express the regexp above with the code you wish you had
end
Quando /^tento adivinhar que a palavra tem a letra "(.*?)"$/ do |arg1|
pending # express the regexp above with the code you wish you had
end
Então /^o jogo mostra que eu adivinhei uma letra com sucesso$/ do
pending # express the regexp above with the code you wish you had
end
PelasaídadoCucumber,podemosverquedossetestepsusadosnessecenário,
temostrêsquejáestãodefinidoseoutrosquatroqueaindafaltadefinirmos,vamos
começardefinindoostep "o jogo tem as possíveis palavras para sortear”.
9.3 M elhore a testabilidade do seu softw are
Opróximostepqueiremosimplementaréo "o jogo tem as possíveis palavras para
sortear”. Essestepiráservirparadefiniralistadepalavraspossíveisqueonosso
jogopodesortear.Masatéentãoonossosoftwareaindanãotemessainterfacepara
definiralistadepalavrasorteáveis.Precisamosimplementarisso.
Adefiniçãopadrãodalistadepalavrassorteáveisestáemumarray hard-coded
naclasse WordRaffler:
class WordRaffler
def initialize(words = %w(hi mom game fruit))
@words = words
end
# (...)
end
Reparenocódigoacimaqueapesardocomportamentonormaldonossojogo
serutilizarsomenteaspalavras "hi, mom, game, fruit”comoopçõesparaosorteio,
adefiniçãodessalistapodeserinjetadano WordRaffler.Essalistade4palavraé
apenasumalistadefault,casoumaoutralistanãosejapassadacomoargumento.
Fizemosodesigndessaclasseusandoinje çãodedependênciaporqueostestes
delanos“obrigaram”.Ouseja,paraquefossepossíveltestá-la,eranecessáriopoder
175

## Página 190

9.3. Melhoreatestabilidadedoseusoftware CasadoCódigo
passarumalistadepalavrascomoargumento,comovocêpodevernostestesda
classe WordRaffler:
describe WordRaffler do
it "raffles a word from a given list of words" do
words = %w(me you nice)
raffler = WordRaffler.new(words)
raffler.raffle(3).should == "you"
raffler.raffle(2).should == "me"
raffler.raffle(4).should == "nice"
end
# (...)
end
Comovocêverámaisafrente,essedesignnospermitirádemodomaisfácilcriar
umainterfaceparasetaralistadepalavrassorteáveisdonossojogoduranteostestes
deCucumber.Precisaremosdissoparaimplementarostep "o jogo tem as possíveis
palavras para sortear”.
Ostestesdaclasse WordRafflerforamamotivaçãoparatermosfeitoalistade
palavrassorteáveiscomoumainjeçãodedependênciadaclasse WordRaffler.Essa
consequência“acidental”dosnossostestesparamelhoraratestabilidadedaclasse
WordRafflernoslevouaumdesignmelhor,equeiránospossibilitarconstruir
ummododesetarmosaspalavrassorteáveisdonossojogoduranteostestesdeCu-
cumber.
Comovocêjáouvirfalar,usarTestDrivenDevelopmentfazcomqueseusoft-
waretenhaumdesignmelhor.Oqueaconteceuacimaéumexemploclaroesimples
disso.
176

## Página 191

CasadoCódigo Capítulo9. Especificandoasegundafuncionalidade
Testabilidade
Testabilidadeéumrequisitonãofuncionalquemede“quãofácil”é
testarumsoftware.Umdosfatoresquecompõematestabilidadedeum
softwareéa controlabilidadedele,ouseja,emquenívelépossívelcon-
trolaroestadodosoftwareparaquesejamaisfáciltestá-lo.
Ostep "o jogo tem as possíveis palavras para sortear” foifeitopara
aumentaracontrolabilidadedonossojogo.
Noambientedeproduçãoojogadornãopoderádefinir,ousaber,
quaissãoaspalavrasdisponíveisparasorteiodentrodonossojogo.Mas,
noambientedetesteénecessárioquesejapossívelcontrolarquaispala-
vrasestãodisponíveis,paraquesejapossíveltestaroprogramademodo
determinístico.
Porfim,melhoraratestabilidadedonossojogonospossibilitaescre-
verumtestedeCucumbermelhor,noqualoleitordotestepossaenten-
derarelaçãodecausaeconsequênciaentreoestadoinicialdosistemae
alógicadeverificação(etapadesetupedeverificaç ão).
Voltandoaimplementaçãodosnossossteps,vamosrodaroCucumbermaisuma
vezparanoslembrarqualopróximopasso:
$ bundle exec cucumber -t @wip
(...)
1 scenario (1 undefined)
7 steps (3 skipped, 4 undefined)
0m0.008s
You can implement step definitions for undefined steps with these
snippets:
Dado /^o jogo tem as possíveis palavras para sortear:$/ do |table|
# table is a Cucumber::Ast::Table
pending # express the regexp above with the code you wish you had
end
(...)
177

## Página 192

9.3. Melhoreatestabilidadedoseusoftware CasadoCódigo
PelasaídadoCucumber,podemosnoslembrarqueopróximopassoédefiniro
step "o jogo tem as possíveis palavras para sortear”.Vamosfazerisso.
Construindo uma interface para definir as palavras sorteáveis
Ostep "o jogo tem as possíveis palavras para sortear” iráimplementaralógica
necessáriaparadefiniraspalavrassorteáveisduranteumdeterminadocenáriode
Cucumber.Antesdecome çarmosaimplementá-lo,vamospensarumpouconoque
elevaifazerecomo.
Nossojogoéexecutadopelostestespelamesmainterfacedousuário,vialinha
decomando. Logo,precisamosqueainterfacedelinhacomandodonossojogo
possibilitedefiniralistadepalavrassorteáveis.Ummododefazerissoseriapassando
paraobináriodonossojogoumargumentocomessalista. Esseargumentoseria
usadodoseguintemodo:
$ bin/forca "oi ola voce"
Naideiaacimaestamospassandoalistadepalavrassorteáveiscomoargumento
paraobináriodonossojogo.Vamosimplementaressaideia.
Paraimplementaressaideia,precisaremoseditarobinário bin/forcapara
lidarcomesseargumentoepassarparao WordRaffleressalistadepalavrascomo
alistadepalavrassorteáveisdojogo. Esseargumentosóseráusadonormalmente
noambientedeteste,logoobináriovaiterquelidarcomosdoiscasos,quandofor
passadooargumentoequandonãofor.
Atéentãoobináriodonossojogoestáassim:
#!/usr/bin/env ruby
$:.unshift File.join(File.dirname(__FILE__), "..", "lib")
require 'game_flow'
game_flow = GameFlow.new
game_flow.start
while not game_flow.ended?
game_flow.next_step
end
Precisamosmodificá-loparaqueelelidecomonovoargumentoqueestamos
adicionando. Paraquepossamossetaralistadepalavrassorteáveisdonossojogo,
178

## Página 193

CasadoCódigo Capítulo9. Especificandoasegundafuncionalidade
precisamospassaressalistaparaoconstrutordo WordRaffler.O WordRaffler
éumadependênciadaclasse Game,queumaédependênciadaclasse GameFlow.
Logo,teremosqueconstruirum WordRafflercomalistadepalavrasquevirá
comoargumentopelalinhadecomando,passaresseobjeto word_rafflercomo
argumentoparao Gameepassaresse Gamecomoargumentoparao GameFlow.
Editeoarquivo bin/forcaparaqueelefaçaissoefiqueassim:
# (...)
def create_game
word_raffler = create_word_raffler
Game.new(word_raffler)
end
def create_word_raffler
if ARGV.first
words = ARGV.pop
words = words.split
WordRaffler.new(words)
else
WordRaffler.new
end
end
game = create_game
game_flow = GameFlow.new(game)
game_flow.start
while not game_flow.ended?
game_flow.next_step
end
Repareomodocomoestamoscriandooobjeto WordRaffler.Estamosche-
candoseestávindoalgumargumentodalinhadecomando,eseestivervindo,esta-
mosusandoesseargumentocomolistadepalavrassorteáveisdojogo.
Comobináriomodificado,podemoscome çaraimplementarostep "o jogo tem
as possíveis palavras para sortear”paraqueelefaçausodessenovoargumento.Esse
stepdefinitionvaiterqueusaralistadepalavrassorteadasdestatabela:
Contexto:
179

## Página 194

9.3. Melhoreatestabilidadedoseusoftware CasadoCódigo
* o jogo tem as possíveis palavras para sortear:
| número de letras | palavra sorteada |
| 3 | avo |
E passar as palavras da segunda coluna para oWordRaffler. Va-
mos implementar esse step definition do seguinte modo no arquivo arquivo
features/step_definitions/game_steps.rb:
Dado /^o jogo tem as possíveis palavras para sortear:$/ do |words_table|
words = words_table.rows.map(&:last).join(" " )
set_rafflable_words(words)
end
Notequeométodo set_rafflable_wordsaindanãoexiste,estamosusando
umcódigoquegostaríamosqueexistisse. Fizemosdessejeitoparadeixarostep
definitionbemsimplesedelegaramaiorpartedalógicaparaessemétodo,quefará
partedosupportcode.
Aideiadométodo set_rafflable_wordséqueelesalvealistadepa-
lavras sorteáveis em uma variável de instância, para que ela seja usada pelo
step que inicia o jogo de fato. Vamos implementar esse método no arquivo
features/support/game_helpers.rb:
module NewGameHelpers
def set_rafflable_words(words)
@raffable_words = words
end
# (...)
end
Comessehelpermethoddefinido,precisamosatualizarosstepsqueiniciamum
novojogoparautilizaralistadepalavrassorteáveisdefinidaporessemétodo,caso
elaexista.
Podemosvernoarquivo features/step_definitions/game_steps.rb
queexistemosseguintesstepdefinitionssobrecome çarumnovojogo:
Dado /^que comecei um jogo$/ do
start_new_game
end
180

## Página 195

CasadoCódigo Capítulo9. Especificandoasegundafuncionalidade
Quando /^começo um novo jogo$/ do
start_new_game
end
Ambososstepdefinitionsestãodelegandotodalógicaparaosupportcode,logo
bastaquemodifiquemosométodo start_new_gameparautilizaralistadefinida
pelométodo set_rafflable_words.Reparecomofoiumaboadecisãodelegar
alógicadessesstepdefinitionsparaosupportcode,poisagorasóprecisamosmudar
emumúnicalugar,aoinvésdeterquemudartodososstepdefinitionsquetemaver
cominiciarumnovojogo.
Vamos modificar o método start_new_game no arquivo
features/support/game_helpers.rb para que ele utilize a lista de pala-
vrassorteáveis:
module NewGameHelpers
def set_rafflable_words(words)
@raffable_words = words
end
def start_new_game
set_rafflable_words(%w[hi mom game fruit]) if @raffable_words.nil?
steps %{
When I run `forca "#{@raffable_words}"` interactively
}
end
end
Oquemudamosnométodo start_new_gameforamduascoisas.Eledefinea
listadepalavrassorteáveisusandoométodo set_rafflable_words,eaoexecu-
tarnossojogopelalinhadecomandoviaAruba,estápassandoessalistadepalavras
comoargumento.
VamosrodaroCucumber,everificarseestátudook:
$ bundle exec cucumber -t @wip
(...)
1 scenario (1 undefined)
7 steps (2 skipped, 3 undefined, 2 passed)
0m0.019s
181

## Página 196

9.3. Melhoreatestabilidadedoseusoftware CasadoCódigo
You can implement step definitions for undefined steps with these
snippets:
Dado /^que escolhi que a palavra a ser sorteada deverá ter "(.*?)"\
letras\
$/ do |number_of_letters|
pending # express the regexp above with the code you wish you had
end
(...)
Ostep "o jogo tem as possíveis palavras para sortear”passou.Opróximostepa
serdefinidoéo ’E que escolhi que a palavra a ser sorteada deverá ter “3” letras’.
Aimplementaçãodessestepconsisteapenasemdigitarotamanhodapalavra
asersorteada. Comofizemosantes,vamosutilizaroArubaparasimularessain-
teraçãocomalinhadecomando. Adicioneoseguintestepdefinitionnoarquivo
features/step_definitions/game_steps.rb:
Dado /^que escolhi que a palavra a ser sorteada deverá ter "(.*?)"\
letras\
$/ do |number_of_letters|
steps %{
When I type "#{number_of_letters}"
}
end
Ao rodar o Cucumber novamente, vemos que esse step passou. O pró-
ximo step pendente é o"Quando tento adivinhar que a palavra tem a le-
tra “a"”. Assim como o step acima, esse step é apenas mais uma intera-
ção de escrita com a linha de comando, então podemos utilizar o Aruba para
implementá-lo.Adicioneaseguinteimplementaçãodessestepdefinitionnoarquivo
features/step_definitions/game_steps.rb:
Quando /^tento adivinhar que a palavra tem a letra "(.*?)"$/ do |letter|
steps %{
When I type "#{letter}"
}
end
AorodaroCucumbernovamente,vemosquesósobrouumsteppendente:
182

## Página 197

CasadoCódigo Capítulo9. Especificandoasegundafuncionalidade
$ bundle exec cucumber -t @wip
(...)
1 scenario (1 undefined)
7 steps (1 skipped, 1 undefined, 5 passed)
0m0.323s
You can implement step definitions for undefined steps with these
snippets:
Então /^o jogo mostra que eu adivinhei uma letra com sucesso$/ do
pending # express the regexp above with the code you wish you had
end
Osteppendenteéo "Então o jogo mostra que eu adivinhei uma letra com sucesso”.
Ojogoirámostrarprojogadorqueeleadivinhouumaletracomsucessoimprimindo
natelaamensagem "Você adivinhou uma letra com sucesso.".Entãoo
queadefiniçãodessestepdevefazeréapenasverificarseessamensagemfoiimpressa
natela.VamosfazerissousandooAruba,adicionandooseguintestepdefinitionno
arquivo features/step_definitions/game_steps.rb:
Então /^o jogo mostra que eu adivinhei uma letra com sucesso$/ do
steps %{
Then the stdout should contain:
"""
Você adivinhou uma letra com sucesso.
"""
}
end
AorodaroCucumber,nãotemosmaisstepspendenteseocenáriofinalmente
quebra:
$ bundle exec cucumber -t @wip
(...)
Diff:
- Você adivinhou uma letra com sucesso.
+ Bem vindo ao jogo da forca!
+ Qual o tamanho da palavra a ser sorteada?
(...)
183

## Página 198

9.4. Pontos-chavedestecapítulo CasadoCódigo
1 scenario (1 failed)
ComovocêpodeverpelamensagemdefalhadoCucumber,ocenáriofalhou
porqueojogonãoimprimiunatelaamensagem "Você adivinhou uma letra
com sucesso.".Eraoqueesperávamos.Agoraquefinalizamosaespecificaçãoeo
testedeaceitaçãodoprimeirocenáriodafuncionalidade“Adivinharletra”,podemos
continuarofluxodeoutside-indevelopmentepartirparaumtestedeRSpec.Mas,
vamosdeixarparafazerissosónocapítuloseguinte.
9.4 P ontos-chave deste capítulo
Nestecapítulonóscome çamosaespecificaçãodafuncionalidade“Adivinharletra”.O
desenvolvimentodessaespecificaçãofoiumpoucodiferentedoquetínhamosfeito
atéentão. Primeirocomeçamoscomumadescriçãodafuncionalidadeemtexto
abertoparadeixarclaroedocumentadooentendimentodoescopodessafuncio-
nalidade.
Apósisso,definimosquaisseriamoscenáriosdetestequeiriamcomporocrité-
riodeaceitedessafuncionalidade.Escrevemosnãosóotítulodoscenáriosdeteste
comotambémumadescriçãodecadaumdeles.Sódepoisdissotudoquecome ça-
mosaimplementardefatooprimeirocenáriodetestedeaceitaç ão.
Aideiadeterfeitoessefluxonaespecificaç ão(requisitosemtextoaberto,defini-
çãodoscenárioeporúltimoimplementaçãodoscenários)erademostrarquevalea
penapensarumpouconoescopodafuncionalidadeantesatédeimplementaropri-
meirotestedeaceitação.Dessemodo,orequisitodafuncionalidadeficamaisclaro
paravocêeparafuturosmembrosdoprojeto,quepoderãolerumadocumentaç ão
sucintadorequisitojuntamentecomosseustestesautomatizados.Juntandoassim
escopo,critériodeaceiteetestesautomatizados.
Duranteaimplementaçãodoprimeirocenário,tivemostambémumaboadis-
cussãosobretestabilidade,quandofoinecessáriocriarummododedefiniralistade
palavrassorteáveisdonossojogonocontextodeumtestedeaceitaç ão.Háquemfale
quevocênuncadevemudarseucódigosóporcausadeumteste.Mascadacasoéum
caso.Nonossoaomelhorarmosacontrolabilidadedonossosoftware,odeixamos
maismaleáveletambémmaisfácildetestar.Seguirofeedbackdostestescostuma
levaraumdesignmelhordoseusoftware,mascabeavocêdecidirseumamudan ça
nocódigodeproduçãodevidoaumtestevaidefatomelhorarseudesignouésó
parafazerotestepassar.
184

## Página 199

CasadoCódigo Capítulo9. Especificandoasegundafuncionalidade
Parafinalizar,valeapenaselembrarque T estabilidadeétambémumrequisitode
software,assimcomoumrequisitofuncional.Seseusoftwaretiverumatestabilidade
baixa,serádifícildetestá-lo.Sefordifícildetestá-lo,ficadifícildepraticarTDDe
aindapior,éprovávelqueomotivodeserdifícildetestarseusoftwareéporqueo
designestáruim.
185

## Página 201

Capítulo10
Finalizandoasegunda
funcionalidade
Nocapítuloanteriorfizemosaespecificaçãodafuncionalidade“Adivinharletra”eo
testedeaceitaçãodoseuprimeirocenário. Nestecapítulovamoscontinuartraba-
lhandonessafuncionalidade,finalizandoseustestesesuaimplementaç ão.
Aofinaldestecapítulo,ojogadordonossojogojávaipoderadivinharasletras
dapalavrasorteada.
Quemviver,verá!
10.1 R efatorando nosso jogo para ter uma máquina
de estados
Nacapítuloanterioranteriorfinalizamosoprimeirocenáriodafuncionalidade "Adi-
vinhar letra”,quefoiocenário "Sucesso ao adivinhar letra”.
Otestedeaceitaçãodessecenárioestavafalhandoporqueojogonãoimprimiua

## Página 202

10.1. Refatorandonossojogoparaterumamáquinadeestados CasadoCódigo
mensagem "Você adivinhou uma letra com sucesso.".Dadoqueoteste
deCucumberestáquebrando,opróximopassoéfazermosumtestedeunidadecom
RSpecparaespecificarocomportamentonecessário.
Ocomportamentoreferentea“jogoimprimeumamensagemdesucessoquando
ojogadoradivinhaumaletra”fazpartedofluxodojogo.Entãovamosescreveroteste
dessecomportamentocomopartedostestesdométodo GameFlow#next_step.
Oqueessetesteprecisafazeré:
1) dadoqueojogoestánoestadoquejátemumapalavrasorteada
2) quandoojogadoradivinharumaletracomsucesso
3) entãoojogoimprimeamensagem“Vocêadivinhouumaletracomsucesso.”
Paraimplementaressasaçõesnonossoteste,adicioneoseguintecódigonoar-
quivo spec/game_flow_spec.rb:
describe "#next_step" do
(...)
context "when the player guess a letter with success" do
it "prints a success message" do
game.stub(raffled_word: "hey")
success_message = "Você adivinhou uma letra com sucesso."
ui.should_receive(:write).with(success_message)
game.next_step
end
end
end
AorodaroRSpec,otestequebracomoesperado. Parafazeressetestepassar
seránecessáriomudarocomportamentodométodo Game#next_step. Vamos
analisarcomoessemétodoestáhojeepensarcomopodemosmodificá-lo:
def next_step
@ui.write("Qual o tamanho da palavra a ser sorteada?")
player_input = @ui.read.strip
if player_input == "fim"
188

## Página 203

CasadoCódigo Capítulo10. Finalizandoasegundafuncionalidade
@game.finish
else
if @game.raffle(player_input.to_i)
print_letters_feedback
else
error_message = "Não temos uma palavra com o tamanho " <<
"desejado,\n" <<
"é necessário escolher outro tamanho."
@ui.write(error_message)
end
end
end
Oqueessemétodoestáfazendoatéentãoélidarcomofluxodojogonoestado
ondeojogoaindanãotemumapalavrasorteada.Nesseestado,ofluxoconsisteem
perguntarprojogadorotamanhodapalavraasersorteadaesortearessapalavra.O
queprecisamosfazeréopassoseguintedojogo,noestadonoqualapalavrajáfoi
sorteadaeojogodevepedirprojogadoradivinharumaletra.
Paraimplementaressepróximopassodojogo,serianecessárioadicionarmais
umacondicionalnométodo next_step,checandoseexisteumapalavrasorteada
nojogoounão.Adicionarmaisumacondicionalnessemétodonãoéumaboaideia.
Antesmesmodepensaremadicionaressanovacondicional,nósjátínhamosidenti-
ficadoqueoaninhamentodecondicionaisatualnessemétodojáéumdébitotécnico.
Nãoqueremospiorarodébitotécnicoaumentandomaisaindaesseaninhamentode
condicionais.
Umaoutrasoluçãoparacontrolarofluxodojogoseriasalvaroestadodojogo
noobjeto gameeutilizaressainformaçãoparacontrolarofluxo.Seoobjeto game
estivernoestado :initial(estadoinicial),entãoopróximopassodofluxodojogo
deveserodesorteiodepalavra.Seoestadodo gamefor :word_raffled(palavra
sorteada),entãoopróximopassodofluxodojogoépedirprojogadoradivinharuma
letra.
Vamosimplementaressasolução,come çandopornovostestesdaclasse Game.
Comovamosmudaraclasse Game,masotestenovoqueadicionamosdaclasse
GameFlowainda está quebrado, vamos marcar esse teste como pendente, para
queasuítepossarodarnoverdeenquantomodificamosaclasse Game. Parafa-
zerisso,podemosusarométodo xitdoRSpec. Editeonovotestenoarquivo
spec/game_flow_spec.rbparaficarassim:
189

## Página 204

10.1. Refatorandonossojogoparaterumamáquinadeestados CasadoCódigo
context "when the player guess a letter with success" do
xit "prints a success message" do
# (...)
end
end
Apósessaedição,aorodarasuítedetestedoRSpec,vocêpodeverqueelainteira
passouequetemosumtestependente:
$ bundle exec rspec
(...)
14 examples, 0 failures, 1 pending
Com a suíte no verde, vamos fazer um teste para verificar que um jogo
novo começa no estado :initial. Adicione o seguinte teste no arquivo
spec/game_spec.rb:
context "when just created" do
its(:state) { should == :initial }
end
Parafazeressetestepassar,podemosinicializaroestadodeumobjeto game
como :initialnoseuconstrutoreadicionarum attr_writer: statena
classe:
class Game
attr_accessor :state
def initialize(word_raffler = WordRaffler.new)
@word_raffler = word_raffler
@ended = false
@state = :initial
end
end
AorodaroRSpec,vocêpodeverqueotestepassou.Vamosparaopróximoteste.
Opróximotesteserásobreatransiçãodeestadodoobjeto game.Quandouma
palavraforsorteadacomsucesso,o gamedeveirdoestado :initialparaestado
:word_raffled.Especifiqueessecomportamentoadicionandooseguintetesteno
arquivo spec/game_spec.rb:
190

## Página 205

CasadoCódigo Capítulo10. Finalizandoasegundafuncionalidade
describe "#raffle" do
# (...)
it "makes a transition from :initial to :word_raffled on success" do
word_raffler.stub(raffle: "word")
expect do
game.raffle(3)
end.to change { game.state }.from(:initial).to(:word_raffled)
end
end
Notecomonossospecficoubonitoaousarmosomatcher expect changedoRS-
pec!ApósapreciarmosumpoucoasintaxedoRSpec,vamosfazerotestepassar.
Parafazerotestepassar,bastaquemodifiquemosométodo Game#rafflepara
fazeratransiçãodoestadoquandoosorteiodapalavraforfeitocomsucessopelo
word_raffler.Seguindoessaideiamodifiqueométodo Game#raffleparaficar
assim:
def raffle(word_length)
if @raffled_word = @word_raffler.raffle(word_length)
@state = :word_raffled
end
end
AorodarmosoRSpec,podemosverqueotestpassou,vamosparaopróximo
teste.
Opróximotesteéparaocenárioquandoosorteiodapalavranãotemsucesso.
Nessecenárioo gamedevecontinuarnoestado :initial.Especifiqueessecom-
portamentoescrevendooseguintetestenoarquivo spec/game_spec.rb:
describe "#raffle" do
# (...)
it "stays on the :initial state when a word can 't be raffled" do
word_raffler.stub(raffle: nil)
game.raffle(3)
game.state.should == :initial
191

## Página 206

10.1. Refatorandonossojogoparaterumamáquinadeestados CasadoCódigo
end
end
AorodarmosoRSpec,vemosqueessetestejáestánoverde,devidoaomodo
comoimplementamosaclasse Game.
Antesdevoltarmosparaotestependentedaclasse GameFlow,vamosdaruma
olhadanocódigodaclasse Game.Devidoanovapropriedadedeestadoda Game,
existeummétodoquevaleapenasermodificado.Éométodo Game#finish:
def finish
@ended = true
end
Essemétodoérelacionadocomamanuten çãodoestadodo game.Comoagora
temosumavariáveldeinstânciaparacontrolaroestadodojogocomoumtodo,vale
apenaautilizarmosparacontrolarseo gameestánoestadofinalounão.Parafazer
isso,vamosmodificarométodo Game#finish,ométodo Game#ended?edeletar
ainicializaçãodavariáveldeinstância @endeddoconstrutordaclasse Game.
Ocódigodamodificaçãodessasparteséoseguinte:
class Game
# (...)
def initialize(word_raffler = WordRaffler.new)
@word_raffler = word_raffler
@state = :initial
end
# (...)
def ended?
@state == :ended
end
def finish
@state = :ended
end
end
AorodaroRSpec,podemosperceberqueostestescontinuamnoverdeecon-
cluímosquenossarefatoraçãonãoquebrounada. Finalmentepodemosvoltarpro
192

## Página 207

CasadoCódigo Capítulo10. Finalizandoasegundafuncionalidade
testequeoriginoutodasessasmodificaçõesnaclassegame,queéoseguintetestedo
GameFlow:
context "when the player guess a letter with success" do
xit "prints a success message" do
game.stub(raffled_word: "hey")
success_message = "Você adivinhou uma letra com sucesso."
ui.should_receive(:write).with(success_message)
game.next_step
end
end
10.2 R efatorando o fluxo do jogo para usar a má-
quina de estados
Antesdecontinuarmosatrabalharnoteste:
context "when the player guess a letter with success" do
xit "prints a success message" do
game.stub(raffled_word: "hey")
success_message = "Você adivinhou uma letra com sucesso."
ui.should_receive(:write).with(success_message)
game.next_step
end
end
Vamosverseonovomododecontrolaroestadodo gamenãoinfluencianesse
testedaclasse GameFlow,jáqueo gameéumadependênciadogame_flow.
Essetesteserveparatestarocenáriodeadivinhaç ãodeletracomsucesso.Esse
cenáriosódeveacontecerdepoisqueapalavradojogojáfoisorteada, ouseja,
quandooestadodo gamefor :word_raffled.Setaresseestadovaifazerparte
dosetupdesseteste.Podemosfazerissonosetupdessetestedoseguintemodo:
game.stub(state: :word_raffled)
Alémdesse stubserãonecessáriosmaisalgunspassosnosetupdesseteste.
193

## Página 208

10.2. Refatorandoofluxodojogoparausaramáquinadeestados CasadoCódigo
Comoocenáriodessetesteenvolveadivinharumaletracomsucesso,precisamos
decidirdeondeviráessainformação.O“chute”daletra,inputdojogador,virádo
ui.read.Podemosfazeressesetupnotestedoseguintemodo:
letter_guess = "e"
ui.stub(read: letter_guess)
Porfim,precisamosfazerosetupsobredeondevemainformaç ãoqueochute
daletrafoiumaadivinhaçãocomsucesso. Comoquemguardaapalavrasorteada
éo game,elepodeserresponsávelporsaberseumadadaletraexistenapalavra
sorteadaounão.Ouseja,eleseráoresponsávelpordizerseaadivinhaç ãodaletra
tevesucessoounão.
Vamosimaginarqueexistisseummétodochamado game.guess_letter,que
recebeumaletraecasoaadivinhaç ãotenhasucesso,eleretorna true,casocon-
trário,retorna false. Comoocenáriodotestequeestamosescrevendoésobre
adivinhaçãodeletracomsucesso,seessemétodoexistisse,ousaríamosparafazero
setupdonossotestedoseguintemodo:
game.stub(guess_letter: true)
Juntandotodosospassosdesetupacima,nossotesteficaráassim:
context "when the player guess a letter with success" do
it "prints a success message" do
game.stub(state: :word_raffled, guess_letter: true)
success_message = "Você adivinhou uma letra com sucesso."
ui.should_receive(:write).with(success_message)
game_flow.next_step
end
end
AorodarmosoRSpec,vemosqueessetestequebracomaseguintemensagem:
$ bundle exec rspec
(...)
Failures:
1) GameFlow#next_step when the player guess a letter with success
194

## Página 209

CasadoCódigo Capítulo10. Finalizandoasegundafuncionalidade
prints a success message
Failure/Error: ui.should_receive(:write).with(success_message)
Double "ui" received :write with unexpected arguments
expected: ("Você adivinhou uma letra com sucesso.")
got: ("Qual o tamanho da palavra a ser sorteada?"), ("")
Pelamensagemdeerropodemosverqueoproblemafoiqueamensagemde
adivinhaçãodeletracomsucessonãofoiimpressa.Vamosfazeressetestepassar.
Parafazerotestepassarprecisamosprimeiromodificaraclasse GameFlowpara
queelatomasuasaçõesbaseadononovoatributodeestadodoobjeto game.Hoje
ométodoquecuidadopróximopassodofluxodojogo, GameFlow#next_step
estáassim:
def next_step
@ui.write("Qual o tamanho da palavra a ser sorteada?")
player_input = @ui.read.strip
if player_input == "fim"
@game.finish
else
if @game.raffle(player_input.to_i)
print_letters_feedback
else
error_message = "Não temos uma palavra com o tamanho " <<
"desejado,\n" <<
"é necessário escolher outro tamanho."
@ui.write(error_message)
end
end
end
Opassoimplementadoacimaéoprimeiropassodojogoesódeveserrealizado
quandoojogoestivernoestadoinicial.Vamosextrairalógicaacimaparaummé-
todoprivadoesóchamá-loquando @game.stateforiguala :initial:
def next_step
case @game.state
when :initial
ask_to_raffle_a_word
195

## Página 210

10.2. Refatorandoofluxodojogoparausaramáquinadeestados CasadoCódigo
end
end
private
# (...)
def ask_to_raffle_a_word
@ui.write("Qual o tamanho da palavra a ser sorteada?")
player_input = @ui.read.strip
if player_input == "fim"
@game.finish
else
if @game.raffle(player_input.to_i)
print_letters_feedback
else
error_message = "Não temos uma palavra com o tamanho " <<
"desejado,\n" <<
"é necessário escolher outro tamanho."
@ui.write(error_message)
end
end
end
AorodarmosoRSpecdepoisdessamodificaç ão,podemosverquequasetodos
ostestesdaclasse GameFlowquebraram:
$ bundle exec rspec
(...)
16 examples, 6 failures
Failed examples:
rspec ./spec/game_flow_spec.rb:83
rspec ./spec/game_flow_spec.rb:23
rspec ./spec/game_flow_spec.rb:35
rspec ./spec/game_flow_spec.rb:44
rspec ./spec/game_flow_spec.rb:54
rspec ./spec/game_flow_spec.rb:70
196

## Página 211

CasadoCódigo Capítulo10. Finalizandoasegundafuncionalidade
Essamodificaçãoquebrouessestestesporquenessestestesnãoestásendofeito
nenhumsetupdoestadodadependência game. Paratodosostestesdaclasse
GameFlowquetínhamosfeitoatéentãoénecessárioqueo gameestejanoestado
:initial. Ouseja,todosessestestescompartilhamummesmosetup. Podemos
colocaressesetupno letquedefineocolaborador gamenocomeçodesseteste.
Hojeesse letestáassim:
let(:game) { double("game").as_null_object }
Vamosadicionaro stubdo statepararetornar :initial,demodoaficar
assim:
let(:game) { double("game", state: :initial).as_null_object }
AorodaroRSpecdepoisdessamodificação,podemosverificarquetodosostes-
tesquetinhamquebradovoltaramapassar. Ficamossomentecomumtesteque-
brado,queéotestequeestamostrabalhando:
context "when the player guess a letter with success" do
it "prints a success message" do
# (...)
end
end
Para fazermos esse teste passar, basta fazermos que o método Game-
Flow#next_steplidecomoestado:word_raffleddoobjeto game.
Primeirovamosadicionaresseestadonométodo Game#next_stepnoarquivo
lib/game_flow.rb:
def next_step
case @game.state
when :initial
ask_to_raffle_a_word
when :word_raffled
ask_to_guess_a_letter
end
end
Nocódigoacima,estamoschamandoométodo ask_to_guess_a_letter
paraexecutaropróximopassoquandoojogoestivernoestado :word_raffled.
Agorafaltaimplementarmosessemétodo.
197

## Página 212

10.3. Organizandoseustestesotimizandoparaleitura CasadoCódigo
Comoespecificamosnonossoteste,oqueessemétodoprecisafazeratéagoraé
executaraadivinhaçãodeletradojogadoreimprimirumamensagemdesucessose
essaadivinhaçãoforcorreta.Parafazerissoadicioneoseguintemétodoprivadona
classe GameFlow:
private
# (...)
def ask_to_guess_a_letter
letter = @ui.read.strip
if @game.guess_letter(letter)
@ui.write("Você adivinhou uma letra com sucesso.")
end
end
AorodaroRSpec,vocêpodeverquedepoisdessamodificaç ão,finalmenteos
testesvoltaramaficar100%noverde!Vamosaproveitarqueostestesestãonoverde
ereorganizarostestesdaclasse GameFlow.
10.3 O rganizando seus testes otimizando para lei-
tura
Ao ler o arquivospec/game_flow_spec.rb você pode ver que o método
next_steptemmuitostestes:
GameFlow
#next_step
finishes the game when the player asks to
when the player guess a letter with success
prints a success message
when the player asks to raffle a word
tells if it 's not possible to raffle with the given length
prints a '_' for each letter in the raffled word
raffles a word with the given length
when the game just started
asks the player for the length of the word to be raffled
Jáqueocomportamentodométodo next_stepéfazerumasériedeações
baseadonoestadodo game,vamosreorganizaressestestesparaficaremagrupados
segundooestadodo game. Seguindoessaideia,essestestesficariamorganizados
assim:
198

## Página 213

CasadoCódigo Capítulo10. Finalizandoasegundafuncionalidade
GameFlow
#next_step
when the game is in the 'initial' state
asks the player for the length of the word to be raffled
and the player asks to raffle a word
tells if it 's not possible to raffle with the given length
prints a '_' for each letter in the raffled word
raffles a word with the given length
when the game is in the 'word raffled' state
and the player guess a letter with success
prints a success message
finishes the game when the player asks to
Para fazer essa reorganização, vamos começar pelos testes do grupo
do estado inicial. Para fazer isso comece modificando no arquivo
spec/game_flow_spec.rb onde antes era "when the game just
started"para "when the game is in the 'initial'state":
describe "#next_step" do
context "when the game is in the 'initial' state" do
it "asks the player for the length of the word to be raffled" do
# (...)
end
end
Depoisdisso,coloqueotrechodecódigodo context "when the player
asks to raffle a word" dentro do context "when the game is in
the 'initial'state":
describe "#next_step" do
context "when the game is in the 'initial' state" do
it "asks the player for the length of the word to be raffled" do
# (...)
end
context "when the player asks to raffle a word" do
it "raffles a word with the given length" do
# (...)
end
it "prints a '_' for each letter in the raffled word" do
199

## Página 214

10.3. Organizandoseustestesotimizandoparaleitura CasadoCódigo
# (...)
end
it "tells if it's not possible to raffle with the given length" do
# (...)
end
end
end
Eparafinalizaressepartedoagrupamentodoestadoinicial,modifiqueotexto
deondeera context "when the player asks to raffle a word" para
context "and the player asks to raffle a word".
Agoravamosorganizarostestesdoagrupamentodoestado word raffled.
Crieumnovo contextparaesseagrupamentoecoloqueo context "when
the player guess a letter with success" dentrodessenovo context,
demodoaficarassim:
context "when the game is in the 'word raffled ' state" do
context "and the player guess a letter with success" do
it "prints a success message" do
game.stub(state: :word_raffled, guess_letter: true)
success_message = "Você adivinhou uma letra com sucesso."
ui.should_receive(:write).with(success_message)
game_flow.next_step
end
end
end
AorodaroRSpec,podemosverqueostestescontinuampassando.Fizemostoda
essareorganizaçãodos contextsparaquealeituradosnossostestesficassemais
fácileintuitiva.Parachecarseanovaestruturadonossotesteficouboa,podemos
rodaroRSpeccomo output formatter documentationeleroresultado. Façaisso
executandooseguintecomando:
$ bundle exec rspec --format documentation spec/game_flow_spec.rb
Vocêveráoseguinteoutput:
200

## Página 215

CasadoCódigo Capítulo10. Finalizandoasegundafuncionalidade
Figura10.1:RSpeccomoutputformatadoparadocumentaç ão
Pronto,comostestesorganizadosdemodoaserfácildelê-los,podemosirem
frente.Vamosfinalizarostestesdeunidadenecessáriosparaaadivinhaç ãodeletra
comsucesso.
10.4 I nterface discovery utilizando test doubles
Antesdecontinuarodesenvolvimentodonossojogo,vamosfalardeumatécnica
muitointeressantechamada Interface discovery.
Interface discoveryéumatécnicaqueconsisteemdescobrir(definir)aAPI(inter-
face)deumobjetocolaboradorduranteoprocessodeTDDutilizando Mock Objects.
Elafoidefinidainicialmentenopaper Endo-testing: unit testing with mock objects[8],
edepoismaisexploradanopaper Mock roles, not Objects[6]etambémnotradicional
livro Growing Object-Oriented Software, Guided by T ests[7].
Utilizamosumavariantedessatécnicanase ção 10.2,quandoduranteopro-
cessodeTDDdo GameFlow,definimosqueeleprecisariadependerdeummétodo
Game#guess_letterqueaindanãoexistia,parasaberseojogadortinhaadivi-
nhadoumaletracomsucesso.Nestase çãoutilizaremosdenovoessavariantedessa
técnica,maisdemodomaisexplícito,demodoquefiqueclarooseuuso.Paraco-
nheceraversãooriginaldessatécnica,recomendoquevocêleiaopaper Mock roles,
not Objects[6].
201

## Página 216

10.4. Interfacediscoveryutilizandotestdoubles CasadoCódigo
Voltandoaodesenvolvimentodonossojogo,vamosrelembrarafuncionalidade
queestamosdesenvolvendoolhandoocenáriodeCucumberqueestáquebrando:
Cenário: Sucesso ao adivinhar letra
Se o jogador adivinhar a letra com sucesso, o jogo mostra uma
mensagem de sucesso e mostra em que posição está a letra que o
jogador adivinhou.
Dado que comecei um jogo
E que escolhi que a palavra a ser sorteada deverá ter "3" letras
Quando tento adivinhar que a palavra tem a letra "a"
E termino o jogo
Então o jogo mostra que eu adivinhei uma letra com sucesso
E o jogo termina com a seguinte mensagem na tela:
"""
a _ _
"""
Paraessafuncionalidadefuncionar,oseguintefluxodeveserimplementado:
1) Ojogodeveestarnoestado :word_raffled
2) Ojogopedeparaojogadoradivinharumaletra
3) Jogadoradivinhaumaletracomsucesso
4) Jogomostramensagemdesucesso
5) Jogomostraletrasadivinhadas
Játrabalhamosnoprimeiro,terceiroequartopassosdofluxoacima,aindafaltam
osegundoequintopassos.Vamostrabalharnisso.
Vamosescreverumtestedeunidadeparaespecificarquequandoojogoestáno
estado :word_raffled,opróximopassodojogoéperguntarprojogadorqual
letraeleachaqueapalavratem. Faç aissoescrevendooseguintetestenoarquivo
spec/game_flow_spec.rb:
context "when the game is in the 'word raffled ' state" do
it "asks the player to guess a letter" do
game.stub(state: :word_raffled)
202

## Página 217

CasadoCódigo Capítulo10. Finalizandoasegundafuncionalidade
question = "Qual letra você acha que a palavra tem?"
ui.should_receive(:write).with(question)
game_flow.next_step
end
context "and the player guess a letter with success" do
# (...)
end
end
RodeostestesdeRSpeceverifiquequeessetestequebrou.
Parafazeressetestepassar,bastafazermoscomqueojogofaç aessapergunta
quandoeleestivertratandooestado :word_raffled.Hojejátemosummétodo
queestátratandoesseestado,ométodo Game#ask_to_guess_a_letter.Vamos
modificaressemétodoparaqueelefaçaaperguntaprojogador:
def ask_to_guess_a_letter
@ui.write("Qual letra você acha que a palavra tem?")
letter = @ui.read.strip
if @game.guess_letter(letter)
@ui.write("Você adivinhou uma letra com sucesso.")
end
end
AorodaroRSpecagora,podemosverqueotestepassou.Comostestesnoverde,
podemospararpararefatorá-losumpouco.
Aolerostestesdentrodocontext context "when the game is in the
'word raffled'state",podemosverquetodoselesestãosetandooestadodo
gamepara :word_rafflednafasedesetupdoteste.Parareduziressaduplicaç ão,
vamosextrairissoparaum before block.Aofazerissoseustestesficarãoassim:
context "when the game is in the 'word raffled ' state" do
before { game .stub(state: :word_raffled) }
it "asks the player to guess a letter" do
question = "Qual letra você acha que a palavra tem?"
ui.should_receive(:write).with(question)
game_flow.next_step
203

## Página 218

10.4. Interfacediscoveryutilizandotestdoubles CasadoCódigo
end
context "and the player guess a letter with success" do
it "prints a success message" do
game.stub(guess_letter: true)
success_message = "Você adivinhou uma letra com sucesso."
ui.should_receive(:write).with(success_message)
game_flow.next_step
end
end
end
Usando Interface discovery
AseguirvamosutilizaratécnicadeInterfacediscovery,masdiferentementede
comofizemosnase ção10.2,vamosdeixarexplícitoqueaestamosutilizando,para
vocêentendermelhorousodessatécnicanaprática.
Opróximocomportamentoaserespecificadoéodequandoojogadoradivinhar
umaletracomsucesso,ojogodevemostrarpraeleasletrasadivinhadas. Vamos
especificaressecomportamento.
Paraqueo GameFlowimprimaasletrasadivinhadas,essainformaç ãoprecisa
estarsalvaemalgumlugar,precisamosdefinirqualmétodoretornaráessainforma-
ção.Comooresponsávelportodooestadodojogoéoobjeto Game,entãovamos
imaginarqueéesseobjetoqueteráummétodoqueretornaráumarraydasletras
adivinhadas.Vamoschamaressemétodode Game#guessed_letters.
Énessemomentoqueestamosdescobrindoumapartenovadainterfacedoob-
jeto game.Oobjeto gameéumcolaboradordo game_flow,eduranteodesen-
volvimentodeumnovocomportamentodo game_flow,descobrimosqueelevai
dependerdeumnovométododo game,chamado guessed_letters. Apesar
determosdescobertoessanovadependênciaagora,nãoprecisamosimplementar
essemétodonestemomento,porqueparaostestesdaclasse GameFlowpodemos
representaressadependênciausandoo test double game.
Essaéatécnicade Interface discovery,descobrirumnovométodoquevaifazer
partedaAPIdeumobjetocolaboradorduranteoprocessodeTDDerepresentar
essadependêncianostestesutilizandoum test double.
Dada essa definição que vai existir um método chamado
204

## Página 219

CasadoCódigo Capítulo10. Finalizandoasegundafuncionalidade
Game#guessed_letters, podemos escrever nosso próximo teste stubando
essemétododoseguintemodo:
context "and the player guess a letter with success" do
# (...)
it "prints the guessed letters" do
game.stub(guess_letter: true, raffled_word: "hey",
guessed_letters: ["e"])
ui.should_receive(:write).with("_ e _")
game_flow.next_step
end
end
AorodaroRSpec,vemosaseguintesaída:
$ bundle exec rspec
1) GameFlow#next_step when the game is in the 'word raffled' state
and the player guess a letter with success
prints the guessed letters
Failure/Error: ui.should_receive(:write).with("_ e _")
Double "ui" received :write with unexpected arguments
expected: ("_ e _")
got: ("Qual letra você acha que a palavra tem?"),
("Você adivinhou uma letra com sucesso.")
Amensagemdizqueotestequebrouporqueo uinãorecebeuamensagem
writecomoargumento "_ e _",ouseja,quebrouporquenossojogonãoimpri-
miuasletrasadivinhadas.
Parafazerfazerotestepassar,bastafazercomquenossojogoimprimaasletras
adivinhadasquandoojogadoradivinharumaletracomsucesso. Vamosfazerisso
adicionando @ui.write(guessed_letters)nométodoquetrataadivinhação
deletra,o Game#ask_to_guess_a_letter:
def ask_to_guess_a_letter
@ui.write("Qual letra você acha que a palavra tem?")
letter = @ui.read.strip
205

## Página 220

10.4. Interfacediscoveryutilizandotestdoubles CasadoCódigo
if @game.guess_letter(letter)
@ui.write("Você adivinhou uma letra com sucesso.")
@ui.write(guessed_letters)
end
end
Agoraprecisamosimplementarométodo guessed_letters,queéoargu-
mentosendopassadopara @ui.write.Essemétodoiráretornarumastringrepre-
sentandoasletrasqueforamadivinhadasatéentão.Nocasodonossoteste,eledeve
retornar "_ e _".
Paraimplementaressemétodo,podemositerarsobrecadaletradapalavrasor-
teadaechecarseessaletraéumaletraquejáfoiadivinhada. Seelajáfoiadivi-
nhada,devemoscolocá-lanastringderetorno.Senãofoiadivinhada,devemosco-
locarum "_"nastring. Implementeessemétododoseguintemodonoarquivo
lib/game_flow.rb:
private
# (...)
def guessed_letters
letters = ""
@game.raffled_word.each_char do |letter|
if @game.guessed_letters.include?(letter)
letters << letter + " "
else
letters << "_ "
end
end
letters.strip!
end
AorodarmosoRSpecagora,podemosverqueotestepassou!Vamoschecarse
podemosrefatoraralgononossocódigoouteste.
Nostestessobrequandoojogadoradivinhaumaletracomsucesso,fazpartedo
setupfazerostub game.stub(guess_letter: true)parasetaraadivinhação
comsucesso.Essesetupestáduplicadoentreessestestes:
context "and the player guess a letter with success" do
it "prints a success message" do
206

## Página 221

CasadoCódigo Capítulo10. Finalizandoasegundafuncionalidade
game.stub(guess_letter: true)
# (...)
end
it "prints the guessed letters" do
game.stub(guess_letter: true, raffled_word: "hey",
guessed_letters: ["e"])
# (...)
end
end
Vamosextrairessesetupparaumbeforeblockdessecontext. Modifiqueesses
testesparaficaremassim:
context "and the player guess a letter with success" do
before { game. stub(guess_letter: true) }
it "prints a success message" do
# (...)
end
it "prints the guessed letters" do
game.stub(raffled_word: "hey", guessed_letters: ["e"])
# (...)
end
end
AorodarnovamenteoRSpec,vemosqueostestescontinuamnoverde,logo
nossarefatoraçãofoiokenãoquebrounada.Alémdessarefatoraç ãonoteste,pode-
mosrefatorartambémocódigodeprodução.
Se você checar os métodos GameFlow#print_letters_feedback
e GameFlow#guessed_letters, verá que o segundo é na verdade pra-
ticamente uma generalização do primeiro. Então onde antes usávamos
print_letters_feedback, podemos agora usar o guessed_letters,
reduzindo assim a duplicação de comportamento. O único lugar onde está
sendo usado oprint_letters_feedback é no seguinte trecho do método
ask_to_raffle_a_word:
def ask_to_raffle_a_word
# (...)
207

## Página 222

10.4. Interfacediscoveryutilizandotestdoubles CasadoCódigo
if player_input == "fim"
# (...)
else
if @game.raffle(player_input.to_i)
print_letters_feedback
else
# (...)
end
end
end
Parautilizaronovo guessed_letters,podemosmodificaressetrechopara
ficarassim:
def ask_to_raffle_a_word
# (...)
if player_input == "fim"
# (...)
else
if @game.raffle(player_input.to_i)
@ui.write(guessed_letters)
else
# (...)
end
end
end
Ao fazer isso, o teste ‘it "prints a '_'for each letter in the
raffled word"’quebra. Elequebraporqueagoraqueocomportamentoespe-
cificadonessetestetambémdependedométodo Game#guessed_letters,éne-
cessárioquefaçamosumstubdessemétodono letquedefineo double game.
Hojeesse letestáassim:
let(:game) { double("game", state: :initial).as_null_object }
Vamosmodificá-loparaficarassim:
let(:game) { double("game",
state: :initial,
guessed_letters: []).as_null_object }
208

## Página 223

CasadoCódigo Capítulo10. Finalizandoasegundafuncionalidade
AorodaroRSpec,vemosqueestátudonoverdenovamente,logonossarefa-
toraçãotevesucesso.Vamosvoltaraocenáriodeadivinhaç ãodeletracomsucesso
comoumtodo.
Ostestesquefizemosdo GameFlowparaespecificarocenáriodeadivinhação
deletracomsucessoforam:
context "when the game is in the 'word raffled ' state" do
it "asks the player to guess a letter" do
context "and the player guess a letter with success" do
it "prints a success message" do
it "prints the guessed letters"
end
end
Ouseja,jáfizemostodosostestesdeunidadenecessáriosdo GameFlowpara
cobrirocenáriodeadivinhaçãodeletracomsucesso.Noentanto,afuncionalidade
nãoestáprontaainda.Paraverificarmosisso,podemosrodaroCucumbereverque
eleaindatemtestesnovermelho:
$ bundle exec cucumber
(...)
game_flow.rb:69:in `ask_to_guess_a_letter':
undefined method `guess_letter' for #<Game:0x007fbdf1c96740>
(NoMethodError)
7 scenarios (2 failed, 5 passed)
ComovocêpodevernamensagemdeerrodoCucumber,otesteestáquebrando
porqueométodo Game#guess_letteraindanãofoiimplementado.Elenãofoi
implementandoaindaporqueadependênciadeleatéentãotinhasidostubadanos
testesdeunidadedo GameFlow,masagoraprecisamosfazerumaimplementaç ão
concretadessemétodo.
Implementando métodos descobertos via interface discovery
PercebemosquenossostestesdeCucumberestãoquebradosporquefaltaim-
plementarométodo Game#guess_letter.Essemétodofoidefinidoduranteos
209

## Página 224

10.4. Interfacediscoveryutilizandotestdoubles CasadoCódigo
testesdeunidadedo GameFlowutilizandoatécnicadeInterfacediscovery.Assim
comoessemétodo,definimosoutrométododomesmomodo,queaindaprecisa
serimplementado,o Game.guessed_letters.Vamoscome çarespecificandoo
Game#guess_letter.
Ométodo Game#guess_letterreceberácomoargumentoumaletra. Sea
palavrasorteadacontiveressaletra,essemétodoretorna, true,casocontrário,
eleretornafalse.Escrevaumtesteparaespecificaressecomportamentonoarquivo
spec/game_spec.rbdoseguintemodo:
describe "#guess_letter" do
it "returns true if the raffled word contains the given letter" do
game.raffled_word = "hey"
game.guess_letter("h").should be_true
end
end
Ao rodar esse teste, vemos que ele quebra porque o método
Game#guess_letter ainda não foi definido. Para fazer o teste passar, im-
plementeessemétododoseguintemodonoarquivo lib/game.rb:
def guess_letter(letter)
@raffled_word.include?(letter)
end
Rodandooteste,podemosverqueelepassa.Vamosparaopróximo.Agorapre-
cisamosescreverumtestequeverificaqueométodo guess_letterdeveretornar
false,casoapalavrasorteadanãocontenhaaletradadacomoargumento.Escreva
essetestedoseguintemodo:
describe "#guess_letter" do
it "returns true if the raffled word contains the given letter" do
# (...)
end
it "returns false if the raffled word doesn 't contain the given" <<
" letter" do
game.raffled_word = "hey"
game.guess_letter("z").should be_false
210

## Página 225

CasadoCódigo Capítulo10. Finalizandoasegundafuncionalidade
end
end
Aorodaresseteste,vemosqueelejáestánoverde.Issoéporqueaimplementa-
çãoquefizemosdessemétodojácobriaessecenáriodeinsucessotambém.
Porúltimo,vamosescreverumtestedesanidadeparaessemétodo,vamosespe-
cificaroqueaconteceseelerecebeumastringvaziaousócomespaçosembranco.
Nessecaso,ométododeveretornar falsetambém.Escrevaoseguintetestepara
especificaressecomportamento:
it "returns false if the given letter is an blank string" do
game.raffled_word = "hey"
game.guess_letter("").should be_false
game.guess_letter(" ").should be_false
end
Aorodarmosesseteste,vemosqueelequebra.Elequebrouporqueoqueaim-
plementaçãodonossométodofazé:
def guess_letter(letter)
@raffled_word.include?(letter)
end
Aconteceque @raffled_word.include?("")retorna true.Porissonosso
testequebrou.Vamosalterarnossométodopararetornar falsecasoastringdada
comoargumentosejavaziaousótenhaespaçosembranco.Modifiquenossométodo
paraficarassim:
def guess_letter(letter)
return false if letter.strip == ''
@raffled_word.include?(letter)
end
AorodaroRSpecagora, vemosqueostestespassam. Comonãohánada
pararefatoraratéagora, podemosirparaopróximoteste, queéodométodo
Game.guessed_letters.
Essemétododeveretornarumarraycomasletrasadivinhadasatéentão. En-
tão,seojogotemcomopalavrasorteadaapalavra“hey”,ealetra“e”jáfoiadi-
vinhadacomsucesso,logoométodo Game#guessed_lettersdeveretornaro
211

## Página 226

10.4. Interfacediscoveryutilizandotestdoubles CasadoCódigo
array ['e']. Escrevaumtesteparaespecificaressecomportamentonoarquivo
spec/game_spec.rb:
describe "#guessed_letters" do
it "returns the guessed letters" do
game.raffled_word = "hey"
game.guess("e")
game.guessed_letters.should = ["e"]
end
end
Aorodaresseteste,vemosqueelequebraporqueométodo guessed_letters
aindanãofoidefinido.Vamosdefini-lo.
Vamos imaginar que as letras adivinhadas fiquem salvas em uma variá-
vel de instância chamada@guessed_letters, então bastaria que o método
guessed_lettersfossedefinidocomoumum attr_readernaclasse Game.
Parafazerisso,adicioneesse attr_readernocomeçodoarquivolib/game.rb:
class Game
attr_accessor :raffled_word
attr_accessor :state
attr_reader :guessed_letters
# (...)
end
Precisamosagorainicializaressavariável.Quandoumnovojogoécriado,essa
variáveldevevircomumarrayvazio.Escrevaumtesteparaissodoseguintemodo:
describe "#guessed_letters" do
it "returns the guessed letters" do
# (...)
end
it "returns an empty array when there 's no guessed letters" do
game.guessed_letters.should = []
end
end
Parafazeressetestepassar,bastainicializarmosessavariávelcomumarrayvazio
noconstrutordaclasse Game:
212

## Página 227

CasadoCódigo Capítulo10. Finalizandoasegundafuncionalidade
def initialize(word_raffler = WordRaffler.new)
@word_raffler = word_raffler
@state = :initial
@guessed_letters = []
end
AorodarmosoRSpecagora,vemosqueumtestepassoumasumdessesnovos
testesquebrou,comaseguintemensagem:
$ bundle exec rspec
Failures:
1) Game#guessed_letters returns the guessed letters
Failure/Error: game.guessed_letters.should == ["e"]
expected: ["e"]
got: [] (using ==)
Paraqueométodo guessed_lettersretorneasletrasadivinhadas,éneces-
sárioquealguématualizeoarray @guessed_letters.Issopodeserfeitopelomé-
todo Game#guess_letter,quandoaadivinhaçãodaletrativersucesso. Vamos
especificaressenovocomportamentodométodo Game#guess_letter.Adicione
oseguintetestenoarquivo spec/game_spec.rb:
describe "#guess_letter" do
it "returns true if the raffled word contains the given letter" do
# (...)
end
it "saves the guessed letter when the guess is right" do
game.raffled_word = "hey"
expect do
game.guess_letter("h")
end.to change { game.guessed_letters }.from([]).to(["h"])
end
AorodaroRSpec,vemosqueessetestequebra.Parafazê-lopassar,bastaalterar-
mosométodo Game#guess_letterparasalvaraletraadivinhadacomsucesso:
def guess_letter(letter)
return false if letter.strip == ''
213

## Página 228

10.4. Interfacediscoveryutilizandotestdoubles CasadoCódigo
if @raffled_word.include?(letter)
@guessed_letters << letter
return true
else
return false
end
end
AorodarmosoRSpecagora,vemosquetodosostestesestãonoverde! Falta
fazermossomentemaisumtesteparaométodo Game#guess_letter,queéo
cenárioondeojogadoradivinhacomsucessoamesmaletramaisdeumavez.Nesse
cenário,avariável@guessed_lettersnãodevesalvaraletraadivinhadademodo
repetido,massimumaúnicavez. Especifiqueessecomportamentoescrevendoo
seguintetestenoarquivo spec/game_spec.rb:
describe "#guess_letter" do
# (...)
it "saves the guessed letter when the guess is right" do
# (...)
end
it "does not save a guessed letter more than once" do
game.raffled_word = "hey"
game.guess_letter("h")
expect do
game.guess_letter("h")
end.to_not change { game.guessed_letters } .from(["h"])
end
# (...)
AorodaroRSpec,vemosqueessetestequebracomaseguintemensagem:
$ bundle exec rspec
Failures:
1) Game#guess_letter does not save a guessed letter more than once
214

## Página 229

CasadoCódigo Capítulo10. Finalizandoasegundafuncionalidade
Failure/Error: expect do
result should not have changed, but
did change from ["h"] to ["h", "h"]
Oproblemaqueaconteceuéquealetraadivinhadacomsucessoestásendo
salva mais de uma vez no array@guessed_letters. Altere o método
Game#guessed_lettersparanãoduplicarumaletraadivinhadacomsucessofa-
zendoum uniq!na @guessed_letters:
def guess_letter(letter)
return false if letter.strip == ''
if @raffled_word.include?(letter)
@guessed_letters << letter
@guessed_letters.uniq!
return true
else
return false
end
end
AgoraaorodaroRSpec,podemosverqueestátudonoverde! Vamosrodaro
Cucumber.
AorodaroCucumber,vocêpodeverqueaindatemtestequebrado. Essepro-
blemaestáacontecendoporquequandoojogoestánoestado :word_raffled,ele
nãoestálidandocomoinput "fim",queéquandoojogadorquerfinalizarojogo
nomeio,comportamentoqueestamosutilizandonostestesdoCucumber.
Hojejátemosumtesteno spec/game_flow_spec.rbparalidarcomocaso
dojogadorquererfinalizarojogonomeio:
describe "#next_step" do
# (...)
it "finishes the game when the player asks to" do
player_input = "fim"
ui.stub(read: player_input)
game.should_receive(:finish)
game_flow.next_step
215

## Página 230

10.4. Interfacediscoveryutilizandotestdoubles CasadoCódigo
end
end
Noentantoessetestesóestásendoaplicadoparaquandoo gameestánoestado
:initial.Precisamosfazercomqueessetesteverifiqueessecomportamentoen-
quantoogameestivertambémnoestado :word_raffled.Parafazerisso,modi-
fiqueessetesteparaficarassim:
it "finishes the game when the player asks to" do
player_input = "fim"
ui.stub(read: player_input)
game.stub(state: :initial)
game.should_receive(:finish)
game_flow.next_step
game.stub(state: :word_raffled)
game.should_receive(:finish)
game_flow.next_step
end
AorodaroRSpec,podemosverqueessetestequebracomaseguintemensagem:
$ bundle exec rspec
Failures:
1) GameFlow#next_step finishes the game when the player asks to
Failure/Error: game.should_receive(:finish)
(Double "game").finish(any args)
expected: 1 time
received: 0 times
O erro ocorreu porque se o jogador digitar"fim”, e o estado dogamefor
:word_raffled,amensagem finishnãoestásendoenviadapara gamequando
ométodo GameFlow#next_stepéexecutado.
Antesdefazeressetestepassar,vamosprimeirochecarcomoqueoinput "fim"
estásendotratadonocasodo gameestarnoestado :initial. Essetratamento
estásendofeitonométodo GameFlow#ask_to_raffle_a_word:
def ask_to_raffle_a_word
@ui.write("Qual o tamanho da palavra a ser sorteada?")
216

## Página 231

CasadoCódigo Capítulo10. Finalizandoasegundafuncionalidade
player_input = @ui.read.strip
if player_input == "fim"
@game.finish
else
# (...)
end
end
Paratrataroinput "fim"nométodoGameFlow#ask_to_guess_a_letter,
queéométodousadoquandoo gameestánoestado :word_raffled,seriane-
cessárioduplicarestapartedométodo ask_to_raffle_a_word:
player_input = @ui.read.strip
if player_input == "fim"
@game.finish
# (...)
Aoinvésdefazerisso,vamosfazerumarefatoraç ãoparaevitaressaduplica-
ção. Vamosextrairessecomportamentodefazerumaperguntaprojogadoretra-
taroinput "fim"paraumoutrométodoprivado,quepoderáserreutilizadopor
ask_to_raffle_a_worde ask_to_guess_a_letter.Comovamosfazeruma
refatoraçãoetemosumtestequebrado,marqueessetestequebradocomopendente,
utilizandoo xitdoRSpec,aoinvésdo it:
xit "finishes the game when the player asks to" do
# (...)
end
Agoravamosextrairdométodo ask_to_raffle_a_wordalógicadefa-
zerumaperguntaprojogadoretrataroinput fimparaummétodochamado
ask_the_player:
def ask_to_raffle_a_word
ask_the_player("Qual o tamanho da palavra a ser sorteada?") do |length|
if @game.raffle(length.to_i)
print_letters_feedback
else
error_message = "Não temos uma palavra com o tamanho " <<
"desejado,\n" <<
217

## Página 232

10.4. Interfacediscoveryutilizandotestdoubles CasadoCódigo
"é necessário escolher outro tamanho."
@ui.write(error_message)
end
end
end
Oqueométodo ask_the_playeriráfazeréimprimirumaperguntaprojo-
gadoretrataroinputderesposta. Quandooinputfordiferentede "fim",então
essemétododaum yielddoinputdojogador.Casocontrário,elefinalizaojogo.
Implementeessemétododoseguintemodonoarquivo lib/game_flow.rb
private
# (...)
def ask_the_player(question)
@ui.write(question)
player_input = @ui.read.strip
if player_input == "fim"
@game.finish
else
yield player_input.strip
end
end
AorodaroRSpec,vemosquenãoquebramosnenhumtestequejáestavapas-
sando,logonossorefatoraçãotevesucesso.Vamosagorareativarotestequetínha-
mosmarcadocomopendente:
it "finishes the game when the player asks to" do
player_input = "fim"
ui.stub(read: player_input)
game.stub(state: :initial)
game.should_receive(:finish)
game_flow.next_step
game.stub(state: :word_raffled)
game.should_receive(:finish)
game_flow.next_step
end
218

## Página 233

CasadoCódigo Capítulo10. Finalizandoasegundafuncionalidade
Ao rodar o RSpec, vemos que esse teste continua quebrando. Para fazer
ele passar, basta que usemos o novo métodoask_the_player no método
ask_to_guess_a_letterparaqueelelidecominput "fim"também. Modi-
fiqueométodo ask_to_guess_a_letterparaficarassim:
def ask_to_guess_a_letter
ask_the_player("Qual letra você acha que a palavra tem?") do |letter|
if @game.guess_letter(letter)
@ui.write("Você adivinhou uma letra com sucesso.")
@ui.write(guessed_letters)
end
end
end
AorodaroRSpecnovamente,vemosqueeleestánoverde.Eomelhor,aoro-
darmosoCucumberagora,vemosqueeletambémestánoverde!
$ bundle exec cucumber
(...)
7 scenarios (7 passed)
21 steps (21 passed)
FinalmenteocenáriodoCucumber‘Sucesso ao adivinhar letra’está
noverde!Comoelejáestánoverde,retireatag @wipdele.
Agoraestamosprontosparairparaospróximoscenáriosdafuncionalidade
“Adivinharletra”efinalmentefinalizá-la.
10.5 Finalizando a funcionalidade Adivinhar letra
Paraafuncionalidade ’ Adivinhar letra’letradefinimososseguintescenárioscomCu-
cumber:
• Sucessoaoadivinharletra;
• Erroaoadivinharletra;
• Jogadoradvinhacomsucessoduasvezes;
• Jogadorerratrêsvezesaoadivinharletra.
219

## Página 234

10.5. FinalizandoafuncionalidadeAdivinharletra CasadoCódigo
Oprimeirocenárionósjáimplementamos,estánoverde.Vamosparaosegundo,
o ’Erro ao adivinhar letra’.
Paraessecenáriodeerro,tínhamosdefinidoaseguinteespecificaç ão:
Cenário: Erro ao adivinhar letra
Se o jogador errar ao tentar adivinhar a letra, o jogo mostra uma
mensagem de erro e mostra quais as partes o boneco da forca já
perdeu.
Oqueprecisamosfazeragoraéescreverotestedeaceitaç ãoparaessecenário.A
estruturadotestedessecenárioémuitosemelhantecomadocenáriodeadivinhação
deletracomsucesso.Asúnicasdiferen çassãoqueojogadortemquetentaradivinhar
umaletraquenãotemnapalavra,ojogodevemostrarqueeleerrouedevemostrar
quaissãoaspartesqueobonecodaforcajáperdeu.Seguindoessaideia,escrevaesse
testedoseguintemodo:
@wip
Cenário: Erro ao adivinhar letra
Se o jogador errar ao tentar adivinhar a letra, o jogo mostra uma
mensagem de erro e mostra quais as partes o boneco da forca já
perdeu.
Dado que comecei um jogo
E que escolhi que a palavra a ser sorteada deverá ter "3" letras
Quando tento adivinhar que a palavra tem a letra "z"
E termino o jogo
Então o jogo mostra que eu errei a adivinhação da letra
E o jogo termina com a seguinte mensagem na tela:
"""
O boneco da forca perdeu as seguintes partes do corpo: cabeça
"""
AorodaroCucumbernósvemososeguinte:
$ bundle exec cucumber -t @wip
(...)
1 scenario (1 undefined)
7 steps (1 skipped, 1 undefined, 5 passed)
0m0.324s
220

## Página 235

CasadoCódigo Capítulo10. Finalizandoasegundafuncionalidade
You can implement step definitions for undefined steps with these
snippets:
Então /^o jogo mostra que eu errei a adivinhação da letra$/ do
pending # express the regexp above with the code you wish you had
end
Como você pode ver pela saída do Cucumber, o step “Então o jogo
mostra que eu errei a adivinhação da letra” está indefinido.
O que esse step precisa fazer é apenas checar se a mensagem"Você
errou a letra." foi impressa na tela. Defina esse step no arquivo
features/step_definitions/game_steps.rbdoseguintemodo:
Então /^o jogo mostra que eu errei a adivinhação da letra$/ do
steps %{
Then the stdout should contain:
"""
Você errou a letra.
"""
}
end
AorodaroCucumberagora,vemosqueelefalhacomaseguintemensagem:
$ bundle exec cucumber -t @wip
(...)
Diff:
@@ -1,2 +1,6 @@
-Você errou a letra.
+Bem vindo ao jogo da forca!
+Qual o tamanho da palavra a ser sorteada?
+_ _ _
+Qual letra você acha que a palavra tem?
+Qual letra você acha que a palavra tem?
1 scenario (1 failed)
7 steps (1 failed, 1 skipped, 5 passed)
Elefalhouporqueamensagem "Você errou a letra."nãofoiimpressa
natela. Precisamosfazercomquenossojogolidecomocenáriodeadivinhaç ão
comerro.Paraisso,vamosescreverumtestedeunidadeparao GameFlow.
221

## Página 236

10.5. FinalizandoafuncionalidadeAdivinharletra CasadoCódigo
Precisamos fazer um teste que verifique que dado que o jogo está no es-
tado :word_raffled, quandoojogadorerraaoadivinharumaletra, entãoa
mensagemdeerroéimpressa. Escrevaessetestedoseguintemodonoarquivo
spec/game_flow_spec.rb:
describe "#next_step" do
# (...)
context "when the game is in the 'word raffled' state" do
before { game.stub(state: :word_raffled) }
# (...)
context "and the player fails to guess a letter" do
before { game.stub(guess_letter: false) }
it "prints a error message" do
error_message = "Você errou a letra."
ui.should_receive(:write).with(error_message)
game_flow.next_step
end
end
end
end
RodeoRSpeceverifiquequeotestequebrou.Parafazeressetestepassar,basta
quealteremosométodo GameFlow#ask_to_guess_a_letterparalidarcomo
casoquandoométodo Game#guess_letterretorna false.Altereessemétodo
paralidarcomessecasodemodoqueelefiqueassim:
def ask_to_guess_a_letter
ask_the_player("Qual letra você acha que a palavra tem?") do |letter|
if @game.guess_letter(letter)
@ui.write("Você adivinhou uma letra com sucesso.")
@ui.write(guessed_letters)
else
@ui.write("Você errou a letra.")
end
end
end
AorodaroRSpecagora,podemosverqueeleestánoverde. Vamosrodaro
Cucumber:
222

## Página 237

CasadoCódigo Capítulo10. Finalizandoasegundafuncionalidade
$ bundle exec cucumber -t @wip
(...)
E o jogo termina com a seguinte mensagem na tela:
"""
O boneco da forca perdeu as seguintes partes do corpo: cabeça
"""
Diff:
@@ -1,2 +1,7 @@
-O boneco da forca perdeu as seguintes partes do corpo: cabeça
+Bem vindo ao jogo da forca!
+Qual o tamanho da palavra a ser sorteada?
+_ _ _
+Qual letra você acha que a palavra tem?
+Você errou a letra.
+Qual letra você acha que a palavra tem?
1 scenario (1 failed)
7 steps (1 failed, 6 passed)
Ostepqueantesestavaquebrandoagoraestápassando,masostepseguinteque-
brou. Ostepquequebroufoioqueverificaseojogoimprimiunatelaasparte
queobonecodaforcaperdeu.Paraimplementaressecomportamento,vamosantes
especificá-locomtestesdeunidadedaclasse GameFlow.
Essetestedeveverificarquequandoojogadorfazumaadivinhaç ãodeletrain-
correta,ojogoimprimealistasdaspartesqueobonecodaforcajáperdeu.Vamos
começarimplementandoessetestedoseguintemodo:
context "and the player fails to guess a letter" do
before { game. stub(guess_letter: false) }
# (...)
it "prints the list of the missed parts" do
missed_parts_message = "O boneco da forca perdeu as " <<
"seguintes partes do corpo: cabeça"
ui.should_receive(:write).with(missed_parts_message)
game_flow.next_step
end
end
223

## Página 238

10.5. FinalizandoafuncionalidadeAdivinharletra CasadoCódigo
Aestruturadotesteestácompleta,porém,nemtodasasinformaçõesnecessárias
paraosetupdotesteestãodefinidas.Deondevemainformaç ãodequeaparteque
obonecoperdeuatéentãofoiacabe ça?
Podemosimaginarqueoobjeto gamepoderáguardaressasinformaçãocomo
partedoestadodojogo.Dessemodo,oobjeto gamepoderiaterummétodocha-
mado Game#missed_partsqueretornariaumarraycomaspartesqueoboneco
jáperdeu.Supondoqueessemétodoexistirá,podemosstubaressenovométodono
nossoteste:
it "prints the list of the missed parts" do
game.stub(missed_parts: ["cabeça"])
missed_parts_message = "O boneco da forca perdeu as " <<
"seguintes partes do corpo: cabeça"
ui.should_receive(:write).with(missed_parts_message)
game_flow.next_step
end
Agora nosso teste deve estar completo. Rode o RSpec e verifique
que esse teste quebrou. Para fazê-lo passar, basta modificarmos o mé-
todo GameFlow#ask_to_guess_a_letter para utilizar o método
Game#missed_parts:
def ask_to_guess_a_letter
ask_the_player("Qual letra você acha que a palavra tem?") do |letter|
if @game.guess_letter(letter)
# (...)
else
@ui.write("Você errou a letra.")
missed_parts_message = "O boneco da forca perdeu as " <<
"seguintes partes do corpo: "
missed_parts_message << @game.missed_parts.join(", ")
@ui.write(missed_parts_message)
end
end
end
AgoraaorodaroRSpec,podemosverqueestátudonoverde.Noentantoantes
derodaroCucumber,precisamosimplementaressenovométodoquedescobrimos
224

## Página 239

CasadoCódigo Capítulo10. Finalizandoasegundafuncionalidade
quetemquefazerpartedaAPIdoobjeto Game,ométodo Game#missed_parts.
Paracomeçarmosaespecificaressemétodo,adicioneaseguinteestruturadetes-
tesnoarquivo spec/game_spec.rb:
describe "#missed_parts" do
it "returns an empty array when there 's no missed parts"
it "returns the missed parts for each fail in guessing a letter"
end
Oprimeirotesteéparatestarocomportamentodessemétodoquandoojogo
acaboudecome çar.Osegundotesteéparatestarocomportamentodessemétodo
quandojáaconteceramalgunsinsucessosnaadivinhaç ãodeletra. Vamosescre-
vendooprimeiroteste:
it "returns an empty array when there 's no missed parts" do
game.missed_parts.should == []
end
Aorodarmosesseteste,vemosqueelefalhaporqueométodo missed_parts
aindanãofoidefinido.Vamosdefini-locolocandoum attr_readerparaoatri-
buto missed_partseinicializandoesseatributonoconstrutordaclasse Game:
class Game
# (...)
attr_reader :missed_parts
def initialize(word_raffler = WordRaffler.new)
@word_raffler = word_raffler
@state = :initial
@guessed_letters = []
@missed_parts = []
end
AorodaroRSpec,vemosqueelepassou.Vamosparaopróximoteste.
Opróximotesteéparaexercitarquesealgumastentativasdeadivinhaç ãode
letrajáforamfeitassemsucesso,entãoométodo missed_partsdeveretornaruma
partedobonecoparacadatentativaerrada.Escrevaessetestedoseguintemodo:
it "returns the missed parts for each fail in guessing a letter" do
game.raffled_word = "hey"
225

## Página 240

10.5. FinalizandoafuncionalidadeAdivinharletra CasadoCódigo
3.times do
game.guess_letter("z")
end
game.missed_parts.should == ["cabeça", "corpo", "braço esquerdo"]
end
Ao rodarmos o RSpec podemos ver que esse teste falha. Ele falha porque
o métodogame.guess_letter não está atualizando a variável de instância
@missed_partsquandoaadivinhaçãodeletrafoierrada.Vamosescreverumteste
paraespecificaressecomportamentotambém:
describe "#guess_letter" do
# (...)
it "updates the missed parts when the guess is wrong" do
game.raffled_word = "hey"
game.guess_letter("z")
game.missed_parts.should == ["cabeça"]
end
end
AorodaroRSpec,vemosqueelecontinuanovermelho. Parafazerosdois
testes que estão no vermelho passarem, precisamos fazer com que o método
Game#guess_letteratualizeavariáveldeinstância @missed_partsdeacordo
comonúmerodeerrosdeadivinhaçãodeletra.Parafazeressetestepassar,vamos
começarprimeirosalvandoquaissãoaspossíveispartesqueobonecopodeperder
emumaconstantedentrodaclasse Game:
class Game
HANGMAN_PARTS = [
"cabeça", "corpo", "braço esquerdo",
"braço direito", "perna esquerda", "perna direita"
]
# (...)
end
Agora que temos essa constante, para cada erro que é feito ao adivinhar
umaletra,ométodo guess_letterprecisacolocarumelementodaconstante
226

## Página 241

CasadoCódigo Capítulo10. Finalizandoasegundafuncionalidade
HANGMAN_PARTSnavariáveldeinstância @missed_parts. Parafazerisso,será
necessáriosaberonúmerodeerrosdeadivinhaçãodeletra.Vamoscriarumavariá-
veldeinstânciaparasalvaressainformaç ãoeinicializá-lacom zeronoconstrutor
daclasse Game:
class Game
def initialize(word_raffler = WordRaffler.new)
@word_raffler = word_raffler
@state = :initial
@guessed_letters = []
@missed_parts = []
@wrong_guesses = 0
end
end
Agorapodemosutilizaressavariávelparaatualizara @missed_partsquando
forfeitoumaadivinhaçãoerrada:
def guess_letter(letter)
return false if letter.strip == ''
if @raffled_word.include?(letter)
# (...)
else
@missed_parts << HANGMAN_PARTS[@wrong_guesses]
@wrong_guesses += 1
return false
end
end
AorodaroRSpecagora,podemosverqueeleestánoverde.Eomelhor,aorodar
oCucumber,vemosqueeletambémestánoverde:
$ bundle exec cucumber -t @wip
(...)
1 scenario (1 passed)
7 steps (7 passed)
Retireatag @wipdessecenárioevamosparaosdoisúltimoscenáriosdesta
funcionalidade.
227

## Página 242

10.5. FinalizandoafuncionalidadeAdivinharletra CasadoCódigo
Jogador pode tentar adivinhar mais de uma letra
Osdoiscenáriosqueestãofaltandoparafinalizarmosestafuncionalidadesão:
Cenário: Jogador advinha com sucesso duas vezes
Quanto mais o jogador for acertando, mais o jogo vai mostrando pra
ele as letras que ele adivinhou.
Cenário: Jogador erra três vezes ao adivinhar letra
Quanto mais o jogador for errando, mais partes do boneco da forca
são perdidas.
Aideiadessescenáriosétestaroqueacontecequandoojogadoracertaouerra
maisdeumavezaotentaradivinharumaletra.Vamoscome çarcriandootestede
aceitaçãoparaoprimeirocenário.
Otestedeaceitaçãoparaessecenárioconsistiráemsimularqueojogadoracerta
duasvezesaadivinhaçãodeletraeentãoojogodevemostrarparaojogadorasduas
letrasqueeleadivinhou.Escrevaessetestedoseguintemodo:
@wip
Cenário: Jogador advinha com sucesso duas vezes
Quanto mais o jogador for acertando, mais o jogo vai mostrando pra
ele as letras que ele adivinhou.
Dado que comecei um jogo
E que escolhi que a palavra a ser sorteada deverá ter "3" letras
Quando tento adivinhar que a palavra tem a letra "a"
E tento adivinhar que a palavra tem a letra "v"
E termino o jogo
Então o jogo termina com a seguinte mensagem na tela:
"""
a v _
"""
AorodaroCucumbervemosqueessetestepassa:
$ bundle exec cucumber -t @wip
(...)
1 scenario (1 passed)
7 steps (7 passed)
228

## Página 243

CasadoCódigo Capítulo10. Finalizandoasegundafuncionalidade
Essetestepassoudeprimeiraporqueocomportamentoespecificadoporesse
testeéapenasumaextensãodocomportamentodeadivinhaçãodeletracomsucesso,
eelejáfoiimplementadoantes.
Retireatag @wipdessetesteevamosparaopróximo.
Oúltimocenárioserviráparaverificarquequandoojogadorerramaisdeuma
vezaotentaradivinharumaletra,entãoojogodevemostrarpraeleaspartesque
obonecodaforcaperdeudeacordocomonúmerodeerros. Escrevaessetestedo
seguintemodo:
@wip
Cenário: Jogador erra três vezes ao adivinhar letra
Quanto mais o jogador for errando, mais partes do boneco da forca
são perdidas.
Dado que comecei um jogo
E que escolhi que a palavra a ser sorteada deverá ter "3 " letras
Quando tento adivinhar que a palavra tem a letra "z"
E tento adivinhar que a palavra tem a letra "y"
E termino o jogo
Então o jogo termina com a seguinte mensagem na tela:
"""
boneco da forca perdeu as seguintes partes do corpo: cabeça, corpo
"""
AorodarmosoCucumber,vemosqueessetestetambémpassadeprimeira!Ele
passoudeprimeirapelomesmomotivodoanterior,poiseleéapenasumaextensão
docomportamentodeerroaoadivinhardeletra. Comoessetesteestápassando,
vocêjápodetiraratag @wipdeletambém.
Paragarantirqueestátudook,rodeasuíteinteiradoRSpecedoCucumbere
verifiquequeelasestãonoverde.
Pronto,depoisdeumárduotrabalhoconstruindoessafuncionalidade,final-
menteafinalizamos. Agorafaltabempoucoparaterminarmosonossojogo,falta
apenasafuncionalidadedefinalizarjogo,sejapelojogadoradivinhandotodasas
letrasouerrandodemais.
10.6 P ontos-chave deste capítulo
Nestecapítuloconseguimosfinalizaraparteprincipaldonossojogo,afunciona-
lidadequepermiteaojogadortentaradivinharumaletra. Foiumcapítulolongo,
229

## Página 244

10.6. Pontos-chavedestecapítulo CasadoCódigo
nãosódevidoaodesenvolvimentodafuncionalidadeemsi,mastambémdevidoas
váriasatividadesquefizemoseaprendemosaolongodestecapítulo.
Começamosrefatorandonossojogoparacontrolarseuestadobaseadoemuma
máquinadeestados.Emcimadoresultadodesserefactoringfoipossívelcontinuar
odesenvolvimentodofluxodojogosemdeixarométodo GameFlow#next_step
commaiscondicionaisaninhadas.
Apósorefactoring,reorganizamosaestruturadostestesdeunidadedaclasse
GameFlowparaquealeituradostestesficassemaisfácileintuitiva.Émuitoimpor-
tantequeaoescreverumtestevocêpensenãosónoqueotesteestáverificando,mas
tambémpensarnotestecomoumaformadedocumentaç ãodoseusoftware.Sefor
fácildeleroseutesteeentenderarelaç ãodecausaeconsequênciadele,eleseráum
dosmelhoresartefatosdedocumentaçãodoseusistema,poiseleéumadocumen-
taçãoexecutável,logo,bastantefidedignaaocomportamentorealdoseusoftware.
Porfim,aprendemoseutilizamosumavariaç ãodatécnica Interface Discovery,
queutilizaoprocessodeTDDaliadaatestdoublesparadescobriredefiniraAPIdos
seusobjetos.Encorajovocêfortementealersobreaversãocanônicadessatécnicano
paper Mock roles, not Objects[6],paraquevocêentendaoporquêdemockobjectse
comoosseuscriadorespensaramqueelesdevemserutilizados.Lembre-se,mocks
estubssãodiferentesetemdiferentescasosdeuso[5].
230

## Página 245

Capítulo11
Finalizandonossojogo
Esteéoúltimocapítulododesenvolvimentodonossojogo.Atéentãoojogadorjá
podecomeçarumjogo,tentaradivinharumaletra,adivinharcomsucessoeadivi-
nharsemsucesso.Faltaapenasafuncionalidadequepermiteaojogadorganharou
perderojogo.Vamosdesenvolveressafuncionalidadeefinalmenteterminaronosso
jogo.
Aofinaldestecapítulovocêterádesenvolvidoumaaplicaçãocompletausando
TDDdocome çoaofim.Parabéns!
Issopodeserumpequenopassoparahomem,masumgrandepassonodesen-
volvimentodesoftwarecomqualidade!
11.1 E specificando o fim do jogo
Existem3modosdonossojogoterminar:
1) Jogadorterminajogonomeio;

## Página 246

11.2. Jogadorvenceojogo CasadoCódigo
2) Jogadorvenceojogo;
3) Jogadorperdeojogo
Oprimeiromodonósjádesenvolvemosnoscapítulosanteriores.Vamosfocar
agoranosegundoeterceiromodos.
Paraqueojogadorpossavencerojogoeleprecisaadivinhartodasasletrasdo
jogoantesquetodasaspartesdobonecodaforcaapare çam.
Paraqueojogadorpercaojogo,bastaqueeleerre6vezesaotentaradivinhar
umaletra.
Vamos criar um arquivo de Cucumber com o nome
features/fim_do_jogo.feature para documentar a especificação que
definimosacima:
# language: pt
Funcionalidade: Fim do jogo
O jogo termina em dois cenários:
1. O jogador adivinhou todas as letras da palavra,
então ele ganha! :)
2. O jogador errou 6 vezes ao tentar adivinhar as letras da palavra,
então ele perde. :(
Cenário: Jogador vence o jogo
Para que o jogador possa vencer o jogo ele precisa adivinhar todas
as letras do jogo antes que todas as partes do boneco da forca
apareçam.
Cenário: Jogador perde o jogo
Para que o jogador perca o jogo, basta que ele erre 6 vezes ao
tentar adivinhar uma letra.
Comaespecificaçãoecritériodeaceitedefinidos,vamosagoraescrevertestes
comoCucumberparaimplementaressescritériosdeaceite. Vamoscome çarpelo
cenárioondeojogadorvenceojogo.
11.2 J ogador vence o jogo
Parafazermosumtestedocenárioondeojogadorvenceojogo,bastasimularmos
queojogadorconsegueadivinhartodasasletrasdapalavraeverificarmosseuma
232

## Página 247

CasadoCódigo Capítulo11. Finalizandonossojogo
mensagemdesucessoéimpressanatela. Escrevaessetestedoseguintemodono
arquivo features/fim_do_jogo.feature:
Contexto:
* o jogo tem as possíveis palavras para sortear:
| número de letras | palavra sorteada |
| 3 | avo |
@wip
Cenário: Jogador vence o jogo
Para que o jogador possa vencer o jogo ele precisa adivinhar todas
as letras do jogo antes que todas as partes do boneco da forca
apareçam.
Dado que comecei um jogo
E que escolhi que a palavra a ser sorteada deverá ter "3 " letras
Quando tento adivinhar que a palavra tem a letra "a"
E tento adivinhar que a palavra tem a letra "v"
E tento adivinhar que a palavra tem a letra "o"
Então o jogo termina com a seguinte mensagem na tela:
"""
Você venceu! :)
"""
Percebaquealémdosstepsdocenárioemsi,foinecessáriocolocarosstepsdo
Contexto,paraquefossepossívelsaberquequandoojogosortearumapalavracom
3letras,apalavrasorteadaserá“avo”.EsseContextoéomesmoqueusamosnafun-
cionalidade“Adivinharletra”.
AorodaroCucumberdessaspecvemosqueelefalhacomaseguintemensagem:
$ bundle exec cucumber -t @wip
(...)
Então o jogo termina com a seguinte mensagem na tela:
# features/step_definitions/game_steps.rb:43
"""
Você venceu! :)
"""
process still alive after 3 seconds (ChildProcess::TimeoutError)
233

## Página 248

11.2. Jogadorvenceojogo CasadoCódigo
Pelamensagemdeerropodemosverqueoproblemaapontadoéqueapósa
execuçãodetodososstepsdonossoteste,oprocessodojogonãoterminou.Elenão
terminouporquenessecenárionãoestamosutilizandoaquelestep "E termino o jogo”
queutilizamosnasoutrasspecsdeCucumberdonossosistema. Nãoprecisamos
utilizaressestepporqueocomportamentoesperadoéqueaojogadoracertartodasas
letrasdapalavra,ojogoimprimeumamensagemdesucessoeterminaoseuprocesso
semsernecessárioqueojogadordigitemaisnada.
DadoqueessaspecdeCucumberestánovermelho,vamosescreverumaspec
deRSpecparaespecificarocomportamentoesperado.
Vamoscomeçarprimeirocomaestruturadostestesquequeremosescrever.
Quandoojogadorganharojogo,ojogoestaránoestado :endedeojogodeve
imprimirumamensagemdesucesso.Escrevaaseguinteestruturadespecparaesse
comportamentonoarquivo spec/game_flow_spec.rb:
describe "#next_step" do
# (...)
context "when the game is in the 'ended' state" do
before { game.stub(state: :ended) }
it "prints a success message when the player win"
end
Amensagemdesucessoquandoojogadorvencerojogoserá:“Vocêvenceu!:)”.
Paraverificarqueamensagemdesucessofoiimpressa,bastaverificarqueamensa-
gem writefoienviadaparaoobjeto uicomoargumentocorreto:
it "prints a success message when the player win" do
ui.should_receive(:write).with("Você venceu! :)")
game_flow.next_step
end
Faltaapenasumainformaçãonosetupdesseteste.Paraqueo game_flowsaiba
queojogadorvenceuojogo,nãobastasaberqueojogoacabouequeoobjeto game
estanoestado :ended,énecessáriosaberqueojogoacaboueojogadorvenceu.
Vamosimaginarentãoqueexistaummétodochamado Game#player_won?que
retornaessainformaçãoevamosstubaressemétodonosetupdonossoteste:
234

## Página 249

CasadoCódigo Capítulo11. Finalizandonossojogo
it "prints a success message when the player win" do
game.stub(player_won?: true)
ui.should_receive(:write).with("Você venceu! :)")
game_flow.next_step
end
AorodaroRSpec,vemosqueessetestequebra. Parafazê-lopassar,bastaque
modifiquemosométodo GameFlow#next_stepparalidarcomoestado :ended
doobjetogame,checandoseojogadorganhouparapoderimprimiramensagemde
sucesso:
def next_step
case @game.state
when :initial
ask_to_raffle_a_word
when :word_raffled
ask_to_guess_a_letter
end
print_game_final_result if @game.ended?
end
private
# (...)
def print_game_final_result
if @game.player_won?
@ui.write("Você venceu! :)")
end
end
AorodaroRSpecagora,podemosverqueotesteestánoverde.Agoraéneces-
sárioimplementarmosométodoquestubamos,o Game#player_won?.
Essemétododeveteroseguintecomportamento:
• deveretornarfalseseojogonãoestivernoestado :ended,jáqueseo
jogadorganhou,ojogotemqueestarnoestadofinal;
• deveretornartruecasoojogadortenhaadivinhadotodasasletrascomsu-
cesso;
235

## Página 250

11.2. Jogadorvenceojogo CasadoCódigo
• deveretornarfalsecasoojogadornãotenhaadivinhadotodasasletrascom
sucesso.
Vamoscomeçarescrevendoumtesteparaocenáriodesucesso,quandoomé-
todoretorna true. Nessetestequeremossimularqueojogadoradivinhoutodas
asletrascomsucessoparaentãoverificarqueoretornodométodo player_won?
serátrue. Parasimularessecenário,devemosprimeirocolocaroobjeto game
noestado :word_raffled, depoisfazercomquetodasasletrassejamadivi-
nhadascomsucesso.Implementeessecomportamentonumnovotestenoarquivo
spec/game_spec.rb:
describe "#player_won?" do
it "returns true when the player guessed all letters with success" do
game.state = :word_raffled
game.raffled_word = "hi"
game.guess_letter("h")
game.guess_letter("i")
game.player_won?.should be_true
end
end
Aorodaresseteste,vemosqueelequebra.Parafazê-lopassar,precisamosim-
plementarométodo Game#player_won?,fazê-lochecarqueoestadodoobjeto
gameéiguala :endedefazê-lochecarseojogadoradivinhoutodasasletrascom
sucesso.Escrevaessemétododoseguintemodonoarquivo lib/game.rb:
def player_won?
return false if @state != :ended
raffled_word_letters = @raffled_word.to_s.chars.to_a.uniq.sort
@guessed_letters.sort == raffled_word_letters
end
Ao rodar o teste, vemos que ele continua quebrando. Ele está retornando
falseporqueoestadodojogoestáchegandocomo :word_raffled,nãocomo
:ended.Issoaconteceporqueatéentãoninguémestáfazendoatransiçãodoestado
:word_raffledpara :endedquandoojogadoradivinhatodasasletrascomsu-
cesso.Essatransiçãodeveriaserfeitapelométodo Game#guess_letter,quando
236

## Página 251

CasadoCódigo Capítulo11. Finalizandonossojogo
ojogadoradivinhartodasasletrascomsucesso.Vamosescreverumtesteparaesse
comportamentonoarquivo spec/game_spec.rb:
describe "#guess_letter" do
# (...)
it "makes a transition to the 'ended' state when all the letters " <<
"are guessed with success" do
game.state = :word_raffled
game.raffled_word = "hi"
expect do
game.guess_letter("h")
game.guess_letter("i")
end.to change { game.state }.from(:word_raffled).to(:ended)
end
end
Aorodaresseteste,vemosqueelequebra. Parafazê-lopassar,vamosfazero
métodoGame#guess_letteratualizaroestadopara :endedquandoojogador
conseguiradivinhartodasasletras:
def guess_letter(letter)
return false if letter.strip == ''
if @raffled_word.include?(letter)
@guessed_letters << letter
@guessed_letters.uniq!
@state = :ended if all_letters_were_guessed?
return true
else
@missed_parts << HANGMAN_PARTS[@wrong_guesses]
@wrong_guesses += 1
return false
end
end
Notequeutilizamosummétodochamado all_letters_were_guessed?
que ainda não existe. Esse método deve retornartrue quando todas as le-
237

## Página 252

11.2. Jogadorvenceojogo CasadoCódigo
trasjáforamadivinhadas. Implementeelecomoummétodoprivadonoarquivo
lib/game.rb:
private
def all_letters_were_guessed?
raffled_word_letters = @raffled_word.to_s.chars.to_a.uniq.sort
@guessed_letters.sort == raffled_word_letters
end
Aorodarmosostestesagora,vemosquetodospassaram. Inclusiveotestedo
métodoGame#player_won?!Vamosparaarefatoração.
Percebaqueosmétodo player_won?e all_letters_were_guessed?tem
muitaduplicação:
def player_won?
return false if @state != :ended
raffled_word_letters = @raffled_word.to_s.chars.to_a.uniq.sort
@guessed_letters.sort == raffled_word_letters
end
private
def all_letters_were_guessed?
raffled_word_letters = @raffled_word.to_s.chars.to_a.uniq.sort
@guessed_letters.sort == raffled_word_letters
end
Para retiramos essa duplicação, basta reutilizarmos o método
all_letters_were_guessed?dentrodométodo player_won?:
def player_won?
return false if @state != :ended
all_letters_were_guessed?
end
RodeoRSpeceverifiquequeelecontinuanoverde. ComoRSpecinteirono
verde,podemosescreverosoutrostestesdométodo player_won?.
238

## Página 253

CasadoCódigo Capítulo11. Finalizandonossojogo
Vamosescreverotesteparaocasoquandoojogadorterminouojogomasnão
conseguiuadivinhartodasasletras. Paraojogadorterminarojogosemteradivi-
nhadotodasasletras,eletemquetererradoseisvezes:
describe "#player_won?" do
# (...)
it "returns false when the player didn 't guessed all letters" do
game.state = :word_raffled
game.raffled_word = "hi"
6.times { game.guess_letter("z") }
game.player_won?.should be_false
end
end
AorodaroRSpec,podemosverqueessetestepassaantesmesmodetermosim-
plementandoocódigoparafazê-lopassar.NofluxodeTDD,normalmentequando
escrevemosumteste,primeiroeledevequebrar,esódepoisqueimplementarmos
códigodeprodução,eledevepassar.Nessecasootestejápassoudeprimeira,sema
necessidadedeescrevermoscódigonovo.
Quandoaconteceralgoassim,vocêdevesecertificarqueseutesteestárealmente
testandooquevocêquerequeseutesteestápassandopelomotivocorreto.Nocaso
dessetesteemquestão,eleestápassando,masnãoestápassandopelomotivocorreto.
Eleestápassandoporqueoestadodoobjeto gamenessetesteficousetadocomo
:word_raffled,poisnãoaconteceuatransiç ãoparaoestado :ended.Ouseja,
quemestáfazendoo return falsedométodo player_won?nessetestenão
éachecagemdequeojogadoradivinhoutodasasletrascomsucesso,massima
primeiralinhadométodoqueverificaoestadodoobjeto game:
def player_won?
return false if @state != :ended
all_letters_were_guessed?
end
Oqueprecisaserfeitoéespecificareimplementarquequandoojogadorerra
seisvezes,ométodo guess_letterfaráatransiçãodoestado :word_raffled
para :ended. MasfaremosissosóquandoformostestarocenáriodeCucumber
239

## Página 254

11.2. Jogadorvenceojogo CasadoCódigo
quandoojogadorperdeojogo. Porenquanto,vamosnosateraocenárioondeo
jogadorvenceojogo.
Ficoufaltandofazermosumúltimotestedométodo player_won?,queéo
testequeverificaqueoretornoé falsequandoojogonãoestánoestado :ended:
describe "#player_won?" do
# (...)
it "returns false when the game is not in the 'ended' state" do
game.state = :initial
game.player_won?.should be_false
game.state = :word_raffled
game.player_won?.should be_false
end
AorodarmosoRSpec,vemosquecontinuatodonoverde.VamosrodaroCu-
cumbereverificarsefinalizamosoprimeirocenáriodafuncionalidadede“fimdo
jogo":
$ bundle exec cucumber -t @wip
(...)
1 scenario (1 passed)
7 steps (7 passed)
OCucumberestánoverde,terminamosessecenário!Retireatag @wipdesse
cenárioerodeasuíteinteiradeCucumberparaverificarseosistemainteirocontinua
funcionando:
$ bundle exec cucumber
(...)
9 scenarios (9 passed)
47 steps (47 passed)
ComopodemosverpelasaídadoCucumber,estátudonoverde.Sabendoque
todosostestesdeCucumbereRSpecestãonoverde,podemosirparaopróximo
cenário,queserásobrequandoojogadorperdeojogo.
240

## Página 255

CasadoCódigo Capítulo11. Finalizandonossojogo
11.3 J ogador perde o jogo
Naseção11.1nósjáespecificamosocritériodeaceitedocenárioquandoojogador
perdeojogo:
Cenário: Jogador perde o jogo
Para que o jogador perca o jogo, basta que ele erre 6 vezes ao
tentar adivinhar uma letra.
Agoraprecisamosdefinirosstepsdessecenário. Paraimplementaressecená-
rio,bastasimularmosojogadorerrandoseisvezesaotentaradivinharumaletrada
palavrasorteadaeverificarmosqueamensagem“Vocêperdeu. :(”éimpressana
tela:
@wip
Cenário: Jogador perde o jogo
Para que o jogador perca o jogo, basta que ele erre 6 vezes ao
tentar adivinhar uma letra.
Dado que comecei um jogo
E que escolhi que a palavra a ser sorteada deverá ter "3 " letras
Quando tento adivinhar que a palavra tem a letra "z" "6" vezes
Então o jogo termina com a seguinte mensagem na tela:
"""
Você perdeu. :(
"""
Notequeparafazerojogadorerraraotentaradivinharumaletra,estamossi-
mulandoqueeledigitouseisvezesaletra“z”. Sabemosquealetra“z”nãoestána
palavrasorteadanessecenário,porqueessecenáriotambémrodanomesmocon-
textodocenárioqueojogadorvenceojogo,noqualapalavrasorteadacomtrês
letraé“avo”.
AorodarmosoCucumberparaessecenário,vemosqueumstepestáindefinido:
$ bundle exec cucumber -t @wip
(...)
1 scenario (1 undefined)
5 steps (1 skipped, 1 undefined, 3 passed)
0m0.131s
241

## Página 256

11.3. Jogadorperdeojogo CasadoCódigo
You can implement step definitions for undefined steps with
these snippets:
Quando /^tento adivinhar que a palavra tem a letra "(.*?)" "(.*?)"
vezes$/ do |arg1, arg2|
pending # express the regexp above with the code you wish you had
end
Essestepqueestáindefinidoémuitoparecidocomumstepquejátemospronto:
Quando /^tento adivinhar que a palavra tem a letra "(.*?)"$/ do |letter|
steps %{
When I type "#{letter}"
}
end
Para implementar esse step indefinido, podemos reutilizar o step
definition já pronto, simplesmente o chamando o número de ve-
zes que for necessário. Faç a isso do seguinte modo no arquivo
features/step_definitions/game_steps.rb:
Quando /^tento adivinhar que a palavra tem a letra "(.*?)" \
"(.*?)" vezes$/ do |letter, number_of_guesses|
number_of_guesses.to_i.times do
steps %{
* tento adivinhar que a palavra tem a letra "#{letter}"
}
end
end
PercebaquenossonovostepdefinitionirásimplesmentechamarooutrostepN
vezes.Nocasodonossocenário,eleiráchamarseisvezes.
RodeoCucumberparaessecenárioeverifiqueasaída:
$ bundle exec cucumber -t @wip
(...)
process still alive after 3 seconds (ChildProcess::TimeoutError)
Failing Scenarios:
cucumber features/fim_do_jogo.feature:32 # Scenario: Jogador perde o jogo
242

## Página 257

CasadoCódigo Capítulo11. Finalizandonossojogo
1 scenario (1 failed)
5 steps (1 failed, 4 passed)
PelasaídadoCucumberpodemosverqueotestenãopassouporqueapóstodos
osstepsdoseremexecutados,oprocessodonossojogounãoterminou.Essemesmo
comportamentoaconteceuquandoescrevemosocenáriodequandoojogadorvence
ojogo. Issoestáacontecendoporqueaojogadorerrarseisvezes,ojogonãoestá
finalizandosozinhoenemimprimindoamensagemdederrota. Vamosescrever
testesdeunidadeparaespecificaressecomportamento.
Vamoscomeçarespecificandoofluxodojogoquandoojogadorperde.Escrevao
seguintetestenoarquivo spec/game_flow_spec.rbparaespecificarquequando
ojogadorperde,umamensagemdederrotaéimpressa:
context "when the game is in the 'ended' state" do
before { game. stub(state: :ended) }
# (...)
it "prints a defeat message when the player lose" do
game.stub(player_won?: false)
ui.should_receive(:write).with("Você perdeu. :(")
game_flow.next_step
end
end
Notequeparasaberquejogadorperdeu,estamosacreditandoqueocontratodo
métodoGame#player_won?éretornar falsenessecaso.
AorodaroRSpec,vemosqueessetestaquebra.Parafazê-lopassar,bastaalterar-
mosométodoprivado GameFlow#print_game_final_result. Atéentãoele
estáassim:
def print_game_final_result
if @game.player_won?
@ui.write("Você venceu! :)")
end
end
243

## Página 258

11.3. Jogadorperdeojogo CasadoCódigo
Modifiqueessemétodoparalidarcomocenárioquando @game.player_won?
retornar false:
def print_game_final_result
if @game.player_won?
@ui.write("Você venceu! :)")
else
@ui.write("Você perdeu. :(")
end
end
Ao rodarmos o RSpec, podemos ver que agora está no verde. Antes de
seguirmos em frente e rodarmos o Cucumber, lembre-se que na seção ante-
rior, falamosqueaindaeranecessárioespecificareimplementarqueométodo
Game#guess_letterdevefazerumatransiçãodeestadoparaoestado :ended
quandoojogadorerrarseisvezesaotentaradivinharumaletra.Vamosfazerisso.
Escreva o seguinte teste para especificar esse comportamento no arquivo
spec/game_spec.rb:
describe "#guess_letter" do
# (...)
it "makes a transition to the 'ended' state when the player " <<
"miss 6 times trying to guess a letter " do
game.state = :word_raffled
game.raffled_word = "hi"
expect do
6.times { game.guess_letter("z") }
end.to change { game.state }.from(:word_raffled).to(:ended)
end
end
AorodarmosoRSpec,vemosqueessetestequebra. Parafazê-lopassar,pre-
cisamosalterarométodo Game#guess_letterparafazeratransiçãodeestado
quandoojogadorerrarseisvezes.Atéentãoessemétodoestádoseguintemodo:
def guess_letter(letter)
return false if letter.strip == ''
if @raffled_word.include?(letter)
244

## Página 259

CasadoCódigo Capítulo11. Finalizandonossojogo
# (...)
else
@missed_parts << HANGMAN_PARTS[@wrong_guesses]
@wrong_guesses += 1
return false
end
end
Notequejáexisteumcontadordequantasvezesojogadorerrou.Bastafazermos
atransiçãodeestadoquandoessecontadorforigualaseis:
def guess_letter(letter)
return false if letter.strip == ''
if @raffled_word.include?(letter)
# (...)
else
@missed_parts << HANGMAN_PARTS[@wrong_guesses]
@wrong_guesses += 1
@state = :ended if @wrong_guesses == 6
return false
end
end
AorodarmosoRSpecagora,vemosqueeleestánoverde. Aproveiteerodeo
Cucumberdocenárioqueestamostrabalhando:
$ bundle exec cucumber -t @wip
(...)
1 scenario (1 passed)
5 steps (5 passed)
OCucumberestánoverdetambém, finalizamosoúltimocenáriodonosso
jogo!!!Agoraqueessecenárioestánoverde,retireatag @wipdele.
Apenasparaverificarqueestátudook,rodeoRSpeceCucumberdasuíteinteira
econfirmequeestátudonoverde.
Sim,terminamosdedesenvolvernossojogo. Esperoquetenhasidotãolegal
paravocêquantofoiparamim.
245

## Página 260

11.4. Próximospassos CasadoCódigo
11.4 P róximos passos
VocêacaboudeconstruirumaaplicaçãointeirausandoTDDeoutside-indevelop-
mentdocome çoaofim.Esperoqueodesenvolvimentodessaaplicaç ãotenhadei-
xadomaisclaroparavocêcomoédesenvolversoftwareutilizandoTDD.
Vocêagorajádeveentenderotradicionalfluxo“red,green,refactor”doTDD.
Deveentendertambématécnica“outside-indevelopment”,queéomodopadrãode
desenvolversoftwaresegundoafilosofiadoBDD(behavior-drivendevelopment).
Opróximopassoparavocêganharconfian çaeexperiêncianodesenvolvimento
desoftwareorientadoatestesépraticar. Praticar,praticarepraticar. Odesenvol-
vimentoquefizemosnestelivrofoiapenasumdosseusprimeirosexercíciosnesta
técnica.IncentivovocêautilizarTDDemtodososseuspróximosprojetos,poissó
assimvocêpoderádominaressatécnica.
Voudeixartambémumaliçãodecasaparavocêjáterpelomenosumpróximo
exercícioafazer.Nolivro T est-Driven Development: T este e Design no Mundo Real[1],
oMauricioAnichefalaquemuitostestesparaumúnicométodopodeserumindício
deproblemadedesign.Devemosouvirofeedbackdosnossostesteseutilizá-lopara
melhorarodesigndonossosoftware. Nossojogotemumcasocommuitostestes
paraummétodosó,noarquivo spec/game_flow_spec.rb:
$ rspec -fd -e "#next_step" spec/game_flow_spec.rb
GameFlow
#next_step
finishes the game when the player asks to
when the game is in the 'initial' state
asks the player for the length of the word to be raffled
and the player asks to raffle a word
raffles a word with the given length
prints a '_' for each letter in the raffled word
tells if it 's not possible to raffle with the given length
when the game is in the 'word raffled' state
asks the player to guess a letter
and the player guess a letter with success
prints a success message
prints the guessed letters
and the player fails to guess a letter
prints a error message
prints the list of the missed parts
246

## Página 261

CasadoCódigo Capítulo11. Finalizandonossojogo
when the game is in the 'ended' state
prints a success message whe the player win
prints a defeat message when the player lose
Percebaquãograndeéonúmerodetestesquefizemossóparaessemétodoomé-
todo GameFlow#next_step.Seudeverdecasaserárefatoraraclasse GameFlow
paraevitarquesejanecessáriofazertantostestesparaummétodosó. Faç aissoe
mandeoresultadodasuarefatoraçãocomumlinkparaseuGithubparaoendere ço
dalistadee-maildestelivro,queécasadocodigo-tdd-ruby@googlegroups.com.
247

## Página 263

CasadoCódigo ReferênciasBibliográficas
Referências Bibliográficas
[1] M.Aniche. T est-Driven Development: T este e Design no Mundo Real. Casado
Código,2012.
[2] BarryWBoehm.Softwareengineeringeconomics.1981.
[3] DavidChelimsky,DaveAstels,ZachDennis,AslakHellesøy,BryanHelmkamp,
andDanNorth. Therspecbook.2009.
[4] EricEvans.Domain-drivendesign:tacklingcomplexityintheheartofsoftware.
2004.
[5] M. Fowler. Mocks aren’t stubs. http://martinfowler.com/articles/
mocksArentStubs.html.
[6] S.Freeman,T.Mackinnon,N.Pryce,andJ.Walnes. Mockroles,notobjects.
2004.
[7] S.FreemanandN.Pryce. Growingobject-orientedsoftware,guidedbytests.
2009.
[8] T.Mackinnon,S.Freeman,andP.Craig.Endo-testing:unittestingwithmock
objects.2001.
[9] R.C.Martin. Principlesofood. http://butunclebob.com/ArticleS.UncleBob.
PrinciplesOfOod.
[10] G.Meszaros.xunittestpatterns:Refactoringtestcode.2007.
[11] D.North.Introducingbdd.http://dannorth.net/introducing-bdd/.
249