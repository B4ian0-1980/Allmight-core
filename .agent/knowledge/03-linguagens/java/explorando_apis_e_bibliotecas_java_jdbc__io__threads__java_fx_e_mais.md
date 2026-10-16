---json
{
  "id": "explorando_apis_e_bibliotecas_java_jdbc__io__threads__java_fx_e_mais",
  "title": "Explorando APIs e bibliotecas Java JDBC, IO, Threads, Java FX e mais",
  "categoria": "03-linguagens",
  "subcategoria": "java",
  "resumo": "**Arquivo Original:** `Explorando APIs e bibliotecas Java JDBC, IO, Threads, Java FX e mais.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "apis",
    "bibliotecas",
    "explorando",
    "java",
    "jdbc",
    "linguagens",
    "mais",
    "threads"
  ],
  "perguntas_tipo": [
    "Como utilizar Explorando APIs e bibliotecas Java JDBC, IO, Threads, Java FX e mais?",
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

# Explorando APIs e bibliotecas Java JDBC, IO, Threads, Java FX e mais

> **Arquivo Original:** `Explorando APIs e bibliotecas Java JDBC, IO, Threads, Java FX e mais.pdf`
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

CasadoCódigo
“ÀsfamíliasBertoldo,FerreiraeTurini.”
–RodrigoTurini
i

## Página 5

CasadoCódigo
Agradecimentos
Emprimeirolugar,gostariamuitodeagradeceravocê,oleitor.Foiparavocê
quecuidadosamenteescreviesselivro,pensandosempreemcomoocon-
teúdopoderiaseraplicadoemseudiaadia. Esperoatendere,quemsabe,
superarassuasexpectativas.
Paraevitarconsequênciasimprevisíveis,nãopossodeixardeagradecerà
minhaesposaJordana. Semseuvaliosoincentivoestelivronãopassariade
umplano.EtambémparapequenaKatherine,quenessemomentoprovavel-
menteestáchutandoasuabarriga.
NãopossodeixardemencionarafamíliaSilveira,que,pramim,sãoos
maioresincentivadoresdomundo.AoPaulo,pelapresen ça,incentivoe men-
toring.AoGuilherme,pelasideias,pareamentosetodoconhecimentocom-
partilhado.EfinalmenteaoSr.Carlos,pelaculturaeinspiraç ãodiária.
Porfim,masnemumpoucomenosimportante,atodaequipedaCaelum
eAlura. EmespecialaoVictorHarada,poissemsuasideias,críticasedis-
cussões,boapartedestelivroseriadiferente.
iii

## Página 7

CasadoCódigo Sumário
Sumário
1 Introdu ção 1
1.1 Oprojetoeastecnologias . . . . . . . . . . . . . . . . . . . . . 1
1.2 InstalandoeconfigurandooEclipse . . . . . . . . . . . . . . . 2
1.3 Downloaddosarquivosproprojeto . . . . . . . . . . . . . . . 3
1.4 Acesseocódigodesselivro . . . . . . . . . . . . . . . . . . . . 4
1.5 Aproveitandoaomáximooconteúdo . . . . . . . . . . . . . . 5
1.6 Tirandosuasdúvidas . . . . . . . . . . . . . . . . . . . . . . . 5
2 Java FX 7
2.1 NossaprimeiraAppemJavaFX . . . . . . . . . . . . . . . . . 7
2.2 Configurandoalivraria-base . . . . . . . . . . . . . . . . . . . 11
2.3 Preparandonossocenário . . . . . . . . . . . . . . . . . . . . 13
2.4 Umalistagemdeprodutos . . . . . . . . . . . . . . . . . . . . 18
3 Java IO 29
3.1 Entradaesaídadedados . . . . . . . . . . . . . . . . . . . . . 29
3.2 Lendoumarquivodetexto . . . . . . . . . . . . . . . . . . . . 30
3.3 LendotextodotecladocomSystem.in . . . . . . . . . . . . . 34
3.4 TornandotudomaissimplescomScanner . . . . . . . . . . . 36
3.5 SaídadedadoseoOutputStream . . . . . . . . . . . . . . . . 38
3.6 EscritamaissimplescomPrintStream . . . . . . . . . . . . . 42
3.7 GerandoumCSVdeprodutos . . . . . . . . . . . . . . . . . . 43
3.8 Botãodeexportarprodutos . . . . . . . . . . . . . . . . . . . 48
3.9 AdicionandoaçõescomsetOnAction . . . . . . . . . . . . . . 49
3.10 JavaFxeJava8 . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
v

## Página 8

Sumário CasadoCódigo
4 Banco de Dados e JDBC 57
4.1 IniciandocomMySQL . . . . . . . . . . . . . . . . . . . . . . 57
4.2 Criandoatabeladeprodutos . . . . . . . . . . . . . . . . . . . 60
4.3 Opacotejava.sqleoJDBC . . . . . . . . . . . . . . . . . . . . 61
4.4 AbrindoconexãocomMySQLemJava . . . . . . . . . . . . . 63
4.5 Listandotodososprodutosdobanco . . . . . . . . . . . . . . 66
4.6 Importandoprodutosdeumdump . . . . . . . . . . . . . . . 69
4.7 Parasabermais:Adicionandoprogramaticamente . . . . . . 71
4.8 Qualamelhorformadefecharaconexão? . . . . . . . . . . . 75
4.9 OpadrãodeprojetoDAO . . . . . . . . . . . . . . . . . . . . 78
5 Threads e Paralelismo 85
5.1 Processamentodemorado,eagora? . . . . . . . . . . . . . . . 86
5.2 Trabalhandocom ThreadsemJava. . . . . . . . . . . . . . . 87
5.3 OcontratoRunnable . . . . . . . . . . . . . . . . . . . . . . . 89
5.4 Threadscomclassesanônimaselambdas . . . . . . . . . . . 91
5.5 Exportandoemumathreadseparada . . . . . . . . . . . . . . 94
5.6 Umpoucomaissobreas Threads. . . . . . . . . . . . . . . . 99
5.7 GarbageCollector . . . . . . . . . . . . . . . . . . . . . . . . . 101
5.8 JavaFXassíncrono . . . . . . . . . . . . . . . . . . . . . . . . . 103
5.9 TrabalhandocomaclasseTask . . . . . . . . . . . . . . . . . . 104
5.10 Códigofinalcomesemlambdas . . . . . . . . . . . . . . . . . 112
6 CSS no Java FX 117
6.1 SeuprimeiroCSSnoJavaFX . . . . . . . . . . . . . . . . . . . 118
6.2 Extraindoestilospraumarquivo.css . . . . . . . . . . . . . . 120
7 JAR, bibliotecas e build 135
7.1 JAR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
7.2 GerandoJARexecutávelpelaIDE . . . . . . . . . . . . . . . . 136
7.3 Executandoalivraria-fx.jar . . . . . . . . . . . . . . . . . . . . 138
7.4 BibliotecasemJava . . . . . . . . . . . . . . . . . . . . . . . . 140
7.5 DocumentandoseuprojetocomJavadoc . . . . . . . . . . . . 141
vi

## Página 9

CasadoCódigo Sumário
7.6 AutomatizandobuildcomMaven . . . . . . . . . . . . . . . . 146
7.7 TransformandonossaappemumprojetoMaven . . . . . . . 147
7.8 AdicionandoasdependênciascomMaven . . . . . . . . . . . 151
7.9 ExecutandoalgumastasksdoMaven . . . . . . . . . . . . . . 157
7.10 AdicionandoplugindoJavaFX . . . . . . . . . . . . . . . . . 159
7.11 Mavennalinhadecomando . . . . . . . . . . . . . . . . . . . 163
7.12 Comoficounossopom.xml . . . . . . . . . . . . . . . . . . . 165
8 Refatorações 169
8.1 Refatoração . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170
8.2 OstãopopularesDesignPatterns . . . . . . . . . . . . . . . . 175
9 Próximos passos com Java 179
9.1 Entreemcontatoconosco . . . . . . . . . . . . . . . . . . . . 180
vii

## Página 11

Capítulo1
Introdução
1.1 O projeto e as tecnologias
Duranteestelivro,trabalharemosnoprojetodeumalivraria. Aprincípio,
vamoscriarumalistagemdeprodutoscom JavaFXeaodecorrerdoscapítu-
losincrementaremossuasfuncionalidades,passandopelas APIsdeIO,JDBC,
Threadsemuitomais.Alémdisso,atodoomomentodiscutiremossobreboas
práticasdaorientaçãoaobjetose designpatterns.
Aofinal,oprojetodeveficarparecidocom:

## Página 12

1.2. InstalandoeconfigurandooEclipse CasadoCódigo
Fig.1.1:Aparênciafinaldoprojetodestelivro
EssalistagemdelivrosécarregadadeumbancodedadosMySQL,uti-
lizandoaAPIde JDBC.O buildegerenciamentodedependênciasétotal-
menteautomatizado,comusodotãopopularMaven.Aaç ãodeexportaros
livroséfeitaemuma Threaddiferente,querodaemparalelocoma Thread
principaldaaplicação.
NossocódigojáusaráasintaxeerecursosdoJava8,comoasfamosasex-
pressõeslambdas.Masnãosepreocupe,vocênãoprecisaconhecerJava8ou
nenhumaoutratecnologiaalémdeJavapuroparacontinuar,cadanovidade
serámuitobemdetalhada.Prontoparacome çar?
1.2 I nstalando e configurando o Eclipse
Paracomeçar,vocêprecisarádoEclipseouqualqueroutraIDEdesuaprefer-
ência.UtilizareioEclipseemmeusexemplos,devidoaoganhodeprodutivi-
2

## Página 13

CasadoCódigo Capítulo1. Introdução
dade(queserámencionadoemalgunspontosdolivro),alémdesuapopu-
laridadenomercadoeinstituiçõesdeensino. Sequiser,vocêpodefazero
downloaddoEclipseem:
https://www.eclipse.org/downloads/
ParautilizaroJavaFXnoEclipse,vocêtambémprecisarádo e(fx)clipse,
quepodeserbaixadopeloseguintelink,noqualvocêtambémencontraráum
passoapassoparainstalá-lo.
http://www.eclipse.org/efxclipse/install.html
Algumas outras opções
AlémdoEclipse,existemdiversasoutrasIDEsquepodemserutilizadas
nodesenvolvimentodesseprojeto. NetbeanseIntellijIDEAsãoalgumasdelas.
ONetbeansjávemcomsuporteaoJavaFX,sendoassimvocênãoprecisará
instalarnada.Vocêpodelermaissobreeleefazerodownloadem:
https://netbeans.org/
Segundoaspesquisasmaisrecentes,logodepoisdoEclipse,o IntellijIDEA
éaIDEmaisutilizadapelosdesenvolvedoresJava.Masháumaquestão:ela
épaga.Vocêpodebaixarumaversão CommunityEdition(gratuita),masela
deixaumpoucoadesejar. Sequiserexperimentaraversãocompleta,tem
comoopçãobaixarum trialpor30dias.
https://www.jetbrains.com/idea/
ApesardeutilizamosEclipsenosexemplosdesselivro,vocêpodeusara
IDEdesuapreferência.Fiqueàvontadeemsuaescolha.
1.3 D ownload dos arquivos pro projeto
Nolinkaseguir,vocêencontrarátodososarquivosnecessáriosparaacom-
panharativamenteoscódigosdesselivro.Eleincluiabasedoprojeto,os jars
necessáriosparavocêfazerosexercícios,umarquivode dumpcomalguns
livrosjácadastradosnobanco,entreoutros.
http://goo.gl/CfzTLB
3

## Página 14

1.4. Acesseocódigodesselivro CasadoCódigo
Desbrav ando a Orientação a Objetos
Sevocêjáleumeulivro DesbravandoaOrienta çãoaObjetos,perce-
beráqueestaéumaevoluçãodoprojetoquedesenvolvemosporlá.Você
podecontinuarcomseupróprioprojeto,oubaixaroprojetojáprontose
preferir.
Fig.1.2:DesbravandoJavaeOrientaçãoaObjetos
http://www.casadocodigo.com.br/products/
livro-orientacao-objetos-java
1.4 A cesse o código desse livro
Todososexemplosdesselivroetambémseucódigofinal,emJava7e8,podem
serencontradosnoseguinterepositório:
• https://github.com/Turini/livro-java
Nãodeixedeescrevertodososcódigoseexercitá-losduranteoscapítulos.
Assimvocêpodetirarumproveitomaiordoconteúdo.Váalémdoqueéaqui
sugerido,escrevanovostestes,novoslayoutsenãodeixedecompartilharsua
experiênciaconosco.
4

## Página 15

CasadoCódigo Capítulo1. Introdução
1.5 A proveitando ao máximo o conteúdo
Alémdecolocartodososexemplosemprática,nãodeixedeconsultartam-
bémadocumentaçãodecadaAPIebibliotecaquevamosutilizar.Eusempre
disponibilizoalgunslinksquepodemserúteisquandoumnovoassuntoé
introduzido.
ComonossofocoprincipaléJava,tenhasempreporpertoadocumen-
taçãodalinguagem:
http://docs.oracle.com/javase/8/docs/api/
Seestiverdevidamenteconfigurado,vocêpodeveradocumentaç ãodas
classesemétodospelopróprioEclipse.Semprequeestouconhecendouma
nova API, costumo usar o recurso deautocomplete(atalho Control+
space)enavegarpelosseusmétodos.
Vejaque,quandoparamosemummétodoespecífico,um boxcomsua
documentaçãoéexibido:
Fig.1.3:ExplorandoaAPIdoJavapeloEclipse
1.6 T irando suas dúvidas
Ficoucomalgumadúvidaduranteolivro?Mandeume-mail!Umalistade
discussõesfoicriadaexclusivamenteparafacilitarseucontatocomigoecom
osdemaisleitoresdestelivro. Vocêpodeedevecompartilharsuasdúvidas,
ideias,sugestõesecriticas.Todasserãomuitobem-vindas.
https://groups.google.com/group/livro-java
5

## Página 16

1.6. Tirandosuasdúvidas CasadoCódigo
Outrorecursoquevocêpodeutilizarparaesclarecersuasdúvidasepar-
ticiparativamentenacomunidadeJavaéofórumdoGUJ.Lávocênãosó
podeperguntar,mastambémresponder,editar,comentareassistiradiversas
discussõessobreouniversodaprogramaç ão.
http://www.guj.com.br/
6

## Página 17

Capítulo2
JavaFX
2.1 N ossa primeira App em Jav aFX
Nestecapítulo,criaremosumatelasimplesusandoJavaFX,queservirácomo
baseparaintegrarmosalgumasdasoutrasAPIsqueveremosnodecorrerdo
livro. Apesardenossofoconãoserainterfacegráficaemsi,escolhemoso
JavaFXporserumaalternativamuitointeressanteemaismodernadoqueo
swing,alémdeserbastanteelegante.OJavaFXjáveminclusono JDKeJRE.
Criando o projeto no Eclipse
AgoraquejáconfiguramosnossoEclipseparaescreveraplicaçõesemJava
FX,podemoscriarumnovoprojeto.Parafazerisso,bastaclicarem File>
New> Other...eescolheraop ção Java FX Project.Podemoschamar
oprojetode livraria-fx,depoisclicarem finishparaconcluir.

## Página 18

2.1. NossaprimeiraAppemJavaFX CasadoCódigo
SevocêestiverutilizandoumaversãoatualdoEclipse(oqueébastante
recomendado),jádeveráaparecerumaestruturapadrãoparasuaaplicaç ão,
comonaseguinteimagem:
Fig.2.1:EstruturainicialdoprojetonoEclipse
Notequedentrodo src,temosumapacotechamado application
comaclasse Main.javaeoarquivo application.css. Veremosmais
detalhessobreessearquivo .cssmaisàfrente,porenquantovamosfocar
nocódigoJava.Aclasse Mainjádevetersidocriadacomoseguintecódigo:
public class Main extends Application {
@Override
public void start(Stage primaryStage) {
try {
BorderPane root = new BorderPane();
Scene scene = new Scene(root,400,400);
scene.getStylesheets()
.add(getClass().getResource("application.css")
.toExternalForm());
primaryStage.setScene(scene);
primaryStage.show();
} catch(Exception e) {
8

## Página 19

CasadoCódigo Capítulo2. JavaFX
e.printStackTrace();
}
}
public static void main(String[] args) {
launch(args );
}
}
NãosepreocupecasoemseuEclipse, ouqualqueroutraIDEdesua
preferência,essaclassenãotenhasidocriada.Vocêpodecriá-lafacilmente,
masaproveiteemantenhaapenasocódigoqueimportaagoranessecome ço.
Vamosapagaresse try catch elinhasquecriamaclasse Sceneeaplicam
oestilo css.Poragorasóprecisamosdoseguintecódigo:
public class Main extends Application {
@Override
public void start(Stage primaryStage) {
primaryStage.setTitle("Sistema da livraria com Java FX");
primaryStage.show();
}
public static void main(String[] args) {
launch(args );
}
}
NotequejáadicioneiumtituloquenãoexistianoarquivoJava,faç ao
mesmoeexecuteessaclasseparaveroprimeiroresultado. Setudocorreu
bem,umatelacinzacomotítulo SistemadalivrariacomJavaFX deveapare-
cer:
9

## Página 20

2.1. NossaprimeiraAppemJavaFX CasadoCódigo
Fig.2.2:PrimeiratelaemJavaFX
Executando código no Eclipse
CasonãoestejafamiliarizadocomoEclipse,vocêpodeexecutarseu
códigodediversasmaneiras.Umadelaséclicandocomobotãodireitona
classe,selecionando Run As... edepois Java Application.Outra
alternativabempráticaéutilizandooatalho Control + F11.
Excelente,játemosalgumresultado.Masantesdeseguirprecisamosen-
tenderumpoucomaissobreaanatomiadessenossoprimeirocódigo.
Podemoscomeçarpelaclasse javafx.application.Application.
Aregraésimples,aclasseprincipaldenossasaplicaçõesemJavaFXpre-
cisaherdarde Applicationeconsequentementesobrescreverseuúnico
métodoabstrato,chamado start. Esseéopontodepartidadetodaapli-
caçãoqueemJavaFX.
Vale lembrar que como esse método éabstrato, somos obrigados a
sobrescrevê-lo. Portanto,casovocênãolembredisso,ocompiladorcerta-
mentelhelembrarácomumerro.Alémdisso,percebaqueessemétodore-
10

## Página 21

CasadoCódigo Capítulo2. JavaFX
cebeumobjetodotipo Stagecomoparâmetro,queéo containerprincipal
daaplicação.
Porfim,notetambémquetemosummétodo main.Nele,invocamosum
outrométodochamado launch,tambémpresentenaclasse Application.
Eleéoresponsávelporiniciaraaplicação.
2.2 C onfigurando a livraria-base
Agora que já sabemos um pouco mais sobre esse código inicial, vamos
começaraimplementaranossalistagemde Produtos.Paraisso,precisare-
mosdainterface Produtoedesuasimplementações,presentesnoarquivo
quevocêdeveterbaixadonocapítuloanterior.Nãosepreocupesevocêainda
nãobaixou,vocêpodefazerissoagorapeloseguintelink:
http://goo.gl/CfzTLB
Apósconcluirodownload,vocêprecisaráimportaroprojetonoEclipse.
Primeiro,extraiaoconteúdodo ZIPquevocêbaixouparaalgumapastade
suapreferência.Agora,peloEclipse,cliquenomenu File, Import...e
depoisem Existing Projects into Workspace.
Fig.2.3:ImportandoprojetopeloEclipse.
Selecioneodiretório(em Browse...)ondevocêcolocouoprojeto
11

## Página 22

2.2. Configurandoalivraria-base CasadoCódigo
livraria-base, que estava dentro doZIP, e logo depois clique em
Finish.
Fig.2.4:Concluindoimportdoprojetobase.
Queremosagoravincularosdoisprojetos. Porenquanto,faremosisso
pelopróprioEclipse,clicandocomobotãodireitonoprojeto livraria-fx,
opção Build Path edepois Configure Build Path....
12

## Página 23

CasadoCódigo Capítulo2. JavaFX
Fig.2.5:BuildPath>ConfigureBuildPath...
VáàabaProjects,cliqueem Add,escolhaoprojeto livraria-base,
queacabamosdeimportar.Depoisbastaclicarem Ok.
Fig.2.6:Adicionandoprojetonobuildpath.
2.3 P reparando nosso cenário
Antesdecriarumatabela,precisamoscriarumcenário,ondeficarátodoo
conteúdodessanossatela.UmateladoJavaFXsempreécompostaporum
containerprincipal( Stage)etambémporumcenário,representadopela
classe Scene.Repareemsuaestrutura:
Scene scene = new Scene(root, largura, altura)
13

## Página 24

2.3. Preparandonossocenário CasadoCódigo
Osparâmetros largurae alturarepresentambemseusignificado,
nãoé?Definimosneleotamanhodonossocenário,dateladanossaaplicaç ão.
Jáesserootnadamaisédoqueumauxiliar,queajudanoprocessode layout,
comoaoadicionarouremoverelementos.
Otipodoparâmetro rootéjavafx.scene.Parent,queéumaclasse
abstrata. Deacordocomnossanecessidade,escolhemosumadesuasim-
plementações.Comoatelaserácompostapor2elementos(um labeleuma
tabela),podemosusarum Group.
14

## Página 25

CasadoCódigo Capítulo2. JavaFX
Outras implementações
Além do Group, temos como opções diretamente as classes
Control, Regione WebView. Alémdisso,cadaumadessastemdi-
versasoutras subclasses.Sãováriaspossibilidades!Umaop çãobastante
usadaéa GridPane,dopacote javafx.scene.layout.Elaéfilha
de Pane,queéfilhade Regionque,finalmente,éfilhade Parent.
Ufa!
Fig.2.7:Hierarquiadaclassejavafx.scene.layout.GridPane
Vocêpodeconhecerumpoucomaissobreessaeoutrasimplemen-
taçõesem:
https://docs.oracle.com/javafx/2/api/javafx/scene/Parent.html
Veremosdiversasdelasduranteolivro.
Ocódigodonossométodo startdeveficarparecidocom:
public void start( Stage primaryStage) {
Group group = new Group();
Scene scene = new Scene( group, 690, 510);
primaryStage.setScene(scene);
15

## Página 26

2.3. Preparandonossocenário CasadoCódigo
primaryStage.setTitle("Sistema da livraria com Java FX");
primaryStage.show();
}
Percebaqueestamoschamandoométodo setScene, vinculandoo
cenáriocomocontainerprincipal. Querveroresultado? Nãodeixedeex-
ecutarocódigoacadaevoluç ão.Agoraatelaestarámaiorecomumfundo
branco,padrãodocenário.
Opróximopassoserácolocarumtextonatela,indicandoqueessaseráa
nossalistagemdeprodutos.Faremosissocomaauxiliodaclasse Label,do
pacote javafx.scene.control.
Label label = new Label("Listagem de Livros");
Podemosagorautilizaraclasse Group, queestávinculadaaonosso
cenário, para adicionar esse novo elemento na página. Para fazer isso,
bastachamarseumétodo getChildreneadicionartodososelementos
necessários,quenestecasoseráapenaso label:
group.getChildren().addAll(label);
Ocódigocompletodométodo startdeveráficarassim:
public void start( Stage primaryStage) {
Group group = new Group();
Scene scene = new Scene( group, 690, 510);
Label label = new Label( "Listagem de Livros");
group.getChildren().addAll(label);
primaryStage.setScene(scene);
primaryStage.setTitle("Sistema da livraria com Java FX");
primaryStage.show();
}
Aorodaressecódigo,teremosasaídaesperada,masotextoestámuito
pequenoegrudadonasmargensdatela!
16

## Página 27

CasadoCódigo Capítulo2. JavaFX
Fig.2.8:Listagemcomolabeldesalinhado.
Paramelhorarumpoucoaaparênciadesse label,podemosmudarsua
fonteetambémadicionarum padding.Paraisso,vamosutilizarosmétodos
setFonte setPadding,comoaseguir:
Label label = new Label("Listagem de Livros");
label.setFont(Font
.font("Lucida Grande", FontPosture.REGULAR, 30));
label.setPadding(new Insets(20, 0, 10, 10));
Ométodoestático font,daclasse javafx.scene.text.Font,nos
possibilitapassarafamília,tipoetamanhodafontequequeremosaplicar
emnossotexto. Existemoutrassobrecargasdessemétodoparaaplicarape-
nasotamanho,apenasfamíliaeassimpordiante. Reparetambémqueno
setPaddingestamosutilizandoumaclasseauxiliarparapassarasmedidas,
a Insets.
Executeseucódigomaisumavezparaperceberoresultado:
17

## Página 28

2.4. Umalistagemdeprodutos CasadoCódigo
Fig.2.9:Listagemcomlabelalinhada.
Umpoucomelhor,nãoacha?Agorapodemospartirparaatabela!
2.4 U ma listagem de produtos
Nossopróximopassoserácriarumatabelaparaexibirnossalistadepro-
dutos. Antesdefocarnatabela, vamoscriarumanovaclassenopacote
repositorio,queseráresponsávelporretornaralistadeprodutosquede-
veráserexibida.Podemoschamá-lade RepositorioDeProdutos:
package repositorio;
public class RepositorioDeProdutos {
public ObservableList<Produto> lista() {
Autor autor = new Autor();
autor.setNome("Rodrigo Turini");
autor.setEmail("rodrigo.turini@caelum.com.br");
autor.setCpf("123.456.789.10");
Livro livro = new LivroFisico(autor);
livro.setNome("Java 8 Prático");
livro.setDescricao("Novos recursos da linguagem");
livro.setValor(59.90);
livro.setIsbn("978-85-66250-46-6");
18

## Página 29

CasadoCódigo Capítulo2. JavaFX
Livro maisUmlivro = new LivroFisico(autor);
maisUmlivro .setNome("Desbravando a O.O.");
maisUmlivro .setDescricao("Livro de Java e O.O");
maisUmlivro .setValor(59.90);
maisUmlivro .setIsbn("321-54-67890-11-2");
Autor outroAutor = new Autor();
outroAutor.setNome("Paulo Silveira");
outroAutor.setEmail("paulo.silveira@caelum.com.br");
outroAutor.setCpf("123.456.789.10");
Livro outroLivro = new LivroFisico(outroAutor );
outroLivro.setNome("Lógica de Programação");
outroLivro.setDescricao("Crie seus primeiros programas");
outroLivro.setValor(59.90);
outroLivro.setIsbn("978-85-66250-22-0");
return FXCollections
.observableArrayList(livro, maisUmlivro, outroLivro);
}
}
Por enquanto, estamos criando os livros e autores manualmente,
mas muito em breve faremos isso de uma forma bem mais interes-
sante. Você já deve ter notado que o tipo de retorno dessa lista é um
tanto diferente daquilo com que estamos acostumados, ela retorna uma
ObservableList<Produto>. Esse é o tipo de lista que a tabela do
Java FX espera receber. Criá-la é bem simples com o apoio da factory
FXCollections,dopacote javafx.collections:
ObservableList lista =
FXCollections.observableArrayList(...);
Agoraquejátemosumalista,podemosvoltarparaaclasse Mainecriar
umnovoelementoemnossocenário( Scene),umatabela.Parafazerisso,
utilizaremosaclasse TableView,comoaseguir:
ObservableList<Produto> produtos =
new RepositorioDeProdutos().lista();
19

## Página 30

2.4. Umalistagemdeprodutos CasadoCódigo
TableView tableView = new TableView<>(produtos);
Jáestamospassandoalistadeprodutosdo RepositorioDeProdutos
comoargumentoemseuconstrutor. Nessemomentoocódigodenosso
método startestáassim:
public void start( Stage primaryStage) {
Group group = new Group();
Scene scene = new Scene( group, 690, 510);
ObservableList<Produto> produtos =
new RepositorioDeProdutos().lista();
TableView tableView = new TableView<>(produtos);
Label label = new Label( "Listagem de Livros");
label.setFont(Font
.font("Lucida Grande", FontPosture.REGULAR, 30));
label.setPadding(new Insets(20, 0, 10, 10));
group.getChildren().addAll(label);
primaryStage.setScene(scene);
primaryStage.setTitle("Sistema da livraria com Java FX");
primaryStage.show();
}
Podemosagoracriarascolunasdenossatabela.Bastacriarumainstância
dotipo TableColumn,recebendoonomedacolunacomoparâmetro:
TableColumn nomeColumn = new TableColumn("Nome");
Alémdisso,paracadacolunaprecisamosdefinirsuafontededados,ou
seja,qualpropriedadedaclasse Produtodeveserexibidanessadetermi-
nadacoluna. Paraisso,chamamosseumétodo setCellValueFactory,
passandoumnovo PropertyValueFactorycomoparâmetro:
20

## Página 31

CasadoCódigo Capítulo2. JavaFX
TableColumn nomeColumn = new TableColumn("Nome");
nomeColumn.setCellValueFactory(
new PropertyValueFactory("nome"));
Opcionalmente,vocêpodedefinirumtamanhomínimoemáximopara
essacoluna,utilizandoseusmétodos setMinWidthe setMaxWidth.Um
exemploseria:
descColumn.setMinWidth(230);
Vamoscriarumacolunaparacadaumdosquatroatributosprincipais
denossos Produtos,seunome,descrição,valore ISBN(queéseucódigo
único).
Aofinal,seucódigodeveficarassim:
public void start( Stage primaryStage) {
Group group = new Group();
Scene scene = new Scene( group, 690, 510);
ObservableList<Produto> produtos =
new RepositorioDeProdutos().lista();
TableView tableView = new TableView(produtos );
TableColumn nomeColumn = new TableColumn("Nome");
nomeColumn .setMinWidth(180);
nomeColumn .setCellValueFactory(
new PropertyValueFactory("nome"));
TableColumn descColumn = new TableColumn("Descrição");
descColumn .setMinWidth(230);
descColumn .setCellValueFactory(
new PropertyValueFactory("descricao"));
TableColumn valorColumn = new TableColumn("Valor");
valorColumn.setMinWidth(60);
valorColumn.setCellValueFactory(
21

## Página 32

2.4. Umalistagemdeprodutos CasadoCódigo
new PropertyValueFactory("valor"));
TableColumn isbnColumn = new TableColumn("ISBN");
isbnColumn .setMinWidth(180);
isbnColumn .setCellValueFactory(
new PropertyValueFactory("isbn"));
Label label = new Label( "Listagem de Livros");
label.setFont(Font
.font("Lucida Grande", FontPosture.REGULAR, 30));
label.setPadding(new Insets(20, 0, 10, 10));
group.getChildren().addAll(label);
primaryStage.setScene(scene);
primaryStage.setTitle("Sistema da livraria com Java FX");
primaryStage.show();
}
Porfim,vamosadicionarascolunasnatabelaedepoisadicioná-laao
nossocenário:
tableView.getColumns().addAll(nomeColumn,
descColumn , valorColumn, isbnColumn);
group.getChildren().addAll(label, tableView);
Aoexecutarocódigo,atabelaestarápopuladacomoesperamos,masto-
talmentedesalinhadaeescondendoanossa Label:
22

## Página 33

CasadoCódigo Capítulo2. JavaFX
Fig.2.10:TableViewdesalinhada,cobrindoolabel.
Para resolver o problema, vamos envolver essatableViewem um
VBox.Esseelementovainosajudaraalinharatabela,jáquepodemosdefinir
um padding,comoaseguir:
VBox vbox = new VBox(tableView);
vbox.setPadding(new Insets(70, 0, 0 ,10));
Bastaadicionaressenovoitememnossocenário,assimcomofizemos
comatabela:
group.getChildren().addAll(label, vbox);
Ocódigofinaldasuaclasse Maindeveficarassim:
package application;
import javafx.application.Application;
import javafx.collections.ObservableList;
23

## Página 34

2.4. Umalistagemdeprodutos CasadoCódigo
import javafx.geometry.Insets;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.VBox;
import javafx.scene.text.Font;
import javafx.scene.text.FontPosture;
import javafx.stage.Stage;
import repositorio.RepositorioDeProdutos;
import br.com.casadocodigo.livraria.produtos.Produto;
public class Main extends Application {
@Override
public void start(Stage primaryStage) {
Group group = new Group();
Scene scene = new Scene( group, 690, 510);
ObservableList<Produto> produtos =
new RepositorioDeProdutos().lista();
TableView <Produto> tableView = new TableView<>(produtos);
TableColumn nomeColumn = new TableColumn("Nome");
nomeColumn.setMinWidth(180);
nomeColumn.setCellValueFactory(
new PropertyValueFactory("nome"));
TableColumn descColumn = new TableColumn("Descrição");
descColumn.setMinWidth(230);
descColumn.setCellValueFactory(
new PropertyValueFactory("descricao"));
TableColumn valorColumn = new TableColumn("Valor");
valorColumn.setMinWidth(60);
24

## Página 35

CasadoCódigo Capítulo2. JavaFX
valorColumn.setCellValueFactory(
new PropertyValueFactory("valor"));
TableColumn isbnColumn = new TableColumn("ISBN");
isbnColumn.setMinWidth(180);
isbnColumn.setCellValueFactory(
new PropertyValueFactory("isbn"));
tableView.getColumns().addAll(nomeColumn, descColumn,
valorColumn, isbnColumn);
final VBox vbox = new VBox(tableView);
vbox.setPadding(new Insets(70, 0, 0 ,10));
Label label = new Label("Listagem de Livros");
label.setFont(Font
.font("Lucida Grande", FontPosture.REGULAR, 30));
label.setPadding(new Insets(20, 0, 10, 10));
group.getChildren().addAll(label, vbox);
primaryStage.setTitle("Sistema da livraria com Java FX");
primaryStage.setScene(scene);
primaryStage.show();
}
public static void main(String[] args) {
launch(args );
}
}
Aoexecutá-lo,teremoscomoresultadoumatelaparecidacom:
25

## Página 36

2.4. Umalistagemdeprodutos CasadoCódigo
Fig.2.11:Listagemdeprodutoscomoselementosalinhados.
26

## Página 37

CasadoCódigo Capítulo2. JavaFX
Usando @SuppressWarnings no Eclipse
Paraevitarosdiversosalertas(warning s)emamarelonoEclipse,você
podeadicionarsobasuaclasseaanotaç ão @SuppressWarnings:
@SuppressWarnings({ "unchecked", "rawtypes" })
public class Main extends Application {
@Override
public void start(Stage primaryStage) {
Group group = new Group();
Scene scene = new Scene(group, 690, 510);
// restante do código omitido
}
Esseswarningsacontecemporcausadosparâmetrosgenéricos,que
optamosnãopassarparasimplificareevitartantarepetiç ãoemnosso
código. Nãosepreocupecomisso,voltaremosafalardissonofinaldo
livro.Porenquanto,vocêpodedeixaros warnings(ocódigofuncionará
normalmente),ouadicionaraanotação @SuppressWarnings.
Excelente,játemosumainterfacevisualparanossoprojeto.Aodecorrer
dolivro,trabalharemoscomleituraeescritaemarquivos,acessoabancode
dadosemais.Acadanovocapítuloumaoumaisnovasfuncionalidadesserão
adicionadasànossaaplicação.
27

## Página 38

2.4. Umalistagemdeprodutos CasadoCódigo
Mais sobre Jav aFx
SevocêgostoudoJavaFXequiserestudarumpoucomaisafundo,
talvezqueiradarumaolhadaemsuapáginanositedaOracle:
http://www.oracle.com/technetwork/java/javase/overview/
javafx-overview-2158620.html?ssSourceSiteId=otnpt
Nelavocêencontraumoverviewsobreatecnologiaelinksparadoc-
umentação,exemplosemuitomais.
28

## Página 39

Capítulo3
JavaIO
3.1 E ntrada e saída de dados
Nossa listagem ainda trabalha com valores fixos, definidos no
RepositorioDeProdutos. Apesar disso, já queremos adicionar uma
funçãodeexportarosdadosdessalistagemparaumarquivodetexto. Ao
clicarnobotãodeexportar,umarquivodeverásergeradocomosdadosda
listagem.
Trabalharcomentradaesaídadedadoséumanecessidadecompleta-
mentenaturalnosmaisdiferentestiposdeprojetos.Lervaloresdigitadospelo
teclado,lerouescreveremumarquivodediferentesformatosetc.,conhecer
aAPIdecontroledeentradaesaída,ou IOcomoécomumentechamada,é
umpassofundamental.Esseseránossoobjetivoduranteessecapítulo.

## Página 40

3.2. Lendoumarquivodetexto CasadoCódigo
3.2 L endo um arquivo de texto
Jávamoscomeçardeformaprática,queremosleroconteúdodeumarquivo.
Paracomeçaratestar,crienaraizdoseuprojeto(pasta livraria-fx)um
arquivochamado teste.txt.
Adicionenessearquivooseguinteconteúdo:
Esse é um teste de leitura de arquivo
Queremos ler o conteúdo de todas as linhas
Mas como ler arquivos em Java?
Umaformadeleroarquivoseriautilizandoum FileInputStream,
responsávelporfazeraleituradebytesdeumarquivo. Oconstrutordessa
classenosobrigapassaronomedoarquivoqueserálido,quenestecasoserá
teste.txt:
try {
InputStream is = new FileInputStream("teste.txt");
} catch (FileNotFoundException e) {
System.out.println("Arquivo não encontrado "+ e);
}
Quandoestamostrabalhandocomopacote java.io,grandepartede
seusmétodoslançam IOException.Comoessaéuma CheckedException
(nãoevitável),somosobrigadosatratá-laoudeclará-lacomum throws.Em
meuexemplo,euopteiportratar,imprimindoumamensagemamigávelno
console.
Outro detalhe importante é que declaramos o tipo da classe
FileInputStream como InputStream, que é suasuperclasse. Essa
é uma classe abstrata e tem diversas outras implementações, como
AudioInputStreame ByteArrayInputStream.
30

## Página 41

CasadoCódigo Capítulo3. JavaIO
Fig.3.1:InputStreamealgumasdesuassubclasses
Agrandeideiado InputStreaméqueelaimplementaocomporta-
mentoemcomumentreosdiferentestiposdeentrada. Alémdelerum
arquivodetexto,podemosprecisarlerdeumáudio,umaconexãoremota
(comsockets)etc.Cadatipodeleituraterásuasparticularidades,masaclasse
InputStream define o comportamento padrão entre elas.
Qualavantagemdessaabstração?Ébemsimples,podemostirarproveito
do polimorfismo.Imagineummétodoquerecebeum InputStreampara
fazerumaleituradebytes. Deondeosdadosvirão? Deum txt? Deum
blobdobancodedados?Nãoimporta.Independentedeondeosdadosvêm,
oprocessodeleituraseráomesmo.Quandoprecisarmoslerbytes,nãoim-
portandodeonde,poderemoschamarummétodoqueaceitaqualquerim-
plementaçãode InputStream.
31

## Página 42

3.2. Lendoumarquivodetexto CasadoCódigo
Fig.3.2:MétodorecebendoumInputStreamcomoparâmetro.
O padrão de projeto template method
Essaabstraçãoutilizadanaclasse InputStreamilustraumpadrão
deprojeto,ou DesignPattern,bastanteconhecidoeinteressante.Estamos
falandodo TemplateMethod.
HáumpostnoblogdaCaelumqueseaprofundabemnesseexemplo:
http://blog.caelum.com.br/design-patterns-no-java-se-o-template-method/
Omesmoacontececom OutputStream, quelogoveremos. Assim
como usaremos InputStream para leitura de bytes, podemos usar o
OutputStreamparaescrita. Opacotede java.iousaeabusadaorien-
taçãoaobjetos,comclassesabstratas,interfacese muito polimorfismo.
Paraconcluiraleituradoarquivo,precisamostransformarosbytesdesse
arquivoemunicode,guardandoumconjuntode chars. Emseguida,con-
catenaresseconjuntode charsparaformaras Stringscomoconteúdode
cadaumadesuaslinhas.
Parecebemtrabalhoso,nãoé?MasaAPIébemsimples,vocêveráque
essecódigoébempadrão.Logotambémveremosalgumasclassesdopacote
java.utilquesimplificamtodoesseprocesso,masprimeiro,éimportante
entendê-lo.
32

## Página 43

CasadoCódigo Capítulo3. JavaIO
Deformavisual,ofluxopadrãodeentradaé:
Fig.3.3:Etapasdofluxopadrãodeentrada
Easresponsáveisporessetrabalho:
Fig.3.4:InputStream,InputStreamReadereBufferedReader
Jáconhecemosa InputStream. Asclasses InputStreamReadere
BufferedReadersãoasresponsáveisporfazerorestantedotrabalho,ler
charsetransformá-lasem Strings:
try {
InputStream is = new FileInputStream("teste.txt");
InputStreamReader isr = new InputStreamReader(is);
BufferedReader reader = new BufferedReader(isr);
String linha = reader.readLine();
while (linha != null ) {
System.out.println(linha);
linha = reader.readLine();
}
reader.close();
} catch (IOException e) {
System.out.println("Erro ao tentar ler o arquivo " + e);
}
Acadachamada,ométodo readLinelêumalinhaemudaocursorpara
apróxima,atéqueoarquivoacabe.Nestecaso,retornará null.
33

## Página 44

3.3. LendotextodotecladocomSystem.in CasadoCódigo
Escrevaeexecuteessecódigoevocêveráquetodasaslinhasdoarquivo
serãoimpressasnoconsole.Legal,nãoé?
3.3 L endo texto do teclado com System.in
Querumaprovadequeaabstraç ãoutilizadano InputStreaméinteres-
sante? Vejacomoésimplesmudarnossocódigoparaquepassealerdo
tecladoemvezdeumarquivo:
try {
InputStream is = System.in;
InputStreamReader isr = new InputStreamReader(is);
BufferedReader reader = new BufferedReader(isr);
String linha = reader .readLine();
while (linha != null) {
System.out.println(linha);
linha = reader.readLine();
}
reader.close();
} catch (IOException e ) {
System.out.println("Erro ao tentar ler o arquivo " + e);
}
Percebeu a diferença? Ela está apenas na primeira linha, quando
declaramos o InputStream. Tudo que precisamos fazer foi utilizar o
System.in,queéaimplementaçãodo InputStreamresponsávelporesse
tipodeleitura,doteclado.
Executeométodoparaveroresultado.Oconsoleficaráembranco,es-
perandoqueumtextosejadigitado.Digitequalquercoisaepressione Enter,
ovalorseráimpressodevoltanoconsole.Percebaque,diferentedequando
estamoslendodeumarquivo,nestecasoa linhanuncaseránula.Portanto,
ocódigoficaráem looping,sempreesperandoumanovaentrada.
34

## Página 45

CasadoCódigo Capítulo3. JavaIO
Fig.3.5:ExemplodesaídadoSystem.in
35

## Página 46

3.4. TornandotudomaissimplescomScanner CasadoCódigo
Encerrando execução manualmente ou com EOF
Parapararaaplicaçãoqueestáem looping,aguardandoapróxima
entradadoteclado,vocêpodepeloEclipseclicarnoíconede stop.
Fig.3.6:ComointerromperaexecuçãopeloEclipse
Outraalternativaseriamandarumsinaldefimde stream,ocon-
hecido EOF(endoffile).Emsistemasoperacionaisdebase :Unix,como
LinuxeMacOS,vocêfazissocomocomando Control+ D.PeloWin-
dowsocomandoserá Control+ Z.
3.4 T ornando tudo mais simples com Scanner
Émuitointeressanteconheceressaanatomiado InputStreamparaentrada
dedados,masarealidadeéquedessaformaoprocessoémuitoverboso,com
todasessasetapas.Háumamaneiramaisatualeinteressante.
Podemosfazeramesmaleituradoarquivo teste.txtutilizandoa
classe Scanner,presentenopacote java.util. Reparecomoocódigo
émaisdeclarativo:
Scanner sc = new Scanner( new File("teste.txt"));
while (sc.hasNextLine()) {
36

## Página 47

CasadoCódigo Capítulo3. JavaIO
System.out.println(sc.nextLine());
}
Executeocódigoevocêperceberáqueasaídaseráamesma. Muito
maissimples,nãoacha? O java.util.ScannersurgiunoJava5etem
umasériedemétodosúteisparafacilitarseutrabalhocomleituradeum
InputStream.Métodoscomo nextDouble,quejálêosbytesefazacon-
versão,podemserbastanteconvenientesnotrabalhododiaadia.
Conhecendo a API
Durante a leitura, não deixe de se aprofundar ainda mais pelo
assunto consultando a documentação das classes mencionadas. O
java.util.Scanner,porexemplo,estábemdocumentadoem:
http://docs.oracle.com/javase/8/docs/api/java/util/Scanner.html
Vejaqueaprópriadocumentaçãodaclasse,logonoinício,jámostra
algunstrechosdecódigocomoexemplo.
Notecomoficanossocódigodeentradadotecladocomessaclasse:
Scanner sc = new Scanner( System.in);
System.out.println("Digite seu nome");
String nomeDigitado = sc.nextLine();
System.out.println("Digite sua idade");
int idadeDigitada = sc.nextInt();
System.out.println("Nome: " + nomeDigitado);
System.out.println("Idade: " + idadeDigitada);
Bastoumudaro InputStreampassadonoconstrutordo Scannerpara
o System.in,quejávimos.Notetambémqueestamosutilizandoométodo
nextIntpararecuperarovalorejáconverterparauminteiro,casocontrário
serianecessáriofazeressaconversãomanualmente.Porexemplo:
String idadeDigitada = sc.nextLine();
int idade = Integer.parseInt(idadeDigitada);
ExerciteessecódigoparairsefamiliarizandocomaAPI,escrevaeexecute
emseuprojeto.Umexemplodesaídaseria:
37

## Página 48

3.5. SaídadedadoseoOutputStream CasadoCódigo
Digite seu nome
> Rodrigo Turini
Digite sua idade
> 25
Nome: Rodrigo Turini
Idade: 25
3.5 S aída de dados e oOutputS tream
O processo de escrita (saída de dados) é muito parecido, mas no lu-
gar de InputStream, InputStreamReader e BufferedReader,
temos respectivamente o OutputStream, OutputStreamWriter e
BufferedWriter.
Fig.3.7:OutputStream,OutputStreamWritereBufferedWriter
Umexemplodeusoseria:
OutputStream os = new FileOutputStream("saida.txt");
OutputStreamWriter osw = new OutputStreamWriter(os);
BufferedWriter bw = new BufferedWriter(osw);
Noteque,agora,nolugardelerdeumarquivoexistente,estamoscriando
umnovo,nestecasochamado saida.txt.Tambémsomosobrigadosapas-
saressainformaçãonoconstrutordaclasse FileOutputStream.
Por sinal, note novamente o polimorfismo em ação. Usamos um
FileOutputStream,masdissemosqueseutipoé OutputStream. Há
umaimplementaçãoparacadatipodeescrita:
38

## Página 49

CasadoCódigo Capítulo3. JavaIO
Fig.3.8:OutputStreamealgumasdesuassubclasses
Podemosutilizarométodo writeparaescritadoarquivo,maselenão
fazumaquebradelinha. Umaalternativaparaissoseriachamarométodo
newLine,quecarregaessaresponsabilidade.
bw.write("Testando a escrita em arquivo");
bw.newLine();
bw.write("Conteúdo na próxima linha");
Ousimplesmenteconcatenarum /nna String:
bw.write("Testando a escrita em arquivo\n");
bw.write("Conteúdo na próxima linha");
39

## Página 50

3.5. SaídadedadoseoOutputStream CasadoCódigo
Fechando o arquivo com close
Éfundamentalsemprefecharmosoarquivo,chamandoseumétodo
close. Ao chamar o métodoclose de um BufferedWriter,
ele já fará o trabalho de fechar oOutputStreamWriter e
FileOutputStreamparavocê.Emcascata.
Casovocêseesque çadefecharoarquivonesseexemplo,queéum
programaminúsculo,eleprovavelmentenãovaifazeraescritanoar-
quivo(os bytesficamno bufferdoescritor).Seforumaaplicaçãomaior,
opróprioJavafecharáo BufferedWriterparavocêemalgummo-
mento(porcausado garbagecollector,queveremosmaisàfrente).Mas
nuncadevemosdeixardefecharumarquivoesperandoqueissoacon-
teça,sempredevemoschamaro closequandoterminarmosdefazer
umaescritaouleitura(um io).
No próximo capítulo, veremos uma forma bem interessante de
fechar recursos, como um arquivo ou mesmo uma conexão com
banco de dados. Vamos aprender que isso pode e deve ser feito
emumbloco finally,ouaindacomumrecursoconhecidocomo
try-with-resources.
Pronto,agoraquejásabemosissopodemoscriarumanovaclassedeteste
paraveressecódigoemaç ão.Crieaclasse TesteSaidaparafazeralguns
testes,elapodeseparecercom:
public class TesteSaida {
public static void main(String[] args)
throws IOException {
OutputStream os = new FileOutputStream("saida.txt");
OutputStreamWriter osw = new OutputStreamWriter(os);
BufferedWriter bw = new BufferedWriter(osw);
bw.write( "Testando a escrita em arquivo");
bw.newLine();
40

## Página 51

CasadoCódigo Capítulo3. JavaIO
bw.write("Conteúdo na próxima linha");
bw.close();
}
}
Executeocódigoparaveroresultado.UmpontoimportanteéqueaIDE
normalmentenãoatualizaoseuprojetoautomaticamentesevocêcriarum
arquivoporforadela,portanto,nãoseesque çadedarum F5(refresh)no
projetoapósexecutaraclasseparaqueoarquivo saida.txtfiquevisível.
Fig.3.9:Arquivosaida.txtnoEclipse
Sóporcuriosidade,sequiservocêpodetestarmudaraimplementaç ãode
OutputStream,assimcomofizemosnoexemplodeescrita. Experimente
usaro System.out:
public class TesteSaida {
public static void main(String[] args)
throws IOException {
OutputStream os = System.out;
OutputStreamWriter osw = new OutputStreamWriter(os);
BufferedWriter bw = new BufferedWriter(osw);
41

## Página 52

3.6. EscritamaissimplescomPrintStream CasadoCódigo
bw.write("Testando a escrita em arquivo");
bw.newLine();
bw.write("Conteúdo na próxima linha");
bw.close();
}
}
Simples,nãoé?Amudan çafoimínimaejátemosacapacidadedeescr-
everemoutrolocal,alémdeumarquivo.Asaídaserá:
Testando a escrita em arquivo
Conteúdo na próxima linha
Mas,claro,nessecasoespecíficoum System.out.printlnseriamuito
maissimples.Porfalaremsimplicidade,veremosagoracomosimplificaresse
processodeescrita.
3.6 E scrita mais simples com PrintS tream
Assimcomoo java.util.Scannerfacilitaoprocessodeleituradebytes,
desdeoJava5temosumaformamaisinteressantedefazeresseprocessodees-
crita,comaclasse java.io.PrintStream.Reparecomoficanossocódigo
utilizando-a:
PrintStream out = new PrintStream("saida.txt");
out.println("Testando a escrita em arquivo");
out.println("Conteúdo na próxima linha");
out.close();
Muitomaissimples,nãoacha? AchouessaAPIfamiliar? Naverdade,
vocêprovavelmentejávemusandoindiretamenteo PrintStreamdesdeo
seuprimeiro helloworldemJava,poisesteéotipodoatributo outdaclasse
System.Repare:
PrintStream out = System.out;
out.println("agora a saída é no console");
out.println("Conteúdo na próxima linha");
42

## Página 53

CasadoCódigo Capítulo3. JavaIO
Ambasasclasses Scannere PrintStreamfacilitambastanteopro-
cessodeentradaesaídadedados. Querlermaissobreessasduasclasses?
Nãodeixedeconferirsuadocumentaç ão:
• http://docs.oracle.com/javase/8/docs/api/java/io/PrintStream.html
• http://docs.oracle.com/javase/8/docs/api/java/util/Scanner.html
3.7 G erando um CSV de produtos
AgoraquejáconhecemosumpoucodaAPIde io,vamosadicionarumnovo
comportamentoemnossalistagemdeprodutos.Queremosexportarospro-
dutosdalistagemparaumarquivo CSV.OtermoCSVvemde commasep-
aratedvalue,ouseja,valoresseparadosporvírgula.Esseformatoébastante
comumeutilizadonodiaadia.
Queremosaofinalterumarquivoparecidocom:
Nome, Descricao, Valor, ISBN
Java 8 Prático, Novos recursos da linguagem, 59.9,
978-85-66250-46-6
Vamoscomeçarcriandoaclasse Exportador,queseráresponsávelpor
essetrabalho.Elateráumúnicométodo,chamado paraCSV,quereceberá
um Listde Produtocomoparâmetro:
public class Exportador {
public void paraCSV(List<Produto> produtos) {
}
}
Implementandoessemétodo,nossoprimeiropassoserácriarumarquivo
produtos.csvejácolocarumcabe çalhocomasinformaçõesquevamos
escrever.Podemosusarum PrintStreamparafazerotrabalho,repare:
public void paraCSV(List<Produto> produtos)
throws IOException {
43

## Página 54

3.7. GerandoumCSVdeprodutos CasadoCódigo
PrintStream ps = new PrintStream("produtos.csv");
ps.println("Nome, Descricao, Valor, ISBN");
ps.close();
}
Jáexecuteocódigoparaveroresultado.Oarquivodevesercriadonaraiz
doseuprojetoeporenquantoapenascomoconteúdo:
Nome, Descricao, Valor, ISBN
Excelente.Agoratudooqueprecisamosfazeréiterarnessalistadepro-
dutosadicionandoumalinhaparacadaelemento,comoporexemplo:
public void paraCSV(List<Produto> produtos )
throws IOException {
PrintStream ps = new PrintStream("produtos.csv");
ps.println("Nome, Descricao, Valor, ISBN");
for (Produto produto : produtos) {
ps.println(produto.getNome() + ", "
+ produto.getDescricao() + ", "
+ produto.getValor() + ", "
+ produto.getIsbn());
}
ps.close();
}
Issojátraráoresultadoqueesperamos.Masocódigoestébemfeio,não
acha?Essaconcatenaçãode Stringspodeprejudicarbastantealegibilidade
edificultaramanuten çãodenossocódigo.
44

## Página 55

CasadoCódigo Capítulo3. JavaIO
Usando o projeto do outro livro?
Se,nolugardebaixaroprojetobase,vocêestiverutilizandooprojeto
dolivro DesbravandoJavaeOrienta çãoaObjetos,vocêprecisarámodi-
ficarsuainterface Produtoparaqueessecódigocompile.
Eladeveficarassim:
public interface Produto
extends Comparable<Produto> {
double getValor();
String getNome();
String getDescricao();
String getIsbn();
}
Umaopçãotalvezmaisinteressanteseriausaro String.format,como
aseguir:
public void paraCSV(List<Produto> produtos)
throws IOException {
PrintStream ps = new PrintStream("produtos.csv");
ps.println("Nome, Descricao, Valor, ISBN");
for (Produto produto : produtos) {
ps.println( String.format("%s, %s, %s, %s",
produto.getNome(),
produto.getDescricao(),
produto.getValor(),
produto.getIsbn()));
}
ps.close();
}
Ufa! Um pouco melhor. Claro, poderíamos ter usado um
45

## Página 56

3.7. GerandoumCSVdeprodutos CasadoCódigo
StringBuilder, StringJoiner etc., mas essa opção é bem sim-
plesejáresolveoproblema. Vamosverseestáfuncionando? Crieum
método maindentrodessamesmaclasseparatestar,elepodeficarassim:
public static void main(String[] args)
throws IOException {
Livro livro = new LivroFisico(new Autor());
livro.setNome("Java 8 Prático");
livro.setDescricao("Novos recursos da linguagem");
livro.setValor(59.90);
livro.setIsbn("978-85-66250-46-6");
Livro maisUmlivro = new LivroFisico(new Autor());
maisUmlivro.setNome("Desbravando a O.O.");
maisUmlivro.setDescricao("Livro de Java e O.O");
maisUmlivro.setValor(59.90);
maisUmlivro.setIsbn("321-54-67890-11-2");
new Exportador ().paraCSV(Arrays.asList(livro, maisUmlivro ));
}
Oresultadoseráoarquivo produtos.csv,comoseguinteconteúdo:
Nome, Descricao, Valor, ISBN
Java 8 Prático, Novos recursos da linguagem, 59.9,
978-85-66250-46-6
Desbravando a OO, Livro de Java e O.O, 59.9, 321-54-67890-11-2
Nãoencontrouoarquivo? Lembre-sededarum F5(refresh)emseu
projetoparaeleaparecernaIDE.Ou,sepreferir,abraapastadoseuprojeto
diretopeloseusistemaoperacional.
46

## Página 57

CasadoCódigo Capítulo3. JavaIO
Fig.3.10:Arquivoprodutos.csvvistopelosistemaoperacional
Nossaclasse Exportadorficouassim:
import java.io.IOException;
import java.io.PrintStream;
import java.util.List;
import br.com.casadocodigo.livraria.produtos.Produto;
public class Exportador {
public void paraCSV(List<Produto> produtos)
throws IOException {
PrintStream ps = new PrintStream("produtos.csv");
ps.println( "Nome, Descricao, Valor, ISBN");
for (Produto produto : produtos) {
ps.println(String.format("%s, %s, %s, %s",
produto.getNome(),
produto.getDescricao(),
produto.getValor(),
produto.getIsbn()));
}
ps.close();
}
47

## Página 58

3.8. Botãodeexportarprodutos CasadoCódigo
}
3.8 B otão de exportar produtos
Agoraquejátemosocódigoparaexportarumalistadeprodutoscomoum
CSV,podemosadicionarumbotãoemnossalistagemfeitaemJavaFXpara
dispararessalógica.Issoébemsimples.
O primeiro passo é criar um Button, do pacote
javafx.scene.control. Opcionalmente, em seu construtor você já
podepassarotextoquequerexibir.Podemosfazer:
Button button = new Button("Exportar CSV");
Damesmaformaquefizemoscoma labele tableView,precisamos
adicionaressebotãonocenáriodapágina. Bastaadicioná-locomoargu-
mentodométodo addAll:
group.getChildren().addAll(label, vbox, button);
Executeocódigoevocêperceberáqueelejáestánapágina,masestáde-
salinhado,cobrindootextodanossa lable:
Fig.3.11:Buttondesalinhadonatela
Bem,paraalinhá-lopodemosenvolveresse buttonemum VBoxcom
umpaddingdefinido,assimcomofizemoscomatabela. Outraop çãomais
simpleséutilizarseusmétodos setLayoutXe setLayoutYparadefinir
suaposição,algocomo:
48

## Página 59

CasadoCódigo Capítulo3. JavaIO
Button button = new Button("Exportar CSV");
button.setLayoutX(575);
button.setLayoutY(25);
Agorasim,oresultadoserá:
Fig.3.12:ButtonalinhadocomsetLayoutXesetLayoutY
Masnotequeaoclicarnobotãonenhumaaç ãoseráexecutada.Fazsen-
tido,aindanãoimplementamosisso.
3.9 A dicionando ações com setO nA ction
Ométodo setOnActionéoresponsávelpordefinirasaçõesqueserãoex-
ecutadasnomomentodo clickdenosso Button.Podemosfazer:
button.setOnAction(???); // oq?
Essemétodoesperareceberumainstânciadotipo EventHandler(in-
terface)comoparâmetro.Sim,poderíamoscriarumaclassequeimplemen-
tasseessainterfaceepassá-lacomoparâmetro,mascomumentefazemosisso
comuma classeanônima:
button.setOnAction(new EventHandler<ActionEvent>() {
@Override
public void handle(ActionEvent event) {
// ação a ser executada
}
});
49

## Página 60

3.9. AdicionandoaçõescomsetOnAction CasadoCódigo
Classe anônima
Sevocênãoestáacostumadooununcaviuclassesanônimas,nãosepre-
ocupe.Apesardeumtantofeias,elassãobemsimplesdeentender.Nolugar
deusarumaclasseanônima,poderíamostercriadoumaclassequeimple-
mentasse EventHandler<ActionEvent>:
public class AcaoDoBotao
implements EventHandler<ActionEvent> {
@Override
public void handle(ActionEvent event) {
// ação a ser executada
}
}
Poderíamosusá-laassim:
button.setOnAction(new AcaoDoBotao());
Oproblemadessecódigoéquecadabotãopodeterumaaç ãoquenãovai
serepetiremnenhumoutromomentodocódigo,sóseráusadaaqui.Além
disso,podemosterváriosbotões;teríamosquecriarumaclassenovapara
fazeraaçãodecadaumdeles?
Aquiqueentraaclasseanônima!Nolugardecriarumaclasse,digamos
queconvencional,podemosinstanciardiretamenteainterfaceejáinstanciar
seusmétodosalimesmo.Essainstânciacriadaéfrutodeumaclasseanônima,
umaclassequenemtemumnome.
Agora,voltandoaobotão.Queremosportantoadicionaraaç ãodo click
dentrodométodo handle,queestamosimplementandonaclasseanônima.
Vamoscomeçarcomumexemplosimples,apenasmostrandoumamensagem
noconsole:
button.setOnAction(new EventHandler<ActionEvent>() {
@Override
public void handle(ActionEvent event) {
System.out.println("Click!");
}
});
50

## Página 61

CasadoCódigo Capítulo3. JavaIO
Paratestar,executeaaplicaçãoepressioneobotão Exportar CSV al-
gumasvezes,vocêveráqueacada clickotextoseráimpresso.
Oquequeremosnaverdadeéexportartodososnossosprodutoscomo
um CSV,portanto,fazemos:
button.setOnAction(new EventHandler<ActionEvent>() {
@Override
public void handle(ActionEvent event) {
new Exportador ().paraCSV(produtos);
}
});
Mas,espera!Essecódigoaindanãocompila.Comoométodo paraCSV
lançauma IOException,precisamostratá-laoudeclará-la.Vamostratar:
button.setOnAction(new EventHandler<ActionEvent>() {
@Override
public void handle(ActionEvent event) {
try {
new Exportador ().paraCSV(produtos );
} catch (IOException e) {
System.out.println("Erro ao exportar: "+ e);
}
}
});
Pronto!Coloqueessecódigoemaç ão,bastaclicarnobotão Exportar
CSVqueoarquivo produtos.csvserácriadonaraizdeseuprojeto.
Fig.3.13:Projetocomarquivoprodutos.csvcriado
51

## Página 62

3.10. JavaFxeJava8 CasadoCódigo
3.10 J av aFx eJav a8
QuetaldarumtoquedeJava8nessecódigo?Osnovosrecursosdessaver-
sãodeixamocódigodoJavaFXbemmaisenxutoeinteressante. Querum
exemplo?Dêumaboaolhadanovamentenaclasseanônimaquecriamosno
setOnActiondobotãodeexportar:
button.setOnAction(new EventHandler <ActionEvent>() {
@Override
public void handle(ActionEvent event) {
try {
new Exportador ().paraCSV(produtos);
} catch (IOException e) {
System.out.println("Erro ao exportar: "+ e);
}
}
});
Quetalescrevê-locomoaseguir,utilizandouma expressãolambda?
button.setOnAction(event -> {
try {
new Exportador().paraCSV(produtos );
} catch (IOException e) {
System.out.println("Erro ao exportar: "+ e);
}
});
Cortamosocódigoquasepelametade!Masnemsempremenoslinhasde
códigosignificamelhora,temosqueconsiderarqueissopodediminuirum
poucoalegibilidade. Paradeixaressecódigoumpoucomaislimpo,vamos
extrairummétodo.Podemoschamá-lode exportaEmCSV:
private void exportaEmCSV(ObservableList<Produto> produtos) {
try {
new Exportador().paraCSV(produtos );
} catch (IOException e) {
System.out.println("Erro ao exportar: "+ e);
}
}
52

## Página 63

CasadoCódigo Capítulo3. JavaIO
Aexpressãolambdaficaráassim:
button.setOnAction(event -> exportaEmCSV(produtos));
Temosagoraumalinhadecódigo!Eelaébastantedeclarativa>temosum
eventocomoparâmetroequeremoschamarométodo exportaEmCSV,
passandoalistadeprodutos.Muitomaisenxutoelegível,nãoacha?
Claro,oJava8vaimuitoalémdisso.Hádiversasoutrasnovidades.Está
curiosoparaconheceralgumasdelas?Entãocomcertezavocêvaigostardo
livroqueescrevijuntocomoPauloSilveira,o Java8PráticoLambdas,Streams
eosnovosrecursosdalinguagem.
http://www.casadocodigo.com.br/products/livro-java8
ApesardeestarmosusandoalgumascoisasdoJava8nosexemplosdesse
livro,essenãoénossofoco.VocêquenãotemoJava8instaladopodemanter
asintaxedasclassesanônimas.Eusempreprocuromostrardasduasformas
paraquevocêconsigaacompanharindependentedasuaversãodoJava.Ok?
Nesseponto,ocódigofinaldaclasse Mainestáassim:
@SuppressWarnings({ "unchecked", "rawtypes" })
public class Main extends Application {
@Override
public void start(Stage primaryStage) {
Group group = new Group();
Scene scene = new Scene(group, 690, 510);
ObservableList<Produto> produtos =
new RepositorioDeProdutos().lista();
TableView<Produto> tableView = new TableView<>(produtos);
TableColumn nomeColumn = new TableColumn("Nome");
nomeColumn.setMinWidth(180);
nomeColumn.setCellValueFactory(
new PropertyValueFactory("nome"));
TableColumn descColumn = new TableColumn("Descrição");
53

## Página 64

3.10. JavaFxeJava8 CasadoCódigo
descColumn.setMinWidth(230);
descColumn.setCellValueFactory(
new PropertyValueFactory("descricao"));
TableColumn valorColumn = new TableColumn("Valor");
valorColumn.setMinWidth(60);
valorColumn.setCellValueFactory(
new PropertyValueFactory("valor"));
TableColumn isbnColumn = new TableColumn("ISBN");
isbnColumn.setMinWidth(180);
isbnColumn.setCellValueFactory(
new PropertyValueFactory("isbn"));
tableView .getColumns().addAll(nomeColumn, descColumn,
valorColumn , isbnColumn);
final VBox vbox = new VBox( tableView);
vbox.setPadding(new Insets(70, 0, 0 ,10));
Label label = new Label( "Listagem de Livros");
label.setFont(Font
.font("Lucida Grande", FontPosture.REGULAR, 30));
label.setPadding(new Insets(20, 0, 10, 10));
Button button = new Button("Exportar CSV");
button.setLayoutX(575);
button.setLayoutY(25);
button.setOnAction(event -> exportaEmCSV(produtos));
group.getChildren().addAll(label, vbox, button);
primaryStage.setTitle("Sistema da livraria com Java FX");
primaryStage.setScene(scene);
primaryStage.show();
}
54

## Página 65

CasadoCódigo Capítulo3. JavaIO
private void exportaEmCSV(ObservableList<Produto> produtos) {
try {
new Exportador ().paraCSV(produtos );
} catch (IOException e) {
System.out.println("Erro ao exportar: "+ e);
}
}
public static void main(String[] args) {
launch(args );
}
}
A única diferença para você, que está usando Java 7, será no
setOnActiondo button.Agoraqueextraímosométodo,eleficaráassim
comclasseanônima:
button.setOnAction(new EventHandler<ActionEvent>() {
@Override
public void handle(ActionEvent event) {
exportaEmCSV(produtos);
}
});
55

## Página 67

Capítulo4
BancodeDadoseJDBC
Aaplicaçãoestáficandomaiscompleta,masaindaestamostrabalhandocom
valoresfixosnalistagemdeprodutosquecriamosmanualmentenaclasse
RepositorioDeProdutos. Nossoobjetivoagoraserábuscaressasinfor-
maçõesdeumbancodedados,comoénaturalnasaplicaçõesdodiaadia.
4.1 I niciando com MySQL
UsaremosobancodedadosMySQLnoprojetodenossalivraria,jáqueé
umdosbancosdedadosrelacionaismaisutilizadosnomercado,égratuitoe
bastantesimplesdeinstalar.
SevocêaindanãotemoMySQLinstalado,podefazerdownloadpelolink:
http://dev.mysql.com/downloads/mysql/

## Página 68

4.1. IniciandocomMySQL CasadoCódigo
Aofinaldapágina,vocêencontraráumcampoparaescolherseusistema
operacional.Selecioneedepoiscliqueemdownload,naop çãoquepreferir:
Nomesmosite,vocêencontraumtutorialdeinstalaçãodeacordocomo
58

## Página 69

CasadoCódigo Capítulo4. BancodeDadoseJDBC
seusistemaoperacional.Ouvocêpodeacessarotutorialdiretamenteem:
http://dev.mysql.com/doc/refman/5.7/en/installing.html
ApósbaixareinstalaroMySQL,vamosnoslogarnoMySQLecriarabase
dedados(database)denossoprojeto.Oprimeiropassoébemsimples,tudo
quevocêprecisafazerparaselogaréabrirseuterminaledigitar:
mysql -u SEU_USUARIO -p SUA_SENHA
Comoemmeucasoousuárioé rooteeunãotenhoumasenha,só
precisofazer:
mysql -u root
Fig.4.3:TelainicialdoMySQLCommandLine
MySQL Command Line ou Workbench?
Háquemprefirautilizaro MySQLWorkbench,queéumaferramenta
visual.Pelasimplicidade,nosexemplosdolivrovamosutilizaro MySQL
CommandLine. Nele,nósexecutamosasinstruçõesdiretamentepela
linhadecomando,noterminal.
Setiverqualquerdificuldadeparainstalarouexecutaroscomandos,
nãopenseduasvezesantesdemandarume-mailparalistadesselivro.
59

## Página 70

4.2. Criandoatabeladeprodutos CasadoCódigo
Agora que já estamos logados, podemos criar uma novadatabase
chamada livraria.Issopodeserfeitocomocomando:
create database livraria;
Apósexecutá-lo,asaídadeveserparecidacom:
Query OK, 1 row affected (0.00 sec)
Perfeito,vamosusaragoraocomando use livraria paraacessaressa
basededadosquecriamos.
use livraria;
Amensagem Database changed deveserexibida.
4.2 C riando a tabela de produtos
Podemosagoracriarumatabelaondeserão persistidasasinformaçõesde
nossosprodutos.Faremosissocomocomando create table aseguir:
CREATE TABLE produtos (
id BIGINT NOT NULL AUTO_INCREMENT,
nome VARCHAR(255),
descricao VARCHAR(255),
valor VARCHAR( 255),
isbn VARCHAR(255),
PRIMARY KEY (id)
);
SevocênãoestáacostumadocomSQL,nãosepreocupe.Nossofocoaqui
seráaintegraçãodocódigoJavacomumbancodedados,enãooSQLemsi.
Empoucaspalavras,ocomandocriouumatabeladeprodutoscomascolunas
id, nome, descricaoe isbn,queéoqueprecisamosporagora. Note
tambémquedissemosqueo iddoprodutonãopodesernuloedeveser
autoincrementado,assimoprópriobancodedadoscuidarádeincrementaro
valordo idacadanovoregistro.
60

## Página 71

CasadoCódigo Capítulo4. BancodeDadoseJDBC
4.3 O pacote jav a.sql e oJDBC
AbibliotecapadrãodoJavaparapersistênciaembancodedadosécon-
hecidacomoJDBC,deJavaDataBaseConnective.O JDBCé,naverdade,um
conjuntodeinterfacesbemelaboradoquedeveserimplementadodeforma
diferenteparacadabancodedados.Dessaforma,evitamosquecadabanco
tenhaseupróprioconjuntodeclassesemétodos. Qualavantagemdisso?
Manutenibilidadeéumadasmuitas. Migrardeumbancoparaoutroéum
processofácil,jáquetodosimplementamasmesmasinterfaces,portantopos-
suemmétodoscomamesmaassinatura.
Esseconjuntodeclasseséconhecidocomo driver;elasfazemaponte
entreaAPIde JDBCeobancodedados.Onomeéanálogoaosdriversuti-
lizadosnainstalaçãodeimpressoras.Damesmaformaqueosdriverspossi-
bilitamacomunicaçãoentreumadeterminadaimpressoracomosdiferentes
sistemasoperacionaisexistentes,osdriversqueimplementamasinterfacesdo
JDBCpossibilitamacomunicaçãoentrenossocódigoJavacomosdiferentes
bancosdedadosexistentes.
61

## Página 72

4.3. Opacotejava.sqleoJDBC CasadoCódigo
Fig.4.4:ComunicaçãoentrecódigoJavaeBancodeDados
Boa prática: pacote jav a.sql
Nomomentodefazeros importsdasclasses,tomeocuidadodesem-
preescolheropacote java.sql. Nuncaescolhaop çõesdeclasses
equivalentesdopacote com.mysql,ouqualqueroutrobancodedados
quevocêestiverutilizando.Dessaforma,vocênãoseacoplacomaAPI
dobancodedadosqueestáutilizando.
62

## Página 73

CasadoCódigo Capítulo4. BancodeDadoseJDBC
4.4 A brindo conexão com MySQL em Jav a
Aclasse DriverManageréaresponsávelporgerenciaroprocessodecomu-
nicaçãocomosdriversdosbancosdedados.Paraabrirumaconexão,tudo
queprecisamosfazeréinvocarseumétodo getConnectionpassandocomo
parâmetroumaStringdeconexãodoJDBC,seuloginesenha.Essa String
deconexão,paraoMySQL,temaseguinteestrutura:
jdbc:mysql://IP/DATABASE
O IPdevesersubstituídopeloIPdoservidorondeseencontraobanco
dedados. Emnossocaso,comoseránamesmamáquina,podemosdeixar
como localhost.A DATABASEdevesersubstituídapelonomedabasede
dadosquecriamosparaoprojeto,a livraria.Portanto:
jdbc:mysql://localhost/livraria
Parautilizaro DriverManager, precisaremosadicionarodriverdo
MySQLemnossoprojeto. Essearquivotambémestádisponívelno zip
quevocêbaixoucomosarquivosnecessáriosparaestelivro.Bastacopiaro
arquivo mysql-connector-java-5.1.34-bin.jarparadentrodoseu
projetonoEclipse.Comobotãodireitodomouse,cliquenodriveredepois
em Build Path e Add to Build Path.
Fig.4.5:AdicionandodriverdoMySQLnoBuildPath.
Sevocêaindanãoestáfamiliarizadocomotermo JAR,nãosepreocupe.
Temosumcapítuloquedetalhabemessetipodearquivoeseuuso.
Agoraquetemosodriver,vamoscriarumanovaclasse,quechamaremos
de ConnectionFactoryparacolocarissotudoemprática.Seucódigode-
veráseparecercom:
63

## Página 74

4.4. AbrindoconexãocomMySQLemJava CasadoCódigo
public class ConnectionFactory {
public Connection getConnection() {
String url = "jdbc:mysql://localhost/livraria";
return DriverManager.getConnection(url, "root", "");
}
}
Design Patterns e o Factory Method
Nãofoiporacasoquechamamosaclasse ConnectionFactory
dessaforma.Essaéumapráticadeprojetomuitocomumebastantere-
comendada.Muitasvezesqueremoscontrolaroprocessodecriaç ãode
umobjetoquepodeserrepetidodiversasvezesemnossocódigo,como
odeabrirumaconexão. Oqueaconteceriaseessecódigoestivessees-
palhadopornossaaplicaçãoealgumainformaçãomudasse?Umatroca
delogin,porexemplo,fariavocêmudardiversaspartesdoseucódigo.
Noteque,agoraquetemosaclasse ConnectionFactory,nãoes-
tamosdeixandoasinformaçõesdobancodedadossereplicaremem
todanossaaplicação.Ométodo getConnectionnãorecebenenhum
parâmetroeretornaumaconexãoprontaparaserutilizada.Algumain-
formaçãomudou?Nãotemproblema,sóprecisomudarumúnicoponto
domeucódigo(aimplementaç ãodométodo getConnection),que
issoseráreplicadopratodosqueousam.Interessante,nãoacha?
Essaboapráticadeprojetoéconhecidacomo factory method e
compõeumdosdiversos DesignPatternsexistentes.
Masessecódigoaindanãocompila,ométodo getConnectionlança
uma SQLException.Precisamostrataroudeclararessaexce çãodealguma
forma.umamaneirabastanterecomendadadetratarseria:
public class ConnectionFactory {
public Connection getConnection() {
String url = "jdbc:mysql://localhost/livraria";
64

## Página 75

CasadoCódigo Capítulo4. BancodeDadoseJDBC
try {
return DriverManager.getConnection(url, "root", "");
} catch (SQLException e) {
throw new RuntimeException(e);
}
}
}
Qualavantagememfazerisso? Afinalsóestamos“embrulhando”ere-
lançandoa SQLExceptioncomouma RuntimeException. Agrande
ideiadessapráticaéqueassimnãodeixamosessa exceptiondaAPIdeJDBC
seespalharpelonossocódigo,diminuindo acoplamentocomessaAPI.
Já podemos testar nosso código para garantir que a conexão com o
bancodedadosestáacontecendosemnenhumproblema. Podemoscriar
ummétodo main,naprópriaclasse ConnectionFactory,comoseguinte
código:
public static void main(String[] args) {
Connection conn = new ConnectionFactory().getConnection();
System.out.println("Conexao aberta, e agora?");
conn.close();
}
Executeparaversetudoestáok.Algunsdoserroscomunssão:
• Erraradigitaçãoda Stringdeconexões,comoporexemploesquecer
deumabarraoualgodessetipo. Nestecaso,uma exceptionparecida
comaseguintedeveacontecer:
Caused by: java.sql.SQLException: No suitable
driver found for jdbc:mysql:/localhost/livraria
• Referenciarumadatabasequenãoexiste.Porexemplo,seeunãocriar
adatabase livrarianoMySQL,oseguinteerrovaiacontecer:
Caused by: com.mysql.jdbc.exceptions.jdbc4
.MySQLSyntaxErrorException: Unknown database 'livraria'
65

## Página 76

4.5. Listandotodososprodutosdobanco CasadoCódigo
Setudocorreubem,amensagem Conexaoaberta,eagora? deveserex-
ibida. Podemosdarmaisumpasso,adicionarelistarelementoscomaAPI
doJDBC.
4.5 L istando todos os produtos do banco
Vamoscomeçarpelonossoobjetivo,queélistartodososprodutosdobanco
dedados. Parafazerisso,limpeoconteúdodométodo listadaclasse
RepositorioDeProdutos,deixeapenas:
public class RepositorioDeProdutos {
public ObservableList<Produto> lista() {
return FXCollections.observableArrayList();
}
}
OprimeiropassoseráescreveraSQLquequeremosexecutarnobanco,
queseráalgocomo:
String sql = "select * from produtos";
Acláusula selectcom *estáindicandoquequeremostodasascolu-
nasdetodososprodutos.Paraexecutaresta,ouqualqueroutra query,pre-
cisaremosantesabrirumaconexãocomobancoepraissopodemosutilizar
a ConnectionFactoryquecriamos.Ocódigoficaassim:
Connection conn = new ConnectionFactory().getConnection();
String sql = "select * from produtos";
Comoenviareexecutaressa queryemumbancodedados?Ébemsim-
ples,háumainterfacechamada PreparedStatementparanosajudarneste
trabalho. Bastachamarométodo prepareStatementda Connection
quecriamos,passandoaSQLcomoargumento:
Connection conn = new ConnectionFactory().getConnection();
String sql = "select * from produtos";
PreparedStatement ps = conn.prepareStatement(sql);
ps.executeQuery();
66

## Página 77

CasadoCódigo Capítulo4. BancodeDadoseJDBC
Esse código lança uma SQLException, vamos relançar essa
exceção como uma Runtime, da mesma forma que fizemos na
ConnectionFactory para diminuir o acoplamento com a API de
JDBC.Ocódigoficaráassim:
Connection conn = new ConnectionFactory().getConnection();
PreparedStatement ps;
try {
ps = conn.prepareStatement("select * from produtos");
ps.executeQuery();
} catch (SQLException e) {
throw new RuntimeException(e);
}
O métodoexecuteQueryfará seu trabalho e retornará um objeto
comtodososregistrosdoresultadodaconsulta. Esseobjetotemotipo
ResultSet. Cadachamadaaoseumétodo nextretornará trueen-
quantohouverpróximosregistros,portanto,énaturaliterarnessaestrutura
utilizandoum while,comofaremosaseguir:
while(resultSet.next()) {
// como pegar o nome, valor, etc?
}
Seusmétodos getsãoosresponsáveisporrecuperarovalordeuma
determinadacolunadatabela. Seforumacolunadetexto, utilizamoso
getString, getIntparauminteiroeassimpordiante. Emnossocaso,
precisaremosapenasdosmétodos getStringparanome,descricao,isbne
do getDoubleparao valordoproduto.Ocódigodeveficarassim:
while(resultSet.next()) {
String nome = resultSet.getString("nome");
String descricao = resultSet.getString("descricao");
double valor = resultSet.getDouble("valor");
String isbn = resultSet.getString("isbn");
}
Paraconcluir,nossométodoprecisaretornara ObservableListde
ProdutosqueseráconsumidapelanossalistagememJavaFX.Porenquanto,
vamosrepresentarosprodutosapenascomo LivroFisico:
67

## Página 78

4.5. Listandotodososprodutosdobanco CasadoCódigo
while(resultSet.next()) {
LivroFisico livro = new LivroFisico(new Autor());
livro.setNome(resultSet.getString("nome"));
livro.setDescricao(resultSet.getString("descricao" ));
livro.setValor(resultSet.getDouble("valor"));
livro.setIsbn(resultSet.getString("isbn"));
produtos.add(livro);
}
Aofinal,nossaclasse RepositorioDeProdutosdeveficarassim:
public class RepositorioDeProdutos {
public ObservableList<Produto> lista() {
ObservableList<Produto> produtos = observableArrayList();
Connection conn = new ConnectionFactory().getConnection();
PreparedStatement ps;
try {
ps = conn.prepareStatement("select * from produtos");
ResultSet resultSet = ps.executeQuery();
while(resultSet.next()) {
LivroFisico livro = new LivroFisico(new Autor());
livro.setNome(resultSet.getString("nome"));
livro.setDescricao(resultSet.getString("descricao" ));
livro.setValor(resultSet.getDouble("valor"));
livro.setIsbn(resultSet.getString("isbn"));
produtos.add(livro);
}
resultSet.close();
ps.close();
conn.close();
} catch (SQLException e) {
throw new RuntimeException(e);
}
return produtos;
}
}
68

## Página 79

CasadoCódigo Capítulo4. BancodeDadoseJDBC
Mas,espera!Aoexecutaraclasse Mainagora,nossalistagemdeprodutos
estávazia!Fazsentido,nãoé?Afinal,nãoadicionamosnenhumprodutoao
bancodedados,atabela produtosestávazia. Esseseránossopróximo
passo.
Inserindo manualmente no MySQL
Sevocêquiser,podeinserirumlivromanualmentenatabeladepro-
dutosparaconfirmardesdejáqueseucódigoestáfuncionandocomo
deveria.Vocêpodefazerissoexecutandoosseguintescomandosemseu
terminal:
$ mysql -u root livraria
$ insert into produtos (nome, descricao, valor, isbn)
values ('Java 8 Prático', 'Novos recursos da linguagem',
'59.90', '978-85-66250-46-6');
4.6 I mportando produtos de um dump
Para não precisar cadastrar manualmente, vamos importar o arquivo
dump.sqlcomalgunslivrosjácadastradosparanossatabeladeprodutos.
Umarquivode dumbéumarquivodetextocominstruçõesSQL,comos in-
sertsdedadosouatémesmocomasinstruçõesdecriaçãodetabelas.
Criando seu próprio dump
Sequisersabermaissobreessearquivode dump,oumesmocriaro
seupróprio,vocêpodedarumaolhadanolink:
http://dev.mysql.com/doc/refman/5.0/en/mysqldump-sql-format.
html
Issopodeserbemútilquandoqueremosfazer backupsdesegurança
denossasbasesdedados.
69

## Página 80

4.6. Importandoprodutosdeumdump CasadoCódigo
Essearquivotambémestápresentenaquele zipcomoconteúdoinicial
doprojeto,em arquivos-do-livro/dump.sql. Tudoqueprecisamos
fazerparaimportaresse dumpemnossobancodedadoséexecutaraseguinte
instruçãonoterminal:
mysql -uroot < CAMINHO_COMPLETO_PARA_O_DUMP
Parafacilitaroprocesso,vocêpodecopiaroarquivo dump.sqlparaa
pastaraizdeseuusuário,eexecutarapenas:
mysql -uroot < dump.sql
Ótimo!Depoisqueconcluir,tenteacessarnovamentealistagemdepro-
dutos.Setudocorreubem,diversoslivrosdevemserlistados.
70

## Página 81

CasadoCódigo Capítulo4. BancodeDadoseJDBC
Frameworks ORM
ExistemdiversasferramentasquefacilitamemuitoousodoJDBC,
quesãoconhecidascomoferramentas ORM,de ObjectRelationalMap-
ping.Aideiaéquevocêtrabalhepensandoexclusivamenteemorientação
aobjetos,enquantoessasbibliotecas(ou frameworks,comosãocomu-
mentechamadas)oajudamatraduzirissoparaomundorelacionaldos
bancosdedados.O Hibernateéumdosframeworksde ORMmaiscon-
hecidoseutilizadosdomercado.Aconselhobastantequevocêpesquise
arespeitodesseseoutrosapósconheceraAPIdeJDBCdoJava.
Sequisersabermaissobreohibernatevocêpodequererdarumaol-
hadanosite:
http://hibernate.org/orm/
4.7 P ara saber mais: A dicionando programati-
camente
ParaconhecerumpouquinhomaissobreaAPIdoJDBC,vamoscriarmais
ummétodonaclasse RepositorioDeProdutos,queexemplificarácomo
éfeitoum INSERTnobancodedadosprogramaticamente.Vamoschamá-lo
de adiciona,afinalesseseráseupropósito.
public class RepositorioDeProdutos {
public ObservableList<Produto> lista() {
// código omitido
}
public void adiciona(Produto produto) {
// código de adicionar com JDBC
}
}
Notequeessemétodojáestárecebendoo Produtoquedeveráseradi-
cionadonobanco.
71

## Página 82

4.7. Parasabermais:Adicionandoprogramaticamente CasadoCódigo
Damesmaformacomofizemoscomométodo lista,utilizaremosa
interface PreparedStatementparaexecutarasinstruçõesSQLnobanco
dedados.
public void adiciona(Produto produto) {
Connection conn = new ConnectionFactory().getConnection();
PreparedStatement ps = conn.prepareStatement("???");
// código de executar o PreparedStatement
ps.close();
conn.close();
}
Vale lembrar que esse código não compilará se não tratarmos a
SQLExceptionqueométodo prepareStatementlança.
public void adiciona(Produto produto) {
Connection conn = new ConnectionFactory().getConnection();
PreparedStatement ps;
try {
ps = conn.prepareStatement("???");
// código de executar o PreparedStatement
ps.close();
conn.close();
} catch (SQLException e) {
throw new RuntimeException(e);
}
}
Porenquanto,ocódigoestámuitoparecidocomodelistagem,masa
grandediferençacomeçaaqui. Umaformadeescreveracláusula INSERT
queseráexecutadanobancodedadosseria:
ps = conn.prepareStatement("insert into produtos (nome,
descricao, valor, isbn) values ('Livro de PHP',
'Um livro sobre PHP', '59.90', '123-45-67890-12-3')");
72

## Página 83

CasadoCódigo Capítulo4. BancodeDadoseJDBC
Mas,claro,nãopodemosdeixaressesvaloresfixosemnossocódigo.Uma
alternativaéconcatenarosatributosdo Produto,comofaremosaseguir:
ps = conn.prepareStatement("insert into produtos (nome, "
+ "descricao, valor, isbn) values ('"+produto.getNome()+"', "
+ "'"+produto .getDescricao()+"', '"+produto.getValor()+"', "
+ "'"+produto .getIsbn()+")");
Quetal? Nemumpoucolegível,nãoacha? Imaginesenolugarde4
camposexistissemcercade20,comoqueessecódigosepareceria?
Aprovadequeémuitodifícilmanterumcódigocomoesseéqueaofinal
da Stringeudeixeideforauma ‘(aspassimples).Vocêidentificouissoao
olharprocódigo?Semdúvidapoderiapassardespercebido.
Masessenãoéoúnicoproblemadessecódigocheiodeconcatenações,há
aindaoclássicoproblemadenomesquecontêmaspassimples(como Joana
D’arc).Oqueaconteceriaaotentarconcatenaressa StringnaSQLanterior?
AinstruçãoSQLvaiquebrartoda!Piorainda,fazerconcatenaç ãodessaforma
possibilitaaousuáriofinalmodificarseuSQLparaexecutaroqueelebem
entender,oclássicoproblemade SQL Injection.
73

## Página 84

4.7. Parasabermais:Adicionandoprogramaticamente CasadoCódigo
Para saber mais: SQL I njection
Paraentendermelhoroqueéumainje çãodeSQL,vamosconsiderar
aseguinteinstruçãoquefazum SELECTverificandoseousuárioexiste.
Elacomumenteseriaexecutadaporumformuláriodelogin.
ps = conn.prepareStatement("select * from usuarios where "
+ "login = '"+login+ "' and senha ='"+senha+"'");
Oqueaconteceseovalordavariável loginforumtextovazioeo
valordavariável senhafor ’ or 1=1? Vamossubstituira String
comessesvaloresparaverificar.Oresultadoserá:
select * from usuarios where login ='' and senha ='' or 1=1
Essecomandotrarátodososusuáriosdenossobancodedados!Ou
seja,ousuáriofinaldaaplicaçãopodeenviarqualquerinformação,que
podesermaliciosa, eresultaremumretornoinesperadocomoesse.
NuncadevemosconcatenarvariáveisemcomandosSQLdessaforma.
Bem,jávimosqueessaéumapéssimaprática. Nolugardeconcatenar
dessaforma,ainterface PreparedStatementnosofereceumasériede
métodos setparapopularmososvaloresvariáveisdainstruçãoSQL.Nosso
comandoSQLficarácomoaseguir,deixandopontosdeinterrogaçãonolugar
dessesvalores:
ps = conn.prepareStatement("insert into produtos (nome,"
+ " descricao, valor, isbn) values (?,?,?,?)");
Parapopularasvariáveis,podemosutilizarosmétodos setStringpara
osvaloresdetextoe setDoubleparaocampo valor, queédotipo
double,semprepassandoaposição(quecuriosamentecome çaem1,enão
0),seguidadovalorquedeveserpreenchido:
ps = conn.prepareStatement("insert into produtos (nome,"
+ " descricao, valor, isbn) values (?,?,?,?)");
74

## Página 85

CasadoCódigo Capítulo4. BancodeDadoseJDBC
ps.setString(1, produto.getNome());
ps.setString(2, produto.getDescricao());
ps.setDouble(3, produto.getValor());
ps.setString(4, produto.getIsbn());
4.8 Q ual a melhor forma de fechar a conexão?
Umpontofundamentalqueprecisasercuidadosamenteverificadosempre
queestamostrabalhandocombancodedadoséaformacomofechamosnos-
sasconexões.Onossocódigopareceestarfazendoissoadequadamente,não
acha?Dêumaboaolhada:
public class RepositorioDeProdutos {
public ObservableList<Produto> lista() {
// código omitido
try {
// código omitido
conn.close();
} catch (SQLException e) {
throw new RuntimeException(e);
}
return produtos;
}
}
Tudopareceestarcerto,afinalestamosfechandoaconexão. Issoéfeito
dentrodobloco try,logoapósexecutarocódigonobancodedados.Mas
oqueaconteceráquandoessecódigolan çaruma Exception?Bem,vocêjá
deveterpercebidooproblema.Ocódigodobloco tryseráinterrompido,o
catchseráexecutadoeaconexãonãoseráfechada.
Uma forma de resolver o problema seria adicionando a chamada ao
método closetambémdentrodo catch,comonoexemplo:
public class RepositorioDeProdutos {
75

## Página 86

4.8. Qualamelhorformadefecharaconexão? CasadoCódigo
public ObservableList<Produto> lista() {
// código omitido
try {
// código omitido
conn.close();
} catch (SQLException e) {
conn.close();
throw new RuntimeException(e);
}
return produtos;
}
}
Issoresolveoproblema,masoquevocêachadasoluç ão?Nuncaémuito
interessantereplicarcódigodessaforma;oqueaconteceriaseessemétodo
tivessemúltiplosblocos catch?Copiamosecolamosemcadaumdeles?E
seesquecermosdealgum?
Pornossasortenãoprecisamosfazerdessaforma,quenãopareceser
ideal.Podemosutilizaro finally:
public class RepositorioDeProdutos {
public ObservableList<Produto> lista() {
// código omitido
try {
// código omitido
} catch (SQLException e) {
throw new RuntimeException(e);
} finally {
conn.close();
}
return produtos;
}
}
As instruções de dentro do blocofinallysempre são executadas,
emcasode exceptionounão. Ésempremuitointeressantefazeroper-
76

## Página 87

CasadoCódigo Capítulo4. BancodeDadoseJDBC
açõescomoesta,defecharumaconexão,dentrodessebloco.Colocamosno
finallyoperaçõesquedevemserexecutadasaqualquercusto.
Masaindaháumproblema.Sevocêfezessamudan ça,jádeveterperce-
bidoqueocódigoparoudecompilar.Oproblemaéqueométodo closeda
classe Connectionlançauma checkedexception,ouseja,umaexce çãoque
precisasertratadaoudeclarada.Adicionarumnovo try catch dentrodo
bloco finallyteriaumcustobemgrandenalegibilidadedessecódigo.Re-
parecomoeleficaria:
public class RepositorioDeProdutos {
public ObservableList<Produto> lista() {
// código omitido
try {
// código omitido
} catch (SQLException e) {
throw new RuntimeException(e);
} finally {
try {
conn.close();
} catch (SQLException e) {
throw new RuntimeException(e);
}
}
return produtos;
}
}
Ocódigoficoubemruim,nãoacha? Pornossasorte,oJava7trouxe
umanovidademuitointeressante,conhecidacomo try-with-resources.
Vocêpodedeclararetambéminicializara Connectiondentrodo try,
comoaseguir:
public class RepositorioDeProdutos {
public ObservableList<Produto> lista() {
77

## Página 88

4.9. OpadrãodeprojetoDAO CasadoCódigo
// código omitido
try (Connection conn = new ConnectionFactory()
.getConnection()) {
// código omitido
} catch (SQLException e) {
throw new RuntimeException(e);
}
return produtos;
}
}
Pronto,aconexãoseráfechadaparavocê,independentedeseocódigo
funcionououlan çouumaexception. Masemquemomentochamamos
ométodo close? Arespostaé: emnenhum. Osegredodesserecurso
estánainterface AutoCloseable,queinterfacescomoa Connection
herdam. Vocêsópodeusaro try-with-resourcesemobjetosdotipo
AutoCloseable, assimoJavasabeexatamentequalométodoquedeve
serchamadoapósaexecuç ãodoseu try catch. Elefuncionacomoum
finallyimplícito.
4.9 O padrão de projeto DAO
Uma última alteração que podemos fazer nessa classe, a
RepositorioDeProdutos, é em seu nome. O que estamos fazendo
éumapráticabemcomum:isolaralógicadeacessoaobancodedadosem
umaclasseespecialistanestetrabalho.Ofluxoatualestáassim:
Fig.4.7:Fluxoatualdeacessoadados.
O benefício deencapsularessa regra de negócios (acesso ao banco)
em uma classe já é facilmente notado quando pensamos em evoluções
futuras. Por exemplo, se no lugar de persistirmos as informações em
78

## Página 89

CasadoCódigo Capítulo4. BancodeDadoseJDBC
um banco de dados resolvermos utilizar uma planilha deExcel, quantas
classes precisarão ser alteradas em nosso projeto? Apenas uma, nosso
RepositorioDeProdutos.
Fig.4.8:Acessoadadosdobancoouplanilha.
Comoocomportamentoestáisolado,encapsulado,ficafácilevoluirsem
causarefeitoscolateraisindesejados. Paraaclasse Main,poucoimporta
sequandoelachama repositorio.lista()alistagemécarregadade
umaplanilhaoubasededadosdoMySQL, PostgreSQL,Oracleouqualquer
outro. PoucoimportaseestamosusandoJDBCoualgumaferramentaque
simplifiqueotrabalho,comoo hibernate.Oqueimportaparaquemchamao
método listaéqueeleretornealistagemdeprodutos,eponto.
Essaboapraticaétãoconhecidaeutilizadanodiaadiaqueacabouvi-
randoumdosmaisimportantes DesignPatterns;eleéusadoemtodosospro-
jetosqueconhe ço!Talvezvocêjátenhaouvidofalardotermo DAO,eisseu
significado:éumacrônimopara Data Access Object.
Mesmosemsaber,jáestamosusandoo designpattern DAO,masémuito
comumerecomendadoseguirmosopadrãodenomedessetipodeclasse.
Comoelaencapsulaacessoadadosdaclasse Produto,porpadrãonormal-
menteachamamosde ProdutoDAO.
Notequeémuitosimilaraoquefizemoscoma ConnectionFactory,
queéoutro designpattern queconhecemos. Comoelaéumafábricade
Connection,recebecomoprefixoonomedaclasseecomosufixoapalavra
Factory.
Agora que sabemos a convenção, vamos fazer a alteração em nosso
código. PararenomearumaclassepeloEclipse,bastaselecionaressaclasse
79

## Página 90

4.9. OpadrãodeprojetoDAO CasadoCódigo
pelopackageexplorer(viewlateral)epressionar F2.
Umajanelachamada RenameCompilationUnit deveserexibida. Para
concluir,mudamosonomepara ProdutoDAOeclicamosem Finish.
80

## Página 91

CasadoCódigo Capítulo4. BancodeDadoseJDBC
Nosso DAOcompletodeveficarassim:
public class ProdutoDAO {
public ObservableList<Produto> lista() {
ObservableList<Produto> produtos =
observableArrayList();
PreparedStatement ps;
try (Connection conn =
new ConnectionFactory().getConnection()) {
ps = conn.prepareStatement(
"select * from produtos");
ResultSet resultSet = ps.executeQuery();
while(resultSet.next()) {
LivroFisico livro =
new LivroFisico(new Autor());
livro.setNome(resultSet.getString("nome"));
81

## Página 92

4.9. OpadrãodeprojetoDAO CasadoCódigo
livro.setDescricao(resultSet.getString(
"descricao"));
livro.setValor(resultSet.getDouble("valor"));
livro.setIsbn(resultSet.getString("isbn"));
produtos.add(livro);
}
resultSet.close();
ps.close();
} catch (SQLException e) {
throw new RuntimeException(e);
}
return produtos;
}
public void adiciona(Produto produto) {
PreparedStatement ps;
try (Connection conn =
new ConnectionFactory().getConnection()) {
ps = conn.prepareStatement("insert into produtos
(nome," + " descricao, valor, isbn)
values (?,?,?,?)");
ps.setString(1, produto.getNome());
ps.setString(2, produto.getDescricao());
ps.setDouble(3, produto.getValor());
ps.setString(4, produto.getIsbn());
ps.execute();
ps.close();
} catch (SQLException e) {
throw new RuntimeException(e);
}
}
}
Oúnicoimpactoemnossaclasse Mainseránalinhaemqueusávamos
o RepositorioDeProdutos:
ObservableList<Produto> produtos =
82

## Página 93

CasadoCódigo Capítulo4. BancodeDadoseJDBC
new RepositorioDeProdutos().lista();
Agoraqueelechama ProdutoDAO,alinhaficaráassim:
ObservableList<Produto> produtos = new ProdutoDAO().lista();
Masnãosepreocupeemalterarmanualmente,oEclipsejáfezissopara
você.
Ofluxoagoraé:
Fig.4.11:AcessoadadosencapsuladoemumDAO.
Outras alternativ as para renomear classes
Aformaquevimoséumadasmuitasdeserenomearumaclassepela
IDE.Outraop çãobastantecomumpeloEclipseéutilizandooatalho
Control+ Shift+ R(rename). Adiferençaéqueoutilizamosdi-
retamentenaclasse,comocursorsobseunome:
Bastamudarseunomeedepoispressionar Enter.Todosquefazem
referênciaparaessaclassetambémserãoatualizadosautomaticamente.
83

## Página 94

4.9. OpadrãodeprojetoDAO CasadoCódigo
Tambémpodemosrenomearopacotedonosso ProdutoDAO,queatual-
mentesechama repositorio.Vamosalterarpara dao.Oprocessoseráo
mesmo,clicamosnopacote,pressionamos F2,escolhemosumnovonomee
depois Finish.Eleficaráassim:
Avantagemdeutilizaressasconven çõesdenomeséqueémuitomais
fácilparaquemcairdeparaquedas noprojetosaibasecontextualizar.Sevocê
entrarhojeemumprojetoeprecisaralteraraformaqueum Usuarioé
persistido,qualclassevocêvaiabrir? O UsuarioDAO.Nãotemerro,você
nãoprecisasabernadasobreoprojetoparasaberdisso.
84

## Página 95

Capítulo5
ThreadseParalelismo
Aconsultaaobancodedadosquealimentanossalistagemdeprodutosésu-
ficientementerápida,afinalestamostrabalhandocompoucosvalores.Masjá
parouparapensaroqueaconteceriaseelademorassepararesponder?Outro
pontoquepoderiacausarumproblemaéaexportaç ãodessalistaparaoar-
quivo CSV.Quantomaisprodutos,maiseladevedemorar.Comonossaapli-
caçãoreageenquantoumatarefaestádemorandoparaserexecutada?
Nestecapítulo,veremosesseproblemaemprática,assimcomoumaal-
ternativapararesolvê-lo.VamosconhecerumpoucodaformacomooJava
fazparaexecutaraçõesemparalelo,comusode Threads,classesanônimas
emuitoslambdasdoJava8. Sevocêaindanãoestáacostumadocomesse
recurso,comcertezavaiaproveitarbastanteosexemplosdestecapítulopara
praticar.

## Página 96

5.1. Processamentodemorado,eagora? CasadoCódigo
5.1 P rocessamento demorado , e agora?
Umaformasimplesdeexperienciarissoempráticaseriafor çandonossaapli-
caçãoadormirporalgunsinstantes,nomomentoemquegeramosoarquivo
CSV.Assimconseguimossimularqueafun çãodemoracercade20segundos
paraserexecutada.
button.setOnAction(event -> {
Thread.sleep(20000);
exportaEmCSV(produtos);
});
Vejaquequemcuidoudessetrabalhofoiométodoestático sleep,pre-
sentenaclasse Thread(quemuitoembreveserádesmistificada).Essaclasse
estápresentenopacote java.lang,portantonãoprecisaserimportada.Ele
recebecomoparâmetrootempoemmilissegundosemquedevedormir(tem-
porariamentepausar)alinhadeexecuçãoatual,eofor çaatrataroudeclarar
uma InterruptedException.
button.setOnAction(event -> {
try {
Thread.sleep(20000);
} catch (InterruptedException e) {
System.out.println("Ops, ocorreu um erro: "+ e);
}
exportaEmCSV(produtos);
});
Depoisdessaalteração,aaçãodeexportaroarquivo produtos.csvvai
levarpelomenos20segundosparaserexecutada. Executeaaplicaç ãopara
verissoacontecendo.
Oqueacontecesevocêtentarredimencionarajanela,clicarnaslinhasda
tabela,oufazerqualquercoisasimilarenquantoaaç ãodo buttonestásendo
executada?
86

## Página 97

CasadoCódigo Capítulo5. ThreadseParalelismo
Fig.5.1:Aplicaçãonãorespondendo,totalmentetravada.
Aaplicaçãoficatotalmentetravada!
A necessidade de executar ações em paralelo
Podemsermuitasassituaçõesemqueprecisamosexecutaraçõesempar-
alelo.Emumsistemaoperacional,porexemplo,fazemosissootempotodo!
Podemosfazerumdownloadeaomesmotemponavegarnainternet.Jápen-
soucomoseriaterqueesperarodownloadterminarparasódepoisfazerqual-
queroutracoisa?Oprópriosistemaoperacionaljágerenciatodososprogra-
masexecutadosemváriosprocessosparalelos,nãoprecisamosnospreocupar
comisso.
EmnossaaplicaçãoJavatambémpodemosexecutaraçõesemparalelo,
comoexportarosdadosdalistagemsemterquetravarasdemaisfun çõese,
enquantoisso,mostraroavan çodafunçãodeexportarparadarumretorno
(feedback)aousuário.
5.2 T rabalhando com Threads em Jav a
Em Java podemos criar linhas de execuções paralelas utilizando a classe
Thread,dopacote java.lang,amesmaqueutilizamosparafazeraapli-
87

## Página 98

5.2. TrabalhandocomThreadsemJava CasadoCódigo
caçãodormirpor20segundos.
Paracriareiniciaraexecuç ãodeuma thread,sóprecisamosinstanciar
umobjetodessetipoechamarseumétodo start:
Thread thread = new Thread();
thread.start();
Masháumaquestão,oqueessa threadfaz? Criamosumanovalinha
deexecução,masemnenhummomentodissemosoqueeladevefazer. Ela
morreráassimqueforcriada.
Aclasse Threadtemumconstrutorquerecebecomoargumentoumob-
jetocomocódigoquequeremosexecutar,tudoqueprecisamosfazerécriar
essaclasse.Vamoschamá-lade ExportadorDeCSV,jáqueéissooquequer-
emosfazeremparalelo.
package threads;
public class ExportadorDeCSV {
public void exporta() {
// código que deve ser executado em paralelo
}
}
Vamos,agora,nomomentodecriaruma Thread,passaroexportador
comoargumento:
ExportadorDeCSV exportador = new ExportadorDeCSV();
Thread thread = new Thread(exportador);
thread.start();
Tudoparececerto,masessecódigonãovaicompilar.Oerroserá:
constructor java.lang.Thread.Thread(java.lang.Runnable) is
not applicable. (argument mismatch; threads.ExportadorDeCSV
cannot be converted to java.lang.Runnable)
Fazsentido,afinal,comoa Threadsaberáqualométodoquedeveser
executado?Eseaclasse ExportadorDeCSVtivessedezmétodos,comoela
escolheriaum?
88

## Página 99

CasadoCódigo Capítulo5. ThreadseParalelismo
5.3 O contrato Runnable
Paraensinaràclasse Threadqualmétododeveserexecutadoedaruma
garantiaaocompiladordequeessemétodoestádeclaradoemnossaclasse,
usamosum contrato,umainterfaceJava.Nãoprecisamoscriarumanovain-
terface;sevocêolharcomaten çãonamensagemgeradapeloerrodecompi-
lação,vocêperceberáqueessecontratojáexisteeéesperado.Estamosfalando
dainterface java.lang.Runnable.
Umaclassequeassinaocontrato Runnableassumearesponsabilidade
deserumexecutável.Essainterfacetemumúnicométodo,chamado run.
Poressemotivo,a Threadsabeexatamentecomoexecutá-la.
Vamosmodificarnosso ExportadorDeCSVparaimplementaressain-
terface. Agoraquesabemoscomoométododevesechamar,trocaremoso
nomedométodode exportapara run:
package threads;
public class ExportadorDeCSV implements Runnable {
@Override
public void run() {
// código que deve ser executado em paralelo
}
}
Ótimo,nossocódigopassouacompilar.
Paratestar,coloqueum System.out.printlnnométodo run.Algo
simples,como:
package threads;
public class ExportadorDeCSV implements Runnable {
@Override
public void run() {
System.out.println("Rodando em paralelo!");
}
}
89

## Página 100

5.3. OcontratoRunnable CasadoCódigo
Agora,crieaclasse TestandoThread,comoseguintemétodo main:
package threads;
public class TestandoThread {
public static void main (String... args) {
ExportadorDeCSV exportador = new ExportadorDeCSV();
Thread thread = new Thread(exportador);
thread.start();
System.out.println("Terminei de rodar o main");
}
}
Executeocódigoparaveroresultado.Deveráseralgocomo:
Rodando em paralelo!
Terminei de rodar o main
Aordempodevariar,jáquesãoduaslinhasdeexecuçõesemparalelo.
Masnãosepreocupecomissoagora. Oimportanteéasduasmensagens
teremsidoimpressasnoconsole.Notequeemnenhummomentochamamos
ométodo rundonosso ExportadorDeCSV,masaochamarométodo
startdaclasse Threadelafezissopornós.
90

## Página 101

CasadoCódigo Capítulo5. ThreadseParalelismo
Para saber mais: escalonador de Threads
Comoexecutamosaçõesemparaleloquandoexisteumúnicopro-
cessadornamáquina? Osegredoestáno schedulerdethreads. Eleé
umescalonadorquepegatodasas threadsqueprecisamserexecutadas
efazseuprocessadoralternarentreelas. Issoacontecetãorápidoque
parecequeasduas(oumais) threadsestãorodandoaomesmotempo.
Essaalternaçãoqueelefazéconhecidacomo context switch,outroca
decontexto.
Quandoexistemdoisoumaisprocessadores,amáquinavirtualdo
Javaegrandeparte(senãotodos)ossistemasoperacionaisconseguem
tirarproveitodisso.Nessecaso,verdadeiramenteteremosexecuçõespar-
alelas,aindaescalonadaspelo schedulerdoJava.Issoporquepodemos
ter20 threadssendoexecutadasemdoisprocessadores,porexemplo.A
diferençaéqueatrocadecontextoaconteceráentreelesenãoemum
únicoprocessador.
5.4 T hreads com classes anônimas e lambdas
No lugar de criarmos a classeExportadorDeCSV implementando um
Runnable,poderíamosfazerissodiretamenteutilizandouma classeanôn-
ima. Isso é extremamente comum quando estamos trabalhando com
Threads.Ocódigoficariaassim:
Runnable exportador = new Runnable() {
@Override
public void run() {
System.out.println("Rodando em paralelo!");
}
};
Thread thread = new Thread(exportador);
thread.start();
Nolugardeextrairasvariáveisintermediárias,énaturalfazerissodireta-
mente:
91

## Página 102

5.4. Threadscomclassesanônimaselambdas CasadoCódigo
new Thread(new Runnable() {
@Override
public void run() {
System.out.println("Rodando em paralelo!");
}
}).start();
Ocódigocompletodaclasse TestandoThreadfica:
package threads;
public class TestandoThread {
public static void main (String... args) {
new Thread(new Runnable() {
@Override
public void run() {
System.out.println("Rodando em paralelo!");
}
}).start();
System.out.println("Terminei de rodar o main");
}
}
Vamosexecutarocódigoparaveroresultado?Amesmacoisa.Asduas
mensagensserãoimpressas,podendovariarumpoucoaordem,jáquesão
executadasemparalelo.
Oproblemadessecódigoestátantonaverbosidadequantonasintaxe,que
ébempoluída.Chegamachamaressetipodecódigode “problemavertical
,porcausadaquantidadedelinhas.
Essafoiumadasmotivaçõesparaintroduçãodas expressõeslambdas,do
Java8.Assimcomojáestamosusandoesserecursocomaaç ãodo button,
podemosusarcomo Runnable. Osegredoestánoconceitode interface
funcional,queécomoumainterfacedeumúnicométodoabstratoéchamada
noJava8.
Emoutraspalavras,comoum Runnablesótemummétodoabstrato,
podemosusarasintaxedolambda,jáqueoJavasaberáexatamentequal
92

## Página 103

CasadoCódigo Capítulo5. ThreadseParalelismo
métodoestásendoimplementado.Ocódigoficaráassim:
package threads;
public class TestandoThread {
public static void main (String... args) {
new Thread(() -> {
System.out.println("Rodando em paralelo!");
}).start();
System.out.println("Terminei de rodar o main");
}
}
Oqueacha,maissimples?Asintaxepodeparecerestranhanocome ço,
massemdúvidaocódigoestámaisenxuto.Comoexisteapenasumaúnica
instruçãodentrodaexpressãolambda,podemostiraraschaves,pontoevír-
gulaecolocartudoemumúnico statement:
package threads;
public class TestandoThread {
public static void main (String... args) {
new Thread(() -> System.out
.println("Rodando em paralelo!")).start();
System.out.println("Terminei de rodar o main");
}
}
OfocodolivronãoéJava8,massevocêaindanãoestáacostumadocom
asexpressõeslambdaseoutrosrecursos,nãodeixedepraticar. Ficoucom
algumadúvida?Lembre-sedemandarume-mailnalistadogrupo.
93

## Página 104

5.5. Exportandoemumathreadseparada CasadoCódigo
5.5 E xportando em uma thread separada
Pronto,agoraqueconhecemosumpoucomaissobre ThreadsemJava,
podemosatacaroproblemadalógicadeexportarem CSV.Paranãotravar
aaplicação,podemosrodartodaalógicadeexportaralistadeprodutosem
paralelo!
Vamosaplicaressamudan çaàclasse Main.A actiondo buttonficará
assim:
Button button = new Button("Exportar CSV");
button.setOnAction(event -> {
new Thread(() -> {
try {
Thread.sleep(20000);
} catch (InterruptedException e) {
System.out.println("Ops, ocorreu um erro: "+ e);
}
exportaEmCSV(produtos);
}).start();
});
94

## Página 105

CasadoCódigo Capítulo5. ThreadseParalelismo
Se você está com Jav a7 ...
EmJava7,comusodasclassesanônimas,essecódigoficariaassim:
Button button = new Button("Exportar CSV");
button.setOnAction(new EventHandler<ActionEvent>() {
@Override
public void handle(ActionEvent event) {
new Thread(new Runnable() {
@Override
public void run() {
try {
Thread.sleep(20000);
} catch (InterruptedException e) {
System.out.println("Ops,
ocorreu um erro: "+ e);
}
exportaEmCSV(produtos);
}
}).start();
}
});
ValelembrarquevocênãoprecisateroJava8instaladopararodar
essesexemplos,nofinaldocapítulovoumostrarocódigocompletocom
Java7também.Aproveiteparafazerumacomparaçãoentreasduassin-
taxes.
Para melhorar um pouco a legibilidade, vamos extrair o código do
Thread.sleep,quefazaaplicaç ãodormirpor20segundos,paradentro
deummétodo:
private void dormePorVinteSegundos() {
try {
Thread.sleep(20000);
95

## Página 106

5.5. Exportandoemumathreadseparada CasadoCódigo
} catch (InterruptedException e) {
System.out.println("Ops, ocorreu um erro: " + e);
}
}
Agoraocódigoda actiondeexportarem CSVficaassim:
button.setOnAction(event -> {
new Thread(() -> {
dormePorVinteSegundos();
exportaEmCSV(produtos);
}).start();
});
Comessasalterações,ocódigocompletodaclasse Maindeveficarda
seguinteforma:
package application;
// imports omitidos
@SuppressWarnings({ "unchecked", "rawtypes" })
public class Main extends Application {
@Override
public void start(Stage primaryStage) {
Group group = new Group();
Scene scene = new Scene( group, 690, 510);
ObservableList<Produto> produtos =
new ProdutoDAO ().lista();
TableView< Produto> tableView =
new TableView<>(produtos);
TableColumn nomeColumn = new TableColumn("Nome");
nomeColumn .setMinWidth(180);
nomeColumn .setCellValueFactory(
new PropertyValueFactory("nome"));
96

## Página 107

CasadoCódigo Capítulo5. ThreadseParalelismo
TableColumn descColumn = new TableColumn("Descrição");
descColumn.setMinWidth(230);
descColumn.setCellValueFactory(
new PropertyValueFactory("descricao"));
TableColumn valorColumn = new TableColumn("Valor");
valorColumn .setMinWidth(60);
valorColumn .setCellValueFactory(
new PropertyValueFactory("valor"));
TableColumn isbnColumn = new TableColumn("ISBN");
isbnColumn.setMinWidth(180);
isbnColumn.setCellValueFactory(
new PropertyValueFactory("isbn"));
tableView.getColumns().addAll(nomeColumn, descColumn,
valorColumn, isbnColumn);
final VBox vbox = new VBox(tableView);
vbox.setPadding(new Insets(70, 0, 0 ,10));
Label label = new Label("Listagem de Livros");
label.setFont(Font
.font("Lucida Grande", FontPosture.REGULAR, 30));
label.setPadding(new Insets(20, 0, 10, 10));
Button button = new Button("Exportar CSV");
button.setLayoutX(575);
button.setLayoutY(25);
button.setOnAction(event -> {
new Thread(() -> {
dormePorVinteSegundos();
exportaEmCSV(produtos);
}).start();
});
97

## Página 108

5.5. Exportandoemumathreadseparada CasadoCódigo
group.getChildren().addAll(label, vbox, button);
primaryStage.setTitle(
"Sistema da livraria com Java FX");
primaryStage.setScene(scene);
primaryStage.show();
}
private void exportaEmCSV(ObservableList<Produto> produtos){
try {
new Exportador ().paraCSV(produtos);
} catch (IOException e) {
System.out.println("Erro ao exportar: "+ e);
}
}
private void dormePorVinteSegundos() {
try {
Thread.sleep(20000);
} catch (InterruptedException e) {
System.out.println("Ops, ocorreu um erro: "+ e);
}
}
public static void main(String[] args) {
launch(args);
}
}
Prontoparatestarmaisumavez?Executeaaplicaç ãoemandeexportara
listadeprodutoscomo CSV.Vocêvaiperceberque,mesmoqueessecódigo
demore20segundosparaserexecutado,orestantedaaplicaç ãocontinuafun-
cionandosemtravar.Experimenteredimencionarajanela,clicarnaslinhas
databelaetc.Tudocontinuafuncionando.
98

## Página 109

CasadoCódigo Capítulo5. ThreadseParalelismo
5.6 U m pouco mais sobre as Threads
Trabalharcom Threadsnemsempreéumsonho.Quandoestamostrabal-
handocomlinhasdeexecuçõesdiferentes,acomplexidadedenossocódigo
aumenta.Háaindaumapreocupaçãoconstante,quesãoostemíveisproble-
masdeconcorrência.Oquepoderiadarerrado?
Dêumaboaolhadanoseguintecódigo:
public class LivroFisico extends Livro
implements Promocional {
private boolean jaTeveDesconto = false;
// parte do código omitido
public boolean aplicaDescontoDe(double porcentagem) {
if (jaTeveDesconto) {
return false;
}
jaTeveDesconto = true;
// restante do código do método
}
}
Grandepartedocódigoestáomitido, massóprecisamosfocarnessa
parte. Essaclassepossuiummétodochamado aplicaDescontoDe,que
daformaqueestásóaplicaodescontoumaúnicavezporinstância.Temos
umatributobooleanparanosajudar,o jaTeveDesconto.Ocódigoébem
simplesetudoparececerto.Decertamaneiraestá,oproblemasóvaiaparecer
quandoduasoumais Threadconcorrerempeloacessodessemétodo.
Imaginequequeremosfazerumprocessamentoemmassa,emtodosos
nossoslivros,chamandoométodo aplicaDescontoDe. Esseprocessa-
mentoseráexecutadoemparalelo,comdiversas Threads.Oqueacontece
seduas Threadspassarem“aomesmotempo”peloifquevalidaseelejá
tevedesconto?
Issopoderesultaremumdesastre. Comoaprimeira Threadpode
ainda não ter chegado à linha que atribuitrue ao valor do atributo
jaTeveDesconto,asduasvãopassarpelo if.Emoutraspalavras,vamos
aplicarodescontoduasvezesparaomesmoobjeto.
99

## Página 110

5.6. Umpoucomaissobreas Threads CasadoCódigo
Claro,esseéumexemplobemsimpleseoproblemanãoaconteceriasem-
pre.Essecódigopoderiaserexecutadoporummêssemnuncaaconteceruma
acessoconcorrente,atéqueumbelodiao schedulerdethreadspassasseduas
paraomesmoobjeto.
Comoimpedirisso?OJavanosofereceumrecursointeressante,ummeio
degarantirqueapenasuma Threadacessarádeterminadoblocooumétodo.
Seoutra Threadchegar,elavaiprecisaresperaraprimeiraterminartodoo
trabalhoparadepoiscome çaroseu.Oacessoé sincronizado.
public class LivroFisico extends Livro
implements Promocional {
private boolean jaTeveDesconto = false;
// parte do código omitido
public synchronized boolean
aplicaDescontoDe(double porcentagem) {
if (jaTeveDesconto) {
return false;
}
jaTeveDesconto = true;
// restante do código do método
}
}
Notenousodapalavrachave synchronized.Éelaquemdáessacarac-
terísticaaométodo aplicaDescontoDe.Comisso,jáestamosprevenindo
acessoconcorrenteaessalógica,garantimosquenãoexistiráconcorrência
nela.Normalmentechamamosde thread safeumaclassequeestáprotegida
contraacessoconcorrente.
100

## Página 111

CasadoCódigo Capítulo5. ThreadseParalelismo
Bloco sincronizado
Utilizandoomodificador synchronizedemummétodo,estamos
dizendoquetodoocódigodaquelemétodoésincronizado.Fazsentido.
Mascomodizerqueapenasumblocodecódigodevesersincronizado?
Háumaoutraformadeutilizaro synchronized,definindoum
blocodecódigoquerecebequaléoobjetoqueserábloqueado:
public boolean aplicaDescontoDe(double porcentagem) {
synchronized (this) {
if (jaTeveDesconto) {
return false;
}
}
jaTeveDesconto = true;
// restante do código do método
}
Agoraapenaso ifestánoblocodo synchronized,nolugarde
todoométodo.
5.7 Garbage Collector
Nãopodemosfalarde threadssemcomentarsobreuma Threadbastante
conhecidaemJava,responsávelporjogarforaosobjetosquenãoestãomais
sendoreferenciadosemnossocódigo.Estamosfalandodofamoso Garbage
Collector(coletordelixo).
Jánãoéumanovidadequequandocriamosumnovoobjeto,suasinfor-
maçõesserãomantidasemmemória.Atribuímosesseobjetodotipo Autor,
porexemplo,aumavariávelparafuturamentetermosumaformadenosref-
erenciarmosaele:
Autor autor = new Autor();
101

## Página 112

5.7. GarbageCollector CasadoCódigo
Fig.5.2:Variávelautorreferenciandooobjetoemmemória.
Masoqueacontececomoobjetoemmemóriaquandodeixamosdenos
referenciaraele?Porexemplo,aoatribuirumnovoautorparaessavariável:
Autor autor = new Autor();
Autor outro = new Autor();
autor = outro;
Fig.5.3:Duasvariáveisreferenciandoomesmoobjeto.
Apartirdessemomento,ninguémmaisestáreferenciandoesseobjeto,di-
retaouindiretamente.Issosignificaqueelenãoexistemaisemmemória?Não
necessariamente.Significacomtodaacertezaqueelenãoestámaisacessível,
masnãoqueelefoiremovidodamemória.
Vale lembrar que quem cuida desse trabalho é oGarbage Collector
(GC),queéuma Thread. Masquandoelaéexecutada? Atodomo-
mento? Provavelmentenão,issoteriaumcustobemgrandeetotalmente
102

## Página 113

CasadoCódigo Capítulo5. ThreadseParalelismo
desnecessário.Elaéexecutadadeformaestratégica,quandoforprecisoecon-
venienteparaaJVM,podendodependerdeumaimplementaç ãoparaoutra.
Nãoháumaformadeobrigara threaddoGarbageCollectoraserexecu-
tada.Aclasse Systematépossuiummétodoestáticochamado gc,masnão
seengane,chamá-lonãosignificaqueo GCseráexecutado.Issoapenassug-
ereparaaJVMquerodeoGC,elapodeounãoaceitar.Ousodessemétodo
normalmenteédesencorajado,sãopouquíssimasassituaçõesemqueusá-lo
faráalgumadiferençaemsuaaplicação,oidealénãodependerdisso.
5.8 J av aFX assíncrono
AgoraquejáconhecemosumpoucomaissobreaAPIde ThreadsdoJava,
podemosvoltaraonossocódigo.Resolvemosoproblemadeaaç ãodemorada
travaraaplicação,masnãoestamosdandoumarespostamuitoadequadapara
oclientequepediualistacomoum CSV.Eleclicanãobotão,olhanodiretório
eoarquivo produtos.csvaindanãoestálá.Sódepoisdealgunssegundos
oarquivoégerado.
Paramelhorarisso,podemosmostrarumamensagemindicandoqueo
arquivoestásendoexportadoelogoemseguidaatualizá-laparaindicarque
otrabalhofoiconcluído.
Vamos começar criando uma Label chamada progresso, para
mostrarestetexto.
Label progresso = new Label();
Notequenãoatribuímosumtextoinicialparaela,seutextoseráadi-
cionadoeatualizadodinamicamentepelaaçãodeexportarprodutos.
Lembre-sedeque,paradeixá-lavisível,precisamosadicioná-laao group
deelementosdessatela:
group.getChildren().addAll(
label, vbox, button, progresso);
Ótimo,agorapodemostentaradicionareatualizarseutextodentroda
Threadqueaconteceno setOnActiondobotãodeexportar.Umapossi-
bilidadeseria:
103

## Página 114

5.9. TrabalhandocomaclasseTask CasadoCódigo
button.setOnAction(event -> {
new Thread(() -> {
progresso.setText("Exportando...");
dormePorVinteSegundos();
exportaEmCSV(produtos);
progresso.setText("Concluído!");
}).start();
});
Comisso, queremosque, aoiniciar, nossa Threadadicioneotexto
Exportando...no Label,quechamamosde progresso.Quandocon-
cluir,mudeseutextopara Concluído!.Parecefazersentido,nãoacha?Mas
aoexecutar:
Exception in thread "Thread-5"
java.lang.IllegalStateException:
Not on FX application thread;
Issoaconteceuporquenãopodemosadicionarouatualizarotextodeum
elementodoJavaFXemuma ThreadquenãosejadoJavaFX,ousuaprópria
Threadprincipal.
5.9 T rabalhando com a classe Task
Paranosajudarnessetrabalho,oJavaFXofereceumaclassechamada Task.
Essaclasseébemútilquandoestamostrabalhandodeformaassíncrona,
comojáveremosemprática. Elatemumúnicométodoabstrato,chamado
call.
Comumenteinstanciamosuma Taskutilizandoclassesanônimas:
Task<Void> task = new Task<Void>() {
@Override
protected Void call() throws Exception {
// algum trabalho
return null;
}
};
104

## Página 115

CasadoCódigo Capítulo5. ThreadseParalelismo
Pergunta: por que não um lambda?
Talvezvocêsepergunteporquecriamosa Taskusandoumaclasse
anônimaenãocomumaexpressãolambda? Porquefuncionacomo
Runnable,masnãocoma Task.Nãovoufalararespostaagora,tente
descobrir.Ok?Nãosepreocupe,embreveeulheconto.
A Taskpodeterumretorno,masnoteque,comonãoqueremosretornar
nada,utilizamosotipo Void(classewrapperdojátãoconhecido void).
Vamosmodificarnossocódigoparaque,nolugardeexecutarométodo
dedormirpor20segundoseexportardentrodeum Runnable,elafaçaisso
dentroda Task.
Nolugardefazer:
button.setOnAction(event -> {
new Thread(() -> {
dormePorVinteSegundos();
exportaEmCSV(produtos);
}).start();
});
Vamosquebraressetrabalhoemduaspartes,primeirocriandoumain-
stânciade Taskcujométodo callfaráessetrabalho.Eladeveficardentro
do setOnAction,nobotãodeexportar:
button.setOnAction(event -> {
Task<Void> task = new Task<Void>() {
@Override
protected Void call() throws Exception {
dormePorVinteSegundos();
exportaEmCSV(produtos);
return null;
}
};
});
105

## Página 116

5.9. TrabalhandocomaclasseTask CasadoCódigo
Agora,aindadentrodo setOnAction,vamoscriareiniciarumanova
Threadpassandoessa Taskcomoargumento.
button.setOnAction(event -> {
Task<Void> task = new Task<Void>() {
@Override
protected Void call() throws Exception {
dormePorVinteSegundos();
exportaEmCSV(produtos);
return null;
}
};
new Thread(task).start();
});
Otrechodecódigodobotãodeexportarficaráassim:
Button button = new Button("Exportar CSV");
Label progresso = new Label();
button.setOnAction(event -> {
Task<Void> task = new Task<Void>() {
@Override
protected Void call() throws Exception {
dormePorVinteSegundos();
exportaEmCSV(produtos);
return null;
}
};
new Thread(task).start();
});
Podemosexecutarnossaaplicaçãoparaconfirmarquetudoestáfuncio-
nando.
106

## Página 117

CasadoCódigo Capítulo5. ThreadseParalelismo
Resposta: por que não um lambda?
Vocêprovavelmentejádescobriuomotivo,masnãopodemosimple-
mentara Taskcomoumlambdaporqueelanãoéuma interface fun-
cional.Elanãoénemmesmouma interface:sevocêolharseucódigo
perceberáquesetratadeumaclasseanônima. Nóssópodemosusara
sintaxedolambdacominterfacesfuncionais,semexce ções.
Mas e quanto ao texto da Label?
Mudamospara Tasketudocontinuafuncionando,masequantoaotexto
da Labelde progresso?Oproblemaaindanãofoiresolvido.
AgoraqueestamosusandoaAPIdoJavaFXparaexecutarcódigoassín-
crono,podemostirarbastanteproveitodealgunsrecursos.Porexemplo,há
ummétodochamado setOnRunningem Taskquenospermiteexecutar
umeventoquandoa taskestáprestesaserexecutada.
task.setOnRunning(new EventHandler <WorkerStateEvent>() {
@Override
public void handle(WorkerStateEvent e) {
// alguma ação aqui
}
});
O EventHandlersiméumainterfacefuncional,portanto,podemos
tirarproveitodolambda.Ocódigoficaassim:
task.setOnRunning( e -> {
// alguma ação aqui
});
Nessemomento,podemosatualizarotextoda Label,dizendoqueo
produtoestásendoexportado:
task.setOnRunning(e -> {
progresso.setText("exportando...");
});
107

## Página 118

5.9. TrabalhandocomaclasseTask CasadoCódigo
Comoéumaúnicaexpressão,nãoprecisamosdaschavesnemdoponto
evírgula:
task.setOnRunning(e -> progresso.setText("exportando..."));
Ocódigodoeventode setOnActionficaráassim:
button.setOnAction(event -> {
Task<Void> task = new Task<Void>() {
@Override
protected Void call() throws Exception {
dormePorVinteSegundos();
exportaEmCSV(produtos);
return null;
}
};
task.setOnRunning(e -> progresso.setText("exportando..."));
new Thread(task).start();
});
Vamostestar. Apósmodificarocódigo,podemosexecutá-loeaoclicar
em exportaroresultadoseráoesperado:
108

## Página 119

CasadoCódigo Capítulo5. ThreadseParalelismo
Fig.5.4:Texto‘exportando...’sendoexibidonatela.
Otextoestádesalinhado,claro.Maslogocuidaremosdisso.Aindapre-
cisamosfazercomqueessetextosejaatualizadonomomentoemquea Task
sejaconcluída.Podemosfazerissoutilizandoumoutrométodode callback,
o setOnSucceeded.
Eletambémrecebeum EventHandlercomoparâmetro,portanto,va-
mosdelambda:
task.setOnSucceeded(e -> {
progresso.setText("concluído!");
});
Agoranossocódigoestáassim:
button.setOnAction(event -> {
Task<Void> task = new Task<Void>() {
@Override
protected Void call() throws Exception {
dormePorVinteSegundos();
exportaEmCSV(produtos);
return null;
}
};
109

## Página 120

5.9. TrabalhandocomaclasseTask CasadoCódigo
task.setOnRunning(e -> progresso.setText("exportando..."));
task.setOnSucceeded(e -> progresso.setText("concluído!"));
new Thread(task).start();
});
Outros métodos interessantes
Alémdo setOnRunninge setOnSucceeded,queacabamosde
conhecer,aclasse Tasktemoutrosmétodosde callbackquepodemser
muitoúteisemseudiaadia.Sãoeles:
•setOnCancelled
•setOnFailed
•setOnScheduled
Nãodeixedeconferiradocumentaç ãodaclasse Taskparasaber
maisdetalhesdesseseoutrosmétodos. Alémdepesquisar,tentetestar
algunsdelesemseuprojeto.
https://docs.oracle.com/javafx/2/api/javafx/concurrent/Task.html
Pronto,vamosveroresultado. Aoclicarem Exportar CSV amen-
sagem exportando...éexibida.Algunssegundosdepois,otextoéatual-
izadopara concluído!.Sucesso.
110

## Página 121

CasadoCódigo Capítulo5. ThreadseParalelismo
Fig.5.5:Textoconcluídosendoexibidonatela.
Porfim, podemosalinharessasmensagens. Faremosissodamesma
formacomofoifeitono button:
Label progresso = new Label();
progresso.setLayoutX(485);
progresso.setLayoutY(30);
Aoexecutaraaplicação,clincandoem Exportar CSV teremos:
111

## Página 122

5.10. Códigofinalcomesemlambdas CasadoCódigo
Apósalgunssegundos...
Perfeito.Vimosquetrabalharcom Threadsnãoéfácil,mastambémnão
éumbichodesetecabe ças.Temosquetomaralgunscuidadosextras,claro.
EmJavaFX,aclasse Taskajudabastantenessetrabalho. Elaofereceuma
formaflexíveledesacopladadeencapsulareexecutarcódigoparalelo.
5.10 C ódigo final com e sem lambdas
Nossocódigofinal,comJava8,ficouassim:
@SuppressWarnings({ "unchecked", "rawtypes" })
public class Main extends Application {
@Override
public void start(Stage primaryStage) {
Group group = new Group();
Scene scene = new Scene( group, 690, 510);
ObservableList<Produto> produtos =
new ProdutoDAO ().lista();
TableView <Produto> tableView =
112

## Página 123

CasadoCódigo Capítulo5. ThreadseParalelismo
new TableView<>(produtos);
TableColumn nomeColumn = new TableColumn("Nome");
nomeColumn.setMinWidth(180);
nomeColumn.setCellValueFactory(
new PropertyValueFactory("nome"));
TableColumn descColumn = new TableColumn("Descrição");
descColumn.setMinWidth(230);
descColumn.setCellValueFactory(
new PropertyValueFactory("descricao"));
TableColumn valorColumn = new TableColumn("Valor");
valorColumn .setMinWidth(60);
valorColumn .setCellValueFactory(
new PropertyValueFactory("valor"));
TableColumn isbnColumn = new TableColumn("ISBN");
isbnColumn.setMinWidth(180);
isbnColumn.setCellValueFactory(
new PropertyValueFactory("isbn"));
tableView.getColumns().addAll(nomeColumn, descColumn,
valorColumn, isbnColumn);
final VBox vbox = new VBox(tableView);
vbox.setPadding(new Insets(70, 0, 0 ,10));
Label label = new Label("Listagem de Livros");
label.setFont(Font
.font("Lucida Grande", FontPosture.REGULAR, 30));
label.setPadding(new Insets(20, 0, 10, 10));
Label progresso = new Label();
progresso.setLayoutX(485);
progresso.setLayoutY(30);
113

## Página 124

5.10. Códigofinalcomesemlambdas CasadoCódigo
Button button = new Button("Exportar CSV");
button.setLayoutX(575);
button.setLayoutY(25);
button.setOnAction(event -> {
Task<Void> task = new Task<Void>() {
@Override
protected Void call() throws Exception {
dormePorVinteSegundos();
exportaEmCSV(produtos);
return null;
}
};
task.setOnRunning(
e -> progresso.setText("exportando..."));
task.setOnSucceeded(
e -> progresso.setText("concluído!"));
new Thread(task).start();
});
group.getChildren().addAll(label, vbox, button,
progresso);
primaryStage.setTitle(
"Sistema da livraria com Java FX");
primaryStage.setScene(scene);
primaryStage.show();
}
private void exportaEmCSV(ObservableList<Produto> produtos){
try {
new Exportador ().paraCSV(produtos);
} catch (IOException e) {
System.out.println("Erro ao exportar: "+ e);
}
114

## Página 125

CasadoCódigo Capítulo5. ThreadseParalelismo
}
private void dormePorVinteSegundos() {
try {
Thread.sleep(20000);
} catch (InterruptedException e) {
System.out.println("Ops, ocorreu um erro: "+ e);
}
}
public static void main(String[] args) {
launch(args );
}
}
Conformeprometido,apartequemudado setOnActionemJava7:
button.setOnAction(new EventHandler<ActionEvent>() {
@Override
public void handle(ActionEvent event) {
Task<Void> task = new Task<Void>() {
@Override
protected Void call() throws Exception {
dormePorVinteSegundos();
exportaEmCSV(produtos);
return null;
}
};
task.setOnRunning(new EventHandler <WorkerStateEvent>() {
@Override
public void handle(WorkerStateEvent e) {
progresso.setText("exportando...");
}
});
task.setOnSucceeded(
new EventHandler<WorkerStateEvent>() {
@Override
115

## Página 126

5.10. Códigofinalcomesemlambdas CasadoCódigo
public void handle(WorkerStateEvent e) {
progresso.setText("concluído!");
}
});
new Thread(task).start();
}
});
Curiosamente,oEclipsenosofereceumaformabemsimplesdeconverter
classesanônimasparaexpressõeslambdaevice-versa.Bastavocêselecionar
ocódigoeutilizaroatalho Control+ 1. Quandotemosumlambda,a
opçãoConverttoanonymousclassecreation estarádisponível.
Fig.5.8:ConvertendolambdaparaclasseanônimanoEclipse.
Omesmovaleparaocaminhocontrário,quandotemosumaclasseanôn-
imaequeremostransformaremumaexpressãolambda,masnessecasoa
opçãoseráConverttolambdaexpression.EssesrecursosdaIDEnosajudam
muito,migrarclassesanônimasparalambdasnuncafoitãodivertido!
116

## Página 127

Capítulo6
CSSnoJavaFX
Nossaaplicaçãoestácadavezmaiscompleta,masantesdecontinuarveremos
comomelhoraraindamaisnãosóaaparênciadenossalistagemdeprodutos,
mastambémaqualidadeemanutenibilidadedenossocódigo.
Sevocêperceber,oestilopadrãodoJavaFXjáébastanteatraente.Sem
adicionarcoresouconfigurarnada,nossaaplicaçãojáestácomumaaparên-
ciabemaceitável.Repareemdetalhescomoabordaealinhaselecionadana
tabeladeprodutos. Aopassaromousesobobotão Exportar CSV,você
tambémpodeperceberquesuacorficarámaissuave.
MasaoutilizarestilospersonalizadosdoJavaFXvamosalémdaaparên-
cia. Vocêperceberáaolongodocapítuloqueissopossibilitadeixarnosso
códigoaindamaislimpo,enxutoefácildemanter.Vamoscome çar?

## Página 128

6.1. SeuprimeiroCSSnoJavaFX CasadoCódigo
6.1 S eu primeiro CSS no Jav aFX
Antesdesairaplicandonovosestilosemnossocódigo,vamosolharmaisde
pertoaformacomofizemosatéagora. Reparecomofizemosparaperson-
alizarafonteeadicionarum paddingemnossa Label,porexemplo.
Label label = new Label("Listagem de Livros");
label.setFont(Font.font(
"Lucida Grande", FontPosture.REGULAR, 30));
label.setPadding(new Insets(20, 0, 10, 10));
Issofuncionamuitobem,masadicionaumacertaverbosidadeanosso
código. Oquerealmenteimportaaquiéaprimeiralinha,ondecriamosa
Label.Queremosumcódigolimpoesimplesdeentender,pois,quantomais
próximodissonossocódigofor,melhorserásuamanutenibilidade. Repare
noqueacontecesetirarmosoestilodessecódigo:
Label label = new Label("Listagem de Livros");
Ficouótimo!Bemsimplesdeentender.Masoresultadovisual...
Opontoé:precisamosatacarosdoispontos.Ocódigoprecisaserlimpo,
masaomesmotemponossas viewsprecisamserestilizadasparaqueaapli-
caçãofiquemaisatraenteetenhaumaboausabilidade.
Nossasoluçãoinicialseráextrairestesestiloseaplicá-losutilizandoo
método setStyle,comoaseguir:
118

## Página 129

CasadoCódigo Capítulo6. CSSnoJavaFX
Label label = new Label("Listagem de Livros");
label.setStyle(???);
Essemétodoesperarecebercomoparâmetroaspropriedades CSSque
devemseraplicadasnoelemento.Umexemploseria:
Label label = new Label("Listagem de Livros");
label.setStyle("-fx-font-size:
30px; -fx-padding: 20 0 10 10;");
SevocêjáestáhabituadocomCSS,deveterpercebidoqueaspropriedades
aquisãomuitoparecidascomCSSqueutilizamosnaweb,tendooprefixo
-fxsemprepresentecomoumadiferen ça.Nestecaso,ocódigoestáfazendo
omesmoqueoanterior,ondedeclarávamosotamanhodafontee padding
programaticamente.Podemosexecutá-loparaverificaroresultado:
Excelente! Eleestácomaaparênciaesperada,masagorautilizandoas
propriedadesdoCSS.
119

## Página 130

6.2. Extraindoestilospraumarquivo.css CasadoCódigo
Jav aFX CSS R eferenceGuide
Nadocumentaçãodométodo setStyle,vocêencontraráumlink
diretoparaapágina CSSReferenceGuide,ondeospossíveisestilossão
explicadosdetalhadamente. Essapáginapodeajudarbastantenodiaa
dia;consulte-asemprequequiserconhecermaisdetalhessobreaspro-
priedadesepossibilidadesdosparâmetrosCSS.
Fig.6.3:DocumentaçãodométodosetStylepeloEclipse
6.2 E xtraindo estilos pra um arquivo .css
A mudança que fizemos já pode ser interessante, mas ainda não resolve
nossoproblema. Aindaestamosmisturandonossocódigodeestiloscom
o restante do código! No lugar de utilizar osetStyle dessa forma,
podemos(edevemos,semprequepossível)isolarnossosestilosnoarquivo
application.css.
SevocêcriouoprojetoutilizandoumaversãomaisatualdoEclipse,ou
qualqueroutraIDEmoderna,oarquivo application.cssdevetersido
criadojuntocomele.Nãosepreocupeseissonãoaconteceu,esseéumar-
quivonormal. Senecessário,vocêpodecriá-loclicandoem New...,sub-
menu Fileedigitandoonome application.cssouqualqueroutro
nomequepreferir.
120

## Página 131

CasadoCódigo Capítulo6. CSSnoJavaFX
Dentrodelecolocaremososeguinteconteúdo:
.label {
-fx-font-size: 30px;
-fx-padding: 20 0 10 10;
}
NotequeseparecemuitocomaestruturadoCSSpadrão. Aplicamoso
efeitoem .label,poiséaclassepadrão(default )doelemento Label. A
maiorpartedoselementosvisuaisdoJavaFXjátemumaclasse default,que
normalmenteéseupróprionome.
Agora tudo que precisamos fazer é adicionar o arquivo
application.csscomo um estilo de nosso cenário. Em nossa classe
Main,faremosalgocomo:
scene.getStylesheets().add(getClass()
.getResource("application.css" ).toExternalForm());
Pronto!Aorodaressecódigo,vemosqueoresultadonãofoibemoque
estávamosesperando:
Oefeitofoiaplicado,masparatodosos labelsda view.Paranossasorte
(ouoopostodisso)ocomponente TableViewtambémutilizalabelsemsuas
colunas.
121

## Página 132

6.2. Extraindoestilospraumarquivo.css CasadoCódigo
Identificando elementos únicos
Precisamosdeumaformaúnicadeidentificaro Labelquecontémnosso
textodalistagem,semqueosefeitosdeleinterfiramnosdemais Labelsque
existem,oupossamexistiremalgummomentofuturo,na view. Podemos
fazerissoadicionandoum identificador únicoaoelemento,comoaseguir:
Label label = new Label("Listagem de Livros");
label.setId("label-listagem");
Comovocêpodever,ométodo setIdnosajudacomessetrabalho.
Agoraquetemosumamaneiraúnicadenosreferirao Label,bastamod-
ificaroarquivo application.cssparaficarassim:
#label-listagem {
-fx-font-size: 30px;
-fx-padding: 20 0 10 10;
}
Oseletordeidtemaestruturaidêntica,masrecebeum #comoprefixo,
nolugardo .utilizadoparaasclassesdoselementos. Executeocódigoe
dessavezoresultadoseráoesperado:
Extraindo mais estilos pro application.css
Damesmaformacomofizemosparatiraro paddingna Labelprinci-
paldanossalistagem,podemostirardo VBoxqueutilizamosparaalinhara
tabela.Vejacomoeleestáagora:
122

## Página 133

CasadoCódigo Capítulo6. CSSnoJavaFX
VBox vbox = new VBox(tableView);
vbox.setPadding(new Insets(70, 0, 0 ,10));
Poderíamossimplesmenteremoverachamadaaométodo setPadding
enoarquivo application.cssadicionaroestilo:
.vbox {
-fx-padding: 70 0 0 10;
}
Masháumdetalheimportante,nemtodoelementoemJavaFXtemuma
classeseletorajádefinida.
Emoutraspalavras,paraaplicarumestilono Label,fizemos:
.label {
# estilos aqui
}
Ou seja, por padrão oLabeljá tem uma classe seletora, chamada
.label.Jáo VBoxnãotemumaclassepadrão,ouseja,oCSSqueescreve-
moscomoseletor .vboxnãovaifuncionar.Aoexecutaraappdessaforma,
percebemosqueo paddingnãofoiaplicado:
Jásabemoscomoresolveresseproblema,certo?Damesmaformacomo
demosum identificador únicoparao Label(label-listagem),podemosdar
um IDparao VBox,aplicandoumestiloparaele:
123

## Página 134

6.2. Extraindoestilospraumarquivo.css CasadoCódigo
VBox vbox = new VBox(tableView);
vbox.setId( "vbox");
Emnossoarquivo application.css,podemosfazer:
#vbox {
-fx-padding: 70 0 0 10;
}
Ótimo,aoexecutarocódigovemosqueo paddingfoiaplicado.Noteo #
doseletor,paraidentificá-locomoum ID.
Podemos agora modificar um pouco o estilo doButtonde expor-
tarprodutoscomo CSV.Aprimeiramudan çapodeserextrairosmétodos
setLayoutsparaumestilo CSS.Ocódigoagoraestáassim:
Button button = new Button("Exportar CSV");
button.setLayoutX(575);
button.setLayoutY(25);
No lugar disso, removemos as chamadas aos dois métodos e adi-
cionamos o mesmo efeito noapplication.css, utilizando as pro-
priedades -fx-translate-xe -fx-translate-y:
.button {
-fx-translate-x: 575;
-fx-translate-y: 25;
}
Também podemos aplicar uma cor nesse botão, utilizando o
-fx-background-color.Umaformadefazerissoseria:
.button {
-fx-translate-x: 575;
-fx-translate-y: 25;
-fx-background-color: rgb(31, 149, 206);
-fx-text-fill: white;
}
Assim,o buttonficarácomoazulpadrãodo Java FX.Sepreferir,
vocêpodeaplicarqualqueroutracor. Omesmoparaosoutroselementos,
124

## Página 135

CasadoCódigo Capítulo6. CSSnoJavaFX
claro. Notequetambémutilizamosapropriedade -fx-text-fillpara
deixarotextobranco. Alémdesses,existemdiversasoutraspropriedades.
Aproveiteparaexploraro JavaFX CSSReferenceGuide duranteseustestes
paraconhecermaisalgumasdelas.
Outrodetalhebeminteressanteéque,damesmaformaquenoCSScon-
vencionaldenavegadores,tambémpodemosadicionarum :hoveremnos-
sosseletoresparadefiniroestiloparaomomentoemqueomouseestiver
soboelemento. Paraverissoemprática,vamosdizerquequeremosuma
transparênciamaiorno button,quandoestiverem hover:
.button:hover {
-fx-background-color: rgba(31, 149, 206, 0.71);
}
Atualizeeexecuteseucódigo.Vocêperceberáatransparênciaaopassar
ocursordomousesobobotão.
Fig.6.7:Buttoncomesemefeitodehover
Omesmopodeserfeitocomo Labelde progresso,queestáassim:
Label progresso = new Label();
progresso.setLayoutX(485);
progresso.setLayoutY(30);
Removemosessasduaslinhasedamosum IDparaessecampo:
Label progresso = new Label();
progresso.setId("label-progresso");
AgorabastaadicionaroestilonoarquivodeCSS:
125

## Página 136

6.2. Extraindoestilospraumarquivo.css CasadoCódigo
#label-progresso {
-fx-translate-x: 485;
-fx-translate-y: 30;
}
Explorando mais seletores e efeitos
Você pode utilizar diversas outras funções e efeitos, como um
linear-gradientnacordeseu buttonoufundodo scene.Eque
talumefeitodesombra?
.button {
-fx-background-color:
linear-gradient(#61a2b1, #2A5058);
-fx-effect : dropshadow(three-pass -box,
rgba(0,0,0,0.6), 5, 0.0, 0, 1);
}
Nãodeixedetestar.Vocêpodeveressesediversosoutrosefeitosno
tutorialdeJavaFXdaOracle:
https://docs.oracle.com/javase/8/javafx/get-started-tutorial
Quantidade de produtos e valor em estoque
Paradeixarnossalistagemumpoucomaiscompleta,vamosadicionarum
novo Labelcomovalortotalquetemosemestoqueetambémaquantidade
deprodutos. Criara labeljásabemos. Podemostambémadicionarum
identificadorúnico,comométodo setID,paraaplicarumestilononovo
elemento.Ocódigoficaráassim:
Label labelFooter = new Label("Texto vai aqui");
labelFooter .setId("label-footer");
No CSS, podemos alinhar alabel-footere também modificar o
tamanhodesuafonte,paraquetenhaumdestaquemaior.
#label-footer {
-fx-font-size: 15px;
126

## Página 137

CasadoCódigo Capítulo6. CSSnoJavaFX
-fx-translate-x: 210;
-fx-translate-y: 480;
}
Precisamosagoraadicionarotextoevaloresquedevemaparecernesse
Label.Vamosutilizarométodo formatdaclasse Stringmaisumavez,
paradeixaroresultadoformatadocomoaseguir:
Label labelFooter = new Label(
String.format("Você tem R$%.2f em estoque, " +
"com um total de %d produtos.", 100.00, 10));
labelFooter .setId("label-footer");
Dessaforma,oresultadoseráparecidocom:
Você tem R$100.00 em estoque, com um total de 10 produtos.
Para saber mais: S tring#format
Notequeutilizamos %.2fparaformatarumnúmerodepontoflu-
tuanteemduascasasdecimais,alémdo %dparaexibironúmeroin-
teiro.Existemdiversasoutrasop ções,como %spara Strings, %c
para charse %tparadatas. Sevocênãoestáfamiliarizadocomas
convençõesdoFormatterequiserconhecerumpoucomais,podedar
umaolhadaem:
https://docs.oracle.com/javase/7/docs/api/java/util/Formatter.html
Nãoqueremostrabalharcomumvalorfixo,comoacabamosdefazer.No
lugardisso,nosinteressarecuperarovalortotaldetodososprodutosdenossa
lista.Podemositerarnalistaacumulandotodososvaloresemumavariável
temporária:
double valorTotal = 0.0;
for (Produto produto: produtos) {
valorTotal += produto.getValor();
}
127

## Página 138

6.2. Extraindoestilospraumarquivo.css CasadoCódigo
Nãotemmuitosegredonessecódigo,usamoso +=paraincrementaro
valordecadaproduto.
Código mais declarativo com Jav a8
Nolugardeescreveressecódigoimperativo,ondedeclaramosuma
variávelintermediária(valorTotal)eincrementamosseuvalorem
um enhanced-for,quetalfazeressemesmotrabalhodeumaforma
maisdeclarativa,comumtoquedeprogramaç ãofuncionaldoJava8?
UtilizandoanovaAPIde Stream,ocódigoficariaassim:
double valorTotal = produtos.stream()
.mapToDouble(Produto::getValor ).sum();
SevocêestáutilizandoJava8,atualizeseucódigoparatestar.Oresul-
tadoseráomesmo.
Paraconcluir,podemosrecuperaraquantidadedeprodutosemestoque
utilizandoométodo sizedalistade produtos:
Label labelFooter = new Label(
String.format("Você tem R$%.2f em estoque, " +
"com um total de %d produtos.",
valorTotal , produtos.size()));
labelFooter .setId("label-footer");
Sóprecisamosadicionaro labelFooternaview,epronto:
group.getChildren().addAll(label,
vbox, button, progresso, labelFooter);
Perfeito,executeocódigoparaveroresultado!
128

## Página 139

CasadoCódigo Capítulo6. CSSnoJavaFX
Ocódigocompletodaclasse Mainficouassim:
package application;
import io.Exportador;
import java.io.IOException;
import javafx.application.Application;
import javafx.collections.ObservableList;
import javafx.concurrent.Task;
import javafx.geometry.Insets;
import javafx.scene.*;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.VBox;
129

## Página 140

6.2. Extraindoestilospraumarquivo.css CasadoCódigo
import javafx.scene.text.*;
import javafx.stage.Stage;
import br.com.casadocodigo.livraria.produtos.Produto;
import dao.ProdutoDAO;
@SuppressWarnings({ "unchecked", "rawtypes" })
public class Main extends Application {
@Override
public void start(Stage primaryStage) {
Group group = new Group();
Scene scene = new Scene( group, 690, 510);
scene.getStylesheets().add(getClass()
.getResource("application.css").toExternalForm());
ObservableList<Produto> produtos =
new ProdutoDAO ().lista();
TableView <Produto> tableView =
new TableView<>(produtos);
TableColumn nomeColumn = new TableColumn("Nome");
nomeColumn.setMinWidth(180);
nomeColumn.setCellValueFactory(
new PropertyValueFactory("nome"));
TableColumn descColumn = new TableColumn("Descrição");
descColumn.setMinWidth(230);
descColumn.setCellValueFactory(
new PropertyValueFactory("descricao"));
TableColumn valorColumn = new TableColumn("Valor");
valorColumn.setMinWidth(60);
valorColumn.setCellValueFactory(
new PropertyValueFactory("valor"));
TableColumn isbnColumn = new TableColumn("ISBN");
130

## Página 141

CasadoCódigo Capítulo6. CSSnoJavaFX
isbnColumn.setMinWidth(180);
isbnColumn.setCellValueFactory(
new PropertyValueFactory("isbn"));
tableView.getColumns().addAll(nomeColumn, descColumn,
valorColumn, isbnColumn);
final VBox vbox = new VBox(tableView);
vbox.setId( "vbox");
Label label = new Label("Listagem de Livros");
label.setId("label-listagem");
Label progresso = new Label();
progresso.setId("label-progresso");
Button button = new Button("Exportar CSV");
button.setOnAction(event -> {
Task<Void> task = new Task<Void>() {
@Override
protected Void call() throws Exception {
dormePorVinteSegundos();
exportaEmCSV(produtos);
return null;
}
};
task.setOnRunning(e -> progresso.setText(
"exportando..."));
task.setOnSucceeded(e -> progresso.setText(
"concluído!"));
new Thread(task).start();
});
double valorTotal = produtos.stream()
131

## Página 142

6.2. Extraindoestilospraumarquivo.css CasadoCódigo
.mapToDouble(Produto::getValor).sum();
Label labelFooter = new Label(
String.format("Você tem R$%.2f em estoque, " +
"com um total de %d produtos.",
valorTotal, produtos.size()));
labelFooter.setId("label-footer");
group.getChildren().addAll(label,
vbox, button, progresso, labelFooter);
primaryStage.setTitle(
"Sistema da livraria com Java FX");
primaryStage.setScene(scene);
primaryStage.show();
}
private void exportaEmCSV(ObservableList<Produto> produtos){
try {
new Exportador ().paraCSV(produtos);
} catch (IOException e) {
System.out.println("Erro ao exportar: "+ e);
}
}
private void dormePorVinteSegundos() {
try {
Thread.sleep(20000);
} catch (InterruptedException e) {
System.out.println("Ops, ocorreu um erro: "+ e);
}
}
public static void main(String[] args) {
launch(args);
}
}
132

## Página 143

CasadoCódigo Capítulo6. CSSnoJavaFX
Enossoarquivo application.css:
#label-listagem {
-fx-font-size: 30px;
-fx-padding: 20 0 10 10;
}
#label-progresso {
-fx-translate-x: 485;
-fx-translate-y: 30;
}
.table-view {
-fx-min-width: 665;
-fx-max-width: 665;
}
.table-column {
-fx-padding: 0 0 0 10;
}
#vbox {
-fx-padding: 70 0 0 10;
}
.button {
-fx-translate-x: 575;
-fx-translate-y: 25;
-fx-background-color: rgb(31, 149, 206);
-fx-text-fill: white;
}
.button:hover {
-fx-background-color: rgba(31, 149, 206, 0.71);
}
#label-footer {
-fx-font-size: 15px;
-fx-translate-x: 210;
133

## Página 144

6.2. Extraindoestilospraumarquivo.css CasadoCódigo
-fx-translate-y: 480;
}
Antesdeseguirparaospróximoscapítulos,vocêpodepersonalizarainda
maisasualistagem.Apliquenovosestilos,cores,fontes,efeitos.Useeabuse
dadocumentaçãoparaabsorveresseconteúdodeformaprática. Sequiser,
vocêpodecompartilharcomigoecomosdemaisleitoresoresultadofinaldo
projetocomassuasmelhorias.
134

## Página 145

Capítulo7
JAR,bibliotecasebuild
Queremos o quanto antes lançar nossa aplicação, distribuir nas diversas
livrariase standsdevenda.Porondepodemoscome çar?
Nestecapítulo,veremosnãosócomocompactaredistribuirnossaapli-
caçãofinal,mastambémcomogerareutilizarbibliotecasparalinguagem
Java.Alémdisso,veremosumaformainteressantedefazero buildegerenci-
amentodedependênciasdenossoprojeto,utilizando Maven,queéumadas
ferramentasmaisessenciaisdomercadodehojeemdia.
7 .1 JAR
Nãoqueremosmandartodasasnossasclassesearquivosdeconfigurações
soltosparaoclientefinal,issoseriaumabagun ça. Perderumdosarquivos
implicarianonãofuncionamentodaaplicação,porexemplo.Umaformabem

## Página 146

7.2. GerandoJARexecutávelpelaIDE CasadoCódigo
maisinteressanteseriacompactartudoemumúnicoarquivo,um ZIPcom
tudoqueousuárioprecisaparaexecutarnossocódigo.
Essetipode ZIPrecebenaverdadeaextensão JAR,de Java ARchive
(arquivo Java). Nele estarão presentes nosso código-fonte compilado (
bytecode),arquivosdeconfiguraçõesedependências.
Comocriarum JARexecutável?Issoébemsimples,vocêinclusivepode
fazercomqualquercompactador ZIPatualqueconhe ça. Veremosuma
formabempráticadefazerpelaprópriaIDE,emnossocasooEclipse.
JAR na linha de comando
Vocêtambémpodegerarum JARdiretamentepalalinhadeco-
mando,utilizandooprograma jarpresentenoJDK.Apesardeserum
poucomaistrabalhoso,vocêconseguegeraroseuexecutávelcomoco-
mando:
jar -cvf livraria.jar
src/application/*.java
src/db/*.java
src/io/*.java
src/repositorio/*.java;
7 .2 G erando JAR executável pela IDE
FazeroprocessopeloEclipse,ouqualqueroutraIDEmoderna,éverdadeira-
mentemaissimples.Parageraro JARexecutáveldenossaaplicaçãoJavaFX,
tudooqueprecisamosfazeréclicarcomobotãodireitonoprojeto,selecionar
Exporteemseguidaaop ção Runnable JAR File.
136

## Página 147

CasadoCódigo Capítulo7. JAR,bibliotecasebuild
Após selecioná-la, podemos escolher emLaunch configurationqual a
classe que deverá ser executada ao rodar esseJAR. Vamos escolher a
classe Main. Alémdisso,nocampo Export destination,precisamos
preencherolocalemqueoarquivoexecutávelJavadevesercriado,assim
comoseunomeeextensão(queserá .jar):
137

## Página 148

7.3. Executandoalivraria-fx.jar CasadoCódigo
Emmeucaso,ocaminhoficou /Users/turini/Desktop/livraria-fx.jar,
emoutraspalavras,oarquivosechamará livraria-fx.jareserácriado
emminhaáreadetrabalho.
Tudopronto,bastaclicarem Finish.Simples,nãoacha?Aproveitepara
geraro JARexecutávelemsuacasa,sigaessespassoseconfiraseoarquivo
livraria-fx.jarfoicriadonocaminhoquevocêdefiniu.
7 .3 E xecutando a livraria-fx.jar
Agoraquetemosoarquivocriado,podemostentarexecutá-loparaconferirse
tudocorreubem.Vamosfazerissopelalinhadecomando,utilizando java
138

## Página 149

CasadoCódigo Capítulo7. JAR,bibliotecasebuild
-jar SEU_EXECUTAVEL.Umexemploseria:
java -jar Desktop/livraria-fx.jar
Excelente,aappestáfuncionandoconformeesperado!
Noteque,aoclicarem Export CSV,oarquivo produtos.csvcoma
relaçãodetodososlivrosserácriadonaáreadetrabalho,mesmolocalonde
seencontrao JAR.
139

## Página 150

7.4. BibliotecasemJava CasadoCódigo
Para saber mais: JAR L auncher e outros
Vocêpodeutilizarprogramascomoo JARLauncher pararodaros
seusexecutáveisJavacomapenasumclick,semanecessidadededigi-
tarocomando java -jar noterminal.NoMacOS,porexemplo,esse
programajáveminstalado.Hádiversasoutrasop çõesparaosmaisdifer-
entessistemasoperacionais.
7 .4 B ibliotecas emJav a
Um JARnãoprecisanecessariamenteserumexecutável. Émuitocomum
criarmosum JARcomumconjuntodeclassesquepodemserreutilizados
emoutrosprojetos.Emoutraspalavras,criaruma bibliotecaJava.
Porsinal,ograndenúmerodebibliotecasgratuitasemJavaéumdosfa-
toresquefazemalinguagemsertãobemaceitanomercado. Precisagerar
140

## Página 151

CasadoCódigo Capítulo7. JAR,bibliotecasebuild
relatórios,manipular XMLs,conectaraobancodedados,gerarcódigosde
barrasetc.? Vocêjátemtudoissopronto! OecossistemadoJavaéenorme.
E,omelhor,grandeparte(talvezamaiorparte)dosprojetos(bibliotecas)em
Javaégratuitaetemseucódigoaberto,osconhecidos opensources.
ACaelum,empresaondetrabalho,possuidiversosprojetos opensource.
VRaptor, Mamutee Stellasãoalgunsdeles.Contribuircomprojetosde
códigoabertotemdiversosbenefícios,desdeoconhecimento,quevocêcom
certezavaiadquirirecompartilhar,atéoreconhecimentoedivulgaç ãodeseu
trabalho.Sevocêquiser,podeconheceralgunsdelesnorepositóriopúblico
daCaelum:
http://github.com/caelum/
7 .5 D ocumentando seu projeto com Jav adoc
Ésempremuitointeressantedocumentarassuasclassesquandovocêcria
umnovo JAR.Afinal,comoapessoaquevaiusá-losaberáquaisclassese
métodosestãodisponíveis?Outrasinformaçõescomoexce çõesqueocódigo
podelançaredetalhesimportantesdeseuusotambémsãodiferenciaissig-
nificantes.
OprópriocódigodoJavaétododocumentado,vocêpodeveradocu-
mentaçãocompletadesuaAPIpelositedaOracle:
http://download.java.net/jdk8/docs/api/index.html
141

## Página 152

7.5. DocumentandoseuprojetocomJavadoc CasadoCódigo
Vocêpode(edeve)usaro javadocparacriarumadocumentaçãoequiv-
alenteparaosseusprojetos. EsseprogramatambémjávemnaJDKepode
serusadodiretamentepelalinhadecomando,oucomajudadaIDE.Seainda
nãoconheceo javadoc,podegostardelermaisarespeitoem:
http://www.oracle.com/technetwork/articles/java/index-137868.html
Um exemplo prático de documentação em Java
ÉmuitosimplesdocumentarseusprojetosemJava,o javadoccuidade
boapartedotrabalhopesado.Mas,claro,ésempreinteressanteofereceralgu-
masinformaçõesparaenriqueceradocumentaçãodenossoprojeto.Fazemos
issonoprópriocódigo:
142

## Página 153

CasadoCódigo Capítulo7. JAR,bibliotecasebuild
/**
* Cuida do acesso aos dados da classe {@link Produto}.
*
* @author Rodrigo Turini <rodrigo.turini@caelum.com.br>
* @since 1.0
*/
public class ProdutoDAO {
/**
* Lista todos os produtos do banco de dados
*
* @return {@link ObservableList} com todos os produtos
* @throws RuntimeException em caso de erros
*/
public ObservableList<Produto> lista() {
// código omitido
}
/**
* @param produto que deverá ser adicionado no banco.
* @throws RuntimeException em caso de erros
*/
public void adiciona(Produto produto) {
// código omitido
}
}
Observequeissoéfeitocomumtipodeblocodecomentáriocomsignifi-
cadoespecial. Elesemprecome çacom /**eterminacom */,nasoutras
linhas,colocamosapenasum *.
Vocêpodeadicionarumadescriçãoparaasclassesemétodos,masprefira
nadamuitoextensoequecontedetalhesdeimplementaç ão. Porexemplo,
imaginequeno javadoceudigaqueestamospersistindoemumbancode
dadosMySQL.Oqueaconteceráseeumigrardebanco? Adocumentaç ão
ficarádesatualizadaoueuprecisareilembrar(oqueprovavelmentenãovai
acontecer).
Tambémpodemosdefiniroutrasinformaçõesnadocumentação,como
fizemoscomoautor,desdequandoaclasseexiste(since),parâmetros,retorno,
143

## Página 154

7.5. DocumentandoseuprojetocomJavadoc CasadoCódigo
exceptionsetc.Tudoissoéfeitodeformasimplescomasprópriasanotações
demarcaçãodo javadoc.
Depois de devidamente documentado, pelo Eclipse, podemos ir em
Projectedepoisescolheraop ção Generate Javadoc.
Fig.7.6:GerandojavadocpelainterfacedoEclipse.
Umanovajanelaaparecerá.Tudooqueprecisamosfazeréselecionaro
projetoquequeremosdocumentareodiretórioondeadocumentaç ãodeverá
sergerada. Vamoscolocardentrodeumapastachamada docdentrodo
próprioprojeto.
144

## Página 155

CasadoCódigo Capítulo7. JAR,bibliotecasebuild
Fig.7.7:Configurandooprojetoedestinodojavadoc.
Agorasóprecisamosclicarem Finishepronto,confiraqueapasta doc
foicriada:
Fig.7.8:Arquivoscriadospelojavadocnapastadoc.
145

## Página 156

7.6. AutomatizandobuildcomMaven CasadoCódigo
Abraoarquivo index.htmlemseunavegadorparaveroresultado,
vocêvaigostar.
7 .6 A utomatizando build com Maven
OEclipsefacilitoubastanteoprocessodegeraro JARexecutável,mascon-
formeaaplicaçãovaievoluindooprocessode buildpodesetornarmaiscom-
plexo. Énecessáriocompilaroprojeto,copiarsuasdependências,configu-
raçõesetc.Esseprocessotemqueserrepetidosempre.
Fazerissomanualmente,aindaquecomajudadaIDE,podesertantotra-
balhosoquantoproblemático.Acadaexecução,ohumanoqueestáfazendo
atarefapodeseesquecerdealgumdospassos,cometeralgumerroetc.
Qualasolução?Automatizartodoesseprocesso.Existemdiversasferra-
mentasde buildquenosauxiliamnessetrabalho,o Mavenéumadasmais
populares. Comeleeseusdiversosplugins,oprocessode buildegerencia-
mentodedependênciasdenossasaplicaçõesficambemsimplesesofisticados.
146

## Página 157

CasadoCódigo Capítulo7. JAR,bibliotecasebuild
Download e instalação do Maven
ParasabersevocêtemoMaveninstaladoemseusistemaoperacional,
bastaabriroterminaledigitarocomando mvn -version. Asaída
deveráserparecidacom:
Rodrigos-MacBook-Pro:~ turini$ mvn -version
Apache Maven 3.2.3 (...; 2014-08-11T17:58:10-03:00)
Maven home: /Applications/apache-maven-3.2.3
Java version: 1.8.0_25, vendor: Oracle Corporation
Java home: /Library/Java/.../jdk1.8.0_25.jdk/Contents/Home/jre
Default locale: en_US, platform encoding: UTF-8
OS name: "mac os x", version: "10.9.4", arch: "x86_64"
SevocêaindanãotemoMaveninstalado,podefazerseudownload
diretopeloseusite:
http://maven.apache.org/download.cgi
LávocêtambémencontrainstruçõesdeinstalaçãoparacadaSO.Se
encontrarqualquerdificuldadeparafazerisso,nãodeixedepostarno
GUJounosmandarume-mail.
7 .7 T ransformando nossa app em um projeto
Maven
Agoraquejátemostudobaixadoeconfigurado,podemosconverternossa
appparaumprojetoMaven. OEclipsetambémsimplificamuitoessetra-
balho,tudooqueprecisamosfazeréclicarcomobotãodireitonoprojetoe
selecionar:
• Configure
• ConverttoMavenProject
147

## Página 158

7.7. TransformandonossaappemumprojetoMaven CasadoCódigo
AjanelaCreatenewPOM deveaparecer.Nela,vamospreencherocampo
Group Id com br.com.casadocodigo,queéopacotepadrãodoprojeto,
o Artifact Id comonome livraria-fxemanterasoutrasop çõescom
ovalorpadrão.
148

## Página 159

CasadoCódigo Capítulo7. JAR,bibliotecasebuild
Clicamosem Finishepronto,umarquivochamado pom.xmlfoicri-
adoemnossoprojeto.
149

## Página 160

7.7. TransformandonossaappemumprojetoMaven CasadoCódigo
Essearquivopossuioseguinteconteúdo:
<project xmlns="http://maven.apache.org/POM/4.0.0"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
http://maven.apache.org/xsd/maven-4.0.0.xsd">
<modelVersion>4.0.0</modelVersion>
<groupId>br.com.casadocodigo</groupId>
<artifactId>livraria-fx</artifactId>
<version>0.0.1-SNAPSHOT</version>
<build>
<sourceDirectory>src</sourceDirectory>
<resources>
<resource>
<directory>src</directory>
<excludes>
<exclude>**/*.java</exclude>
150

## Página 161

CasadoCódigo Capítulo7. JAR,bibliotecasebuild
</excludes>
</resource>
</resources>
<plugins>
<plugin>
<artifactId>maven-compiler-plugin</artifactId>
<version>3.1</version>
<configuration>
<source>1.8</source>
<target>1.8</target>
</configuration>
</plugin>
</plugins>
</build>
</project>
Aoabriroarquivopelaprimeiravez,oEclipseprovavelmentemostrará
apenasapáginadeOverview.Paraveroconteúdodeste XML,vocêpodeclicar
naaba pom.xmlqueficavisívelnorodapédoeditor:
Nãosepreocupeementendercadadetalhedeste XMLdeconfiguração
agora,masnotequeelejátemalgumasinformaçõesessenciaisdenosso build.
NossaappagorajáéumprojetoMaven.Bemsimples,nãoacha?
7 .8 A dicionando as dependências com Maven
AgoraquejáestamostrabalhandocomMaven,podemosdeixarocontrole
dasbibliotecasquetemosemnossoprojetocomele. Eleseráoresponsável
pelogerenciamentodenossasdependências.
151

## Página 162

7.8. AdicionandoasdependênciascomMaven CasadoCódigo
Atualmentenossoprojetotemapenasduas: odriverdeconexãocom
MySQLeabasedoprojetodalivraria,ondeseencontraainterface Produto
esuasimplementações.
Paracomeçar,vamosremoveressesdoiselementosdenosso classpath.
Faremosissoclicandocomobotãodireitonoprojeto,op ção Build Path e
Configure Build Path.
Naaba Library,clicamosno mysql-connector-java.jareem
Remove.
Emseguida,faremosomesmocomoprojeto livraria-base,naaba
Project:
152

## Página 163

CasadoCódigo Capítulo7. JAR,bibliotecasebuild
Aoclicarem Ok,oprojetojádeveparardecompilar,afinalessasbibliote-
cassãonecessárias.Vamosagoraabriroarquivo pom.xmledeclararessas
duasdependênciaslá:
<!-- inicio do arquivo omitido -->
<dependencies>
<dependency>
<groupId>br.com.caelum.livraria</groupId>
<artifactId>livraria-base</artifactId>
<version>1.0.0-SNAPSHOT</version>
</dependency>
<dependency>
<groupId>mysql</groupId>
<artifactId>mysql-connector-java</artifactId>
<version>5.1.34</version>
</dependency>
</dependencies>
153

## Página 164

7.8. AdicionandoasdependênciascomMaven CasadoCódigo
</project>
Note que para fazer isso só precisamos adicionar umatag chamada
dependencies,eparacadadependênciaumanova tag dependencycom
aseguinteestrutura:
<dependency>
<groupId> VALOR_AQUI </groupId>
<artifactId> VALOR_AQUI </artifactId>
<version> VALOR_AQUI </version>
</dependency>
Adicionando pela interface doEclipse
Sepreferir,vocêtambémpodeadicionarnovasdependênciasemseu
projetodiretamentepelainterfacedoEclipse.Bastaclicarem Mavene
Add Dependency.
Dessaforma,vocênãoprecisaescrevernenhumalinhade XML,ele
faráessetrabalhoparavocê.
154

## Página 165

CasadoCódigo Capítulo7. JAR,bibliotecasebuild
Vamosversetudofuncionou?Bastaclicarcomobotãodiretonoprojeto,
Maveneescolher Update Project... (oupressionaroatalho Alt+ F5).
Feitoisso,aferramentafaráseutrabalhoeoprojetodevevoltaracom-
pilar.Notequeasdependênciasficamvisíveisem Maven Dependencies,
diretopelo package explorer:
155

## Página 166

7.8. AdicionandoasdependênciascomMaven CasadoCódigo
Buscando por dependências no Maven
Assimcomoo mysql-connector-java,vocêpodeencontrarqual-
queroutradependêncianecessáriapraseusprojetosnosite:
http://search.maven.org/
156

## Página 167

CasadoCódigo Capítulo7. JAR,bibliotecasebuild
Bastaclicarnaversãoquequerutilizarecopiara tagdadependênciapara
dentrodoarquivo pom.xmldeseuprojeto.
7 .9 E xecutando algumas tasks do Maven
VamosagoraverobuilddoMavenemprática?Naop ção Run As...,cli-
candocomobotãodireitonoprojeto,escolha Maven Build.
157

## Página 168

7.9. ExecutandoalgumastasksdoMaven CasadoCódigo
Adicionenocampo Goalsasopções:
• compilepackage
Essassãoalgumasdas taskspadrõesdoMaven.Comoopróprionomejá
diz,estamosdizendoquequeremoscompilareempacotar,gerarum JARdo
projeto.Sevocêquiser,podelermaissobreesses Goalsem:
158

## Página 169

CasadoCódigo Capítulo7. JAR,bibliotecasebuild
http://maven.apache.org/guides/introduction/
introduction-to-the-lifecycle.html
Aoexecutar,asaídaseráparecidacom:
[INFO] Scanning for projects...
[INFO]
...
[INFO] -----------------------------------------------
[INFO] Building livraria-fx 0.0.1-SNAPSHOT
[INFO] -----------------------------------------------
[INFO]
...
[INFO] Building jar: /Users/turini/Documents/workspace
/livraria-fx/target/livraria-fx-0.0.1-SNAPSHOT.jar
[INFO] -----------------------------------------------
[INFO] BUILD SUCCESS
[INFO] -----------------------------------------------
[INFO] Total time: 7.129 s
[INFO] Finished at: 2014-11-22T20:14:47-03:00
[INFO] Final Memory: 8M/94M
[INFO] -----------------------------------------------
Sucesso!Obuildfoiconcluídosemnenhumafalha.Notequeo JARfoi
criadodentrodeumapastachamada target,esseéodestinopadrãoda
ferramenta.
Masesse JARnãoéumexecutável! PrecisamosdeixarclaroaoMaven
queesseéumprojetoJavaFX.Comofazerisso?
7 .10 A dicionando plugin do Jav aFX
Comoumextra,ensinaremosaoMavencomogerarum JARexecutáveldo
JavaFX.Sódepensarparecetrabalhoso,nãoé?Masnaverdadeissotudojá
estápronto,existemdiversospluginsquenosauxiliamnessetrabalho.Uma
opçãobastanteutilizadaéo javafx-maven-plugin.
Damesmaformacomofizemosparaadicionarumadependência,pode-
mosabriroarquivo pom.xmleadicionarasseguinteslinhasdoplugin,logo
apóso maven-compiler-pluginquejáestádeclarado:
159

## Página 170

7.10. AdicionandoplugindoJavaFX CasadoCódigo
<plugins>
<!-- maven-compiler-plugin omitido -->
<plugin>
<groupId>com.zenjava</groupId>
<artifactId>javafx-maven-plugin</artifactId>
<version>8.1.2</version>
<configuration>
<mainClass>application.Main</mainClass>
</configuration>
</plugin>
</plugins>
Observequeestamosdefinindoqueaclasse application.Mainéa
classeprincipaldenossaaplicação. Alémdisso,precisamosadicionara tag
organizationcomoaseguir:
<organization>
<name>Casa do Código</name>
</organization>
Tudopronto! Jápodemosusarumadesuas tasks. Paragerarum JAR
executável,porexemplo,vocêpodeclicarem Run As..., Maven Build
eem Goalsadicionarovalor jfx:jar.
160

## Página 171

CasadoCódigo Capítulo7. JAR,bibliotecasebuild
Aoclicarem Run,oresultadoseráparecidocom:
[INFO] Scanning for projects...
...
[INFO] Building Java FX JAR for application
[INFO] Adding 'deploy' directory to Mojo
classpath: /Users/turini/Documents
/workspace/livraria-fx/src/main/deploy
[INFO] ---------------------------------------
[INFO] BUILD SUCCESS
[INFO] ---------------------------------------
[INFO] Total time: 6.793 s
[INFO] Finished at: 2014-11-22T20:36:10-03:00
[INFO] Final Memory: 9M/93M
[INFO] ---------------------------------------
Notequeoarquivo JARfoigeradodentrodapasta target,nosubdi-
retório jfx/app:
161

## Página 172

7.10. AdicionandoplugindoJavaFX CasadoCódigo
Sequiser,testeparaverificarqueelefoicriadocorretamente. Paraisso,
bastadigitarocomando:
java -jar target/jfx/app/livraria-fx-0.0.1-SNAPSHOT-jfx.jar
Perfeito,tudoestáfuncionando.Masissofoiumpoucotrabalhoso,não
acha?Paranossasorte,oplugindeJavaFXjátemuma taskquecriaeexecuta
o JARdenossaaplicaçãoautomaticamente!Parautilizá-la,cliquenovamente
em Run As..., Maven Build....Nocampo Goalsadicione jfx:run:
162

## Página 173

CasadoCódigo Capítulo7. JAR,bibliotecasebuild
Agorabastaclicarem Runeaappseráexecutadaapartirdo JARcriado
peloplugin.
Conhecendo mais alguns plugins
AlémdoplugindeJavaFXqueutilizamos,existemmaiscentenasde
pluginsquefacilitambastanteonossotrabalho.Vocêpodeverumalista
comalgunsdospluginsexistentesem:
http://maven.apache.org/plugins/index.html
7 .11 M aven na linha de comando
VimosqueépossívelexecutarasmetasdoMavendiretamentepeloEclipse,
mascomumenteessetrabalhoéfeitodiretamentepelalinhadecomando.Se
vocêquisertestar,bastaabrirapastadoseuprojetopeloterminaleexecutar
ainstrução mvncomasmetasquevocêquiser.Porexemplo:
mvn jfx:run
163

## Página 174

7.11. Mavennalinhadecomando CasadoCódigo
Notequeoresultadoseráomesmo,um JARexecutáveldenossaappserá
criadoeexecutado. Vocêpodeexecutarumasériedecomandosdeumasó
vez,bastasepará-losporumespaço,comoaseguir:
mvn clean jfx:run
Aprimeirametaexecutada,o clean,éutilizadaparalimparosarquivos
ediretóriosgeradospeloMavennapasta target.Essecomando,portanto,
limpaapasta targetelogoemseguidaexecutao jfx:runresponsável
porgerareexecutaro JARdoprojeto.
AlgumasdasmetasmaiscomunsdoMavensão:
•compile compilaocódigo-fontedoprojeto
•test compilaeexecutaseustestesdeunidadeexistentesnoprojeto
•package empacota(gerao JAR,porexemplo)docódigocompilado
deseuprojeto
•validate validaseoprojetotemtodasasinformaçõesnecessárias
paraseufuncionamento
•install instalalocalmenteseuprojeto
Sevocêestiverinteressado,podeconhecerumpoucomaissobreaspos-
sibilidadesdoMavenem:
http://maven.apache.org/general.html
164

## Página 175

CasadoCódigo Capítulo7. JAR,bibliotecasebuild
Outra opção: ANT e Ivy
Outraopçãobastanteconhecidaeutilizadanomercadoéo Ant,tam-
bémdaApache.Elecuidaapenasdoprocessodebuild.Paraogerencia-
mentodedependênciasvocêpodecontarcomoutroframeworkbastante
conhecido,o Ivy.Essesdoistrabalhambemjuntosetêmsuasvantagens
edesvantagens,assimcomoqualqueroutraferramenta.Háquemprefira
usá-losnolugardoMaven.Interessadoemsabermaissobre AnteIvy?
Adocumentaçãodelespodeajudarbastante,elasestãodisponíveisnos
links:
•http://ant.apache.org/manual/index.html
•http://ant.apache.org/ivy/
7 .12 C omo ficou nosso pom.xml
Apósasalterações,nossoarquivo pom.xmlficouassim:
<project xmlns="http://maven.apache.org/POM/4.0.0"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
http://maven.apache.org/xsd/maven-4.0.0.xsd">
<modelVersion>4.0.0</modelVersion>
<groupId>livraria-fx</groupId>
<artifactId>livraria-fx</artifactId>
<version>0.0.1-SNAPSHOT</version>
<organization>
<name>Casa do Código</name>
</organization>
<build>
<sourceDirectory>src</sourceDirectory>
165

## Página 176

7.12. Comoficounossopom.xml CasadoCódigo
<resources>
<resource>
<directory>src</directory>
<excludes>
<exclude>**/*.java</exclude>
</excludes>
</resource>
</resources>
<plugins>
<plugin>
<artifactId>maven-compiler-plugin</artifactId>
<version>3.1</version>
<configuration>
<source>1.8</source>
<target>1.8</target>
</configuration>
</plugin>
<plugin>
<groupId>com.zenjava</groupId>
<artifactId>javafx-maven-plugin</artifactId>
<version>8.1.2</version>
<configuration>
<mainClass>application.Main</mainClass>
</configuration>
</plugin>
</plugins>
</build>
<reporting>
<plugins>
<plugin>
<groupId>org.apache.maven.plugins</groupId>
<artifactId>maven-plugin-plugin</artifactId>
<version>3.2</version>
</plugin>
</plugins>
</reporting>
<dependencies>
<dependency>
<groupId>br.com.caelum.livraria</groupId>
166

## Página 177

CasadoCódigo Capítulo7. JAR,bibliotecasebuild
<artifactId>livraria-base</artifactId>
<version>1.0.0-SNAPSHOT</version>
</dependency>
<dependency>
<groupId>mysql</groupId>
<artifactId>mysql-connector-java</artifactId>
<version>5.1.34</version>
</dependency>
</dependencies>
</project>
Énaturalnãoreagirtãobemaoverumarquivo xmlcomtantasin-
formações,masapósusaraferramentaporalgunsinstantesvocêlogodeve
perceberquenãoénadadetãocomplicado. Atualizarsuasdependências
nuncafoitãofácil,alémdequepodemosfazero buildcompletodenossa
aplicaçãocomapenasumcomando.
167

## Página 179

Capítulo8
Refatorações
“Refatoraçãoéumatécnicacontroladaparareestruturarumtrechodecódigo
existente,alterandosuaestruturainternasemmodificarseucomportamento
externo.Consisteemumasériedepequenastransformaçõesquepreservamo
comportamentoinicial.Cadatransforma ção(chamadaderefatoração)reflete
emumapequenamudan ça,masumasequênciadetransformaçõespode
produzirumasignificantereestrutura ção.Comocadarefatoraçãoépequena,é
menosprovávelqueseintroduzaumerro.Alémdisso,osistemacontinuaem
plenofuncionamentodepoisdecadapequenarefatora ção,reduzindoas
chancesdeosistemaserseriamentedanificadoduranteareestrutura ção.
–Martin Fowler
Essaideiadeutilizarpequenastransformaçõesparamelhoraraqualidade
donossocódigorecebeonomede babysteps (passosdebebê). Essaéuma
práticafundamental,utilizadaparamelhoraralegibilidade,clarezaedesign

## Página 180

8.1. Refatoração CasadoCódigo
denossocódigo. Semprequeforfazerumarefatoraç ão,evitemudartudo
deumasóvez. Casoalgumerroapare ça,serámuitomaisdifícilidentificar
qualdasmudan çasfoiaresponsávelpeloerro(ou bug,comonormalmente
chamamos).
Nestecapítulo,vamosfazerpequenasrefatoraçõesemnossocódigo,bus-
candomelhoraralegibilidade,evitarrepetiçõese,comisso,aumentaraqual-
idadeemanutenibilidadedenossoprojeto.Alémdisso,relembraremosalgu-
masdasboaspráticase designpatternsquevimosaodecorrerdolivro.Pronto
paracomeçar?
8.1 R efatoração
Logoquecome çamosatrabalharcomatabelade Produtos,vocêdeveter
percebidoqueoEclipsemostrouvários warnings. Inclusive,usamosaano-
tação @SuppressWarningsparasilenciaressesalertas,masporqueeles
estãoacontecendo?
Olhandocomcuidadoparaamensagem,temosainformaç ão:
TableColumn is a raw type. References to generic
type TableColumn<S,T> should be parameterized
Emoutraspalavras,nãoestamosinformandoosparâmetrosgenéricosda
classe TableColumn.Idealmente,nolugardefazer:
TableColumn nomeColumn = new TableColumn("Nome");
nomeColumn.setMinWidth(180);
nomeColumn.setCellValueFactory(
new PropertyValueFactory("nome"));
170

## Página 181

CasadoCódigo Capítulo8. Refatorações
Serianecessáriofazerassim:
TableColumn<Produto, String> nomeColumn =
new TableColumn<Produto, String>("Nome");
nomeColumn.setMinWidth(180);
nomeColumn.setCellValueFactory(
new PropertyValueFactory<Produto, String>("nome"));
Vejaqueagoraestamosdefinindoaclasse TableColumnpassandoo
Produto,queéotipodoobjetoqueestásendomanipulado,maisa String,
queéotipodoconteúdonocampodatabela. Masocódigoficoumuito
maisverboso,nãoacha? Porisso,desdeoiníciooptamospornãopassaro
parâmetrogenérico,apesardascentenasde warnings.
Outroproblemanessapartedocódigoestánaquantidadederepetições.
Observequegrandepartedocódigoestáidêntico,paracadacoluna:
TableView<Produto> tableView = new TableView <>(produtos);
TableColumn nomeColumn = new TableColumn("Nome");
nomeColumn.setMinWidth(180);
nomeColumn.setCellValueFactory(
new PropertyValueFactory("nome"));
TableColumn descColumn = new TableColumn("Descrição");
descColumn.setMinWidth(230);
descColumn.setCellValueFactory(
new PropertyValueFactory("descricao"));
TableColumn valorColumn = new TableColumn("Valor");
valorColumn .setMinWidth(60);
valorColumn .setCellValueFactory(
new PropertyValueFactory("valor"));
TableColumn isbnColumn = new TableColumn("ISBN");
isbnColumn.setMinWidth(180);
isbnColumn.setCellValueFactory(
new PropertyValueFactory("isbn"));
171

## Página 182

8.1. Refatoração CasadoCódigo
tableView.getColumns().addAll(nomeColumn, descColumn,
valorColumn, isbnColumn);
Seguindoasboaspráticasdaorientaçãoaobjetos,devemosisolarcom-
portamentosrepetidosemmétodos.Oganhovaidesdeareutilizaç ão,jáque
elepoderáserchamadováriasvezesemnossocódigo,atéemlegibilidade,já
quepodemoslhedarumnomebastantesignificativo.
Vamos fazer essa pequena refatoração em nosso código. O método
poderáficarassim:
private TableColumn criaColuna(String titulo,
int largura, String atributo) {
TableColumn column = new TableColumn(titulo);
column.setMinWidth(largura);
column.setCellValueFactory(
new PropertyValueFactory(atributo));
return column;
}
172

## Página 183

CasadoCódigo Capítulo8. Refatorações
Usando Extract Method do Eclipse
Experimenteselecionarotrechodecódigoquevocêquerextraire
pressionarasteclasdeatalho Control+ Shift+ M.
Bastadigitaronomedométodoquevocêquercriarepronto!
Apesardesimples,essapequenamudan çajádáumacarabemmelhor
paranossocódigo.Eleficouassim:
TableView<Produto> tableView = new TableView <>(produtos);
TableColumn nomeColumn = criaColuna("Nome", 180, "nome");
TableColumn descColumn =
criaColuna ("Descrição", 230, "descricao");
TableColumn valorColumn = criaColuna("Valor", 60, "valor");
TableColumn isbnColumn = criaColuna("ISBN", 180, "isbn");
173

## Página 184

8.1. Refatoração CasadoCódigo
tableView.getColumns().addAll(nomeColumn, descColumn,
valorColumn, isbnColumn);
Alémdisso,agoraqueeleestáisolado,podemosatéadicionarosparâmet-
rosgenéricossemsentirtantoocustodelegibilidade.Ométodoficaráassim:
private TableColumn<Produto, String> criaColuna(String titulo,
int largura, String atributo) {
TableColumn<Produto, String> column =
new TableColumn<Produto, String>(titulo);
column.setMinWidth(largura);
column.setCellValueFactory(
new PropertyValueFactory<Produto, String>(atributo));
return column;
}
Outras formas de refatoração
Aextraçãodemétodoséapenasumdosmuitostiposderefatorações.
Renomearvariáveis,classesemétodostambémfazbastantediferen çaem
nossocódigo,quantomaisclaroforonome,maisfácilseráentenderoal-
goritmo.Extrairvariáveiséumoutrotipobastantecomumerecomendado.
OEclipseajudabastantenessetrabalho,háumadiversidadebemgrande
deatalhospararefatoração. Aprincípio,vocênãoprecisadecorarcadaum
dessesatalhos,bastaselembrardo Alt+ Shift+ T.Elemostraaspossíveis
refatoraçõesparaumdeterminadotrechodecódigo.Porexemplo,aousá-lo
emumaclasse:
174

## Página 185

CasadoCódigo Capítulo8. Refatorações
Observequealgumasdassugestõessão:renomearaclasse,moverpara
outropacote,extrairumainterface,entrediversasoutras.
Desafio: mais e mais refatorações
Asmudan çasquefizemosaquisãobastantesimples,meuobjetivofoi
mostraroquantoissopodesignificaremnossocódigo.Daquiparafrenteé
comvocê.Queoutrastransformaçõespoderiammelhoraresseprojeto?Passe
umtempopesquisandoarespeito,comtodacertezavaivalerapena. Vale
lembrarqueexistemrefatoraçõesbemmaiscomplexas,queafetamdiversas
partesdenossaaplicaçãoeatémesmoasuaarquitetura.
8.2 O s tão populares Design Patterns
Nãoéàtoaqueelessãopopulares,valemuitoapenaentendereaplicaresses
conceitossemprequeforpossívelemnossosprojetos.Eisso não muda de-
pendendo da linguagem ou tecnologia que você estiver utilizando,oque
tornaaideiaaindamaisinteressante.
DesignPatternséumassuntomuitoextenso,precisaríamosdepelomenos
175

## Página 186

8.2. OstãopopularesDesignPatterns CasadoCódigo
maisumas200páginaspranosaprofundarnisso.Masmesmoassimeutentei
mostraraquialgunsdosmaisfundamentaisparanossodiaadiadesenvol-
vendoemJava.Relembrandoalgunsdeles:
•Factory Method: vocênãoquerdeixarocódigodecriaç ãodeum
objetocomplicadoespalhadoporaí. Podemosestarfalandodeuma
ConnectiondoJDBC,comovimosnoexemplopassado,ouqualquer
outro.Elenãoselimitaaumatecnologiaespecífica.Nossocódigoficou
assim:
public class ConnectionFactory {
public Connection getConnection() {
String url = "jdbc:mysql://localhost/livraria";
try {
return DriverManager.getConnection(url, "root", "");
} catch (SQLException e) {
throw new RuntimeException(e);
}
}
}
Quaisasvantagens? Estamos encapsulandoesseprocessocompli-
cadoqueécriarumaconexão. Alémdisso,concentramosnossasin-
formaçõesdelogin,senhaenomedobancodedadosemumúnico
objeto. Sealgumadessasinformaçõesmudar,eusóprecisoatualizar
essaclasse, um único ponto da minha aplicaçãoenãooszilharesde
lugaresqueacessamnossobanco.
•DAO:aideiadesse patternécriarumacamadaespecialistaemacessar
dadosdenossosobjetos. NãoimportaseeleestáusandoJDBC,Hi-
bernateouqualqueroutratecnologia.AsregrasdoMySQL,Oracleou
qualqueroutrobancodedadosficamencapsuladas.Noteque encapsu-
lamentoéumdospilaresdequasetodosos designpatterns.Nolugar
desairacessandoobancodedadosdiretamentepelasnossasclasses,
passamossemprepelacamadado DAO:
176

## Página 187

CasadoCódigo Capítulo8. Refatorações
Fig.8.4:AcessoadadosencapsuladoemumDAO.
•T emplate Method:apesardenãoimplementarmosesse patterndire-
tamenteemnossocódigo,vimoseleempráticanaAPIdeIOdoJava.
InputStreamilustraesseexemplo,nofluxodeentrada. Ofluxoéo
mesmo,independentedeondevamoslerosbytes:
Fig.8.5:MétodorecebendoumInputStreamcomoparâmetro.
Essessãoapenasalgunsdosmuitosquevocêprovavelmentevaiusarem
seudiaadia.Mesmoquenãosaiba,muitasvezesissoacontece.
177

## Página 189

Capítulo9
PróximospassoscomJava
Éisso,esperoquetenhaaproveitadobastanteoconteúdo.Foiumalongajor-
nada,queparavocêtalveztenhacome çadonolivro DesbravandoJavaeOri-
entaçãoaObjetos. Nosdoislivrostenteiapresentartodososconceitoscom
exemplosmãonamassaecomumfocomaisprático.
Nãopareporaqui,continuepraticando!Tentesempreiralémcomnovos
testesecenáriosalémdosaquipropostos.Paramim,apráticaéaformamais
efetivadeaprenderefixarqualquercoisa.
Apartirdaqui,vocêpodedescobrirasmuitasoutrasfuncionalidadesda
linguagem,assimcomosuasmilharesdebibliotecas,explorarnovasAPIsetc.
HámuitomaisoqueexplorarnoecossistemadaplataformaJava.

## Página 190

9.1. Entreemcontatoconosco CasadoCódigo
9.1 E ntre em contato conosco
Nãoseesque çadequevocêpodeencaminharsuasdúvidasnalistaquefoi
criadaespecialmenteparaestelivro.Nãosódúvidas!Assugestões,críticas,
ideiasemelhoriastambémsãoessenciaisparanós:
https://groups.google.com/group/livro-java
180