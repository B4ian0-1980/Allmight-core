---json
{
  "id": "swift_programe_para_iphone_e_ipad_1",
  "title": "Swift Programe para iPhone e iPad",
  "categoria": "04-frameworks",
  "subcategoria": "mobile",
  "resumo": "**Arquivo Original:** `Swift Programe para iPhone e iPad.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "frameworks",
    "ipad",
    "iphone",
    "mobile",
    "para",
    "programe",
    "swift"
  ],
  "perguntas_tipo": [
    "Como utilizar Swift Programe para iPhone e iPad?",
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

# Swift Programe para iPhone e iPad

> **Arquivo Original:** `Swift Programe para iPhone e iPad.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 2

© Casa do Código
T odos os direitos reservados e protegidos pela Lei nº9.610, de
10/02/1998.
Nenhuma parte deste livro poderá ser reproduzida, nem transmitida, sem
autorização prévia por escrito da editora, sejam quais forem os meios:
fotográﬁcos, eletrônicos, mecânicos, gravação ou quaisquer outros.
Casa do Código
Livros para o programador
Rua Vergueiro, 3185 - 8º andar
04101-300 – Vila Mariana – São Paulo – SP – Brasil

## Página 3

CasadoCódigo Sumário
Sumário
1 Introdução 1
1.1 Motivação: mobile ......................... 1
1.2 Motivação: boaspráticasecodesmells ............. 2
1.3 Agradecimentos .......................... 2
2 Projeto:nossaprimeiraApp 5
2.1 InstalandooXcode ........................ 5
2.2 NossaprimeiraApp ........................ 6
2.3 ViewControllerdecadastroderefeição ............. 9
2.4 Boaprática: placeholderekeyboardtype ............ 2 3
2.5 Conectandoainterfaceaocódigo ................ 2 4
2.6 Conectandovariáveismembroàsuapartevisual: @IBOutlet 32
2.7 Resumo ............................... 3 8
3 Swift:alinguagem 39
3.1 Brincandonoplayground ..................... 3 9
3.2 Arrays ................................ 4 8
3.3 Boaprática: cuidadocominferênciadetipos ......... 5 2
3.4 Resumo ............................... 5 3
4 Swift:mapeandonossosmodeloseintroduçãoàOrientaçãoaOb-
jetos 55
4.1 Boaprática: organizandoosdados ............... 5 5
4.2 Boaprática: Goodcitizen(evitenulos )eoinit ........ 6 4
i

## Página 4

Sumário CasadoCódigo
4.3 NossoGoodCitizen ........................ 6 4
4.4 Codesmell(malcheirodecódigo): opcional! ......... 7 0
4.5 Resumo ............................... 7 1
5 Projeto:organizandomodeloscomOOearquivosemgrupos 73
5.1 Boaprática: crieumdiretórioporgrupo ............ 7 4
5.2 Movendoarquivosnosistemaoperacional ........... 7 8
5.3 AplicandoobásicodeOrientaçãoaObjetos .......... 8 3
5.4 Resumo ............................... 8 7
6 ListandoasrefeiçõescomTableViewController 89
6.1 TabelasdinâmicasusandoDynamicPrototypes ........ 9 7
6.2 Resumo ............................... 1 0 7
7 Projeto:listaderefeições 109
7.1 Resumo ............................... 1 1 3
8 Navegandoentretelas 115
8.1 Navegandocomumapilhadetelas ............... 1 1 9
8.2 Resumo ............................... 1 2 1
9 Designpattern:delegate 123
9.1 Configurandoumdelegateviasegue .............. 1 2 7
9.2 Codesmell: nomesgenéricosdemaisecomoextrairumpro-
tocolo ................................ 1 3 1
9.3 Resumo ............................... 1 3 5
10 Relacionamentoumparamuitos:listadealimentos 137
10.1 ProtocolosdaAPI ......................... 1 4 1
10.2 SeleçãomúltiplaeCellAccessory ................ 1 4 2
10.3 Desselecionandoelementos ................... 1 4 6
10.4 Armazenandoaseleção ...................... 1 4 6
10.5 Resumo ............................... 1 5 2
ii

## Página 5

CasadoCódigo Sumário
11 Criandonovositens 153
11.1 Pushandoviewsparaapilhaprogramaticamente ....... 1 6 3
11.2 Voltandodeumpushprogramático ............... 1 6 5
11.3 Invocandoumdelegatedeformaprogramática ........ 1 6 8
11.4 Resumo ............................... 1 7 8
12 MostrandoosdetalhesdeumarefeiçãocomLongpress 179
12.1 Recuperandoondeocorreuumeventodelongpress ..... 1 8 2
12.2 Mostrandoosdetalhesemumalerta .............. 1 8 6
12.3 Mostrandoosdetalhesdositens ................. 1 9 3
12.4 Resumo ............................... 1 9 6
13 Alerta:optionalseerros 197
13.1 Boaprática: eviteoptional,garantatudocomiflet ...... 2 0 0
13.2 Tratandooerrocomumamensagemnovamente ....... 2 0 0
13.3 Boaprática: mensagensdeerrodescritivas ........... 2 0 2
13.4 Refatoração: tratandodiversoserros .............. 2 0 4
13.5 Parâmetrosdefault ......................... 2 0 6
13.6 Boaprática:SingleResponsibilityPrinciple,PrincípiodeRes-
ponsabilidadeÚnica ........................ 2 0 8
13.7 Casosmaiscomplexosdetratamentodeerro ......... 2 0 9
13.8 Codesmell: Nestedifs ....................... 2 1 0
13.9 Resumo ............................... 2 1 4
14 Removendoumarefeição 215
14.1 Açõesdestrutivaseestilos .................... 2 1 5
14.2 Passandoumafunçãocomocallback .............. 2 1 7
14.3 Indentificandoalinhaaserremovida .............. 2 2 0
14.4 Removendoeatualizandoatela ................. 2 2 3
14.5 Closures ............................... 2 2 4
14.6 Codesmell: closuresarodo ................... 2 2 5
14.7 Resumo ............................... 2 2 9
iii

## Página 6

Sumário CasadoCódigo
15 Armazenandoasrefeiçõesdentrodofilesystem 231
15.1 Salvandoasrefeiçõesnosistemadearquivos .......... 2 3 7
15.2 Salvandoelendoitensnosistemadearquivos ......... 2 4 2
16 Boaprática:dividindoresponsabilidade seoDataAccessObject 249
17 Aondechegamosepróximospassos 255
iv

## Página 7

Capítulo1
Introdução
1.1 Motivação:mobile
OmercadoiOScrescecadavezmaisnoBrasil,eseadecisãodeumaempresa
ou indivíduo é a de criar aplicações nativas, a escolha prática para o mundo
iOSacabasendoentreObjectiveCouSwift.
Comoumalinguagemnovaebeta,Swiftaindapossuiespaçoparapeque-
nasmudançasquepodemalteraramaneiradeumprogramadordesenvolver
umaaplicação,masnesseinstanteaApplejáaconsideramaduraosuficiente
paraquenovosaplicativospossamsercriadoscomela.
Porsernova,foramtrazidosconceitosqueestãoemvoganacomunidade
de desenvolvimento em geral, como podemos ver a influência da linguagem
ScalaemS wift.
Como uma linguagem compilada e com uma IDE rica, recebemos mui-
tasnotificaçõesdepossíveiserrosaindaemtempodedesenvolvimento,oque

## Página 8

1.2. Motivação: boaspráticasecodesmells CasadoCódigo
evitadiversoserrostradicionais,comooacessoaponteirosinválidosname-
mória,algomuitofácildeseprotegeremSwift.
Para desenvolvedores novos no mundo iOS, este livro busca ser um guia
queensinadiversaspartesdalinguagemedaAPIdisponívelduranteacriação
emanutençãodeumaaplicaçãomobilecompleta.
Todososníveisdedesenvolvedorespodemsebeneficiardosconceitosde
boaspráticas, codesmells,refatoraçõese designpatterns apresentadosnolivro.
1.2 Motivação:boaspráticasecodesmells
Oobjetivodesselivronãoésomenteguiá-loatravésdesuaprimeiraaplicação
iOS, mas sim de ser capaz de julgar por si só o que é uma boa estratégia de
programação,pormeiodaintroduçãodeumadezenadeboaspráticase code
smellsque facilitam ou dificultam a manutenção do código com o passar do
tempo.
Umcodesmelléum sinalforte dequeexistealgodeestranhonocódigo,
nãoumagarantiadequeexistaumproblema. Damesmaforma,boaspráticas
e design patterns possuem situações específicas que podem trazer mais mal
doquebenefícios. Comofazemosnolivro,todasituaçãoencontradadeveser
analisadafriamente:qualocustodemanterocódigocomoestáequalocusto
derefatorá-lo?
Saber pesar e tomar decisões como essa diferenciam um programador
iniciantedeumprofissionaleéissoquebuscamosaqui: nãosomenteensinar
aprogramar,massimcriarprofissionaisemnossaárea.
São dezenas de boas práticas, design patterns e code smells catalogados
no decorrer do livro que podem ser acessados diretamente através do índice
remissivo.
1.3 Agradecimentos
Gostaria de agradecer ao desafio proposto pelo Paulo SilveiraeoA d r i a n o
Almeida. Não é fácil escrever um livro de boas práticas de linguagem e API
quando uma é tão nova e a outra carregada de decisões antigas. É delicado
entender as implicações de cada decisão da linguagem, mas o aprendizado
quepassamospo restep r o jetoéoquetr o uxeaeletan tovalo r .
2

## Página 9

CasadoCódigo Capítulo 1. Introdução
Um agradecimento especial ao Hugo Corbucci que tanto nos ajudou na
revisãodolivro,eaoRodrigoTurini,amboscompartilharamconoscoosbugs,
as dificuldades e as alegrias de utilizar e ensinar uma linguagem ainda em
desenvolvimento. Agradecemostambémpelasconversasediscussõesdepa-
drõeseboaspráticascomoMaurícioAniche,alémdoFranciscoSokol,Diego
Chohfi,UbiratanSoareseoutros.
3

## Página 11

Capítulo2
Projeto: nossaprimeiraApp
2.1 InstalandooXcode
O processo de instalação do Xcode se tornou bem simples, basta acessar a
AppleStoreeprocurarpeloXcode. Cliqueeminstalar.

## Página 12

2.2. NossaprimeiraApp CasadoCódigo
SevocêdesejausarumaversãobetadoXcode,entrenoprogramade beta
developersda Apple e siga o link de download de uma versão beta. Cuidado,
versões beta podem sofrer alterações e quebrar a qualquer instante - e que-
bram.
2.2 NossaprimeiraApp
Nossa aplicação será um gerenciador de calorias e felicidade. Como usuário
final eu faço um diário das comidas que ingeri, indicando quais alimentos
estavam dentro dela e o quão feliz fiquei. Meu objetivo final seria descobrir
quais alimentos me deixam mais felizes com o mínimo de calorias possíveis,
umparaíso.
Paraissoseránecessáriocadastrarrefeições(
Meal)epa racadar ef eição
queremosincluirositens( Item)queacompõem.Desejamoslistaressasre-
feiçõesefazerorelacionamentoentreessesdoismodelos,afinalumarefeição
possuidiversositens,alémdearmazenartodosessesdadosnocelular.
Porfim,veremosoprocessodeexecuçãodenossaappemumsimulador,
6

## Página 13

CasadoCódigo Capítulo2. Projeto: nossaprimeiraApp
eodedeplo ydenossaa pptan toemumcel ularparticularparatestesquan to
naappstore.
Isso tudo será intercalado com seções de boas práticas de desenvolvi-
mento de softwares e caixas de informações extras, ambos ganchos para que
você possa se tornar um bom programador à medida que pesquisa a infor-
mação contida nessas seções e se aprofunda nelas. Não se sinta obrigado a
pesquisá-las no mesmo momento que as lê, sugiro, inclusive, que você ter-
mine primeiro o conteúdo aqui apresentado para só então se aprofundar.
Dessa forma, terá uma opinião mais formada sobre diversos itens ao entrar
nessasdiscussõesavançadassobrequalidadedecódigo,usabilidadeetc.
Ao término de nossa jornada, teremos uma aplicação com diversas fun-
cionalidades,entreelas,adicionarnovasrefeições:
7

## Página 14

2.2. NossaprimeiraApp CasadoCódigo
8

## Página 15

CasadoCódigo Capítulo2. Projeto: nossaprimeiraApp
Visualizarseusdetalheseremovê-lasdesejado:
Prontoparacomeçar?
2.3 ViewControllerdecadastroderefeição
Vamoscriarumanovaaplicação. NoXcode,escolhemos“Criarumnovopro-
jeto”e,noWizardquesegue,escolhemos iOS, SingleViewApplication,
que seria uma aplicação de uma tela só. Aos poucos, evoluiremos a mesma
para mais telas. O nome do nosso projeto é
eggplant-brownie e a orga-
nização br.com.alura.
Escolhemos a linguagem swift e nosso alvo será oiPhone.At e l ad e
criaçãoficaentãocomoaseguir:
9

## Página 16

2.3. ViewControllerdecadastroderefeição CasadoCódigo
Logo de cara abriremos a nossa janela de criação de interface prin-
cipal: o storyboard (chamado Main.storyboard dentro da pasta
eggplant-brownie). Ao clicarmos nele, somos capazes de ver uma
janela quadrada que será a primeira tela de nossa aplicação: nosso
ViewController.O View Controller é chamado assim tanto por ser
responsávelpela Viewquantoporfazerocontroledoqueseráexecutadoao
interagirmoscomessa View.
Temalgodeestranhoaqui,nossatelaestáquasequadradaesabemosque
um iPhone não é quadrado. Vamos escolher oview controllerclicando no
quadrado e, em seguida, no botão amarelo que aparece no topo à esquerda
doquadrado:
10

## Página 17

CasadoCódigo Capítulo2. Projeto: nossaprimeiraApp
No lado direito, podemos navegar entre diversas propriedades do atual
elemento escolhido. Na aba Attributes, temos uma seção chamada
Simulated Metrics onde alteramos a opçãosize, escolhendo iPhone
4-inch. Agora sim temos um tamanho compatível com umiPhone de
4polegadas.
Desejamosadicionarduasmensagensdetextoedoiscamposdetexto,um
11

## Página 18

2.3. ViewControllerdecadastroderefeição CasadoCódigo
p a r aon o m ed ac o m i d a(name) e outro para o nível de felicidade com ela (
happiness). Primeiro, buscamos na barra de componentes (canto inferior
direito)umcampochamado Label:
Eagoraoarrastamosduasvezesparanosso ViewController.Or e s u l -
tadosãodois labelscomnomessemsentido:
12

## Página 19

CasadoCódigo Capítulo2. Projeto: nossaprimeiraApp
13

## Página 20

2.3. ViewControllerdecadastroderefeição CasadoCódigo
Precisamostrocarseusvalores. Afinal,umrepresentaráonomeeooutro
nosso nível de felicidade com aquela comida. Um duplo clique nolabel
permitealterarseuvalor. Mudemospara Namee Happiness:
14

## Página 21

CasadoCódigo Capítulo2. Projeto: nossaprimeiraApp
15

## Página 22

2.3. ViewControllerdecadastroderefeição CasadoCódigo
Adicionamosagoradoiscamposde Text Field damesmaforma, um
para Nameeumpara Happiness. Nomesmocantoinferiordireito,procu-
ramospor Text Field earrastamosoresultadoduasvezes.
Colocamos um botão, procurando pelo componente chamadoButton
e,assimcomocomoutroscomponentes,mudamosseutextopara add.
Oresultadodenosso storyboardéesse:
16

## Página 23

CasadoCódigo Capítulo2. Projeto: nossaprimeiraApp
17

## Página 24

2.3. ViewControllerdecadastroderefeição CasadoCódigo
Op r ó x i m op a s soér od a rn o s sop r o g r a m ae mu mi P h o n e .M a sc a l m al á ,
eunãotenhoumiPhone4,5,6etc.,atodoinstante. Queroprimeirovercomo
ficariaemumiPhonenomeucomputador,entãovamossimularumiPhone.
Para isso clicamos no botão
Play que fica no canto superior esquerdo da
janela.
PoderíamosrodaremoutroiPhone,reparequepodemostrocaromodelo
aqualquerinstantequedesejarmos. Porexemplo,aoescolherumiPhone5:
18

## Página 25

CasadoCódigo Capítulo2. Projeto: nossaprimeiraApp
Or esul tadoéateladenossop r ogramar odando:
19

## Página 26

2.3. ViewControllerdecadastroderefeição CasadoCódigo
Podemos diminuir o zoom do emulador escolhendo, na aplicaçãoiOS
Simulator,menu Window,submenu Scaleeaopçãoqueacharmosmais
adequada. Podemos também optar por mostrar o teclado em nosso emu-
lador no menu Hardware, submenu Keyboard e Toggle software
keyboard.
Emuladorousimulador?
Umemuladoremulatambémohardware,osimuladorutilizaohard-
ware da máquina onde está rodando (host). No nosso caso, estamos
usando um simulador, com o hardware de nossa máquina, portanto
nossa aplicação rodará em geral mais rápido do que em um iPhone de
verdade. Lembre-se sempre disso antes de colocar uma aplicação que
abusadeprocessamentodisponívelparaomundo: vocêquerrodá-laem
umemuladorouemseucelularantesparaconferirseudesempenho.
Ainda tem algo de estranho em nossa aplicação, o campo de felicidade
permite digitar texto. Não desejamos isso. Podemos parar o emulador cli-
candonobo tãode
stopnocantosuperioresquerdo.
20

## Página 27

CasadoCódigo Capítulo2. Projeto: nossaprimeiraApp
Aoselecionarmosumcampodetextocomoodefelicidade,notamosque
àdireita,naabadepropriedades,aofinaldasinformaçõespara Text Field ,
temosumao pçãoqueindicaoti podeteclado ,o Keyboard Type :
21

## Página 28

2.3. ViewControllerdecadastroderefeição CasadoCódigo
Vamos escolher o tipo chamado Number Pad . Escolhemos tam-
bém um texto padrão para ficar no fundo dos dois campos de texto,
um placeholder, que será dani’s cheesecake, guilherme’s
sundubu etc e 1 for sad, 5 for amazing .
22

## Página 29

CasadoCódigo Capítulo2. Projeto: nossaprimeiraApp
Rodamosnossoprogramaclicandonovamenteno Playe,agora,aocli-
carmos no campo de texto do número, podemos verificar que o teclado que
aparece é o teclado numérico, facilitando bastante a entrada de informações
pelousuáriofinal.
2.4 Boaprática:placeholderekeyboardtype
Formulárioscujaentradadedadosnãosejadodiaadiadousuáriofinalpo-
demdeixá-loperdido. Umformuláriodeloginétãocomumquenãoprecisa
de
placeholder eat e l afi c am a i sl i m p a .J áu mplaceholder em um
formuláriocomplexoqueousuáriovêpelaprimeiravezpodeajudá-loaen-
tenderqueti podevalo rop r ogramaesperadele.
Alémdo
placeholder,otipodetecladoajudaousuárioaodigitarda-
dosespecíficoscomoe-mails,númerosinteirosoudecimais.
Semprequeadicionarumcampodetextoemsuaaplicação,lembre-sede
configuraro placeholdereo keyboard type adequado.
Dica:cutuqueaspropriedades
Brinque com algumas propriedades de fonte de seu componente
Label. Mas lembre-se: é raro que uma aplicação com muitos estilos
defontesejalembradaporessefator. Evitemuitasvariaçõesdefonteem
suaaplicação. Nãocrie100estilosdiferentespara3telas.
23

## Página 30

2.5. Conectandoainterfaceaocódigo CasadoCódigo
Dica:salvandoseusarquivos
N o t eq u et o d av e zq u er o d a m o sn o s s op r o g r a m ee l eés a l v oa u t o m a -
ticamente. Paraperceberseseuarquivonãoestásalvo,vocêverificaque
onomedeleestáemnegritoouseuíconeestáescurecido:
2.5 Conectandoainterfaceaocódigo
Mas o que acontece quando clicamos no botão add? Desejamos exe-
cutar algum código ao clicar neste botão. Para isso, abrimos o arquivo
ViewController.swift, onde definiremos uma função em Swift. Clica-
mosnono medoar quivonabarraesquer da:
24

## Página 31

CasadoCódigo Capítulo2. Projeto: nossaprimeiraApp
Quem é ele? Prazer, nossoViewController,q u ej áv e mu mc o m p o r -
tamentomínimo:
import UIKit
class ViewController: UIViewController {
override func viewDidLoad() {
super.viewDidLoad()
// Do any additional setup after loading the view,
// typically from a nib.
}
override func didReceiveMemoryWarning() {
super.didReceiveMemoryWarning()
// Dispose of any resources that can be recreated.
}
}
Os dois métodos que a IDE adicionou são opcionais, portanto os remo-
vemosparaficarmosco mnosso ViewControllerpuro:
import UIKit
class ViewController: UIViewController {
25

## Página 32

2.5. Conectandoainterfaceaocódigo CasadoCódigo
}
O básico da linguagem aqui é que um ViewController herda de
UIViewController. Sóisso! Oquequeremoséadicionarumafunçãoque
seráinvocadaquandoobotão add sejaclicado. Nadamaisnaturalquedefi-
nirmos nossa função comoadd. Toda vez que o botão for clicado, a função
poderáserchamada.
import UIKit
class ViewController: UIViewController {
func add() {
}
}
Queremosqueessafunçãosejainvocadatodavezqueaconteceralgocom
nossa interface com o usuário. Isto é, gostaríamos que essa função fosse
um listener dos eventos da nossaview. Portanto, nós o anotamos de modo
a dizer ao Interface Builder (IB) que este método de nossa classe de
ViewController é uma ação (Action) que será informada pela tela. O
métodoéanotadocomo @IBAction:
@IBAction func add() {
}
Paratestarnosso callback,adicionamosumaimpressãoaolog:
@IBAction func add() {
println("button pressed!")
}
O log ficará na parte de baixo da tela, e aparecerá automaticamente ao
imprimirmosalgo,oupodemosmostrá-loacessandoomenu View,submenu
Debug Area ,o pção Hide/Show Debug Area .
26

## Página 33

CasadoCódigo Capítulo2. Projeto: nossaprimeiraApp
Esses3botões(osdebaixoparaYosemiteemaisrecente,osdecimapara
maisantigos)queseencontramnocantosuperiordireitodajaneladoXcode
servemparaesconderdiferentesbarrasdaaplicação:abarradenavegaçãonos
arquivos do projeto (
Navigator, Command+1 para mostrar, Command+0
paraesconder),abarradepropriedades( Utilities)eaba rraq uem os tra
o console e o debug embaixo (Debug). Utilize a cada instante o modo que
fo rmaisagradá velparaatar efaqueestáefetuando .
Rodamosoprograma,comosempre,clicandoem Play,e,naaplicação,
clicamosnobotão add,masnossolognaIDEnãomostranada:
27

## Página 34

2.5. Conectandoainterfaceaocódigo CasadoCódigo
C l a r o ,n ó sa i n d an ã oc o n e c t a m o sob o t ã oadd com nossa função. Po-
demos fazer isso de diversas maneiras e a primeira que veremos aqui é feita
arrastandoocódigoparaobotãovisualmente. Mascomoarrastaralgovisual
paraocódigoseaIDEmostraso men teumaco isapo rvez?
No topo, à direita do Xcode, ao lado dos ícones para exibir/esconder as
barras,conseguimosmodificaramaneiradevisualizarnossaáreadetrabalho.
Oprimeirobotãoativaavisualizaçãot radicionalqueutilizamosatéagora. O
segundoativaavisualizaçãoquepermiteabrirdoiseditoresaomesmotempo
eénelaquecostumamostrabalharenquantodesenvolvemosapartevisualde
nossasapps. Vamosclicarnessebotão.
Abrimos o storyboard clicando na barra à esquerda e clicamos no nosso
ViewControllerdentrodele. Automaticamenteoassistente(apartedadi-
reita)abreocódigo-fontedocontroller:
28

## Página 35

CasadoCódigo Capítulo2. Projeto: nossaprimeiraApp
Note a bola vazia ao lado de nosso@IBAction. É ela que arrastamos
paraconectaraobotão add:
29

## Página 36

2.5. Conectandoainterfaceaocódigo CasadoCódigo
Testamos nossa aplicação e, ao clicarmos no botão, o log indica que o
eventoocorreu. Sucesso:
DevoltaaoXcode,aoselecionarmosobotão add,podemosverificarna
última aba de propriedades (Connections Inspector - último ícone à
direita)queaação Touch Up Inside invocaránossafunção.
30

## Página 37

CasadoCódigo Capítulo2. Projeto: nossaprimeiraApp
Poderíamos acessar esta listagem de eventos (Sent Events ) e puxar
qualquer um dos eventos para uma função decallback que definimos. No
entanto,nãonecessitamosdemaisnenhumaagora.
Nmaneiras:omesmoresultado
Essas são só duas das maneiras de trabalhar com o Xcode para criar
uma @IBAction, e existem outras que veremos. Mesmo que no final
todastenhamomesmoresultado,tenta remosmostrardiversasdelaspara
quevocêpossaescolheraquelaemquesentirmaispráticadeacordocom
oquevocêtememmãosabertoemsuatelanaqueleinstante-oudequais
configuraçõesdesejafazeraocriaruma
IBActionousimilares.
Chegou a hora de ler os dados dos dois campos,Name e Happiness.
Dentro de nossa função, vamos imprimir os dois, primeiro declarando duas
Stringseconcatenando-asduranteaimpressão:
@IBAction func add() {
var name : String = "guilherme’s sundubu";
var happiness : String = "5";
println("eaten: \(name) \(happiness)!");
}
31

## Página 38

2.6. Conectandovariáveismembroàsuapartevisual: @IBOutlet CasadoCódigo
N o t eq u ee mS w i fto; é opcional, ele só é obrigatório quando desejar
utilizarduasexpressõesnamesmalinha,portantopodemosremoveros ;:
@IBAction func add() {
var name : String = "guilherme’s sundubu"
var happiness : String = "5"
println("eaten: \(name) \(happiness)!")
}
Como já estamos inicializando as variáveis no mesmo instante de suas
declarações,nãoprecisamosdeclararseustipos,elastêmseustiposinferidos
diretonainicialização:
@IBAction func add() {
var name = "guilherme’s sundubu"
var happiness = "5"
println("eaten: \(name) \(happiness)!")
}
Além disso, tanto o nome quanto a felicidade não mudam de valor, de
modoquepodemosdeclará-lascomoreferênciasimutáveis,ouseja,constan-
tes. Podemosfazerissoutilizandoapalavrareservada let:
@IBAction func add() {
let name = "guilherme’s sundubu"
let happiness = "5"
println("eaten: \(name) \(happiness)!")
}
2.6 Conectando variáveis membro à sua parte
visual:@IBOutlet
Voltandoaocódigo,nãoqueremosvaloresarbitrárioscomo“guilherme’ssun-
dubu” ou “5”. Desejamos ler o valor de nossos campos de texto. Como fazer
isso? Da mesma maneira como conectamos uma função a um elemento vi-
sual, podemos conectar um elemento visual por inteiro a uma variável. No
nossocaso,queremosrepresentarum
UITextField,portantonossavariá-
velserádestetipo:
32

## Página 39

CasadoCódigo Capítulo2. Projeto: nossaprimeiraApp
var nameField: UITextField
var happinessField: UITextField
Cuidado, pois não declaramos essas variáveis como locais à função! As-
sim como a função, elas são membros de nossa classe, membros de nosso
ViewController:
import UIKit
class ViewController: UIViewController {
var nameField: UITextField
var happinessField: UITextField
@IBAction func add() {
let name = "guilherme’s sundubu"
let happiness = "5"
println("eaten: \(name) \(happiness)!")
}
}
Mas,nahoraemqueaadicionamos,aIDEindicaerros. Aoclicarmosno
íconevermelhoquerepresentaumerronabarraàesquerda,vemosamensa-
gemdequea Class ViewController has no initializers :
33

## Página 40

2.6. Conectandovariáveismembroàsuapartevisual: @IBOutlet CasadoCódigo
Issoocorrepoistodavariávelmembrodeveserinicializadaoudeclarada
comoopcional.
Errosdecompilação
InfelizmenteoparserecompiladordalinguagemSwiftpodeserper-
der em seu código com uma certa facilidade. Caso o Xcode não mostre
oerromencionado,tenterodarsuaaplicação,nesseinstanteécertoque
eletentarácompilarseucódigoeencontraráoerro. Semprequeerapara
terumerrodecompilaçãoeoXcodenãomostrarparavocê,tenterodar
suaaplicação,forçandoacompilação.
Colocamoso !aofinaldadeclaraçãoparaindicarqueelaéopcionalpara
acriaçãodeum ViewController.
var nameField: UITextField!
var happinessField: UITextField!
Cuidado:opcionaiscom!
Cuidado: uma variável declarada opcional com! que tenha valor
nuloesejaacessadapodecrashearsuaaplicação. Veremosoutramaneira
de declarar e acessar variáveis opcionais, além de vantagens e desvanta-
gensdecadaabordagemnodecorrerdoconteúdoaquiapresentado.
Nãodesejamosprogramardequalquerjeitoeumadasprincipaisboas
práticasqueveremosdiversasvezesestaráligadaaousoadequadodeva-
lores opcionais para evitar erros em nossa aplicação. Não pretendemos
ensinardequalquermaneiraautilizaçãode
! nemmesmoincentivaro
uso indiscriminado do mesmo: seremos bem críticos em relação a ele.
Por enquanto, adotamos o
! na declaração de nossas variáveis para in-
dicaraocompiladorqueavariáveléopcionalmasnós,desenvolvedores,
sabemosqueelatemvalor(ecorremosorisco).
Damesmamaneiracomofizemoscomnossaação,devemosanotarnos-
sas variáveis. Desta vez, nós as anotamos como@IBOutletsep u x a m o sa
34

## Página 41

CasadoCódigo Capítulo2. Projeto: nossaprimeiraApp
bola vazia ao lado da variávelname para nosso campo name na interface
visual:
Agora,dentrodenossafunçãodeadicionarumanovarefeição,podemos
pegarovalordenossoscampos. Emcadaumdeles,utilizamosapropriedade
textparaextrairseusvalores:
import UIKit
class ViewController: UIViewController {
@IBOutlet var nameField: UITextField!
@IBOutlet var happinessField: UITextField!
@IBAction func add() {
let name = nameField.text
let happiness = happinessField.text
println("eaten: \(name) \(happiness)!")
}
35

## Página 42

2.6. Conectandovariáveismembroàsuapartevisual: @IBOutlet CasadoCódigo
}
Aoclicarmosnobotão,vemosoresultadonologcomosvaloresqueen-
tramosnoscampos. Éoqueesperávamos!
36

## Página 43

CasadoCódigo Capítulo2. Projeto: nossaprimeiraApp
Açõesconectadas
Preste sempre atenção ao desenho dos círculos (as bolinhas) ao lado
desuasações. Seumcírculoestiverpreenchido,eleestáconectadoaalgo.
Seeleestivervazio,entãoestádesconectado. Sevocêrenomearométodo,
e l es ed e s c o n e c t a r áp o i sac o n e x ã oéf e i t av i aon o m ed om é t o d o .T o m e
cuidado sempre que renomear métodos ou atributos anotados. Tenha
cuidadotambémemcopiar/colarcomponentesconectadospoisacone-
xão também é copiada. Caso seja necessário renomear ou copiar/colar
um item já conectado, lembre-se de desfazer a conexão efetuada anteri-
ormente,poisoXcodeacusaráumerro:
Sevocêrodaraaplicaçãocomumaconexãomalfeita,elapodedesde
(semquerer)funcionardemaneirainesperadacomoparar.
37

## Página 44

2.7. Resumo CasadoCódigo
Nomedoscampos
Existeumpadrãocomumemdesenvolvimentodeinterfacesdepro-
gramasdesktopbaseadonanotaçãohúngara,ondetentamosindicarno
nomedavariávelqualoseutipo.
Um combo box para representar o gênero de um usuário poderia se
chamar cbGender, enquanto o campo de texto com seu nome seria o
txtName. Esse padrão não é seguido como regra geral no desenvolvi-
mento de aplicações iOS. Outro padrão comum é utilizarfield como
prefixo ou sufixo. Aqui adotamosfield como sufixo, assim como é
f e i t on on o m ed a sc l a s s e s(Controller, Delegate etc) nas APIs do
iOS.
2.7 Resumo
Somos capazes de criar uma interface mínima com nosso usuário, além de
recebervaloresetermétodosinvocadosquandodeterminadoseventosocor-
rem.
Aprendemos um pouco da linguagem Swift: sabemos criar uma classe,
variáveislocaisemembros,alémdadefiniçãodeconstantes. Vimostambém
que a linguagem é
type safe inclusive em relação à não inicialização de
variáveis: fomos obrigados a utilizar o! para dizer que sabemos que essa
variáveléopcionaleteráumvalorválidoemexecução.
Aprendemos também a usar nossa IDE para navegar no projeto e cons-
truir nossa interface, que foi rodada em um simulador do iPhone. Somos
capazesdetestá-laemdiversasversõesdeiPhones.
Duranteessecaminhotodoconseguim osperceberalgumasboaspráticas
de desenvolvimento de software em geral, tanto em relação à utilização de
constantesquandocabívelquantoemrelaçãoàinterfacequeoferecemospara
nossousuáriofinal.
Nosso próximo passo é aprender mais dessa linguagem para podermos
modelar nossas classes que representarão uma refeição (
Meal)eu mi t e m
contidonela( Item).
38

## Página 45

Capítulo3
Swift: alinguagem
Veremosaquiabasedalinguagemqueserásuficienteparacriarmosumaapli-
caçãoutilizandodiversasboaspráticasdeprogramação. Nãonosviciaremos
comousodesnecessáriodevariáveisglobaiseoutrasmáspráticasquedificul-
tamamanutençãodocódigoaolongoprazo. Paraissoutilizaremosdiversos
padrões,alémdobásicodeOrientaçãoaObjetos.
NossofoconãoéensinarOrientaçãoaObjetos(OO)avançadaaqui,mas
quantomaiorsuabaseemboaspráticasdeOOdeoutraslinguagens,melhor
poderá tomar cuidados importantes em Swift. Diversos deles serão citados
poraqui.
3.1 Brincandonoplayground
Criamosprimeiroumplayground,ondepoderemostestardiversasfunciona-
lidades. NajaneladoXcode,
Command+Neescolhemos iOS, playground,

## Página 46

3.1. Brincandonoplayground CasadoCódigo
deixamos o nome MyPlayground.playground e temos o playground
pronto! Naesquerda,escrevemosocódigo,nadireitavemososeuresultado:
N o t eq u eop la y gr o u n dn ã of a zpa rt ed ose up r o je t oe ms i ,so m e n t ed ev e
ser usado para testes rápidos, queéon o s s oc a s o .V a m o su t ilizá-lo para en-
tendermosmelhordiversosconceitosdalinguagem.
Primeiro, testaremos algumas coisas que já conhecemos. Removemos o
códigodoplaygroundatualecriamosuma Stringimprimindo-a:
var name = "Guilherme"
name = "Guilherme Silveira"
println(name)
Nadireita,temososresultadosdenossasexecuções:
40

## Página 47

CasadoCódigo Capítulo3. Swift: alinguagem
Da mesma forma como usamos um editor com assistência para arras-
tar nossos IBOutletse IBAction, o playground oferece um assistente
chamado Timeline. Ele pode ser ativado clicando naquele ícone que usa-
m o sp a r aa b r i roe d i t o rp a r aa r r a s t a ra sa ç õ e so un om e n uView, submenu
Assistant Editor ,o p ç ã oShow Assistant Editor . Na saída dele,
vemosoresultadodenossasinformaçõesdelog:
Comovimosantes,emSwift,o ;nofimdeumainstruçãoéopcional,ele
sóéob riga tó rioquandod uasinstruçõesficamnamesmalinha:
var name = "Guilherme"
name = "Guilherme Silveira"; println(name)
Podemos também criar uma constante. Se tentarmos atribuir um novo
valoràconstante,ocompiladormostraumamensagemdeerro:
let project = "Eggplant Brownie"
project = "Zucchini Muffin"
41

## Página 48

3.1. Brincandonoplayground CasadoCódigo
Boaprática:constantes
Utilizar constantes (em Swift,let), quando cabível, é considerado
uma boa prática em programação em geral, ao invés de referências mu-
táveis (em Swift,var). Isso pois, uma vez definida, a variável continua
com o mesmo valor até “deixar de existir” (oficialmente, ser desreferen-
ciada). Não existe nenhuma complexidade ligada à troca de referências.
Como vimos, uma constante define uma conexão imutável entre seu
nome e o valor passado durante sua inicialização. Não há preocupação de
elatersidoalteradaantesdeacessá-laemqualquerpontodeseuprograma.
E se desejamos comentar alguma linha no nosso código? O comentário
tradicionaléo
//quecomentaorestodalinha:
// too complex code need a one line comment
let project = "too complex, so it requires a comment"
O u t r ao p ç ã os e r i au s a ro/* ... */ , que permite o comentário em
diversaslinhas.
/*
nuclear devices code might need
multiple line comments
*/
let device = "nuclear"
O /* ... */ pode ser usado também para comentar algo no meio da
linha:
42

## Página 49

CasadoCódigo Capítulo3. Swift: alinguagem
let universe /* needs a middle comment to explain */ = "big"
Codesmell:comentários
Emgeral, quandoprecisamoscomentaralgo, ésinaldequeocódigo
está complexo e o próximo desenvolvedor sofrerá para entendê-lo. Se o
desenvolvedorsofre,achancedesurgiremnovoserrosporumamudança
indevida é grande. Isto é, a necessidade do comentário está indicando
queocódigoqueescrevemosestádeclaradodedeterminadamaneiraque
nãopareceserfácildemanter.
Sendoassim,esse
code smell podeserusadocomoumsinalpara
alterarmos nosso código. Temos como arsenal de refatoração diversas
ações, como extrair variáveis, métodos, renomear ambos etc. Deixar
nosso código claro o suficiente para o próximo desenvolvedor pode di-
minuirachancedefuturosbugsseremintroduzidosemnossaaplicação.
Vamosaplicaradeclaraçãodevariáveisaonossodomínio,derefeiçõese
itens. Podemosapagartodoonossoplayground.
Primeiro, precisaremos representar uma refeição. Em inglês, uma refei-
çãoserárepresentadaporum meal,eelatemtantoonomequedemospara
a refeição daquele dia (String), quanto nossa nota, que será representada
comumnúmerointeiro( Int):
let name = "Dani’s paradise"
let happiness = 5 // Int
Representaremosumarefeiçãoporumconjuntodealimentos,comouma
sopa de abóbora ou seu brownie de berinjela, com poucas calorias. Para re-
presentarascalorias,usaremosumnúmerodecimal,umnúmerocomponto
flutuante:
let name = "eggplant brownie"
let calories = 50.5 // Double
43

## Página 50

3.1. Brincandonoplayground CasadoCódigo
Masreparequeocódigonãocompilarásevocêmantiveroexemploante-
rior:duasvariáveisnãopodemteromesmonome( name)nomesmoescopo.
Nestecapítulo,antesdecadaexemplo,lembre-sedeapagaroucomentarocó-
digoanteriorantesdecontinuar.
Além desses tipos, será recorrente o uso de variáveis do tipotrue ou
false,ostiposbooleanos:
let eggplantBrownieIsVeggie = true
let eggplantBrownieTastesAsChocolate = false
VariáveisbooleanasemSwiftsãodotipo Bool,portantoumadeclaração
comtipagemexplícitaseria:
let eggplantBrownieIsVeggie:Bool = true
let eggplantBrownieTastesAsChocolate:Bool = false
Tiposbásicos
Existem, claro, diversos outros tipos para utilizarmos, mas o básico
quecobreamaiorpartedoscasossãoosapresentadosatéaqui: Double,
Bool, Int e String. Além desses, já vimos e continuaremos vendo
outrasclassesqueserãoutilizadasemnossoprojeto.
Há desde tipos numéricos só de valores positivos até classes que
permitem o acesso ao disco. Você pode consultar a documentação da
Apple para conhecer mais sobre as classes que deseja emhttp://bit.ly/
swift-linguagem-guiadereferencia
Podemosdefinirfunçõesnovas,comousode func,einvocá-las:
func helloCalories() {
println("hello calories!")
}
helloCalories()
Note que o resultado aparece como a impressão da linha onde fizemos
o println, e não da linha onde invocamos nosso método. Isso porque o
44

## Página 51

CasadoCódigo Capítulo3. Swift: alinguagem
playgroundestáquerendonosmostraroqueaconteceucomcadalinhade
códigoquandoelasforamexecutadas.
Vamostentarinvocarduasvezesomesmométodoeimprimiroutrovalor
nomeio:
func helloCalories() {
println("hello calories!")
}
helloCalories()
println("oi tudo bem")
helloCalories()
Observeque,noresultadoquetemosagora,essalinhafoiexecutadaduas
vezes.
45

## Página 52

3.1. Brincandonoplayground CasadoCódigo
Por mais que essa visualização nos ajude bastante para entender o resul-
tado de execução de cada linha isoladamente, talvez seja interessante ver o
resultado à medida que o código foi executado, ou seja, a saída que foi jo-
gada com
println à medida que o tempo foi passando, umatimeline.É
exa tamen teissoqueoassisten teTimelinequevimosanteriormentefaz.
Ao exibi-lo, temos o resultado em ordem doTimeline. Se seu Xcode
nãomostrá-lonomodoassistente,cliqueondeestáescrito Timelinecomo
naimagemaseguireselecione-o:
46

## Página 53

CasadoCódigo Capítulo3. Swift: alinguagem
Bugdoassistant
Caso o assistente não mostre um console vazio, nem mostre o resul-
tado das invocações, você pode voltar ao modo normal e novamente ao
assistente. Emalgumasversões,oXcodepossuiumbugquefazcomque,
na primeira vez que mudamos para o
Timeline, ele mostre o console
vazio.
Tambémpodemosclicarnoíconecircularàesquerdadoplayground,que
seassemelhaaosímbolode +quandopassamosomouseporcimadele:
O resultado é que logo abaixo do console conseguimos ver a saída so-
mentedestalinha:
47

## Página 54

3.2. Arrays CasadoCódigo
As funções podemreceber parâmetros, como o nome eo número deca-
loriasaoadicionarumnovoitemaumarefeição. Quandoosrecebemos,de-
vemosdizerquaisostiposdessesparâmetros:
func add(name: String, calories: Double) {
println("adding \(name) \(calories)")
}
add("Eggplant", 50.5)
3.2 Arrays
Atéagoraestamostrabalhandocomtudoemumaúnicaunidade. Nãopode-
mosterduasvariáveiscomomesmonomenomesmoescopo. Comoacumu-
lar diversos produtos? Diversos elementos do mesmo tipo? Queremos criar
umarray. Podemoscriarumarraydecalorias,porexemplo:
let calories = [50.5, 100, 300, 500]
Poderíamosopcionalmentedeclararotipodoarrayexplicitamente:
let calories:Array<Int> = [ 50.5, 100, 300, 500]
Opa,nãocompila. Claro,umdosvaloresé double,portantoéumarray
dedoubles:
48

## Página 55

CasadoCódigo Capítulo3. Swift: alinguagem
let calories:Array<Double > = [ 50.5, 100, 300, 500]
Somente se o array fosse vazio seria interessante indicar o tipo de array
quequeremos:
let items:Array<Double >=[]/ /D o ubles
A g o r aq u et e n h ou ma r r a yd ec a l o r i a s ,c o mtipagemimplícita, gostaria
de passar por todos os seus itens para somá-los. Como fazer isso? Fazemos
um forde0até4(onúmerodeelementos,exclusive):
let calories = [ 50.5, 100, 300, 500]
f o rv a ri=0 ;i<4 ;i + +{
println(calories[i])
}
Podemos utilizar a propriedadecount de um Array para fazer esse
laço:
let calories = [ 50.5, 100, 300, 500]
for var i = 0; i < calories.count; i++ {
println(calories[i])
}
Quandonosso foréespecíficodesomarumemumonúmerodoíndice,
podemosusaroa talhoquepassaen tr eo0eo3,incl usive:
let calories = [ 50.5, 100, 300, 500]
for i in 0...3 {
println(calories[i])
}
Se utilizarmos calories.count, temos que tomar cuidado. Esse va-
lor será 4 e teremos um erro, afinal estaríamos iterando da posição 0 a 4 (5
elementos). Queremos,portanto, calories.count - 1 :
let calories = [ 50.5, 100, 300, 500]
for i in 0...(calories.count - 1) {
println(calories[i])
}
49

## Página 56

3.2. Arrays CasadoCódigo
Quecódigofeio! Mesmoextraindoumavariávelaindanãopareceserum
códigoidealemnossasituação:
let calories = [ 50.5, 100, 300, 500]
let total = calories.count - 1
for i in 0...total {
println(calories[i])
}
Quando desejamos passar por todos os elementos de umArray, pode-
mosutilizaro for in :
let calories = [ 50.5, 100, 300, 500]
for c in calories {
println(c)
}
Porfim,umafunçãopoderetornaralgo,comoototaldecaloriascontidas
emum Arraydecalorias:
func allCalories(calories: Array<Double>) {
var total = 0
for c in calories {
total += c
}
return total
}
allCalories([ 10.5, 100, 300, 500])
Mas precisamos dizer qual o retorno da função. Como ela devolve um
Double,será -> Double :
func allCalories(calories: Array<Double>) -> Double {
var total = 0
for c in calories {
total += c
}
return total
}
50

## Página 57

CasadoCódigo Capítulo3. Swift: alinguagem
allCalories([ 10.5, 100, 300, 500])
Contudo, ainda tem algo de errado. O que não compila nesse código? A
variável totaléimplicitamenteum Intesomosavisadosdisso. Mudamos
en tãoparaum Double:
func allCalories(calories: Array<Double>) -> Double {
var total = 0.0
for c in calories {
total += c
}
return total
}
allCalories([ 10.5, 100, 300, 500])
Oudefinimosatipagemexplícita:
func allCalories(calories: Array<Double>) -> Double {
var total:Double = 0
for c in calories {
total += c
}
return total
}
allCalories([ 10.5, 100, 300, 500])
Por fim, quando invocamos uma função que retorna algo, podemos uti-
lizarseuretornodiretamenteouaplicá-loaumavariável:
func allCalories(calories: Array<Double>) -> Double {
var total:Double = 0
for c in calories {
total += c
}
return total
}
51

## Página 58

3.3. Boaprática: cuidadocominferênciadetipos CasadoCódigo
let totalCalories = allCalories([ 10.5, 100, 300, 500])
println(totalCalories)
3.3 Boaprática: cuidadocominferênciadeti-
pos
Éprecisotomarcuidadocomainferênciaautomáticadetipos. Umproblema
clássico ocorre quando dividimos doisIntseor e s u l t a d ofi n a léu mInt
sem percebermos, achando que estamos dividindoDoubles. Preste muita
atenção ao usar a inferência, ela ajuda a digitar menos, mas exige mais na
horadeutilizá-la.
var values = [ 1, 2]
var total = 0
for v in values {
total += v
}
println(total / values.count) // 1? 1.5?
Tome muito cuidado com tipos implícitos. Digitar menos é bom. Mas o
maisimportanteéquenossoprogramafuncione.
PareceserporessemotivoqueSwiftreforçaotipoderetornoaoinvocar
ummétodo. EnquantoemScala,umalinguagemmuitoparecidaemdiversos
pontos com Swift, o retorno pode ser implícito, em Swift ele não pode. O
código a seguir não compila pois a função não indicou qual tipo ela retorna.
Elapoderiainferir
Int:
func number() {
return 15 // compilation error
}
var values = [ number(), number()]
Comoalinguagemnãoinfere,precisamosdeclararotipoderetorno.
func number() -> Int {
return 15
52

## Página 59

CasadoCódigo Capítulo3. Swift: alinguagem
}
var values = [ number(), number()]
3.4 Resumo
Neste capítulo, vimos como criar um playground e utilizá-lo para testar ca-
racterísticasdalinguagemouexecutarpequenostrechosdecódigoSwift.
Vimoscomoalinguagemcuidadadeclaraçãoeinicializaçãodevariáveis,
comoelaseviracomatipagemimplícit aeocuidadoquedevemostomarcom
ela.
Criamosfunçõesquerecebemargumentos,quedevolvemvaloresetraba-
lhamos com Int, Double, Bool e Strings. Fizemos algumas operações
aritméticaseutilizamosolaçodotipo forparaiterarporelementos.
Apesar de não termos utilizado aqui, oif, while e outros, eles se as-
semelham em muito a outras linguagens comoJava, C e C#. Alguns deles
veremosnestematerial,outrossãodesimplesaprendizadoedefácilconsulta
noguiadereferênciadalinguagem.
53

## Página 61

Capítulo4
Swift: mapeandonossosmodelos
ein tr od uçãoàOrien taçãoa
Objetos
4.1 Boaprática:organizandoosdados
Toda vez que tenho uma refeição, devo trabalhar com duas variáveis (nome,
felicidade)eumarray? Seumafunçãodesejapassarumarefeiçãoparaoutra
função,devepassaressestrêsargumentos? Todavez?
Etodafunçãoquedependedeumarefeiçãodeveficarjogadapeloscantos
do nosso programa? O cálculo de calorias total, o cálculo de felicidade por
caloria? Cadacoisajogadaemumcanto?
Orientação a Objetos apresenta uma solução para esses problemas ao

## Página 62

4.1. Boaprática: organizandoosdados CasadoCódigo
agrupar os dados e comportamentos ligados em um único lugar, uma única
classe.
Swiftoferecetambémcaracterísticasdeumalinguagemorientadaaobje-
tos. Para agruparmos todos os atributos que uma refeição possui, junto com
oscomportamentosqueelapodeter ,criamosumaclasse.Aclasseéaabstra-
çãodeumarefeição. Atributosdarefeiçãoseriamonome,afelicidadeeseus
itens. Já comportamentos (métodos) da classe seriam o cálculo de calorias
totais,defelicidadeporcaloriaetc.
V amoslim partodonossopla ygr o undecolocaraclasse
Meal:
class Meal {
}
Boaprática:parasabermaisdeOrientaçãoaObjetos
VocêpodeconhecermaisdeOrientaçãoaObjetosestudandoocon-
ceitocomaapostiladaCaelum,disponívelonlineemseusite.
O blog da Caelum também oferece diversos artigos sobre o assunto,
comooartigoquemostracomoevitarsequênciasde ifsemOrientação
aObjetos: http://bit.ly/como-nao-aprender-oo
Portanto,nonossocaso,todarefeiçãoteráumnomeeumníveldefelici-
dade,osquaischamamosemSwiftdepropriedadesarmazenadas:
class Meal {
var name = "Eggplant Brownie"
var happiness = 5
}
Podemos agora criar uma refeição, acessar e alterar seus valores. Para
criá-la,usamosseuconstrutor,seu inicializador,queseassemelhaàchamada
deumafunção(oumétodo)comonomeigualaodotipodaclasse:
let brownie = Meal()
println(brownie.name)
56

## Página 63

CasadoCódigo Capítulo4. Swift: mapeandonossosmodeloseintroduçãoàOrientação...
println(brownie.happiness)
brownie.happiness = 3
println(brownie.happiness)
Oqueestamosfazendoaquiédefinindoumavariávelchamada brownie
quereferenciaumobjeto. Ele“aponta”,referenciaoobjetoqueestácriadona
memória.
Noteque,apesarde brownieserumaconstante,podemostrocarosva-
lores dentro do objeto. Como os valores foram declarados comovars, eles
puderam ser alterados; é a referência ao objeto que não pode ser trocada. O
código a seguir tenta alterar nossa referência de uma constante, apontando
agoraparaumanovarefeição,efalha:
let brownie = Meal()
println(brownie.name)
println(brownie.happiness)
brownie.happiness = 3
println(brownie.happiness)
brownie = Meal() // error!
Nessecaso,oquefizemosfoipegaraquelavariávelquereferenciaumob-
jeto,efazê-lapassarareferenciar(apontar)paraoutroobjeto. Agoraninguém
57

## Página 64

4.1. Boaprática: organizandoosdados CasadoCódigo
maisreferenciaoprimeiroobjetoquecriamos.
Mas, claro, nem toda refeição será um brownie de berinjela. Não parece
fazer sentido que, toda vez que criarmos um objeto do tipoMeal, ele ve-
nhaautomaticamentepreenchidocomotalbrownie. Vamosremoverovalor
inicialeverificaroqueacontece... temostrêserrosemnossaclasse!
class Meal {
var name
var happiness
}
Para vermos os erros que aconteceram, podemos clicar na exclamação
vermelhaqueficaàesquerdadalinhaqueocorreu. Alinhainteiraficaráver-
melha:
Dois destes erros são fáceis de resolver: antes o compilador sabia o tipo
dasvariáveis,poisinferiaosmesmosatravésdesuasinicializações,entãoadi-
cionamosastipagensexplícitas:
class Meal {
var name: String
var happiness: Int
}
Ficamos agora com um único erro, o compilador diz que a classeMeal
não possui um inicializador. O que está acontecendo? Lembre-se que, em
Swift, a não existência de valor (em geral, onull em outras linguagens) é
umcasoimportanteosuficienteparaterqueserdeclaradoporexplícito. Não
queremos erros do tipo do acesso a
null e mt e m pod ee x ecu çã o ,po ri s soa
58

## Página 65

CasadoCódigo Capítulo4. Swift: mapeandonossosmodeloseintroduçãoàOrientação...
linguagemcolocabarreirasparaevitaraexistênciadeles. Seodesenvolvedor
desejaraexistênciadeum null,eledeveserr espo nsá velpo rmar caraquele
cam poco motal,umcam poqueéopcional,quepodeterumvalornulo.
class Meal {
var name: String?
var happiness: Int?
}
Reparequeaimpressãodeumnomeedoníveldefelicidademostraagora
osvalores nil(o nullemSwift):
class Meal {
var name: String?
var happiness: Int?
}
let brownie = Meal()
println(brownie.name)
println(brownie.happiness)
Esecolocarmosumvalo rden tr odenossar efeição ,co moficaasaída?
let brownie = Meal()
brownie.name = "Eggplant brownie"
brownie.happiness = 3
println(brownie.name)
println(brownie.happiness)
59

## Página 66

4.1. Boaprática: organizandoosdados CasadoCódigo
Ele deixou claro que o que temos agora não é mais umaString ou um
Int, mas sim umOptional[String] ou um Optional[Int].Oq u e
o compilador faz é: se você deseja uma variável com valor opcional, marque
com o ?. Nesse caso, seu valor inicial énil e, ao colocar algo lá dentro, ele
passaavaler Optional(valor colocado) .
Observe que podemos deixar explícito o uso doOptional ao atribuir
valoraumavariávelopcional,comonocódigoaseguir:
var name:String?
name = Optional("Zucchini muffin")
Maspodemosdeixarimplícitaatransformaçãodeumvalorparaseutipo
Optional,co moem:
var name:String?
name = "Zucchini muffin"
As duas abordagens produzem o mesmo resultado para o compilador,
umavezque,apartirdomomentoqueavariávelfordeclaradacom String?,
elaserátratadadessaformaemambososcasos.
Temos algo de estranho ainda: não desejamos imprimir
Optional("Zucchini muffin") ,massimso men teono me,a String.
var name:String?
name = "Zucchini muffin"
println(name)
60

## Página 67

CasadoCódigo Capítulo4. Swift: mapeandonossosmodeloseintroduçãoàOrientação...
Piorainda,setentarmosimprimirotamanhodenossa Stringusandoa
função countElements,percebemosqueparaumadeclaraçãonormal,ela
funciona:
var name = "brownie"
println(countElements(name)) // 7
Masnãofuncionaparao Optional,afinalométodorecebe String,e
não String?:
var name:String?
name = "brownie"
println(countElements(name)) // error: type ’String?’
// does not conform to protocol
// ’_CollectionType’
Acontecequeum Optionalnãoédotipoquequeremos,desejamosex-
trairoqueestáládentro ,tantonahoradaimpressãoquantonomomentode
usaroconteúdodenossa String?.M asoco m p ilado rnãoébo bo ,e leq uer
nos ajudar e dizer: desenvolvedor, ao tentar usar essa variável, você tem na
verdadeum
Optional,temumriscoaí,talvezsejaalgo nil. Temcerteza?
Desenvolvedor,sevocêacessá-lasemverificarseéválida,écapazdeseupro-
grama parar completamente - pior ainda, ele com certeza vai parar caso seja
nilevocêchameummétododele.
Vamos dizer ao compilador que sabemos o que estamos fazendo. Nós
sabemos que o que está lá dentro é algo não nulo, e que assumimos o risco
utilizandoocaractere
!:
var name:String?
name = "brownie"
println(countElements(name!)) // 7
Perfeito, mas isso é arriscado, olhe o que acontece caso sejanil,oc a s o
queoco m p ilado rten to uatodocustoevi tar:
var name:String?
println(countElements(name!)) // fatal error
61

## Página 68

4.1. Boaprática: organizandoosdados CasadoCódigo
CuidadocombugsdocompiladordoXcode
Como Swift é uma linguagem nova, o compilador utilizado pelo
Xcode pode se confundir com algumas coisas. Nos exemplos feitos a
partir deste capítulo, tome cuidado: caso a mensagem de erro apareça
em uma linha diferente daquela esperada, teste o caso que está interes-
sado isoladamente. Fazer cada um dos testes de maneira isolada evita
deixarocompiladorperdido. Noplayground,issoocorremaisfrequen-
temente,umavezqueeleutilizainformaçõesdedebugparaimprimiros
resultadosdoladodireitodenossaIDE.
Nãoqueremosqueissoaconteça,portantoomaiscomuméverificarseo
campoénãonulo,esóentãoutilizá-lo:
if (name != nil) {
println(countElements(name!)) // 7
} else {
println("empty")
}
No Swift,osparêntesesdo if(edoslaços)éopcional,portantopode-
mosfazer:
if name != nil {
println(countElements(name!)) // 7
} else {
println("empty")
}
Comoestamosutilizandonossa Stringmaisdeumavezdentrodocó-
digo, podemos querer fugir do uso do! ao fazer o if ej ád e c l a r a ru m a
variávelcomovalorrealaomesmotempo:
var name:String?
if let n = name {
println(countElements(n)) // 7
} else {
62

## Página 69

CasadoCódigo Capítulo4. Swift: mapeandonossosmodeloseintroduçãoàOrientação...
println("empty")
}
Massejamossinceros. Nessecaso,nóstemoscertezadequeexisteumva-
lornanossa Stringe,apesardeadeclararmoscomoopcional,gostaríamos
de dizer ao compilador que temos certeza de que ela tem um valor válido,
usandoo !nadeclaraçãodavariável:
var name:String!
name = "Eggplant Brownie"
println(countElements(name)) // 7
Lembre-sedetomarmuitocuidadotodavezqueusaro !,sejaparaaces-
sar o valor de uma variável opcional, seja ao declarar uma variável opcional
quandovocêtemcertezadequeelaseráinicializada.
Se tentássemos usá-lo sem o valor inicializado, a responsabilidade seria
dop r ogramado reoerr oseriafa tal:
var name:String!
println(countElements(name)) // fatal error
E toda essa história de uma linguagem tratar um valor opcional (
Optional)comtantocarinho,comoficanoscasosdeinvocaçãodemétodos
queretornamvaloresopcionais? Vamosdefiniruma Stringcomovalor 5
etransfo rmá-laemum Int,qualotiporetornado?
let happiness = "5"
println(happiness.toInt())
O resultado é um Optional<Int>,a fi n a lp o d es e rq u ed êu me r r o
e o valor aí dentro de nossaString não seja um número. Repare que o
Optional pode ser usado como alternativa no retorno de um método para
dizerqueoprocessofoiumsucessoounão. Éum tradeoff queosimplemen-
tadoresdalinguagemescolheramnahoradeimplementarométodo toInt
da String.
63

## Página 70

4.2. Boaprática: Goodcitizen(evitenulos )eoinit CasadoCódigo
4.2 Boaprática: Goodcitizen(evitenulos)eo
init
Sempre que criamos uma refeição, precisamos de um nome e de um nível
de felicidade. Essas não são características opcionais. Diversas linguagens
orientadas a objeto favorecem e pregam a “boa prática” (ironia intencional)
de deixar tudo mutável através degettersesetters, propriedades ou qualquer
outronomedadoaumavariávelmembro(propriedade)queémutáveleini-
cializadacomzeroounulo.
Operigodeumavariávelnãoinicializadaésimples: vocêtemumobjeto
quepodenãoestarpreparadoparaterummétodochamado. Opadrão
Good
Citizen diz que todo objeto, assim que criado, deve estar pronto para ter
todos os seus métodos executados. Não existe “não invoque enquanto” ou
“invoquesomenteapós”. Comissoevitamos,porexemplo,osdiversos
null
pointers ou fatal errors que podemos tomar em nossas aplicações:
todososvaloresestãopreenchidos,nenhumestávazio!
Swift reforça isso com a utilização de variáveis opcionais explícitas: se
você quiser que ela seja opcional, deve explicitar, e deve também, quando
acessá-la,explicitarquesabeoqueestáfazendo. Sãodoispassosqueumde-
senvolvedorprecisatomarantesdefazerumabobagem.
Codesmell:comonãoaprenderOrientaçãoaObjetos:
GetterseSetters
O blog da Caelum possui um post de Paulo Silveira sobre como não
aprenderOrientaçãoaObjetos,eosproblemasdautilizaçãode getterse
setters:
http://bit.ly/encapsulamentoGetterSetter
4.3 NossoGoodCitizen
Devemos obrigar todos os programadores que desejam instanciarMeal a
passarosdoisargumentos. Éoquedefinimosnonossoinicializador,ocons-
trutor,ealteramosnossocódigoparagarantirisso,nãoqueremosopcionais!
64

## Página 71

CasadoCódigo Capítulo4. Swift: mapeandonossosmodeloseintroduçãoàOrientação...
class Meal {
var name:String?
var happiness:Int?
init(name: String, happiness: Int) {
}
}
Podemosinstanciaremostrarquenosso Mealsempretemvalor,enunca
aceita nil. Podemos ser felizes com umMeal, que ele nunca vai dar um
fatal error (ouequivalenteaum Null pointer ):
let brownie = Meal("Eggplant brownie", 5)
println(brownie.name)
println(brownie.happiness)
Masocompiladorreclama. Aoinicializarmosumobjetoduranteacons-
trução,éobrigatóriaapassagemdonomedosparâmetros,ficandoclarooque
éoquê:
let brownie = Meal(name: "Eggplant brownie", happiness: 5)
println(brownie.name)
println(brownie.happiness)
Mas se recebemos o nome e a felicidade no construtor, não precisamos
dosopcionais:
class Meal {
var name:String
var happiness:Int
init(name: String, happiness: Int) {
}
}
AgoraoXcodereclamadequenãoinicializamosasvariáveisquenãosão
opcionais. Desejamos ser um bom cidadão, e, se você possuir uma referên-
c i ap a r au mMeal, pode ter certeza de que tudo que está lá dentro está bem
configurado, com todos os valores preenchidos. Portanto, em nosso cons-
trutor, atribuímos os valores dos parâmetros para nossas propriedades. Para
65

## Página 72

4.3. NossoGoodCitizen CasadoCódigo
isso,referenciamosopróprioobjetoqueestásendoconstruído(ouquejáfoi
construído)atravésdareferência self:
class Meal {
var name:String
var happiness:Int
init(name: String, happiness: Int) {
self.name = name
self.happiness = happiness
}
}
Agora sim, nosso código compila e podemos ver que ele já tem valores
válidoslogoemsuainicialização. Podemostambémconferirqueaexecução
denossocódigonãopermi teapassagemden ulo:
let brownie = Meal(name: nil, happiness: 5) // compile error
Temos nosso Good Citizen ,u mo b j e t od oq u a l ,q u a n d ot e m o su m a
referência,temoscertezadequeduaspropriedadesestãobemdefinidasepo-
demosutilizá-lo.
Seguindoosmesmosprincípios,criamosnosso
Item:
class Item {
var name:String
var calories:Double
init(name: String, calories: Double) {
self.name = name
self.calories = calories
}
}
class Meal {
var name:String
var happiness:Int
init(name: String, happiness: Int) {
self.name = name
self.happiness = happiness
}
}
66

## Página 73

CasadoCódigo Capítulo4. Swift: mapeandonossosmodeloseintroduçãoàOrientação...
Mas queremos que nossa refeição possua diversos itens. Usemos, então,
umarraydeitens:
class Item {
var name:String
var calories:Double
init(name: String, calories: Double) {
self.name = name
self.calories = calories
}
}
class Meal {
var name:String
var happiness:Int
var items
init(name: String, happiness: Int) {
self.name = name
self.happiness = happiness
}
}
Masissonãofazsentido. Queremosqueavariável items sejaumarray
vaziodeitens:
class Item {
var name:String
var calories:Double
init(name: String, calories: Double) {
self.name = name
self.calories = calories
}
}
class Meal {
var name:String
var happiness:Int
var items = Array<Item>()
init(name: String, happiness: Int) {
67

## Página 74

4.3. NossoGoodCitizen CasadoCódigo
self.name = name
self.happiness = happiness
}
}
Alémdepropriedadeseconstrutores,umaclassepodetermétodos,como
umquenosajudeacalcularototaldecaloriasdeumarefeição:
class Item {
var name:String
var calories:Double
init(name: String, calories: Double) {
self.name = name
self.calories = calories
}
}
class Meal {
var name:String
var happiness:Int
var items = Array<Item>()
init(name: String, happiness: Int) {
self.name = name
self.happiness = happiness
}
func allCalories() -> Double {
var total = 0.0
for i in items {
total += i.calories
}
return total
}
}
Podemoscriaragoraumnovoitem:
let brownie = Meal(name: "Eggplant brownie", happiness: 5)
let item1 = Item(name: "brownie", calories: 115)
let item2 = Item(name: "vegan cream", calories: 40)
68

## Página 75

CasadoCódigo Capítulo4. Swift: mapeandonossosmodeloseintroduçãoàOrientação...
Mas queremos adicioná-los nos itens do brownie. Por isso, chamamos o
método append:
let brownie = Meal(name: "Eggplant brownie", happiness: 5)
let item1 = Item(name: "brownie", calories: 115)
let item2 = Item(name: "vegan cream", calories: 40)
brownie.items.append(item1)
brownie.items.append(item2)
Como as variáveis só foram utilizadas para invocar o métodoappend,
podemos invocá-lo direto, passando como parâmetro a referência ao objeto
queacabadeserinicializado:
let brownie = Meal(name: "Eggplant brownie", happiness: 5)
brownie.items.append(Item(name: "brownie", calories: 115))
brownie.items.append(Item(name: "vegan cream", calories: 40))
println(brownie.allCalories())
Oresultadodo printlné 155.0,comoesperado.
69

## Página 76

4.4. Codesmell(malcheirodecódigo): opcional! CasadoCódigo
Boaprática:encapsulamento
Encapsulamento é esconder como as coisas são feitas e permitir
acesso a uma interface que executa as tarefas pedidas. No nosso caso,
deixamos de acessar diretamente nossos itens e passamos a perguntar à
refeiçãoqualototaldecalorias.
Encapsular vai muito além de uma mera definição de método, de-
vemos controlar o escopo de acesso de nossas variáveis, métodos e até
mesmo classes e pacotes. Veremos outras características ligadas ao en-
capsulamento ao decorrer do material, e existe uma leitura abrangente
sobreotemanoblogdaCaelumem:
• http://bit.ly/revisitandoOO
• http://bit.ly/encapsulamentoScala
• http://bit.ly/encapsulamentoGetterSetter
• http://bit.ly/encapsulamentoEModificadores
4.4 Code smell (mal cheiro de código): opcio-
nal!
Ousodoopcionalcomo !noSwiftcomopropriedadeindicaqueumavariá-
velteráumvaloremtempodeexecuçãomasqueocompiladornãosabedisso,
porissooprogramadorforçouo
!goelaabaixonadefiniçãodavariável. Mas
comopodeserqueocompiladornãosaibaquevaitervalor?
Isso acontece comumente, já que a variável utilizada não será iniciali-
z a d an oc o n s t r u t o r .C o m ov i m o sc o m oGood Citizen , a inicialização no
construtorevitaproblemasemtempodeexecução;nocasodoSwifteleevita
fatal errors. Portanto, a regra geral é usar sempre valores válidos, evitando
Optional, e quando usarOptional, tentar usar sempre? com if para
garan tirovalo r;po rfim,usar!,nessaordemdepreferência.
70

## Página 77

CasadoCódigo Capítulo4. Swift: mapeandonossosmodeloseintroduçãoàOrientação...
Veja que os exemplos a seguir todos causam um erro em execução e um
crash de sua aplicação, pois o desenvolvedor cometeu o erro de não checar
o valor opcional. O código doMeal está protegido, mas antes de invocar o
construtor, ao extrair o valor da variávelname, o desenvolvedor comete o
erro:
var name:String?
let brownie = Meal(name: name!, happiness: 5)
Ouaindaem:
var name:String!
let brownie = Meal(name: name, happiness: 5)
4.5 Resumo
Vimos até aqui como definir uma classe, suas propriedades, métodos, inici-
alizadores, como instanciá-la e como invocar seus métodos. Vimos também
boas práticas e cuidados a serem tomados durante a utilização de variáveis
opcionais e obrigatórias. Por fim, colocamos o método em seu devido lugar:
um método fica em quem sabe lidar com determinados dados, Orientação a
Objetosagrupadadosecomportamentos. Nopróximocapítulo,aplicaremos
tudoissoaonossoprojeto.
71

## Página 79

Capítulo5
Projeto: organizandomodelos
co mOOear quivosemgru pos
Voltando ao código do projeto, podemos criar um novo arquivo que conte-
nha nossas classes de modelo. Mas osarquivos facilmente ficarão bagunça-
dos. Para agrupá-los, o Xcode possui uma funcionalidade de criar grupos.
Clicando no projeto, vamos no menu ‘File‘, ‘New Group‘ e chamamos ele de
models. Nossoprojetoficaassim:

## Página 80

5.1. Boaprática: crieumdiretórioporgrupo CasadoCódigo
O problema é que no sistema operacional ele não cria diretório nenhum
e,derepente,temosdiversosarquivosnomesmodiretórionosistemaopera-
cional(enonossorepositório).
5.1 Boaprática:crieumdiretórioporgrupo
Removemos esse grupo usando o delete. Antes de criar um grupo, fazemos
um diretório com o mesmo nome no sistema operacional. Faremos isso cri-
andoodiretório
modelsdentrodo eggplant-browniedonossoprojeto:
74

## Página 81

CasadoCódigo Capítulo5. Projeto: organizandomodeloscomOOearquivosemgrupos
Agora, arrastamos esse diretório para dentro do nosso projeto na pasta
eggplant-brownie, e confirmamos, o que automaticamente cria esse
grupo. Apartirdessemomento,aocriarmososarquivosdentrodessegrupo,
eles são automaticamente gravados no diretório que criamos, assim sempre
teremosumsistemadearquivosrefletindooqueaparecedentrodoXcode.
Aproveitamos e criamos nossos diretórios e grupos para views e
viewcontrollers:
75

## Página 82

5.1. Boaprática: crieumdiretórioporgrupo CasadoCódigo
Dentro do nosso grupo models, criaremos dois arquivos Swift,
Meal.swift e Item.swift. Para isso, clicamos no grupomodels segu-
randoocontroloucomobotãodireitoeescolhemos New File... , Swift
Fileeescolhemosono me Meal.swift.
class Meal {
var name:String
var happiness:Int
var items = Array<Item>()
init(name: String, happiness: Int) {
self.name = name
76

## Página 83

CasadoCódigo Capítulo5. Projeto: organizandomodeloscomOOearquivosemgrupos
self.happiness = happiness
}
func allCalories() -> Double {
println("calculating")
var total = 0.0
for i in items {
total += i.calories
}
return total
}
}
Fazemosomesmoparao Item:
class Item {
var name:String
var calories:Double
init(name: String, calories: Double) {
self.name = name
self.calories = calories
}
}
Mas para que usaremosvar se tais valores são, por enquanto, imutá-
veis? Seguindoaboapráticademanterimutávelaquiloquenãodevemudar,
redefinimostodososcampos,excetooarraycomo let:
class Meal {
let name:String
let happiness:Int
var items = Array<Item>()
init(name: String, happiness: Int) {
self.name = name
self.happiness = happiness
}
func allCalories() -> Double {
println("calculating")
77

## Página 84

5.2. Movendoarquivosnosistemaoperacional CasadoCódigo
var total = 0.0
for i in items {
total += i.calories
}
return total
}
}
class Item {
let name:String
let calories:Double
init(name: String, calories: Double) {
self.name = name
self.calories = calories
}
}
Qualomotivodenãocolocaro arraycomoconstante? Acontecequeele
poderáterseuvaloralteradocomopassardotempo. Pretendemosadicionar
itens nele através do métodoappend que vimos antes. Portanto, oarray
aindaémutável.
5.2 Movendoarquivosnosistemaoperacional
V a m o sm o v e rp o rf o r an o s s oa r q u i v oViewController. Primeiro, nosis-
tema operacional, o movemos para o diretórioviewcontrollers.A o
voltar ao storyboard, percebemos que ele está marcado em vermelho,
como removido. Clicamos com o botão direito e confirmamos a operação
de
delete:
78

## Página 85

CasadoCódigo Capítulo5. Projeto: organizandomodeloscomOOearquivosemgrupos
Git
AmarcaçãovermelhacomaletraDsóaparececasooseuprojetoes-
teja configurado para utilizar um repositório do tipo Git. Por padrão o
Xcode cria seu projeto dessa maneira, mas ele pode não aparecer para
vocêcasotenhadesselecionadoessaopçãoduranteacriaçãodeseupro-
jeto.
Agoraoarrastamosdosistemaoperacionalparadentrodonossoprojeto,
dentrodogrupoquequeremos,o viewcontrollers. OXcodeperguntase
desejamos criar grupos para diretórios. Como dessa vez estamos arrastando
somenteumarquivo,podemosclicar
Oksemmedo:
79

## Página 86

5.2. Movendoarquivosnosistemaoperacional CasadoCódigo
Já o Main.storyboard está dentro diretório Base.lproj;v a m o s
movê-loparao views. ExecutamosomesmoprocessodenoXcoderemover
oar quivoeefetuaro drag and drop :
80

## Página 87

CasadoCódigo Capítulo5. Projeto: organizandomodeloscomOOearquivosemgrupos
Como mudamos os diretórios de diversos arquivos que estavam conec-
tados via texto em configuração, precisamos garantir que todas as conexões
aindaestãook.
Abrimos o storyboard, clicamos no ícone amarelo de
ViewController ec o n f e r i m o ss eac l a s s ed en o s s oViewController
aindaéacerta:
81

## Página 88

5.2. Movendoarquivosnosistemaoperacional CasadoCódigo
Seestivercerto,clicamosnasetaparaverocódigo. Seocódigonãoestiver
conectado, use oassistant editor para conectar novamente o botão e
ascaixasdetexto.
N ossop r o jetoficaen tão:
82

## Página 89

CasadoCódigo Capítulo5. Projeto: organizandomodeloscomOOearquivosemgrupos
5.3 AplicandoobásicodeOrientaçãoaObjetos
AgoradevemosutilizaroqueaprendemosdeOOemnossoprojeto. Devolta
aonosso controller:
@IBAction func add() {
let name = nameField.text;
let happiness = happinessField.text;
83

## Página 90

5.3. AplicandoobásicodeOrientaçãoaObjetos CasadoCódigo
println("eaten: \(name) \(happiness)!")
}
Podemosinstanciarumnovo Meal:
@IBAction func add() {
let name = nameField.text
let happiness = happinessField.text
let meal = Meal(name: name, happiness: happiness)
println("eaten: \(meal.name) \(meal.happiness)")
}
Masocódigonãocompila,o happinessdeveriaserumnúmerointeiro:
@IBAction func add() {
let name = nameField.text
let happiness = happinessField.text.toInt()
let meal = Meal(name: name, happiness: happiness)
println("eaten: \(meal.name) \(meal.happiness)")
}
E ainda não compila: o métodotoInt devolve um opcional, isso fica
clarosetentássemosaplicartipagemexplícita:
@IBAction func add() {
let name:String = nameField.text
let happiness:Int = happinessField.text.toInt()
let meal = Meal(name: name, happiness: happiness)
println("eaten: \(meal.name) \(meal.happiness)")
}
Não estamos aqui para brincadeira, portanto só acessaremos os valores
após ter certeza de que eles são válidos: não queremos nossa aplicação que-
brando. Extraímosovalordedentrodeles,eremovemosatipagemexplícita:
@IBAction func add() {
if nameField == nil || happinessField == nil {
return
}
84

## Página 91

CasadoCódigo Capítulo5. Projeto: organizandomodeloscomOOearquivosemgrupos
let name = nameField!.text
let happiness = happinessField!.text.toInt()
if happiness == nil {
return
}
let meal = Meal(name: name, happiness: happiness!)
println("eaten: \(meal.name) \(meal.happiness)")
}
No futuro veremos como mostrar uma mensagem de alerta indicando
queocorreualgumerro,umamensagemeducada. Testamosnossaaplicação
evemosqueocódigofunciona.
85

## Página 92

5.3. AplicandoobásicodeOrientaçãoaObjetos CasadoCódigo
86

## Página 93

CasadoCódigo Capítulo5. Projeto: organizandomodeloscomOOearquivosemgrupos
Lembre-se: se por algum motivo desconhecido o campo
happinessField tivesse um valor que não fosse válido para a trans-
formaçãovia toInt,teríamosum nilenadaaconteceria.
5.4 Resumo
Não só sabemos utilizar a IDE e a linguagem, mas já conhecemos diversas
boas e más práticas de programação para IOS com Swift. Aprendemos a or-
ganizar nossos arquivos em diretórios no sistema operacional e em grupos
dentro do Xcode. Vimos também como aplicar os conceitos básicos de Ori-
entaçãoaObjetosaocódigoquehavíamosimplementadoanteriormente. Re-
forçamosavalidaçãodevaloresopcionaisparadeixaronossocódigomenos
propícioa fatal errorsecrashesdaaplicação.
87

## Página 95

Capítulo6
Listandoasrefeiçõescom
TableViewController
Nossopróximopassoélistartodasasnossasrefeiçõesatuais,permitindolin-
karousuárioparaumatelaondeeleadicionaumanovarefeição. Estaúltima
jáfoicriada,masprecisamosaindaaprenderafazerumatelacomumatabela
eatrabalharcomanavegaçãoentretelas,i.e. entre views,umconceitomuito
importante.
Oprimeiropassoseráa prenderacriarumatabeladetamanhofixoeen-
tenderoqueénecessáriofornecermosparacriá-la.
Começamos criando um novo projeto no Xcode, temporário, pressio-
nando
Command+Shift+N. Escolhemos novamenteiOS, Single View
Applicationedamosumnomequalquercomo meal-table. Dessavez,
apósabrirmoso Main.storyboard,nãocolocamosnenhum label,que-

## Página 96

CasadoCódigo
remos uma tabela.
Comoéextremamentecomumqueumatabelasejaocomponenteúnico
deum ViewController,temosumcomponentejáchamado Table View
Controller,quepodesercriadocomoum ViewControllerquejápos-
suiumúnicoelemento: uma Table View .
Com o storyboard de nosso projeto aberto, selecionamos nosso
ViewController padrãoeoa p a g a m o su s a n d ooc l i q u ed ad i r e i t a .N o s s o
storyboard fica vazio. Na lista de componentes escolhemos e arrastamos
um Table View Controller paranosso storyboard.
Lembre-se de alterar o tamanho da tela para o iPhone que desejar cli-
cando no UITableViewController, ícone amarelo à esquerda, indo nas
propriedadeseselecionandoo size.
Masaorodaroprogramatemosumatelapreta,oqueaconteceu? Quando
deletamos o ViewController inicial, o programa perdeu a referência do
pontodeentradadanossaaplicação. Opontodeentradaéindicadoporuma
setaqueaparecenoladoesquerdodonosso ViewController.
O que fazemos é selecionar o nossoTable View Controller , cli-
candonaimagemamarela,iràspropriedades( Attributes Inspector ),
ee m Attributes Inspector m a r c a rao p ç ã oIs Initial View
Controller:
90

## Página 97

CasadoCódigo Capítulo6. ListandoasrefeiçõescomTableViewController
A go rasimr odamosop r ogramaevemosatelaco mnossatabela:
91

## Página 98

CasadoCódigo
92

## Página 99

CasadoCódigo Capítulo6. ListandoasrefeiçõescomTableViewController
Primeiro fixaremos o número de linhasde nossa tabela selecionando a
Table View . Confira que ela foi selecionada clicando dentro de onde está
escrito Table View Prototype Content :
Agora, na barra de propriedades à direita, mudamos o conteúdo para o
tipo Static Cells . Assimquefazemosamudança,ficaclaroqueporpa-
drãotemos3célulasemnossatabela. Sedesejamosumnúmerofixodelinhas
nela, podemos remover células selecionando-as ou adicionar novas células
emumatabelautilizandoocomponente
Table View Cell :
93

## Página 100

CasadoCódigo
Adicionamos aquarta célula arrastandoo componente docanto inferior
direito para nossa tabela para exemplificar o funcionamento de uma tabela
customizada. Agora queremos que cada uma das células contenha um texto
básico. Istoé,queremosqueoestilodenossascélulasseja
basic.P a r ai s s o ,
selecionamos as quatro células usando ocommand click em cada uma
delas. Nas propriedades, alteramos ostyle para basic e o resultado são
quatrolinhascomotexto Title,quefuncionabasicamentecomoumlabel
tradicional:
94

## Página 101

CasadoCódigo Capítulo6. ListandoasrefeiçõescomTableViewController
Usandoo double click emcadaumdostextos,alteramosseusvalores
paraquatrorefeiçõesdistintas:
95

## Página 102

CasadoCódigo
96

## Página 103

CasadoCódigo Capítulo6. ListandoasrefeiçõescomTableViewController
Rodamosop r ogramaetemosnossatabela!
Selecionandoo VIEW CONTROLLER inicial
Casoaindativéssemoso View Controller inicial,poderíamoster
arrastadoasetaparao Table View Controller ,indicandocomisso
queeleseriaopontodeentradadenossaaplicação.
6.1 Tabelas dinâmicas usando Dynamic Pro-
totypes
Mas nem sempre sabemos em tempo de programação quantas linhas dese-
jamos ter em uma tabela e seu conteúdo exato. Em geral, desejamos que a
tabelarepresenteumconjuntodedadosquetemosemmemória,algumtipo
de
Array. Àmedidaquemodificamoso Arraydesejamosatualizaratabela
pararefletirtalmudança.
Para isso, usaremos um outro tipo de tabela, a baseada em
Dynamic Prototypes . Criamos um novo projeto com Single
View Application como feito anteriormente. Podemos chamá-lo de
dynamic-meal-table. Arrastamos um Table View Controller e
arrastamosasetaparaqueelepossasernossatelainicial. Deletamostambém
o
View Controller original.
Escolhendo agora nossa tabela, conferimos a opçãoContent na barra
de propriedades à direita, que já deve estar selecionada comoDynamic
Prototypes.
Agoraqueremosconectarnossocódigo ViewController.swiftcom
esse novo controller que criamos no storyboard. Como fazer isso?
Selecionandoo Table View controller ,clicandoemseuíconeamarelo
notipodajanelado table view àdireita:
97

## Página 104

6.1. TabelasdinâmicasusandoDynamicPrototypes CasadoCódigo
98

## Página 105

CasadoCódigo Capítulo6. ListandoasrefeiçõescomTableViewController
Podemosno Identity Inspector (terceiroíconedaesquerdapradi-
reita na barra de propriedades) escolher quem é o código que identifica esse
controller no nosso storyboard. Estamos conectando aview inteira
comanossaclasseSwift.
Estranhamente, ao começar a digitar ViewController (o nome de
nossaclasse),oXcodenãoasugere,porquê?
Acontece que nossa classe não representa um
UITableViewController, mas somente um ViewController co-
mum. Alteramos nosso código para herdar deUITableViewController
járemovendoosegundométodoquenãonosinteressa:
class ViewController :: UITableViewController {
override func viewDidLoad() {
super.viewDidLoad()
}
}
Mas para nosso teste, alteraremos oviewDidLoad para que, ao ter a
viewcarregada,mostremosumamensagemdesucesso:
override func viewDidLoad() {
super.viewDidLoad()
println("view did load")
}
99

## Página 106

6.1. TabelasdinâmicasusandoDynamicPrototypes CasadoCódigo
Herança, SUPER ealtoacoplamento
A palavra-chave override indica que estamos sobrescrevendo um
métodoquejáexistiaemnossaclassemãe.
Oq u eée s s et a ld esuper? Ele invoca o método com a assinatura
(nomeeparâmetros)definidonaclassemãe(oupai,tantofaz),nonosso
caso UITableViewController.Co monãosabemosoq ueométodo
faznaclassemãe,éimportanteochamarmosparaqueeleinicializeoque
fornecessário.
Apalavra
superentregaaoprogramadoratentoaexistênciaumalto
acoplamento entre classes que usam herança: a classe filha tem que en-
tendermuitobemocódigodaclassemãeparasaberquandoelatemque
chamar
superobrigatoriamenteequandoelanãopodechamar super.
Ousoindiscriminadodeherançapodelevaraproblemasdemanutenção
decódigoalongoprazo.
http://blog.caelum.com.br/como-nao-aprender-orientacao-a-objetos-heranca/
Uma vez salvas as alterações no ViewController,d ev o l t aa o
storyboard,aIDEsugereo ViewControllercomoclassequecustomiza
ocomportamentodenosso controller:
Rodamosoprogramaetemosnossatelasemnenhumacélula,masjáco-
100

## Página 107

CasadoCódigo Capítulo6. ListandoasrefeiçõescomTableViewController
nectadaao controller,podemosconferirissoanalisandoolog,quemos-
tranossamensagemimpressaduranteo viewDidLoad:
Precisamosagorado Arrayquerepresentaráosalimentosaseremmos-
trados. Como esse projeto novo não possui nossas refeições, começaremos
comumasimples,de Strings:
let meals = [ "eggplant brownie", "zucchini muffin"]
Mas como armazenar essas refeições de tal maneira que elas fiquem na
memóriaenquantonosso controllerexistir? Podemoscolocarnossomo-
deloqueestásendoexibido(nestecaso,a Arrayde Strings)comopropri-
edadesdenossaclasse:
class ViewController: UITableViewController {
let meals = [ "eggplant brownie", "zucchini muffin"]
override func viewDidLoad() {
super.viewDidLoad()
println("view did load")
}
}
Assim como fizemos com a tabela com tamanho fixo, queremos dizer a
ela quantas linhas desejamos ter. Mas em vez de notificarmos a tabela, nós
101

## Página 108

6.1. TabelasdinâmicasusandoDynamicPrototypes CasadoCódigo
seremos perguntados por ela, isto é, escrevemos uma função que devolve o
númerodelinhasquenossa Table View terá:
func howManyLinesDoWeHaveInOurTable() -> Int {
return meals.count
}
Esse método já existe com o retorno padrão 0, e desejamos reescrevê-lo.
Seuno meé tableVieweelerecebedoisparâmetrosquenãoutilizaremos:
override func tableView(tableView: UITableView,
numberOfRowsInSection section: Int) -> Int {
return meals.count
}
Ao tentarmos rodar, temos um problema. Acontece que falamos o nú-
mero de células desejadas mas não o valor de cada uma delas. Aí não dá...
Vamos definir o valor de cada uma de maneira análoga ao que fizemos com
umatabeladetamanho .
Podemospararoprogramaclicandono
stopevoltaraveronossopro-
jeto clicando emProject Navigator (primeiro ícone da barra de nave-
gaçãoàesquerda).
102

## Página 109

CasadoCódigo Capítulo6. ListandoasrefeiçõescomTableViewController
103

## Página 110

6.1. TabelasdinâmicasusandoDynamicPrototypes CasadoCódigo
Reescreveremosumoutrométododa tableView. Emvezdosdoispa-
râmetrosanteriores(tabelaenúmerodelinhas),recebemosatabelaealinha
daqualelequersaberacélulaaserutilizada:
override func tableView(tableView: UITableView,
cellForRowAtIndexPath indexPath: NSIndexPath)
-> UITableViewCell {
let row = indexPath.row
let meal = meals[ row ]
}
Agora que extraímos a linha em que estamos interessados, criamos uma
nova view do tipo UITableViewCell com o estilo padrão e sem passar
umidentificador:
override func tableView(tableView: UITableView,
cellForRowAtIndexPath indexPath: NSIndexPath)
-> UITableViewCell {
let row = indexPath.row
let meal = meals[ row ]
var cell = UITableViewCell(
style: UITableViewCellStyle.Default,
reuseIdentifier: nil)
}
Játemosacélula. Vamosalterarseutextoparaovalordarefeiçãoeretor-
namos:
override func tableView(tableView: UITableView,
cellForRowAtIndexPath indexPath: NSIndexPath)
-> UITableViewCell {
let row = indexPath.row
let meal = meals[ row ]
var cell = UITableViewCell(
style: UITableViewCellStyle.Default,
reuseIdentifier: nil)
cell.textLabel.text = meal
104

## Página 111

CasadoCódigo Capítulo6. ListandoasrefeiçõescomTableViewController
return cell
}
Ocódigofinaldenosso controlleré:
import UIKit
class ViewController: UITableViewController {
let meals = [ "eggplant brownie", "zucchini muffin" ]
override func viewDidLoad() {
super.viewDidLoad()
println("view did load")
}
override func tableView(tableView: UITableView,
numberOfRowsInSection section: Int) -> Int {
return meals.count
}
override func tableView(tableView: UITableView,
cellForRowAtIndexPath indexPath: NSIndexPath)
-> UITableViewCell {
let row = indexPath.row
let meal = meals[ row ]
var cell = UITableViewCell(
style: UITableViewCellStyle.Default,
reuseIdentifier: nil)
cell.textLabel.text = meal
return cell
}
}
Rodamosnovamenteetemosumatabeladinâmica,comosdoiselemen-
tosquerepresentamasduasrefeições!
105

## Página 112

6.1. TabelasdinâmicasusandoDynamicPrototypes CasadoCódigo
106

## Página 113

CasadoCódigo Capítulo6. ListandoasrefeiçõescomTableViewController
View
Umaviewéumcomponentevisualqualquer. Tantoo controller
éu m av i e wq u a n t oaLabel e uma célula são views. Views po-
dem ser colocadas umas dentro das outras para compor uma view
mais complexa. Nesse nosso caso, temos umcontroller com uma
table view com diversas table view cell .E n q u a n t o c r i a m o s
o UITableViewController visualmente, arrastando-o da barra de
componentes,criamosas UITableViewCellprogramaticamente.
A go raého radea plicarissotudoemnossop r o jeto!
6.2 Resumo
V imoscomocriarumatabeladetamanhofixo ,umatarefaquepodeserapli-
cadaquandotemosdeterminadascaracterísticasaseremconfiguradasouop-
ções a serem selecionadas dentro de um conjunto predeterminado, cujo de-
senvolvedorpodeescreveremtempodedesenvolvimento.
Passamos pela criação de um
controller que já possui um único ele-
mento,atabelaemsi,o UITableViewControllereaprendemosaindicar
qualéopo n todeiníciodenossaaplicação.
Criamosum controllerquemostravaumatabelarefletindoonúmero
de elementos contidos em um array, assim como customizamos o conteúdo
dacéluladessastabelasdeacordocomoconteúdodessearray.
107

## Página 115

Capítulo7
Projeto: listaderefeições
Agoraquejásomoscapazesdecriarumanovarefeição,esabemoscriaruma
tabela,desejamoscriarumavisualizaçãocapazdemostrartodasasrefeições.
Como fazer isso? Se desejamos uma nova visualização no nosso
p r o j e t oo r i g i n a l(eggplant-brownie), podemos adicionar um novo
ViewController,u mq u ei n c l u ad e n t r od e l eu mc o m p o n e n t eq u es e j a
umalistagemderefeições,umatabela. Podemossimplesmenteadicionarum
TableViewController. Abrimos nosso Main.storyboard, procura-
mos o TableViewController na lista de componentes no campo infe-
riordireitoeopuxamosparanosso storyboard. Lembre-sedejámudaro
sizedeleparaode iPhonequeestamosutilizandoatéagora.
Diferentemente do que acontecia até agora nessa aplicação, desejamos
que ela comece com essa view, e não a anterior, a view de adicionar refei-
ç ã o ,p o r t a n t om o v e m o sas e t ad estarting pointde nossa aplicação para esse
novo
controller.

## Página 116

CasadoCódigo
Queremosqueessatabelasejadinâmica,eàmedidaqueadicionemosno-
voselementosnalistaderefeições,elareflitaessanossalista. Temosdiversos
passosparaimplementar:
• Criarocódigodenosso controller;
• Criarumarrayderefeições;
• Fazeratabelarefletirosdadosdoarrayderefeições;
• Permitirclicaremumbotãoeirparaateladeadicionarrefeição;
• Aovoltardateladeadicionarrefeição,atualizaroarrayderefeições.
Começamos criando o código de nosso
controller.N a p a s t a
viewcontrollers, clicando com o botão direito ou com umcontrol-
click, escolhemos New File... . Selecionamos Source dentro de
110

## Página 117

CasadoCódigo Capítulo7. Projeto: listaderefeições
iOS e, clicando duas vezes em Cocoa Touch Class , damos o nome
Meals e escolhemos o tipo UITableViewController, resultando em
MealsTableViewController. Confirmamos que escolhemos Swift
comolinguagem:
OXcodecriaumnovo ViewControllerqueagoraherdaocomporta-
mento de UITableViewController. A classe criada possui diversos mé-
todosimplementadosecomentados,mascomo,emgeral,nãovamosusá-los,
podemos apagar todos os métodos. Já já escreveremos os métodos que nos
interessam.
Precisamosconectaraviewdonosso
storyboardcomo controller
que acabamos de criar, fazendo isso na propriedade de classe customizada,
comofizemosanteriormenteno
storyboard:
111

## Página 118

CasadoCódigo
Cuidado para não tentar customizar a classe somente de sua
UITableView, o Xcode não dará a sugestão que deseja. Escolha seu
MealsTableViewController clicando no ícone amarelo que representa
selecionar o view controller para só então alterar a classe que a
identifica.
Se rodarmos a aplicação, percebemos que não aparece nenhuma linha
p r eenchida.A go raéaho radecriarmosnossasr efeiçõesiniciais:
class MealsTableViewController: UITableViewController {
var meals = [ Meal(name: "Eggplant brownie", happiness: 5),
Meal(name: "Zucchini Muffin", happiness: 3)]
}
Implementamostambémocódigoparadefinironúmerodelinhasrefle-
tindoototalderefeiçõesemnossoarray:
override func tableView(tableView: UITableView,
numberOfRowsInSection section: Int) -> Int {
return meals.count
}
Ométodoquedevolveoconteúdodecadalinhaextrairáonomedecada
refeição:
112

## Página 119

CasadoCódigo Capítulo7. Projeto: listaderefeições
override func tableView(tableView: UITableView,
cellForRowAtIndexPath indexPath: NSIndexPath)
-> UITableViewCell {
let row = indexPath.row
let meal = meals[ row ]
var cell = UITableViewCell(
style: UITableViewCellStyle.Default,
reuseIdentifier: nil)
cell.textLabel.text = meal.name
return cell
}
Rodamos a aplicação: agora temos uma tela com todas as refeições! Mas
ainda temos algo de estranho por aqui, como faremos para adicionar uma
novarefeição? Precisamosdeumabarradenavegação,queveremosembreve.
7.1 Resumo
Vimos neste capítulo como criar umTableViewController que mos-
tra todas as refeições, além de configurá-lo para ser o novo ponto
de entrada de nossa aplicação. Sobrescrevendo métodos de nosso
TableViewController, fomos capazes de configurar a quantidade de li-
nhaseoconteúdodecadacéluladenossatabelaparaseguirosdadospresen-
tesemumarra ydeob jetos.
113

## Página 121

Capítulo8
Navegandoentretelas
Precisamosfornecerumamaneiraparanossousuáriosairdalistagemdere-
feiçõeseirparaateladenovarefeição: queremostrabalharcomanavegação
e n t r et e l a s .E l ep r e c i s an a v e g a re n t r eat e l ad el i s t a g e mead en o v ar e f e i ç ã o ,
tantoaidaquantoavolta. Queremosumabarradenavegação,eissopodeser
feitoatravésdeum
Navigation Controller .
Começamos clicando em nossa tabela e, no menuEditor, submenu
Embed In , escolhemos Navigation Controller , fazendo com que
nosso controllertenhaagoraumabarradenavegação. Comodecostume,
mude o tamanho do seuNavigation Controller . Note também que o
X codejámo veuopon todeen tradadoprogramaparaatelacomna vegação:

## Página 122

CasadoCódigo
Primeiro, foi criado um Navigation Controller en o s s o
MealsViewController foi alterado para ser a raiz ( root), o ponto
de entrada desseNavigation Controller .N ap r á t i c a ,oNavigation
Controllerésóumacapaquevesteonosso controllerinicial. Apartir
daí, a navegação é feita sempre mantendo essa capa de navegação. Portanto,
não faremos nada agora no Navigation Controller em si, mas no
nosso controllerantigo.
Noteque,nonosso controllerantigo,temosumabarradenavegação,
naqualpodemosadicionarumcomponentechamado Bar Button Item ,
em udamosseuno mepara Add.
116

## Página 123

CasadoCódigo Ca p í tulo8. N a vegandoen tr etelas
Agora, com a teclaControl apertada, arrastamos o botão para nossa
tela de Adicionar Refeição , escolhendo a opçãoAction Segue ->
show,istoé,aoclicarnobo tão ,mostr eessatela.
117

## Página 124

CasadoCódigo
Podemos perceber que alguns campos do formulário ficaram atrás da
barra de navegação. Para fazer com que apareçam embaixo da barra, cli-
camos no View Controller do formulário e, no menu de propriedades
( Attributes Inspector ), desmarcamos Under Top Bars .P r o n t o ,
agoraoscampossãodeslocadosautomaticamenteparabaixo.
Rodamosoprogramaepercebemosque,aoclicarnobotão,vamosdireto
paraateladenovarefeição. Perfeito,masaoclicaremadicionar,nãovoltamos
paraatelaanterior. Temosquefazeravolta.
118

## Página 125

CasadoCódigo Ca p í tulo8. N a vegandoen tr etelas
8.1 Navegandocomumapilhadetelas
Parafazeravolta,devemosdizerparanosso controllerdenavegaçãoque
desejamosvoltaratrásnatelaatual. Istoé,cadavezquemostramosumatela
de maneira tradicional (chamada depush), estamos empilhando uma tela
emcimadaoutra.
Quando desejamos remover a tela atual de cima da anterior, usamos o
método pop. Portanto, em nossa funçãoadd,n o ViewController, de-
vemospegarnosso navigationController (queéopcional)efalarpara
eleremovero view controller demaneiraanimada:
self.navigationController!.popViewControllerAnimated(true)
Cuidado com métodos de nome parecido com o
popViewControllerAnimated, a escolha de outro método trará um
outroefeito,claro.
Mas, opa, nosso atual controller pode e pode não ter um
navigationController, sendo assim estamos acessando uma variável
que pode destruir nossa aplicação. Podemos nos proteger usando a constru-
ção
let:
if let navigation = self.navigationController {
navigation.popViewControllerAnimated(true)
}
Agora sim, temos nosso métodoadd que extrai os dados, transforma
on ú m e r oev o l t ap r at e l aa n t e r i o r ,s e m p r ec o mag a r a n t i ad eq u ee r r o sd e
inicializaçãooudeentradadousuár ionãoquebrarãonossaapp:
@IBAction func add() {
if nameField == nil || happinessField == nil {
return
}
let name = nameField!.text
let happiness = happinessField!.text.toInt()
if happiness == nil {
return
119

## Página 126

8.1. Navegandocomumapilhadetelas CasadoCódigo
}
let meal = Meal(name: name, happiness: happiness!)
println("eaten: \(meal.name) \(meal.happiness)")
if let navigation = self.navigationController {
navigation.popViewControllerAnimated(true)
}
}
Navigationopcional?
Eaperguntade1000reais:comoassimo navigationController
éumavariávelopcionaldomeu controller? Aconteceque,devidoà
decisão da API de fazer com que umUIViewControllersemprete-
n h ae s s av a r i á v e l ,e l ap o d ee s t a rs e t a d ao un ã o . . .p o i sv o c êp o d ee s t a r
dentro de um UINavigationViewController ou não. Em tempo
decompilação,aAPInãosabedisso,portantodeixaavariávelcomoop-
cional.
AAPIpoderiaserrecriada(quebrandocompatibilidadecomversões
anteriores, o que é muitas vezes indesejado) para que a variável só exis-
tisse em compilação caso seu
controller estivesse realmente dentro
deum navigation controller ,evitandoavariávelopcionalepos-
síveiserrosemtempodeexecução.
Mas como toda decisão de quebrar compatibilidade é perigosa, por
enquanto convivemos com tal variável opcional e o perigo de acessá-la
semverificarseuvalor.
Testamosnovamentenossaaplicaçãoe,agora,quandoclicamosnobotão
de adicionar, ele desempilha nossa tela, mostrando a tela de refeições nova-
mente.
120

## Página 127

CasadoCódigo Ca p í tulo8. N a vegandoen tr etelas
8.2 Resumo
Vimos como podemos criar um NavigationController que permite
a navegação entre diversos View controllers . Apresentamos um
controller com o push de um segue ev o l t a m o sp a r aat e l aa n t e r i o r
como popprogramático.
121

## Página 129

Capítulo9
Designpattern: delegate
Nossopróximopassoéconseguiratualizarnossatelacomarefeiçãoqueacaba
desercriada. Comofazerisso? Podeserdediversasmaneiras:aprimeiraéfa-
zercomquealistafiqueperguntandoatodoomomentoseumanovarefeição
foi criada. Esta técnica é chamada de
polling e parece não se encaixar de
jeito nenhum aqui. Uma segunda forma é pedir para que o formulário avise
que uma nova refeição foi criada, e quem quiser pode escutar este evento e
fazerasaçõesnecessárias.
Estaúltimaéaimplementaçãodop adrãochamado
Delegate:of o rm u -
láriodelegaaresponsabilidadedeadicionaroresultadonoarrayparaalguém
quesabeterminaressetrabalho,atualizandoatelacomanovarefeição. Esse
design patternlembra o
Observer do livro “Design Patterns: Elements of
ReusableObjected-OrientedSoftware”,ondeumoutroobjetoénotificadode
umeventoqueocorreu.
Primeiro, precisamos que nosso
MealsTableViewController seja

## Página 130

CasadoCódigo
capaz de adicionar uma nova refeição ao array existente. Adicionamos nele
ummétodo add:
func add(meal: Meal) {
meals.append(meal)
}
A go ra,of o rm ulá riodoViewController,apósadicionaranovarefei-
ção, deve invocar uma ação que faça o registro dela para quem precisar ser
informadodesteevento,ouseja,parao
delegatedestaação:
@IBAction func add() {
if nameField == nil || happinessField == nil {
return
}
let name = nameField!.text
let happiness = happinessField!.text.toInt()
if happiness == nil {
return
}
let meal = Meal(name: name, happiness: happiness!)
println("eaten: \(meal.name) \(meal.happiness)")
delegate.add(meal)
if let navigation = self.navigationController {
navigation.popViewControllerAnimated(true)
}
}
M a so n d ee s t áav a r i á v e ldelegate? Precisamos criá-la como proprie-
dade,paraquealguémpossaconfigurá-la:
var delegate:MealsTableViewController
@IBAction func add() {
if nameField == nil || happinessField == nil {
124

## Página 131

CasadoCódigo Capítulo9. Designpattern: delegate
return
}
let name = nameField!.text
let happiness = happinessField!.text.toInt()
if happiness == nil {
return
}
let meal = Meal(name: name, happiness: happiness!)
println("eaten: \(meal.name) \(meal.happiness)")
delegate.add(meal)
if let navigation = self.navigationController {
navigation.popViewControllerAnimated(true)
}
}
M a ss en o s s o delegate só vai ser configurado após o
ViewController ser criado, precisamos deixá-lo como variável opci-
onal:
var delegate:MealsTableViewController?
@IBAction func add() {
if nameField == nil || happinessField == nil {
return
}
let name = nameField!.text
let happiness = happinessField!.text.toInt()
if happiness == nil {
return
}
let meal = Meal(name: name, happiness: happiness!)
println("eaten: \(meal.name) \(meal.happiness)")
125

## Página 132

CasadoCódigo
delegate.add(meal)
if let navigation = self.navigationController {
navigation.popViewControllerAnimated(true)
}
}
Ejásabemosque,seéopcional,temosquecuidarcomcarinho:
var delegate:MealsTableViewController?
@IBAction func add() {
if nameField == nil || happinessField == nil {
return
}
let name = nameField!.text
let happiness = happinessField!.text.toInt()
if happiness == nil {
return
}
let meal = Meal(name: name, happiness: happiness!)
println("eaten: \(meal.name) \(meal.happiness)")
if delegate == nil {
return
}
delegate!.add(meal)
if let navigation = self.navigationController {
navigation.popViewControllerAnimated(true)
}
}
Rodamosonossoprograma,amensagemdelogaparecemasnãosaimos
da tela. Clicamos no botão ‘Back‘ e não temos o elemento na tabela. Isso
aconteceporqueanossavariávelopcional,o delegate,nãofoiconfigurada!
126

## Página 133

CasadoCódigo Capítulo9. Designpattern: delegate
P o rt a n t oo‘ p r i n t l n ‘f o ie x e cu t a d oel o g od e po i sae x e cu ç ã op a r o uac h a m a d a
anossafunção‘add‘pois‘delgate==nil‘eraverdadeiro.
Quem será então nossodelegate? Quem observará a view de adicio-
narrefeiçãoparasernotificadoquandoumanovarefeiçãofoicriada? Nosso
MealsTableViewController.
9.1 Configurandoumdelegateviasegue
Precisamos agora notificar o ViewController de que nós,
MealsTableViewController,s o m o sos e uObserver,os e u delegate.
Mas como fazer isso se a conexão entre os doiscontrollers é feita via
umaseta(um segue)nostoryboard,enãoviaprogramação? Comopassar
um parâmetro via programação para outro controller, sendo que a
conexãoéfeitaviaarrastaesolta?
Se tivéssemos acesso aocontroller de destino na hora da navegação,
poderíamospegaroobjetoecolocarnossodelegatenele.
Nossos controllersnosdisponibilizamummomentodealegriaantes
deredirecionaremparaoutraview. Aoseprepararparaseguirum segue,o
controller invoca um método chamadoprepareForSegue,o n d ep o -
demossobrescreverefazeralgocomoqueserámostrado.
override func prepareForSegue(segue:
UIStoryboardSegue, sender: AnyObject?) {
}
Reparequeafunçãorecebeum segue,aquelequeeleestáseguindo. Mas
comosabemosqualeleestáseguindo? Precisamosdealgumidentificador,de
um
id. Vamos emnossostoryboard, clicamosno segue e, em seguida, no
menu Attributes Inspector ,vamosconfigurarseuidentificadorcomo
addMeal.
127

## Página 134

9.1. Configurandoumdelegateviasegue CasadoCódigo
Agora sim, em nosso prepareForSegue do
MealsTableViewController podemos condicionar a execução ao
seguequedesejamos:
override func prepareForSegue(segue: UIStoryboardSegue,
sender: AnyObject?) {
if(segue.identifier == "addMeal") {
}
}
O que falta agora é pegar nossocontroller de destino, que podemos
ob terdap r ó p riasegue:
override func prepareForSegue(segue: UIStoryboardSegue,
sender: AnyObject?) {
if(segue.identifier == "addMeal") {
let view = segue.destinationViewController as ViewController
}
}
128

## Página 135

CasadoCódigo Capítulo9. Designpattern: delegate
Esetarmosnosso delegate:
override func prepareForSegue(segue: UIStoryboardSegue,
sender: AnyObject?) {
if(segue.identifier == "addMeal") {
let view = segue.destinationViewController as ViewController
view.delegate = self
}
}
Pronto. Testamosnossaaplicação,arefeiçãoéadicionadacomsucesso:
129

## Página 136

9.1. Configurandoumdelegateviasegue CasadoCódigo
130

## Página 137

CasadoCódigo Capítulo9. Designpattern: delegate
Boaprática:recarregueosdadosdeumatabela
Nossocódigodeadicionarnovarefeiçãoestábemsimples:
func add(meal: Meal) {
meals.append(meal)
}
Mas a tabela não é redesenhada automaticamente só por ter adicio-
nadoumelementonovoemumarray. Nonossocaso,elaéredesenhada
pois retiramos umViewController q u ee s t a v an af r e n t e ,f o r ç a n d oa
apariçãodatabelanovamente. Comoométodo add podeserchamado
em situações em que opop não seria chamado, é interessante garantir
que, toda vez que adicionamos algo através desse método, a tabela seja
redesenhada. Para isso, invocamos o método
reloadData de nossa
tableView:
func add(meal: Meal) {
meals.append(meal)
tableView.reloadData()
}
9.2 Codesmell: nomesgenéricosdemaisecomo
extrairumprotocolo
M a sq u a lot i p od av a r i á v e ldelegate? Sério mesmo que é
MealsTableViewController? I s t oé ,n oc ó d i g od eu mcontroller
temos uma referência para o outro, e no outro para o um, explicitamente.
Quantomaioroacoplamentoentreduasclasses,maiscomplexoficamudá-las
semumaalteraraoutra,eissoéalgoquequeremosevitar,claro.
Esta variável precisa ser de um tipo que possua obrigatoriamente o mé-
todo
add para que possamos invocá-lo, mas não precisa ter todo o resto
que um MealsTableViewController tem. Para podermos garantir que
on o s s odelegate terá com toda a certeza o métodoadd, temos que fa-
131

## Página 138

9.2. Codesmell: nomesgenéricosdemaisecomoextrairumprotocolo CasadoCódigo
zer com que ele assine uma espécie de um contrato que o obrigue a ter este
método. Umcontratofuncionacomoumainterface: todosqueaimplemen-
tarem devem cumprir com os métodos definidos lá dentro. Este contrato é
chamadode
Protocol.
Precisamos extrair o protocolo que tenha o métodoadd que recebe um
Meal:
protocol MyDelegate {
func add(meal: Meal)
}
Comoeste protocolseráutilizadoparaquenosso ViewController
consigainvocaro delegate,vamosdeclará-lonomesmoarquivodenosso
ViewController,o ViewController.swift logo antes da declaração
daclasse:
protocol MyDelegate {
func add(meal: Meal)
}
class ViewController: UIViewController {
//restante do código
}
Falta decidir qual nome usar para nossa interface, nossoprotocol,
MyDelegate não parece um nome que diz muito sobre nosso domínio ou
oqueoprotocolofaz. ExisteumaconvençãodaAppleparanomesdeproto-
colos,criadanaépocadoObjective-C: http://bit.ly/swiftcodenamingbasics
M aspa raoscasosde Delegate aregraqueaAppleutilizaemsuaAPI,
é de colocar o nome da classe que terá seu comportamento delegado mais
a palavra
Delegate. Veremos em breve oUITableViewDelegate,p o r
exemplo. Emnossocaso,temosentão ViewControllerDelegate:
protocol ViewControllerDelegate {
func add(meal: Meal)
}
132

## Página 139

CasadoCódigo Capítulo9. Designpattern: delegate
Nomenclaturadeprotocolos
O problema dessa convenção ao mesmo tempo oficial e não oficial no
padrão do delegate está ligado à sua desconexão do nosso domínio. O
que um ViewControllerDelegate faz? Não tenho ideia. O que um
AddAMealDelegatefaz? Eleadicionaumarefeição. Adesconexãodonosso
projetocomodomíniodenegócioséumdosfatoresquedificultaamanuten-
çãodocódigo. Alémdisso,umadasmaneirasdeveresse delegateécomo
um Observer;notifique-mequandoumanovarefeiçãoforcriada. Teríamos
umprotocolototalmentediferente:
protocol MealsObserver {
func created(meal: Meal)
}
O resultado seria o mesmo, sendo uma mera discussão de “qualdesign
patternesto uusando ” ,po rtan tode“ qualno medevousar ” .
Nonossocaso,vamosfugirdopadrão ViewControllerDelegatepor
um único motivo: ele nos induz a manter um únicodelegate. E se dese-
jássemos ter doisdelegates para uma única tela, como por exemplo um
dashboard de funções de nossa aplicação, em que cada gráfico clicado gera
umaaçãototalmentediferente? Usandoopadrãomencionado,teríamosum
único
Delegate? O desenvolvedor, para tentar seguir o padrão, se sentiria
tentadoamanterocódigotodoemumúnicolugar.
Emvezdecolocarmosmuitaresponsabilidadeemumúnicolugar,vamos
lutar pela separação de responsabilidades e por protocolos menores, sendo
assim,jáescolheremosumnomededomínioparanosso
Delegate.
Queremos um nome deDelegate que faça sentido para nosso domí-
nio, um protocolo que define quem será capaz de adicionar refeições, um
AddAMealDelegate. Nossoprotocoloé,naverdade:
protocol AddAMealDelegate {
func add(meal: Meal)
}
Agorapodemoscolocarotipodenossavariável:
var delegate:AddAMealDelegate?
133

## Página 140

9.2. Codesmell: nomesgenéricosdemaisecomoextrairumprotocolo CasadoCódigo
T e m o st a m b é mq u ef a l a rq u en o s s ac l a s s e
MealsTableViewControlleradotaesseprotocolo:
class MealsTableViewController: UITableViewController,
AddAMealDelegate {
// ...
}
P o rtan to ,ocódigodenossoViewControllerfica:
import UIKit
protocol AddAMealDelegate {
func add(meal: Meal)
}
class ViewController: UIViewController {
@IBOutlet var nameField: UITextField!
@IBOutlet var happinessField: UITextField!
var delegate:AddAMealDelegate?
@IBAction func add() {
if nameField == nil || happinessField == nil {
return
}
let name = nameField!.text
let happiness = happinessField!.text.toInt()
if happiness == nil {
return
}
let meal = Meal(name: name, happiness: happiness!)
println("eaten: \(meal.name) \(meal.happiness)")
if delegate == nil {
return
134

## Página 141

CasadoCódigo Capítulo9. Designpattern: delegate
}
delegate!.add(meal)
if let navigation = self.navigationController {
navigation.popViewControllerAnimated(true)
}
}
}
T estamosno vamen tenossaa plicaçãoeocódigoestáfuncio nando .
Máprática:muitosseguescomparâmetros
O uso de muitossegues gera um código cheio deifs,t a m b é m
conhecido como switch. Ambos são indicadores de que existe muita
responsabilidade em um único ponto de nosso código, o que o torna
cada vez mais difícil de manter. Existem diversas técnicas para evi-
tar esses
ifs, como o uso de polimorfismo em Orientação a Obje-
tos. Veremos mais à frente como evitar a passagem de parâmetro via
prepareForSeguefazendocomoosdesenvolvedoressêniores,usando
programaçãonormal.
9.3 Resumo
Conhecemos aqui o padrão observer que é aplicado com o nome de
Delegate paranotificarumaoutrateladeumaaçãorealizadanatelaatual.
Quemobservaanotificaçãonãoprecisavanecessariamenteseroutratela,bas-
tavaimplementarum
protocolquedefinimos.
Precisamos dar uma identificação para osegue para que ele possa ser
utilizadoduranteapreparaçãoderedirecionamento,omomentonoqualcon-
figuramosemnosso viewcontroller quemseráo
delegateaserinvocado.
O delegate é o coração da comunicação entre telas, sem ele seríamos
obrigados a apelar para variáveis globais - a maior de todas as quebras de
encapsulamento.
135

## Página 142

9.3. Resumo CasadoCódigo
OpostdaCaelum http://bit.ly/singletons-statictemumaexplicaçãosobre
algunsmotivospelosquaisvariáveisglobaissãoperigosasparaamanutenção
deumaaplicação.
O sn o m e sd ec l a s s e s ,m é t o d o sev a r i á v e i ss ã oi m p o r t a n t e sp a r aam a n u -
t e n ç ã od eu mc ód i g oe ml o n g op r a z oead i scu s s ã oéu m aq u ea i n d ae s t áe m
aberto. Porumlado,temosumaconvençãoquenoslevaaacumularrespon-
sabilidades em um único protocolo, e posteriormente em uma única classe,
poroutrolado,umnomequefogedaconvenção.
136

## Página 143

Capítulo10
Relacionamentoumparamuitos:
listadealimentos
Aoadicionarumanovarefeição,devemosescolherquaissãoosalimentosque
a compõem. Isto é, desejamos mostrar a lista de itens na tela de nova refei-
ção. Sevamosmostrarumalista,adicionaremosumatabela. Mascomofazer
issoseo
controller quevimosatéagoraparaacriaçãodetabelaspermi-
tia somente a existência de tabelas? Vamos adicionar um único componente
novoao
controllerdenovarefeição: uma TableView,arrastando,como
sempre, a view do canto inferior direito até nossoview controller no
storyboard:

## Página 144

CasadoCódigo
138

## Página 145

CasadoCódigo Capítulo10. Relacionamentoumparamuitos: listadealimentos
Comotoda TableView dinâmica, devemos indicar quem será o objeto
responsávelporimplementarosmétodosquedescrevemumatabela,comoo
númerodecélulaseseuconteúdo.
Como queremos que nossoview controllerseja responsável por tais mé-
todos, devemos primeiro fazer com que ele implemente os protocolos ade-
quados ou herde de
UITableViewController. Mas não somos bem um
UITableViewController, certo? Não queremos assumir mais responsa-
bilidades do que realmente devemos, portanto preferimos implementar so-
menteoprotocoloqueforneceosdadosdatabela,afontededados,o
data
source,oprotocolochamado UITableViewDataSource:
class ViewController: UIViewController, UITableViewDataSource {
// ...
}
No storyboard, selecionamos nosso TableView e, na aba
Connections Inspector (último ícone na barra de propriedades),
puxamos o dataSource para o ícone de nosso View Controller
(aqueleamarelonotopodateladeadicionar):
139

## Página 146

CasadoCódigo
Precisamosimplementaragoraosmétodos tableView q uer eto rna ma
quantidade de alimentos dentre os quais o usuário selecionará os que entra-
ramnarefeição,alémdométodoquedevolveoconteúdodecadacélula. Para
isso, vamos primeiro criar um array com todos os alimentos possíveis. Se-
gundominhaesposaconfeiteira,obrowniedeberinjelapodecombinarcom
uma cobertura de chocolate, enquanto o muffin de abobrinha vai bem com
gotinhas de chocolate. Criamos alguns itens para nossas sobremesas saudá-
veiscomcoberturasopcionais:
var items = [ Item(name: "Eggplant Brownie", calories: 10),
Item(name: "Zucchini Muffin", calories: 10),
Item(name: "Cookie", calories: 10),
Item(name: "Coconut oil", calories: 500),
Item(name: "Chocolate frosting", calories: 1000),
Item(name: "Chocolate chip", calories: 1000)
]
Implementamos os dois métodos de fonte de dados de uma tabela que
vimosdiversasvezes. Oqueretornaaquantidadedeelementos:
func tableView(tableView: UITableView,
numberOfRowsInSection section: Int) -> Int {
return items.count
}
Eoqueretornaoconteúdodecadacélula:
func tableView(tableView: UITableView,
cellForRowAtIndexPath indexPath: NSIndexPath)
-> UITableViewCell {
let row = indexPath.row
let item = items[ row ]
var cell = UITableViewCell(style:
UITableViewCellStyle.Default,reuseIdentifier: nil)
cell.textLabel.text = item.name
return cell
}
140

## Página 147

CasadoCódigo Capítulo10. Relacionamentoumparamuitos: listadealimentos
Se rodarmos a aplicação, notamos que a tabela já reflete os dados do ar-
ray, mas ainda temos alguns passos pela frente: sempre é bom entendermos
melhoroquefizemos,melhoramosocódigoecontinuamos.
10.1 ProtocolosdaAPI
Masporquenãoestamosescrevendomais override func tableView e,
inclusive, se usarmos a palavraoverride ocompiladorreclama? Acontece
que o protocoloUITableViewDataSource não fornece nenhuma imple-
mentaçãodométodo,somentesuacara,suainterface(basicamenteseunome
eseusparâmetros).
Já ao herdar o
UITableViewController, ele mesmo implementa o
protocolo UITableViewDataSource e já escreve uma versão inicial des-
ses métodos. Como no caso doUITableViewController estamos so-
brescrevendo um método já existente, usamos a palavra-chaveoverride
para deixar isso claro. Como somente puxamos a definição do proto-
colo, não estamos sobrescrevendo nada. Você pode conferir o protocolo
UITableViewDataSource mantendoo command apertadoeclicandoem
seunome:
protocol UITableViewDataSource : NSObjectProtocol {
func tableView(tableView: UITableView,
numberOfRowsInSection section: Int) -> Int
func tableView(tableView: UITableView,
cellForRowAtIndexPath indexPath: NSIndexPath)
-> UITableViewCell
// optional
}
A primeira vez que você executa esse clique o Xcode pode dizer que
não encontrou o que procurara (Symbol not found ). Em XCode,
Preferences, Downloads vocêpodebaixaradocumentaçãodoiOS.
Repare que oUITableViewDataSource possui dois métodos obriga-
tórios,justamenteosdoisquedefinimos.
141

## Página 148

10.2. SeleçãomúltiplaeCellAccessory CasadoCódigo
Testamos nossa aplicação e ela já mostra a tabela com os alimentos que
entramemnossarefeição. Faltaagorasercapazdeselecioná-los.
10.2 SeleçãomúltiplaeCellAccessory
Cada vez que selecionamos um item, gostaríamos de marcá-lo
com um check, algo que indique que vamos utilizá-lo na hora
de criar nossa refeição. O UITableViewCell fornece uma ma-
neira de colocar informações extras em uma célula através da
enum
UITableViewCellAccessoryType*. Por exemplo, o
UITableViewCellAccessoryType.Checkmark adiciona uma marca de
checkenquantoo UITableViewCellAccessoryType.Noneéopadrão
semnenhumamarca.
Enum
Uma enum é basicamente uma coleção de valores limitados e pré-
fixados. Veja no caso a seguir, onde definimos o tipo de erro como pos-
sivelmentesendo
FATALou WARNING:
enum ErrorType {
case FATAL
case WARNING
}
Enumspodemserutilizadasemprogramaçãofuncionalcomoumre-
cursoparagarantirquetodososcasosforamtratados,comoquandofa-
zemospatternmatching. EmOrientaçãoaObjetos,écomumutilizarmos
polimorfismoparaobterresultadossimilares.
Precisamosescreverométodoqueéinvocadotodavezqueousuáriotenta
selecionarumacélula:
func tableView(tableView: UITableView,
didSelectRowAtIndexPath indexPath: NSIndexPath) {
}
142

## Página 149

CasadoCódigo Capítulo10. Relacionamentoumparamuitos: listadealimentos
M a sa ot e n t a re s c r e v e rtableView percebemos que o editor não nos
ajuda: essemétodoaindanãoexiste. Comoassim?
Se vamos implementar os comportamentos de delegate como fi-
zemos aqui, temos que dizer que estamos suportando esse protocolo, o
UITableViewDelegate:
class ViewController: UIViewController,
UITableViewDataSource, UITableViewDelegate {
// ...
}
AgorasimoXcodenosajudaepodemos,dentrodessemétodo,recuperar
acél ulaquefo iescolhidapelousuário:
func tableView(tableView: UITableView,
didSelectRowAtIndexPath indexPath: NSIndexPath) {
let cell = tableView.cellForRowAtIndexPath(indexPath)!
}
Marcamoscolocandoummarcadordotipo Checkmark:
func tableView(tableView: UITableView,
didSelectRowAtIndexPath indexPath: NSIndexPath) {
let cell = tableView.cellForRowAtIndexPath(indexPath)
cell.accessoryType = UITableViewCellAccessoryType.Checkmark
}
O código não compila, a tipagem explícita escondeu queacell é opci-
onal. Vamosverificarseacélulafoiencontradaparaentãomarcá-la:
func tableView(tableView: UITableView,
didSelectRowAtIndexPath indexPath: NSIndexPath) {
let cell = tableView.cellForRowAtIndexPath(indexPath)
if cell == nil {
return
}
cell!.accessoryType = UITableViewCellAccessoryType.Checkmark
}
143

## Página 150

10.2. SeleçãomúltiplaeCellAccessory CasadoCódigo
Rodamos nossa aplicação, selecionamos os elementos nos quais te-
mos interesse e nada acontece. Esquecemos de marcar que o nosso
ViewControllernãosóéresponsávelpelafontededados( data source )
denossatabela,mastambémteráseusmétodosinvocadosquandoalgonata-
bela acontecer. Ele é nossoobserver da tabela - nossodelegate.V o l t a m o s
à edição visual daTableView e agora arrastamos odelegate para nosso
ViewController,comofizemosparao dataSource:
Testamosnossaaplicaçãoetemosoresultado:
144

## Página 151

CasadoCódigo Capítulo10. Relacionamentoumparamuitos: listadealimentos
145

## Página 152

10.3. Desselecionandoelementos CasadoCódigo
10.3 Desselecionandoelementos
Opa, mas e se selecionei errado? Já era? Faltou implementarmos suporte
para que quem está marcado possa ser desmarcado. Verificamos se nossa
c é l u l an ã op o s s u iu m
checkmark e, se não possuir, o adicionamos; caso
possua, removemos. Vamos adicionar essa verificação no mesmo método a
queatribuímoso
Checkmarkanteriormente:
if (cell!.accessoryType == UITableViewCellAccessoryType.None) {
cell!.accessoryType = UITableViewCellAccessoryType.Checkmark
} else {
cell!.accessoryType = UITableViewCellAccessoryType.None
}
10.4 Armazenandoaseleção
Precisamos agora armazenar nossa seleção em algum lugar, para podermos
criarnossarefeiçãonahoraadequada. Podemoscriarumarrayquemantém
osnúmerosdaslinhasselecionadas:
var selected = Array<Int>()
func tableView(tableView: UITableView,
didSelectRowAtIndexPath indexPath: NSIndexPath) {
let cell = tableView.cellForRowAtIndexPath(indexPath)!
if (cell.accessoryType == UITableViewCellAccessoryType.None){
cell.accessoryType =
UITableViewCellAccessoryType.Checkmark
selected.append(indexPath.row)
} else {
cell.accessoryType = UITableViewCellAccessoryType.None
// remove
}
}
Mas um array deInt? Sériomesmo? Estamostrabalhandocomobjetos
eagorabrincamoscomarraysde Int? Nossoarrayéde Item:
146

## Página 153

CasadoCódigo Capítulo10. Relacionamentoumparamuitos: listadealimentos
var selected = Array<Item>()
func tableView(tableView: UITableView,
didSelectRowAtIndexPath indexPath: NSIndexPath) {
let cell = tableView.cellForRowAtIndexPath(indexPath)!
if (cell.accessoryType == UITableViewCellAccessoryType.None){
cell.accessoryType =
UITableViewCellAccessoryType.Checkmark
selected.append(items[indexPath.row])
} else {
cell.accessoryType = UITableViewCellAccessoryType.None
// remove
}
}
Para testarmos, ao inicializarmos nossoMeal desejamos configurar seu
meal.itemseimprimi-lo:
@IBAction func add() {
if nameField == nil || happinessField == nil {
return
}
let name = nameField!.text
let happiness = happinessField!.text.toInt()
if happiness == nil {
return
}
let meal = Meal(name: name, happiness: happiness)
meal.items = selected
println(
"eaten: \(meal.name) \(meal.happiness) \(meal.items)")
if delegate == nil {
return
}
147

## Página 154

10.4. Armazenandoaseleção CasadoCódigo
delegate!.add(meal)
if let navigation = self.navigationController {
navigation.popViewControllerAnimated(true)
}
}
Podemostestarnossaaplicaçãoeveroresultado: perfeito,eleimprimeno
log um array com o mesmo número de elementos que selecionei em minha
tabela:
Faltaremovermososdesselecionados. Paraisso,desejamoschamarafun-
ção removedenossoarray:
selected.remove....
Masnãoexistefunçãoquerecebeoobjetoaserremovido. Somenteuma
funçãoquerequeraposiçãoaserremovida:
selected.removeAtIndex(position)
Logo, devemos primeiro achar a posição de nosso elemento em nosso
array,usandoafunção find:
let position = find(selected, items[indexPath.row])
selected.removeAtIndex(position)
148

## Página 155

CasadoCódigo Capítulo10. Relacionamentoumparamuitos: listadealimentos
Masocódigonãocompila. Acontecequeafunção findpassaportodos
os elementos de nosso array, verificando se cada um deles é igual (==)a o
elemento que estamos procurando. Caso ele encontre o valor, ele retorna a
posição,casocontrário,retorna nil. Umaimplementaçãopossívelparaessa
função find,quejáexiste,seriaalgosimilara:
func find(elements:Array<Item>, toFind:Item) -> Int? {
let max = elements.count - 1
for i in 0...max {
if toFind == elements[i] {
return i
}
}
return nil
}
Implementandoo==
Note que, para encontrarmos o elemento, usamos o operador=, mas
como comparar dois Items? Precisamos de alguma maneira falar que
esses itens são comparáveis, que temos como verificar se eles são iguais,
Equatable. Portanto,fazemosnossaclasseadotaroprotocolo Equatable:
class Item: Equatable {
// code
}
Eimplementarafunção ==,querecebedoisitensedevolveum Bool:
func ==(first:Item, second:Item) -> Bool {
return first.name == second.name &&
first.calories == second.calories
}
Muitocuidado! Afunção ==deveserdefinidaforadaclasse:
// Item.swift
class Item: Equatable {
149

## Página 156

10.4. Armazenandoaseleção CasadoCódigo
// code
}
func ==(first:Item, second:Item) -> Bool {
return first.name == second.name &&
first.calories == second.calories
}
A implementação do== permite que o programador faça comparações
entreobjetosaoutilizardiversaspartesdaAPIfornecidapeloiOS.Alémdisso,
outros programadores criam suas bibliotecas baseadas na existência de uma
comparaçãocompatívelcomadefiniçãodo
==.
Agora sim, podemos verificar se nosso item existe dentro de nosso array
utilizando a funçãofind que já existe. Mas lembre-se: ofind retorna um
Optional, vamos verificar se encontramos a posição com o elemento que
queremosremover,eaíoremovemos:
if let position = find(selected, items[indexPath.row]) {
selected.removeAtIndex(position)
}
O código final do método vai permitir incluir ou remover um elemento
selecionadoemnossoarray:
func tableView(tableView: UITableView,
didSelectRowAtIndexPath indexPath: NSIndexPath) {
let cell = tableView.cellForRowAtIndexPath(indexPath)
if cell == nil {
return
}
if (cell!.accessoryType ==
UITableViewCellAccessoryType.None) {
cell!.accessoryType =
UITableViewCellAccessoryType.Checkmark
selected.append(items[indexPath.row])
} else {
cell!.accessoryType = UITableViewCellAccessoryType.None
if let position = find(selected, items[indexPath.row]) {
selected.removeAtIndex(position)
}
150

## Página 157

CasadoCódigo Capítulo10. Relacionamentoumparamuitos: listadealimentos
}
}
Lembrando, nossa função de adicionar cria a refeição, seta os itens sele-
cionadoseosimprime:
@IBAction func add() {
if nameField == nil || happinessField == nil {
return
}
let name = nameField!.text
let happiness = happinessField!.text.toInt()
if happiness == nil {
return
}
let meal = Meal(name: name, happiness: happiness)
meal.items = selected
println(
"eaten: \(meal.name) \(meal.happiness) \(meal.items)")
if delegate == nil {
return
}
delegate!.add(meal)
if let navigation = self.navigationController {
navigation.popViewControllerAnimated(true)
}
}
Testamosnossaaplicaçãoeagorasomoscapazesdecomer cookies de
óleo de coco , selecionar e desselecionar diversos itens e, ao adicionar a
refeição final, temos no log o resultado com a impressão de quantos itens
estavamemnossarefeição:
151

## Página 158

10.5. Resumo CasadoCódigo
10.5 Resumo
Vimos como podemos adicionar umaTableView em um controller
existenteeconectá-laaoseu data source eseu delegateusandoo pat-
tern Observer. Vimos também como receber eventos de seleção em nosso
delegateecomissoutilizaraenum UITableViewCellAccessoryType
para marcar as células como selecionadas. Armazenamos as células selecio-
nadas e removemos as desselecionadas de um array que reflete tais escolhas
dousuário.
Para a remoção, foi importante conhecer mais de um protocolo bastante
utilizado para usar com coleções: a capacidade de dois itens serem compa-
rados com o
==,op r o t o c o l oEquatable. Utilizamos a funçãofind ea
removeAtPositionparabuscareremoverumelementodenossoarray.
Por fim, usamos esse array logo após instanciar nossa refeição para pre-
encheroscamposqueforamescolhidos.
152

## Página 159

Capítulo11
Criandonovositens
Chegouahoradepermitiraousuáriocriarnovositens. Paraisso,adicionare-
m o su mn o v oViewController q u er e p r e s e n t a r áu mf o r m u l á r i o .E l et e r á
o campo com o nome e o número de calorias desse item, além de um botão
de adicionar. Ao concluir a operação no formulário, devemos voltar para a
teladeediçãodarefeição.
Jáconhecemostudoisso,portantoveremosumanovamaneiraderealizar
o
push,alémdeaproveitaraoportunidadeparaexercitartudooquefizemos
anteriormente. Citamosanteriormenteumdosproblemasdemanutençãode
código ao lidar com diversos
segues visuais, o código pode ficar cheio de
clá usulasdoti poif,comumacomplexidadealta.
Uma outra alternativa, muito citada por desenvolvedores sêniores, está
ligada à navegação entre telas de maneira programática. Da mesma maneira
como fizemos um
pop para desempilhar uma tela, utilizaremos umpush
(ousimilar)paraempilharumatela.

## Página 160

CasadoCódigo
Nosso primeiro passo é criar a representação visual de nosso
viewcontroller, mas espere. Dessa vez não puxaremos ocontroller
paranosso storyboard.
BoapráticaouCodesmell? OStoryboardéumasolu-
çãodobemoudomal?
O Storyboardveio como alternativa para a criação de cada view se-
paradamente,eletambémfacilitaoarrastaesoltacomomaneiradepro-
gramaraiteraçãoentreviews. Porumlado,essetrabalhoficamuitosim-
ples;poroutro,eleacabaforçandoacriaçãodecódigocomdeterminadas
práticas que não são consideradas as melhores (uma séries de
ifs,p o r
exemplo).
Alémdisso,comopassardotempoostoryboardpodeficarcomtan-
tas telas que fica difícil manter todas as conexões visualmente compre-
ensíveis.
O maior problema do storyboard acontece quando trabalhamos em
equipe: quandoduaspessoasoalteramdemaneiraincompatível. Seráo
trabalho de um deles de fazer o processo demergena mão. Essa pessoa
deverá alterar um
xml q u ed e s c r e v ea sc e n a s ,p o i soe d i t o rv i s u a ln ã o
serácapazdemostrarasdiferenças.
Como regra geral, em projetos mais simples, com menos views, o
usodostoryboardpodenãocomprometeramanutençãodeseuprojeto.
Aqui aprenderemos tanto a maneira visual com o storyboard quanto a
programáticacomarquivos
Xib(antigos nib).
Vamos então isolar e criar um arquivo visual separado para esse nosso
viewcontroller,oarquivovisual(nasversõesmaisrecentesdoiOS)pos-
sui a extensão XIB. Portanto, no grupoviews, escolhemos o menuFile,
New, iOS, Source, Cocoa Touch Class , NewItemViewController,
UIViewController, Also create XIB File e Swift:
154

## Página 161

CasadoCódigo Capítulo11. Criandonovositens
Eleécriadononossogrupode views. Notequetemosagoradoisarqui-
vos,o XIB:
155

## Página 162

CasadoCódigo
Eo controllerquejáconhecemos:
Comotantoo controllerquantoo xibforamcriadosnomesmodi-
retório,vamosmovero viewcontrollerdamesmamaneiracomofizemos
156

## Página 163

CasadoCódigo Capítulo11. Criandonovositens
anteriormente,movendodiretamentenodiretório,removendoareferênciae
adicionandonovamentepeloXcode.
Emnosso XIB,selecionesua Viewclicandonoíconebrancoàesquerda
e escolha o tamanho do iPhone que estamos utilizando. Adicionamos agora
os campos do formulário de um
item, que são name e calories,eu m
bo tãodeco nfirmarincl usão ,chamadoadd:
157

## Página 164

CasadoCódigo
158

## Página 165

CasadoCódigo Capítulo11. Criandonovositens
Lembre-se de mudar o teclado do campocalories para Decimal e
colocarplaceholdernosdo iscam pos:sundubue 10.
159

## Página 166

CasadoCódigo
No XIB, conferimos que ao selecionar ofile owner sua identidade
éon o s s oNewItemViewController. Podemos até usar o assistant
editorparaconferirqueaconexãoaindaestáfeita:
Na nossa tela de adicionar nova refeição, dentro dostoryboard, va-
mos agora colocar o botão para conseguirmos fazer a navegação para esta
telanova. Poderíamosfazeracriaçãodestebotãodeformavisual,arrastando
oc o m po n e n t ep a r aat e l ad i r e t on o
storyboard, porém desta vez faremos
programaticamente.
Abrimos nosso ViewController. Dentro dele, sobrescrevemos o mé-
todo viewDidLoad, onde criaremos umUIBarButtonItem. Para criar-
mos um UIBarButtonItem, precisamos dizer qual o texto que queremos
nobotão( title),qualoforma to( style),quemdeveserchamadoaocli-
carmosnele( target)equalaaçãoquequeremosexecutarnesteobjetoque
forchamado( action).
override func viewDidLoad() {
let newItemButton = UIBarButtonItem(title: "new item",
style: UIBarButtonItemStyle.Plain,
target: self,
action: ?????)
}
Mas como podemos passar a chamada de um método para o botão exe-
cutar? Nãopodemoschamarométododireto, poisdessemodoeleseráexe-
160

## Página 167

CasadoCódigo Capítulo11. Criandonovositens
cutado no momento em que o chamarmos. Precisamos que o botão chame
o método. Para isto, criamos umSelector,p a s s a n d oc o m op a r â m e t r oo
nomedométodoquequeremosquesejachamado:
override func viewDidLoad() {
let newItemButton = UIBarButtonItem(title: "new item",
style: UIBarButtonItemStyle.Plain,
target: self,
action: Selector("showNewItem"))
}
Adicionamos também o botão no lado direito de nossoNavigation
Controller:
override func viewDidLoad() {
let newItemButton = UIBarButtonItem(title: "new item",
style: UIBarButtonItemStyle.Plain,
target: self,
action: Selector("showNewItem"))
navigationItem.rightBarButtonItem = newItemButton
}
Rodamosaaplicaçãoepodemosverqueobotãofoicriadocomsucesso:
161

## Página 168

CasadoCódigo
162

## Página 169

CasadoCódigo Capítulo11. Criandonovositens
Criamos o código da função que abrirá a tela denew item em nosso
ViewController,imprimindoumamensagemdeteste:
@IBAction func showNewItem() {
println("new item")
}
Etestamosnossaaplicação,obotãoaparece,eaoclicarmosnelevemosa
mensagem de log. Perceba o poder de criar views programaticamente: você
pode customizar todas as características de seu programa dinamicamente.
Vale como regra geral desenhar o que é fixo via arrasta e solta (interface
builder); e o que é customizado, dinâmico, acabamos fazendo programati-
camente,comoporexemploumbotãoquesóaparecequandoousuárioestá
logado.
11.1 Pushando views para a pilha programati-
camente
Agora estamos prontos para pegar nosso navegador e mostrar a tela
NewItemViewController:
@IBAction func showNewItem() {
let newItem = ???
if let navigation = navigationController {
navigation.pushViewController(newItem, animated: true)
}
}
Precisamos criar nossocontroller, mas lembre-se que estamos pro-
gramando orientado a objetos e nossoNewItemViewController éu m a
classe: bastainstanciá-la!
@IBAction func showNewItem() {
let newItem = NewItemViewController()
if let navigation = navigationController {
navigation.pushViewController(newItem, animated: true)
}
}
163

## Página 170

11.1. Pushandoviewsparaapilhaprogramaticamente CasadoCódigo
Testamose,aoclicarnobotão,temosumatelapreta!
O que acontece? Nós pedimos para instanciar o
NewItemViewController mas ninguém falou qual arquivo xib era
para ser usado. O xib é a nova versão do arquivo nib,p o r t a n t o ,a o
construirmos nosso NewItemViewController, dizemos qual arquivo de
viewqueremosqueeleleia:
@IBAction func showNewItem() {
let newItem = NewItemViewController(
nibName: "NewItemViewController", bundle: nil)
if let navigation = navigationController {
navigation.pushViewController(newItem, animated: true)
}
}
164

## Página 171

CasadoCódigo Capítulo11. Criandonovositens
Testamosaaplicaçãoe,mesmosemcriaro segue,fomoscapazesdama-
nipular a tela atual! Note que, se fosse importante passar algum argumento
para nosso controller, bastaria chamar o construtor passando o argu-
mento a mais (e criá-lo em nossa classe, claro), algo muito mais educado do
queficarsetandopropriedadesapósaconstrução.
11.2 Voltandodeumpushprogramático
Precisamos agora voltar para a nossa tela anterior ao clicar no botão
de confirmação. Já conhecemos o código do
pop, logo, em nosso
NewItemViewController.swift colocamos a função addNewItem.
Além disso, definiremos as duas variáveis que nos ajudarão a ler os campos
doitemnovo:
class NewItemViewController: UIViewController {
@IBOutlet var nameField:UITextField?
@IBOutlet var caloriesField:UITextField?
165

## Página 172

11.2. Voltandodeumpushprogramático CasadoCódigo
@IBAction func addNewItem() {
}
}
Usamos o arrasta da bolinha para conectarmos osoutletsea actioncom
oscam posdetextoeobo tão .
Executamoso pop:
@IBOutlet var nameField:UITextField?
@IBOutlet var caloriesField:UITextField?
@IBAction func addNewItem() {
if let navigation = navigationController {
navigation.popViewControllerAnimated(true)
}
}
166

## Página 173

CasadoCódigo Capítulo11. Criandonovositens
Agoralemososvaloresdoscamposecriamosumnovoitem:
@IBAction func addNewItem() {
let name = nameField.text
let calories = caloriesField.text
let item = Item(name: name, calories: calories)
if let navigation = navigationController {
navigation.popViewControllerAnimated(true)
}
}
Algumas coisas não compilam, primeiro devemos verificar valores opci-
onais:
@IBAction func addNewItem() {
if nameField == nil || caloriesField == nil {
return
}
let name = nameField!.text
let calories = caloriesField!.text
let item = Item(name: name, calories: calories)
if let navigation = navigationController {
navigation.popViewControllerAnimated(true)
}
}
Eagora, caloriesaindaé String! Queremosconverterpara Double,
procuramos o toDouble ev e m o sq u ee l en ã oe x i s t en ac l a s s ed eString
padrão. Issopoisconversãodepontodecimalestáligadaàlocalizaçãoeinter-
nacionalização. No nosso caso, usaremos o padrão da linguagem Objective
C,quejápossuíaumaString(
NSString)comométododecon versão .Cri-
amosainstânciadeuma NSStringeconvertemos:
@IBAction func addNewItem() {
if nameField == nil || caloriesField == nil {
return
}
167

## Página 174

11.3. Invocandoumdelegatedeformaprogramática CasadoCódigo
let name = nameField!.text
let calories =
NSString(string: caloriesField!.text).doubleValue
let item = Item(name: name, calories: calories)
if let navigation = navigationController {
navigation.popViewControllerAnimated(true)
}
}
Testamos a aplicação e ela vai e vem,mas ainda não notificamos a tela
paraaqualvoltamoscomodadodonovoitemqueacabadeseradicionado.
Estánahoradefazernosso delegate.
11.3 Invocando um delegate de forma progra-
mática
Assimcomofizemosantes,queremosnotificaratelaquenosinvocoudeque
o trabalho foi finalizado e temos um novo item para adicionar nela. Vamos
criaroprotocolodenosso
delegate,o AddAnItemDelegate:
protocol AddAnItemDelegate {
func addNew(item:Item)
}
E o implementamos, adotamos o AddAnItemDelegate em nosso
ViewController:
class ViewController: UIViewController, UITableViewDataSource,
UITableViewDelegate, AddAnItemDelegate {
// ...
func addNew(item: Item) {
items.append(item)
}
// ...
168

## Página 175

CasadoCódigo Capítulo11. Criandonovositens
}
Precisamos agora atualizar nossa tabela, mas onde está
nossa tableView?Q u a n d o o controller era do tipo
UITableViewController era fácil: ele já vinha com uma tabela.
Agoraprecisamoscriarumnovooutleteconectá-loanossatabela:
@IBOutlet var tableView: UITableView?
func addNew(item: Item) {
items.append(item)
if tableView == nil {
return
}
tableView!.reloadData()
}
Nãoesquecemosdeconectarooutletusandoo drag and drop.
Como trabalhar agora no nossoNewItemViewController? Precisa-
mos de um delegate lá, logo, como um bom cidadão, recebemo-lo em
nossoinicializador:
class NewItemViewController: UIViewController {
let delegate:AddAnItemDelegate?
init(delegate:AddAnItemDelegate) {
self.delegate = delegate
}
// ...
}
Mas o compilador reclama. Ao definirmos nosso inicializador, pre-
cisamos invocar o inicializador de nossa classe pai. Com certeza! An-
tes, invocávamos o construtor que recebia o nibName. O que era o
nibName? O nome do arquivo que representa aview, a cena conectada
aeste viewcontroller,entãovamosinvocá-lologoapósconfigurarnosso
delegate:
169

## Página 176

11.3. Invocandoumdelegatedeformaprogramática CasadoCódigo
class NewItemViewController: UIViewController {
let delegate:AddAnItemDelegate?
init(delegate:AddAnItemDelegate) {
self.delegate = delegate
super.init(nibName: "NewItemViewController", bundle: nil)
}
// ...
}
E novamente o compilador reclama: dessa vez ele pede a criação de
um inicializador que receba um NSCoder. A c o n t e c eq u eac l a s s ep a i ,
UIViewController requer tal inicializador, portanto, vamos redefini-lo,
simplesmenteinvocandooconstrutordenossopai:
class NewItemViewController: UIViewController {
let delegate:AddAnItemDelegate?
init(delegate:AddAnItemDelegate) {
self.delegate = delegate
super.init(nibName: "NewItemViewController", bundle: nil)
}
required init(coder aDecoder: NSCoder) {
super.init(coder: aDecoder)
}
// ...
}
170

## Página 177

CasadoCódigo Capítulo11. Criandonovositens
Nomenclaturadeparâmetro
Mas que história é essa? Um parâmetro com dois nomes? O nome
internodonossoparâmetroé aDecoder,enquantoqueminvocanosso
inicializadorusaráonome coder.
O exemplo a seguir demonstra a utilização de um nome interno e
externoparadeixarclaroovalorqueestamosreferenciando:
class User {
init(name newName:String) {
println("creating a \(newName\)")
}
}
let guilherme = User(name: "guilherme")
Claro, agora precisamos invocar odelegate para adicionar um ele-
mento:
@IBAction func addNewItem() {
if nameField == nil || caloriesField == nil {
return
}
let name = nameField!.text
let calories =
NSString(string: caloriesField!.text).doubleValue
let item = Item(name: name, calories: calories)
if delegate == nil {
return
}
delegate!.addNew(item)
if let navigation = navigationController {
navigation.popViewControllerAnimated(true)
171

## Página 178

11.3. Invocandoumdelegatedeformaprogramática CasadoCódigo
}
}
Pronto. Naprática,oqueaconteceéqueinvocaremosoconstrutoremque
estamos interessados, alterando nossa antiga chamada de inicialização para
invocaroquerecebeum delegate,portantoemnosso ViewController:
@IBAction func showNewItem() {
let newItem = NewItemViewController(delegate: self)
if let navigation = navigationController {
navigation.pushViewController(newItem, animated: true)
}
}
N ossocódigodo ViewControllerficaassim:
import UIKit
protocol AddAMealDelegate {
func add(meal: Meal)
}
class ViewController: UIViewController, UITableViewDataSource,
UITableViewDelegate, AddAnItemDelegate {
var items = [ Item(name: "Eggplant Brownie", calories: 10),
Item(name: "Zucchini Muffin", calories: 10),
Item(name: "Cookie", calories: 10),
Item(name: "Coconut oil", calories: 500),
Item(name: "Chocolate frosting", calories: 1000),
Item(name: "Chocolate chip", calories: 1000)
]
@IBOutlet var nameField: UITextField!
@IBOutlet var happinessField: UITextField!
var delegate:AddAMealDelegate?
var selected = Array<Item>()
@IBOutlet var tableView: UITableView?
func addNew(item: Item) {
172

## Página 179

CasadoCódigo Capítulo11. Criandonovositens
items.append(item)
if tableView == nil {
return
}
tableView!.reloadData()
}
func tableView(tableView: UITableView,
numberOfRowsInSection section: Int) -> Int {
return items.count
}
func tableView(tableView: UITableView,
cellForRowAtIndexPath indexPath: NSIndexPath)
-> UITableViewCell {
let row = indexPath.row
let item = items[ row ]
var cell = UITableViewCell(style:
UITableViewCellStyle.Default,reuseIdentifier: nil)
cell.textLabel.text = item.name
return cell
}
func tableView(tableView: UITableView,
didSelectRowAtIndexPath indexPath: NSIndexPath) {
let cell = tableView.cellForRowAtIndexPath(indexPath)
if cell == nil {
return
}
if (cell!.accessoryType ==
UITableViewCellAccessoryType.None) {
cell!.accessoryType =
UITableViewCellAccessoryType.Checkmark
selected.append(items[indexPath.row])
} else {
cell!.accessoryType =
UITableViewCellAccessoryType.None
if let position =
173

## Página 180

11.3. Invocandoumdelegatedeformaprogramática CasadoCódigo
find(selected, items[indexPath.row]) {
selected.removeAtIndex(position)
}
}
}
override func viewDidLoad() {
let newItemButton = UIBarButtonItem(title: "new item",
style: UIBarButtonItemStyle.Plain,
target: self,
action: Selector("showNewItem"))
navigationItem.rightBarButtonItem = newItemButton
}
@IBAction func showNewItem() {
let newItem = NewItemViewController(delegate: self)
if let navigation = navigationController {
navigation.pushViewController(newItem, animated:true)
}
}
@IBAction func add() {
if nameField == nil || happinessField == nil {
return
}
let name = nameField!.text
let happiness = happinessField!.text.toInt()
if happiness == nil {
return
}
let meal = Meal(name: name, happiness: happiness!)
meal.items = selected
println(
"eaten: \(meal.name) \(meal.happiness) \(meal.items)")
if delegate == nil {
174

## Página 181

CasadoCódigo Capítulo11. Criandonovositens
return
}
delegate!.add(meal)
if let navigation = self.navigationController {
navigation.popViewControllerAnimated(true)
}
}
}
Enquantoisso,nosso NewItemViewController:
import UIKit
protocol AddAnItemDelegate {
func addNew(item:Item)
}
class NewItemViewController: UIViewController {
let delegate:AddAnItemDelegate?
init(delegate:AddAnItemDelegate) {
self.delegate = delegate
super.init(nibName: "NewItemViewController", bundle: nil)
}
required init(coder aDecoder: NSCoder) {
super.init(coder: aDecoder)
}
@IBOutlet var nameField:UITextField?
@IBOutlet var caloriesField:UITextField?
@IBAction func addNewItem() {
if nameField == nil || caloriesField == nil {
return
}
let name = nameField!.text
let calories =
NSString(string: caloriesField!.text).doubleValue
175

## Página 182

11.3. Invocandoumdelegatedeformaprogramática CasadoCódigo
let item = Item(name: name, calories: calories)
if delegate == nil {
return
}
delegate!.addNew(item)
if let navigation = navigationController {
navigation.popViewControllerAnimated(true)
}
}
}
Testamosnossaaplicaçãoe,àmedidaqueadicionamosnovositens,jáos
temosnanossalistadeitensaseremutilizadosparaacriaçãodeumarefeição.
176

## Página 183

CasadoCódigo Capítulo11. Criandonovositens
177

## Página 184

11.4. Resumo CasadoCódigo
11.4 Resumo
Vimos neste capítulo como criar um XIB, uma view de um
ViewController que pode ser reutilizada mais facilmente, e vimos
como definir o que nosso construtor recebe durante sua construção. Revi-
samos a criação de um formulário, opush eo pop programático, além do
usodeum delegateparanotificarnosso observerdeumatarefaexecutada
emnossatela.
178

## Página 185

Capítulo12
Mostrandoosdetalhesdeuma
refeiçãocomLongpress
Mas após adicionada, como conferimos os detalhes de cada refeição? Quais
ositensesuasrespectivascalorias?
Parafazermosisso,usaremosumrecursoquefrequentementeapareceem
aplicativos iOS, o Long Press : ao segurarmos o clique em uma linha de
nossatabela,queremosvisualizarateladedetalhes.
Precisamos primeiramente dizer que nossa célula consegue reconhecer
este tipo de interação e qual ação deve ocorrer quando for identificado o
evento de
Long Press . O responsável por fazer esse reconhecimento é o
“elemento visual reconhecedor de movimento de manter apertado”, literal-
mente o
UILongPressGestureRecognizer. Lembra quando criamos
nossacélulano MealsTableViewController?

## Página 186

CasadoCódigo
override func tableView(tableView: UITableView,
cellForRowAtIndexPath indexPath: NSIndexPath) ->
UITableViewCell {
let row = indexPath.row
let meal = meals[ row ]
var cell = UITableViewCell(
style: UITableViewCellStyle.Default,
reuseIdentifier: nil)
cell.textLabel.text = meal.name
return cell
}
Instanciamos o UILongPressGestureRecognizer e o adicionamos
ànossacélula:
override func tableView(tableView: UITableView,
cellForRowAtIndexPath
indexPath: NSIndexPath) -> UITableViewCell {
//...
let longPress =
UILongPressGestureRecognizer(/* parameters */)
cell.addGestureRecognizer(longPress)
return cell
}
M a sq u a ls e r áom é t o d oe x e c u t a d oq u a n d oou s u á r i om a n t i v e rod e d o
pressionado nesta célula? De alguma maneira, devemos falar nosso alvo, o
objeto a ser notificado (target)eom é t o d oas e ri n v o c a d o(action). Já
conhecemosessepar,oobjetoeo Selector:
override func tableView(tableView: UITableView,
cellForRowAtIndexPath indexPath: NSIndexPath) ->
UITableViewCell {
//...
let longPress = UILongPressGestureRecognizer(target: self,
action: Selector("showDetails"))
cell.addGestureRecognizer(longPress)
return cell
}
180

## Página 187

CasadoCódigo Capítulo12. MostrandoosdetalhesdeumarefeiçãocomLongpress
Criamosométodoparamostrarmaisdetalhesdarefeição:
func showDetails(){
}
Mas como saberemos qual refeição foi selecionada? Felizmente, o pró-
prio UILongPressGestureRecognizer guarda a informação sobre em
qual view o evento ocorreu, temos apenas que pedir o reconhecedor por
parâmetro:
func showDetails(recognizer: UILongPressGestureRecognizer){
}
Só precisamos agora indicar aoLongPressGestureRecognizer que
queremos recebê-lo no momento em que o métodoshowDetails for in-
vocado. Pararepresentarmosquequeremosreceberumparâmetrononosso
Selector,co loca m os":" (doispontos)nofinaldonomedométodo. Isto
éherançadoObjective-C,ondeindicávamosapassagemdeparâmetroscom
os ":".
override func tableView(tableView: UITableView,
cellForRowAtIndexPath indexPath: NSIndexPath) ->
UITableViewCell {
//...
let longPress = UILongPressGestureRecognizer(target: self,
action: Selector("showDetails:"))
cell.addGestureRecognizer(longPress)
return cell
}
Vamosmostrarosdetalhesdenossarefeição,masemqualmomentoque-
remosqueelesapareçam?Quandooeventode long press começou! Por-
tanto, verificamos o estado e colocamos umprintln para sabermos que
funcionou.
func showDetails(recognizer: UILongPressGestureRecognizer){
if recognizer.state == UIGestureRecognizerState.Began {
println("Long press")
181

## Página 188

12.1. Recuperandoondeocorreuumeventodelongpress CasadoCódigo
}
}
Vamos rodar. Ao efetuarmos oLong Press , clicando e segurando a
linhadatabeladaqualqueremosvermaisdetalhes,ologmostraamensagem:
12.1 Recuperando onde ocorreu um evento de
longpress
Agoratemosquerecuperarqualacélulaemqueocorreuo Long Press eo
seuconteúdo. Paraisso,primeiroextraímosdo recognizerquala viewà
qualeleestavaatrelado,nossacélula:
func showDetails(recognizer: UILongPressGestureRecognizer){
if recognizer.state == UIGestureRecognizerState.Began {
let cell = recognizer.view
println("Long press")
}
}
Agora que temos a célula, podemos buscar o índice dela em nossa
tableViewatravésdométodo indexPathForCell:
func showDetails(recognizer: UILongPressGestureRecognizer){
if recognizer.state == UIGestureRecognizerState.Began {
let cell = recognizer.view
182

## Página 189

CasadoCódigo Capítulo12. MostrandoosdetalhesdeumarefeiçãocomLongpress
let indexPath = tableView.indexPathForCell(cell)
println("Long press")
}
}
Mas, ao digitar a chamada para o método, o Xcode não consegue re-
conhecer o método pois aview não é nosso UITableViewCell, afinal,
um UILongPressGestureRecognizer pode ser aplicado para qualquer
tipo de UIView! Como nós, desenvolvedores, temos certeza de que temos
uma célula aí dentro referenciada pelaview, podemos fazer ocast para
UITableViewCell:
func showDetails(recognizer: UILongPressGestureRecognizer){
if recognizer.state == UIGestureRecognizerState.Began {
let cell = recognizer.view as UITableViewCell
let indexPath = tableView.indexPathForCell(cell)
println("Long press")
}
}
183

## Página 190

12.1. Recuperandoondeocorreuumeventodelongpress CasadoCódigo
Codesmell:cast
Semprequefazemosum castestamosdizendoquenós,comodesen-
volvedores,sabemosoqueestáacontecendo,eocompiladornão. Seisso
acontece,estamoscorrendorisco. Ocompiladorexisteparagarantirdi-
versas coisas, dentre elas, que não acessamos algo pensando que é outra
coisa. Ocastingpermitecometeresseerro(eestouraraaplicação).
Como fugir do cast? Em casos similares como esse, caso o
UILongPressGestureRecognizerfossegenéricomaspermitissedi-
zerotipodeclasseparaoqualfosseaplicado,definiríamosemsuacria-
ção que ele só pode trabalhar com
UITableViewCell e teríamos cer-
teza de que as views onde ele ocorreu são do tipoUITableViewCell.
Esse tipo de comportamento pode ser alcançado com o uso degenerics,
mascomoomesmoéumcomponentedabibliotecapadrãodoiOS,não
temoscomoalterarocódigoparatalbenefíciodecompilação.
Coma cell eu m atableView em mãos, somos capazes de descobrir
emquallinhaocorreuaação, masreparequeaIDEadicionaum ? deopci-
onal:
func showDetails(recognizer: UILongPressGestureRecognizer){
if recognizer.state == UIGestureRecognizerState.Began {
let cell = recognizer.view as UITableViewCell
let indexPath = tableView.indexPathForCell(cell)
let row = indexPath?.row
println("Long press")
}
}
Nãoqueremosopcionalecorrerrisco,logo, ifnele:
func showDetails(recognizer: UILongPressGestureRecognizer){
if recognizer.state == UIGestureRecognizerState.Began {
let cell = recognizer.view as UITableViewCell
let indexPath = tableView.indexPathForCell(cell)
184

## Página 191

CasadoCódigo Capítulo12. MostrandoosdetalhesdeumarefeiçãocomLongpress
if indexPath == nil {
return
}
let row = indexPath!.row
println("Long press")
}
}
Portanto,podemosextrairarefeiçãoquefoiclicada,buscando-aemnosso
array:
func showDetails(recognizer: UILongPressGestureRecognizer){
if recognizer.state == UIGestureRecognizerState.Began {
let cell = recognizer.view as UITableViewCell
let indexPath = tableView.indexPathForCell(cell)
if indexPath == nil {
return
}
let row = indexPath!.row
let meal = meals[ row ]
println("Long press")
}
}
Vamosmudaro printlnparamostraronomeeoníveldefe licidadeda
refeiçãoselecionada:
func showDetails(recognizer: UILongPressGestureRecognizer){
if recognizer.state == UIGestureRecognizerState.Began {
let cell = recognizer.view as UITableViewCell
let indexPath = tableView.indexPathForCell(cell)
if indexPath == nil {
return
}
let row = indexPath!.row
let meal = meals[ row ]
println("meal: \(meal.name) \(meal.happiness)")
185

## Página 192

12.2. Mostrandoosdetalhesemumalerta CasadoCódigo
}
}
Rodamos e agora o log mostra a refeição selecionada ao efetuarmos o
Long Press :
Estamosprontosparanossopróximopasso:mostrarosdadosnatelaatra-
vésdeumo u tr oController.
12.2 Mostrandoosdetalhesemumalerta
Para mostrarmos os detalhes de uma refeição selecionada, criaremos um
alerta,um UIAlertController,ouseja,um popupcomosdadosqueque-
remosmostrar:
func showDetails(recognizer: UILongPressGestureRecognizer){
if recognizer.state == UIGestureRecognizerState.Began {
let cell = recognizer.view as UITableViewCell
let indexPath = tableView.indexPathForCell(cell)
if indexPath == nil {
return
}
let row = indexPath!.row
let meal = meals[ row ]
let details = UIAlertController(/* parameters */)
}
}
186

## Página 193

CasadoCódigo Capítulo12. MostrandoosdetalhesdeumarefeiçãocomLongpress
Quaisparâmetrosdevemospassaraonossoalerta? Primeiro,otítulocom
ono medar efeiçãoeamensagemco moníveldefe licidade:
func showDetails(recognizer: UILongPressGestureRecognizer){
if recognizer.state == UIGestureRecognizerState.Began {
let cell = recognizer.view as UITableViewCell
let indexPath = tableView.indexPathForCell(cell)
if indexPath == nil {
return
}
let row = indexPath!.row
let meal = meals[ row ]
let details = UIAlertController(title: meal.name,
message: "Happiness: \(meal.happiness)",
/* extra parameter */ )
}
}
Masdevemosfalartambémqualotipodealertaquedesejamosmostrar,
oestilotradicional:
func showDetails(recognizer: UILongPressGestureRecognizer){
if recognizer.state == UIGestureRecognizerState.Began {
let cell = recognizer.view as UITableViewCell
let indexPath = tableView.indexPathForCell(cell)
if indexPath == nil {
return
}
let row = indexPath!.row
let meal = meals[ row ]
let details = UIAlertController(title: meal.name,
message: "Happiness: \(meal.happiness)",
preferredStyle: UIAlertControllerStyle.Alert)
}
}
Por fim, pedimos para mostrar nossocontroller de alerta através do
método presentViewController,animado. Nãoutilizamosoúltimopa-
187

## Página 194

12.2. Mostrandoosdetalhesemumalerta CasadoCódigo
râmetroparaessemétodo,entãoodesejamosvazio:
func showDetails(recognizer: UILongPressGestureRecognizer){
if recognizer.state == UIGestureRecognizerState.Began {
let cell = recognizer.view as UITableViewCell
let indexPath = tableView.indexPathForCell(cell)
if indexPath == nil {
return
}
let row = indexPath!.row
let meal = meals[ row ]
let details = UIAlertController(title: meal.name,
message: "Happiness: \(meal.happiness)",
preferredStyle: UIAlertControllerStyle.Alert)
presentViewController(
details, animated: true, completion: nil)
}
}
188

## Página 195

CasadoCódigo Capítulo12. MostrandoosdetalhesdeumarefeiçãocomLongpress
189

## Página 196

12.2. Mostrandoosdetalhesemumalerta CasadoCódigo
Mas e como fechamos os detalhes? Precisamos avisar nossa tela de que
queremosvoltarparaatelaanterioreremoveratelaatual.
Modal
Repareque,anteriormente,quandoprecisamosapresentarumanova
tela,utilizamosanavegaçãotradicional,com pushparamostraratelae
popparafechar. Fizemosissopoisqueríamosmantersempreohistórico
denavegação,porquaistelaspassamoseparaondevoltaríamos. Nocaso
do ActionController, queremos apenas mostrar o popup, sem pre-
cisar interferir no fluxo de navegação anterior, portanto este popup não
precisaentrarnapilhadenavegação. Paraestescasos,fazemosanavega-
ç ã od em o d o
Modal, apresentando a tela por cima da anterior, através
dosmétodo presentViewController(mostrar). Aresponsabilidade
detiraratelaapresentadaficaparaquemchamouomodal,istoé,nóste-
mos que lembrar de adicionar a
Action para permitir fechar o modal.
Desejamosadicionarumbotão“Ok”quepermitafecharnossatela. Como
fizemos anteriormente, vamos instanciá-lo passando diversos parâmetros,
en tr eosquaisotí tulo(
Ok)eoestilo( Cancel):
let details = UIAlertController(title: meal.name,
message: "Happiness: \(meal.happiness)",
preferredStyle: UIAlertControllerStyle.Alert)
let ok = UIAlertAction(title: "Ok",
style: UIAlertActionStyle.Cancel,
/* extra parameters */)
presentViewController(details, animated: true, completion: nil)
Emseguida,adicionamosobotãodecancelaremnossodetalhamento:
let details = UIAlertController(title: meal.name,
message: "Happiness: \(meal.happiness)",
preferredStyle: UIAlertControllerStyle.Alert)
190

## Página 197

CasadoCódigo Capítulo12. MostrandoosdetalhesdeumarefeiçãocomLongpress
let ok = UIAlertAction(title: "Ok",
style: UIAlertActionStyle.Cancel,
/* extra parameters */)
details.addAction(ok)
presentViewController(details, animated: true, completion: nil)
Mas temos ainda que falar que não queremos executar nada ao fechar
nossodiálogo,passando nilcomoparâmetro:
let details = UIAlertController(title: meal.name,
message: "Happiness: \(meal.happiness)",
preferredStyle: UIAlertControllerStyle.Alert)
let ok = UIAlertAction(title: "Ok",
style: UIAlertActionStyle.Cancel,
handler: nil)
details.addAction(ok)
presentViewController(details, animated: true, completion: nil)
Rodamos e agora podemos voltar para a lista através do botão deOk do
nosso popup:
191

## Página 198

12.2. Mostrandoosdetalhesemumalerta CasadoCódigo
192

## Página 199

CasadoCódigo Capítulo12. MostrandoosdetalhesdeumarefeiçãocomLongpress
12.3 Mostrandoosdetalhesdositens
Agora quejá conseguimos mostrar osdados básicos deuma refeição, vamos
acrescentartambémositensqueaquelarefeiçãotem. Pegamostodosositens
q u et e m o sn ar e f e i ç ã oec o n c a t e n a m o sn am e n s a g e md op o p u p .C o m ou m a
refeição pode ter mais do que um item, usamos um
for para efetuarmos a
concatenação. Acrescentamosnométodo showDetails:
var message = "Happiness: \(meal.happiness)"
for item in meal.items {
message += "\n * \(item.name) - calories: \(item.calories)"
}
let details = UIAlertController(title: meal.name,
message: message,
preferredStyle: UIAlertControllerStyle.Alert)
Bacana,temosagoratodoodetalhamentodenossasrefeiçõesmasnosso
métodoficoucomresponsabilidadesdemais. Alémdebuscaracélulaseleci-
onada,aindaprecisaserresponsávelporimprimirasinformaçõesetambém
mostraropopupcomodetalhamento. Saberasinformaçõesdedetalheséres-
ponsabilidade da própria refeição, logo, vamos extrair este comportamento
paraaclasse
Meal:
class Meal {
// ...
func details() -> String {
var message = "Happiness: \(self.happiness)"
for item in self.items {
message
+= "\n * \(item.name) - calories: \(item.calories)"
}
return message
}
}
193

## Página 200

12.3. Mostrandoosdetalhesdositens CasadoCódigo
Agorasóprecisamosutilizarestenovométododentrodo showDetails,
queficarádaseguinteforma:
func showDetails(recognizer: UILongPressGestureRecognizer){
if recognizer.state == UIGestureRecognizerState.Began {
let cell = recognizer.view as UITableViewCell
let indexPath = tableView.indexPathForCell(cell)
if indexPath == nil {
return
}
let row = indexPath!.row
let meal = meals[ row ]
let details = UIAlertController(title: meal.name,
message: meal.details(),
preferredStyle: UIAlertControllerStyle.Alert)
let ok = UIAlertAction(title: "Ok",
style: UIAlertActionStyle.Cancel,
handler: nil)
details.addAction(ok)
presentViewController(
details, animated: true, completion: nil)
}
}
Nosso controllernãoprecisamaissabercomofazerparaimprimiras
refeições. A única coisa de que ele precisa é invocar o métododetails da
classe Meal. Estaideiadenãoprecisarconhecerdetalhesdaimplementação
para conseguir executar a ação desejada é um conceito muito importante da
OrientaçãoaObjetoschamadode encapsulamento.
R o d a m o sec r i a m o su mn o v oi t e mc h a m a d ocheese com 100 ca-
lorias. Adicionamo-lo junto do cookie em uma nova refeição chamada
cheesecake. Efetuamoso Long Press etemosoresultado:
194

## Página 201

CasadoCódigo Capítulo12. MostrandoosdetalhesdeumarefeiçãocomLongpress
195

## Página 202

12.4. Resumo CasadoCódigo
12.4 Resumo
Vimosnestecapítulocomopodemosresponderaumeventodecliquelongo(
Long Press )ecomopodemosmostrarumpopuppersonalizadoutilizando
um UIAlertController. Tambémvimosquepodemosnavegarparaou-
trastelassemutilizar push,atravésdomodo Modale,nofinal,melhoramos
nosso código, separando as responsabilidades e encapsulando as funcionali-
dadesespecíficasemseusdevidoslugares.
196

## Página 203

Capítulo13
Alerta: optionalseerros
Aindatemosmuitoscódigosespalhadosquefazemverificaçõesparadetectar
seasvariáveisestãocomvaloresválidosantesdeexplodiraaplicação.
Ou sod eOptionals em Swift é muito interessante, mas como toda re-
ferênciaquepodesernula,seuusoéperigoso.
Vejamos o que podemos fazer agora para melhorar todos osifs que
retornam de nossas funções, e tratar os erros desconhecidos do sistema de
umamaneirauniforme,demodoqueousuárioentendaoqueaconteceu.
Primeiro, vamos à nossa tela de nova refeição, à qual adicionamos um
novo item, no
ViewController. Repare que, ao adicionarmos um novo
itememnossoarray,utilizamosocódigoaseguir:
func addNew(item: Item) {
items.append(item)
if tableView == nil {

## Página 204

CasadoCódigo
return
}
tableView!.reloadData()
}
Q u a lop e r i g od eu s a ru m!? É que sempre que usamos um! estamos
dizendo ao compilador que sabemos o que estamos fazendo, e que a apli-
cação vai parar se der algum problema de acesso. O acesso a uma variável
Optionalcom !éoequivalenteaoacessodeobjetostradicionalmentefeito
emoutraslinguagenscomoJava. Seareferênciafornula,aaplicaçãocrasheia.
Perigoso. Como não queremos isso, prometi a vocês não digitar jamais um
!,masacabamosusando-oaqui.
Apesardisso,comobonsprogramadores,devemosnosprotegeremtodo
onossoprograma. Sempreantesdeusarumareferênciaopcional,verificamos
seu valor com
if.Q u a lop r o b l e m ad o!, então? É que dependemos de
nós mesmos, temos que lembrar de usar oif, se esquecermos, ou se nos
enganarmos,aaplicaçãocrasheia.
Nãoqueremosdependerdealgotãofrágilquantonossaprópriamemória.
Porisso,vamosevitaro !semprequepossível: nãoqueremosqueaaplicação
crasheieenãoqueremoscorreroriscodeesquecernosso if.
A solução? Só quero chamar o método reloadData se a variável
tableView foi definida adequadamente, caso contrário não chame o mé-
todo:
func addNew(item: Item) {
items.append(item)
tableView?.reloadData()
}
O próprio compilador adiciona o if. S óe x e c u t a m o som é t o d o
reloadData se a referência para a tabela for válida. Como código, é bem
menosdigitação,ecomobonsprogram adores,nossoobjetivodevidaédigi-
taromínimopossível,certo? Errado. Nãosomospagosparadigitaromínimo
decaracteres,somospagosporumprodutodequalidade.
O código anterior possui um perigo tremendo: se a variável estiver de-
finida, tudo funciona como o esperado. Se não, ele adiciona no array e não
198

## Página 205

CasadoCódigo Capítulo13. Alerta: optionalseerros
atualiza a tabela. Inocente? Pensemos com mais cuidado: o usuário final re-
alizaumatarefacomoefetuarumatransferência:
func transfer(from:Account, to:Account, value:Double) {
from.withdraw(amount)
to.deposit(amount)
navigationController!.popViewControllerAnimated(true)
}
A única linha que não funcionouéaq u ea t u aliza a mensagem na tela.
Nessaversão,aaplicaçãocrasheiaeousuárioficasemsaberoqueaconteceu.
Jánaversãoadiante,dependemosdeodesenvolvedorselembrardefazerum
if:
func transfer(from:Account, to:Account, value:Double) {
from.withdraw(amount)
to.deposit(amount)
if navigationController == nil {
// display alert
return
}
navigationController!.popViewControllerAnimated(true)
}
M udamosparao optional chaining ,istoé,usandoa ?nolugarda
!:
func transfer(from:Account, to:Account, value:Double) {
from.withdraw(amount)
to.deposit(amount)
navigationController?.popViewControllerAnimated(true)
}
A linha novamente não funciona, opop não é feito, mas a transferência
jáfoiefetuada. Oqueousuáriofinalfaz,umavezquenãosabequealgodeu
errado? Eletransferenovamente.Caboom. Aaplicaçãonãocrasheia,masele
efetuaduasvezesumacoisaquesóqueriaefetuaruma.
Optional chaining ébonitomastãooumaisperigosoqueumcrash
desuaaplicação. Pioraindaseexi stelógicaapósumachamadade optional
199

## Página 206

13.1. Boaprática: eviteoptional,garantatudocomiflet CasadoCódigo
chaining! Ele potencializa o caso de esquecimento do desenvolvedor, que
comoqualquerserhumanoestáfadadoaoerro.
13.1 Boaprática:eviteoptional,garantatudo
comiflet
Masseambossãoruins,qualminhaalternativa? Jamaisutilizaro !sobqual-
quercircunstânciaejamaisusaro ?para optional chaining . Sãopala-
vrasfortes, masvalecomoquasesempre. Quasesemprevaleapenagarantir
quesuaaplicaçãonãoteráumcrashnofuturo.
Só tenho variáveis obrigatórias ou opcionais definidas como?,q u eéo
que forçamos até agora. Como extrair o valor de uma delas? Usando oif
let. Se não usamos optional chaining nem !, a única maneira de
extrair o valor é com oif let : não tem como o desenvolvedor esquecer o
if!
func addNew(item: Item) {
items.append(item)
if let table = tableView {
table.reloadData()
}
}
Será que Swift seria uma linguagem ainda mais segura se não existissem
o optional chaining eo !? Talvez,sóotempodirá.
Claro, um desenvolvedor preguiçoso, que prefere digitar menos e correr
maisrisco, podeargumentarqueassimestamosdigitandomais. Éverdade...
Edaí?
13.2 Tratando o erro com uma mensagem nova-
mente
Vamos aplicar a regra que definimos dosoptionals e tratar nossos erros.
Começamos com a função que mencionamos. Quando o usuário adiciona
um item, caso um erro aconteça, desejamos mostrar alguma mensagem de
erro:
200

## Página 207

CasadoCódigo Capítulo13. Alerta: optionalseerros
func addNew(item: Item) {
items.append(item)
if let table = tableView {
table.reloadData()
} else {
let alert = UIAlertController(title: "Sorry",
message: "Unexpected error.",
preferredStyle: UIAlertControllerStyle.Alert)
let ok = UIAlertAction(title: "Understood",
style: UIAlertActionStyle.Cancel,
handler: nil)
alert.addAction(ok)
presentViewController(
alert, animated: true, completion: nil)
}
}
Paratestarmos,precisamosdesconectarnosso outlet,simulandoumerro
deconfiguraçãooude runtime. Vamosaonosso storyboard,selecionamos
o UITableView da tela de nova refeição e, na parte da direita, onde temos
o connections inspector ,removemoso outletclicandono x.
A go ratestamosaa plicaçãoetemosamensagemdeerr o:
201

## Página 208

13.3. Boaprática: mensagensdeerrodescritivas CasadoCódigo
13.3 Boa prática: mensagens de erro descriti-
vas
Apesardoerro,amensagempodedeixarousuárioconfuso. Nasituaçãoque
vimos,elaindicaquealgoinesperadoaconteceu,masoquê? Ecomoousuário
devesesentiremrelaçãoaisso? Qualseupróximopasso?
Escolhasuasmensagensdeerrodeformabastantedescritiva. Aqui,ape-
sar de não ser possível atualizar a tabela, conseguimos adicionar o elemento
em nosso array, por exemplo um
sundubu.A oc l i ca rm o se mback, vemos
queoresultadohaviasidopositivo,mesmotendosidomostradaamensagem
deerro:
202

## Página 209

CasadoCódigo Capítulo13. Alerta: optionalseerros
203

## Página 210

13.4. Refatoração: tratandodiversoserros CasadoCódigo
Portanto, mudamos nossa mensagem de erro para indicar essa situação
claramente, dizendo que o item foi adicionado com sucesso mas algum erro
inesperadoocorreu:
func addNew(item: Item) {
items.append(item)
if let table = tableView {
table.reloadData()
} else {
let alert = UIAlertController(title: "Sorry",
message: "Unexpected error, but the item was added.",
preferredStyle: UIAlertControllerStyle.Alert)
let ok = UIAlertAction(title: "Understood",
style: UIAlertActionStyle.Cancel,
handler: nil)
alert.addAction(ok)
presentViewController(
alert, animated: true, completion: nil)
}
}
13.4 Refatoração:tratandodiversoserros
Sódeimaginarocódigoquecolocaremosaquijábateumapreguiça... vaificar
tão repetitivo. Não só isso, nosso controller já tem tantas responsabilidades
distintas; devemos bater na tecla de uma classe, uma responsabilidade. Se-
riatãobomsepudéssemosresumiressaresponsabilidadeemumainvocação
simplesdemostrarmensagemdealerta:
func addNew(item: Item) {
items.append(item)
if let table = tableView {
table.reloadData()
} else {
Alert().show("Unexpected error, but the item was added.")
}
}
204

## Página 211

CasadoCódigo Capítulo13. Alerta: optionalseerros
Se queremos simplificar, podemos. Extraímos o código de mostrar um
alert deerroparaumaclasseespecíficaemnossogrupo views:
class Alert {
func show(message:String) {
let details = UIAlertController(title: "Sorry",
message: message,
preferredStyle: UIAlertControllerStyle.Alert)
let cancel = UIAlertAction(title: "Understood",
style: UIAlertActionStyle.Cancel,
handler: nil)
details.addAction(cancel)
presentViewController(
details, animated: true, completion: nil)
}
}
O código ainda não compila. Primeiro devemos importarUIKit,p o i s
usamosdiversoscomponentesde UInele:
import UIKit
Agora temos um último erro de compilação, uma vez que o método
presentViewController não existe por aqui. Ele está definido em
um UIViewController. Precisamos de nosso controller aqui? Ótimo,
recebemo-lonainicialização,afinal,somos goodcitizens:
class Alert {
let controller:UIViewController
init(controller:UIViewController) {
self.controller = controller
}
func show(message:String) {
let details = UIAlertController(title: "Sorry",
message: message,
preferredStyle: UIAlertControllerStyle.Alert)
let cancel = UIAlertAction(title: "Understood",
style: UIAlertActionStyle.Cancel,
205

## Página 212

13.5. Parâmetrosdefault CasadoCódigo
handler: nil)
details.addAction(cancel)
controller.presentViewController(details,
animated: true, completion: nil)
}
}
Aocriarmosnossoalerta,devemospassarocontroller:
func addNew(item: Item) {
items.append(item)
if let table = tableView {
table.reloadData()
} else {
Alert(controller: self).show(
"Unexpected error, but the item was added.")
}
}
Bonito. Testamos agora e, após toda essa refatoração para simplificar
nossocódigofinal,continuamoscomnossamensagemdeerrofuncionando.
O objetivo de toda refatoração é extrair uma parte suja, simplificando-a de
algumamaneiraeaomesmotempofacilitandoautilizaçãodaquelapartepor
quem já a utilizava. É o que fizemos aqui: isolamos uma responsabilidade e
simplificamosocódigodequemprecisainvocá-la.
13.5 Parâmetrosdefault
Muitas vezes utilizaremos a mesma mensagem de erro. Nesses casos, pode-
mosutilizarumvalorpadrãoparanossoparâmetro:
func show(message:String = "Unexpected error.") {
let details = UIAlertController(title: "Sorry",
message: message,
preferredStyle: UIAlertControllerStyle.Alert)
let cancel = UIAlertAction(title: "Understood",
style: UIAlertActionStyle.Cancel,
handler: nil)
206

## Página 213

CasadoCódigo Capítulo13. Alerta: optionalseerros
details.addAction(cancel)
presentViewController(
details, animated: true, completion: nil)
}
Agorapoderíamosinvocá-losemparâmetros:
func addNew(item: Item) {
items.append(item)
if let table = tableView {
table.reloadData()
} else {
Alert(controller: self).show()
}
}
Mas se desejamos manter a mensagem customizada de antes, agora que
utilizamos valores default somos obrigados a dizer qual parâmetro esta-
mosrepassando:
func addNew(item: Item) {
items.append(item)
if let table = tableView {
table.reloadData()
} else {
Alert(controller: self).show(message:
"Unexpected error, but the item was added.")
}
}
207

## Página 214

13.6. Boaprática: SingleResponsibilityPrinciple,PrincípiodeResponsabilidadeÚnica CasadoCódigo
Codesmell:diversosparâmetroscomvalorpadrão
Pormaisquepareçainteressanteutilizardiversosparâmetroscomva-
lorpadrão,temosalgunscuidadosatomar. Primeiro,assimcomoemdi-
versasoutraslinguagens,osparâmetrosopcionaissãosempreosúltimos
de uma função. Segundo, um número grande de parâmetros opcionais
em geral indica uma grande quantidade de possibilidades de resultados
diferentes para uma invocação à sua função e, se esse for o caso, a com-
plexidadedométodotambémpodeestaralta.
Tomecuidadocomparâmetrosopcionais:seeleindicaumaaltacom-
plexidade (ciclomática) do seu método, refatore. Se ele indica somente
númerosou
Stringspadrãoquenãoentramemcláusulascondicionais
(como ifs, forse switchs),menosproblemas.
Uma das maneiras de refatorar um código com muitos parâmetros
opcionais (principalmente um construtor com tais características) é a
utilizaçãodo design pattern
Builder.
13.6 Boaprática: SingleResponsibilityPrinci-
ple,PrincípiodeResponsabilidadeÚnica
É considerada uma boa prática a utilização de uma única responsabilidade
por unidade de código. Em Orientação a Objetos, é comum que os métodos
estejam agrupados em uma classe de acordo com uma determinada funcio-
nalidade. Por exemplo, os métodos deentrada e saída devem ficar em uma
classediferentequeasdeinterfacecomousuário. Éporissomesmoquecri-
amosesseisolamentobásicodaclasse
Alertdorestodenossoprograma.
Agora podemos aplicar nossoAlert ao u t r a sp a r t e sd oc ó d i g o .V a m o s
primeiroao showNewItemdenosso ViewController:
@IBAction func showNewItem() {
let newItem = NewItemViewController(delegate: self)
if let navigation = navigationController {
navigation.pushViewController(newItem, animated:true)
208

## Página 215

CasadoCódigo Capítulo13. Alerta: optionalseerros
}
}
Aquidesejamosmostraramensagempadrãodeerro:
@IBAction func showNewItem() {
let newItem = NewItemViewController(delegate: self)
if let navigation = navigationController {
navigation.pushViewController(newItem, animated:true)
} else {
Alert(controller: self).show()
}
}
13.7 Casos mais complexos de tratamento de
erro
Namesmaclasse,temosafunção add,umcasomaiscomplicado:
if nameField == nil || happinessField == nil {
return
}
Eagora? Duascondições?
if let nameField = nameField {
if let happinessField = happinessField {
let name = nameField.text
let happiness = happinessField.text.toInt()
// ...
}
}
209

## Página 216

13.8. Codesmell: Nestedifs CasadoCódigo
ifletx=x
Ac o n s t r u ç ã oif let permite definir uma variável com o mesmo
nomedavariávelopcionalqueestamostestando. Issopodepareceruma
ótima funcionalidade, mas se o nome da variável opcional é igual ao
nome da variável que tem valor, isso significa que um programador de-
savisadopodeacreditarquevariáveltemvalor. Perigoso.
ComoemSwiftseránecessárioousodo
!,ou ?,ou letparaextrair
o valor, o compilador pegará o erro do desenvolvedor (exceto em casos
emqueainferênciadetipopodeser“esperta”epassarumarasteiranele).
Em outras linguagens, é ainda mais importante que uma variável in-
diqueseseuvaloréopcionalousempreválido.
13.8 Codesmell:Nestedifs
Nested ifs ? Bem feio. Ainda mais agora que precisamos de um terceiro
ifpararesgataroterceirovalor,ointeiro:
if let nameField = nameField {
if let happinessField = happinessField {
let name = nameField.text
let happiness = happinessField.text.toInt()
if let happiness = happiness {
// ...
}
}
}
Haja coração para aturar esse código: cinco linhas pequenas com três
ifs, cinco lets,q u a t r onames, seis happiness e seis Fields.O s
nested ifs ( ifsaninhados)sãoumindicadordequehámuitaresponsa-
bilidadeecomplexidadeemnossocódigo. Paremosuminstanteefaçamosa
perguntaanósmesmos: oquequeremosaqui?
Dado um formulário, quero umMeal. Ótimo, isolemos esse comporta-
mento,aresponsabilidadede,dadoumformulário UI,extrairum Meal:
210

## Página 217

CasadoCódigo Capítulo13. Alerta: optionalseerros
func getMealFromForm() -> Meal {
}
Claro,faltaimplementarométodo,quedeixaremoscomoestavaantes:
func getMealFromForm() -> Meal {
if nameField == nil || happinessField == nil {
return
}
let name = nameField!.text
let happiness = happinessField!.text.toInt()
if happiness == nil {
return
}
let meal = Meal(name: name, happiness: happiness!)
meal.items = selected
println(
"eaten: \(meal.name) \(meal.happiness) \(meal.items)")
}
Quandopercebemosquetemosalgoinválido,devolvemosvazio;nocaso
desucesso,devolvemosnosso meal:
func getMealFromForm() -> Meal {
if nameField == nil || happinessField == nil {
return nil
}
let name = nameField!.text
let happiness = happinessField!.text.toInt()
if happiness == nil {
return nil
}
let meal = Meal(name: name, happiness: happiness!)
meal.items = selected
println(
211

## Página 218

13.8. Codesmell: Nestedifs CasadoCódigo
"eaten: \(meal.name) \(meal.happiness) \(meal.items)")
return meal
}
Mas calma, se podemos retornar ummeal ou não, o retorno deve ser
marcadocomoopcional,paraqueminvocaressemétodolembrardetrataro
casodevazio:
func getMealFromForm() -> Meal? {
if nameField == nil || happinessField == nil {
return nil
}
let name = nameField!.text
let happiness = happinessField!.text.toInt()
if happiness == nil {
return nil
}
let meal = Meal(name: name, happiness: happiness!)
meal.items = selected
println(
"eaten: \(meal.name) \(meal.happiness) \(meal.items)")
return meal
}
Agorainvocamosométodoadequadamente:
@IBAction func add() {
if let meal = getMealFromForm() {
if delegate == nil {
return
}
delegate!.add(meal)
if let navigation = self.navigationController {
navigation.popViewControllerAnimated(true)
}
212

## Página 219

CasadoCódigo Capítulo13. Alerta: optionalseerros
}
}
Podemosmelhoraravalidaçãodo delegatecomum if let :
@IBAction func add() {
if let meal = getMealFromForm() {
if let meals = delegate {
meals.add(meal)
if let navigation = self.navigationController {
navigation.popViewControllerAnimated(true)
}
}
}
}
Apesar de não ser o ideal, não vamos refatorar mais nosso código. Os
nested ifs que restaram podem ser refatorados, principalmente criando
algum tipo de framework para lidar comdelegates e navegação. O que
faremosémostrarumalertanocasodeproblemadenavegação:
@IBAction func add() {
if let meal = getMealFromForm() {
if let meals = delegate {
meals.add(meal)
if let navigation = self.navigationController {
navigation.popViewControllerAnimated(true)
} else {
Alert(controller: self).show(
message: "Unexpected error, but the meal was added.")
}
}
}
}
Emcasodesucesso,saímosdafunção;casosurjaoutrafalha,mostramos
amensagempadrãodeerro:
@IBAction func add() {
if let meal = getMealFromForm() {
213

## Página 220

13.9. Resumo CasadoCódigo
if let meals = delegate {
meals.add(meal)
if let navigation = self.navigationController {
navigation.popViewControllerAnimated(true)
} else {
Alert(controller: self).show(
message: "Unexpected error, but the meal was added.")
}
return
}
}
Alert(controller: self).show()
}
13.9 Resumo
Vimoscomoousodooptionalsépoderosoeaomesmotempoextremamente
perigoso. Conversamossobreoperigodo !equalomotivoparaevitá-loao
máximo. Analisamosousodo ?parafazer optional chaining eosperi-
gosaindamaisgravesemsuautilização. Porfim,optamosporusaro if let
sempre,comoaúnicaalternativaseguraaotrabalharcomvaloresopcionais.
Valelembrarquesempredaremospreferênciaparavaloresobrigatórios.
Orestodocódigocriadoatéagoraemnossosoutroscontrollerseclasses
podesebeneficiardamesmatécnica,naqualevitamos copyepasteefa v o r e-
cemosaextraçãodecódigocomum,deresponsabilidades.
Aprendemosoprincípioderesponsabilidadeúnica,fundamentalparafa-
cilitaramanutençãodenossocódigoemlongoprazo.
Nomeiodocaminho,aprendemoscomocriarparâmetrosopcionaiseos
cuidadosquedevemostomarcomeles. Isolamosocódigodevisualizaçãode
alertasemumaclassequefoireutilizadaemtodosospontosdenossaaplica-
çãoemquevaloresopcionaissãoencontrados.
214

## Página 221

Capítulo14
Removendoumarefeição
14.1 Açõesdestrutivaseestilos
Nosso próximo passo é permitir que o usuário final seja capaz de remover
uma refeição quando entrar com algum dado errado. Para isso, primeiro al-
teramosnossobotãoqueéreferenciadoatravésdeumavariávelchamada
ok
para cancel,alémdemudarseunomepara Cancel:
func showDetails(recognizer: UILongPressGestureRecognizer){
if recognizer.state == UIGestureRecognizerState.Began {
let cell = recognizer.view as UITableViewCell
let indexPath = tableView.indexPathForCell(cell)
if indexPath == nil {
return
}
let row = indexPath!.row

## Página 222

14.1. Açõesdestrutivaseestilos CasadoCódigo
let meal = meals[ row ]
let details = UIAlertController(title: meal.name,
message: meal.details(),
preferredStyle: UIAlertControllerStyle.Alert)
let cancel = UIAlertAction(title: "Cancel",
style: UIAlertActionStyle.Cancel,
handler: nil)
details.addAction(cancel)
presentViewController(
details, animated: true, completion: nil)
}
}
Agoraadicionamosumnovobotão,chamado Remove:
let remove = UIAlertAction(title: "Remove",
style: UIAlertActionStyle.Cancel,
handler: nil)
details.addAction(remove)
let cancel = UIAlertAction(title: "Cancel",
style: UIAlertActionStyle.Cancel,
handler: nil)
details.addAction(cancel)
Note que temos um problema: uma ação decancel não é destrutiva,
enquantoumade removedestróialgo,éumaaçãoperigosaeousuáriodeve
entender isso. Além disso, é muito estranho que um alerta tenha duas ações
de cancelar, não faz sentido! Existe um estilo chamadoDestructive que
indicaqueaaçãoserádestru tiva,eéelequeusar emos.
let remove = UIAlertAction(title: "Remove",
style: UIAlertActionStyle.Destructive,
handler: nil)
details.addAction(remove)
let cancel = UIAlertAction(title: "Cancel",
style: UIAlertActionStyle.Cancel,
216

## Página 223

CasadoCódigo Capítulo14. Removendoumarefeição
handler: nil)
details.addAction(cancel)
Agora sim a caixa de diálogo nos diz que ao clicarmos emRemove algo
perigosoacontecerá:
14.2 Passandoumafunçãocomocallback
Mas clicamos e nada acontece. Como assim? Claro, precisamos escrever a
funçãoqueseráinvocadapeloiOSquandoousuárioclicarem Remove.V a -
mosdefinirummétodochamado removeSelecteddentrodenossaclasse:
func removeSelected() {
println("removed the selected one")
}
Já passamos por outras situações em que dissemos para algum compo-
nente de UI que, ao efetuar uma tarefa, umObserver devia ser chamado,
passando tanto um objeto, comumente oself,eon o m ed om é t o d oa t r a -
v é sd eu mSelector -u m aString. String? Como assim? Um perigo
217

## Página 224

14.2. Passandoumafunçãocomocallback CasadoCódigo
só. Sequalquercoisamuda,a String nãoéinterpretadapelocompiladore
somentedescobrimoserrosemtempodeexecução.
Em vez de trabalharmos comselectors, algumas partes da API do
iOS nos permitem passar um bloco de código, uma função ou um método.
Podemos passar diretamente comohandler d en o s s aa ç ã ou m ar e f e r ê n c i a
paraafunção removeSelected:
let remove = UIAlertAction(title: "Remove",
style: UIAlertActionStyle.Destructive,
handler: removeSelected)
details.addAction(remove)
let cancel = UIAlertAction(title: "Cancel",
style: UIAlertActionStyle.Cancel,
handler: nil)
details.addAction(cancel)
Repare que não escrevemosremoveSelected(), que seria o equiva-
lenteainvocarafunção. Nãoqueremosinvocarafunção,queremossomente
p a s s a rar e f e r ê n c i ad af u n ç ã op a r aoUIAlertAction. Por isso, passamos
somente removeSelected.
Masocompiladorreclama. Chato. Sim,estaéumadasideiasportrásde
usar um compilador: pegar em desenvolvimento problemas que quebrariam
nossa aplicação em tempo de execução. Ele indica que
UIAlertAction!
não pode ser convertido para (). Nossa função não recebe nada, e
UIAlertAction!nãopodeserconvertidoparanada.
Vamosrecebê-lo:
func removeSelected(action:UIAlertAction!) {
println("removed the selected one")
}
218

## Página 225

CasadoCódigo Capítulo14. Removendoumarefeição
Codesmell: usandocomponentesUIcomoparâmetros
emobserverseoswitch
Qualomotivoderecebernossaprópria UIAlertActioncomopa-
râmetr oaoexecu tarafunçãoa tr eladaaumaUIAlertAction?
Uma função de callback como essa pode ser reutilizada por diver-
sos eventos. Um exemplo disso é oprepareForSegue, um callback
invocadoquandoqualquer segue deseucontrollerforativado. Opro-
blemadeterumaúnicafunçãoparaduasações( segues sãoexemplos
deações)diferenteséqueprecisamosagoracriarumasequênciade ifs
queverificamvaloresemtempodeexecução: ocompiladordeixadenos
ajudar e passamos a ter uma função com alta complexidade ao invés de
diversasfunçõescompoucacomplexidade.
Oquedevemosfazer? Somentereutilizeomesmocallback,amesma
função, caso a ação a ser executada for realmente do mesmo tipo entre
diversos botões,
segues etc. Caso o código de uma ação não tenha
nenhuma relação com o código de outra ação, não existe motivo para
os dois estarem no mesmo método: crie duas funções e passe cada uma
comoargumentoparaquemiráinvocá-la.
Inicialmente, os autores do livro acreditavam que o modelo em que
o cliente que é notificado das observações (ou, hoje em dia, umlistener
que é notificado de eventos) e conhece mais sobre o objeto que está ob-
servando (modelo
push) era um modelo que dificultava o reúso. Hoje
emdia,RalphJohnsondefendeemsuaspalestrasqueomodelo observers
especializadossãoreutilizáveis,enquantoquegenéricosnão.
Sendoassim,ousodeummesmo observer(oulistener)paradiversas
ações totalmente diferentes, em que recebemos como parâmetro nosso
componente UI para decidir o que fazer, é um cheiro de que é possí-
vel que algo esteja ocorrendo de muito feio: muita complexidade com
ifs e switchs indica um cheiro ainda maior. Evite, ajude o próximo
desenvolvedor e a manutenção de seu código: cada ação distinta é uma
responsabilidadediferenteemereceseuprópriométodo.
219

## Página 226

14.3. Indentificandoalinhaaserremovida CasadoCódigo
Rodamosnossaaplicaçãoe,agorasim,efetuamoso long press emum
dos elemento. Temos o resultado impresso no log ao selecionarmos a opção
remove.
14.3 Indentificandoalinhaaserremovida
Gostaríamos agora de imprimir o nome da refeição que será removida, so-
mente para conferir que está tudo ok. Mas como acessar a variável que foi
definidaemoutrométodo? Comoométodo
removeSelectedacessaava-
riável mealdentrodométodo showDetails? Complicado... Cadavariável
temseupróprioescopoenãopodeseracessadaforadele:
func showDetails(recognizer: UILongPressGestureRecognizer){
if recognizer.state == UIGestureRecognizerState.Began {
let cell = recognizer.view as UITableViewCell
let indexPath = tableView.indexPathForCell(cell)
if indexPath == nil {
return
}
let row = indexPath!.row
let meal = meals[ row ]
// code that shows the controller
}
}
func removeSelected(action:UIAlertAction!) {
220

## Página 227

CasadoCódigo Capítulo14. Removendoumarefeição
// meal.name????????????????????????????????????
println("removed the selected one \(meal.name)")
}
Podemos criar uma variável opcional em nosso
MealsTableViewController que representa a refeição selecio-
nada, atribuir um valor dentro do método que seleciona e aplicá-lo no
removeSelected. Difícil?
var selectedMeal:Meal?
func showDetails(recognizer: UILongPressGestureRecognizer){
if recognizer.state == UIGestureRecognizerState.Began {
let cell = recognizer.view as UITableViewCell
let indexPath = tableView.indexPathForCell(cell)
if indexPath == nil {
return
}
let row = indexPath!.row
let meal = meals[ row ]
selectedMeal = meal
// code that shows the controller
}
}
func removeSelected(action:UIAlertAction!) {
if let meal = selectedMeal {
println("removed the selected one \(meal.name)")
}
}
Complicado e feio, feio demais. Quanto mais tentamos “globalizar” nos-
sas variáveis, e perder o escopo, perdemos o controle sobre elas. Deixá-las
como opcionais? Estamos perdendo ainda mais o controle sobre o que está
acontecendo e qual a situação atual de nossos objetos. Não vamos por esse
caminho.
Note que a função
removeSelected não precisa necessariamente vi-
ver dentro de nossa classe. Nossa função é um método, por ser definida
221

## Página 228

14.3. Indentificandoalinhaaserremovida CasadoCódigo
na classe, podendo ser invocada como um comportamento dos objetos do
tipo MealsTableViewController. Mas não precisamos disso. Só pre-
cisamos dela dentro do métodoshowDetails.És o m e n t ea om o s t r a ro s
detalhesdeumarefeiçãoqueénecessárioumafunçãocapazderemoverrefei-
ções. Oquefazer? Colocamosafunção
removeSelected dentrodenosso
showDetails). Umafunçãopodeexistirdentrodeoutra,nãotemproblema
nenhumnisso:
func showDetails(recognizer: UILongPressGestureRecognizer){
if recognizer.state == UIGestureRecognizerState.Began {
let cell = recognizer.view as UITableViewCell
let indexPath = tableView.indexPathForCell(cell)
if indexPath == nil {
return
}
let row = indexPath!.row
let meal = meals[ row ]
func removeSelected(action:UIAlertAction!) {
println("removed the selected one \(meal.name)")
}
let details = UIAlertController(title: meal.name,
message: meal.details(),
preferredStyle: UIAlertControllerStyle.Alert)
let remove = UIAlertAction(title: "Remove",
style: UIAlertActionStyle.Destructive,
handler: removeSelected)
details.addAction(remove)
let cancel = UIAlertAction(title: "Cancel",
style: UIAlertActionStyle.Cancel,
handler: nil)
details.addAction(cancel)
presentViewController(
details, animated: true, completion: nil)
}
}
222

## Página 229

CasadoCódigo Capítulo14. Removendoumarefeição
Removemosadefiniçãoanteriordafunção(nãoseesqueça!) etudoconti-
nua compilando! Claro,removeSelected continua sendo uma referência
para uma função. Antes, a função era especial, um método. Agora, a fun-
çãotambéméespecial,umafunçãodefinidadentrodenossocódigo. Escopo
controlado,masambassãofunçõesepodemserreferenciadas.
14.4 Removendoeatualizandoatela
Opróximopassoéremoverdeverdadeusandoo removeAtIndex:
func showDetails(recognizer: UILongPressGestureRecognizer){
if recognizer.state == UIGestureRecognizerState.Began {
let cell = recognizer.view as UITableViewCell
let indexPath = tableView.indexPathForCell(cell)
if indexPath == nil {
return
}
let row = indexPath!.row
let meal = meals[ row ]
func removeSelected(action:UIAlertAction!) {
println("removed the selected one \(meal.name)")
meals.removeAtIndex(row)
}
// show the controller
}
223

## Página 230

14.5. Closures CasadoCódigo
}
Testamos agora nossa aplicação, mas a tabela continua inteira. Clicamos
novamenteem removerparaapagaraúltimarefeiçãodalista,eaaplicação
crasheia. Oqueacontece? Eletentaacessaroarrayemumaposiçãoinválida!
Comoassim? Jáhavíamosmencionadoaimportânciadeatualizarmosnossa
tabela toda vez que o array for atualizado, e acabamos de cometer esse erro.
Atualizamos o array mas não pedimos para a tabela ser redesenhada-ee l a
nãofoi.
Mudemosnosso
removeSelectedparaatualizá-la:
func showDetails(recognizer: UILongPressGestureRecognizer){
if recognizer.state == UIGestureRecognizerState.Began {
// get the meal
func removeSelected(action:UIAlertAction!) {
println("removed the selected one \(meal.name)")
meals.removeAtIndex(row)
tableView.reloadData()
}
// show the controller
}
}
Agorasim,somoscapazesderemoverelementos.
14.5 Closures
Já podemos remover nossoprintln, que ficou desnecessário. O que mais
podemosatualizaremnossocódigo?
Uma outra maneira de criar uma função que será utilizada poucas vezes
é criá-la e já atribuí-la, seja para uma variável, seja como parâmetro na in-
vocação de um método. Por exemplo, podemos invocar o inicializador do
UIAlertAction já passando nosso bloco (umaclosure) que será invocado
posteriormente. Como nosso bloco recebe umUIAlertAction e devolve
nada,marcamoscomo (UIAlertAction) -> Void :
224

## Página 231

CasadoCódigo Capítulo14. Removendoumarefeição
let remove = UIAlertAction(title: "Remove",
style: UIAlertActionStyle.Destructive,
handler: {(action:UIAlertAction!) -> Void in
meals.removeAtIndex(row)
table.reloadData()
})
Como o compilador é capaz de inferir qual o tipo do parâmetro, pois o
estamospassandodiretamente,nãoprecisamosdefini-lo. Amesmacoisavale
paraoretorno,portantonossocódigoficaassim:
let remove = UIAlertAction(title: "Remove",
style: UIAlertActionStyle.Destructive,
handler: { action in
meals.removeAtIndex(row)
table.reloadData()
})
Ótimo, mas ainda não compila. Acontece que, para umaclosureacessar
uma propriedade de nossa classe, ela precisa deixar isso explícito através do
usodo self:
let remove = UIAlertAction(title: "Remove",
style: UIAlertActionStyle.Destructive,
handler: { action in
self.meals.removeAtIndex(row)
self.table.reloadData()
})
Agorasim,nossocódigofuncionacomoanteriormente,eestamosusando
umaclosureemvezdeumafunçãoouummétodo.
14.6 Codesmell:closuresarodo
Como vimos, uma função pode ser utilizada de diversas maneiras: ela pode
ser declarada e utilizada diretamente como umaclosure, pode ser definida
dentrodenossocódigocomoumafunçãonormalouaindadeclaradaemuma
classeparafuncionarcomoummétododenossosobjetos. Poreducação,não
criamosfunçõesglobais.
225

## Página 232

14.6. Codesmell: closuresarodo CasadoCódigo
Cada uma delas é aplicada com suas vantagens e desvantagens. Lembre-
se: blocos eclosuressão mais difíceis de testar por compactar muito o con-
teúdo. São às vezes chamados deconciso, mas não confunda ‘conciso’ - que
exige clareza, sem ambiguidades - com ‘mínimo de digitação possível’, que
permiteambiguidadeeporvezesdificultaacompreensão.
Por mais tentador que seja adotar o uso declosuresem todo canto, tome
muito cuidado. No mundo selvagem de programação você verá isso acon-
tecendo de maneira descontrolada: usando sem dó nem piedade. Não deixe
queodescontroleeousodediversoscomportamentosemumúnicométodo
odominem: aocolocardiversas closuresempoucoespaço,muitoscomporta-
mentos tomam conta daquele código. Fuja dessa cilada, mantenha uma res-
ponsabilidadeporunidadedecódigo.
Estamos falando tanto de muita responsabilidade e qualidade de código,
mas esta classe está bem feia. Não por ser muita digitação, mas sim por ter
muita responsabilidade. Note que ela é responsável por tudo ligado à view
de todas as refeições, mas também à view de remover uma refeição. Onde
já se viu isso? Uma classe de
view controller que lida com doisview
controllers. Falta de respeito por dificultar a manutenção de nosso có-
digo. Extrairemosnossaresponsabilidade.
Podemosprimeiroextrairummétodochamado show,umaoperaçãode
refatoraçãotradicional:
func showDetails(recognizer: UILongPressGestureRecognizer){
if recognizer.state == UIGestureRecognizerState.Began {
let cell = recognizer.view as UITableViewCell
let indexPath = tableView.indexPathForCell(cell)
if indexPath == nil {
return
}
let row = indexPath!.row
let meal = meals[ row ]
show(meal)
}
}
func show(meal:Meal) {
226

## Página 233

CasadoCódigo Capítulo14. Removendoumarefeição
let details = UIAlertController(title: meal.name,
message: meal.details(),
preferredStyle: UIAlertControllerStyle.Alert)
let remove = UIAlertAction(title: "Remove",
style: UIAlertActionStyle.Destructive,
handler: { action in
self.meals.removeAtIndex(row)
self.tableView.reloadData()
})
details.addAction(remove)
let cancel = UIAlertAction(title: "Cancel",
style: UIAlertActionStyle.Cancel,
handler: nil)
details.addAction(cancel)
presentViewController(
details, animated: true, completion: nil)
}
Mas nosso código precisa mais do que a refeição, ele precisa também do
número da linha. Não vamos começar a passar diversos parâmetros picados
paraométodo. Daquiapouco,eleprecisadeumoutro Int,deuma String.
Sedesejamosmostrarodiálogod eremoverrefeição,passemoso handlerin-
teirodeumavez:
func showDetails(recognizer: UILongPressGestureRecognizer){
if recognizer.state == UIGestureRecognizerState.Began {
let cell = recognizer.view as UITableViewCell
let indexPath = tableView.indexPathForCell(cell)
if indexPath == nil {
return
}
let row = indexPath!.row
let meal = meals[ row ]
show(meal, { action in
self.meals.removeAtIndex(row)
self.tableView.reloadData()
})
227

## Página 234

14.6. Codesmell: closuresarodo CasadoCódigo
}
}
func show(meal:Meal, handler:(UIAlertAction!) -> Void) {
let details = UIAlertController(title: meal.name,
message: meal.details(),
preferredStyle: UIAlertControllerStyle.Alert)
let remove = UIAlertAction(title: "Remove",
style: UIAlertActionStyle.Destructive,
handler: handler)
details.addAction(remove)
let cancel = UIAlertAction(title: "Cancel",
style: UIAlertActionStyle.Cancel,
handler: nil)
details.addAction(cancel)
presentViewController(
details, animated: true, completion: nil)
}
Por fim, nosso método não nos pertence: vamos extraí-lo para outra
classe, uma classe que representa nossa view de remover refeição. Criamos
nogrupo viewsoarquivo RemoveMealController.swift,seguindoo
mesmoestilodonosso Alert.swift:
class RemoveMealController {
let controller:UIViewController
init(controller:UIViewController) {
self.controller = controller
}
func show(meal:Meal, handler:(UIAlertAction!) -> Void) {
let details = UIAlertController(title: meal.name,
message: meal.details(),
preferredStyle: UIAlertControllerStyle.Alert)
let remove = UIAlertAction(title: "Remove",
style: UIAlertActionStyle.Destructive,
handler: handler)
details.addAction(remove)
let cancel = UIAlertAction(title: "Cancel",
228

## Página 235

CasadoCódigo Capítulo14. Removendoumarefeição
style: UIAlertActionStyle.Cancel,
handler: nil)
details.addAction(cancel)
controller.presentViewController(
details, animated: true, completion: nil)
}
}
Eusamosnossanovaclasse:
func showDetails(recognizer: UILongPressGestureRecognizer){
if recognizer.state == UIGestureRecognizerState.Began {
let cell = recognizer.view as UITableViewCell
let indexPath = tableView.indexPathForCell(cell)
if indexPath == nil {
return
}
let row = indexPath!.row
let meal = meals[ row ]
RemoveMealController(controller: self).show(meal,
{ action in
self.meals.removeAtIndex(row)
self.table.reloadData()
})
}
}
Agoratudofuncionaeocódigoestámaisbemextraído. Ganhamosmuito
comasvantagensderefatoraçãoegarantiasdecompilaçãodenossocódigo.
14.7 Resumo
Vimos neste capítulo como permitir a remoção de uma refeição, mas, para
chegar até esse ponto e mesmo após alcançá-lo, passamos por diversas me-
lhoriasdenossocódigo.
Aprendemosacriarum handlerquepoderiaserumareferênciaparauma
função qualquer: desde umaclosureaté o método de um objeto específico.
229

## Página 236

14.7. Resumo CasadoCódigo
Aprendemos a receber uma referência para uma função em nosso código ao
extrairmosummétodoeumaclasseparaisolarmelhorasresponsabilidades
de nosso programa. Somos capazes agora de dizer o que é uma função, e
quandoelaestádefinidacomoumamerafunção,uma closureouummétodo
deumaclasse.
Vimostambémdiversoscuidadosquedevemostomarepossíveisrefato-
rações a serem efetuadas para melhorar nosso código a cada novo passo que
damos.
230

## Página 237

Capítulo15
Armazenandoasrefeiçõesdentro
dofilesystem
Conseguimoscriaremostraralistaderefeições,masoqueacontecequando
fechamosaaplicação? Aorodarmosnovamente,vemosqueosdadosquees-
tavaminseridosnãoaparecemmais! Queremosque,umavezqueasrefeições
e os itens sejam cadastrados, eles continuem dentro da app. Para isso, preci-
samosdeixardesalvarnossosdadosemmemóriaesalvarmosnosistemade
arquivosdoaparelhotodavezquesairmosdenossaaplicação.
Primeiro,vamosreconectarnossatabeladeitensparaqueelavolteafun-
cionar. Para isso, voltamos a selecionar a nossa
TableView ec o n e c t a m o s
seu IBOutletcomnossavariávelnocontroller.

## Página 238

CasadoCódigo
Umaclassequenospossibilitafazerissoéa NSKeyedArchiver.El ape r -
miteconverterqualquerobjetoparaumformatoquepodesergravadoemum
arquivonosistemadearquivos,temosapenasquedizerquaisdadosdenosso
objetoqueremosquesejamarmazenados. Mascomoo
NSKeyedArchiver
sabequalobjetopodeequalnãopodesergravado?
Para garantir que conseguimos responder a este formato, temos que im-
plementarummétodoespecíficocomoqualo NSKeyedArchiversabetra-
balhar. É o que fazemos utilizando o protocoloNSCoding em nosso objeto
Meal:
class Meal : NSCoding {
// ...
}
Para o protocolo funcionar, precisamos que nossa classe herde os com-
p o r t a m e n t o sd ac l a s s eNSObject. Portanto, na classeMeal vamos herdar
de NSObjecteassinaroprotocolo NSCoding:
class Meal : NSObject, NSCoding {
// ...
}
Ocompiladoriráreclamarquenãoimplementamosométododoproto-
colo,apesardedizermosqueoadotamos. Claro! Jásabemoscomoprotocolos
funcionam. Mas quais os comportamentos que precisamos ter? Primeiro, o
NSKeyedArchiverdevesercapazdetransformarnossosobjetosemalgum
valor que possa ser salvo, portanto precisamos de um método que, ao ser
executadoemumobjeto,salvaosdadosdele,ummétodoque
encodenosso
232

## Página 239

CasadoCódigo Capítulo15. Armazenandoasrefeiçõesdentrodofilesystem
objeto,queoserialize. Depois,precisaremosdeumcomportamentoqueper-
mita desserializar, recuperar o objeto para a memória dadas as informações
que estavam (em nosso caso) em um arquivo. Isso é, precisamos inicializar
umobjetoelerosdadosquejáexistiam,emoutraspalavrasprecisaremosde
uminicializadorparaadeserialização.
Vamos colocar o método
encodeWithCoder,q u eéor e s p o n s á v e lp o r
transformar nosso objetoMeal emalgoquepossasergravadoemdisco, ou
seja,encodaronossoobjeto.Essemétodorecebeumobjetodotipo NSCoder
ondejogamososdadosdenossoobjetopassandoumachaveeovalorcorres-
pondente:
class Meal : NSObject, NSCoding {
// ...
func encodeWithCoder(aCoder: NSCoder) {
aCoder.encodeObject(self.name, forKey: "name")
aCoder.encodeInteger(self.happiness, forKey: "happiness")
aCoder.encodeObject(self.items, forKey: "items")
}
}
Sabemos como encodar, mas e como buscaremos os dados do arquivo?
Temos que fazer a volta! O protocoloNSCoding também define um inici-
alizador para isso, para criar um objeto utilizando os dados do disco. Colo-
camos o inicializador na nossa classeMeal decodando os dados a partir do
NSCoder:
class Meal : NSObject, NSCoding {
// ...
init(coder aDecoder: NSCoder) {
self.name = aDecoder.decodeObjectForKey("name") as String
self.happiness =
aDecoder.decodeIntegerForKey("happiness")
self.items =
aDecoder.decodeObjectForKey("items") as Array<Item>
}
233

## Página 240

CasadoCódigo
func encodeWithCoder(aCoder: NSCoder) {
aCoder.encodeObject(self.name, forKey: "name")
aCoder.encodeInteger(self.happiness, forKey: "happiness")
aCoder.encodeObject(self.items, forKey: "items")
}
}
Deixandodessaforma,oXcodevaireclamarpoisoprotocoloobrigaque
oconstrutorsejaimplementadoportodasasclasses,logo,precisamoscolocar
apalavra requirednaassinaturadométodo:
class Meal : NSObject, NSCoding {
// ...
required init(coder aDecoder: NSCoder) {
self.name = aDecoder.decodeObjectForKey("name") as String
self.happiness =
aDecoder.decodeIntegerForKey("happiness")
self.items =
aDecoder.decodeObjectForKey("items") as Array<Item>
}
func encodeWithCoder(aCoder: NSCoder) {
aCoder.encodeObject(self.name, forKey: "name")
aCoder.encodeInteger(self.happiness, forKey: "happiness")
aCoder.encodeObject(self.items, forKey: "items")
}
}
234

## Página 241

CasadoCódigo Capítulo15. Armazenandoasrefeiçõesdentrodofilesystem
Boaprática:desserializaçãonainicialização
De qual outra maneira poderíamos ter feito, em vez de implementar
adesserializaçãonoconstrutor? Duasopçõessãobemcomuns: umaem
queimplementamosummétodo,algocomo decodeWithDecoder:
func decodeWithDecoder(aDecoder: NSCoder) {
self.name = aDecoder.decodeObjectForKey("name") as String
self.happiness =
aDecoder.decodeIntegerForKey("happiness")
self.items =
aDecoder.decodeObjectForKey("items") as Array<Item>
}
M a sn o t eq u en e s s aa b o r d a g e ms e r i ai m p o s s í v e lc r i a r m o sgood
citizens. Aoutraéacriaçãodeumsegundoobjetocapazdeserializar
edesserializardados,alguémresponsávelpeloprocessodeserializaçãoe
desserialização de um modelo (algo como umafactorye de-factory,u m
converter):
class MealConverter {
func decodeWithDecoder(aDecoder: NSCoder) -> Meal {
let name = aDecoder.decodeObjectForKey("name") as String
let happiness = aDecoder.decodeIntegerForKey("happiness")
let items =
aDecoder.decodeObjectForKey("items") as Array<Item>
let meal = Meal(name, happiness)
meal.items = items
return meal
}
func encodeWithCoder(meal:Meal, aCoder: NSCoder) {
aCoder.encodeObject(meal.name, forKey: "name")
aCoder.encodeInteger(meal.happiness, forKey: "happiness")
aCoder.encodeObject(meal.items, forKey: "items")
}
}
Enquanto na desserialização ainda temos umgood citizen,aa b o r d a -
gem do encodeWithCoder quebra a regra básica de encapsulamento,
aoobrigaraconhecertudoqueumarefeiçãopossuiaoconverter.
L e v a n d oe mc o n t aotrade-offentre quebrar o good citizen
e quebra de enca psulamento, aa b o r d agem do NSCoding éad e
235

## Página 242

CasadoCódigo
Goodcitizeneoarraydeitens
Até agora usamos a definição dos itens de uma refeição após a cria-
çãodeum Meal. Continuaremosassimpelonossoprojeto,maséclara-
mentevisívelque,seumarefeiçãonãotivesseseusitensalteradosnunca,
osmesmospoderiamserconfiguradosnainicialização,podendomanter
adefiniçãodavariável
itemscomum let,umaconstante.
InicializandoumviewcontrollercomNSCoder
Agora podemos entender que quando herdamos de um
UIViewController ganhamos de graça a capacidade de seriali-
zar nossos controllers eéj u s t a m e n t ep o ri s s oq u e ,a oc r i a r m o s
um novo inicializador, devemos garantir que a inicialização também
ocorrerá educadamente caso o
controller seja deserializado, isto é,
o init(coder aDecoder: NSCoder) sejainvocado.
Podemosfazerum Command+Clicknonomedoprotocolo, NSCoding
e revisar como ele foi definido. Repare que ele possui as duas características
mencionadas anteriormente: tanto o método
encodeWithCode quanto o
initdevemserdefinidos.
Ensinamos como fazemos para encodar uma refeição, mas a refeição é
composta por itens, logo, devemos ensinar como encodar os itens também.
Na classe
Item repetimos o mesmo processo que fizemos na classeMeal.
Elaficarádaseguinteforma:
class Item: NSObject, Equatable, NSCoding {
let name:String
let calories:Double
init(name: String, calories: Double) {
self.name = name
self.calories = calories
}
236

## Página 243

CasadoCódigo Capítulo15. Armazenandoasrefeiçõesdentrodofilesystem
required init(coder aDecoder: NSCoder) {
self.name = aDecoder.decodeObjectForKey("name") as String
self.calories = aDecoder.decodeDoubleForKey("calories")
}
func encodeWithCoder(aCoder: NSCoder) {
aCoder.encodeObject(self.name, forKey: "name")
aCoder.encodeDouble(self.calories, forKey: "calories")
}
}
15.1 Salvandoasrefeiçõesnosistemadearqui-
vos
Agora que conseguimos transformar os objetos, chegou o momento de sal-
varmososdados nonosso file system . Todavezquecriamosumanova
refeição, queremos salvar os dados de nossas refeições. Alteramos o método
add de nosso MealsTableViewController para salvar os dados no ar-
quivousandoo NSKeyedArchiveretiramosasrefeiçõesquehavíamosco-
locadoanteriormente,inicializandocomum Arrayvazio:
var meals = Array<Meal>()
func add(meal: Meal) {
meals.append(meal)
NSKeyedArchiver.archiveRootObject(meals, toFile: archive)
tableView.reloadData()
}
Precisamossaberondecriaroarquivoquequeremosgravarecujosdados
queremosler .Sópodemosefetuaraleituraeaescritadearquivosqueestejam
dentro do diretório de nossa aplicação, portanto obtemos o caminho para o
diretórioatravésdafunção
NSSearchPathForDirectoriesInDomains.
override func viewDidLoad() {
let userDirs = NSSearchPathForDirectoriesInDomains(
?,
237

## Página 244

15.1. Salvandoasrefeiçõesnosistemadearquivos CasadoCódigo
?,
?)
}
Masafunçãorecebetrêsparâmetros. Oprimeiroindicaquetipodedire-
tórioestamosprocurando,odiretóriodedocumentos. Osegundoindicaqual
domínio estamos procurando, o de usuários. Por fim, o terceiro argumento
diz se desejamos que o caminho para o diretório seja absoluto ou relativo à
homedousuário. Desejamosabsoluto:
override func viewDidLoad() {
let userDirs = NSSearchPathForDirectoriesInDomains(
NSSearchPathDirectory.DocumentDirectory,
NSSearchPathDomainMask.UserDomainMask,
true)
}
Invocar NSSearchPathForDirectoriesInDomainsretorna,umar-
raycomtodososdiretóriosdeusuários,mascomonoiOStemossomenteum
usuário,podemospegarsempreaprimeiraposiçãodestearray. Montamoso
nomedoarquivoe,comoeleseránecessáriotantoparalerquantoparaescre-
ver,criamosodiretórioumaúnicavezdentrodométodo
viewDidLoad.
override func viewDidLoad() {
let userDirs = NSSearchPathForDirectoriesInDomains(
NSSearchPathDirectory.DocumentDirectory,
NSSearchPathDomainMask.UserDomainMask,
true)
let dir = userDirs [0]a s String
let archive = "\(dir)/eggplant-brownie-meals"
}
Jápodemoslerasrefeiçõesdoarquivocasoelejáexista:
var meals = Array<Meal>()
override func viewDidLoad() {
let userDir = NSSearchPathForDirectoriesInDomains(
NSSearchPathDirectory.DocumentDirectory,
238

## Página 245

CasadoCódigo Capítulo15. Armazenandoasrefeiçõesdentrodofilesystem
NSSearchPathDomainMask.UserDomainMask,
true)
let dir = userDir [0]a s String
let archive = "\(dir)/eggplant-brownie-meals"
if let loaded =
NSKeyedUnarchiver.unarchiveObjectWithFile(archive) {
self.meals = loaded as Array
}
}
Enonossométododesalvar,usamosomesmoarquivo:
func add(meal: Meal) {
meals.append(meal)
let userDir = NSSearchPathForDirectoriesInDomains(
NSSearchPathDirectory.DocumentDirectory,
NSSearchPathDomainMask.UserDomainMask,
true)
let dir = userDir [0]a s String
let archive = "\(dir)/eggplant-brownie-meals"
NSKeyedArchiver.archiveRootObject(meals, toFile: archive)
tableView.reloadData()
}
Mas... Copye pastemesmo? Vamos refatorar nosso código e extrair um
método,o getUserDir:
func add(meal: Meal) {
meals.append(meal)
let dir = getUserDir()
let archive = "\(dir)/eggplant-brownie-meals"
NSKeyedArchiver.archiveRootObject(meals, toFile: archive)
tableView.reloadData()
}
func getUserDir() -> String {
let userDir = NSSearchPathForDirectoriesInDomains(
NSSearchPathDirectory.DocumentDirectory,
NSSearchPathDomainMask.UserDomainMask,
true)
return userDir[ 0 ] as String
239

## Página 246

15.1. Salvandoasrefeiçõesnosistemadearquivos CasadoCódigo
}
override func viewDidLoad() {
let dir = getUserDir()
let archive = "\(dir)/eggplant-brownie-meals"
if let loaded =
NSKeyedUnarchiver.unarchiveObjectWithFile(archive) {
self.meals = loaded as Array
}
}
Agoravamosrodarnossaaplicação. Vemosatabelalimpa:
Adicionamos uma nova refeição: umSundubu(tofu coreano). No menu
de Hardware, escolhemos aHome (ou restartamos o simulador do zero) e
podemosverquenossarefeiçãoaindaestáarmazenada.
240

## Página 247

CasadoCódigo Capítulo15. Armazenandoasrefeiçõesdentrodofilesystem
241

## Página 248

15.2. Salvandoelendoitensnosistemadearquivos CasadoCódigo
15.2 Salvandoelendoitensnosistemadearqui-
vos
Conseguimos gravar as refeições, mas precisamos gravar também os
itens separadamente. Vamos efetuar a mesma alteração em nosso
ViewController. Primeiro,inicializamoso Arraydeitensvazio:
var items = Array<Item>()
Obtemos o caminho para o arquivo e montamos o nome dele dentro do
viewDidLoad:
func getUserDir() -> String {
let userDir = NSSearchPathForDirectoriesInDomains(
NSSearchPathDirectory.DocumentDirectory,
NSSearchPathDomainMask.UserDomainMask,
true)
return userDir[ 0 ] as String
}
override func viewDidLoad() {
// Creating button...
let dir = getUserDir()
let archive = "\(dir)/eggplant-brownie-items"
}
Carregamos também os dados do arquivo dentro de nossa variável
items:
override func viewDidLoad() {
// Creating button...
let dir = getUserDir()
let archive = "\(dir)/eggplant-brownie-items"
if let loaded =
NSKeyedUnarchiver.unarchiveObjectWithFile(archive) {
items = loaded as Array
}
}
242

## Página 249

CasadoCódigo Capítulo15. Armazenandoasrefeiçõesdentrodofilesystem
Porfim,salvamososdadosnoarquivodentrodométodo addNew:
func addNew(item: Item) {
items.append(item)
let dir = getUserDir()
let archive = "\(dir)/eggplant-brownie-items"
NSKeyedArchiver.archiveRootObject(items, toFile: archive)
if let table = tableView {
table.reloadData()
} else {
Alert(controller: self).show(message:
"Unexpected error, but the item was added.")
}
}
Conseguimos acessar o diretório Library para procurarmos onde
o arquivo foi gerado, fazendo cmd+shift+g no Finder e digitando
~/Library:
Oarquivoserágeradoemumcaminhoparecidocomoseguinte:
243

## Página 250

15.2. Salvandoelendoitensnosistemadearquivos CasadoCódigo
Como agora os dados pré-cadastrados não existem mais, rodamos e cri-
amos novamente um novo item chamadocheesecom 100 calorias, um item
chamadocookie, e adicionamos os dois em uma nova refeição chamadache-
esecakecom nível de felicidade 5. Ao efetuarmos olong press , podemos
verqueosdadosforamcadastradoscomsucesso:
244

## Página 251

CasadoCódigo Capítulo15. Armazenandoasrefeiçõesdentrodofilesystem
245

## Página 252

15.2. Salvandoelendoitensnosistemadearquivos CasadoCódigo
Paraverificarmosseositenscontinuamlámesmoapóssairmosdenossa
aplicação,ésófazer cmd+shift+hnosimulador,queelefecharáaaplicação:
246

## Página 253

CasadoCódigo Capítulo15. Armazenandoasrefeiçõesdentrodofilesystem
247

## Página 254

15.2. Salvandoelendoitensnosistemadearquivos CasadoCódigo
Aoclicarmosnaaplicação,podemosverquearefeiçãoadicionadaconti-
nua lá.
Resumo
Nestecapítulo,vimoscomotransformarobjetosparaseremsalvoserecu-
peradosatravésdoprotocolo NSCodingetambémcomomanipulararquivos
utilizando NSKeyedArchivere NSKeyedUnarchiver.
Aprendemos como o protocoloNSCoding obriga não só a implemen-
tação de um método como também a existência de um inicializador do tipo
required. Vimostambémcomo,aosairevoltaranossaaplicação,osdados
foramcarregadosdosistemadearquivos,inclusivesendocapazesdelocalizá-
losemnossocomputador.
Notrajetoatéaquiextraímosumafunçãoquenosauxiliaadefinirodire-
tóriodearmazenamentodedados,masaindaparecequetemosmuito copy
e paste ,algoquedevemosa tacarnop r ó ximoca p í tulo .
248

## Página 255

Capítulo16
Boaprática: dividindo
r espo nsab ilidadeseoDa ta
AccessObject
Conseguimos salvar e buscar os dados com sucesso, porém nosso controller
acabouficandocommuitasresponsabilidades: alémderepresentarerespon-
der as ações da view e de interagir com outras, agora ele é responsável por
armazenarelerosdadosdodisco. Temosquepensaraindaquecadacontrol-
ler está cuidando de seus próprios dados, repetindo, por exemplo, a lógica
parabuscarmosodiretórioondecriamososnossosarquivos. Esealgumdia
resolvermos armazenar os dados de uma outra forma? Teremos que alterar
emtodososcontrollersestanossalógica. Paranãotermosesteproblema,va-
mos criar uma outra classe no grupo
models, que terá a responsabilidade

## Página 256

CasadoCódigo
detrabalharcomoarmazenamentodedados. Paraisso,escolhemosomenu
File, New, iOS, Source, Swift File edamosono mede Dao:
class Dao {
}
Em nosso Dao, criamos as variáveis que vão receber o nome de nossos
arquivos:
class Dao {
let mealsArchive: String
let itemsArchive: String
}
Vamos efetuar também o carregamento dos dados no momento em que
inicializarmoso Dao.Criamosoconstrutorparaele,ondebuscamosodir e-
tóriodousuárioumaúnicavezemontamososnomesdosdoisarquivosque
utilizaremos:
init(){
let userDir = NSSearchPathForDirectoriesInDomains(
NSSearchPathDirectory.DocumentDirectory,
NSSearchPathDomainMask.UserDomainMask,
true)
let dir = userDir[0] as String
mealsArchive = "\(dir)/eggplant-brownie-meals"
itemsArchive = "\(dir)/eggplant-brownie-items"
}
Agoracriamosométodoparasalvarecarregarasrefeições:
func saveMeals(meals: Array<Meal>){
NSKeyedArchiver.archiveRootObject(
meals, toFile: mealsArchive)
}
func loadMeals() -> Array<Meal> {
if let loaded =
NSKeyedUnarchiver.unarchiveObjectWithFile(mealsArchive) {
return loaded as Array
250

## Página 257

CasadoCódigo Capítulo16. Boaprática: dividindoresponsabilidadeseoDa taA ccess...
}
}
Masprecisamoscuidardocasodeoarquivonãoexistir,emqueretorna-
mosumarrayvazio:
func loadMeals() -> Array<Meal> {
if let loaded =
NSKeyedUnarchiver.unarchiveObjectWithFile(mealsArchive) {
return loaded as Array
}
return Array<Meal>()
}
V amossalvarecarr egari tens:
func saveItems(items: Array<Item>){
NSKeyedArchiver.archiveRootObject(
items, toFile: itemsArchive)
}
func loadItems() -> Array<Item> {
if let loaded =
NSKeyedUnarchiver.unarchiveObjectWithFile(itemsArchive) {
return loaded as Array
}
return Array<Item>()
}
UmDaopormodelo
Emaplicaçõesmaiores,écomumutilizarumaclassedeDAOpormo-
delo, ou ainda, algum outro tipo de divisão de responsabilidades de sal-
varecarregardadosdeumafonte. Nonossoprojeto,emquepossuímos
somente quatro métodos de uma linha, não há a necessidade de refinar
aindamaisaresponsabilidadedetaisclasses. Comoumbomprograma-
dor, sempre julgue com cuidado o momento no qual acredita ser ade-
quadaaquebraderesponsabilidades.
251

## Página 258

CasadoCódigo
Codesmell:nomedotipononomedavariável,métodoetc
Repare qual a palavra que se repete em cada uma das linhas; e quantas
vezes?
func saveItems(items: Array<Item>)
func saveMeals(meals: Array<Meal>)
func loadMeals() -> Array<Meal>
func loadItems() -> Array<Item>
Em uma linguagem como Swift, o próprio compilador é capaz de dizer
qual método está sendo invocado de acordo com os tipos dos argumentos
passados. Portanto, não há necessidade de repetir o nome do tipo recebido
comoparâmetrononomedeummétodo.Asfunçõesde
savepoderiamser:
func save(items: Array<Item>)
func save(meals: Array<Meal>)
func loadMeals() -> Array<Meal>
func loadItems() -> Array<Item>
Masimaginecomoficariaestranhoseomesmoocorressecomométodo
load, que dependeria do tipo da variável ao qual o retorno está sendo apli-
cado, para o compilador entender qual método está sendo invocado. Com-
plexo. Poressemotivo,manteremosospadrões loadMealse loadItems.
Jáquemantemosessepadrãono load,man ter emosomesmono save.
O dia em que você como desenvolvedor julgar adequado quebrar o có-
digoemdois Daos,poderátranquilamenterenomearosmétodosparaevitar
r epetiçãodeno medeti poemno medemétodo .
Agora que o Dao está pronto, podemos alterar nossos controllers para
utilizar este novo objeto. Primeiro, mudamos a classeViewController
para apenas chamar o métodoloadItems no viewDidLoad, removendo
ocódigoanteriorondebuscávamosodiretório:
override func viewDidLoad() {
let newItemButton = UIBarButtonItem(title: "new item",
style: UIBarButtonItemStyle.Plain,
target: self,
action: Selector("showNewItem"))
252

## Página 259

CasadoCódigo Capítulo16. Boaprática: dividindoresponsabilidadeseoDa taA ccess...
navigationItem.rightBarButtonItem = newItemButton
items = Dao().loadItems()
}
No momento em que salvamos os dados, vamos chamar o método
saveItemsparaguardarositensnoarquivo:
func addNew(item: Item) {
items.append(item)
Dao().saveItems(items)
if let table = tableView {
table.reloadData()
} else {
Alert(controller: self).show(message:
"Unexpected error, but the item was added.")
}
}
Com o ViewController certo, vamos arrumar agora o
MealsTableViewController para buscar e salvar as refeições utili-
zando os métodos loadMeals e saveMeals, removendo todo o código
anteriordemanipulaçãodoarquivo:
override func viewDidLoad() {
meals = Dao().loadMeals()
}
func add(meal: Meal) {
meals.append(meal)
Dao().saveMeals(meals)
tableView.reloadData()
}
Rodamosnovamenteenossaaplicaçãocontinuafuncionandodamesma
forma.
Resumo
Tiramos responsabilidades exageradas de nossos controllers, isolando a
funcionalidadedemanipulaçãodoarquivo,quenaverdadeéadeacessoaos
253

## Página 260

CasadoCódigo
dados,emumaúnicaclasse. Aindanãoosdeixamoscomumaúnicarespon-
sabilidade, mas essa refatoração é mais um passo a caminho de um código
maisfácildesemanter. Aprendemoscomissoopadrãodeprojetochamado
Data Access Object ,oD A O .
Vimos também quando devemos quebrar essa responsabilidade em pe-
daços ainda menores e como a nomenclatura de métodos e variáveis pode
influenciaralegibilidadedenossocódigo.
254

## Página 261

Capítulo17
Aondechegamosepróximos
passos
P as sa mosj un t ospo rumalo n gajo rnada.J un t ospo isoli vr of o iescri t oàme-
dida que a linguagem se desenvolvia, desde suas versões beta (junto com o
XcodeeYosemitetambémbeta),commuitasmudançasnocaminho.
A visão geral da linguagem e mais aprofundada de alguns tópicos cria
aqui uma base da linguagem que nos permite primeiramente escrever um
código mais bonito. Não estou falando de beleza por ter menos linhas ou
ser funcional. A beleza de ter um código que funciona e que foi escrito com
outrosdesenvolvedoresemmente-comapreocupaçãodamanutenção.
A utilização de boas práticas e padrões de projeto nos ajudam a atingir
taisobjetivos.
Apartirdeagora, descobrirnovasfuncionalidadesdalinguagem,explo-

## Página 262

CasadoCódigo
rar novas APIs, utilizar novas bibliotecas etc. passa a ser seu trabalho do dia
a dia. Coloque tudo o que viu até aqui em prática, e que a nova geração de
desenvolvedoresiOSaproveiteasmelhorescaracterísticasdalinguagemeda
APIparaamudançadomundoemquevivemos.
Boajornada.
256

## Página 263

CasadoCódigo ÍndiceRemissivo
ÍndiceRemissivo
Boa prática ou Code smell? O Story-
b o a r déu m as o l u ç ã od o
bemo udomal?,154
Boaprática: constantes,42
Boa prática: crie um diretório por
grupo,74
Boa prática: cuidado com inferência
detipos, 52
Boa prática: desserialização na inici-
alização,234
Boaprática: encapsulamento,69
Boa prática: evite optional, garanta
tudocomiflet, 200
Boa prática: Good citizen (evite nu-
los),63
Boa prática: mensagens de erro des-
critivas,202
Boaprática:organizandoosdados, 55
Boaprática: OrientaçãoaObjetos, 56
Boa prática: placeholder e keyboard
type,23
Boa prática: recarregue os dados de
umatabela, 131
Boa prática: Single Responsibility
Principle, Princípio de Res-
ponsabilidadeÚnica, 208
Code smell (mal cheiro de código):
opcional,70
Codesmell: cast,183
Codesmell: closuresarodo, 225
Codesmell: comentárioslongos, 43
Codesmell: ComonãoaprenderOri-
entaçãoaObjetos: Getterse
Setters,64
Codesmell: Nestedifs, 210
Codesmell: nomesgenéricosdemais
e como extrair um proto-
colo,131
Codesmell: usandocomponentesUI
comoparâmetrosemobser-
verseoswi tch,218
Designpattern: delegate,123
Má prática: muitossegues com parâ-
metros,135
257