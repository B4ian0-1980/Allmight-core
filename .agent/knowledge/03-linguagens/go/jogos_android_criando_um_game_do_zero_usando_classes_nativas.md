---json
{
  "id": "jogos_android_criando_um_game_do_zero_usando_classes_nativas",
  "title": "Jogos Android Criando um game do zero usando classes nativas",
  "categoria": "03-linguagens",
  "subcategoria": "go",
  "resumo": "**Arquivo Original:** `Jogos Android Criando um game do zero usando classes nativas.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "android",
    "classes",
    "criando",
    "game",
    "jogos",
    "linguagens",
    "nativas",
    "usando"
  ],
  "perguntas_tipo": [
    "Como utilizar Jogos Android Criando um game do zero usando classes nativas?",
    "Quais as boas praticas de go?"
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
  "dono": "stack-go",
  "prioridade": 2
}
---

# Jogos Android Criando um game do zero usando classes nativas

> **Arquivo Original:** `Jogos Android Criando um game do zero usando classes nativas.pdf`
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
1 Sobre o autor 1
2 Por que um jogo mobile? 3
3 Come çando o Jumper 5
3.1 Criandooprojetoeatelaprincipal . . . . . . . . . . . . . . . 5
3.2 CriandooloopprincipaldoJumper . . . . . . . . . . . . . . 11
3.3 ComodesenharelementosnoSurfaceView? . . . . . . . . . . 13
3.4 CriandonossoprimeiroelementodoJumper:aclassePassaro 15
3.5 Criandoocomportamentopadrãodopássaro:ométodocai 20
4 Colocando uma imagem de fundo 21
4.1 Implementandoocontroledojogador:opulodopássaro . . 29
5 Criando o cano inferior 31
5.1 Movimentandoocano . . . . . . . . . . . . . . . . . . . . . . 37
6 Criando vários canos 39
6.1 Criandooslimitesparapulo:ochãoeteto . . . . . . . . . . . 44
7 Criando os canos superiores 47
7.1 Criandoinfinitoscanos . . . . . . . . . . . . . . . . . . . . . . 51
7.2 Descartandocanosanteriores . . . . . . . . . . . . . . . . . . 53
8 Criando a pontuaç ão do jogo 57
i

## Página 4

Sumário CasadoCódigo
9 Tratando colisões 69
9.1 Criandoateladegameover . . . . . . . . . . . . . . . . . . . 72
9.2 Centralizandoumtextohorizontalmentenatela . . . . . . . 75
10 Aprimorando o layout do jogo 79
10.1 Substituindoosretângulosporbitmaps . . . . . . . . . . . . . 82
11 Adicionando som ao jogo 87
ii

## Página 5

Capítulo1
Sobreoautor
Desdeomomentoemqueescreviminhaprimeiralinhadecódigoemum
projetinhoAndroiddeestudosmesenticompletamenteempolgadocomas
diversaspossibilidadesdeaplicaçõesquepoderiadesenvolvereresolvimer-
gulharnessemundoeaprendertudooquepudessesobreesseuniverso.
Naquelemomento,cursavameuúltimoanodagraduaç ãonoIME-USP
eestavapesquisandooquefarianomeuprojetodeconclusãodecurso.Não
tivedúvidas:queriafazeralgocomAndroid,poisteriaumachanceparame
dedicaraaprendê-loafundo.Nofimdascontas,acabamosfazendoemdu-
plaumotimizadorderotas,ondetivemeuprimeirocontatocomalgumas
tecnologiasdoAndroid,comooatual Google Cloud Messaging.
Aotérminodagraduação,sentianecessidadedeparticipardealgumpro-
jeto open source,porémqueriaalgonoqualeurealmentepudessefazerdife-
rençaequefossedivertidotambém,entãocomeceiapesquisarcomodeveria

## Página 6

CasadoCódigo
fazerparaparticipardocódigo-fontedoAndroid.Algumasnoitesmaldor-
midas(egigabytesdedownload)depoisejátinhatudoconfiguradoparao
meuprimeiro commitno Android Open Source Project.
Paralelamenteaisso,liaalgunstextossobredesenvolvimentodejogose
resolvientrarnessaárea,porémmuitomaterialqueviaerafocadonousode
algum framework,demodoqueatémesmoaquelejogomaissimplespreci-
savadeumcaminhãodeAPIparaserdesenvolvido.Nestemomento,resolvi
tentarfazerjogossimplesgraficamente,semousodeframeworks,etivebas-
tanteêxito,rendendoumconviteparapalestrarnoConexãoJavaeumjogo
publicadonoGooglePlaycommaisde100mildownloads.
AtualmentesoudesenvolvedoreinstrutornaCaelumapaixonadopelo
mundo mobile,dedicoumtempoajudandoadesenvolverocódigo-fontedo
Androidemuitodoqueaprendiduranteessesanosdeestudoestácomparti-
lhadonestelivro.
2

## Página 7

Capítulo2
Porqueumjogomobile?
Somenteemumano,dentrodaindústriadejogosmobiles,temosfatura-
mentoemdólarescomo:
• OjogoClash of Clansrecebeu800milhões.
• AsagaCandy Crushfaturou300milhões.
• AsérieAngry Birdsganhou195milhões.
Avendade smartphonese tabletsvemaumentandocadavezmais,tor-
nandoseususuáriosumgrandepúbliconãosóparaaplicativosmastambém
parajogos.MuitasdasgrandesdesenvolvedorasdegamescomoEA,Game-
lofteUbisoftjáperceberamissoecontamcomdivisõesinteirasdestinadas
somenteaodesenvolvimentodegamesparaplataformasmóveis.

## Página 8

CasadoCódigo
Nãohácomoignorarotamanhodessemercado.Disponibilizar,ounão,
umaversão mobiledeumjogoéadiferen çaentreestarnestemercadobilio-
nárioouficardefora.
Como este livro está organizado?
Estelivroestáorganizadoemcapítulosfocadosnaprogramaç ãodosdi-
versoselementosdonossojogoe,principalmente,nateoriaportrásdocó-
digo. Dessaforma,emvezdesimplesmentereplicarmosocódigoapresen-
tado,entenderemosoquesepassaeteremoscondiçõesdecriarmosnossos
própriosjogos!
Como será o nosso jogo?
Umjogoquesedestacoubastanteeganhounotoriedadenamídiafoio
FlappyBird,criadoemapenastrêsdiaspelovietnamitaDongNguyen,que
chegouafaturar120milreaispordiacomanúncios. ComooFlappyBird
apresentaosprincipaiselementosdeumjogo(eébemdivertido),vamoscriar
anossaversãodessegame:oJumper!
Agoraquetemosumaideiadojogoquefaremos,umadúvidaqueapa-
receé:oquevamosusarparacriarnossogame?Umarápidabuscanainternet
pelotema“ferramentasparajogosAndroid”poderevelarinúmerasalterna-
tivasenosdeixarconfusos: seráquedevemosusarlibGDXouUnitycom
Chipmunk?SeráqueoCocos2Dnãoseriamelhor?
Aperguntaquedevemosfazeré: sempreteremosqueusaralgumfra-
meworkparadesenvolvimentodejogos?Muitasvezes,não.
Osframeworkspodemnosajudaremváriosaspectosdodesenvolvi-
mentodeumjogo,porém,paramuitosjogoselesnãosãonecessários. No
nossoJumper,nãoutilizaremosnenhumaferramentaespecíficaparajogos,
apenasasfuncionalidadesqueaAPIdoAndroidnosoferece!Dessaforma,
podemosaprenderosconceitosportrásdeumjogoeentenderasvantagens
edesvantagensdeutilizarumframework.
4

## Página 9

Capítulo3
ComeçandooJumper
3.1 C riando o projeto e a tela principal
ComooJumperéumjogoparaAndroid,vamoscriarumnovoprojetono
AndroidStudio.Paraisso,vamosa File -> New Project epreenchere-
mososcampos Application Namee Company Domain:

## Página 10

3.1. Criandooprojetoeatelaprincipal CasadoCódigo
Fig.3.1:TeladecriaçãodoprojetonoAndroidStudio.
Nonossojogo,teremosuma Viewcomumpássaro,canoseum back-
groundcomnuvens.ComooAndroidnãoapossuiporpadrão,vamospreci-
sarcriarnossaprópria Viewcustomizada.
Paraimplementá-la, podemoscriarumaclassefilhade Viewoude
SurfaceView.Adiferen çaentreelaséque,enquantoa Viewfaztodosos
desenhosnaUIThread,aSurfaceViewdisponibilizauma threadparaque
possamosfazeroperaçõesmaispesadasemsegundoplanosemcomprometer
ausabilidadedaaplicação.Comonossojogoteráelementosdispostosnatela
emposiçõescalculadas,teremosqueutilizaruma SurfaceView.
Paracriarnossoprópriocomponentede View,vamoscriarumaclasse
chamada Game no pacote br.com.casadocodigo.jumper.engine,
herdarde SurfaceVieweimplementarseuconstrutor:
public class Game extends SurfaceView {
public Game(Context context) {
super(context);
}
}
Agoraquetemosnossa View, precisaremosvinculá-laauma Activity.
Quandocriamosnossoprojeto,opróprioassistentejácriouuma Activity
chamada MainActivityeum layoutchamado activity::main.xml.
Vamos alterar esse layout para conter apenas um “espaço vazio” (um
FrameLayoutcomoid container),noqualcolocaremosnossa Viewcus-
tomizada:
6

## Página 11

CasadoCódigo Capítulo3. ComeçandooJumper
<FrameLayout xmlns:android=
"http://schemas.android.com/apk/res/android"
android:id="@+id/container"
android:layout_width="match_parent"
android:layout_height="match_parent" />
Paraadicionaro SurfaceViewao FrameLayout,precisaremosins-
tanciarnossaclasse Gameechamarométodo addView.Issoseráfeitono
onCreatedanossa MainActivity:
protected void onCreate(Bundle savedInstance) {
super.onCreate(savedInstance);
setContentView(R.layout.activity_main);
FrameLayout container =
(FrameLayout) findViewById(R.id.container);
Game game = new Game(this);
container.addView(game);
}
Comonossa SurfaceViewnãofaznada,aorodarojogoseráexibida
umatelapretaeabarrasuperior,contendoonomedanossaaplicaç ão:
7

## Página 12

3.1. Criandooprojetoeatelaprincipal CasadoCódigo
Fig.3.2:NossaSurfaceViewatéomomento.
Umadecisãoimportantequetemosquetomaraocriarumjogodizres-
peitoàorientaçãodatela:devemosdeixá-lanaposiçãovertical(portrait )ou
8

## Página 13

CasadoCódigo Capítulo3. ComeçandooJumper
horizontal(landscape)?Muitosjogosprecisamdeespaçohorizontalparaexi-
birelementosgráficoscomoplacar,vidas,inimigos. Jáoutrosnãotêmessa
necessidadeeoptampelaorientaçãovertical.NocasodoJumper,vamosfixar
aorientaçãonavertical(portrait ).
No AndroidManifest.xmltemosoregistrodetodasasactivitiesda
nossaaplicação.Nonossocaso,comotemosapenasa MainActivity,po-
demosvê-laregistradanatag <activity>.Comoqueremosfixarsuaori-
entação,podemosutilizarapropriedade android:screenOrientation
edefini-lacomo portrait:
<activity
android:name="br.com.casadocodigo.jumper.MainActivity"
android:label="@string/app_name"
android:screenOrientation="portrait">
Seria interessante removermos a barra superior da nossa aplicação
paraquenossojogopossaserexibidoem fullscreen. Porpadrão, natag
<application>,no AndroidManifest.xml,oAndroiddefineumícone,
onomedaaplicaçãoeumtemaquecontémabarrasuperior:
<application
android:icon="@drawable/ic_launcher"
android:label="@string/app_name"
android:theme="@style/AppTheme">
Paradeixarnossojogoem fullscreenteremosquealteraressetemapara:
android:theme="@android:style/Theme.NoTitleBar.Fullscreen"
Comisso,eleseráexibidoem fullscreeneemmodo portrait!
9

## Página 14

3.1. Criandooprojetoeatelaprincipal CasadoCódigo
Fig.3.3:SurfaceViewemtelacheia.
Atéomomento,nãotemosumjogodosmaisdesafiadores.Aseguir,va-
moscriaroselementosdoJumperparadeixá-lomaisemocionante!
10

## Página 15

CasadoCódigo Capítulo3. ComeçandooJumper
3.2 C riando o loop principal doJumper
Umjogoécompostoporváriosquadros(ou frames),sendoquecadaframe
representaumaconfiguraçãodosseuselementosnaquelemomentoespecí-
fico. Porém,paradarano çãodemovimentoeanimaç ão,emumsegundo
muitosdessesframesdevemserexibidos.Amaioriadosjogostrabalhacom
umaquantidadede60FPS(framesporsegundo).
Paracriarmosessesframes,precisaremosdeumaestruturaquefiquero-
dandoenquantoojogoestiversendoutilizado.Essaestruturaéchamadade
loopprincipaldojogo. Nesse loopfaremososdesenhosdoselementosdo
nossojogo,atualizaremosapontuaç ãodojogador,verificaremossehouve
colisão,enfim,gerenciaremostodososaspectosdinâmicosdoJumper.
Comonossaclasse Gameéum SurfaceView,podemosutilizaruma
threadseparadaparaonossoloopprincipal.Naclasse Gamevamosimple-
mentarainterface Runnable:
public class Game extends SurfaceView implements Runnable {
@Override
public void run(){
// Aqui vamos implementar o loop principal do nosso jogo!
}
}
Enquantoousuárionãosairdojogo,vamosdeixarolooprodando.Para
isso,vamoscriarumavariável booleanqueindicaseojogodeverodarounão:
public class Game extends SurfaceView implements Runnable {
private boolean isRunning = true;
@Override
public void run() {
while(isRunning) {
//Neste loop vamos gerenciar os elementos do Jumper.
}
}
}
11

## Página 16

3.2. CriandooloopprincipaldoJumper CasadoCódigo
Oqueacontecerácomonossoloopquandoojogadordeixaraaplicaç ão?
Atéomomento,quandoojogadorsairdoJumper,ojogocontinuaráro-
dandopoisathreadnãofoiparada!Issopodeconsumirrecursosdoaparelho
desnecessariamente.
Precisamoscontrolaroinícioepausadoloopdojogo.Porém,comopo-
demossaberqueojogadorsaiudanossaaplicaç ão?Utilizandoociclodevida
da MainActivity!
No onPause,vamospausarathreaddojogo:
public class MainActivity extends Activity {
@Override
protected void onPause() {
super.onPause();
game.cancela();
}
}
Nanossaclasse Gameaindanãotemosométodo cancela. Vamos
implementá-loagora:
public class Game extends SurfaceView implements Runnable {
public void cancela() {
this.isRunning = false;
}
}
Agorapodemospausarnossoloopaodeixaraaplicaç ão,mascomofare-
mospararodá-lonovamente?Comopodemossaberqueojogadorvoltouao
nossojogo?No onResumeda MainActivity!
Vamos iniciar o loop principal no Jumper no onResume da
MainActivity:
public class MainActivity extends Activity {
@Override
protected void onResume() {
super.onResume();
game.inicia();
12

## Página 17

CasadoCódigo Capítulo3. ComeçandooJumper
new Thread(game).start();
}
}
Ométodo iniciaficaassim:
public class Game extends SurfaceView implements Runnable {
public void inicia() {
this.isRunning = true;
}
}
Comoloopprincipalfuncionando,podemoscriaroselementosdojogo!
3.3 C omo desenhar elementos no SurfaceView?
Paradesenharalgoemum SurfaceViewprecisamosteracessoaoobjeto
responsávelporrenderizarelementosnatela:o canvas.Comesseobjeto,po-
demosdesenharformasgeométricasouatémesmo bitmaps.
Desenharelementosemumcanvasconsomeumtempodealgunsmilis-
segundosquejáéosuficienteparaonossoolhoperceberqueumquadroestá
sendosubstituídoporoutro. Enquantoocanvasnãoestápronto,atelafica
preta,porumperíodomuitocurto,criandooefeitodetela“piscante”cha-
mado flickering.
Paranãotermosquenospreocuparcomisso,oAndroidjátemumaforma
deevitaresse flickering:enquantoumquadroestásendoexibidoparaojo-
gador,umnovoestásendodesenhadoemsegundoplano. Quandoonovo
quadroestápronto,oAndroidsótrocaovelhopelonovo.Aúnicacoisaque
temosquefazerépegarocanvasparadesenhare,quandotudoestiverpronto,
exibi-lo.
Paratermosacessoaocanvas,precisamosdeumobjetoquepermitaa
ediçãodecadapixeldanossatela.Esseobjetoéo SurfaceHolder.Como
estamosemum SurfaceView,paraobtermosacessoao SurfaceHolder,
bastachamarométodo getHolder:
public class Game extends SurfaceView implements Runnable{
13

## Página 18

3.3. ComodesenharelementosnoSurfaceView? CasadoCódigo
private final SurfaceHolder holder = getHolder();
}
Pormeiodesse SurfaceHolderteremosacessoaocanvas! Paraisso,
bastachamarométodo lockCanvasdentrodoloopprincipalnonossojogo:
public class Game extends SurfaceView implements Runnable{
private final SurfaceHolder holder = getHolder();
@Override
public void run() {
while(isRunning) {
Canvas canvas = holder.lockCanvas();
}
}
}
Alémdisso,quandoterminarmosdedesenharoselementosnonosso
canvas, vamos liberá-lo para a tela do jogador por meio do método
unlockCanvasAndPost:
public class Game extends SurfaceView implements Runnable{
private final SurfaceHolder holder = getHolder();
@Override
public void run() {
while(isRunning) {
Canvas canvas = holder.lockCanvas();
//Aqui vamos desenhar os elementos do jogo!
holder.unlockCanvasAndPost(canvas);
}
}
}
Aochamaro getHolder, precisamosgarantirquetemosacessoao
SurfaceHolder antesdecomeçarmosadesenhar. Docontrário,tomare-
14

## Página 19

CasadoCódigo Capítulo3. ComeçandooJumper
mosum NullPointerException.Aformamaissimplesparatercertezadeque
sóvamosdesenharquandonosso holderestiverprontoparaissoéuma
verificaçãoemnossoloop:
public class Game extends SurfaceView implements Runnable{
@Override
public void run() {
while(isRunning) {
if(!holder .getSurface().isValid()) continue;
//Restante do código...
}
}
}
3.4 C riando nosso primeiro elemento do Jum-
per: a classe Passaro
Vamoscriaroprincipalcomponentedonossojogo:opássaro.Paraisso,cri-
aremosumaclasse Passaro. Inicialmente,vamosutilizaralgumaforma
simplespararepresentarnossopássaro:umcírculo.Alémdisso,eleteráacor
vermelha.
Paradesenharumcírculovermelhonatela,utilizamosummétododa
classe Canvaschamado drawCircle:
public class Passaro {
private static final int X = 100;
private static final int RAIO = 50;
private int altura;
public Passaro() {
this.altura = 100;
}
15

## Página 20

3.4. CriandonossoprimeiroelementodoJumper:aclassePassaro CasadoCódigo
public void desenhaNo(Canvas canvas){
canvas.drawCircle(X, altura, RAIO, ??);
}
}
Paracriarmosacorvermelha,vamosutilizaraclasse Paint.Comotam-
bémserãousadasoutrascoresaolongodojogo,vamoscentralizá-lasemuma
classechamada Cores.Nestaclasse,teremosométodo getCorDoPassaro
queretornaráum Paintrepresentandoacorvermelha:
public class Cores {
public static Paint getCorDoPassaro() {
Paint vermelho = new Paint();
vermelho.setColor(0xFFFF0000);
return vermelho ;
}
}
Vejaqueacorvermelha(0xFF0000)érepresentadacomo0x FFFF0000.
Essesdoisprimeirosvaloresrepresentamaquantidadede opacidadedacor,
sendoqueFFsignificaomáximodeopacidade(ouomínimodetransparên-
cia)possível. Esseformatoquepermitecontrolaratransparênciadacoré
chamadode ARGB.
Comométodo getCorDoPassaropronto,bastachamá-lonaclasse
Passaro:
public class Passaro {
private static final Paint vermelho =
Cores.getCorDoPassaro();
private static final int X = 100;
private static final int RAIO = 50;
private int altura;
public Passaro() {
this.altura = 100;
16

## Página 21

CasadoCódigo Capítulo3. ComeçandooJumper
}
public void desenhaNo(Canvas canvas) {
canvas.drawCircle(X, altura, RAIO, vermelho);
}
}
Tendoométodo desenhaNo, vamoschamá-lonoloopprincipalda
nossaclasse Game:
public class Game extends SurfaceView implements Runnable{
private Passaro passaro;
@Override
public void run() {
while(isRunning) {
if(!holder .getSurface().isValid()) continue;
canvas = holder.lockCanvas();
passaro.desenhaNo(canvas);
holder.unlockCanvasAndPost(canvas);
}
}
}
Perceba que em nenhum momento instanciamos a classePassaro.
Ondepodemosfazerisso?
Temosquetomarbastantecuidadoondedaremos newnosnossosele-
mentos. Seráqueprecisaremosdeumnovo Passaroacadaloop? Não.
Dessaforma,sempremanipularemosa mesmainstânciade Passaro!Caso
instanciemoso Passarodentrodoloop,criaremosmuitosobjetosname-
móriadoaparelho,causandoumalentidãononossojogo!
Sendo assim, vamos criar um métodoinicializaElementos e
chamá-lonoconstrutordanossaclasse Game:
17

## Página 22

3.4. CriandonossoprimeiroelementodoJumper:aclassePassaro CasadoCódigo
public class Game extends SurfaceView implements Runnable{
private Passaro passaro;
public Game(Context context) {
super(context);
inicializaElementos();
}
private void inicializaElementos() {
this.passaro = new Passaro();
}
}
AorodaroJumper,teremosaseguintetela:
18

## Página 23

CasadoCódigo Capítulo3. ComeçandooJumper
Fig.3.4:Nossopássaronateladojogo.
Temosnossoprimeiroelementosendodesenhadonatela,porémeleestá
estático.Nodecorrerdojogo,oqueacontececomopássaro?Elecai.Vamos
19

## Página 24

3.5. Criandoocomportamentopadrãodopássaro:ométodocai CasadoCódigo
implementarisso!
3.5 C riando o comportamento padrão do pás-
saro: o método cai
Noloopprincipal,alémdedesenharo Passaro,vamosfazê-locairpormeio
dométodo cai:
public class Game extends SurfaceView implements Runnable{
@Override
public void run() {
while(isRunning) {
if(!holder .getSurface().isValid()) continue;
canvas = holder.lockCanvas();
passaro.desenhaNo(canvas);
passaro.cai();
holder.unlockCanvasAndPost(canvas);
}
}
}
Faremosopássarocair5pixelsacadachamadaaométodo cai.Sendo
assim,nossaimplementaçãodométodo caideveseraseguinte:
public class Passaro {
private int altura;
public void cai() {
this.altura += 5;
}
}
Issoéosuficienteparaderrubarmosopássaroacadaiteraç ãodonosso
loopprincipal.
20

## Página 25

Capítulo4
Colocandoumaimagemde
fundo
Temosnossopássarodesenhadonatela.Porém,aoimplementarmosomé-
todo cai,criamosumrastroindesejado.Comopoderemosresolverisso?
Vimosqueaclasse SurfaceView(mãedanossaclasse Game)éares-
ponsávelpordesenharoselementosdonossojogonatelaeque,aofazero
desenho,essaclassenãomanipulaos pixelsqueestãosendovisualizadospelo
jogador;odesenhoéfeitoemsegundoplanoeentãoexibidoaojogador.
Essaestrutura,quefoitãoútilparaevitarbugsdeatualizaç ãodatela(flic-
kering),tambéméresponsávelpordeixarorastrodoselementos!
QuandooAndroidtrocao framequeestáemprimeiroplanoparaaquele
queestáemsegundoplano(evice-versa),ele nãolimpaoconteúdoanteri-
ormentedesenhado!Éexatamenteesseconteúdo“desatualizado”quevemos.

## Página 26

CasadoCódigo
Percebaqueorastrodabolaéformadopelassuasposiçõesanteriormente
desenhadas.
Fig.4.1:Rastrodabolinhaaocair.
22

## Página 27

CasadoCódigo Capítulo4. Colocandoumaimagemdefundo
Vamoscorrigiresseproblemacolocandoumaimagemqueocupeatela
inteira.Dessaforma,vamosocultarasimagens“desatualizadas”edeixarape-
nasafiguraatualdabola.Seráo backgrounddonossojogo!
Arquivos usados no jogo
Osarquivosqueusaremosaolongodesselivropodemserbaixados
emhttps://github.com/felipetorres/jumper-arquivos.
ComoobackgrounddoJumperseráumaimagem,vamosprecisardeum
drawableparausarnonossocódigo.Ondepodemoscolocaressaimagem,já
queexistemváriaspastas drawable?
Muitasvezeséimportantetercontrolesobrecomoasimagensserãore-
dimensionadaspeloAndroid. Cada qualifierpresentenaspastas drawable
(mdpi,hdpi,xhdpietc.) representaumtipodedensidadedetela(medium,
high, extra high)quenecessitadeumaresoluç ãoetamanhoespecíficos.Po-
demoscriarumtamanhodonossobackgroundparacadatipodetelaoure-
dimensionarmosviacódigo,diminuindootamanhodaapp.Éoquefaremos.
Paraisso,precisaremosdizeraoAndroid nãoredimensionarautomatica-
mentenossobackground. Nessescasos,devemoscolocarnossaimagemna
pasta drawable-**nodpi**.Nãosepreocupecasoestapastanãoexista;
bastacriá-lanodiretório res.
Na classe Game podemos pegar a imagem utilizando o método
decodeResourcedaclasse BitmapFactory:
this.background = BitmapFactory.decodeResource(getResources(),
R.drawable.background);
Agora,podemosdesenharesse backgroundno loopprincipaldonosso
jogoutilizandoométodo drawBitmapdo canvas.Percebaqueosdese-
nhossãofeitosemcamadas:osdesenhosquesãofeitosprimeiroficamabaixo
dosseguintes,logonossobackgroundtemqueseraprimeiracoisaaserde-
senhadanatela:
@Override
public void run() {
23

## Página 28

CasadoCódigo
while(isRunning) {
if(!holder.getSurface().isValid()) continue;
canvas = holder.lockCanvas();
canvas.drawBitmap(background, 0, 0, null );
//código de desenho do pássaro...
holder.unlockCanvasAndPost(canvas);
}
}
24

## Página 29

CasadoCódigo Capítulo4. Colocandoumaimagemdefundo
Fig.4.2:Backgroundadicionadoaojogo.
Precisamosredimensionarnossobackgroundparaqueeleocupetodoo
espaçoverticaldatela.Porém,paradefinirmosaalturadessaimagem,deve-
25

## Página 30

CasadoCódigo
mossaberaalturadatela;vamosutilizaraclasse WindowManagerparanos
forneceressasinformações.
WindowManager wm = (WindowManager) context.getSystemService(
Context.WINDOW_SERVICE);
Comessaclasse,podemosobterasdimensõesdatelapormeiodométodo
getDefaultDisplayedométodo getMetrics:
WindowManager wm = (WindowManager) context.getSystemService(
Context.WINDOW_SERVICE);
Display display = wm.getDefaultDisplay();
metrics = new DisplayMetrics();
display.getMetrics(metrics);
Ao executar esse código, as dimensões da tela estarão no objeto
DisplayMetrics.Pararecuperaraalturadatela,bastachamarométodo
heightPixelsnavariável metrics:
int alturaDaTela = metrics.heightPixels;
Vamoscentralizaressasoperaçõesemumaclassechamada Telacom
ummétodo getAltura:
public class Tela {
private DisplayMetrics metrics;
public Tela(Context context) {
WindowManager wm = (WindowManager) context.getSystemService(
Context.WINDOW_SERVICE);
Display display = wm.getDefaultDisplay();
metrics = new DisplayMetrics();
display.getMetrics(metrics);
}
public int getAltura() {
return metrics .heightPixels;
}
}
26

## Página 31

CasadoCódigo Capítulo4. Colocandoumaimagemdefundo
Comessaclasse,podemosredimensionarnossobackgrounddaclasse
Gamechamandoométodo createScaledBitmap:
Bitmap back = BitmapFactory.decodeResource(getResources(),
R.drawable.background);
this.background = Bitmap.createScaledBitmap(back,
back.getWidth(), tela.getAltura(), false);
Como queremos redimensionar a imagem apenas na vertical, vamos
manteralarguraoriginaldobackground. Paracapturaressalargura,basta
chamarométodo getWidth.
Issoéosuficienteparanossaimagemdefundoficarcomaseguinteapa-
rência:
27

## Página 32

CasadoCódigo
Fig.4.3:Backgroundocupandoatelainteira.
28

## Página 33

CasadoCódigo Capítulo4. Colocandoumaimagemdefundo
4.1 I mplementando o controle do jogador: o
pulo do pássaro
Nestemomento,oelemento Passaronãodeixanatelamaisnenhumrastro
visívelaojogador!Podemosnosdedicaraoseumovimento.Oúnicocontrole
disponívelaojogadordoJumperseráo toque na tela(nãoteremosnenhum
outrobotão)quefaráopássaropular.
Paraimplementaropulodopássaro,bastadeslocá-loumaquantidade
de pixelsparacima. Vamosfazerissocriandoométodo pulanaclasse
Passaro:
public class Passaro {
//...
public void pula() {
this.altura -= 150;
}
}
Notequeométodopula diminuiaalturaem150pixels.Comooponto
(0,0)representao canto superior esquerdodatela,aodecrementaraaltura,
estamosfazendoopássaroserdeslocadoparacima!
Emquemomentovamoschamaressemétodo pula?Quandoojogador
tocara Viewdojogo!
Paraisso,temosqueimplementarométodo onTouchnaclassequere-
presentaa Viewdonossojogo: aclasse Game. Paratermosacessoaomé-
todo onTouch,vamosdizerqueessaclassedeveimplementarainterface
onTouchListener:
public class Game extends SurfaceView implements Runnable,
OnTouchListener {
@Override
public boolean onTouch(View v, MotionEvent event) {
return false;
}
}
29

## Página 34

4.1. Implementandoocontroledojogador:opulodopássaro CasadoCódigo
Nestemétodo,bastachamaro puladoobjeto passaro:
public class Game extends SurfaceView implements Runnable,
OnTouchListener {
@Override
public boolean onTouch(View v, MotionEvent event ) {
passaro.pula();
return false;
}
}
Implementamoso listener,porémissonãoésuficienteparaqueométodo
onTouchsejachamadosemprequeojogadortocarnanossa View,poisem
nenhummomentodissemosqual Viewdeveráchamaresse onTouch.Vamos
fazerissocomométodo setOnTouchListener.
Comonossaclasse Game é uma View,podemoschamaressemétodo
diretamentenoseuconstrutor:
public class Game extends SurfaceView implements Runnable,
OnTouchListener{
public Game(Context context) {
super(context);
//...
setOnTouchListener(this);
}
}
Comisso,finalizamosocontroledojogador! Contudo,aindatemosal-
gunsoutroselementosnestejogo.
30

## Página 35

Capítulo5
Criandoocanoinferior
Alémdopássaro,oJumpertambémpossuioutroelementoaserdesenhadona
tela:oscanos!Comoaproximamosinicialmenteopássaroparaumabolinha,
vamosaproximaroscanospararetângulos.
Assimcomofeitocomopássaro,nossoobjetivoserádesenharoscanos
no loopprincipaldaclasse Game,algocomo:
public class Game extends SurfaceView implements Runnable,
OnTouchListener{
@Override
public void run() {
while(isRunning) {
//lockCanvas e desenhos anteriores...
cano.desenhaNo(canvas);

## Página 36

CasadoCódigo
//unlock...
}
}
}
Vamoscriarumaclasse Canocontendoométodo desenhaNo. Além
disso,vamosdefinirocanocom250 pixelsdealturae100 pixelsdelargura:
public class Cano {
private static final int TAMANHO_DO_CANO = 250;
private static final int LARGURA_DO_CANO = 100;
public void desenhaNo(Canvas canvas) {
//Como será o desenho do cano?
}
}
Primeiramente, vamos criar o cano inferior com o método
desenhaCanoInferiorNo. Paradesenharumretângulo,chamaremoso
método drawRectdaclasse Canvas:
public class Cano {
public void desenhaNo(Canvas canvas) {
desenhaCanoInferiorNo(canvas);
}
private void desenhaCanoInferiorNo(Canvas canvas) {
canvas.drawRect(??, ??, ??, ??, ??);
}
}
Paradesenharumretângulocomométodo drawRect,precisamospas-
sarascoordenadas(x,y)dedoispontos:ocantosuperioresquerdoeocanto
inferiordireito.
Noentanto,quaisserãoessespontos?
32

## Página 37

CasadoCódigo Capítulo5. Criandoocanoinferior
Ocantoinferiordireitodocanodeveestarna base da tela,ouseja,deve
teramesmaalturadatela(lembre-sedequeoponto(0,0)estánotopoda
tela).Comojáconseguimospegaraalturadatela,podemospassá-laparao
drawRect:
canvas.drawRect(??, ??, ??, tela.getAltura(), ??);
Ocanodeveter250 pixelsdealtura,logodeveacabar250 pixels antesda
basedatela. Bastasubtrair250 pixelsdaalturadatelaeteremososegundo
parâmetrodocano:
int alturaDoCanoInferior =
tela.getAltura() - TAMANHO_DO_CANO;
public class Cano {
private static final int TAMANHO_DO_CANO = 250;
private int alturaDoCanoInferior;
private Tela tela ;
public Cano(Tela tela) {
this.tela = tela;
this.alturaDoCanoInferior =
tela.getAltura() - TAMANHO_DO_CANO;
}
private void desenhaCanoInferiorNo(Canvas canvas) {
canvas.drawRect(??, alturaDoCanoInferior, ??,
tela.getAltura(), ??);
}
}
Atéessemomento,limitamosaalturadocano.Porém,comolimitaremos
asualargura? Oprimeiroeterceiroargumentosdo drawRectsereferem
justamenteaisso!
Temosquedesenharessecanodetalformaquesuaposiç ãohorizontal
possavariar,poisafinaldecontas,eledeverásemoverparaadire çãodopás-
saro.Vamosreceberessaposiçãonoconstrutordo Cano:
33

## Página 38

CasadoCódigo
public class Cano {
private static final int TAMANHO_DO_CANO = 250;
private int alturaDoCanoInferior;
private Tela tela ;
private int posicao;
public Cano(Tela tela, int posicao) {
this.tela = tela;
this.posicao = posicao;
this.alturaDoCanoInferior =
tela.getAltura() - TAMANHO_DO_CANO;
}
private void desenhaCanoInferiorNo(Canvas canvas) {
canvas.drawRect(posicao, alturaDoCanoInferior, ??,
tela.getAltura(), ??);
}
}
Agoratemosquealateralesquerdado Canocomeçaráem posicao,
sóprecisamosdefinirondeficaráalateraldireitadesse Cano.Inicialmente,
definimosqueeledeveriater100 pixelsdelargura,oquesignificaquealateral
direitadeveráficara100 pixelsda posicao!
public class Cano {
private static final int TAMANHO_DO_CANO = 250;
private static final int LARGURA_DO_CANO = 100;
public Cano(Tela tela, int posicao) {
this.posicao = posicao;
this.alturaDoCanoInferior =
tela.getAltura() - TAMANHO_DO_CANO;
}
private void desenhaCanoInferiorNo(Canvas canvas) {
canvas.drawRect(posicao, alturaDoCanoInferior,
posicao + LARGURA_DO_CANO, tela.getAltura(), ??);
34

## Página 39

CasadoCódigo Capítulo5. Criandoocanoinferior
}
}
Comisso,sóprecisamosdefiniracorqueesseelementoterá.
Todoelementodesenhadono canvaspodereceberumacorpormeio
deum Paint.Damesmaformaquefizemoscomo Passaro,vamoscriar
ummétodo getCorDoCanonaclasse Cores:
public class Cores {
public static Paint getCorDoCano() {
Paint verde = new Paint();
verde.setColor(0xFF00FF00);
return verde;
}
}
Definimosacorverdeparao Cano(00FF00),porémlembre-sedequea
cordeveestarnoformato ARGB,quepermiteousodetransparência.Neste
formato,acorverdeé FF00FF00.
Comacordo Canocriada,podemospassá-laparaoúltimoargumento
doseu drawRect:
public class Cano {
private final Paint verde = Cores.getCorDoCano();
//Códigos anteriores...
private void desenhaCanoInferiorNo(Canvas canvas) {
canvas.drawRect(..., ..., ..., ..., verde);
}
}
Sóprecisamosinstanciaresse Canonanossaclasse Gamedizendoqual
serásuaposiçãoinicial:
this.cano = new Cano( tela, 200);
35

## Página 40

CasadoCódigo
Comisso,finalizamosacriaçãodocanoinferiordoJumper!
Fig.5.1:Jumpercomumcanoinferior.
36

## Página 41

CasadoCódigo Capítulo5. Criandoocanoinferior
5.1 M ovimentando o cano
NoJumper,oscanosdevemsemovernadire çãodopássaro.Atéomomento,
nossoinimigoestáestáticonatela.Vamosimplementarseumovimentopara
aesquerda.
Utilizandoamesmaideiadaclasse Passaro,vamosdeslocaresse Cano
alguns pixelsparaaesquerdaacadaiteraç ãodonosso loopprincipal. Para
isso,precisaremosdeummétodo move:
public class Game extends SurfaceView implements Runnable,
OnTouchListener{
@Override
public void run() {
while(isRunning) {
//lockCanvas...
//Desenho do pássaro...
cano.desenhaNo(canvas);
cano.move();
//unlock...
}
}
}
Comodeixamosa posicaodo Canovariáveleaconsideramospara
fazeracontadalargura,podemossimplesmentealteraressa posicaoeo
Canosemoverácorretamentemantendosualargura.Ométodo moveapenas
alteraráavariávelposicao:
public class Cano {
//...
public void move() {
posicao -= 5;
}
}
Issoéosuficienteparamovermoso Canoparaaesquerda!
37

## Página 43

Capítulo6
Criandovárioscanos
Aindatemossomenteumcanononossojogo,alémdissoelesaimuitorápido
datela.Estánahoradecolocarumpoucomaisdeemo çãocommaiscanos.
Podemosalterarnossacriaçãodeumcanoparacriardiversoscanos,cinco
porexemplo:
this.cano1 = new Cano (tela, 200);
this.cano2 = new Cano (tela, 450);
this.cano3 = new Cano (tela, 700);
this.cano4 = new Cano (tela, 950);
this.cano5 = new Cano (tela, 1200);
Ocódigoparecefeio,umavezqueoestamoscopiandoecolandoportodo
lado.Vamoscriaroscanosemumlaço,colocandoumadistânciade250 pixels
entrecadaum:

## Página 44

CasadoCódigo
int posicao = 200;
for(int i=0; i<5; i++) {
posicao += 250;
Cano cano = new Cano(tela, posicao);
}
Masqueremosagoraacumulartodosessescanosparapoderdesenhá-los.
Paraissodevemoscriaruma Listde Canos:
List<Cano> canos = new ArrayList<Cano>();
int posicao = 200;
for(int i=0; i<5; i++) {
posicao += 250;
Cano cano = new Cano(tela, posicao);
canos.add( cano);
}
Pronto,cincocanosemnossasmãos.Sófaltadesenhá-los.Devemosco-
locaralistacomovariávelmembroefazerum fornahoradodesenho,mas
calmalá:nossocódigodo Gameestámisturandomuitacoisa.Temcano,tem
pássaro,tembackground,temmaiscanos,tem touch,start,stop.Vamosiso-
larumpoucomelhorascoisas.Assimcomo Canoéumelementodenosso
jogo, Canostambémpareceser:temosumconjuntodecanosnojogoeva-
moscriarumaclassechamada Canospararepresentartodoseles,nopacote
elementos:
public class Canos {
private List<Cano> canos = new ArrayList<Cano>();
public Canos(Tela tela) {
int posicaoInicial = 200;
for(int i=0; i < 5; i++) {
posicaoInicial += 250;
canos.add(new Cano(tela, posicaoInicial));
}
}
}
40

## Página 45

CasadoCódigo Capítulo6. Criandovárioscanos
Paratiraraimpressãodeestarmosusando“númerosmágicos”,vamosre-
fatorareextrairalgumasvariáveisparadarsignificadoaosnúmerosimpor-
tantesdonossojogo:
public class Canos {
private static final int QUANTIDADE_DE_CANOS = 5;
private static final int DISTANCIA_ENTRE_CANOS = 250;
private final List<Cano> canos = new ArrayList<Cano >();
public Canos( Tela tela) {
int posicaoInicial = 200;
for(int i=0; i<QUANTIDADE_DE_CANOS; i++) {
posicaoInicial += DISTANCIA_ENTRE_CANOS;
canos.add( new Cano(tela, posicaoInicial));
}
}
}
Agorasim,dentrodenosso Gameainicializaçãodoselementosficamais
simples:bastadizerquequeremoscriaroscanos.Removemosoúnicocano
quetínhamosecriamostodoselesdeumaúnicavez:
private Canos canos;
private void inicializaElementos() {
this.passaro = new Passaro();
this.canos = new Canos(tela);
Bitmap back = BitmapFactory.decodeResource(getResources(),
R.drawable.background);
this.background = Bitmap.createScaledBitmap(back,
back.getWidth(), tela.getAltura(), false);
}
Faltaagoradesenharessescincocanos! Ondeantesdesenhávamosum
únicocanoeomovíamos,chamaremosométodoequivalenteparatodosde
umaúnicavez:
41

## Página 46

CasadoCódigo
canos.desenhaNo(canvas);
canos.move();
Claro,osdoismétodosaindanãoexistememnosso Canosedevemos
implementá-los,fazendoum looppelosnossos canos:
public void desenhaNo(Canvas canvas) {
for(Cano cano : canos )
cano.desenhaNo(canvas);
}
public void move() {
for(Cano cano : canos )
cano.move();
}
Rodamosnossojogoeagoratemoscincocanos!Todosdetamanhoigual,
éverdade,masjásãocincocanos!
42

## Página 47

CasadoCódigo Capítulo6. Criandovárioscanos
Fig.6.1:Nossojogocomoscanosinferiores.
43

## Página 48

6.1. Criandooslimitesparapulo:ochãoeteto CasadoCódigo
6.1 C riando os limites para pulo: o chão e teto
Vamosagoralimitarnossossaltosequedas.Primeiramente,quandoopássaro
tocarnabasedatela,devemosparardecair.
Comoestamoslidandocomumcírculo,parasabersesuabordatocaa
basedatelabastaverificarseasua alturamaisseu RAIOémaiorqueo
tamanhoda tela:
public void cai() {
boolean chegouNoChao = altura + RAIO > tela.getAltura();
if(!chegouNoChao) {
altura += 5;
}
}
Vejaqueprecisamosdeummétodoqueestánaclasse Tela,porémainda
nãotemosacessoaesseobjetodentrodaclasse Passaro.Pararesolverisso,
vamosrecebera Telanoconstrutordo Passaro:
public class Passaro {
private Tela tela ;
public Passaro(Tela tela) {
this.tela = tela;
//...
}
//Outros métodos...
}
Tambémnãopodemospularalémdotopodatela,issoé,temosqueve-
rificarquandoabordadonossocírculotocaotopodatela.Comootopoda
telatem alturaigualazero,nossocírculotocaráotopodatela sempreque
sua alturaforigualaoseupróprio RAIO.Logo,seessa alturafor maior,
sabemosqueeleaindanãoestánotopo.Lembre-sequequantomaioraaltura,
maisparabaixodatelaoelementoestá((0,0)éocanto superioresquerdo!).
44

## Página 49

CasadoCódigo Capítulo6. Criandovárioscanos
Nossométodo pula,paraverificarsechegamosaotopodatela,deve
ficarassim:
public void pula() {
if(altura > RAIO) {
altura -= 150;
}
}
Comoalteramosoconstrutordo Passaro,apareceuumerronaclasse
Game.Bastapassaravariável telaparao Passaro:
private void incializaElementos() {
this.passaro = new Passaro(tela);
//...
}
45

## Página 51

Capítulo7
Criandooscanossuperiores
Ganharumjogoquesópossuicanosembaixoémuitofácil,bastaficarvo-
andonoalto. Estánahoradedeixarmosnossojogomaisdifícil! Paraisso,
praticaremososcálculosdedimensãodetelaeosmétodosdedesenhoquejá
vimosanteriormente.Nossopróximopassoécolocarcanosnãosóembaixo,
mastambémemcimadatela.
Nãoseesque çadequeotamanhodocanoinferioreraigualaotamanho
datelamenosotamanhodocano:
this.alturaDoCanoInferior = tela.getAltura() - TAMANHO_DO_CANO;
Portanto,énaturalcolocarmosotamanhodocanosuperiorcomosendo
0(pontoinicialdatela)maisotamanhodocano:
this.alturaDoCanoInferior = tela.getAltura() - TAMANHO_DO_CANO;
this.alturaDoCanoSuperior = 0 + TAMANHO_DO_CANO;

## Página 52

CasadoCódigo
Masaindatemalgodeestranho: nossoscanostêmtodosomesmota-
manho.Vamosaleatorizarumpoucoessasdimensõespegandoumnúmero
entre0e150paraconstruircanosdiferentes:
this.alturaDoCanoInferior =
tela.getAltura() - TAMANHO_DO_CANO - valorAleatorio();
this.alturaDoCanoSuperior =
0 + TAMANHO_DO_CANO + valorAleatorio();
Definimoso valorAlteatorio:
private int valorAleatorio() {
return (int) (Math.random() * 150);
}
Agora,precisamosdesenharocanodebaixo eocanodecima.Paradese-
nharocanosuperior,vamoscriarummétodo desenhaCanoSuperiorNo:
private final Paint VERDE = Cores.getCorDoCano();
public void desenhaNo(Canvas canvas) {
desenhaCanoSuperiorNo(canvas);
desenhaCanoInferiorNo(canvas);
}
private void desenhaCanoSuperiorNo(Canvas canvas) {
canvas.drawRect(??, ??, ??, ??, VERDE);
}
private void desenhaCanoInferiorNo(Canvas canvas) {
canvas.drawRect(posicao, alturaDoCanoInferior,
posicao + LARGURA_DO_CANO, tela.getAltura(), VERDE);
}
Vamos olhar com calma o conteúdo do métododrawRect do
desenhaCanoSuperiorNo:
canvas.drawRect(??, ??, ??, ??, VERDE);
48

## Página 53

CasadoCódigo Capítulo7. Criandooscanossuperiores
Lembre-sedequeosdoisprimeirosargumentosrepresentamo canto su-
perior esquerdodoretânguloeosoutrosdoissãooseu canto inferior di-
reito. Sendoassim,ondeestaráocantosuperioresquerdodonossocano
superior?Notopodatela!
Logo,osegundoargumentodeveráserzero:
canvas.drawRect(??, 0, ??, ??, VERDE);
Qualdeveráseraalturadocanosuperior?Comojácriamosumavariável
alturaDoCanoSuperior,podemospassá-ladiretamenteaoquartoargu-
mento:
canvas.drawRect(??, 0, ??, alturaDoCanoSuperior, VERDE);
Aalturadocanosuperiorestádefinida.Vamosvercomoficarásualar-
gura.Comonossocanosuperiordeverátera mesma largura do cano infe-
rior,devemospassarosmesmosvaloresparaosdois.Comoocanoinferior
começaem posicaoetem posicao + LARGURA_DO_CANO delargura,
vamospassaressesmesmosvaloresparaocanosuperior!
canvas.drawRect(posicao, 0, posicao + LARGURA_DO_CANO,
alturaDoCanoSuperior, VERDE);
Nossométodo desenhaCanoSuperiorNoficaráassim:
private void desenhaCanoSuperiorNo(Canvas canvas) {
canvas.drawRect(posicao, 0, posicao + LARGURA_DO_CANO,
alturaDoCanoSuperior, VERDE);
}
Agorapodemosrodarnossojogonovamenteevemosquetemosdezca-
noscomtamanhosdiferentesparadesviarmos!
49

## Página 54

CasadoCódigo
Fig.7.1:Canoscomtamanhosdiferentes.
Masnossojogoaindaémuitocurto.Cincoparesdecanospassammuito
rápidopornossatelaeficamossemtermaisoquefazernojogo.Vamosfazer
50

## Página 55

CasadoCódigo Capítulo7. Criandooscanossuperiores
comqueoscanosnuncaparemdeaparecer. Paraissoprecisamosdecanos
infinitos,mascomo?
7 .1 C riando infinitos canos
Umatáticaemjogosinfinitosédefazercomquequandoocanosaiadatela,
umnovocanosejacolocadonofimdetodososcanos:dessamaneirasempre
temosamesmaquantidadedecanos.Lembre-sedenossométododemover
canos:
public void move() {
for(Cano cano : canos) {
cano.move();
}
}
Apósmoverumcano,verificaremosseelesaiudatela:
for(Cano cano : canos ) {
cano.move();
if(cano.saiuDaTela()) {
//O que faremos?
}
}
Casoeletenhasaídodatela,podemoscriaroutro Canoeadicioná-loà
nossa List<Cano>:
for(Cano cano : canos ) {
cano.move();
if(cano.saiuDaTela()) {
Cano outroCano =
new Cano(tela , getMaximo() + DISTANCIA_ENTRE_CANOS);
canos.add(outroCano);
}
}
Percebaquetentamosadicionarum canoàmesmalistaqueépercorrida
no for.Issocausaráuma ConcurrentModificationException!Para
51

## Página 56

7.1. Criandoinfinitoscanos CasadoCódigo
adicionaralgoàlistaqueépercorrida,precisaremosdeum ListIterator;
paraobtermosesseobjetobastachamarométodo listIteratorquetoda
Listpossui.Portanto,emvezdeum forvamosalterá-loparaum while:
ListIterator<Cano> iterator = canos.listIterator();
while(iterator.hasNext()) {
Cano cano = (Cano) iterator.next();
cano.move();
if(cano.saiuDaTela()) {
Cano outroCano =
new Cano(tela, getMaximo() + DISTANCIA_ENTRE_CANOS);
iterator.add(outroCano);
}
}
Paraverificarseumcanosaiudatela,naclasse Canobastaconferirse
suaposiçãoémenorquezero:
public boolean saiuDaTela() {
return posicao < 0;
}
Quaseisso... Ocanonãosaidatelaquandoseupontoesquerdosaida
tela,elesaiquandoelepassouporcompleto(todasualargura):
public boolean saiuDaTela() {
return posicao + LARGURA_DO_CANO < 0;
}
Agorasóprecisamossabercomofaremosométodo getMaximo.Temos
queadicionarumnovo Canoàquelesjáexistentes,emqualposiçãoeledeverá
sercolocado?
Precisamossaberqualéo Canoquepossuiamaiorposição(ouseja,o
Canomaisàdireitapossível)danossalistaparapodermosdeterminarapo-
siçãodonovo Cano.Então,bastapercorrernossalistaecompararaposiç ão:
private int getMaximo() {
int maximo = 0;
52

## Página 57

CasadoCódigo Capítulo7. Criandooscanossuperiores
for(Cano cano : canos) {
maximo = Math.max( cano.getPosicao(), maximo);
}
return maximo ;
}
Nãoseesque çadefazero getPosicaonaclasse Cano.
Comisso,sempreteremosumnovo Canocriadoassimquealgumsair
datela. Agoratemosumasequênciainfinitadecanosdosquaisojogador
precisadesviar!
Nestemomento,aojogaroJumper,veremosalgoestranhoconformeo
tempopassa.Oqueseráisso?
7 .2 D escartando canos anteriores
Conformeotempopassa(eos Canossaemdatela),vamoscriandooutros
Canoseadicionando-osàlista.Vejaqueelaestáficandocadavezmaior,com
maiselementos!Apartirdeummomentoédeseesperarqueteremostantos
Canosnanossalista,quenossoaparelhonãovaidarcontadegerenciá-lose
oJumperficarábastantelento.
Pararesolveresseproblema,podemosnoslivrardealguns Canos.Quais?
Justamenteaquelesquesaíramdatela!
Logo,seo Canosairdatela,vamosremovê-lodalista!
Vamosusarométodo removedo Iteratorassimqueo canosairda
tela:
ListIterator<Cano> iterator = canos.listIterator();
while(iterator.hasNext()) {
Cano cano = (Cano) iterator.next();
cano.move();
if(cano.saiuDaTela()) {
iterator.remove();
Cano outroCano =
new Cano(tela, getMaximo() + DISTANCIA_ENTRE_CANOS);
iterator.add(outroCano);
53

## Página 58

7.2. Descartandocanosanteriores CasadoCódigo
}
}
Rodandoojogoagoratemosumaserieinfinitadecanosdetamanhos
diferentes!
54

## Página 59

CasadoCódigo Capítulo7. Criandooscanossuperiores
Fig.7.2:Agorapodemosgerarinfinitoscanos.
55

## Página 61

Capítulo8
Criandoapontuaçãodojogo
Chegouahoradecolocarumamaneiradenosdesafiarmosnojogo:quantos
pontossomoscapazesdefazer?Paracontá-los,aoinicializarojogodevemos
criarumnovoobjeto,a Pontuacao:
private void inicializaElementos() {
this.pontuacao = new Pontuacao();
// outras inicializações
}
Ospontossobemcadavezqueum Canosaidatela,demonstrandoa
vitóriadopássarosobreoscanos.Nonossométododemovimentodoscanos,
devemosaumentarapontuaçãotodavezqueumcanosaidatela:
public void move() {
ListIterator<Cano> iterator = canos.listIterator();

## Página 62

CasadoCódigo
while(iterator.hasNext()) {
Cano cano = (Cano) iterator.next();
cano.move();
if(cano.saiuDaTela()) {
pontuacao.aumenta();
iterator.remove();
Cano outroCano =
new Cano(tela, getMaximo() + DISTANCIA_ENTRE_CANOS);
iterator.add(outroCano);
}
}
}
Paraissoaclasse Canosdeveteracessoàpontuação.Devemospassá-la
noconstrutorduranteainicializaçãodenossoselementos:
private void inicializaElementos() {
this.pontuacao = new Pontuacao();
this.passaro = new Passaro();
this.canos = new Canos(tela, pontuacao);
Bitmap back = BitmapFactory.decodeResource(getResources(),
R.drawable.background);
this.background = Bitmap.createScaledBitmap(back,
back.getWidth(), tela.getAltura(), false);
}
Esetaravariávelnoconstrutor:
private final Pontuacao pontuacao;
public Canos(Tela tela, Pontuacao pontuacao) {
this.pontuacao = pontuacao;
int posicaoInicial = 200;
for (int i = 0; i < QUANTIDADE_DE_CANOS; i++) {
posicaoInicial += DISTANCIA_ENTRE_CANOS;
canos.add( new Cano(tela, posicaoInicial));
}
}
58

## Página 63

CasadoCódigo Capítulo8. Criandoapontuaçãodojogo
Faltou criar o método de aumento de pontos dentro de nossa classe
Pontuacao:
public class Pontuacao {
private int pontos = 0;
public void aumenta() {
pontos++;
}
}
Pronto. Quandoocanosaidatela,notificamosapontuaç ãodequeela
deveaumentaremum.Masondeelavaiaparecernatela?Assimcomoqual-
queroutroelemento,vamosimplementarométodo desenhaNo,pedindo
paradesenharumtextopormeiodométodo drawTextdo canvas:
public class Pontuacao {
private static final Paint BRANCO =
Cores.getCorDaPontuacao();
private int pontos = 0;
public void aumenta() {
pontos++;
}
public void desenhaNo(Canvas canvas) {
canvas.drawText(String.valueOf( pontos), 100, 100,
BRANCO);
}
}
Ométodo drawTextrecebeotextoaserescrito,oponto(x,y)ondeesse
textodeveráserposicionadoesuacor.Vamosdesenharumtextonaposiç ão
(100,100)danossatelanacorbranca.
Agora,bastadefiniracorbrancanaclasse Cores:
public static Paint getCorDaPontuacao() {
Paint branco = new Paint ();
branco.setColor(0xFFFFFFFF);
59

## Página 64

CasadoCódigo
return branco;
}
Epedirparadesenharnonossojogo:
@Override
public void run() {
while (isRunning) {
if (!holder.getSurface().isValid()) continue;
canvas = holder.lockCanvas();
canvas.drawBitmap(background, 0, 0, null );
passaro.desenhaNo(canvas);
passaro.cai();
pontuacao .desenhaNo(canvas);
canos.desenhaNo(canvas);
canos.move();
holder.unlockCanvasAndPost(canvas);
}
}
Dessejeito,apontuaçãoficou muitopequena.Ébastantedifícilenxergar
onúmeronocantosuperioresquerdodatela:
60

## Página 65

CasadoCódigo Capítulo8. Criandoapontuaçãodojogo
Fig.8.1:Seráqueficoulegalparaojogador?
Quetalcolocarmosumafontemaiorecom bold(negrito)? Repareque
oobjeto Paintpermiteconfigurardiversascaracterísticasrelacionadasao
61

## Página 66

CasadoCódigo
elementoqueestamosdesenhandonatela.
public static Paint getCorDaPontuacao() {
Paint branco = new Paint ();
branco.setColor(0xFFFFFFFF);
branco.setTextSize(80);
branco.setTypeface(Typeface.DEFAULT_BOLD);
return branco;
}
Bemmelhor!Agoraépossívelverapontuaçãosemproblemas.
62

## Página 67

CasadoCódigo Capítulo8. Criandoapontuaçãodojogo
Fig.8.2:Aumentandoumpoucoafonte,ficoubemmelhor,não?
Podemosiralémedefinirumasombraparaanossapontuaç ão.Asom-
braéumrecursocomumutilizadopelopessoaldedesignparadardestaque
63

## Página 68

CasadoCódigo
emumtextoqueestáporcimadeumaimagem. Bastausarmosométodo
setShadowLayerdo Paint:
branco.setShadowLayer(??, ??, ??, ??);
Noúltimoargumentodizemosqualacordessasombra.Nonossocaso,
vamosdeixá-lapreta:
branco.setShadowLayer(??, ??, ??, 0xFF000000);
Temosquedizerqualseráodeslocamentodessasombraemrelaç ãoao
textooriginal;quantomaisdeslocada,maisvisívelelaestará,porémmenos
naturalserásuaaparência.Vamosdeslocar5 pixelsparabaixoe5 pixelspara
adireita:
branco.setShadowLayer(??, 5, 5, 0xFF000000);
Agora, temos que dizer o quão definida será a borda dessa sombra.
Quantomaiorovalor,menosdefinidosserãoosseuslimites(mais“esfuma-
çada”será).Vamoscolocarumvalor3paraesseargumento:
branco.setShadowLayer(3, 5, 5, 0xFF000000);
Pronto!Bastachamaressemétodono getCorDaPontuacao:
public static Paint getCorDaPontuacao() {
Paint branco = new Paint ();
branco.setColor(0xFFFFFFFF);
branco.setTextSize(80);
branco.setTypeface(Typeface.DEFAULT_BOLD);
branco.setShadowLayer(3, 5, 5, 0xFF000000);
return branco;
}
Vejaqueapontuaçãopossuiumasombra:
64

## Página 69

CasadoCódigo Capítulo8. Criandoapontuaçãodojogo
Fig.8.3:Pontuaçãocomsombraparaummaiordestaque.
Nossojogojáparecebemlegal!Porém,temosumpequenoproblema:o
queacontececomapontuaçãoquandooscanospassampelaposiç ãoonde
65

## Página 70

CasadoCódigo
elaestádesenhada?
Vejao loopprincipaldaclasse Game:
@Override
public void run() {
while(isRunning) {
//Lock canvas...
canvas.drawBitmap(background, 0, 0, null );
passaro.desenhaNo(canvas);
passaro.cai();
pontuacao .desenhaNo(canvas);
canos.desenhaNo(canvas);
canos.move();
//Unlock...
}
}
Percebaquea pontuacaoédesenhadaantesdos canos.Comoo canvas
trabalhacomdesenhoporcamadas,ascamadasdesenhadasprimeiroficarão
por baixodasdesenhadasposteriormente.
Issosignificaqueos canos“passarãoporcima”danossapontuação!
Queremosqueapontuação sempreestejavisívelaojogador,entãovamos
apenastrocaraordemdascamadas:
@Override
public void run() {
while(isRunning) {
//Lock canvas...
canvas.drawBitmap(background, 0, 0, null );
passaro.desenhaNo(canvas);
passaro.cai();
canos.desenhaNo(canvas);
canos.move();
66

## Página 71

CasadoCódigo Capítulo8. Criandoapontuaçãodojogo
pontuacao.desenhaNo(canvas);
//Unlock...
}
}
Vejaqueapontuaçãoagoraficaemcimadoscanos.Perfeito!
67

## Página 72

CasadoCódigo
Fig.8.4:Apontuaçãoéexibidaporcimadoscanos.
68

## Página 73

Capítulo9
Tratandocolisões
Quandonossojogoacaba?Quandoopássarobateremqualquercano.Mas
comodescobrirqueumpássaroencostounocano?Comonosso Passaro
éumcírculoeo Canoumretângulo,temosquedescobrirseocírculotem
algumaintersecçãocomoretângulo.
Casonosso Passarocolidacomalgum Cano,podemossimplesmente
cancelaro loopprincipal.Comotemosumavariável isRunningquecon-
trolao loop,paracancelá-lobastasetar isRunningpara false:
if(new VerificadorDeColisao(passaro, canos).temColisao()) {
isRunning = false ;
}
Aindanãotemosaclasse VerificadorDeColisao.Vamoscriá-lano
pacote engine.

## Página 74

CasadoCódigo
Comoprecisamosverificaracolisãoentreo Passaroeos Canos,vamos
receberessesobjetosnoconstrutordaclasse VerificadorDeColisao:
public class VerificadorDeColisao {
private final Passaro passaro;
private final Canos canos;
public VerificadorDeColisao(Passaro passaro, Canos canos) {
this.passaro = passaro;
this.canos = canos ;
}
public boolean temColisao() {
return canos.temColisaoCom(passaro);
}
}
Mascomoimplementaroalgoritmodecolisão?Precisamosconferirque
o Passaronãobateuemnenhumcano,portantodevemospassarporcada
umdoscanosdaclasse Canos:
public boolean temColisaoCom(Passaro passaro) {
for (Cano cano : canos) {
}
}
Seelenãobateremnenhumcano,nãotemcolisão:
public boolean temColisaoCom(Passaro passaro) {
for (Cano cano : canos) {
}
return false;
}
Mastemosquedescobrirseo Passarobateucomocanoatual.Paraisso
verificaremosseelecolidiuverticalmente ehorizontalmente:
public boolean temColisaoCom(Passaro passaro) {
for (Cano cano : canos) {
70

## Página 75

CasadoCódigo Capítulo9. Tratandocolisões
if (cano.temColisaoHorizontalCom(passaro)
&& cano.temColisaoVerticalCom(passaro)) {
return true;
}
}
return false;
}
Agorafaltaimplementarosdoismétodosdecolisãonaclasse Cano.
Para detectarmos uma colisão vertical entre oPassaro e o Cano
inferior, basta sabermos quando aborda do pássaro toca o topo do
cano. Ouseja,quandoaalturadopássaromaisseuraioformaiorquea
alturaDoCanoInferior.Lembre-seque,quantomaiorovalordaaltura,
maisbaixoestáoelemento!
Paraocanosuperior,aideiaésemelhante: precisamossaberquandoa
bordasuperiordopássarotocaabasedocanosuperior. Parapegarmosa
bordasuperiordopássarobastasubtrairo RAIOdasua altura.
Comisso,temosométodo temColisaoVerticalCom:
public boolean temColisaoVerticalCom( Passaro passaro) {
return passaro.getAltura() -
passaro.RAIO < this.alturaDoCanoSuperior
|| passaro.getAltura() + passaro.RAIO >
this.alturaDoCanoInferior;
}
Seadistânciaentrea posicaohorizontaldocanoeaposiç ão X(ho-
rizontal)dopássarofor menorqueoseu RAIO,sabemosquehouveuma
colisão.Ométodo temColisaoHorizontalComtemesseconteúdo:
public boolean temColisaoHorizontalCom(Passaro passaro) {
return this.posicao - passaro.X < passaro.RAIO;
}
Temosnosso VerificadorDeColisaopronto!Aobateremumcano,
oqueacontececomojogo?
71

## Página 76

9.1. Criandoateladegameover CasadoCódigo
9.1 C riando a tela de game over
Testamosojogoeelepararepentinamentequandoperdemos. Faltoualgo
maisbonitoaqui,umateladefimdejogo,de game over.Vamosmudarnossa
verificaçãodecolisãoparadesenharatelade game over:
if(new VerificadorDeColisao(passaro , canos).temColisao()) {
new GameOver(tela).desenhaNo(canvas);
isRunning = false ;
}
Nossatelade game overdeveserconstruídanopacote elementosetero
métododedesenhotradicional:
public class GameOver {
private final Tela tela;
public GameOver(Tela tela) {
this.tela = tela;
}
public void desenhaNo(Canvas canvas) {
}
}
Vamoscriarafontedotextode game over,umafontevermelha,comne-
gritoesombra,definidanaclasse Cores:
public static Paint getCorDoGameOver() {
Paint vermelho = new Paint();
vermelho.setColor(0xFFFF0000);
vermelho.setTextSize(50);
vermelho.setTypeface(Typeface.DEFAULT_BOLD);
vermelho.setShadowLayer(2, 3, 3, 0xFF000000);
return vermelho;
}
Partimosparaodesenhoemsi,primeiramentecolocandootextonomeio
datelaverticalmente( tela.getAltura() / 2),àesquerda:
72

## Página 77

CasadoCódigo Capítulo9. Tratandocolisões
private static final Paint VERMELHO = Cores.getCorDoGameOver();
public void desenhaNo(Canvas canvas) {
String gameOver = "Game Over";
canvas.drawText(gameOver, 0, tela.getAltura() / 2, VERMELHO);
}
73

## Página 78

9.1. Criandoateladegameover CasadoCódigo
Fig.9.1:Gameoverexibidonojogo.
74

## Página 79

CasadoCódigo Capítulo9. Tratandocolisões
9.2 C entralizando um texto horizontalmente
na tela
Onosso GameOverjáfuncionamasaindaprecisamoscentralizá-lonaho-
rizontal.Estejápassaaserumproblemaumpoucomaior.Paracentralizar
nahorizontaltemosquesaberquantootexto ”Game Over” ocupadatela
eissodependedotamanhodafonte,datelaetc.Felizmente,oobjeto Paint
podenosajudaredizerquantos pixelsserãonecessáriosparadesenharessa
Stringnatela.Comométodo getTextBoundsficamossabendoqualo
tamanhodoretânguloqueenglobatodaanossa String:
Rect limiteDoTexto = new Rect();
vermelho.getTextBounds(texto, 0, texto.length(), limiteDoTexto);
No método getTextBounds dizemos que queremos o retângulo (
limiteDoTexto)queenglobaa String( texto),quecome çanaposi-
ção 0eterminaem texto.length().
Comisso,nosso limiteDoTextopassaaseroretânguloquecontémas
dimensõesexatasdo texto(nocaso, ”Game Over”).Agora,bastadesco-
brirondeestáocentrohorizontaldesseretângulo;sesoubermosisso,pode-
moscentralizá-lohorizontalmentenatela.
Para encontrarmos o centro horizontal do nosso retângulo
limiteDoTexto, basta dividir seu tamanho horizontal por 2. Mas
qualéoseutamanhohorizontal?
Seutamanhohorizontaldependedeondeoretângulocome ça( left)e
ondeeleacaba( right).Bastafazer:
(limiteDoTexto.right - limiteDoTexto.left)/2
Agoraquetemosocentrohorizontaldoretângulo limiteDoTexto,
queremoscentralizá-lona telaeparaissovamosprecisardasualargura.
Casocoloquemosnossotexto começandonametadeda tela,elenãoes-
tarácentralizado(somenteaprimeiraletraestarárealmentenocentro);en-
tão,vamosencontrarocentrohorizontaldatelae “recuar” metade do nosso
retângulo. Issoalinharáocentrodoretângulocomocentrohorizontalda
tela:
75

## Página 80

9.2. Centralizandoumtextohorizontalmentenatela CasadoCódigo
int centroHorizontal = tela.getLargura()/2 -
(limiteDoTexto.right - limiteDoTexto.left)/2;
Comisso,nosso centralizaTextoficaráassim:
private int centralizaTexto(String texto) {
Rect limiteDoTexto = new Rect();
vermelho.getTextBounds(texto, 0, texto.length(),
limiteDoTexto);
int centroHorizontal = tela.getLargura()/2 -
(limiteDoTexto.right - limiteDoTexto .left)/2;
return centroHorizontal;
}
Precisamostambémcriaro getLarguranaclasse Tela,claro:
public int getLargura() {
return metrics .widthPixels;
}
Emandardesenharnossa Stringnocentrohorizontal:
public void desenhaNo(Canvas canvas) {
String gameOver = "Game Over";
int centroHorizontal = centralizaTexto(gameOver);
canvas.drawText(gameOver, centroHorizontal,
tela.getAltura()/2, VERMELHO);
}
Agorasimpodemosveroresultadofinal.
76

## Página 81

CasadoCódigo Capítulo9. Tratandocolisões
Fig.9.2:Gameoveréexibidocentralizadonatela.
77

## Página 83

Capítulo10
Aprimorandoo layoutdojogo
Agoraquetemostodaamecânicadojogofuncionandocorretamente,vamos
melhoraroaspectovisualdoselementosdoJumpersubstituindoocírculodo
Passaroeosretângulosdos Canosporimagensbonitas!
Vamosprecisardeumaimagempararepresentaro Passaro,masnãose
preocupe:todasasimagensqueusaremosjáestãono zipemhttps://github.
com/felipetorres/jumper-arquivos.
Tudooqueprecisamosfazeréutilizaressaimagemnonossojogopara
substituirocírculovermelho.Percebaquenossaimagemébasicamenteum
círculo,dessaformapodemosmantertodasascontasdetamanhoecolisão
inalteradas!
Para utilizar a imagem chamada passaro.png da pasta
drawable-nodpi, vamos chamar o método decodeResource da
classe BitmapFactory,damesmaformacomofizemosparaobackground:

## Página 84

CasadoCódigo
Bitmap bp = BitmapFactory.decodeResource(context.getResources(),
R.drawable.passaro);
Qualtamanhoessaimagemteránonossojogo?Seráqueé exatamenteo
mesmotamanhodocírculovermelho?Temosquetomarcuidadocomisso,
poisseaimagemformaior(oumenor)teremosproblemasnotratamentodas
colisões.
Paragarantirqueasdimensõessejamasmesmasdocírculo,noconstru-
tordaclasse Passarovamosredimensionarnossaimagemcomométodo
createScaledBitmapepassarasdimensõesquenossocírculotinha!
Bitmap bp = BitmapFactory.decodeResource(context.getResources(),
R.drawable.passaro);
this.passaro = Bitmap.createScaledBitmap(bp, RAIO*2, RAIO*2 ,
false);
Como precisamos de umContext para o getResources, basta
chamá-lonoconstrutordo Passaro.
Vejaquepassamos RAIO*2paraaalturaelarguradonovo bitmap.
Comonossocírculotinhaoraiodotamanho RAIO,sualarguraealturaeram
RAIO*2;agoranossaimagemtemasmesmasdimensõesqueocírculo.
Garantimosquenossaimagemestácomotamanhocorreto. Podemos
garantirqueessaimagemserádesenhadacomomesmoposicionamentodo
círculo?
Aolidarcomcírculos,usamososeucentrocomoreferênciadeposicio-
namento.Dissemosqueseucentroestarianaposiç ão(X, altura):
canvas.drawCircle(X, altura, RAIO, vermelho);
Porém,aolidarcomimagens(bitmaps),areferênciaparadesenhoéo
canto superior esquerdo.Logo,semantivermos(X, altura)paraseudesenho,
canvas.drawBitmap(passaro, X, altura, null );
teremosumaimagemdesalinhadacomaposiç ãooriginal.Paraarrumar
isso,vamos centralizaraimagemem(X, altura).Comoelatem RAIO*2de
alturaelargura,bastasubtrair RAIOdeambasascoordenadaseteremoso
bitmapcentralizado:
80

## Página 85

CasadoCódigo Capítulo10. Aprimorandoolayoutdojogo
canvas.drawBitmap(passaro, X-RAIO, altura-RAIO, null);
Vejacomoficaránossaaplicação:
Fig.10.1:Nossopássaroficoubemmelhor,não?
81

## Página 86

10.1. Substituindoosretângulosporbitmaps CasadoCódigo
10.1 Substituindo os retângulos por bitmaps
Vamosusaramesmaideiaanteriorparasubstituirosretângulosdos Canos
por bitmapsbonitos! Porém,emvezdepossuirumaimagempara todoo
cano,teremosapenasum“filete”,queseráesticadoparaomesmotamanho
dosretângulosiniciais.
Assim como feito noPassaro, na classeCanos vamos utilizar o
BitmapFactoryparapegaraimagem.Precisaremosdeum Contextem
seuconstrutor:
Bitmap bp = BitmapFactory.decodeResource( context.getResources(),
R.drawable.cano);
Paraocanoinferior,vamosredimensionaressefiletequeestáem bppara
otamanhocorreto.Vejaqueesseprocessoébemsimples,poisjátemosasdi-
mensõesguardadasem LARGURA_DO_CANOe alturaDoCanoInferior:
this.canoInferior = Bitmap.createScaledBitmap(bp,
LARGURA_DO_CANO, this.alturaDoCanoInferior, false);
Para desenhar esse canoInferior na tela, devemos alterar o
desenhaCanoInferiorNo.Atualmente,temososeguintecódigo:
private void desenhaCanoInferiorNo(Canvas canvas) {
canvas.drawRect(posicao, alturaDoCanoInferior,
posicao + LARGURA_DO_CANO, tela.getAltura(), VERDE);
}
Lembre-se que os dois primeiros valores dodrawRect represen-
tam ocanto superior esquerdo do retângulo. Da mesma forma que o
drawBitmap!Ouseja,aocontráriodo Passaro,noqualtivemosquefazer
umapequenacorre ção,paraos Canosjátemosessascoordenadasprontas!
canvas.drawBitmap(canoInferior, posicao, alturaDoCanoInferior,
null);
82

## Página 87

CasadoCódigo Capítulo10. Aprimorandoolayoutdojogo
Fig.10.2:Canosinferioresagorasãobitmapstambém.
Paraoscanossuperiores,vamosfazerdamesmaforma,porémnãotere-
mosqueutilizaro BitmapFactorynovamente,bastaredimensioná-lode
83

## Página 88

10.1. Substituindoosretângulosporbitmaps CasadoCódigo
acordocomosretângulossuperiores:
this.canoSuperior = Bitmap.createScaledBitmap(bp,
LARGURA_DO_CANO, this.alturaDoCanoSuperior, false);
Vamossubstituiro desenhaCanoSuperiorNo,ondechamávamoso
drawRect,pelo drawBitmap,masantesprecisaremosdacoordenadado
seucantosuperioresquerdo:
private void desenhaCanoSuperiorNo(Canvas canvas) {
canvas.drawRect(posicao, 0, posicao + LARGURA_DO_CANO,
alturaDoCanoSuperior, VERDE);
}
Comoesseretânguloestácomseucantosuperioresquerdoem(posicao,
0)teremosqueusaressamesmacoordenadaparanosso bitmap:
private void desenhaCanoSuperiorNo(Canvas canvas) {
canvas.drawBitmap(canoSuperior, posicao, 0, null);
}
Aotérmino,temosnossoJumperbemmaisbonitoesemnenhumamu-
dançadrásticanocódigo!
84

## Página 89

CasadoCódigo Capítulo10. Aprimorandoolayoutdojogo
Fig.10.3:AparênciadoJumpercomosbitmaps.
85

## Página 91

Capítulo11
Adicionandosomaojogo
Nossojogojáestábastantedivertido,comtodoonecessárioparadesafiaros
jogadores.Porémfaltaumapartecrucialdeumjogo:suamúsica.Penseem
todososprincipaisjogosdomercado,amaioriadelestemumatrilhasonora
ouatémesmoumsommarcantequecativaojogador.
NoJumpernãovamosfazertodootrabalhoaltamentecomplexodeum
engenheirodesom,masvamostersonsparaosprincipaismomentosdojogo,
comoopulodopássaro,acolisãoeaumentodapontuaç ão!
Paracolocarmosumsomemumaaplicaç ãoAndroid,aprimeirasolu-
çãoéutilizaraclasse MediaPlayerdopróprioAndroid.Essaclasseéinte-
ressantequandoprecisamoscriarformasmaiselaboradasdeinteraç ãocom
sons.Penseemumaplicativodemúsica:neletemososcontrolespara play,
stop, pause, avançaretc. Entretanto,emumjogonãoprecisamosdetodos
essescontroles;narealidadesóqueremostocarumsomdecurtaduraç ãoe,
nomáximo,umatrilhasonoraconstanteaofundo.

## Página 92

CasadoCódigo
Tendoemmenteessaestruturamaissimples,temosaclasse SoundPool,
cujoobjetivoéjustamentefornecerumaformamaisleveparatocarsonsde
curtaduraçãoidealparajogos!
Aoinstanciarum SoundPoolpodemospassar,noseuconstrutor,otipo
desomqueserátocado,alémdequantosarquivossimultâneospoderãoser
tocados.Comotemostrêssonspossíveis,setaremosessevalorpara 3:
SoundPool pool = new SoundPool(3, AudioManager.STREAM_MUSIC, 0);
Vamoscriarumaclasseresponsávelporgerenciaresse SoundPool.No
pacote engine,criaremosaclasse Som:
public class Som {
private SoundPool soundPool;
public Som() {
soundPool = new SoundPool(3, AudioManager.STREAM_MUSIC, 0);
}
}
Paratocarmosalgumsom,antesprecisaremoscarregá-locomométodo
load.Nele,passaremosoarquivodesom,quedeveráestarnapasta res/raw.
Seocarregamentoforfeitocomsucesso,o loadretornaráumidquedeverá
serusadosemprequequisermostocá-lo.
public class Som {
private SoundPool soundPool;
public static int PULO;
public Som(Context context) {
soundPool = new SoundPool(3, AudioManager.STREAM_MUSIC, 0);
PULO = soundPool.load(context, R.raw.pulo, 1);
}
}
Agoraquetemososom PULOcarregado,vamostocá-locomométodo
play,querecebeo iddosom,ovolumeesquerdo,volumedireitoe,porúl-
timo,avelocidadedosom(Lembre-se:1éavelocidadenormal).
88

## Página 93

CasadoCódigo Capítulo11. Adicionandosomaojogo
soundPool.play(idDoSom, 1, 1, 1, 0, 1);
Nanossaclasse Som,teremososeguintecódigo:
public class Som {
private SoundPool soundPool;
public static int PULO;
public Som(Context context) {
soundPool = new SoundPool(3, AudioManager.STREAM_MUSIC, 0);
PULO = soundPool.load(context, R.raw.pulo, 1);
}
public void play( int som) {
soundPool.play(som, 1, 1, 1, 0, 1);
}
}
Emqualmomentotocaremososomdopulodopássaro? Quandoo
Passaropular. Porém,emquallugardonossocódigotemosalógicado
pulo?Nométodo puladaclasse Passaro!
public class Passaro {
public void pula() {
if(altura > RAIO) {
som.play(Som.PULO);
altura -= 150;
}
}
}
Agora,bastarecebero Somnoconstrutordo Passaro:
private Som som;
public Passaro(Tela tela, Context context, Som som) {
this.som = som;
}
89

## Página 94

CasadoCódigo
Comomudamosoconstrutordo Passaro,quebramosaclasse Game,
queinstanciao Passaro.Naclasse Game,vamosinstanciaro Somepassar
parao Passaro:
public class Game extends SurfaceView implements Runnable,
OnTouchListener{
//Outras variáveis...
private Som som;
public Game(Context context) {
//...
this.som = new Som(context);
}
private void inicializaElementos() {
this.passaro = new Passaro(tela, context, som);
//...
}
//Outros métodos...
}
Comisso,nosso Passaroemitiráumsomacadapulo!
90